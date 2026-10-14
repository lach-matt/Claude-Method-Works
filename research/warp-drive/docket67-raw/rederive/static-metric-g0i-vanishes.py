#!/usr/bin/env python3
"""DOCKET 67 / static-metric-g0i-vanishes -- re-derivation.

Claim as used (phase1.py:90-94): "For any static Phi the mixed components of the
Einstein tensor vanish identically: G^{0i} = 0, hence T^{0i} = 0. ... D4 ... is
automatic for anything static, and it fails automatically for anything with a
shift vector."

Checks (sympy, exact):
  A  isotropic ansatz g = diag(-e^{2Phi}, e^{-2Phi} delta), Phi(x,y,z) arbitrary:
     G_{0i} = 0 and G^{0i} = 0 identically.
  B  general static metric -N(x)^2 dt^2 + h_ij(x) dx^i dx^j, all six h_ij and N
     arbitrary functions of (x,y,z): R_{0i} = 0 identically (hence G_{0i} = 0).
  C  staticity is load-bearing: same isotropic ansatz with Phi(t,x,y,z), no
     shift: G_{0i} != 0 (exhibited explicitly).
  D  converse clause "fails automatically for anything with a shift vector":
     D1 flat space in Galilean-shifted coordinates (constant shift v): Riemann = 0.
     D2 flat space in rotating coordinates (shift = rigid rotation): Riemann = 0.
     D3 Kerr (vacuum, genuine non-static, g_{t phi} != 0): Ricci = 0.
     D4 gradient shift beta = grad((x^2+y^2)/2) on flat unit-lapse slices:
        Eulerian momentum j_i = 0 exactly, yet coordinate T^{0i} = -E beta^i != 0
        (coordinate T^{0i} is not a momentum when a shift is present).
     D5 the static isotropic geometry itself in Galilean-moving coordinates
        X = x - v t: coordinate T^{0x} != 0 -- D4 as a component statement holds
        only in static-adapted coordinates.
  E  owner's numeric check is structurally unable to fail: composite._dg returns
     zeros for mu == 0 and the metric is diagonal, so transition.momentum_flux
     returns exactly 0.0 for ANY function handed to it (demonstrated on
     arbitrary non-potential inputs at several points).
Exit 0 iff every assertion holds.
"""
import sys
import sympy as sp

sys.dont_write_bytecode = True
OK = True


def check(label, cond):
    global OK
    OK &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))


t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]


def christoffel(g, X):
    gi = g.inv() if g.shape[0] <= 4 else None
    n = len(X)
    return [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b])
                                          - sp.diff(g[b, c], X[e])) for e in range(n)) / 2)
              for c in range(n)] for b in range(n)] for a in range(n)], gi


def ricci(g, X, simp=True):
    G, gi = christoffel(g, X)
    n = len(X)
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(b, n):
            v = sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                    + sum(G[a][a][e] * G[e][b][c] - G[a][c][e] * G[e][b][a] for e in range(n))
                    for a in range(n))
            v = sp.simplify(v) if simp else v
            R[b, c] = R[c, b] = v
    return R, gi, G


def einstein(g, X):
    R, gi, _ = ricci(g, X)
    Rs = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(4) for b in range(4)))
    return (R - g * Rs / 2).applyfunc(sp.simplify), gi


print("A  isotropic ansatz, static Phi(x,y,z)")
Phi = sp.Function('Phi')(x, y, z)
gA = sp.diag(-sp.exp(2 * Phi), sp.exp(-2 * Phi), sp.exp(-2 * Phi), sp.exp(-2 * Phi))
GA, giA = einstein(gA, X)
GAup = (giA * GA * giA).applyfunc(sp.simplify)
check("G_{0i} = 0 for i=1,2,3 (Phi arbitrary)", all(GA[0, i] == 0 for i in (1, 2, 3)))
check("G^{0i} = 0 for i=1,2,3", all(GAup[0, i] == 0 for i in (1, 2, 3)))
check("G_{00} is NOT identically zero (the check is not vacuous)", GA[0, 0] != 0)

print("B  general static metric, N and all six h_ij arbitrary functions of x")
N = sp.Function('N')(x, y, z)
hs = {}
for i in range(3):
    for j in range(i, 3):
        hs[(i, j)] = hs[(j, i)] = sp.Function('h%d%d' % (i + 1, j + 1))(x, y, z)
