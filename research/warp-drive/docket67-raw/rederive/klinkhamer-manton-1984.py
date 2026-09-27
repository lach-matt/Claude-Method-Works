#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Klinkhamer-Manton 1984 sphaleron energy
   E_sph = (4 pi v / g) B(lambda/g^2) = (2 m_W/alpha_W) B(m_H/m_W),  B from 1.56 to 2.72.

The KM paper (PRD 30, 2212) was NOT read in this run (arXiv/alphaXiv unreachable: egress
403 and alphaXiv quota).  The reduced energy functional below is RECONSTRUCTED from the
standard spherically symmetric theta_W = 0 ansatz (A_i ~ f(xi), Phi = (v/sqrt2) h(xi) U,
xi = g v r) -- its Higgs-potential and Higgs-kinetic prefactors are re-derived here in sympy
from V = lambda (Phi^+Phi - v^2/2)^2, m_W = g v/2, m_H^2 = 2 lambda v^2.  The gauge terms
(4 f'^2 + 8 f^2 (1-f)^2/xi^2) and the covariant cross term h^2 (1-f)^2 are taken as the
standard form and are CHECKED only through the outputs (three independent numbers the tree
holds READ: 1.56, 2.72 and ~1.91 at the measured m_H) and through Derrick's virial identity.

Stdlib + numpy + scipy + sympy.  Exits 1 if a check fails.
"""
import math, sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_bvp, quad
from scipy.interpolate import CubicSpline

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)

# ---------------------------------------------------------------- 1. sympy: prefactors
r, xi, g, v, lam, mW, mH = sp.symbols("r xi g v lambda m_W m_H", positive=True)
h = sp.Function("h")
# potential: V = lam (Phi^+Phi - v^2/2)^2 with Phi^+Phi = v^2 h^2/2
V = lam * (v**2 * h(xi)**2 / 2 - v**2 / 2)**2
# energy element 4 pi r^2 dr with r = xi/(g v)
jac = 4 * sp.pi * (xi / (g * v))**2 / (g * v)
pot = sp.simplify(jac * V / (4 * sp.pi * v / g))
target_pot = lam / (4 * g**2) * xi**2 * (h(xi)**2 - 1)**2
chk("Higgs potential term = (lambda/4g^2) xi^2 (h^2-1)^2 in units 4 pi v/g",
    sp.simplify(pot - target_pot) == 0)
# kinetic: |d_r Phi|^2 = (v^2/2) h'(r)^2, d/dr = g v d/dxi
kin = sp.simplify(jac * (v**2 / 2) * (g * v)**2 * sp.Derivative(h(xi), xi)**2 / (4 * sp.pi * v / g))
chk("Higgs kinetic term = (xi^2/2) h'^2 in units 4 pi v/g",
    sp.simplify(kin - xi**2 / 2 * sp.Derivative(h(xi), xi)**2) == 0)
# prefactor identities
aW = g**2 / (4 * sp.pi)
chk("2 m_W/alpha_W = 4 pi v/g at m_W = g v/2",
    sp.simplify((2 * (g * v / 2) / aW) - 4 * sp.pi * v / g) == 0)
chk("4 pi v/g = 2 pi v^2/m_W at g = 2 m_W/v",
    sp.simplify((4 * sp.pi * v / g).subs(g, 2 * mW / v) - 2 * sp.pi * v**2 / mW) == 0)
chk("lambda/(4 g^2) = (m_H/m_W)^2/32 at m_H^2 = 2 lambda v^2",
    sp.simplify((lam / (4 * g**2)).subs(lam, mH**2 / (2 * v**2)).subs(g, 2 * mW / v)
                - (mH / mW)**2 / 32) == 0)

# ---------------------------------------------------------------- 2. numeric B(k)
def L_density(x, f, fp, hh, hp, k):
    return (4 * fp**2 + 8 * f**2 * (1 - f)**2 / x**2
            + x**2 * hp**2 / 2 + hh**2 * (1 - f)**2 + k * x**2 * (hh**2 - 1)**2)

def parts(x, f, fp, hh, hp, k):
    Eg = np.trapezoid(4 * fp**2 + 8 * f**2 * (1 - f)**2 / x**2, x)
    Ek = np.trapezoid(x**2 * hp**2 / 2, x)
    Em = np.trapezoid(hh**2 * (1 - f)**2, x)
    Ep = np.trapezoid(k * x**2 * (hh**2 - 1)**2, x)
    return Eg, Ek, Em, Ep

def solve(k, xmax=None, h_is_one=False, guess=None):
    """EL equations of the reduced functional:
       8 f'' = 16 f(1-f)(1-2f)/xi^2 - 2 h^2 (1-f)
       (xi^2 h')' = 2 h (1-f)^2 + 4 k xi^2 h (h^2 - 1)"""
    x0 = 1e-4
    if xmax is None:
        xmax = 400.0 if k == 0 else max(30.0, 25.0 / math.sqrt(8 * k) + 20.0)
    x = np.concatenate([np.geomspace(x0, 1.0, 200), np.linspace(1.0, xmax, 3000)[1:]])
    if h_is_one:
        def rhs(x, y):
            f, fp = y
            return np.vstack([fp, (16 * f * (1 - f) * (1 - 2 * f) / x**2 - 2 * (1 - f)) / 8])
        def bc(ya, yb):
            return np.array([ya[0], yb[0] - 1])
        y = np.vstack([1 - np.exp(-x**2 / 4), x / 2 * np.exp(-x**2 / 4)])
    else:
        def rhs(x, y):
            f, fp, hh, hp = y
            fpp = (16 * f * (1 - f) * (1 - 2 * f) / x**2 - 2 * hh**2 * (1 - f)) / 8
            hpp = (2 * hh * (1 - f)**2 + 4 * k * x**2 * hh * (hh**2 - 1) - 2 * x * hp) / x**2
            return np.vstack([fp, fpp, hp, hpp])
        def bc(ya, yb):
            if k == 0:   # massless Higgs: far field h = 1 - c/xi  =>  h' = (1-h)/xi
                return np.array([ya[0], ya[2], yb[0] - 1, yb[3] - (1 - yb[2]) / xmax])
            return np.array([ya[0], ya[2], yb[0] - 1, yb[2] - 1])
        if guess is None:
            y = np.vstack([np.tanh(x / 3)**2, 2 * np.tanh(x / 3) / np.cosh(x / 3)**2 / 3,
                           np.tanh(x / 2), 0.5 / np.cosh(x / 2)**2])
        else:
            y = guess(x)
    sol = solve_bvp(rhs, bc, x, y, tol=1e-7, max_nodes=400000)
    xs = np.concatenate([np.geomspace(x0, 1.0, 4000), np.linspace(1.0, xmax, 200000)[1:]])
    Y = sol.sol(xs)
    if h_is_one:
        f, fp = Y; hh = np.ones_like(f); hp = np.zeros_like(f)
    else:
        f, fp, hh, hp = Y
    Eg, Ek, Em, Ep = parts(xs, f, fp, hh, hp, k)
    B = Eg + Ek + Em + Ep
    if k == 0 and not h_is_one:
        # tail beyond xmax: h = 1 - c/xi, f = 1 (exp.), only xi^2 h'^2/2 = c^2/(2 xi^2) survives
        c = (1 - hh[-1]) * xmax
        B += c**2 / (2 * xmax)
    return sol.status, B, (Eg, Ek, Em, Ep), sol

results = {}
# k -> 0 limit (massless Higgs): KM's B(0)
st, B0, p0, sol0 = solve(0.0)
results["B(m_H/m_W=0)"] = B0
chk("solve_bvp converged at m_H = 0", st == 0, "status %d" % st)
# Derrick virial at k=0: E_gauge = E_kin_h + E_mix (scaling xi -> mu xi)
vir0 = p0[0] - (p0[1] + p0[2] + 3 * p0[3])
chk("Derrick virial at m_H = 0 (E_gauge - E_kin - E_mix - 3E_pot ~ 0)", abs(vir0) < 2e-2 * B0,
    "residual %.2e (B = %.4f; tail of E_kin beyond xmax not in the residual)" % (vir0, B0))

# k -> infinity: h = 1 for xi > 0
st, Binf, pinf, _ = solve(0.0, xmax=60.0, h_is_one=True)
results["B(m_H/m_W=inf), h=1"] = Binf
chk("solve_bvp converged at m_H = infinity (h = 1)", st == 0)

# large-k sequence approaching the h = 1 limit
for ratio in (1.0, 1.5578, 3.0, 5.0, 10.0, 20.0):
    k = ratio**2 / 32
    st, B, p, _ = solve(k)
    vir = p[0] - (p[1] + p[2] + 3 * p[3])
    results["B(m_H/m_W=%.4g)" % ratio] = B
    print("   m_H/m_W = %-7.4g k = %-9.5f B = %.4f  status %d  virial residual %.1e"
          % (ratio, k, B, st, vir))
    chk("virial at m_H/m_W = %g" % ratio, abs(vir) < 1e-3 * B)

for k_, v_ in results.items():
    print("   %-26s %.4f" % (k_, v_))

# convergence of the two endpoints (the tail of E_kin at k = 0 is added analytically)
B0s = [solve(0.0, xmax=xm)[1] for xm in (100.0, 400.0, 1000.0)]
chk("B(0) converged in xmax (100, 400, 1000)", max(B0s) - min(B0s) < 1e-4, " ".join("%.5f" % b for b in B0s))
Bis = [solve(0.0, xmax=xm, h_is_one=True)[1] for xm in (20.0, 60.0, 120.0)]
chk("B(inf) converged in xmax (20, 60, 120)", max(Bis) - min(Bis) < 1e-4, " ".join("%.5f" % b for b in Bis))
# continuation toward the h = 1 limit: B(k) must stay below B(inf) and rise toward it
prev = None; seq = []
for ratio in (20.0, 30.0, 45.0, 70.0, 100.0):
    k = ratio**2 / 32
    guess = None if prev is None else (lambda x, S=prev: S.sol(np.clip(x, S.x[0], S.x[-1])))
    st, B, p, prev = solve(k, xmax=40.0, guess=guess)
    seq.append((ratio, st, B))
    print("   continuation m_H/m_W = %-5g status %d B = %.4f" % (ratio, st, B))
okseq = [b for (_r, st, b) in seq if st == 0]
chk("continuation: B rises monotonically and stays below B(inf)",
    all(a < b for a, b in zip(okseq, okseq[1:])) and all(b < Binf for b in okseq), "%d converged" % len(okseq))
# DISCREPANCY, recorded not repaired: the restated endpoints against the computed minima
print("   DISCREPANCY  B(0): restated 1.56, computed %.4f (%.2f%% below)" % (B0, 100 * (1.56 - B0) / 1.56))
print("   DISCREPANCY  B(inf): restated 2.72, computed %.4f (%.2f%% below)" % (Binf, 100 * (2.72 - Binf) / 2.72))
chk("computed endpoints lie BELOW the restated ones (consistent with the restated being upper estimates)",
    B0 < 1.56 and Binf < 2.72)
chk("computed B(0) = 1.520 and B(inf) = 2.706 (3 decimals)", abs(B0 - 1.520) < 5e-4 and abs(Binf - 2.706) < 5e-4,
    "%.5f %.5f" % (B0, Binf))
Bm = results["B(m_H/m_W=1.558)"]
chk("B at measured m_H/m_W = 1.916 (FFS 9.08/4.74 = 1.916; TW 1.31 + 0.60 = 1.91)", abs(Bm - 1.916) < 1e-3, "%.4f" % Bm)
chk("B at measured m_H/m_W lies inside [1.56, 2.72]", 1.56 < Bm < 2.72, "%.4f" % Bm)
chk("B monotone increasing in m_H/m_W over the sample",
    all(a < b for a, b in zip([B0] + [results["B(m_H/m_W=%.4g)" % r_] for r_ in (1.0, 1.5578, 3.0, 5.0, 10.0, 20.0)],
                              [results["B(m_H/m_W=%.4g)" % r_] for r_ in (1.0, 1.5578, 3.0, 5.0, 10.0, 20.0)] + [Binf])))

# where the restated lower end 1.56 is actually reached
from scipy.optimize import brentq
r156 = brentq(lambda r_: solve(r_**2 / 32)[1] - 1.56, 0.02, 0.5, xtol=1e-4)
print("   computed B = 1.56 at m_H/m_W = %.4f (m_H = %.2f GeV at m_W = 80.3692)" % (r156, r156 * 80.3692))
chk("the bracket [1.56, 2.72] holds for m_H/m_W >= %.3f, which includes the measured 1.558" % r156,
    r156 < 1.5578)

# ---------------------------------------------------------------- 3. data and prefactor
def pref_tev(mw, vv):
    return 2 * math.pi * vv**2 / mw / 1000.0

tree_mw, tree_v = 80.362, 246.21964023926205       # massform.M_W_GEV, higgs.vev()
p_tree = pref_tev(tree_mw, tree_v)
chk("tree prefactor 2 m_W/alpha_W reproduces 4.740 TeV", abs(p_tree - 4.740) < 5e-4, "%.5f TeV" % p_tree)
print("   E_sph at tree prefactor x B(measured) = %.3f TeV  (tree holds READ 9.08 FFS / 9.11 TW)"
      % (p_tree * Bm))
print("   E_sph bracket from KM range: %.3f to %.3f TeV" % (p_tree * 1.56, p_tree * 2.72))
# sensitivity to the moved/contested data: m_W across CDF-2022 (80.4335) to CMS-2024 (80.3602),
# m_H 124..126; v from G_F (moves < 1e-6 relative)
lo, hi = None, None
for mw in (80.3602, 80.362, 80.3692, 80.377, 80.4335):
    for rat_mh in (124.0, 125.2, 126.0):
        k = (rat_mh / mw)**2 / 32
        st, B, p, _ = solve(k)
        E = pref_tev(mw, tree_v) * B
        lo = E if lo is None else min(lo, E); hi = E if hi is None else max(hi, E)
print("   E_sph over m_W in [80.3602, 80.4335], m_H in [124, 126]: %.4f .. %.4f TeV (spread %.2f%%)"
      % (lo, hi, 100 * (hi - lo) / lo))
chk("E_sph moves < 1% across every m_W / m_H value in play", (hi - lo) / lo < 0.01)
# scheme sensitivity of alpha_W: g from 2 m_W/v vs alpha(m_Z)/sin^2 theta_W (1/29 of RS96)
print("   alternative prefactor 2 m_W/alpha_W at alpha_W = 1/29 (RS96's value): %.3f TeV"
      % (2 * tree_mw * 29 / 1000))
print("   alternative prefactor at alpha_W = 1/30: %.3f TeV" % (2 * tree_mw * 30 / 1000))

print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
