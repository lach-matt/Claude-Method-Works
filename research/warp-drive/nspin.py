#!/usr/bin/env python3
r"""
nspin.py -- WHAT A SEATED NUCLEAR-SPIN TABLE WOULD DO TO THE GRAVITY INDEX,
AND WHY MAGNETIC RESONANCE IS A DATA SOURCE AND NOT A PROPULSION ROUTE.

M: "I am thinking about MRI research.  Can a gravity be a solution via magnet
resinence" -- and then "Adding centrifugal force of some kind with
electromagnets, creating a strong resinence field that alters the relative
gravity of any object within the field".

    python3 nspin.py             the reading
    python3 nspin.py --selftest  fixtures

Two questions were asked and they have opposite answers.  As a WAY TO MAKE
GRAVITY, a resonant rotating electromagnet fails by eighteen orders of
magnitude and has a published null result against it.  As a SOURCE OF INDEX
DATA, a ground-state nuclear-spin table is a real input: it moves 755 seated
members off X = 0 and makes the gravity bound STRONGER by 128 demanded cells.

Nothing here is seated.  This file MEASURES what seating would do; it does not
do it, because the I table is not banked and a bound may not be swapped under a
chart that was built without it.  Section 4 states that limit precisely.

===============================================================================
1. THE PROPULSION QUESTION, ANSWERED BY ARITHMETIC
===============================================================================

Gravity couples to stress-energy.  A magnetic field's contribution is its own
stored energy over c^2, so a rotating electromagnet drags frames exactly as
hard as its field WEIGHS -- and a field weighs almost nothing.

`rig_table()` puts uniform B through a sphere of radius R, spins it at f, and
takes the solid-sphere moment of the field's mass-equivalent.  At the world
continuous-field record of 45 T the rig stores 422 MEGAJOULES and that energy
has a mass of 4.7 NANOGRAMS.  Its gravitomagnetic field at the rim is 1.0e-18
of Earth's, and a test mass moving at 1 m/s inside it feels 3.6e-33 g.

RESONANCE IS THE RIGHT INSTINCT AND IT IS NOT ENOUGH.  A resonant cavity
multiplies stored energy by its quality factor Q, so the deficit is a Q
requirement: reaching parity with Earth's frame-dragging needs Q ~ 1e18.  B
itself does not scale away either -- 45 T is the continuous record and 100 T is
pulsed and destroys the coil.

AND IT HAS BEEN TRIED.  Tajmar and de Matos predicted an enhanced
gravitomagnetic London moment from a rotating superconductor, many orders above
the general-relativistic value, and reported a positive signal.  Graham et al.
(2008) repeated it with a lead disk and a ring-laser gyroscope and got a null
result within one sigma, bounding any effect at 21 times smaller than
predicted.  The claim has a falsification on the record.

FINALLY, THE SHAPE IS WRONG.  `ROTATING-SHELL.md` in this tree records that a
single rotating shell carries ADM angular momentum, so its exterior is Kerr --
which destroys the exactly-Schwarzschild exterior the Fuchs et al. positive-
energy construction is built on.  Counter-rotation sets J = 0 exactly.  If
rotation enters a design here it enters as a counter-rotating pair, and its job
is gyroscopic, not gravitational.

===============================================================================
2. THE INDEX QUESTION, WHICH IS THE PRODUCTIVE ONE
===============================================================================

`gravity.py` section 8 refuses to call 2Je the member's spin: "The nuclear part
is not banked, so chi as computed is the electronic contribution to the Kerr
parameter and nothing more."  That refusal names the missing datum, and a
ground-state nuclear-spin table is exactly it.

Nuclear spin I enters the chart today through ONE function:

    forced(A, Ne) = (A + Ne) % 2

which reads I's PARITY and never its value.  That is exact and this file does
not touch it.  What a seated I would change is the OTHER axis:

    X   spin-decade rank of chi = Je hbar c / (G M^2)

which is built from the ELECTRONIC angular momentum alone.  With I seated, X
would be read from the TOTAL F = Je + I, and `image_with_I()` sweeps the
coordinate map under that substitution.

===============================================================================
3. WHAT IT MEASURES
===============================================================================

    image now, Je only              1416 cells
    image with I seated             1088 cells      328 lost, NONE gained

    demanded 1550    FORBIDDEN 1080 -> 1208     OPEN 470 -> 342

NOTHING IS GAINED, WHICH IS THE STRONGEST FORM THE ANSWER COULD TAKE.  The
I-image is a STRICT SUBSET of the image the chart has now, so seating I can
only forbid -- it cannot open a cell the present bound closes, and no
adjudication already made can be reversed by it.

THE BOUND GETS STRONGER, NOT WEAKER, AND ONE PARITY FACT DOES IT.  F = 1 means
A + Ne is odd, so exactly one of I and Je is half-odd-integer, so their sum is
half-odd-integer and CANNOT VANISH -- so chi is never zero and the cell
(F = 1, X = 0) LEAVES THE IMAGE ENTIRELY.  The chart already knows that parity,
in `forced`; the X axis cannot see it, because X is built from Je alone.

The same parity governs the sweep itself, and getting it wrong was this file's
one defect: 2Je is odd exactly when Ne is odd, and a first sweep let 2Je run
free of Ne.  That admitted 2F = 0 at 34 cells the parity forbids and understated
the effect by 86 demanded cells.  `stale_chart_cells()` is the fixture that
caught it -- 78 of the 112 rather than all 112 -- and it is kept for that.

    seated members moved off X = 0           755
    of which odd-A, Je = 0                   593
    even-A odd-Z odd-N, Je = 0               162

A SECOND STATUS MOVES.  `vanishes()` rests on the pairing rule, which
`PAIRING_RULE_STATUS` marks an exceptionless empirical rule and not a theorem.
Read off a measured I table it becomes READ.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

**TO SEAT THE SUBSTITUTION.**  The I table is not banked.  Every figure in
section 3 is what the sweep reports under a MODEL of I -- parity fixed by A,
2I running to 16 -- and not a measurement of any nuclide's spin.

**TO READ THE 168 AS A REFUTATION.**  168 currently-seated cells fall outside
the I-image, and EVERY ONE OF THEM HAS X = 0: 112 at F = 1, and 56 at F = 0
with a charge.  That is the signature of a RE-CHART, not a contradiction --
X = 0 is precisely the reading that a seated I replaces, so the comparison
holds an old chart against a new image and the disagreement is located exactly
where it must be.  A bound may not be swapped under a chart built without the
datum the bound uses.  `stale_chart_cells()` returns the pair, and
`stale_are_all_X0()` returns the shape.

**TO CALL THE PROPULSION ARITHMETIC AN EXPERIMENT.**  Section 1 is a
scaling estimate on a uniform field in a sphere.  It is three orders of
magnitude robust, which is all it needs to be against a deficit of eighteen,
and it is not a design.
"""

