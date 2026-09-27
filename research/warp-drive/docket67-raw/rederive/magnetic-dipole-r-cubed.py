#!/usr/bin/env python3
"""DOCKET 67 -- magnetic-dipole-r-cubed.  Re-derivation and sensitivity.

(A) sympy: the point-dipole field B = curl(mu0/4pi m x r / r^3) is
    mu0/4pi (3 (m.rhat) rhat - m)/r^3, divergence-free and curl-free for r != 0,
    and exactly homogeneous of degree -3 (B(lam r) = lam^-3 B(r)); so at FIXED
    angle B(r) = B(R) (R/r)^3 exactly -- the form spec.py:225-227 uses.
    Pole/equator ratio = 2.  An l-pole scalar potential gives B ~ r^-(l+2).
(B) numeric: reproduce spec.py:51-53 / 268-276 with spec.py's own constants.
(C) sensitivity: every datum and every dropped hypothesis, one at a time:
    B_s over the McGill catalog (1309.4167 Table 2), R = 1.0e4 vs 1.2e4 m,
    pole vs equator, falloff exponent 3 -> 2 (twisted / split monopole),
    light cylinder R_L = cP/2pi for every catalogued P, with B ~ 1/r beyond it.
(D) the conclusion 'does not seat' as a BOUND: for any field with
    B(r) <= B_s (R/r)^2 outside the star, B(l) l <= B_s R^2 / l <= B_s R,
    against the seating invariant sqrt(2 mu0 pi c^4/(4G)) = 1.5456e19 T m.
Exit 0 if every check agrees with the recorded numbers.
"""
import math
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))

print("(A) symbolic")
x, y, z, lam = sp.symbols('x y z lam', real=True)
lamp = sp.symbols('lamp', positive=True)
mx, my, mz, k = sp.symbols('m_x m_y m_z k', real=True)
r = sp.sqrt(x**2 + y**2 + z**2)
m = sp.Matrix([mx, my, mz]); R3 = sp.Matrix([x, y, z])
A = k * m.cross(R3) / r**3
def curl(F):
    return sp.Matrix([sp.diff(F[2], y) - sp.diff(F[1], z),
                      sp.diff(F[0], z) - sp.diff(F[2], x),
                      sp.diff(F[1], x) - sp.diff(F[0], y)])
B = curl(A)
Bform = k * (3 * (m.dot(R3)) * R3 / r**5 - m / r**3)
chk("curl A == k (3(m.r)r/r^5 - m/r^3)", all(sp.simplify(B[i] - Bform[i]) == 0 for i in range(3)))
divB = sp.simplify(sum(sp.diff(B[i], v) for i, v in enumerate((x, y, z))))
chk("div B == 0 for r != 0", divB == 0)
chk("curl B == 0 for r != 0 (vacuum, no currents)", all(sp.simplify(c) == 0 for c in curl(B)))
Bs = B.subs({x: lamp * x, y: lamp * y, z: lamp * z}, simultaneous=True)
chk("B(lam r) == lam^-3 B(r) exactly (homogeneous, degree -3)",
    all(sp.simplify(Bs[i] - B[i] / lamp**3) == 0 for i in range(3)))
Bz = sp.Matrix(Bform.subs({mx: 0, my: 0}))
pole = sp.simplify(Bz.subs({x: 0, y: 0, z: 1}).norm())
eq = sp.simplify(Bz.subs({x: 1, y: 0, z: 0}).norm())
chk("|B_pole| / |B_equator| == 2 at equal r", sp.simplify(pole / eq) == 2)
# l-pole: scalar potential r^-(l+1) P_l -> |B| ~ r^-(l+2)
rr, th = sp.symbols('r theta', positive=True)
for l in range(1, 5):
    Phi = sp.legendre(l, sp.cos(th)) / rr**(l + 1)
    Br = -sp.diff(Phi, rr)
    chk("l=%d pole: B_r ~ r^-%d" % (l, l + 2), sp.simplify(Br * rr**(l + 2)).has(rr) is False)

