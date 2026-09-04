from itertools import combinations
from lam8 import L8

def build(capn,cape,capl,capk,capf):
    out=[]
    for n in range(1,capn+1):
      for l in range(0,min(capl,n-1)+1):
        for k in range(1,min(capk,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,cape+1):
              for f in range(0,min(capf,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,k+1):
                    out.append((n,l,k,q,e,f,g,S2))
    return out

# coordinate order: 0 n,1 l,2 k,3 q,4 e,5 f,6 g,7 2S
# seven constraints as hi_i <= phi(lo_j)
CONS=[('l<=n-1',   lambda lo,hi: hi[1] <= lo[0]-1),
      ('k<=2(2l+1)',lambda lo,hi: hi[2] <= 4*lo[1]+2),
      ('q<=k',     lambda lo,hi: hi[3] <= lo[2]),
      ('g<=q',     lambda lo,hi: hi[6] <= lo[3]),
      ('g<=2(2f+1)',lambda lo,hi: hi[6] <= 4*lo[5]+2),
      ('f<=e-1',   lambda lo,hi: hi[5] <= lo[4]-1),
      ('2S<=k',    lambda lo,hi: hi[7] <= lo[2])]

def rates(cells):
    n=len(cells); tot=0
    cnt=[0]*7; joint=0
    for a,b in combinations(cells,2):
        lo=tuple(min(u,v) for u,v in zip(a,b))
        hi=tuple(max(u,v) for u,v in zip(a,b))
        tot+=1
        ok=True
        for i,(nm,f) in enumerate(CONS):
            r=f(lo,hi)
            if r: cnt[i]+=1
            else: ok=False
        if ok: joint+=1
    return tot,cnt,joint

cells=L8()
tot,cnt,joint=rates(cells)
p=[c/tot for c in cnt]
prod=1.0
for v in p: prod*=v
print("pairs",tot)
for (nm,_),v in zip(CONS,p): print(f"  {nm:14s} {v*100:6.2f}%")
print("individual range %.2f%%–%.2f%%"%(min(p)*100,max(p)*100))
print("product %.4f%%"%(prod*100))
print("joint   %.4f%%"%(joint/tot*100))
print("factor  %.4f"%((joint/tot)/prod))
