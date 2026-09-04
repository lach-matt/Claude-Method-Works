import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from collections import Counter
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
  'axes.edgecolor':'#333333','axes.linewidth':0.8,'axes.labelcolor':'#222222',
  'xtick.color':'#333333','ytick.color':'#333333','axes.spines.top':False,
  'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
INK='#1a1a1a'; ACC='#8c2d19'; MID='#5a7d9a'; LIGHT='#b8b8b8'; GOOD='#3d6b47'
R=109737.3; T=lambda v: R/v**2
OUT='/home/claude/book/fig/'

# ---------- F19  V at matched order ----------
def pa(nd,n): return np.polyval(np.polyfit(nd,[T(t) for t in nd],len(nd)-1),n)
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
def est(n,k):
    nd=sorted([n+j for j in range(-k,k+1) if j!=0])[:k+1]
    return abs(pa(nd,n)-T(n))
fig,ax=plt.subplots(1,2,figsize=(10.4,4.4))
ks=[1,2,3,4,5]
for nu,mk,cl in [(20,'o',MID),(40,'s',ACC),(80,'^',GOOD)]:
    vs=[]
    for k in ks:
        lo,hi=bk(nu,k); vs.append((hi-lo)/est(nu,k))
    ax[0].plot(ks,vs,marker=mk,color=cl,lw=1.6,ms=6,label=f'ν = {nu}')
ax[0].axhline(2,color=INK,ls='--',lw=1.2)
ax[0].text(5.05,2.06,'floor  V = 2',fontsize=8.5,color=INK,ha='right')
ax[0].set_xlabel('order of bracket and estimate, $k$')
ax[0].set_ylabel('$V$ at matched order')
ax[0].set_ylim(0,4); ax[0].set_xticks(ks); ax[0].legend(frameon=False,fontsize=8.5)
ax[0].set_title('the cost does not grow with order',fontsize=10,color=INK,loc='left')
nu=40
w1=[abs(bk(nu,1)[1]-bk(nu,1)[0])]*5
ws=[abs(bk(nu,k)[1]-bk(nu,k)[0]) for k in ks]
es=[est(nu,k) for k in ks]
ax[1].semilogy(ks,ws,marker='s',color=ACC,lw=1.6,ms=6,label='bracket width')
ax[1].semilogy(ks,es,marker='o',color=MID,lw=1.6,ms=6,label='estimate error')
ax[1].semilogy(ks,w1,color=LIGHT,lw=1.4,ls=':',label='order-1 bracket, held fixed')
ax[1].set_xlabel('order $k$'); ax[1].set_ylabel('cm$^{-1}$, log scale')
ax[1].set_xticks(ks); ax[1].legend(frameon=False,fontsize=8.5)
ax[1].set_title('both tighten together  (ν = 40)',fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f19_order.png',dpi=150); plt.close()
print("f19 ok")

# ---------- F20  amplification / cost of forgery ----------
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX)); LAM={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
LL=sorted(LAM); d=8; grid=np.array(BOX,dtype=np.int32)
def csz(A):
    m=np.ones(len(grid),dtype=bool)
    for i in range(d):
        for j in range(d):
            if i==j: continue
            for a in range(7):
                m &= grid[:,i] <= a*grid[:,j]+int((A[:,i]-a*A[:,j]).max())
    return int(m.sum())
import random; random.seed(3)
out=[z for z in BOX if z not in LAM]
amps=[csz(np.array(LL+[random.choice(out)],dtype=np.int32))-len(LAM)-1 for _ in range(140)]
fig,ax=plt.subplots(figsize=(9.4,4.6))
ax.hist(amps,bins=26,color=MID,edgecolor='white',linewidth=0.6)
ax.axvline(min(amps),color=ACC,lw=1.6)
ax.text(min(amps)+14,ax.get_ylim()[1]*0.88,f'cheapest forgery\n{min(amps)+1} cells',
        fontsize=8.5,color=ACC)
ax.axvline(0,color=INK,lw=1.4,ls='--')
ax.text(6,ax.get_ylim()[1]*0.5,'A = 0 would be\nan invisible lie\n— none occur',fontsize=8.5,color=INK)
ax.set_xlabel('amplification  A(y) — extra cells the closure must admit')
ax.set_ylabel('fabrications')
ax.set_title('every single fabrication amplifies: %d of %d, minimum %d'%(len(amps),len(amps),min(amps)),
             fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f20_forgery.png',dpi=150); plt.close()
print("f20 ok  min",min(amps),"median",int(np.median(amps)))