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
st = ["Λ₈", "Λ₉", "Λ₁₀", "Λ₁₁", "Λ₁₂", "Λ₁₃"]
fr = [0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381]
kind = ["base", "counting", "counting", "coupling", "coupling", "coupling"]
fig, ax = plt.subplots(figsize=(8.4, 4.2), dpi=160)
for i in range(len(st) - 1):
    c = BLUE if kind[i+1] == "counting" else RED
    ax.plot([i, i+1], [fr[i], fr[i+1]], color=c, lw=2.6, zorder=2)
for i, (x, y) in enumerate(zip(range(len(st)), fr)):
    c = BLUE if kind[i] == "counting" else (RED if kind[i] == "coupling" else INK)
    ax.scatter([x], [y], s=90, color="white", edgecolor=c, lw=2.2, zorder=3)
    ax.annotate(f"{y:.3f}", (x, y), textcoords="offset points", xytext=(0, 13),
                ha="center", fontsize=8.6, color=INK)
ax.annotate("peak", (2, fr[2]), textcoords="offset points", xytext=(0, 30),
            ha="center", fontsize=9, color=INK, style="italic")
ax.set_xticks(range(len(st))); ax.set_xticklabels(st, fontsize=11)
ax.set_ylim(-0.06, 0.95); ax.set_ylabel("composable fraction", fontsize=9.4)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", color="#eeeeee", zorder=0)
ax.plot([], [], color=BLUE, lw=2.6, label="a COUNTING axis was added")
ax.plot([], [], color=RED, lw=2.6, label="a COUPLING axis was added")
ax.legend(frameon=False, fontsize=8.8, loc="lower right")
ax.set_title("Composability up the tower — counting axes raise it, coupling axes lower it",
             fontsize=10.4, color=INK, pad=14)
save(fig, "fig-i1-tower.png")

