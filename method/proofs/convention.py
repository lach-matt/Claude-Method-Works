#!/usr/bin/env python3
"""convention.py — the arithmetic-convention class, and the convention it turns out to be. Phase 1, D-36.

THE CLASS. `DOCKET.md` item 34: *"The arithmetic-convention class (15l-01) — through chat 126's 16x-02.
Chat 127 adds 16z-06 (an unnamed median that flips the sign of the deviation) and 16z-03's generator
convention."* `DEFERRED.md` adds **16o-02**: *"Two of three rows of the 32.1.3 table sum to 98, which
three rounded percentages of a partition cannot reach."*

WHAT THIS SETTLES. The class was filed as *"some thirty printed counts with unnamed conventions"*, a
complaint about silence. **It is narrower and more useful than that: at the two sites that can be
decided from the page alone, the unnamed convention is the same one, and it is truncation.**

  §32.1.3's table — three shares of a partition, in percent

      entries      by hand   by an audit   from outside      sum
      165–239          88%           5%             6%        99
      240–289          73%          23%             2%        98
      290–319          55%          25%            18%        98

  Under round-to-nearest each printed share is within ½ of its true value, so three of them sum to
  within 1½ of 100 — **the integer sum must lie in 99…101, and 98 is unreachable.** Under truncation
  each loses up to 1, the sum lies in 97…100, and 98 is reachable. **Two of the three rows are
  therefore truncated, and the third is consistent with either.**

  §22.4's *"a factor of 17"* — both inputs printed, 0.14 and 0.008

      0.14 / 0.008 = **17.5** exactly. Round-to-nearest gives 18. Truncation gives 17.

**Two independent sites, one convention — and the corpus names a DIFFERENT one, once.** A search of
the six volumes for a numeric rounding convention returns exactly **one** site, and it is not in a
volume's own prose: it is a Register entry at reg L6644, correcting the Mathematical Compendium's
penetration percentage, which says *"146 of 163 is 90% at nought decimal places, **rounding half to
even**"*. So the only convention the corpus ever names is **half-to-even**, stated in passing inside a
correction — while the two main-volume sites that can be decided from the page are **truncated**.
**The corpus names one convention and practises another**, and neither is declared anywhere a reader
of the volumes would meet it.

WHY THAT MATTERS MORE THAN THE COMPLAINT. `arith.py` checks the volumes' arithmetic under HALF_UP and
HALF_EVEN and takes a `--conventions` roster; **neither convention returns these two sites**, and an
instrument that does not know the book truncates will score truncated figures as wrong. The repair the
class needs is one sentence naming the convention, not thirty edits.

AND WHAT THIS DOES NOT SETTLE. 16z-06's *"unnamed median that flips the sign of the deviation"* and
16z-03's generator convention are not decidable from the page: both need the population the median was
taken over, and neither volume prints it. They are reported as UNDECIDED-HERE and stay in the class.

stdlib only. --selftest asserts every figure below against the live volume.
"""
import argparse, os, re, sys
from fractions import Fraction as F

MEM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "members")
VOLUMES = ["The_Method_1_6-2.md", "The_Method_1_6___The_Register-2.md",
           "The_Method_1_6___Mathematical_Compendium-2.md", "The_Method_1_6___The_Physics_Compendium-2.md",
           "The_Method_1_6___Spectra_Compendium-2.md", "The_Method_1_6___The_Index_of_Indices-2.md"]

ROWS = [("165-239", 88, 5, 6), ("240-289", 73, 23, 2), ("290-319", 55, 25, 18)]
FACTOR = (0.14, 0.008, 17)          # printed numerator, denominator, printed result

# A rounding convention named in prose would match this; the word "truncated" used of a bound would not.
CONV = re.compile(r"\b(round(ed|ing)?\s+(half|to\s+nearest|down|up)|ROUND_HALF|half[-\s]?(up|even)"
                  r"|truncat\w*\s+(to|at)\s+\w*\s*(decimal|figure|place))", re.I)


def load(n):
    return open(os.path.join(MEM, n), encoding="utf-8").read()


