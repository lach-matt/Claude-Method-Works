import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, warnings
warnings.filterwarnings('ignore')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
  'axes.edgecolor':'#333333','axes.linewidth':0.8,'axes.labelcolor':'#222222',
  'xtick.color':'#333333','ytick.color':'#333333','axes.spines.top':False,
  'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
INK='#1a1a1a'; ACC='#8c2d19'; MID='#5a7d9a'; GOOD='#3d6b47'; LIGHT='#b8b8b8'
R=109737.3; T=lambda v: R/v**2
def pa(nd,n): return np.polyval(np.polyfit(nd,[T(t) for t in nd],len(nd)-1),n)
def nodes(n,k):
    S=set()
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)==k+1 and min(nd)>=2: S|=set(nd)
    return sorted(S)
def bk(n,k):
    lo,hi=-np.inf,np.inf
    for m in range(0,k+2):
        bl=k+1-m
        if bl<0: continue
        nd=sorted([n+j for j in range(1,m+1)]+[n-j for j in range(1,bl+1)])
        if len(nd)!=k+1 or min(nd)<2: continue
        p=pa(nd,n)
        if (k+1+m)%2==0: lo=max(lo,p)
        else: hi=min(hi,p)
    return lo,hi
ks=[1,2,3,4,5]
fig,ax=plt.subplots(1,2,figsize=(10.4,4.4))
for nu,mk,cl in [(20,'o',MID),(40,'s',ACC),(80,'^',GOOD)]:
    V=[]
    for k in ks:
        lo,hi=bk(nu,k); nb=nodes(nu,k)
        V.append((hi-lo)/abs(pa(nb,nu)-T(nu)))
    ax[0].semilogy(ks,V,marker=mk,color=cl,lw=1.6,ms=6,label=f'ν = {nu}')
ax[0].set_xlabel('order $k$  (bracket and estimate on the same nodes)')
ax[0].set_ylabel('$V$ = bracket width / estimate error')
ax[0].set_xticks(ks); ax[0].legend(frameon=False,fontsize=8.5)
ax[0].set_title('the cost of a guarantee grows with order',fontsize=10,color=INK,loc='left')
nu=40
w=[bk(nu,k)[1]-bk(nu,k)[0] for k in ks]
e=[abs(pa(nodes(nu,k),nu)-T(nu)) for k in ks]
ax[1].semilogy(ks,w,marker='s',color=ACC,lw=1.7,ms=6,label='bracket width — deductive')
ax[1].semilogy(ks,e,marker='o',color=MID,lw=1.7,ms=6,label='estimate error — inferential')
ax[1].fill_between(ks,e,w,color=LIGHT,alpha=0.35)
ax[1].text(3.1,3e-5,'the gap is the price\nof certainty,\nand it widens',fontsize=8.5,color=INK)
ax[1].set_xlabel('order $k$'); ax[1].set_ylabel('cm$^{-1}$, log scale')
ax[1].set_xticks(ks); ax[1].legend(frameon=False,fontsize=8.5,loc='lower left')
ax[1].set_title('both improve — the estimate faster  (ν = 40)',fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig('/home/claude/book/fig/f19_order.png',dpi=150); plt.close()
print("f19 redrawn")
for nu in (20,40,80):
    V=[]
    for k in ks:
        lo,hi=bk(nu,k); nb=nodes(nu,k)
        V.append((hi-lo)/abs(pa(nb,nu)-T(nu)))
    print("  nu=%2d  V: %s"%(nu,"  ".join("%.3g"%v for v in V)))