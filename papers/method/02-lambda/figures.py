#!/usr/bin/env python3
"""figures.py -- regenerates every figure in figures/.

Three kinds of figure and the script makes all three the same way it records them:

  * the three computed plates are drawn here from the data check.py verifies, by importing
    check.py and calling the same functions the obligations call;
  * the five archival plates are copied byte-for-byte from the audited image the caption
    check matched, and their md5 is recorded in FIGURES.tsv.

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
    ("fig3-rank-sequence.png",
     "extracted/archives/the-method-1-6-figures-build8/figures/figure-8.2.png"),
    ("fig4-occupancy-measure.png",
     "extracted/archives/restore-point-2-13/figures/fig05.png"),
    ("fig5-caterpillar.png",
     "extracted/archives/restore-point-2-13/figures/fig07.png"),
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
    byr = defaultdict(list)
    for t in range(chk.JJ):
        byr[rank[t]].append(t)
    order = {4: ["n >= 2", "k >= 2", "q >= 1", "e >= 2", "2S >= 1"],
             5: ["l >= 1", "n >= 3", "g >= 1", "f >= 1", "e >= 3"],
             6: ["q >= 2", "2S >= 2"], 7: ["k >= 3"], 8: ["g >= 2"],
             10: ["q >= 3", "2S >= 3"], 15: ["g >= 3"]}
    pos = {}
    for r, names in order.items():
        idx = [chk.GNAME.index(nm) for nm in names]
        n = len(idx)
        for j, t in enumerate(idx):
            pos[t] = ((j - (n - 1) / 2) * 2.05, r)
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    for a, b in covP:
        same = chk.GORDER[a][0][0] == chk.GORDER[b][0][0]
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]],
                color=(WARM if same else COOL), lw=1.5 if same else 1.0,
                ls="-" if same else "--", zorder=1, alpha=0.9)
    for t in range(chk.JJ):
        x, y = pos[t]
        s = 90 + weight[t] * 0.5
        ax.scatter([x], [y], s=s, color="white", edgecolor=INK, zorder=2, linewidths=1.2)
        ax.text(x, y - 0.55, chk.GNAME[t].replace(">=", "≥"), ha="center", va="top",
                fontsize=8, color=INK)
        ax.text(x, y + 0.42, str(weight[t]), ha="center", va="bottom",
                fontsize=7, color=GREY)
    ax.set_ylabel("rank in Λ")
    ax.set_yticks(sorted(order))
    ax.set_xticks([])
    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(2.6, 16.4)
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.legend(handles=[Line2D([], [], color=WARM, lw=1.5,
                              label="within one coordinate (9)"),
                       Line2D([], [], color=COOL, lw=1.0, ls="--",
                              label="between coordinates (11)")],
              loc="upper left", frameon=False, fontsize=8)
    ax.set_title("The seventeen generators and their twenty implications\n"
                 "area is the number of the 976 cells the generator lies under",
                 fontsize=9.5, color=INK)
    fig.tight_layout()
    p = os.path.join(OUT, "fig2-generating-poset.png")
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

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.5))
    names = sorted(marg, key=lambda k: -marg[k])
    lab = [n.replace("<=", "≤").replace("4l+2", "4ℓ+2").replace("n-1", "n−1")
            .replace("e-1", "e−1").replace("l <=", "ℓ ≤") for n in names]
    ax1.barh(range(len(names)), [marg[n] for n in names], color=COOL, edgecolor=INK, lw=0.5)
    for t, n in enumerate(names):
        ax1.text(marg[n] + 8, t, str(marg[n]), va="center", fontsize=8, color=INK)
    ax1.set_yticks(range(len(names)))
    ax1.set_yticklabels(lab, fontsize=8)
    ax1.invert_yaxis()
    ax1.set_xlabel("box points excluded by this bound alone")
    ax1.set_xlim(0, 760)
    ax1.set_title("(a) no bound is redundant", fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax1.spines[sp].set_visible(False)

    rn = sorted(rates, key=lambda k: -rates[k])
    ax2.bar(range(len(rn)), [rates[n] / pairs for n in rn], color=COOL,
            edgecolor=INK, lw=0.5)
    ax2.axhline(joint, color=WARM, lw=1.6)
    ax2.axhline(prod, color=GREY, lw=1.2, ls="--")
    ax2.text(len(rn) - 0.4, joint + 0.015, "joint %.4f" % joint, ha="right",
             fontsize=8, color=WARM)
    ax2.text(len(rn) - 0.4, prod - 0.045, "product %.4f" % prod, ha="right",
             fontsize=8, color=GREY)
    ax2.set_xticks(range(len(rn)))
    ax2.set_xticklabels([n.split()[0].replace("l", "ℓ") if n.startswith("l") else n.split()[0]
                         for n in rn], fontsize=8)
    ax2.set_ylabel("fraction of the 475,800 pairs")
    ax2.set_ylim(0, 1.05)
    ax2.set_title("(b) the seven containment events, and their lift %.4f" % (joint / prod),
                  fontsize=9.5, color=INK)
    for sp in ("top", "right"):
        ax2.spines[sp].set_visible(False)
    fig.tight_layout()
    p = os.path.join(OUT, "fig7-void.png")
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
    fig_seed()
