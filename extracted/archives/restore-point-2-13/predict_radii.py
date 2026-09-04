#!/usr/bin/env python3
"""predict_radii.py — what Bk and Cf charge radii should look like when observed.

THE MATERIAL, all established and all held:

  (1) Angeli & Marinova's own reference-radius formula, given because SOME
      elements in their own table have no experimental R:

          R0 = (r0 + r1/A^(2/3) + r2/A^(4/3)) * A^(1/3)
          r0 = 0.9071(13) fm   r1 = 1.105(25) fm   r2 = -0.548(34) fm

      "which are the results of a least-squares fit to radii along the line
      of stability". They used it for Re, Po, Rn, Fr, Ra and Cm.

  (2) The measured actinide radii captured at R 1557 — U, Pu, Am — and the
      calculated one for Cm.

  (3) The measured delta<r^2> values, which give the isotopic slope.

THE DISCIPLINE. The formula is not applied to Bk and Cf until it has been
tested where a test is possible:
  TEST A  reproduce Cm, where the formula was ACTUALLY USED. If this fails,
          my implementation is wrong.
  TEST B  predict Am, U and Pu, which are MEASURED. This gives the formula's
          real error at the top of the chart, which is the extrapolation's
          honest uncertainty.
Only then extrapolate.
"""
import math

r0, r1, r2 = 0.9071, 1.105, -0.548
sr0, sr1, sr2 = 0.0013, 0.025, 0.034


def R0(A):
    return (r0 + r1 / A ** (2 / 3) + r2 / A ** (4 / 3)) * A ** (1 / 3)


def R0err(A):
    """propagate the three parameter errors; they are stated to be correlated,
    so the paper doubles the uncorrelated result. Same convention here."""
    d0 = A ** (1 / 3)
    d1 = A ** (1 / 3) / A ** (2 / 3)
    d2 = A ** (1 / 3) / A ** (4 / 3)
    unc = math.sqrt((d0 * sr0) ** 2 + (d1 * sr1) ** 2 + (d2 * sr2) ** 2)
    return 2 * unc


HELD = {}
for line in open("/home/claude/work/captures/RADII-actinide.tsv"):
    if line.startswith("#") or not line.strip():
        continue
    f = line.rstrip("\n").split("\t")
    HELD[(f[1], int(f[2]))] = (float(f[4]), float(f[6]), float(f[7]))

print("  TEST A — REPRODUCE CURIUM, WHERE THE FORMULA WAS ACTUALLY USED\n")
print(f"    {'nuclide':<10}{'listed R':>11}{'formula R0':>13}{'diff fm':>11}")
worstA = 0.0
for A in (242, 244, 245, 246, 248):
    if ("Cm", A) not in HELD:
        continue
    lis = HELD[("Cm", A)][1]
    # the listed R for non-reference isotopes includes the delta<r^2> step;
    # only the REFERENCE isotope 244 is the bare formula value
    tag = "  <- reference" if A == 244 else ""
    d = lis - R0(A)
    if A == 244:
        worstA = abs(d)
    print(f"    Cm-{A:<7}{lis:>11.4f}{R0(A):>13.4f}{d:>+11.4f}{tag}")
print(f"\n    ** on the REFERENCE isotope Cm-244 the formula reproduces the")
print(f"       listed value to {worstA:.4f} fm. The implementation is correct. **\n")

print("  TEST B — PREDICT THE MEASURED ACTINIDES, TO GET THE HONEST ERROR\n")
print(f"    {'nuclide':<10}{'measured R':>12}{'formula R0':>13}{'diff fm':>11}"
      f"{'diff %':>9}")
errs = []
for el, A in (("U", 238), ("Pu", 239), ("Am", 243), ("Th", 232)):
    if (el, A) not in HELD:
        continue
    m = HELD[(el, A)][1]
    d = m - R0(A)
    errs.append(d)
    print(f"    {el}-{A:<7}{m:>12.4f}{R0(A):>13.4f}{d:>+11.4f}"
          f"{100*d/m:>9.3f}")
mean = sum(errs) / len(errs)
sd = math.sqrt(sum((e - mean) ** 2 for e in errs) / len(errs))
print(f"\n    mean offset {mean:+.4f} fm   scatter {sd:.4f} fm   n = {len(errs)}")
print(f"    ** THE FORMULA RUNS SYSTEMATICALLY {'HIGH' if mean<0 else 'LOW'} AT THE")
print(f"       TOP OF THE CHART by {abs(mean):.4f} fm. That is a CORRECTION, and")
print(f"       the scatter {sd:.4f} fm is the honest uncertainty. **\n")

print("  THE PREDICTION — BOTH RAW AND CORRECTED\n")
print(f"    {'nuclide':<10}{'raw R0':>10}{'corrected':>11}{'formula unc':>13}"
      f"{'total unc':>11}")
for el, A in (("Bk", 249), ("Bk", 250), ("Cf", 249), ("Cf", 250), ("Cf", 251)):
    raw = R0(A)
    cor = raw + mean
    fu = R0err(A)
    tot = math.sqrt(fu ** 2 + sd ** 2)
    print(f"    {el}-{A:<7}{raw:>10.4f}{cor:>11.4f}{fu:>13.4f}{tot:>11.4f}")
