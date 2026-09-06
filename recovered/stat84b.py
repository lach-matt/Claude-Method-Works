#!/usr/bin/env python3
"""stat84b.py -- ITEM 2 DRIVER, REPAIRED AT s84.  F83.2 IS CLOSED HERE OR NOT AT ALL.

**pack83/stat84.py IS SEALED AND IS NOT EDITED.**  This is its successor.  Every
clause of the standing prediction 631d5861...a49ed538 binds unchanged; the
prediction is NOT re-filed and its sha still gates every run.

THE FAULT BEING REPAIRED (F83.2).  stat84.stationary() called nlguard.run_guarded
twice with no re-seed, so the second call repeated the same deterministic SCF and
the restart offset was +0.000000 BY CONSTRUCTION rather than by physics.

THE REPAIR, AGAINST conf82's PATTERN.  conf82 re-seeds a solve from its own
converged orbitals -- `FX.Frozen81.P0, .EPS0 = h.P, h.eps` -- via a `seed()`
override.  nlguard drives hfc2.HFC, which has no such override, so the pattern is
applied to the class the CHAIN actually uses:

    class _Seeded(H.HFC):  P0 = None; EPS0 = None; seed() falls through when P0 is None

With P0 None the class is hfc2.HFC exactly, so a first pass reproduces sealed
values bit-for-bit; with P0 set it restarts from the previous pass's orbitals.

DESIGN DECISIONS, DECLARED
  D1  **THE LEVER IS ONE FLAG ON ONE CODE PATH.**  `stationary(..., reseed=)` runs
      the same loop either way, so the DEAD and LIVE arms of the probe differ in
      the lever and in nothing else.  Two separate functions could differ anywhere.
  D2  **THE PROOF IS SITED AT HIGH Z (Z=89), NOT AT LOW Z.**  F83.2 survived its own
      passing control because at Z=2,3,4 offset=0 is also the correct physical
      answer, so a dead lever and a live one are indistinguishable there.
  D3  **THE PROBE'S OBJECT IS conf82's OBJECT** -- Z=89, cfg88+6d -- so the LIVE arm
      is scored against a number measured in another session by other machinery.
      Checked first at s84: plain hfc2.HFC with CORR=False reproduces conf82's
      first-pass energy -25694.541630578 to +0.000000 mHa, so the two instruments
      are solving the same problem and the comparison is fair.
  D4  **THE RESTART OFFSET IS SIGNED (R81.7).**  Its magnitude is a RESOLUTION.
      The stationarity test is on a magnitude, never on a signed difference.
  D5  **THE SEED IS RESET TO None AFTER EVERY CONFIGURATION.**  A leaked class
      attribute would silently seed the next configuration from the wrong orbitals.
  D6  **NO SEALED ROW IS EDITED.**  Output is a second chain, pack84/statchain.jsonl.

VERDICT, FILED BEFORE THE PROBE RUNS
  DEAD arm (no re-seed, stat84's behaviour):  offset EXACTLY +0.000000 mHa.
  LIVE arm (re-seed, conf82's pattern):       offset NON-ZERO, and within 0.002 mHa
                                              of s82's -0.034493 mHa.
  Any other outcome -- including a LIVE arm that also returns zero, or a DEAD arm
  that does not -- leaves LEVER_DEAD stamped and Item 2 blocked.  The probe writes
  its receipt to pack84/lever84.json and `run` reads the receipt, not a hand edit.

usage:  python3 stat84b.py canfail        -- gate, synthetic; runs first
        python3 stat84b.py lever          -- ITEM 0: the proof, Z=89, both arms
        python3 stat84b.py real           -- C10, real rows Z=2,3,4
        python3 stat84b.py run Z0 Z1      -- a Zeno segment of the chain
        python3 stat84b.py score          -- compare against the sealed chain
"""
import json, os, sys, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RT = os.path.join(ROOT, 'rt')
sys.path.insert(0, RT)
# the C kernels are dlopened by RELATIVE path in t7b_hf; every consumer runs from rt/.
os.chdir(RT)

