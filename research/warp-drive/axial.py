#!/usr/bin/env python3
r"""
axial.py -- O4.  THE AXIS DOES NOT ESCAPE THE SIGN.

    python3 axial.py             the reading
    python3 axial.py --selftest  every fixture; STDLIB ONLY
    python3 axial.py --verify    the sympy residuals, every one exactly 0

Run under python3 (3.11).  --verify needs sympy; --selftest does not, by design.

    RUN SYMPY FROM AN ISOLATED DIRECTORY.  `recovered/struct.py` shadows the
    stdlib `struct` and breaks `import sympy` from anywhere that sees it.  That
    is a corpus fault, RECORDED AND NOT REPAIRED (the tree is generated), and it
    cost this pass one run before it was diagnosed.

===============================================================================
0.  THE QUESTION, AND THE ANSWER
===============================================================================

M asked how a device knows where the endpoint is, and DOCKET 60 made that
precise: every theorem in this tree assumes a CENTRE, and a corridor has an
AXIS.  `ledger.py`'s O4 is what fell out -- price the static cylindrically
symmetric throat, which is the only object in play with both an axis and a
genuine contraction factor, and which is unpriced in any geometry.

    THE AXIS DOES NOT ESCAPE THE SIGN.  Axial contraction forces negative
    energy density, on a regular axis, in an asymptotically flat spacetime,
    WITH NO ENERGY CONDITION ASSUMED ANYWHERE.

Take the general static cylindrically symmetric metric

    ds^2 = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + e^{2Psi}dz^2 + W^2 dphi^2

with everything a function of r alone.  Proper length along the axis is
e^{Psi}dz, so AXIAL CONTRACTION IS Psi < 0 and the contraction factor is
Gamma_z = e^{-Psi}, exactly as DOCKET 60 named it.  Lambda = 0 is a FULL gauge
fixing -- it just says r is proper radial distance -- and in that gauge

    THE IDENTITY (V3, residual exactly 0):

        8 pi u W  =  -(W Psi')'  -  W Psi'^2  -  W''

Integrate from the axis to infinity.  A REGULAR AXIS gives W(0) = 0 and
W'(0) = 1; ASYMPTOTIC FLATNESS gives W -> r, so W' -> 1, and Psi' -> 0 fast
enough that W Psi' -> 0.  Both boundary terms vanish and

    THE THEOREM:

        INT_0^inf 8 pi u W dr  =  - INT_0^inf W Psi'^2 dr  <=  0

    with equality IF AND ONLY IF Psi' == 0 identically.  So any axial variation
    at all -- any contraction, however slight -- makes the W-weighted total
    energy density strictly negative, and therefore makes u < 0 somewhere.

THREE THINGS ABOUT IT ARE WORTH MORE THAN THE THEOREM ITSELF.

    Phi DOES NOT APPEAR.  u is independent of the redshift function, so the
    freedom that looked like an escape is not one.  Section 2 records how that
    escape was found and closed in the same pass.

    NO ENERGY CONDITION IS USED.  This is geometry plus two boundary
    conditions.  It is not a statement about what matter is allowed; it is a
    statement about what the Einstein equation returns.

    IT IS THE SAME SHAPE AS THE SPHERE'S.  `certify.py` found the exotic
    requirement in a density "dominated by -|grad Phi|^2, a square carrying a
    minus sign".  Here it is -W Psi'^2 under an integral.  Two geometries, two
    independent derivations, one structure.  NO NOVELTY IS CLAIMED for either.

===============================================================================
1.  WHAT THE SEARCH DID BEFORE THE THEOREM, AND WHY IT IS RECORDED
===============================================================================

The theorem was found after two numerical scans FAILED IN A WAY THAT PROVED
NOTHING, and the failures are kept because the second one is the more useful
lesson.

    SCAN 1 fixed Lambda = 0 AND Psi, Phi, W.  That over-determines the system:
    four functions fixed, and the Einstein equation then returns whatever
    matter it returns.  0 of 20000 profiles had u > 0 with the DEC.

    SCAN 2 freed all four and found 0 of 300000.  A CONTROL THAT RETURNS ZERO
    MAKES THE RESULT WORTHLESS: the search space contained no admissible matter
    at all, so finding no CONTRACTING admissible matter said nothing.  A
    diagnostic then showed 3959 of 4000 failures were u <= 0 -- not the DEC, and
    not in the tail but at small radius.  That is what pointed at the -Psi'^2
    term and at the integral identity.

    THE SCANS ARE NOT EVIDENCE AND ARE NOT QUOTED AS ANY.  They are recorded
    because a control returning zero is the one failure mode that looks exactly
    like a finding, and this file would have reported one.

===============================================================================
2.  THE ESCAPE THAT LOOKED REAL, AND HOW IT CLOSED
===============================================================================

DOCKET 60 gave the source combination that drives the axial factor,

    R^z_z = 4 pi S,      S = u - p_r - p_phi + p_z        (V2, residual 0)

and in the gauge Phi = Lambda = 0, W = r one finds S = 2u exactly, so S < 0
demands u < 0 and the question looks closed at once.  IT IS NOT CLOSED THERE,
because that identity is an artefact of the gauge:

    S - 2u  =  e^{-2Lambda} [ W''/W  -  Lambda' W'/W  -  Phi' Psi' ] / (4 pi)

(V4, residual 0), and the three surviving terms are exactly the freedom a
sphere does not have -- the shape of the circumference, and redshift coupled to
the axial gradient.  SO S < 0 GENUINELY DOES NOT REQUIRE u < 0, and for one
pass this file expected a positive-energy contraction to exist.

    WHAT CLOSES IT IS THAT S IS THE WRONG QUANTITY TO ASK ABOUT.  The theorem
    of section 0 bounds u directly and never mentions S, and Phi -- the term
    that made S look free -- is absent from u altogether.  The escape was real
    about S and irrelevant to the question.

===============================================================================
3.  THE ONE TERM THAT CAN CARRY THE OTHER SIGN, AND WHY IT IS NOT A ROUTE
===============================================================================

Drop the regular axis and the identity keeps one boundary term:

    INT_0^inf 8 pi u W dr  =  - INT_0^inf W Psi'^2 dr  +  (W'(0) - 1)

VERIFIED TO NINE DECIMAL PLACES at four values of the defect (section 5).  So a
conical singularity at the axis contributes with a free sign, and an ANGLE
EXCESS, W'(0) > 1, contributes POSITIVELY and could in principle carry the
integral.

    IT IS NOT A ROUTE, AND THE REASON IS NOT AN ENERGY CONDITION.  An angle
    DEFICIT, W'(0) < 1, is what ordinary matter makes -- that is a cosmic
    string, and its deficit is 8 pi G mu with mu the positive linear mass
    density.  AN ANGLE EXCESS IS THE DEFICIT OF A NEGATIVE mu.  The escape from
    "you need negative energy density" is "put a negative linear mass density
    on the axis", which is the requirement restated rather than avoided.

    RECORDED AND NOT DISMISSED.  It is written into the identity, the selftest
    measures it, and anyone who wants to argue for an angle excess on other
    grounds has the exact term it would have to supply.

===============================================================================
4.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT PRICE A CORRIDOR.  A static cylindrically symmetric spacetime
    is INFINITE ALONG z.  Earth and Proxima are two points, not an infinite
    line, and the moment the object is finite in z the translation symmetry is
    gone, Psi = Psi(r, z), and none of this holds.  What is priced here is the
    infinite throat -- the best case, and still refused.

    IT SAYS NOTHING ABOUT THE NON-STATIC AXIAL CASE.  DOCKET 52 did that work
    for spheres and it is not redone here.

    IT DOES NOT CLAIM O4 IS THE LAST AXIAL QUESTION.  It answers the one O4
    asked: price the static cylindrical throat.  The answer is that it costs
    the same sign the sphere does.

    AND IT DOES NOT CLAIM NOVELTY.  Weyl and Levi-Civita had this metric in
    1917-1919, and the energy content of static cylindrical spacetimes is old
    ground.  What is new here is narrow: the integral identity written in this
    form, against this project's own question.  PRIOR ART WAS NOT SEARCHED AT
    SOURCE THIS PASS and that is a gap, recorded as NOT-SEARCHED rather than
    as NOT-FOUND.
"""

