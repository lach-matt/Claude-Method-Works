#!/usr/bin/env python3
"""mpdata5.py -- c3: the data of translated, rotated and boosted Myers-Perry metrics lie in the class of Lemma 0.1.

Lemma 0.1 (supplement proof5/PART-VII-ASSEMBLY.md) asks that the Cartesian components of gamma - delta and k lie in
rho^2 C^inf and rho^3 C^inf of the radial compactification, rho = 1/|x|, x = omega/rho; [Hin26]'s data class contains
the data of every nearby translated, rotated and boosted Myers-Perry metric (the paper's section 8). The Myers-Perry
metric in Kerr-Schild form, g = eta + h (k_mu dx^mu)^2, with spins a, b in the (x1, x2) and (x3, x4) planes, has
k = dt + (r (x1 dx1 + x2 dx2) + a (x1 dx2 - x2 dx1))/(r^2 + a^2) + (the same in (x3, x4) with b), h = mu r^2/(Pi F),
Pi = (r^2 + a^2)(r^2 + b^2), F = 1 - a^2 (x1^2 + x2^2)/(r^2 + a^2)^2 - b^2 (x3^2 + x4^2)/(r^2 + b^2)^2, and r given by
(x1^2 + x2^2)/(r^2 + a^2) + (x3^2 + x4^2)/(r^2 + b^2) = 1.

  B1 (exact) In compactified coordinates u := (r rho)^2 solves a quadratic whose root with u(0) = 1 is a power series in
     rho^2 (its discriminant is 1 + O(rho^2)); so h = rho^2 mu u/((u + a^2 rho^2)(u + b^2 rho^2) F) with F = 1 + O(rho^2)
     and k_i = (u^(1/2) omega_i + a rho omega_i')/(u + a^2 rho^2) are rho^2 C^inf and C^inf: the series to rho^8 have
     only integer powers, h's starting at rho^2 mu (at three rational points of S^3, (a, b) = (1/3, 1/5)).
  B2 (exact) A boost Lambda along x1 (velocity beta), a translation c and a rotation compose with the chart: at t' = 0
     the rest-frame point is x = (gamma x1', x2', x3', x4') - c, and rho_rest/rho' = Q(omega' - rho' c')^(-1/2) with
     Q(y) = gamma^2 y1^2 + y2^2 + y3^2 + y4^2 >= 1 on S^3, analytic at rho' = 0, as is omega_rest; so h and k_mu (whose
     components transform by the constant matrix Lambda) stay rho'^2 C^inf and C^inf (series at three points, beta =
     3/5, c = (1, -2, 1/3, 0)).
  B3 (exact) d/dx_i maps rho^p C^inf to rho^(p+1) C^inf: for F = rho^p f(rho, omega), d_i F = rho^(p+1) (-p omega_i f
     - rho omega_i d_rho f + d_(omega_i) f - omega_i (omega . d_omega) f) (chain rule, f generic). So gamma - delta = h
     k_i k_j and the shift h k_i are rho^2 C^inf, the lapse's square 1 - h + ... is 1 + rho^2 C^inf, d_t' = gamma beta
     d_(x1) of a rest-frame field gains rho, and k = (1/2N)(d_t gamma - D beta - (D beta)^T) is rho^3 C^inf.
  B4 (exact) Directly, for the boosted and translated Tangherlini metric (a = b = 0): gamma - delta and k computed in
     at t' = 0 along x' = omega'/rho' at three rational points, every component a power series in rho' with exact
     coefficients (truncated power-series arithmetic to rho'^7 for the inverse, the lapse and the Christoffel symbols):
     the lowest orders are rho'^2 and rho'^3.
  Control: a mass term falling as rho (h = mu rho, the four-dimensional rate) gives gamma - delta of order rho^1: not in
     the class, and B4's criterion rejects it.

Labels: computed (exact, sympy series). The finite series support the structural statement (compositions of functions
analytic at rho = 0), which is what Lemma 0.1 needs.

Run: python3 checks/mpdata5.py   (about four minutes)
"""
import sys

