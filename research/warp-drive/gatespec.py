#!/usr/bin/env python3
"""
gatespec.py -- GATE 1, living specification sheet.

Every field carries a STATUS, and the sheet is a diagnostic: the OPEN and
INVALID rows are where the design is still missing, counted rather than
narrated.  Regenerate as findings land; the counts should fall.

  MEASURED     came out of a run in this project
  DERIVED      closed form from MEASURED or PINNED inputs
  PINNED       stated in the literature or a seated member
  ESTIMATED    order of magnitude, no better
  ASSUMED      a design choice, named as such
  OPEN         no value: this is a gap
  INVALID      a value that was carried over and does NOT survive the torus

The geometry changed from sphere to torus at commit 23ef2fc, and much of the
spherical specification did not survive that change.  Rows marked INVALID are
the ones this sheet caught.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30

# --- torus geometry, carried from torus.py's DEC-compliant design point ------
R0, A_TUBE = 4902.0, 1600.0            # major, minor radius (m)
R_BORE     = R0 - A_TUBE               # bore radius (m)
M_GATE     = 2.200330e30               # kg
V_WARP     = 0.0476                    # c
E_STORE    = 1.17e46                   # J

def torus_volume(R0=R0, a=A_TUBE):
    return 2.0*math.pi**2*R0*a**2

def torus_density(M=M_GATE, R0=R0, a=A_TUBE):
    return M/torus_volume(R0, a)

def lambda_max(R0=R0, a=A_TUBE):
    return c**2/(G*math.log(8.0*R0/a))

def dec_margin(M=M_GATE, R0=R0, a=A_TUBE):
    return 2.0*math.pi*R0*lambda_max(R0, a)/M

# (section, field, value, unit, status, note)
SPEC = [
 ("IDENTITY","designation","GATE 1","","ASSUMED","first article"),
 ("IDENTITY","class","geodesic launcher / brake","","DERIVED","launcher.py"),
 ("IDENTITY","topology","open torus","","DERIVED","residue.py: sealed gate launches nothing"),
 ("IDENTITY","role","fixed terminal, one direction","","DERIVED","gate1.py: shift is a vector"),

 ("GEOMETRY","major radius R0",R0,"m","ASSUMED","matched to the sphere's R1 for comparison"),
 ("GEOMETRY","minor radius a",A_TUBE,"m","ASSUMED","a/R0 = 0.33"),
 ("GEOMETRY","bore radius",R_BORE,"m","DERIVED","R0 - a"),
 ("GEOMETRY","tube volume",torus_volume(),"m^3","DERIVED","2 pi^2 R0 a^2"),
 ("GEOMETRY","shift profile shape",None,"","OPEN",
  "S(r) raised cosine was SPHERICAL; the toroidal profile is underived"),
 ("GEOMETRY","gamma = R2/R1 = 1+sqrt(3)",None,"","INVALID",
  "the geometry optimum was derived for a SPHERICAL shell; no torus analogue"),

 ("MASS","total mass",M_GATE,"kg","ASSUMED","carried from the spherical design point"),
 ("MASS","  in solar masses",M_GATE/MSUN,"Msun","DERIVED",""),
 ("MASS","tube density",torus_density(),"kg/m^3","DERIVED","M / 2 pi^2 R0 a^2"),
 ("MASS","  vs nuclear saturation",torus_density()/2.3e17,"x","DERIVED","2.3e17 kg/m^3"),
 ("MASS","material","degenerate nuclear matter","","PINNED","gate1.py: no vessel reaches 1e34 Pa"),
 ("MASS","source","a neutron star","","DERIVED","self-gravity is the only confinement"),

 ("STRUCTURE","hoop tension margin (DEC)",dec_margin(),"x","DERIVED","torus.py closed form"),
 ("STRUCTURE","lambda_max",lambda_max(),"kg/m","DERIVED","c^2 / G ln(8R0/a)"),
 ("STRUCTURE","circulation dynamic stress",None,"Pa","OPEN",
  "2.25e33 Pa was the SPHERICAL wall figure; toroidal flow geometry undefined"),
 ("STRUCTURE","equilibrium","hoop tension, no rotation","","DERIVED","torus.py"),
 ("STRUCTURE","dynamical stability",None,"","OPEN",
  "self-gravitating tori have a known runaway instability; not assessed"),

 ("FIELD","v_warp",V_WARP,"c","MEASURED","TARGET-1, spherical; assumed to carry over"),
 ("FIELD","interior lapse alpha",0.762761,"","INVALID",
  "measured in the SPHERICAL cavity; a torus has no enclosed interior"),
 ("FIELD","flat region",None,"","OPEN",
  "CRITICAL -- see the flagged item below"),
 ("FIELD","circulation speed",0.330,"c","INVALID",
  "gearing k = 6.94 was derived from the spherical k_hat; no toroidal value"),
 ("FIELD","energy conditions","Type I, DEC margin 5.89x","","DERIVED",
  "torus.py hoop bound only -- not the full stress-energy"),

 ("POWER","reservoir",E_STORE,"J","ASSUMED","carried from the spherical design"),
 ("POWER","per launch, 1000 t",1.019915e20,"J","DERIVED","launcher.py"),
 ("POWER","source","accretion","","DERIVED","gate1.py: only 1e46 J process on a NS"),
 ("POWER","accretion time",26.65,"Myr","DERIVED","Eddington-limited"),
 ("POWER","flow topology coupling",None,"","OPEN",
  "accretion is toroidal rotation; the metric needs a different flow"),

 ("OPERATIONS","delivered speed",V_WARP,"c","DERIVED","one gate, from rest"),
 ("OPERATIONS","proper acceleration on payload",0.0,"g","DERIVED","geodesic throughout"),
 ("OPERATIONS","shell recoil, 1000 t",6.493779e-18,"m/s","DERIVED","launcher.py"),
 ("OPERATIONS","launches before depletion",1.147154e26,"","DERIVED","launcher.py"),
 ("OPERATIONS","switching mechanism",None,"","OPEN",
  "how the shift is raised while a payload is inside; relaxation permits it"),
 ("OPERATIONS","cycle time",None,"s","OPEN","depends on switching"),

 ("NAVIGATION","aim","one partner, fixed at build","","DERIVED","gate1.py"),
 ("NAVIGATION","lead angle, Alpha Cen",332.4492,"arcsec","DERIVED","gate1.py"),
 ("NAVIGATION","v_warp tuning","relativistic composition","","DERIVED","gate1.py"),

 ("INTERFACE","ingress","through the bore","","DERIVED","open topology; no wall transit"),
 ("INTERFACE","egress","through the bore","","DERIVED","the reason the torus is required"),
 ("INTERFACE","payload envelope",None,"m","OPEN",
  "bore radius is 3302 m but the usable flat volume is undefined"),
 ("INTERFACE","tidal load on payload",None,"g","OPEN","not computed for the torus"),
]

FLAG = """
  THE ONE THE SHEET CAUGHT -- FIELD / flat region.

  The whole value of the warp shell is a FLAT interior: alpha and beta constant,
  every Christoffel vanishing, the payload on a geodesic feeling nothing.  In the
  SPHERE that region is the enclosed cavity, and TARGET-1 measured it directly.

  A torus has no enclosed cavity.  Along the bore axis there is no matter at all
  -- and that is where the problem sits, precisely:

    In the sphere, the shift ramps from beta = v inside to beta = 0 outside
    THROUGH THE MATTER.  TARGET-1 measured exactly that: beta = 0.040000 at
    r = 0-8 m, falling across the wall, 0.000000 by r = 24 m.  The momentum
    constraint ties the shift's gradient to the momentum density T^0i, and the
    matter is there to supply it.

    In the torus, the shift must also fall to zero along the AXIS, going out of
    the bore mouth.  But the axis is VACUUM: T^0i = 0.  The momentum constraint
    is then HOMOGENEOUS there, which does not forbid a shift gradient but does
    severely constrain which profiles are admissible -- and nothing in this
    project has checked whether a profile exists that is flat in the bore,
    tapers to zero along the axis, and sources that taper with no matter.

  Note this is NOT the Krasnikov objection: the boosted region here is bounded,
  a few km long, not an unbounded channel, so the Everett-Roman no-go for
  Krasnikov tubes does not apply as stated.  The concern is narrower and is
  about the AXIAL TERMINATION of the shift in vacuum.

  torus.py's 5.89x DEC margin does not touch this.  It bounds the HOOP STRESS of
  the ring against collapse.  It says nothing about the stress-energy needed to
  sustain and terminate a boosted region inside the bore, which is a different
  component of the same tensor.

  The ingress bound FORCED the open topology.  Whether the open topology can
  carry a shift at all is now the live question, and it is sharper than the one
  it replaced.
