#!/usr/bin/env python3
"""floor87.py -- s87 · ITEM 1b · THE FLOOR ON S''.  Prediction hashed before this file.
usage: canfail | run Z.. | score"""
import json, os, sys, math, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
for p in ('pack87', 'pack86', 'pack85', 'pack84', 'pack83', 'pack81', 'rt'):
    sys.path.insert(0, os.path.join(ROOT, p))
import numpy as np
import semi87 as S87, semi85 as S85, semi84 as S84
PRED = os.path.join(HERE, 'PREDICTION-S87-ITEM1b-FLOOR.md'); PSHA = PRED.replace('.md', '.sha256')
OUT = os.path.join(HERE, 'floor87-out.json')


def gate_sha():
    want = open(PSHA).read().split()[0]; got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got: print("HALT rc=3 sha"); sys.exit(3)


def J_floor_closed(b0, b1, m):
    """floor m~ + tent of mass K-m~: J = J_tent(b0'/(1-m/2), b1'/(1-m/2)) / sqrt(1-m/2)."""
    if m >= 2: return float('inf')
    s = 1.0 - 0.5 * m
    b0p, b1p = max(b0 - 0.5 * m, 0.0), max(b1 - 0.5 * m, 0.0)
    return S85.J_tent(b0p / s, b1p / s) / math.sqrt(s)


def J_floor_quad(b0, b1, m):
    b0p, b1p = max(b0 - 0.5 * m, 0.0), max(b1 - 0.5 * m, 0.0)
    K = b0p + b1p; tc = b1p / K if K > 0 else 0.5
    S = lambda t: -0.5 * m * t * (1 - t) + S87.Stilde_ramp(t, b0p, b1p, 0.0)
    return S87.J_profile(S, ramp=(tc - 1e-4, tc + 1e-4))


def rc_floor(b0, b1, m):
    b0p, b1p = max(b0 - 0.5 * m, 0.0), max(b1 - 0.5 * m, 0.0); K = b0p + b1p
    tc = b1p / K if K > 0 else 0.5
    return tc * (1 - tc) * (1 - 0.5 * m) + float(S87.Stilde_ramp(np.array([tc]), b0p, b1p, 0.0)[0])


def canfail():
    gate_sha(); ok = True
    def rep(n, g, msg):
        nonlocal ok; ok = ok and bool(g); print(f"  {n} {msg}  {'PASS' if g else '**FAIL**'}")
    a, b = J_floor_closed(0.55, 0.55, 0.30), J_floor_closed(0.55, 0.55, 0.0)
    rep('CF1', math.isfinite(a) and a < 2 and b == float('inf'), f"K=1.1: m~=0.30 J={a:.4f} (<2 certifies); m~=0 J={b}")
    q = J_floor_quad(0.55, 0.55, 0.30)
    rep('CF2', abs(q - a) < 1e-5, f"closed {a:.6f} vs quadrature {q:.6f}")
    c = J_floor_closed(0.55, 0.55, 0.15)
    rep('CF3', c > a, f"m~=0.15 J={c} vs m~=0.30 J={a:.4f} -- the floor moves J")
    d = J_floor_closed(0.70, 0.70, 0.30)
    rep('CF4', not (math.isfinite(d) and d < 2), f"K=1.40 m~=0.30 J={d} -- NOT certified")
    print(f"\n  CAN-FAIL GATE: {'PASS' if ok else '**FAIL**'}"); return ok


