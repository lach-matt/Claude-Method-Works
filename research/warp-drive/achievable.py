#!/usr/bin/env python3
"""
achievable.py -- is there a core that can actually be made?  NO.

M: "we have to determine our core, and it must be something achievable, not
something hypothetical."  That is the right demand and this file answers it, and
the answer is still NO -- but THE GROUND THIS FILE FIRST ANSWERED ON WAS WRONG.
DOCKET 55 withdrew it in place.  The withdrawals, their reasons and the
replacement are the last section of this docstring, and every passage below that
a withdrawal touches carries its own marker.

    WHAT FELL.  This file read Ford & Roman's quantum inequality as a cap on
    |rho| over a SPATIAL scale L, called that cap a theorem, and priced the core
    against it.  Ford & Roman's inequality is a TIME average at ONE SPATIAL
    POINT, and the first line of their own introduction is that "the energy
    density may be unboundedly negative at a spacetime point".  There is no
    pointwise cap to price anything against.  The "sixty-five orders" that stood
    in this sentence was computed from that misreading, with the inequality's own
    coefficient dropped, and IT IS NOT A PUBLISHABLE FIGURE.

    WHAT STANDS, AND IT IS A DIFFERENT SENTENCE.  A corridor must HOLD its
    contraction for at least one light-crossing or it transmits nothing, and the
    worldline QEI's DURATION bound prices exactly that.  Measured here in this
    file's own geometry: 71.256 orders short at b = 1 m, widening as b^2, with
    the sampling time now FORCED by the transit rather than chosen.  The census
    below names real effects; what each MEASURED is stated item by item, and
    for none of them is it a negative energy density.

-- THE CENSUS OF REAL EFFECTS CITED FOR NEGATIVE ENERGY DENSITY ---------------
Everything real, what was measured, and what bounds it:

  CASIMIR between IDEAL plates    the FORCE is MEASURED (parallel plates at
                                  0.5-3 um, Bressi 2002).  rho = -pi^2 hbar c/
                                  (720 d^4) is the ideal perfect-conductor
                                  density, computed, valid for d >> lambda_p.
  SQUEEZED VACUUM                 sub-vacuum quadrature noise <:X^2:> < 0
                                  MEASURED (LIGO uses it).  Negative <:T_00:>
                                  is INFERRED, under the single-mode
                                  identification and for t0 < 3.1e-16 s; at
                                  LIGO's resolution the average is positive.
                                  Ford-Roman bounded (free field, Minkowski).
  DYNAMICAL CASIMIR               photon generation and two-mode squeezing
                                  MEASURED (Wilson 2011, superconducting
                                  circuit, arXiv:1105.4714).  No energy
                                  density was measured.
  HAWKING flux (analogue)         the outgoing flux is analogue-observed
                                  (restated in 2106.03960 p.1).  Its negative
                                  energy density is a computed test-field
                                  result for gravitational holes, UNPERFORMED
                                  in any analogue (door.py).  "Unruh" stood
                                  here too: the Unruh EFFECT carries zero
                                  energy density, and no Unruh analogue
                                  measurement is cited.
  VACUUM POLARISATION             the Lamb shift is MEASURED, as a frequency
                                  interval.  Its VP part is one term of the
                                  QED sum, not isolated, and it strengthens
                                  the Coulomb field.  The energy-condition-
                                  violating VP is the curved-space
                                  semiclassical one, and it is unmeasured.

    CORRECTED -- DOCKET 67.  What stood above, verbatim, was a header "THE
    CENSUS OF KNOWN NEGATIVE ENERGY DENSITY", the sentence "The census of real
    negative-energy sources below stands item by item", and the rows
    "CASIMIR between boundaries  MEASURED.  rho = -pi^2 hbar c/(720 d^4)",
    "SQUEEZED VACUUM  MEASURED (LIGO uses it)", "DYNAMICAL CASIMIR  MEASURED
    (Wilson 2011, superconducting circuit)", "HAWKING / UNRUH flux
    analogue-measured; same family" and "VACUUM POLARISATION  MEASURED via
    the Lamb shift".  Each row put a measured effect under a negative-energy-
    density header; what each experiment measured is now the row.  The
    correction removes census members and so cannot weaken the SURVEY
    refusal; it opens nothing either, since no row was ever a supply of the
    required sign and magnitude.

    WITHDRAWN IN PLACE -- DOCKET 55.  What stood here, verbatim, was:

        "ALL OF THEM OBEY ONE BOUND.  Ford & Roman's quantum inequality caps
         negative energy sustained over a scale L at |rho| <~ hbar c / L^4, and
         Casimir is that bound saturated, not an exception to it.  This is a
         theorem about quantum field theory, not a limit of apparatus."

    All three clauses fail, each against the paper it names, read at source.
    The DOCKET 55 section quotes them.  What replaces the sentence is a bound on
    DURATION, not on magnitude -- and the duration bound is real, exact, and
    still refuses the core.

THREE THINGS THAT LOOK LIKE EXCEPTIONS AND ARE NOT, named because they are the
most likely next hope:

  DARK ENERGY as a cosmological constant (w = -1) has negative PRESSURE and
  POSITIVE energy density for every observer.  rho_Lambda > 0 (Planck 2018).
  A component with w < -1, which DESI DR2's w0wa fits reach at z > 0.35-0.50,
  is negative only for a boosted observer; its comoving density is positive in
  every fit read.  It is the wrong sign of the wrong quantity.

  "EFFECTIVE NEGATIVE MASS" in BECs and metamaterials is a curvature of a
  DISPERSION RELATION -- how a quasiparticle responds to a force in a medium.
  m* is not T_00, m* does not gravitate (the quasiparticle's energy does, as
  E/c^2), and a negative m* will not source a metric.  The same caution
  applies to negative-index metamaterials, which are about the refractive
  index: under the dispersive (Brillouin) energy density in a low-loss band,
  that is not the energy density.

    CORRECTED -- DOCKET 67.  This read "TWO THINGS" over three entries;
    "DARK ENERGY has negative PRESSURE and POSITIVE energy density", with
    w = -1 implied and never stated; "It is not T_00, it does not gravitate",
    which is true of m* and false of the quasiparticle; and the metamaterial
    line without the dispersive form its energy density needs.

-- THE PRICE, AND IT IS NOT CLOSE ---------------------------------------------
concentric.py's device at corridor radius b needs a core of size a = 0.02 b
carrying mass m/b >~ 5e-3, so its energy density is

        required  =  (m/b) c^4 / [ G b^2 (4/3) pi (0.02)^3 ]  ~  1.81e46 / b^2  Pa

against what this file CALLED the quantum bound over the core's own size:

        available =  hbar c / (0.02 b)^4  ~  1.98e-19 / b^4  Pa   <- WITHDRAWN

    This is the one line the docket turned on.  It reads a SPATIAL core radius
    into a TEMPORAL sampling slot, sets the sampling fraction to 1 with no
    argument, and drops Ford & Roman's own 3/(32 pi^2) -- measured here as
    105.276x more generous than the inequality they actually printed.  The table
    is kept, because it is correct arithmetic and four other files pin it, but it
    is a RATIO OF TWO DENSITIES and not a bound.  Nothing asserts that quantity.

        b               required (Pa)     available (Pa)    avail/req
        1 m             1.806e+46         1.976e-19         1.09e-65
        100 km          1.806e+36         1.976e-39         1.09e-75
        solar system    1.806e+22         1.976e-67         1.09e-89
        1 light-year    1.806e+14         1.976e-83         1.09e-97
        10 kly          1.806e+06         1.976e-99         1.09e-105

-- THE GAP WIDENS WITH SIZE.  THE TREND SURVIVES; ITS REASON DID NOT ----------
Required falls as 1/b^2; the withdrawn "available" falls as 1/b^4.  So on the
file's original curves, going bigger makes it worse by two powers.

    WITHDRAWN IN PLACE -- DOCKET 55, the REASON only.  The 1/b^4 is a function
    of b solely because this file CHOSE the sampling length to be 0.02 b.  Ford,
    Helfer and Roman prove that no purely spatially averaged quantum inequality
    exists over a bounded region, for the massless minimally coupled free
    scalar in four-dimensional Minkowski spacetime, so no spatial theorem ties
    a sampling length to the region's size, and on the original ground the
    trend had no warrant.
        CORRECTED -- DOCKET 67.  This read "Ford, Helfer and Roman prove the
        sampling scale need not track the region at all": an inference from
        their theorem, not a sentence of the paper.

    THE TREND IS RESCUED BY A DIFFERENT ROUTE AND THE EXPONENT IS UNCHANGED.
    Price the core against the DURATION bound with the hold time set by the
    transit it must support, T = b/c, and the shortfall goes exactly as b^2 --
    measured 2.000000 over a decade -- because T is now forced by the geometry
    instead of chosen.  71.256 orders at 1 m, 77.256 at 1 km, 103.256 at a
    light-year.  "Go bigger" is still closed, and now it is closed on a
    sampling scale nobody picked.

    AND overturn.py's L3 closes it a second way with no quantum input at all:
    the strong field returns strictly LESS distance per unit |m|, 0.833 at
    |m| = 1 falling to 0.0035 at |m| = 1e4.

The two original curves cross only at

        b = 3.31e-33 m,   core size a = 6.62e-35 m  =  4.09 PLANCK LENGTHS

    WITHDRAWN IN PLACE -- DOCKET 55.  What stood here was "THIRD INDEPENDENT
    ROUTE TO THE PLANCK SCALE ... When three unrelated estimates land at the
    Planck scale, that is where the physics is, not where the arithmetic went."

    IT IS WHERE THE ARITHMETIC WENT.  Setting hbar c/L^4 = K c^4/(G L^2) gives
    L = l_P/sqrt(K) for ANY dimensionless K, so every crossover of this shape is
    l_P times an O(1) number BY CONSTRUCTION.  This file's crossing is
    l_P/(alpha sqrt(k)) with alpha sqrt(k) = 0.244301, reproducing its own
    measured 4.0933 to four digits.  It is a dimensional identity, not evidence,
    and it is fragile as well as circular.  Ford & Roman (gr-qc/9510071) sample
    at tau_0 = f r_m, a fraction f << 1 of the smallest curvature radius r_m,
    and take f ~= 0.01 in their curved-throat examples (eqs 51, 69, Sec. 5.1)
    but f ~= 0.1 for Casimir plates (Sec. 4.5), as Pfenning-Ford take
    alpha = 1/10.  Applied to the core radius a in place of r_m, and with
    Ford-Roman's 3/(32 pi^2) included, the crossing core goes as f^-2 from
    0.399 l_P: 3989 l_P at f = 0.01 (four decades from 0.399, about three from
    the 4.09 above) and 39.9 l_P at f = 0.1.  At every sourced f it moves at
    least a decade.  The number is kept because gjw.py pins it; its STATUS is
    now DIMENSIONAL IDENTITY, never a route to the Planck scale.
        CORRECTED -- DOCKET 67.  This read "at Ford & Roman's own practice of
        sampling at a hundredth of the geometric scale the crossing core moves
        to 3989 l_P, four decades away": the practice is not uniform, F&R's
        scale is r_m and not a (in this core r_c/a is 0.82 to 2.0, which
        puts the f = 0.01 figure at 997..5984 l_P), the 3/(32 pi^2) was
        silent, and "four decades" is counted from 0.399, not from 4.09.

And even taking the BOUND as though it were an apparatus:

        Casimir gap 10 nm (unsourced)         ->  needs b = 7.6e19 m  (8000 ly)
        Casimir gap 0.1 nm (below contact)    ->  needs b = 7.6e15 m  (0.8 ly)

    CORRECTED -- DOCKET 55, and the correction STRENGTHENS the row.  Those two
    lines used quantum_bound(gap), not this file's own casimir_density(gap).
    The ideal-plate Casimir density is 72.951x smaller than the bound, so even
    ideal plates need a corridor sqrt(72.951) = 8.541x larger:

        Casimir gap 10 nm, IDEAL plates     ->  b = 6.5e20 m  (68,000 ly)
        Casimir gap 0.1 nm, IDEAL plates    ->  b = 6.5e16 m  (6.8 ly)

    This is the soundest argument in the file and it was the one understated.
    It is also a CENSUS claim about apparatus, not a theorem, and must be
    reported as one.  A core 0.02 of that is still thousands of astronomical
    units of continuous atomic-separation vacuum apparatus, for the WEAKEST
    configuration in the window.  This is not an engineering programme.

    CORRECTED -- DOCKET 67, and again the correction runs in the refusing
    direction.  The rows read "10 nm (state of the art)", "0.1 nm (atomic
    floor)" and "MEASURED effect".  (i) What Casimir experiments measure is the
    force -- between parallel plates only at 0.5-3 um, sphere-plate down to
    ~120 nm -- never the energy density.  casimir_density is the IDEAL
    perfect-conductor density, which needs d >> lambda_p (gold 137.8 nm), as
    scale.py itself states; at 10 nm real gold gives 0.1099 of it (T = 0
    Lifshitz, plasma model at 9.0 eV, computed in the DOCKET 67 audit), so the
    10 nm corridor is 1.95e21 m, not 6.5e20.  (ii) "State of the art" carried
    no source and no date; that census datum is OPEN.  (iii) 0.1 nm is below
    gold's nearest-neighbour distance, 0.288 nm, so below atomic contact, where
    no continuum Casimir energy exists: that row is a generous bound, not an
    apparatus.  The figures above are kept as ideal-plate upper bounds on |rho|;
    every correction lowers |rho| and lengthens the corridor.

-- WHAT THIS DOES AND DOES NOT SETTLE -----------------------------------------
IT DOES NOT RETRACT THE DEVICE.  concentric.py's configuration is a valid
solution: M_ADM = 0, a vacuum corridor, seats and leads over most of a decade,
a shell of ordinary matter that is radially stable for free, and a Type I core
whose exoticism is exactly one sign.  Every one of those stands.

WHAT IT SETTLES IS THAT THE CORE IS NOT BUILDABLE WITH KNOWN PHYSICS.  The
second half of that sentence -- "and the shortfall is a theorem rather than a
budget" -- is WITHDRAWN IN PLACE, DOCKET 55.  No theorem of the right shape caps
the ball integral, and Ford, Helfer and Roman prove that none can exist over a
bounded region in four-dimensional Minkowski spacetime, by a counterexample in
the massless minimally coupled free scalar.  What does exist is a DURATION
theorem, and it is narrower than a theorem about nature: it holds for the
massless minimally coupled scalar and all Hadamard states, in flat space, and
Fewster (1208.5399 Sec. 5.1, after Fewster-Osterbrink 0708.2450) reports that
the massless scalar NONMINIMALLY coupled with xi > 0 in Minkowski space sustains
arbitrarily negative energy density over arbitrarily large spacetime volumes,
so it admits no state-independent QEI at all (that phrase is his Sec. 5.2's).
The verdict therefore rests on a convergence of proven limits, which is a
SURVEY and not a theorem, and it must be reported as one.
    CORRECTED -- DOCKET 67.  This read "Fewster states in print that the
    NONMINIMALLY coupled scalar admits no state-independent QEI at all": a
    paraphrase given as Sec. 5.1's wording, with the sign xi > 0, masslessness
    and Minkowski space dropped.

    WITHDRAWN IN PLACE -- DOCKET 55.  What stood here was:

        "THE HONEST STATEMENT OF THE PROJECT IS NOW ONE SENTENCE: a complete,
         self-consistent, stability-checked warp architecture whose single unmet
         requirement is a matter type no known physics provides, with the
         shortfall quantified at 65 orders of magnitude and shown to widen with
         scale."

    THE CORRECTED SENTENCE: a complete, self-consistent, stability-checked warp
    architecture whose single unmet requirement is a matter type no known
    physics provides; whose demand cannot be refused by any spatial bound,
    because Ford-Helfer-Roman prove no such bound exists; and which is
    nonetheless refused, on the PERSISTENCE axis, by 71.256 orders at metre
    scale for the one field where a state-independent QEI is proven.  "65
    orders" is not the banked figure -- candidates.py gets 70.606 at the same
    metre from the same inequality, differing only in an unargued sampling
    choice worth 8.8 orders -- and it must not be quoted.

NOT SETTLED: whether some physics beyond the standard framework supplies it.
That is a question this project cannot ask, and pretending otherwise would be
the failure mode every withdrawal in this tree was about.

===============================================================================
DOCKET 55 -- THE WITHDRAWALS, WITH THE SOURCES THAT FORCED THEM
===============================================================================

bounds.py and this file contradicted each other in print and neither named the
other.  bounds.py was right.  The three sentences that carried the fault:

(1) "Ford & Roman's quantum inequality caps negative energy sustained over a
    scale L at |rho| <~ hbar c / L^4."  FALSE -- WRONG FUNCTIONAL, WRONG
    VARIABLE.  Ford & Roman, "Restrictions on Negative Energy Density in Flat
    Spacetime", gr-qc/9607003, read at source.  Their Eq. (1), verbatim:

        rho-hat == (t_0/pi) INT <T_00> dt/(t^2 + t_0^2)  >=  -3/(32 pi^2 t_0^4)

    and p.4, verbatim: "the energy density is evaluated in the reference frame
    of an inertial observer, AT AN ARBITRARY SPATIAL POINT WHICH WE CHOOSE TO BE
    x = 0.  The time coordinate t is the proper time of this observer."  It is a
    TIME average at ONE POINT.  It caps nothing "over a scale L" in space, and
    it is not pointwise -- their introduction (p.2) says "the energy density
    may be UNBOUNDEDLY NEGATIVE at a spacetime point", and credits the fact to
    their ref. [2], Epstein, Glaser and Jaffe, Nuovo Cim. 36, 1016 (1965).  As
    restated (Kontou-Sanders 2003.01815; Fewster math-ph/0501073), EGJ prove
    that negative values occur; unboundedness is a further, scaling, result,
    shown for free fields over Hadamard states (Fewster 1208.5399 p.8).  A
    pointwise lower bound is the very thing quantum inequalities exist because
    there is not.
        CORRECTED -- DOCKET 67.  This read 'the first line of their
        introduction is "..." (Epstein, Glaser and Jaffe ...)', placing the
        citation in the quotation; the line carries none, and EGJ is credited
        there with the fact, of which it proves the nonpositivity half.

(2) "Casimir is that bound saturated, not an exception to it."  NEVER SHOWN,
    AND REFUTED BY CALCULATION FOR FEWSTER'S BOUND.  Fewster, "Lectures on
    quantum energy inequalities", arXiv:1208.5399 Sec. 1.3, read at source,
    derives the a priori bound T_00 >= -C/(2 l)^4 for a trajectory at distance
    l from a Casimir plate and states that the known Casimir density -- that of
    the massless minimally coupled scalar between ideal Dirichlet plates --
    "ranges between 3-7% of the bound".  Reproduced from his own expression by
    bounds.py's casimir_fraction_of_bound (no code here computes it): 6.8% at
    the midpoint, 3.4% and 3.2% at z/L = 0.2 and 0.4, on his printed 1140,
    which is a misprint for 1440 (6.7%, 3.3%, 3.2% on 1440).  He then asks, in
    print, "why is the Casimir energy density a comparatively small proportion
    of the allowed bound?"  Saturation of Fewster's bound is not 3 %.  Two
    limits on that: Fewster states the bound rests on Eq. (3), which "is known
    not to be optimal", so saturation of the SHARP bound would need a sharp
    constant C/14.9 at the midpoint, which is OPEN; and his bound is not Ford &
    Roman's -- in their own capped treatment (gr-qc/9510071 Sec. 2) the
    constant Casimir density meets their Eq. (1) with equality at the cap
    tau_0 <= 0.46 L, by construction.  bounds.py carries the same
    overstatement in its Ford-Roman row and it is recorded there.
        CORRECTED -- DOCKET 67.  The status read "REFUTED BY MEASUREMENT":
        Fewster's 3-7% is a CALCULATION (an ideal Dirichlet scalar density over
        a derived bound), and no measured quantity enters it.  The withdrawal
        stands because saturation was never shown; it is not a refutation of
        "saturated" in Ford-Roman's own sense.

(3) "This is a theorem about quantum field theory, not a limit of apparatus."
    FALSE, AND IT WAS THE LOAD-BEARING SENTENCE.  The flat-space theorem is
    about a worldline time average and does not reach a ball integral.  Ford,
    Helfer and Roman, "Spatially Averaged Quantum Inequalities Do Not Exist in
    Four-Dimensional Spacetime", PRD 66 124012, gr-qc/0208045, read at source,
    prove the reverse: for every spatial sampling function of finite width,
    S(F) = INT d^3x F(x) <:T_00:> at fixed time is UNBOUNDED BELOW, over a
    sequence of Hadamard states that SATISFY the temporal inequality.  Their
    summary, verbatim: "there are no purely spatially averaged quantum
    inequalities over bounded regions in four-dimensional Minkowski spacetime,
    even though the integral over all space is bounded."  And Ford & Roman's own
    word for the curved-spacetime step is "argued" -- gr-qc/9607003 Sec. 4,
    p.11: "Recently we argued that such bounds should also hold in a curved
    spacetime and/or one with boundaries, if the sampling time is restricted to
    be much smaller than the smallest local radius of curvature and/or the
    distance to any boundaries in the spacetime [23]."  They cite two
    supporting cases (Eq. (1) proved for Casimir plates at sampling times much
    smaller than the separation, p.2; a QI in the static Robertson-Walker
    universes that reduces to theirs, [24]), and Kontou & Olum, 1410.0665,
    later proved the scalar case to first order in curvature -- still a
    worldline TIME average, so nothing here reaches a ball integral.
        CORRECTED -- DOCKET 67.  The quotation closed after "radius of
        curvature." without "and/or the distance to any boundaries in the
        spacetime [23]", used p.2's word order, capitalised "IF" inside the
        quotation marks, and omitted the two supporting cases and the later
        proof, understating the curved step.

THE REPLACEMENT, AND IT IS WHY THE VERDICT SURVIVES.  Fewster 1208.5399 Eq. (4),
read at source: if <T_00> < rho throughout an interval of duration tau, then

        rho  >=  -C/tau^4,   C = mu_1^4/(16 pi^2),  cos(mu_1) cosh(mu_1) = 1

where C is the least eigenvalue of d^4/dt^4 on the interval under clamped
boundary conditions, divided by 16 pi^2.  Computed here by bisection, stdlib:
mu_1 = 4.730040744862704 and C = 3.169857938310467, reproducing Fewster's
printed "C ~ 3.17".  NO COEFFICIENT.

    WHY THIS IS LICENSED WHERE THE OLD READING WAS NOT.  Eq. (4) is a statement
    at EACH SPATIAL POINT SEPARATELY, about a DURATION.  It never averages in
    space, so Ford-Helfer-Roman -- whose witness states are explicitly transient
    and explicitly obey the temporal inequality -- is powerless against it.  The
    corridor is static over the interval, so the per-point bound may be applied
    at each point of the core and summed.  The sampling time is the transit
    requirement itself, T = b/c, so the free factor that cost the old reading
    8.8 orders is gone.

    FOUR LIVE CAVEATS, none cosmetic.  (a) massless MINIMALLY coupled scalar,
    Hadamard states; Fewster Sec. 5.1 states that for the NONMINIMALLY coupled
    field (massless, xi > 0, Minkowski space, after Fewster-Osterbrink
    0708.2450) "states of arbitrarily negative energy density can be sustained
    over arbitrarily large spacetime volumes", and his Sec. 5.2 says that for
    interacting fields "one cannot expect state-independent QEIs to hold" --
    an expectation, which the same section qualifies: QEIs hold in a large
    class of two-dimensional conformal field theories, and "modified QEIs" may
    hold.  (b) Fewster states the bound "is known not to be optimal".
    (c) boundary-free flat space.  Fewster & Teo, gr-qc/9812032, give a QEI
    with no curvature cap for a free minimally coupled scalar on a globally
    static spacetime, in the Fock space on the static vacuum (not shown
    optimal: in 2D it is 1.5 times weaker than Flanagan's optimal bound).
    Their flat massless bound is 9/64 of Ford-Roman's FOR FORD-ROMAN'S
    LORENTZIAN SAMPLER -- and C above ALREADY IS that family's constant at the
    clamped optimum, the infimum over compactly supported samplers, which lies
    outside F&T's smooth class: F&T (5.6) at C = 0, i.e. Minkowski, returns
    mu_1^4/(16 pi^2) there (fewsterteo.py, by Parseval).  So NO 64/9
    adjustment applies to C; taking log10(64/9) = 0.852 orders off the refusal
    would count one tightening twice.  Their own conclusions name the curved
    evaluation for a static wormhole as still to be done; their Schwarzschild section shows the bound
    going arbitrarily negative near a horizon ("at least in the present
    approximation", F&T's words), and its mode basis is defined
    by that horizon, which the corridor lacks; and (5.6) is derived only for
    Minkowski and the static open Robertson-Walker universe, so it is not a
    formula of the corridor and supplies no curvature tightening there.  The
    flat figure below stands under flat space, an assumed hypothesis
    (fewsterteo.py, DOCKET 62): F&T's own zero-gap Schwarzschild case differs
    from flat, and their Einstein static universe at gap C = 5 is looser than
    flat.
        CORRECTED IN PLACE -- DOCKET 62.  This caveat read "-- 9/64 of
        Ford-Roman's in the Minkowski limit, so TIGHTER --", which invites a
        void 0.851937-order adjustment to C.  Kept here so the correction
        names what it corrects; NINE_64_APPLIES_TO_C pins the refusal.
        That is the ONLY phrase DOCKET 62 corrected.  The clause "their
        Schwarzschild section shows the bound going arbitrarily negative near
        a horizon" was NOT withdrawn and stays in the LIVE text above: the
        consolidation's first rewrite of (c) dropped it, which the ruling did
        not order, and it is restored verbatim.  The mode-basis sentence
        beside it is ADDED (ruling 62 O2(c): F&T Sec. 7 is not continued to
        the corridor because the horizon is its mode-defining surface); it
        does not replace the clause.
        CORRECTED IN PLACE -- DOCKET 67.  (a) put the interacting-field clause
        under "Sec. 5.1" (it is Sec. 5.2) and left the nonminimal coupling
        unsigned and without massless or Minkowski; (c) read "an EXACT QEI for
        static spacetimes", "OPTIMAL COMPACTLY SUPPORTED sampler", "F&T (5.6)
        at zero spectral gap returns mu_1^4/(16 pi^2) exactly", and "on an
        asymptotically flat corridor the spectral gap that could tighten (5.6)
        is zero, so the flat figure below stands" -- (5.6) is undefined on the
        corridor.  The horizon clause gains F&T's own qualifier; it is not
        withdrawn.
    (d) it prices persistence and says nothing at an
    instant, which is exactly consistent with Ford-Helfer-Roman.

    SO THE VERDICT IS NO-IN-PRACTICE AND NOT NO-BY-THEOREM.  Nothing here is a
    theorem about all matter.  Saying otherwise is the error this docket
    repaired, one level up.

    NOT A NEW SHORTFALL.  71.256 orders at a metre is the SAME inequality family
    as candidates.py's banked 70.606; it differs by the sampling choice and the
    geometry.  Do not report it as an independent confirmation.

stdlib only.  concentric.py supplies the device, seatindex.py the threshold,
corridor.py the two earlier Planck-scale crossings.  Ford & Roman gr-qc/9607003,
Ford-Helfer-Roman gr-qc/0208045, Fewster arXiv:1208.5399 and Fewster & Teo
gr-qc/9812032 were all read at source in the Docket 55 pass.
"""
import math, sys