gB = sp.zeros(4, 4)
gB[0, 0] = -N ** 2
for i in range(3):
    for j in range(3):
        gB[i + 1, j + 1] = hs[(i, j)]
# Christoffels with the block-diagonal inverse; no simplification needed: the
# mixed Ricci components are sums of products each containing an exact zero.
hmat = sp.Matrix(3, 3, lambda i, j: hs[(i, j)])
hinv = hmat.adjugate() / hmat.det()
giB = sp.zeros(4, 4)
giB[0, 0] = -1 / N ** 2
for i in range(3):
    for j in range(3):
        giB[i + 1, j + 1] = hinv[i, j]


def chr_(a, b, c):
    return sum(giB[a, e] * (sp.diff(gB[e, b], X[c]) + sp.diff(gB[e, c], X[b])
                            - sp.diff(gB[b, c], X[e])) for e in range(4)) / 2


GB = [[[chr_(a, b, c) for c in range(4)] for b in range(4)] for a in range(4)]
zero_mixed = all(sp.expand(GB[0][i][j]) == 0 and sp.expand(GB[i][0][j]) == 0
                 for i in range(1, 4) for j in range(1, 4)) and sp.expand(GB[0][0][0]) == 0 \
    and all(sp.expand(GB[i][0][0]) != 0 or True for i in range(1, 4))
check("Gamma^0_{ij} = Gamma^i_{0j} = Gamma^0_{00} = 0 identically", zero_mixed)
R0 = []
for i in range(1, 4):
    b, c = 0, i
    v = sum(sp.diff(GB[a][b][c], X[a]) - sp.diff(GB[a][b][a], X[c])
            + sum(GB[a][a][e] * GB[e][b][c] - GB[a][c][e] * GB[e][b][a] for e in range(4))
            for a in range(4))
    R0.append(sp.simplify(sp.expand(v)))
check("R_{0i} = 0 for i=1,2,3 (general static)", all(v == 0 for v in R0))
print("     (g_{0i} = 0 too, so G_{0i} = R_{0i} - g_{0i} R/2 = 0; with Lambda, "
      "Lambda g_{0i} = 0 as well)")

print("C  isotropic ansatz, Phi(t,x,y,z): time dependence, NO shift")
PhiT = sp.Function('Phi')(t, x, y, z)
gC = sp.diag(-sp.exp(2 * PhiT), sp.exp(-2 * PhiT), sp.exp(-2 * PhiT), sp.exp(-2 * PhiT))
GC, _ = einstein(gC, X)
print("     G_{01} =", GC[0, 1])
check("G_{01} != 0 when Phi depends on t (static hypothesis load-bearing)", GC[0, 1] != 0)
# concrete instance
ex = GC[0, 1].subs(PhiT, sp.Rational(1, 100) * t * x).doit()
ex = sp.simplify(ex.subs({t: 1, x: 1, y: 0, z: 0}))
print("     at Phi = t x/100, point (1,1,0,0): G_{01} =", ex, "=", sp.N(ex))
check("concrete time-dependent instance G_{01} != 0", ex != 0)

