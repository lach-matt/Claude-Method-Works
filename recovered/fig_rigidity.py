import numpy as np, itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from collections import Counter
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})
CAP=lambda l: 2*(2*l+1)
occ=set(ed.E.values())
def leq(a,b): return all(x<=y for x,y in zip(a,b))

OK='#1f6f3f'; BAD='#a8203c'; GR='#c9c4bc'; BL='#2c5f9e'

fig=plt.figure(figsize=(12.6,4.05))
gs=fig.add_gridspec(1,3,width_ratios=[1.0,1.22,1.05],wspace=0.30)

# ── (a) ℓ-orderings: 1 of 120 ────────────────────────────────────
ax=fig.add_subplot(gs[0])
def test_l(perm):
    cap={i:CAP(perm[i]) for i in range(5)}
    Lx=[(n,i,k) for n in range(1,8) for i in range(0,min(n,5)) for k in range(1,cap[i]+1)]
    pos={perm[i]:i for i in range(5)}
    Ox=set()
    for (n,l,k) in occ:
        i=pos[l]
        if i>n-1 or k>cap[i]: return 'inadmissible'
        Ox.add((n,i,k))
    return 'ok' if not any(leq(y,x) and y not in Ox for x in Ox for y in Lx) else 'not-downset'
res=Counter()
good=[]
for p in itertools.permutations(range(5)):
    r=test_l(p); res[r]+=1
    if r=='ok': good.append(p)
labels=['admits elements\nAND down-set','admits but\nnot a down-set','cannot admit\nthe elements']
vals=[res['ok'],res['not-downset'],res['inadmissible']]
cols=[OK,'#d8a13a',GR]
b=ax.bar(range(3),vals,color=cols,edgecolor='#333',lw=0.6,width=0.62)
for i,v in enumerate(vals):
    ax.text(i,v+2.5,str(v),ha='center',fontsize=10,fontweight='bold')
ax.set_xticks(range(3)); ax.set_xticklabels(labels,fontsize=7.8)
ax.set_ylabel('orderings of {s,p,d,f,g}',fontsize=9)
ax.set_ylim(0,132)
ax.set_title('(a)  the ℓ-axis order is forced',fontsize=10,loc='left')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
nm=' < '.join('spdfg'[good[0][i]] for i in range(5))
ax.text(0.5,0.80,f'the unique survivor:\n{nm}',transform=ax.transAxes,
        ha='center',fontsize=9,color=OK,fontweight='bold',
        bbox=dict(fc='white',ec=OK,lw=0.9,pad=4))

# ── (b) shear family ─────────────────────────────────────────────
ax=fig.add_subplot(gs[1])
Lbig=[(n,l,k) for n in range(1,40) for l in range(0,n) for k in range(1,CAP(l)+1)]
PER=[2,2,8,8,18,18,32,32]
def seqof(a,b,c):
    cnt=Counter(a*n+b*l+c*k for (n,l,k) in Lbig)
    ks=sorted(cnt); return [cnt[x] for x in ks[:8]]
combos=[(a,b,c) for a in range(3) for b in range(3) for c in range(3) if (a,b,c)!=(0,0,0)]
match=[]; other=[]
for t in combos:
    (match if seqof(*t)==PER else other).append(t)
ax.scatter([t[0]+np.random.uniform(-.11,.11) for t in other],
           [t[1]+np.random.uniform(-.11,.11) for t in other],
           s=[26+34*t[2] for t in other],color=GR,edgecolors='#8a8378',lw=0.5,zorder=2)
ax.scatter([t[0] for t in match],[t[1] for t in match],
           s=[40+46*t[2] for t in match],color=OK,edgecolors='white',lw=1.0,zorder=5)
for t in match:
    ax.annotate(f'({t[0]},{t[1]},{t[2]})',(t[0],t[1]),xytext=(9,7),
                textcoords='offset points',fontsize=8.4,color=OK,fontweight='bold')
ax.set_xlabel('coefficient a  (on n)',fontsize=9)
ax.set_ylabel('coefficient b  (on ℓ)',fontsize=9)
ax.set_xticks(range(3)); ax.set_yticks(range(3))
ax.set_xlim(-0.5,2.7); ax.set_ylim(-0.5,2.6)
ax.set_title('(b)  which shears an+bℓ+ck give the period lengths?',fontsize=10,loc='left')
ax.grid(alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.97,0.90,'marker size ∝ c\ngreen = reproduces\n2,2,8,8,18,18,32,32',
        transform=ax.transAxes,ha='right',va='top',fontsize=7.8,color='#444',
        bbox=dict(fc='white',ec='#ccc',lw=0.6,pad=3))

# ── (c) the n-axis reflection is not a lattice symmetry ──────────
ax=fig.add_subplot(gs[2])
prof={n: len(set(l for (nn,l,k) in occ if nn==n)) for n in range(1,8)}
adm={n: min(n,5) for n in range(1,8)}
xs=np.arange(1,8); w=0.38
ax.bar(xs-w/2,[adm[n] for n in xs],w,color=GR,edgecolor='#8a8378',lw=0.5,label='columns admitted')
ax.bar(xs+w/2,[prof[n] for n in xs],w,color=BL,edgecolor='#1c3f6e',lw=0.5,label='columns occupied')
for n in xs:
    if adm[n]!=prof[n]:
        ax.annotate('',xy=(n+w/2,prof[n]),xytext=(n+w/2,adm[n]),
                    arrowprops=dict(arrowstyle='<->',color=BAD,lw=1.1))
        ax.text(n+w/2+0.13,(prof[n]+adm[n])/2,f'−{adm[n]-prof[n]}',fontsize=8,color=BAD)
for a,b in [(2,7),(3,6),(4,5)]:
    ax.plot([a+w/2,b+w/2],[prof[a]+0.30,prof[b]+0.30],color=BAD,lw=1.0,ls=(0,(3,2)))
ax.set_xticks(xs); ax.set_xlabel('n  (shell)',fontsize=9)
ax.set_ylabel('(n,ℓ) columns',fontsize=9)
ax.set_ylim(0,6.6)
ax.set_title('(c)  equal occupied-column counts pair shells',fontsize=10,loc='left')
ax.legend(frameon=False,fontsize=7.8,loc='upper left')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.5,0.045,'shells 2↔7, 3↔6, 4↔5 have identical profiles —\n'
                  'an artifact of truncation at Z=118, not a symmetry of Λ',
        transform=ax.transAxes,ha='center',fontsize=7.4,style='italic',color=BAD)

plt.savefig('/home/claude/figB_rigidity.png',bbox_inches='tight')
print('ok')