import math
import sys

import gravity as g

HBAR = 1.054571817e-34
C = g.C_SI
G_N = 6.67430e-11
MU0 = 4e-7 * math.pi
ALPHA = 7.2973525693e-3

#: (B tesla, R metre, f Hz) -- the continuous record, a pulsed field, and a
#: large slow rig, so the reader can see the scaling rather than one number.
RIGS = (
    (20.0, 1.0, 100.0),
    (45.0, 0.5, 1000.0),
    (100.0, 0.5, 1000.0),
)

#: Earth, for the ratio.  Moment-of-inertia factor 0.3307, sidereal day.
EARTH_M, EARTH_R, EARTH_MOI = 5.972e24, 6.371e6, 0.3307
EARTH_DAY = 86164.0

#: The published null result the propulsion claim has to clear.
TAJMAR_REPLICATION = (
    "Graham, Hurst, Thirkettle, Rowe, Butler (2008), 'Experiment to detect "
    "frame dragging in a lead superconductor' -- ring-laser gyroscope against "
    "a rotating lead disk, null within 1 sigma, bounding any Tajmar-de Matos "
    "gravitomagnetic London moment at >= 21x smaller than predicted."
)


# --------------------------------------------------------- 1. the propulsion

def earth_bg():
    """(J, B_g) for Earth -- the denominator of every ratio below."""
    J = EARTH_MOI * EARTH_M * EARTH_R ** 2 * (2 * math.pi / EARTH_DAY)
    return J, 2 * G_N * J / (C ** 2 * EARTH_R ** 3)


