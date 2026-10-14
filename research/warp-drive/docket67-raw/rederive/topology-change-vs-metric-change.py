#!/usr/bin/env python3
"""
DOCKET 67 -- audit re-derivation for key 'topology-change-vs-metric-change'.

Tree's claim (create.py:102-108, 235-245): enlarging an existing throat
r_0 -> r_1 on already-nontrivial topology is a METRIC change, not a topology
change, so Geroch / Tipler / Borde say nothing about it; encoded as
is_topology_change(initial_nontrivial, final_nontrivial) = (initial != final).

What the sources state (Borde gr-qc/9406053v1, READ from cached text):
  Thm 1: M (time-oriented) causally compact, interpolating S1 -> S2, no CTC
         ==> M diffeomorphic to S1 x [0,1] (in particular S1 ~ S2).
  Thm 3: dim >= 3, generic + half-integral null convergence ==> same product.
  Reinhart/Sorkin (quoted by Borde): n even ==> M admits the required
         transverse timelike field if chi(M) = 0.
  chi(A#B) = chi(A) + chi(B) - 2 (even n), chi(CP2) = 3.
The conclusion of each theorem is about the INTERPOLATING MANIFOLD M, not
about a pair of booleans at the endpoints.

Checks
  C1 sympy : an explicit enlargement family on a FIXED manifold,
             g = -dt^2 + dl^2 + (l^2 + a(t)^2) dOmega^2, a(t) from r0 to r1 > 0:
             g^{tt} = -1 everywhere, so t is a time function and no closed
             timelike (or causal) curve exists; M = Sigma x [0,1] is a product;
             the throat (minimal 2-sphere, R'=0, R''>0) exists for every a>0.
             => Geroch/Borde Thm 1 & 3 conclusions hold trivially: SILENT.  (agrees)
  C2 sympy+z3: the same family's NEC.  At l=0, G_kk = -2(1 + a a'')/a^2 for
             both radial null k.  At Hayward's dynamic mouth (theta_+ = 0,
             l_h = -a a'), G_++ = -2(1 + a'^2 + a a'')/(a^2(1 + a'^2)); z3: a
             TEMPORAL mouth (|d l_h/dt| < 1) with G_++ >= 0 is unsat.  So
             'permitted' by the topology theorems is not 'free': enlargement
             still needs NEC violation at the mouth (Hayward 2009, Hochberg-
             Visser 1998), reproduced here for this family.
  C3 integer: is_topology_change(True, True) = False is FALSE as a general
             predicate: Sigma1 = R^3 # (S1xS2) (b1=1) and Sigma2 = R^3 # 2(S1xS2)
             (b1=2) are both 'nontrivial' and not homeomorphic.
  C4 integer: identical nontrivial endpoints, NON-product M, Lorentz metric
             exists: M = (Sigma x I) # (S1xS3) # CP2 # CP2, Sigma = S1xS2.
             chi(M) = 0 (Reinhart: field exists), b1(M) = 2 != b1(Sigma x I) = 1
             => M not a product => by Thm 1 (M compact => causally compact) M
             HAS a CTC although initial = final = the same nontrivial Sigma.
             So 'before and after nontrivial' is NOT sufficient for 'the
             theorems say nothing'; the operative hypothesis is 'M = Sigma x I'
             (a metric family on a fixed manifold), which the prose carries and
             the boolean / specthm W-enlarge (hyps []) do not.
  C5 z3    : the logic.  Thm1 as an axiom over {cc, to, ctc, product,
             same_endpoints}; show (a) product ==> theorem imposes nothing
             (ctc free: both sat); (b) same_endpoints & not product & cc & to
             ==> ctc (unsat of the negation); (c) vacuity guards.
"""
import sys
import sympy as sp

ok = True


def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-70s %s %s" % (label, "ok" if cond else "FAIL", detail))


# ------------------------------------------------------------------ C1, C2
print("C1/C2  explicit enlargement family on a fixed manifold (sympy)")
t, l, th, ph = sp.symbols('t l theta phi', real=True)
a = sp.Function('a', positive=True)(t)
X = [t, l, th, ph]
R2 = l**2 + a**2
g = sp.diag(-1, 1, R2, R2 * sp.sin(th)**2)
ginv = g.inv()
chk("C1 g^{tt} = -1 (dt timelike everywhere: t is a time function)",
    sp.simplify(ginv[0, 0] + 1) == 0)
chk("C1 det g = -(l^2+a^2)^2 sin^2(theta) != 0 for a>0 off the poles",
    sp.simplify(g.det() + R2**2 * sp.sin(th)**2) == 0)
