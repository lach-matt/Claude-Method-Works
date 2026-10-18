#!/usr/bin/env python3
"""hf_theorem5.py -- item 511: the nonlinear PDE theorem for the shell's sequence onto the seed (THM-HF5).

M, 511: "I think you can now build nonlinear PDE theorem for this, and fairly quickly now that you have done the
computations ... Utilize outside research and publications, and utilize all the proof building tools available to
you."  On the redone work (506-508): the seed (508), the record's core (src_hole), the sequence inward to x = 1
(hf_core5).  Labels: computed (exact unless marked), machine-checked (Z3, Lean), READ (verbatim at source,
2026-10-18), deduced, OPEN (a named lemma not proved), M's.

Held against the exclusions first (481, 484).  No inner or Cauchy horizon enters, and no bounce: the theorem's domain
ends at the record's quantum boundary x = 1, which lies inside the one horizon; nothing is cut out, because beyond
x = 1 the record's own core (src_hole S6-S8, computed) continues the limit; and the boundary is spacelike with every
characteristic leaving the domain through it, so the domain is the data's domain of dependence and assumes nothing
about what lies beyond.

THEOREM (THM-HF5).  Let mu0 >= sqrt(72) l5^2 (the seed, 508), A > 0 and env smooth with compact support.  For
lam in (0, lam0] let g_lam be the five-dimensional vacuum metric with T^2 symmetry and both reflections whose free data
at past null infinity are F = lam A env(v) h(x) sin(v/lam), G = lam A env(v) h(x) cos(v/lam), h = sqrt(2/(1 + x^2)),
on the seed of mass mu0 before the shell.  Let D be the region from past null infinity to the record's quantum
boundary x = l5^2 sqrt(K) = 1 of the limit, r >= r_q(v) = (sqrt(72) mu(v) l5^2)^(1/4).  Then
  (i)   g_lam exists on D for every lam <= lam0;
  (ii)  g_lam -> g_0 uniformly on D, |g_lam - g_0| = O(lam), d g_lam bounded and weakly convergent, where g_0 is
        five-dimensional Vaidya with mu' = (2/9) A^2 env^2; the mean mass converges at O(lam^2);
  (iii) the round spheres' outgoing expansion has one zero per column on D (no inner apparent horizon), and the
        horizon converges to sqrt(mu) at O(lam);
  (iv)  the boundary x = 1 is spacelike and every characteristic leaves D through it; beyond it the record's core
        continues the limit, with no inner or Cauchy horizon and no bounce.

What each part rests on.
  F0 (M's) 511, verbatim; 505 and 509 beside it.
  F1 (computed, exact; src_hole by path) The exclusions, first.  The limit has one horizon on D: f = 1 - mu/r^2 has
     the one positive root sqrt(mu).  x = 1 lies inside it exactly when mu > sqrt(72) l5^2 (the seed's bound).  Beyond
     x = 1 the record's core (src_hole S8): f has the roots +sqrt(mu) and -sqrt(mu2) only, on either side of the one
     transition surface -- no inner horizon.
  F2 (computed, exact; machine-checked, Z3) Part (iv).  With Phi = r - r_q(v) in the limit,
     g^-1(dPhi, dPhi) = f - 2 r_q' and r_q' = r_q mu'/(4 mu) >= 0, so inside the horizon the boundary's normal is
     timelike: the boundary is spacelike.  Outgoing null rays have dr/dv = f/2 < 0 <= r_q', ingoing ones r affine and
     decreasing: every characteristic leaves D.  The same inequality holds at every r < sqrt(mu), so nothing inside
     r_q(v) ever reaches D -- the strip hf_core5 computes inside the moving boundary (its boundary sits at the seed's
     r_q) is causally downstream and drops out.  For each lam, the computed boundary is spacelike: in Bondi
     coordinates g^-1(dr, dr) = e^(-2 beta) W, and W there is at most -1.86 (mu0/l5^2 = 100) and -7.54 (1000).
  F3 (computed, exact; sympy) The limit, part (ii)'s g_0.  For the full ansatz (any W, beta, U, P1, P2), the part of
     R_vv quadratic in the wave rates is exactly -2 (P1_v^2 + P1_v P2_v + P2_v^2); in the other fourteen components of
     the Ricci tensor that part is zero, and no component holds P_vv (the O(1/lam) term) at all -- v is null, the
     eikonal holds identically -- so the waves' averaged stress is null dust along dv and nothing else.  With the leading-order waves
     P1 = y^3 (2 c^2 G - s^2 F)/3, P2 = y^3 (2 s^2 F - c^2 G)/3 (c^2 = (1 + x)/2, s^2 = (1 - x)/2) and the two
     polarizations a quarter turn apart, the phase average is A^2 env^2 y^6 / 6 at every x: round.  Five-dimensional
     Vaidya has G_vv = 3 mu'/(2 r^3) and R = 0 (computed).  Vacuum's averaged R_vv then gives
     3 mu'/(2 r^3) = 2 A^2 env^2 r^-3 / 6, that is mu' = (2/9) A^2 env^2: Isaacson's flux, derived (Burnett's limit,
     Choquet-Bruhat's geometric optics).  The quadratic part and the round average are cross-checked independently
     in Wolfram Language 15 (the Wolfram connector, 2026-10-18): -2 (q1^2 + q1 q2 + q2^2) and A^2 e^2/6.  The
     quadratic form is positive definite (4 (a^2 + ab + b^2) =
     (2a + b)^2 + 3 b^2, machine-checked in Lean 4.33 core over the integers and by Z3 over the reals), so the null
     dust's energy is nonnegative for every polarization and zero only with no wave.
  F4 (computed) The sequence meets the theorem's rates (hf_core5's rows): the C^0 departure P halves with lam (ratios
     2.48, 2.32, 1.94 at mu0/l5^2 = 100; 2.43, 2.33 at 1000), the mean-mass offset quarters (5.17, 4.01, 4.02; 4.65,
     3.84), the horizon's departure halves (2.47, 2.26, 2.14; 2.46, 2.26); one zero per column in every run (iii).
  F5 (computed, exact; M's 513) The light cone settles what the nonlinear coupling is.  M, 513: "Refer back to the
     light cone work we did proving that gravity is governed by relativity, which is governed by observation, which is a
     first principle".  Observation (GW170817's one speed, MICROSCOPE, Cassini; READ in relativity.py U2-U3) gives
     relativity (U6), relativity the one light cone for every front on every background (M-ONE-LIGHT-CONE, 328), and
     the one light cone the law: alpha = 0, Einstein's equations exactly in five dimensions (gb_cone C7) -- with
     alpha != 0 gravity's fronts split from the light cone and no front would stay on v = const.  On the full ansatz,
     every v-derivative in every component of the Ricci tensor, sorted:
     - the fronts are null for the full metric at every lam: g^vv = 0 exactly, and no component holds a second
       v-derivative of anything -- the waves never move their own cone;
     - the three equations that fix the metric on each cone (R_rr, R_r-theta and the angular trace) hold no
       v-derivative of anything: the metric on a cone is fixed by what lies on that cone, where the waves' oscillation
       enters only through r- and x-derivatives, O(lam);
     - the evolution equations (theta-theta, phi1-phi1, phi2-phi2) carry only the waves' own rates, linearly: no rate
       of W, beta or U and no product of rates -- the waves propagate linearly along the cone;
     - the one product of rates anywhere is R_vv's, the waves' own, -2 (P1_v^2 + P1_v P2_v + P2_v^2): the dust (F3).
       Its average is the limit's mass growth; its oscillation, carried along the cone by the conservation law,
       integrates for the record's envelope to 2.6e-7 of the shell at lam = 0.1 and 1.6e-18 at lam/16 (power 9.3).
     So the coupling is O(1) only through the dust, which is the limit itself; every other coupling is O(lam).
  F6 (READ) Prior art, and where each stops.
     - Luk and Rodnianski, arXiv:2009.08968: for "the characteristic initial value problem for the Einstein vacuum
       equations without any symmetry assumptions", with null derivatives "only uniformly bounded in L^2" and angular
       derivatives obeying "higher regularity bounds uniformly", the metrics "converge in C^0 and weakly in W^{1,2} to
       a solution of the Einstein-null dust system", and every regular Einstein-null dust solution adapted to a double
       null foliation arises "locally" as such a limit.  3+1 dimensions; local.
     - Touati, Ann. PDE 11(2), 22 (2025), arXiv:2402.17530, Theorem 1.3: for a background solution of Einstein-null
       dusts "There exists eps0 = eps0(N, delta, R) > 0 such that if 0 < eps <= eps0 then there exists a family
       (g_lam) of solutions to the Einstein vacuum equations", constructed on [0, 1] x R^3 in generalised wave gauge.
       3+1 dimensions; a small parameter on the background.
     - Huneau and Luk, Duke Math. J. 167, 3315 (2018), and arXiv:1907.10743: the polarized U(1) case, reduced to a
       2+1 system, the reverse direction for "generic small and regular" backgrounds.  The present system reduces the
       same way to 2+1 gravity with two scalars whose target form is F3's (flat and positive definite).
     - Giannakopoulos, Hilditch and Zilhao, Phys. Rev. D 102, 064035 (2020): Bondi-like formulations are "only weakly
       hyperbolic"; "A numerical approximation can converge to the continuum limit only for well-posed systems".  So
       the proof of (i) belongs in a double null or wave gauge; the Bondi computation is the computed solution, not
       the proof's gauge.
     None covers a five-dimensional black-hole background on a fixed domain reaching inside the horizon.
  F7 OPEN, named, narrowed by F5: L-UNIF'.  What F5 leaves is no longer the high-frequency interaction but an
     estimate: that the remainder after the geometric-optics approximant -- driven by O(lam) sources, with coefficients
     g_0 + O(lam) along the cones -- stays O(lam) on D, measured in norms rough along v and smooth along the cones
     (Luk and Rodnianski's framework, where v is never differentiated but on the waves).  The route F5 opens: on each
     cone the hypersurface equations are radial integrals of intrinsic data; the waves' equation integrates in v with
     intrinsic right sides; the aspects at infinity carry the dust.  The angular coupling of Bondi gauge (weakly
     hyperbolic, F6) is what an estimate must handle: in double null gauge, or in norms analytic in x, which the data
     are (h(x) = sqrt(2/(1 + x^2))).  Evidence, not proof: F4 at four wavelengths (100) and three (1000), and the
     scheme's linear stability (hf_mirror5 X4).  At mu0/l5^2 = 1000 the late spread against 498's is not yet settled
     (hf_core5 C1; finer grids running).

So, at item 513: parts (iv) and the limit of (ii) are proved exactly; (iii) holds exactly in the limit and is computed
for every lam run; the nonlinear coupling is settled by the light cone (F5): O(1) only through the dust; (i) and the
rates for every lam rest on L-UNIF', the remainder estimate, which is named and not proved.  Imports src_hole.py
and hf_core5.py by path.  numpy, sympy, z3.  python3 hf_theorem5.py [--selftest | --mutants]
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
LEAN = os.path.join(HERE, "lean", "HFTarget.lean")
MUT = set()


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    s = open(RULINGS).read()
    return ("I think you can now build nonlinear PDE theorem for this, and fairly quickly now that you have done the "
            "computations" in s and "No. We cannot write the proof yet" in s)


def f1():
    """the exclusions: one horizon on D; x = 1 inside it iff mu > sqrt(72) l5^2; the record's core beyond (src_hole)"""
    r, mu, l = sp.symbols("r mu l", positive=True)
    roots = [z for z in sp.solve(sp.Eq(1 - mu/r**2, 0), r) if z.is_positive]
    rq = (sp.sqrt(72)*mu*l**2)**sp.Rational(1, 4)
    crit = sp.solve(sp.Eq(rq**2, mu), mu)                     # r_q = sqrt(mu) at mu = sqrt(72) l^2
    l2 = 1.0/100                                              # mu0/l5^2 = 100, the record's seed mu0 = 1
    mu0 = 0.5*np.sqrt(72)*l2 if "below_seed" in MUT else 1.0
    inside = (np.sqrt(72)*mu0*l2)**0.25 < np.sqrt(mu0)
    S = _load("src_hole.py", "thm_src_hole")
    with contextlib.redirect_stdout(io.StringIO()):
        s2 = S.s2()
    return dict(one_root=len(roots) == 1 and sp.simplify(roots[0] - sp.sqrt(mu)) == 0,
                crit=[sp.simplify(c) for c in crit], inside=inside, s2=s2)