import sympy as sp

rho, mu, a, b, beta = sp.symbols("rho mu a b beta", positive=True)
w = sp.symbols("w1:5", real=True)
ORDER = 8


POINTS = [(sp.Rational(1, 2),)*4, (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7), 0),
          (sp.Rational(3, 5), 0, 0, sp.Rational(4, 5))]                 # rational points of S^3
AB = (sp.Rational(1, 3), sp.Rational(1, 5))


def powers(e, var, order):
    """(only integer powers?, lowest power) of e's series in var to the given order; a log or a fractional power fails"""
    s = sp.expand(sp.series(e, var, 0, order).removeO())
    if s.has(sp.log):
        return False, None
    pows = set()
    for t in sp.Add.make_args(s):
        if t == 0:
            continue
        p_ = t.as_coeff_exponent(var)[1]
        if not p_.is_integer:
            return False, None
        pows.add(int(p_))
    return True, (min(pows) if pows else None)


def mp_ingredients(om, a_, b_):
    """u = (r rho)^2, h and k_1..k_4 of Myers-Perry along x = omega/rho"""
    A = om[0]**2 + om[1]**2
    B = om[2]**2 + om[3]**2
    disc = (1 - (a_**2 + b_**2)*rho**2)**2 - 4*(a_**2*b_**2*rho**4 - A*b_**2*rho**2 - B*a_**2*rho**2)
    u = (1 - (a_**2 + b_**2)*rho**2 + sp.sqrt(disc))/2
    F = 1 - a_**2*A*rho**2/(u + a_**2*rho**2)**2 - b_**2*B*rho**2/(u + b_**2*rho**2)**2
    h = mu*u*rho**2/((u + a_**2*rho**2)*(u + b_**2*rho**2)*F)
    k = [(sp.sqrt(u)*om[0] - a_*rho*om[1])/(u + a_**2*rho**2), (sp.sqrt(u)*om[1] + a_*rho*om[0])/(u + a_**2*rho**2),
         (sp.sqrt(u)*om[2] - b_*rho*om[3])/(u + b_**2*rho**2), (sp.sqrt(u)*om[3] + b_*rho*om[2])/(u + b_**2*rho**2)]
    eq = sp.simplify(A*(u + b_**2*rho**2) + B*(u + a_**2*rho**2) - (u + a_**2*rho**2)*(u + b_**2*rho**2))
    return u, h, k, eq


def b1(control=False):
    ok, lows = True, []
    for om in POINTS:
        u, h, k, eq = mp_ingredients(om, *AB)
        if control:
            h = mu*rho
        okh, lh = powers(h, rho, ORDER)
        lows.append(lh)
        ok &= okh and (control or (eq == 0 and powers(u, rho, ORDER)[0]
                                   and all(powers(kk, rho, ORDER)[0] for kk in k)
                                   and sp.simplify(sp.series(h, rho, 0, 3).removeO().coeff(rho, 2) - mu) == 0))
    if control:
        return ok and min(lows) >= 2
    print("  B1: at three rational points of S^3, spins (a, b) = (1/3, 1/5): u solves the quadratic, and u, h, k_i have"
          " only integer powers of rho to rho^%d; h starts at mu rho^%s: %s" % (ORDER, min(lows), ok), flush=True)
    return ok and min(lows) == 2


def b2(control=False):
    if control:
        return False
    c = (1, -2, sp.Rational(1, 3), 0)
    bv = sp.Rational(3, 5)
    g = 1/sp.sqrt(1 - bv**2)
    ok = True
    for om in POINTS:
        y = [om[i] - rho*c[i] for i in range(4)]
        Q = g**2*y[0]**2 + y[1]**2 + y[2]**2 + y[3]**2
        exprs = [1/sp.sqrt(Q), g*y[0]/sp.sqrt(Q)] + [y[i]/sp.sqrt(Q) for i in (1, 2, 3)]
        ok &= all(powers(e_, rho, ORDER)[0] for e_ in exprs)
    Qmin = sp.simplify((g**2 - 1)*w[0]**2 + 1)
    print("  B2: rho_rest/rho' and omega_rest analytic at rho' = 0 (integer powers to rho'^%d at three points, beta ="
          " 3/5, c = (1, -2, 1/3, 0)): %s; Q(omega') = %s >= 1 on S^3" % (ORDER, ok, Qmin), flush=True)
    return ok


