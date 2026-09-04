#!/usr/bin/env python3
"""fig_indices.py -- four figures for the Index of Indices.

  i1  the composability profile up the tower, counting against coupling
  i2  the index landscape — cells against defect, transition against state
  i3  Λ₈'s constraint tree, with the one coupling drawn as a join
  i4  the electromagnetic crossing — within an atom against across the table
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image as _I

INK, RED, BLUE, GREY = "#1a1a1a", "#b03030", "#2a5d8f", "#8a8a8a"
def save(fig, name):
    fig.savefig(name, dpi=160, bbox_inches="tight", facecolor="white")
    _I.open(name).convert("RGB").save(name)
    plt.close(fig); print(f"  wrote {name}")

# ---------------------------------------------------------------- i1
# ---------------------------------------------------------------- i2
objs = [("Λ₈", 976, 0, "t"), ("Λ₉", 1654, 0, "t"), ("Λ₁₀", 2535, 0, "t"),
        ("Λ₁₃", 199130, 0, "t"), ("violation index", 2370, 30, "t"),
        ("periodic table", 90, 36, "s"), ("Janet", 118, 0, "s"),
        ("calendar", 365, 7, "s"), ("chessboard", 64, 0, "s"),
        ("box ordering", 35, 0, "s"), ("the audits", 21, 16, "s"),
        ("the protocols", 19, 105, "s"), ("Q", 8, 5, "s")]
fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=160)
for nm, n, e, k in objs:
    c = BLUE if k == "t" else RED
    m = "o" if k == "t" else "s"
    ax.scatter([n], [e + 0.6], s=70, color="white", edgecolor=c, lw=2, marker=m, zorder=3)
    ax.annotate(nm, (n, e + 0.6), textcoords="offset points", xytext=(7, 4),
                fontsize=7.8, color=INK)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("cells", fontsize=9.4); ax.set_ylabel("E + 1  (defect)", fontsize=9.4)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(color="#f0f0f0", zorder=0)
ax.scatter([], [], color="white", edgecolor=BLUE, lw=2, marker="o", label="TRANSITION index — has a time column")
ax.scatter([], [], color="white", edgecolor=RED, lw=2, marker="s", label="STATE index — cannot have one")
ax.legend(frameon=False, fontsize=8.6, loc="upper left")
ax.set_title("The index landscape — every index this work builds or draws",
             fontsize=10.4, color=INK, pad=14)
save(fig, "fig-i2-landscape.png")

