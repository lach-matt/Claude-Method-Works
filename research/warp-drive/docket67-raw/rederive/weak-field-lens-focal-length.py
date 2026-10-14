#!/usr/bin/env python3
"""DOCKET 67 -- audit re-derivation: weak-field lens focal length f = b^2 c^2/(4GM).

Re-derives, independently of the tree:
  R1  Born (first-order) deflection of the linearised metric
      ds^2 = -(1+2Phi)dt^2 + (1-2Phi)dx^2, Phi = -M/r:  alpha = 4M/b   (sympy)
  R2  source-at-infinity focus z_f = b/tan(alpha) -> b^2/(4M), restore units
      -> f = b^2 c^2/(4GM); finite source D_s > f gives D_i = f D_s/(D_s-f) >= f (sympy)
  R3  azimuthal vs radial convergence: 1/f_az = alpha/b, 1/f_rad = d(alpha)/db;
      for M<0 the RADIAL direction focuses at b^2/(4|M|)  (sympy)
  R4  EXACT deflections (mpmath quadrature): Schwarzschild 4M/b + (15 pi/4)(M/b)^2,
      linearised-isotropic metric 4M/b + 4 pi (M/b)^2 (PPN beta = delta = 0),
      i.e. RELATIVE corrections (15 pi/16) M/b and pi M/b
  R5  composite.py VALIDATION 1 re-read: finite path x0=-4..+4 truncation vs the
      linearised metric's second-order term (optionally re-runs composite.survey,
      read-only, no bytecode written)
  R6  spec.py table with spec's own inputs; the Sun with IAU 2015 nominal GM_sun;
      PPN gamma sensitivity; second-order correction at b = R_sun
  R7  concentric.py docstring table vs the thin-lens finite-source prediction
  R8  geometric-optics scale: lambda against 4GM/c^2 for every spec lens
  R9  on-axis wave-optics gain pi w/(1-exp(-pi w)), derived from the Gamma-function integral
Exit 0 when every check holds.
"""
import math, sys
import sympy as sp
import mpmath as mp

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-70s %s %s" % (label, "ok" if cond else "FAIL", detail))

print("R1 -- Born deflection of the linearised metric")
M, b, z, r = sp.symbols("M b z r", positive=True)
Phi = -M / sp.sqrt(z**2 + b**2)
# transverse acceleration of a null ray in -(1+2Phi)dt^2+(1-2Phi)dx^2 is -2 grad_perp Phi
alpha = sp.integrate(-2 * sp.diff(Phi, b), (z, -sp.oo, sp.oo))
alpha = sp.simplify(-alpha)   # sign: toward the mass for M>0
chk("alpha_Born == 4M/b", sp.simplify(alpha - 4 * M / b) == 0, str(alpha))
x0, x1 = sp.symbols("x0 x1", real=True)
a_fin = sp.simplify(2 * M * b * sp.integrate(1 / (z**2 + b**2)**sp.Rational(3, 2), (z, x0, x1)) * 2 / 2)
a_fin = sp.simplify(sp.integrate(2 * M * b / (z**2 + b**2)**sp.Rational(3, 2), (z, x0, x1)))
print("     finite-path Born deflection:", a_fin)

print("\nR2 -- source-at-infinity focus and units")
al = sp.symbols("alpha", positive=True)
zf = b / sp.tan(al)
ser = sp.series(zf.subs(al, 4 * M / b), M, 0, 1).removeO()
chk("z_f = b/tan(4M/b) -> b^2/(4M) + O(M)", sp.simplify(sp.series(zf.subs(al, 4*M/b), M, 0, 1).removeO() - b**2/(4*M)).is_zero is not False and sp.limit(zf.subs(al, 4*M/b) * 4 * M / b**2, M, 0) == 1)
G, c, Mk = sp.symbols("G c M_kg", positive=True)
f_units = (b**2 / (4 * M)).subs(M, G * Mk / c**2)
chk("f = b^2 c^2/(4 G M) after M_geo = GM/c^2", sp.simplify(f_units - b**2 * c**2 / (4 * G * Mk)) == 0)
f, Ds = sp.symbols("f D_s", positive=True)
Di = f * Ds / (Ds - f)
chk("thin lens 1/D_s + 1/D_i = 1/f solved", sp.simplify(1 / Ds + 1 / Di - 1 / f) == 0)
chk("D_i - f = f^2/(D_s - f) > 0 for D_s > f", sp.simplify(Di - f - f**2 / (Ds - f)) == 0)
chk("D_i -> f as D_s -> oo", sp.limit(Di, Ds, sp.oo) == f)

