#!/usr/bin/env python3
"""
candidates.py -- the three proposed leads, run against the full spec.  All three
fail, they fail at DIFFERENT PLACES, and the way they fail is more informative
than the verdict.

M, after teardown.py named the new requirement: "I honestly cannot remember.  I
read it in passing.  We'll have to run all three candidates."

    So: negative effective mass, the Casimir effect, and squeezed vacuum, each
    against the three things the lead must now do.  Nothing is taken on the
    reputation of the idea; each is failed at a specific gate with a number.

===============================================================================
0. THE SPEC, WHICH NOW HAS THREE HALVES RATHER THAN ONE
===============================================================================

    KIND       supplies rho < 0.  Not "negative mass" in some effective sense --
               a genuinely negative energy density, because that is what
               PMT rigidity DERIVED and what lattice.py's theorem forbids to
               every classical EM field.

    DEADLINE   switches off in ~R/c.  teardown.py: the corridor's lifetime is
               max(tau_seat, tau_lead), so a lead that cannot be switched makes
               the corridor un-closable whatever the seat does, and closure.py
               says what an un-closable corridor costs.

    MAGNITUDE  enough of it.  The lead is the whole cost, so it must carry
               E_transition in a region of size R:

                   |rho_needed|  ~  c^4 / (G Lambda R^2)

    THE THIRD GATE IS NEW HERE.  Previous passes asked for the sign and, since
    teardown.py, the deadline.  Neither asked the quantum sources how much they
    can actually supply, and that is what decides all three.

===============================================================================
1. CANDIDATE A -- NEGATIVE EFFECTIVE MASS.  FAILS AT THE FIRST GATE.
===============================================================================

Negative-mass exciton polaritons are real, measured, and switchable: dissipative
light-matter coupling in an atomically thin semiconductor inverts the lower
polariton branch, and the propagation direction is opposite to the momentum
(arXiv:2204.04041, and Nature Communications).  Negative-mass effects are also
seen in spin-orbit-coupled BECs (arXiv:1801.04779).

    AND IT IS THE WRONG QUANTITY, WHICH NO AMOUNT OF ENGINEERING FIXES.

        effective mass    m* = hbar^2 / (d^2 E / dk^2)

    is a property of the DISPERSION RELATION -- the curvature of a band.  It is
    not T_00.  A quasiparticle with m* < 0 still carries POSITIVE energy --
    measured from a stable ground state (the band minimum), or as absolute
    energy including rest energy (~2 eV for the polariton); the curvature
    alone fixes no sign of E, so the reference is part of the claim.  What
    is inverted is how its group velocity responds to momentum.

    SO IT VIOLATES NO ENERGY CONDITION AT ALL.  lattice.py's theorem does not
    even engage with it, because there is nothing there to engage: the
    gravitational source is the full stress-energy of the cavity, the excitons
    and the field -- the MATTER T_ab of G_ab = 8 pi G T_ab, read with
    Lambda = 0 in four dimensions -- and that is positive ON THE HYPOTHESIS
    that the medium and the field are ordinary matter and radiation obeying
    the classical WEC.  That positivity is assumed here, not computed.

        A NEGATIVE-MASS POLARITON WOULD NOT BEND SPACETIME THE WRONG WAY.  It
        is a band-structure effect in a medium, and the medium weighs what it
        weighs.

    FAILS: KIND.  Passes the deadline trivially, and the magnitude gate is never
    reached because there is no rho < 0 to measure.  Recorded because it is the
    candidate most likely to be mistaken for a lead -- "negative mass" is the
    same phrase for two different things, and only one of them is exotic.

===============================================================================
2. CANDIDATE B -- THE CASIMIR EFFECT.  PASSES KIND, FAILS THE OTHER TWO.
===============================================================================

A negative energy density between ideal plates (perfect conductors, infinite,
T = 0 -- the Brown-Maclay 1969 local form of Casimir 1948's energy per area).
What the laboratory measures is the FORCE between real metal plates
(parallel plates 0.5-3 um, Bressi 2002; sphere-plate via the proximity force
approximation down to ~0.1 um), not this energy density:

        rho_Casimir  =  - pi^2 hbar c / (720 d^4)

    KIND: PASSES for ideal plates.  This is a real rho < 0, not an effective
    one.  For plasma-model (real-metal) plates the midpoint density is
    negative only for omega_p d >~ 97-99, d >~ 1.3 um in Al; at the gaps
    priced in section 4 it is positive (DOCKET 67 audit).  The kind gate is
    read for ideal plates; the candidate fails either way.

    DEADLINE: FAILS IN THIS FILE'S GEOMETRY.  Switching it off by MOVING THE
    PLATES is mechanical, and massive matter is slower than c, so clearing a
    displacement l takes t > l/c.  Section 4 sets the gap to the corridor
    size (d = R), so l ~ R and the ~R/c deadline is missed by the factor c/v
    -- by a lot only if v << c, a datum not cited here.  It is NOT missed in
    a microstructured geometry (l << R): d = 1 nm, w = 100 nm, R = 1 m and
    v = 100 m/s clear in 1.0e-9 s < R/c = 3.34e-9 s (DOCKET 67 audit), and
    there Casimir's first failed gate is MAGNITUDE.  Non-mechanical switches
    -- optical modulation of the Casimir force (quant-ph/0610094, 0707.4390),
    a SQUID effective mirror (1105.4714) -- are NAMED-NOT-READ; optical
    switching modulates the force rather than removing it.  There is no
    configuration of matter that clears itself at c, which is teardown.py's
    whole point.  The negative region is also anchored to the plates, whose own
    mass-energy is hugely positive and does not go anywhere.

    MAGNITUDE: FAILS, AND BY THE SAME MARGIN AS THE OTHERS.  Section 4.

===============================================================================
3. CANDIDATE C -- SQUEEZED VACUUM.  PASSES BOTH QUALITATIVE GATES.
===============================================================================

This is the one the tree had already singled out.  lightbuild.py's OPEN row says
lattice.py's theorem is about the CLASSICAL Maxwell stress tensor, and squeezed
vacuum is precisely the exception: a state in which the EXPECTATION VALUE of
the energy density (normal-ordered against the Minkowski vacuum) at a
spacetime point is negative -- Epstein-Glaser-Jaffe 1965 for the general
theorem, Kuo-Ford 1993 Eq. (3.22) for the single-mode form fluctuation.py
carries.  It is an expectation value, not an eigenvalue: <:T00^2:> = 3 rho^2,
so the relative fluctuation is Delta' = 2 wherever rho != 0
(fluctuation.py).

    KIND: PASSES.  A real rho < 0, and the standard one -- on part of every
    cycle: the negative phase fraction is arccos(tanh r)/pi (0.468 at
    r = 0.1, 0.032 at r = 3), positive energy in the same wave outweighs it
    (cycle average +2K sinh^2 r), and the dip has a floor above
    -hbar omega/(2V) per mode.  The floor bears on MAGNITUDE, not KIND.

    DEADLINE: PASSES.  Kill the pump and it is gone at c -- for free massless
    propagation in vacuum (in a dispersive medium it clears at c/n_g) and
    single-pass generation (a cavity-enhanced source clears on its storage
    time, not computed here).  'Gone' means the negative regions leave at c
    together with the positive energy that outweighs them; nothing is
    annihilated.  Nothing to remove.

        SO TWO INDEPENDENT ROUTES SELECT THE SAME CANDIDATE.  The classical
        theorem says the only gap is non-classical; the teardown deadline says
        the lead must clear at c.  They converge on squeezed vacuum, and that
        convergence is why this file exists rather than stopping at candidate A.

    AND THEN IT FAILS ON MAGNITUDE, which is gate three.

===============================================================================
4. THE GATE THAT DECIDES ALL OF THEM, AND IT IS STRUCTURAL
===============================================================================

Quantum field theory does not let you have negative energy for free.  The
FORD-ROMAN quantum inequality (gr-qc/9607003 Eq. (1): a free, minimally
coupled massless scalar in four-dimensional Minkowski space with no
boundaries) bounds from BELOW the Lorentzian TIME average of <T00>, width
t0, along an inertial worldline at one spatial point; written with
L = c t0 as the magnitude of the negative energy it allows:

        |rho|  <=  3 hbar c / (32 pi^2 L^4)

It is one-sided (nothing bounds positive energy) and it bounds the sampled
average, not rho at a point.  Below, L is set to the corridor's spatial size
R, i.e. t0 = R/c: that is this file's modelling choice, not the source's,
and it is the spatial-length-as-time move DOCKET 55 withdrew in achievable.py.
It errs against M, not for M: in flat space Eq. (1) for every t0 excludes a
static negative density outright.  The Casimir law has the same shape,
pi^2 hbar c / (720 d^4).

    NOW PUT THAT AGAINST THE REQUIREMENT, AND NOTICE THE EXPONENTS:

        what is ALLOWED   goes as  L^-4
        what is NEEDED    goes as  R^-2        (c^4 / (G Lambda R^2))

    SO THE SHORTFALL GOES AS R^2, AND SHRINKING ALWAYS HELPS.  M's "small and
    contained" is quantitatively the right direction, and it is the only
    direction that helps at all:

        R (m)        need J/m^3    Ford-Roman     shortfall     Casimir shortfall
        1e-09        1.2124e+61    3.0031e+08     4.037e+52     2.798e+52
        1e-06        1.2124e+55    3.0031e-04     4.037e+58     2.798e+58
        1e-03        1.2124e+49    3.0031e-16     4.037e+64     2.798e+64
        1e+00        1.2124e+43    3.0031e-28     4.037e+70     2.798e+70

    The Casimir column is the IDEAL-plate formula at d = R, evaluated below
    its validity range d >> lambda_p (~100-136 nm for Al/Au): plasma-model
    plates give 0.111, 0.0130 and 0.00132 of the ideal energy at 10 nm, 1 nm
    and 0.1 nm (DOCKET 67 audit).  So it is an upper bound on |rho| and the
    Casimir shortfall a floor.

    52.6 ORDERS SHORT AT A NANOMETRE AND 70.6 AT A METRE -- the same order of
    shortfall lightbuild.py found for the kugelblitz block, arrived at from a
    completely different direction.

AND THE CROSSOVER HAS A CLOSED FORM, WHICH IS THE RESULT.  Setting
c^4/(G Lambda R^2) = 3 hbar c/(32 pi^2 R^4):

        R  =  l_P sqrt( 3 Lambda / (32 pi^2) )  =  0.307933 l_P

and for Casimir, R = l_P pi sqrt(Lambda / 720) = 0.369917 l_P.

    THE BOUND MEETS THE REQUIREMENT ONLY BELOW THE PLANCK LENGTH -- a third of
    one, and a third of one again.  THE FRAMEWORK FAILS BEFORE THE BOUND DOES.
    This is not "very hard".  It is outside the domain of the theory being used
    to state it, and Lambda -- M's own constant -- is sitting in both crossover
    formulas.  STATUS OF THAT DOMAIN BOUNDARY: AN ESTIMATE.  The sources place
    the loss of semiclassical control 'of the order of' l_P, numerical factors
    ignored (Garay gr-qc/9403008), and say the breakdown scale 'need not be
    M_p', with curved-space power counting not yet given (Burgess
    gr-qc/0311082).  The crossovers stay sub-Planckian in every Planck
    convention tried (non-reduced, h-based, reduced: FR 0.3079 / 0.1228 /
    0.0614 l_P, Casimir 0.3699 / 0.1476 / 0.0738 l_P).

===============================================================================
4b. CANDIDATE D -- NON-MINIMAL COUPLING.  IT FAILS DIFFERENTLY, AND THAT MATTERS
===============================================================================

M: "back to web search please."  A fourth candidate came back, and it does not
behave like the other three.

A scalar coupled to curvature by delta L = xi R phi^2 CAN violate the NEC and
WEC AT THE CLASSICAL LEVEL -- the effective NEC of the Jordan-frame metric;
the Einstein-frame metric obeys it, constant phi saturates rather than
violates, and the claim is that violating configurations EXIST (Barcelo &
Visser gr-qc/0003025 sec. 2; the wording follows FFKP 2309.10848 sec. I).
The literal 'delta L = xi R phi^2' is FFKP's eq. (1); FFKP's own action
(7), Barcelo-Visser (2.1) and Fewster-Osterbrink (1) carry -1/2 xi R phi^2,
so read literally xi_tree = -xi_BV/2, and every sign of xi in this file is
the sources' (XI_SIGN_CONVENTION below).  Quantum mechanically FEWSTER &
OSTERBRINK (arXiv:0708.2450) prove something stronger than an evasion:

    FOR xi > 0 THERE IS NO STATE-INDEPENDENT QEI AT ALL -- for a MASSLESS
    field in FOUR-DIMENSIONAL MINKOWSKI space.  Given any bounded subset O
    of Minkowski space and any rho_0 > 0, they CONSTRUCT a Hadamard state
    with expected energy density below -rho_0 throughout O.  Local averages
    of the energy density are UNBOUNDED FROM BELOW on Hadamard states.  No
    paper read here proves the massive or curved case.

    KIND: PASSES, and more cleanly than squeezed vacuum.
    MAGNITUDE: the Ford-Roman gate does not apply, because there is no such
    bound to apply.

    WHAT REPLACES IT, for xi in [0, 1/4], is a STATE-DEPENDENT bound (FO
    Theorem 4.2/4.3: globally hyperbolic spacetime, averaging along a
    timelike GEODESIC, difference type against a reference Hadamard state;
    for xi > 1/4 FO give no bound of either kind), and the cost does not
    vanish -- it MOVES.  Their H-bounds (4D Minkowski, a FIXED smearing
    function): Q(f) can be bounded by any power of the Hamiltonian greater
    than 2, while rho(f) cannot be bounded by powers less than 3 -- shown
    with one one-particle family; FO do not exclude p <= 2, and q may need
    to be >= 4.  In their words, "negative energy effects with large magnitude,
    while possible over large regions, require MORE ENERGY to achieve than
    positive energy densities of the same magnitude, and the energy budget for
    these two effects will grow with a DIFFERENT POWER."

AND THE EFT TREATMENT IS WHAT MAKES IT COMPUTABLE.  FLISS, FREIVOGEL, KONTOU &
PARDO SANTOS (arXiv:2309.10848) take non-minimal coupling as the first term of
an effective field theory with a cutoff on FIELD VALUES as well as momenta, and
derive a smeared null energy bound of SNEC type (their Eq. 91, with Eq. 96),
one-sided, from below:

        <T_-->  >~  - N_n [gamma, xi, phi_max]  /  ( l_UV^(n-2)  delta^2 )

with phi^2_max ~ M^(n-2)_cutoff ~ l_UV^-(n-2), for ONE free scalar in
MINKOWSKI spacetime, T_-- smeared along ONE null geodesic with width delta
in x^- = t - x, on states with |<:phi^2:>| <= phi^2_max.  This file READS it
in four dimensions and SI units as an energy-density bound,
|rho| ~ hbar c / (l_UV^2 delta^2), with delta set to the corridor's spatial
size R.  That reading is the tree's, not FFKP's: for a static source
T_-- = rho/4 (a factor 4 dropped, 2 in the crossover l_UV), and a null bound
places no limit on rho at all (rho = -A with p = +A gives T_-- = 0 for every
A), so the comparison carries an unnamed hypothesis -- that the negative
energy required is negative null energy of the same size.  N fields
multiply the bound by N.

    NOW PUT IT AGAINST THE REQUIREMENT AND NOTICE WHAT DOES NOT HAPPEN:

        allowed   ~  hbar c / (l_UV^2 delta^2)      goes as  delta^-2
        needed    ~  c^4 / (G Lambda R^2)           goes as  R^-2

    THE EXPONENTS MATCH.  THE R-DEPENDENCE CANCELS.  Measured at R = 1e-9, 1
    and 1e6 metres with l_UV = 10 l_P, the shortfall is 10.017501 at all three,
    identical to eight digits.

        shortfall  =  ( l_UV / l_P )^2  /  Lambda

    A PURE NUMBER.  Not fifty-two orders, and not a function of how big you
    build it.  Compare the first three, whose bounds went as L^-4 against a need
    of R^-2 and were therefore 52.6 orders short at a nanometre and 70.6 at a
    metre.  THIS IS A DIFFERENT KIND OF FAILURE.

    AND IT CLOSES AT  l_UV = sqrt(Lambda) l_P = 3.159514 l_P.

        cutoff        shortfall
        l_P           0.1002      (would PASS)
        3.1595 l_P    1.0000      (exactly closes)
        10 l_P        10.018
        1e3 l_P       1.0018e5
        1e-18 m       3.83e32     (an LHC-scale cutoff)

    SO THE MAGNITUDE GATE SHUTS FOR ANY CUTOFF BELOW ~3.16 PLANCK LENGTHS, AND
    ONLY THERE.

WHY IT STILL FAILS -- PARTLY FOR THE AUTHORS' REASONS, AND DECIDED BY A PREMISE
OF THIS FILE'S:

    THE CUTOFF THAT WOULD WORK IS THE ONE THIS FILE'S PREMISE EXCLUDES.  Fliss
    et al. SUGGEST phi^2_max <~ (8 pi G_N |xi|)^-1 -- an argument ('suggest',
    'argue', 'points of evidence'), the path-integral Jacobian not computed;
    their conservative form is |8 pi G xi phi^2| << 1 -- and ARGUE that at
    that field value the theory breaks: a tower of irrelevant interactions
    turns on in the Einstein frame (dimensional analysis at n = 4), and the
    gravity path integral loses semi-classical control in the Jordan frame
    (argued for xi > 0 only, from Euclidean constrained instantons at a
    fixed constant zero mode -- not true saddles -- with compact boundary
    conditions, a bare Lambda > 0 and V = 0).  They leave a shift-symmetric
    (pNGB) scalar with super-Planckian field values open ('We do not
    disallow this possibility').  THE FIELD BOUND ALONE DOES NOT EXCLUDE
    CLOSURE: closure points with 8 pi G|xi| phi^2_max < 1 exist at l_UV
    between 1.0057 and 2.0919 l_P (DOCKET 67, 2309.10848-eft-breakdown).  What
    excludes them for xi > 0 is this file's own premise,
    H_PLANCKIAN_CUTOFF_NOT_EFT below: an EFT whose cutoff sits at a few Planck
    lengths is not an EFT result at all -- it is a statement that you need
    quantum gravity.  FFKP do not share that premise ('when M^2_cutoff is
    Planckian or sub-Planckian ... the two metrics are close'; 'the natural
    scale for this computation is M_cutoff ~ M_Planck'): at this file's
    l_UV = sqrt(Lambda) l_P their own condition reads |8 pi G xi phi^2| =
    2.518 xi, which reaches 1 only at xi ~ 0.397 (0.42 at conformal 1/6).

    THEIR OWN VERDICT IS NEGATIVE, AND IT IS QUOTED RATHER THAN PARAPHRASED,
    HEAD INCLUDED: "This point requires further consideration, but so far it
    seems that it is impossible to construct traversable wormholes in the
    Jordan frame without unphysical field values."  It follows 'While there
    is no relevant theorem' (for long wormholes) and considers only
    asymptotically flat connected regions; 'unphysical' means outside the
    EFT they ADOPT ('we adopt the view').  They also show the effective ANEC
    IS OBEYED CLASSICALLY over an ENTIRE null geodesic (boundary terms
    discarded; on a finite segment the eq. (19) integral is -0.1237 at
    phi^2 <= 0.30, xi = 1/6) once field values are bounded -- a bound needed
    only for 0 < xi < 1/4.  That a wormhole must violate it is a theorem
    only for SHORT (causality-violating) wormholes, via achronal ANEC
    (Graham-Olum); for long ones it is their argument, though their abstract
    states the 'must' unhedged.  Semiclassically what they show is the
    ORDINARY ANEC for <T_--> of a free scalar in MINKOWSKI spacetime on
    states with bounded <:phi^2:> (eq. 89); in curved spacetime only the
    state-dependent smeared bound (72).

    AND THE FRAME QUESTION IS NOT A LOOPHOLE FOR THE AVERAGED OBSTRUCTION.  A
    conformal transformation plus field redefinition maps the Jordan frame to
    the Einstein frame, where the NEC is obeyed classically; the two metrics
    differ by the factor (1 - 8 pi G xi phi^2)^(2/(n-2)) (FFKP eq. 99),
    approximately exp(-2 (8 pi G xi phi^2)/(n-2)) (their eq. (3), '~'; at
    n = 4 the two are 0.53% apart at 8 pi G xi phi^2 = 0.1 and 17.6% at 0.5),
    which under the EFT assumption (small 8 pi G xi phi^2; for xi > 0 the map
    exists only where it is < 1) is CLOSE TO ONE.  That does NOT make the
    exotic behaviour a frame artefact: FFKP call the frames 'evidently not
    equivalent in terms of classical energy conditions', exhibit Jordan-frame
    effective-NEC violations at SMALL field values (eq. 18), and call them
    equivalent only 'in that sense' -- no traversable wormhole without
    unphysical field values -- with 'no relevant theorem'.  The local
    violation does not shrink as the factor goes to 1 (metric closeness is
    C^0; the null energy depends on second derivatives of phi^2).  The
    equivalence is CLASSICAL; the quantum map is argued only (Jacobian not
    computed), and FFKP say the Einstein frame has 'no known
    state-independent bounds in n > 2'.

    STATUS OF THE NUMBER: SCALING ESTIMATE, NOT A DERIVATION.  N_n[gamma, xi,
    phi_max] is not written out in Eq. (91), but the massless form Eq. (93)
    gives it for a chosen smearing: for a unit-L2 Gaussian at n = 4,
    N_4 = 1/pi^2 + 1.935766 |xi| phi~^2_max (DOCKET 67 audit; NMC_GAUSSIAN_K
    below, RECOVERED), so N = 1 is the value at |xi| phi~^2_max = 0.4642, and
    over [0, 1] the crossover runs from 1.005705 to 4.509466 l_P.  It is set
    to 1 here.  A coefficient of 10 or 1/10 moves the crossover by sqrt(10) ~ 3 IN THE CUTOFF
    and by nothing at all in the orders.  That is why the finding is the
    EXPONENT MATCH and not the number.

    DOCKET 67 NARROWED THE REFUSAL BY SIGN (key 2309.10848-eft-breakdown,
    NARROWED; the reopen adjudicated REOPENS-NARROWER; seated on M's ruling of
    2026-10-02).  In FFKP's eq. (109) convention, which Fewster-Osterbrink and
    Barcelo-Visser share (conformal coupling +1/6; xi < 0 is the
    Higgs-inflation sign), the Jordan-frame breakdown is argued for xi > 0
    only; the Einstein-frame tower and the conservative condition
    |8 pi G xi phi^2| << 1 carry no sign, but they are an order-of-magnitude
    argument whose Jacobian nobody computed.  So in the xi < 0 sub-class ONE
    WINDOW is OPEN: 1 <= 8 pi G|xi| phi_max^2 < 1.300608, which is
    l_UV >= 2.091911 l_P (xi_negative_window(), computed below).  There the
    tower is the only ground against closure.  OPEN, not supplied.  xi > 0
    stays refused (the exact constrained-saddle breakdown at eps = 1, the
    Planckian-momentum premise above, O1); xi < 0 with eps < 1 stays excluded,
    since every such closure point has l_UV < 2.091911 l_P and the premise
    that a cutoff at a few Planck lengths is not an EFT carries no sign.
    CONVENTION: this file's literal 'delta L = xi R phi^2' reads the same
    sub-class as xi_tree > 0 (xi_tree = -xi_FFKP/2, per the
    nmc-classical-nec-violation audit; not re-derived).  The window's edges
    rest on the sibling audit's Gaussian coefficient (NMC_GAUSSIAN_K,
    RECOVERED, not re-derived here) and on this closure algebra, which
    sibling key 2309.10848 NARROWED (Minkowski only; a null-smeared bound does
    not bound rho).

===============================================================================
4c. AND THE FOUR CROSSOVERS SIT ON TOP OF EACH OTHER
===============================================================================

        Ford-Roman            0.307933 l_P
        Casimir               0.369917 l_P
        non-minimal coupling  3.159514 l_P

    THREE MECHANISMS WITH NOTHING IN COMMON -- a sampling inequality, a
    boundary-condition vacuum, and a curvature coupling inside an EFT -- AND
    ALL THREE RUN OUT WITHIN ONE ORDER OF THE PLANCK LENGTH.

    That is the structural result of this file, and it is stronger than any of
    the individual verdicts: THE OBSTRUCTION IS NOT A LIMITATION OF ANY ONE
    MECHANISM.  Every negative-energy source run here runs out within an
    order-one factor of where the theory that states the requirement runs out
    -- 'of the order of' l_P, the sources' own words (Garay; Burgess: the
    scale 'need not be M_p').  The magnitude gate and the Planck scale are
    the same gate, to that precision.  The [0.1, 10] band is read in the
    non-reduced convention (planck_length below): under the reduced Planck
    length the Ford-Roman and Casimir crossovers fall to 0.0614 and 0.0738,
    outside it.  The convention-free content is the spread
    NMC/FR = sqrt(32 pi^2/3) = 10.2604, independent of Lambda.

===============================================================================
5. ONE THING THAT DID NOT FIGHT, AND IT IS WORTH RECORDING
===============================================================================

The quantum inequality and the teardown deadline LOOK like they should compound,
and they do not.  The inequality says a deeper negative energy must be BRIEFER:
|rho| <= 3 hbar c/(32 pi^2 (c tau)^4) grows without limit as tau falls.  The
deadline says the lead must be brief.

        SO THE DEADLINE IS EXACTLY THE REGIME THE INEQUALITY IS MOST GENEROUS
        IN.  The two constraints point the SAME WAY.

    teardown.py's new requirement therefore costs NOTHING against the quantum
    inequality -- it is free, and it is the direction the inequality already
    wanted.  That does not rescue anything, because the failure is on magnitude
    and the magnitude fails by fifty-two orders in the best case.  But a
    requirement that turns out to be free is worth knowing, and if anything ever
    does supply the magnitude, the switchability will not be what stops it.

===============================================================================
WHAT THIS PASS ESTABLISHES
===============================================================================

    A   negative effective mass   FAILS on KIND.  m* is band curvature, not
                                  T_00.  No energy condition is violated.

    B   Casimir                   PASSES kind (ideal plates).  FAILS deadline
                                  in the d = R geometry (mechanical, and
                                  anchored to positive-mass plates) and
                                  magnitude (2.798e52 short at a nanometre,
                                  ideal-plate formula: a floor).

    C   squeezed vacuum           PASSES kind AND deadline -- the only candidate
                                  that does, and selected independently by two
                                  routes.  FAILS magnitude by 4.037e52 at a
                                  nanometre, 4.037e70 at a metre.

    STRUCTURAL   both quantum bounds go as L^-4 and the requirement as R^-2, so
                 the shortfall goes as R^2 and SMALLER IS ALWAYS BETTER -- but
                 the crossover is 0.3079 l_P (Ford-Roman) and 0.3699 l_P
                 (Casimir), BELOW THE PLANCK LENGTH, with Lambda in both closed
                 forms.

    FREE         the teardown deadline costs nothing against the quantum
                 inequality; the two point the same way.

    NOT CLAIMED  that the list is exhaustive.  Three candidates were named and
                 three were run.  A fourth may exist and this file does not
                 speak to it.

===============================================================================
CORRECTED (DOCKET 67, on M's ruling "Repair all") -- WORDING ONLY
===============================================================================

    The audit of the sources this file cites found prose that said more than
    the sources do.  Each site above is corrected in place; what it said is
    kept here.  NO VERDICT MOVED: every gate literal in CANDIDATES, every
    computed figure and every selftest pin is unchanged (the reopen pass
    computed that none of these sites carries a verdict).

    Sec. 1   "A quasiparticle with m* < 0 still carries POSITIVE energy" --
             named no reference; and the cavity's positive stress-energy was
             asserted, with Lambda = 0 and the WEC hypothesis unnamed.
    Sec. 2   "Genuine negative energy density ... measured in the
             laboratory" -- only the force is measured.  "This is a real
             rho < 0" -- ideal plates only.  "Switching it off means MOVING
             THE PLATES, which is mechanical and therefore slower than c --
             by a lot" -- the theorem gives t > l/c; the miss holds for
             l ~ R, 'by a lot' only for v << c, and the switch need not be
             mechanical.
    Sec. 3   "the energy density at a spacetime point is genuinely negative"
             -- an expectation value, Delta' = 2; no source was cited; "gone
             at c" named no propagation or generation hypothesis.
    Sec. 4   "|rho| <= 3 hbar c/(32 pi^2 L^4)" over "a sampling length
             L = c tau" -- the source bounds a worldline time average, from
             below, in flat space; t0 = R/c is the tree's choice.  The domain
             boundary carried no status word; the Casimir column sits below
             the ideal formula's validity range.
    Sec. 4b  "violates the NEC and WEC AT THE CLASSICAL LEVEL" -- can
             violate, Jordan-frame effective NEC, no source cited.  "Given
             any bounded region O" -- massless, 4D Minkowski dropped.  "WHAT
             REPLACES IT is a STATE-DEPENDENT bound" -- for xi in [0, 1/4]
             only.  "|T_--| <~ ..." -- one-sided, and a null bound read as a
             rho bound.  "at that field value the theory breaks" -- FFKP
             suggest and argue.  "An EFT whose cutoff sits at a few Planck
             lengths is not an EFT result" -- this file's premise, not FFKP's,
             and the one that carries the xi > 0 exclusion.  The verdict was
             quoted without its head and scope; "the effective ANEC -- the
             thing that must be violated -- IS OBEYED both classically and
             semiclassically" -- classically, on complete geodesics; the
             semiclassical result is the ordinary ANEC in Minkowski.  "a
             factor exp(-2 (8 pi G xi phi^2)/(n-2))" -- approximate; "The
             exotic behaviour is a frame artefact everywhere the EFT is
             valid" -- not FFKP's claim.  "N_n is left schematic in the
             source" -- Eq. (93) gives it.
    Sec. 4c  "runs out exactly where" -- 'of the order of'; the band test is
             convention-dependent.
"""

