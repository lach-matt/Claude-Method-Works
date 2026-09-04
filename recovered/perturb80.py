#!/usr/bin/env python3
"""perturb80.py -- SESSION 80, ITEM 2.  O-C1's FALSIFIER.

Step 0(ii) was ADOPTED at s79: the field is DEFINED as a GLOBAL MINIMISER of E^RHF at
fixed shell occupancies.  RULING-S79 registered the obligation and named the falsifier:
    "THE FALSIFIER IS CHEAP AND IS NOT YET RUN: perturb a CONVERGED solution and
     re-converge.  A second basin at lower energy kills the rule as stated."
The evidence held is four seeds agreeing from 52 Ha away.  s79 wrote: "THAT IS A
FOUR-START BASIN TEST.  IT IS NOT A PROOF OF A GLOBAL MINIMUM."  Seeds probe where the
iteration STARTS.  This probes the neighbourhood of where it LANDS, which is the
different question, and the one O-C1 actually asks.

DECLARED LINES FROM THE SEALED PATH:
  H1  hfc2.HFC.seed is overridden to return a PERTURBED COPY of a stored converged
      solution instead of the numerov seed.  run2, solve_one, the field and the energy
      functional are UNTOUCHED.
  H2  THE LEVER IS VERIFIED ON EVERY RUN, NOT ONCE.  The standing methodological law
      (F54.2): an instrument that varies a parameter must DEMONSTRATE the parameter
      moves the object before any row is computed.  Each run reports dP = max over
      shells of ||P_pert - P*||_2.  amp > 0 with dP = 0 EXITS rc=4 and computes nothing.
  H3  TWO KINDS OF PERTURBATION, not one (Method 2.24).  'noise' is isotropic and
      structureless; 'mix' contaminates each shell with the next shell of the same l,
      which is the direction an RHF instability would actually lie along.  A basin that
      survives only one kind has not been tested.
  H4  THE COMPARATOR REPORTS THREE VERDICTS, and the lower-energy one is the kill.
      SAME BASIN | SECOND BASIN, LOWER -- O-C1 FALSIFIED | SECOND SOLUTION, HIGHER.

usage:  python3 perturb80.py control-return     # comparator can say SAME
        python3 perturb80.py control-differ     # comparator can say NOT SAME
        python3 perturb80.py run <kind> <amp> <rng>
        python3 perturb80.py score
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'perturb80.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S80-ITEM2-OC1.md')
PSHA = os.path.join(HERE, 'PREDICTION-S80-ITEM2-OC1.sha256')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
import numpy as np
import hfc2
from t7c_kernel import C0

E_SEALED_6D = -25694.541630577907
TOL = 1e-6                      # same-rung identity; F47.3's ~1e-5 is the mixed-rung figure


def gate_sha():
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")


class Perturbed(hfc2.HFC):
    """H1.  Starts from a stored converged solution, perturbed."""
    P0 = None
    EPS0 = None
    AMP = 0.0
    KIND = 'noise'
    RNG = 0
    DP = None

    def seed(self, qtail):
        dr = self.dr
        P = {k: v.copy() for k, v in self.P0.items()}
        eps = dict(self.EPS0)
        if self.AMP > 0:
            rng = np.random.default_rng(self.RNG)
            keys = list(P.keys())
            byl = {}
            for (n, l) in keys:
                byl.setdefault(l, []).append((n, l))
            for l in byl:
                byl[l].sort()
            for a in keys:
                if self.KIND == 'noise':
                    d = rng.standard_normal(self.npts) * np.abs(P[a])
                elif self.KIND == 'mix':
                    sib = byl[a[1]]
                    i = sib.index(a)
                    b = sib[(i + 1) % len(sib)]
                    d = P[b].copy() if b != a else rng.standard_normal(self.npts) * np.abs(P[a])
                else:
                    raise SystemExit(f"unknown kind {self.KIND}")
                nd_ = math.sqrt(float(np.sum(d * d * dr)))
                if nd_ > 0:
                    d = d / nd_
                P[a] = P[a] + self.AMP * d
                P[a] = P[a] / math.sqrt(float(np.sum(P[a] ** 2 * dr)))
        # H2: LEVER VERIFICATION, EVERY RUN
        self.DP = max(math.sqrt(float(np.sum((P[k] - self.P0[k]) ** 2 * dr))) for k in P)
        return P, eps


def converge_reference():
    import nlchain as NC
    rows = NC.load()
    cfg = NC.add(NC.cfg_from_chain(88, rows), (6, 2))
    h = hfc2.HFC(89, [tuple(t) for t in cfg], c=C0)
    E, Ec, it, eps = h.run2(beta=0.4, maxit=100)
    return h, cfg, float(E), it


def verdict(E, Eref):
    if E is None:
        return "NO CONVERGENCE"
    d = E - Eref
    if abs(d) <= TOL:
        return "SAME BASIN"
    if d < -TOL:
        return "SECOND BASIN, LOWER -- O-C1 FALSIFIED"
    return "SECOND SOLUTION, HIGHER"


def run(kind, amp, rngseed, maxit=100, tag=None):
    gate_sha()
    t0 = time.time()
    h, cfg, Eref, itref = converge_reference()
    if abs(Eref - E_SEALED_6D) > 1e-9:
        raise SystemExit(f"HALT: reference is not the sealed 6d solution: {Eref}")
    Perturbed.P0, Perturbed.EPS0 = h.P, h.eps
    Perturbed.AMP, Perturbed.KIND, Perturbed.RNG = float(amp), kind, int(rngseed)
    p = Perturbed(89, [tuple(t) for t in cfg], c=C0)
    err = None
    try:
        E, Ec, it, eps = p.run2(beta=0.4, maxit=maxit)
        E = float(E)
    except Exception as e:
        E, it = None, None
        err = type(e).__name__ + ": " + str(e)[:120]
    dp = p.DP
    if amp > 0 and (dp is None or dp < 1e-12):          # H2
        print(f"  LEVER DEAD: amp={amp} produced dP={dp}. NOTHING COMPUTED.")
        sys.exit(4)
    v = verdict(E, Eref)
    rec = dict(kind=(tag or 'question'), pert=kind, amp=float(amp), rng=int(rngseed),
               maxit=maxit, dP=(None if dp is None else round(dp, 8)),
               E_ref=Eref, E=E, dE_mHa=(None if E is None else round((E - Eref) * 1000, 6)),
               it=it, err=err, verdict=v, sec=int(time.time() - t0))
    with open(CACHE, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    print(f"  {kind:>5} amp={amp:<5} rng={rngseed}  dP={rec['dP']}  E={E}  "
          f"dE={rec['dE_mHa']} mHa  it={it}  -> {v}   {rec['sec']}s")
    if err:
        print(f"    err={err}")
    return rec


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == 'control-return':
        r = run('noise', 0.0, 0, tag='C1')
        ok = r['verdict'] == "SAME BASIN" and r['dP'] == 0.0
        print(f"  C1 zero perturbation -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'control-differ':
        r = run('noise', 0.6, 99, maxit=3, tag='C2')
        ok = r['verdict'] not in ("SAME BASIN",)
        print(f"  C2 comparator can report NOT-SAME -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'run':
        run(sys.argv[2], float(sys.argv[3]), int(sys.argv[4]))
    elif cmd == 'score':
        gate_sha()
        rows = [json.loads(l) for l in open(CACHE) if l.strip()]
        q = [r for r in rows if r['kind'] == 'question']
        print(f"  {'pert':>6} {'amp':>6} {'rng':>4} {'dP':>10} {'dE (mHa)':>12} {'it':>4}  verdict")
        low = 0
        for r in q:
            print(f"  {r['pert']:>6} {r['amp']:>6} {r['rng']:>4} {str(r['dP']):>10} "
                  f"{str(r['dE_mHa']):>12} {str(r['it']):>4}  {r['verdict']}")
            if 'FALSIFIED' in r['verdict']:
                low += 1
        print(f"\n  runs={len(q)}  lower-energy basins found={low}")
        print("  O-C1: " + ("FALSIFIED -- the adopted rule dies as stated."
                            if low else "NOT FALSIFIED BY THIS TEST. This is NOT a proof "
                                        "of global minimality and must never be quoted as one."))
