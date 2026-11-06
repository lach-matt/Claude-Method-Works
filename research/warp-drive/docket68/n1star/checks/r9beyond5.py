"""r9beyond5.py -- SETTLE-GLAM5 round 9: BEYOND5 Lemma 6.4 (iv) written out (Lemma R9.1), every inequality computed.
The record's chart (tau, x), r = |x|, v = tau + r; on v >= v_end, g0 = eta + m dv dv, g0^-1 = eta^-1 - m L0 L0,
L0 = d_tau - xhat.d_x, m = mu_end r^-2 <= 1/16 on r >= 4R; Sigma_IVP cap {r >= R_3} = {tau = F(r)}, |F'| <= 1/4 on
r >= 4R; S := Sigma_IVP cap {r >= 4R}, tau_S := F(4R), v1 := 4R + tau_S, t~ := tau - F(r),
W := {v >= v1, t~ <= 0, r >= 4R}, N := {v = v1} cap W, Zb := {v <= v1, r >= 4R}.

  B1 (exact, sympy) g0's contractions: dv null, g0^-1(dv, dtau) = -1, g0^-1(dtau, dtau) = -1 - m, g0^-1(dr, dr) = 1 - m,
     g0^-1(dtau, dr) = m; g0^-1(dt~, dt~) = -1 + F'^2 - m(1 + F')^2 <= -15/16; L0 future null and ingoing (L0(v) = 0,
     L0(r) = -1, L0(tau) = 1); d(r + F)/dr = 1 + F' >= 3/4, and t~ increases along L0's rays; beta = dr + 2 dt~ and
     alpha = dr - 2 dt~ timelike (so |dr(Y)| < 2 dt~(Y) for future causal Y). Control: at F' = -1 the slice is null.
  B2 (exact, z3 and sampled) the cone comparisons: for |g^-1 - g0^-1|_op <= e, omega := dv + 2e dtau is g-timelike and
     future, so dv(Y) >= -2e dtau(Y) for every future g-causal Y (g0^-1(omega, omega) + e |omega|_E^2 = -2e - 4m e^2 +
     4e^3 < 0); for |g - g0|_op <= e, Y_e := L0 + 2e d_tau is g-timelike and future, dv(Y_e) = 2e, dtau(Y_e) = 1 + 2e,
     dr(Y_e) = -1 (g0(Y_e, Y_e) + e |Y_e|_E^2 = -2e + 4m e^2 + 4e^3 < 0); both for 0 < e <= 1/8, 0 <= m <= 1/16 (z3,
     with the vacuity guard). Sampled: 3000 random perturbations of each kind. The sharp constant of the first, over
     the samples and the extremal direction, lies in (1/2, 2]. Controls: with 2e replaced by e/2 the extremal
     perturbation makes omega spacelike and Y_e spacelike.
  B3 (z3, linear real arithmetic) the placement, from Part VII Lemma 1.2's inequalities (tau_S >= tau0 + 1, tau_S <=
     tau_top, tau'_end >= tau_top + 1, tau'_end >= V' - q_end, V' >= tau_top + 2R + q_end + 1, q_end >= 0, 4R > a'):
     m_Omega := V' + 1 - (v1 + tau_S - tau'_end) >= q_end + 3; every point of {v <= v1 + 1/2, r >= 4R} lies in Omega'
     (tau >= tau0: tau <= tau'_end - 1/2, v + (tau - tau'_end) <= V' - 1, r >= a') or in P' (tau <= tau0, 0 < h <= kappa:
     v + h(tau) <= V'_P - 3); v1 = V'_P - kappa - (tau_S - tau0) - m_Omega <= V'_P - kappa - 1 - m_Omega. Vacuity guard:
     the hypotheses are satisfiable in each case. Control: with V' >= tau_top + 2R + q_end - 3 a counterexample exists.
  B3n (numeric) one instance of Lemma 1.2's construction (theta, r_q concrete): every point of a grid of
     {v <= v1 + 1/2, r >= 4R} is in Omega' or P'. Control: V' three below Lemma 1.2's choice leaves grid points out.
  B4 (exact and numeric) the displacement: I(tau) := 2 int_tau^tau_max eps; for the record's bound eps = C lam min(1,
     t^(-3/2)) on Zb (t = 1 + tau0 - tau), I(-oo) = 2 C lam (tau_S - tau0 + 2) (exact); for C (lam + eps_B)
     (v1 - tau)^-2 on W, int_(-oo)^(tau_max) (v1 - tau)^-2 = 1/(v1 - tau_max) (exact). On a radial model with g^-1 = g0^-1
     + eps(tau) n n^T (eight directions n, eps = 0.05 min(1, t^(-3/2))), the past g-null generator from dS stays in
     |v - v1| <= I(tau) down to tau_S - 3000; control: the extremal direction leaves |v - v1| <= I(tau)/4.
  B5 (sampled, model F = F0 + c/r, |F'| <= 1/4) W = D^-(S; g0): from 300 points of W, 40 random future causal curves
     each meet S; from 300 points outside W the ingoing null ray misses S. Perturbed (eps profile of B4, the direction
     n = dv): from points of {v >= v1 + I(tau)} random future g-causal curves meet S; from points of {v < v1 - I(tau),
     r >= 4R} the Y_e curve reaches {r = 4R} at v < v1, missing S. Control: {v >= v1 - 2, t~ <= 0} has points whose
     ingoing ray misses S.
  B6 (READ, by content) the cited lines: Part VII Lemma 1.2's inequalities (PART-VII-ASSEMBLY.md 150-159), v >= v_end + 2,
     the radiation field vanishing on {v > v_end} (124-129), Sigma_IVP = {t_KS = f} for r >= R_3 (162-163); (9.1)'s V_P,
     Lemma 9.1 (c), (P-iii) and the margin |g_app - g0| <= C lam t^(-3/2) (N1STAR-PROOF.md). Control: an altered quote is
     not found.
Labels: B1, B3, B4 (integrals) exact; B2 exact (z3) with samples; B3n, B4 (model), B5 numeric.

    python3 checks/r9beyond5.py     (20 to 90 seconds)
"""
import os
import random
import sys

