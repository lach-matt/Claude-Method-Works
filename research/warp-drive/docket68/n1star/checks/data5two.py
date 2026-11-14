#!/usr/bin/env python3
"""data5two: data5.py's S2 with two families on Sigma (FAMILIES5 4i, D566).

The record's Theorem D solves the constraints for the approximant's slice data by an outward iteration whose
linearisation (data5.py S2) has no coefficient of order 1/lam: the wave W_TT is traceless on the spheres and its phase v
is null. With two families the slice data are g0 + lam (W_in(s) + W_out(s2)), s = v/lam, s2 = u/lam, on Sigma = {tau =
tau0}, where v = tau0 + r and u = tau0 - r, so that d_r -> d_r + d_v + lam^-1 d_s - d_u - lam^-1 d_s2 and d_tau -> d_v +
lam^-1 d_s + d_u + lam^-1 d_s2. W_out is W_TT's angular form with phase s2 and an envelope E2(u): purely angular, so
W_out(l, .) = 0 for every radial null l, and traceless on the spheres. This reuses data5.py's slice data, constraint map
and Racz parametrisation (h = a dr dr, Q = w Pi + q (dth dr + dr dth)) by replacing its derivative along Sigma and its
wave.

  T1 (exact) on the flat background (mu = 0, where u and v are both null), with both families: the linearised
     constraints (J_r, J_th, rho) in (a, w, q) have no coefficient of order 1/lam.
  T2 (exact) the same with the outgoing family alone (the ingoing alone is data5's S2 at mu = 0).
  T3 (exact) the outgoing family alone with a phase that is not null, s2 = (tau - r/2)/lam (slowness 1/2, crest speed
     2; corrected D568, verifier 247): still no 1/lam coefficient.
  T4 (exact) the outgoing family alone with u = tau - r on Vaidya (mu != 0), where du is not null (g0^-1(du, du) =
     -4mu/r^2 in the (v, r) form): still none. So S2's cancellation does not use the phase's nullness; it uses W's
     tracelessness on the spheres, as data5's mutant trace_W shows for the ingoing family.
  T5 (control, exact) an outgoing wave with an oscillating trace on the spheres (data5's trace_W for the outgoing
     family), flat background: a 1/lam coefficient appears.
  T6 (exact; D568, verifier 247's P4) both families on Vaidya, u = tau - r: none.
  T7 (exact; D568, verifier 247's P6) both families on the static background mu = 1/2 with both phases null: the
     outgoing phase u = tau - int c dr with c(r) = 2/f - 1, f = 1 - mu/r^2, the root of g0^-1(du, du) = 0 with d_tau u
     = 1 (checked here); none. Static only: for mu' != 0 the outgoing eikonal fixes d_tau(d_tau u) on Sigma, which Dt
     sets to zero, so the dynamic outgoing null phase is outside this code (verifier 247).
  T8 (control, exact; verifier 247's P7) T7's outgoing wave with an oscillating trace: a 1/lam coefficient appears.
  T9, T10 (exact; D579) both families with each family's second harmonic chi on Sigma, data5's S4 for two families
     (chi dv dv for the ingoing, chi_2 du du for the outgoing, which enters the shift g_taur with the opposite sign):
     no 1/lam coefficient on the flat background (T9) and on Vaidya with u = tau - r (T10).
  T11 (exact; D579) data5's S6 for two families: with both families and chi, the order-0 coefficients of the
     principal terms ((J_r, J_th) in (w, q), rho in a) equal the background's, flat and Vaidya.

The 1/lam coefficients of the linearisation are linear in the waves (they come from lam^-1 d_s^2 of lam W), so each
family's cancellation is the single-family one and the mixed terms enter at order lam^0 only; T1-T2 check this on flat
space, T3-T4 that the phase need not be null for it (D566), T6-T7 both families off flat space (D568). The waves carry
no chi in T1-T8; T9-T11 add each family's (D579). Labels: computed (exact, sympy, data5.py's
normal form).

Run: python3 checks/data5two.py   (T1-T9 about twenty minutes; T10-T11 about five and a half hours, 331 minutes
on the run saved as checks/data5two.out; --t10t computes T10-T11 by exact truncation in about an hour)
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import data5 as d5                                                                  # noqa: E402

u, s2 = sp.symbols("u s2", real=True)
E2 = sp.Function("E2")(u)
SPEED = {"c": 1}                    # the outgoing phase (tau - c r)/lam on Sigma; c = 1 is null on flat space


def D(e, k):
    if k == 0:
        c = SPEED["c"]
        return (sp.diff(e, r_) + sp.diff(e, d5.v) + sp.diff(e, d5.s) * d5.IL - c * sp.diff(e, u)
                - c * sp.diff(e, s2) * d5.IL)
    if k == 1:
        return sp.diff(e, d5.th)
    return sp.Integer(0)


def Dt(e):
    return sp.diff(e, d5.v) + sp.diff(e, d5.s) * d5.IL + sp.diff(e, u) + sp.diff(e, s2) * d5.IL


r_ = d5.r
WHICH = {"in": True, "out": True}


def wave(with_w=True, with_chi=False):
    C, S_, A, Hf = d5.C, d5.S_, d5.A, d5.Hf
    y3 = r_**sp.Rational(-3, 2)
    comp = [0, 0, 0]
    for on, env, ph in ((WHICH["in"], d5.Ef, d5.s), (WHICH["out"], E2, s2)):
        if not (with_w and on):
            continue
        if ph is s2 and WHICH.get("trace_out"):
            F = A * env * Hf * y3 * sp.cos(ph)
            for i, x in enumerate((r_**2 * F, r_**2 * C**2 * F, r_**2 * S_**2 * F)):
                comp[i] += x
            continue
        a1 = A * env * Hf * y3 * (2 * C**2 * sp.cos(ph) - S_**2 * sp.sin(ph)) / 3
        a2 = A * env * Hf * y3 * (2 * S_**2 * sp.sin(ph) - C**2 * sp.cos(ph)) / 3
        for i, x in enumerate((-2 * r_**2 * (a1 + a2), 2 * r_**2 * C**2 * a1, 2 * r_**2 * S_**2 * a2)):
            comp[i] += x
    # D579: each family's second harmonic chi, data5's form, chi dv dv for the ingoing and chi_2 du du for the outgoing
    ch = A * d5.Ef * Hf * y3 * sp.cos(2 * d5.s) if (with_w and with_chi and WHICH["in"]) else 0
    CHI["out"] = A * E2 * Hf * y3 * sp.cos(2 * s2) if (with_w and with_chi and WHICH["out"]) else 0
    return comp, ch


CHI = {"out": 0}


def slice_data2(with_w=True, with_chi=False):
    """data5's slice_data with chi_2 du du added: du = dtau - dr on Sigma, so chi_2 enters g_tautau, g_rr with + and the
    shift g_taur with - (chi dv dv enters all three with +)"""
    trunc, lam, mu, C, S_ = d5.trunc, d5.lam, d5.mu, d5.C, d5.S_
    Wa, ch = d5.wave(with_w, with_chi)
    ch2 = CHI["out"]
    m = mu / r_**2
    gtt = -1 + m + lam * (ch + ch2)
    btr = m + lam * (ch - ch2)
    gam = sp.diag(1 + m + lam * (ch + ch2), r_**2 + lam * Wa[0], r_**2 * C**2 + lam * Wa[1], r_**2 * S_**2 + lam * Wa[2])
    gi = sp.zeros(4)
    for i in range(4):
        g0_, d_ = gam[i, i].subs(lam, 0), gam[i, i] - gam[i, i].subs(lam, 0)
        full = 1 / g0_ - d_ / g0_**2 + d_**2 / g0_**3
        MINORD["gi"] = min(MINORD.get("gi", 0), minord(full))
        MINORD["gam"] = min(MINORD.get("gam", 0), minord(gam[i, i]))
        gi[i, i] = trunc(full, TOPS["gi"])
    beta = [btr, 0, 0, 0]
    MINORD["beta"] = min(MINORD.get("beta", 0), minord(btr))
    N2full = -gtt + gi[0, 0] * btr**2
    MINORD["N2"] = min(MINORD.get("N2", 0), minord(N2full))
    N2 = trunc(N2full, TOPS["N2"])
    N20 = N2.subs(lam, 0)
    dl = trunc((N2 - N20) / (2 * N20), TOPS["dl"])
    Ninv = (1 - dl + sp.Rational(3, 2) * dl**2) / sp.sqrt(N20)
    G = d5.christoffel(gam, gi)
    K = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            lie = d5.D(beta[j], i) + d5.D(beta[i], j) - 2 * sum(G[k][i][j] * beta[k] for k in range(4))
            Kf = sp.expand((d5.Dt(gam[i, j]) - lie) * Ninv / 2)
            MINORD["K"] = min(MINORD.get("K", 0), minord(Kf))
            K[i, j] = trunc(Kf, TOPS["K"])
    return gam, gi, K


# D595: the truncations of slice_data2. TOPS is the full pipeline's (D579). The constraints are polynomial in gi, the
# Christoffel symbols G = gi D gamma, K and their D-derivatives, D lowers the order in lam by at most one (lam^-1 d_s),
# and gamma, gi, beta, N2 and K have no negative order (MINORD records it, computed). So the lam^-1 coefficients of the
# linearisation are exact with gi and K kept to order 0 and N^-1 to its background value (TOPS_10: J needs gi_0 (D K)_-1
# and D(trK)_-1, so K mod lam; rho needs gi_0 (D G)_-1, so G mod lam, gi_0 and gamma mod lam^2, which gamma is
# exactly), and the order-0 principal coefficients of data5's S6 with gi to order 1 (TOPS_11: rho's a_r coefficient
# takes (D gi)_0 and G_0; no named coefficient takes K). --t10t checks both against the full pipeline exactly.
TOPS = {"gi": 2, "N2": 2, "dl": 1, "K": 1}
TOPS_10 = {"gi": 0, "N2": 0, "dl": 0, "K": 0}
TOPS_11 = {"gi": 1, "N2": 0, "dl": 0, "K": 0}
MINORD = {}


def minord(e):
    o = d5.orders(e)
    return min(o) if o else 0


def canonical2(e):
    """data5's normal form, with the outgoing envelope's jets and phase made symbols first"""
    z2 = sp.Symbol("z2", nonzero=True)
    x = e
    for k in (3, 2, 1):
        x = x.subs(sp.Derivative(E2, (u, k)), sp.Symbol("f%d" % k))
    x = x.subs(E2, sp.Symbol("f0"))
    x = sp.expand_trig(x.rewrite(sp.sin).rewrite(sp.cos))
    x = x.subs({sp.cos(s2): (z2 + 1 / z2) / 2, sp.sin(s2): (z2 - 1 / z2) / (2 * sp.I)})
    return d5.canonical(x)


def has_inverse(lin):
    for x in lin:
        for k_, c_ in d5.orders(d5.jet(x)[0]).items():
            if k_ < 0 and canonical2(c_) != 0:
                return True
    return False


MU0 = d5.mu


SLICE0 = d5.slice_data
NAMES = (("w_r", "w_t", "q_r", "q_t"), ("w_r", "w_t", "q_r", "q_t"), ("a_rr", "a_rt", "a_r", "a_tt"))


def principal(lin):
    """data5's S6: the order-0 coefficients of the principal terms ((J_r, J_th) in (w, q), rho in a)"""
    g = {str(v_): v_ for v_ in d5.jet(sp.Integer(0))[1].values()}
    return [sp.expand(d5.jet(d5.coeff(x, 0))[0]).coeff(g[nm]) for x, nms in zip(lin, NAMES) for nm in nms]


