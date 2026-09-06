#!/usr/bin/env python3
"""front83.py -- THE FRONTIER WIDTH W.  s83, under F83.1.

F83.1: gtest83 scored the FULL candidate ladder.  Clause 2 rules the derivation to
the DIFFERENTIATING ELECTRON only.  So the condition that matters is not on the whole
ladder but on the FRONTIER -- the w channels of least nu at each Z.

    W := smallest w for which the g-condition holds at ALL 107 rows on the frontier
         of width w.

Prediction: pack83/PREDICTION-S83-ITEM1B-FRONTIER.md, hashed before this ran.

usage: python3 front83.py [canfail|run]
"""
import json, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gtest83 import bank, channels, verdicts, madelung_key   # noqa: E402

PRED = os.path.join(HERE, 'PREDICTION-S83-ITEM1B-FRONTIER.md')
PRED_SHA = '8f9aa8d8c62a41fdd1783c96107ca218a5cf22c623f51e71fe0a9c86be843c81'
WMAX = 9


def pred_gate():
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if got != PRED_SHA:
        print(f"HALT: prediction sha mismatch\n  want {PRED_SHA}\n  got  {got}")
        sys.exit(3)
    print(f"  prediction sha OK  {got[:8]}...{got[-8:]}")


def frontier(chs, w):
    return sorted(chs, key=lambda c: c['nu'])[:w]


def row_fails(chs, w):
    """does the frontier of width w violate Madelung?  Uses the SAME test the sealed
    walk uses -- nu-order against sigma-then-n order -- restricted to the window."""
    f = frontier(chs, w)
    if len(f) < 2:
        return False, []
    a = [c['tag'] for c in sorted(f, key=lambda c: c['nu'])]
    b = [c['tag'] for c in sorted(f, key=madelung_key)]
    if a == b:
        return False, []
    return True, [(x, y) for x, y in zip(a, b) if x != y]


def canfail():
    print("=== CAN-FAILS · front83 · they GATE ==================================")
    pred_gate()
    ok = True
    rows = bank()

    # CF1 POSITIVE, REAL ROW.  Z=2 has 3 candidates and the sealed entrant is 1s.
    # Verdict written first in Q5's spirit: a width-2 frontier at Z=2 cannot fail,
    # 1s is sigma-minimal AND nu-minimal.
    z2 = channels(next(r for r in rows if r['Z'] == 2))
    f, _ = row_fails(z2, 2)
    ok &= (not f)
    print(f"  CF1 real row Z=2, w=2, must be CLEAN                     "
          f"{'PASS' if not f else '**FAIL**'}")

    # CF2 REAL ROW, OTHER DIRECTION.  Z=90's sealed tie-break failure (6d before 5f,
    # same sigma=8, 5f has smaller n) MUST be caught at w=2.  Written first, Q3.
    z90 = channels(next(r for r in rows if r['Z'] == 90))
    f, why = row_fails(z90, 2)
    ok &= f
    print(f"  CF2 real row Z=90, w=2, must FAIL (sealed tie-break)     "
          f"{'PASS' if f else '**FAIL**'}   {why}")

    # CF3 monotonicity machinery: widening a window can never REMOVE a violation.
    mono = True
    for r in rows[:20]:
        chs = channels(r)
        seq = [row_fails(chs, w)[0] for w in range(2, 7)]
        if any(seq[i] and not seq[i + 1] for i in range(len(seq) - 1)):
            mono = False
    ok &= mono
    print(f"  CF3 violations are monotone in w on 20 real rows         "
          f"{'PASS' if mono else '**FAIL**'}")

    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL** -- nothing is scored'}")
    return 0 if ok else 4


def run():
    rc = canfail()
    if rc:
        return rc
    rows = bank()
    print("\n=== THE FRONTIER WIDTH ===============================================")
    print("   w   rows failing   first five failing Z")
    table = {}
    for w in range(2, WMAX + 1):
        bad = [r['Z'] for r in rows if row_fails(channels(r), w)[0]]
        table[w] = bad
        print(f"  {w:<4}{len(bad):<15}{bad[:5]}")

    W = next((w for w in range(2, WMAX + 1) if not table[w]), None)
    print(f"\n  W (smallest clean width) = {W if W else 'NONE -- fails at every width'}")
    print(f"  failures at w=2 : {table[2]}")

    json.dump({str(k): v for k, v in table.items()},
              open(os.path.join(HERE, 'front83-out.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'run'
    sys.exit({'canfail': canfail, 'run': run}[cmd]())
