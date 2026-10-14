#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 2309.10848-verdict-anec.

FFKP (Fliss, Freivogel, Kontou, Pardo Santos, arXiv:2309.10848v1):
  classical effective ANEC, Sec. II.B eqs. (18)-(20);
  semiclassical ANEC limit, Sec. IV.C eqs. (85)-(89).
Source text read from scratchpad/d67/src/2309.10848.flat (alphaXiv full-text extraction,
md5 of .txt 4f31876842f625e48506444afd216ee0).

Checks
  A  (19) - (20) integrand is an exact total derivative   (sympy, arbitrary phi(lambda))
  B  sign regions of the (20) numerator N = 1 - xi*x*(1-4xi), x = 8 pi G phi^2 >= 0   (z3)
     with vacuity guards (each hypothesis set satisfiable)
  C  numeric: complete geodesic, bounded field -> (19) integral >= 0 and equals (20);
     finite segment around a local minimum of phi^2 -> (19) integral < 0
     (the complete-geodesic / fall-off hypothesis is load-bearing)
  D  semiclassical limit of (85): delta+ -> 0 with delta+ delta- = alpha^2 fixed; both terms
     vanish for finite phi_max in every reading of the source's alpha exponent; with no
     field bound (phi_max^2 growing like delta-^2) the second term does not vanish.
