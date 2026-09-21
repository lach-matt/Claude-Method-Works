#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

Imports check.py by path and draws from its own constructions: periodic_cells(), janet_cells(),
E_of(), slot(), channel_rows() and coord_rows().  Nothing is drawn by hand; no number is typed
here that check.py does not also produce.  Figure 1 is not made here -- it is an existing audited
plate, recorded in FIGURES.tsv.

Palette: light surface, recessive hairline grid, slot 1 blue for what an index holds, slot 2
orange for what its coordinates admit and it denies, a muted red for the physically forbidden.
"""
import collections
import importlib.util
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0]]                       # check.py reads sys.argv for --selftest
spec = importlib.util.spec_from_file_location("check", os.path.join(HERE, "check.py"))
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e6e5e1"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
RED = "#b23b3b"
GOLD = "#d8a13a"
GREY = "#b9b8b4"
OUT = os.path.join(HERE, "figures")

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GRID, "axes.labelcolor": TEXT2,
    "xtick.color": TEXT2, "ytick.color": TEXT2, "axes.facecolor": SURFACE, "figure.facecolor": SURFACE,
    "axes.grid": False, "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})


def style(ax):
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


def cell(ax, x, y, col, w=0.86, h=0.86):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=col, edgecolor="none"))


# ---------------------------------------------------------------- figure 2
def fig2():
    """The same elements on two presentations, with the defect each carries."""
    X = check.periodic_cells()
    S, E = check.E_of(X, ["period", "group"])
    admitted = sorted(S - set(X))
    J = check.janet_cells(check.JANET_ROWS_118)
    SJ, EJ = check.E_of(J, ["n+l", "Z"])

    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.7),
                               gridspec_kw={"width_ratios": [1.0, 1.55]})
    for p, g in X:
        cell(a, g, p, BLUE)
    for p, g in admitted:
        cell(a, g, p, ORANGE)
    a.set_xlim(0.3, 18.7)
    a.set_ylim(7.7, 0.3)
    a.set_xticks([1, 5, 10, 15, 18])
    a.set_yticks(range(1, 8))
    a.set_xlabel("group")
    a.set_ylabel("period")
    a.set_title("(period, group):  %d cells in a box of %d,  E = %d"
                % (len(set(X)), len(S), E), fontsize=9.5, color=TEXT, loc="left")
    style(a)
    for s in ("left", "bottom"):
        a.spines[s].set_visible(False)

    rows = check.JANET_ROWS_118
    starts = [min(z for (r, z) in J if r == rr) for rr in range(1, 9)]
    ends = [max(z for (r, z) in J if r == rr) for rr in range(1, 9)]
    for r in range(1, 9):
        b.add_patch(Rectangle((starts[r - 1] - 0.5, r - 0.42),
                              rows[r - 1], 0.84, facecolor=BLUE, edgecolor="none"))
        b.text(ends[r - 1] + 2.5, r, "%d" % rows[r - 1], va="center", ha="left",
               fontsize=8, color=TEXT2)
    b.set_xlim(-2, 132)
    b.set_ylim(8.7, 0.3)
    b.set_xticks([1, 21, 39, 57, 89, 118])
    b.set_yticks(range(1, 9))
    b.set_xlabel("atomic number Z")
    b.set_ylabel("n + ℓ")
    b.set_title("(n + ℓ, Z):  %d cells in a box of %d,  E = %d"
                % (len(J), len(rows) * 118, EJ), fontsize=9.5, color=TEXT, loc="left")
    style(b)
    for s in ("left", "bottom"):
        b.spines[s].set_visible(False)
    b.plot([], [], "s", color=BLUE, ms=8, label="held by the index")
    a.plot([], [], "s", color=BLUE, ms=8, label="held by the index")
    a.plot([], [], "s", color=ORANGE, ms=8, label="admitted and denied")
    a.legend(loc="lower center", bbox_to_anchor=(0.5, -0.42), ncol=2, fontsize=8.5,
             handletextpad=0.4, columnspacing=1.4)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2-two-presentations.png"), dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------- figure 3
def fig3():
    """The thirty-six identified, and what helium's placement costs."""
    X = check.periodic_cells()
    S, E = check.E_of(X, ["period", "group"])
    admitted = sorted(S - set(X))
    forb, defer = collections.Counter(), collections.Counter()
    kind = {}
    for p, g in admitted:
        n, l = check.slot(p, g)
        name = "%d%s" % (n, "spdf"[l])
        if l > n - 1:
            forb[name] += 1
            kind[(p, g)] = ("forbidden", name)
        else:
            defer[name] += 1
            kind[(p, g)] = ("deferred", name)

    X2 = check.periodic_cells(helium_group=2)
    S2, E2 = check.E_of(X2, ["period", "group"])
    adm2 = sorted(S2 - set(X2))

    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.5),
                               gridspec_kw={"width_ratios": [1.0, 1.0]})
    for p, g in X:
        cell(a, g, p, GREY)
    for p, g in admitted:
        cell(a, g, p, RED if kind[(p, g)][0] == "forbidden" else GOLD)
    for lab, gs, p in (("1d", (3, 12), 1), ("1p", (13, 17), 1), ("2d", (3, 12), 2),
                       ("3d", (3, 12), 3)):
        a.text((gs[0] + gs[1]) / 2, p, lab, ha="center", va="center", fontsize=8,
               color="white", fontweight="bold")
    a.text(2, 1, "1s", ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
    a.set_xlim(0.3, 18.7)
    a.set_ylim(7.7, 0.3)
    a.set_xticks([1, 5, 10, 15, 18])
    a.set_yticks(range(1, 8))
    a.set_xlabel("group")
    a.set_ylabel("period")
    a.set_title("the %d, by the subshell the slot would hold:  %d forbidden by ℓ ≤ n−1,  %d deferred"
                % (E, sum(forb.values()), sum(defer.values())), fontsize=9, color=TEXT, loc="left")
    style(a)
    for s in ("left", "bottom"):
        a.spines[s].set_visible(False)

    for p, g in X2:
        cell(b, g, p, GREY)
    for p, g in adm2:
        cell(b, g, p, GOLD)
    b.set_xlim(0.3, 18.7)
    b.set_ylim(7.7, 0.3)
    b.set_xticks([1, 5, 10, 15, 18])
    b.set_yticks(range(1, 8))
    b.set_xlabel("group")
    b.set_ylabel("period")
    b.set_title("the same %d cells with helium drawn at group 2:  E = %d"
                % (len(set(X2)), E2), fontsize=9, color=TEXT, loc="left")
    style(b)
    for s in ("left", "bottom"):
        b.spines[s].set_visible(False)
    b.plot([], [], "s", color=RED, ms=8, label="no such orbital (ℓ > n−1)")
    b.plot([], [], "s", color=GOLD, ms=8, label="an orbital exists; filled later")
    b.legend(loc="lower center", bbox_to_anchor=(0.0, -0.44), ncol=2, fontsize=8.5,
             handletextpad=0.4, columnspacing=1.4)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig3-thirty-six.png"), dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------- figure 4
def fig4():
    """The rows of the (n+ℓ, Z) index, and the measured defects across their openings."""
    J = check.janet_cells(check.JANET_ROWS_118)
    rows = check.JANET_ROWS_118
    starts = [min(z for (r, z) in J if r == rr) for rr in range(1, 9)]
    LW1, POP = check.LW1, check.POP
    crows = check.coord_rows()
    thr = {2: 21, 3: 57}
    pts = []
    for r in crows:
        if r["grade"] != "measured" or r["l"] not in (2, 3):
            continue
        core = r["Z"] - r["charge"]
        if core >= 1 and POP.core_p(core, r["l"]) != 0:
            continue
        pts.append((r["Z"], r["l"], float(r["delta"]), r["Z"] >= thr[r["l"]]))

    fig, (a, b) = plt.subplots(2, 1, figsize=(9.6, 5.4), sharex=True,
                               gridspec_kw={"height_ratios": [1.0, 1.25]})
    for r in range(1, 9):
        a.add_patch(Rectangle((starts[r - 1] - 0.5, r - 0.40), rows[r - 1], 0.80,
                              facecolor=BLUE, edgecolor="none"))
        a.text(starts[r - 1] - 1.5, r, "%d" % starts[r - 1], va="center", ha="right",
               fontsize=7.5, color=TEXT2)
    a.set_ylim(8.7, 0.3)
    a.set_yticks(range(1, 9))
    a.set_ylabel("n + ℓ")
    a.set_title("the rows of the (n + ℓ, Z) index: lengths %s"
                % ", ".join(str(k) for k in rows), fontsize=9, color=TEXT, loc="left")
    style(a)
    for s in ("left", "bottom"):
        a.spines[s].set_visible(False)

    for Z, l, d, past in pts:
        b.plot(Z, d, "o" if l == 2 else "^", ms=7,
               color=ORANGE if past else BLUE, mec=SURFACE, mew=1.3, zorder=3)
    for z0 in (21, 57, 89):
        for ax in (a, b):
            ax.axvline(z0, color=TEXT2, lw=0.9, ls=(0, (4, 3)), zorder=1)
    b.set_xlim(-2, 122)
    b.set_xticks([1, 21, 39, 57, 89, 118])
    b.set_xlabel("atomic number Z")
    b.set_ylabel("quantum defect δ")
    b.grid(True, axis="y", color=GRID, lw=1)
    b.set_axisbelow(True)
    style(b)
    b.plot([], [], "o", color=BLUE, ms=7, mec=SURFACE, mew=1.3, label="ℓ = 2, below its block opening")
    b.plot([], [], "^", color=BLUE, ms=7, mec=SURFACE, mew=1.3, label="ℓ = 3, below its block opening")
    b.plot([], [], "o", color=ORANGE, ms=7, mec=SURFACE, mew=1.3, label="ℓ = 2, at or past it")
    b.legend(loc="upper right", fontsize=8.5, handletextpad=0.4)
    b.set_title("the %d measured d and f channels whose core holds no orbital of that ℓ"
                % len(pts), fontsize=9, color=TEXT, loc="left")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4-janet-rows.png"), dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------- figure 5
def fig5():
    """The parent census: who needs a parent written, who has one, and the two-limit species."""
    hdr, data = check.channel_rows()
    for l in range(4):
        for k in range(4 * l + 3):
            check.TERMS[(l, k)] = sum(check.ls_terms(l, k).values())
    sp = [check.species_of(c) for i, c in data]
    cls = {s: check.core_class(check.core_config(s)[2]) for s in set(sp)}
    order = [("bare", "bare nucleus"), ("closed", "closed shell"),
             ("one-term-1J", "one term, one level"), ("one-term-2J", "one term, two levels"),
             ("multi", "several terms")]
    named = collections.Counter((cls[check.species_of(c)], "(" in c[1]) for i, c in data)

    fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.0),
                               gridspec_kw={"width_ratios": [1.15, 1.0]})
    y = range(len(order))
    for k, (key, lab) in enumerate(order):
        n0, n1 = named[(key, False)], named[(key, True)]
        a.barh(k, n1, color=BLUE, height=0.62)
        a.barh(k, n0, left=n1, color=GREY, height=0.62)
        a.text(n1 + n0 + 4, k, "%d" % (n1 + n0), va="center", fontsize=8.5, color=TEXT2)
        if n1:
            a.text(n1 / 2, k, "%d" % n1, va="center", ha="center", fontsize=8,
                   color="white", fontweight="bold")
    a.set_yticks(list(y))
    a.set_yticklabels([lab for _, lab in order], fontsize=8.5)
    a.invert_yaxis()
    a.set_xlim(0, 210)
    a.set_xlabel("channel rows")
    a.set_title("596 rows by what the ionic core carries", fontsize=9, color=TEXT, loc="left")
    a.grid(True, axis="x", color=GRID, lw=1)
    a.set_axisbelow(True)
    style(a)
    a.legend(handles=[Rectangle((0, 0), 1, 1, facecolor=BLUE),
                      Rectangle((0, 0), 1, 1, facecolor=GREY)],
             labels=["label names a parent", "it does not"],
             loc="lower right", fontsize=8.5, handletextpad=0.4)

    lims = collections.defaultdict(list)
    for i, c in data:
        lims[check.species_of(c)].append(c[10])
    four = ["Ba III", "Ne I", "Ne II", "Si I"]
    TERM = {"2P*": "²P°", "2S": "²S", "3P": "³P", "1D": "¹D"}
    for k, s in enumerate(four):
        vals = sorted({float(x.replace(",", "")) for x in lims[s]})
        cnt = collections.Counter(float(x.replace(",", "")) for x in lims[s])
        b.plot([0, len(vals) - 1], [k, k], "-", color=GRID, lw=2, zorder=1)
        for j, v in enumerate(vals):
            rows_here = [c for i, c in data
                         if check.species_of(c) == s and float(c[10].replace(",", "")) == v]
            key = {check.parent_key(c[1]) for c in rows_here}
            terms = sorted(k for k in key if k and k[0] != "j")
            js = sorted({k[1] for k in key if k and k[1]})
            kk = terms[0] if terms else sorted(key)[0]
            lab = TERM.get(kk[0], kk[0]) + (" " + js[0] if js else "")
            b.plot(j, k, "o", ms=6 + 0.32 * cnt[v], color=ORANGE, mec=SURFACE, mew=1.5, zorder=3)
            b.text(j, k - 0.26, lab, ha="center", va="bottom", fontsize=8.5, color=TEXT)
            b.text(j, k + 0.26, "%d row%s" % (cnt[v], "" if cnt[v] == 1 else "s"),
                   ha="center", va="top", fontsize=7.5, color=TEXT2)
        b.text(2.55, k, "span %s cm⁻¹" % "{:,.0f}".format(vals[-1] - vals[0]),
               va="center", fontsize=8, color=TEXT2)
    b.set_yticks(range(len(four)))
    b.set_yticklabels(four, fontsize=9)
    b.invert_yaxis()
    b.set_ylim(3.72, -0.72)
    b.set_xlim(-0.45, 4.2)
    b.set_xticks([0, 1, 2])
    b.set_xticklabels(["first limit", "second", "third"])
    b.set_title("the four species printing two or more limits",
                fontsize=9, color=TEXT, loc="left")
    b.grid(True, axis="x", color=GRID, lw=1)
    b.set_axisbelow(True)
    style(b)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig5-parent-census.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    fig2()
    fig3()
    fig4()
    fig5()
    for f in sorted(os.listdir(OUT)):
        print("  figures/%s" % f)
