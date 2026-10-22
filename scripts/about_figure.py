"""Generate the About-section figure: pathology image -> spatial omics -> AI.

Three panels, all drawn procedurally (no real patient images):
  1. an H&E-style tissue section: eosin-pink stroma, hematoxylin-purple nuclei,
     glands, and a dense tumor region;
  2. the same section overlaid with a Visium-style spot array, colored by
     spatial domain and shaded by expression;
  3. a multimodal model: image and omics tokens feed a small network whose
     outputs are diagnosis, prognosis, and therapy response.

Writes a wide layout (desktop) and a stacked layout (phones):
  assets/svg/about-figure-wide.svg
  assets/svg/about-figure-tall.svg

Run from the repo root:  python3 scripts/about_figure.py
"""

import math
import random

SEED = 7
PANEL = 300  # panel width and height in SVG units

FONT = "Inter, -apple-system, Helvetica, Arial, sans-serif"
SERIF = "'Source Serif 4', Georgia, serif"
INK = "#1b1b1b"
MUTED = "#5d5d5d"
LINE = "#e7e4de"
ACCENT = "#8c1515"
EOSIN = "#f2c3d3"
EOSIN_DARK = "#e39bb8"
HEMATOXYLIN = "#4f2f86"
HEMATOXYLIN_LIGHT = "#7a5aae"
DOMAINS = ["#8c1515", "#175e54", "#b58a2e", "#4d5f8c", "#9d2a6b"]


# --- Shared tissue geometry (in unit coordinates, 0..1) ---------------------

rng = random.Random(SEED)
EDGE_WAVES = [(rng.uniform(0.04, 0.08), k, rng.uniform(0, 2 * math.pi)) for k in (2, 3, 5, 7)]
TUMOR = (0.34, 0.62, 0.17)  # center x, center y, radius
TUMOR_WAVES = [(rng.uniform(0.08, 0.14), k, rng.uniform(0, 2 * math.pi)) for k in (2, 3, 4, 6)]
GLANDS = [(0.66, 0.30, 0.055, 0.035), (0.74, 0.55, 0.045, 0.03), (0.52, 0.22, 0.04, 0.028), (0.60, 0.74, 0.05, 0.03)]
DOMAIN_SEEDS = [(0.30, 0.25), (0.70, 0.22), (0.75, 0.68), (0.52, 0.48), TUMOR[:2]]
EXPR_WAVES = [(rng.uniform(0.4, 1), rng.uniform(-9, 9), rng.uniform(-9, 9), rng.uniform(0, 6.3)) for _ in range(5)]


def tissue_r(theta):
    return 1.0 + sum(a * math.sin(k * theta + p) for a, k, p in EDGE_WAVES)


def in_tissue(u, v, margin=0.0):
    dx, dy = (u - 0.5) / 0.44, (v - 0.5) / 0.40
    return math.hypot(dx, dy) < tissue_r(math.atan2(dy, dx)) - margin


def tumor_r(theta):
    return TUMOR[2] * (1 + sum(a * math.sin(k * theta + p) for a, k, p in TUMOR_WAVES))


def in_tumor(u, v):
    dx, dy = u - TUMOR[0], v - TUMOR[1]
    return math.hypot(dx, dy) < tumor_r(math.atan2(dy, dx))


def in_gland(u, v, pad=0.0):
    return any(((u - x) / (a + pad)) ** 2 + ((v - y) / (b + pad)) ** 2 < 1 for x, y, a, b in GLANDS)


def polar_path(ox, oy, s, cx, cy, rx, ry, rfun, steps=140):
    pts = []
    for k in range(steps):
        t = 2 * math.pi * k / steps
        r = rfun(t)
        pts.append((ox + s * (cx + r * rx * math.cos(t)), oy + s * (cy + r * ry * math.sin(t))))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"


def tissue_path(ox, oy, s):
    return polar_path(ox, oy, s, 0.5, 0.5, 0.44, 0.40, tissue_r)


