#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'schwarzschild-radius-collapse-criterion'.

The tree (spec.py:39-48, 214-222; specthm.py:611-614, 1334-1350) uses:
  H_ball     uniform energy density u over a BALL of radius l, M = u (4/3) pi l^3 / c^2
  H_collapse 'a region is a black hole iff 2GM/c^2 >= l'
  => u_collapse = 3 c^4 / (8 pi G l^2), u_seat = pi c^4/(4 G l^2), ratio 2 pi^2/3.

Checks (sympy + z3 + numeric).  Exit 0 iff every check comes out as recorded.
  R1  Sturm threshold and the ratio 2 pi^2/3, exact; G and c cancel.
  R2  Schwarzschild 1916 interior (physics/9912033 eqs 29,30,35,40,43): Einstein
      equations hold; Misner-Sharp mass at the surface = (4 pi/3) rho0 P_o^3, so the
      tree's M formula is EXACT with l = areal radius ('radius measured outside');
      alpha/P_o = sin^2 chi_a; central pressure infinite at cos chi_a = 1/3 <=> 2m/R = 8/9.
  R3  the source's own numerics (alpha_sun ~ 3 km; 1 g -> 1.5e-28 cm; ~500 R_sun; v ~ c/500).
  R4  trapped-sphere identity (Hayward Prop.1 / Misner-Sharp): Gamma^2 - U^2 = 1 - 2m/R,
      z3: 2m/R > 1 => U^2 >= 2m/R - 1 > 0 (no static configuration); at 2 pi^2/3, |U| >= 2.36 c.
  R5  the 'iff' of H_collapse fails both ways (closed-FRW dust = Oppenheimer-Snyder interior):
      (a) a sphere inside the event horizon with 2m/R < 1; (b) the time reverse: a
      past-trapped (expanding) sphere with 2m/R > 1 that lies in no black hole.
  R6  robustness of the tree's CONCLUSION (ratio > threshold) over the choices the tree
      fixes by definition: ball radius l vs l/2 (smallest ball holding a chord of length l),
      T_kk/u in {1, 4/3, 2}, threshold 1 (trapped) or 8/9 (Buchdahl, static isotropic).
  R7  the tree's own function values (spec.seat_over_collapse at 1, 1e5, 1e8, 1e11 m).
