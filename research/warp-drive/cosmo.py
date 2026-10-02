#!/usr/bin/env python3
"""
cosmo.py -- the shared hypothesis, and the case that is already observed.

Every device-level no-go this project established carries the same hypothesis:

    CM-THEOREM   no isolated system moves its own CoM   P_ADM  -> asympt. flat
    T2-ADM       P_ADM = 0, M_ADM > 0, cannot translate P_ADM  -> asympt. flat
    SSV-NOGO     Natario drives violate the NEC         asymptotically flat
    NO-TAPER     a shift cannot terminate in vacuum     MINKOWSKI background
    NO-PORTAL    topological censorship, no shortcut    asympt. flat + glob. hyp.

Five of eight.  The three that do not (EM-GAP, NO-BORE, SWIMMER) are arithmetic
or local material timescales and are untouched by anything here.

THE UNIVERSE IS NOT ASYMPTOTICALLY FLAT.  It is FLRW, and in FLRW none of those
five theorems is even statable: there is no ADM mass, no ADM momentum, and the
hypotheses of topological censorship fail.

And metric transport faster than light is not speculative there.  It is measured.

  PINNED, Planck 2018 (arXiv:1807.06209): H0 = 67.36 km/s/Mpc, age 13.797 Gyr,
  comoving particle horizon 14.26 Gpc.  [As first written.  The horizon was
  never READ; it is now COMPUTED, 14.151 Gpc -- see the follow-up below.]

  CORRECTED (DOCKET 67).  The two Planck figures are Table 2's TT,TE,EE+lowE+
  lensing 68% values, H0 = 67.36 +- 0.54 and age 13.797 +- 0.023 Gyr, and
  Planck calls H0 "inferred (model-dependent)" under base-LCDM, "in
  significant, 3.6 sigma, tension with local measurements" (4.4 sigma in its
  conclusions).  The 14.26 Gpc horizon is NOT printed in the Planck pages
  read; its origin is NAMED-NOT-READ.  Flat base-LCDM with Planck's own Table
  2 column gives 14.147 Gpc, so 14.26 is 0.80% high (WMAP-era parameters give
  14.28).  The recession at the horizon then reads about 3.18 c rather than
  3.204 c -- superluminal either way, and no verdict here uses more than the
  sign of H0.

  CORRECTED (DOCKET 67 follow-up, on M's rulings "ok, update" and "address/
  correct/repair all figures").  HORIZON_GPC = 14.26 carried the status word
  PINNED, which this tree reserves for a value READ at a source; it was not
  READ anywhere.  It is now COMPUTED here, horizon_gpc(), by integrating flat
  base-LCDM from Planck 2018's READ inputs: Table 2 (TT,TE,EE+lowE+lensing)
  H0 = 67.36 and Omega_m = 0.3153; T_CMB = 2.7255 K (p.14); N_eff = 3.046
  (abstract, p.1); and Table 1's caption, "Omega_m includes the contribution
  from one neutrino with a mass of 0.06 eV".  Result: 14.151 Gpc = 46.155 Gly,
  agreeing with DOCKET 67's verifier (14.151, with the massive neutrino; the
  auditor's 14.147 is the massless-neutrino approximation, reproduced in the
  selftest).  The typed 14.26 is kept as HORIZON_GPC_TYPED, NAMED-NOT-READ,
  0.77% above.  Recession at the horizon moves 3.204 c -> 3.180 c and the
  transport ratio 3.371 -> 3.345.  NO VERDICT MOVED: superluminal either way.
  HYPOTHESES, NAMED: spatial flatness and w = -1 (base-LCDM, Planck's model,
  not a measurement of either); the Table 2 central values, with their 68%
  intervals NOT propagated (they are correlated in Planck's chains, which
  were not read); N_eff shared equally over three species, two massless and
  one of 0.06 eV (Planck's baseline; the equal split is a convention,
  NAMED-NOT-READ); no other relativistic species.  The computed age, 13.796
  Gyr against the READ 13.797, is the integrator's check, not a new figure;
  the transport ratio keeps the READ age.

stdlib only.
"""
import math, sys

c   = 299792458.0
MPC = 3.0856775814913673e22
GLY = 9.4607304725808e24
YR  = 3.15576e7        # Julian year, 365.25 x 86400 -- must match GLY

H0_KMSMPC   = 67.36          # PINNED Planck 2018 (+- 0.54; base-LCDM, model-
                             # dependent; 3.6-4.4 sigma tension -- DOCKET 67)
