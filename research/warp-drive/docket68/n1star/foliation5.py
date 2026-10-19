#!/usr/bin/env python3
"""foliation5.py -- N1*, route W, steps 3 and 5: the null foliation, Touati's commutator lemma and the domain, on
five-dimensional Vaidya.

Commissioned at item 522 (N1STAR-LOG.md).  Touati regains his derivative loss "by a null foliation associated to g0
as well as a Fourier cut-off" (arXiv:2206.12318v4, abstract, READ 2026-10-19).  The null foliation enters through his
Lemma 3.1, READ verbatim: "Let f be compactly supported, we have ||[L0, box_g0] f||_L2 <= C(C0) (||d L0 f||_L2
+ ||box_g0 f||_L2 + ||d f||_L2)" (3.32), proved in his Appendix B from the background null frame; and his smallness
enters the geometry where he writes "Taking eps small enough in (2.9) and (2.10) then ensures that |1/L^t_0| + |L0^m|
+ |d L0^m| <= C(C0)" (5.48) and "Taking eps small enough in (2.9) we obtain the existence of a universal constant C'
> 0 such that 1/C' E_sigma(h) <= E <= C' E_sigma(h)" (5.52).  On the record's background all of this is explicit.
Labels: computed (exact, sympy), READ, deduced.

  B1 (computed, exact) The slices.  tau = v - r has g0^-1(dtau, dtau) = (1 - mu/r^2) - 2 = -1 - mu/r^2 <= -1 at every
     r > 0, inside the horizon included: Sigma_tau is spacelike everywhere, with induced metric
     (1 + mu/r^2) dr^2 + r^2 dOmega_3^2.  L0(tau) = 1 exactly: the null generator is transverse to every slice with
     L0^tau = 1, which replaces Touati's (5.48) without any smallness.
  B2 (computed, exact) The null foliation.  The level sets of v are null for g0 (B1 of ansatz5); L0 = -d_r is their
     null geodesic generator; the conjugate null vector Lb0 = 2 d_v + (1 - mu/r^2) d_r has g0(Lb0, Lb0) = 0 and
     g0(L0, Lb0) = -2; e_A = r^-1 (d_th, d_phi1/cos th, d_phi2/sin th) complete Touati's background null frame (2.14).
     The leaves P_{tau, v} = Sigma_tau cap {v = const} are the round 3-spheres r = v - tau: compact, so Touati's
     asymptotically-planar condition (2.10) has no counterpart to meet.  (Deduced, not computed: the foliation is
     regular on {r > 0}, its generators -d_r reaching r = 0 only, outside D.)
  B3 (computed, exact) Touati's Lemma 3.1 on Vaidya, its structure exactly.  For any u(v, r, th, phi1, phi2), with
     F = 1 - mu/r^2 and the principal part box~ = g0^{mn} d_m d_n,
        [L0, box~] u = (d_r F + 2F/r) d_r(L0 u) + (4/r) d_v(L0 u) + (2/r) box~ u = (2/r) (d_r(L0 u)
                       + 2 d_v(L0 u) + box~ u)
     exactly (d_r F + 2F/r = 2/r: the mass drops out).  Touati's lemma is stated for the wave operator of g0, which
     equals box~ only under his wave condition (2.7); in these coordinates box_g0 = box~ + (3/r) d_v
     + (3/r - mu/r^3) d_r + (2/(r^2 tan 2th)) d_th, and for it
        [L0, box_g0] u = (2/r) (d_r(L0 u) + 2 d_v(L0 u) + box_g0 u) - (3/r^2) d_v u - (3/r^2 + mu/r^4) d_r u,
     a first-order remainder, bounded on D by the ||d u|| term of (3.32).  In both forms the only second derivatives
     are d(L0 u) and the wave operator, as (3.32) needs; no null frame, no Appendix B and no smallness enter.  The same
     holds for T^2-invariant u.  (Found by the session's verifier, 2026-10-19: an earlier wording claimed "no
     remainder" for Touati's operator.)
  B4 (computed, exact, for mu >= mu0 > 0) The domain is bounded away from r = 0 and from infinity.  For tau >= tau0
     and v <= V = v_end + T, r = v - tau <= V - tau0, and r >= r_q(v) = (sqrt(72) mu(v) l5^2)^(1/4)
     >= (sqrt(72) mu0 l5^2)^(1/4) > 0 since mu is nondecreasing; so D_T cap {tau >= tau0} lies in
     r_q(mu0) <= r <= V - tau0, where the slices' induced metric (1 + mu/r^2) dr^2 + r^2 dOmega^2 has eigenvalues
     between 1 and 1 + mu(V)/r_q(mu0)^2 relative to the flat one: this replaces (5.52).  (Deduced, not computed here:
     its boundary is Sigma_tau0 (spacelike, past), {v = V} (null, future) and {r = r_q(v)} (spacelike, future:
     hf_theorem5 F2), so the energy identity on it has nonnegative fluxes on the future boundaries.)

Deduced, not computed here (see N1STAR-STATUS.md): T^2-invariant functions on the slices obey H^2 in L^oo (the orbits
of T^2 on {r > 0} are circles on the axes and tori elsewhere, so near an axis an invariant function is a function on
a three-dimensional quotient); this is what lets Touati's second-order ansatz (his section 3.2.4: "This shows why
K >= 2 is necessary") stay second order in 4+1 dimensions, where H^2 is not in L^oo without the symmetry.
sympy.  python3 foliation5.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

MUT = set()
MUTANTS = {"wrong_slice": "the slices tau = v + r: timelike (B1)",
           "L0_past": "L0 = +d_r, the past-directed generator: transversality fails (B1)",
           "no_box_term": "the box~ u term dropped from the commutator decomposition (B3)",
           "bad_Lb": "Lb0 = 2 d_v + d_r: not null for mu != 0 (B2)",
           "no_seed_floor": "the seed mass allowed to vanish: no positive lower bound on r (B4)"}

v, r, th, p1, p2 = sp.symbols("v r theta phi1 phi2", real=True)
X = [v, r, th, p1, p2]
mu = sp.Function("mu")(v)
F = 1 - mu/r**2
C, S = sp.cos(th), sp.sin(th)


def metric():
    g = sp.diag(-F, 0, r**2, r**2*C**2, r**2*S**2)
    g[0, 1] = g[1, 0] = 1
    return g, sp.simplify(g.inv())


def b1():
    g, gi = metric()
    tau = v + r if "wrong_slice" in MUT else v - r
    dtau = [sp.diff(tau, x) for x in X]
    norm = sp.simplify(sum(gi[i, j]*dtau[i]*dtau[j] for i in range(5) for j in range(5)))
    L0 = [-gi[i, 0] for i in range(5)]
    if "L0_past" in MUT:
        L0 = [-x for x in L0]
    L0tau = sp.simplify(sum(L0[i]*dtau[i] for i in range(5)))
    # induced metric on Sigma_tau: v = tau + r
    tt = sp.Symbol("tau")
    ind = sp.simplify(g[0, 0] + 2*g[0, 1])           # dv = dr: coefficient of dr^2
    m_ = sp.Symbol("m", positive=True)
    rr = sp.Symbol("rr", positive=True)
    return dict(norm=norm, bound=sp.simplify(norm + 1 + mu/r**2), L0tau=L0tau, ind_rr=ind,
                neg=sp.simplify(norm.subs(mu, m_).subs(r, rr)).is_negative)


def b2():
    g, gi = metric()
    L0 = [-gi[i, 0] for i in range(5)]
    Lb = [2, F, 0, 0, 0]
    if "bad_Lb" in MUT:
        Lb = [2, 1, 0, 0, 0]
    gg = lambda a, b: sp.simplify(sum(g[i, j]*a[i]*b[j] for i in range(5) for j in range(5)))
    eA = [[0, 0, 1/r, 0, 0], [0, 0, 0, 1/(r*C), 0], [0, 0, 0, 0, 1/(r*S)]]
    frame = (gg(L0, L0) == 0 and gg(Lb, Lb) == 0 and sp.simplify(gg(L0, Lb) + 2) == 0
             and all(gg(L0, e) == 0 and gg(Lb, e) == 0 for e in eA)
             and all(sp.simplify(gg(eA[i], eA[j]) - (1 if i == j else 0)) == 0 for i in range(3) for j in range(3)))
    # the leaf {tau = tau0, v = v0} is r = v0 - tau0 with the round metric r^2 dOmega_3
    return dict(frame=frame, L0=L0)


def b3():
    g, gi = metric()
    sq = r**3*C*S
    boxc = lambda w: sp.expand(sum(sp.diff(sq*gi[i, j]*sp.diff(w, X[j]), X[i]) for i in range(5) for j in range(5))/sq)
    u = sp.Function("u")(*X)
    box = lambda w: sp.expand(sum(gi[i, j]*sp.diff(w, X[i], X[j]) for i in range(5) for j in range(5)))
    L0 = lambda w: -sp.diff(w, r)
    comm = sp.expand(L0(box(u)) - box(L0(u)))
    L0u = L0(u)
    cb = 0 if "no_box_term" in MUT else 2/r
    model = (sp.diff(F, r) + 2*F/r)*sp.diff(L0u, r) + (4/r)*sp.diff(L0u, v) + cb*box(u)
    resid = sp.expand(comm - model)
    second = [d for d in resid.atoms(sp.Derivative) if sum(k for _, k in d.variable_count) >= 2]
    exact = resid == 0
    # T^2-invariant case
    w = sp.Function("w")(v, r, th)
    comm_w = sp.expand(L0(box(w)) - box(L0(w)))
    model_w = (sp.diff(F, r) + 2*F/r)*sp.diff(L0(w), r) + (4/r)*sp.diff(L0(w), v) + cb*box(w)
    second_w = [d for d in sp.expand(comm_w - model_w).atoms(sp.Derivative)
                if sum(k for _, k in d.variable_count) >= 2]
    # the covariant wave operator of g0: its commutator with L0 differs by the stated first-order remainder
    uc = sp.Function("u")(*X)
    commc = sp.expand(-sp.diff(boxc(uc), r) + boxc(sp.diff(uc, r)))
    L0c = -sp.diff(uc, r)
    remc = sp.simplify(commc - (2/r)*(sp.diff(L0c, r) + 2*sp.diff(L0c, v) + boxc(uc))
                       - (-(3/r**2)*sp.diff(uc, v) - (3/r**2 + mu/r**4)*sp.diff(uc, r)))
    return dict(second=second, second_w=second_w, exact=exact, coeffs=[sp.simplify(sp.diff(F, r) + 2*F/r), 4/r, cb],
                cov_rem=remc)


def b4():
    """r is bounded on D_T cap {tau >= tau0}: above by V - tau0, below by r_q(mu0) > 0 (mu nondecreasing)"""
    import z3
    R, Vv, T0, tau, vv, m0, m, l, s72 = z3.Reals("R V tau0 tau v m0 m l s72")
    rq = z3.Real("rq")
    seed = (m0 >= 0) if "no_seed_floor" in MUT else (m0 > 0)
    hyp = [s72 > 0, s72*s72 == 72, l > 0, seed, m >= m0, tau >= T0, vv <= Vv, R == vv - tau,
           rq >= 0, rq*rq*rq*rq == s72*m*l*l, R >= rq]
    lo = z3.Real("lo")
    hyp += [lo >= 0, lo*lo*lo*lo == s72*m0*l*l]
    s = z3.Solver()
    s.add(*hyp)
    s.add(z3.Not(z3.And(R <= Vv - T0, R >= lo, lo > 0)))
    bounded = s.check() == z3.unsat
    # induced metric on Sigma_tau: dr^2 coefficient 1 + mu/r^2, between 1 and 1 + mu/r^2 at the extremes
    g, _ = metric()
    ind = sp.simplify(g[0, 0] + 2*g[0, 1])
    return dict(bounded=bounded, ind=ind)


def compute():
    return dict(b1=b1(), b2=b2(), b3=b3(), b4=b4())


def checks(o):
    c = {}
    q = o["b1"]
    c["B1 tau = v - r: g0^-1(dtau, dtau) = -1 - mu/r^2 <= -1 (spacelike everywhere); L0(tau) = 1; induced dr^2 "
      "coefficient 1 + mu/r^2"] = (q["bound"] == 0 and q["L0tau"] == 1
                                   and sp.simplify(q["ind_rr"] - (1 + mu/r**2)) == 0)
    q = o["b2"]
    c["B2 Touati's null frame on Vaidya: L0 = -d_r, Lb0 = 2 d_v + F d_r, g(L0, Lb0) = -2, e_A orthonormal"] = (
        q["frame"] and q["L0"] == [0, -1, 0, 0, 0])
    q = o["b3"]
    c["B3 [L0, box~] u = (2/r)(d_r(L0 u) + 2 d_v(L0 u) + box~ u) exactly; for box_g0 a first-order remainder only"] = (
        not q["second"] and not q["second_w"] and q["exact"] and q["coeffs"][0] == 2/r and q["cov_rem"] == 0)
    q = o["b4"]
    c["B4 on D_T cap {tau >= tau0}: r_q(mu0) <= r <= V - tau0 (Z3); induced dr^2 coefficient 1 + mu/r^2"] = (
        q["bounded"] and sp.simplify(q["ind"] - (1 + mu/r**2)) == 0)
    return c


def selftest():
    o = compute()
    c = checks(o)
    for k, v_ in c.items():
        print("%-118s %s" % (k[:118], "PASS" if v_ else "FAIL"))
    print("  B3 coefficients: %s" % (o["b3"]["coeffs"],))
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear()
        MUT.add(m_)
        try:
            c = checks(compute())
            failed = [k[:40] for k, v_ in c.items() if not v_]
        except Exception as ex:                       # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-14s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