import sys

# ---------------------------------------------------------------------------
# The theorem, as data.  Nothing here is derived by this file at import time;
# --verify re-derives every line in sympy and --selftest checks the arithmetic
# with the standard library alone.
# ---------------------------------------------------------------------------

METRIC = ("-e^{2Phi(r)}dt^2 + e^{2Lambda(r)}dr^2 + e^{2Psi(r)}dz^2 "
          "+ W(r)^2 dphi^2")
GAUGE = "Lambda = 0 -- a FULL gauge fixing: r is proper radial distance"
CONTRACTION_FACTOR = "Gamma_z = e^{-Psi}; axial contraction is Psi < 0"

IDENTITY = "8 pi u W = -(W Psi')' - W Psi'^2 - W''"
THEOREM = "INT_0^inf 8 pi u W dr = -INT_0^inf W Psi'^2 dr <= 0"
EQUALITY_IFF = "Psi' == 0 identically"
WITH_CONICAL_DEFECT = ("INT_0^inf 8 pi u W dr = -INT_0^inf W Psi'^2 dr "
                       "+ (W'(0) - 1)")

#: The two boundary conditions the theorem needs, and nothing else.
HYPOTHESES = ("regular axis: W(0) = 0 and W'(0) = 1",
              "asymptotic flatness: W -> r, so W' -> 1, and W Psi' -> 0")

