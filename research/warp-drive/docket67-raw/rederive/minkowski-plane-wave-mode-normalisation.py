#!/usr/bin/env python3
"""DOCKET 67 / pass S #23 -- minkowski-plane-wave-mode-normalisation.

Tree use (fewsterteo.py:27-33, 456-477): U_k = e^{ik.x}/sqrt((2 pi)^n 2 w_k),
'control norm=1 returns P = 1/2'.  Checks, all symbolic unless stated:

 C1  KG inner product of f_k = U_k e^{-i w t} with f_k' (plane-wave overlap
     INT d^n x e^{i(k'-k).x} = (2pi)^n delta^n(k-k') supplied as the only
     distributional input): norm=2 gives coefficient 1 (orthonormal), norm=1
     gives 2 (NOT orthonormal).  n symbolic.
 C2  Canonical commutator [phi(x), pi(x')] = i delta^n(x-x') from the mode
     expansion: requires |N|^2 = 1/((2pi)^n 2 w); norm=2 gives i, norm=1 2i.
 C3  Label-convention independence: the coincidence Wightman function
     SUM_lambda |U_lambda|^2 e^{-w eps} for n=3, massless, equals the Hadamard
     coefficient 1/(4 pi^2 eps^2) (W = 1/(4 pi^2 sigma), sigma = -(t - i eps)^2
     at x = x', t = 0) with norm=2; norm=1 gives 1/(2 pi^2 eps^2).
 C4  F&T (2.10) as transcribed (DOCKET 62, not re-read) on plane waves:
     -(1/2) [w^2 + k^2 + mu^2] |U_k|^2 with w^2 = k^2 + mu^2 -> -(1/2) w/(2pi)^n,
     i.e. (3.2) as transcribed, WITHOUT passing through (2.12): the factor 2
     is forced by (2.10)'s -(1/2) matching (3.2)'s -(1/2).  norm=1 -> -w/(2pi)^n.
 C5  Tree's route 2 reproduced: P = 1 at norm=2, P = 1/2 at norm=1.
 C6  Absolute-constant consistency of the transcription chain (a DISCREPANCY
     probe, not a refutation): (3.2) with INT_0^oo dw as transcribed, massless
     n = 3, reduced to INT du u^4 |fhat^{1/2}(u)|^2 gives 1/(16 pi^2); the
     transcribed (5.6) prints 1/(16 pi^3).  With the Lorentzian sampler and
     Ford-Roman's -3/(32 pi^2 t0^4) (gr-qc/9410043) the 1/(16 pi^3) form gives
     the tree's 9/64, the 1/(16 pi^2) form gives 9 pi/64.  A 1/pi is missing
     from the transcribed (2.10)/(3.2) dw measure (or from the fhat
     convention); it is common to (2.12) and (3.2), so P (a ratio) is immune.
"""
import sys
import sympy as sp

rows = []
def chk(label, got, want):
    ok = sp.simplify(got - want) == 0
    rows.append((label, ok, got, want))

n = sp.Symbol('n', positive=True, integer=True)
w, k, mu, eps, t0 = sp.symbols('omega k mu epsilon t_0', positive=True)
DELTA = sp.Symbol('delta')   # stands for delta^n(k - k') as a formal factor

def N2(norm):
    return 1 / ((2 * sp.pi) ** n * norm * w)

# C1: (f_k, f_k') = i INT d^n x (f_k^* d_t f_k' - d_t f_k^* f_k'), at k = k'
t = sp.Symbol('t', real=True)
for norm, want in ((2, 1), (1, 2)):
    N = sp.sqrt(N2(norm))
    fk = N * sp.exp(-sp.I * w * t)          # spatial phase handled by overlap
    ip_density = sp.I * (sp.conjugate(fk) * sp.diff(fk, t)
                         - sp.diff(sp.conjugate(fk), t) * fk)
    coeff = sp.simplify(ip_density * (2 * sp.pi) ** n)  # times (2pi)^n delta
    chk("C1 KG norm coefficient of delta^n(k-k'), norm=%d" % norm, coeff, want)

