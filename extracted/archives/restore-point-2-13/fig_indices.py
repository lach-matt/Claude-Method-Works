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
fr = [0.0000, 0.7068, 0.8087, 0.6956, 0.6394, 0.6186]
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

# ---------------------------------------------------------------- i2
objs = [("Λ₈", 976, 0, "t"), ("Λ₉", 1654, 0, "t"), ("Λ₁₀", 2535, 0, "t"),
        ("Λ₁₃", 64290, 0, "t"), ("violation index", 2370, 30, "t"),
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

# ---------------------------------------------------------------- i3
POS = {"n": (0, 1), "ℓ": (1, 1), "k": (2, 1), "q": (3, 1),
       "g": (4.2, 1), "f": (5.4, 1), "e": (6.4, 1), "2S": (2, 0.42)}
E1 = [("ℓ", "n"), ("k", "ℓ"), ("q", "k"), ("2S", "k"), ("f", "e")]
fig, ax = plt.subplots(figsize=(9.2, 3.4), dpi=160)
for a, b in E1:
    x1, y1 = POS[a]; x2, y2 = POS[b]
    ax.annotate("", xy=(x1, y1), xytext=(x2, y2),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.4, shrinkA=15, shrinkB=15))
for a in ("q", "f"):
    x1, y1 = POS["g"]; x2, y2 = POS[a]
    ax.annotate("", xy=(x1, y1), xytext=(x2, y2),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4, shrinkA=15, shrinkB=15))
for nm, (x, y) in POS.items():
    hub = nm in ("k", "g")
    ax.add_patch(plt.Circle((x, y), 0.2, facecolor="white",
                            edgecolor=RED if nm == "g" else INK, lw=2.2 if hub else 1.4, zorder=3))
    ax.text(x, y, nm, ha="center", va="center", fontsize=10.5,
            fontweight="bold" if hub else "normal", zorder=4)
ax.text(4.2, 0.30, "g ≤ min(q, 4f+2)", ha="center", fontsize=9.4, color=RED)
ax.text(4.2, 0.09, "the one coupling — and it is the Pauli principle", ha="center",
        fontsize=8.2, color=RED, style="italic")
ax.text(-0.4, 1.62, "Λ₈ · eight coordinates · seven constraints · a caterpillar with 2S pendant at k",
        fontsize=9.2, color=INK)
ax.set_xlim(-0.6, 7.1); ax.set_ylim(-0.05, 1.8); ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-i3-lambda8.png")

# ---------------------------------------------------------------- i4
lbl = ["all cells", "EM-allowed\n|Δℓ| = 1", "EM-forbidden", "parity\nconserving", "parity\nchanging"]
wi = [0.227, 0.116, 0.407, 0.384, 0.201]
ac = [0.852, 0.897, 0.779, 0.898, 0.845]
x = range(len(lbl))
fig, ax = plt.subplots(figsize=(8.4, 4.2), dpi=160)
ax.bar([i - 0.19 for i in x], wi, width=0.36, color="white", edgecolor=RED, lw=2,
       label="composable WITHIN one element")
ax.bar([i + 0.19 for i in x], ac, width=0.36, color="white", edgecolor=BLUE, lw=2,
       label="composable ACROSS the 118")
for i, (a, b) in enumerate(zip(wi, ac)):
    ax.text(i - 0.19, a + 0.02, f"{a:.3f}", ha="center", fontsize=8, color=RED)
    ax.text(i + 0.19, b + 0.02, f"{b:.3f}", ha="center", fontsize=8, color=BLUE)
ax.set_xticks(list(x)); ax.set_xticklabels(lbl, fontsize=8.6)
ax.set_ylim(0, 1.02); ax.set_ylabel("composable fraction", fontsize=9.4)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", color="#f0f0f0", zorder=0)
ax.legend(frameon=False, fontsize=8.8, loc="upper left")
ax.set_title("The crossing — allowed transitions compose least within an atom and most between atoms",
             fontsize=10.2, color=INK, pad=14)
save(fig, "fig-i4-crossing.png")
