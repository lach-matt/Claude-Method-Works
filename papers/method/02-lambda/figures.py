#!/usr/bin/env python3
"""figures.py -- regenerates every figure in figures/.

Three kinds of figure and the script makes all three the same way it records them:

  * the four computed plates are drawn here from the data check.py verifies, by importing
    check.py and calling the same functions the obligations call;
  * the four archival plates are copied byte-for-byte from the audited image the caption
    check matched, and their md5 is recorded in FIGURES.tsv.

File numbers match the paper's figure numbers: figN-*.png is Figure N.

    python3 figures.py
"""
import hashlib
import importlib.util
import os
import shutil
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                    # noqa: E402
from matplotlib.lines import Line2D                                # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

sys.argv = [sys.argv[0]]
_spec = importlib.util.spec_from_file_location("chk", os.path.join(HERE, "check.py"))
chk = importlib.util.module_from_spec(_spec)
sys.modules["chk"] = chk
_spec.loader.exec_module(chk)

INK = "#1b3a57"
WARM = "#b5502a"
COOL = "#4b7ba8"
GREY = "#7a7a7a"
plt.rcParams.update({"font.size": 9, "figure.dpi": 170,
                     "axes.edgecolor": "#555555", "axes.labelcolor": "#222222"})

ARCHIVAL = [
    ("fig1-constraint-tree.png",
     "extracted/archives/the-method-1-6-figures-build8/figures/figure-7.1.png"),
    ("fig2-rank-sequence.png",
     "extracted/archives/the-method-1-6-figures-build8/figures/figure-8.2.png"),
    ("fig4-interval-measure.png",
     "extracted/archives/restore-point-2-13/figures/fig05.png"),
    ("fig6-rank-polynomial.png",
     "extracted/archives/restore-point-2-13/figures/fig08.png"),
]


def md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def copy_archival():
    for name, rel in ARCHIVAL:
        src = os.path.join(REPO, rel)
        dst = os.path.join(OUT, name)
        shutil.copyfile(src, dst)
        print("  copied %-28s from %s  md5 %s" % (name, rel, md5(dst)))


def fig_poset():
    """The seventeen generators and their twenty implications, laid out by rank."""
    covP = [(a, b) for a in range(chk.JJ) for b in range(chk.JJ)
            if chk.GBELOW[a][b]
            and not any(chk.GBELOW[a][c] and chk.GBELOW[c][b] for c in range(chk.JJ))]
    rank = [chk.rank(m) for m in chk.GCELL]
    weight = [sum(1 for x in chk.LAM if chk.le(m, x)) for m in chk.GCELL]
    # laid out by LAYER (the seven ranks the generators occupy), evenly spaced, with the
    # rank printed on the axis; x chosen by hand to keep the twenty edges legible.
    layout = {"n >= 2": (-4.4, 0), "k >= 2": (-2.0, 0), "q >= 1": (0.4, 0),
              "e >= 2": (2.6, 0), "2S >= 1": (4.8, 0),
              "n >= 3": (-5.2, 1), "l >= 1": (-3.4, 1), "g >= 1": (0.4, 1),
              "f >= 1": (2.2, 1), "e >= 3": (3.8, 1),
              "q >= 2": (-1.0, 2), "2S >= 2": (3.4, 2),
              "k >= 3": (-3.0, 3), "g >= 2": (-0.4, 4),
              "q >= 3": (-1.6, 5), "2S >= 3": (2.4, 5), "g >= 3": (0.0, 6)}
    layers = [4, 5, 6, 7, 8, 10, 15]
    pos = {chk.GNAME.index(k): (v[0], v[1]) for k, v in layout.items()}
    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    for a, b in covP:
        same = chk.GORDER[a][0][0] == chk.GORDER[b][0][0]
        ax.annotate("", xy=pos[a], xytext=pos[b],
                    arrowprops=dict(arrowstyle="-", color=(WARM if same else COOL),
                                    lw=1.5 if same else 1.0,
                                    ls="-" if same else "--",
                                    shrinkA=20, shrinkB=20, alpha=0.9), zorder=1)
    for t in range(chk.JJ):
        x, y = pos[t]
        ax.text(x, y, chk.GNAME[t].replace(">=", "≥").replace("l ≥", "ℓ ≥"),
                ha="center", va="center",
                fontsize=8, color=INK, zorder=3,
                bbox=dict(boxstyle="round,pad=0.30", fc="white", ec=INK, lw=1.0))
        ax.text(x, y - 0.26, str(weight[t]), ha="center", va="top",
                fontsize=7, color=GREY, zorder=3)
    ax.set_ylabel("rank in Λ")
    ax.set_yticks(range(len(layers)))
    ax.set_yticklabels([str(r) for r in layers])
    ax.set_xticks([])
    ax.set_xlim(-6.4, 6.2)
    ax.set_ylim(-0.85, 6.7)
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.legend(handles=[Line2D([], [], color=WARM, lw=1.5,
                              label="within one coordinate (9)"),
                       Line2D([], [], color=COOL, lw=1.0, ls="--",
                              label="between coordinates (11)")],
              loc="upper left", frameon=False, fontsize=8)
    ax.set_title("The seventeen generators and their twenty implications\n"
                 "the grey number is how many of the 976 cells the generator lies under",
                 fontsize=9.5, color=INK)
    fig.tight_layout()
    p = os.path.join(OUT, "fig3-generating-poset.png")
    fig.savefig(p)
    plt.close(fig)
    print("  drew   %-28s md5 %s" % (os.path.basename(p), md5(p)))


