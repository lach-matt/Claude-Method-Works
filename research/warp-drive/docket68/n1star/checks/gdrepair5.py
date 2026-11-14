#!/usr/bin/env python3
"""gdrepair5.py -- GAUGEDECAY5.md Round 2, section R2.V: the verifier's findings on round 1, computed.

Background and class as in rwgauge5.py / hgauge5.py (ingoing chart, s = sqrt(mu) = r_h, f = 1 - s^2/r^2).

  V1 (exact; limits at the horizon) The supplement's K* is singular at the horizon.  N1STAR-PROOF.md Proposition 10.2
     (iv) (READ, lines 1780-1782): K := dg/dmu of the static chart, K* := K + pi_{W**}, W** = t W* + A dt + B dr,
     A = (log f + mu/r^2)/(2 sqrt mu), B = (3 mu^2 log(r^2 - mu) + 2 mu^2 + 3 mu r^2 - 2 r^4 log r + r^4 log(r^2 - mu))
     /(8 mu r (r^2 - mu)).  Written in the ingoing chart (t = v - r_*, dt = dv - dr/f): Theta(K*_supp) = 0 (its W3
     holds), and at mu = 1, (r - 1) K*_vr and (r - 1)^2 K*_rr have the limits -3/8 and 3/8 as r -> 1+, while the
     horizon-regular K*_reg := dv^2/r^2 + L_{W**} g of GAUGEDECAY5 Proposition 2.1 (d) is finite there.  K*_supp -
     K*_reg - (v/2) L_{W*} g is stationary and singular.  Control: K*_reg's components times (r - 1) tend to 0.
  V2 (exact) The l = 0 sector of the harmonic gauge.  (a) K*_reg has Theta = 0, dmu[K*_reg] = 1, and K*_reg - (v/2)
     L_{W*} g is stationary and finite at r_h.  (b) Psi := (v + F)^2 + K, F = -r - s log(r/(r + s)), K' = (r^4/2 + r^2
     s^2 - 3 s^4/2 + 2 s^4 log(r/s))/(r (r^2 - s^2)) solves Box_0 Psi = 0 with d Psi finite at r_h, and S := K*_reg -
     (4 mu)^-1 L_{d Psi} g is stationary, finite at r_h, Theta(S) = 0, dmu[S] = 1, and S_vv -> -1/mu as r -> oo: a
     stationary horizon-regular harmonic-gauge mass change exists, but it is O(1) at infinity and its gauge vector
     grows in v and r.  Control: with (2 mu)^-1 in place of (4 mu)^-1, S is not stationary.
  V3 (exact) Round 1's H4, its r-component made exact: Box W** - dv/r^3 = 0 in every component after
     expand_log(force=True).  Control: the coefficient 1 in place of 1/2.
  V4 (exact) Controls that round 1's R3 (c)-(f), H2 (l = 2) and H3 (values) lacked, and a non-tautological one for
     R5; each "control" below is a claim that must fail.
     R3c: without the class restriction a smooth divergence-free 1-form exists (cos^2 th dphi1): "divergence-free
          1-forms are exact" fails off the class.
     R3d: a symmetric tensor with a (th, phi1) component (excluded by the reflections) has a phi1 divergence component.
     R3e: the norm identity with (k^2 - 2) in place of (k^2 - 3) fails at quadrature precision.
     R3f: with k^2 (k^2 - 2) in place of k^2 (k^2 - 3) the supremum is not 243/80.
     H2: Q of a general l = 0 class 1-form does not vanish (Q is not identically zero).
     H3: Q[W* + (d_v)^flat] = 4 pi^2 (1 + mu) != 4 pi^2, and ell([Box, v] (d_v)^flat) != 4 pi^2: the values
         discriminate.
     R5: for Y = (1 + v)^-q r d_r, L_Y g is not O(v^(-q-1)): the loss of one power is particular to d_v.
  V5 (exact) The static mass change of supplement Proposition 10.1 is K_static = dt^2/r^2 + dr^2/(r^2 f^2) = dv^2/r^2 +
     L_{zeta d_v} g with zeta' = 1/(r^2 f^2), which has a double pole at r_h: GAUGEDECAY5 Definition 1.1's gauge
     (l = 0 part c K, K of (0.1), horizon-regular) agrees with Proposition 10.1's at l >= 2 only.  Control: zeta' =
     1/(r^2 f).

Labels: computed (exact, sympy; R3e by quadrature at 40 digits).  Run: python3 checks/gdrepair5.py
"""
import sys

