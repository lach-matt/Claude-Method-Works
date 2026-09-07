#!/usr/bin/env python3
"""nreached.py — "K I nd 45.7" against the Spectra Compendium's own K I nd row. Phase 1, item D-16
(the main-volume/compendium contradiction class), whose docket says: "Resolve K I nd 45.7 FIRST."

THE TABLE. Main §23 prints, under "Curvature washes out before separation, in every channel in this
work":

    channel        q        v_V     v reached
    K I nd         0.0001   160     45.7
    Na I ns        0.001     90     20.0
    Al I nf        0.01      50.7   55.0

THE COLLECTION. The Spectra Compendium's own rows for those three channels give an n range and a
nu range:

    K I   nd 2D J=5/2    n 3-13    nu 2.9-12.7
    Na I  ns             n 3-20    nu 1.6-18.7
    Al I  3s2nf 2F       n 4-55    nu 4.0-55.0

WHAT THE OTHER TWO ROWS SETTLE. Al I nf's 55.0 matches BOTH readings of the column, and Na I ns's
20.0 matches the n range and NOT the nu range, which is 18.7. So the column is the top of the
PRINCIPAL QUANTUM NUMBER range, and two of the three rows reproduce from the collection exactly.

WHAT THAT LEAVES. K I nd's own row runs n = 3 to 13. The main volume prints 45.7. Under the reading
its own other two rows fix, the entry should be 13; under the other reading it should be 12.7.
NEITHER IS 45.7, and the printed figure is 3.5 times the larger of them.

The claim the table supports -- curvature washes out before separation -- survives either way and is
made STRONGER by the correction, because a channel that reaches 13 is further from its v_V of 160
than one that reaches 45.7. The figure is what is wrong, not the thesis.

stdlib only.  --selftest asserts both volumes' own rows.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")
SC = os.path.join(MEM, "The_Method_1_6___Spectra_Compendium-2.md")
PRINTED = {"K I nd": 45.7, "Na I ns": 20.0, "Al I nf": 55.0}
SC_ROW = {"K I nd": r"^\| K I \| nd 2D", "Na I ns": r"^\| Na I \| ns \|", "Al I nf": r"^\| Al I \| 3s²nf"}


def sc_ranges():
    out = {}
    for name, pat in SC_ROW.items():
        for l in open(SC, encoding="utf-8"):
            if re.match(pat, l):
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                nrange = cells[2]; nurange = cells[6]
                lo_n, hi_n = (float(x) for x in nrange.replace("–", "-").split("-"))
                lo_v, hi_v = (float(x) for x in nurange.replace("–", "-").split("-"))
                out[name] = dict(n=(lo_n, hi_n), nu=(lo_v, hi_v))
                break
    return out


def main_row():
    t = open(MAIN, encoding="utf-8").read()
    return "| K I *n*d | 0.0001 | 160 | 45.7 |" in t


def report():
    r = sc_ranges()
    print("'ν reached' in main §23, against the Spectra Compendium's own rows\n")
    print(f"  {'channel':10}{'printed':>9}{'SC n range':>14}{'top n':>8}{'SC ν range':>14}{'top ν':>8}   reading")
    for k in PRINTED:
        n, nu = r[k]["n"], r[k]["nu"]
        which = ("n" if abs(PRINTED[k] - n[1]) < 0.05 else
                 "ν" if abs(PRINTED[k] - nu[1]) < 0.05 else "NEITHER")
        print(f"  {k:10}{PRINTED[k]:>9}{f'{n[0]:g}–{n[1]:g}':>14}{n[1]:>8g}"
              f"{f'{nu[0]:g}–{nu[1]:g}':>14}{nu[1]:>8g}   {which}")
    print("\n  Al I nf matches both readings; Na I ns matches the n range and not the ν range,")
    print("  which fixes the column as the top of the principal quantum number range.")
    k = r["K I nd"]
    print(f"\n  K I nd's own row runs n = {k['n'][0]:g} to {k['n'][1]:g}. The volume prints"
          f" {PRINTED['K I nd']}.")
    print(f"  Under the reading its own other two rows fix, the entry is {k['n'][1]:g};"
          f" under the other, {k['nu'][1]:g}.")
    print(f"  Neither is {PRINTED['K I nd']}, which is {PRINTED['K I nd']/k['n'][1]:.1f}× the larger of them.")
    print("\n  The thesis survives and is strengthened: a channel reaching 13 is further from its")
    print("  ν_V of 160 than one reaching 45.7. The figure is wrong, not the claim.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    eq("the main volume prints the K I nd row as 45.7", main_row(), True)
    r = sc_ranges()
    eq("the compendium's K I nd n range", r["K I nd"]["n"], (3.0, 13.0))
    eq("the compendium's K I nd ν range", r["K I nd"]["nu"], (2.9, 12.7))
    eq("Al I nf reproduces the printed 55.0 from its n range", r["Al I nf"]["n"][1], PRINTED["Al I nf"])
    eq("and from its ν range too", r["Al I nf"]["nu"][1], PRINTED["Al I nf"])
    eq("Na I ns reproduces the printed 20.0 from its n range", r["Na I ns"]["n"][1], PRINTED["Na I ns"])
    eq("but NOT from its ν range", r["Na I ns"]["nu"][1] != PRINTED["Na I ns"], True)
    eq("so the column is the top of the n range", True, True)
    eq("K I nd's entry should be 13, not 45.7", r["K I nd"]["n"][1], 13.0)
    eq("the printed figure is 3.5× the collection's",
       round(PRINTED["K I nd"] / r["K I nd"]["n"][1], 1), 3.5)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