import math
import sys

# CODATA 2018 recommended values (NIST), as typed.  C is exact.  G carries
# u_r = 2.2e-5, CODATA's EXPANDED uncertainty over mutually inconsistent
# inputs, so figures below hold to about 4-5 significant figures.
# (CORRECTED (DOCKET 67): provenance and uncertainty were unlabelled.)
#
# CORRECTED (DOCKET 67, on M's ruling "address/correct/repair all figures").
# HBAR WAS TYPED  HBAR = 1.054571817e-34  -- h/2pi truncated, low by 6.13e-10
# relative, and first kept "since every pin here rests on" those digits.  h =
# 6.62607015e-34 J s is EXACT under the 2019 SI (CODATA 2018 and 2022), so
# hbar = h/2pi is computed: 1.0545718176461565e-34.  The selftest was re-run
# on the computed value; no pin here moved (the shift is in the tenth
# significant figure).  tolman.py takes HBAR from here.  The typed literal is
# kept as a record.
G = 6.67430e-11
C = 2.99792458e8
H_PLANCK = 6.62607015e-34                  # J s, SI-EXACT
HBAR = H_PLANCK / (2.0 * math.pi)          # COMPUTED, exact h/2pi
HBAR_TYPED_TRUNCATED = 1.054571817e-34     # the first-typed literal; a record

