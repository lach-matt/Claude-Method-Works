import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle, Patch, FancyArrowPatch
from matplotlib.lines import Line2D
import eldata as ed

plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'axes.linewidth':0.7,'savefig.dpi':200,'figure.facecolor':'white'})

L=set((n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1))
def leq(a,b): return all(x<=y for x,y in zip(a,b))

A=[(7,2,6),(5,4,6),(5,2,8)]        # minimals
B=[(5,4,8),(7,2,8),(7,4,6)]        # maximals

MIN='#2c5f9e'; MAX='#b02a4a'; OK='#0a7a3a'; GR='#c9c4bc'

fig=plt.figure(figsize=(12.6,4.15))
gs=fig.add_gridspec(1,3,width_ratios=[1.05,1.10,1.15],wspace=0.28)

# ── (a) the S3 bipartite incidence ──────────────────────────────
ax=fig.add_subplot(gs[0])
ax.set_xlim(0,1); ax.set_ylim(-0.12,1.05); ax.axis('off')
ya=[0.80,0.52,0.24]
for i,(a,y) in enumerate(zip(A,ya)):
    ax.add_patch(Rectangle((0.03,y-0.07),0.28,0.14,facecolor=MIN,alpha=0.15,
                           edgecolor=MIN,lw=1.2))
    ax.text(0.17,y+0.015,f'a{i+1}',ha='center',fontsize=9.5,fontweight='bold',color=MIN)
    ax.text(0.17,y-0.042,f'{a}',ha='center',fontsize=7.4,color='#333')
for j,(b,y) in enumerate(zip(B,ya)):
    ax.add_patch(Rectangle((0.69,y-0.07),0.28,0.14,facecolor=MAX,alpha=0.15,
                           edgecolor=MAX,lw=1.2))
    ax.text(0.83,y+0.015,f'b{j+1}',ha='center',fontsize=9.5,fontweight='bold',color=MAX)
    ax.text(0.83,y-0.042,f'{b}',ha='center',fontsize=7.4,color='#333')
for i in range(3):
    for j in range(3):
        if leq(A[i],B[j]):
            ax.add_patch(FancyArrowPatch((0.325,ya[i]),(0.685,ya[j]),
                         arrowstyle='-',color=OK,lw=1.25,alpha=0.85,
                         connectionstyle='arc3,rad=0.0'))
ax.text(0.5,0.98,'aᵢ ≤ bⱼ  ⟺  i ≠ j',ha='center',fontsize=9.5,style='italic',color=OK)
ax.text(0.5,0.045,'the standard example S₃',ha='center',fontsize=8.6,color='#444')
ax.text(0.5,-0.03,'its presence forces dim ≥ 3',ha='center',fontsize=8.0,
        color=OK,style='italic')
ax.set_title('(a)  a 3-dimensional witness in Λ',fontsize=10,loc='left')

# ── (b) incidence matrix ────────────────────────────────────────
ax=fig.add_subplot(gs[1])
M=np.array([[1 if leq(a,b) else 0 for b in B] for a in A])
ax.imshow(M,cmap='Greens',vmin=-0.35,vmax=1.4)
for i in range(3):
    for j in range(3):
        ax.text(j,i,'≤' if M[i,j] else '∥',ha='center',va='center',
                fontsize=15,color='white' if M[i,j] else '#7a7a7a',
                fontweight='bold')
ax.set_xticks(range(3)); ax.set_xticklabels([f'b{j+1}\n{B[j]}' for j in range(3)],fontsize=7.4)
ax.set_yticks(range(3)); ax.set_yticklabels([f'a{i+1}\n{A[i]}' for i in range(3)],fontsize=7.4)
ax.set_title('(b)  incidence: off-diagonal comparable',fontsize=10,loc='left')
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(length=0)
ax.text(0.5,-0.30,'Each minimal lies below exactly two of the three maximals.\n'
                  'No two linear orders can reproduce this pattern.',
        transform=ax.transAxes,ha='center',fontsize=7.8,color='#555',style='italic')

# ── (c) the witness located in Λ ────────────────────────────────
ax=fig.add_subplot(gs[2],projection='3d')
for (n,l,k) in L:
    ax.scatter(n,l,k,s=5,c=GR,alpha=0.30,edgecolors='none',depthshade=False)
for a in A:
    ax.scatter(*a,s=64,c=MIN,edgecolors='white',lw=0.7,depthshade=False,zorder=6)
for b in B:
    ax.scatter(*b,s=64,c=MAX,edgecolors='white',lw=0.7,depthshade=False,zorder=6)
for i in range(3):
    for j in range(3):
        if leq(A[i],B[j]):
            ax.plot([A[i][0],B[j][0]],[A[i][1],B[j][1]],[A[i][2],B[j][2]],
                    color=OK,lw=1.0,alpha=0.75)
ax.set_xlabel('n',fontsize=8.5,labelpad=-4)
ax.set_ylabel('ℓ',fontsize=8.5,labelpad=-4)
ax.set_zlabel('k',fontsize=8.5,labelpad=-4)
ax.set_xticks([1,3,5,7]); ax.set_yticks([0,2,4]); ax.set_zticks([1,6,12,18])
ax.tick_params(labelsize=7)
ax.view_init(elev=17,azim=-58)
ax.set_title('(c)  the witness inside the lattice',fontsize=10,loc='left')
try: ax.set_box_aspect((1.3,1,1.15))
except Exception: pass
hl=[Line2D([],[],marker='o',ls='',ms=6,mfc=MIN,mec='white',label='minimals aᵢ'),
    Line2D([],[],marker='o',ls='',ms=6,mfc=MAX,mec='white',label='maximals bⱼ'),
    Line2D([],[],marker='o',ls='',ms=4,mfc=GR,mec='none',label='other cells of Λ')]
ax.legend(handles=hl,frameon=False,fontsize=7.2,loc='upper left',
          bbox_to_anchor=(-0.06,0.99))

plt.savefig('/home/claude/fig07_dimension.png',bbox_inches='tight')
print('ok')
