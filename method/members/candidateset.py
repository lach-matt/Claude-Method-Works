#!/usr/bin/env python3
"""candidateset.py -- the one question in Chapter 34 the data does not settle.

Two instruments in this repository compute the same corridor and disagree, and the
disagreement is not a bug in either.  They use different CANDIDATE SETS, and a seated
Register entry's universal is true under one and false under the other.

THE TWO GENERATORS

  r2-ch16y.py    a SEATED member.  Candidates are every (n, l) with n <= 7, l <= 3,
                 not at capacity.  NO g SUBSHELLS.
  walk.py        recovered, and the instrument that produced section 34.6's eighteen.
                 Candidates run l = 0..4 -- G SUBSHELLS INCLUDED -- taking every
                 partly-filled subshell of each l plus the first empty one.

WHERE THEY DISAGREE, AND IT IS ONE SUBSHELL

  At protactinium the entrant is 5f, whose node count is n - l - 1 = 1.  A rival lies
  below it exactly when its node count is smaller, that is zero.  The node-count-zero
  subshells are 1s, 2p, 3d, 4f -- all full at thorium -- AND 5g, which is empty.

    without g   nothing lies below 5f, so L = -infinity
    with g      5g lies below 5f, so L = 0

  That single subshell decides three printed things.

WHAT IT DECIDES

  1. REGISTER 1414, seated: "the floor is minus infinity EXACTLY WHEN the entering
     subshell is node-free ... 106 of 106, no exception, and derivable rather than
     observed."  Measured: TRUE at 106 of 106 with g admitted; FALSE at eleven steps
     without it -- every 5f step from Pa 91 to No 102, each with L = -infinity and a
     node count of one.

  2. SECTION 34.9's CONCLUSION, "no rival lies below and L = -infinity" at every f
     opening.  TRUE without g; FALSE at 5f with g, where L = 0.

  3. REGISTER 1403's "protactinium's L is degenerate at zero", which is walk.py's
     answer and not the seated instrument's.

  Section 34.9's PREMISE -- "at any f opening p = n - l - 1 = 0" -- is false at 5f
  under both, since 5 - 3 - 1 = 1 either way.  That much needs no ruling.

WHY THE DATA CANNOT SETTLE IT
  No g subshell is occupied in any neutral atom in the table, so no observation
  distinguishes the two candidate sets.  They differ only in what the law is allowed
  to CONSIDER, which is a statement about the law's domain and not about the elements.
  The seated instrument knows this and says so: its own comment reads "FAULT 3,
  self-caught: one generator convention is not a count.  Sweep (NMAX, LMAX) and say
  which."  It sweeps, and it reports the endpoint counts under each -- but it prints
  its one-sided corridors under l <= 3 alone.

REFUSALS
  This program does not choose.  It measures both and states what each decides.  The
  choice is a ruling about the law's domain and belongs to M.  Nothing is repaired.

stdlib only.  --selftest asserts both measurements and the seated instrument's own
banked output.
"""
import argparse, importlib.util, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
LET = "spdfg"
INF = float("inf")


def cap(l):
    return 2 * (2 * l + 1)