import numpy as np
import sympy as sp
import z3
from sympy.calculus.util import maximum

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []
Q = sp.Rational


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------------------------------------- B1
def part_b1():
    print("B1  g0 in the record's chart, exact")
    m, fp = sp.symbols("m fp", real=True)
    etai = sp.diag(-1, 1, 1, 1, 1)
    L0 = sp.Matrix([1, -1, 0, 0, 0])                    # xhat = e_1 (the statements are O(4)-invariant)
    dv = sp.Matrix([1, 1, 0, 0, 0])
    g0i = etai - m*L0*L0.T
    g0 = etai + m*dv*dv.T                                # eta = eta^-1 as matrices
    inv_ok = sp.simplify(g0*g0i - sp.eye(5)) == sp.zeros(5, 5)
    dtau, dr = sp.Matrix([1, 0, 0, 0, 0]), sp.Matrix([0, 1, 0, 0, 0])
    c = lambda a, b: sp.expand((a.T*g0i*b)[0])
    cs = (c(dv, dv) == 0 and c(dv, dtau) == -1 and sp.simplify(c(dtau, dtau) + 1 + m) == 0
          and sp.simplify(c(dr, dr) - 1 + m) == 0 and sp.simplify(c(dtau, dr) - m) == 0)
    dtt = dtau - fp*dr
    gtt = c(dtt, dtt)
    form = sp.simplify(gtt - (-1 + fp**2 - m*(1 + fp)**2)) == 0
    If = sp.Interval(-Q(1, 4), Q(1, 4))
    mx = maximum(gtt.subs(m, 0), fp, If)
    dec = sp.simplify(sp.diff(gtt, m) + (1 + fp)**2) == 0
    l_ok = ((L0.T*g0*L0)[0] == 0 and (dv.T*L0)[0] == 0 and (dr.T*L0)[0] == -1 and (dtau.T*L0)[0] == 1)
    mono = sp.minimum(1 + fp, fp, If) == Q(3, 4)
    # along the ray of L0 (v fixed): t~ = v - r - F(r), d t~/d(-r) = 1 + F' > 0
    beta, alpha = dr + 2*dtt, dr - 2*dtt
    bb, aa = c(beta, beta), c(alpha, alpha)
    mb, ma = maximum(bb.subs(m, 0), fp, If), maximum(aa.subs(m, 0), fp, If)
    decb = (sp.simplify(sp.diff(bb, m) + (1 + 2*fp)**2) == 0      # -(L0 . beta)^2: decreasing in m
            and sp.simplify(sp.diff(aa, m) + (3 + 2*fp)**2) == 0)
    ok = inv_ok and cs and form and mx == -Q(15, 16) and dec and l_ok and mono and mb == -Q(7, 4) \
        and ma == -Q(7, 4) and decb and (beta.T*sp.Matrix([1, 0, 0, 0, 0]))[0] == 2
    check("B1 g0 g0^-1 = 1; dv null, g0^-1(dv, dtau) = -1, (dtau, dtau) = -1 - m, (dr, dr) = 1 - m, (dtau, dr) = m; "
          "g0^-1(dt~, dt~) = -1 + F'^2 - m(1 + F')^2 <= -15/16 on |F'| <= 1/4 (decreasing in m); L0 future null, "
          "ingoing; 1 + F' >= 3/4; beta = d(r + 2t~), alpha = d(r - 2t~) with g0^-1 <= -7/4 (exact)", ok,
          f"max g0^-1(dt~, dt~) = {mx}; min(1 + F') = 3/4; beta, alpha maxima {mb}, {ma}")
    ctl = sp.simplify(gtt.subs(fp, -1)) == 0
    check("B1' control: at F' = -1 the slice {t~ = 0} is null for every m (g0^-1(dt~, dt~) = 0) and r + F is constant "
          "along it", ctl and (1 + fp).subs(fp, -1) == 0)


