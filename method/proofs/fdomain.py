#!/usr/bin/env python3
"""fdomain.py -- why L = -infinity at an f opening, derived rather than asserted.

Section 34.9 of the main volume says:

    "f is outside the domain and the law says so.  At any f opening p = n-l-1 = 0,
     the floor of the node count -- no subshell has fewer nodes than none -- so no
     rival lies below and L = -infinity.  The quantity t = (a-L)/(U-L) does not
     exist there."

The PREMISE is false at 5f, which opens at protactinium with p = 5-3-1 = 1
(finding R4-06, and the record's 34re-07 before it).  The CONCLUSION is true at
both f openings.  This program supplies the reason the conclusion actually has,
and the reason turns out to prove something stronger than section 34.9 claims.

THE DERIVATION, and it is three lines

  Write rho(r) = n_r - l_r - 1 for a subshell's NODE COUNT, and p_r for the law's
  own argument under the root,

      p_r = rho(r) + q_r / 2(2 l_r + 1),

  where q_r is its occupancy at the step.  Admissibility is the law's own:
  q_r < 2(2 l_r + 1), so the fractional term lies in [0, 1).

  At an OPENING the entrant has q_g = 0, so p_g = rho(g) exactly, an integer.

  CLAIM.  An admissible rival lies below the entrant of an opening -- p_r < p_g --
  if and only if it has a strictly smaller node count, rho(r) < rho(g).

  PROOF.  If rho(r) < rho(g) then p_r < rho(r) + 1 <= rho(g) = p_g, since the
  fractional term is under 1 and the node counts are integers.  If rho(r) >= rho(g)
  then p_r >= rho(r) >= rho(g) = p_g.  Both directions, no cases left.  QED

  COROLLARY.  L = -infinity at the opening of g exactly when NO admissible subshell
  has a smaller node count -- that is, when every subshell of smaller node count is
  FULL.

  Two ways that happens, and section 34.9 states only the first:
    (i)  rho(g) = 0.  Nothing has fewer nodes than none, so the set is empty and the
         conclusion is vacuous.  This is the book's node floor, and at 4f it is the
         right reason.
    (ii) rho(g) > 0 and every subshell below is already complete.  This is 5f, where
         rho = 1 and the four node-floor subshells 1s, 2p, 3d and 4f are all full at
         thorium.  The floor is reached by exhaustion instead of by arithmetic.

WHAT THE MEASUREMENT THEN SHOWS, and it is more than the book claims

  Over the observed order, L = -infinity at exactly FIVE of the twenty-four
  openings: 1s, 2p, 3d, 4f and 5f.  So "no rival lies below" is NOT an f-only
  property -- it fires at one opening of every other l as well, and each of those is
  the node-floor member.

  But f is the only l for which EVERY opening is of this kind.  s, p and d each lose
  exactly their rho = 0 member and keep the rest.  f loses both: 4f by the floor and
  5f by exhaustion.  THAT is what "f is outside the domain" is true of, and the
  reason it is true is that f arrives late enough for every node-floor subshell to
  have closed before its second member opens.

INPUT
  method/members/LW1-ground.py -- the seated member, register 1306, the observed
  NIST ASD 5.12 ground configurations.  Imported by path, never copied.

REFUSALS
  This program derives the reason and measures it.  It does not repair section 34.9,
  and it makes no claim about t(l), the entry point, or the figures 1.028 and 1.785,
  which the record carries as 34re-04 UNREPRODUCIBLE.  Nothing is repaired.

stdlib only.  --selftest asserts the derivation against the observed order.
"""
import argparse, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
LET = "spdfg"
NMAX, LMAX = 7, 3          # the candidate set, the record's convention (READ-ch34re)


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


def cap(l):
    return 2 * (2 * l + 1)


def rho(n, l):
    return n - l - 1


def p_of(n, l, q):
    return rho(n, l) + q / cap(l)


def all_openings(g, zmax=108):
    """Every Z at which a subshell becomes occupied having been empty at Z-1.
    Re-openings count; the record's own partition requires it (finding R4-06)."""
    out, prev = [], {}
    for Z in range(1, zmax + 1):
        cur = occupancy(g, Z)
        for k, v in cur.items():
            if v > 0 and prev.get(k, 0) == 0:
                out.append((Z, k))
        prev = cur
    return out


def candidates(prev):
    """Every admissible subshell in the candidate set, with its p."""
    out = []
    for n in range(1, NMAX + 1):
        for l in range(0, min(LMAX + 1, n)):
            q = prev.get((n, l), 0)
            if q < cap(l):
                out.append((n, l, q, p_of(n, l, q)))
    return out


def below(prev, entrant):
    """Admissible rivals strictly below the entrant in p, and separately those of
    strictly smaller node count.  The claim is that these two sets are equal."""
    n, l = entrant
    pg = p_of(n, l, prev.get(entrant, 0))
    by_p = [c for c in candidates(prev) if c[3] < pg - 1e-12]
    by_rho = [c for c in candidates(prev) if rho(c[0], c[1]) < rho(n, l)]
    return pg, by_p, by_rho


