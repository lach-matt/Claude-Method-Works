#!/usr/bin/env python3
"""inverse6_5m: the six inverse bounds of CONSTANTS5.md R6.3-R9.5, part 2: certified real-axis resolvent bounds for the
mode-decomposed operators behind III.D:365 (box on 1-forms at b0) and III.F'':223 (L_b0 at sigma != 0), every harmonic.
Labels: computed (exact, sympy), certified (interval arithmetic, mpmath.iv at 30 digits, with explicit tail bounds;
every printed decimal rounded outward), deduced (Lemma E2.8 of E2-PILOT.md 3e, READ and applied; the monotonicity and
tail inequalities are proved in INVERSE5-SIX.md section 3). Part 1 is inverse6_5.py.

The master equations (mu = 1, r_h = 1, ' = d/dr_*, y = 1/r^2, f = 1 - y, U := f y, Q := f y^2):
  III.D (M2)-(M4) (PART-III-D-GAUGEPOT.md:345-358, modes5.py): the 1-form box at sigma != 0 reduces, harmonic by
  harmonic, to -Phi'' + V Phi - sigma^2 Phi = 0 with V_0 = (k + 3/4) U + (9/4) Q (scalar step), V_1 = (k + 3/4) U +
  (5/4) Q (vector type, lambda = (l + 1)^2), V_2 = (k + 3/4) U - (7/4) Q (scalar-type Maxwell), k = l (l + 2);
  III.F'' Theorem 2.2 via gmodes5.py G1-G3 ([KI03] at n = 3): V_T = V_0 (tensor, l >= 2), V_V = (k + 3/4) U - (27/4) Q
  (vector, l >= 2), V_S = f Q_S/(16 r^2 H^2) (scalar, l >= 2), H = m + 6 y, m = k - 3.
Every potential is P(y), V' = -(2 f/r^3) P'(y). For a multiplier phi = tanh g (g' > 0, g(x_c) = 0) Lemma E2.8 needs
w := -phi V' - phi'''/2 >= 0 on R, and then for real sigma != 0, f in L^2(I), I = {r in [1.2, 4]}, u the outgoing
solution: ||chi_I R(sigma) chi_I||_(L^2(dr_*)) <= B(sigma) := ((2/m' + (M' + 2|sigma|)^2/w_I)/w_I)^(1/2), m' = min_I
phi', M' = max_I phi', w_I = min_I w (and with 4|sigma| for Im sigma > 0, Lemma E2.10).

  M0 (exact) the potentials as P(y): V_0, V_1, V_2, V_V are a U + b Q with a = k + 3/4 and b = 9/4, 5/4, -7/4, -27/4
     (from the record's printed forms); V_S = a U - (39/4) Q + U g_m, g_m = 24 y (5 y - 3)/H + 288 y^2 (1 - y)/H^2
     (exact partial fraction of Q_S/(16 H^2)), so P_S' = P'_(a, -39/4) + E(y, 1/m) with E printed; U' = (2 f/r^3)(2y - 1)
     changes sign exactly at r = 2^(1/2), so for a multiplier centred at the photon sphere -phi U' >= 0 on R and w is
     nondecreasing in a and affine in b: a certificate at (a_0, b_lo) and (a_0, b_hi) covers every a >= a_0,
     b in [b_lo, b_hi] with the same m', M' and w_I >= the two endpoints' least.
  M1 (certified) family A, phi_A = tanh g (centre r_*(2^(1/2)), s_L = 23/25, s_R = 4, k_s = 1): w >= 0 on R at
     (a, b) = (15/4, 5/4), (15/4, 9/4): V_0 and V_1 at every l >= 1.
  M2 (certified) family B, (s_L, s_R, k_s) = (49/50, 4, 1): (35/4, -7/4), (35/4, 9/4): V_0, V_1, V_2, V_T at l >= 2.
  M3 (certified) family C, (49/50, 2, 1): (63/4, -39/4), (63/4, 9/4): every master potential a U + b Q with
     b in [-39/4, 9/4] at l >= 3, so V_V at l >= 3.
  M4 (certified) V_S for every l >= 4: with phi_C, W_S := w_(99/4, -39/4) - |phi| (2 f/r^3) sup_(eps in [0, 1/21]) |E(y,
     eps)| >= 0 on R (E enclosed over eight eps-subintervals); then w_S(l) >= W_S for every m >= 21.
  M5 (certified) the harmonics the families do not reach, each with its own multiplier (no monotonicity needed): V_2 at
     l = 1 and V_V at l = 2 and V_S at l = 2 (centre shifted to r_* = r_*(2^(1/2)) + 3/10, 4/5, 7/10; s_L = 49/50,
     s_R = 3/2, k_s = 1/2), V_S at l = 3 (phi_C).
  M6 (certified) the constants and the bounds: m', M', w_I for each certificate, B at sigma = 0+, 1, 3, 10, and the
     table of every master operator's bound for every l in its range; V_0 at l = 0 is E2-PILOT 3g's (cited).
  M7 (deduced; exact identities) the transfer to the operators' own blocks: with the record's master relations rerun
     (modes5.py M2, M3; gmodes5.py G1, imported) and the exact pointwise norm identities, ||chi_I u|| <= (max_I f) B
     ||F|| with max_I f = 15/16, for box on functions, box on the vector-type 1-form blocks (V_1), and 2 L_b0 on the
     tensor-type blocks (V_T; the gauge terms vanish on TT angular tensors): in L^2(I x S^3, r^3 dr dw), SO(4)-
     invariant, so the bound over all such blocks is the sup over l (Schur).
  Controls (each mutates the computed path and must fail): C1 family C's multiplier with its centre moved to
  r_*(2^(1/2)) + 1/2: -phi U' < 0 at a point (certified), so the monotonicity in a fails; C2 V_V at l = 1 (the
  exceptional Killing sector, a = 15/4, b = -27/4) with phi_A: the bisection fails and a point value is certified < 0;
  C3 the V_S majorant at l >= 3 (m >= 12, eps <= 1/12) with phi_C: fails (a point value certified < 0); C4 family B with
  s_L = 3/2: the left tail's exponent 2 (1/s_L - 1) is negative, so the tail bound grows toward the horizon.

    python3 checks/inverse6_5m.py [--selftest]          (tens of minutes on a loaded machine)
"""
import builtins
import contextlib
import io
import math
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr

import sympy as sp
from mpmath import iv, mp, mpf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import e2certify5 as EC                 # noqa: E402  (r_*(t), imported, not copied)

iv.dps = 30
mp.prec = iv.prec
OK = {}
TL, RR = -120, 120                          # bisection range t in [TL, ln(RR - 1)], as e2certify5


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def Q(x):
    x = Fr(x)
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


dec = EC.dec
X_PH = EC.xr(iv.log(iv.sqrt(2) - 1))         # r_*(2^(1/2))


# ------------------------------------------------------------------------------------------------- potentials
def poly_iv(coeffs, Y):
    """coeffs: integers or Fractions, ascending powers"""
    out = iv.mpf(0)
    for c in reversed(coeffs):
        out = out * Y + Q(c)
    return out


def Pp_ab(a, b):
    a, b = Fr(a), Fr(b)
    return lambda Y: Q(a) * (1 - 2 * Y) + Q(b) * (2 * Y - 3 * Y**2)


Y_, M_, E_ = sp.symbols('y m epsilon', positive=True)


def vs_exact():
    H = M_ + 6 * Y_
    QS = 1296 * Y_**3 + (624 * M_ - 144) * Y_**2 + 36 * M_ * (M_ - 12) * Y_ + 16 * M_**3 + 60 * M_**2
    h = QS / (16 * H**2)
    a = M_ + sp.Rational(15, 4)
    part = a - sp.Rational(39, 4) * Y_ + 24 * Y_ * (5 * Y_ - 3) / H + 288 * Y_**2 * (1 - Y_) / H**2
    ok_pf = sp.simplify(h - part) == 0
    Pp = sp.factor(sp.together(sp.diff((1 - Y_) * Y_ * h, Y_)))
    num, den = sp.fraction(Pp)
    ok_den = sp.expand(den - 4 * H**3) == 0
    g = 24 * Y_ * (5 * Y_ - 3) * E_ / (1 + 6 * Y_ * E_) + 288 * Y_**2 * (1 - Y_) * E_**2 / (1 + 6 * Y_ * E_)**2
    E = sp.factor(sp.together(sp.diff((1 - Y_) * Y_ * g, Y_)))
    en, ed = sp.fraction(E)
    ok_ed = sp.expand(ed - (1 + 6 * Y_ * E_)**3) == 0
    Pab = a * (1 - 2 * Y_) - sp.Rational(39, 4) * (2 * Y_ - 3 * Y_**2)
    ok_split = sp.simplify(Pp - Pab - E.subs(E_, 1 / M_)) == 0
    return ok_pf and ok_den and ok_ed and ok_split, sp.expand(num), sp.expand(en), E