def tumor_path(ox, oy, s):
    return polar_path(ox, oy, s, TUMOR[0], TUMOR[1], 1, 1, tumor_r)


# --- Panels ------------------------------------------------------------------

def frame(ox, oy, s):
    return f'<rect x="{ox}" y="{oy}" width="{s}" height="{s}" rx="14" fill="#fcfbf9" stroke="{LINE}"/>'


def he_panel(ox, oy, s, cid):
    r = random.Random(SEED + 1)
    out = [frame(ox, oy, s),
           f'<clipPath id="{cid}"><path d="{tissue_path(ox, oy, s)}"/></clipPath>',
           f'<path d="{tissue_path(ox, oy, s)}" fill="{EOSIN}"/>',
           f'<g clip-path="url(#{cid})">']
    # stroma fibers
    for _ in range(70):
        u, v = r.random(), r.random()
        ang = r.uniform(-0.5, 0.5) + 0.3
        L = r.uniform(0.05, 0.12)
        x1, y1 = ox + s * u, oy + s * v
        x2, y2 = x1 + s * L * math.cos(ang), y1 + s * L * math.sin(ang)
        cx, cy = (x1 + x2) / 2 + r.uniform(-4, 4), (y1 + y2) / 2 + r.uniform(-4, 4)
        out.append(f'<path d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" '
                   f'stroke="{EOSIN_DARK}" stroke-width="1" fill="none" opacity="0.55"/>')
    # tumor bed slightly darker
    out.append(f'<path d="{tumor_path(ox, oy, s)}" fill="#e7a9c4" opacity="0.7"/>')
    # gland lumens with nuclear rims
    for x, y, a, b in GLANDS:
        out.append(f'<ellipse cx="{ox + s * x:.1f}" cy="{oy + s * y:.1f}" rx="{s * a:.1f}" ry="{s * b:.1f}" '
                   f'fill="#fdf6f8" stroke="{EOSIN_DARK}" stroke-width="1.5"/>')
        for k in range(14):
            t = 2 * math.pi * k / 14
            nx, ny = ox + s * (x + (a + 0.012) * math.cos(t)), oy + s * (y + (b + 0.012) * math.sin(t))
            out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.6" ry="1.7" '
                       f'transform="rotate({math.degrees(t) + 90:.0f} {nx:.1f} {ny:.1f})" fill="{HEMATOXYLIN}" opacity="0.85"/>')
    # nuclei: dense, large, pleomorphic in tumor; sparse elsewhere; a few lymphocyte clusters
    for _ in range(2600):
        u, v = r.random(), r.random()
        if not in_tissue(u, v) or in_gland(u, v, 0.02):
            continue
        tumor = in_tumor(u, v)
        if not tumor and r.random() > 0.28:
            continue
        # tumor nuclei: large and round-ish; stromal fibroblasts: small and spindle-shaped
        rx = r.uniform(2.2, 3.6) if tumor else r.uniform(1.8, 2.8)
        ry = rx * (r.uniform(0.6, 0.95) if tumor else r.uniform(0.3, 0.5))
        col = HEMATOXYLIN if tumor else HEMATOXYLIN_LIGHT
        x, y = ox + s * u, oy + s * v
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
                   f'transform="rotate({r.uniform(0, 180):.0f} {x:.1f} {y:.1f})" fill="{col}" opacity="{r.uniform(0.7, 0.95):.2f}"/>')
    for cxu, cyu in [(0.72, 0.42), (0.24, 0.36)]:
        for _ in range(26):
            u, v = cxu + r.gauss(0, 0.025), cyu + r.gauss(0, 0.025)
            out.append(f'<circle cx="{ox + s * u:.1f}" cy="{oy + s * v:.1f}" r="1.6" fill="#3b2366"/>')
    out.append("</g>")
    out.append(f'<path d="{tissue_path(ox, oy, s)}" fill="none" stroke="{EOSIN_DARK}" stroke-width="1.2"/>')
    return out