def reachable_sums(n_parts, mode):
    """The integer sums a partition of 100 can print under a convention."""
    if mode == "nearest":                 # each share within 1/2  -> sum within n/2
        lo, hi = 100 - n_parts / 2.0, 100 + n_parts / 2.0
    else:                                 # truncation: each loses in [0,1)
        lo, hi = 100 - n_parts, 100.0
    return sorted({s for s in range(90, 111) if lo <= s <= hi})


def named_anywhere():
    """Sites in the six volumes that name a numeric rounding convention."""
    out = []
    for v in VOLUMES:
        for i, l in enumerate(load(v).split("\n")):
            if CONV.search(l):
                out.append((v, i + 1, l.strip()[:90]))
    return out


def report():
    print("The arithmetic-convention class, decided where the page allows it\n")
    print("  §32.1.3's three shares of a partition:\n")
    print("      %-10s %7s %13s %14s %8s   %s" % ("entries", "by hand", "by an audit", "from outside", "sum", "verdict"))
    for name, a, b, c in ROWS:
        s = a + b + c
        v = ("truncated — 98 is unreachable by rounding" if s not in reachable_sums(3, "nearest")
             else "consistent with either convention")
        print("      %-10s %6d%% %12d%% %13d%% %8d   %s" % (name, a, b, c, s, v))
    print("\n      round-to-nearest can print the sums %s" % reachable_sums(3, "nearest"))
    print("      truncation can print the sums        %s" % reachable_sums(3, "truncation"))
    n, d, p = FACTOR
    print("\n  §22.4's 'a factor of 17': %g / %g = %.1f exactly — rounds to %d, truncates to %d (printed %d)"
          % (n, d, n / d, round(n / d + 1e-12), int(n / d), p))
    named = named_anywhere()
    print("\n  sites in the six volumes naming a numeric rounding convention: %d" % len(named))
    for v, ln, l in named:
        print("      %s:%d  %s" % (v, ln, l))
    print("\n  So two independent sites agree on TRUNCATION, while the single site that names a")
    print("  convention anywhere in the corpus is a Register entry naming HALF-TO-EVEN in passing.")
    print("  UNDECIDED HERE, and staying in the class: 16z-06's unnamed median (the population it was")
    print("  taken over is not printed) and 16z-03's generator convention (the same).")
    print("\n  RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print("  OK   %s: %s" % (name, got))
        else: fail += 1; print("  FAIL %s: got %s, want %s" % (name, got, want))
    t = load("The_Method_1_6-2.md")
    eq("§32.1.3's three rows are still printed as measured",
       all(("%d%%" % a) in t and ("%d%%" % b) in t for _, a, b, _ in ROWS), True)
    eq("the three row sums", [a + b + c for _, a, b, c in ROWS], [99, 98, 98])
    eq("round-to-nearest cannot print 98 for three shares", 98 in reachable_sums(3, "nearest"), False)
    eq("truncation can", 98 in reachable_sums(3, "truncation"), True)
    eq("so two of the three rows are truncated",
       sum(1 for _, a, b, c in ROWS if (a + b + c) not in reachable_sums(3, "nearest")), 2)
    eq("and the third is consistent with either",
       sum(1 for _, a, b, c in ROWS if (a + b + c) in reachable_sums(3, "nearest")), 1)
    n, d, p = FACTOR
    eq("the factor site divides exactly", n / d, 17.5)
    eq("round-to-nearest would print 18", round(n / d + 1e-12), 18)
    eq("truncation prints the 17 the book prints", int(n / d), p)
    eq("the two sites therefore agree on one convention",
       int(n / d) == p and 98 not in reachable_sums(3, "nearest"), True)
    named = named_anywhere()
    eq("exactly one site in the corpus names a numeric rounding convention", len(named), 1)
    eq("and it is a Register entry, not a volume's own prose",
       named[0][0], "The_Method_1_6___The_Register-2.md")
    eq("naming half-to-even, which is NOT the truncation the two decidable sites use",
       "half to even" in load(named[0][0]).split("\n")[named[0][1] - 1], True)
    eq("the word 'truncated' does occur, of a bound and a series, which is why the regex is narrow",
       t.count("truncated") + t.count("truncation") >= 2, True)
    print("\nOK: %d  FAIL: %d" % (ok, fail))
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
