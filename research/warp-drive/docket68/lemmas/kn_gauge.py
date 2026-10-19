#!/usr/bin/env python3
"""kn_gauge.py -- item 517: the Killing-norm torus-frame gauge (KN gauge), derived from L-UNIF''s five needs and
proved to meet them.

M, 517: "We need to derive and then prove a new or previously unidentified gauge that will meet the needs of the
theorem".  The needs are 515's: N1 a well-posed problem on the domain; N2 uniform linear control of the growing 5D
hole over the shell; N3 the high-frequency remainder; N4 the interior to x = 1, nothing cut out; N5 the nonlinear
closure.  516 found that no published gauge meets all five, and that none meets N2 (linearized gravity on a growing
5D hole: Teukolsky does not decouple in D > 4).  Labels: computed (exact unless marked), READ, deduced, M's.

  K0 (M's) 517 and 518, verbatim.
  K1 (computed, exact) The derivation's first step: the class carries no gravitational waves in its base.  For any
     5D metric g = g3 + e^(2U1) dphi1^2 + e^(2U2) dphi2^2 (the T^2-mirror class: two commuting, orthogonal,
     hypersurface-orthogonal Killing fields), with g3 general (Bondi form: every 3D metric with a null foliation):
       R_(phi_i phi_i) = -e^(2U_i) box_5 U_i,  R_(a phi) = 0,  R_ab = R3_ab - sum_i (D_a D_b U_i + d_a U_i d_b U_i),
     and in the torus frame h = rho^2 g3, rho = e^(U1+U2), off shell,
       R[h]_ab = R_ab + sum_i d_a U_i d_b U_i + d_a psi d_b psi + g3_ab sum_i e^(-2U_i) R_(phi_i phi_i),  psi = ln rho.
     So vacuum in the class is exactly 2+1 gravity on h coupled to two free massless scalars:
       R[h] = (3/2) dpsi^2 + 2 domega^2,   box_h psi = box_h omega = 0,   omega = (U1 - U2)/2.
     2+1 gravity has no local degrees of freedom: every wave of the class lives in psi and omega, which are the
     Killing norms -- geometric scalars, the same in every gauge.  (Prior art: the reduction of D dimensions with D-2
     commuting hypersurface-orthogonal Killing fields to 2D dilaton gravity with scalars, Schmidt gr-qc/9712034; the
     4D polarized-U(1) reduction to 2+1 Einstein-wave map, Choquet-Bruhat-Moncrief, Huneau-Luk 1706.09499.  The 5D
     cohomogeneity-three T^2 form, with its torus frame, is the step identified here for this problem.)
  K2 (computed, exact) Waves and energy.  For every T^2-invariant f, box_h f = rho^-2 box_5 f, and for every base
     vector field X the 5D energy current J = T[f](X, .) obeys
       div_5 J = rho^2 ( (1/2) T_h[f]^ab (L_X h)_ab + (X f) box_h f ).
     The radiation's own oscillation -- in psi, omega, the torus, the conformal factor -- never enters the energy
     identity of a T^2-invariant field.  Only the base metric h does.
  K3 (computed, exact) The gauge.  Coordinates: v the phase of the incoming radiation, null (g^vv = 0); theta
     comoving along the null generators; r fixed by h_thth = r^6 sin^2 theta cos^2 theta.  On the record's ansatz
     this is exactly its Bondi gauge (h_thth = rho^2 g_thth = r^6 s^2 c^2 for all P1, P2), so F1-F7 and every run
     stand in it.  In it h_rr = h_rth = 0 and h_thth is wave-independent, so every oscillation of h lies in the v-row,
     which is l (x) zeta + zeta (x) l with l = dv: pure gauge.  This is special to 2+1: the kernel of the linearized
     Ricci tensor's high-frequency symbol (null l) has dimension 3 = n in 2+1 -- gauge only -- against 6 = 4 + 2 in
     3+1 and 10 = 5 + 5 in 4+1, where the excess is the gravitational polarizations.  The near-identity fast
     diffeomorphism x -> x + lam^2 Xi(x, v/lam) adds lam (l (x) h.Xi' + h.Xi' (x) l) + O(lam^2) and so removes h's
     first-order oscillation: in the averaged KN gauge h is C^1-close (O(lam)) to the averaged metric.  On the
     background the torus frame reproduces Tangherlini exactly, and to first order h_vr's response is exactly
     2 dpsi h_vr (the rr equation).
  K4 (computed, exact) The contraction.  For a Bondi-form h, T_h[f]^(va) contains no f_v: the oscillation, which
     lives in the v-row, meets only the derivatives f_r, f_th that the energy on the null cones v = const controls.
  K5 (computed, exact; constants computed) N2, the linear engine.  By K1-K2 the linear problem of the class is the
     scalar wave equation for T^2-invariant fields on the averaged background, 5D Vaidya with mu' >= 0 -- not
     linearized gravity.  On it, in units of sqrt(mu(v)), z = r/sqrt(mu):
       (a) Kodama: the bulk of T = d_v is (mu'/2r^2) f_r^2 >= 0, the apparent horizon is spacelike and a future
           boundary of the exterior, so the exterior T-energy is non-increasing apart from what enters at past null
           infinity;
       (b) the multiplier X = alpha d_v - sigma d_r, alpha = 12z^4 - 4z^6 + (3/8)z^8, sigma = z^2 (4 - z^2)^2 for
           z < 2, X = 32 d_v beyond (C^1 at z = 2), is future timelike on (0, inf) (root count), its bulk is
           positive definite on (0, sqrt(12/7)) -- through the apparent horizon at z = 1 -- and its (v, r) block is
           semidefinite to z = 2 (root count), for every growth rate eps = mu'/sqrt(mu) in [0, 1/20];
       (c) the shell's largest eps is 0.0219 (the record's sin^8 flux, D = 269.15 r_h, the least seed);
       (d) with b = 0.0748 (the bulk's rate on (0, 1.2]), B = 15.6 (its angular deficit on [1.2, 2] against the
           T-energy), C1 = 76.3, c1 = 8.38 (the energies' ratios outside), Dafermos-Rodnianski's argument (red-shift
           plus a monotone T-energy; READ, with the lemma proved here) gives the nondegenerate energy on every cone
           at most C2 = 1 + (B/b + C1)/c1 = 35.0 times its data and input -- uniformly in v and lam, across the
           horizon, to x = 1;
       (e) the weight at x = 1 (z_q = 1/158 at the end): the energy density there is weighted by z^2, a factor
           2.2e4 in energy, 150 in amplitude.
  K6 (deduced) N1.  In the KN gauge the radiative equations are linear waves (K1-K2) and the base's three main
     equations (rr, r theta, theta theta) have sources 2 dPsi.dPsi in the cone-tangential derivatives only -- no
     v-derivative, no second derivative (K1).  The second derivatives that make Bondi's free evolution weakly
     hyperbolic (D D U in R3) are removed exactly by the torus frame.  Well-posedness of the characteristic problem
     then follows the standard energy method; that step is not machine-checked here.
     [Item 520, counterpart5.py: K6 withdrawn.  The KN gauge's hypersurface equations are Bondi's hierarchy:
     theta-theta fixes h_vv through d_theta^2 h_vr, and h_vv is in h^rr, so an estimate loses two angular derivatives
     (P2).  And K5 corrected: the background Killing norms' wave operator, linearized in the base metric, holds h_vv,
     d_r h_vv, d_theta h_vr and d_r h_vth with O(1) coefficients (P3), so the class's linear problem is linearized
     gravity; K5's multiplier and constant 35 hold for T^2-invariant test fields, and K8's ratios are measured against
     that energy.]
  K7 (deduced) N4.  The coordinates are the record's (K3): the sequence reaches x = 1 in them (hf_core5) and the
     boundary there is spacelike with every characteristic leaving (hf_theorem5 F2); the averaging diffeomorphism is
     O(lam^2), so the boundary stays spacelike.
  K8 (computed; one estimate, one part open) N3 and N5, the oscillation in the energy estimate.  The first-order
     response of h is computed exactly: h_vr 2 dpsi h_vr, h_vth Phi c_p(theta) r^(7/2), h_vv from the theta theta
     equation; the record's profiles satisfy the leading supplementary constraints (vanishing to 1e-15), so the
     homogeneous mass and angular-momentum aspects are not driven at first order.  Its contraction with T_h is a form
     in (f_r, f_th) (K4); against X's positive bulk its largest ratio is lambda(z) per unit A env mu^(-1/4): 1.7e-4 at
     z = 0.01, 0.2 at 0.5, 4.4 at 1, 15 at 1.2.  Over the record's shell with 10 l5 waves the oscillation is absorbed
     outright below z_hf = (29.1 w/sqrt(mu))^(1/2) (the waves' high-frequency edge) and z = 1.2: largest ratio 0.92
     (it reaches 1 at 12.5 l5); above z_hf the averaging removes it exactly (K3).  After the seed phase the remainder
     is second order: exponent 0.21 (estimate: strain times the first-order rate, not computed at second order).  The
     seed phase -- the hole under 20 wavelengths, sqrt(mu) < 202 l5, s < 0.11, 7.7e-6 of the shell's energy -- is
     where the waves are not high-frequency outside the hole and no positive bulk is there: the crude sup-norm
     exponent is 1.2e4 (the whole shell crude: 1.4e4; 515's e^43 was the end scale only).  That part of N5 stays
     open: it needs a weighted (Morawetz or Hardy) estimate outside the small hole in place of the sup.
     [Item 520: the seed phase exists only above 0.144 l5 and the 0.21 is held by its edge (counterpart5 P1): both
     belong to the 10 l5 application, not to the lam -> 0 theorem.]

numpy, sympy.  Imports hf_anchor5.py (our universe's values) by path.
python3 kn_gauge.py [--selftest | --mutants | --build-k8]   (the K8 core is cached in data/kn_gauge_k8.json, keyed by the hash of
the code that computes it; --build-k8 recomputes it, about three minutes)
"""
import contextlib
import importlib.util
import io
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()
EPS_STAR = sp.Rational(1, 20)
Z_G = 1.2


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    t = open(RULINGS, encoding="utf-8").read()
    return ("derive and then prove a new or previously unidentified gauge that will meet the needs of the theorem" in t
            and "Continue, and check the background tasks please" in t)


