#!/usr/bin/env python3
"""walkresets.py -- the eighteen resets of section 34.6, and which of them move `a` at all.

Section 34.6 says:

    "`a` is carried between elements and resets eighteen times.  Every reset is a
     subshell opening (8), an aufbau exception (6), or the return from one (4).
     It never resets mid-subshell, which is why each subshell fills at constant `a`."

THE INSTRUMENT THAT PRODUCED THE EIGHTEEN IS HELD, and it states its own rule in its
own first lines:

    "THE HANDSHAKE -- a resets only when the previous atom's value fails.
     walk Z upward.  keep a if it still lies in the new bracket.
     if not, move it the MINIMUM distance to re-enter."

That is the reset rule, and it is a rule about the CARRIED VALUE, not about subshells:
`a` resets exactly when the value carried in from the previous element falls outside
the current step's corridor.  Nothing in it mentions a subshell, so "never resets
mid-subshell" is an observation about where the rule happens to fire, not a reason.

AND THE RULE FIRES IN TWO DIFFERENT WAYS, which the count of eighteen conceals.
walk.py tests `lo < a < hi` STRICTLY and then moves `a` by 1e-6 past the endpoint.
When the carried value sits exactly ON a corridor endpoint the test fails and a
"recalibration" is recorded -- but the value does not move.  This program separates
the two, because the distinction is what decides section 34.6's second clause.

  A REAL MOVE      |da| far above the 1e-6 nudge; `a` genuinely changes.
  A BOUNDARY TOUCH |da| = 1e-6 exactly; the carried value was already an endpoint of
                   the new corridor, and the walk steps it inside by an epsilon.

WHY IT MATTERS.  "Each subshell fills at constant `a`" is a claim about the VALUE.
A boundary touch does not change the value to any printed precision, so it cannot
falsify that clause; a real move can.  Scored on real moves the clause fails, and it
fails in ONE place rather than the several a count of all eighteen suggests.

INPUT
  extracted/archives/restore-point-2-13/walk.py -- the corpus's own walk, imported by
  path and never copied, with the seated member LW1-ground.py injected as its
  `ground` dependency.  walk.py's own `ground.py` in the delivery is byte-identical
  to the seated member (md5 236975ac23aa29960d4f7c2a4d200cd6).

REFUSALS
  This program does not rescore register 1333's 8 / 6 / 4 partition, which finding
  R4-01 measured exact and which stands.  It does not choose a placement policy: the
  policy is walk.py's own, minimum distance to re-enter, and a different policy would
  give a different count (register 1580: three values pierce all 106 corridors).
  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
WALK = os.path.join(ROOT, "extracted", "archives", "restore-point-2-13", "walk.py")
LET = "spdfg"
NUDGE = 1e-6
REAL = 1e-4          # far above the nudge, far below any genuine move measured here


def load(members):
    """Import the seated member, then run the corpus's own walk against it."""
    gpath = os.path.join(members, "LW1-ground.py")
    gspec = importlib.util.spec_from_file_location("ground", gpath)
    ground = importlib.util.module_from_spec(gspec)
    gspec.loader.exec_module(ground)

    saved = sys.modules.get("ground")
    sys.modules["ground"] = ground           # walk.py does `import ground as G`
    buf, o_out = io.StringIO(), sys.stdout
    try:
        sys.stdout = buf                     # walk.py prints its own report on import
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


def occupancy(g, Z):
    if Z < 1:
        return {}
    c = {}
    for n, l, o in g.expand(Z):
        c[(n, l)] = c.get((n, l), 0) + o
    return c


def spans(g, zmax=108):
    """Each subshell's filling span: first occupied -> first at capacity.  A subshell
    that never reaches capacity inside the table is carried with an open end."""
    first, done = {}, {}
    for Z in range(1, zmax + 1):
        for k, v in occupancy(g, Z).items():
            capk = 2 * (2 * k[1] + 1)
            if v > 0 and k not in first:
                first[k] = Z
            if v >= capk and k not in done:
                done[k] = Z
    return {k: (first[k], done.get(k)) for k in first}


