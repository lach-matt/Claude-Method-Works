#!/usr/bin/env python3
"""D67 re-derivation: static linear Higgs response to a fermion scalar density.

Owner under audit: research/warp-drive/address.py:136-147, 163-186, 297-303,
663-683, 692-721.  READ-ONLY import of address.py (no bytecode written).

Parts
  R1  Lagrangian -> static EOM, sign, uniform solution; equals Brax-Burrage
      2101.10693 eq.(10) linearised and Shi 1908.02159 p.1 shift.
  R2  v^2 m_h^2 = 8|V_min| (SM quartic) ; linear response depends on m_h^2 only;
      the 8|V_min| rewrite and the O(eps^3) field energy depend on the
      (unmeasured) self-coupling shape kappa.
  R3  Yukawa exterior solution; uniform sphere: surface value -> eps_in/2.
  R4  scalar/vector density of a free Fermi gas at n0 (psibar psi ~ n).
  R5  numbers: EPS_NUCLEAR and ratios over eps_det under moved inputs
      (f_N, S incl. strange, beyond-LO heavy sum, n0, m_h); electrons.
  R6  Shi 2107.04206 nonperturbative-phase critical mass vs the tree's uses.
  R7  ultralocal limit: multiplicative vs absolute error (1D example).
Exit 0 iff every check passes.
"""
import math
import sys

sys.dont_write_bytecode = True
import sympy as sp

FAIL = []


def chk(name, ok, extra=""):
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + extra) if extra else ""))
    if not ok:
        FAIL.append(name)


# ----------------------------------------------------------------- R1
print("== R1 field equation and uniform solution")
x, y, z, t = sp.symbols("x y z t", real=True)
v, mh, lam, m, n, rho = sp.symbols("v m_h lambda m n rho", positive=True)
h = sp.Function("h")(t, x, y, z)
# SM-shape potential for the real radial mode (mostly-minus metric):
V = lam / 4 * (h ** 2 - v ** 2) ** 2
L = sp.Rational(1, 2) * (sp.diff(h, t) ** 2 - sp.diff(h, x) ** 2 - sp.diff(h, y) ** 2
                         - sp.diff(h, z) ** 2) - V - (m / v) * h * n
EL = sp.euler_equations(L, [h], [t, x, y, z])[0].lhs
# linearise about v: h = v + d
d = sp.Function("d")(x, y, z)
lin = EL.subs(h, v + d).doit()
lin = sp.series(lin.subs(d, sp.Symbol("e") * d), sp.Symbol("e"), 0, 2).removeO().subs(sp.Symbol("e"), 1)
lin = sp.expand(lin.doit())
mh2 = sp.diff(V.subs(h, sp.Symbol("H")), sp.Symbol("H"), 2).subs(sp.Symbol("H"), v)  # = 2 lam v^2
target = sp.diff(d, x, 2) + sp.diff(d, y, 2) + sp.diff(d, z, 2) - mh2 * d - (m / v) * n
# EL = -(box d) - V'(h) - (m/v) n ; static: box d = -lap d
chk("static linearised EOM is (lap - m_h^2) d = (m/v) n  [address.py:138]",
    sp.simplify(lin - target) == 0, "residual %s" % sp.simplify(lin - target))
chk("m_h^2 = V''(v) = 2 lambda v^2", sp.simplify(mh2 - 2 * lam * v ** 2) == 0)
d0 = sp.solve(sp.Eq(-mh2 * sp.Symbol("D") - (m / v) * n, 0), sp.Symbol("D"))[0]
eps = sp.simplify(d0 / v)
chk("uniform eps = -m n/(v^2 m_h^2) = -rho/(v^2 m_h^2)  (rho = m n, nonrelativistic)",
    sp.simplify(eps + m * n / (v ** 2 * mh2)) == 0, str(eps))
# Brax-Burrage 2101.10693 eq (10), mostly-plus: box h + mu^2 h - lam h^3 - rho/v = 0,
# box = -d_t^2 + lap ; mu^2 = lam v^2 (eq 7).  Static linearised:
D = sp.Symbol("D")
bb = (sp.Symbol("LAP") + lam * v ** 2 * (v + D) - lam * (v + D) ** 3 - rho / v)
bb_lin = sp.expand(sp.series(bb, D, 0, 2).removeO())
chk("Brax-Burrage eq(10) linearised == (lap - 2 lam v^2) D - rho/v  (same as tree)",
    sp.simplify(bb_lin - (sp.Symbol("LAP") - 2 * lam * v ** 2 * D - rho / v)) == 0)
