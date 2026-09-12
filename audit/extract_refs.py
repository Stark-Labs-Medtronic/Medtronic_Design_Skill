#!/usr/bin/env python3
"""Extract cross-references (MD-to-MD and MD-to-asset) from the Medtronic branding skill.

Reference styles, resolved in order of strictness:
  1. Formal markdown links/images `[text](path)` / `![alt](path)`: resolved literally,
     relative to the source file's own directory - exactly how a renderer resolves them.
     A miss here is a genuine broken link.
  2. Backtick-quoted path tokens containing "/": resolved the same literal way first.
     Several reference docs (asset-manifest.md's table, and prose in others) write
     asset/reference paths root-relative (e.g. "assets/icons/") rather than with the
     "../" a literal same-directory resolution would need - so on a literal miss, also
     try resolving against the skill root as a fallback before calling it broken.
  3. Bare filenames in backticks (no "/"): resolved by searching the whole skill
     (including the third-party Carbon crawl this time, since generic filenames like
     content.md/meta.json genuinely exist there) for a file with that exact name.
  4. Glob-style targets (contain "*"): validated by checking the parent directory
     exists, not the literal (unexpandable) filename.
  5. Targets ending in an archive-file extension (.zip/.docx/.pdf/.mov) that the skill's
     own docs describe as living in the separate, unbundled `Archive/` source zips: never
     expected to resolve inside this repo - flagged as "archive-only", not broken.
"""
import json
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_ROOT = os.path.join(REPO_ROOT, "medtronic-branding")
CARBON_ROOT = os.path.join(SKILL_ROOT, "assets", "third-party", "carbon-design-system")

# Manually reviewed exceptions: (source_file, raw_target) -> note. These are prose
# mentions that are not really broken file references at all (a hypothetical output
# filename, or a file explicitly documented as deliberately excluded from the crawl) -
# left in the sheet for transparency rather than silently dropped.
MANUAL_NOTES = {
    ("medtronic-branding/references/asset-manifest.md", "page.html"):
        "Not missing by accident - carbon-design-system.md documents raw page.html as "
        "deliberately excluded from the crawl (redundant with content.md, ~997MB).",
    ("medtronic-branding/references/ui-design-system-colors.md", "design-tokens.json"):
        "Not a reference to a bundled file - names a hypothetical output file a "
        "developer might generate from the pasted JSON tokens, per the surrounding prose.",
}

MD_FILES = [os.path.join(REPO_ROOT, "README.md"), os.path.join(SKILL_ROOT, "SKILL.md")]
for fn in sorted(os.listdir(os.path.join(SKILL_ROOT, "references"))):
    if fn.endswith(".md"):
        MD_FILES.append(os.path.join(SKILL_ROOT, "references", fn))

ASSET_EXTS = {
    ".svg", ".png", ".ico", ".ttf", ".css", ".html", ".ase", ".jpg", ".jpeg",
    ".gif", ".json", ".woff", ".woff2", ".otf", ".pdf", ".docx", ".zip", ".mp4", ".mov"
}
ARCHIVE_EXTS = {".zip", ".docx", ".pdf", ".mov"}