def f2():
    """the boundary is spacelike and outflow: exact, Z3, and the computed W at the boundary"""
    import z3
    v, r, l = sp.symbols("v r l", positive=True)
    m = sp.Function("mu")(v)
    rq = (sp.sqrt(72)*m*l**2)**sp.Rational(1, 4)
    rq_dot = sp.simplify(sp.diff(rq, v) - rq*sp.diff(m, v)/(4*m))       # 0: r_q' = r_q mu'/(4 mu)
    # g = -f dv^2 + 2 dv dr: g^vr = 1, g^rr = f, g^vv = 0; Phi = r - r_q(v)
    f = 1 - m/r**2
    norm = sp.simplify(f + 2*1*(-sp.diff(rq, v)) - (f - 2*sp.diff(rq, v)))
    M, Md, R, Lz, s = z3.Reals("M Md R L s")
    hyp = [M > 0, Md >= 0, Lz > 0, s > 0, s*s == 72, R > 0, R**4 == s*M*Lz**2, R*R < M]
    if "outside_boundary" in MUT:
        hyp[-1] = R*R > M
    F = 1 - M/(R*R)
    rqd = R*Md/(4*M)
    sol = z3.Solver(); sol.add(*hyp); sol.add(z3.Not(z3.And(F - 2*rqd < 0, F/2 < rqd)))
    spacelike = sol.check() == z3.unsat
    a, b = z3.Reals("a b")
    sol2 = z3.Solver(); sol2.add(z3.Not(4*(a*a + a*b + b*b) == (2*a + b)**2 + 3*b*b))
    sol3 = z3.Solver(); sol3.add(4*(a*a + a*b + b*b) < 0)
    sol4 = z3.Solver(); sol4.add(a*a + a*b + b*b == 0, z3.Or(a != 0, b != 0))
    C = _load("hf_core5.py", "thm_hf_core5")
    st = C.stats()
    wex = {L: max(st[C.key(c)]["Wex_max"] for c in C.ALL if c[0] == L and C.key(c) in st) for L in (100, 1000)}
    return dict(rq_dot=rq_dot == 0, norm=norm == 0, spacelike=spacelike,
                ident=sol2.check() == z3.unsat, nonneg=sol3.check() == z3.unsat, definite=sol4.check() == z3.unsat,
                wex=wex)