def spots_panel(ox, oy, s, cid):
    out = [frame(ox, oy, s),
           f'<path d="{tissue_path(ox, oy, s)}" fill="{EOSIN}" opacity="0.45"/>']
    spacing = s * 0.05
    row_h = spacing * math.sqrt(3) / 2
    for j in range(int(s / row_h) + 2):
        offset = spacing / 2 if j % 2 else 0
        for i in range(int(s / spacing) + 2):
            x, y = i * spacing + offset, j * row_h
            u, v = x / s, y / s
            if not in_tissue(u, v, margin=0.03):
                continue
            d = min(range(5), key=lambda k: math.hypot(u - DOMAIN_SEEDS[k][0], v - DOMAIN_SEEDS[k][1]) - (0.06 if k == 4 and in_tumor(u, v) else 0))
            if in_tumor(u, v):
                d = 4
            e = 0.5 + 0.5 * math.tanh(sum(a * math.sin(fx * u + fy * v + p) for a, fx, fy, p in EXPR_WAVES) * 0.9)
            out.append(f'<circle cx="{ox + x:.1f}" cy="{oy + y:.1f}" r="{spacing * 0.38:.1f}" '
                       f'fill="{DOMAINS[d]}" fill-opacity="{0.3 + 0.65 * e:.2f}"/>')
    out.append(f'<path d="{tumor_path(ox, oy, s)}" fill="none" stroke="{INK}" stroke-opacity="0.6" '
               f'stroke-width="1.4" stroke-dasharray="4 4"/>')
    return out


def ai_panel(ox, oy, s):
    r = random.Random(SEED + 2)
    out = [frame(ox, oy, s)]
    # input tokens: image patches (pink/purple) and omics spots (domain colors)
    tok = 15
    img_tokens = [(ox + 26, oy + 44 + k * 22) for k in range(5)]
    omx_tokens = [(ox + 26, oy + 170 + k * 22) for k in range(4)]
    layers = [
        [(ox + 112, oy + 50 + k * 40) for k in range(6)],
        [(ox + 178, oy + 70 + k * 40) for k in range(5)],
    ]
    outputs = [(ox + 236, oy + 92 + k * 58) for k in range(3)]
    src = [(x + tok, y + tok / 2) for x, y in img_tokens + omx_tokens]
    hot = {(1, 2), (4, 3), (6, 1), (2, 4)}
    for a_i, a in enumerate(src):
        for b_i, b in enumerate(layers[0]):
            hl = (a_i, b_i) in hot
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                       f'stroke="{ACCENT if hl else INK}" stroke-opacity="{0.7 if hl else 0.12}" stroke-width="{1.4 if hl else 0.8}"/>')
    for a_i, a in enumerate(layers[0]):
        for b_i, b in enumerate(layers[1]):
            hl = r.random() < 0.12
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                       f'stroke="{ACCENT if hl else INK}" stroke-opacity="{0.6 if hl else 0.14}" stroke-width="{1.3 if hl else 0.8}"/>')
    for a in layers[1]:
        for b in outputs:
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                       f'stroke="{INK}" stroke-opacity="0.14" stroke-width="0.8"/>')
    for k, (x, y) in enumerate(img_tokens):
        out.append(f'<rect x="{x}" y="{y}" width="{tok}" height="{tok}" rx="3" '
                   f'fill="{[EOSIN_DARK, HEMATOXYLIN_LIGHT, "#e7a9c4", HEMATOXYLIN, EOSIN_DARK][k]}"/>')
    for k, (x, y) in enumerate(omx_tokens):
        out.append(f'<rect x="{x}" y="{y}" width="{tok}" height="{tok}" rx="7.5" fill="{DOMAINS[k]}" fill-opacity="0.8"/>')
    for layer in layers:
        for x, y in layer:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#fff" stroke="{INK}" stroke-width="1.4"/>')
    labels = [("Diagnosis", 0.82), ("Prognosis", 0.64), ("Response", 0.74)]
    for (x, y), (name, val) in zip(outputs, labels):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{ACCENT}"/>')
        out.append(f'<text x="{x - 6:.1f}" y="{y - 14:.1f}" font-family="{FONT}" font-size="11" fill="{MUTED}">{name}</text>')
        out.append(f'<rect x="{x + 12:.1f}" y="{y - 3:.1f}" width="40" height="6" rx="3" fill="{LINE}"/>')
        out.append(f'<rect x="{x + 12:.1f}" y="{y - 3:.1f}" width="{40 * val:.1f}" height="6" rx="3" fill="{ACCENT}" fill-opacity="0.75"/>')
    out.append(f'<text x="{ox + 20}" y="{oy + 30}" font-family="{FONT}" font-size="10" letter-spacing="0.6" fill="{MUTED}">IMAGE</text>')
    out.append(f'<text x="{ox + 20}" y="{oy + 160}" font-family="{FONT}" font-size="10" letter-spacing="0.6" fill="{MUTED}">OMICS</text>')
    return out


