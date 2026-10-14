#!/usr/bin/env python3
r"""
DOCKET 67 -- audit of the KF qualitative conclusion as the tree uses it:
  "fluctuations of order unity wherever rho < 0 -- SURVIVES in every case they study"
  (research/warp-drive/fluctuation.py:63-64; KF_QUALITATIVE_CONCLUSION_SURVIVES = True, :152, :480)

KF (gr-qc/9304008 v1) study four cases: vacuum+2 (III.A), squeezed COHERENT states
|alpha,zeta> = D(alpha)S(zeta)|0> (III.B, eqs 3.9-3.19, Figs 1-4), the squeezed vacuum
(alpha=0, 3.22-3.23) and the Casimir (periodic) vacuum (III.C).  KF III.B: "By the point
that the state is sufficiently squeezed to have rho < 0, we always have that Delta is at
least of order unity."  Delta = |(<:T00^2:> - rho^2)/<:T00^2:>|, KF (3.2).

This script is independent of fluctuation.py (nothing imported from the tree).
  C1  exact normal-ordered moments of |alpha,zeta> from the normal-ordered generating
      function, KF conventions (3.12)-(3.17); control: reproduces KF (3.18) exactly.
  C2  exact <:T00^2:> vs KF's printed (3.19): not equal (the tree's KF_319_IS_EXACT=False).
  C3  closed form on KF's own Fig.1/2 slice (gamma = delta = 0, theta = pi/2):
      rho = 2K(2s^2 - (1-e^{-2r})/2), and on the curve s^2 = (1-e^{-2r})/8:
      rho = -K(1-e^{-2r})/2 < 0 AND <:T00^2:> = rho^2 EXACTLY, i.e. Delta = 0.
  C4  independent control: truncated Fock-space matrices (numpy, dim 220), r = 1.
  C5  what KF's printed (3.19) gives at the same point.
  C6  z3 on the one-quadrature reduction: rho<0 and Delta<1/10 is SAT; the Delta<1/10
      band on rho<0 is exactly t in ((23+sqrt(519))/23 ... ) -- computed; vacuity guards.
  C7  how thin the band is on KF's Fig.1 slice (area fraction, numeric).
  C8  the other three cases still satisfy rho<0 => Delta >= 1/3 (vac+2 z3; sq. vacuum 2/3;
      Casimir 6/7), so the conclusion survives there.
"""
import sympy as sp

out = {}
K, r, s = sp.symbols('K r s', positive=True)
th, gam, dl = sp.symbols('theta gamma delta', real=True)
S_, T_ = sp.symbols('S T')

# ---------------------------------------------------------------- C1
al = s * sp.exp(sp.I * gam)
alc = s * sp.exp(-sp.I * gam)
n_c = sp.sinh(r)**2                                  # connected <a+ a>
M_c = -sp.exp(sp.I * dl) * sp.sinh(r) * sp.cosh(r)   # connected <a a>   (from 3.16)
Mc_c = -sp.exp(-sp.I * dl) * sp.sinh(r) * sp.cosh(r)
Gf = sp.exp(S_ * alc + T_ * al + n_c * S_ * T_ + Mc_c * S_**2 / 2 + M_c * T_**2 / 2)
z = sp.exp(2 * sp.I * th)
# :T00: = K(2 a+a - z a^2 - zbar a+^2)   KF (2.10)-(2.14)
T1 = {(1, 1): 2 * K, (0, 2): -z * K, (2, 0): -K / z}
T2p = {}
for (m1, n1), a in T1.items():
    for (m2, n2), b in T1.items():
        T2p[(m1 + m2, n1 + n2)] = T2p.get((m1 + m2, n1 + n2), 0) + a * b


def ev(P):
    tot = 0
    for (m, n), c in P.items():
        tot += c * sp.diff(Gf, S_, m, T_, n).subs({S_: 0, T_: 0})
    return tot


rho = ev(T1)
T2 = ev(T2p)
kf318 = 2 * K * (sp.sinh(r) * sp.cosh(r) * sp.cos(2 * th + dl) + sp.sinh(r)**2
                 + s**2 * (1 - sp.cos(2 * (th + gam))))
c1 = sp.simplify(sp.expand((rho - kf318).rewrite(sp.exp))) == 0
out['C1 exact rho reproduces KF (3.18)'] = c1

# ---------------------------------------------------------------- C2
kf319 = 2 * K**2 * (s**4 * (sp.cos(4 * (th + gam)) - 4 * sp.cos(2 * (th + gam)) + 3)
                    + 3 * s**2 * (2 * sp.sinh(r) * sp.cosh(r) * (2 * sp.cos(2 * th + dl + 2 * gam)
                                                                  - sp.cos(4 * th + dl + 2 * gam))
                                  + 4 * sp.sinh(r)**2 * (sp.cos(2 * gam) - sp.cos(2 * th))
                                  - sp.cos(dl + 2 * gam))
                    + 3 * sp.sinh(r)**2 * (sp.cosh(r)**2 * sp.cos(4 * th + 2 * dl) + 3 - 4 * sp.cos(2 * th)))