Prints REDERIVE PASS on success.
"""
import sympy as sp
import z3
import math

ok = True
def rep(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("   " + extra if extra else ""))

# ---------------------------------------------------------------- A
lam, a, xi = sp.symbols('lambda a xi', real=True)
phi = sp.Function('phi', real=True)(lam)
g = 1 / (1 - a * phi**2)                       # a = 8 pi G_N xi
I19 = g * (sp.diff(phi, lam)**2 - xi * sp.diff(phi**2, lam, 2))
I20 = (1 - a * (1 - 4 * xi) * phi**2) / (1 - a * phi**2)**2 * sp.diff(phi, lam)**2
boundary = -xi * g * sp.diff(phi**2, lam)      # (19) - (20) = d/dlambda [boundary]
rep("A1 (19)-(20) = d/dlambda[-xi (phi^2)'/(1-a phi^2)]  (sympy, arbitrary phi)",
    sp.simplify(I19 - I20 - sp.diff(boundary, lam)) == 0)
# FFKP's a = 8 pi G xi: substitute and confirm numerator is 1 - 8piG xi (1-4xi) phi^2
G = sp.symbols('G', positive=True)
num = sp.factor(sp.simplify(I20 * (1 - a*phi**2)**2 / sp.diff(phi, lam)**2).subs(a, 8*sp.pi*G*xi))
rep("A2 numerator = 1 - 8 pi G xi (1-4 xi) phi^2 (FFKP eq. 20)",
    sp.simplify(num - (1 - 8*sp.pi*G*xi*(1-4*xi)*phi**2)) == 0, str(num))
# pole behaviour: numerator at a phi^2 = 1 equals 4 xi
rep("A3 numerator at 8piG xi phi^2 = 1 equals 4 xi (positive for xi>0)",
    sp.simplify((1 - a*(1-4*xi)*phi**2).subs(phi**2, 1/a) - 4*xi) == 0)

# ---------------------------------------------------------------- B
X, XI = z3.Reals('x xi')
N = 1 - XI * X * (1 - 4 * XI)
def valid(hyp, concl):
    s = z3.Solver(); s.add(hyp, z3.Not(concl)); r = s.check()
    v = z3.Solver(); v.add(hyp); vac = v.check()
    return r == z3.unsat and vac == z3.sat
base = X >= 0
rep("B1 xi<0 => N>0 (all field values)", valid(z3.And(base, XI < 0), N > 0))
rep("B2 xi>1/4 => N>0 (all field values)", valid(z3.And(base, XI > z3.RealVal(1)/4), N > 0))
rep("B3 0<xi<1/4 and EFT bound xi*x<1 => N>0",
    valid(z3.And(base, XI > 0, XI < z3.RealVal(1)/4, XI*X < 1), N > 0))
rep("B4 0<xi<1/4 and N<0 => xi*x > 1/(1-4xi) > 1 (negativity needs beyond-critical field)",
    valid(z3.And(base, XI > 0, XI < z3.RealVal(1)/4, N < 0), z3.And(XI*X*(1-4*XI) > 1, XI*X > 1)))
s = z3.Solver(); s.add(base, XI > 0, XI < z3.RealVal(1)/4, N < 0)
rep("B5 non-vacuous: a violating point exists beyond the bound", s.check() == z3.sat, str(s.model()) if s.check()==z3.sat else "")
s = z3.Solver(); s.add(base, XI == z3.RealVal(1)/6, N < 0, XI*X <= 3)
rep("B6 at conformal xi=1/6, N<0 impossible for 8piG xi phi^2 <= 3 (threshold 1/(1-4xi)=3)", s.check() == z3.unsat)

# ---------------------------------------------------------------- C
def integrate(f, lo, hi, n=200000):
    h = (hi - lo) / n; s = 0.5 * (f(lo) + f(hi))
    for k in range(1, n): s += f(lo + k*h)
    return s * h
def make(av, xv, prof, dprof, d2prof):
    # phi = prof(l); returns integrands of (19) and (20)
    def i19(l):
        p, dp, d2p = prof(l), dprof(l), d2prof(l)
        d2phi2 = 2*dp*dp + 2*p*d2p
        return (dp*dp - xv*d2phi2) / (1 - av*p*p)
    def i20(l):
        p, dp = prof(l), dprof(l)
        return (1 - av*(1-4*xv)*p*p) / (1 - av*p*p)**2 * dp*dp
    return i19, i20
xv = 1.0/6.0; av = 1.0          # units 8 pi G = 1/xi -> a = 8 pi G xi = 1 ; bound phi^2 < 1
A0 = 0.9                        # peak a phi^2 = 0.81 < 1 : inside the EFT bound
prof = lambda l: A0*math.exp(-l*l)
dprof = lambda l: -2*l*A0*math.exp(-l*l)
d2prof = lambda l: (4*l*l-2)*A0*math.exp(-l*l)
i19, i20 = make(av, xv, prof, dprof, d2prof)
J19 = integrate(i19, -12, 12); J20 = integrate(i20, -12, 12)
rep("C1 complete geodesic, bounded Gaussian profile: (19) integral >= 0", J19 > 0, "I19=%.8f" % J19)
rep("C2 (19) and (20) integrals agree when boundary terms vanish", abs(J19 - J20) < 1e-8, "I20=%.8f" % J20)
# finite segment around a local MINIMUM of phi^2 (xi>0, small field): effective NEC violated there
p0, eps, L = 0.5, 1.0, 0.3
prof2 = lambda l: p0*(1+eps*l*l); dprof2 = lambda l: 2*p0*eps*l; d2prof2 = lambda l: 2*p0*eps
j19, _ = make(av, xv, prof2, dprof2, d2prof2)
K = integrate(j19, -L, L, 20000)
rep("C3 finite segment [-0.3,0.3] at a local min of phi^2, a phi^2<=0.30: (19) integral < 0",
    K < 0 and max(av*prof2(l)**2 for l in (-L, 0, L)) < 1, "I=%.6f" % K)

# ---------------------------------------------------------------- D
dp_, al, n_, Nn, C, A, xiabs, pm2 = sp.symbols('delta_p alpha n N_n C A xiabs phimax2', positive=True)
dm = al**2 / dp_
t1 = (dm / A) * Nn / (dp_**((n_-2)/2) * dm**((n_+2)/2))
t2 = (dm / A) * C * xiabs * pm2 / dm**2                       # phi_max fixed (dimensionful)
t1s = sp.simplify(sp.powsimp(sp.expand_power_base(t1, force=True), force=True))
t2s = sp.simplify(t2)
rep("D1 first term of (85) after ANEC normalisation ~ delta+ / (A alpha^n)",
    sp.simplify(t1s - Nn*dp_/(A*al**n_)) == 0, str(t1s))
rep("D2 second term, phi_max fixed: ~ delta+ /(A alpha^2)  -> 0",
    sp.simplify(t2s - C*xiabs*pm2*dp_/(A*al**2)) == 0 and sp.limit(t2s, dp_, 0) == 0, str(t2s))
pt = sp.symbols('phitilde2', positive=True)
t2t = sp.simplify(t2.subs(pm2, pt * al**(-(n_-2))))            # phi~^2 = alpha^(n-2) phi^2 fixed
rep("D3 second term, phi~_max fixed: ~ delta+/(A alpha^n); = alpha^-4 at n=4 (source prints alpha^4)",
    sp.simplify(t2t - C*xiabs*pt*dp_/(A*al**n_)) == 0, str(t2t))
t2u = sp.simplify(t2.subs(pm2, dm**2))                          # no field bound: phi_max^2 ~ delta-^2
rep("D4 guard: unbounded field (phi_max^2 ~ delta-^2) -> second term does NOT vanish",
    sp.limit(t2u, dp_, 0) != 0, "limit=%s" % sp.limit(t2u, dp_, 0))

print("REDERIVE PASS" if ok else "REDERIVE FAIL")
