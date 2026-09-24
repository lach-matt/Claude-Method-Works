#!/usr/bin/env python3
"""figures.py -- regenerates every figure in figures/ from the data check.py verifies.

    python3 figures.py

All four figures are drawn from check.py's VALUES (and, for Figure 1, from its periodic_cells()
and R) after a full clean run; nothing is drawn by hand. Figure 1 replaces the audited plate that
was used until 2026-09-24 (its title collided with the first row of cells and it had no legend);
the cells it draws are C2 / C2b of check.py.
"""
import contextlib
import io
import os
import sys
import importlib.util as iu

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle

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

BLUE, ORANGE, RED = "#2a78d6", "#eb6834", "#d33f3f"      # categorical slots of the reference palette
INK, INK2, GRID = "#0b0b0b", "#52514e", "#dcdcd8"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2,
                     "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "axes.spines.top": False, "axes.spines.right": False})

# ---------------------------------------------------------------- Figure 1: the periodic table as an index
pt = check.periodic_cells()
gaps = sorted(check.R(pt) - set(pt))
fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=200)
for (p, g), col in [(c, BLUE) for c in pt] + [(c, RED) for c in gaps]:
    ax.add_patch(Rectangle((g - 0.5, p - 0.5), 1, 1, facecolor=col, edgecolor="white", linewidth=0.8))
ax.set_xlim(0.5, 18.5)
ax.set_ylim(7.5, 0.5)
ax.set_xticks(range(1, 19))
ax.set_yticks(range(1, 8))
ax.set_xlabel("group")
ax.set_ylabel("period")
ax.set_aspect("equal")
ax.set_title("The periodic table as an index on (period, group): %d cells held, %d admitted and absent" % (len(pt), len(gaps)),
             loc="left", color=INK, fontsize=9.5, pad=8)
ax.legend(handles=[Patch(color=BLUE, label="held (%d)" % len(pt)), Patch(color=RED, label="admitted and absent (%d)" % len(gaps))],
          frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, fontsize=8.5)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-1-periodic-table.png"))
plt.close(fig)

# ---------------------------------------------------------------- Figure 2: the defect table, grouped
rows = [
    ("Λ (eight coordinates)", V["lam_cells"], V["lam_E"], "theorem"),
    ("Λ₉", V["L9_cells"], 0, "theorem"),
    ("Λ₁₀", V["L10_cells"], 0, "theorem"),
    ("Janet (n+ℓ, Z)", V["jan_cells"], V["jan_E"], "theorem"),
    ("box ordering l ≥ w ≥ h", V["box_cells"], V["box_E"], "theorem"),
    ("product grid (Z, c, ℓ)", V["sp_cells"], 0, "theorem"),
    ("chessboard (rank, file)", 64, 0, "full box"),
    ("dipole image (|Δℓ|, |ΔS|)", 8, 0, "full box"),
    ("three capped oscillators", 64, 0, "full box"),
    ("AME2020 nuclides (Z, N)", V["ame_cells"], V["ame_E"], "named"),
    ("calendar (month, day)", V["cal_cells"], V["cal_E"], "named"),
    ("particle-bound nuclides Z ≤ 7", V["nuc_cells"], V["nuc_E"], "named"),
    ("particle-bound nuclides Z ≤ 10", V["nuc10_cells"], V["nuc10_E"], "named"),
    ("periodic table (period, group)", V["pt_cells"], V["pt_E"], "named"),
    ("witnessed channels (Z, c, ℓ)", V["wit_cells"], V["wit_E"], "named"),
    ("Kreuzer–Skarke χ = ±6 slice", V["ks_cells"], V["ks_E"], "forced"),
]
COL = {"theorem": BLUE, "full box": "#8fb6e8", "named": ORANGE, "forced": RED}
fig, ax = plt.subplots(figsize=(7.2, 5.2), dpi=200)
labels = ["%s — %s cells" % (n, format(c, ",")) for n, c, e, g in rows]
y = list(range(len(rows)))
ax.barh(y, [e for _, _, e, _ in rows], color=[COL[g] for *_, g in rows], height=0.62, linewidth=0)
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.grid(axis="x", color=GRID, linewidth=0.6)
ax.set_axisbelow(True)
for i, (_, _, e, _) in enumerate(rows):
    ax.text(e + 8, i, str(e), va="center", ha="left", color=INK, fontsize=8.5)
ax.set_xlabel("closure defect E = |ℛ(X)| − |X|")
ax.set_xlim(0, 1080)
ax.legend(handles=[Patch(color=COL["theorem"], label="closed by theorem (Proposition 2)"),
                   Patch(color=COL["full box"], label="full box (Theorem 2)"),
                   Patch(color=COL["named"], label="open, admitted-and-absent cells named"),
                   Patch(color=COL["forced"], label="open by construction (hole in a difference)")],
          frameon=False, loc="upper right", fontsize=8)
