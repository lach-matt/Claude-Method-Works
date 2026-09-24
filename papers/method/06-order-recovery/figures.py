#!/usr/bin/env python3
"""figures.py -- every computed figure of PAPER.md, drawn from check.py's results.json and from
nothing else.

    python3 check.py            (writes results.json)
    python3 figures.py          (writes figures/fig*.png)

The two audited plates in figures/ -- figure-15.1.png and figure-30.2.png -- are NOT drawn here;
they are copied files and FIGURES.tsv records their provenance and md5.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt          # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")
R = json.load(open(os.path.join(HERE, "results.json")))

BLUE = "#2b6a8f"
RED = "#a8322a"
GREY = "#8a8a8a"
LIGHT = "#dce6ec"
plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "figure.dpi": 200,
                     "axes.spines.top": False, "axes.spines.right": False})


def _grid(ax, cells, nx, ny, colour, title, sub):
    ax.set_title(title, color=colour, fontsize=10, pad=8)
    for (u, b) in cells:
        ax.add_patch(Rectangle((u + 0.08, b + 0.08), 0.84, 0.84, facecolor=colour,
                               edgecolor="none"))
    ax.set_xlim(-0.15, nx + 0.15)
    ax.set_ylim(-0.15, ny + 0.15)
    ax.set_xticks([i + 0.5 for i in range(nx)])
    ax.set_xticklabels(range(nx))
    ax.set_yticks([i + 0.5 for i in range(ny)])
    ax.set_yticklabels(range(ny))
    ax.set_aspect("equal")
    ax.tick_params(length=0, labelsize=7)
    for s in ax.spines.values():
        s.set_color(GREY)
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax.set_xlabel(sub, fontsize=8, color="#444444", labelpad=6)


def fig_example():
    """Figure 1: the worked example built, scrambled, its may-precede digraph, recovered."""
    E = R["example"]
    built = [tuple(c) for c in E["cells"]]
    scr = [tuple(c) for c in E["scrambled"]]
    r0, r1 = E["recovered0"], E["recovered1"]
    rank0 = {v: i for i, v in enumerate(r0)}
    rank1 = {v: i for i, v in enumerate(r1)}
    rec = [(rank0[u], rank1[b]) for (u, b) in scr]

    fig = plt.figure(figsize=(9.6, 3.1))
    gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1.35, 1], wspace=0.34)
    _grid(fig.add_subplot(gs[0, 0]), built, 5, 4, BLUE, "as built",
          "%d cells; every fibre an interval" % E["n_cells"])
    _grid(fig.add_subplot(gs[0, 1]), scr, 5, 4, RED, "both alphabets permuted",
          "the same cells, relabelled")

    ax = fig.add_subplot(gs[0, 2])
    vals, P = E["vals"], E["P"]
    idx = {v: k for k, v in enumerate(vals)}
    lay = [idx[v] for v in r0]                    # nodes left to right in the recovered order
    n = len(lay)
    pos = {k: (k, 0.0) for k in range(n)}
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            i, j = lay[a], lay[b]
            if not P[i][j]:
                continue
            if b > a:
                rad, col, y = 0.16 + 0.10 * (b - a), BLUE, 1
            else:
                rad, col, y = -0.55, RED, -1
            ax.add_patch(FancyArrowPatch(pos[a], pos[b], connectionstyle="arc3,rad=%.2f" % (y * rad),
                                         arrowstyle="-|>", mutation_scale=6,
                                         color=col, lw=0.7, shrinkA=7, shrinkB=7, zorder=2))
    for k in range(n):
        ax.add_patch(plt.Circle(pos[k], 0.20, facecolor="white", edgecolor="#333333", lw=0.9,
                                zorder=3))
        ax.text(pos[k][0], pos[k][1], str(vals[lay[k]]), ha="center", va="center",
                fontsize=7.5, zorder=4)
    ax.set_xlim(-0.8, n - 0.2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")
    tie = E["ties"][0]
    ax.text(0.5, 0.955, "may precede", transform=ax.transAxes, ha="center", fontsize=10)
    ax.text(0.5, 0.055, "a total preorder; one tie: %d ⊑ %d and %d ⊑ %d"
            % (tie[0], tie[1], tie[1], tie[0]), transform=ax.transAxes, ha="center", fontsize=7.5,
            color="#444444")

    _grid(fig.add_subplot(gs[0, 3]), rec, 5, 4, BLUE, "recovered",
          "%d of the 2,880 orderings admit it" % E["admissible"])
    fig.savefig(os.path.join(FIG, "fig1-example.png"), bbox_inches="tight")
    plt.close(fig)


def fig_arity():
    """Figure 4: the constraint language by arity, and the reorderable share of each box."""
    ex = R["bijunctive_exact"]
    ms = sorted(int(k) for k in ex)
    tot = [ex[str(m)]["relations_containing_zero"] for m in ms]
    bij = [ex[str(m)]["bijunctive"] for m in ms]
    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.3))

    ax = axs[0]
    xs = range(len(ms))
    ax.bar(xs, [1] * len(ms), color=LIGHT, edgecolor=GREY, lw=0.5, width=0.62)
    ax.bar(xs, [b / t for b, t in zip(bij, tot)], color=BLUE, width=0.62)
    for i, (b, t) in enumerate(zip(bij, tot)):
        ax.text(i, 1.025, "{:,} / {:,}".format(b, t), ha="center", fontsize=7.5)
    ax.axvline(1.5, color=RED, ls="--", lw=1.1)
    ax.text(1.56, 0.30, "the boundary", color=RED, fontsize=8, rotation=90)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([str(m + 1) for m in ms])
    ax.set_xlabel("constraint arity")
    ax.set_ylabel("fraction closed under the majority")
    ax.set_ylim(0, 1.16)
    ax.set_title("the language leaves the bijunctive class at arity 4")

    ax = axs[1]
    rows = [r for r in R["census"]]
    labs = ["×".join(map(str, r["box"])) for r in rows]
    frac = [r["reorderable_all"] / r["subsets"] for r in rows]
    cols = [BLUE if len(r["box"]) == 2 else (RED if len(r["box"]) == 3 else "#4d4d4d") for r in rows]
    ax.bar(range(len(rows)), frac, color=cols, width=0.66)
    for i, r in enumerate(rows):
        ax.text(i, frac[i] + 0.022, "%d" % r["step"], ha="center", fontsize=7.5, color="#333333")
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels(labs, rotation=60, fontsize=7.5, ha="right")
    ax.set_ylabel("subsets closed under some ordering")
    ax.set_ylim(0, 1.16)
    ax.set_title("the reorderable share, and the growth step above each bar")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig4-arity.png"), bbox_inches="tight")
    plt.close(fig)


def fig_amplification():
    """Figure 5: the cost of one fabricated cell, over every ambient non-cell."""
    A = R["amplification"]
    v = A["values"]
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.hist(v, bins=60, color=BLUE, edgecolor="none")
    ax.axvline(0, color=RED, ls="--", lw=1.2)
    ax.annotate("an undetectable insertion would sit here", xy=(0, ax.get_ylim()[1] * 0.20),
                xytext=(max(v) * 0.34, ax.get_ylim()[1] * 0.97), color=RED, fontsize=8,
                va="top", arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))
    ax.axvline(A["min"], color="#333333", lw=1.0)
    ax.text(A["min"], ax.get_ylim()[1] * 0.62, "  minimum %d" % A["min"], fontsize=8)
    ax.axvline(A["median"], color="#333333", ls=":", lw=1.0)
    ax.text(A["median"], ax.get_ylim()[1] * 0.80, "  median %.0f" % A["median"], fontsize=8)
    ax.set_xlabel("further cells the closure must admit")
    ax.set_ylabel("ambient non-cells")
    ax.set_title("every one of the %s non-cells costs something to insert" % f"{A['noncells']:,}")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig5-amplification.png"), bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(FIG, exist_ok=True)
    fig_example()
    fig_arity()
    fig_amplification()
    for f in sorted(os.listdir(FIG)):
        print("  figures/%s  %d bytes" % (f, os.path.getsize(os.path.join(FIG, f))))
