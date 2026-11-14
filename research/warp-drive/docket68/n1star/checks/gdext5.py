#!/usr/bin/env python3
"""gdext5.py -- GAUGEDECAY5.md Round 4, task 1: (Ext Box), the exterior estimate for the 1-form wave operator near
I_0 and I+, by transposing Part IV (PART-IV-EB.md), IV' (PART-IV2-TAME.md), IV'' (PART-IV3-NM.md) and IV'''
(PART-IV4-SLAB.md) from the gauge-fixed operator L to Box := 2 delta G delta^* on 1-forms.  Computed.

Background near infinity: III.B Lemma 3.5 (b) (as PART-IV4-SLAB.md:71 reads it), g = eta + mu r^-2 (dx^1)^2, x^1 =
t - r, in the Cartesian coordinates (t, x1..x4) of III.B; a Kerr-Schild metric with the eta-null form l = dt - dr, so
det g = -1 and g^-1 = eta^-1 - mu r^-2 l# l#.  Box is computed as d delta + delta d (with sqrt|g| = 1) and checked
against 2 delta G delta^* (the definition, III.D (1.1)), which needs Ric = 0.  Box_0 is the scalar operator
-|g|^-1/2 d_a |g|^1/2 g^ab d_b.  Part IV's chart: rho_0 = (2 - x^1)^-1, rho_I = (2 - x^1)/r, rho = rho_0 rho_I = 1/r,
X_0 = rho_0 d_rho0, X_I = rho_I d_rhoI, x_I = rho_I^(1/2); the conjugated operator is L_Box := rho_I rho^(-7/2) Box
rho^(3/2) (Part IV (2.1)).

  E1 (exact, at integer points with integer r) The 1-form operator in Cartesian components.  (a) det g = -1 and
     g g^-1 = 1.  (b) d delta + delta d = 2 delta G delta^* on test 1-forms (so Ric = 0: this is III.D's Box).
     (c) (Box Z)_c = Box_0 Z_c + C_c^{nu b} d_b Z_nu + D_c^nu Z_nu: no second-order coupling; C and D vanish at mu = 0,
     are t-independent, and are sums sum_{k>=1} mu^k C_k, mu^k D_k with C_k, D_k homogeneous in x of degrees -1-2k and
     -2-2k (so O(r^-3) and O(r^-4), the leading terms of degrees -3 and -4); C_1 is not identically 0.  Controls: (b) on
     the non-vacuum Kerr-Schild metric with mu r^-1 in place of mu r^-2 the two operators differ; (c) in the polar
     component of a 1-form a dr (not Cartesian) the coupling at mu = 0 is 3 a r^-2, of degree -2 and nonzero.
  E2 (exact) The edge-b order of the coupling.  d_t = rho_0 (X_0 - X_I), d_r = rho_0 (-X_0 + (1 - rho_I) X_I) and
     r^-1 d_omega = rho_0 rho_I^(1/2) (x_I d_omega); with the prefactor rho_I rho^-2 and the conjugation by rho^(3/2),
     a coefficient homogeneous of degree -3 (or less) times d_t, d_r, r^-1 d_omega, the conjugation term, and a degree -4
     zeroth-order term all lie in rho_0^2 rho_I^2 C^infty (rho_0, rho_I): so L_Box = L (x) Id + rho_0^2 x_I^4
     Diff^1_eb, the first-order matrix A-bar of Part IV' (1.1) is 0.  Control: a degree -1 coefficient (a connection
     term of a non-Cartesian frame) gives an order-0 eb coefficient, which would enter the leading part.
  E3 (exact) The indicial polynomial at I+.  For the scalar radial operator of g and for the full 1-form Box on
     Z = rho^(3/2) rho_0^a rho_I^lam e_nu (e_nu = dt, dx^1), rho_I rho^(-7/2) (Box Z)/(rho_0^a rho_I^lam) -> -2 lam
     (a - lam) as rho_I -> 0 at fixed rho_0, omega, in the component nu, and 0 in the others: roots lam = 0 (the
     radiation field, I+-order 3/2 for Z) and lam = a (functions of rho = 1/r).  Control: conjugation by rho (n = 3)
     instead of rho^(3/2) does not give -2 lam (a - lam).
  E4 (exact) The normal operator at I_0.  In (tau, rho) = (t/r, 1/r), rho^(-2-alpha) Box_0 (rho^alpha v(tau)) -> (1 -
     tau^2) v'' + c1 v' + c0 v at rho = 0, with the v'' coefficient 1 - tau^2 for every alpha: tau is a b-time function
     on |tau| < 1 for every weight (Part IV Proposition 4.1 applies at every alpha), and the Cartesian coupling is
     rho^2 relative (E1's degrees), so absent from the normal operator.  Control: the polar component's term 3 a r^-2
     survives in rho^-2 Box: 3 at I_0.
  E5 (exact, rational samples) The multiplier.  With A-bar = 0 the quadratic form of Part IV' Proposition 2.2's proof
     on each slot is 4(0 - a_I)|Y|^2 + 4 kappa (a_0 - a_I)|Z|^2, and the angular coefficient of Part IV (3.3) is 1 +
     2(a_0 - a_I) + kappa(1 - 2 a_I): positive for every kappa > 0 iff a_I < min(a_0, 0).  Controls: a_I = 0 and
     a_I = a_0 give a degenerate form.
  E6 (exact, rational samples) The weights of (Ext Box).  dot h on the exterior has I_0-order > 3/2 + 2 gam (Part VIII
     Proposition 1.2 (2)'s proof, polyhomogeneous with min Re E_0 > 3/2 + 2 gam), F_Y = chi E^Ups G dot h one more
     (the factor |x|^-1 of c_Ups), the solution two less, the conjugated source a_0 = (I_0-order of F_Y) - 7/2; the
     interval (beta - 1, min(a_0, 0)) for a_I is non-empty, and p := 3/2 + a_I > 1/2 + beta, for every beta in (0,
     delta_#), delta_# = (1 - e) gam, at every sample; the I+-weight of the conjugated source is >= a_I.  With the
     statement-level weight l_0^flat = 3/2 + delta_#/2 (III.C' Theorem 3.1) the same holds for beta < delta_#/2.
     Controls: (i) with l_0^flat and beta >= delta_#/2 the interval is empty; (ii) without the factor |x|^-1 of c_Ups
     the interval is empty at every sample.

Labels: computed (exact, sympy; E1 at integer points, E5-E6 at exact rational samples).
Run: python3 checks/gdext5.py   (a few minutes)
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

t = sp.Symbol("t", real=True)
XS = sp.symbols("x1:5", real=True)
mu = sp.Symbol("mu", positive=True)
X = [t] + list(XS)
N = 5
RS = sp.Symbol("r", positive=True)
R = RS                     # r = |x| as a symbol; D below differentiates with d_i r = x^i/r (exact chain rule)


def D(e, a):
    """d/dX[a] of an expression in (t, x, r), with r = |x|"""
    if a == 0:
        return sp.diff(e, t)
    return sp.diff(e, XS[a - 1]) + sp.diff(e, RS)*XS[a - 1]/RS

# integer points with integer r: (x1, x2, x3, x4) -> r
PTS = [((1, 2, 2, 4), 5), ((2, 4, 5, 6), 9), ((2, 3, 6, 0), 7), ((1, 1, 1, 1), 2)]


class KS:
    """g = eta + V l l, l = dt - dr; V = mu r^-2 (vacuum) or mu r^-1 (control)"""

    def __init__(self, V):
        ell = [1] + [-xi/R for xi in XS]
        ellup = [-1] + [-xi/R for xi in XS]
        eta = sp.diag(-1, 1, 1, 1, 1)
        self.g = sp.Matrix(N, N, lambda a, b: eta[a, b] + V*ell[a]*ell[b])
        self.gi = sp.Matrix(N, N, lambda a, b: eta[a, b] - V*ellup[a]*ellup[b])
        self._gam = None

    def gam(self):
        if self._gam is None:
            dg = [[[D(self.g[a, b], c) for c in range(N)] for b in range(N)] for a in range(N)]
            self._gam = [[[sp.Rational(1, 2)*sum(self.gi[c, d]*(dg[d][b][a] + dg[d][a][b] - dg[a][b][d])
                                                    for d in range(N))
                           for b in range(N)] for a in range(N)] for c in range(N)]
        return self._gam

    def box0(self, phi):
        return -sum(D(self.gi[a, b]*D(phi, b), a) for a in range(N) for b in range(N))

    def hodge(self, Z):
        gi, g = self.gi, self.g
        dl = -sum(D(gi[a, b]*Z[b], a) for a in range(N) for b in range(N))
        F = [[D(Z[b], a) - D(Z[a], b) for b in range(N)] for a in range(N)]
        Fu = [[sum(gi[a, e]*gi[b, f]*F[e][f] for e in range(N) for f in range(N)) for b in range(N)]
              for a in range(N)]
        divF = [sum(D(Fu[a][b], a) for a in range(N)) for b in range(N)]
        return [D(dl, c) - sum(g[c, b]*divF[b] for b in range(N)) for c in range(N)]

    def two_dGds(self, Z):
        """2 delta G delta^* Z with the Levi-Civita connection"""
        G_, g, gi = self.gam(), self.g, self.gi
        nab = [[D(Z[b], a) - sum(G_[c][a][b]*Z[c] for c in range(N)) for b in range(N)] for a in range(N)]
        k = [[(nab[a][b] + nab[b][a])/2 for b in range(N)] for a in range(N)]
        tr = sum(gi[a, b]*k[a][b] for a in range(N) for b in range(N))
        Gk = [[k[a][b] - g[a, b]*tr/2 for b in range(N)] for a in range(N)]
        out = []
        for b in range(N):
            s_ = 0
            for a in range(N):
                for c in range(N):
                    if gi[a, c] == 0:
                        continue
                    nk = D(Gk[a][b], c) - sum(G_[d][c][a]*Gk[d][b] + G_[d][c][b]*Gk[a][d] for d in range(N))
                    s_ += gi[a, c]*nk
            out.append(-2*s_)
        return out


def at(e, pt, tval=sp.Rational(1, 3), muval=None):
    sub = {t: tval, RS: sp.sqrt(sum(sp.Integer(q)**2 for q in pt))}
    sub.update({XS[i]: sp.Integer(pt[i]) for i in range(4)})
    if muval is not None:
        sub[mu] = muval
    if e == 0:
        return sp.Integer(0)
    return sp.cancel(sp.together(sp.sympify(e).xreplace(sub)))


# --------------------------------------------------------------------------------------------------------------- E1
def e1(control=False):
    V = mu/R if control else mu/R**2
    G = KS(V)
    pts = PTS[:2]
    # (a)
    ok_a = True
    for pt, _ in pts:
        ok_a &= at(G.g.det(), pt) == -1
        ok_a &= all(at(e, pt) == (1 if i % 6 == 0 else 0) for i, e in enumerate(G.g*G.gi))
    # (b) the vacuum identity on test forms
    tests = [[t*XS[0], XS[1]**2, XS[2]*XS[3], t**2, XS[0]*XS[1]]]
    ok_b = True
    for Z in tests:
        H, B = G.hodge(Z), G.two_dGds(Z)
        for pt, _ in pts:
            ok_b &= all(at(H[c] - B[c], pt) == 0 for c in range(N))
    if control:
        print("  E1 control (non-vacuum V = mu/r): d delta + delta d = 2 delta G delta^* on test forms: %s" % ok_b,
              flush=True)
        # (c) control: the polar component of a dr at mu = 0
        G0 = KS(sp.Integer(0))
        a = t
        Z = [0] + [a*xi/R for xi in XS]
        H = G0.hodge(Z)
        rad = sum(H[i + 1]*XS[i]/R for i in range(4)) - G0.box0(a)
        vals = [at(rad*R**2, pt) for pt, _ in pts]
        polar_scalar = all(v == 0 for v in vals)
        print("  E1 control (polar component of a dr, a = t, mu = 0): (Box Z)(d_r) - Box_0 a = (%s) a r^-2, so the "
              "component is scalar: %s" % (vals[0]/sp.Rational(1, 3), polar_scalar), flush=True)
        return ok_b or polar_scalar
    # (c) coupling coefficients from test forms phi e_nu, phi in {1, x^b, x^b x^e}
    DD = [[None]*N for _ in range(N)]
    C = [[[None]*N for _ in range(N)] for _ in range(N)]
    for nu in range(N):
        e = [0]*N
        e[nu] = sp.Integer(1)
        H = G.hodge(e)
        for c in range(N):
            DD[c][nu] = H[c]
        for b in range(N):
            Z = [0]*N
            Z[nu] = X[b]
            H = G.hodge(Z)
            for c in range(N):
                C[c][nu][b] = H[c] - (G.box0(X[b]) if c == nu else 0) - DD[c][nu]*X[b]
    # second-order coupling: for phi = x^b x^e the difference minus C, D terms vanishes
    ok_2 = True
    for nu, b, e_ in [(0, 1, 2), (2, 1, 1), (4, 0, 3)]:
        phi = X[b]*X[e_]
        Z = [0]*N
        Z[nu] = phi
        H = G.hodge(Z)
        for c in range(N):
            rest = H[c] - (G.box0(phi) if c == nu else 0) - sum(C[c][nu][q]*D(phi, q) for q in range(N)) \
                - DD[c][nu]*phi
            for pt, _ in pts[:1]:
                ok_2 &= at(rest, pt) == 0
    ok_mu0 = True
    ok_hom = True
    nonzero = False
    degs = set()

    def mu_coeffs(e):
        P = sp.Poly(sp.expand(e), mu)
        return {m[0]: cf for m, cf in zip(P.monoms(), P.coeffs())}
    for pt, rr in pts:
        p2 = tuple(2*q for q in pt)
        entries = [(DD[c][nu], 2) for c, nu in itertools.product(range(N), range(N))]
        entries += [(C[c][nu][b], 1) for c, nu, b in itertools.product(range(N), range(N), range(N))]
        for e_, base in entries:
            k1 = mu_coeffs(at(e_, pt))
            k2 = mu_coeffs(at(e_, p2, tval=sp.Rational(7, 2)))
            ok_mu0 &= k1.get(0, 0) == 0
            for k in set(k1) | set(k2):
                # the mu^k part is homogeneous of degree -(base + 2k) and t-independent
                ok_hom &= sp.Integer(2)**(base + 2*k)*k2.get(k, 0) == k1.get(k, 0)
                if k1.get(k, 0) != 0:
                    degs.add((base, k))
            if base == 1 and k1.get(1, 0) != 0:
                nonzero = True
    sample = at(C[0][1][0]*R**3, PTS[0][0])
    print("  E1: det g = -1, g g^-1 = 1: %s; d delta + delta d = 2 delta G delta^* (Ric = 0): %s; no second-order "
          "coupling: %s; C, D vanish at mu = 0: %s; C = sum_k mu^k C_k, D = sum_k mu^k D_k with C_k, D_k "
          "t-independent and homogeneous of degrees -1-2k, -2-2k (k >= 1): %s, powers present (C: 1, D: 2; k): %s; "
          "C_1 != 0: %s (e.g. r^3 C_t^{x1 t} = %s at x = (1,2,2,4))"
          % (ok_a, ok_b, ok_2, ok_mu0, ok_hom, sorted(degs), nonzero, sample), flush=True)
    return ok_a and ok_b and ok_2 and ok_mu0 and ok_hom and nonzero


# --------------------------------------------------------------------------------------------------------------- E2
r0, rI, xI = sp.symbols("rho_0 rho_I x_I", positive=True)
TT, RR = sp.symbols("T R", positive=True)


def eb_fields():
    """d_t, d_r in the frame (X_0, X_I), from rho_0 = 1/(2 - t + r), rho_I = (2 - t + r)/r"""
    p0 = 1/(2 - TT + RR)
    pI = (2 - TT + RR)/RR
    back = {TT: 2 - 1/r0 + 1/(r0*rI), RR: 1/(r0*rI)}
    dt = (sp.simplify((sp.diff(p0, TT)/p0).subs(back)), sp.simplify((sp.diff(pI, TT)/pI).subs(back)))
    dr = (sp.simplify((sp.diff(p0, RR)/p0).subs(back)), sp.simplify((sp.diff(pI, RR)/pI).subs(back)))
    return dt, dr


def smooth_over(expr, w0, wI):
    """expr / (rho_0^w0 rho_I^wI) is a polynomial in (rho_0, x_I), x_I = rho_I^(1/2): smooth on M_sharp"""
    q = sp.cancel(sp.expand(sp.powsimp((expr/(r0**w0*rI**wI)).subs(rI, xI**2), force=True)))
    num, den = sp.fraction(q)
    return den.free_symbols == set() and num.is_polynomial(r0, xI)


def e2(control=False):
    dt, dr = eb_fields()
    ok_f = sp.simplify(dt[0] - r0) == 0 and sp.simplify(dt[1] + r0) == 0 and sp.simplify(dr[0] + r0) == 0 and \
        sp.simplify(dr[1] - r0*(1 - rI)) == 0
    rho = r0*rI
    pref = rI*rho**-2
    deg = 1 if control else 3
    coef = rho**deg                                    # a coefficient homogeneous of degree -deg (at fixed omega)
    terms = {"d_t -> X_0": pref*coef*dt[0], "d_t -> X_I": pref*coef*dt[1],
             "d_r -> X_0": pref*coef*dr[0], "d_r -> X_I": pref*coef*dr[1],
             "r^-1 d_omega -> x_I d_omega": pref*coef*rho*sp.sqrt(rI)**-1,
             "conjugation (3/2) d_r log rho": pref*coef*sp.Rational(3, 2)*(-rho)}
    if not control:
        terms["zeroth order, degree -4"] = pref*rho**4
    res = {k: smooth_over(v, 2, 2) for k, v in terms.items()}
    if control:
        lead = sp.simplify(terms["d_t -> X_0"])
        print("  E2 control (degree -1 coefficient): the coefficients lie in rho_0^2 rho_I^2 C^oo: %s; that of X_0 from "
              "d_t is %s, order 0 at I+ and I_0" % (all(res.values()), lead), flush=True)
        return all(res.values())
    print("  E2: d_t = rho_0 X_0 + (%s) X_I, d_r = (%s) X_0 + (%s) X_I: %s; every coupling coefficient after "
          "rho_I rho^-2 and the conjugation lies in rho_0^2 rho_I^2 C^oo: %s"
          % (sp.simplify(dt[1]), sp.simplify(dr[0]), sp.factor(dr[1]), ok_f, res), flush=True)
    return ok_f and all(res.values())


# --------------------------------------------------------------------------------------------------------------- E3
a_, lam = sp.symbols("a lambda", real=True)


def radial_box0(phi, V):
    """scalar Box_0 of the Kerr-Schild metric on phi(T, R) (l = 0), polar form with sqrt|g| = R^3"""
    gtt, gtr, grr = -1 - V, -V, 1 - V
    pt_, pr_ = sp.diff(phi, TT), sp.diff(phi, RR)
    return -(sp.diff(RR**3*(gtt*pt_ + gtr*pr_), TT) + sp.diff(RR**3*(gtr*pt_ + grr*pr_), RR))/RR**3


def to_rho(e):
    return e.subs({TT: 2 - 1/r0 + 1/(r0*rI), RR: 1/(r0*rI)})


def e3(control=False):
    c = 1 if control else sp.Rational(3, 2)
    p0 = 1/(2 - TT + RR)
    pI = (2 - TT + RR)/RR
    rho = 1/RR
    phi = rho**c*p0**a_*pI**lam
    V = mu/RR**2
    ex = to_rho(rI*rho**-sp.Rational(7, 2)*radial_box0(phi, V)/(p0**a_*pI**lam))
    ex = sp.simplify(sp.powsimp(sp.expand_power_base(ex, force=True), force=True))
    lim = sp.simplify(sp.limit(ex, rI, 0))
    ok_rad = sp.simplify(lim + 2*lam*(a_ - lam)) == 0
    # the full 1-form Box on Z = phi e_nu at one direction and one (a, lam), mu = 1
    ok_full = True
    if not control:
        G = KS(1/R**2)
        A, L_ = sp.Rational(1, 3), sp.Rational(1, 5)
        rhoC = 1/R
        p0C = 1/(2 - t + R)
        pIC = (2 - t + R)/R
        phiC = rhoC**c*p0C**A*pIC**L_
        om = [sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5), sp.Rational(4, 5)]
        for nu in (0, 1):
            Z = [0]*N
            Z[nu] = phiC
            H = G.hodge(Z)
            for cc in range(N):
                e_ = H[cc]*pIC*rhoC**-sp.Rational(7, 2)/(p0C**A*pIC**L_)
                sub = {XS[i]: om[i]/(r0*rI) for i in range(4)}
                sub[RS] = 1/(r0*rI)
                sub[t] = 2 - 1/r0 + 1/(r0*rI)
                e_ = e_.subs(sub)
                e_ = sp.simplify(sp.powsimp(sp.expand_power_base(e_, force=True), force=True))
                lm = sp.simplify(sp.limit(e_, rI, 0))
                want = -2*L_*(A - L_) if cc == nu else 0
                ok_full &= sp.simplify(lm - want) == 0
    msg = "conjugation by rho" if control else "conjugation by rho^(3/2)"
    print("  E3%s (%s): radial limit = %s, equal to -2 lam (a - lam): %s; full 1-form Box, components dt and dx^1 at "
          "a = 1/3, lam = 1/5, mu = 1, omega = (1,2,2,4)/5, diagonal -2 lam (a - lam), off-diagonal 0: %s"
          % (" control" if control else "", msg, lim, ok_rad, ok_full), flush=True)
    return ok_rad and ok_full


# --------------------------------------------------------------------------------------------------------------- E4
tau, rh, alpha = sp.symbols("tau rho alpha", real=True)


def e4(control=False):
    if control:
        # the polar component of a dr at mu = 0 carries 3 a r^-2 (E1's control): rho^-2 times it at rho = 0
        val = sp.limit(sp.Integer(3)*rh**2/rh**2, rh, 0)
        print("  E4 control: rho^-2 (3 a r^-2) at I_0 = %s a (nonzero: the polar component is not scalar at I_0)"
              % val, flush=True)
        return val == 0
    v = sp.Function("v")
    phi = (1/RR)**alpha*v(TT/RR)
    ex = radial_box0(phi, mu/RR**2).subs({TT: tau/rh, RR: 1/rh})
    ex = (ex/rh**(2 + alpha)).doit()
    V0, V1, V2 = sp.symbols("v v' v''")
    ex = ex.subs(sp.Derivative(v(tau), (tau, 2)), V2).subs(sp.Derivative(v(tau), tau), V1).subs(v(tau), V0)
    ex = sp.expand(sp.powsimp(sp.expand_power_base(sp.expand(ex), force=True), force=True))
    lim = sp.simplify(sp.limit(ex, rh, 0))
    c2 = sp.simplify(sp.expand(lim).coeff(V2))
    ok = sp.simplify(c2 - (1 - tau**2)) == 0 and not c2.has(alpha)
    print("  E4: rho^(-2-alpha) Box_0(rho^alpha v(tau)) at rho = 0 = %s; v'' coefficient 1 - tau^2, independent of "
          "alpha: "
          "%s" % (lim, ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- E5
def e5(control=False):
    samples = [(Fr(-1, 3), Fr(1, 2)), (Fr(-1, 10), Fr(-1, 20)), (Fr(-3, 4), Fr(-1, 2)), (Fr(-1, 2), Fr(2))]
    if control:
        samples = [(Fr(0), Fr(1, 2)), (Fr(-1, 2), Fr(-1, 2))]
    ok = True
    for aI, a0 in samples:
        for kap in (Fr(1, 100), Fr(1, 2), Fr(3)):
            M = sp.Matrix([[-4*aI, 0], [0, 4*kap*(a0 - aI)]])          # A-bar = 0: no cross term
            ang = 1 + 2*(a0 - aI) + kap*(1 - 2*aI)
            pd = M[0, 0] > 0 and M.det() > 0 and ang > 0
            ok &= pd
    print("  E5%s: the slot form 4(0 - a_I)|Y|^2 + 4 kappa(a_0 - a_I)|Z|^2 and the angular coefficient are positive at "
          "every sample (a_I, a_0) = %s: %s" % (" control" if control else "", [(str(p), str(q)) for p, q in samples],
                                               ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- E6
def e6(mode=None):
    """the weight chain at exact rational samples; returns (all good, some good, all good with l_0^flat for beta <
    delta_#/2, some good with l_0^flat for beta >= delta_#/2, count)"""
    gams = [Fr(1, 50), Fr(1, 10), Fr(1, 5), Fr(1, 3)]
    es = [Fr(0), Fr(1, 4), Fr(1, 2)]
    allg, someg, allf, somef_hi, cnt = True, False, True, False, 0
    gain = 0 if mode == "nogain" else 1
    for gam, e in itertools.product(gams, es):
        dsh = (1 - e)*gam
        for k in range(1, 6):
            beta = dsh*Fr(k, 6)                                   # beta in (0, delta_#)
            q_h = Fr(3, 2) + 2*gam                                # dot h: I_0-order > 3/2 + 2 gam (the bound used)
            q_F = q_h + gain                                      # F_Y = chi E^Ups G dot h: the factor |x|^-1
            a0 = q_F - Fr(7, 2)                                   # (q_F - 2) - 3/2: solution weight, conjugated
            # I+: F_Y has order l_I^flat + 1 = 5/2 + delta_#/4 by S1 (5/2- if the radiation slot were seen);
            # conjugated (- 5/2): delta_#/4, or 0-; either is above every a_I < 0
            fI = min(dsh/4, Fr(0))
            lo, hi = beta - 1, min(a0, Fr(0), fI)
            good = lo < hi
            if good:
                aI = (lo + hi)/2
                p = Fr(3, 2) + aI
                good = p > Fr(1, 2) + beta and aI < min(a0, 0)
            allg &= good
            someg |= good
            a0f = Fr(3, 2) + dsh/2 + gain - Fr(7, 2)              # statement-level l_0^flat = 3/2 + delta_#/2
            goodf = beta - 1 < min(a0f, Fr(0))
            if beta < dsh/2:
                allf &= goodf
            else:
                somef_hi |= goodf
            cnt += 1
    return allg, someg, allf, somef_hi, cnt


def e6c(control=False):
    if control:
        _, _, _, somef_hi, _ = e6()
        _, some_ng, _, _, _ = e6("nogain")
        print("  E6 control (i) (l_0^flat, beta >= delta_#/2): the interval is non-empty at some sample: %s" % somef_hi,
              flush=True)
        print("  E6 control (ii) (no factor |x|^-1 in c_Ups): the interval is non-empty at some sample: %s" % some_ng,
              flush=True)
        return somef_hi or some_ng
    allg, _, allf, _, cnt = e6()
    print("  E6: at %d samples (gam, e, beta), beta in (0, delta_#): the interval (beta - 1, min(a_0, 0)) is non-empty "
          "and p = 3/2 + a_I > 1/2 + beta: %s; with l_0^flat for beta < delta_#/2: %s" % (cnt, allg, allf), flush=True)
    return allg and allf


CHECKS = [("E1", e1), ("E2", e2), ("E3", e3), ("E4", e4), ("E5", e5), ("E6", e6c)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
