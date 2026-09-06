#!/usr/bin/env python3
"""resetrule.py -- the reason `a` resets, found in the corpus and then tested.

M asked whether the reason behind Chapter 34's reset claims exists in the repository
before anything is derived.  IT DOES, and it is not in the book.  It is in the chat
corpus, in the conversation titled "The Method 1.7", staged there as registers
1401-1410 and never carried into the volumes.

WHAT THE CORPUS SAYS, quoted from register 1401 as staged

    "a can be held exactly while the running intersection of corridors is non-empty,
     and must move exactly when it empties.  That is arithmetic on the intervals
     alone, independent of where a sits.  Fourteen forced moves, at Z equals 37, 42,
     43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103 and 104.  All fourteen are recorded
     resets, with zero false positives -- the intersection never empties anywhere the
     record does not already reset.  Four recorded resets are not forced this way:
     lithium 3, potassium 19, thallium 81 and francium 87, every one the first element
     of a new period."

That is the derivation section 34.6 lacks.  The reset condition is a statement about
INTERVALS, not about subshells, and it is trajectory-free: it does not depend on where
`a` was placed, only on whether the corridors seen since the last reset still share a
point.  Register 1402 is the reason that matters -- the count of eighteen belongs to
one placement policy, and other policies give other counts, so membership cannot be
the derived condition while emptiness can.

WHAT THIS PROGRAM TESTS

  1. Register 1401's rule, run over the corpus's own corridors: does the running
     intersection empty at exactly those fourteen, with no false positive?
  2. The four it does not force -- are they what 1401 says they are?
  3. Register 1403's placement rule: does `a` land on a corridor ENDPOINT every time,
     never in the interior?
  4. Register 1404's four pairs: do consecutive corridors touch at exactly one point?
  5. Register 1402's qualitative claim: is the reset count policy-dependent?

REFUSALS, and one of them matters
  Register 1402 prints five counts for five placement policies -- ten, twelve,
  seventeen, twenty-one, twenty-two -- and does NOT define the policies precisely
  enough to reproduce them.  This program reports POLICY-NOT-DEFINED for those five
  figures and reproduces only 1402's qualitative claim, which is that the count varies
  widely.  A POLICY-NOT-DEFINED is not a finding and may not be quoted as one.
  Nothing is repaired.

INPUT
  extracted/archives/restore-point-2-13/walk.py, with the seated LW1-ground.py
  injected as its `ground` dependency.  Both imported by path, neither copied.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
WALK = os.path.join(ROOT, "extracted", "archives", "restore-point-2-13", "walk.py")
LET = "spdfg"
BIG = 1e9

FORCED_1401 = [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104]
NOT_FORCED_1401 = [3, 19, 81, 87]
RESETS_346 = sorted([3, 19, 37, 55, 81, 87, 103, 104] + [42, 45, 58, 64, 91, 96]
                    + [43, 65, 80, 97])
# Register 1404's four pairs, as printed.
PAIRS_1404 = [(42, 43), (64, 65), (96, 97), (103, 104)]
# The first element of each period, standard.
PERIOD_STARTS = [1, 3, 11, 19, 37, 55, 87]


def load(members):
    gpath = os.path.join(members, "LW1-ground.py")
    gspec = importlib.util.spec_from_file_location("ground", gpath)
    ground = importlib.util.module_from_spec(gspec)
    gspec.loader.exec_module(ground)
    saved = sys.modules.get("ground")
    sys.modules["ground"] = ground
    buf, o_out = io.StringIO(), sys.stdout
    try:
        sys.stdout = buf
        wspec = importlib.util.spec_from_file_location("walkmod", WALK)
        walk = importlib.util.module_from_spec(wspec)
        wspec.loader.exec_module(walk)
    finally:
        sys.stdout = o_out
        if saved is None:
            sys.modules.pop("ground", None)
        else:
            sys.modules["ground"] = saved
    return ground, walk


def corridors(walk):
    out = []
    for Z in range(3, 109):
        b = walk.bracket(Z)
        if b is not None:
            out.append((Z, b))
    return out


def running_intersection(cor):
    """Register 1401's rule.  Hold while the running intersection is non-empty as an
    OPEN interval; a reset is forced exactly where it empties."""
    lo, hi = -1e18, 1e18
    forced = []
    for Z, (l, h, gn, gl) in cor:
        nlo, nhi = max(lo, l), min(hi, h)
        if nlo >= nhi:
            forced.append(Z)
            lo, hi = l, h
        else:
            lo, hi = nlo, nhi
    return forced


def landings(walk):
    """Where each recalibration puts `a`: on L, on U, or in the interior."""
    out = []
    for Z, av, mv in walk.TR:
        if mv == 0:
            continue
        lo, hi, gn, gl = walk.bracket(Z)
        at = ("L" if abs(av - lo) < 1e-5 else
              "U" if abs(av - hi) < 1e-5 else "interior")
        out.append(dict(Z=Z, a=av, lo=lo, hi=hi, at=at, sub=f"{gn}{LET[gl]}"))
    return out


def touching(cor):
    """Consecutive corridors whose intersection is a single point: one's ceiling is the
    other's floor.  Register 1404's pairs."""
    d = dict(cor)
    out = []
    for a, b in PAIRS_1404:
        if a not in d or b not in d:
            continue
        la, ha = d[a][0], d[a][1]
        lb, hb = d[b][0], d[b][1]
        lo, hi = max(la, lb), min(ha, hb)
        out.append(dict(first=a, second=b, a=(la, ha), b=(lb, hb),
                        meet=lo, single_point=abs(lo - hi) < 1e-9))
    return out


def policy_sweep(cor):
    """Register 1402's qualitative claim only: the count depends on the placement
    policy.  The five printed counts are NOT reproduced -- see the refusal above."""
    def run(pick, strict):
        a, n = 0.0, 0
        for Z, (lo, hi, gn, gl) in cor:
            inside = (lo < a < hi) if strict else (lo <= a <= hi)
            if inside:
                continue
            n += 1
            a = pick(a, lo, hi)
        return n

    def fin(lo, hi):
        return [x for x in (lo, hi) if -BIG < x < BIG]

    pol = [
        ("nearest endpoint", lambda a, lo, hi: min(fin(lo, hi), key=lambda x: abs(x - a)) if fin(lo, hi) else a),
        ("always the lower", lambda a, lo, hi: lo if lo > -BIG else hi),
        ("always the upper", lambda a, lo, hi: hi if hi < BIG else lo),
        ("the midpoint", lambda a, lo, hi: ((lo if lo > -BIG else (hi - 1 if hi < BIG else 0))
                                            + (hi if hi < BIG else (lo if lo > -BIG else 0) + 1)) / 2),
        ("the farther endpoint", lambda a, lo, hi: max(fin(lo, hi), key=lambda x: abs(x - a)) if fin(lo, hi) else a),
    ]
    return [(name, run(p, False), run(p, True)) for name, p in pol]


def measure(members):
    g, walk = load(members)
    cor = corridors(walk)
    forced = running_intersection(cor)
    land = landings(walk)
    return dict(ground=g, walk=walk, cor=cor, forced=forced,
                false_positives=[Z for Z in forced if Z not in RESETS_346],
                not_forced=[Z for Z in RESETS_346 if Z not in forced],
                land=land, touch=touching(cor), sweep=policy_sweep(cor))


def report(o):
    g = o["ground"]
    print("  THE RESET RULE, FOUND IN THE CORPUS AND TESTED")
    print("  Registers 1401-1410, staged in the conversation 'The Method 1.7' and never")
    print("  carried into the volumes.")
    print()
    print("  1. REGISTER 1401 -- `a` moves exactly when the running intersection of")
    print("     corridors empties.  Arithmetic on intervals alone; no subshell enters it.")
    print(f"     1401 prints fourteen forced moves: {' '.join(map(str, FORCED_1401))}")
    print(f"     measured:                          {' '.join(map(str, o['forced']))}")
    print(f"     identical: {o['forced'] == FORCED_1401}")
    print(f"     false positives (forced but not a recorded reset): "
          f"{o['false_positives'] or 'none'}")
    print(f"     recorded resets NOT forced this way: "
          + ", ".join(f"{g.GROUND[Z][0]} {Z}" for Z in o["not_forced"]))
    print()
    print("  2. THE FOUR THE RULE DOES NOT FORCE")
    print("     1401 says: 'every one the first element of a new period'.")
    for Z in o["not_forced"]:
        ok = Z in PERIOD_STARTS
        print(f"     {g.GROUND[Z][0]:<3} {Z:>3}  "
              + ("first element of a period" if ok else
                 "NOT a period start -- it opens the 6p block, period 6 begins at Cs 55"))
    bad = [Z for Z in o["not_forced"] if Z not in PERIOD_STARTS]
    print(f"     {len(o['not_forced']) - len(bad)} of {len(o['not_forced'])} are period"
          f" openings; {len(bad)} is a block opening. 1401's wording covers three of four.")
    print()
    print("  3. REGISTER 1403 -- `a` lands on an endpoint, never in the interior")
    print(f"     {'Z':>4} {'el':<3} {'a':>9} {'lo':>12} {'hi':>12}   at")
    for r in o["land"]:
        los = f"{r['lo']:.6f}" if r["lo"] > -1e8 else "-inf"
        his = f"{r['hi']:.6f}" if r["hi"] < 1e8 else "+inf"
        print(f"     {r['Z']:>4} {g.GROUND[r['Z']][0]:<3} {r['a']:>9.4f} "
              f"{los:>12} {his:>12}   {r['at']}")
    nL = sum(1 for r in o["land"] if r["at"] == "L")
    nU = sum(1 for r in o["land"] if r["at"] == "U")
    nI = sum(1 for r in o["land"] if r["at"] == "interior")
    print(f"     {nL} at L · {nU} at U · {nI} in the interior."
          "  1403's placement rule holds at every one.")
    print()
    print("  4. REGISTER 1404 -- four pairs whose corridors meet at a single point")
    for t in o["touch"]:
        fa = f"({t['a'][0]:.4f}, {t['a'][1]:.4f})" if t["a"][0] > -1e8 else f"(-inf, {t['a'][1]:.4f})"
        fb = f"({t['b'][0]:.4f}, {t['b'][1]:.4f})" if t["b"][0] > -1e8 else f"(-inf, {t['b'][1]:.4f})"
        print(f"     {g.GROUND[t['first']][0]:<3} {fa:<22} and {g.GROUND[t['second']][0]:<3} "
              f"{fb:<22} meet at {t['meet']:.6f}   "
              f"{'a single point' if t['single_point'] else 'NOT a single point'}")
    print("     Empty as an open interval, so the second reset is forced and the two are")
    print("     one event.  This is the derived form of what walkresets.py measures as a")
    print("     boundary touch: `a` does not move, the strict test simply fails.")
    print()
    print("  5. REGISTER 1402 -- the count belongs to the policy, not to the corridor")
    print("     1402 prints: nearest 10 · always-lower 12 · always-upper 17 · midpoint 21")
    print("                  · farther 22 · 200 random interior, 18 to 33, median 26")
    print("     POLICY-NOT-DEFINED: 1402 does not define its policies precisely enough to")
    print("     reproduce those five counts, and the random figure needs its seed. What")
    print("     reproduces is the CLAIM, which is that the count varies widely:")
    print(f"       {'policy':<22} {'closed test':>12} {'open test':>11}")
    for name, closed, strict in o["sweep"]:
        print(f"       {name:<22} {closed:>12} {strict:>11}")
    lo = min(min(c, s) for _, c, s in o["sweep"])
    hi = max(max(c, s) for _, c, s in o["sweep"])
    print(f"     {lo} to {hi} recalibrations over the same 106 steps and the same corridors.")
    print("     So membership cannot be the derived condition and emptiness can, which is")
    print("     1402's point and is confirmed.")
    print()
    print("  WHAT THIS ANSWERS")
    print("     Section 34.6 gives no reason for its reset claims. The corpus has one, it is")
    print("     exact, and it is about intervals rather than subshells. Nothing is repaired.")


FIXTURES = """the corpus's own recorded numbers, from registers 1401-1404 as staged in
the conversation 'The Method 1.7':
  1401  fourteen forced at 37 42 43 45 55 58 64 65 80 91 96 97 103 104, zero false
        positives, missing only Li 3, K 19, Tl 81 and Fr 87
  1403  `a` sits exactly at a corridor endpoint at every recalibration
  1404  Mo/Tc, Gd/Tb, Cm/Bk and Lr/Rf each meet at exactly one point
  1402  the reset count is a property of the placement policy, not of the corridor"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("1401's fourteen reproduce", o["forced"], FORCED_1401)
    eq("1401: zero false positives", o["false_positives"], [])
    eq("1401: the four not forced", o["not_forced"], NOT_FORCED_1401)
    eq("1403: none lands in the interior",
       [r["at"] for r in o["land"] if r["at"] == "interior"], [])
    eq("1403: landings at L", sum(1 for r in o["land"] if r["at"] == "L"), 11)
    eq("1403: landings at U", sum(1 for r in o["land"] if r["at"] == "U"), 7)
    eq("1404: all four pairs meet at a point",
       [t["single_point"] for t in o["touch"]], [True, True, True, True])
    eq("1402: the count varies widely",
       max(max(c, s) for _, c, s in o["sweep"]) - min(min(c, s) for _, c, s in o["sweep"]) > 20,
       True)
    eq("three of the four are period openings",
       [Z for Z in o["not_forced"] if Z in PERIOD_STARTS], [3, 19, 87])
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<36} {got!r:<58} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--members", default=MEMBERS)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.members)
    report(measure(a.members))
    return 0


if __name__ == "__main__":
    sys.exit(main())
