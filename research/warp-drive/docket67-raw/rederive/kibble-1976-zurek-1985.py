#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key kibble-1976-zurek-1985.

The tree's use (warpfolder.py:75-79, 397-398): a rapid quench through a
symmetry-breaking transition gives causally disconnected domains with
independent phases, whose generic output is a TOPOLOGICAL DEFECT NETWORK, not a
templated object -- applied to the Standard Model electroweak transition.

What is checkable here without reading Kibble 1976 / Zurek 1985 (neither could
be READ this stage -- see the audit JSON):

  A. the SM Higgs vacuum manifold M = {H in C^2 : H^dag H = v^2/2} is the round
     3-sphere, SU(2) acts transitively on it, the stabiliser has dim 1
     (dim G - dim H = 4 - 1 = 3 = dim M).                         [sympy]
  B. pi_0, pi_1, pi_2 of S^3 are trivial: explicit null-homotopies of random
     loops and random 2-spheres in S^3 (miss a point, stereographically project,
     contract in R^3, project back), checked to stay on S^3.      [numeric]
     pi_3(S^3) = Z is stated, not computed.
     => in 3 space dimensions the SM EW vacuum manifold carries no
     topologically stable walls (pi_0), strings (pi_1) or monopoles (pi_2).
  C. Zurek's freeze-out algebra in its standard form: tau(eps) = tau0/|eps|^(z nu),
     eps = t/tau_Q, freeze-out tau(eps(t^)) = |t^| => xi^ = xi0 (tau_Q/tau0)^(nu/(1+z nu)).
     And the CROSSOVER case: with a regulated tau, xi (bounded by tau_max, xi_max)
     the freeze-out xi^ saturates at xi_max as tau_Q -> infinity. [sympy+numeric]
  D. the data: T_c (tree 160 'ORDER'; D'Onofrio-Rummukainen 159.5 +/- 1.5 as the
     tree quotes it), m_H/m_Z and on-shell sin^2 theta_W from the tree's
     PDG-2026 capture, m_H against the first-order endpoint ~72 GeV (NAMED-NOT-READ).
