#!/usr/bin/env python3
"""DOCKET 67 -- audit rederivation for key lens-focal-length-b2-over-4m.

The tree's use (composite.py:48-49, 290-293, 383-388):
  * focal length f = b^2/(4|M|) for a ray at impact parameter b past a mass M;
  * a point source INSIDE f (at fixed b) forms no real image (no conjugate point, det A = 0);
  * |M| is used, so the same f is applied to M < 0;
  * design point b = 0.3, M = 2e-3 -> f = 11.25; source at 40 seats, source at 5 does not.

Checks (nothing carried from memory; every number computed):
  R1 sympy: Riemann tensor of the linearised static metric
       ds^2 = -(1+2 eps Phi) dt^2 + (1-2 eps Phi) dx^2,  Phi generic,
     contracted with the null k = (1,1,0,0): the optical tidal matrix
     T_ab = R_{a k b k}, a,b in {y,z}, at first order in eps.  Trace vs Ricci.
  R2 sympy: for Phi = -M/r on the straight ray y = b, the INTEGRATED transverse
     powers  P_ab = int T_ab dx  -> azimuthal +4M/b^2, radial -4M/b^2 (astigmatic;
     trace 0).  So the focusing direction's power is 4|M|/b^2 for EITHER sign:
     f = b^2/(4|M|).  For M > 0 it is the azimuthal direction (alpha/b, which is
     the 4M/b deflection route); for M < 0 it is the RADIAL direction (-d alpha/db).
  R3 sympy: thin-lens conjugate relation for a point source at D_s:
     1/D_s + 1/D_i = 1/f;  real conjugate (D_i > 0) iff D_s > f.
     Design point f = 11.25 exactly; D_s = 40 -> D_i and lambda_conj = D_s + D_i.
  R4 numeric, independent of composite.py: integrate the 2x2 Jacobi matrix
     A'' = -T A, A(0)=0, A'(0)=I from a point source, (a) along the straight
     (Born) ray with the R1 tidal matrix, (b) along the weak-field bent ray.
     Conjugate points for source 40 (both signs) and source 5 (lambda = 60).
     Sweep of D_s across f to locate where the conjugate point appears.
  R5 (optional, --run-composite) run composite.selftest() read-only (python -B,
     no file in research/ is written).
"""
import math, sys
import sympy as sp

ok_all = True


def check(label, cond, extra=""):
    global ok_all
    ok_all &= bool(cond)
    print("  %-72s %s %s" % (label, "ok" if cond else "FAIL", extra))


# ------------------------------------------------------------------ R1
print("R1 -- optical tidal matrix of the linearised metric (sympy, first order)")
t, x, y, z, eps = sp.symbols("t x y z epsilon")
Phi = sp.Function("Phi")(x, y, z)
X = [t, x, y, z]
g = sp.diag(-(1 + 2 * eps * Phi), 1 - 2 * eps * Phi, 1 - 2 * eps * Phi, 1 - 2 * eps * Phi)
ginv = sp.diag(*[1 / g[i, i] for i in range(4)])


def lin(e):
    return sp.expand(sp.series(e, eps, 0, 2).removeO())


Gam = [[[lin(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]


def Riem_up(a, b, c, d):  # R^a_{bcd}, first order (Gamma*Gamma is O(eps^2))
    return lin(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d]))


k = [1, 1, 0, 0]
T = sp.zeros(2, 2)
for i, a in enumerate((2, 3)):
    for j, b in enumerate((2, 3)):
        # R_{a mu b nu} k^mu k^nu with lowered first index: g_aa R^a_{mu b nu} (flat to O(eps))
        s = 0
        for m in range(4):
            for n in range(4):
                if k[m] and k[n]:
                    s += Riem_up(a, m, b, n) * k[m] * k[n]
        T[i, j] = sp.simplify(lin(s))  # first order; g_aa = 1 at this order
print("  T_yy =", T[0, 0])
print("  T_zz =", T[1, 1])
print("  T_yz =", T[0, 1])
lap = sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2) + sp.diff(Phi, z, 2)
trace = sp.simplify(T[0, 0] + T[1, 1])
check("trace T = 2 eps nabla^2 Phi (so traceless in vacuum, R_kk = 0)",
      sp.simplify(trace - 2 * eps * lap) == 0, "trace=" + str(trace))
