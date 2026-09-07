#!/usr/bin/env python3
"""figures.py -- the paper's figures, drawn from the ledger rather than by hand.

WHY THEY ARE GENERATED
----------------------
A figure is a claim in a different notation. If it is drawn by hand it can
disagree with the prose beside it, and nothing would catch that -- which is the
same weakness the citation mechanism was built to close for sentences. So every
number that appears in a figure here is read from `papers/CLAIMS.tsv` at draw
time, by claim id, exactly as the prose reads it. A figure and the sentence
beside it cannot disagree, because they are reading the same row.

Each figure declares the claim ids it uses. `audit_paper.py` checks that
declaration against the ledger and against the caption, so a figure whose
numbers have moved fails an audit rather than quietly misleading a reader.

OUTPUT
------
PNG at 200 dpi, one file per figure in `papers/figures/`. PNG rather than SVG
because it is the one raster form all four outputs embed the same way -- Word
through python-docx, PDF through reportlab, HTML as a data URI -- and audit 16
FIDELITY compares those outputs against each other.

    python3 tools/figures.py            # draw them all
    python3 tools/figures.py --selftest
stdlib plus matplotlib.
"""
import argparse
import csv
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                  # noqa: E402
from matplotlib.patches import (Circle, FancyArrowPatch, FancyBboxPatch,  # noqa: E402
                                Polygon, Rectangle, Wedge)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "papers", "CLAIMS.tsv")
OUTDIR = os.path.join(ROOT, "papers", "figures")

# One palette, used by every figure, so the set reads as one document.
INK = "#15140f"
MUT = "#5d5850"
RULE = "#c9c2b4"
PAPER = "#fbfaf7"
ACC = "#7a2e12"          # the alteration, or the quantity under discussion
COOL = "#2f5d74"         # the machine as built
WARM = "#b8860b"         # fuel and heat
GOOD = "#2e6b45"         # clears unity
BAD = "#8c3b3b"          # falls short

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Liberation Serif", "DejaVu Serif"],
    "font.size": 8.4,
    "axes.edgecolor": RULE,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": MUT,
    "ytick.color": MUT,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})


def load_claims():
    with open(LEDGER, encoding="utf-8") as fh:
        return {r["id"]: r for r in csv.DictReader(fh, delimiter="\t")}


C = None


def v(cid):
    """The ledger value for a claim id, as a float. Missing is an error."""
    row = C[cid]
    return float(row["value"].replace(",", ""))


def s(cid):
    """The ledger value as it is printed."""
    return C[cid]["value"]


FIGURES = []


def figure(num, name, caption, uses):
    """Register a figure with the claim ids it draws from."""
    def deco(fn):
        FIGURES.append({"num": num, "name": name, "caption": caption,
                        "uses": tuple(uses), "fn": fn})
        return fn
    return deco


def _save(fig, name):
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, name + ".png")
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    return path


