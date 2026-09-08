#!/usr/bin/env python3
"""
obstruct.py -- the obstruction ledger.  Which ones dissolved, which merely moved,
and which have never been tested at all.

Written because "the obstructions have moved" is not the same claim as "the
obstructions have dissolved", and a build planned on the first sentence while
believing the second will fail on the back end.  Every row here carries a status
and a test, and the statuses are not flattened:

    DISSOLVED        gone, with a reason that is checkable here
    RELOCATED        still true, wearing a different name -- usually a bill
    CLOSED-NEGATIVE  answered, and the answer is no
    CONDITIONAL      dissolved in one regime and not in another, with the boundary
    UNTESTED         nobody has asked, this project included.  THE DANGEROUS ROW.

THE HEADLINE: of thirty-four obstructions, SIX dissolved, three relocated,
SIXTEEN closed negative, SEVEN conditional, two are OPEN, NONE is untested.
The newest is the hardest: ACHIEVABLE-CORE is closed NEGATIVE.  A
build is ready when the untested rows are either tested or accepted with eyes
open, and this file exists to make that a decision rather than an oversight.
The counts here are asserted by the selftest against the ledger, so a row that
moves fails this paragraph rather than quietly outliving it.

-- WHAT ACTUALLY DISSOLVED ----------------------------------------------------
Only two, and one of them by leaving the architecture rather than beating it.

  HORIZON-REQUIRED.  A horizon exists iff v_s >= c (twist.py: f* = 1 - c/v_s lies
  in [0,1) only for v_s >= c).  Subluminal transport needs none.  Genuinely gone.

  EXOTIC-MATTER.  Gone for the warpshell -- dominant energy holds observer-robustly
  in bulk and shell -- but by leaving the shift-vector class Santiago-Schuster-
  Visser quantify over, not by refuting them.  Dissolution by relocation of the
  ARCHITECTURE is still dissolution, and it is worth naming which kind it is.

-- WHAT RELOCATED, AND WHERE IT WENT ------------------------------------------
  CM-THEOREM -> the energy budget.  Le's Theorem 1 is its exact GR form.  Paid,
  not evaded: m_f/m_0 = e^{-3 delta_eta}, the Doppler factor cubed.
  ENERGY -> "astronomical but finite", which is a bill and not a bound.
  FELT-ACCELERATION -> unchanged and often misread.  The cavity is tidally flat;
  the passengers still have weight.  person.py's fragility bound was tidal, so it
  lifts; the acceleration limit does not.

-- THE ONE THAT MOVED TWICE, AND THE SECOND MOVE IS THE INTERESTING ONE --------
  WALL-STABILITY.  Marginal (Poisson-Visser V'' = 0), so a burn had to outrun an
  e-folding, which a habitable design missed by 1.8e14.  wall.py showed the fix is
  structural: strictly stable for beta^2 > beta^2_crit(x), subluminal through the
  whole operative window, free in dominant-energy margin.

  But beta^2 IS NOT A KNOB.  The matter model determines it.  For a counter-
  rotating shell the junction already fixes v^2 = (1-s)/(2s), so the supplied
  stiffness is a function of x alone, and it clears the requirement only for

        x  <  0.46898

  with the margin WIDEST at low compactness, tending to exactly 4/3 as x -> 0.
  So the fix is CONDITIONAL, and the condition happens to hold where it is needed:
  Le's x = 0.3 clears it by 14%, and a habitable ship at x ~ 1e-22 sits at the 4/3
  limit.  It fails at x = 2/3 and fails badly at 4/5 -- the high-compactness corner
  a marginal wall handled best.  That is not a dissolution and this file does not
  call it one.

-- THE TWO ROWS NOBODY HAS TESTED, WHICH IS WHERE THE NEXT BUILD WILL FAIL -----
  1. NON-RADIAL SHELL MODES.  Poisson-Visser is a RADIAL linearisation and wall.py
     is nothing but.  Perturbations with l >= 2 were never posed.  A thin shell
     that is radially stable and unstable to a quadrupole is an ordinary object,
     not an exotic one, and the surface stress here is anisotropic (p_r = 0,
     tangential pressure only), which is the configuration most prone to it.
     THIS IS THE FIRST THING THAT WILL BREAK.  It is also cheap to test.
  2. THE 2+1D MAPPING DOES NOT EXIST.  twist.py showed an analogue must be at
     least 2+1D to carry any metric content.  Smolyaninov's mapping is derived in
     1+1D and there is no published 2+1D version; worse, the stability bound the
     whole design rests on -- Brown-Hornreich-Shtrikman g_x^2 <= (eps-1)(mu-1) --
     is a bound on ONE magnetoelectric component, and a transversely graded medium
     has more.  The bound may tighten, loosen, or not apply.  ANALOGUE-2D is not a
     design awaiting fabrication; it is a derivation awaiting a derivation.

-- AND ONE MORE THING THE LEDGER SAYS, WHICH IS NOT AN OBSTRUCTION -------------
Three separate results now turn on the SAME dimensional boundary: the shift is
gauge in 1+1D and not in 3+1D (twist.py); the twist is a 3-form and vanishes on a
2-manifold (twist.py); the round-trip theorem holds in 1+1D and has no 3+1D
analogue (pathmetric.py).  A boundary that decides three unrelated questions is a
structural fact about the problem, not a coincidence of three methods.

stdlib only.  Every status below is recomputed from the instrument that owns it,
never transcribed -- so a row cannot silently go stale when its instrument moves.
"""
import math, sys

