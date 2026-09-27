#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Misner-Sharp mass function as certify.py uses it.

Reads nothing from the corpus or from research/; imports certify.py READ-ONLY only for
the seated potential phi() and enclosed_mass_from_grr() so the proxy it uses can be
compared with the invariant Misner-Sharp mass.

Checks (each prints PASS/FAIL, exit 1 on any FAIL):
 C1  metric -e^{2Phi}dt^2 + dr^2/(1-2m/r) + r^2 dOmega^2: the invariant MS mass
     E = (R/2)(1 - g^{ab} d_aR d_bR) with R = areal radius equals m(r).
 C2  Einstein tensor: G^t_t = -2 m'/r^2 exactly, so G = 8 pi T with rho = -T^t_t gives
     m' = 4 pi r^2 rho (any Phi, any anisotropic matter).  With a cosmological constant,
     m' = 4 pi r^2 rho + Lambda r^2 / 2 (rho then EXCLUDES vacuum energy).
 C3  z3: for r > 0 and 1 - 2m/r > 0, g_rr = 1/(1-2m/r) < 1  <=>  m < 0 (the THEOREM).
 C4  Reissner-Nordstrom: m = M - Q^2/2r obeys m' = 4 pi r^2 rho with rho = Q^2/(8 pi r^4)>0
     yet m < 0 for r < Q^2/2M: the COROLLARY needs a regular centre (certify.py:132-141).
 C5  Static hypothesis is load-bearing: open FRW dust on a comoving slice has
     E = (4 pi/3) rho R^3 > 0 while dl/dR = 1/cosh(chi) < 1 (contracted).
 C6  Hypothesis drift: enclosed_mass_from_grr(g, r) is the MS mass only when r is AREAL.
     (a) Schwarzschild in isotropic coords: true E = M; proxy != M.
     (b) certify's seated conformastatic metric (isotropic coordinate rho, areal
         R = rho e^{-Phi}): true E = (R/2) rho Phi' (2 - rho Phi'); compare signs with the
         proxy at certify's radii and beyond R_s.
     (c) a potential where proxy and true MS mass have opposite signs.
