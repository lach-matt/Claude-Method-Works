import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, json, os
from itertools import product
from collections import Counter
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,
  'axes.edgecolor':'#333333','axes.linewidth':0.8,'axes.labelcolor':'#222222',
  'xtick.color':'#333333','ytick.color':'#333333','axes.spines.top':False,
  'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
INK='#1a1a1a'; ACC='#8c2d19'; MID='#5a7d9a'; LIGHT='#b8b8b8'; GOOD='#3d6b47'; WARM='#c98b3a'
OUT='/home/claude/book/fig/'
R=109737.3

# ---------- F21  refusal rate vs order — the perturbation detector ----------
def fd(Tv,nodes,order):
    ys=[Tv[x] for x in nodes]
    for _ in range(order): ys=[ys[i+1]-ys[i] for i in range(len(ys)-1)]
    return ys[0] if ys else None
def status(Tv,n,k,sig):
    span=[n+j for j in range(-(k+1),k+2)]
    if any(x not in Tv for x in span): return 'missing'
    want = 1 if (k+1)%2==0 else -1
    floor=5*(2.0**(k+1))*sig
    for s in range(0,len(span)-(k+1)):
        dd=fd(Tv,span[s:s+k+2],k+1)
        if dd is None: return 'missing'
        if abs(dd)<floor: return 'unresolved'
        if np.sign(dd)!=want: return 'refused'
    return 'ok'
LIM={'na1.json':(41449.451,1),'k1.json':(35009.8140,1),'al1.json':(48278.480,1),
 'li1.json':(43487.11420,1),'ga1.json':(48387.634,1),'he1.json':(198310.66637,1),
 'ca2.json':(95751.87,2),'cd2.json':(136374.74,2),'mg2.json':(121267.64,2),
 'si2.json':(131838.14,2),'zn2.json':(144892.6,2),'be2.json':(146882.86,2),
 'li2.json':(610078.4,2),'he2.json':(438908.871,2)}
chans=[]
for fn,(I,Z) in LIM.items():
    p='/home/claude/data/'+fn
    if not os.path.exists(p): continue
    for lab,M in json.load(open(p)).items():
        M={int(a):b for a,b in M.items()}
        Tv={n:I-M[n] for n in M if I-M[n]>0}
        if len(Tv)>=5:
            dg=0
            for v in [M[n] for n in M]:
                s=("%.6f"%v).rstrip('0')
                if '.' in s: dg=max(dg,len(s.split('.')[1]))
            chans.append((Tv,10.0**(-dg) if dg else 1.0))
ks=list(range(1,8)); OK=[];RF=[];UN=[]
for k in ks:
    o=r=u=0
    for Tv,sig in chans:
        for n in sorted(Tv):
            s=status(Tv,n,k,sig)
            if s=='ok': o+=1
            elif s=='refused': r+=1
            elif s=='unresolved': u+=1
    OK.append(o);RF.append(r);UN.append(u)
fig,ax=plt.subplots(1,2,figsize=(10.4,4.4))
w=0.62
ax[0].bar(ks,OK,w,color=GOOD,label='admitted — contained')
ax[0].bar(ks,RF,w,bottom=OK,color=ACC,label='refused — wrong sign (physics)')
ax[0].bar(ks,UN,w,bottom=np.array(OK)+np.array(RF),color=LIGHT,label='unresolved — below quotation floor')
ax[0].set_xlabel('order $k$'); ax[0].set_ylabel('cells')
ax[0].legend(frameon=False,fontsize=8)
ax[0].set_title('the higher the order, the finer the detector',fontsize=10,color=INK,loc='left')
rate=[100*r/max(o+r,1) for o,r in zip(OK,RF)]
ax[1].plot(ks,rate,marker='o',color=ACC,lw=1.8,ms=6)
for k,v in zip(ks,rate): ax[1].annotate(f'{v:.0f}%',(k,v),textcoords='offset points',
    xytext=(0,7),ha='center',fontsize=8,color=INK)
