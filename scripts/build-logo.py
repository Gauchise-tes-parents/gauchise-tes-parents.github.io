#!/usr/bin/env python3
"""Génère le logo typographique « GAUCHISE TES PARENTS » en SVG (tracés vectoriels).

Les lettres sont extraites de la police Poppins Bold (licence SIL OFL 1.1),
puis épaissies (contour arrondi de même couleur) et légèrement décalées / tournées
pour obtenir un rendu « cartoon ». Le SVG obtenu ne dépend d'aucune police installée.

Usage : python3 scripts/build-logo.py [chemin/vers/Poppins-Bold.ttf]
"""
import json
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = sys.argv[1] if len(sys.argv) > 1 else "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
OUT = os.path.join(ROOT, "public", "img")
os.makedirs(OUT, exist_ok=True)

font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
UPM = font["head"].unitsPerEm


def word_paths(word, size, rotations, dys, spacing=0):
    """Renvoie [(d, x, width, rot, dy)] pour chaque lettre, à la taille `size` px."""
    scale = size / UPM
    x = 0.0
    out = []
    for i, ch in enumerate(word):
        gname = cmap[ord(ch)]
        glyph = gs[gname]
        pen = SVGPathPen(gs)
        # retournement vertical (les polices ont l'axe Y vers le haut)
        tpen = TransformPen(pen, (scale, 0, 0, -scale, 0, size * 0.78))
        glyph.draw(tpen)
        w = glyph.width * scale
        out.append({"d": pen.getCommands(), "x": round(x, 2), "w": round(w, 2),
                    "rot": rotations[i % len(rotations)], "dy": dys[i % len(dys)]})
        x += w + spacing
    return out, x


def letters_svg(items, fill, stroke, stroke_w, shadow=None, shadow_off=(5, 6)):
    parts = []
    for it in items:
        cx = it["x"] + it["w"] / 2
        tr = f'translate({it["x"]} {it["dy"]}) rotate({it["rot"]} {it["w"]/2} 40)'
        if shadow:
            parts.append(f'<path d="{it["d"]}" transform="translate({shadow_off[0]} {shadow_off[1]}) {tr}" '
                         f'fill="{shadow}" stroke="{shadow}" stroke-width="{stroke_w}" stroke-linejoin="round"/>')
        parts.append(f'<path d="{it["d"]}" transform="{tr}" fill="{fill}" stroke="{stroke}" '
                     f'stroke-width="{stroke_w}" stroke-linejoin="round" paint-order="stroke"/>')
    return "\n    ".join(parts)


ROT = [-4, 3, -2, 4, -3, 2, -4, 3]
DY = [2, -3, 1, -2, 3, -1, 2, -2]
gauch, gw = word_paths("GAUCHISE", 96, ROT, DY, spacing=4)
tes, tw = word_paths("TES PARENTS", 30, [0], [0], spacing=1.5)

NIGHT = "#2B1A5C"   # violet nuit
LEMON = "#FFE11A"   # jaune citron
ORANGE = "#FF7A2F"  # orange chaleureux
CREAM = "#FFF7E6"

pad = 14
W = int(gw + pad * 2 + 10)
bubble_w = tw + 36
bubble_x = W - bubble_w - 6
H = 168

logo = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="logoTitle">
  <title id="logoTitle">Gauchise tes parents</title>
  <g transform="translate({pad} 10)">
    {letters_svg(gauch, LEMON, NIGHT, 9, shadow=ORANGE)}
  </g>
  <g transform="translate({bubble_x:.1f} 110)">
    <path d="M10 0 H{bubble_w-10:.1f} Q{bubble_w:.1f} 0 {bubble_w:.1f} 10 V30 Q{bubble_w:.1f} 40 {bubble_w-10:.1f} 40 H44 L26 54 L30 40 H10 Q0 40 0 30 V10 Q0 0 10 0 Z"
      fill="{CREAM}" stroke="{NIGHT}" stroke-width="4" stroke-linejoin="round" transform="rotate(-2 {bubble_w/2:.1f} 20)"/>
    <g transform="translate(18 5) rotate(-2 {tw/2:.1f} 15)">
      {letters_svg(tes, NIGHT, NIGHT, 0.6)}
    </g>
  </g>
</svg>
'''

# Version « nuit » : même dessin, conçu pour fond sombre (bulle conservée)
logo_dark = logo  # le logo est déjà contrasté (contour nuit + bulle crème), il fonctionne sur fond violet.

# Icône d'application : un « G » citron + loupe, sur pastille violette
g_only, gw1 = word_paths("G", 120, [-6], [0])
icon = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192" role="img" aria-label="Gauchise tes parents">
  <rect x="6" y="6" width="180" height="180" rx="44" fill="{NIGHT}"/>
  <g transform="translate({(192-gw1)/2 - 10:.1f} 20)">
    {letters_svg(g_only, LEMON, NIGHT, 0, shadow=ORANGE, shadow_off=(5, 6))}
  </g>
  <g transform="translate(118 112) rotate(-35)">
    <rect x="-7" y="30" width="14" height="38" rx="7" fill="{ORANGE}" stroke="{CREAM}" stroke-width="5"/>
    <circle cx="0" cy="0" r="30" fill="#BFE9FF" fill-opacity=".85" stroke="{CREAM}" stroke-width="9"/>
    <path d="M-14 -10 Q-8 -20 4 -20" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
  </g>
</svg>
'''

with open(os.path.join(OUT, "logo.svg"), "w") as f:
    f.write(logo)
with open(os.path.join(OUT, "icon.svg"), "w") as f:
    f.write(icon)
# fichier de tracés pour l'intégration inline dans l'interface
with open(os.path.join(ROOT, "public", "js", "logo-data.js"), "w") as f:
    f.write("// Généré par scripts/build-logo.py — ne pas modifier à la main.\n")
    f.write("export const LOGO_SVG = " + json.dumps(logo) + ";\n")
    f.write("export const ICON_SVG = " + json.dumps(icon) + ";\n")
print("logo.svg", W, "x", H, "| icon.svg 192x192")