AGE_GYR     = 13.797         # PINNED (+- 0.023)
# CORRECTED (DOCKET 67 follow-up).  First typed  HORIZON_GPC = 14.26  # PINNED.
# Not in the Planck pages read (origin NAMED-NOT-READ), so the word PINNED was
# wrong.  Kept as a record; the horizon is now COMPUTED by horizon_gpc().
HORIZON_GPC_TYPED = 14.26    # NAMED-NOT-READ, a record -- never used in a figure
HORIZON_GPC_STATUS = "COMPUTED"   # flat base-LCDM from READ Planck 2018 inputs

# READ inputs for the horizon integral (Planck 2018 VI, arXiv:1807.06209v4).
OMEGA_M     = 0.3153         # READ Table 2, TT,TE,EE+lowE+lensing (+- 0.0073)
T_CMB_K     = 2.7255         # READ p.14, Fixsen 2009, adopted by Planck
N_EFF       = 3.046          # READ p.1 (abstract), the SM value Planck assumes
M_NU_EV     = 0.06           # READ Table 1 caption: one neutrino of 0.06 eV
# SI-exact constants (2019 SI) and CODATA 2018 G, for Omega_gamma.
_KB   = 1.380649e-23
_HBAR = 6.62607015e-34/(2.0*math.pi)
_EV   = 1.602176634e-19
_G    = 6.67430e-11

def H0():
    """s^-1."""
    return H0_KMSMPC*1e3/MPC

def _simpson(f, a, b, n):
    n += n % 2
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0)*f(a+i*h)
    return s*h/3.0

def _fd_massive_ratio(x):
    """rho(m)/rho(m=0) for one Fermi-Dirac neutrino species, x = m c^2/(k T_nu)."""
    num = _simpson(lambda q: q*q*math.sqrt(q*q+x*x)/(math.exp(q)+1.0), 0.0, 60.0, 600)
    return num/(7.0*math.pi**4/120.0)

_FLCDM_CACHE = {}

def flat_lcdm(m_nu_ev=M_NU_EV, n=4000):
    """(comoving particle horizon in Gpc, age in Gyr) of flat base-LCDM with
    the READ Planck 2018 inputs above.  m_nu_ev = 0 gives the massless-neutrino
    approximation (DOCKET 67's auditor's 14.147).  Integrated in ln a from
    a = 1e-9 (the [0, 1e-9] piece added in closed form), composite Simpson."""
    key = (m_nu_ev, n)
    if key in _FLCDM_CACHE:
        return _FLCDM_CACHE[key]
    H = H0()
    rhoc = 3.0*H*H/(8.0*math.pi*_G)
    Og = (math.pi**2/15.0)*(_KB*T_CMB_K)**4/(_HBAR*c)**3/c**2/rhoc
    O1 = Og*(7.0/8.0)*(N_EFF/3.0)*(4.0/11.0)**(4.0/3.0)   # one species, relativistic
    if m_nu_ev > 0:
        Tnu = T_CMB_K*(4.0/11.0)**(1.0/3.0)*(N_EFF/3.0)**0.25
        x0 = m_nu_ev*_EV/(_KB*Tnu)
        lx0, lx1, N = math.log(1e-4), math.log(1e6), 800
        lx = [lx0+i*(lx1-lx0)/N for i in range(N+1)]
        lF = [math.log(_fd_massive_ratio(math.exp(v))) for v in lx]
        def F(x):
            if x < 1e-4:
                return 1.0
            t = (math.log(x)-lx0)/(lx[1]-lx[0]); i = min(int(t), N-1); f = t-i
            return math.exp((1.0-f)*lF[i]+f*lF[i+1])
        Ocb = OMEGA_M - O1*F(x0)
        Orad = Og + 2.0*O1
        OL = 1.0 - OMEGA_M - Orad
        a4E2 = lambda a: Ocb*a + Orad + O1*F(x0*a) + OL*a**4
    else:
        Orad = Og + 3.0*O1
        OL = 1.0 - OMEGA_M - Orad
        a4E2 = lambda a: OMEGA_M*a + Orad + OL*a**4
    t1 = math.log(1e-9)
    chi = _simpson(lambda t: math.exp(t)/math.sqrt(a4E2(math.exp(t))), t1, 0.0, n) \
        + 1e-9/math.sqrt(a4E2(0.0))
    age = _simpson(lambda t: math.exp(2.0*t)/math.sqrt(a4E2(math.exp(t))), t1, 0.0, n)
    out = (chi*c/H/MPC/1e3, age/H/(1e9*YR))
    _FLCDM_CACHE[key] = out
    return out

