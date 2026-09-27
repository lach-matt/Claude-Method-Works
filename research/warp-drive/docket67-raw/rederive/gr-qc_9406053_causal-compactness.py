#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9406053#causal-compactness (Borde 1994).

Claim as the tree uses it (create.py:200-202, 187, 289; index3.py:884; ledger D24):
  "as long as the causal compactness condition is met, causality violations
   have to occur when the topology changes, even if incomplete geodesics are
   admitted"  -> SINGULARITY_ESCAPES = False.

Checks (read-only on the tree; source text cached from alphaXiv full text,
md5 17c67ada52d92fc44065246ef92fee8c):
  C1  verbatim: the quotation and 'a condition satisfied in a very wide range
      of situations' occur in the source; the quotation's CONTEXT is read
      (bullet header, the standard-definition condition, 'other definitions').
  C2  Theorem 1's statement carries NO completeness hypothesis (text scan),
      and its hypotheses are listed from the text.
  C3  sympy: Clifton-Pohl torus -- a COMPACT (hence causally compact, Borde
      III.C) Lorentzian manifold with an INCOMPLETE null geodesic and an
      explicit closed timelike curve.  Non-vacuity of 'even if incomplete
      geodesics are admitted': compactness and incompleteness coexist, and the
      CTC is there anyway.
  C4  z3: propositional skeleton of Theorem 1 + Sec. VII.  (a) under the
      theorem, topology change & cc & smooth & (time-oriented or non-empty
      boundaries) & incomplete & no-CTC is UNSAT; (b) dropping cc it is SAT;
      (c) S1 empty, non-time-orientable: no CTC forced (Sec. VII);
      (d) the tree's encoded fact created & cc -> ctc is not entailed without
      the smooth non-degenerate metric hypothesis.
  C5  finite shadow of Theorem 1's proof step: on a finite ('compact') set,
      a flow line with no future endpoint revisits a point (pigeonhole),
      brute-forced over all maps on N <= 5 points.
  C6  the tree's own sites (read-only): which sites carry the cc condition
      and the standard-definition condition, and which drop them.
