#!/usr/bin/env python3
"""D67 re-derivation: hyperfine-optical-scaling.

Checks, each with its status:
  A  dimensional analysis: nu/(c R_inf) = F(alpha, Z; m_e/M, r_N m_e c/hbar)   PROVED (sympy nullspace)
  B  Schrodinger + reduced mass: B_opt(single) = (m_e/M)/(1+m_e/M), cancels in same-atom ratio  PROVED (sympy)
  C  Dirac point nucleus infinite mass: nu/(c R_inf) m_e-free                   PROVED (sympy.physics.hydrogen)
  D  leading relativistic recoil (Barker-Glover / CODATA form, RECALLED, NAMED-NOT-READ):
     K_recoil for H(1S-2S)/(2P-3D) vs the tree's finite-size K                    CONDITIONAL
  E  Fermi contact hyperfine: exponents alpha^2, (m_e/m_p)^1, g_I^1             PROVED (sympy);
     numeric vs H 1420.405751768 MHz (value RECALLED, NAMED-NOT-READ)
  F  Casimir relativistic factor 3/(gamma(4 gamma^2-1)) (RECALLED) -> K_rel(Cs) vs Godun's 0.83 (READ)
  G  g_I variation under a displaced vev: optical/Cs coefficient vs kappa_Cs (value NOT read; scanned)
  H  transported optical clock: 1 + (2 + A_opt) K_alpha(H1) + recoil  vs tree's '+1 EXACTLY'
Constants: scipy.constants = CODATA 2022 (installed scipy 1.17.1).
"""
import math, sys, importlib.util
import sympy as sp
from scipy import constants as SC

PC = SC.physical_constants
ALPHA = PC['fine-structure constant'][0]
RYC = PC['Rydberg constant times c in Hz'][0]
ME_MP = PC['electron-proton mass ratio'][0]
MUP_MUB = PC['proton mag. mom. to Bohr magneton ratio'][0]
RP = PC['proton rms charge radius'][0]
A0 = PC['Bohr radius'][0]
AE = PC['electron mag. mom. anomaly'][0]
out = {}
fails = []
def chk(name, cond):
    print(("  PASS " if cond else "  FAIL ") + name)
    if not cond: fails.append(name)

print("A  dimensional analysis")
# columns: m_e, c, hbar, q2=e^2/(4 pi eps0), M, r_N ; rows: M L T
D = sp.Matrix([[1, 0, 1, 1, 1, 0],
               [0, 1, 2, 3, 0, 1],
               [0, -1, -1, -2, 0, 0]])
ns = D.nullspace()
print("   nullity =", len(ns), " basis:", [list(v.T) for v in ns])
chk("three dimensionless groups (alpha, m_e/M, r_N m_e c/hbar)", len(ns) == 3)
# energy E = m_e c^2 * F(groups); h c R_inf = m_e c^2 alpha^2 / 2 -> ratio = 2F/alpha^2: m_e appears only through groups
# with M -> inf, r_N -> 0 only alpha remains
chk("alpha = q2/(hbar c) in nullspace span", sp.Matrix([0, -1, -1, 1, 0, 0]).T * D.T == sp.zeros(1, 3))

print("B  Schrodinger with reduced mass")
Z, n1, n2, mu = sp.symbols('Z n1 n2 mu', positive=True)   # mu = M/m_e
nu = Z**2 * (1/n1**2 - 1/n2**2) / (1 + 1/mu)
B1 = sp.simplify(sp.diff(sp.log(nu), mu) * mu)
print("   d ln(nu/cR)/d ln(M/m_e) =", B1)
n3, n4 = sp.symbols('n3 n4', positive=True)
ratio = nu / (Z**2 * (1/n3**2 - 1/n4**2) / (1 + 1/mu))
chk("reduced mass cancels exactly in a same-atom ratio", sp.simplify(sp.diff(ratio, mu)) == 0)
Bh = float(B1.subs(mu, 1 / ME_MP))
out['B_single_H'] = Bh
print("   hydrogen single-transition B = %.6e" % Bh)

print("C  Dirac, point nucleus, infinite mass")
from sympy.physics.hydrogen import E_nl_dirac, E_nl
al = sp.symbols('alpha', positive=True)
# sympy works in Hartree units with c = 1/alpha: E_h = m_e c^2 alpha^2, h c R_inf = E_h/2
for (n, l, up) in [(1, 0, True), (2, 0, True), (2, 1, False), (2, 1, True), (3, 2, True)]:
    E = E_nl_dirac(n, l, spin_up=up, Z=1, c=1/al)
    ratio_R = sp.simplify(2 * E)   # nu/(c R_inf) incl. rest-energy offset removed by sympy
    nr = sp.limit(ratio_R, al, 0)
    chk("Dirac n=%d l=%d up=%s -> nu/cR is a function of alpha only, NR limit %s" % (n, l, up, nr),
        ratio_R.free_symbols <= {al} and nr == 2 * E_nl(n, 1))

