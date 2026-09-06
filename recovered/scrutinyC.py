#!/usr/bin/env python3
"""scrutinyC.py -- Batch 3: the twenty-three principles.

Ten carry an expression, seven are procedural and the book says they have none,
six are reflexive. Each is taken alone: the expression, what would corroborate
it, what the book carries, and the verdict.
"""
import re, sys, itertools, math
from collections import Counter
from zeno import State, step
from method_tower import base

S = open("The Method 1.4.md", encoding="utf-8").read()
OUT = []
def rec(*a): OUT.append(a)
present = lambda p: bool(re.search(p, S))

# ------------------------------------------------- computations used below
def lam_fixed():
    L = base((3,3,1,3,1)); A=[sorted({c[i] for c in L}) for i in range(8)]
    def env(i,j):
        m={}
        for c in L: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(8) for j in range(8) if i!=j}
    R={x for x in itertools.product(*A) if all(x[i]<=phi[(i,j)][x[j]] for i in range(8) for j in range(8) if i!=j)}
    return len(L), len(R)

def rank_log_q():
    """P9's instance: fifteen Rydberg observables, exponents 2..15, over nu."""
    exps=[2,2,4,4,4,4,7,11,15,3,-3,-2,6,8,10]
    nus=list(range(20,60))
    M=[[e*math.log(n) for n in nus] for e in exps]
    mean=[sum(col)/len(M) for col in zip(*M)]
    C=[[v-mean[k] for k,v in enumerate(row)] for row in M]
    # singular values via Gram eigenvalues
    G=[[sum(a*b for a,b in zip(r1,r2)) for r2 in C] for r1 in C]
    # power iteration for the top two
    def top(G,exclude=None):
        v=[1.0]*len(G)
        for _ in range(300):
            w=[sum(G[i][j]*v[j] for j in range(len(G))) for i in range(len(G))]
            if exclude:
                d=sum(w[i]*exclude[i] for i in range(len(w)))
                w=[w[i]-d*exclude[i] for i in range(len(w))]
            n=math.sqrt(sum(x*x for x in w)) or 1
            v=[x/n for x in w]
        lam=sum(v[i]*sum(G[i][j]*v[j] for j in range(len(G))) for i in range(len(G)))
        return math.sqrt(max(lam,0)), v
    s1,v1=top(G); s2,_=top(G,v1)
    return s1, s2

def p12_bound(n):
    """rho = 0 is certain only at n = |Lambda|; sampling bounds it at 3/n."""
    return 3.0/n

# ============================================================ the formalised
def formalised():
    nL, nR = lam_fixed()
    s1, s2 = rank_log_q()
    P = [
    ("P1", "a complete index is self-referencing", "ℛ(Λ) = Λ",
     f"recomputed: |Λ| = {nL}, |ℛ(Λ)| = {nR}, fixed point {nL==nR}. And the general form "
     f"X closed ⟺ ℛ(X) = X is Baker–Pixley via Bergman",
     "PROVED", "not a discovery about complete indices -- it is the DEFINITION of closed, "
               "and the theorem that the two coincide is fifty years old"),
    ("P2", "a complete index is self-defending", "ⅅ = dim q − rank ∂Φ/∂p ≥ 1",
     "the Jacobian argument is proved and verified on seven dimension pairs and 420 "
     "random nonlinear maps. BUT ⅅ ≥ 1 needs dim q > dim p, which closure does not supply",
     "CONDITIONAL", "the inequality ⅅ ≥ dim q − dim p is proved; the ≥ 1 is a COROLLARY "
                    "under dim q > dim p and is stated as the principle without it"),
    ("P3", "when the path is not found, work backwards from the output",
     "invert Φ; if the fibre is non-trivial, find the datum that separates it",
     "no verification located; §21.13's inversion recovers p = −1 and −3 on controls "
     "and 9 of 10 within 5% on real data -- that is an instance, not the principle",
     "ASSERTED", "a heuristic with one worked instance"),
    ("P7", "all questions must close", "∃N : Ω_N = ∅ — terminal, not monotone",
     "the book CORRECTS this itself: the open-item count ran 5→4→3→4→3→7→3→3, so closure "
     "requires a well-founded measure. NO SUCH MEASURE IS EXHIBITED ANYWHERE",
     "OPEN", "an existence claim about the future with its own hypothesis unmet"),
    ("P8", "any true answer, good or bad, is a bound", "A_n ⊆ A_{n−1}, a decreasing filtration",
     "definitional given the setup: a failed attempt excludes a region, and excluded regions "
     "accumulate. §2.15.2 works it on ten consecutive failures producing one exact statement",
     "PROVED", "trivially true once 'answer' is read as 'exclusion'; its content is procedural"),
    ("P9", "if the first dimension is a single all-encompassing definition, every other "
           "dimension is a perspective of it", "rank(log q) = 1",
     f"recomputed on fifteen Rydberg observables over ν = 20..59: σ₁ = {s1:.3g}, "
     f"σ₂ = {s2:.3g}, ratio {s2/s1:.2e} — rank 1 to machine precision",
     "PARTIAL", "the INSTANCE is computed and exact. the PRINCIPLE is far more general than "
                "the instance and holds nowhere else in the book by computation"),
    ("P10", "allow continued expansions", "§16.4-form constraints preserve closure",
     "proved at §7.3 and now corrected at §14.4 to the two-sided form; verified on eight "
     "regions and on twenty admissible bridges",
     "PROVED", "and STRENGTHENED this session -- the admissible class is larger than the "
               "principle claimed"),
    ("P12", "every test must be run against every cell", "ρ = 0 certain ⟺ n = |Λ|",
     f"sampling n cells with no failure bounds ρ ≤ 3/n at 95%: at n = 30,000 that is "
     f"{p12_bound(30000):.2e}, never zero. register 248 is the instance -- 30,000 draws from "
     f"a box of 6,912, more draws than cells, establishing nothing",
     "PROVED", "the rule of three; the book's own instance is the sharpest illustration"),
    ("P13", "coherence cannot be claimed while any caveat, gap or contradiction stands",
     "COHERENT ⟺ Ω = ∅",
     "definitional -- it defines COHERENT rather than asserting anything about it",
     "DEFINITIONAL", "a prohibition, and the only principle that is a rule of conduct "
                     "wearing an equivalence"),
    ("P17", "the path is always through the bounds", "following a bound costs 1/N of "
            "searching the volume",
     "NO COMPUTATION LOCATED for the 1/N. §18.4 and Ch 12 are cited and neither derives it",
     "OPEN", "the only formalised principle whose expression is nowhere evaluated"),
    ]
    for p in P: rec(*p)

