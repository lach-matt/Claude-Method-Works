#!/usr/bin/env python3
"""DOCKET 67, pass S, result 13: cauchy-schwarz-inequality.

The tree's use (research/warp-drive/formation.py:182-192, checked at 1072-1075):
    INT_0^tau_p f_tau^2 dtau >= (INT_0^tau_p f_tau dtau)^2 / tau_p = 1/tau_p
under H_ENDS (f: 0 -> 1), H_REST (f C^1, f_tau = 0 at both ends), H_FAMILY,
and its consequence INT (time part of rho + p_T) dtau = -(omega^2/8pi) INT f_tau^2
<= -(omega^2/8pi)/tau_p, "STRICTLY NEGATIVE".

Checks (each prints OK/FAIL; exit 1 on any FAIL):
 C1 sympy  Lagrange/variance identity: INT f'^2 - (INT f')^2/T = INT (f' - mean f')^2
           for a generic degree-6 polynomial f on [0,T] (exact, symbolic).
 C2 sympy  the three tree profiles: INT_0^1 f_s^2 ds exactly, each > 1 (strict).
 C3 sympy  equality case: f' constant (linear) gives exactly 1/T -- and violates H_REST.
 C4 sympy  sharpness: trapezoid-velocity profiles at rest at both ends with ramp eps
           give INT f'^2 = 1/(T(1 - 2eps/(3T))^2)... -> 1/T as eps -> 0, so 1/tau_p is
           the infimum under H_REST and is NOT attained (strict but sharp).
 C5 sympy  the coordinate->Eulerian conversion of p_T's time part:
           e^{-2 f phi}(f'' - (phi+omega) f'^2) == f_tautau - omega f_tau^2, dtau = e^{f phi}dt.
 C6 numeric integration by parts in tau on each profile at two lapses: INT f_tautau dtau = 0
           and INT f_tau^2 dtau >= 1/tau_p, with tau computed from dtau = e^{f phi} dt.
 C7 z3     discrete analogue over R^4: sum x^2 >= (sum x)^2/4 (unsat of negation), strict
           with x_1 = x_4 = 0 and sum = 1; VACUITY GUARD: equality IS satisfiable without
           the rest constraint; ENCODING GUARD: a drifted bound (sum x)^2/3 is refuted (sat).
 C8 sympy  what strictness needs beyond C-S: omega = ln W_1 != 0; at W_1 = 1 the cost is 0.
"""
import sys
import sympy as sp
import mpmath as mp

fails = []


def chk(tag, label, got, want=True):
    ok = (got == want)
    print("  [%s] %-4s %s -> %s" % ("OK" if ok else "FAIL", tag, label, got))
    if not ok:
        fails.append(label)


print("C1  variance identity (generic polynomial, exact)")
t, T = sp.symbols("t T", positive=True)
cs = sp.symbols("c0:7")
f = sum(c * t**k for k, c in enumerate(cs))
fp = sp.diff(f, t)
lhs = sp.integrate(fp**2, (t, 0, T)) - sp.integrate(fp, (t, 0, T))**2 / T
mean = sp.integrate(fp, (t, 0, T)) / T
rhs = sp.integrate((fp - mean)**2, (t, 0, T))
chk("sym", "INT f'^2 - (INT f')^2/T - INT (f'-mean)^2 == 0", sp.expand(lhs - rhs), 0)

print("C2  the tree's three profiles (formation.py:804-808), s in [0,1]")
s = sp.Symbol("s")
PROFILES = {
    "smoothstep": 3 * s**2 - 2 * s**3,
    "sine": sp.sin(sp.pi * s / 2)**2,
    "overshoot": 3 * s**2 - 2 * s**3 + sp.Rational(4, 5) * sp.sin(sp.pi * s)**2,
}
vals = {}
for name, p in PROFILES.items():
    dp = sp.diff(p, s)
    ends = [sp.simplify(e) for e in (p.subs(s, 0), p.subs(s, 1), dp.subs(s, 0), dp.subs(s, 1))]
    chk("sym", "%s: (f0,f1,f'0,f'1) = (0,1,0,0)" % name, ends, [0, 1, 0, 0])
    I = sp.simplify(sp.integrate(dp**2, (s, 0, 1)))
    vals[name] = I
    chk("sym", "%s: INT f_s^2 = %s = %.6f > 1 (strict)" % (name, I, float(I)), bool(I > 1))
chk("sym", "smoothstep value is exactly 6/5", vals["smoothstep"], sp.Rational(6, 5))
chk("sym", "sine value is exactly pi^2/8", sp.simplify(vals["sine"] - sp.pi**2 / 8), 0)

print("C3  equality case")
lin = t / T
chk("sym", "linear f = t/T gives INT f'^2 = 1/T exactly",
    sp.simplify(sp.integrate(sp.diff(lin, t)**2, (t, 0, T)) - 1 / T), 0)
chk("sym", "linear f is NOT at rest (f'(0) = 1/T != 0): violates H_REST",
    sp.diff(lin, t).subs(t, 0) != 0)

print("C4  sharpness: trapezoid velocity at rest at both ends, ramps of width e")
e, v = sp.symbols("e v", positive=True)
# f' = v t/e on [0,e], v on [e,T-e], v (T-t)/e on [T-e,T]; INT f' = 1 fixes v
area = sp.integrate(v * t / e, (t, 0, e)) + v * (T - 2 * e) + sp.integrate(v * (T - t) / e, (t, T - e, T))
vsol = sp.solve(sp.Eq(area, 1), v)[0]
E2 = (sp.integrate((v * t / e)**2, (t, 0, e)) + v**2 * (T - 2 * e)
      + sp.integrate((v * (T - t) / e)**2, (t, T - e, T))).subs(v, vsol)