"""
import math
import random
import sys

import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ A
print("A. the SM Higgs vacuum manifold")
x1, x2, x3, x4, v = sp.symbols("x1 x2 x3 x4 v", real=True, positive=False)
vp = sp.symbols("v", positive=True)
h1 = x1 + sp.I * x2
h2 = x3 + sp.I * x4
HdH = sp.expand(sp.conjugate(h1) * h1 + sp.conjugate(h2) * h2)
chk("A1 H^dag H = x1^2+x2^2+x3^2+x4^2 (so H^dag H = v^2/2 is S^3 of radius v/sqrt2 in R^4)",
    sp.simplify(HdH - (x1**2 + x2**2 + x3**2 + x4**2)) == 0)
# SU(2) element carrying H0 = (0, v/sqrt2) to an arbitrary H on the manifold
r = vp / sp.sqrt(2)
U = sp.Matrix([[sp.conjugate(h2), h1], [-sp.conjugate(h1), h2]]) / r
H0 = sp.Matrix([0, r])
on = {x4: sp.sqrt(r**2 - x1**2 - x2**2 - x3**2)}
UU = (U.H * U).subs(on).applyfunc(sp.simplify)
chk("A2 U^dag U = 1 on the manifold", UU == sp.eye(2))
chk("A3 det U = 1 on the manifold", sp.simplify(U.det().subs(on)) == 1)
chk("A4 U H0 = H (transitive: SU(2) alone reaches every vacuum)",
    (U * H0 - sp.Matrix([h1, h2])).applyfunc(sp.simplify) == sp.zeros(2, 1))
chk("A5 dim count: dim(SU2xU1)=4, dim(U1_em)=1, 4-1 = 3 = dim S^3", 4 - 1 == 3)

# ------------------------------------------------------------------ B
print("\nB. homotopy of S^3 (numeric witnesses)")
random.seed(67)


def norm(p):
    s = math.sqrt(sum(c * c for c in p))
    return [c / s for c in p]


def rand_s3():
    return norm([random.gauss(0, 1) for _ in range(4)])


def stereo(p, n):
    # project from n (unit) onto the hyperplane orthogonal to n through origin
    d = sum(a * b for a, b in zip(p, n))
    return [(a - d * b) / (1.0 - d) for a, b in zip(p, n)]


def inv_stereo(y, n):
    y2 = sum(c * c for c in y)
    return [(2 * a + (y2 - 1) * b) / (y2 + 1) for a, b in zip(y, n)]


def missed_point(samples):
    # a point of S^3 far from every sample (a 1- or 2-dim image misses an open set)
    best, bd = None, -1.0
    for _ in range(4000):
        q = rand_s3()
        md = min(1.0 - sum(a * b for a, b in zip(q, s)) for s in samples)
        if md > bd:
            best, bd = q, md
    return best, bd


def null_homotopy_ok(samples):
    n, gap = missed_point(samples)
    ys = [stereo(p, n) for p in samples]
    y0 = [0.0] * 4
    worst_off, worst_back = 0.0, 0.0
    for s in [k / 20 for k in range(21)]:
        for p, y in zip(samples, ys):
            ys_ = [(1 - s) * a + s * b for a, b in zip(y, y0)]
            q = inv_stereo(ys_, n)
            worst_off = max(worst_off, abs(sum(c * c for c in q) - 1.0))
            if s == 0.0:
                worst_back = max(worst_back, max(abs(a - b) for a, b in zip(q, p)))
    end = inv_stereo(y0, n)
    return gap > 1e-3 and worst_off < 1e-12 and worst_back < 1e-12, gap, worst_off, end


# pi_0: path-connected -- great-circle arc between two random points
a, b = rand_s3(), rand_s3()
arc_ok = all(abs(sum(c * c for c in norm([(1 - t) * x + t * y for x, y in zip(a, b)])) - 1) < 1e-12
             for t in [k / 50 for k in range(51)])
chk("B1 pi_0(S^3) = 0: any two vacua joined by an arc on S^3 (no domain walls)", arc_ok)

# pi_1: random smooth loops
ok_all = True
for trial in range(20):
    K = 6
    co = [[random.gauss(0, 1) for _ in range(4)] for _ in range(2 * K + 1)]
    loop = []
    for j in range(200):
        th = 2 * math.pi * j / 200
        p = [co[0][i] + sum(co[2 * k - 1][i] * math.cos(k * th) + co[2 * k][i] * math.sin(k * th)
                            for k in range(1, K + 1)) for i in range(4)]
        loop.append(norm(p))
    ok, gap, off, _ = null_homotopy_ok(loop)
    ok_all &= ok
chk("B2 pi_1(S^3) = 0: 20 random Fourier loops each contracted on S^3 (no strings)", ok_all)

# pi_2: random smooth 2-spheres
ok_all = True
for trial in range(10):
    M = [[random.gauss(0, 1) for _ in range(3)] for _ in range(4)]
    c = [random.gauss(0, 0.5) for _ in range(4)]
    sph = []
    for i in range(24):
        th = math.pi * (i + 0.5) / 24
        for j in range(24):
            ph = 2 * math.pi * j / 24
            u = [math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)]
            u2 = [u[0] * u[1], u[1] * u[2], u[2] * u[0]]
            p = [c[k] + sum(M[k][m] * u[m] for m in range(3)) + 0.7 * math.sin(3 * u2[k % 3]) for k in range(4)]
            sph.append(norm(p))
    ok, gap, off, _ = null_homotopy_ok(sph)
    ok_all &= ok
chk("B3 pi_2(S^3) = 0: 10 random smooth 2-spheres each contracted on S^3 (no monopoles)", ok_all)

# pi_3(S^3) = Z (textures) is NOT computed here -- stated only, and whether
# textures are dynamically stable is not decided here either.
print("      pi_3(S^3) = Z (textures): NOT computed here; stated, not checked")

# ------------------------------------------------------------------ C
print("\nC. Zurek's freeze-out algebra (standard form, derived here, source NOT READ)")
t, tQ, t0, xi0, z, nu = sp.symbols("t tau_Q tau_0 xi_0 z nu", positive=True)
tau = t0 / (t / tQ) ** (z * nu)
that = sp.solve(sp.Eq(tau, t), t)
chk("C1 freeze-out time t^ = (tau0 tau_Q^(z nu))^(1/(1+z nu))",
    len(that) == 1 and sp.simplify(sp.log(that[0]) - sp.log((t0 * tQ ** (z * nu)) ** (1 / (1 + z * nu)))) == 0,
    str(that))
eps_hat = sp.simplify(that[0] / tQ)
xihat = sp.simplify(xi0 / eps_hat ** nu)
target = xi0 * (tQ / t0) ** (nu / (1 + z * nu))
chk("C2 xi^ = xi0 (tau_Q/tau0)^(nu/(1+z nu))",
    sp.simplify(sp.expand_log(sp.log(xihat) - sp.log(target), force=True)) == 0)
for name, nv, zv in (("mean field", sp.Rational(1, 2), 2), ("3D XY (nu~0.6717, z=2)", sp.Rational(6717, 10000), 2)):
    ex = nv / (1 + zv * nv)
    print("      exponent nu/(1+z nu), %s: %s = %.4f; string density ~ xi^-2 ~ tau_Q^-%.4f"
          % (name, ex, float(ex), float(2 * ex)))

# crossover: regulate tau and xi with a finite gap delta (no critical point)
print("      crossover model: tau = tau0/(eps^2+d^2)^(z nu/2), xi = xi0/(eps^2+d^2)^(nu/2), d=0.05")


def freeze_xi(tq, d, zz=2.0, nn=0.5, tt0=1.0, x0=1.0):
    f = lambda tt: tt0 / ((tt / tq) ** 2 + d * d) ** (zz * nn / 2) - tt
    lo, hi = 1e-15, 1e15
    if f(lo) < 0:
        return x0 / d ** nn
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    e = lo / tq
    return x0 / (e * e + d * d) ** (nn / 2)


d = 0.05
xs = [(tq, freeze_xi(tq, d), freeze_xi(tq, 0.0 + 1e-300)) for tq in (1e0, 1e2, 1e4, 1e6, 1e8, 1e10)]
for tq, xc, xk in xs:
    print("      tau_Q=%8.0e   xi^(crossover)=%9.4f   xi^(critical, KZ)=%12.4f" % (tq, xc, xk))
xmax = 1.0 / d ** 0.5
chk("C3 crossover: xi^ saturates at xi_max = xi0 d^-nu (%.4f) -- no KZ power law as tau_Q -> inf" % xmax,
    abs(xs[-1][1] - xmax) / xmax < 1e-3 and abs(xs[-2][1] - xmax) / xmax < 1e-3)
chk("C4 critical: xi^ keeps growing as tau_Q^(1/4) (mean field)",
    abs(math.log(xs[-1][2] / xs[-2][2]) / math.log(100) - 0.25) < 1e-3)
chk("C5 rapid quench (tau_Q small): crossover and critical agree -- the fast end is insensitive to d",
    abs(xs[0][1] - xs[0][2]) / xs[0][2] < 0.02, "%.4f vs %.4f" % (xs[0][1], xs[0][2]))

# ------------------------------------------------------------------ D
print("\nD. data")
KB = 1.380649e-23
eV = 1.602176634e-19
tree_Tc = 160.0
DR_Tc, DR_err = 159.5, 1.5
chk("D1 tree T_EW 160 GeV ('ORDER') vs D'Onofrio-Rummukainen 159.5 +/- 1.5 (as tree quotes): %.2f sigma"
    % ((tree_Tc - DR_Tc) / DR_err), abs(tree_Tc - DR_Tc) / DR_err < 1)
print("      160 GeV = %.4e K" % (tree_Tc * 1e9 * eV / KB))
mH, mZ, mW = 125.130, 91.1879, 80.362  # GeV, research/warp-drive/captures/PDG-2026.tsv rows 25, 23, 24
beta = (mH / mZ) ** 2
s2w = 1 - (mW / mZ) ** 2
print("      PDG-2026 capture: m_H=%.3f m_Z=%.4f m_W=%.3f GeV" % (mH, mZ, mW))
print("      beta = m_H^2/m_Z^2 = %.4f ; on-shell sin^2 theta_W = %.4f" % (beta, s2w))
chk("D2 m_H > m_Z (beta > 1): the regime in which semilocal/Z-strings are reported unstable "
    "(criterion NAMED-NOT-READ)", beta > 1)
ENDPOINT = 72.0  # GeV, first-order endpoint, Kajantie et al. 1996 / later lattice -- NAMED-NOT-READ
chk("D3 m_H = %.2f GeV is %.2f x the ~72 GeV first-order endpoint: crossover side (endpoint NAMED-NOT-READ)"
    % (mH, mH / ENDPOINT), mH > ENDPOINT)
hbarc = 197.3269804e-18  # GeV m
print("      Higgs correlation length at T=0: hbar c/m_H = %.4e m" % (hbarc / mH))

print()
if FAIL:
    print("FAILED: %s" % FAIL)
    sys.exit(1)
print("ALL %s CHECKS PASS" % "A-D")
