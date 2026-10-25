#!/usr/bin/env python3
"""hthresh5.py -- box^C's threshold quantity at the conormal bundle of the horizon of five-dimensional Tangherlini,
computed from its definition at the record's point (N1STAR-PROOF.md 10.79; the readings census's root RH; D171).
Labels: computed (exact, sympy; T6 numerical, mpmath), READ.

[Hin26c] (Hintz, arXiv:2606.28008) asks of a stationary operator P_0 on a bundle, at the radial set over the event
horizon, s_0 > 1/2 + vartheta_H+ (Proposition 7.4, p. 116; Proposition 9.9, p. 165; section 9.4, p. 193), with

    vartheta_H+ := sup_{N*H+ \\ o} spec [ varrho^2/(2(r_+ - m)) rho_oo sigma_1((P_0 - P_0^*)/(2i)) ],  rho_oo := xi_0^-1,

"with respect to a positive definite fiber inner product" ((5.17), Definition 5.11(4), p. 104); R+_H+ is the component
xi_0 > 0 of N*H+ (Definition 4.8, p. 84), in the future characteristic set, where g^-1(zeta, .) is future causal (p. 81),
and rho_oo^-1 H_G rho_oo = 2(r_+ - m) there for G = varrho^2 g^-1 ((4.28)), so the factor is 1/beta_0 of (9.24) for G =
g^-1.  The record (10.21 (d)) needs 1/2 + vartheta_H+ < -C_0 = -100 for box^C = 2 delta G (delta* + C_h), C_h omega =
h^-1 (2 c (x)_s omega - (2/3)(1 - e) g iota_{c#} omega), at (v, e, h) = (1/2, 1/102400, 10^-6), with cform5.py's c,
which near the horizon is (2 r_0)^-1 (dt + (v/2) dr), r_0 = 100, on g = -f dt^2 + 2(1 - f) dt dr + (2 - f) dr^2 + r^2
dOmega_3^2, f = 1 - mu/r^2, r_h = mu^(1/2); delta* omega = (1/2)(omega_{a;b} + omega_{b;a}), G = Id - (1/2) g tr_g,
(delta k)_a = -g^{bc} k_{ab;c}.  The fibre inner product is [Hin26a] Lemma 3.3's B = g^-1 - (1 + e) G(c)^-1 c# (x) c#
(semiclass5.py W1), positive definite for e > 0 and conditioned like 1/e.  (varrho^2 = r^2 + a^2 cos^2 theta,
Kerr's area-radius factor, r^2 at a = 0; e is e_C, not Euler's number.)

  T1 (computed, exact) The normalisation.  At zeta = xi dr over r = r_h, H_G's base component in the spatial slice
     vanishes (g^rr = f = 0) and rho_oo^-1 H_G rho_oo = f'(r_h) = 2/r_h for rho_oo = xi^-1: the factor is r_h/2 (at
     n = 3, a = 0 his r^2/(2(r_+ - m)) = r_+ = 1/f'(r_+), the same formula).  dr# = d_t at r_h, future directed, and
     <c, dr> = c_t(r_h) > 0 for cform5.py's past timelike c: xi > 0 is R+_H+ and dr is future null there.  Control:
     the Schwarzschild check with r_+ = 3m.
  T2 (computed, exact) The adjoint.  P_0 = 2 delta G delta* and L = 2 delta G C_1 (C_1 = h C_h) built from their
     definitions with the Christoffel symbols of g, their coefficient matrices read off, and the formal adjoint taken
     for |dg| = r^3 cos th sin th and a fibre form M on the components: P_0's principal symbol is G Id, and for M =
     g^-1 its imaginary part has no first-order term anywhere -- P_0 is g-symmetric, so the adjoint is taken right.
     Control: the density r^2 cos th sin th, for which the first-order term does not vanish.
  T3 (computed, exact) The box part in B.  At r_h, rho_oo sigma_1((P_0 - P_0^*)/(2i)) in B is the B-symmetric part
     of 2 Gamma_t, (Gamma_t)_a^c = Gamma^c_{t a}, the connection along (dr)# = d_t; both routes agree, and its spectrum
     is {+-(e^(1/2) + e^(-1/2))/r_h, 0, 0, 0}, free of v and of c's factor: vartheta_0 := (e^(1/2) + e^(-1/2))/2 =
     102401/640 at e = 1/102400 (the Gamma_t route at every r_h).  B's conditioning is the source: in g^-1, an
     indefinite form, the part is 0.  Control: the adjoint in g^-1 does not give this spectrum.
  T4 (computed, exact) The damping.  rho_oo sigma_1 of h^-1 L's imaginary part at r_h is -h^-1 l(dr), l(zeta) omega
     = 2(<c, zeta> omega + <zeta, omega> c - e <omega, c> zeta), B-self-adjoint with spectrum 2a (three times), 4a and
     2(1 - e) a, a = <c, dr> = c_t(r_h) = 1/200: B-negative definite, his Remark 5.7's mechanism.  Control: the trace
     weight 1 (four dimensions') in place of 2/3, which breaks the spectrum.
  T5 (computed, exact) The threshold.  vartheta_H+ = (r_h/2) lambda_max of T3's part minus h^-1 l(dr), B-symmetric:
     the angular eigenvalue -a r_h/h and the larger root of the (t, r) block's quadratic.  At h = 10^-6 it is
     -4995.834..., so 1/2 + vartheta_H+ < -C_0 = -100 with room (certified by the quadratic's signs), below 10.21
     (d)'s bound vartheta_0 - h^-1 (1 - e) r_h a = -4839.95...; lambda_max decreases in h^-1 (l(dr) B-positive), so
     the threshold holds for every h in (0, h_2), h_2 = 2.61974726...e-5 the positive root of 31744512005000 h^2 +
     3077109850 h - 102399 (the (t, r) block binds; the angular eigenvalue alone allows 1/20100), and 10^-6 < h_2.
     Control: h = 10^-3, where it fails.
  T6 (computed, numerical, mpmath at 30 digits; D175) Other fibre inner products.  (5.17) asks for one positive
     definite fibre inner product, and B is one.  With e' for B's e (the operator's e kept), B is positive definite at
     e' = 10^-5, 1/10 and 3, and (r_h/2) lambda_max of the B-symmetric part of 2 Gamma_t - h^-1 l(dr) -- l(dr) is
     B-self-adjoint only at e' = e -- gives 1/2 + vartheta_H+ = -4995.44..., -4877.97... and -2500.47... at h =
     10^-6: below -C_0 in each.  Control: h = 10^-3.
  T7 (computed, numerical, mpmath at 30 digits; D177, D179, D182) The dependence on the inner product: at e' = 10, B'
     still positive definite, 1/2 + vartheta_H+ = +790.428... > -C_0.  Control: e' = 3 claimed above -C_0.
  T8 (computed, numerical, mpmath at 30 digits; D179, D182) Bisection on [3, 10] puts the crossing of -C_0 at e' =
     7.7638634... (the sixty-ninth verifier's finding).  Control: the crossing claimed in (7, 7.5).
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

t, r, th, p1, p2 = sp.symbols("t r th p1 p2")
XS = [t, r, th, p1, p2]
N = 5
E = sp.Rational(1, 102400)
V = sp.Rational(1, 2)
K = sp.Rational(1, 200)                                # (2 r_0)^-1, r_0 = 100
H = sp.Rational(1, 10**6)
C0 = 100
e_, v_, k_, mu_, h_, lam = sp.symbols("e v k mu h lambda", positive=True)


def metric(mu):
    f = 1 - mu / r**2
    g = sp.zeros(N, N)
    g[0, 0], g[0, 1], g[1, 0], g[1, 1] = -f, 1 - f, 1 - f, 2 - f
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2 * sp.cos(th)**2, r**2 * sp.sin(th)**2
    return g, f


def christoffel(g, gi):
    return [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], XS[c]) + sp.diff(g[d, c], XS[b]) - sp.diff(g[b, c], XS[d]))
                              for d in range(N)) / 2) for c in range(N)] for b in range(N)] for a in range(N)]


def fibre_B(gi, c, e):
    cs = gi * c
    Gc = (c.T * gi * c)[0]
    return (gi - (1 + e) / Gc * cs * cs.T), cs, Gc


def ell(gi, c, z, e):
    """l(zeta) on components: (l w)_a = 2(<c, zeta> w_a + c_a <zeta, w> - e zeta_a <c, w>)."""
    zs, cs = gi * z, gi * c
    cz = (c.T * zs)[0]
    return sp.Matrix(N, N, lambda a, d: 2 * (cz * (1 if a == d else 0) + c[a] * zs[d] - e * z[a] * cs[d]))


def adj(Xm, M):
    return M.inv() * Xm.T * M


_OPS = {}


def operators(weight=sp.Rational(2, 3)):
    """Coefficient matrices of P_0 = 2 delta G delta* and L = 2 delta G C_1 on 5D Tangherlini (mu = 1), from the
    definitions; c = k (dt + (v/2) dr) symbolic."""
    if weight in _OPS:
        return _OPS[weight]
    g, f = metric(1)
    gi = g.inv().applyfunc(sp.simplify)
    Gam = christoffel(g, gi)
    W = [sp.Function("W%d" % q)(*XS) for q in range(N)]

    def nab1(w):
        return [[sp.diff(w[a], XS[b]) - sum(Gam[d][b][a] * w[d] for d in range(N)) for a in range(N)] for b in range(N)]

    def delta(kt):
        return [-sum(gi[b, c] * (sp.diff(kt[a][b], XS[c]) - sum(Gam[d][c][a] * kt[d][b] + Gam[d][c][b] * kt[a][d]
                                                                for d in range(N)))
                     for b in range(N) for c in range(N)) for a in range(N)]

    def Gop(kt):
        tr = sum(gi[a, b] * kt[a][b] for a in range(N) for b in range(N))
        return [[kt[a][b] - g[a, b] * tr / 2 for b in range(N)] for a in range(N)]

    def dstar(w):
        nw = nab1(w)
        return [[(nw[a][b] + nw[b][a]) / 2 for b in range(N)] for a in range(N)]

    c = sp.Matrix([k_, k_ * v_ / 2, 0, 0, 0])
    cs = gi * c

    def C1(w):
        cw = sum(cs[a] * w[a] for a in range(N))
        return [[c[a] * w[b] + c[b] * w[a] - weight * (1 - e_) * g[a, b] * cw for b in range(N)] for a in range(N)]

    P0 = [sp.expand(2 * x) for x in delta(Gop(dstar(W)))]
    L = [sp.expand(2 * x) for x in delta(Gop(C1(W)))]

    def coeffs(ex, order):
        out = {}
        for a in range(N):
            for q in range(N):
                for m in range(N):
                    if order == 1:
                        out.setdefault(m, sp.zeros(N, N))[a, q] = ex[a].coeff(sp.diff(W[q], XS[m]))
                        continue
                    for n_ in range(m, N):
                        co = ex[a].coeff(sp.diff(W[q], XS[m], XS[n_])) / (1 if m == n_ else 2)
                        out.setdefault((m, n_), sp.zeros(N, N))[a, q] = co
                        out.setdefault((n_, m), sp.zeros(N, N))[a, q] = co
        return out

    _OPS[weight] = dict(g=g, gi=gi, f=f, Gam=Gam, c=c, P0=(coeffs(P0, 2), coeffs(P0, 1)), L=(None, coeffs(L, 1)))
    return _OPS[weight]


def imag_first(op, M, dens, nu_dir=1):
    """The coefficient Q^nu of d_nu in P - P^* (P^* for int v^T M u dens): sigma_1((P - P^*)/2i)(zeta) =
    (1/2) zeta_nu Q^nu.  P = a^{mn} d_m d_n + b^m d_m + ..."""
    a2, b1 = op
    Mi = M.inv()
    S = sp.zeros(N, N)
    if a2 is not None:
        for nu in range(N):
            S += 2 * sp.diff(dens * a2[(nu, nu_dir)].T * M, XS[nu])
    S -= dens * b1[nu_dir].T * M
    return b1[nu_dir] - Mi * S / dens


def evs(Mx, at=None):
    at = at or {}
    return sorted(sp.Matrix(Mx).eigenvals(multiple=True), key=lambda z: sp.N(sp.sympify(z).subs(at)))


# ------------------------------------------------------------------ T1
def t1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    xi = sp.Symbol("xi", positive=True)
    for dim, fn, rh, want in ((5, 1 - mu_ / r**2, sp.sqrt(mu_), sp.sqrt(mu_) / 2),
                              (4, 1 - 2 * sp.Symbol("m", positive=True) / r, None, None)):
        m = sp.Symbol("m", positive=True)
        if dim == 4:
            rh = (3 if control else 2) * m
            want = rh**2 / (2 * (rh - m))                      # his rho^2 / (2 (r_+ - m)) at a = 0
        Gsym = fn * xi**2                                     # G at sigma = 0, eta = 0: g^rr xi^2
        base = sp.diff(Gsym, xi).subs(r, rh)
        HGrho = (-sp.diff(Gsym, r) * sp.diff(1 / xi, xi)).subs(r, rh)       # H_G rho_oo = -d_r G d_xi(xi^-1)
        beta0 = sp.simplify(HGrho)                     # rho_oo^-1 (rho_oo H_G) rho_oo = H_G rho_oo
        chk(f"n = {dim - 1}: H_G's base component vanishes at r_h", sp.simplify(base) == 0)
        chk(f"n = {dim - 1}: 1/beta_0 = {sp.simplify(1 / beta0)}, his factor {sp.simplify(want)}",
            sp.simplify(1 / beta0 - want) == 0 and sp.simplify(beta0) != 0)
    g, f = metric(mu_)
    gi = g.inv().applyfunc(sp.simplify)
    rh = sp.sqrt(mu_)
    dr_sharp = (gi * sp.Matrix([0, 1, 0, 0, 0])).subs(r, rh).applyfunc(sp.simplify)
    chk("(dr)# = d_t at r_h, future directed", list(dr_sharp) == [1, 0, 0, 0, 0])
    c = K * sp.Matrix([1, V / 2, 0, 0, 0])
    cdr = sp.simplify((c.T * gi * sp.Matrix([0, 1, 0, 0, 0]))[0].subs(r, rh))
    Gc = sp.simplify((c.T * gi * c)[0].subs(r, rh))
    chk(f"a = <c, dr> = c_t(r_h) = {cdr} > 0, G(c) = {Gc} < 0", cdr == K and Gc < 0)
    return chk.ok


# ------------------------------------------------------------------ T2
def t2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ops = operators()
    gi = ops["gi"]
    a2 = ops["P0"][0]
    chk("P_0's principal part is -g^{mn} d_m d_n Id",
        all(sp.simplify(a2[(m, n_)] + gi[m, n_] * sp.eye(N)) == sp.zeros(N, N) for m in range(N) for n_ in range(N)))
    dens = (r**2 if control else r**3) * sp.cos(th) * sp.sin(th)
    ok = all((imag_first(ops["P0"], gi, dens, nu)).applyfunc(sp.simplify) == sp.zeros(N, N) for nu in range(N))
    chk("in g^-1, P_0 - P_0^* has no first-order term, every direction, every r", ok)
    return chk.ok


# ------------------------------------------------------------------ T3
def t3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ops = operators()
    gi = ops["gi"]
    dens = r**3 * sp.cos(th) * sp.sin(th)
    c = ops["c"]
    B = fibre_B(gi, c, e_)[0]
    M = gi if control else B
    Q0 = (imag_first(ops["P0"], M, dens) / 2).subs(r, 1).applyfunc(sp.simplify)
    Gt = sp.Matrix(N, N, lambda a, q: ops["Gam"][q][0][a]).subs(r, 1)
    B1 = B.subs(r, 1)
    sym = (Gt + adj(Gt, B1)).applyfunc(sp.simplify)
    chk("definition route = Gamma_t route: 2 Gamma_t's B-symmetric part", (Q0 - sym).applyfunc(sp.simplify) ==
        sp.zeros(N, N))
    want = [-(1 + e_) / sp.sqrt(e_), 0, 0, 0, (1 + e_) / sp.sqrt(e_)]
    got = evs(Q0, {e_: E, v_: V, k_: K})
    chk(f"spectrum {{+-(e^(1/2) + e^(-1/2)), 0, 0, 0}} free of v and k: {got}",
        len(got) == 5 and all(sp.simplify(x - y) == 0 for x, y in zip(got, want)))
    # the Gamma_t route at every r_h
    g, f = metric(mu_)
    gim = g.inv().applyfunc(sp.simplify)
    Gam = christoffel(g, gim)
    rh = sp.sqrt(mu_)
    Gtm = sp.Matrix(N, N, lambda a, q: Gam[q][0][a]).subs(r, rh).applyfunc(sp.simplify)
    Bm = fibre_B(gim, K * sp.Matrix([1, V / 2, 0, 0, 0]), E)[0].subs(r, rh).applyfunc(sp.simplify)
    symm = (Gtm + adj(Gtm, gim.subs(r, rh) if control else Bm)).applyfunc(sp.simplify)
    top = evs(symm, {mu_: 1})[-1]
    th0 = sp.simplify(rh / 2 * top)
    chk(f"vartheta_0 = (r_h/2) lambda_max = {th0} = (e^(1/2) + e^(-1/2))/2 at every r_h",
        sp.simplify(th0 - (1 + E) / (2 * sp.sqrt(E))) == 0 and th0 == sp.Rational(102401, 640))
    return chk.ok


# ------------------------------------------------------------------ T4
def t4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ops = operators(1 if control else sp.Rational(2, 3))
    gi = ops["gi"]
    dens = r**3 * sp.cos(th) * sp.sin(th)
    c = ops["c"]
    B = fibre_B(gi, c, e_)[0]
    QL = (imag_first(ops["L"], B, dens) / 2).subs(r, 1).applyfunc(sp.simplify)
    l_dr = ell(gi, c, sp.Matrix([0, 1, 0, 0, 0]), e_).subs(r, 1).applyfunc(sp.simplify)
    chk("rho_oo sigma_1 of L's imaginary part at r_h is -l(dr)", (QL + l_dr).applyfunc(sp.simplify) == sp.zeros(N, N))
    chk("l(dr) is B-self-adjoint", (adj(l_dr, B.subs(r, 1)) - l_dr).applyfunc(sp.simplify) == sp.zeros(N, N))
    a = k_
    want = sorted([2 * a, 2 * a, 2 * a, 4 * a, 2 * (1 - e_) * a], key=lambda z: sp.N(z.subs({k_: 1, e_: E})))
    got = evs(l_dr, {k_: 1, e_: E, v_: V})
    chk(f"spectrum 2a (x3), 4a, 2(1 - e) a, a = k: {got}",
        len(got) == 5 and all(sp.simplify(x - y) == 0 for x, y in zip(got, want)))
    return chk.ok


# ------------------------------------------------------------------ T5
def block_threshold(hval):
    """The (t, r) block of (r_h/2)(2 Gamma_t's B-symmetric part - h^-1 l(dr)) at the record's point, and the angular
    eigenvalue."""
    g, f = metric(1)
    gi = g.inv().applyfunc(sp.simplify)
    Gam = christoffel(g, gi)
    c = K * sp.Matrix([1, V / 2, 0, 0, 0])
    B = fibre_B(gi, c, E)[0].subs(r, 1).subs(th, sp.Rational(1, 3))
    gi1 = gi.subs(r, 1).subs(th, sp.Rational(1, 3))
    Gt = sp.Matrix(N, N, lambda a, q: Gam[q][0][a]).subs(r, 1)
    S = Gt + adj(Gt, B)
    T = (S - ell(gi1, c, sp.Matrix([0, 1, 0, 0, 0]), E) / hval) / 2
    return T[:2, :2].applyfunc(sp.nsimplify), T[2, 2], T


def t5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    hv = sp.Rational(1, 1000) if control else H
    Tb, ang, T = block_threshold(hv)
    chk("the angular block is diagonal and decoupled", T[2:, :2] == sp.zeros(3, 2) and T[:2, 2:] == sp.zeros(2, 3)
        and T[2:, 2:] == ang * sp.eye(3))
    p = sp.expand((Tb - lam * sp.eye(2)).det())
    target = -C0 - sp.Rational(1, 2)
    roots = sorted(sp.Poly(p, lam).nroots(n=20))
    top = max(roots[-1], ang)
    # certified: both roots below target iff p(target) > 0 and the vertex (trace/2) < target
    cert = p.subs(lam, target) > 0 and Tb.trace() / 2 < target and ang < target
    chk(f"h = {hv}: vartheta_H+ = {sp.N(top, 12)}, 1/2 + vartheta_H+ = {sp.N(top + sp.Rational(1, 2), 12)} < -C_0",
        bool(cert))
    bound = (1 + E) / (2 * sp.sqrt(E)) - (1 - E) * K / hv
    chk(f"below 10.21 (d)'s bound vartheta_0 - h^-1 (1 - e) r_h a = {sp.N(bound, 12)}", top <= bound)
    if not control:
        # h_2: the largest h with every eigenvalue below the target; lambda_max decreases in h^-1
        hs = sp.Symbol("hs", positive=True)
        Tb_h, ang_h, _ = block_threshold(hs)
        h_ang = sp.solve(sp.Eq(ang_h, target), hs)[0]
        pb = sp.together((Tb_h - target * sp.eye(2)).det())
        quad = 31744512005000 * hs**2 + 3077109850 * hs - 102399
        chk("the block's crossing is the positive root of 31744512005000 h^2 + 3077109850 h - 102399",
            sp.simplify(sp.numer(pb) + quad) == 0 or sp.simplify(sp.numer(pb) - quad) == 0)
        cands = [z for z in sp.Poly(sp.numer(pb), hs).nroots(n=30) if z.is_real and z > 0]
        h_blk = max(cands)
        h2 = min(h_ang, h_blk)
        chk(f"h_2 = min(angular {h_ang}, block {sp.N(h_blk, 10)}) = {sp.N(h2, 10)} > 10^-6", h2 > H)
        Tb2, ang2, _ = block_threshold(sp.nsimplify(h2) * sp.Rational(999, 1000))
        p2 = sp.expand((Tb2 - lam * sp.eye(2)).det())
        chk("just below h_2 the threshold holds",
            bool(p2.subs(lam, target) > 0 and Tb2.trace() / 2 < target and ang2 < target))
    return chk.ok


def _other_inner(hv):
    """(r_h/2) lambda_max of the B'-symmetric part of 2 Gamma_t - h^-1 l(dr), B' = B at e' for e (the operator's e
    kept)."""
    import mpmath as mp
    mp.mp.dps = 30
    g, f = metric(1)
    gi = g.inv().applyfunc(sp.simplify)
    Gam = christoffel(g, gi)
    c = K * sp.Matrix([1, V / 2, 0, 0, 0])
    gi1 = gi.subs(r, 1).subs(th, sp.Rational(1, 3))
    Gt = sp.Matrix(N, N, lambda a, q: Gam[q][0][a]).subs(r, 1)
    X = 2 * Gt - ell(gi1, c, sp.Matrix([0, 1, 0, 0, 0]), E) / hv

    def thr(ep):
        Bp = fibre_B(gi, c, ep)[0].subs(r, 1).subs(th, sp.Rational(1, 3))
        wB = mp.eigsy(mp.matrix(Bp.evalf(30).tolist()))[0]
        T = (X + adj(X, Bp)) / 4                      # (r_h/2) times the B-symmetric part, r_h = 1
        w = mp.eig(mp.matrix(T.evalf(30).tolist()))[0]
        return min(wB), max(mp.re(z) for z in w) + mp.mpf(1) / 2, max(abs(mp.im(z)) for z in w)
    return thr


def t6(control=0, verbose=False):
    """T6: below -C_0 in other fibre inner products, B with e' for e."""
    import mpmath as mp
    chk = Checklist(verbose, quiet=control != 0)
    thr = _other_inner(sp.Rational(1, 1000) if control else H)
    for ep in (sp.Rational(1, 10**5), sp.Rational(1, 10), sp.Integer(3)):
        b0, val, im = thr(ep)
        chk(f"e' = {ep}: B positive definite (least eigenvalue {mp.nstr(b0, 4)}), real spectrum, "
            f"1/2 + vartheta_H+ = {mp.nstr(val, 9)} < -C_0", bool(b0 > 0 and im < mp.mpf(10)**-20 and val < -C0))
    return chk.ok


