#!/usr/bin/env python3
"""DOCKET 67 -- audit 21/286: painleve-gullstrand-velocity.

Re-derivation, INDEPENDENT of research/warp-drive (nothing imported from it).
Source restatements read at alphaXiv:
  Martel & Poisson, gr-qc/0001069 (2001), Sec. II eqs (2.1)-(2.7):
      tdot = Etilde/f, rdot^2 + f = Etilde^2, f = 1 - 2M/r;  Etilde = 1 <=> v_inf = 0;
      rdot = -sqrt(1-f) = -sqrt(2M/r);   ds^2 = -dT^2 + (dr + sqrt(2M/r) dT)^2 + r^2 dOmega^2.
  Hamilton & Lisle, gr-qc/0411060, eqs (1)-(6): beta = sqrt(2GM/r) "the Newtonian escape
      velocity"; horizon at beta = 1; beta > 1 inside.
  de Haro, 2601.18660 eqs (18)-(29) (restating Landau-Lifshitz Sec.100 / Lemaitre 1933):
      Lemaitre chart  ds^2 = dT^2 - (r_s/r) dR^2 - r^2 dOmega^2,  R - T = (2/3) r^{3/2}/sqrt(r_s).
Checks:
  C1  Lemaitre chart is Ricci-flat (vacuum), computed from scratch.
  C2  In the tree's (Phi, Lambda, R) frame:  U = -sqrt(r_s/R),  W = 1,  m_MS = r_s/2.
  C3  Lemaitre -> PG is an exact coordinate change (the '= PG' the tree ASSERTS, derived here).
  C4  PG slices are flat;  W = 1  <=>  the T=const slice is flat (dl = dR).
  C5  Etilde = 1 geodesic has rdot = -sqrt(2M/r)  (Martel-Poisson 2.1);  Etilde^2 - 1 = U^2 - 2M/R = 2E_LTB.
  C6  U^2 = W^2 - 1 + 2m/R is the DEFINITION of m_MS rearranged (tautology; z3 confirms and a
      vacuity guard shows the content lives in the witness, not the identity).
  C7  numerics the tree pins: sqrt(2/10) = 0.4472135955; threshold = 1 at R = 2m; |U| > 1 for R < r_s.
  C8  Newtonian escape velocity sqrt(2GM/r) in SI equals c*sqrt(r_s/r) exactly (G, c cancel).
  C9  NARROWING (Faraoni-Vachon 2006.10827): the PG shift is real only where m_MS >= 0.
"""
import sys
import sympy as sp

fails = []
def chk(label, cond):
    print(("  PASS  " if cond else "  FAIL  ") + label)
    if not cond:
        fails.append(label)

# ---------------------------------------------------------------- C1, C2
tau, rho, rs, th, ph = sp.symbols("tau rho r_s theta phi", positive=True)
Rl = (sp.Rational(3, 2) * (rho - tau))**sp.Rational(2, 3) * rs**sp.Rational(1, 3)
x = [tau, rho, th, ph]
Phi = sp.Integer(0)
Lam = sp.log(sp.sqrt(rs / Rl))
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), Rl**2, Rl**2 * sp.sin(th)**2)
gi = g.inv()

def ricci(g, gi, x):
    n = 4
    Gm = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                        - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(n):
                    s += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.simplify(s)
    return Ric

print("C1  Lemaitre chart R = (3/2 (rho - tau))^(2/3) r_s^(1/3), Phi = 0, e^Lambda = sqrt(r_s/R)")
Ric = ricci(g, gi, x)
chk("Ricci tensor vanishes identically (vacuum)", Ric == sp.zeros(4, 4))

print("C2  frame components as the tree defines them (nonstatic.py:302-304, recomputed here)")
U = sp.simplify(sp.exp(-Phi) * sp.diff(Rl, tau))
W = sp.simplify(sp.exp(-Lam) * sp.diff(Rl, rho))
m = sp.simplify(Rl / 2 * (1 - W**2 + U**2))
chk("W = 1 exactly", sp.simplify(W - 1) == 0)
chk("U = -sqrt(r_s/R) = -sqrt(2m/R)", sp.simplify(U + sp.sqrt(rs / Rl)) == 0
    and sp.simplify(U + sp.sqrt(2 * m / Rl)) == 0)