import mpmath
import sympy as sp

from rwgauge5 import N, SPH, X, dmu_formula, gam, gami, legendre_S, mu, r, s, sph_div_form, sph_div_tensor, sph_hess, \
    sph_lap, sqg, th, v, zero
from hgauge5 import A_EXPR, B_EXPR, GEO, S3, WSTAR, box, charge_density, delta1, dform, theta

f = 1 - mu/r**2
LOGR = sp.log((r - s)/(r + s))


def lie(w):
    return GEO.lie(w)


def comps(h):
    return [sp.simplify(h[0][0]), sp.simplify(h[0][1]), sp.simplify(h[1][1]), sp.simplify(h[2][2]/r**2)]


def add(h1, h2, c=1):
    return [[h1[a][b] + c*h2[a][b] for b in range(N)] for a in range(N)]


def kstar_reg():
    K = [[0]*N for _ in range(N)]
    K[0][0] = 1/r**2
    W = [v*WSTAR[0]/2 + A_EXPR, v*WSTAR[1]/2 + B_EXPR, 0, 0, 0]
    return add(K, lie(W))


def kstar_supp():
    """N1STAR-PROOF.md (10.2)-(iv) in the ingoing chart: K_static + L_{W**_s} g"""
    As = (sp.log(f) + mu/r**2)/(2*s)
    Bs = (3*mu**2*sp.log(r**2 - mu) + 2*mu**2 + 3*mu*r**2 - 2*r**4*sp.log(r) + r**4*sp.log(r**2 - mu)) / \
        (8*mu*r*(r**2 - mu))
    rstar = r + s*LOGR/2
    t = v - rstar
    K = [[0]*N for _ in range(N)]                                  # r^-2 dt^2 + r^-2 f^-2 dr^2, dt = dv - dr/f
    K[0][0] = 1/r**2
    K[0][1] = K[1][0] = -1/(r**2*f)
    K[1][1] = 2/(r**2*f**2)
    W = [t*WSTAR[0] + As, t*WSTAR[1] + Bs - As/f, 0, 0, 0]
    return add(K, lie(W))


def l0_dmu(h):
    return sp.simplify(dmu_formula(h[0][0], h[0][1], h[1][1], h[2][2]/(2*r**2)))


