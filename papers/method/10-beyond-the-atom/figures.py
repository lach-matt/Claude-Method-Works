#!/usr/bin/env python3
"""figures.py -- regenerates every computed figure in figures/ from the data check.py verifies.

    python3 figures.py

Figure 1 (figures/figure-1-periodic-table.png) is an audited plate copied from the tree and is not
regenerated here; FIGURES.tsv records its source and md5. Figures 2-4 are drawn from check.py's
VALUES after a full run; nothing is drawn by hand.
"""
import contextlib
import io
import os
import sys
import importlib.util as iu

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

spec = iu.spec_from_file_location("check", os.path.join(HERE, "check.py"))
check = iu.module_from_spec(spec)
sys.modules["check"] = check
spec.loader.exec_module(check)
with contextlib.redirect_stdout(io.StringIO()):
    V = check.compute_all()
if check.FAIL:
    print("check.py reports %d failures; figures not drawn" % check.FAIL)
    sys.exit(1)

BLUE, ORANGE = "#2a78d6", "#eb6834"      # categorical slots 1 and 2 of the reference palette
INK, INK2, GRID = "#0b0b0b", "#52514e", "#dcdcd8"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2,
                     "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.spines.top": False, "axes.spines.right": False})


def bars_h(ax, labels, values, color, fmt=lambda v: str(v)):
    y = range(len(labels))
    ax.barh(y, values, color=color, height=0.62, linewidth=0)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.grid(axis="x", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for i, v in enumerate(values):
        ax.text(v + max(values) * 0.01, i, fmt(v), va="center", ha="left", color=INK, fontsize=8.5)


# ---------------------------------------------------------------- Figure 2: the defect table
rows = [
    ("chessboard (rank, file)", 64, 64, 0),
    ("box ordering l ≥ w ≥ h", V["box_cells"], V["box_box"], V["box_E"]),
    ("Janet (n+ℓ, Z)", V["jan_cells"], V["jan_box"], V["jan_E"]),
    ("Λ (eight coordinates)", V["lam_cells"], V["lam_box"], V["lam_E"]),
    ("Λ₉ (nine coordinates)", V["L9_cells"], V["L9_box"], 0),
    ("dipole image (|Δℓ|, |ΔS|)", 8, 8, 0),
    ("AME2020 nuclides (Z, N)", V["ame_cells"], None, V["ame_E"]),
    ("calendar (month, day)", V["cal_cells"], V["cal_box"], V["cal_E"]),
    ("particle-bound nuclides Z ≤ 7 (Z, N)", V["nuc_cells"], None, V["nuc_E"]),
    ("periodic table (period, group)", V["pt_cells"], V["pt_box"], V["pt_E"]),
    ("Kreuzer–Skarke χ = ±6 slice", V["ks_cells"], V["ks_box"], V["ks_E"]),
]
fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=200)
labels = ["%s — %s cells" % (n, format(c, ",")) for n, c, b, e in rows]
bars_h(ax, labels, [e for *_, e in rows], BLUE)
ax.set_xlabel("closure defect E = |ℛ(X)| − |X|")
ax.set_xlim(0, 600)
ax.set_title("The closure defect of eleven indexes", loc="left", color=INK, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-2-defects.png"))
plt.close(fig)

# ---------------------------------------------------------------- Figure 3: redundancy
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.1), dpi=200, gridspec_kw={"width_ratios": [1.1, 1]})
proj = V["proj"]                                   # (d, cells, redundancy)
ds = [d for d, _, _ in proj]
rs = [100 * float(r) for _, _, r in proj]
a1.bar(ds, rs, color=BLUE, width=0.62, linewidth=0)
for d, r in zip(ds, rs):
    a1.text(d, r + 1.2, "%.0f%%" % r, ha="center", va="bottom", color=INK, fontsize=8.5)
a1.set_xlabel("coordinates kept, d (Λ projected to its first d)")
a1.set_ylabel("redundancy (%)")
a1.set_ylim(0, 72)
a1.grid(axis="y", color=GRID, linewidth=0.6)
a1.set_axisbelow(True)
a1.set_title("Redundancy against dimension, one object", loc="left", color=INK, fontsize=9.5)
tab = V["red_table"]                               # (name, d, envelopes, coupling, redundancy, E, cells)
short = {"Lambda": "Λ", "channel survey grid": "survey grid", "box ordering": "box ordering",
         "Janet down-set": "Janet", "periodic table": "periodic table", "calendar": "calendar"}
for name, d, nenv, cp, rd, e, n in tab:
    a2.scatter(100 * float(cp), 100 * float(rd), s=34, color=BLUE, zorder=3, edgecolor="white", linewidth=1)
seen = {}
for name, d, nenv, cp, rd, e, n in tab:
    key = (round(float(cp), 3), round(float(rd), 3))
    seen.setdefault(key, []).append(short[name])
for (x, y), names in seen.items():
    a2.annotate(", ".join(names), (100 * x, 100 * y), xytext=(5, 4), textcoords="offset points", fontsize=8, color=INK)
a2.set_xlabel("coupling: envelopes that bind (%)")
a2.set_ylabel("redundancy (%)")
a2.set_xlim(-4, 62)
a2.set_ylim(-5, 72)
a2.grid(color=GRID, linewidth=0.6)
a2.set_axisbelow(True)
a2.set_title("Redundancy against coupling: r² = %s" % V["r2"], loc="left", color=INK, fontsize=9.5)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-3-redundancy.png"))
plt.close(fig)

# ---------------------------------------------------------------- Figure 4: the crossing
cr = V["crossing"]
order = ["all", "allowed", "forbidden", "parity-conserving", "parity-changing"]
names = ["all cells", "dipole-allowed\n|Δℓ| = 1", "forbidden\n|Δℓ| ≠ 1", "parity-\nconserving", "parity-\nchanging"]
within = [100 * float(cr[k][2]) for k in order]
across = [100 * float(cr[k][4]) for k in order]
fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=200)
x = range(len(order))
w = 0.36
ax.bar([i - w / 2 for i in x], within, width=w - 0.03, color=BLUE, linewidth=0, label="followable within one element")
ax.bar([i + w / 2 for i in x], across, width=w - 0.03, color=ORANGE, linewidth=0, label="followable across the 118 elements")
for i in x:
    ax.text(i - w / 2, within[i] + 1.2, "%.1f" % within[i], ha="center", va="bottom", fontsize=8, color=INK)
    ax.text(i + w / 2, across[i] + 1.2, "%.1f" % across[i], ha="center", va="bottom", fontsize=8, color=INK)
ax.set_xticks(list(x))
ax.set_xticklabels(names)
ax.set_ylabel("followable cells (%)")
ax.set_ylim(0, 100)
ax.grid(axis="y", color=GRID, linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=8.5)
ax.set_title("The crossing", loc="left", color=INK, fontsize=9.5, pad=22)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-4-crossing.png"))
plt.close(fig)
print("figures written to", OUT)