R = sp.sqrt(R2)
dR = sp.diff(R, l)
d2R = sp.diff(R, l, 2)
chk("C1 throat at l=0: R'(0) = 0", sp.simplify(dR.subs(l, 0)) == 0)
chk("C1 flare-out at l=0: R''(0) = 1/a > 0",
    sp.simplify(d2R.subs(l, 0) - 1 / a) == 0)
chk("C1 throat radius R(0) = a(t): r0 -> r1 is a(t) moving, manifold fixed",
    sp.simplify(R.subs(l, 0) - a) == 0)
# degeneracy only at a = 0: that limit is the pinch (topology change)
chk("C1 at a=0 the l=0 sphere collapses (R(0)=0): the pinch is the excluded limit",
    sp.simplify(R.subs(l, 0).subs(a, 0)) == 0)

# Christoffels and Ricci
n = 4
Gam = [[[sp.simplify(sum(ginv[i, m] * (sp.diff(g[m, j], X[k]) + sp.diff(g[m, k], X[j])
                                        - sp.diff(g[j, k], X[m])) for m in range(n)) / 2)
         for k in range(n)] for j in range(n)] for i in range(n)]


def ricci(j, k):
    s = 0
    for i in range(n):
        s += sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
        for m in range(n):
            s += Gam[i][i][m] * Gam[m][j][k] - Gam[i][k][m] * Gam[m][j][i]
    return sp.simplify(s)


Ric = sp.Matrix(n, n, lambda j, k: ricci(j, k))
Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
G = sp.simplify(Ric - Rs * g / 2)
kp = sp.Matrix([1, 1, 0, 0])
km = sp.Matrix([1, -1, 0, 0])
Gpp = sp.simplify((kp.T * G * kp)[0].subs(l, 0))
Gmm = sp.simplify((km.T * G * km)[0].subs(l, 0))
print("      G_ab k+^a k+^b at throat =", Gpp)
print("      G_ab k-^a k-^b at throat =", Gmm)
ad, add = sp.symbols('adot addot', real=True)
A = sp.symbols('A', positive=True)
Gpp_s = sp.simplify(Gpp.subs(sp.Derivative(a, (t, 2)), add).subs(sp.Derivative(a, t), ad).subs(a, A))
Gmm_s = sp.simplify(Gmm.subs(sp.Derivative(a, (t, 2)), add).subs(sp.Derivative(a, t), ad).subs(a, A))
print("      (a -> A, a' -> adot, a'' -> addot):", Gpp_s, "|", Gmm_s)
chk("C2 static limit (adot=addot=0): G_kk = -2/A^2 < 0 (NEC violated)",
    sp.simplify(Gpp_s.subs({ad: 0, add: 0}) + 2 / A**2) == 0)
sumk = sp.simplify(Gpp_s + Gmm_s)
print("      G_++ + G_-- at throat =", sumk)
# dynamic: is at least one of the two radial null contractions negative for all adot, addot?
# decide by sign analysis
# Hayward (0903.5438, READ): the dynamic mouth is where an expansion vanishes,
# not l = 0.  theta_+ ~ d_+R = (a a' + l)/R vanishes at l_h = -a a'.
Lsym = sp.symbols('L', real=True)
Gpp_gen = sp.simplify((kp.T * G * kp)[0])
sub = lambda e: sp.simplify(e.subs(sp.Derivative(a, (t, 2)), add).subs(sp.Derivative(a, t), ad).subs(a, A))
Gpp_gen_s = sub(Gpp_gen)
dplusR = sub(sp.diff(R, t) + sp.diff(R, l))
lh = sp.solve(sp.Eq(sp.numer(sp.together(dplusR)), 0), l)
chk("C2 theta_+ = 0 surface at l_h = -a a'", lh == [-A * ad], str(lh))
Gmouth = sp.factor(sp.simplify(Gpp_gen_s.subs(l, lh[0])))
print("      G_++ at the theta_+=0 mouth =", Gmouth)
chk("C2 G_++(mouth) = -2(1 + adot^2 + A addot)/(A^2 (1+adot^2))",
    sp.simplify(Gmouth + 2 * (1 + ad**2 + A * add) / (A**2 * (1 + ad**2))) == 0)
# the mouth's world-line l_h(t) = -a a' has slope dl_h/dt = -(a'^2 + a a'')
# temporal (Hayward's wormhole mouth) iff |slope| < 1 in the -dt^2+dl^2 plane
try:
    import z3 as _z
    Az, adz, addz = _z.Reals('A adot addot')
    slope = adz * adz + Az * addz
    sv = _z.Solver()
    sv.add(Az > 0, slope > -1, slope < 1, Az * addz + adz * adz + 1 <= 0)
    chk("C2 z3: temporal mouth & NEC holding at it (G_++ >= 0) is unsat", sv.check() == _z.unsat)
    sv2 = _z.Solver(); sv2.add(Az > 0, slope > -1, slope < 1)
    chk("C2 z3 vacuity guard: temporal mouth is sat", sv2.check() == _z.sat)
    sv3 = _z.Solver(); sv3.add(Az > 0, Az * addz + adz * adz + 1 <= 0)
    chk("C2 z3: NEC can hold at theta_+=0 surface only off-temporal (sat, spacelike)",
        sv3.check() == _z.sat)