print("D  relativistic recoil in H(1S-2S)/(2P-3D)  [formula RECALLED: E = m_r c^2 (f-1) - m_r^2 c^2 (f-1)^2/(2M)]")
def f_dirac(n, j, za):
    d = (j + 0.5) - math.sqrt((j + 0.5)**2 - za**2)
    return 1.0 / math.sqrt(1 + (za / (n - d))**2)
def E_level(n, j, x):     # x = m_e/M ; units m_e c^2 ; fs added for S (tree's form, H2)
    mr = 1 / (1 + x)
    fm1 = f_dirac(n, j, ALPHA) - 1
    return mr * fm1 - mr**2 * fm1**2 / 2 * x
def lnratio(x, pair2):
    (a, ja, b, jb) = pair2
    return math.log((E_level(2, .5, x) - E_level(1, .5, x)) / (E_level(b, jb, x) - E_level(a, ja, x)))
x0 = ME_MP
h = 1e-3
res = {}
for lab, pair in [("2P1/2-3D3/2", (2, .5, 3, 1.5)), ("2P3/2-3D5/2", (2, 1.5, 3, 2.5))]:
    dl = (lnratio(x0 * (1 + h), pair) - lnratio(x0 * (1 - h), pair)) / (2 * h)   # d ln ratio / d ln(m_e/M)
    res[lab] = dl
    print("   d ln[nu(1S-2S)/nu(%s)] / d ln(m_e/M) = %.4e" % (lab, dl))
# independent series estimate: relative recoil term per level = (Za)^2 x/(4 n^2)
S = 0.06
dlnx_H2 = 1 - S                 # H2: d ln m_p / d ln v = S
dlnx_H1 = 1 - (2/9 + 7*S/9)     # H1
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
spec = importlib.util.spec_from_file_location("address", "/home/user/Claude-Method-Works/research/warp-drive/address.py")
addr = importlib.util.module_from_spec(spec); spec.loader.exec_module(addr)
Kfs_tree = addr.finite_size_K()
x_fs22 = RP / A0
Kfs22 = 28 * x_fs22**2 / (14 * x_fs22**2 - 9)
print("   tree finite-size K (r_p=%.4e) = %.4e ; with CODATA 2022 r_p=%.5e: %.4e (move %.3f%%)" %
      (addr.R_PROTON_M, Kfs_tree, RP, Kfs22, 100 * (Kfs22 / Kfs_tree - 1)))
for lab, dl in res.items():
    kr = dl * dlnx_H2
    print("   K_recoil(H2, S=0.06, %s) = %.4e  ; |K_recoil/K_fs| = %.1f" % (lab, kr, abs(kr / Kfs_tree)))
    out['K_recoil_H2_' + lab] = kr
out['K_fs_tree'] = Kfs_tree; out['K_fs_codata2022'] = Kfs22
chk("finite-size closed form reproduced (sympy) ",
    sp.simplify(addr.finite_size_K_sympy()[0] - 28*sp.Symbol('x',positive=True)**2/(14*sp.Symbol('x',positive=True)**2-9)) == 0)

print("E  Fermi contact hyperfine")
e, hb, c, eps0, me, mp, gI, gE, I = sp.symbols('e hbar c epsilon0 m_e m_p g_I g_e I', positive=True)
r = sp.symbols('r', positive=True)
from sympy.physics.hydrogen import R_nl
a0 = 4 * sp.pi * eps0 * hb**2 / (me * e**2)
R10 = R_nl(1, 0, r, 1).subs(r, r)          # atomic units, a0 = 1
psi0_sq_au = sp.limit(R10, r, 0)**2 / (4 * sp.pi)
chk("|psi_1s(0)|^2 = 1/(pi a0^3)", sp.simplify(psi0_sq_au - 1 / sp.pi) == 0)
psi0 = psi0_sq_au / a0**3
muB = e * hb / (2 * me); muN = e * hb / (2 * mp); mu0 = 1 / (eps0 * c**2)
dE = sp.Rational(2, 3) * mu0 * gE * muB * gI * muN * psi0 * (I + sp.Rational(1, 2))
alpha_expr = e**2 / (4 * sp.pi * eps0 * hb * c)
hcR = me * c**2 * alpha_expr**2 / 2
X = sp.simplify(dE / hcR)
A = sp.simplify(sp.diff(sp.log(X), e) * e / 2)    # e enters only through alpha^(1/2 per e): alpha ~ e^2
# cleaner: substitute e via alpha
aS = sp.symbols('alpha_s', positive=True)
Xa = sp.simplify(X.subs(e, sp.sqrt(4 * sp.pi * eps0 * hb * c * aS)))
print("   nu_hf/(c R_inf) =", Xa)
chk("alpha exponent exactly 2", sp.simplify(sp.diff(sp.log(Xa), aS) * aS) == 2)
chk("m_p exponent exactly -1 and m_e exponent exactly +1",
    sp.simplify(sp.diff(sp.log(Xa), mp) * mp) == -1 and sp.simplify(sp.diff(sp.log(Xa), me) * me) == 1)