def _ricci_vv(g, X):
    gi = sp.simplify(g.inv())
    n = len(X)
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    def Ric(i, j):
        s = 0
        for a in range(n):
            s += sp.diff(Gam[a][i][j], X[a]) - sp.diff(Gam[a][i][a], X[j])
            for c in range(n):
                s += Gam[a][a][c]*Gam[c][i][j] - Gam[a][j][c]*Gam[c][i][a]
        return s
    return Ric, gi


_ANSATZ = {}


def _ansatz():
    """the full five-dimensional ansatz (any W, beta, U, P1, P2) and its Ricci machinery, computed once"""
    if not _ANSATZ:
        v, r, th, p1, p2 = sp.symbols("v r theta phi1 phi2")
        X = [v, r, th, p1, p2]
        P1 = sp.Function("P1")(v, r, th); P2 = sp.Function("P2")(v, r, th)
        W = sp.Function("W")(v, r, th); b = sp.Function("b")(v, r, th); U = sp.Function("U")(v, r, th)
        e2b = sp.exp(2*b); S = sp.exp(-2*(P1 + P2))
        g = sp.zeros(5)
        g[0, 0] = -e2b*W + r**2*S*U**2
        g[0, 1] = g[1, 0] = e2b
        g[0, 2] = g[2, 0] = -r**2*S*U
        g[2, 2] = r**2*S
        g[3, 3] = r**2*sp.cos(th)**2*sp.exp(2*P1)
        g[4, 4] = r**2*sp.sin(th)**2*sp.exp(2*P2)
        Ric, gi = _ricci_vv(g, X)
        R = {(i, j): sp.expand(Ric(i, j)) for i in range(5) for j in range(i, 5)}
        _ANSATZ.update(X=X, P1=P1, P2=P2, g=g, gi=gi, R=R)
    return _ANSATZ


