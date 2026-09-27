#!/usr/bin/env python3
"""DOCKET 67 -- magnetic-energy-density.  Re-derivation / machine check.

Checks, in order:
 (A) sympy: Hilbert stress tensor of the SI Maxwell action, obtained by
     differentiating sqrt(-g) L w.r.t. the inverse metric, gives
     T_00 = (eps0 E^2 + B^2/mu0)/2, so for E = 0, u = B^2/(2 mu0).
 (B) sympy: for E = 0 and a null vector k = (1, n), T_kk = (B^2/mu0) sin^2(theta)
     = 2 u sin^2(theta), theta the angle between n and B.  T_kk ranges over
     [0, 2u]; it equals u only at sin^2 = 1/2.
 (C) numerics: spec.py's numbers with MU0 CODATA-2018 (the tree's) and
     CODATA-2022; WITHDRAWN 2 and the B*l invariant redone with T_kk in {u, 2u, 0}.
 (D) mpmath: one-loop Euler-Heisenberg correction to the pure-magnetic energy
     density u = -L_eff(B), at 1e11 T (b = B/B_c ~ 22.7) and at the far field.
Exit 0 if every assertion holds.
"""
import math
import sympy as sp
import mpmath as mp

ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))


# ---------------------------------------------------------------- (A)
print("(A) Hilbert stress tensor of S = INT sqrt(-g) (-1/(4 mu0)) F_ab F^ab")
mu0, eps0, c = sp.symbols("mu0 epsilon0 c", positive=True)
E = sp.symbols("E1:4", real=True)
B = sp.symbols("B1:4", real=True)
eta = sp.diag(-1, 1, 1, 1)                     # x^0 = c t
# F_{0i} = -E_i/c (so F^{0i} = E_i/c), F_{ij} = eps_{ijk} B_k
F = sp.zeros(4, 4)
for i in range(3):
    F[0, i + 1] = -E[i] / c
    F[i + 1, 0] = E[i] / c
lc = sp.LeviCivita
for i in range(3):
    for j in range(3):
        F[i + 1, j + 1] = sum(lc(i, j, k) * B[k] for k in range(3))
d = sp.symbols("d0:10")
idx = [(a, b) for a in range(4) for b in range(a, 4)]
ginv = sp.Matrix(eta)
for s, (a, b) in zip(d, idx):
    ginv[a, b] += s
    if a != b:
        ginv[b, a] += s
sqrtg = 1 / sp.sqrt(-ginv.det())               # sqrt(-det g) = 1/sqrt(-det g^-1)
F2 = sum(F[a, b] * F[cc, dd] * ginv[a, cc] * ginv[b, dd]
         for a in range(4) for b in range(4) for cc in range(4) for dd in range(4))
dens = sqrtg * (-F2 / (4 * mu0))
at0 = {s: 0 for s in d}
T = sp.zeros(4, 4)
for s, (a, b) in zip(d, idx):
    der = sp.diff(dens, s).subs(at0)
    if a != b:
        der = der / 2                          # s multiplies both g^ab and g^ba
    T[a, b] = T[b, a] = sp.simplify(-2 * der)  # sqrt(-g)=1 at eta
T00 = sp.simplify(T[0, 0].subs(mu0, 1 / (eps0 * c ** 2)))
E2 = sum(e ** 2 for e in E)
B2 = sum(b ** 2 for b in B)
want = sp.simplify((eps0 * E2 + B2 / (mu0)).subs(mu0, 1 / (eps0 * c ** 2)) / 2)
check("T_00 == (eps0 E^2 + B^2/mu0)/2   [sympy, from the action]",
      sp.simplify(T00 - want) == 0)
u_mag = sp.simplify(T[0, 0].subs({e: 0 for e in E}))
check("E = 0  =>  T_00 == B^2/(2 mu0)   [spec.py:178-179 energy_density]",
      sp.simplify(u_mag - B2 / (2 * mu0)) == 0)
trace = sp.simplify(sum(eta[a, a] * T[a, a] for a in range(4)))
check("trace T^a_a == 0 (conformal, so no mass term hidden)", trace == 0)

# ---------------------------------------------------------------- (B)
print("\n(B) T_kk for a pure magnetic field and null k = (1, n)")
th, ph = sp.symbols("theta phi", real=True)
Bm = sp.symbols("B", positive=True)
Bvec = (0, 0, Bm)
n = (sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th))
k = (1,) + n
sub = {E[i]: 0 for i in range(3)}
sub.update({B[i]: Bvec[i] for i in range(3)})
Tkk = sp.simplify(sum(T[a, b].subs(sub) * k[a] * k[b] for a in range(4) for b in range(4)))
uB = Bm ** 2 / (2 * mu0)
check("T_kk == (B^2/mu0) sin^2(theta) == 2 u sin^2(theta)",
      sp.simplify(Tkk - 2 * uB * sp.sin(th) ** 2) == 0)
check("T_kk == u only where sin^2(theta) == 1/2 (not an identity)",
      sp.simplify(Tkk - uB) != 0)
print("     T_kk / u  in [0, 2]:  0 along B, 2 across B")

