import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, random, math, itertools
plt.rcParams.update({'font.family':'serif','font.serif':['FreeSerif','DejaVu Serif'],
    'font.size':9,'axes.linewidth':0.7,'figure.dpi':300,'savefig.dpi':300,
    'axes.spines.top':False,'axes.spines.right':False,'axes.grid':False})
INK='#1a1a1a'; ACC='#8c2f39'; MUT='#9a9a9a'; W=6.4
FD='/home/claude/paper/fig/'

L={1:248956422,2:242193529,3:198295559,4:190214555,5:181538259,6:170805979,7:159345973,
   8:145138636,9:138394717,10:133797422,11:135086622,12:133275309,13:114364328,14:107043718,
   15:101991189,16:90338345,17:83257441,18:80373285,19:58617616,20:64444167,21:46709983,
   22:50818468,23:156040895,24:57227415}
order=sorted(L); lens=[L[c] for c in order]
lab=[str(c) for c in range(1,23)]+['X','Y']
N=sum(lens)

def R2(cells):
    S=set(cells)
    while True:
        new={tuple(map(max,zip(x,y))) for x in S for y in S}|{tuple(map(min,zip(x,y))) for x in S for y in S}
        if new<=S: return S
        S|=new
def E2(c): return len(R2(c))-len(set(c))

