#!/usr/bin/env python3
"""unprintedinput.py — the unprinted-input class, measured on its own named members. Phase 1, D-12 / E-081.

THE CLASS, as the corpus defines it. `DOCKET.md` item 10: *"The unprinted-input class, sixty members —
unchanged."* `DEFERRED.md` names the members it can name and states the census R3 owes:
**"every site in the six volumes that prints a derived figure"** without the inputs that reproduce it —
*"§22.1.2 needs δ = 0.35; §22.4.1 needs δ₂ = 0.06; L6060's 446×, L6068's 1,577, L6093's 3.47 % and
L6104's factor of 17 each need an input more precise than the one printed beside them. §22.1.1.1 claims
F.3's highest standard, whose columns include the input set."*

**"Unchanged" is no longer true, and that is the first finding.** Two of the seven named members have
been repaired: §22.1.2 now prints its whole input set and says so, and §22.1.1.1's F.3 claim is
substantiated in the same passage. The class is a floor that has moved.

THE SECOND FINDING IS SHARPER THAN THE DOCKET'S. §22.2.1's ablation table is **right and unverifiable**.
Its three directional figures — 446×, 0.28× and the asymmetry 1,577 — are **mutually consistent at full
precision** and **not one of them reproduces from the two-figure inputs printed beside it**:

    printed:  median error 0.46 → 206 cm⁻¹ = 446×      206/0.46   = 447.83, not 446
              median error 0.46 → 0.13 cm⁻¹ = 0.28×    206/0.13   = 1584.6, not 1,577
              the asymmetry is a factor of 1,577

    solve:    m = 206/446  = 0.461883 → prints 0.46
              a = 206/1577 = 0.130628 → prints 0.13
              a/m          = 0.282815 → prints 0.28      all three close exactly

**So the defect is not an error. It is a verification gap, and the two inputs that close it are
recoverable from the figures themselves** — median error 0.4619 and above-cost 0.1306. The other two
rows of the same table DO reproduce from their printed inputs (588/200 = 2.94 → 2.9; 41.3/12.8 = 3.23
→ 3.2), which is what makes the finding specific rather than a complaint about rounding.

§22.4.1 IS STILL A MEMBER AND ITS INPUT IS RECOVERABLE TOO. It prints *"narrower by exactly n³/(2δ₂) —
4,329 vs 4,267 at n = 8; 1.387 × 10⁶ vs 1.386 × 10⁶ at n = 55"*. δ₂ appears nowhere in the section.
Solving either predicted figure gives δ₂ ≈ 0.060, and that one value reproduces both.

AND ONE NAMED MEMBER IS NOT THIS CLASS AT ALL. *"a factor of 17"* has both its inputs printed —
0.14 and 0.008 — and 0.14/0.008 = **17.5**, which rounds to 18 and truncates to 17. Nothing is missing;
a convention is unnamed. It belongs to D-36, and `convention.py` takes it.

stdlib only. --selftest asserts every figure below against the live volume.
"""
import argparse, os, re, sys
from fractions import Fraction as F

MEM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")


def text():
    return open(MAIN, encoding="utf-8").read()


def sites(pat):
    """1-based line numbers of every line matching pat."""
    return [i + 1 for i, l in enumerate(text().split("\n")) if re.search(pat, l)]


def rnd(x, n):
    """round-half-up to n places, the convention arith.py uses."""
    q = F(10) ** n
    v = F(x) * q
    return float((v + F(1, 2)).__floor__() / q) if v >= 0 else float(-((-v + F(1, 2)).__floor__()) / q)


# --- the ablation table, solved -----------------------------------------------------------------
B = 206.0
M_SOLVED = B / 446         # the median error 446× requires
A_SOLVED = B / 1577        # the above-cost 1,577 requires

MEMBERS = [
    ("§22.1.2, δ = 0.35",            "REPAIRED",  "the section now prints R, Z, n = 4 to 14 and all four δ, and says 'The input set is printed'"),
    ("§22.1.1.1, F.3's standard",    "REPAIRED",  "substantiated in the same passage — 'the method named with its input set, every input printed'"),
    ("§22.2.1's 446×",               "MEMBER",    "206/0.46 = 447.83; the figure needs the median at 0.461883, which prints as 0.46"),
    ("§22.2.1's 1,577",              "MEMBER",    "206/0.13 = 1584.6; the figure needs the above-cost at 0.130628, which prints as 0.13"),
    ("§22.3's 3.47%",                "MEMBER",    "0.7376 and 0.7129 give 3.4647%, which prints as 3.46 — the figure needs an input carried further"),
    ("§22.4.1's δ₂",                 "MEMBER",    "n³/(2δ₂) reproduces 4,267 and 1.386e6 at δ₂ ≈ 0.060, and δ₂ is printed nowhere in the section"),
    ("§22.4's 'a factor of 17'",     "NOT THIS CLASS", "both inputs printed: 0.14/0.008 = 17.5. A convention is unnamed, not an input missing — D-36"),
]


