#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Fewster & Osterbrink arXiv:0708.2450v2 Sec. 3
(massless scalar, xi > 0, 4D Minkowski), and a test of the warp board's ledger
O1 figures E_pos/|E_neg| = 3 pi/(32 f xi c0^3) >= 1039.13 (xi=1/4), >= 1803.55
(xi=1/6), which the tree says come 'from Fewster & Osterbrink's own construction'
and which no instrument in the tree re-derives (f and c0 are defined nowhere).

Everything here is computed from FO's printed definitions:
  h_kappa(k) = 4 pi sqrt2 (kappa - |k|/3) e^{-|k|/kappa} / kappa^2      (their 25)
  d mu(k)    = d^3k / ((2 pi)^3 2|k|)                                  (their 15)
  F(t,x)     = <Omega|Phi(t,x) Psi> = int dmu e^{-i(t|k| - k.x)} h(k)  (their 25)
  rho        = |d_t F|^2 + (1-4xi)|grad F|^2 - 4 xi Re(conj F d_t^2 F)  (their 24)
Units: kappa = 1 unless stated (their scaling relation (27) restores it).
Run: python3 0708.2450.py      (exit 0 = every CHECK passed; prints findings)
"""
import sys
import sympy as sp
import numpy as np

ok = True
def check(label, cond):
    global ok
    ok &= bool(cond)
    print(("  PASS  " if cond else "  FAIL  ") + label)

k, r, t, xi, kap, s = sp.symbols('k r t xi kappa s', positive=True)
pi = sp.pi

print("1. normalisation and energy of Psi_kappa (FO eq. 25-26)")
h = 4*pi*sp.sqrt(2)*(kap - k/3)*sp.exp(-k/kap)/kap**2
# ||h||^2 = int d^3k/((2pi)^3 2k) |h|^2 = (1/(4 pi^2)) int_0^oo k |h|^2 dk
norm = sp.simplify(sp.integrate(k*h**2, (k, 0, sp.oo))/(4*pi**2))
energy = sp.simplify(sp.integrate(k**2*h**2, (k, 0, sp.oo))/(4*pi**2))
print("     ||h||^2 =", norm, "   <H> =", energy)
check("||h_kappa|| = 1", sp.simplify(norm - 1) == 0)
check("<Psi_kappa|H Psi_kappa> = 2 kappa/3 (FO 26)", sp.simplify(energy - 2*kap/3) == 0)

print("2. the one-particle wave function in closed form (kappa = 1)")
# angular integral: int dOmega e^{i k.x} = 4 pi sin(kr)/(kr)
#   F = 1/(4 pi^2 r) int_0^oo sin(kr) e^{-k s} h(k) dk,  s = 1 + i t
I0 = sp.integrate(sp.sin(k*r)*sp.exp(-k*s), (k, 0, sp.oo), conds='none')
I1 = sp.integrate(k*sp.sin(k*r)*sp.exp(-k*s), (k, 0, sp.oo), conds='none')
F_s = sp.simplify(4*pi*sp.sqrt(2)*(I0 - I1/3)/(4*pi**2*r))
F_closed = sp.sqrt(2)/pi*(1/(s**2 + r**2) - 2*s/(3*(s**2 + r**2)**2))
check("F(s,r) = (sqrt2/pi)[1/(s^2+r^2) - 2s/(3(s^2+r^2)^2)]",
      sp.simplify(F_s - F_closed) == 0)

tt, rr = sp.symbols('t r', real=True)
Fx = F_closed.subs(s, 1 + sp.I*tt).subs(r, rr)
Ft = sp.diff(Fx, tt); Ftt = sp.diff(Fx, tt, 2); Fr = sp.diff(Fx, rr)
def re(z): return (z + sp.conjugate(z))/2
def ab2(z): return z*sp.conjugate(z)
rho = ab2(Ft) + (1 - 4*xi)*ab2(Fr) - 4*xi*re(sp.conjugate(Fx)*Ftt)

print("3. energy density at the spatial origin (FO eq. 28) and at the spacetime origin (29)")
rho0t = sp.simplify(sp.expand_complex(rho.subs(rr, 0)))
fo28 = 8/(3*(1 + tt**2)**5*pi**2)*((3*tt**4 + 3*tt**2) - xi*(18*tt**4 - 44*tt**2 + 2))
check("rho(t,0) = FO (28) with kappa=1, identically in t and xi", sp.simplify(rho0t - fo28) == 0)
rho00 = sp.simplify(rho0t.subs(tt, 0))
check("rho(0,0) = -xi (2 kappa)^4/(3 pi^2) (FO 29)", sp.simplify(rho00 + xi*16/(3*pi**2)) == 0)

print("4. the j-particle step (FO 32-34): arithmetic as printed")
kp, rho_0, tau, taup = sp.symbols("kappa' rho_0 tau tau'", positive=True)
thresh = xi*(2*kp)**4/(6*pi**2)          # (30)/(32): rho <= -thresh on the ball
j_printed = 6*pi**2*rho_0/(xi*kp**4)     # FO: 'choose an integer j > ...'
j_needed = sp.simplify(rho_0/thresh)     # j*thresh > rho_0 is what (33) needs
print("     j printed  >", j_printed, "   j needed >", j_needed,
      "   ratio =", sp.simplify(j_printed/j_needed))
check("printed j exceeds the needed j (sufficient: (33) still holds), by 16 = 2^4",
      sp.simplify(j_printed/j_needed - 16) == 0)
E_from_printed_j = sp.simplify(2*j_printed*kp/3)
print("     2 j kappa'/3 at the printed j =", E_from_printed_j,
      " ; FO print  > 2 pi^2 rho_0/(xi kappa'^3)")
check("FO (34) lower bound 2pi^2 rho0/(xi k'^3) is below 2jk'/3 at their j (true, loose by 2)",
      sp.simplify(E_from_printed_j/(2*pi**2*rho_0/(xi*kp**3)) - 2) == 0)
E_min = sp.simplify(2*j_needed*kp/3)
print("     the minimum total energy the construction needs = ", E_min)
check("(34) tau-form: 1/kappa'^3 = tau'^3/(kappa tau)^3 with kappa' = kappa tau/tau'",
      sp.simplify((1/kp**3).subs(kp, kap*tau/taup) - taup**3/(kap*tau)**3) == 0)
check("FO 'energy density less than -xi k^4 tau^4/(6 pi^2 tau'^4)': true, 16x weaker than (32)",
      sp.simplify(thresh.subs(kp, kap*tau/taup)/(xi*kap**4*tau**4/(6*pi**2*taup**4)) - 16) == 0)

print("5. theorem content: for every xi > 0 the construction gives rho < -rho_0 on any ball")
check("rho(0,0) < 0 for every xi > 0 (sign of -16 xi/(3 pi^2))",
      sp.ask(sp.Q.negative(rho00), sp.Q.positive(xi)) is True)
# massless ONLY: with m > 0, h_kappa's scaling relation (27) fails because
# omega(k) = sqrt(k^2+m^2) breaks the homogeneity; the ball-enlarging step
# kappa' = kappa tau/tau' is a massless step.  (Stated, not computed: FO do not
# treat m > 0 in Sec. 3; see report.)

print("6. the ledger O1 figures: 3 pi/(32 f xi c0^3)")
rho_num = sp.lambdify((tt, rr, xi), rho, 'numpy')
def rho_np(T, R, x):
    return np.real(rho_num(T, R, x))
# identity behind the formula: one particle, E_pos := <H> = 2/3 (kappa=1);
# |E_neg| := (threshold f*|rho(0,0)|) x (volume of the spatial ball radius c0)
f_, c0_ = sp.symbols('f c0', positive=True)
ratio_formula = sp.simplify((sp.Rational(2, 3)) /
                            (f_*16*xi/(3*pi**2)*sp.Rational(4, 3)*pi*c0_**3))
check("(2 kappa/3)/[f |rho(0,0)| (4pi/3)(c0/kappa)^3] == 3 pi/(32 f xi c0^3)",
      sp.simplify(ratio_formula - 3*pi/(32*f_*xi*c0_**3)) == 0)
print("     => f is a fraction of the peak |rho(0,0)|, c0 = kappa*tau a ball radius.")

T = np.linspace(-3, 3, 1201); R = np.linspace(0, 3, 601)
TT, RR = np.meshgrid(T, R, indexing='ij')
def c0_of(f, x, spacetime=True):
    val = rho_np(TT, RR, x)
    thr = -f*16*x/(3*np.pi**2)
    bad = val > thr
    if spacetime:
        d = np.sqrt(TT**2 + RR**2)
    else:
        d = np.where(np.abs(TT) < 1e-12, RR, np.inf)
    return float(np.min(d[bad])) if bad.any() else np.inf

def c0_fine(f, x, spacetime=True):
    # refine by bisection on radius: max tau s.t. sup_{ball} rho <= thr
    thr = -f*16*x/(3*np.pi**2)
    th = np.linspace(0, np.pi, 721)      # (t, r) = tau (cos th, sin th), r >= 0
    def sup_on_sphere(tau):
        if spacetime:
            return np.max(rho_np(tau*np.cos(th), tau*np.sin(th), x))
        return float(rho_np(0.0, tau, x))
    lo, hi = 0.0, 3.0
    # sup over the ball = max over spheres of radius <= tau: scan monotone envelope
    taus = np.linspace(1e-4, 3, 3001)
    sups = np.array([sup_on_sphere(u) for u in taus])
    env = np.maximum.accumulate(sups)
    idx = np.argmax(env > thr)
    if env[-1] <= thr:
        return np.inf
    lo, hi = taus[idx-1], taus[idx]
    for _ in range(50):
        mid = 0.5*(lo+hi)
        if max(env[idx-1], sup_on_sphere(mid)) > thr:
            hi = mid
        else:
            lo = mid
    return lo

results = {}
for x, label, target in ((0.25, "1/4", 1039.13), (1/6, "1/6", 1803.55)):
    for geom in (True, False):
        best = None
        for f in np.linspace(0.02, 0.98, 49):
            c0 = c0_fine(f, x, geom)
            R_ = 3*np.pi/(32*f*x*c0**3)
            if best is None or R_ < best[0]:
                best = (R_, f, c0)
        c0h = c0_fine(0.5, x, geom)
        Rh = 3*np.pi/(32*0.5*x*c0h**3)
        results[(label, geom)] = (best, Rh, c0h)
        print("     xi=%s %-9s: min_f 3pi/(32 f xi c0^3) = %.2f at f=%.2f (c0=%.5f);"
              " at FO's f=1/2: c0=%.5f -> %.2f   [ledger: %.2f]"
              % (label, "spacetime" if geom else "t=0 slice", best[0], best[1],
                 best[2], c0h, Rh, target))


print("6b. refine f (bounded scalar minimisation) and compare with the ledger")
from scipy.optimize import minimize_scalar
for x, label, target in ((0.25, "1/4", 1039.13), (1/6, "1/6", 1803.55)):
    obj = lambda f: 3*np.pi/(32*f*x*c0_fine(f, x, True)**3)
    res = minimize_scalar(obj, bounds=(0.30, 0.46), method='bounded', options={'xatol': 1e-4})
    c0 = c0_fine(res.x, x, True)
    print("     xi=%s: min = %.3f at f = %.4f, c0 = %.6f ; ledger %.2f ; rel diff %.2e"
          % (label, res.fun, res.x, c0, target, res.fun/target - 1))
    results[("min", label)] = (res.fun, res.x, c0)
    check("xi=%s: ledger O1 figure reproduced (spacetime ball B(tau) of FO (31), min over f) to 0.05%%" % label,
          abs(res.fun/target - 1) < 5e-4)

print("7. the TRUE negative energy on the t = 0 slice, one particle, kappa = 1")
from scipy.integrate import quad
from scipy.optimize import brentq
for x, label in ((0.25, "1/4"), (1/6, "1/6")):
    g = lambda u: rho_np(0.0, u, x)
    # first zero of rho(0,r)
    grid = np.linspace(1e-6, 10, 20001); vals = g(grid)
    sgn = np.where(np.diff(np.sign(vals)) != 0)[0]
    zeros = [brentq(g, grid[i], grid[i+1]) for i in sgn]
    neg = 0.0; a = 0.0
    edges = [0.0] + zeros + [60.0]
    for lo_, hi_ in zip(edges[:-1], edges[1:]):
        mid = 0.5*(lo_+hi_)
        if g(mid) < 0:
            neg += quad(lambda u: 4*np.pi*u*u*g(u), lo_, hi_, limit=200)[0]
    tot = quad(lambda u: 4*np.pi*u*u*g(u), 0, 200, limit=400)[0]
    print("     xi=%s: zeros of rho(0,r) at r=%s ; int_{rho<0} rho d^3x = %.6f ;"
          " int rho d^3x = %.6f (<H> = %.6f) ; <H>/|E_neg| = %.4f"
          % (label, ["%.5f" % z for z in zeros], neg, tot, 2/3, (2/3)/abs(neg)))
    check("xi=%s: integral of rho over the t=0 slice equals <H> = 2/3 (xi-terms are divergences)"
          % label, abs(tot - 2/3) < 1e-6)
    results[("true", label)] = (2/3)/abs(neg)

print("7b. other time slices (t in [0,2]): is t = 0 the slice with the most negative energy?")
for x, label in ((0.25, "1/4"), (1/6, "1/6")):
    best = 0.0
    for T in np.linspace(0, 2, 41):
        fn = lambda u: 4*np.pi*u*u*min(rho_np(T, u, x), 0.0)
        n = sum(quad(fn, a_, b_, limit=200)[0] for a_, b_ in [(0, 0.5), (0.5, 2), (2, 10), (10, 100)])
        best = min(best, n)
    print("     xi=%s: most negative slice E_neg = %.6f -> <H>/|E_neg| = %.3f" % (label, best, (2/3)/abs(best)))
    check("xi=%s: ledger figure exceeds the state's actual <H>/|E_neg| on every slice t in [0,2] by > 10x" % label,
          results[("min", label)][0] > 10*(2/3)/abs(best))

print()
print("SUMMARY")
print("  FO Sec. 3 re-derived: (26), (28), (29) exact; (33) holds; (34) and the")
print("  printed threshold are TRUE but loose (a dropped 2^4 in j, a factor 2 in (34)).")
for label in ("1/4", "1/6"):
    b_st, Rh_st, _ = results[(label, True)]
    b_sl, Rh_sl, _ = results[(label, False)]
    print("  xi=%s: formula min over f: spacetime ball %.2f, t=0 ball %.2f ; true <H>/|E_neg| = %.3f"
          % (label, b_st[0], b_sl[0], results[("true", label)]))
sys.exit(0 if ok else 1)
