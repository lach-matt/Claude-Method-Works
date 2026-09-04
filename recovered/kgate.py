"""kgate.py -- SESSION 69. Scores PREDICTION-K-HALF (sha256 d9bbb93d...).

Sealed data only: rt/nlchain.jsonl. NO SOLVES. No constant entered.

alpha(Z,n,l) = [D(n,l+1) - D(n,l)] / [D(n+1,l) - D(n,l)]     (pack64/alpha.py)
Extended here from l in 0..2 to l in 0..3, and split by the R 1255 / PD-4
centrifugal gate on the entering channel: GATED iff l >= l_core + 2, where
l_core is the largest l occupied in the configuration at Z-1.

METHODOLOGICAL LAW: the lever must be shown to move the output before any row
is scored, every run. rc=4 if the lever is dead or the null cannot fail.
"""
import os, sys, json, math
import statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(HERE, '..', 'rt', 'nlchain.jsonl')
SYM = 'spdfgh'
T = lambda n, l: f"{n}{SYM[l]}"

LMAX = 4          # compute alpha for l = 0..3, so the upper channel runs to g
TOL = 1e-4


def load():
    return {json.loads(x)['Z']: json.loads(x) for x in open(CHAIN)}


def cfg_at(Z, rows):
    """occupancy dict at atomic number Z, built from the chain's own entrants"""
    d = {(1, 0): 1}
    for z in range(2, Z + 1):
        n, l = rows[z]['ent_nl']
        d[(n, l)] = d.get((n, l), 0) + 1
    return d


def rows_alpha(rows):
    """every (Z, n, l, alpha, l_core, gated) the sealed chain supports"""
    out = []
    for Z in sorted(rows):
        if Z < 3:
            continue
        D = dict(rows[Z]['order'])
        c = cfg_at(Z - 1, rows)
        lcore = max(l for (n, l) in c)
        for n in range(2, 9):
            for l in range(0, LMAX):
                a, b, cc = T(n, l), T(n, l + 1), T(n + 1, l)
                if a in D and b in D and cc in D:
                    den = D[cc] - D[a]
                    if abs(den) > TOL:
                        out.append((Z, n, l, (D[b] - D[a]) / den,
                                    lcore, l >= lcore + 2))
    return out


def summarise(vals):
    n = len(vals)
    if n == 0:
        return None
    m = st.mean(vals)
    sd = st.stdev(vals) if n > 1 else 0.0
    se = sd / math.sqrt(n) if n > 1 else 0.0
    return n, m, sd, se, st.median(vals)


# ---------------------------------------------------------------- checks
def lever_check(data):
    """l must actually move alpha. Compare alpha at fixed (Z,n) across l."""
    byzn = {}
    for Z, n, l, a, lc, g in data:
        byzn.setdefault((Z, n), {})[l] = a
    spreads = [max(d.values()) - min(d.values())
               for d in byzn.values() if len(d) >= 2]
    if not spreads:
        return False, "no (Z,n) carries two l values -- lever untestable"
    md = st.median(spreads)
    return md > 0.05, f"median spread in alpha across l at fixed (Z,n) = {md:.4f} over {len(spreads)} cells"


def canfail_check(data):
    """the P-1 test must REJECT a deliberately wrong k."""
    r = [a / (l + 1) for Z, n, l, a, lc, g in data]
    s = summarise(r)
    if s is None:
        return False, "no rows"
    _, m, _, se, _ = s
    if se == 0:
        return False, "zero standard error -- test cannot reject anything"
    wrong = 2.0
    z_wrong = abs(m - wrong) / se
    return z_wrong > 2.0, f"null k={wrong} rejected at {z_wrong:.1f} s.e. -- the test can fail"