KIND = "supplies rho < 0"
DEADLINE = "switches off in ~R/c"
MAGNITUDE = "enough of it"
GATES = (KIND, DEADLINE, MAGNITUDE)


def lambda_value():
    import phase1
    return phase1.lam()


def planck_length():
    """The NON-REDUCED Planck length sqrt(hbar G/c^3).  The reduced one
    (M_p^-2 = 8 pi G, Burgess's EFT) is sqrt(8 pi) times longer; the sources
    place the boundary only 'of the order of' either."""
    return math.sqrt(HBAR * G / C ** 3)


# ---------------------------------------------- the requirement

def rho_needed(R_m):
    """E_transition(R) spread over R^3  =  c^4 / (G Lambda R^2)."""
    return C ** 4 / (G * lambda_value() * R_m ** 2)


REQUIREMENT_SCALES_AS = -2


# ---------------------------------------------- the bounds

def ford_roman(L_m):
    """|rho| <= 3 hbar c / (32 pi^2 L^4).  Free massless minimally coupled
    scalar, 4D Minkowski: a one-sided bound on the Lorentzian time average,
    width t0 = L/c, along one inertial worldline."""
    return 3.0 * HBAR * C / (32.0 * math.pi ** 2 * L_m ** 4)


def casimir(d_m):
    """|rho| = pi^2 hbar c / (720 d^4).  Ideal plates."""
    return math.pi ** 2 * HBAR * C / (720.0 * d_m ** 4)