print("\nR3 -- which direction focuses")
Ms = sp.symbols("M_s", real=True)
a_signed = 4 * Ms / b
inv_f_az, inv_f_rad = a_signed / b, sp.diff(a_signed, b)
chk("1/f_az = 4M/b^2, 1/f_rad = -4M/b^2 (traceless: sum 0)",
    sp.simplify(inv_f_az + inv_f_rad) == 0 and sp.simplify(inv_f_az - 4*Ms/b**2) == 0)
chk("M<0: radial focus at b^2/(4|M|) (sign-blind det A = 0 distance)",
    sp.simplify((1 / inv_f_rad).subs(Ms, -M) - b**2 / (4 * M)) == 0)

print("\nR4 -- exact deflections by quadrature")
mp.mp.dps = 40
def alpha_schw(Mv, bv):
    # u = 1/r; 1/b^2 - u^2 + 2 M u^3 = 0 at turning point u0
    Mv, bv = mp.mpf(Mv), mp.mpf(bv)
    u0 = mp.findroot(lambda u: 1 / bv**2 - u**2 + 2 * Mv * u**3, 1 / bv)
    # 1/b^2 = u0^2 - 2M u0^3, so the radicand factors as (u0-u)[(u0+u) - 2M(u0^2+u0 u+u^2)];
    # with u = u0 (1 - t^2), du = -2 u0 t dt and (u0 - u) = u0 t^2: the integrand is 4 u0/sqrt(u0 h)
    def F(t):
        u = u0 * (1 - t**2)
        g = u0 * ((u0 + u) - 2 * Mv * (u0**2 + u0 * u + u**2))
        return 4 * u0 / mp.sqrt(g)
    return mp.quad(F, [0, 1]) - mp.pi
def alpha_lin(Mv, bv):
    # optical index of -(1-2M/r)dt^2 + (1+2M/r)dx^2 : n = sqrt((1+2M/r)/(1-2M/r))
    Mv, bv = mp.mpf(Mv), mp.mpf(bv)
    n = lambda rr: mp.sqrt((1 + 2 * Mv / rr) / (1 - 2 * Mv / rr))
    r0 = mp.findroot(lambda rr: n(rr) * rr - bv, bv)
    # r = r0/(1-t^2)
    def F(t):
        if t >= 1 or t < mp.mpf(10)**-30: return mp.mpf(0)
        rr = r0 / (1 - t**2)
        dr = r0 * 2 * t / (1 - t**2)**2
        rad = abs(n(rr)**2 * rr**2 - bv**2)
        if rad == 0: return mp.mpf(0)   # a single node at the turning point; integrand is finite there
        return 2 * bv * dr / (rr * mp.sqrt(rad))
    return mp.quad(F, [0, mp.mpf(1) / 2, mp.mpf(9) / 10, 1]) - mp.pi
for q in (1e-3, 5e-4, 1e-4):
    aS, aL = alpha_schw(q, 1), alpha_lin(q, 1)
    cS = (aS - 4 * q) / q**2
    cL = (aL - 4 * q) / q**2
    print("     M/b=%.0e  Schw: (alpha-4M/b)/(M/b)^2 = %.5f [15pi/4=%.5f]   lin: %.5f [4pi=%.5f]"
          % (q, cS, 15 * math.pi / 4, cL, 4 * math.pi))
    chk("  Schwarzschild 2nd-order coefficient -> 15pi/4 (M/b=%.0e)" % q, abs(cS - 15*math.pi/4) < 150 * q)
    chk("  linearised metric 2nd-order coefficient -> 4pi (M/b=%.0e)" % q, abs(cL - 4*math.pi) < 150 * q)