"""
import math
import sys

import sympy as sp
import z3

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import certify  # read-only import

FAIL = []


def chk(name, ok, detail=""):
    print("%-4s %s %s" % ("PASS" if ok else "FAIL", name, detail))
    if not ok:
        FAIL.append(name)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
Phi = sp.Function("Phi")(r)
m = sp.Function("m")(r)
X = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - 2 * m / r), r**2, r**2 * sp.sin(th) ** 2)
gi = g.inv()


def einstein_mixed(g, gi, X):
    n = 4
    Gam = [[[sp.simplify(sum(gi[l, s] * (sp.diff(g[s, a], X[b]) + sp.diff(g[s, b], X[a])
                                          - sp.diff(g[a, b], X[s])) for s in range(n)) / 2)
             for b in range(n)] for a in range(n)] for l in range(n)]
    Ric = sp.zeros(n)
    for a in range(n):
        for b in range(n):
            e = 0
            for l in range(n):
                e += sp.diff(Gam[l][a][b], X[l]) - sp.diff(Gam[l][a][l], X[b])
                for s in range(n):
                    e += Gam[l][l][s] * Gam[s][a][b] - Gam[l][b][s] * Gam[s][a][l]
            Ric[a, b] = sp.simplify(e)
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    G = Ric - Rs * g / 2
    return sp.simplify(gi * G), Rs


# C1 invariant MS mass
E = sp.simplify(r / 2 * (1 - gi[1, 1] * sp.diff(r, r) ** 2))
chk("C1 invariant MS mass equals m(r) in areal form", sp.simplify(E - m) == 0, "E=%s" % E)

# C2 tt Einstein equation
Gmix, Rs = einstein_mixed(g, gi, X)
Gtt = sp.simplify(Gmix[0, 0])
chk("C2 G^t_t = -2 m'/r^2", sp.simplify(Gtt + 2 * sp.diff(m, r) / r**2) == 0, "G^t_t=%s" % Gtt)
rho, Lam = sp.symbols("rho Lambda", real=True)
# G^t_t + Lambda delta^t_t = 8 pi T^t_t = -8 pi rho
sol = sp.solve(sp.Eq(Gtt + Lam, -8 * sp.pi * rho), sp.diff(m, r))[0]
chk("C2b with Lambda: m' = 4 pi r^2 rho + Lambda r^2/2",
    sp.simplify(sol - (4 * sp.pi * r**2 * rho + Lam * r**2 / 2)) == 0, "m'=%s" % sol)
chk("C2c G^t_t contains no Phi (the tt equation is Phi-free)", not Gtt.has(Phi))

# C3 z3 proof of the iff
rr, mm = z3.Reals("r m")
s = z3.Solver()
hyp = z3.And(rr > 0, 1 - 2 * mm / rr > 0)
grr = 1 / (1 - 2 * mm / rr)
s.add(hyp, z3.Not((grr < 1) == (mm < 0)))
res = s.check()
chk("C3 z3: under r>0, 1-2m/r>0: g_rr<1 <=> m<0 (negation UNSAT)", res == z3.unsat, str(res))
s2 = z3.Solver(); s2.add(hyp)
chk("C3b vacuity guard: hypotheses satisfiable", s2.check() == z3.sat)
# without 1-2m/r>0 (trapped side, g_rr<0 counts as 'shorter' numerically) the iff fails
s3 = z3.Solver(); s3.add(rr > 0, 1 - 2 * mm / rr < 0, z3.Not((grr < 1) == (mm < 0)))
chk("C3c the untrapped hypothesis is load-bearing for the literal code test g_rr<1",
    s3.check() == z3.sat, "counterexample exists when 1-2m/r<0")

# C4 RN
M, Q = sp.symbols("M Q", positive=True)
mRN = M - Q**2 / (2 * r)
rhoRN = Q**2 / (8 * sp.pi * r**4)
chk("C4 RN obeys m' = 4 pi r^2 rho", sp.simplify(sp.diff(mRN, r) - 4 * sp.pi * r**2 * rhoRN) == 0)
val = mRN.subs({M: 1, Q: 1, r: sp.Rational(1, 4)})
chk("C4b RN m(r=1/4; M=Q=1) < 0 with rho > 0 (corollary needs m(0)=0)", val < 0, "m=%s" % val)

# C5 open FRW dust, comoving slice: MS original (Hayward eq.27) 1-2E/R = e^{-lam} R'^2 - Rdot^2
a, adot, chi, rh = sp.symbols("a adot chi rho_d", positive=True)
Rar = a * sp.sinh(chi)
Rp = a * sp.cosh(chi)          # dR/dchi on the slice
Rdot = adot * sp.sinh(chi)
lam_e = a**2                   # g_chichi
adot2 = 8 * sp.pi * rh * a**2 / 3 + 1   # open Friedmann
Efrw = sp.simplify((Rar / 2) * (1 - (Rp**2 / lam_e - Rdot**2)).subs(adot, sp.sqrt(adot2)))
chk("C5 open FRW: E = (4 pi/3) rho R^3 > 0", sp.simplify(Efrw - sp.Rational(4, 3) * sp.pi * rh * Rar**3) == 0,
    "E=%s" % Efrw)
dl_dR = sp.simplify(sp.sqrt(lam_e) / Rp)
chk("C5b open FRW comoving slice: dl/dR = 1/cosh(chi) < 1 (contracted with E>0)",
    sp.simplify(dl_dR - 1 / sp.cosh(chi)) == 0, "dl/dR=%s" % dl_dR)

# C6 hypothesis drift: proxy on non-areal coordinate
rho_i = sp.symbols("rho_i", positive=True)
u = M / (2 * rho_i)
B = (1 + u) ** 4
Rarea = rho_i * sp.sqrt(B)
Etrue = sp.simplify(Rarea / 2 * (1 - (1 / B) * sp.diff(Rarea, rho_i) ** 2))
chk("C6a Schwarzschild isotropic: invariant MS mass = M", sp.simplify(Etrue - M) == 0, "E=%s" % Etrue)
proxy = float((rho_i / 2 * (1 - 1 / B)).subs({M: 1, rho_i: 2}))
chk("C6a' proxy (rho/2)(1-1/g_rhorho) at M=1, rho=2 is NOT M", abs(proxy - 1) > 1e-3,
    "proxy=%.6f vs M=1" % proxy)

# (b) seated metric
Pf, Pp = sp.symbols("P Pp", real=True)
# general conformastatic: R = rho e^{-P}, g^{rhorho} = e^{2P}; E = (R/2)(1 - e^{2P} R'^2)
Pfun = sp.Function("P")(rho_i)
Rc = rho_i * sp.exp(-Pfun)
Ec = sp.simplify(Rc / 2 * (1 - sp.exp(2 * Pfun) * sp.diff(Rc, rho_i) ** 2))
target = Rc / 2 * rho_i * sp.diff(Pfun, rho_i) * (2 - rho_i * sp.diff(Pfun, rho_i))
chk("C6b conformastatic MS mass = (R/2) rho P'(2 - rho P')", sp.simplify(Ec - target) == 0)


def dphi(x, m=certify.M_SEATED, a=certify.A_CORE, Rs=certify.R_SHELL):
    """Analytic Phi'(rho) of certify.phi (finite differences cancel beyond R_s)."""
    d = -m * x / (x * x + a * a) ** 1.5
    if x > Rs:
        d += m / (x * x)
    return d


