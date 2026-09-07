#!/usr/bin/env python3
"""voidrange.py — §10.2's "seventeenfold" against Figure 10.1's "hundredfold". Phase 1, items D-60,
F-191 and H-23 (three annex rows, one finding).

THE COLLISION. Two lines apart, of one quantity:

  §10.2 L2038      "The void-free fraction is 27.7-30.1% across 776 million pairs and a
                    SEVENTEENFOLD range in cell count. Stable, no trend."
  Figure 10.1 caption L2058
                   "The void-free fraction across a HUNDREDFOLD range in cell count, computed
                    exhaustively over 776 million pairs. Stable at 27.7-30.1%, with no trend."
  Appendix L10289  "void-free fraction stable  27.7-30.1%  2.4 points over a 100x"

Seventeen and a hundred are not the same number and the two sentences describe one measurement.
A third site, main L3538's "2.17-fold spread in cell count", is a DIFFERENT object -- one transition
said four ways -- and is not part of this collision; it is listed here so it is not swept in.

WHY IT CANNOT BE DECIDED FROM THE RECORD, AND THE REGISTER SAYS SO FIRST. Register 1830 already
measured that these very figures name no population: "the pair population at the base caps
(3,3,1,3,1) is 475,800, and no one-parameter cap family from the base sums to 776 million ... 1.33
to 1.66 sampled across six settings to 234,340 cells ... a measurement at a population the record
does not name." A range in cell count is a ratio between the largest and smallest member of a cap
family, and the family is not named anywhere.

WHAT IS MEASURABLE, AND IT IS THE POINT. Every cell-count ratio the record DOES name is computed
here, and NONE of them is seventeen and none is a hundred. So the collision is not a choice between
a right number and a wrong one: both printed ranges are unsupported by every family the corpus
names, and the repair is a measurement someone must make, not a word someone must pick.

stdlib only; imports the seated tower by path.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
PRINTED = {"section_10_2": 17, "figure_caption": 100, "appendix": 100, "other_object": 2.17}
R1830 = {"base_pairs": 475800, "sampled_to_cells": 234340, "pairs_claimed": 776_000_000,
         "factor_exhaustive": 1.4081}


def tower():
    spec = importlib.util.spec_from_file_location("t2", os.path.join(MEM, "tower-2.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def ratios():
    t2 = tower()
    sizes = {d: len(t2.STAGES[d]()) for d in range(8, 14)}
    base = sizes[8]
    out = []
    out.append(("the tower Λ8 to Λ13", base, sizes[13], sizes[13] / base))
    out.append(("Λ8 to Λ12", base, sizes[12], sizes[12] / base))
    out.append(("Λ8 to Λ11", base, sizes[11], sizes[11] / base))
    out.append(("Λ8 to Λ10", base, sizes[10], sizes[10] / base))
    out.append(("register 1830's six sampled settings", base, R1830["sampled_to_cells"],
                R1830["sampled_to_cells"] / base))
    return sizes, out


def report():
    sizes, R = ratios()
    print("§10.2's range in cell count, against every family the record names\n")
    print(f"  the tower's own sizes: " + ", ".join(f"Λ{d} {n:,}" for d, n in sizes.items()))
    print(f"\n  {'family':40}{'from':>9}{'to':>10}{'ratio':>9}   17x?  100x?")
    for name, a, b, r in R:
        print(f"  {name:40}{a:>9,}{b:>10,}{r:>9.1f}   "
              f"{'yes' if abs(r-17) < 0.5 else 'no ':<6}{'yes' if abs(r-100) < 5 else 'no'}")
    print(f"\n  §10.2 prints a {PRINTED['section_10_2']}-fold range; Figure 10.1's caption and the")
    print(f"  appendix row print a {PRINTED['figure_caption']}-fold one, of the same measurement.")
    print("  NO family the record names gives either number.")
    print(f"\n  Register 1830 already recorded why: the base-cap pair population is "
          f"{R1830['base_pairs']:,},")
    print(f"  no one-parameter cap family from the base sums to the {R1830['pairs_claimed']:,} pairs")
    print("  both sentences claim, and the six sampled settings reach 234,340 cells — a 240-fold")
    print("  range, not seventeen and not a hundred. The population is not named anywhere.")
    print("\n  So this is not a choice between a right number and a wrong one. Both are unsupported,")
    print("  and what the volume owes is the cap family, after which the ratio is arithmetic.")
    print("\n  NOT part of this collision: main L3538's '2.17-fold spread in cell count' is a")
    print("  different object — one transition said four ways — and is named here so it is not swept in.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    sizes, R = ratios()
    eq("Λ8 is 976 cells", sizes[8], 976)
    eq("Λ13 is 199,130 cells", sizes[13], 199130)
    eq("the tower's own range, rounded", round(sizes[13] / sizes[8]), 204)
    eq("register 1830's sampled range, rounded", round(R1830["sampled_to_cells"] / sizes[8]), 240)
    eq("no named family gives seventeen", any(abs(r - 17) < 0.5 for _, _, _, r in R), False)
    eq("no named family gives a hundred", any(abs(r - 100) < 5 for _, _, _, r in R), False)
    eq("the two printed ranges differ", PRINTED["section_10_2"] != PRINTED["figure_caption"], True)
    eq("the appendix row agrees with the caption, not the section",
       PRINTED["appendix"], PRINTED["figure_caption"])
    eq("the 2.17-fold site is a different object", PRINTED["other_object"], 2.17)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
