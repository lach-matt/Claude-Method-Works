#!/usr/bin/env python3
"""vlasov5: Einstein-massless Vlasov in the T^2 x Z2 x Z2 class, and where its passage to vacuum stops
(FAMILIES5-AXIS.md section 4).

  V1 (exact, sympy) the restricted system. Off the axes g = h_ab dy^a dy^b + e^(2 psi1) dphi1^2 + e^(2 psi2) dphi2^2
     (h a Lorentzian metric on the three-dimensional orbit space, every function of y). The geodesic Hamiltonian is
     Hm = (1/2)(h^ab p_a p_b + sum_i e^(-2 psi_i) p_(phi_i)^2); p_(phi_i) is conserved, and on {p_phi = 0} Hamilton's
     equations are those of h's geodesic flow: the restricted measures (FAMILIES5-FULL Part III V(b): every Burnett
     limit in the class has T_phiphi = 0, so its momenta have p_phi = 0) form an invariant set, on which the Vlasov
     equation is the orbit space's, and T_(phi_i phi_i) = int f p_(phi_i)^2 = 0. Control (must fail): off the set
     (p_phi != 0) dp_a/ds acquires the term -(1/2) p_phi^2 d_a e^(-2 psi).
  V2 (exact, sympy) the axis. Near the axis x3 = x4 = 0, the planar block of a smooth symmetric 2-tensor invariant
     under the rotation of (x3, x4) and the reflections is T_ij = A(s) delta_ij + B(s) x_i x_j (s = |x|^2): computed
     by imposing the invariance on the general polynomial tensor of degree <= 4. Hence T(e_ph, e_ph) = A and
     T(e_rho, e_rho) = A + s B: a smooth stress with T_phph = 0 has radial planar flux T_rhorho = O(rho2^2).
     Control (must fail): the non-smooth xhat (x) xhat (radial dust through the axis, T_phph = 0) has T_rhorho = 1 at
     the axis.
  V3 (computed, mpmath) consequence for a restricted density f(rho2, alpha) >= 0, alpha the angle of the momentum
     with the axis in the meridional plane: T_rhorho = int f E^2 sin^2(alpha) d alpha / (2 pi) must vanish like
     rho2^2. A density continuous in alpha with f(0, alpha) = c > 0 gives T_rhorho(0) = c/2 != 0 (control: not
     smooth); a density concentrating at the axial directions with fixed total density, f = rho2^-1 (exp(-alpha^2 /
     rho2^2) + exp(-(|alpha| - pi)^2/rho2^2)), gives T_rhorho/rho2^2 -> 1/(2 sqrt(pi)) at second order, while d_alpha f
     blows up: at an axis a restricted Vlasov field with smooth stress is either zero there or, in the limit, the two
     radial dusts along the axis (Part I's); a density smooth in (x, alpha) must vanish there.
  V4 (exact, sympy) the high-frequency approximation by N families. For N restricted families with orbit-space
     directions alpha_k = 2 pi k / N, the mixed symbol g^-1(du_A, du_B) = -E_A E_B (1 - cos(alpha_A - alpha_B)) (flat
     orbit space, unit energies) has least modulus 1 - cos(2 pi / N), and N^2 (1 - cos(2 pi / N)) -> 2 pi^2: the
     division of FAMILIES5-FULL section 4 costs a factor of order N^2 / (2 pi^2) per stage, besides [HL25]'s C(N) =
     c^N N^N (READ in FAMILIES5-FULL Part III). Control: N = 2 (one ingoing, one outgoing, Part I) gives 2 for every
     N-independent normalisation, the -2 of axisphase5 A4.

Labels: computed (V1, V2, V4 exact; V3 mpmath). Run: python3 checks/vlasov5.py   (under a minute)
"""
import sys

import mpmath as mp
import sympy as sp


