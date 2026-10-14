#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of phase1.py's transition equation
    Delta d = (G/c^2) M Lambda,  Lambda = 2[ln(2 R_s/b) - 1]   (code: b -> sqrt(b^2+a^2))
Reads nothing under research/ except by re-implementing phase1.py:261-277 and
phase1.py:359-361 verbatim (no import, so no __pycache__ is written there).
sympy for the closed form and its series; mpmath quad for the exact integrals."""
import math, json, sys
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
OUT = {}

# ---------------- phase1.py re-implemented verbatim ----------------
C_SI, G_SI = 2.99792458e8, 6.67430e-11
SOLAR_MASS, LIGHT_YEAR = 1.98892e30, 9.4607e15
A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0
def phi_device(x, b, m, a=A_CORE, Rs=R_SHELL):
    r = math.hypot(x, b); return m / math.sqrt(r*r + a*a) - m / max(r, Rs)
def _simpson(f, X, n=100001):
    h = 2.0*X/n; s = 0.0
    for i in range(n+1):
        x = -X + i*h
        s += (1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)) * f(x)
    return s*h/3.0
def proper_contraction(m, b=B_RAY, X=20000.0, n=100001):
    return _simpson(lambda x: 1.0 - math.exp(-phi_device(x, b, m)), X, n)
def lam(b=B_RAY, a=A_CORE, Rs=R_SHELL):
    return 2.0*(math.log(2.0*Rs/math.sqrt(b*b + a*a)) - 1.0)

# ---------------- (1) sympy: first-order integral inside the shell ----------------
x, c, R, X0 = sp.symbols('x c R X0', positive=True)
inner = sp.integrate(1/sp.sqrt(x**2 + c**2) - 1/R, (x, -X0, X0))
inner = sp.simplify(inner)
# chord half-length X0 = sqrt(R^2 - b^2); c^2 = b^2 + a^2
b_, a_ = sp.symbols('b a', positive=True)
lam_exact_in = inner.subs(X0, sp.sqrt(R**2 - b_**2)).subs(c, sp.sqrt(b_**2 + a_**2))
eps = sp.symbols('epsilon', positive=True)  # eps = 1/R
lam_log = lam_exact_in.rewrite(sp.log)
ser = sp.series(lam_log.subs(R, 1/eps), eps, 0, 3).removeO()
closed = 2*(sp.log(2/(eps*sp.sqrt(b_**2 + a_**2))) - 1)
diff_ser = sp.simplify(sp.expand_log(sp.expand(ser - closed), force=True))
OUT['sympy_inner_integral'] = str(inner)
OUT['sympy_series_minus_closed_form'] = str(diff_ser)
print('inner integral             :', inner)
print('exact-in minus closed form :', diff_ser, '  (O(1/R_s^2): closed form is exact to leading order)')

# ---------------- (2) exact first-order Lambda incl. exterior tail ----------------
def phi1(xx, b=1.0, a=A_CORE, Rs=R_SHELL):  # Phi/m
    r = mp.sqrt(xx**2 + b**2); return 1/mp.sqrt(r**2 + a**2) - 1/max(r, Rs)
Xc = mp.sqrt(R_SHELL**2 - 1.0)
lam_in = 2*mp.quad(lambda t: phi1(t), [0, 1, 10, Xc])
lam_tail_inf = 2*mp.quad(lambda t: phi1(t), [Xc, 400, 2000, 20000, mp.inf])
lam_first_order = lam_in + lam_tail_inf
OUT['Lambda_closed_form_code'] = lam()
OUT['Lambda_closed_form_prose_b_only'] = 2*(math.log(2*R_SHELL/B_RAY) - 1)
OUT['Lambda_first_order_exact_inside'] = float(lam_in)
OUT['Lambda_exterior_tail_to_inf'] = float(lam_tail_inf)
OUT['Lambda_first_order_exact'] = float(lam_first_order)
OUT['rel_closed_vs_exact'] = float((lam() - lam_first_order)/lam_first_order)
print('Lambda closed (code)  %.9f  closed (prose, b only) %.9f' % (lam(), OUT['Lambda_closed_form_prose_b_only']))
print('Lambda first-order exact %.9f  (inside %.9f, exterior tail %.3e)' % (lam_first_order, lam_in, lam_tail_inf))
print('closed vs exact rel diff %.3e' % OUT['rel_closed_vs_exact'])

# ---------------- (3) nonlinear exact integral and phase1's Simpson ----------------
def exact_contraction(m, X=20000.0, b=1.0):
    f = lambda t: 1 - mp.exp(-m*phi1(t, b))
    Xc_ = mp.sqrt(R_SHELL**2 - b**2)
    pts = [0, 1, 10, Xc_] + [p for p in (400, 2000, 20000) if p < X] + [X]
    return 2*mp.quad(f, pts)
rows = []
for m in (5e-3, 1e-2, 2e-2, 4e-2, 8e-2):
    s = proper_contraction(m)/m
    e = float(exact_contraction(m))/m
    # second-order prediction: per-unit-m = Lambda1 - (m/2) int phi1^2
    q2 = float(2*mp.quad(lambda t: phi1(t)**2, [0, 1, 10, Xc, 20000]))
    q3 = float(2*mp.quad(lambda t: phi1(t)**3, [0, 1, 10, Xc, 20000]))
    pred = float(lam_first_order) - m*q2/2 + m*m*q3/6
    rows.append(dict(m=m, simpson_per_m=s, exact_per_m=e, second_third_order_pred=pred,
                     simpson_minus_exact_rel=(s-e)/e))
    print('m=%-6g simpson %.6f  exact %.6f  series(Phi^3) %.6f  simpson-exact rel %.2e' % (m, s, e, pred, (s-e)/e))
OUT['per_unit_m'] = rows
OUT['owner_quoted_per_unit_m'] = [9.975, 9.967, 9.952, 9.923, 9.864]
OUT['owner_quotes_reproduced_3dp'] = all(abs(round(r['simpson_per_m'], 3) - q) < 1.5e-3
                                        for r, q in zip(rows, OUT['owner_quoted_per_unit_m']))
OUT['agreement_m5e-3_closed_vs_measured_pct'] = 100*(lam() - rows[0]['simpson_per_m'])/lam()
OUT['phi2_drift_pred_m5e-3_pct'] = 100*(5e-3*float(2*mp.quad(lambda t: phi1(t)**2, [0,1,10,Xc,20000]))/2)/float(lam_first_order)
print('closed vs measured at m=5e-3: %.4f %%;  Phi^2 term predicts %.4f %%' %
      (OUT['agreement_m5e-3_closed_vs_measured_pct'], OUT['phi2_drift_pred_m5e-3_pct']))

# ---------------- (4) saturation: X = 400, 2000, 20000 ----------------
m = 2e-2
sat_s = {X: proper_contraction(m, X=X) for X in (400.0, 2000.0, 20000.0)}
sat_e = {X: float(exact_contraction(m, X=X)) for X in (400.0, 2000.0, 20000.0)}
OUT['saturation_simpson'] = {str(k): v for k, v in sat_s.items()}
OUT['saturation_exact'] = {str(k): v for k, v in sat_e.items()}
OUT['saturation_simpson_max_rel_spread'] = (max(sat_s.values())-min(sat_s.values()))/abs(sat_s[20000.0])
OUT['saturation_exact_max_rel_spread'] = (max(sat_e.values())-min(sat_e.values()))/abs(sat_e[20000.0])
print('saturation Simpson', sat_s, 'spread %.2e' % OUT['saturation_simpson_max_rel_spread'])
print('saturation exact  ', sat_e, 'spread %.2e' % OUT['saturation_exact_max_rel_spread'])
# inside-shell endpoints: the law does NOT saturate there (scope hypothesis X >= chord)
ins = {X: float(exact_contraction(m, X=X))/m for X in (50.0, 100.0, 150.0)}
OUT['per_unit_m_endpoints_inside_shell'] = {str(k): v for k, v in ins.items()}
print('endpoints INSIDE the shell (per unit m):', ins)

# ---------------- (5) Simpson with odd n: flaw present, harmless ----------------
OUT['simpson_n_is_odd'] = (100001 % 2 == 1)
def simpson_even(f, X, n=100000):
    h = 2.0*X/n; s = f(-X) + f(X)
    for i in range(1, n): s += (4.0 if i % 2 else 2.0)*f(-X+i*h)
    return s*h/3.0
se = simpson_even(lambda t: 1.0 - math.exp(-phi_device(t, 1.0, 5e-3)), 20000.0)/5e-3
OUT['proper_simpson_even_n_per_m_5e-3'] = se
print('odd-n Simpson (phase1) %.9f  vs even-n %.9f  vs exact %.9f' % (rows[0]['simpson_per_m'], se, rows[0]['exact_per_m']))

# ---------------- (6) position-independence along the ray (extends the claim) ----------------
# point source (Plummer core a) at (xs, rho) inside a concentric compensating shell R_s, ray at y=0
def lam_offaxis(xs, rho, a=A_CORE, Rs=R_SHELL, X=1e6):
    src = lambda t: 1/mp.sqrt((t-xs)**2 + rho**2 + a**2)
    shell = lambda t: 1/max(abs(t), Rs)   # ray through the shell centre plane: take ray at y=0 through centre
    f = lambda t: src(t) - shell(t)
    pts = sorted(set([-X, -Rs, xs-10, xs-1, xs, xs+1, xs+10, Rs, X]))
    return float(mp.quad(f, pts))
off = {str(xs): lam_offaxis(xs, 1.0) for xs in (0.0, 50.0, 100.0, 150.0)}
OUT['Lambda_point_source_rho1_vs_position'] = off
OUT['Lambda_closed_rho1_ray_through_centre'] = 2*(math.log(2*R_SHELL/math.sqrt(1+A_CORE**2)) - 1)
print('Lambda for a source at distance 1 from a ray through the shell centre, by position xs:', off)

# ---------------- (7) PPN gamma: Delta d scales with gamma ----------------
# spatial metric (1 + 2 gamma U) delta_ij  =>  dl_proper = (1 + gamma U) dl: Delta d proportional to gamma.
gamma_minus_1, sig = 2.1e-5, 2.3e-5   # Cassini, Bertotti et al. 2003, as quoted in arXiv:1710.05834
OUT['gamma_shift_in_Lambda_rel_max'] = abs(gamma_minus_1) + 3*sig
# ---------------- (8) price numbers ----------------
er = C_SI**2/(G_SI*lam())
GM_sun_IAU = 1.3271244e20
Msun_IAU = GM_sun_IAU/G_SI
OUT['exchange_rate_kg_per_m'] = er
OUT['solar_mass_buys_m_phase1'] = G_SI*SOLAR_MASS/C_SI**2*lam()
OUT['solar_mass_buys_m_IAU_GM'] = GM_sun_IAU/C_SI**2*lam()
OUT['Msun_phase1_vs_IAU_rel'] = (SOLAR_MASS - Msun_IAU)/Msun_IAU
print('exchange rate %.5e kg/m; one M_sun buys %.4f m (phase1 M_sun) / %.4f m (IAU GM_sun); M_sun rel diff %.2e'
      % (er, OUT['solar_mass_buys_m_phase1'], OUT['solar_mass_buys_m_IAU_GM'], OUT['Msun_phase1_vs_IAU_rel']))

# ---------------- (9) linearity outside the measured window (specthm.py:96, :945 'for every m > 0') ----------------
big = {str(mm): float(exact_contraction(mm))/mm for mm in (0.08, 0.2, 0.5, 1.0, 2.0)}
OUT['per_unit_m_beyond_window'] = big
OUT['per_unit_m_rel_drop_vs_Lambda'] = {k: 1 - v/float(lam_first_order) for k, v in big.items()}
print('per unit m beyond the measured window:', {k: round(v, 4) for k, v in big.items()})
print('   relative drop from Lambda:', {k: '%.2f%%' % (100*v) for k, v in OUT['per_unit_m_rel_drop_vs_Lambda'].items()})

# ---------------- (10) scope of the price figures (phase1.py:174-178 and selftest) ----------------
# Saturation needs both endpoints outside the shell: half-baseline X >= R_s = 200 b.
# Delta d = m Lambda b  =>  m = (Delta d / L) * 2 (R_s/b) / Lambda  at the tightest geometry X = R_s.
RB = R_SHELL / B_RAY
def m_min(frac, Lam=lam(), rb=RB): return frac * 2.0 * rb / Lam
OUT['m_min_4ly_1pct'] = m_min(0.01)
OUT['m_min_4ly_50pct'] = m_min(0.50)
OUT['max_fraction_in_measured_window_m0.08'] = 0.08 * lam() / (2.0 * RB)
L4 = 4.0 * LIGHT_YEAR
OUT['b_max_for_4ly_m'] = (L4/2)/RB
print('4 ly by 1%%: needs m >= %.3f (measured window ends at 0.08); by 50%%: m >= %.2f' % (OUT['m_min_4ly_1pct'], OUT['m_min_4ly_50pct']))
print('largest fractional contraction the seated geometry certifies with m <= 0.08: %.3f %%' % (100*OUT['max_fraction_in_measured_window_m0.08']))
# nonlinear integral at the tightest geometry for the 1% case: per-unit-m and the mass it would really take
m1 = OUT['m_min_4ly_1pct']
per = float(exact_contraction(m1, X=R_SHELL))/m1
OUT['per_unit_m_at_m_min_1pct_X_eq_Rs'] = per
OUT['price_underestimate_1pct_rel'] = lam()/per - 1
print('at m = %.3f, X = R_s: per unit m %.4f vs Lambda %.4f -> law under-prices by %.2f %% (and Phi ~ %.2f is not weak field)'
      % (m1, per, lam(), 100*OUT['price_underestimate_1pct_rel'], m1))
# a weak-field-consistent geometry for the 1% case: choose R_s/b so that m_min <= 0.08
import bisect
lo, hi = 2.0, 200.0
for _ in range(200):
    mid = 0.5*(lo+hi); Lm = 2*(math.log(2*mid) - 1)
    (lo, hi) = (mid, hi) if m_min(0.01, Lm, mid) <= 0.08 else (lo, mid)
Lw = 2*(math.log(2*lo) - 1)
OUT['weak_field_geometry_1pct'] = dict(Rs_over_b=lo, Lambda=Lw,
     solar_masses=(0.01*L4)*C_SI**2/(G_SI*Lw)/SOLAR_MASS)
print('weak-field-consistent 1%% geometry: R_s/b <= %.2f, Lambda = %.3f, mass %.4e M_sun (vs 2.5667e10 at Lambda 9.98)'
      % (lo, Lw, OUT['weak_field_geometry_1pct']['solar_masses']))

ok = (abs(OUT['rel_closed_vs_exact']) < 1e-4 and OUT['owner_quotes_reproduced_3dp']
      and OUT['saturation_exact_max_rel_spread'] < 1e-8 and abs(er/1.34894e26 - 1) < 1e-4)
OUT['VERDICT_numbers_agree'] = ok
print('ALL OWNER NUMBERS REPRODUCED:', ok)
json.dump(OUT, open(sys.argv[1] if len(sys.argv) > 1 else '/dev/null', 'w'), indent=1, default=str)
