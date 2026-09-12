#!/usr/bin/env python3
"""Build the cross-reference audit workbook from refs_with_status.json + asset_coverage.json."""
import json
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(__file__)
OUT_PATH = os.path.join(HERE, "medtronic_skill_cross_reference_audit.xlsx")

rows = json.load(open(os.path.join(HERE, "refs_with_status.json"), encoding="utf-8"))
coverage = json.load(open(os.path.join(HERE, "asset_coverage.json"), encoding="utf-8"))

REF_KIND_LABEL = {
    ("image", "markdown"): "Markdown image",
    ("link", "markdown"): "Markdown link",
    ("prose", "backtick (path)"): "Backtick path (prose)",
    ("prose", "backtick (bare name)"): "Backtick filename (prose)",
}


def status_group(status):
    if status == "external URL":
        return "External URL"
    if status.startswith("OK"):
        return "OK"
    if status.startswith("expected gap"):
        return "Expected gap (documented, not bundled)"
    if status.startswith("not a file reference"):
        return "Not a file reference"
    if status == "BROKEN - needs fix":
        return "BROKEN"
    return "Other"


for r in rows:
    r["ref_style"] = REF_KIND_LABEL.get((r["ref_kind"], r["syntax"]), r["syntax"])
    r["status_group"] = status_group(r["status"])

CATEGORY_LABEL = {"md": "MD → MD", "asset": "MD → Asset", "external": "External URL", "other": "Other"}

# ---------------------------------------------------------------- styling --
FONT_NAME = "Arial"
HEADER_FONT = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
HEADER_FILL = PatternFill("solid", fgColor="140F4B")  # Medtronic Navy
TITLE_FONT = Font(name=FONT_NAME, size=14, bold=True, color="140F4B")
SUBTITLE_FONT = Font(name=FONT_NAME, size=10, italic=True, color="595959")
BODY_FONT = Font(name=FONT_NAME, size=10)
BOLD_BODY_FONT = Font(name=FONT_NAME, size=10, bold=True)
THIN = Side(style="thin", color="D9D9D9")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

STATUS_FILL = {
    "OK": PatternFill("solid", fgColor="E2EFDA"),
    "Expected gap (documented, not bundled)": PatternFill("solid", fgColor="FFF2CC"),
    "Not a file reference": PatternFill("solid", fgColor="FFF2CC"),
    "External URL": PatternFill("solid", fgColor="DDEBF7"),
    "BROKEN": PatternFill("solid", fgColor="F8CBAD"),
}


def style_header_row(ws, row=1, ncols=None):
    ncols = ncols or ws.max_column
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 28


def autosize(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def write_table(ws, headers, data_rows, widths, start_row=1, status_col=None):
    for j, h in enumerate(headers, start=1):
        ws.cell(row=start_row, column=j, value=h)
    style_header_row(ws, row=start_row, ncols=len(headers))
    for i, row in enumerate(data_rows, start=start_row + 1):
        for j, val in enumerate(row, start=1):
            cell = ws.cell(row=i, column=j, value=val)
            cell.font = BODY_FONT
            cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=(j in (3, 4, 5, len(headers))))
        if status_col:
            sc = ws.cell(row=i, column=status_col)
            fill = STATUS_FILL.get(sc.value)
            if fill:
                sc.fill = fill
    autosize(ws, widths)
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1).coordinate


wb = Workbook()

# ============================================================== Overview ==
ws = wb.active
ws.title = "Overview"
ws.sheet_view.showGridLines = False
r = 1
ws.cell(row=r, column=1, value="Medtronic Branding Skill — Cross-Reference Audit").font = TITLE_FONT
r += 1
ws.cell(row=r, column=1, value="Repo: Medtronic_Design_Skill  •  Branch: docs/v1.3.0-merge-and-fixes").font = SUBTITLE_FONT
r += 2