def v1():
    print("V1 (exact) the geodesic flow on {p_phi = 0} is the orbit space's")
    y = sp.symbols('y0:3')
    pa = sp.symbols('p0:3')
    pf = sp.symbols('q1 q2')
    hinv = [[sp.Function('k%d%d' % (min(i, j), max(i, j)))(*y) for j in range(3)] for i in range(3)]
    psi = [sp.Function('psi%d' % i)(*y) for i in (1, 2)]
    Hm = sp.Rational(1, 2) * (sum(hinv[a][b] * pa[a] * pa[b] for a in range(3) for b in range(3))
                              + sum(sp.exp(-2 * psi[i]) * pf[i]**2 for i in range(2)))
    dp = [-sp.diff(Hm, y[a]) for a in range(3)]
    dpf = [0, 0]                                                                # Hm independent of phi: conserved
    dy = [sp.diff(Hm, pa[a]) for a in range(3)]
    Hh = sp.Rational(1, 2) * sum(hinv[a][b] * pa[a] * pa[b] for a in range(3) for b in range(3))
    on = {pf[0]: 0, pf[1]: 0}
    ok = all(sp.simplify(dp[a].subs(on) + sp.diff(Hh, y[a])) == 0 for a in range(3)) and \
        all(sp.simplify(dy[a].subs(on) - sp.diff(Hh, pa[a])) == 0 for a in range(3)) and dpf == [0, 0]
    off = {pf[0]: 1, pf[1]: 0}
    ctl = any(sp.simplify(dp[a].subs(off) + sp.diff(Hh, y[a])) != 0 for a in range(3))
    print("   on p_phi = 0: (dy, dp) = h's geodesic flow, p_phi conserved:", ok, "; control (p_phi1 = 1) differs:", ctl)
    return ok and ctl


def v2():
    print("V2 (exact) a smooth invariant planar tensor: T_ij = A(s) delta_ij + B(s) x_i x_j")
    x3, x4, th = sp.symbols('x3 x4 theta', real=True)
    X = [x3, x4]
    mons = [x3**i * x4**j for i in range(5) for j in range(5) if i + j <= 4]
    cs = {}
    T = [[0, 0], [0, 0]]
    for (i, j) in ((0, 0), (0, 1), (1, 1)):
        ex = 0
        for k, m in enumerate(mons):
            c = sp.Symbol('c_%d%d_%d' % (i, j, k))
            cs[c] = None
            ex += c * m
        T[i][j] = ex
    T[1][0] = T[0][1]
    Tm = sp.Matrix(T)
    # invariance under the rotation by angle th (infinitesimal suffices for SO(2)): L_K T = 0, K = x3 d4 - x4 d3
    K = [-x4, x3]
    dK = sp.Matrix([[sp.diff(K[i], X[j]) for j in range(2)] for i in range(2)])   # dK[i, j] = d_j K^i
    LT = sp.zeros(2, 2)
    for a in range(2):
        for b in range(2):
            LT[a, b] = sum(K[c] * sp.diff(Tm[a, b], X[c]) for c in range(2)) + \
                sum(Tm[c, b] * dK[c, a] + Tm[a, c] * dK[c, b] for c in range(2))
    # reflection x4 -> -x4: T_33(x3,-x4) = T_33, T_34(x3,-x4) = -T_34, T_44(x3,-x4) = T_44
    refl = [Tm[0, 0] - Tm[0, 0].subs(x4, -x4), Tm[0, 1] + Tm[0, 1].subs(x4, -x4), Tm[1, 1] - Tm[1, 1].subs(x4, -x4)]
    eqs = []
    for e in list(LT) + refl:
        eqs += sp.Poly(sp.expand(e), x3, x4).coeffs()
    sol = sp.solve(eqs, list(cs), dict=True)[0]
    Ts = Tm.subs(sol)
    sv = x3**2 + x4**2
    # fit A, B: T(e_ph, e_ph) and T(e_rho, e_rho) at (rho, 0)
    rho = sp.Symbol('rho', positive=True)
    Tpp = sp.expand(Ts[1, 1].subs({x3: rho, x4: 0}))
    Trr = sp.expand(Ts[0, 0].subs({x3: rho, x4: 0}))
    Aexpr = Tpp
    Bexpr = sp.expand((Trr - Tpp) / rho**2)
    # check T = A(s) delta + B(s) x x with A, B functions of s = rho^2 (even in rho)
    Af = sp.expand(Aexpr.subs(rho, sp.sqrt(sv)))
    Bf = sp.expand(Bexpr.subs(rho, sp.sqrt(sv)))
    ok_form = all(sp.expand(Ts[i, j] - (Af * (1 if i == j else 0) + Bf * X[i] * X[j])) == 0
                  for i in range(2) for j in range(2))
    even = sp.expand(Aexpr - Aexpr.subs(rho, -rho)) == 0 and sp.expand(Bexpr - Bexpr.subs(rho, -rho)) == 0
    # T_phph = 0 forces A = 0, then T_rhorho = s B = O(rho^2)
    Asol = sp.solve(sp.Poly(Aexpr, rho).coeffs(), list(Aexpr.free_symbols - {rho}), dict=True)[0]
    Trr0 = sp.Poly(sp.expand(Trr.subs(Asol)), rho)
    ok_flux = Trr0.is_zero or min(m[0] for m in Trr0.monoms()) >= 2
    # control: xhat (x) xhat, non-smooth, T_phph = 0 and T_rhorho = 1 at the axis
    ctl = sp.limit((x3**2 / sv).subs({x3: rho, x4: 0}), rho, 0) == 1
    print("   the general invariant smooth planar tensor (degree <= 4) is A(s) delta + B(s) x x:", ok_form and even,
          "; T_phph = 0 gives T_rhorho = O(rho^2):", ok_flux, "; control xhat xhat has T_rhorho -> 1:", ctl)
    return ok_form and even and bool(ok_flux) and ctl


