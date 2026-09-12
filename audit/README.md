# Cross-reference audit

`medtronic_skill_cross_reference_audit.xlsx` — every reference between the skill's own markdown
files, and from those files to bundled asset files, extracted and checked against the real
filesystem. See the workbook's own **Overview** and **Summary** sheets for the methodology and
headline results (as of the last regeneration: 645 references extracted, 0 broken, 828 bundled
assets checked with 100% covered directly or at the folder level).

## Regenerating

Run in order from this directory (each writes a `.json` intermediate the next step reads):

```bash
python extract_refs.py     # scans SKILL.md + references/*.md + README.md -> refs_raw.json
python build_coverage.py   # derives status + bundled-asset coverage -> refs_with_status.json, asset_coverage.json
python build_workbook.py   # builds medtronic_skill_cross_reference_audit.xlsx
python verify_formulas.py  # independently re-derives the workbook's Summary numbers, for a sanity check
```

Requires `openpyxl` (`pip install openpyxl`). The `.json` intermediates are gitignored — they're
build output, not source.

Re-run this whenever `SKILL.md`, `references/*.md`, or the bundled `assets/` tree change, to keep
the audit current.
