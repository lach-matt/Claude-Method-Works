#!/usr/bin/env python3
"""racglobal5: where [Rac16]'s algebraic-hyperbolic split is hyperbolic on Part I's whole slice, what replaces it
where it is not, and the one charge of exactly localised vacuum data (FAMILIES5-VLASOV.md section 5).

  R1 (computed, floating point; twobg5's background at n = 40, 80, 160) Nk (bandconst5 B2: the split is hyperbolic
     exactly where Nk < 0, given E f < 1) on the whole of Sigma_tau0 in Omega_2, every region (seed, packet, gap,
     shell, outside), from the double-null solution: psi_R = B/(3 R^2 R_u^2), psi_vhat, mu_R, mu_vhat through twobg5
     G1 (a)-(c). Nk < 0 everywhere except a band inside the shell, R in [4.29, 4.53] (converged), max Nk = 1.79e-3 at
     R = 4.40: there the split is NOT hyperbolic. Controls (must fail): the same with the flux term -E f_v/2 of Nk
     dropped has no positive value (the shell's flux is the cause); with half the shell's amplitude no positive value.
     [R6, the verifier of round 5, minor 2: the band printed before was the outermost positive samples. The edges are
     now the interpolated zero crossings of Nk, [4.2916, 4.5283] at n = 80 and [4.2914, 4.5284] at n = 160, inside
     [4.29, 4.53] with the margins printed (0.0014 and 0.0016).]
  R2 (exact, sympy) the region-I criterion and the obstruction. In ingoing Vaidya (psi = 0, f = 1 - mu(vhat)/R^2) B2's
     Nk is (mu/R^3)(f - 3) + mu'(vhat)/(2 R^2): hyperbolic iff mu' < 2 mu (2 + mu/R^2)/R. Where Nk > 0 the slice's K
     is negative definite (kappa < 0, K^l_l < 0, round): for every unit normal nhat of every foliation through the
     point, kappa' = K(nhat, nhat) < 0 and K'^l_l = tr K - kappa' < 0, so kappa' K'^l_l > 0 and [Rac16] Lemma 4.1's
     condition fails for every foliation. Control (must fail): a K of mixed sign admits a foliation with kappa' K'^l_l
     < 0. [R6, the verifier of round 5: Lemma 4.1 is sufficient only, so its failure proves nothing by itself. The
     conclusion follows from [Rac16] (4.22): for a covector xi_S tangent to the leaf and orthogonal to k' (the leaves
     are three-dimensional, so a torus direction serves; k'(e_phi) = 0 for a round K) the quadratic K'^l_l xi_n^2 - 2
     xi_n (k'.xi_S) + kappa' |xi_S|^2 has discriminant -kappa' K'^l_l |xi_S|^2 < 0: complex characteristic roots, so
     no tilted foliation is hyperbolic (computed exactly here); control: for the mixed-sign K's hyperbolic tilt the
     discriminant is positive for the torus direction and for the in-plane one. This concerns foliations of the given
     slice only; a different slice through the band is hyperbolic (racslice5).] [R7, the round-6 verifier's n4: the
     exact parts are the identities (Nk, the criterion, K'^l_l and the discriminants as functions of the tilt); that
     their signs hold for every tilt is the one-line deduction above (kappa' < 0, K'^l_l < 0); the 400 random draws
     illustrate it.]
  R3 (exact, sympy) the invariant Killing fields of five-dimensional Tangherlini are the multiples of d_t: solving
     L_X g = 0 for X = X^t d_t + X^R d_R + X^th d_th, components functions of (t, R, th) (T^2 x Z2 x Z2-invariance
     excludes d_phi components, which are odd under phi_i -> -phi_i). Control (must fail): admitting d_phi components
     adds d_phi1, d_phi2. The static KID on Part I's slice in a Tangherlini region (region III: psi = psi(vhat)), X =
     e^-psi d_vhat, has lapse N_s = e^-psi/sqrt(2 e^-psi - f) > 0 (computed as -g(X, n)).
  R4 (computed, floating point) the one charge has a sign on the stream-function seeds. For bandconst5 B4's compactly
     supported linear data (dgamma = 0, a stream function in a band of the seed region of Part I's slice, th in
     [pi/8, 3 pi/8]) the second-order charge against the static KID, Q = int N_s ((tr dK)^2 - |dK|^2) dvol (the
     momentum constraint is linear in K at fixed gamma and contributes none), is negative for every seed tested: 45
     seeds, three bands (one inside the horizon), three frequencies, five directions. Pointwise (exact on Tangherlini,
     psi = 0): (tr dK)^2 - |dK|^2 = (2/(3 (2 - f))) dKt^2 - 2 dp^2 - 2 ds2^2, dkappa from the linearised Hamiltonian
     constraint; the momentum constraint's ds2 makes it negative. Control (must flip): the integrand without its
     -2 ds2^2 term gives Q > 0 for a seed oscillating in th. [R6: qsign5 Q1-Q4 proves the sign for every momentum
     seed, ds1 included: Q <= -int Gamma psi^2/sin 2th, Gamma = 4 mu/R where psi_P = 0; the dust clause of round 5 is
     corrected there (Q5-Q6: inside the horizon outgoing dust has T(xi, n) < 0).]

Labels: computed (R2's identities, R3 exact; R1, R4 floating point). Run: python3 checks/racglobal5.py   (a few minutes)
"""
import importlib.util
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
DROP_S2 = False


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- R1
def slice_nk(tb, n, drop_flux=False):
    uu, vv, R, S, Ru, Rv, mu = tb.run(n)
    dv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]                                            # psi = 0 on N = {u = 0}
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
    tau0 = -tb.AA + 0.02
    A = tb.AAMP * tb.sbump(vv, tb.V1S, tb.V2S)
    B = tb.BAMP * tb.sbump(uu, tb.U1P, tb.U2P)
    Sv = np.gradient(S, dv, axis=1, edge_order=2)
    lvpp = np.gradient(np.log(vhp), dv, edge_order=2)
    out = []
    for i in range(len(uu)):
        tau = vh - R[i]
        m = np.isfinite(tau)
        if not m.any():
            continue
        t = tau[m]
        j = np.where(m)[0]
        k = np.searchsorted(t, tau0)
        if k == 0 or k >= len(t):
            continue
        j0, j1 = j[k - 1], j[k]
        w = (tau0 - tau[j0]) / (tau[j1] - tau[j0])
        I = lambda F: (1 - w) * F[i, j0] + w * F[i, j1]                     # noqa: E731
        I1 = lambda F: (1 - w) * F[j0] + w * F[j1]                           # noqa: E731
        Rr, s, ru, rv, M = I(R), I(S), I(Ru), I(Rv), I(mu)
        sv, vp, vpp, a_, b_ = I(Sv), I1(vhp), I1(lvpp), I1(A), B[i]
        E = np.exp(2 * s) / (-ru * vp)
        f = 1 - M / Rr**2
        psi_u = b_ / (3 * Rr**2 * ru)                                         # twobg5 G1 (b)
        psi_v = 2 * sv + np.exp(2 * s) * M / Rr**3 / ru - vpp                 # R_uv = -e^(2s) mu/R^3, G1 (c)
        psi_R, psi_vh = psi_u / ru, (psi_v - rv / ru * psi_u) / vp
        mu_u = -(2 / 3) * b_ * np.exp(-2 * s) * rv                            # G1 (a)
        mu_v = -(2 / 3) * a_ * np.exp(-2 * s) * ru
        mu_R, mu_vh = mu_u / ru, (mu_v - rv / ru * mu_u) / vp
        fR, fv = 2 * M / Rr**3 - mu_R / Rr**2, -mu_vh / Rr**2
        flux = 0.0 if drop_flux else -E * fv / 2
        Nk = E**2 * f**2 * psi_R + E**2 * f * fR / 2 - 3 * E * f * psi_R + flux - 3 * E * fR / 2 - psi_vh + psi_R
        out.append((Rr, Nk, E * f, a_, mu_vh, M))
    return np.array(out)


