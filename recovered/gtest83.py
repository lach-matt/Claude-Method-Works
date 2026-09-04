#!/usr/bin/env python3
"""gtest83.py -- CLAUSE 1, ROUTE (c): the g-ladder at the RELAXED field.

THE OBJECT (adopted by M at s83 open).  F_core's tail is exactly Coulombic with net
charge 1 -- MEASURED at s82, q_eff = -rV = 1.000000 over 20-298 a0.  Every bound
candidate therefore has an EXACT defect representation:

    D(n,l) = -1/(2 nu^2),   nu = n - delta,   delta = n - (-2D)^(-1/2)

and with sigma = n+l the identity

    nu = sigma - g(l),      g(l) = l + delta(n,l)

makes Madelung EXACTLY equivalent to two conditions on g:

    (G-within)  g increasing in l inside a sigma-class   <=> tie-break, least n first
    (G-across)  max g(sigma+1) - min g(sigma) < 1        <=> the n+l ordering

CURRENCY.  D is the sealed total-energy currency of nlchain.jsonl, relaxed on BOTH
sides.  It is NOT an eigenvalue.  F79.2 is the fault that exists because the two were
once mixed; nothing here is compared to an eigenvalue without saying so (route (b)
does exactly that, and says so).

SCOPE, STATED IN THE SOURCE.  **THIS DERIVES AN EQUIVALENCE, NOT A BOUND.**  It does
not show that F_core must satisfy the condition.  NO PROPERTY OF F_core IS DERIVED
HERE.

usage:  python3 gtest83.py canfail      -- the gate, runs first
        python3 gtest83.py run          -- routes (c) and (a)
        python3 gtest83.py relax        -- route (b), Z=89/90 fixed vs relaxed
"""
import json, os, re, sys, math, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'rt', 'nlchain.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S83-ITEM1-GLADDER.md')
PRED_SHA = '86da5c2b40b0aab1424ed764a99d7d2bd871f301560dbc12cf679eef4c5b7b7e'
ZLO, ZHI = 2, 108
LMAX_TRUSTED = 3
LSYM = 'spdfg'
TAG = re.compile(r'^(\d+)([spdfg])$')

sys.path.insert(0, os.path.join(ROOT, 'pack82'))
from doubt82 import Domain                                    # noqa: E402


# ---------------------------------------------------------------- prediction gate
def pred_gate():
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if got != PRED_SHA:
        print(f"HALT: prediction sha mismatch\n  want {PRED_SHA}\n  got  {got}")
        sys.exit(3)
    print(f"  prediction sha OK  {got[:8]}...{got[-8:]}")


# ---------------------------------------------------------------- the arithmetic
def defect(n, D):
    """delta and nu from the exact Rydberg representation with net charge 1."""
    if D >= 0.0:
        return None, None
    nu = 1.0 / math.sqrt(-2.0 * D)
    return n - nu, nu


def channels(row, lmax=LMAX_TRUSTED):
    """[(tag, n, l, sigma, D, nu, delta, g)] for one banked row, bound and l<=lmax."""
    out = []
    for tag, D in row.get('order', []):
        m = TAG.match(tag)
        if not m:
            continue
        n, l = int(m.group(1)), LSYM.index(m.group(2))
        if l > lmax:
            continue
        delta, nu = defect(n, D)
        if nu is None:
            continue
        out.append(dict(tag=tag, n=n, l=l, sigma=n + l, D=D,
                        nu=nu, delta=delta, g=l + delta))
    return out


def verdicts(chs):
    """(G-within, G-across) verdicts plus the offending pairs, for one Z."""
    by_sigma = {}
    for c in chs:
        by_sigma.setdefault(c['sigma'], []).append(c)

    within = []
    for s, cs in by_sigma.items():
        cs = sorted(cs, key=lambda c: c['l'])
        for a, b in zip(cs, cs[1:]):
            if not (b['g'] > a['g']):
                within.append((s, a['tag'], b['tag'], b['g'] - a['g']))

    across = []
    for s in sorted(by_sigma):
        if s + 1 not in by_sigma:
            continue
        lo = min(c['g'] for c in by_sigma[s])
        hi = max(c['g'] for c in by_sigma[s + 1])
        if not (hi - lo < 1.0):
            across.append((s, hi - lo))
    return within, across, by_sigma


def madelung_key(c):
    return (c['sigma'], c['n'])


def order_agrees(chs):
    """does nu-order reproduce D-order?  (P1 machinery)"""
    a = [c['tag'] for c in sorted(chs, key=lambda c: c['D'])]
    b = [c['tag'] for c in sorted(chs, key=lambda c: c['nu'])]
    return a == b


def madelung_holds(chs):
    """does the RELAXED field's own nu-order equal the Madelung order?"""
    a = [c['tag'] for c in sorted(chs, key=lambda c: c['nu'])]
    b = [c['tag'] for c in sorted(chs, key=madelung_key)]
    return a == b


def bank():
    rows = [json.loads(l) for l in open(BANK)]
    return [r for r in rows if ZLO <= r.get('Z', 0) <= ZHI]


