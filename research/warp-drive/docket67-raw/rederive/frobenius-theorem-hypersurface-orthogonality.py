#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key frobenius-theorem-hypersurface-orthogonality.

Tree use: research/warp-drive/foliation.py:104-122 (lemma) and :658-674 (V5, V6).
Claim as used: for ANY rapidity w(t,r), u' = cosh w u + sinh w n is unit timelike,
has twist u'_[a d_b u'_c] = 0 in all 64 components, and (Frobenius) "each such u'
is the normal of a foliation"; in the adapted chart the metric is again diagonal.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
 C1  V5 re-run exactly as the tree: diagonal (t,r) block, Phi,Lambda,R of (t,r),
     w(t,r) free -> number of nonzero components of the twist, and V6.
 C2  Generalisation: ANY 1-form u = A(t,r)dt + B(t,r)dr on ANY warped product
     g = h_AB(t,r) dx^A dx^B + R(t,r)^2 dOmega^2 (h with off-diagonal term) has
     u ^ du = 0 identically; and the covariant form (nabla) equals the partial form.
 C3  Vacuity guards: the same detector returns NONZERO for (a) a 1-form with an
     angular leg f(r) dphi, (b) the tree's u' with w depending on theta. So the
     zero in C1 is content, and w independent of the angles is load-bearing.
 C4  Linear-algebra identity: for unit timelike u, u ^ F = 0  <=>  h.F.h = 0
     (twist-form of Frobenius  <=>  zero vorticity, the Ellis-van Elst form).
 C5  Spherical symmetry forces u into the (t,r) plane: a tangent vector on S^2
     fixed by the isotropy rotations is zero.
 C6  Frobenius's CONCLUSION constructed numerically for smooth w on the
     Schwarzschild exterior chart: tau with d tau ∝ u', rho with d rho ∝ n',
     g^{-1}(d tau, d rho) = 0 (adapted chart diagonal), d tau ^ d rho != 0.
 C7  Named hypothesis REGULARITY: a continuous, non-Lipschitz w
     (tanh w = sgn(t) sqrt|t|) gives a spherically symmetric unit timelike field
     whose orthogonal line field has THREE integral curves through (t=0, r=c):
     no foliation has it as normal. The literal 'w arbitrary' needs w C^1
     (classical) or Lipschitz (Simic 1996 / Rampazzo 2007).
 C8  Named hypothesis LOCALITY: smooth metric and smooth w for which the leaf
     through a point exits the chart in finite r (blow-up), so the naive global
     time function 'intercept at r0' is undefined outside a neighbourhood --
     the theorem's conclusion is local, as Frobenius states it.
"""
import sys
import math
import itertools
import sympy as sp
from sympy.combinatorics import Permutation
import numpy as np
from scipy.integrate import solve_ivp

FAIL = []


def report(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]


def twist_components(uc):
    """number of nonzero components of the tree's V5 expression (64 index triples)."""
    bad = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                e = (uc[a] * (sp.diff(uc[c], x[b]) - sp.diff(uc[b], x[c]))
                     + uc[b] * (sp.diff(uc[a], x[c]) - sp.diff(uc[c], x[a]))
                     + uc[c] * (sp.diff(uc[b], x[a]) - sp.diff(uc[a], x[b])))
                if sp.simplify(e) != 0:
                    bad += 1
    return bad


# ---------------------------------------------------------------- C1
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
w = sp.Function("w")(t, r)
u = sp.Matrix([sp.exp(-Phi), 0, 0, 0])
n = sp.Matrix([0, sp.exp(-Lam), 0, 0])
up = sp.cosh(w) * u + sp.sinh(w) * n
uc = g * up
bad = twist_components(uc)
norm = sp.simplify((up.T * g * up)[0, 0] + 1)
report("C1 V5 re-run: nonzero twist components of 64, w(t,r) free", bad == 0, "count=%d" % bad)
report("C1 V6 re-run: u'.u' + 1", norm == 0, "residual=%s" % norm)

