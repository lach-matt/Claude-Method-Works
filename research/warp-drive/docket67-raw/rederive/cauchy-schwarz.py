#!/usr/bin/env python3
"""DOCKET 67 -- audit rederivation: cauchy-schwarz.
Tree's use (research/warp-drive/fluctuation.py:75-79): for real symmetric 4x4 G,
SUM_AB G_AB^2 >= (tr G)^2/4, equality only at G = (tr G/4) I = (rho/2) I, rho = tr G/2;
hence Delta' = (1/2) SUM G^2 / rho^2 >= 1/2 and Delta = Delta'/(1+Delta') >= 1/3.
Independent of fluctuation.py (does not import it). Exits 1 on any failure."""
import sys, itertools
import sympy as sp
try:
    import z3
except ImportError:
    z3 = None
ok = True
def chk(label, got, want):
    global ok
    r = (got == want)
    ok &= r
    print(("PASS " if r else "FAIL ") + label + "   got=%s" % (got,))

# 1. SOS certificate (sympy, exact): for ANY real n x n matrix (no symmetry)
#    n*SUM_AB G_AB^2 - (tr G)^2 = SUM_{A<B} (G_AA-G_BB)^2 + n*SUM_{A!=B} G_AB^2
for n in (2, 3, 4, 5):
    G = sp.Matrix(n, n, lambda a, b: sp.Symbol('g%d_%d' % (a, b), real=True))
    tr = G.trace()
    fro = sum(G[a, b]**2 for a in range(n) for b in range(n))
    sos = sum((G[a, a] - G[b, b])**2 for a in range(n) for b in range(a+1, n)) \
        + n * sum(G[a, b]**2 for a in range(n) for b in range(n) if a != b)
    chk("SOS identity n=%d, general real (non-symmetric) matrix" % n, sp.expand(n*fro - tr**2 - sos), 0)
# Cauchy-Schwarz proper (Cauchy 1821 Note II form) is the diagonal step:
d = sp.symbols('d0:4', real=True)
chk("Lagrange identity: 4 SUM d_i^2 - (SUM d_i)^2 = SUM_{i<j}(d_i-d_j)^2",
    sp.expand(4*sum(x**2 for x in d) - sum(d)**2 - sum((d[i]-d[j])**2 for i in range(4) for j in range(i+1, 4))), 0)

# 2. equality: every SOS term vanishes  <=>  off-diagonals 0 and diagonal equal  <=>  G = (trG/4) I
rho = sp.Symbol('rho', real=True)
chk("equality point G=(rho/2)I has tr G = 2 rho and 4 SUM G^2 = (trG)^2",
    (sp.simplify((sp.eye(4)*rho/2).trace() - 2*rho), sp.simplify(4*sum(x**2 for x in (sp.eye(4)*rho/2)) - (2*rho)**2)), (0, 0))

# 3. Delta' and Delta floors
Dp = sp.Symbol('Dp', real=True)
chk("Delta = Dp/(1+Dp) is increasing (derivative 1/(1+Dp)^2 > 0)", sp.simplify(sp.diff(Dp/(1+Dp), Dp) - 1/(1+Dp)**2), 0)
chk("Dp = 1/2 -> Delta = 1/3", sp.Rational(1, 2)/(1 + sp.Rational(1, 2)), sp.Rational(1, 3))

# 4. controls against the tree's printed values (diagonal G built from rho, p_i for the
#    massless minimally coupled scalar: G00 = (rho+SUM p)/2, G_ii = rho + p_i - G00)
def dprime_from(rho_, p):
    g00 = (rho_ + sum(p))/2
    diag = [g00] + [rho_ + pi - g00 for pi in p]
    assert sp.simplify(sum(diag) - 2*rho_) == 0
    return sp.simplify(sp.Rational(1, 2)*sum(x**2 for x in diag)/rho_**2)
r = sp.Symbol('r', positive=True)
chk("thermal (p=rho/3): Delta' = 2/3 (fluctuation.py:87)", dprime_from(r, [r/3]*3), sp.Rational(2, 3))
chk("Casimir (xi=-1,-1,3): Delta' = 6 (KF 3.45 as the tree reads it)", dprime_from(r, [-r, -r, 3*r]), 6)
chk("Casimir sign-flipped rho<0 gives the same Delta' (sign-blind)", dprime_from(-r, [r, r, -3*r]), 6)
k0, k1, k2, k3 = sp.symbols('k0:4', real=True)
kv = sp.Matrix([k0, k1, k2, k3]); Gk = kv*kv.T
Dk = sp.simplify((sp.Rational(1, 2)*sum(x**2 for x in Gk)/(Gk.trace()/2)**2).subs(k0**2, k1**2+k2**2+k3**2))
chk("single null plane-wave mode, G = k k^T: Delta' = 2, Delta = 2/3 (squeezed-vacuum value)", (Dk, Dk/(1+Dk)), (2, sp.Rational(2, 3)))
chk("equality needs p_i = 0 for all i: p=(0,0,0) gives Delta' = 1/2", dprime_from(r, [0, 0, 0]), sp.Rational(1, 2))