except ImportError:
    chk("C2 z3 available", False)

# ------------------------------------------------------------------ C3
print("\nC3  two nontrivial spatial topologies that differ (integer homology)")


def b1_R3_sum_handles(k):
    # R^3 # k (S^1 x S^2): H_1 = Z^k
    return k


def is_topology_change_tree(initial_nontrivial, final_nontrivial):  # create.py:235-236
    return initial_nontrivial != final_nontrivial


s1, s2 = b1_R3_sum_handles(1), b1_R3_sum_handles(2)
chk("C3 b1(R3#(S1xS2)) = 1, b1(R3#2(S1xS2)) = 2: not homeomorphic", s1 != s2)
chk("C3 tree predicate on (nontrivial, nontrivial) returns False", is_topology_change_tree(True, True) is False)
chk("C3 => predicate says 'no topology change' for a genuine change (1 -> 2 handles)",
    (s1 != s2) and not is_topology_change_tree(True, True))

# ------------------------------------------------------------------ C4
print("\nC4  same nontrivial endpoints, non-product Lorentzian cobordism (dim 4)")
chi = {"S1xS2": 0, "S1xS3": 0, "CP2": 3}
b = {"S1xS2": (1, 1), "S1xS3": (1, 0), "CP2": (0, 1)}  # (b1, b2)


def csum(chiA, chiB):  # even dimension: chi(A#B) = chi(A)+chi(B)-2  (Borde, READ)
    return chiA + chiB - 2


chi_prod = chi["S1xS2"]  # chi(Sigma x I) = chi(Sigma) = 0
chiM = csum(csum(csum(chi_prod, chi["S1xS3"]), chi["CP2"]), chi["CP2"])
b1_prod, b2_prod = b["S1xS2"]
b1M = b1_prod + b["S1xS3"][0] + 2 * b["CP2"][0]
b2M = b2_prod + b["S1xS3"][1] + 2 * b["CP2"][1]
print("      chi(Sigma x I) = %d ; chi(M) = %d ; b1: %d vs %d ; b2: %d vs %d"
      % (chi_prod, chiM, b1_prod, b1M, b2_prod, b2M))
chk("C4 chi(M) = 0 => Reinhart field exists => Lorentz metric, S1,S2 spacelike", chiM == 0)
chk("C4 b1(M) != b1(Sigma x I) => M not diffeomorphic to Sigma x [0,1]", b1M != b1_prod)
chk("C4 endpoints identical (both Sigma = S1xS2, nontrivial): tree predicate False",
    is_topology_change_tree(True, True) is False)
chk("C4 => Borde Thm 1 (compact => causally compact) forces a CTC in M anyway",
    chiM == 0 and b1M != b1_prod)

# ------------------------------------------------------------------ C5
print("\nC5  z3: the logic of Thm 1 against the tree's predicate")
try:
    import z3
except ImportError:
    z3 = None
    chk("C5 z3 available", False)
if z3:
    cc, to, ctc, prod, same = z3.Bools('cc to ctc product same_endpoints')
    thm1 = z3.Implies(z3.And(cc, to, z3.Not(ctc)), z3.And(prod, same))
    prod_implies_same = z3.Implies(prod, same)

    def status(*f):
        s = z3.Solver(); s.add(*f); return s.check()

    base = [thm1, prod_implies_same]
    # (a) product: theorem silent -- both ctc and not-ctc consistent
    chk("C5a product & cc & to & no-CTC is sat (theorem imposes nothing)",
        status(*base, prod, cc, to, z3.Not(ctc)) == z3.sat)
    # (b) same endpoints, non-product, cc, to => ctc
    chk("C5b same & not product & cc & to & no-CTC is unsat (CTC forced)",
        status(*base, same, z3.Not(prod), cc, to, z3.Not(ctc)) == z3.unsat)
    chk("C5b vacuity guard: same & not product & cc & to is sat",
        status(*base, same, z3.Not(prod), cc, to) == z3.sat)
    # (c) the tree's inference 'same endpoints => theorems silent' is not valid
    chk("C5c 'same endpoints => no CTC forced' refuted: exists model same & forced ctc",
        status(*base, same, z3.Not(prod), cc, to, z3.Not(ctc)) == z3.unsat)
    chk("C5c 'product => no CTC forced' holds: no-CTC consistent under product",
        status(*base, prod, cc, to, z3.Not(ctc)) == z3.sat)

print("\n  RE-DERIVATION " + ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