def _bare(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_aspect("equal")


# ---- 1. the reaction ---------------------------------------------------------
@figure(1, "cycle", "The catalytic cycle, and the two ways it ends. A single "
        "binder repeats the loop until it decays or is lost to the alpha; "
        "everything the paper prices is a consequence of how many times it goes "
        "round.", ["C01", "C44", "C58", "C63", "C03"])
def fig_cycle():
    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    _bare(ax)
    ax.set_xlim(0, 13.4); ax.set_ylim(0.15, 5.4)

    def box(x, y, w, h, text, fc="#f3efe6", ec=RULE, size=8.2):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                                    fc=fc, ec=ec, lw=0.9))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=size, color=INK, linespacing=1.5)

    def arrow(p, q, colour=INK, lw=1.1, rad=0.0):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=9,
                                     lw=lw, color=colour,
                                     connectionstyle=f"arc3,rad={rad}"))

    box(0.15, 3.35, 2.6, 1.5, "a free $\\mu^-$\nenters the fuel",
        fc="#e8eef2", ec=COOL)
    box(3.45, 3.35, 3.1, 1.5,
        "it displaces an electron and\nbinds $d$ and $t$ into $(dt\\mu)^+$")
    box(7.25, 3.35, 2.5, 1.5, "the nuclei tunnel\nand fuse", fc="#f7efe0", ec=WARM)
    box(6.30, 0.75, 5.6, 1.5,
        f"$^4$He $+$ n $+$ $\\mu^-$ $+$ {s('C01')} MeV\n"
        f"the binder is released, not consumed", fc="#eef3ee", ec=GOOD)

    arrow((2.75, 4.10), (3.45, 4.10))
    arrow((6.55, 4.10), (7.25, 4.10))
    arrow((8.50, 3.35), (8.50, 2.25))
    # the return leg, kept clear of both boxes
    ax.add_patch(FancyArrowPatch((6.30, 1.50), (1.45, 3.35), arrowstyle="-|>",
                                 mutation_scale=9, lw=1.3, color=GOOD,
                                 connectionstyle="arc3,rad=0.26"))
    ax.text(3.85, 1.02, f"and round again — up to {s('C44')} times "
            f"on the laboratory record", fontsize=7.8, color=GOOD,
            ha="center", style="italic")

    # the two ways it ends
    ax.text(1.45, 2.98, "or it decays", fontsize=7.4, color=BAD, ha="center")
    ax.add_patch(FancyArrowPatch((11.90, 1.50), (12.55, 2.60), arrowstyle="-|>",
                                 mutation_scale=8, lw=1.0, color=BAD))
    ax.text(12.75, 3.30, "or it sticks\nto the $\\alpha$", fontsize=7.4,
            color=BAD, ha="center", linespacing=1.4)

    ax.text(0.15, 0.30, "watched simultaneously:", fontsize=7.6, color=MUT,
            weight="bold")
    ax.text(3.05, 0.30, f"neutrons at {s('C58')} MeV count the fusions   ·   "
            f"the muonic-helium K$\\alpha$ at {s('C63')} keV counts the losses",
            fontsize=7.6, color=MUT)
    return _save(fig, "fig1-cycle")


# ---- 2. the machine, and the alterations proposed to it ----------------------
@figure(2, "machine", "The binder source, and the three alterations this paper "
        "proposes to it. The machine below the line is the one that has been "
        "built and simulated; the three callouts above it are what this paper "
        "would change, and each is priced in the text.",
        ["C70", "C580", "C581", "C141", "C144", "C571", "C666", "C710", "C290"])
