#!/usr/bin/env python3
"""chain89.py -- s89 · UNIT 1a · L3 AT THE PAIR. Prediction pack89/PREDICTION-S89-UNIT1A-PAIR.md
hashed BEFORE this file existed.  Per row: rank-1/rank-2 candidates by nu, both wells' J,
dg/dl = 2 - J_outer, banked Delta g/Delta l = (g2-g1)/(l2-l1).  Lever = region count.
usage: canfail | run Z.. | score
"""
import json, os, sys, math, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
for p in ('pack88', 'pack85', 'pack84', 'pack83', 'pack81', 'rt'):
    sys.path.insert(0, os.path.join(ROOT, p))
import numpy as np
import semi84 as S84, semi85 as S85
PRED = os.path.join(HERE, 'PREDICTION-S89-UNIT1A-PAIR.md'); PSHA = PRED.replace('.md', '.sha256')
OUT = os.path.join(HERE, 'chain89-out.json')


def gate_sha():
    want = open(PSHA).read().split()[0]; got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got: print("HALT rc=3 sha"); sys.exit(3)


def wells_of(E, l, qfun):
    J, meta = S84.J_of(E, l, qfun, detail=True)
    if J is None: return None
    L = l + 0.5
    Ji = (L / math.pi) * meta['I_inner'] if meta.get('I_inner') else None
    return dict(J=round(J, 6), J_inner=(None if Ji is None else round(Ji, 6)), n_regions=meta['n_regions'],
                r_outer=round(meta['r_outer'], 4), r_inner=round(meta['r_inner'], 4), dg_dl=round(2.0 - J, 6))


def canfail():
    gate_sha(); ok = True
    def rep(n, g, msg):
        nonlocal ok; ok = ok and bool(g); print(f"  {n} {msg}  {'PASS' if g else '**FAIL**'}")
    ONE = lambda rr: np.ones_like(np.atleast_1d(np.asarray(rr, float)))
    w = wells_of(-0.5 / (3.0 ** 2), 1, ONE)                     # n=3 p, charge 1
    rep('CF1', w and w['n_regions'] == 1 and abs(w['J'] - 1.0) < 1e-6, f"Coulomb: reg={w['n_regions']} J={w['J']}")
    # CF2 synthetic barrier: q(r) = 1 + 6*exp(-((r-0.5)/0.15)^2) -> inner well carved at l=2
    def qb(rr, a=6.0):
        rr = np.atleast_1d(np.asarray(rr, float)); return 1.0 + a * np.exp(-((rr - 0.5) / 0.15) ** 2)
    wb = wells_of(-0.02, 2, qb)
    rep('CF2', wb is not None and wb['n_regions'] == 2, f"barrier q: reg={None if wb is None else wb['n_regions']} J_out={None if wb is None else wb['J']} J_in={None if wb is None else wb['J_inner']}")
    wm = wells_of(-0.02, 2, lambda rr: qb(rr, 0.0))
    rep('CF3', wm is not None and wm['n_regions'] == 1, f"barrier removed (merge reportable): reg={None if wm is None else wm['n_regions']}")
    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}"); return ok


