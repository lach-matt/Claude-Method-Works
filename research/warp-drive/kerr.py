#!/usr/bin/env python3
"""
kerr.py -- NO-TAPER was too strong, and Kerr is the counterexample.

GATE-CLOSED.md measured that a shift bump on a Minkowski background needs
Hawking-Ellis Type IV stress-energy in every cell, and concluded

    "a shift cannot terminate in vacuum".

That is too strong, and a textbook solution refutes it.  KERR has

    g_tphi != 0 everywhere outside the horizon, and T_mn = 0 everywhere
    outside the horizon.

A vacuum shift, dragging the local inertial frame at HALF THE SPEED OF LIGHT at
the horizon of a near-extremal hole, with all four energy conditions holding
trivially because there is nothing there to violate them.

THE CORRECT STATEMENT.  My test bump was tanh-tapered -- COMPACTLY SUPPORTED to
machine precision.  Kerr's shift is not: omega ~ 1/r^3, decaying forever and
reaching zero only at infinity.  So:

    a shift cannot be COMPACTLY SUPPORTED in vacuum.
    a shift CAN decay asymptotically in vacuum.

WHAT THAT COSTS.  A vacuum shift is not free: it is tied to a CONSERVED CHARGE
of the source -- angular momentum for the rotational shift (g_tphi ~ GJ/c^3 r),
linear momentum for the translational one (g_ti ~ GP_i/c^3 r).  You cannot have
a shift without J or P.

AND HERE IS THE OPENING.  CM-THEOREM forbids an isolated system manufacturing
linear momentum.  IT SAYS NOTHING ABOUT ANGULAR MOMENTUM.  Spinning is not
translating.  The one charge this project proved unmanufacturable is P; the
charge that sources the strongest known vacuum shift is J.

stdlib only.
"""
import math, sys

c, G, MSUN = 299792458.0, 6.67430e-11, 1.98892e30

# Boyer-Lindquist, geometric units G = c = M = 1; a is the spin parameter a/M.
def r_plus(a):
    return 1.0 + math.sqrt(max(1.0-a*a, 0.0))

def r_ergo(a, th=math.pi/2):
    return 1.0 + math.sqrt(max(1.0 - a*a*math.cos(th)**2, 0.0))

def omega(r, a, th=math.pi/2):
    """Frame-dragging angular velocity of a zero-angular-momentum observer."""
    D = r*r - 2.0*r + a*a
    A = (r*r + a*a)**2 - a*a*D*math.sin(th)**2
    return 2.0*a*r/A

def omega_horizon(a):
    """Angular velocity of the horizon itself, a/(2 r_+)."""
    return a/(2.0*r_plus(a))

def v_drag(r, a):
    """omega * r, in units of c: the speed the local frame is dragged."""
    return omega(r, a)*r

def irreducible_fraction(a):
    """M_irr/M = sqrt((1+sqrt(1-a^2))/2)."""
    return math.sqrt((1.0+math.sqrt(max(1.0-a*a, 0.0)))/2.0)

def rotational_energy_fraction(a):
    """(M - M_irr)/M: the fraction of the hole's mass that is extractable spin."""
    return 1.0 - irreducible_fraction(a)

