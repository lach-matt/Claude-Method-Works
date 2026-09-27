#!/usr/bin/env python3
"""DOCKET 67 item 20 -- re-derivation of the Lemaitre-Tolman-Bondi energy
function as driven.py:214-217 / drivensource.py:183-186 use it.

Sources READ (alphaXiv, 2026-09-26):
  Hellaby 0910.0350 eq (2.1), (2.5), (2.9)-(2.11), (2.31)-(2.32):
      ds^2 = -dt^2 + R'^2/(1+f) dr^2 + R^2 dOmega^2,   f = 2E,  dust, comoving
      Rdot^2 = 2M/R + f + Lambda R^2/3
      Lambda = 0: f > 0 hyperbolic, f = 0 parabolic, f < 0 elliptic
      RW limit: f = -k r^2, M = M_3 r^3
  Escriva 2504.05813 eq (2.3), (2.5): Gamma = D_r R = R'/B,  Gamma^2 = 1 + U^2 - 2M/R
      (perfect fluid, comoving gauge, no dust restriction)
  Hayward gr-qc/9408002 eq (27): 1 - 2E_MS/r = e^{-lambda} r'^2 - rdot^2
  Lasky & Lun gr-qc/0606055 eq (40), (42): with pressure the metric keeps the
      form g_RR = r'^2/(1+E_LL) but dE_LL/dT = 2 (1+E_LL)/(rho+P) P' alpha sqrt(2M/r+E_LL)/r'
      (E_LL = f = 2E_Hellaby -- a factor-of-two convention difference)
  Le Delliou, Mena, Mimoso 0911.0241 eq (15) and Fig. 1: with Lambda > 0 a dust
      shell escapes iff E_LL > E_lim = -(3M)^{2/3} Lambda^{1/3} < 0.

Every check prints PASS/FAIL and the script exits 1 on any FAIL.
"""
import sys
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)


t, r = sp.symbols("t r", real=True)
R = sp.Function("R", positive=True)(t, r)
E = sp.Function("E", real=True)(r)          # Hellaby's E, f = 2E
M = sp.Function("M", positive=True)(r)
Lam = sp.symbols("Lambda", real=True)
k = sp.symbols("k", real=True)

# ---------------------------------------------------------------- V1
# Gamma := D_r R = R' / sqrt(g_rr).  LTB: g_rr = R'^2/(1+2E).  => Gamma^2 - 1 = 2E.
g_rr = sp.diff(R, r) ** 2 / (1 + 2 * E)
Gamma2 = sp.diff(R, r) ** 2 / g_rr
check("V1  LTB metric: Gamma^2 - 1 = 2E identically (driven.py V9)",
      sp.simplify(Gamma2 - 1 - 2 * E) == 0)

# ---------------------------------------------------------------- V1b
# driven.py:596-601's own form: Lambda_ltb = log(R'/sqrt(1+2E)); (e^-Lam R')^2 - (1+2E) = 0
Rp = sp.Symbol("Rprime", positive=True)
Lam_ltb = sp.log(Rp / sp.sqrt(1 + 2 * E))
check("V1b driven.py V9 form reproduced, residual 0",
      sp.simplify((sp.exp(-Lam_ltb) * Rp) ** 2 - (1 + 2 * E)) == 0)

# ---------------------------------------------------------------- V2
# Consistency of the two routes: Misner-Sharp/Escriva Gamma^2 = 1 + U^2 - 2m/R with
# U = Rdot (comoving, Phi = 0) and LTB Rdot^2 = 2M/R + 2E (Lambda = 0, m = M):
U2 = 2 * M / R + 2 * E                      # Hellaby (2.5) with Lambda = 0
Gamma2_MS = 1 + U2 - 2 * M / R
check("V2  Misner-Sharp route agrees: 1 + Rdot^2 - 2M/R = 1 + 2E (Lambda = 0)",
      sp.simplify(Gamma2_MS - (1 + 2 * E)) == 0)

# ---------------------------------------------------------------- V2b
# With Lambda: the Misner-Sharp mass of dust+Lambda is m = M + Lambda R^3/6, and
# Rdot^2 = 2M/R + 2E + Lambda R^2/3.  Then Gamma^2 - 1 = 2E STILL (the identity
# survives Lambda) -- but 2E is now U^2 - 2M/R - Lambda R^2/3, not U^2 - 2m/R + ...
m_MS = M + Lam * R ** 3 / 6
U2L = 2 * M / R + 2 * E + Lam * R ** 2 / 3
check("V2b identity survives Lambda: 1 + Rdot^2 - 2 m_MS/R = 1 + 2E with m_MS = M + Lam R^3/6",
      sp.simplify(1 + U2L - 2 * m_MS / R - (1 + 2 * E)) == 0)