# C2: [phi(x),pi(x')] = INT d^n k |N|^2 (i w + i w) e^{ik(x-x')} = coeff * i delta^n
for norm, want in ((2, sp.I), (1, 2 * sp.I)):
    coeff = sp.simplify(N2(norm) * 2 * sp.I * w * (2 * sp.pi) ** n)
    chk("C2 CCR coefficient of delta^n(x-x'), norm=%d" % norm, coeff, want)

# C3: n=3 massless coincidence Wightman, regulated e^{-k eps}
for norm, want in ((2, 1 / (4 * sp.pi ** 2 * eps ** 2)),
                   (1, 1 / (2 * sp.pi ** 2 * eps ** 2))):
    integrand = (N2(norm).subs({n: 3, w: k}) * 4 * sp.pi * k ** 2
                 * sp.exp(-k * eps))
    W = sp.integrate(integrand, (k, 0, sp.oo))
    chk("C3 Wightman(eps) vs Hadamard 1/(4pi^2 eps^2), norm=%d" % norm, W, want)

# C4: (2.10) bracket on plane waves, on shell
for norm, want in ((2, -sp.Rational(1, 2) * w / (2 * sp.pi) ** n),
                   (1, -w / (2 * sp.pi) ** n)):
    kk2 = w ** 2 - mu ** 2                  # dispersion relation, |k|^2
    b210 = (w ** 2 + kk2 + mu ** 2) * N2(norm)   # |grad U|^2 = k^2 |U|^2
    chk("C4 (2.10) on plane waves -> (3.2) density, norm=%d" % norm,
        -sp.Rational(1, 2) * b210, want)

# C5: tree's route 2 (same algebra as fewsterteo.prefactor_route2)
P = sp.Symbol('P', positive=True)
for norm, want in ((2, 1), (1, sp.Rational(1, 2))):
    mod2 = N2(norm)                          # |U_k|^2, x-independent
    lap = 0                                  # grad^2 of a constant
    bracket = w ** 2 * mod2 + lap / 4
    sol = sp.solve(sp.Eq(-P * bracket, -sp.Rational(1, 2) * w / (2 * sp.pi) ** n), P)
    chk("C5 route 2 prefactor, norm=%d" % norm, sol[0], want)

# C6: absolute constant of the transcription chain
u, kk, ww = sp.symbols('u kk ww', positive=True)
F = sp.Function('F')
# -(1/2) INT_0^oo dw INT d^3k/(2pi)^3 k F(w+k): inner INT_0^u k^3 dk = u^4/4
c_trans = -sp.Rational(1, 2) * 4 * sp.pi / (2 * sp.pi) ** 3 * sp.Rational(1, 4)
chk("C6a transcribed (3.2) -> coefficient of INT u^4 F(u) du is -1/(16 pi^2)",
    c_trans, -1 / (16 * sp.pi ** 2))
av = sp.Rational(5, 2)
Iv = 2 ** (2 * av - 3) * sp.gamma(av) ** 4 / sp.gamma(2 * av)   # INT v^4 K0^2
lor = 4 / (sp.pi * t0 ** 4) * Iv            # INT u^4 (4 t0/pi) K0(t0 u)^2 du
FR = -sp.Rational(3, 32) / (sp.pi ** 2 * t0 ** 4)
chk("C6b with 1/(16 pi^3) (transcribed 5.6): ratio to Ford-Roman = 9/64",
    (-lor / (16 * sp.pi ** 3)) / FR, sp.Rational(9, 64))
chk("C6c with 1/(16 pi^2) (transcribed 3.2 + mode norm): ratio = 9 pi/64",
    (c_trans * lor) / FR, 9 * sp.pi / 64)
# numeric cross-check of INT v^4 K0(v)^2 dv
import mpmath as mp
mp.mp.dps = 25
q = mp.quad(lambda v: v ** 4 * mp.besselk(0, v) ** 2, [0, 1, 10, 60])
chk("C6d numeric INT v^4 K0^2 = 27 pi^2/512 (rel 1e-15)",
    sp.Integer(1) if abs(q - 27 * mp.pi ** 2 / 512) / q < 1e-15 else 0, 1)

fails = 0
for label, ok, got, want in rows:
    print("%-4s %s   got=%s want=%s" % ("PASS" if ok else "FAIL", label, got, want))
    fails += (not ok)
print("\n%d/%d PASS" % (len(rows) - fails, len(rows)))
sys.exit(1 if fails else 0)