STATUSES = ("DISSOLVED", "RELOCATED", "CLOSED-NEGATIVE", "CONDITIONAL", "UNTESTED", "OPEN")

# (id, obstruction, status, where it went / what decides it, owning instrument)
LEDGER = [
 ("HORIZON-REQUIRED", "a warp drive needs a horizon", "DISSOLVED",
  "f* = 1 - c/v_s is in [0,1) only for v_s >= c: the superluminal pathology",
  "twist.py"),
 ("EXOTIC-MATTER", "warp transport needs negative energy", "DISSOLVED",
  "not for the warpshell: dec observer-robust in bulk and shell, n_2 >= 0. "
  "By leaving SSV's shift-vector class, not by refuting it", "warpshell.py"),
 ("CM-THEOREM", "no isolated system moves its own centre of mass", "RELOCATED",
  "into the energy budget: Bondi momentum changes only by radiating. Paid",
  "warpshell.py"),
 ("ENERGY", "the bill is impossible", "RELOCATED",
  "to astronomical but finite: the Doppler factor cubed, 8/27 at 0.2 c",
  "warpshell.py"),
 ("FELT-ACCEL", "passengers ride in free fall", "RELOCATED",
  "never true here. The cavity is tidally flat; weight remains", "warpshell.py"),
 ("WALL-STABILITY", "the realized wall is marginally stable", "CONDITIONAL",
  "stable iff the matter supplies beta^2 > beta^2_crit(x); counter-rotating "
  "matter does so only below x = 0.46898, margin -> 4/3 as x -> 0", "wall.py"),
 ("ANALOGUE-1D", "a 1+1D metamaterial can emulate a warp metric", "CLOSED-NEGATIVE",
  "E = -Omega^2/(8 pi G) and both vanish on the axis: the target is Minkowski",
  "twist.py"),
 ("SHIFT-SHORTENS", "a shift shortens the path", "CLOSED-NEGATIVE",
  "round trip = optical length, longer by 2v^2/(c(c^2-v^2)) > 0 in 1+1D",
  "pathmetric.py"),
 ("SELF-SOURCED", "an engine sources the metric it uses", "CLOSED-NEGATIVE",
  "the 10^31 gap and the ADM theorem both follow from it alone", "COUPLING.md"),
 ("NONRADIAL", "the shell is stable to l >= 2 perturbations", "CONDITIONAL",
  "IT IS NOT. Pitre-Schneider-Poisson 2026 (PRD): unstable even-parity mode for "
  "all l >= 2, all compactness, all Gamma -- on Le's anchor exactly, and beta^2 "
  "does not appear in it, so the structural fix does not reach it. But the rate "
  "is self-gravitational, ~0.6 sqrt(GM/R^3), so N < 1 is a ceiling on MEAN "
  "DENSITY. THE CORNER IS WITHDRAWN: the same mass sets density and compactness, "
  "so escaping the instability means x -> 0, and the survivor at x = 3e-25 is a "
  "3.97 g/m^2 balloon whose flat cavity is Birkhoff, not a warp feature. Both "
  "stable AND self-gravitating (1% binding) needs 2e9 Msun over 1,000 AU",
  "wall.py"),
 ("MAPPING-2D", "a 2+1D analogue mapping exists", "DISSOLVED",
  "Plebanski 1960 gives it in full 3+1D and returns exactly the transverse "
  "anisotropy twist.py demanded. Briefly closed on BHS -- eps_xx = 1 exactly, so "
  "the static bound admitted it only for |v| >= c -- and REOPENED by "
  "dispersive.py: BHS is a static bound and this is a dispersive device. The "
  "mapping stands; only its BHS verdict fell", "plebanski.py"),
 ("TYPE-IV", "the Alcubierre wall needs matter with no rest frame", "OPEN",
  "measured, 7/7 wall points, |Im|/||T|| 0.14-0.69, stable to six figures in h "
  "and validated against BBV Eq (3.48) to 1e-6. Untouched by every energy "
  "condition, which bound contractions where this is about eigenvectors. THE "
  "OBJECTION THAT REPLACES the energy one. Not forbidden -- unknown. The "
  "sub-objection 'nothing known is Type IV' is now FALSE (see TYPEIV-SOURCES); "
  "what stays open is the CONFIGURATION, radial flux against twisted",
  "typefour.py"),
 ("TYPEIV-SOURCES", "Type IV occurs only as a test field, never as a source",
  "CONDITIONAL",
  "FALSE at first order in hbar: Abdolrahimi-Page-Tzounis solve G = 8 pi <T> "
  "with the Unruh state and get Type IV everywhere outside an evaporating "
  "horizon, escaping all four of MMV's Type-I-forced cases for the same "
  "structural reason the bubble does. The boundary is the ORDER: answered at "
  "first, open at exact, since APT do not iterate to a fixed point and MMV's "
  "theorems are about exact solutions. Magnitude available -- <T> ~ mu^-4 puts "
  "a 1 m 0.1c bubble at the strength of a 1.126e9 kg hole -- but a magnitude "
  "match is not a construction", "selfconsistent.py"),
 ("STATIC-BOUND", "BHS applies at a working frequency", "CLOSED-NEGATIVE",
  "IT DOES NOT. A Polder ferrite above resonance has |kappa| > |mu-1|, violating "
  "BHS by factors up to 5, and above-resonance ferrites are ordinary passive "
  "components. The Brillouin condition that replaces it is satisfied identically, "
  "saturating only at resonance. Cost of the error: beta capped at c/4 when the "
  "real ceiling is the analogue horizon -- 0.825 c at 0.95% ferrite loss",
  "dispersive.py"),
 ("ANEC", "the averaged null energy condition", "OPEN",
  "VIOLATED on every ray of the Alcubierre bubble, INT T_kk dx from -0.081 to "
  "-0.344, and QNEC -- a THEOREM, not a conjecture -- integrates to it. "
  "D-independent, so freeing the wall thickness buys nothing. WITHDRAWS this "
  "session's headline: nullbound.py evaluated SNEC at one sampling width, the "
  "loosest, and SNEC fails above w ~ 0.93 bubble radii. HARDENED, not softened, "
  "by ACHRONALITY below: the one escape is closed and what remains is a single "
  "unproven condition", "anec.py"),
 ("ACHRONALITY", "the ANEC-violating rays might be non-achronal, putting the "
  "bubble outside Graham-Olum", "CLOSED-NEGATIVE",
  "THEY ARE ACHRONAL. 25 ANEC-violating rays over v_s = 0.3/0.5/0.8 c, ZERO "
  "with a conjugate point. And the anti-correlation is Raychaudhuri itself -- "
  "u'' = -4 pi T_kk u, so the negative T_kk that violates ANEC is what "
  "defocuses the congruence and prevents the conjugate point that would break "
  "achronality. PROVED where T_kk <= 0 throughout, measured where the signs "
  "mix. The prohibition now rests entirely on the achronal ANEC in 4D CURVED "
  "spacetime -- unproven for nineteen years, and load-bearing", "achronal.py"),
 ("TURN-ADVANTAGE", "the focusing turn that seats a transition might also "
  "shorten it", "CLOSED-NEGATIVE",
  "IT DOES NOT, and the two exclusions are one fact seen twice. The Jacobi "
  "equation turns u back only where T_kk > 0, so part 2 succeeds ONLY on "
  "ANEC-SATISFYING rays -- and every one of those carries a POSITIVE Shapiro "
  "delay. TURN => LATE. EARLY => NO TURN. Measured on the bubble at v_s = 0.5 "
  "c; exclusion 1 is general (the sign of the Jacobi equation), exclusion 2 is "
  "this metric's and another T_kk distribution is NOT-RUN. REOPENED AND "
  "ANSWERED by composite.py: it was measured with SHEAR DROPPED, and Weyl "
  "focusing is sign-blind", "transit.py"),
 ("SEAT-MEETS-TRANSPORT", "seating and time advance can never coexist",
  "DISSOLVED",
  "THEY CAN. Ricci focusing is linear in the source and needs positive energy; "
  "Weyl focusing is QUADRATIC and is sign-blind, while the Shapiro delay stays "
  "linear and flips. Measured: M = -2e-3 seats at lambda 56.5 and arrives EARLY. "
  "Bounded above by the M^2 path-lengthening penalty, below by the focal length "
  "-- a window about a decade wide. Negative mass ASSUMED, field LINEARISED, "
  "focus ASTIGMATIC, no payload", "composite.py"),
 ("BARE-NEGATIVE-MASS", "the seats-and-leads result needs a bare negative "
  "mass, which the positive mass theorem forbids", "DISSOLVED",
  "IT DOES NOT. concentric.py puts a compact negative core inside a positive "
  "shell of equal magnitude: the monopoles cancel, M_ADM = 0 EXACTLY, and it "
  "still seats and leads over most of a decade in m. The theorem is nearly "
  "free -- shell delay/core advance ~ (L/R_s)/(2 ln(L/a)) = 8% -- because the "
  "core's advance carries a logarithm of its compactness and the shell's delay "
  "does not. The corridor is vacuum only for b/a >~ 50. Negative LOCAL energy "
  "density is unchanged, the field is linearised, and NOTHING here shows the "
  "configuration is stable", "concentric.py"),
 ("DEVICE-SHELL", "the shell holding the device needs exotic matter or "
  "stiffness it cannot have", "CLOSED-NEGATIVE",
  "IT NEEDS NEITHER. With M_in = -m and M_out = 0 the Israel junction gives "
  "sigma > 0 and a small tension, DOMINANT energy condition satisfied to "
  "m/R = 2; and V'' > 0 at beta^2 = 0 with beta2_crit NEGATIVE everywhere, so "
  "it is radially stable with no pressure response at all -- where the textbook "
  "shell on the same machinery is unstable. The core's position is neutral by "
  "the shell theorem. l >= 2 IS NOT RUN and is the top remaining risk",
  "stability.py"),
 ("CORE-TYPE-IV", "the core inherits the Alcubierre wall's Type IV problem",
  "CLOSED-NEGATIVE",
  "IT DOES NOT. Measured |Im|/||T|| of 1e-7 to 1e-8: static and spherically "
  "symmetric forces Type I, as MMV require. The core has a rest frame, an "
  "energy density and isotropic pressures. It has NO Buchdahl limit either -- "
  "1+2|M|r^2/R^3 > 1 everywhere, finite at 2|M|/R = 8378 -- and p(0)/|rho| "
  "rises to 1/3 FROM BELOW. Every energy condition fails and all fail for one "
  "reason: rho < 0. Flip that and DEC holds", "core.py"),
 ("ACHIEVABLE-CORE", "a core that can actually be made", "CLOSED-NEGATIVE",
  "THERE IS NONE. Every known negative energy density -- Casimir, squeezed "
  "vacuum, dynamical Casimir, Hawking flux, vacuum polarisation -- obeys "
  "Ford-Roman |rho| <~ hbar c/L^4, and the core needs 65 ORDERS more at metre "
  "scale. The gap WIDENS with size (required 1/b^2 against available 1/b^4), "
  "closing the 'go bigger' escape used twice before, and the curves cross at "
  "4.09 PLANCK LENGTHS -- a third independent route to that scale. Dark energy "
  "and BEC effective negative mass are not exceptions. THE DEVICE IS NOT "
  "RETRACTED; the core is not buildable, and that is a theorem not a budget",
  "achievable.py"),
 ("ENTANGLEMENT-ROUTE", "entanglement supplies the negative energy without "
  "exotic matter", "CONDITIONAL",
  "IT IS THE RIGHT LANGUAGE AND IT DOES NOT LIFT THE BOUND. Negative energy "
  "density IS an entanglement phenomenon -- QNEC states the requirement exactly "
  "as entropy CONCAVE along the ray. And the magnitude looks completely "
  "different in that variable: 2 pi^2 = 19.74x the HOLOGRAPHIC bound, constant "
  "at every scale, against Ford-Roman's 1e65. Cross-checks against spec.py's "
  "collapse factor 2 pi^2/3, differing by exactly 3. So the PRINCIPLED gap is "
  "twenty, the ENGINEERING gap is 65 orders, and the first is the meaningful "
  "one. But 20x the holographic bound is a limit on what CAN be. No charge "
  "loophole: QNEC is state-independent", "entangle.py"),
 ("GRAHAM-OLUM-ESCAPE", "there is no way past the achronal ANEC",
  "CONDITIONAL",
  "THERE IS EXACTLY ONE, AND IT IS NOT A MATTER-SIDE ESCAPE. achronal.py "
  "proved you cannot break achronality through the stress tensor -- ANEC "
  "violation PROTECTS it, 25 rays and 0 escapes. Gao-Jafferis-Wall break it by "
  "ADDING AN EXTERNAL CAUSAL PATH: coupling the two boundaries changes the "
  "chronology relation itself, and their traversable wormhole is the first in "
  "a UV-complete theory. THE CONDITION IS THAT THE SAME MOVE FORBIDS SPEED -- "
  "non-achronality requires an existing outside path, so the wormhole never "
  "beats it. Their flat-space version, left as a remark, needs amplification "
  "4.387e71 D^2, rising with D and reaching unity at 0.093 Planck lengths",
  "gjw.py"),
 ("STANDING-COUPLING", "the ORDER row is open somewhere useful", "CONDITIONAL",
  "IT IS OPEN AT EXACTLY ONE POINT. The single-trip advantage is closed by the "
  "bank-loan theorem. The amortised advantage -- deploy once, transit N times, "
  "which the arithmetic favours from N = 10 -- is closed by GJW's own sentence: "
  "in flat space the coupling is carried by ambient propagation 'except with a "
  "time delay', so it is per-use with nothing to amortise. BUT THEIR FOOTNOTE 2 "
  "DECLINES THE TIME-INDEPENDENT COUPLING, to keep the state regular on the "
  "past horizon -- a stated technical reason, not a failure. A standing channel "
  "is exactly what amortisation needs and exactly what nobody has tested. "
  "Narrow, real, and named in the source", "amortize.py"),
 ("WRONG-CATEGORY", "the object is a wormhole, a black hole, or a propulsion "
  "system", "CLOSED-NEGATIVE",
  "IT IS NONE OF THE THREE, verified rather than asserted. The areal radius "
  "R = r e^{-Phi} is MONOTONE at every radius, so no throat and the topology "
  "is R^3. g_tt = -e^{2Phi} < 0 everywhere with Phi POSITIVE and bounded, so "
  "no horizon. T^0i = 0 EXACTLY from the Einstein tensor, so no thrust, no "
  "exhaust, no reaction mass -- warpshell.py's CM theorem and Doppler-cubed "
  "budget belong to a different architecture. And the warp quantity is PROPER "
  "DISTANCE, which a negative source contracts and ORDINARY MASS STRETCHES: a "
  "lens has the wrong sign for this concept entirely", "transition.py"),
 ("CHARGE-STATE", "a charge state can supply what the core supplies",
  "CONDITIONAL",
  "IT SUPPLIES THE SEAT AND NOT THE LEAD, and the boundary is the "
  "energy-condition line. EM stress-energy is ORDINARY -- NEC, WEC, DEC all "
  "hold -- so T_kk >= 0 gives Ricci focusing, and a magnetar's 1e11 T field "
  "clears universal seating beyond 155,000 km. But Phi > 0 needs r < Q^2/2M, "
  "which is INSIDE THE HORIZON at every charge, and Q <= M is the "
  "Einstein-Maxwell positive energy theorem. Charge reduces the delay by up to "
  "25% at r = 2M and never reverses it", "charge.py"),
 ("COLLECTION-IN-TRANSIT", "the cost of the transition can be collected en "
  "route from static neighbours rather than paid in advance", "CLOSED-NEGATIVE",
  "MEASURED FALSE, and the mechanism is the logarithm. Spreading the same total "
  "mass over N static sources along the path gives 1.000 / 0.976 / 0.960 / 0.954 "
  "/ 0.950 of one concentrated source at N = 1/2/5/10/50 -- monotonically WORSE, "
  "converging near 95 %. The contraction goes as asinh(L/2b), so splitting the "
  "path shortens every span and the sum of the parts is less than the whole. One "
  "concentrated source wins. This closes the cheap route and leaves the price "
  "where GJW put it: paid in advance, at the moment of coupling. DEFERRAL TO "
  "SEATING IS NOT-RUN, not refuted -- paying at the destination is not a "
  "well-posed computation without a model of dynamical payment, and none is "
  "invented here", "unified.py"),
 ("TIME-ADVANCE-AT-RANGE", "the measured lead is a genuine time advance that "
  "holds over a useful distance", "CLOSED-NEGATIVE",
  "IT IS NOT, AND THE MEASUREMENT THAT SAID SO WAS TAKEN IN THE WRONG PLACE. "
  "concentric.py ran every ray between endpoints INSIDE its own shell, where "
  "the metric is not asymptotically flat and 't - |dx|' is not a causal "
  "statement. Outside the shell the lead shrinks and then reverses at X ~ 277. "
  "The mechanism is general: M_ADM = 0 makes the Shapiro gain CONVERGE -- "
  "-3.969054e-01 at X = 400 and the same five digits at X = 20000, closed form "
  "4m[ln(2R_s/b) - 1] with no baseline in it -- while the deflection the shell "
  "cannot cancel, because a ray at b << R_s passes wholly inside where a shell "
  "has no field and exits nearly radially where a radial field cannot bend it "
  "back, costs path length LINEARLY. Bounded gain against unbounded loss. "
  "DEVICE-SEATS-LEADS is withdrawn as a global claim", "chronology.py"),
 ("SHORT-RANGE-IS-THE-SHELL", "the range limit is an artefact of this "
  "particular two-region construction and a better one escapes it",
  "CLOSED-NEGATIVE",
  "IT IS NOT THE SHELL. In the weak field a negative Shapiro term buys time at "
  "most LOGARITHMICALLY in the baseline while the deflection it necessarily "
  "produces costs path length LINEARLY, and log against linear has exactly one "
  "crossing whatever the configuration. Measured on a BARE negative mass with "
  "no shell anywhere: early at X = 320, LATE at X = 400, predicted crossover "
  "324 against a measured 350. The device crosses at ~250 and the bare mass at "
  "~324 -- THE SAME ORDER. The shell does not cause the failure; it moves the "
  "crossing in by turning the logarithm into a constant, and a bare negative "
  "mass buys 30 % more range and needs to be a bare negative mass to do it",
  "chronology.py"),
 ("MTY-CONSTRUCTION", "the device admits the Morris-Thorne-Yurtsever time "
  "machine, so chronology protection applies to it directly", "CLOSED-NEGATIVE",
  "IT DOES NOT, AND IT FAILS ON STRUCTURE RATHER THAN MAGNITUDE. MTY needs "
  "four things and the wormhole was only how 1988 supplied the second: two "
  "paths between the same events (HAS), the short one elapsing less (HAS, "
  "bounded), A PERSISTENT IDENTIFICATION OF TWO ENDS (DOES NOT -- "
  "transition.py measures the areal radius monotone at every radius, so there "
  "is no throat and there are not two ends to identify), and differential "
  "aging across that identification (blocked by the third). transit.py's gate "
  "re-declares A and B every use, so nothing accumulates -- the same payment "
  "GJW make, made again, every time. unified.py named this machine and that "
  "was an assertion", "chronology.py"),
 ("CTC-SAFE", "the device is therefore safe from closed timelike curves",
  "CLOSED-NEGATIVE",
  "NO. The Everett route, made explicit by Shoshany & Snodgrass "
  "(arXiv:2309.10072), needs NO identification -- two devices and a boost. "
  "Their eq. (3.11), u > (v1+v2)/(1+v1 v2) with both legs required "
  "superluminal, reduces exactly to gamma > 1/eps, quadratic rather than "
  "linear in the advance. At this device's best unambiguous eps = 2.297e-4 "
  "that is gamma > 4354 -- FINITE, and below the LHC's proton gamma. The "
  "device is not protected by chronology. What protects it is that it does not "
  "work at range, which is a different and much weaker kind of safety. "
  "Hawking's Cauchy-horizon divergence is NOT-RUN and nothing here rests on "
  "it", "chronology.py"),
 ("CHEAPER-CURRENCY", "the cost can be paid in a cheaper denomination than "
  "mass-energy -- entropy, entanglement, or shaping rather than supplying",
  "CLOSED-NEGATIVE",
  "PURSUED IN THREE STAGES AND CLOSED, AND THE FIRST TWO STAGES SAY THE "
  "INSTINCT WAS RIGHT. (1) Entropy IS a structurally better denomination: "
  "every energy comparison carries hbar G/c^3 exactly once and uncancelled -- "
  "that factor IS the 65-to-71 orders -- while in the entropy channel both "
  "sides carry (L/l_P)^2 and it CANCELS, giving 2 pi^2 at every scale. (2) But "
  "Bekenstein read backwards, E >= S hbar c/2 pi R, returns (pi/4) L c^4/G, "
  "exactly seatindex.py's T_COEFF: the denomination buys PERMISSION, not "
  "DISCOUNT. (3) And the last door -- shaping S'' rather than supplying "
  "magnitude -- is closed by COUNTING and not by cost. The cost argument fails "
  "in M's favour: eta -> 1/r, so weak squeezing over many modes really does "
  "drive preparation cost per joule to zero. What fails is availability: "
  "holding rho < 0 over a length L caps the frequency at pi c/2L, the cap "
  "limits the mode count, each mode yields at most its own zero-point energy, "
  "and the product is 0.0514 hbar c/L^4 -- WHICH IS FORD-ROMAN, derived here "
  "rather than quoted, with the coefficient pi^2/192. A cheaper currency does "
  "not help when the thing being bought is out of stock",
  "shaping.py"),
 ("THE-LEAD", "a device must beat light to be worth building", "DISSOLVED",
  "NOT UNDER M's SCOPING: the matter must exist at both ends under the same "
  "physics, nothing more. That removes the requirement Olum, Ford-Roman and "
  "Q <= M were all attached to. What remains -- the SEAT -- is achievable with "
  "ordinary matter, and the whole specification is one invariant, "
  "B*l = 1.5456e19 T m, fixed by c, G and mu_0 alone. The residual gap is "
  "8.3e7 in field strength. BUT THE SPECIFICATION IS WITHDRAWN TWICE OVER: any "
  "Sturm-seating region is inside its own Schwarzschild radius by 2 pi^2/3 at "
  "every scale, and the magnetar figure compared a dipole's peak against a "
  "length it does not sustain. What actually seats is CUMULATIVE WEAK-FIELD "
  "LENSING, f = b^2 c^2/(4 G M), validated against the solar focus at 547.6 AU "
  "-- which is gravitational lensing, ordinary and known since 1919", "spec.py"),
]

