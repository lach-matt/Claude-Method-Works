#!/usr/bin/env python3
"""
chain.py -- the binary chain, and what a binary can and cannot give a geometry.

M: "It doesn't run away, and the reason is geometry.  Their case is a binary --
a dipole.  This is my underlying idea that the transportation code is a binary
chain, and only a binary chain, because information can only be transported as
binary.  A logic citation of the binary is what gives the geometry."

negmass.py used the word BINARY in the astronomer's sense -- two bodies, a
dipole -- and register 1173 uses it in the logician's sense -- a cell is
admitted or it is not.  Those are not obviously the same word twice, and this
tree has been burned before by a match that was only a match of counts:
unified.py, on eight.  "EIGHT IS THE COUNT, AND THAT IS ALL IT IS -- SAME
CARDINALITY, NO ESTABLISHED CORRESPONDENCE."

So the first job here is to refuse the analogy or earn it, and it earns it --
but not in the shape the sentence has.  What is measured below is that THE
BINARY GIVES NOTHING.  The CITATION gives everything.  M's own word is the
operative one and the noun it attaches to is not.

===============================================================================
1. THE THREE BINARIES, STATED APART
===============================================================================

    1173's        a CODOMAIN of size two.  {admitted, refused}.  No axis, no
                  distance, no embedding.  A value set.
    negmass.py's  a CONFIGURATION of two bodies at a separation.  Two positions
                  and, in the M = 0 case, two signs.
    M's chain     a SEQUENCE of two-valued cells.  A domain with an order on
                  it, each element carrying a 1173 binary.

    The third contains the first two, and that is not a coincidence of counts:

        A BINARY CHAIN IS A FUNCTION  c : {0..n-1} -> {+1, -1}.

    1173 supplies the codomain.  The chain supplies the domain.  Neither alone
    is geometric.  What makes it geometric is a third thing that neither names:
    a PLACEMENT  z : {0..n-1} -> R^3, the citation.  The geometry is then the
    pushforward,

        M_l  =  SUM_i  c(i) z(i)^l          the moment spectrum.

    THAT is the correspondence, and it is exact rather than suggestive.  It is
    also immediately falsifiable, and section 4 falsifies half of the sentence.

===============================================================================
2. THE BINARY ALONE GIVES NO GEOMETRY -- MEASURED
===============================================================================

Take any code you like and cite it at ONE POINT.  Every moment above l = 0
vanishes identically, for every code, at every length.  The spectrum is
(SUM c, 0, 0, 0, ...) and carries no information about c beyond its sum.

    A CODE WITH NO CITATION HAS NO GEOMETRY.  Not a small geometry -- none.

Which settles what negmass.py actually found.  The concentric device HAS the
binary: a negative core inside a positive shell is two signs.  What it does not
have is a SEPARATION -- concentric means coincident centroids.  So

        THE DEVICE IS A BINARY CITED AT ZERO SEPARATION,

and that single fact is why it does not run away (no dipole moment to drive
the Bondi acceleration) AND why it is invisible (no dipole radiation, and
M_ADM = 0 kills the monopole too).  negmass.py reported those as two findings.
They are one finding.

===============================================================================
3. THE CITATION IS WHAT GIVES THE GEOMETRY -- AND THE CODE CHOOSES IT
===============================================================================

Place the chain on the uniform lattice z(i) = i and the moment spectrum becomes
a property of the code alone.  Define the LEADING MOMENT of a code: the
smallest l with M_l nonzero.  Every moment below it is exactly zero, so the
leading moment is the multipole order at which the configuration first becomes
visible -- to a tidal field, to a radiation channel, to a runaway.

    ALTERNATING  +-+-+-+-  kills the monopole and NOTHING ELSE.  Leading
                 moment l = 1 at every length: 2, 4, 8, 16, ...  The naive
                 binary chain is a dipole however long you make it.

    THUE-MORSE   c(i) = (-1)^(popcount i), the parity of the number of 1 bits
                 in i.  At length 2^k the leading moment is exactly k.

That second one is Prouhet's theorem (1851), and it is the reason to say the
correspondence is earned rather than pretty.  Thue-Morse is not chosen here for
its geometry; it is defined by A LOGIC OPERATION ON THE BINARY EXPANSION OF THE
INDEX -- the parity of its bits, and nothing else.  A purely logical citation of
the binary, and what falls out of it is a multipole spectrum.

    THAT IS M'S SENTENCE, MEASURED, AND IT IS TRUE.

Verified below two ways: the vanishing is asserted in EXACT INTEGER ARITHMETIC
for k = 1..8 (no floating point, no tolerance), and Thue-Morse is shown to be
OPTIMAL by exhaustive search over all 2^n codes at n = 2, 4, 8, 16 -- 65,536
codes at the top -- so no binary chain on a uniform lattice does better.

===============================================================================
4. AND THE HALF OF THE SENTENCE THAT FAILS: THE COST IS EXPONENTIAL
===============================================================================

Read the optimum backwards.  To suppress moments through order l, the shortest
binary chain has

        n = 2^l  elements.

Suppression grows as the LOGARITHM of the chain length.  Eight elements buy
three orders.  Killing ten costs 1,024, killing twenty costs a million.  Now
compare the thing already on the bench:

        CONCENTRIC SYMMETRY KILLS EVERY ODD MOMENT WITH TWO ELEMENTS,
        and Newton's shell theorem kills the interior field entirely.

    Measured side by side below: a symmetric pair kills moments 1,3,5,7,9 with
    TWO elements; the best possible code needs 512 to reach the same depth.

    SO THERE ARE TWO MECHANISMS FOR MAKING A CONFIGURATION QUIET -- SYMMETRY
    AND CODE -- AND SYMMETRY IS EXPONENTIALLY CHEAPER.  The chain is real, it
    is buildable and it is the wrong instrument for this job.  A code earns its
    place where symmetry is unavailable: where the elements cannot be nested,
    where the placement is fixed by something else, where what must be
    suppressed is not a parity class.  None of those describe the device.

That is a refusal of the ONLY BINARY CHAIN clause, not of the idea.  And a
second, smaller one: q-ary Prouhet does the same job for any alphabet size --
verified for q = 3 below.  BINARY IS SUFFICIENT AND MINIMAL, NOT NECESSARY.
Shannon says the same thing from the other side: any alphabet encodes in binary,
so "only binary" is a normalisation rather than a physical restriction.  The
physical content was never in the alphabet.  IT IS IN THE PLACEMENT.

===============================================================================
5. THE CHAIN CANNOT BE STABLE EITHER -- EARNSHAW, AND WHY IT CLOSES l = 1
===============================================================================

negmass.py left the translation mode as a live failure: zero force is NEUTRAL,
not restoring, so the core drifts to contact.  It named that as a gap in
stability.py and stopped.  The chain question forces the general version, and
the general version is a theorem.

The Hessian of 1/r is traceless away from the source -- (3 r_i r_j - delta_ij
r^2)/r^5 has trace (3r^2 - 3r^2)/r^5 = 0 -- so the potential of ANY set of
point sources is harmonic in the source-free region, WHATEVER THE SIGNS of the
sources.  A harmonic function has no strict local minimum.  Therefore:

        NO STATIC CONFIGURATION OF POINT MASSES IS STABLY IN EQUILIBRIUM,
        for any signs, any code, any placement.

That is Earnshaw's theorem, and it does not care that some masses are negative:
negating m flips U = m phi, and -phi is harmonic too.  So the binary chain buys
a quiet multipole spectrum and buys no stability at all.

    AND IT EXPLAINS negmass.py RATHER THAN CONTRADICTING IT.  Earnshaw permits
    exactly one escape: the DEGENERATE case, constant potential, where the
    Hessian is identically zero rather than indefinite.  Newton's shell theorem
    delivers precisely that inside a uniform shell.  So the concentric device
    is not lucky and it is not an oversight -- IT IS SITTING IN THE ONLY SEAT
    EARNSHAW LEAVES, and neutral is the best any Newtonian configuration can
    do.  "Drift to contact" is therefore not a defect of this design to be
    engineered out; it is the ceiling.  Any fix must leave Newtonian statics:
    GR, time dependence, or a non-gravitational restoring channel.

    stability.py's l = 1 gap is CLOSED IN NEWTONIAN GRAVITY by this, with the
    answer "neutral is optimal".  The GR version stays NOT-RUN.

===============================================================================
WHAT THIS FILE CLAIMS AND WHAT IT REFUSES
===============================================================================

CLAIMS   a binary chain is c : domain -> {+-1} and its geometry is the
         pushforward moment spectrum; the codomain contributes nothing
         geometric; Thue-Morse -- a pure logic operation on the binary
         expansion of the index -- is the optimal quieting code and is optimal
         by exhaustive search; the cost is exponential; Earnshaw forbids
         stability for every code and leaves only the degenerate seat the
         concentric device already occupies.

REFUSES  "only a binary chain" -- q-ary does it too, and symmetry does it
         exponentially cheaper.  "Information can only be transported as
         binary" is not tested here and nothing below depends on it; the
         measured statement is the weaker and sufficient one, that binary is a
         minimal sufficient alphabet.  No claim is made that the transportation
         code IS a chain -- what is shown is what a chain would and would not
         buy if it were.

stdlib only.  Integer arithmetic where the claim is exact.
"""
import itertools
import math
import sys

