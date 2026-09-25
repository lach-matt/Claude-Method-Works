#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

Nothing is drawn by hand: each figure is computed from the reference implementation in check.py
(imported by path), and every number in a caption is one check.py prints.
"""
import importlib.util
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("check", os.path.join(HERE, "check.py"))
check = importlib.util.module_from_spec(spec)
sys.modules["check"] = check
spec.loader.exec_module(check)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#d6d5d0"
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK})


def fig1_staircase():
    """A five-cell X in a 5 x 5 box, its staircase closure, and the two boundary functions."""
    X = {(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)}
    R = check.stair(X)
    ph = check.phi(X)
    A = check.alphabets(X)
    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    n = 5
    for s in range(n):
        for t in range(n):
            c = (s, t)
            if c in X:
                fc, ec = BLUE, BLUE
            elif c in R:
                fc, ec = ORANGE, ORANGE
            else:
                fc, ec = "white", GRID
            ax.add_patch(Rectangle((s + 0.08, t + 0.08), 0.84, 0.84, facecolor=fc, edgecolor=ec, linewidth=0.8))
    # phi_21(s): the largest second coordinate reachable with first coordinate <= s (upper staircase)
    xs, ys = [], []
    for s in A[0]:
        xs += [s, s + 1]
        ys += [ph[1, 0, s] + 1, ph[1, 0, s] + 1]
    ax.plot(xs, ys, color=INK, linewidth=1.6, solid_capstyle="butt")
    ax.text(2.5, ph[1, 0, 2] + 1.12, "φ₂₁", ha="center", va="bottom", fontsize=9, color=INK)
    # phi_12(t): the largest first coordinate reachable with second coordinate <= t (right staircase)
    xs, ys = [], []
    for t in A[1]:
        ys += [t, t + 1]
        xs += [ph[0, 1, t] + 1, ph[0, 1, t] + 1]
    ax.plot(xs, ys, color=INK, linewidth=1.6, linestyle=(0, (3, 2)))
    ax.text(ph[0, 1, 4] + 1.12, 4.55, "φ₁₂", ha="left", va="center", fontsize=9, color=INK)
    ax.set_xlim(-0.2, 5.6)
    ax.set_ylim(-0.2, 5.6)
    ax.set_xticks([i + 0.5 for i in range(n)])
    ax.set_xticklabels(range(n))
    ax.set_yticks([i + 0.5 for i in range(n)])
    ax.set_yticklabels(range(n))
    ax.set_xlabel("x₁")
    ax.set_ylabel("x₂")
    ax.set_aspect("equal")
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.tick_params(length=0)
    ax.add_patch(Rectangle((0.15, 5.05), 0.3, 0.3, facecolor=BLUE, edgecolor=BLUE))
    ax.text(0.55, 5.2, "X, %d cells" % len(X), va="center", fontsize=8.5, color=INK)
    ax.add_patch(Rectangle((2.35, 5.05), 0.3, 0.3, facecolor=ORANGE, edgecolor=ORANGE))
    ax.text(2.75, 5.2, "ℛ(X) ∖ X, %d cells" % (len(R) - len(X)), va="center", fontsize=8.5, color=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig1-staircase.png"), dpi=220)
    plt.close(fig)
    return X, R


def fig2_moore():
    """The thirteen closed subsets of the 2 x 2 box, as the Hasse diagram of the Moore family."""
    cells = [(0, 0), (0, 1), (1, 0), (1, 1)]
    fam = [frozenset()] + [frozenset(c for i, c in enumerate(cells) if m >> i & 1) for m in range(1, 16)
                           if check.is_closed(frozenset(c for i, c in enumerate(cells) if m >> i & 1))]
    assert len(fam) == 13
    covers = [(a, b) for a in fam for b in fam if a < b and not any(a < c < b for c in fam)]
    levels = {}
    for S in fam:
        levels.setdefault(len(S), []).append(S)
    pos = {}
    for k, group in levels.items():
        group.sort(key=lambda S: sorted(S))
        w = len(group)
        for i, S in enumerate(group):
            pos[S] = ((i - (w - 1) / 2) * 1.35, k * 1.5)
    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    for a, b in covers:
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=GRID, linewidth=0.9, zorder=1)
    for S, (x, y) in pos.items():
        for (s, t) in cells:
            fc = BLUE if (s, t) in S else "white"
            ax.add_patch(Rectangle((x - 0.42 + s * 0.42, y - 0.42 + t * 0.42), 0.40, 0.40, facecolor=fc, edgecolor=MUTED, linewidth=0.6, zorder=3))
    # the one pair whose union escapes: two 2-chains through (0,0)
    S1, S2 = frozenset({(0, 0), (1, 0)}), frozenset({(0, 0), (0, 1)})
    for S in (S1, S2):
        x, y = pos[S]
        ax.add_patch(Rectangle((x - 0.52, y - 0.52), 1.04, 1.04, facecolor="none", edgecolor=ORANGE, linewidth=1.4, zorder=4))
    ax.text(0, -0.95, "∅", ha="center", va="center", fontsize=9, color=INK)
    for k in range(1, 5):
        ax.text(-4.6, k * 1.5, "%d cell%s: %d" % (k, "" if k == 1 else "s", len(levels[k])), ha="left", va="center", fontsize=8.5, color=MUTED)
    ax.text(-4.6, 0, "empty: 1", ha="left", va="center", fontsize=8.5, color=MUTED)
    ax.set_xlim(-4.8, 4.2)
    ax.set_ylim(-1.3, 6.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig3-moore-family.png"), dpi=220)
    plt.close(fig)
    return len(fam), len(covers)


def fig3_nine():
    """The nine-cell staircase between L(s) = floor(s/2) and U(s) = s + floor(s/3)."""
    L = lambda s: s // 2
    U = lambda s: s + s // 3
    nine = {(s, t) for s in range(4) for t in range(6) if L(s) <= t <= U(s)}
    assert check.stair(nine) == nine
    fig, ax = plt.subplots(figsize=(3.6, 4.4))
    for s in range(4):
        for t in range(5):
            fc = BLUE if (s, t) in nine else "white"
            ec = BLUE if (s, t) in nine else GRID
            ax.add_patch(Rectangle((s + 0.08, t + 0.08), 0.84, 0.84, facecolor=fc, edgecolor=ec, linewidth=0.8))
    xs, ys = [], []
    for s in range(4):
        xs += [s, s + 1]
        ys += [U(s) + 1, U(s) + 1]
    ax.plot(xs, ys, color=INK, linewidth=1.6)
    ax.text(4.1, U(3) + 1, "U(s) = s + ⌊s/3⌋", va="center", fontsize=8.5, color=INK)
    xs, ys = [], []
    for s in range(4):
        xs += [s, s + 1]
        ys += [L(s), L(s)]
    ax.plot(xs, ys, color=INK, linewidth=1.6, linestyle=(0, (3, 2)))
    ax.text(4.1, L(3), "L(s) = ⌊s/2⌋", va="center", fontsize=8.5, color=INK)
    ax.set_xlim(-0.2, 4.2)
    ax.set_ylim(-0.2, 5.2)
    ax.set_xticks([i + 0.5 for i in range(4)])
    ax.set_xticklabels(range(4))
    ax.set_yticks([i + 0.5 for i in range(5)])
    ax.set_yticklabels(range(5))
    ax.set_xlabel("s")
    ax.set_ylabel("t")
    ax.set_aspect("equal")
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.tick_params(length=0)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2-staircase-algebra.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)
    return sorted(nine)


RED = "#c0392b"


def fig_periodic():
    """The 18-column table on (period, group): the 90 held cells and the 36 the staircase adds."""
    pt = check.periodic_cells(18)
    R = check.stair(pt)
    gaps = R - pt
    assert len(pt) == 90 and len(R) == 126 and len(gaps) == 36
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    for p in range(1, 8):
        for g in range(1, 19):
            c = (p, g)
            if c in pt:
                fc, ec = BLUE, BLUE
            elif c in gaps:
                fc, ec = RED, RED
            else:
                fc, ec = "white", GRID
            ax.add_patch(Rectangle((g + 0.08, 8 - p + 0.08), 0.84, 0.84, facecolor=fc, edgecolor=ec, linewidth=0.8))
    ax.set_xlim(0.9, 19.1)
    ax.set_ylim(0.9, 8.1)
    ax.set_xticks([g + 0.5 for g in range(1, 19)])
    ax.set_xticklabels(range(1, 19))
    ax.set_yticks([8 - p + 0.5 for p in range(1, 8)])
    ax.set_yticklabels(range(1, 8))
    ax.set_xlabel("group")
    ax.set_ylabel("period")
    ax.set_aspect("equal")
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.tick_params(length=0)
    # legend below the grid, clear of every cell
    ax.add_patch(Rectangle((1.1, -0.85), 0.5, 0.5, facecolor=BLUE, edgecolor=BLUE, clip_on=False))
    ax.text(1.75, -0.6, "held, %d cells" % len(pt), va="center", fontsize=8.5, color=INK)
    ax.add_patch(Rectangle((6.1, -0.85), 0.5, 0.5, facecolor=RED, edgecolor=RED, clip_on=False))
    ax.text(6.75, -0.6, "admitted by ℛ and denied by the table, %d cells" % len(gaps), va="center", fontsize=8.5, color=INK)
    fig.subplots_adjust(bottom=0.3)
    fig.savefig(os.path.join(OUT, "fig-periodic-table.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)
    return len(pt), len(R), len(gaps)


def fig4_seed():
    """The seed of the full box c^d: the exact law c - 2 + m(d) against the linear d + c - 2."""
    ds = list(range(2, 36))
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for c, col, dy in ((2, BLUE, 0), (3, AQUA, 0)):
        ex = [check.seed_formula_box(c, d) for d in ds]
        ax.step(ds, ex, where="post", color=col, linewidth=2.0)
        ax.text(ds[-1] + 0.4, ex[-1], "c = %d, exact" % c, va="center", fontsize=8.5, color=INK)
    lin = [d + 2 - 2 for d in ds]
    ax.plot(ds, lin, color=ORANGE, linewidth=1.4, linestyle=(0, (3, 2)))
    ax.text(16.6, 14.2, "d + c − 2 at c = 2", fontsize=8.5, color=INK, ha="left")
    # the exhaustively verified points
    pts = [(2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3)]
    ax.scatter([d for c, d in pts], [check.seed_formula_box(c, d) for c, d in pts], s=28, facecolor="white", edgecolor=INK, linewidth=1.0, zorder=5)
    ax.set_xlabel("d, the number of coordinates")
    ax.set_ylabel("cells in a minimum seed")
    ax.set_xlim(1.5, 41)
    ax.set_ylim(0, 16)
    ax.set_yticks(range(0, 17, 2))
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4-seed-law.png"), dpi=220)
    plt.close(fig)


if __name__ == "__main__":
    X, R = fig1_staircase()
    print("fig1: |X| = %d, |R(X)| = %d, E = %d" % (len(X), len(R), len(R) - len(X)))
    n, e = fig2_moore()
    print("fig2: %d closed subsets of 2x2, %d covering relations" % (n, e))
    print("fig3: nine cells", fig3_nine())
    print("fig-periodic: held %d, |R| = %d, gaps %d" % fig_periodic())
    fig4_seed()
    print("fig4: written")
