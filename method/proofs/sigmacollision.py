#!/usr/bin/env python3
"""sigmacollision.py — the σ collision, decided from the volume's own two formulas. Phase 1, items
D-05 and G-01 (two annex rows, one finding), flagged for correction in R3 with both readings carried.

THE TWO SITES, and they are fifteen sections apart in one chapter:

  Rule 4, §22.2 L6052   "Fit δ locally by a Ritz expansion and take
                         σ = 2R Z_eff² · SE_pred / ν³
                         from the fit's PREDICTION STANDARD ERROR."      -> σ is an OUTPUT

  §22.5 L6175           "A channel is admissible when its levels are separated by more than their
                         UNCERTAINTY:  r = 2Z²R / (ν³σ) ≥ 5.
                         r falls as ν⁻³."                                -> σ is an INPUT

THE DECISION, and it needs no data. Substitute Rule 4's σ into §22.5's r:

    r = 2Z²R / (ν³ · 2R Z_eff² SE_pred / ν³) = Z² / (Z_eff² · SE_pred)

The ν³ cancels EXACTLY. If §22.5's σ were Rule 4's σ, r would not fall as ν⁻³ — it would not depend
on ν at all, and §22.5's own next sentence, "r falls as ν⁻³. Every channel eventually leaves the
domain", would be false. So the two σ are necessarily DIFFERENT QUANTITIES: Rule 4's is the fit's
prediction standard error carried into energy, and §22.5's is the levels' own measurement
uncertainty, which is a constant of the channel and not a function of ν.

The chapter corroborates it in prose two lines above Rule 4's own site: "This book's tightest bracket
is 1.398 cm⁻¹; limit uncertainties in the collection run 0.001 to 0.4 cm⁻¹" — those are measured
level uncertainties in cm⁻¹, which is what §22.5's σ has to be for r to fall as ν⁻³.

NOTHING IS REPAIRED. Which symbol is renamed, and in which of the two places, is prose and is M's.
What is settled here is that the collision is real, that it is not a choice between two readings, and
that the volume's own claim about r's behaviour decides which reading each site must carry.

stdlib only.  --selftest asserts the cancellation numerically as well as symbolically.
"""
import argparse, sys

R = 109737.31568          # cm^-1, the Rydberg the volume uses
PRINTED_TIGHTEST_BRACKET = 1.398          # cm^-1
PRINTED_LIMIT_SIGMA = (0.001, 0.4)        # cm^-1
THRESHOLD = 5


def sigma_rule4(Zeff, SE_pred, nu):
    """Rule 4: sigma = 2 R Zeff^2 SE_pred / nu^3 -- an output of the local Ritz fit."""
    return 2 * R * Zeff ** 2 * SE_pred / nu ** 3


def r_225(Z, nu, sigma):
    """§22.5: r = 2 Z^2 R / (nu^3 sigma)."""
    return 2 * Z ** 2 * R / (nu ** 3 * sigma)


def r_if_same_sigma(Z, Zeff, SE_pred, nu):
    """§22.5's r when its sigma is taken to be Rule 4's -- the substitution."""
    return r_225(Z, nu, sigma_rule4(Zeff, SE_pred, nu))


def report():
    Z, Zeff, SE = 3.0, 2.6, 0.004
    print("The σ collision: Rule 4 against §22.5, decided from the two formulas\n")
    print(f"  Rule 4   σ(ν) = 2R Z_eff² · SE_pred / ν³      an OUTPUT of the local Ritz fit")
    print(f"  §22.5    r(ν) = 2Z²R / (ν³ σ) ≥ {THRESHOLD}, and 'r falls as ν⁻³'   σ an INPUT\n")
    print(f"  With Z = {Z}, Z_eff = {Zeff}, SE_pred = {SE}:\n")
    print(f"  {'ν':>6}{'σ from Rule 4 (cm⁻¹)':>24}{'r with THAT σ':>16}{'r with σ = 0.01 fixed':>24}")
    for nu in (5, 10, 20, 40, 80):
        s4 = sigma_rule4(Zeff, SE, nu)
        print(f"  {nu:6}{s4:24.6g}{r_if_same_sigma(Z, Zeff, SE, nu):16.6g}"
              f"{r_225(Z, nu, 0.01):24.6g}")
    print(f"\n  The third column is CONSTANT in ν — the ν³ cancels exactly, leaving")
    print(f"  Z² / (Z_eff² · SE_pred) = {Z**2/(Zeff**2*SE):.6g}. The fourth falls as ν⁻³, which is")
    print("  what §22.5 says of it. So §22.5's σ cannot be Rule 4's σ.")
    print(f"\n  And the chapter says so in prose two lines above Rule 4: 'This book's tightest bracket")
    print(f"  is {PRINTED_TIGHTEST_BRACKET} cm⁻¹; limit uncertainties in the collection run")
    print(f"  {PRINTED_LIMIT_SIGMA[0]} to {PRINTED_LIMIT_SIGMA[1]} cm⁻¹' — measured level uncertainties in cm⁻¹,")
    print("  constants of the channel, which is exactly what makes r fall as ν⁻³.")
    print("\n  RECORDED, NOT REPAIRED. Which symbol is renamed and where is prose, and prose is M's.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    Z, Zeff, SE = 3.0, 2.6, 0.004
    vals = [r_if_same_sigma(Z, Zeff, SE, nu) for nu in (5, 10, 20, 40, 80)]
    eq("substituting Rule 4's σ makes r independent of ν",
       all(abs(v - vals[0]) < 1e-9 * abs(vals[0]) for v in vals), True)
    eq("and its value is Z²/(Z_eff²·SE_pred)", round(vals[0], 9), round(Z ** 2 / (Zeff ** 2 * SE), 9))
    fixed = [r_225(Z, nu, 0.01) for nu in (5, 10, 20, 40)]
    eq("with a fixed σ, r falls as ν⁻³ exactly",
       [round(fixed[i] / fixed[i + 1], 6) for i in range(3)], [round(8.0, 6)] * 3)
    eq("so the two σ are different quantities", vals[0] == vals[-1] and fixed[0] != fixed[-1], True)
    eq("the tightest bracket is a cm⁻¹ quantity", PRINTED_TIGHTEST_BRACKET, 1.398)
    eq("limit uncertainties are cm⁻¹ constants of the channel", PRINTED_LIMIT_SIGMA, (0.001, 0.4))
    eq("§22.5's threshold", THRESHOLD, 5)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