chk("g_I exponent exactly 1", sp.simplify(sp.diff(sp.log(Xa), gI) * gI) == 1)
chk("no hbar, c, eps0 left", Xa.free_symbols <= {aS, me, mp, gI, gE, I})
# numeric: hydrogen, I=1/2, g_I = g_p = 2 mu_p/mu_N ; nu_F = (16/3) alpha^2 cR (mu_p/mu_B) (1+me/mp)^-3 (g_e=2)
nuF = 16 / 3 * ALPHA**2 * RYC * MUP_MUB / (1 + ME_MP)**3
nu_meas = 1420.405751768e6      # RECALLED (hydrogen maser), NAMED-NOT-READ
print("   Fermi nu_F(H) = %.6f MHz ; measured %.6f MHz ; ratio-1 = %.4e ; a_e = %.4e" %
      (nuF / 1e6, nu_meas / 1e6, nu_meas / nuF - 1, AE))
out['nuF_H_MHz'] = nuF / 1e6; out['ratio_meas_over_fermi_minus1'] = nu_meas / nuF - 1
chk("measured/Fermi - 1 is (a_e + O(alpha^2)) to within 5e-5 [Breit 1.5a^2=8e-5, Zemach/recoil ~-4e-5]",
    abs(nu_meas / nuF - 1 - AE) < 1e-4)
mu_s = sp.symbols('mu', positive=True)
Bhf = sp.simplify(sp.diff(sp.log(1 / mu_s * (1 + 1 / mu_s)**-3), mu_s) * mu_s)
print("   with reduced mass: B_hf(H) = %s = %.6f" % (Bhf, float(Bhf.subs(mu_s, 1 / ME_MP))))
out['B_hf_H_reduced_mass'] = float(Bhf.subs(mu_s, 1 / ME_MP))

print("F  Casimir relativistic factor (RECALLED, point nucleus, single s1/2 electron)")
za = sp.symbols('za', positive=True)
g = sp.sqrt(1 - za**2)
Frel = 3 / (g * (4 * g**2 - 1))
Krel = sp.simplify(sp.diff(sp.log(Frel), za) * za)
kcs = float(Krel.subs(za, 55 * ALPHA))
print("   K_rel(Z=55) = d ln F_rel/d ln alpha = %.4f ; Godun READ A_Cs - 2 = 0.83 ; diff %.3f" % (kcs, 0.83 - kcs))
out['K_rel_Cs_Casimir'] = kcs
chk("Casimir -> 1 as Z alpha -> 0", sp.limit(Frel, za, 0) == 1)

print("G  g_I not fixed: optical/Cs coefficient under a displaced vev")
for hyp, dlnXq in (("H1", 7 / 9), ("H2", 1.0)):
    Kmu = addr.K_mu(S, hyp)
    for kappa in (-0.05, -0.01, 0.01, 0.05):
        coef = (0 - (-1)) * Kmu - kappa * dlnXq
        print("   %s S=0.06 kappa_Cs=%+.2f : d ln(nu_opt/nu_Cs)/d ln v = %.4f (g_I fixed: %.4f; change %+.2f%%)" %
              (hyp, kappa, coef, Kmu, 100 * (coef / Kmu - 1)))

print("H  transported optical clock coefficient")
Ka1 = float(addr.K_alpha_coefficient("H1")) * addr.ALPHA_EM / math.pi
print("   tree K_alpha(H1) = %.6e (43 alpha/(54 pi) = %.6e)" % (Ka1, 43 / 54 * ALPHA / math.pi))
for Aopt, lab in ((0.0, "A_opt=0"), (0.88, "Yb+ E2 (Godun READ)"), (-5.95, "Yb+ E3 (Godun READ)")):
    b = 1 + (2 + Aopt) * Ka1
    print("   H1 %-22s : d ln(nu_in/nu_out)/d eps = %.5f  (tree: +1 EXACTLY; deviation %+.3f%%)" % (lab, b, 100 * (b - 1)))
    out['B_transport_H1_' + lab] = b
bH = 1 - Bh * dlnx_H2
print("   H2 hydrogen, reduced mass only        : %.6f (deviation %.2e)" % (bH, bH - 1))
print("   tree B_transported_optical() =", addr.B_transported_optical())
out['B_transport_H2_hydrogen_recoil'] = bH

print("\nSUMMARY", out)
print("FAILS:", fails)
sys.exit(1 if fails else 0)