PENROSE_MAX_GAIN = (math.sqrt(2.0)-1.0)/2.0   # 20.7%, single-event classic bound

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-9):
        nonlocal ok
        good = (got == want) if isinstance(want, bool) else abs(got-want) <= tol*abs(want)
        g = got if isinstance(want, bool) else "%.8g" % got
        w = want if isinstance(want, bool) else "%.8g" % want
        ok &= good
        print("  %-50s %14s %14s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("Kerr horizons and the ergosphere")
    chk("r_+ for a=0 is 2M (Schwarzschild)", r_plus(0.0), 2.0)
    chk("r_+ for extremal a=1 is M", r_plus(1.0), 1.0)
    chk("equatorial ergosphere is 2M for ALL spins", r_ergo(0.998), 2.0)
    chk("  and for a=0.5 too (identity)", r_ergo(0.5), r_ergo(0.998))
    chk("no dragging without spin (identity)", omega(5.0, 0.0), 0.0)

    print("\nThe vacuum shift -- the counterexample to NO-TAPER")
    chk("v_drag at the horizon, a=0.998", v_drag(r_plus(0.998), 0.998), 0.499, tol=2e-3)
    chk("v_drag -> 0.5 c as a -> 1", v_drag(r_plus(0.9999), 0.9999), 0.5, tol=1e-3)
    chk("Omega_H for extremal is 1/(2M)", omega_horizon(1.0), 0.5)
    # the falloff: omega r^3 -> 2 a M, which is why it is NOT compactly supported
    chk("omega r^3 -> 2a at large r (identity)", omega(3000.0, 0.998)*3000.0**3,
        2.0*0.998, tol=1e-5)
    chk("  still nonzero at r = 10^6 M", omega(1e6, 0.998) > 0.0, True)

    print("\nWhat the spin stores, and what is extractable")
    chk("M_irr/M for extremal is 1/sqrt(2)", irreducible_fraction(1.0), 1.0/math.sqrt(2.0))
    # exact closed forms -- compare to the form, not to a truncated decimal
    chk("extractable fraction is 1 - 1/sqrt(2)", rotational_energy_fraction(1.0),
        1.0 - 1.0/math.sqrt(2.0), tol=1e-15)
    chk("nothing extractable at a=0 (identity)", rotational_energy_fraction(0.0), 0.0)
    chk("Penrose max gain is (sqrt(2)-1)/2", PENROSE_MAX_GAIN,
        (math.sqrt(2.0)-1.0)/2.0, tol=1e-15)
    chk("  and equals 1/sqrt(2) - 1/2 (identity)", PENROSE_MAX_GAIN,
        1.0/math.sqrt(2.0) - 0.5, tol=1e-15)
    E10 = rotational_energy_fraction(1.0)*10*MSUN*c**2
    chk("10 Msun extremal spin energy (J)", E10, 5.2356e47, tol=1e-4)
    chk("  vs the gate's built reservoir 1.17e46 J", E10/1.17e46, 44.749, tol=1e-3)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("KERR -- the vacuum shift, and the charge this project never checked")
    print("="*78)
    print("""
GATE-CLOSED.md concluded "a shift cannot terminate in vacuum" from a measurement
that was correct and a generalisation that was not.  Kerr refutes it: g_tphi is
nonzero everywhere outside the horizon and T_mn is zero everywhere outside the
horizon.  A vacuum shift, and the energy conditions hold trivially.

The measured bump was TANH-TAPERED -- compactly supported to machine precision.
Kerr's shift decays as 1/r^3 and never reaches zero at finite radius.  Corrected:

    a shift cannot be COMPACTLY SUPPORTED in vacuum   <- what was measured
    a shift CAN decay asymptotically in vacuum        <- what Kerr proves
""")
    print("  %-8s %8s %8s %10s %12s %12s" %
          ("a/M","r_+","r_ergo","Omega_H","v_drag(r+)","v_drag(3M)"))
    for a in (0.0, 0.5, 0.9, 0.99, 0.998, 0.9999):
        print("  %-8.4f %8.4f %8.4f %10.5f %12.5f %12.5f" %
              (a, r_plus(a), r_ergo(a), omega_horizon(a),
               v_drag(r_plus(a), a), v_drag(3.0, a)))
    print("""
  Inside the ergosphere NO STATIC OBSERVER EXISTS.  Everything is dragged, and
  at a near-extremal horizon the drag is half the speed of light.  This is the
  strongest warp field known, it is made of nothing, and it is common.

-- What a vacuum shift costs -----------------------------------------------
  It is tied to a CONSERVED CHARGE of the source:

      rotational      g_tphi ~ -2GJ sin^2(th)/(c^3 r)     omega ~ 1/r^3
      translational   g_ti   ~ -4GP_i/(c^3 r)             ~ 1/r

  So there is no shift without J or P -- and that is the whole reason a
  manufactured bubble needs exotic matter.  It has neither.

-- The charge this project never checked -----------------------------------
  CM-THEOREM: an isolated system cannot manufacture LINEAR MOMENTUM.  Proved,
  measured, and it killed the drive, the launcher and the gate.

  IT SAYS NOTHING ABOUT ANGULAR MOMENTUM.  Spinning is not translating, and the
  charge that sources the strongest vacuum shift in nature is J, not P.
""")
    print("  %-8s %14s %16s" % ("a/M","E_rot/Mc^2","10 Msun (J)"))
    for a in (0.5, 0.9, 0.99, 0.998, 1.0):
        f = rotational_energy_fraction(a)
        print("  %-8.3f %14.5f %16.4e" % (a, f, f*10*MSUN*c**2))
    E10 = rotational_energy_fraction(1.0)*10*MSUN*c**2
    print("""
  Penrose extracts it GEODESICALLY: a body falls in, releases ballast inside the
  ergosphere, and the remainder escapes with more energy than it arrived with --
  up to %.1f%% more in a single event.  The only non-geodesic moment is letting
  go of the ballast.

  Against this project's own ledger:
      gate circulation reservoir          1.17e46 J   BUILT, 26.7 Myr of accretion
      10 Msun extremal Kerr spin energy   %.3e J   ALREADY THERE
      ratio                               %.1fx

-- What this does and does not resurrect -----------------------------------
  DOES NOT resurrect the gate as a directed launcher.  Rotational dragging is
  CIRCULAR: it points nowhere, so it cannot aim a payload at a destination.

  DOES supply the two things the surviving design was missing.  The coupling
  family needs a MOVING WELL, and the deepest wells available also SPIN --
  so the deflectors in THE-ENGINE.md should be Kerr, not Schwarzschild.  Zhang
  says so explicitly and set it aside: a fast-spinning hole should increase the
  gain per slingshot and help prevent capture, and he did not pursue it.

  So the correction to my own error points at a specific, unexplored improvement
  to the one architecture still standing.
""" % (100*PENROSE_MAX_GAIN, E10, E10/1.17e46))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
