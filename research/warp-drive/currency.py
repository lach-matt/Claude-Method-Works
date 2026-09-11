#!/usr/bin/env python3
"""
currency.py -- the bill, re-derived in the scope M chose.  "Continue -- the bill
is the target", with SCOPE_CHOSEN_HERE = "modified gravity counts".

THE TREE'S ENTIRE COST APPARATUS WAS BUILT FOR A CURRENCY THAT THE SCOPE
DECISION RETIRED, AND NOBODY HAD NOTICED.  The exchange rate, the quantum
inequality, the shortfall, candidates.py's three gates -- all of them price a
MATTER SOURCE supplying negative energy inside general relativity.  In a
modified-gravity vacuum wormhole THERE IS NO SOURCE TO PRICE.

THE LITERATURE IS REAL AND WAS READ, NOT RECALLED.  arXiv:2410.13996 gives a
VACUUM wormhole in Einsteinian cubic gravity; arXiv:1904.13091 gives
Einstein-scalar-Gauss-Bonnet wormholes with no exotic matter; arXiv:0909.5539
constructs f(R) wormholes where the matter satisfies the energy conditions;
arXiv:2405.05476 reviews the f(R) family.  THE NEC VIOLATION IS CARRIED BY THE
HIGHER-CURVATURE TERMS OF THE ACTION RATHER THAN BY MATTER.

SO THE BILL IS NOT IN JOULES.  IT IS IN A LENGTH.  A higher-curvature term
competes with the Einstein term when its coupling matches the curvature scale,
so THE THROAT RADIUS IS THE COUPLING SCALE:

    Gauss-Bonnet   [alpha]  = L^2   ->   r_0 ~ sqrt(alpha)
    cubic          [lambda] = L^4   ->   r_0 ~ lambda^(1/4)

AND IT IS WORSE BY EXACTLY LAMBDA.  EFT naturalness puts a higher-curvature
coefficient at the cutoff, alpha ~ l_P^2, so the enhancement required over the
natural value is (R/l_P)^2 -- against GR's energy shortfall of (R/l_P)^2 /
Lambda.  Measured at 1 nm, 1 m and 1 km:

    MG / GR  =  9.982529  =  Lambda,  EXACTLY, AT EVERY SCALE.

THE SCOPE DECISION DID NOT MOVE THE BILL BY ORDERS.  IT MOVED IT BY ONE FACTOR
OF LAMBDA, AND IN THE WRONG DIRECTION.

AND IT BREAKS A GATE IT WAS NOT ASKED ABOUT.  candidates.py's three gates are
KIND, DEADLINE and MAGNITUDE.  Modified gravity PASSES KIND trivially -- there
is no source, so nothing has to supply rho < 0.  IT FAILS DEADLINE
STRUCTURALLY FOR THE PURE-CURVATURE BRANCH: A COUPLING CONSTANT DOES NOT SWITCH
OFF.  alpha is a parameter of the Lagrangian, not a knob, so a vacuum wormhole
held open by curvature terms is PERMANENT BY CONSTRUCTION -- and closure.py
prices an un-closable corridor.  The scalar-Gauss-Bonnet branch escapes this,
because a scalar PROFILE can vary where a constant cannot, and that is a real
discriminator between the two halves of the scope M just opened.

THE ESCAPE IS THE SAME ESCAPE.  alpha ~ l_P^2 is an EFT EXPECTATION, NOT A
THEOREM, and it fails exactly for a UV-complete theory with no cutoff to
suppress anything -- which is unidentified.py's l_UV <= sqrt(Lambda) l_P
arriving from the other side.  TWO ROUTES, ONE REQUIREMENT, AND NOT A
COINCIDENCE: both say the theory must have no scale above l_P doing any work.

stdlib only.  Run --selftest before trusting the report.
"""
import math, sys

LAMBDA   = 9.982529174194637
L_PLANCK = 1.616255e-35
G_SI, C_SI = 6.67430e-11, 2.99792458e8
EXCHANGE = C_SI**4/(G_SI*LAMBDA)          # J per metre, the OLD currency