# ---------------------------------------------------------------- C2
A = sp.Function("A")(t, r)
B = sp.Function("B")(t, r)
hTT = sp.Function("hTT")(t, r)
hTR = sp.Function("hTR")(t, r)
hRR = sp.Function("hRR")(t, r)
g2 = sp.Matrix([[hTT, hTR, 0, 0], [hTR, hRR, 0, 0], [0, 0, R**2, 0],
                [0, 0, 0, R**2 * sp.sin(th)**2]])
ucov = sp.Matrix([A, B, 0, 0])
bad2 = twist_components(ucov)
report("C2 any 1-form A dt + B dr (warped product, off-diagonal h): twist", bad2 == 0,
       "nonzero=%d" % bad2)
# covariant vs partial: Christoffel terms cancel under antisymmetrisation
gi = g2.inv()
Gam = [[[sum(gi[a, d] * (sp.diff(g2[d, b], x[c]) + sp.diff(g2[d, c], x[b])
                         - sp.diff(g2[b, c], x[d])) for d in range(4)) / 2
         for c in range(4)] for b in range(4)] for a in range(4)]
Pw = sp.Function("P")(t, r, th, ph)
Qw = sp.Function("Q")(t, r, th, ph)
Sw = sp.Function("S")(t, r, th, ph)
Tw = sp.Function("T")(t, r, th, ph)
v = [Pw, Qw, Sw, Tw]  # arbitrary 1-form, arbitrary dependence
maxdiff = 0
for (a, b, c) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
    def nab(i, j):  # nabla_i v_j
        return sp.diff(v[j], x[i]) - sum(Gam[k][i][j] * v[k] for k in range(4))
    cov = sum(Permutation(list(p)).signature()
              * v[[a, b, c][p[0]]] * nab([a, b, c][p[1]], [a, b, c][p[2]])
              for p in itertools.permutations(range(3)))
    par = sum(Permutation(list(p)).signature()
              * v[[a, b, c][p[0]]] * sp.diff(v[[a, b, c][p[2]]], x[[a, b, c][p[1]]])
              for p in itertools.permutations(range(3)))
    dd = sp.simplify(cov - par)
    maxdiff += 0 if dd == 0 else 1
report("C2 v_[a nabla_b v_c] == v_[a d_b v_c] for arbitrary v (torsion-free)", maxdiff == 0,
       "differing triples=%d" % maxdiff)

# ---------------------------------------------------------------- C3 vacuity
f = sp.Function("f")(r)
ug = sp.Matrix([-1, 0, 0, f])  # dt + f(r) dphi  (a twisting 1-form)
bad3a = twist_components(ug)
wth = sp.Function("W")(t, r, th)
up3 = sp.cosh(wth) * u + sp.sinh(wth) * n
bad3b = twist_components(g * up3)
report("C3a guard: -dt + f(r) dphi has NONZERO twist", bad3a > 0, "nonzero=%d" % bad3a)
report("C3b guard: tree's u' with w(t,r,theta) has NONZERO twist", bad3b > 0,
       "nonzero=%d" % bad3b)

# ---------------------------------------------------------------- C4
eta = sp.diag(-1, 1, 1, 1)
okC4 = True
for (bx, by, bz) in [(sp.Rational(1, 3), sp.Rational(-1, 5), sp.Rational(2, 7)),
                     (sp.Rational(3, 5), 0, 0), (sp.Rational(-1, 9), sp.Rational(4, 9), sp.Rational(1, 9))]:
    bb = bx**2 + by**2 + bz**2
    gam = 1 / sp.sqrt(1 - bb)
    uu = sp.Matrix([gam, gam * bx, gam * by, gam * bz])   # vector
    ul = eta * uu                                          # 1-form
    hmix = sp.eye(4) + uu * ul.T                           # h^a_b
    Fs = sp.symbols("F01 F02 F03 F12 F13 F23")
    F = sp.zeros(4, 4)
    for (i, j), s in zip([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], Fs):
        F[i, j] = s
        F[j, i] = -s
    wedge = []
    for (a, b, c) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
        wedge.append(ul[a] * F[b, c] + ul[b] * F[c, a] + ul[c] * F[a, b])
    proj = (hmix.T * F * hmix)
    projl = [proj[i, j] for i in range(4) for j in range(i + 1, 4)]
    M1 = sp.Matrix([[sp.diff(e, s) for s in Fs] for e in wedge])
    M2 = sp.Matrix([[sp.diff(e, s) for s in Fs] for e in projl])
    N1 = M1.nullspace()
    N2 = M2.nullspace()
    same = (len(N1) == len(N2) and
            sp.Matrix.hstack(*N1).rank() == sp.Matrix.hstack(*(N1 + N2)).rank())
    okC4 = okC4 and same and len(N1) == 3