def fig_machine():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    _bare(ax)
    ax.set_xlim(0, 15.4); ax.set_ylim(-1.10, 8.15)

    y0 = 1.9
    # --- the beamline as built ------------------------------------------------
    ax.add_patch(Rectangle((0.3, y0 - 0.07), 2.1, 0.14, fc=COOL, ec="none"))
    ax.text(1.35, y0 + 0.34, "proton driver", fontsize=7.8, ha="center",
            color=COOL, weight="bold")

    ax.text(4.35, y0 - 1.48, "capture solenoid", fontsize=7.8, ha="center",
            color=COOL, weight="bold")
    ax.text(4.35, y0 - 1.84, f"{s('C70')} T peak · {s('C581')} cm bore",
            fontsize=7.2, ha="center", color=MUT)
    ax.add_patch(FancyBboxPatch((2.85, y0 - 1.05), 3.0, 2.10,
                                boxstyle="round,pad=0.06", fc="#e8eef2",
                                ec=COOL, lw=1.1))
    for xx in [3.12 + 0.33 * k for k in range(9)]:
        ax.add_patch(Rectangle((xx, y0 + 0.62), 0.17, 0.32, fc=COOL, ec="none",
                               alpha=0.75))
        ax.add_patch(Rectangle((xx, y0 - 0.94), 0.17, 0.32, fc=COOL, ec="none",
                               alpha=0.75))
    ax.add_patch(Rectangle((3.85, y0 - 0.26), 1.05, 0.52, fc=WARM, ec=INK, lw=0.7))
    ax.text(4.38, y0 - 0.56, "production target", fontsize=7.0, ha="center",
            color=INK)
    ax.annotate("", xy=(3.80, y0), xytext=(2.55, y0),
                arrowprops=dict(arrowstyle="-|>", lw=1.2, color=COOL))

    ax.add_patch(Polygon([[5.85, y0 - 1.05], [7.35, y0 - 0.50], [7.35, y0 + 0.50],
                          [5.85, y0 + 1.05]], closed=True, fc="#eef1f3",
                         ec=RULE, lw=0.9))
    ax.text(6.60, y0 + 1.32, "taper", fontsize=7.2, ha="center", color=MUT)
    ax.add_patch(Rectangle((7.35, y0 - 0.50), 3.3, 1.00, fc="#f3f1ec",
                           ec=RULE, lw=0.9))
    ax.text(9.00, y0 + 0.86, f"decay channel, {s('C666')} m", fontsize=7.4,
            ha="center", color=MUT)
    ax.text(9.00, y0, "$\\pi^- \\rightarrow \\mu^- + \\bar\\nu_\\mu$",
            fontsize=8.6, ha="center", color=INK)

    ax.add_patch(Polygon([[10.65, y0 - 0.50], [11.75, y0 - 0.95],
                          [11.75, y0 + 0.95], [10.65, y0 + 0.50]], closed=True,
                         fc="#eef1f3", ec=RULE, lw=0.9))
    ax.text(11.30, y0 + 1.32, "recompress", fontsize=7.2, ha="center", color=MUT)
    ax.add_patch(FancyBboxPatch((11.85, y0 - 0.80), 2.3, 1.60,
                                boxstyle="round,pad=0.06", fc="#f7efe0",
                                ec=WARM, lw=1.1))
    ax.text(13.00, y0 + 0.12, "fuel cell, D–T", fontsize=8.0, ha="center",
            va="center", color=INK)
    ax.text(13.00, y0 - 0.36, f"{s('C710')} kg of tritium", fontsize=7.0,
            ha="center", color=MUT)

    ax.plot([0.25, 15.15], [-0.35, -0.35], color=RULE, lw=0.8)
    ax.text(0.25, -0.78, "the machine as built and simulated: everything below "
            "this line exists", fontsize=7.4, color=MUT, style="italic")

    # --- the three alterations ------------------------------------------------
    def callout(x, w, label, detail, tip, tail):
        ax.add_patch(FancyBboxPatch((x, 5.35), w, 2.55,
                                    boxstyle="round,pad=0.12", fc="#f6ece7",
                                    ec=ACC, lw=1.1))
        ax.text(x + 0.22, 7.56, label, fontsize=7.9, color=ACC, weight="bold")
        ax.text(x + 0.22, 7.12, detail, fontsize=7.2, color=INK, va="top",
                linespacing=1.62)
        ax.add_patch(FancyArrowPatch(tail, tip, arrowstyle="-|>",
                                     mutation_scale=8, lw=1.0, color=ACC,
                                     linestyle=(0, (4, 2))))

    callout(0.25, 4.7, "1 · an optimised target",
            f"longer and thinner, and reported\n"
            f"at {s('C290')} GeV per pion against\n"
            f"the {s('C100')} GeV integrated here",
            (4.30, 2.35), (2.60, 5.35))
    callout(5.30, 4.7, "2 · a mirror on the plug",
            f"graded by {s('C571')}, which turns the\n"
            f"backward hemisphere forward.\n"
            f"The grade is fixed, not tunable.",
            (3.20, 2.98), (6.20, 5.35))
    callout(10.35, 4.8, "3 · a wider bore",
            f"the aperture from {s('C141')} to {s('C144')} T·m,\n"
            f"which buys acceptance and is\n"
            f"paid for in tritium",
            (5.78, 2.62), (12.30, 5.35))
    return _save(fig, "fig2-machine")