def run_chi(flat):
    """D579: both families with chi on Sigma; returns (a 1/lam coefficient?, the principal coefficients equal the
    background's?)"""
    d5.D, d5.Dt, d5.wave, d5.slice_data = D, Dt, wave, slice_data2
    SPEED["c"] = 1
    WHICH.update({"in": True, "out": True, "trace_out": False})
    d5.mu = sp.Integer(0) if flat else MU0
    try:
        lin, _ = d5.perturbed(True, True)
        lin0, _ = d5.perturbed(False, False)
    finally:
        d5.mu = MU0
        d5.slice_data = SLICE0
        CHI["out"] = 0
    same = all(canonical2(sp.expand(x - y)) == 0 for x, y in zip(principal(lin), principal(lin0)))
    return has_inverse(lin), same


def run(flat, c, which, static=None):
    d5.D, d5.Dt, d5.wave = D, Dt, wave
    SPEED["c"] = c
    WHICH.update(which)
    d5.mu = sp.Integer(0) if flat else MU0
    lin, _ = d5.perturbed(True)
    d5.mu = MU0                     # data5's normal form substitutes for mu, so it must be the function again
    if static is not None:          # mu(v) -> a constant after the linearisation (verifier 247's probes)
        q_ = sp.Symbol("q_")
        lin = [sp.expand(x.subs(MU0.func, sp.Lambda(q_, static)).doit()) for x in lin]
    return has_inverse(lin)