MD_LINK_RE = re.compile(r'(!)?\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
BACKTICK_RE = re.compile(r'`([^`]+)`')
PATH_LIKE_RE = re.compile(
    r'^(\.{0,2}/)?(assets|references|Archive)/[^\s`]+$'
    r'|^[A-Za-z0-9_.\-]+\.(md|svg|png|ico|ttf|css|html|ase|json|docx|pdf|zip)$'
)

# Full filename index, including the third-party crawl this time.
name_index = {}
for dirpath, dirnames, filenames in os.walk(SKILL_ROOT):
    for fn in filenames:
        name_index.setdefault(fn, []).append(os.path.join(dirpath, fn))
for fn in os.listdir(REPO_ROOT):
    full = os.path.join(REPO_ROOT, fn)
    if os.path.isfile(full):
        name_index.setdefault(fn, []).append(full)


def rel(path):
    return os.path.relpath(path, REPO_ROOT).replace("\\", "/")


def classify(resolved_rel, raw_target):
    ext = os.path.splitext(resolved_rel.split("*")[0])[1].lower()
    if raw_target.startswith(("http://", "https://", "mailto:")):
        return "external"
    if ext == ".md":
        return "md"
    if ext in ASSET_EXTS or "/assets/" in ("/" + resolved_rel.replace("\\", "/")):
        return "asset"
    return "other"


def resolve_path_token(base_dir, target_clean):
    """Try literal (relative-to-file), then root-relative fallback, then glob-parent."""
    is_glob = "*" in target_clean
    literal = os.path.normpath(os.path.join(base_dir, target_clean))
    if is_glob:
        parent = os.path.dirname(literal)
        if os.path.isdir(parent):
            return rel(literal), True, "glob pattern - parent directory exists"
        # try root-relative parent too
        root_literal = os.path.normpath(os.path.join(SKILL_ROOT, target_clean))
        root_parent = os.path.dirname(root_literal)
        if os.path.isdir(root_parent):
            return rel(root_literal), True, "glob pattern - parent exists (root-relative)"
        return rel(literal), False, "glob pattern - parent directory NOT found"
    if os.path.exists(literal):
        return rel(literal), True, "literal (relative to source file)"
    # root-relative fallback (common in prose that assumes skill-root-relative paths)
    root_literal = os.path.normpath(os.path.join(SKILL_ROOT, target_clean))
    if os.path.exists(root_literal):
        return rel(root_literal), True, "resolved via root-relative fallback (not a literal same-dir path)"
    # third-party-crawl-root-relative fallback (asset-manifest.md describes some crawl
    # subfolders, e.g. "assets/pictograms/", relative to the crawl root, not skill root)
    carbon_literal = os.path.normpath(os.path.join(CARBON_ROOT, target_clean))
    if os.path.exists(carbon_literal):
        return rel(carbon_literal), True, "resolved relative to the Carbon crawl root (assets/third-party/carbon-design-system/)"
    ext = os.path.splitext(target_clean)[1].lower()
    if ext in ARCHIVE_EXTS:
        return rel(literal), False, "archive-only: lives in the separate, unbundled Archive/ source zips"
    return rel(literal), False, "NOT FOUND"


rows = []

for f in MD_FILES:
    with open(f, encoding="utf-8") as fh:
        text = fh.read()
    src_rel = rel(f)
    base_dir = os.path.dirname(f)

    def add_row(ref_kind, syntax, link_text, raw_target, resolved_rel, category, exists, note=""):
        rows.append({
            "source_file": src_rel, "ref_kind": ref_kind, "syntax": syntax,
            "link_text": link_text, "raw_target": raw_target,
            "resolved_path": resolved_rel, "category": category,
            "exists": exists, "note": note,
        })

    for m in MD_LINK_RE.finditer(text):
        is_image = bool(m.group(1))
        link_text, target = m.group(2), m.group(3)
        if target.startswith(("http://", "https://", "mailto:")):
            add_row("image" if is_image else "link", "markdown", link_text, target, target, "external", True, "external URL")
            continue
        target_clean = target.split("#")[0].strip()
        if not target_clean:
            continue
        rr, exists, note = resolve_path_token(base_dir, target_clean)
        kind = classify(rr, target)
        add_row("image" if is_image else "link", "markdown", link_text, target, rr, kind, exists, note)

    text_no_links = MD_LINK_RE.sub(" ", text)
    for m in BACKTICK_RE.finditer(text_no_links):
        token = m.group(1).strip()
        if not token or " " in token or "\n" in token:
            continue
        if not PATH_LIKE_RE.match(token):
            continue
        target_clean = token.split("#")[0]
        if "/" in target_clean:
            rr, exists, note = resolve_path_token(base_dir, target_clean)
            kind = classify(rr, token)
            add_row("prose", "backtick (path)", token, token, rr, kind, exists, note)
        else:
            matches = name_index.get(target_clean, [])
            ext = os.path.splitext(target_clean)[1].lower()
            kind = "md" if ext == ".md" else ("asset" if ext in ASSET_EXTS else "other")
            if len(matches) == 1:
                add_row("prose", "backtick (bare name)", token, token, rel(matches[0]), kind, True,
                        "resolved by unique filename match")
            elif len(matches) > 1:
                add_row("prose", "backtick (bare name)", token, token,
                        rel(matches[0]), kind, True,
                        f"common filename, {len(matches)} files share this name "
                        f"(also at: {', '.join(rel(p) for p in matches[1:])})")
            else:
                if ext in ARCHIVE_EXTS:
                    add_row("prose", "backtick (bare name)", token, token, "", kind, False,
                            "archive-only: lives in the separate, unbundled Archive/ source zips")
                else:
                    add_row("prose", "backtick (bare name)", token, token, "", kind, False,
                            "NOT FOUND anywhere in the skill")

for r in rows:
    key = (r["source_file"], r["raw_target"])
    if key in MANUAL_NOTES and r["exists"] is False:
        r["note"] = MANUAL_NOTES[key]

with open(os.path.join(os.path.dirname(__file__), "refs_raw.json"), "w", encoding="utf-8") as out:
    json.dump(rows, out, indent=2)

archive_only = sum(1 for r in rows if "archive-only" in r["note"])
manually_reviewed = sum(1 for r in rows if (r["source_file"], r["raw_target"]) in MANUAL_NOTES and r["exists"] is False)
truly_broken = [
    r for r in rows
    if r["exists"] is False and "archive-only" not in r["note"]
    and (r["source_file"], r["raw_target"]) not in MANUAL_NOTES
]

print(f"Extracted {len(rows)} references from {len(MD_FILES)} markdown files.")
for cat in ("md", "asset", "external", "other"):
    print(f"  category={cat}: {sum(1 for r in rows if r['category']==cat)}")
print(f"  archive-only (expected, not bundled): {archive_only}")
print(f"  manually reviewed non-bugs: {manually_reviewed}")
print(f"  TRULY BROKEN: {len(truly_broken)}")
for r in truly_broken:
    print("   ", r["source_file"], "|", r["raw_target"], "|", r["note"])
