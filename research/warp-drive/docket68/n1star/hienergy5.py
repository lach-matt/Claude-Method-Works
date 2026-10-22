#!/usr/bin/env python3
"""hienergy5.py -- the five-dimensional inputs of [Hin26c] Theorems 9.5 and 9.16 for the gauge potential operator on
Tangherlini: the threshold at the incoming radial set, the trapping hypotheses (Gamma.1)-(Gamma.4) with the loss
function delta_Gamma, and the global dynamics (N1STAR-PROOF.md section 10.19; ROUTES-OPEN.md 4.20; D62).  Labels:
computed (exact, sympy), deduced, READ.

[Hin26c] (arXiv:2606.28008v1) section 9 states its spectral theory for stationary asymptotically Minkowski wave
operators on R^n (Definition 9.4): P_0 = -2 d_t* rho (rho d_rho - (n - 1)/2 - S) + P_0-hat(0) + Q d_t* - g00 d_t*^2,
d_sigma P_0-hat(0) = 2i rho (rho d_rho - (n - 1)/2 - S) - iQ "symmetric with respect to the Euclidean volume density
r^(n-1) |dr dg|" at S = Q = 0 ((9.37)).  His estimates for the spectral family need: at the horizon s > 1/2 +
vartheta_H+ (10.18: 3/2); at R_in, r + alpha > (1/2)(-1 + vartheta_in), vartheta_in = sup over the boundary of the
b-symbol of Im P_0-hat(0) at -2 dr/r minus 2 Re S ((9.16b), (9.32)); at R_out, r + alpha < -1/2 + S-bar ((9.16c)); at
the trapped set, (Gamma.1)-(Gamma.4), with beta_0 = min g^-1(-dt + xi, dt), p_1 = sigma_h((P_h,1 - P_h,1^*)/2ih),
gamma_+ = sup p_1/(2 beta_0), gamma_- = gamma_+ - nu_min/(4 beta_0), and the loss delta_Gamma(eta) = max((gamma_+ -
eta)/(gamma_+ - gamma_-), 0) ((9.79)-(9.81)); near the interior hypersurface, dr future timelike (Proposition 9.35).
[Hin26] p. 119 records vartheta_in = vartheta_out = S-bar = 0 for the unmodified 1-form wave operator. S-bar is the
endomorphism in V1's identity and the number min Re spec of it in a threshold ((5.2); [Hin26] footnote 60).

  V1 (computed, exact) On 4+1 Minkowski: rho (rho d_rho - c) is skew for rho^(-n-1) d rho, n = 4, iff c = (n - 1)/2
     = 3/2 -- (Lu) v + u (Lv) = rho^(n+1) d_rho (rho^(1-n) u v); and for box^Ups at the weight 2/3 the first-order
     part of P_0-hat(0) at the incoming covector, A_w, satisfies A_w + S-bar = D S-bar D, D the reflection in the radial
     direction: spec (A_w + S-bar) = spec S-bar, his (6.11)'s, so vartheta_in = -2 S-bar (within eps, exactly when
     S-bar is diagonalisable) and the threshold at R_in is r + alpha > -1/2 - S-bar, the mirror of R_out's.  At gam =
     0 vartheta_in = 0, his p. 122's r > -1/2.  Four-dimensional control: the same at the weight 1.  Controls: the
     constant 1 in place of 3/2; the weight 1 in five dimensions, where spec (A_w + S-bar) is not his; the outgoing
     covector, where -A_w + S-bar is not similar to S-bar.
  V2 (computed, exact) (Gamma.1)-(Gamma.3) on Tangherlini for the semiclassical family at z = 1, G_1 = -1/f + f xi^2
     + C/r^2: Gamma = {r^2 = 2 mu, xi = 0, C = 4 mu}, its only point with r > r_h; on Sigma_1 the linearised flow in
     (r, xi) has eigenvalues +-nu, nu = 4 (2 mu)^(-1/2), with phi_s/u = xi +- (nu/(2 f)) (r - r_ph) as left
     eigenvectors (H phi_s = nu phi_s, H phi_u = -nu phi_u to first order) and {phi_u, phi_s} = nu/f > 0; dG_1 != 0
     there (d_C G_1 = 1/r^2); beta_0 = 1/f(r_ph) = 2, unchanged by t* = t - F(r); and the strip nu/(4 beta_0) =
     (8 mu)^(-1/2), half trap5.py T1's rate per unit t.  Four-dimensional control: r = 3 mu/2, beta_0 = 3, nu/(4
     beta_0) = 1/(3^(3/2) mu).  Control: the four-dimensional ratio r_ph = (3/2) r_h.
  V3 (computed, exact) (Gamma.4) and delta_Gamma: at a point of Gamma (sigma = 1, r^2 = 2 mu, C = 4 mu), nabla_{H_G}
     on trap5.py's frame is e_0 -> 0, e_1 -> -2 e_0, e_2 -> -2 e_1, with no V_perp part, and the angular covectors
     orthogonal to eta are carried into V_perp; with diag(1, eta^-1, eta^-2) on the span, p_1 = -(M + M^*)/2 has
     spectrum 0, +-(2 eta)^(1/2), so sup p_1 = (2 eta)^(1/2) and delta_Gamma(0) = 2 sup p_1/nu = (mu eta)^(1/2) -> 0.
     Four-dimensional control: the same spectrum, delta_Gamma(0) = (3 mu^2 eta/2)^(1/2).  Control: a connection that
     is not nilpotent (a diagonal entry -1), where sup p_1 does not tend to 0.
  V4 (computed, exact) The global dynamics and the interior: on Sigma_1, f^2 xi^2 = 1 - C W(r), W = f/r^2, and W' =
     2 (2 mu - r^2)/r^5 on r > r_h: one critical point, a maximum W = 1/(4 mu) at r^2 = 2 mu, W(r_h) = 0, W -> 0 at
     infinity; g^-1 is positive on ann(d_t) for r > r_h (no ergoregion); and in the ingoing chart g^-1(dr, dr) = f <
     0 on 0 < r < r_h with g^-1(dr) future directed.  Four-dimensional control: W' = (3 mu - 2 r)/r^4, maximum at r =
     3 mu/2.  Control: the four-dimensional ratio r_ph = (3/2) r_h.

Deduced, not computed here: with 10.18's vartheta_H+ = 1 and R_out threshold, every input of [Hin26c] Theorems 9.5
and 9.16 is computed in five dimensions, its section 9 stated for general n; so, on the reading that its proofs carry
over as their statements do, the spectral family of box^Ups is Fredholm of index 0 at bounded sigma != 0 with kernel
elements in A^(3/2 + S-bar - eps), and invertible for |sigma| >= C_0, Im sigma >= 0, with semiclassical loss
delta_Gamma(0) as small as wished: [Hin26] Proposition 6.5; with 10.16, his Proposition 6.9 for small E^Ups.

READ.  [Hin26c] pp. 81 (Definition 4.5), 98 (Proposition 4.24), 104-105 (Definition 5.11, Lemma 5.12), 158-159
(Definition 9.4, (9.4)-(9.6)), 161, 163 ((9.16a)-(9.16c), Theorem 9.5), 167-168 (Proposition 9.10, (9.32)-(9.42)),
174-175 (Theorem 9.16, Remarks 9.17-9.18), 178 (Proposition 9.25), 180 (Propositions 9.26-9.27), 182 ((Gamma.1)-
(Gamma.4), (9.79)-(9.81)), 191 (Proposition 9.35), 193 (the proof of Theorem 9.16); [Hin26] pp. 113, 116 (Lemma 6.4's
proof, Proposition 6.5), 118-119 (Lemma 6.8's proof, Proposition 6.9 and its proof), 121-122 (Proposition 6.12, the
orders of its proof), 200 (Remark 10.2); alphaXiv, 2026-10-22.

sympy.  python3 hienergy5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import gaugepot5 as G
import thresh5 as T
import trap5 as T5
from damping5 import Checklist

D = sp.diff
mu = G.mu
gam, e = T.gam, T.e


# ------------------------------------------------------------------------------------------------- V1
def v1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rho = sp.Symbol("rho", positive=True)
    u, v = sp.Function("u")(rho), sp.Function("v")(rho)
    n = 4
    c = sp.Rational(n - 1, 2) if control != 1 else 1
    L = lambda w: rho*(rho*D(w, rho) - c*w)
    chk(f"rho (rho d_rho - {c}) skew for rho^(-{n + 1}) d rho: (Lu) v + u (Lv) = rho^{n + 1} d_rho (rho^{1 - n} u v)",
        sp.simplify(L(u)*v + u*L(v) - rho**(n + 1)*D(rho**(1 - n)*u*v, rho)) == 0)
    if control == 1:
        return chk.ok
    for n in ((4,) if control else (4, 3)):
        w = sp.Rational(2, n - 1) if control != 2 else 1
        Mk = T.minkowski(n, w)
        P, W, Tt, x, r, N = Mk["P"], Mk["W"], Mk["T"], Mk["x"], Mk["r"], Mk["N"]
        sgn = -1 if control == 3 else 1
        A = sp.Matrix(N, N, lambda a, b: sgn*sum(P[a].coeff(D(W[b], x[i]))*x[i] for i in range(n)))
        S = sp.Matrix(N, N, lambda a, b: r/2*P[a].coeff(D(W[b], Tt)) - (sp.Rational(n - 1, 2) if a == b else 0))
        Dm = sp.diag(1, *([1]*n)) - 2*sp.diag(0, sp.Matrix(n, 1, lambda i, j: x[i]/r)*sp.Matrix(1, n, lambda i, j:
                                                                                                  x[j]/r))
        sim = all(T.exact0(q, x) for q in A + S - Dm*S*Dm)
        pt = {x[0]: 1, **{xi: 0 for xi in x[1:]}}
        ev = {sp.factor(a): m for a, m in (A + S).subs(pt).eigenvals().items()}
        want = {sp.factor(gam*(1 - e)): 1, 2*gam: 1, gam: n - 1}
        chk(f"n + 1 = {n + 1}: A_w + S-bar = D S-bar D (weight {w}), spec = gam (1 - e), 2 gam, gam: vartheta_in = "
            f"-2 S-bar, threshold -1/2 - S-bar at R_in", sim and ev == want)
        z0 = (A + S).subs(pt).subs(gam, 0)
        chk(f"n + 1 = {n + 1}: at gam = 0, A_w + S-bar = 0: vartheta_in = 0 (his p. 122)", z0 == sp.zeros(N, N))
    return chk.ok


# ------------------------------------------------------------------------------------------------- V2
def v2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    r, xi, Cc, F = sp.symbols("r xi C F", real=True)
    for n in ((4,) if control else (4, 3)):
        f = 1 - mu/r**2 if n == 4 else 1 - mu/r
        rh = sp.sqrt(mu) if n == 4 else mu
        rph = sp.sqrt(2*mu) if n == 4 else 3*mu/2
        if control == 1:
            rph = sp.Rational(3, 2)*sp.sqrt(mu)
        G1 = -1/f + f*xi**2 + Cc/r**2
        Cph = sp.simplify((r**2/f).subs(r, rph))
        crit = [sp.simplify(q.subs({xi: 0, Cc: Cph, r: rph})) for q in (G1, D(G1, r), D(G1, xi))]
        rts = [q for q in sp.solve(sp.numer(sp.together(D(G1, r).subs(Cc, r**2/f).subs(xi, 0))), r)
               if q.is_positive and sp.simplify(q - rh) != 0]
        Lrx = r**2*(1/f - f*xi**2)                                 # C on Sigma_1, conserved
        rd, xd = D(G1, xi), -D(G1, r).subs(Cc, Lrx)
        J = sp.Matrix([[D(rd, r), D(rd, xi)], [D(xd, r), D(xd, xi)]]).subs({xi: 0}).subs(r, rph).applyfunc(sp.simplify)
        nu = sp.sqrt(sp.simplify(J[0, 1]*J[1, 0]))
        fph = f.subs(r, rph)
        k = sp.simplify(nu/(2*fph))
        left = all(sp.simplify(q) == 0 for q in sp.Matrix([[k, 1]])*J - nu*sp.Matrix([[k, 1]])) and \
            all(sp.simplify(q) == 0 for q in sp.Matrix([[-k, 1]])*J + nu*sp.Matrix([[-k, 1]]))
        bracket = sp.simplify(1*k - (-k)*1)
        beta0 = sp.simplify((1/f).subs(r, rph))
        # t* = t - F(r): g^-1(zeta, dt*) = g^-1(zeta, dt) - F' g^rr zeta_r, zeta_r = xi = 0 on Gamma
        beta_star = sp.simplify((1/f - F*f*xi).subs(xi, 0).subs(r, rph))
        lam_t = 1/sp.sqrt(2*mu) if n == 4 else 2/(3*sp.sqrt(3)*mu)
        want = (4/sp.sqrt(2*mu), 2) if n == 4 else (6*lam_t, 3)
        chk(f"n + 1 = {n + 1}: Gamma = (r = {rph}, xi = 0, C = {Cph}), the only critical point in r > r_h; nu = {nu}, "
            f"phi_s/u left eigenvectors, {{phi_u, phi_s}} = {bracket} > 0, d_C G_1 = 1/r^2, beta_0 = {beta0}, strip "
            f"nu/(4 beta_0) = {sp.simplify(nu/(4*beta0))} = (T1's rate)/2",
            all(q == 0 for q in crit) and len(rts) == 1 and left and bracket.is_positive and
            sp.simplify(nu - want[0]) == 0 and beta0 == want[1] and sp.simplify(beta_star - beta0) == 0 and
            sp.simplify(nu/(4*beta0) - lam_t/2) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- V3
def v3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    eta = sp.Symbol("eta", positive=True)
    for n in ((4,) if control else (4, 3)):
        Pd = T5.phase(n)
        C = Pd["C"]
        X, z, N, r, f = C["X"], Pd["z"], C["N"], C["r"], C["f"]
        rph = sp.sqrt(2*mu) if n == 4 else 3*mu/2
        e0, e1, e2 = T5.frame(Pd)
        pt = {X[1]: rph, X[2]: sp.pi/4, **{a: 0 for a in X[3:]}} if n == 4 else {X[1]: rph, X[2]: sp.pi/2, X[3]: 0}
        zp = {z[0]: -1, z[1]: 0, z[2]: sp.sqrt(1/(f.subs(r, rph)*C["gi"][2, 2].subs(pt))),
              **{z[k]: 0 for k in range(3, N)}}

        def ev(vec):
            return [sp.simplify(sp.sympify(q).subs(pt).subs(zp)) for q in vec]

        perp = [[1 if k == j else 0 for k in range(N)] for j in range(3, N)]
        B = sp.Matrix([ev(e0), ev(e1), ev(e2)] + perp).T
        on = sp.simplify(Pd["Gf"].subs(pt).subs(zp)) == 0
        Cv = sp.simplify((r**2*sum(C["gi"][a, a]*z[a]**2 for a in range(2, N))).subs(pt).subs(zp))
        M = sp.zeros(N, N)
        for j, vec in enumerate([e0, e1, e2] + perp):
            M[:, j] = B.LUsolve(sp.Matrix(ev(Pd["nab"](vec)))).applyfunc(sp.simplify)
        if control == 1:
            M[1, 1] = -1
        span = M[:3, :3]
        blocks = M[3:, :3] == sp.zeros(N - 3, 3) and M[:3, 3:] == sp.zeros(3, N - 3)
        nil = span == sp.Matrix([[0, -2, 0], [0, 0, -2], [0, 0, 0]])
        H = sp.diag(1, 1/eta, 1/eta**2)
        p1 = -(span + H.inv()*span.T*H)/2
        spec = {sp.simplify(a): m for a, m in p1.eigenvals().items()}
        sup = max(spec, key=lambda a: a.subs(eta, sp.Rational(1, 100)))
        nu = 4/sp.sqrt(2*mu) if n == 4 else 4/(sp.sqrt(3)*mu)
        beta0 = 2 if n == 4 else 3
        gp = sup/(2*beta0)
        gm = gp - nu/(4*beta0)
        dG = sp.simplify(gp/(gp - gm))
        want = sp.sqrt(mu*eta) if n == 4 else sp.sqrt(3*mu**2*eta/2)
        chk(f"n + 1 = {n + 1}: at Gamma (C = {Cv}) nabla_(H_G): e_1 -> -2 e_0, e_2 -> -2 e_1, V_perp invariant; spec "
            f"p_1 = {sorted(spec, key=str)}, sup p_1 = {sup} -> 0, delta_Gamma(0) = {dG}",
            on and Cv == 4*mu*(1 if n == 4 else sp.Rational(27, 16)*mu) and blocks and nil and
            sp.simplify(sup - sp.sqrt(2*eta)) == 0 and sp.simplify(dG - want) == 0 and sp.limit(sup, eta, 0) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- V4
def v4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    r, xi, Cc = sp.symbols("r xi C", positive=True)
    for n in ((4,) if control else (4, 3)):
        f = 1 - mu/r**2 if n == 4 else 1 - mu/r
        rh = sp.sqrt(mu) if n == 4 else mu
        rph = sp.sqrt(2*mu) if n == 4 else 3*mu/2
        if control == 1:
            rph = sp.Rational(3, 2)*sp.sqrt(mu)
        Wf = f/r**2
        G1 = -1/f + f*xi**2 + Cc/r**2
        sig = sp.simplify(f*G1 - (f**2*xi**2 - 1 + Cc*Wf)) == 0
        Wp = sp.factor(D(Wf, r))
        want = 2*(2*mu - r**2)/r**5 if n == 4 else (3*mu - 2*r)/r**4
        crit = [q for q in sp.solve(sp.numer(Wp), r) if q.is_positive]
        top = sp.simplify(Wf.subs(r, rph))
        ends = sp.simplify(Wf.subs(r, rh)) == 0 and sp.limit(Wf, r, sp.oo) == 0
        maxi = sp.simplify(D(Wf, r, 2).subs(r, rph)) < 0 if sp.simplify(Wp.subs(r, rph)) == 0 else False
        Ci = G.ch(n, "ingoing")
        grr = sp.simplify(Ci["gi"][1, 1] - Ci["f"])
        inside = sp.simplify(Ci["f"].subs(Ci["r"], rh/2)) < 0 and sp.simplify(D(Ci["f"], Ci["r"])).subs(
            Ci["r"], rh/2).is_positive
        gtt = -f
        chk(f"n + 1 = {n + 1}: f^2 xi^2 = 1 - C W on Sigma_1; W' = {Wp}, one critical point, a maximum W = {top} at "
            f"r = {rph}, W(r_h) = 0, W -> 0; g_tt = -f < 0 off the horizon; g^-1(dr, dr) = f < 0 inside",
            sig and sp.simplify(Wp - want) == 0 and len(crit) == 1 and maxi and ends and grr == 0 and inside and
            sp.simplify(gtt.subs(r, 2*rh)) < 0)
    return chk.ok


CHECKS = [("V1 R_in on 4+1 Minkowski: A_w + S-bar = D S-bar D, vartheta_in = -2 S-bar, threshold -1/2 - S-bar",
           v1, 3),
          ("V2 (Gamma.1)-(Gamma.3) on Tangherlini: r^2 = 2 mu, nu = 4 (2 mu)^(-1/2), beta_0 = 2, strip (8 mu)^(-1/2)",
           v2, 1),
          ("V3 (Gamma.4): nilpotent connection at Gamma, sup p_1 = (2 eta)^(1/2), delta_Gamma(0) = (mu eta)^(1/2)", v3,
           1),
          ("V4 global dynamics: W = f/r^2 one maximum at r^2 = 2 mu, no ergoregion, dr timelike inside", v4, 1)]


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
    print(f"hienergy5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"hienergy5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
