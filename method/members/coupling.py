#!/usr/bin/env python3
"""coupling.py — §12.11.2's lattice paragraph, re-derived. R4, on M's "complete R3 please".

WHAT IT SETTLES. §12.11.2 makes two different claims about meet-closure and they have very
different evidential standing:

  (1) THE TRIANGLE REGION, four caps and a parity variant — "the region {|2L-2S| <= 2J <= 2L+2S}
      is JOIN-closed — zero failures at caps 6, 8, 10 and 12 — and meet-broken at every one, by
      2,862, 12,489, 40,887 and 110,229 failing meets ... impose the parity congruence as well and
      the join closure dies too — 1,848 failures at cap 6".
      ALL FIVE FIGURES REPRODUCE EXACTLY HERE, from the region's own definition. So does the join
      closure, at every cap: zero.

  (2) THE FIVE PRESENTATIONS — "the exact coupling region is not a lattice in any presentation
      tried: as 2S' (50,592 failures), as parity alone (52,080), as the min-cap (17,856), as pair
      count (7,254), as (2S,2L,2J) (2,443 meets)".
      NOT REPRODUCED, and this instrument does not pretend otherwise. The five presentations are
      named in the prose and defined nowhere; FINDING-R4-02 established that no instrument in the
      repository prints any of the five counts. What IS recorded here is the search that was run
      and one arithmetic lead: 31 divides four of the five.

CONVENTION, fixed by the reproduction rather than assumed: pairs are UNORDERED and distinct, the
meet and join are componentwise min and max, and a "failure" is a pair whose meet (or join) is not
in the region. Counting ordered pairs doubles every figure and matches none of them.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, itertools, sys

PRINTED_MEET = {6: 2862, 8: 12489, 10: 40887, 12: 110229}
PRINTED_PARITY_JOIN_CAP6 = 1848
FIVE = {"2S'": 50592, "parity alone": 52080, "min-cap": 17856,
        "pair count": 7254, "(2S,2L,2J)": 2443}


def triangle(cap, parity=False):
    """{(2S,2L,2J) in [0,cap]^3 : |2L-2S| <= 2J <= 2L+2S}, optionally with the parity congruence."""
    R = set()
    for L in range(cap + 1):
        for S in range(cap + 1):
            for J in range(abs(L - S), min(L + S, cap) + 1):
                if parity and (J - L - S) % 2:
                    continue
                R.add((S, L, J))
    return R


def failures(R):
    """(meet failures, join failures) over unordered distinct pairs."""
    cells = sorted(R)
    m = j = 0
    for a, b in itertools.combinations(cells, 2):
        if tuple(map(min, a, b)) not in R:
            m += 1
        if tuple(map(max, a, b)) not in R:
            j += 1
    return m, j


def first_meet_failure(R):
    """the first failing meet in sorted order — §12.11.2 says it manufactures J = 1/2 from S = L = 0."""
    for a, b in itertools.combinations(sorted(R), 2):
        mt = tuple(map(min, a, b))
        if mt not in R:
            return a, b, mt
    return None


def report():
    print("§12.11.2, the triangle region {|2L-2S| <= 2J <= 2L+2S}, unordered distinct pairs")
    print(f"  {'cap':>5} {'cells':>7} {'meet-fail':>10} {'printed':>10} {'join-fail':>10}")
    for cap in sorted(PRINTED_MEET):
        R = triangle(cap)
        m, j = failures(R)
        mark = "OK" if m == PRINTED_MEET[cap] else "DIFFERS"
        print(f"  {cap:5} {len(R):7} {m:10} {PRINTED_MEET[cap]:10} {j:10}   {mark}")
    R6p = triangle(6, parity=True)
    m6p, j6p = failures(R6p)
    print(f"\n  with the parity congruence at cap 6: cells {len(R6p)}, join-fail {j6p} "
          f"(printed {PRINTED_PARITY_JOIN_CAP6}) {'OK' if j6p == PRINTED_PARITY_JOIN_CAP6 else 'DIFFERS'}, "
          f"meet-fail {m6p}")
    a, b, mt = first_meet_failure(triangle(6))
    print(f"  first failing meet at cap 6: {a} /\\ {b} = {mt}  "
          f"— 2S = 2L = {mt[0]},{mt[1]}, 2J = {mt[2]}, so J = {mt[2]}/2")
    print("\n  FIVE OF FIVE printed figures in that paragraph reproduce, and the join closure is")
    print("  exact at every cap. The componentwise minimum forgets that J is built from L and S.")

    print("\n§12.11.2's OTHER claim — the five presentations — is NOT reproduced here")
    for k, v in FIVE.items():
        print(f"  {k:14} {v:8}   divisible by 31: {'yes' if v % 31 == 0 else 'no '}"
              f"   {v // 31 if v % 31 == 0 else ''}")
    print("  31 divides four of the five. The presentations are named in the prose and defined")
    print("  nowhere, and FINDING-R4-02 established that no instrument here prints any of the five.")
    print("  Recorded as a lead, not as a finding.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    for cap, want in sorted(PRINTED_MEET.items()):
        m, j = failures(triangle(cap))
        eq(f"meet failures at cap {cap}", m, want)
        eq(f"join failures at cap {cap}", j, 0)
    R6p = triangle(6, parity=True)
    m6p, j6p = failures(R6p)
    eq("join failures at cap 6 with parity", j6p, PRINTED_PARITY_JOIN_CAP6)
    a, b, mt = first_meet_failure(triangle(6))
    eq("first failing meet has 2S = 2L = 0", (mt[0], mt[1]), (0, 0))
    eq("first failing meet has 2J = 1 (J = 1/2)", mt[2], 1)
    eq("cells at cap 8", len(triangle(8)), 369)
    eq("ordered counting would double cap 6", 2 * PRINTED_MEET[6], 5724)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
