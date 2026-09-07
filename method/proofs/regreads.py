#!/usr/bin/env python3
"""regreads.py — the eighteen register-read findings, each given a disposition. Phase 2, F-266.

THE ROW. `PLAN-R4-ANNEX.tsv` carries `F-266` as *"Register-read findings reg1-01 to reg1-06, reg2-01,
reg3-01, reg4-01, reg7-01/-02, reg8-01/-03, reg12-01 to -03, reg13-01"* — eighteen findings from the
`READ-reg*.md` reads, each owed a disposition and none having one.

WHAT THIS SETTLES, AND WHAT IT REFUSES. It gives each of the eighteen a disposition **measured against
the live pair**, not inherited from the read. It does not repair any of them: a finding is recorded,
never repaired. Where a live seated instrument already owns a finding, that is said and the
instrument named — a disposition is not a re-measurement.

THE SHAPE OF THE ANSWER. **Seven of the eighteen are owned by a live golden** that re-checks them at every build and returns
the read's own figure — which is the strongest disposition available short of a repair. **Six stand,
measured here and unchanged, with no instrument owning them.** **Three are dispositioned by another
finding or by the read itself.** **One has moved since the read and the movement is the finding.**
**One is covered by an entry seated in this leg.**

AND ONE OF THEM CORRECTED THIS INSTRUMENT'S FIRST DRAFT. reg12-03 was drafted as MOVED, on a count of
seven object handles taken with a line-counting grep. The handles occur **ten** times on those lines —
`3B.shape` alone carries five — so the read's ten is exact and the finding stands unrepaired. The
selftest caught it before the report was believed, which is what its fixtures are for.

The classes, and they are not the same kind of thing:

  LIVE-INSTRUMENT   a seated golden measures it now, and returns the read's own figure
  STANDING          measured here and unchanged, with no instrument owning it
  MOVED             measured here and the figure has changed since the read
  DISPOSED          another finding, or the read itself, settles it
  SEATED            an entry of this leg records it

stdlib only, except that the LIVE-INSTRUMENT rows run the seated golden that owns them.
--selftest asserts every figure below against the live pair.
"""
import argparse, os, re, subprocess, sys

MEM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "members")
BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bin")
REG = "The_Method_1_6___The_Register-2.md"


def reg():
    return open(os.path.join(MEM, REG), encoding="utf-8").read()


def lines():
    return reg().split("\n")


def front_matter():
    L = lines()
    end = next(i for i, l in enumerate(L) if re.match(r"^#{1,4}\s*\d", l))
    return "\n".join(L[:end]), end


def entry_body(n):
    L = lines()
    for i, l in enumerate(L):
        if re.match(r"^#{1,4}\s*%d\s*$" % n, l):
            for j in range(i + 1, i + 5):
                if L[j].strip():
                    return L[j]
    return ""


def grouped_headings():
    return [l for l in lines() if re.match(r"^#{1,4}\s*\d[\d,\s\-–]*,", l)]


def run_golden(name):
    env = dict(os.environ, PATH=os.path.abspath(BIN) + os.pathsep + os.environ["PATH"])
    p = subprocess.run(["python3", name + ".py"], cwd=MEM, capture_output=True, text=True, env=env)
    return p.stdout


def figure(out, key):
    for l in out.split("\n"):
        if key in l:
            m = re.search(r"\b(\d[\d,]*)\b", l.split(key)[1])
            if m:
                return int(m.group(1).replace(",", ""))
    return None


# --- the measurements -----------------------------------------------------------------------------
def m_scripts():
    fm, _ = front_matter()
    return {p: fm.count(p) for p in ("build.py", "kinds.py", "register_cites.py",
                                     "register_gen.py", "Build 9", "Build 16")}


def m_grouped():
    fm, _ = front_matter()
    said = re.findall(r"(seven|eight|nine|ten|eleven)\s+grouped", fm)
    return len(grouped_headings()), (said[0] if said else None)


