#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation / machine-check for geroch-1967-topology-change.

Geroch's theorem (and Borde's Theorem 1) is a theorem of differential topology on
a continuum; it is NOT finite, so it is not machine-checked here as a whole.
What IS checked:
  A. every quotation the tree carries (create.py constants) against the cached
     source text of Borde gr-qc/9406053v1, whitespace-normalised;
  B. the escape list: Borde sec. IX names the Euclidean path integral plus
     three Lorentzian-framework possibilities A/B/C; create.ESCAPES has three;
  C. the Reinhart-Sorkin / Poincare-Hopf arithmetic behind 'kinematically
     possible' and behind the Misner trick (sympy integers);
  D. a concrete non-vacuity instance: Borde's own 2-D example (cylinder,
     S1 u S1 <-> empty) built with an explicit nowhere-degenerate Lorentz metric;
     Theorem 1 predicts a CTC and one is exhibited; the past-directed integral
     curves are shown to accumulate on it (the mechanism of Borde's proof);
  E. a hole-cut spacetime (causal compactness dropped) with a change of slice
     topology and a global time function (so NO CTC): H_cc is load-bearing;
  F. z3: the finite core of the proof (acyclic successor map on a finite set
     => every orbit exits) with a vacuity guard; and the propositional split
     between Theorem 1 (kinematic, no T_ab) and Theorem 3 (dynamic, needs the
     half-integral null convergence condition).
Reads the tree read-only (ast parse of create.py); writes nothing but stdout.
"""
import ast, math, os, re, sys

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
BORDE_TXT = os.path.join(D67, "src/gr-qc_9406053.txt")
PISANA_TXT = os.path.join(D67, "2505.02210.txt")
CREATE = "/home/user/Claude-Method-Works/research/warp-drive/create.py"

results = []
def chk(label, got, want):
    ok = (got == want)
    results.append((label, ok))
    print("  %-70s got=%-8s want=%-8s %s" % (label[:70], got, want, "ok" if ok else "FAIL"))
    return ok

def norm(s):
    s = s.replace("≥", ">=").replace("’", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"-\s*\n\s*", "-", s)
    return re.sub(r"\s+", " ", s).strip().lower()

# ---------------------------------------------------------------- A
print("A. THE TREE'S QUOTATIONS AGAINST THE SOURCE TEXT (Borde gr-qc/9406053v1)")
borde = norm(open(BORDE_TXT, encoding="utf-8").read())
src = open(CREATE, encoding="utf-8").read()
tree = ast.parse(src)
consts = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        try:
            consts[node.targets[0].id] = ast.literal_eval(node.value)
        except Exception:
            pass
for name in ("BORDE", "BORDE_SINGULARITY", "BORDE_DYNAMICS", "BORDE_CAUTION"):
    chk("create.%s occurs verbatim in Borde" % name, norm(consts[name]) in borde, True)
for q in ("topology change is only to be had at a price",
          "a condition satisfied in a very wide range of situations",
          "highly undesirable feature", "would have to be fairly severe"):
    chk("docstring/ESCAPES phrase '%s' in Borde" % q[:40], norm(q) in borde, True)
chk("create.GEROCH_NEEDS_MATTER_ASSUMPTION is False", consts["GEROCH_NEEDS_MATTER_ASSUMPTION"], False)
chk("create.EXOTIC_MATTER_HELPS_CREATION is False", consts["EXOTIC_MATTER_HELPS_CREATION"], False)
# Borde's own definition of 'causality violation' = a CTC (so specthm's 'ctc' is faithful)
chk("Borde: 'causality violation' means at least one CTC",
    norm('By "causality violation" it is meant that there is at least one closed timelike curve') in borde, True)
chk("Borde Theorem 1 is stated for a (time-oriented) spacetime",
    norm("Theorem 1: Let M be a (time-oriented) causally compact spacetime") in borde, True)
chk("Borde: weakening curvature constraints 'would not affect the presence of causality violations'",
    norm("This would not affect the presence of causality violations") in borde, True)
chk("Borde names energy-condition violation as a route past Theorem 3 (wormhole creation)",
    norm("Some discussions of wormhole creation are, for example, based precisely on large violations of the energy condition") in borde, True)

# Geroch 1967 restated exactly (Pisana-Shoshany-Antoniou-Kauffman-Lambropoulou, 2505.02210v4, Thm III.2)
pis = norm(open(PISANA_TXT, encoding="utf-8").read())
chk("2505.02210 Thm III.2 restates Geroch: compact W, spacelike boundary, no CTC => Sigma_i x [0,1]",
    norm("Let W be a compact spacetime whose boundary is the disjoint union of two compact spacelike") in pis
    and norm("If W has no CTCs, then") in pis, True)
chk("2505.02210 Def. 6: spacetime = everywhere non-degenerate TIME-ORIENTABLE Lorentz metric",
    norm("non-degenerate time-orientable Lorentzian metric") in pis, True)
chk("2505.02210 ref [7] prints the Geroch year as 2004 (misprint; Borde ref 5 prints 1967)",
    "(2004)" in norm(open(PISANA_TXT).read()[open(PISANA_TXT).read().find("[7] R. P. Geroch"):][:140]), True)

# ---------------------------------------------------------------- B
print("\nB. THE ESCAPE LIST")
esc = consts.get("ESCAPES")
chk("create.ESCAPES has 3 entries", len(esc), 3)
borde_lorentzian = [norm(x) in borde for x in ("A ] Dropping causal compactness",
                                              "B ] Weakening the curvature constraints",
                                              "C ] Degenerate metrics")]
chk("Borde sec IX has A, B, C inside 'the general Lorentzian framework'", all(borde_lorentzian), True)
chk("Borde: 'even within the general Lorentzian framework there are still several interesting possibilities'",
    norm("But even within the general Lorentzian framework there are still several interesting possibilities") in borde, True)
tree_names = [e[0] for e in esc]
chk("create.ESCAPES names 'degenerate metrics' (Borde IX.C)", any("degenerate" in n for n in tree_names), False)
chk("create.ESCAPES[1] mentions energy-condition violation (Borde IX.B second route)",
    "energy" in esc[1][2].lower(), False)

# ---------------------------------------------------------------- C
print("\nC. REINHART-SORKIN / POINCARE-HOPF ARITHMETIC (sympy integers)")
import sympy as sp
def chi_betti(b): return sum((-1)**i * bi for i, bi in enumerate(b))
chi = {"S3": chi_betti([1, 0, 0, 1]), "S1xS2": chi_betti([1, 1, 1, 1]), "T3": chi_betti([1, 3, 3, 1]),
       "CP2": chi_betti([1, 0, 1, 0, 1]), "S2xS2": chi_betti([1, 0, 2, 0, 1]), "T4": chi_betti([1, 4, 6, 4, 1]),
       "S1xS3": chi_betti([1, 1, 0, 1, 1])}
chk("every closed 3-manifold listed has chi = 0 (odd dim)", all(chi[k] == 0 for k in ("S3", "S1xS2", "T3")), True)
chk("chi(CP2)=3, chi(S2xS2)=4, chi(T4)=0", (chi["CP2"], chi["S2xS2"], chi["T4"]), (3, 4, 0))
# connected sum in even dim n: chi(M#V) = chi(M)+chi(V)-2  (remove a ball: chi drops by 1 since chi(S^{n-1})=0)
cM, cV = sp.symbols("cM cV", integer=True)
chiS_nm1_even_n = 0   # S^{n-1} with n even is odd-dim sphere
consum = (cM - 1) + (cV - 1) - chiS_nm1_even_n
chk("chi(M#V) = chi(M)+chi(V)-2 (n even), by Mayer-Vietoris count", sp.simplify(consum - (cM + cV - 2)) == 0, True)
# Morse/handle count: chi(W) = chi(Sigma_i) + sum_k (-1)^k  (one k-handle per index-k critical point)
def chi_handles(chi_in, idx): return chi_in + sum((-1)**k for k in idx)
w1 = chi_handles(chi["S3"], [1])           # S^3 -> S^1 x S^2 : one 1-handle (0-surgery = wormhole nucleation)
chk("wormhole creation S^3 -> S^1xS^2 by one 1-handle: chi(W) = -1", w1, -1)
chk("so (n=4 even, RS rule needs chi(W)=0) no nowhere-vanishing field: needs a fix", w1 == 0, False)
chk("Misner trick: chi(W # CP2) = 0  (the 2505.02210 choice)", w1 + chi["CP2"] - 2, 0)
chk("alternative: chi(W # S2xS2 # T4) = -1+4-2+0-2 = -1 (even steps cannot fix odd chi)", w1 + chi["S2xS2"] - 2 + chi["T4"] - 2, -1)
# n = 3: chi(S1)=chi(S2) forbids every genus-changing transition of oriented closed surfaces
g1, g2 = sp.symbols("g1 g2", integer=True, nonnegative=True)
chk("n=3 RS rule: 2-2g1 = 2-2g2 <=> g1 = g2", sp.solve(sp.Eq(2 - 2*g1, 2 - 2*g2), g1) == [g2], True)
# the trousers S1 u S1 -> S1 (n=2 even) has chi = -1: no Lorentz metric, hence the crotch singularity
chk("2-D trousers chi = 2-2*0-3 = -1 != 0 (singular)", 2 - 0 - 3, -1)
chk("2-D cylinder chi = 0 (admits a Lorentz metric)", 2 - 0 - 2, 0)

# ---------------------------------------------------------------- D
print("\nD. BORDE'S 2-D EXAMPLE, BUILT: cylinder [-1,1] x S^1 as  empty -> S^1 u S^1")
import numpy as np
# V = x d_x + (1 - x^2) d_theta ; outward at x = +-1 ; nowhere zero
# g = h - 2 (V_flat (x) V_flat)/h(V,V), h = dx^2 + dtheta^2  => g(V,V) = -h(V,V)
def V(x): return np.array([x, 1.0 - x * x])
def g(x):
    v = V(x); hvv = v @ v
    return np.eye(2) - 2.0 * np.outer(v, v) / hvv
xs = np.linspace(-1, 1, 20001)
dets = np.array([np.linalg.det(g(x)) for x in xs])
gvv = np.array([V(x) @ g(x) @ V(x) for x in xs])
chk("V nowhere zero on [-1,1]", bool(np.min([np.linalg.norm(V(x)) for x in xs]) > 0.5), True)
chk("det g = -1 everywhere (nondegenerate, Lorentzian)", bool(np.allclose(dets, -1.0)), True)
chk("g(V,V) < 0 everywhere (time-orientable by V)", bool(np.max(gvv) < 0), True)
th = np.array([0.0, 1.0])
chk("boundary circles x=+-1 spacelike: g(d_theta,d_theta) = +1",
    (round(float(th @ g(1.0) @ th), 12), round(float(th @ g(-1.0) @ th), 12)), (1.0, 1.0))
chk("circle x=0 closed, tangent d_theta = V(0): g = -1  => a CTC", round(float(th @ g(0.0) @ th), 12), -1.0)
# M is compact => causally compact; S1 = empty, S2 = S1 u S1 not diffeomorphic => Thm 1 predicts a CTC: consistent
# past-directed integral curves: dx/dt = -x, dtheta/dt = -(1-x^2): x -> 0, theta winds without bound
x0, t = 0.9, np.linspace(0, 40, 4001)
xt = x0 * np.exp(-t)
theta_t = -(t - x0**2 * (1 - np.exp(-2 * t)) / 2.0)
chk("past integral curve from x=0.9 has no past endpoint on a boundary (x -> 0)", bool(xt[-1] < 1e-15), True)
chk("and winds unboundedly (accumulates on the closed timelike orbit x=0)", bool(abs(theta_t[-1]) > 2 * math.pi * 5), True)

# ---------------------------------------------------------------- E
print("\nE. DROP CAUSAL COMPACTNESS: a slit cylinder changes slice topology with NO CTC")
# flat 2-D cylinder t in [0,1], theta in S^1, g = -dt^2 + dtheta^2, remove the closed slit {theta=0, t>=1/2}
# t is a global time function: g^{-1}(dt,dt) = -1 < 0, so t strictly increases on every future causal curve -> no CTC
ginv = np.diag([-1.0, 1.0]); dt = np.array([1.0, 0.0])
chk("g^{-1}(dt,dt) = -1 (global time function => no closed causal curve)", float(dt @ ginv @ dt), -1.0)
# simplicial models: S^1 = N-gon (N vertices, N edges); S^1 minus the slit point = remove one vertex
# and its two incident open edges -> path with N-1 vertices, N-2 edges
N = 12
chi_S1 = N - N
chi_cut = (N - 1) - (N - 2)
chk("initial slice S^1: chi = 0 ; final slice S^1 minus a point: chi = 1 (not diffeomorphic)", (chi_S1, chi_cut), (0, 1))
print("      ARGUED, NOT COMPUTED: the slit spoils causal compactness (closure of I+(p) for p")
print("      below the slit tip reaches the removed set), so Theorem 1 does not apply; H_cc is")
print("      load-bearing -- this is Borde's own reason for imposing it (sec. III.B).")

# ---------------------------------------------------------------- F
print("\nF. z3: finite core of Theorem 1, and the Theorem 1 / Theorem 3 split")
try:
    import z3
except ImportError:
    print("  z3 missing: pip install z3-solver"); sys.exit(2)
def core(n, allow_cycle):
    # cells 0..n-1, EXIT = n; succ: cell -> cell or EXIT ; rank-function encodes 'no cycle'
    s = z3.Solver()
    succ = [z3.Int("s%d" % i) for i in range(n)]
    rank = [z3.Int("r%d" % i) for i in range(n)]
    for i in range(n):
        s.add(succ[i] >= 0, succ[i] <= n)
        if not allow_cycle:
            for j in range(n):
                s.add(z3.Implies(succ[i] == j, rank[j] < rank[i]))
    # orbit of cell 0 after n steps
    cur = z3.IntVal(0)
    for _ in range(n):
        nxt = z3.IntVal(n)
        for j in range(n):
            nxt = z3.If(cur == j, succ[j], nxt)
        cur = z3.If(cur == n, z3.IntVal(n), nxt)
    s.add(cur != n)               # negation: orbit of 0 has NOT exited after n steps
    return s.check()
for n in (3, 5, 7):
    chk("n=%d acyclic successor map: some orbit never exits  (expect unsat)" % n, str(core(n, False)), "unsat")
    chk("n=%d vacuity guard, cycle allowed: non-exiting orbit exists (expect sat)" % n, str(core(n, True)), "sat")
created, cc, ctc, einstein, ncc, generic, exotic = z3.Bools("created cc ctc einstein ncc generic exotic")
thm1 = z3.Implies(z3.And(created, cc), ctc)                                # no T_ab, no field equation
thm3 = z3.Implies(z3.And(cc, einstein, ncc, generic), z3.Not(created))    # dim >= 3
exotic_def = z3.Implies(exotic, z3.Not(ncc))
s = z3.Solver(); s.add(thm1, thm3, exotic_def, created, cc, exotic, z3.Not(ctc))
chk("Thm1: created & cc & exotic & no CTC  (expect unsat: exotic matter cannot remove the CTC)", str(s.check()), "unsat")
s = z3.Solver(); s.add(thm1, thm3, exotic_def, created, cc, einstein, ncc, generic)
chk("Thm3: created & cc & Einstein & NCC & generic  (expect unsat)", str(s.check()), "unsat")
s = z3.Solver(); s.add(thm1, thm3, exotic_def, created, cc, einstein, generic, exotic)
chk("created & cc & Einstein & exotic: NOT excluded by Thm1+Thm3 (expect sat; with ctc forced)", str(s.check()), "sat")
m = s.model()
chk("  ... and in that model ctc is True", bool(z3.is_true(m.eval(ctc))), True)

print()
bad = [l for l, ok in results if not ok]
print("%d checks, %d FAIL" % (len(results), len(bad)))
for l in bad: print("  FAIL:", l)
sys.exit(1 if bad else 0)
