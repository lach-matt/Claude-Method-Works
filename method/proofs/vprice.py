#!/usr/bin/env python3
"""vprice.py — V = 4ν/3 printed as an equality. Phase 1, items D-14 and E-089 (the
truncation-printed-as-equality class, at its largest site).

WHAT THE VOLUME PRINTS. `V = 4ν/3` appears **24 times on 22 lines of the main volume** and once in the
Mathematical Compendium, in tables, in summary rows, in the chapter's thesis sentence and in the
priority section's title -- almost always with an equals sign and no qualifier.

WHAT THE VOLUME ALSO PRINTS, once, at §23:

  "The exact V is rational at every ν -- 32/11, 54/13, 256/47, 250/37, 4000/299 -- and
   4ν/3 + 4/(9ν) is its ASYMPTOTIC form, LOW BY 0.69% AT ν = 2"

and the closed form two lines below: V = 4ν³ / (h(3ν² − h²)), which at h = 1 is V = 4ν³/(3ν² − 1).

MEASURED HERE. All five printed rationals reproduce exactly from that closed form, so the object is
identified beyond doubt. The two-term asymptotic is low by 0.694% at ν = 2, which is the volume's own
0.69%. **And the bare 4ν/3 -- the form the other twenty-two sites print with an equals sign -- is low
by 8.33% at ν = 2**, twelve times the error of the form the volume calls asymptotic.

So the defect is not that 4ν/3 is wrong. It is that ONE site states it as an approximation with its
error, and twenty-two lines state it as an identity, and the reader who meets any of the twenty-two first has
no way to know. The class is docket 12's, and this is its largest instance.

NOTHING IS REPAIRED. Which sites take a qualifier and which are safe as printed is prose.

stdlib only.  --selftest asserts the volume's own five rationals and its own 0.69%.
"""
import argparse, os, re, sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
PRINTED_RATIONALS = {2: F(32, 11), 3: F(54, 13), 4: F(256, 47), 5: F(250, 37), 10: F(4000, 299)}
PRINTED_ASYMPTOTIC_ERROR_AT_2 = 0.69     # per cent, low


def V_exact(nu, h=1):
    """§23's closed form, as the volume prints it after its sign was repaired: 4v^3 / (h(3v^2 - h^2))."""
    nu = F(nu); h = F(h)
    return 4 * nu ** 3 / (h * (3 * nu ** 2 - h ** 2))


def V_two_term(nu):
    """the volume's asymptotic form: 4v/3 + 4/(9v)."""
    nu = F(nu)
    return F(4, 3) * nu + F(4, 9) / nu


def V_bare(nu):
    """the form twenty-two sites print with an equals sign."""
    return F(4, 3) * F(nu)


def sites():
    m = open(os.path.join(MEM, "The_Method_1_6-2.md"), encoding="utf-8").read()
    mc = open(os.path.join(MEM, "The_Method_1_6___Mathematical_Compendium-2.md"),
              encoding="utf-8").read()
    return m.count("4ν/3"), mc.count("4ν/3")


def report():
    main, mc = sites()
    print("V = 4ν/3, printed as an equality\n")
    print(f"  occurrences of the string '4ν/3': main volume {main} on 22 lines, Mathematical Compendium {mc}\n")
    print(f"  {'ν':>4}{'exact V = 4ν³/(3ν²−1)':>24}{'printed':>12}{'4ν/3 + 4/(9ν)':>16}"
          f"{'low by':>9}{'bare 4ν/3':>12}{'low by':>9}")
    for nu, pr in PRINTED_RATIONALS.items():
        ex = V_exact(nu); tt = V_two_term(nu); bs = V_bare(nu)
        print(f"  {nu:>4}{str(ex):>24}{str(pr):>12}{float(tt):>16.6f}"
              f"{float(100*(1-tt/ex)):>8.2f}%{float(bs):>12.6f}{float(100*(1-bs/ex)):>8.2f}%")
    print(f"\n  All five printed rationals reproduce exactly from the closed form, so the object is")
    print(f"  identified. The two-term asymptotic is low by {float(100*(1-V_two_term(2)/V_exact(2))):.2f}% at ν = 2,")
    print(f"  which is the volume's own {PRINTED_ASYMPTOTIC_ERROR_AT_2}%. The BARE form is low by")
    print(f"  {float(100*(1-V_bare(2)/V_exact(2))):.2f}% there — twelve times the error of the form the volume itself")
    print("  calls asymptotic, and it is the bare form that twenty-two sites print with an equals sign.")
    print("\n  One site states the approximation and its error; twenty-two state an identity. RECORDED,")
    print("  NOT REPAIRED — which sites take a qualifier is prose.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    for nu, pr in PRINTED_RATIONALS.items():
        eq(f"the closed form reproduces the printed V at ν = {nu}", V_exact(nu), pr)
    eq("the two-term asymptotic is low by 0.69% at ν = 2",
       round(float(100 * (1 - V_two_term(2) / V_exact(2))), 2), PRINTED_ASYMPTOTIC_ERROR_AT_2)
    eq("the bare form is low by 8.33% at ν = 2",
       round(float(100 * (1 - V_bare(2) / V_exact(2))), 2), 8.33)
    eq("so the bare form's error is twelve times the asymptotic's",
       round(float((1 - V_bare(2) / V_exact(2)) / (1 - V_two_term(2) / V_exact(2)))), 12)
    main, mc = sites()
    eq("occurrences in the main volume", main, 24)
    eq("sites in the Mathematical Compendium", mc, 1)
    eq("the exact V exceeds the bare form at every ν measured",
       all(V_exact(n) > V_bare(n) for n in PRINTED_RATIONALS), True)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
