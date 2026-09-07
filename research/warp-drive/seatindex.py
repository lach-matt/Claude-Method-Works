#!/usr/bin/env python3
"""
seatindex.py -- the conditions that seat a transition, as an index.

M: "the whole focus is now the conjugate point.  We must identify what
conditions/parameters do and do not allow for universal transport.  This is
again an index, and we are looking for the conditions that maximize universal
transport."

So: an index whose cells are parameter tuples, whose admission test is DOES IT
SEAT, and whose structure is then read with the corpus's own instruments.

-- THE OBJECT ----------------------------------------------------------------
transit.py reduced seating to one equation, u'' = -q u with q = 4 pi T_kk,
u(0) = 0, the turn being the next zero.  The question "what conditions seat"
is therefore a question about q alone, and it has TWO SHARP CLASSICAL BOUNDS
that bracket it from either side:

  LYAPUNOV (necessary).   If u(a) = u(b) = 0 with u non-trivial then
                          (b - a) INT q+ > 4.  Below that, NOTHING seats,
                          whatever the shape.
  STURM (sufficient).     If q >= m > 0 on a CONTIGUOUS length l >= pi/sqrt(m),
                          every solution has a zero inside that stretch.
                          Equivalently  m l^2 >= pi^2.

Between them is a band where seating depends on the shape of q and on where the
congruence happens to be when it arrives.  That band is not a gap in knowledge;
it is the object.

-- THE ANSWER TO "UNIVERSAL" --------------------------------------------------
The word does the work.  Sturm's condition is UNIVERSAL in the strict sense:
the zero occurs INSIDE the focusing stretch, so nothing outside it can prevent
the seat.  Measured -- at exactly m l^2 = pi^2, over five approach distances crossed with
surrounding potentials of 0, -5 and -20, the turn lands inside the slab in all
fifteen.  Drop below the frontier and universality breaks: at Sturm 0.49 one
case fails, at 0.25 seven do, and the failures are always SHORT APPROACH plus
HOSTILE OUTSIDE -- the combination a fixed approach hides, and the reason the
first version of this test was wrong.  Sufficiency is a theorem; the exact
frontier of universality is NOT-RUN, never absent.

Lyapunov's condition is universal the other way: below it nothing seats, ever.

    THE THREE POPULATIONS ARE M'S OWN, AND THEY ARE NOT FORCED ONTO THIS.
    Register 1206: "the Method equation partitions an index into three
    populations: interior captures, the working overlap, and exterior
    predictions."  Here:

      INTERIOR CAPTURE     m l^2 >= pi^2       seats, universally
      WORKING OVERLAP      Lyapunov met but not Sturm -- seats or not
                           depending on shape and approach.  NOT universal.
      EXTERIOR             L INT q+ <= 4       never seats, whatever the shape

    This was flagged NOT-RUN when the resemblance was first noticed.  It is run
    here, and the trichotomy is exact rather than suggestive.

-- WHAT MAXIMIZES IT, WHICH IS WHAT WAS ASKED ---------------------------------
Inside the universal region the frontier is m l^2 = pi^2, and the cost of
holding it is the focusing budget INT q ~ m l.  Substituting,

        m l = pi^2 / l

    THE COST OF A UNIVERSAL SEAT FALLS AS 1/l.  Long and weak beats short and
    strong, without limit, up to the length the congruence is allowed.  With a
    total available length L the cheapest universal seat is the whole of it:
    l = L, m = pi^2/L^2, budget pi^2/L.

That is a design equation, and it is the same shape as this project's others --
area over thickness, and now strength over length.

In physical units, q = (4 pi G / c^4) T_kk, so the universal condition reads

        T_kk  >=  pi c^4 / (4 G l^2)   =   9.5054e43 / l^2   Pa

and THAT NUMBER IS NOT EXOTIC.  It is positive, ordinary, energy-condition-
satisfying matter -- the sector exclusion 1 of transit.py already forced -- and
at l ~ 100 km it is BELOW nuclear density.  Matter that seats a conjugate point
exists in nature; it is called a neutron star.

-- WHICH COORDINATES THE INDEX ACTUALLY NEEDS ---------------------------------
The information language's test (does a coordinate add join-irreducibles?) run
on the four candidates:

  m   strength      KEEPS cells.  An axis.
  l   extent        KEEPS cells.  An axis.  And it enters as l^2, not l.
  L   total length  KEEPS cells -- it is the Lyapunov denominator.
  c   position      FOLDS.  transit.py's reversal theorem makes c and
                    L - l - c the same cell, so the index is SYMMETRIC ABOUT
                    ITS MIDPOINT and the coordinate is halved, not removed.

The fold is a real E reduction and it is a theorem, not a fit: the Jacobi
operator is self-adjoint, so reading the path from the far end gives the same
answer, which is exactly M's both-ends prediction spending itself as a
coordinate saving.

-- WHAT THIS IS NOT -----------------------------------------------------------
UNIVERSAL SEATING IS NOT UNIVERSAL TRANSPORT, and the gap is the honest part.
A seat is a conjugate point: a null congruence leaves A and reconverges at B.
It carries no payload.  And transit.py's exclusion 2 stands -- every turning ray
arrives LATE.  So this file answers "what conditions seat, universally" exactly,
and "what conditions transport" not at all.  The index is the right index; it is
not yet the index of transport.

stdlib only.  transit.py supplies the turn; typefour.py the stress tensor when
the index is checked against the real bubble rather than a model potential.
"""
import math, sys

