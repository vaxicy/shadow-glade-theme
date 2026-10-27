<p align="center">
  <img src="logo/logo.png" width="128" alt="Shadow Glade Theme logo">
</p>

<h1 align="center">Shadow Glade Theme</h1>

<p align="center">
  A cool retro Chrome theme in ink navy and pale mint — dark glade chrome over a light meadow page.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/manifest-v3-202734" alt="Manifest V3">
  <img src="https://img.shields.io/badge/version-1.0.0-36415a" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/chrome-dark-e0f8c7" alt="Dark chrome">
  <img src="https://img.shields.io/badge/license-non--commercial-2f5d3a" alt="Non-commercial license">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/shadow-glade-theme/main/store-assets/promo/1400x560.png" alt="Shadow Glade Theme promo" width="700">
</p>

## Overview

Shadow Glade pairs an ink-navy frame with a slate toolbar, then opens onto a soft greige New Tab Page where a muted sage Google logo sits quietly. Pale mint ink keeps every tab, bookmark and toolbar icon readable on the dark chrome, links take a deep moss tone, and a single-row shortcut layout keeps the New Tab Page clean.

The page is deliberately desaturated: the greens stay in the chrome and in the mark, so the New Tab Page reads as shade rather than meadow.

## Design Concept

The source palette is two cold families: an ink/slate navy pair and a sage/mint green pair. The navy does the structural work (frame and toolbar), the greens supply the light — mint as the ink on the chrome and as the mark's moon, sage for buttons and the New Tab header. Between them sits a greige page, desaturated from the original mint so the derived Google logo no longer competes with the chrome.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Ink | `#202734` | 32, 39, 52 | Frame |
| Slate | `#36415A` | 54, 65, 90 | Toolbar / secondary buttons |
| Sage | `#B7D894` | 183, 216, 148 | New Tab header / buttons |
| Mint | `#E0F8C7` | 224, 248, 199 | Chrome ink / mark |
| Page | `#E2E6DA` | 226, 230, 218 | New Tab background |
| Moss | `#2F5D3A` | 47, 93, 58 | New Tab links |
| Dark Ink | `#22302A` | 34, 48, 42 | New Tab text |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Cool retro palette: ink navy, slate, sage and mint
- Dark navy chrome with pale mint ink — 8.9:1 on the toolbar
- Tab text, bookmark text and toolbar icons all share the same mint ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Screenshots

| Browser | Palette |
|:-:|:-:|
| <img src="https://raw.githubusercontent.com/vaxicy/shadow-glade-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" width="420" alt="Shadow Glade New Tab"> | <img src="https://raw.githubusercontent.com/vaxicy/shadow-glade-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" width="420" alt="Shadow Glade palette"> |

## Installation

### Load unpacked (development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** in the top right.
4. Click **Load unpacked** and select this folder (`shadow-glade-theme`).
5. The theme is active immediately.

### Package for the Chrome Web Store

```
chrome://extensions → Pack extension → select this folder → shadow-glade-theme.zip
```

Upload the resulting `.zip` to the [Chrome Web Store developer dashboard](https://chrome.google.com/webstore/devconsole).

## Store listing copy

Ready to paste into the store listing (also kept in `store-assets/store-description.txt`):

> Shadow Glade is a cool retro Chrome theme: ink-navy chrome, a soft greige New Tab Page, and a muted sage Google logo that sits quietly on it. Pale mint ink keeps every tab, bookmark and toolbar icon readable on the dark frame. Solid colors only, no wallpaper.

## Project structure

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build contact sheets, export `logo/logo.png` from `SELECTED` |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles (1400×560 window hero, 440×280 dot palette) |
| `logo/candidates/` | Candidate previews and light/dark contact sheets |
| `LICENSE` | Non-Commercial License (English / 中文) |

## Regenerating assets

Every asset is code-generated, so nothing here is hand-drawn or hand-copied:

```bash
py -3 scripts/generate-logo-vector.py         # candidates + contact sheets + logo/logo.png
py -3 scripts/generate-screenshot-headless.py # store screenshot 1 (browser mockup)
py -3 scripts/generate-screenshot-2-palette.py # store screenshot 2 (palette)
py -3 scripts/generate-promo.py               # promo 440x280 + 1400x560
```

To ship a different icon candidate, change `SELECTED` at the top of `generate-logo-vector.py` and re-run, then re-run the three asset scripts so the promo and screenshots pick up the new logo.

## License

Shadow Glade Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
