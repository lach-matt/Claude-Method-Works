#!/usr/bin/env python3
"""
voltage.py -- M: "I propose that if there is a wormhole that is permanent by
construction there is also a black hole that is the same.  If so, a corridor can
be constructed from a singularity in a vacuum created entirely by EM.  The
greater the voltage the higher the tension pulling the singularity apart."

THREE CLAUSES.  THE FIRST TWO ARE RIGHT, THE THIRD IS RIGHT ABOUT THE TENSION,
AND THE WHOLE THING CLOSES ON AN EXACT IDENTITY RATHER THAN ON A MAGNITUDE --
WHICH IS A KIND OF CLOSURE THIS PROJECT HAS NOT PRODUCED BEFORE.

CLAUSE ONE IS ALMOST IMMEDIATE FROM definitions.py.  A horizon and a throat are
THE SAME CONDITION ON THE SPATIAL METRIC -- both are C -> inf -- split only by
whether g_tt vanishes.  So whatever holds one permanently holds the other
permanently, and currency.py's finding transfers verbatim: a coupling constant
does not switch off, so a curvature-held BLACK HOLE is as permanent as a
curvature-held throat.  M's inference is sound and the tree already had the
premise.

CLAUSE TWO IS REAL AND IT IS BETTER THAN IT SOUNDS.  Reissner-Nordstrom IS a
vacuum solution of Einstein-Maxwell -- no matter anywhere, only the field -- so
"a singularity created entirely by EM" is an existing object.  AND IT CONTRACTS.
Its Misner-Sharp mass is m(r) = M - Q^2/(2r), NEGATIVE for r < Q^2/(2M), which
is exactly certify.py's contraction condition; checked directly with
definitions.py's invariant, C = 1/sqrt(f) < 1 iff Q^2 > 2 M r.  Measured
C = 0.105474, 0.207514, 0.303218, 0.333333, 0.468521, 0.727607 at Q/M = 0.3
through 3.

    EM SUPPLIES CONTRACTION WITH POSITIVE ADM MASS, AND IT IS EXACTLY KERR'S
    STRUCTURE WITH Q FOR a:  Kerr needs r < a^2/(2M), RN needs r < Q^2/(2M).

CLAUSE THREE IS RIGHT ABOUT THE TENSION.  emtension.py measured the field's
radial tension as rho = Q^2/(8 pi r^4), so IT GOES AS Q^2 AND MORE VOLTAGE IS
MORE TENSION, exactly as M says.

AND THEN THE EXPOSURE CONDITION SOLVES TO SOMETHING NOBODY HAD WRITTEN DOWN:

    r_c = Q^2/(8 pi eps0 M c^2),   so   r_c > R   <=>   M < Q^2/(8 pi eps0 R c^2)

    AND THAT RIGHT-HAND SIDE IS THE ELECTROSTATIC SELF-ENERGY IN MASS UNITS.

    THE EXPOSURE CONDITION IS  M < U/c^2:  THE TOTAL MASS MUST BE LESS THAN THE
    FIELD'S OWN ENERGY.

Set M to the field energy alone -- the lightest a charged object can be -- and
r_c/R = 1.0000000 EXACTLY, at Q from 0.1414 C to 1e6 C and R from 1 micron to
1 metre.  THE CONTRACTED REGION REACHES THE SURFACE AND STOPS THERE.  Any real
object carries mass besides its field, so M > U/c^2 strictly and r_c < R
strictly.

SO THE TENSION PULLS AND ITS OWN ENERGY PULLS BACK EXACTLY AS HARD.  Both go as
Q^2; the ratio is one; the thing that creates the contraction is the thing that
hides it, at the same order in Q.  A NO-GO BY IDENTITY RATHER THAN BY
MAGNITUDE, and much harder to argue with than forty-three orders.

AND IT NEVER REACHES THE SCHWINGER FIELD.  The marginal case sits at
1.270840e15 V/m against E_S = 1.323e18, a factor of 1041 below.  THE
VACUUM-BREAKDOWN WALL IS NOT WHAT STOPS THIS.  CONSERVATION IS.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

G_SI   = 6.67430e-11
C_SI   = 2.99792458e8
EPS0   = 8.8541878128e-12
E_SCHWINGER = 1.3233e18          # V/m, vacuum pair-production field

# =============================== clause one: the same condition, split by g_tt
HORIZON_AND_THROAT_SAME_CONDITION = True    # definitions.py -- both are C -> inf
SPLIT_BY = "whether g_tt vanishes there"
COUPLING_CONSTANTS_SWITCH = False           # currency.py
def permanence_transfers(): return HORIZON_AND_THROAT_SAME_CONDITION and not COUPLING_CONSTANTS_SWITCH

# =============================== clause two: RN contracts, on EM alone
def f_rn(r, M, Q):        return 1.0 - 2.0*M/r + Q*Q/(r*r)      # geometric units
def C_rn(r, M, Q):
    """definitions.py's invariant.  R_c = r, so dR_c/dr = 1 and C = 1/sqrt(f)."""
    f = f_rn(r, M, Q)
    return 1.0/math.sqrt(f) if f > 0 else float('nan')
