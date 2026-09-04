#!/usr/bin/env python3
"""fig3d.py -- 3D spectra index from sealed rt/nlchain.jsonl. Visualization only."""
import json, numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

rows = [json.loads(l) for l in open('rt/nlchain.jsonl')]
LC = {0: '#1f6feb', 1: '#e36209', 2: '#2da44e', 3: '#cf222e', 4: '#8250df'}
LN = 'spdfg'
MAD = ['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p','8s','5g','6g','7g','8g']
YPOS = {ch: i for i, ch in enumerate(MAD)}
EXC = {57: 'La', 89: 'Ac', 90: 'Th'}

series = {}
for r in rows:
    for ch, d in r['order']:
        if ch in YPOS:
            series.setdefault(ch, []).append((r['Z'], d))

def render(elev, azim, fname):
    fig = plt.figure(figsize=(14, 9))
    ax = fig.add_subplot(111, projection='3d')
    verts, colors, ys = [], [], []
    for ch in MAD:
        if ch not in series: continue
        pts = sorted(series[ch])
        zs, ds = zip(*pts)
        poly = [(zs[0], 0.0)] + list(zip(zs, ds)) + [(zs[-1], 0.0)]
        verts.append(poly); ys.append(YPOS[ch])
        colors.append(LC[LN.index(ch[-1])])
    pc = PolyCollection(verts, facecolors=colors, edgecolors='k',
                        linewidths=0.5, alpha=0.55)
    ax.add_collection3d(pc, zs=ys, zdir='y')
    # entrant trajectory threading the sheet
    ez = [r['Z'] for r in rows if r['ent'] in YPOS]
    ey = [YPOS[r['ent']] for r in rows if r['ent'] in YPOS]
    ed = [r['D_ent'] for r in rows if r['ent'] in YPOS]
    ax.plot(ez, ey, ed, color='black', lw=2.6, zorder=50, label='entrant path')
    for Z, nm in EXC.items():
        r = next(x for x in rows if x['Z'] == Z)
        ax.scatter([Z], [YPOS[r['ent']]], [r['D_ent']], s=70, facecolors='yellow',
                   edgecolors='black', lw=1.2, zorder=60)
        ax.text(Z, YPOS[r['ent']], r['D_ent'] + 0.06, nm, fontsize=9, ha='center')
    # evidentiary boundary plane at Z=108.5
    yy, zz = np.meshgrid([0, len(MAD) - 1], [-0.9, 0.02])
    ax.plot_surface(np.full_like(yy, 108.5, dtype=float), yy, zz,
                    color='0.3', alpha=0.12, zorder=5)
    ax.text(109.5, len(MAD) - 1.5, 0.04, 'Z=108\nboundary', fontsize=8)
    ax.set_xlabel('Z'); ax.set_xlim(0, 122)
    ax.set_yticks(range(len(MAD))); ax.set_yticklabels(MAD, fontsize=6.5)
    ax.set_ylim(0, len(MAD) - 1)
    ax.set_zlabel('depth (Ha)'); ax.set_zlim(-0.9, 0.02)
    ax.set_title('THE SPECTRA INDEX IN 3D, Z = 2-120\nchannel ribbons = candidate depths of the '
                 '$V^{N-1}$ walk (colored by l); black line = entrant path;\nflat purple ribbons '
                 '= g channels pinned at $-1/(2n^2)$ (no g block); yellow = tie-break exceptions '
                 '(derived); grey plane = evidentiary boundary', fontsize=10)
    ax.view_init(elev=elev, azim=azim)
    ax.invert_zaxis() if False else None
    plt.tight_layout()
    plt.savefig(fname, dpi=165)
    plt.close()

render(28, -63, '/mnt/user-data/outputs/FIG5-spectra-index-3D.png')
render(18, -18, '/mnt/user-data/outputs/FIG5b-spectra-index-3D-side.png')
print("3D figures written")