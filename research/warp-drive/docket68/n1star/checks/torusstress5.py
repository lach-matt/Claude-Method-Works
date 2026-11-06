#!/usr/bin/env python3
"""torusstress5: what massless Vlasov limits the T^2 class can produce (FAMILIES5-FULL.md part III).

In the class, g5 = g3 + e^(2A) dphi1^2 + e^(2B) dphi2^2, psi = A + B, omega = (B - A)/2, h = e^(2 psi) g3, and (the
paper's Proposition 2.1, computed in paper/response5.py R1) e^(2 psi) box_h psi = -(e^(-2A) R11 + e^(-2B) R22),
e^(2 psi) box_h omega = (e^(-2A) R11 - e^(-2B) R22)/2, Ric[g5]_(a phi_i) = Ric[g5]_(phi1 phi2) = 0 identically. So the
torus components of the five-dimensional Ricci tensor are the two wave operators box_h psi, box_h omega, and these are in
divergence form, sqrt|h| box_h f = d_a(sqrt|h| h^ab d_b f).

  V1 (exact) the two-scale mean of a divergence-form operator carries no quadratic term: with H^ab := sqrt|h| h^ab =
     H0^ab + lam H1^ab(X, th) (any H1), f = f0 + lam f1(X, th), th = u/lam, u null for H0 (H0(du, du) = 0), the lam^-1
     coefficient of d_a(H^ab d_b f) vanishes and the th-mean of its lam^0 coefficient is d_a(H0^ab d_b f0) exactly,
     every oscillating contribution being a th-derivative. The mean of the quadratic term of Ric[h], (3/2) d psi d psi,
     has the extra Isaacson term (3/2) <(d_th psi1)^2> du du. Hence (deduced, with the weak-limit argument of
     FAMILIES5-FULL.md part III) every Burnett limit inside the class has R11 = R22 = 0 and no mixed torus components:
     its effective stress vanishes on the torus directions.
     Control: the non-divergence operator h^ab d_a d_b f (h = h0 + lam h1, h1 any) has the mean term <h1(du, du)
     d_th^2 f1> = -<d_th h1(du, du) d_th f1>, nonzero for generic h1.
  V2 (exact) for a massless Vlasov measure (a positive combination of null momenta p), T = sum w p (x) p has T_(phi phi)
     = sum w p_phi^2: zero exactly when every momentum in the support has p_phi1 = p_phi2 = 0. With V1: in the class,
     a Burnett limit that is massless Vlasov has its measure on the momenta tangent to the orbit space (the 5D T^2
     analogue of [HL19] Definition 2.7's restricted system).
  V3 (exact; corrected 2026-11-02, round 2, the verifier's item 2) a round background gives a round stress tensor, not
     an invariant measure, so the argument uses T alone. (a) Schur: a symmetric bilinear form on the tangent space of
     S^3 at a point that commutes with the isotropy so(3) (generators J_1, J_2, J_3 in an orthonormal frame (e_th, e_p1,
     e_p2)) is a multiple of the identity: solving [S, J_i] = 0 for a general symmetric S leaves S = c I. So T's
     angular block is c gamma, and T_(th th) = T_(p1 p1) = T_(p2 p2) in that frame. (b) With V2's T_(p p) = 0, c = 0,
     so int p_th^2 d mu = T_(th th) = 0: for a positive measure (weights w_i > 0) the quadratic form sum w_i p_th,i^2
     has Hessian diag(2 w_i), positive definite, so p_th = 0 on the support. The momenta are radial. (Round 5, the
     verifier's minor 3: the test now computes the least eigenvalue, and a control with one negative weight exhibits a
     nonzero p_th with sum w p_th^2 = 0, which the test rejects.)
     Example: a measure with p_p = 0 and one momentum with p_th != 0 has T_(th th) > 0 = T_(p1 p1): not round.
     Control (must fail): without V2, roundness alone does not give p_th = 0: the measure with equal weights on
     +-e_th, +-e_p1, +-e_p2 (null, with p_r = 0) has a round angular block with T_(th th) > 0, so 'round => T_(th th)
     = 0' is false for it.
  V4 (exact) radial null momenta at a point of Vaidya are multiples of dv or of the outgoing radial covector k_out, so a
     radial massless Vlasov measure has T = (int E^2 df_in) dv dv + (int E^2 df_out) k_out k_out: the stress of two null
     dusts, one ingoing and one outgoing (and radial momenta stay radial along radial geodesics).
     Computed (round 5, the verifier's minor 3: the earlier test compared a sum with its own factoring): k_in and
     k_out are the roots of the actual g0^-1, every momentum of the measure is null, and its stress is solved into
     span(k_in k_in, k_out k_out). Controls (must fail): the measure with one more null momentum carrying p_th != 0
     has no such solution; k_out taken from a wrong metric (mu -> mu/2) is not null for g0^-1.

So inside the class, round massless Vlasov limits are exactly the two-dust limits of part I. Labels: computed (exact,
sympy); the weak-limit step deduced. Run: python3 checks/torusstress5.py   (seconds)
"""
import random
import sys