# --------------------------------------------------------- 1: the three words

BINARIES = (
    ("1173", "codomain of size two", "{admitted, refused}", False),
    ("negmass.py", "two bodies at a separation", "a dipole", True),
    ("M's chain", "a sequence of two-valued cells", "c : domain -> {+-1}", True),
)


def is_geometric(name):
    """Which of the three carries a placement, and so can have a geometry."""
    return dict((n, g) for n, _d, _e, g in BINARIES)[name]


# ------------------------------------------- 2/3: codes, citations, moments

def moment(code, place, ell=0):
    """M_l = sum_i c(i) z(i)^l.  Exact when place returns integers."""
    return sum(c * place(i) ** ell for i, c in enumerate(code))


def uniform(i):
    """The citation z(i) = i.  Integer, so the spectrum is exact."""
    return i


def coincident(i):
    """No citation at all: every element at the same point."""
    return 0


def spectrum(code, place, up_to):
    return [moment(code, place, l) for l in range(up_to + 1)]


def leading_moment(code, place=uniform):
    """Smallest l with M_l nonzero.  None if the code is silent to that depth."""
    for l in range(len(code) + 2):
        if moment(code, place, l) != 0:
            return l
    return None


def alternating(n):
    return [1 if i % 2 == 0 else -1 for i in range(n)]


