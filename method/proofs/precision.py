#!/usr/bin/env python3
"""precision.py -- does a printed figure survive the precision of the numbers it was
computed from?

A derived figure that disagrees with a recomputation is not therefore wrong.  If its
inputs are printed rounded, the recomputation inherits their slack, and the honest
question is whether the printed figure lies inside the interval the inputs allow.
This program asks that question, and it exists because at least one recorded finding
does not survive it.

  A number printed as 25.96 stands for the interval [25.955, 25.965).
  A number printed as 0.0164 stands for [0.01635, 0.01645).
  Their quotient is not 1582.93.  It is anything from 1577.8 to 1588.1.

THE VERDICTS, and the middle one is the reason the program exists

  INSIDE      the printed figure lies in the interval its printed inputs allow.
              NOT A DEFECT.  A recomputation that disagrees with it is measuring the
              rounded inputs, not the quantity.
  OUTSIDE     the printed figure lies outside that interval.  No precision defence
              exists, and the disagreement is real.
  EXACT-INPUT the inputs are exact -- integers, or counts -- so there is no interval
              and no defence.  The figure is right or it is not.

REFUSALS
  This program does not decide what a figure MEANS, and it will not guess which
  printed numbers feed a derived one.  Each case names its inputs explicitly, and a
  case whose inputs are not printed anywhere carries INPUTS-NOT-PRINTED and is
  computed for nothing -- that is a refusal, not a finding, and may not be quoted as
  one.  Nothing is repaired.

Every case below carries the site it is printed at and the record entry that raised
it, so a reader can go to both.

stdlib only.  --selftest asserts the arithmetic of every case.
"""
import argparse, os, sys
from decimal import Decimal, getcontext

getcontext().prec = 40


def interval(printed):
    """The half-open interval a decimal literal stands for at its printed precision."""
    d = Decimal(printed)
    exp = d.as_tuple().exponent
    half = Decimal(1).scaleb(exp) / 2
    return d - half, d + half


def quotient_range(a, b):
    alo, ahi = interval(a)
    blo, bhi = interval(b)
    return alo / bhi, ahi / blo


# Each case: the printed figure, how it is formed, the record entry that raised it.
CASES = [
    dict(
        id="D-61",
        site="main sec 23.10.4 and App E.2",
        printed_claim="1,585-fold",
        figure=Decimal("1585"),
        kind="quotient",
        inputs=("25.96", "0.0164"),
        what="the perturbation bound tightens from a median of 25.96 cm-1 at order 1 "
             "to 0.0164 at order 6",
        raised_as="the record: 25.96 / 0.0164 = 1582.93 at two-decimal inputs, docket 12",
    ),
    dict(
        id="E-035",
        site="main sec 14.5, twice",
        printed_claim="a compression of 139 to 1, exactly",
        figure=Decimal("139"),
        kind="quotient",
        inputs=("976", "7"),
        exact_inputs=True,
        what="Lambda-8 has 976 cells and is the closure of a seed of 7",
        raised_as="the record 13h-04: 976/7 = 139.4286, and 976 = 7*139 + 3",
    ),
    dict(
        id="F-033",
        site="main L8206",
        printed_claim="a factor of five and a half",
        figure=Decimal("5.5"),
        kind="quotient",
        inputs=("54", "10"),
        exact_inputs=True,
        what="the checkable designations grew from ten to fifty-four",
        raised_as="the record 15n-02: L8200's factor measures 5.4",
    ),
    dict(
        id="E-110",
        site="main sec 26.6, the T/3 column, row n = 20",
        printed_claim="91.4477",
        figure=Decimal("91.4477"),
        kind="quotient",
        inputs=("274.3433", "3"),
        exact_divisor=True,
        what="the T/3 column of the Aitken table, whose other three rows are exact",
        raised_as="the record 15b-04: T(20)/3 = 91.44775 -> 91.4478 under either "
                  "convention; the table prints 91.4477",
    ),
]