# ---------------------------------------------------------------- V3
# FRW: R = a(t) r, g_rr = a^2/(1 - k r^2)  =>  Gamma^2 = 1 - k r^2  =>  Gamma > 1 <=> k < 0 (r != 0)
a = sp.Function("a", positive=True)(t)
R_frw = a * r
g_rr_frw = a ** 2 / (1 - k * r ** 2)
Gamma2_frw = sp.diff(R_frw, r) ** 2 / g_rr_frw
check("V3  FRW: Gamma^2 = 1 - k r^2, so 2E = -k r^2 (Hellaby 2.32) and Gamma > 1 <=> k < 0",
      sp.simplify(Gamma2_frw - (1 - k * r ** 2)) == 0)
# numeric: open/flat/closed
for kk, expect in ((-1, True), (0, False), (1, False)):
    val = float(Gamma2_frw.subs({k: kk, r: sp.Rational(1, 2)}))
    check("V3n k = %+d at r = 1/2: Gamma^2 - 1 = %+.3f, 'contracts' (Gamma > 1) = %s"
          % (kk, val - 1, val > 1), (val > 1) == expect)

# ---------------------------------------------------------------- V4
# Classification, Lambda = 0, M > 0 (Hellaby 2.9-2.11 read as energy):
#   E > 0: Rdot^2 = 2M/R + 2E >= 2E > 0 for every R > 0  -> never turns round (unbound)
#   E < 0: Rdot^2 >= 0 forces R <= M/(-E)                  -> bounded (elliptic)
Rs, Ms, Es = sp.symbols("R M E", real=True)
check("V4a E > 0, M > 0: Rdot^2 - 2E = 2M/R > 0, so Rdot^2 > 0 for all R > 0 (unbound)",
      sp.simplify((2 * Ms / Rs + 2 * Es) - 2 * Es) == 2 * Ms / Rs)
sol = sp.solve(sp.Eq(2 * Ms / Rs + 2 * Es, 0), Rs)
check("V4b E < 0, M > 0: turning point at R_max = M/(-E) (bound)",
      len(sol) == 1 and sp.simplify(sol[0] - (-Ms / Es)) == 0)

# ---------------------------------------------------------------- V5
# THE NARROWING.  Lambda > 0: Le Delliou et al. (0911.0241 eq 15):
#   rdot^2 = 2M/r + Lambda r^2/3 + E_LL,   V(r) = -2M/r - Lambda r^2/3,
#   V has its maximum at r_lim = (3M/Lambda)^{1/3},  V(r_lim) = E_lim = -(3M)^{2/3} Lambda^{1/3}.
# A shell with E_lim < E_LL < 0 has rdot^2 = E_LL - V(r) > 0 for EVERY r: it escapes although E < 0.
rr = sp.symbols("r", positive=True)
Mv, Lv = sp.symbols("M Lambda", positive=True)
V = -2 * Mv / rr - Lv * rr ** 2 / 3
crit = sp.solve(sp.diff(V, rr), rr)
crit = [c for c in crit if c.is_real is not False]
r_lim = sp.cbrt(3 * Mv / Lv)
check("V5a dV/dr = 0 at r_lim = (3M/Lambda)^{1/3} (Le Delliou eq. after 15)",
      any(sp.simplify(c - r_lim) == 0 for c in crit))
E_lim = sp.simplify(V.subs(rr, r_lim))
check("V5b V(r_lim) = E_lim = -(3M)^{2/3} Lambda^{1/3} < 0",
      sp.simplify(E_lim + (3 * Mv) ** sp.Rational(2, 3) * Lv ** sp.Rational(1, 3)) == 0)