mp.mp.dps = 30


def v3():
    print("V3 (mpmath) a restricted density at the axis: continuous in alpha forbids it; concentrating gives dust")

    def Trr(f, rho):
        return mp.quad(lambda al: f(rho, al) * mp.sin(al)**2, [-mp.pi, -mp.pi / 2, 0, mp.pi / 2, mp.pi]) / (2 * mp.pi)
    iso = lambda rho, al: mp.mpf(1)                                                   # noqa: E731
    t_iso = Trr(iso, mp.mpf('1e-6'))
    ctl = abs(t_iso - mp.mpf(1) / 2) < mp.mpf('1e-20')
    conc = lambda rho, al: (mp.exp(-al**2 / rho**2) + mp.exp(-(abs(al) - mp.pi)**2 / rho**2)) / rho   # noqa: E731
    norm, dal = [], []
    for rho in ('0.2', '0.1', '0.05', '0.025'):
        r_ = mp.mpf(rho)
        norm.append(Trr(conc, r_) / r_**2)
        dal.append(mp.diff(lambda al: conc(r_, al), r_ / 2))
    L = 1 / (2 * mp.sqrt(mp.pi))
    conv = abs(norm[-1] - L) < mp.mpf('2e-4') and abs(norm[-2] - L) / abs(norm[-1] - L) > 3.5   # second order
    grows = all(abs(dal[i + 1]) > 1.8 * abs(dal[i]) for i in range(3))
    print("   control: continuous f = 1 at the axis has T_rhorho = %s (must be 1/2, not O(rho^2)): %s"
          % (mp.nstr(t_iso, 10), ctl))
    print("   concentrating f: T_rhorho/rho^2 =", [mp.nstr(x, 8) for x in norm], "-> 1/(2 sqrt(pi)):", conv,
          "; d_alpha f grows like 1/rho:", grows)
    return ctl and conv and grows


def v4():
    print("V4 (exact) N restricted families: the least mixed symbol is 1 - cos(2 pi/N) ~ 2 pi^2/N^2")
    ok = True
    vals = []
    for N in (2, 3, 4, 8, 16, 32, 64):
        al = [2 * sp.pi * k / N for k in range(N)]
        least = min(sp.nsimplify(1 - sp.cos(al[a] - al[b])) for a in range(N) for b in range(a + 1, N))
        want = 1 - sp.cos(2 * sp.pi / N)
        ok &= sp.simplify(least - want) == 0
        vals.append((N, least))
    lim = sp.limit(sp.Symbol('N')**2 * (1 - sp.cos(2 * sp.pi / sp.Symbol('N'))), sp.Symbol('N'), sp.oo)
    ok_lim = sp.simplify(lim - 2 * sp.pi**2) == 0
    ctl = sp.simplify(vals[0][1] - 2) == 0
    print("   least symbol:", ", ".join("N=%d: %s" % (N, sp.N(v, 6)) for N, v in vals))
    print("   matches 1 - cos(2 pi/N):", ok, "; N^2 (1 - cos(2 pi/N)) -> 2 pi^2:", ok_lim,
          "; control N = 2 (in/out) gives 2:", ctl)
    return ok and ok_lim and ctl


if __name__ == '__main__':
    res = [v1(), v2(), v3(), v4()]
    print("PASS" if all(res) else "FAIL")
    sys.exit(0 if all(res) else 1)