def r1():
    print("R1 (computed) Nk on the whole of Part I's Sigma_tau0 (twobg5's background)")
    tb = load('twobg5')
    rows, ok = [], True
    for n in (40, 80, 160):
        o = slice_nk(tb, n)
        pos = o[o[:, 1] > 0]
        band = (float(pos[:, 0].min()), float(pos[:, 0].max())) if len(pos) else None
        # [R6] the interpolated zero crossings of Nk
        srt = o[np.argsort(o[:, 0])]
        cr = [float(srt[j, 0] - srt[j, 1] * (srt[j + 1, 0] - srt[j, 0]) / (srt[j + 1, 1] - srt[j, 1]))
              for j in range(len(srt) - 1) if srt[j, 1] * srt[j + 1, 1] < 0]
        if len(cr) == 2:
            band = (cr[0], cr[1])
        im = int(np.argmax(o[:, 1]))
        # region I check: Nk = (mu/R^3)(f - 3) + mu_vhat/(2 R^2) where psi = 0 and no outgoing dust (A > 0 rows)
        sh = o[o[:, 3] > 0.05]
        f_ = 1 - sh[:, 5] / sh[:, 0]**2
        nk1 = sh[:, 5] / sh[:, 0]**3 * (f_ - 3) + sh[:, 4] / (2 * sh[:, 0]**2)
        dev = float(np.max(np.abs(nk1 - sh[:, 1])))
        rows.append((n, len(o), float(o[:, 0].min()), float(o[:, 0].max()), band, float(o[im, 1]), float(o[im, 0]),
                     float(o[:, 2].max()), dev))
    for (n, npts, rmin, rmax, band, mx, rmx, efmax, dev) in rows:
        print("   n = %d: %d slice points, R in [%.3f, %.3f]; Nk > 0 on R in [%.4f, %.4f] (interpolated zero crossings; "
              "margins to [4.29, 4.53]: %.4f, %.4f); max Nk = %.4e at R = %.4f; max E f = %.4f < 1; region-I formula "
              "vs grid in the shell: %.1e" % (n, npts, rmin, rmax, band[0], band[1], band[0] - 4.29, 4.53 - band[1], mx,
                                              rmx, efmax, dev))
    conv = abs(rows[-1][4][0] - rows[-2][4][0]) < 1e-3 and abs(rows[-1][4][1] - rows[-2][4][1]) < 1e-3 and \
        abs(rows[-1][5] - rows[-2][5]) < 1e-5 and rows[-1][4][0] > 4.29 and rows[-1][4][1] < 4.53
    falls = all(rows[i + 1][8] < rows[i][8] / 3 for i in range(2)) and rows[-1][8] < 1e-6
    ok = all(r[4] is not None and r[5] > 0 and r[7] < 1 for r in rows) and conv and falls
    print("   the region-I formula agrees with the grid to an error falling at second order: %s" % falls)
    # controls
    o_nf = slice_nk(tb, 80, drop_flux=True)
    ctl1 = float(o_nf[:, 1].max()) < 0
    keep = tb.AAMP
    tb.AAMP = keep / 2
    o_h = slice_nk(tb, 80)
    tb.AAMP = keep
    ctl2 = float(o_h[:, 1].max()) < 0
    print("   converged (band edges to 1e-3, inside [4.29, 4.53]; max to 1e-5): %s; controls: flux term dropped, "
          "max Nk = %.4f < 0: %s; half the shell's amplitude, max Nk = %.4f < 0: %s" %
          (conv, float(o_nf[:, 1].max()), ctl1, float(o_h[:, 1].max()), ctl2))
    print("   so the split is hyperbolic on Sigma_tau0 except on the band, which the example's shell creates")
    return ok and ctl1 and ctl2


