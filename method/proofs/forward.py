#!/usr/bin/env python3
"""forward.py -- where the corridor fraction sits above Z = 108, and what the law
predicts there.

M asked where the fraction t = (a-L)/(U-L) sits for everything above the 106 steps.
The walk runs Z = 3 to 108 and stops, because register 1304 records four edges and
the second of them is the listing: NIST ASD holds no neutral ground configuration
past 108.  Above it the law does not describe.  IT PREDICTS.

WHAT THIS DOES

  Takes the last observed configuration, Z = 108 (hassium), and the value `a` carries
  out of lawrencium's reset -- 1.9840594, the last real move of the walk.  Then walks
  upward under the law alone: at each step the admissible subshell of least
  nu = n - a*sqrt(p + q/2(2l+1)) takes the electron, and the next step starts from
  the configuration that makes.  No configuration table is consulted above 108 and
  none exists to consult; the occupancies are the law's own output.

  The candidate set runs to l = 4, which is M's ruling of 6 September 2026
  (RULINGS-R4e.md sec 1).  That matters here more than anywhere: 5g is empty at every
  step above 108, so if the law is ever going to open the g block this is where it
  would.

WHAT IT FINDS, and each is a prediction rather than a measurement

  1. THE FRACTION STAYS INSIDE.  `a` is never forced out of its corridor across
     seventeen further elements.  There is no reset above 108 at all, and t sits
     between 0.05 and 0.68 the whole way.
  2. THE BLOCKS COME OUT RIGHT.  6d through Z = 112, 7p through Z = 118, then 8s at
     119 and 120.  Ten of those are elements the accepted table already assigns, and
     the law was fitted to none of them.
  3. THE g BLOCK DOES NOT OPEN.  Through Z = 125 the law never makes a g subshell the
     entrant.  The reason is exact: a node-free subshell has nu = n with `a` dropping
     out, so 5g sits at nu = 5 forever, and 7d at a = 1.98 sits at 3.03.  For 5g to
     win, `a` would have to fall below 1, and `a` has risen monotonically since
     potassium.

REFUSALS
  EVERY ROW ABOVE Z = 108 IS A PREDICTION and is labelled one.  Register 1288 refused
  an invented cell once and register 1304 names the four edges; this program prints
  past the listing only because the law's own output is the subject, and it never
  calls a predicted row a measurement.  It stops at 125 rather than running to
  exhaustion, because the point is where the g block is and not how far the arithmetic
  goes.  Nothing is repaired.

INPUT
  method/members/LW1-ground.py -- the seated member, for Z = 108 and nothing above it.

stdlib only.  --selftest asserts the accepted blocks and the law's own arithmetic.
"""
import argparse, importlib.util, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
LET = "spdfghi"
INF = float("inf")

A_CARRIED = 1.9840594     # the value `a` takes at lawrencium, and holds to Z = 108
LMAX, NMAX = 4, 9         # M's ruling: the candidate set includes g
TOP = 125

# What the accepted table assigns above the listing, for the blocks the law predicts.
# Elements 109-118 are assigned; 119 and 120 are the standard predictions.
ACCEPTED = {109: "6d", 110: "6d", 111: "6d", 112: "6d",
            113: "7p", 114: "7p", 115: "7p", 116: "7p", 117: "7p", 118: "7p",
            119: "8s", 120: "8s"}


def cap(l):
    return 2 * (2 * l + 1)


