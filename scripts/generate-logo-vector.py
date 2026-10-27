#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shadow Glade Theme — vector logo candidates (SVG rendered by headless Chromium).

Every mark carries a gradient fill, a soft drop shadow and highlights so it reads
as a designed icon rather than flat clip-art. The palette is one deep navy pair
plus one mint pair, so marks alternate navy silhouettes against mint light.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "01"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


INK = hx(_C["frame"])                              # #202734
SLATE = hx(_C["toolbar"])                          # #36415A
SAGE = hx(_C["ntp_header"])                        # #B7D894
# the page background was desaturated to a greige, so the mark keeps the palette
# mint explicitly instead of following ntp_background (2026-10-27)
MINT = "#E0F8C7"
DEEP_GREEN = hx(_C["ntp_link"])                    # #2F5D3A
INK_T = hx(_C["ntp_text"])                         # #22302A

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="%s" flood-opacity=".22"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def conifer(cx, base_y, height, width, fill):
    """Three stacked triangles plus a trunk."""
    out = []
    tiers = 3
    for i in range(tiers):
        w = width * (1 - 0.22 * i)
        h = height / (tiers + 1.1)
        top = base_y - height + i * h * 0.92
        out.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="%s"/>'
                   % (cx, top, cx - w / 2, top + h * 1.28, cx + w / 2, top + h * 1.28, fill))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>'
               % (cx - width * 0.05, base_y - height * 0.12, width * 0.10, height * 0.14,
                  width * 0.04, fill))
    return "".join(out)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<rect x="40" y="40" width="176" height="176" rx="46" fill="url(#g1)" filter="url(#ds)"/>
<circle cx="128" cy="104" r="26" fill="%s"/>
<path d="M40 168 Q84 132 128 168 Q172 132 216 168 V216 H40 Z" fill="%s"/>
<path d="M40 190 Q84 160 128 190 Q172 160 216 190 V216 H40 Z" fill="%s" fill-opacity=".72"/>
<circle cx="128" cy="104" r="26" fill="none" stroke="%s" stroke-opacity=".22" stroke-width="3"/>
""" % (SLATE, INK, SHADOW, MINT, SAGE, DEEP_GREEN, INK))

SVG_02 = svg_open("""
<defs>
  <linearGradient id="lf2" x1="0" y1="0" x2="0.7" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g transform="translate(14 12)" opacity=".34">
  <path d="M128 40 C176 62 200 108 194 152 C188 196 160 218 128 218 C96 218 68 196 62 152
           C56 108 80 62 128 40 Z" fill="%s"/>
</g>
<path d="M128 40 C176 62 200 108 194 152 C188 196 160 218 128 218 C96 218 68 196 62 152
         C56 108 80 62 128 40 Z" fill="url(#lf2)" filter="url(#ds)"/>
<path d="M128 62 V206" stroke="%s" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/>
<g stroke="%s" stroke-opacity=".45" stroke-width="4" stroke-linecap="round" fill="none">
  <path d="M128 96 C110 92 98 80 94 66"/>
  <path d="M128 96 C146 92 158 80 162 66"/>
  <path d="M128 142 C106 138 92 124 86 108"/>
  <path d="M128 142 C150 138 164 124 170 108"/>
</g>
""" % (SAGE, DEEP_GREEN, SHADOW, INK, DEEP_GREEN, DEEP_GREEN))

SVG_03 = svg_open("""
<defs>%s</defs>
<circle cx="128" cy="118" r="66" fill="%s" filter="url(#ds)"/>
<circle cx="146" cy="104" r="56" fill="%s" fill-opacity=".95"/>
<g fill="%s">
  <path d="M30 212 Q70 150 110 212 Z"/>
  <path d="M146 212 Q186 150 226 212 Z"/>
</g>
<path d="M30 212 H226" stroke="%s" stroke-width="8" stroke-linecap="round"/>
""" % (SHADOW, MINT, SLATE, INK_T, DEEP_GREEN))

SVG_04 = svg_open("""
<defs>%s</defs>
<g filter="url(#ds)">
  %s
  %s
</g>
<path d="M98 226 H158 L141 136 a13 13 0 0 0 -26 0 Z" fill="%s"/>
""" % (SHADOW,
       conifer(76, 226, 150, 62, INK_T),
       conifer(182, 226, 150, 62, SLATE),
       SAGE))

SVG_05 = svg_open("""
<defs>%s</defs>
<circle cx="128" cy="128" r="102" fill="%s" filter="url(#ds)"/>
<circle cx="128" cy="104" r="24" fill="%s"/>
<path d="M40 176 Q84 138 128 176 Q172 138 216 176 V214 a6 6 0 0 1 -6 6 H46 a6 6 0 0 1 -6 -6 Z"
      fill="%s"/>
<path d="M52 196 Q88 168 128 196 Q168 168 204 196 V214 H52 Z" fill="%s" fill-opacity=".78"/>
""" % (SHADOW, INK, MINT, SAGE, DEEP_GREEN))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="sl6" x1="0" y1="0" x2="1" y2="0.4">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)" transform="rotate(-18 128 128)">
  <rect x="46" y="96" width="164" height="22" rx="11" fill="url(#sl6)"/>
  <rect x="62" y="132" width="132" height="22" rx="11" fill="%s" fill-opacity=".9"/>
  <rect x="80" y="168" width="96" height="22" rx="11" fill="%s"/>
  <rect x="98" y="60" width="60" height="22" rx="11" fill="%s" fill-opacity=".75"/>
</g>
""" % (MINT, SAGE, SHADOW, SAGE, DEEP_GREEN, MINT))

CANDIDATES = [
    ("01", "glade-moon", "Moon over a glade in a rounded tile — most literal scene", SVG_01),
    ("02", "leaf-shadow", "Mint leaf with its own cast shadow — says 'shadow' twice", SVG_02),
    ("03", "moon-canopy", "Pale moon behind a navy canopy — simplest silhouette", SVG_03),
    ("04", "glade-path", "Two conifers flanking a mint path — clearest 'glade'", SVG_04),
    ("05", "glade-badge", "Badge with moon, canopy and meadow — strongest at 32px", SVG_05),
    ("06", "dappled-light", "Diagonal light bars with shadows — most abstract", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            # Playwright's bundled headless shell may be missing after an update;
            # fall back to the locally installed Chrome instead of a 150MB download.
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (236, 248, 224))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(32, 39, 52))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (236, 248, 224), (32, 39, 52), (108, 124, 100),
                  CAND_DIR / "contact-light.png", "Shadow Glade — vector logo candidates (light)")
    contact_sheet(rendered, (26, 32, 43), (224, 248, 199), (150, 172, 150),
                  CAND_DIR / "contact-dark.png", "Shadow Glade — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
