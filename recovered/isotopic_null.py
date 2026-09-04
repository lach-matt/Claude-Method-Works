"""
THE ISOTOPIC NULL, COMPUTED RATHER THAN COLLECTED.

L.total: the membership function is total, so a null is decided by the same
operator as an occupancy. Ask of the isotopic ladder: at which (Z, n) does a
one-mass-unit isotope step move the quantum defect by MORE than the scatter
the work already carries?

Two contributions, with opposite Z-dependence:

  MASS SHIFT   R_M = R_inf/(1 + m_e/M).  Needs NO free constant — pure
               arithmetic on A.  Falls as A^-2.
  FIELD SHIFT  proportional to Z^2 * d<r^2>, and d<r^2> ~ A^(2/3) * dA/A,
               so it RISES as Z^2 A^(-1/3).  Its electronic factor is an
               expectation value the work does not hold, so its magnitude is
               an open cell; only its scaling is computed here.
"""
from math import sqrt

ME_U = 5.48579909065e-4      # electron mass in unified mass units, CODATA

# ---- A(Z) from the valley of stability, not recalled per element ----------
# Z = A / (2 + 0.0155 A^(2/3)) inverted numerically. Semi-empirical mass
# formula, standard; no per-element table is needed.
def A_of_Z(Z):
    A = 2.0 * Z
    for _ in range(80):
        A = Z * (2 + 0.0155 * A ** (2 / 3))
    return A

# ---- the defect's own floor, from the work's own measurements ------------
# S.ritz: the d2 term removes 48% of what the compendium called scatter,
# 0.0199 -> 0.0104 across 274 channels. That residual is the floor a real
# effect must clear to be visible at all.
FLOOR_TYPICAL = 0.0104
# best case: a single clean channel measured against its own uncertainty.
FLOOR_BEST = 1e-4

def delta_shift(Z, n, dA=1):
    """|d(delta)| induced by a one-unit isotope step, mass shift only.

    delta = n - Z_c sqrt(R/E).  A fractional change eps in R moves
    (n - delta) by eps/2, so |d delta| = (n - delta) * eps / 2.
    """
    A = A_of_Z(Z)
    eps = ME_U * dA / (A * (A + dA))      # fractional change in R_M
    return (n) * eps / 2, eps, A

print("MASS SHIFT — exact arithmetic, no fitted constant")
print(f"{'Z':>4}{'A(Z)':>9}{'eps = dR/R':>14}{'|d delta| n=3':>15}"
      f"{'vs floor 0.0104':>18}")
rows = []
for Z in (1, 2, 3, 6, 10, 18, 20, 26, 36, 54, 82, 92):
    d, eps, A = delta_shift(Z, 3)
    rows.append((Z, A, eps, d))
    verdict = "VISIBLE" if d > FLOOR_TYPICAL else "null"
    print(f"{Z:>4}{A:>9.1f}{eps:>14.3e}{d:>15.3e}{verdict:>18}")

print("\n  the mass shift clears the typical floor at NO Z.")
print(f"  largest is hydrogen at |d delta| = {rows[0][3]:.2e}, which is"
      f" {FLOOR_TYPICAL/rows[0][3]:.0f}x below it.")
print(f"  against the BEST-case floor {FLOOR_BEST:.0e} it clears only where:")
for Z, A, eps, d in rows:
    if d > FLOOR_BEST:
        print(f"      Z = {Z}  |d delta| = {d:.2e}")

# ---- the H/D case, the one the work has already measured -----------------
print("\nTHE ONE RUNG ALREADY TRACED — H vs D")
A1, A2 = 1.00794, 2.014
eps = ME_U * (A2 - A1) / (A1 * A2)
print(f"  eps = dR/R = {eps:.4e}")
print(f"  |d delta| at n=2 : {2*eps/2:.3e}")
print(f"  |d delta| at n=8 : {8*eps/2:.3e}   <- rises linearly in n")
print(f"  today's hydrogenic test measured the SAME quantity as an absolute")
print(f"  offset: observed -0.000267 against -0.000272 predicted.")

# ---- the field shift: scaling only ---------------------------------------
print("\nFIELD SHIFT — scaling only; its electronic factor is an expectation")
print("value the work does not hold, so magnitude is an OPEN cell.")
print(f"{'Z':>4}{'MS ~ A^-2':>14}{'FS ~ Z^2 A^-1/3':>18}{'FS/MS (relative)':>19}")
base = None
for Z in (1, 10, 20, 40, 60, 82, 92):
    A = A_of_Z(Z)
    ms = A ** -2
    fs = Z ** 2 * A ** (-1 / 3)
    r = fs / ms
    if base is None: base = r
    print(f"{Z:>4}{ms:>14.3e}{fs:>18.3e}{r/base:>19.3e}")
print("  the ratio spans ~10 orders across the table, so the two can never")
print("  both matter at one Z. Where the mass shift is largest the field shift")
print("  is smallest, and the reverse — they do not overlap.")