chk("m_MS = r_s/2 (Schwarzschild mass, positive)", sp.simplify(m - rs / 2) == 0)

# ---------------------------------------------------------------- C3
print("C3  Lemaitre -> Painleve-Gullstrand: the '= PG' the tree asserts (drivensource.py:374,189)")
# On the Lemaitre chart, dr = R_tau dtau + R_rho drho.  Solve for drho and substitute into
# (r_s/R) drho^2; the result must be (dr + sqrt(r_s/r) dtau)^2 -- Martel-Poisson (2.7) with T = tau.
r, dtau, dr = sp.symbols("r dtau dr", positive=True)
R_tau = sp.simplify(sp.diff(Rl, tau))
R_rho = sp.simplify(sp.diff(Rl, rho))
chk("R_tau = -sqrt(r_s/R), R_rho = +sqrt(r_s/R) on the chart",
    sp.simplify(R_tau + sp.sqrt(rs / Rl)) == 0 and sp.simplify(R_rho - sp.sqrt(rs / Rl)) == 0)
drho = (dr - R_tau * dtau) / R_rho
lem_rr = (rs / Rl) * drho**2
pg_rr = (dr + sp.sqrt(rs / Rl) * dtau)**2
chk("(r_s/R) drho^2 == (dr + sqrt(r_s/R) dtau)^2  [PG form, Martel-Poisson (2.7), T = tau]",
    sp.simplify(sp.expand(lem_rr - pg_rr)) == 0)
# and PG <- Schwarzschild, Martel-Poisson (2.4)-(2.6): dt = dT - f^{-1} sqrt(2M/r) dr
M, dT = sp.symbols("M dT", positive=True)
f = 1 - 2 * M / r
dt = dT - sp.sqrt(2 * M / r) / f * dr
schw = sp.expand(-f * dt**2 + dr**2 / f)
pg = sp.expand(-dT**2 + (dr + sp.sqrt(2 * M / r) * dT)**2)
chk("Schwarzschild -> PG via T = t + int sqrt(1-f)/f dr  [Martel-Poisson (2.4)-(2.7)]",
    sp.simplify(schw - pg) == 0)

# ---------------------------------------------------------------- C4
print("C4  flat slices and W = 1")
# Lemaitre slice dtau = 0: (r_s/R) drho^2 + R^2 dOmega^2 with drho = sqrt(R/r_s) dR  ->  dR^2 + R^2 dOmega^2
slice_rr = sp.simplify((rs / Rl) * (dr / R_rho)**2)
chk("Lemaitre tau=const slice: g_RR = 1 (intrinsically flat, = PG T=const slice)", sp.simplify(slice_rr - dr**2) == 0)
# General: on a t=const slice of diag(-e^{2Phi}, e^{2Lambda}, R^2, R^2 sin^2), proper radial length
# dl = e^{Lambda} dr = (e^{Lambda}/R') dR = dR / W.  So W = 1 <=> dl = dR <=> slice metric dR^2 + R^2 dOmega^2.
Wsym, dRs = sp.symbols("W dR", positive=True)
chk("dl = dR / W  =>  W = 1 <=> the slice is the flat metric dR^2 + R^2 dOmega^2", sp.simplify((dRs / Wsym).subs(Wsym, 1) - dRs) == 0)

# ---------------------------------------------------------------- C5
print("C5  the marginally bound geodesic (Martel-Poisson 2.1-2.2)")
Et = sp.Symbol("Etilde", positive=True)
rdot2 = Et**2 - f                       # (2.1): rdot^2 + f = Etilde^2
chk("Etilde = 1  =>  rdot^2 = 2M/r, i.e. |rdot| = sqrt(2M/r) = the PG shift",
    sp.simplify(rdot2.subs(Et, 1) - 2 * M / r) == 0)
chk("Etilde^2 - 1 = rdot^2 - 2M/r  (= 2E_LTB, the tree's 'W^2 - 1 = 2E' with W = Etilde)",
    sp.simplify((Et**2 - 1) - (rdot2 - 2 * M / r)) == 0)
