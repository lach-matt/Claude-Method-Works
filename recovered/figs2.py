# RECONSTRUCTED FROM TRANSCRIPT (chat b778e075, 2026-08-23). Original heredoc `figs2.py`. Writes to OUT.
# Seam: the Fig 4 title string was split across two transcript snippets; joined at "Fig. 4  U on the collinear circle".
import numpy as np, matplotlib, os; matplotlib.use('Agg'); import matplotlib.pyplot as plt
OUT=os.environ.get('OUT','.')
exec(open('audit.py').read().split('print("case')[0])
# Fig 4 (Physics): potential along the collinear equator for three mass cases; minima = Euler points
th=np.linspace(0.001,2*np.pi-0.001,3000); fig,ax=plt.subplots(figsize=(7,3.5))
for m,lab in [((1,1,1),'(1,1,1)'),((1,2,3),'(1,2,3)'),((3,1,1),'(3,1,1)')]:
    m=np.array(m,float); U=[V0_shape(np.array([np.cos(t),np.sin(t),0]),m) for t in th]
    ax.plot(th,U,label=f'm = {lab}'); 
ax.set_ylim(0,40); ax.set_xlabel('angle on the collinear equator'); ax.set_ylabel('U(w), |w| = 1'); ax.legend(fontsize=8)
ax.set_title('Fig. 4  U on the collinear circle: three poles (binary collisions), three minima (Euler points), every mass case.',fontsize=8)
plt.savefig(f'{OUT}/fig4_equator_potential.png',dpi=160,bbox_inches='tight')
# Fig 5 (Index of Indices / Math): constraint graphs and consistency levels
fig,ax=plt.subplots(1,2,figsize=(7,3)); 
for a,(pts,edges,title) in zip(ax,[([(0,0),(1,0)],[(0,1)],'two bodies: K₂, treewidth 1\nℛ reaches level 2 = needed'),([(0,0),(1,0),(0.5,0.87)],[(0,1),(1,2),(0,2)],'three bodies: K₃, treewidth 2\nneeds strong 3-consistency; ℛ gives 2')]):
    for i,j in edges: a.plot([pts[i][0],pts[j][0]],[pts[i][1],pts[j][1]],'k-')
    for k,(x,y) in enumerate(pts): a.scatter(x,y,s=300,c='w',edgecolors='k',zorder=3); a.text(x,y,f'm{k+1}',ha='center',va='center',fontsize=9,zorder=4)
    a.set_title(title,fontsize=8); a.set_xlim(-0.4,1.4); a.set_ylim(-0.4,1.3); a.axis('off')
fig.suptitle('Fig. 5  The deficit is exactly one level (§21.5.1); the tree closes, the triangle does not.',fontsize=9)
plt.savefig(f'{OUT}/fig5_constraint_graphs.png',dpi=160,bbox_inches='tight')