def measure(members):
    g = load_ground(members)
    rows, claim_holds = [], True
    for Z, (n, l) in all_openings(g):
        prev = occupancy(g, Z - 1)
        pg, by_p, by_rho = below(prev, (n, l))
        if sorted(c[:2] for c in by_p) != sorted(c[:2] for c in by_rho):
            claim_holds = False
        blocked = [c for c in candidates(prev) if rho(c[0], c[1]) < rho(n, l)]
        full_below = [(nn, ll) for nn in range(1, NMAX + 1)
                      for ll in range(0, min(LMAX + 1, nn))
                      if rho(nn, ll) < rho(n, l) and prev.get((nn, ll), 0) >= cap(ll)]
        rows.append(dict(Z=Z, el=g.GROUND[Z][0], sub=f"{n}{LET[l]}", n=n, l=l,
                         rho=rho(n, l), pg=pg, by_p=by_p, by_rho=by_rho,
                         blocked=blocked, full_below=full_below,
                         minus_inf=not by_p))
    by_l = {}
    for r in rows:
        by_l.setdefault(r["l"], []).append(r)
    return dict(ground=g, rows=rows, claim_holds=claim_holds, by_l=by_l)


def report(o):
    rows = o["rows"]
    inf = [r for r in rows if r["minus_inf"]]
    print("  WHY L = -INFINITY AT AN F OPENING, DERIVED AND THEN MEASURED")
    print()
    print("  THE CLAIM: at an opening, an admissible rival lies below the entrant in p")
    print("  if and only if its node count rho = n - l - 1 is strictly smaller.")
    print(f"  Checked at all {len(rows)} openings of the observed order: "
          f"{'HOLDS at every one' if o['claim_holds'] else 'FAILS'}")
    print()
    print("  EVERY OPENING, AND WHETHER ANYTHING LIES BELOW IT")
    print(f"    {'Z':>4} {'el':<3} {'sub':<4} {'rho':>4}  {'admissible rivals of smaller node count':<44} {'L':>7}")
    for r in rows:
        names = ", ".join(f"{c[0]}{LET[c[1]]}" for c in r["by_rho"])
        print(f"    {r['Z']:>4} {r['el']:<3} {r['sub']:<4} {r['rho']:>4}  "
              f"{(names or '(none)')[:44]:<44} {'-inf' if r['minus_inf'] else 'finite':>7}")
    print()
    print(f"  L = -INFINITY AT {len(inf)} OF {len(rows)} OPENINGS: "
          + ", ".join(f"{r['sub']} (Z {r['Z']}, {r['el']})" for r in inf))
    print()
    print("  AND THE TWO REASONS ARE DIFFERENT")
    for r in inf:
        if r["rho"] == 0:
            print(f"    {r['sub']:<3} rho = 0.  Nothing has fewer nodes than none -- the node floor,")
            print(f"        which is the reason section 34.9 gives, and at this opening it is right.")
        else:
            fb = ", ".join(f"{n}{LET[l]}" for n, l in r["full_below"])
            print(f"    {r['sub']:<3} rho = {r['rho']}, so the floor is NOT the reason.  Every subshell of")
            print(f"        smaller node count -- {fb} -- is FULL at "
                  f"{o['ground'].GROUND[r['Z'] - 1][0]} (Z {r['Z'] - 1}) and so fails the law's")
            print(f"        own admissibility test q < 2(2l+1).  The floor is reached by exhaustion.")
    print()
    print("  WHICH l HAS EVERY OPENING OUTSIDE THE DOMAIN")
    for l in sorted(o["by_l"]):
        rs = o["by_l"][l]
        k = sum(1 for r in rs if r["minus_inf"])
        mark = "  <== EVERY ONE" if k == len(rs) else ""
        print(f"    {LET[l]}: {k} of {len(rs)} openings have L = -inf"
              f"   ({', '.join(r['sub'] for r in rs if r['minus_inf']) or 'none'}){mark}")
    print()
    print("  So section 34.9's conclusion is true and its reason is not.  The true reason")
    print("  covers both f openings in one clause: AT EVERY F OPENING NO ADMISSIBLE SUBSHELL")
    print("  HAS A SMALLER NODE COUNT -- at 4f because none exists, at 5f because every one")
    print("  of them is full.  And f is the ONLY l of which that is true at every opening,")
    print("  which is what 'f is outside the domain' should mean.  Nothing is repaired here.")


FIXTURES = """derived, then checked against the observed order (register 1306):
  the claim   p_r < p_g at an opening  <=>  rho(r) < rho(g)      -- holds at all 24 openings
  4f          rho = 0, the node floor                            -- section 34.9's own reason, right here
  5f          rho = 1; 1s, 2p, 3d, 4f all full at Th (Z 90)      -- 34re-07's p = 1, given its reason
  the set     L = -inf at exactly 1s, 2p, 3d, 4f, 5f
  f alone     the only l with EVERY opening outside the domain"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(name, got, want):
        checks.append((name, got, want, got == want))

    rows = {r["sub"] + str(r["Z"]): r for r in o["rows"]}
    inf = [r["sub"] for r in o["rows"] if r["minus_inf"]]
    eq("the claim holds at every opening", o["claim_holds"], True)
    eq("openings found", len(o["rows"]), 24)
    eq("L = -inf openings", inf, ["1s", "2p", "3d", "4f", "5f"])
    eq("4f rho", rows["4f58"]["rho"], 0)
    eq("5f rho", rows["5f91"]["rho"], 1)
    eq("nothing below 4f", len(rows["4f58"]["by_rho"]), 0)
    eq("nothing below 5f", len(rows["5f91"]["by_rho"]), 0)
    eq("what is full below 5f",
       [f"{n}{LET[l]}" for n, l in rows["5f91"]["full_below"]], ["1s", "2p", "3d", "4f"])
    for l, name in ((0, "s"), (1, "p"), (2, "d")):
        rs = o["by_l"][l]
        eq(f"{name}: not every opening is -inf",
           sum(1 for r in rs if r["minus_inf"]) == len(rs), False)
    rs = o["by_l"][3]
    eq("f: every opening is -inf", sum(1 for r in rs if r["minus_inf"]) == len(rs), True)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<36} {got!r:<28} expected {want!r}")
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
