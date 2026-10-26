#!/usr/bin/env python3
"""sbar5.py -- [Hin26] Lemma 8.2's S-bar_{E^Ups, E^C} and (8.7) in five dimensions: the endomorphism by which the
linearized gauge-fixed Einstein operator's d_t* terms differ from the wave operator's on 4+1 Minkowski, its spectrum,
and the decay and threshold it gives (N1STAR-PROOF.md section 10.25; ROUTES-OPEN.md 4.26; D74).  Labels: computed
(exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Lemma 8.1 writes 2 L-bar = -2 d_t* rho (rho d_rho - 1 - S-bar_{E^Ups, E^C}) + L-bar(0)
((8.3b)); Lemma 8.2 computes S-bar as "1/2 rho^-1 times the sum of d_t*-coefficients of the second and third terms" of
2 L-bar = box + 2 E^C delta G + 2 (delta* + E^C) E^Ups G, finds it lower triangular in the splitting (5.27) with
diagonal 2 (1 - v) gam_C, (1 - v) gam_C, (1 - e_C)(1 - v) gam_C, (1 - e_Ups) gam_Ups, gam_Ups, 0, 2 gam_Ups ((8.8)),
and so "min spec S-bar = 0. (8.7)".  His proof of Proposition 8.6 uses (8.7) to improve the decay at sctf to 1 - eps
and then the threshold r + alpha_+ < -1/2 at the outgoing radial set (p. 152); Corollary 8.7 asks beta_sctf < 1 + min
Re S-bar = 1 ((8.18a)).  Here, from the definitions (lin5.py's E^Ups and E^C, with time dependence): fields h(t*, x) on
(n+1)-Minkowski, t* = t - r, d_t = d_t*, d_i = d/dx_i - (x_i/r) d_t*, r = |x|.

  S1 (computed, exact) The structure: the wave operator on symmetric 2-tensors, componentwise in the Cartesian frame,
     has no d_t*^2 term, mixed terms 2 (x_i/r) d_t* d_i and the d_t* term (n - 1)/r, that is -2 d_t* rho (rho d_rho -
     (n - 1)/2) plus a stationary operator -- in five dimensions rho d_rho - 3/2, his rho d_rho - 1; and 2 L - box is
     first order with d_t* coefficient 2 rho S-bar, S-bar constant: free of r at (R, 0, 0, 0), and with the same
     characteristic polynomial at (1, 2, 2, 4).  Four-dimensional control: the same at n = 3.  Control: c_Ups = dt in
     place of r^-1 dt, where S-bar carries r.
  S2 (computed, exact) The spectrum: spec S-bar = spec S-bar^Ups u spec S-bar^C u {0 ((n - 1) n/2 - 1 times)}, the two
     1-form endomorphisms computed by the same construction from 2 E^Ups G delta* and 2 delta G E^C and equal to
     thresh5.py U2's gam_U {1 - e_U, 2, 1 (n - 1 times)} and cpmodes5.py K1's gam_C {2 (1 - v), (1 - e_C)(1 - v), 1 - v
     (n - 1 times)} (typed from there); every eigenvalue is >= 0 for 0 < v, e_U, e_C < 1 and gam_U, gam_C > 0, and 0 is
     one, so min spec S-bar = 0: his (8.7) in five dimensions, with the zero five times (twice in four); at the trace
     weight 1 in five dimensions the two eigenvalues (1 - e) gam become (3/2)(1 - e) gam (m (n - 1)/2 times) and the
     rest stay, so the minimum is 0 there too.  Four-dimensional control: his (8.8)'s seven values with multiplicities
     1, 2, 1, 1, 2, 2, 1 in his order, the ranks of the summands of his splitting (5.27).  At gam_C = 0, the unmodified
     symmetric gradient: spec S-bar^Ups u {0 ((n + 1) + (n - 1) n/2 - 1 times)}, the minimum 0 again.  Control: the
     incoming t* = t + r, where the constraint part becomes gam_C {2 (1 + v), (1 - e_C)(1 + v), 1 + v (n - 1 times)} --
     cpmodes5.py K2's spectrum at R_in -- and the union fails.
  S3 (computed, exact; what follows "so" is deduced) The consequences: the transport equation (rho d_rho - (n - 1)/2 -
     s) u = 0 has u = rho^((n - 1)/2 + s), so the improvement at sctf is to (n - 1)/2 + min spec S-bar - eps = 3/2 -
     eps, his 1 - eps; rho^(3/2 - eps) lies in rho^l L^2(r^(n-1) dr) near infinity iff l < -1/2 - eps, the
     dimension-free -1/2 of the outgoing threshold r + alpha_+ < -1/2 (p. 152); and with the unweighted b-density
     rho^(3/2 + s) lies in rho^beta L^2(drho/rho) iff beta < 3/2 + s, so (8.18a) reads beta_sctf < 3/2 + min Re S-bar
     = 3/2 in five dimensions, his 1.  Four-dimensional control: his 1 - eps, -1/2 and 1.  Control: his 1 - eps
     claimed in five dimensions.
  S4 (computed, exact) S-bar is semisimple: at two parameter points with gam_Ups small the product of S-bar - s over
     its distinct eigenvalues s vanishes (seven of them in five dimensions), so S-bar is diagonalisable with constant
     eigenvalues and its spectral projections are smooth; the proof is III.G' Lemma 1.1 (proof5/PART-III-G2-IOTA.md).
     Four-dimensional control: the same at n = 3.  Control: gam_Ups = gam_C (1 - v), where the two 1-form spectra meet
     and S-bar has a Jordan block: the product alone is tested there, and does not vanish (D240).

Deduced, not computed here: (8.4) on five-dimensional Tangherlini -- S_{E^Ups, E^C} - S-bar in rho C^oo -- as 10.18
deduces (6.7), Tangherlini differing from Minkowski by O(mu rho^2) and c, c_Ups equal to Minkowski's for large r; and
with S1-S3 the step of [Hin26] Proposition 8.6's kernel half that 10.24(c) left OPEN, on the reading of [Hin26c]
Theorem 9.38 at n = 4.

READ.  [Hin26] pp. 144-146 (section 8: its opening on p. 144, fixing c_Ups = r^-1 dt and gam_Ups << 1; (8.1), Lemma 8.1
with (8.2)-(8.5), Lemma 8.2 with (8.6)-(8.8) and its proof), 152 (the proof of Proposition 8.6, its parenthetical on
(8.7) and the threshold), 153 (Corollary 8.7, (8.18a)); alphaXiv, 2026-10-23.

sympy.  python3 sbar5.py [--selftest | --mutants]   (--verbose lists every sub-check; about a minute)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

D = sp.diff
v, eC, gC, eU, gU = sp.symbols("v e_C gam_C e_U gam_U", positive=True)
lam, eps = sp.symbols("lam epsilon", positive=True)
HALF = sp.Rational(1, 2)


class Mink:
    """(n+1)-Minkowski in (t*, x), t* = t - sgn r, r = |x| explicit"""

    def __init__(self, n, sgn=1):
        self.n, self.N, self.sgn = n, n + 1, sgn
        self.T = sp.Symbol("T")
        self.x = sp.symbols("x1:%d" % (n + 1), real=True)
        self.r = sp.sqrt(sum(q**2 for q in self.x))
        self.eta = sp.diag(-1, *([1] * n))

    def d(self, f, a):
        if a == 0:
            return D(f, self.T)
        return D(f, self.x[a - 1]) - self.sgn * self.x[a - 1] / self.r * D(f, self.T)

    def tr(self, k):
        return sum(self.eta[a, a] * k[a, a] for a in range(self.N))

    def G(self, k):
        return k - self.eta * self.tr(k) / 2

    def delta(self, k):
        return [-sum(self.eta[c, c] * self.d(k[a, c], c) for c in range(self.N)) for a in range(self.N)]

    def dstar(self, w):
        return sp.Matrix(self.N, self.N, lambda a, b: (self.d(w[b], a) + self.d(w[a], b)) / 2)

    def EU(self, k, m, cfar=True):
        """E^Ups k = -gam_U (2 iota_{c_U#} k - m (1 - e_U) c_U tr k), c_U = r^-1 dt (dt for cfar False)"""
        cU = [1 / self.r if cfar else 1] + [0] * self.n
        t_ = self.tr(k)
        return [-gU * (2 * sum(self.eta[j, j] * cU[j] * k[j, a] for j in range(self.N)) - m * (1 - eU) * cU[a] * t_)
                for a in range(self.N)]

    def EC(self, w, m):
        """E^C w = gam_C (2 c (x)_s w - m (1 - e_C) g <c, w>), c = r^-1 (dt - v dr)"""
        c = [1 / self.r] + [-v * q / self.r**2 for q in self.x]
        cw = sum(self.eta[j, j] * c[j] * w[j] for j in range(self.N))
        return sp.Matrix(self.N, self.N,
                         lambda a, b: gC * (c[a] * w[b] + c[b] * w[a] - m * (1 - eC) * self.eta[a, b] * cw))

    def tensor(self):
        F = {(a, b): sp.Function("h%d%d" % (a, b))(self.T, *self.x) for a in range(self.N) for b in range(a, self.N)}
        return sp.Matrix(self.N, self.N, lambda a, b: F[(min(a, b), max(a, b))]), F

    def oneform(self):
        F = {(a,): sp.Function("w%d" % a)(self.T, *self.x) for a in range(self.N)}
        return [F[(a,)] for a in range(self.N)], F


def coeffs(C, outs, F, deriv, pt):
    """the matrix of the coefficients of deriv(F_k) in the components of outs, at the point pt"""
    keys = sorted(F)
    sub = dict(zip(C.x, pt))
    rows = []
    for o in outs:
        e_ = sp.expand(o)
        rows.append([sp.simplify(e_.coeff(deriv(F[k])).subs(sub)) for k in keys])
    return sp.Matrix(rows)


def flat(C, M):
    return [M[a, b] for a in range(C.N) for b in range(a, C.N)] if isinstance(M, sp.MatrixBase) else list(M)


def sbar_L(n, m, pt=None, sgn=1, cfar=True):
    """S-bar of L: 2 rho S-bar = the d_t* coefficient of 2 L - box = 2 E^C delta G + 2 (delta* + E^C) E^Ups G"""
    C = Mink(n, sgn)
    h, F = C.tensor()
    Gh = C.G(h)
    eu = C.EU(Gh, m, cfar)
    out = 2 * C.EC(C.delta(Gh), m) + 2 * (C.dstar(eu) + C.EC(eu, m))
    R = sp.Symbol("R", positive=True)
    pt = pt or [R] + [0] * (n - 1)
    rho = 1 / sp.sqrt(sum(q**2 for q in pt))
    M = coeffs(C, flat(C, out), F, lambda f: D(f, C.T), pt)
    second = any(sp.expand(o).has(sp.Derivative(F[k], C.T, 2)) or any(sp.expand(o).has(sp.Derivative(F[k], C.T, q))
                                                                      for q in C.x) for o in flat(C, out) for k in F)
    return (M / (2 * rho)).applyfunc(sp.simplify), second


def sbar_1form(n, m, which):
    """S-bar of box^Ups = box + 2 E^Ups G delta* and of box^C = box + 2 delta G E^C on 1-forms, the same way"""
    C = Mink(n)
    w, F = C.oneform()
    if which == "U":
        out = [2 * q for q in C.EU(C.G(C.dstar(w)), m)]
    else:
        out = [2 * q for q in C.delta(C.G(C.EC(w, m)))]
    R = sp.Symbol("R", positive=True)
    pt = [R] + [0] * (n - 1)
    return (coeffs(C, out, F, lambda f: D(f, C.T), pt) * R / 2).applyfunc(sp.simplify)


def spec(M):
    return {sp.factor(k): mm for k, mm in M.eigenvals().items()}


def nonneg(expr):
    p_, q1, q2 = sp.symbols("p q1 q2", positive=True)
    s_ = sp.factor(sp.together(expr.subs({v: 1 / (1 + p_), eU: 1 / (1 + q1), eC: 1 / (1 + q2)})))
    return s_ == 0 or s_.is_nonnegative


# ------------------------------------------------------------------------------------------------- S1
def s1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        C = Mink(n)
        u = sp.Function("u")(C.T, *C.x)
        box = sp.expand(-sum(C.eta[a, a] * C.d(C.d(u, a), a) for a in range(C.N)))
        R = sp.Symbol("R", positive=True)
        pt = {C.x[0]: R, **{q: 0 for q in C.x[1:]}}
        c_T = sp.simplify(box.coeff(D(u, C.T)).subs(pt))
        c_TT = sp.simplify(box.coeff(D(u, C.T, 2)).subs(pt))
        c_Tr = sp.simplify(box.coeff(D(u, C.T, C.x[0])).subs(pt))
        okbox = c_TT == 0 and sp.simplify(c_Tr - 2) == 0 and sp.simplify(c_T - (n - 1) / R) == 0
        S, second = sbar_L(n, sp.Rational(2, n - 1), cfar=control != 1)
        S2, _ = sbar_L(n, sp.Rational(2, n - 1), pt=[1, 2, 2, 4] if n == 4 else [1, 2, 2], cfar=control != 1)
        same = sp.expand(S.charpoly(lam).as_expr() - S2.charpoly(lam).as_expr()) == 0
        const = not (S.free_symbols & {sp.Symbol("R", positive=True)})
        chk(f"n + 1 = {n + 1}: box has no d_t*^2 term, d_t* d_r coefficient 2, d_t* coefficient {n - 1}/r: -2 d_t* rho "
            f"(rho d_rho - {sp.Rational(n - 1, 2)}); 2 L - box first order, its d_t* coefficient 2 rho S-bar with "
            f"S-bar ({S.shape[0]} x {S.shape[0]}) free of r and of the point", okbox and not second and same and const)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S2
def s2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        m = sp.Rational(2, n - 1)
        S, _ = sbar_L(n, m, sgn=-1 if control == 1 else 1)
        sp_L = spec(S)
        sU, sC = spec(sbar_1form(n, m, "U")), spec(sbar_1form(n, m, "C"))
        wantU = {sp.factor(gU * (1 - eU)): 1, 2 * gU: 1, gU: n - 1}                       # thresh5.py U2
        wantC = {sp.factor(2 * gC * (1 - v)): 1, sp.factor(gC * (1 - eC) * (1 - v)): 1, sp.factor(gC * (1 - v)): n - 1}
        union = dict(wantU)
        for k, mm in wantC.items():
            union[k] = union.get(k, 0) + mm
        union[sp.Integer(0)] = union.get(sp.Integer(0), 0) + (n - 1) * n // 2 - 1
        ok = sU == wantU and sC == wantC and sp_L == union
        ok &= sum(sp_L.values()) == (n + 1) * (n + 2) // 2
        allpos = all(nonneg(k) for k in sp_L)
        zero = 0 in sp_L
        wfree = True
        if control == 0:                                                    # the trace weight 1: (1 - e) gam scaled
            s1w = spec(sbar_L(n, sp.Integer(1))[0])
            f_ = sp.Rational(n - 1, 2)
            scale = {sp.factor(gU * (1 - eU)): sp.factor(f_ * gU * (1 - eU)),
                     sp.factor(gC * (1 - eC) * (1 - v)): sp.factor(f_ * gC * (1 - eC) * (1 - v))}
            wfree = s1w == {scale.get(k, k): mm for k, mm in sp_L.items()} and 0 in s1w
        if n == 3:                                       # his (8.8): the seven values in his order, with the ranks
            his = [(2 * (1 - v) * gC, 1), ((1 - v) * gC, 2), ((1 - eC) * (1 - v) * gC, 1),    # of his (5.27)'s summands
                   ((1 - eU) * gU, 1), (gU, 2), (sp.Integer(0), 2), (2 * gU, 1)]
            ok &= sp_L == {sp.factor(k): mm for k, mm in his}
        if control == 0:                                         # gam_C = 0: the unmodified symmetric gradient
            want0 = dict(wantU)
            want0[sp.Integer(0)] = (n + 1) + (n - 1) * n // 2 - 1
            ok &= spec(S.subs(gC, 0)) == want0
        chk(f"n + 1 = {n + 1}: spec S-bar = {sorted(sp_L.items(), key=str)}: S-bar^Ups's u S-bar^C's u "
            f"{{0 x {(n - 1) * n // 2 - 1}}}; every eigenvalue >= 0 and 0 one of them, min spec S-bar = 0 ((8.7)); "
            f"at the trace weight 1 the (1 - e) gam scaled by {sp.Rational(n - 1, 2)}, the minimum 0; at gam_C = 0 the "
            f"minimum 0",
            ok and allpos and zero and wfree)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S3
def s3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    s_, a_, l_, be = sp.symbols("s a l beta", real=True)
    rho = sp.Symbol("rho", positive=True)
    for n in ((4,) if control else (4, 3)):
        u = rho**((n - 1) * HALF + s_)
        transport = sp.simplify(rho * D(u, rho) - ((n - 1) * HALF + s_) * u) == 0
        improve = (n - 1) * HALF + 0 - eps                                       # min spec S-bar = 0 (S2)
        if control == 1:
            improve = 1 - eps                                                     # control: his 1 - eps claimed
        # rho^a in rho^l L^2(r^(n-1) dr) near infinity: rho^(2(a - l)) rho^-(n+1) drho integrable at 0
        lmax = sp.solve(sp.Eq(2 * (improve - a_) - (n + 1), -1), a_)[0]
        thr = sp.simplify(lmax - (-HALF - eps)) == 0
        # unweighted b-density: rho^(2(a - beta)) drho/rho integrable iff a > beta
        bsc = sp.solve(sp.Eq(2 * ((n - 1) * HALF + s_ - be), 0), be)[0]
        want_b = {4: sp.Rational(3, 2), 3: 1}[n]
        ok = transport and thr and bsc.subs(s_, 0) == want_b
        chk(f"n + 1 = {n + 1}: u = rho^((n - 1)/2 + s) solves the transport equation; the improvement {improve}; "
            f"rho^({improve}) in rho^l L^2(r^{n - 1} dr) iff l < {lmax}; (8.18a) beta_sctf < {bsc}, at min spec 0 "
            f"{bsc.subs(s_, 0)}", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- S4
def s4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    R_ = sp.Rational
    pts = [{v: R_(1, 4), eC: R_(1, 2), gC: 2, eU: R_(1, 3), gU: R_(1, 50)},
           {v: R_(1, 3), eC: R_(1, 5), gC: 7, eU: R_(3, 4), gU: R_(1, 100)}]
    if control == 1:
        pts = [{v: R_(1, 4), eC: R_(1, 2), gC: 2, eU: R_(1, 3), gU: R_(3, 2)}]       # gam_U = gam_C (1 - v)
    for n in ((4,) if control else (4, 3)):
        S, _ = sbar_L(n, sp.Rational(2, n - 1))
        for pt in pts:
            M = S.subs(pt)
            ev = list(M.eigenvals())
            P_ = sp.eye(M.shape[0])
            for e in ev:
                P_ = P_ * (M - e * sp.eye(M.shape[0]))
            ok = P_.applyfunc(sp.simplify) == sp.zeros(*M.shape)
            if not control:
                ok = ok and len(ev) == 7
            chk(f"n + 1 = {n + 1} at {sorted((str(k), str(q)) for k, q in pt.items())}: {len(ev)} distinct eigenvalues, "
                f"the product of S-bar - s over them {'vanishes' if ok else 'does not vanish'}", ok)
    return chk.ok


CHECKS = [("S1 2 L - box on 4+1 Minkowski: first order, d_t* coefficient 2 rho S-bar, S-bar constant; rho d_rho - 3/2",
           s1, 1),
          ("S2 spec S-bar = S-bar^Ups's u S-bar^C's u {0 x 5}, min spec S-bar = 0: (8.7) in five dimensions", s2, 1),
          ("S3 the improvement to 3/2 - eps, the threshold -1/2, (8.18a) beta_sctf < 3/2 in five dimensions", s3, 1),
          ("S4 S-bar semisimple with constant eigenvalues for gam_Ups small; Jordan block where the spectra meet", s4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"sbar5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"sbar5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