PI2 = math.pi * math.pi
C_SI = 299792458.0
G_SI = 6.67430e-11
#  q = (4 pi G / c^4) T  =>  T >= pi c^4 / (4 G l^2)
T_COEFF = math.pi * C_SI ** 4 / (4.0 * G_SI)      # Pa m^2

# the three populations -- register 1206's own names
CAPTURE, OVERLAP, EXTERIOR = "INTERIOR-CAPTURE", "WORKING-OVERLAP", "EXTERIOR"


# ------------------------------------------------------------------- the cell

def slab(m, c, l, outside=0.0):
    """q = m on [c, c+l], `outside` elsewhere.  The index's parameterisation."""
    return lambda x: m if c <= x <= c + l else outside


def seats(q, L, n=4000):
    """Admission: does u return to zero on [0, L]?  Returns the turn or None."""
    h = L / n
    u, up = 0.0, 1.0
    for i in range(n):
        a = -q(i * h) * u
        un = u + h * up + 0.5 * h * h * a
        up += 0.5 * h * (a + (-q((i + 1) * h) * un))
        if i > 2 and un <= 0.0:
            return i * h
        u = un
    return None


# ------------------------------------------------------------- the two bounds

def sturm_number(m, l):
    """m l^2 / pi^2.  >= 1 is the universal region."""
    return m * l * l / PI2


def sturm_sufficient(m, l):
    return m > 0.0 and sturm_number(m, l) >= 1.0


def lyapunov_number(m, l, L):
    """L * INT q+ / 4.  <= 1 excludes seating for ANY shape."""
    return L * max(m, 0.0) * l / 4.0


def lyapunov_excluded(m, l, L):
    return lyapunov_number(m, l, L) <= 1.0


def population(m, l, L):
    """The trichotomy.  Nothing here integrates -- it is read off the bounds."""
    if sturm_sufficient(m, l):
        return CAPTURE
    if lyapunov_excluded(m, l, L):
        return EXTERIOR
    return OVERLAP


# ------------------------------------------------------- what maximizes it

def universal_budget(l):
    """INT q for a universal seat of extent l: m l with m = pi^2/l^2."""
    return PI2 / l


def cheapest_universal(L):
    """With total length L available, the cheapest universal seat uses all of it."""
    return {"l": L, "m": PI2 / (L * L), "budget": PI2 / L}


def tkk_required(l):
    """The universal-seating threshold in SI: T_kk >= pi c^4 / (4 G l^2), in Pa."""
    return T_COEFF / (l * l)


# --------------------------------------------------------- the index, scanned

MS = (0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)
LS = (0.25, 0.5, 1.0, 2.0, 4.0)
TOTAL = 12.0
CPOS = (0.5, 1.5, 3.0, 5.0)


def scan(ms=MS, ls=LS, cs=CPOS, L=TOTAL):
    """One row per cell: parameters, population, and whether it actually seats
    from a given approach.  The population is predicted; the seat is measured."""
    rows = []
    for m in ms:
        for l in ls:
            pop = population(m, l, L)
            for c in cs:
                if c + l > L:
                    continue
                rows.append({"m": m, "l": l, "c": c, "L": L, "pop": pop,
                             "seats": seats(slab(m, c, l), L) is not None})
    return rows


APPROACHES = (0.02, 0.1, 0.3, 1.0, 3.0)
HOSTILES = (0.0, -5.0, -20.0)