VS_NUM = VS_EN = None


def Pp_S(m):
    """P_S'(y) = N_m(y)/(4 (m + 6 y)^3), N_m with integer coefficients"""
    cs = sp.Poly(VS_NUM.subs(M_, m), Y_).all_coeffs()[::-1]
    cs = [Fr(int(c)) for c in cs]
    return lambda Y: poly_iv(cs, Y) / (4 * (Q(m) + 6 * Y)**3)


def E_mag(eps_hi, nsub=8):
    """Y -> an upper bound of sup_(eps in [0, eps_hi]) |E(Y, eps)| (interval enclosure on nsub eps-pieces)"""
    P = sp.Poly(VS_EN, Y_, E_)
    terms = [(i, j, Fr(int(c))) for (i, j), c in zip(P.monoms(), P.coeffs())]
    pieces = [(Fr(eps_hi) * k / nsub, Fr(eps_hi) * (k + 1) / nsub) for k in range(nsub)]

    def f(Y):
        best = mpf(0)
        for lo, hi in pieces:
            e = iv.mpf([Q(lo).a, Q(hi).b])
            num = sum((Q(c) * Y**i * e**j for i, j, c in terms), iv.mpf(0))
            val = num / (1 + 6 * Y * e)**3
            best = max(best, abs(val.a), abs(val.b))
        return best
    return f


# ------------------------------------------------------------------------------------------------- multiplier
class Mult:
    """phi = tanh g, g(x_c) = 0, g' = 1/s_R + (1/s_L - 1/s_R)/(1 + e^((r_* - x_c)/k_s)); requires s_L <= s_R"""

    def __init__(self, sL, sR, ks, off=Fr(0)):
        self.sL, self.sR, self.ks = Q(sL), Q(sR), Q(ks)
        self.fr = (Fr(sL), Fr(sR), Fr(ks), Fr(off))
        assert Fr(sL) <= Fr(sR)
        self.D = 1 / self.sL - 1 / self.sR
        self.xc = X_PH + Q(off)

    def g_all(self, X):
        d = X - self.xc
        zs = d / self.ks
        if zs.a > 0:
            lg = zs + iv.log(1 + iv.exp(-zs))
        else:
            lg = iv.log(1 + iv.exp(zs))
        g = d / self.sL + self.D * self.ks * (iv.log(2) - lg)
        E = iv.exp(zs) if zs.b < 0 else None
        if E is None:
            Em = iv.exp(-zs)
            sig = Em / (1 + Em)
            s1 = Em / (1 + Em)**2
            s2 = -Em * (Em - 1) / (1 + Em)**3
        else:
            sig = 1 / (1 + E)
            s1 = E / (1 + E)**2
            s2 = -E * (1 - E) / (1 + E)**3
        g1 = 1 / self.sR + self.D * sig
        g2 = -self.D * s1 / self.ks
        g3 = self.D * s2 / self.ks**2
        return g, g1, g2, g3

    def phis(self, X):
        g, g1, g2, g3 = self.g_all(X)
        if g.b < -3 or g.a > 3:
            Ex = iv.exp(2 * g) if g.b < 0 else iv.exp(-2 * g)
            S2 = 4 * Ex / (1 + Ex)**2
            T = (1 - Ex) / (1 + Ex) * (-1 if g.b < 0 else 1)
        else:
            Ex = iv.exp(2 * g)
            T = 1 - 2 / (Ex + 1)
            S2 = 1 - T**2
        ph1 = S2 * g1
        ph3 = S2 * g3 - 6 * T * S2 * g1 * g2 + (4 * T**2 - 2 * S2) * S2 * g1**3
        return T, ph1, ph3, g

    def K(self):
        """upper bound of |g'''| + 6 |g'| |g''| + 4 |g'|^3 on R (|sigma'| <= 1/4, |sigma''| <= 1/10, g' <= 1/s_L)"""
        return self.D / (10 * self.ks**2) + 6 * self.D / (4 * self.ks * self.sL) + 4 / self.sL**3