def t7(control=0, verbose=False):
    """T7: the threshold depends on the inner product: above -C_0 at e' = 10."""
    import mpmath as mp
    chk = Checklist(verbose, quiet=control != 0)
    thr = _other_inner(H)
    ep = sp.Integer(3) if control else sp.Integer(10)
    b0, val, im = thr(ep)
    chk(f"e' = {ep}: B positive definite ({mp.nstr(b0, 4)}), 1/2 + vartheta_H+ = {mp.nstr(val, 9)} > -C_0",
        bool(b0 > 0 and im < mp.mpf(10)**-20 and val > -C0))
    return chk.ok


def t8(control=0, verbose=False):
    """T8: the crossing of -C_0 between e' = 3 and e' = 10, at 7.7638634..."""
    chk = Checklist(verbose, quiet=control != 0)
    thr = _other_inner(H)
    lo, hi = sp.Integer(3), sp.Integer(10)
    for _ in range(30):
        mid = (lo + hi) / 2
        if thr(mid)[1] < -C0:
            lo = mid
        else:
            hi = mid
    window = (sp.Rational(70, 10), sp.Rational(75, 10)) if control else (sp.Rational(77, 10), sp.Rational(78, 10))
    chk(f"the crossing of -C_0 lies at e' = {sp.N(lo, 8)}, in {window}", window[0] < lo < window[1])
    return chk.ok