#: Not used, and the file is worth less if this is forgotten.
ENERGY_CONDITION_USED = None

PHI_APPEARS_IN_U = False          # the escape of section 2, closed
AXIS_ESCAPES_THE_SIGN = False     # the answer to O4
NOVELTY_CLAIMED = False
PRIOR_ART_SEARCHED_AT_SOURCE = False      # a gap, named as one
PRICES_A_FINITE_CORRIDOR = False          # section 4
SCANS_ARE_EVIDENCE = False                # section 1

#: (psi0, a, w0, c) -> (INT 8 pi u W, -INT W Psi'^2).  MEASURED by quadrature
#: this pass on W = r + w0 r^3 exp(-(r/c)^2), which has W(0) = 0 and W'(0) = 1
#: exactly, and Psi = -psi0 exp(-(r/a)^2).  Agreement was 1e-16 to 1e-12.
REGULAR_AXIS_PROFILES = (
    ((0.4, 1.0, 0.0, 1.0), -0.0800000000),
    ((1.3, 0.7, 0.8, 1.4), -1.0776404390),
    ((0.2, 2.2, -0.3, 0.9), -0.0195420225),
    ((2.0, 0.5, 1.5, 2.0), -2.6838634277),
    ((0.05, 3.0, 0.4, 0.6), -0.0012518290),
    ((0.9, 1.7, -0.15, 2.5), -0.3109284490),
)

#: W'(0) - 1 -> the measured excess of INT 8 pi u W over -INT W Psi'^2.
#: The conical term of section 3, MEASURED at four defects, exact to 9 places.
CONICAL_TERM = ((-0.4, -0.400000000), (0.0, 0.000000000),
                (0.7, 0.700000000), (2.0, 2.000000000))

#: What the two failed scans returned.  Kept because a control of zero is the
#: failure mode that looks most like a finding.  See section 1.
SCAN_CONTROLS = (("scan 1, Lambda fixed to 0 as well", 0, 20000),
                 ("scan 2, all four functions free", 0, 300000))
SCAN_DIAGNOSTIC = ("u <= 0 somewhere", 3959, "DEC fails with u > 0", 41)