def universality_failures(m, l, L=TOTAL, approaches=APPROACHES, hostiles=HOSTILES):
    """The STRICT reading of 'universal': it must seat from every approach AND
    against every surrounding potential.  Fixing the approach is not a test of
    universality -- an early arrival at the slab carries a small u and needs
    less focusing, so a favourable approach can carry a sub-Sturm slab."""
    return [(c, h) for c in approaches for h in hostiles
            if c + l <= L and seats(slab(m, c, l, outside=h), L) is None]


def universal_holds(m, l, L=TOTAL, approaches=APPROACHES, hostiles=HOSTILES):
    return universality_failures(m, l, L, approaches, hostiles) == []


# ---------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-62s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-62s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The admission test, against the exact analytic slab")
    # Inside the slab u(s) = c cos(ks) + sin(ks)/k = A sin(ks + phi), A =
    # sqrt(c^2 + 1/k^2), phi = atan(ck).  So the turn is INTERNAL at
    # s* = (pi - phi)/k when that is within the slab, and otherwise the ray
    # exits with u'(l) = cos(kl) - ck sin(kl) and seats later iff that is
    # negative.  The first version of this fixture used only the second branch
    # and mis-scored the one slab that zeroes inside.
    for m, c, l in ((10.0, 1.0, 0.5), (40.0, 1.0, 0.5), (2.0, 1.0, 3.0),
                    (0.5, 1.0, 1.0)):
        k = math.sqrt(m)
        phi = math.atan(c * k)
        s_star = (math.pi - phi) / k
        internal = s_star <= l
        exact = c + s_star if internal else None
        if not internal:
            slope = math.cos(k * l) - c * k * math.sin(k * l)
        got = seats(slab(m, c, l), TOTAL)
        chk("m=%g l=%.1f seats?" % (m, l), got is not None,
            internal or slope < 0.0)
        if internal:
            near("  and the internal turn is exactly (pi - atan(ck))/k",
                 got, exact, 2e-3)

    print("\nSTURM IS UNIVERSAL -- it seats whatever surrounds the slab")
    mcrit, lcrit = 12.0, math.pi / math.sqrt(12.0)
    near("the critical slab sits exactly on the frontier",
         sturm_number(mcrit, lcrit), 1.0, 1e-12)
    chk("and it seats from every approach against every hostile outside",
        universality_failures(mcrit, lcrit), [])
    # below the frontier universality genuinely breaks, and the failures are
    # SHORT APPROACH plus HOSTILE OUTSIDE -- exactly the combination a fixed
    # approach hides.  The scan EXHIBITS a failure; it does not locate the
    # exact boundary of universality, which stays NOT-RUN.
    half = universality_failures(mcrit, lcrit / math.sqrt(2.0))
    chk("at Sturm 0.49 universality fails somewhere", half != [], True)
    chk("and the failure is the short approach against the harshest outside",
        half[0], (0.02, -20.0))
    quarter = universality_failures(mcrit, lcrit / 2.0)
    chk("at Sturm 0.25 it fails much more widely", len(quarter) > len(half), True)
    print("       Sturm 1.00 -> 0 failures;  0.49 -> %d;  0.25 -> %d."
          % (len(half), len(quarter)))
    print("       Sufficiency is a THEOREM; the exact frontier of universality")
    print("       is not located by this scan and is NOT-RUN, not absent.")

    print("\nLYAPUNOV IS UNIVERSAL THE OTHER WAY -- below it nothing seats")
    excl = [(m, l) for m in MS for l in LS if lyapunov_excluded(m, l, TOTAL)]
    chk("cells the necessary bound excludes", len(excl) > 0, True)
    bad = [(m, l, c) for (m, l) in excl for c in CPOS
           if c + l <= TOTAL and seats(slab(m, c, l), TOTAL) is not None]
    chk("of those, how many seat anyway (must be none)", bad, [])

    print("\nThe three populations -- register 1206's partition, run not assumed")
    rows = scan()
    pops = {}
    for r in rows:
        pops.setdefault(r["pop"], []).append(r)
    for p in (CAPTURE, OVERLAP, EXTERIOR):
        got = pops.get(p, [])
        n_s = sum(1 for r in got if r["seats"])
        print("     %-18s %4d cells, %4d seat" % (p, len(got), n_s))
    chk("every INTERIOR-CAPTURE cell seats",
        all(r["seats"] for r in pops.get(CAPTURE, [])), True)
    chk("no EXTERIOR cell seats",
        any(r["seats"] for r in pops.get(EXTERIOR, [])), False)
    chk("the WORKING OVERLAP does BOTH -- that is what makes it the overlap",
        (any(r["seats"] for r in pops.get(OVERLAP, [])),
         any(not r["seats"] for r in pops.get(OVERLAP, []))), (True, True))
    chk("all three populations are occupied", sorted(pops), sorted([CAPTURE, OVERLAP, EXTERIOR]))

    print("\nWhich coordinates the index needs (the information language's test)")
    # m and l keep cells: varying either changes the population
    chk("m is an axis -- fixing it collapses populations",
        len({population(m, 1.0, TOTAL) for m in MS}) > 1, True)
    chk("l is an axis -- and it enters as l^2, not l",
        sturm_number(4.0, 2.0) == 4.0 * sturm_number(4.0, 1.0), True)
    chk("L is an axis -- it is the Lyapunov denominator",
        lyapunov_excluded(0.5, 0.25, 4.0) != lyapunov_excluded(0.5, 0.25, 64.0), True)
    # c FOLDS: reversal maps c -> L - l - c and the answer is unchanged
    m, l = 6.0, 0.9
    folded = [(c, TOTAL - l - c) for c in (0.5, 1.5, 3.0)]
    chk("c folds about the midpoint -- reversal gives the same seat/no-seat",
        all((seats(slab(m, a, l), TOTAL) is not None)
            == (seats(slab(m, b, l), TOTAL) is not None) for a, b in folded), True)
    print("       the fold is transit.py's reversal theorem spent as a coordinate")
    print("       saving: self-adjointness halves the index rather than shrinking it.")

    print("\nWHAT MAXIMIZES UNIVERSAL SEATING -- the frontier and its cost")
    near("budget at l = 1", universal_budget(1.0), PI2, 1e-12)
    near("budget at l = 10 is ten times cheaper", universal_budget(10.0), PI2 / 10.0, 1e-12)
    chk("cost falls monotonically with extent",
        all(universal_budget(a) > universal_budget(b)
            for a, b in zip((0.5, 1.0, 2.0, 4.0), (1.0, 2.0, 4.0, 8.0))), True)
    cheap = cheapest_universal(TOTAL)
    near("cheapest universal seat uses the whole length", cheap["l"], TOTAL, 1e-12)
    chk("and sits exactly on the frontier",
        abs(sturm_number(cheap["m"], cheap["l"]) - 1.0) < 1e-12, True)

    print("\nThe threshold in SI, and it is ORDINARY matter")
    near("coefficient pi c^4 / 4G  (Pa m^2)", T_COEFF, 9.50536e43, 1e39)
    print("     %10s %18s %s" % ("l", "T_kk needed (Pa)", "vs nuclear ~1e35 Pa"))
    for l, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e5, "100 km"), (1.0e6, "1000 km")):
        t = tkk_required(l)
        print("     %10s %18.4e %10.3g x nuclear" % (tag, t, t / 1.0e35))
    chk("at 100 km the requirement is BELOW nuclear density",
        tkk_required(1.0e5) < 1.0e35, True)
    chk("and it is positive -- the energy-condition-satisfying sector",
        tkk_required(1.0e5) > 0.0, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE INDEX")
    print("  %6s %6s %10s %10s %-18s %s"
          % ("m", "l", "Sturm", "Lyapunov", "population", "seats (by c)"))
    for m in MS:
        for l in LS:
            pop = population(m, l, TOTAL)
            s = "".join("Y" if seats(slab(m, c, l), TOTAL) else "." 
                        for c in CPOS if c + l <= TOTAL)
            print("  %6g %6g %10.3f %10.3f %-18s %s"
                  % (m, l, sturm_number(m, l), lyapunov_number(m, l, TOTAL), pop, s))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  Universal seating is Sturm's condition, m l^2 >= pi^2, and it is")
    print("  universal in the strict sense: the turn happens INSIDE the focusing")
    print("  stretch, so nothing outside it can prevent the seat.  Below")
    print("  Lyapunov, L INT q+ <= 4, nothing seats whatever the shape.  Between")
    print("  them the answer depends on shape and approach and is NOT universal.")
    print("\n  What maximizes it: the frontier costs INT q = pi^2 / l, so LONG AND")
    print("  WEAK beats short and strong without limit.  In SI the threshold is")
    print("  T_kk >= 9.5054e43 / l^2 Pa -- positive, ordinary, energy-condition-")
    print("  satisfying matter, and below nuclear density beyond about 100 km.")
    print("\n  UNIVERSAL SEATING IS NOT UNIVERSAL TRANSPORT.  A seat is a light")
    print("  focus and carries no payload, and every turning ray arrives late.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