def w_of(tt, mult, Pp, emag=None):
    e = iv.exp(tt)
    r = 1 + e
    Y = 1 / r**2
    f = e * (2 + e) / r**2
    X = EC.xr(tt)
    T, ph1, ph3, _ = mult.phis(X)
    pre = 2 * f / r**3
    w = T * pre * Pp(Y) - ph3 / 2
    if emag is not None:
        Tm = max(abs(T.a), abs(T.b))
        w = w - iv.mpf(Tm) * pre * iv.mpf(emag(Y))
    return w


def certify_positive(mult, Pp, emag=None, t0=TL, t1=None, minw=mpf('1e-9')):
    if t1 is None:
        t1 = iv.log(iv.mpf(RR) - 1).b
    stack, n, acc = [(mpf(t0), mpf(t1))], 0, 0
    while stack:
        lo, hi = stack.pop()
        val = w_of(iv.mpf([lo, hi]), mult, Pp, emag)
        n += 1
        if val.a >= 0:
            acc += 1
            continue
        if hi - lo < minw:
            return False, n, (lo, hi, val)
        mid = (lo + hi) / 2
        stack += [(lo, mid), (mid, hi)]
    return True, n, None


def tails(mult, Pp, emag=None):
    """left: ratio (phi'''/2)/(-phi V') <= K_L e^(2 r_*(1/s_L - 1)) for r_* <= X_L, decreasing toward the horizon iff
    s_L < 1; right: <= K_R e^(-2 (r_* - x_c)/s_R)(r_* + d_R)^3, decreasing once r_* + d_R > 3 s_R/2"""
    tL = iv.mpf(TL)
    eL = iv.exp(tL)
    rL = 1 + eL
    XL = EC.xr(tL)
    yL = 1 / rL**2
    YL = iv.mpf([yL.a, 1])
    betaL = (-Pp(YL)).a - (emag(YL) if emag else 0)
    gL = mult.phis(XL)[3]
    thL = (1 - iv.exp(2 * gL)) / (1 + iv.exp(2 * gL))          # tanh|g_L|, g_L < 0
    KL = 2 * mult.K() * iv.exp(2 * mult.D * mult.ks * iv.log(2)) * iv.exp(-2 * mult.xc / mult.sL)
    den = thL * 8 * iv.exp(-2 * rL) / rL**5 * iv.mpf(betaL)
    rhoL = KL / den * iv.exp(2 * XL * (1 / mult.sL - 1))
    expoL = 1 / mult.sL - 1
    rR = iv.mpf(RR)
    XR = EC.xr(iv.log(rR - 1))
    dR = -iv.log((rR - 1) / (rR + 1)) / 2
    yR = 1 / rR**2
    YR = iv.mpf([0, yR.b])
    betaR = Pp(YR).a - (emag(YR) if emag else 0)
    gR = mult.phis(XR)[3]
    thR = (1 - iv.exp(-2 * gR)) / (1 + iv.exp(-2 * gR))
    KR = 2 * mult.K() * iv.exp(-2 * (XR - mult.xc) / mult.sR)
    rhoR = KR * (XR + dR)**3 / (2 * thR * (1 - yR) * iv.mpf(betaR))
    mono = XR + dR - 3 * mult.sR / 2
    good = betaL > 0 and betaR > 0 and rhoL.b < 1 and expoL.a > 0 and rhoR.b < 1 and mono.a > 0
    return good, rhoL, rhoR, expoL