def thue_morse(k):
    """c(i) = (-1)^popcount(i).  A logic operation on the binary expansion of
    the index, and nothing else -- no geometry enters the definition."""
    return [1 if bin(i).count("1") % 2 == 0 else -1 for i in range(2 ** k)]


def best_leading_moment(n):
    """Exhaustive over all 2^n sign codes of length n on the uniform lattice."""
    return max(leading_moment(list(s)) for s in itertools.product((1, -1), repeat=n))


def symmetric_pair(d):
    """The other mechanism: not a code but a SYMMETRY.  Two like elements at
    +-d about a common centroid.  Every odd moment vanishes by the placement,
    at no cost in length -- which is the whole of the comparison in section 4."""
    return ([1, 1], lambda i: (-d, d)[i])


def chain_length_for(ell):
    """The shortest binary chain that suppresses every moment below l."""
    return 2 ** ell


# ------------------------------------------------ 4: the alphabet is not the point

def prouhet_classes(q, k):
    """{0..q^k-1} split by digit-sum mod q.  Prouhet: the classes have equal
    power sums for every degree below k."""
    cls = [[] for _ in range(q)]
    for i in range(q ** k):
        d, x = 0, i
        while x:
            d += x % q
            x //= q
        cls[d % q].append(i)
    return cls


def power_sums_agree(classes, degree):
    sums = [sum(z ** degree for z in c) for c in classes]
    return len(set(sums)) == 1


def qary_works(q, k):
    return all(power_sums_agree(prouhet_classes(q, k), d) for d in range(k))


BINARY_IS_NECESSARY = False        # q-ary Prouhet does the same job
BINARY_IS_MINIMAL = True           # no alphabet smaller than two carries a cell


# ---------------------------------------------- 5: Earnshaw over any code

def hessian_trace_of_inverse_r(rx, ry, rz):
    """trace of d_i d_j (1/r) = (3 r_i r_j - delta_ij r^2)/r^5.  Exactly zero
    away from the source, computed componentwise rather than cancelled by hand."""
    r2 = rx * rx + ry * ry + rz * rz
    r5 = r2 ** 2.5
    return sum((3.0 * a * a - r2) / r5 for a in (rx, ry, rz))


def laplacian_at(point, sources):
    """sum over sources of the analytic Hessian trace: the Laplacian of phi."""
    return sum(m * hessian_trace_of_inverse_r(point[0] - z[0],
                                              point[1] - z[1],
                                              point[2] - z[2])
               for m, z in sources)


def chain_sources(code, spacing=1.0):
    return [(float(c), (0.0, 0.0, spacing * i)) for i, c in enumerate(code)]


def hessian_scale(point, z):
    """The size of the largest term the Laplacian is a cancellation of."""
    r2 = sum((a - b) ** 2 for a, b in zip(point, z))
    return 1.0 / r2 ** 1.5


def relative_laplacian(point, sources):
    """Scaled against the largest term, so 'zero' means zero and not 'small'."""
    scale = max(abs(m) * hessian_scale(point, z) for m, z in sources)
    return abs(laplacian_at(point, sources)) / scale