def b3(control=False):
    if control:
        return False
    x = sp.symbols("x1:5", real=True)
    p = sp.Symbol("p", integer=True)
    R = sp.sqrt(sum(xi**2 for xi in x))
    rr, o = sp.Symbol("rr"), sp.symbols("o1:5")
    f = sp.Function("f")(rr, *o)
    F = R**(-p)*f.subs({rr: 1/R, **{o[i]: x[i]/R for i in range(4)}})
    ok = True
    for i in range(4):
        lhs = sp.diff(F, x[i])
        grad = [sp.diff(f, oi) for oi in o]
        rhs = rr**(p + 1)*(-p*o[i]*f - rr*o[i]*sp.diff(f, rr) + grad[i] - o[i]*sum(o[j]*grad[j] for j in range(4)))
        rhs = rhs.subs({rr: 1/R, **{o[j]: x[j]/R for j in range(4)}})
        ok &= sp.simplify(sp.expand(lhs - rhs)) == 0
    print("  B3: d/dx_i (rho^p f(rho, omega)) = rho^(p+1) (-p omega_i f - rho omega_i f_rho + f_(omega_i) - omega_i"
          " omega . grad_omega f), f generic: %s" % ok, flush=True)
    return ok


class TS:
    """truncated power series in rho with exact coefficients, to order NT"""
    NT = 7

    def __init__(self, c):
        self.c = (list(c) + [0]*(self.NT + 1))[:self.NT + 1]

    @classmethod
    def of(cls, e):
        s = sp.expand(sp.series(e, rho, 0, cls.NT + 1).removeO())
        if s.has(sp.log):
            raise ValueError("log")
        cs = [0]*(cls.NT + 1)
        for t in sp.Add.make_args(s):
            if t == 0:
                continue
            co, p_ = t.as_coeff_exponent(rho)
            if not (p_.is_integer and 0 <= p_ <= cls.NT):
                raise ValueError("power %s" % p_)
            cs[int(p_)] += co
        return cls(cs)

    def __add__(self, o):
        o = o if isinstance(o, TS) else TS([o])
        return TS([a_ + b_ for a_, b_ in zip(self.c, o.c)])

    __radd__ = __add__

    def __neg__(self):
        return TS([-a_ for a_ in self.c])

    def __sub__(self, o):
        return self + (-(o if isinstance(o, TS) else TS([o])))

    def __mul__(self, o):
        if not isinstance(o, TS):
            return TS([a_*o for a_ in self.c])
        out = [0]*(self.NT + 1)
        for i, a_ in enumerate(self.c):
            if a_ == 0:
                continue
            for j in range(self.NT + 1 - i):
                out[i + j] += a_*o.c[j]
        return TS(out)

    __rmul__ = __mul__

    def inv(self):
        c0 = self.c[0]
        out = [sp.Integer(0)]*(self.NT + 1)
        out[0] = 1/c0
        for n in range(1, self.NT + 1):
            out[n] = -sum(self.c[k]*out[n - k] for k in range(1, n + 1))/c0
        return TS(out)

    def sqrt_inv(self):
        """1/sqrt(series) for c0 > 0"""
        c0 = self.c[0]
        x = TS([0] + [ci/c0 for ci in self.c[1:]])
        out, term = TS([1]), TS([1])
        coef = sp.Integer(1)
        for n in range(1, self.NT + 1):
            coef *= (sp.Rational(-1, 2) - n + 1)/n
            term = term*x
            out = out + term*coef
        return out*(1/sp.sqrt(c0))

    def low(self):
        nz = [i for i, ci in enumerate(self.c) if sp.simplify(ci) != 0]
        return nz[0] if nz else None