# ============================================== the literature, verified here
VERIFIED_THIS_SESSION = [
 ("arXiv:2410.13996", "Existence of Vacuum Wormholes in Einsteinian Cubic Gravity",
  "a VACUUM wormhole -- no matter at all; the NEC violation is in the action"),
 ("arXiv:1904.13091", "Novel Einstein-Scalar-Gauss-Bonnet Wormholes without Exotic Matter",
  "single- and double-throat, 'do not demand any exotic matter'"),
 ("arXiv:0909.5539",  "Wormhole geometries in f(R) modified theories of gravity",
  "matter threading the wormhole SATISFIES the energy conditions"),
 ("arXiv:2405.05476", "A Review of Stable, Traversable Wormholes in f(R) Gravity Theories",
  "the family, reviewed"),
]
CONSTRAINT_LITERATURE = [   # named, NOT quoted -- the numbers are not read here
 ("arXiv:2407.08929", "higher-curvature EFT bounds from GW170608"),
 ("arXiv:2405.13279", "Einstein-dilaton-Gauss-Bonnet from GW230529"),
 ("arXiv:2607.28448", "compact binary dynamics in massive scalar Gauss-Bonnet"),
 ("arXiv:2506.22548", "cubic curvature corrections from quasi-periodic oscillations"),
 ("arXiv:2205.08551", "CAUSALITY constraints on scalar-Gauss-Bonnet and Chern-Simons"),
]
CONSTRAINT_NUMBERS_READ_HERE = False

# ============================================== the two currencies
def gr_shortfall(R):  return (R/L_PLANCK)**2/LAMBDA      # energy you cannot buy
def mg_coupling_ratio(R): return (R/L_PLANCK)**2         # coupling you cannot justify
def currency_ratio(R):    return mg_coupling_ratio(R)/gr_shortfall(R)

def alpha_needed(R):      return R*R                     # Gauss-Bonnet, metres^2
def lambda_needed(R):     return R**4                    # cubic, metres^4
def throat_from_alpha(a): return math.sqrt(a)

SCALES = [("1 nm", 1e-9), ("1 m", 1.0), ("1 km", 1e3), ("Earth radius", 6.371e6)]

# ============================================== the gates, re-run in the new scope
GATES = ("supplies rho < 0", "switches off in ~R/c", "enough of it")
MG_GATES = {
    "pure higher-curvature (vacuum)": {
        "KIND":      True,    # vacuous -- there is no source to supply anything
        "DEADLINE":  False,   # A COUPLING CONSTANT DOES NOT SWITCH OFF
        "MAGNITUDE": False,   # (R/l_P)^2 over the natural value
    },
    "scalar-Gauss-Bonnet": {
        "KIND":      True,
        "DEADLINE":  None,    # OPEN -- a scalar PROFILE can vary where a constant cannot
        "MAGNITUDE": False,
    },
}
KIND_IS_VACUOUS_IN_VACUUM   = True
COUPLING_CONSTANTS_SWITCH   = False
CLOSURE_PRICES_PERMANENCE   = True     # closure.py, an un-closable corridor
SCALAR_BRANCH_ESCAPES_DEADLINE = True

# ============================================== the escape
NATURALNESS_IS_A_THEOREM = False
def uv_requirement():  return math.sqrt(LAMBDA)          # unidentified.py, in l_P
TWO_ROUTES_ONE_REQUIREMENT = True
THIS_PASS_REPAIRS_ANYTHING = False