# Shi 1908.02159 p.1: L = u^2 phi^2/4 - lam phi^4/4! - f phi psibar psi ; v = u sqrt(3/lam);
# shift <phi> = v - f n/u^2.
u, f, lS = sp.symbols("u f lambda_S", positive=True)
P = sp.Symbol("P")
VS = -u ** 2 * P ** 2 / 4 + lS * P ** 4 / 24
vS = u * sp.sqrt(3 / lS)
chk("Shi: V'(v)=0 at v = u sqrt(3/lam)", sp.simplify(sp.diff(VS, P).subs(P, vS)) == 0)
chk("Shi: u is the physical mass, V''(v) = u^2", sp.simplify(sp.diff(VS, P, 2).subs(P, vS) - u ** 2) == 0)
shift = sp.solve(sp.diff(VS, P, 2).subs(P, vS) * D + f * n, D)[0]
chk("Shi: linear shift -f n/u^2 ; eps = -(f v n)/(v^2 u^2) = tree form",
    sp.simplify(shift + f * n / u ** 2) == 0)

# ----------------------------------------------------------------- R2
print("== R2 8|V_min| identity, and what depends on the unmeasured shape")
Hs = sp.Symbol("H")
Vsm = lam / 4 * (Hs ** 2 - v ** 2) ** 2
Vmin_depth = Vsm.subs(Hs, 0) - Vsm.subs(Hs, v)  # |V_min| relative to V(0) -- SM convention
chk("v^2 m_h^2 = 2 lam v^4 = 8|V_min|  [address.py:142]",
    sp.simplify(v ** 2 * 2 * lam * v ** 2 - 8 * Vmin_depth) == 0)
e = sp.Symbol("epsilon")
chk("V(v(1+e)) - V(v) = |V_min| e^2 (2+e)^2  [address.py:129]",
    sp.simplify(Vsm.subs(Hs, v * (1 + e)) - Vsm.subs(Hs, v) - Vmin_depth * e ** 2 * (2 + e) ** 2) == 0)
# General shape with same v and same curvature m_h^2, cubic deformed by kappa:
kap = sp.Symbol("kappa")
d_ = sp.Symbol("delta")
Vgen = sp.Rational(1, 2) * mh ** 2 * d_ ** 2 + kap * mh ** 2 / (2 * v) * d_ ** 3 + mh ** 2 / (8 * v ** 2) * d_ ** 4
# kappa = 1 reproduces the SM expansion
Vsm_exp = sp.expand(Vsm.subs(Hs, v + d_).subs(lam, mh ** 2 / (2 * v ** 2)) - Vsm.subs(Hs, v).subs(lam, mh ** 2 / (2 * v ** 2)))
chk("kappa = 1 family member is the SM potential", sp.simplify(Vgen.subs(kap, 1) - Vsm_exp) == 0)
lin_resp = sp.solve(sp.diff(Vgen, d_, 2).subs(d_, 0) * D + rho / v, D)[0] / v
chk("linear response eps = -rho/(v^2 m_h^2) is kappa-INDEPENDENT (curvature only)",
    sp.simplify(sp.diff(lin_resp, kap)) == 0 and sp.simplify(lin_resp + rho / (v ** 2 * mh ** 2)) == 0)
Egen = sp.expand(Vgen.subs(d_, v * e))
lead = sp.Rational(1, 2) * mh ** 2 * v ** 2 * e ** 2
chk("field energy at O(eps^2) = (1/2) m_h^2 v^2 eps^2 = 4|V_min|eps^2, kappa-independent",
    sp.simplify(Egen.coeff(e, 2) - mh ** 2 * v ** 2 / 2) == 0)
chk("O(eps^3) field energy depends on kappa (not fixed by data)",
    sp.simplify(sp.diff(Egen.coeff(e, 3), kap)) != 0, str(Egen.coeff(e, 3)))