def _christ(g, X):
    gi = sp.simplify(g.inv()); n = len(X)
    G = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    return gi, G


def _ricci(g, X):
    gi, G = _christ(g, X); n = len(X)
    R = sp.zeros(n)
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                for d in range(n):
                    e += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            R[b, c] = R[c, b] = e
    return gi, G, R


def k1_k2():
    """the reduction, the torus frame, the wave operator and the energy identity -- exact, general Bondi base"""
    v, r, th, p1, p2 = sp.symbols("v r theta phi1 phi2")
    X3 = [v, r, th]; X = X3 + [p1, p2]
    b, W, U, gam, U1, U2 = [sp.Function(n)(v, r, th) for n in ("b", "W", "U", "gam", "U1", "U2")]
    g3 = sp.Matrix([[-sp.exp(2*b)*W + gam*U**2, sp.exp(2*b), -gam*U], [sp.exp(2*b), 0, 0], [-gam*U, 0, gam]])
    g5 = sp.zeros(5); g5[:3, :3] = g3; g5[3, 3] = sp.exp(2*U1); g5[4, 4] = sp.exp(2*U2)
    _, _, R5 = _ricci(g5, X)
    gi3, G3, R3 = _ricci(g3, X3)
    s3 = sp.exp(2*b)*sp.sqrt(gam)
    rho = sp.exp(U1 + U2)
    d = lambda f, a: sp.diff(f, X3[a])
    box5 = lambda f: sum(sp.diff(rho*s3*gi3[a, c]*d(f, c), X3[a]) for a in range(3) for c in range(3))/(rho*s3)
    hess = lambda f, a, c: sp.diff(f, X3[a], X3[c]) - sum(G3[e][a][c]*d(f, e) for e in range(3))
    sgn = -1 if "torus_sign" in MUT else 1
    I1 = [sp.simplify(R5[3, 3] + sgn*sp.exp(2*U1)*box5(U1)), sp.simplify(R5[4, 4] + sgn*sp.exp(2*U2)*box5(U2)),
          sp.simplify(R5[3, 4])] + [sp.simplify(R5[a, k]) for a in range(3) for k in (3, 4)]
    I2 = [sp.simplify(R5[a, c] - (R3[a, c] - sum(hess(Ui, a, c) + d(Ui, a)*d(Ui, c) for Ui in (U1, U2))))
          for a in range(3) for c in range(a, 3)]
    pw = 1 if "no_rho2" in MUT else 2
    h = rho**pw*g3
    gih, _, Rh = _ricci(h, X3)
    om = U1 + U2
    I3 = [sp.simplify(Rh[a, c] - (R5[a, c] + sum(d(Ui, a)*d(Ui, c) for Ui in (U1, U2)) + d(om, a)*d(om, c)
                                  + g3[a, c]*(sp.exp(-2*U1)*R5[3, 3] + sp.exp(-2*U2)*R5[4, 4])))
          for a in range(3) for c in range(a, 3)]
    F = sp.Function("F")(v, r, th)
    sh = sp.sqrt(sp.simplify(-h.det()))
    boxh = sum(sp.diff(sh*gih[a, c]*d(F, c), X3[a]) for a in range(3) for c in range(3))/sh
    I4 = sp.simplify(boxh - box5(F)/rho**2)
    Xv = [sp.Function("X%d" % i)(v, r, th) for i in range(3)]
    gr_g = sum(gi3[a, c]*d(F, a)*d(F, c) for a in range(3) for c in range(3))
    T5 = lambda a, c: d(F, a)*d(F, c) - sp.Rational(1, 2)*g3[a, c]*gr_g
    J5 = [sum(gi3[a, q]*T5(q, c)*Xv[c] for q in range(3) for c in range(3)) for a in range(3)]
    div5 = sum(sp.diff(rho*s3*J5[a], X3[a]) for a in range(3))/(rho*s3)
    gr_h = sum(gih[a, c]*d(F, a)*d(F, c) for a in range(3) for c in range(3))
    Th = lambda a, c: d(F, a)*d(F, c) - sp.Rational(1, 2)*h[a, c]*gr_h
    LXh = lambda a, c: sum(Xv[e]*sp.diff(h[a, c], X3[e]) + h[e, c]*sp.diff(Xv[e], X3[a]) + h[a, e]*sp.diff(Xv[e], X3[c])
                           for e in range(3))
    Thup = lambda a, c: sum(gih[a, p]*gih[c, q]*Th(p, q) for p in range(3) for q in range(3))
    XF = sum(Xv[e]*d(F, e) for e in range(3))
    I5 = sp.simplify(sp.expand(div5 - rho**2*(sp.Rational(1, 2)*sum(Thup(a, c)*LXh(a, c) for a in range(3) for c in range(3))
                                              + XF*boxh)))
    return dict(I1=I1, I2=I2, I3=I3, I4=I4, I5=I5)


