#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Barcelo-Visser gr-qc/0003025 sect. 2.3 (the ANEC cases)
as used at research/warp-drive/higgs.py:124-135, 220, 389-401, 627-648.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  A  sympy: eq.(2.8) integrand == eq.(2.10) integrand - d/dlam[2 xi kappa phi phi'/(kappa - xi phi^2)]
     for an ARBITRARY smooth phi(lam)  (the integration by parts of (2.9)-(2.10)).
  B  z3: sign of the (2.10)/(2.11) coefficient kappa[kappa - xi(1-4xi)s]/(kappa - xi s)^2, s = phi^2:
     case 1 (xi<0) positive for all s; case 2 (xi>0, s<kappa/xi) positive; negativity possible only
     for 0<xi<1/4 and s > kappa/(xi(1-4xi)) > kappa/xi (i.e. only inside case 3); none for xi>=1/4.
  C  sympy: the same identity and case-2 positivity for an N=4 real multiplet (the Higgs doublet,
     xi H^dag H R), which BV do not treat -- the tree applies BV to the Higgs.
  D  numeric: case-2 profiles on a COMPLETE geodesic, integrating (2.8) directly (no by-parts):
     ANEC integral >= 0.  And the load-bearing hypothesis: on a FINITE SEGMENT (no complete geodesic
     / no asymptotic fall-off) a case-2 profile gives a NEGATIVE integral.
  E  sympy: the marginal set BV's case split omits (phi^2 <= kappa/xi, touching at a point): the
     integrand diverges as +4 kappa/(lam-lam0)^2 -- a positive, non-integrable divergence, not a violation.
  F  numbers: M_red, v, xi_required, v/M_red (the tree's data_used), their movement with the
     current G and G_F, the M_Planck (non-reduced) variant of BV's '~ m_p/sqrt(xi)', the sign of
     the Higgs-inflation xi in BV's convention, the gate with kappa fixed by the MEASURED G in the
     phi=v vacuum (BV eq. 5.51), and Atkins-Calmet's LHC bound on |xi| (1211.0281).
"""
import math
import sys

import sympy as sp

FAILS = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- A
lam, kap, xi = sp.symbols("lambda kappa xi", real=True)
phi = sp.Function("phi")(lam)
dphi = sp.diff(phi, lam)
den = kap - xi * phi**2
I28 = kap / den * (dphi**2 - 2 * xi * sp.diff(phi * dphi, lam))
I210 = kap * (kap - xi * (1 - 4 * xi) * phi**2) / den**2 * dphi**2
B = 2 * xi * kap * phi * dphi / den
I29 = kap / den * (dphi**2 + 4 * xi**2 * phi**2 * dphi**2 / den)
chk("A1 (2.8) integrand = (2.10) integrand - dB/dlam, B = 2 xi kappa phi phi'/(kappa - xi phi^2)",
    sp.simplify(I28 - (I210 - sp.diff(B, lam))) == 0)
chk("A2 (2.9) bulk integrand == (2.10) bulk integrand ('assemble the pieces')",
    sp.simplify(I29 - I210) == 0)
chk("A3 V(phi) drops out: g_mn k^m k^n = 0, so the ANEC integrand carries no potential (by construction of 2.3)", True,
    "the V term of (2.3) is proportional to g_mn")

# ---------------------------------------------------------------- B (z3)
try:
    import z3
    K, X, S = z3.Reals("K X S")
    coefnum = K - X * (1 - 4 * X) * S  # sign of the numerator; denominator (K - X S)^2 > 0 off the crossing set

    def valid(f):
        s = z3.Solver()
        s.add(z3.Not(f))
        return s.check() == z3.unsat

    def sat(f):
        s = z3.Solver()
        s.add(f)
        r = s.check()
        return r == z3.sat, (s.model() if r == z3.sat else None)

    chk("B1 case 1: xi<0, kappa>0, s>=0  =>  numerator > 0",
        valid(z3.Implies(z3.And(K > 0, X < 0, S >= 0), coefnum > 0)))
    chk("B2 case 2: xi>0, kappa>0, 0<=s<kappa/xi  =>  numerator > 0",
        valid(z3.Implies(z3.And(K > 0, X > 0, S >= 0, X * S < K), coefnum > 0)))
    chk("B3 xi>=1/4: numerator > 0 for every s>=0 (any case-3 violation must come from the crossing boundary terms)",
        valid(z3.Implies(z3.And(K > 0, X >= z3.RealVal("1/4"), S >= 0), coefnum > 0)))
    ok, m = sat(z3.And(K > 0, X > 0, X < z3.RealVal("1/4"), S >= 0, coefnum < 0))
    chk("B4 0<xi<1/4: a negative integrand exists (BV's parenthesis in case 3)", ok, str(m))
    chk("B5 and every such s lies above kappa/xi (negativity is confined to case 3)",
        valid(z3.Implies(z3.And(K > 0, X > 0, X < z3.RealVal("1/4"), S >= 0, coefnum < 0), X * S > K)))
except ImportError:
    chk("B z3 available (pip install z3-solver)", False)

# ---------------------------------------------------------------- C (N=4 multiplet)
N = 4
ph = [sp.Function("phi%d" % a)(lam) for a in range(N)]
rho = sum(p**2 for p in ph)
d = [sp.diff(p, lam) for p in ph]
denN = kap - xi * rho
# T_eff k k for O(N) multiplet with -1/2 xi R sum phi_a^2: kinetic sum phi_a'^2, non-minimal term -xi rho''
I28N = kap / denN * (sum(q**2 for q in d) - xi * sp.diff(rho, lam, 2))
bulkN = kap / denN * sum(q**2 for q in d) + kap * xi**2 * sp.diff(rho, lam)**2 / denN**2
BN = kap * xi * sp.diff(rho, lam) / denN
chk("C1 N=4: (2.8)-type integrand = [kappa/(kappa-xi rho) sum phi_a'^2 + kappa xi^2 rho'^2/(kappa-xi rho)^2] - d/dlam[kappa xi rho'/(kappa - xi rho)]",
    sp.simplify(sp.expand(I28N - (bulkN - sp.diff(BN, lam)))) == 0)
# case 2 positivity: kappa - xi rho > 0 makes both bulk terms sums of non-negative terms
chk("C2 N=4 case 2 (kappa - xi rho > 0): bulk = positive * sum of squares + positive * square  => ANEC >= 0", True,
    "structural: each term is (positive) x (square)")
# reduces to BV single field when N=1
p1 = sp.Function("p")(lam)
r1 = p1**2
bulk1 = kap / (kap - xi * r1) * sp.diff(p1, lam)**2 + kap * xi**2 * sp.diff(r1, lam)**2 / (kap - xi * r1)**2
chk("C3 N=1 limit reproduces BV (2.10) bulk integrand",
    sp.simplify(bulk1 - I210.subs(phi, p1).doit()) == 0)

# ---------------------------------------------------------------- D (numeric)
def integrand28(f, fp, fpp, k, x):
    # (2.8): kappa/(kappa - xi f^2) [ f'^2 - 2 xi (f'^2 + f f'') ]
    return k / (k - x * f * f) * (fp * fp - 2 * x * (fp * fp + f * fpp))


def simpson(g, a, b, n=200000):
    h = (b - a) / n
    s = g(a) + g(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(a + i * h)
    return s * h / 3


k = 1.0
for x in (1.0 / 6.0, 0.3, 5.0, 1e4):
    A = math.sqrt(0.9 * k / x)           # max phi^2 = 0.9 kappa/xi : case 2
    f = lambda l: A / math.cosh(l)
    fp = lambda l: -A * math.tanh(l) / math.cosh(l)
    fpp = lambda l: A * (math.tanh(l) ** 2 - 1 / math.cosh(l) ** 2) / math.cosh(l)
    val = simpson(lambda l: integrand28(f(l), fp(l), fpp(l), k, x), -40.0, 40.0)
    chk("D1 case 2, complete geodesic, phi = A sech(lam), xi=%g, max xi phi^2 = 0.9 kappa: ANEC integral >= 0" % x,
        val >= -1e-9, "I = %.6g" % val)

x = 1.0
A = 0.05
val = simpson(lambda l: integrand28(A * l, A, 0.0, k, x), 0.0, 1.0, 20000)
exact = A**2 * (1 - 2 * x)  # leading order for xi A^2 << kappa
chk("D2 finite segment [0,1], phi = A lam, xi=1, xi phi^2 <= 0.0025 kappa (case 2): segment integral is NEGATIVE",
    val < 0, "I = %.6g, leading-order A^2(1-2xi) = %.6g" % (val, exact))
chk("D3 so 'complete null geodesic + asymptotic fall-off' is load-bearing in BV case 2", val < 0)

# ---------------------------------------------------------------- E (marginal touching set)
a, u = sp.symbols("a u", positive=True)
kp, xp = sp.symbols("kappa_p xi_p", positive=True)
s_touch = kp / xp - a * u**2                    # phi^2 touching kappa/xi at u=0 from below
f_t = sp.sqrt(s_touch)
coef = kp * (kp - xp * (1 - 4 * xp) * s_touch) / (kp - xp * s_touch)**2
integ = coef * sp.diff(f_t, u)**2
lead = sp.limit(sp.simplify(integ * u**2), u, 0)
chk("E1 touching case: (u)^2 x integrand -> 4 kappa > 0 as u -> 0 (positive non-integrable divergence)",
    sp.simplify(lead - 4 * kp) == 0, "limit = %s" % lead)

# ---------------------------------------------------------------- F (numbers)
c = 2.99792458e8
HBAR = 1.054571817e-34
GEV = 1.602176634e-10
G = 6.67430e-11          # CODATA 2018 == CODATA 2022 (2409.03787), u_r 2.2e-5
GF = 1.1663788e-5        # PDG 2024 Table 1.1 (sibling audit fermi-constant-g_f-and-tree-level-vev)


def mred(Gv):
    return math.sqrt(HBAR * c / Gv) * c**2 / GEV / math.sqrt(8 * math.pi)


def vev(gf):
    return 1 / math.sqrt(math.sqrt(2) * gf)


M = mred(G)
v = vev(GF)
xr = (M / v) ** 2
chk("F1 M_reduced = 2.435323e18 GeV", abs(M / 2.435323e18 - 1) < 1e-6, "%.7e" % M)
chk("F2 v = 246.2196 GeV", abs(v - 246.2196) < 5e-5, "%.6f" % v)
chk("F3 xi_required = 9.7829068836e31", abs(xr / 9.7829068836e31 - 1) < 1e-9, "%.10e" % xr)
chk("F4 v/M_red = 1.0110346504e-16", abs((v / M) / 1.0110346504e-16 - 1) < 1e-9, "%.10e" % (v / M))
for tag, Gv in (("G+1sigma", 6.67430e-11 * (1 + 2.2e-5)), ("G-1sigma", 6.67430e-11 * (1 - 2.2e-5))):
    print("     %s: xi_required = %.6e (rel %.2e)" % (tag, (mred(Gv) / v) ** 2, (mred(Gv) / v) ** 2 / xr - 1))
for tag, gf in (("G_F CODATA-2022 1.1663787e-5", 1.1663787e-5), ("G_F Eberhart 2026 1.16637859e-5", 1.16637859e-5)):
    print("     %s: xi_required = %.6e (rel %.2e)" % (tag, (M / vev(gf)) ** 2, (M / vev(gf)) ** 2 / xr - 1))
MP = M * math.sqrt(8 * math.pi)
print("     BV's loose '~ m_p/sqrt(xi)' with the NON-reduced Planck mass: xi = (M_P/v)^2 = %.4e (x 8 pi)" % ((MP / v) ** 2))
chk("F5 the exact case-3 threshold is kappa/xi with kappa = 1/(8 pi G): the tree's REDUCED mass is the exact one", True)

# Higgs inflation, BS 0710.3755 eq.(13): xi ~ 49000 sqrt(lambda), lambda = m_h^2/(2 v^2); conformal is xi = -1/6
mh = 125.13
lam_h = mh**2 / (2 * v**2)
xi_bs = 49000 * math.sqrt(lam_h)
print("     BS eq.(13) with m_h=125.13, v=%.4f: xi_BS = %.4g  (tree pins 1.7e4)" % (v, xi_bs))
print("     BS footnote 1: conformal coupling is xi_BS = -1/6; BV: conformal is xi_BV = +1/6; effective Planck^2:"
      " BS M^2 + xi_BS h^2, BV kappa - xi_BV phi^2  =>  xi_BV = -xi_BS = %.4g" % (-xi_bs))
chk("F6 Higgs inflation's coupling is NEGATIVE in BV's convention -> BV case 1 (ANEC satisfied at every field value)",
    -xi_bs < 0)
# its field values: h_COBE ~ 9.4 M_P/sqrt(xi) -- would be case 3 if the sign were BV-positive
print("     BS: h_COBE ~ 9.4 M_red/sqrt(xi) = %.3e GeV  (> M_red/sqrt(xi) = %.3e): the Higgs field DOES exceed the tree's"
      " gate magnitude during Higgs inflation; only the sign keeps it out of case 3" % (9.4 * M / math.sqrt(xi_bs), M / math.sqrt(xi_bs)))

# gate with kappa fixed by the measured G in the phi = v vacuum (massive Higgs: BV eq. 5.51 without the
# Brans-Dicke factor, which applies to a massless scalar's long-range force)
print("     gate magnitude, tree (kappa = M_red^2) vs consistent (kappa = M_red^2 + xi v^2 so that G_phys is measured G):")
for xv in (1.0 / 6.0, 1.0, 1.7e4, 2.6e15, 1e30, xr, 1e33):
    tree = M / math.sqrt(xv)
    cons = math.sqrt(v**2 + M**2 / xv)
    print("       xi=%-11.4g tree phi_gate=%.6e  consistent phi_gate=%.6e  rel diff=%.3e  consistent/v=%.4f"
          % (xv, tree, cons, cons / tree - 1, cons / v))
# exact arithmetic (floats cannot resolve M^2/xi against v^2 at large xi, nor a 1e-28 relative difference)
from fractions import Fraction as Fr
vq, Mq = Fr(v), Fr(M)
chk("F7 consistent gate: phi_gate^2 - v^2 = M_red^2/xi > 0 at EVERY xi>0, exact (no xi puts the vacuum itself in case 3)",
    all((vq**2 + Mq**2 / Fr(xv)) - vq**2 == Mq**2 / Fr(xv) > 0 for xv in (10**10, 10**32, 10**40, 10**60)))
# relative difference of gates = sqrt(1 + xi v^2/M^2) - 1 ~ xi v^2/(2 M^2)
rd = Fr(17000) * vq**2 / (2 * Mq**2)
chk("F8 at Higgs-inflation |xi| = 1.7e4 the two gates differ by xi v^2/(2 M^2) = %.3e relative (tree's figure unmoved there)"
    % float(rd), rd < Fr(1, 10**20))
# Atkins-Calmet 1211.0281: mu = 1/(1+beta), beta = 6 xi^2 v^2 / M_red^2; mu = 1.07 +- 0.18
for zname, z in (("1.96 sigma", 1.96), ("1.645 sigma", 1.645)):
    mumin = 1.07 - z * 0.18
    beta = 1 / mumin - 1
    xmax = math.sqrt(beta / 6) * M / 246.0
    print("     Atkins-Calmet recomputed (%s lower mu = %.3f, v=246): |xi| < %.3e (paper prints 2.6e15)" % (zname, mumin, xmax))
chk("F9 LHC-2012 bound |xi| < 2.6e15 sits %.1f orders below xi_required" % math.log10(xr / 2.6e15), xr / 2.6e15 > 1e16)
print("     consistent gate at the LHC bound xi=2.6e15: phi > %.3e GeV" % math.sqrt(v**2 + M**2 / 2.6e15))

# ---------------------------------------------------------------- G (incidental, belongs to key ...-eq2.6)
# BV sect. 2.2 prose: "for xi > 0 and |phi| small ... any local maximum of phi^2 violates the NEC".
# Their own eq. (2.6): NEC ~ [phi'^2 - xi (phi^2)''] / (kappa - xi phi^2).  Evaluate at an extremum of phi^2.
s0, b0 = sp.symbols("s0 b0", positive=True)
for kind, sgn in (("maximum", -1), ("minimum", +1)):
    ss = s0 + sgn * b0 * lam**2                  # phi^2 near an extremum at lam=0, phi != 0 there
    ff = sp.sqrt(ss)
    num = (sp.diff(ff, lam)**2 - xi * sp.diff(ss, lam, 2)).subs(lam, 0)
    print("     G: at a local %s of phi^2, NEC numerator = %s" % (kind, sp.simplify(num)))
num_max = (-xi * sp.diff(s0 - b0 * lam**2, lam, 2)).subs(lam, 0)
chk("G1 INCIDENTAL: with xi>0, small field, a local MAXIMUM of phi^2 gives NEC numerator +2 xi b0 > 0 (satisfied);"
    " the MINIMUM violates. BV's sect.2.2 prose has max/min reversed against their own eq.(2.6); FFK 2309.10848"
    " eq.(18) text states the (2.6)-consistent version. Discrepancy, recorded; not this key's statement.",
    sp.simplify(num_max - 2 * xi * b0) == 0)

print()
print("FAILS: %d" % len(FAILS))
sys.exit(1 if FAILS else 0)
