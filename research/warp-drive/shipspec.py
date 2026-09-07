#!/usr/bin/env python3
"""
shipspec.py -- VEHICLE 1, living specification for the surviving architecture.

Everything that manufactures a shift is closed: the drive (CM-THEOREM), the
portal (topological censorship), the gate (egress + NO-TAPER), and the object
itself (elements.py: v_warp <= 0.0713 c for anything, ever).  What survives
manufactures no shift and therefore owes no charge -- the coupling family.

So this is not a drive specification.  It is a specification for a PASSIVE
PAYLOAD WITH STEERING, riding gradients it did not make.

Same discipline as gatespec.py: every field carries a status, and the OPEN
rows are the diagnostic.  Regenerate as findings land.

  MEASURED / DERIVED / PINNED / ESTIMATED / ASSUMED / OPEN / INVALID

stdlib only.
"""
import math, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import person as PZ

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30
YR = 3.15576e7

# ---- Kerr geometry: what spin buys, and what it costs -----------------------
def isco(a, pro=True):
    Z1 = 1.0 + (1-a*a)**(1.0/3.0)*((1+a)**(1.0/3.0) + (1-a)**(1.0/3.0))
    Z2 = math.sqrt(3*a*a + Z1*Z1)
    return 3 + Z2 + (-1 if pro else 1)*math.sqrt((3-Z1)*(3+Z1+2*Z2))

def r_photon(a, pro=True):
    return 2.0*(1.0 + math.cos((2.0/3.0)*math.acos((-1 if pro else 1)*a)))

def b_crit(a, pro=True):
    """Critical impact parameter, equatorial. From R(r)=R'(r)=0 on the radial
    potential: b = (r^2 + a^2 + a sqrt(Delta)) / (a + sqrt(Delta))."""
    r = r_photon(a, pro); D = r*r - 2.0*r + a*a
    sD = math.sqrt(max(D, 0.0))
    return (r*r + a*a + a*sD)/(a + sD) if (a + sD) > 0 else 2.0

def dv_gain(a):
    """dv ~ c sqrt(r_s/b), so closer approach buys sqrt(b0/b)."""
    return math.sqrt(b_crit(0.0)/b_crit(a))

def tide_penalty(a):
    """Tides go as 1/r^3 at the closest allowed approach."""
    return (r_photon(0.0)/r_photon(a))**3

def mass_floor(a_max_g, d, r_over_M):
    """Smallest deflector mass holding the tide under a_max across extent d,
    at closest approach r = r_over_M x M (geometric).  Tides fall as 1/M^2."""
    a_max = a_max_g*9.80665
    # a_tide = 2 G M d / r^3 with r = r_over_M * GM/c^2
    #        = 2 c^6 d / (r_over_M^3 G^2 M^2)
    return math.sqrt(2.0*c**6*d/(a_max*r_over_M**3*G**2))

# ---- the route (NAVIGATION.md, slingshot.py) --------------------------------
# SUPERSEDED by person.py.  The earlier sheet flew beta_A = 0.10 at a deep pass
# (k ~ 3 r_s) and needed an 8823 Msun deflector.  person.py shows k is the lever:
# M ~ k^-3/2 while passes ~ k, so trading gain for distance buys the deflector
# down into the LIGO catalogue -- and shows beta_A = 0.10 fails the merger budget
# outright (margin 0.119).  Both numbers below now come from that instrument.
BETA_A    = 0.03                                  # below person.beta_ceiling
Q_RATIO   = PZ.routh_q_max()                      # largest q with stable L4/L5
CHI       = PZ.fragility(2.0, 9.8)                # 2 m payload at 1 g
DEFLECTOR = 50.0 * MSUN                           # the fast component
K_PASS    = PZ.pass_distance(DEFLECTOR, CHI)      # 94.4 r_s
GAIN      = PZ.gain_per_pass(BETA_A, K_PASS)      # 6.36e-4, not 0.25
PASSES    = PZ.passes_to(2.0, BETA_A, K_PASS)     # 1090
_A, _T, ORBITS = PZ.unequal_binary(DEFLECTOR, Q_RATIO, BETA_A)

def passes_to(gamma_t, gain=GAIN):
    return math.log(gamma_t)/math.log(1.0+gain)