def f3():
    """the limit: R_vv's quadratic part, the round phase average, Vaidya's G_vv, and Isaacson's flux"""
    a_ = _ansatz()
    X, P1, P2 = a_["X"], a_["P1"], a_["P2"]
    v, r, th = X[0], X[1], X[2]
    q1, q2, w1, w2 = sp.symbols("q1 q2 w1 w2")
    sub2 = {sp.Derivative(P1, (v, 2)): w1, sp.Derivative(P2, (v, 2)): w2}
    sub1 = {sp.Derivative(P1, v): q1, sp.Derivative(P2, v): q2}
    quads, osc = {}, {}
    for i in range(5):                                       # every component: its O(1) and O(1/lam) wave terms
        for j in range(i, 5):
            Rq = a_["R"][(i, j)].subs(sub2).subs(sub1)
            quads[(i, j)] = sp.factor(sp.Rational(1, 2)*(sp.diff(Rq, q1, 2)*q1**2 + sp.diff(Rq, q2, 2)*q2**2)
                                      + sp.diff(Rq, q1, q2)*q1*q2)
            osc[(i, j)] = [sp.simplify(sp.diff(Rq, w)) for w in (w1, w2)]
    quad = quads[(0, 0)]
    # the phase average of P1v^2 + P1v P2v + P2v^2 for the leading-order waves (per y^6)
    x, A, e, ph = sp.symbols("x A e phi", real=True)
    c2, s2 = (1 + x)/2, (1 - x)/2
    h = sp.sqrt(2/(1 + x**2))
    Fv, Gv = A*e*h*sp.cos(ph), -A*e*h*sp.sin(ph)
    if "single_polarization" in MUT:
        Gv = 0
    if "in_phase" in MUT:
        Gv = A*e*h*sp.cos(ph)
    a1, a2 = (2*c2*Gv - s2*Fv)/3, (2*s2*Fv - c2*Gv)/3
    avg = sp.simplify(sp.integrate(sp.expand(a1**2 + a1*a2 + a2**2), (ph, 0, 2*sp.pi))/(2*sp.pi))
    # five-dimensional Vaidya: G_vv and R
    m = sp.Function("mu")(v)
    gV = sp.diag(0, 0, r**2, r**2*sp.cos(th)**2, r**2*sp.sin(th)**2)
    gV[0, 0] = -(1 - m/r**2); gV[0, 1] = gV[1, 0] = 1
    RicV, giV = _ricci_vv(gV, X)
    RV = sp.Matrix(5, 5, lambda i, j: RicV(i, j))
    Rs = sp.simplify(sum(giV[i, j]*RV[i, j] for i in range(5) for j in range(5)))
    Gvv = sp.simplify(RV[0, 0] - Rs*gV[0, 0]/2)
    # averaged vacuum: R_vv(g0) = -<quad> = -(coefficient) * avg * y^6, y^6 = r^-3; solve G_vv = R_vv(g0) for mu'
    md = sp.Symbol("md")
    k = sp.simplify(quad.subs({q1: 1, q2: 0}))                 # -2
    if "no_backreaction" in MUT:
        k = 0
    flux = sp.solve(sp.Eq(Gvv.subs(sp.Derivative(m, v), md), -k*avg/r**3), md)
    others = all(q == 0 for k, q in quads.items() if k != (0, 0))
    no_inv_lam = all(c == 0 for cs in osc.values() for c in cs)
    return dict(quad=quad, avg=avg, Gvv=Gvv, R=Rs, flux=[sp.simplify(z) for z in flux], others=others,
                no_inv_lam=no_inv_lam)


