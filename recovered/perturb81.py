#!/usr/bin/env python3
"""perturb81.py -- SESSION 81, ITEM 2.  F80.3's REPAIR, AND O-C1's FALSIFIER AT A SECOND
CONFIGURATION.

F80.3: perturb80's TOL was 1e-6 Ha, set by choice, and below the 0.0345 mHa stopping
resolution F80.2 measured in the same session.  It labelled ordinary convergence scatter
"SECOND BASIN, LOWER -- O-C1 FALSIFIED" three times.  M's order: set TOL from the MEASURED
floor, not chosen, and extend the falsifier to a second configuration.

DECLARED, AND J2 IS THE REAL REPAIR:
  J1  **TOL IS MEASURED, NEVER CHOSEN, AND IT IS MEASURED PER CONFIGURATION, EVERY RUN.**
      TOL := the total drop of the reference's own restart-to-stationarity ladder.  That
      drop IS the distance the eigenvalue-drift stopping test leaves on the table at this
      point in this field; a difference smaller than it is not resolvable by this scheme.
      No multiplier is applied.  A chosen multiplier is what F80.3 was about.
  J2  **BOTH SIDES ARE RESTARTED TO STATIONARITY BEFORE THEY ARE COMPARED.**  s80
      restarted the REFERENCE only.  The perturbed run stops on the same eigenvalue-drift
      test and therefore lands ~0.03 mHa ABOVE its own floor too, so s80 compared a
      stationary point against a still-descending one and the comparison carried a bias
      of the size of the effect it was looking for.  Stationary-to-stationary removes it.
  J3  THE LEVER IS VERIFIED ON EVERY RUN (H2, the F54.2 law).  amp > 0 with dP = 0 exits
      rc=4 and computes nothing.
  J4  TWO KINDS OF PERTURBATION, carried from H3 unchanged.
  J5  THE CONFIGURATION IS AN ARGUMENT.  cfg88+6d (rank 1, s80's) and cfg88+7p (rank 2).

usage:  python3 perturb81.py stationary <ch>       # measure TOL for that configuration
        python3 perturb81.py control-return <ch>   # comparator can say SAME
        python3 perturb81.py control-differ <ch>   # comparator can say NOT-SAME
        python3 perturb81.py run <ch> <kind> <amp> <rng>
        python3 perturb81.py score <ch>
        python3 perturb81.py relabel               # F80.3: s80's rows at the measured TOL
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'perturb81.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S81-ITEM2-TOL.md')
PSHA = os.path.join(HERE, 'PREDICTION-S81-ITEM2-TOL.sha256')
S80LOG = os.path.join(os.path.dirname(HERE), 'pack80', 'perturb80.jsonl')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
import numpy as np
import hfc2
from t7c_kernel import C0

ZZ = 89
NL = {'6d': (6, 2), '7p': (7, 1)}
SEALED = {'6d': -25694.541630577907, '7p': -25694.509298091765}
ESTAT = 1e-10
NREST = 12
F802 = 0.034493       # mHa. F80.2's measured drop at Z=89 6d. Comparand, not a setting.


def gate_sha():
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")


class Perturbed(hfc2.HFC):
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
        self.DP = max(math.sqrt(float(np.sum((P[k] - self.P0[k]) ** 2 * dr))) for k in P)
        return P, eps


def cfg_of(ch):
    import nlchain as NC
    rows = NC.load()
    return [tuple(t) for t in NC.add(NC.cfg_from_chain(88, rows), NL[ch])]


def stationarise(h, cfg, E):
    """J2.  Restart from own converged orbitals until the ENERGY stops moving."""
    ladder = [float(E)]
    for k in range(NREST):
        Perturbed.P0, Perturbed.EPS0 = h.P, h.eps
        Perturbed.AMP, Perturbed.KIND, Perturbed.RNG = 0.0, 'noise', 0
        h2 = Perturbed(ZZ, cfg, c=C0)
        E2, _, it2, _ = h2.run2(beta=0.4, maxit=100)
        ladder.append(float(E2))
        h = h2
        done = abs(float(E2) - E) < ESTAT
        E = float(E2)
        if done:
            break
    return h, float(E), ladder


REF = {}


def reference(ch):
    """The stationary reference AND the measured TOL for this configuration (J1)."""
    if ch in REF:
        return REF[ch]
    cfg = cfg_of(ch)
    Perturbed.P0 = None
    h = hfc2.HFC(ZZ, cfg, c=C0)
    E, _, it, _ = h.run2(beta=0.4, maxit=100)
    if abs(float(E) - SEALED[ch]) > 1e-9:
        raise SystemExit(f"HALT: first pass is not the sealed {ch} solution: {E!r}")
    h, Eref, ladder = stationarise(h, cfg, float(E))
    tol = abs(ladder[0] - ladder[-1]) * 1e-3          # Ha; J1, measured
    Perturbed.P0 = None
    REF[ch] = dict(h=h, cfg=cfg, Eref=Eref, ladder=ladder, TOL=tol,
                   drop_mHa=round((ladder[-1] - ladder[0]) * 1000, 6))
    return REF[ch]


def verdict(E, Eref, TOL):
    if E is None:
        return "NO CONVERGENCE"
    d = E - Eref
    if abs(d) <= TOL:
        return "SAME BASIN"
    if d < -TOL:
        return "SECOND BASIN, LOWER -- O-C1 FALSIFIED"
    return "SECOND SOLUTION, HIGHER"


def run(ch, kind, amp, rngseed, maxit=100, tag=None, stationary=True):
    gate_sha()
    t0 = time.time()
    R = reference(ch)
    h, cfg, Eref, TOL = R['h'], R['cfg'], R['Eref'], R['TOL']
    Perturbed.P0, Perturbed.EPS0 = h.P, h.eps
    Perturbed.AMP, Perturbed.KIND, Perturbed.RNG = float(amp), kind, int(rngseed)
    p = Perturbed(ZZ, cfg, c=C0)
    err, ladder2 = None, []
    try:
        E, Ec, it, eps = p.run2(beta=0.4, maxit=maxit)
        E = float(E)
        E_land = E
        if stationary:                                # J2
            p, E, ladder2 = stationarise(p, cfg, E)
    except Exception as e:
        E, it, E_land = None, None, None
        err = type(e).__name__ + ": " + str(e)[:120]
    dp = p.DP
    if amp > 0 and (dp is None or dp < 1e-12):        # J3
        print(f"  LEVER DEAD: amp={amp} produced dP={dp}. NOTHING COMPUTED.")
        sys.exit(4)
    v = verdict(E, Eref, TOL)
    rec = dict(kind=(tag or 'question'), ch=ch, pert=kind, amp=float(amp), rng=int(rngseed),
               maxit=maxit, dP=(None if dp is None else round(dp, 8)),
               E_ref=Eref, E=E, E_landing=E_land,
               dE_mHa=(None if E is None else round((E - Eref) * 1000, 6)),
               dE_landing_mHa=(None if E_land is None else round((E_land - Eref) * 1000, 6)),
               j2_gain_mHa=(None if (E is None or E_land is None) else round((E - E_land) * 1000, 6)),
               it=it, err=err, verdict=v, TOL_mHa=round(TOL * 1000, 6),
               ref_drop_mHa=R['drop_mHa'], n_rest2=len(ladder2), sec=int(time.time() - t0))
    with open(CACHE, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    print(f"  {ch} {kind:>5} amp={amp:<5} rng={rngseed} dP={rec['dP']} "
          f"dE_land={rec['dE_landing_mHa']} -> dE={rec['dE_mHa']} mHa (TOL={rec['TOL_mHa']}) "
          f"it={it} -> {v}  {rec['sec']}s")
    if err:
        print(f"    err={err}")
    return rec


def relabel():
    """F80.3.  s80's TEN ROWS, RE-LABELLED AT THE MEASURED TOL. No re-run: the raw dE
    are recorded in pack80/perturb80.jsonl and the floor is a property of the scheme."""
    gate_sha()
    rows = [json.loads(l) for l in open(S80LOG) if l.strip()]
    q = [r for r in rows if r['kind'] == 'question']
    TOL = F802 / 1000.0
    print(f"  s80's rows re-labelled at TOL = {F802} mHa (F80.2's MEASURED drop, Z=89 6d)")
    print(f"  {'pert':>6} {'amp':>6} {'dE (mHa)':>12}  {'s80 label':<38} -> re-label")
    out = []
    for r in q:
        old = r['verdict']
        new = verdict(r['E'], r['E_ref'], TOL) if r['E'] is not None else "NO STARTING POINT"
        out.append(dict(pert=r['pert'], amp=r['amp'], dE_mHa=r['dE_mHa'], s80=old, s81=new))
        print(f"  {r['pert']:>6} {r['amp']:>6} {str(r['dE_mHa']):>12}  {old[:36]:<38} -> {new}")
    json.dump(dict(TOL_mHa=F802, rows=out),
              open(os.path.join(HERE, 'perturb81_relabel.json'), 'w'), indent=1)
    n = sum(1 for r in out if 'FALSIFIED' in r['s81'])
    print(f"\n  rows={len(out)}  lower-energy basins AT THE MEASURED FLOOR = {n}")
    return out


def score(ch):
    gate_sha()
    rows = [json.loads(l) for l in open(CACHE) if l.strip()]
    q = [r for r in rows if r['kind'] == 'question' and r['ch'] == ch]
    print(f"  {'pert':>6} {'amp':>6} {'dP':>9} {'land':>10} {'stat':>10} {'gain':>9}  verdict")
    low = 0
    for r in q:
        print(f"  {r['pert']:>6} {r['amp']:>6} {str(r['dP']):>9} "
              f"{str(r['dE_landing_mHa']):>10} {str(r['dE_mHa']):>10} "
              f"{str(r['j2_gain_mHa']):>9}  {r['verdict']}")
        if 'FALSIFIED' in r['verdict']:
            low += 1
    if q:
        d = [r['dE_mHa'] for r in q if r['dE_mHa'] is not None]
        dl = [r['dE_landing_mHa'] for r in q if r['dE_landing_mHa'] is not None]
        print(f"\n  {ch}: runs={len(q)} converged={len(d)} TOL={q[0]['TOL_mHa']} mHa")
        if d:
            print(f"  stationary spread {min(d):+.6f} .. {max(d):+.6f} mHa "
                  f"(range {max(d)-min(d):.6f})")
            print(f"  landing    spread {min(dl):+.6f} .. {max(dl):+.6f} mHa "
                  f"(range {max(dl)-min(dl):.6f})")
        print(f"  lower-energy basins found = {low}")
    return q


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == 'stationary':
        gate_sha()
        ch = sys.argv[2]
        R = reference(ch)
        print(f"  restart ladder, Z=89 {ch}, rung 0:")
        for i, v in enumerate(R['ladder']):
            print(f"    pass {i}  E={v!r}   {(v-R['ladder'][0])*1000:+.6f} mHa")
        print(f"  STATIONARY after {len(R['ladder'])-1} restarts.  "
              f"TOTAL DROP = {R['drop_mHa']:.6f} mHa")
        print(f"  **TOL := {R['drop_mHa']:.6f} mHa, MEASURED (J1).  "
              f"F80.2's Z=89 6d figure was {F802} mHa.**")
    elif cmd == 'control-return':
        r = run(sys.argv[2], 'noise', 0.0, 0, tag='C1')
        ok = r['verdict'] == "SAME BASIN" and r['dP'] == 0.0
        print(f"  C1 zero perturbation -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'control-differ':
        r = run(sys.argv[2], 'noise', 0.6, 99, maxit=3, tag='C2', stationary=False)
        ok = r['verdict'] not in ("SAME BASIN",)
        print(f"  C2 comparator can report NOT-SAME -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'grid':
        ch = sys.argv[2]
        for k, a, g in [('noise', 0.02, 1), ('noise', 0.10, 1), ('noise', 0.30, 1),
                        ('noise', 0.60, 1), ('mix', 0.02, 0), ('mix', 0.10, 0)]:
            run(ch, k, a, g)
    elif cmd == 'run':
        run(sys.argv[2], sys.argv[3], float(sys.argv[4]), int(sys.argv[5]))
    elif cmd == 'relabel':
        relabel()
    elif cmd == 'score':
        score(sys.argv[2])
    else:
        raise SystemExit(f"unknown cmd {cmd}")