def k3():
    """the gauge on the record's ansatz; the 2+1 symbol kernel; the fast diffeomorphism; the background"""
    out = {}
    r, th = sp.symbols("r theta", positive=True)
    P1, P2 = sp.symbols("P1 P2", real=True)
    rho = r**2*sp.cos(th)*sp.sin(th)*sp.exp(P1 + P2)
    gthth = r**2*sp.exp(-2*(P1 + P2))
    out["hthth"] = sp.simplify(rho**2*gthth - r**6*sp.sin(th)**2*sp.cos(th)**2)
    # high-frequency symbol of linearized Ricci: k -> l(l.k) + (l.k)l - l l tr k, null l
    dims = {}
    for n in (3, 4, 5):
        eta = sp.diag(*([-1] + [1]*(n - 1)))
        l = sp.Matrix([1, 1] + [0]*(n - 2))                      # null covector
        basis = [(i, j) for i in range(n) for j in range(i, n)]
        cols, gauge = [], []
        for (i, j) in basis:
            k = sp.zeros(n); k[i, j] = k[j, i] = 1
            lk = k*eta*l                                          # (l.k)_a = k_ab eta^bc l_c
            trk = (eta*k).trace()
            sig = l*lk.T + lk*l.T - l*l.T*trk
            if "tt_in_3" in MUT and n == 3:
                sig = l*lk.T + lk*l.T
            cols.append([sig[a, b] for (a, b) in basis])
        Mx = sp.Matrix(cols).T
        ker = Mx.shape[1] - Mx.rank()
        for c in range(n):                                        # pure gauge l (x) zeta + zeta (x) l
            zeta = sp.zeros(n, 1); zeta[c] = 1
            kg = l*zeta.T + zeta*l.T
            gauge.append([kg[a, b] for (a, b) in basis])
        G = sp.Matrix(gauge).T
        in_ker = (Mx*G).is_zero_matrix
        dims[n] = (ker, G.rank(), in_ker)
    out["kernel"] = dims
    # fast diffeomorphism: xi = lam^2 Xi(v/lam, v, r, th); the O(lam) part of L_xi h
    v, r2, th2, tau, lam = sp.symbols("v r2 th2 tau lam")
    X3 = [v, r2, th2]
    hb = sp.Matrix(3, 3, lambda i, j: sp.Function("h%d%d" % (min(i, j), max(i, j)))(v, r2, th2))
    Xi = [sp.Function("Xi%d" % c)(tau, v, r2, th2) for c in range(3)]

    def dd(f, a):                                                 # d/dx^a with v -> (1/lam) d_tau + d_v
        return sp.diff(f, X3[a]) + (sp.diff(f, tau)/lam if a == 0 else 0)
    xi = [lam**2*Xi[c] for c in range(3)]
    L = sp.Matrix(3, 3, lambda a, b: sum(xi[c]*dd(hb[a, b], c) + hb[c, b]*dd(xi[c], a) + hb[a, c]*dd(xi[c], b)
                                         for c in range(3)))
    L1 = L.applyfunc(lambda e: sp.expand(e).coeff(lam, 1))
    l = sp.Matrix([1, 0, 0])
    hX = hb*sp.Matrix([sp.diff(Xi[c], tau) for c in range(3)])
    out["fast"] = (L1 - (l*hX.T + hX*l.T)).applyfunc(sp.simplify).is_zero_matrix
    out["fast_lam0"] = L.applyfunc(lambda e: sp.expand(e).coeff(lam, 0)).is_zero_matrix
    return out