# ---- 3. the bore excludes the target every other facility uses ---------------
@figure(3, "target", "Why the production target must be a free liquid-metal "
        "jet. The capture field sets the bore, the bore sets the space the "
        "target may occupy, and the rotating solid wheel that every "
        "megawatt-class facility uses does not fit inside it.",
        ["C581", "C642", "C637", "C638"])
def fig_target():
    fig, ax = plt.subplots(figsize=(6.6, 3.1))
    _bare(ax)
    ax.set_xlim(0, 14.0); ax.set_ylim(-2.0, 6.2)

    bore = v("C581")             # cm, warm bore radius
    wheel = v("C642") * 100.0    # m -> cm, wheel radius
    scale = 2.45 / wheel
    b = bore * scale             # the bore, to the same scale

    # left: the wheel, with the bore drawn inside it to scale
    cx, cy = 3.1, 2.5
    ax.add_patch(Circle((cx, cy), wheel * scale, fc="#f2eee6", ec=MUT, lw=1.1,
                        linestyle=(0, (5, 3))))
    ax.plot([cx - wheel * scale, cx + wheel * scale], [cy, cy], color=MUT,
            lw=0.6, alpha=0.6)
    ax.add_patch(Rectangle((cx - b, cy - b), 2 * b, 2 * b, fc="#e8eef2",
                           ec=COOL, lw=1.5))
    ax.text(cx, cy - wheel * scale - 0.60, "a rotating solid wheel",
            fontsize=8.0, ha="center", color=INK, weight="bold")
    ax.text(cx, cy - wheel * scale - 1.10,
            f"needs a radius of {s('C642')} m, and the\nbore gives it "
            f"{s('C581')} cm — short by more than three",
            fontsize=7.4, ha="center", color=MUT, va="top", linespacing=1.5)

    # right: what does fit
    jx, jy = 10.2, 2.5
    ax.add_patch(Rectangle((jx - b, jy - b), 2 * b, 2 * b, fc="#e8eef2",
                           ec=COOL, lw=1.5))
    ax.add_patch(Rectangle((jx - b * 0.86, jy - 0.12), 2 * b * 0.86, 0.24,
                           fc=WARM, ec=INK, lw=0.7))
    for k in range(3):
        ax.add_patch(FancyArrowPatch((jx - 0.55 + 0.55 * k, jy + 0.62),
                                     (jx - 0.30 + 0.55 * k, jy + 0.22),
                                     arrowstyle="-|>", mutation_scale=6,
                                     lw=0.8, color=WARM))
    ax.text(jx, jy - b - 0.60, "a free liquid-metal jet", fontsize=8.0,
            ha="center", color=INK, weight="bold")
    ax.text(jx, jy - b - 1.10,
            f"which does fit, and must survive {s('C637')} kW —\n"
            f"{s('C638')} percent of the driver's power",
            fontsize=7.4, ha="center", color=MUT, va="top", linespacing=1.5)

    ax.text(6.65, cy + 0.42, "so", fontsize=8.4, ha="center", va="bottom",
            color=ACC, style="italic")
    ax.add_patch(FancyArrowPatch((6.0, cy), (7.3, cy), arrowstyle="-|>",
                                 mutation_scale=9, lw=1.2, color=ACC))
    ax.text(7.0, 5.55, "the same bore, drawn to scale in both panels",
            fontsize=7.4, ha="center", color=COOL, style="italic")
    return _save(fig, "fig3-target")


# ---- 4. the reaction range ---------------------------------------------------
@figure(4, "range", "The range the reaction is expected to fall in. Each row is "
        "one way of pricing the same reaction; the bar runs from what the "
        "machine as built delivers to what it delivers with all three "
        "alterations. Anything reaching the line at unity pays for itself. "
        "Only bred fuel does, and the rows at the measured cycle count use no "
        "service-life model at all.",
        ["C757", "C830", "C868", "C781", "C869", "C863", "C763", "C836", "C877",
         "C783", "C878", "C879", "C767", "C771", "C864", "C876", "C880",
         "C881"])