# ---------------------------------------------------------------- R2
def r2():
    print("R2 (exact identities; signs over the tilts deduced, illustrated on 400 draws) the region-I criterion; where "
          "Nk > 0 no foliation is hyperbolic")
    E, F0, pR, pv, fR, fv, R, mu, mup = sp.symbols('E f psi_R psi_v f_R f_v R mu mup', real=True)
    Nk = E**2 * F0**2 * pR + E**2 * F0 * fR / 2 - 3 * E * F0 * pR - E * fv / 2 - 3 * E * fR / 2 - pv + pR
    f = 1 - mu / R**2
    nkI = Nk.subs({E: 1, pR: 0, pv: 0, F0: f, fR: 2 * mu / R**3, fv: -mup / R**2})
    ok1 = sp.simplify(nkI - (mu / R**3 * (f - 3) + mup / (2 * R**2))) == 0
    crit = sp.simplify(sp.solve(sp.Eq(nkI, 0), mup)[0] - 2 * mu * (2 + mu / R**2) / R) == 0
    # negative definite K = diag(k0, k, k, k) (round, p = 0): every unit normal nhat = (cos b, sin b e)
    k0, k, b = sp.symbols('k0 k b', real=True)
    kap = sp.cos(b)**2 * k0 + sp.sin(b)**2 * k
    Kll = (k0 + 3 * k) - kap
    prod = sp.simplify(kap * Kll)
    rng = np.random.default_rng(5)
    neg_ok, mixed_found = True, False
    for _ in range(400):
        kk0, kk = -rng.uniform(0.01, 3), -rng.uniform(0.01, 3)
        bb = rng.uniform(0, math.pi)
        neg_ok &= float(prod.subs({k0: kk0, k: kk, b: bb})) > 0
    # control: mixed signs (k0 > 0 > k) admit nhat with kappa' Kll' < 0 (the hyperbolic case)
    for _ in range(400):
        bb = rng.uniform(0, math.pi)
        mixed_found |= float(prod.subs({k0: 1.3, k: -0.4, b: bb})) < 0
    # and exactly: for k0, k < 0, kappa' < 0 and Kll' = sin^2 b k0 + (3 - sin^2 b) k < 0
    exact = sp.simplify(Kll - (sp.sin(b)**2 * k0 + (3 - sp.sin(b)**2) * k)) == 0
    # [R6] [Rac16] (4.22): the discriminant for a leaf covector orthogonal to k' (a torus direction)
    kp_plane = sp.sin(b) * sp.cos(b) * (k - k0)                     # k'(e1), e1 the in-plane leaf direction
    disc_torus = sp.simplify(-Kll * kap)                            # (k'.xi)^2 - K'^l_l kappa' |xi|^2, xi = e_phi
    disc_plane = sp.simplify(kp_plane**2 - Kll * kap)
    dneg = True
    for _ in range(400):
        kk0, kk = -rng.uniform(0.01, 3), -rng.uniform(0.01, 3)
        bb = rng.uniform(0, math.pi)
        dneg &= float(disc_torus.subs({k0: kk0, k: kk, b: bb})) < 0
    dpos = False
    for _ in range(400):
        bb = rng.uniform(0, math.pi)
        vals = {k0: 1.3, k: -0.4, b: bb}
        if float(prod.subs(vals)) < 0:
            dpos |= float(disc_torus.subs(vals)) > 0 and float(disc_plane.subs(vals)) > 0
    print("   region I: Nk = (mu/R^3)(f - 3) + mu'/(2 R^2): %s; hyperbolic iff mu' < 2 mu (2 + mu/R^2)/R: %s" %
          (ok1, crit))
    print("   [Rac16] (4.22): the discriminant for a torus direction (k' . e_phi = 0) is -kappa' K'^l_l: negative for "
          "every tilt of a negative definite K (400 draws): %s; control: the mixed-sign K's hyperbolic tilt has both "
          "discriminants positive: %s" % (dneg, dpos))
    print("   K negative definite: K'^l_l = sin^2 b k0 + (3 - sin^2 b) k (exact): %s; kappa' K'^l_l > 0 for every "
          "tilt (400 draws): %s; control (mixed signs) has a hyperbolic tilt: %s" % (exact, neg_ok, mixed_found))
    return ok1 and crit and exact and neg_ok and mixed_found and dneg and dpos