def k3_background():
    """the torus frame on Tangherlini solves R[h] = (3/2)dpsi^2 + 2 domega^2 exactly; h_vr's first-order response"""
    v, r, th, e, mu = sp.symbols("v r theta e mu", positive=True)
    X = [v, r, th]
    s, c = sp.sin(th), sp.cos(th)
    rho = r**2*s*c
    Fm = 1 - mu/r**2
    hb = rho**2*sp.Matrix([[-Fm, 1, 0], [1, 0, 0], [0, 0, r**2]])
    _, _, R = _ricci(hb, X)
    psi = sp.log(rho); om = sp.log(c/s)/2
    src = lambda j, k: sp.Rational(3, 2)*sp.diff(psi, X[j])*sp.diff(psi, X[k]) + 2*sp.diff(om, X[j])*sp.diff(om, X[k])
    bg = [sp.simplify(R[j, k] - src(j, k)) for j in range(3) for k in range(j, 3)]
    # first order rr equation: 6 b_r/r - 24 b/r^2 ... solved by b = 2 dpsi h_vr (checked directly)
    dps = sp.Function("dps")(v, r, th)
    hvr = r**4*s**2*c**2
    b = 2*dps*hvr if "wrong_hvr" not in MUT else dps*hvr
    dh = sp.Matrix([[0, b, 0], [b, 0, 0], [0, 0, 0]])
    h = hb + e*dh
    gi = h.inv().applyfunc(lambda x: sp.series(x, e, 0, 2).removeO())
    n = 3
    G = [[[sp.expand(sp.series(sum(gi[i, d]*(sp.diff(h[d, j], X[k]) + sp.diff(h[d, k], X[j]) - sp.diff(h[j, k], X[d]))
                                   for d in range(n))/2, e, 0, 2).removeO()) for k in range(n)] for j in range(n)]
         for i in range(n)]
    Rrr = 0
    for i in range(n):
        Rrr += sp.diff(G[i][1][1], X[i]) - sp.diff(G[i][1][i], X[1])
        for d in range(n):
            Rrr += G[i][i][d]*G[d][1][1] - G[i][1][d]*G[d][1][i]
    lin = sp.expand(Rrr).coeff(e, 1) - sp.Rational(3, 2)*2*sp.diff(psi, r)*sp.diff(dps, r)
    return dict(bg=bg, hvr=sp.simplify(lin))


def k4():
    """T_h^(va) has no f_v for a Bondi-form h"""
    v, r, th = sp.symbols("v r theta")
    b, W, U, R2 = [sp.Function(n)(v, r, th) for n in ("b", "W", "U", "R2")]
    h = sp.Matrix([[-sp.exp(2*b)*W + R2*U**2, sp.exp(2*b), -R2*U], [sp.exp(2*b), 0, 0], [-R2*U, 0, R2]])
    if "rr_nonzero" in MUT:
        h[1, 1] = sp.Function("q")(v, r, th)
    hi = sp.simplify(h.inv())
    fv, fr, ft = sp.symbols("f_v f_r f_t")
    df = [fv, fr, ft]
    gr = sum(hi[a, c]*df[a]*df[c] for a in range(3) for c in range(3))
    T = sp.Matrix(3, 3, lambda a, c: df[a]*df[c] - sp.Rational(1, 2)*h[a, c]*gr)
    Tu = (hi*T*hi).applyfunc(sp.expand)
    return [sp.simplify(sp.diff(Tu[0, a], fv)) for a in range(3)]


def k5():
    """N2: Kodama sign; the multiplier's bulk (exact root counts); the shell's eps; the constants"""
    v, r, th, p1, p2 = sp.symbols("v r theta phi1 phi2", real=True)
    z, eps = sp.symbols("z epsilon", positive=True)
    X = [v, r, th, p1, p2]
    mu = sp.Function("mu")(v)
    Fm = 1 - mu/r**2
    g = sp.zeros(5); g[0, 0] = -Fm; g[0, 1] = g[1, 0] = 1; g[2, 2] = r**2
    g[3, 3] = r**2*sp.cos(th)**2; g[4, 4] = r**2*sp.sin(th)**2
    gi = sp.simplify(g.inv())
    fv, fr, ft = sp.symbols("f_v f_r f_t", real=True)
    df = [fv, fr, ft, 0, 0]
    gr = sum(gi[a, c]*df[a]*df[c] for a in range(5) for c in range(5))
    T = sp.Matrix(5, 5, lambda a, c: df[a]*df[c] - sp.Rational(1, 2)*g[a, c]*gr)
    Tu = gi*T*gi
    m, mp = sp.Symbol("m", positive=True), sp.Symbol("mp", real=True)

    def bulk(Xv):
        pi = sp.Matrix(5, 5, lambda a, c: sum(Xv[e]*sp.diff(g[a, c], X[e]) + g[e, c]*sp.diff(Xv[e], X[a])
                                              + g[a, e]*sp.diff(Xv[e], X[c]) for e in range(5)))
        K = sp.Rational(1, 2)*sum(Tu[a, c]*pi[a, c] for a in range(5) for c in range(5))
        return K.subs(sp.Derivative(mu, v), mp).subs(mu, m)
    out = {}
    kod = sp.expand(sp.simplify(bulk([1, 0, 0, 0, 0])))
    out["kodama"] = sp.simplify(kod - mp*fr**2/(2*r**2))
    if "kodama_sign" in MUT:
        out["kodama"] = sp.simplify(kod + mp*fr**2/(2*r**2))
    Z = sp.Symbol("Z", positive=True)
    alz = 12*Z**4 - 4*Z**6 + sp.Rational(3, 8)*Z**8
    sgz = Z**2*(4 - Z**2)**2
    if "sigma_off_at_horizon" in MUT:
        sgz = Z**2*(1 - Z**2)**2
    zz = r/sp.sqrt(mu)
    K = bulk([alz.subs(Z, zz), -sgz.subs(Z, zz), 0, 0, 0])
    K = sp.expand(sp.simplify(K.subs({r: z*sp.sqrt(m)}).subs(mp, eps*sp.sqrt(m))*sp.sqrt(m)).subs(m, 1))
    P = sp.Poly(K, fv, fr, ft)
    C = {mo: sp.factor(cf) for mo, cf in zip(P.monoms(), P.coeffs())}
    qvv, qvr, qrr, qtt = C.get((2, 0, 0), 0), C.get((1, 1, 0), 0), C.get((0, 2, 0), 0), C.get((0, 0, 2), 0)
    al, sg = alz.subs(Z, z), sgz.subs(Z, z)
    Fz = 1 - 1/z**2
    tl = sp.factor(al*Fz + 2*sg)
    det = sp.factor(sp.together(4*qvv*qrr - qvr**2))
    out["forms"] = dict(qvv=qvv, qvr=qvr, qrr=qrr, qtt=qtt, tl=tl, det=det)
    # exact root counts
    tln = sp.Poly(sp.expand(sp.cancel(tl/z**2)), z)
    out["timelike"] = (tln.count_roots(0, 2) == 0 and tln.eval(0) > 0)
    qvvn = sp.Poly(sp.expand(sp.cancel(qvv/z**3)), z)
    out["qvv"] = (qvvn.count_roots(0, sp.Rational(199, 100)) == 0 and qvvn.eval(0) > 0)
    Dz = sp.cancel(det/(sp.Rational(3, 4)*z**2*(z - 2)**2*(z + 2)**2))
    dres = [] if not sp.fraction(Dz)[1].has(z) else [(False, False)]  # det carries q_vv's factor z^2 (z^2 - 4)^2
    for E in ((0, EPS_STAR) if not dres else ()):
        Dp = sp.Poly(sp.expand(Dz.subs(eps, E)), z)
        roots = [x for x in Dp.real_roots() if 0 <= x < 2]
        dres.append((len(roots) == 0, Dp.eval(0) > 0))
    out["det"] = all(a and b for a, b in dres)
    qtn = []
    for E in (0, EPS_STAR):
        qq = sp.cancel(qtt.subs(eps, E)*4*z/(4 - z**2))
        if sp.fraction(qq)[1].has(z):                                # q_thth carries the factor (z^2 - 4)
            qtn.append(0.0); continue
        qp = sp.Poly(sp.expand(qq), z)
        qtn.append(min([float(x) for x in qp.real_roots() if 0 < x < 2] or [9]))
    out["qtt_zero"] = qtn                                         # first zero of the angular coefficient
    out["qtt_pos"] = (abs(qtn[0] - float(sp.sqrt(sp.Rational(12, 7)))) < 1e-9 and qtn[1] > qtn[0])
    # constants (computed on fine grids from the exact forms)
    err = sg + al*Fz/2; eth = al/(2*z**2)
    f = sp.lambdify(z, [sp.cancel(Dz.subs(eps, 0)/(16*z)), err, qtt.subs(eps, 0), eth], "numpy")
    Zg = np.linspace(1e-3, Z_G, 200001); a, b_, c, d = f(Zg)
    out["b"] = float(min((a/b_).min(), (c/d).min()))
    Z2 = np.linspace(Z_G, 2, 200001); a, b_, c, d = f(Z2); F2 = 1 - 1/Z2**2
    out["B"] = float(np.max(2*Z2**2*np.maximum(-c, 0)))
    out["C1"] = float(max((b_/(F2/2)).max(), (2*Z2**2*d).max()))
    Z4 = np.linspace(1.0001, 2, 200001); a, b_, c, d = f(Z4); F4 = 1 - 1/Z4**2
    out["c1"] = float(min((b_/(F4/2)).min(), (2*Z4**2*d).min(), 32.0))
    out["C2"] = 1 + (out["B"]/out["b"] + out["C1"])/out["c1"]
    out["e_rr"] = sp.factor(err)
    # the shell's growth rate eps = mu'/sqrt(mu), our universe's values
    A5 = _load("hf_anchor5.py", "kn_hf_anchor5")
    R = A5.a1()
    rh, Dd, seed = R["rh_l5"], R["D"], R["seed"]
    mu0 = seed/rh**2; dmu = 1 - mu0
    s = np.linspace(0, 1, 400001); env = np.sin(np.pi*s)**4
    mup = dmu*env**2/((35/128)*Dd)
    muv = mu0 + np.concatenate([[0], np.cumsum((mup[1:] + mup[:-1])/2*np.diff(s*Dd))])
    out["eps_max"] = float(np.max(mup/np.sqrt(muv)))
    zq = (np.sqrt(72)*rh**2)**0.25/rh
    out["zq"] = zq
    out["w_energy"] = float(err.subs(z, 1)/err.subs(z, zq))
    out["w_amp"] = float(np.sqrt(out["w_energy"]))
    out["Ap_max"] = float(np.max(np.sqrt(9*dmu/(2*Dd*(35/128)))*env/muv**0.25))
    return out