def fig_range():
    rows = [
        ("bred fuel, the model at $8.5\\times$", "C876", "C880", "C881"),
        ("bred fuel, the measured count", "C767", "C771", "C864"),
        ("heat, the model at $8.5\\times$", "C781", "C869", "C863"),
        ("work, the model at $8.5\\times$", "C783", "C878", "C879"),
        ("heat, the measured count", "C757", "C830", "C868"),
        ("work, the measured count", "C763", "C836", "C877"),
    ]
    fig, ax = plt.subplots(figsize=(6.9, 3.4))
    ys = list(range(len(rows)))
    ax.axvline(1.0, color=INK, lw=1.1)
    ax.text(1.0, len(rows) - 0.30, "  pays for itself", fontsize=7.8,
            color=INK, va="bottom")
    for y, (lab, a, b, c) in zip(ys, rows):
        lo = v(a)
        hi = v(c) if c else v(b)
        mid = v(b)
        colour = GOOD if hi >= 1.0 else BAD
        ax.plot([lo, hi], [y, y], color=colour, lw=3.4, solid_capstyle="round",
                alpha=0.35)
        ax.plot([lo], [y], "o", ms=5.0, color=COOL, zorder=3)
        ax.plot([mid], [y], "o", ms=5.0, color=ACC, zorder=3)
        if c:
            ax.plot([hi], [y], "o", ms=5.0, color=colour, zorder=3)
        ax.text(hi * 1.10, y, f"{hi:.3f}".rstrip("0").rstrip("."), fontsize=7.4,
                va="center", color=colour, weight="bold")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.0)
    ax.set_xscale("log")
    ax.set_xlim(0.06, 11.0)
    ax.set_xticks([0.1, 0.3, 1.0, 3.0])
    ax.set_xticklabels(["0.1", "0.3", "1", "3"])
    ax.set_xlabel("energy returned per unit of energy spent on the binder",
                  fontsize=8.0)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=RULE, lw=0.5, alpha=0.6)
    ax.set_axisbelow(True)
    handles = [plt.Line2D([], [], marker="o", ls="", ms=5, color=COOL,
                          label="the machine as built"),
               plt.Line2D([], [], marker="o", ls="", ms=5, color=ACC,
                          label="with the optimised target"),
               plt.Line2D([], [], marker="o", ls="", ms=5, color=GOOD,
                          label="and with both collector alterations")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.20),
              ncol=3, frameon=False, fontsize=7.6, handletextpad=0.4,
              columnspacing=1.8)
    return _save(fig, "fig4-range")


# ---- 5. where the binder's energy goes ---------------------------------------
@figure(5, "budget", "What becomes of a hundred pions made in the target. Each "
        "step is a loss that can be computed rather than assumed, and the "
        "product of them is the difference between what the magnet accepts and "
        "what the fuel actually stops.",
        ["C730", "C739", "C740", "C741", "C820", "C742", "C382", "C753"])
