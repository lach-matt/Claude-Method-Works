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
  V3 (exact) on a round (SO(4)-invariant) background, at a point the isotropy SO(3) acts on the angular part of p by
     rotations of R^3; the set {p_phi1 = p_phi2 = 0} meets it in the line spanned by e_th, and a rotation moves e_th off
     that line: an SO(3)-invariant measure supported in the line is supported at 0. So a round limit's measure is on
     radial momenta.
  V4 (exact) radial null momenta at a point of Vaidya are multiples of dv or of the outgoing radial covector k_out, so a
     radial massless Vlasov measure has T = (int E^2 df_in) dv dv + (int E^2 df_out) k_out k_out: the stress of two null
     dusts, one ingoing and one outgoing (and radial momenta stay radial along radial geodesics).
     Control: a null momentum with p_th != 0 gives T_(th th) > 0, not of that form.

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
    # V3: a rotation about e_phi2 moves e_th off span(e_th) (angular momentum space R^3 = span(e_th, e_phi1, e_phi2))
    al = sp.Rational(1, 3)
    c, s = (1 - al**2) / (1 + al**2), 2 * al / (1 + al**2)
    Rot = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    eth = sp.Matrix([1, 0, 0])
    img = Rot * eth
    v3 = img[1] != 0 or img[2] != 0
    # V4: radial null covectors at a point of Vaidya, in (tau, r): eta^-1 - (mu/r^2) L0 L0; the stress of radial ones
    mu, r = sp.symbols('mu r', positive=True)
    ginv = sp.Matrix([[-1, 0], [0, 1]]) - (mu / r**2) * sp.Matrix([[1, -1], [-1, 1]])
    a = sp.Symbol('a')
    sols = sp.solve(sp.Eq((sp.Matrix([1, a]).T * ginv * sp.Matrix([1, a]))[0], 0), a)
    kin = sp.Matrix([1, 1])
    kout = [sp.Matrix([1, s_]) for s_ in sols if sp.simplify(s_ - 1) != 0][0]
    E = [sp.Rational(rng.randint(1, 7), 3) for _ in range(6)]
    Tr = sum((E[i]**2 * kin * kin.T for i in range(3)), sp.zeros(2, 2)) + \
        sum((E[i]**2 * kout * kout.T for i in range(3, 6)), sp.zeros(2, 2))
    two = sp.simplify(Tr - (sum(e**2 for e in E[:3]) * kin * kin.T + sum(e**2 for e in E[3:]) * kout * kout.T))
    v4 = two == sp.zeros(2, 2) and len(sols) == 2
    # control: a non-radial null momentum has T_thth > 0
    ctl = null(1, sp.Rational(1, 2), 0, 0)[2]**2 > 0
    return v2a and v2b, v3, v4, ctl


def main():
    lm1, mean_ok, quad_ok, ctl1 = v1()
    print('  V1: lam^-1 coefficient of d_a(H^ab d_b f) vanishes on a null phase: %s; its lam^0 th-mean is d_a(H0^ab d_b '
          'f0) exactly: %s; the quadratic term of Ric[h] keeps its Isaacson mean (3/2) <(d_th psi1)^2> du du: %s; '
          'control (h^ab d_a d_b f) acquires a mean term: %s' % (lm1, mean_ok, quad_ok, ctl1), flush=True)
    v2, v3, v4, ctl4 = v2_v4()
    print('  V2: T_(phi phi) = 0 exactly for a measure on momenta with p_phi = 0, > 0 once one has p_phi != 0: %s' % v2)
    print('  V3: a rotation of the isotropy SO(3) moves e_th off its line: %s' % v3)
    print('  V4: radial null momenta at a point of Vaidya are dv and k_out, and their stress is two null dusts: %s; '
          'control (p_th != 0 gives T_thth > 0): %s' % (v4, ctl4), flush=True)
    ok = {'V1': lm1 and mean_ok and quad_ok and ctl1, 'V2': v2, 'V3': v3, 'V4': v4 and ctl4}
    for kname, val in ok.items():
        print(kname, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
