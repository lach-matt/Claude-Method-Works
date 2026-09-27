#!/usr/bin/env python3
"""DOCKET 67 / audit of gr-qc/0009013 (M. Alcubierre, 'The warp drive: hyper-fast travel
within general relativity', CQG 11 (1994) L73-L77; arXiv copy posted 5 Sep 2000).

What the tree uses (research/warp-drive/phase1.py:63-64, 93-94, 254-256, 408-409, 535):
  Alcubierre: "The shift vector gives T^{0i} != 0, so D4 fails" -- and the generalisation
  "T^{0i} = 0 is automatic for a static metric and impossible with a shift vector" /
  "it fails automatically for anything with a shift vector".

The source (eq. 19) computes ONLY the Eulerian energy density; it never computes T^{0i}.
So this script supplies the momentum computation the tree asserts, and tests the
generalisation.  Sign conventions: G = c = 1, signature (-+++), metric eq.(8),
n_mu = (-1,0,0,0), n^mu = (1,-beta^i) (eq.18 with alpha = 1).  T = G/8pi.

  C1  eq.(19): 8pi rho_E = G^{00} = -(1/4) v^2 (y^2+z^2)/r_s^2 f'(r_s)^2        (source check)
  C2  eq.(12): theta = -Tr K = v (x-x_s)/r_s f'                                    (source check)
  C3  the tree's claim for Alcubierre: Eulerian momentum density j_i and coordinate
      T^{0i} for beta^x = -W(t,x,y,z): 8pi j = (-(W_yy+W_zz)/2, W_xy/2, W_xz/2),
      8pi T^{0x} = 8pi(rho n^x + j^x); evaluated for eq.(6) f at a wall point: != 0.
  C3d within Alcubierre's whole class (lapse 1, flat slices, shift along a fixed axis),
      j == 0 everywhere forces W = A(t,x) + B(t,y,z), B harmonic in (y,z); with compact
      support that is W == 0.  Checked: the three PDEs are exactly W_xy = W_xz = 0,
      W_yy + W_zz = 0 (read off C3's symbolic j), plus a z3-free argument recorded in text.
  C4  counterexample A to the generalisation: uniform shift, G == 0 identically.
  C5  counterexample B: rigidly rotating Minkowski, beta^phi = omega, G == 0 identically.
  C6  counterexample C (physical, not gauge): Kerr (M=1, a=0.6), beta^phi != 0,
      Ricci == 0 at three test points (40-digit evaluation of exact expressions).
  C7  zero-vorticity warp (beta = grad Phi; Santiago-Schuster-Visser 2105.03079 sec.4/7):
      Eulerian flux j == 0 identically, yet coordinate T^{0x} != 0 where rho != 0:
      the tree's 'T^{0i}' is frame-dependent and its frame is not named.
Exit 0 when every check returns its recorded expectation.
"""
import sys
import sympy as sp

ok = True


def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ((" :: " + str(detail)) if detail != "" else ""))


