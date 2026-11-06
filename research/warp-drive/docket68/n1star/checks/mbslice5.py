#!/usr/bin/env python3
"""mbslice5: Theorem T (iii) and Lemma X1 of FAMILIES5-MB.md on every class slice, as exact polynomial identities
(FAMILIES5-MB.md section 2, minor 1 of its round-8 review; mbsign5 E2-E3 check them at three slice points only).

The slices. A class slice of Tangherlini in ingoing coordinates is v = V(R) with w := V' > 0 and f w < 2 (spacelike),
f = 1 - mu/R^2. Every such slice is w = 2/(f + q^2) with q := sqrt(2/w - f) > 0, and then sqrt(gamma_RR) =
sqrt(w (2 - f w)) = 2 q/(f + q^2) (the parametrisation of the round-8 reader of FAMILIES5-MB). With
S := R^2 - mu + R^2 q^2 every slice quantity is a polynomial over a monomial R^a q^b S^c:
    w = 2 R^2/S,  sqrt(gamma_RR) = 2 q R^2/S,  gamma_RR = 4 q^2 R^4/S^2,  N_s = S/(2 q R^2),
    Y_s^R = (R^2 q^2 - R^2 + mu) S/(4 q^2 R^4),  n^R = -(R^2 q^2 - R^2 + mu)/(2 q R^2),
    K_RR = (R^5 w' - R^2 mu w^3 + 3 R^2 mu w^2 + mu^2 w^3)/(R^5 sqrt(gamma_RR))   (mbsign5 E2's closed form),
and R-derivatives are total derivatives in the jets q, q', q'', ... (and S' = 2R + 2R q^2 + 2R^2 q q' is a polynomial).

The route (exact; no simplification, no gcd). Every quantity is held as (numerator, a, b, c), the numerator a
polynomial with rational coefficients in R, mu, the jets of q and the jets of H and P (sympy's sparse polynomial
ring), the denominator R^a q^b S^c. Sums bring both to the larger exponents, products add them, the total derivative
is D(p/(R^a q^b S^c)) = (R q S D p - p (a q S + b R q' S + c R q S'))/(R^(a+1) q^(b+1) S^(c+1)), and only quantities
whose numerator is a constant times a monomial in R, q (times a power of S) are inverted. A rational function of this
form is identically zero iff its numerator polynomial is the zero polynomial, which is read off exactly. The
theta-integrated Q-density of tensor data on an abstract round slice is mbsign5's own (its constraint map, qsign5's
constraints_fast, and its theta integral; mbsign5 is imported, not modified); every abstract slice function and
derivative in it is replaced by the exact quantity above, symbol by symbol.

  S1 Theorem T (iii) on every class slice, l = 2 and l = 4: the Euler operator in H and in P of
     (theta-integrated Q-density) + 2 |T|^2 T_m(xi, n) sqrt(gamma_RR) is the zero rational function of (R, mu, q,
     q', ...): the Q-density is -2 |T|^2 T_m sqrt(gamma_RR) up to a d/dR, on every slice and every mu.
  S2 Lemma X1 on every class slice, l = 2: with P = -(Y_s^R/N_s) H_R the Q-density plus |T|^2 (R^3 f H_R^2 +
     (k_T^2 + 2) R H^2) has zero Euler operator in H; with H = 0 it equals -|T|^2 R^3 P^2 pointwise.
  S3 the slice identities N_s sqrt(gamma_RR) = 1 and N_s^2 - gamma_RR (Y_s^R)^2 = f, exactly in this representation.
  Controls (each must fail, i.e. give a nonzero polynomial): S1 with |T|^2 halved (l = 2, 4); S1 with K_RR's w' term
  dropped (a wrong slice); S2 with k_T^2 + 2 replaced by k_T^2 + 3; S2's pointwise identity with R^3 P^2 doubled.

Labels: computed, exact (polynomial identities over the rationals). Run: python3 checks/mbslice5.py   (a few minutes)
"""
import importlib.util
import os
import sys
import time

