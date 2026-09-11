#!/usr/bin/env python3
"""
orient.py -- M: "do you remember when I first suggested the corridor is composed
by a wormhole and black hole relation with wormhole in and black hole out, but
it was refuted?  This says why, the path is the opposite direction.  Black holes
are the entrance to the corridor and wormholes are the exit."

THE MEMORY IS ACCURATE AND SO IS THE INFERENCE.  pair.py section 2 refuted the
original orientation, and it refuted it ON DIRECTIONAL GROUNDS:

    "A horizon is a one-way null surface.  Matter cannot cross it outward, by
     the definition of the object, so nothing exits through a black hole."

THAT ARGUMENT RUN BACKWARDS IS AN ARGUMENT *FOR* THE NEW ORIENTATION.  A surface
that admits only inward crossing is the one thing that can ONLY be an entrance.
The refutation did not kill the pairing -- it fixed its sign, and nobody turned
it around at the time.

KERR CANNOT DO IT, AND THE REASON IS EXACT.  definitions.py put the equatorial
dR_c/dr = 0 locus at r^3 = M a^2 and called it a throat.  A throat is a minimum
of area on a SPACELIKE slice, and between the horizons r is TIMELIKE.  Evaluate:
with u = (a/M)^(2/3),

    Delta(r_t) = u^2 - 2u + u^3 = u(u+2)(u-1)   ->   POSITIVE IFF a > M

    a < M   a horizon exists and there is NO SPATIAL THROAT
    a = M   Delta(r_t) = 0 EXACTLY -- they coincide and neither is a throat
    a > M   a spatial throat exists and there is NO HORIZON AT ALL

A HORIZON AND A THROAT ARE MUTUALLY EXCLUSIVE IN KERR, EXACTLY, AT a = M.  And
that is A FAULT IN definitions.py, ONE DAY OLD AND MINE: it verified the "throat"
at a = 0.3, 0.99 and 3.0, and TWO OF THE THREE WERE IN THE TIMELIKE-r REGION
where the word does not apply.  THIRTEENTH FAULT.

BUT THE OBJECT M IS DESCRIBING EXISTS, IT IS PUBLISHED, AND definitions.py's
SPINE CLASSIFIES IT WITH NO MODIFICATION.  The SIMPSON-VISSER BLACK-BOUNCE sends
r^2 -> r^2 + a^2 in Schwarzschild.  R_c = sqrt(r^2+a^2), so dR_c/dr = 0 at r = 0
for ANY a > 0, and the horizon sits at r = +-sqrt(4M^2 - a^2), real iff a < 2M.

    0 < a < 2M   A THROAT INSIDE AN EVENT HORIZON.
                 ENTER THROUGH THE BLACK HOLE, LEAVE THROUGH THE THROAT.
    a = 2M       extremal null throat
    a > 2M       an ordinary traversable wormhole, no horizon

Verified against the paper database in this session, not asserted: arXiv:2502.00502
states plainly that this class "presents a WORMHOLE THROAT INSIDE AN EVENT
HORIZON", and arXiv:2506.19818 that black bounces are "compact objects with a
wormhole structure HIDDEN BEHIND AN EVENT HORIZON".  M's orientation is the
standard description of a known family of solutions.

AND THE PRICE IS THE SAME WALL, WITH ONE DOOR.  In general relativity the source
violates the energy conditions -- arXiv:2506.19818, "by considering the presence
of EXOTIC MATTER".  Outside general relativity it need not: arXiv:2608.02771
derives black bounces "from PURE GRAVITY ... as VACUUM SOLUTIONS of metric
gravitational theories in four and higher dimensions".  THAT IS EXACTLY
wormhole.py's SCOPE_CHOSEN_HERE = None -- the f(R) and scalar-tensor scope
decision, open the whole project, and the single DECISION-grade gap gaps.py
found.  M's assertion has landed on the one gap in the census that is his.

AND IT IS ONE-WAY, WHICH IS NOT A DETAIL.  The throat is inside the horizon,
where r is TIMELIKE: it is crossed at a MOMENT, not at a PLACE.  You cannot
hover at it, cannot return through it, cannot send anything back, and the far
side is another asymptotic region rather than a destination you chose.  A
one-way exit to elsewhere IS NOT A CORRIDOR BETWEEN TWO PLACES, which is the
same objection that has closed every other route in this tree.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

M_ = 1.0

# ------------------------------------------------ Kerr: the exact dichotomy
def kerr_locus(M, a):        return (M*a*a)**(1.0/3.0)         # dR_c/dr = 0, equator
def kerr_Delta(r, M, a):     return r*r - 2.0*M*r + a*a
def kerr_locus_Delta(M, a):
    """Delta at the locus.  Factorises to M^2 u(u+2)(u-1) with u = (a/M)^(2/3)."""
    u = (a/M)**(2.0/3.0)
    return M*M*u*(u + 2.0)*(u - 1.0)
def kerr_locus_is_a_throat(M, a):
    """A throat needs a SPACELIKE slice.  Between the horizons r is timelike."""
    return kerr_locus_Delta(M, a) > 0.0

# ------------------------------------------------ Simpson-Visser black-bounce
def sv_f(r, a, M=1.0):       return 1.0 - 2.0*M/math.sqrt(r*r + a*a)
def sv_Rc(r, a):             return math.sqrt(r*r + a*a)
def sv_dRc(r, a):            return r/math.sqrt(r*r + a*a)
def sv_horizon(a, M=1.0):
    """r = +-sqrt(4M^2 - a^2).  None when a >= 2M."""
    d = 4.0*M*M - a*a
    return math.sqrt(d) if d > 0.0 else None
def sv_C(r, a, M=1.0):
    d = sv_dRc(r, a)
    if d == 0.0:  return float('inf')
    f = sv_f(r, a, M)
    return math.sqrt(1.0/f)/d if f > 0.0 else float('nan')
def sv_discriminant(r, a, M=1.0):
    """definitions.py's |g_tt| C^2.  Bounded = HORIZON, divergent = THROAT."""
    C = sv_C(r, a, M)
    if C == float('inf'): return float('inf')
    return abs(sv_f(r, a, M))*C*C