def rig(B, R, f):
    """(E joule, m_eq kg, J J.s, B_g 1/s) for uniform B in a sphere, spun at f.

    The mass that can drag frames is the field's stored energy over c^2.  That
    is the whole argument: a magnetic field is a very light thing to build out
    of, and no amount of spinning changes what it weighs.
    """
    V = (4.0 / 3.0) * math.pi * R ** 3
    E = B * B / (2 * MU0) * V
    m = E / C ** 2
    J = 0.4 * m * R * R * (2 * math.pi * f)
    return E, m, J, 2 * G_N * J / (C ** 2 * R ** 3)


def rig_table():
    """[(B, R, f, E, m_eq, B_g, B_g/Earth)] over RIGS."""
    _, bge = earth_bg()
    return [(B, R, f) + rig(B, R, f)[:1] + rig(B, R, f)[1:2] + (rig(B, R, f)[3],
            rig(B, R, f)[3] / bge) for (B, R, f) in RIGS]


def q_required(B=45.0, R=0.5, f=1000.0):
    """The resonant quality factor that would bring one rig to Earth parity.

    B_g is linear in stored energy, and a resonator multiplies stored energy by
    Q, so the shortfall IS the Q requirement.  It is not a small number.
    """
    _, bge = earth_bg()
    return bge / rig(B, R, f)[3]


def test_mass_accel(B=45.0, R=0.5, f=1000.0, v=1.0):
    """Frame-dragging acceleration on a test mass at speed v, in g."""
    return rig(B, R, f)[3] * v / 9.80665


# ------------------------------------------------------------- 2. the index

def zero_je_population():
    """(total Je=0, odd-A, even-A, even-even) over the seated members.

    Odd A makes I half-odd-integer, so F = Je + I cannot vanish and chi cannot
    be zero -- yet the chart reads X = 0 for every one of them, because X is
    built from Je.  That gap is what a seated I closes.
    """
    ms = g.members()
    z = [m for m in ms if m[5] == 0]
    odd = [m for m in z if m[2] % 2 == 1]
    even = [m for m in z if m[2] % 2 == 0]
    ee = [m for m in z if m[0] % 2 == 0 and m[1] % 2 == 0]
    return len(z), len(odd), len(even), len(ee)


def members_moved():
    """How many seated members would gain a nonzero X from a seated I.

    Every Je = 0 member except the even-even ones the pairing rule zeroes.
    """
    return sum(1 for m in g.members()
               if m[5] == 0 and not (m[0] % 2 == 0 and m[1] % 2 == 0))


_IIMAGE = {}


def image_with_I(cut=16, icut=16):
    """The coordinate map's image with X read from TOTAL F = Je + I.

    The same exhaustion `ghosts.gravity_image` runs, with one substitution: 2I
    runs over the values A's parity permits, and X is taken from every 2F in
    |2Je - 2I| .. 2Je + 2I stepping by two, rather than from 2Je alone.

    I IS A MODEL HERE AND NOT A MEASUREMENT.  Section 4 says so; this docstring
    repeats it because the return value is a set of cells and looks measured.
    """
    key = (cut, icut)
    if key in _IIMAGE:
        return _IIMAGE[key]
    sp, ch = g._ranks()
    spi = {d: i + 1 for i, d in enumerate(sp)}
    chd = {d: i + 1 for i, d in enumerate(ch)}
    seeds = set()
    for Z, N, A, _sym, dm, _qual in g.nuclides():
        base = A * g.U_KG + dm * g.KEV_J / C ** 2
        for q in range(0, Z + 1):
            M = base - q * g.M_E
            if M <= 0:
                continue
            aG = G_N * M * M / (HBAR * C)
            Y = 0
            if q > 0:
                Y = chd.get(math.floor(math.log10(
                    math.sqrt(q * q * ALPHA / aG))))
                if Y is None:
                    continue
            F = (A + (Z - q)) % 2
            for ti in range(A % 2, icut + 1, 2):
                # 2Je is odd exactly when Ne is odd.  Letting it run free of
                # Ne's parity admits 2F = 0 where the parity forbids it, and
                # the fixture caught that: 34 cells the free sweep kept.
                for tj in range((Z - q) % 2, cut + 1, 2):
                    for tf in range(abs(tj - ti), tj + ti + 1, 2):
                        if tf == 0:
                            X = 0
                        else:
                            X = spi.get(math.floor(math.log10((tf / 2.0) / aG)))
                            if X is None:
                                continue
                        seeds.add((F, X, Y, tf == 0, 1 if q > 0 else 0))
    out = {(D, g.bound_class(D, qp, F, Jz), F, X_, Y, L, E)
           for (F, X_, Y, Jz, qp) in seeds
           for D in range(4, 12) for L in (0, 1) for E in (0, 1)}
    _IIMAGE[key] = out
    return out


