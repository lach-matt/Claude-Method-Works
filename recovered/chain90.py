#!/usr/bin/env python3
"""chain90.py -- s90 ITEM 1 · L3-ACROSS dl=2 at the s->d collapse. Prediction
pack90/PREDICTION-S90-ITEM1-ACROSS-DL2.md hashed BEFORE this file existed.
usage: canfail | run Z.. | score
"""
import json, os, sys, math, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
for p in ('pack89', 'pack88', 'pack85', 'pack84', 'pack83', 'pack81', 'rt'):
    sys.path.insert(0, os.path.join(ROOT, p))
import numpy as np
import semi84 as S84, semi85 as S85
PRED = os.path.join(HERE, 'PREDICTION-S90-ITEM1-ACROSS-DL2.md'); PSHA = PRED.replace('.md', '.sha256')
OUT = os.path.join(HERE, 'chain90-out.json')
ROWS = {36: ('5s', '5p', '4d'), 37: ('5s', '5p', '4d'), 38: ('5s', '5p', '4d'),
        54: ('6s', '6p', '5d'), 55: ('6s', '6p', '5d'), 56: ('6s', '6p', '5d')}
PRE = {36, 37, 54, 55}; POST = {38, 56}


def gate_sha():
    want = open(PSHA).read().split()[0]; got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got: print("HALT rc=3 sha"); sys.exit(3)


def _phase(f, u1, u2):
    """int p dr over an allowed region in u=1/r: dr = du/u^2; p = sqrt(f). Endpoint zeros are
    sqrt-type (integrable, no singularity); same sin^2 substitution as semi84._quad."""
    th = 0.25 * math.pi * (S84._GLX + 1.0)
    s2 = np.sin(th) ** 2
    u = u1 + (u2 - u1) * s2
    val = f(u)
    jac = 2.0 * (u2 - u1) * np.sin(th) * np.cos(th)
    integ = np.where(val > 0, np.sqrt(np.maximum(val, 0.0)) / (u * u) * jac, 0.0)
    return float(0.25 * math.pi * np.sum(S84._GLW * integ))


def wells(E, l, qfun):
    """Per region: J, phase; plus delta_outer and delta_sc as defined in the prediction."""
    E = float(E); L = l + 0.5
    f = lambda u: 2.0 * E + 2.0 * qfun(1.0 / np.maximum(u, 1e-300)) * u - (L * L) * u * u
    fC = lambda u: 2.0 * E + 2.0 * u - (L * L) * u * u            # q == 1
    qmax = float(np.atleast_1d(qfun(1e-7))[0]); umax = 4.0 * (qmax + 1.0) / (L * L)
    regs = S84._regions(f, 1e-8, umax)
    if not regs: return None
    u1, u2 = regs[0]                                               # outer well
    J = (L / math.pi) * S84._quad(f, u1, u2)
    Ph_out = _phase(f, u1, u2)
    PhC_out = _phase(fC, u1, u2)                                   # Coulomb on the SAME interval
    Ph_in = sum(_phase(f, a, b) for a, b in regs[1:])
    # full Coulomb phase at (E,L): pi*(nu - L), nu = 1/sqrt(-2E); exact closed form
    nu = 1.0 / math.sqrt(-2.0 * E); PhC_full = math.pi * (nu - L)
    d_out = (Ph_out - PhC_out) / math.pi
    d_sc = (Ph_out + Ph_in - PhC_full) / math.pi
    return dict(J=round(J, 6), dg_dl=round(2.0 - J, 6), n_regions=len(regs),
                r_outer=round(1.0 / u1, 4), r_inner=round(1.0 / regs[-1][1], 4),
                phase_outer=round(Ph_out, 6), phase_inner=round(Ph_in, 6),
                delta_outer=round(d_out, 6), delta_sc=round(d_sc, 6))


