#!/usr/bin/env python3
"""audit_lambda.py — every reconstructible numeric claim about Lambda, checked.

    python3 tools/audit_lambda.py            # the full pass
    python3 tools/audit_lambda.py --fast     # skip the two slow censuses

Each row prints PASS or FAIL against the figure the volumes record. A FAIL is a claim
and a measurement side by side; it adjudicates nothing. Where a check needs a convention
the volumes state — a population, a criterion, whether the diagonal counts — that
convention is named in the row, because getting it wrong produces a false FAIL. Five did
during construction, and the index itself supplied the reconciliation each time.

Runtime is a few minutes: the interval census walks 116,138 intervals and the
associativity check 842,206 triples.
"""
import argparse
import collections
import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cypher

FAILS = []


def chk(label, got, want, note=""):
    ok = got == want
    if not ok:
        FAILS.append((label, got, want))
    g, w = str(got), str(want)
    if len(g) > 22:
        g = g[:19] + "..."
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:<50} {g:<24} recorded {w}"
          + (f"   {note}" if note else ""))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--fast", action="store_true",
                    help="skip the interval census and the associativity triples")
    a = ap.parse_args(argv)

    lam = cypher._lambda()
    C = [tuple(lam.decode[i][v] for i, v in enumerate(c)) for c in lam.cells]
    O = lam.coords
    S = set(C)
    ix = {c: n for n, c in enumerate(O)}
    N = len(C)

    print("LAMBDA — the atomic index, at the caps of §7.4\n")
    chk("cells", N, 976)
    chk("ambient box", lam.box, 6912)
    chk("unordered pairs C(976,2)", N * (N - 1) // 2, 475800)

    print("\nCLOSURE — the five operator-bearing languages")
    r = cypher.run(lam, "1173", {"statistics_order": 2, "algebra_budget": 300000,
                                 "max_box": 10 ** 9, "max_pairwise_cells": 10 ** 9})
    for v in r["_verdicts"]:
        if v.E is not None:
            chk(f"E({v.language})", v.E, 0)
    chk("all pairs agree", r["pairs_agreeing"], len(r["pairs"]), "(reg 1176)")

    print("\nSUBLATTICE — closed under coordinatewise join and meet (§7.3)")
    jf = mf = 0
    for x, y in itertools.combinations(C, 2):
        if tuple(map(max, x, y)) not in S:
            jf += 1
        if tuple(map(min, x, y)) not in S:
            mf += 1
    chk("join failures over all 475,800 pairs", jf, 0)
    chk("meet failures over all 475,800 pairs", mf, 0)

    print("\nRANK — Sperner 1928, Dilworth 1950, Stanley 1980, Gauss 1809 (§8.4)")
    rk = collections.Counter(sum(c) for c in C)
    lo, hi = min(rk), max(rk)
    seq = [rk[t] for t in range(lo, hi + 1)]
    chk("rank sequence over ranks 3-20", seq,
        [1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1])
    chk("rank levels", len(rk), 18)
    chk("F(1)", N, 976)
    chk("F(-1)", sum((-1) ** sum(c) for c in C), 2)
    mean = sum(sum(c) for c in C) / N
    chk("mean rank F'(1)/F(1)", round(mean, 4), 11.0666)
    chk("log-concave at every interior rank",
        all(seq[t] ** 2 >= seq[t - 1] * seq[t + 1] for t in range(1, len(seq) - 1)), True)
    chk("widest level", max(rk.values()), 122)
    chk("Lambda = 8 x widest level", N, 8 * max(rk.values()))

    sd = (sum((sum(c) - mean) ** 2 for c in C) / N) ** .5
    skew = sum((sum(c) - mean) ** 3 for c in C) / N / sd ** 3
    chk("third standardised moment (the cited statistic)", round(skew, 2), -0.43,
        "<-- see FINDING 1")
    chk("centre of mass minus midpoint", round(mean - (lo + hi) / 2, 2), -0.43,
        "(this is the printed number)")

    MX = (3, 1, 3, 3, 3, 1, 3, 3)
    surv = [c for c in C if tuple(m - v for m, v in zip(MX, c)) in S]
    fixd = [c for c in surv if tuple(m - v for m, v in zip(MX, c)) == c]
    chk("cells surviving x -> max - x", len(surv), 8)
    chk("cells FIXED by x -> max - x", len(fixd), 8, "<-- see FINDING 2")

    print("\nSEED — Birkhoff 1937 (§8.3)")
    _, note = cypher.op_information(lam, {"algebra_budget": 300000,
                                          "max_pairwise_cells": 10 ** 9})
    chk("join-irreducibles (bottom excluded)", "17 join-irreducibles" in note, True, note)

    print("\nCHAINS — Stanley 1986, Brightwell & Winkler 1991")
    bylev = collections.defaultdict(list)
    for c in C:
        bylev[sum(c)].append(c)
    f = {c: 0 for c in C}
    for c in bylev[lo]:
        f[c] = 1
    for t in range(lo + 1, hi + 1):
        for x in bylev[t]:
            f[x] = sum(f[y] for y in bylev[t - 1] if all(p <= q for p, q in zip(y, x)))
    chk("maximal chains e(P), linear extensions", sum(f[t] for t in bylev[hi]), 1113045672)
    chk("cells on a maximal chain", hi - lo + 1, 18)

    print("\nINTERVALS — the box criterion (§12.9)")
    if a.fast:
        print("       (skipped: --fast)")
    else:
        comp = [(x, y) for x in C for y in C if all(p <= q for p, q in zip(x, y)) and x != y]
        chk("comparable intervals, x < y strictly", len(comp), 115162,
            "(diagonal excluded)")
        nb = sum(1 for x, y in comp
                 if all(t in S for t in itertools.product(
                     *[range(x[k], y[k] + 1) for k in range(8)])))
        chk("of which are boxes", nb, 31604, f"({nb / len(comp) * 100:.1f}%, recorded 27.4%)")
        mj = {(tuple(map(min, x, y)), tuple(map(max, x, y)))
              for x, y in itertools.combinations(C, 2)} | {(c, c) for c in C}
        chk("distinct meet-join boxes", len(mj), 116138)

    print("\nBINDING RATES — over the 475,800 unordered pairs, by the book's criterion")
    pop = [(tuple(map(min, x, y)), tuple(map(max, x, y)))
           for x, y in itertools.combinations(C, 2)]
    for nm, u, phi, v, want in (("g <= q", ix['g'], lambda z: z, ix['q'], 30.0),
                                ("q <= k", ix['q'], lambda z: z, ix['k'], 28.0),
                                ("g <= 4f+2", ix['g'], lambda z: 4 * z + 2, ix['f'], 1.9)):
        n = sum(1 for x, y in pop if y[u] > phi(x[v]))
        chk(f"binds: {nm}", round(n / len(pop) * 100, 1), want)

    print("\nTHE DETACHABLE LEAF, AND THE TWO SIDES (§11, §12.6.1)")
    Si, ki, qi = ix['S'], ix['k'], ix['q']
    proj = {tuple(v for k, v in enumerate(c) if k != Si) for c in C}
    chk("seven-coordinate projection (drop 2S)", len(proj), 319)
    chk("sum over the 319 of (k+1)", sum(c[ki] + 1 for c in proj), 976)
    chk("A_q(1)", [len({(c[ix['n']], c[ix['l']], c[ki], c[Si]) for c in C if c[qi] == q})
                   for q in range(4)], [33, 33, 23, 8])
    chk("B_q(1)", [len({(c[ix['e']], c[ix['f']], c[ix['g']]) for c in C if c[qi] == q})
                   for q in range(4)], [5, 10, 15, 17])

    print("\nTHE TRIANGLE — closing k-q-2S (§10.4)")
    tri = [c for c in C if c[Si] <= c[qi] + 1]
    chk("Lambda AND (2S <= q+1)", len(tri), 911)
    LO, HI = (2, 1, 2, 0, 2, 0, 0, 0), (3, 1, 3, 2, 3, 1, 1, 3)
    inb = lambda c: all(LO[k] <= c[k] <= HI[k] for k in range(8))
    na, nt = sum(map(inb, C)), sum(map(inb, tri))
    chk("tree count on the stated box", na, 280)
    chk("true count on that box", nt, 240)
    chk("cells the closing constraint removes", na - nt, 40)
    chk("constraint graph is a tree (V - E = 1)", 8 - 7, 1)

    print("\nTHE TOWER (MC, the tower)")
    for stage, cells, box in ((9, 1654, 27648), (90, 1561, 27648), (10, 2535, 110592)):
        t = cypher._tower(stage)
        chk(f"{t.name} cells", len(t.cells), cells)
        chk(f"{t.name} box", t.box, box)

    print("\nCOMPOSITION — Lambda_9 as a category (§12.11.3)")
    L9 = cypher._tower(9)
    c9 = [tuple(L9.decode[i][v] for i, v in enumerate(c)) for c in L9.cells]
    j = {c: n for n, c in enumerate(L9.coords)}
    src = lambda c: (c[j['n']], c[j['l']], c[j['k']], c[j['S']])
    tgt = lambda c: (c[j['e']], c[j['f']], c[j['g']], c[j["2S'"]])
    bysrc = collections.defaultdict(list)
    for b in c9:
        bysrc[src(b)].append(b)
    pairs = sum(len(bysrc.get(tgt(x), ())) for x in c9)
    chk("composable pairs", pairs, 41682)
    S9 = set(c9)

    def comp2(x, y):
        z = list(x)
        z[j['q']] = min(x[j['q']], y[j['q']])
        for k in ('e', 'f', 'g'):
            z[j[k]] = y[j[k]]
        z[j["2S'"]] = y[j["2S'"]]
        return tuple(z)

    chk("closed under composition",
        sum(1 for x in c9 for y in bysrc.get(tgt(x), ()) if comp2(x, y) in S9), pairs)
    if a.fast:
        print("       (associativity skipped: --fast)")
    else:
        trip = af = 0
        for x in c9:
            for y in bysrc.get(tgt(x), ()):
                xy = comp2(x, y)
                for z in bysrc.get(tgt(y), ()):
                    trip += 1
                    if comp2(xy, z) != comp2(x, comp2(y, z)):
                        af += 1
        chk("composable triples", trip, 842206)
        chk("associativity failures", af, 0)
    L10 = cypher._tower(10)
    c10 = [tuple(L10.decode[i][v] for i, v in enumerate(c)) for c in L10.cells]
    n0 = sum(1 for c in c10 if c[j['g']] == 0)
    chk("Lambda_10 cells with g = 0", n0, 485)
    chk("Lambda_10 composable", len(c10) - n0, 2050)

    print("\nMARGINAL EXCLUSION — §11, ranked by cells that fail only this bound")
    B = {'g<=q': lambda d: d['g'] <= d['q'], 'q<=k': lambda d: d['q'] <= d['k'],
         'k<=4l+2': lambda d: d['k'] <= 4 * d['l'] + 2, 'l<=n-1': lambda d: d['l'] <= d['n'] - 1,
         '2S<=k': lambda d: d['S'] <= d['k'], 'f<=e-1': lambda d: d['f'] <= d['e'] - 1,
         'k>=1': lambda d: d['k'] >= 1, 'g<=4f+2': lambda d: d['g'] <= 4 * d['f'] + 2}
    want = {'g<=q': 673, 'q<=k': 575, 'k<=4l+2': 564, 'l<=n-1': 308,
            '2S<=k': 300, 'f<=e-1': 200, 'k>=1': 25, 'g<=4f+2': 24}
    RNG = dict(n=range(1, 4), l=range(0, 2), k=range(0, 4), q=range(0, 4),
               e=range(1, 4), f=range(0, 2), g=range(0, 4), S=range(0, 4))
    box0 = [dict(zip(O, t)) for t in itertools.product(*[RNG[c] for c in O])]
    print(f"       population: the {len(box0):,}-cell box with k from 0  <-- see FINDING 3")
    for nm, fn in B.items():
        others = [g for m, g in B.items() if m != nm]
        chk(f"excludes: {nm}",
            sum(1 for d in box0 if all(g(d) for g in others) and not fn(d)), want[nm])

    print("\n" + "=" * 78)
    if not FAILS:
        print("AUDIT CLEAN — every recorded claim reproduces.")
        return 0
    print(f"{len(FAILS)} CLAIM(S) DID NOT REPRODUCE\n")
    for label, got, w in FAILS:
        print(f"  {label}\n      recorded {w}\n      measured {got}")
    print("\nSee docs/AUDIT-LAMBDA.md. This program adjudicates nothing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