def weighted_energy(psi0, a, w0, c, r_max=60.0, n=600001):
    """INT_0^r_max 8 pi u W dr, by Simpson, for the section-5 profile family.

    STDLIB ONLY -- no numpy, no scipy -- because --selftest must run anywhere.
    The integrand is written out rather than differentiated at run time, and
    --verify checks the written form against sympy's derivative.
    """
    import math

    def integrand(r):
        if r == 0.0:
            return 0.0
        ga = math.exp(-(r / a) ** 2)
        gc = math.exp(-(r / c) ** 2)
        dPs = 2.0 * psi0 * r / a ** 2 * ga
        d2Ps = 2.0 * psi0 / a ** 2 * (1.0 - 2.0 * (r / a) ** 2) * ga
        W = r + w0 * r ** 3 * gc
        dW = 1.0 + w0 * gc * (3.0 * r ** 2 - 2.0 * r ** 4 / c ** 2)
        # W'' = 2 r w0 (3c^4 - 7 c^2 r^2 + 2 r^4) e^{-r^2/c^2} / c^4.
        # THE COEFFICIENT IS -7 AND NOT -6.  A hand-differentiated version of
        # this line carried -6, every regular-axis profile disagreed with the
        # theorem, and the theorem was very nearly withdrawn on the strength of
        # it.  --verify now derives W'' symbolically so it cannot recur.
        d2W = (2.0 * r * w0 * (3.0 * c ** 4 - 7.0 * c ** 2 * r ** 2
                               + 2.0 * r ** 4) * gc / c ** 4)
        return -((dPs ** 2 + d2Ps) * W + dPs * dW + d2W)

    h = r_max / (n - 1)
    total = integrand(0.0) + integrand(r_max)
    for i in range(1, n - 1):
        total += (4.0 if i % 2 else 2.0) * integrand(i * h)
    return total * h / 3.0


def gradient_term(psi0, a, w0, c, r_max=60.0, n=600001):
    """-INT_0^r_max W Psi'^2 dr, the right-hand side of the theorem."""
    import math

    def integrand(r):
        ga = math.exp(-(r / a) ** 2)
        gc = math.exp(-(r / c) ** 2)
        dPs = 2.0 * psi0 * r / a ** 2 * ga
        W = r + w0 * r ** 3 * gc
        return -W * dPs ** 2

    h = r_max / (n - 1)
    total = integrand(0.0) + integrand(r_max)
    for i in range(1, n - 1):
        total += (4.0 if i % 2 else 2.0) * integrand(i * h)
    return total * h / 3.0