ratio = sp.simplify((v ** 2 * mh ** 2 * e) / lead)
chk("source/field ratio -> 2/eps at leading order, curvature-only", sp.simplify(ratio - 2 / e) == 0)


# R2b: the exact (nonlinear, SM-shape) uniform solution vs the linear law
rho_exact = sp.solve(sp.Eq(sp.diff(Vsm, Hs).subs(Hs, v * (1 + e)), -rho / v), rho)[0]
chk("exact uniform SM-shape source: rho = -8|V_min| eps (1+eps)(1+eps/2)",
    sp.simplify(rho_exact + 8 * Vmin_depth * e * (1 + e) * (1 + e / 2)) == 0, str(sp.factor(rho_exact)))
ratio_exact = sp.simplify(sp.Abs(rho_exact).subs(e, sp.Symbol("q", positive=True)) /
                          (Vmin_depth * e ** 2 * (2 + e) ** 2).subs(e, sp.Symbol("q", positive=True)))
q = sp.Symbol("q", positive=True)
chk("exact source/field ratio = 4(1+eps)/(eps(2+eps)); tree's 8/(eps(2+eps)^2) is its linear-source form",
    sp.simplify(ratio_exact - 4 * (1 + q) / (q * (2 + q))) == 0)
rel = sp.simplify((4 * (1 + q) / (q * (2 + q))) / (8 / (q * (2 + q) ** 2)))
print("     exact/tree ratio = %s ; at eps = 8.2e-16: %.3e ; at eps = 1: %s" % (rel, float(rel.subs(q, 8.2e-16)) - 1, rel.subs(q, 1)))

# ----------------------------------------------------------------- R3
print("== R3 Yukawa exterior and the uniform sphere")
r, R, M_, r0, J = sp.symbols("r R M r_0 J", positive=True)
lamh = 1 / M_
ext = (r0 / r) * sp.exp(-(r - r0) * M_)
res = sp.simplify(sp.diff(r ** 2 * sp.diff(ext, r), r) / r ** 2 - M_ ** 2 * ext)
chk("eps_0 (r0/r) e^{-(r-r0)/lam} solves (lap - m^2) eps = 0 outside  [address.py:164]", res == 0)
A, B = sp.symbols("A B")
inside = A * sp.sinh(M_ * r) / r - J / M_ ** 2      # (lap - m^2) d = J inside
outside = B * sp.exp(-M_ * r) / r
sol = sp.solve([sp.Eq(inside.subs(r, R), outside.subs(r, R)),
                sp.Eq(sp.diff(inside, r).subs(r, R), sp.diff(outside, r).subs(r, R))], [A, B], dict=True)[0]
surf = sp.simplify(outside.subs(sol).subs(r, R) / (-J / M_ ** 2))
lim = sp.limit(surf, R, sp.oo)
chk("uniform sphere, R >> lambda_h: surface value / interior value -> 1/2", sp.simplify(lim - sp.Rational(1, 2)) == 0,
    "exact ratio = %s" % sp.simplify(surf))
print("     => a tail started at the INTERIOR eps overstates the standoff by lambda_h ln 2")

# ----------------------------------------------------------------- R4
print("== R4 scalar density vs number density (psibar psi -> n hypothesis)")
k, kF, mN = sp.symbols("k k_F m_N", positive=True)
rs = 3 / kF ** 3 * sp.integrate(k ** 2 * mN / sp.sqrt(k ** 2 + mN ** 2), (k, 0, kF))
hbarc = 197.3269804  # MeV fm
n0 = 0.16
kF_val = (1.5 * math.pi ** 2 * n0) ** (1.0 / 3.0)   # symmetric matter, degeneracy 4
mN_val = 938.92 / hbarc
rs_val = float(rs.subs({kF: kF_val, mN: mN_val}))
print("     k_F = %.4f fm^-1, rho_s/rho_B (free, M* = m_N) = %.5f" % (kF_val, rs_val))
chk("free Fermi gas at n0: rho_s/rho_B within 3%% of 1", abs(1 - rs_val) < 0.03, "%.4f" % rs_val)

# ----------------------------------------------------------------- R5
print("== R5 numbers from the owner and under moved inputs")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import address as A_  # noqa: E402  (read-only)