def horizon_gpc():
    """Comoving particle horizon, Gpc -- COMPUTED (DOCKET 67 follow-up)."""
    return flat_lcdm()[0]

def hubble_time_gyr():
    return 1.0/H0()/(1e9*YR)

def hubble_radius_gly():
    return c/H0()/GLY

def horizon_gly():
    # CORRECTED (DOCKET 67 follow-up): first  return HORIZON_GPC*1e3*MPC/GLY
    # with the typed 14.26; now the computed horizon.
    return horizon_gpc()*1e3*MPC/GLY

def recession(d_gly):
    """Hubble-law recession speed at comoving distance d, in c."""
    return H0()*d_gly*GLY/c

def superluminal_distance_gly():
    """Comoving distance at which recession reaches c: exactly the Hubble radius."""
    return hubble_radius_gly()

def transport_ratio():
    """Comoving horizon divided by (c x age): how far metric transport has
    outrun light in the observed universe."""
    return horizon_gly()/AGE_GYR

# Energy conditions of a perfect fluid, exactly (rho > 0 assumed):
def conditions(w):
    """w = p/rho.  Returns (NEC, WEC, SEC, DEC) as booleans."""
    return (1.0+w >= 0.0, 1.0+w >= 0.0, 1.0+3.0*w >= 0.0, 1.0 >= abs(w))

