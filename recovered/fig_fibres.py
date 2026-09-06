import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch, FancyArrowPatch
from matplotlib.lines import Line2D
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

zs=sorted(ed.E)
fib={}
for z in zs:
    n,l,k=ed.E[z]; fib.setdefault((l,k),[]).append(z)

FIB='#2c5f9e'; HE='#0a7a3a'; KA='#b02a4a'; GR='#d6d1c8'

fig=plt.figure(figsize=(12.6,4.15))
gs=fig.add_gridspec(1,3,width_ratios=[1.22,1.00,1.05],wspace=0.30)

# ── (a) fibres: fix (l,k), vary n ───────────────────────────────
ax=fig.add_subplot(gs[0])
show=[(0,1),(0,2),(1,1),(1,4),(1,6),(2,5),(3,7)]
ylab=[]
for i,(l,k) in enumerate(show):
    mem=sorted(fib.get((l,k),[]))
    ns=[ed.E[z][0] for z in mem]
    col = HE if (l,k)==(0,2) else FIB
    ax.plot(ns,[i]*len(ns),'-',color=col,lw=1.0,alpha=0.55,zorder=2)
    ax.scatter(ns,[i]*len(ns),s=46,color=col,edgecolors='white',lw=0.7,zorder=4)
    for z,n in zip(mem,ns):
        ax.annotate(ed.SYM[z],(n,i),xytext=(0,7),textcoords='offset points',
                    ha='center',fontsize=6.6,color='#333')
    ylab.append(f"ℓ={l}, k={k}")
# highlight He
ax.scatter([1],[1],s=150,facecolors='none',edgecolors=HE,lw=2.0,zorder=6)
ax.annotate('He sits with the s-block,\nnot the noble gases',
            xy=(1,1),xytext=(2.05,1.62),fontsize=7.6,color=HE,style='italic',
            arrowprops=dict(arrowstyle='->',color=HE,lw=1.1))
ax.set_yticks(range(len(show))); ax.set_yticklabels(ylab,fontsize=7.8)
ax.set_xticks(range(1,8)); ax.tick_params(labelsize=8)
ax.set_xlabel('n  (shell)',fontsize=9)
ax.set_xlim(0.4,7.7); ax.set_ylim(-0.7,len(show)-0.2)
ax.set_title('(a)  a chemical group is a fibre of Λ',fontsize=10,loc='left')
ax.grid(axis='x',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)

# ── (b) kainosymmetric diagonal ─────────────────────────────────
ax=fig.add_subplot(gs[1])
for n in range(1,8):
    for l in range(0,min(n,5)):
        kain = (l==n-1)
        ax.add_patch(Rectangle((l-0.42,n-0.42),0.84,0.84,
                               facecolor=KA if kain else GR,
                               alpha=0.85 if kain else 0.65,
                               edgecolor='white',lw=0.8))
        if kain:
            ax.text(l,n,f"{n}{'spdfg'[l]}",ha='center',va='center',
                    fontsize=7.4,color='white',fontweight='bold')
xs=np.array([-0.42,4.42])
ax.plot(xs,xs+1,color=KA,lw=1.3,ls=(0,(4,2)),zorder=5)
ax.set_xlim(-0.8,4.8); ax.set_ylim(0.3,7.7); ax.invert_yaxis()
ax.set_xticks(range(5)); ax.set_xticklabels(['s','p','d','f','g'],fontsize=9)
ax.set_yticks(range(1,8)); ax.tick_params(labelsize=8)
ax.set_xlabel('ℓ',fontsize=9.5); ax.set_ylabel('n',fontsize=9.5)
ax.set_title('(b)  kainosymmetry lies on ℓ = n−1',fontsize=10,loc='left')
ax.text(2.55,6.4,'the boundary where\nℓ ≤ n−1 is tight',fontsize=7.8,
        color=KA,style='italic',ha='center')

# ── (c) parity balance ──────────────────────────────────────────
ax=fig.add_subplot(gs[2])
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
ev=sum(1 for c in L if sum(c)%2==0); od=len(L)-ev
oe=sum(1 for c in occ if sum(c)%2==0); oo=len(occ)-oe
x=np.arange(2); w=0.36
ax.bar(x-w/2,[ev,oe],w,color='#4a7c9e',edgecolor='#2a4c6e',lw=0.6,label='even rank')
ax.bar(x+w/2,[od,oo],w,color='#c9a227',edgecolor='#8a6f17',lw=0.6,label='odd rank')
for xi,(a,b) in zip(x,[(ev,od),(oe,oo)]):
    ax.text(xi-w/2,a+2.5,str(a),ha='center',fontsize=8.6,fontweight='bold')
    ax.text(xi+w/2,b+2.5,str(b),ha='center',fontsize=8.6,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(['all of Λ\n(210 cells)','occupied\n(118 cells)'],fontsize=8.4)
ax.set_ylabel('cells',fontsize=9); ax.set_ylim(0,128)
ax.set_title('(c)  parity balance, forced by spin',fontsize=10,loc='left')
ax.legend(frameon=False,fontsize=8,loc='upper right')
ax.grid(axis='y',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
ax.text(0.5,0.55,'every column capacity 2(2ℓ+1)\nis even, so F(−1) = 0 exactly',
        transform=ax.transAxes,fontsize=7.8,ha='center',color='#555',style='italic')

plt.savefig('/home/claude/fig11_fibres.png',bbox_inches='tight')
print('ok')