# ---------------------------------------------------------------------------------------------------------- B2
def z3_box_negative(expr_of, guard=True):
    """for 0 < e <= 1/8, 0 <= m <= 1/16: expr < 0 (unsat of the negation), and the box non-empty (vacuity guard)"""
    e, m = z3.Reals("e m")
    box = z3.And(e > 0, e <= z3.RealVal("1/8"), m >= 0, m <= z3.RealVal("1/16"))
    s = z3.Solver()
    s.add(box, z3.Not(expr_of(e, m) < 0))
    proved = s.check() == z3.unsat
    s2 = z3.Solver()
    s2.add(box)
    return proved, s2.check() == z3.sat


def part_b2():
    print("B2  the cone comparisons, exact (z3) and sampled")
    e, m = sp.symbols("e m", positive=True)
    etai = sp.diag(-1, 1, 1, 1, 1)
    L0 = sp.Matrix([1, -1, 0, 0, 0])
    dv = sp.Matrix([1, 1, 0, 0, 0])
    dtau = sp.Matrix([1, 0, 0, 0, 0])
    g0i = etai - m*L0*L0.T
    g0 = etai + m*dv*dv.T
    om = dv + 2*e*dtau
    ex1 = sp.expand((om.T*g0i*om)[0] + e*(om.T*om)[0])
    Y = L0 + 2*e*dtau
    ex2 = sp.expand((Y.T*g0*Y)[0] + e*(Y.T*Y)[0])
    f1 = sp.simplify(ex1 - (-2*e - 4*m*e**2 + 4*e**3)) == 0
    f2 = sp.simplify(ex2 - (-2*e + 4*m*e**2 + 4*e**3)) == 0
    p1, g1 = z3_box_negative(lambda e_, m_: -2*e_ - 4*m_*e_**2 + 4*e_**3)
    p2, g2 = z3_box_negative(lambda e_, m_: -2*e_ + 4*m_*e_**2 + 4*e_**3)
    p3, _ = z3_box_negative(lambda e_, m_: -1 + m_ + e_)       # d_tau g-timelike
    p4, _ = z3_box_negative(lambda e_, m_: -1 - m_ + e_)       # dtau g-timelike
    vals = ((dv.T*Y)[0], (dtau.T*Y)[0], (sp.Matrix([0, 1, 0, 0, 0]).T*Y)[0])
    ok_vals = sp.simplify(vals[0] - 2*e) == 0 and sp.simplify(vals[1] - 1 - 2*e) == 0 and vals[2] == -1
    check("B2 g0^-1(omega, omega) + e|omega|_E^2 = -2e - 4m e^2 + 4e^3 and g0(Y_e, Y_e) + e|Y_e|_E^2 = -2e + 4m e^2 + "
          "4e^3, both < 0 on 0 < e <= 1/8, 0 <= m <= 1/16 (z3, box non-empty); d_tau and dtau stay timelike; dv(Y_e) = "
          "2e, dtau(Y_e) = 1 + 2e, dr(Y_e) = -1 (exact)", f1 and f2 and p1 and p2 and p3 and p4 and g1 and g2
          and ok_vals, f"z3: {p1}, {p2}, {p3}, {p4}; guards {g1}, {g2}")
    # sampled: |delta|_op = e on g^-1 (first) and on g (second), random point, random future causal Y
    rng = random.Random(91)
    worst1, worst2, cstar = -1e9, -1e9, 0.0
    for _ in range(3000):
        e_ = rng.uniform(1e-4, 1/8)
        m_ = rng.uniform(0, 1/16)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = x/np.linalg.norm(x)
        E = np.diag([-1.0, 1, 1, 1, 1])
        L0n = np.concatenate(([1.0], -xh))
        dvn = np.concatenate(([1.0], xh))
        g0in = E - m_*np.outer(L0n, L0n)
        g0n = E + m_*np.outer(dvn, dvn)
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        D = (A + A.T)/2
        D *= e_/max(abs(np.linalg.eigvalsh(D)))
        gi = g0in + D
        g = np.linalg.inv(gi)
        omn = dvn + 2*e_*np.array([1.0, 0, 0, 0, 0])
        worst1 = max(worst1, omn@gi@omn)
        # a random future g-null vector: Z + c d_tau with g(Z + c d_tau, .) = 0, Z spatial
        Z = np.concatenate(([0.0], np.array([rng.gauss(0, 1) for _ in range(4)])))
        T0 = np.array([1.0, 0, 0, 0, 0])
        a2, a1, a0 = T0@g@T0, 2*(T0@g@Z), Z@g@Z
        roots = np.roots([a2, a1, a0])
        cfut = max(roots.real)
        Yn = Z + cfut*T0
        if Yn[0] < 0:
            Yn = -Yn
        dvY, dtY = dvn@Yn, Yn[0]
        cstar = max(cstar, -dvY/(e_*dtY))
        H = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        H = (H + H.T)/2
        H *= e_/max(abs(np.linalg.eigvalsh(H)))
        Ye = L0n + 2*e_*T0
        worst2 = max(worst2, Ye@(g0n + H)@Ye)
    # the extremal direction for the first: delta = e dv dv^T/|dv|^2 (dv spacelike for g), in the (tau, r) plane
    def cone_min_ratio(e_, m_):
        gi2 = np.array([[-1 - m_, m_], [m_, 1 - m_]]) + e_*np.outer([1, 1], [1, 1])/2
        g2 = np.linalg.inv(gi2)
        ys = np.roots([g2[1, 1], 2*g2[0, 1], g2[0, 0]]).real     # null Y = (1, y)
        return max(-(1 + y)/e_ for y in ys)
    cext = max(cone_min_ratio(e_, m_) for e_ in (1e-3, 1e-2, 0.05, 1/8) for m_ in (0, 1/32, 1/16))
    cstar = max(cstar, cext)
    check("B2' sampled (3000): omega stays g-timelike for |g^-1 - g0^-1|_op = e and Y_e g-timelike for |g - g0|_op = e; "
          "the sharp constant c* := sup(-dv(Y)/(e dtau(Y))) over the samples and the extremal direction lies in "
          "(1/2, 2]", worst1 < 0 and worst2 < 0 and 0.5 < cstar <= 2, f"max g^-1(omega, omega) {worst1:.3e}, max "
          f"g(Y_e, Y_e) {worst2:.3e}, c* = {cstar:.4f}")
    # controls: 2e -> e/2 with the extremal perturbations
    om_c = dv + (e/2)*dtau
    ctl1 = sp.expand((om_c.T*g0i*om_c)[0] + e*(om_c.T*om_c)[0]).subs({e: Q(1, 10), m: 0})
    Y_c = L0 + (e/2)*dtau
    ctl2 = sp.expand((Y_c.T*g0*Y_c)[0] + e*(Y_c.T*Y_c)[0]).subs({e: Q(1, 10), m: 0})
    check("B2'' control: with e/2 in place of 2e, the extremal perturbations (delta = e omega omega^T/|omega|^2, H = e "
          "Y Y^T/|Y|^2) make omega and Y_e spacelike (e = 1/10, m = 0)", ctl1 > 0 and ctl2 > 0, f"{ctl1}, {ctl2}")