def measure(members):
    g, walk = load(members)
    resets = []
    for Z, a_after, mv in walk.TR:
        if abs(mv) < 1e-12 and Z != 3:
            # walk.py records a reset whenever the strict test fails; a zero move at
            # any Z but the first is a boundary touch that rounded to exactly zero.
            pass
        if mv == 0 and Z != 3:
            continue
        b = walk.bracket(Z)
        resets.append(dict(Z=Z, el=g.GROUND[Z][0], sub=f"{b[2]}{LET[b[3]]}",
                           key=(b[2], b[3]), before=a_after - mv, after=a_after,
                           move=mv, lo=b[0], hi=b[1]))
    # walk.py's own count is len of the entries it recalibrated; recover it the same way
    recal = [t for t in walk.TR if t[2] != 0 or t[0] == 3]
    steps = len([t for t in walk.TR])
    # Z = 3 is not a reset: it is where `a` is first PLACED, from the initial 0.0,
    # because there is no carried value yet.  walk.py counts it among the eighteen and
    # that is right for its own purpose; it is separated here because the clause under
    # test is about a value being carried.
    init = [r for r in resets if r["Z"] == 3]
    rest = [r for r in resets if r["Z"] != 3]
    real = [r for r in rest if abs(r["move"]) >= REAL]
    touch = [r for r in rest if abs(r["move"]) < REAL]
    # Where does each REAL move land relative to the subshell that is ENTERING?
    op = {}
    prev = {}
    for Z in range(1, 109):
        cur = occupancy(g, Z)
        for k, v in cur.items():
            if v > 0 and prev.get(k, 0) == 0:
                op.setdefault(Z, []).append(k)
        prev = cur
    for r in resets:
        r["at_opening"] = r["key"] in op.get(r["Z"], [])
    # Register 1580's corridor census, and section 34.6's three forced values.
    # Same object, same instrument: walk.py's own bracket at every step.
    BIG = 1e9
    cor = []
    for Z in range(3, 109):
        b = walk.bracket(Z)
        if b is None:
            continue
        lo, hi, gn, gl = b
        cor.append(dict(Z=Z, el=g.GROUND[Z][0], lo=lo, hi=hi,
                        sub=f"{gn}{LET[gl]}",
                        kind=("both" if lo > -BIG and hi < BIG else
                              "below" if lo > -BIG else
                              "above" if hi < BIG else "unbounded")))
    # A maximum pairwise-disjoint set of intervals, and a minimum piercing set, are the
    # same greedy sweep by right endpoint -- which is why the two agreeing certifies both.
    iv = sorted(((max(c["lo"], -1e6), min(c["hi"], 1e6), c) for c in cor), key=lambda t: t[1])
    disjoint, pierce, last = [], [], -1e18
    for a, b_, c in iv:
        if a >= last:
            disjoint.append(c)
            pierce.append(b_ - 1e-9 if b_ < 1e6 else a + 1e-6)
            last = b_
    census = dict(rows=cor, disjoint=disjoint, pierce=pierce,
                  both=sum(1 for c in cor if c["kind"] == "both"),
                  below=sum(1 for c in cor if c["kind"] == "below"),
                  above=sum(1 for c in cor if c["kind"] == "above"),
                  unbounded=sum(1 for c in cor if c["kind"] == "unbounded"),
                  lr=[c for c in cor if c["Z"] == 103][0])
    sp = spans(g)
    notconst = []
    for k, (a, b) in sorted(sp.items(), key=lambda kv: kv[1][0]):
        end = b if b is not None else 108
        hits = [r for r in real if a < r["Z"] <= end]
        if hits:
            notconst.append(dict(sub=f"{k[0]}{LET[k[1]]}", opens=a, full=b,
                                 hits=hits, complete=b is not None))
    return dict(ground=g, steps=steps, resets=resets, real=real, touch=touch, init=init,
                census=census,
                notconst=notconst, spans=sp)


def report(o):
    print("  THE EIGHTEEN RESETS, AND WHICH OF THEM MOVE `a`")
    print(f"    walk.py's own run: {o['steps']} steps, {len(o['resets'])} recalibrations")
    print("    the rule, in walk.py's own words: keep `a` if it still lies in the new")
    print("    bracket; if not, move it the minimum distance to re-enter.")
    print()
    print(f"    {'Z':>4} {'el':<3} {'fills':<5} {'a before':>10} {'a after':>10} {'move':>11}   kind")
    for r in o["resets"]:
        kind = ("initial placement, no value carried yet" if r["Z"] == 3
                else "REAL MOVE" if abs(r["move"]) >= REAL
                else "boundary touch, value unchanged")
        print(f"    {r['Z']:>4} {r['el']:<3} {r['sub']:<5} {r['before']:>10.4f} "
              f"{r['after']:>10.4f} {r['move']:>+11.6f}   {kind}")
    print()
    print(f"    {len(o['real'])} REAL MOVES · {len(o['touch'])} boundary touches "
          f"· {len(o['init'])} initial placement · {len(o['resets'])} recalibrations in all")
    print()
    print("  WHERE THE REAL MOVES LAND RELATIVE TO THE ENTERING SUBSHELL")
    at, notat = [r for r in o["real"] if r["at_opening"]], [r for r in o["real"] if not r["at_opening"]]
    print(f"    {len(at)} of the {len(o['real'])} real moves are at the OPENING of the subshell entering:")
    print("      " + ", ".join(f"{r['el']} {r['Z']} ({r['sub']})" for r in at))
    if notat:
        print(f"    {len(notat)} is not:")
        for r in notat:
            print(f"      {r['el']} {r['Z']}, entrant {r['sub']}, which opened earlier"
                  " -- section 34.6's 'return from an exception'")
    print()
    print('  SECTION 34.6\'s SECOND CLAUSE: "each subshell fills at constant `a`"')
    print("    scored on REAL MOVES only, since a boundary touch does not change the value:")
    if not o["notconst"]:
        print("      no subshell carries a real move between its opening and its completion.")
    for nc in o["notconst"]:
        end = nc["full"] if nc["complete"] else "never completes in the table"
        where = ", ".join(f"{h['el']} {h['Z']} ({h['before']:.4f} -> {h['after']:.4f}, "
                          f"entrant {h['sub']})" for h in nc["hits"])
        print(f"      {nc['sub']:<3} opens Z {nc['opens']}, full {end}:  {where}")
    print()
    print("  REGISTER 1580's CORRIDOR CENSUS, AND SECTION 34.6's THREE FORCED VALUES")
    c = o["census"]
    print(f"    {len(c['rows'])} corridors: {c['both']} bounded both sides, "
          f"{c['below']} bounded below only, {c['above']} bounded above only, "
          f"{c['unbounded']} unbounded")
    print(f"    Lr 103's corridor: ({c['lr']['lo']:.6f}, {c['lr']['hi']:.6f})"
          f"  -- upper bound {c['lr']['hi']:.4f}")
    print(f"    largest pairwise-disjoint set: {len(c['disjoint'])} -- "
          + ", ".join(f"{d['el']} {d['Z']}" for d in c["disjoint"]))
    print(f"    smallest piercing set: {len(c['pierce'])} -- "
          + ", ".join(f"{p:.6f}" for p in c["pierce"]))
    print("    The two agree, which is what certifies both; and the three disjoint corridors")
    print("    are boron, lanthanum and lawrencium, exactly as section 34.6 names them.")
    print("    Every figure of register 1580 reproduces.  This one is VERIFIED, not a finding.")
    print()
    print("  READ TOGETHER, AND THIS IS THE SHAPE OF IT")
    print("    `a` never moves inside the filling of the subshell that is ENTERING: every")
    print("    real move is at that subshell's own opening, or at the one return from an")
    print("    exception.  So the first half of section 34.6's sentence is very nearly right.")
    print()
    print("    What defeats the second half is that SUBSHELLS OVERLAP.  5d is open when 4f")
    print("    enters, and 6d is open when 5f and 7p enter, so a move made at one subshell's")
    print("    opening lands in the middle of another's filling.  That is why 5d and 6d do")
    print("    not fill at constant `a` while every other subshell does, and it happens only")
    print("    in the d block, because d straddles f.  Nothing is repaired here.")