FLUIDS = [("dust (matter)", 0.0), ("radiation", 1.0/3.0),
          ("curvature", -1.0/3.0), ("cosmological constant", -1.0)]

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-4):
        nonlocal ok
        if isinstance(want, (bool, tuple)):
            good = (got == want)
        else:
            good = abs(got-want) <= tol*abs(want)
        ok &= good
        fmt = (lambda v: str(v)) if isinstance(want, (bool, tuple)) else (lambda v: "%.6g" % v)
        g, w = fmt(got), fmt(want)
        print("  %-40s %18s %18s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Planck 2018 values reproduced")
    chk("H0 (s^-1)", H0(), 2.182989e-18, tol=1e-6)
    chk("Hubble time (Gyr)", hubble_time_gyr(), 14.515918, tol=1e-6)
    chk("Hubble radius (Gly)", hubble_radius_gly(), 14.515918, tol=1e-6)
    chk("  Hubble radius == Hubble time x c (identity)",
        hubble_radius_gly(), hubble_time_gyr(), tol=1e-12)
    # CORRECTED (DOCKET 67 follow-up): these three were pinned to the typed,
    # NAMED-NOT-READ 14.26 Gpc -- 46.509899 Gly, 3.204062 c, 3.371015.  They
    # are now pinned to the horizon COMPUTED from READ Planck inputs.
    chk("comoving particle horizon (Gpc), COMPUTED", horizon_gpc(), 14.151331, tol=1e-6)
    chk("comoving particle horizon (Gly)", horizon_gly(), 46.155467, tol=1e-6)
    chk("  integrator check: computed age vs READ 13.797 Gyr (2e-4)",
        abs(flat_lcdm()[1]/AGE_GYR - 1.0) < 2e-4, True)
    chk("  massless-neutrino variant = D67 auditor's 14.147 Gpc",
        round(flat_lcdm(m_nu_ev=0.0)[0], 3), 14.147, tol=0)
    chk("  converged: doubling the steps moves it < 1e-9",
        abs(flat_lcdm(n=8000)[0]/horizon_gpc() - 1.0) < 1e-9, True)
    chk("  the typed 14.26 is NOT the computed horizon (0.77% high)",
        round(HORIZON_GPC_TYPED/horizon_gpc() - 1.0, 4), 0.0077, tol=0)
    chk("  the horizon's status is COMPUTED, never PINNED",
        HORIZON_GPC_STATUS == "COMPUTED", True)

    print("\nMetric transport already exceeds c, in the observed universe")
    chk("recession at the horizon (c)", recession(horizon_gly()), 3.179645, tol=1e-6)
    chk("recession at the Hubble radius (c)", recession(hubble_radius_gly()), 1.0, tol=1e-12)
    chk("horizon / (c x age) -- light outrun by", transport_ratio(), 3.345326, tol=1e-6)
    chk("  superluminal at the horizon either way (typed or computed)",
        recession(horizon_gly()) > 1.0 and
        recession(HORIZON_GPC_TYPED*1e3*MPC/GLY) > 1.0, True)
    chk("recession is linear in distance (identity)",
        recession(20.0)/recession(10.0), 2.0, tol=1e-12)

    print("\nEnergy conditions of the expanding fluid")
    n, w_, s, d = conditions(0.0)
    chk("dust: NEC", n, True); chk("dust: WEC", w_, True)
    chk("dust: SEC", s, True); chk("dust: DEC", d, True)
    chk("radiation: all four", all(conditions(1.0/3.0)), True)
    chk("Lambda violates SEC only", conditions(-1.0), (True, True, False, True))
    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE SHARED HYPOTHESIS -- and the case already in the sky")
    print("="*78)
    print("""
Five of the eight bounds this project established assume ASYMPTOTIC FLATNESS:
CM-THEOREM, T2-ADM, SSV-NOGO, NO-TAPER and NO-PORTAL.  In an FLRW universe not
one of them is even statable -- there is no ADM mass, no ADM momentum, and
topological censorship loses its hypotheses.

That is the same shape of finding as CM-THEOREM itself.  There, every failure
shared the word ISOLATED, and dropping it opened the coupling family.  Here,
every failure shares ASYMPTOTICALLY FLAT, and the universe is not.

-- What is already measured ------------------------------------------------""")
    print("  Hubble radius            %8.3f Gly" % hubble_radius_gly())
    print("  comoving particle horizon %7.3f Gly   (COMPUTED, flat LCDM, Planck 2018 inputs)"
          % horizon_gly())
    print("  age of the universe      %8.3f Gyr" % AGE_GYR)
    print("  recession at the horizon %8.3f c" % recession(horizon_gly()))
    print("  horizon / (c x age)      %8.3f      <-- light outrun by this factor"
          % transport_ratio())
    print("""
  Objects beyond %.2f Gly recede faster than light, and the horizon recedes at
  %.2f c.  This is geodesic: comoving observers are in free fall and feel
  nothing.  There is no thrust, no exotic matter and no violation.
""" % (hubble_radius_gly(), recession(horizon_gly())))
    print("  %-24s %6s %6s %6s %6s %6s" % ("fluid","w","NEC","WEC","SEC","DEC"))
    for name, w in FLUIDS:
        n, we, s, d = conditions(w)
        f = lambda b: " ok " if b else "FAIL"
        print("  %-24s %6.3f %6s %6s %6s %6s" % (name, w, f(n), f(we), f(s), f(d)))
    print("""
  DUST SATISFIES ALL FOUR AND STILL EXPANDS SUPERLUMINALLY AT LARGE DISTANCE.
  Superluminal metric transport therefore requires NO energy-condition
  violation whatever.  It is not exotic, it is not hypothetical, and it is
  not rare -- it is the largest and best-measured thing there is.

-- Stated precisely, because this is where it would be easy to overclaim ----
  WHAT THIS SHOWS.  Metric transport at v > c, geodesic, zero felt
  acceleration, sourced by ordinary matter satisfying all four pointwise
  energy conditions, is OBSERVED.  Warp travel in that sense is not a
  conjecture and never was: TARGET-1 measured a local warp state, and
  cosmology measures the transport.

  WHAT THIS DOES NOT SHOW.  Dropping asymptotic flatness removes the PROOFS,
  not necessarily the OBSTRUCTION.  Five theorems become unstatable; that is
  not the same as their conclusions becoming false.  Nothing here exhibits a
  localized, steerable construction.

  AND THE SIGN IS WRONG.  Expansion SEPARATES.  Travel needs the opposite:
  contraction between here and there.  Nature does that too -- overdense
  regions decouple from the Hubble flow and collapse, with ordinary matter and
  no violation -- which is structure formation, and it is the same borrowed
  gradient the coupling family already exploits, written at cosmological scale.

-- Where this says to look --------------------------------------------------
  The question is no longer "can spacetime transport a payload superluminally
  without exotic matter", because the answer is measured and it is yes.  It is:

      CAN THAT MECHANISM BE LOCALIZED AND GIVEN THE OPPOSITE SIGN?

  Every no-go this project holds was proved in the wrong background.  That does
  not make them false, and it does make them silent on this question.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