# ---------------------------------------------------------------- (C)
print("\n(C) the tree's numbers")
MU0_2018 = 1.25663706212e-6      # spec.py:135 == CODATA 2018 (scipy _codata.py txt2018)
MU0_2022 = 1.25663706127e-6      # CODATA 2022 (scipy 1.17.1 _codata.py txt2022)
G, C = 6.67430e-11, 299792458.0
T_COEFF = math.pi * C ** 4 / (4 * G)
u11_18 = 1e22 / (2 * MU0_2018)
u11_22 = 1e22 / (2 * MU0_2022)
print("     u(1e11 T) 2018 mu0 = %.9e Pa ; 2022 mu0 = %.9e Pa ; rel move %.2e"
      % (u11_18, u11_22, u11_22 / u11_18 - 1))
check("mu0 2018->2022 moves u by < 1e-9 relative", abs(u11_22 / u11_18 - 1) < 1e-9)
tkk_req = T_COEFF / 1.5456e8 ** 2
print("     tkk_required(1.5456e8) = %.6e ; energy_density(1e11) = %.6e ; ratio-1 = %.2e"
      % (tkk_req, u11_18, tkk_req / u11_18 - 1))
inv_u = math.sqrt(2 * MU0_2018 * T_COEFF)      # tree: T_kk := u
inv_2u = math.sqrt(MU0_2018 * T_COEFF)         # T_kk = 2u (B across the path)
print("     B*l invariant with T_kk=u : %.5e T m (tree, spec.py:156)" % inv_u)
print("     B*l invariant with T_kk=2u: %.5e T m (factor 1/sqrt2)" % inv_2u)
check("tree invariant reproduces 1.54562e19", abs(inv_u / 1.54562e19 - 1) < 1e-4)
Bfar = 1e11 * (1e4 / 1.5456e8) ** 3
ufar = Bfar ** 2 / (2 * MU0_2018)
for tag, fac in (("T_kk=u (tree)", 1.0), ("T_kk=2u (equatorial, B across path)", 2.0)):
    r = fac * ufar / tkk_req
    print("     WITHDRAWN 2, %-38s ratio %.3e  (%.2f orders short)" % (tag, r, -math.log10(r)))
    check("  still short by > 20 orders under %s" % tag, r < 1e-20)
print("     WITHDRAWN 2, T_kk=0 (polar, B along path): ratio 0 -- shorter still")
# collapse ratio if the matter were pure magnetic field with T_kk = 2u:
print("     (context) seat/collapse with T_kk = 2u instead of u: %.4f (tree 2pi^2/3 = %.4f); >1 either way"
      % (math.pi ** 2 / 3, 2 * math.pi ** 2 / 3))

# ---------------------------------------------------------------- (D)
print("\n(D) one-loop Euler-Heisenberg: u = -L_eff(B) for E = 0")
me, e, hbar = 9.1093837139e-31, 1.602176634e-19, 1.054571817e-34
alpha = 7.2973525643e-3
Bc = me ** 2 * C ** 2 / (e * hbar)
print("     B_c = m_e^2 c^2/(e hbar) = %.4e T" % Bc)
mp.mp.dps = 30


def I(b):
    """INT_0^inf dt/t^3 e^-t [bt coth(bt) - 1 - (bt)^2/3]  (negative)."""
    def f(t):
        x = b * t
        if x < mp.mpf("1e-3"):
            br = -x ** 4 / 45 + 2 * x ** 6 / 945
        else:
            br = x * mp.coth(x) - 1 - x ** 2 / 3
        return mp.e ** (-t) * br / t ** 3
    return mp.quad(f, [0, 1 / max(b, 1), 1, 10, mp.inf])


def du_over_u(b):
    # L1 = -(m^4/8pi^2) I(b); u0 = B^2/2 = b^2 m^4/(8 pi alpha)  (HL, hbar=c=1)
    # u = u0 - L1  =>  du/u0 = (alpha/pi) I(b)/b^2
    return alpha / math.pi * float(I(b)) / b ** 2


bw = 1e-2
check("weak-field limit reproduces -(alpha/45 pi) b^2 (Heisenberg-Euler 1936 coefficient)",
      abs(du_over_u(bw) / (-alpha * bw ** 2 / (45 * math.pi)) - 1) < 1e-3)
b11 = 1e11 / Bc
r11 = du_over_u(b11)
print("     b = %.3f at 1e11 T : du/u = %.4e  (leading-log -(alpha/3pi) ln b = %.4e)"
      % (b11, r11, -alpha / (3 * math.pi) * math.log(b11)))
check("|du/u| at 1e11 T below 1% (one loop)", abs(r11) < 1e-2)
check("|du/u| at 1e11 T exceeds the spec.py consistency tolerance 1e-3 is %s"
      % (abs(r11) > 1e-3), True)
bfar = Bfar / Bc
rfar = -alpha * bfar ** 2 / (45 * math.pi)
print("     far field %.3e T (b = %.2e): du/u = %.2e" % (Bfar, bfar, rfar))
check("far-field correction negligible (< 1e-20)", abs(rfar) < 1e-20)

print("\nRESULT:", "ALL CHECKS OK" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