def run_out_chi(trace):
    """D592: the outgoing family alone with chi_2 du du on Vaidya, u = tau - r; with trace, an oscillating trace in its
    W (the control); returns whether a 1/lam coefficient appears"""
    d5.D, d5.Dt, d5.wave, d5.slice_data = D, Dt, wave, slice_data2
    SPEED["c"] = 1
    WHICH.update({"in": False, "out": True, "trace_out": trace})
    d5.mu = MU0
    try:
        lin, _ = d5.perturbed(True, True)
    finally:
        d5.slice_data = SLICE0
        CHI["out"] = 0
        WHICH["trace_out"] = False
    return has_inverse(lin)


def t10b():
    """--t10b (D592): T10 by its single-wave parts. The 1/lam coefficients are linear in the waves (FAMILIES5 4i), the
    ingoing W_TT and chi dv dv on Vaidya are data5.py S2 and S4, the outgoing W_TT is T4/T6; this is the last part, the
    outgoing chi_2 du du alone, with an oscillating trace as the control (about half an hour)"""
    a = run_out_chi(False)
    print("  T10b: the outgoing family alone with chi_2 du du on Vaidya, u = tau - r: a 1/lam coefficient: %s" % a,
          flush=True)
    b = run_out_chi(True)
    print("  T10b (control): the same with an oscillating trace: a 1/lam coefficient: %s" % b, flush=True)
    ok = (not a) and b
    print("T10b", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ok = {}
    t1 = run(True, 1, {"in": True, "out": True})
    ok['T1'] = not t1
    print('  T1: flat background, both families, null phases: a 1/lam coefficient: %s' % t1, flush=True)
    t2 = run(True, 1, {"in": False, "out": True})
    ok['T2'] = not t2
    print('  T2: flat background, the outgoing family alone: a 1/lam coefficient: %s' % t2, flush=True)
    t3 = run(True, sp.Rational(1, 2), {"in": False, "out": True})
    ok['T3'] = not t3
    print('  T3: outgoing phase of slowness 1/2 (crest speed 2), not null: a 1/lam coefficient: %s' % t3, flush=True)
    t4 = run(False, 1, {"in": False, "out": True})
    ok['T4'] = not t4
    print('  T4: u = tau - r on Vaidya, not null there: a 1/lam coefficient: %s' % t4, flush=True)
    t5 = run(True, 1, {"in": False, "out": True, "trace_out": True})
    WHICH["trace_out"] = False
    ok['T5'] = t5
    print('  T5 (control): an outgoing wave with an oscillating trace: a 1/lam coefficient: %s' % t5, flush=True)
    t6 = run(False, 1, {"in": True, "out": True})
    ok['T6'] = not t6
    print('  T6: both families on Vaidya, u = tau - r: a 1/lam coefficient: %s' % t6, flush=True)
    M = sp.Rational(1, 2)
    cphys = 2 / (1 - M / r_**2) - 1
    m_ = M / r_**2                  # (tau, r) block of g0 = eta + (mu/r^2) dv dv, and its inverse
    gi = sp.Matrix([[-1 + m_, m_], [m_, 1 + m_]]).inv()
    null = sp.simplify((sp.Matrix([[1, -cphys]]) * gi * sp.Matrix([1, -cphys]))[0]) == 0
    t7 = run(False, cphys, {"in": True, "out": True}, static=M)
    ok['T7'] = null and not t7
    print('  T7: both families, static mu = 1/2, both phases null (outgoing c(r) = 2/f - 1, null: %s): a 1/lam '
          'coefficient: %s' % (null, t7), flush=True)
    t8 = run(False, cphys, {"in": False, "out": True, "trace_out": True}, static=M)
    WHICH["trace_out"] = False
    ok['T8'] = t8
    print('  T8 (control): T7\'s outgoing wave with an oscillating trace: a 1/lam coefficient: %s' % t8, flush=True)
    t9, p9 = run_chi(True)
    ok['T9'] = not t9
    print('  T9: both families with chi (chi dv dv and chi_2 du du) on the flat background: a 1/lam coefficient: %s'
          % t9, flush=True)
    t10, p10 = run_chi(False)
    ok['T10'] = not t10
    print('  T10: the same on Vaidya, u = tau - r: a 1/lam coefficient: %s' % t10, flush=True)
    ok['T11'] = p9 and p10
    print('  T11: data5\'s S6 with both families and chi: the order-0 principal coefficients equal the background\'s\n'
          '       (flat %s, Vaidya %s)' % (p9, p10), flush=True)
    for k, val in ok.items():
        print(k, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


def lin_of(which, chi, tops, flat=False):
    """the linearisation of data5's constraint map at the slice data of the waves in which (with chi if chi), under the
    truncations tops"""
    d5.D, d5.Dt, d5.wave, d5.slice_data = D, Dt, wave, slice_data2
    SPEED["c"] = 1
    WHICH.update({"in": False, "out": False, "trace_out": False})
    WHICH.update(which)
    TOPS_SAVE = dict(TOPS)
    TOPS.update(tops)
    d5.mu = sp.Integer(0) if flat else MU0
    try:
        lin, _ = d5.perturbed(True, chi)
    finally:
        d5.mu = MU0
        d5.slice_data = SLICE0
        CHI["out"] = 0
        WHICH["trace_out"] = False
        TOPS.update(TOPS_SAVE)
    return lin


def neg_part(lin):
    """the lam^-1 (and lower) coefficients of each component, the unknowns' jets as symbols"""
    return [sp.expand(sum(c_ * d5.IL**(-k) for k, c_ in d5.orders(d5.jet(x)[0]).items() if k < 0)) for x in lin]


def same(xs, ys):
    return all(canonical2(sp.expand(x - y)) == 0 for x, y in zip(xs, ys))


def t10t():
    """--t10t (D595): T10 and T11 computed directly, both families and chi on Vaidya, by the exact truncations TOPS_10
    and TOPS_11, each first held against the full pipeline (TOPS) on cases where that is affordable, controls with a
    1/lam coefficient among them (about an hour)"""
    import time
    ok, t0 = {}, time.time()
    out_tr = {"out": True, "trace_out": True}
    cases = (("both families, no chi", {"in": True, "out": True}, False),
             ("the ingoing family with chi", {"in": True}, True),
             ("the outgoing family, an oscillating trace, no chi (control)", out_tr, False),
             ("the outgoing family with chi_2, an oscillating trace (control)", out_tr, True))
    agree, nonzero = [], []
    for name, wh, chi in cases:
        full = neg_part(lin_of(wh, chi, TOPS))
        cut = neg_part(lin_of(wh, chi, TOPS_10))
        a = same(full, cut)
        nz = any(canonical2(x) != 0 for x in full)
        agree.append(a)
        nonzero.append(nz)
        print("  G (%s): the lam^-1 coefficients of TOPS_10 equal the full pipeline's: %s; nonzero: %s [%.0fs]"
              % (name, a, nz, time.time() - t0), flush=True)
    ok["G10"] = all(agree) and nonzero == [False, False, True, True]
    for name, wh in (("the ingoing family with chi", {"in": True}), ("the outgoing family with chi_2", {"out": True})):
        a = same(principal(lin_of(wh, True, TOPS)), principal(lin_of(wh, True, TOPS_11)))
        agree.append(a)
        ok.setdefault("G11", True)
        ok["G11"] = ok["G11"] and a
        print("  G (%s): the order-0 principal coefficients of TOPS_11 equal the full pipeline's: %s [%.0fs]"
              % (name, a, time.time() - t0), flush=True)
    MINORD.clear()
    both = {"in": True, "out": True}
    t10 = neg_part(lin_of(both, True, TOPS_10))
    ok["T10t"] = all(canonical2(x) == 0 for x in t10) and min(MINORD.values()) >= 0
    print("  T10t: both families with chi on Vaidya, u = tau - r: a 1/lam coefficient: %s; least orders of gamma, gi, "
          "beta, N^2, K: %s [%.0fs]" % (not ok["T10t"], dict(sorted(MINORD.items())), time.time() - t0), flush=True)
    ctl = neg_part(lin_of({"in": True, "out": True, "trace_out": True}, True, TOPS_10))
    parts = [sp.expand(x + y) for x, y in zip(neg_part(lin_of({"in": True}, True, TOPS_10)),
                                                neg_part(lin_of(out_tr, True, TOPS_10)))]
    ok["T10t-control"] = any(canonical2(x) != 0 for x in ctl) and same(ctl, parts)
    print("  T10t (control): the outgoing wave with an oscillating trace: a 1/lam coefficient: %s, and it is the sum of "
          "the two families' own: %s [%.0fs]" % (any(canonical2(x) != 0 for x in ctl), same(ctl, parts),
                                               time.time() - t0), flush=True)
    p = principal(lin_of(both, True, TOPS_11))
    p0 = principal(lin_of({}, False, TOPS_11))
    ok["T11t"] = same(p, p0)
    print("  T11t: both families with chi on Vaidya: the order-0 principal coefficients equal the background's: %s "
          "[%.0fs]" % (ok["T11t"], time.time() - t0), flush=True)
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(t10b() if '--t10b' in sys.argv else t10t() if '--t10t' in sys.argv else main())
