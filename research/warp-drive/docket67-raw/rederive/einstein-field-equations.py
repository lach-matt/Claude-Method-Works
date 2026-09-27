#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for the external result 'einstein-field-equations'.

What is checked (sympy, exact unless marked numeric):
  C1  trace: in n dims g^ab G_ab = (1 - n/2) R, so for n = 4 G_ab = 8 pi T_ab  <=>
      R_ab = 8 pi (T_ab - T g_ab / 2), and Ricci = 0 <=> G = 0 (vacuum).  n = 2 is degenerate.
  C2  static spherical, areal gauge: G^t_t = -2 m'/r^2, so G = 8 pi T with T^t_t = -rho gives
      dm/dr = 4 pi r^2 rho  (certify.py:118, tolman.py:313-317, overturn.py:40-41).
  C3  contracted Bianchi: nabla_a G^a_r = 0 identically for the same metric (Carroll p.117:
      "take the metric of your choice, compute G, demand T = G" -- T is then conserved).
  C4  axial.py V2: 8 pi (p_z - T/2) = 4 pi (u - p_r - p_phi + p_z), T = -u+p_r+p_z+p_phi.
  C5  null contraction: R_ab k^a k^b = 8 pi T_ab k^a k^b for null k, and a Lambda g_ab term
      drops out exactly (g_kk = 0) -- Morris-Thorne test metric, radial null k.
  C6  Raychaudhuri, shear- and twist-free: theta = 2 J'/J  =>  J'' = -(R_kk/2) J, so
      q = R_kk / 2 = (4 pi G / c^4) T_kk  (seatindex.py:89-91); Sturm frontier q l^2 = pi^2.
  C7  seatindex T_COEFF = pi c^4 / (4 G) with CODATA 2018 = CODATA 2022 G (numeric).
  C8  Lambda (measured later, Planck 2018): with G_ab + Lambda g_ab = 8 pi T^matter_ab,
      (a) de Sitter (T^matter = 0: traceless, conserved, static, spherical, regular centre)
          solves it and is NOT Minkowski  -> tolman THEOREM X needs Lambda = 0 when T is
          read as matter; with Lambda absorbed into T (T := G/8pi) the trace is 4 rho_L != 0
          and the hypothesis 'traceless' excludes it, so the theorem stands in that reading;
      (b) Misner-Sharp: m' = 4 pi r^2 rho + Lambda r^2 / 2;
      (c) magnitudes (numeric): rho_Lambda c^2, the shift in m(r) at stated radii, and the
          T_kk threshold of seatindex (unaffected: Lambda g_kk = 0).
  C9  foliation.py V7 claim: the metric at foliation.py:184 is Ricci-flat (vacuum).
  C10 certify.stress_energy returns G_ab itself ('c^4/8piG = 1'), i.e. 8 pi x the G=c=1
      T of certify.py:118; energy-condition SIGN tests are invariant under the positive
      factor 8 pi (checked on a sample), so the two conventions in one file do not collide.
