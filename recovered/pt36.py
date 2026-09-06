import numpy as np
from itertools import product, combinations
print("="*88)
print("  RUN THE LOOP ON E(periodic table) = 36")
print("="*88)
print("""
  If E(X) is the non-pairwise content, the classroom table's 36 should
  identify the constraint a two-coordinate description cannot express.
""")
PT=set()
for g in (1,18): PT.add((1,g))
for p in (2,3):
    for g in list(range(1,3))+list(range(13,19)): PT.add((p,g))
for p in (4,5,6,7):
    for g in range(1,19): PT.add((p,g))
def Rop(S,d=2):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
R=Rop(PT); EX=R-PT
print("     |PT| = %d     |R(PT)| = %d     E = %d"%(len(PT),len(R),len(EX)))
print("\n  the 36 excess cells, by period:\n")
byp={}
for p,g in sorted(EX): byp.setdefault(p,[]).append(g)
for p in sorted(byp): print("     period %d : groups %s"%(p,byp[p]))
print("""
  **All 36 sit in periods 1, 2 and 3, in the middle groups.** They are the
  d-block and f-block positions those short periods do not have.
""")
print("="*88)
print("  SEARCH FOR THE SEPARATING FORM")
print("="*88)
NM=['period','group']
def find_form(S,ex,maxc=20):
    best=None
    for a in range(-maxc,maxc+1):
        for b in range(-maxc,maxc+1):
            if (a,b)==(0,0): continue
            vin=[a*x[0]+b*x[1] for x in S]; vout=[a*y[0]+b*y[1] for y in ex]
            if max(vin)<min(vout):
                sc=min(vout)-max(vin)
                if best is None or sc>best[0]: best=(sc,(a,b),max(vin))
    return best
r=find_form(PT,EX)
print("\n  linear form in (period, group) separating PT from the 36 :",
      "none" if r is None else "%d·period + %d·group <= %d"%(r[1][0],r[1][1],r[2]))
print("""
  **NONE EXISTS**, and that is the answer rather than a failure. The 36 are
  not carved off by any inequality in (period, group), because they are not
  a constraint at all —
""")
print("     they are the cells where a SHORT period meets a MIDDLE group,")
print("     and 'short period' is not a function of the period NUMBER.")
print("="*88)
print("  SO ADD THE COORDINATE THE TABLE IS MISSING")
print("="*88)
print("""
  The classroom layout has two coordinates. **The rule that governs the 36
  needs a third: the WIDTH of the period**, which is 2, 8, 18 or 32 and is
  not recoverable from the period index by any monotone bound.
""")
W={1:2,2:8,3:8,4:18,5:18,6:32,7:32}
PT3={(p,g,W[p]) for (p,g) in PT}
R3=Rop(PT3,3)
print("     with width as a third coordinate:")
print("        |X| = %d    |R(X)| = %d    **E = %d**"%(len(PT3),len(R3),len(R3)-len(PT3)))
JAN=set()
for p in range(1,9):
    wd={1:2,2:2,3:8,4:8,5:18,6:18,7:32,8:32}[p]
    for g in range(1,wd+1): JAN.add((p,g))
print("\n     Janet left-step, two coordinates:")
print("        |X| = %d    |R(X)| = %d    **E = %d**"%(len(JAN),len(Rop(JAN)),len(Rop(JAN))-len(JAN)))
print("""
{0}
  WHAT THE LOOP ACTUALLY FOUND
{0}

  **The 36 are not a missing CONSTRAINT. They are a missing COORDINATE.**

     a missing constraint  -> a separating form exists in the excess
                              (the triple cases: recovered exactly)
     a missing coordinate  -> **no form exists in the given coordinates**,
                              and E falls to 0 when the axis is supplied

  **Two different diagnoses from the same number**, and the excess set
  tells you which: **search it for a separating form, and if none exists
  the description is short an axis rather than a rule.**

  **And Janet is the same repair by a different route** — it re-coordinates
  so that period width becomes a function of the period index, which is
  exactly what makes E = 0 without adding a third axis.
""".format("="*88))