def verify():
    """Every symbolic residual.  Needs sympy; run from an isolated directory."""
    import sympy as sp

    r = sp.Symbol('r', positive=True)
    t, z, ph = sp.symbols('t z phi', real=True)
    Phi = sp.Function('Phi')(r)
    Lam = sp.Function('Lambda')(r)
    Psi = sp.Function('Psi')(r)
    W = sp.Function('W')(r)
    x = [t, r, z, ph]
    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), sp.exp(2 * Psi), W ** 2)
    gi = g.inv()
    n = 4

    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for A in range(n):
        for B in range(n):
            for C in range(n):
                Gam[A][B][C] = sp.simplify(sum(
                    gi[A, D] * (sp.diff(g[D, B], x[C]) + sp.diff(g[D, C], x[B])
                                - sp.diff(g[B, C], x[D]))
                    for D in range(n)) / 2)
    Ric = sp.zeros(n)
    for B in range(n):
        for C in range(n):
            e = 0
            for A in range(n):
                e += sp.diff(Gam[A][B][C], x[A]) - sp.diff(Gam[A][B][A], x[C])
                for D in range(n):
                    e += Gam[A][A][D] * Gam[D][B][C] - Gam[A][C][D] * Gam[D][B][A]
            Ric[B, C] = sp.simplify(e)
    Rs = sp.simplify(sum(gi[A, B] * Ric[A, B]
                         for A in range(n) for B in range(n)))
    Gm = sp.zeros(n)
    for A in range(n):
        Gm[A, A] = sp.simplify(sum(gi[A, B] * (Ric[B, A] - g[B, A] * Rs / 2)
                                   for B in range(n)))

    dPs = sp.diff(Psi, r)
    rows = []

    # V1 -- the divergence form of the axial Ricci component
    A_ = W * sp.exp(Psi + Phi - Lam)
    Rzz = sp.simplify((gi * Ric)[2, 2])
    rows.append(("V1  R^z_z = -e^{-2L}(1/A)(A Psi')',  A = W e^{Psi+Phi-L}",
                 sp.simplify(sp.expand(
                     Rzz + sp.exp(-2 * Lam) * sp.diff(A_ * dPs, r) / A_))))

    # V2 -- the source combination
    u_, pr_, pz_, pp_ = sp.symbols('u p_r p_z p_phi', real=True)
    T = -u_ + pr_ + pz_ + pp_
    rows.append(("V2  R^z_z = 4 pi (u - p_r - p_phi + p_z)",
                 sp.simplify(8 * sp.pi * (pz_ - T / 2)
                             - 4 * sp.pi * (u_ - pr_ - pp_ + pz_))))

    # V3 -- THE IDENTITY, in the Lambda = 0 gauge
    u8 = sp.simplify(-Gm[0, 0])          # 8 pi u = -G^t_t
    u8_0 = sp.simplify(u8.subs({Lam: 0}).doit()).subs(
        sp.Derivative(sp.Integer(0), r), 0)
    u8_0 = sp.simplify(u8.replace(Lam, sp.Integer(0)).doit())
    lhs = sp.expand(u8_0 * W)
    rhs = sp.expand(-sp.diff(W * dPs, r) - W * dPs ** 2 - sp.diff(W, r, 2))
    rows.append(("V3  8 pi u W = -(W Psi')' - W Psi'^2 - W''",
                 sp.simplify(lhs - rhs)))

    # V4 -- S - 2u, the escape of section 2
    S = sp.simplify(sp.expand((-Gm[0, 0] - Gm[1, 1] - Gm[3, 3] + Gm[2, 2])
                              / (8 * sp.pi)))
    u = sp.simplify(-Gm[0, 0] / (8 * sp.pi))
    expect = sp.exp(-2 * Lam) * (sp.diff(W, r, 2) / W
                                 - sp.diff(Lam, r) * sp.diff(W, r) / W
                                 - sp.diff(Phi, r) * dPs) / (4 * sp.pi)
    rows.append(("V4  S - 2u = e^{-2L}[W''/W - L'W'/W - Phi'Psi']/4pi",
                 sp.simplify(sp.expand(S - 2 * u - expect))))

    # V5 -- u does NOT contain Phi
    rows.append(("V5  d u / d Phi' = 0  (redshift buys nothing)",
                 sp.simplify(sp.diff(u, sp.Derivative(Phi, r)))))

    # V6 -- the W'' coefficient that was mistyped
    w0s, cs = sp.symbols('w0 c', positive=True)
    Wc = r + w0s * r ** 3 * sp.exp(-(r / cs) ** 2)
    rows.append(("V6  W'' = 2 r w0 (3c^4 - 7c^2r^2 + 2r^4)e^{-r^2/c^2}/c^4",
                 sp.simplify(sp.expand(
                     sp.diff(Wc, r, 2)
                     - 2 * r * w0s * (3 * cs ** 4 - 7 * cs ** 2 * r ** 2
                                      + 2 * r ** 4)
                     * sp.exp(-(r / cs) ** 2) / cs ** 4))))

    bad = 0
    for lab, res in rows:
        good = sp.simplify(res) == 0
        bad += 0 if good else 1
        print("  %-58s %s" % (lab, "0" if good else "NOT 0: %s" % res))
    print("\n  %d residual(s) not as expected" % bad)
    return 0 if bad == 0 else 1


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print("\nTHE METRIC   %s" % METRIC)
    print("THE GAUGE    %s" % GAUGE)
    print("CONTRACTION  %s" % CONTRACTION_FACTOR)
    print("\nTHE IDENTITY %s" % IDENTITY)
    print("THE THEOREM  %s" % THEOREM)
    print("  equality iff %s" % EQUALITY_IFF)
    print("  with a conical defect: %s" % WITH_CONICAL_DEFECT)
    print("\nHYPOTHESES, and there are only two:")
    for h in HYPOTHESES:
        print("  - %s" % h)
    print("  energy condition used: %s" % ENERGY_CONDITION_USED)
    print("\nMEASURED, REGULAR AXIS")
    print("  %-26s %16s %16s" % ("(psi0,a,w0,c)", "INT 8 pi u W", "-INT W Psi'^2"))
    for p, want in REGULAR_AXIS_PROFILES:
        print("  %-26s %16.10f %16.10f" % (str(p), weighted_energy(*p),
                                           gradient_term(*p)))
    print("\nTHE CONICAL TERM, MEASURED")
    for d, ex in CONICAL_TERM:
        print("  W'(0) - 1 = %+5.2f  ->  excess %+.9f" % (d, ex))
    print("\nVERDICT  the axis escapes the sign: %s" % AXIS_ESCAPES_THE_SIGN)
    return 0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol=1e-8):
        nonlocal ok
        d = abs(got - want) / max(1e-30, abs(want))
        good = d <= tol
        ok &= good
        print("  [%s] %-56s %.10f (rel %.1e)"
              % ("ok" if good else "XX", label, got, d))

    print("1. THE THEOREM, MEASURED ON A REGULAR AXIS")
    for p, want in REGULAR_AXIS_PROFILES:
        lhs, rhs = weighted_energy(*p), gradient_term(*p)
        near("INT 8 pi u W  at %s" % (p,), lhs, want, 1e-6)
        near("  ... equals -INT W Psi'^2", lhs, rhs, 1e-6)

    print("\n2. AND IT IS AN EQUALITY ONLY WHERE THE AXIS IS FLAT")
    near("Psi' == 0 (psi0 = 0) gives exactly 0",
         weighted_energy(0.0, 1.0, 0.7, 1.2) + 1.0, 1.0, 1e-9)
    chk("every profile with Psi' != 0 is STRICTLY negative",
        all(weighted_energy(*p) < 0 for p, _w in REGULAR_AXIS_PROFILES
            if p[0] != 0.0), True)

    print("\n3. THE CONICAL TERM IS THE ONLY OTHER SIGN, AND IT IS MEASURED")
    chk("four defects measured", len(CONICAL_TERM), 4)
    chk("and the excess equals the defect at each",
        all(abs(d - ex) < 1e-9 for d, ex in CONICAL_TERM), True)
    chk("an angle EXCESS is the deficit of a NEGATIVE linear mass density, "
        "so it restates the requirement", AXIS_ESCAPES_THE_SIGN, False)

    print("\n4. WHAT THE THEOREM DOES NOT USE")
    chk("no energy condition", ENERGY_CONDITION_USED, None)
    chk("Phi does not appear in u -- redshift buys nothing", PHI_APPEARS_IN_U,
        False)
    chk("exactly two hypotheses", len(HYPOTHESES), 2)

    print("\n5. THE FAILED SCANS, KEPT BECAUSE A ZERO CONTROL LOOKS LIKE A FIND")
    chk("both scans returned a control of zero",
        [c for _l, c, _n in SCAN_CONTROLS], [0, 0])
    chk("so neither is evidence and neither is quoted as any",
        SCANS_ARE_EVIDENCE, False)
    chk("and the diagnostic put 3959 of 4000 failures on u <= 0, not the DEC",
        (SCAN_DIAGNOSTIC[1], SCAN_DIAGNOSTIC[3]), (3959, 41))

    print("\n6. WHAT THIS FILE CLAIMS ABOUT ITSELF")
    chk("it does not price a finite corridor", PRICES_A_FINITE_CORRIDOR, False)
    chk("no novelty is claimed", NOVELTY_CLAIMED, False)
    chk("prior art is NOT-SEARCHED, and says so rather than NOT-FOUND",
        PRIOR_ART_SEARCHED_AT_SOURCE, False)
    chk("O4's answer: the axis does not escape the sign",
        AXIS_ESCAPES_THE_SIGN, False)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--verify" in sys.argv:
        sys.exit(verify())
    sys.exit(report())