Exit 0 iff every check passes.
"""
import sys
import sympy as sp

OK = []


def chk(name, cond):
    OK.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)


def ricci(g, X):
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    s += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            R[b, c] = sp.simplify(s)
    return R, gi, Gam


t, r, th, ph = sp.symbols('t r theta phi', real=True)
X = [t, r, th, ph]

# ---- C1 trace identity (n generic) -----------------------------------------
n, Rs = sp.symbols('n R')
trG = Rs - sp.Rational(1, 2) * n * Rs        # g^ab R_ab - (1/2) R g^ab g_ab
chk("C1 trace g^ab G_ab = (1 - n/2) R", sp.simplify(trG - (1 - n / 2) * Rs) == 0)
chk("C1 n=4: trace G = -R, so R = -8 pi T and R_ab = 8 pi (T_ab - T g_ab/2)",
    sp.simplify(trG.subs(n, 4) + Rs) == 0)
chk("C1 n=2: trace G = 0 identically (Einstein tensor degenerate)", trG.subs(n, 2) == 0)

# ---- C2, C3 static spherical Misner-Sharp -----------------------------------
Phi = sp.Function('Phi')(r)
m = sp.Function('m')(r)
g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - 2 * m / r), r**2, r**2 * sp.sin(th)**2)
R, gi, Gam = ricci(g, X)
Rsc = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(4) for b in range(4)))
Gdn = sp.simplify(R - Rsc * g / 2)
Gmix = sp.simplify(gi * Gdn)
chk("C2 G^t_t = -2 m'/r^2", sp.simplify(Gmix[0, 0] + 2 * sp.diff(m, r) / r**2) == 0)
rho = sp.Function('rho')(r)
sol = sp.solve(sp.Eq(Gmix[0, 0], 8 * sp.pi * (-rho)), sp.diff(m, r))
chk("C2 G = 8 pi T, T^t_t = -rho  =>  dm/dr = 4 pi r^2 rho",
    len(sol) == 1 and sp.simplify(sol[0] - 4 * sp.pi * r**2 * rho) == 0)
# divergence of the mixed tensor, component r: nabla_a G^a_b
b = 1
div = sum(sp.diff(Gmix[a, b], X[a]) for a in range(4))
div += sum(Gam[a][a][c] * Gmix[c, b] for a in range(4) for c in range(4))
div -= sum(Gam[c][a][b] * Gmix[a, c] for a in range(4) for c in range(4))
chk("C3 contracted Bianchi nabla_a G^a_r == 0 identically", sp.simplify(div) == 0)

# ---- C4 axial V2 ------------------------------------------------------------
u_, pr_, pz_, pp_ = sp.symbols('u p_r p_z p_phi', real=True)
T = -u_ + pr_ + pz_ + pp_
chk("C4 8 pi (p_z - T/2) == 4 pi (u - p_r - p_phi + p_z)",
    sp.simplify(8 * sp.pi * (pz_ - T / 2) - 4 * sp.pi * (u_ - pr_ - pp_ + pz_)) == 0)

# ---- C5 null contraction, Lambda drops out ----------------------------------
b_ = sp.Function('b')(r)
gmt = sp.diag(-sp.exp(2 * Phi), 1 / (1 - b_ / r), r**2, r**2 * sp.sin(th)**2)
Rm, gim, _ = ricci(gmt, X)
Rscm = sp.simplify(sum(gim[a, c] * Rm[a, c] for a in range(4) for c in range(4)))
Gm = sp.simplify(Rm - Rscm * gmt / 2)
k = sp.Matrix([sp.exp(-Phi), sp.sqrt(1 - b_ / r), 0, 0])
gkk = sp.simplify((k.T * gmt * k)[0])
Rkk = sp.simplify((k.T * Rm * k)[0])
Gkk = sp.simplify((k.T * Gm * k)[0])
L = sp.symbols('Lambda')
chk("C5 k is null (g_kk = 0)", gkk == 0)
chk("C5 G_kk == R_kk for null k (so R_kk = 8 pi T_kk)", sp.simplify(Gkk - Rkk) == 0)
chk("C5 Lambda g_kk == 0: T_kk is the same with or without Lambda", sp.simplify(L * gkk) == 0)

# ---- C6 Raychaudhuri -> Jacobi, q = R_kk/2 -----------------------------------
lam = sp.symbols('lambda')
J = sp.Function('J')(lam)
Rkk_s = sp.symbols('R_kk')
theta = 2 * sp.diff(J, lam) / J
ray = sp.diff(theta, lam) + theta**2 / 2 + Rkk_s      # = 0 for shear-free twist-free
chk("C6 theta' + theta^2/2 + R_kk == 2 (J'' + (R_kk/2) J)/J",
    sp.simplify(ray - 2 * (sp.diff(J, lam, 2) + Rkk_s / 2 * J) / J) == 0)
Gc, c = sp.symbols('G c', positive=True)
Tkk = sp.symbols('T_kk')
q = sp.Rational(1, 2) * (8 * sp.pi * Gc / c**4) * Tkk
chk("C6 q = R_kk/2 = (4 pi G/c^4) T_kk", sp.simplify(q - 4 * sp.pi * Gc / c**4 * Tkk) == 0)
ll, mm = sp.symbols('l m', positive=True)
sl = sp.sin(sp.sqrt(mm) * lam)       # J(0) = 0 solution of J'' + m J = 0
chk("C6 J = sin(sqrt(m) lambda) solves J'' + m J = 0",
    sp.simplify(sp.diff(sl, lam, 2) + mm * sl) == 0)
chk("C6 first conjugate zero at sqrt(m) l = pi  (m l^2 = pi^2)",
    sp.simplify(sl.subs(lam, sp.pi / sp.sqrt(mm))) == 0)

# ---- C7 T_COEFF -------------------------------------------------------------
C_SI = 299792458.0
G_2018 = 6.67430e-11         # CODATA 2018
G_2022 = 6.67430e-11         # CODATA 2022 (arXiv:2409.03787 Table XXXII: identical to 2018)
uG = 0.00015e-11
coeff = 3.141592653589793 * C_SI**4 / (4 * G_2022)
print("     T_COEFF = pi c^4/(4G) = %.6e Pa m^2 ; rel. unc. from G = %.1e" % (coeff, uG / G_2022))
chk("C7 T_COEFF matches seatindex selftest 9.50536e43 within 1e39", abs(coeff - 9.50536e43) < 1e39)
chk("C7 CODATA 2018 -> 2022 move in G is zero", G_2018 == G_2022)

# ---- C8 Lambda ---------------------------------------------------------------
LL = sp.symbols('Lambda', positive=True)
gds = sp.diag(-(1 - LL * r**2 / 3), 1 / (1 - LL * r**2 / 3), r**2, r**2 * sp.sin(th)**2)
Rd, gid, _ = ricci(gds, X)
Rscd = sp.simplify(sum(gid[a, c] * Rd[a, c] for a in range(4) for c in range(4)))
Gd = sp.simplify(Rd - Rscd * gds / 2)
chk("C8a de Sitter solves G + Lambda g = 0 (T^matter = 0: traceless, static, regular)",
    sp.simplify(Gd + LL * gds) == sp.zeros(4, 4))
chk("C8a ...and is not Minkowski (Ricci scalar 4 Lambda != 0)", sp.simplify(Rscd - 4 * LL) == 0)
TL = -LL * gds / (8 * sp.pi)                              # Lambda absorbed into T
trTL = sp.simplify(sum(gid[a, c] * TL[a, c] for a in range(4) for c in range(4)))
chk("C8a with Lambda absorbed, trace T = -Lambda/2pi != 0 (excluded by 'traceless')",
    sp.simplify(trTL + LL / (2 * sp.pi)) == 0)
# C8b Misner-Sharp with Lambda
solL = sp.solve(sp.Eq(Gmix[0, 0] + LL, 8 * sp.pi * (-rho)), sp.diff(m, r))
chk("C8b with Lambda: m' = 4 pi r^2 rho + Lambda r^2 / 2",
    sp.simplify(solL[0] - (4 * sp.pi * r**2 * rho + LL * r**2 / 2)) == 0)
# C8c magnitudes (numeric)
Mpc = 3.0856775814913673e22
H0 = 67.36e3 / Mpc
OmL = 0.6847
Lam = 3 * H0**2 * OmL / C_SI**2
rhoL_c2 = Lam * C_SI**4 / (8 * 3.141592653589793 * G_2022)
print("     Planck 2018: Lambda = %.4e m^-2, rho_Lambda c^2 = %.4e J/m^3" % (Lam, rhoL_c2))
chk("C8c Lambda in (1.0e-52, 1.2e-52) m^-2", 1.0e-52 < Lam < 1.2e-52)
for R_, M_, tag in ((1.0, 1.0, "1 m, 1 kg"), (6.371e6, 5.972e24, "Earth"),
                    (1.2e4, 2.8e30, "neutron star")):
    m_geom = G_2022 * M_ / C_SI**2
    dm = Lam * R_**3 / 6
    print("     %-13s  m = %.3e m ; Lambda r^3/6 = %.3e m ; ratio %.2e" % (tag, m_geom, dm, dm / m_geom))
l_eq = (coeff / rhoL_c2) ** 0.5
print("     seatindex threshold T_kk = %.3e/l^2 Pa equals rho_Lambda c^2 only at l = %.2e m"
      " -- and Lambda contributes 0 to T_kk anyway (C5)" % (coeff, l_eq))
chk("C8c Lambda r^3/6 < 1e-25 of m for a neutron star", Lam * 1.2e4**3 / 6 < 1e-25 * G_2022 * 2.8e30 / C_SI**2)

# ---- C9 foliation V7 --------------------------------------------------------
tau, Rr, M, E = sp.symbols('tau R M E', positive=True)
Y = [tau, Rr, th, ph]
s = sp.sqrt(2 * M / Rr + 2 * E)
gf = sp.zeros(4, 4)
# ds^2 = -dtau^2 + (dR + s dtau)^2/(1+2E) + R^2 dOmega^2
gf[0, 0] = -1 + s**2 / (1 + 2 * E)
gf[0, 1] = gf[1, 0] = s / (1 + 2 * E)
gf[1, 1] = 1 / (1 + 2 * E)
gf[2, 2] = Rr**2
gf[3, 3] = Rr**2 * sp.sin(th)**2
Rf, _, _ = ricci(gf, Y)
chk("C9 foliation.py:184 metric is Ricci-flat (vacuum under G = 8 pi T, Lambda = 0)",
    sp.simplify(Rf) == sp.zeros(4, 4))

# ---- C10 certify convention -------------------------------------------------
import random
random.seed(67)
agree = True
for _ in range(2000):
    Tm = [random.uniform(-1, 1) for _ in range(4)]      # diag T in an orthonormal frame
    nec = all(Tm[0] + Tm[i] >= 0 for i in (1, 2, 3))
    nec8 = all(8 * 3.141592653589793 * (Tm[0] + Tm[i]) >= 0 for i in (1, 2, 3))
    agree &= (nec == nec8)
chk("C10 NEC sign verdict invariant under the factor 8 pi (2000 random diag T)", agree)

print("\n%d/%d checks pass" % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
