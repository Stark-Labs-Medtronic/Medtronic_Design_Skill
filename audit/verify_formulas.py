#!/usr/bin/env python3
"""LibreOffice isn't installed in this environment, so recalc.py can't run.
Independently re-derive, in Python, exactly what every Summary/Inbound-Links
formula should evaluate to, so the formulas can be sanity-checked by hand
against numbers computed a completely different way (direct aggregation
over the same source data, not by re-reading the formula strings)."""
import fnmatch
import json
import os

HERE = os.path.dirname(__file__)
rows = json.load(open(os.path.join(HERE, "refs_with_status.json"), encoding="utf-8"))
coverage = json.load(open(os.path.join(HERE, "asset_coverage.json"), encoding="utf-8"))

MD_FILES = sorted({r["source_file"] for r in rows})
md_rows = [r for r in rows if r["category"] == "md"]
asset_rows = [r for r in rows if r["category"] == "asset"]
other_rows = [r for r in rows if r["category"] in ("other", "external")]


def countif(seq, pattern):
    return sum(1 for s in seq if fnmatch.fnmatchcase(s, pattern))


print("=== Summary sheet expected values ===")
print("Markdown files audited:", len(MD_FILES))
print("Total references extracted:", len(rows))
print("  MD-to-MD:", len(md_rows))
print("  MD-to-asset:", len(asset_rows))
print("  Other/external:", len(other_rows))
statuses = [r["status"] for r in rows]
print("References resolving OK:", countif(statuses, "OK*"))
print("Expected gaps:", countif(statuses, "expected gap*"))
print("Not a file reference:", countif(statuses, "not a file reference*"))
print("External URLs:", countif(statuses, "external URL"))
print("BROKEN:", countif(statuses, "BROKEN*"))
print("  (OK+gap+notref+external+broken should == total):",
      countif(statuses, "OK*") + countif(statuses, "expected gap*") +
      countif(statuses, "not a file reference*") + countif(statuses, "external URL") +
      countif(statuses, "BROKEN*"), "vs", len(rows))

print()
print("Bundled asset files audited:", len(coverage))
cov_statuses = [c["status"] for c in coverage]
print("  Direct:", countif(cov_statuses, "Direct*"))
print("  Folder-level:", countif(cov_statuses, "Folder-level*"))
print("  Not individually referenced:", countif(cov_statuses, "Not individually*"))

print()
print("=== MD File Inbound Links (SUMPRODUCT equivalent) expected values ===")
inbound = {}
for r in md_rows:
    if r["status"].startswith("OK"):
        inbound[r["resolved_path"]] = inbound.get(r["resolved_path"], 0) + 1
orphans = 0
for f in MD_FILES:
    n = inbound.get(f, 0)
    is_entry = "SKILL.md" in f or "README.md" in f
    flag = "" if n > 0 or is_entry else "ORPHAN"
    if flag == "ORPHAN":
        orphans += 1
    print(f"  {n:3d}  {flag:8s}  {f}")
print("Orphan count:", orphans)