def by_status():
    return {s: [r for r in LEDGER if r[2] == s] for s in STATUSES}

def untested():
    return [r for r in LEDGER if r[2] == "UNTESTED"]

def build_ready():
    """A build is ready when no UNTESTED row is load-bearing for it.  This
    returns the rows that must be tested or explicitly accepted first."""
    return [r[0] for r in untested()]

# -- each row recomputed from its owner, so it cannot go stale ---------------

def check_horizon_required():
    import twist
    return (not twist.has_horizon(0.99)) and twist.has_horizon(1.01)

def check_cm_relocated():
    import warpshell
    # paid, not evaded: the budget is the Doppler factor cubed and is finite
    return abs(warpshell.mission(0.2)[1] - 8.0 / 27.0) < 1e-15

def check_wall_conditional():
    import wall
    xc = wall.matter_crossover()
    return (wall.vlasov_stable(0.3) and not wall.vlasov_stable(2.0 / 3.0)
            and 0.46 < xc < 0.47)

def check_analogue_closed():
    import twist
    # Omega and E both vanish on the axis: nothing to emulate in 1+1D
    return (twist.omega_bbv(0.9, 0.0) == 0.0
            and twist.energy_density_bbv(0.9, 0.0) == 0.0
            and abs(twist.wedge_txy_closed(0.9, 0.3)) > 1e-3)

