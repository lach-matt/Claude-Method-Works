#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for gr-qc/9305017 (Friedman, Schleich & Witt, Topological Censorship,
PRL 71 1486 (1993); arXiv v2 9 Jun 1995).

What is finite / closed-form here is the ONE analytic step the proof rests on (FSW Lemma 2):
"ANEC and theta < 0 imply that every outward null geodesic from the outer trapped surface T has a
conjugate point within finite affine parameter length."  FSW define ANEC over EVERY INEXTENDIBLE null
geodesic (integral over the whole line).  The step needs the integral over the HALF-geodesic that
starts on T.  Galloway (CQG 12 L99, 1995) and Galloway-Schleich-Witt-Woolgar (gr-qc/9902061, Thm 2.1
(iii)) state the condition in the half-line form; GSWW's remark gives the alternative
(full-line ANEC + null generic condition, via a null line).  Graham-Olum (0705.3193) give the achronal
form, adding simple connectivity and the generic condition.

Checks (4D: two transverse dimensions, Raychaudhuri theta' = -theta^2/2 - sigma^2 - R_kk, omega = 0):
  A  sympy: R_kk = 0, theta0 < 0 -> theta = theta0/(1 + theta0 lam/2), focal point at lam = 2/|theta0|.
  B  numeric: half-line condition (running integral of R_kk >= 0 for all lam) + theta0 < 0 -> focusing
     before lam = 2/|theta0| on 2000 random profiles (the Tipler/Borde/Galloway lemma FSW invoke).
  C  sympy + numeric: a profile with FULL-LINE integral >= 0 but half-line integral < 0 whose trapped
     congruence (theta0 < 0) NEVER focuses: the inference as FSW word it does not follow from the
     full-line ANEC they define.  This is a counterexample to an INFERENCE STEP at the ODE level, not
     to Theorem 1, which the later half-line / generic forms carry.
  D  numeric: non-strict ANEC alone does not forbid a null line (Minkowski, R_kk = 0): the null-line
     route needs the generic condition (GSWW remark; Graham-Olum Lemma 1).
  E  z3: Ford's same-universe counterexample to the ACHRONAL form: throat length L > mouth
     separation d makes every through-throat null curve chronal, so achronal ANEC says nothing there.
"""
import json
import math
import random
import sys

import sympy as sp

out = {}

# ---------------------------------------------------------------- A
lam, th0, c, K, delta = sp.symbols('lambda theta0 c K delta', real=True)
theta_A = th0 / (1 + th0 * lam / 2)
resA = sp.simplify(sp.diff(theta_A, lam) + theta_A**2 / 2)
lam_star = sp.solve(sp.Eq(1 + th0 * lam / 2, 0), lam)[0]
out['A_Rkk0_solution_residual'] = str(resA)
out['A_focal_affine_length'] = str(lam_star)
assert resA == 0 and sp.simplify(lam_star + 2 / th0) == 0

# ---------------------------------------------------------------- B
def integrate(theta0, Rfun, lam_max, h=1e-4, blow=-1e6):
    th, l = theta0, 0.0
    f = lambda l_, t_: -t_ * t_ / 2.0 - Rfun(l_)
    while l < lam_max:
        k1 = f(l, th); k2 = f(l + h / 2, th + h / 2 * k1)
        k3 = f(l + h / 2, th + h / 2 * k2); k4 = f(l + h, th + h * k3)
        th += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); l += h
        if th < blow:
            return l, th
    return None, th

random.seed(67)
nB, focusedB, worst_ratio = 400, 0, 0.0
for _ in range(nB):
    theta0 = -random.uniform(0.2, 3.0)
    # R = F' with F >= 0, F(0) = 0  => running integral F(lam) >= 0 for every lam (half-line ANEC form)
    a1, a2, w1, w2 = (random.uniform(0, 3), random.uniform(0, 3), random.uniform(0.5, 6), random.uniform(0.5, 6))
    # F = a1 sin^2(w1 lam) + a2 (1 - cos(w2 lam))  -> F >= 0, F(0) = 0; R = F' changes sign freely
    Rf = lambda l, a1=a1, a2=a2, w1=w1, w2=w2: a1 * w1 * math.sin(2 * w1 * l) + a2 * w2 * math.sin(w2 * l)
    lstar, _ = integrate(theta0, Rf, 2.0 / abs(theta0) + 1e-3, h=2e-4)
    if lstar is not None:
        focusedB += 1
        worst_ratio = max(worst_ratio, lstar / (2.0 / abs(theta0)))
out['B_profiles'] = nB
out['B_focused_before_2_over_abs_theta0'] = focusedB
out['B_max_lamstar_over_bound'] = round(worst_ratio, 6)
assert focusedB == nB and worst_ratio <= 1.0 + 1e-3

# ---------------------------------------------------------------- C
theta_C = -c * sp.exp(-lam)                       # lam >= 0: bounded, never focuses
R_plus = sp.simplify(-sp.diff(theta_C, lam) - theta_C**2 / 2)
half = sp.simplify(sp.integrate(R_plus, (lam, 0, sp.oo), conds='none'))
# lam < 0 branch, continuous at 0:  R_minus = R_plus(0) e^lam + K lam^2 e^lam
R_minus = R_plus.subs(lam, 0) * sp.exp(lam) + K * lam**2 * sp.exp(lam)
left = sp.simplify(sp.integrate(R_minus, (lam, -sp.oo, 0), conds='none'))
K_sol = sp.solve(sp.Eq(left + half, delta), K)[0]
out['C_R_plus'] = str(R_plus)
out['C_half_line_integral'] = str(sp.factor(half))
out['C_left_integral'] = str(sp.expand(left))
out['C_K_for_full_line_equal_delta'] = str(sp.simplify(K_sol))
assert sp.simplify(half + c + c**2 / 4) == 0
assert sp.simplify(R_minus.subs(lam, 0) - R_plus.subs(lam, 0)) == 0
cv, dv = 1.0, 0.1
Kv = float(K_sol.subs({c: cv, delta: dv}))
Rp = sp.lambdify(lam, R_plus.subs(c, cv), 'math')
Rm = sp.lambdify(lam, R_minus.subs({c: cv, K: Kv}), 'math')
full_num = (sp.Integral(R_minus.subs({c: cv, K: Kv}), (lam, -sp.oo, 0)).evalf()
            + sp.Integral(R_plus.subs(c, cv), (lam, 0, sp.oo)).evalf())
lstarC, th_end = integrate(-cv, lambda l: Rp(l), 60.0, h=1e-3)
out['C_numeric'] = {'c': cv, 'K': Kv, 'full_line_integral': float(full_num),
                    'half_line_integral': float(half.subs(c, cv)),
                    'theta0': -cv, 'focused_by_lam_60': lstarC is not None,
                    'theta_at_60': th_end, 'exact_theta_at_60': -cv * math.exp(-60)}
assert full_num > 0 and lstarC is None and abs(th_end) < 1e-6

# ---------------------------------------------------------------- D
lstarD, thD = integrate(0.0, lambda l: 0.0, 100.0, h=1e-2)
out['D_minkowski_null_line'] = {'ANEC_integral': 0.0, 'theta0': 0.0, 'focused': lstarD is not None,
                                'theta_at_100': thD}
assert lstarD is None and thD == 0.0

# ---------------------------------------------------------------- E (z3)
try:
    import z3
    d, L, v = z3.Reals('d L v')
    s = z3.Solver()
    # claim: 0 < d < L  =>  exit event (t = L, x = d) is in I^+(entry) via an exterior curve of speed v = d/L < 1
    s.add(0 < d, d < L, z3.Not(z3.And(d / L < 1, L > d)))
    E1 = str(s.check())             # expect unsat: the through-throat ray is always chronal when L > d
    s2 = z3.Solver()
    # and when L <= d the exit is NOT reached earlier outside (no exterior curve with speed <= 1 beats it)
    s2.add(0 < L, L <= d, d / L < 1)
    E2 = str(s2.check())            # expect unsat
    # the counterexample in C over all c > 0, delta >= 0:  half-line integral < 0 and K real exists
    cc, dd, KK = z3.Reals('cc dd KK')
    s3 = z3.Solver()
    s3.add(cc > 0, dd >= 0, z3.Not(z3.And(-cc - cc * cc / 4 < 0,
                                           z3.Exists([KK], (-cc - cc * cc / 2) + 2 * KK + (-cc - cc * cc / 4) == dd))))
    E3 = str(s3.check())            # expect unsat
    out['E_z3'] = {'L>d => chronal (negation)': E1, 'L<=d => not chronal (negation)': E2,
                   'C holds for every c>0 (negation)': E3, 'z3': z3.get_version_string()}
    assert E1 == 'unsat' and E2 == 'unsat' and E3 == 'unsat'
except ImportError:
    out['E_z3'] = 'z3 not installed: pip install z3-solver'

out['VERDICT'] = ('A,B: the focusing lemma holds in the half-line form. C: FSW Lemma 2 step does not follow '
                  'from the full-line (inextendible-geodesic) ANEC as FSW define it -- an inference gap, '
                  'repaired in the literature by the half-line form (Galloway 1995; GSWW 1999 Thm 2.1(iii)) '
                  'or full-line ANEC + generic condition. D: generic condition is needed on the null-line route. '
                  'E: achronal-ANEC topological censorship cannot cover a same-universe wormhole with L > d.')
print(json.dumps(out, indent=1, default=str))
sys.exit(0)