def fig_void():
    """What each bound removes, and how the seven containment events depend on one another."""
    marg = {}
    for name, i, j, f in chk.CONSTRAINTS:
        others = [(ii, jj, ff) for nm, ii, jj, ff in chk.CONSTRAINTS if nm != name]
        marg[name] = sum(1 for x in __import__("itertools").product(*chk.ranges(chk.CAPS))
                         if all(x[ii] <= ff(x[jj]) for ii, jj, ff in others)
                         and not x[i] <= f(x[j]))
    pairs = chk.N * (chk.N - 1) // 2
    rates = {nm: 0 for nm, _, _, _ in chk.CONSTRAINTS}
    free = 0
    for a in range(chk.N):
        xa = chk.LAM[a]
        for b in range(a + 1, chk.N):
            xb = chk.LAM[b]
            lo, hi = chk.meet(xa, xb), chk.join(xa, xb)
            vol = 1
            for i in range(8):
                vol *= hi[i] - lo[i] + 1
            if chk.count_direct(lo, hi) == vol:
                free += 1
            for nm, i, j, f in chk.CONSTRAINTS:
                if hi[i] <= f(lo[j]):
                    rates[nm] += 1
    prod = 1.0
    for v in rates.values():
        prod *= v / pairs
    joint = free / pairs

    def pretty(n):
        return (n.replace("<=", "≤").replace("4l+2", "4ℓ+2").replace("n-1", "n−1")
                 .replace("e-1", "e−1").replace("l ≤", "ℓ ≤"))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 3.6))
    names = sorted(marg, key=lambda k: -marg[k])
    ax1.barh(range(len(names)), [marg[n] for n in names], color=COOL, edgecolor=INK, lw=0.5)
    for t, n in enumerate(names):
        ax1.text(marg[n] + 10, t, str(marg[n]), va="center", fontsize=8, color=INK)
    ax1.set_yticks(range(len(names)))
    ax1.set_yticklabels([pretty(n) for n in names], fontsize=8)
    ax1.invert_yaxis()
    ax1.set_xlabel("box points excluded by this bound alone")
    ax1.set_xlim(0, 790)
    ax1.set_title("(a) no bound is redundant", fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax1.spines[sp].set_visible(False)

    rn = sorted(rates, key=lambda k: -rates[k])
    ax2.bar(range(len(rn)), [rates[n] / pairs for n in rn], color=COOL,
            edgecolor=INK, lw=0.5, width=0.62)
    ax2.axhline(joint, color=WARM, lw=1.6)
    ax2.axhline(prod, color=GREY, lw=1.2, ls="--")
    ax2.text(-0.45, joint + 0.03, "all seven together %.4f" % joint, ha="left",
             fontsize=8, color=WARM, zorder=6,
             bbox=dict(boxstyle="square,pad=0.14", fc="white", ec="none"))
    ax2.text(-0.45, prod - 0.11, "their product %.4f" % prod, ha="left",
             fontsize=8, color=GREY, zorder=6,
             bbox=dict(boxstyle="square,pad=0.14", fc="white", ec="none"))
    ax2.set_xticks(range(len(rn)))
    ax2.set_xticklabels([pretty(n) for n in rn], fontsize=7.5, rotation=40, ha="right")
    ax2.set_ylabel("fraction of the 475,800 pairs")
    ax2.set_ylim(0, 1.12)
    ax2.set_title("(b) the seven containment events, lift %.4f" % (joint / prod),
                  fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax2.spines[sp].set_visible(False)
    fig.tight_layout()
    p = os.path.join(OUT, "fig5-void.png")
    fig.savefig(p)
    plt.close(fig)
    print("  drew   %-28s md5 %s" % (os.path.basename(p), md5(p)))


def fig_caterpillar():
    """The constraint graph read in the nesting order of Theorem 14: an arrow runs from a
    coordinate to a coordinate whose range depends on it.  Edges are taken from the seven
    bounds check.py verifies; only the positions are chosen by hand."""
    names = {"n": "n", "l": "ℓ", "k": "k", "q": "q", "e": "e", "f": "f", "g": "g", "2S": "2S"}
    pos = {"n": (0, 0), "l": (1, 0), "k": (2, 0), "q": (3, 0), "g": (4, 0), "f": (5, 0),
           "e": (6, 0), "2S": (2, -1)}
    label = {"l <= n-1": "ℓ ≤ n − 1", "k <= 4l+2": "k ≤ 4ℓ + 2", "q <= k": "q ≤ k",
             "f <= e-1": "f ≤ e − 1", "g <= 4f+2": "g ≤ 4f + 2", "g <= q": "g ≤ q",
             "2S <= k": "2S ≤ k"}
    fig, ax = plt.subplots(figsize=(9.2, 3.4))
    for nm, i, j, _f in chk.CONSTRAINTS:
        a, b = chk.CO[j], chk.CO[i]                       # bounding -> bounded
        (xa, ya), (xb, yb) = pos[a], pos[b]
        pauli = nm in ("k <= 4l+2", "g <= 4f+2")
        ax.annotate("", xy=(xb, yb), xytext=(xa, ya),
                    arrowprops=dict(arrowstyle="-|>", color=(WARM if pauli else INK),
                                    lw=1.3, shrinkA=16, shrinkB=16), zorder=1)
        mx, my = (xa + xb) / 2, (ya + yb) / 2
        if ya == yb:
            ax.text(mx, my + 0.16, label[nm], ha="center", va="bottom", fontsize=8,
                    color=(WARM if pauli else GREY))
        else:
            ax.text(mx + 0.08, my, label[nm], ha="left", va="center", fontsize=8, color=GREY)
    for c, (x, y) in pos.items():
        ax.text(x, y, names[c], ha="center", va="center", fontsize=10, color=INK, zorder=3,
                bbox=dict(boxstyle="circle,pad=0.35", fc="white", ec=INK, lw=1.1))
    ax.text(2, -1.42, "a leaf: factors out as (1 − zᵏ⁺¹)/(1 − z)", ha="center", va="top",
            fontsize=8, color=COOL)
    ax.text(4, -0.42, "two parents: g ≤ min(q, 4f + 2)", ha="center", va="top",
            fontsize=8, color=WARM)
    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-1.9, 0.75)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("a caterpillar: a path of seven with one pendant, read in the nesting order "
                 "n, ℓ, k, 2S, q, e, f, g\nan arrow runs from a coordinate to one whose range "
                 "it bounds; Pauli bounds in red", fontsize=9.5, color=INK)
    fig.tight_layout()
    p = os.path.join(OUT, "fig7-caterpillar.png")
    fig.savefig(p)
    plt.close(fig)
    print("  drew   %-28s md5 %s" % (os.path.basename(p), md5(p)))


def fig_seed():
    """How the 24,585 minimum covers spread over the cells that appear in one."""
    _, size, total, forced, counts, _uniq, _lb = chk.seed()
    vals = sorted(counts.values(), reverse=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.5))
    ax1.plot(range(1, len(vals) + 1), vals, color=COOL, lw=1.4)
    ax1.scatter([1], [vals[0]], color=WARM, zorder=3, s=26)
    ax1.annotate("one cell in all %s covers" % format(total, ","),
                 xy=(1, vals[0]), xytext=(14, vals[0] * 0.55), fontsize=8, color=WARM,
                 arrowprops=dict(arrowstyle="-", color=WARM, lw=0.8))
    ax1.set_yscale("log")
    ax1.set_xlabel("cells, ordered by how many minimum covers hold them")
    ax1.set_ylabel("minimum covers holding the cell")
    ax1.set_title("(a) %d of the 976 cells appear in a minimum cover" % len(vals),
                  fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax1.spines[sp].set_visible(False)

    share = [100.0 * v / total for v in vals]
    ax2.hist(share, bins=40, color=COOL, edgecolor=INK, lw=0.4)
    ax2.set_yscale("log")
    ax2.set_xlabel("share of the minimum covers holding the cell (%)")
    ax2.set_ylabel("cells")
    ax2.set_title("(b) the tail is heavy: median %.2f%%, maximum 100%%"
                  % (100.0 * sorted(counts.values())[len(vals) // 2] / total),
                  fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax2.spines[sp].set_visible(False)
    fig.tight_layout()
    p = os.path.join(OUT, "fig8-seed.png")
    fig.savefig(p)
    plt.close(fig)
    print("  drew   %-28s md5 %s" % (os.path.basename(p), md5(p)))


if __name__ == "__main__":
    print("figures/")
    copy_archival()
    fig_poset()
    fig_void()
    fig_caterpillar()
    fig_seed()
