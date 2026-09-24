#!/usr/bin/env python3
"""figures.py — regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

The audited plate figures/sections-plate.png is copied, not drawn; see FIGURES.tsv.
"""
import importlib.util, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("check", os.path.join(HERE, "check.py"))
C = importlib.util.module_from_spec(spec)
sys.modules["check"] = C
spec.loader.exec_module(C)

# the reference palette (dataviz skill): categorical slots 1–3, text tokens, light surface
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.titlesize": 10, "axes.titleweight": "bold", "figure.facecolor": SURF,
                     "axes.facecolor": SURF, "savefig.facecolor": SURF, "axes.spines.top": False, "axes.spines.right": False,
                     "font.family": "DejaVu Sans"})
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)


def fig_stages():
    L = C.stages()
    counts = {d: len(L[d]) for d in C.STAGES}
    box = {}
    for d in C.STAGES:
        r, b = C.staircase_sweep(L[d])
        box[d] = b
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9))
    xs = list(C.STAGES)
    labels = ["Λ%s" % "".join(chr(0x2080 + int(ch)) for ch in str(d)) for d in xs]
    a1.bar(xs, [counts[d] for d in xs], color=BLUE, width=0.62)
    a1.set_yscale("log")
    a1.set_xticks(xs, labels)
    a1.set_ylabel("cells (log)")
    a1.set_title("Cells per stage")
    for d in xs:
        a1.text(d, counts[d] * 1.25, "{:,}".format(counts[d]), ha="center", va="bottom", fontsize=7.5, color=INK)
    a1.set_ylim(500, 1.2e6)
    a1.yaxis.grid(True, color=GRID)
    a1.set_axisbelow(True)
    fill = [100 * counts[d] / box[d] for d in xs]
    a2.plot(xs, fill, color=ORANGE, lw=2, marker="o", ms=5)
    a2.set_yscale("log")
    a2.set_xticks(xs, labels)
    a2.set_ylabel("fill  |Λ| / |Box|  (%, log)")
    a2.set_title("Fill of the ambient box")
    for d, f in zip(xs, fill):
        a2.text(d, f * 1.22, "%.2f%%" % f, ha="center", va="bottom", fontsize=7.5, color=INK)
    a2.set_ylim(0.2, 40)
    a2.yaxis.grid(True, color=GRID)
    a2.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "stages.png"), dpi=200)
    plt.close(fig)


def fig_graph():
    """The constraint graph at the thirteenth stage, under the one-parent reading of the K bound.  The core's
    angular momentum is labelled 2Jₚ, as the paper writes it (no Unicode subscript c exists)."""
    pos = {"n": (0.0, 2.2), "\u2113": (1.1, 2.2), "k": (2.2, 2.2), "2S": (2.2, 3.25),
           "2J_c": (3.5, 2.2), "2K": (4.75, 2.2), "2J": (6.0, 2.2),
           "q": (2.2, 1.05), "g": (3.5, 1.05), "v": (4.85, 1.52), "2S\u2032": (4.85, 0.58),
           "f": (3.5, -0.05), "e": (2.2, -0.05)}
    envelope = {"2J_c", "2K", "2J"}                       # bounded by a monotone envelope
    tri = {"2S\u2032", "g", "v"}                              # the one cycle
    edges = set()
    for s_ in C.STAGES:
        edges |= set(C.EDGES[s_])
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        on_tri = {a, b} <= tri
        ax.plot([x1, x2], [y1, y2], color=AQUA if on_tri else INK2,
                lw=2.6 if on_tri else 1.6, zorder=1)
    for v, (x, y) in pos.items():
        rim = ORANGE if v in envelope else BLUE
        ax.add_patch(Circle((x, y), 0.235, facecolor=SURF, edgecolor=rim, lw=2.2, zorder=2))
        ax.text(x, y, {"2J_c": "2J\u209a"}.get(v, v), ha="center", va="center", fontsize=8.5, color=INK, zorder=3)
    ax.annotate("every parent\u2013target path runs through q", xy=(2.2, 1.05), xytext=(-0.4, 0.5),
                fontsize=8, color=INK2, ha="left",
                arrowprops=dict(arrowstyle="->", color=INK2, lw=1.0, shrinkB=12))
    ax.text(0.0, 2.75, "parent side", fontsize=8.5, color=INK2, ha="left", style="italic")
    ax.text(2.2, -0.52, "target side", fontsize=8.5, color=INK2, ha="center", style="italic")
    ax.plot([], [], color=BLUE, lw=2.2, label="exact bound")
    ax.plot([], [], color=ORANGE, lw=2.2, label="envelope bound")
    ax.plot([], [], color=AQUA, lw=2.6, label="the one cycle, 2S\u2032\u2013g\u2013v")
    ax.legend(loc="lower right", frameon=False, fontsize=7.8, ncol=1,
              bbox_to_anchor=(1.0, -0.02))
    ax.set_xlim(-0.45, 6.5)
    ax.set_ylim(-0.7, 3.7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Thirteen coordinates, thirteen constraints, cycle rank 1", pad=2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "constraint-graph.png"), dpi=200)
    plt.close(fig)


def fig_profile():
    L = C.stages()
    s8, s13 = C.sections_of(L[8]), C.sections_of(L[13])
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    q = [0, 1, 2, 3]
    for secs, ls, tag in ((s13, "-", "Λ₁₃"), (s8, ":", "Λ₈")):
        A = [a for _, a, b in secs]
        B = [b for _, a, b in secs]
        AB = [a * b for _, a, b in secs]
        ax.plot(q, A, ls, color=ORANGE, lw=2, marker="o", ms=5, label="|A(q)| parent side, %s" % tag)
        ax.plot(q, B, ls, color=BLUE, lw=2, marker="s", ms=5, label="|B(q)| target side, %s" % tag)
        ax.plot(q, AB, ls, color=INK, lw=1.6, marker="D", ms=4, label="|A(q)|·|B(q)| section, %s" % tag)
        for x, y in zip(q, AB):
            ax.text(x, y * (1.35 if ls == "-" else 0.62), "{:,}".format(y), ha="center", fontsize=7.5, color=INK)
    ax.set_yscale("log")
    ax.set_xticks(q)
    ax.set_xlabel("q — the transfer")
    ax.set_ylabel("cells (log)")
    ax.yaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=7.2, ncol=3, loc="upper center",
              bbox_to_anchor=(0.5, -0.16))
    ax.set_title("The sections of the cylinder: the parent side falls, the target side rises")
    ax.set_ylim(3, 1.1e6)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "profile.png"), dpi=200)
    plt.close(fig)