# 5. hypothesis probes (what the inequality does and does not need)
chk("n-dependence: C-S floor on Delta' is 2/n; n=4 -> 1/2, n=5 (massive: +m phi component) -> 2/5",
    [sp.Rational(2, n) for n in (4, 5)], [sp.Rational(1, 2), sp.Rational(2, 5)])

if z3 is not None:
    def prove(hyps, goal):
        s = z3.Solver(); s.add(*hyps); s.add(z3.Not(goal)); return s.check() == z3.unsat
    # symmetric (tree's encoding, reproduced independently)
    gs = {(a, b): z3.Real('s%d%d' % (min(a, b), max(a, b))) for a in range(4) for b in range(4)}
    trs = z3.Sum([gs[a, a] for a in range(4)]); sqs = z3.Sum([gs[a, b]*gs[a, b] for a in range(4) for b in range(4)])
    chk("z3: symmetric real 4x4, 4 SUM G^2 >= (trG)^2", prove([], 4*sqs >= trs*trs), True)
    chk("z3: equality => G = (trG/4) I",
        prove([4*sqs == trs*trs], z3.And([gs[a, b] == (trs/4 if a == b else 0) for a in range(4) for b in range(a, 4)])), True)
    # general non-symmetric real 4x4: symmetry is NOT needed
    gn = {(a, b): z3.Real('n%d%d' % (a, b)) for a in range(4) for b in range(4)}
    trn = z3.Sum([gn[a, a] for a in range(4)]); sqn = z3.Sum([gn[a, b]*gn[a, b] for a in range(4) for b in range(4)])
    chk("z3: NON-symmetric real 4x4 also satisfies it (symmetry is an added, harmless hypothesis)", prove([], 4*sqn >= trn*trn), True)
    # vacuity guards
    s = z3.Solver(); s.add(z3.Not(3*sqs >= trs*trs)); chk("guard: 3 SUM G^2 >= (trG)^2 is refuted (constant 1/4 is sharp)", s.check() == z3.sat, True)
    s = z3.Solver(); s.add(4*sqs == trs*trs, trs != 0); chk("guard: equality case is attainable (nonvacuous)", s.check() == z3.sat, True)
    # reality IS needed: complex entries with the unconjugated square SUM G_AB^2 can violate it
    re_ = {(a, b): z3.Real('re%d%d' % (min(a, b), max(a, b))) for a in range(4) for b in range(4)}
    im_ = {(a, b): z3.Real('im%d%d' % (min(a, b), max(a, b))) for a in range(4) for b in range(4)}
    tr_re = z3.Sum([re_[a, a] for a in range(4)]); tr_im = z3.Sum([im_[a, a] for a in range(4)])
    sq_re = z3.Sum([re_[a, b]*re_[a, b] - im_[a, b]*im_[a, b] for a in range(4) for b in range(4)])
    s = z3.Solver(); s.add(tr_im == 0, tr_re != 0, z3.Not(4*sq_re >= tr_re*tr_re))
    chk("probe: complex symmetric G with real trace, unconjugated SUM G^2 < (trG)^2/4 is SAT (reality is load-bearing)", s.check() == z3.sat, True)
    # the Delta' step: rho = trG/2, rho != 0  =>  (1/2) SUM G^2 >= (1/2) rho^2
    chk("z3: rho = trG/2 != 0  =>  (1/2)SUM G^2 / rho^2 >= 1/2", prove([trs != 0], sqs/2 >= (trs/2)*(trs/2)/2), True)
    # the 5-component (massive) case: the 1/2 floor is NOT delivered by C-S alone
    g5 = {(a, b): z3.Real('f%d%d' % (min(a, b), max(a, b))) for a in range(5) for b in range(5)}
    tr5 = z3.Sum([g5[a, a] for a in range(5)]); sq5 = z3.Sum([g5[a, b]*g5[a, b] for a in range(5) for b in range(5)])
    s = z3.Solver(); s.add(tr5 != 0, z3.Not(sq5/2 >= (tr5/2)*(tr5/2)/2))
    chk("probe: 5x5 (matrix-level only) -- C-S alone does not give Delta' >= 1/2 (SAT)", s.check() == z3.sat, True)
    chk("z3: 5x5 gives Delta' >= 2/5", prove([tr5 != 0], sq5/2 >= sp.Rational(2, 5).p*(tr5/2)*(tr5/2)/sp.Rational(2, 5).q), True)
else:
    print("z3 not available: z3 checks skipped (pip install z3-solver)"); ok = False

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
