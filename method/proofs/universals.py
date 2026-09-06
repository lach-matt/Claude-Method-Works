#!/usr/bin/env python3
"""universals.py -- two universals of Chapter 34's law, tested where the book measures them.

Candidate D-21 of CANDIDATES-R4-subject-matter.tsv, and the record's 34re-03 and
34re-07.  Both are universal claims about the Loewdin law, and a universal is
settled by one counterexample.

  (1) "a is carried and resets eighteen times, NEVER MID-SUBSHELL"
      -- main sec 34.6, register 1333 and 1350.
      A mid-subshell reset is an entrant equal to the previous step's entrant --
      the convention is the record's, recorded with READ-ch34re.
      Tested against register 1401's own list of forced resets.

  (2) "p = 0 is the node floor, so L = -inf at EVERY f OPENING"
      -- register 1350, and the same claim at sec 34.
      p = n - l - 1 at an opening, where q = 0.  Tested at every f opening the
      observed order contains.

INPUT
  method/members/LW1-ground.py -- the seated member, register 1306, the observed
  NIST ASD 5.12 ground configurations.  It is imported by path and never copied.
  Nothing here is reconstructed: the entrant of each step is read off the observed
  configurations, and the reset list is register 1401's as printed.

REFUSALS
  This program tests two universals and reports where they fail.  It does not
  decide whether a is carried as one system or several, and it does not rescore
  the 8 / 6 / 4 partition -- that is register 1333's and it stands (finding
  R4-01, withdrawn).  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")

LET = "spdfg"

# Register 1401's fourteen forced resets, as printed.
FORCED_1401 = [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104]

# Sec 34.6's own eighteen, in its own three classes.  Register 1333 prints them and
# finding R4-01 measured the partition disjoint at 8 / 6 / 4 -- that partition stands
# and is not re-scored here.  The four not in register 1401's forced list are Li, K,
# Tl and Fr.
RESETS_346 = {
    "at a subshell opening, not an exception": [3, 19, 37, 55, 81, 87, 103, 104],
    "at an aufbau exception":                  [42, 45, 58, 64, 91, 96],
    "at the return from an exception":         [43, 65, 80, 97],
}


def load_ground(members):
    path = os.path.join(members, "LW1-ground.py")
    spec = importlib.util.spec_from_file_location("LW1_ground", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def entrants(g, zmax=108):
    """The entrant of each step, under the record's convention: the subshell whose
    occupancy grows most between Z-1 and Z.  Ties are broken by filling order,
    which is the order the configuration is printed in."""
    out = {}
    prev = None
    for Z in range(1, zmax + 1):
        cur = {}
        order = []
        for n, l, o in g.expand(Z):
            cur[(n, l)] = cur.get((n, l), 0) + o
            if (n, l) not in order:
                order.append((n, l))
        if prev is not None:
            grew = [(cur[k] - prev.get(k, 0), order.index(k), k) for k in cur
                    if cur[k] > prev.get(k, 0)]
            if grew:
                grew.sort(key=lambda t: (-t[0], t[1]))
                out[Z] = grew[0][2]
        prev = cur
    return out


def occupancy(g, Z):
    cur = {}
    for n, l, o in g.expand(Z):
        cur[(n, l)] = cur.get((n, l), 0) + o
    return cur


def opens_at(g, zmax=108):
    """Every Z at which a subshell becomes occupied having been empty at Z-1.

    A RE-opening counts, and it has to: the record's own partition calls Gd, Cm and
    Rf openings, and 5d, 6d and 6d are each empty at the step before.  Scoring only
    a subshell's FIRST appearance gives nine openings against the recovered
    instrument's twelve, and where a reconstruction disagrees with the record the
    finding is about the reconstruction (G0c).  This is that correction."""
    out = {}
    prev = {}
    for Z in range(1, zmax + 1):
        cur = occupancy(g, Z)
        for k, v in cur.items():
            if v > 0 and prev.get(k, 0) == 0:
                out.setdefault(Z, []).append(k)
        prev = cur
    return out


def first_seen(g, zmax=108):
    seen = {}
    for Z in range(1, zmax + 1):
        for k, v in occupancy(g, Z).items():
            if v > 0 and k not in seen:
                seen[k] = Z
    return seen


def rivals_below(g, Z, entrant, nmax=7, lmax=3):
    """Admissible candidates at step Z whose p lies strictly below the entrant's.

    Admissibility is the law's own: q < 2(2l+1), read at Z-1.  The candidate set
    n <= N_MAX, l <= 3 is the record's convention, named with READ-ch34re.  p is the
    law's own argument under the root, n - l - 1 + q/2(2l+1).
    """
    prev = occupancy(g, Z - 1)

    def p_of(n, l):
        cap = 2 * (2 * l + 1)
        return n - l - 1 + prev.get((n, l), 0) / cap

    pg = p_of(*entrant)
    out = []
    for n in range(1, nmax + 1):
        for l in range(0, min(lmax + 1, n)):
            if prev.get((n, l), 0) < 2 * (2 * l + 1) and p_of(n, l) < pg - 1e-12:
                out.append((n, l, p_of(n, l)))
    return pg, sorted(out, key=lambda t: t[2])


def filling_spans(g, zmax=108):
    """Each subshell's filling span: from the Z at which it first becomes occupied to
    the Z at which it first reaches capacity 2(2l+1)."""
    first, done = {}, {}
    for Z in range(1, zmax + 1):
        for k, v in occupancy(g, Z).items():
            cap = 2 * (2 * k[1] + 1)
            if v > 0 and k not in first:
                first[k] = Z
            if v >= cap and k not in done:
                done[k] = Z
    return {k: (first[k], done[k]) for k in first if k in done}


def measure(members):
    g = load_ground(members)
    ent = entrants(g)
    mid = [Z for Z in FORCED_1401 if Z in ent and ent.get(Z) == ent.get(Z - 1)]
    op = opens_at(g)
    seen = first_seen(g)
    f_open = sorted(((n, l), Z) for (n, l), Z in seen.items() if l == 3)
    f_p = []
    for (n, l), Z in f_open:
        pg, below = rivals_below(g, Z, (n, l))
        f_p.append((f"{n}{LET[l]}", Z, g.GROUND[Z][0], n - l - 1, pg, below))
    # The plainer test of the same universal, over all eighteen of sec 34.6's resets:
    # is the reset at a subshell OPENING, or inside a subshell already filling?
    allZ = sorted(z for v in RESETS_346.values() for z in v)
    inside = []
    for Z in allZ:
        e = ent.get(Z)
        if e is not None and e not in op.get(Z, []):
            since = max((y for y in range(1, Z) if e in op.get(y, [])), default=None)
            inside.append((Z, g.GROUND[Z][0], e, since))
    # The consequent's own test: does any reset fall strictly between a subshell's
    # opening and its completion?  If one does, that subshell does not fill at
    # constant a, whatever convention is used for the word "mid-subshell".
    spans = filling_spans(g)
    notconst = []
    for k, (a, b) in sorted(spans.items(), key=lambda kv: kv[1][0]):
        hits = [Z for Z in allZ if a < Z <= b]
        if hits:
            notconst.append((k, a, b, hits))
    return dict(ground=g, entrants=ent, openings=op, first=seen, mid=mid, f=f_p,
                resets=allZ, inside=inside, notconst=notconst,
                elements=len(g.GROUND),
                electrons_ok=sum(1 for Z in g.GROUND if g.occ_count(Z) == Z))


def report(o):
    g = o["ground"]
    print("  TWO UNIVERSALS OF CHAPTER 34's LAW, TESTED ON THE OBSERVED ORDER")
    print(f"    input: LW1-ground.py, register 1306, {o['elements']} elements, "
          f"electron counts {o['electrons_ok']}/{o['elements']}")
    print()
    print('  (1) "a resets eighteen times, NEVER MID-SUBSHELL"')
    print("      a mid-subshell reset = an entrant equal to the previous step's entrant")
    print("      tested on register 1401's own fourteen forced resets:")
    for Z in FORCED_1401:
        e, p = o["entrants"].get(Z), o["entrants"].get(Z - 1)
        tag = "  <== MID-SUBSHELL" if e == p else ""
        print(f"        Z {Z:>3}  {g.GROUND[Z][0]:<3}  entrant {e[0]}{LET[e[1]]}"
              f"   previous step {p[0]}{LET[p[1]]}{tag}")
    if o["mid"]:
        names = ", ".join(f"{g.GROUND[Z][0]} {Z}" for Z in o["mid"])
        print(f"      REFUTED at {len(o['mid'])} of the fourteen: {names}")
    else:
        print("      holds on all fourteen")
    print()
    print('  (1a) the same universal read plainly: is each of the eighteen resets AT AN OPENING?')
    print('       sec 34.6: "It never resets mid-subshell, which is why each subshell fills at')
    print('       constant a."  A reset inside a subshell already filling refutes both halves.')
    for Z, el, e, opened in o["inside"]:
        print(f"        Z {Z:>3}  {el:<3}  entrant {e[0]}{LET[e[1]]}, occupied since Z {opened}"
              f"  -- so this reset is inside a subshell already filling")
    print(f"      {len(o['inside'])} of sec 34.6's {len(o['resets'])} resets fall inside a subshell")
    print(f"      already filling; {len(o['resets']) - len(o['inside'])} are at an opening.")
    print()
    print('  (1b) the consequent, tested on its own terms:')
    print('       "which is why EACH SUBSHELL FILLS AT CONSTANT a" -- a subshell fails this if')
    print("       any reset falls strictly between its opening and its completion.")
    n = 0
    for (nn, ll), a, b, hits in o["notconst"]:
        n += len(hits)
        print(f"        {nn}{LET[ll]} opens Z {a}, full Z {b}:  resets at "
              + ", ".join(f"{g.GROUND[z][0]} {z}" for z in hits))
    print(f"      {len(o['notconst'])} subshells do not fill at constant a, carrying {n} resets"
          " between them.")
    print()
    print('  (2) "p = 0 is the node floor, so L = -inf at EVERY f opening"')
    print("      p = n - l - 1 at an opening, where q = 0")
    for name, Z, el, p, pg, below in o["f"]:
        tag = "" if p == 0 else "  <== p is NOT 0"
        print(f"        {name} opens at Z {Z} ({el})   p = n - l - 1 = {p}{tag}")
    bad = [f for f in o["f"] if f[3] != 0]
    if bad:
        print(f"      the PREMISE is refuted at {len(bad)} of {len(o['f'])}: "
              + ", ".join(f"{f[0]} (p = {f[3]})" for f in bad))
    print()
    print('      but the CONCLUSION -- "no rival lies below, so L = -inf" -- is tested separately,')
    print("      because a false reason does not make a false result:")
    for name, Z, el, p, pg, below in o["f"]:
        if below:
            names = ", ".join(f"{n}{LET[l]} (p = {q:g})" for n, l, q in below)
            print(f"        {name} at Z {Z}: {len(below)} admissible rival(s) below -- {names}")
        else:
            print(f"        {name} at Z {Z}: NO admissible rival below the entrant, so L = -inf HOLDS")
    print("      At 4f it holds because p = 0 is the node floor.  At 5f it holds for a")
    print("      different reason: p = 1, and every subshell with a lower p -- 1s, 2p, 3d,")
    print("      4f -- is FULL and therefore inadmissible.  The conclusion survives; the")
    print("      reason the book gives for it does not.")
    print("      This depends on the candidate set l <= 3, which is the record's convention:")
    print("      5g would have p = 0 and would lie below 5f if g subshells were admitted.")
    print()
    print("  The record's findings 34re-03 and 34re-07 are reproduced from the seated member")
    print("  rather than quoted, and both are widened: 34re-03 names two counterexamples and")
    print("  there are six; 34re-07's p = 1 at 5f refutes a premise whose conclusion survives.")
    print("  Nothing is repaired.")


FIXTURES = """the corpus's own recorded numbers:
  34re-03   'never resets mid-subshell' fails at Mo 42 and Rh 45 of register 1401's own list
  34re-07   5f opens with p = 1
  reg 1306  108 elements, every electron count exact
  reg 1401  fourteen forced resets: 37 42 43 45 55 58 64 65 80 91 96 97 103 104
  reg 1333  eighteen resets, 8 / 6 / 4, disjoint (finding R4-01)
  resets.py 'opens a subshell : 12 of 18' -- the recovered instrument's own reading
  sec 34.9  L = -inf at every f opening -- the conclusion, which holds"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("elements", o["elements"], 108)
    eq("electron counts exact", o["electrons_ok"], 108)
    eq("register 1401's forced resets", len(FORCED_1401), 14)
    eq("mid-subshell resets among them", o["mid"], [42, 45])
    eq("their elements", [o["ground"].GROUND[Z][0] for Z in o["mid"]], ["Mo", "Rh"])
    eq("f openings found", [f[0] for f in o["f"]], ["4f", "5f"])
    eq("p at 4f", [f[3] for f in o["f"] if f[0] == "4f"], [0])
    eq("p at 5f", [f[3] for f in o["f"] if f[0] == "5f"], [1])
    eq("rivals below the 4f entrant", [len(f[5]) for f in o["f"] if f[0] == "4f"], [0])
    eq("rivals below the 5f entrant", [len(f[5]) for f in o["f"] if f[0] == "5f"], [0])
    eq("sec 34.6's resets", len(o["resets"]), 18)
    eq("resets at an opening", len(o["resets"]) - len(o["inside"]), 12)
    eq("resets inside a filling subshell", [z for z, _, _, _ in o["inside"]],
       [42, 43, 45, 65, 80, 97])
    eq("subshells not filling at constant a",
       [f"{n}{LET[l]}" for (n, l), _, _, _ in o["notconst"]], ["4d", "5d", "4f", "5f"])
    eq("resets inside a filling span", sum(len(h) for _, _, _, h in o["notconst"]), 10)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<20} expected {want!r}")
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