def image_delta():
    """(now, with I, lost, gained) -- the image shrinks, so the bound tightens."""
    import ghosts
    cur, new = ghosts.gravity_image(), image_with_I()
    return len(cur), len(new), len(cur - new), len(new - cur)


def demand_delta():
    """(demanded, FORBIDDEN now, FORBIDDEN with I, net moved OPEN->FORBIDDEN)."""
    import demand
    import ghosts
    import registry
    X = frozenset(registry.index_of("gravity.index"))
    d = sorted(demand.demand(X))
    cur, new = ghosts.gravity_image(), image_with_I()
    fc = sum(1 for c in d if c not in cur)
    fn = sum(1 for c in d if c not in new)
    return len(d), fc, fn, fn - fc


def stale_chart_cells():
    """(seated cells outside the I-image, how many are exactly (F=1, X=0)).

    THIS IS NOT A REFUTATION.  It is the arithmetic signature of a re-chart:
    the seated chart's X was computed from Je, so of course it disagrees with
    an image built on total F.  Seating I recomputes those members too.
    `stale_are_all_X0` carries the evidence: the disagreement is confined to
    the exact reading a seated I replaces.
    """
    import registry
    X = frozenset(registry.index_of("gravity.index"))
    new = image_with_I()
    bad = [c for c in X if c not in new]
    return len(bad), sum(1 for c in bad if c[2] == 1 and c[3] == 0)


def stale_are_all_X0():
    """True iff EVERY seated cell outside the I-image reads X = 0.

    The caution in section 4 rests on this and on nothing else.  If a cell with
    X > 0 ever fell outside, the substitution would be moving something other
    than the reading it is meant to move, and this file's conclusion would not
    hold.
    """
    import registry
    new = image_with_I()
    return all(c[3] == 0 for c in registry.index_of("gravity.index")
               if c not in new)


def image_is_subset():
    """True iff the I-image is contained in the image the chart has now.

    Seating I can then only FORBID.  No cell the present bound closes is
    opened by it, so no adjudication already recorded can be reversed.
    """
    import ghosts
    return image_with_I() <= ghosts.gravity_image()


# ------------------------------------------------------------------- reading

