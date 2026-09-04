"""p1d.py -- THE EXACT FEASIBILITY CONDITION on the increasing 8-vector.

Claim to be tested, not assumed:

  With A = n and B = v[p], step Z is feasible  <=>  the entrant, plotted as the
  point (v[p], n) among its candidates, is a VERTEX OF THE LOWER CONVEX HULL of
  the candidate point set.  nu = n - a*v is a linear functional; minimising it
  for some a is exactly hull membership.

  A vertex of a lower hull is a point strictly below every chord that straddles
  it.  Each chord gives ONE inequality, and because y = n is constant data and
  x = v[p] is the unknown, that inequality is LINEAR IN v.

If the claim holds, "the feasible set" is a POLYHEDRON, not an uncharacterised
region, and the exact condition is its irredundant facet list.
"""
import sys, math, random, itertools
sys.path.insert(0, "/home/claude/work")
import ground as G

L = "spdfg"
def cap(l): return 2*(2*l+1)

# ---- STEPS: rebuilt by the same construction as brack.py / p1.py -------------
STEPS = []
for Z in range(3, 109):
    pr = {(n,l):o for n,l,o in G.expand(Z-1)}
    cu = {(n,l):o for n,l,o in G.expand(Z)}
    got = [k for k in cu if cu[k] > pr.get(k,0)]
    if len(got) != 1: continue
    gn, gl = got[0]; cand = []
    for l in range(5):
        for n in range(l+1, 9):
            if pr.get((n,l),0) >= cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0) == 0: break
    if (gn,gl) not in cand or len(cand) < 2: continue
    STEPS.append((Z, gn, gl, cand))
print("steps:", len(STEPS))

p_of = lambda n,l: n-l-1

# ---- the corridor, verbatim from p1.py, used ONLY as the oracle to test against
def corridors(A, B):
    IV = []
    for Z, gn, gl, cand in STEPS:
        lo, hi = -math.inf, math.inf; dead = False
        for n,l in cand:
            if (n,l) == (gn,gl): continue
            d = B(n,l) - B(gn,gl); r = A(n,l) - A(gn,gl)
            if abs(d) < 1e-12:
                if r <= 0: dead = True
                continue
            if d > 0: hi = min(hi, r/d)
            else:     lo = max(lo, r/d)
        if dead or lo >= hi: IV.append((Z,None,None)); continue
        IV.append((Z,lo,hi))
    return IV

# ---- BUILD THE INEQUALITY SYSTEM --------------------------------------------
# per step: collapse candidates by p, keeping min n (a candidate at the same p
# with n <= n_g kills the step outright, for every v).
ROWS = []          # (coef vector length 8, provenance)
UNCONDITIONAL = [] # steps that fail for all v
for Z, gn, gl, cand in STEPS:
    pg, ng = p_of(gn,gl), gn
    byp = {}
    for n,l in cand:
        pp = p_of(n,l)
        if pp not in byp or n < byp[pp]: byp[pp] = n
    if byp.get(pg, 10**9) < ng or (pg in byp and byp[pg] < ng):
        UNCONDITIONAL.append((Z,"same-p rival with lower n")); continue
    lows  = sorted([q for q in byp if q < pg])
    highs = sorted([q for q in byp if q > pg])
    for p1 in lows:
        for p2 in highs:
            n1, n2 = byp[p1], byp[p2]
            c = [0.0]*8
            c[pg] += (n2-n1)
            c[p1] += (ng-n2)
            c[p2] -= (ng-n1)
            if max(abs(x) for x in c) < 1e-12: continue
            ROWS.append((tuple(c), (Z, p1, pg, p2, n1, ng, n2)))

print("unconditional failures:", UNCONDITIONAL)
uniq = {}
for c, prov in ROWS:
    g = math.gcd(*[int(round(x)) for x in c]) or 1
    key = tuple(round(x/g, 12) for x in c)
    uniq.setdefault(key, []).append(prov)
print(f"chord inequalities generated: {len(ROWS)}  distinct after normalisation: {len(uniq)}")

KEYS = list(uniq.keys())
def satisfies(v, tol=0.0):
    return all(sum(k[i]*v[i] for i in range(8)) > tol for k in KEYS)

# ---- TEST THE CLAIM against the oracle, on random vectors -------------------
random.seed(11)
def oracle_feasible(v):
    A = lambda n,l: n; B = lambda n,l: v[p_of(n,l)]
    return all(lo is not None for Z,lo,hi in corridors(A,B))

agree = dis = 0; examples = []
for _ in range(20000):
    d = [random.random() for _ in range(7)]
    v = [0.0]
    for x in d: v.append(v[-1]+x)
    s = v[-1]; v = [x/s for x in v]
    o, q = oracle_feasible(v), satisfies(v)
    if o == q: agree += 1
    else:
        dis += 1
        if len(examples) < 3: examples.append((v,o,q))
print(f"\nORACLE vs POLYHEDRON on 20,000 increasing vectors: agree {agree}  disagree {dis}")
for e in examples: print("   ", e)
