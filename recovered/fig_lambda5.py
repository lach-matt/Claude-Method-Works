import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
from collections import Counter
from itertools import product
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})
CAP=lambda l:2*(2*l+1)
L3=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
L5=[(n,l,k,q,e) for (n,l,k) in L3 for q in range(0,k+1) for e in range(n,10)]
occ=set(ed.E.values())

BASE='#2c5f9e'; QC='#c1751a'; EC='#1f6f3f'; GR='#c9c4bc'; RED='#a8203c'

fig=plt.figure(figsize=(13.2,8.6))
gs=fig.add_gridspec(2,3,height_ratios=[1.0,1.05],width_ratios=[1.05,1.15,1.0],
                    hspace=0.34,wspace=0.30)

# ── (a) the nesting ──────────────────────────────────────────────────
ax=fig.add_subplot(gs[0,0]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
tiers=[('Λ₅  (n, ℓ, k, q, e)',7136,'#e8eef6',5,BASE),
       ('Λ_qe slice at e = n',1565,'#f3e4d0',4,QC),
       ('Λ_q slice, e = n',1565,'#e0efe4',4,EC),
       ('Λ   q = 0, e = n',210,'#ffffff',3,'#333333')]
y=0.86
for lab,n,fc,d,col in tiers:
    ax.add_patch(Rectangle((0.06,y-0.16),0.88,0.19,facecolor=fc,edgecolor=col,lw=1.4))
    ax.text(0.11,y-0.03,lab,fontsize=9.6,fontweight='bold',color=col,va='center')
    ax.text(0.90,y-0.03,f'{n:,} cells\ndim {d}',fontsize=8.2,ha='right',va='center',color='#444')
    y-=0.225
ax.text(0.5,0.05,'each level is a slice of the one above',ha='center',
        fontsize=8.4,style='italic',color='#555')
ax.set_title('(a)  the lattice and its slices',fontsize=10.5,loc='left')

# ── (b) the 5-cube ───────────────────────────────────────────────────
ax=fig.add_subplot(gs[0,1]); ax.axis('off')
ax.set_xlim(-0.6,6.4); ax.set_ylim(-0.6,4.6)
base=(2,0,1,0,3)
# project 5-cube: coords (n,l,k,q,e) -> 2D via two 2D-cube layouts
def pos(m):
    n_,l_,k_,q_,e_=m
    x = n_*0.9 + k_*2.6 + q_*0.42
    y = l_*0.9 + e_*2.2 + q_*0.30
    return x,y
pts={}
for m in product([0,1],repeat=5):
    pts[m]=pos(m)
for m in product([0,1],repeat=5):
    for i in range(5):
        if m[i]==0:
            m2=list(m); m2[i]=1; m2=tuple(m2)
            col=[BASE,BASE,BASE,QC,EC][i]
            ax.plot([pts[m][0],pts[m2][0]],[pts[m][1],pts[m2][1]],
                    color=col,lw=1.0,alpha=0.55,zorder=1)
for m,(x,y) in pts.items():
    ax.scatter([x],[y],s=44,color='white',edgecolors='#333',lw=0.9,zorder=3)
ax.scatter(*pts[(0,0,0,0,0)],s=90,color=RED,edgecolors='white',lw=1.2,zorder=5)
ax.annotate('base (2, 0, 1, 0, 3)\n2s¹, neutral, e→3',pts[(0,0,0,0,0)],
            xytext=(-14,-30),textcoords='offset points',fontsize=7.8,color=RED,
            ha='left',bbox=dict(fc='white',ec=RED,lw=0.7,pad=2))
for lab,col,dx,dy in [('n, ℓ, k',BASE,0.2,4.3),('q',QC,3.4,4.3),('e',EC,4.6,4.3)]:
    ax.plot([dx,dx+0.5],[dy,dy],color=col,lw=2.0)
    ax.text(dx+0.6,dy,lab,fontsize=8.4,color=col,va='center')
ax.set_title('(b)  a 5-cube: 32 admissible cells, all physical',fontsize=10.5,loc='left')

# ── (c) equation ─────────────────────────────────────────────────────
ax=fig.add_subplot(gs[0,2]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.add_patch(Rectangle((0.02,0.14),0.96,0.74,facecolor='#f7f6f4',edgecolor='#999',lw=1.0))
ax.text(0.06,0.80,'Λ₅  =  { (n, ℓ, k, q, e) ∈ ℤ⁵ :',fontsize=10.5,fontweight='bold')
rows=[('1 ≤ n ≤ N','shell',BASE),
      ('0 ≤ ℓ ≤ min(n−1, L)','subshell — bounded by n',BASE),
      ('1 ≤ k ≤ 2(2ℓ+1)','occupancy — bounded by ℓ',BASE),
      ('0 ≤ q ≤ k','ionic charge — bounded by k',QC),
      ('n ≤ e ≤ E','excitation target — bounded by n',EC)]
yy=0.68
for eq,note,col in rows:
    ax.text(0.10,yy,eq,fontsize=9.4,family='monospace',color=col)
    ax.text(0.10,yy-0.055,note,fontsize=7.4,style='italic',color='#666')
    yy-=0.125
ax.text(0.06,0.175,'}',fontsize=10.5,fontweight='bold')
ax.text(0.5,0.055,'every bound monotone in ONE coordinate,\nevery floor constant or rising',
        ha='center',fontsize=8.0,style='italic',color='#444')
ax.set_title('(c)  the defining constraints',fontsize=10.5,loc='left')

# ── (d) slice populations ────────────────────────────────────────────
ax=fig.add_subplot(gs[1,0])
qc=Counter(c[3] for c in L5)
ks=sorted(qc)[:12]
ax.bar(ks,[qc[k] for k in ks],color=QC,edgecolor='#8a5410',lw=0.5)
ax.set_xlabel('ionic charge  q',fontsize=9); ax.set_ylabel('cells',fontsize=9)
ax.set_title('(d)  population by charge',fontsize=10.5,loc='left')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.96,0.92,'q = 0 is the\nneutral slice',transform=ax.transAxes,ha='right',
        va='top',fontsize=7.6,color='#555')

# ── (e) excitation slices ────────────────────────────────────────────
ax=fig.add_subplot(gs[1,1])
ec=Counter(c[4] for c in L5)
ks=sorted(ec)
ax.bar(ks,[ec[k] for k in ks],color=EC,edgecolor='#12482a',lw=0.5)
ax.set_xlabel('excitation target shell  e',fontsize=9); ax.set_ylabel('cells',fontsize=9)
ax.set_title('(e)  population by excitation target',fontsize=10.5,loc='left')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.04,0.92,'saturates at e ≥ 7:\nevery cell with n ≤ 7\nadmits every target',
        transform=ax.transAxes,fontsize=7.6,va='top',color='#555')

# ── (f) the elements in the base slice ───────────────────────────────
ax=fig.add_subplot(gs[1,2])
for (n,l,k) in L3:
    filled=(n,l,k) in occ
    ax.scatter([l+ (k-1)*0.055],[n],s=13 if filled else 7,
               color=BASE if filled else GR,alpha=0.9 if filled else 0.5,
               edgecolors='none')
ax.set_xlabel('ℓ  (with k spread within each block)',fontsize=8.6)
ax.set_ylabel('n',fontsize=9)
ax.set_title('(f)  the 118 elements, q = 0 and e = n',fontsize=10.5,loc='left')
ax.set_yticks(range(1,8)); ax.invert_yaxis()
ax.grid(alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.97,0.06,'blue = occupied\ngrey = reserved',transform=ax.transAxes,
        ha='right',fontsize=7.6,color='#555')

plt.savefig('/home/claude/fig_lambda5.png',bbox_inches='tight')
print('ok')
