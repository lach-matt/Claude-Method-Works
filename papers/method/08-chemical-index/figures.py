#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

check.py writes figures/check-results.json on every run; this script reads it and draws.  Run
check.py first.  Nothing here is drawn by hand.

    python3 check.py && python3 figures.py
"""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")
RES = os.path.join(FIG, "check-results.json")
if not os.path.isfile(RES):
    print("run check.py first (it writes figures/check-results.json)")
    sys.exit(1)
R = json.load(open(RES, encoding="utf-8"))

# one hue for magnitude/identity, a second only where two series must be told apart
INK = "#0b0b0b"
INK2 = "#52514e"
BLUE = "#2a78d6"
BLUE_FILL = "#dce8f8"
ORANGE = "#eb6834"
GRID = "#c9c8c3"
EMPTY = "#f4f4f2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GRID,
                     "axes.linewidth": 0.6, "text.color": INK, "axes.labelcolor": INK,
                     "xtick.color": INK2, "ytick.color": INK2})

ORD_K = R["ORD_K"]      # kind, in the closing order
ORD_P = R["ORD_P"]      # dependency, in the closing order
SEATS = R["ORD_S"]
PNAME = {"P": "physics parameter", "C": "charge role", "A": "amplitude integral"}
grid = {tuple(int(v) for v in k.split(",")): names for k, names in R["grid"].items()}


# ------------------------------------------------------------------ Figure 1: the fourteen cells
def fig1():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), gridspec_kw={"width_ratios": [1, 1]})
    for si, ax in enumerate(axes):
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 4)
        ax.set_aspect("auto")
        ax.set_xticks([i + 0.5 for i in range(3)])
        ax.set_xticklabels([PNAME[p] for p in ORD_P])
        ax.set_yticks([i + 0.5 for i in range(4)])
        ax.set_yticklabels(ORD_K)
        ax.tick_params(length=0)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(SEATS[si], fontsize=10, color=INK, pad=8)
        for k in range(4):
            for p in range(3):
                names = grid.get((k, si, p), [])
                held = bool(names)
                ax.add_patch(Rectangle((p + 0.03, k + 0.03), 0.94, 0.94, facecolor=BLUE_FILL if held else EMPTY,
                                       edgecolor=BLUE if held else GRID, linewidth=1.0 if held else 0.5))
                if held:
                    ax.text(p + 0.5, k + 0.5, "\n".join(names), ha="center", va="center", fontsize=7.2, color=INK)
        if si == 1:
            # the last cell: symmetry x valence x charge
            k = ORD_K.index("symmetry")
            p = ORD_P.index("C")
            ax.add_patch(Rectangle((p + 0.03, k + 0.03), 0.94, 0.94, facecolor="none", edgecolor=ORANGE,
                                   linewidth=2.0, linestyle=(0, (4, 2))))
    axes[0].set_ylabel("kind, in the closing order  →", color=INK2)
    fig.text(0.5, 0.01, "dependency, in the closing order  →", ha="center", color=INK2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(FIG, "fig1-chem-grid.png"), dpi=200)
    plt.close(fig)


# ------------------------------------------------------------------ Figure 2: routing by residual
def fig2():
    routes = R["ROUTE"]   # (residual, property, kind, seat, pca, breadth, class)
    n = len(routes)
    props = []
    for r in routes:
        if r[1] not in props:
            props.append(r[1])
    m = len(props)
    fig, ax = plt.subplots(figsize=(9.6, 3.9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, n + 0.55)
    ax.axis("off")
    for x, label in ((0.15, "residual left by a universal form"),
                     (3.55, "property (kind · seat · dependency)"),
                     (7.85, "class the property holds on")):
        ax.text(x, n + 0.22, label, fontsize=8.5, color=INK2, va="bottom")
    # left lane: one row per residual; right lane: one non-overlapping slot per property
    ry = {i: n - 0.5 - i for i in range(n)}
    py = {prop: n * (m - 0.5 - j) / m for j, prop in enumerate(props)}
    for i, r in enumerate(routes):
        ax.text(0.15, ry[i], r[0], fontsize=8.6, va="center", color=INK)
        ax.add_patch(FancyArrowPatch((3.05, ry[i]), (3.48, py[r[1]]), arrowstyle="-|>",
                                     mutation_scale=9, color=BLUE, linewidth=1.0))
    for prop in props:
        y = py[prop]
        r = next(x for x in routes if x[1] == prop)
        ax.add_patch(Rectangle((3.5, y - 0.40), 3.9, 0.80, facecolor=BLUE_FILL, edgecolor=BLUE,
                               linewidth=1.0))
        ax.text(3.68, y + 0.13, prop, fontsize=8.8, va="center", color=INK)
        ax.text(3.68, y - 0.16, "%s · %s · %s" % (r[2], r[3].replace("the ", ""), PNAME[r[4]]),
                fontsize=7.4, va="center", color=INK2)
        ax.add_patch(FancyArrowPatch((7.42, y), (7.78, y), arrowstyle="-|>", mutation_scale=9,
                                     color=BLUE, linewidth=1.0))
        ax.text(7.85, y, r[6], fontsize=8.6, va="center", color=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig2-routing.png"), dpi=200)
    plt.close(fig)


# ------------------------------------------------------------------ Figure 3: the boundary
def fig3():
    labels = ["subvalence\n+ valence", "+ the core", "+ the nucleus", "+ the aggregate", "all five seats"]
    filled = R["got_filled"]
    held = R["got_held"]
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    xs = list(range(5))
    w = 0.36
    ax.bar([x - w / 2 for x in xs], [e for _, e in filled], width=w, color=BLUE, label="term symbol on the charge role (closed index)")
    ax.bar([x + w / 2 for x in xs], [e for _, e in held], width=w, color=ORANGE, label="term symbol on a physics parameter (before the fill)")
    for x, (n, e) in zip(xs, filled):
        ax.text(x - w / 2, e + 0.3, "%d\n(%d cells)" % (e, n), ha="center", va="bottom", fontsize=7.4, color=INK)
    for x, (n, e) in zip(xs, held):
        ax.text(x + w / 2, e + 0.3, "%d\n(%d cells)" % (e, n), ha="center", va="bottom", fontsize=7.4, color=INK)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels)
    ax.set_ylabel("minimum defect E over every ordering")
    ax.set_ylim(0, 23)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=7.8, loc="upper left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig3-boundary.png"), dpi=200)
    plt.close(fig)


# ------------------------------------------------------------------ Figure 4: the merged index
def fig4():
    table = R["pca_table"]   # rows standard, mathematics, literature, this work; cols the six domains
    srcs = ["standard", "mathematics", "literature", "this work"]
    doms = ["universal", "all elements", "low (c = 2)", "neutral (c = 1)", "hydrogenic (c ≥ 3)", "one species"]
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4)
    ax.set_xticks([i + 0.5 for i in range(6)])
    ax.set_xticklabels(doms, fontsize=8)
    ax.set_yticks([i + 0.5 for i in range(4)])
    ax.set_yticklabels(srcs)
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    for s in range(4):
        for d in range(6):
            n = table[s][d]
            ax.add_patch(Rectangle((d + 0.03, s + 0.03), 0.94, 0.94, facecolor=BLUE_FILL if n else EMPTY,
                                   edgecolor=BLUE if n else GRID, linewidth=1.0 if n else 0.5))
            if n:
                ax.text(d + 0.5, s + 0.5, str(n), ha="center", va="center", fontsize=11, color=INK)
    # the staircase L(s) = floor(s/2), U(s) = s + floor(s/3), drawn as the two boundary paths
    L = [s // 2 for s in range(4)]
    U = [s + s // 3 for s in range(4)]
    for s in range(4):
        ax.plot([L[s], L[s]], [s, s + 1], color=ORANGE, linewidth=2)
        ax.plot([U[s] + 1, U[s] + 1], [s, s + 1], color=ORANGE, linewidth=2)
        if s < 3:
            ax.plot([L[s], L[s + 1]], [s + 1, s + 1], color=ORANGE, linewidth=2)
            ax.plot([U[s] + 1, U[s + 1] + 1], [s + 1, s + 1], color=ORANGE, linewidth=2)
    ax.text(0.08, 3.86, "L(s) = ⌊s/2⌋", color=ORANGE, fontsize=8, va="top")
    ax.text(5.05, 3.86, "U(s) = s + ⌊s/3⌋", color=ORANGE, fontsize=8, va="top")
    ax.set_xlabel("domain d, in the closing order  →", color=INK2)
    ax.set_ylabel("source s, in the closing order  →", color=INK2)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig4-pca-grid.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    print("figures written to", FIG)
