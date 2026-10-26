#!/usr/bin/env python3
"""dualv1_5.py -- the vector type 1 dual states at n = 4 ([Hin26] Proposition 7.4 and Lemma 7.5 in five dimensions):
the checks behind Part III.E' (proof5/PART-III-E2-V1STATES.md, D227).  Labels: computed (exact, sympy).

On Minkowski space R^(1+4) with gbar = -dt^2 + dx^2, W in so(4), V := (W x) . dx (a rotation 1-form, Killing), r = |x|,
c-bar = r^-1 (dt - v dr), (E-bar_C)* h = gam (2 iota_(c-bar#) h - (2/3)(1 - e) c-bar tr h), G-bar h = h - (1/2) gbar tr h,
delta-bar = -div:

  V1 (computed, exact) the leading cancellation.  With h_0 := mu r^-4 (dt + dr) (x)_s V (the leading term of
     delta*_(g_b) V_b, Part III.E' Lemma 2.2) and c_0 := mu (1 + 2 (1 + v) gam) / (3 (1 + 2 v gam)),
     2 (delta-bar + (E-bar_C)*) G-bar (h_0 + delta-bar*(c_0 r^-3 V)) = 0 identically; the two pieces are
     -mu (1 + 2 gam (1 + v)) r^-5 V and 3 c_0 (1 + 2 gam v) r^-5 V.  Control: c_0 (1 + 1/10) leaves a nonzero result.
  V2 (computed, exact) the leading term of h-sharp: h_0 + delta-bar*(c_0 r^-3 V) = mu r^-4 (dt_* + kappa dr) (x)_s V
     with dt_* := dt - dr and kappa := (1 + 2 (v - 1) gam) / (1 + 2 v gam).  Control: kappa with v -> v + 1/7.
  V3 (computed, exact) the pieces: delta-bar* V = 0, delta-bar*(r^-3 V) = -3 r^-4 dr (x)_s V, tr h_0 = 0 (so e drops
     out), delta-bar(f dt (x)_s V) = 0 and delta-bar(f dr (x)_s V) = -(1/2)(f' + 5 f / r) V for f = r^-4.  Control: the
     four-dimensional 3 f / r in place of 5 f / r.
  V4 (computed, exact) the Killing rotations: dim ker ad_A on so(4) for A = a J_12 + b J_34 is 6 at a = b = 0, 4 at
     a = b != 0 and at a = -b != 0, 2 otherwise.  Control: claimed 2 at a = b = 1.

Run: python3 dualv1_5.py (about ten seconds).  The Kerr-Schild family's equivariance and its expansion at every spin are
mp5.py M2-M3.
"""
import sys
import sympy as sp

t, x1, x2, x3, x4 = sp.symbols('t x1 x2 x3 x4', real=True)
X = [t, x1, x2, x3, x4]
xs = [x1, x2, x3, x4]
mu, gam, v, e = sp.symbols('mu gamma v e', positive=True)
r = sp.sqrt(sum(xi**2 for xi in xs))
ginv = [-1, 1, 1, 1, 1]  # gbar and its inverse are diagonal with these entries
POINTS = [(1, 2, 2, 4), (2, 3, 6, 0), (4, 4, 7, 0)]  # |x| = 5, 7, 9
W = sp.Matrix([[0, 1, 2, 3], [-1, 0, 4, 5], [-2, -4, 0, 6], [-3, -5, -6, 0]])


def vec_W(Wm):
    return [0] + [sum(Wm[i, k] * xs[k] for k in range(4)) for i in range(4)]


def sym(a, b):
    return [[sp.Rational(1, 2) * (a[m] * b[n] + a[n] * b[m]) for n in range(5)] for m in range(5)]


def add(h, k, cf=1):
    return [[h[m][n] + cf * k[m][n] for n in range(5)] for m in range(5)]


def scal(f, h):
    return [[f * h[m][n] for n in range(5)] for m in range(5)]


def dstar(w):
    return [[sp.Rational(1, 2) * (sp.diff(w[n], X[m]) + sp.diff(w[m], X[n])) for n in range(5)] for m in range(5)]


def tr(h):
    return sum(ginv[m] * h[m][m] for m in range(5))


def G(h):
    th = tr(h)
    return [[h[m][n] - (sp.Rational(1, 2) * ginv[m] * th if m == n else 0) for n in range(5)] for m in range(5)]


def delta(h):
    return [-sum(ginv[m] * sp.diff(h[m][nn], X[m]) for m in range(5)) for nn in range(5)]


DT = [1, 0, 0, 0, 0]
DR = [0] + [xi / r for xi in xs]


def Estar(h, trace_factor=sp.Rational(2, 3)):
    c = [(DT[m] - v * DR[m]) / r for m in range(5)]
    csharp = [ginv[m] * c[m] for m in range(5)]
    th = tr(h)
    iota = [sum(csharp[m] * h[m][nn] for m in range(5)) for nn in range(5)]
    return [gam * (2 * iota[nn] - trace_factor * (1 - e) * c[nn] * th) for nn in range(5)]


