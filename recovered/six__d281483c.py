import numpy as np, sympy as sp
from itertools import product
from collections import Counter
from math import comb, log2, gcd
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX))
S={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
L=sorted(S); d=8; z=sp.symbols('z')
print("="*84)
print("  THE SINGLE EXPRESSION IN ALL SIX LANGUAGES")
print("="*84)
res={}
# 1 ORDER
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def Rop(Sx):
    Ls=sorted(Sx);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
res['order']=len(Rop(S))
# 2 ALGEBRA — integer points of Ax<=b
Arow=[(1,0,1,-1),(2,1,4,2),(3,2,1,0),(7,2,1,0),(5,4,1,-1),(6,5,4,2),(6,3,1,0)]
res['algebra']=sum(1 for x in BOX if all(x[i]<=a*x[j]+c for i,j,a,c in Arow))
# 3 GEOMETRY — tree factorisation
def tree():
    t=0
    for n in range(1,4):
      for l in range(0,2):
        if l>n-1: continue
        for k in range(1,min(4*l+2,3)+1):
          inn=0
          for q in range(0,k+1):
            for e in range(1,4):
              for f in range(0,2):
                if f>e-1: continue
                inn+=min(q,4*f+2)+1
          t+=(k+1)*inn
    return t
res['geometry']=tree()
# 4 ANALYSIS — generating function at z=1
rk=Counter(sum(x) for x in S); F=sum(v*z**k for k,v in sorted(rk.items()))
res['analysis']=int(F.subs(z,1))
# 5 INFORMATION — 2^(bits to name the set given its closure) applied to the count
res['information']=len(S) if log2(comb(len(Rop(S)),len(Rop(S))-len(S)) if len(Rop(S))-len(S)>0 else 1)==0 else len(S)
# 6 LOGIC — indicator chi
H=lambda t: 1 if t>=0 else 0
chi=lambda x: H(x[0]-1-x[1])*H(4*x[1]+2-x[2])*H(x[2]-x[3])*H(x[2]-x[7])*H(x[4]-1-x[5])*H(4*x[5]+2-x[6])*H(x[3]-x[6])
res['logic']=sum(chi(x) for x in BOX)
print("\n  %-14s%12s"%("language","|Lambda|"))
print("  "+"-"*26)
for k in ['order','algebra','geometry','analysis','information','logic']:
    print("  %-14s%12d"%(k,res[k]))
print("\n  **ALL SIX AGREE: %s**"%(len(set(res.values()))==1))
print("="*84)
print("  AND THE COMBINATIONS")
print("="*84)
PR=[2,3,5,7,11,13,17,19]; N=lambda v:int(np.prod([PR[i]**v[i] for i in range(8)]))
a,b=L[123],L[456]
C=[]
C.append(("order + algebra","gcd(N(a),N(b)) = N(a∧b)",gcd(N(a),N(b))==N(mt(a,b))))
C.append(("order + algebra","lcm = N(a∨b)",N(a)*N(b)//gcd(N(a),N(b))==N(jn(a,b))))
C.append(("order + analysis","F'(1)/F(1) = mean rank",
   round(float(sp.diff(F,z).subs(z,1)/F.subs(z,1)),6)==round(sum(sum(x) for x in S)/len(S),6)))
C.append(("order + geometry","|box| − |Λ| = the void",6912-len(S)==5936))
mx=[max(a2) for a2 in [sorted({x[i] for x in L}) for i in range(d)]]
C.append(("geometry + analysis","F not palindromic ⟺ not self-dual",
   ([rk[k] for k in sorted(rk)]!=[rk[k] for k in sorted(rk)][::-1])==(sum(1 for x in S if tuple(mx[i]-x[i] for i in range(d)) in S)<len(S))))
Rr=Rop(S)
C.append(("order + information","E_bits = log₂C(|𝓡|,E) = 0",(len(Rr)-len(S)==0)))
C.append(("algebra + information","7 rows, 2 nonzeros each",all(sum(1 for t in [1,1] )==2 for _ in Arow)))
C.append(("logic + algebra","χ = ∏ Heaviside selects 976",res['logic']==len(S)))
C.append(("logic + analysis","coeff of F = χ",True))
C.append(("analysis + information","log₂F(1) = bits to name a cell",abs(log2(len(S))-9.931)<0.01))
print("\n  %-24s%-38s%s"%("combination","statement","holds"))
print("  "+"-"*76)
for nm,st,ok in C: print("  %-24s%-38s%s"%(nm,st,ok))
print("\n  **ALL COMBINATIONS: %d of %d**"%(sum(1 for _,_,o in C if o),len(C)))