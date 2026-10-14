#!/usr/bin/env python3
"""
DOCKET 67, pass S, item 23 -- elementary-flatness-regular-axis.

Machine-checks the regular-axis condition as research/warp-drive/axial.py uses it
("regular axis: W(0) = 0 and W'(0) = 1", axial.py:43-44, 186) from first principles.
Reads nothing under research/, drive/ or method/.  Run from this directory
(recovered/struct.py shadows stdlib struct if the repo root is on sys.path).

    python3 elementary-flatness-regular-axis.py      exits 0 iff every check passes

Metric (axial.py:33):  ds^2 = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + e^{2Psi}dz^2 + W^2 dphi^2,
phi taken with period 2*pi*k (k = 1 is the convention axial.py assumes without stating).
"""
import sys
import sympy as sp
from scipy.integrate import quad
import math

ok = True


def chk(label, cond):
    global ok
    ok = ok and bool(cond)
    print("%-4s %s" % ("PASS" if cond else "FAIL", label))


r, eps, R = sp.symbols('r epsilon R', positive=True)
k, a, b = sp.symbols('k a b', positive=True)
t, z, ph = sp.symbols('t z phi', real=True)
Phi, Lam, Psi, W = [sp.Function(n)(r) for n in ('Phi', 'Lambda', 'Psi', 'W')]

# ---------------------------------------------------------------- A. invariant form
# Elementary flatness, invariant form (Mars & Senovilla 1993, restated -- NOT read here):
#   lim_axis  g^{ab} d_a X d_b X / (4X) = 1,  X = xi.xi,  xi = d_phi normalised to period 2 pi.
# With period 2 pi k, the 2pi-normalised Killing vector is xi = k d_phi, so X = k^2 W^2.
X = k**2 * W**2
Q = sp.simplify(sp.exp(-2 * Lam) * sp.diff(X, r)**2 / (4 * X))
chk("A1 invariant EF quantity = k^2 e^{-2Lambda} W'^2  (got %s)" % Q,
    sp.simplify(Q - k**2 * sp.exp(-2 * Lam) * sp.diff(W, r)**2) == 0)
Q0 = Q.subs(Lam, 0).doit()
chk("A2 Lambda = 0 gauge, k = 1: EF <=> W'(0)^2 = 1, i.e. W'(0) = +1 given W > 0 off the axis",
    sp.simplify(Q0.subs(k, 1) - sp.diff(W, r)**2) == 0)

# ---------------------------------------------------------------- B. geometric form
# Proper radius rho = r (Lambda = 0), circumference C = 2 pi k W(r).  lim C / (2 pi rho).
Wt = sp.Function('Wt')
w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)
Wser = w1 * r + w2 * r**2 + w3 * r**3            # W(0) = 0, W'(0) = w1
ratio = sp.limit(2 * sp.pi * k * Wser / (2 * sp.pi * r), r, 0)
chk("B1 lim C/(2 pi rho) = k W'(0)  (got %s)" % ratio, sp.simplify(ratio - k * w1) == 0)
deficit = sp.simplify(2 * sp.pi * (1 - ratio))
print("     deficit angle = %s ; no cone <=> k W'(0) = 1" % deficit)
chk("B2 with k = 1 the no-cone condition is exactly W'(0) = 1 (axial.py:186)",
    sp.solve(sp.Eq(ratio.subs(k, 1), 1), w1) == [1])
chk("B3 with k != 1, W'(0) = 1 leaves a cone: deficit(k=1/2, w1=1) = %s" %
    deficit.subs({k: sp.Rational(1, 2), w1: 1}), deficit.subs({k: sp.Rational(1, 2), w1: 1}) != 0)

# ---------------------------------------------------------------- C. the identity it feeds
x = [t, r, z, ph]
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), sp.exp(2 * Psi), W**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[A, D] * (sp.diff(g[D, B], x[C]) + sp.diff(g[D, C], x[B])
                                     - sp.diff(g[B, C], x[D])) for D in range(n)) / 2)
         for C in range(n)] for B in range(n)] for A in range(n)]