PRED = os.path.join(ROOT, 'pack83', 'PREDICTION-S84-ITEM2-STATIONARY-CHAIN.md')
PRED_SHA = '631d58612ee19774dc03b7c1a6cdacc3be05d18c59ec45f0b0308951a49ed538'
LEDGER = os.path.join(HERE, 'statchain.jsonl')
RECEIPT = os.path.join(HERE, 'lever84.json')

ESTAT = 1e-10          # scheme-wide floor, Ha.  conf82's value, carried unchanged.
NREST = 20             # restart cap.  s81 V6: 12 did not exhaust ESTAT at Z=90.

# ---- the probe's object and its filed target (s82, pack82/conf82_ref.json)
PZ, PZPREV, PENT = 89, 88, (6, 2)
TARGET_OFFSET_MHA = -0.034493
TARGET_TOL_MHA = 0.002

import nlguard as NG          # sets SIC_NOCLAMP/SUBCELL, imports hfc2, CORR=False
import hfc2 as H
from t7c_kernel import C0


class _Seeded(H.HFC):
    """hfc2.HFC with conf82's restart seed.  P0 None => hfc2.HFC exactly."""
    P0 = None
    EPS0 = None

    def seed(self, qtail):
        if self.P0 is None:
            return super().seed(qtail)
        return {k: v.copy() for k, v in self.P0.items()}, dict(self.EPS0)


def gate_sha():
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if got != PRED_SHA:
        print(f"HALT rc=3: prediction sha mismatch\n  want {PRED_SHA}\n  got  {got}")
        sys.exit(3)
    return got


def lever_live():
    """Item 2 may run only against a receipt written by `lever`, never a hand edit."""
    if not os.path.exists(RECEIPT):
        return False, "no receipt: pack84/lever84.json absent"
    r = json.load(open(RECEIPT))
    return bool(r.get('LEVER_LIVE')), r.get('verdict', '')


def doubt_exercised():
    if not os.path.exists(RECEIPT):
        return False
    return bool(json.load(open(RECEIPT)).get('DOUBT_EXERCISED'))


def ledger():
    if not os.path.exists(LEDGER):
        return {}
    return {r['Z']: r for r in (json.loads(l) for l in open(LEDGER) if l.strip())}


def put(row):
    with open(LEDGER, 'a') as f:
        f.write(json.dumps(row) + '\n')
        f.flush()
        os.fsync(f.fileno())


# ------------------------------------------------------------ guarded solve
def guarded(Z, cfg, seed=None):
    """nlguard.run_guarded's rung ladder, on _Seeded so a restart can be seeded.

    Returns the guard's dict plus the converged orbitals, so the caller can seed
    the next pass.  seed is (P, eps) or None.
    """
    cfg = [tuple(x) for x in cfg]
    last = None
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        t = time.time()
        try:
            _Seeded.P0, _Seeded.EPS0 = (seed if seed else (None, None))
            h = _Seeded(Z, cfg, c=C0)
            E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        except Exception as e:
            return dict(E=None, conv=False, rung=rung, beta=beta,
                        err=type(e).__name__ + ": " + str(e)[:120],
                        sec=int(time.time() - t))
        finally:
            _Seeded.P0 = _Seeded.EPS0 = None            # D5
        if it < maxit:
            return dict(E=float(E), it=it, beta=beta, rung=rung, conv=True,
                        err=None, P=h.P, eps=h.eps, sec=int(time.time() - t))
        last = (E, it, beta, maxit)
    E, it, beta, maxit = last
    return dict(E=None, conv=False, it=it, beta=beta, rung=len(NG.LADDER) - 1,
                err=f"NoConvergence: cycled at every rung of {NG.LADDER}")