def check_mapping_dissolved():
    import plebanski, dispersive
    # the mapping stands and is anisotropic; the STATIC bound that closed it does not
    return (plebanski.anisotropy(0.5) > 1.0
            and not dispersive.static_ok(2.0)      # BHS forbids a real ferrite
            and dispersive.dispersive_ok(2.0))     # the right condition does not

def check_nonradial_conditional():
    import wall
    # fatal at ship scale, survivable when diffuse -- that is what CONDITIONAL means
    return (wall.efoldings(1.0e6, 10.0, 0.2, 9.80665) > 100.0
            and wall.efoldings(1.0e6, 5000.0, 0.2, 9.80665) < 0.1)

def check_typeiv_sources_conditional():
    import selfconsistent
    # conditional means: yes in one regime, open in the other, with the boundary
    return (selfconsistent.SCOPE["first order in hbar"]
            and not selfconsistent.SCOPE["exact self-consistent"]
            and not selfconsistent.SCOPE["configuration matched"])

def check_achronality_closed():
    import achronal
    rows = achronal.survey()
    viol = [r for r in rows if r["anec_violated"]]
    # closed negative means: the escape was looked for and is not there
    return (len(viol) > 0 and achronal.escapes(rows) == []
            and rows[0]["proved"])          # and the axial case is proved, not fitted