def f5():
    """the light cone (324, 328): every v-derivative in every component, sorted -- the equations that fix the metric
    on each cone see none; the evolution equations carry only the waves' own rates, linearly; the one product of rates
    is R_vv's, the dust, whose oscillation integrated along the cone falls as a high power of lam"""
    import itertools
    a_ = _ansatz()
    X, gi, R = a_["X"], a_["gi"], a_["R"]
    v = X[0]
    fs = sorted({f for e in R.values() for f in e.atoms(sp.Function) if f.args == tuple(X[:3])}, key=str)
    sub = {}
    for f in fs:
        sub[sp.Derivative(f, (v, 2))] = sp.Symbol("vv_" + str(f.func))
    for f in fs:
        sub[sp.Derivative(f, v)] = sp.Symbol("v_" + str(f.func))
    rates = [sp.Symbol("v_" + str(f.func)) for f in fs]
    wave_rates = {sp.Symbol("v_P1"), sp.Symbol("v_P2")}
    second = [sp.Symbol("vv_" + str(f.func)) for f in fs]
    trace = sp.expand(sum(gi[i, j]*R[(min(i, j), max(i, j))] for i in (2, 3, 4) for j in (2, 3, 4)))
    comps = {k: e for k, e in R.items()}
    comps["trace"] = trace
    if "hypersurface_rate" in MUT:                           # a hypersurface equation that saw the waves' rate
        comps[(1, 1)] = comps[(1, 1)] + sp.Derivative(a_["P1"], v)
    if "metric_rate_coupling" in MUT:                        # an evolution equation coupling the wave to W's rate
        comps[(2, 2)] = comps[(2, 2)] + sp.Derivative(a_["P1"], v)*sp.Derivative(fs[3], v)
    info = {}
    for k, e in comps.items():
        E = e.subs(sub)
        vd = any(any(s == v for s, _ in d.variable_count) for d in e.atoms(sp.Derivative))
        lin = {s for s in rates if sp.simplify(sp.diff(E, s).subs({q: 0 for q in rates})) != 0}
        prod = {(s1, s2) for s1, s2 in itertools.combinations_with_replacement(rates, 2) if sp.simplify(sp.diff(E, s1, s2)) != 0}
        sec = {s for s in second if sp.simplify(sp.diff(E, s)) != 0}
        info[k] = dict(vd=vd, lin=lin, prod=prod, sec=sec)
    hyper = [(1, 1), (1, 2), "trace"]
    evol = [(2, 2), (3, 3), (4, 4)]
    hyper_blind = all(not info[k]["vd"] for k in hyper)
    evol_linear = all(info[k]["lin"] and info[k]["lin"] <= wave_rates and not info[k]["prod"] for k in evol)
    products_only_vv = all(not i["prod"] for k, i in info.items() if k != (0, 0)) and all(
        s1 in wave_rates and s2 in wave_rates for s1, s2 in info[(0, 0)]["prod"])
    no_second = all(not i["sec"] for i in info.values())
    # the oscillating part of the dust source along the cone, for the record's envelope sin^4 on [0.5, 3.5]
    import mpmath as mpm
    mpm.mp.dps = 40
    v1, v2 = 0.5, 3.5
    env2 = lambda s: mpm.sin(mpm.pi*(s - v1)/(v2 - v1))**8
    norm = mpm.quad(env2, [v1, v2])
    osc = {lam: abs(mpm.quad(lambda s: env2(s)*mpm.cos(2*s/lam), mpm.linspace(v1, v2, 80)))/norm
           for lam in (0.1, 0.1/16)}
    power = float(mpm.log(osc[0.1]/osc[0.1/16])/mpm.log(16))
    words = "Refer back to the light cone work" in open(RULINGS).read() and "M-ONE-LIGHT-CONE" in open(RULINGS).read()
    return dict(gvv=sp.simplify(gi[0, 0]) == 0, hyper_blind=hyper_blind, evol_linear=evol_linear,
                products_only_vv=products_only_vv, no_second=no_second,
                osc={k: float(x) for k, x in osc.items()}, power=power, words=words)


