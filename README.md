# Medtronic Skills Collection

This repo is a collection of Medtronic-specific Copilot Agent Skills, following the same
`SKILL.md`-per-subfolder layout Copilot itself uses for a project's `.github/skills/` directory
(and the pattern Anthropic's own [anthropics/skills](https://github.com/anthropics/skills) repo
uses). Right now it contains one skill:

## [`medtronic-branding/`](./medtronic-branding/)

Applies official Medtronic brand identity (logo, Full-life Symbol, tagline, exact color palette,
Avenir Next World typography, iconography, composition rules) whenever building or restyling a UI
in GitHub Copilot Chat — React, Streamlit, HTML/CSS, PowerPoint, or general design work.

Bundles real logo/symbol/icon artwork and exact hex/RGB/CMYK color tokens extracted from
Medtronic's official Brand Central guidelines, so Copilot doesn't recreate the logo, guess brand
colors, or invent a substitute palette.

> **Internal use only.** This repo contains Medtronic's proprietary logo, Full-life Symbol, and
> icon artwork under Medtronic's brand license. Do not make this repo public, and do not use these
> assets outside of Medtronic-approved work. See [`medtronic-branding/references/brand-guidelines.md`](./medtronic-branding/references/brand-guidelines.md)
> for trademark/copyright rules and the Avenir Next World font-licensing process.

