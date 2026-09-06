#!/usr/bin/env python3
"""score87.py -- S1..S7 of PREDICTION-S87-ITEM1-KINETIC-CAP.md. Population A = nu_rank 0,1."""
import json, os, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))


def fin(v): return isinstance(v, (int, float)) and math.isfinite(v)


def score():
    d = json.load(open(os.path.join(HERE, 'semi87-out.json')))
    A = [dict(r, Z=int(z)) for z, row in d.items() for r in row['rows'] if r.get('J') is not None and r['nu_rank'] <= 1]
    Kge = [r for r in A if r['K'] >= 1.0]
    print(f"rows {len(d)}  A {len(A)}  K>=1 {len(Kge)}")
    # S1 theorem: sup_orbit S'' <= Mu2 <= Mu1
    v1 = [r for r in A if not (r['Spp_orbit'] <= r['Mu2'] * (1 + 1e-9) <= r['Mu1'] * (1 + 1e-9))]
    idn = max(abs(r['Spp_orbit'] - r['Mu3']) / r['Mu3'] for r in A if r['Mu3'] > 0)
    print(f"S1 [A,74] sup S'' <= Mu2 <= Mu1: violations {len(v1)}/{len(A)}  filed 0  -> {'CORRECT' if not v1 else 'FALSIFIED'}"
          f"   (S''=r^2 rho_r identity: max rel dev {idn:.1e})")
    # S2 nesting
    bad = 0
    for r in A:
        seq = [r['Jtent'], r['Jmax1'], r['Jmax2'], r['Jmax3']]
        seq = [float('inf') if v == 'inf' else v for v in seq]
        for x, y in zip(seq, seq[1:]):
            if fin(y) and fin(x) and y > x + 1e-9: bad += 1
            if fin(x) and not fin(y): bad += 1
        if fin(seq[3]) and seq[3] < r['J'] - 1e-6: bad += 1
    print(f"S2 [A,74] nesting Jtent>=Jmax1>=Jmax2>=Jmax3>=J: violations {bad}  filed 0  -> {'CORRECT' if not bad else 'FALSIFIED'}")
    # S3, S4, S5
    c2 = [r for r in Kge if fin(r['Jmax2']) and r['Jmax2'] < 2]
    c3 = [r for r in Kge if fin(r['Jmax3']) and r['Jmax3'] < 2]
    print(f"S3 [A,K>=1,{len(Kge)}] certified by Mu2 (from T): {len(c2)}  filed <=2  -> {'CORRECT' if len(c2) <= 2 else 'FALSIFIED'}")
    okS4 = len(c3) <= 5 and all(r['l'] == 1 and r['K'] < 1.10 for r in c3)
    print(f"S4 [A,K>=1,{len(Kge)}] certified by Mu3 (sup-language ceiling): {len(c3)}  filed <=5, all p with K<1.10 -> {'CORRECT' if okS4 else 'FALSIFIED'}")
    for r in c3: print(f"     Z={r['Z']} {r['tag']} K={r['K']:.4f} J={r['J']:.4f} Jmax3={r['Jmax3']:.4f} tau3={r['tau3']:.3f}")
    df = [r for r in Kge if r['K'] >= 1.20]
    c5 = [r for r in df if fin(r['Jmax3']) and r['Jmax3'] < 2]
    print(f"S5 [A,K>=1.20,{len(df)}] certified by Mu3: {len(c5)}  filed 0  -> {'CORRECT' if not c5 else 'FALSIFIED'}")
    m21 = float(np.median([r['Mu1'] / r['Mu2'] for r in A])); m23 = float(np.median([r['Mu2'] / r['Mu3'] for r in A]))
    print(f"S6 [A,74] median Mu2/Mu3 = {m23:.1f} (>10 filed), median Mu1/Mu2 = {m21:.2f} (<3 filed) -> {'CORRECT' if m23 > 10 and m21 < 3 else 'FALSIFIED'}")
    mt = max(r['tau3'] for r in A)
    print(f"S7 [A,74] max tau3 = {mt:.3f}  filed <0.10 -> {'CORRECT' if mt < 0.10 else 'FALSIFIED'}")
    # the informative table by l
    print("\nINFORMATIVE FRACTION by l, population A, K>=1:  tau3 against tau*(K) (symmetric ramp, J<2)")
    for l in (1, 2, 3):
        g = [r for r in Kge if r['l'] == l]
        if not g: continue
        t3 = [r['tau3'] for r in g]; Ks = [r['K'] for r in g]
        print(f"  l={l}: n={len(g)}  K [{min(Ks):.3f},{max(Ks):.3f}]  tau3 median {np.median(t3):.3f} max {max(t3):.3f}  "
              f"certified by Mu3: {sum(1 for r in g if fin(r['Jmax3']) and r['Jmax3'] < 2)}  finite Jmax3: {sum(1 for r in g if fin(r['Jmax3']))}")
    # outside A, for the record
    B = [dict(r, Z=int(z)) for z, row in d.items() for r in row['rows'] if r.get('J') is not None and r['nu_rank'] > 1]
    cB = [r for r in B if r['K'] >= 1 and fin(r['Jmax3']) and r['Jmax3'] < 2]
    print(f"\nOUTSIDE A (nu_rank 2-4, {len(B)} channels): K>=1 certified by Mu3: " + ", ".join(f"Z={r['Z']} {r['tag']} K={r['K']:.3f} Jmax3={r['Jmax3']:.3f} tau3={r['tau3']:.3f}" for r in cB))
    sK = [r for r in B if r['l'] == 0 and r['K'] >= 1]
    print(f"s channels with K>=1 outside A: " + ", ".join(f"Z={r['Z']} {r['tag']} K={r['K']:.4f}" for r in sK))
    return 0


if __name__ == '__main__':
    score()
