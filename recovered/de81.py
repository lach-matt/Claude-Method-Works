#!/usr/bin/env python3
"""de81.py -- SESSION 81, ITEM 3.  THE TWO REMAINING Z=89 BRACKETS, 7d AND 8d.

s79 left them CLASS B: refine79 found no target-node zero.  M's order: **de80's fallback
is the instrument that can now reach them if a zero exists at all** -- refine79 searched
under F80.1's undeclared orientation and with a bound of its own choosing.

DECLARED CONSTRUCTION.  **NO SEALED FILE IS EDITED AND NOTHING IS WRITTEN INTO pack80.**
  K1  pack80/de80.py is IMPORTED, not copied.  Its Fallback class, its G1-G7 repairs and
      its ladder are used exactly as sealed.  de80.NL is extended in memory with
      7d -> (7,2) and 8d -> (8,2); de80.put is NOT called, and this driver's receipts go
      to pack81/de81.jsonl.
  K2  BOTH SELECTION BRANCHES ARE RUN on every channel (G7 / F80.1), and the spread and
      zero count are recorded from de80's own fallback log.
  K3  THE CURRENCY IS dE, NOT eps.  dE = E(cfg88+ch) - E_REF, the same currency as the
      sealed ranks.  F79.2 exists because those two were once mixed.
  K4  CAN-FAIL FIRST AND IT GATES: 6d through this same driver, fallback inert, must
      return the sealed pack77 energy.  If it does not, nothing else is scored.

usage:  python3 de81.py canfail
        python3 de81.py run <7d|8d> <most-bound|least-bound>
        python3 de81.py score
"""
import os, sys, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
P80 = os.path.join(os.path.dirname(HERE), 'pack80')
CACHE = os.path.join(HERE, 'de81.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S81-ITEM3-BRACKETS.md')
PSHA = os.path.join(HERE, 'PREDICTION-S81-ITEM3-BRACKETS.sha256')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
sys.path.insert(0, P80)
import de80

de80.NL.update({'7d': (7, 2), '8d': (8, 2)})       # K1
E_REF = de80.E_REF
SEALED = de80.SEALED_E
M89 = 0.032332                                      # Ha, sealed margin at Z=89


def gate_sha():
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")


def put(rec):
    with open(CACHE, 'a') as f:
        f.write(json.dumps(rec) + '\n')


def one(ch, select, tag=None):
    gate_sha()
    t0 = time.time()
    cfg = de80.cfgs(ch)
    r = de80.guarded(89, cfg, select=select)
    dE = None if r.get('E') is None else (r['E'] - E_REF)
    fb = r.get('fb') or []
    rec = dict(tag=(tag or 'question'), ch=ch, select=select, conv=r['conv'],
               E=r.get('E'), dE_mHa=(None if dE is None else round(dE * 1000, 6)),
               above_6d_mHa=(None if dE is None else round((dE - (SEALED['6d'] - E_REF)) * 1000, 3)),
               above_7p_mHa=(None if dE is None else round((dE - (SEALED['7p'] - E_REF)) * 1000, 3)),
               x_m89=(None if dE is None else round((dE - (SEALED['7p'] - E_REF)) / M89, 3)),
               it=r.get('it'), rung=r.get('rung'), err=r.get('err'),
               n_fb=len(fb), n_zeros=[f.get('n_zeros') for f in fb],
               spread=[f.get('spread') for f in fb],
               edge=[bool(f.get('edge_lo') or f.get('edge_hi')) for f in fb],
               sec=int(time.time() - t0))
    put(rec)
    print(f"  {ch} [{select}] conv={rec['conv']} it={rec['it']} dE={rec['dE_mHa']} mHa "
          f"above7p={rec['above_7p_mHa']} ({rec['x_m89']} x m89) n_fb={rec['n_fb']} "
          f"nz={rec['n_zeros']} {rec['sec']}s")
    if rec['err']:
        print(f"    err={rec['err']}")
    return rec


def canfail():
    """K4.  6d through this driver, fallback inert, must land on the sealed energy."""
    gate_sha()
    r = one('6d', 'least-bound', tag='K4')
    ok = r['conv'] and abs(r['E'] - SEALED['6d']) < 1e-9 and r['n_fb'] == 0
    print(f"  K4 machinery: E={r['E']!r} vs sealed {SEALED['6d']!r}  fb={r['n_fb']} -> "
          f"{'PASS' if ok else 'FAIL'}")
    return ok


def score():
    gate_sha()
    rows = [json.loads(l) for l in open(CACHE) if l.strip()]
    q = [r for r in rows if r['tag'] == 'question']
    print(f"  {'ch':>4} {'select':>12} {'conv':>6} {'dE (mHa)':>11} {'above 7p':>10} "
          f"{'x m89':>7}  zeros")
    for r in q:
        print(f"  {r['ch']:>4} {r['select']:>12} {str(r['conv']):>6} "
              f"{str(r['dE_mHa']):>11} {str(r['above_7p_mHa']):>10} "
              f"{str(r['x_m89']):>7}  {r['n_zeros']}")
    return q


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'score'
    if cmd == 'canfail':
        canfail()
    elif cmd == 'run':
        one(sys.argv[2], sys.argv[3])
    elif cmd == 'score':
        score()
    else:
        raise SystemExit(f"unknown cmd {cmd}")