**Note on structure:** each skill subfolder (e.g. `medtronic-branding/`) contains only
`SKILL.md` + `assets/` + `references/` — no README inside it — per Anthropic's skill-authoring
guidance ("don't include README.md inside your skill folder... you'll still want a repo-level
README for human users," which is this file). Keep it that way if you add more skills here.

## Requirements

- VS Code with GitHub Copilot Chat (a recent version that supports Agent Skills / `SKILL.md`).
- Access to Medtronic's internal GitLab Dedicated instance (`medtronic.gitlab-dedicated.com`) —
  this uses company SSO, so anyone on a Medtronic-managed laptop/VPN with repo access should be
  able to clone it with no extra credential setup. A GitHub mirror also exists at
  `github.com/ms68_mdt/Skill-Medtronic-Branding` for anyone who specifically needs that host
  instead (that one needs its own auth — see the troubleshooting note at the bottom).

## Install (pick one)

### Option A — Use in every project (recommended for most people)

Clone this repo to a staging folder, then copy just the skill subfolder you want into your
personal skills directory. Don't clone directly *into* `~/.agents/skills/medtronic-branding` —
that would nest it one level too deep (this repo's root is the collection, not the skill itself).

**Windows (PowerShell):**

```powershell
git clone https://medtronic.gitlab-dedicated.com/ms68/Medtronic_Design_Skill.git "$env:TEMP\mdt-skills"
Copy-Item -Recurse "$env:TEMP\mdt-skills\medtronic-branding" "$env:USERPROFILE\.agents\skills\medtronic-branding"
Remove-Item -Recurse -Force "$env:TEMP\mdt-skills"
```

**macOS / Linux:**

```bash
git clone https://medtronic.gitlab-dedicated.com/ms68/Medtronic_Design_Skill.git /tmp/mdt-skills
cp -r /tmp/mdt-skills/medtronic-branding ~/.agents/skills/medtronic-branding
rm -rf /tmp/mdt-skills
```

`~/.agents/skills/` is one of three personal skill locations Copilot Chat checks automatically
(the others are `~/.copilot/skills/` and `~/.claude/skills/` — any one works the same way).

**Shortcut if `~/.agents/skills/` doesn't exist yet on your machine:** you can clone this whole
repo directly to that path instead (its layout already matches what Copilot expects there):

```powershell
git clone https://medtronic.gitlab-dedicated.com/ms68/Medtronic_Design_Skill.git "$env:USERPROFILE\.agents\skills"
```

Only do this if that folder is empty/missing — `git clone` refuses to clone into a non-empty
directory, so if you already have other personal skills installed, use the copy method above
instead.

### Option B — Use in just one project (team-shared, checked into that repo)

Same idea, scoped to a project's `.github/skills/`:

```powershell
git clone https://medtronic.gitlab-dedicated.com/ms68/Medtronic_Design_Skill.git "$env:TEMP\mdt-skills"
Copy-Item -Recurse "$env:TEMP\mdt-skills\medtronic-branding" ".github\skills\medtronic-branding"
Remove-Item -Recurse -Force "$env:TEMP\mdt-skills"
```

Commit the result if you want everyone who clones *that* project to get the skill automatically
too. (If a project's `.github/skills/` is empty/doesn't exist yet, you can also clone this repo
directly to `.github/skills` the same way as the Option A shortcut above.)

### Option C — `skills` CLI (if your machine has Node.js >= 20.12)

```bash
npx skills add https://medtronic.gitlab-dedicated.com/ms68/Medtronic_Design_Skill.git
```

Note: this CLI installs whatever's at the repo root. Since this repo root is now a collection
(not a single skill), check what it places under `~/.agents/skills/` afterward — you may still
need to move the `medtronic-branding` folder up one level manually per Option A above.

## Using it

Open Copilot Chat in any project and either:

- type `/medtronic-branding` directly, or
- just ask for something that needs it — e.g. *"brand this dashboard like Medtronic"*, *"add the
  Medtronic logo to the header"*, *"what's our brand blue hex code"* — Copilot will pull in the
  skill automatically based on its description.

### Using the GitHub mirror instead

If your machine (or a contractor's laptop) isn't on the Medtronic corporate network/VPN and can't
reach `medtronic.gitlab-dedicated.com`, swap any URL above for the GitHub mirror:
`https://github.com/ms68_mdt/Skill-Medtronic-Branding.git`. That one isn't SSO-backed, so the
first clone needs its own auth (repo access granted as a collaborator, plus either `gh auth login`,
an SSH key, or a personal access token) — set that up first if `git clone`/`npx skills add`
fails with an authentication error.

The skill enforces **two separate gates**: brand compliance (exact tokens, assets, and rules) and
design quality (hierarchy, spacing rhythm, craft, and a build critique) — because a UI can use every
correct Medtronic token and still be a poorly composed page. The design-quality half lives in
`references/design-intuition.md`, `visual-hierarchy.md`, `craft-details.md`, `content-and-copy.md`,
and `design-review.md`.

See [`medtronic-branding/SKILL.md`](./medtronic-branding/SKILL.md) for the full workflow,
[`medtronic-branding/references/`](./medtronic-branding/references/) for the condensed brand
rules, color tokens, design-quality guidance, and React/Streamlit integration guides, and
[`medtronic-branding/assets/`](./medtronic-branding/assets/) for the actual logo/symbol/icon
files.

## Keeping it up to date

This is a live repo — brand guidelines change over time. Pull the latest whenever you want:

```bash
git -C ~/.agents/skills/medtronic-branding pull
```

## Updating / contributing

If Medtronic's brand guidelines change (new colors, new logo lockup, updated font policy), update
the relevant file under `references/` or `assets/` here and push — everyone who installed via
Option A/C will get the update on their next `git pull`. Don't hand-edit color hex values or
recreate logo artwork from scratch; re-derive from the official source documents
(`1st Half Guidelines.docx`, `2nd Half Guidelines.docx`, `Style Guide.pdf`,
`doc-color-palette-breakdown.pdf`, `doc-avenir-next-world-agreement.docx`) which live in the
broader `Skill for Medtronic Branding` working folder (not included in this repo — see below).

## Why the raw brand-kit zips aren't in this repo

The full Medtronic brand kit (animated Symbol videos, AI vector source, PowerPoint templates,
production graphics toolkit) is several hundred MB to ~1.5GB total, including files larger than
GitHub's 100MB per-file limit. This repo intentionally ships only the compact, curated subset
(~6MB) needed for day-to-day app/UI work. If you need something beyond what's bundled here (print
CMYK files, animated Symbol video, the full icon set in every color), get it from Brand Central or
your Global Brand contact — see [`references/asset-manifest.md`](./medtronic-branding/references/asset-manifest.md)
for exactly what's bundled vs. not.