# ---------------------------------------------------------------------------------------------------------- B3
def placement_z3(vp_slack):
    R_, t0, tS, ttop, tpe, Vp, qe, kap, a_ = z3.Reals("R tau0 tauS tautop taupe Vp qend kappa a")
    v, r, h = z3.Reals("v r h")
    v1 = tS + 4*R_
    VPp = Vp + 1 + (tpe - t0) + kap
    mO = Vp + 1 - (v1 + tS - tpe)
    hyp = z3.And(R_ > 0, tS >= t0 + 1, tS <= ttop, tpe >= ttop + 1, tpe >= Vp - qe,
                 Vp >= ttop + 2*R_ + qe + vp_slack, qe >= 0, kap == z3.RealVal("1/2"), a_ > 0, 4*R_ > a_)
    pt = z3.And(v <= v1 + z3.RealVal("1/2"), r >= 4*R_)
    tau = v - r
    caseA = z3.And(hyp, pt, tau >= t0)
    claimA = z3.And(tau <= tpe - z3.RealVal("1/2"), v + (tau - tpe) <= Vp - 1, r >= a_)
    caseB = z3.And(hyp, pt, tau <= t0, h > 0, h <= kap)
    claimB = v + h <= VPp - 3
    res = {}
    for name, case, claim in (("m_Omega", hyp, mO >= qe + 3), ("Omega'", caseA, claimA), ("P'", caseB, claimB),
                              ("v1", hyp, z3.And(v1 == VPp - kap - (tS - t0) - mO, v1 <= VPp - kap - 1 - mO))):
        s = z3.Solver()
        s.add(case, z3.Not(claim))
        r1 = s.check()
        g = z3.Solver()
        g.add(case)
        res[name] = (r1 == z3.unsat, g.check() == z3.sat)
    return res