def run(zs):
    gate_sha()
    import gtest83 as G
    out = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for Z in zs:
        t0 = time.time()
        h, cfg, ent, eps, row, Etot = S84.field_of(Z); core = S87.core_numbers(h)
        r, rho = core['r'], core['rho_r']; rows = []
        for rank, c in enumerate(sorted(G.channels(row, lmax=3), key=lambda c: c['nu'])[:5]):
            n, l, E = c['n'], c['l'], float(c['D'])
            rr, q = S85.q_native(h, n, l); R = S85.channel_row(E, l, rr, q)
            if R is None: rows.append(dict(tag=c['tag'], l=l, nu_rank=rank, J=None)); continue
            orb = (r >= R['r_in']) & (r <= R['r_out']); L = l + 0.5
            Smin = float((r * r * rho)[orb].min()) if orb.any() else 0.0
            m = 2.0 * Smin / (L * L); b0, b1 = max(R['b0'], 0), max(R['b1'], 0)
            Jc = J_floor_closed(b0, b1, m); Jq = J_floor_quad(b0, b1, m) if math.isfinite(Jc) else float('inf')
            rows.append(dict(tag=c['tag'], l=l, nu_rank=rank, K=R['K'], J=R['J'], b0=b0, b1=b1, Smin=Smin, m=m,
                             Jtent=S85.J_tent(b0, b1), Jfloor=Jc, Jquad=Jq,
                             rc_tent=rc_floor(b0, b1, 0.0), rc_floor=rc_floor(b0, b1, m), rc_half=rc_floor(b0, b1, 0.5 * m)))
        live = [x for x in rows if x.get('J') is not None]
        lv = sorted(live, key=lambda x: x['l'])[0]
        d1 = lv['rc_floor'] - lv['rc_tent']; d2 = lv['rc_half'] - lv['rc_tent']
        if not (lv['m'] > 0 and d1 != 0 and d2 != 0 and abs(d1) > abs(d2)):
            print(f"  Z={Z}: **LEVER DEAD** at {lv['tag']} m={lv['m']:.3e} d1={d1:.3e} d2={d2:.3e}"); return 4
        cert = [x for x in live if x['nu_rank'] <= 1 and x['K'] >= 1 and math.isfinite(x['Jfloor']) and x['Jfloor'] < 2]
        print(f"  Z={Z} {row['ent']:>3} lever LIVE {lv['tag']} (rc {lv['rc_tent']:.3e} -> {lv['rc_floor']:.3e}, half {lv['rc_half']:.3e})  certified: "
              + ", ".join(f"{x['tag']} K={x['K']:.3f} m={x['m']:.3f} Jf={x['Jfloor']:.3f} J={x['J']:.3f}" for x in cert) + f"  ({int(time.time()-t0)}s)")
        out[str(Z)] = dict(Z=Z, ent=row['ent'], rows=[{k: ('inf' if v == float('inf') else v) for k, v in x.items()} for x in rows])
        json.dump(out, open(OUT, 'w'), indent=1)
    return 0


def score():
    d = json.load(open(OUT)); fin = lambda v: isinstance(v, (int, float)) and math.isfinite(v)
    A = [dict(x, Z=int(z)) for z, row in d.items() for x in row['rows'] if x.get('J') is not None and x['nu_rank'] <= 1]
    Kge = [x for x in A if x['K'] >= 1]; print(f"rows {len(d)} A {len(A)} K>=1 {len(Kge)}")
    f1 = sum(1 for x in A if fin(x['Jfloor']) and abs(x['Jfloor'] - x['Jquad']) > 1e-5)
    print(f"F1 closed==quadrature: violations {f1}  -> {'CORRECT' if not f1 else 'FALSIFIED'}")
    f2 = [x for x in A if fin(x['Jfloor']) and x['Jfloor'] < x['J'] - 1e-6]
    print(f"F2 Jfloor >= J: violations {len(f2)}  -> {'CORRECT' if not f2 else 'FALSIFIED'}")
    for x in f2: print(f"    Z={x['Z']} {x['tag']} J={x['J']:.4f} Jfloor={x['Jfloor']:.4f}")
    cert = [x for x in Kge if fin(x['Jfloor']) and x['Jfloor'] < 2]
    print(f"F3 certified by the floor: {len(cert)} of {len(Kge)}  filed >=15 -> {'CORRECT' if len(cert) >= 15 else 'FALSIFIED'}")
    for l, need, tot in ((1, 10, 30), (2, 3, 16), (3, 1, 4)):
        n = sum(1 for x in cert if x['l'] == l); print(f"F4 l={l}: {n} of {sum(1 for x in Kge if x['l']==l)}  filed >={need} -> {'CORRECT' if n >= need else 'FALSIFIED'}")
    five = [x for x in Kge if x['J'] >= 2]
    print(f"F5 J>=2 channels certified: {sum(1 for x in five if fin(x['Jfloor']) and x['Jfloor']<2)} of {len(five)}  filed 0")
    mm = float(np.median([x['m'] for x in A])); print(f"F6 median m~ = {mm:.4f}  filed >=0.05 -> {'CORRECT' if mm >= 0.05 else 'FALSIFIED'}")
    print("\nby l (A, K>=1): K range, m~ median, Jfloor finite, certified")
    for l in (1, 2, 3):
        g = [x for x in Kge if x['l'] == l]
        print(f"  l={l} n={len(g)} K[{min(x['K'] for x in g):.3f},{max(x['K'] for x in g):.3f}] m~ med {np.median([x['m'] for x in g]):.3f} max {max(x['m'] for x in g):.3f}"
              f" finite {sum(1 for x in g if fin(x['Jfloor']))} cert {sum(1 for x in g if fin(x['Jfloor']) and x['Jfloor']<2)}")
    print("\nuncertified K>=1 (Z tag K m~ K-m~ Jfloor J):")
    for x in Kge:
        if not (fin(x['Jfloor']) and x['Jfloor'] < 2): print(f"  {x['Z']} {x['tag']} {x['K']:.3f} {x['m']:.3f} {x['K']-x['m']:.3f} {x['Jfloor']} {x['J']:.3f}")
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'canfail': sys.exit(0 if canfail() else 4)
    if a[0] == 'run': sys.exit(run([int(x) for x in a[1:]]))
    if a[0] == 'score': sys.exit(score())
