"""nlguard.py -- s47: THE CONVERGENCE GUARD.  Repairs F47.2.

F47.2: hfc2.run2 breaks on dmax<tol but RETURNS UNCONDITIONALLY at maxit with no
error and no flag.  A cycling SCF therefore yields a total energy that is
indistinguishable in the record from a converged one.  D_6p(Z=54) = +0.11105 is
such a value: at beta=0.4 the SCF orbits (300 and 600 iterations give identical
energies to six decimals), and at beta=0.2 it converges in 72 iterations to
-0.08193, which is 0.19 Ha lower and lies exactly on the 52/53 trend.

WHAT THE GUARD IS ALLOWED TO DO, AND WHY.
beta is a DAMPING, not a term in the Hamiltonian.  Changing it changes the path
to the fixed point and cannot change the fixed point.  That is an argument, so it
is EVIDENCED rather than asserted: at (Z=56, +5d) the ruling beta=0.4/maxit=100
and beta=0.2/maxit=600 converge to -0.11818 and -0.11818 -- identical to five
decimals, in 35 and 74 iterations.  A converged answer here is damping-
independent, measured.  The ruling field's CHOSEN parameters are UNCHANGED: the
guard runs beta=0.4, maxit=100 FIRST and returns its value whenever it converges,
so every already-sealed converged number is reproduced bit-for-bit.

WHAT THE GUARD MAY NOT DO.
It may not return a number for a channel that never converges.  A non-converging
channel is a FAILURE and joins `fail`, beside the node-count failures.  Silently
returning the last iterate is precisely the defect being repaired, and a guard
that did that at a lower beta would only move the fault.

usage:  python3 nlguard.py gate      -> gate 84, 6 clauses  (~3 min, runs SCF)
        python3 nlguard.py gate --fail
"""
import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import hfc2 as H
from t7c_kernel import C0
H.CORR = False

# (beta, maxit) tried IN ORDER.  The first is the ruling field, unchanged.
LADDER = [(0.4, 100), (0.2, 600), (0.1, 1200)]


def run_guarded(Z, cfg, tag=""):
    """returns dict(E=, it=, beta=, rung=, conv=bool, err=None|str)

    conv=False with E=None is a FAILURE, not a value.  Callers must treat it as
    they treat a node-count failure: excluded from the ordering, recorded in fail.
    """
    last = None
    for rung, (beta, maxit) in enumerate(LADDER):
        t = time.time()
        try:
            E, _, it, eps = H.HFC(Z, [tuple(x) for x in cfg], c=C0).run2(
                beta=beta, maxit=maxit)
        except Exception as e:
            # a node-count failure is NOT a convergence failure and is not retried:
            # damping does not repair a search that found the wrong state.
            return dict(E=None, it=None, beta=beta, rung=rung, conv=False,
                        err=type(e).__name__ + ": " + str(e)[:120],
                        sec=int(time.time() - t))
        if it < maxit:
            return dict(E=float(E), it=it, beta=beta, rung=rung, conv=True,
                        err=None, sec=int(time.time() - t))
        last = (E, it, beta, maxit)
    E, it, beta, maxit = last
    return dict(E=None, it=it, beta=beta, rung=len(LADDER) - 1, conv=False,
                err=f"NoConvergence: cycled at every rung of {LADDER}",
                sec=None, last_iterate=float(E))


# ---------------------------------------------------------------- gate 84
# TWO CASES, AND THEY ARE THE TWO THAT MATTER.  One is a value the ruling field
# gets RIGHT and the guard must not disturb; one is a value the ruling field gets
# WRONG and the guard must repair.  A guard tested only on the broken case cannot
# show it is safe on the sealed chain.
GATE = dict(
    d5d56_ruling=-0.11818,   # converges at rung 0 -> sealed value reproduced
    d5d56_rung=0,
    d6p54_cycles_at_rung0=True,
    d6p54_guarded=-0.08193,  # repaired value, rung 1
    d6p54_rung=1,
    d6p54_sealed=+0.11105,   # what the unguarded instrument returned
)


def gate(fail=False):
    import nlchain as NC
    rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
    got = {}

    Z = 56; cfg = NC.cfg_from_chain(Z - 1, rows)
    ref = run_guarded(Z, cfg); ch = run_guarded(Z, NC.add(cfg, (5, 2)))
    got['d5d56_ruling'] = round(ch['E'] - ref['E'], 5)
    got['d5d56_rung'] = ch['rung']

    Z = 54; cfg = NC.cfg_from_chain(Z - 1, rows)
    ref = run_guarded(Z, cfg)
    r0 = H.HFC(Z, [tuple(x) for x in NC.add(cfg, (6, 1))], c=C0).run2(
        beta=0.4, maxit=100)
    got['d6p54_cycles_at_rung0'] = (r0[2] >= 100)
    got['d6p54_sealed'] = round(r0[0] - ref['E'], 5)
    ch = run_guarded(Z, NC.add(cfg, (6, 1)))
    got['d6p54_guarded'] = round(ch['E'] - ref['E'], 5)
    got['d6p54_rung'] = ch['rung']

    if fail:
        got['d6p54_guarded'] = round(got['d6p54_guarded'] + 1e-4, 5)
        got['d6p54_rung'] = 0
        got['d5d56_ruling'] = round(got['d5d56_ruling'] - 1e-4, 5)

    bad = 0
    for k, want in GATE.items():
        ok = got[k] == want
        bad += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {k:<22} got {got[k]}  want {want}")
    print(f"\nNLGUARD GATE 84: {'PASS -- all clauses' if not bad else f'FAIL -- {bad} clause(s)'}")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'gate':
        sys.exit(gate(fail='--fail' in sys.argv))
    print(__doc__)