FIXTURES = """the corpus's own recorded numbers, from walk.py's banked output:
  section 34.6   106 steps, 106 satisfied, 18 recalibrations
  the trajectory a = 0.5774 from K, 1.0000 from Rb, 1.2168 from Cs, 0.7071 from Ce,
                 0.8090 from Hg, 1.0000 from Tl, 1.3938 from Fr, 1.3660 from Pa,
                 1.9841 from Lr -- nine values.  Four of them are the ns/(n-1)d crossings
                 section 34.5 gives a closed form for, and the walk computes that form's
                 OWN values: 0.5773503, 1.0000000, 1.2167605, 1.3938469.  Section 34.5
                 PRINTS 1.2168450 and 1.3938270 at n = 6 and 7, which is the record's
                 16z-04 / 34re-01 and is not this program's finding
  register 1580  73 bounded / 7 below-only / 26 above-only; Lr's upper bound 2.4409
  section 34.6   three forced values, B / La / Lr pairwise disjoint; largest disjoint
                 set and smallest piercing set agree at three"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("steps walked", o["steps"], 106)
    eq("recalibrations", len(o["resets"]), 18)
    eq("real moves", len(o["real"]), 9)
    eq("boundary touches", len(o["touch"]), 8)
    eq("initial placement", len(o["init"]), 1)
    eq("where the boundary touches are",
       [r["el"] for r in o["touch"]], ["Mo", "Tc", "Rh", "Gd", "Tb", "Cm", "Bk", "Rf"])
    eq("where the real moves are",
       [r["el"] for r in o["real"]], ["K", "Rb", "Cs", "Ce", "Hg", "Tl", "Fr", "Pa", "Lr"])
    vals = [round(r["after"], 4) for r in o["real"]]
    eq("the values a takes", vals,
       [0.5774, 1.0, 1.2168, 0.7071, 0.809, 1.0, 1.3938, 1.366, 1.9841])
    eq("subshells not filling at constant a",
       [nc["sub"] for nc in o["notconst"]], ["5d", "6d"])
    eq("real moves at the entrant's own opening",
       [r["el"] for r in o["real"] if r["at_opening"]],
       ["K", "Rb", "Cs", "Ce", "Tl", "Fr", "Pa", "Lr"])
    eq("real moves not at an opening",
       [r["el"] for r in o["real"] if not r["at_opening"]], ["Hg"])
    c = o["census"]
    eq("reg 1580: bounded both sides", c["both"], 73)
    eq("reg 1580: bounded below only", c["below"], 7)
    eq("reg 1580: bounded above only", c["above"], 26)
    eq("reg 1580: Lr's upper bound", round(c["lr"]["hi"], 4), 2.4409)
    eq("sec 34.6: largest disjoint set", len(c["disjoint"]), 3)
    eq("sec 34.6: the three forced", [d["el"] for d in c["disjoint"]], ["B", "La", "Lr"])
    eq("sec 34.6: smallest piercing set", len(c["pierce"]), 3)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<52} expected {want!r}")
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