import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
T0 = time.time()
NJ = 14                                                          # jets kept for q, H and P


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    sys.argv = sys.argv[:1]                                      # mbsign5 reads its flags from argv at import
    spec.loader.exec_module(m)
    return m


MB = load('mbsign5')
NAMES = ['R', 'mu'] + ['q%d' % k for k in range(NJ)] + ['H%d' % k for k in range(NJ)] + ['P%d' % k for k in range(NJ)]
RING, *GENS = ring(','.join(NAMES), QQ)
RR, MU = GENS[0], GENS[1]
QJ = GENS[2:2 + NJ]
HJ = GENS[2 + NJ:2 + 2 * NJ]
PJ = GENS[2 + 2 * NJ:2 + 3 * NJ]
SS = RR**2 - MU + RR**2 * QJ[0]**2
_SP = [RING(1)]


def spow(k):
    while len(_SP) <= k:
        _SP.append(_SP[-1] * SS)
    return _SP[k]


def Dpoly(p):
    """the total derivative in R of a polynomial in R, mu and the jets"""
    out = p.diff(RR)
    for J in (QJ, HJ, PJ):
        if p.diff(J[-1]) != 0:
            raise RuntimeError("jet order exceeded")
        for k in range(NJ - 1):
            dk = p.diff(J[k])
            if dk:
                out += J[k + 1] * dk
    return out


