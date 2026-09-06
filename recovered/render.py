import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, json
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
                     'font.size':8,'figure.dpi':300,'savefig.dpi':300})

# --- Λ_G at a size that can be examined -------------------------------
A=[2,2,2,3,3,4,5,6,8,10]                       # A(u) non-decreasing in HEIGHT
S=[(u,a) for u,Au in enumerate(A) for a in range(Au)]
T=[(k,e) for k in range(3) for e in range(k+1)]
LG=[(u,a,k,e) for (u,a) in S for (k,e) in T]
print(f'|S|={len(S)}  |T|={len(T)}  |Λ_G|={len(LG)}')

X=np.array([c[0] for c in LG],float)
Y=np.array([c[1] for c in LG],float)
Z=np.array([c[2]+c[3]*0.26 for c in LG],float)   # dosage k, expressed e as sub-offset
Ecol=np.array([c[3] for c in LG])
CM={0:'#c9d6df',1:'#5b8ca8',2:'#8c2f39'}
COL=[CM[e] for e in Ecol]

cell={c:(c[0],c[1],c[2]+c[3]*0.26) for c in LG}
edges=[]
for (u,a,k,e) in LG:
    for d in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
        n=(u+d[0],a+d[1],k+d[2],e+d[3])
        if n in cell: edges.append((cell[(u,a,k,e)],cell[n]))
print(f'{len(edges)} covering edges')

def panel(ax,elev,azim,title,show_edges=True):
    if show_edges:
        for p,q in edges:
            ax.plot([p[0],q[0]],[p[1],q[1]],[p[2],q[2]],color='#b8b8b8',lw=.28,alpha=.55,zorder=1)
    ax.scatter(X,Y,Z,c=COL,s=13,depthshade=True,edgecolors='none',zorder=3)
    ax.view_init(elev=elev,azim=azim)
    ax.set_xlabel('u  snarl height',labelpad=-6,fontsize=7)
    ax.set_ylabel('a  allele index',labelpad=-6,fontsize=7)
    ax.set_zlabel('k  dosage  (+ e)',labelpad=-6,fontsize=7)
    ax.set_title(title,fontsize=8,loc='left',pad=0)
    ax.tick_params(labelsize=5.5,pad=-3)
    ax.set_box_aspect((2.0,1.5,1.0))
    for pane in (ax.xaxis,ax.yaxis,ax.zaxis):
        pane.pane.set_alpha(0.03); pane.pane.set_edgecolor('#dddddd')
    ax.grid(alpha=.15)

fig=plt.figure(figsize=(11,8.4))
for i,(el,az,t) in enumerate([(20,-62,'(a)  the staircase, extruded along dosage'),
                              (6,-90,'(b)  along a — the monotone bound A(u)'),
                              (74,-90,'(c)  from above — the (u,a) staircase'),
                              (12,-6,'(d)  along u — the dosage triangle e ≤ k')]):
    panel(fig.add_subplot(2,2,i+1,projection='3d'),el,az,t)
h=[plt.Line2D([],[],marker='o',ls='',color=CM[i],label=f'e = {i} expressed') for i in range(3)]
fig.legend(handles=h,loc='lower center',ncol=3,frameon=False,fontsize=8,bbox_to_anchor=(.5,.005))
fig.suptitle('Λ_G — the diploid genome lattice.   E = 0, density 0.1531 at full scale '
             f'(shown: {len(LG)} cells, A(u) = {A})',fontsize=9.5,x=.02,ha='left')
fig.tight_layout(rect=[0,.035,1,.955])
fig.savefig('/home/claude/lattice/lambda_G_3d.pdf'); fig.savefig('/home/claude/lattice/lambda_G_3d.png')
print('static figure written')
json.dump({'A':A,'cells':LG,'edges':[[list(a),list(b)] for a,b in
    [( (u,a,k,e),(u+d[0],a+d[1],k+d[2],e+d[3]) ) for (u,a,k,e) in LG
      for d in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
      if (u+d[0],a+d[1],k+d[2],e+d[3]) in set(LG)]]},
    open('/home/claude/lattice/lg.json','w'))