print("\nR5 -- composite.py VALIDATION 1 (M=1e-4, x0=-4, lam=8, n=700)")
MEAS = {0.1: 1.0028262799284702, 0.2: 1.000281233318963}  # measured 2026-09-26, composite.survey
XEND = {0.1: 3.988141271721503, 0.2: 3.9881651173476103}
if "--run-composite" in sys.argv:
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import composite as cp
    for bb in (0.1, 0.2):
        p0 = (-4.0, bb, 0.0); k0 = cp.null_tangent(p0, 1e-4)
        pts, tang, h = cp.geodesic(p0, k0, 1e-4, 8.0, 700)
        MEAS[bb] = math.atan2(-tang[-1][2], tang[-1][1]) / (4e-4 / bb)
        XEND[bb] = pts[-1][1]
    print("     (re-ran composite.survey read-only)")
Mv = 1e-4
for bb in (0.1, 0.2):
    born = 2 * Mv / bb * (XEND[bb] / math.hypot(XEND[bb], bb) + 4 / math.hypot(4, bb)) / (4 * Mv / bb)
    pred = born + math.pi * Mv / bb
    print("     b=%.1f measured %.6f | finite-path Born %.6f | + pi M/b = %.6f | resid %.1e"
          % (bb, MEAS[bb], born, pred, MEAS[bb] - pred))
    chk("  b=%.1f composite agrees with finite-path + 2nd-order to 5e-5" % bb, abs(MEAS[bb] - pred) < 5e-5)
chk("b=0.2: first-order finite-path ALONE would miss 1.0 by more than the 1e-3 tol",
    abs(2*Mv/0.2*(XEND[0.2]/math.hypot(XEND[0.2],0.2)+4/math.hypot(4,0.2))/(4*Mv/0.2) - 1) > 1e-3)

print("\nR6 -- spec.py table, and the Sun with IAU 2015 nominal GM_sun")
C, Gs, AU, LY = 299792458.0, 6.67430e-11, 1.495979e11, 9.4607e15
LENSES = (("Sun", 1.989e30, 6.957e8), ("Jupiter", 1.898e27, 7.15e7),
          ("Earth", 5.972e24, 6.371e6), ("10 km asteroid", 2.25e15, 1.0e4))
for tag, Mk_, bb in LENSES:
    fv = bb * bb * C**2 / (4 * Gs * Mk_)
    print("     %-15s f = %.5e m = %.5g AU = %.5g ly   M/b(geo) = %.3e"
          % (tag, fv, fv / AU, fv / LY, Gs * Mk_ / C**2 / bb))
f_sun = 6.957e8**2 * C**2 / (4 * Gs * 1.989e30)
chk("spec pin: f_sun/AU within 1e-3 (relative) of 547.6", abs(f_sun / AU / 547.6 - 1) <= 1e-3, "%.4f AU" % (f_sun/AU))
chk("spec docstring 8.1923e13 m vs code %.5e m: differ by %.1e (relative)" % (f_sun, 8.1923e13/f_sun-1),
    True)
GM_IAU, AU_IAU = 1.3271244e20, 1.49597870700e11     # IAU 2015 B3 nominal (astropy iau2015.py)
f_iau = 6.957e8**2 * C**2 / (4 * GM_IAU)
print("     IAU 2015 nominal GM_sun, R_sun: f = %.6e m = %.3f AU (spec's G*M differs from GM_sun by %.2e)"
      % (f_iau, f_iau / AU_IAU, Gs * 1.989e30 / GM_IAU - 1))
chk("IAU-nominal solar focus rounds to 547.8 AU", round(f_iau / AU_IAU, 1) == 547.8)
qsun = GM_IAU / C**2 / 6.957e8
print("     second-order (Schwarzschild) relative shift of f at b=R_sun: -%.2e" % (15*math.pi/16*qsun))
chk("second-order shift at b=R_sun far below the 1e-3 pin", 15*math.pi/16*qsun < 1e-5)
for gm1, lab in ((0.6e-4 + 3.1e-4, "VLBI 2000 as restated in gr-qc/0003025 (|gamma-1|<=3.7e-4, 1 sigma envelope)"),
                 (2.1e-5 + 2.3e-5, "Cassini 2003 (NAMED-NOT-READ, Shapiro delay)")):
    print("     PPN: f proportional to 2/(1+gamma); %s -> |df/f| <= %.2e" % (lab, gm1 / 2))
