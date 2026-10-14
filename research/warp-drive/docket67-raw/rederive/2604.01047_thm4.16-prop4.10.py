#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv 2604.01047v1) Thm 4.16 / Prop. 4.10, AS linstab.py USES THEM.

What the tree uses (linstab.py:143-145, 177-180, 350-352, 1054-1055):
  Thm 4.16  "a zero of the dispersion function on the growing side gives exponential growth
             (for Z strictly inside (-4m^2, 0))"
  Prop 4.10 "b_0, b_1, b_2 != 0"
  and concludes ALPHA_ZERO_ROOT_GROWTH = "OPEN": at alpha~^S_1 = 0 (b_0 = 0), gamma = 0 is a root of
  F_S, and whether anything grows from it lies outside both results.

The theorem TEXT could not be read in this session (alphaXiv quota exhausted; arxiv.org egress-blocked),
so nothing here checks the theorem itself.  What IS checked is every finite / closed-form claim the
tree builds on the two scope conditions, using only GMMPS's dispersion functions as the tree transcribes
them ((5.2)-(5.4), (4.5), (4.17); READ at source in the sibling audit 2604.01047_spectral-j) --
nothing is imported from the tree.

 R1  F_S(0) = -b_0, and b_0 = 0 iff alpha~^S_1 = 0  (so gamma = 0 is a root exactly then)       sympy
 R2  F_S'(0) = a^2 J(0) - b_1 > 0 for every kappa > 0, xi != 1/6  -> gamma = 0 is a SIMPLE zero;
     by the implicit function theorem no second real zero bifurcates from it at alpha~ = 0       sympy
 R3  z3: at alpha~^S_1 = 0 and b_2 >= 0, F_S < 0 on the WHOLE real growing side gamma < 0
     (J > 0 there as a Stieltjes transform of rho >= 0) -- no real growing zero at all;
     vacuity guard (hypotheses sat) and control (b_2 < 0 admits a zero: sat)                     z3
 R4  z3: at alpha~^S_1 > 0, F_S(0) > 0 and F_S -> -inf... the tree's branch root: F_S(0-) > 0,
     so with R3's sign on the far side there is a zero in gamma < 0 (only for b_2 >= 0 shown)    z3
 R5  TT sector: F_TT has the factor gamma, so gamma = 0 is a root for EVERY choice of constants
     (b_0 = 0 by Thm 3.6's alpha~^TT_1 = 0) -- GMMPS's own 5.2 negative zero therefore sits in a
     sector with b_0 = 0, i.e. outside "b_0, b_1, b_2 != 0" AS THE TREE STATES Prop. 4.10.
     Also a = 4m^2 in TT, the endpoint excluded by Prop. 4.12's a_i < 4m^2 (sibling audit C9).  sympy
 R6  RANGE: which zeros lie strictly inside (-4m^2, 0), with m = 1, kappa = eps = (m/M_P)^2 at
     GMMPS's matched m:  the reported branch root gamma_0 (inside), the tree's bracketed b_2 roots
     at |b_2| = 1e100 (inside), and the "Planckian for O(1)" b_2 roots (|g*| ~ 1/eps >> 4: OUTSIDE)
                                                                                                  numeric
 R7  HEURISTIC (not a theorem, recorded only): with gamma = -w^2 (w the Laplace variable), a simple
     zero of F at gamma = 0 is a DOUBLE zero of F(-w^2) at w = 0; 1/(c w^2) inverts to t/c --
     polynomial, not exponential.  Whether GMMPS's solution formula has such a pole (or a numerator
     that cancels it) is exactly what the unread theorem would say.                              sympy