def b4(control=False):
    xs = sp.symbols("y1:5", real=True)
    t = sp.Symbol("t", real=True)
    bv = sp.Rational(3, 5)
    g = 1/sp.sqrt(1 - bv**2)
    c = [1, -2, sp.Rational(1, 3), 0]
    X = [g*(xs[0] + bv*t) - c[0]] + [xs[i] - c[i] for i in (1, 2, 3)]
    T = g*(t + bv*xs[0])
    R2 = sum(xi**2 for xi in X)
    hh = 1/R2 if not control else 1/sp.sqrt(R2)                            # mu = 1
    kr = [1] + [X[i]/sp.sqrt(R2) for i in range(4)]
    Xs, Y = [T] + X, [t] + list(xs)
    J = sp.Matrix(5, 5, lambda m_, n_: sp.diff(Xs[m_], Y[n_]))
    kp = J.T*sp.Matrix(kr)
    G = J.T*sp.diag(-1, 1, 1, 1, 1)*J + hh*kp*kp.T
    lows_g, lows_k = [], []
    for om in POINTS:
        ray = {xs[i]: om[i]/rho for i in range(4)}
        at = lambda e_: TS.of(e_.subs(t, 0).subs(ray))                      # noqa: E731
        gam = [[at(G[i + 1, j + 1]) for j in range(4)] for i in range(4)]
        dgam = [[[at(sp.diff(G[i + 1, j + 1], xs[k_])) for k_ in range(4)] for j in range(4)] for i in range(4)]
        bet = [at(G[0, i + 1]) for i in range(4)]
        dbet = [[at(sp.diff(G[0, i + 1], xs[k_])) for k_ in range(4)] for i in range(4)]
        dtg = [[at(sp.diff(G[i + 1, j + 1], t)) for j in range(4)] for i in range(4)]
        g00 = at(G[0, 0])
        hmat = [[gam[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)]
        lows_g.append(min(x for x in (hmat[i][j].low() for i in range(4) for j in range(4)) if x is not None))
        if control:
            continue
        gi = [[TS([1 if i == j else 0]) for j in range(4)] for i in range(4)]      # (1 + h)^-1 = 1 - h + h^2 - ...
        term = [[TS([1 if i == j else 0]) for j in range(4)] for i in range(4)]
        for n in range(1, 4):
            term = [[sum((term[i][k_]*hmat[k_][j] for k_ in range(4)), TS([0]))*(-1) for j in range(4)]
                    for i in range(4)]
            gi = [[gi[i][j] + term[i][j] for j in range(4)] for i in range(4)]
        betu = [sum((gi[i][j]*bet[j] for j in range(4)), TS([0])) for i in range(4)]
        N2 = -g00 + sum((betu[i]*bet[i] for i in range(4)), TS([0]))
        Ninv = N2.sqrt_inv()
        Chr = [[[sum((gi[l_][m_]*(dgam[m_][i][j] + dgam[m_][j][i] - dgam[i][j][m_]) for m_ in range(4)), TS([0]))
                 * sp.Rational(1, 2) for j in range(4)] for i in range(4)] for l_ in range(4)]
        low_k = []
        for i in range(4):
            for j in range(i, 4):
                Db = dbet[j][i] + dbet[i][j] - sum((Chr[l_][i][j]*bet[l_] for l_ in range(4)), TS([0]))*2
                kij = (dtg[i][j] - Db)*Ninv*sp.Rational(1, 2)
                low_k.append(kij.low())
        lows_k.append(min(x for x in low_k if x is not None))
    if control:
        return min(lows_g) >= 2
    print("  B4: boosted (beta = 3/5) and translated (c = (1, -2, 1/3, 0)) Tangherlini at t' = 0, at three rational"
          " points of S^3, series in rho' to order %d (exact): gamma - delta starts at rho'^%s, k at rho'^%s; every"
          " series a power series (no log, no fractional power)" % (TS.NT, min(lows_g), min(lows_k)), flush=True)
    return min(lows_g) == 2 and min(lows_k) == 3


CHECKS = [("B1", b1), ("B2", b2), ("B3", b3), ("B4", b4)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
