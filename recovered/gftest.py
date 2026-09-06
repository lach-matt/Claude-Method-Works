import sympy as sp, pickle, math
from fractions import Fraction as F
y=sp.symbols('y')
G=pickle.load(open('/home/claude/stage/gf.pkl','rb'))
A=G['A']; NUMC=G['NUM']
def series_from_gf(r,upto):
    P=sum(NUMC[r][k]*y**k for k in range(len(NUMC[r])))
    f=sp.series(P/(1-y)**(2*r-1),y,0,upto+1).removeO()
    return [int(sp.Poly(sp.expand(f),y).coeff_monomial(y**k)) for k in range(1,upto+1)]
def monos(k,hi):
    out=[]
    def rec(i,last,acc):
        if i==k: out.append(tuple(acc)); return
        for v in range(last,hi):
            acc.append(v); rec(i+1,v,acc); acc.pop()
    rec(0,-1,[])
    return out
def a_direct(r,c):
    M=monos(r,c); N=monos(c,r)
    ROWM=[]
    for m in M:
        mk=0
        for i in range(r):
            if m[i]>=0: mk |= ((1<<(m[i]+1))-1) << (i*c)
        ROWM.append(mk)
    COLM=[]
    for nn in N:
        mk=0
        for j in range(c):
            if nn[j]>=0:
                for i in range(nn[j]+1): mk |= 1<<(i*c+j)
        COLM.append(mk)
    fr=[(1<<(i*c+c))-(1<<(i*c)) for i in range(r)]
    fc=[sum(1<<(i*c+j) for i in range(r)) for j in range(c)]
    seen=set()
    for rm in ROWM:
        if rm==0: continue
        for cm in COLM:
            S=rm & cm
            if S==0: continue
            if all(S & x for x in fr) and all(S & x for x in fc): seen.add(S)
    return len(seen)
print("="*88)
print("  TEST 1 — EXTRAPOLATION  (a prediction test)")
print("="*88)
print("""
  **The GF was built from values up to c = 14 for r ≤ 4 and c = 9 for r = 5.
  Ask it for values it was never given, and compute those directly.**
""")
print("  %8s%14s%16s%10s"%("a(r,c)","from the GF","computed direct","match"))
print("  "+"-"*52)
ok1=bad1=0
for r,c in [(2,15),(2,18),(3,12),(3,15),(4,11),(5,10),(5,11)]:
    s=series_from_gf(r,max(c,20))
    pred=s[c-1]
    if r*c<=60:
        act=a_direct(r,c)
        m=(pred==act); ok1+=m; bad1+= (not m)
        print("  %8s%14d%16d%10s"%("a(%d,%d)"%(r,c),pred,act,"YES" if m else "**NO**"))
    else:
        print("  %8s%14d%16s%10s"%("a(%d,%d)"%(r,c),pred,"too large","—"))
print("\n     extrapolation : %d correct, %d wrong"%(ok1,bad1))
print("="*88)
print("  TEST 2 — SYMMETRY  (a structural test, not a value test)")
print("="*88)
print("""
  **a(r,c) = a(c,r) is a property of the object, not of the fit.** The GFs
  were built row by row with no symmetry imposed. **If they respect it, they
  encode the object rather than the data.**
""")
print("  %14s%14s%14s%10s"%("pair","a(r,c)","a(c,r)","match"))
print("  "+"-"*54)
ok2=bad2=0
for r,c in [(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(3,2),(5,2)]:
    sr=series_from_gf(r,20); sc=series_from_gf(c,20)
    v1=sr[c-1]; v2=sc[r-1]
    m=(v1==v2); ok2+=m; bad2+=(not m)
    print("  %14s%14d%14d%10s"%("(%d,%d)"%(r,c),v1,v2,"YES" if m else "**NO**"))
print("\n     symmetry : %d of %d"%(ok2,ok2+bad2))
print("="*88)
print("  TEST 3 — THE BOX IDENTITY  (a test against a different quantity)")
print("="*88)
print("""
  **N(R,C) = Σ C(R,r)C(C,c)a(r,c) was verified against direct enumeration.
  Feed the GF's values into it and compare with the known box counts** —
  a test against a quantity the GF was never fitted to.
""")
KNOWN={(2,2):12,(2,3):37,(3,3):146,(2,4):103,(3,4):505,(4,4):2102,(5,5):34087,(4,5):7886}
print("  %10s%14s%16s%10s"%("box","from the GF","known N(R,C)","match"))
print("  "+"-"*52)
ok3=bad3=0
SER={r:series_from_gf(r,20) for r in range(1,6)}
for (R,C),v in sorted(KNOWN.items()):
    s=0
    for r in range(1,R+1):
        for c in range(1,C+1):
            s+=math.comb(R,r)*math.comb(C,c)*SER[r][c-1]
    m=(s==v); ok3+=m; bad3+=(not m)
    print("  %10s%14d%16d%10s"%("%dx%d"%(R,C),s,v,"YES" if m else "**NO**"))
print("\n     box identity : %d of %d"%(ok3,ok3+bad3))
print("="*88)
print("  RESULT")
print("="*88)
print("""
     Test 1  extrapolation to unseen c : %d / %d
     Test 2  symmetry a(r,c)=a(c,r)    : %d / %d
     Test 3  the box identity N(R,C)   : %d / %d
"""%(ok1,ok1+bad1,ok2,ok2+bad2,ok3,ok3+bad3))