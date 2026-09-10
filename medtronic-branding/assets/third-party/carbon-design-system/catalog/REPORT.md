# Carbon Design System — Crawl & Asset Extraction Report

Generated: 2026-09-05T10:58:57.929Z

## Scope

- Primary crawl target: `carbondesignsystem.com` / `www.carbondesignsystem.com` (all pages reachable from the sitemap and in-site navigation).
- Interactive/client-rendered content (icon & pictogram libraries) was rendered and scroll-revealed with Playwright to capture the full inline SVG set, not just the initial HTML.
- External sites were **recorded, not crawled** — see "Official external resources" below.

## Pages

- Crawled successfully: **356**
- Failed (after retries): **0**
- Total unique URLs visited: **356**

### Broken links discovered in source content

33 in-scope URLs were linked from real pages but resolve to Carbon's 404 page — these are dead links in the *source site's* content (typos, stale paths, malformed markdown), not crawler failures. They were still fetched and are recorded (with their referring context recoverable via `crawl.log`) in `catalog/broken-links.json`, but should not be treated as real content pages.

## Assets collected (original formats preserved)

| Type | Files | Size |
|---|---|---|
| Icons (SVG, from Elements → Icons library) | 2739 | 1.7 MB |
| Pictograms (SVG, from Elements → Pictograms library) | 1565 | 2.7 MB |
| Images (PNG/JPG/WebP/etc. referenced in page content) | 2001 | 59.5 MB |
| Documents (PDF/ZIP/design-tool artifacts, e.g. color palettes) | 4 | 8.6 MB |
| Fonts (woff/woff2/ttf/otf) | 0 | 0 B |
| Videos | 12 | 56.0 MB |
| Data (llms.txt, MCP agent instructions/prompts) | 3 | 44.7 KB |
| **Total** | 6324 | 128.6 MB |

All assets are deduplicated by content hash (see `catalog/asset-index.json`) — identical files referenced from multiple pages are stored once.

## AI/agent-facing resources (high relevance for a future design skill)

The site publishes a small set of files aimed specifically at AI tooling (an `llms.txt` index and a Carbon MCP server with agent instructions/prompts). These were captured and are worth reading first when building the design skill:

- **output/assets/data/llms.txt** — Official LLM-readable site index (llms.txt standard) — curated summary of Carbon's IA with descriptions per section
- **output/assets/data/GUIDELINES.txt** — Carbon MCP: system instructions for an AI agent ("Figma Make") generating Carbon v11 code
- **output/assets/data/figma-make-user-prompt.txt** — Carbon MCP: example user prompt template for Figma-to-code generation with Carbon
- **output/assets/documents/carbon-mcp-claude-extension.mcpb** — Packaged Carbon MCP server extension for Claude
- **output/assets/documents/carbon-builder.zip** — Carbon builder tool bundle

Note: `llms.txt` describes an in-progress site restructuring (`/foundations/...` paths) that does not yet match the live site's current URLs (`/elements/...`) crawled here — treat it as a forward-looking map, not a literal link index.

## External resources recorded (not crawled)

Links to other domains found on in-scope pages were catalogued in `catalog/external-resources.json`, grouped by category:

| Category | Distinct URLs |
|---|---|
| github | 521 |
| other | 445 |
| storybook-react | 132 |
| ibm | 119 |
| storybook-web-components | 45 |
| storybook-angular-community | 43 |
| storybook-vue-community | 41 |
| figma | 36 |
| npm | 21 |
| social | 19 |
| carbon-charts | 1 |

### Notable official resources not deep-crawled this phase

These are legitimate parts of the Carbon ecosystem but live outside `carbondesignsystem.com` and were intentionally left for a later, explicitly-scoped crawl rather than followed automatically:

- **react.carbondesignsystem.com** — React component Storybook (live demos, controls, API docs per component)
- **web-components.carbondesignsystem.com** — Web Components Storybook
- **angular.carbondesignsystem.com** — Angular (community) Storybook
- **vue.carbondesignsystem.com** — Vue (community) Storybook
- **charts.carbondesignsystem.com** — Carbon Charts documentation site
- **preview.carbondesignsystem.com** — Redesigned preview of the main Carbon site (banner-linked)
- **github.com/carbon-design-system/*** — Source repos: carbon, carbon-website, carbon-charts, etc.
- **figma.com (community files)** — Official Figma UI kit, type sets, color & icon/pictogram libraries
- **npmjs.com** — Published packages (@carbon/react, @carbon/icons, @carbon/colors, etc.)

## Output layout

```
output/
  pages/<url-path>/page.html    Full rendered HTML per page
  pages/<url-path>/content.md   Cleaned text/markdown extraction (headings, prose, lists, tables, code)
  pages/<url-path>/meta.json    Title, description, canonical, headings, tab navigation
  assets/icons/*.svg            Every icon from the Icons library, original SVG markup
  assets/pictograms/*.svg       Every pictogram from the Pictograms library
  assets/images/*               Downloaded images referenced by pages
  assets/documents/*            PDFs, ZIPs, design-tool artifacts (e.g. IBM color palette .ase/.clr)
  assets/fonts/*                Any linked webfont files
  assets/videos/*               Any linked video assets
  assets/data/*                 llms.txt and Carbon MCP agent instructions/prompts (see AI resources section above)
  catalog/manifest.json         Per-page crawl record (status, hash, asset counts, timestamps)
  catalog/external-resources.json  Categorized external links with source pages
  catalog/icons-manifest.json   Icon name -> category -> file path
  catalog/pictograms-manifest.json
  catalog/broken-links.json     Dead links found in the source content (see above)
  catalog/asset-index.json     sha256 -> stored file path (dedup index)
  catalog/crawl.log / errors.log  JSONL event & error logs
```

## Reuse notes for a future design-skill build

- Component doc pages (`/components/<name>/{usage,style,code,accessibility}/`) are on **separate URLs**, not client-side tabs — each was crawled as its own page.
- Component `/code/` pages do not embed source code; they link out to per-framework Storybooks (React/Web Components official; Angular/Vue community) and embed a live Storybook iframe preview. Those links are in `external-resources.json` under `storybook-*` categories, keyed by source page.
- Icons/pictograms are stored as standalone `.svg` files with their catalog display name and category preserved in the matching `*-manifest.json`.