def part_b3():
    print("B3  the placement in Omega' cup P', from Part VII Lemma 1.2's inequalities (z3)")
    res = placement_z3(1)
    check("B3 m_Omega >= q_end + 3; {v <= v1 + 1/2, r >= 4R} cap {tau >= tau0} in Omega' (tau <= tau'_end - 1/2, "
          "v + (tau - tau'_end) <= V' - 1, r >= a'), cap {tau <= tau0} in P' (v + h <= V'_P - 3); v1 = V'_P - kappa - "
          "(tau_S - tau0) - m_Omega <= V'_P - kappa - 1 - m_Omega (each proved, hypotheses satisfiable)",
          all(p and g for p, g in res.values()), str(res))
    ctl = placement_z3(-3)
    check("B3' control: with V' >= tau_top + 2R + q_end - 3 the Omega' claim has a counterexample",
          not ctl["Omega'"][0], str(ctl["Omega'"]))


def instance(vp_shift):
    r0, R3, R = 1.0, 3.0, 4.0
    tau0, v_end, q_end, kap = 0.0, 5.0, 0.7, 0.5
    rr = np.linspace(r0, 4*R, 400)
    theta = 2.0 - 0.1*rr + 0.3*np.sin(rr)                    # psi_IVP - T_mu_end on [r0, 4R], continuous
    c0 = theta.min() - max(tau0 + 1, v_end + 2 - r0)
    tau_top = theta.max() - c0
    Vp = tau_top + 2*R + q_end + 1 + vp_shift
    rq = lambda v: q_end*min(1.0, max(v, 0.0)/v_end)        # nondecreasing, at most q_end
    vs = np.linspace(-50, Vp, 20001)
    tpe = max(vs - np.array([rq(x) for x in vs]))
    tauS = theta[-1] - c0
    v1 = 4*R + tauS
    VPp = Vp + 1 + (tpe - tau0) + kap
    return dict(R=R, tau0=tau0, v_end=v_end, kap=kap, tauS=tauS, v1=v1, tpe=tpe, Vp=Vp, VPp=VPp, a=0.4,
                tau_on_S=theta - c0, rr=rr)


def in_omega_or_p(P, v, r):
    tau = v - r
    h = P["kap"]*(1 + P["tau0"] - tau)**(-0.25) if tau <= P["tau0"] else None
    om = (P["tau0"] <= tau <= P["tpe"]) and r >= P["a"] and v + (tau - P["tpe"]) <= P["Vp"] + 1
    pp = tau <= P["tau0"] and r >= P["a"] and v + h <= P["VPp"]
    return om or pp