def load_ground(members):
    path = os.path.join(members, "LW1-ground.py")
    spec = importlib.util.spec_from_file_location("LW1_ground", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def occupancy(g, Z):
    if Z < 1:
        return {}
    c = {}
    for n, l, o in g.expand(Z):
        c[(n, l)] = c.get((n, l), 0) + o
    return c


def entrant(g, Z):
    pr, cu = occupancy(g, Z - 1), occupancy(g, Z)
    got = [k for k in cu if cu[k] > pr.get(k, 0)]
    return got[0] if len(got) == 1 else None


def gen_seated(prev, NMAX=7, LMAX=3):
    """r2-ch16y.py's generator, a seated member: every (n, l) not at capacity."""
    return [(n, l) for n in range(1, NMAX + 1)
            for l in range(0, min(LMAX, n - 1) + 1)
            if prev.get((n, l), 0) < cap(l)]


def gen_walk(prev):
    """walk.py's generator: l = 0..4, every partly-filled subshell of each l plus the
    first empty one."""
    out = []
    for l in range(5):
        for n in range(l + 1, 9):
            if prev.get((n, l), 0) >= cap(l):
                continue
            out.append((n, l))
            if prev.get((n, l), 0) == 0:
                break
    return out


def corridor(g, Z, gen):
    prev = occupancy(g, Z - 1)
    e = entrant(g, Z)
    if e is None:
        return None
    cs = gen(prev)
    if e not in cs:
        return None
    pg = e[0] - e[1] - 1
    lo, hi = -INF, INF
    for r in cs:
        if r == e:
            continue
        d = math.sqrt(r[0] - r[1] - 1) - math.sqrt(pg)
        dn = r[0] - e[0]
        if abs(d) < 1e-12:
            continue
        if d > 0:
            hi = min(hi, dn / d)
        else:
            lo = max(lo, dn / d)
    return dict(Z=Z, lo=lo, hi=hi, ent=e, rho=pg,
                sub=f"{e[0]}{LET[e[1]]}", minus_inf=(lo == -INF))


def sweep(g, gen):
    rows = [corridor(g, Z, gen) for Z in range(3, 109)]
    rows = [r for r in rows if r]
    minf = [r for r in rows if r["minus_inf"]]
    nodefree = [r for r in rows if r["rho"] == 0]
    a, b = {r["Z"] for r in minf}, {r["Z"] for r in nodefree}
    return dict(rows=rows, minf=minf, nodefree=nodefree,
                iff_holds=(a == b),
                minf_not_nodefree=[r for r in minf if r["rho"] != 0],
                nodefree_not_minf=[r for r in nodefree if not r["minus_inf"]])


def measure(members):
    g = load_ground(members)
    return dict(ground=g,
                seated=sweep(g, gen_seated),
                walk=sweep(g, gen_walk),
                pa_seated=corridor(g, 91, gen_seated),
                pa_walk=corridor(g, 91, gen_walk),
                ce_seated=corridor(g, 58, gen_seated),
                ce_walk=corridor(g, 58, gen_walk))


def fmt(r):
    lo = "-inf" if r["lo"] == -INF else f"{r['lo']:.7f}"
    hi = "+inf" if r["hi"] == INF else f"{r['hi']:.7f}"
    return f"({lo}, {hi})"


def report(o):
    print("  THE CANDIDATE SET, AND WHAT IT DECIDES")
    print()
    print("  THE TWO F OPENINGS UNDER EACH GENERATOR")
    print(f"    {'':<28} {'4f at Ce 58':<28} {'5f at Pa 91'}")
    print(f"    {'seated r2-ch16y.py, l <= 3':<28} {fmt(o['ce_seated']):<28} {fmt(o['pa_seated'])}")
    print(f"    {'walk.py, l <= 4 (g admitted)':<28} {fmt(o['ce_walk']):<28} {fmt(o['pa_walk'])}")
    print("    The 4f corridor is the same under both.  The 5f corridor is not: without g")
    print("    nothing lies below 5f; with g, 5g does, and the floor becomes zero.")
    print("    The seated instrument's banked output prints (-inf, 1.3660254) at Pa.")
    print()
    print("  REGISTER 1414, SEATED: 'the floor is minus infinity exactly when the entering")
    print("  subshell is node-free -- 106 of 106, no exception, derivable rather than observed'")
    for name, s in (("seated r2-ch16y.py, l <= 3", o["seated"]),
                    ("walk.py, l <= 4 (g admitted)", o["walk"])):
        print(f"    {name}")
        print(f"      steps with L = -inf {len(s['minf']):>4}   entrant node-free {len(s['nodefree']):>4}"
              f"   the iff holds: {s['iff_holds']}")
        if s["minf_not_nodefree"]:
            print(f"      L = -inf but NOT node-free, {len(s['minf_not_nodefree'])} steps:")
            print("        " + ", ".join(
                f"{o['ground'].GROUND[r['Z']][0]} {r['Z']} ({r['sub']}, node count {r['rho']})"
                for r in s["minf_not_nodefree"]))
        if s["nodefree_not_minf"]:
            print(f"      node-free but L finite, {len(s['nodefree_not_minf'])} steps")
    print()
    print("  WHAT TURNS ON IT")
    print("    register 1414        TRUE with g admitted, FALSE without it at eleven steps")
    print("    section 34.9's       TRUE without g, FALSE at 5f with it")
    print("      conclusion")
    print("    register 1403's      'protactinium's L is degenerate at zero' is walk.py's")
    print("      answer                answer, not the seated instrument's")
    print("    section 34.9's       FALSE at 5f under BOTH -- 5 - 3 - 1 = 1 either way,")
    print("      premise               so that much needs no ruling")
    print()
    print("  NO OBSERVATION DISTINGUISHES THEM.  No g subshell is occupied in any neutral")
    print("  atom in the table, so the two candidate sets agree on every measurement and")
    print("  differ only in what the law may CONSIDER.  That is a ruling about the law's")
    print("  domain.  This program does not make it.")


FIXTURES = """the corpus's own recorded numbers:
  r2-ch16y.out  Z=58 Ce entrant 4f (L, U) = (-inf, 0.7071068)
  r2-ch16y.out  Z=91 Pa entrant 5f (L, U) = (-inf, 1.3660254)   -- the SEATED answer
  register 1403 'protactinium's L is degenerate at zero'         -- walk.py's answer
  register 1414 'the floor is minus infinity exactly when the entering subshell is
                node-free: 106 of 106, no exception'"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("seated: 4f at Ce has L = -inf", o["ce_seated"]["minus_inf"], True)
    eq("seated: 5f at Pa has L = -inf", o["pa_seated"]["minus_inf"], True)
    eq("seated: Pa's upper bound", round(o["pa_seated"]["hi"], 7), 1.3660254)
    eq("seated: Ce's upper bound", round(o["ce_seated"]["hi"], 7), 0.7071068)
    eq("walk: 4f at Ce has L = -inf", o["ce_walk"]["minus_inf"], True)
    eq("walk: 5f at Pa has L = -inf", o["pa_walk"]["minus_inf"], False)
    eq("walk: Pa's floor is zero", round(o["pa_walk"]["lo"], 9), 0.0)
    eq("register 1414 holds with g", o["walk"]["iff_holds"], True)
    eq("register 1414 fails without g", o["seated"]["iff_holds"], False)
    eq("the eleven exceptions are all 5f",
       sorted({r["sub"] for r in o["seated"]["minf_not_nodefree"]}), ["5f"])
    eq("how many exceptions", len(o["seated"]["minf_not_nodefree"]), 11)
    eq("they run Pa to No",
       [o["seated"]["minf_not_nodefree"][0]["Z"], o["seated"]["minf_not_nodefree"][-1]["Z"]],
       [91, 102])
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<14} expected {want!r}")
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
