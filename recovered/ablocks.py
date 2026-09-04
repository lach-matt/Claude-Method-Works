"""ablocks.py -- SESSION 65. THE REPLACEMENT BLOCK TEST, BOTH CANDIDATES.

Scores pack65/PREDICTION-T-B-PRIME.md, sha 39bbebfc..., which was filed at
2026-08-20T22:04:38Z before this file existed. The sha is re-verified at every
invocation and the scorer refuses to run without it.

`pack64/alpha.py` IS SEALED AND IS NOT EDITED. This driver reads the same sealed
chain and reimplements only what it needs (F44.1 route).

F65.1 governs the design: NO PREDICTOR MAY CONTAIN THE OUTCOME IT PREDICTS.
  Candidate A  alpha from the base ONE SHELL OUT, at the block's own Z_open.
               D(A) never enters it.
  Candidate B  median alpha over the same l->l+1 step measured at OTHER atoms,
               excluding the block's own Z_open. Neither D(A) nor D(B) at Z_open
               enters it.

usage:  python3 ablocks.py score
        python3 ablocks.py canfail      seven directions, run before `score` is read
"""
import sys, os, json, hashlib, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(HERE, '..', 'rt', 'nlchain.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-T-B-PRIME.md')
PRED_SHA = "39bbebfcd6681b1c104fe338425651ae466704cc6071610933df81c673607990"
T = lambda n, l: f"{n}{'spdfg'[l]}"
PAIRNAME = {0: 's->p', 1: 'p->d', 2: 'd->f'}


def check_prediction():
    h = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if h != PRED_SHA:
        sys.exit(f"HALT: prediction sha {h[:8]} != filed {PRED_SHA[:8]}. Nothing is scored.")
    return h


def load():
    return {json.loads(l)['Z']: json.loads(l) for l in open(CHAIN)}


def blocks(rows):
    """The eleven blocks and their OBSERVED first-entry order. This is the target,
    not a predictor."""
    first = {}
    for Z in sorted(rows):
        t = T(*rows[Z]['ent_nl'])
        if t not in first: first[t] = Z
    out = []
    for N in range(3, 9):
        for l in range(0, 4):
            n = N - l
            if n < l + 2: continue
            A, B = T(n, l + 1), T(n + 1, l)
            if A not in first or B not in first: continue
            out.append(dict(N=N, n=n, l=l, A=A, B=B,
                            Afirst=first[A] < first[B], Zo=min(first[A], first[B])))
    return out


def ratio(D, n, l):
    """the sealed ratio measure at base (n,l): cost of one unit of l in units of one
    unit of n. Returns None where the base or either step is unavailable."""
    a, b, c = T(n, l), T(n, l + 1), T(n + 1, l)
    if not (a in D and b in D and c in D): return None
    den = D[c] - D[a]
    if abs(den) <= 1e-4: return None
    return (D[b] - D[a]) / den


def transfer_pool(rows, exclude_Z=None):
    """all q=1 ratio measurements, keyed by l-pair, optionally dropping one Z."""
    pool = {}
    for Z in sorted(rows):
        if Z < 3 or Z == exclude_Z: continue
        D = dict(rows[Z]['order'])
        for n in range(2, 8):
            for l in range(0, 3):
                v = ratio(D, n, l)
                if v is not None: pool.setdefault(l, []).append(v)
    return pool