# ------------------------------------------------------------ stationary solve
def stationary(Z, cfg, tag, reseed=True):
    """Converge, then RESTART to stationarity.  Returns E and BOTH floors.

    reseed=False reproduces stat84's dead-lever behaviour and exists ONLY so the
    probe's two arms share one code path (D1).  The chain always runs reseed=True.
    scheme_floor : the fixed ESTAT the whole scheme is judged by.
    perconf_floor: the MEASURED |E_k - E_{k-1}| of the final restart for THIS
                   configuration.  Both recorded.  Neither selects.
    RESTART OFFSET is SIGNED (R81.7).  Its magnitude is a RESOLUTION.
    """
    g = guarded(Z, cfg)
    if not g['conv']:
        return dict(conv=False, err=g['err'], rung=g.get('rung'))
    E0 = float(g['E'])
    steps = [E0]
    E = E0
    seed = (g['P'], g['eps'])
    passes = 0
    for _ in range(NREST):
        g2 = guarded(Z, cfg, seed=(seed if reseed else None))
        if not g2['conv']:
            return dict(conv=False, err=g2['err'], rung=g2.get('rung'))
        E2 = float(g2['E'])
        steps.append(E2)
        seed = (g2['P'], g2['eps'])
        passes += 1
        stationary_here = abs(E2 - E) < ESTAT          # magnitude only (D4)
        E = E2
        if stationary_here:
            break
    perconf = abs(steps[-1] - steps[-2]) if len(steps) > 1 else 0.0
    return dict(conv=True, E=E, E_first=E0,
                offset_mHa=round((E - E0) * 1000.0, 6),          # SIGNED
                passes=passes, exhausted=(passes == NREST),
                scheme_floor=ESTAT, perconf_floor=perconf,
                rung=g.get('rung'), steps_n=len(steps), steps=steps)


# ------------------------------------------------------------ ITEM 0, THE PROOF
def cfg_probe():
    import nlchain as NC
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    return NC.add(NC.cfg_from_chain(PZPREV, sealed), PENT)


def lever():
    """F83.2.  Two arms, one code path, sited at Z=89.  Verdict filed in __doc__."""
    print("=== ITEM 0 · THE RESTART LEVER · Z=89, cfg88+6d ======================")
    print(f"  prediction sha OK  {gate_sha()[:8]}...")
    print(f"  filed verdict: DEAD arm offset == 0.000000 exactly;")
    print(f"                 LIVE arm offset != 0 and within {TARGET_TOL_MHA} mHa"
          f" of {TARGET_OFFSET_MHA:+.6f} mHa")
    cfg = cfg_probe()
    out = {}
    for arm, rs in (('dead', False), ('live', True)):
        t = time.time()
        s = stationary(PZ, cfg, '6d', reseed=rs)
        if not s['conv']:
            print(f"  {arm.upper():>4} arm DID NOT CONVERGE -- {s.get('err')}")
            return 4
        out[arm] = dict(offset_mHa=s['offset_mHa'], passes=s['passes'],
                        E_first=s['E_first'], E=s['E'],
                        perconf_floor=s['perconf_floor'],
                        exhausted=s['exhausted'], sec=int(time.time() - t))
        print(f"  {arm.upper():>4} arm  offset={s['offset_mHa']:+.6f} mHa"
              f"  passes={s['passes']}  E={s['E']:.9f}  {int(time.time()-t)}s")

    dead_ok = (out['dead']['offset_mHa'] == 0.0)
    moved = (out['live']['offset_mHa'] != 0.0)
    d = abs(out['live']['offset_mHa'] - TARGET_OFFSET_MHA)
    control_ok = (d <= TARGET_TOL_MHA)
    live_ok = moved and control_ok
    print(f"\n  DEAD arm returns exactly zero      {'PASS' if dead_ok else '**FAIL**'}")
    print(f"  LIVE arm moves the number          {'PASS' if moved else '**FAIL**'}")
    print(f"  LIVE arm reproduces s82 (|d|={d:.6f} mHa) "
          f"{'PASS' if control_ok else '**FAIL**'}")
    verdict = ('LEVER LIVE and the doubt-sited control HELD'
               if (dead_ok and live_ok) else
               'LEVER NOT DEMONSTRATED -- Item 2 stays blocked')
    rec = dict(probe='F83.2 restart lever', Z=PZ, ent='6d',
               target_mHa=TARGET_OFFSET_MHA, tol_mHa=TARGET_TOL_MHA,
               dead=out['dead'], live=out['live'], delta_vs_s82_mHa=round(d, 6),
               LEVER_LIVE=bool(dead_ok and live_ok),
               DOUBT_EXERCISED=bool(dead_ok and live_ok),
               verdict=verdict, when=time.strftime('%Y-%m-%dT%H:%M:%S'))
    json.dump(rec, open(RECEIPT, 'w'), indent=1)
    print(f"\n  {verdict}")
    print(f"  receipt: {RECEIPT}")
    return 0 if (dead_ok and live_ok) else 4