ax.set_title("The closure defect of the sixteen rows of Table 1", loc="left", color=INK, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-2-defects.png"))
plt.close(fig)

# ---------------------------------------------------------------- Figure 3: redundancy
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.1), dpi=200, gridspec_kw={"width_ratios": [1.1, 1]})
proj = V["proj"]                                   # (d, cells, redundancy)
ds = [d for d, _, _ in proj]
rs = [100 * float(r) for _, _, r in proj]
cols = [BLUE if V["proj_logs"][d] else GRID for d, _, _ in proj]
a1.bar(ds, [r if V["proj_logs"][d] else 2 for d, r in zip(ds, rs)], color=cols, width=0.62, linewidth=0)
for d, r in zip(ds, rs):
    a1.text(d, (r if V["proj_logs"][d] else 2) + 1.2, "%.0f%%" % r if V["proj_logs"][d] else "below\nresolution",
            ha="center", va="bottom", color=INK, fontsize=8 if V["proj_logs"][d] else 7)
a1.set_xlabel("coordinates kept, d (Λ projected to its first d)")
a1.set_ylabel("redundancy rung reached (%)")
a1.set_ylim(0, 72)
a1.grid(axis="y", color=GRID, linewidth=0.6)
a1.set_axisbelow(True)
a1.set_title("Rung reached against dimension, one object", loc="left", color=INK, fontsize=9.5)
tab = V["red_table"]                               # (name, d, envelopes, coupling, redundancy, E, cells)
short = {"Lambda": "Λ", "channel survey grid": "product grid", "box ordering": "box ordering",
         "Janet down-set": "Janet", "periodic table": "periodic table", "calendar": "calendar"}
for name, d, nenv, cp, rd, e, n in tab:
    a2.scatter(100 * float(cp), 100 * float(rd), s=34, color=BLUE, zorder=3, edgecolor="white", linewidth=1)
seen = {}
for name, d, nenv, cp, rd, e, n in tab:
    key = (round(float(cp), 3), round(float(rd), 3))
    seen.setdefault(key, []).append(short[name])
for (x, yy), names in seen.items():
    a2.annotate(", ".join(names), (100 * x, 100 * yy), xytext=(5, 4), textcoords="offset points", fontsize=8, color=INK)
a2.set_xlabel("coupling: envelopes that bind (%)")
a2.set_ylabel("redundancy rung reached (%)")
a2.set_xlim(-4, 62)
a2.set_ylim(-5, 72)
a2.grid(color=GRID, linewidth=0.6)
a2.set_axisbelow(True)
a2.set_title("Rung reached against coupling, six indexes", loc="left", color=INK, fontsize=9.5)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figure-3-redundancy.png"))
plt.close(fig)

# ---------------------------------------------------------------- Figure 4: followability on two populations
order = ["all", "allowed", "forbidden", "parity-conserving", "parity-changing"]
names = ["all cells", "allowed\n|Δℓ| = 1", "forbidden\n|Δℓ| ≠ 1", "Δℓ even", "Δℓ odd"]
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.4), dpi=200, sharey=True)
for ax, key, title in ((axes[0], "crossing", "Unfiltered population, %s moves" % format(V["cr_cells"], ",")),
                       (axes[1], "crossing_phys", "Physical one-electron moves, %d" % V["cr_phys"])):
    cr = V[key]
    within = [100 * float(cr[k][2]) for k in order]
    across = [100 * float(cr[k][4]) for k in order]
    x = range(len(order))
    w = 0.36
    ax.bar([i - w / 2 for i in x], within, width=w - 0.03, color=BLUE, linewidth=0, label="within one element")
    ax.bar([i + w / 2 for i in x], across, width=w - 0.03, color=ORANGE, linewidth=0, label="across the 118 elements")
    for i in x:
        ax.text(i - w / 2, within[i] + 1.2, "%.1f" % within[i], ha="center", va="bottom", fontsize=7, color=INK)
        ax.text(i + w / 2, across[i] + 1.2, "%.1f" % across[i], ha="center", va="bottom", fontsize=7, color=INK)
    ax.set_xticks(list(x))
    ax.set_xticklabels(names, fontsize=7.5)
    ax.set_ylim(0, 100)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.set_title(title, loc="left", color=INK, fontsize=9)
axes[0].set_ylabel("followable cells (%)")
fig.legend(*axes[0].get_legend_handles_labels(), frameon=False, loc="lower center", ncol=2, fontsize=8, bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(os.path.join(OUT, "figure-4-crossing.png"))
plt.close(fig)
print("figures written to", OUT)