def op(h):
    Gh = G(h)
    d, E = delta(Gh), Estar(Gh)
    return [2 * (d[nn] + E[nn]) for nn in range(5)]


def is_zero_vec(w, extra=None):
    for p in POINTS:
        for c in w:
            val = c.subs(dict(zip(xs, p)))
            if extra:
                val = val.subs(extra)
            if sp.simplify(val) != 0:
                return False
    return True


def run():
    ok = True
    V = vec_W(W)
    c0 = mu * (1 + 2 * (1 + v) * gam) / (3 * (1 + 2 * v * gam))
    h0 = scal(mu / r**4, sym([DT[m] + DR[m] for m in range(5)], V))
    corr = dstar([c0 / r**3 * V[m] for m in range(5)])
    # V1
    res = op(add(h0, corr))
    v1 = is_zero_vec(res)
    pa = op(h0)
    pb = op(corr)
    v1 &= is_zero_vec([pa[m] + mu * (1 + 2 * gam * (1 + v)) / r**5 * V[m] for m in range(5)])
    v1 &= is_zero_vec([pb[m] - 3 * c0 * (1 + 2 * gam * v) / r**5 * V[m] for m in range(5)])
    corr_bad = dstar([c0 * sp.Rational(11, 10) / r**3 * V[m] for m in range(5)])
    ctrl1 = not is_zero_vec(op(add(h0, corr_bad)))
    print('V1 leading cancellation with c_0:', 'PASS' if v1 and ctrl1 else 'FAIL', '(control fails as designed)' if ctrl1 else '')
    ok &= v1 and ctrl1
    # V2
    kappa = (1 + 2 * (v - 1) * gam) / (1 + 2 * v * gam)
    DTS = [DT[m] - DR[m] for m in range(5)]
    lead = scal(mu / r**4, sym([DTS[m] + kappa * DR[m] for m in range(5)], V))
    diff = add(add(h0, corr), lead, -1)
    v2 = is_zero_vec([diff[m][n] for m in range(5) for n in range(5)])
    kb = (1 + 2 * (v + sp.Rational(1, 7) - 1) * gam) / (1 + 2 * (v + sp.Rational(1, 7)) * gam)
    lead_bad = scal(mu / r**4, sym([DTS[m] + kb * DR[m] for m in range(5)], V))
    diffb = add(add(h0, corr), lead_bad, -1)
    ctrl2 = not is_zero_vec([diffb[m][n] for m in range(5) for n in range(5)])
    print('V2 leading term of h-sharp:', 'PASS' if v2 and ctrl2 else 'FAIL', '(control fails as designed)' if ctrl2 else '')
    ok &= v2 and ctrl2
    # V3
    dV = dstar(V)
    v3 = is_zero_vec([dV[m][n] for m in range(5) for n in range(5)])
    dr3 = dstar([V[m] / r**3 for m in range(5)])
    want = scal(-3 / r**4, sym(DR, V))
    v3 &= is_zero_vec([dr3[m][n] - want[m][n] for m in range(5) for n in range(5)])
    v3 &= is_zero_vec([tr(h0)])
    f = 1 / r**4
    fp = -4 / r**5
    v3 &= is_zero_vec(delta(scal(f, sym(DT, V))))
    dd = delta(scal(f, sym(DR, V)))
    v3 &= is_zero_vec([dd[m] + sp.Rational(1, 2) * (fp + 5 * f / r) * V[m] for m in range(5)])
    ctrl3 = not is_zero_vec([dd[m] + sp.Rational(1, 2) * (fp + 3 * f / r) * V[m] for m in range(5)])
    print('V3 the pieces:', 'PASS' if v3 and ctrl3 else 'FAIL', '(control fails as designed)' if ctrl3 else '')
    ok &= v3 and ctrl3
    # V4
    def J(i, j):
        m = sp.zeros(4)
        m[i, j], m[j, i] = 1, -1
        return m
    basis = [J(0, 1), J(2, 3), J(0, 2), J(0, 3), J(1, 2), J(1, 3)]

    def coords(m):
        return [m[0, 1], m[2, 3], m[0, 2], m[0, 3], m[1, 2], m[1, 3]]

    def kerdim(a, b):
        A = a * J(0, 1) + b * J(2, 3)
        M = sp.Matrix([coords(A * B - B * A) for B in basis]).T
        return 6 - M.rank()
    cases = {(0, 0): 6, (1, 1): 4, (2, -2): 4, (1, 2): 2, (1, 0): 2, (0, 3): 2, (sp.Rational(1, 3), sp.Rational(1, 5)): 2}
    v4 = all(kerdim(a, b) == d for (a, b), d in cases.items())
    ctrl4 = kerdim(1, 1) != 2
    print('V4 dim ker ad_A:', 'PASS' if v4 and ctrl4 else 'FAIL', '(control fails as designed)' if ctrl4 else '')
    ok &= v4 and ctrl4
    print('dualv1_5.py:', 'all checks pass' if ok else 'FAILURES')
    return ok


if __name__ == '__main__':
    sys.exit(0 if run() else 1)