Hperp = sp.Matrix([[sp.diff(Phi, y, y), sp.diff(Phi, y, z)], [sp.diff(Phi, y, z), sp.diff(Phi, z, z)]])
# relation to the Born ray-map (transverse Hessian) form 2 Hess_perp Phi
diff_ = sp.simplify(T - 2 * eps * Hperp)
print("  T - 2 eps Hess_perp(Phi) =", diff_)

# ------------------------------------------------------------------ R2
print("\nR2 -- integrated transverse powers along the straight ray y = b (Phi = -M/r)")
M, b, r = sp.symbols("M b r", positive=True)
Mn = sp.symbols("M_n", real=True)
PhiN = -Mn / sp.sqrt(x ** 2 + y ** 2 + z ** 2)
Tn = T.subs(eps, 1)
Tn = Tn.subs(Phi, PhiN).doit()
Tn = sp.simplify(Tn.subs({y: b, z: 0}))
P = Tn.applyfunc(lambda e: sp.simplify(sp.integrate(e, (x, -sp.oo, sp.oo))))
print("  P_yy (radial)    =", P[0, 0])
print("  P_zz (azimuthal) =", P[1, 1])
print("  P_yz             =", P[0, 1])
check("azimuthal power = +4 M/b^2 (the alpha/b of the 4M/b deflection)",
      sp.simplify(P[1, 1] - 4 * Mn / b ** 2) == 0)
check("radial power = -4 M/b^2 (-d alpha/db): astigmatic, trace 0",
      sp.simplify(P[0, 0] + 4 * Mn / b ** 2) == 0)
alpha = 4 * Mn / b
check("radial power equals -d(alpha)/db, azimuthal equals alpha/b",
      sp.simplify(P[0, 0] - sp.diff(alpha, b)) == 0 and sp.simplify(P[1, 1] - alpha / b) == 0)
# focusing (positive) power for either sign of M
fpow = sp.Max(P[0, 0], P[1, 1])
for sgn in (+1, -1):
    val = sp.simplify(fpow.subs(Mn, sgn * M))
    check("M sign %+d: the focusing direction's power = 4|M|/b^2" % sgn,
          sp.simplify(val - 4 * M / b ** 2) == 0, str(val))
# Born-form check: 2 Hess_perp integrates to the same powers (end terms integrate to zero)
HB = (2 * Hperp).subs(Phi, PhiN).doit().subs({y: b, z: 0})
PB = HB.applyfunc(lambda e: sp.simplify(sp.integrate(sp.simplify(e), (x, -sp.oo, sp.oo))))
check("Born ray-map form 2 Hess_perp(Phi) integrates to the same P (infinite line)",
      sp.simplify(PB - P) == sp.zeros(2, 2))

# ------------------------------------------------------------------ R3
print("\nR3 -- thin-lens conjugate relation and the 'no real image inside f' criterion")
Ds, Di, f = sp.symbols("D_s D_i f", positive=True)
DiSol = sp.solve(sp.Eq(1 / Ds + 1 / Di, 1 / f), Di)
Di_expr = f * Ds / (Ds - f)
check("1/D_s + 1/D_i = 1/f  =>  D_i = f D_s/(D_s - f)",
      len(DiSol) == 1 and sp.simplify(DiSol[0] - Di_expr) == 0)
check("D_i > 0 iff D_s > f  (D_s < f: D_i < 0, virtual; D_s = f: D_i = infinity)",
      sp.simplify(Di_expr.subs(Ds, f / 2)) < 0 and sp.simplify(Di_expr.subs(Ds, 2 * f)) > 0)
fdes = sp.Rational(3, 10) ** 2 / (4 * sp.Rational(2, 1000))
check("design point b = 0.3, M = 2e-3: f = 45/4 = 11.25 exactly", fdes == sp.Rational(45, 4), str(fdes))
Di40 = Di_expr.subs({f: fdes, Ds: 40})
lam40 = 40 + Di40
print("  D_s = 40: D_i = %s = %.4f ; lambda_conj (from source) = %.4f" % (Di40, float(Di40), float(lam40)))
print("  composite.py:52-53 prints lambda = 55.16 (M=+2e-3) and 56.52 (M=-2e-3)")
print("  offsets from thin lens: %+.3f and %+.3f ; their mean %+.3f"
      % (55.16 - float(lam40), 56.52 - float(lam40), (55.16 + 56.52) / 2 - float(lam40)))
