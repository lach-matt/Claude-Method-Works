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

The 1/lam coefficients of the linearisation are linear in the waves (they come from lam^-1 d_s^2 of lam W), so each
family's cancellation is the single-family one and the mixed terms enter at order lam^0 only; T1-T2 check this on flat
space, T3-T4 that the phase need not be null for it (D566), T6-T7 both families off flat space (D568). The waves carry
no chi here (wave() takes no chi term), so the two-family chi is untested. Labels: computed (exact, sympy, data5.py's
normal form).

Run: python3 checks/data5two.py   (about ten minutes)
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
    return comp, 0


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
    for k, val in ok.items():
        print(k, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
