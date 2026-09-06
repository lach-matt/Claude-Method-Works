import math
src=open("madelung2.py",encoding="utf-8").read()
src=src[:src.index('# ---------------------------------------------------------------- the test')]
g={}; exec(src,g)
config=g["config"]; core_p=g["core_p"]; delta=g["delta"]; ORDER=g["ORDER"]
L="spdfg"
def n0_of(ne,l): return core_p(ne,l)+l+1
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for a,b,o in cfg:
        if a==n and b==l: return o
    return 0
print("  THE CORRECT TEST — at each Z, which subshell receives the electron?\n")
print("  Aufbau fills the subshell in n+ℓ order. The equation says the one with the")
print("  smallest n* = n − δ among those not yet full. Do they pick the same one?\n")
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z
    cfg=config(ne-1)                       # the core: Z-1 electrons
    # candidates: every (n,l) not yet full, reachable
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(cfg,n,l)>=cap(l): continue
        # only the first available n for this l is a real candidate
        if n!=n0_of(ne-1,l) and occ(cfg,n,l)==0: continue
        d=delta(Z,1,l)
        cand.append((n,l,d,n-d))
    if len(cand)<2: continue
    # what aufbau actually does
    full=config(ne)
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(cfg,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[3])
    if (pick[0],pick[1])==got: ok+=1
    else:
        bad+=1
        BAD.append((Z,got,pick,cand))
print(f"      elements       : {ok+bad}")
print(f"      equation picks the aufbau subshell : {ok}  ({100*ok/(ok+bad):.1f}%)")
print(f"      picks a different one              : {bad}")
print()
if BAD:
    from collections import Counter
    print("      by the pair confused:")
    c=Counter((f"{g_[0]}{L[g_[1]]}", f"{p[0]}{L[p[1]]}") for _,g_,p,_ in BAD)
    for (a,b),v in c.most_common(10): print(f"          aufbau {a}, equation {b}: {v}")
    print()
    print(f"      {'Z':>4}{'aufbau':>9}{'equation':>10}{'n* aufbau':>11}{'n* eq':>9}")
    for Z,g_,p,cand in BAD[:16]:
        na=[x for x in cand if (x[0],x[1])==g_]
        print(f"      {Z:>4}{f'{g_[0]}{L[g_[1]]}':>9}{f'{p[0]}{L[p[1]]}':>10}"
              f"{(na[0][3] if na else float('nan')):>11.3f}{p[3]:>9.3f}")