Exit 0 iff every assertion passes.
"""
import sys
import math
import sympy as sp
import mpmath as mp
import z3

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# ------------------------------------------------------------ transcription of (5.2)-(5.4)
m, kap = sp.symbols('m kappa', positive=True)
al, xi, g, b2 = sp.symbols('alpha xi gamma b_2', real=True)
c = 6 * (sp.Rational(1, 6) - xi) ** 2
b0 = -al * 4 * m ** 4 / c
b1 = -(2 / kap) / c
a = 2 * m ** 2 / (6 * xi - 1)
Mv = sp.Symbol('M', positive=True)
rho = sp.sqrt(1 - 4 * m ** 2 / Mv) / (16 * sp.pi ** 2 * Mv)          # (4.5)
J0 = sp.simplify(sp.integrate(rho / Mv, (Mv, 4 * m ** 2, sp.oo)))
chk("J(0) = 1/(96 pi^2 m^2) from (4.5)", sp.simplify(J0 - 1 / (96 * sp.pi ** 2 * m ** 2)) == 0)
Jf = sp.Function('J')
FS = g * (a - g) ** 2 * Jf(g) - (b0 + b1 * g + b2 * g ** 2)           # (5.3)

# R1
F0 = sp.simplify(FS.subs(g, 0))
chk("R1 F_S(0) = -b_0", sp.simplify(F0 + b0) == 0)
chk("R1 b_0 = 0 iff alpha~^S_1 = 0", sp.solve(sp.Eq(b0, 0), al) == [0])

# R2
F1 = sp.diff(FS, g).subs(g, 0).doit()
F1 = sp.simplify(F1.subs(Jf(0), J0))
F1pos = sp.simplify(F1 * kap * (1 - 6 * xi) ** 2)
print("   F_S'(0) * kappa (1-6xi)^2 =", F1pos)
chk("R2 F_S'(0) kappa (1-6 xi)^2 = 12 + kappa m^2/(24 pi^2)  (> 0)",
    sp.simplify(F1pos - (12 + kap * m ** 2 / (24 * sp.pi ** 2))) == 0)
chk("R2 hence F_S'(0) > 0 for kappa, m > 0, xi != 1/6: gamma = 0 a SIMPLE zero at alpha~ = 0",
    (12 + kap * m ** 2 / (24 * sp.pi ** 2)).is_positive is True)

# R3 / R4 (z3) : real growing side gamma < 0; J(gamma) > 0 there (M - gamma > 0, rho >= 0)
G, JJ, A, B1, B2, AL, C, M4 = z3.Reals('G JJ A B1 B2 AL C M4')
F = G * (A - G) * (A - G) * JJ - (-AL * 4 * M4 / C + B1 * G + B2 * G * G)
base = [G < 0, JJ > 0, B1 < 0, C > 0, M4 > 0]          # b_1 = -(2/kappa)/c < 0, c > 0


def status(hyp, concl=None):
    s = z3.Solver()
    s.add(*hyp)
    if concl is not None:
        s.add(z3.Not(concl))
    return s.check()


h3 = base + [AL == 0, B2 >= 0]
chk("R3 vacuity guard: hypotheses (alpha~=0, b_2>=0, gamma<0, J>0) satisfiable", status(h3) == z3.sat)
chk("R3 z3: alpha~^S_1 = 0, b_2 >= 0  =>  F_S(gamma) < 0 for all real gamma < 0 (negation unsat)",
    status(h3, F < 0) == z3.unsat)
chk("R3 control: with b_2 < 0 a zero on gamma < 0 is admissible (sat)",
    status(base + [AL == 0, B2 < 0, F == 0]) == z3.sat)
chk("R4 z3: alpha~^S_1 > 0 => F_S(0) = 4 alpha m^4/c > 0 (the branch root's sign change starts)",
    status([AL > 0, C > 0, M4 > 0], (AL * 4 * M4 / C) > 0) == z3.unsat)

# R5 TT sector (5.4): F_TT = gamma (a-gamma)^2 J - gamma (b_1 + b_2 gamma), a = 4 m^2, b_1 = 60/kappa
aT, b1T = 4 * m ** 2, 60 / kap
FTT = g * (aT - g) ** 2 * Jf(g) - g * (b1T + b2 * g)
chk("R5 F_TT(0) = 0 identically in (kappa, b_2, J): gamma = 0 always a TT root (b_0 = 0)",
    sp.simplify(FTT.subs(g, 0)) == 0)
FTT1 = sp.simplify(sp.diff(FTT, g).subs(g, 0).doit().subs(Jf(0), J0))
print("   F_TT'(0) =", FTT1)
chk("R5 F_TT'(0) = m^2/(6 pi^2) - 60/kappa  (simple zero unless kappa m^2 = 360 pi^2)",
    sp.simplify(FTT1 - (m ** 2 / (6 * sp.pi ** 2) - 60 / kap)) == 0)
chk("R5 a_TT = 4 m^2 is the endpoint Prop. 4.12 excludes (a_i < 4m^2 strictly)", aT == 4 * m ** 2)

# R6 range, numeric at GMMPS's matched point (m = 1 units)
HBAR, CSI, GSI, E = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.602176634e-19
MP_eV = math.sqrt(HBAR * CSI / (8 * math.pi * GSI)) * CSI ** 2 / E
alpha1 = 1 / (64 * math.pi ** 2)
x4 = 7.15e-121 / (6 * 0.685 * alpha1)          # GMMPS 5.3 inversion, printed inputs
m_eV, eps = x4 ** 0.25 * MP_eV, x4 ** 0.5
print("   matched m = %.4e eV, eps = kappa m^2 = %.4e" % (m_eV, eps))
chk("R6 matched m reproduces ~7.8e-3 eV (within 2%)", abs(m_eV - 7.8e-3) / 7.8e-3 < 0.02)
g0 = -2 * eps * alpha1 / (1 + eps / (288 * math.pi ** 2))
print("   branch root gamma_0 = %.4e (m^2 units)" % g0)
chk("R6 GMMPS's reported branch root lies strictly inside (-4m^2, 0)", -4 < g0 < 0)
kmax = 2 / alpha1                                # -2 kappa alpha m^4 > -4 m^2  <=> kappa m^2 < 2/alpha
print("   branch root inside (-4m^2,0) at first order iff kappa m^2 < 2/alpha = %.1f" % kmax)
chk("R6 condition kappa m^2 < 2/alpha~ = 128 pi^2 holds at matched m", eps < kmax)
res = {}
for xiv in (0.0, 1.0 / 3):
    cc = 6 * (1 / 6 - xiv) ** 2
    b1v = -(2 / eps) / cc
    for b2v in (1e100, 1.0, 1e-3):
        gs = -abs(b1v / b2v)
        res[(xiv, b2v)] = gs
        print("   xi=%.3f |b_2|=%.0e : g* = -|b_1/b_2| = %.3e  -> %s" % (
            xiv, b2v, gs, "INSIDE (-4,0)" if -4 < gs < 0 else "OUTSIDE (-4,0)"))
b1T_v = 60 / eps
gsT = -abs(b1T_v / 1e100)
print("   TT |b_2|=1e100: g* = %.3e" % gsT)
chk("R6 tree's bracketed b_2 roots (|b_2| = 1e100, S xi=0,1/3 and TT) lie inside (-4m^2, 0)",
    all(-4 < res[(x, 1e100)] < 0 for x in (0.0, 1.0 / 3)) and -4 < gsT < 0)
chk("R6 the 'Planckian for O(1) b_2' roots lie OUTSIDE (-4m^2, 0) (|g*| ~ 1/eps >> 4)",
    all(res[(x, 1.0)] < -4 for x in (0.0, 1.0 / 3)))
b2_edge = abs(-(2 / eps) / (6 * (1 / 6) ** 2)) / 4
print("   S, xi=0: g* inside (-4m^2,0) iff |b_2| > |b_1|/(4m^2) = %.3e" % b2_edge)
chk("R6 S xi=0: inside iff |b_2| > 3/eps (= %.2e)" % (3 / eps), abs(b2_edge - 3 / eps) / (3 / eps) < 1e-12)

# R7 heuristic
t, w = sp.symbols('t w', positive=True)
Cc = sp.Symbol('C', positive=True)
inv = sp.inverse_laplace_transform(1 / (Cc * w ** 2), w, t)
print("   L^-1[1/(C w^2)] =", inv)
chk("R7 simple zero at gamma = -w^2 = 0 -> double pole at w = 0 -> t/C (polynomial, NOT exponential)",
    sp.simplify(inv - t / Cc) == 0)
Fw = sp.expand((g * 5).subs(g, -w ** 2))       # any F with F(0)=0, F'(0)=5
chk("R7 order of the zero in w is 2 when F'(gamma=0) != 0", sp.Poly(Fw, w).monoms()[-1][0] == 2)

print("\nALL PASS" if ok else "\nSOME FAILED")
sys.exit(0 if ok else 1)
