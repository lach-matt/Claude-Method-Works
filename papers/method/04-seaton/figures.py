#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

Imports check.py by path and draws from its run_fits()/stats(); nothing is drawn by hand and no
number is typed here.  Palette: the dataviz reference instance (slot 1 blue for p = 0, slot 2
orange for p >= 1), light surface, recessive hairline grid, >= 8 px markers with a surface ring.
"""
import importlib.util
import os
import sys

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


def fmt(x, nd=3):
    """A number with a true minus sign, as the axes print it."""
    return ("%.*f" % (nd, x)).replace("-", "\u2212")


def fig1(rows, st):
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.9))
    # (a) delta2/delta0 for all thirteen, against p, with Seaton's value per l
    for r in rows:
        col = BLUE if r["p"] == 0 else ORANGE
        a.plot(r["p"], float(r["d2"] / r["d0"]), "o", ms=8, color=col, mec=SURFACE, mew=2, zorder=3)
    for l, y, lab in ((1, -2 / 3, "ℓ = 1"), (2, -2.0, "ℓ = 2"), (3, -4.0, "ℓ = 3")):
        a.axhline(y, color=TEXT2, lw=1, zorder=1)
        a.text(5.6, y, "\u2212\u2113(\u2113+1)/3, " + lab, va="bottom", ha="left", fontsize=7.5, color=TEXT2)
    a.axhline(0, color=TEXT2, lw=1, zorder=1)
    a.text(5.6, 0, "\u2212\u2113(\u2113+1)/3, \u2113 = 0", va="bottom", ha="left", fontsize=7.5, color=TEXT2)
    for r in rows:
        if r["p"] == 0 or r["name"] in ("In I d", "Rb I d"):
            a.annotate(r["name"], (r["p"], float(r["d2"] / r["d0"])), xytext=(6, -2), textcoords="offset points",
                       fontsize=7.5, color=TEXT2)
    a.set_xlim(-0.5, 7.6)
    a.set_xticks(range(6))
    a.set_xlabel("p, core orbitals of the channel's ℓ")
    a.set_ylabel("δ₂ / δ₀")
    a.set_title("(a) the fitted ratio, all thirteen series", loc="left", fontsize=9.5, color=TEXT)
    style(a)
    # (b) rho against p with class medians and population-sd bands
    p0 = [r for r in rows if r["rho"] is not None and r["p"] == 0]
    p1 = [r for r in rows if r["rho"] is not None and r["p"] >= 1]
    b.axhspan(st["p0_median"] - st["p0_sd"], st["p0_median"] + st["p0_sd"], xmin=0.03, xmax=0.22, color=BLUE, alpha=0.10, lw=0)
    b.axhspan(st["p1_median"] - st["p1_sd"], st["p1_median"] + st["p1_sd"], xmin=0.22, xmax=0.97, color=ORANGE, alpha=0.10, lw=0)
    b.plot([-0.3, 0.5], [st["p0_median"]] * 2, color=BLUE, lw=2, solid_capstyle="round")
    b.plot([0.5, 3.6], [st["p1_median"]] * 2, color=ORANGE, lw=2, solid_capstyle="round")
    b.axhline(1.0, color=TEXT2, lw=1)
    b.text(4.05, 1.0, "ρ = 1", va="bottom", ha="left", fontsize=7.5, color=TEXT2)
    for r in p0:
        b.plot(r["p"], r["rho"], "o", ms=8, color=BLUE, mec=SURFACE, mew=2, zorder=3, label="p = 0" if r is p0[0] else None)
    for r in p1:
        b.plot(r["p"], r["rho"], "o", ms=8, color=ORANGE, mec=SURFACE, mew=2, zorder=3, label="p ≥ 1" if r is p1[0] else None)
    for r in sorted(p0, key=lambda r: r["rho"]):
        dy = {0: -11, 1: 6, 2: -4}[sorted(p0, key=lambda q: q["rho"]).index(r)]
        b.annotate(r["name"], (r["p"], r["rho"]), xytext=(9, dy), textcoords="offset points", fontsize=7.5, color=TEXT2)
    b.text(-0.3, st["p0_median"] + st["p0_sd"] + 0.03, "median %s, sd %s" % (fmt(st["p0_median"]), fmt(st["p0_sd"])), fontsize=7.5, color=TEXT2, va="bottom")
    # the p >= 1 label sits below its band, at the right edge, clear of every marker
    b.text(4.7, st["p1_median"] - st["p1_sd"] - 0.05, "median %s, sd %s" % (fmt(st["p1_median"]), fmt(st["p1_sd"])), fontsize=7.5, color=TEXT2, va="top", ha="right")
    b.set_xlim(-0.5, 4.8)
    b.set_xticks(range(4))
    b.set_xlabel("p")
    b.set_ylabel("ρ = (δ₂/δ₀) / (−ℓ(ℓ+1)/3)")
    b.set_title("(b) the ratio ρ to the polarisation value, nine series with ℓ ≥ 1", loc="left", fontsize=9.5, color=TEXT)
    b.legend(loc="upper right", fontsize=8)
    style(b)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig1-ratio-vs-p.png"), dpi=200)
    plt.close(fig)


def fig2(rows, st):
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    classes = [("p = 0", BLUE, st["p0_rho"], st["p0_median"], st["p0_sd"]),
               ("p ≥ 1, ℓ ≥ 1", ORANGE, st["p1_rho"], st["p1_median"], st["p1_sd"])]
    for i, (lab, col, vals, med, sd) in enumerate(classes):
        y = i
        ax.axvspan(med - sd, med + sd, ymin=(y + 0.30) / 2.5, ymax=(y + 0.90) / 2.5, color=col, alpha=0.10, lw=0)
        ax.plot([med, med], [y + 0.7, y + 1.3], color=col, lw=2, solid_capstyle="round", zorder=2)
        k = len(vals)
        jitter = [(i - (k - 1) / 2) * 0.09 for i in range(k)]
        for v, j in zip(sorted(vals), jitter):
            ax.plot(v, y + 1 + j, "o", ms=8, color=col, mec=SURFACE, mew=2, zorder=3)
        # the label sits at the right edge of the row, clear of the rho = 0 and rho = 1 lines
        ax.text(2.55, y + 1.46, "median %s, sd %s, %d series" % (fmt(med), fmt(sd), len(vals)), ha="right", fontsize=7.5, color=TEXT2)
    ax.axvline(1.0, color=TEXT2, lw=1)
    ax.text(1.02, 2.72, "ρ = 1", ha="left", fontsize=7.5, color=TEXT2)
    ax.axvline(0.0, color=TEXT2, lw=1)
    ax.text(0.02, 2.72, "ρ = 0", ha="left", fontsize=7.5, color=TEXT2)
    ax.set_yticks([1, 2])
    ax.set_yticklabels([c[0] for c in classes])
    ax.set_ylim(0.4, 2.9)
    ax.set_xlim(-0.6, 2.6)
    ax.set_xlabel("ρ = (δ₂/δ₀) / (−ℓ(ℓ+1)/3)")
    ax.grid(axis="y", visible=False)
    ax.set_title("The two distributions of ρ", loc="left", fontsize=9.5, color=TEXT)
    style(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2-distributions.png"), dpi=200)
    plt.close(fig)


def fig3(rows):
    p0 = [r for r in rows if r["p"] == 0]
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.2))
    for ax, r in zip(axes, p0):
        ns = [n for n, _ in r["pts"]]
        ds = [float(d) for _, d in r["pts"]]
        d0, d2 = float(r["d0"]), float(r["d2"])
        xs = [4 + 0.05 * i for i in range(0, 121)]
        ax.plot(xs, [d0 + d2 / (x - d0) ** 2 for x in xs], color=BLUE, lw=2, label="Ritz fit")
        sea = d2 / d0
        ax.plot(xs, [d0 * (1 - 4.0 / (x - d0) ** 2) for x in xs], color=ORANGE, lw=2, label="polarisation shape, same δ₀")
        ax.plot(ns, ds, "o", ms=8, color=TEXT, mec=SURFACE, mew=2, zorder=3, label="measured")
        ax.set_title("%s, ρ = %s" % (r["name"], fmt(r["rho"])), loc="left", fontsize=9.5, color=TEXT)
        ax.set_xlabel("n")
        ax.set_xticks(ns)
        style(ax)
    axes[0].set_ylabel("δ(n)")
    axes[0].legend(loc="lower right", fontsize=7.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig3-p0-curves.png"), dpi=200)
    plt.close(fig)


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = check.run_fits()
    st = check.stats(rows)
    fig1(rows, st)
    fig2(rows, st)
    fig3(rows)
    for f in sorted(os.listdir(OUT)):
        print("  figures/%s" % f)


if __name__ == "__main__":
    main()