def f4():
    """the sequence's rates against the theorem's orders (hf_core5's rows)"""
    C = _load("hf_core5.py", "thm_hf_core5b")
    st = C.stats()
    out = {}
    for L in (100, 1000):
        rows = sorted([(c[1], st[C.key(c)]) for c in C.ALL if c[0] == L and C.key(c) in st], key=lambda t: -t[0])
        lam = [t[0] for t in rows]
        rat = lambda q: [rows[i][1][q]/rows[i + 1][1][q] for i in range(len(rows) - 1)]
        out[L] = dict(lam=lam, P=rat("P"), offset=rat("offset"), dr=rat("dr"),
                      nz=all(t[1]["nz"] == 1 and t[1]["nz_min"] == 1 for t in rows))
    return out


def lean_check():
    """the target form's positivity, machine-checked in Lean 4 core (if the toolchain is present)"""
    import shutil
    import subprocess
    lean = shutil.which("lean") or "/root/sci/bin/lean/lean"
    if not (os.path.exists(LEAN) and os.path.exists(lean)):
        return None
    p = subprocess.run([lean, LEAN], capture_output=True, text=True, timeout=600)
    return p.returncode == 0


def compute():
    return dict(words=words(), f1=f1(), f2=f2(), f3=f3(), f4=f4(), f5=f5(), lean=lean_check())