ax[1].set_xlabel('order $k$'); ax[1].set_ylabel('refused, % of admissible')
ax[1].set_ylim(0,105)
ax[1].set_title('refusal is a perturbation, detected deductively',fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f21_refusal.png',dpi=150); plt.close()
print("f21 ok  rates",[round(x) for x in rate])

# ---------- F22  the caterpillar tree ----------
fig,ax=plt.subplots(figsize=(9.6,3.0))
path=['n','ℓ','k','q','g','f','e']
xs=np.arange(len(path))*1.0
for i in range(len(path)-1):
    ax.annotate('',xy=(xs[i+1]-0.16,0),xytext=(xs[i]+0.16,0),
        arrowprops=dict(arrowstyle='-|>',color=INK,lw=1.3,shrinkA=0,shrinkB=0))
for x,lab in zip(xs,path):
    ax.add_patch(plt.Circle((x,0),0.16,color='white',ec=INK,lw=1.3,zorder=3))
    ax.text(x,0,lab,ha='center',va='center',fontsize=11,zorder=4,color=INK)
kx=xs[2]
ax.annotate('',xy=(kx,-0.72+0.16),xytext=(kx,-0.16),
    arrowprops=dict(arrowstyle='-|>',color=MID,lw=1.3,shrinkA=0,shrinkB=0))
ax.add_patch(plt.Circle((kx,-0.72),0.16,color='white',ec=MID,lw=1.3,zorder=3))
ax.text(kx,-0.72,'2S',ha='center',va='center',fontsize=10,zorder=4,color=MID)
ax.annotate('',xy=(xs[4]+0.16,0.02),xytext=(xs[3]+0.30,0.42),
    arrowprops=dict(arrowstyle='-|>',color=ACC,lw=1.3,ls=(0,(4,2))))
ax.text(xs[3]+0.34,0.50,'g ≤ q',fontsize=8.5,color=ACC)
ax.text(xs[4]+0.44,0.32,'g ≤ 2(2f+1)   ← the Pauli principle,\nthe only coupling in the expression',
        fontsize=8.5,color=ACC,va='bottom')
ax.text(kx,-1.10,'a leaf: algebraically inert,\nfactors out as (1−z⁸ᵏ⁺¹)/(1−z₈)',
        ha='center',fontsize=8,color=MID)
ax.set_xlim(-0.6,len(path)-0.1); ax.set_ylim(-1.45,0.95); ax.axis('off')
ax.set_title('a caterpillar: a path of seven, one pendant — the simplest tree that is not a path',
             fontsize=10,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f22_caterpillar.png',dpi=150); plt.close()
print("f22 ok")

# ---------- F23  the rank polynomial and its asymmetry ----------
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
rk=Counter(sum(x) for x in LAM); ks2=sorted(rk); c=[rk[k] for k in ks2]
fig,ax=plt.subplots(figsize=(9.6,4.4))
ax.bar(ks2,c,0.74,color=MID,edgecolor='white',linewidth=0.6,label='coefficient of $z^r$')
ax.plot(ks2,c[::-1],color=ACC,lw=1.5,ls='--',marker='',label='the same read backwards')
mean=sum(k*rk[k] for k in ks2)/sum(c); mid=(min(ks2)+max(ks2))/2
ax.axvline(mean,color=INK,lw=1.2)
ax.axvline(mid,color=LIGHT,lw=1.2,ls=':')
ax.annotate('mean rank 11.07',(mean,max(c)*0.97),xytext=(mean-4.6,max(c)*0.99),
    fontsize=8.5,color=INK,arrowprops=dict(arrowstyle='-',color=INK,lw=0.8))
ax.annotate('midpoint 11.5',(mid,max(c)*0.80),xytext=(mid+1.0,max(c)*0.84),
    fontsize=8.5,color='#777777',arrowprops=dict(arrowstyle='-',color=LIGHT,lw=0.8))
ax.set_xlabel('rank $r$ = sum of coordinates'); ax.set_ylabel('cells of that rank')
ax.legend(frameon=False,fontsize=8.5,loc='upper right')
ax.set_title('$F(z)$: forwards 1, 5, 15, 34 …  backwards 1, 4, 10, 21 —  not palindromic, so not self-dual',
             fontsize=9.6,color=INK,loc='left')
plt.tight_layout(); plt.savefig(OUT+'f23_rankpoly.png',dpi=150); plt.close()
print("f23 ok  skew",round(mean-mid,2))