class RF:
    """num / (R^a q^b S^c)"""
    __slots__ = ('n', 'a', 'b', 'c')

    def __init__(self, n, a=0, b=0, c=0):
        self.n, self.a, self.b, self.c = RING(n), a, b, c

    def lift(self, a, b, c):
        return self.n * RR**(a - self.a) * QJ[0]**(b - self.b) * spow(c - self.c)

    def __add__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        a, b, c = max(self.a, o.a), max(self.b, o.b), max(self.c, o.c)
        return RF(self.lift(a, b, c) + o.lift(a, b, c), a, b, c)
    __radd__ = __add__

    def __neg__(self):
        return RF(-self.n, self.a, self.b, self.c)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, RF) else RF(o)))

    def __rsub__(self, o):
        return RF(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        return RF(self.n * o.n, self.a + o.a, self.b + o.b, self.c + o.c)
    __rmul__ = __mul__

    def inv(self):
        n = self.n
        for k in range(8):
            try:
                m = n.exquo(spow(k))
            except Exception:
                break                                            # not divisible by S^k, so not by S^(k+1)
            if len(m) == 1:
                (mon, cf), = m.terms()
                if all(e == 0 for i, e in enumerate(mon) if i not in (0, 2)):
                    ea, eb = mon[0], mon[2]
                    return RF(RING(1 / cf) * RR**self.a * QJ[0]**self.b * spow(self.c), ea, eb, k)
        raise ValueError("not invertible in this representation")

    def __pow__(self, k):
        if k < 0:
            return self.inv()**(-k)
        out = RF(1)
        for _ in range(k):
            out = out * self
        return out

    def D(self):
        n, a, b, c = self.n, self.a, self.b, self.c
        q0, q1 = QJ[0], QJ[1]
        num = RR * q0 * SS * Dpoly(n) - n * (a * q0 * SS + b * RR * q1 * SS + c * RR * q0 * Dpoly(SS))
        return RF(num, a + 1, b + 1, c + 1)

    def diff(self, g):
        return RF(self.n.diff(g), self.a, self.b, self.c)

    def iszero(self):
        return self.n == 0


# ------------------------------------------------------------------ the slice, exactly
def slice_quantities(drop_wprime=False):
    f = RF(RR**2 - MU, 2)
    w = RF(2 * RR**2, 0, 0, 1)
    ssq = RF(2 * QJ[0] * RR**2, 0, 0, 1)                         # sqrt(gamma_RR)
    G = ssq * ssq
    N = RF(SS, 2, 1, 0)
    Y = RF((RR**2 * QJ[0]**2 - RR**2 + MU) * SS, 4, 2, 0)
    nR = RF(-(RR**2 * QJ[0]**2 - RR**2 + MU), 2, 1, 0)
    R5 = RF(RR**5)
    mu = RF(MU)
    wp = RF(0) if drop_wprime else w.D()
    K = (R5 * wp - RF(RR**2) * mu * w**3 + RF(3 * RR**2) * mu * w**2 + mu * mu * w**3) * (R5 * ssq).inv()
    return dict(f=f, w=w, ss=ssq, G=G, N=N, Y=Y, n=nR, K=K)


def jets_of(x, k):
    out = [x]
    for _ in range(k):
        out.append(out[-1].D())
    return out


class Converter:
    """a sympy expression in R, mu, the abstract slice functions Gf, Kf, nf, Nf, Yf (and sqrt(Gf)), H and P with
    their R-derivatives, and rational numbers -> RF, symbol by symbol"""

    def __init__(self, F, sq, order=8):
        Gf, Kf, nf, Nf, Yf, H, P = F
        self.Rsym = MB.R_
        self.Gf, self.H, self.P = Gf, H, P
        self.jets = {Gf: jets_of(sq['G'], order), Kf: jets_of(sq['K'], order), nf: jets_of(sq['n'], order),
                     Nf: jets_of(sq['N'], order), Yf: jets_of(sq['Y'], order)}
        self.ssj = sq['ss']
        self.memo = {}

    def __call__(self, e):
        if e in self.memo:
            return self.memo[e]
        out = self._conv(e)
        self.memo[e] = out
        return out

    def _conv(self, e):
        if e.is_Rational:
            return RF(QQ(int(e.p), int(e.q)))
        if e == self.Rsym:
            return RF(RR)
        if e == MB.mu:
            return RF(MU)
        if e in self.jets:
            return self.jets[e][0]
        if e == self.H:
            return RF(HJ[0])
        if e == self.P:
            return RF(PJ[0])
        if isinstance(e, sp.Derivative):
            fn = e.expr
            k = sum(c for v, c in e.variable_count)
            if fn in self.jets:
                return self.jets[fn][k]
            if fn == self.H:
                return RF(HJ[k])
            if fn == self.P:
                return RF(PJ[k])
            raise ValueError("unknown derivative %s" % e)
        if e.is_Add:
            out = RF(0)
            for t in e.args:
                out = out + self(t)
            return out
        if e.is_Mul:
            out = RF(1)
            for t in e.args:
                out = out * self(t)
            return out
        if e.is_Pow:
            base, ex = e.args
            if base == self.Gf and ex.is_Rational and ex.q == 2:
                return self.ssj**int(ex.p)
            if ex.is_Integer:
                return self(base)**int(ex)
            raise ValueError("power %s" % e)
        raise ValueError("unknown atom %s" % e)


def euler(L, J):
    """the Euler operator of the RF L in the field whose jets are J"""
    out = RF(0)
    for k in range(NJ - 1):
        dk = L.diff(J[k])
        if dk.iszero():
            continue
        t = dk
        for _ in range(k):
            t = t.D()
        out = out + (t if k % 2 == 0 else -t)
    return out


def main():
    print("mbslice5: Theorem T (iii) and Lemma X1 on every class slice, as exact polynomial identities", flush=True)
    td = MB.tensor_density()
    Gf, Kf, nf, Nf, Yf, H, P = td['F']
    R_ = MB.R_
    HR = sp.diff(H, R_)
    print("   the abstract theta-integrand from mbsign5's constraint map (%.0f s)" % (time.time() - T0), flush=True)
    sq = slice_quantities()
    sq_bad = slice_quantities(drop_wprime=True)
    # S3
    one = sq['N'] * sq['ss'] - RF(1)
    lap = sq['N'] * sq['N'] - sq['G'] * sq['Y'] * sq['Y'] - sq['f']
    s3 = one.iszero() and lap.iszero()
    print("S3 N_s sqrt(gamma_RR) = 1: %s; N_s^2 - gamma_RR (Y_s^R)^2 = f: %s" % (one.iszero(), lap.iszero()))
    print('S3', 'PASS' if s3 else 'FAIL', flush=True)
    ok = s3
    s1, ctl1, ctlK = True, True, True
    iq = {}
    for n in (0, 1):
        A, B, C, kT2, l = MB.class_tt(n)
        nT = sp.integrate(sp.expand(sp.expand_trig((A**2 + B**2 + C**2) * MB.s_ * MB.c_)), (MB.th, 0, sp.pi / 2))
        Iq = MB.theta_integral(td['dens'], td['TA'], n)
        iq[l] = (Iq, nT, kT2)
        Tm = R_**3 * ((Nf * P + Yf * HR) * P + sp.Rational(1, 2) * Nf * (-P**2 + HR**2 / Gf)) \
            + sp.Rational(1, 2) * Nf * (kT2 + 2) * R_ * H**2
        for scale, label in ((1, 'identity'), (sp.Rational(1, 2), '|T|^2 halved')):
            cv = Converter(td['F'], sq)
            L = cv(Iq + 2 * scale * nT * Tm * sp.sqrt(Gf))
            eH, eP = euler(L, HJ), euler(L, PJ)
            z = eH.iszero() and eP.iszero()
            print("   S1, l = %d (|T|^2 = %s, k_T^2 = %d), %s: Euler operator in H zero %s, in P zero %s (numerator terms "
                  "%d, %d; %.0f s)" % (l, nT, kT2, label, eH.iszero(), eP.iszero(), len(eH.n), len(eP.n),
                                       time.time() - T0), flush=True)
            if scale == 1:
                s1 &= z
            else:
                ctl1 &= not z
        if n == 0:
            cv = Converter(td['F'], sq_bad)
            L = cv(Iq + 2 * nT * Tm * sp.sqrt(Gf))
            zb = euler(L, HJ).iszero() and euler(L, PJ).iszero()
            ctlK = not zb
            print("   control: K_RR with its w' term dropped (a wrong slice), l = 2: identity fails (rejected): %s (%.0f s)"
                  % (ctlK, time.time() - T0), flush=True)
    print('S1', 'PASS' if s1 else 'FAIL', flush=True)
    ok &= s1
    # S2: Lemma X1, l = 2
    Iq, nT, kT2 = iq[2]
    cv = Converter(td['F'], sq)
    fR = 1 - MB.mu / R_**2
    res = {}
    for extra, label in ((2, 'identity'), (3, 'k_T^2 + 3')):
        dX = Iq.subs(P, -Yf / Nf * HR).doit() + nT * (R_**3 * fR * HR**2 + (kT2 + extra) * R_ * H**2)
        res[label] = euler(cv(dX), HJ).iszero()
    d0 = Iq.subs(H, 0).doit()
    b_ok = cv(d0 + nT * R_**3 * P**2).iszero()
    b_ctl = not cv(d0 + 2 * nT * R_**3 * P**2).iszero()
    s2 = res['identity'] and b_ok
    print("   S2, l = 2: with P = -(Y_s^R/N_s) H_R, Q-density + |T|^2 (R^3 f H_R^2 + (k_T^2 + 2) R H^2) has zero Euler "
          "operator in H: %s; with H = 0 the Q-density is -|T|^2 R^3 P^2 pointwise: %s (%.0f s)" %
          (res['identity'], b_ok, time.time() - T0), flush=True)
    print("   controls: k_T^2 + 3 in place of k_T^2 + 2 fails (rejected): %s; R^3 P^2 doubled fails (rejected): %s" %
          (not res['k_T^2 + 3'], b_ctl))
    print('S2', 'PASS' if s2 else 'FAIL', flush=True)
    ok &= s2
    ctl = ctl1 and ctlK and not res['k_T^2 + 3'] and b_ctl
    print("controls rejected:", 'PASS' if ctl else 'FAIL')
    print("S1-S3:", 'PASS' if ok else 'FAIL', "(%.0f s)" % (time.time() - T0))
    return 0 if ok and ctl else 1


if __name__ == '__main__':
    sys.exit(main())