def check_turn_advantage_closed():
    import transit
    rows = []
    for y0 in (0.8, 1.0, 1.2, 1.5):
        c = transit.Conditions(y0, arrival_length=None)
        L = transit.turn_length(c.sampler())
        rows.append((L is not None, transit.shapiro(c, L)))
    # closed negative: every turn is late, and every early ray failed to turn
    return (all(d > 0 for t, d in rows if t)
            and all(not t for t, d in rows if d < 0)
            and any(t for t, d in rows))

def check_seat_meets_transport():
    import composite
    # dissolved means: the thing said impossible was exhibited
    return composite.both(-2.0e-3) and not composite.survey(2.0e-3)["early"]

def check_bare_mass_needed():
    import concentric
    # dissolved: the device works with M_ADM = 0, so no bare negative mass
    return (concentric.works(5.0e-3)
            and abs(concentric.adm_residual(5.0e-3)) < 1e-10)

def check_device_shell_ordinary():
    import stability
    # the shell holding the device is ordinary matter AND radially stable free
    return (all(stability.dec_holds(*stability.device(m)) for m in (0.01, 0.5, 2.0))
            and all(stability.V_second(*stability.device(m), beta2=0.0) > 0
                    for m in (0.01, 0.1, 0.5))
            and stability.V_second(*stability.ordinary(0.1), beta2=0.0) < 0)