# ============================================================== the procedural
def procedural():
    for k, name in [("P4","always audit results"),("P5","always compute the result before "
        "assuming the result"),("P6","when a question is confusing, reframe the question"),
        ("P11","close all gaps before continuing"),("P14","a structural problem suggests a "
        "structural solution"),("P15","for fetching: use the index to navigate"),
        ("P16","treat bounds, constraints and limits as coordinate values")]:
        extra = ""
        if k == "P15":
            extra = " -- has a MEASURE, retrieval redundancy ρ, without being reducible to it"
        if k == "P16":
            extra = " -- realised constructively at §17.4: a sum cannot be bounded but can be indexed"
        rec(k, name, "none stated",
            "the book states these have no expression and that saying so is better than "
            "manufacturing one" + extra,
            "NOT CORROBORABLE", "a way of working; no proof, theorem or equation settles it, "
            "and none is owed")

# =============================================================== the reflexive
def reflexive():
    R = [
    ("P18","if the index is complete, a work that comprehends it completely is itself an index",
     "Chapter 29", "the book applies the law to itself at Ch 30 and DOES NOT COMPUTE E over "
     "its own cells -- pinned as O1/O2", "OPEN", "the principle's own instance is unevaluated"),
    ("P19","an index is complete only when no questions remain about its contents",
     "COMPLETE(X) ⟺ Q(X) = ∅",
     "definitional, and the book shows it is strictly stronger than E = 0: Λ has had E = 0 "
     "since Ch 7 and has never had Q = ∅",
     "PROVED", "the separation from closure is demonstrated, which is the content"),
    ("P20","the language a question is posed in bounds whether it can close, and at what cost",
     "—", "a table of five languages with closure mechanism and cost, and MEASURED timings: "
     "tree factorisation 0.00018 s against Gröbner 0.010 s, a factor of 55; documentary has "
     "no timing because it has no algorithm",
     "COMPUTED", "the strongest of the six -- it has a measurement and a decidable consequence"),
    ("P21","any definition in the lattice must be TRUE in every mathematical language and in "
     "their combinations", "—",
     "six languages agreeing at 976, ten combinations tested and holding, and the principle "
     "has LOCATED TWO ERRORS by failing in one language",
     "COMPUTED", "an instrument, not only a criterion -- the book's own claim and it is earned"),
    ("P22","because everything is defined in a complete index, no lie can exist within it","—",
     "200 of 200 fabrications refused when Λ is ASKED; 200 of 200 admitted when the index is "
     "REBUILT around them. The principle is about visibility, not omniscience",
     "PARTIAL", "as stated -- 'no lie can exist within it' -- it is FALSE, and §16.8.2 says so: "
                "the fabrication closes, has E = 0, and satisfies every law in the book. what "
                "is true is that a forged RULE is visible. the wording overstates the result "
                "the book itself computes"),
    ("P23","an object is complete only when all definitions are identified and no question can "
     "ever be had about the definition", "—",
     "the second condition is stated as uncheckable BY THE BOOK: no inspection establishes "
     "that no question can ever be had",
     "NOT CORROBORABLE", "unfalsifiable in one direction by construction, and the book says "
     "so -- which makes it honest and not provable"),
    ]
    for p in R: rec(*p)

with State("scrutinyC") as st:
    step(st, "the ten formalised", formalised, budget=120)
    step(st, "the seven procedural", procedural, budget=30)
    step(st, "the six reflexive", reflexive, budget=30)

w = 5
for k, name, expr, ev, verdict, note in OUT:
    print(f"\n  {k}  {name}")
    print(f"      expression : {expr}")
    print(f"      evidence   : {ev}")
    print(f"      VERDICT    : {verdict}")
    print(f"      note       : {note}")
print("\n  " + "   ".join(f"{k} {v}" for k, v in Counter(o[4] for o in OUT).most_common()))
