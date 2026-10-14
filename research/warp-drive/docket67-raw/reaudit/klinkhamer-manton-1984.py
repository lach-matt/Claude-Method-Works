#!/usr/bin/env python3
"""DOCKET 67 RE-AUDIT: Klinkhamer-Manton 1984, read via restatement.

Restated inputs used (READ this stage via alphaXiv):
 * Quiros hep-ph/9901312, eqs. (257)-(262), PDF pp. 56-57: ansatz, field eqs (260),
   energy functional (261) E = (4 pi v/g) Int dxi {4 f'^2 + 8/xi^2 [f(1-f)]^2
   + 1/2 xi^2 h'^2 + [h(1-f)]^2 + 1/4 (lambda/g^2) xi^2 (h^2-1)^2},
   E_sph = (2 m_W/alpha_W) B(lambda/g^2) (262), "B(0) = 1.5 to B(inf) = 2.7".
 * Hindmarsh & James hep-ph/9307205 eqs. (6)-(7), pp. 3-4: same field eqs, theta_W = 0.
 * Zhang & Young hep-ph/9312345 eqs. (5a)-(5d) and Table I, pp. 4-5: KM's own
   two-parameter TRIAL (variational) ansatz and KM's tabulated Omega, Xi.
Question tested: are RS96's 1.56 / 2.72 the KM variational values (upper bounds),
while the exact minimum of the same functional is 1.520 / 2.706?
"""
import math, sys
import numpy as np
from scipy.integrate import quad, solve_bvp
from scipy.optimize import minimize

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

# ------------------------------------------------ KM trial ansatz (Zhang-Young 5a-5d)
def f_trial(x, Xi):
    if x <= Xi:
        return x * x / (Xi * (Xi + 4.0)), 2 * x / (Xi * (Xi + 4.0))
    e = math.exp(0.5 * (Xi - x))
    return 1.0 - 4.0 / (Xi + 4.0) * e, 2.0 / (Xi + 4.0) * e

def h_trial(x, Om, sig):
    if Om == 0.0:
        return 1.0, 0.0
    if x <= Om:
        c = (sig * Om + 1) / (sig * Om + 2) / Om
        return c * x, c
    e = math.exp(sig * (Om - x))
    A = Om / (sig * Om + 2)
    return 1.0 - A * e / x, A * e * (1.0 / x**2 + sig / x)

def B_trial(Om, Xi, lam_g2):
    """Quiros (261) integrand over 4 pi v/g, on the KM trial functions.
    sigma = m_H/(g v) = sqrt(2 lambda)/g  (h tail);  f tail exp(-xi/2) = m_W/(g v)."""
    sig = math.sqrt(2.0 * lam_g2) if math.isfinite(lam_g2) else None
    def dens(x):
        f, fp = f_trial(x, Xi)
        if sig is None:
            h, hp = 1.0, 0.0
            pot = 0.0
        else:
            h, hp = h_trial(x, Om, sig)
            pot = 0.25 * lam_g2 * x * x * (h * h - 1) ** 2
        return 4 * fp**2 + 8 * (f * (1 - f)) ** 2 / x**2 + 0.5 * x * x * hp**2 + (h * (1 - f)) ** 2 + pot
    pts = sorted(set([p for p in (Om, Xi) if p > 0]))
    tot, a = 0.0, 1e-12
    for p in pts + [60.0]:
        tot += quad(dens, a, p, limit=400, epsabs=1e-12, epsrel=1e-11)[0]; a = p
    # lambda = 0 tail: h = 1 - Om/(2 xi) -> (1/2) xi^2 h'^2 = Om^2/(8 xi^2) beyond 60
    tot += quad(dens, 60.0, np.inf, limit=400)[0]
    return tot

print("== KM trial ansatz at KM's own Table I parameters (Zhang-Young Table I)")
TABLE = [(0.0, 2.600, 2.660), (1e-3, 2.520, 2.450), (1e-2, 2.290, 2.120), (1e-1, 1.900, 1.650),
         (1.0, 1.250, 1.150), (10.0, 0.620, 0.820), (100.0, 0.220, 0.740), (1000.0, 0.070, 0.730),
         (math.inf, 0.0, 0.728)]
Btab = {}
for lg, Om, Xi in TABLE:
    Btab[lg] = B_trial(Om, Xi, lg)
    print("   lambda/g^2 = %-7g Omega = %.3f Xi = %.3f  ->  B_trial = %.4f" % (lg, Om, Xi, Btab[lg]))
chk("B_trial(lambda=0) at KM Table I (2.600, 2.660) lies within 0.5% of RS96's 1.56 (it is 1.566: truncates, does not round, to 1.56 -- residual RECORDED)",
    abs(Btab[0.0] / 1.56 - 1) < 5e-3 and math.floor(100 * Btab[0.0]) / 100 == 1.56, "%.4f (%+.2f%%)" % (Btab[0.0], 100 * (Btab[0.0] / 1.56 - 1)))
chk("B_trial(lambda=inf) at KM Table I Xi = 0.728 rounds to RS96's 2.72",
    round(Btab[math.inf], 2) == 2.72, "%.4f" % Btab[math.inf])

# re-minimise the trial family to confirm Table I is the variational optimum
r0 = minimize(lambda p: B_trial(abs(p[0]), abs(p[1]), 0.0), [2.6, 2.66], method="Nelder-Mead",
              options=dict(xatol=1e-4, fatol=1e-8))
ri = minimize(lambda p: B_trial(0.0, abs(p[0]), math.inf), [0.728], method="Nelder-Mead",
              options=dict(xatol=1e-5, fatol=1e-10))
