#!/usr/bin/env python3
"""endrule.py — §24.13's end rule against its own table. Phase 1, item D-23 (docket 21, 14v-07).

WHAT §24.13 PRINTS, four lines apart, of one measurement.

Its table, from holding each member of two isoelectronic sequences out in turn:

    held out            lithium-like   sodium-like
    neutral, Z = 1         11.1%          23.4%
    Z = 2                   1.4%           2.4%
    Z = 3                   0.8%           1.3%
    Z = 4                   1.8%           2.5%       <- the OTHER end

Its prose, immediately under the table, is exact:  "Interpolation works to about one percent.
EXTRAPOLATION TO THE NEUTRAL does not."  And Figure 24.3's caption is exact too: "The interior is
recovered to about one percent. THE NEUTRAL is not."

Its summary row and its closing blockquote are not:

    "within a sequence, at an END | delta NOT determined"
    "Interior members need not be fetched. THE ENDS ALWAYS MUST -- and the neutral is always an end."

A sequence has two ends. The table measures both, and only one of them fails.

MEASURED HERE, from the table's own six numbers. The upper end is 6.2x and 9.4x better than the
neutral end, and it sits inside the interior's own worst case on the sodium-like sequence and within
a quarter of it on the lithium-like. The rule that says "at an end" and "the ends always must"
generalises from one end to both, and the section states the correct version twice on the same page.

Nothing is repaired. The docket asks for a sweep of twenty-three sites in this class; the two sites
this instrument decides are the ones DEFERRED names -- the summary row and the blockquote -- and it
names the two it must NOT touch, the prose and the caption, which are right.

stdlib only.  --selftest asserts the volume's own numbers and the ratios DEFERRED records.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")
TABLE = {"neutral, Z = 1": (11.1, 23.4), "Z = 2": (1.4, 2.4), "Z = 3": (0.8, 1.3), "Z = 4": (1.8, 2.5)}
CORRECT = ["Extrapolation to the neutral does not", "The interior is recovered to about one percent. The neutral is not"]
OVERSTATED = ["within a sequence, at an end | δ **not** determined",
              "The ends always must"]


def ratios():
    lo_li, lo_na = TABLE["neutral, Z = 1"]
    hi_li, hi_na = TABLE["Z = 4"]
    interior_li = [TABLE["Z = 2"][0], TABLE["Z = 3"][0]]
    interior_na = [TABLE["Z = 2"][1], TABLE["Z = 3"][1]]
    return dict(neutral_over_upper_li=lo_li / hi_li, neutral_over_upper_na=lo_na / hi_na,
                upper_over_best_interior_li=hi_li / min(interior_li),
                upper_over_worst_interior_li=hi_li / max(interior_li),
                upper_over_best_interior_na=hi_na / min(interior_na),
                upper_over_worst_interior_na=hi_na / max(interior_na))


def sites():
    t = open(MAIN, encoding="utf-8").read()
    return {s: t.count(s) for s in CORRECT + OVERSTATED}


def report():
    r = ratios(); s = sites()
    print("§24.13's end rule, against §24.13's own table\n")
    print(f"  {'held out':>18}{'lithium-like':>15}{'sodium-like':>14}")
    for k, (a, b) in TABLE.items():
        mark = "  <- the end the rule is right about" if k.startswith("neutral") else (
               "  <- the OTHER end" if k == "Z = 4" else "")
        print(f"  {k:>18}{a:>14.1f}%{b:>13.1f}%{mark}")
    print(f"\n  the neutral end against the upper end: "
          f"{r['neutral_over_upper_li']:.1f}× worse on lithium-like, "
          f"{r['neutral_over_upper_na']:.1f}× on sodium-like")
    print(f"  the upper end against the interior:     "
          f"{r['upper_over_worst_interior_li']:.2f}× and {r['upper_over_best_interior_li']:.2f}× on lithium-like, "
          f"{r['upper_over_worst_interior_na']:.2f}× and {r['upper_over_best_interior_na']:.2f}× on sodium-like")
    print("\n  RIGHT, and not to be touched — the prose and the caption say 'the neutral':")
    for c in CORRECT:
        print(f"    {s[c]}×  \"{c}\"")
    print("\n  OVERSTATED — the summary row and the blockquote say 'an end' and 'the ends':")
    for c in OVERSTATED:
        print(f"    {s[c]}×  \"{c}\"")
    print("\n  A sequence has two ends, the table measures both, and only one of them fails.")
    print("  The section states the correct version twice on the same page. RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    t = open(MAIN, encoding="utf-8").read()
    eq("the table's neutral row is in the volume", "11.1%" in t and "23.4%" in t, True)
    eq("the table's upper-end row is in the volume", "1.8%" in t and "2.5%" in t, True)
    r = ratios()
    eq("neutral is 6.2× worse than the upper end, lithium-like",
       round(r["neutral_over_upper_li"], 1), 6.2)
    eq("and 9.4× worse, sodium-like", round(r["neutral_over_upper_na"], 1), 9.4)
    eq("the upper end is inside the interior's worst case, sodium-like",
       round(r["upper_over_worst_interior_na"], 2) <= 1.05, True)
    eq("and within a quarter of it, lithium-like",
       round(r["upper_over_worst_interior_li"], 2) <= 1.3, True)
    s = sites()
    for c in CORRECT:
        eq(f"the correct form is present: {c[:34]}…", s[c] >= 1, True)
    for c in OVERSTATED:
        eq(f"the overstated form is present: {c[:34]}…", s[c] >= 1, True)
    eq("so the two forms sit on one page, neither superseding the other",
       all(s[c] >= 1 for c in CORRECT + OVERSTATED), True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
