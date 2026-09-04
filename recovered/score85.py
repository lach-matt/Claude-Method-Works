#!/usr/bin/env python3
"""score85.py -- S1..S10 against pack85/PREDICTION-S85-ITEM1-THE-BOUND.md.

**EVERY CLAUSE NAMES ITS POPULATION** (F83.1, twelfth appearance).
  A = width-2 frontier: nu_rank in {0,1}.   B = all l<=3 among the five lowest-nu.
"""
import json, os, math, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'semi85-out.json')
LSY = 'spdf'


def load():
    d = json.load(open(OUT))
    B, A = [], []
    for z in sorted(d, key=int):
        for r in d[z]['rows']:
            if r.get('J') is None:
                continue
            r = dict(r, Z=int(z), ent=d[z]['ent'])
            B.append(r)
            if r['nu_rank'] < 2:
                A.append(r)
    return A, B


def score():
    A, B = load()
    Zs = sorted({r['Z'] for r in B})
    print(f"=== SCORE · semi85 · {len(Zs)} rows · A={len(A)} frontier channels · "
          f"B={len(B)} channels ===")

    # S1 THEOREM
    viol = [r for r in B if r['J'] > r['Jbar'] + 1e-6]
    info = [r for r in B if r['K'] < 1.0]
    print(f"\n  S1 [THEOREM]  J <= Jbar(K) violations over B: {len(viol)}   "
          f"{'CORRECT' if not viol else '**FALSIFIED** ' + str(viol[:3])}")
    print(f"     the bound is INFORMATIVE (K<1) at {len(info)}/{len(B)} of B, "
          f"{len([r for r in A if r['K']<1])}/{len(A)} of A")

    # S2 ENTAILED
    ent = [(r['Z'], r['tag'], r['K'], r['J']) for r in B
           if (r['Z'], r['tag']) in ((89, '6d'), (90, '5f'))]
    ok2 = all(k >= 1.0 for _, _, k, _ in ent)
    print(f"\n  S2 [ENTAILED]  " + "  ".join(
        f"Z={z} {t}: K={k:.4f} J={j:.4f}" for z, t, k, j in ent) +
        f"   {'CORRECT' if ok2 else '**FALSIFIED**'}")

    # S3 / S4  over A
    hi = [r for r in A if r['K'] >= 1.0]
    hi_lo_l = [r for r in hi if r['l'] <= 1]
    print(f"\n  S3 [RISKY]  over A, l<=1 channels with K>=1: {len(hi_lo_l)}   "
          f"{'CORRECT' if not hi_lo_l else '**FALSIFIED**'}")
    for r in hi_lo_l[:8]:
        print(f"       Z={r['Z']} {r['tag']} rank{r['nu_rank']} K={r['K']:.4f} "
              f"J={r['J']:.4f}")
    hi_f = [r for r in hi if r['l'] == 3]
    ok4 = (not hi_lo_l) and bool(hi_f)
    print(f"  S4 [RISKY]  over A, K>=1 set: {len(hi)} channels, l=3 among them "
          f"{len(hi_f)}   {'CORRECT' if ok4 else '**FALSIFIED**'}")
    print(f"       K>=1 over A: " + ", ".join(
        f"Z{r['Z']}:{r['tag']}({r['K']:.4f},J={r['J']:.3f})" for r in hi))

    # S5 eccentricity, AS FILED and EXACT
    print(f"\n  S5 [RISKY]  median eps over A, by l   (filed eps vs exact Gamma/c*)")
    ok5 = True
    for l in range(4):
        v = [r['eps'] for r in A if r['l'] == l and r.get('eps')]
        w = [r['eps_exact'] for r in A if r['l'] == l and r.get('eps_exact')]
        if not v:
            continue
        print(f"       l={l} ({LSY[l]}) n={len(v):3d}  eps_filed={st.median(v):.4f}"
              f"   eps_exact={st.median(w):.4f}")
    tgt = {0: ('>', 0.90), 1: ('>', 0.60), 3: ('<', 0.45)}
    for l, (op, th) in tgt.items():
        v = [r['eps'] for r in A if r['l'] == l and r.get('eps')]
        if not v:
            print(f"       l={l}: NO CHANNELS IN A -- clause unscoreable")
            ok5 = False
            continue
        m = st.median(v)
        good = (m > th) if op == '>' else (m < th)
        ok5 = ok5 and good
        print(f"       l={l} filed {op}{th}: {m:.4f}  {'ok' if good else '**MISS**'}")
    z90 = [r for r in A if r['Z'] == 90 and r['tag'] == '5f']
    if z90:
        print(f"       Z=90 5f eps_filed={z90[0]['eps']:.4f} "
              f"eps_exact={z90[0]['eps_exact']:.4f} (filed <0.35)")
    print(f"     S5 {'CORRECT' if ok5 else '**FALSIFIED**'}")

    # S6 the s channel of A
    sch = [r for r in A if r['l'] == 0]
    ks = [(r['Z'], r['K']) for r in sch]
    rng = (min(k for _, k in ks), max(k for _, k in ks))
    mono = all(ks[i][1] <= ks[i + 1][1] + 1e-12 for i in range(len(ks) - 1))
    inband = all(0.80 < k < 1.00 for _, k in ks)
    print(f"\n  S6 [RISKY]  A's l=0 channels: n={len(ks)} K in [{rng[0]:.4f},"
          f"{rng[1]:.4f}]  monotone in Z={mono}  all in (0.80,1.00)={inband}   "
          f"{'CORRECT' if (mono and inband) else '**FALSIFIED**'}")
    print(f"       " + " ".join(f"{z}:{k:.4f}" for z, k in ks))

    # S7 Z=91
    z91 = [r for r in B if r['Z'] == 91 and r['tag'] == '5f']
    if z91:
        r = z91[0]
        print(f"\n  S7 [RISKY]  Z=91 5f rank{r['nu_rank']} K={r['K']:.4f} "
              f"J={r['J']:.4f}   {'CORRECT' if r['K']>=1 else '**FALSIFIED**'}")
    else:
        print(f"\n  S7 Z=91 has no 5f among the five lowest-nu -- unscoreable")

    # S8 count
    print(f"\n  S8 [RISKY]  |{{K>=1}}| over A = {len(hi)} (filed <=8)   "
          f"{'CORRECT' if len(hi)<=8 else '**FALSIFIED**'}")

    # S9 widening
    bad9 = [r for r in A if r['l'] <= 1 and r['J'] >= 2.0]
    j0 = [r['J'] for r in A if r['l'] == 0]
    j1 = [r['J'] for r in A if r['l'] == 1]
    b0 = [x for x in j0 if not (1.15 <= x <= 1.30)]
    b1 = [x for x in j1 if not (1.45 <= x <= 1.90)]
    print(f"\n  S9 [RISKY]  over A: l<=1 with J>=2: {len(bad9)}; "
          f"J(l=0) in [{min(j0):.4f},{max(j0):.4f}] outside 1.15-1.30 at {len(b0)}; "
          f"J(l=1) in [{min(j1):.4f},{max(j1):.4f}] outside 1.45-1.90 at {len(b1)}")
    print(f"     S9 {'CORRECT' if not (bad9 or b0 or b1) else '**FALSIFIED**'}")

    print(f"\n  S10 [FALSIFIED at CF8] the eccentricity rewriting is not exact for "
          f"varying q.  max|K-K_alt| over B = "
          f"{max(abs(r['K']-r['K_alt']) for r in B if r.get('K_alt')):.3e}")

    # THE SEPARATION, l=1 AGAINST l=3, over A -- the order's own test
    print(f"\n  === THE l-DISCRIMINATION, OVER A ===")
    for l in range(4):
        v = [r for r in A if r['l'] == l]
        if not v:
            continue
        print(f"    l={l} ({LSY[l]}) n={len(v):3d}  K median {st.median([r['K'] for r in v]):.4f}"
              f"  max {max(r['K'] for r in v):.4f}   J median "
              f"{st.median([r['J'] for r in v]):.4f}  max {max(r['J'] for r in v):.4f}"
              f"   K>=1 at {len([r for r in v if r['K']>=1])}")
    return 0


if __name__ == '__main__':
    score()