report("C4 u^F=0 <=> hFh=0 (kernel dims 3=3, same span), 3 exact boosts", okC4)

# ---------------------------------------------------------------- C5
al, va, vb = sp.symbols("alpha a b", real=True)
Rot = sp.Matrix([[sp.cos(al), -sp.sin(al)], [sp.sin(al), sp.cos(al)]])
sol = sp.solve(list((Rot * sp.Matrix([va, vb]) - sp.Matrix([va, vb])).subs(al, sp.pi / 2)),
               [va, vb], dict=True)
report("C5 tangent vector on S^2 fixed by isotropy rotation is zero", sol == [{va: 0, vb: 0}],
       str(sol))

# ---------------------------------------------------------------- C6 (numeric)
M = 1.0


def PhiN(tt, rr): return 0.5 * math.log(1 - 2 * M / rr)
def LamN(tt, rr): return -0.5 * math.log(1 - 2 * M / rr)
def wN(tt, rr): return 0.6 * math.sin(0.7 * tt) / (1 + 0.1 * (rr - 6) ** 2) + 0.2


def tau_of(tt, rr, r0=6.0):
    # leaf orthogonal to u': dt/dr = e^{Lam-Phi} tanh w ; tau = t at r = r0
    s = solve_ivp(lambda R_, y: [math.exp(LamN(y[0], R_) - PhiN(y[0], R_)) * math.tanh(wN(y[0], R_))],
                  [rr, r0], [tt], rtol=1e-12, atol=1e-12)
    return s.y[0, -1]


def rho_of(tt, rr, t0=0.0):
    # integral curve of u': dr/dt = e^{Phi-Lam} tanh w ; rho = r at t = t0
    s = solve_ivp(lambda T_, y: [math.exp(PhiN(T_, y[0]) - LamN(T_, y[0])) * math.tanh(wN(T_, y[0]))],
                  [tt, t0], [rr], rtol=1e-12, atol=1e-12)
    return s.y[0, -1]


worst_tau = worst_rho = worst_orth = 0.0
min_jac = 1e9
hstep = 1e-5
for (tt, rr) in [(0.3, 5.0), (-0.8, 7.5), (1.1, 4.2), (0.0, 9.0), (2.0, 6.5)]:
    ph_, la_, ww = PhiN(tt, rr), LamN(tt, rr), wN(tt, rr)
    ut, ur = -math.exp(ph_) * math.cosh(ww), math.exp(la_) * math.sinh(ww)   # u'_a
    nt, nr = -math.exp(ph_) * math.sinh(ww), math.exp(la_) * math.cosh(ww)   # n'_a
    dtt = (tau_of(tt + hstep, rr) - tau_of(tt - hstep, rr)) / (2 * hstep)
    dtr = (tau_of(tt, rr + hstep) - tau_of(tt, rr - hstep)) / (2 * hstep)
    drt = (rho_of(tt + hstep, rr) - rho_of(tt - hstep, rr)) / (2 * hstep)
    drr = (rho_of(tt, rr + hstep) - rho_of(tt, rr - hstep)) / (2 * hstep)
    worst_tau = max(worst_tau, abs(ut * dtr - ur * dtt) / (abs(ut * dtr) + abs(ur * dtt)))
    worst_rho = max(worst_rho, abs(nt * drr - nr * drt) / (abs(nt * drr) + abs(nr * drt)))
    gtt, grr = -math.exp(-2 * ph_), math.exp(-2 * la_)
    orth = gtt * dtt * drt + grr * dtr * drr
    worst_orth = max(worst_orth, abs(orth) / (abs(gtt * dtt * drt) + abs(grr * dtr * drr)))
    min_jac = min(min_jac, abs(dtt * drr - dtr * drt))