"""

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-52s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Geometry")
    chk("bore radius (m)", R_BORE, 3302.0)
    chk("tube volume (m^3)", torus_volume(), 2.0*math.pi**2*R0*A_TUBE**2)
    chk("density (kg/m^3)", torus_density(), M_GATE/torus_volume())
    print("\nIdentities")
    chk("volume scales as a^2 (identity)", torus_volume(R0,2*A_TUBE)/torus_volume(), 4.0)
    chk("density inverse to volume (identity)",
        torus_density(M_GATE,R0,2*A_TUBE)*torus_volume(R0,2*A_TUBE), M_GATE)
    chk("DEC margin agrees with torus.py", dec_margin(), 5.892177, tol=1e-5)

    print("\nSheet integrity -- the diagnostic")
    stat = {}
    for row in SPEC:
        stat[row[4]] = stat.get(row[4], 0) + 1
    for k in sorted(stat):
        print("  %-52s %14d" % (k, stat[k]))
    # every OPEN and INVALID row must carry a note saying why
    bad = [r[1] for r in SPEC if r[4] in ("OPEN","INVALID") and not r[5]]
    ok &= (bad == [])
    print("  %-52s %14s %14s  %s" % ("OPEN/INVALID rows lacking a reason", bad, [],
                                     "ok" if bad==[] else "FAIL"))
    # An OPEN row must carry no value.  An INVALID row may carry the superseded
    # number or drop it, so the rule is an IMPLICATION, not an equivalence --
    # the first version of this check was an equivalence and flagged a correct row.
    mism = [r[1] for r in SPEC if r[4]=="OPEN" and r[2] is not None]
    ok &= (mism == [])
    print("  %-52s %14s %14s  %s" % ("OPEN rows carrying a value", mism, [],
                                     "ok" if mism==[] else "FAIL"))
    # and no row outside OPEN/INVALID may be valueless
    ghost = [r[1] for r in SPEC if r[2] is None and r[4] not in ("OPEN","INVALID")]
    ok &= (ghost == [])
    print("  %-52s %14s %14s  %s" % ("valueless rows with a live status", ghost, [],
                                     "ok" if ghost==[] else "FAIL"))
    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*80)
    print("GATE 1 -- SPECIFICATION SHEET (living; regenerate as findings land)")
    print("="*80)
    sec = None
    for s, f, v, u, st, note in SPEC:
        if s != sec:
            print("\n%s" % s); print("-"*80); sec = s
        if v is None:
            val = "--"
        elif isinstance(v, float):
            val = ("%.4f" % v) if 1e-3 < abs(v) < 1e5 else ("%.4e" % v)
        else:
            val = str(v)
        mark = {"OPEN":"  <<< GAP","INVALID":"  <<< DOES NOT SURVIVE THE TORUS"}.get(st,"")
        print("  %-30s %-22s %-8s %-9s%s" % (f, val[:22], u, st, mark))
        if note and st in ("OPEN","INVALID"):
            print("  %-30s   %s" % ("", note))
    n_open = sum(1 for r in SPEC if r[4]=="OPEN")
    n_inv  = sum(1 for r in SPEC if r[4]=="INVALID")
    print("\n" + "="*80)
    print("  %d fields, %d OPEN, %d INVALIDATED BY THE TORUS" % (len(SPEC), n_open, n_inv))
    print("="*80)
    print(FLAG)
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