C = A_.C
VMIN = A_.VMIN_SI
ed = {h_: A_.eps_det_stationary(h_) for h_ in ("H1", "H2")}


def eps_mat(rho_tot, frac, vmin=VMIN):
    return -(rho_tot * frac) * C ** 2 / (8.0 * vmin)


tree = {h_: A_.EPS_NUCLEAR[h_] for h_ in ("H1", "H2")}
mine = {h_: eps_mat(A_.RHO_NUCLEAR, A_.higgs_fraction(0.06, h_)) for h_ in ("H1", "H2")}
chk("EPS_NUCLEAR reproduced independently (H1, H2)",
    all(abs(mine[h_] / tree[h_] - 1) < 1e-12 for h_ in mine),
    "H1 %.6e  H2 %.6e" % (tree["H1"], tree["H2"]))
print("     tree ratios over eps_det: H1 %.1f  H2 %.1f" % (A_.EPS_NUCLEAR_OVER_DET["H1"], A_.EPS_NUCLEAR_OVER_DET["H2"]))
# hbar-c conversion of 8|Vmin| to v^2 m_h^2 in SI
v2m2 = A_.higgs.gev4_to_si(A_.V_GEV ** 2 * A_.M_HIGGS ** 2)
chk("8|V_min| (SI) == v^2 m_h^2 (SI) numerically", abs(8 * VMIN / v2m2 - 1) < 1e-12)
cases = [
    ("tree H1, S=0.06 (LO SVZ, u+d only)", 2 / 9 + 7 / 9 * 0.06),
    ("H1 at S=0.09 (strange included, tree's 3rd scan)", 2 / 9 + 7 / 9 * 0.09),
    ("H1 beyond-LO heavy sum at S=0.06 (sibling, Hill-Solon)", 0.28177),
    ("f_N = 0.30 (Cline et al 1306.4710v5 p.8, READ)", 0.30),
    ("f_N = 0.305 (Hoferichter 2015 eq24, via sibling)", 0.305),
    ("f_N = 0.35 (upper literature value, WebSearch snippet)", 0.35),
    ("tree H2, S=0.06", 0.06),
    ("H2 with strange S=0.111", 0.111),
]
print("     %-58s %12s %10s %10s" % ("coupling case", "eps", "/det_H1", "/det_H2"))
worst = 1e99
for lab, fr in cases:
    for n0x in (0.15, 0.16):
        rho_tot = A_.RHO_NUCLEAR * n0x / 0.16
        ev = eps_mat(rho_tot, fr)
        r1, r2 = abs(ev) / ed["H1"], abs(ev) / ed["H2"]
        worst = min(worst, r1, r2)
        print("     %-50s n0=%.2f %12.4e %10.1f %10.1f" % (lab, n0x, ev, r1, r2))
chk("every coupling/n0 case keeps nuclear eps above eps_det (verdict unmoved)", worst > 1, "min ratio %.1f" % worst)
# m_h move (PDG 2024 125.20 vs RPP 2026 125.13): eps ~ 1/m_h^2
mh_move = (125.13 / 125.20) ** 2 - 1
print("     m_h 125.13 -> 125.20 moves eps by %.2e (relative)" % mh_move)
chk("m_h move below 0.2%", abs(mh_move) < 2e-3)
# electrons: coupling m_e/v per electron, Z/A ~ 0.4-0.5 electrons per nucleon
for ZA in (0.4, 0.5):
    for lab, fr in (("H1", 0.26889), ("H2", 0.06)):
        share = ZA * A_.M_E_MEV / (fr * 938.92)
        print("     electrons Z/A=%.1f vs %s nucleon Higgs part: %.2e" % (ZA, lab, share))
chk("electron neglect < 0.5%% even against H2", 0.5 * A_.M_E_MEV / (0.06 * 938.92) < 5e-3)
# courier densities: H1 physical coupling vs H2
print("     courier source (eps=1e-18 over an atom): H1 %.3e  H2 %.3e kg/m^3"
      % (A_.COURIER_SOURCE_KG_M3["H1"], A_.COURIER_SOURCE_KG_M3["H2"]))
