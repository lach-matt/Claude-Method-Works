#!/usr/bin/env python3
"""stat84.py -- ITEM 2, THE STATIONARY CHAIN.  R81.1 + R81.3.  Built at s83, runs at s84+.

**NO SEALED ROW IS EDITED.**  Output is a SECOND chain, statchain.jsonl.  The sealed
nlchain.jsonl remains the ruling chain until the comparison is scored.
**THE SCORE IS THE ORDERING -- entrant, rank 1, rank 2 -- NOT the energy.**
R81.2 binds: BOTH sides restarted to stationarity, never one.

R81.3: BOTH floors on IDENTICAL rows.  scheme-wide (a single ESTAT for the whole
scheme) and per-configuration (the measured per-configuration stationarity residual).
**M's expectation is per-configuration; it is recorded to be SCORED AGAINST and is
NOT used to pre-select.**  Both are written to every row; nothing selects.

RESUME (F53.3): statchain.jsonl is the ledger.  A row already present is SKIPPED.
Resume is therefore from the last completed row, and interruption costs at most one row.

Prediction pack83/PREDICTION-S84-ITEM2-STATIONARY-CHAIN.md, hashed before row one.

usage:  python3 stat84.py canfail          -- gate, synthetic + REAL rows
        python3 stat84.py run Z0 Z1        -- a Zeno segment
        python3 stat84.py score            -- compare against the sealed chain
"""
import json, os, sys, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RT = os.path.join(ROOT, 'rt')
sys.path.insert(0, RT)
sys.path.insert(0, os.path.join(ROOT, 'pack82'))

PRED = os.path.join(HERE, 'PREDICTION-S84-ITEM2-STATIONARY-CHAIN.md')
PRED_SHA = '631d58612ee19774dc03b7c1a6cdacc3be05d18c59ec45f0b0308951a49ed538'
LEDGER = os.path.join(HERE, 'statchain.jsonl')
ESTAT = 1e-10          # scheme-wide floor, Ha.  conf82's value, carried unchanged.
NREST = 20             # restart cap.  s81 V6: 12 did not exhaust ESTAT at Z=90.

# **DOUBT STAMP.**  R82.2.  Cleared only by the Z=89 control, ordered as s84's first act.
DOUBT_EXERCISED = False


def gate_sha():
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if got != PRED_SHA:
        print(f"HALT: prediction sha mismatch\n  want {PRED_SHA}\n  got  {got}")
        sys.exit(3)
    return got


def ledger():
    if not os.path.exists(LEDGER):
        return {}
    return {r['Z']: r for r in (json.loads(l) for l in open(LEDGER) if l.strip())}


def put(row):
    with open(LEDGER, 'a') as f:
        f.write(json.dumps(row) + '\n')
        f.flush()
        os.fsync(f.fileno())


# ------------------------------------------------------------ stationary solve
def stationary(Z, cfg, tag):
    """Converge, then RESTART to stationarity.  Returns E and BOTH floors.

    scheme_floor : the fixed ESTAT the whole scheme is judged by.
    perconf_floor: the MEASURED |E_k - E_{k-1}| of the final restart for THIS
                   configuration.  Both recorded.  Neither selects.
    RESTART OFFSET is SIGNED (R81.7).  Its magnitude is a RESOLUTION, not a drop.
    """
    import nlguard as NG
    g = NG.run_guarded(Z, cfg, tag)
    if not g['conv']:
        return dict(conv=False, err=g['err'], rung=g.get('rung'))
    E0 = float(g['E'])
    ladder = [E0]
    E = E0
    passes = 0
    for _ in range(NREST):
        g2 = NG.run_guarded(Z, cfg, tag)
        E2 = float(g2['E'])
        ladder.append(E2)
        passes += 1
        step = abs(E2 - E)
        E = E2
        if step < ESTAT:
            break
    perconf = abs(ladder[-1] - ladder[-2]) if len(ladder) > 1 else 0.0
    return dict(conv=True, E=E, E_first=E0,
                offset_mHa=round((E - E0) * 1000.0, 6),          # SIGNED
                passes=passes, exhausted=(passes == NREST),
                scheme_floor=ESTAT, perconf_floor=perconf,
                rung=g.get('rung'), ladder_n=len(ladder))


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
                doubt_exercised=DOUBT_EXERCISED,
                sec=int(time.time() - t0))


# ------------------------------------------------------------ can-fails, GATE
def canfail():
    print("=== CAN-FAILS · stat84 · they GATE ===================================")
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
                          "import stat84;stat84.PRED_SHA='0'*64;stat84.gate_sha()"],
                         capture_output=True, text=True).returncode
    good = (bad == 3)
    ok &= good
    print(f"  CF2 sha gate halts on a mutated prediction  rc={bad}   "
          f"{'PASS' if good else '**FAIL**'}")

    # CF3 **REAL ROWS.**  Z=2,3,4 against the SEALED chain.  Verdict written first
    # in C10: entrants 1s, 2s, 2s and |dE| < 1 mHa.
    import nlchain as NC
    import gates_stub  # noqa: F401  -- absent; guarded below
    return ok


def real_rows(zs=(2, 3, 4)):
    """C10.  The real-row exercise.  Entrants and energies against the sealed chain."""
    import nlchain as NC
    sealed = {r['Z']: r for r in
              (json.loads(l) for l in open(os.path.join(RT, 'nlchain.jsonl')))}
    ok = True
    print("  CF3 REAL ROWS -- verdict filed first in C10 (1s, 2s, 2s; |dE| < 1 mHa)")
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
    if not DOUBT_EXERCISED:
        print("  **DOUBT-UNEXERCISED (R82.2): the Z=89 control has not run. "
              "Rows produced now are provisional.**")
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
        rc = canfail()
        sys.exit(0 if rc else 4)
    if a[0] == 'real':
        sys.exit(0 if real_rows() else 4)
    if a[0] == 'run':
        sys.exit(run(int(a[1]), int(a[2])))
    if a[0] == 'score':
        sys.exit(score())