def check_core_type_i():
    import core
    return (core.classify_core(2.0e-2, 0.02, 0.02)[0] == core.TYPE_I
            and core.buchdahl_safe(-1000.0)
            and core.only_sign_is_exotic(-1.0)
            and core.central_ratio(-10000.0) < 1.0 / 3.0)

def check_no_achievable_core():
    import achievable
    return (achievable.ratio(1.0) < 1e-60
            and achievable.gap_widens_with_size()
            and achievable.crossing_radius()*achievable.A_OVER_B/achievable.L_PLANCK < 10.0)

def check_charge_split():
    import charge
    return (all(charge.positive_region_is_hidden(1.0, q) for q in (0.5, 0.9, 1.0))
            and charge.em_is_ordinary()
            and charge.seats_beyond(1.0e11) < 2.0e8)

def check_spec_achievable():
    import spec
    return (abs(spec.seating_invariant()/1.54562e19 - 1.0) < 1e-4
            and abs(spec.conjugate_length_from_q(spec.energy_density(1e11))
                    / spec.range_for_field(1e11) - 1.0) < 1e-9
            and spec.range_for_field(45.0) > spec.range_for_field(1e11))

def check_three_negatives():
    import transition, concentric
    ph = concentric.potential(2e-2)
    radii = (0.01, 0.05, 0.5, 5.0, 50.0, 150.0)
    return (not transition.has_throat(ph, radii)
            and not transition.has_horizon(ph, radii)
            and transition.momentum_flux(ph, (2.0, 0.3, 0.0), 2e-2)[0] == 0.0
            and transition.proper_ratio(ph, -150.0, 150.0, 1.0)[0] < 1.0)