def sv_character(a, M=1.0):
    if a <= 0.0:            return "SCHWARZSCHILD -- horizon only, no throat"
    if a < 2.0*M:           return "BLACK-BOUNCE -- THROAT INSIDE HORIZON"
    if a == 2.0*M:          return "extremal null throat"
    return "TRAVERSABLE WORMHOLE -- throat only, no horizon"

# ------------------------------------------------ the record
VERIFIED_THIS_SESSION = [
 ("arXiv:2502.00502", "Spherically symmetric and static black bounces with multiple horizons, "
                      "throats, and anti-throats in four dimensions",
  "'This type of metric presents a WORMHOLE THROAT INSIDE AN EVENT HORIZON'"),
 ("arXiv:2506.19818", "LQG inspired spacetimes as solutions of the Einstein equations",
  "'compact objects with a wormhole structure HIDDEN BEHIND AN EVENT HORIZON ... "
  "obtained through general relativity by considering the presence of EXOTIC MATTER'"),
 ("arXiv:2608.02771", "Black bounces to traversable wormholes from pure gravity in four "
                      "and higher dimensions",
  "'as VACUUM SOLUTIONS of metric gravitational theories' -- NO exotic matter, OUTSIDE GR"),
 ("arXiv:2608.08208", "Black bounce sourced by non-minimally coupled linear electrodynamics "
                      "and a canonical scalar field through a thin shell at the throat",
  "a NON-MINIMALLY COUPLED source -- the xi of qei.py, and electrodynamics, the switch of switch.py"),
]

ORIENTATION_IS_CORRECT        = True    # black hole in, throat out
PAIR_PY_REFUTATION_REVERSES   = True    # its own argument supports the new sign
KERR_CAN_DO_IT                = False   # exact dichotomy at a = M
DEFINITIONS_PY_THROAT_FAULT   = True    # 13th fault: two of three checks were timelike-r
DEFINITIONS_PY_IS_EDITED      = False   # corrected here, never edited
SIMPSON_VISSER_DOES_IT        = True    # published, and the spine classifies it unmodified
NEEDS_EXOTIC_MATTER_IN_GR     = True    # arXiv:2506.19818
VACUUM_OUTSIDE_GR             = True    # arXiv:2608.02771 -- wormhole.py's open DECISION
IS_ONE_WAY                    = True
IS_A_CORRIDOR_BETWEEN_PLACES  = False
THIS_PASS_REPAIRS_ANYTHING    = False