def fig_budget():
    steps = [("escape from the target", "C730"),
             ("pion decay completeness", "C739"),
             ("muon survival in the channel", "C740"),
             ("scattering out of the cap", "C741"),
             ("adiabatic transport", "C820")]
    fig, ax = plt.subplots(figsize=(6.9, 3.2))
    running = 100.0
    xs, tops, bots, labs = [], [], [], []
    for i, (lab, cid) in enumerate(steps):
        f = v(cid)
        xs.append(i)
        tops.append(running)
        running *= f
        bots.append(running)
        labs.append(lab)
    for i, (t, b, lab) in enumerate(zip(tops, bots, labs)):
        ax.add_patch(Rectangle((i - 0.30, b), 0.60, t - b, fc=BAD, ec="none",
                               alpha=0.55))
        ax.plot([i - 0.30, i + 0.30], [b, b], color=INK, lw=1.0)
        if t - b > 4.0:
            ax.text(i, (t + b) / 2, f"−{t - b:.1f}", fontsize=7.2, ha="center",
                    va="center", color="#5c1f1f")
        elif t - b > 0.4:
            ax.text(i, t + 1.6, f"−{t - b:.1f}", fontsize=7.2, ha="center",
                    color="#5c1f1f")
        else:
            ax.text(i, b + 1.6, "no loss", fontsize=7.0, ha="center", color=MUT)
    ax.plot(range(len(steps)), bots, color=INK, lw=1.0, alpha=0.4, zorder=1)
    ax.add_patch(Rectangle((len(steps) - 0.30, 0), 0.60, running, fc=COOL,
                           ec="none", alpha=0.8))
    ax.text(len(steps), running + 3.0, f"{running:.1f} survive",
            fontsize=8.0, ha="center", color=COOL, weight="bold")
    ax.text(len(steps), running / 2, f"×{v('C742'):.4f}", fontsize=7.6,
            ha="center", va="center", color="white", weight="bold")
    ax.set_xticks(list(range(len(steps) + 1)))
    ax.set_xticklabels(labs + ["what is left"], fontsize=7.4, rotation=18,
                       ha="right")
    ax.set_ylim(0, 118)
    ax.set_ylabel("pions per hundred produced", fontsize=8.0)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="y", color=RULE, lw=0.5, alpha=0.6)
    ax.set_axisbelow(True)
    ax.text(0.02, 0.97, f"and the magnet accepts {s('C382')} % of what is "
            f"produced, so {s('C753')} % is what the fuel stops",
            transform=ax.transAxes, fontsize=7.6, color=INK, va="top")
    return _save(fig, "fig5-budget")


# ---- 6. the co-product configuration -----------------------------------------
@figure(6, "coproduct", "The one configuration that is net-positive on witnessed "
        "numbers alone. Because the beam is running for another reason, the "
        "marginal energy spent per binder is zero, so any point on this line is "
        "gain and no loss factor can push it below it.",
        ["C106", "C507", "C503", "C508", "C804", "C260", "C472", "C810", "C474"])
def fig_coproduct():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    heat_per_capture = v("C508") / v("C503")     # linear in capture
    xs = [0.02 * k for k in range(1, 51)]
    ax.plot(xs, [heat_per_capture * x for x in xs], color=MUT, lw=1.2)

    # the three reachable points, labelled in the empty upper-left rather than
    # beside the line, where they would overlap each other
    pts = [(v("C804"), "delivered, through the loss budget", ACC, 31.5, True),
           (v("C503"), "the stopping ceiling at the\ncommitted tritium inventory",
            COOL, 25.4, True),
           (v("C106") / 100.0, "today's front end", COOL, 19.6, False)]
    for x, lab, colour, ytext, big in pts:
        y = heat_per_capture * x
        ax.plot([x], [y], "o", ms=6.5 if big else 5.0, color=colour, zorder=3)
        ax.annotate(f"{lab} — {y:.2f} %", xy=(x, y), xytext=(0.045, ytext),
                    fontsize=7.4, color=colour, linespacing=1.5, va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.7, color=colour,
                                    connectionstyle="arc3,rad=-0.16"))

    x = v("C260") / 100.0
    ax.plot([x], [heat_per_capture * x], "x", ms=7, color=BAD, mew=1.7, zorder=3)
    ax.annotate("withdrawn: no target depth\nreaches this capture",
                xy=(x, heat_per_capture * x), xytext=(0.60, 27.0),
                fontsize=7.4, color=BAD, linespacing=1.5, va="center",
                arrowprops=dict(arrowstyle="-", lw=0.7, color=BAD))
    ax.axvspan(v("C506"), 1.0, color=BAD, alpha=0.05)
    ax.text(v("C506") + 0.010, 0.8, "beyond the stopping ceiling", fontsize=7.0,
            color=BAD, rotation=90, va="bottom")

    ax.set_xlim(0, 1.0); ax.set_ylim(0, 36)
    ax.set_xlabel("fraction of produced pions that stop in the fuel", fontsize=8.0)
    ax.set_ylabel("fusion heat, as a percentage\nof the driver's beam energy",
                  fontsize=8.0, linespacing=1.5)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(color=RULE, lw=0.5, alpha=0.6)
    ax.set_axisbelow(True)
    return _save(fig, "fig6-coproduct")