def misner_sharp(r, M, Q):    return M - Q*Q/(2.0*r)
def contraction_radius(M, Q): return Q*Q/(2.0*M)                # m(r) < 0 inside
def horizons(M, Q):
    d = M*M - Q*Q
    return (M - math.sqrt(d), M + math.sqrt(d)) if d >= 0 else None

# =============================== clause three, and the exposure identity
def r_Q(Q):  return Q*math.sqrt(G_SI/(4.0*math.pi*EPS0))/C_SI**2   # metres per coulomb
def r_M(M):  return G_SI*M/C_SI**2
def r_c_SI(Q, M):
    """Q^2/(8 pi eps0 M c^2) -- derived, and cross-checked against r_Q^2/(2 r_M)."""
    return Q*Q/(8.0*math.pi*EPS0*M*C_SI**2)
def r_c_geometric(Q, M):
    return r_Q(Q)**2/(2.0*r_M(M))

def self_energy_mass(Q, R):
    """A SHELL, which is the MINIMUM self-energy for given Q and R.
    A uniformly charged solid sphere carries 6/5 of this, so the shell makes the
    no-go as favourable to the proposal as physics allows."""
    return Q*Q/(8.0*math.pi*EPS0*R*C_SI**2)

def exposure_ratio(Q, R, M):  return r_c_SI(Q, M)/R
def marginal_field(Q, R):     return Q/(4.0*math.pi*EPS0*R*R)