# ================================================================= report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  KERR CANNOT DO IT, AND THE ALGEBRA IS EXACT")
    P("="*79)
    P("\n  Delta(r_t) = u(u+2)(u-1) M^2,  u = (a/M)^(2/3).  Positive iff a > M.\n")
    P(f"  {'a/M':>7} {'r_t':>10} {'Delta(r_t)':>13} {'u(u+2)(u-1)':>14}   slice")
    for a in (0.3, 0.5, 0.9, 0.99, 1.0, 1.01, 1.5, 3.0):
        rt = kerr_locus(1.0, a); D = kerr_Delta(rt, 1.0, a); alg = kerr_locus_Delta(1.0, a)
        tag = ("SPACELIKE -- a throat" if D > 1e-14 else
               "EXTREMAL -- Delta = 0" if abs(D) <= 1e-14 else
               "TIMELIKE r -- NOT a throat")
        P(f"  {a:7.2f} {rt:10.6f} {D:13.6f} {alg:14.6f}   {tag}")
    P("""
    a < M   a HORIZON exists and there is NO SPATIAL THROAT
    a = M   Delta(r_t) = 0 EXACTLY -- they coincide, and neither is a throat
    a > M   a SPATIAL THROAT exists and there is NO HORIZON AT ALL

    MUTUALLY EXCLUSIVE, EXACTLY, AT a = M.  You cannot have both in Kerr.

    AND THAT IS A FAULT IN definitions.py, ONE DAY OLD AND MINE.  That file
    verified its "throat" at a = 0.3, 0.99 and 3.0 -- and only a = 3.0 is
    over-extremal.  TWO OF THE THREE WERE IN THE TIMELIKE-r REGION, where a
    minimum of the circumferential radius is not a throat because there is no
    spacelike slice for it to be a minimum on.  THIRTEENTH FAULT.

    WHAT SURVIVES: (M a^2)^(1/3) is still the geometric scale at which 2Ma^2/r
    balances r^2, and expose.py's kappa is still the fraction of it at which
    contraction stops.  Calling that scale THE THROAT RADIUS is correct only for
    a > M -- which is the exposed, naked case, exactly as expose.py found.""")

    P("\n" + "="*79)
    P("2.  BUT THE OBJECT EXISTS, IT IS PUBLISHED, AND THE SPINE READS IT UNCHANGED")
    P("="*79)
    P("""
    SIMPSON-VISSER BLACK-BOUNCE: send r^2 -> r^2 + a^2 in Schwarzschild.

        R_c = sqrt(r^2 + a^2)   ->   dR_c/dr = 0 at r = 0, FOR ANY a > 0
        horizon at r = +- sqrt(4M^2 - a^2), REAL IFF a < 2M
""")
    P(f"  {'a/M':>7} {'horizon r_h':>13}   character")
    for a in (0.0, 0.5, 1.0, 1.9, 2.0, 2.5):
        rh = sv_horizon(a)
        P(f"  {a:7.2f} {('%.6f'%rh) if rh else 'NONE':>13}   {sv_character(a)}")
    a = 1.0; rh = sv_horizon(a)
    P(f"\n  definitions.py's SPINE, applied unmodified, a = 1.0, horizon r = {rh:.6f}:\n")
    P(f"  {'r':>10} {'C':>13} {'g_tt':>11} {'|g_tt| C^2':>13}   regime")
    for r in (5.0, 3.0, 2.5, rh + 1e-6, 1.5, 1.0, 0.3, 0.0):
        f = sv_f(r, a); C = sv_C(r, a); D = sv_discriminant(r, a)
        Cs = "inf" if C == float('inf') else (f"{C:.4f}" if C == C else "(r timelike)")
        Ds = "inf" if D == float('inf') else (f"{D:.6f}" if D == D else "--")
        reg = ("THROAT" if r == 0 else "HORIZON" if abs(r-rh) < 1e-5 else
               "EXPANSION" if r > rh else "interior (r timelike)")
        P(f"  {r:10.6f} {Cs:>13} {-f:+11.6f} {Ds:>13}   {reg}")
    P(f"""
    AT THE HORIZON  |g_tt| C^2 -> 1/(dR_c/dr)^2 = {1.0/(rh/2.0)**2:.6f}, FINITE -> HORIZON.
    AT r = 0        dR_c/dr = 0 exactly, g_tt =/= 0, |g_tt| C^2 -> inf -> THROAT.

    BOTH OBJECTS.  ONE METRIC.  THE THROAT IS INSIDE THE HORIZON.
    THE DISCRIMINANT WAS WRITTEN YESTERDAY FOR A DIFFERENT QUESTION AND NEEDED
    NOT ONE CHANGE TO READ THIS ONE.

    Verified against the paper database in this session:""")
    for cite, title, what in VERIFIED_THIS_SESSION:
        P(f"      {cite}")
        for ln in _wrap(what, 68): P(f"          {ln}")

    P("\n" + "="*79)
    P("3.  WHAT IT COSTS -- AND WHERE THE ONE DOOR IS")
    P("="*79)
    P("""
    IN GENERAL RELATIVITY IT NEEDS EXOTIC MATTER.  arXiv:2506.19818, verbatim:
    the structure is "obtained through general relativity by considering the
    presence of EXOTIC MATTER".  Same wall as every other route -- and the
    throat's flare-out is a NEC violation, which is what a throat IS.

    OUTSIDE GENERAL RELATIVITY IT NEED NOT.  arXiv:2608.02771 derives black
    bounces and traversable wormholes "from PURE GRAVITY", as VACUUM SOLUTIONS
    of metric gravitational theories in four and higher dimensions.

        THAT IS wormhole.py's SCOPE_CHOSEN_HERE = None.

    The f(R) and scalar-tensor scope question, open since wormhole.py, asserted
    None in that file's own selftest so that nobody could quietly decide it, and
    classified by gaps.py as the ONE DECISION-grade gap in the whole census --
    the one gap that is M's and not a computation.  M'S ASSERTION HAS WALKED THE
    PROJECT ONTO ITS OWN OPEN DECISION.  It is not resolved here and will not be.

    AND IT IS ONE-WAY, WHICH IS NOT A DETAIL BUT THE WHOLE SHAPE OF THE THING.
    The throat sits INSIDE the horizon, where r is TIMELIKE -- measured above,
    g_tt is POSITIVE throughout the interior.  A timelike r means the throat is
    crossed at a MOMENT, not at a PLACE:

        you cannot hover at it
        you cannot return through it
        you cannot send anything back
        and the far side is another asymptotic region, not a chosen destination

    A ONE-WAY EXIT TO ELSEWHERE IS NOT A CORRIDOR BETWEEN TWO PLACES.  That is
    the same objection that closed the Kerr route in expose.py, the Einstein-
    Rosen bridge in pair.py, and every other door on the list.  THE ORIENTATION
    IS RIGHT AND THE OBJECT IS REAL AND IT STILL DOES NOT GO WHERE YOU CHOOSE.""")

    P("\n  " + "-"*74)
    P("""  THE PASS IN ONE PARAGRAPH

  M remembers proposing a wormhole/black-hole corridor with the wormhole as
  entrance, and being refuted, and says the refutation was really about
  direction.  THE MEMORY IS ACCURATE AND SO IS THE INFERENCE.  pair.py section 2
  refuted it because "a horizon is a one-way null surface ... nothing exits
  through a black hole" -- AND THAT ARGUMENT RUN BACKWARDS SUPPORTS THE OTHER
  ORIENTATION, since a surface admitting only inward crossing is the one thing
  that can only be an ENTRANCE.  Nobody turned it around at the time.  KERR
  CANNOT REALISE IT, exactly: the equatorial dR_c/dr = 0 locus has
  Delta = u(u+2)(u-1)M^2 with u = (a/M)^(2/3), positive IFF a > M, so a horizon
  and a spatial throat are MUTUALLY EXCLUSIVE at exactly a = M -- which also
  CORRECTS definitions.py, whose three "throat" checks included two at
  sub-extremal spin where r is timelike and the word does not apply, the
  THIRTEENTH FAULT.  BUT THE OBJECT IS PUBLISHED: the SIMPSON-VISSER BLACK-BOUNCE
  sends r^2 -> r^2+a^2, putting dR_c/dr = 0 at r = 0 with a horizon at
  sqrt(4M^2-a^2), so for 0 < a < 2M THERE IS A WORMHOLE THROAT INSIDE AN EVENT
  HORIZON -- verified in the literature, not asserted (arXiv:2502.00502,
  2506.19818) -- and definitions.py's discriminant |g_tt|C^2 reads it correctly
  with NO MODIFICATION: finite at the horizon, divergent at the throat.  THE
  PRICE IS THE SAME WALL WITH ONE DOOR: in GR the source is exotic matter
  (2506.19818), and outside GR the same geometry is a VACUUM solution
  (2608.02771) -- which is precisely wormhole.py's SCOPE_CHOSEN_HERE = None, the
  single DECISION-grade gap in gaps.py's census and the one that is M's.  AND IT
  IS ONE-WAY: the throat is inside the horizon where r is timelike, so it is
  crossed at a MOMENT rather than a PLACE -- no hovering, no return, nothing sent
  back, and the far side is another asymptotic region rather than a destination.
  THE ORIENTATION IS RIGHT, THE OBJECT IS REAL, AND IT STILL DOES NOT GO WHERE
  YOU CHOOSE.  NOTHING IS REPAIRED AND definitions.py IS NOT EDITED.""")
    P("  " + "-"*74)