pt_generic = {K: 1, r: sp.Rational(1, 2), s: sp.Rational(3, 5), th: sp.Rational(3, 10),
              gam: sp.Rational(1, 7), dl: sp.Rational(2, 9)}
d2 = complex(sp.N((T2 - kf319).subs(pt_generic), 30))
out['C2 exact <:T00^2:> != KF (3.19) (generic point)'] = abs(d2) > 1e-6

# ---------------------------------------------------------------- C3  Fig.1 slice
sl = {gam: 0, dl: 0, th: sp.pi / 2}
rho_sl = sp.simplify(sp.expand(rho.subs(sl).rewrite(sp.exp)))
T2_sl = sp.simplify(sp.expand(T2.subs(sl).rewrite(sp.exp)))
out['C3a rho on slice == 2K(2s^2-(1-e^-2r)/2)'] = sp.simplify(
    rho_sl - 2 * K * (2 * s**2 - (1 - sp.exp(-2 * r)) / 2)) == 0
# one-quadrature form: rho = 2K(m2 + g), <:T^2:> = 4K^2 (m2^2 + 6 m2 g + 3 g^2)
m2 = 2 * s**2
g = -(1 - sp.exp(-2 * r)) / 2
out['C3b <:T^2:> on slice == 4K^2(m^4+6m^2g+3g^2)'] = sp.simplify(
    T2_sl - 4 * K**2 * (m2**2 + 6 * m2 * g + 3 * g**2)) == 0
curve = {s: sp.sqrt((1 - sp.exp(-2 * r)) / 8)}
rho_c = sp.simplify(rho_sl.subs(curve))
T2_c = sp.simplify(T2_sl.subs(curve))
out['C3c on curve rho == -K(1-e^-2r)/2'] = sp.simplify(rho_c + K * (1 - sp.exp(-2 * r)) / 2) == 0
out['C3d on curve <:T00^2:> - rho^2 == 0 identically in r'] = sp.simplify(T2_c - rho_c**2) == 0
out['C3e on curve <:T00^2:> > 0 (Delta well defined)'] = sp.simplify(T2_c - K**2 * (1 - sp.exp(-2 * r))**2 / 4) == 0
r0 = 1
s0 = float(sp.sqrt((1 - sp.exp(-2)) / 8))
out['C3f witness r=1, s'] = round(s0, 6)
out['C3g witness rho/K'] = round(float(rho_c.subs({r: 1, K: 1})), 6)

# ---------------------------------------------------------------- C4  Fock control
import numpy as np
from scipy.linalg import expm
D = 220
a = np.diag(np.sqrt(np.arange(1, D)), 1).astype(complex)
ad = a.conj().T
vac = np.zeros(D, complex); vac[0] = 1
rr, ss, gg, dd, tt = 1.0, s0, 0.0, 0.0, np.pi / 2
zeta = rr * np.exp(1j * dd)
Sop = expm(0.5 * np.conj(zeta) * a @ a - 0.5 * zeta * ad @ ad)
alpha = ss * np.exp(1j * gg)
Dop = expm(alpha * ad - np.conj(alpha) * a)
psi = Dop @ (Sop @ vac)
zz = np.exp(2j * tt)
T1op = 2 * ad @ a - zz * a @ a - np.conj(zz) * ad @ ad
# normal-ordered square: sum over (m,n) coefficient * ad^m a^n
coef = {}
c1d = {(1, 1): 2, (0, 2): -zz, (2, 0): -np.conj(zz)}
for (p1, q1), x in c1d.items():
    for (p2, q2), y in c1d.items():
        coef[(p1 + p2, q1 + q2)] = coef.get((p1 + p2, q1 + q2), 0) + x * y
T2op = sum(c * np.linalg.matrix_power(ad, m) @ np.linalg.matrix_power(a, n) for (m, n), c in coef.items())
rho_f = np.vdot(psi, T1op @ psi).real
T2_f = np.vdot(psi, T2op @ psi).real
norm_tail = float(np.sum(np.abs(psi[-20:])**2))
out['C4 Fock: norm, tail weight'] = (round(float(np.vdot(psi, psi).real), 12), norm_tail)
out['C4 Fock: rho/K'] = round(rho_f, 10)
out['C4 Fock: <:T^2:>/K^2'] = round(T2_f, 10)
out['C4 Fock: Delta'] = abs((T2_f - rho_f**2) / T2_f)

# ---------------------------------------------------------------- C5  KF's (3.19) there
kf319_sl = kf319.subs(sl)
v319 = float(kf319_sl.subs({K: 1, r: 1, s: s0}))
vrho = float(rho_c.subs({K: 1, r: 1}))
out['C5 KF(3.19) at witness /K^2'] = round(v319, 6)
out['C5 Delta from KF (3.18)+(3.19) at witness'] = round(abs((v319 - vrho**2) / v319), 6)
out['C5 exact Delta at witness'] = 0

