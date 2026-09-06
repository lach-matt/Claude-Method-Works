import lam8
from collections import Counter, defaultdict
from itertools import product as iprod
L8=lam8.L8()

# ---- MC-19: full polynomial identities per q ----
print("== MC-19 ==")
ok_all=True
for q in range(4):
    # enumerated A(q): distinct (n,l,k,2S) from cells with this q
    Aset={(x[0],x[1],x[2],x[7]) for x in L8 if x[3]==q}
    Bset={(x[4],x[5],x[6]) for x in L8 if x[3]==q}
    encA=Counter(sum(t) for t in Aset)
    encB=Counter(sum(t) for t in Bset)
    # closed forms
    cfA=Counter()
    for n in range(1,4):
        for l in range(0,min(n-1,1)+1):
            for k in range(max(q,1),min(4*l+2,3)+1):
                for s in range(0,min(k,3)+1):
                    cfA[n+l+k+s]+=1
    cfB=Counter()
    for e in range(1,4):
        for f in range(0,min(e-1,1)+1):
            for g in range(0,min(q,4*f+2)+1):
                cfB[e+f+g]+=1
    okA = encA==cfA; okB = encB==cfB
    ok_all &= okA and okB
    print(f"q={q}: A poly identity {okA} (A_q(1)={sum(cfA.values())})  B poly identity {okB} (B_q(1)={sum(cfB.values())})")
print("polynomial identities all q:", ok_all)

# fibration levels as exact products
def is_product(cells, split):
    left={split(c)[0] for c in cells}; right={split(c)[1] for c in cells}
    return cells=={(a+b if isinstance(a,tuple) else None) for a in left for b in right} if False else \
           cells=={l+r for l in left for r in right}
lvl_ok=True
for q in range(4):
    Aset={(x[0],x[1],x[2],x[7]) for x in L8 if x[3]==q}
    byk=defaultdict(set)
    for (n,l,k,s) in Aset: byk[k].add((n,l,k,s))
    for k,cells in byk.items():
        nl={(n,l) for (n,l,_,s) in cells}; ss={(s,) for (_,_,_,s) in cells}
        prod={(n,l,k,s[0]) for (n,l) in nl for s in ss}
        if prod!=cells: lvl_ok=False; print(f"A_q={q} k={k} NOT product")
    Bset={(x[4],x[5],x[6]) for x in L8 if x[3]==q}
    byf=defaultdict(set)
    for (e,f,g) in Bset: byf[f].add((e,f,g))
    for f,cells in byf.items():
        es={e for (e,_,_) in cells}; gs={g for (_,_,g) in cells}
        prod={(e,f,g) for e in es for g in gs}
        if prod!=cells: lvl_ok=False; print(f"B_q={q} f={f} NOT product")
print("fibration levels exact products (A over k, B over f, all q):", lvl_ok)

# ---- MC-20: modular law + distributivity per slice; S'(1)/S(1) exact ----
print("\n== MC-20 ==")
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def leq(a,b): return all(x<=y for x,y in zip(a,b))
tot_mod=0; tot_dist=0; fail=0
for q in range(4):
    for cells in ({(x[0],x[1],x[2],x[7]) for x in L8 if x[3]==q},
                  {(x[4],x[5],x[6]) for x in L8 if x[3]==q}):
        L=list(cells)
        for x in L:
            for a in L:
                for b in L:
                    # distributive law
                    tot_dist+=1
                    if mt(x,jn(a,b))!=jn(mt(x,a),mt(x,b)): fail+=1
                    # modular law where x<=b
                    if leq(x,b):
                        tot_mod+=1
                        if jn(x,mt(a,b))!=mt(jn(x,a),b): fail+=1
print(f"distributive law: {tot_dist} triples, modular law: {tot_mod} conditioned triples, failures: {fail}")
from fractions import Fraction
S1=Fraction(165+330+345+136); Sp1=Fraction(0*165+1*330+2*345+3*136)
print("S'(1)/S(1) =", Sp1, "/", S1, "=", float(Sp1/S1))
print("peak share 345/976 =", round(100*345/976,1), "%")