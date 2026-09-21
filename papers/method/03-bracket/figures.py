#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from results.json, which
check.py --json writes. Two further figures are audited plates copied from the tree
(FIGURES.tsv records their source and md5); this script does not touch those.

    python3 check.py --json && python3 figures.py
"""
import json
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")
R = 109737.31568
BLUE, ORANGE, AQUA, YELLOW, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#8a8985"

plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": "#e6e6e3", "grid.linewidth": 0.5})

res = json.load(open(os.path.join(HERE, "results.json")))
N = res["numbers"]


def fig3_bounds():
    """Every held cell bounds its own perturbation by w/2, against 2Z^2R/nu^3 at Z = 1 and 2."""
    b = res["results"]["bounds"]                # (w/2, D, nu, Z, species, series, n)
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for Z, col in ((1, BLUE), (2, ORANGE)):
        pts = [(x[2], x[0]) for x in b if x[3] == Z]
        ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=6, color=col, alpha=0.55, linewidths=0,
                   label="held cells, Z = %d (%d)" % (Z, len(pts)))
    pts = [(x[2], x[0]) for x in b if x[3] >= 3]
    ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=6, color=AQUA, alpha=0.55, linewidths=0,
               label="held cells, Z ≥ 3 (%d)" % len(pts))
    nus = [1.5 * 1.05 ** i for i in range(90)]
    for Z, col, ls in ((1, BLUE, "-"), (2, ORANGE, "--")):
        ax.plot(nus, [2 * Z * Z * R / n ** 3 for n in nus], color=col, ls=ls, lw=1.2, label="2Z²R/ν³, Z = %d" % Z)
    t = b[0]
    ax.annotate("tightest: %.2f cm⁻¹ at ν = %.1f" % (t[0], t[2]), (t[2], t[0]), xytext=(t[2] / 4, t[0] * 0.35),
                fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7))
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("effective quantum number ν"); ax.set_ylabel("bound on the local displacement, w/2 (cm⁻¹)")
    ax.legend(frameon=False, fontsize=7.5, loc="upper right")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3-bounds.png"), dpi=170); plt.close(fig)


def fig4_v_measured():
    """V measured on triples of measured levels against the exact 4r^3/(3r^2 - 1)."""
    vp = res["results"]["vpairs"]               # (V_meas, V_exact, nu, r, h)
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    for h, col in ((1, BLUE), (2, ORANGE)):
        pts = [(x[3], x[0]) for x in vp if x[4] == h]
        ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=6, color=col, alpha=0.5, linewidths=0,
                   label="measured, h = %d (%d triples)" % (h, len(pts)))
    rs = [1.2 * 1.04 ** i for i in range(110)]
    ax.plot(rs, [4 * r ** 3 / (3 * r * r - 1) for r in rs], color="#0b0b0b", lw=1.2, label="4r³/(3r² − 1)")
    ax.axhline(32 / 11, color=YELLOW, ls=":", lw=1, label="floor 32/11")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("r = ν/h"); ax.set_ylabel("V = w/e")
    ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig4-v-measured.png"), dpi=170); plt.close(fig)


def fig5_order_census():
    """The order-k census under the admissibility rule."""
    c = res["numbers"]["order_census"]
    ks = sorted(int(k) for k in c)
    adm = [c[str(k)][0] for k in ks]; ref = [c[str(k)][1] for k in ks]; unr = [c[str(k)][2] for k in ks]
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.bar(ks, adm, color=BLUE, width=0.62, label="admitted, sign as predicted")
    ax.bar(ks, ref, bottom=adm, color=ORANGE, width=0.62, label="wrong sign (a perturbation)")
    ax.bar(ks, unr, bottom=[a + r for a, r in zip(adm, ref)], color="#c9c8c3", width=0.62, label="unresolved, below 5·2ᵏ⁺¹q")
    for k, a, r_, u in zip(ks, adm, ref, unr):
        ax.text(k, a + r_ + u + 12, "%d" % (a + r_ + u), ha="center", fontsize=7.5, color="#52514e")
    ax.set_xlabel("order k (a run of k + 2 consecutive members)"); ax.set_ylabel("runs")
    ax.legend(frameon=False, fontsize=7.5)
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig5-order-census.png"), dpi=170); plt.close(fig)


if __name__ == "__main__":
    os.makedirs(FIG, exist_ok=True)
    fig3_bounds(); fig4_v_measured(); fig5_order_census()
    print("wrote fig3-bounds.png, fig4-v-measured.png, fig5-order-census.png")
