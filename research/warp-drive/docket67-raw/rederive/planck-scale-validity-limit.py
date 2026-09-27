#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for 'planck-scale-validity-limit'.

What is checkable here (the extrapolation itself -- that semiclassical GR+QFT
fails near l_P -- is not a finite claim and is not checked; see the audit):

  F1  l_P = sqrt(hbar G / c^3) from the tree's constants, and its sensitivity
      to G (CODATA 1-sigma).
  F2  sympy: the three crossover closed forms candidates.py states
      (Ford-Roman, Casimir, non-minimal-coupling cutoff).
  F3  numeric: 0.307933, 0.369917, 3.159514 at the board's Lambda.
  F4  CONVENTION: the sources state the Planck scale only up to O(1)
      ('irrelevant numerical factors are ignored', Garay p.2) and Burgess's EFT
      uses the REDUCED Planck mass M_p^-2 = 8 pi G (p.4, p.23).  Re-run the
      tree's two boolean tests (sub-Planckian; 0.1 <= R/l <= 10) under
      l_P, l_P*sqrt(2 pi) (h instead of hbar) and l_P*sqrt(8 pi) (reduced).
  F5  z3: for which Lambda do the band test and the sub-Planckian test hold,
      in each convention (exact, nonlinear real arithmetic on squares).
  F6  independent breakdown measure at the crossover: curvature x l_P^2
      (Burgess p.46: quantum corrections controlled by l_p^2/r^2), and the
      NMC cutoff energy against the Planck energy in both conventions.