# ------------------------------------------------------------ chain step
def step_row(Z, cfg_prev):
    """One stationary chain step.  Mirrors nlchain.step, both sides restarted."""
    import nlchain as NC
    t0 = time.time()
    ref = stationary(Z, cfg_prev, 'ref')
    if not ref['conv']:
        raise RuntimeError(f"Z={Z}: reference did not converge -- {ref.get('err')}")
    D, floors = {}, {}
    for c in NC.candidates(cfg_prev):
        tag = NC.tagof(c)
        s = stationary(Z, NC.add(cfg_prev, c), tag)
        if s['conv']:
            D[tag] = round(s['E'] - ref['E'], 6)
            floors[tag] = dict(scheme=s['scheme_floor'], perconf=s['perconf_floor'],
                               offset_mHa=s['offset_mHa'], passes=s['passes'],
                               exhausted=s['exhausted'])
        else:
            floors[tag] = dict(err=s.get('err'))
        print(f"    {Z} {tag:>3} {D.get(tag)} passes={floors[tag].get('passes')}",
              flush=True)
    ok = {k: v for k, v in D.items() if v is not None}
    srt = sorted(ok, key=lambda k: ok[k])
    return dict(Z=Z, mode='stationary', ent=srt[0], D_ent=ok[srt[0]],
                rank1=srt[0], rank2=(srt[1] if len(srt) > 1 else None),
                margin=(round(ok[srt[1]] - ok[srt[0]], 6) if len(srt) > 1 else None),
                order=[[k, ok[k]] for k in srt],
                ref_offset_mHa=ref['offset_mHa'], ref_passes=ref['passes'],
                ref_exhausted=ref['exhausted'],
                scheme_floor=ESTAT, floors=floors,
                doubt_exercised=doubt_exercised(),
                sec=int(time.time() - t0))


# ------------------------------------------------------------ can-fails, GATE
def canfail():
    print("=== CAN-FAILS · stat84b · they GATE ==================================")
    print(f"  prediction sha OK  {gate_sha()[:8]}...")
    ok = True

    # CF1 SYNTHETIC, both directions on the ledger/resume logic.
    tmp = LEDGER + '.cftest'
    if os.path.exists(tmp):
        os.remove(tmp)
    globals()['LEDGER'] = tmp
    put(dict(Z=2, ent='1s')); put(dict(Z=3, ent='2s'))
    L = ledger()
    good = (set(L) == {2, 3})
    ok &= good
    print(f"  CF1 ledger round-trips and resume sees rows      "
          f"{'PASS' if good else '**FAIL**'}")
    os.remove(tmp)
    globals()['LEDGER'] = os.path.join(HERE, 'statchain.jsonl')

    # CF2 the sha gate must HALT on a changed prediction.  Tested by mutation.
    import subprocess
    bad = subprocess.run([sys.executable, '-c',
                          f"import sys;sys.path.insert(0,{HERE!r});"
                          "import stat84b;stat84b.PRED_SHA='0'*64;stat84b.gate_sha()"],
                         capture_output=True, text=True).returncode
    good = (bad == 3)
    ok &= good
    print(f"  CF2 sha gate halts on a mutated prediction  rc={bad}   "
          f"{'PASS' if good else '**FAIL**'}")

    # CF3 **THE SEED MUST ACTUALLY REACH THE SOLVER.**  Synthetic, cheap, and it is
    # the fault F83.2 was: a seed that is set but never read gives an unchanged
    # first iterate.  Seeded with DELIBERATELY WRONG orbitals, the first iterate
    # must differ; unseeded, it must not.  Z=3, seconds.
    cfg3 = [(1, 0, 2), (2, 0, 1)]
    a = guarded(3, cfg3)
    scaled = ({k: v * 0.5 for k, v in a['P'].items()}, dict(a['eps']))
    b = guarded(3, cfg3, seed=scaled)
    c = guarded(3, cfg3)
    it_moves = (b['it'] != a['it'])
    same_fp = (abs(b['E'] - a['E']) < 1e-8) and (c['it'] == a['it'])
    ok &= it_moves and same_fp
    print(f"  CF3 a wrong seed changes the ITERATION COUNT "
          f"({a['it']} -> {b['it']}) and not the fixed point   "
          f"{'PASS' if (it_moves and same_fp) else '**FAIL**'}")

    # CF4 the run gate must HALT while no lever receipt says LEVER_LIVE.
    live, _ = lever_live()
    print(f"  CF4 lever receipt present and live? {live}  "
          f"(run halts rc=4 while this is False)")

    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}")
    return ok


