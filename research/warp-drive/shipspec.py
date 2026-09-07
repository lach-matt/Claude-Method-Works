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
import stationkeep as SK

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
DV_TOTAL  = SK.treadmill_dv(K_PASS, BETA_A, PASSES)   # 6.711 c -- the open row, closed
CEILING   = SK.ceiling_beta(K_PASS)                   # 0.0937 c, whatever N is

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
 ("PERFORMANCE","terminal speed, as specified",0.866,"c","INVALID",
  "unreachable -- stationkeep.py: gamma_final <= 1 + one pass, and N does not appear"),
 ("PERFORMANCE","terminal speed, achievable",CEILING,"c","DERIVED","the bound-return ceiling at this k"),
 ("PERFORMANCE","proper acceleration felt",0.0,"g","DERIVED","geodesic throughout"),
 ("PERFORMANCE","propellant for transport",0.0,"kg","DERIVED","borrowed gradient"),
 ("PERFORMANCE","free passes before escape",SK.free_passes(K_PASS,BETA_A),"","DERIVED",
  "the binding budget is the whole free ride, and it is 4 passes"),

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
 ("NAVIGATION","station-keeping delta-v",DV_TOTAL,"c","DERIVED",
  "COMPUTED -- 1086 paid re-binds at Oberth cost. It decided against the ladder"),
 ("NAVIGATION","timing precision required",None,"s","OPEN","chaotic stratum, unquantified"),

 ("ARRIVAL","with a deflector present","free","","DERIVED","time-symmetric reverse pass"),
 ("ARRIVAL","without, mass ratio at 0.87c",3.7314,"","DERIVED","arrival.py, photon floor"),
 ("ARRIVAL","magsail at 0.87c",2.6,"ly","DERIVED","brake distance; must start before departure"),
 ("ARRIVAL","destination has a deflector",None,"","OPEN","routing constraint, unsurveyed"),

 ("ONBOARD","power for transport",0.0,"W","DERIVED","none required"),
 ("ONBOARD","power for steering",None,"W","OPEN",
  "moot for the ladder; live again only for the billiard branch"),
 ("ONBOARD","life support envelope",None,"","OPEN","not attempted"),
 ("ONBOARD","mission duration",None,"yr","OPEN","depends on route, unselected"),
]

FLAG = """
  THE FLAGGED ITEM IS NO LONGER A GAP.  IT IS A VERDICT.

  Every version of this sheet has carried one OPEN row marked "the number that
  decides whether the ship needs an engine": the station-keeping delta-v.
  stationkeep.py computed it, and it answered a larger question than it was
  asked.

  THE NUMBER.  A payload only returns for another pass if it is BOUND, and the
  binding budget at k = 94.4 is 1 - E/m = 2.64e-3 -- four passes.  The other
  1086 must each be bought back: braked at periapsis, 6.18e-3 c apiece,
  6.711 c of proper delta-v in total, to deliver 0.87 c.  The architecture's
  one claim was ZERO PROPELLANT.

  THE THEOREM, which is worse.  Bound means E/m < 1, and E/m IS the gamma the
  payload would show at infinity.  So before the final pass gamma_inf <= 1, and
  one pass adds at most dgamma:

      gamma_final  <=  1 + 2 beta_A gamma_A sin(delta/2)

  N DOES NOT APPEAR.  The 6.711 c buys nothing -- the rungs of the ladder are
  spent climbing back to escape and only the last one goes anywhere.  Reaching
  gamma = 2 in one pass needs beta_A >= 0.4472, a binary at 0.625 r_s, inside
  its own horizon.  No flywheel spins that fast because none can.

  WHAT THE SHEET NOW SPECIFIES.  Not 0.87 c.  The bound-return ceiling at this
  deflector, %.4f c -- reached in ONE pass, in 14 seconds, with no station-
  keeping at all, off an object in the LIGO catalogue.  That is a real vehicle
  and it is 89%% short of the target.

  AND THE TRADE IS NOW EXPLICIT.  The ceiling is a function of k, the same k
  that made the deflector catalogued:

      k = 94.4    50 Msun   catalogued        0.0937 c
      k =  3.0  8823 Msun   IMBH              0.4751 c
      k =  1.5 24956 Msun   IMBH              0.6066 c
      absolute ceiling, a = 3 r_s, delta = pi 0.7085 c

  YOU CAN HAVE THE CATALOGUED OBJECT OR YOU CAN HAVE THE SPEED.  324x the
  deflector buys 5.9x the speed, and even paying it in full stops at 0.71 c.

  THE ONE THING STILL OPEN, and it is not on this sheet -- stationkeep.billiard.
  The theorem assumes the payload turns around by falling back.  A backscatter
  turns it around with no binding, so gamma compounds: 1.99 bounces to gamma = 2
  rather than 1090 passes.  Whether a rotating dumbbell can present a LEADING
  FACE twice per cycle is three-body geometry nobody here has asked, and it is
  the only route left to 0.87 c that does not carry propellant.
""" % CEILING

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