# --- Fig 1 : the closure staircase --------------------------------------
run=np.maximum.accumulate(lens)
f,ax=plt.subplots(figsize=(W,3.0))
x=np.arange(24)
ax.fill_between(x,0,np.array(run)/1e6,step='mid',color=ACC,alpha=.16,lw=0,label='ℛ(X) — admitted by closure')
ax.fill_between(x,0,np.array(lens)/1e6,step='mid',color=INK,alpha=.80,lw=0,label='X — assembled bases')
ax.step(x,np.array(run)/1e6,where='mid',color=ACC,lw=1.1)
ax.set_xticks(x); ax.set_xticklabels(lab,fontsize=7); ax.set_xlim(-.6,23.6)
ax.set_ylabel('Mb'); ax.set_xlabel('chromosome, conventional label')
ax.legend(frameon=False,fontsize=8,loc='upper right')
ax.set_title('E(X) = 2,886,684,296 — the shaded difference',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f1_staircase.pdf'); plt.close(f)

# --- Fig 2 : inversions --------------------------------------------------
f,ax=plt.subplots(figsize=(W,2.7))
cols=[ACC if c in(10,11,19,20,21,22) else INK for c in order]
ax.bar(x,np.array(lens)/1e6,color=cols,width=.72)
for a,b in [(9,10),(18,19),(20,21)]:
    ax.annotate('',xy=(b,lens[b]/1e6+9),xytext=(a,lens[a]/1e6+9),
        arrowprops=dict(arrowstyle='<->',color=ACC,lw=.9))
    ax.text((a+b)/2,max(lens[a],lens[b])/1e6+14,'inv',ha='center',fontsize=7,color=ACC)
ax.set_xticks(x); ax.set_xticklabels(lab,fontsize=7); ax.set_ylabel('Mb')
ax.set_title('Three autosome inversions: (10,11), (19,20), (21,22)',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f2_inversions.pdf'); plt.close(f)

# --- Fig 3 : inversion-count stability ----------------------------------
random.seed(3); cnt={}
for _ in range(2000):
    p=[int(v*random.uniform(.97,1.03)) for v in lens]
    n=sum(1 for i in range(24) for j in range(i+1,24) if p[i]<p[j] and order[i]<=22 and order[j]<=22)
    cnt[n]=cnt.get(n,0)+1
f,ax=plt.subplots(figsize=(W,2.4))
ks=sorted(cnt); ax.bar(ks,[cnt[k] for k in ks],color=[ACC if k==3 else MUT for k in ks],width=.7)
ax.set_xlabel('autosome inversions under ±3% length perturbation'); ax.set_ylabel('trials (of 2000)')
ax.set_title('The count of three is not structural — reproduced 475/2000',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f3_stability.pdf'); plt.close(f)
STAB=cnt.get(3,0)

# --- Fig 4 : E/N -> 3 ----------------------------------------------------
random.seed(7); Ns=[25,50,100,200,400,800,1600]; ratio=[]
for n in Ns:
    s=[random.randrange(4) for _ in range(n)]
    ratio.append(E2([(i,b) for i,b in enumerate(s)])/n)
f,ax=plt.subplots(figsize=(W,2.5))
ax.axhline(3,color=ACC,lw=.9,ls='--',label='|Σ| − 1 = 3')
ax.plot(Ns,ratio,'o-',color=INK,ms=4,lw=1)
ax.set_xscale('log'); ax.set_xlabel('sequence length N'); ax.set_ylabel('E / N')
ax.set_ylim(2.7,3.15); ax.legend(frameon=False,fontsize=8)
ax.set_title('E = N(|Σ| − 1) for a random sequence',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f4_ratio.pdf'); plt.close(f)

# --- Fig 5 : the k-mer crossing -----------------------------------------
ks=np.arange(8,24); a=4.0**ks; b=N-ks+1
f,ax=plt.subplots(figsize=(W,2.9))
ax.semilogy(ks,a,color=INK,lw=1.2,label=r'$4^k$  alphabet cap')
ax.semilogy(ks,b,color=ACC,lw=1.2,label=r'$N-k+1$  length cap')
ax.semilogy(ks,np.minimum(a,b),color='k',lw=2.2,alpha=.25)
kst=math.log(N,4); ax.axvline(kst,color=MUT,lw=.8,ls=':')
ax.annotate(f'k* = {kst:.3f}',xy=(kst,4**kst),xytext=(kst+1.6,10**7),fontsize=8,
            arrowprops=dict(arrowstyle='-',color=MUT,lw=.7))
ax.set_xlabel('k'); ax.set_ylabel('distinct k-mers (bound)'); ax.legend(frameon=False,fontsize=8)
ax.set_title('Two branches, and where they cross',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f5_kmer.pdf'); plt.close(f)

# --- Fig 6 : three budgets ----------------------------------------------
names=['coordinate\nE(chr,pos)','ignorance\nE(N-runs)','contingent\nE(pos,base)']
vals=[2886684296,150630700,3*N]; obs=[0,150630700,786500648]
f,ax=plt.subplots(figsize=(W,2.9))
ax.bar(range(3),vals,color=[MUT,ACC,INK],width=.55)
ax.bar(range(3),obs,color='none',edgecolor='w',lw=1.1,hatch='///',width=.55)
for i,(v,o) in enumerate(zip(vals,obs)):
    ax.text(i,v*1.35,f'{v:,}',ha='center',fontsize=7.5)
    if o: ax.text(i,o*0.32,f'settled\n{o/v:.1%}',ha='center',fontsize=7,color='w')
ax.set_yscale('log'); ax.set_xticks(range(3)); ax.set_xticklabels(names,fontsize=8)
ax.set_ylabel('admitted-and-absent cells'); ax.set_ylim(1e7,4e10)
ax.set_title('E partitions by the modality of the admitted cell',fontsize=9,loc='left')
f.tight_layout(); f.savefig(FD+'f6_budgets.pdf'); plt.close(f)

# --- Fig 7 : the snarl tower --------------------------------------------
D=28; H=94; A=[max(2,round(H**(u/D))) for u in range(D+1)]
occ=sum(A); box=(D+1)*max(A); dens=occ/box
cells=[(u,aa) for u,Au in enumerate(A) for aa in range(Au)]
rev  =[(u,aa) for u,Au in enumerate(A[::-1]) for aa in range(Au)]
Eh,El=E2(cells),E2(rev)
f,axs=plt.subplots(1,2,figsize=(W,2.8),sharey=True)
for ax,vec,ttl,e in ((axs[0],A,'by height  u = D − level',Eh),(axs[1],A[::-1],'by level, as labelled',El)):
    ax.fill_between(range(D+1),0,vec,step='post',color=INK if e==0 else MUT,alpha=.8,lw=0)
    ax.step(range(D+1),vec,where='post',color=ACC if e==0 else MUT,lw=1)
    ax.set_title(f'{ttl}\nE = {e:,}',fontsize=8.5,loc='left'); ax.set_xlabel('u')
axs[0].set_ylabel('A(u), observed alleles')
f.suptitle(f'The snarl tower — density {dens:.4f}, not a full product',fontsize=9,x=.01,ha='left')
f.tight_layout(rect=[0,0,1,.93]); f.savefig(FD+'f7_snarl.pdf'); plt.close(f)

# --- Fig 8 : the lemma ---------------------------------------------------
random.seed(5); pts=[]
for _ in range(3000):
    n=random.randint(2,8); v=[random.randint(1,9) for _ in range(n)]
    d=sum(1 for i in range(n) for j in range(i+1,n) if v[i]>v[j])
    pts.append((d,E2([(i,x) for i,x in enumerate(v)])))
d0=[e for d,e in pts if d==0]; dn=[e for d,e in pts if d>0]
f,ax=plt.subplots(figsize=(W,2.6))
jx=[d+random.uniform(-.18,.18) for d,_ in pts]
ax.scatter(jx,[e for _,e in pts],s=5,color=INK,alpha=.28,lw=0)
ax.scatter([0]*len(d0),d0,s=9,color=ACC,alpha=.9,lw=0)
ax.set_xlabel('inversions in v'); ax.set_ylabel('E(X)')
ax.set_title(f'E = 0 ⟺ v non-decreasing. {len(d0)} monotone cases, all at E = 0; '
             f'{sum(1 for e in dn if e==0)} non-monotone at E = 0',fontsize=8.5,loc='left')
f.tight_layout(); f.savefig(FD+'f8_lemma.pdf'); plt.close(f)

import json
json.dump({'E_pos':2886684296,'N':N,'stab3':STAB,'kstar':math.log(N,4),
           'occ':occ,'box':box,'dens':dens,'Eh':Eh,'El':El,
           'mono_nonzero':sum(1 for e in d0 if e!=0),'nonmono_zero':sum(1 for e in dn if e==0),
           'nfig':8},open('/home/claude/paper/facts.json','w'),indent=1)
print(f'8 figures written. N={N:,}  density={dens:.4f}  Eh={Eh} El={El:,}')
print(f'stability(3 inversions)={STAB}/2000   k*={math.log(N,4):.3f}')
print(f'lemma check: monotone-with-E!=0 = {sum(1 for e in d0 if e!=0)}, '
      f'nonmonotone-with-E=0 = {sum(1 for e in dn if e==0)}')