def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 74)
    print("1.  THE PROPULSION ARITHMETIC")
    print("=" * 74)
    ej, ebg = earth_bg()
    print("   Earth   J %.3e J.s    B_g %.3e 1/s" % (ej, ebg))
    print()
    print("   %-24s %-11s %-11s %-11s %s"
          % ("rig", "stored E", "mass-eq", "B_g", "/ Earth"))
    for B, R, f in RIGS:
        E, m, _J, bg = rig(B, R, f)
        print("   %-24s %.3e J %.3e kg %.3e   %.3e"
              % ("%g T, R=%g m, %g Hz" % (B, R, f), E, m, bg, bg / ebg))
    print()
    print("   resonant Q needed for Earth parity, 45 T rig   %.2e"
          % q_required())
    print("   frame-drag on a 1 m/s test mass, 45 T rig      %.2e g"
          % test_mass_accel())
    print()
    print("   " + TAJMAR_REPLICATION)
    print()
    print("=" * 74)
    print("2.  WHAT A SEATED NUCLEAR-SPIN TABLE WOULD DO")
    print("=" * 74)
    z, odd, even, ee = zero_je_population()
    print("   seated members with Je = 0                     %d" % z)
    print("      A odd    -- I half-odd-integer, F != 0      %d" % odd)
    print("      A even   -- I integer, may be 0             %d" % even)
    print("      even-even -- the pairing rule zeroes these  %d" % ee)
    print("   members that would gain a nonzero X            %d" % members_moved())
    print()
    now, new, lost, gained = image_delta()
    print("   image now, Je only                             %d" % now)
    print("   image with I seated                            %d" % new)
    print("      cells lost                                  %d" % lost)
    print("      cells gained                                %d" % gained)
    print()
    dem, fc, fn, net = demand_delta()
    print("   demanded                                       %d" % dem)
    print("      FORBIDDEN now                               %d   OPEN %d"
          % (fc, dem - fc))
    print("      FORBIDDEN with I                            %d   OPEN %d"
          % (fn, dem - fn))
    print("      net moved OPEN -> FORBIDDEN                 %d" % net)
    print()
    bad, f1x0 = stale_chart_cells()
    print("   seated cells outside the I-image               %d" % bad)
    print("      of which exactly (F=1, X=0)                 %d" % f1x0)
    print("   -- a RE-CHART signature, not a refutation.  See section 4.")
    print()
    print("=" * 74)
    print("3.  THE REFUSALS")
    print("=" * 74)
    print(__doc__.split("4. WHAT THIS FILE REFUSES", 1)[1]
          .split("=====", 1)[0].strip().replace("\n", "\n   ").rjust(3))


# ------------------------------------------------------------------ fixtures

def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-58s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("nspin.py fixtures")

    # -- the propulsion arithmetic, to three significant figures --------------
    def sig3(x):
        return float("%.3g" % x)

    _, ebg = earth_bg()
    chk("Earth's gravitomagnetic field at the surface (1/s)",
        sig3(ebg), 3.36e-14)
    chk("45 T, R=0.5 m rig stores this many joules",
        sig3(rig(45.0, 0.5, 1000.0)[0]), 4.22e8)
    chk("and its stored energy weighs this many kg",
        sig3(rig(45.0, 0.5, 1000.0)[1]), 4.69e-9)
    chk("its B_g as a fraction of Earth's",
        sig3(rig(45.0, 0.5, 1000.0)[3] / ebg), 1.04e-18)
    chk("the resonant Q that would close that gap",
        sig3(q_required()), 9.58e17)
    chk("frame-drag on a 1 m/s test mass, in g",
        sig3(test_mass_accel()), 3.57e-33)
    chk("more field always means more B_g -- monotone in B",
        [rig(b, 0.5, 1000.0)[3] for b in (20.0, 45.0, 100.0)]
        == sorted(rig(b, 0.5, 1000.0)[3] for b in (20.0, 45.0, 100.0)), True)

    # -- the index measurement ------------------------------------------------
    chk("Je = 0 population (total, odd-A, even-A, even-even)",
        zero_je_population(), (1178, 593, 585, 423))
    chk("members that would gain a nonzero X", members_moved(), 755)
    chk("image (now, with I, lost, gained)", image_delta(), (1416, 1088, 328, 0))
    chk("demand (total, FORBIDDEN now, with I, net)",
        demand_delta(), (1550, 1080, 1208, 128))
    chk("stale-chart cells, and how many are (F=1, X=0)",
        stale_chart_cells(), (168, 112))
    chk("every stale cell reads X = 0 -- the caution's whole evidence",
        stale_are_all_X0(), True)
    chk("the I-image is a SUBSET: seating I can only forbid",
        image_is_subset(), True)
    chk("2Je's parity is tied to Ne -- the defect the fixtures caught",
        [(m[4] % 2, m[5] % 2) for m in g.members()[:400]
         if m[4] % 2 != m[5] % 2], [])

    # -- the substitution is the ONLY change, and it is the right one ---------
    chk("forced() is untouched: it reads parity and never I's value",
        [g.forced(a, n) for a, n in ((1, 0), (1, 1), (2, 0), (2, 1))],
        [1, 0, 0, 1])
    chk("the image shrinks, so the bound can only tighten",
        image_delta()[1] < image_delta()[0], True)
    chk("nothing is gained, so no recorded adjudication reverses",
        image_delta()[3], 0)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
