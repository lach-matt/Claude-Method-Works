#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Newton's shell theorem as research/warp-drive uses it.

Owners: concentric.py:30-31,55-63,163-168,358-359 ; stability.py:73-77,106-112,118-121,269-272.
Nothing here edits the tree.  G = c = 1 throughout (the tree's units).

  S1  sympy: potential of a uniform thin shell at distance d, by the exact angular integral:
      -M/R for d<R (constant), -M/d for d>R.                        [Principia I, Prop 70/71]
  S2  sympy: interior field d(Phi)/dd = 0 and interior Hessian (tidal tensor) = 0.
  S3  sympy: the tree's encoding -m/max(r,R_s) (concentric.py:164,167) IS the S1 piecewise form.
  S4  sympy: the linearised metric -(1+2c)dt^2+(1-2c)dx^2 with c constant has Riemann == 0
      exactly (shell adds delay, no tidal field); ANY linearised Phi gives R_0i0j = d_i d_j Phi.
  S5  numeric: direct quadrature force on an OFF-CENTRE point core, d/R = 0..0.99, both core signs;
      and the third law: force on the rigid shell from that core.
  S6  numeric: the tree's own numbers -- shell delay / core advance = (L/R_s)/(2 ln(L/a))
      (concentric.py:325) at L=300, R_s=200, a=0.02 gives ~7.8 %, the verdict's '~8 %'.
  S7  scope: a ray that CROSSES the shell meets Ricci (matter) focusing 8 pi sigma / cos(alpha) per
      crossing; ratio to the core's focal power 4m/b^2 is b^2/R_s^2 (2.5e-5 at b=1, R_s=200).
      Zero for the tree's measured ray (x from -150 to +150, wholly inside R_s = 200).
  S8  scope: Plummer core (concentric.py:164) is not compactly supported; mass fraction beyond R_s
      and the resulting force on a displaced core -- non-zero, O(1e-8) relative.
  S9  hypothesis probe: replace 1/r by a Yukawa-corrected kernel (1 + alpha e^{-r/lam})/r: the
      interior potential is no longer constant, so 'zero force at every interior point' requires
      the exact inverse-square law (Newtonian limit of GR), a hypothesis, not a free fact.
"""
import math, sys
import sympy as sp
from scipy import integrate

ok_all = True
def chk(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))

# ---------------------------------------------------------------- S1, S2
print("S1/S2  uniform thin shell, exact angular integral")
R, d, M, th = sp.symbols("R d M theta", positive=True)
u = sp.symbols("u", real=True)  # u = cos(theta)
sigma = M / (4 * sp.pi * R**2)
# Phi(d) = -sigma * 2 pi R^2 * int_{-1}^{1} du / sqrt(R^2 + d^2 - 2 R d u)
anti = sp.integrate(1 / sp.sqrt(R**2 + d**2 - 2 * R * d * u), u)
val = sp.simplify(anti.subs(u, 1) - anti.subs(u, -1))  # = (|R+d| - |R-d|)/(R d)
val_in = sp.simplify(((R + d) - (R - d)) / (R * d))    # d < R : |R-d| = R-d
val_out = sp.simplify(((R + d) - (d - R)) / (R * d))   # d > R : |R-d| = d-R
# confirm the antiderivative difference equals (|R+d|-|R-d|)/(Rd) numerically at both regimes
for dd in (sp.Rational(1, 3), sp.Rational(7, 2)):
    a1 = float(val.subs({R: 1, d: dd}))
    a2 = float(((1 + dd) - abs(1 - dd)) / dd)
    chk("antiderivative difference = (|R+d|-|R-d|)/(R d) at R=1, d=%s" % dd, abs(a1 - a2) < 1e-12)
Phi_in = sp.simplify(-sigma * 2 * sp.pi * R**2 * val_in)
Phi_out = sp.simplify(-sigma * 2 * sp.pi * R**2 * val_out)
print("       Phi_in(d)  =", Phi_in, "   Phi_out(d) =", Phi_out)
chk("interior potential is -M/R (independent of d)", sp.simplify(Phi_in + M / R) == 0)
chk("exterior potential is -M/d (Prop 71)", sp.simplify(Phi_out + M / d) == 0)
chk("interior field dPhi/dd == 0 identically", sp.diff(Phi_in, d) == 0)
x, y, z = sp.symbols("x y z", real=True)
Phi3 = Phi_in.subs(d, sp.sqrt(x**2 + y**2 + z**2))
H = sp.hessian(Phi3, (x, y, z))
chk("interior tidal tensor d_i d_j Phi == 0 (all 9 components)", all(sp.simplify(e) == 0 for e in H))

# ---------------------------------------------------------------- S3
print("S3  the tree's encoding -m/max(r,R_s)")
m, Rs, r = sp.symbols("m R_s r", positive=True)
enc = -m / sp.Max(r, Rs)
chk("r<R_s branch = -m/R_s", sp.simplify(enc.subs(r, Rs / 2) + m / Rs) == 0)
chk("r>R_s branch = -m/r", sp.simplify(enc.subs(r, 2 * Rs) + m / (2 * Rs)) == 0)
# distributional Laplacian: jump of dPhi/dr at R_s equals 4 pi sigma = m / R_s^2
jump = sp.diff(-m / r, r).subs(r, Rs) - 0
chk("jump in dPhi/dr at R_s = m/R_s^2 = 4 pi sigma", sp.simplify(jump - m / Rs**2) == 0)

# ---------------------------------------------------------------- S4
print("S4  linearised metric, constant Phi inside")
t = sp.symbols("t")
X = [t, x, y, z]
def riemann_nonzero(g):
    ginv = g.inv()
    n = 4
    Gam = [[[sum(ginv[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                 for e in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    out = []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    e = sp.diff(Gam[a][b][dd], X[c]) - sp.diff(Gam[a][b][c], X[dd]) + sum(
                        Gam[a][c][k] * Gam[k][b][dd] - Gam[a][dd][k] * Gam[k][b][c] for k in range(n))
                    e = sp.simplify(e)
                    if e != 0:
                        out.append(((a, b, c, dd), e))
    return out
c0 = sp.symbols("c", real=True)
g_const = sp.diag(-(1 + 2 * c0), 1 - 2 * c0, 1 - 2 * c0, 1 - 2 * c0)
chk("Riemann of diag(-(1+2c),(1-2c),..) with c constant is identically 0 (exact, not linearised)",
    riemann_nonzero(g_const) == [])
eps = sp.symbols("epsilon")
F = sp.Function("Phi")(x, y, z)
g_lin = sp.diag(-(1 + 2 * eps * F), 1 - 2 * eps * F, 1 - 2 * eps * F, 1 - 2 * eps * F)
# R^x_{t x t} to first order in eps: tidal = d_x d_x Phi (well-known; checked here)
ginv = g_lin.inv()
def Gam(a, b, c):
    return sum(ginv[a, e] * (sp.diff(g_lin[e, b], X[c]) + sp.diff(g_lin[e, c], X[b]) - sp.diff(g_lin[b, c], X[e]))
               for e in range(4)) / 2
a_, b_, c_, d_ = 1, 0, 1, 0
Rxtxt = sp.diff(Gam(a_, b_, d_), X[c_]) - sp.diff(Gam(a_, b_, c_), X[d_]) + sum(
    Gam(a_, c_, k) * Gam(k, b_, d_) - Gam(a_, d_, k) * Gam(k, b_, c_) for k in range(4))
lin = sp.simplify(sp.series(Rxtxt, eps, 0, 2).removeO().coeff(eps, 1))
chk("linearised R^x_{txt} = d_x^2 Phi (tidal field = Hessian of Phi)",
    sp.simplify(lin - sp.diff(F, x, 2)) == 0, "[got %s]" % lin)

# ---------------------------------------------------------------- S5
print("S5  direct quadrature: force on an off-centre point core, and the third law")
def shell_force_on_point(dz, Rsh=1.0, Msh=1.0, mc=1.0):
    # Newtonian force on point mass mc at (0,0,dz) from a uniform shell; F_i = mc * g_i
    sig = Msh / (4 * math.pi * Rsh**2)
    def integrand(thv):
        # azimuth integrated analytically: only the z-component survives by symmetry
        zs = Rsh * math.cos(thv); rho = Rsh * math.sin(thv)
        dx = zs - dz
        s3 = (rho * rho + dx * dx) ** 1.5
        return sig * 2 * math.pi * Rsh**2 * math.sin(thv) * dx / s3  # attraction toward shell element
    val, err = integrate.quad(integrand, 0, math.pi, limit=400, epsabs=1e-13, epsrel=1e-12,
                              points=[math.acos(max(-1, min(1, dz)))] if 0 < dz < 1 else None)
    return mc * val, err
for dz in (0.0, 0.25, 0.5, 0.9, 0.99):
    for mc in (+1.0, -1.0):
        Fz, err = shell_force_on_point(dz, mc=mc)
        chk("F_z on core m_c=%+.0f at d/R=%.2f" % (mc, dz), abs(Fz) < 1e-9, "(F_z=%.2e, quad err %.1e)" % (Fz, err))
# third law: force on the shell from the point core = - force on core
for dz in (0.5, 0.9):
    Fz, _ = shell_force_on_point(dz, mc=-1.0)
    chk("force on rigid shell from core at d/R=%.1f = -F_core = 0" % dz, abs(-Fz) < 1e-9)
# exterior check: the same routine gives -M m/d^2 outside (validates the quadrature)
Fz_out, _ = shell_force_on_point(2.0)
chk("quadrature validated outside: F_z(d=2R) = -M m/d^2 = -0.25", abs(Fz_out + 0.25) < 1e-9, "(%.12f)" % Fz_out)

# ---------------------------------------------------------------- S6
print("S6  the tree's own delay budget (concentric.py:325, 360-362)")
LAM, R_S, A = 300.0, 200.0, 0.02
ratio = (LAM / R_S) / (2 * math.log(LAM / A))
print("       shell delay 2mL/R_s over core advance 4m ln(L/a): %.4f" % ratio)
chk("shell delay is ~8 % of the core advance, as the verdict prints", 0.07 < ratio < 0.085)
xmax = math.hypot(150.0, 1.0)
chk("measured ray (x in [-150,150], b=1) stays inside R_s=200 at all points", xmax < R_S, "(r_max=%.3f)" % xmax)

# ---------------------------------------------------------------- S7
print("S7  scope: a ray that CROSSES the shell")
b = 1.0
cosal = math.sqrt(1 - (b / R_S) ** 2)
# per unit m: optical Ricci term int R_ab k^a k^b dl = 2 * int lap(Phi) dl = 2 * 4 pi sigma / cos(alpha)
shell_focus_per_crossing = 2 * (1.0 / R_S**2) / cosal       # = 8 pi sigma / cos(alpha), sigma = m/(4 pi R_s^2)
core_focus = 4.0 / b**2                                      # 1/f = 4m/b^2 (concentric.py f = b^2/4m)
rel = 2 * shell_focus_per_crossing / core_focus
print("       two crossings / core focal power = %.3e  (b^2/R_s^2 = %.3e)" % (rel, (b / R_S) ** 2))
chk("crossing-ray shell focusing is non-zero but O(b^2/R_s^2)", abs(rel - (b / R_S) ** 2) / (b / R_S) ** 2 < 1e-3)

# ---------------------------------------------------------------- S8
print("S8  scope: the Plummer core is not compactly supported")
frac_out = 1 - R_S**3 / (R_S**2 + A**2) ** 1.5
print("       Plummer mass fraction beyond R_s = %.3e (1.5 a^2/R_s^2 = %.3e)" % (frac_out, 1.5 * A**2 / R_S**2))
def plummer_force_displaced(dz, Rsh=R_S, a=A, Msh=1.0, mc=-1.0):
    # force on a Plummer core of total mass mc centred at (0,0,dz) from the shell: only core mass
    # at |x| > Rsh feels the exterior field -Msh xhat/|x|^2.
    norm = 3.0 / (4 * math.pi * a**3)
    def rho(s):
        return norm * (1 + (s / a) ** 2) ** -2.5
    def inner(ct, rr):
        s = math.sqrt(max(rr * rr + dz * dz - 2 * rr * dz * ct, 0.0))
        return rho(s) * ct  # z-component of xhat
    def outer(rr):
        v, _ = integrate.quad(inner, -1, 1, args=(rr,), epsabs=0, epsrel=1e-10)
        return 2 * math.pi * rr * rr * v * (-Msh / rr**2)
    v, _ = integrate.quad(outer, Rsh, 50 * Rsh, epsabs=0, epsrel=1e-8, limit=400)
    v2, _ = integrate.quad(outer, 50 * Rsh, math.inf, epsabs=0, epsrel=1e-8, limit=400)
    return mc * (v + v2)
for dz in (50.0, 100.0):
    Fz = plummer_force_displaced(dz)
    print("       m=1 Plummer core (mc=-1), displaced %.0f: F_z = %+.3e  (compare M m/R_s^2 = %.3e)" %
          (dz, Fz, 1 / R_S**2))
    chk("displaced Plummer core: force non-zero but < 1e-7 of M m/R_s^2", 0 < abs(Fz) < 1e-7 / R_S**2)

# ---------------------------------------------------------------- S9
print("S9  hypothesis probe: Yukawa-corrected kernel (1 + alpha e^{-r/lam})/r")
al, lam = sp.symbols("alpha lambda", positive=True)
s = sp.symbols("s", positive=True)
# shell potential with kernel e^{-s/lam}/s: int over shell = sigma*2pi R^2 int du e^{-s/lam}/s,
# ds = -(R d / s) du  =>  int_{|R-d|}^{R+d} e^{-s/lam} ds / (R d)
PhiY_in = -sigma * 2 * sp.pi * R**2 * al * sp.integrate(sp.exp(-s / lam), (s, R - d, R + d)) / (R * d)
PhiY_in = sp.simplify(PhiY_in)
print("       Yukawa part inside:", PhiY_in)
closed = -M * al * lam * sp.exp(-R / lam) * sp.sinh(d / lam) / (R * d)
chk("Yukawa interior = -alpha M lam e^{-R/lam} sinh(d/lam)/(R d)",
    sp.simplify((PhiY_in - closed).rewrite(sp.exp)) == 0)
dPhi = sp.diff(closed, d)
num = float(dPhi.subs({M: 1, al: sp.Rational(1, 100), lam: 1, R: 1, d: sp.Rational(1, 2)}))
chk("with alpha != 0 the interior field is NOT zero (d=R/2, lam=R, alpha=0.01)", abs(num) > 1e-6, "(dPhi/dd=%.3e)" % num)
chk("alpha -> 0 recovers the shell theorem", sp.limit(dPhi, al, 0) == 0)

print("\nALL PASS" if ok_all else "\nSOME FAIL")
sys.exit(0 if ok_all else 1)