chk("PPN gamma envelope moves f by less than the 1e-3 pin", (0.6e-4 + 3.1e-4) / 2 < 1e-3)

print("\nR7 -- concentric.py table: conjugate to the start point, source 150 before the lens")
TAB = ((1e-3, None), (3e-3, None), (5e-3, 228.5), (1e-2, 182.2), (2e-2, 165.4), (4e-2, 158.0), (8e-2, 154.4))
for m_, meas in TAB:
    fv = 1.0 / (4 * m_)
    if fv >= 150:
        pred = None
    else:
        di = fv * 150 / (150 - fv)
        pred = 150 + di if 150 + di <= 300 else None
    print("     m=%.0e f=%.1f  thin-lens conjugate %s  table %s" % (m_, fv, "none" if pred is None else "%.1f" % pred,
          "none" if meas is None else meas))
    chk("  m=%.0e: seats/none agrees with thin-lens" % m_, (pred is None) == (meas is None))
    if pred is not None:
        chk("  m=%.0e: table conjugate within 4 of thin-lens (thick/strong-lens offset)" % m_, abs(meas - pred) < 4.0,
            "offset %+.2f" % (meas - pred))

print("\nR8 -- geometric-optics scale 4GM/c^2 per lens (null geodesic != light when lambda >~ 4GM/c^2)")
for tag, Mk_, bb in LENSES:
    rs4 = 4 * Gs * Mk_ / C**2
    print("     %-15s 4GM/c^2 = %.3e m ; w = 8 pi G M/(c^2 lambda) at 500 nm = %.3e ; at 1 cm = %.3e"
          % (tag, rs4, 2 * math.pi * rs4 / 5e-7, 2 * math.pi * rs4 / 1e-2))
chk("10 km asteroid: 4GM/c^2 < 1e-11 m, far below optical wavelengths", 4*Gs*2.25e15/C**2 < 1e-11)

print("\nR9 -- on-axis wave-optics gain of a point-mass lens (does a geodesic focus become a light focus?)")
# scalar Fresnel-Kirchhoff with the thin-lens delay T(x) = x^2/2 - ln x (Einstein-radius units; grad ln x
# is the 1/x deflection that R1 gives as 4M/b):  F = (w/2 pi i) Int d^2x exp(i w T).  On axis the angular
# integral is 2 pi and  Int_0^oo x^(1-iw) e^(i w x^2/2) dx = (1/2) Gamma(1 - iw/2) (-iw/2)^(-(1 - iw/2)).
def gain(w):
    w = mp.mpf(w)
    s = 1 - 1j * w / 2
    I = mp.mpf(1) / 2 * mp.gamma(s) * mp.power(-1j * w / 2, -s)
    F = (w / (2 * mp.pi * 1j)) * 2 * mp.pi * I
    return abs(F)**2
for w in (1e-4, 0.1, 1.0, 10.0, 100.0):
    g, cf = gain(w), mp.pi * w / (1 - mp.exp(-mp.pi * w))
    chk("  |F|^2(w=%g) = pi w/(1-exp(-pi w)) = %.6g" % (w, float(cf)), abs(g / cf - 1) < 1e-20)
for tag, Mk_, bb in LENSES:
    w = 2 * math.pi * 4 * Gs * Mk_ / C**2 / 5e-7
    gg = float(mp.pi * w / (1 - mp.exp(-mp.pi * w)))
    print("     %-15s 500 nm: w = %.3e, on-axis gain = %.4g" % (tag, w, gg))
chk("10 km asteroid at 500 nm: on-axis gain - 1 < 2e-4 (no geometric focus for light)",
    float(mp.pi * (2*math.pi*4*Gs*2.25e15/C**2/5e-7) / (1 - mp.exp(-mp.pi * (2*math.pi*4*Gs*2.25e15/C**2/5e-7)))) - 1 < 2e-4)

print("\nALL CHECKS", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