print("\n(B) spec.py's numbers, spec.py's constants")
MU0 = 1.25663706212e-6; G = 6.67430e-11; C = 299792458.0
T_COEFF = math.pi * C**4 / (4 * G)
def treq(l): return T_COEFF / l**2
INV = math.sqrt(2 * MU0 * T_COEFF)
print("  seating invariant B*l = %.5e T m" % INV)
chk("invariant == 1.5456e19 T m (spec.py:36)", abs(INV / 1.5456e19 - 1) < 1e-4)
Bs0, R0, r0 = 1.0e11, 1.0e4, 1.5456e8
Bfar = Bs0 * (R0 / r0)**3; u = Bfar**2 / (2 * MU0)
print("  B(1.5456e8 m) = %.4e T ; u = %.4e Pa ; required %.4e Pa ; short by 10^%.2f"
      % (Bfar, u, treq(r0), math.log10(treq(r0) / u)))
chk("B = 2.7e-2 T (spec.py:52)", abs(Bfar / 2.7e-2 - 1) < 0.01)
chk("u = 2.9e2 Pa (spec.py:52)", abs(u / 2.9e2 - 1) < 0.01)
chk("required = 4.0e27 Pa (spec.py:52)", abs(treq(r0) / 4.0e27 - 1) < 0.01)
chk("short by twenty-five orders (floor of log10 == 25)", int(math.log10(treq(r0) / u)) == 25)

print("\n(C) sensitivity -- orders short = log10(required/u) at r = 1.5456e8 m")
def short(B): return math.log10(treq(r0) / (B**2 / (2 * MU0)))
rows = []
def row(tag, B):
    s = short(B); rows.append((tag, B, s))
    print("  %-62s B=%10.3e T  short 10^%6.2f  >20:%s seats:%s" % (tag, B, s, s > 20, s <= 0))
row("tree: B_s=1e11 T, R=1e4 m, n=3", Bs0 * (R0 / r0)**3)
row("catalog max SGR 1806-20 B=2.0e15 G=2.0e11 T (1309.4167 T2)", 2.0e11 * (R0 / r0)**3)
row("catalog min SGR 0418+5729 B=6.1e12 G=6.1e8 T", 6.1e8 * (R0 / r0)**3)
row("pole field = 2 x equatorial spin-down B (2x1e11)", 2e11 * (R0 / r0)**3)
row("R = 1.2e4 m, B_s = 2e11 (pole, max)", 2e11 * (1.2e4 / r0)**3)
for p in (1.0, 0.5, 0.2, 0.0):
    row("twisted self-similar n = 2+p, p=%.1f (B_s=2e11, R=1.2e4)" % p, 2e11 * (1.2e4 / r0)**(2 + p))
# light cylinder, catalog periods (1309.4167 Table 2)
CAT = [("CXOU J0100", 8.020392, 3.9), ("4U 0142+61", 8.68832877, 1.3), ("SGR 0418", 9.07838822, 0.061),
       ("SGR 0501", 5.76209653, 1.9), ("SGR 0526-66", 8.0544, 5.6), ("1E 1048", 6.4578754, 3.9),
       ("1E 1547.0-5408", 2.0721255, 3.2), ("PSR J1622", 4.3261, 2.7), ("SGR 1627-41", 2.594578, 2.2),
       ("CXOU J1647", 10.610644, 0.66), ("1RXS J1708", 11.003027, 4.6), ("CXOU J1714", 3.825352, 5.0),
       ("SGR J1745-2900", 3.7635537, 1.6), ("SGR 1806-20", 7.547728, 20.0), ("XTE J1810", 5.5403537, 2.1),
       ("Swift J1822", 8.43771958, 0.51), ("SGR 1833", 7.5654084, 1.6), ("Swift J1834.9", 2.4823018, 1.4),
       ("1E 1841", 11.782898, 6.9), ("SGR 1900+14", 5.19987, 7.0), ("1E 2259", 6.978948446, 0.59)]
