#!/usr/bin/env python3
"""figs104.py -- j-120 spectra-index figures from SEALED data only (rt/nlchain.jsonl,
OUTPUT-BEYOND-109-120 values, S103 G4 table). Visualization; no solve."""
import json, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

rows = [json.loads(l) for l in open('rt/nlchain.jsonl')]
LC = {0: '#1f6feb', 1: '#e36209', 2: '#2da44e', 3: '#cf222e', 4: '#8250df'}
LN = 'spdfg'
MAD = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p','8s']
YPOS = {ch: i for i, ch in enumerate(MAD)}
EXC = {57: 'La', 89: 'Ac', 90: 'Th'}

# ---------- FIG 1: the filling index 2-120 ----------
fig, ax = plt.subplots(figsize=(13, 6.5))
for r in rows:
    Z, ent = r['Z'], r['ent']
    if ent not in YPOS: continue
    l = r['ent_nl'][1]
    pred = Z > 108
    ax.scatter(Z, YPOS[ent], s=46, c=LC[l], marker='s' if not pred else 'D',
               edgecolors='black' if not pred else LC[l], linewidths=0.4,
               facecolors=LC[l] if not pred else 'white', zorder=3)
for Z, nm in EXC.items():
    r = next(x for x in rows if x['Z'] == Z)
    ax.scatter(Z, YPOS[r['ent']], s=200, facecolors='none', edgecolors='black',
               linewidths=1.6, zorder=4)
    ax.annotate('%s %d\n(tie-break, derived:\ncollapse condition)' % (nm, Z),
                (Z, YPOS[r['ent']]), textcoords='offset points', xytext=(8, 14),
                fontsize=7, ha='left')
ax.axvline(108.5, color='k', ls='--', lw=1)
ax.text(108.8, 18.9, 'evidentiary boundary Z=108\n(right: PREDICTED output,\nfalsifiable; Dirac-Fock (n,l,j)\nsequence reproduced)', fontsize=7.5, va='top')
for i, ch in enumerate(MAD):
    ax.axhline(i, color='0.92', lw=0.5, zorder=0)
ax.set_yticks(range(len(MAD))); ax.set_yticklabels(MAD, fontsize=9)
ax.set_xlabel('Z'); ax.set_xlim(0, 122); ax.set_ylim(-0.8, len(MAD) - 0.2)
ax.set_title('THE FILLING INDEX, Z = 2-120 -- entrant channel per row, derived from the '
             'many-electron field\n(scalar-relativistic Koelling-Harmon HF; c = 137.035999 the '
             'only entered number; ordering clause 107/107)', fontsize=10)
hs = [plt.Line2D([], [], marker='s', ls='', color=LC[i], label=LN[i]) for i in range(4)]
hs.append(plt.Line2D([], [], marker='D', ls='', markerfacecolor='white', color='0.4', label='predicted (Z>108)'))
ax.legend(handles=hs, loc='upper left', fontsize=8, framealpha=0.95)
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/FIG1-filling-index-2-120.png', dpi=170)
plt.close()

# ---------- FIG 2: the spectra index (candidate depths vs Z) ----------
fig, ax = plt.subplots(figsize=(13, 7))
series = {}
for r in rows:
    for ch, d in r['order']:
        series.setdefault(ch, []).append((r['Z'], d))
for ch, pts in series.items():
    if ch not in YPOS and ch[-1] != 'g': continue
    zs, ds = zip(*sorted(pts))
    l = LN.index(ch[-1])
    if ch[-1] == 'g':
        ax.plot(zs, ds, color=LC[4], lw=1.1, alpha=0.85, zorder=2)
        ax.annotate('%s pinned at -1/(2n^2)' % ch, (zs[-1], ds[-1]), fontsize=7,
                    color=LC[4], xytext=(3, 0), textcoords='offset points', va='center')
    else:
        ax.plot(zs, ds, color=LC[l], lw=0.9, alpha=0.55, zorder=1)
ent_z = [r['Z'] for r in rows]; ent_d = [r['D_ent'] for r in rows]
ax.plot(ent_z, ent_d, color='black', lw=2.2, zorder=3, label='entrant depth $D_{ent}$')
run_d = [r['D_ent'] + r['margin'] for r in rows]
ax.fill_between(ent_z, ent_d, run_d, color='0.75', alpha=0.5, zorder=2,
                label='margin to runner-up')