"""
import math
import sys

import sympy as sp
import z3

G = 6.67430e-11          # candidates.py:315 (CODATA 2018 = 2022)
G_SIG = 0.00015e-11      # CODATA 1-sigma
C = 2.99792458e8         # exact
HBAR = 1.054571817e-34   # exact since 2019 SI
LAM = 9.982529174194637  # phase1.lam() at the board's seated parameters

ok = True


def check(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))


print("F1  Planck length")
lP = math.sqrt(HBAR * G / C ** 3)
check("tree value 1.61625502392855e-35 m reproduced", abs(lP - 1.61625502392855e-35) < 1e-48,
      "(got %.15e)" % lP)
check("agrees with CODATA 2022 1.616255(18)e-35 m", abs(lP - 1.616255e-35) < 0.000018e-35)
rel = 0.5 * G_SIG / G
print("      G 1-sigma moves l_P by %.2e relative; every crossover is a multiple of l_P"
      " with a Lambda-only coefficient, so R/l_P does not move at all." % rel)

print("F2  closed forms (sympy)")
R, Lam, hb, Gs, c, l = sp.symbols("R Lambda hbar G c l", positive=True)
lPs = sp.sqrt(hb * Gs / c ** 3)
need = c ** 4 / (Gs * Lam * R ** 2)
fr = sp.solve(sp.Eq(need, 3 * hb * c / (32 * sp.pi ** 2 * R ** 4)), R)[0]
cas = sp.solve(sp.Eq(need, sp.pi ** 2 * hb * c / (720 * R ** 4)), R)[0]
nmc = sp.solve(sp.Eq(need, hb * c / (l ** 2 * R ** 2)), l)[0]   # delta = R, N_n = 1
fr_c = sp.simplify(fr / lPs)
cas_c = sp.simplify(cas / lPs)
nmc_c = sp.simplify(nmc / lPs)
check("Ford-Roman R/l_P = sqrt(3 Lambda/(32 pi^2))",
      sp.simplify(fr_c - sp.sqrt(3 * Lam / (32 * sp.pi ** 2))) == 0, str(fr_c))
check("Casimir R/l_P = pi sqrt(Lambda/720)",
      sp.simplify(cas_c - sp.pi * sp.sqrt(Lam / 720)) == 0, str(cas_c))
check("NMC l_UV/l_P = sqrt(Lambda), R-independent",
      sp.simplify(nmc_c - sp.sqrt(Lam)) == 0 and R not in nmc_c.free_symbols, str(nmc_c))
ratio = sp.simplify(nmc_c / fr_c)
check("spread NMC/FR = sqrt(32 pi^2/3), Lambda-free",
      sp.simplify(ratio - sp.sqrt(32 * sp.pi ** 2 / 3)) == 0,
      "= %.6f" % float(ratio))

print("F3  numeric at the board's Lambda = %.12f" % LAM)
vals = {"Ford-Roman": math.sqrt(3 * LAM / (32 * math.pi ** 2)),
        "Casimir": math.pi * math.sqrt(LAM / 720),
        "NMC cutoff": math.sqrt(LAM)}
want = {"Ford-Roman": 0.307933, "Casimir": 0.369917, "NMC cutoff": 3.159514}
for k in vals:
    check("%-10s %.6f l_P" % (k, vals[k]), abs(vals[k] - want[k]) < 1e-6)

print("F4  convention dependence of the tree's two booleans")
convs = {"l_P = sqrt(hbar G/c^3)  (tree)": 1.0,
         "sqrt(h G/c^3)  = sqrt(2 pi) l_P": math.sqrt(2 * math.pi),
         "reduced sqrt(8 pi hbar G/c^3)": math.sqrt(8 * math.pi)}
table = {}
for name, f in convs.items():
    r = {k: v / f for k, v in vals.items()}
    band = all(0.1 <= x <= 10 for x in r.values())
    sub = r["Ford-Roman"] < 1 and r["Casimir"] < 1
    table[name] = (r, band, sub)
    print("   %-34s FR %.4f  Cas %.4f  NMC %.4f   band[0.1,10]=%s  sub-Planckian=%s"
          % (name, r["Ford-Roman"], r["Casimir"], r["NMC cutoff"], band, sub))
check("sub-Planckian holds in all three conventions",
      all(t[2] for t in table.values()))
check("band test holds in tree convention", table["l_P = sqrt(hbar G/c^3)  (tree)"][1])
check("band test FAILS in the reduced convention (recorded, not a refutation)",
      not table["reduced sqrt(8 pi hbar G/c^3)"][1])

print("F5  z3: Lambda windows (squares; exact reals)")
L = z3.Real("L")
pi2 = z3.RealVal(str(math.pi ** 2))  # pi^2 to double precision; bounds printed below


def window(scale2):
    """band: 0.01 <= (x/s)^2 <= 100 for FR, Cas, NMC; scale2 = s^2."""
    fr2 = 3 * L / (32 * pi2) / scale2
    ca2 = pi2 * L / 720 / scale2
    nm2 = L / scale2
    return z3.And(*[z3.And(x >= z3.RealVal("0.01"), x <= 100) for x in (fr2, ca2, nm2)])


for name, s2 in (("tree", 1), ("reduced", 8 * math.pi)):
    s2r = z3.RealVal(str(s2))
    lo = 0.01 * 32 * math.pi ** 2 / 3 * s2
    hi = 100 * s2
    s = z3.Solver()
    s.add(L > 0, z3.Not(z3.Implies(z3.And(L >= z3.RealVal(str(lo * (1 + 1e-12))),
                                          L <= z3.RealVal(str(hi * (1 - 1e-12)))),
                                   window(s2r))))
    r1 = s.check()
    s2c = z3.Solver()
    s2c.add(L == z3.RealVal(str(LAM)), window(s2r))
    r2 = s2c.check()
    print("   %-8s band holds for Lambda in [%.4f, %.2f]: z3 counterexample search -> %s;"
          " board Lambda inside -> %s" % (name, lo, hi, r1, r2))
    check("%s window proved (unsat = no Lambda in window fails)" % name, r1 == z3.unsat)
    if name == "tree":
        check("board Lambda inside tree window", r2 == z3.sat)
    else:
        check("board Lambda OUTSIDE reduced window", r2 == z3.unsat)
s = z3.Solver()
s.add(L > 0, 3 * L / (32 * pi2) >= 1)
print("   FR crossover reaches l_P only for Lambda >= 32 pi^2/3 = %.3f;"
      " Casimir for Lambda >= 720/pi^2 = %.3f" % (32 * math.pi ** 2 / 3, 720 / math.pi ** 2))

print("F6  independent breakdown measures")
# G_00 = 8 pi G rho / c^4 with rho = c^4/(G Lambda R^2)  ->  curvature K = 8 pi/(Lambda R^2)
for k in ("Ford-Roman", "Casimir"):
    x = vals[k]
    K_lP2 = 8 * math.pi / (LAM * x ** 2)
    print("   at the %-10s crossover: l_P^2 * (8 pi G rho/c^4) = %.3f ;"
          " l_P^2 * (G rho/c^4) = %.3f ;  (l_P/R)^2 = %.3f" % (k, K_lP2, K_lP2 / (8 * math.pi),
                                                             1 / x ** 2))
check("curvature in Planck units is >= O(1) at both sub-Planckian crossovers",
      all(1 / (LAM * vals[k] ** 2) > 0.5 for k in ("Ford-Roman", "Casimir")))
xn = vals["NMC cutoff"]
e_over_EP = 1 / xn
e_over_EPred = math.sqrt(8 * math.pi) / xn
print("   NMC cutoff energy hbar c/l_UV: %.4f E_P (non-reduced), %.4f E_P (reduced);"
      " (E/M)^2 = %.3f vs %.3f; with Burgess's loop factor (E/4 pi M)^2 = %.4f vs %.4f"
      % (e_over_EP, e_over_EPred, e_over_EP ** 2, e_over_EPred ** 2,
         (e_over_EP / (4 * math.pi)) ** 2, (e_over_EPred / (4 * math.pi)) ** 2))
check("NMC cutoff is below E_P non-reduced but ABOVE reduced M_p (convention-dependent)",
      e_over_EP < 1 < e_over_EPred)

# Fliss et al. (2309.10848) EFT condition |8 pi G xi phi^2| << 1 with phi^2_max ~ l_UV^-2
# (n = 4, hbar = c = 1, G = l_P^2): 8 pi G xi / l_UV^2 = 8 pi xi / Lambda at l_UV = sqrt(Lambda) l_P
coef = 8 * math.pi / LAM
xi_star = 1 / coef
print("   at l_UV = sqrt(Lambda) l_P: |8 pi G xi phi^2_max| = %.4f xi  -> reaches 1 at xi = %.4f;"
      " conformal xi = 1/6 gives %.3f" % (coef, xi_star, coef / 6))
check("EFT field bound at the NMC crossover is xi-dependent (1 crossed at xi ~ 0.40)",
      0.3 < xi_star < 0.5)

print("\nRESULT:", "ALL CHECKS AS STATED" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