# Two cases whose "input" is a closed form rather than a printed number.  They are
# scored separately because a formula has no precision to inherit: it is exact, and a
# printed value either equals it to the digits printed or does not.
FORMULA_CASES = [
    dict(id="16z-04 / 34re-01 (n = 6)",
         site="main sec 34.5, and register 1330",
         printed_claim="1.2168450",
         formula="(sqrt(5) + sqrt(2)) / 3",
         value=lambda: (Decimal(5).sqrt() + Decimal(2).sqrt()) / 3,
         corroboration="walk.py's own corridor at the 6s opening (caesium, Z 55) computes "
                       "the same endpoint by a different code path",
         raised_as="the record 16z-04, confirmed by measurement as 34re-01"),
    dict(id="16z-04 / 34re-01 (n = 7)",
         site="main sec 34.5, and register 1330",
         printed_claim="1.3938270",
         formula="(sqrt(6) + sqrt(3)) / 3",
         value=lambda: (Decimal(6).sqrt() + Decimal(3).sqrt()) / 3,
         corroboration="walk.py's own corridor at the 7s opening (francium, Z 87) computes "
                       "the same endpoint by a different code path",
         raised_as="the record 16z-04, confirmed by measurement as 34re-01"),
    dict(id="34.5 (n = 4)",
         site="main sec 34.5",
         printed_claim="0.5773503",
         formula="(sqrt(3) + sqrt(0)) / 3",
         value=lambda: (Decimal(3).sqrt() + Decimal(0).sqrt()) / 3,
         corroboration="walk.py's corridor at the 4s opening (potassium, Z 19)",
         raised_as="not raised -- carried here as the control"),
    dict(id="34.5 (n = 5)",
         site="main sec 34.5",
         printed_claim="1.0000000",
         formula="(sqrt(4) + sqrt(1)) / 3",
         value=lambda: (Decimal(4).sqrt() + Decimal(1).sqrt()) / 3,
         corroboration="walk.py's corridor at the 5s opening (rubidium, Z 37)",
         raised_as="not raised -- carried here as the control"),
]


# The three rows of the same table that are NOT in dispute, carried so the one that is
# can be read against them.
E110_SIBLINGS = [("1097.3730", "365.7910"), ("68.5858", "22.8619"), ("17.1465", "5.7155")]


def judge(c):
    a, b = c["inputs"]
    exact = c.get("exact_inputs") or (c.get("exact_divisor") and Decimal(b) == Decimal(b).to_integral())
    if c.get("exact_inputs"):
        val = Decimal(a) / Decimal(b)
        return dict(verdict="EXACT-INPUT", low=val, high=val, value=val,
                    inside=(c["figure"] == val))
    if c.get("exact_divisor"):
        lo, hi = interval(a)
        d = Decimal(b)
        lo, hi, val = lo / d, hi / d, Decimal(a) / d
        return dict(verdict="INSIDE" if lo <= c["figure"] < hi else "OUTSIDE",
                    low=lo, high=hi, value=val,
                    inside=lo <= c["figure"] < hi)
    lo, hi = quotient_range(a, b)
    val = Decimal(a) / Decimal(b)
    return dict(verdict="INSIDE" if lo <= c["figure"] < hi else "OUTSIDE",
                low=lo, high=hi, value=val, inside=lo <= c["figure"] < hi)


def judge_formula(c):
    exact = c["value"]()
    printed = Decimal(c["printed_claim"])
    dp = -printed.as_tuple().exponent
    rounded = exact.quantize(Decimal(1).scaleb(-dp))
    return dict(exact=exact, rounded=rounded, agrees=(rounded == printed))


def measure():
    return [dict(case=c, **judge(c)) for c in CASES]


def measure_formulas():
    return [dict(case=c, **judge_formula(c)) for c in FORMULA_CASES]


