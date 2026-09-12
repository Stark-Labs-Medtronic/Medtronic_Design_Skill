#!/usr/bin/env python3
"""Compute bundled-asset coverage (excluding the third-party Carbon crawl) and a
derived per-row status for refs_raw.json, ready for the workbook builder."""
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_ROOT = os.path.join(REPO_ROOT, "medtronic-branding")
ASSETS_ROOT = os.path.join(SKILL_ROOT, "assets")
THIRD_PARTY = os.path.join(ASSETS_ROOT, "third-party")

HERE = os.path.dirname(__file__)
rows = json.load(open(os.path.join(HERE, "refs_raw.json"), encoding="utf-8"))


def status_for(r):
    if r["category"] == "external":
        return "external URL"
    if r["exists"]:
        if r["note"].startswith("literal"):
            return "OK"
        return "OK (" + r["note"] + ")"
    if "archive-only" in r["note"]:
        return "expected gap - not bundled (Archive/ source zips)"
    if r["source_file"] == "medtronic-branding/references/asset-manifest.md" and r["raw_target"] == "page.html":
        return "expected gap - deliberately excluded from crawl"
    if r["raw_target"] == "design-tokens.json":
        return "not a file reference (hypothetical output name)"
    return "BROKEN - needs fix"


for r in rows:
    r["status"] = status_for(r)

broken = [r for r in rows if r["status"] == "BROKEN - needs fix"]
print(f"Rows with status BROKEN - needs fix: {len(broken)}")

with open(os.path.join(HERE, "refs_with_status.json"), "w", encoding="utf-8") as out:
    json.dump(rows, out, indent=2)

# --- Bundled asset coverage (excludes assets/third-party/) -----------------
referenced_files = set()
referenced_dirs = set()

for r in rows:
    if r["category"] != "asset":
        continue
    rp = r["resolved_path"]
    if not rp or rp.startswith("medtronic-branding/assets/third-party"):
        continue
    is_glob = "glob pattern" in r["note"] or "*" in rp
    is_dir_ref = (
        r["raw_target"].rstrip().endswith("/")
        or is_glob
        or os.path.isdir(os.path.join(REPO_ROOT, rp))
    )
    if is_dir_ref:
        referenced_dirs.add((os.path.dirname(rp) if is_glob else rp).rstrip("/"))
    else:
        referenced_files.add(rp)
        referenced_dirs.add(os.path.dirname(rp))

def rel(p):
    return os.path.relpath(p, REPO_ROOT).replace("\\", "/")

coverage_rows = []
for dirpath, dirnames, filenames in os.walk(ASSETS_ROOT):
    if os.path.commonpath([dirpath, THIRD_PARTY]) == THIRD_PARTY:
        dirnames[:] = []
        continue
    for fn in sorted(filenames):
        full = os.path.join(dirpath, fn)
        rr = rel(full)
        d = rel(dirpath)
        if rr in referenced_files:
            coverage_rows.append({"path": rr, "status": "Direct - exact file referenced"})
        elif d in referenced_dirs:
            coverage_rows.append({"path": rr, "status": "Folder-level - containing directory referenced"})
        else:
            # check ancestor directories too (a reference two levels up still "covers" contextually
            # only note it if the immediate parent isn't already covered - ancestors rarely apply here)
            coverage_rows.append({"path": rr, "status": "Not individually referenced"})

coverage_rows.sort(key=lambda r: r["path"])
with open(os.path.join(HERE, "asset_coverage.json"), "w", encoding="utf-8") as out:
    json.dump(coverage_rows, out, indent=2)

print(f"Bundled (non-third-party) asset files: {len(coverage_rows)}")
by_status = {}
for r in coverage_rows:
    by_status[r["status"]] = by_status.get(r["status"], 0) + 1
for k, v in by_status.items():
    print(f"  {k}: {v}")