check("D_s = 5 < f = 11.25: D_i < 0, no real conjugate point at ANY run length",
      Di_expr.subs({f: fdes, Ds: 5}) < 0, "D_i=%s" % Di_expr.subs({f: fdes, Ds: 5}))

# ------------------------------------------------------------------ R4
print("\nR4 -- independent numeric Jacobi integration (not composite.py's code)")
Tfun = sp.lambdify((x, y, z, Mn), list(Tn.subs({b: y}) if False else
                    T.subs(eps, 1).subs(Phi, PhiN).doit()), "math")


def tidal_num(px, py, pz, m):
    v = Tfun(px, py, pz, m)
    return [[v[0], v[1]], [v[2], v[3]]]


def jacobi(m, bb, x0, lam, n=60000, bent=False):
    """Point source at (x0, bb, 0), initial direction +x.  Returns first lambda with det A <= 0."""
    h = lam / n
    py, vy = bb, 0.0       # transverse position/velocity of the ray (bent case)
    A = [[0.0, 0.0], [0.0, 0.0]]
    dA = [[1.0, 0.0], [0.0, 1.0]]

    def acc(px, py_, A_):
        Tm = tidal_num(px, py_, 0.0, m)
        return [[-(Tm[r_][0] * A_[0][c] + Tm[r_][1] * A_[1][c]) for c in range(2)] for r_ in range(2)]

    for i in range(n):
        px = x0 + i * h
        # RK4 on (A, dA) and on the ray (py, vy); ray eq  y'' = -2 dPhi/dy  (weak field)
        def ray_acc(pxx, pyy):
            rr = math.sqrt(pxx * pxx + pyy * pyy)
            return -2.0 * m * pyy / rr ** 3
        if bent:
            k1y, k1v = vy, ray_acc(px, py)
            k2y, k2v = vy + 0.5 * h * k1v, ray_acc(px + 0.5 * h, py + 0.5 * h * k1y)
            k3y, k3v = vy + 0.5 * h * k2v, ray_acc(px + 0.5 * h, py + 0.5 * h * k2y)
            k4y, k4v = vy + h * k3v, ray_acc(px + h, py + h * k3y)
            ys = [py, py + 0.5 * h * k1y, py + 0.5 * h * k2y, py + h * k3y]
        else:
            ys = [bb] * 4
        a1 = acc(px, ys[0], A)
        A2 = [[A[r_][c] + 0.5 * h * dA[r_][c] for c in range(2)] for r_ in range(2)]
        dA2 = [[dA[r_][c] + 0.5 * h * a1[r_][c] for c in range(2)] for r_ in range(2)]
        a2 = acc(px + 0.5 * h, ys[1], A2)
        A3 = [[A[r_][c] + 0.5 * h * dA2[r_][c] for c in range(2)] for r_ in range(2)]
        dA3 = [[dA[r_][c] + 0.5 * h * a2[r_][c] for c in range(2)] for r_ in range(2)]
        a3 = acc(px + 0.5 * h, ys[2], A3)
        A4 = [[A[r_][c] + h * dA3[r_][c] for c in range(2)] for r_ in range(2)]
        dA4 = [[dA[r_][c] + h * a3[r_][c] for c in range(2)] for r_ in range(2)]
        a4 = acc(px + h, ys[3], A4)
        for r_ in range(2):
            for c in range(2):
                A[r_][c] += h / 6 * (dA[r_][c] + 2 * dA2[r_][c] + 2 * dA3[r_][c] + dA4[r_][c])
                dA[r_][c] += h / 6 * (a1[r_][c] + 2 * a2[r_][c] + 2 * a3[r_][c] + a4[r_][c])
        if bent:
            py += h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
            vy += h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        if i > 5 and A[0][0] * A[1][1] - A[0][1] * A[1][0] <= 0.0:
            return (i + 1) * h
    return None