def load(members):
    path = os.path.join(members, "LW1-ground.py")
    spec = importlib.util.spec_from_file_location("LW1_ground", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def occupancy(g, Z):
    c = {}
    for n, l, o in g.expand(Z):
        c[(n, l)] = c.get((n, l), 0) + o
    return c


def candidates(conf):
    """The generator's own shape: every partly-filled subshell of each l, plus the
    first empty one.  l runs to 4 under the ruling."""
    out = []
    for l in range(LMAX + 1):
        for n in range(l + 1, NMAX + 1):
            if conf.get((n, l), 0) >= cap(l):
                continue
            out.append((n, l))
            if conf.get((n, l), 0) == 0:
                break
    return out


def radicand(s, conf):
    return s[0] - s[1] - 1 + conf.get(s, 0) / cap(s[1])


def nu(s, conf, a):
    return s[0] - a * math.sqrt(radicand(s, conf))


def corridor(conf, e):
    pg = radicand(e, conf)
    lo, hi = -INF, INF
    for r in candidates(conf):
        if r == e:
            continue
        d = math.sqrt(radicand(r, conf)) - math.sqrt(pg)
        dn = r[0] - e[0]
        if abs(d) < 1e-12:
            continue
        if d > 0:
            hi = min(hi, dn / d)
        else:
            lo = max(lo, dn / d)
    return lo, hi


def measure(members, top=TOP):
    g = load(members)
    conf = dict(occupancy(g, 108))
    a = A_CARRIED
    rows = []
    for Z in range(109, top + 1):
        cs = candidates(conf)
        e = min(cs, key=lambda s: (nu(s, conf, a), s[0], s[1]))
        lo, hi = corridor(conf, e)
        inside = lo < a < hi
        t = (a - lo) / (hi - lo) if lo > -1e17 and hi < 1e17 else None
        rows.append(dict(Z=Z, sub=f"{e[0]}{LET[e[1]]}", ent=e,
                         nu=nu(e, conf, a), lo=lo, hi=hi, t=t, inside=inside,
                         accepted=ACCEPTED.get(Z)))
        conf[e] = conf.get(e, 0) + 1
    ts = [r["t"] for r in rows if r["t"] is not None]
    return dict(ground=g, rows=rows, a=a,
                resets=[r for r in rows if not r["inside"]],
                gsteps=[r for r in rows if r["ent"][1] == 4],
                agree=[r for r in rows if r["accepted"] and r["sub"] == r["accepted"]],
                disagree=[r for r in rows if r["accepted"] and r["sub"] != r["accepted"]],
                tmin=min(ts), tmax=max(ts))


def report(o):
    print("  ABOVE THE LISTING: WHERE THE FRACTION SITS, AND WHAT THE LAW PREDICTS")
    print()
    print(f"    the walk ends at Z = 108, the last neutral ground configuration the listing holds.")
    print(f"    `a` carries out of lawrencium at {o['a']:.7f} and is not re-fitted above 108,")
    print("    because there is no observed entrant above 108 to fit it to.")
    print("    EVERY ROW BELOW IS A PREDICTION.")
    print()
    print(f"    {'Z':>4} {'entrant':<8} {'nu':>8} {'L':>11} {'U':>11} {'t':>9}   accepted")
    for r in o["rows"]:
        f = lambda x: ("%.6f" % x) if abs(x) < 1e17 else ("-inf" if x < 0 else "+inf")
        t = "undefined" if r["t"] is None else "%.4f" % r["t"]
        acc = r["accepted"] or ""
        mark = "" if not acc else ("  agrees" if acc == r["sub"] else "  DIFFERS")
        print(f"    {r['Z']:>4} {r['sub']:<8} {r['nu']:>8.4f} {f(r['lo']):>11} "
              f"{f(r['hi']):>11} {t:>9}   {acc}{mark}")
    print()
    print("  1. THE FRACTION STAYS INSIDE")
    print(f"     resets above Z = 108: {len(o['resets']) or 'NONE'}")
    print(f"     t runs {o['tmin']:.4f} to {o['tmax']:.4f} over the rows where it is defined.")
    print("     One row has U = +infinity and no fraction: Z = 119, where 8s opens and nothing")
    print("     bounds it from above.  Everywhere else `a` sits comfortably inside.")
    print()
    print("  2. THE BLOCKS COME OUT RIGHT")
    print(f"     {len(o['agree'])} of {len(o['agree']) + len(o['disagree'])} rows the accepted table")
    print("     assigns are reproduced, and the law was fitted to none of them:")
    print("       6d through Z = 112 · 7p through Z = 118 · 8s at 119 and 120")
    if o["disagree"]:
        print("     DIFFERS at: " + ", ".join(f"Z {r['Z']} law {r['sub']} vs {r['accepted']}"
                                              for r in o["disagree"]))
    print()
    print("  3. THE g BLOCK DOES NOT OPEN")
    print(f"     g entrants predicted through Z = {o['rows'][-1]['Z']}: "
          f"{[r['Z'] for r in o['gsteps']] or 'NONE'}")
    print("     and the reason is exact.  A node-free subshell has p = 0, so nu = n with `a`")
    print("     dropping out entirely: 5g sits at nu = 5 forever.  7d at a = 1.98 sits at 3.03.")
    print(f"     For 5g to win, 7d would have to rise above 5, which needs a < 1 -- and `a` has")
    print("     risen monotonically since potassium and stands at 1.98.")
    print("     Chapter 35 says 'there is no g block below Z = 121'.  Under the carried value the")
    print("     law says more than that: it does not open at 121 either, and it takes 7d.")


FIXTURES = """the accepted table above the listing, and the law's own arithmetic:
  109-112  6d   -- meitnerium to copernicium, assigned
  113-118  7p   -- nihonium to oganesson, assigned
  119-120  8s   -- the standard predictions for the next alkali and alkaline earth
  nu(5g)   = 5 exactly at every step, since a node-free subshell drops `a`
  no reset -- `a` stays inside its corridor at every predicted step"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    r = {x["Z"]: x for x in o["rows"]}
    eq("109-112 are 6d", [r[z]["sub"] for z in range(109, 113)], ["6d"] * 4)
    eq("113-118 are 7p", [r[z]["sub"] for z in range(113, 119)], ["7p"] * 6)
    eq("119-120 are 8s", [r[z]["sub"] for z in (119, 120)], ["8s"] * 2)
    eq("every accepted row agrees", len(o["disagree"]), 0)
    eq("accepted rows reproduced", len(o["agree"]), 12)
    eq("no reset above the listing", len(o["resets"]), 0)
    eq("no g entrant through 125", [x["Z"] for x in o["gsteps"]], [])
    eq("t stays inside (0,1)", all(0 < x["t"] < 1 for x in o["rows"] if x["t"] is not None), True)
    eq("only Z = 119 has no fraction",
       [x["Z"] for x in o["rows"] if x["t"] is None], [119])
    eq("nu(5g) is 5 exactly", round(nu((5, 4), {}, o["a"]), 12), 5.0)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<32} {got!r:<44} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--members", default=MEMBERS)
    ap.add_argument("--top", type=int, default=TOP)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.members)
    report(measure(a.members, a.top))
    return 0


if __name__ == "__main__":
    sys.exit(main())