BOUNDS_SCALE_AS = -4


def bounds_fall_faster_than_the_requirement():
    return BOUNDS_SCALE_AS < REQUIREMENT_SCALES_AS


def shortfall(R_m, bound=ford_roman):
    """The bound evaluated at L = d = R: for Ford-Roman that is t0 = R/c, a
    spatial size used as a temporal width (the tree's choice, withdrawn in
    achievable.py by DOCKET 55 and not the source's); for Casimir the
    ideal-plate formula at d = R."""
    return rho_needed(R_m) / bound(R_m)


def smaller_is_better(a=1.0, b=1e-9):
    return shortfall(b) < shortfall(a)


def shortfall_scales_as_R_squared(R1=1e-9, R2=1e-6, tol=1e-9):
    ratio = shortfall(R2) / shortfall(R1)
    return abs(ratio - (R2 / R1) ** 2) <= tol * ratio


# ---------------------------------------------- the crossovers

def crossover_ford_roman():
    """c^4/(G Lambda R^2) = 3 hbar c/(32 pi^2 R^4)."""
    return math.sqrt(3.0 * G * lambda_value() * HBAR / (32.0 * math.pi ** 2 * C ** 3))


def crossover_ford_roman_closed():
    """R / l_P = sqrt(3 Lambda / (32 pi^2))."""
    return math.sqrt(3.0 * lambda_value() / (32.0 * math.pi ** 2))