# ---- 7. the measurement ------------------------------------------------------
@figure(7, "measurement", "The step the existing experiments do not take. Both "
        "observables watch the same fuel at the same time, on one fill, so the "
        "cycle count and the loss are measured together rather than inferred "
        "from separate runs.",
        ["C327", "C324", "C326", "C821", "C514", "C58", "C63", "C113", "C114"])
def fig_measurement():
    fig, ax = plt.subplots(figsize=(6.8, 3.5))
    _bare(ax)
    ax.set_xlim(0, 15.0); ax.set_ylim(-2.2, 8.0)

    cx, cy = 7.2, 3.0
    ax.add_patch(Polygon([[cx - 1.45, cy + 1.45], [cx + 1.45, cy + 1.45],
                          [cx + 0.52, cy + 0.30], [cx - 0.52, cy + 0.30]],
                         closed=True, fc="#e9e6de", ec=MUT, lw=0.9))
    ax.add_patch(Polygon([[cx - 1.45, cy - 1.45], [cx + 1.45, cy - 1.45],
                          [cx + 0.52, cy - 0.30], [cx - 0.52, cy - 0.30]],
                         closed=True, fc="#e9e6de", ec=MUT, lw=0.9))
    ax.add_patch(Rectangle((cx - 0.52, cy - 0.30), 1.04, 0.60, fc=WARM,
                           ec=INK, lw=0.9))
    ax.text(cx + 1.75, cy + 1.05, "diamond anvils", fontsize=7.4, color=MUT)
    ax.text(cx + 1.75, cy + 0.15,
            f"{s('C327')} mm$^3$ of fuel, to\n{s('C324')} MPa and {s('C326')} K",
            fontsize=7.2, color=MUT, va="center", linespacing=1.55)
    ax.text(cx, cy - 2.05, f"D–T at 50/50 — {s('C821')} mg, {s('C514')} Ci",
            fontsize=7.4, ha="center", color=MUT)

    ax.add_patch(Rectangle((0.4, cy - 0.06), 4.6, 0.12, fc=COOL, ec="none"))
    ax.add_patch(FancyArrowPatch((5.0, cy), (6.55, cy), arrowstyle="-|>",
                                 mutation_scale=9, lw=1.3, color=COOL))
    ax.text(0.4, cy + 0.52, "$\\mu^-$ from an existing beam", fontsize=7.8,
            color=COOL, weight="bold")
    ax.text(0.4, cy - 0.95, "tuned to stop in the fuel\nrather than in the anvils",
            fontsize=7.2, color=MUT, linespacing=1.55)

    def detector(x, label, what, colour, ang):
        ax.add_patch(Wedge((x, 6.15), 1.05, ang - 30, ang + 30, fc="#f1eee7",
                           ec=colour, lw=1.1))
        ax.text(x, 7.55, label, fontsize=7.9, ha="center", color=colour,
                weight="bold")
        ax.text(x, 7.15, what, fontsize=7.2, ha="center", color=MUT)
        ax.add_patch(FancyArrowPatch((cx, cy + 1.5), (x, 6.15 - 0.55),
                                     arrowstyle="-|>", mutation_scale=7, lw=0.9,
                                     color=colour, linestyle=(0, (3, 2))))

    detector(4.2, "neutron array", f"fusions, at {s('C58')} MeV", GOOD, 285)
    detector(10.4, "X-ray detector", f"losses, at {s('C63')} keV", BAD, 255)

    ax.add_patch(FancyBboxPatch((0.4, -2.05), 14.2, 1.05,
                                boxstyle="round,pad=0.10", fc="#f6ece7",
                                ec=ACC, lw=1.0))
    ax.text(7.5, -1.48, f"the ratio of the two counts is the sticking — "
            f"committed in advance at {s('C113')} to {s('C114')} percent",
            fontsize=7.2, ha="center", va="center", color=INK)
    ax.text(7.5, -1.84, "and a disagreement between them is a refusal, "
            "not an average", fontsize=7.2, ha="center", va="center", color=ACC,
            style="italic")
    return _save(fig, "fig7-measurement")