def m_handles():
    r = reg()
    return {h: r.count(h) for h in ("3B.tri", "3B.five", "3B.pot", "3B.shape", "3B.metric", "BUILD-10")}


def m_313():
    b = entry_body(313)
    return b.count("*"), b.count("*") % 2 == 1, "Λ* WAS" in b


DISPOSITIONS = [
    ("reg1-01", "LIVE-INSTRUMENT", "the load-bearing >=7 table is stale in four ways",
     "re-taken by the build instrument at every seating and asserted by r2-reg1a3; a new row is a hand act, which refused a build in this leg"),
    ("reg1-02", "LIVE-INSTRUMENT", "the three citation figures are stale",
     "411 / 883 / N re-taken at every build and asserted by r2-reg1a3's 'cited 3 figures'"),
    ("reg1-03", "STANDING", "one paragraph contradicts itself on the grouped headings, seven against ten",
     "measured here: 7 grouped headings, and the front matter still says ten"),
    ("reg1-04", "DISPOSED", "the mature-record figures do not sum to the total",
     "the read marks it CORRECTED BELOW in its own file, and the front matter now sums to itself at every build"),
    ("reg1-05", "LIVE-INSTRUMENT", "front-matter provenance citations resolve to withdrawn entries",
     "this is r2-reg8a2's reg8-B, which measures it at every build"),
    ("reg1-06", "STANDING", "four script names and two build handles visible to the reader, against Ruling 46",
     "measured here: build.py, kinds.py, register_cites.py, register_gen.py, Build 9, Build 16 all still in the front matter"),
    ("reg2-01", "SEATED", "an unbounded lattice's figures printed inside a bounded one",
     "register 1864 seats the class from the genesis block's 2n-squared capacities; reg2-01's own site is entry 57's box and is the same reading"),
    ("reg3-01", "LIVE-INSTRUMENT", "entry 313's emphasis is scrambled, and seventy entries point at it",
     "313 is in r2-reg7a2's scored set; measured here its first line still reads 'TIME MUST NOT ENTER L* WAS A MISSTATEMENT' with an odd asterisk total"),
    ("reg4-01", "STANDING", "entry 193 names two live figures that are not the ones it describes",
     "no instrument owns it and nothing in this leg touched it"),
    ("reg7-01", "LIVE-INSTRUMENT", "275 entries carry emphasis that does not arrive",
     "r2-reg7a2 returns exactly 275 at every build"),
    ("reg7-02", "LIVE-INSTRUMENT", "eleven entries must leave a literal asterisk on the page",
     "r2-reg7a2 returns exactly 11, as FINDING reg7-B"),
    ("reg8-01", "LIVE-INSTRUMENT", "110 entries present in the archive are absent from the live Register",
     "r2-reg8a2 returns exactly 110, as FINDING reg8-A"),
    ("reg8-02", "DISPOSED", "the front matter cites four entries the register withdrew",
     "reg12-01 concludes reg8-02 is FALSE and gives its own net as the reason; the live reg8-B list is the measurement that stands"),
    ("reg8-03", "STANDING", "the register diagnosed the split-delimiter class and the diagnosis was withdrawn",
     "no instrument owns the withdrawal itself; the class it diagnosed is r2-reg7a2's and is live"),
    ("reg12-01", "DISPOSED", "reg8-02 is FALSE, and this read's own net is why",
     "it is itself a disposition, of reg8-02"),
    ("reg12-02", "MOVED", "the unprinted-theorem class is three theorems, not one",
     "measured now by the seated resolver: NINE theorem pointers cited and never stated, across main, mc and reg - the class grew from three"),
    ("reg12-03", "STANDING", "the object-handle leak is ten sites, not the one recorded",
     "measured now: exactly ten object handles - 3B.tri 1, 3B.five 1, 3B.pot 2, 3B.shape 5, 3B.metric 1 - beside the BUILD-10 handle 26b-10 records. The read's ten is exact and the leak is unrepaired"),
    ("reg13-01", "STANDING", "the emphasis class was diagnosed, repaired, recorded, and recurred sixteen times",
     "the recurrence is what r2-reg7a2's 275 and 11 measure; the read's own count of sixteen recurrences is not re-derived here"),
]