vinf = sp.Symbol("v_inf", nonnegative=True)
chk("Etilde = 1/sqrt(1 - v_inf^2) = 1  <=>  v_inf = 0  (free fall from REST at infinity)",
    sp.solve(sp.Eq(1 / sp.sqrt(1 - vinf**2), 1), vinf) == [0])

# ---------------------------------------------------------------- C6
print("C6  what the identity U^2 = W^2 - 1 + 2m/R is: the definition of m_MS rearranged")
Us, Ws, ms, Rs = sp.symbols("U W m R", real=True)
chk("m := R/2 (1 - W^2 + U^2)  ==>  U^2 - (W^2 - 1 + 2m/R) == 0 identically",
    sp.simplify(Us**2 - (Ws**2 - 1 + 2 * (Rs / 2 * (1 - Ws**2 + Us**2)) / Rs)) == 0)
try:
    import z3
    U_, W_, m_, R_ = z3.Reals("U W m R")
    s = z3.Solver()
    s.add(R_ > 0, W_ > 0, m_ == R_ / 2 * (1 - W_ * W_ + U_ * U_))
    s.add(z3.Not((W_ == 1) == (U_ * U_ == 2 * m_ / R_)))
    chk("z3: W = 1 <=> U^2 = 2m/R given the m_MS definition (no counterexample)", s.check() == z3.unsat)
    # vacuity guard: without the definition of m the equivalence must NOT be provable
    s2 = z3.Solver()
    s2.add(R_ > 0, W_ > 0, z3.Not((W_ == 1) == (U_ * U_ == 2 * m_ / R_)))
    chk("z3 vacuity guard: drop the m_MS definition and a counterexample exists", s2.check() == z3.sat)
    # |U| > 1 inside r_s for the witness U^2 = r_s/R:
    s3 = z3.Solver(); rs_, R3, U3 = z3.Reals("rs R3 U3")
    s3.add(rs_ > 0, R3 > 0, R3 < rs_, U3 * U3 == rs_ / R3, U3 * U3 <= 1)
    chk("z3: U^2 = r_s/R and 0 < R < r_s  =>  U^2 > 1 (no counterexample)", s3.check() == z3.unsat)
    # C9 narrowing: W = 1 forces m >= 0
    s4 = z3.Solver()
    s4.add(R_ > 0, m_ == R_ / 2 * (1 - W_ * W_ + U_ * U_), W_ == 1, m_ < 0)
    chk("z3: W = 1 and R > 0  =>  m_MS >= 0  (PG shift real only where m >= 0; Faraoni-Vachon)", s4.check() == z3.unsat)
except ImportError:
    print("  SKIP  z3 not installed")

# ---------------------------------------------------------------- C7
print("C7  numerics the tree pins (driven.py:732-739, :220)")
import math
chk("sqrt(2*1/10) = 0.4472135955 (1e-9)", abs(math.sqrt(0.2) - 0.4472135955) < 1e-9)
chk("threshold = 1 exactly at R = 2m", math.sqrt(2 * 1.0 / 2.0) == 1.0)
chk("|U| = sqrt(r_s/R) > 1 at R = 0.5 r_s, 0.1 r_s", all(math.sqrt(1 / q) > 1 for q in (0.5, 0.1, 0.999)))

# ---------------------------------------------------------------- C8
print("C8  Newtonian escape velocity, SI (CODATA 2018 G, exact c) vs geometric sqrt(r_s/r)")
G, c = 6.67430e-11, 299792458.0
Msun, rr = 1.98892e30, 6.957e8
v_esc = math.sqrt(2 * G * Msun / rr)
r_s_SI = 2 * G * Msun / c**2
chk("sqrt(2GM/r) == c*sqrt(r_s/r) to machine precision (G and c cancel: no datum enters)",
    abs(v_esc - c * math.sqrt(r_s_SI / rr)) / v_esc < 1e-14)
print("     v_esc(Sun surface) = %.4f km/s; r_s(Sun) = %.4f km" % (v_esc / 1e3, r_s_SI / 1e3))

print()
print("RESULT:", "ALL CHECKS PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