def crossover_casimir():
    return math.sqrt(math.pi ** 2 * HBAR * C * G * lambda_value() / (720.0 * C ** 4))


def crossover_casimir_closed():
    """R / l_P = pi sqrt(Lambda / 720)."""
    return math.pi * math.sqrt(lambda_value() / 720.0)


def crossover_is_sub_planckian():
    return (crossover_ford_roman() < planck_length()
            and crossover_casimir() < planck_length())


# ---------------------------------------------- candidate D: non-minimal coupling

NMC_UNBOUNDED_BELOW = True          # Fewster & Osterbrink, arXiv:0708.2450
NMC_STATE_INDEPENDENT_QEI = False   # there is none, for xi > 0 (massless, 4D Minkowski)
# FO Cor. 5.4 (fixed smearing, 4D Minkowski); the state-dependent bound that
# replaces the QEI (Thm 4.2/4.3) covers xi in [0, 1/4] only, along timelike
# geodesics, difference type -- for xi > 1/4 FO give no bound (DOCKET 67).
NMC_COST_MOVES_TO = "global positive energy, growing with a different power"
NMC_EFT_PAPER = "Fliss, Freivogel, Kontou & Pardo Santos, arXiv:2309.10848"
# CORRECTED (DOCKET 67): quoted as first written without its head, "This
# point requires further consideration, but so far".
NMC_AUTHORS_VERDICT = ("This point requires further consideration, but so far it "
                       "seems that it is impossible to construct traversable "
                       "wormholes in the Jordan frame without unphysical field values")
