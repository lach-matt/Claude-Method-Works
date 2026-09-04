#!/usr/bin/env python3
"""fig6.py -- FIG 6: relativistic vs non-relativistic filling index, from the two sealed
chains (rt/nlchain.jsonl, rt/cinf.jsonl). Visualization only."""
import json
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

sr = [json.loads(l) for l in open('rt/nlchain.jsonl') if json.loads(l)['Z'] <= 108]
nr = [json.loads(l) for l in open('rt/cinf.jsonl')]
LC = {0: '#1f6feb', 1: '#e36209', 2: '#2da44e', 3: '#cf222e'}
SYM = {25:'Mn',30:'Zn',47:'Ag',48:'Cd',60:'Nd',61:'Pm',62:'Sm',71:'Lu',80:'Hg',103:'Lr',104:'Rf'}
S = {r['Z']: r for r in sr}; N = {r['Z']: r for r in nr}
diff = sorted(z for z in set(S) & set(N) if S[z]['ent'] != N[z]['ent'])

fig, ax = plt.subplots(figsize=(13, 4.6))
for z in sorted(S):
    ax.add_patch(plt.Rectangle((z - 0.5, 1.0), 1, 0.8,
                 color=LC[S[z]['ent_nl'][1]], ec='white', lw=0.3))
for z in sorted(N):
    ax.add_patch(plt.Rectangle((z - 0.5, 0.0), 1, 0.8,
                 color=LC[N[z]['ent_nl'][1]], ec='white', lw=0.3))
for z in diff:
    ax.add_patch(plt.Rectangle((z - 0.5, -0.12), 1, 2.04, fill=False,
                 ec='black', lw=1.6, zorder=5))
    ax.annotate('%s\n%d' % (SYM[z], z), (z, 1.95), ha='center', fontsize=7.5)
    ax.annotate('%s' % N[z]['ent'], (z, 0.4), ha='center', va='center',
                fontsize=6.5, color='white', fontweight='bold', zorder=6)
    ax.annotate('%s' % S[z]['ent'], (z, 1.4), ha='center', va='center',
                fontsize=6.5, color='white', fontweight='bold', zorder=6)
ax.text(0.2, 1.4, 'c = 137.035999\n(this work: matches\nobservation 107/107)',
        ha='right', va='center', fontsize=8.5)
ax.text(0.2, 0.4, 'c ' + r'$\to\infty$' + '\n(non-relativistic:\neleven elements move)',
        ha='right', va='center', fontsize=8.5)
ax.set_xlim(-14, 110); ax.set_ylim(-0.35, 2.35)
ax.set_yticks([]); ax.set_xlabel('Z')
ax.set_xticks(range(10, 109, 10))
ax.spines[['left', 'top', 'right']].set_visible(False)
hs = [plt.Line2D([], [], marker='s', ls='', color=LC[i], markersize=9, label='spdf'[i])
      for i in range(4)]
ax.legend(handles=hs, loc='lower left', fontsize=8, ncol=4, framealpha=0.95,
          bbox_to_anchor=(0.0, -0.28))
ax.set_title('THE TABLE IS RELATIVISTIC -- the derived filling index with the speed of light '
             'switched off\nSame equation, same algorithm, same single constant removed: the '
             'non-relativistic field misplaces Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf',
             fontsize=10)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/FIG6-relativistic-vs-nonrelativistic.png', dpi=170)
print('fig6 written; divergent Z:', diff)