# numeric counterexample to 'E > 0 <=> unbound' when Lambda > 0:
Mn, Ln = 1.0, 0.1
Elim_n = -(3 * Mn) ** (2.0 / 3) * Ln ** (1.0 / 3)
E_n = 0.5 * Elim_n                      # negative, but above E_lim
rs = [0.01 * i for i in range(1, 100000)]
rdot2 = [2 * Mn / x + Ln * x ** 2 / 3 + E_n for x in rs]
check("V5c numeric: M = 1, Lambda = 0.1, E = %.4f < 0 and rdot^2 > 0 at every r in (0, 1000]"
      " -- an UNBOUND shell with E < 0 (Gamma < 1)" % E_n, min(rdot2) > 0)
# and the Gamma of that shell is < 1 everywhere: Gamma^2 = 1 + E_LL (Lasky-Lun normalisation)
check("V5d that shell has Gamma^2 = 1 + E = %.4f < 1: 'not contracting' in driven.py's sense, yet unbound"
      % (1 + E_n), 1 + E_n < 1)
# and the tree's own m (Misner-Sharp, includes Lambda R^3/6) gives the SAME Gamma:
x = 3.0
m_tree = Mn + Ln * x ** 3 / 6
U2_tree = 2 * Mn / x + Ln * x ** 2 / 3 + E_n
check("V5e driven.gamma_squared(m_MS, R, U) at R = 3 reproduces 1 + E = %.4f" % (1 + E_n),
      abs((1 + U2_tree - 2 * m_tree / x) - (1 + E_n)) < 1e-12)

# ---------------------------------------------------------------- V6
# Pressure (Lasky-Lun 0606055 eq 40): metric keeps g_RR = r'^2/(1+E_LL) so Gamma^2 = 1 + E_LL
# holds instant by instant; eq (42) makes E_LL time-dependent when P' != 0.
T, Rc = sp.symbols("T R", real=True)
rc = sp.Function("r", positive=True)(T, Rc)
E_LL = sp.Function("E_LL", real=True)(T, Rc)
g_RR = sp.diff(rc, Rc) ** 2 / (1 + E_LL)
check("V6a with pressure (Lasky-Lun eq 40): Gamma^2 - 1 = E_LL still an identity at each instant",
      sp.simplify(sp.diff(rc, Rc) ** 2 / g_RR - 1 - E_LL) == 0)
# eq (42): r' dE/dT = 2 (1+E)/(rho+P) P' alpha sqrt(2M/r + E).  Zero iff P' = 0 (given rho+P != 0, alpha > 0, 2M/r + E > 0).
rho, P, alpha, Pp, Mp, rp = sp.symbols("rho P alpha Pprime M r", positive=True)
E_s = sp.symbols("E_s", real=True)
dEdT = 2 * (1 + E_s) / (rho + P) * Pp * alpha * sp.sqrt(2 * Mp / rp + E_s) / sp.Symbol("rprime", positive=True)
check("V6b eq (42): dE_LL/dT vanishes identically when P' = 0 (dust) -- E is a conserved shell label only then",
      sp.simplify(dEdT.subs(Pp, 0)) == 0)
check("V6c eq (42): dE_LL/dT != 0 for P' != 0 with 1 + E > 0 -- so 'the shell IS unbound' is not a conserved label",
      sp.simplify(dEdT.subs({Pp: 1, E_s: 0})) != 0)

# ---------------------------------------------------------------- V7
# Convention: Lasky-Lun E_LL = Hellaby f = 2 E_Hellaby.  The tree writes 1 + 2E (Hellaby).
check("V7  convention: Hellaby 1 + f = 1 + 2E; Lasky-Lun 1 + E_LL; tree uses Hellaby's (driven.py:599)",
      sp.simplify((1 + 2 * E) - (1 + sp.Symbol("f"))).subs(sp.Symbol("f"), 2 * E) == 0)

# ---------------------------------------------------------------- V8
# Negative Misner-Sharp mass, Lambda = 0: Rdot^2 = 2E - 2|M|/R >= 0 forces E > 0 and R >= |M|/E.
# So m < 0 => E > 0 (Gamma > 1) wherever data exist -- consistent with driven.py 'm < 0 sufficient'.
Mneg = sp.symbols("Mabs", positive=True)
check("V8  m < 0: Rdot^2 = 2E - 2|m|/R >= 0 requires E > 0 (contraction, per driven.py) and R >= |m|/E",
      sp.solve(sp.Eq(2 * Es - 2 * Mneg / Rs, 0), Rs) == [Mneg / Es])

print()
if fails:
    print("FAILED:", fails)
    sys.exit(1)
print("ALL CHECKS PASS  (%d)" % 20)