def part_b3n():
    print("B3n  one instance of Lemma 1.2's construction, on a grid of {v <= v1 + 1/2, r >= 4R}")
    P = instance(0.0)
    lemma12 = (P["tau_on_S"].min() >= P["tau0"] + 1 - 1e-12 and (P["tau_on_S"] + P["rr"]).min() >= P["v_end"] + 2
               - 1e-12 and P["tpe"] >= P["tau_on_S"].max() + 1)
    pts = [(P["v1"] + 0.5 - dv_, 4*P["R"] + dr_) for dv_ in np.linspace(0, 60, 121) for dr_ in
           np.linspace(0, 400, 201)]
    out = [p for p in pts if not in_omega_or_p(P, *p)]
    check("B3n Lemma 1.2's construction holds (tau >= tau0 + 1, v >= v_end + 2 on Sigma_IVP cap {r <= 4R}, tau'_end >= "
          "tau_top + 1), v1 >= v_end + 2, and all 24321 grid points lie in Omega' cup P'",
          lemma12 and P["v1"] >= P["v_end"] + 2 and not out, f"v1 = {P['v1']:.4f}, V'_P = {P['VPp']:.4f}; "
          f"outside: {len(out)}")
    Pc = instance(-3.0)
    outc = [p for p in pts if not in_omega_or_p(Pc, *p)]
    check("B3n' control: V' three below Lemma 1.2's choice leaves grid points outside Omega' cup P'", len(outc) > 0,
          f"outside: {len(outc)}")


# ---------------------------------------------------------------------------------------------------------- B4
def eps_profile(tau, tau0, e0):
    t = 1 + tau0 - tau
    return e0 if t <= 1 else e0*t**(-1.5)


def I_profile(tau, tauS, tau0, e0):
    """2 int_tau^tauS eps, exact for the profile"""
    if tau >= tau0:
        return 2*e0*(tauS - tau)
    t = 1 + tau0 - tau
    return 2*e0*((tauS - tau0) + 2*(1 - t**(-0.5)))


def metric2(n, e_, m_):
    gi2 = np.array([[-1 - m_, m_], [m_, 1 - m_]]) + e_*np.outer(n, n)
    return np.linalg.inv(gi2)


def null_slopes(g2):
    ys = np.sort(np.roots([g2[1, 1], 2*g2[0, 1], g2[0, 0]]).real)
    return ys        # (ingoing, outgoing): dr/dtau of the two future null directions


def generator(n, e0, tauS, v1, tau0, mu, steps=60000, dtau=0.05, factor=1.0):
    """the past g-null generator from dS = (tauS, r = v1 - tauS), ingoing branch, integrated to the past (RK2)"""
    tau, r = tauS, v1 - tauS
    worst = 0.0
    for _ in range(steps):
        def slope(tau_, r_):
            return null_slopes(metric2(n, eps_profile(tau_, tau0, e0), mu/r_**2))[0]
        k1 = slope(tau, r)
        k2 = slope(tau - dtau, r - dtau*k1)
        r -= dtau*(k1 + k2)/2
        tau -= dtau
        dev = abs(tau + r - v1) - factor*I_profile(tau, tauS, tau0, e0)
        worst = max(worst, dev)
    return worst


def part_b4():
    print("B4  the displacement of the null hypersurface through dS")
    tau, t0, tS, C, lam, v1, tmx = sp.symbols("tau tau0 tauS C lam v1 taumax", real=True)
    I_rec = 2*C*lam*(sp.integrate(1, (tau, t0, tS)) + sp.integrate((1 + t0 - tau)**Q(-3, 2), (tau, -sp.oo, t0)))
    ok1 = sp.simplify(I_rec - 2*C*lam*(tS - t0 + 2)) == 0
    s = sp.Symbol("s", positive=True)                       # s := v1 - tau
    I_W = sp.integrate(s**-2, (s, v1 - tmx, sp.oo), conds="none")
    ok2 = sp.simplify(I_W - 1/(v1 - tmx)) == 0
    check("B4 I(-oo) = 2 C lam (tau_S - tau0 + 2) for eps = C lam min(1, t^(-3/2)), and int_(-oo)^(tau_max) "
          "(v1 - tau)^-2 dtau = 1/(v1 - tau_max) (exact)", ok1 and ok2, f"{sp.simplify(I_rec)}; {sp.simplify(I_W)}")
    mu, tau0_, tauS_, v1_ = 1.0, 0.0, 3.0, 19.0
    dirs = [np.array([np.cos(a), np.sin(a)]) for a in np.linspace(0, np.pi, 8, endpoint=False)]
    dirs[2] = np.array([1.0, 1.0])/np.sqrt(2)               # n along dv: the extremal one
    w = [generator(n, 0.05, tauS_, v1_, tau0_, mu) for n in dirs]
    check("B4' the past g-null generator from dS, eight directions of g^-1 - g0^-1 = eps n n^T, eps = 0.05 min(1, "
          "t^(-3/2)), down to tau_S - 3000: |v - v1| <= I(tau) throughout", max(w) <= 1e-9,
          f"max(|v - v1| - I) over the eight: {max(w):.3e}")
    wc = generator(dirs[2], 0.05, tauS_, v1_, tau0_, mu, factor=0.25)
    check("B4'' control: along dv the generator leaves |v - v1| <= I(tau)/4", wc > 0, f"max excess {wc:.4f}")


