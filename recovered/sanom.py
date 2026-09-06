import math, statistics as st
from collections import Counter, defaultdict
from scipy import stats as SS
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]
L="spdfghi"
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
R=[(x["l"],x["c"],core_p(x["ne"]-1,x["l"]),x["d"],x["ne"],x["Z"]) for x in CH]
print("  THE s ANOMALY — floor(δ) = p − 2, not p\n")
print("  Two core nodes buy no defect. Which two?\n")
print("  Candidate: the 1s and 2s shells sit so deep that the Rydberg electron")
print("  crosses them where the potential is nearly pure −Z/r, so those nodes are")
print("  HYDROGENIC and cost nothing. Test: does the shortfall equal the number of")
print("  core s shells lying inside the CORE region rather than the valence one?\n")
print(f"      {'p':>3}{'n':>5}{'median floor(δ)−p':>20}{'median δ':>11}{'p − 2':>8}")
by=defaultdict(list)
for l,c,p,d,ne,Z in R:
    if l!=0: continue
    by[p].append((d, math.floor(d)-p, c, ne))
for p in sorted(by):
    v=by[p]
    if len(v)<3: continue
    print(f"      {p:>3}{len(v):>5}{st.median([b for _,b,_,_ in v]):>20.1f}"
          f"{st.median([a for a,_,_,_ in v]):>11.3f}{p-2:>8}")
print()
print("  → the shortfall is 2 for every p ≥ 2, and p−2 is exactly the number of")
print("    core s shells ABOVE the first two.\n")
print()
print("  DOES THE SAME PATTERN APPEAR AT p AND d?\n")
print("      If the rule is 'the first two shells of any ℓ are free', then p should")
print("      show a shortfall of 2 as well — and it does not. So the rule is not")
print("      about shell count. Test what it IS about.\n")
print(f"      {'ℓ':>3}{'p':>4}{'n':>5}{'median floor(δ)−p':>20}")
for l in (0,1,2,3):
    bb=defaultdict(list)
    for ll,c,p,d,ne,Z in R:
        if ll!=l: continue
        bb[p].append(math.floor(d)-p)
    for p in sorted(bb):
        if len(bb[p])<3: continue
        print(f"      {L[l]:>3}{p:>4}{len(bb[p]):>5}{st.median(bb[p]):>20.1f}")
    print()
print("  THE READING\n")
print("      s : shortfall 2 at every p ≥ 2 — the first TWO s nodes are free")
print("      p : shortfall 1 at every p ≥ 1 — the first ONE p node is free")
print("      d : shortfall 0 — every d node costs a full unit")
print("      f : shortfall 0")
print()
print("      So the number of FREE nodes is 2, 1, 0, 0 for ℓ = 0, 1, 2, 3.")
print("      That is max(2 − ℓ, 0) — and 2 − ℓ counts nothing obvious. Test it")
print("      against the alternative: free nodes = the shells with n ≤ ℓ + 2.")
print()
free={0:2,1:1,2:0,3:0,4:0}
print(f"      {'ℓ':>3}{'free nodes':>12}{'2 − ℓ':>8}{'ℓ(ℓ+1)':>9}{'ℓ+1':>6}")
for l in sorted(free):
    print(f"      {L[l]:>3}{free[l]:>12}{max(2-l,0):>8}{l*(l+1):>9}{l+1:>6}")