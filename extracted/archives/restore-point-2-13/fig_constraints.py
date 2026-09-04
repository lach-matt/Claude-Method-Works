#!/usr/bin/env python3
"""fig_constraints.py -- the tower's constraint graph, drawn.

Twelve nodes, thirteen edges, girth 5, treewidth 2, cycle rank 2. The base is a
tree; each two-parent axis adds one independent cycle. Drawn so the two cycles
and the hub are visible without a legend.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# node: (x, y, stage at which it enters)
POS = {
 "n":   (0.0, 1.00, 0), "ℓ":  (1.0, 1.00, 0), "k":  (2.0, 1.00, 0),
 "q":   (3.0, 1.00, 0), "g":  (4.0, 1.00, 0), "f":  (5.0, 1.00, 0),
 "e":   (6.0, 1.00, 0),
 "2S":  (2.0, 0.10, 1),
 "v":   (3.3, -0.55, 2),
 "2Jc": (1.4, 1.95, 3),
 "2K":  (3.6, 2.55, 4),
 "2J":  (4.9, 3.15, 5),
}
EDGES = [("ℓ","n",0),("k","ℓ",0),("q","k",0),("f","e",0),("g","f",0),("g","q",0),
         ("2S","k",1),("v","2S",2),("v","g",2),("2Jc","k",3),
         ("2K","2Jc",4),("2K","f",4),("2J","2K",5)]
INK   = "#1a1a1a"
STAGE = {0:"#1a1a1a", 1:"#4a4a4a", 2:"#b03030", 3:"#4a4a4a", 4:"#b03030", 5:"#4a4a4a"}

fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=160)
# the two independent cycles, marked on their own edges — cycle 1 has length 5
# and gives the girth; cycle 2 runs 2K-2Jc-k-q-g-f and has length 6.
CYC1 = {("v","2S"),("2S","k"),("q","k"),("g","q"),("v","g")}
CYC2 = {("2K","2Jc"),("2Jc","k"),("q","k"),("g","q"),("g","f"),("2K","f")}
def cyc(a, b):
    return (a,b) in CYC1 or (b,a) in CYC1 or (a,b) in CYC2 or (b,a) in CYC2

for a, b, st in EDGES:
    x1, y1, _ = POS[a]; x2, y2, _ = POS[b]
    on = cyc(a, b)
    ax.annotate("", xy=(x1, y1), xytext=(x2, y2),
                arrowprops=dict(arrowstyle="-|>",
                                color="#b03030" if on else "#4a4a4a",
                                lw=2.1 if on else 1.2,
                                shrinkA=13, shrinkB=13, alpha=0.95 if on else 0.75))
deg = {n: sum(1 for a, b, _ in EDGES if n in (a, b)) for n in POS}
for n, (x, y, st) in POS.items():
    r = 0.165 + 0.022 * deg[n]
    ax.add_patch(plt.Circle((x, y), r, facecolor="white",
                            edgecolor=STAGE[st], lw=2.1 if deg[n] >= 3 else 1.4, zorder=3))
    ax.text(x, y, n, ha="center", va="center", fontsize=10.5,
            fontweight="bold" if deg[n] >= 3 else "normal", color=INK, zorder=4)

ax.text(1.42, 0.44, "hub · degree 4", ha="center", fontsize=8.2, color="#666", style="italic")
ax.text(3.3, -0.98, "Λ₁₀ takes two parents — cycle 1, length 5", ha="center", fontsize=8.4, color="#b03030")
ax.text(2.55, 3.02, "Λ₁₂ takes two parents — cycle 2, length 6", ha="center", fontsize=8.4, color="#b03030")
ax.text(-0.35, 3.15,
        "12 nodes · 13 edges · cycle rank 2 · girth 5 · treewidth 2 · no triangle",
        fontsize=9.2, color=INK)
ax.set_xlim(-0.7, 6.7); ax.set_ylim(-1.25, 3.5)
ax.set_aspect("equal"); ax.axis("off")
plt.tight_layout()
plt.savefig("fig-constraints.png", dpi=160, bbox_inches="tight", facecolor="white")
# flatten: an alpha channel makes pdfimages report a soft mask as a second image
from PIL import Image as _I; _I.open("fig-constraints.png").convert("RGB").save("fig-constraints.png")
print("  wrote fig-constraints.png")