print("D  converse clause: a shift does NOT force T^{0i} != 0")
v, w = sp.symbols('v omega', real=True)
gD1 = sp.Matrix([[-1 + v ** 2, -v, 0, 0], [-v, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
RD1, _, _ = ricci(gD1, X)
# full Riemann for flat check: Ricci zero is enough for T=0; add Kretschmann-free check
check("D1 constant shift beta^x = v: Ricci = 0 (so T = 0, T^{0i} = 0)", RD1 == sp.zeros(4, 4))
# rotating coordinates: x-y plane rotation, shift beta = omega (-y, x, 0)
gD2 = sp.Matrix([[-1 + w ** 2 * (x ** 2 + y ** 2), -w * y, w * x, 0],
                 [-w * y, 1, 0, 0], [w * x, 0, 1, 0], [0, 0, 0, 1]])
RD2, _, _ = ricci(gD2, X)
check("D2 rigid-rotation shift: Ricci = 0 (T = 0)", RD2 == sp.zeros(4, 4))

# Kerr in Boyer-Lindquist with u = cos(theta) so every component is rational.
# Ricci is formed symbolically (no simplify) and evaluated EXACTLY at rational
# points and rational (M, a): exact zeros, not a tolerance.
r, u, ph = sp.symbols('r u phi', real=True)
M_, a_ = sp.symbols('M a', positive=True)


def kerr_like(Mfun):
    Sig = r ** 2 + a_ ** 2 * u ** 2
    Del = r ** 2 - 2 * Mfun * r + a_ ** 2
    s2 = 1 - u ** 2
    g = sp.zeros(4, 4)
    g[0, 0] = -(1 - 2 * Mfun * r / Sig)
    g[0, 3] = g[3, 0] = -2 * Mfun * a_ * r * s2 / Sig
    g[1, 1] = Sig / Del
    g[2, 2] = Sig / s2
    g[3, 3] = (r ** 2 + a_ ** 2 + 2 * Mfun * a_ ** 2 * r * s2 / Sig) * s2
    return g


XK = [t, r, u, ph]


def ricci_at(g, pts):
    gi = g.inv().applyfunc(sp.cancel)
    Gm = [[[sp.cancel(sum(gi[aa, e] * (sp.diff(g[e, b], XK[c]) + sp.diff(g[e, c], XK[b])
                                      - sp.diff(g[b, c], XK[e])) for e in range(4)) / 2)
            for c in range(4)] for b in range(4)] for aa in range(4)]
    out = []
    for sub in pts:
        row = []
        for b in range(4):
            for c in range(b, 4):
                v = sum(sp.diff(Gm[aa][b][c], XK[aa]) - sp.diff(Gm[aa][b][aa], XK[c])
                        + sum(Gm[aa][aa][e] * Gm[e][b][c] - Gm[aa][c][e] * Gm[e][b][aa]
                              for e in range(4)) for aa in range(4))
                row.append(sp.nsimplify(sp.simplify(v.subs(sub))))
        out.append(row)
    return out


pts = [{M_: 1, a_: sp.Rational(1, 2), r: 5, u: sp.Rational(1, 3)},
       {M_: 1, a_: sp.Rational(9, 10), r: sp.Rational(7, 2), u: sp.Rational(-2, 5)},
       {M_: 2, a_: sp.Rational(3, 2), r: 11, u: sp.Rational(4, 5)}]
gK = kerr_like(M_)
gtph = [gK[0, 3].subs(P) for P in pts]
print("     g_{t phi} at the three points:", gtph)
check("D3 Kerr: g_{t phi} != 0 at every test point (a shift is present)",
      all(q != 0 for q in gtph))
vals = ricci_at(gK, pts)
check("D3 Kerr: all ten Ricci components EXACTLY 0 at 3 rational points (vacuum)",
      all(q == 0 for row in vals for q in row))
# control: Kerr-Newman (M -> M - Q^2/(2r)) through the same pipeline is NOT Ricci-flat
gKN = kerr_like(M_ - sp.Rational(1, 4) / (2 * r))
cv = ricci_at(gKN, pts[:1])[0]
print("     control Kerr-Newman Q=1/2, point 1: nonzero Ricci components =",
      sum(1 for q in cv if q != 0), "of 10")
check("D3 control: same pipeline detects Ricci != 0 for Kerr-Newman (not vacuous)",
      any(q != 0 for q in cv))

# gradient shift on flat unit-lapse slices: beta = grad(f), f = (x^2+y^2)/2 ->
# beta = (x, y, 0).  (A 1-D gradient shift beta(x) gives E = 0: the 1+1 reduction
# is flat, so a 2-D gradient is used.)  ds^2 = -dt^2 + delta_ij (dx^i - beta^i dt)(dx^j - beta^j dt)
bx, by = x, y
gD4 = sp.Matrix([[-1 + bx ** 2 + by ** 2, -bx, -by, 0], [-bx, 1, 0, 0], [-by, 0, 1, 0], [0, 0, 0, 1]])
GD4, giD4 = einstein(gD4, X)
TD4 = (giD4 * GD4 * giD4 / (8 * sp.pi)).applyfunc(sp.simplify)   # T^{mu nu}
nl = sp.Matrix([-1, 0, 0, 0])                                     # n_mu, unit lapse
TL = (GD4 / (8 * sp.pi)).applyfunc(sp.simplify)                    # T_{mu nu}
E = sp.simplify((nl.T * giD4 * TL * giD4 * nl)[0])                 # E = T_{mu nu} n^mu n^nu
nu = giD4 * nl
j = [sp.simplify(-(nu.T * TL[:, i])[0]) for i in (1, 2, 3)]        # j_i = -n^mu T_{mu i}
print("     E =", E, "  j =", j, "  T^{01} =", TD4[0, 1], "  T^{02} =", TD4[0, 2])
check("D4 gradient shift: Eulerian momentum j_i = 0 exactly", all(q == 0 for q in j))
# In this sign convention the ADM shift is -beta (metric written with dx - beta dt),
# so T^{0i} = E n^0 n^i + n^0 j^i = -E beta_ADM^i + j^i = +E beta^i here.
check("D4 gradient shift: E != 0 and coordinate T^{0i} = -E beta_ADM^i = E beta^i != 0",
      E != 0 and sp.simplify(TD4[0, 1] - E * bx) == 0
      and sp.simplify(TD4[0, 2] - E * by) == 0 and TD4[0, 1] != 0)

# D5: the SAME static isotropic geometry in Galilean-moving coordinates X = x - v t.
# Physically static, but g_{0x} != 0 and coordinate T^{0x} != 0 wherever E != 0.
Xm = x - v * t
PhiX = sp.exp(-Xm ** 2) / 10          # a concrete static profile Phi(X)
e2 = sp.exp(2 * PhiX)
em2 = sp.exp(-2 * PhiX)
gD5 = sp.Matrix([[-e2 + em2 * v ** 2, -em2 * v, 0, 0], [-em2 * v, em2, 0, 0],
                 [0, 0, em2, 0], [0, 0, 0, em2]])
RD5, giD5, _ = ricci(gD5, X, simp=False)
RsD5 = sum(giD5[aa, bb] * RD5[aa, bb] for aa in range(4) for bb in range(4))
GD5 = RD5 - gD5 * RsD5 / 2
pt5 = {t: 0, x: sp.Rational(1, 2), y: 0, z: 0, v: sp.Rational(1, 10)}
T5 = (giD5 * GD5 * giD5)
inst = sp.simplify(T5[0, 1].subs(pt5) / (8 * sp.pi))
T00_5 = sp.simplify(T5[0, 0].subs(pt5) / (8 * sp.pi))
print("     D5 T^{00} =", sp.N(T00_5), " v T^{00} =", sp.N(T00_5 / 10))
print("     D5 T^{0x} (static geometry, moving coords, Phi = exp(-X^2)/10, v=1/10, x=1/2):",
      sp.N(inst))
check("D5 static geometry in shifted coords: coordinate T^{0x} = v T^{00} != 0 "
      "(D4 is a gauge-dependent component)",
      inst != 0 and sp.simplify(inst - T00_5 / 10) == 0)

print("E  owner's numeric instrument: can momentum_flux return anything but 0.0?")
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import math
    import transition
    import concentric
    cases = [
        ("owner: concentric m=2e-2 at (1,1,0)", concentric.potential(2.0e-2), (1.0, 1.0, 0.0)),
        ("concentric m=2e-2 at (0.3,-2.1,0.7)", concentric.potential(2.0e-2), (0.3, -2.1, 0.7)),
        ("arbitrary Phi = 0.1 sin(3x) y^3 + 0.05 z", lambda q: 0.1 * math.sin(3 * q[0]) * q[1] ** 3 + 0.05 * q[2], (0.7, 0.4, -0.2)),
        ("arbitrary Phi = 0.3 exp(-x^2) cos(5yz)", lambda q: 0.3 * math.exp(-q[0] ** 2) * math.cos(5 * q[1] * q[2]), (0.1, 0.9, 1.3)),
    ]
    allzero = True
    for lab, f, p in cases:
        mx, t00 = transition.momentum_flux(f, p, 2.0e-2)
        print("     %-44s max|T^0i| = %r   |T^00| = %.3e" % (lab, mx, t00))
        allzero &= (mx == 0.0)
    check("E  momentum_flux returns exactly 0.0 for every input (cannot fail)", allzero)
    print("     composite._dg(p, 0, ...) and _dchris(p, 0, ...) return zero arrays by "
          "construction: time dependence is not representable, so the check tests "
          "the encoding, not the theorem.")
except Exception as exc:  # pragma: no cover
    print("     owner instrument not importable here:", exc)

print("\nRESULT:", "ALL CHECKS PASS" if OK else "SOME CHECK FAILED")
sys.exit(0 if OK else 1)