_K5F = {}


def k5_forms():
    if not _K5F:
        _K5F.update(k5()["forms"])
    return _K5F


def _lin_base():
    """first-order base equations of the torus frame about Tangherlini, the oscillation in the v-row (exact)"""
    v, r, th, e, mu = sp.symbols("v r theta e mu", positive=True)
    X = [v, r, th]
    sn, cs = sp.sin(th), sp.cos(th)
    rho = r**2*sn*cs
    Fm = 1 - mu/r**2
    a, b, cc, dps, dom = [sp.Function(n)(v, r, th) for n in ("a", "b", "cc", "dps", "dom")]
    hb = rho**2*sp.Matrix([[-Fm, 1, 0], [1, 0, 0], [0, 0, r**2]])
    dh = sp.Matrix([[a, b, cc], [b, 0, 0], [cc, 0, 0]])
    h = hb + e*dh
    gi = h.inv().applyfunc(lambda x: sp.series(x, e, 0, 2).removeO())
    n = 3
    G = [[[sp.expand(sp.series(sum(gi[i, d]*(sp.diff(h[d, j], X[k]) + sp.diff(h[d, k], X[j]) - sp.diff(h[j, k], X[d]))
                                   for d in range(n))/2, e, 0, 2).removeO()) for k in range(n)] for j in range(n)]
         for i in range(n)]

    def Ric(j, k):
        ex = 0
        for i in range(n):
            ex += sp.diff(G[i][j][k], X[i]) - sp.diff(G[i][j][i], X[k])
            for d in range(n):
                ex += G[i][i][d]*G[d][j][k] - G[i][k][d]*G[d][j][i]
        return sp.expand(ex)
    psib = sp.log(rho); omb = sp.log(cs/sn)/2
    ps, om = psib + e*dps, omb + e*dom
    src = lambda j, k: sp.expand(sp.Rational(3, 2)*sp.diff(ps, X[j])*sp.diff(ps, X[k]) + 2*sp.diff(om, X[j])*sp.diff(om, X[k]))
    out = {}
    for jk in [(1, 2), (2, 2), (0, 1), (0, 2)]:
        out[jk] = sp.simplify(Ric(*jk).coeff(e, 1) - src(*jk).coeff(e, 1))
    return out, (v, r, th, mu, a, b, cc, dps, dom)


def _rsplit(ex, r):
    """a sum of powers of r with r-free coefficients: {exponent: coefficient}.  Each term is split structurally --
    common factors pulled out of any sum that carries r -- and a term that is not a power of r times an r-free factor
    raises"""
    def split(f):
        e_, c = 0, 1
        for base, ex_ in f.as_powers_dict().items():
            if base == r:
                e_ += ex_
            elif not base.has(r):
                c *= base**ex_
            elif base.is_Add:
                b2 = sp.factor_terms(base)
                if b2 == base:
                    raise ValueError("not a power of r: %s" % base)
                e2, c2 = split(b2)
                e_ += e2*ex_; c *= c2**ex_
            elif base.is_Mul or base.is_Pow:
                e2, c2 = split(sp.expand_power_base(base, force=True))
                e_ += e2*ex_; c *= c2**ex_
            else:
                raise ValueError("not a power of r: %s" % base)
        return e_, c
    d = {}
    for t in sp.Add.make_args(sp.expand(ex)):
        e_, c = split(t)
        d.setdefault(e_, []).append(c)
    return {e_: sp.Add(*cs) for e_, cs in d.items()}