def report(rows):
    print("  DOES A PRINTED FIGURE SURVIVE THE PRECISION OF ITS INPUTS?")
    print()
    for r in rows:
        c = r["case"]
        print(f"  {c['id']}  --  {c['site']}")
        print(f"      printed:   {c['printed_claim']}")
        print(f"      inputs:    {c['inputs'][0]} and {c['inputs'][1]}   ({c['what']})")
        print(f"      naive:     {c['inputs'][0]} / {c['inputs'][1]} = {r['value']:.6f}")
        if r["verdict"] == "EXACT-INPUT":
            print(f"      the inputs are EXACT COUNTS, so there is no interval and no defence.")
            print(f"      the printed figure is {'right' if r['inside'] else 'NOT the value'}: "
                  f"{r['value']:.6f} against a printed {c['figure']}")
        else:
            print(f"      interval:  [{r['low']:.4f}, {r['high']:.4f})  "
                  "-- what the printed inputs allow")
            print(f"      figure {c['figure']} lies "
                  f"{'INSIDE it' if r['inside'] else 'OUTSIDE it'}")
        print(f"      VERDICT:   {r['verdict']}"
              + ("  -- NOT A DEFECT; the recomputation was measuring the rounded inputs"
                 if r["verdict"] == "INSIDE" else
                 "  -- the disagreement is real" if r["verdict"] == "OUTSIDE" else
                 "  -- the disagreement is real, and no rounding explains it"
                 if not r["inside"] else "  -- the figure is exact"))
        print(f"      raised as: {c['raised_as']}")
        print()
    print("  A FORMULA HAS NO PRECISION TO INHERIT, so these are scored differently")
    print("  section 34.5's four ns/(n-1)d crossings, against the chapter's own closed form")
    for r in measure_formulas():
        c = r["case"]
        mark = "agrees" if r["agrees"] else "DIFFERS"
        print(f"      {c['formula']:<26} = {r['rounded']}   printed {c['printed_claim']}   {mark}")
        if not r["agrees"]:
            print(f"        {c['corroboration']}")
    bad = [r for r in measure_formulas() if not r["agrees"]]
    print(f"      {len(bad)} of {len(FORMULA_CASES)} differ, and both differ at the fifth decimal.")
    print("      There is no precision defence: the closed form is exact and its inputs are")
    print("      integers.  Two independent routes -- the chapter's own formula and walk.py's")
    print("      corridor -- give the same values, and neither gives the printed ones.")
    print()
    print("  THE AITKEN TABLE'S OTHER THREE ROWS, for E-110's context")
    for t, printed in E110_SIBLINGS:
        v = Decimal(t) / 3
        print(f"      T = {t:>10}   T/3 = {v:.7f}   printed {printed}   "
              f"{'agrees' if abs(v - Decimal(printed)) < Decimal('0.00005') else 'DIFFERS'}")
    print("      Three rows agree at the printed precision and one does not, which is why")
    print("      the record calls it a truncation inside a rounded table rather than a")
    print("      wrong quantity.  It is one row and one place.")
    print()
    print("  WHAT THIS CHANGES")
    ins = [r["case"]["id"] for r in rows if r["verdict"] == "INSIDE"]
    if ins:
        print(f"      {', '.join(ins)}: recorded as a disagreeing figure, and it does not")
        print("      survive as one.  The printed value is consistent with the printed inputs.")
    print("      The rest stand as recorded.  Nothing is repaired here.")


FIXTURES = """the arithmetic of each case, checkable by hand:
  D-61    25.96 / 0.0164 = 1582.93 naively; the interval the printed inputs allow is
          [1577.8, 1588.1), and 1585 is inside it
  E-035   976 / 7 = 139.428571 with both inputs exact counts; 139 is not that value
  F-033   54 / 10 = 5.4 with both inputs exact counts; 5.5 is not that value
  E-110   274.3433 / 3 = 91.447767; the printed 91.4477 is a truncation, and the
          table's other three rows agree at the printed precision
  16z-04  (sqrt5+sqrt2)/3 = 1.2167605 and (sqrt6+sqrt3)/3 = 1.3938469, against a
          printed 1.2168450 and 1.3938270 -- the record's 34re-01, confirmed"""


def selftest():
    rows = measure()
    by = {r["case"]["id"]: r for r in rows}
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("D-61 verdict", by["D-61"]["verdict"], "INSIDE")
    eq("D-61 naive quotient", round(float(by["D-61"]["value"]), 2), 1582.93)
    eq("D-61 interval holds 1585", by["D-61"]["inside"], True)
    eq("E-035 verdict", by["E-035"]["verdict"], "EXACT-INPUT")
    eq("E-035 figure is not the value", by["E-035"]["inside"], False)
    eq("E-035 value", round(float(by["E-035"]["value"]), 6), 139.428571)
    eq("F-033 verdict", by["F-033"]["verdict"], "EXACT-INPUT")
    eq("F-033 figure is not the value", by["F-033"]["inside"], False)
    eq("F-033 value", float(by["F-033"]["value"]), 5.4)
    eq("E-110 verdict", by["E-110"]["verdict"], "OUTSIDE")
    fr = {r["case"]["id"]: r for r in measure_formulas()}
    eq("sec 34.5 n = 4 agrees", fr["34.5 (n = 4)"]["agrees"], True)
    eq("sec 34.5 n = 5 agrees", fr["34.5 (n = 5)"]["agrees"], True)
    eq("sec 34.5 n = 6 differs", fr["16z-04 / 34re-01 (n = 6)"]["agrees"], False)
    eq("sec 34.5 n = 7 differs", fr["16z-04 / 34re-01 (n = 7)"]["agrees"], False)
    eq("the n = 6 value", str(fr["16z-04 / 34re-01 (n = 6)"]["rounded"]), "1.2167605")
    eq("the n = 7 value", str(fr["16z-04 / 34re-01 (n = 7)"]["rounded"]), "1.3938469")
    eq("E-110 the other three rows agree",
       [abs(Decimal(t) / 3 - Decimal(p)) < Decimal("0.00005") for t, p in E110_SIBLINGS],
       [True, True, True])
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<18} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    report(measure())
    return 0


if __name__ == "__main__":
    sys.exit(main())