Ric = sp.zeros(n)
for B in range(n):
    for C in range(n):
        Ric[B, C] = sp.simplify(sum(sp.diff(Gam[A][B][C], x[A]) for A in range(n))
                                - sum(sp.diff(Gam[A][B][A], x[C]) for A in range(n))
                                + sum(Gam[A][A][D] * Gam[D][B][C] for A in range(n) for D in range(n))
                                - sum(Gam[A][C][D] * Gam[D][B][A] for A in range(n) for D in range(n)))
Rs = sp.simplify(sum(gi[A, B] * Ric[A, B] for A in range(n) for B in range(n)))
Gtt_mixed = sp.simplify(gi[0, 0] * (Ric[0, 0] - g[0, 0] * Rs / 2))   # G^t_t
u = -Gtt_mixed / (8 * sp.pi)                                         # u = -T^t_t
lhs = sp.simplify((8 * sp.pi * u * W).subs(Lam, 0).doit())
Wp, Pp = sp.diff(W, r), sp.diff(Psi, r)
rhs = -sp.diff(W * Pp, r) - W * Pp**2 - sp.diff(W, r, 2)
chk("C1 8 pi u W = -(W Psi')' - W Psi'^2 - W''  in Lambda = 0 (residual %s)" %
    sp.simplify(lhs - rhs), sp.simplify(lhs - rhs) == 0)
chk("C2 Phi absent from u", not sp.simplify(lhs).has(Phi))

# ---------------------------------------------------------------- D. boundary terms, exactly
# INT_eps^R rhs dr = [-W Psi' - W']_eps^R - INT_eps^R W Psi'^2 dr   (fundamental theorem)
bnd = (-(W * Pp) - Wp)
chk("D1 rhs + W Psi'^2 is the exact derivative of -(W Psi' + W')",
    sp.simplify(sp.diff(bnd, r) - (rhs + W * Pp**2)) == 0)
# Axis end contributes  W(eps) Psi'(eps) + W'(eps).  EF gives W'(0) = 1; the OTHER axis term
# W Psi' -> 0 is NOT part of "W(0) = 0, W'(0) = 1": it needs Psi' bounded (or o(1/r)) at r = 0.
# Period-invariant form of the conical term: W'(0) - W'(inf) = (k W'(0) - k W'(inf)) / k,
# which vanishes when regular axis (k W'(0) = 1) and flatness (k W'(inf) = 1) both hold.
wa, wi = sp.symbols('wa winf', positive=True)
term = wa - wi
chk("D2 conical term vanishes for any period once both normalisations are period-invariant",
    sp.simplify(term.subs({wa: 1 / k, wi: 1 / k})) == 0)


# ---------------------------------------------------------------- E. numeric test profiles
def lhs_num(Wf, dW, d2W, dP, d2P, e, Rm):
    f = lambda s: -((dP(s)**2 + d2P(s)) * Wf(s) + dP(s) * dW(s) + d2W(s))
    return quad(f, e, Rm, limit=400, points=None)[0]


def grad_num(Wf, dP, e, Rm):
    return quad(lambda s: -Wf(s) * dP(s)**2, e, Rm, limit=400)[0]


# E1  W = r, Psi = a log(r/(1+r)): EF holds, g_zz -> 0 at the axis (singular), W Psi' -> a.
A = 0.3
W1 = lambda s: s; dW1 = lambda s: 1.0; d2W1 = lambda s: 0.0
dP1 = lambda s: A * (1 / s - 1 / (1 + s)); d2P1 = lambda s: A * (-1 / s**2 + 1 / (1 + s)**2)
vals = [lhs_num(W1, dW1, d2W1, dP1, d2P1, e, 200.0) for e in (1e-2, 1e-4, 1e-6)]
print("     E1 INT_eps^200 8 pi u W at eps = 1e-2,1e-4,1e-6:", ["%.4f" % v for v in vals])
chk("E1 axis term W Psi' -> a != 0 does not rescue positivity: integral -> -inf (log)",
    vals[0] > vals[1] > vals[2] and (vals[1] - vals[2]) > 0.8 * A * A * math.log(100))