report("C6 d tau ∝ u' (relative wedge residual)", worst_tau < 1e-6, "%.2e" % worst_tau)
report("C6 d rho ∝ n' (relative wedge residual)", worst_rho < 1e-6, "%.2e" % worst_rho)
report("C6 adapted chart diagonal: g^-1(dtau,drho) (relative)", worst_orth < 1e-6, "%.2e" % worst_orth)
report("C6 (tau,rho) is a chart: |d tau ^ d rho| > 0", min_jac > 1e-3, "min=%.3f" % min_jac)

# ---------------------------------------------------------------- C7 regularity
# tanh w = sgn(t) sqrt|t| (|t| < 1/4): continuous, not Lipschitz at t = 0.
# Minkowski block, Phi = Lam = 0. Leaves: dt/dr = sgn(t) sqrt|t|.
ts = sp.symbols("t_s", real=True)
c = sp.Rational(3)
cands = {"t=0": sp.Integer(0),
         "t=+(r-c)^2/4 (r>c)": (r - c)**2 / 4,
         "t=-(r-c)^2/4 (r>c)": -(r - c)**2 / 4}
resid = {}
for name, h in cands.items():
    rhs = sp.sign(h) * sp.sqrt(sp.Abs(h))
    e = sp.diff(h, r) - rhs
    resid[name] = [sp.nsimplify(sp.N(e.subs(r, rv), 30), tolerance=1e-25)
                   for rv in (c + sp.Rational(1, 10), c + sp.Rational(1, 2), c + 1)]
all_solve = all(all(z == 0 for z in vals) for vals in resid.values())
distinct = len({sp.N(h.subs(r, c + 1)) for h in cands.values()}) == 3
# the field is unit timelike and in the (t,r) plane for |t|<1/4:
tv = 0.2
wv = math.atanh(math.copysign(math.sqrt(abs(tv)), tv))
unit = -math.cosh(wv) ** 2 + math.sinh(wv) ** 2
report("C7 non-Lipschitz w: 3 distinct integral curves of the leaf field through (0,c)",
       all_solve and distinct and abs(unit + 1) < 1e-12,
       "residuals all 0: %s; u'.u'=%.1f" % (all_solve, unit))

# ---------------------------------------------------------------- C8 locality
# metric -dt^2 + e^{2 t^2} dr^2 + r^2 dOmega^2 (smooth), w = 1 constant (smooth).
# Leaf: dt/dr = e^{t^2} tanh(1)  -> t reaches +inf at finite r (Riccati-type blow-up).
# Parametrise the leaf by t (well-behaved): dr/dt = e^{-t^2}/tanh(1).
s8 = solve_ivp(lambda T_, y: [math.exp(-T_ ** 2) / math.tanh(1.0)], [0.0, 12.0], [1.0],
               rtol=1e-12, atol=1e-14)
rstar = s8.y[0, -1]                     # r reached as t -> 12 (~ infinity)
rexact = 1 + (math.sqrt(math.pi) / 2) / math.tanh(1.0)
# A point whose leaf never meets r = 1: need r_p - 1 > (sqrt(pi)/2)(1+erf(t_p))/tanh(1)
tp, rp = 0.0, 3.5
reach = (math.sqrt(math.pi) / 2) * (1 + math.erf(tp)) / math.tanh(1.0)
report("C8 smooth data: leaf through (t=0,r=1) reaches only r* < inf as t -> inf; "
       "leaf through (0,3.5) never meets r=1 (tau := intercept at r=1 undefined there)",
       abs(rstar - rexact) < 1e-9 and rp - 1 > reach,
       "r*(numeric)=%.10f r*(exact)=%.10f; max r-span back from (0,3.5)=%.4f < 2.5"
       % (rstar, rexact, reach))

print()
print("SUMMARY: %d FAIL" % len(FAIL) + ("" if not FAIL else " -> " + ", ".join(FAIL)))
sys.exit(1 if FAIL else 0)