# ---------------------------------------------------------------- can-fails, GATE
def canfail():
    print("=== CAN-FAILS · they run FIRST and they GATE ==========================")
    pred_gate()
    ok = True
    rows = bank()

    # CF1 POSITIVE, ON REAL ROWS FROM THE REAL BANK (the R82.1 spirit).
    # Verdict written down first in P1: 107 of 107.
    n_ok = sum(1 for r in rows if order_agrees(channels(r)))
    good = (n_ok == len(rows) == 107)
    ok &= good
    print(f"  CF1 nu-order == D-order on real banked rows   {n_ok}/{len(rows)}   "
          f"{'PASS' if good else '**FAIL**'}")

    # CF2 NEGATIVE.  Reverse one real pair by hand; the instrument MUST notice.
    r = dict(json.loads(json.dumps(next(x for x in rows if x['Z'] == 90))))
    o = list(r['order'])
    o[0], o[1] = (o[0][0], o[1][1]), (o[1][0], o[0][1])       # swap the two D values
    r['order'] = o
    changed = not madelung_holds(channels(r)) or \
        [c['tag'] for c in sorted(channels(r), key=lambda c: c['nu'])] != \
        [c['tag'] for c in sorted(channels(next(x for x in rows if x['Z'] == 90)),
                                  key=lambda c: c['nu'])]
    ok &= changed
    print(f"  CF2 a hand-reversed real pair changes the verdict        "
          f"{'PASS' if changed else '**FAIL**'}")

    # CF3 NEGATIVE-DIRECTION on the g test itself: a synthetic ladder that is
    # MONOTONE with variation 0.5 must be scored CLEAN by both conditions.
    synth_ok = [dict(tag='a', n=4, l=0, sigma=4, D=-1, nu=0, delta=0, g=4.0),
                dict(tag='b', n=3, l=1, sigma=4, D=-1, nu=0, delta=0, g=4.2),
                dict(tag='c', n=5, l=0, sigma=5, D=-1, nu=0, delta=0, g=4.3),
                dict(tag='d', n=4, l=1, sigma=5, D=-1, nu=0, delta=0, g=4.5)]
    w, a, _ = verdicts(synth_ok)
    good = (not w and not a)
    ok &= good
    print(f"  CF3 clean synthetic ladder scores CLEAN                  "
          f"{'PASS' if good else '**FAIL**'}")

    # CF4 the other direction: variation 1.5 must FAIL G-across, and a decreasing
    # ladder must FAIL G-within.  Both verdicts reachable on the identical path.
    synth_bad = [dict(tag='a', n=4, l=0, sigma=4, D=-1, nu=0, delta=0, g=4.0),
                 dict(tag='b', n=3, l=1, sigma=4, D=-1, nu=0, delta=0, g=3.5),
                 dict(tag='c', n=5, l=0, sigma=5, D=-1, nu=0, delta=0, g=5.2)]
    w, a, _ = verdicts(synth_bad)
    good = (len(w) == 1 and len(a) == 1)
    ok &= good
    print(f"  CF4 broken synthetic ladder fails BOTH conditions   "
          f"within={len(w)} across={len(a)}   {'PASS' if good else '**FAIL**'}")

    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL** -- nothing is scored'}")
    return 0 if ok else 4


# ---------------------------------------------------------------- doubt82 binding
def bind_doubt(rows):
    D = Domain('gtest83 g-ladder, clause 1 route (c)',
               trusted='penetrating channels l<=3, where delta is a computed '
                       'property of the self-consistent F_core',
               doubted='l=4 (g) channels, whose banked D values sit at the '
                       'hydrogenic -1/(2n^2) to five decimals and may be a FLOOR '
                       'rather than a measurement')
    D.control('6d at Z=90 gives g = 6.382 +/- 0.001', region='trusted',
              expect='|g - 6.382| < 0.001',
              filed_in='PREDICTION-S83-ITEM1-GLADDER.md P6/worked example',
              sha_of=PRED)
    D.control('l=4 D values vary with Z at fixed n', region='doubted',
              expect='PASS iff spread in Z > 1e-5 at fixed n; P6 predicts FAIL',
              filed_in='PREDICTION-S83-ITEM1-GLADDER.md P6', sha_of=PRED)
    D.gate()

    # trusted
    z90 = next(r for r in rows if r['Z'] == 90)
    g6d = next(c['g'] for c in channels(z90) if c['tag'] == '6d')
    D.record('6d at Z=90 gives g = 6.382 +/- 0.001',
             abs(g6d - 6.382) < 0.001, f'g = {g6d:.6f}')

    # doubted -- sited where the instrument is NOT trusted
    seen = {}
    for r in rows:
        for tag, d in r['order']:
            m = TAG.match(tag)
            if m and m.group(2) == 'g':
                seen.setdefault(tag, set()).add(round(d, 8))
    spread = {t: (max(v) - min(v)) for t, v in seen.items()}
    worst = max(spread.values()) if spread else 0.0
    hyd = {t: abs(min(seen[t]) + 1.0 / (2.0 * int(TAG.match(t).group(1)) ** 2))
           for t in seen}
    D.record('l=4 D values vary with Z at fixed n', worst > 1e-5,
             f'max spread over Z = {worst:.2e}; max |D + 1/(2n^2)| = '
             f'{max(hyd.values()):.2e} over {len(seen)} g channels')
    return D