def run(zs):
    gate_sha(); import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time(); h, cfg, ent, eps, row, Etot = S84.field_of(Z); r = np.asarray(h.r, float)
        by_nu = sorted(G.channels(row, lmax=3), key=lambda c: c['nu'])
        rows = []
        for rank, c in enumerate(by_nu[:4]):
            n, l, E = c['n'], c['l'], float(c['D'])
            rr, q = S85.q_native(h, n, l)
            qfun = lambda x, r_=rr, q_=q: np.interp(np.log(np.clip(np.atleast_1d(np.asarray(x, float)), r_[0], r_[-1])), np.log(r_), q_)
            w = wells_of(E, l, qfun)
            d = dict(tag=c['tag'], n=n, l=l, E=E, nu=c['nu'], g=c['g'], rank=rank, occ=bool((n, l) in h.P))
            if w: d.update(w)
            rows.append(d)
        c1, c2 = by_nu[0], by_nu[1]
        banked = (c2['g'] - c1['g']) / (c2['l'] - c1['l']) if c2['l'] != c1['l'] else None
        r2 = rows[1]
        s7 = None if (banked is None or 'J' not in r2) else (np.sign(banked) == np.sign(r2['dg_dl']))
        out[str(Z)] = dict(Z=Z, ent=row['ent'], rows=rows, banked_dg_dl=banked, s7_agree=(None if s7 is None else bool(s7)), sec=int(time.time() - t0))
        print(f"  Z={Z} ent={row['ent']} banked dg/dl={banked!s:>8}  S7={'agree' if s7 else ('n/a' if s7 is None else 'DISAGREE')}  ({int(time.time()-t0)}s)")
        for d in rows:
            if 'J' in d:
                print(f"    r{d['rank']} {d['tag']:>3} occ={int(d['occ'])} reg={d['n_regions']} J_out={d['J']:.4f}" + (f" J_in={d['J_inner']:.4f}" if d['J_inner'] else "          ") + f" dg/dl={d['dg_dl']:+.4f} r[{d['r_inner']},{d['r_outer']}]")
            else: print(f"    r{d['rank']} {d['tag']:>3} no allowed region")
        json.dump(out, open(OUT, 'w'), indent=1)
    # LEVER on this run: region count must take >= 2 distinct values across frontier channels
    regs = {d['n_regions'] for Z in out for d in out[Z]['rows'][:2] if 'n_regions' in d}
    if len(regs) < 2:
        print(f"  **LEVER DEAD**: region counts seen {regs} -- rc=4 (P1 fails as the lever, reported)"); return 4
    print(f"  lever LIVE: region counts seen {sorted(regs)}"); return 0


def score():
    gate_sha(); out = json.load(open(OUT)); Zs = sorted(int(k) for k in out)
    print(f"=== SCORE chain89 rows {Zs} ===")
    s7 = [(Z, out[str(Z)]['s7_agree']) for Z in Zs if out[str(Z)]['s7_agree'] is not None]
    print(f"  P2 S7 agree {sum(1 for _, a in s7 if a)}/{len(s7)}; disagree at {[Z for Z, a in s7 if not a]}")
    bad3 = [(Z, d['tag'], d['J']) for Z in Zs for d in out[str(Z)]['rows'] if d.get('n_regions') == 2 and d['J'] >= 2]
    print(f"  P3 two-well channels with J_out >= 2: {bad3}")
    p4 = []
    for Z in Zs:
        o = out[str(Z)]; r1, r2 = o['rows'][0], o['rows'][1]
        if 'J' not in r1 or 'J' not in r2 or o['banked_dg_dl'] is None: continue
        pred = +1 if r1['J'] < 1.3 else np.sign(r2['dg_dl'])
        p4.append((Z, r1['tag'], round(r1['J'], 3), r2['tag'], round(r2['J'], 3), int(pred), int(np.sign(o['banked_dg_dl']))))
    print(f"  P4 (sign = sign(2-J2) unless J1<1.3 -> +): agree {sum(1 for x in p4 if x[5]==x[6])}/{len(p4)}")
    for x in p4: print(f"     Z={x[0]} r1 {x[1]} J={x[2]} r2 {x[3]} J={x[4]} pred {x[5]:+d} banked {x[6]:+d}{'' if x[5]==x[6] else '  <-- FAIL'}")
    f = [(Z, d['n_regions'], d['J'], d.get('J_inner')) for Z in Zs for d in out[str(Z)]['rows'] if d['tag'] == '5f' and 'J' in d]
    print(f"  P5 5f (Z, reg, J_out, J_in): {f}")
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail': sys.exit(0 if canfail() else 4)
    if a[0] == 'run': sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score': sys.exit(score())
