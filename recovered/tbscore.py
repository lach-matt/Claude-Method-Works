"""tbscore.py -- SESSION 64. Scores pack64/tbctrl64.jsonl against
pack63/PREDICTION-TIEBREAK-CONTROLS.md, sha 0b12ef684c1e39b3b26fc9d0ebf988cda1929e2e658047f8ee2e3b88f0b61c20.

The prediction's three clauses, transcribed and not paraphrased:
  T1  entrant unchanged at all four rows under the OBSERVED reference:
      Z=57 -> 5d, Z=58 -> 4f, Z=89 -> 6d, Z=91 -> 5f, and ok=True at 4/4.
  T2  the tie-break departure survives: 5d selected over 4f at Z=57, 6d over 5f at Z=89.
  T3  margins at Z=57 and Z=89 exceed the 0.05 mHa working floor by at least 20x.

FALSIFIERS, also from the prediction, checked explicitly rather than left implicit:
  * any entrant flipping to the Madelung order (4f at 57, 5f at 89)  -> WITHDRAW s63
  * a margin at or below the floor                                   -> NOT DECIDABLE
  * non-convergence of a row                                         -> NO-DATA, not a pass

usage: python3 tbscore.py                 score the sealed rows
       python3 tbscore.py --canfail       run the injected-failure controls and exit
A scorer that cannot go red is not a scorer (s63, SCORE-RUNG-0-ASSEMBLY §CONTROLS).
"""
import sys, os, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
PRED = os.path.join(HERE, '..', 'pack63', 'PREDICTION-TIEBREAK-CONTROLS.md')
PRED_SHA = '0b12ef684c1e39b3b26fc9d0ebf988cda1929e2e658047f8ee2e3b88f0b61c20'
ROWS = os.path.join(HERE, 'tbctrl64.jsonl')
FLOOR = 0.00005          # 0.05 mHa, in Ha. Rung 7 grid floor / s61 seed-memory floor.

T1 = {57: '5d', 58: '4f', 89: '6d', 91: '5f'}
MADELUNG = {57: '4f', 89: '5f'}      # what the tie-break clause would have required
T2_PAIRS = {57: ('5d', '4f'), 89: ('6d', '5f')}


def verify_prediction():
    h = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if h != PRED_SHA:
        print(f"HALT: prediction sha {h[:12]}... != filed {PRED_SHA[:12]}...")
        sys.exit(1)
    return h


def score(rows):
    """rows: {Z: record}. Returns (verdict, lines). Verdict PASS / WITHDRAW / NOT-DECIDABLE / NO-DATA."""
    out, verdict = [], 'PASS'
    Dof = lambda r: dict(r['order'])

    # --- falsifier 1, checked FIRST because the prediction says report it first ---
    flipped = [Z for Z, tag in MADELUNG.items()
               if Z in rows and rows[Z]['ent'] == tag]
    if flipped:
        out.append(f"  FALSIFIED  entrant flipped to Madelung order at Z={flipped}")
        out.append("  ** THE s63 TIE-BREAK RESTATEMENT MUST BE WITHDRAWN. **")
        return 'WITHDRAW', out

    missing = [Z for Z in T1 if Z not in rows]
    if missing:
        out.append(f"  NO-DATA    rows absent: {missing}")
        return 'NO-DATA', out

    # --- T1 ---
    bad = [(Z, rows[Z]['ent'], t) for Z, t in T1.items() if rows[Z]['ent'] != t]
    nok = sum(1 for Z in T1 if rows[Z]['ok'] is True)
    if bad:
        out.append(f"  T1  FAIL   entrant differs: {bad}")
        verdict = 'FAIL'
    else:
        out.append(f"  T1  PASS   entrant unchanged 4/4; ok=True {nok}/4")
        if nok != 4:
            out.append(f"  T1  FAIL   ok=True only {nok}/4")
            verdict = 'FAIL'

    # --- T2 ---
    for Z, (w, l) in T2_PAIRS.items():
        D = Dof(rows[Z])
        if w not in D or l not in D:
            out.append(f"  T2  NO-DATA Z={Z}: {w} or {l} did not converge")
            verdict = 'NO-DATA' if verdict == 'PASS' else verdict
            continue
        gap = D[l] - D[w]
        ok = gap > 0
        out.append(f"  T2  {'PASS' if ok else 'FAIL'}   Z={Z}: {w} over {l} by "
                   f"{gap*1000:.2f} mHa  ({gap/FLOOR:.0f}x floor)")
        if not ok:
            verdict = 'FAIL'

    # --- T3 ---
    for Z in (57, 89):
        m = rows[Z]['margin']
        if m is None:
            out.append(f"  T3  NO-DATA Z={Z}: no runner-up")
            continue
        x = m / FLOOR
        if m <= FLOOR:
            out.append(f"  T3  NOT-DECIDABLE Z={Z}: margin {m*1000:.2f} mHa at or below floor")
            verdict = 'NOT-DECIDABLE' if verdict == 'PASS' else verdict
        else:
            out.append(f"  T3  {'PASS' if x >= 20 else 'FAIL'}   Z={Z}: entrant margin "
                       f"{m*1000:.2f} mHa = {x:.0f}x floor (predicted >= 20x)")
            if x < 20:
                verdict = 'FAIL'
    return verdict, out


def load():
    return {d['Z']: d for d in map(json.loads, open(ROWS))}


def canfail():
    """The scorer must go red in both directions or it is not an instrument."""
    base = load()
    print("CAN-FAIL CONTROLS")
    v, _ = score(base)
    print(f"  [0] unmodified rows                        -> {v}   (expect PASS)")

    a = {Z: dict(r) for Z, r in base.items()}
    a[57] = dict(a[57], ent='4f')
    v, _ = score(a)
    print(f"  [1] Z=57 entrant forced to 4f              -> {v}   (expect WITHDRAW)")

    b = {Z: dict(r) for Z, r in base.items()}
    b[89] = dict(b[89], ent='5f')
    v, _ = score(b)
    print(f"  [2] Z=89 entrant forced to 5f              -> {v}   (expect WITHDRAW)")

    c = {Z: dict(r) for Z, r in base.items()}
    c[57] = dict(c[57], margin=0.00001)
    v, _ = score(c)
    print(f"  [3] Z=57 margin driven under the floor     -> {v}   (expect NOT-DECIDABLE)")

    d = {Z: dict(r) for Z, r in base.items() if Z != 91}
    v, _ = score(d)
    print(f"  [4] Z=91 row removed                       -> {v}   (expect NO-DATA)")

    e = {Z: dict(r) for Z, r in base.items()}
    e[58] = dict(e[58], ok=False)
    v, _ = score(e)
    print(f"  [5] Z=58 ok forced False                   -> {v}   (expect FAIL)")

    f = {Z: dict(r) for Z, r in base.items()}
    f[57] = dict(f[57], order=[['5d', -0.10556], ['4f', -0.20585]])
    v, _ = score(f)
    print(f"  [6] Z=57 5d/4f depths swapped in order     -> {v}   (expect FAIL)")


if __name__ == '__main__':
    h = verify_prediction()
    print(f"PREDICTION {os.path.relpath(PRED, HERE)}  sha {h[:12]}...  VERIFIED")
    if '--canfail' in sys.argv:
        canfail(); sys.exit(0)
    rows = load()
    verdict, lines = score(rows)
    print(f"ROWS {len(rows)}: Z = {sorted(rows)}")
    print('\n'.join(lines))
    print(f"\nVERDICT: {verdict}")
