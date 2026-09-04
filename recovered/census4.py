import numpy as np, random, math, sys
from itertools import product, permutations, combinations
random.seed(467)
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=S
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d,cap=3*10**5):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def canon(S,d):
    A=alph(S,d); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        T=tuple(sorted(relab(S,[list(p) for p in ps],d)))
        if best is None or T<best: best=T
    return best
def minimal(S,d):
    if reord(S,d) is not False: return False
    for z in sorted(S):
        T=S-{z}; A=alph(T,d)
        if any(len(x)<2 for x in A): continue
        if reord(T,d) is False: return False
    return True
print("="*86)
print("  THE THREE MISSES — WHAT ARE THEY?")
print("="*86)
Ax=[list(range(4)) for _ in range(3)]
cl=list(product(*Ax))
# rebuild the 3x3x3 census
A3=[list(range(3)) for _ in range(3)]
c3=list(product(*A3))
CS=set()
for k in (3,4,5):
    for T in combinations(c3,k):
        S=set(T); Aa=alph(S,3)
        if any(len(x)<2 for x in Aa): continue
        if reord(S,3) is not False: continue
        if minimal(S,3): CS.add(canon(S,3))
print("\n     3×3×3 census : %d obstructions"%len(CS))
def has_obs(S,d,ks=(3,4,5)):
    for k in ks:
        for T in combinations(sorted(S),k):
            Ts=set(T); Aa=alph(Ts,d)
            if any(len(x)<2 for x in Aa): continue
            if canon(Ts,d) in CS: return True
    return False
misses=[]
tries=0
while len(misses)<6 and tries<4000:
    tries+=1
    S=set(random.sample(cl,random.randint(3,7)))
    Aa=alph(S,3)
    if any(len(x)<2 for x in Aa): continue
    r=reord(S,3)
    if r is not False: continue
    if not has_obs(S,3): misses.append(S)
print("     misses collected : %d  (from %d draws)"%(len(misses),tries))
print("\n  the misses, and their minimal cores:\n")
newobs={}
for S in misses[:6]:
    core=None
    for k in range(3,len(S)+1):
        for T in combinations(sorted(S),k):
            Ts=set(T); Aa=alph(Ts,3)
            if any(len(x)<2 for x in Aa): continue
            if reord(Ts,3) is False and minimal(Ts,3): core=Ts; break
        if core: break
    print("     %d cells : %s"%(len(S),sorted(S)))
    if core:
        c=canon(core,3)
        newobs.setdefault(c,core)
        print("        minimal core (%d cells) : %s"%(len(core),sorted(core)))
        print("        alphabets of the core   : %s"%[len(a) for a in alph(core,3)])
    else:
        print("        no minimal core found within it")
print("="*86)
print("  ARE THE NEW CORES BIGGER, OR JUST WIDER?")
print("="*86)
print("""
  **The distinguishing question.** If the new obstructions have ≤5 cells but
  need alphabets of size 4, the census grows with |A| and not with cell
  count — **so a bounded-cell census can never be complete.**
""")
if newobs:
    print("\n  %10s%16s%s"%("cells","alphabets","obstruction"))
    print("  "+"-"*66)
    for c,S in newobs.items():
        print("  %10d%16s  %s"%(len(S),[len(a) for a in alph(S,3)],str(sorted(S))[:40]))
    sizes=[len(S) for S in newobs.values()]
    alfs=[max(len(a) for a in alph(S,3)) for S in newobs.values()]
    print("\n     cell sizes  : %s"%sorted(set(sizes)))
    print("     max alphabet: %s"%sorted(set(alfs)))
    if max(sizes)<=5 and max(alfs)>3:
        print("""
  > **The new obstructions are SMALL in cells and WIDE in alphabet.** So the
  > obstruction set is not bounded by cell count — it grows with the
  > alphabet, and no finite forbidden-substructure theorem in cells alone
  > can decide the problem.""")
    elif max(sizes)>5:
        print("""
  > **The new obstructions are LARGER in cells.** The census must go deeper,
  > and whether it terminates is still open.""")