# --------------------------------------------------------------------------------------------------------------- V1
def v1(control=False):
    Kr = kstar_reg()
    if control:
        lims = [sp.limit(((r - 1)*e).subs(s, 1), r, 1, "+") for e in (Kr[0][1], Kr[1][1])]
        bad = any(x != 0 for x in lims)
        print("  V1 control: (r - 1) x K*_reg (vr, rr) -> %s at mu = 1; nonzero: %s" % (lims, bad), flush=True)
        return bad
    Ks = kstar_supp()
    th_ok = all(zero(sp.expand_log(sp.simplify(e), force=True)) for e in theta(GEO, Ks))
    vr = sp.limit(((r - 1)*Ks[0][1]).subs(s, 1), r, 1, "+")
    rr = sp.limit(((r - 1)**2*Ks[1][1]).subs(s, 1), r, 1, "+")
    reg = [sp.limit(e.subs({s: 1, v: sp.Rational(7, 3)}), r, 1, "+") for e in (Kr[0][0], Kr[0][1], Kr[1][1])]
    LW = lie(WSTAR)
    D = add(add(Ks, Kr, -1), LW, -v/2)
    stat = all(zero(sp.diff(D[a][b], v)) for a in range(N) for b in range(N))
    dsing = sp.limit(((r - 1)**2*D[1][1]).subs(s, 1), r, 1, "+")
    ok = th_ok and vr == sp.Rational(-3, 8) and rr == sp.Rational(3, 8) and all(x.is_finite for x in reg) and stat
    ok &= dsing != 0
    print("  V1: Theta(K*_supp) = 0: %s; at mu = 1: (r-1) K*_vr -> %s, (r-1)^2 K*_rr -> %s; K*_reg (vv, vr, rr) at r_h, "
          "v = 7/3: %s; K*_supp - K*_reg - (v/2) L_{W*} g stationary: %s, (r-1)^2 x its rr component -> %s"
          % (th_ok, vr, rr, reg, stat, dsing), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- V2
def v2(control=False):
    Kr = kstar_reg()
    F = -r - s*sp.log(r/(r + s))
    Fp = sp.diff(F, r)
    Kp = (r**4/2 + r**2*s**2 - sp.Rational(3, 2)*s**4 + 2*s**4*sp.log(r/s))/(r*(r**2 - s**2))
    dPsi = [2*(v + F), 2*(v + F)*Fp + Kp, 0, 0, 0]
    c = 1/(2*mu) if control else 1/(4*mu)
    S = add(Kr, lie(dPsi), -c)
    stat = all(zero(sp.diff(S[a][b], v)) for a in range(N) for b in range(N))
    if control:
        print("  V2 control ((2 mu)^-1): S stationary: %s" % stat, flush=True)
        return stat
    LW = lie(WSTAR)
    a_stat = all(zero(sp.diff(Kr[a][b] - v*LW[a][b]/2, v)) for a in range(N) for b in range(N))
    a_th = all(zero(sp.expand_log(e, force=True)) for e in theta(GEO, Kr))
    a_dmu = zero(sp.expand_log(l0_dmu(Kr) - 1, force=True))
    fp_ok = zero(Fp + (r**2 + r*s + s**2)/(r*(r + s)))
    box0 = zero(sp.expand_log(delta1(GEO, dPsi), force=True))
    dpsi_h = [sp.limit(e.subs({s: 1, v: 0}), r, 1, "+") for e in dPsi[:2]]
    s_th = all(zero(sp.expand_log(e, force=True)) for e in theta(GEO, S))
    s_dmu = zero(sp.expand_log(l0_dmu(S) - 1, force=True))
    s_h = [sp.limit(sp.expand_log(e, force=True).subs({s: 1, v: 0}), r, 1, "+") for e in comps(S)]
    s_inf = sp.limit(sp.expand_log(S[0][0], force=True).subs(v, 0), r, sp.oo)
    ok = a_stat and a_th and a_dmu and fp_ok and box0 and all(x.is_finite for x in dpsi_h) and stat and s_th and s_dmu
    ok &= all(x.is_finite for x in s_h) and zero(s_inf + 1/mu)
    print("  V2: (a) K*_reg - (v/2) L_{W*} g stationary %s, Theta(K*_reg) = 0 %s, dmu[K*_reg] = 1 %s; (b) F' as stated "
          "%s, Box_0 Psi = 0 %s, d Psi at r_h (mu = 1, v = 0) %s; S stationary %s, Theta(S) = 0 %s, dmu[S] = 1 %s, S "
          "(vv, vr, rr, thth/r^2) at r_h %s, S_vv -> %s at infinity" % (a_stat, a_th, a_dmu, fp_ok, box0, dpsi_h, stat,
                                                                      s_th, s_dmu, s_h, s_inf), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- V3
def v3(control=False):
    cc = 1 if control else sp.Rational(1, 2)
    W = [cc*v*WSTAR[0] + A_EXPR, cc*v*WSTAR[1] + B_EXPR, 0, 0, 0]
    bW = box(GEO, W)
    res = [bW[0] - 1/r**3] + bW[1:]
    ok = all(zero(sp.expand_log(sp.simplify(e), force=True)) for e in res)
    print("  V3%s: Box W** = dv/r^3 exactly in every component (expand_log(force=True)): %s"
          % (" control (coefficient 1)" if control else "", ok), flush=True)
    return ok


# --------------------------------------------------------------------------------------------------------------- V4
def v4(control=False):
    """each item: the round-1 claim (must hold) and its control (must fail); returns (claims ok, some control holds)"""
    out = {}
    a = sp.Function("a")(th)
    sol = sp.dsolve(sph_div_form([a, 0, 0]), a)
    # control: 'every smooth divergence-free 1-form is exact' off the class; cos^2 th dphi1 is divergence-free and
    # not closed ((dw)_{th phi1} != 0), so that claim fails
    w = [0, sp.cos(th)**2, 0]
    dw = sp.diff(w[1], th)
    out["R3c"] = (zero(sp.diff(sol.rhs*sqg, th)), not (zero(sph_div_form(w)) and not zero(dw)))
    t1, t2, t3, t4 = [sp.Function(n)(th) for n in ("t1", "t2", "t3", "t4")]
    Tg = sp.Matrix([[t1, t4, 0], [t4, t2, 0], [0, 0, t3]])
    dvg = sph_div_tensor(Tg)
    out["R3d"] = (True, zero(dvg[1]))                                 # control claim: no phi1 component
    mpmath.mp.dps = 40
    meas = 4*sp.pi**2*sqg
    errs = []
    for j in (1, 2):
        l = 2*j
        k2 = l*(l + 2)
        S = legendre_S(j)
        HsS, _ = sph_hess(S)
        TS = HsS - gam*sph_lap(S)/3
        dens = sum(gami[i, i]*gami[jj, jj]*TS[i, jj]**2 for i in range(3) for jj in range(3))*meas
        num = mpmath.quad(sp.lambdify(th, dens, "mpmath"), [0, mpmath.pi/4, mpmath.pi/2])
        n0 = sp.Rational(1, 2*j + 1)*2*sp.pi**2
        tgt = mpmath.mpf(sp.N(sp.Rational(2, 3)*k2*(k2 - 2)*n0, 40))
        errs.append(abs(num - tgt)/abs(tgt))
    out["R3e"] = (True, max(errs) < mpmath.mpf("1e-30"))
    x = sp.Symbol("x", positive=True)
    q2 = (1 + x)**2/(sp.Rational(2, 3)*x*(x - 2))
    out["R3f"] = (True, sp.maximum(q2, x, sp.Interval(8, sp.oo)) == sp.Rational(243, 80))
    av, bv = sp.Function("av")(v, r), sp.Function("bv")(v, r)
    q0 = sp.simplify(charge_density(GEO, [av, bv, 0, 0, 0]).subs(r, s).doit())
    out["H2"] = (True, zero(q0))
    Kil = [-f, 1, 0, 0, 0]
    qsum = sp.simplify(S3*charge_density(GEO, [WSTAR[i] + Kil[i] for i in range(N)]).subs(r, s))
    vK = [v*e for e in Kil]
    ellK = sp.simplify(S3*s**3*sp.simplify(box(GEO, vK)[0]).subs(r, s))
    out["H3"] = (zero(qsum - 4*sp.pi**2*(1 + mu)), zero(qsum - 4*sp.pi**2) or zero(ellK - 4*sp.pi**2))
    qq = sp.Rational(3, 2)
    Y = (1 + v)**(-qq)
    L = GEO.lie([Y*r*1, 0, 0, 0, 0])                                # the 1-form of the vector Y r d_r is (Y r) dv
    lim = sp.limit(sp.simplify(L[2][2]*v**(qq + 1)), v, sp.oo)
    out["R5"] = (True, bool(lim.is_finite))
    ok_claims = all(c[0] for c in out.values())
    some_ctl = any(c[1] for c in out.values())
    if control:
        print("  V4 controls (each must be False): %s" % {k: c[1] for k, c in out.items()}, flush=True)
        return some_ctl
    print("  V4 claims re-checked where a value is stated (R3c, H3): %s; H3 values: Q[W* + (d_v)^flat] = %s, "
          "ell([Box, v](d_v)^flat) = %s" % ({k: c[0] for k, c in out.items()}, qsum, ellK), flush=True)
    return ok_claims


# --------------------------------------------------------------------------------------------------------------- V5
def v5(control=False):
    """K_static - dv^2/r^2 = L_{zeta d_v} g with zeta' = 1/(r^2 f^2): the static mass change differs from (0.1)'s K
    (which is dv^2/r^2 on {r <= 2 R_1}) by a gauge vector with a double pole at r_h"""
    zeta = sp.Function("zeta")(r)
    Ks = [[0]*N for _ in range(N)]
    Ks[0][0] = 1/r**2
    Ks[0][1] = Ks[1][0] = -1/(r**2*f)
    Ks[1][1] = 2/(r**2*f**2)
    L = GEO.lie([-f*zeta, zeta, 0, 0, 0])
    zp = 1/(r**2*f) if control else 1/(r**2*f**2)
    diff = [[Ks[a][b] - (1/r**2 if a == b == 0 else 0) - L[a][b] for b in range(N)] for a in range(N)]
    ok = all(zero(sp.simplify(e.subs(sp.Derivative(zeta, r), zp).subs(zeta, 0))) for row in diff for e in row)
    pole = sp.limit(((r - 1)**2*zp).subs(s, 1), r, 1, "+")
    print("  V5%s: K_static - dv^2/r^2 = L_{zeta d_v} g with zeta' = %s: %s; (r - 1)^2 zeta' -> %s at mu = 1"
          % (" control" if control else "", zp, ok, pole), flush=True)
    return ok and (control or pole != 0)


CHECKS = [("V1", v1), ("V2", v2), ("V3", v3), ("V4", v4), ("V5", v5)]


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
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
