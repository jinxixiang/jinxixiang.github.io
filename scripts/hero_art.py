"""Generate assets/svg/hero-art.svg: a stylized spatial-omics tissue section.

A hexagonal spot array (as in Visium) is clipped to an organic tissue outline.
Spots are colored by spatial domain and shaded by a smooth "expression" field;
a sparse k-nearest-neighbor graph over the spots evokes graph neural networks,
and a dashed contour marks a tumor region. Colors come from CSS classes so the
page can restyle the art for dark mode.

Run from the repo root:  python3 scripts/hero_art.py
"""

import math
import random

W, H = 600, 520
SPACING = 17.0  # center-to-center distance between spots
RADIUS = 6.2
SEED = 7

random.seed(SEED)


def noise(x, y, waves):
    return sum(a * math.sin(fx * x + fy * y + p) for a, fx, fy, p in waves)


def make_waves(n, scale):
    return [
        (
            random.uniform(0.4, 1.0),
            random.uniform(-scale, scale),
            random.uniform(-scale, scale),
            random.uniform(0, 2 * math.pi),
        )
        for _ in range(n)
    ]


# Tissue outline: a wobbly ellipse in polar form.
CX, CY = W / 2, H / 2
RX, RY = 268, 228
edge_waves = [(random.uniform(0.04, 0.09), k, random.uniform(0, 2 * math.pi)) for k in (2, 3, 5, 7)]


def tissue_radius(theta):
    wobble = sum(a * math.sin(k * theta + p) for a, k, p in edge_waves)
    return 1.0 + wobble


def inside_tissue(x, y, margin=0.0):
    dx, dy = (x - CX) / RX, (y - CY) / RY
    r = math.hypot(dx, dy)
    return r < tissue_radius(math.atan2(dy, dx)) - margin


# Spatial domains: nearest seed point, with a noisy boundary.
seeds = [(190, 140, "d1"), (430, 150, "d2"), (420, 370, "d3"), (300, 250, "d4"), (165, 345, "d5")]
domain_waves = make_waves(4, 0.02)
expr_waves = make_waves(5, 0.03)


def domain(x, y):
    jitter = noise(x, y, domain_waves) * 28
    return min(seeds, key=lambda s: math.hypot(x - s[0], y - s[1]) + (jitter if s[2] == "d5" else 0))[2]


# Tumor region: a noisy blob around the d5 seed, left of the portrait so it stays visible.
TX, TY, TR = 160, 345, 72
tumor_waves = [(random.uniform(0.06, 0.12), k, random.uniform(0, 2 * math.pi)) for k in (2, 3, 4, 6)]


def tumor_radius(theta):
    return TR * (1 + sum(a * math.sin(k * theta + p) for a, k, p in tumor_waves))


# Hexagonal spot grid.
spots = []
row_h = SPACING * math.sqrt(3) / 2
for j in range(int(H / row_h) + 2):
    y = j * row_h
    offset = SPACING / 2 if j % 2 else 0
    for i in range(int(W / SPACING) + 2):
        x = i * SPACING + offset
        if inside_tissue(x, y, margin=0.02):
            e = 0.5 + 0.5 * math.tanh(noise(x, y, expr_waves) * 0.9)
            spots.append((x, y, domain(x, y), 0.18 + 0.72 * e))

# Sparse kNN graph over a random subset of spots.
nodes = random.sample(spots, 46)
edges = set()
for a in nodes:
    near = sorted((n for n in nodes if n is not a), key=lambda n: math.hypot(n[0] - a[0], n[1] - a[1]))[:2]
    for b in near:
        edges.add(tuple(sorted([(a[0], a[1]), (b[0], b[1])])))
attention = random.sample(nodes, 6)


def path_from_polar(cx, cy, rfun, sx=1.0, sy=1.0, steps=120):
    pts = []
    for k in range(steps):
        t = 2 * math.pi * k / steps
        r = rfun(t)
        pts.append((cx + r * sx * math.cos(t), cy + r * sy * math.sin(t)))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return d


tissue_d = path_from_polar(CX, CY, tissue_radius, RX, RY)
tumor_d = path_from_polar(TX, TY, tumor_radius)

out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" class="hero-art" focusable="false">',
    f'<path class="tissue" d="{tissue_d}"/>',
    '<g class="spots">',
]
for x, y, d, o in spots:
    out.append(f'<circle class="{d}" cx="{x:.1f}" cy="{y:.1f}" r="{RADIUS}" fill-opacity="{o:.2f}"/>')
out.append("</g>")
out.append('<g class="edges">')
for (x1, y1), (x2, y2) in sorted(edges):
    out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
out.append("</g>")
out.append('<g class="nodes">')
for x, y, _, _ in nodes:
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4"/>')
out.append("</g>")
out.append('<g class="attention">')
for x, y, _, _ in attention:
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11"/>')
out.append("</g>")
out.append(f'<path class="tumor" d="{tumor_d}"/>')
out.append("</svg>")

with open("assets/svg/hero-art.svg", "w") as f:
    f.write("\n".join(out) + "\n")
print(f"{len(spots)} spots, {len(edges)} edges")