rows = []
disagree_sampled = 0
for x in (0.005, 0.05, 1.0, 10.0, 100.0, 199.0, 201.0, 300.0, 1000.0):
    P = certify.phi(x); Pd = dphi(x)
    R = x * math.exp(-P)
    Et = R / 2 * x * Pd * (2 - x * Pd)
    Ep = certify.enclosed_mass_from_grr(math.exp(-2 * P), x)
    rows.append((x, P, Et, Ep))
    print("     rho=%-7g Phi=%+.3e  true E=%+.4e  proxy=%+.4e  signs %s"
          % (x, P, Et, Ep, "agree" if (Et < 0) == (Ep < 0) else "DISAGREE"))
    if x <= 100 and (Et < 0) != (Ep < 0):
        disagree_sampled += 1
chk("C6b' at certify's sampled radii the true MS mass is negative (conclusion survives)",
    all(Et < 0 for (x, P, Et, Ep) in rows if x <= 100) and disagree_sampled == 0)
ratio = [Et / Ep for (x, P, Et, Ep) in rows if x <= 100]
print("     true/proxy magnitude ratios at sampled radii:", ["%.3g" % q for q in ratio])
chk("C6b'' outside R_s both true E and proxy are POSITIVE (docstring 'everywhere' is loose)",
    all(Et > 0 and Ep > 0 for (x, P, Et, Ep) in rows if x > 200))

# (c) a potential where they disagree: Phi = m/sqrt(rho^2+a^2) - C, C large => Phi<0, Phi'<0
mm_, aa, C, x = 0.02, 0.02, 1.0, 1.0
P = mm_ / math.sqrt(x * x + aa * aa) - C
Pd = -mm_ * x / (x * x + aa * aa) ** 1.5
R = x * math.exp(-P)
Et = R / 2 * x * Pd * (2 - x * Pd)
Ep = certify.enclosed_mass_from_grr(math.exp(-2 * P), x)
chk("C6c non-areal proxy can carry the WRONG SIGN (shown: proxy>0, true<0)",
    Ep > 0 and Et < 0, "proxy=%+.4e true=%+.4e" % (Ep, Et))
# and the true contraction criterion agrees with the true mass (theorem is fine in areal form)
dl_dR = 1 / abs(1 - x * Pd)
chk("C6c' true contraction dl/dR<1 agrees with true E<0 (theorem intact, proxy is not)",
    (dl_dR < 1) == (Et < 0), "dl/dR=%.6f" % dl_dR)

print("\nRESULT:", "ALL PASS" if not FAIL else "FAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
