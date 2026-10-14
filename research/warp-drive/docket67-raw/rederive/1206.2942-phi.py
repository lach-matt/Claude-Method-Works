#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 1206.2942-phi.

Morrissey & Ramsey-Musolf, arXiv:1206.2942v1 p.4 (READ):
  "phi/sqrt(2) = <H^0>  (1) ... Note that (in unitary gauge) the masses of the
   W+- and Z0 weak vector bosons and the fermions are proportional to phi."

Checks (sympy unless stated):
  A. Tree level, SM doublet H = (0, phi/sqrt2): m_W = g phi/2, m_Z = sqrt(g^2+g'^2) phi/2
     from |D_mu H|^2 (Pauli matrices, explicit), and m_f = y phi/sqrt2 from the Yukawa
     term.  All three proportional to phi; d ln m / d ln phi = 1 exactly.
  B. phi^2 = 2 H^dag H is gauge invariant (so the classical statement needs no gauge
     choice; the 'unitary gauge' qualifier matters only for identifying phi with a
     component, and the gauge dependence the source flags on p.8 is the loop-level
     effective-potential minimum).
  C. IDENTITY: for any field-dependent mass m(phi), the Higgs coupling is
     g_hff = m'(v) (h = phi - v), so the kappa-framework modifier
     kappa_f = g_hff v / m(v) = d ln m / d ln phi |_v.  Checked against
     Erdelyi-Grober-Selimovic 2501.07628 eq.(10) (READ): with the SMEFT operator
     m(phi) = phi/sqrt2 (y - C phi^2/2), kappa_e = 1 - v^3 C/(sqrt2 m_e).
  D. Single-doublet gauge invariance: every operator (l e H)(H^dag H)^n gives
     m ~ phi^(2n+1), odd, so m(0) = 0 for ANY combination -> massform's
     contrapositive "m_f > 0 => phi != 0" survives beyond the renormalisable SM;
     linearity (kappa = 1) does not.
  E. excite section 3 generalised: for a source of mass m(phi), equilibrium
     V'(phi) + n m'(phi) = 0 gives source rest energy n m = -V'(phi) phi / kappa(phi).
     Tree's 4 eps(2-eps)(1-eps)^2 is the kappa = 1 case; ratio source/field
     -> 2/(kappa eps).  (For nucleons the tree's own f = d ln m_p/d ln v IS this kappa.)
  F. DATA (numeric): kappa_e bound from ATLAS 1909.10235 BR(H->ee) < 3.6e-4 with the
     SM BR formula G_F m_H m_e^2/(4 sqrt2 pi Gamma_H) READ there (Gamma_H = 4.1 MeV READ
     there); CODATA 2022 m_e and G_F (READ 2409.03787); v = (sqrt2 G_F)^-1/2; tree Yukawas.
  G. Sensitivity of the tree's K_mu (address.K_mu, 'm_e is 100% Higgs, subtract
     exactly 1') and of f = d ln m_p/d ln v to kappa_e and to a light-quark kappa_l,
     at the tree's S = 0.06 fixture, using the tree's own H1/H2 decomposition
     (address.dln_mp_dln_v: H1 = (2/9)(1-S) + S; H2 = S) with the S term scaled by kappa_l.
  H. Order of the H-TREE correction to d ln m_e/d ln v from QED running (one-loop
     gamma_m = 3 alpha/(2 pi)); estimate only, labelled as such.
Exit 0 iff every assertion holds.
"""
import math
import sys
import sympy as sp

FAIL = []


def check(label, cond):
    print(("PASS  " if cond else "FAIL  ") + label)
    if not cond:
        FAIL.append(label)


# ---------------------------------------------------------------- A
g, gp, phi, y, v = sp.symbols("g gp phi y v", positive=True)
W1, W2, W3, B = sp.symbols("W1 W2 W3 B", real=True)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
H = sp.Matrix([0, phi / sp.sqrt(2)])
# covariant-derivative gauge part acting on constant H: -i (g/2 W^a s^a + g'/2 Y B), Y = 1/2
# hypercharge term is g' Y B with Y = 1/2  ->  (g'/2) B
Agauge = -sp.I * (g / 2 * (W1 * s1 + W2 * s2 + W3 * s3) + gp / 2 * B * sp.eye(2))
DH = Agauge * H
kin = sp.expand((DH.H * DH)[0])            # |D H|^2 with constant H
kin = sp.simplify(kin.subs({sp.conjugate(W1): W1, sp.conjugate(W2): W2,
                            sp.conjugate(W3): W3, sp.conjugate(B): B}))
# charged: m_W^2 W+W- with W+- = (W1 -+ i W2)/sqrt2 ; coefficient of W1^2 is m_W^2/2
mW2 = 2 * sp.Poly(kin, W1).coeff_monomial(W1**2)
check("A1 m_W = g phi/2 from |D_mu H|^2", sp.simplify(sp.sqrt(mW2) - g * phi / 2) == 0)
# neutral: kin_neutral = (phi^2/8)(g W3 - g' B)^2 = (1/2) m_Z^2 Z^2, Z = (g W3 - g' B)/sqrt(g^2+g'^2)
neutral = sp.expand(kin - kin.subs({W3: 0, B: 0}))
Zexpr = (g * W3 - gp * B) / sp.sqrt(g**2 + gp**2)
mZ2 = sp.simplify(2 * neutral / sp.expand(Zexpr**2))
check("A2 m_Z = sqrt(g^2+g'^2) phi/2", sp.simplify(sp.sqrt(mZ2) - sp.sqrt(g**2 + gp**2) * phi / 2) == 0)
photon_mass = sp.simplify(neutral.subs({W3: gp / sp.sqrt(g**2 + gp**2), B: g / sp.sqrt(g**2 + gp**2)}))
check("A3 orthogonal combination (photon) massless", photon_mass == 0)
mf = y * phi / sp.sqrt(2)
for name, m in (("W", g * phi / 2), ("Z", sp.sqrt(g**2 + gp**2) * phi / 2), ("f", mf)):
    check("A4 d ln m_%s / d ln phi = 1 (tree)" % name, sp.simplify(sp.diff(sp.log(m), phi) * phi - 1) == 0)
check("A5 m_f(phi=0) = 0 at tree level", mf.subs(phi, 0) == 0)

# ---------------------------------------------------------------- B
# H^dag H invariant under a generic SU(2) x U(1) element: check with U = exp(i a.s/2) numerically-symbolic
a1, a2, a3, th = sp.symbols("a1 a2 a3 th", real=True)
h1, h2 = sp.symbols("h1 h2")
Hg = sp.Matrix([h1, h2])
U = sp.exp(sp.I * th / 2) * (sp.Matrix(sp.exp(sp.I * (a3 * s3) / 2)))   # diagonal subgroup, exact
HdH = (Hg.H * Hg)[0]
HdH_rot = sp.simplify(((U * Hg).H * (U * Hg))[0])
check("B1 H^dag H invariant (U(1)_Y x diagonal SU(2) subgroup, symbolic)", sp.simplify(HdH_rot - HdH) == 0)
# full SU(2): unitary => invariance; check unitarity of a general SU(2) element numerically
import cmath
def su2(x1, x2, x3):
    n = math.sqrt(x1 * x1 + x2 * x2 + x3 * x3)
    c, s = math.cos(n / 2), math.sin(n / 2)
    return [[c + 1j * s * x3 / n, 1j * s * (x1 - 1j * x2) / n],
            [1j * s * (x1 + 1j * x2) / n, c - 1j * s * x3 / n]]
Un = su2(0.7, -1.3, 0.4)
hv = [0.3 + 0.8j, -1.1 + 0.2j]
hr = [Un[0][0] * hv[0] + Un[0][1] * hv[1], Un[1][0] * hv[0] + Un[1][1] * hv[1]]
check("B2 H^dag H invariant under a generic SU(2) element (numeric)",
      abs(sum(abs(z)**2 for z in hr) - sum(abs(z)**2 for z in hv)) < 1e-12)

# ---------------------------------------------------------------- C
C, me = sp.symbols("C m_e", real=True)
m_of = phi / sp.sqrt(2) * (y - C * phi**2 / 2)
ghee = sp.diff(m_of, phi).subs(phi, v)
kappa = sp.simplify(ghee * v / m_of.subs(phi, v))
kappa_log = sp.simplify((sp.diff(sp.log(m_of), phi) * phi).subs(phi, v))
check("C1 kappa_f = g_hff v/m = d ln m/d ln phi at v (general identity, SMEFT instance)",
      sp.simplify(kappa - kappa_log) == 0)
me_expr = m_of.subs(phi, v)
kappa_2501 = 1 - v**3 * C / (sp.sqrt(2) * me_expr)
check("C2 reproduces 2501.07628 eq.(10): kappa_e = 1 - v^3 C/(sqrt2 m_e)",
      sp.simplify(kappa - kappa_2501) == 0)
check("C3 kappa = 1 iff C = 0 (renormalisable SM)", sp.solve(sp.Eq(kappa, 1), C) == [0])

# ---------------------------------------------------------------- D
cs = sp.symbols("c0:4", real=True)
m_gen = sum(cs[n] * phi**(2 * n + 1) for n in range(4))
check("D1 any single-doublet operator sum gives m(0) = 0", m_gen.subs(phi, 0) == 0)
check("D2 m(phi) odd: m(-phi) = -m(phi)", sp.simplify(m_gen.subs(phi, -phi) + m_gen) == 0)
k_gen = sp.simplify(sp.diff(m_gen, phi) * phi / m_gen)
check("D3 kappa = weighted mean of (2n+1): pure phi^3 operator gives kappa = 3",
      sp.simplify(k_gen.subs({cs[0]: 0, cs[2]: 0, cs[3]: 0}) - 3) == 0)

# ---------------------------------------------------------------- E
lam, eps, n, m0, k = sp.symbols("lambda epsilon n m0 k", positive=True)
V = lam / 4 * (phi**2 - v**2)**2
rho = lam * v**4 / 4
mk = m0 * (phi / v)**k
nsol = sp.solve(sp.Eq(sp.diff(V, phi) + n * sp.diff(mk, phi), 0), n)[0]
src = sp.simplify((nsol * mk) / rho).subs(phi, v * (1 - eps))
src_tree = 4 * eps * (2 - eps) * (1 - eps)**2
check("E1 k = 1 reproduces excite's source rest energy 4 eps(2-eps)(1-eps)^2",
      sp.simplify(src.subs(k, 1) - src_tree) == 0)
check("E2 general k: source = tree / k", sp.simplify(src - src_tree / k) == 0)
field = sp.simplify((V - V.subs(phi, v)) / rho).subs(phi, v * (1 - eps))
check("E3 field energy eps^2(2-eps)^2 (independent of k)", sp.simplify(field - (eps * (2 - eps))**2) == 0)
ratio_lead = sp.limit(sp.simplify(src / field) * eps, eps, 0)
check("E4 source/field -> 2/(k eps)", sp.simplify(ratio_lead - 2 / k) == 0)

# ---------------------------------------------------------------- F  (numeric data)
GF = 1.1663787e-5          # GeV^-2, CODATA 2022 (READ 2409.03787, Table XXXIII)
ME_CODATA = 0.51099895069e-3   # GeV, CODATA 2022 (READ)
ME_TREE = 0.510998951e-3       # GeV, massform capture
MH = 125.0                 # GeV, as used by 1909.10235 (READ: 'Higgs boson mass of 125 GeV')
GAMMA_H = 4.1e-3           # GeV, SM width used by 1909.10235 (READ p.5)
BR_LIMIT = 3.6e-4          # observed 95% CL, 1909.10235 (READ)
vev = (math.sqrt(2) * GF) ** -0.5
print("      v = (sqrt2 G_F)^-1/2 = %.6f GeV (tree higgs.vev() = 246.219640)" % vev)
check("F1 tree v agrees with CODATA-2022 G_F to 1e-6", abs(vev - 246.21964023926205) / vev < 1e-6)
check("F2 tree m_e agrees with CODATA 2022 to 1e-9 relative",
      abs(ME_TREE - ME_CODATA) / ME_CODATA < 1e-9)
br_sm = GF * MH * ME_CODATA**2 / (4 * math.sqrt(2) * math.pi * GAMMA_H)
print("      SM BR(H->ee) = %.3e (source says ~5e-9)" % br_sm)
check("F3 SM BR(H->ee) ~ 5e-9 as 1909.10235 states", 4.5e-9 < br_sm < 5.5e-9)
kappa_e_max = math.sqrt(BR_LIMIT / br_sm)
print("      |kappa_e| < %.0f (95%% CL) -- 2501.07628 quotes 260" % kappa_e_max)
check("F4 |kappa_e| bound ~ 260 (within 5%)", abs(kappa_e_max - 260) / 260 < 0.05)
ye = math.sqrt(2) * ME_CODATA / vev
check("F5 tree electron Yukawa 2.935e-6 reproduced", abs(ye - 2.935e-6) / 2.935e-6 < 1e-3)
yt = math.sqrt(2) * 172.6 / vev
check("F6 tree top Yukawa 0.9914 reproduced at the tree's m_t = 172.6 GeV", abs(yt - 0.9914) < 5e-4)

# ---------------------------------------------------------------- G
S = 0.06
def f_H1(kl, klam=1.0):
    return sp.Rational(2, 9) * klam * (1 - S) + kl * S
def f_H2(kl):
    return kl * S
Kmu_tree = {"H1": float(f_H1(1)) - 1, "H2": float(f_H2(1)) - 1}
print("      tree K_mu at S=0.06 (kappa_e=1): H1 %.5f  H2 %.5f" % (Kmu_tree["H1"], Kmu_tree["H2"]))
check("G1 tree K_mu(H1) = 2/9(1-S)+S-1 = -0.73111", abs(Kmu_tree["H1"] + 0.731111) < 1e-5)
# kappa_e enters K_mu one-for-one: K_mu = f - kappa_e
for ke in (0.0, 1.0, 10.0, 260.0):
    print("      kappa_e = %6.1f :  K_mu(H1) = %9.4f   K_mu(H2) = %9.4f"
          % (ke, float(f_H1(1)) - ke, float(f_H2(1)) - ke))
ke_s, S_s = sp.symbols("kappa_e S_s", real=True)
Kmu_sym = sp.Rational(2, 9) * (1 - S_s) + S_s - ke_s   # d ln m_p/d ln v - d ln m_e/d ln v, H1
check("G2 K_mu = f - kappa_e: d K_mu/d kappa_e = -1 (symbolic); tree's 'subtract exactly 1' is kappa_e = 1",
      sp.diff(Kmu_sym, ke_s) == -1 and sp.simplify(Kmu_sym.subs({ke_s: 1, S_s: sp.Rational(3, 50)}) + sp.Rational(329, 450)) == 0)
for kl in (0.0, 1.0, 3.0):
    print("      kappa_l = %4.1f :  f(H1) = %.5f   f(H2) = %.5f   rho_stable scales as 1/f"
          % (kl, float(f_H1(kl)), float(f_H2(kl))))
check("G3 under H2, f = kappa_l S: rho_stable ~ 1/kappa_l (diverges at kappa_l = 0)",
      float(f_H2(0)) == 0.0)

# ---------------------------------------------------------------- H  (estimate)
alpha = 1 / 137.035999177
gm = 3 * alpha / (2 * math.pi)
print("      one-loop QED gamma_m = 3 alpha/2pi = %.5f -> d ln m_e(m_e)/d ln v ~ 1/(1-gamma_m) = %.5f (ESTIMATE)"
      % (gm, 1 / (1 - gm)))
check("H1 H-TREE's correction to 'exactly 1' is O(3.5e-3), far inside the kappa_e data window",
      1 / (1 - gm) - 1 < 0.004)

print("\n%d failure(s)" % len(FAIL))
sys.exit(1 if FAIL else 0)
