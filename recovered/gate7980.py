#!/usr/bin/env python3
"""gate7980.py -- s44, M's ruling (b) on F44.1. THE DRIVER GATES 79 AND 80 NEVER HAD.

F44.1: gate 79 was specified as `python3 t7e_probe.py`. That module has no __main__ block,
so it imports its dependencies and exits 0 having compared nothing -- a pass that was never
a check. Gate 80 named `D_of`/`run`/`CFG_CA` on `t7g_exc`, where they do not exist; they are
defined in `t7f_rep.py`. This file is the driver. It edits nothing: `t7e_probe.py`,
`t7f_rep.py` and `t7g_exc.py` are imported, never patched, so their manifest hashes and
gates 1-71 stay byte-identical (H.4).

USAGE
    python3 gate7980.py            run both gates, exit 0 iff all clauses pass
    python3 gate7980.py 79         gate 79 (PP-0) only
    python3 gate7980.py 80         gate 80 (inertness + named exception) only
    python3 gate7980.py --fail 79  can-fail: perturb the reference e by 1e-7, |de| bound must trip
    python3 gate7980.py --fail 80  can-fail: compare a deliberately NON-INERT subclass, must trip

EVERY CLAUSE CAN FAIL, AND THE FAILURE MODE IS NAMED BESIDE IT (4.6). A clause that cannot
fail is not evidence, which is the whole content of F44.1.

FILED BOUNDS (s42 FINDING-PROBE-4D, s43 bridge 6). Bounds, not values -- s42's bracket was
never filed, so the probe root is reproducible only to the gate's own tolerance, not to its
tenth decimal. That is stated in F44.1 and is not treated as a failure here.
"""
import sys, math

TOL_DE      = 1e-8        # gate 79: |probe root - parent solve_one|
TOL_LOGNRM  = 1e-6        # gate 79: |log(nrm)| at the parent's own e
D1_REF      = -0.266643   # gate 80: the s42 D1 reference
IT_REF      = [30, 35]

FAILS = []


def clause(name, ok, got, want):
    """Record one clause. Every call is capable of both outcomes."""
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %-42s got %-34s want %s" % (tag, name, got, want))
    if not ok:
        FAILS.append(name)
    return ok


# ---------------------------------------------------------------- GATE 79 (PP-0)
def gate79(perturb=0.0):
    """The probe is the parent kernel called directly. TESTED, not asserted.

    Failure mode: if make_shoot does not re-express solve_one's inner shoot verbatim,
    the root of log(nrm) drifts from the parent's eigenvalue and |de| exceeds 1e-8.
    """
    import t7e_probe as P, t7f_rep as R
    from scipy.optimize import brentq

    print("GATE 79 (PP-0) -- probe root vs parent solve_one, Z=21, l=2 n=3 (healthy channel)")
    cap = P.capture(21, R.CFG_CA + [(3, 2, 1.0)], (2, 3))
    if cap is None:
        clause("capture returns the l=2 n=3 channel", False, "None", "a capture dict")
        return
    e_parent = cap['e'] + perturb
    if perturb:
        print("  !! CAN-FAIL MODE: reference e perturbed by %+.1e" % perturb)

    sh = P.make_shoot(cap)
    f = lambda e: math.log(sh(e)['nrm'])

    # PP-0b: the probe's own shoot at the parent's e sits on the normalisation root.
    lg = f(cap['e'])
    clause("PP-0b |log(nrm)| at parent e", abs(lg) < TOL_LOGNRM,
           "%.3e" % lg, "< %.0e" % TOL_LOGNRM)

    # PP-0a: the probe's independently-found root equals the parent's eigenvalue.
    a, b = cap['e'] - 2e-6, cap['e'] + 2e-6
    if f(a) * f(b) > 0:
        clause("PP-0a bracket straddles the root", False,
               "f(a),f(b) same sign", "opposite signs")
        return
    root = brentq(f, a, b, xtol=1e-14)
    de = abs(root - e_parent)
    clause("PP-0a |probe root - parent e|", de < TOL_DE,
           "%.2e (root %.10f)" % (de, root), "< %.0e" % TOL_DE)
    clause("PP-0a node count at the root", sh(root)['nd'] == 0, sh(root)['nd'], 0)


# ---------------------------------------------------------------- GATE 80
def gate80(noninert=False):
    """t7g_exc.HFCN raises a NAMED exception where the parent raises, and is otherwise INERT.

    Failure mode: any subclass that perturbs the field returns a different D, and the
    identity clause trips. Exercised directly by --fail 80.
    """
    import t7f_rep as R, t7g_exc, hfc2, nlchain as N

    print("GATE 80 -- t7g_exc.HFCN inertness and named exception, Z=21")

    if noninert:
        class NotInert(hfc2.HFC):
            """Deliberately NOT inert: shifts every eigenvalue by 1e-4 Ha."""
            def solve_one(self, l, n, Vloc, X, e0, Pold=None):
                u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
                return u, e + 1e-4, nd, res
        under_test, label = NotInert, "NotInert (can-fail)"
        print("  !! CAN-FAIL MODE: testing a subclass that shifts e by 1e-4")
    else:
        under_test, label = t7g_exc.HFCN, "HFCN"

    a = R.D_of(under_test, (3, 2), 21)
    b = R.D_of(hfc2.HFC,   (3, 2), 21)

    clause("80a D(%s) == D(HFC)" % label, a['D'] == b['D'],
           "%.6f vs %.6f" % (a['D'], b['D']), "identical")
    clause("80a iteration counts identical", a['it'] == b['it'],
           "%s vs %s" % (a['it'], b['it']), "identical")
    clause("80a eps_ent identical", a['eps_ent'] == b['eps_ent'],
           "%.6f vs %.6f" % (a['eps_ent'], b['eps_ent']), "identical")
    clause("80a D matches the s42 D1 reference", a['D'] == D1_REF,
           "%.6f" % a['D'], "%.6f" % D1_REF)
    clause("80a it matches the s42 D1 reference", a['it'] == IT_REF,
           "%s" % a['it'], "%s" % IT_REF)

    if noninert:
        return                      # the exception half is not what --fail 80 exercises

    # 80b: the named exception, carrying channel, target and eigenvalue.
    r = R.run(t7g_exc.HFCN, N.add(R.CFG_CA, (4, 2)), 21)
    err = str(r.get('err', ''))
    clause("80b Ca+4d at Z=21 does not converge", r.get('ok') is False,
           r.get('ok'), False)
    clause("80b exception is NodeCountMismatch", "NodeCountMismatch" in err,
           err.split(':')[0], "NodeCountMismatch")
    for tok in ("4d", "nodes 0", "target 1", "e=-0.083340"):
        clause("80b message carries %r" % tok, tok in err,
               "yes" if tok in err else "no", "yes")


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    args = sys.argv[1:]
    fail = "--fail" in args
    if fail:
        args.remove("--fail")
    which = args[0] if args else "both"

    if which in ("79", "both"):
        gate79(perturb=1e-7 if (fail and which == "79") else 0.0)
    if which in ("80", "both"):
        gate80(noninert=(fail and which == "80"))

    print()
    if FAILS:
        print("GATE7980: FAIL -- %d clause(s): %s" % (len(FAILS), ", ".join(FAILS)))
        sys.exit(1)
    print("GATE7980: PASS -- all clauses")
    sys.exit(0)