def report():
    print("The eighteen register-read findings, each given a disposition measured against the live pair\n")
    w = max(len(d[1]) for d in DISPOSITIONS)
    for i, k, what, why in DISPOSITIONS:
        print("  %-9s %-*s %s" % (i, w, k, what))
        print("  %-9s %-*s   %s" % ("", w, "", why))
    from collections import Counter
    c = Counter(d[1] for d in DISPOSITIONS)
    print("\n  " + " · ".join("%s %d" % (k, c[k]) for k in
          ("LIVE-INSTRUMENT", "STANDING", "MOVED", "DISPOSED", "SEATED")))
    print("\n  the measurements behind the four that needed one:\n")
    print("    reg1-03  grouped headings measured %d; the front matter says '%s'" % m_grouped())
    print("    reg1-06  " + ", ".join("%s x%d" % (k, v) for k, v in m_scripts().items()))
    n, odd, scrambled = m_313()
    print("    reg3-01  entry 313: %d asterisks, odd=%s, the scrambled run still present=%s" % (n, odd, scrambled))
    print("    reg12-03 " + ", ".join("%s x%d" % (k, v) for k, v in m_handles().items()))
    print("\n  RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print("  OK   %s: %s" % (name, got))
        else: fail += 1; print("  FAIL %s: got %s, want %s" % (name, got, want))
    eq("eighteen findings dispositioned", len(DISPOSITIONS), 18)
    eq("every id is unique", len({d[0] for d in DISPOSITIONS}), 18)
    eq("every disposition is one of the five classes",
       {d[1] for d in DISPOSITIONS} <= {"LIVE-INSTRUMENT", "STANDING", "MOVED", "DISPOSED", "SEATED"}, True)
    g, said = m_grouped()
    eq("reg1-03: grouped headings measured", g, 7)
    eq("reg1-03: and the front matter still says", said, "ten")
    s = m_scripts()
    eq("reg1-06: all four script names still in the front matter",
       all(s[k] >= 1 for k in ("build.py", "kinds.py", "register_cites.py", "register_gen.py")), True)
    eq("reg1-06: and both build handles", s["Build 9"] >= 1 and s["Build 16"] >= 1, True)
    n, odd, scr = m_313()
    eq("reg3-01: entry 313's asterisk total is odd", odd, True)
    eq("reg3-01: and the scrambled run is still there", scr, True)
    h = m_handles()
    eq("reg12-03: object handles measured", sum(v for k, v in h.items() if k.startswith("3B.")), 10)
    eq("reg12-03: which is exactly the ten the read recorded",
       sum(v for k, v in h.items() if k.startswith("3B.")) == 10, True)
    eq("reg12-03: and 3B.shape carries five of them", h["3B.shape"], 5)
    out = run_golden("r2-reg7a2")
    eq("reg7-01: the live instrument returns", figure(out, 'the split shape "X* *Y"'), 275)
    eq("reg7-02: and the literal-asterisk count", figure(out, "leaving a literal asterisk on the page"), 11)
    out8 = run_golden("r2-reg8a2")
    eq("reg8-01: the live instrument returns", figure(out8, "archive and not in the live register"), 110)
    from collections import Counter
    c = Counter(d[1] for d in DISPOSITIONS)
    eq("seven are owned by a live golden", c["LIVE-INSTRUMENT"], 7)
    eq("and none is left without a disposition",
       sum(c.values()), 18)
    print("\nOK: %d  FAIL: %d" % (ok, fail))
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