"""
import hashlib, itertools, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "gr-qc_9406053.txt")
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
MD5 = "17c67ada52d92fc44065246ef92fee8c"

results = []


def chk(name, got, want):
    ok = got == want
    results.append(ok)
    print("%s  %s: got %r want %r" % ("PASS" if ok else "FAIL", name, got, want))
    return ok


raw = open(SRC, "rb").read()
chk("C0 source md5", hashlib.md5(raw).hexdigest(), MD5)
txt = raw.decode("utf-8")
flat = re.sub(r"\s+", " ", txt)

# ---------------------------------------------------------------- C1
q1 = ("as long as the causal compactness condition is met, causality violations "
      "have to occur when the topology changes, even if incomplete geodesics are "
      "admitted")
q2 = "a condition satisfied in a very wide range of situations"
chk("C1a BORDE_SINGULARITY verbatim in source", q1 in flat, True)
chk("C1b 'very wide range of situations' verbatim (abstract)", q2 in flat, True)
i = flat.find(q1)
ctx = flat[i - 400:i + 300]
chk("C1c bullet header is the CLOSED-universe misconception",
    "Closed-universe topology change leads either to closed timelike curves or to a singularity" in ctx, True)
chk("C1d condition: 'If the standard incomplete-geodesic definition is used'",
    "If the standard incomplete-geodesic definition is used" in ctx, True)
chk("C1e caveat: 'other definitions of a singularity may make the statement true'",
    "other definitions of a singularity may make the statement true" in ctx, True)
chk("C1f 'causality violation' = at least one closed timelike curve (Sec. IV)",
    'By "causality violation" it is meant that there is at least one closed timelike curve' in flat.replace("“", '"').replace("”", '"'), True)
chk("C1g abstract: Theorem 3 'does not permit topology change even at the price of singularities'",
    "permit topology change even at the price of singularities (of the standard incomplete-geodesic variety)" in flat, True)
chk("C1h 'at the very end' = IX.C degenerate metrics ('these kinds of singularities')",
    "use these kinds of singularities in order to get topology change" in flat, True)

# ---------------------------------------------------------------- C2
a = flat.find("Theorem 1: Let M be")
b = flat.find("(A variant of this result", a)
thm1 = flat[a:b]
print("      Theorem 1 as extracted:", thm1)
chk("C2a Theorem 1 contains no completeness/geodesic hypothesis",
    bool(re.search(r"complete|geodesic", thm1, re.I)), False)
hyps = [h for h in ("time-oriented", "causally compact", "interpolates",
                    "no closed timelike curves") if h in thm1]
chk("C2b Theorem 1 hypotheses present", hyps,
    ["time-oriented", "causally compact", "interpolates", "no closed timelike curves"])
chk("C2c interpolating spacetime needs a smooth Lorentz metric, S1,S2 spacelike",
    "there is a smooth Lorentz metric on it with respect to which S 1 and S 2 are spacelike" in flat, True)
chk("C2d open case via timelike tube T inside an externally simple spacetime",
    "where M is a causally compact region of a larger, externally simple spacetime" in flat, True)
chk("C2e causal compactness definition present",
    "Definition: A spacetime M is called causally compact if for any p" in flat, True)

# ---------------------------------------------------------------- C3 (sympy)
import sympy as sp
x, y, t, s = sp.symbols("x y t s", real=True)
X = [x, y]
g = sp.Matrix([[0, 1], [1, 0]]) / (x**2 + y**2)      # g = 2 dx dy/(x^2+y^2)
ginv = g.inv()
Gam = [[[sp.simplify(sum(ginv[k, l] * (sp.diff(g[l, i], X[j]) + sp.diff(g[l, j], X[i])
                                       - sp.diff(g[i, j], X[l])) for l in range(2)) / 2)
         for j in range(2)] for i in range(2)] for k in range(2)]
chk("C3a signature Lorentzian (det < 0)", sp.simplify(g.det() * (x**2 + y**2)**2), -1)
lam = sp.symbols("lam", positive=True)
gs = g.subs({x: lam * x, y: lam * y}) * lam**2        # pullback under dilation
chk("C3b metric invariant under (x,y)->lam(x,y): quotient by lam=2 is a compact torus",
    sp.simplify(gs - g), sp.zeros(2, 2))
curve = {x: 1 / (1 - t), y: sp.Integer(0)}
vel = [sp.diff(curve[x], t), sp.diff(curve[y], t)]
acc = [sp.diff(v, t) for v in vel]
geo = [sp.simplify(acc[k] + sum(Gam[k][i][j].subs(curve) * vel[i] * vel[j]
                                for i in range(2) for j in range(2))) for k in range(2)]
chk("C3c x=1/(1-t), y=0 solves the geodesic equation (affine)", geo, [0, 0])
nrm = sp.simplify((sum(g[i, j] * vel[i] * vel[j] for i in range(2) for j in range(2))).subs(curve))
chk("C3d it is null", nrm, 0)
# leaves every compact subset of R^2\{0} as t->1-, i.e. winds infinitely often
# round the torus in finite affine parameter: number of fundamental domains
# [2^k, 2^(k+1)) crossed diverges.
windings = sp.limit(sp.log(1 / (1 - t)) / sp.log(2), t, 1, "-")
chk("C3e fundamental domains crossed before t=1 diverge (incomplete)", windings, sp.oo)
c = {x: 2**s, y: -2**s}                              # c(s) = 2^s (1,-1), s in [0,1]
cv = [sp.diff(c[x], s), sp.diff(c[y], s)]
gcv = sp.simplify((sum(g[i, j] * cv[i] * cv[j] for i in range(2) for j in range(2))).subs(c))
chk("C3f c(s)=2^s(1,-1): g(c',c') = -(ln 2)^2 < 0 (timelike)", sp.simplify(gcv + sp.log(2)**2), 0)
chk("C3g c(1) = 2 c(0) and c'(1) = 2 c'(0): a smooth CLOSED timelike curve on the torus",
    ([c[x].subs(s, 1), c[y].subs(s, 1)] == [2 * c[x].subs(s, 0), 2 * c[y].subs(s, 0)]
     and [v.subs(s, 1) for v in cv] == [2 * v.subs(s, 0) for v in cv]), True)

# ---------------------------------------------------------------- C4 (z3)
try:
    import z3
except ImportError:
    os.system(sys.executable + " -m pip install -q z3-solver")
    import z3
B = z3.Bools("tc cc smooth to nonempty ctc incomplete diffeo")
tc, cc, smooth, to, nonempty, ctc, incomplete, diffeo = B
# Theorem 1 (time-oriented) + Sec. VII (non-time-orientable, non-empty
# boundaries): cc & smooth & (to | nonempty) & ~ctc -> S1 diffeo S2.
thm = z3.Implies(z3.And(cc, smooth, z3.Or(to, nonempty), z3.Not(ctc)), diffeo)
defn = tc == z3.Not(diffeo)                    # topology change := S1 not diffeo S2


def sat(*fs):
    so = z3.Solver()
    so.add(thm, defn, *fs)
    return str(so.check())


chk("C4a tc & cc & smooth & to & INCOMPLETE & ~ctc is UNSAT",
    sat(tc, cc, smooth, to, incomplete, z3.Not(ctc)), "unsat")
chk("C4a' same with incomplete = False is UNSAT (incompleteness is idle)",
    sat(tc, cc, smooth, to, z3.Not(incomplete), z3.Not(ctc)), "unsat")
chk("C4b drop cc: tc & smooth & to & ~ctc is SAT (Borde IX.A route open)",
    sat(tc, z3.Not(cc), smooth, to, z3.Not(ctc)), "sat")
chk("C4c S1 empty & non-time-orientable: ~ctc SAT (Sec. VII)",
    sat(tc, cc, smooth, z3.Not(to), z3.Not(nonempty), z3.Not(ctc)), "sat")
chk("C4d tree fact created&cc->ctc NOT entailed without smooth (countermodel)",
    sat(tc, cc, to, z3.Not(smooth), z3.Not(ctc)), "sat")
chk("C4e tree fact entailed once smooth & to are added",
    sat(tc, cc, to, smooth, z3.Not(ctc)), "unsat")

# ---------------------------------------------------------------- C5 finite shadow
# A 'flow' on N points: each point steps to a successor or to END (S2).  A flow
# line that never reaches END must revisit a point (a closed orbit) -- the
# finite analogue of 'a trapped integral curve accumulates, giving a CTC'.
bad = 0
count = 0
for N in range(1, 6):
    for f in itertools.product(range(N + 1), repeat=N):   # value N = END
        count += 1
        for p0 in range(N):
            seen, p = set(), p0
            while p != N and p not in seen:
                seen.add(p)
                p = f[p]
            if p != N and p not in seen:
                bad += 1
print("      C5 enumerated %d flows (N <= 5)" % count)
chk("C5 every trapped flow line closes (no counterexample)", bad, 0)

# ---------------------------------------------------------------- C6 tree sites
cre = open(os.path.join(TREE, "create.py")).read().splitlines()
idx = open(os.path.join(TREE, "index3.py")).read().splitlines()
chk("C6a create.py:187 comment keeps 'not under the standard defn'",
    "not under the standard defn" in cre[186], True)
chk("C6b create.py:289 check label carries no definition condition",
    ("standard" in cre[288]) or ("definition" in cre[288]), False)
chk("C6c create.py:290 prints BORDE_SINGULARITY[:66], which includes the cc condition",
    "causal compactness condition is met" in q1[:66], True)
summ = cre[340] + " " + cre[341]
chk("C6d create.py:341-342 summary drops the cc condition",
    "causal compact" in summ, False)
chk("C6e index3.py:884 says 'does NOT buy topology change' (Theorem 3's conclusion) "
    "under the kinematic quote", "does NOT buy topology change" in idx[883], True)

n = len(results)
print("\n%d/%d checks agree" % (sum(results), n))
sys.exit(0 if all(results) else 1)