# ---------------------------------------------------------------------------------------------------------- B5
def part_b5():
    print("B5  W = D^-(S; g0), sampled on a model, and the perturbed sandwich")
    R4, F0, cF, mu = 16.0, 3.0, 64.0, 1.0
    F = lambda r: F0 + cF/r                                  # |F'| = cF/r^2 <= 1/4 on r >= 16, r + F increasing
    tauS = F(R4)
    v1 = R4 + tauS
    rng = random.Random(95)
    inW = lambda tau, r: tau + r >= v1 and tau - F(r) <= 0 and r >= R4

    def ray_meets(tau, r):
        """the ingoing null ray from (tau, r): v fixed, r' decreasing from r; it meets S iff some r' in [4R, r] has
        r' + F(r') = v (r + F is increasing, so bisection on [4R, r] decides it)"""
        v = tau + r
        if r < R4 or v < v1:
            return False
        lo, hi = R4, r
        if hi + F(hi) < v:
            return False
        for _ in range(200):
            mid = (lo + hi)/2
            lo, hi = (mid, hi) if mid + F(mid) < v else (lo, mid)
        return True

    def curve_meets(tau, r, n=None, e0=0.0, tau0=0.0, dt=0.25, tol=1e-3):
        """a random future causal polygon (radial model) until t~ >= 0 (then: is v >= v1, i.e. on S?) or r < 4R"""
        for _ in range(100000):
            if tau - F(r) >= 0:
                return tau + r >= v1 - tol
            if r < R4:
                return False
            m_ = mu/r**2
            if n is None:
                yi, yo = -1.0, (1 - m_)/(1 + m_)
            else:
                yi, yo = null_slopes(metric2(n, eps_profile(tau, tau0, e0), m_))
            y = rng.uniform(yi, yo)
            tau, r = tau + dt, r + dt*y
        return None

    okW, okRay, n_in, n_tot = True, True, 0, 0
    while n_in < 300:
        r = rng.uniform(R4, R4 + 300)
        tau = rng.uniform(-150, 0) + F(r)
        if not inW(tau, r):
            continue
        n_in += 1
        okW = okW and all(curve_meets(tau, r) is True for _ in range(40))
    for _ in range(600):
        r = rng.uniform(1.0, R4 + 300)
        tau = rng.uniform(-150, 60)
        okRay = okRay and (ray_meets(tau, r) == inW(tau, r))
        n_tot += 1
    check("B5 (g0) from 300 points of W, 40 random future causal curves each meet S; at 600 random points the ingoing "
          "null ray meets S exactly when the point is in W", okW and okRay, f"{n_in} in W, {n_tot} decided")
    # perturbed: n along dv, eps = 0.05 min(1, t^(-3/2)), tau0 = tau_S - 2
    n = np.array([1.0, 1.0])/np.sqrt(2)
    e0, tau0 = 0.05, tauS - 2
    Iof = lambda tau: I_profile(min(tau, tauS), tauS, tau0, e0)
    okP, okM, k_in, k_out = True, True, 0, 0
    while k_in < 120:
        r = rng.uniform(R4, R4 + 200)
        tau = rng.uniform(F(r) - 120, F(r))
        if tau + r < v1 + Iof(tau):
            continue
        k_in += 1
        okP = okP and all(curve_meets(tau, r, n=n, e0=e0, tau0=tau0) is True for _ in range(20))
    while k_out < 120:
        r = rng.uniform(R4, R4 + 200)
        tau = rng.uniform(F(r) - 120, F(r))
        if tau + r >= v1 - Iof(tau):
            continue
        k_out += 1
        t_, r_ = tau, r                       # the Y_e curve: dtau = 1 + 2e, dr = -1, dv = 2e per unit parameter
        while r_ > R4:
            e_ = eps_profile(t_, tau0, e0)
            ds = min(0.05, r_ - R4)
            t_, r_ = t_ + ds*(1 + 2*e_), r_ - ds
            if t_ - F(r_) >= 0 and t_ + r_ >= v1:
                okM = False
                break
        okM = okM and t_ + r_ < v1
    check("B5' perturbed (n = dv, eps = 0.05 min(1, t^(-3/2))): from 120 points of {v >= v1 + I(tau), t~ <= 0} 20 "
          "random future g-causal curves each meet S; from 120 points of {v < v1 - I(tau), r >= 4R} the Y_e curve "
          "reaches r = 4R at v < v1, missing S", okP and okM, f"{k_in}, {k_out}")
    bad = 0
    for _ in range(300):
        r = rng.uniform(R4, R4 + 50)
        tau = rng.uniform(v1 - 2 - r, v1 - r)
        if tau - F(r) <= 0 and not inW(tau, r) and not ray_meets(tau, r):
            bad += 1
    check("B5'' control: {v >= v1 - 2, t~ <= 0, r >= 4R} is not in D^-(S; g0): it has points whose ingoing null ray "
          "misses S", bad > 0, f"{bad} of 300")