ax.axvline(108.5, color='k', ls='--', lw=1)
for Z, nm in EXC.items():
    r = next(x for x in rows if x['Z'] == Z)
    ax.scatter(Z, r['D_ent'], s=90, facecolors='none', edgecolors='black', lw=1.4, zorder=5)
    ax.annotate(nm, (Z, r['D_ent']), xytext=(0, -13), textcoords='offset points',
                ha='center', fontsize=8)
ax.annotate('113: 7p entrant\n(Law B domain edge)', (113, -0.16), xytext=(-95, -42),
            textcoords='offset points', fontsize=8,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlabel('Z'); ax.set_ylabel('channel depth  (Ha)')
ax.set_xlim(0, 122); ax.set_ylim(-0.95, 0.01)
ax.set_title('THE SPECTRA INDEX, Z = 2-120 -- candidate-channel depths of the $V^{N-1}$ walk\n'
             '(entrant bold; grey band = margin; g channels pinned flat: the field contains no '
             'g block anywhere in Z <= 120)', fontsize=10)
ax.legend(loc='lower left', fontsize=8)
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/FIG2-spectra-index-2-120.png', dpi=170)
plt.close()

# ---------- FIG 3: the j-120 window ----------
fig, ax = plt.subplots(figsize=(9, 5.5))
w = [r for r in rows if r['Z'] >= 109]
zs = [r['Z'] for r in w]
de = [r['D_ent'] for r in w]; ru = [r['D_ent'] + r['margin'] for r in w]
cols = [LC[r['ent_nl'][1]] for r in w]
for r, z, d, u, c in zip(w, zs, de, ru, cols):
    ax.plot([z, z], [d, u], color='0.6', lw=1.2, zorder=1)
    ax.scatter(z, d, s=90, c=c, zorder=3, marker='D', edgecolors='black', lw=0.5)
    ax.scatter(z, u, s=40, c='0.45', zorder=2, marker='_')
    ax.annotate(r['ent'], (z, d), xytext=(0, -14), textcoords='offset points',
                ha='center', fontsize=9, color=c)
ax.axhspan(-0.083, 0, color='#cf222e', alpha=0.07)
ax.text(109.1, -0.078, 'spin-orbit worst-case narrowing <= 0.083 Ha (s97/s98):\nDirac kernel '
        'non-gating -- every margin clears', fontsize=7.5, va='bottom')
ax.set_xlabel('Z'); ax.set_ylabel('depth (Ha)')
ax.set_title('THE j-120 WINDOW, Z = 109-120 -- PREDICTED output (no experimental score '
             'exists)\nentrant (diamond) vs runner-up (tick); sequence reproduces Dirac-Fock '
             '(n,l,j) ordering; falsifiable when spectra are taken', fontsize=9.5)
ax.set_xticks(zs); ax.set_ylim(-0.47, 0.0)
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/FIG3-j120-window.png', dpi=170)
plt.close()

# ---------- FIG 4: correlation widening at the five V5 rows ----------
fig, ax = plt.subplots(figsize=(8.5, 5))
V5 = [38, 56, 72, 89, 105]
pt = {38: 1.33, 56: 1.24, 72: 2.65, 89: 2.20, 105: 2.16}
lo = {38: 1.33, 56: 1.24, 72: 2.57, 89: 1.92, 105: 2.16}
hi = {38: 1.33, 56: 1.24, 72: 2.73, 89: 3.32, 105: 2.16}
x = np.arange(5)
ax.bar(x, [pt[z] for z in V5], 0.55, color='#2da44e', alpha=0.85, zorder=2)
ax.errorbar(x, [pt[z] for z in V5],
            yerr=[[pt[z] - lo[z] for z in V5], [hi[z] - pt[z] for z in V5]],
            fmt='none', ecolor='black', capsize=5, lw=1.3, zorder=3)
ax.axhline(0, color='k', lw=1); ax.axhline(1, color='0.4', ls=':', lw=1)
ax.text(4.45, 1.03, 'dm2 = margin\n(break-even)', fontsize=7.5, ha='right')
ax.set_xticks(x); ax.set_xticklabels(['Z=%d' % z for z in V5])
ax.set_ylabel('dm2 / margin')
ax.set_title('CORRELATION WIDENS EVERY CONTESTED ROW (Lowdin criterion 3)\nsecond-order '
             'differential at the five V5 rows: every row > 0, no flip; brackets = declared '
             'estimate envelopes\n(consumer bounds clear at worst 26x -- S103 G4 table)',
             fontsize=9.5)
ax.set_ylim(0, 3.6)
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/FIG4-dm2-widening.png', dpi=170)
plt.close()
print("four figures written")