def real_rows(zs=(2, 3, 4)):
    """C10.  The real-row exercise.  Entrants and energies against the sealed chain."""
    import nlchain as NC
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    ok = True
    print("  C10 REAL ROWS -- verdict filed at s83 (1s, 2s, 2s; |dD| < 1 mHa)")
    for Z in zs:
        cfg = NC.cfg_from_chain(Z - 1, sealed)
        row = step_row(Z, cfg)
        d = abs(row['D_ent'] - sealed[Z]['D_ent']) * 1000.0
        good = (row['ent'] == sealed[Z]['ent']) and d < 1.0
        ok &= good
        print(f"      Z={Z}  stationary ent={row['ent']:>3} sealed={sealed[Z]['ent']:>3}"
              f"  |dD|={d:.4f} mHa  ref_offset={row['ref_offset_mHa']:+.6f} mHa"
              f"  {'PASS' if good else '**FAIL**'}")
        put(row)
    return ok


def run(z0, z1):
    print(f"  prediction sha OK  {gate_sha()[:8]}...")
    live, verdict = lever_live()
    if not live:
        print(f"HALT rc=4 (F83.2): the restart lever is not demonstrated -- {verdict}")
        print("  Run `python3 stat84b.py lever` first.  No row may be produced until")
        print("  the lever is shown to move the output AT HIGH Z.")
        sys.exit(4)
    if not doubt_exercised():
        print("  **DOUBT-UNEXERCISED (R82.2): rows produced now are provisional.**")
    L = ledger()
    import nlchain as NC
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    for Z in range(z0, z1 + 1):
        if Z in L:
            print(f"SKIP {Z} (already in ledger)", flush=True)
            continue
        cfg = NC.cfg_from_chain(Z - 1, sealed)
        put(step_row(Z, cfg))
    return 0


def score():
    L, out = ledger(), []
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    for Z in sorted(L):
        r, s = L[Z], sealed.get(Z)
        if not s or 'order' not in r:
            continue
        so = [k for k, _ in s['order']]
        out.append(dict(Z=Z, ent_same=(r['ent'] == s['ent']),
                        r1_same=(r['order'][0][0] == so[0]),
                        r2_same=(len(so) > 1 and r['order'][1][0] == so[1])))
    n = len(out)
    print(f"  rows scored {n}")
    for k in ('ent_same', 'r1_same', 'r2_same'):
        bad = [o['Z'] for o in out if not o[k]]
        print(f"  {k:<10} changed at {len(bad)} rows  {bad[:10]}")
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail':
        sys.exit(0 if canfail() else 4)
    if a[0] == 'lever':
        sys.exit(lever())
    if a[0] == 'real':
        sys.exit(0 if real_rows() else 4)
    if a[0] == 'run':
        sys.exit(run(int(a[1]), int(a[2])))
    if a[0] == 'score':
        sys.exit(score())