def caption(x, y, title, sub, anchor="middle"):
    return [f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{SERIF}" font-size="19" font-weight="600" fill="{INK}">{title}</text>',
            f'<text x="{x}" y="{y + 22}" text-anchor="{anchor}" font-family="{FONT}" font-size="13" fill="{MUTED}">{sub}</text>']


def arrow(x1, y1, x2, y2):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx = [x2 - 9 * math.cos(ang - 0.45), x2 - 9 * math.cos(ang + 0.45)]
    hy = [y2 - 9 * math.sin(ang - 0.45), y2 - 9 * math.sin(ang + 0.45)]
    return [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
            f'<path d="M{hx[0]:.1f},{hy[0]:.1f} L{x2},{y2} L{hx[1]:.1f},{hy[1]:.1f}" fill="none" stroke="{ACCENT}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>']


TITLES = [("Pathology image", "Routine H&amp;E histology"),
          ("Spatial omics", "Molecular maps in tissue context"),
          ("Multimodal AI", "Foundation models for the clinic")]


def build(layout):
    s = PANEL
    if layout == "wide":
        gap = 70
        W, H = 3 * s + 2 * gap, s + 62
        pos = [(i * (s + gap), 0) for i in range(3)]
        arrows = [arrow(s + 16, s / 2, s + gap - 16, s / 2), arrow(2 * s + gap + 16, s / 2, 2 * s + 2 * gap - 16, s / 2)]
        caps = [caption(x + s / 2, s + 32, *t) for (x, _), t in zip(pos, TITLES)]
    else:
        gap = 120
        W, H = s, 3 * s + 2 * gap
        pos = [(0, i * (s + gap)) for i in range(3)]
        arrows = [arrow(s / 2, s + 72, s / 2, s + gap - 12), arrow(s / 2, 2 * s + gap + 72, s / 2, 2 * s + 2 * gap - 12)]
        caps = [caption(s / 2, y + s + 30, *t) for (_, y), t in zip(pos, TITLES)]
    body = []
    body += he_panel(*pos[0], s, f"tissue-{layout}")
    body += spots_panel(*pos[1], s, f"spots-{layout}")
    body += ai_panel(*pos[2], s)
    for a in arrows:
        body += a
    for c in caps:
        body += c
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 {W + 4} {H + 4}" '
           f'role="img" aria-label="Pathology images and spatial omics feed a multimodal AI model">'] + body + ["</svg>"]
    path = f"assets/svg/about-figure-{layout}.svg"
    with open(path, "w") as f:
        f.write("\n".join(svg) + "\n")
    print(path, f"{W}x{H}")


build("wide")
build("tall")