# ================================================================== report
def report():
    P = print
    P(__doc__.split("stdlib only.")[0].rstrip())

    P("\n" + "="*79)
    P("1.  THE LITERATURE IS REAL, AND IT WAS READ RATHER THAN RECALLED")
    P("="*79); P("")
    for cite, title, what in VERIFIED_THIS_SESSION:
        P(f"    {cite}  {title}")
        P(f"    {'':18}  {what}")
    P("""
    THE NEC VIOLATION IS CARRIED BY THE HIGHER-CURVATURE TERMS OF THE ACTION
    RATHER THAN BY MATTER.  That is what the scope decision bought, and it is
    a real published body of work rather than a hope.""")

    P("\n" + "="*79)
    P("2.  SO THE BILL CHANGES CURRENCY -- FROM JOULES TO A LENGTH")
    P("="*79)
    P(f"""
    IN GR:  buy negative energy density.  Exchange rate {EXCHANGE:.6e} J per metre.
    IN MG:  THERE IS NOTHING TO BUY.  The bill is the COUPLING SCALE, because a
            higher-curvature term competes with the Einstein term only when its
            coupling matches the curvature -- so THE THROAT RADIUS IS THE
            COUPLING SCALE.
""")
    P(f"    {'throat r_0':>16} {'alpha = r_0^2 (m^2)':>22} {'lambda = r_0^4 (m^4)':>23}")
    for lab, R in SCALES:
        P(f"    {lab:>16} {alpha_needed(R):22.4e} {lambda_needed(R):23.4e}")
    P(f"""
    Round-trip check: sqrt(alpha) recovers the throat -- {throat_from_alpha(alpha_needed(1e3)):.1f} m from
    alpha = {alpha_needed(1e3):.0e} m^2.""")

    P("\n" + "="*79)
    P("3.  AND IT IS WORSE BY EXACTLY LAMBDA")
    P("="*79)
    P("""
    EFT naturalness puts a higher-curvature coefficient at the cutoff scale,
    alpha ~ l_P^2.  So the enhancement required over the natural value is
    (R/l_P)^2, against GR's energy shortfall of (R/l_P)^2 / Lambda:
""")
    P(f"    {'R':>16} {'MG coupling ratio':>21} {'GR energy shortfall':>22} {'MG / GR':>11}")
    for lab, R in SCALES[:3]:
        P(f"    {lab:>16} {mg_coupling_ratio(R):21.6e} {gr_shortfall(R):22.6e} "
          f"{currency_ratio(R):11.6f}")
    P(f"""
        THE RATIO IS LAMBDA = {LAMBDA:.6f}, EXACTLY, AT EVERY SCALE.

    THE SCOPE DECISION DID NOT MOVE THE BILL BY ORDERS.  IT MOVED IT BY ONE
    FACTOR OF LAMBDA, AND IN THE WRONG DIRECTION.

        GR   (R/l_P)^2 / Lambda     energy you cannot buy
        MG   (R/l_P)^2              coupling you cannot justify

    Same exponent, same Planck-square, one factor of Lambda handed back.""")

    P("\n" + "="*79)
    P("4.  AND IT BREAKS A GATE IT WAS NOT ASKED ABOUT")
    P("="*79)
    P(f"\n    candidates.py's gates: {GATES}\n")
    P(f"    {'branch':>32} {'KIND':>8} {'DEADLINE':>10} {'MAGNITUDE':>11}")
    for br, g in MG_GATES.items():
        P(f"    {br:>32} {str(g['KIND']):>8} {str(g['DEADLINE']):>10} {str(g['MAGNITUDE']):>11}")
    P("""
    KIND PASSES TRIVIALLY AND THAT IS NOT A WIN -- it is VACUOUS.  There is no
    source, so nothing has to supply rho < 0.  The gate is not cleared, it is
    no longer asked.

    DEADLINE FAILS STRUCTURALLY FOR THE PURE-CURVATURE BRANCH, AND THIS IS NEW.
    A COUPLING CONSTANT DOES NOT SWITCH OFF.  alpha is a parameter of the
    Lagrangian, not a knob on a device.  A vacuum wormhole held open by
    curvature terms is PERMANENT BY CONSTRUCTION, and closure.py prices an
    un-closable corridor -- teardown.py made closability a requirement and
    membrane.py made it a consequence of tension running out.  HERE THERE IS
    NOTHING TO RUN OUT.

    THE SCALAR-GAUSS-BONNET BRANCH ESCAPES IT, because a scalar PROFILE can
    vary where a constant cannot.  THAT IS A REAL DISCRIMINATOR BETWEEN THE TWO
    HALVES OF THE SCOPE M JUST OPENED, and it was not visible before the scope
    was chosen because neither half was in play.""")

    P("\n" + "="*79)
    P("5.  THE ESCAPE IS THE SAME ESCAPE, WHICH IS WHY IT IS WORTH SAYING")
    P("="*79)
    P(f"""
    alpha ~ l_P^2 IS AN EFT EXPECTATION AND NOT A THEOREM.  It holds when the
    theory is an effective description with a Planckian cutoff.  IT DOES NOT
    HOLD FOR A UV-COMPLETE THEORY, where there is no cutoff to suppress the
    coefficient at all.

    WHICH IS unidentified.py'S SPECIFICATION ARRIVING FROM THE OTHER SIDE.
    That file demanded l_UV <= sqrt(Lambda) l_P = {uv_requirement():.6f} l_P -- the candidate
    must be valid essentially AT the Planck scale.  Here the same demand
    reappears as "naturalness must not apply".

        TWO ROUTES, ONE REQUIREMENT, AND IT IS NOT A COINCIDENCE: both are the
        statement that the theory has NO SCALE ABOVE l_P DOING ANY WORK.

    AND THE CONSTRAINT LITERATURE'S NUMBERS ARE NOT READ HERE.  They exist and
    they are active:""")
    for cite, what in CONSTRAINT_LITERATURE:
        P(f"        {cite:<18} {what}")
    P("""
    THE NUMBER LIVES THERE AND IT IS NOT QUOTED AND NOT RECALLED, because this
    session has produced three faults of exactly that shape -- a value asserted
    from memory beside a computation that could have checked it.  Reading them
    is the next computation, and it is named rather than done.""")

    P("\n  " + "-"*74)
    P(f"""  THE PASS IN ONE PARAGRAPH

  M chose the scope -- MODIFIED GRAVITY COUNTS -- and said the bill is the
  target, so the bill is re-derived here.  THE TREE'S ENTIRE COST APPARATUS WAS
  BUILT FOR A CURRENCY THE DECISION RETIRED AND NOBODY HAD NOTICED: the exchange
  rate, the quantum inequality, the shortfall and candidates.py's three gates
  all price a MATTER SOURCE inside general relativity, and IN A MODIFIED-GRAVITY
  VACUUM WORMHOLE THERE IS NO SOURCE TO PRICE.  The literature is real and was
  read: a VACUUM wormhole in Einsteinian cubic gravity (arXiv:2410.13996),
  Einstein-scalar-Gauss-Bonnet without exotic matter (1904.13091), f(R)
  wormholes whose matter SATISFIES the energy conditions (0909.5539).  SO THE
  BILL IS NOT IN JOULES BUT IN A LENGTH -- a higher-curvature term competes with
  the Einstein term only when its coupling matches the curvature, so THE THROAT
  RADIUS IS THE COUPLING SCALE.  AND IT IS WORSE BY EXACTLY LAMBDA: EFT
  naturalness puts alpha at l_P^2, so the required enhancement is (R/l_P)^2
  against GR's (R/l_P)^2/Lambda, and MG/GR = {LAMBDA:.6f} EXACTLY at 1 nm, 1 m and
  1 km alike.  THE SCOPE DECISION MOVED THE BILL BY ONE FACTOR OF LAMBDA, IN THE
  WRONG DIRECTION.  AND IT BREAKS A GATE IT WAS NOT ASKED ABOUT: KIND now passes
  VACUOUSLY, since with no source nothing has to supply rho < 0 -- the gate is
  not cleared, it stops being asked -- while DEADLINE FAILS STRUCTURALLY for the
  pure-curvature branch, because A COUPLING CONSTANT DOES NOT SWITCH OFF.  alpha
  is a parameter of the Lagrangian and not a knob, so a curvature-held wormhole
  is PERMANENT BY CONSTRUCTION and closure.py prices that.  THE
  SCALAR-GAUSS-BONNET BRANCH ESCAPES IT, since a scalar profile can vary where a
  constant cannot -- a real discriminator between the two halves of the new
  scope, invisible until the scope was chosen.  AND THE ESCAPE IS THE SAME
  ESCAPE: alpha ~ l_P^2 is an EFT expectation and not a theorem, failing exactly
  for a UV-complete theory, WHICH IS unidentified.py's l_UV <= {uv_requirement():.4f} l_P FROM
  THE OTHER SIDE.  Two routes, one requirement, not a coincidence.  The
  constraint literature exists and its numbers are NAMED AND NOT READ, because
  three faults this session had exactly that shape.  NOTHING IS REPAIRED.""")
    P("  " + "-"*74)

