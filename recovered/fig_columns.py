import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
from collections import Counter
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
cap={(n,l):2*(2*l+1) for (n,l) in cols}
occ=set(ed.E[z] for z in ed.E)
h={c: max([k for (n,l,k) in occ if (n,l)==c], default=0) for c in cols}

def leq(a,b): return a[0]<=b[0] and a[1]<=b[1]
order=sorted(cols)
allds=[]
def enum(i, ch):
    if i==len(order): allds.append(frozenset(ch)); return
    c=order[i]
    enum(i+1, ch)
    if all((d in ch) for d in cols if leq(d,c) and d!=c):
        enum(i+1, ch|{c})
enum(0, frozenset())
real=frozenset(c for c in cols if h[c]>0)
cells=[sum(cap[c] for c in d) for d in allds]

SAT='#2c5f9e'; EMP='#d6d1c8'; RE='#0a7a3a'

fig=plt.figure(figsize=(12.6,4.05))
gs=fig.add_gridspec(1,3,width_ratios=[1.15,0.95,1.15],wspace=0.30)

# ── (a) column heights vs capacity ───────────────────────────────
ax=fig.add_subplot(gs[0])
xs=np.arange(len(cols))
capv=[cap[c] for c in cols]; hv=[h[c] for c in cols]
ax.bar(xs, capv, color=EMP, edgecolor='#9c968c', lw=0.5, width=0.78, label='capacity 2(2ℓ+1)')
ax.bar(xs, hv, color=SAT, edgecolor='#1c3f6e', lw=0.5, width=0.78, label='cells occupied')
for i,c in enumerate(cols):
    if h[c]==cap[c]:
        ax.plot([i],[cap[c]+0.7],marker='v',ms=3.4,color=SAT)
ax.set_xticks(xs)
ax.set_xticklabels([f"{n}{'spdfg'[l]}" for (n,l) in cols], fontsize=6.0, rotation=90)
ax.set_ylabel('cells in column', fontsize=9)
ax.set_ylim(0,20.5)
ax.set_title('(a)  every column is full or empty', fontsize=10, loc='left')
ax.legend(frameon=False, fontsize=7.6, loc='upper left')
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.98,0.62,'19 saturated\n6 empty\n0 partial', transform=ax.transAxes,
        fontsize=8.4, ha='right', va='top', color=SAT, fontweight='bold',
        bbox=dict(fc='white', ec='#ccc', lw=0.6, pad=4))

# ── (b) the column poset, realised down-set marked ───────────────
ax=fig.add_subplot(gs[1])
for (n,l) in cols:
    filled = (n,l) in real
    ax.add_patch(Rectangle((l-0.40, n-0.40), 0.80, 0.80,
                           facecolor=SAT if filled else EMP,
                           edgecolor='white', lw=0.9))
    ax.text(l, n, f"{cap[(n,l)]}", ha='center', va='center', fontsize=7.2,
            color='white' if filled else '#6a6459', fontweight='bold')
# frontier of the column down-set
maxcols=[c for c in real if not any(leq(c,d) and c!=d for d in real)]
for c in maxcols:
    ax.add_patch(Rectangle((c[1]-0.45, c[0]-0.45), 0.90, 0.90,
                           facecolor='none', edgecolor=RE, lw=1.9, zorder=6))
ax.set_xlim(-0.75,4.75); ax.set_ylim(0.3,7.7)
ax.invert_yaxis()
ax.set_xticks(range(5)); ax.set_xticklabels(['s','p','d','f','g'], fontsize=9)
ax.set_yticks(range(1,8)); ax.tick_params(labelsize=8)
ax.set_xlabel('ℓ', fontsize=9.5); ax.set_ylabel('n', fontsize=9.5)
ax.set_title('(b)  the column poset', fontsize=10, loc='left')
hl=[Patch(facecolor=SAT,label='filled column'),Patch(facecolor=EMP,label='empty column'),
    Line2D([],[],color=RE,lw=1.9,label='maximal filled')]
ax.legend(handles=hl, frameon=False, fontsize=7.4, loc='lower left',
          bbox_to_anchor=(-0.02,-0.02))

# ── (c) all 120 admissible configurations by size ────────────────
ax=fig.add_subplot(gs[2])
cnt=Counter(cells)
ks=sorted(cnt)
ax.bar(ks,[cnt[k] for k in ks],width=2.2,color=EMP,edgecolor='#9c968c',lw=0.5)
rc=sum(cap[c] for c in real)
ax.bar([rc],[cnt[rc]],width=2.2,color=RE,edgecolor='#08532a',lw=0.8)
ax.annotate(f'the periodic system\n{rc} cells  ·  79th pct',
            xy=(rc,cnt[rc]), xytext=(-96,26), textcoords='offset points',
            fontsize=8, color='#08532a', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RE, lw=1.1))
ax.set_xlabel('cells spanned by the configuration', fontsize=9)
ax.set_ylabel('number of configurations', fontsize=9)
ax.set_title('(c)  120 aufbau-consistent configurations', fontsize=10, loc='left')
ax.grid(axis='y', alpha=0.2, lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.03,0.93,f'total: {len(allds)} down-sets\nof the 25-column poset',
        transform=ax.transAxes, fontsize=7.8, va='top', color='#555')

plt.savefig('/home/claude/fig10_columns.png', bbox_inches='tight')
print('ok', len(allds), rc, cnt[rc])