CHECKS = [("T1 the normalisation 1/beta_0 = r_h/2; R+ = {xi > 0}, dr future null, a = c_t(r_h) = 1/200", t1),
          ("T2 P_0, L from the definitions; P_0 g-symmetric: the adjoint for |dg| taken right", t2),
          ("T3 the box part in B: spectrum +-(e^(1/2) + e^(-1/2))/r_h, 0 (x3); vartheta_0 = 102401/640", t3),
          ("T4 the damping: -h^-1 l(dr), B-self-adjoint, 2a (x3), 4a, 2(1 - e) a", t4),
          ("T5 at (1/2, 1/102400, 10^-6): 1/2 + vartheta_H+ < -100; every h in (0, h_2), 10^-6 < h_2", t5),
          ("T6 other fibre inner products: 1/2 + vartheta_H+ below -100 at e' = 10^-5, 1/10 and 3", t6),
          ("T7 the dependence on the inner product: 1/2 + vartheta_H+ above -100 at e' = 10", t7),
          ("T8 bisection on [3, 10]: the crossing of -100 at e' = 7.7638634...", t8)]


def run(only=None, verbose=False):
    ok = True
    for q, (name, fn) in enumerate(CHECKS, 1):
        if only and q != only:
            continue
        t0 = time.time()
        res = fn(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"hthresh5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, fn in CHECKS:
        total += 1
        res = fn(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"hthresh5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