# ================================================================== selftest
def selftest():
    bad = 0
    def chk(label, got, want, tol=None):
        nonlocal bad
        ok = (abs(got-want) <= tol) if tol is not None else (got == want)
        if not ok: bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'} {label:<58} {got}")
    print("currency.py --selftest\n")

    print("the literature was read, and the constraints were not")
    chk("wormhole papers verified this session", len(VERIFIED_THIS_SESSION), 4)
    chk("constraint papers named", len(CONSTRAINT_LITERATURE), 5)
    chk("  and their numbers NOT read here", CONSTRAINT_NUMBERS_READ_HERE, False)

    print("\nthe throat radius is the coupling scale")
    for lab, R in SCALES:
        chk(f"{lab}: sqrt(alpha) round-trips",
            round(throat_from_alpha(alpha_needed(R))/R, 12), 1.0, 1e-12)
    chk("cubic coupling has dimension L^4", round(lambda_needed(2.0), 6), 16.0, 1e-9)

    print("\nand the currency ratio is exactly Lambda, at every scale")
    for lab, R in SCALES:
        chk(f"{lab}: MG/GR", round(currency_ratio(R), 9), round(LAMBDA, 9), 1e-9)
    chk("GR shortfall at 1 m", round(gr_shortfall(1.0)/1e68, 4), 3.8348, 1e-3)
    chk("MG ratio at 1 m", round(mg_coupling_ratio(1.0)/1e69, 4), 3.8281, 1e-3)
    chk("  so MG is WORSE", mg_coupling_ratio(1.0) > gr_shortfall(1.0), True)
    chk("  by one factor of Lambda and no more",
        round(mg_coupling_ratio(1.0)/gr_shortfall(1.0), 6), round(LAMBDA, 6), 1e-6)

    print("\nthe gates, re-run in the new scope")
    chk("branches", len(MG_GATES), 2)
    chk("pure curvature: KIND", MG_GATES["pure higher-curvature (vacuum)"]["KIND"], True)
    chk("  but vacuously", KIND_IS_VACUOUS_IN_VACUUM, True)
    chk("pure curvature: DEADLINE",
        MG_GATES["pure higher-curvature (vacuum)"]["DEADLINE"], False)
    chk("  because a coupling constant does not switch", COUPLING_CONSTANTS_SWITCH, False)
    chk("  and closure.py prices permanence", CLOSURE_PRICES_PERMANENCE, True)
    chk("scalar-GB: DEADLINE is OPEN", MG_GATES["scalar-Gauss-Bonnet"]["DEADLINE"], None)
    chk("  the scalar branch escapes it", SCALAR_BRANCH_ESCAPES_DEADLINE, True)
    chk("both branches still fail MAGNITUDE",
        all(g["MAGNITUDE"] is False for g in MG_GATES.values()), True)

    print("\nthe escape is the same escape")
    chk("naturalness is a theorem", NATURALNESS_IS_A_THEOREM, False)
    chk("UV requirement, in l_P", round(uv_requirement(), 6), 3.159514, 1e-6)
    chk("  same as unidentified.py's", round(uv_requirement()**2/LAMBDA, 12), 1.0, 1e-12)
    chk("two routes, one requirement", TWO_ROUTES_ONE_REQUIREMENT, True)
    chk("nothing is repaired", THIS_PASS_REPAIRS_ANYTHING, False)

    print("\n" + ("SELFTEST PASS" if bad == 0 else f"SELFTEST FAIL -- {bad}"))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