print("\n  light cylinder R_L = cP/2pi against r = 1.5456e8 m (P_crit = %.3f s)" % (2 * math.pi * r0 / C))
outside = []
for name, P, B14 in CAT:
    RL = C * P / (2 * math.pi)
    Bs = B14 * 1e10  # 1e14 G = 1e10 T
    if r0 < RL:
        Bd = Bs * (R0 / r0)**3; zone = "inside R_L (x=%.2f)" % (r0 / RL)
    else:
        Bd = Bs * (R0 / RL)**3 * (RL / r0); zone = "OUTSIDE R_L (x=%.2f)" % (r0 / RL)
        outside.append(name)
    print("   %-16s P=%7.3f s R_L=%.3e m %-22s B=%.3e T short 10^%.2f" % (name, P, RL, zone, Bd, short(Bd)))
chk("catalogued magnetars with r = 1.5456e8 m outside the light cylinder: 1E 1547.0-5408, SGR 1627-41, Swift J1834.9",
    sorted(outside) == sorted(["1E 1547.0-5408", "SGR 1627-41", "Swift J1834.9"]))
# worst case: split monopole from the surface + toroidal beyond R_L, fastest catalogued P, max B, pole, R=1.2e4
P = 2.0721255; RL = C * P / (2 * math.pi)
Bmono = 2e11 * (1.2e4 / r0)**2
Bphi = Bmono * (r0 / RL)
row("bound: split monopole n=2 + toroidal (r/R_L) beyond R_L, P=2.07 s", math.hypot(Bmono, Bphi))
# Swift J1818.0-1607 (P = 1.36 s, 2020; NOT read here) -- illustrative only
P = 1.36; RL = C * P / (2 * math.pi)
row("illustrative (not read): P=1.36 s split monopole + toroidal, B_s=2e11", math.hypot(Bmono, Bmono * r0 / RL))
chk("EVERY row: does not seat (u < required)", all(s > 0 for _, _, s in rows))
chk("NOT every row: short by > 20 orders (selftest threshold is dipole-specific)",
    not all(s > 20 for _, _, s in rows))
print("  minimum shortfall over all rows: 10^%.2f" % min(s for _, _, s in rows))

print("\n(D) the conclusion as a bound independent of the falloff law")
# the invariant cannot be met for l >= R by any B(r) <= B_s (R/r)^2: B(l) l <= B_s R^2/l <= B_s R
Bs_, R_, l_ = sp.symbols('B_s R l', positive=True)
chk("B_s (R/l)^2 * l <= B_s R for l >= R (sympy)",
    sp.simplify((Bs_ * R_ - Bs_ * (R_ / l_)**2 * l_).subs(l_, R_ * (1 + sp.Symbol('e', nonnegative=True)))).is_nonnegative)

for Bs, R in ((1e11, 1e4), (2e11, 1.2e4), (1e12, 1.2e4)):
    print("  B_s R = %.3e T m  vs  invariant %.4e  (ratio 10^%.2f)" % (Bs * R, INV, math.log10(INV / (Bs * R))))
chk("2 B_s R < invariant by > 2.8 orders even for the 1e12 T interior estimate (spec.py:145), R=1.2e4",
    math.log10(INV / (2 * 1e12 * 1.2e4)) > 2.8)
# toroidal zone beyond R_L: |B| r <= B_s R^2 (1/r + 1/R_L) <= 2 B_s R for r >= R_L >= R
RLs = sp.Symbol('R_L', positive=True)
expr = 2 * Bs_ * R_ - Bs_ * R_**2 * (1 / l_ + 1 / RLs)
chk("toroidal zone: B_s R^2 (1/l + 1/R_L) <= 2 B_s R for l, R_L >= R (sympy)",
    sp.simplify(expr.subs({l_: R_ * (1 + sp.Symbol('e', nonnegative=True)),
                           RLs: R_ * (1 + sp.Symbol('f', nonnegative=True))})).is_nonnegative)
print("\nALL OK" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