_K8CORE = {}
K8DATA = os.path.join(HERE, "data", "kn_gauge_k8.json")


def _k8_hash():
    """the core's own source (with what it calls): a cached core is used only if this is unchanged"""
    import hashlib
    import inspect
    src = "".join(inspect.getsource(f) for f in (_lin_base, _rsplit, _k8_core, k5))
    return hashlib.md5(src.encode()).hexdigest()


def build_k8():
    """compute the core (about three minutes) and store it with the hash of the code that produced it"""
    import json
    core = _k8_core()
    out = dict(core, lam_in=[float(x) for x in core["lam_in"]], Zi=[float(x) for x in core["Zi"]],
               kap_ext=float(core["kap_ext"]), drives=[list(d) for d in core["drives"]], hash=_k8_hash())
    os.makedirs(os.path.dirname(K8DATA), exist_ok=True)
    json.dump(out, open(K8DATA, "w"), indent=1)
    return out


def k8():
    """N3/N5 over the record's shell.  The core (the exact first-order response and its ratio to X's bulk) is read
    from data/kn_gauge_k8.json when the code that wrote it is unchanged (python3 kn_gauge.py --build-k8 rebuilds it),
    and recomputed otherwise; the mutant that alters it recomputes it"""
    import json
    if "drop_dh_vv" in MUT:
        return _k8_shell(_k8_core())
    if not _K8CORE:
        d = json.load(open(K8DATA)) if os.path.exists(K8DATA) else {}
        if d.get("hash") != _k8_hash():
            d = build_k8()
        d = dict(d, lam_in=np.array(d["lam_in"]), Zi=np.array(d["Zi"]))
        _K8CORE.update(d)
    return _k8_shell(_K8CORE)


def _k8_core():
    """the first-order oscillation of h (exact linear response) and its largest ratio to X's positive bulk"""
    L, (v, r, th, mu, a, b, cc, dps, dom) = _lin_base()
    Phi = sp.Function("Phi")(v); p1, p2 = sp.Function("p1")(th), sp.Function("p2")(th)
    Kf, Mf = sp.Function("K")(v, th), sp.Function("M")(v, th)
    k = sp.Rational(-3, 2)
    sn, cs = sp.sin(th), sp.cos(th)
    hvr = r**4*sn**2*cs**2
    cpf = sp.Function("cp")(th)
    Ert = sp.numer(sp.together(L[(1, 2)].subs({dps: p1*Phi*r**k, dom: p2*Phi*r**k, b: 2*p1*Phi*r**k*hvr,
                                                  cc: cpf*Phi*r**sp.Rational(7, 2)}).doit()))
    cp = sp.simplify(sp.solve(sp.expand(sp.simplify(Ert/Phi)), cpf)[0])
    Af = sp.Function("A")(v, r, th)
    # cp stays an undefined function of theta through the expansions (its trigonometric form multiplies their cost
    # many hundredfold) and is put in only where a number is evaluated
    sub0 = {dps: p1*Phi*r**k, dom: p2*Phi*r**k, b: 2*p1*Phi*r**k*hvr, cc: Phi*cpf*r**sp.Rational(7, 2) + Kf*r**2, a: Af}
    E = sp.expand(sp.numer(sp.together(L[(2, 2)].subs(sub0).doit())))
    cAr = E.coeff(sp.Derivative(Af, r)); E0 = sp.expand(E.subs(sp.Derivative(Af, r), 0))
    cA = E0.coeff(Af); rest = sp.expand(E0.subs(Af, 0))
    P = sp.simplify(cA/cAr)
    Q = sp.expand(sp.simplify(-rest/cAr))
    Ip = 0
    for e_, cf in _rsplit(Q, r).items():
        m = e_ - 2
        Ip += cf*(sp.log(r) if m == -1 else r**(m + 1)/(m + 1))
    Apart = sp.expand(r**2*Ip)
    ode_res = sp.expand(sp.diff(Apart, r) + P*Apart - Q)
    sub = dict(sub0); sub[a] = Apart + Mf*r**2
    sup = {}
    for jk in [(0, 2), (0, 1)]:
        sup[jk] = _rsplit(sp.expand(sp.numer(sp.together(L[jk].subs(sub).doit()))), r)
    hx = sp.sqrt(2/(1 + sp.cos(2*th)**2))
    pol = {"F": (sn**2*hx/3, -sn**2*hx/2), "G": (cs**2*hx/3, cs**2*hx/2)}
    # leading supplementary constraints: the coefficient of Phi' vanishes on the record's profiles
    lead = []
    for jk in sup:
        for pw, cf in sup[jk].items():
            cph = sp.expand(cf).coeff(sp.Derivative(Phi, v))
            if cph != 0:
                for pn, (P1, P2) in pol.items():
                    val = cph.subs(cpf, cp).doit().subs({p1: P1, p2: P2}).doit()
                    lead += [abs(float(sp.N(val.subs(th, sp.Rational(t).limit_denominator(1000)), 100))) for t in (0.3, 0.7, 1.1)]
    drives = [jk for jk in sup for pw, cf in sup[jk].items() if cf.has(sp.Derivative(Mf, v))]
    P1F, P2F = pol["F"]
    ode = abs(float(sp.N(ode_res.subs(cpf, cp).doit().subs({p1: P1F, p2: P2F, Kf: sn*v}).doit().subs({Phi: 1, mu: 1}).doit()
                         .subs({r: sp.Rational(3, 2), th: sp.Rational(7, 10), v: 1}), 60)))
    # the error form err = (1/2) rho^-2 T5^ab d_v dh_ab per unit alpha Phi', in units sqrt(mu) = 1
    import mpmath as mpm
    mpm.mp.dps = 160
    fr, ft = sp.symbols("f_r f_t", real=True)
    Fm = 1 - 1/r**2; rhob = r**2*sn*cs
    A0 = (Apart.subs(Kf, 0).doit()/Phi).subs(mu, 1)
    if "drop_dh_vv" in MUT:
        A0 = 2*p1*r**k*(-rhob**2*Fm)
    err = sp.expand(sp.Rational(1, 2)*rhob**(-2)*(fr**2*A0 + 2*(Fm*fr**2/2 - ft**2/(2*r**2))*2*p1*r**k*rhob**2
                                                  + 2*fr*ft/r**2*cpf*r**sp.Rational(7, 2)))
    comps = [_rsplit(c_, r) for c_ in (err.coeff(fr, 2).subs(ft, 0), err.coeff(fr, 1).coeff(ft, 1),
                                       err.coeff(ft, 2).subs(fr, 0))]
    TH = np.linspace(0.03, np.pi/2 - 0.03, 25)
    # each component is a sum of powers of r with coefficients in theta: those coefficients at the 25 angles, once
    Ef = {}
    for pn, (P1, P2) in pol.items():
        rep = {p1: P1, p2: P2}
        Ef[pn] = [[(mpm.mpf(int(sp.Rational(e_).p))/int(sp.Rational(e_).q),
                    [sp.lambdify(th, cf.subs(cpf, cp).doit().subs(rep).doit(), "mpmath")(mpm.mpf(t)) for t in TH])
                   for e_, cf in d.items()] for d in comps]
    z, eps = sp.symbols("z epsilon", positive=True)
    al = 12*z**4 - 4*z**6 + sp.Rational(3, 8)*z**8
    f5 = k5_forms()
    Dq = sp.lambdify(z, sp.cancel(f5["det"].subs(eps, 0)/(4*f5["qvv"])), "mpmath")
    qt = sp.lambdify(z, f5["qtt"].subs(eps, 0), "mpmath")
    alf = sp.lambdify(z, al, "mpmath")
    PH = np.linspace(0, 2*np.pi, 49)

    def gen(zz, coef):
        w_ = 0
        Zm = mpm.mpf(zz)
        for i in range(len(TH)):
            eF, eG = [np.array([float(sum(Zm**ex*vals[i] for ex, vals in cmp)) for cmp in Ef[pn]]) for pn in ("F", "G")]
            e_ = coef*(np.cos(PH)[:, None]*eF[None, :] - np.sin(PH)[:, None]*eG[None, :])
            aa, bb = (float(Dq(zz)), float(qt(zz))) if coef != 1 else (0.5*(1 - 1/zz**2), 0.5/zz**2)
            Pp = np.abs(e_[:, 0])/aa; Ss = np.abs(e_[:, 2])/bb; Qn = np.abs(e_[:, 1])/(2*np.sqrt(aa*bb))
            w_ = max(w_, ((Pp + Ss)/2 + np.sqrt(((Pp - Ss)/2)**2 + Qn**2)).max())
        return w_
    Zi = np.linspace(0.01, Z_G, 40)
    lam_in = np.array([gen(zz, float(alf(zz))) for zz in Zi])
    kap_ext = gen(Z_G, 1)                                        # against the T-energy, at z = 1.2 (its largest)
    return dict(ode=ode, lead=max(lead) if lead else 0.0, n_lead=len(lead), drives=drives, lam_in=lam_in, Zi=Zi,
                kap_ext=kap_ext)


