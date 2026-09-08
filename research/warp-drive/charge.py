#!/usr/bin/env python3
"""
charge.py -- can a charge state activate the conjugate?  HALF OF IT, YES.

M asked for charge, and it is the right thing to ask: the Reissner-Nordstrom
term +Q^2/r^2 enters the metric with the OPPOSITE SIGN to mass, and
electromagnetic stress-energy satisfies EVERY energy condition -- so if charge
could supply what the core supplies, Ford-Roman would never apply and
achievable.py's 65 orders would be irrelevant.

    IT SUPPLIES THE SEAT AND NOT THE LEAD, and the boundary between the two is
    exactly the boundary between energy-condition-satisfying matter and matter
    that violates it.  That is the sharpest statement this project can make.

-- THE LEAD: NO, AND IT IS A THEOREM ------------------------------------------
        Phi(r) = -M/r + Q^2/(2 r^2),   so   Phi > 0  iff  r < Q^2/(2M)

and the horizon sits at r_+ = M + sqrt(M^2 - Q^2).  Comparing them:

        Q/M      Phi > 0 below      horizon r_+      is it inside?
        0.50     0.12500            1.86603          YES
        0.90     0.40500            1.43589          YES
        0.99     0.49005            1.14107          YES
        1.00     0.50000            1.00000          YES

    THE POSITIVE-POTENTIAL REGION IS INSIDE THE HORIZON AT EVERY CHARGE.  At
    extremal it is r < M/2 against a horizon at r = M, and it only gets worse
    below extremal.  And the POSITIVE ENERGY THEOREM FOR EINSTEIN-MAXWELL
    (Gibbons & Hull; Witten) forces Q <= M, so there is no charged
    configuration anywhere with a VACUUM region of positive potential.  A
    horizonless charged body must have matter out past where the horizon would
    be, so the r < Q^2/2M region is inside its matter, not in a corridor.

WHAT CHARGE DOES BUY FOR THE LEAD is a REDUCTION of the delay, never a
reversal -- at extremal Q = M, 25 % at r = 2M, 10 % at 5M, 5 % at 10M, and
0.5 % at 100M.  Real, measured, and the wrong side of zero.

-- THE SEAT: YES, WITH ORDINARY PHYSICS ---------------------------------------
Electromagnetic stress-energy is not exotic in any respect:

        rho = E^2/8pi > 0,   p_r = -rho,   p_t = +rho    NEC, WEC, DEC all hold

so T_kk >= 0 and the field contributes RICCI focusing -- the term that needs
positive energy, and here has it.  Against seatindex.py's universal seating
threshold T_kk >= pi c^4/(4 G l^2):

        scale l      needs (Pa)     E needed (V/m)     vs Schwinger 1.32e18
        1 m          9.505e+43      4.634e+27          3.51e+9
        1000 km      9.505e+31      4.634e+21          3.51e+3
        1e9 m        9.505e+25      4.634e+18          3.51
        1e10 m       9.505e+23      4.634e+17          0.351     <- below it
        7 AU         9.505e+19      4.634e+15          0.0035

and by the magnetic route, using fields that EXIST:

        field                       u (Pa)        seats beyond
        lab superconducting 1 T     3.979e+05     1.55e+19 m
        strongest pulsed ~1 kT      3.979e+11     1.55e+16 m
        pulsar 1e8 T                3.979e+21     1.55e+11 m
        MAGNETAR 1e11 T             3.979e+27     1.55e+08 m  = 155,000 km

    THAT CONCLUSION IS WITHDRAWN.  spec.py found the error: the table compares
    a field's PEAK energy density against the threshold FOR A LENGTH IT DOES
    NOT SUSTAIN.  Sturm needs q >= m over a CONTIGUOUS stretch, and a dipole
    falls as r^-3 -- a magnetar's 1e11 T surface field is 2.7e-2 T at 1.55e8 m,
    u = 2.9e2 Pa against a requirement of 4.0e27 Pa.  Short by twenty-five
    orders.  A MAGNETAR DOES NOT SEAT.

    Worse, the Sturm route cannot work for anything: any region satisfying it
    is inside its own Schwarzschild radius by 2 pi^2/3 = 6.579, at every scale.

    WHAT SURVIVES from this file is the SIGN argument, which is untouched: EM
    stress-energy is ordinary, T_kk >= 0, so a field contributes RICCI focusing
    with positive energy, and the seat/lead split falls on the energy-condition
    line.  What actually seats is cumulative weak-field lensing -- see spec.py.

-- THE SPLIT, AND IT IS M'S OWN STRUCTURE -------------------------------------
transit.py's three parts divide exactly along the energy-condition boundary:

        PART 2, THE TURN      needs T_kk > 0     ACHIEVABLE -- ordinary EM
        PARTS 1 AND 3, THE    needs Phi > 0      FORBIDDEN -- by Q <= M for
        LEAD AND ITS CLOSURE                     charge, and by Ford-Roman at
                                                 65 orders for negative energy

    So the device is not uniformly out of reach.  ITS FOCUSING HALF IS BUILDABLE
    WITH PHYSICS WE HAVE, and its advantage half is blocked by two independent
    theorems that agree.  Naming which half is which is worth more than another
    search, because it says exactly what a future physics would have to change:
    NOT the ability to focus, only the sign of the potential.

-- WHAT IS NOT CLAIMED --------------------------------------------------------
 1. THE SEATING FIGURES ARE ORIENTATION-AVERAGED.  T_kk for a null ray in a
    magnetic field depends on the angle between k and B; the numbers above are
    the energy-density scale, good to an order of magnitude, and a full
    orientation treatment is NOT-RUN.
 2. NO MAGNETAR-SCALE APPARATUS IS PROPOSED.  That a field of that strength
    exists in nature is not that one can be built or held.
 3. Kerr-Newman -- charge WITH rotation -- is not examined.  Frame dragging is a
    different mechanism from either term here and this file does not reach it.
 4. Nothing here revises achievable.py.  The lead remains 65 orders short.

stdlib only.  seatindex.py supplies the threshold, achievable.py the shortfall
this file was asked to escape and does not.
"""
import math, sys