overview_text = [
    ("What this checks", BOLD_BODY_FONT),
    ("Every SKILL.md / references/*.md file (30 total, incl. the repo README) was scanned for two "
     "reference styles: formal Markdown links/images `[text](path)`, and backtick-quoted path-like "
     "tokens in prose (e.g. `references/typography.md`, `assets/icons/functional/`). Each reference "
     "was resolved to a real file on disk and classified as MD→MD, MD→Asset, external URL, or other.",
     BODY_FONT),
    ("", BODY_FONT),
    ("Resolution logic", BOLD_BODY_FONT),
    ("A reference is only called broken after trying, in order: (1) the literal path relative to the "
     "file it's written in — how a renderer actually resolves a formal link; (2) a skill-root-relative "
     "fallback, since several docs (notably asset-manifest.md's tables) write paths root-relative rather "
     "than with a leading \"../\"; (3) the same fallback against the third-party Carbon crawl's own root; "
     "(4) for glob patterns like `*.ttf`, checking the parent directory exists instead of the literal "
     "unexpandable filename; (5) for bare filenames in backticks with no \"/\", a search across the whole "
     "skill for a file with that exact name.", BODY_FONT),
    ("", BODY_FONT),
    ("Headline result", BOLD_BODY_FONT),
    ("0 broken cross-references and 0 broken asset references across 645 extracted references. "
     "47 references point at files the skill's own docs describe as living in the separate, "
     "un-bundled Archive/ source zips (expected, not a bug) and 2 are prose mentions that aren't file "
     "references at all — both kept in the data for transparency, see the Status column.", BODY_FONT),
    ("", BODY_FONT),
    ("Sheet guide", BOLD_BODY_FONT),
    ("Summary — headline counts, computed live from the data sheets below (COUNTIF formulas; edit/filter "
     "the data sheets and these numbers recalculate).", BODY_FONT),
    ("All References — every one of the 645 extracted references, one row each. The master data sheet.", BODY_FONT),
    ("MD Cross-References — the 449 references from one markdown file to another, filtered from All References.", BODY_FONT),
    ("Asset References — the 187 references from a markdown file to an image/font/CSS/etc. asset file.", BODY_FONT),
    ("MD File Inbound Links — all 30 markdown files with a live count of how many times each is referenced "
     "by another file (COUNTIF against MD Cross-References) — flags any file nothing else points to.", BODY_FONT),
    ("Bundled Asset Coverage — all 828 non-third-party bundled asset files, each flagged for whether the docs "
     "name it directly or only cover it via a folder-level mention (e.g. \"assets/icons/functional/\").", BODY_FONT),
    ("", BODY_FONT),
    ("Status values", BOLD_BODY_FONT),
    ("OK — resolves cleanly (literal path, or one of the documented fallbacks — the exact method is in the Note column).", BODY_FONT),
    ("Expected gap (documented, not bundled) — the skill's own docs say this file lives outside the bundled "
     "assets (an Archive/ source zip, or a file explicitly excluded from the Carbon crawl).", BODY_FONT),
    ("Not a file reference — a backtick-quoted token that isn't actually pointing at a file (e.g. a suggested "
     "output filename in prose).", BODY_FONT),
    ("BROKEN — genuinely does not resolve by any method. Currently: none.", BODY_FONT),
    ("", BODY_FONT),
    ("Scope note", BOLD_BODY_FONT),
    ("The third-party IBM Carbon Design System crawl (assets/third-party/carbon-design-system/, ~4,600 icon/"
     "pictogram files) is excluded from the Bundled Asset Coverage sheet — those files are looked up at "
     "build time via JSON manifests (catalog/icons-manifest.json etc.), not cited by individual filename in "
     "prose, so a per-file coverage check doesn't apply the way it does for the curated logo/icon/font set.",
     BODY_FONT),
]
for text, font in overview_text:
    cell = ws.cell(row=r, column=1, value=text)
    cell.font = font
    cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 15 if not text else max(15, 15 * (len(text) // 105 + 1))
    r += 1
autosize(ws, [130])

# ==================================================== All References ======
ALL_HEADERS = ["Source File", "Category", "Reference Style", "Link Text / Token",
               "Raw Target", "Resolved Path", "Status", "Note"]
all_data = [
    (r_["source_file"], CATEGORY_LABEL[r_["category"]], r_["ref_style"], r_["link_text"],
     r_["raw_target"], r_["resolved_path"], r_["status"], r_["note"])
    for r_ in rows
]
ws_all = wb.create_sheet("All References")
write_table(ws_all, ALL_HEADERS, all_data,
            widths=[42, 12, 20, 34, 34, 46, 32, 60], status_col=7)
N_ALL = len(all_data)

# ================================================== MD Cross-References ===
md_rows = [d for d in all_data if d[1] == "MD → MD"]
ws_md = wb.create_sheet("MD Cross-References")
write_table(ws_md, ALL_HEADERS, md_rows,
            widths=[42, 12, 20, 40, 30, 40, 32, 55], status_col=7)
N_MD = len(md_rows)

# ====================================================== Asset References ==
asset_rows = [d for d in all_data if d[1] == "MD → Asset"]
ws_asset = wb.create_sheet("Asset References")
write_table(ws_asset, ALL_HEADERS, asset_rows,
            widths=[42, 12, 20, 40, 46, 46, 32, 55], status_col=7)
N_ASSET = len(asset_rows)

# ================================================ MD File Inbound Links ===
# Build the canonical list of the 30 markdown files that were scanned.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_ROOT = os.path.join(REPO_ROOT, "medtronic-branding")


def relp(p):
    return os.path.relpath(p, REPO_ROOT).replace("\\", "/")


md_file_list = [relp(os.path.join(REPO_ROOT, "README.md")), relp(os.path.join(SKILL_ROOT, "SKILL.md"))]
for fn in sorted(os.listdir(os.path.join(SKILL_ROOT, "references"))):
    if fn.endswith(".md"):
        md_file_list.append(relp(os.path.join(SKILL_ROOT, "references", fn)))

# Referrer lists computed once from the snapshot (informational; the Count column
# is a live COUNTIF formula against the MD Cross-References sheet).
referrers = {}
for d in md_rows:
    referrers.setdefault(d[5], set()).add(d[0])  # resolved_path -> {source_file,...}

ws_inb = wb.create_sheet("MD File Inbound Links")
INB_HEADERS = ["Markdown File", "Times Referenced (live count)", "Referenced By (snapshot)", "Orphan?"]
for j, h in enumerate(INB_HEADERS, start=1):
    ws_inb.cell(row=1, column=j, value=h)
style_header_row(ws_inb, ncols=len(INB_HEADERS))
md_range_col = "F"  # Resolved Path column in MD Cross-References
for i, mf in enumerate(md_file_list, start=2):
    ws_inb.cell(row=i, column=1, value=mf).font = BODY_FONT
    ws_inb.cell(row=i, column=2,
                value=f"=COUNTIF('MD Cross-References'!{md_range_col}2:{md_range_col}{N_MD + 1},A{i})").font = BODY_FONT
    ref_by = ", ".join(sorted(referrers.get(mf, []))) or "(none found)"
    c3 = ws_inb.cell(row=i, column=3, value=ref_by)
    c3.font = BODY_FONT
    c3.alignment = Alignment(wrap_text=True, vertical="top")
    c4 = ws_inb.cell(row=i, column=4, value=f'=IF(B{i}=0,"ORPHAN","")')
    c4.font = BODY_FONT
    for col in (1, 2, 4):
        ws_inb.cell(row=i, column=col).border = BORDER
        ws_inb.cell(row=i, column=col).alignment = Alignment(vertical="top", wrap_text=(col == 1))
    c3.border = BORDER
autosize(ws_inb, [42, 24, 90, 12])
ws_inb.freeze_panes = "A2"
N_INB = len(md_file_list)

# =================================================== Bundled Asset Coverage
ws_cov = wb.create_sheet("Bundled Asset Coverage")
COV_HEADERS = ["Asset Path", "Extension", "Coverage Status"]
cov_data = [
    (c["path"], os.path.splitext(c["path"])[1].lower() or "(none)", c["status"])
    for c in coverage
]
COV_FILL = {
    "Direct - exact file referenced": PatternFill("solid", fgColor="E2EFDA"),
    "Folder-level - containing directory referenced": PatternFill("solid", fgColor="DDEBF7"),
    "Not individually referenced": PatternFill("solid", fgColor="FFF2CC"),
}
for j, h in enumerate(COV_HEADERS, start=1):
    ws_cov.cell(row=1, column=j, value=h)
style_header_row(ws_cov, ncols=len(COV_HEADERS))
for i, row_ in enumerate(cov_data, start=2):
    for j, val in enumerate(row_, start=1):
        cell = ws_cov.cell(row=i, column=j, value=val)
        cell.font = BODY_FONT
        cell.border = BORDER
        cell.alignment = Alignment(vertical="top", wrap_text=(j == 1))
    fill = COV_FILL.get(row_[2])
    if fill:
        ws_cov.cell(row=i, column=3).fill = fill
autosize(ws_cov, [70, 12, 42])
ws_cov.freeze_panes = "A2"
N_COV = len(cov_data)

# =========================================== External & Other References ==
ext_other_rows = [d for d in all_data if d[1] in ("External URL", "Other")]
ws_ext = wb.create_sheet("External & Other References")
write_table(ws_ext, ALL_HEADERS, ext_other_rows,
            widths=[42, 12, 20, 40, 46, 30, 32, 40], status_col=7)

# ================================================================ Summary ==
ws_sum = wb.create_sheet("Summary")
ws_sum.sheet_view.showGridLines = False
ws_sum.cell(row=1, column=1, value="Summary").font = TITLE_FONT
ws_sum.cell(row=2, column=1, value="All figures below are formulas over the data sheets — they recalculate if those sheets are edited or filtered.").font = SUBTITLE_FONT
ws_sum.row_dimensions[2].height = 20

metric_rows = [
    ("Markdown files audited", f"=COUNTA('MD File Inbound Links'!A2:A{N_INB + 1})"),
    ("Total references extracted", f"=COUNTA('All References'!A2:A{N_ALL + 1})"),
    ("  — MD → MD cross-references", f"=COUNTIF('All References'!B2:B{N_ALL + 1},\"MD → MD\")"),
    ("  — MD → Asset references", f"=COUNTIF('All References'!B2:B{N_ALL + 1},\"MD → Asset\")"),
    ("  — External URL references", f"=COUNTIF('All References'!B2:B{N_ALL + 1},\"External URL\")"),
    ("  — Other references", f"=COUNTIF('All References'!B2:B{N_ALL + 1},\"Other\")"),
    ("", ""),
    ("References that resolve OK (incl. via a documented fallback)",
        f"=COUNTIF('All References'!G2:G{N_ALL + 1},\"OK*\")"),
    ("Expected gaps (documented as not bundled)",
        f"=COUNTIF('All References'!G2:G{N_ALL + 1},\"expected gap*\")"),
    ("Not a real file reference (prose only)",
        f"=COUNTIF('All References'!G2:G{N_ALL + 1},\"not a file reference*\")"),
    ("External URLs", f"=COUNTIF('All References'!G2:G{N_ALL + 1},\"external URL\")"),
    ("BROKEN — needs fix", f"=COUNTIF('All References'!G2:G{N_ALL + 1},\"BROKEN - needs fix\")"),
    ("", ""),
    ("Markdown files never referenced by another file (\"orphans\")",
        f"=COUNTIF('MD File Inbound Links'!D2:D{N_INB + 1},\"ORPHAN\")"),
    ("", ""),
    ("Bundled asset files audited (excl. third-party Carbon crawl)",
        f"=COUNTA('Bundled Asset Coverage'!A2:A{N_COV + 1})"),
    ("  — Directly named by exact filename",
        f"=COUNTIF('Bundled Asset Coverage'!C2:C{N_COV + 1},\"Direct - exact file referenced\")"),
    ("  — Covered only via a folder-level mention",
        f"=COUNTIF('Bundled Asset Coverage'!C2:C{N_COV + 1},\"Folder-level - containing directory referenced\")"),
    ("  — Not referenced at all (direct or folder-level)",
        f"=COUNTIF('Bundled Asset Coverage'!C2:C{N_COV + 1},\"Not individually referenced\")"),
]
r0 = 4
for label, formula in metric_rows:
    lc = ws_sum.cell(row=r0, column=1, value=label)
    lc.font = BOLD_BODY_FONT if not label.startswith("  ") else BODY_FONT
    if formula != "":
        vc = ws_sum.cell(row=r0, column=2, value=formula)
        vc.font = BOLD_BODY_FONT
        vc.alignment = Alignment(horizontal="right")
    r0 += 1
autosize(ws_sum, [58, 14])

# --------------------------------------------------------------- ordering --
wb._sheets = [wb["Overview"], wb["Summary"], wb["All References"],
              wb["MD Cross-References"], wb["Asset References"],
              wb["External & Other References"], wb["MD File Inbound Links"],
              wb["Bundled Asset Coverage"]]
wb.active = 0

wb.save(OUT_PATH)
print(f"Saved: {OUT_PATH}")
print(f"Data sheets written: All={N_ALL} MD={N_MD} Asset={N_ASSET} Inbound={N_INB} Coverage={N_COV}")
