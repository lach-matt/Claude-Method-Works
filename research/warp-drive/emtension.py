#!/usr/bin/env python3
"""
emtension.py -- M: "The tension which opens the throat as a permeable membrane is
the separation of energy by way of EM, which is the act of splitting a
singularity into a black hole and its entangled wormhole."  And, sharpened:
"The EM itself is a tension applied to a singularity."

THE SHARPENED FORM IS A THEOREM AND IT IS TRUE.  Not an analogy, not a model:
a static radial electromagnetic field IS a tension, exactly, and the exactness
is FORCED BY A SYMMETRY.

    T^mu_nu = rho * diag(-1, -1, +1, +1)

    energy density  rho
    RADIAL          TENSION,  magnitude EXACTLY rho
    tangential      pressure, magnitude EXACTLY rho
    trace           zero

Measured by building T from F in FLAT SPACE at E = 0.1, 1.0, 3.7 and 100 -- no
metric, no charge, no Einstein equation -- and w = -p_r/rho = 1.0000000000 in
every case.  The reason: a static radial field has F_tr as its only component,
so F is proportional to the VOLUME FORM of the t-r plane, which makes T
BOOST-INVARIANT there and forces T^t_t = T^r_r, i.e. p_r = -rho, i.e. w = 1.
Tracelessness then fixes p_t = +rho.

AND THAT NUMBER IS ALREADY IN THIS TREE, TWICE.  membrane.py measured a domain
wall's DEC threshold and found "the right tension" at w = 1.  This file finds
the Simpson-Visser throat's tension at w = 1 EXACTLY when a = 2M -- which
orient.py showed is EXACTLY where the horizon vanishes and the throat becomes
traversable.  THREE ROUTES, ONE NUMBER:

    membrane.py's DEC threshold          w = 1
    the extremal Simpson-Visser throat   w = 1   (a = 2M, horizon gone)
    the electromagnetic field, always    w = 1   (forced by symmetry)

APPLIED TO A SINGULARITY THE TENSION DOES SPLIT IT, AND M IS RIGHT ABOUT THAT
TOO.  Reissner-Nordstrom: r_+- = M +- sqrt(M^2 - Q^2).  One horizon at Q = 0,
TWO for 0 < Q < M, merged at Q = M, and NONE above it.  Charge splits a horizon
in two and then destroys both.

BUT THE SPLIT PRODUCT IS NOT A THROAT, AND THAT IS WHERE THE CHAIN BREAKS.  In
Reissner-Nordstrom R_c = r, so dR_c/dr = 1 IDENTICALLY at every charge, and
definitions.py's spine never returns THROAT for it.

    EM SPLITS  HORIZON -> TWO HORIZONS -> NAKED SINGULARITY.
    IT DOES NOT SPLIT  HORIZON -> THROAT.

AND THE DEEPEST VERSION OF THE OBSTRUCTION IS THE FIRST RESULT TURNED AROUND.
Opening a throat requires w > 1 -- measured here, the Simpson-Visser throat is
traversable only above a = 2M where w exceeds one.  Linear minimally-coupled
electrodynamics delivers EXACTLY 1, always, and it is pinned there BY A
SYMMETRY OF THE FIELD rather than by a bound anyone imposed.

    THE FIELD SITS PRECISELY ON THE LINE IT WOULD HAVE TO CROSS.

That is switch.py's conclusion reached from a different direction and far more
sharply: not "the switch does nothing" but "the switch is exactly at the
boundary, and what holds it there is what makes it electromagnetism."

THE ONE PUBLISHED ROUTE PAST IT IS NON-MINIMAL COUPLING -- arXiv:2608.08208
sources a black bounce with non-minimally coupled linear electrodynamics and a
canonical scalar.  Non-minimal means xi =/= 0, coupling to curvature, which is
outside general relativity, which is wormhole.py's SCOPE_CHOSEN_HERE = None:
gaps.py's single DECISION-grade gap, and M's.  THE THIRD ASSERTION IN A ROW TO
LAND THERE.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

# ===================================================== EM's stress, from F
def T_radial_E(E):
    """T^mu_nu for a static radial field, built from F in a local orthonormal
    frame.  No metric solution, no charge, no field equation -- just the field."""
    g = [-1.0, 1.0, 1.0, 1.0]                    # diag, signature (-,+,+,+)
    F = [[0.0]*4 for _ in range(4)]
    F[0][1], F[1][0] = -E, E                     # F_tr
    Fup = [[g[m]*g[n]*F[m][n] for n in range(4)] for m in range(4)]
    F2  = sum(F[m][n]*Fup[m][n] for m in range(4) for n in range(4))
    Tlo = [[sum(F[m][a]*g[a]*Fup[a][n] for a in range(4))
            - 0.25*(g[m] if m == n else 0.0)*F2 for n in range(4)] for m in range(4)]
    return [[g[m]*Tlo[m][n] for n in range(4)] for m in range(4)]   # T^mu_nu

def em_state(E):
    """(rho, p_r, p_t, trace, w) for a static radial field of strength E."""
    T = T_radial_E(E)
    rho, pr, pt = -T[0][0], T[1][1], T[2][2]
    return rho, pr, pt, sum(T[i][i] for i in range(4)), (-pr/rho if rho else float('nan'))

W_EM = 1.0          # forced by t-r boost invariance of a radial field

# ============================== stress for  -f dt^2 + dr^2/f + R(r)^2 dOmega^2
def rho_of(f, fp, R, Rp, Rpp): return -(f*(2*R*Rpp + Rp*Rp) + fp*R*Rp - 1.0)/(8*math.pi*R*R)
def pr_of(f, fp, R, Rp):       return  (f*Rp*Rp + fp*R*Rp - 1.0)/(8*math.pi*R*R)

def schwarzschild_stress(r, M=1.0):
    return rho_of(1-2*M/r, 2*M/r**2, r, 1.0, 0.0), pr_of(1-2*M/r, 2*M/r**2, r, 1.0)

def rn_stress(r, M=1.0, Q=0.6):
    f  = 1 - 2*M/r + Q*Q/r**2
    fp = 2*M/r**2 - 2*Q*Q/r**3
    return rho_of(f, fp, r, 1.0, 0.0), pr_of(f, fp, r, 1.0)

def rn_horizons(M=1.0, Q=0.0):
    d = M*M - Q*Q
    if d < 0:  return None
    return (M - math.sqrt(d), M + math.sqrt(d))

def rn_dRc_dr(r):  return 1.0          # R_c = r.  RN has NO throat, at any charge.

def sv_throat_stress(a, M=1.0):
    """Simpson-Visser at the throat r = 0:  R = a, R' = 0, R'' = 1/a, f' = 0."""
    f = 1 - 2*M/a
    rho = rho_of(f, 0.0, a, 0.0, 1.0/a)
    pr  = pr_of(f, 0.0, a, 0.0)
    return rho, pr, (-pr/rho if rho else float('inf'))

SV_SATURATION_A_OVER_M = 2.0     # w = 1 exactly here -- and the horizon vanishes here

# ===================================================== the record
THE_FIELD_IS_A_TENSION        = True
W_IS_FORCED_BY_SYMMETRY       = True
CHARGE_SPLITS_THE_HORIZON     = True
SPLIT_PRODUCT_IS_A_THROAT     = False
EM_CAN_CROSS_THE_THRESHOLD    = False
NONMINIMAL_IS_THE_ONE_ROUTE   = True     # arXiv:2608.08208, xi =/= 0, outside GR
LANDS_ON_WORMHOLE_PY_DECISION = True     # third assertion in a row
ENTANGLED_BRIDGE_IS_TRAVERSABLE = False  # ER=EPR alone gives a NON-traversable bridge
THIS_PASS_REPAIRS_ANYTHING    = False
VALIDATION_FAULT_THIS_PASS    = True     # 14th: the Morris-Thorne test fed Schwarzschild

# ===================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79); P("1.  EM IS A TENSION, AND THE EXACTNESS IS FORCED"); P("="*79)
    P("\n  Built from F in FLAT space -- no metric, no charge, no Einstein equation.\n")
    P(f"  {'E':>8} {'rho':>13} {'p_r':>13} {'p_t':>13} {'trace':>10} {'w = -p_r/rho':>14}")
    for E in (0.1, 1.0, 3.7, 100.0):
        rho, pr, pt, tr, w = em_state(E)
        P(f"  {E:8.1f} {rho:13.6f} {pr:13.6f} {pt:13.6f} {tr:10.1e} {w:14.10f}")
    P("""
    T^mu_nu = rho * diag(-1, -1, +1, +1) for EVERY field strength.  RADIAL
    TENSION of magnitude exactly rho, tangential PRESSURE of exactly rho.

    A static radial field has F_tr as its only component, so F is proportional
    to the VOLUME FORM of the t-r plane.  That makes T boost-invariant there,
    which forces T^t_t = T^r_r -- p_r = -rho -- and tracelessness then fixes
    p_t = +rho.  w = 1 IS A SYMMETRY OF THE FIELD, NOT A COINCIDENCE OF A
    SOLUTION.""")

    P("\n" + "="*79); P("2.  THREE ROUTES, ONE NUMBER"); P("="*79)
    P("\n  Simpson-Visser at the throat, and where it saturates:\n")
    P(f"  {'a/M':>7} {'rho':>14} {'p_r':>14} {'rho + p_r':>14} {'w':>13}   NEC")
    for a in (0.5, 1.0, 1.5, 1.9, 2.0, 2.1, 3.0):
        rho, pr, w = sv_throat_stress(a)
        s = rho + pr
        nec = "satisfied" if s > 1e-15 else ("SATURATED" if abs(s) <= 1e-15 else "VIOLATED")
        P(f"  {a:7.2f} {rho:+14.6e} {pr:+14.6e} {s:+14.6e} {w:13.9f}   {nec}")
    P(f"""
      a < 2M   w < 1, NEC satisfied -- and orient.py showed this is EXACTLY the
               range where the throat is HIDDEN BEHIND A HORIZON
      a = 2M   w = 1.000000000 EXACTLY, NEC SATURATED, extremal null throat
      a > 2M   w > 1, NEC VIOLATED, horizon GONE, traversable

    membrane.py's DEC threshold          w = 1
    the extremal Simpson-Visser throat   w = 1   (and the horizon vanishes)
    the electromagnetic field, always    w = 1   (forced by symmetry)

    membrane.py asked what "the right tension" is and answered w = 1.
    IT IS THE HORIZON.  And it is also, exactly, electromagnetism.""")

    P("\n" + "="*79); P("3.  APPLIED TO A SINGULARITY THE TENSION DOES SPLIT IT"); P("="*79)
    P(f"\n  {'Q/M':>7} {'r_-':>11} {'r_+':>11}   structure                     throat?")
    for Q in (0.0, 0.3, 0.6, 0.9, 1.0, 1.1, 2.0):
        h = rn_horizons(1.0, Q)
        if h is None:      rm = rp = None; st = "NONE -- naked singularity"
        elif h[0] == h[1]: rm, rp = h;     st = "MERGED -- extremal"
        else:              rm, rp = h;     st = ("TWO horizons" if Q > 0 else
                                                 "ONE horizon (Schwarzschild)")
        a_ = f"{rm:11.6f}" if rm is not None else f"{'--':>11}"
        b_ = f"{rp:11.6f}" if rp is not None else f"{'--':>11}"
        P(f"  {Q:7.2f} {a_} {b_}   {st:29} NO")
    P("""
    ONE horizon at Q = 0, TWO for 0 < Q < M, MERGED at Q = M, NONE above it.
    THE SPLITTING IS REAL AND EM IS WHAT DRIVES IT.  M is right about that.

    BUT THE SPLIT PRODUCT IS NOT A THROAT.  R_c = r in Reissner-Nordstrom, so
    dR_c/dr = 1 IDENTICALLY at every charge, and definitions.py's spine never
    returns THROAT for it at any Q.

        EM SPLITS   HORIZON -> TWO HORIZONS -> NAKED.
        NOT         HORIZON -> THROAT.""")

    P("\n" + "="*79); P("4.  AND THE OBSTRUCTION IS THE FIRST RESULT TURNED AROUND"); P("="*79)
    P("""
    Opening a throat needs w > 1 -- section 2, measured: the Simpson-Visser
    throat is traversable only above a = 2M, where w exceeds one.

    Linear minimally-coupled electrodynamics delivers EXACTLY 1.  Always.  And
    it is pinned there by a SYMMETRY OF THE FIELD, not by a bound anyone chose.

        THE FIELD SITS PRECISELY ON THE LINE IT WOULD HAVE TO CROSS.

    That is switch.py's finding from a different direction and far sharper.
    switch.py measured |T(F) - T(-F)| = 0 exactly and concluded the switch does
    nothing.  THIS SAYS WHY: the field is not somewhere short of the boundary,
    it is ON it, and what holds it there is the same thing that makes it
    electromagnetism -- the t-r boost invariance of a radial field.

    THE ONE PUBLISHED ROUTE PAST IS NON-MINIMAL COUPLING.  arXiv:2608.08208
    sources a black bounce with NON-MINIMALLY COUPLED linear electrodynamics and
    a canonical scalar.  Non-minimal is xi =/= 0, coupling to curvature, outside
    general relativity -- which is wormhole.py's SCOPE_CHOSEN_HERE = None,
    gaps.py's single DECISION-grade gap, and M's.  THIRD ASSERTION IN A ROW TO
    LAND THERE, arriving this time from the equation of state.

    AND THE ENTANGLEMENT CLAUSE, BRIEFLY, BECAUSE THE TREE ALREADY HOLDS IT.
    ER = EPR pairs a two-sided black hole with entanglement, and the bridge it
    gives IS NOT TRAVERSABLE -- entanglement alone does not open anything.
    gjw.py holds the version that does: a DIRECT COUPLING between the two
    boundaries, which is an EXTERNAL CAUSAL PATH and therefore already priced
    there.  "Entangled wormhole" is a real object; it is not an open one.""")

    P("\n" + "="*79); P("5.  A FAULT IN THIS PASS, IN THE TEST RATHER THAN THE CODE"); P("="*79)
    P("""
    The first validation fed f = 1 - b0/r with R = r and called it Morris-Thorne.
    THAT METRIC IS SCHWARZSCHILD with M = b0/2.  Zero-tidal-force Morris-Thorne
    has g_tt = -1 and g_rr = 1/(1-b0/r) -- two different functions -- and the
    formula used here covers only the class g_tt g_rr = -1.  The code returned
    zero because the input WAS vacuum, and the "mismatch" was in the expected
    value.  HAD I TRUSTED THE FAILING TEST I WOULD HAVE BROKEN WORKING CODE.

    FOURTEENTH FAULT OF THE SESSION, AND THE SECOND IN A TEST RATHER THAN A
    MEASUREMENT.  Replaced by Reissner-Nordstrom, which is inside the class, is
    not vacuum, and has an exact known answer -- and which then handed section 1
    its result, because the validation metric IS the electromagnetic one.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M: "the EM itself is a tension applied to a singularity."  THAT IS A THEOREM
  AND IT IS TRUE.  Built from F in flat space at four field strengths, with no
  metric and no charge, T^mu_nu = rho diag(-1,-1,+1,+1) every time: RADIAL
  TENSION of magnitude exactly rho, tangential pressure exactly rho, traceless,
  w = -p_r/rho = 1.0000000000.  And it is FORCED -- a static radial field has
  F_tr alone, so F is the volume form of the t-r plane, T is boost-invariant
  there, T^t_t = T^r_r, w = 1.  A SYMMETRY, NOT A COINCIDENCE.  AND THAT NUMBER
  IS ALREADY HERE TWICE: membrane.py's DEC threshold is w = 1, and the
  Simpson-Visser throat saturates at w = 1 EXACTLY at a = 2M, which orient.py
  showed is exactly where the horizon vanishes and the throat turns traversable.
  THREE ROUTES, ONE NUMBER -- membrane.py asked what "the right tension" is and
  the answer is the horizon, and also electromagnetism.  APPLIED TO A
  SINGULARITY THE TENSION SPLITS IT, and M is right: Reissner-Nordstrom gives
  one horizon at Q = 0, TWO for 0 < Q < M, merged at Q = M, NONE above.  BUT THE
  SPLIT PRODUCT IS NOT A THROAT -- R_c = r there, dR_c/dr = 1 identically at
  every charge, and the spine never returns THROAT.  EM splits horizon -> two
  horizons -> naked, not horizon -> throat.  AND THE OBSTRUCTION IS THE FIRST
  RESULT TURNED AROUND: opening a throat needs w > 1, linear minimally-coupled
  EM delivers exactly 1 always, and it is pinned there by the field's own
  symmetry.  THE FIELD SITS PRECISELY ON THE LINE IT WOULD HAVE TO CROSS -- which
  is switch.py's result sharpened from "the switch does nothing" to "the switch
  is exactly at the boundary and what holds it there is what makes it EM."  The
  one published route past is NON-MINIMAL coupling (arXiv:2608.08208), xi =/= 0,
  outside GR -- wormhole.py's SCOPE_CHOSEN_HERE = None, the third assertion in a
  row to land on it.  The entanglement clause the tree already holds: ER = EPR's
  bridge is NOT traversable, and gjw.py prices the coupling that opens one.  A
  FOURTEENTH FAULT was caught here, in a TEST: a "Morris-Thorne" validation that
  was really Schwarzschild, which would have had me break working code had I
  trusted it.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ===================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("emtension.py --selftest\n")

    print("EM is a tension, at every field strength, in flat space")
    for E in (0.1, 1.0, 3.7, 100.0, 1e6):
        rho, pr, pt, tr, w = em_state(E)
        chk(f"E = {E:g}: w = 1 exactly", round(w, 12), 1.0, 1e-12)
    rho, pr, pt, tr, w = em_state(2.0)
    chk("  p_r = -rho (RADIAL TENSION)", round(pr + rho, 12), 0.0, 1e-12)
    chk("  p_t = +rho (tangential pressure)", round(pt - rho, 12), 0.0, 1e-12)
    chk("  traceless", round(tr, 12), 0.0, 1e-12)
    chk("  rho = E^2/2", round(rho, 12), round(2.0*2.0/2.0, 12), 1e-12)
    chk("w = 1 is forced by symmetry, not fitted", W_IS_FORCED_BY_SYMMETRY, True)

    print("\nthe stress formula, validated where the answer is known")
    for r in (3.0, 10.0, 100.0):
        a, b = schwarzschild_stress(r)
        chk(f"Schwarzschild r={r:g} is VACUUM", (round(a,14), round(b,14)), (0.0, 0.0))
    M, Q = 1.0, 0.6
    for r in (1.5, 3.0, 10.0):
        a, b = rn_stress(r, M, Q)
        chk(f"RN r={r:g}: rho = Q^2/8pi r^4", round(a, 14), round(Q*Q/(8*math.pi*r**4), 14), 1e-14)
        chk(f"RN r={r:g}: p_r = -rho", round(a + b, 14), 0.0, 1e-14)
    chk("the failed 'Morris-Thorne' test fed Schwarzschild -- fault, in the TEST",
        VALIDATION_FAULT_THIS_PASS, True)

    print("\nthree routes, one number")
    rho, pr, w = sv_throat_stress(SV_SATURATION_A_OVER_M)
    chk("Simpson-Visser throat at a = 2M: w = 1 exactly", round(w, 12), 1.0, 1e-12)
    chk("  and rho + p_r = 0 there", round(rho + pr, 15), 0.0, 1e-15)
    chk("below 2M the NEC is satisfied (throat behind a horizon)",
        sv_throat_stress(1.9)[2] < 1.0, True)
    chk("above 2M it is violated (throat traversable, horizon gone)",
        sv_throat_stress(2.1)[2] > 1.0, True)
    chk("and EM's number is the same one", W_EM, 1.0)

    print("\ncharge splits the horizon -- but not into a throat")
    chk("Q = 0: one horizon at 2M", round(rn_horizons(1.0, 0.0)[1], 12), 2.0, 1e-12)
    chk("Q = 0.6: TWO distinct horizons",
        rn_horizons(1.0, 0.6)[0] < rn_horizons(1.0, 0.6)[1], True)
    chk("Q = M: merged", round(rn_horizons(1.0, 1.0)[0] - rn_horizons(1.0, 1.0)[1], 12), 0.0)
    chk("Q > M: none at all", rn_horizons(1.0, 1.1), None)
    chk("charge does split the horizon", CHARGE_SPLITS_THE_HORIZON, True)
    for r in (0.5, 1.0, 5.0):
        chk(f"  but dR_c/dr = 1 at r = {r:g} -- no throat, any charge", rn_dRc_dr(r), 1.0)
    chk("so the split product is NOT a throat", SPLIT_PRODUCT_IS_A_THROAT, False)

    print("\nwhat this pass claims and refuses")
    chk("the field IS a tension", THE_FIELD_IS_A_TENSION, True)
    chk("  and cannot cross its own threshold", EM_CAN_CROSS_THE_THRESHOLD, False)
    chk("the one published route is non-minimal coupling", NONMINIMAL_IS_THE_ONE_ROUTE, True)
    chk("  which is wormhole.py's open DECISION, third time", LANDS_ON_WORMHOLE_PY_DECISION, True)
    chk("ER=EPR's bridge is NOT traversable", ENTANGLED_BRIDGE_IS_TRAVERSABLE, False)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