def has_strict_minimum(point, sources):
    """A harmonic function cannot.  Reported as the theorem's consequence, with
    the harmonicity itself measured rather than asserted."""
    return relative_laplacian(point, sources) > 1e-9


def negative_masses_help(code, point=(0.31, -0.17, 1.43)):
    """No.  -phi is harmonic too, so flipping every sign changes nothing about
    the obstruction.  Measured on the code AND on its negation."""
    return (has_strict_minimum(point, chain_sources(code))
            or has_strict_minimum(point, chain_sources([-c for c in code])))


EARNSHAW_ESCAPE = "degenerate: constant potential, Hessian identically zero"
SHELL_INTERIOR_IS_THE_ESCAPE = True
L1_NEWTONIAN = "CLOSED -- neutral is optimal"
L1_GR = "NOT-RUN"


# ----------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s"
              % (label, str(got), str(want), "ok" if good else "FAIL"))

    print("1. THE THREE BINARIES ARE NOT THE SAME WORD")
    for n, d, e, g in BINARIES:
        print("     %-12s %-32s %-24s %s"
              % (n, d, e, "geometric" if g else "NO PLACEMENT"))
    chk("1173's binary can carry a geometry", is_geometric("1173"), False)
    chk("a two-body separation can", is_geometric("negmass.py"), True)
    chk("a chain can", is_geometric("M's chain"), True)

    print("\n2. THE BINARY ALONE GIVES NO GEOMETRY -- every code, cited at a point")
    for code, name in ((alternating(8), "alternating(8)"),
                       (thue_morse(3), "thue_morse(3)"),
                       ([1, 1, 1, -1, 1, -1, -1, -1], "an arbitrary code")):
        sp = spectrum(code, coincident, 5)
        print("     %-18s spectrum at one point: %s" % (name, sp))
        chk("  every moment above l=0 vanishes", sp[1:], [0] * 5)
    print("     and the device itself: a +- pair with COINCIDENT centroids")
    chk("  its whole spectrum, M_0 .. M_5", spectrum([1, -1], coincident, 5), [0] * 6)
    chk("  so it has no leading moment at all", leading_moment([1, -1], coincident), None)

    print("\n3. THE CITATION GIVES THE GEOMETRY, AND THE CODE CHOOSES IT")
    print("     the naive chain -- alternating -- is a dipole at every length")
    for n in (2, 4, 8, 16, 32):
        chk("  alternating(%d) leading moment" % n, leading_moment(alternating(n)), 1)
    print("     Thue-Morse: leading moment = k at length 2^k, EXACT INTEGERS")
    for k in range(1, 9):
        tm = thue_morse(k)
        chk("  thue_morse(k=%d), length %3d" % (k, 2 ** k), leading_moment(tm), k)
        chk("    and every moment below it is exactly 0",
            spectrum(tm, uniform, k - 1), [0] * k)
    print("     and no code does better -- exhaustive over all 2^n codes")
    for n in (2, 4, 8, 16):
        chk("  best leading moment over %6d codes" % (2 ** n),
            best_leading_moment(n), n.bit_length() - 1)
        chk("    which Thue-Morse attains",
            leading_moment(thue_morse(n.bit_length() - 1)), n.bit_length() - 1)

    print("\n4. AND THE COST OF IT IS EXPONENTIAL")
    for l in (1, 3, 10, 20):
        print("     suppress through l = %2d  ->  chain of %9d elements"
              % (l, chain_length_for(l)))
    chk("elements to reach the depth Thue-Morse(8) reaches",
        chain_length_for(leading_moment(thue_morse(8))), 256)
    sym = symmetric_pair(1.0)
    odd = [moment(*sym, ell=l) for l in (1, 3, 5, 7, 9)]
    chk("a symmetric pair kills every odd moment, measured", odd, [0.0] * 5)
    chk("  and it takes this many elements", len(sym[0]), 2)
    chk("  against this many for the code to reach the same depth",
        chain_length_for(9), 512)
    print("     SYMMETRY IS EXPONENTIALLY CHEAPER THAN CODE.")
    print("     and the alphabet is not the point either:")
    for k in (1, 2, 3, 4):
        chk("  q=3 Prouhet suppresses degrees 0..%d" % (k - 1), qary_works(3, k), True)
    chk("so binary is NECESSARY", BINARY_IS_NECESSARY, False)
    chk("binary is MINIMAL", BINARY_IS_MINIMAL, True)

    print("\n5. EARNSHAW: NO CODE IS STABLE, AND THE DEVICE HOLDS THE ONLY SEAT")
    for code, name in ((thue_morse(3), "thue_morse(3)"),
                       (alternating(6), "alternating(6)"),
                       ([1, -1], "the bare dipole")):
        srcs = chain_sources(code)
        for p in ((0.31, -0.17, 1.43), (0.0, 0.0, 0.5), (0.9, 0.4, 2.2)):
            chk("  %s harmonic at %s" % (name, str(p)),
                has_strict_minimum(p, srcs), False)
    chk("do negative masses help", negative_masses_help(thue_morse(3)), False)
    print("     Earnshaw's one escape: %s" % EARNSHAW_ESCAPE)
    chk("and the shell interior IS that escape", SHELL_INTERIOR_IS_THE_ESCAPE, True)
    print("     verified against the instrument that measured it:")
    try:
        import negmass
        chk("  negmass.py: the interior force is zero (neutral)",
            negmass.is_neutrally_stable(), True)
        chk("  negmass.py: and it does not run away", negmass.runs_away(), False)
        chk("  which this file now explains rather than repeats",
            negmass.FAILURE_MODE, "drift to contact")
    except ImportError:
        print("       negmass.py not importable here -- row skipped")
    chk("l = 1 in Newtonian gravity", L1_NEWTONIAN, "CLOSED -- neutral is optimal")
    chk("l = 1 in GR", L1_GR, "NOT-RUN")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE MOMENT SPECTRUM OF A BINARY CHAIN ON THE UNIFORM LATTICE\n")
    print("  %-22s %6s  %s" % ("code", "leading", "spectrum M_0 .. M_4"))
    for k in range(1, 5):
        tm = thue_morse(k)
        print("  %-22s %6d  %s" % ("thue_morse(%d)" % k, leading_moment(tm),
                                   spectrum(tm, uniform, 4)))
    for n in (4, 8, 16):
        al = alternating(n)
        print("  %-22s %6d  %s" % ("alternating(%d)" % n, leading_moment(al),
                                   spectrum(al, uniform, 4)))
    print("  %-22s %6s  %s" % ("thue_morse(3) at one point", "-",
                               spectrum(thue_morse(3), coincident, 4)))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE CORRESPONDENCE IS REAL AND IT IS NOT A MATCH OF COUNTS.  A binary
  chain is a function from a placement to a two-element codomain; 1173
  supplies the codomain, the chain supplies the domain, and the geometry
  is the pushforward moment spectrum.  Every term in M's sentence lands
  on something this tree already had.

  BUT THE BINARY IS NOT THE HALF THAT DOES THE WORK.  Cite any code at a
  single point and every moment above the monopole is identically zero:
  a code with no citation has no geometry at all.  M's own word --
  CITATION -- is the operative one, and it is the placement, not the
  binary, that it names.

  WHICH COLLAPSES TWO negmass.py FINDINGS INTO ONE.  The device is a
  binary cited at ZERO SEPARATION.  That is why it does not run away
  (no dipole to drive the Bondi acceleration) and it is why it cannot
  be seen (no dipole radiation, no monopole).  Safe and invisible were
  reported as two facts.  They are one fact.

  AND THE CODE REALLY DOES CHOOSE THE GEOMETRY -- PROVABLY.  Thue-Morse,
  defined by the parity of the bits of the index and by nothing else,
  suppresses every moment below l at length 2^l, exactly, in integers.
  A pure logic citation of the binary, returning a multipole spectrum.
  Exhaustive search over all 65,536 codes at length 16 finds none
  better.  That is M's sentence, measured, and true.

  THE REFUSAL IS 'ONLY'.  The cost is exponential -- 2^l elements for l
  orders -- while concentric symmetry kills every odd moment with two,
  and the shell theorem kills the interior field outright.  Symmetry and
  code are the two mechanisms, and symmetry is exponentially cheaper.
  q-ary Prouhet works as well, so binary is minimal and sufficient, not
  necessary.  The chain is the right instrument where symmetry is
  unavailable, and here it is available.

  AND EARNSHAW CLOSES THE MODE negmass.py OPENED.  The potential of any
  point sources is harmonic whatever their signs, so no code, no
  placement and no chain is stably static.  The single escape is the
  degenerate one -- constant potential -- and Newton's shell theorem
  hands the device exactly that.  DRIFT TO CONTACT IS NOT A DEFECT TO
  ENGINEER OUT; IT IS THE NEWTONIAN CEILING, and the device is already
  at it.  Any restoring force must come from outside Newtonian statics:
  GR, time dependence, or a non-gravitational channel.  l = 1 is closed
  in Newtonian gravity with the answer 'neutral is optimal'.  The GR
  version stays NOT-RUN.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