# ---------------------------------------------------------------- routes (c),(a)
def run():
    rc = canfail()
    if rc:
        return rc
    rows = bank()
    print()
    D = bind_doubt(rows)
    print()
    print(D.report())

    print("\n=== ROUTE (c) · THE g-LADDER AT THE RELAXED FIELD =====================")
    fail_w, fail_a, fail_m, per = [], [], [], []
    for r in rows:
        chs = channels(r)
        w, a, _ = verdicts(chs)
        mh = madelung_holds(chs)
        per.append(dict(Z=r['Z'], ent=r['ent'], within=w, across=a, mad=mh))
        if w:
            fail_w.append(r['Z'])
        if a:
            fail_a.append(r['Z'])
        if not mh:
            fail_m.append(r['Z'])

    n = len(rows)
    print(f"  rows scored (Z={ZLO}..{ZHI}, l<=3)                  {n}")
    print(f"  G-WITHIN violated (tie-break)                    {len(fail_w)} rows")
    print(f"  G-ACROSS violated (n+l ordering)                 {len(fail_a)} rows")
    print(f"  Madelung order != relaxed-field nu order         {len(fail_m)} rows")
    inter = sorted(set(fail_w + fail_a) & set(fail_m))
    union = sorted(set(fail_w + fail_a))
    print(f"  g-condition failures                             {len(union)} rows")
    print(f"  overlap with Madelung failures                   {len(inter)} rows")
    if union and fail_m:
        smaller = min(len(union), len(fail_m))
        print(f"  overlap / smaller set                            "
              f"{len(inter)}/{smaller} = {100*len(inter)//smaller}%")

    print("\n  --- ROUTE (a) · THE SAME STATEMENT, Z BY Z ---")
    print("  Z   ent   G-within        G-across       Madelung")
    shown = 0
    for p in per:
        if not p['within'] and not p['across'] and p['mad']:
            continue
        w = ','.join(f"{a}<{b}@s{s}" for s, a, b, _ in p['within'][:2]) or '-'
        a = ','.join(f"s{s}:{v:+.3f}" for s, v in p['across'][:2]) or '-'
        print(f"  {p['Z']:<4}{p['ent']:<6}{w:<16}{a:<15}{'ok' if p['mad'] else 'FAIL'}")
        shown += 1
    print(f"  ({shown} rows carry at least one flag; the rest are clean)")

    json.dump(dict(within=fail_w, across=fail_a, mad=fail_m, n=n),
              open(os.path.join(HERE, 'gtest83-out.json'), 'w'), indent=1)
    D.dump(os.path.join(HERE, 'doubt83-first-exercise.json'))
    return 0


# ---------------------------------------------------------------- route (b)
def relax():
    """The relaxation term expressed in g-units, at Z=90.  s81's FROZEN-FIELD
    eigenvalues against the RELAXED total-energy currency.  These are two different
    currencies and that is the whole point of the comparison (F79.2)."""
    pred_gate()
    eps = {('6d', 'Phi_d*'): -0.217248225,
           ('5f', 'Phi_d*'): -0.138004359,
           ('5f', 'Phi_f*'): -0.227905042}
    nl = {'6d': (6, 2), '5f': (5, 3)}
    print("\n=== ROUTE (b) · THE RELAXATION TERM IN g-UNITS, Z=90 ==================")
    print("  channel  field     E (Ha)          nu        delta      g")
    G = {}
    for (tag, fld), e in eps.items():
        n, l = nl[tag]
        d, nu = defect(n, e)
        G[(tag, fld)] = l + d
        print(f"  {tag:<9}{fld:<10}{e:<16.9f}{nu:<10.5f}{d:<11.5f}{l+d:.5f}")
    z90 = next(r for r in bank() if r['Z'] == 90)
    for c in channels(z90):
        if c['tag'] in nl:
            G[(c['tag'], 'relaxed')] = c['g']
            print(f"  {c['tag']:<9}{'relaxed':<10}{c['D']:<16.9f}"
                  f"{c['nu']:<10.5f}{c['delta']:<11.5f}{c['g']:.5f}")
    shift = G[('5f', 'Phi_f*')] - G[('5f', 'Phi_d*')]
    print(f"\n  5f relaxation shift in g-units   {shift:+.5f}")
    print(f"  fixed-field  g(6d)={G[('6d','Phi_d*')]:.4f}  "
          f"g(5f)={G[('5f','Phi_d*')]:.4f}   G-within "
          f"{'HOLDS' if G[('5f','Phi_d*')] > G[('6d','Phi_d*')] else '**FAILS**'}")
    print(f"  relaxed      g(6d)={G[('6d','relaxed')]:.4f}  "
          f"g(5f)={G[('5f','relaxed')]:.4f}   G-within "
          f"{'HOLDS' if G[('5f','relaxed')] > G[('6d','relaxed')] else '**FAILS**'}")
    return 0


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'run'
    sys.exit({'canfail': canfail, 'run': run, 'relax': relax}[cmd]())