# ---------------------------------------------------------------- R3
def r3():
    print("R3 (exact) the invariant Killing fields of Tangherlini; the static KID's lapse on Part I's slice")
    t, R, th, p1, p2 = sp.symbols('t R theta phi1 phi2', positive=True)
    mu = sp.Symbol('mu', positive=True)
    f = 1 - mu / R**2
    X = [t, R, th, p1, p2]
    g = sp.diag(-f, 1 / f, R**2, R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2)

    def lie(V):
        return sp.Matrix(5, 5, lambda i, j: sp.simplify(
            sum(V[k] * sp.diff(g[i, j], X[k]) + g[k, j] * sp.diff(V[k], X[i]) + g[i, k] * sp.diff(V[k], X[j])
                for k in range(5))))
    Xt, XR, Xth = [sp.Function(nm)(t, R, th) for nm in ('Xt', 'XR', 'Xth')]
    L = lie([Xt, XR, Xth, 0, 0])
    sol = sp.solve([L[3, 3], L[4, 4]], [XR, Xth], dict=True)
    only_t = bool(sol) and sol[0][XR] == 0 and sol[0][Xth] == 0
    L2 = L.subs(sol[0]).doit()
    rest = [sp.simplify(L2[i, j]) for i in range(5) for j in range(i, 5)]
    # with X^R = X^th = 0: L_X g = 0 forces dX^t = 0
    need = set()
    for e in rest:
        for d in e.atoms(sp.Derivative):
            need.add(d)
    const = need <= {sp.Derivative(Xt, t), sp.Derivative(Xt, R), sp.Derivative(Xt, th)} and all(
        sp.simplify(e.subs({sp.Derivative(Xt, t): 0, sp.Derivative(Xt, R): 0, sp.Derivative(Xt, th): 0})) == 0
        for e in rest)
    # control: admitting d_phi components, X = c1 d_phi1 + c2 d_phi2 is Killing
    c1, c2 = sp.symbols('c1 c2')
    ctl = lie([0, 0, 0, c1, c2]) == sp.zeros(5, 5)
    print("   L_X g = 0 for invariant X forces X^R = X^th = 0: %s, then X^t constant: %s; control: d_phi1, d_phi2 "
          "Killing (excluded by the reflections): %s" % (only_t, const, ctl))
    # the static KID's lapse on the slice tau = vhat - R of g0 = -e^(2 psi) f dvhat^2 + 2 e^psi dvhat dR + R^2 dOm^2
    vh = sp.Symbol('vh')
    ps = sp.Function('psi')(vh)
    F = sp.Symbol('F', real=True)
    g2 = sp.Matrix([[-sp.exp(2 * ps) * F, sp.exp(ps)], [sp.exp(ps), 0]])
    gi2 = g2.inv()
    dtau = sp.Matrix([1, -1])
    nn = -(gi2 * dtau) / sp.sqrt(-(dtau.T * gi2 * dtau)[0])
    Xv = sp.Matrix([sp.exp(-ps), 0])
    Ns = sp.simplify(-(Xv.T * g2 * nn)[0])
    want = sp.exp(-ps) / sp.sqrt(2 * sp.exp(-ps) - F)
    lapse = sp.simplify(Ns - want) == 0
    print("   N_s = -g(e^-psi d_vhat, n) = e^-psi/sqrt(2 e^-psi - f) (> 0 since e^psi f < 2): %s" % lapse)
    return only_t and const and ctl and lapse