rows = {}
for bent in (False, True):
    tag = "bent" if bent else "Born"
    for m in (2e-3, -2e-3):
        c40 = jacobi(m, 0.3, -40.0, 75.0, bent=bent)
        c5 = jacobi(m, 0.3, -5.0, 60.0, bent=bent)
        rows[(tag, m)] = (c40, c5)
        print("  %-4s M=%+.1e  source 40 (lam 75): conj %s   source 5 (lam 60): conj %s"
              % (tag, m, "%.3f" % c40 if c40 else "none", "%.3f" % c5 if c5 else "none"))
for (tag, m), (c40, c5) in rows.items():
    check("%s M=%+.0e: source 40 seats within 1.5 of thin-lens %.2f" % (tag, m, float(lam40)),
          c40 is not None and abs(c40 - float(lam40)) < 1.5, "%.3f" % (c40 or -1))
    check("%s M=%+.0e: source 5 (inside f) does not seat in lambda = 60" % (tag, m), c5 is None)
cb_p, cb_m = rows[("bent", 2e-3)][0], rows[("bent", -2e-3)][0]
print("  bent-ray split between signs: %.3f vs composite's 56.52-55.16 = %.2f" % (cb_m - cb_p, 56.52 - 55.16))
check("bent ray reproduces the sign ordering of composite.py (M<0 conjugate later than M>0)",
      cb_m > cb_p)

print("\n  sweep: source distance D_s across f = 11.25 (Born, M=+2e-3, run to 4000 past lens)")
first = None
for Dsv in (8.0, 10.0, 11.0, 11.5, 12.0, 13.0, 15.0, 20.0):
    c = jacobi(2e-3, 0.3, -Dsv, Dsv + 4000.0, n=120000)
    thin = Dsv * 11.25 / (Dsv - 11.25) if Dsv > 11.25 else None
    print("    D_s=%5.1f  numeric D_i=%s  thin-lens D_i=%s"
          % (Dsv, "%.1f" % (c - Dsv) if c else "none(<=4000)", "%.1f" % thin if thin else "virtual"))
    if c and first is None:
        first = Dsv
check("no conjugate point for D_s <= 11.0; first appears in (11.0, 11.5] (thin lens: 11.25)",
      first == 11.5)

print("\nR4b -- the fixed-b qualifier: the SAME point source at D_s = 5 seen through a smaller b")
fb = 0.15 ** 2 / (4 * 2e-3)
thin_b = fb * 5.0 / (5.0 - fb)
c_small = jacobi(2e-3, 0.15, -5.0, 60.0, bent=True)
print("  b = 0.15: f = %.4f < D_s = 5 ; thin-lens D_i = %.3f ; numeric conj at lambda = %s"
      % (fb, thin_b, "%.3f" % c_small if c_small else "none"))
check("a source inside b^2/4M at b = 0.3 DOES form a real conjugate point through b = 0.15",
      c_small is not None and abs((c_small - 5.0) - thin_b) < 0.5)
print("  => 'a source inside f forms no real image' holds for the rays at THAT b, not for the lens")

print("\nR6 -- the only physical datum: PPN gamma in alpha = 2(1+gamma)M/b  => f = b^2/(2(1+gamma)M)")
for lab, gm1, sig in (("VLBI, Barcelo-Visser gr-qc/0003025 eq.5.52 (as restated there)", -0.6e-4, 3.1e-4),):
    rel = abs(gm1) / 2 + 3 * sig / 2
    print("  %s: |df/f| <= |gamma-1|/2 + 3 sigma/2 = %.1e" % (lab, rel))
    check("gamma at its measured value moves f = 11.25 by < 0.01 (source-5 margin is 6.25)",
          11.25 * rel < 0.01, "%.2e" % (11.25 * rel))
print("  composite.py's metric is GR by construction (gamma = 1): no datum enters its focal length")

# ------------------------------------------------------------------ R5
if "--run-composite" in sys.argv:
    print("\nR5 -- composite.selftest(), read-only")
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import composite
    rc = composite.selftest()
    check("composite.selftest() exits 0", rc == 0)

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