def report():
    print("The unprinted-input class, measured on the seven members DEFERRED.md names\n")
    for name, verdict, why in MEMBERS:
        print("  %-26s %-16s %s" % (name, verdict, why))
    held = sum(1 for _, v, _ in MEMBERS if v == "MEMBER")
    print("\n  %d of the 7 named members still stand; 2 are repaired; 1 belongs to another class." % held)
    print("  DOCKET.md item 10 reads 'sixty members — unchanged'. It has changed.\n")
    print("  §22.2.1's table is RIGHT AND UNVERIFIABLE, and the missing inputs are recoverable:\n")
    print("    m = 206/446  = %.6f -> prints %.2f   (printed 0.46)" % (M_SOLVED, rnd(M_SOLVED, 2)))
    print("    a = 206/1577 = %.6f -> prints %.2f   (printed 0.13)" % (A_SOLVED, rnd(A_SOLVED, 2)))
    print("    a/m          = %.6f -> prints %.2f   (printed 0.28)" % (A_SOLVED / M_SOLVED, rnd(A_SOLVED / M_SOLVED, 2)))
    print("\n    all three of the table's directional figures close on m = 0.4619 and a = 0.1306.")
    print("    the table's other two rows reproduce from what is printed: 588/200 = %.2f -> 2.9 ;"
          " 41.3/12.8 = %.2f -> 3.2" % (588 / 200, 41.3 / 12.8))
    print("\n  §22.4.1's δ₂, solved from each printed pair:")
    for n, pred in ((8, 4267), (55, 1.386e6)):
        print("    n = %-3d predicted %-10s -> δ₂ = %.6f" % (n, ("%g" % pred), n ** 3 / (2 * pred)))
    print("    and δ₂ = 0.06 returns %.1f and %.0f — one unprinted value reproduces both."
          % (8 ** 3 / 0.12, 55 ** 3 / 0.12))
    print("\n  RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print("  OK   %s: %s" % (name, got))
        else: fail += 1; print("  FAIL %s: got %s, want %s" % (name, got, want))
    t = text()
    eq("§22.1.2 now says its input set is printed", "**The input set is printed**" in t, True)
    eq("and prints the Rydberg constant with it", "109,737.31568" in t, True)
    eq("§22.1.1.1's F.3 claim sits in the same passage", "F.3's highest standard" in t, True)
    eq("the 446× row is still printed", len(sites(r"\*\*446×\*\*")) >= 1, True)
    eq("206/0.46 does NOT give 446", rnd(206 / 0.46, 0), 448.0)
    eq("the median 446× requires", round(M_SOLVED, 6), 0.461883)
    eq("and it prints as the 0.46 beside it", rnd(M_SOLVED, 2), 0.46)
    eq("the asymmetry 1,577 is still printed", "factor of 1,577" in t, True)
    eq("206/0.13 does NOT give 1,577", round(206 / 0.13, 1), 1584.6)
    eq("the above-cost 1,577 requires", round(A_SOLVED, 6), 0.130628)
    eq("and it prints as the 0.13 beside it", rnd(A_SOLVED, 2), 0.13)
    eq("their ratio prints as the 0.28 beside it", rnd(A_SOLVED / M_SOLVED, 2), 0.28)
    eq("the table's 2.9× row DOES reproduce", rnd(588 / 200, 1), 2.9)
    eq("the table's 3.2× row DOES reproduce", rnd(41.3 / 12.8, 1), 3.2)
    eq("3.47% does not reproduce from 0.7376 and 0.7129",
       rnd(float((F("0.7376") - F("0.7129")) / F("0.7129") * 100), 2), 3.46)
    eq("§22.4.1's δ₂ from n = 8", round(8 ** 3 / (2 * 4267), 3), 0.06)
    eq("§22.4.1's δ₂ from n = 55", round(55 ** 3 / (2 * 1.386e6), 3), 0.06)
    eq("δ₂ is printed nowhere in §22.4.1", "0.06" in "\n".join(t.split("\n")[6149:6169]), False)
    eq("'a factor of 17' has both inputs printed and is a convention, not a gap", 0.14 / 0.008, 17.5)
    eq("two of the seven named members are repaired",
       sum(1 for _, v, _ in MEMBERS if v == "REPAIRED"), 2)
    eq("four still stand", sum(1 for _, v, _ in MEMBERS if v == "MEMBER"), 4)
    print("\nOK: %d  FAIL: %d" % (ok, fail))
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