def fig_brackets():
    L = C.stages()
    fig, axes = plt.subplots(1, 6, figsize=(9.6, 2.6), sharey=False)
    for ax, d in zip(axes[:5], C.STAGES[1:]):
        fib = {}
        for c in L[d]:
            fib.setdefault(sum(c), set()).add(sum(c[:-1]))
        rs = sorted(fib)
        lo = [min(fib[r]) for r in rs]
        hi = [max(fib[r]) for r in rs]
        ax.fill_between(rs, lo, hi, color=BLUE, alpha=0.25, lw=0)
        ax.plot(rs, lo, color=BLUE, lw=1.6)
        ax.plot(rs, hi, color=BLUE, lw=1.6)
        ax.set_title("Λ%s → Λ%s" % ("".join(chr(0x2080 + int(ch)) for ch in str(d)), "".join(chr(0x2080 + int(ch)) for ch in str(d - 1))), fontsize=9)
        ax.set_xlabel("rank above")
        ax.yaxis.grid(True, color=GRID)
        ax.set_axisbelow(True)
    axes[0].set_ylabel("ranks below")
    ax = axes[5]
    direct = {}
    for c in L[13]:
        direct.setdefault(sum(c), set()).add(sum(c[:8]))
    br = {}
    for d in C.STAGES[1:]:
        fib = {}
        for c in L[d]:
            fib.setdefault(sum(c), set()).add(sum(c[:-1]))
        br[d] = {r: (min(s), max(s)) for r, s in fib.items()}
    rs = sorted(direct)
    clo, chi = [], []
    for r in rs:
        lo = hi = r
        for d in (13, 12, 11, 10, 9):
            los = [br[d][x][0] for x in range(lo, hi + 1) if x in br[d]]
            his = [br[d][x][1] for x in range(lo, hi + 1) if x in br[d]]
            lo, hi = min(los), max(his)
        clo.append(lo)
        chi.append(hi)
    ax.fill_between(rs, clo, chi, color=ORANGE, alpha=0.25, lw=0, label="composed")
    ax.plot(rs, [min(direct[r]) for r in rs], color=INK, lw=1.4, label="direct")
    ax.plot(rs, [max(direct[r]) for r in rs], color=INK, lw=1.4)
    ax.set_title("Λ₁₃ → Λ₈", fontsize=9)
    ax.set_xlabel("rank in Λ₁₃")
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    ax.yaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    fig.suptitle("Stage brackets: the ranks below a rank above are a gap-free interval with monotone ends", fontsize=10, fontweight="bold")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "brackets.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_stages()
    fig_graph()
    fig_profile()
    fig_brackets()
    print("wrote", sorted(os.listdir(OUT)))
