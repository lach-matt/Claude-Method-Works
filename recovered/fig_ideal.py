import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch, FancyArrowPatch
from matplotlib.lines import Line2D
from collections import Counter
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
maxel=[x for x in occ if not any(leq(x,y) and x!=y for y in occ)]
Ls=set(L)
nxt=set()
for m in maxel:
    for d in range(3):
        c=list(m); c[d]+=1; c=tuple(c)
        if c in Ls and c not in occ: nxt.add(c)

OCC='#2c5f9e'; EMP='#d6d1c8'; FR='#0a7a3a'; NX='#c8860a'

fig = plt.figure(figsize=(12.6, 4.15))
gs = fig.add_gridspec(1, 3, width_ratios=[1.30, 1.00, 1.05], wspace=0.30)

# ── (a) the ideal, shown as (ℓ,k) panels stacked by n ────────────
ax = fig.add_subplot(gs[0])
# lay shells side by side: x = l + 5*(n-1)/1.0 offset
xoff = {n: n*5.6 for n in range(1,8)}
for (n,l,k) in L:
    x = xoff[n] + l
    y = k
    filled = (n,l,k) in occ
    col = OCC if filled else EMP
    ax.add_patch(Rectangle((x-0.42, y-0.42), 0.84, 0.84,
                           facecolor=col, edgecolor='white', lw=0.35,
                           alpha=0.95 if filled else 0.75))
for m in maxel:
    n,l,k=m
    ax.add_patch(Rectangle((xoff[n]+l-0.46, k-0.46), 0.92, 0.92,
                           facecolor='none', edgecolor=FR, lw=1.9, zorder=6))
for c in nxt:
    n,l,k=c
    ax.add_patch(Rectangle((xoff[n]+l-0.46, k-0.46), 0.92, 0.92,
                           facecolor='none', edgecolor=NX, lw=1.4,
                           linestyle=(0,(2.5,1.5)), zorder=6))
for n in range(1,8):
    ax.text(xoff[n]+1.6, -1.5, f'n={n}', fontsize=8, ha='center', color='#444')
ax.set_xlim(xoff[1]-1.2, xoff[7]+5.2)
ax.set_ylim(-2.6, 19.4)
ax.set_ylabel('k  (occupancy)', fontsize=9)
ax.set_xticks([])
ax.set_title('(a)  the 118 occupied cells form a down-set of Λ', fontsize=10, loc='left')
ax.spines[['top','right','bottom']].set_visible(False)
ax.tick_params(labelsize=8)
hl=[Patch(facecolor=OCC, label='occupied (118)'),
    Patch(facecolor=EMP, label='unoccupied (92)'),
    Line2D([],[],color=FR, lw=1.9, label='maximal / frontier (3)'),
    Line2D([],[],color=NX, lw=1.4, ls=(0,(2.5,1.5)), label='covering cells (5)')]
ax.legend(handles=hl, frameon=False, fontsize=7.6, ncol=2,
          loc='upper left', bbox_to_anchor=(0.005,1.005))

# ── (b) the down-set property, tested ───────────────────────────
ax = fig.add_subplot(gs[1])
# for each occupied cell count how many admissible cells lie below it, and how many are occupied
below_tot=[]; below_occ=[]
for x in sorted(occ):
    b=[y for y in L if leq(y,x)]
    below_tot.append(len(b)); below_occ.append(sum(1 for y in b if y in occ))
ax.scatter(below_tot, below_occ, s=16, color=OCC, alpha=0.55, edgecolors='none', zorder=3)
lim=[0,max(below_tot)+6]
ax.plot(lim, lim, color='#b02a4a', lw=1.3, ls='--', zorder=2)
ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel('admissible cells below x', fontsize=9)
ax.set_ylabel('of those, cells that are occupied', fontsize=9)
ax.set_title('(b)  every cell below an element is an element', fontsize=10, loc='left')
ax.grid(alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.05, 0.90, 'all 118 points lie exactly on\nthe diagonal — 0 violations',
        transform=ax.transAxes, fontsize=8.2, color='#b02a4a', va='top',
        bbox=dict(fc='white', ec='#ddd', lw=0.6, pad=4))

# ── (c) the frontier and where growth can occur ─────────────────
ax = fig.add_subplot(gs[2])
ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
rows=[('Lr',103,(5,3,14),[(5,4,14),(6,3,14)]),
      ('Cn',112,(6,2,10),[(6,3,10),(7,2,10)]),
      ('Og',118,(7,1,6), [(7,2,6)])]
y=0.86
for sym,Z,cell,covs in rows:
    ax.add_patch(Rectangle((0.03,y-0.075),0.30,0.13, facecolor=FR, alpha=0.13,
                           edgecolor=FR, lw=1.2))
    ax.text(0.18, y, f'{sym}  (Z={Z})', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#08532a')
    ax.text(0.18, y-0.052, f'{cell}', ha='center', va='center',
            fontsize=7.4, color='#333')
    for j,c in enumerate(covs):
        yy = y + (0.055 if len(covs)>1 and j==0 else (-0.055 if len(covs)>1 else 0))
        ax.add_patch(FancyArrowPatch((0.345, y), (0.60, yy),
                     arrowstyle='-|>', mutation_scale=9,
                     color=NX, lw=1.0, connectionstyle='arc3,rad=0.12'))
        ax.add_patch(Rectangle((0.61,yy-0.037),0.31,0.074, facecolor=NX, alpha=0.12,
                               edgecolor=NX, lw=1.0, linestyle=(0,(2.5,1.5))))
        ax.text(0.765, yy, f'{c}', ha='center', va='center', fontsize=7.6, color='#7a5200')
    y -= 0.30
ax.text(0.03, 0.055, 'Any new element must occupy a cell covering\none of the three maximal cells: five addresses.',
        fontsize=7.8, color='#444', style='italic')
ax.text(0.03, -0.02, 'This constrains configuration space only — not\nnuclear stability, cross-section, or half-life.',
        fontsize=7.4, color='#8a4a4a', style='italic')
ax.set_title('(c)  the discovery frontier', fontsize=10, loc='left')

plt.savefig('/home/claude/fig9_ideal.png', bbox_inches='tight')
print('ok')