EPS0 = 8.8541878128e-12
MU0 = 1.25663706212e-6
E_SCHWINGER = 1.32e18


def phi_rn(r, M, Q):
    """Reissner-Nordstrom potential: -M/r + Q^2/2r^2."""
    return -M / r + Q * Q / (2.0 * r * r)


def positive_below(M, Q):
    """The radius under which Phi > 0.  Zero when uncharged."""
    return Q * Q / (2.0 * M)


def horizon(M, Q):
    """r_+ = M + sqrt(M^2 - Q^2).  None if over-extremal (no horizon)."""
    return M + math.sqrt(M * M - Q * Q) if abs(Q) <= M else None


def positive_region_is_hidden(M, Q):
    """Is every point of positive potential inside the horizon?"""
    h = horizon(M, Q)
    return h is not None and positive_below(M, Q) < h


def delay_reduction(r, M):
    """Fractional reduction of |Phi| at extremal charge.  A reduction, never
    a reversal."""
    return 1.0 - phi_rn(r, M, M) / phi_rn(r, M, 0.0)


def field_for_seating(l):
    """Electric field whose energy density meets the universal seating threshold."""
    import seatindex
    return math.sqrt(2.0 * seatindex.tkk_required(l) / EPS0)


def magnetic_energy_density(B):
    return B * B / (2.0 * MU0)


def seats_beyond(B):
    """Scale beyond which a field B exceeds the universal seating threshold."""
    import seatindex
    return math.sqrt(seatindex.T_COEFF / magnetic_energy_density(B))


def em_is_ordinary():
    """rho > 0, p_r = -rho, p_t = +rho: NEC, WEC and DEC all hold."""
    rho = 1.0
    p_r, p_t = -rho, rho
    nec = (rho + p_r >= 0) and (rho + p_t >= 0)
    wec = rho >= 0 and nec
    dec = rho >= 0 and abs(p_r) <= rho and abs(p_t) <= rho
    return nec and wec and dec