"""
import math
import os
import sys

import sympy as sp
import z3

sys.dont_write_bytecode = True
FAIL = []


def rec(tag, ok, msg):
    print("  [%s] %-5s %s" % ("ok" if ok else "FAIL", tag, msg))
    if not ok:
        FAIL.append(tag)


# ------------------------------------------------------------------ R1
print("R1  Sturm threshold and the ratio")
G, c, l, u, lam, T = sp.symbols("G c l u lambda T", positive=True)
# null Raychaudhuri, 2 transverse dims, shear-free: x = sqrt(area), x'' = -(R_kk/2) x,
# R_kk = 8 pi G T_kk / c^4.  First conjugate point at lambda = pi/omega.
omega = sp.sqrt(4 * sp.pi * G * T / c**4)
Tseat = sp.solve(sp.Eq(sp.pi / omega, l), T)[0]
rec("R1a", sp.simplify(Tseat - sp.pi * c**4 / (4 * G * l**2)) == 0,
    "Sturm/Raychaudhuri: T_kk >= %s  (seatindex.T_COEFF/l^2)" % Tseat)
M = u * sp.Rational(4, 3) * sp.pi * l**3 / c**2
ucol = sp.solve(sp.Eq(2 * G * M / c**2, l), u)[0]
rec("R1b", sp.simplify(ucol - 3 * c**4 / (8 * sp.pi * G * l**2)) == 0,
    "2GM/c^2 = l with M = u(4/3)pi l^3/c^2  <=>  u = %s  (spec.collapse_bound)" % ucol)
ratio = sp.simplify(Tseat / ucol)
rec("R1c", sp.simplify(ratio - 2 * sp.pi**2 / 3) == 0 and not ratio.free_symbols,
    "u_seat/u_collapse = %s = %.10f, free symbols %s (G, c, l cancel)"
    % (ratio, float(ratio), ratio.free_symbols or "none"))

# ------------------------------------------------------------------ R2
print("R2  Schwarzschild 1916 interior, uniform incompressible ball (G = c = 1, kappa = 8 pi)")
chi, chia, rho0, th, ph, t = sp.symbols("chi chi_a rho0 theta phi t", positive=True)
kap = 8 * sp.pi
a = sp.sqrt(3 / (kap * rho0))                        # curvature radius sqrt(3/kappa rho0)
f4 = ((3 * sp.cos(chia) - sp.cos(chi)) / 2) ** 2     # eq (29)
p = rho0 * 2 * sp.cos(chia) / (3 * sp.cos(chia) - sp.cos(chi)) - rho0  # eq (30)
X = [t, chi, th, ph]
g = sp.diag(-f4, a**2, a**2 * sp.sin(chi) ** 2, a**2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)  # eq (35), -+++
gi = g.inv()
Gam = [[[sum(gi[i, s] * (sp.diff(g[s, j], X[k]) + sp.diff(g[s, k], X[j]) - sp.diff(g[j, k], X[s]))
             for s in range(4)) / 2 for k in range(4)] for j in range(4)] for i in range(4)]
Ric = sp.zeros(4)
for j in range(4):
    for k in range(4):
        Ric[j, k] = sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                                    + sum(Gam[i][i][s] * Gam[s][j][k] - Gam[i][k][s] * Gam[s][j][i]
                                          for s in range(4)) for i in range(4)))
Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
Ein = sp.simplify(Ric - Rs * g / 2)
uvec = sp.Matrix([1 / sp.sqrt(f4), 0, 0, 0])
ul = g * uvec
Tmn = sp.Matrix(4, 4, lambda i, j: (rho0 + p) * ul[i] * ul[j] + p * g[i, j])
res = sp.simplify(Ein - kap * Tmn)
rec("R2a", all(sp.simplify(e) == 0 for e in res),
    "eq.(35) with p from eq.(30) solves G_mn = 8 pi T_mn (perfect fluid rho0, p) exactly")
rec("R2b", sp.simplify(p.subs(chi, chia)) == 0, "p = 0 at the surface chi = chi_a")
Rareal = a * sp.sin(chi)
# Misner-Sharp: m = (R/2)(1 - g^{ab} dR dR); only chi-derivative on the static slice
mMS = sp.simplify(Rareal / 2 * (1 - gi[1, 1] * sp.diff(Rareal, chi) ** 2))
rec("R2c", sp.simplify(mMS - sp.Rational(4, 3) * sp.pi * rho0 * Rareal**3) == 0,
    "Misner-Sharp m(chi) = (4 pi/3) rho0 R^3 with R = areal radius  ==> tree's M = u(4/3)pi l^3/c^2 is EXACT for l = areal radius")
Po = a * sp.sin(chia)
alpha = 2 * mMS.subs(chi, chia)
rec("R2d", sp.simplify(alpha - kap * rho0 / 3 * Po**3) == 0 and sp.simplify(alpha / Po - sp.sin(chia) ** 2) == 0,
    "eq.(40): alpha = (kappa rho0/3) P_o^3 and alpha/P_o = sin^2 chi_a (source, READ)")
pc = sp.simplify(p.subs(chi, 0))
cstar = sp.solve(sp.Eq(3 * sp.cos(chia) - 1, 0), sp.cos(chia))[0]
rec("R2e", cstar == sp.Rational(1, 3) and sp.simplify(1 - cstar**2) == sp.Rational(8, 9),
    "central pressure %s diverges at cos chi_a = %s  <=>  2m/R = sin^2 chi_a = %s  (source: 'limit 9/8 alpha')"
    % (pc, cstar, 1 - cstar**2))
# proper-volume mass vs gravitational mass, eq (43)
Mprop = rho0 * 4 * sp.pi * a**3 * sp.integrate(sp.sin(chi) ** 2, (chi, 0, chia))
r43 = sp.simplify((alpha / 2) / Mprop)
want43 = sp.Rational(2, 3) * sp.sin(chia) ** 3 / (chia - sp.sin(2 * chia) / 2)
rec("R2f", sp.simplify(r43 - want43) == 0,
    "eq.(43): gravitational/substantial mass = (2/3) sin^3 chi_a/(chi_a - sin 2chi_a/2); at chi_a=acos(1/3): %.4f"
    % float(want43.subs(chia, sp.acos(sp.Rational(1, 3)))))
# proper radius vs areal radius at the Buchdahl limit
ca = math.acos(1 / 3)
rec("R2g", ca / math.sin(ca) > 1.3,
    "at the 8/9 limit proper radius / areal radius = chi_a/sin chi_a = %.4f (l as proper length != l as areal radius)"
    % (ca / math.sin(ca)))

# ------------------------------------------------------------------ R3
print("R3  the 1916 interior paper's own numerics (IAU 2015 nominal GM_sun, R_sun; CODATA G, c)")
GMs, Rs_, Gsi, csi = 1.3271244e20, 6.957e8, 6.67430e-11, 299792458.0
al_sun = 2 * GMs / csi**2
al_g = 2 * Gsi * 1e-3 / csi**2 * 100.0
rho_sun = (GMs / Gsi) / (4 / 3 * math.pi * Rs_**3)
curv = math.sqrt(3 * csi**2 / (8 * math.pi * Gsi * rho_sun))
vfall = math.sqrt(al_sun / Rs_)
rec("R3a", abs(al_sun / 3.0e3 - 1) < 0.02, "alpha_sun = %.1f m  vs source 'equal to 3 km'" % al_sun)
rec("R3b", abs(al_g / 1.5e-28 - 1) < 0.02, "alpha(1 g) = %.4g cm vs source '1.5 . 10^-28 cm'" % al_g)
rec("R3c", 400 < curv / Rs_ < 600, "interior curvature radius = %.0f R_sun vs source 'about 500 times'" % (curv / Rs_))
rec("R3d", 400 < 1 / vfall < 600, "surface fall velocity = c/%.0f vs source 'about 1/500'" % (1 / vfall))
rec("R3e", al_sun / Rs_ < 1e-5, "Sun: 2GM/(c^2 R) = %.3e << 1 (tree SR2: 'the Sun is not inside its Schwarzschild radius')" % (al_sun / Rs_))

# ------------------------------------------------------------------ R4
print("R4  trapped-sphere identity and 'no static configuration inside r_s'")
Gm_, U_, q_ = z3.Reals("Gamma U q")
hyp = z3.And(Gm_ * Gm_ - U_ * U_ == 1 - q_, q_ > 1)
s = z3.Solver()
s.add(hyp, z3.Not(z3.And(U_ * U_ >= q_ - 1, U_ != 0)))
r4 = s.check()
v = z3.Solver()
v.add(hyp)
rec("R4a", r4 == z3.unsat and v.check() == z3.sat,
    "z3: [Gamma^2 - U^2 = 1 - 2m/R, 2m/R > 1] => U^2 >= 2m/R - 1 and U != 0  (%s; vacuity guard %s)"
    % (r4, v.check()))
q = 2 * math.pi**2 / 3
rec("R4b", math.sqrt(q - 1) > 2.3,
    "at 2m/R = 2 pi^2/3 the areal radius must change at |dR/dtau| >= sqrt(2m/R - 1) c = %.4f c: "
    "the configuration is collapsing (black hole) or expanding (white hole), never static" % math.sqrt(q - 1))
# the identity itself on a general spherical metric: comoving -e^{2Phi}dt^2 + e^{2L}dr^2 + R(t,r)^2 dOmega^2
tt, rr = sp.symbols("t r")
Phi, L, R = [sp.Function(n)(tt, rr) for n in ("Phi", "Lam", "R")]
grad2 = -sp.exp(-2 * Phi) * sp.diff(R, tt) ** 2 + sp.exp(-2 * L) * sp.diff(R, rr) ** 2
Uc = sp.exp(-Phi) * sp.diff(R, tt)
Gc = sp.exp(-L) * sp.diff(R, rr)
rec("R4c", sp.simplify(grad2 - (Gc**2 - Uc**2)) == 0,
    "g^{ab} dR dR = Gamma^2 - U^2 for any comoving spherical metric, so 1 - 2m/R = Gamma^2 - U^2")

# ------------------------------------------------------------------ R5
print("R5  the 'iff' of H_collapse, closed-FRW dust (Oppenheimer-Snyder interior)")
eta, am = sp.symbols("eta a_m", positive=True)
aa = am / 2 * (1 + sp.cos(eta))
tau = am / 2 * (eta + sp.sin(eta))
adot = sp.simplify(sp.diff(aa, eta) / sp.diff(tau, eta))
rho = 3 * am / (8 * sp.pi * aa**3)                   # Friedmann: adot^2 + 1 = (8 pi/3) rho a^2 = a_m/a
rec("R5a", sp.simplify(adot**2 + 1 - sp.Rational(8, 3) * sp.pi * rho * aa**2) == 0,
    "cycloid a(eta), tau(eta) solves closed Friedmann dust: adot = %s" % adot)
# on each comoving sphere: R = a sin chi, U = adot sin chi, Gamma = cos chi
q_frw = sp.simplify(1 - (sp.cos(chi) ** 2 - (adot * sp.sin(chi)) ** 2))
rec("R5b", sp.simplify(q_frw - sp.sin(chi) ** 2 / sp.cos(eta / 2) ** 2) == 0,
    "2m/R = sin^2 chi sec^2(eta/2); at max expansion (eta = 0) 2m/R = sin^2 chi <= 1")
chi0 = 0.3                                            # ball edge, any 0 < chi0 < pi/2
eta_AH = math.pi - 2 * chi0                           # surface reaches 2m = R
eta_c = eta_AH - chi0                                 # outgoing radial null ray chi = eta - eta_c reaches chi0 at eta_AH
e1 = eta_c + 0.05
chi1 = 0.02                                           # a sphere inside the EH at e1 (EH at chi = e1 - eta_c = 0.05)
q1 = math.sin(chi1) ** 2 / math.cos(e1 / 2) ** 2
rec("R5c", chi1 < e1 - eta_c and q1 < 1,
    "(a) sphere chi = %.2f at eta = %.4f lies INSIDE the event horizon (EH at chi = %.2f) yet 2m/R = %.4f < 1"
    % (chi1, e1, e1 - eta_c, q1))
e2 = -(eta_AH + 0.2)                                  # time reverse: expanding branch
q2 = math.sin(chi0) ** 2 / math.cos(e2 / 2) ** 2
U2 = float(adot.subs({eta: e2})) * math.sin(chi0)
rec("R5d", q2 > 1 and U2 > 0,
    "(b) time reverse at eta = %.3f: surface has 2m/R = %.3f > 1 while EXPANDING (dR/dtau = +%.3f): past-trapped, a white hole, not a black hole"
    % (e2, q2, U2))

# ------------------------------------------------------------------ R6
print("R6  robustness of the tree's conclusion over the choices it fixes by definition")
rows = []
for geo, gf in (("ball radius l (tree H_ball)", 1.0), ("ball radius l/2 (smallest ball holding the chord)", 0.25)):
    for mat, tk in (("T_kk = u (dust / tree's identification)", 1.0), ("T_kk = 4u/3 (radiation fluid)", 4 / 3),
                    ("T_kk = 2u (magnetic, ray perp. B; stiff fluid)", 2.0)):
        qq = (2 * math.pi**2 / 3) * gf / tk
        rows.append((geo, mat, qq, qq > 1.0, qq > 8 / 9))
        print("      %-48s %-46s 2m/R = %.4f  trapped:%s  >Buchdahl 8/9:%s" % (geo, mat, qq, qq > 1, qq > 8 / 9))
rec("R6a", rows[0][2] == 2 * math.pi**2 / 3 and all(r[3] for r in rows[:3]),
    "on the tree's own H_ball (radius l) every material row is trapped (min %.4f)" % min(r[2] for r in rows[:3]))
rec("R6b", (not rows[5][3]) and (not rows[5][4]) and abs(rows[5][2] - math.pi**2 / 12) < 1e-12,
    "radius l/2 with T_kk = 2u gives 2m/R = pi^2/12 = %.4f < 8/9 < 1: NOT trapped -- 'ANY region' needs H_ball as stated" % rows[5][2])
# EM check: pure B along z, T_kk for k along x and along z (k^0 = 1)
B, mu0 = sp.symbols("B mu0", positive=True)
uB = B**2 / (2 * mu0)
Tem = sp.diag(uB, uB, uB, -uB)                        # T_00, T_xx, T_yy, T_zz for B = B zhat
kx = sp.Matrix([1, 1, 0, 0]); kz = sp.Matrix([1, 0, 0, 1])
Tkx = sp.simplify((kx.T * Tem * kx)[0]); Tkz = sp.simplify((kz.T * Tem * kz)[0])
rec("R6c", sp.simplify(Tkx - 2 * uB) == 0 and Tkz == 0,
    "EM: T_kk = %s = 2u for a ray perp. B, %s for a ray along B (spec.py:156 sets u_B = B^2/2mu0 = T_kk threshold)" % (Tkx, Tkz))
rec("R6d", 2 * math.pi**2 / 3 * 9 / 8 > 7.4,
    "with Buchdahl's static bound instead of the trapped bound (tree's H_ball): ratio = 3 pi^2/4 = %.4f" % (3 * math.pi**2 / 4))

# ------------------------------------------------------------------ R7
print("R7  the tree's own values (read-only import, bytecode off)")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import spec  # noqa: E402
    vals = [spec.seat_over_collapse(x) for x in (1.0, 1e5, 1e8, 1e11)]
    rec("R7a", all(abs(v_ / (2 * math.pi**2 / 3) - 1) < 1e-12 for v_ in vals),
        "spec.seat_over_collapse = %s" % ", ".join("%.12g" % v_ for v_ in vals))
    rec("R7b", abs(spec.collapse_bound(1.0) / (3 * csi**4 / (8 * math.pi * Gsi)) - 1) < 1e-12 and spec.G_SI == Gsi,
        "spec.collapse_bound(1 m) = %.6e Pa; spec.G_SI = %g (CODATA 2018 = 2022 value)" % (spec.collapse_bound(1.0), spec.G_SI))
except Exception as exc:  # pragma: no cover
    rec("R7", False, "import failed: %r" % exc)

print("\n%s" % ("ALL AS RECORDED" if not FAIL else "FAILED: %s" % FAIL))
sys.exit(1 if FAIL else 0)