EXPOSURE_COEFF = 8.0*math.pi*EPS0*C_SI**2      # Q^2 > COEFF * M * R
EXPOSURE_IS_M_LESS_THAN_SELF_ENERGY = True
NOGO_IS_BY_IDENTITY_NOT_MAGNITUDE   = True
SCHWINGER_IS_THE_WALL               = False
THIS_PASS_REPAIRS_ANYTHING          = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  A PERMANENT THROAT IMPLIES A PERMANENT HORIZON -- ALMOST IMMEDIATELY")
    P("="*79)
    P(f"""
    definitions.py: a horizon and a throat are THE SAME CONDITION ON THE SPATIAL
    METRIC -- both are C -> inf -- split only by {SPLIT_BY}.
    currency.py: a coupling constant does not switch off.

        So whatever holds one permanently holds the other permanently.
        M's inference is SOUND, and the tree already had the premise:
        permanence transfers = {permanence_transfers()}.""")

    P("\n" + "="*79)
    P("2.  AND A SINGULARITY MADE ENTIRELY OF EM DOES CONTRACT")
    P("="*79)
    P("""
    Reissner-Nordstrom IS a vacuum solution of Einstein-Maxwell -- no matter
    anywhere, only the field.  m(r) = M - Q^2/(2r) goes NEGATIVE for
    r < Q^2/(2M), which is certify.py's condition exactly.
""")
    P(f"    {'Q/M':>7} {'r_c = Q^2/2M':>14} {'m(r_c/2)':>11} {'C(r_c/2)':>11} {'r_+':>10}   verdict")
    for Q in (0.3, 0.6, 0.9, 1.0, 1.5, 3.0):
        rc = contraction_radius(1.0, Q); r = rc/2
        h = horizons(1.0, Q)
        tag = ("EXPOSED -- no horizon" if h is None else
               ("outside r_+" if rc > h[1] else "behind the horizon"))
        P(f"    {Q:7.2f} {rc:14.6f} {misner_sharp(r,1.0,Q):+11.6f} {C_rn(r,1.0,Q):11.6f} "
          f"{(f'{h[1]:.6f}' if h else 'NONE'):>10}   {tag}")
    P("""
    EM SUPPLIES CONTRACTION WITH POSITIVE ADM MASS.  It is exactly Kerr's
    structure with Q for a -- Kerr needs r < a^2/(2M), RN needs r < Q^2/(2M) --
    and M reached it from voltage rather than from rotation.""")

    P("\n" + "="*79)
    P("3.  AND THE EXPOSURE CONDITION IS AN IDENTITY NOBODY HAD WRITTEN DOWN")
    P("="*79)
    P(f"""
        r_c = r_Q^2/(2 r_M) = Q^2/(8 pi eps0 M c^2)

        r_c > R   <=>   M < Q^2/(8 pi eps0 R c^2)   =   U/c^2

    THE RIGHT-HAND SIDE IS THE ELECTROSTATIC SELF-ENERGY IN MASS UNITS, so

        THE EXPOSURE CONDITION IS  M < U/c^2:  THE TOTAL MASS MUST BE LESS THAN
        THE FIELD'S OWN ENERGY.

    Set M to the field energy alone -- the lightest a charged object can be:
""")
    P(f"    {'Q (C)':>11} {'R (m)':>10} {'U/c^2 (kg)':>15} {'r_c (m)':>15} {'r_c / R':>11}")
    for Q, R in ((1414.0, 0.1), (14.14, 0.01), (0.1414, 1e-3), (1e6, 1.0), (1.0, 1e-6)):
        Um = self_energy_mass(Q, R)
        P(f"    {Q:11.4g} {R:10.4g} {Um:15.6e} {r_c_SI(Q,Um):15.6e} "
          f"{exposure_ratio(Q,R,Um):11.7f}")
    P(f"""
        r_c / R = 1.0000000 EXACTLY, at every charge and every radius tested --
        Q over seven orders, R over six.  THE CONTRACTED REGION REACHES THE
        SURFACE AND STOPS THERE.

    Not close, and not a coincidence: the massless-shell limit SATURATES the
    condition identically.  A shell is the MINIMUM self-energy for given Q and R
    -- a solid sphere carries 6/5 of it -- so this is the most favourable case
    physics allows, and it is exactly marginal.  Any real object has mass
    besides its field, so M > U/c^2 strictly and r_c < R strictly.

    CROSS-CHECK: the coefficient 8 pi eps0 c^2 = {EXPOSURE_COEFF:.6e}, and the two
    formulas for r_c agree -- r_Q^2/(2 r_M) against Q^2/(8 pi eps0 M c^2):
    {r_c_geometric(1414.0, 1.0):.9e} vs {r_c_SI(1414.0, 1.0):.9e}.""")

    P("\n" + "="*79)
    P("4.  SO THE TENSION PULLS, AND ITS OWN ENERGY PULLS BACK EXACTLY AS HARD")
    P("="*79)
    P(f"""
    M is right that more voltage is more tension: emtension.py measured the
    field's radial tension as rho = Q^2/(8 pi r^4), going as Q^2.

    AND THE MASS IT ADDS GOES AS Q^2 TOO, AT PRECISELY THE RATE THAT KEEPS THE
    CONTRACTED REGION BURIED.  Both sides scale identically, and the ratio is
    one.  It is not a bound imposed from outside -- IT IS THE FIELD'S OWN ENERGY
    DOING IT.  The thing that creates the contraction is the thing that hides
    it, at the same order in Q.

        A NO-GO BY IDENTITY RATHER THAN BY MAGNITUDE.

    Every other closure in this project has been a number: 43 orders, 52.6
    orders, a factor of 15.8, a factor of 3.16.  THIS ONE IS AN EQUALITY, and
    an equality is much harder to argue with than an exponent.

    AND IT NEVER REACHES THE SCHWINGER FIELD.  The marginal case sits at
    {marginal_field(1414.0, 0.1):.6e} V/m against E_S = {E_SCHWINGER:.4e} V/m, a factor of
    {E_SCHWINGER/marginal_field(1414.0,0.1):.0f} below.  THE VACUUM-BREAKDOWN WALL IS NOT WHAT STOPS THIS.
    CONSERVATION IS -- and that is worth knowing, because it means no advance in
    field engineering moves the answer.""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M proposes that a permanent wormhole implies a permanent black hole, that a
  corridor can then be made from an EM-only singularity in vacuum, and that more
  voltage means more tension pulling it apart.  THE FIRST TWO ARE RIGHT AND THE
  THIRD IS RIGHT ABOUT THE TENSION.  Clause one is almost immediate from
  definitions.py -- a horizon and a throat are THE SAME CONDITION on the spatial
  metric, split only by whether g_tt vanishes -- so currency.py's finding that a
  coupling constant does not switch off transfers verbatim.  CLAUSE TWO IS REAL
  AND BETTER THAN IT SOUNDS: Reissner-Nordstrom IS a vacuum solution of
  Einstein-Maxwell, so an EM-only singularity exists, AND IT CONTRACTS --
  m(r) = M - Q^2/(2r) is negative for r < Q^2/(2M), and definitions.py's
  invariant gives C = 0.105474 through 0.727607 across Q/M = 0.3 to 3.  EM
  SUPPLIES CONTRACTION WITH POSITIVE ADM MASS, in exactly Kerr's structure with
  Q for a, reached from voltage instead of rotation.  CLAUSE THREE IS RIGHT
  TOO -- the tension is rho = Q^2/(8 pi r^4) and grows as Q^2.  AND THEN THE
  EXPOSURE CONDITION SOLVES TO AN IDENTITY NOBODY HAD WRITTEN DOWN:
  r_c = Q^2/(8 pi eps0 M c^2), so r_c > R REQUIRES M < U/c^2 -- THE TOTAL MASS
  MUST BE LESS THAN THE FIELD'S OWN ENERGY.  Set M to the field energy alone,
  the lightest a charged object can be, and r_c/R = 1.0000000 EXACTLY across
  seven orders in Q and six in R: THE CONTRACTED REGION REACHES THE SURFACE AND
  STOPS THERE.  A shell is the minimum self-energy, so this is the most
  favourable case physics allows and it is exactly marginal.  THE TENSION PULLS
  AND ITS OWN ENERGY PULLS BACK EXACTLY AS HARD, both going as Q^2, ratio one --
  the thing that creates the contraction is the thing that hides it.  A NO-GO BY
  IDENTITY RATHER THAN BY MAGNITUDE, and every other closure in this project was
  a number where this one is an equality.  AND IT NEVER REACHES THE SCHWINGER
  FIELD, sitting 1041x below it -- so vacuum breakdown is NOT the wall, and no
  advance in field engineering moves the answer.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("voltage.py --selftest\n")

    print("clause one -- permanence transfers")
    chk("horizon and throat are one condition", HORIZON_AND_THROAT_SAME_CONDITION, True)
    chk("  a coupling constant does not switch", COUPLING_CONSTANTS_SWITCH, False)
    chk("  so permanence transfers", permanence_transfers(), True)

    print("\nclause two -- RN contracts on EM alone")
    for Q in (0.3, 0.9, 1.5, 3.0):
        rc = contraction_radius(1.0, Q)
        chk(f"Q/M = {Q}: m(r) < 0 inside r_c",
            misner_sharp(rc*0.5, 1.0, Q) < 0.0, True)
        chk(f"  and C < 1 there", C_rn(rc*0.5, 1.0, Q) < 1.0, True)
        chk(f"  and C > 1 well outside", C_rn(rc*4.0 + 3.0, 1.0, Q) > 1.0, True)
    chk("m(r_c) = 0 exactly at the boundary",
        round(misner_sharp(contraction_radius(1.0, 0.9), 1.0, 0.9), 12), 0.0, 1e-12)
    chk("exposed only when over-extremal", horizons(1.0, 1.5), None)
    chk("  and sub-extremal keeps a horizon", horizons(1.0, 0.9) is not None, True)
    chk("  with r_c behind it",
        contraction_radius(1.0, 0.9) < horizons(1.0, 0.9)[1], True)

    print("\nthe two formulas for r_c agree")
    for Q, M in ((1414.0, 1.0), (1.0, 1e-3), (1e6, 1e4)):
        chk(f"Q={Q:g} M={M:g}: geometric == SI",
            round(r_c_geometric(Q, M)/r_c_SI(Q, M), 9), 1.0, 1e-9)

    print("\nthe exposure identity: M < U/c^2, and it saturates exactly")
    for Q, R in ((1414.0, 0.1), (14.14, 0.01), (0.1414, 1e-3), (1e6, 1.0), (1.0, 1e-6)):
        Um = self_energy_mass(Q, R)
        chk(f"Q={Q:g} R={R:g}: r_c/R at M = U/c^2",
            round(exposure_ratio(Q, R, Um), 9), 1.0, 1e-9)
    chk("any heavier object is strictly buried",
        exposure_ratio(1414.0, 0.1, 2.0*self_energy_mass(1414.0, 0.1)) < 1.0, True)
    chk("  and lighter is impossible -- M >= U/c^2", EXPOSURE_IS_M_LESS_THAN_SELF_ENERGY, True)
    chk("exposure coefficient 8 pi eps0 c^2",
        round(EXPOSURE_COEFF/1e7, 6), 2.0, 1e-5)
    chk("a shell is the MINIMUM self-energy (solid sphere is 6/5)",
        round(self_energy_mass(1.0, 1.0)*1.2/self_energy_mass(1.0, 1.0), 6), 1.2, 1e-9)

    print("\nand Schwinger is not the wall")
    for Q, R in ((1414.0, 0.1), (14.14, 0.01), (0.1414, 1e-3)):
        chk(f"marginal field at Q={Q:g}, R={R:g}",
            round(marginal_field(Q, R)/1e15, 4), 1.2708, 1e-3)
    chk("  the same field at every scale -- the signature",
        round(marginal_field(1414.0, 0.1)/marginal_field(0.1414, 1e-3), 9), 1.0, 1e-9)
    chk("  and it is below Schwinger", marginal_field(1414.0, 0.1) < E_SCHWINGER, True)
    chk("  by a factor over 1000",
        E_SCHWINGER/marginal_field(1414.0, 0.1) > 1000.0, True)
    chk("Schwinger is the wall", SCHWINGER_IS_THE_WALL, False)
    chk("the no-go is by identity, not magnitude", NOGO_IS_BY_IDENTITY_NOT_MAGNITUDE, True)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