def _k8_shell(core, w=None):
    """over the record's shell with our universe's values: where the oscillation is absorbed, removed, or left open
    (w the wavelength in l5, the record's 10 by default; item 520 scans it)"""
    Zi, lam_in, kap_ext = core["Zi"], core["lam_in"], core["kap_ext"]
    A5 = _load("hf_anchor5.py", "kn8_hf_anchor5")
    R = A5.a1()
    rh, Dd, seed = R["rh_l5"], R["D"], R["seed"]
    mu0 = seed/rh**2; dmu = 1 - mu0
    s = np.linspace(0, 1, 200001); env = np.sin(np.pi*s)**4
    mup = dmu*env**2/((35/128)*Dd)
    muv = mu0 + np.concatenate([[0], np.cumsum((mup[1:] + mup[:-1])/2*np.diff(s*Dd))])
    Ap = np.sqrt(9*dmu/(2*Dd*(35/128)))*env/muv**0.25
    w = w if w is not None else (20.0 if "w20" in MUT else 10.0)
    zhf = np.sqrt(10*w*72**0.25/(np.sqrt(muv)*rh))
    ratio = Ap*np.interp(np.minimum(zhf, Z_G), Zi, lam_in)
    seedph = zhf > Z_G
    f = kap_ext*Ap/np.sqrt(muv)
    strain = (2/3)*(w/(2*np.pi)/rh)*Ap/np.sqrt(muv)/Z_G**1.5
    late = np.trapezoid(np.where(~seedph, f*(1 if "no_averaging" in MUT else strain), 0), s*Dd)
    sp_ = seedph.any()
    return dict(core, ratio=float(ratio.max()), s_ratio=float(s[ratio.argmax()]),
                seed_s=float(s[seedph].max()) if sp_ else 0.0,
                seed_sqrtmu=float(np.sqrt(muv[seedph].max())*rh) if sp_ else 0.0,
                seed_energy=float(mup[seedph].sum()/mup.sum()),
                seed_crude=float(np.trapezoid(np.where(seedph, f, 0), s*Dd)), late=float(late),
                late_strain=float(strain[~seedph].max()), crude_all=float(np.trapezoid(f, s*Dd)), w=w)


def compute():
    o5 = k5(); _K5F.clear(); _K5F.update(o5["forms"])
    return dict(words=words(), k12=k1_k2(), k3=k3(), k3b=k3_background(), k4=k4(), k5=o5, k8=k8())


