import time
from fractions import Fraction as F
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def a_fast(r,c):
    """canonical closed-set count, bitmask representation"""
    M=monos(r,c); N=monos(c,r)
    # precompute row masks for each M: bits j<=m[i] in row i
    ROWM=[]
    for m in M:
        mk=0
        for i in range(r):
            if m[i]>=0:
                mk |= ((1<<(m[i]+1))-1) << (i*c)
        ROWM.append(mk)
    COLM=[]
    for nn in N:
        mk=0
        for j in range(c):
            if nn[j]>=0:
                for i in range(nn[j]+1): mk |= 1<<(i*c+j)
        COLM.append(mk)
    full_rows=[(1<<(i*c+c))-(1<<(i*c)) for i in range(r)]
    full_cols=[sum(1<<(i*c+j) for i in range(r)) for j in range(c)]
    seen=set()
    for rm in ROWM:
        if rm==0: continue
        for cm in COLM:
            S=rm & cm
            if S==0: continue
            ok=True
            for fr in full_rows:
                if not (S & fr): ok=False; break
            if not ok: continue
            for fc in full_cols:
                if not (S & fc): ok=False; break
            if ok: seen.add(S)
    return len(seen)
print("="*84)
print("  a(5,c) — THE NEXT ROW")
print("="*84)
t0=time.time()
row5=[]
for c in range(1,10):
    v=a_fast(5,c); row5.append(v)
    print("     a(5,%d) = %-10d   %.1fs"%(c,v,time.time()-t0))
print("\n     a(5,c) =",row5)
d=row5[:]; k=0
while len(set(d))>1 and len(d)>1 and k<10:
    d=[d[i+1]-d[i] for i in range(len(d)-1)]; k+=1
    print("        Δ^%d : %s"%(k,d))
if len(set(d))==1: print("        **degree %d, Δ^%d = %s**"%(k,k,d[0]))
def fit(vals,deg):
    n=deg+1
    A=[[F(c**kk) for kk in range(n)] for c in range(1,n+1)]
    b=[F(v) for v in vals[:n]]
    M=[A[i][:]+[b[i]] for i in range(n)]
    for i in range(n):
        p=next(j for j in range(i,n) if M[j][i]!=0)
        M[i],M[p]=M[p],M[i]
        pv=M[i][i]; M[i]=[x/pv for x in M[i]]
        for j in range(n):
            if j!=i and M[j][i]!=0:
                f=M[j][i]; M[j]=[M[j][t]-f*M[i][t] for t in range(n+1)]
    return [M[i][n] for i in range(n)]
if len(row5)>=9:
    co=fit(row5,8)
    pred=[sum(co[kk]*F(c**kk) for kk in range(9)) for c in range(1,len(row5)+1)]
    print("\n     degree-8 fit exact on all %d : %s"%(len(row5),all(pred[i]==row5[i] for i in range(len(row5)))))
    print("     leading coefficient : %s      1/lead = %s"%(co[8],1/co[8] if co[8] else "—"))
print("="*84)
print("  THE LEADING DENOMINATORS")
print("="*84)
L=[1,2,12,144]
if len(row5)>=9 and co[8]:
    L.append(int(1/co[8]))
print("\n     r      : 1  2   3    4     5")
print("     1/lead : %s"%("  ".join(str(x) for x in L)))
print("     ratios : %s"%["%s"%(F(L[i+1],L[i])) for i in range(len(L)-1)])
import math
print("\n     compare (r-1)!^2 :",[math.factorial(r-1)**2 for r in range(1,len(L)+1)])
print("     compare  (2r-2)! :",[math.factorial(2*r-2) for r in range(1,len(L)+1)])
print("     compare 2^(r-1)·(r-1)! :",[2**(r-1)*math.factorial(r-1) for r in range(1,len(L)+1)])