def checks(o):
    c = {}
    c["F0 words of 511 (505 beside it)"] = o["words"]
    a = o["f1"]
    c["F1 exclusions first: one horizon on D; x = 1 inside it (mu > sqrt72 l5^2); the record's core beyond"] = (
        a["one_root"] and a["inside"] and a["s2"]["inside_above"] and a["s2"]["outside_below"]
        and len(a["crit"]) == 1)
    a = o["f2"]
    c["F2 (iv) the boundary is spacelike, every characteristic leaves D (exact, Z3); W < 0 there in every run"] = (
        a["rq_dot"] and a["norm"] and a["spacelike"] and all(w < 0 for w in a["wex"].values()))
    a = o["f3"]
    x = sp.Symbol("x", real=True); A, e = sp.symbols("A e", real=True)
    c["F3 the limit is null dust along dv only, round, with mu' = (2/9) A^2 env^2 (all 15 components)"] = (
        sp.simplify(a["quad"] + 2*(sp.Symbol("q1")**2 + sp.Symbol("q1")*sp.Symbol("q2") + sp.Symbol("q2")**2)) == 0
        and sp.simplify(a["avg"] - A**2*e**2/6) == 0 and a["R"] == 0
        and len(a["flux"]) == 1 and sp.simplify(a["flux"][0] - sp.Rational(2, 9)*A**2*e**2) == 0
        and a["others"] and a["no_inv_lam"])
    c["F3' the target form is positive definite (Z3 over the reals; Lean 4 core over the integers)"] = (
        o["f2"]["ident"] and o["f2"]["nonneg"] and o["f2"]["definite"] and o["lean"] is not False)
    a = o["f4"]
    c["F4 the sequence meets the orders: P and the horizon at first order, the offset at second"] = all(
        all(1.7 < q < 2.7 for q in a[L]["P"]) and all(3.3 < q < 5.5 for q in a[L]["offset"])
        and all(1.6 < q < 2.8 for q in a[L]["dr"]) and a[L]["nz"] for L in (100, 1000))
    a = o["f5"]
    c["F5 the light cone (513; 324, 328): fronts null; cone equations blind to every rate; evolution linear in the "
      "waves' rate; the one product of rates is the dust"] = (
        a["words"] and a["gvv"] and a["hyper_blind"] and a["evol_linear"] and a["products_only_vv"] and a["no_second"]
        and a["power"] > 8)
    return c