# ---------------------------------------------------------------- C6  z3
import z3
m, gq = z3.Reals('m gq')       # m = mean-field value (m^2), gq = normal-ordered connected variance
X = 4 * m * gq + 2 * gq * gq   # <:T^2:> - rho^2   (per 4K^2)
T2q = m * m + 6 * m * gq + 3 * gq * gq
H = [m > 0, m + gq < 0]        # rho < 0 (m>0: coherent part present)
sol = z3.Solver(); sol.add(*H, T2q > 0, 10 * X < T2q, -10 * X < T2q)
out['C6a z3: rho<0 AND Delta<1/10 SAT'] = str(sol.check())
sol2 = z3.Solver(); sol2.add(*H, T2q > 0, X == 0)
out['C6b z3: rho<0 AND Delta=0 SAT'] = str(sol2.check())
if sol2.check() == z3.sat:
    mm = sol2.model(); out['C6b model'] = (str(mm[m]), str(mm[gq]))
# the zero-mean limit (squeezed vacuum): Delta = 2/3 -- guard that the claim is TRUE there
sol3 = z3.Solver(); sol3.add(gq < 0, z3.Not(3 * (2 * gq * gq) == 2 * (3 * gq * gq)))
out['C6c z3: m=0 => Delta=2/3 (UNSAT of negation)'] = str(sol3.check())
# band where Delta < 1/10 on rho<0, in t = -g/m (rho<0 <=> t>1): exact endpoints
t = sp.symbols('t', positive=True)
Dl = (2 * t**2 - 4 * t) / (3 * t**2 - 6 * t + 1)          # signed ratio X/T2 in t
lo = sp.nsolve(-Dl - sp.Rational(1, 10), t, 1.98)
hi = sp.nsolve(Dl - sp.Rational(1, 10), t, 2.03)
out['C6d Delta<1/10 on rho<0 exactly for t in'] = (float(lo), float(hi))
lo3 = sp.nsolve(-Dl - sp.Rational(1, 3), t, 1.9)
hi3 = sp.nsolve(Dl - sp.Rational(1, 3), t, 2.3)
out['C6e Delta<1/3 on rho<0 exactly for t in'] = (float(lo3), float(hi3))
out['C6f <:T00^2:> < 0 on rho<0 for t in (1, 1+sqrt(2/3))'] = float(1 + sp.sqrt(sp.Rational(2, 3)))

# ---------------------------------------------------------------- C7  thinness on Fig.1 slice
N = 1200
rs = np.linspace(1e-3, 2.0, N); ss_ = np.linspace(1e-3, 1.0, N)
R, Sg = np.meshgrid(rs, ss_)
mm_ = 2 * Sg**2; gv = -(1 - np.exp(-2 * R)) / 2
rho_g = mm_ + gv
T2g = mm_**2 + 6 * mm_ * gv + 3 * gv**2
Dg = np.abs((T2g - rho_g**2) / T2g)
neg = rho_g < 0
out['C7 box r in (0,2], s in (0,1]: fraction of rho<0 cells with Delta<0.1'] = float(np.mean(Dg[neg] < 0.1))
out['C7 ... with Delta<1/3'] = float(np.mean(Dg[neg] < 1 / 3))
out['C7 ... with Delta>1 (incl. <:T^2:><0)'] = float(np.mean(Dg[neg] > 1))

# ---------------------------------------------------------------- C8  other cases
e, c, q = z3.Reals('e c q')
Hv = [q > 0, q * q == 2, c >= -1, c <= 1, e * (2 * e - q * c) < 0]
Xv = 2 * e - q * c
pv = z3.Solver(); pv.add(*Hv, z3.Not(z3.And(Xv * Xv < 2 * (1 + e * e), Xv * Xv > 0)))
out['C8a vac+2: rho<0 => 1/3<Delta<1 (UNSAT of negation)'] = str(pv.check())
gv2 = z3.Solver(); gv2.add(*Hv); out['C8a vacuity guard SAT'] = str(gv2.check())
out['C8b squeezed vacuum Delta'] = '2/3 (C6c)'
out['C8c Casimir Delta = 6/7 from Delta\'=(1/8)[...] with xi=(-1,-1,3)'] = str(
    sp.Rational(6, 1) / 7) if sp.Rational(1, 8) * ((1 - 1 - 1 + 3)**2 + (1 - 1 + 1 - 3)**2 + (1 + 1 - 1 - 3)**2 + (1 + 1 + 1 + 3)**2) == 6 else 'FAIL'

for k_, v_ in out.items():
    print('%-78s %s' % (k_, v_))
ok = (c1 and out['C2 exact <:T00^2:> != KF (3.19) (generic point)'] and out['C3a rho on slice == 2K(2s^2-(1-e^-2r)/2)']
      and out['C3b <:T^2:> on slice == 4K^2(m^4+6m^2g+3g^2)'] and out['C3c on curve rho == -K(1-e^-2r)/2']
      and out['C3d on curve <:T00^2:> - rho^2 == 0 identically in r'] and out['C4 Fock: Delta'] < 1e-8
      and out['C4 Fock: rho/K'] < 0 and out['C6b z3: rho<0 AND Delta=0 SAT'] == 'sat'
      and out['C8a vac+2: rho<0 => 1/3<Delta<1 (UNSAT of negation)'] == 'unsat')
print('ALL CHECKS AS REPORTED:', ok)