# CODATA 2018, unchanged in CODATA 2022 for these four (DOCKET 67 provenance).
# c is exact.  HBAR is h/2pi TRUNCATED to ten figures: the exact value is
# 1.0545718176...e-34, so HBAR is low by 6.1e-10 relative.  G = 6.67430(15)e-11
# carries u_r 2.2e-5, so no figure here is fixed by G past 4-5 significant
# figures.  L_PLANCK = 1.616255(18)e-35 m.
HBAR = 1.054571817e-34
HBAR_C = HBAR * 299792458.0
C_SI = 299792458.0
G_SI = 6.67430e-11
L_PLANCK = 1.616255e-35

M_OVER_B = 5.0e-3          # concentric.py's window, weakest end
A_OVER_B = 0.02            # the vacuum-corridor constraint


def required_density(b, m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    """|rho| c^2 the core must carry, in Pa, at corridor radius b."""
    M = m_over_b * b * C_SI ** 2 / G_SI
    V = (4.0 / 3.0) * math.pi * (a_over_b * b) ** 3
    return M * C_SI ** 2 / V


def quantum_bound(L):
    """WITHDRAWN AS A BOUND -- DOCKET 55.  Kept because four other files pin the
    numbers it feeds, and because the arithmetic is correct.  It is NOT
    Ford-Roman: theirs is a TIME average at one spatial point carrying a
    coefficient 3/(32 pi^2), and for free fields in Minkowski space no
    pointwise lower bound on rho exists over Hadamard states (a scaling
    argument, Fewster 1208.5399 p.8; Epstein-Glaser-Jaffe 1965, which
    gr-qc/9607003 cites on p.2, proves that negative values occur).
    CORRECTED (DOCKET 67): this read "no pointwise cap on |rho| exists at all
    (Epstein-Glaser-Jaffe 1965, quoted in gr-qc/9607003's first line)".  Read
    this as "hbar c over the fourth power of a length", a dimensional estimate
    with no theorem behind it.  Use ford_roman_allow or duration_bound instead."""
    return HBAR_C / L ** 4


def ford_roman_allow(t0):
    """The inequality Ford & Roman actually printed, gr-qc/9607003 Eq. (1):
    a LORENTZIAN TIME average at one spatial point, over sampling time t0.
        rho-hat  >=  -3 hbar /(32 pi^2 c^3 t0^4)
    Returned as an energy density in Pa.  t0 in seconds."""
    return 3.0 * HBAR / (32.0 * math.pi ** 2 * C_SI ** 3 * t0 ** 4)


def fewster_constant():
    """C = mu_1^4/(16 pi^2), mu_1 the first positive root of cos(mu)cosh(mu) = 1.

    The least eigenvalue of d^4/dt^4 on an interval under clamped boundary
    conditions, divided by 16 pi^2 -- Fewster arXiv:1208.5399 Eq. (4), where it
    is printed as "C ~ 3.17".  Computed here by bisection, stdlib only, so the
    constant is COMPUTED and never a coefficient."""
    f = lambda m: math.cos(m) * math.cosh(m) - 1.0
    lo, hi = 4.0, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0.0:
            hi = mid
        else:
            lo = mid
    mu = 0.5 * (lo + hi)
    return mu, mu ** 4 / (16.0 * math.pi ** 2)


FEWSTER_MU1, FEWSTER_C = fewster_constant()

#: Caveat (c), corrected DOCKET 62: C is already the Fewster-Teo family's
#: constant at the optimal compactly supported sampler, so the 9/64 of their
#: Lorentzian-sampler comparison is NOT applied to it.  fewsterteo.py owns the
#: derivation; this pin keeps the refusal visible where C lives.
NINE_64_APPLIES_TO_C = False


def duration_bound(T):
    """THE INSTRUMENT THAT ACTUALLY APPLIES.  If <T_00> stays below rho for a
    duration T at a point, then rho >= -C hbar/(c^3 T^4).  A statement at EACH
    SPATIAL POINT about a DURATION -- it never averages in space, so
    Ford-Helfer-Roman does not touch it, and under the corridor's own staticity
    it may be applied at every point of the core and summed.  Pa; T in seconds.

    SCOPE: massless minimally coupled scalar, Hadamard states, flat space.  The
    massless scalar nonminimally coupled with xi > 0, in Minkowski space,
    admits NO state-independent QEI (Fewster 1208.5399 Sec. 5.1, after
    Fewster-Osterbrink 0708.2450).  CORRECTED (DOCKET 67): this read "The
    nonminimally coupled scalar admits NO state-independent QEI (Fewster
    5.1)", with the sign, masslessness and Minkowski space dropped."""
    return FEWSTER_C * HBAR / (C_SI ** 3 * T ** 4)


def hold_time(b, hold=1.0):
    """How long the core must hold: `hold` light-crossings of the corridor.
    hold = 1 is the transit requirement -- below it the corridor transmits
    nothing -- and it is FORCED by the geometry, not chosen."""
    return hold * b / C_SI


def persistence_allow(b, hold=1.0):
    return duration_bound(hold_time(b, hold))


def persistence_shortfall(b, hold=1.0):
    """required / allowed on the DURATION axis.  This is the corrected ground."""
    return required_density(b) / persistence_allow(b, hold)


def persistence_crossing(hold=1.0, m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    """Where the duration bound stops refusing.  Same dimensional identity as
    crossing_radius -- l_P times an O(1) number by construction, NOT evidence."""
    k = m_over_b / ((4.0 / 3.0) * math.pi * a_over_b ** 3)
    return math.sqrt(FEWSTER_C * HBAR * G_SI / (hold ** 4 * k * C_SI ** 3))


def casimir_b_needed(gap):
    """The apparatus row done with the ideal-plate Casimir density rather than
    the bound.  CORRECTED (DOCKET 67): this read "with the MEASURED effect";
    the force is what is measured, and casimir_density is the ideal form."""
    return b_needed_for(casimir_density(gap))


def available_density(b, a_over_b=A_OVER_B):
    return quantum_bound(a_over_b * b)


def ratio(b):
    return available_density(b) / required_density(b)


def crossing_radius(m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    """Where available meets required.  required ~ 1/b^2, available ~ 1/b^4."""
    k = m_over_b / ((4.0 / 3.0) * math.pi * a_over_b ** 3)
    return math.sqrt(HBAR_C / a_over_b ** 4 / (k * C_SI ** 4 / G_SI))


def casimir_density(gap):
    """The IDEAL perfect-conductor Casimir energy density at plate separation
    `gap`, valid for gap >> the plasma wavelength (gold 137.8 nm); at 10 nm
    real gold gives 0.1099 of it.  CORRECTED (DOCKET 67): this read "The
    measured effect" -- Casimir experiments measure the force, never this
    density, and the ideal-plate qualifier was dropped."""
    return (math.pi ** 2) * HBAR_C / (720.0 * gap ** 4)


def b_needed_for(rho_available, m_over_b=M_OVER_B, a_over_b=A_OVER_B):
    k = m_over_b / ((4.0 / 3.0) * math.pi * a_over_b ** 3)
    return math.sqrt(k * C_SI ** 4 / G_SI / rho_available)


# DOCKET 55.  The verdict's KIND, pinned so it cannot quietly drift back.
# NO-BY-THEOREM would need a theorem of the right shape; Ford-Helfer-Roman prove
# no spatial one can exist, and the duration theorem that does bite holds for one
# field in flat space, not for matter in general.
VERDICT_IS_A_THEOREM = False
VERDICT_KIND = "SURVEY"

# Things that look like exceptions and are not.
NOT_EXCEPTIONS = {
    "dark energy": "negative PRESSURE, positive energy density, for w >= -1 "
                   "(Lambda); a phantom w < -1 is negative only for a boosted "
                   "observer, never comoving in any fit read. Wrong sign of "
                   "the wrong quantity.",
    "effective negative mass (BEC, metamaterial)":
        "a curvature of a DISPERSION RELATION, not T_00. m* does not "
        "gravitate; the quasiparticle's energy does, as E/c^2.",
    "negative-index metamaterial":
        "the refractive index, not the energy density (under the dispersive, "
        "Brillouin, energy density in a low-loss band).",
}


def gap_widens_with_size(b1=1.0, b2=1.0e6):
    """required ~ 1/b^2 and available ~ 1/b^4, so bigger is worse."""
    return ratio(b2) < ratio(b1)


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

    print("THE PRICE")
    print("     %14s %18s %18s %14s" % ("b", "required (Pa)", "available (Pa)", "avail/req"))
    for b, tag in ((1.0, "1 m"), (1.0e5, "100 km"), (1.0e12, "solar system"),
                   (1.0e16, "1 light-year")):
        print("     %14s %18.4e %18.4e %14.3e"
              % (tag, required_density(b), available_density(b), ratio(b)))
    # RE-PINNED, DOCKET 55.  The number is unchanged and other files pin it, but
    # the CLAIM it pinned is withdrawn: this is a ratio of two densities, not a
    # shortfall against a bound, because no theorem asserts the denominator.
    near("ratio of the two curves at metre scale (NOT a shortfall)",
         ratio(1.0), 1.094e-65, 1e-3)
    chk("nowhere close at any scale tried",
        all(ratio(b) < 1e-60 for b in (1.0, 1e5, 1e12, 1e16)), True)
    # and what the fixture above was mistaken for: 65 orders is not the banked
    # figure.  candidates.py gets 70.606 at the same metre from the same
    # inequality; the difference is an unargued sampling choice.
    near("the coefficient-free form is this much more generous than Ford-Roman",
         quantum_bound(1.0) / ford_roman_allow(1.0 / C_SI), 105.276, 1e-4)

    print("\nTHE CORRECTED GROUND -- A DURATION, NOT A MAGNITUDE")
    near("Fewster's clamped-beam root mu_1", FEWSTER_MU1, 4.730040744862704, 1e-12)
    near("and his constant C = mu_1^4/(16 pi^2), printed as ~3.17",
         FEWSTER_C, 3.169857938310467, 1e-12)
    chk("caveat (c): no 64/9 adjustment is applied to C (DOCKET 62)",
        NINE_64_APPLIES_TO_C, False)
    print("     %14s %18s %18s %10s" % ("b", "required (Pa)", "allowed (Pa)", "orders"))
    for b, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e16, "1 light-year")):
        print("     %14s %18.4e %18.4e %10.3f"
              % (tag, required_density(b), persistence_allow(b),
                 math.log10(persistence_shortfall(b))))
    near("persistence shortfall at metre scale, in orders",
         math.log10(persistence_shortfall(1.0)), 71.256, 1e-4)
    near("and it goes exactly as b^2 -- the sampling time is FORCED, not chosen",
         math.log10(persistence_shortfall(10.0) / persistence_shortfall(1.0)),
         2.0, 1e-9)
    chk("the duration bound still refuses the core at every scale tried",
        all(persistence_shortfall(b) > 1e30 for b in (1.0, 1e5, 1e12, 1e16)), True)
    chk("and it is NOT an independent confirmation of candidates.py's 70.606",
        abs(math.log10(persistence_shortfall(1.0)) - 70.606) < 1.0, True)

    print("\nAND THE GAP WIDENS WITH SIZE -- the 'go bigger' escape is closed")
    chk("bigger is worse", gap_widens_with_size(), True)
    near("required falls as 1/b^2", required_density(1.0) / required_density(10.0),
         100.0, 1e-9)
    near("available falls as 1/b^4", available_density(1.0) / available_density(10.0),
         1.0e4, 1e-9)
    print("       seatindex.py's 1/l saving and concentric.py's far shell were")
    print("       both 'go bigger'.  Here two powers run the other way.")

    # RE-PINNED, DOCKET 55.  The numbers are unchanged -- gjw.py pins them --
    # but "a third independent route to the Planck scale" is WITHDRAWN.  Every
    # crossover of the form hbar c/L^4 = K c^4/(G L^2) sits at l_P/sqrt(K) for
    # ANY dimensionless K, so landing near l_P is forced by construction.
    print("\nTHE CROSSING IS A DIMENSIONAL IDENTITY, NOT A ROUTE TO THE PLANCK SCALE")
    bc = crossing_radius()
    near("crossing corridor radius (m)", bc, 3.3079e-33, 1e-3)
    near("core size there, in Planck lengths", bc * A_OVER_B / L_PLANCK, 4.09, 1e-2)
    _k = M_OVER_B / ((4.0 / 3.0) * math.pi * A_OVER_B ** 3)
    near("which is exactly l_P/(alpha sqrt k), alpha sqrt k = 0.244301",
         A_OVER_B * math.sqrt(_k), 0.244301, 1e-5)
    near("so the crossing core is l_P/0.244301, derived not measured",
         (L_PLANCK / (A_OVER_B * math.sqrt(_k))) / L_PLANCK, 4.0933, 1e-4)
    chk("AND THE PLACEMENT IS FRAGILE: the duration route's crossing is elsewhere",
        abs(persistence_crossing() * A_OVER_B / L_PLANCK - 4.09) > 1.0, True)
    print("       corridor.py's two earlier crossings are the same identity with")
    print("       different O(1) coefficients.  Not three routes -- one route.")

    print("\nTAKING THE APPARATUS AS AN APPARATUS -- corrected, DOCKETS 55 and 67")
    for gap, tag in ((1.0e-8, "10 nm, unsourced"),
                     (1.0e-10, "0.1 nm, below contact")):
        print("     %24s  IDEAL-PLATE |rho| = %.3e Pa  ->  b = %.3e m = %.2e ly"
              % (tag, casimir_density(gap), casimir_b_needed(gap),
                 casimir_b_needed(gap) / 9.461e15))
    # the original rows used quantum_bound, not casimir_density.  Correcting it
    # STRENGTHENS the row, so the withdrawal costs this argument nothing.
    near("the bound is this much larger than the ideal-plate Casimir density",
         quantum_bound(1.0e-10) / casimir_density(1.0e-10), 72.951, 1e-4)
    near("so the honest corridor is sqrt of that times larger",
         casimir_b_needed(1.0e-10) / b_needed_for(quantum_bound(1.0e-10)),
         8.541, 1e-3)
    chk("the 0.1 nm row needs a corridor of several light-years",
        casimir_b_needed(1.0e-10) > 6.0e16, True)
    print("       This is a CENSUS claim about apparatus, not a theorem, on")
    print("       ideal plates: real gold at 10 nm gives 0.1099 of the ideal density.")

    print("\nTHREE THINGS THAT LOOK LIKE EXCEPTIONS AND ARE NOT")
    for k, v in NOT_EXCEPTIONS.items():
        print("     %-42s %s" % (k, v))
    chk("three of them, named so they are not reached for later",
        len(NOT_EXCEPTIONS), 3)

    print("\nWHAT IS NOT RETRACTED")
    import concentric, stability, core
    chk("the device still seats and leads", concentric.works(5.0e-3), True)
    chk("with M_ADM = 0", abs(concentric.adm_residual(5.0e-3)) < 1e-10, True)
    chk("a shell of ordinary matter",
        stability.dec_holds(*stability.device(0.1)), True)
    chk("radially stable for free",
        stability.V_second(*stability.device(0.1), beta2=0.0) > 0, True)
    chk("and a Type I core", core.classify_core(2.0e-2, 0.02, 0.02)[0], core.TYPE_I)
    print("       Every one of those stands.  What is settled is that the CORE")
    print("       is not buildable with known physics.")
    # WITHDRAWN, DOCKET 55: "and the shortfall is a THEOREM rather than a budget".
    # No theorem of the right shape caps the ball integral, and Ford-Helfer-Roman
    # prove none can exist over a bounded region in four-dimensional Minkowski
    # spacetime (counterexample: the massless minimally coupled free scalar).
    chk("'the shortfall is a THEOREM rather than a budget' is WITHDRAWN",
        VERDICT_IS_A_THEOREM, False)
    chk("the verdict rests on a convergence of proven limits -- a SURVEY",
        VERDICT_KIND, "SURVEY")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE PRICE")
    print("  %16s %18s %18s %14s" % ("b", "required (Pa)", "available (Pa)", "avail/req"))
    for b, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e5, "100 km"),
                   (1.0e12, "solar system"), (1.0e16, "1 light-year"),
                   (1.0e20, "10 kly")):
        print("  %16s %18.4e %18.4e %14.3e"
              % (tag, required_density(b), available_density(b), ratio(b)))
    print("\n  crossing at b = %.4e m, core size %.2f Planck lengths"
          % (crossing_radius(), crossing_radius() * A_OVER_B / L_PLANCK))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  THERE IS NO ACHIEVABLE CORE, AND THE REASON IS A DURATION.")
    print("  A corridor must hold its contraction for at least one light-crossing")
    print("  or it transmits nothing, and the worldline QEI's duration bound")
    print("  rho >= -C hbar/(c^3 T^4), C = %.6f computed here, refuses that by"
          % FEWSTER_C)
    print("  %.3f orders at b = 1 m, widening exactly as b^2 because the"
          % math.log10(persistence_shortfall(1.0)))
    print("  sampling time is FORCED by the transit rather than chosen.")
    print("\n  WITHDRAWN, DOCKET 55: that every known source 'obeys |rho| <~ hbar c")
    print("  / L^4', that the shortfall is 65 orders, that it is a THEOREM rather")
    print("  than a budget, and that the Planck-scale crossing is a third")
    print("  independent route.  Ford-Roman bounds a TIME average at one point;")
    print("  Ford-Helfer-Roman prove no spatial bound exists at all; the crossing")
    print("  is the identity L = l_P/sqrt(K).  See the DOCKET 55 section.")
    print("\n  THE DEVICE IS NOT RETRACTED: it seats and leads, M_ADM = 0, the")
    print("  shell is ordinary matter and stable, the core is Type I with a")
    print("  one-sign exoticism.  What is settled is that the core is not")
    print("  buildable with known physics.  THE VERDICT IS NO-IN-PRACTICE AND NOT")
    print("  NO-BY-THEOREM: its limbs are each proven, their hypotheses do not")
    print("  jointly cover all matter, and their conjunction is a SURVEY.")
    print("  Whether physics beyond the standard framework supplies it is a")
    print("  question this project cannot ask.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