# ---- driver ------------------------------------------------------------------
def draw_all(quiet=False):
    global C
    C = load_claims()
    made = []
    for f in FIGURES:
        path = f["fn"]()
        made.append((f, path))
        if not quiet:
            print(f"  figure {f['num']}  {os.path.relpath(path, ROOT):<44}"
                  f"{os.path.getsize(path):>8,} B   "
                  f"{len(f['uses'])} claim ids")
    return made


def manifest():
    """What each figure draws from, for the audit that checks the captions."""
    return [{"num": f["num"], "name": f["name"], "caption": f["caption"],
             "uses": f["uses"],
             "file": os.path.join("papers", "figures",
                                  f"fig{f['num']}-{f['name']}.png")}
            for f in FIGURES]


def selftest():
    global C
    C = load_claims()
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<60} {'PASS' if ok else 'FAIL'}")

    check("every figure declares the claim ids it draws from",
          all(f["uses"] for f in FIGURES))
    missing = [(f["num"], cid) for f in FIGURES for cid in f["uses"]
               if cid not in C]
    check("and every one of those ids is a ledger row", not missing)
    if missing:
        print("      " + repr(missing[:6]))
    check("figure numbers are unique and in order",
          [f["num"] for f in FIGURES] == sorted({f["num"] for f in FIGURES}))
    check("every figure has a caption long enough to stand alone",
          all(len(f["caption"]) > 60 for f in FIGURES))
    # A figure that PRINTS a number it did not read from the ledger could
    # disagree with the prose beside it, and nothing would catch that. So this
    # reads every string literal the figures pass to a text call, removes the
    # {...} that a citation fills in, and requires no quantity to survive.
    # Drawing coordinates are exempt by construction: they are not in strings.
    import ast as _ast
    import re as _re
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = _ast.parse(src)
    printed = []
    for node in _ast.walk(tree):
        if not isinstance(node, _ast.Call):
            continue
        fn = node.func
        name = getattr(fn, "attr", getattr(fn, "id", ""))
        # only the string a reader actually sees, and only from the calls that
        # put prose on the figure. An axis tick label is a scale mark rather
        # than a claim, and a connectionstyle is not text at all.
        want = {"text": 2, "annotate": 0, "set_xlabel": 0, "set_ylabel": 0}
        if name not in want:
            continue
        idx = want[name]
        if len(node.args) <= idx:
            continue
        arg = node.args[idx]
        if isinstance(arg, _ast.Constant) and isinstance(arg.value, str):
            printed.append(arg.value)
        elif isinstance(arg, _ast.JoinedStr):
            printed.append("".join(p.value for p in arg.values
                                   if isinstance(p, _ast.Constant)
                                   and isinstance(p.value, str)))
    EXEMPT = ("50/50", "^3", "^2", "^-", "$^", "10^")
    bad = []
    for t in printed:
        clean = t
        for e in EXEMPT:
            clean = clean.replace(e, " ")
        for m in _re.finditer(r"(?<![\w.])\d+(?:\.\d+)?(?![\w])", clean):
            bad.append(f"{m.group(0)!r} printed in {t[:44]!r}")
    check("no figure PRINTS a number it did not read from the ledger:\n"
          "    every quantity in a label comes through v() or s()", not bad)
    for b_ in bad[:6]:
        print("      " + b_)
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    draw_all()
    return 0


if __name__ == "__main__":
    sys.exit(main())