def einstein(g, gi, X, red=sp.expand):
    n = len(X)
    Gam = [[[red(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                 - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    s += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            Ric[b, c] = red(s)
    R = red(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return (Ric - R * g / 2).applyfunc(red), Ric


t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]


def shift_metric(beta):            # lapse 1, flat slices, shift beta^i (lower = upper)
    g = sp.zeros(4)
    g[0, 0] = -1 + sum(b**2 for b in beta)
    gi = sp.zeros(4)
    gi[0, 0] = -1
    for i in range(3):
        g[0, i + 1] = g[i + 1, 0] = beta[i]
        g[i + 1, i + 1] = 1
        gi[0, i + 1] = gi[i + 1, 0] = beta[i]
        for j in range(3):
            gi[i + 1, j + 1] = (1 if i == j else 0) - beta[i] * beta[j]
    assert sp.simplify(g * gi) == sp.eye(4)
    return g, gi


# ---------------------------------------------------------------- Alcubierre class, general W
W = sp.Function('W')(t, x, y, z)                      # beta^x = -W ; Alcubierre: W = v_s f(r_s)
g, gi = shift_metric([-W, 0, 0])
G, _ = einstein(g, gi, X)
Gup = (gi * G * gi).applyfunc(sp.expand)
nup = sp.Matrix([1, W, 0, 0])
G00 = sp.factor(Gup[0, 0])
j8 = [sp.factor(-(G[:, i].T * nup)[0]) for i in (1, 2, 3)]      # 8pi j_i
T0i8 = [sp.factor(Gup[0, i]) for i in (1, 2, 3)]                # 8pi T^{0i} (coordinate)
print("   8pi rho_E      =", G00)
print("   8pi j_i        =", j8)
print("   8pi T^{0i}     =", T0i8)

# C1: substitute W = v(t) f(r_s), x_s(t) general
xs = sp.Function('x_s')(t)
v = sp.diff(xs, t)
F = sp.Function('f')
rs = sp.sqrt((x - xs)**2 + y**2 + z**2)
r = sp.Symbol('r', positive=True)
Walc = v * F(rs)
fprime = sp.Subs(sp.Derivative(F(r), r), r, rs)
rho_sub = G00.subs(W, Walc).doit()
target = -sp.Rational(1, 4) * v**2 * (y**2 + z**2) / rs**2 * fprime**2
chk("C1 eq.(19): G^00 = -(1/4) v_s^2 (y^2+z^2)/r_s^2 (df/dr_s)^2  [i.e. T^{mu nu}n_mu n_nu = -(1/8pi) v^2 rho^2/(4 r_s^2) f'^2]",
    sp.simplify(rho_sub.doit() - target.doit()) == 0)

# C2: K_ij = (1/2)(d_i beta_j + d_j beta_i) (eq.10), theta = -alpha Tr K (eq.11)
theta = -sp.diff(-Walc, x)
chk("C2 eq.(12): theta = v_s (x-x_s)/r_s df/dr_s",
    sp.simplify((theta - v * (x - xs) / rs * fprime).doit()) == 0)

# C3: momentum, symbolic identities then Alcubierre's tanh f at a wall point
chk("C3a 8pi j = (-(W_yy+W_zz)/2, W_xy/2, W_xz/2)",
    sp.simplify(j8[0] + (sp.diff(W, y, 2) + sp.diff(W, z, 2)) / 2) == 0
    and sp.simplify(j8[1] - sp.diff(W, x, y) / 2) == 0
    and sp.simplify(j8[2] - sp.diff(W, x, z) / 2) == 0)
chk("C3b coordinate T^{0i} = rho_E n^i + j^i  (n^x = W)",
    sp.simplify(T0i8[0] - (G00 * W + j8[0])) == 0 and sp.simplify(T0i8[1] - j8[1]) == 0
    and sp.simplify(T0i8[2] - j8[2]) == 0)
sig, Rb, v0 = 8, 1, 1          # the source's Fig.1 parameters: sigma = 8, R = v_s = 1
rr = sp.Symbol('rr', positive=True)
ftanh = (sp.tanh(sig * (rr + Rb)) - sp.tanh(sig * (rr - Rb))) / (2 * sp.tanh(sig * Rb))
Wnum = v0 * ftanh.subs(rr, sp.sqrt((x - v0 * t)**2 + y**2 + z**2))
P = {t: 0, x: sp.Rational(7, 10), y: sp.Rational(7, 10), z: sp.Rational(1, 5)}
vals = {name: sp.N(e.subs(W, Wnum).doit().subs(P), 15)
        for name, e in [("8pi rho", G00), ("8pi j_x", j8[0]), ("8pi j_y", j8[1]), ("8pi j_z", j8[2]),
                        ("8pi T0x", T0i8[0]), ("8pi T0y", T0i8[1]), ("8pi T0z", T0i8[2])]}
print("   Alcubierre eq.(6) f, sigma=8, R=v=1, point (t,x,y,z)=(0,.7,.7,.2):", vals)
chk("C3c Alcubierre: Eulerian momentum density j_i != 0 on the wall",
    max(abs(vals[k]) for k in ("8pi j_x", "8pi j_y", "8pi j_z")) > 1e-3)
chk("C3d Alcubierre: coordinate T^{0i} != 0 on the wall",
    max(abs(vals[k]) for k in ("8pi T0x", "8pi T0y", "8pi T0z")) > 1e-3)
# C3e: class statement.  j == 0  <=>  W_xy = W_xz = 0 and W_yy + W_zz = 0 (from C3a).
# W_xy = W_xz = 0 => W = A(t,x) + B(t,y,z); then B_yy + B_zz = 0 (harmonic in the plane).
# Compact support in space: at |y|,|z| outside the support W = 0 for all x, so A(t,x) = -B(t,y0,z0)
# is x-independent; then W = B~(t,y,z) harmonic with compact support in R^2 => B~ = 0 (max principle).
A_, B_ = sp.Function('A')(t, x), sp.Function('B')(t, y, z)
Wsep = A_ + B_
chk("C3e ansatz W = A(t,x)+B(t,y,z) solves W_xy = W_xz = 0 and leaves j = (-(B_yy+B_zz)/2,0,0)",
    [sp.simplify(e.subs(W, Wsep).doit()) for e in j8] == [sp.simplify(-(sp.diff(B_, y, 2) + sp.diff(B_, z, 2)) / 2), 0, 0])

# ---------------------------------------------------------------- the generalisation, counterexamples
vc = sp.Symbol('v', real=True, nonzero=True)
gA, giA = shift_metric([-vc, 0, 0])
GA, _ = einstein(gA, giA, X)
chk("C4 uniform shift beta^x = -v != 0: G_{mu nu} == 0 identically", GA == sp.zeros(4))

om = sp.Symbol('omega', real=True, nonzero=True)
Rc, ph = sp.Symbol('R', positive=True), sp.Symbol('phi', real=True)
gB = sp.Matrix([[-1 + om**2 * Rc**2, 0, om * Rc**2, 0], [0, 1, 0, 0],
                [om * Rc**2, 0, Rc**2, 0], [0, 0, 0, 1]])        # (t,R,phi,z)
giB = gB.inv().applyfunc(sp.simplify)
GB, _ = einstein(gB, giB, [t, Rc, ph, z], red=sp.simplify)
betaB = sp.simplify(gB[0, 2] / gB[2, 2])
chk("C5 rigidly rotating Minkowski, beta^phi = omega != 0: G == 0 identically",
    GB == sp.zeros(4) and betaB == om, "beta^phi = " + str(betaB))

rK, thK = sp.symbols('r theta', positive=True)
M, a = sp.Integer(1), sp.Rational(3, 5)
Sig = rK**2 + a**2 * sp.cos(thK)**2
Del = rK**2 - 2 * M * rK + a**2
gK = sp.zeros(4)
gK[0, 0] = -(1 - 2 * M * rK / Sig)
gK[0, 3] = gK[3, 0] = -2 * M * a * rK * sp.sin(thK)**2 / Sig
gK[1, 1] = Sig / Del
gK[2, 2] = Sig
gK[3, 3] = (rK**2 + a**2 + 2 * M * a**2 * rK * sp.sin(thK)**2 / Sig) * sp.sin(thK)**2
giK = gK.inv().applyfunc(sp.cancel)
_, RicK = einstein(gK, giK, [t, rK, thK, ph], red=sp.cancel)
mx = 0
for (rv, tv) in [(3, sp.Rational(7, 10)), (5, sp.Rational(3, 2)), (sp.Rational(5, 2), 1)]:
    for i in range(4):
        for j in range(4):
            mx = max(mx, abs(sp.N(RicK[i, j].subs({rK: rv, thK: tv}), 40)))
bphi = sp.N((gK[0, 3] / gK[3, 3]).subs({rK: 3, thK: sp.Rational(7, 10)}), 12)
chk("C6 Kerr M=1 a=0.6: Ricci = 0 at 3 points (so T^{0i} = 0) with shift beta^phi = g_{t phi}/g_{phi phi} != 0",
    mx < 1e-30 and abs(bphi) > 1e-3, "max|R_mu nu| = %s, beta^phi(r=3,th=.7) = %s" % (sp.N(mx, 3), bphi))

Phi = sp.Function('Phi')(t, x, y, z)
bZ = [sp.diff(Phi, c) for c in (x, y, z)]
gZ, giZ = shift_metric(bZ)
GZ, _ = einstein(gZ, giZ, X)
nupZ = sp.Matrix([1] + [-b for b in bZ])
jZ = [sp.simplify(-(GZ[:, i].T * nupZ)[0]) for i in (1, 2, 3)]
chk("C7a zero-vorticity warp beta = grad Phi: Eulerian flux j_i == 0 identically", jZ == [0, 0, 0])
GupZ = (giZ * GZ * giZ)
Phi0 = x * sp.exp(-(x**2 + y**2 + z**2))
Pz = {t: 0, x: sp.Rational(1, 2), y: sp.Rational(1, 3), z: sp.Rational(1, 4)}
rhoZ = sp.N(GupZ[0, 0].subs(Phi, Phi0).doit().subs(Pz), 12)
T0xZ = sp.N(GupZ[0, 1].subs(Phi, Phi0).doit().subs(Pz), 12)
chk("C7b same metric, Phi = x exp(-r^2): coordinate T^{0x} != 0 where rho != 0",
    abs(T0xZ) > 1e-4 and abs(rhoZ) > 1e-4, "8pi rho = %s, 8pi T^{0x} = %s" % (rhoZ, T0xZ))

print("\nALL CHECKS " + ("PASS" if ok else "FAIL"))
sys.exit(0 if ok else 1)
