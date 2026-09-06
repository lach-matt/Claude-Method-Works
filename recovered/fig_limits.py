import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Patch
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})
OK='#1f6f3f'; BAD='#a8203c'; GR='#c9c4bc'; BL='#2c5f9e'

fig=plt.figure(figsize=(12.6,4.05))
gs=fig.add_gridspec(1,3,width_ratios=[1.0,1.05,1.15],wspace=0.32)

# ── (a) every axis is a count ────────────────────────────────────
ax=fig.add_subplot(gs[0]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
rows=[('n','radial nodes + 1','count'),
      ('ℓ','angular nodes','count'),
      ('k','electrons in subshell','count')]
y=0.78
for sym,what,kind in rows:
    ax.add_patch(Rectangle((0.05,y-0.09),0.90,0.17,facecolor=BL,alpha=0.10,
                           edgecolor=BL,lw=1.1))
    ax.text(0.12,y,sym,fontsize=15,fontweight='bold',color=BL,va='center',ha='center')
    ax.text(0.24,y+0.030,what,fontsize=9,color='#222',va='center')
    ax.text(0.24,y-0.038,f'dimension: {kind}',fontsize=7.8,color='#666',va='center',style='italic')
    y-=0.24
ax.text(0.5,0.16,'Λ ⊆ ℕ³',ha='center',fontsize=17,fontweight='bold',color=BAD)
ax.text(0.5,0.055,'every quantity built from the coordinates\nis a pure number',
        ha='center',fontsize=8.4,style='italic',color='#444')
ax.set_title('(a)  the axes are counts, not measures',fontsize=10,loc='left')

# ── (b) the metric-axis dilemma ──────────────────────────────────
ax=fig.add_subplot(gs[1]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.text(0.5,0.93,'add a metric fourth axis  E ?',ha='center',fontsize=10.5,
        fontweight='bold',color='#222')
# two branches
ax.add_patch(FancyArrowPatch((0.5,0.87),(0.24,0.70),arrowstyle='-|>',
             mutation_scale=11,color='#666',lw=1.2))
ax.add_patch(FancyArrowPatch((0.5,0.87),(0.76,0.70),arrowstyle='-|>',
             mutation_scale=11,color='#666',lw=1.2))
ax.add_patch(Rectangle((0.02,0.40),0.44,0.28,facecolor=GR,alpha=0.30,
                       edgecolor='#8a8378',lw=1.0))
ax.text(0.24,0.615,'E independent\nof (n,ℓ,k)',ha='center',fontsize=8.8,fontweight='bold')
ax.text(0.24,0.485,'carries no information\nabout the lattice —\nthe axis is decorative',
        ha='center',fontsize=7.8,color='#444')
ax.add_patch(Rectangle((0.54,0.40),0.44,0.28,facecolor=BAD,alpha=0.12,
                       edgecolor=BAD,lw=1.0))
ax.text(0.76,0.615,'E a function\nof (n,ℓ,k)',ha='center',fontsize=8.8,
        fontweight='bold',color=BAD)
ax.text(0.76,0.485,'the set becomes a\nfunctional graph —\nclosure is destroyed',
        ha='center',fontsize=7.8,color=BAD)
ax.add_patch(Rectangle((0.14,0.14),0.72,0.17,facecolor='white',
                       edgecolor=BAD,lw=1.3))
ax.text(0.5,0.225,'14,293 join failures   ·   14,293 meet failures',
        ha='center',fontsize=9,color=BAD,fontweight='bold')
ax.text(0.5,0.055,'informative ⟹ dependent ⟹ not a sublattice',
        ha='center',fontsize=8.4,style='italic',color='#444')
ax.set_title('(b)  no metric coordinate can be added',fontsize=10,loc='left')

# ── (c) applications attempted ───────────────────────────────────
ax=fig.add_subplot(gs[2])
apps=[('hydride formation\nenthalpy',0.514,0.790,'lost to Pettifor'),
      ('anomalous ground\nstates',0.0,None,'no enrichment'),
      ('exchange-energy\nlabelling',0.089,None,'AUC ≈ 0.5'),
      ('ionisation energy',0.42,None,'via imported 1/n²'),
      ('electronegativity',0.12,None,'essentially none')]
ys=np.arange(len(apps))[::-1]
for i,(nm,v,base,note) in enumerate(apps):
    yy=ys[i]
    col=BL if v>0.3 else GR
    ax.barh(yy,max(v,0.005),color=col,edgecolor='#333',lw=0.5,height=0.55)
    if base is not None:
        ax.plot([base,base],[yy-0.32,yy+0.32],color=BAD,lw=2.0)
        ax.text(base+0.015,yy+0.30,'Pettifor',fontsize=7.2,color=BAD)
    ax.text(-0.02,yy,nm,ha='right',va='center',fontsize=8.0)
    ax.text(max(v,0.02)+0.02,yy-0.02,note,va='center',fontsize=7.4,color='#555')
ax.set_yticks([]); ax.set_xlim(0,1.06)
ax.set_xlabel('cross-validated R²  (or AUC−0.5 scaled)',fontsize=8.6)
ax.set_title('(c)  every predictive application attempted',fontsize=10,loc='left')
ax.grid(axis='x',alpha=0.2,lw=0.5); ax.set_axisbelow(True)
ax.spines[['top','right','left']].set_visible(False)
ax.text(0.99,0.03,'no application predicts a measured\nquantity competitively',
        transform=ax.transAxes,ha='right',fontsize=7.6,style='italic',color=BAD)

plt.savefig('/home/claude/figC_limits.png',bbox_inches='tight')
print('ok')