import sympy as sp


def v1():
    lam, th = sp.symbols('lam theta')
    n = 3
    X = sp.symbols('x0:3')
    # a null covector field k = du: take u with H0(du, du) = 0 imposed algebraically at the end
    u = sp.Function('u')(*X)
    k = [sp.diff(u, x) for x in X]
    H0 = [[sp.Function('H0_%d%d' % (min(a, b), max(a, b)))(*X) for b in range(n)] for a in range(n)]
    # two harmonics for every oscillating amplitude
    def osc(name):
        return sum(sp.Function('%s_%d' % (name, m))(*X) * sp.exp(sp.I * m * th) for m in (-2, -1, 1, 2))
    H1 = [[osc('H1_%d%d' % (min(a, b), max(a, b))) for b in range(n)] for a in range(n)]
    f0 = sp.Function('f0')(*X)
    f1 = osc('f1')
    il = sp.Symbol('il')                                                         # 1/lam

    def D(e, a):
        return sp.diff(e, X[a]) + il * k[a] * sp.diff(e, th)
    H = [[H0[a][b] + lam * H1[a][b] for b in range(n)] for a in range(n)]
    f = f0 + lam * f1
    div = sum(D(H[a][b] * D(f, b), a) for a in range(n) for b in range(n))
    div = sp.expand(div.subs(il, 1 / lam))
    nul = sum(H0[a][b] * k[a] * k[b] for a in range(n) for b in range(n))

    def mean(e):
        e = sp.expand(e)
        return sum(t for t in sp.Add.make_args(e) if not t.has(th))
    cm1 = sp.expand(div.coeff(lam, -1))
    c0 = div.coeff(lam, 0)
    # impose nullness: H0_00 eliminated
    sol = sp.solve(sp.Eq(nul, 0), H0[0][0])[0]

    def onnull(e):
        return sp.simplify(sp.expand(e).subs(H0[0][0], sol).doit())
    lam_m1 = onnull(cm1) == 0
    bg = sum(sp.diff(H0[a][b] * sp.diff(f0, X[b]), X[a]) for a in range(n) for b in range(n))
    mean_ok = onnull(mean(c0) - bg) == 0
    # the Ricci quadratic term's mean: (3/2) d_a psi d_b psi with psi = f
    q = sp.expand(sp.Rational(3, 2) * D(f, 0) * D(f, 0)).subs(il, 1 / lam)
    qm = mean(sp.expand(q).coeff(lam, 0))
    isa = sp.Rational(3, 2) * k[0]**2 * mean(sp.expand(sp.diff(f1, th)**2))
    quad_ok = sp.simplify(qm - sp.Rational(3, 2) * sp.diff(f0, X[0])**2 - isa) == 0 and sp.simplify(isa) != 0
    # control: h^ab d_a d_b f, non-divergence
    nd = sp.expand(sum(H[a][b] * D(D(f, b), a) for a in range(n) for b in range(n)).subs(il, 1 / lam))
    nd0 = mean(nd.coeff(lam, 0))
    bgnd = sum(H0[a][b] * sp.diff(f0, X[a], X[b]) for a in range(n) for b in range(n))
    ctl = onnull(nd0 - bgnd) != 0
    return lam_m1, mean_ok, quad_ok, ctl


