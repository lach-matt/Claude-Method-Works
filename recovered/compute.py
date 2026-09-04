"""Single source of truth. Every number in the paper and every figure derives from this."""
import json, math, random
from itertools import product

def R2(cells):
    S=set(cells)
    while True:
        new={tuple(map(max,zip(x,y))) for x in S for y in S}|{tuple(map(min,zip(x,y))) for x in S for y in S}
        if new<=S: return S
        S|=new
def E(cells): return len(R2(cells))-len(set(cells))

D={}
# ---- 1 coordinate index ---------------------------------------------------
L={1:248956422,2:242193529,3:198295559,4:190214555,5:181538259,6:170805979,7:159345973,
   8:145138636,9:138394717,10:133797422,11:135086622,12:133275309,13:114364328,14:107043718,
   15:101991189,16:90338345,17:83257441,18:80373285,19:58617616,20:64444167,21:46709983,
   22:50818468,23:156040895,24:57227415}
NAME={23:'X',24:'Y'}
order=sorted(L); lens=[L[c] for c in order]
nm=lambda c: NAME.get(c,str(c))
def clos(v):
    M=[];r=0
    for x in v: r=max(r,x); M.append(r)
    return sum(M),M
Rsz,M=clos(lens); occ=sum(lens)
D['chrom']={'names':[nm(c) for c in order],'lens':lens,'M':M,'occ':occ,'R':Rsz,'E':Rsz-occ,
            'ratio':(Rsz-occ)/occ,'Mconst':len(set(M))==1}
def viol(v): return sum(1 for i in range(len(v)) for j in range(len(v)) if max(v[i],v[j])>v[max(i,j)])
D['chrom']['viol']=viol(lens); D['chrom']['pairs']=len(lens)**2
srt=sorted(lens); Rs,_=clos(srt)
D['chrom']['E_sorted']=Rs-sum(srt); D['chrom']['viol_sorted']=viol(srt)
inv=[(nm(order[i]),nm(order[j])) for i in range(len(lens)) for j in range(i+1,len(lens)) if lens[i]<lens[j]]
D['chrom']['inv_all']=len(inv)
D['chrom']['inv_aut']=[(a,b) for a,b in inv if a.isdigit() and b.isdigit()]
# stability
random.seed(11)
def stab(pct,trials=2000):
    same=0; dist={}
    base=D['chrom']['inv_aut']
    for _ in range(trials):
        p=[int(x*random.uniform(1-pct,1+pct)) for x in lens]
        iv=[(nm(order[i]),nm(order[j])) for i in range(len(p)) for j in range(i+1,len(p))
            if p[i]<p[j] and str(nm(order[i])).isdigit() and str(nm(order[j])).isdigit()]
        if [list(t) for t in iv]==[list(t) for t in base]: same+=1
        dist[len(iv)]=dist.get(len(iv),0)+1
    return same,dist
D['chrom']['stab3'],D['chrom']['dist3']=stab(0.03)
random.seed(11)
closed10=sum(1 for _ in range(2000) if viol([int(x*random.uniform(.9,1.1)) for x in lens])==0)
D['chrom']['closed_under_10pct']=closed10
# R overwrites bounds
toy=[10,7,13,4]; X={(c,p) for c,l in enumerate(toy) for p in range(1,l+1)}
RX=R2(X); D['toy']={'declared':toy,
  'recovered':[max(p for cc,p in X if cc==c) for c in range(4)],
  'after_R':[max(p for cc,p in RX if cc==c) for c in range(4)],'E':len(RX)-len(X)}

# ---- 2 sequence content ---------------------------------------------------
random.seed(7); seq=[]
for N in (50,100,200,400,800):
    v=[random.randrange(4) for _ in range(N)]
    e=E([(i,b) for i,b in enumerate(v)])
    s=E([(i,b) for i,b in enumerate(sorted(v))])
    seq.append({'N':N,'E':e,'ratio':e/N,'E_sorted':s})
D['seq']=seq
N=occ; D['content']={'N':N,'E':3*N,'bits':N*math.log2(4),'MB':N*2/8/1e6}

# ---- 3 budgets ------------------------------------------------------------
D['budget']={'coordinate':Rsz-occ,'ignorance':150630700,'contingent':3*N,
             'obs_snv':786500648,'field':8892915237,'N':N}
D['budget']['occupancy']=786500648/(3*N)
D['budget']['ign_frac']=150630700/((Rsz-occ)+150630700+3*N)

# ---- 4 kmer crossing ------------------------------------------------------
D['kmer']={'k':list(range(10,23)),'alpha':[4**k for k in range(10,23)],
           'length':[N-k+1 for k in range(10,23)],'kstar':math.log(N,4),
           'first_int':min(k for k in range(10,40) if 4**k>=N-k+1)}

# ---- 5 pangenome: sum does not obstruct ----------------------------------
H,A=12,4
comps=[c for c in product(range(1,H),repeat=A) if sum(c)==H]
byE={}
for c in comps: byE.setdefault(E([(a,x) for a,x in enumerate(c)]),[]).append(c)
D['pan']={'ncomp':len(comps),'byE':{str(k):len(v) for k,v in sorted(byE.items())},
  'nmono':sum(1 for c in comps if list(c)==sorted(c)),
  'mono_E':sorted({E([(a,x) for a,x in enumerate(c)]) for c in comps if list(c)==sorted(c)}),
  'invariance':[{'H':h,'c':[h-6,2,3,1],'E':E([(a,x) for a,x in enumerate([h-6,2,3,1])])} for h in (12,40,400)],
  'withH':E([(a,x,12) for a,x in enumerate([6,2,3,1])]),'withoutH':E([(a,x) for a,x in enumerate([6,2,3,1])])}

# ---- 6 lemma test ---------------------------------------------------------
random.seed(5); mnz=nmz=0; T=4000
for _ in range(T):
    v=[random.randint(1,9) for _ in range(random.randint(2,7))]
    e=E([(i,x) for i,x in enumerate(v)]); mono=(v==sorted(v))
    if mono and e!=0: mnz+=1
    if (not mono) and e==0: nmz+=1
D['lemma']={'trials':T,'mono_nonzero':mnz,'nonmono_zero':nmz}

# ---- 7 snarl tower --------------------------------------------------------
Dl=28; Hh=94
Av=[max(2,round(Hh**(u/Dl))) for u in range(Dl+1)]
cells=[(u,a) for u,Au in enumerate(Av) for a in range(Au)]
rev=[(u,a) for u,Au in enumerate(Av[::-1]) for a in range(Au)]
D['snarl']={'D':Dl,'H':Hh,'A':Av,'occ':sum(Av),'box':(Dl+1)*max(Av),
  'density':sum(Av)/((Dl+1)*max(Av)),'E_height':E(cells),'E_level':E(rev),
  'dup':[{'f':f,'distinct':sum(Av)-int(f*sum(Av)),'reported':sum(Av),'over':int(f*sum(Av))} for f in (0.05,0.10,0.20)]}

json.dump(D,open('/home/claude/paper/data.json','w'),indent=1)
print("computed. keys:",list(D))
for k in ('chrom','budget','snarl','lemma'):
    print(f"  {k}: ", {kk:vv for kk,vv in D[k].items() if not isinstance(vv,(list,dict))})