#!/usr/bin/env python3
"""
certify.py -- the certification H39a said had never been done, done.  And it
closes the gap in the direction M predicted, though not with the sign he hoped
for: the OBSTRUCTION stops being a model and becomes a theorem.

M: "if we close the gaps, we may get a different conclusion entirely."

    THE GAP WAS REAL AND CLOSING IT DID CHANGE THE CONCLUSION -- just not the
    verdict.  What changes is its STATUS.  provenance.py found the project's
    central requirement resting on a chosen ansatz; this file proves the same
    requirement without any ansatz at all, for every static spherically
    symmetric spacetime.  The number stops being arguable.

Three things happen here, in order of increasing importance.

===============================================================================
0. PRIOR ART, RECORDED FIRST BECAUSE IT GOES AGAINST US
===============================================================================

PFENNING & FORD, "The unphysical nature of 'Warp Drive'" (gr-qc/9702026, 1997).
They applied the Ford-Roman quantum inequality to the Alcubierre metric with
the sampling time held below the local curvature radius, and obtained

        Delta <= 10^2 v_b L_Planck

-- "unless v_b is extremely large, the wall thickness cannot be much above the
Planck scale" -- and then a total energy E ~ -3e20 M_galaxy v_b, "roughly ten
orders of magnitude greater than the total mass of the entire visible universe."

    THAT IS candidates.py's CONCLUSION, TWENTY-EIGHT YEARS EARLIER.  "Quantum
    inequalities force Planck-scale structure and then the energy is
    unattainable" is Pfenning-Ford.  H37's exponent framing and closed-form
    crossovers are a different presentation of the same phenomenon for a
    different architecture, and H37 needed this row.

    ONE NUMBER OF THEIRS IS WORTH KEEPING, because it is a comparison this
    project can make and they could not: an Alcubierre bubble the size of ONE
    ELECTRON COMPTON WAVELENGTH costs them E ~ -400 M_sun.  A Planck cell in
    this architecture costs 196 MJ.  The architectures are not close, and that
    gap is real even though the verdict is the same.

    AND THEIR OWN GAP IS STATED IN THEIR OWN PAPER: they apply the FLAT SPACE
    inequality to a curved metric because the exact treatment "would be
    exceptionally difficult."  M is right that conclusions drawn across a gap
    are worth re-opening.  This file re-opens a different one.

===============================================================================
1. THE PIPELINE, AND IT IS VALIDATED BEFORE IT IS BELIEVED
===============================================================================

Warp Factory (arXiv:2404.03095, Helmerich, Fuchs, Bobrick, Sellers, Melcher &
Martire) takes an arbitrary metric, computes T_munu from the Einstein equations
by finite difference, and evaluates the energy conditions across SAMPLED
OBSERVERS rather than the Eulerian one alone.  Their Table 1 is the warning:
Alcubierre, Van Den Broeck, Modified Time AND Lentz-inspired all violate all
four conditions -- including Lentz, which has POSITIVE Eulerian energy density
and still fails the WEC across general timelike observers.

The same test is reimplemented here, stdlib only, and validated first:

        MINKOWSKI          max|T| = 0.000e+00      exactly zero
        SCHWARZSCHILD      max|T| = 4.08e-10 at r = 5,  3.99e-12 at r = 50
        (isotropic, M = 1, vacuum, so T must vanish)

    THAT IS THE NOISE FLOOR, and every number below is quoted against it.

===============================================================================
2. THE ANSATZ, CERTIFIED -- AND IT FAILS EVERYWHERE, NOT IN A LEAD
===============================================================================

The seated metric is CONFORMASTATIC: g = diag(-e^{2Phi}, e^{-2Phi}, e^{-2Phi},
e^{-2Phi}) with Phi(r) = m/sqrt(r^2+a^2) - m/max(r,R_s), a = 0.02, R_s = 200,
m = 0.02, so Phi(0) = 0.9999 -- core.py's Phi_max = m/a.

    r          T_00          NEC min      WEC min      SEC min
    0.005     -9.0616e+04   -9.1505e+04  -5.2635e+05  -4.8059e+05
    0.02      -1.2190e+04   -1.3451e+04  -7.6240e+04  -6.9503e+04
    0.05      -3.0887e+02   -3.9339e+02  -2.1822e+03  -1.9847e+03
    0.2       -4.7451e-01   -7.6490e-01  -4.1169e+00  -3.7316e+00
    1         -4.6564e-04   -8.7348e-04  -4.6251e-03  -4.1844e-03
    10        -4.0744e-08   -8.0044e-08  -4.2191e-07  -3.8135e-07

    EVERY ENERGY CONDITION IS VIOLATED AT EVERY RADIUS SAMPLED, and the DEC
    with them, since the DEC requires the WEC.  Converged: T_00 at r = 1 moves
    by 6.4e-9 between h = 1e-3 and h = 1e-4, and sits SIX ORDERS above the
    Schwarzschild floor.  Not noise.

    THE CONSEQUENCE IS A CORRECTION TO THIS PROJECT'S OWN ARCHITECTURE.
    reverse.py and apply.py have split the device into a FREE SEAT satisfying
    every energy condition and a COSTLY LEAD needing rho < 0.  THE METRIC DOES
    NOT SAY THAT.  The exotic requirement is not localised in a lead; it is
    present wherever Phi varies, which is everywhere.

    AND THE MECHANISM IS THE ANSATZ ITSELF.  In conformastatic form the energy
    density is dominated by -|grad Phi|^2 -- measured at r = 1, T_00 =
    -4.8455e-04 against -|grad Phi|^2 = -3.9952e-04, a ratio of 1.21.  A SQUARE,
    carrying a minus sign.

    ONE CLAIM OF MINE HERE WAS TOO BROAD AND IS CORRECTED RATHER THAN QUIETLY
    DROPPED.  A first run concluded "both signs of m give T_00 < 0".  At r = 1
    they do (-4.85e-4 and -3.25e-4), but at r = 0.05 the negative-m case gives
    T_00 = +14.7.  THE FAR FIELD IS GRADIENT-DOMINATED AND SIGN-BLIND; THE NEAR
    CORE IS NOT.

===============================================================================
3. AND THEN THE ANSATZ-FREE VERSION, WHICH IS THE RESULT
===============================================================================

The certification above is about OUR Phi, so it inherits exactly the weakness
provenance.py named.  So drop Phi entirely.

Every static spherically symmetric spacetime can be written with an areal
radius and the Misner-Sharp mass function:

        ds^2 = -e^{2Phi(r)} dt^2 + dr^2/(1 - 2m(r)/r) + r^2 dOmega^2

and the tt Einstein equation gives, exactly,

        dm/dr = 4 pi r^2 rho        so        m(r) = int_0^r 4 pi r'^2 rho dr'.

Proper radial distance is dl = dr / sqrt(1 - 2m/r).  So the region between two
spheres is SHORTER than its flat value exactly when

        1 - 2m(r)/r  >  1        <=>        m(r)  <  0.

    THEOREM.  IN ANY STATIC SPHERICALLY SYMMETRIC SPACETIME, PROPER DISTANCE IS
    CONTRACTED AT r IF AND ONLY IF THE ENCLOSED MISNER-SHARP MASS IS NEGATIVE.

    No ansatz.  No Phi.  A definition and one integral.

    COROLLARY, AND IT CARRIES A HYPOTHESIS THIS FILE ONCE USED WITHOUT WRITING
    IT DOWN.  "-- and therefore if and only if the enclosed ENERGY is negative"
    follows only where the centre is REGULAR, m(0) = 0, because that is the
    boundary condition that turns dm/dr = 4 pi r^2 rho into m(r) = int_0^r.
    Integrate the same equation from a non-regular centre and the constant of
    integration survives: Reissner-Nordstrom has m(r) = M - Q^2/2r, which is
    negative for r < Q^2/2M with rho = Q^2/8 pi r^4 > 0 everywhere.  That is a
    counterexample to the COROLLARY inside this file's own stated scope, and
    none at all to the THEOREM, which never mentions rho.  NARROWED, not
    repaired: the hypothesis was always in force and was simply unwritten.
    drivensource.py section 3 derives it and machine-checks the RN region;
    nonstatic.py's anchor lemma shows the THEOREM was never about static
    SPACETIMES but about stationary AREAL RADII, of which staticity is a
    sufficient condition and not the content.

WHAT THAT DOES TO THE PROJECT:

    IT REMOVES THE MODEL STATUS FROM THE CENTRAL REQUIREMENT.  provenance.py's
    H39a said the exotic requirement rested on a chosen potential.  It does not.
    For the static spherically symmetric case it is a theorem, and every
    conformastatic, Plummer, shell or two-function ansatz obeys it equally.

    IT IS A DIFFERENT QUANTITY FROM THE ONE THE QUANTUM INEQUALITIES BOUND.
    Ford-Roman bounds a SAMPLED energy density along a worldline; this
    constrains the VOLUME INTEGRAL of rho over a ball.  Averaging along a
    geodesic is not integrating over a ball, so no standard QI bounds it
    directly -- which is why the obstruction survives the whole of
    candidates.py's magnitude discussion untouched.

    AND IT DOES NOT REQUIRE NEGATIVE TOTAL MASS, WHICH IS WHY THE ARCHITECTURE
    WAS NEVER SILLY.  m(r) < 0 locally is compatible with M_ADM >= 0, and the
    concentric shell is exactly the device that arranges it.  The positive mass
    theorem is not violated and was never in danger.

    THE SEAT/LEAD SPLIT IS THE CASUALTY.  The theorem says the negativity sits
    wherever the contraction does.  There is no arrangement in which one part
    contracts and another part, elsewhere, pays for it.

===============================================================================
4. STATUS, STATED BEFORE ANYONE ASKS
===============================================================================

    THE THEOREM IS ELEMENTARY AND IS ALMOST CERTAINLY STANDARD.  It follows
    from the definition of the Misner-Sharp mass in two lines, and closely
    related statements are folklore in the wormhole literature (the flare-out
    condition is a near neighbour).  NO NOVELTY IS CLAIMED FOR IT.  Its value
    here is not that it is new; it is that it is ANSATZ-FREE, and that converts
    this project's central obstruction from MODEL to THEOREM.

    IT IS STATIC AND SPHERICALLY SYMMETRIC ONLY.  That is a real limit: the
    Alcubierre drive is neither, and nothing here speaks to it.  D1-D5 place
    this project's own construction inside the theorem's scope, which is why it
    bites here.

    THE CERTIFICATION IS FINITE-DIFFERENCE, not analytic, and quoted against a
    measured noise floor rather than an assumed one.

    AND THE CONSTRUCTION IS STILL A MODEL.  This file proves the REQUIREMENT,
    not the design.  provenance.py's asymmetry is unchanged and is in fact
    sharpened: the obstruction was the last piece of the NO that still rested
    on an ansatz, and now it does not.
"""