SPEC = [
 ("IDENTITY","designation","VEHICLE 1","","ASSUMED","first article"),
 ("IDENTITY","class","passive payload, steered","","DERIVED","every shift-maker is closed"),
 ("IDENTITY","propulsion","NONE","","DERIVED","the point: it owes no charge"),
 ("IDENTITY","shift manufactured","none","","DERIVED","so SSV, Type IV, OBJ-CEILING are silent"),

 ("ROUTE","deflector type","Kerr binary","","DERIVED","kerr.py: spin buys approach"),
 ("ROUTE","deflector mass",DEFLECTOR/MSUN,"Msun","DERIVED","person.py: set by k, not by beta"),
 ("ROUTE","pass distance k = r_p/r_s",K_PASS,"","DERIVED","person.py: (chi/tau_s)^(2/3)"),
 ("ROUTE","light-component speed",BETA_A,"c","DERIVED","person.py: below the 0.0587 ceiling"),
 ("ROUTE","mass ratio m1:m2",1.0/Q_RATIO,"","ASSUMED","the FORK -- see the flagged item"),
 ("ROUTE","companion mass",DEFLECTOR/Q_RATIO/MSUN,"Msun","DERIVED","Routh, not tides"),
 ("ROUTE","orbits to merger",ORBITS,"","DERIVED","person.py: unequal_binary at this q"),
 ("ROUTE","merger margin",ORBITS/PASSES,"x","DERIVED","orbits left / passes needed"),
 ("ROUTE","L4/L5 stability","STABLE","","DERIVED","mu < (9-sqrt69)/18"),
 ("ROUTE","component spin a/M",None,"","OPEN",
  "no measured spin distribution for IMBH binaries; assumed high, never sourced"),
 ("ROUTE","a known binary meeting spec",None,"","OPEN",
  "NARROWED, not closed -- the 50 Msun DEFLECTOR is catalogued; the companion is not"),

 ("PERFORMANCE","gain per pass",GAIN,"","DERIVED","person.py: 2 beta gamma sin(1/k)"),
 ("PERFORMANCE","Kerr dv enhancement",dv_gain(0.998),"x","DERIVED","b_crit 5.196 -> 2.111"),
 ("PERFORMANCE","passes to gamma = 2",PASSES,"","DERIVED","geometric, non-saturating"),
 ("PERFORMANCE","mission time",PASSES*_T/86400.0,"d","DERIVED","one pass per orbit, ASSUMED cadence"),
 ("PERFORMANCE","terminal speed",0.866,"c","DERIVED","gamma = 2"),
 ("PERFORMANCE","proper acceleration felt",0.0,"g","DERIVED","geodesic throughout"),
 ("PERFORMANCE","propellant for transport",0.0,"kg","DERIVED","borrowed gradient"),

 ("STRUCTURE","tidal penalty at Kerr r_ph",tide_penalty(0.998),"x","DERIVED","vs Schwarzschild 3M"),
 ("STRUCTURE","deflector floor at a DEEP pass, 1 g / 20 m",
   mass_floor(1.0,20.0,r_photon(0.998))/MSUN,"Msun","DERIVED","the wall k was found to go round"),
 ("STRUCTURE","tide on a 2 m body at k",PZ.S.tidal_accel(DEFLECTOR,K_PASS,2.0)/9.80665,"g",
   "DERIVED","the constraint that DEFINES k"),
 ("STRUCTURE","hull design",None,"","OPEN","no structural spec attempted"),
 ("STRUCTURE","radiation environment",None,"","OPEN",
  "accretion flow and Blandford-Znajek fields at r_ph are unmodelled"),

 ("NAVIGATION","flight plan","braid word in B_3","","DERIVED","Law 4: no trajectory exists"),
 ("NAVIGATION","guidance law","bracket propagator","","DERIVED","join closes, meet fails"),
 ("NAVIGATION","masses need not be known","yes","","DERIVED","Law 5, mass-uniformity"),
 ("NAVIGATION","which braid word",None,"","OPEN","unselected; must drift with the inspiral"),
 ("NAVIGATION","station-keeping delta-v",None,"m/s","OPEN",
  "NEVER COMPUTED. The one number that decides whether the ship needs an engine"),
 ("NAVIGATION","timing precision required",None,"s","OPEN","chaotic stratum, unquantified"),

 ("ARRIVAL","with a deflector present","free","","DERIVED","time-symmetric reverse pass"),
 ("ARRIVAL","without, mass ratio at 0.87c",3.7314,"","DERIVED","arrival.py, photon floor"),
 ("ARRIVAL","magsail at 0.87c",2.6,"ly","DERIVED","brake distance; must start before departure"),
 ("ARRIVAL","destination has a deflector",None,"","OPEN","routing constraint, unsurveyed"),

 ("ONBOARD","power for transport",0.0,"W","DERIVED","none required"),
 ("ONBOARD","power for steering",None,"W","OPEN","follows from station-keeping delta-v"),
 ("ONBOARD","life support envelope",None,"","OPEN","not attempted"),
 ("ONBOARD","mission duration",None,"yr","OPEN","depends on route, unselected"),
]