E2 = sp.simplify(E2)
print("      INT f'^2 =", E2)
chk("sym", "INT f'^2 - 1/T > 0 for 0 < e < T/2 (sampled e = T/10, T/100)",
    all(bool(sp.simplify((E2 - 1 / T).subs(e, T / k)) > 0) for k in (10, 100)))
chk("sym", "lim_{e->0} INT f'^2 = 1/T (bound is the infimum, not attained)",
    sp.simplify(sp.limit(E2, e, 0) - 1 / T), 0)

print("C5  coordinate-time -> Eulerian-proper-time form of p_T's time part")
ph, om = sp.symbols("phi omega", real=True)
F = sp.Function("f")(t)
fd, fdd = sp.diff(F, t), sp.diff(F, t, 2)
lapse = sp.exp(F * ph)
ftau = fd / lapse
ftautau = sp.diff(ftau, t) / lapse
coord = sp.exp(-2 * F * ph) * (fdd - (ph + om) * fd**2)
euler = ftautau - om * ftau**2
chk("sym", "e^{-2f phi}(f''-(phi+omega)f'^2) - (f_tautau - omega f_tau^2) == 0",
    sp.simplify(coord - euler), 0)

print("C6  numeric, in Eulerian proper time, at two lapse values (phi = -0.3, +0.2)")
mp.mp.dps = 30
Tn = mp.mpf(3)
for name, p in PROFILES.items():
    pf = sp.lambdify(s, p, "mpmath")
    dpf = sp.lambdify(s, sp.diff(p, s), "mpmath")
    ddpf = sp.lambdify(s, sp.diff(p, s, 2), "mpmath")
    for phv in (mp.mpf("-0.3"), mp.mpf("0.2")):
        L = lambda tt: mp.e**(pf(tt / Tn) * phv)                # dtau/dt
        fdot = lambda tt: dpf(tt / Tn) / Tn
        fddot = lambda tt: ddpf(tt / Tn) / Tn**2
        ftau_n = lambda tt: fdot(tt) / L(tt)
        ftautau_n = lambda tt: (fddot(tt) - phv * fdot(tt)**2) / L(tt)**2
        pts = [0, Tn / 4, Tn / 2, 3 * Tn / 4, Tn]
        taup = mp.quad(L, pts)
        I1 = mp.quad(lambda tt: ftau_n(tt) * L(tt), pts)          # INT f_tau dtau
        I2 = mp.quad(lambda tt: ftau_n(tt)**2 * L(tt), pts)       # INT f_tau^2 dtau
        Ibp = mp.quad(lambda tt: ftautau_n(tt) * L(tt), pts)      # INT f_tautau dtau
        chk("num", "%-10s phi=%5s: INT f_tau dtau = 1" % (name, mp.nstr(phv, 2)),
            abs(I1 - 1) < mp.mpf(10)**-25)
        chk("num", "%-10s phi=%5s: INT f_tautau dtau = 0 (IBP, H_REST)" % (name, mp.nstr(phv, 2)),
            abs(Ibp) < mp.mpf(10)**-25)
        chk("num", "%-10s phi=%5s: tau_p*INT f_tau^2 = %s > 1" % (name, mp.nstr(phv, 2),
            mp.nstr(taup * I2, 10)), taup * I2 > 1)

print("C7  z3, discrete analogue on R^4")
try:
    import z3
    x = z3.Reals("x1 x2 x3 x4")
    S1 = sum(x)
    S2 = sum(xi * xi for xi in x)
    sol = z3.Solver()
    sol.add(4 * S2 < S1 * S1)
    chk("z3", "4 sum x^2 < (sum x)^2 is UNSAT (C-S / QM-AM)", str(sol.check()), "unsat")
    sol = z3.Solver()
    sol.add(x[0] == 0, x[3] == 0, S1 == 1, 4 * S2 <= 1)
    chk("z3", "rest ends + sum = 1 + 4 sum x^2 <= 1 is UNSAT (strict)", str(sol.check()), "unsat")
    sol = z3.Solver()
    sol.add(S1 == 1, 4 * S2 == 1)
    chk("z3", "VACUITY GUARD: without rest, equality 4 sum x^2 = 1 is SAT", str(sol.check()), "sat")
    sol = z3.Solver()
    sol.add(3 * S2 < S1 * S1)
    chk("z3", "ENCODING GUARD: drifted bound (sum x)^2/3 is refutable (SAT)", str(sol.check()), "sat")
except ImportError:
    print("  z3 not installed: C7 NOT RUN (pip install z3-solver)")
    fails.append("z3 missing")

print("C8  strictness needs omega = ln W_1 != 0 (a hypothesis outside Cauchy-Schwarz)")
W1 = sp.Symbol("W1", positive=True)
cost = -(sp.log(W1)**2) / (8 * sp.pi)   # times INT f_tau^2 > 0
chk("sym", "at W_1 = 1 the transverse time-part cost is exactly 0", cost.subs(W1, 1), 0)
chk("sym", "at W_1 = 1.1 and 0.9 it is < 0",
    all(bool(cost.subs(W1, w) < 0) for w in (sp.Rational(11, 10), sp.Rational(9, 10))))

print("\n%s: %d failure(s)" % ("FAIL" if fails else "ALL CHECKS PASS", len(fails)))
sys.exit(1 if fails else 0)