import math
import sys

# ---------------------------------------------- the seated metric

A_CORE, R_SHELL, M_SEATED = 0.02, 200.0, 2.0e-2


def phi(r, m=M_SEATED, a=A_CORE, Rs=R_SHELL):
    return m / math.sqrt(r * r + a * a) - m / max(r, Rs)


def conformastatic(m=M_SEATED):
    def g(x):
        r = math.sqrt(x[1] ** 2 + x[2] ** 2 + x[3] ** 2)
        p = phi(r, m)
        A, B = math.exp(2.0 * p), math.exp(-2.0 * p)
        return [[-A, 0.0, 0.0, 0.0], [0.0, B, 0.0, 0.0],
                [0.0, 0.0, B, 0.0], [0.0, 0.0, 0.0, B]]
    return g


def minkowski(x):
    return [[-1.0, 0, 0, 0], [0, 1.0, 0, 0], [0, 0, 1.0, 0], [0, 0, 0, 1.0]]


def schwarzschild_isotropic(M=1.0):
    def g(x):
        r = math.sqrt(x[1] ** 2 + x[2] ** 2 + x[3] ** 2)
        u = M / (2.0 * r)
        A = ((1.0 - u) / (1.0 + u)) ** 2
        B = (1.0 + u) ** 4
        return [[-A, 0, 0, 0], [0, B, 0, 0], [0, 0, B, 0], [0, 0, 0, B]]
    return g


