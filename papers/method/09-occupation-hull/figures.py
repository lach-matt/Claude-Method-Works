#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

Imports check.py by path and draws from its compute(); nothing is drawn by hand and no number is
typed here.  Palette: light surface, recessive hairline grid, one blue for the hull and the
corridor, one orange for the observed entrant and the recalibration sites.
"""
import importlib.util
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("check", os.path.join(HERE, "check.py"))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e6e5e1"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
GREY = "#9a9894"
OUT = os.path.join(HERE, "figures")

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GRID, "axes.labelcolor": TEXT2,
    "xtick.color": TEXT2, "ytick.color": TEXT2, "axes.facecolor": SURFACE, "figure.facecolor": SURFACE,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1, "grid.linestyle": "-",
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})


def style(ax):
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


def fig1(Z=57, N=8, lmax=4):
    """The point set (sqrt(r), n) at one step, its lower hull, and the entrant's corridor."""
    prev, S, pts = check.step(Z, "p", N, lmax)
    H = check.hull_chain(pts)
    e = check.entrant(Z)
    i = S.index(e)
    lo, hi, _ = check.corridor(i, pts)
    xs = [math.sqrt(p[0]) for p in pts]
    ys = [p[1] for p in pts]
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 4.2), gridspec_kw=dict(width_ratios=[1.35, 1]))

    hx = [math.sqrt(pts[j][0]) for j in H]
    hy = [pts[j][1] for j in H]
    a.plot(hx, hy, "-", color=BLUE, lw=1.6, zorder=2)
    a.plot(xs, ys, "o", ms=5.5, color=GREY, mec=SURFACE, mew=1.4, zorder=3)
    a.plot(hx, hy, "o", ms=7.5, color=BLUE, mec=SURFACE, mew=1.6, zorder=4)
    a.plot([math.sqrt(pts[i][0])], [pts[i][1]], "o", ms=10, color=ORANGE, mec=SURFACE, mew=2, zorder=5)
    for j, s in enumerate(S):
        if s in {S[k] for k in H} or s == e:
            a.annotate(check.name(s), (xs[j], ys[j]), xytext=(5, 4), textcoords="offset points",
                       fontsize=7.5, color=TEXT2)
    k = H.index(i)
    for lab, sl, j0, j1 in (("L", lo, H[k - 1], i), ("U", hi, i, H[k + 1])):
        x0, y0 = math.sqrt(pts[j0][0]), pts[j0][1]
        x1, y1 = math.sqrt(pts[j1][0]), pts[j1][1]
        a.annotate("%s = %s" % (lab, check.closed(sl)), ((x0 + x1) / 2, (y0 + y1) / 2),
                   xytext=(0, -14 if lab == "L" else 10), textcoords="offset points",
                   fontsize=8, color=BLUE, ha="center")
    a.set_xlabel("x = √r")
    a.set_ylabel("y = n")
    a.set_title("the point set at Z = %d (%s), and its lower hull" % (Z, check.G.GROUND[Z][0]),
                fontsize=9.5, color=TEXT, loc="left")
    style(a)

    L, U = float(check.val(lo)), float(check.val(hi))
    grid = [L - 0.45 + 0.9 * t / 400 * (U - L + 0.9) / (U - L + 0.9) for t in range(401)]
    grid = [L - 0.45 + (U - L + 0.9) * t / 400 for t in range(401)]
    win = []
    for g in grid:
        vals = [(ys[j] - g * xs[j], j) for j in range(len(S))]
        win.append(min(vals)[1])
    seen = []
    for t, j in enumerate(win):
        if not seen or seen[-1][0] != j:
            seen.append((j, grid[t], grid[t]))
        else:
            seen[-1] = (j, seen[-1][1], grid[t])
    for j, g0, g1 in seen:
        col = ORANGE if j == i else BLUE
        b.barh(0, g1 - g0, left=g0, height=0.5, color=col, alpha=0.95 if j == i else 0.25,
               edgecolor=SURFACE, linewidth=1)
        b.text((g0 + g1) / 2, 0.38, check.name(S[j]), ha="center", va="bottom", fontsize=7.5,
               color=TEXT if j == i else TEXT2, rotation=90)
    b.axvline(L, color=TEXT2, lw=1)
    b.axvline(U, color=TEXT2, lw=1)
    b.text(L, -0.45, check.closed(lo), ha="center", va="top", fontsize=8, color=TEXT2)
    b.text(U, -0.45, check.closed(hi), ha="center", va="top", fontsize=8, color=TEXT2)
    b.set_ylim(-0.75, 0.95)
    b.set_yticks([])
    b.set_xlabel("slope a")
    b.set_title("which subshell a line of slope a reaches first", fontsize=9.5, color=TEXT, loc="left")
    style(b)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig1-hull-and-corridor.png"), dpi=200)
    plt.close(fig)