c_fN = A_.source_density(1e-18, 0.30)[0]
print("     ... with f_N = 0.30: %.3e kg/m^3 = %.2e x osmium (22590)" % (c_fN, c_fN / 22590))
chk("courier source with READ f_N still > 1e7 x osmium", c_fN / 22590 > 1e7)
lam_code = A_.yukawa_range()
print("     lambda_h computed %.5e m (address.py:163 prose says 1.5761e-18 = 125.20 value)" % lam_code)
chk("prose 1.5761e-18 is the 125.20 value (stale rounding, discrepancy only)",
    abs(A_.HBAR * C / (125.20 * A_.GEV_IN_J) - 1.5761e-18) / 1.5761e-18 < 1e-4 and abs(lam_code - 1.5761e-18) / 1.5761e-18 > 4e-4)

# ----------------------------------------------------------------- R6
print("== R6 Shi 2107.04206 nonperturbative (1210) phase vs the tree's uses")
# READ (p.15): M_1210 ~ 2.7e14 a_m^2 kg with valence coupling (m_u+m_d)/2 = 3.45 MeV per nucleon.
f_val = 3.45 / 938.92
for lab, fr in (("valence (Shi)", f_val), ("tree H1", 0.26889), ("tree H2", 0.06)):
    for what, a_m, need_rho in (("nucleus a=7 fm, rho_n", 7e-15, A_.RHO_NUCLEAR),
                                ("Bohr region, courier H2", A_.A_BOHR_M, A_.COURIER_SOURCE_KG_M3["H2"]),
                                ("1 m sphere, courier H2", 1.0, A_.COURIER_SOURCE_KG_M3["H2"])):
        Mc = 2.7e14 * a_m ** 2 * (f_val / fr)
        rho_c = Mc / (4.0 / 3.0 * math.pi * a_m ** 3)
        print("     %-14s %-26s rho_c %.2e  needed %.2e  margin %.1e" % (lab, what, rho_c, need_rho, rho_c / need_rho))
chk("nuclear and atomic-scale uses sit in the perturbative phase for every coupling",
    all(2.7e14 * a ** 2 * (f_val / fr) / (4 / 3 * math.pi * a ** 3) > 10 * nr
        for fr in (0.26889, 0.06, 0.35) for a, nr in ((7e-15, A_.RHO_NUCLEAR),
                                                       (A_.A_BOHR_M, A_.COURIER_SOURCE_KG_M3["H2"]))))
rc1m = 2.7e14 * (f_val / 0.26889) / (4 / 3 * math.pi)
print("     1 m sphere under tree H1: rho_c ~ %.2e kg/m^3 -- linear branch NOT unique above this" % rc1m)

# ----------------------------------------------------------------- R7
print("== R7 ultralocal limit d = -J/m^2 [1 + O((lam/L)^2)]")
X, Lx, a0 = sp.symbols("X L a0", positive=True)
Jx = a0 + sp.cos(X / Lx)          # offset source with zeros when a0 < 1
# exact periodic solution of (d_XX - m^2) d = J
dex = -a0 / M_ ** 2 - sp.cos(X / Lx) / (M_ ** 2 + 1 / Lx ** 2)
chk("exact 1D solution", sp.simplify(sp.diff(dex, X, 2) - M_ ** 2 * dex - Jx) == 0)
absdiff = sp.simplify(dex + Jx / M_ ** 2)
bound = sp.simplify(sp.Abs(sp.diff(Jx, X, 2)) / M_ ** 4)
chk("absolute error |d + J/m^2| <= |J''|/m^4 (sup norm)",
    sp.simplify(sp.Abs(absdiff).subs({a0: 0}) - (sp.Abs(sp.cos(X / Lx)) / (Lx ** 2 * M_ ** 2 * (M_ ** 2 + 1 / Lx ** 2)))) == 0)
val = absdiff.subs({a0: sp.Rational(1, 2), X: sp.acos(-sp.Rational(1, 2)) * Lx})
Jzero = Jx.subs({a0: sp.Rational(1, 2), X: sp.acos(-sp.Rational(1, 2)) * Lx})
chk("multiplicative form fails where J = 0 but d != 0 (offset source)", sp.simplify(Jzero) == 0 and sp.simplify(val) != 0,
    "d at J=0: %s" % sp.simplify(val))

print()
print("FAILS:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)