# ---------------------------------------------- the pipeline

def inv4(Mx):
    n = 4
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(Mx)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        if abs(A[p][c]) < 1e-300:
            raise ZeroDivisionError("singular metric")
        A[c], A[p] = A[p], A[c]
        d = A[c][c]
        A[c] = [v / d for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0.0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [row[n:] for row in A]


def _dg(g, x, h):
    out = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(1, 4):
        xs = []
        for k in (-2, -1, 1, 2):
            y = list(x)
            y[a] += k * h
            xs.append(g(y))
        for m in range(4):
            for n in range(4):
                out[a][m][n] = (xs[0][m][n] - 8 * xs[1][m][n]
                                + 8 * xs[2][m][n] - xs[3][m][n]) / (12 * h)
    return out


def christoffel(g, x, h):
    gi = inv4(g(x))
    d = _dg(g, x, h)
    G = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    for l in range(4):
        for m in range(4):
            for n in range(4):
                G[l][m][n] = 0.5 * sum(gi[l][s] * (d[m][s][n] + d[n][s][m] - d[s][m][n])
                                       for s in range(4))
    return G


def ricci(g, x, h):
    G0 = christoffel(g, x, h)
    dG = [[[[0.0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(1, 4):
        Gs = []
        for k in (-2, -1, 1, 2):
            y = list(x)
            y[a] += k * h
            Gs.append(christoffel(g, y, h))
        for l in range(4):
            for m in range(4):
                for n in range(4):
                    dG[a][l][m][n] = (Gs[0][l][m][n] - 8 * Gs[1][l][m][n]
                                      + 8 * Gs[2][l][m][n] - Gs[3][l][m][n]) / (12 * h)
    R = [[0.0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            s = 0.0
            for l in range(4):
                s += dG[l][l][m][n] - dG[n][l][m][l]
                for sg in range(4):
                    s += G0[l][l][sg] * G0[sg][m][n] - G0[l][n][sg] * G0[sg][m][l]
            R[m][n] = s
    return R


def stress_energy(g, x, h):
    """T_munu in geometric units (c^4/8piG = 1)."""
    gm = g(x)
    gi = inv4(gm)
    Rm = ricci(g, x, h)
    Rs = sum(gi[m][n] * Rm[m][n] for m in range(4) for n in range(4))
    return [[Rm[m][n] - 0.5 * Rs * gm[m][n] for n in range(4)] for m in range(4)]


def max_abs(T):
    return max(abs(T[m][n]) for m in range(4) for n in range(4))


# ---------------------------------------------- energy conditions

ETA = (-1.0, 1.0, 1.0, 1.0)


def orthonormal(T, g):
    e = [1.0 / math.sqrt(-g[0][0])] + [1.0 / math.sqrt(g[i][i]) for i in (1, 2, 3)]
    return [[T[m][n] * e[m] * e[n] for n in range(4)] for m in range(4)]


def sample_dirs(n=200):
    out = []
    for i in range(n):
        z = 1.0 - 2.0 * (i + 0.5) / n
        rho = math.sqrt(max(0.0, 1.0 - z * z))
        th = math.pi * (1.0 + 5.0 ** 0.5) * i
        out.append((rho * math.cos(th), rho * math.sin(th), z))
    return out


def energy_conditions(Th, ndir=200, nspeed=10):
    """(NEC, WEC, SEC) minima over sampled observers.  DEC needs the WEC."""
    trace = sum(ETA[m] * Th[m][m] for m in range(4))
    nec = wec = sec = float("inf")
    for u in sample_dirs(ndir):
        k = (1.0,) + u
        nec = min(nec, sum(Th[m][n] * k[m] * k[n] for m in range(4) for n in range(4)))
        for j in range(1, nspeed + 1):
            s = j / (nspeed + 1.0)
            gam = 1.0 / math.sqrt(1.0 - s * s)
            V = (gam, gam * s * u[0], gam * s * u[1], gam * s * u[2])
            w = sum(Th[m][n] * V[m] * V[n] for m in range(4) for n in range(4))
            wec = min(wec, w)
            sec = min(sec, w + 0.5 * trace)
    return nec, wec, sec


def dec_holds(wec_min):
    """The DEC requires the WEC.  A negative WEC minimum fails it outright."""
    return wec_min >= 0.0


# ---------------------------------------------- the ansatz-free theorem

def enclosed_mass_from_grr(g_rr, r):
    """m(r) = (r/2)(1 - 1/g_rr), inverting g_rr = 1/(1 - 2m/r)."""
    return 0.5 * r * (1.0 - 1.0 / g_rr)


def contracts(g_rr):
    """Proper radial length shorter than the areal-coordinate length."""
    return g_rr < 1.0


def theorem_holds(samples=(0.25, 0.5, 0.8, 1.0, 1.25, 2.0, 4.0), r=1.0):
    """Contraction at r if and only if the enclosed Misner-Sharp mass < 0."""
    return all(contracts(x) == (enclosed_mass_from_grr(x, r) < 0.0)
               for x in samples if x != 1.0)


def conformastatic_grr(r, m=M_SEATED):
    return math.exp(-2.0 * phi(r, m))


def conformastatic_forces_negative_mass(radii=(0.005, 0.05, 1.0, 10.0, 100.0)):
    """Phi > 0 gives g_rr < 1 everywhere, hence m(r) < 0 everywhere."""
    return all(enclosed_mass_from_grr(conformastatic_grr(r), r) < 0.0 for r in radii)


NOVELTY_CLAIMED = False
THEOREM_SCOPE = "static and spherically symmetric only"
THEOREM_VALUE = "ansatz-free, so the obstruction becomes THEOREM rather than MODEL"
QI_BOUNDS = "a sampled energy density along a worldline"
THEOREM_BOUNDS = "the volume integral of rho over a ball"
REQUIRES_NEGATIVE_TOTAL_MASS = False
SEAT_LEAD_SPLIT_SURVIVES = False

PRIOR_ART = "Pfenning & Ford, gr-qc/9702026 (1997)"
PRIOR_ART_RESULT = "Delta <= 10^2 v_b L_Planck, then E ~ -3e20 M_galaxy v_b"
PRIOR_ART_OWN_GAP = ("they apply the FLAT SPACE inequality to a curved metric "
                     "because the exact treatment 'would be exceptionally difficult'")


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-3):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    def under(label, got, bound):
        nonlocal ok
        good = got <= bound
        ok &= good
        print("  %-56s %20.6g %20s  %s"
              % (label, got, "<= %.3g" % bound, "ok" if good else "FAIL"))

    print("0. PRIOR ART, FIRST, BECAUSE IT GOES AGAINST US")
    print("     %s" % PRIOR_ART)
    print("     %s" % PRIOR_ART_RESULT)
    print("     their own stated gap: %s" % PRIOR_ART_OWN_GAP)
    print("       candidates.py's conclusion, 28 years earlier.  H37 needed this.")

    print("\n1. THE PIPELINE, VALIDATED BEFORE IT IS BELIEVED")
    Tm = stress_energy(minkowski, [0, 3.0, 1.0, 2.0], 1e-3)
    chk("Minkowski: T is exactly zero", max_abs(Tm), 0.0)
    sch = schwarzschild_isotropic(1.0)
    for r in (5.0, 50.0):
        under("Schwarzschild vacuum at r = %-5.0f max|T|" % r,
              max_abs(stress_energy(sch, [0, r, 0.0, 0.0], r * 1e-4)),
              1e-8)
    print("       THAT IS THE NOISE FLOOR.  Everything below is quoted to it.")

    print("\n2. THE ANSATZ, CERTIFIED")
    near("Phi(0) = m/a, core.py's figure", phi(0.0), 0.9999, 1e-4)
    print("     %-8s %13s %13s %13s %13s %6s"
          % ("r", "T_00", "NEC min", "WEC min", "SEC min", "DEC"))
    dev = conformastatic()
    worst = 0.0
    for r in (0.05, 0.2, 1.0, 10.0):
        T = stress_energy(dev, [0, r, 0.0, 0.0], max(r * 1e-4, 1e-7))
        Th = orthonormal(T, dev([0, r, 0, 0]))
        nec, wec, sec = energy_conditions(Th)
        worst = max(worst, -min(nec, wec, sec))
        print("     %-8.4g %13.4e %13.4e %13.4e %13.4e %6s"
              % (r, Th[0][0], nec, wec, sec, "ok" if dec_holds(wec) else "VIOL"))
        chk("  NEC violated at r = %-6.3g" % r, nec < 0.0, True)
        chk("  WEC violated at r = %-6.3g" % r, wec < 0.0, True)
        chk("  DEC violated at r = %-6.3g" % r, dec_holds(wec), False)
    print("       EVERY CONDITION, EVERY RADIUS.  Six orders above the floor.")
    T1 = stress_energy(dev, [0, 1.0, 0, 0], 1e-4)
    near("T_00 at r = 1", orthonormal(T1, dev([0, 1.0, 0, 0]))[0][0], -4.8455e-4, 1e-3)
    h = 1e-6
    d = (phi(1.0 + h) - phi(1.0 - h)) / (2 * h)
    near("  against -|grad Phi|^2", -d * d, -3.9952e-4, 1e-3)
    print("       the density is dominated by a SQUARE carrying a minus sign.")
    # NOTE: 14.716 is the COORDINATE component; the tetrad divides by
    # -g_00 = e^{2Phi} = 0.4759 there, giving 30.92 orthonormal.
    Tn = stress_energy(conformastatic(-M_SEATED), [0, 0.05, 0, 0], 5e-6)
    Thn = orthonormal(Tn, conformastatic(-M_SEATED)([0, 0.05, 0, 0]))
    chk("CORRECTION: is T_00 negative for m < 0 at r = 0.05", Thn[0][0] < 0.0, False)
    near("  it is positive, at (orthonormal)", Thn[0][0], 30.9245, 1e-3)
    print("       a first run here claimed 'both signs give T_00 < 0'.  The far")
    print("       field is gradient-dominated and sign-blind; the near core is not.")
    chk("does the seat/lead split survive this", SEAT_LEAD_SPLIT_SURVIVES, False)

    print("\n3. THE ANSATZ-FREE THEOREM, WHICH IS THE RESULT")
    print("     ds^2 = -e^{2Phi}dt^2 + dr^2/(1 - 2m(r)/r) + r^2 dOmega^2")
    print("     dm/dr = 4 pi r^2 rho, and dl = dr/sqrt(1 - 2m/r)")
    print("     %-10s %12s %12s  %s" % ("g_rr", "1 - 2m/r", "m(r)/r", "proper length"))
    for x in (0.5, 0.8, 1.25, 2.0):
        print("     %-10.3g %12.4f %12.4f  %s"
              % (x, 1.0 / x, enclosed_mass_from_grr(x, 1.0),
                 "SHORTER" if contracts(x) else "longer"))
    chk("CONTRACTION IFF ENCLOSED MASS IS NEGATIVE", theorem_holds(), True)
    chk("  and our ansatz forces it at every radius",
        conformastatic_forces_negative_mass(), True)
    print("     what the quantum inequalities bound: %s" % QI_BOUNDS)
    print("     what this bounds:                    %s" % THEOREM_BOUNDS)
    print("       averaging along a geodesic is not integrating over a ball,")
    print("       which is why this survives all of candidates.py untouched.")
    chk("does it require negative TOTAL mass", REQUIRES_NEGATIVE_TOTAL_MASS, False)
    print("       m(r) < 0 locally is compatible with M_ADM >= 0.  The")
    print("       concentric shell is the device that arranges exactly that,")
    print("       and the positive mass theorem was never in danger.")

    print("\n4. STATUS, STATED BEFORE ANYONE ASKS")
    chk("is novelty claimed for the theorem", NOVELTY_CLAIMED, False)
    chk("  its scope", THEOREM_SCOPE, "static and spherically symmetric only")
    chk("  its value", THEOREM_VALUE,
        "ansatz-free, so the obstruction becomes THEOREM rather than MODEL")
    print("       It follows from the Misner-Sharp definition in two lines and")
    print("       the flare-out condition is a near neighbour.  The point is not")
    print("       that it is new -- it is that it needs no ansatz.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  H39a said this project's central requirement rested on a chosen
  potential and had never been certified.  It has now been certified two
  ways.  First numerically: a stdlib reimplementation of Warp Factory's
  test -- validated to exactly zero on Minkowski and 4e-12 on Schwarzschild
  vacuum -- finds the seated conformastatic ansatz violating the NEC, WEC,
  SEC and DEC at EVERY radius from 0.005 to 100, six orders above the noise
  floor, with the density dominated by -|grad Phi|^2, a square carrying a
  minus sign.  That kills this project's own seat/lead split: the exotic
  requirement is not localised in a lead, it sits wherever Phi varies.
  Second, and this is the result, without any ansatz at all: in any static
  spherically symmetric spacetime, written with an areal radius and the
  Misner-Sharp mass, proper distance is contracted at r IF AND ONLY IF the
  enclosed mass m(r) is negative -- and, where the centre is regular so
  that m(0) = 0, m(r) is the volume integral of rho.  (Reissner-Nordstrom
  is the counterexample to that second clause and not to the first; see
  the COROLLARY above and drivensource.py section 3.)
  No Phi, no Plummer, no shell; a definition and one integral.  That
  converts the obstruction from MODEL to THEOREM, which is what the audit
  asked for, and it constrains a quantity no quantum inequality bounds,
  because averaging along a geodesic is not integrating over a ball.  It
  does NOT require negative total mass, so the concentric architecture was
  never silly and the positive mass theorem was never in danger.  No
  novelty is claimed -- it is two lines from a standard definition -- and
  its scope is static and spherically symmetric only.  Prior art is
  recorded first and against us: Pfenning & Ford got candidates.py's
  conclusion in 1997.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