def canfail():
    gate_sha(); ok = True
    def rep(n, g, msg):
        nonlocal ok; ok = ok and bool(g); print(f"  {n} {msg}  {'PASS' if g else '**FAIL**'}")
    ONE = lambda rr: np.ones_like(np.atleast_1d(np.asarray(rr, float)))
    # CF1 Coulomb n=3,l=1: J=1, delta_outer=0, delta_sc=0 (exact to quadrature)
    w = wells(-0.5 / 9.0, 1, ONE)
    rep('CF1', w and w['n_regions'] == 1 and abs(w['J'] - 1) < 1e-6 and abs(w['delta_outer']) < 1e-6 and abs(w['delta_sc']) < 1e-5,
        f"Coulomb: J={w['J']} d_out={w['delta_outer']} d_sc={w['delta_sc']}")
    # CF2 screened one-well q = 1 + 2 exp(-r): delta_sc must be POSITIVE and d_out nonzero (lever on delta)
    qs = lambda rr: 1.0 + 2.0 * np.exp(-np.atleast_1d(np.asarray(rr, float)))
    w2 = wells(-0.5 / 9.0, 1, qs)
    rep('CF2', w2 and w2['n_regions'] == 1 and w2['delta_sc'] > 0.01 and w2['delta_outer'] > 0.01,
        f"screened: d_out={w2['delta_outer']} d_sc={w2['delta_sc']}")
    # CF3 barrier (F89.1 siting) at l=2: two wells, inner phase > 0
    def qb(rr, a=6.0):
        rr = np.atleast_1d(np.asarray(rr, float)); return 1.0 + a * np.exp(-((rr - 1.0) / 0.2) ** 2)
    w3 = wells(-0.02, 2, qb)
    rep('CF3', w3 and w3['n_regions'] == 2 and w3['phase_inner'] > 0, f"barrier: reg={w3 and w3['n_regions']} Ph_in={w3 and w3['phase_inner']}")
    w4 = wells(-0.02, 2, lambda rr: qb(rr, 0.0))
    rep('CF4', w4 and w4['n_regions'] == 1, f"barrier removed: reg={w4 and w4['n_regions']}")
    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}"); return ok


def run(zs):
    gate_sha(); import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time(); h, cfg, ent, eps, row, Etot = S84.field_of(Z)
        chs = {c['tag']: c for c in G.channels(row, lmax=3)}
        rec = dict(Z=Z, ent=row['ent'], ch={})
        for tag in ROWS[Z]:
            c = chs.get(tag)
            if c is None: rec['ch'][tag] = None; print(f"  Z={Z} {tag} ABSENT from banked row"); continue
            n, l, E = c['n'], c['l'], float(c['D'])
            rr, q = S85.q_native(h, n, l)
            qfun = lambda x, r_=rr, q_=q: np.interp(np.log(np.clip(np.atleast_1d(np.asarray(x, float)), r_[0], r_[-1])), np.log(r_), q_)
            w = wells(E, l, qfun)
            d = dict(n=n, l=l, E=E, nu=c['nu'], g=c['g'], delta=c['delta'], occ=bool((n, l) in h.P))
            if w: d.update(w)
            rec['ch'][tag] = d
        s, p, dd = (rec['ch'][t] for t in ROWS[Z])
        if s and dd and 'g' in s and 'g' in dd:
            rec['banked_across'] = dd['g'] - s['g']
            rec['a_across'] = (dd['l'] + dd['delta_outer'] - s['g']) if 'delta_outer' in dd else None
            if p and 'dg_dl' in p and 'dg_dl' in s and 'dg_dl' in dd:
                rec['b_across'] = 0.5 * (s['dg_dl'] + p['dg_dl']) + 0.5 * (p['dg_dl'] + dd['dg_dl'])
            rec['naive_across'] = 2 * 0.5 * (s['dg_dl'] + dd['dg_dl']) if 'dg_dl' in dd else None
        rec['sec'] = int(time.time() - t0); out[str(Z)] = rec
        print(f"  Z={Z} ent={row['ent']} banked g(d)-g(s)={rec.get('banked_across', float('nan')):+.4f} "
              f"(a)={rec.get('a_across')} (b)={rec.get('b_across')} naive={rec.get('naive_across')} ({rec['sec']}s)")
        for tag in ROWS[Z]:
            d = rec['ch'][tag]
            if d and 'J' in d:
                print(f"    {tag} occ={int(d['occ'])} reg={d['n_regions']} J={d['J']:.4f} dg/dl={d['dg_dl']:+.4f} "
                      f"delta={d['delta']:+.4f} d_sc={d['delta_sc']:+.4f} d_out={d['delta_outer']:+.4f} Ph_in={d['phase_inner']:.3f}")
        json.dump(out, open(OUT, 'w'), indent=1)
    regs = {out[z]['ch'][ROWS[int(z)][2]]['n_regions'] for z in out if out[z]['ch'].get(ROWS[int(z)][2]) and 'n_regions' in out[z]['ch'][ROWS[int(z)][2]]}
    if len(regs) < 2: print(f"  **LEVER DEAD** d-region counts {regs} rc=4"); return 4
    print(f"  lever LIVE: d-region counts {sorted(regs)}"); return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'canfail': sys.exit(0 if canfail() else 2)
    if a[0] == 'run': sys.exit(run([int(z) for z in a[1:]]))