FLAG = """
  THE ONE THE SHEET CATCHES -- ROUTE / mass ratio, and it has MOVED.

  The earlier sheet flagged inventory: the design called for an IMBH binary at
  25:1 and near-extremal spin, and no such object is confirmed.  person.py
  removed half of that.  The tide sets only the PASS DISTANCE k, and k trades
  against deflector mass as M ~ k^-3/2 while costing only N ~ k passes.  Pull k
  from 3 r_s out to 94.4 and the deflector falls from 8823 Msun to 50 -- which
  is a LIGO-catalogue object (GW150914 was 36 + 29).  The deflector is found.

  What is NOT found is the companion, and the reason is now precise.  L4/L5 is
  linearly stable only below Routh's mu = (9-sqrt69)/18, so a 50 Msun deflector
  with a stable co-orbital parking point needs a companion of 1248 Msun.  The
  IMBH is no longer a TIDAL requirement.  It is a PARKING requirement, and it is
  the only clause of the old conjunction still standing.

  So the sheet forks, and both branches are priced:

    q = 1       2 x 50 Msun, catalogued, 4.3 h mission, merger margin 14.7x.
                No stable L4/L5.  Station-keeping must be ACTIVE.
    q = 0.0401  50 + 1248 Msun, NOT catalogued, 16.7 d mission, margin 2603x.
                Free parking.  The ship can sit there and owe nothing.

  THE ONE NUMBER THAT DECIDES IT -- NAVIGATION / station-keeping delta-v.
  It has never been computed, and it now decides two things rather than one.
  If it is small, the q = 1 branch works: VEHICLE 1 is a passive payload with
  thrusters, the "no propulsion" claim holds, and THE ENGINE IS AN OBJECT THAT
  HAS ALREADY BEEN OBSERVED.  If it is large, the ship needs a real engine to
  hold the accelerating family, the propellant saved on transport is spent on
  steering, and the design falls back to the q = 0.0401 branch -- where the
  parking is free and the object is once again one nobody has found.

  The project has not run out of physics.  It has run out of arithmetic it
  declined to do.  Nothing here has looked, and it is computable.
"""

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        good = (got == want) if isinstance(want,(bool,str)) else abs(got-want) <= tol*abs(want)
        g = got if isinstance(want,(bool,str)) else "%.7g" % got
        w = want if isinstance(want,(bool,str)) else "%.7g" % want
        ok &= good
        print("  %-50s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Kerr geometry -- against textbook values")
    chk("Schwarzschild ISCO is 6M", isco(0.0), 6.0, tol=1e-9)
    chk("extremal prograde ISCO is 1M", isco(1.0), 1.0, tol=1e-6)
    chk("Schwarzschild photon sphere is 3M", r_photon(0.0), 3.0, tol=1e-12)
    chk("extremal prograde photon orbit is 1M", r_photon(1.0), 1.0, tol=1e-12)
    chk("Schwarzschild b_crit is 3sqrt(3)", b_crit(0.0), 3*math.sqrt(3.0), tol=1e-9)
    chk("extremal prograde b_crit is 2M", b_crit(1.0), 2.0, tol=1e-9)

    print("\nIdentities")
    chk("no gain without spin (identity)", dv_gain(0.0), 1.0, tol=1e-12)
    chk("no tide penalty without spin (identity)", tide_penalty(0.0), 1.0, tol=1e-12)
    chk("mass floor scales as sqrt(d) (identity)",
        mass_floor(1.0,80.0,3.0)/mass_floor(1.0,20.0,3.0), 2.0, tol=1e-12)
    chk("mass floor scales as 1/sqrt(a_max) (identity)",
        mass_floor(4.0,20.0,3.0)/mass_floor(1.0,20.0,3.0), 0.5, tol=1e-12)
    chk("passes: gamma=4 is twice gamma=2 (identity)",
        passes_to(4.0)/passes_to(2.0), 2.0, tol=1e-12)

    print("\nAgainst person.py -- the sheet must not drift from the instrument")
    chk("deflector mass floor at k reproduces 50 Msun",
        PZ.deflector_mass(CHI, K_PASS)/MSUN, 50.0, tol=1e-9)
    chk("tide at the sheet's k is exactly 1 g",
        PZ.S.tidal_accel(DEFLECTOR, K_PASS, 2.0), 9.8, tol=1e-9)
    chk("sheet's beta is under person.beta_ceiling",
        BETA_A < PZ.beta_ceiling(2.0, K_PASS), True)
    chk("sheet's q is exactly Routh's ceiling", Q_RATIO, PZ.routh_q_max(), tol=1e-12)
    chk("merger margin at the sheet's q", ORBITS/PASSES, 2603.083, tol=1e-5)
    chk("companion mass (Msun)", DEFLECTOR/Q_RATIO/MSUN, 1247.9968, tol=1e-5)

    print("\nSheet integrity")
    stat = {}
    for r in SPEC: stat[r[4]] = stat.get(r[4],0)+1
    for k in sorted(stat): print("  %-50s %14d" % (k, stat[k]))
    bad = [r[1] for r in SPEC if r[4]=="OPEN" and not r[5]]
    ok &= (bad==[])
    print("  %-50s %14s %14s  %s" % ("OPEN rows lacking a reason", bad, [], "ok" if bad==[] else "FAIL"))
    mism = [r[1] for r in SPEC if r[4]=="OPEN" and r[2] is not None]
    ok &= (mism==[])
    print("  %-50s %14s %14s  %s" % ("OPEN rows carrying a value", mism, [], "ok" if mism==[] else "FAIL"))
    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*80)
    print("VEHICLE 1 -- SPECIFICATION SHEET (the surviving architecture)")
    print("="*80)
    sec=None
    for s,f,v,u,st,note in SPEC:
        if s!=sec: print("\n%s"%s); print("-"*80); sec=s
        val = "--" if v is None else (("%.4f"%v) if isinstance(v,float) and 1e-3<abs(v)<1e5
              else ("%.4e"%v if isinstance(v,float) else str(v)))
        mark = "  <<< GAP" if st=="OPEN" else ""
        print("  %-30s %-16s %-7s %-9s%s" % (f, val[:16], u, st, mark))
        if note and st=="OPEN": print("  %-30s   %s" % ("", note))
    n=sum(1 for r in SPEC if r[4]=="OPEN")
    print("\n"+"="*80)
    print("  %d fields, %d OPEN" % (len(SPEC), n))
    print("="*80)
    print(FLAG)
    print("-- What spin buys, and what it costs ------------------------------------------")
    print("  %-8s %9s %9s %10s %12s" % ("a/M","r_photon","b_crit","dv gain","tide penalty"))
    for a in (0.0,0.5,0.9,0.99,0.998,1.0):
        print("  %-8.3f %9.4f %9.4f %10.4f %11.1fx"
              % (a, r_photon(a), b_crit(a), dv_gain(a), tide_penalty(a)))
    print("""
  Spin does not change the deflector's SPEED, which is what Zhang's gain scales
  with.  It changes how CLOSE the approach may be: b_crit falls from 3sqrt(3) to
  2, worth %.3fx in dv.  The bill is %.0fx the tidal load, and since tides fall
  as 1/M^2 that is bought back with %.1fx the deflector mass -- which is why the
  mass floor in this sheet is %.2e Msun rather than the 2.8e4 of the
  Schwarzschild case.
""" % (dv_gain(1.0), tide_penalty(1.0), math.sqrt(tide_penalty(1.0)),
       mass_floor(1.0,20.0,r_photon(0.998))/MSUN))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
