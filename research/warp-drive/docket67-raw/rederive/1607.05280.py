"""DOCKET 67 -- re-derivation checks for Abdolrahimi-Page-Tzounis, arXiv:1607.05280v4 (PRD 100, 124038).

Everything checked is a closed form printed on a page that was READ (pp. 1-3, 6, 8, 9, 16, 17, 21).
Pages 4-5, 7, 10-15, 18-20 were NOT read (alphaXiv quota exhausted this pass), so the metric
functions g(z), h(z), psi(v,z) of eqs (17)-(19), S(z)'s definition and the Bardeen fit
coefficients k_3..k_7 are NOT re-derived here.

Exit 0 iff every check passes.
"""
import math
import sys

import sympy as sp

fails = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    if not ok:
        fails.append(name)


a, u, v, r, z, mu, mu0, L, eps = sp.symbols("alpha u v r z mu mu0 L epsilon", positive=True)

# 1. eq (3) solves eq (2): mu(u) = (-3 alpha u)^(1/3), u < 0, gives mu' = -alpha/mu^2
un = sp.symbols("u_n", negative=True)
m_u = (-3 * a * un) ** sp.Rational(1, 3)
chk("eq(3) solves eq(2): dmu/du = -alpha/mu^2",
    sp.simplify(sp.diff(m_u, un) + a / m_u ** 2) == 0)

# 2. eq (4) -> eq (5): mu^3 = -3 alpha u with u = v - 2(r - 2mu) - 4 mu ln(r/2mu), r = 2mu/z
u_of = v - 2 * (r - 2 * mu) - 4 * mu * sp.log(r / (2 * mu))
lhs5 = sp.expand(-3 * a * u_of)
rhs5 = -3 * a * v + 12 * a * mu * (1 / z - sp.log(z) - 1)
diff5 = sp.simplify(sp.expand_log(lhs5.subs(r, 2 * mu / z) - rhs5, force=True))
chk("eq(4) -> eq(5) algebra, r = 2 mu/z", diff5 == 0, str(diff5))

# 3. eq (9) is the Cardano root of eq (5): mu^3 - 3 mu0^2 eps mu - mu0^3 = 0,
#    eps = 4 alpha/mu0^2 (1/z - ln z - 1)  [eq (8); the garbled PDF shows '(1/4 - eps^3)^(1/2)']
import mpmath
mpmath.mp.dps = 60
ok9 = True
worst = mpmath.mpf(0)
for e in ("0", "1e-6", "1e-3", "0.1", "0.3", "0.6", "0.62"):
    e = mpmath.mpf(e)
    if e ** 3 >= mpmath.mpf(1) / 4:
        continue
    s_ = mpmath.sqrt(mpmath.mpf(1) / 4 - e ** 3)
    root = mpmath.cbrt(mpmath.mpf(1) / 2 + s_) + mpmath.cbrt(mpmath.mpf(1) / 2 - s_)   # real cube roots
    res = root ** 3 - 3 * e * root - 1          # mu0 = 1
    worst = max(worst, abs(res))
    ok9 = ok9 and abs(res) < mpmath.mpf("1e-40")
worst = float(worst)
chk("eq(9) Cardano root solves mu^3 - 3 mu0^2 eps mu - mu0^3 = 0 (eps^3 < 1/4)", ok9,
    "max residual %.2e" % worst)
# and eq (5) is that cubic once eps is substituted
cub = sp.expand(mu ** 3 - (mu0 ** 3 + 12 * a * mu * (1 / z - sp.log(z) - 1)))
cub2 = sp.expand(mu ** 3 - 3 * mu0 ** 2 * (4 * a / mu0 ** 2 * (1 / z - sp.log(z) - 1)) * mu - mu0 ** 3)
chk("eq(5) with mu0^3 = -3 alpha v is the depressed cubic of eq(9)", sp.simplify(cub - cub2) == 0)
# the real-root condition eps^3 < 1/4 fails only at large r: z_min where eps = 4^(-1/3)
for m0 in (1.0, 1e3, 1e19):
    # eps ~ 4 alpha/(mu0^2 z) at small z
    zmin = 4 * 3.7474e-5 / (m0 ** 2 * 4 ** (-1 / 3))
    print("     mu0 = %.0e l_P: Cardano form (9) real only for z >~ %.2e (r <~ %.2e mu0)"
          % (m0, zmin, 2 / zmin))