# ---------------------------------------------------------------- main
def main():
    rows = load()
    data = rows_alpha(rows)

    print("=" * 68)
    print("  CAN-FAIL AND LEVER CHECKS (run before any row is scored)")
    print("=" * 68)
    ok1, msg1 = lever_check(data)
    print(f"  LEVER    {'OK  ' if ok1 else 'DEAD'}  {msg1}")
    ok2, msg2 = canfail_check(data)
    print(f"  CANFAIL  {'OK  ' if ok2 else 'DEAD'}  {msg2}")
    if not (ok1 and ok2):
        print("\n  rc=4 -- instrument is not scoreable. No rows reported.")
        return 4
    print()

    print("=" * 68)
    print(f"  {len(data)} rows from the sealed chain, l = 0..{LMAX-1}")
    print("=" * 68)

    print("\n  P-1 · IS k EXACTLY ONE HALF?   ratio r = alpha/(l+1)")
    print(f"  {'l':>3} {'n':>5} {'mean r':>9} {'sd':>8} {'s.e.':>8} {'median':>9}")
    permeans = []
    for l in range(0, LMAX):
        v = [a / (l + 1) for Z, nn, ll, a, lc, g in data if ll == l]
        s = summarise(v)
        if s is None:
            print(f"  {l:>3} {'NO-DATA':>5}")
            continue
        n, m, sd, se, med = s
        permeans.append((l, m))
        print(f"  {l:>3} {n:>5} {m:>9.4f} {sd:>8.4f} {se:>8.4f} {med:>9.4f}")
    allr = [a / (l + 1) for Z, nn, l, a, lc, g in data]
    n, m, sd, se, med = summarise(allr)
    z = abs(m - 0.5) / se if se else float('inf')
    print(f"  {'ALL':>3} {n:>5} {m:>9.4f} {sd:>8.4f} {se:>8.4f} {med:>9.4f}")
    print(f"\n  distance from 0.500 : {m-0.5:+.4f}  =  {z:.1f} s.e.")
    mono = (len(permeans) >= 3 and
            (all(permeans[i][1] < permeans[i+1][1] for i in range(len(permeans)-1)) or
             all(permeans[i][1] > permeans[i+1][1] for i in range(len(permeans)-1))))
    print(f"  per-l means monotone in l : {mono}")
    print(f"  P-1 VERDICT : {'HELD' if (z <= 2.0 and not mono) else 'FALSIFIED'}")

    print("\n  P-2 · THE GATE AS DOMAIN EDGE   (gated iff l >= l_core + 2)")
    print(f"  {'set':>9} {'n':>5} {'mean r':>9} {'sd':>8} {'median':>9}")
    res = {}
    for lab, sel in (("UNGATED", False), ("GATED", True)):
        v = [a / (l + 1) for Z, nn, l, a, lc, g in data if g == sel]
        s = summarise(v)
        res[lab] = s
        if s is None:
            print(f"  {lab:>9} {'NO-DATA':>5}")
            continue
        n, mm, sd, se, med = s
        print(f"  {lab:>9} {n:>5} {mm:>9.4f} {sd:>8.4f} {med:>9.4f}")
    if res["GATED"] and res["UNGATED"]:
        gm, um = res["GATED"][4], res["UNGATED"][4]
        gs, us = res["GATED"][2], res["UNGATED"][2]
        print(f"\n  gated median below ungated : {gm < um}   ({gm:.4f} vs {um:.4f})")
        print(f"  gated carries the scatter  : {gs > us}   (sd {gs:.4f} vs {us:.4f})")
        print(f"  P-2 VERDICT : {'HELD' if (gm < um and gs > us) else 'FALSIFIED or PARTIAL'}")
    else:
        print("  P-2 VERDICT : NO-DATA on one side")

    print("\n  P-3 · l = 3 (f->g) BREAKS THE LAW")
    v3 = [a for Z, nn, l, a, lc, g in data if l == 3]
    if not v3:
        print("  NO-DATA at l=3 -- reported as NO-DATA, not as a held prediction.")
    else:
        s = summarise(v3)
        n, mm, sd, se, med = s
        print(f"  n={n}  mean alpha={mm:.4f}  sd={sd:.4f}  median={med:.4f}")
        print(f"  linear law demands 4k ~ 2.00-2.11 ; predicted < 1.00")
        print(f"  P-3 VERDICT : {'HELD' if med < 1.0 else 'FALSIFIED'}")

    print("\n  CARRIED CAVEAT F67.4: filtered subset; population claims inherit bias.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