def v2_v4(seed=5):
    rng = random.Random(seed)
    # V2: T_phiphi of a positive discrete measure on null momenta (Minkowski 4+1 at a point, orthonormal frame
    # (t, r, th, phi1, phi2))
    def null(pr, pth, p1, p2):
        return [sp.sqrt(pr**2 + pth**2 + p1**2 + p2**2), pr, pth, p1, p2]
    ws = [sp.Rational(rng.randint(1, 9), 4) for _ in range(5)]
    moms_orbit = [null(sp.Rational(rng.randint(-5, 5), 3), sp.Rational(rng.randint(-5, 5), 3), 0, 0) for _ in range(5)]
    T = lambda moms: [[sum(w * p[a] * p[b] for w, p in zip(ws, moms)) for b in range(5)] for a in range(5)]  # noqa
    To = T(moms_orbit)
    v2a = To[3][3] == 0 and To[4][4] == 0 and all(To[a][3] == 0 and To[a][4] == 0 for a in range(5))
    moms_bad = moms_orbit[:4] + [null(1, 0, sp.Rational(1, 2), 0)]
    Tb = T(moms_bad)
    v2b = Tb[3][3] > 0
    # V3 (a): Schur for so(3) on the angular tangent space, orthonormal frame (e_th, e_p1, e_p2)
    Ss = sp.Matrix(3, 3, lambda a, b: sp.Symbol("S%d%d" % (min(a, b), max(a, b))))
    Js = [sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]), sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
          sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])]
    eqs = [e for J in Js for e in (Ss * J - J * Ss)]
    sol = sp.solve(eqs, sorted(Ss.free_symbols, key=str), dict=True)
    Sinv = Ss.subs(sol[0]) if sol else None
    schur = Sinv is not None and sp.simplify(Sinv - Sinv[0, 0] * sp.eye(3)) == sp.zeros(3)
    # V3 (b): with T_(p1 p1) = 0 the round block is 0, so sum w p_th^2 = 0; for positive weights this forces p_th = 0
    # (round 5, the verifier's minor 3: the test now uses the weights' sign). The form's least eigenvalue is computed;
    # control: one negative weight admits a nonzero p_th with sum w p_th^2 = 0.
    nw = 5

    def forces_zero(ws_):
        Hs = sp.diag(*[2 * w for w in ws_])
        evs = list(Hs.eigenvals().keys())
        if min(evs) > 0:
            return True
        # exhibit a nonzero null vector of the form when it exists (two weights of opposite signs)
        ip = [i for i, w in enumerate(ws_) if w > 0]
        im = [i for i, w in enumerate(ws_) if w < 0]
        if ip and im:
            q = [0] * nw
            q[ip[0]] = sp.sqrt(-ws_[im[0]])
            q[im[0]] = sp.sqrt(ws_[ip[0]])
            assert sp.simplify(sum(w * x**2 for w, x in zip(ws_, q))) == 0 and any(x != 0 for x in q)
        return False
    wpos = [sp.Rational(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(nw)]
    wmix = list(wpos)
    wmix[2] = -wmix[2]
    posdef = forces_zero(wpos) and not forces_zero(wmix)
    # example: p_p = 0, one momentum with p_th != 0: T_thth > 0 = T_p1p1 -> not round
    moms_ex = moms_orbit[:4] + [null(sp.Rational(1, 3), sp.Rational(1, 2), 0, 0)]
    Tex = T(moms_ex)
    notround = Tex[2][2] > 0 and Tex[3][3] == 0
    # control: no V2 premise; equal weights on +-e_th, +-e_p1, +-e_p2 (null, p_r = 0): round block, T_thth > 0
    iso = [null(0, s_ * 1, 0, 0) for s_ in (1, -1)] + [null(0, 0, s_ * 1, 0) for s_ in (1, -1)] + \
        [null(0, 0, 0, s_ * 1) for s_ in (1, -1)]
    Tiso = [[sum(p[a] * p[b] for p in iso) for b in range(5)] for a in range(5)]
    blk = sp.Matrix(3, 3, lambda a, b: Tiso[a + 2][b + 2])
    iso_round = sp.simplify(blk - blk[0, 0] * sp.eye(3)) == sp.zeros(3)
    v3_ctl_implication = (not iso_round) or Tiso[2][2] == 0                     # 'round => T_thth = 0' on it
    v3 = schur and posdef and notround and not v3_ctl_implication
    # V4: radial null covectors at a point of Vaidya, in (tau, r): g0^-1 = eta^-1 - (mu/r^2) L0 L0 (round 5, the
    # verifier's minor 3: the covectors are now tested to be roots of the actual g0^-1, the radial stress is shown to
    # lie in span(k_in k_in, k_out k_out) by solving for its coefficients, and the controls are real)
    mu, r = sp.symbols('mu r', positive=True)

    def ginv_of(m_):
        return sp.Matrix([[-1, 0], [0, 1]]) - (m_ / r**2) * sp.Matrix([[1, -1], [-1, 1]])
    ginv = ginv_of(mu)
    a = sp.Symbol('a')
    q2 = lambda G_, k: sp.simplify((k.T * G_ * k)[0])                                  # noqa: E731
    sols = sp.solve(sp.Eq(q2(ginv, sp.Matrix([1, a])), 0), a)
    ks = [sp.Matrix([1, s_]) for s_ in sols]
    roots_ok = len(ks) == 2 and all(q2(ginv, k) == 0 for k in ks)
    kin = [k for k in ks if sp.simplify(k[1] - 1) == 0][0]
    kout = [k for k in ks if sp.simplify(k[1] - 1) != 0][0]
    E = [sp.Rational(rng.randint(1, 7), 3) for _ in range(6)]
    moms = [E[i] * kin for i in range(3)] + [E[i] * kout for i in range(3, 6)]
    null_ok = all(q2(ginv, p) == 0 for p in moms)
    Tr = sum((p * p.T for p in moms), sp.zeros(2, 2))
    al, be = sp.symbols('alpha beta')
    span = sp.solve(list(Tr - al * kin * kin.T - be * kout * kout.T), [al, be], dict=True)
    in_span = bool(span) and all(sp.simplify(v) != 0 for v in span[0].values())
    v4 = roots_ok and null_ok and in_span
    # control 1 (must fail): one momentum with p_th != 0 (a null covector (p_tau, p_r, p_th) at the point): the stress,
    # with its (th th) entry, is not of the two-dust form
    pth = sp.Rational(3, 7)
    # null: ginv(p, p) + p_th^2/r^2 = 0 with p = (1, x)
    x = sp.Symbol('x')
    xs = sp.solve(sp.Eq(q2(ginv, sp.Matrix([1, x])) + pth**2 / r**2, 0), x)
    extra2 = sp.Matrix([1, xs[0]])
    T3 = sp.zeros(3, 3)
    for p in moms:
        T3[:2, :2] += p * p.T
    pe = sp.Matrix([1, xs[0], pth])
    T3 += pe * pe.T
    K3 = lambda k: sp.Matrix([k[0], k[1], 0]) * sp.Matrix([k[0], k[1], 0]).T   # noqa: E731
    span_bad = sp.solve(list(T3 - al * K3(kin) - be * K3(kout)), [al, be], dict=True)
    ctl1 = not span_bad
    # control 2 (must fail): k_out taken from a wrong metric (mu -> mu/2) is not null for the actual g0^-1
    solw = sp.solve(sp.Eq(q2(ginv_of(mu / 2), sp.Matrix([1, a])), 0), a)
    koutw = [sp.Matrix([1, s_]) for s_ in solw if sp.simplify(s_ - 1) != 0][0]
    ctl2 = q2(ginv, koutw) != 0
    two_dust_rad = in_span
    ctl = ctl1 and ctl2
    return v2a and v2b, (v3, schur, posdef, notround, iso_round, Tiso[2][2], not v3_ctl_implication), \
        v4 and two_dust_rad, ctl


def main():
    lm1, mean_ok, quad_ok, ctl1 = v1()
    print('  V1: lam^-1 coefficient of d_a(H^ab d_b f) vanishes on a null phase: %s;\n'
          '      its lam^0 th-mean is d_a(H0^ab d_b f0) exactly: %s;\n'
          '      the quadratic term of Ric[h] keeps its Isaacson mean (3/2) <(d_th psi1)^2> du du: %s;\n'
          '      control (h^ab d_a d_b f) acquires a mean term: %s' % (lm1, mean_ok, quad_ok, ctl1), flush=True)
    v2, v3, v4, ctl4 = v2_v4()
    print('  V2: T_(phi phi) = 0 exactly for a measure on momenta with p_phi = 0, > 0 once one has p_phi != 0:\n'
          '      %s' % v2)
    v3, schur, posdef, notround, iso_round, tiso, rej = v3
    print('  V3: (a) an so(3)-commuting symmetric form on the angular space is c I (Schur): %s;\n'
          '      (b) sum w p_th^2 = 0 forces p_th = 0 for positive weights (least eigenvalue of diag(2 w) > 0;\n'
          '      control, one negative weight, admits a nonzero p_th and is rejected): %s;\n'
          '      a measure with p_p = 0 and one p_th != 0 is not round: %s' % (schur, posdef, notround))
    print('  V3 control: without V2, the isotropic angular measure is round (%s) with T_thth = %s > 0, so round\n'
          '      alone does not give p_th = 0: the implication is rejected: %s' % (iso_round, tiso, rej))
    print('  V4: radial null momenta at a point of Vaidya are dv and k_out, and their stress is two null dusts: %s;\n'
          '      (k_in, k_out roots of the actual g0^-1, every momentum null, the stress solved into span(k_in k_in,\n'
          '      k_out k_out)); controls rejected (a momentum with p_th != 0 added: no solution; k_out from a wrong\n'
          '      metric not null): %s' % (v4, ctl4),
          flush=True)
    ok = {'V1': lm1 and mean_ok and quad_ok and ctl1, 'V2': v2, 'V3': v3 and rej, 'V4': v4 and ctl4}
    for kname, val in ok.items():
        print(kname, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