def checks(o):
    ch = {}
    ch["K0 words of 517 and 518"] = o["words"]
    k = o["k12"]
    ch["K1 reduction: R_(phi phi) = -e^(2U) box_5 U, R_(a phi) = 0, R_ab = R3_ab - sum(DDU + dUdU) (general base)"] = (
        all(x == 0 for x in k["I1"]) and all(x == 0 for x in k["I2"]))
    ch["K1 torus frame: R[h] = R + sum dUdU + dpsi dpsi + g3 sum e^-2U R_(phi phi), off shell"] = all(x == 0 for x in k["I3"])
    ch["K2 box_h = rho^-2 box_5; div_5 J = rho^2 ((1/2) T_h.L_X h + (Xf) box_h f): the radiation never enters"] = (
        k["I4"] == 0 and k["I5"] == 0)
    q = o["k3"]
    ch["K3 the record's Bondi gauge is the KN gauge: h_thth = r^6 s^2 c^2 for all P1, P2"] = q["hthth"] == 0
    kd = q["kernel"]
    ch["K3 symbol kernel: 3 = gauge only in 2+1; 6 = 4 + 2 in 3+1; 10 = 5 + 5 in 4+1"] = (
        kd[3] == (3, 3, True) and kd[4][0] == 6 and kd[5][0] == 10 and all(kd[n][2] and kd[n][1] == n for n in kd))
    ch["K3 the fast diffeomorphism adds lam (l (x) h.Xi' + h.Xi' (x) l) + O(lam^2): h's oscillation removed"] = (
        q["fast"] and q["fast_lam0"])
    b3 = o["k3b"]
    ch["K3 background: torus frame on Tangherlini exact; first-order h_vr response = 2 dpsi h_vr exact"] = (
        all(x == 0 for x in b3["bg"]) and b3["hvr"] == 0)
    ch["K4 T_h^(va) contains no f_v: the oscillation meets only the cone-tangential derivatives"] = all(
        x == 0 for x in o["k4"])
    m = o["k5"]
    ch["K5a Kodama: bulk of d_v is (mu'/2r^2) f_r^2 >= 0"] = m["kodama"] == 0
    ch["K5b multiplier: timelike on (0, 2]; q_vv > 0; det > 0 on [0, 2) for eps in [0, 1/20]; angular part > 0 to "
       "sqrt(12/7)"] = m["timelike"] and m["qvv"] and m["det"] and m["qtt_pos"]
    ch["K5c the shell's largest growth rate eps = 0.0219 < 1/20"] = 0.0215 < m["eps_max"] < 0.0225 < float(EPS_STAR)
    ch["K5d uniform energy bound C2 = 1 + (B/b + C1)/c1 = 35.0 (b 0.0748, B 15.6, C1 76.3, c1 8.38)"] = (
        abs(m["b"] - 0.0748) < 5e-4 and abs(m["B"] - 15.6) < 0.05 and abs(m["C1"] - 76.3) < 0.1
        and abs(m["c1"] - 8.38) < 0.01 and abs(m["C2"] - 35.0) < 0.1)
    ch["K5e weight at x = 1: 2.2e4 in energy, 150 in amplitude"] = (
        2.2e4 < m["w_energy"] < 2.3e4 and 149 < m["w_amp"] < 152)
    q8 = o["k8"]
    ch["K8a the record's profiles satisfy the leading supplementary constraints; the aspects are not driven"] = (
        q8["ode"] < 1e-30 and q8["n_lead"] > 0 and q8["lead"] < 1e-12 and not q8["drives"])
    ch["K8b first-order oscillation absorbed by X's bulk below min(z_hf, 1.2) over the whole shell: ratio 0.92 < 1"] = (
        0.85 < q8["ratio"] < 1)
    ch["K8c after the seed phase, averaged, second order: exponent 0.21 (estimate; crude would be 1.39e4 in all)"] = (
        q8["late"] < 0.3 and q8["crude_all"] > 1e4)
    ch["K8d the seed phase (hole under 20 wavelengths, 7.7e-6 of the energy) stays open: crude exponent 1.2e4"] = (
        abs(q8["seed_s"] - 0.1096) < 1e-3 and q8["seed_energy"] < 1e-5 and q8["seed_crude"] > 1e4)
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-112s %s" % (k_, "PASS" if v_ else "FAIL"))
    q = o["k3"]
    print("  K3 kernel dims (n: kernel, gauge rank, gauge in kernel): %s" % q["kernel"])
    m = o["k5"]
    f = m["forms"]
    print("  K5 q_vv = q_vr = %s; q_rr = %s; q_thth = %s" % (f["qvv"], f["qrr"], f["qtt"]))
    print("     timelike: %s; det = %s" % (f["tl"], f["det"]))
    print("     angular coefficient first zero at z = %.5f (eps 0), %.5f (eps 1/20); e_rr = %s" % (
        m["qtt_zero"][0], m["qtt_zero"][1], m["e_rr"]))
    print("     eps_max %.4f; A env mu^-1/4 max %.3f; b %.4f, B %.2f, C1 %.2f, c1 %.3f -> C2 %.2f; z_q %.5f, "
          "weight %.3g (energy), %.1f (amplitude)" % (m["eps_max"], m["Ap_max"], m["b"], m["B"], m["C1"], m["c1"],
                                                       m["C2"], m["zq"], m["w_energy"], m["w_amp"]))
    q8 = o["k8"]
    print("  K8 lapse response's ODE residual %.1e; leading constraints max |coef| %.2e over %d samples; aspects driven by: %s" % (
        q8["ode"], q8["lead"], q8["n_lead"], q8["drives"]))
    print("     lambda(z) per unit A env mu^-1/4: %s" % "; ".join("%.2f: %.3g" % (zz, l) for zz, l in
                                                                  zip(q8["Zi"][::10], q8["lam_in"][::10])))
    print("     absorption ratio max %.3f at s = %.3f; kappa_ext %.2f; seed phase s < %.4f (sqrt mu < %.0f l5), energy %.2e, "
          "crude exponent %.4g; late averaged exponent %.3f (max strain %.2e); crude over the shell %.4g" % (
              q8["ratio"], q8["s_ratio"], q8["kap_ext"], q8["seed_s"], q8["seed_sqrtmu"], q8["seed_energy"],
              q8["seed_crude"], q8["late"], q8["late_strain"], q8["crude_all"]))
    return o


MUTANTS = {"torus_sign": "R_(phi phi) = +e^(2U) box U (K1)",
           "no_rho2": "torus frame h = rho g3, not rho^2 g3 (K1)",
           "tt_in_3": "the symbol without its trace term (K3)",
           "wrong_hvr": "h_vr's response dpsi h_vr, not 2 dpsi h_vr (K3)",
           "rr_nonzero": "a Bondi-form h with h_rr != 0 (K4)",
           "kodama_sign": "Kodama bulk with the opposite sign (K5a)",
           "sigma_off_at_horizon": "sigma vanishing at the horizon (K5b)",
           "drop_dh_vv": "the lapse response replaced by its psi part alone (K8)",
           "w20": "20 l5 waves in place of the record's 10 l5 (K8b)",
           "no_averaging": "no averaging after the seed phase (K8c)"}


def selftest():
    o = compute(); c = checks(o); report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k[:44] for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-21s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--build-k8" in sys.argv:
        _K5F.update(k5()["forms"])
        o = build_k8()
        print("core stored, hash %s; lambda(1.2) %.3g; leading constraint %.1e; ODE residual %.1e" % (
            o["hash"], o["lam_in"][-1], o["lead"], o["ode"]))
        sys.exit(0)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