# ---------------------------------------------------------------- R4
def r4():
    print("R4 (computed) the charge of B4's linear data on Part I's seed slice has one sign")
    bc = load('bandconst5')
    tb = load('twobg5')
    R, th = bc.R, bc.th
    G, k0, Y0 = [sp.Function(nm)(R) for nm in ('G', 'kappa0', 'Y0')]
    eps = sp.Symbol('eps')
    dKt, dp, ds2, dkap = [sp.Function(nm)(R, th) for nm in ('dKt', 'dp', 'ds2', 'dkappa')]
    G1, G2 = R**2 * sp.sin(th)**2, R**2 * sp.cos(th)**2
    g = sp.diag(G, R**2, G1, G2)
    Kt = 3 * Y0 + eps * dKt
    K = sp.zeros(4, 4)
    K[0, 0] = G * (k0 + eps * dkap)
    K[0, 1] = K[1, 0] = sp.sqrt(G) * eps * dp
    K[1, 1] = R**2 * (Kt / 3)
    K[2, 2] = G1 * (Kt / 3 + eps * ds2)
    K[3, 3] = G2 * (Kt / 3 - eps * ds2)
    H, M, _ = bc.constraints(g, K, bc.X4)
    lin = [sp.expand(sp.diff(e, eps).subs(eps, 0)) for e in (H, M[1])]
    dk = sp.solve(sp.Eq(lin[0], 0), dkap)[0]
    mt = sp.expand(lin[1].subs(dkap, dk).doit())
    cs2 = mt.coeff(ds2)
    ds2_sol = sp.simplify(-(mt.subs(ds2, 0)) / cs2)
    # pointwise identity on Tangherlini (psi = 0): with dkappa from H, (tr dK)^2 - |dK|^2 = A dKt^2 - 2 dp^2 - 2 ds2^2
    Ffun = sp.Symbol('f')
    kap_T = sp.Symbol('kT')
    Kt_T = sp.Symbol('KtT')
    dkap_h = sp.simplify(dk / 1)
    form = sp.expand((dk + dKt)**2 - dk**2 - 2 * dp**2 - (dKt**2 / 3 + 2 * ds2**2))
    coefA = sp.simplify(form.coeff(dKt, 2))
    # on Tangherlini kappa0/Y0 = -(3 - f)/(2 - f) (B2: kappa/Kt = -(3 - f)/(3 (2 - f)))
    Asub = sp.simplify(coefA.subs(k0, -(3 - Ffun) / (2 - Ffun) * Y0))
    okA = sp.simplify(Asub - 2 / (3 * (2 - Ffun))) == 0
    print("   pointwise, Tangherlini: (tr dK)^2 - |dK|^2 = %s dKt^2 - 2 dp^2 - 2 ds2^2 (= 2/(3 (2 - f)) dKt^2 ...): %s"
          % (Asub, okA))
    # numeric background: region III of Part I's slice (psi = psi_III(vhat), mu = mu0), n = 80
    uu, vv, Rg, S, Ru, Rv, mu = tb.run(80)
    ia = uu >= tb.U2P + 0.1
    mu0 = float(np.nanmedian(mu[ia, 0][np.isfinite(mu[ia, 0])]))
    k3 = int(np.argmin(np.abs(uu - (tb.U2P + 0.1))))
    dv = vv[1] - vv[0]
    vhp = -np.exp(2 * S[0]) / Ru[0]
    vh = np.concatenate([[0.0], np.cumsum((vhp[1:] + vhp[:-1]) / 2 * dv)])
    psi = np.log(-np.exp(2 * S[k3]) / (Ru[k3] * vhp))
    m = np.isfinite(psi)
    from scipy.interpolate import UnivariateSpline
    sp_psi = UnivariateSpline(vh[m], psi[m], k=5, s=len(vh[m]) * 1e-10)
    tau0 = -tb.AA + 0.02
    Rs = np.linspace(0.72, 1.80, 2161)
    P = sp_psi(tau0 + Rs)
    dP = sp_psi.derivative(1)(tau0 + Rs)
    Ee = np.exp(P)
    f = 1 - mu0 / Rs**2
    fR = 2 * mu0 / Rs**3
    Nk = Ee**2 * f * fR / 2 - 3 * Ee * fR / 2 - dP
    kap = -Nk / (Ee * np.sqrt(2 / Ee - f) * (2 - Ee * f))
    KtN = 3 * (Ee * f - 1) / (Ee * Rs * np.sqrt(2 / Ee - f))
    Gn = -Ee**2 * f + 2 * Ee
    Ns = np.exp(-P) / np.sqrt(2 * np.exp(-P) - f)
    funs = {'G': UnivariateSpline(Rs, Gn, k=5, s=0), 'kappa0': UnivariateSpline(Rs, kap, k=5, s=0),
            'Y0': UnivariateSpline(Rs, KtN / 3, k=5, s=0)}
    aR = -3 / Rs - kap / (Rs * KtN / 3)
    Ia = np.concatenate([[0.0], np.cumsum((aR[1:] + aR[:-1]) / 2 * np.diff(Rs))])
    Ia -= np.interp(1.25, Rs, Ia)
    # the seeds
    psi_s = sp.Function('psi')(R, th)
    Iaf = sp.Function('Ia')(R)
    w = sp.sin(th) * sp.cos(th)
    dKt_s = sp.exp(Iaf) * sp.diff(psi_s, th) / w
    dp_s = R**2 * sp.exp(Iaf) * sp.diff(psi_s, R) / (sp.sqrt(G) * w)
    aexpr = -3 / R - k0 / (R * Y0)
    exprs = {}
    for nm, e in (('dKt', dKt_s), ('dp', dp_s), ('ds2', ds2_sol.subs({dKt: dKt_s, dp: dp_s}).doit()),
                  ('dk', dk.subs({dKt: dKt_s, dp: dp_s}).doit())):
        e = e.subs(sp.Derivative(Iaf, R), aexpr).doit().subs(sp.Derivative(Iaf, (R, 2)), sp.diff(aexpr, R))
        exprs[nm] = e
    # replace functions and derivatives by symbols
    atoms = set()
    for e in exprs.values():
        atoms |= {d for d in e.atoms(sp.Derivative)}
    fn_atoms = set()
    for e in exprs.values():
        fn_atoms |= {a for a in e.atoms(sp.Function) if isinstance(a, sp.core.function.AppliedUndef)}
    syms, vals_of = {}, {}
    for i_, a in enumerate(sorted(atoms | fn_atoms, key=str)):
        syms[a] = sp.Symbol('z%d' % i_)
    lam = {nm: sp.lambdify([R, th] + list(syms.values()), e.xreplace(syms), 'numpy') for nm, e in exprs.items()}
    Th = np.linspace(math.pi / 8, 3 * math.pi / 8, 241)
    RR, TT = np.meshgrid(Rs, Th, indexing='ij')

    def bump(x, a, b):
        y = 2 * (x - a) / (b - a) - 1
        out = np.zeros_like(y)
        mm = np.abs(y) < 1
        out[mm] = np.exp(1 - 1 / (1 - y[mm]**2))
        return out

    def charge(kind, m_, Rband=(0.75, 1.75)):
        Rb, Tb = bump(RR, Rband[0], Rband[1]), bump(TT, math.pi / 8, 3 * math.pi / 8)
        if kind == 'th':
            core = Rb * Tb * np.sin(m_ * (TT - math.pi / 4))
        elif kind == 'R':
            core = Rb * Tb * np.sin(m_ * (RR - 1.25))
        else:                                                                 # a plane wave of direction kind (rad)
            core = Rb * Tb * np.sin(m_ * (math.cos(kind) * (RR - 1.25) + math.sin(kind) * (TT - math.pi / 4)))
        # derivatives of the seed by finite differences on the grid (the seed is smooth)
        dR_, dT_ = Rs[1] - Rs[0], Th[1] - Th[0]
        D = {}
        D[(0, 0)] = core
        D[(1, 0)] = np.gradient(core, dR_, axis=0, edge_order=2)
        D[(0, 1)] = np.gradient(core, dT_, axis=1, edge_order=2)
        D[(2, 0)] = np.gradient(D[(1, 0)], dR_, axis=0, edge_order=2)
        D[(1, 1)] = np.gradient(D[(1, 0)], dT_, axis=1, edge_order=2)
        D[(0, 2)] = np.gradient(D[(0, 1)], dT_, axis=1, edge_order=2)
        D[(2, 1)] = np.gradient(D[(1, 1)], dR_, axis=0, edge_order=2)
        D[(1, 2)] = np.gradient(D[(1, 1)], dT_, axis=1, edge_order=2)
        D[(0, 3)] = np.gradient(D[(0, 2)], dT_, axis=1, edge_order=2)
        D[(3, 0)] = np.gradient(D[(2, 0)], dR_, axis=0, edge_order=2)
        args = []
        for a in syms:
            if isinstance(a, sp.Derivative):
                base = a.expr
                cnt = dict(a.variable_count)
                nR, nT = cnt.get(R, 0), cnt.get(th, 0)
            else:
                base, nR, nT = a, 0, 0
            nm = base.func.__name__
            if nm == 'psi':
                args.append(D[(nR, nT)])
            elif nm == 'Ia':
                args.append(np.interp(RR, Rs, Ia))
            else:
                args.append(funs[nm].derivative(nR)(RR) if nR else funs[nm](RR))
        v = {nm: fn(RR, TT, *args) for nm, fn in lam.items()}
        dK_, dKt_, dp_, ds2_ = v['dk'], v['dKt'], v['dp'], v['ds2']
        dph = dp_ / RR
        integrand = (dK_ + dKt_)**2 - dK_**2 - 2 * dph**2 - (dKt_**2 / 3 + (0 if DROP_S2 else 2 * ds2_**2))
        Nsg = np.interp(RR, Rs, Ns)
        Gg = funs['G'](RR)
        dvol = np.sqrt(Gg) * RR**3 * np.sin(TT) * np.cos(TT)
        Q = np.trapezoid(np.trapezoid(Nsg * integrand * dvol, Th, axis=1), Rs)
        return float(Q) * (2 * math.pi)**2
    rows = []
    for band in ((0.72, 0.9), (0.75, 1.75), (1.0, 1.75)):
        for m_ in (2, 6, 24):
            for phi in (0.0, 0.8, 1.2, math.pi / 2, 2.4):
                rows.append((band, m_, phi, charge(float(phi), m_, band)))
    allneg = all(r[3] < 0 for r in rows)
    worst = max(rows, key=lambda r: r[3])
    print("   %d seeds (bands (0.72, 0.9) inside the horizon, (0.75, 1.75), (1.0, 1.75); m = 2, 6, 24; five directions):"
          " Q < 0 for every one: %s; the least negative %.3e (band %s, m = %d, direction %.2f)" %
          (len(rows), allneg, worst[3], worst[0], worst[1], worst[2]))
    # control (mutated integrand, must flip): without the -2 ds2^2 term forced by the momentum constraint, a seed
    # oscillating in th has Q > 0
    global DROP_S2
    DROP_S2 = True
    qmut = charge(math.pi / 2, 24)
    DROP_S2 = False
    ctl = qmut > 0
    print("   control: the integrand without its -2 ds2^2 term gives Q = %.3e > 0 for the th-seed (rejected): %s" %
          (qmut, ctl))
    return okA and allneg and ctl


def main():
    res = {}
    for name, fn in (('R1', r1), ('R2', r2), ('R3', r3), ('R4', r4)):
        res[name] = fn()
        print(name, 'PASS' if res[name] else 'FAIL', flush=True)
    return 0 if all(res.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