def fig2(out):
    """The 106 corridors as intervals on the slope axis, with the 19 endpoints."""
    cor = out["cor"]["p"]
    ends = sorted(float(check.val(dict(d))) for d, v in out["ends"]["p"])
    best, spans = out["cover"]["p"]          # the band as surds; drawn at their decimal value
    fig, ax = plt.subplots(figsize=(9.0, 6.6))
    XMIN, XMAX = -0.35, 5.35
    for g0, g1 in spans:
        ax.axvspan(XMIN if g0 is None else float(check.val(g0)), XMAX if g1 is None else float(check.val(g1)),
                   color=ORANGE, alpha=0.16, lw=0, zorder=0)
    ax.grid(axis="x", visible=False)
    for e in ends:
        ax.axvline(e, color="#c4c2bd", lw=0.9, zorder=1)
    for Z in check.STEPS:
        lo, hi, _ = cor[Z]
        L = XMIN if lo is None else float(check.val(lo))
        U = XMAX if hi is None else float(check.val(hi))
        ax.plot([L, U], [Z, Z], "-", color=BLUE, lw=2.2, solid_capstyle="butt", zorder=3)
        if lo is None:
            ax.plot([XMIN], [Z], "<", ms=4, color=BLUE, zorder=4)
    for Z in check.NUM["disjoint_p"]:
        lo, hi, _ = cor[Z]
        L = XMIN if lo is None else float(check.val(lo))
        U = XMAX if hi is None else float(check.val(hi))
        ax.plot([L, U], [Z, Z], "-", color=ORANGE, lw=2.6, solid_capstyle="butt", zorder=5)
        ax.annotate(check.G.GROUND[Z][0], (U, Z), xytext=(4, -3), textcoords="offset points",
                    fontsize=8, color=ORANGE)
    ax.set_xlim(XMIN, XMAX)
    ax.set_ylim(109, 2)
    ax.set_xlabel("slope a")
    ax.set_ylabel("Z")
    ax.set_yticks([3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 108])
    ax.set_title("the 106 corridors, the 19 distinct endpoints, and the widest band "
                 "one slope can cover (%d of 106)" % best, fontsize=9.5, color=TEXT, loc="left")
    style(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2-corridors.png"), dpi=200)
    plt.close(fig)


def fig3(out):
    """The walk: the corridor band, the carried slope, the real moves and the touches."""
    TR = out["TR"]
    BELOW = {58: (0, -17, "center"), 80: (-4, -17, "right"), 91: (2, -17, "left")}
    real = {t[0] for t in check.NUM["real_sites"]}
    touch = {t[0] for t in check.NUM["touch_sites"]}
    fig, ax = plt.subplots(figsize=(9.0, 4.4))
    YMIN, YMAX = -0.25, 5.35
    for t in TR:
        L = YMIN if t["lo"] is None else float(check.val(t["lo"]))
        U = YMAX if t["hi"] is None else float(check.val(t["hi"]))
        ax.plot([t["Z"], t["Z"]], [L, U], "-", color=GRID, lw=3.4, solid_capstyle="butt", zorder=1)
    ax.step([t["Z"] for t in TR], [t["a"] for t in TR], where="post", color=BLUE, lw=1.6, zorder=3)
    for t in TR:
        if t["Z"] in real:
            ax.plot([t["Z"]], [t["a"]], "o", ms=8, color=ORANGE, mec=SURFACE, mew=1.6, zorder=5)
            dx, dy, ha = BELOW.get(t["Z"], (0, 9, "center"))
            ax.annotate(check.G.GROUND[t["Z"]][0], (t["Z"], t["a"]), xytext=(dx, dy),
                        textcoords="offset points", fontsize=8, color=ORANGE, ha=ha)
        elif t["Z"] in touch:
            ax.plot([t["Z"]], [t["a"]], "o", ms=5.5, color=SURFACE, mec=ORANGE, mew=1.6, zorder=5)
    ax.set_xlim(2, 109)
    ax.set_ylim(YMIN, 3.0)
    ax.set_xlabel("Z")
    ax.set_ylabel("slope a")
    ax.set_title("the carried slope against Z: %d recalibrations, %d that move it (filled), "
                 "%d that do not (open)" % (check.NUM["recal"], check.NUM["real"], check.NUM["touch"]),
                 fontsize=9.5, color=TEXT, loc="left")
    style(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig3-walk-and-resets.png"), dpi=200)
    plt.close(fig)


def main():
    os.makedirs(OUT, exist_ok=True)
    check.QUIET[0] = True
    out = check.compute(quiet=True)
    fig1()
    fig2(out)
    fig3(out)
    for f in sorted(os.listdir(OUT)):
        print("  figures/%s" % f)


if __name__ == "__main__":
    main()