# 4. eq (64) re-derived by a DIFFERENT route from APT's (they use the 01 Einstein component):
#    covariant conservation of a pure flux T^r_t on Schwarzschild, plus luminosity L = alpha/mu^2.
t, th, ph = sp.symbols("t theta phi")
M = sp.symbols("M", positive=True)
F = 1 - 2 * M / r
g = sp.diag(-F, 1 / F, r ** 2, r ** 2 * sp.sin(th) ** 2)
X = [t, r, th, ph]
ginv = g.inv()
Gam = [[[sp.simplify(sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                         for l in range(4)) / 2) for k in range(4)] for j in range(4)] for i in range(4)]
Cst = sp.symbols("C")
T = sp.zeros(4, 4)          # mixed T^mu_nu with only T^r_t = C/r^2 and T^t_r fixed by symmetry of T_{mu nu}
T[1, 0] = Cst / r ** 2
# T_{tr} = g_rr T^r_t ; T^t_r = g^tt T_{tr}
T[0, 1] = ginv[0, 0] * g[1, 1] * T[1, 0]
div = []
for nu in range(4):
    d = sum(sp.diff(T[m_, nu], X[m_]) for m_ in range(4))
    d += sum(Gam[m_][m_][l] * T[l, nu] for m_ in range(4) for l in range(4))
    d -= sum(Gam[l][m_][nu] * T[m_, l] for m_ in range(4) for l in range(4))
    div.append(sp.simplify(d))
chk("T^r_t = C/r^2 (and T^t_r by index symmetry) is covariantly conserved on Schwarzschild",
    all(x == 0 for x in div), str(div))
# orthonormal f = T^{0^1^} = e^0_t e^1_r T^{tr}, T^{tr} = g^{tt} T_t^... use T^{tr} = T^r_t g^{tt}
Ttr_up = T[1, 0] * ginv[0, 0]
f_on = sp.sqrt(F) * (1 / sp.sqrt(F)) * Ttr_up
# outgoing luminosity L: T^r_t = -L/(4 pi r^2)  (energy flux outward; T^r_t = -T^{r}{}_{t} sign conv.)
f_on = sp.simplify(f_on.subs(Cst, -L / (4 * sp.pi)))
f_z = sp.simplify((f_on * M ** 4).subs(r, 2 * M / z).subs(L, a / M ** 2))
chk("eq(64): f(z) = alpha z^2/(16 pi (1-z)) from conservation + L = alpha/mu^2",
    sp.simplify(f_z - a * z ** 2 / (16 * sp.pi * (1 - z))) == 0, str(f_z))

# 5. the alternative forms printed in (65), (66), (67) agree
hz, gz, hzz, gzz = sp.symbols("h_z g_z h_zz g_zz")
fz = a * z ** 2 / (16 * sp.pi * (1 - z))
rho1 = z ** 2 / (32 * sp.pi * (1 - z)) * (2 * a * (1 - 2 * z ** 2) - z ** 2 * (1 - z) * hz)
rho2 = fz * (1 - 2 * z ** 2) - z ** 4 * hz / (32 * sp.pi)
chk("eq(65) two printed forms agree", sp.simplify(rho1 - rho2) == 0)
P1 = z ** 2 / (32 * sp.pi * (1 - z)) * (2 * a * (1 - 8 * z + 6 * z ** 2) - 2 * z * (1 - z) ** 2 * gz + z ** 2 * (1 - z) * hz)
P2 = fz * (1 - 8 * z + 6 * z ** 2) - z ** 3 * (1 - z) * gz / (16 * sp.pi) + z ** 4 * hz / (32 * sp.pi)
chk("eq(66) two printed forms agree", sp.simplify(P1 - P2) == 0)
p1 = z ** 3 / (64 * sp.pi) * (16 * a + (2 - 5 * z) * gz - 2 * z * hz + 2 * z * (1 - z) * gzz - z ** 2 * hzz)
p2 = 4 * fz * z * (1 - z) + z ** 3 / (64 * sp.pi) * ((2 - 5 * z) * gz - 2 * z * hz + 2 * z * (1 - z) * gzz - z ** 2 * hzz)
chk("eq(67) two printed forms agree", sp.simplify(p1 - p2) == 0)
# eq (51) minus eq (49) consistency: rho - P = 2p - T  (from the printed decomposition)
p_, H_, G_, T_ = sp.symbols("p H G T")
rho49 = 2 * p_ + z ** 2 / (1 - z) * (H_ + G_) - T_ - sp.Symbol("f")
P51 = z ** 2 / (1 - z) * (H_ + G_) - sp.Symbol("f")
chk("eqs (49),(51),(52): trace -rho + P + 2p = T (conformal anomaly)",
    sp.simplify(-rho49 + P51 + 2 * p_ - T_) == 0)

# 6. Hawking-Ellis type criterion used for 'Type IV': 2x2 block of T^a_b complex iff (rho+P)^2 < 4 f^2
rr, PP, ff, lam = sp.symbols("rho P f lambda", real=True)
Tmix = sp.Matrix([[-rr, -ff], [ff, PP]])      # T^a_b = eta^{ac} T_cb, eta = diag(-1, 1)
disc = sp.discriminant(sp.expand((Tmix - lam * sp.eye(2)).det()), lam)
chk("type-IV discriminant = (rho+P)^2 - 4 f^2", sp.simplify(disc - ((rr + PP) ** 2 - 4 * ff ** 2)) == 0,
    str(sp.factor(disc)))