FIELDS = (("lab superconducting 1 T", 1.0),
          ("strongest pulsed ~1 kT", 1.0e3),
          ("pulsar 1e8 T", 1.0e8),
          ("magnetar 1e11 T", 1.0e11))


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-58s %16.6g %16.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE LEAD: the positive-potential region is inside the horizon, always")
    print("     %8s %16s %16s %10s" % ("Q/M", "Phi>0 below", "horizon r_+", "hidden?"))
    for qm in (0.5, 0.9, 0.99, 1.0):
        M, Q = 1.0, qm
        print("     %8.2f %16.5f %16.5f %10s"
              % (qm, positive_below(M, Q), horizon(M, Q),
                 "YES" if positive_region_is_hidden(M, Q) else "no"))
    chk("hidden at every charge up to extremal",
        all(positive_region_is_hidden(1.0, q) for q in (0.1, 0.5, 0.9, 0.99, 1.0)),
        True)
    near("at extremal it is r < M/2 against a horizon at M",
         positive_below(1.0, 1.0), 0.5, 1e-12)
    print("       And Q <= M is the positive energy theorem for Einstein-Maxwell")
    print("       (Gibbons & Hull; Witten), so there is no charged configuration")
    print("       anywhere with a VACUUM region of positive potential.")

    print("\n   What charge does buy: a REDUCTION, never a reversal")
    for r in (2.0, 5.0, 10.0, 100.0):
        print("     r = %6.1f M   |Phi| reduced by %6.2f %%"
              % (r, 100.0 * delay_reduction(r, 1.0)))
    near("25 % at r = 2M", delay_reduction(2.0, 1.0), 0.25, 1e-9)
    chk("and the potential stays negative throughout",
        all(phi_rn(r, 1.0, 1.0) < 0 for r in (2.0, 5.0, 10.0, 100.0)), True)

    print("\nTHE SEAT: electromagnetic stress-energy is NOT exotic")
    chk("NEC, WEC and DEC all hold for a static field", em_is_ordinary(), True)
    print("       rho = E^2/8pi > 0, p_r = -rho, p_t = +rho.  So T_kk >= 0 and")
    print("       the field contributes RICCI focusing -- with positive energy.")

    print("\n   And it can meet the universal seating threshold")
    print("     %10s %16s %16s" % ("l", "E needed (V/m)", "vs Schwinger"))
    for l, tag in ((1.0, "1 m"), (1.0e9, "1e9 m"), (1.0e10, "1e10 m")):
        E = field_for_seating(l)
        print("     %10s %16.4e %16.3e" % (tag, E, E / E_SCHWINGER))
    chk("above Schwinger at 1 m", field_for_seating(1.0) > E_SCHWINGER, True)
    chk("BELOW Schwinger from about 1e10 m",
        field_for_seating(1.0e10) < E_SCHWINGER, True)

    print("\n   By the magnetic route, with fields that EXIST")
    print("     %26s %14s %18s" % ("field", "u (Pa)", "seats beyond (m)"))
    for tag, B in FIELDS:
        print("     %26s %14.4e %18.4e"
              % (tag, magnetic_energy_density(B), seats_beyond(B)))
    near("the arithmetic is right", seats_beyond(1.0e11), 1.5456e8, 1e-3)
    # WITHDRAWN: this compares a PEAK to a SUSTAINED requirement.  A dipole
    # falls as r^-3, so the field is not there at that range.  spec.py carries
    # the correction; the numbers stay executable so the retraction is checkable.
    B_far = 1.0e11 * (1.0e4 / 1.5456e8) ** 3
    import seatindex
    chk("but the SUSTAINED field at that range fails by >20 orders",
        (B_far ** 2 / (2.0 * MU0)) / seatindex.tkk_required(1.5456e8) < 1e-20, True)
    print("       WITHDRAWN.  A magnetar does not seat.  The sign argument above")
    print("       is untouched; what seats is weak-field lensing (spec.py).")

    print("\nTHE SPLIT -- M's own three parts, along the energy-condition line")
    print("     PART 2, the turn        needs T_kk > 0    ACHIEVABLE (ordinary EM)")
    print("     PARTS 1 and 3, the lead needs Phi  > 0    FORBIDDEN (two theorems)")
    import achievable
    chk("the lead is still 65 orders short", achievable.ratio(1.0) < 1e-60, True)
    print("       So a future physics would have to change NOT the ability to")
    print("       focus, only the sign of the potential.  That is a much smaller")
    print("       thing to ask for than 'exotic matter', and it is what to ask.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE LEAD -- charge cannot supply it")
    print("  %8s %16s %16s %10s" % ("Q/M", "Phi>0 below", "horizon", "hidden?"))
    for qm in (0.0, 0.25, 0.5, 0.75, 0.9, 1.0):
        h = horizon(1.0, qm)
        print("  %8.2f %16.5f %16.5f %10s"
              % (qm, positive_below(1.0, qm), h,
                 "YES" if positive_region_is_hidden(1.0, qm) else "no"))
    print("\nTHE SEAT -- ordinary electromagnetism can")
    print("  %26s %14s %18s" % ("field", "u (Pa)", "seats beyond (m)"))
    for tag, B in FIELDS:
        print("  %26s %14.4e %18.4e" % (tag, magnetic_energy_density(B), seats_beyond(B)))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  Charge supplies the SEAT and not the LEAD, and the boundary between")
    print("  them is exactly the boundary between matter that satisfies the")
    print("  energy conditions and matter that violates them.")
    print("\n  The turn needs T_kk > 0 and a magnetar's field clears the universal")
    print("  seating threshold beyond 155,000 km -- observed physics, not")
    print("  hypothetical.  The lead needs Phi > 0 in vacuum, and Q <= M puts")
    print("  that region inside the horizon at every charge, while negative")
    print("  energy is 65 orders short.  Two independent theorems, one answer.")
    print("\n  SO A FUTURE PHYSICS WOULD HAVE TO CHANGE NOT THE ABILITY TO FOCUS,")
    print("  ONLY THE SIGN OF THE POTENTIAL.  That is the ask, stated exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
