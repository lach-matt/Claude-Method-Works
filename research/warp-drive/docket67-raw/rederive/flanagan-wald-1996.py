#!/usr/bin/env python3
"""DOCKET 67 audit -- Flanagan & Wald, gr-qc/9602052, PRD 54 6233 (1996).

What is finite or closed-form here, checked:
 A. The tree datum: h at the core surface = |g_tt| - 1 = 2(M/b)/(a/b), from
    achievable.py's constants (imported read-only; nothing is written).
 B. What 'eps ~ O(1)' costs a second-order truncation: FW's results are
    statements through O(eps^2) (their eqs 1.6-1.7 truncate at O(eps^3)) and
    carry no remainder bound.  At eps*h = 0.5 the dropped remainder is
    function-dependent -- shown for three redshift-type functions.
 C. FW's long-wavelength hypothesis (L >> l_P) at the corridor's one-metre
    scale -- it HOLDS; only the near-flat hypothesis fails.  And FW's own
    domain-of-validity criterion (Planckian curvature) evaluated at the core:
    not met for any a >> l_P (the fluctuation criterion is NOT evaluated).
 D. A printed closed form in the source (FW footnote [90], p.50):
    INT_0^inf J0(kx) x/(1+x^2)^2 dx = k K1(k)/2, and
    k K1(k) = 1 + k^2 log(k)/2 + [(2 gamma - 1)/4 - log(2)/2] k^2 + O(k^3).
Exit 0 iff every check passes.
"""
import sys, math
import sympy as sp
import mpmath as mp

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.dont_write_bytecode = True   # never write into the tree
sys.path.insert(0, TREE)
fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok: fails.append(name)

# A ----------------------------------------------------------------------
import achievable
h = 2.0 * achievable.M_OVER_B / achievable.A_OVER_B
chk("A1 tree datum h_core = 2(M/b)/(a/b)", abs(h - 0.5) < 1e-15,
    "M/b=%g a/b=%g -> h=%g, |g_tt|=%g, |g_tt|^2=%g" % (achievable.M_OVER_B,
    achievable.A_OVER_B, h, 1+h, (1+h)**2))
chk("A2 |g_tt|^2 = 2.25 (fewsterteo.py:616's figure)", abs((1+h)**2 - 2.25) < 1e-12)

# B ----------------------------------------------------------------------
e = sp.symbols('e')
funcs = {"sqrt(1-e) (Schwarzschild-type lapse)": sp.sqrt(1 - e),
         "1/(1-e)   (g_rr-type)": 1/(1 - e),
         "sqrt(1+e) (tree's |g_tt|=1+h lapse)": sp.sqrt(1 + e)}
rel = {}
for name, f in funcs.items():
    t2 = sp.series(f, e, 0, 3).removeO()
    ex = float(f.subs(e, h)); ap = float(t2.subs(e, h))
    rel[name] = abs(ex - ap) / abs(ex)
    print("     %-40s exact %.6f  O(e^2) %.6f  rel.err %.4f" % (name, ex, ap, rel[name]))
chk("B1 at eps*h=0.5 the O(eps^3) remainder is not uniformly small "
    "(spread over functions spans > 5x)", max(rel.values()) / min(rel.values()) > 5,
    "min %.4f max %.4f" % (min(rel.values()), max(rel.values())))
chk("B2 ratio of successive orders at eps*h=0.5 is 0.5, not << 1", h >= 0.5)

# C ----------------------------------------------------------------------
G, hbar, c = 6.67430e-11, 1.054571817e-34, 299792458.0   # CODATA 2018/2022
lP = math.sqrt(hbar * G / c**3)
L = 1.0   # 'one metre of corridor', throatmass.py:35
alpha = L / lP
chk("C1 l_P = 1.616255e-35 m (CODATA)", abs(lP - 1.616255e-35) / 1.616255e-35 < 1e-5,
    "l_P=%.6e m" % lP)
chk("C2 FW long-wavelength hypothesis alpha=L/l_P >> 1 HOLDS at 1 m",
    alpha > 1e30, "alpha=%.4e (log10 %.2f)" % (alpha, math.log10(alpha)))

# C3: FW's OWN domain-of-validity criterion (p.2, second bullet): curvature
# Planckian somewhere, or fluctuations ~ mean.  Curvature at the core surface
# for a Schwarzschild-type exterior: |Riemann| ~ 2M/a^3 = h/a^2 (h = 2M/a = 0.5).
# In Planck units l_P^2 * R = h (l_P/a)^2 -- Planckian only if a ~ l_P.
for a_m in (1.0, 1e-10, 4.849e-33):
    x = h * (lP / a_m)**2
    print("     core radius a = %.3e m : l_P^2 * |Riem| ~ %.3e" % (a_m, x))
chk("C3 at a = 1 m the core-surface curvature is sub-Planckian by > 60 orders",
    h * (lP / 1.0)**2 < 1e-60, "%.3e" % (h * lP**2))

# D ----------------------------------------------------------------------
mp.mp.dps = 30
worst = 0.0
for k in (0.1, 0.5, 1.0, 2.0, 5.0):
    lhs = mp.quadosc(lambda x: mp.besselj(0, k*x) * x / (1 + x**2)**2,
                     [0, mp.inf], omega=k)
    rhs = k * mp.besselk(1, k) / 2
    worst = max(worst, float(abs(lhs - rhs)))
chk("D1 FW fn[90] integral = k K1(k)/2 at k in {0.1,0.5,1,2,5}", worst < 1e-20,
    "max |lhs-rhs| = %.2e" % worst)
k = sp.symbols('k', positive=True)
ser = sp.series(k * sp.besselk(1, k), k, 0, 3).removeO()
fw = 1 + k**2 * sp.log(k) / 2 + ((2*sp.EulerGamma - 1)/4 - sp.log(2)/2) * k**2
chk("D2 FW fn[90] expansion of k K1(k) through k^2 (sympy)",
    sp.simplify(sp.expand(ser - fw)) == 0, "series = %s" % sp.simplify(ser))

print("\n%d check(s) failed" % len(fails) if fails else "\nALL PASS")
sys.exit(1 if fails else 0)