def constants(mult, Pps, emag=None, pieces=2000):
    tIa, tIb = mpf(iv.log(iv.mpf('0.2')).a), mpf(iv.log(iv.mpf(3)).b)
    ends = [tIa + (tIb - tIa) * k / pieces for k in range(pieces)] + [tIb]
    wI = None
    m1, M1 = None, None
    for ta, tb in zip(ends[:-1], ends[1:]):
        tt = iv.mpf([ta, tb])
        X = EC.xr(tt)
        ph1 = mult.phis(X)[1]
        m1 = ph1.a if m1 is None or ph1.a < m1 else m1
        M1 = ph1.b if M1 is None or ph1.b > M1 else M1
        for Pp in Pps:
            v = w_of(tt, mult, Pp, emag).a
            wI = v if wI is None or v < wI else wI
    return wI, m1, M1


def bound(wI, m1, M1, sigma):
    wI, m1, M1 = iv.mpf(wI), iv.mpf(m1), iv.mpf(M1)
    return iv.sqrt((2 / m1 + (M1 + 2 * Q(sigma))**2 / wI) / wI).b


def certificate(name, mult, Pps, emag=None, verbose=True):
    t0 = time.time()
    good, ns = True, []
    for Pp in Pps:
        g_, n_, bad = certify_positive(mult, Pp, emag)
        tl, rl, rr, ex = tails(mult, Pp, emag)
        good &= g_ and tl
        ns.append(n_)
        if not (g_ and tl) and verbose:
            print('      %s: bisection %s, tails %s (left %s, right %s)%s' % (name, g_, tl, iv.nstr(rl, 4),
                                                                          iv.nstr(rr, 4), '' if g_ else ' at %s'
                                                                          % (bad[:2],)))
    wI, m1, M1 = constants(mult, Pps, emag)
    good &= wI > 0 and m1 > 0
    rho = tails(mult, Pps[0], emag)
    Bs = [bound(wI, m1, M1, s) for s in (0, 1, 3, 10)] if good else []
    if verbose:
        sL, sR, ks, off = mult.fr
        print('  %s: (s_L, s_R, k_s, centre offset) = (%s, %s, %s, %s): w >= 0 on R %s (%s enclosures; left tail '
              'ratio <= '
              '%s, right <= %s); min_I w >= %s, m\' >= %s, M\' <= %s; B(0+, 1, 3, 10) <= %s (%.0f s)'
              % (name, sL, sR, ks, off, good, '+'.join(str(n) for n in ns), dec(rho[1].b, 3, True),
                 dec(rho[2].b, 3, True), dec(wI, 5, False), dec(m1, 5, False), dec(M1, 5, True),
                 ', '.join(dec(b, 4, True) for b in Bs) if Bs else '-', time.time() - t0), flush=True)
    return good, (wI, m1, M1, Bs)


def point_negative(mult, Pp, emag=None, tmin=-6, tmax=5, n=2000):
    """a certified negative point value of w (control): scan a float grid, certify the least at a point"""
    best = None
    for k in range(n + 1):
        t = mpf(tmin) + (mpf(tmax) - mpf(tmin)) * k / n
        v = w_of(iv.mpf(t), mult, Pp, emag)
        if best is None or v.b < best[1].b:
            best = (t, v)
    return best[1].b < 0, best