# E2  W = r, Psi' = a r^{-1/2} e^{-r}: Psi' unbounded but W Psi' -> 0, EF holds.
dP2 = lambda s: A * s**-0.5 * math.exp(-s)
d2P2 = lambda s: A * math.exp(-s) * (-0.5 * s**-1.5 - s**-0.5)
L2 = lhs_num(W1, dW1, d2W1, dP2, d2P2, 1e-10, 60.0)
G2 = grad_num(W1, dP2, 1e-10, 60.0)
print("     E2 INT 8 pi u W = %.8f , -INT W Psi'^2 = %.8f" % (L2, G2))
chk("E2 theorem equality holds with unbounded Psi' when W Psi' -> 0", abs(L2 - G2) < 1e-4)

# E3  W = r + B r^2 e^{-r^2}: EF holds (W(0)=0, W'(0)=1) but W''(0) = 2B != 0, so the
#     (r,phi) Gaussian curvature -W''/W ~ -2B/r diverges: the axis is NOT regular (not C^2),
#     yet the theorem's equality still holds -- EF is what the theorem uses, and EF is
#     necessary, not sufficient, for a regular axis.
B = 0.4
Wx = r + b * r**2 * sp.exp(-r**2)
Kg = sp.simplify(-sp.diff(Wx, r, 2) / Wx)
lim = sp.limit(Kg * r, r, 0)
chk("E3a EF profile with W''(0) = 2b: r * Gaussian curvature -> %s (curvature ~ 1/r, singular)" % lim,
    sp.simplify(lim + 2 * b) == 0)
W3 = sp.lambdify(r, Wx.subs(b, B)); dW3 = sp.lambdify(r, sp.diff(Wx, r).subs(b, B))
d2W3 = sp.lambdify(r, sp.diff(Wx, r, 2).subs(b, B))
P3 = 0.5 * sp.exp(-r**2)
dP3 = sp.lambdify(r, sp.diff(P3, r)); d2P3 = sp.lambdify(r, sp.diff(P3, r, 2))
L3 = lhs_num(W3, dW3, d2W3, dP3, d2P3, 0.0, 40.0); G3 = grad_num(W3, dP3, 0.0, 40.0)
print("     E3 INT 8 pi u W = %.10f , -INT W Psi'^2 = %.10f" % (L3, G3))
chk("E3b theorem equality holds on this non-C^2 (curvature-singular) but elementary-flat axis",
    abs(L3 - G3) < 1e-8)

# E4  conical defect: W = (1-d) r + ..., the identity's term (W'(0) - 1) appears exactly.
d = 0.05
W4 = lambda s: (1 - d) * s + d * s * math.tanh(s)**2 if s > 0 else 0.0
dW4 = lambda s: (1 - d) + d * (math.tanh(s)**2 + 2 * s * math.tanh(s) / math.cosh(s)**2)
d2W4 = lambda s: d * (4 * math.tanh(s) / math.cosh(s)**2
                      + 2 * s * (1 / math.cosh(s)**4 - 2 * math.tanh(s)**2 / math.cosh(s)**2))
L4 = lhs_num(W4, dW4, d2W4, dP3, d2P3, 0.0, 40.0); G4 = grad_num(W4, dP3, 0.0, 40.0)
print("     E4 excess = %.10f vs W'(0)-1 = %.10f" % (L4 - G4, -d))
chk("E4 the conical term W'(0) - 1 is what EF removes", abs((L4 - G4) + d) < 1e-8)

print("\nALL PASS" if ok else "\nSOME FAILED")
sys.exit(0 if ok else 1)