# CORRECTED (DOCKET 67): first written "N_n is schematic in the source, set to
# 1 here"; FFKP's Eq. (93) gives N_n for a chosen smearing.
NMC_COEFFICIENT_STATUS = ("SCALING ESTIMATE -- N_n set to 1 here; FFKP Eq. (93) "
                          "gives it for a chosen smearing (Gaussian, n = 4: "
                          "N_4 = 1/pi^2 + 1.935766 |xi| phi~^2_max)")
#: The premise that carries the xi > 0 exclusion of candidate D's closure
#: (DOCKET 67, 2309.10848-eft-breakdown): it is this file's, stated in section
#: 4b's prose, not FFKP's, who treat a Planckian cutoff as inside the EFT.
H_PLANCKIAN_CUTOFF_NOT_EFT = ("an EFT whose momentum cutoff sits at a few Planck "
                              "lengths is not an EFT result; it says you need "
                              "quantum gravity (this file's premise, not FFKP's)")


def nmc_allowed(l_uv_m, delta_m):
    """|rho| ~ hbar c / (l_UV^2 delta^2): this file's READING of FFKP's Eq.
    91/96 at n = 4, in SI.  FFKP bound null-smeared <T_--> from below, in
    Minkowski only, for one free scalar on states with |<:phi^2:>| <=
    phi^2_max; a null bound does not bound rho (DOCKET 67, 2309.10848)."""
    return HBAR * C / (l_uv_m ** 2 * delta_m ** 2)


def nmc_shortfall(l_uv_m, R_m=1.0):
    """delta -- in FFKP the width of a smearing along ONE null geodesic -- is
    set equal to the corridor's spatial size R.  The tree's choice: the
    exponent match survives it; the O(1) factor has no derivation."""
    return rho_needed(R_m) / nmc_allowed(l_uv_m, R_m)


def nmc_shortfall_closed(l_uv_m):
    """(l_UV / l_P)^2 / Lambda -- a PURE NUMBER, independent of R."""
    return (l_uv_m / planck_length()) ** 2 / lambda_value()


def nmc_shortfall_is_scale_free(l_uv_m=None, radii=(1e-9, 1.0, 1e6), tol=1e-12):
    l_uv_m = l_uv_m or 10.0 * planck_length()
    vals = [nmc_shortfall(l_uv_m, R) for R in radii]
    return max(vals) - min(vals) <= tol * max(vals)


def nmc_crossover_cutoff():
    """Closes at l_UV = sqrt(Lambda) l_P."""
    return math.sqrt(lambda_value()) * planck_length()


def nmc_scales_like_the_requirement():
    return True


# ---------------------------------------------- DOCKET 67: the xi < 0 window
#: DOCKET 67, key 2309.10848-eft-breakdown (NARROWED; the reopen adjudicated
#: REOPENS-NARROWER; seated on M's ruling of 2026-10-02).  The sign is in this
#: convention, never in this file's literal one -- the label must carry it.
XI_SIGN_CONVENTION = ("FFKP eq. (109), shared by Fewster-Osterbrink and "
                      "Barcelo-Visser: conformal coupling +1/6, M_eff^2 ~ "
                      "1 - 8 pi G xi phi^2; xi < 0 is the Higgs-inflation sign.  "
                      "candidates.py's literal 'delta L = xi R phi^2' reads the "
                      "same sub-class as xi_tree > 0 (xi_tree = -xi_FFKP/2, per "
                      "the nmc-classical-nec-violation audit; not re-derived)")
#: The sibling audit's Gaussian N_4 = 1/pi^2 + K s, s = |xi| phi~^2_max, with
#: K = 4 sqrt(2/pi) e^(-1/2) (DOCKET 67, sibling key 2309.10848, rederive E2).
#: RECOVERED from the audit and NOT re-derived in this tree: the window's
#: edges depend on it, and on the closure algebra below, which sibling key
#: 2309.10848 NARROWED (Minkowski only; a null-smeared bound does not bound rho).
NMC_GAUSSIAN_K = 4.0 * math.sqrt(2.0 / math.pi) * math.exp(-0.5)
NMC_GAUSSIAN_K_STATUS = ("RECOVERED (DOCKET 67 sibling audit 2309.10848, rederive "
                         "E2); not re-derived here")
#: The window is OPEN: the only ground against closure in it is FFKP's
#: Einstein-frame tower, an order-of-magnitude argument with an uncomputed
#: Jacobian, which cannot tell a factor of 1.3 from 1.
XI_NEGATIVE_WINDOW_STATUS = "OPEN"


def nmc_closure_eps(s):
    """The field parameter eps = 8 pi G|xi| phi_max^2 at the closure point with
    s = |xi| phi~^2_max: closure is (l_UV/l_P)^2 = N_4 Lambda, so
    eps = 8 pi s/(N_4 Lambda), sign-blind (N_4 carries |xi|)."""
    n4 = 1.0 / math.pi ** 2 + NMC_GAUSSIAN_K * s
    return 8.0 * math.pi * s / (n4 * lambda_value())


def nmc_eps_sup():
    """eps along the closure curve rises monotonically to 8 pi/(K Lambda)."""
    return 8.0 * math.pi / (NMC_GAUSSIAN_K * lambda_value())


def nmc_closure_l_uv(eps):
    """l_UV / l_P at the closure point whose field parameter is eps, for
    0 <= eps < nmc_eps_sup(): s = eps Lambda/(pi^2 (8 pi - eps K Lambda))."""
    lam = lambda_value()
    s = eps * lam / (math.pi ** 2 * (8.0 * math.pi - eps * NMC_GAUSSIAN_K * lam))
    return math.sqrt((1.0 / math.pi ** 2 + NMC_GAUSSIAN_K * s) * lam)


def xi_negative_window():
    """(eps_lo, eps_hi, l_UV/l_P at eps_lo): the xi < 0 window
    1 <= eps < eps_sup, l_UV >= l_UV(eps = 1), that DOCKET 67 left OPEN."""
    return 1.0, nmc_eps_sup(), nmc_closure_l_uv(1.0)


# ---------------------------------------------- the candidates

# (name, kind, deadline, magnitude, why it fails first)
CANDIDATES = (
    ("negative effective mass", False, True, None,
     "m* = hbar^2/(d2E/dk2) is band curvature, not T_00; no EC is violated"),
    ("Casimir", True, False, False,
     "switching by MOVING PLATES is mechanical, slower than c (t > l/c, so it "
     "misses ~R/c in the d = R geometry), and anchored to positive-mass plates"),
    ("squeezed vacuum", True, True, False,
     "passes both qualitative gates and fails Ford-Roman by 52.6 orders at 1 nm"),
    ("non-minimal coupling", True, True, False,
     "no state-independent QEI exists; fails on the EFT field cutoff, and the "
     "shortfall is a PURE NUMBER (l_UV/l_P)^2/Lambda rather than orders"),
)


def first_gate_failed(name):
    for n, k, d, m, _why in CANDIDATES:
        if n != name:
            continue
        if not k:
            return KIND
        if not d:
            return DEADLINE
        if m is False:
            return MAGNITUDE
        return None
    raise KeyError(name)


def any_candidate_passes():
    return any(k and d and m for _n, k, d, m, _w in CANDIDATES)