# ------------------------------------------------------------------------------------------------- main
def main():
    global VS_NUM, VS_EN
    T0 = time.time()
    ok0, VS_NUM, VS_EN, Esym = vs_exact()
    r, mu, k = sp.symbols('r mu k', positive=True)
    f = 1 - mu / r**2
    U, Qf = f / r**2, f * mu / r**4
    rec = {'V_0': (f / r**2 * (k + sp.Rational(3, 4) + 9 * mu / (4 * r**2)), sp.Rational(9, 4)),
           'V_1': (f / r**2 * ((k + 1) - sp.Rational(1, 4) + 5 * mu / (4 * r**2)), sp.Rational(5, 4)),
           'V_2': (f / r**2 * (k + sp.Rational(3, 4) - 7 * mu / (4 * r**2)), sp.Rational(-7, 4)),
           'V_V': (f / r**2 * ((k - 1) + 1 + sp.Rational(3, 4) - 27 * mu / (4 * r**2)), sp.Rational(-27, 4))}
    # V_1: lambda - 1/4 with lambda = (l + 1)^2 = k + 1; V_V: k_V^2 + 7/4 with k_V^2 = k - 1 (gmodes5 G2)
    ok_ab = all(sp.simplify(V - ((k + sp.Rational(3, 4)) * U + b * Qf)) == 0 for V, b in rec.values())
    rr_ = sp.Symbol('rr', positive=True)
    Up = sp.simplify(sp.diff(((1 - 1 / rr_**2) / rr_**2), rr_) * (1 - 1 / rr_**2))
    ok_U = sp.solve(sp.numer(sp.together(Up)), rr_) == [sp.sqrt(2)] or set(sp.solve(sp.numer(sp.together(Up)), rr_)) \
        == {1, sp.sqrt(2)}
    OK['M0'] = ok0 and ok_ab and ok_U
    print('  M0 (exact): V_0, V_1, V_2, V_V = (k + 3/4) U + b Q with b = 9/4, 5/4, -7/4, -27/4: %s; V_S = a U - (39/4) Q'
          ' + U g_m and P_S\' = P\'_(a, -39/4) + E(y, 1/m), E = %s: %s; U\' vanishes on r > 1 only at r = 2^(1/2): %s'
          % (ok_ab, sp.factor(Esym), ok0, ok_U))

    fam = {}
    A = Mult(Fr(23, 25), 4, 1)
    B = Mult(Fr(49, 50), 4, 1)
    C = Mult(Fr(49, 50), 2, 1)
    OK['M1'], fam['A'] = certificate('M1 family A, l >= 1, b in [5/4, 9/4] (V_0, V_1)', A,
                                     [Pp_ab(Fr(15, 4), Fr(5, 4)), Pp_ab(Fr(15, 4), Fr(9, 4))])
    OK['M2'], fam['B'] = certificate('M2 family B, l >= 2, b in [-7/4, 9/4] (V_0, V_1, V_2, V_T)', B,
                                     [Pp_ab(Fr(35, 4), Fr(-7, 4)), Pp_ab(Fr(35, 4), Fr(9, 4))])
    OK['M3'], fam['C'] = certificate('M3 family C, l >= 3, b in [-39/4, 9/4] (V_V and all aU + bQ)', C,
                                     [Pp_ab(Fr(63, 4), Fr(-39, 4)), Pp_ab(Fr(63, 4), Fr(9, 4))])
    OK['M4'], fam['S4'] = certificate('M4 V_S, every l >= 4 (majorant, eps <= 1/21)', C,
                                      [Pp_ab(Fr(99, 4), Fr(-39, 4))], emag=E_mag(Fr(1, 21)))
    ind = {}
    g1, ind['V_2 l=1'] = certificate('M5 V_2 at l = 1', Mult(Fr(49, 50), Fr(3, 2), Fr(1, 2), Fr(3, 10)),
                                     [Pp_ab(Fr(15, 4), Fr(-7, 4))])
    g2, ind['V_V l=2'] = certificate('M5 V_V at l = 2', Mult(Fr(49, 50), Fr(3, 2), Fr(1, 2), Fr(4, 5)),
                                     [Pp_ab(Fr(35, 4), Fr(-27, 4))])
    g3, ind['V_S l=2'] = certificate('M5 V_S at l = 2', Mult(Fr(49, 50), Fr(3, 2), Fr(1, 2), Fr(7, 10)), [Pp_S(5)])
    g4, ind['V_S l=3'] = certificate('M5 V_S at l = 3', C, [Pp_S(12)])
    OK['M5'] = g1 and g2 and g3 and g4

    # M6: the table
    def Bs(key, d):
        return d[key][3]
    table = [('V_0 (scalar step), l = 0', None, 'E2-PILOT 3g: 164.5, 183.5, 275.2, 725.0 (cited)'),
             ('V_0, V_1, l = 1', fam['A'][3], None), ('V_0, V_1, V_2, V_T, l >= 2', fam['B'][3], None),
             ('V_2, l = 1', ind['V_2 l=1'][3], None), ('V_V, l = 2', ind['V_V l=2'][3], None),
             ('V_V, l >= 3', fam['C'][3], None), ('V_S, l = 2', ind['V_S l=2'][3], None),
             ('V_S, l = 3', ind['V_S l=3'][3], None), ('V_S, l >= 4', fam['S4'][3], None)]
    OK['M6'] = all((b is not None and len(b) == 4) or c for _, b, c in table)
    for name, b, c in table:
        print('  M6 %s: ||chi_I R(sigma) chi_I|| <= %s at sigma = 0+, 1, 3, 10' %
              (name, c if c else ', '.join(dec(x, 4, True) for x in b)))
    worst = [max(b[i] for _, b, c in table if b) for i in range(4)]
    print('  M6 every master operator of III.D (M2)-(M4) and of III.F\'\' Theorem 2.2, every l in its range (l = 0 of '
          'V_0'
          ' by E2-PILOT 3g): ||chi_I R(sigma) chi_I|| <= max(the rows) = %s at sigma = 0+, 1, 3, 10, and at every real'
          ' sigma != 0 by B(sigma), increasing in |sigma|' % ', '.join(dec(x, 4, True) for x in worst))

    # M7: the exact transfers to the operators' own blocks (deduced from the record's identities, rerun here)
    with contextlib.redirect_stdout(io.StringIO()):
        import modes5 as MO                  # noqa: E402  (III.D (M2)-(M3), imported, not copied)
        import gmodes5 as GM                 # noqa: E402  (III.F'' / [KI03] tensor type, imported, not copied)
        rec_ok = MO.m2() and MO.m3() and GM.g1()
    rr, Ph, gg, KK, FY = sp.symbols('r Phi g K F_Y', positive=True)
    ff = 1 - 1 / rr**2
    # pointwise, per unit dr_* (dr = f dr_*), harmonic norms factored out:
    # scalar u = r^-3/2 Phi S, source g, G = f r^3/2 g;  vector A = r^-1/2 Phi Y, |A|^2 = r^-3 |Phi|^2, G = f r^1/2 F_Y,
    # |F|^2 = r^-2 |F_Y|^2;  tensor h = 2 r^2 H T, H = r^-3/2 Phi, F = 2 r^2 K T, G = 2 f r^3/2 K
    rows7 = {'scalar': ((rr**-3 * Ph**2) * rr**3 * ff, (ff * rr**sp.Rational(3, 2) * gg)**2, gg**2 * rr**3 * ff, 1),
             'vector 1-form': ((rr**-3 * Ph**2) * rr**3 * ff, (ff * rr**sp.Rational(1, 2) * FY)**2,
                               rr**-2 * FY**2 * rr**3 * ff, 1),
             'tensor 2-tensor': (4 * rr**-3 * Ph**2 * rr**3 * ff, (2 * ff * rr**sp.Rational(3, 2) * KK)**2,
                                 4 * KK**2 * rr**3 * ff, 4)}
    ok7 = rec_ok
    for name, (un, Gn, Fn, c) in rows7.items():
        # ||u|| <= c^(1/2) max f B ||F||
        ok7 &= sp.simplify(un - c * ff * Ph**2) == 0 and sp.simplify(Gn / Fn - ff) == 0
    fmax = (1 - sp.Rational(1, 16))
    ok7 &= fmax == sp.Rational(15, 16) and sp.diff(ff, rr).subs(rr, sp.Rational(6, 5)) > 0
    # ||u||_I^2 = c int f |Phi|^2, ||G||^2 <= max_I f ||F||_I^2 / c'...: ||u||_I <= (max_I f) B ||F||_I in every case
    OK['M7'] = ok7
    tf = lambda b: [dec((Q(Fr(15, 16)) * iv.mpf(x)).b, 4, True) for x in b]
    print('  M7 (deduced; the identities rerun: modes5 M2, M3 and gmodes5 G1: %s) on I x S^3 with r^3 dr dw and the '
          'static frame\'s pointwise norm, ||u||_I = c^(1/2) (int_I f |Phi|^2 dr_*)^(1/2) and ||G||_I <= (max_I '
          'f)^(1/2) ||F||_I/c^(1/2) (pointwise identities exact: %s), max_I f = 15/16; so, Phi being the outgoing '
          'solution (the class of '
          'III.D Proposition 6.2 and III.F\'\' Proposition 3.1): ||chi_I box-hat(sigma)^-1 chi_I|| <= (15/16) B on '
          'functions (E2-PILOT\'s B) and on the vector-type 1-form blocks (V_1: l = 1 %s, l >= 2 %s), and '
          '||chi_I (2 L-hat_b0(sigma))^-1 chi_I|| <= (15/16) B_T on the tensor-type blocks (l >= 2 %s), at sigma = '
          '0+, 1, '
          '3, 10' % (rec_ok, ok7, ', '.join(tf(fam['A'][3])), ', '.join(tf(fam['B'][3])),
                     ', '.join(tf(fam['B'][3]))))

    # controls
    Cs = Mult(Fr(49, 50), 2, 1, Fr(1, 2))
    tm = iv.log(iv.mpf('1.45') - 1)
    e = iv.exp(tm)
    rr = 1 + e
    Y = 1 / rr**2
    ff = e * (2 + e) / rr**2
    T = Cs.phis(EC.xr(tm))[0]
    negU = (-T * (2 * ff / rr**3) * (2 * Y - 1)).b < 0
    OK['C1'] = negU
    print('  C1 (control): family C\'s multiplier centred at r_*(2^(1/2)) + 1/2: -phi U\' at r = 1.45 <= %s < 0, the '
          'monotonicity in a fails: %s' % (dec((-T * (2 * ff / rr**3) * (2 * Y - 1)).b, 4, True), OK['C1']))
    gb, n_, bad = certify_positive(A, Pp_ab(Fr(15, 4), Fr(-27, 4)))
    neg2, best2 = point_negative(A, Pp_ab(Fr(15, 4), Fr(-27, 4)))
    OK['C2'] = (not gb) and neg2
    print('  C2 (control): V_V at l = 1 with phi_A: the bisection fails (%s) and w <= %s at t = %s: %s'
          % (not gb, dec(best2[1].b, 4, True), iv.nstr(iv.mpf(best2[0]), 5), OK['C2']))
    neg3, best3 = point_negative(C, Pp_ab(Fr(63, 4), Fr(-39, 4)), emag=E_mag(Fr(1, 12)), tmin=-8, tmax=-2)
    OK['C3'] = neg3
    print('  C3 (control): the V_S majorant from l = 3 (eps <= 1/12) with phi_C: W_S <= %s at t = %s: %s'
          % (dec(best3[1].b, 4, True), iv.nstr(iv.mpf(best3[0]), 5), OK['C3']))
    Bb = Mult(Fr(3, 2), 4, 1)
    _, _, _, ex = tails(Bb, Pp_ab(Fr(35, 4), Fr(-7, 4)))
    OK['C4'] = ex.b < 0
    print('  C4 (control): family B with s_L = 3/2: 1/s_L - 1 = %s < 0, the left tail bound grows toward the horizon: %s'
          % (iv.nstr(ex, 4), OK['C4']))
    print('  (%.0f s)' % (time.time() - T0))
    for k_, v_ in OK.items():
        builtins.print(k_, 'PASS' if v_ else 'FAIL')
    if '--selftest' in sys.argv:
        sys.exit(0 if all(OK.values()) else 1)


if __name__ == '__main__':
    main()
