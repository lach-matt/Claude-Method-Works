import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, itertools
exec(open('audit.py').read().split('print("case')[0])
# Fig 1: shape sphere, five central configurations + three collision rays, two mass cases
fig=plt.figure(figsize=(10,5))
for k,(title,m) in enumerate([("equal masses (1,1,1)",(1,1,1)),("masses (1,2,3)",(1,2,3))]):
    m=np.array(m,float); ax=fig.add_subplot(1,2,k+1,projection='3d')
    u,v=np.mgrid[0:2*np.pi:40j,0:np.pi:20j]; ax.plot_wireframe(np.cos(u)*np.sin(v),np.sin(u)*np.sin(v),np.cos(v),color='0.85',lw=0.4)
    for (i,j),b in binary_rays(m).items(): ax.scatter(*b,c='k',s=40); ax.text(*b*1.15,f"B{i+1}{j+1}",fontsize=8)
    # Lagrange: equilateral both orientations
    for s in [1,-1]:
        q=np.array([1,np.exp(s*2j*np.pi/3),np.exp(s*4j*np.pi/3)]); q-=(m@q)/m.sum(); w=shape(*jacobi(q,m)); w/=np.linalg.norm(w)
        ax.scatter(*w,c='tab:red',s=60); ax.text(*w*1.15,"L",fontsize=9,color='tab:red')
    # Euler: collinear, solve quintic per ordering numerically via critical points on equator
    th=np.linspace(0,2*np.pi,2000); best=[]
    for t in th:
        w=np.array([np.cos(t),np.sin(t),0]); best.append(V0_shape(w,m))
    best=np.array(best); crit=[i for i in range(1,len(th)-1) if best[i]<best[i-1] and best[i]<best[i+1]]
    for i in crit: w=np.array([np.cos(th[i]),np.sin(th[i]),0]); ax.scatter(*w,c='tab:blue',s=60); ax.text(*w*1.15,"E",fontsize=9,color='tab:blue')
    ax.set_title(title,fontsize=10); ax.set_axis_off()
fig.suptitle("Fig. 1  The shape sphere: 3 Euler (E), 2 Lagrange (L), 3 binary-collision rays (B). Masses move the points; they never change the count.",fontsize=9)
plt.savefig('/mnt/user-data/outputs/fig1_shape_sphere.png',dpi=160,bbox_inches='tight')
# Fig 2: closure defect of the triangle form vs cap
caps=range(3,13); rows=[closure_test(c) for c in caps]
fig,ax=plt.subplots(figsize=(6,3.5))
ax.plot(list(caps),[r[1] for r in rows],'o-',label='meet failures (K₃ triangle)')
ax.plot(list(caps),[r[2] for r in rows],'s-',label='join failures (K₃ triangle)')
ax.plot(list(caps),[r[3] for r in rows],'^-',label='failures, two-body chain')
ax.set_xlabel('cap'); ax.set_ylabel('count'); ax.set_yscale('symlog'); ax.legend(fontsize=8)
ax.set_title("Fig. 2  §12.11.2 on three bodies: join-closed, meet-broken; two bodies close.",fontsize=9)
plt.savefig('/mnt/user-data/outputs/fig2_closure_defect.png',dpi=160,bbox_inches='tight')
print([(c,)+r for c,r in zip(caps,rows)])
# Fig 3: the tower read downward
fig,ax=plt.subplots(figsize=(7,3)); ax.axis('off')
tiers=[("12 inputs\n(ρ₁,ρ₂,p₁,p₂)","full phase space\nℳ_{E,L}","trajectory r_i(s)"),("4 inputs\n(w₁,w₂,p₁,p₂)","planar reduced\nS² geodesic flow","reduced path w(s)"),("2 inputs\n(E, braid word)","periodic stratum\nℳ_per","closed loop in B₃"),("1 input\nL̃ = L²|E|/G²M⁵","ergodic stratum\nℳ_erg","distribution P(ε)")]
for i,(a,b,c) in enumerate(tiers):
    y=0.85-0.27*i; ax.text(0.02,y,a,fontsize=8,va='center'); ax.text(0.35,y,b,fontsize=8,va='center'); ax.text(0.72,y,c,fontsize=8,va='center')
    if i<3: ax.annotate('',xy=(0.5,y-0.13),xytext=(0.5,y-0.05),arrowprops=dict(arrowstyle='->'))
ax.text(0.02,0.98,"axes dropped",fontsize=8,weight='bold'); ax.text(0.35,0.98,"index",fontsize=8,weight='bold'); ax.text(0.72,0.98,"product",fontsize=8,weight='bold')
ax.set_title("Fig. 3  The tower read downward: each dropped axis coarsens the product (§12.11, §17.4).",fontsize=9)
plt.savefig('/mnt/user-data/outputs/fig3_tower.png',dpi=160,bbox_inches='tight')