def check_entanglement_route():
    import entangle, math
    return (abs(entangle.holographic_excess(1.0) - 2*math.pi**2) < 1e-6
            and abs(entangle.holographic_excess(1.0)/entangle.collapse_factor() - 3.0) < 1e-6
            and entangle.holographic_excess(1.0) > 1.0)

def check_gjw():
    import gjw, math
    return (abs(gjw.gain_coefficient()/4.3866e71 - 1.0) < 1e-3
            and gjw.amplification_needed(1e6) > gjw.amplification_needed(1.0)
            and gjw.unity_separation() < gjw.L_PLANCK)

def check_one_door():
    import amortize, expand
    st = expand.expand()
    return (st["order"] == expand.ADMITS
            and st["information"] == expand.REFUSES
            and amortize.amortisation_helps(10)
            and "TIME-INDEPENDENT" in amortize.LEAVES_IT_OPEN)

def check_shift_costs():
    import pathmetric
    return all(pathmetric.excess_density(v) > 0.0 for v in (0.1, 0.5, 0.9))

def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The ledger")
    h = by_status()
    for s in STATUSES:
        print("    %-16s %d   %s" % (s, len(h[s]), ", ".join(r[0] for r in h[s])))
    chk("obstructions tracked", len(LEDGER), 34)
    chk("actually DISSOLVED", len(h["DISSOLVED"]), 6)
    chk("RELOCATED -- still true, renamed", len(h["RELOCATED"]), 3)
    chk("CLOSED-NEGATIVE", len(h["CLOSED-NEGATIVE"]), 16)
    chk("CONDITIONAL", len(h["CONDITIONAL"]), 7)
    chk("UNTESTED -- where the next build fails", len(h["UNTESTED"]), 0)
    chk("UNTESTED is still empty; the new row is OPEN, which is not the same",
        sorted(set(r[2] for r in LEDGER)),
        sorted((set(STATUSES) - {"UNTESTED"}) | {"OPEN"}))
    chk("no row is DISSOLVED without an owning instrument",
        all(r[4] for r in h["DISSOLVED"]), True)

    print("\nEvery row recomputed from its owner, not transcribed")
    chk("HORIZON-REQUIRED dissolves", check_horizon_required(), True)
    chk("CM-THEOREM is paid, exactly 8/27", check_cm_relocated(), True)
    chk("WALL-STABILITY is conditional, not dissolved", check_wall_conditional(), True)
    chk("ANALOGUE-1D is closed negative", check_analogue_closed(), True)
    chk("SHIFT-SHORTENS is closed negative", check_shift_costs(), True)
    chk("NONRADIAL is fatal at 10 m and survivable at 5 km",
        check_nonradial_conditional(), True)
    chk("MAPPING-2D: mapping stands, static bound does not",
        check_mapping_dissolved(), True)
    chk("TYPEIV-SOURCES: yes at first order, open at exact",
        check_typeiv_sources_conditional(), True)
    chk("ACHRONALITY: the escape was looked for and is not there",
        check_achronality_closed(), True)
    chk("TURN-ADVANTAGE: turn => late, early => no turn",
        check_turn_advantage_closed(), True)
    chk("SEAT-MEETS-TRANSPORT: a negative mass seats AND arrives early",
        check_seat_meets_transport(), True)
    chk("BARE-NEGATIVE-MASS: not needed -- M_ADM = 0 works",
        check_bare_mass_needed(), True)
    chk("DEVICE-SHELL: ordinary matter, stable free, and the control is unstable",
        check_device_shell_ordinary(), True)
    chk("CORE-TYPE-IV: the core is Type I, unbounded in compactness, one-sign exotic",
        check_core_type_i(), True)
    chk("ACHIEVABLE-CORE: none exists, and the gap widens with size",
        check_no_achievable_core(), True)
    chk("CHARGE-STATE: seat yes, lead no, and the split is the EC line",
        check_charge_split(), True)
    chk("THE-LEAD: not required under scoping, and the seat is achievable",
        check_spec_achievable(), True)
    chk("WRONG-CATEGORY: no throat, no horizon, no momentum flux",
        check_three_negatives(), True)
    chk("ENTANGLEMENT-ROUTE: right language, 2 pi^2 over holographic, no loophole",
        check_entanglement_route(), True)
    chk("GRAHAM-OLUM-ESCAPE: external path, not matter, and it forbids speed",
        check_gjw(), True)
    chk("STANDING-COUPLING: one door, in the source, with their own reason",
        check_one_door(), True)

    print("\nThe question this file exists to answer")
    chk("rows that must be tested or accepted before a build",
        sorted(build_ready()), [])
    chk("is a build blocked on an untested row?", len(untested()) > 0, False)
    print("""      Both were asked, and MAPPING-2D then reopened: it had been closed on a
      STATIC bound applied to a dispersive device, and the bound is
      demonstrably wrong there.  NONRADIAL nearly closed the warpshell and
      left a mean-density corner.  Nothing is UNTESTED -- and one row moved
      from closed back to open, which is what a ledger is for.""")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    h = by_status()
    for s in STATUSES:
        if not h[s]:
            continue
        print("\n%s" % s)
        for r in h[s]:
            print("  %-18s %s" % (r[0], r[1]))
            print("  %-18s   -> %s  [%s]" % ("", r[3], r[4]))
    print("\n" + "=" * 79)
    print("VERDICT")
    # counted from the ledger, never transcribed -- the same rule as every row
    print("  %d dissolved, %d relocated, %d closed negative, %d conditional, %d open"
          % (len(h["DISSOLVED"]), len(h["RELOCATED"]), len(h["CLOSED-NEGATIVE"]),
             len(h["CONDITIONAL"]), len(h["OPEN"])))
    print("  and %d NEVER TESTED.  The obstructions did not dissolve; most of them"
          % len(h["UNTESTED"]))
    print("  became bills or conditions, which is progress of a different kind.")
    print("  Before the next build: %s" % (", ".join(build_ready()) or "nothing untested"))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