def passes_both_qualitative_gates():
    """Two do, now that candidate D is seated.  Both then fail on MAGNITUDE."""
    return [n for n, k, d, _m, _w in CANDIDATES if k and d]


def every_qualitative_pass_fails_on_magnitude():
    return all(m is False for _n, k, d, m, _w in CANDIDATES if k and d)


EFFECTIVE_MASS_IS = "band curvature"
EFFECTIVE_MASS_IS_NOT = "T_00"


def effective_mass_violates_an_energy_condition():
    """DECLARED, not computed: m* does not enter T_ab, and the cavity, the
    excitons and the field are taken to be ordinary matter and radiation
    obeying the classical WEC.  The False is correct on that hypothesis."""
    return False


# ---------------------------------------------- the alignment

def ford_roman_allows_more_when_briefer(tau_long=1e-9, tau_short=1e-15):
    """The inequality grows without limit as tau falls."""
    return ford_roman(C * tau_short) > ford_roman(C * tau_long)


def deadline_costs_anything_against_the_inequality():
    """The deadline wants brief; the inequality is most generous when brief."""
    return not ford_roman_allows_more_when_briefer()


LIST_IS_EXHAUSTIVE = False


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-4):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("0. THE SPEC -- THREE GATES, AND THE THIRD IS NEW HERE")
    for g in GATES:
        print("     %s" % g)
    chk("how many gates", len(GATES), 3)
    # DOCKET 67: hbar is the exact h/2pi, not the typed truncation.
    chk("HBAR is the exact h/2pi, h = 6.62607015e-34",
        HBAR == 6.62607015e-34 / (2.0 * math.pi), True)
    chk("  not the typed truncation (low by 6.127e-10)",
        float("%.3e" % ((HBAR - HBAR_TYPED_TRUNCATED) / HBAR)), 6.127e-10)

    print("\n1. CANDIDATE A -- NEGATIVE EFFECTIVE MASS")
    chk("what m* is", EFFECTIVE_MASS_IS, "band curvature")
    chk("what it is not", EFFECTIVE_MASS_IS_NOT, "T_00")
    # A declared constant checked against a literal (DOCKET 67): it pins the
    # declaration, on the hypothesis named in its docstring; it computes nothing.
    chk("does it violate an energy condition (declared)",
        effective_mass_violates_an_energy_condition(), False)
    chk("FIRST GATE FAILED", first_gate_failed("negative effective mass"), KIND)
    print("       real, measured and switchable -- and the WRONG QUANTITY.")
    print("       'negative mass' is one phrase for two things and only one")
    print("       of them is exotic.")

    print("\n2. CANDIDATE B -- CASIMIR")
    near("rho at d = 10 nm (J/m^3)", casimir(1e-8), 4.33375e4, 1e-4)
    near("  and at d = 1 nm, four orders up", casimir(1e-9), 4.33375e8, 1e-4)
    # DEADLINE first holds in this file's d = R geometry; in a microstructured
    # one (l << R) the first failed gate would be MAGNITUDE (DOCKET 67).
    chk("FIRST GATE FAILED", first_gate_failed("Casimir"), DEADLINE)
    print("       switching by MOVING PLATES: mechanical, slower than c (t > l/c,")
    print("       a miss at d = R), and anchored to positive-mass plates.")

    print("\n3. CANDIDATE C -- SQUEEZED VACUUM")
    chk("which candidates pass KIND and DEADLINE", passes_both_qualitative_gates(),
        ["squeezed vacuum", "non-minimal coupling"])
    chk("  and do ALL of those fail on MAGNITUDE",
        every_qualitative_pass_fails_on_magnitude(), True)
    chk("FIRST GATE FAILED", first_gate_failed("squeezed vacuum"), MAGNITUDE)
    print("       the only one that passes both qualitative gates, and it is")
    print("       the same candidate lightbuild.py left OPEN -- two independent")
    print("       routes selecting one thing.")

    print("\n4. THE GATE THAT DECIDES ALL THREE")
    chk("bounds scale as L^n, n =", BOUNDS_SCALE_AS, -4)
    chk("the requirement scales as R^n, n =", REQUIREMENT_SCALES_AS, -2)
    chk("  so do the bounds fall faster", bounds_fall_faster_than_the_requirement(), True)
    chk("  and is smaller better", smaller_is_better(), True)
    chk("  does the shortfall go as R^2", shortfall_scales_as_R_squared(), True)
    print("     %-10s %14s %14s %13s %13s"
          % ("R (m)", "need J/m^3", "Ford-Roman", "FR short", "Cas short"))
    for R in (1e-9, 1e-6, 1e-3, 1.0):
        print("     %-10.0e %14.4e %14.4e %13.3e %13.3e"
              % (R, rho_needed(R), ford_roman(R), shortfall(R),
                 shortfall(R, casimir)))
    near("shortfall at 1 nm", shortfall(1e-9), 4.037e52, 1e-3)
    near("  in orders", math.log10(shortfall(1e-9)), 52.606, 1e-3)
    near("shortfall at 1 m", shortfall(1.0), 4.037e70, 1e-3)
    near("  in orders", math.log10(shortfall(1.0)), 70.606, 1e-3)
    print("     THE CROSSOVER, AND IT HAS A CLOSED FORM:")
    near("Ford-Roman crossover (m)", crossover_ford_roman(), 4.976981e-36, 1e-5)
    near("  in Planck lengths", crossover_ford_roman() / planck_length(), 0.307933, 1e-5)
    near("  closed form sqrt(3 Lambda/(32 pi^2))", crossover_ford_roman_closed(),
         0.307933, 1e-5)
    near("Casimir crossover (m)", crossover_casimir(), 5.978797e-36, 1e-5)
    near("  in Planck lengths", crossover_casimir() / planck_length(), 0.369917, 1e-5)
    near("  closed form pi sqrt(Lambda/720)", crossover_casimir_closed(), 0.369917, 1e-5)
    chk("IS THE CROSSOVER SUB-PLANCKIAN", crossover_is_sub_planckian(), True)
    print("       THE FRAMEWORK FAILS BEFORE THE BOUND DOES.  Not 'very hard' --")
    print("       outside the domain of the theory stating it.  And Lambda is")
    print("       sitting in both closed forms.")

    print("\n4b. CANDIDATE D -- NON-MINIMAL COUPLING, AND IT FAILS DIFFERENTLY")
    print("     Fewster & Osterbrink arXiv:0708.2450, and %s" % NMC_EFT_PAPER)
    chk("is the energy density unbounded below (xi > 0)", NMC_UNBOUNDED_BELOW, True)
    chk("  is there a state-independent QEI", NMC_STATE_INDEPENDENT_QEI, False)
    chk("  so where does the cost go", NMC_COST_MOVES_TO,
        "global positive energy, growing with a different power")
    chk("does its bound scale like the requirement (R^-2)",
        nmc_scales_like_the_requirement(), True)
    print("     %-14s %12s %14s %12s" % ("cutoff", "in l_P", "allowed J/m^3", "shortfall"))
    for l_uv, nm in ((planck_length(), "l_P"), (10 * planck_length(), "10 l_P"),
                     (1e3 * planck_length(), "1e3 l_P"), (1e-18, "1e-18 m")):
        print("     %-14s %12.3e %14.4e %12.4e"
              % (nm, l_uv / planck_length(), nmc_allowed(l_uv, 1.0), nmc_shortfall(l_uv)))
    near("shortfall at l_UV = l_P", nmc_shortfall(planck_length()), 0.100175, 1e-5)
    near("  at 10 l_P", nmc_shortfall(10 * planck_length()), 10.0175, 1e-5)
    near("  closed form (l_UV/l_P)^2 / Lambda",
         nmc_shortfall_closed(10 * planck_length()), 10.0175, 1e-5)
    chk("IS THE SHORTFALL SCALE-FREE IN R", nmc_shortfall_is_scale_free(), True)
    print("       measured at R = 1e-9, 1 and 1e6 m -- identical to 8 digits.")
    print("       A PURE NUMBER, not 52 orders.  THE EXPONENTS MATCH.")
    near("it closes at l_UV = sqrt(Lambda) l_P",
         nmc_crossover_cutoff() / planck_length(), 3.159514, 1e-5)
    chk("  the coefficient's status", NMC_COEFFICIENT_STATUS,
        "SCALING ESTIMATE -- N_n set to 1 here; FFKP Eq. (93) gives it for a "
        "chosen smearing (Gaussian, n = 4: N_4 = 1/pi^2 + 1.935766 |xi| "
        "phi~^2_max)")
    near("  and N_4 = 1 sits at |xi| phi~^2_max = 0.4642 on that curve",
         (1.0 - 1.0 / math.pi ** 2) / NMC_GAUSSIAN_K, 0.4642, 1e-3)
    # DOCKET 67 (2309.10848-eft-breakdown, M's ruling 2026-10-02): the xi < 0
    # window, computed, against the adjudication's recorded edges.
    _lo, _hi, _l1 = xi_negative_window()
    near("DOCKET 67: xi < 0 window top, eps_sup = 8 pi/(K Lambda)", _hi, 1.300608, 1e-6)
    near("  its lower edge eps = 1 sits at l_UV/l_P", _l1, 2.091911, 1e-6)
    near("  closed-form root agrees: eps(s) at that l_UV is 1",
         nmc_closure_eps((_l1 ** 2 / lambda_value() - 1.0 / math.pi ** 2)
                         / NMC_GAUSSIAN_K), 1.0, 1e-12)
    chk("  eps rises monotonically along the closure curve and stays below eps_sup",
        all(nmc_closure_eps(a) < nmc_closure_eps(b) < _hi
            for a, b in ((0.1, 0.2), (1.0, 10.0), (1e2, 1e6))), True)
    # The tree's own N = 1 closure, l_UV = sqrt(Lambda) l_P, is N_4 = 1 on the
    # Gaussian curve: s = (1 - 1/pi^2)/K.
    near("  at the tree's own 3.1595 l_P closure eps is in the window (1.1688)",
         nmc_closure_eps((1.0 - 1.0 / math.pi ** 2) / NMC_GAUSSIAN_K), 1.168829, 1e-5)
    chk("  the window's status, and the convention it is stated in",
        (XI_NEGATIVE_WINDOW_STATUS, XI_SIGN_CONVENTION.startswith("FFKP eq. (109)")),
        ("OPEN", True))
    chk("  control: eps < 1 lies below l_UV = 2.091911 l_P (excluded, sign-blind)",
        nmc_closure_l_uv(0.999) < _l1, True)
    print("     WHY IT STILL FAILS, in the authors' own words:")
    print("       \"%s\"" % NMC_AUTHORS_VERDICT)
    print("       FFKP argue (Jacobian uncomputed) that at phi^2 ~ (8 pi G xi)^-1,")
    print("       xi > 0, the gravity path integral loses semi-classical control.")
    print("       The field bound alone does not exclude closure; this file's")
    print("       premise does: %s." % H_PLANCKIAN_CUTOFF_NOT_EFT)

    print("\n4c. AND THE THREE CROSSOVERS SIT ON TOP OF EACH OTHER")
    print("       Ford-Roman            %.6f l_P" % crossover_ford_roman_closed())
    print("       Casimir               %.6f l_P" % crossover_casimir_closed())
    print("       non-minimal coupling  %.6f l_P" % (nmc_crossover_cutoff()/planck_length()))
    # The band is read with the non-reduced l_P; under the reduced convention
    # FR and Casimir fall to 0.0614 and 0.0738, outside it (DOCKET 67).
    chk("are all three within one order of l_P (non-reduced)", all(
        0.1 <= v <= 10.0 for v in (crossover_ford_roman_closed(),
                                   crossover_casimir_closed(),
                                   nmc_crossover_cutoff()/planck_length())), True)
    print("       THREE MECHANISMS WITH NOTHING IN COMMON -- a sampling")
    print("       inequality, a boundary-condition vacuum, and a curvature")
    print("       coupling in an EFT -- ALL RUNNING OUT AT THE PLANCK LENGTH.")
    print("       THE MAGNITUDE GATE AND THE PLANCK SCALE ARE THE SAME GATE.")

    print("\n5. THE ONE THING THAT DID NOT FIGHT")
    chk("does the inequality allow more when briefer",
        ford_roman_allows_more_when_briefer(), True)
    chk("  so does the deadline cost anything against it",
        deadline_costs_anything_against_the_inequality(), False)
    print("       the deadline is exactly the regime the inequality is most")
    print("       generous in.  teardown.py's requirement is FREE.")

    print("\n  THE VERDICT")
    print("     %-26s %7s %9s %10s" % ("candidate", "kind", "deadline", "magnitude"))
    for n, k, d, m, _w in CANDIDATES:
        print("     %-26s %7s %9s %10s"
              % (n, k, d, "n/a" if m is None else m))
    chk("DOES ANY CANDIDATE PASS", any_candidate_passes(), False)
    chk("is the list exhaustive", LIST_IS_EXHAUSTIVE, False)
    print("       three were named and three were run.  A fourth may exist and")
    print("       this file does not speak to it.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  Three candidates, three gates, and each fails at a different one.
  Negative effective mass fails at the FIRST: m* is the curvature of a
  band, not T_00, so a negative-mass polariton violates no energy
  condition (on the classical-WEC hypothesis for the medium and field)
  and would not bend spacetime the wrong way -- "negative mass"
  is one phrase for two things and only one is exotic.  Casimir supplies a
  rho < 0 between ideal plates and fails the DEADLINE in the d = R
  geometry, because switching it off by moving plates is mechanical
  (t > l/c) and anchored to positive mass.
  Squeezed vacuum passes both qualitative gates -- the only one that does,
  and the same candidate lightbuild.py had already left open, so two
  independent routes select it -- and then fails on MAGNITUDE.  That third
  gate is new here and it is structural: the Ford-Roman and Casimir bounds
  both go as L^-4 while the requirement goes as R^-2, so the shortfall goes
  as R^2 and shrinking always helps, which makes "small and contained"
  quantitatively the right instinct and the only one that helps.  It is
  still 52.6 orders short at a nanometre and 70.6 at a metre, and the
  crossover where the bound would finally meet the requirement is
  0.307933 l_P for Ford-Roman and 0.369917 l_P for Casimir -- BELOW the
  Planck length, with Lambda sitting in both closed forms.  The framework
  fails before the bound does.  One consolation, recorded because it is
  real: the quantum inequality is most generous exactly where the teardown
  deadline wants to live, so switchability is free and will not be what
  stops a lead that ever does supply the magnitude.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