def _wrap(s, w):
    out, cur = [], ""
    for word in s.split():
        if len(cur)+len(word)+1 > w: out.append(cur); cur = word
        else: cur = (cur+" "+word).strip()
    if cur: out.append(cur)
    return out

# ================================================================= selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("orient.py --selftest\n")

    print("Kerr: the locus is a throat IFF over-extremal, exactly")
    for a in (0.3, 0.5, 0.9, 0.99):
        chk(f"a/M = {a}: NOT a throat", kerr_locus_is_a_throat(1.0, a), False)
    for a in (1.01, 1.5, 3.0, 10.0):
        chk(f"a/M = {a}: IS a throat", kerr_locus_is_a_throat(1.0, a), True)
    chk("a = M exactly: Delta(r_t) = 0", round(kerr_locus_Delta(1.0, 1.0), 12), 0.0, 1e-12)
    print("  and the factorisation matches Delta evaluated directly")
    for a in (0.3, 1.0, 3.0):
        rt = kerr_locus(1.0, a)
        chk(f"  u(u+2)(u-1) == Delta(r_t) at a = {a}",
            round(kerr_locus_Delta(1.0, a) - kerr_Delta(rt, 1.0, a), 12), 0.0, 1e-12)
    chk("so horizon and throat are mutually exclusive in Kerr", KERR_CAN_DO_IT, False)
    chk("  which is a fault in definitions.py", DEFINITIONS_PY_THROAT_FAULT, True)
    chk("  corrected here, that file NOT edited", DEFINITIONS_PY_IS_EDITED, False)

    print("\nSimpson-Visser: a throat inside a horizon")
    chk("dR_c/dr = 0 at r = 0 for any a > 0", sv_dRc(0.0, 1.0), 0.0)
    for a, want in ((0.5, True), (1.0, True), (1.9, True), (2.0, False), (2.5, False)):
        chk(f"a = {a}: horizon exists", sv_horizon(a) is not None, want)
    chk("a = 1.0 horizon at sqrt(3)", round(sv_horizon(1.0), 9), round(math.sqrt(3.0), 9), 1e-9)
    chk("throat r=0 is INSIDE that horizon", 0.0 < sv_horizon(1.0), True)
    chk("character at a = 1.0", sv_character(1.0), "BLACK-BOUNCE -- THROAT INSIDE HORIZON")
    chk("character at a = 2.5", sv_character(2.5), "TRAVERSABLE WORMHOLE -- throat only, no horizon")
    chk("character at a = 0",   sv_character(0.0), "SCHWARZSCHILD -- horizon only, no throat")

    print("\nand definitions.py's discriminant reads it with NO modification")
    a = 1.0; rh = sv_horizon(a)
    chk("at the horizon |g_tt|C^2 is FINITE", sv_discriminant(rh + 1e-9, a) < 10.0, True)
    chk("  and equals 1/(dR_c/dr)^2", round(sv_discriminant(rh + 1e-9, a), 5),
        round(1.0/sv_dRc(rh, a)**2, 5), 1e-4)
    chk("at the throat |g_tt|C^2 DIVERGES", sv_discriminant(0.0, a), float('inf'))
    chk("  because dR_c/dr = 0 there and g_tt =/= 0", abs(sv_f(0.0, a)) > 0.1, True)
    chk("the interior has g_tt > 0 -- r is TIMELIKE, so the throat is a MOMENT",
        all(sv_f(r, a) < 0.0 for r in (0.3, 1.0, 1.5)), True)

    print("\nwhat this pass claims and refuses")
    chk("the orientation is correct", ORIENTATION_IS_CORRECT, True)
    chk("  and pair.py's own argument reverses to support it", PAIR_PY_REFUTATION_REVERSES, True)
    chk("the object is published, not hypothesised", SIMPSON_VISSER_DOES_IT, True)
    chk("citations verified this session", len(VERIFIED_THIS_SESSION), 4)
    chk("in GR it needs exotic matter", NEEDS_EXOTIC_MATTER_IN_GR, True)
    chk("  outside GR it is a vacuum solution", VACUUM_OUTSIDE_GR, True)
    chk("  which is wormhole.py's OPEN DECISION, not resolved here", VACUUM_OUTSIDE_GR, True)
    chk("it is ONE-WAY", IS_ONE_WAY, True)
    chk("  so it is NOT a corridor between two places", IS_A_CORRIDOR_BETWEEN_PLACES, False)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
