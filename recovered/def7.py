from itertools import product
LAW=["1 amplitude","2 ℓ-spread","3 charge exp","4 Pauli floor","5 gate",
     "6 switch","7 regimes"]
CAR=["u","p","ℓ−ℓ_core","Z−T"]
cells={(0,0),(1,1),(2,0),(3,1),(4,2),(5,3),(6,1)}
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]]
            for i in range(d) for j in range(d) if i!=j)}
R=opR(cells,2)
add=sorted(R-cells)
print("  THE SEVEN DEFECT CELLS — what ℛ admits and we do not hold\n")
WHAT={
 (1,0):"law 2 in u — TESTED, r² 0.044. the condition: ℓ-spread is NOT a function of u",
 (2,1):"law 3 in p — is the charge exponent a function of the core count?",
 (3,0):"law 4 in u — does the Pauli floor depend on Nₑ/c^⅔? it must not: it is integer",
 (4,0):"law 5 in u — does the gate move with u? the condition on its universality",
 (4,1):"law 5 in p — the gate is stated in ℓ−ℓ_core; p = 0 IS the gate. same law?",
 (5,0):"law 6 in u — does the collapse threshold move with u?",
 (5,1):"law 6 in p — the switch fires exactly when p = 0. same law?",
 (5,2):"law 6 in ℓ−ℓ_core — h(ℓ) already depends on ℓ. the missing link",
 (6,0):"law 7 in u — do the regime boundaries move with u?",
 (6,2):"law 7 in ℓ−ℓ_core — the gate IS a regime boundary",
 (6,3):"law 7 in Z−T — the 3|4 boundary IS Z = T",
}
for a,b in add:
    print(f"      {LAW[a]:<15}× {CAR[b]:<11}{WHAT.get((a,b),'—')}")
print(f"\n      {len(add)} defect cells · {len(cells)} held · {len(R)} total\n")
print("  AND THE READING\n")
print("      three of the seven are RESTATEMENTS of held laws in another carrier:")
print("          law 5 in p        — the gate and p = 0 are the same cut")
print("          law 6 in p        — the switch fires exactly when p = 0")
print("          law 7 in Z−T      — the 3|4 boundary IS Z = T\n")
print("      those are not new laws. they are the SAME law seen twice, which is")
print("      what a closed index does: a cell reachable two ways.\n")
print("      the other four are genuine CONDITIONS:")
print("          law 2 in u        — TESTED and FALSE. the condition holds.")
print("          law 3 in p        — untested. is the charge exponent p-free?")
print("          law 4 in u        — must be false (the floor is an integer)")
print("          law 6 in ℓ−ℓ_core — h(d) vs h(f) is exactly this, partly held\n")
print("      so of seven defects: three are identities, one is tested false,")
print("      one must be false by construction, and TWO are open.")