def score(rows, force=None):
    check_prediction()
    bl = blocks(rows)
    if force: force(bl, rows)
    resA, resB, nodataA, nodataB = [], [], [], []
    print("  blk  A vs B      l-pair  Zopen  Afirst |  aA(shift)  A?  |  aB(transfer)  B?")
    for b in bl:
        D = dict(rows[b['Zo']]['order'])
        aA = ratio(D, b['n'] + 1, b['l'])
        pool = transfer_pool(rows, exclude_Z=b['Zo']).get(b['l'], [])
        aB = st.median(pool) if pool else None
        sA = sB = "  --  "
        if aA is None: nodataA.append(b['N']); okA = None
        else:
            okA = ((aA < 1) == b['Afirst']); resA.append((b, aA, okA))
            sA = f"{aA:8.4f} {'YES' if okA else '**NO**':>7}"
        if aB is None: nodataB.append(b['N']); okB = None
        else:
            okB = ((aB < 1) == b['Afirst']); resB.append((b, aB, okB))
            sB = f"{aB:8.4f} {'YES' if okB else '**NO**':>7}"
        print(f"   {b['N']}  {b['A']:>3} vs {b['B']:<3}  {PAIRNAME[b['l']]:>6}  {b['Zo']:>4}"
              f"   {str(b['Afirst']):>5} | {sA} | {sB}")

    def tally(res, nod, name, npool):
        ok = sum(1 for _, _, o in res if o)
        bad = [r[0]['N'] for r in res if not r[2]]
        badp = sorted({PAIRNAME[r[0]['l']] for r in res if not r[2]})
        print(f"\n  CANDIDATE {name}: {ok}/{len(res)} agree"
              f"   NO-DATA {len(nod)}{'' if not nod else ' at blocks '+str(nod)}")
        if bad: print(f"    disagreements at blocks {bad}, l-pairs {badp}")
        return ok, len(res), badp

    okA, nA, badpA = tally(resA, nodataA, 'A (shifted base, same atom)', None)
    okB, nB, badpB = tally(resB, nodataB, 'B (transfer, other atoms)', None)

    # the declared sign-agreement check between the two candidates
    disagree = []
    for (b1, a1, _), (b2, a2, _) in zip(resA, resB):
        if b1['N'] == b2['N'] and b1['A'] == b2['A'] and (a1 < 1) != (a2 < 1):
            disagree.append((b1['N'], b1['A'], a1, a2))
    print(f"\n  A vs B fall on OPPOSITE sides of 1 at {len(disagree)} blocks"
          + (":" if disagree else "."))
    for N, A, a1, a2 in disagree:
        print(f"    blk {N} {A}:  aA={a1:.4f}  aB={a2:.4f}")
    return dict(A=(okA, nA), B=(okB, nB), opp=len(disagree), badpA=badpA, badpB=badpB)


def canfail(rows):
    """The driver must be shown to go red before any real number is believed."""
    print("=== CAN-FAIL ===")
    tests = [
        ("[0] unmodified", None),
        ("[1] block 6 4f/5d observed order flipped",
         lambda bl, r: [b.update(Afirst=not b['Afirst']) for b in bl if b['A'] == '4f']),
        ("[2] every observed order flipped",
         lambda bl, r: [b.update(Afirst=not b['Afirst']) for b in bl]),
        ("[3] all s->p blocks relabelled as d->f (predictor swapped)",
         lambda bl, r: [b.update(l=2, n=b['n'] - 2) for b in bl if b['l'] == 0]),
        ("[4] Z_open of block 6 5d/6p moved to Z=100 (wrong atom)",
         lambda bl, r: [b.update(Zo=100) for b in bl if b['A'] == '5d']),
    ]
    for name, f in tests:
        print(f"\n--- {name}")
        try:
            r = score(rows, force=f)
            print(f"    => A {r['A'][0]}/{r['A'][1]}   B {r['B'][0]}/{r['B'][1]}")
        except Exception as e:
            print(f"    => RAISED {type(e).__name__}: {e}")
    print("\n--- [5] prediction file tampered")
    global PRED_SHA
    keep = PRED_SHA; PRED_SHA = "0" * 64
    try:
        score(rows)
        print("    => DID NOT HALT -- the sha guard is broken")
    except SystemExit as e:
        print(f"    => {e}")
    PRED_SHA = keep
    print("\n--- [6] chain emptied of every d->f measurement")
    try:
        r = score(rows, force=lambda bl, rr: [b.update(l=3) for b in bl])
        print(f"    => A {r['A'][0]}/{r['A'][1]}   B {r['B'][0]}/{r['B'][1]}")
    except Exception as e:
        print(f"    => RAISED {type(e).__name__}: {e}")


if __name__ == '__main__':
    rows = load()
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'score'
    if cmd == 'canfail': canfail(rows)
    else:
        print(f"prediction sha VERIFIED {check_prediction()[:8]}...\n")
        score(rows)