# 7. eq (70), spin 0: beta*xi with xi = 96, beta = 1/(2^13 3^2 5 pi^2), against the conformal-scalar
#    anomaly on a Ricci-flat background, <T> = (1/2880 pi^2) R_abcd R^abcd  [textbook coefficient,
#    Birrell-Davies -- NAMED-NOT-READ in this pass]; Kretschmann computed here from the metric.
Riem = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                e = sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
                e += sum(Gam[i][k][m_] * Gam[m_][j][l] - Gam[i][l][m_] * Gam[m_][j][k] for m_ in range(4))
                Riem[i, j, k, l] = sp.simplify(e)
K = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if Riem[i, j, k, l] == 0:
                    continue
                # R_{ijkl} R^{ijkl} for a diagonal metric
                K += (g[i, i] * Riem[i, j, k, l]) ** 2 * ginv[i, i] * ginv[j, j] * ginv[k, k] * ginv[l, l] * \
                    g[i, i] ** 0 * 1
# correct index placement: R_{ijkl} = g_ii R^i_{jkl}; R^{ijkl} = g^jj g^kk g^ll R^i_{jkl}
K = sp.simplify(sum((g[i, i] * Riem[i, j, k, l]) * (ginv[j, j] * ginv[k, k] * ginv[l, l] * Riem[i, j, k, l])
                    for i in range(4) for j in range(4) for k in range(4) for l in range(4)))
chk("Kretschmann of Schwarzschild = 48 M^2/r^6", sp.simplify(K - 48 * M ** 2 / r ** 6) == 0, str(K))
beta = sp.Rational(1, 2 ** 13 * 3 ** 2 * 5) / sp.pi ** 2
Tz = sp.simplify((K / (2880 * sp.pi ** 2) * M ** 4).subs(r, 2 * M / z))
chk("eq(70) spin 0: mu^4 <T> = beta*96*z^6", sp.simplify(Tz - beta * 96 * z ** 6) == 0, str(Tz))
ratios = {"1/2": sp.Rational(168, 96), "1": sp.Rational(-1248, 96), "3/2": sp.Rational(-5592, 96),
          "2": sp.Rational(20352, 96)}
print("     xi/96 ratios printed by APT (compare Christensen-Duff 1978 coefficients 7/4, -13, -233/4, 212;"
      " NAMED-NOT-READ):", {k: str(x) for k, x in ratios.items()})

# 8. The luminosity consistency printed after (64): L = 16 pi beta f0/mu^2 with f0 = alpha/(16 pi beta)
f0 = a / (16 * sp.pi * sp.Symbol("beta_"))
chk("f0 = alpha/(16 pi beta) => 16 pi beta f0 = alpha",
    sp.simplify(16 * sp.pi * sp.Symbol("beta_") * f0 - a) == 0)

# 9. Scope arithmetic.  APT eq (2) hypothesis: mu >> 1/m for ALL massive particles, and emission
#    'almost entirely into massless particles (photons and gravitons)'.
G_SI, C_SI, HB, KB, EV = 6.67430e-11, 299792458.0, 1.054571817e-34, 1.380649e-23, 1.602176634e-19
MP = math.sqrt(HB * C_SI / G_SI)                     # kg
MP_EV = MP * C_SI ** 2 / EV
def mu_planck(kg):
    return kg / MP
def TH_eV(kg):
    return HB * C_SI ** 3 / (8 * math.pi * G_SI * kg) / EV
def mass_for_T(eV):
    return HB * C_SI ** 3 / (8 * math.pi * G_SI * eV * EV)
m_e = 0.51099895e6 / MP_EV
print("     1/m_e in Planck units = %.3e ; mass with T_H = m_e c^2: %.3e kg" % (1 / m_e, mass_for_T(0.51099895e6)))
for mnu in (0.0086, 0.05):     # sqrt(dm2_sol) ~ 8.6 meV, sqrt(dm2_atm) ~ 50 meV (PDG-order values)
    print("     neutrino %.4f eV: T_H = m_nu at M = %.3e kg  (photon+graviton alpha needs M >> this,"
          " and needs the lightest nu massive)" % (mnu, mass_for_T(mnu)))
Msc = 1.126e9
print("     selfconsistent.py's 1.126e9 kg hole: mu = %.3e l_P, T_H = %.3e eV (%.2f GeV); mu*m_e = %.2e"
      % (mu_planck(Msc), TH_eV(Msc), TH_eV(Msc) / 1e9, mu_planck(Msc) * m_e))
chk("1.126e9 kg violates APT eq(2)'s hypothesis mu >> 1/m_e (mu*m_e << 1)", mu_planck(Msc) * m_e < 1e-3,
    "mu*m_e = %.2e" % (mu_planck(Msc) * m_e))
print("     first-order parameter alpha/mu0^2 at 1.126e9 kg: %.2e (perturbation itself is tiny)"
      % (3.7474e-5 / mu_planck(Msc) ** 2))

# 10. selfconsistent.py:79 quotes 'Type IV only for z < 0.044' for spin 1; APT p.16-17 give
#     0 < z < 0.04374 (fit [64]) OR 0 < z < 0.06151 (fit [65]).
chk("0.044 is 0.04374 rounded (fit [64] only; fit [65] gives 0.06151)", round(0.04374, 3) == 0.044)

print()
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