# ---------------------------------------------------------------------------------------------------------- B6
QUOTES = [
    ("PART-VII-ASSEMBLY.md", r"Then $\tau\ge\tau_0+1$ and $v = \tau+r\ge v_{\mathrm{end}}+2$ there,"),
    ("PART-VII-ASSEMBLY.md", r"so large that $V' := v_{\mathrm{end}}+T'\ge\tau_{\mathrm{top}}+2R+q_{\mathrm{end}}+1$"),
    ("PART-VII-ASSEMBLY.md", r"Then $\tau'_{\mathrm{end}} = \max_{v\le"),
    ("PART-VII-ASSEMBLY.md", r"V'}(v-r_q(v))\ge V'-q_{\mathrm{end}}\ge\tau_{\mathrm{top}}+1$"),
    ("PART-VII-ASSEMBLY.md", r"With $r\ge r_0>a'$, the defining"),
    ("PART-VII-ASSEMBLY.md", r"so $\mu = \mu_{\mathrm{end}}$ there, and the leading wave, proportional to the envelope, "
                             r"vanishes on"),
    ("PART-VII-ASSEMBLY.md", r"oscillating factor in every term. By induction on the stage, every oscillating profile "
                             r"vanishes on"),
    ("PART-VII-ASSEMBLY.md", r"$\{t_{\mathrm{KS}} = f(|x|)\}$ with $f := c_{\mathrm{IVP}}-T_{\mu_{\mathrm{end}}}$"),
    ("N1STAR-PROOF.md", "V_P := V + 1 + (tau_end - tau0) + kappa, so that V_P - kappa is the largest v on Sigma_tau0 "
                        "cap Omega"),
    ("N1STAR-PROOF.md", "(c) Sigma_tau0 cap P = Sigma_tau0 cap Omega."),
    ("N1STAR-PROOF.md", "- (P-iii) on P, |g_lam - g_app| <= C lam^(K-3) t^-2"),
    ("N1STAR-PROOF.md", "margin (|g_app - g0| <= C lam t^(-3/2) and t^(-3/2) <= t^(-5/4))"),
    ("N1STAR-PROOF.md", "- (P-i) g_lam = g0 on P cap {v <= v_start}: the seed, exactly;"),
]


def part_b6():
    print("B6  the cited lines, read by content")
    files = {"PART-VII-ASSEMBLY.md": os.path.join(ROOT, "proof5", "PART-VII-ASSEMBLY.md"),
             "N1STAR-PROOF.md": os.path.join(ROOT, "N1STAR-PROOF.md")}
    text = {k: open(p).read() for k, p in files.items()}
    found = [text[f].count(q) >= 1 for f, q in QUOTES]
    check(f"B6 each of the {len(QUOTES)} quoted passages occurs in the file cited", all(found),
          str([i for i, x in enumerate(found) if not x]))
    altered = text["PART-VII-ASSEMBLY.md"].count(r"$v = \tau+r\ge v_{\mathrm{end}}+3$ there,")
    check("B6' control: the altered quote 'v >= v_end + 3' is not found", altered == 0)


def main():
    for f in (part_b1, part_b2, part_b3, part_b3n, part_b4, part_b5, part_b6):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