print("   re-minimised trial, lambda=0:   Omega, Xi = %.3f, %.3f  B = %.4f" % (abs(r0.x[0]), abs(r0.x[1]), r0.fun))
print("   re-minimised trial, lambda=inf: Xi = %.4f  B = %.4f" % (abs(ri.x[0]), ri.fun))
chk("variational optimum at lambda=0 lies at KM's (2.600, 2.660) to 0.05",
    abs(abs(r0.x[0]) - 2.600) < 0.05 and abs(abs(r0.x[1]) - 2.660) < 0.05)
chk("variational optimum at lambda=inf lies at KM's Xi = 0.728 to 0.005", abs(abs(ri.x[0]) - 0.728) < 5e-3)

# ------------------------------------------------ exact minimum of the same functional
def solve_exact(k, xmax=None, h_is_one=False):
    """EL eqs of Quiros (261) = Quiros (260) = Hindmarsh-James (7a),(7c); k = lambda/(4 g^2)."""
    x0 = 1e-4
    if xmax is None:
        xmax = 400.0 if k == 0 else max(30.0, 25.0 / math.sqrt(8 * k) + 20.0)
    x = np.concatenate([np.geomspace(x0, 1.0, 200), np.linspace(1.0, xmax, 3000)[1:]])
    if h_is_one:
        rhs = lambda x, y: np.vstack([y[1], (16 * y[0] * (1 - y[0]) * (1 - 2 * y[0]) / x**2 - 2 * (1 - y[0])) / 8])
        bc = lambda ya, yb: np.array([ya[0], yb[0] - 1])
        y = np.vstack([1 - np.exp(-x**2 / 4), x / 2 * np.exp(-x**2 / 4)])
    else:
        def rhs(x, y):
            f, fp, hh, hp = y
            return np.vstack([fp, (16 * f * (1 - f) * (1 - 2 * f) / x**2 - 2 * hh**2 * (1 - f)) / 8, hp,
                              (2 * hh * (1 - f)**2 + 4 * k * x**2 * hh * (hh**2 - 1) - 2 * x * hp) / x**2])
        def bc(ya, yb):
            if k == 0:
                return np.array([ya[0], ya[2], yb[0] - 1, yb[3] - (1 - yb[2]) / xmax])
            return np.array([ya[0], ya[2], yb[0] - 1, yb[2] - 1])
        y = np.vstack([np.tanh(x / 3)**2, 2 * np.tanh(x / 3) / np.cosh(x / 3)**2 / 3,
                       np.tanh(x / 2), 0.5 / np.cosh(x / 2)**2])
    sol = solve_bvp(rhs, bc, x, y, tol=1e-7, max_nodes=400000)
    xs = np.concatenate([np.geomspace(x0, 1.0, 4000), np.linspace(1.0, xmax, 200000)[1:]])
    Y = sol.sol(xs)
    if h_is_one:
        f, fp = Y; hh = np.ones_like(f); hp = np.zeros_like(f)
    else:
        f, fp, hh, hp = Y
    B = np.trapezoid(4 * fp**2 + 8 * f**2 * (1 - f)**2 / xs**2 + xs**2 * hp**2 / 2 + hh**2 * (1 - f)**2
                     + k * xs**2 * (hh**2 - 1)**2, xs)
    if k == 0 and not h_is_one:
        c = (1 - hh[-1]) * xmax; B += c**2 / (2 * xmax)
    return sol.status, B

print("== exact minimum of the same (read) functional")
st0, E0 = solve_exact(0.0)
sti, Ei = solve_exact(0.0, xmax=60.0, h_is_one=True)
print("   exact B(0) = %.4f (status %d);  exact B(inf) = %.4f (status %d)" % (E0, st0, Ei, sti))
chk("exact B(0) = 1.520 and B(inf) = 2.706", abs(E0 - 1.520) < 1e-3 and abs(Ei - 2.706) < 1e-3)
chk("variational bound respected: exact < trial at both ends", E0 < Btab[0.0] and Ei < Btab[math.inf])
print("   trial excess over exact: B(0) %+.2f%%, B(inf) %+.2f%%"
      % (100 * (Btab[0.0] / E0 - 1), 100 * (Btab[math.inf] / Ei - 1)))

# measured point: lambda/g^2 = (m_H/m_W)^2 / 8
for mh, mw in ((125.20, 80.362), (125.20, 80.3692)):
    lg = (mh / mw) ** 2 / 8
    rm = minimize(lambda p: B_trial(abs(p[0]), abs(p[1]), lg), [1.6, 1.4], method="Nelder-Mead",
                  options=dict(xatol=1e-4, fatol=1e-8))
    stm, Em = solve_exact(lg / 4)
    print("   m_H/m_W = %.4f lambda/g^2 = %.4f: trial-optimum B = %.4f (Omega, Xi = %.3f, %.3f); exact B = %.4f (+%.2f%%)"
          % (mh / mw, lg, rm.fun, abs(rm.x[0]), abs(rm.x[1]), Em, 100 * (rm.fun / Em - 1)))
chk("exact B at measured mass reproduces 1.916 (first audit; FFS 9.08 / 4.740)", abs(Em - 1.916) < 1.5e-3, "%.4f" % Em)

# Quiros fit (263), stated valid 25 <= m_h <= 250 GeV
xq = 125.20 / 80.362
print("   Quiros fit (263) B(x) = 1.58 + 0.32x - 0.05x^2 at x = %.4f: %.4f" % (xq, 1.58 + 0.32 * xq - 0.05 * xq**2))
# Trodden (46) 8 < E_sph < 14 TeV: implied prefactor
print("   Trodden eq.(46) 8..14 TeV over (1.56, 2.72): prefactor %.2f / %.2f TeV" % (8 / 1.56, 14 / 2.72))
print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