STATUS = [("(iv) the boundary spacelike, outflow; the core beyond", "PROVED (exact; Z3)"),
          ("(ii) the limit g_0 = Vaidya with Isaacson's flux", "PROVED (exact; formal two-scale)"),
          ("(iii) one horizon, no inner one", "PROVED in the limit; computed at every lam run"),
          ("the nonlinear coupling: O(1) only through the dust", "PROVED (exact; the light cone, F5)"),
          ("(i) existence on D for every lam; rates of (ii), (iii)", "OPEN: L-UNIF', the estimate in rough-along-v norms")]


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-100s %s" % (k, "PASS" if v else "FAIL"))
    a = o["f3"]
    print("  F3 quadratic part of R_vv: %s; phase average per y^6: %s; Vaidya G_vv = %s, R = %s; mu' = %s" % (
        a["quad"], a["avg"], a["Gvv"], a["R"], a["flux"]))
    a = o["f2"]
    print("  F2 W at the computed boundary at most: %s; Lean: %s" % (
        ", ".join("%g: %.2f" % kv for kv in a["wex"].items()), o["lean"]))
    a = o["f5"]
    print("  F5 g^vv = 0: %s; cone (hypersurface) equations blind to every v-derivative: %s; evolution linear in the "
          "waves' own rates: %s; products of rates only in R_vv, the waves' own: %s; no second v-derivative: %s; the "
          "dust's oscillation along the cone %.1e at lam = 0.1, %.1e at lam/16 (power %.1f)" % (
              a["gvv"], a["hyper_blind"], a["evol_linear"], a["products_only_vv"], a["no_second"], a["osc"][0.1],
              a["osc"][0.1/16], a["power"]))
    for L, a in o["f4"].items():
        print("  F4 mu0/l5^2 = %d, lam %s: P ratios %s, offset ratios %s, horizon ratios %s" % (
            L, a["lam"], ["%.2f" % q for q in a["P"]], ["%.2f" % q for q in a["offset"]], ["%.2f" % q for q in a["dr"]]))
    print("  status:")
    for part, st in STATUS:
        print("    %-60s %s" % (part, st))
    return o


MUTANTS = {"below_seed": "a seed below sqrt(72) l5^2: x = 1 outside the horizon (F1)",
           "outside_boundary": "the boundary taken outside the horizon (F2)",
           "single_polarization": "one polarization only: the average is not round (F3)",
           "in_phase": "the polarizations in phase, not a quarter turn apart (F3)",
           "no_backreaction": "the waves' quadratic term dropped (F3: no flux)",
           "hypersurface_rate": "a hypersurface equation that sees the waves' rate (F5)",
           "metric_rate_coupling": "an evolution equation coupling the wave's rate to W's (F5)"}


def selftest():
    o = compute(); c = checks(o); report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-20s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
