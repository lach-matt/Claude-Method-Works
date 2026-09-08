#!/usr/bin/env python3
"""
index3.py -- the project as a closed index on its own three directives.

The directives are the axes:

    X  identify warp energy          -- what is it, and how much
    Y  can a warp drive be built     -- can a device produce or use warp transport
    Z  engineer specs and designs    -- does it yield engineering numbers

Every finding this project produced is a CELL at some (x, y, z) with each
coordinate in {-1, 0, +1}:

    +1  answers affirmatively
     0  silent -- does not bear on that directive
    -1  answers negatively: a BOUND

A -1 is an answer, not a failure.  P8 (The_Method_1_6-2.md 2.15): "any true
answer, good or bad, is a bound", and 2.17.3: "three bounds on one object are a
coordinate".  A cell with no zero in it sits on all three axes and is therefore
a coordinate in the exact sense the corpus gives the word.

The question this instrument answers: WHICH CELL SITS ON ALL THREE AXES, and
what supports it.

Closure follows the corpus's own three-body result (Chapter 36, Law 3): three
coupled axes are K_3, which needs strong 3-consistency where the closure
operator delivers 2.  So the join is expected to close and the meet is expected
to fail -- certainty survives upward and dies downward.  That prediction is
tested here rather than assumed.

stdlib only.
"""
import glob, itertools, os, sys

# (id, x, y, z, source file, one-line claim)
FINDINGS = [
 ("T1-STATE",    +1,  0, +1, "TARGET-1-RESULT.md",
  "warp state exists: 4 energy conditions positive, interior frame boosted 0.040000 c"),
 ("T2-ADM",       0, -1, -1, "TARGET-1-RESULT.md",
  "P_ADM = 0 exactly and M_ADM constant across v: the structure cannot translate"),
 # Le arXiv:2605.25417 / 2602.18023: single-frame Eulerian analysis misses 15-28% of
 # DEC violations, and metric-first constructions may not have a well-posed matter
 # model at all.  TARGET-1 is Eulerian and metric-first, so its verdict is not yet
 # frame-independent.  This cell records the gap, not a refutation.
 ("NOT-CERTIFIED", 0, -1,  0, "TARGET-1-RESULT.md",
  "no frame-independent Hawking-Ellis certification: Eulerian is not sufficient"),
 ("TRANSITION",   +1,  0, +1, "TARGET-1-RESULT.md",
  "the source-vacuum transition band is clean and converged; outer negatives fall 8x"),
 ("AXIAL-TERM",   0, -1,  0, "gatespec.py",
  "the shift must taper to zero along the bore axis, in vacuum: unchecked"),
 # The hoop bound stands as a necessary condition and is not sufficient: the ring
 # can hold its hole open, and the hole cannot hold a shift.
 ("OPEN-GATE",   +1, -1, +1, "torus.py",
  "hoop tension holds the bore open (5.89x) but the bore cannot carry a shift"),
 ("RELAX-OK",     0, +1, +1, "residue.py",
  "relaxation permits the flow and the switching: launch is 0.256 dynamical times"),
 ("NO-BORE",       0, -1, -1, "residue.py",
  "a bore closes 100x over before a payload crosses: the gate cannot be loaded"),
 ("NO-PORTAL",   -1, -1,  0, "launcher.py",
  "topological censorship: ANEC forbids any shortcut, so no portal either"),
 ("SSV-NOGO",    -1, -1,  0, "WARP-DRIVE.md",
  "Santiago-Schuster-Visser: M_ADM = 0 warp drives violate the NEC"),
 ("SCALE",       +1,  0, +1, "THE-DRIVE.md",
  "M ~ R and rho ~ 1/R^2: nuclear matter at 4.9 km, 1.11 Msun"),
 ("CIRCULATION", +1,  0, +1, "THE-DRIVE.md",
  "mechanism is internal circulation at 0.330 c, geared 6.94:1, 4.4x stress margin"),
 ("COUPLING",    +1, +1,  0, "COUPLING.md",
  "the drive is a coupling: energy borrowed, ADM silent on falling, so it is possible"),
 # Seated because the index PREDICTED it: join(SSV-NOGO, T2-ADM) = (0,-1,0) was
 # a cell the closure demanded and no finding held.  The theorem existed inside
 # COUPLING.md but had never been isolated from the mechanism it was argued for.
 # It is the only bound on Y that is free of both X and Z: it holds whatever the
 # drive is made of and whatever its design.
 ("CM-THEOREM",   0, -1,  0, "COUPLING.md",
  "M_total a_cm = 0: no isolated system moves its own centre of mass, any design"),
 ("WELL",        +1, +1,  0, "THE-BORROWED-WELL.md",
  "dv = c sqrt(r_s/b): transport borrowed from an existing gradient, energy zero"),
 ("FLYBY",       +1, +1, +1, "THE-GR-FLYBY.md",
  "dv = 2U/(1+U^2) strong field; tides bound the deflector below at ~1e4 Msun"),
 ("SLINGSHOT",   +1, +1, +1, "THE-ENGINE.md",
  "non-saturating gain, 50%/pass at 0.2c: 0.87 c in 11 min at 1 g, zero propellant"),
 ("NAVIGATE",     0, +1, +1, "NAVIGATION.md",
  "Law 4: no trajectory exists; fly a braid word; 25:1 binary, stable L4/L5"),
 ("ARRIVAL",      0, +1, +1, "arrival.py",
  "braking priced: magsail 810 AU at 0.048c; M0/M1 = 3.73 at 0.87c; reverse pass free"),
 ("SWIMMER",      0, -1, -1, "THE-ENGINE.md",
  "curvature swimmer bounded by A*a_tide/c^2 ~ 1e-15 m per cycle: a dead engine"),
 # --- Seated late, and their absence is why this project LOOPED. The index only
 # holds what is seated, so E(X)=0 was measuring the completeness of the
 # BOOKKEEPING, not of the knowledge. ROTATING-SHELL in particular already held
 # the J result twelve exchanges before it was "discovered" again.
 ("ROT-SHELL",    0, -1, +1, "ROTATING-SHELL.md",
  "counter-rotation is REQUIRED: J != 0 gives a Kerr exterior and breaks the construction"),
 ("SHIFT-CEIL",  +1,  0, +1, "SHIFT-CEILING.md",
  "closed form for the shift ceiling: v_max = Phi f / k_hat"),
 ("SHELL-PROF",  +1,  0, +1, "SHELL-PROFILE.md",
  "the shell reconstructed by TOV integration"),
 ("MEASURED",    +1,  0, +1, "MEASURED.md",
  "the ceiling measured under Warp Factory (absolute figures later withdrawn)"),
 ("WHAT-BINDS",  +1,  0, +1, "WHAT-BINDS.md",
  "the fill curve measured, overturning this series' own design rule"),
 ("DENSITY",     +1,  0, +1, "DENSITY-IS-CLOSED.md",
  "density shaping built and measured: a closed lever with its mechanism"),
 ("SPHERICITY",   0,  0, +1, "SPHERICITY.md",
  "sphericity cost measured; the oblate test failed its own control"),
 ("ACCEL",        0, -1,  0, "ACCELERATION.md",
  "the first ADM argument against self-acceleration, later narrowed by COUPLING"),
 # The theorem the loop produced, which neither visit gave alone.
 # The object is what is shifted, so the object's measured density decides the
 # magnitude -- and f <= 1 caps the whole sourcing branch at 7.1% of light.
 ("GRAD-CLOSED",  0, -1,  0, "gradients.py",
  "the gradient space is a classification, not a survey: 5 types, only one pumps"),
 ("NO-MANUFACTURE",0, -1,  0, "gradients.py",
  "a made hole cannot survive: a century needs 3.3e8 kg inside 5e-19 m"),
 ("GW-MEMORY",     0, -1, -1, "gradients.py",
  "radiation gives displacement without velocity: 2.5 cm at 10 r_s, then it stops"),
 ("OBSERVED-ENGINE",+1,+1, +1, "gradients.py",
  "the engine runs today on protons: UHECRs ARE the proof of concept"),
 ("KERR-FLYBY",  +1, +1, +1, "shipspec.py",
  "spin buys 1.612x in dv (b_crit 5.196 -> 2) at 27x tides, i.e. 5.2x deflector mass"),
 ("VEHICLE-SPEC", 0, -1, +1, "shipspec.py",
  "35 fields, 11 open: fully specified, and the engine is a found object nobody has found"),
 ("OBJ-CEILING", +1, -1, +1, "elements.py",
  "v_warp <= Phi/k_hat = 0.0713 c for ANY object: f = r_s/R and f <= 1"),
 ("PERIODIC",    +1,  0, +1, "elements.py",
  "the element sets the density, density sets compactness, compactness IS the shift"),
 ("SHIFT-CHARGE", 0, -1,  0, "THE-LOOP.md",
  "every route to a shift is closed by one accounting: the charge that sources it"),
 ("EM-GAP",      -1, -1, -1, "ENGINE-ASSESSMENT.md",
  "the electromagnetic architectures fail as sources by ~10^31"),
 # --- The three cells the closure predicted at E(X) = 4.  Each existed in
 # substance inside an entangled finding and had never been isolated, exactly
 # as CM-THEOREM had not.  Seating them is bookkeeping, not new physics -- and
 # that they all had to be dug out is itself the finding: this project produces
 # entangled results, and the index keeps demanding the disentangled ones.
 # The structural answer to the structural limit: the theorem forbids moving
 # YOURSELF, so the object stops being a vehicle and becomes infrastructure.
 # First cell on (+1,+1,+1) that is a CONSTRUCTED object rather than a found one.
 # SUPERSEDED by NO-TAPER: the launcher's physics stands (TARGET-1 verified the
 # boosted flat interior) but it can be neither loaded nor unloaded, so it is not
 # buildable.  Y falls from +1 to -1; X and Z stand.
 ("LAUNCHER",    +1, -1, +1, "GATE-CLOSED.md",
  "geodesic launcher: physics sound, 0 g, but it can be neither loaded nor unloaded"),
 # Both predicted by the closure the moment the gate died, and both already held
 # in substance -- the fourth and fifth time the defect has named a real finding.
 ("SPEC-SHEET",   0, -1, +1, "gatespec.py",
  "the gate is fully specified and unbuildable: 44 fields, 9 open, 3 invalidated"),
 ("SOURCING-DEAD",+1, -1,  0, "GATE-CLOSED.md",
  "the verdict on the manufactured branch: energy known, device impossible, nothing to draw"),
 # The audit that reads the bounds as a direction instead of an obituary: five
 # of eight carry ASYMPTOTIC FLATNESS, and the universe does not.  Same shape as
 # CM-THEOREM, where every failure shared the word ISOLATED.
 ("FLAT-HYP",     0, +1,  0, "cosmo.py",
  "5 of 8 bounds assume asymptotic flatness; in FLRW they are not even statable"),
 ("FLRW-OBS",    +1, +1,  0, "cosmo.py",
  "superluminal geodesic metric transport is OBSERVED, dust satisfies all four"),
 # NARROWED by kerr.py.  The measurement stands; the generalisation did not.
 # Kerr has g_tphi != 0 and T = 0 everywhere outside the horizon.
 ("NO-TAPER",     0, -1, -1, "GATE-CLOSED.md",
  "a COMPACTLY SUPPORTED shift needs Type IV in vacuum: measured, every cell"),
 ("KERR-SHIFT",  +1, +1,  0, "kerr.py",
  "a vacuum shift CAN decay asymptotically: Kerr drags at 0.5c with T = 0"),
 ("J-NOT-P",      0, +1,  0, "kerr.py",
  "CM-THEOREM forbids manufacturing P and says nothing about J"),
 ("NO-EXOTIC",   +1,  0,  0, "TARGET-1-RESULT.md",
  "the warp source is ordinary matter: there is no distinct species of warp energy"),
 ("FREE-FALL",    0, +1,  0, "COUPLING.md",
  "a body in free fall is transported with no thrust, any material, any design"),
 ("PROFILE",      0,  0, +1, "THE-DESIGN-EQUATION.md",
  "max|S''| >= 4/d^2 and gamma_opt = 1+sqrt(3): closed-form optima, pure geometry"),
 # person.py.  Zhang's law is a law about test particles; extent is the whole
 # difference between a proton and a person, and it enters through one group.
 ("FRAGILITY",    0,  0, +1, "person.py",
  "chi/tau_s is the only argument: k = (chi/tau_s)^(2/3), extent and tolerance never separate"),
 # NARROWED, and this time by a measurement rather than by a theorem of mine:
 # A&R's Monte Carlo puts one encounter's worth at 0.039 c off this deflector.
 ("CATALOGUE",   +1, +1, +1, "person.py",
  "a person at 50 Msun and a proton at 1.2e9 kg are the SAME mission -- one encounter, 0.039 c"),
 # A bound, and it is the clock rather than the mass that sets it.
 ("MERGER-CEIL",  0, -1, +1, "person.py",
  "beta <= 0.0587 or the flywheel merges mid-mission; Zhang's headline 0.2 misses by 132x"),
 # The one unevidenced object left in VEHICLE 1, and it is not where it was.
 ("ROUTH-FORK",   0,  0, +1, "person.py",
  "the IMBH is a PARKING requirement, not a tidal one: L4/L5 needs a 1248 Msun companion"),
 # stationkeep.py.  The OPEN row every sheet carried, and then the literature.
 # BOUND-RETURN, DV-TREADMILL and ARCH-CEILING were seated here and are WITHDRAWN:
 # they assumed E/m is conserved in a binary, which it is not.  BILLIARD's open
 # question is ANSWERED -- by Fermi, in 1949.  What replaces them:
 ("PAIR-TRAPS",   0, +1, +1, "stationkeep.py",
  "a binary returns the payload for free: perpetual null orbits exist, so N is not bounded"),
 ("SECOND-ORDER", 0, -1, +1, "stationkeep.py",
  "unsteered the mechanism is second order in beta_A: 33x the passes, and it misses the merger clock"),
 ("STEER-IS-ALL", 0, +1, +1, "stationkeep.py",
  "steering is the mechanism, not an optimisation: it is what holds Zhang's optimum over Fermi's average"),
 ("NU-OPEN",      0,  0, +1, "stationkeep.py",
  "OPEN: the per-pass vanquish probability must be held near zero for 1090 passes; nobody has computed it"),
 # The ladder was a conjecture, and somebody had already run the simulation.
 ("NO-COMPOUND",  0, -1, +1, "stationkeep.py",
  "Acevedo & Ritz's Monte Carlo delivers 0.72x ONE encounter, not a ladder: order unity, not 1e9"),
 ("JACOBI",       0, -1, +1, "stationkeep.py",
  "the helical Killing vector caps gamma at (1+b_co)/(1-b_co) with no N in it -- true, and 9x too loose"),
 ("TWO-BODIES",   0,  0, +1, "stationkeep.py",
  "a > 2 k r_s or there is only one deflector; at k = 3 that IS the ISCO limit, identically"),
 # necladder.py -- read out of the volumes at M's prompting.  The NEC is not a
 # boolean, and this project has been standing on the strictest of its five rungs.
 ("RUNG-1",      +1, +1,  0, "necladder.py",
  "the world is MEASURED at NEC rung 1: Casimir violates the NEC pointwise, and that is free"),
 ("RUNG-0-NOGO",  0, -1, +1, "necladder.py",
  "every no-go this project obeyed was graded at rung 0; the index's core is at rung 3"),
 ("QNEC-GAP",    +1,  0,  0, "necladder.py",
  "<T_kk> >= (h/2pi) S''_out: entanglement entropy is the budget, and it is in no alphabet here"),
 ("IC-GUARD",     0, -1,  0, "necladder.py",
  "NEC>=3 forces IC v U v X: macroscopic exotic matter is guarded by a CORRELATION principle"),
 # beamed.py -- the engineering read at M's ruling.  The coupling family's
 # inventory problem was self-inflicted: the source is built, not found.
 ("BUILT-SOURCE",+1, +1, +1, "beamed.py",
  "1000 t to 0.700 c is a published point design; the found-object route gave 0.039 c for 2 m"),
 ("MASS-QUARTER", 0,  0, +1, "beamed.py",
  "v ~ m^(-1/4): the sail grows with the payload, so 10^5 in mass costs 17.8x in speed"),
 ("APERTURE",     0,  0, +1, "beamed.py",
  "D_array x d_sail = lambda x range: acceleration ends where the spot outgrows the sail"),
 ("ENERGY-BILL",  0, -1, +1, "beamed.py",
  "the crewed design wants 1.25e23 J -- 208 world-years at 10 PW for 144 days: a bill, not a bound"),
 ("NO-CARRIER",   0, -1,  0, "beamed.py",
  "theta = 1/gamma has no aperture term: no particle beats photons, so two ends pay light-time"),
 # restatus.py -- every architecture regraded by HOW it closed, at M's ruling.
 ("CLOSURE-KIND", 0, -1, +1, "restatus.py",
  "of six closures this project reasoned to itself, ZERO are MEASURED and five are hypothesis or cost"),
 ("KAPPA-DEAD",   0, -1,  0, "restatus.py",
  "Rodal 2025 closes kappa(x) by MEASUREMENT -- Bianchi, MICROSCOPE, Cassini, PSR J0337: no escape"),
 # NARROWED by device.py TEST 16: the bound that makes it stable also forbids
 # the horizon, so the bench article confirms the medium and not the metric.
 ("ANALOGUE",    +1,  0, +1, "restatus.py",
  "the Alcubierre metric maps onto eps, mu, g_x -- buildable at v <= c/4, but no horizon at any n"),
 # door.py -- M's correction.  "Does not couple to real spacetime" is withdrawn.
 ("THE-DOOR",    +1, +1, +1, "door.py",
  "Sec 17.1: a construction is closed from OUTSIDE by measurement -- 5 of 7 analogue claims pass, 4 are done"),
 ("S-OUT-SEEN",  +1,  0,  0, "door.py",
  "the QNEC's S_out has been MEASURED: Steinhauer's Hawking pair is entangled across the horizon"),
 # EC-UNTAKEN is TAKEN.  neclab.py answers it: yes, and it costs 3.15%.
 ("EC-TAKEN",    +1, +1, +1, "neclab.py",
  "the medium CAN carry the analogue NEC violation: margin +0.9685 where the geometry asks most"),
 ("SHIFT-NOT-GRAD",0, 0, +1, "neclab.py",
  "m depends on f~ alone and decreases, so margin-min sits at max f~ and NEC-peak strictly inside: disjoint"),
 ("C4-CORRECTED", 0, -1, +1, "neclab.py",
  "c/4 is the leading-order bound; the full Eqs (6),(7) saturate at 0.245826 and are unstable at 0.25"),
 # device.py -- the parts list, every field tested as it was written.
 # The HARDWARE closes; what it proves does not.  Y stays +1 (it is buildable),
 # X drops to 0 (it identifies no warp energy), Z stays +1 (it yields numbers).
 ("THE-DEVICE",   0, +1, +1, "device.py",
  "a 9.8 cm YIG bar at 8.22 GHz emulating v_0 = 0.222 c: buildable, and it proves the medium not the metric"),
 ("SRR-FAILED",   0, -1, +1, "device.py",
  "a single-gap ring of the required size resonates at 118 GHz, 16x too high: broadside coupling or nothing"),
 ("REGISTRATION", 0, -1, +1, "device.py",
  "one cell of layer mis-registration gives margin -0.355 at the outer wall; derate 9.5% or co-locate"),
 # Two more parts tests, and a cascade they set off.
 ("GAP-DERIVED",  0,  0, +1, "device.py",
  "eps = mu forces d = S w/c: the ring gap is a CONSTRAINT, and every free knob became derived"),
 ("FERRITE-EPS",  0, -1, +1, "device.py",
  "YIG's own eps_r = 15 caps the fill at 8.8%, pulling the operating point from 1869 to 128 linewidths"),
 # Three more, and the first says the drawn geometry was wrong.
 ("ONE-AXIS",     0,  0, +1, "device.py",
  "Smolyaninov's mapping is 1+1D: y and z are flat spectators, so it is a graded STACK, not a bubble"),
 ("FERRITE-RULES",0,  0, +1, "device.py",
  "Polder gives mu-1 = g_x, so one inclusion carries 90% of eps, mu and g_x -- the rings are the margin"),
 ("FERRITE-FOM",  0, -1, +1, "device.py",
  "loss is invariant under n by exact cancellation; the only knob is Ms/((eps_r-1) dH)"),
 # The verdict.  The hardware works; the epistemics do not, and the reason is a theorem.
 ("NO-HORIZON",   0, -1, +1, "device.py",
  "stability caps v_0 at c(n-1)/n^2 and a horizon needs c/n: (n-1)/n^2 < 1/n for EVERY n"),
 ("RELABEL-ONLY", 0, -1,  0, "device.py",
  "the 2146-degree non-reciprocity is enormous and follows from the g_x built: it confirms the medium"),
 ("T-H-TOO-COLD", 0, -1, +1, "device.py",
  "analogue Hawking is 4.96 mK, below a fridge's 10 mK base; ~100 GHz in 8 mm would give 60 mK"),
 # The deeper reading of TEST 16.  A horizon was never the requirement, and the
 # 1+1D reduction the whole device rests on emulates flat spacetime.
 ("NO-HORIZON-NEEDED", 0, +1,  0, "twist.py",
  "a horizon exists iff v_s >= c, at f* = 1 - c/v_s: it is the superluminal pathology, not a requirement"),
 ("TWIST-IS-3FORM",   0, -1, +1, "twist.py",
  "xi ^ dxi is a 3-form, identically zero on a 2-manifold: >= 2+1D is necessary before a shift is irremovable"),
 # The identity.  Exotic matter and the twist are the same object.
 ("E-IS-TWIST",      +1,  0,  0, "twist.py",
  "E = -Omega^2/(8 pi G): the Alcubierre negative energy IS the coordinate vorticity, squared"),
 ("ONE-AXIS-FLAT",   -1, -1, -1, "twist.py",
  "the 1+1D reduction is the on-axis line, where Omega = 0 and E = 0: the emulated geometry is Minkowski"),
 # Le arXiv:2606.22531.  The first architecture with no negative energy in it.
 ("BONDI-PAYS",       0, +1, +1, "warpshell.py",
  "CM-THEOREM is paid, not evaded: Bondi four-momentum changes only by radiating, and a positive-energy drive saturates it"),
 ("NO-EXOTIC",       +1, +1, +1, "warpshell.py",
  "an accelerating warp drive exists with dominant energy observer-robust in bulk AND shell: no exotic matter at any point"),
 ("DOPPLER-CUBED",    0,  0, +1, "warpshell.py",
  "m_f/m_0 = e^{-3 eta} = the relativistic Doppler factor cubed; 8/27 to reach 0.2 c and stop"),
 ("MARGINAL-WALL",    0, -1, -1, "warpshell.py",
  "the realized wall sits on the Poisson-Visser marginal curve; a habitable 1 g, 10 m design misses the burn criterion by 1.8e14"),
 # Stability is structural, so the fix is the equation of state.  wall.py.
 ("STIFF-WALL",      +1, +1, +1, "wall.py",
  "strictly stable iff beta^2 > (1-s)(3s^2+2s+1)/(4s^2(1+3s)): 0.0793 at x=0.3, and subluminal through all of x < 0.8437"),
 ("DEC-DECOUPLED",    0,  0, +1, "wall.py",
  "the junction fixes sigma_0 and p_0 with no beta^2 in them, so V(R_0)=V'(R_0)=0 identically: stiffness is free in dominant energy"),
 ("BASIN-THEOREM",   +1,  0,  0, "wall.py",
  "beta^2_crit - p_0/sigma_0 = x/(4s^2(1+3s)) > 0 exactly: strict stability IMPLIES an unbounded dec basin"),
 ("BURN-INVERTS",     0, +1, +1, "wall.py",
  "a stable wall oscillates, so the burn must be adiabatic not fast: the 1.8e14 shortfall becomes a 2.2e14 margin"),
 # The method equation's metric half, run on spacetime.  Sec 12.11.1.3 routes it.
 ("JACOBI-IS-GR",     0,  0, +1, "pathmetric.py",
  "the metric half applied to a static spacetime IS the geodesic equation: Jacobi orbit == Schwarzschild to 1.6e-15"),
 ("HORIZON-IS-HILL",  0, -1, +1, "pathmetric.py",
  "the horizon is V=0, where the optical metric blows up; V=E/m is Hill's 1878 zero-velocity surface: classical degeneracies, not warp pathologies"),
 ("SHIFT-COSTS",      0, -1, -1, "pathmetric.py",
  "round trip = INTEGRAL 2c dx/(c^2-v^2), longer by 2v^2/(c(c^2-v^2)) > 0: any 1+1D shift strictly increases the invariant distance"),
 # The obstruction ledger, and the one test that nearly closed the warpshell.
 ("BETA-NOT-FREE",   0, -1, +1, "wall.py",
  "beta^2 is DETERMINED by the matter, not chosen: counter-rotating matter clears the threshold only below x = 0.46898"),
 ("NONRADIAL",       0, -1, +1, "wall.py",
  "Pitre-Schneider-Poisson: unstable for all l>=2, all compactness, all Gamma, on Le's anchor -- and beta^2 is absent from that branch"),
 ("DENSITY-CEILING", 0, -1, +1, "wall.py",
  "the l>=2 rate is self-gravitational, so N<1 is a mean-density ceiling of 2.66e-4 kg/m^3 -- but density and compactness share a mass"),
 ("CORNER-EXITS",    0, -1, -1, "wall.py",
  "escaping l>=2 means x -> 0: the survivor is a 3.97 g/m^2 balloon whose flat cavity is Birkhoff; stable AND self-gravitating needs 2e9 Msun over 1,000 AU"),
 ("SECOND-CLAUSE",  +1, +1,  0, "shape.py",
  "a bound relaxed by changing the object must be checked against what the object was for: an escape that exits the category is not an escape"),
 # The spectral index used as a materials screen.
 ("S-STATE",         0,  0, +1, "materials.py",
  "exactly four S-state shells exist -- s1, p3, d5, f7 -- so Fe3+ is optimal in its shell and f7 is the only way up"),
 ("COLD-MS",         0,  0, +1, "materials.py",
  "device.py paired room-temperature Ms with cryogenic linewidth; corrected, the ferrite merit rises 42.9% and loss falls 30.4%"),
 ("F7-CEILING",      0, -1, +1, "materials.py",
  "EuO's Ms is 9.5x YIG's cold value, so the f7 ceiling is 5.8x -- behind a crystal-growth problem, not a physics one"),
 # MAPPING-2D taken: the mapping was never missing, the medium is.
 ("PLEBANSKI",      +1,  0, +1, "plebanski.py",
  "Plebanski 1960 maps any metric to a medium in full 3+1D, and Alcubierre's gives eps_xx=1, eps_yy=1/(1-v^2), w=-v/(1-v^2)"),
 ("ANISOTROPIC",    +1,  0, +1, "plebanski.py",
  "the exact medium is anisotropic wherever the shift is nonzero: the transverse structure twist.py demanded, present by construction"),
 ("BHS-3D",          0, -1, -1, "plebanski.py",
  "w^2 <= (eps_yy-1)^2 requires v^2 <= v^4: the exact 3+1D medium is forbidden at EVERY subluminal shift, and conformal freedom is invariant"),
 # The exemption, tested -- and it was staticity, not passivity.
 ("STATIC-WRONG",    0, +1, +1, "dispersive.py",
  "a Polder ferrite above resonance violates BHS by up to 5x and is an ordinary passive component: the static bound does not apply here"),
 ("BRILLOUIN",      +1,  0, +1, "dispersive.py",
  "the dispersive condition is d(w kappa)/dw <= d(w mu)/dw - 1, whose ratio is 2 w w0/(w0^2+w^2) <= 1 identically, saturating at resonance"),
 ("C4-WITHDRAWN",    0, +1, +1, "dispersive.py",
  "the c/4 ceiling was a static bound on a dispersive device: beta reaches 0.825 at 0.95% ferrite loss, a 3.7x gain for 4.3x the loss"),
 # The shape as an instrument: cheap, because it is math and not a material.
 ("THE-SHAPE",      +1, +1,  0, "shape.py",
  "a no-go built on a static positivity condition loosens when the dynamics is restored: four closures moved by that one move"),
 # The one thing here that goes on a bench.
 ("LOOP-OBSERVABLE",+1, +1, +1, "bench.py",
  "measure the loop, not the line: the closed-loop phase 2k_0 INT w.dl is gauge-invariant exactly where the twist is nonzero"),
 ("HARD-NULL",       0, +1, +1, "bench.py",
  "the control is a dimension theorem, not a small number: a longitudinally graded sample gives exactly zero, and a uniform w does too"),
 # DIRECTIVE 1, CLOSED.
 ("WARP-ENERGY-IS", +1,  0, +1, "warpenergy.py",
  "warp energy is the squared twist of the shift, negative, and fixed by geometry alone: no matter model enters it"),
 ("WARP-ENERGY-HOW",+1,  0, +1, "warpenergy.py",
  "M = -(v_s^2/12G) INT f'^2 r^2 dr exactly, verified against direct 3-D integration to 5e-12"),
 ("AREA-OVER-THICK",+1, -1, +1, "warpenergy.py",
  "M ~ -v_s^2 R^2/(36 G D): the bill is area over thickness, so the wall is the whole cost and R is not the lever"),
 # DIRECTIVE 2's stated obstacle, and it is the wrong instrument.
 ("NO-NULL-QI",     +1, +1, +1, "nullbound.py",
  "Register 5537: there are no quantum inequalities along null geodesics in 4D, so the timelike bound on the wall is the wrong instrument"),
 ("D-CANCELS",      +1, +1, +1, "nullbound.py",
  "required and allowed both go as 1/(G D^2), so thickness and G cancel: the ratio is v_s^2/(288 pi B), constant over 32 orders in D"),
 ("V-IS-BOUNDED",    0, +1, +1, "nullbound.py",
  "what the null condition bounds is velocity, not thickness: saturation at v_s = 3c, with 900x margin at 0.1c"),
 # USING the breakthrough: directive 3 gets a design equation.
 ("DESIGN-EQUATION",+1, +1, +1, "designpoint.py",
  "M = -beta^2 c^2 R/(12 G) at the thickest admissible wall: one line, two variables, and no D in it"),
 ("CHANGE-OF-KIND", +1, +1, +1, "designpoint.py",
  "1.5e9 observable universes -> 18.8 Earth masses at R=100 m, 0.1c: a factor 2e36 and a change of category"),
 ("GAP-NOT-BOUND",   0, +1, +1, "designpoint.py",
  "the remaining 2.3e42 to a Casimir source is a gap in capability with no theorem in it, which is a different situation"),
 # The objection that replaces the one nullbound.py removed.
 ("TYPE-IV",        +1, -1, -1, "typefour.py",
  "the Alcubierre wall is Hawking-Ellis Type IV at 7/7 points, |Im|/||T|| from 0.14 to 0.69, stable to six figures in h"),
 ("KIND-NOT-SIZE",  +1, -1,  0, "typefour.py",
  "every energy condition bounds a CONTRACTION of T; Type IV is about its eigenvectors, so no energy-condition result reaches it"),
 ("THE-TRADE",      +1, -1, +1, "typefour.py",
  "Alcubierre has a tractable budget and Type IV matter; the warpshell has Type I matter and the l>=2 instability. Neither has both"),
 # QNEC asked properly, and it withdraws this session's headline.
 ("ANEC-VIOLATED",  +1, -1, -1, "anec.py",
  "INT T_kk dx is negative on every ray, -0.081 to -0.344: ANEC is violated and QNEC, a theorem, integrates to it"),
 ("SNEC-RETRACTED",  0, -1,  0, "anec.py",
  "SNEC must hold for EVERY sampling function; nullbound.py used one, the loosest, and it fails above w ~ 0.93 bubble radii"),
 ("D-IRRELEVANT",   +1, -1,  0, "anec.py",
  "the thickness really does drop out -- into prohibition, not permission: ANEC is violated at every D, so the 10^62 kg was the wrong statement"),
 # The inversion: not which element, but which state.
 ("STATE-NOT-ELEMENT",+1, +1, +1, "universal.py",
  "Type IV is realized by a quantum STATE -- the Unruh vacuum, Type IV outside the horizon -- which belongs to no element and to every element's fields"),
 ("ESCAPES-TYPE-I",  +1, +1, +1, "universal.py",
  "MMV force Type I in four back-reacting cases and the bubble is outside all four: not static, no Killing horizon, NOT CIRCULAR, not homogeneous"),
 ("TWIST-IS-WHY",    +1,  0, +1, "universal.py",
  "one reason for all four: twist = 0 gives Minkowski (BBV) and Type I (MMV), so Type IV is forced by the same property that makes it transport"),
 ("SELF-CONSISTENT-OPEN", 0, -1,  0, "universal.py",
  "whether a Type IV solution can SOURCE its own geometry is unsettled: MMV's list is explicitly not exhaustive, and no construction exhibits one"),
 # ANSWERED, at first order, and the status is not flattened: the row above
 # stays as it was asked, and these four say what came back.
 ("SOURCES-ITSELF", +1, +1,  0, "selfconsistent.py",
  "Abdolrahimi-Page-Tzounis solve G = 8 pi <T> with the Unruh state and get Type IV everywhere outside an evaporating horizon: a Type IV stress-energy DOES source a metric"),
 ("MAGNITUDE-MATCH",+1,  0, +1, "selfconsistent.py",
  "<T> goes as mu^-4, so a 1 m 0.1c bubble needs the Type IV strength of a 1.126e9 kg hole: a primordial-BH mass, not an absurd one"),
 ("CONFIG-UNMATCHED", 0, -1, -1, "selfconsistent.py",
  "the hole's Type IV is a spherically symmetric RADIAL flux and the bubble needs a twisted one: same type, same strength, different shape, and a magnitude match is not a construction"),
 ("EXACT-ORDER-OPEN", 0, -1,  0, "selfconsistent.py",
  "APT compute <T> on the UNPERTURBED background and do not iterate to a fixed point; MMV's theorems are about exact solutions, so neither refutes the other and exact order stays open"),
 # The order language, run on the ANEC obstruction.  It closes the escape
 # I proposed, and it closes it against us -- which is still an answer.
 ("ACHRONAL",       +1, -1, -1, "achronal.py",
  "every ANEC-violating ray of the bubble is ACHRONAL: 25 violating rays over v_s = 0.3/0.5/0.8 c and ZERO escapes, so Graham-Olum's hypothesis is met"),
 ("DEFOCUS-PROTECTS",+1, -1,  0, "achronal.py",
  "the anti-correlation is Raychaudhuri itself -- u'' = -4 pi T_kk u, so negative T_kk defocuses and defocusing is what prevents the conjugate point: you cannot buy achronality-failure with ANEC violation"),
 ("ACHRONAL-LEMMA", +1,  0,  0, "achronal.py",
  "PROVED where T_kk <= 0 throughout: u convex with u(0)=0, u'(0)=1 gives u >= lambda > 0, no zero, no conjugate point. Exact on the axial ray; measured where the signs are mixed"),
 ("UNPROVEN-LOAD",   0, -1,  0, "achronal.py",
  "with no configurational dodge left, the prohibition rests ENTIRELY on the achronal ANEC in 4D CURVED spacetime -- unproven for nineteen years, and now load-bearing rather than a footnote"),
 ("LANGUAGE-BOUNDARY",0, -1, 0, "achronal.py",
  "register 1173: analysis returns a magnitude, the prohibition is a binary. anec.py's verdict crossed a language boundary with the ORDER half NOT-RUN -- a sixth instance of register 1172's fault, in our own tree"),
 # M's three-part structure -- travel > turn > seat -- made runnable, and
 # M's both-ends prediction tested rather than admired.
 ("BOTH-ENDS",      +1,  0, +1, "transit.py",
  "M PREDICTED IT AND IT HOLDS: the conjugate length is identical read from departure or arrival, 1e-14 on five rays and 0.00e+00 on an asymmetric control, because the Jacobi operator is self-adjoint"),
 ("GATED-STRUCTURE", 0,  0, +1, "transit.py",
  "travel > turn > seat is coherent and correctly gated: part 2 refuses to initialize without both endpoints declared at onset, and FAILS rather than defaults when the conditions cannot reach part 3"),
 ("TURN-NEEDS-ORDINARY",+1,+1, 0, "transit.py",
  "u'' = -4 pi T_kk u turns back only where T_kk > 0, so the turn succeeds ONLY on ANEC-SATISFYING rays: whatever seats a transition lives in the ordinary-matter half, not the exotic one"),
 ("TURN-IS-LATE",    0, -1, -1, "transit.py",
  "and that half arrives late: every turning ray carries a positive Shapiro delay, every early ray fails to turn. TURN => LATE, EARLY => NO TURN, no configuration on this metric has both"),
 # The conjugate point as an index: what does and does not seat, universally.
 ("UNIVERSAL-SEAT", +1, +1, +1, "seatindex.py",
  "Sturm: q >= m over a contiguous l >= pi/sqrt(m), i.e. m l^2 >= pi^2, seats UNIVERSALLY -- the turn happens INSIDE the stretch, so nothing outside can prevent it, measured against hostile surroundings at every approach"),
 ("NOTHING-BELOW",   0, -1, +1, "seatindex.py",
  "Lyapunov: L INT q+ <= 4 excludes seating for ANY shape. 12 cells excluded, 0 seat. The bound is universal in the other direction"),
 ("THREE-POPULATIONS",+1, 0, +1, "seatindex.py",
  "register 1206's partition, run and not assumed: 64 interior captures all seat, 12 exterior none seat, and the 84-cell working overlap does both -- which is what makes it the overlap"),
 ("LONG-AND-WEAK",  +1, +1, +1, "seatindex.py",
  "the frontier costs INT q = pi^2/l, so universal seating gets CHEAPER without limit as the focusing region lengthens: long and weak beats short and strong"),
 ("ORDINARY-MATTER",+1, +1, +1, "seatindex.py",
  "T_kk >= pi c^4/(4 G l^2) = 9.5053e43/l^2 Pa -- positive, energy-condition-satisfying, and BELOW nuclear density beyond ~100 km. Matter that seats a conjugate point exists in nature"),
 ("C-FOLDS",         0,  0, +1, "seatindex.py",
  "the position coordinate FOLDS about the midpoint rather than being removed: transit.py's reversal theorem spent as a coordinate saving, self-adjointness halving the index"),
 # Where universal seating meets universal transport.  It is not empty, and
 # every earlier pass missed it by dropping shear from the Jacobi equation.
 ("WEYL-IS-SIGNBLIND",+1,+1, +1, "composite.py",
  "Ricci focusing is LINEAR in the source and needs positive energy; WEYL focusing is QUADRATIC and does not. A negative mass shears a congruence exactly as hard as a positive one"),
 ("SEATS-AND-EARLY", +1, +1, +1, "composite.py",
  "MEASURED: M = -2e-3 gives a conjugate point at lambda 56.5 AND arrives early (-3.76e-2), while +2e-3 seats at 55.2 and arrives late. Both signs seat; only the arrival flips. TRUE AT ITS OWN BASELINE and not beyond it: the same bare mass at b=1 turns LATE past X ~ 350"),
 ("THE-WINDOW",      +1, +1, +1, "composite.py",
  "bounded on both sides: below, the focal length exceeds the run and it does not seat; above, the M^2 path lengthening beats the linear Shapiro. About a decade wide at b=0.3, L=75. A THIRD BOUND was found later and it is on RANGE, not on mass -- chronology.py's LOG-AGAINST-LINEAR"),
 ("DROPPED-TERM",     0, -1, +1, "composite.py",
  "achronal.py, transit.py and seatindex.py all wrote u'' = -(R_kk/2)u, dropping shear as conservative. Conservative for an EXISTENCE claim about one ray; FATAL FOR A SEARCH"),
 ("VACUUM-PATH",     +1, +1, +1, "composite.py",
  "the early ray travels entirely through vacuum -- T_kk = 0 on the whole path, ANEC not violated along it -- and past its conjugate point it is not achronal, so Graham-Olum does not reach it"),
 # The corridor: M's vacuum, and the two readings of it compared.
 ("VACUUM-FORCES-WEYL",+1,+1,+1, "corridor.py",
  "a classical vacuum corridor has T_kk = 0, so Einstein forces R_kk = 0 and WEYL is the only focusing available: M's constraint SELECTS composite.py's mechanism and rules out Alcubierre, which needs matter where the rays go"),
 ("CORRIDOR-CLOSED-FORM",+1, 0,+1, "corridor.py",
  "RICCI/WEYL = 4 alpha/(z(1-z) mu^2) exactly -- no z^3, no 16 pi, symmetric about z = 1/2 -- so WHERE in the corridor you stand does not matter, only the mass"),
 ("CLASSICAL-WINS",  +1, +1, +1, "corridor.py",
  "crossover mu = 4 sqrt(alpha) = 5.3293e-10 kg, half a nanogram, against a 1.1263e9 kg design point: the classical vacuum corridor is right by 18.3 orders of magnitude"),
 ("QUANTUM-DEFOCUSES", 0, -1,  0, "corridor.py",
  "where the quantum corridor does apply its Unruh T_kk is NEGATIVE throughout, growing toward the horizon, so it DEFOCUSES: it would hurt the seat and help the lead. Recorded, not pursued"),
 # M found the scope error: the Unruh dismissal needs a horizon.
 ("UNRUH-NEEDS-HORIZON", 0, -1, +1, "corridor.py",
  "the 18-order dismissal used APT's Hawking flux, which requires a HORIZON; a two-region concentric device is horizonless and has no Unruh state, so the number does not transfer to it"),
 ("CASIMIR-ROUTE",   +1, +1, +1, "corridor.py",
  "the right term for a horizonless device is boundary-induced, rho = -pi^2 hbar c/720 d^4, and it meets the seating threshold only at 0.132 PLANCK LENGTHS -- sub-Planckian, still 57x short at l_P itself"),
 ("TWO-ROUTES-AGREE",+1, +1, +1, "corridor.py",
  "Casimir mass-equivalent at l_P is 2.9834e-10 kg against the Unruh crossover 5.3293e-10 kg -- two unrelated quantum estimates within a factor of 1.79, so the Planck-scale verdict is robust to which vacuum you invoke"),
 ("DEVICE-IS-CLASSICAL",+1,+1,+1, "corridor.py",
  "consequence: the two-region concentric device is a purely classical problem at any engineering scale, and composite.py's validated pipeline handles it with no quantum term added"),
 # The two-region device, built and measured.  The last structural item.
 ("ZERO-ADM-DEVICE",+1, +1, +1, "concentric.py",
  "a compact NEGATIVE core inside a POSITIVE shell of equal magnitude: the monopoles cancel so M_ADM = 0 EXACTLY, and the positive mass theorem has no objection to the configuration"),
 ("DEVICE-SEATS-LEADS",+1,-1,+1, "concentric.py",
  "MEASURED AND THEN WITHDRAWN AS A GLOBAL CLAIM: the seating stands (conjugate point 228.45 +- 0.04 over a sixfold refinement) but the LEAD was measured with both endpoints INSIDE the shell at R_s = 200, where the metric is not asymptotically flat. Push them out and the sign reverses at X ~ 277. It survives as a bounded short-range statement, 200 < X < 277, and as nothing wider"),
 ("THEOREM-IS-FREE", +1, +1, +1, "concentric.py",
  "respecting the positive mass theorem costs almost nothing: shell delay/core advance ~ (L/R_s)/(2 ln(L/a)) = 8%, because the core's advance carries a logarithm of its compactness and the shell's delay does not"),
 ("SHELL-THEOREM-SPLIT",+1,+1,+1, "concentric.py",
  "Newton's shell theorem does the division of labour: the shell contributes to g_tt and NOTHING to the tidal field, so all focusing is the core's Weyl term and the shell is pure delay"),
 ("VACUUM-NEEDS-COMPACT", 0, 0, +1, "concentric.py",
  "the corridor is vacuum only if the core is compact against the impact parameter: trace ratio 3.99e-1 at b/a = 2 against 7.55e-4 at b/a = 50. A design constraint, not a numerical detail"),
 ("HARNESS-NOT-SKETCH", 0, -1, +1, "concentric.py",
  "the first window was measured with a scratch driver that silently reset the potential to its own defaults, reporting a five-times-narrower window and a lead two orders too small. WITHDRAWN. Run the instrument, not the sketch"),
 # Does the device hold together?  The shell, asked the way that killed the last one.
 ("SHELL-IS-ORDINARY",+1,+1,+1, "stability.py",
  "Israel junction with M_in = -m and M_out = 0 gives sigma > 0 and a small tension, and the DOMINANT energy condition holds at every compactness to m/R = 2: all the exoticism is in the core"),
 ("STABLE-FOR-FREE", +1, +1, +1, "stability.py",
  "V'' > 0 at beta^2 = 0 and beta2_crit NEGATIVE everywhere measured, so the shell is radially stable with no pressure response at all -- where the textbook shell on the same machinery comes out unstable"),
 ("SIGN-STRUCTURE-3",+1, +1, +1, "stability.py",
  "third appearance of one sign flip: Weyl focusing without positive energy, a lead instead of a lag, and now a reversed potential curvature. V''(ordinary) = -3.036e-2 against V''(device) = +2.965e-2, mirror images"),
 ("CORE-NEUTRAL",     0,  0, +1, "stability.py",
  "Newton's shell theorem makes the field vanish at EVERY interior point, so the core feels no force wherever it sits: its position is neutrally stable, recorded as neither stable nor unstable"),
 ("L2-IS-THE-RISK",   0, -1,  0, "stability.py",
  "l >= 2 is NOT RUN and it is what killed the warpshell. PSP's shells have M_in >= 0 and M_out > 0 where ours has M_in < 0 and M_out = 0, and the radial mode already flipped under that exchange -- a reason to expect, never to assume"),
 # The core, specified.  M's identification phase gets a target.
 ("CORE-IS-TYPE-I", +1, +1, +1, "core.py",
  "MEASURED: |Im|/||T|| of 1e-7 to 1e-8 at every radius. Static and spherically symmetric forces Type I as MMV require, so THE TYPE IV PROBLEM DOES NOT TRANSFER to this architecture"),
 ("NO-BUCHDAHL",    +1, +1, +1, "core.py",
  "negative mass has no compactness bound: 1-2M r^2/R^3 = 1+2|M|r^2/R^3 > 1 everywhere, so the central pressure never diverges -- finite at 2|M|/R = 8378, which is what a core needing b/a >~ 50 requires"),
 ("PRESSURE-CAPPED",+1, +1, +1, "core.py",
  "p > 0 throughout, zero at the surface, and p(0)/|rho| rises monotonically to 1/3 FROM BELOW -- the radiation value, approached and never exceeded"),
 ("ONE-SIGN-EXOTIC",+1, +1, +1, "core.py",
  "all four energy conditions fail and all fail for the SAME reason: rho < 0. Flip that sign and DEC holds. Isotropic, Type I, pressures ordinary -- the identification target is one sign and nothing else"),
 ("CORE-IS-STRONG-FIELD", 0, -1, +1, "core.py",
  "concentric.py's metric CANNOT describe its own core: Phi_max = m/a is 0.25 to 1.0 across the window and the linearised spatial metric flips sign at 1. The corridor is fine; the core needed an exact solution"),
 # M's coordinate discipline applied, and the material census it prompted.
 ("LOG-COORDINATE",  +1, +1, +1, "core.py",
  "section 9's practice -- replace a multiplicative quantity by its additive coordinate -- applied: Phi = (1/2)ln(-g_tt) IS a logarithm, e^{2Phi} never changes sign, and the flip at Phi=1 was the TRUNCATION"),
 ("LIMIT-DISSOLVES", +1, +1, +1, "core.py",
  "re-run on the exponential completion the device is identical to four figures -- conj 228.5, delay -8.4240e-2 against -8.4239e-2 -- because the rays live where Phi ~ 0.02 and the metrics differ at O(Phi^2)"),
 ("MAGNITUDE-REACHED",+1,+1, +1, "core.py",
  "nuclear saturation EXCEEDS the universal seating threshold beyond ~100 km, by 2.175x there and 218x at 1000 km: the density scale is one nature already builds, in neutron stars"),
 ("SIGN-NOT-PHASE",   0, -1, +1, "core.py",
  "and no phase change reaches it: rho c^2 is dominated by rest mass, positive in every solid, liquid, plasma and degenerate state. Mercury and lead fall 13 orders short AND have the wrong sign"),
 ("VACUUM-NOT-MATERIAL",+1,+1,+1, "core.py",
  "negative energy density occurs relative to a VACUUM ground state -- Casimir, squeezed vacuum, Hawking flux -- so the identification phase is a vacuum-state problem wearing a materials name"),
 # M demanded an achievable core.  There is none, and the gap is a theorem.
 ("NO-ACHIEVABLE-CORE",+1,-1,-1, "achievable.py",
  "every known negative energy density obeys Ford-Roman |rho| <~ hbar c/L^4, and the core needs 65 ORDERS more at metre scale: available/required = 1.09e-65"),
 ("GAP-WIDENS",     +1, -1, -1, "achievable.py",
  "required falls as 1/b^2 and available as 1/b^4, so GOING BIGGER LOSES BY TWO POWERS -- closing the escape seatindex.py's 1/l saving and concentric.py's far shell both used"),
 ("PLANCK-THIRD-TIME",+1,+1, +1, "achievable.py",
  "the curves cross at a core size of 4.09 PLANCK LENGTHS -- a third independent route to the Planck scale after corridor.py's Unruh and Casimir crossings, about a different object"),
 ("NOT-EXCEPTIONS",  0,  0, +1, "achievable.py",
  "dark energy has negative PRESSURE and positive energy density; effective negative mass in BECs and metamaterials is a dispersion curvature, not T_00, and does not gravitate. Named so they are not reached for later"),
 ("DEVICE-NOT-RETRACTED",+1,+1,+1, "achievable.py",
  "the device stands: seats and leads, M_ADM = 0, ordinary stable shell, Type I core. What is settled is that the CORE is not buildable with known physics, and that this is a theorem and not a budget"),
 # M's charge state: it supplies the seat and not the lead.
 ("CHARGE-NO-LEAD",  +1, -1, -1, "charge.py",
  "Phi > 0 iff r < Q^2/2M and the horizon is at M + sqrt(M^2-Q^2): the positive-potential region is INSIDE THE HORIZON at every charge, and Q <= M is the Einstein-Maxwell positive energy theorem"),
 ("CHARGE-REDUCES",   0,  0, +1, "charge.py",
  "what charge does buy is a REDUCTION of the delay, never a reversal: 25% at r=2M, 10% at 5M, 5% at 10M, 0.5% at 100M, with Phi negative throughout"),
 ("EM-IS-ORDINARY",  +1, +1, +1, "charge.py",
  "electromagnetic stress-energy has rho = E^2/8pi > 0, p_r = -rho, p_t = +rho, so NEC WEC and DEC all hold and T_kk >= 0 gives RICCI focusing with positive energy"),
 ("MAGNETAR-SEATS",   0, -1, +1, "charge.py",
  "WITHDRAWN by spec.py: a dipole falls as r^-3, so the field is not at that range. The SIGN argument survives -- EM is ordinary, T_kk >= 0, Ricci focusing with positive energy"),
 ("THE-SPLIT",       +1, +1, +1, "charge.py",
  "the device divides along the energy-condition line -- part 2's turn needs T_kk > 0 and is ACHIEVABLE with ordinary EM; parts 1 and 3's lead needs Phi > 0 and is forbidden by two independent theorems"),
 # M's scoping: drop the lead, keep the seat.  The spec becomes achievable.
 ("SCOPE-DROPS-LEAD",+1, +1, +1, "spec.py",
  "M's correction -- the matter must exist at both ends under the same physics, nothing more -- removes the requirement every blocking theorem was attached to. Olum, Ford-Roman and Q<=M all forbid a LEAD that is no longer asked for"),
 ("ONE-INVARIANT",   0, -1, +1, "spec.py",
  "WITHDRAWN AS A SPECIFICATION: B*l = 1.5456e19 T m is arithmetically right and describes a region inside its own Schwarzschild radius by 2 pi^2/3. Kept executable so the retraction is checkable"),
 ("CROSS-ROUTE",    +1,  0, +1, "spec.py",
  "verified by a route sharing no formula: q = (4 pi G/c^4)T_kk gives pi/sqrt(q) = 1.5456e8 m at B = 1e11 T, and seatindex.py's threshold gives the same"),
 ("GAP-IS-ENGINEERING", 0,-1,+1, "spec.py",
  "WITHDRAWN: the magnetar comparison used a dipole's PEAK against a length it does not sustain -- 2.9e2 Pa against 4.0e27 Pa at 1.55e8 m, short by 25 orders. A magnetar does not seat"),
 ("KERR-HALTED",     0, -1,  0, "spec.py",
  "Kerr-Newman metric built and validated (a=0 gives Schwarzschild exactly, ergosphere at x=sqrt(4+a^2)) then HALTED by scoping when the integrator hit the ring: it was a hunt for a lead. NOT-RUN with a reason, and the one untested door if the lead reopens"),
 # The retraction, and the theorem it turned up.
 ("STURM-IMPLIES-COLLAPSE",+1,-1,+1, "spec.py",
  "any region satisfying the universal seating condition is inside its own Schwarzschild radius by exactly 2 pi^2/3 = 6.579, CONSTANT at every scale from 1 m to 1e11 m: the Sturm route describes a black hole, not a device"),
 ("PEAK-NOT-SUSTAINED", 0, -1, +1, "spec.py",
  "the magnetar claim compared a dipole's PEAK energy density against the threshold for a length it does not sustain -- r^-3 falloff gives 2.9e2 Pa where 4.0e27 Pa was needed. WITHDRAWN in spec.py and charge.py"),
 ("LENSING-IS-THE-SEAT",+1,+1,+1, "spec.py",
  "what composite.py actually measured is CUMULATIVE weak-field lensing, f = b^2 c^2/(4 G M), validated against the solar gravitational lens at 547.6 AU where the published focus is ~550"),
 ("SEAT-IS-NOT-NEW",   0, -1, +1, "spec.py",
  "so the seat is gravitational lensing, ordinary and known since 1919, and the Sun already does it. What is new is the sign structure, the split, reversal invariance, the achronality anti-correlation and the 65-order gap -- none of it a warp drive"),
 # M's reframing: measured in the right quantity, and three negatives verified.
 ("PROPER-IS-THE-QUANTITY",+1,+1,+1, "transition.py",
  "the warp quantity is PROPER DISTANCE, INT e^{-Phi} dl, not arrival time INT e^{-2Phi} dl. Not a faster trip, a SHORTER one -- and only the second was ever measured before"),
 ("LENS-HAS-WRONG-SIGN", 0, -1, +1, "transition.py",
  "a gravitational lens STRETCHES proper distance -- 1.000763 against a negative source's 0.999342 -- so it focuses AND lengthens. It is not a weak version of this concept but the opposite one"),
 ("NO-THROAT",         +1, +1, +1, "transition.py",
  "the areal radius R = r e^{-Phi} is MONOTONE at every radius (dR/dr from 0.482 to 1.0001), so there is no throat, no second asymptotic region, and the topology is R^3"),
 ("NO-HORIZON",        +1, +1, +1, "transition.py",
  "g_tt = -e^{2Phi} < 0 everywhere with Phi bounded by m/a = 1.0 and POSITIVE -- the opposite sign from the deep negative potential a horizon needs. Not a black hole, at any radius"),
 ("NO-MOMENTUM-FLUX",  +1, +1, +1, "transition.py",
  "T^0i = 0 EXACTLY from the Einstein tensor at every radius: no thrust, no exhaust, no reaction mass. warpshell.py's CM theorem and Doppler-cubed budget belong to a different architecture"),
 # Where the math stands, what the device must be, and how it is powered.
 ("CONTRACTION-LAW", +1, +1, +1, "budget.py",
  "eps = (2m/L) asinh(L/2b) less the shell's constant, validated against the measured contraction to better than 1.2% at three masses: the design law in closed form"),
 ("COST-IS-ONE-NUMBER",+1,+1,+1, "budget.py",
  "|M| = (c^2/G) L eps/(2 asinh(L/2b)), and c^2/G = 1.3466e27 kg per metre is the whole cost story -- every requirement in this project reduces to that conversion"),
 ("SUBLINEAR-SCALING",+1,  0, +1, "budget.py",
  "the scaling is L/ln(L/b), not linear: doubling the path costs 1.9417x, a 3% logarithmic economy of scale. An earlier draft asserted linearity and was wrong"),
 ("NOT-POWERED",     +1, +1, +1, "budget.py",
  "the configuration is STATIC with T^0i = 0 exactly, so it does no work and consumes nothing to persist; and M_ADM = 0 makes its total energy zero, so it is not expensive to build either"),
 ("SIGN-NOT-POWER",  +1, -1, +1, "budget.py",
  "the device is SIGN-LIMITED, NOT POWER-LIMITED: it is impossible to build rather than expensive, and those are different failures. No amount of power produces a negative energy density"),
 # M's entanglement instinct, tested.  It changes the number by 64 orders.
 ("ENTANGLEMENT-IS-IT",+1,+1,+1, "entangle.py",
  "M is right: negative energy density IS an entanglement phenomenon and there is no other kind. QNEC states the requirement exactly -- <T_kk> >= (hbar c/2pi)S'', so it needs entropy CONCAVE along the ray"),
 ("TWENTY-NOT-65-ORDERS",+1,+1,+1, "entangle.py",
  "in entanglement language the requirement is 2 pi^2 = 19.74x the HOLOGRAPHIC bound, constant at every scale -- not the 1e65 of Ford-Roman. The two gaps differ by 63.7 orders and measure different things"),
 ("TWO-CONSTANTS-AGREE",+1,+1,+1, "entangle.py",
  "cross-checked against spec.py's collapse factor 2 pi^2/3 = 6.5797, derived from gravitational collapse rather than entropy: the two differ by EXACTLY 3"),
 ("PRINCIPLED-VS-BUILDABLE",+1,+1,+1, "entangle.py",
  "so there are two gaps: 20x against what physics PERMITS, 1e65 against what can be MADE. The first is the meaningful one and it is far smaller than this project thought"),
 ("NO-CHARGE-LOOPHOLE", 0, -1, +1, "entangle.py",
  "but QNEC is STATE-INDEPENDENT -- it holds for every state, entangled or not, charged or not, and charge appears nowhere in it. And Gao-Jafferis-Wall's traversable wormhole, which does use entanglement, is SLOWER than the outside route"),
 # GJW read properly.  Their escape mechanism is one achronal.py could not find.
 ("EXTERNAL-PATH-ESCAPE",+1,+1,+1, "gjw.py",
  "GJW break achronality by ADDING AN EXTERNAL CAUSAL PATH -- coupling the boundaries changes the chronology relation itself. achronal.py proved you cannot break it through the MATTER; this is not a matter-side escape at all, and it is the only known way past Graham-Olum"),
 ("BANK-LOAN-THEOREM", +1, -1, -1, "gjw.py",
  "and the same move forbids faster: traversability requires non-achronality, non-achronality requires an existing outside causal path, so you could have gone that way. GJW's own words -- a loan you can only get if you are rich enough not to need it"),
 ("GJW-FLAT-COST",    +1,  0, +1, "gjw.py",
  "their flat-space version is left as a remark; quantified it needs amplification 4.387e71 * D^2, RISING as D^2 exactly over six decades, so bigger separation is HARDER"),
 ("PLANCK-FOURTH-TIME",+1,+1,+1, "gjw.py",
  "and that gain reaches unity at 0.0934 PLANCK LENGTHS -- a fourth independent route to the Planck scale after corridor.py's two and achievable.py's one, about a different geometry again"),
 ("GJW-IS-EXISTENCE-PROOF",+1,+1,+1, "gjw.py",
  "under M's scoping, where the lead is dropped, GJW is an EXISTENCE PROOF: a traversable connection from entanglement plus a coupling, no exotic matter postulated, the negative energy DERIVED. UV-complete and published"),
 # M's structure: binary -> hierarchy -> binary.  I had not been writing it.
 ("ANALYSIS-ALL-ALONG", 0, -1, +1, "expand.py",
  "every headline number this project produced -- 65 orders, 2 pi^2, 4.387e71 D^2 -- is an ANALYSIS answer, a magnitude, and by register 1173 analysis earns NO ROW because logic cannot get a binary back from it"),
 ("THREE-ROWS-ADMIT",  +1, +1, +1, "expand.py",
  "expanded properly: ORDER admits (GJW's external causal path), GEOMETRY admits (no throat, no horizon, M_ADM=0), ALGEBRA admits (junction closes, DEC holds, stable at beta^2=0). Three of four"),
 ("DISSENT-IS-VALUE",  +1, +1, +1, "expand.py",
  "the single dissent is INFORMATION, and by section 33.2 the identity of the dissenting language names the kind of object: one missing a VALUE, not a STRUCTURE"),
 ("NOTHING-STRUCTURAL",+1, +1, +1, "expand.py",
  "so nothing structural stands against faster or cheaper -- speed is an order question and order admits, cost is an algebra question and algebra admits. NOT permission to ignore the magnitude, which is measured and real"),
 ("ORDER-MOVED",       +1, +1, +1, "expand.py",
  "and ORDER moved this session from refusal to admission on GJW's external path. Before pass 27 the expansion stood at TWO refusals. It moved the row that governs SPEED -- the only structural change this project has made to that question"),
 # Pushing the ORDER row: the escape, its closure, and the one open door.
 ("TIMESCALES-INDEPENDENT",+1,0,+1, "amortize.py",
  "GJW's traversal window scales with the MOUTH size R while the benefit scales with the SEPARATION D -- independent parameters. For a 1 m mouth at a light-year the window is 8.5e-15 of the ambient crossing"),
 ("AMORTISATION-CLOSED", 0, -1, +1, "amortize.py",
  "deploy once and transit N times would give advantage from N=10 -- but GJW's own sentence closes it: in flat space the coupling is carried by ambient propagation 'EXCEPT WITH A TIME DELAY', so it is per-use with nothing to amortise"),
 ("STANDING-COUPLING",  +1, +1, +1, "amortize.py",
  "their footnote 2 declines the TIME-INDEPENDENT interaction to keep the state regular on the past horizon -- a stated technical reason, not a failure. A standing channel is exactly what amortisation needs and exactly what nobody has tested"),
 ("ONE-DOOR",            0,  0, +1, "amortize.py",
  "so the ORDER row is not open everywhere: it is open at ONE point, named in the source with the authors' own reason for not opening it. Narrow, real, and untested by anyone"),
 # Pass 30 -- space and time as ONE index, M's four claims, each measured.
 ("SPACE-TIME-ONE",    +1, +1, +1, "unified.py",
  "space and time are ONE quantity, measured: the two savings share a sign at every Phi tested, positive and negative, and their ratio is 2.000 throughout -- e^{-Phi} for proper distance against e^{-2Phi} for light time. One Phi moves both, never separately"),
 ("TIME-CHEAPER-METRIC",+1, +1, +1, "unified.py",
  "and in the METRIC register time is CHEAPER by exactly two: Phi = eps buys a fractional space saving, Phi = eps/2 buys the same fractional time saving. Half the source for the same gain -- the opposite of the intuition that time costs more"),
 ("REGISTER-INVERSION",  0, -1, +1, "unified.py",
  "but in the CAUSAL register the ordering inverts and is severe: a spatial shortcut is not forbidden as such, a temporal displacement is, and the INTERSECTION is the Morris-Thorne-Yurtsever time machine. The cheap one to build is the forbidden one to use"),
 ("PAID-IN-ADVANCE",     0, +1, +1, "unified.py",
  "GJW pay in advance literally: their coupling breaks the H_L - H_R Killing symmetry and so 'fixes the relative time coordinate between them, excluding the possibility of having closed time-like curves'. Causal consistency bought at the moment of coupling, and what it costs is the intersection"),
 ("CHAIN-COSTS-MORE",    0, -1, +1, "unified.py",
  "collection in transit measured FALSE: the same total mass spread over N static sources gives 1.000 / 0.976 / 0.954 / 0.950 of one concentrated source at N = 1/2/10/50. Splitting the path shortens every span and eps goes as asinh(L/2b), so the logarithm punishes it. Deferral to seating is NOT-RUN"),
 ("EIGHT-IS-A-COUNT",    0,  0, +1, "unified.py",
  "the device really does take eight free parameters -- m, a, b, R_s, L, A, B, beta^2 -- two of them the endpoints transit.py gates on. EIGHT IS THE COUNT AND NOTHING MORE: Lambda_8's eight are physical quantities under seven Heaviside constraints, these are device parameters, and no correspondence is asserted"),
 # Pass 31 -- MTY taken apart, and a withdrawal found on the way in.
 ("LEAD-IS-INTERIOR",  +1, -1, +1, "chronology.py",
  "THE WITHDRAWAL: concentric.py ran every ray from -150 to +150 with the shell at R_s = 200, so BOTH ENDPOINTS SAT INSIDE IT. There 't - |dx|' compares a coordinate time against a coordinate distance in a region that is not asymptotically flat, which is not a statement about causal structure at all. Outside the shell the sign reverses"),
 ("GAIN-SATURATES",    +1, -1, +1, "chronology.py",
  "and the reason is what M_ADM = 0 is FOR: cancelling the monopole makes the Shapiro gain CONVERGE. Measured by quadrature, -3.969054e-01 at X = 400 and the same five digits at X = 20000. Closed form 4m[ln(2R_s/sqrt(b^2+a^2)) - 1], which contains no baseline, agreeing to 0.15% at m = 5e-3"),
 ("LOG-AGAINST-LINEAR",+1, -1, +1, "chronology.py",
  "THE GENERAL RESULT, and it is not about this device: in the weak field a negative Shapiro term buys time at most LOGARITHMICALLY in the baseline while the deflection it necessarily produces costs path length LINEARLY, so every configuration crosses over exactly once. The device crosses at ~250, a BARE negative mass at ~324 -- the same order. The shell does not cause the failure; it moves the crossing in"),
 ("CROSSOVER-RANGE",    0, -1, +1, "chronology.py",
  "X_c = b^2[ln(2R_s/sqrt(b^2+a^2)) - 1]/m predicts 249.6 against a measured crossover near 277, and the bare-mass form ln(2X/b) = mX/b^2 predicts 324 against a measured 350. Two independent configurations, both within 11% of a two-term model"),
 ("NARROW-WINDOW",      0, -1, +1, "chronology.py",
  "so the window where the advance is BOTH unambiguous and positive is bounded at both ends -- 200 < X < 277, a factor of 1.39 in baseline -- and the best fractional advance inside it is 2.297e-4, at the near edge"),
 ("SAVING-DOESNT-SCALE",+1, -1, +1, "chronology.py",
  "AND THIS IS THE ANSWER TO 'FASTER': the saving is a fixed offset that does not grow with the journey, so as a fraction of the trip it dies like 1/L -- 7.92e-9 of a four-light-year crossing. A saving that does not scale with the journey is not a faster journey"),
 ("SECOND-COSTS-1E4-SUNS",+1,-1,+1, "chronology.py",
  "priced: one second of saving needs a geometric mass of 1.502e7 m, which is 2.022e34 kg, TEN THOUSAND SOLAR MASSES of negative mass -- and buys that same one second whether the trip is a metre or a thousand light years"),
 ("MTY-CLOSED",         0, +1, +1, "chronology.py",
  "the Morris-Thorne-Yurtsever construction is NOT available to this device, and it fails on STRUCTURE rather than magnitude: MTY needs a persistent identification of two ends, transition.py measures the areal radius monotone at every radius, so there is no throat and there are not two ends to identify"),
 ("GAMMA-CRIT",         0, -1, +1, "chronology.py",
  "but the Everett / Shoshany-Snodgrass route needs no identification -- two devices and a boost. Their eq. (3.11) reduces exactly to gamma > 1/eps, and at the best unambiguous advance that is gamma > 4354: FINITE, below the LHC's proton gamma, and not a prohibition. The device is not protected by chronology, it is protected by not working at range"),
 ("WRONG-MACHINE",      0,  0, +1, "chronology.py",
  "unified.py named Morris-Thorne-Yurtsever and that was an assertion, not a measurement. Right conclusion -- the intersection is a time machine -- wrong machine, and the correction is struck in place there"),
 # PHASE 1 -- the transition defined and proved.  A consolidation, not a pass.
 ("TRANSITION-DEFINED", +1, +1, +1, "phase1.py",
  "D1-D5, every condition checkable: endpoints are LABELS not worldlines, compact support, the proper distance falls, T^{0i} = 0, and both endpoints declared at onset. A construction violating D4 is PROPULSION and out of scope -- which excludes Alcubierre's shift by construction rather than by argument"),
 ("STATIC-IS-THE-SPLIT",+1, +1, +1, "phase1.py",
  "and the static/dynamic split IS the transition/propulsion split, exactly: T^{0i} = 0 is AUTOMATIC for any static metric and IMPOSSIBLE with a shift vector. D4 is not an extra assumption on the construction, it is a consequence of staticity"),
 ("PROPER-IS-THE-ACT",  +1, +1, +1, "phase1.py",
  "THEOREM 1: a payload at rest measures int e^{-Phi} dl, and light measures int e^{-2Phi} dl -- ratio exactly 2, measured. A transition acts on the FIRST, so chronology.py's LATE verdict is an answer about the second and does not touch it"),
 ("NEVER-A-LEAD",        0, -1, +1, "phase1.py",
  "THEOREM 4, computed rather than asserted: a compactly supported metric change is causal, so a corridor of length L is not complete before L/2c, and one establishment plus one traversal costs 1.5 L/c against a signal's L/c. A SINGLE TRANSITION IS 50% WORSE THAN SENDING THE SIGNAL"),
 ("VALUE-IS-AMORTISED", +1, +1, +1, "phase1.py",
  "THEOREM 5: so all the value is in amortisation, and THIS is where GJW's closure does not apply. Their coupling is per-use by their own 'except with a time delay'; a static shape is not a signal, it holds itself (not powered, radially stable) and the establishment share falls as L/2Nc"),
 ("TRANSITION-EQUATION",+1, +1, +1, "phase1.py",
  "THE EQUATION: Delta d = (G/c^2) M Lambda with Lambda = 2[ln(2R_s/b) - 1] = 9.9825. Contraction SATURATES (identical to nine digits over a fiftyfold baseline), is LINEAR in mass (9.975 to 9.864 per unit m over sixteenfold), and closed form agrees with measurement to 0.08%"),
 ("NO-GEOMETRY-LEFT",   +1, -1, +1, "phase1.py",
  "and there is no free parameter remaining: Lambda improves only LOGARITHMICALLY, so reaching Lambda = 20 needs R_s/b = 2.99e4 and Lambda = 100 needs 7.05e21. The contraction is proportional to mass with a coefficient fixed by c^2/G and a logarithm, and nothing in the geometry is left to optimise"),
 ("EXCHANGE-RATE",      +1, -1, +1, "phase1.py",
  "THE PRICE: 1.349e26 kg per metre contracted. One solar mass buys 14.7 km; one percent off Alpha Centauri is 2.57e10 solar masses; half of it is 1.28e12. A galaxy of negative mass to shave one percent, and it is not improvable by cleverness in this architecture"),
 ("ONLY-ENTRY",          0, -1, +1, "phase1.py",
  "the ranking on 'fastest operator, lowest cost' returns ONE candidate -- the static concentric corridor -- and it wins by being the only entry that is both reusable and permitted. GJW is per-use, Alcubierre fails D4, charge gives zero contraction, Casimir is 4.39e71 short, and a bare negative mass is strictly better physics and forbidden. A weak kind of winning, stated as the weak kind"),
 ("PHASE-1-CLOSES",     +1, -1, +1, "phase1.py",
  "PHASE 1 IS FINISHED AS MATHEMATICS. The transition is defined, is not propulsion, is not forbidden, is never a lead, is worth only what amortisation makes it worth, and costs 1.349e26 kg/m. What remains needs M < 0 and is not a mathematics problem"),
 # supply.py -- converting the cost into something suppliable.
 ("CONVERSION-IS-DONE", +1, -1, +1, "supply.py",
  "G/c^4 = (G/c^2)/c^2, so E = mc^2 is NOT something applied to the transition equation -- it is already inside the coupling. Paying in joules rather than kilograms is the same bill in another currency at a rate already applied: 1.2124e43 J per metre, which is 22.6 EARTH MASS-ENERGIES PER METRE"),
 ("STIFFNESS-IS-THE-COST",+1,-1,+1, "supply.py",
  "and c^4/G = 1.21026e44 N is the ONLY constant in the cost. The whole price of this project is one sentence: spacetime is stiff to the tune of 1.2e44 newtons. The supply form changes the LOGISTICS and not the magnitude, because G_munu = 8 pi T_munu does not ask where T came from"),
 ("SIGN-IS-THE-ONLY-QUESTION",+1,+1,+1,"supply.py",
  "so the only thing worth asking a supply route is whether it supplies the SIGN. Four routes exist -- classical fields, charge, binding, quantum vacuum -- and exactly ONE does. The other three are bounded by the SAME theorem, the positive mass theorem; the fourth is bounded by hbar instead"),
 ("POWER-MAKES-IT-WORSE",+1,-1,+1, "supply.py",
  "MEASURED: the Casimir density depends on the GAP and on no applied field, while an applied field contributes POSITIVELY as its square. At a 10 nm gap the field that CANCELS the Casimir dip is 9.894e7 V/m -- BELOW the dielectric breakdown of a solid, and 1.01e6 times below a focused laser. Charge manipulation destroys the only negative energy present before the apparatus even breaks down"),
 ("CHARGE-WRONG-SIDE",   0, -1, +1, "supply.py",
  "and charge cannot supply the sign for two independent reasons: Q <= M by the Einstein-Maxwell positive energy theorem, and charge.py's Phi > 0 region is hidden inside the horizon at every Q. Charge is on the RIGHT side of the seat and the WRONG side of the sign"),
 ("BINDING-BOUNDED",     0, -1, +1, "supply.py",
  "binding energy is genuinely negative and still cannot: 1e-9 chemical, 1e-2 nuclear, 0.42 for Kerr accretion, every one of them a FRACTION of a positive rest mass brought. The net stays positive, and that is the positive mass theorem restated rather than an accident of the examples"),
 ("EFFICIENCY-CANNOT",  +1, -1, +1, "supply.py",
  "and no conversion efficiency rescues it: against the world's annual energy production eta would have to exceed 1 by 36 orders -- more negative energy out than energy in. At a perfect eta = 1 the requirement is still 4.588e57 J, the mass-energy of 2.57e10 suns. EFFICIENCY IS NOT THE PROBLEM; c^4/G IS"),
 ("GAP-IS-THE-LEVER",   +1, -1, +1, "supply.py",
  "what is left is the GAP: the requirement for a fractional contraction falls as 1/b^2 while the Casimir density rises as 1/b^4, so the ratio closes -- 3.57e-69 at a metre, unity at b = 5.98e-35 m = 3.70 PLANCK LENGTHS"),
 ("THREE-CROSSINGS-AGREE",+1,+1,+1, "supply.py",
  "AND THREE INDEPENDENT QUANTITIES CROSS IN THE SAME PLACE: this contraction at 3.70 l_P, corridor.py's Casimir seat at 0.132 l_P, gjw.py's unity coupling separation at 0.0934 l_P. A contraction, a seat and a coupling, all within two orders of the Planck length, computed by three routes sharing no formula"),
 # scale.py -- following the Planck-crossing instinct, and deflating it.
 ("SCALE-THEOREM",     +1, +1, +1, "scale.py",
  "PROVED: the ratio of what the quantum vacuum supplies to what GR demands is kappa (l_P/L)^2 and can be nothing else, because hbar c/L^4 over c^4/GL^2 IS hbar G/c^3 L^2 and those are the only constants available. The crossing is at l_P by DIMENSIONAL NECESSITY -- l_P is defined as where the two meet"),
 ("THEOREM-REPRODUCES",+1, +1, +1, "scale.py",
  "and it is not hand-waving: kappa = pi/360 in closed form predicts gjw.py's gain_coefficient 4.3866e71 and its unity separation 1.5098e-36 m TO FIVE DIGITS, and gjw.py computes both from the Casimir formula sharing no algebra. achievable.py's kappa is measured IDENTICAL TO SIX DIGITS across six decades of length, which is the theorem's signature"),
 ("OUTLIER-RECONCILES", 0,  0, +1, "scale.py",
  "the census reads 0.0934, 0.1320, 3.7013 and 204.67 l_P -- but achievable.py's length is the CORRIDOR RADIUS while the others measure the gap carrying the energy, and its core sits at a/b = 0.02, giving 4.0933 l_P, which that file already prints itself. On the energy-carrying scale all four lie between 0.093 and 4.09 l_P, a factor of 44"),
 ("ONE-OBSTACLE",      +1, -1, +1, "scale.py",
  "SO THE PROJECT'S OBSTACLES UNIFY: 65 orders, 69 orders and 71 orders are not three findings but (L/l_P)^2 divided by three prefactors at three lengths. ONE OBSTACLE COUNTED THREE TIMES, and the identity is checked rather than asserted"),
 ("KAPPA-IS-THE-ONLY-LEVER",+1,-1,+1,"scale.py",
  "and the shortfall is (1/kappa)(L/l_P)^2, so THE EXPONENT IS 2 AND THE BASE IS l_P AND NO MECHANISM CHANGES EITHER -- a mechanism changes only kappa, which is dimensionless and can be large only if the problem holds a large dimensionless number. The honest list has one entry worth two orders: N ~ 100 field species"),
 ("EXTRA-DIMENSIONS",   0,  0, +1, "scale.py",
  "the one lever that changes the BASE rather than kappa is a lower fundamental Planck scale: at the collider bound M_* ~ 3 TeV, l_* = 6.578e-20 m and the metre-scale shortfall falls from 3.83e69 to 2.31e38 -- 31.2 ORDERS FOR FREE AND STILL 38 SHORT. Whether the demand side rescales the same way in a braneworld is a different calculation in a different theory: NOT-RUN, named rather than guessed"),
 ("CROSSING-IS-NOT-A-TARGET",0,-1,+1,"scale.py",
  "THE REFUSAL, and it is the most important line: at the crossing FIVE independent approximations fail at once -- semiclassical gravity needs L >> l_P, Ford-Roman is derived on a FIXED background, geometric optics needs wavelength << curvature radius, the perfect-conductor Casimir formula needs a gap above a plasma wavelength, and every Phi expansion here assumes |Phi| << 1. The crossing is where the theory STOPS, reported in units of length, and may never be quoted as an engineering requirement"),
 ("NARROWER-CLOSING",  +1, -1, +1, "scale.py",
  "so the correct closing statement is narrower than 'you need Planck scale': EVERY ROUTE THIS PROJECT CAN EVALUATE REMAINS SHORT AT EVERY SCALE WHERE THE EVALUATION IS VALID, and the extrapolation to where it would not be short runs off the edge of the map"),
 # currency.py -- is there a cheaper currency?  Partly yes, and structurally.
 ("PLANCK-FACTOR-CANCELS",+1,+1,+1, "currency.py",
  "M'S INSTINCT IS RIGHT AND THE REASON IS STRUCTURAL: every ENERGY comparison carries hbar G/c^3 exactly once and uncancelled, which IS the 65-to-71 orders. In the ENTROPY channel both sides carry (L/l_P)^2 -- QNEC gives S_req = (pi^2/2)(L/l_P)^2 and holography gives (1/4)(L/l_P)^2 -- so it CANCELS EXACTLY and the ratio is 2 pi^2 at every scale, measured scale-free across ten decades"),
 ("ENTROPY-IS-PLANCK-DENOMINATED",+1,+1,+1,"currency.py",
  "and the reason it cancels is that entropy is ALREADY denominated in Planck areas: the holographic bound measures S in units of l_P^2, so stating the requirement as an entropy automatically divides out the factor that kills every energy-denominated route. A real feature of the problem, not a hopeful estimate"),
 ("SEAT-VS-CONTRACTION", +1, +1, +1, "currency.py",
  "AND IT SEPARATES TWO THINGS THE PROJECT HAD FUSED: 2 pi^2 prices the SEAT, but phase1 defined the transition as a CONTRACTION, and a contraction costs 8 pi eps/Lambda of the holographic bound -- 2.518 at eps = 1, 1.007 at 0.4, 0.252 at 0.1. THE SEAT IS HOLOGRAPHICALLY FORBIDDEN AND THE CONTRACTION IS NOT, below eps = 0.397"),
 ("TWENTY-MEASURES-BADLY",0, -1, +1, "currency.py",
  "which corrects entangle.py in place: reading 2 pi^2 as 'the best news this project has produced' is too generous, because the holographic bound is the most entropy a region can hold BY ANY MEANS and exceeding it is impossible rather than twenty times hard. THE FACTOR MEASURES HOW BADLY, NOT HOW NEARLY"),
 ("PERMISSION-NOT-DISCOUNT",+1,-1,+1,"currency.py",
  "BUT THE CURRENCY BUYS PERMISSION, NOT DISCOUNT. Bekenstein's bound read backwards, E >= S hbar c/2 pi R, converts the seat's entropy requirement into (pi/4) L c^4/G = 9.5053e43 J at a metre -- EXACTLY seatindex.py's T_COEFF, by a route sharing no algebra. Changing denomination changes what can be SAID about the requirement and not what must be PAID, and that is a theorem"),
 ("THREE-ARE-ONE",       +1, -1, +1, "currency.py",
  "and three coincidences reconcile: entangle.py's 2 pi^2, spec.py's 2 pi^2/3, and 'the seating region is inside its own Schwarzschild radius'. They differ by EXACTLY 3, and the 3 is the 3 in M = (4/3) pi R^3 rho -- volume against area. All three say one thing: a region that seats a conjugate point is a black hole"),
 ("SHAPING-IS-NOT-RUN",   0,  0, +1, "currency.py",
  "and one question in this neighbourhood stays open honestly: Bekenstein bounds the entropy a region can HOLD given its energy, but whether a state can be PREPARED whose S'' is negative where wanted, at a cost below that floor, in a vacuum ALREADY carrying area-law entanglement, is a different question. NOT-RUN -- the only place a cheaper currency could still be hiding"),
 # shaping.py -- currency.py's last open door, pursued and CLOSED.
 ("VACUUM-SATURATES-QNEC",+1,+1,+1,"shaping.py",
  "the vacuum does not merely satisfy QNEC, IT SATURATES IT: T_kk = 0 and S'' = 0 together. So the vacuum is free, already optimal, and its optimum is ZERO -- and S'' < 0 means DISENTANGLING relative to the ground state, which every deviation from a ground state costs. The premise that an already-entangled vacuum offers its entanglement free is right about the entanglement and wrong about the direction: we need LESS, not more"),
 ("ZERO-POINT-IS-THE-FLOOR",+1,-1,+1,"shaping.py",
  "MEASURED: single-mode squeezed vacuum digs |rho_min|V = (hbar w/2)(1 - e^{-2r}), which SATURATES at exactly hbar w/2 -- the mode's own zero-point energy. Squeezing by e^10 costs 1.2129e8 quanta and buys the same 0.5 that r = 3 bought for 100. You cannot dig a hole in the vacuum deeper than what is in it"),
 ("COST-DOES-NOT-CLOSE-IT",+1,+1,+1,"shaping.py",
  "AND THE COST ARGUMENT FAILS, IN M'S FAVOUR: eta = (1-e^{-2r})/(2 sinh^2 r) -> 1/r, so weak squeezing over many modes drives the preparation cost per joule of negative energy TO ZERO, and no Bekenstein-style reasoning stops it. On cost alone the cheaper currency is real. This is reported rather than buried"),
 ("COUNTING-CLOSES-IT",  +1, -1, +1, "shaping.py",
  "what closes the door is COUNTING, not cost: holding rho < 0 across a length L needs a quarter-wavelength that spans it, capping w at pi c/2L; the cap limits modes to V w^3/6 pi^2 c^3; each yields at most hbar w/2. Together |rho|_max = 0.0514 hbar c/L^4, whatever is spent and however the state is prepared. A CHEAPER CURRENCY DOES NOT HELP WHEN THE THING BEING BOUGHT IS OUT OF STOCK"),
 ("FORD-ROMAN-DERIVED",  +1, +1, +1, "shaping.py",
  "AND THAT NUMBER IS FORD-ROMAN. This project quoted |rho| <~ hbar c/L^4 as an EXTERNAL bound for thirty passes; it is a consequence of zero-point saturation plus mode counting, the coefficient is pi^2/192 = 0.051404, measured scale-free across nine decades, and the Casimir configuration sits below it at pi^2/720 by exactly 3.75 -- as one particular boundary condition must sit below a bound over all of them"),
 ("SHAPING-CLOSED",       0, -1, +1, "shaping.py",
  "so currency.py's one NOT-RUN is CLOSED-NEGATIVE, struck in place there. The three-part answer to 'is there a cheaper currency' is finished: entropy IS a better denomination and the Planck factor cancels; Bekenstein fixes the rate so it buys permission not discount; and preparing the shape is cheap to attempt and leads nowhere. Still NOT-RUN and named: interacting fields, curved backgrounds, non-Gaussian states"),
 # smearing.py -- shaping.py's three NOT-RUNs audited, plus a new theorem.
 ("SNEC-INHERITS-ANEC", +1, -1, +1, "smearing.py",
  "NEW THEOREM: at large smearing the SNEC's left side tends to I/(w sqrt(2 pi)) and falls as 1/w while its bound falls as 1/w^2, so ANY ANEC-violating configuration fails SNEC above w_crit = B sqrt(2 pi)/|I|. SNEC IS NOT AN INDEPENDENT WEAKER CONDITION -- it is a finer statement that inherits ANEC's prohibition at large smearing, and cannot be slipped through"),
 ("W-CRIT",              0, -1, +1, "smearing.py",
  "measured on the static corridor: I = -2.46486e-06 gives a predicted w_crit = 1.0116e4, and the numerical scan crosses at exactly that width (LHS/RHS = 1.0000). This GENERALISES nullbound.py's withdrawal from the Alcubierre wall -- which phase1 excluded by D4 -- to every ANEC-violating configuration, the static corridor included"),
 ("ANEC-CROSS-CHECKED", +1, +1, +1, "smearing.py",
  "and it re-confirms achronal.py by a route sharing no algebra: achronal.py measured ANEC violation on 25 rays by integrating R_kk along geodesics, this file gets I < 0 from a closed-form line integral of the source density. Different computation, same sign"),
 ("NONGAUSSIAN-CLOSED",  0,  0, +1, "smearing.py",
  "NOT-RUN 1 CLOSED: shaping.py's mode-counting bound was derived over Gaussian states, which limits THAT derivation and not the conclusion -- QEIs and SNEC are STATE-INDEPENDENT theorems over all Hadamard states, as nullbound.py already records. A non-Gaussian state cannot evade a bound never conditioned on the state"),
 ("NONMINIMAL-CLOSED",   0, -1, +1, "smearing.py",
  "NOT-RUN 2 CLOSED CONDITIONALLY, and it was the live one: non-minimal coupling xi R phi^2 is the standard example of CLASSICAL energy-condition violation. Fliss, Freivogel, Kontou & Pardo Santos (arXiv:2309.10848) find ANEC obeyed both classically and in QFT under an EFT assumption, their section III.C titled 'Large negative null energies require large field values'. THE CONDITION IS THE EFT ASSUMPTION and is named, not buried"),
 ("SELF-CONSISTENT-OPEN",0,  0, +1, "smearing.py",
  "NOT-RUN 3 STAYS OPEN and is not new: QEIs are proved on FIXED curved backgrounds, but matter that curves the spacetime it is bounded in is not covered. That is obstruct.py's ANEC row, and the corpus's note that self-consistent achronal ANEC in 4D has been unproven for nineteen years"),
 ("ONE-NAME-AGAIN",     +1, -1, +1, "smearing.py",
  "SO THE OBSTACLE HAS ONE NAME AGAIN. SNEC was the last energy condition weak enough to look like a door and it closes whenever ANEC does; every route this project has evaluated is bounded by ANEC alone, and ANEC violation is precisely what the corridor requires and what achronal.py measured"),
 # anecscope.py -- the ANEC row, and a lemma in this tree that was inverted.
 ("SHEAR-CLAIM-INVERTED",+1, +1, +1, "anecscope.py",
  "achronal.py closed the achronality escape against us with SHEAR DROPPED, on the stated ground at its line 53 that dropping shear is conservative. THE DIRECTION IS INVERTED: shear helps focusing, focusing makes conjugate points sooner or where there were none, and a conjugate point is exactly what REMOVES achronality. Dropping shear understates focusing and therefore OVERSTATES achronality"),
 ("VACUUM-DEMONSTRATION",+1, +1, +1, "anecscope.py",
  "demonstrated rather than argued, in the cleanest case: in VACUUM R_kk = 0 exactly, achronal.py's lemma_applies() fires, and the scalar equation gives u = lambda with no zero ever -- while the full matrix finds a conjugate point at 56.50 (M = -2e-3) and 47.17 (M = -4e-3). The lemma T_kk <= 0 => no conjugate point is valid ONLY in the shear-free reduction, because Weyl is traceless and focuses one eigendirection whatever the sign of the source"),
 ("NO-ACHRONAL-VIOLATOR",+1, +1, +1, "anecscope.py",
  "and with that corrected, scanning impact parameter: ANEC violation ceases at b = 2.378288 (bisected) while conjugate points persist well past it, so the ANEC-VIOLATING SET IS STRICTLY CONTAINED IN THE NON-ACHRONAL SET. NO RAY OF THIS CORRIDOR IS BOTH ANEC-VIOLATING AND ACHRONAL, and the containment is nowhere marginal along the scan"),
 ("SEAT-IS-THE-ESCAPE",  +1, +1, +1, "anecscope.py",
  "and the containment is structural, not lucky: the same negative core that makes INTEGRAL T_kk dl negative is the thing that focuses, through Weyl, which is sign-blind. ONE OBJECT PRODUCES BOTH, so the seat and the escape cannot come apart. Where GJW make their geodesics non-achronal with an EXTERNAL causal path, the corridor does it with an INTERNAL conjugate point it already needed"),
 ("OUTSIDE-NOT-REFUTED",  0, -1, +1, "anecscope.py",
  "SO THE CORRIDOR IS OUTSIDE ACHRONAL ANEC'S SCOPE -- and that is a SCOPE finding, not a refutation. Self-consistent achronal ANEC stands exactly where it stood, unproven for nineteen years, and being outside a conjecture's reach is not defeating it. NOT ONE ORDER OF MAGNITUDE MOVED: c^4/G untouched, 1.349e26 kg/m untouched, rho < 0 still required"),
 ("ANEC-RELOCATES",      +1, -1, +1, "anecscope.py",
  "and the ledger changes rather than the physics: obstruct.py's ANEC row has been OPEN throughout and does NOT close, because ANEC violation is still required and still measured. It RELOCATES -- the requirement is no longer answerable by a prohibition, so it becomes a magnitude question like everything else. THE OBSTACLE STILL HAS ONE NAME AND IT IS NO LONGER ANEC: IT IS c^4/G"),
 # dichotomy.py -- "so we need a miniature contained black hole?"  No.
 ("BH-IS-WRONG-SIGN",   +1, +1, +1, "dichotomy.py",
  "a black hole is POSITIVE mass and positive mass STRETCHES proper distance, which phase1 proved is the quantity a transition acts on. Measured both ways at |Phi| = 8e-2: ordinary +M gives LONGER, negative -M gives SHORTER. A BLACK HOLE IS NOT A WEAK VERSION OF WHAT THIS NEEDS -- IT IS THE OPPOSITE SIGN AT MAXIMUM STRENGTH"),
 ("CONTAINMENT-IS-MOOT", 0,  0, +1, "dichotomy.py",
  "and 'contained' buys nothing: by Birkhoff the exterior of any spherically symmetric mass is Schwarzschild with that mass whatever the interior does, so a contained black hole and an uncontained one of equal mass curve the corridor identically"),
 ("COLLAPSE-BINDS-RICCI",+1, +1, +1, "dichotomy.py",
  "and the black-hole result prices the STURM seat, which is a RICCI statement: q l^2 >= pi^2 with q = 4 pi T_kk requires q > 0, positive energy, and seatindex's tkk_required is positive by construction. Our corridor's core T_kk is NEGATIVE -- it does not meet Sturm, is not trying to, and the collapse result does not reach it"),
 ("CORRIDOR-NOT-A-BH",  +1, +1, +1, "dichotomy.py",
  "MEASURED: the corridor seats a conjugate point at lambda = 165.36 with has_throat False, has_horizon False, and M_ADM residual -4.000e-15 -- zero to fifteen digits. It focuses through WEYL, quadratic and sign-blind, which carries no density requirement at all. It seats and it is not a black hole"),
 ("THE-DICHOTOMY",      +1, -1, +1, "dichotomy.py",
  "SO THERE ARE TWO ROUTES WITH TWO DIFFERENT BLOCKERS, and this is the cleanest structure the project has. RICCI: ordinary matter, needs the Sturm density, exceeds collapse by 2 pi^2/3 at every scale, closes inside its own Schwarzschild radius -- BLOCKED BY COLLAPSE, and on that route 'you need a black hole' is true as a PROHIBITION rather than a recipe. WEYL: negative mass, no density requirement, no horizon, M_ADM = 0 -- BLOCKED BY THE SOURCE. A collapse problem exchanged for a source problem, and this project is on the second"),
 ("ONE-STATEMENT-FIXED", 0,  0, +1, "dichotomy.py",
  "and the question forced a correction: currency.py asserted flatly that 'a region that seats a conjugate point is a black hole', and OUR OWN CORRIDOR IS THE COUNTEREXAMPLE. The hypothesis is now attached in place there -- BY RICCI FOCUSING. The over-broad version had stood untested against the device this tree itself built"),
 # reverse.py -- the dichotomy read backwards, per M's own reversal rule.
 ("SIGNBLIND-BOTH-ENDS",+1, +1, +1, "reverse.py",
  "M's reversal rule applied to the DICHOTOMY rather than to a ray: the invariant visible from both ends is that WEYL IS SIGN-BLIND. Forward it says a negative mass escapes the Sturm density and so escapes collapse; backward it says a POSITIVE mass does too, for the same reason. Same binary chain, other end"),
 ("BOTH-SIGNS-SEAT-FREE",+1, +1, +1, "reverse.py",
  "MEASURED: -2e-3 seats at 56.50 and +2e-3 at 55.17, within 2.4% of the same affine parameter, and NEITHER is anywhere near its own Schwarzschild radius -- the region is 75 times r_s. Only the ARRIVAL flips sign. composite.py recorded that and nobody read it backwards"),
 ("SEAT-IS-OBSERVED",   +1, +1, +1, "reverse.py",
  "and the positive-mass seat is not hypothetical: the solar gravitational focus is f = b^2c^2/4GM = 547.6 AU against a published ~550. THE SUN HAS SEATED A CONJUGATE POINT FOR FOUR AND A HALF BILLION YEARS, violating no energy condition, collapsing nothing, and requiring no engineering"),
 ("DEVICE-SPLITS",      +1, -1, +1, "reverse.py",
  "SO THE DEVICE HAS TWO HALVES AND THEY DO NOT COST THE SAME. THE SEAT IS FREE -- ordinary matter, every energy condition satisfied, no collapse, an existing example. THE CONTRACTION CARRIES ALL OF IT -- it needs Phi > 0 hence rho < 0, and ordinary matter gives a proper ratio of 1.003076, which is LONGER. The obstacle was never 'the device'; it was always one half of it"),
 ("FOCUS-DESCRIPTION-STANDS",+1,+1,+1,"reverse.py",
  "which vindicates one description: 'a controlled gravitational focus at a chosen range, addressed by declaring both endpoints, built from fields that satisfy every energy condition' survives everything. What spec.py withdrew was the B*l invariant -- the STURM route to the seat, the one that collapses -- and the tree kept quoting that withdrawal as though it had taken the seat with it. It had not"),
 ("LENS-IS-NOT-TRANSITION",0,-1,+1,"reverse.py",
  "and it changes NO NUMBER. A free seat is not a free transition: the seat alone is a LENS, it focuses light at a range, carries no payload and shortens nothing. Every figure in phase1, supply.py, scale.py, currency.py and shaping.py prices the CONTRACTION and not one moves. 1.349e26 kg per metre stands exactly where it was. A LENS IS NOT A TRANSITION, AND THE SUN IS NOT A WARP DRIVE"),
 # contain.py -- what must be contained in miniature, and what that buys.
 ("CONTAINER-IS-SOLVED",+1, +1, +1, "contain.py",
  "what is contained is a NEGATIVE-ENERGY CORE, and the tree already specifies it end to end: core.py the contents (exact interior Schwarzschild with rho < 0, Hawking-Ellis TYPE I at |Im|/||T|| 1e-7 to 1e-8, p(0)/|rho| -> 1/3 from below, NO Buchdahl limit because a negative mass has none), concentric.py the container (a positive shell cancelling the monopole so M_ADM = 0), stability.py that it holds (V'' = +2.965e-2, stable for free at beta^2 = 0). THE CONTAINER WAS NEVER THE PROBLEM"),
 ("SMALLER-HOLDS-MORE", +1, +1, +1, "contain.py",
  "and miniature is the right instinct for a reason: shaping.py's derived ceiling |rho| <= (pi^2/192) hbar c/a^4 means a region of radius a may hold M <= 0.215321 hbar/(ac), which RISES as the core shrinks. Combined with scale.py's shortfall falling as (a/l_P)^2, shrinking is the ONLY direction in which the vacuum ever catches up"),
 ("MINIATURE-IS-FORCED",  0, -1, +1, "contain.py",
  "so miniature is not a preference but a NECESSITY: at any larger scale the density the corridor needs exceeds what the vacuum permits, and a Planck-sized core is the only size at which the requirement is admissible at all"),
 ("A-CANCELS",          +1, -1, +1, "contain.py",
  "AND IT BUYS EXACTLY NOTHING, BECAUSE THE CORE RADIUS CANCELS. The mass allowed rises as 1/a and the contraction it delivers rises in the same proportion, so M/Delta d = c^2/(G Lambda) -- no length in it and no trace of hbar. Measured size-independent over sixteen decades of a"),
 ("CORES-REPRODUCE-RATE",+1, +1, +1, "contain.py",
  "checked by a route sharing no algebra with phase1: 2.8785e34 Planck-sized cores per metre, each 0.2153 Planck masses, totalling 1.3489e26 kg/m against phase1's exchange rate of 1.3489e26 kg/m. RATIO 1.000000. The containment question and the cost question are the same question from opposite ends -- M's reversal rule landing a third time"),
 ("PACKAGING-IS-FREE",  +1, -1, +1, "contain.py",
  "SO THE ANSWER IS: you do not need to contain anything in miniature. You need to contain 1.349e26 kg of negative mass per metre of contraction and the PACKAGING IS FREE TO CHOOSE. Miniature is forced by the ceiling and changes the bill by nothing -- you simply need 2.9e34 of them"),
 ("NOT-A-COMPONENT",     0, -1, +1, "contain.py",
  "and at a = l_P all five of scale.py's approximations fail at once -- semiclassical gravity, Ford-Roman's own fixed background, geometric optics, the perfect-conductor Casimir formula and the weak field. 'A PLANCK-SIZED NEGATIVE-ENERGY CORE' IS NOT A COMPONENT SPECIFICATION. IT IS THE EDGE OF THE MAP, WEARING A COMPONENT'S NAME"),
 # reversal.py -- the supersession sweep, and a NOT-RUN with a named cause.
 ("SUPERSESSION-SWEEP", +1, +1, +1, "reversal.py",
  "THE PATTERN, NOW FOUR DEEP: when a file corrects another, the corrected file's DEPENDENTS are never swept. composite.py restored shear and three files had dropped it -- achronal.py, transit.py, seatindex.py -- and only achronal.py was ever corrected. NEITHER OF THE OTHER TWO MENTIONS SHEAR AT ALL, which is worse than wrong because nothing signals the scope. Swept deliberately here"),
 ("LYAPUNOV-STRUCK",     0, -1, +1, "reversal.py",
  "seatindex.py's 'Lyapunov's condition is universal the other way: below it nothing seats, ever' is FALSE with shear, and the counterexample was already in the tree: vacuum has q = 4 pi T_kk = 0 identically, so lyapunov_excluded() returns True -- 'excludes seating for ANY shape' -- while composite.py MEASURES A CONJUGATE POINT AT 56.50 in that same vacuum. Struck and narrowed to 'by RICCI focusing alone'. THIRD instance of a Ricci-only result asserted universally, after currency.py's ONE_STATEMENT and achronal.py's lemma"),
 ("MATRIX-REVERSAL-NOT-RUN",0,0,+1, "reversal.py",
  "and transit.py's reversal theorem -- M's own prediction, gating part 1 against part 3 -- was proven on the SCALAR equation. Attempted with the full matrix on a deliberately asymmetric ray: the FORWARD conjugate point converges cleanly (116.117 -> 116.194, settling near 116.20) and THE GAP DOES NOT, sitting near 1.6% and not falling over an EIGHTFOLD refinement in h"),
 ("INSTRUMENT-LIMIT",   +1, +1, +1, "reversal.py",
  "AND THE CAUSE IS MEASURED RATHER THAN GUESSED: the transverse screen is parallel-transported with a FIRST-ORDER EULER step whose traceless leak along that ray is 7.2301e-02. First-order transport is O(h) per step over L/h steps, hence O(1) GLOBALLY, so refining h converges the geodesic and the Jacobi and leaves the screen exactly where it was. A 1.6% EFFECT CANNOT BE RESOLVED WITH A 7.2% ERROR BAR"),
 ("NOT-REFUTED",         0,  0, +1, "reversal.py",
  "so matrix reversal is NOT-RUN and NOT refuted. transit.py's scalar 1.1e-14 stands and is correct about the problem it solved; the analytic argument is sound as far as it goes -- T is symmetric, so the Jacobi operator is self-adjoint and conjugacy is a SYMMETRIC RELATION -- but the measured quantity needs 'no conjugate point in between', itself NOT-RUN"),
 ("FIX-IS-SPECIFIC",     0,  0, +1, "reversal.py",
  "and what is needed is named rather than left open: HIGHER-ORDER PARALLEL TRANSPORT OF THE SCREEN, RK4 rather than Euler on e1 and e2. A contained change to composite.py that would sharpen every matrix result in this tree, not only this one"),
 # entsym.py -- "the symmetric relation is precisely what entanglement provides".
 ("TWO-SYMMETRIES",     +1, +1, +1, "entsym.py",
  "the instinct finds a REAL meeting point but the two symmetries are not the same theorem: CONJUGACY is symmetric because T is symmetric, and relates TWO POINTS ON ONE GEODESIC; ENTANGLEMENT is symmetric because the global state is pure, and relates TWO SUBSYSTEMS. Same word, different objects on each side of the relation"),
 ("QNEC-IS-THE-MEETING",+1, +1, +1, "entsym.py",
  "and where they DO meet is a theorem rather than an analogy: QNEC, <T_kk> >= (hbar c/2 pi) S'', whose left side is exactly what drives the Jacobi equation and whose right side is entanglement curvature along the ray. Already in this tree -- entangle.py inverted it for the corridor's entropy requirement"),
 ("QNEC-HAS-NO-WEYL",   +1, -1, +1, "entsym.py",
  "BUT QNEC BOUNDS T_kk AND CONTAINS NO WEYL TERM AT ALL. In vacuum T_kk = 0 identically, QNEC reads S'' <= 0 and IS SATISFIED, and composite.py seats a conjugate point at 56.50 in that same vacuum -- pure Weyl, with the entanglement bound indifferent to it. THE ENTANGLEMENT BOUND IS SILENT ABOUT THE CHANNEL THAT SEATS"),
 ("LANDS-ON-FREE-HALF", +1, -1, +1, "entsym.py",
  "so it lands on the half that was never the problem: QNEC is SILENT on the seat (no Weyl term) and BINDING on the contraction (the core's T_kk is exactly what it bounds, entangle.py's 2 pi^2). Entanglement's symmetric relation is absent from the half that costs and superfluous on the half that is free -- reverse.py's split, reached from the entanglement side"),
 ("THREE-WANT-A-THROAT",+1, -1, +1, "entsym.py",
  "and GJW shows what the relation needs: their coupling is explicitly bipartite, O_R against O_L, two boundaries thermofield-double entangled, and that symmetry does real work BECAUSE there are two systems. THREE ROUTES, ONE MISSING STRUCTURE: MTY needs two ends to age differentially, GJW two boundaries to couple, entanglement two subsystems to be symmetric between. The corridor has no throat, A and B are two points in ONE region, and the natural entanglement cut puts them on the SAME SIDE of it"),
 ("THE-FORK",            0,  0, +1, "entsym.py",
  "which puts a FORK to M rather than an answer: 'don't associate my theory with worm holes' is what makes the corridor throatless, and throatlessness is exactly what denies entanglement its bipartition. A throat would supply the two systems and would make the object a wormhole. A choice about architecture, not a fact about physics, and entsym.py states it and does not choose it"),
 # wormhole.py -- THE FORK, TAKEN.  M chose the throat.
 ("COST-STOPS-SCALING", +1, +1, +1, "wormhole.py",
  "THE WIN, AND IT IS STRUCTURAL: a throat's cost is proportional to the THROAT RADIUS and to nothing else -- M ~ r_0 c^2/(8 pi G), independent of how far apart the mouths are. A ONE-METRE THROAT COSTS ~9 EARTH MASSES WHETHER THE MOUTHS ARE A METRE OR FOUR LIGHT YEARS APART, against the corridor's 2.567e10 solar masses for 1% of Alpha Centauri: 15.0 ORDERS, and the ratio grows without limit with distance. phase1's complaint that a saving which does not scale with the journey is not a faster journey is EXACTLY what the throat fixes"),
 ("THROAT-WANTS-LARGE", +1, -1, +1, "wormhole.py",
  "BUT IT REVERSES contain.py: the throat tension is c^4/(8 pi G r_0^2) and DIVERGES as the throat shrinks -- 4.8155e42 Pa at a metre, reaching neutron-star central pressure only near 3 km. Kuhfittig's own figures reproduce (4.8155e41 dyn/cm^2 at 10 m; 5.35e35 Pa at 3 km) and his conclusion is 'Morris-Thorne wormholes could only exist on very large scales'. contain.py's 'miniature is forced' was the CORRIDOR's answer -- THE TWO ARCHITECTURES WANT OPPOSITE SIZES"),
 ("SAME-2PI2-AGAIN",    +1, +1, +1, "wormhole.py",
  "and the requirement is the one we already had: seatindex's T_kk coefficient pi c^4/4G = 9.5053e43 against the throat's c^4/8 pi G = 4.8155e42, ratio 19.739209 = 2 pi^2 EXACTLY. The same constant as entangle.py's holographic excess and, times three, spec.py's collapse ratio. THE WORMHOLE IS NOT A NEW PHYSICS PROBLEM -- it is the same requirement in a geometry that spends it better"),
 ("THROAT-REOPENS-MTY",  0, -1, +1, "wormhole.py",
  "and the throat reopens what it was missing: entanglement gets its two subsystems so entsym.py's obstruction lifts, GJW applies DIRECTLY rather than by analogy, and MTY COMES BACK AS A LIVE RISK -- anecscope.py closed it on 'no throat, no two ends to age differentially' and that closure is gone. The known mitigation is GJW's own coupling fixing the relative time coordinate"),
 ("ESCAPES-LEAVE-GR",   +1, -1, +1, "wormhole.py",
  "AND THE SCOPE DECISION IS M'S: Kuhfittig, arguing FOR wormholes, states that the zero-tidal-force solution -- Morris & Thorne's own -- CANNOT BE COMPATIBLE WITH QUANTUM FIELD THEORY in classical GR. Every escape in that literature LEAVES General Relativity: f(R) modified gravity, on the weak ground that the QI's curvature estimates 'come from Einstein's theory, not from the modified theory' (an argument that the DERIVATION does not transfer, not that the bound is absent), or a noncommutative background. Against 'true and proven in its math' that is a decision to prove something in a DIFFERENT THEORY"),
 ("GEOMETRY-NOT-PERMISSION",+1,-1,+1,"wormhole.py",
  "so within classical GR the throat buys GEOMETRY, NOT PERMISSION. The distance scaling is fixed, which is real, large and the reason to take the fork. The exotic source is exactly as unavailable as it was, and everything supply.py, scale.py, shaping.py and contain.py measured about sourcing rho < 0 still stands"),
 # gate.py -- "bigger inside", and projected against gate.
 ("NOT-BIGGER-INSIDE",  +1, -1, +1, "gate.py",
  "MEASURED AND IT DOES NOT HOLD: for Morris-Thorne with b(r) = r_0 the proper distance is l = sqrt(r(r-r_0)) + r_0 ln[(sqrt(r-r_0)+sqrt(r))/sqrt(r_0)], so the excess over the coordinate span is r_0[1/2 + ln 2 + (1/2)ln(r/r_0)] -- LOGARITHMIC. At a million throat radii the interior is longer by 8.101 r_0, eight thousandths of one per cent, and the ratio tends to ONE. Not factorial, not exponential, not even linear"),
 ("SHORTCUT-NOT-ROOM",  +1, +1, +1, "gate.py",
  "and it would cut the WRONG WAY if it were true: a bigger interior is MORE to cross, not less. What a wormhole sells is the SHORTCUT -- two mouths near each other in the embedding while far apart in the exterior -- and that product does not depend on the interior being large at all"),
 ("THROAT-IS-A-BOTTLENECK",+1,-1,+1, "gate.py",
  "and the throat is a HARD bottleneck: areal radius r_0, area 4 pi r_0^2, and a payload must physically fit through it. So the payload picks r_0 and r_0 sets everything -- mass goes as r_0 and wants SMALL, tension as 1/r_0^2 and wants LARGE. Going from human scale (2 m, 17.9 Earth masses, 1.2039e42 Pa) to Kuhfittig's 3 km costs 1500x in mass and buys 2.25e6 in tension. QUADRATIC PUNISHMENT FOR SMALL, LINEAR REWARD, and no optimum -- only a choice of which requirement to break"),
 ("PROJECTED-IS-MTY",    0, -1, +1, "gate.py",
  "PROJECTED LOSES, and by definition: carrying one mouth relative to the other IS the Morris-Thorne-Yurtsever construction, as its operating principle. anecscope.py closed MTY on 'no throat' and wormhole.py recorded that the closure is gone, so projection reopens it MAXIMALLY. It also cannot be established ahead of a signal, by phase1's Theorem 4"),
 ("GATE-WINS",          +1, +1, +1, "gate.py",
  "THE GATE WINS ON BOTH COUNTS: both mouths at rest means no differential aging, nothing accumulates, and the MTY construction has nothing to work with -- the same payment GJW make, the relative time coordinate fixed once at construction. And being STATIC it amortises, which phase1's Theorem 5 identified as the only place value was ever going to live"),
 ("GATE-IS-A-RETURN-TICKET",+1,-1,+1,"gate.py",
  "BUT THE GATE DECIDES WHAT THIS IS FOR: the far mouth must get there conventionally -- 4 ly at 0.1c is 40 YEARS, one way -- and nothing in the wormhole moves it. After that every crossing is free forever, 40/N years amortised. SO A GATE MAKES THE SECOND TRIP FREE AND DOES NOTHING FOR THE FIRST, AND A GATE NETWORK REACHES EXACTLY AS FAR AS CONVENTIONAL TRAVEL HAS. A return ticket and a supply line, not an exploration tool -- worth having, and a DIFFERENT PRODUCT from what this project has been calling warp transition"),
 # bothways.py -- a device for BOTH space and time.  Yes: a third mode.
 ("KNOBS-DECOUPLE",    +1, +1, +1, "bothways.py",
  "THE CAPABILITY DIFFERENCE, and it is structural: unified.py measured the corridor LOCKED -- one Phi, two exponents, ratio exactly 2, space and time unmovable separately at any strength or sign. A wormhole has TWO INDEPENDENT PARAMETERS: the THROAT sets the spatial shortcut, the MOUTH OFFSET sets the temporal displacement, and neither constrains the other. The corridor could not do this at all"),
 ("TIME-HALF-IS-FREE", +1, +1, +1, "bothways.py",
  "and the time half costs NO EXOTIC MATTER. The throat is what needs rho < 0 and it is bought once; the offset is bought with KINEMATICS -- Delta t = tau(gamma - 1), so four years of mouth travel at gamma = 2 banks four years of offset -- and costs propellant to accelerate an ADM mass, not negative mass, at any magnitude"),
 ("SHIFTED-MODE",      +1, +1, +1, "bothways.py",
  "THE ANSWER IS A THIRD OPERATING MODE, not a different object. GATE (offset 0): space only, safest, amortises. SHIFTED (0 < dt < D/c): BOTH space and time, and CHRONOLOGY-RESPECTING -- no closed timelike curves, nothing for chronology protection to act against. TIME MACHINE (dt > D/c): CTCs form. The middle mode is what the question asks for and it is legal"),
 ("WINDOW-GROWS",      +1, +1, +1, "bothways.py",
  "and the usable time displacement is D/c -- four years for a four-light-year gate, a century for a hundred. THE WINDOW GROWS WITH THE SEPARATION, which is the opposite of every other scaling in this project and is the first quantity here that improves with distance"),
 ("CANNOT-PRECEDE-BUILD",0, -1, +1, "bothways.py",
  "AND ONE LIMIT NO DEVICE BEATS: the offset is ACCUMULATED, so it cannot exceed the gate's own age. YOU CAN NEVER REACH BACK BEFORE THE GATE WAS BUILT. A property of the construction rather than of technology -- the quantity is a sum over elapsed time and the sum starts at construction, so there is nothing to improve"),
 ("ONLY-MODE-THREE-OPEN",0,  0, +1, "bothways.py",
  "and only the third mode is open: past D/c, Kim & Thorne (the Cauchy-horizon divergence is cut off at the Planck scale) against Hawking (it is not, and the machine is destroyed as it forms) has been unresolved since 1991. scale.py already carries it NOT-RUN. THE SHIFTED MODE NEVER ENTERS THAT REGIME, so nothing here rests on it"),
 # create.py -- sweeping phase1's dependents; CREATE is not CONTAIN.
 ("GATE-FAILS-D2",      +1, +1, +1, "create.py",
  "SWEEPING phase1's DEPENDENTS AFTER THE ARCHITECTURE CHANGE, per reversal.py's lesson: the wormhole gate FAILS phase1's own D2. R^3 is simply connected and a wormhole is not, and no continuous deformation of a metric on a FIXED MANIFOLD bridges that at ANY support -- it fails on TOPOLOGY, not size. A throat was never in phase1's candidate ranking either, so 'PHASE 1 IS FINISHED AS MATHEMATICS' was finished about an architecture the project has left. Scoped in place there"),
 ("CREATE-IS-NOT-CONTAIN",+1,+1,+1, "create.py",
  "which separates two problems the phrase 'create and contain a stable wormhole' runs together: CONTAIN is a METRIC problem and this tree has worked on it for thirty passes (concentric, stability, core, wormhole, gate); CREATE is a TOPOLOGY problem and the tree had never once looked at it"),
 ("CREATION-IGNORES-SOURCE",+1,-1,+1,"create.py",
  "and creation has its own theorem, harsher IN KIND than the source problem. Geroch, Tipler and Borde (gr-qc/9406053): topology change forces causality violations, and the argument is PURELY KINEMATICAL -- 'neither Geroch's original theorem, nor its mild generalization, assume anything about the energy-momentum tensor, or indeed about a field equation'. SO EXOTIC MATTER CANNOT HELP. Every other wall in this project was about SOURCING something; this one does not care what the source is"),
 ("SINGULARITY-NO-ESCAPE",+1,-1,+1, "create.py",
  "and the escape I expected fails: accepting a singularity does NOT buy topology change. Borde -- 'as long as the causal compactness condition is met, causality violations have to occur when the topology changes, EVEN IF INCOMPLETE GEODESICS ARE ADMITTED'. Dynamically worse: in d >= 3 causally compact topology-changing spacetimes cannot satisfy Einstein's equation with a reasonable source"),
 ("CREATION-ESCAPES-LEAVE-GR",0,-1,+1,"create.py",
  "Borde's three escapes all leave Lorentzian GR or accept a pathology: dropping causal compactness gives Tipler's singularity or A POINT AT INFINITY ('a highly undesirable feature'); weakening the curvature constraints needs an alteration of Einstein's equation that 'would have to be fairly severe'; the Euclidean path integral abandons the Lorentzian framework. Same shape as wormhole.py's scope warning, and his own caution is kept verbatim: the theorems' value is to 'pinpoint what modifications we have to make', not to rule it out"),
 ("ENLARGE-DONT-CREATE",+1, +1, +1, "create.py",
  "AND THE CLEAN ESCAPE IS ARCHITECTURAL: every theorem above is about topology CHANGE. If the topology is ALREADY nontrivial, growing a throat from r_0 to r_1 is a METRIC change and NONE OF IT APPLIES -- and that is exactly the problem this tree has been solving all along. NOT 'manufacture a wormhole' but 'FIND ONE AND ENLARGE IT'"),
 ("SEARCH-NOT-BUILD",    0, -1, +1, "create.py",
  "with the honest cost stated: NOBODY HAS EVER OBSERVED ONE. It converts a construction problem into an ASTRONOMY problem, which is a real conversion and not a small one -- but it is a DIFFERENT problem and nothing in the topology theorems closes it. The live constructive literature (arXiv:2505.02210, wormhole nucleation via Morse theory and 0-surgery) is named rather than leaned on: NOT-RUN"),
 # detect.py -- how to identify one.  The target is now find, not build.
 ("ABSORB-VS-TRANSMIT", +1, +1, +1, "detect.py",
  "THE DISCRIMINATOR IS ONE FACT AND IT IS TOPOLOGICAL: in the tortoise coordinate a black hole's range covers the horizon and ONE asymptotic region while a wormhole's covers TWO with NO horizon (Chakraborty & Chakraborty, arXiv:2509.13715). A BLACK HOLE ABSORBS; A WORMHOLE TRANSMITS. Every signature is that seen through a different instrument, and anything not tracing back to it is not a discriminator"),
 ("SHADOW-CANNOT-SETTLE",0, -1, +1, "detect.py",
  "and the most useful line is which channel FAILS: the review is explicit that 'wormholes can mimic black hole shadows', so THE SHADOW ALONE CANNOT SETTLE IT and EHT by itself is not the answer -- which is the channel a reader assumes decides the question. Five channels do discriminate: QNM spectrum, echoes, grey body factors, lensing, and negative-mass microlensing"),
 ("DAMPING-READS-B-PRIME",+1,+1,+1, "detect.py",
  "THE SMOKING GUN IS QUALITATIVE: Im(omega) = sqrt((b_1-1)(b_0 Phi_1-1))/(sqrt2 r_sh), so as flare-out becomes marginal (b'(r_0) -> 1) the ringing becomes UNDAMPED -- standing waves on a string fixed at the throat. A BLACK HOLE ALWAYS DAMPS, at every parameter, because energy falls through the horizon. And better than a yes/no: the damping INVERTS for b'(r_0), an observable that measures a metric function of the throat"),
 ("TWO-INSTRUMENTS-LOCKED",+1,+1,+1,"detect.py",
  "and Re(omega) = (l+1/2)/r_sh LOCKS TWO INSTRUMENTS TOGETHER: EHT measures r_sh, LIGO measures Re(omega), one object and one relation. The claim can be KILLED by a disagreement rather than only supported by an agreement -- the property this project has demanded of its own results throughout, and it is available here"),
 ("NO-PHOTON-SPHERE",   +1, +1, +1, "detect.py",
  "and our own design carries a surprise: the photon sphere satisfies r Phi'(r) = 1, and Kuhfittig's ZERO-TIDAL-FORCE design has Phi' = 0 identically, so r Phi' = 0 and NEVER 1. THERE IS NO PHOTON SPHERE AT ALL -- the throat itself is the shadow boundary and r_sh = r_0. A sharper prediction than a generic wormhole makes, and a consequence of the design rather than an assumption"),
 ("DESIGN-POINTS-TOO-SMALL",0,-1,+1,"detect.py",
  "and both of our design points ring ABOVE the LIGO band: 5.964e7 Hz at two metres and 3.976e4 Hz at three kilometres, against a band topping out near 10 kHz. NEITHER IS FINDABLE THAT WAY"),
 ("SEARCH-NEEDS-NO-DETECTOR",+1,+1,+1,"detect.py",
  "BUT INVERTING IT GIVES THE TARGET AND IT NEEDS NO NEW INSTRUMENT: a wormhole ringing at 100 Hz has a 1193 km throat and 32.13 SOLAR MASSES of exotic matter -- EXACTLY the stellar-mass range LIGO already observes. The search wants the right DISCRIMINATOR applied to an existing catalogue (echoes, QNM spectrum), not a new detector and not the shadow"),
 ("ALREADY-LARGE-ENOUGH",+1, +1, +1, "detect.py",
  "which reframes M's second half: a LIGO-band find at 1193 km is 400 times Kuhfittig's tension-viable three kilometres, so IF ONE IS FOUND THERE IT IS ALREADY LARGE ENOUGH and 'enlarge it' may be the wrong question. The environment needed is NEC violation locally at the throat and nowhere else"),
 ("RELIC-NOT-CONSTRUCTION",+1,+1,+1,"detect.py",
  "and provenance agrees with create.py from the other direction: the review's own suggestion is that 'primordial microscopic WHs evolve to macroscopic size' during inflation. A RELIC, NOT A CONSTRUCTION -- which create.py's topology theorems forced independently. Two different routes, same conclusion: look for something old, do not try to make something new"),
 # negmass.py -- what the searches found, and Trivedi & Loeb's M = 0 case.
 ("ECHO-STATUS",         0,  0, +1, "negmass.py",
  "detect.py's NOT-RUN settled AS A STATUS: six independent echo analyses 2016-2025 -- Abedi/Dykaar/Afshordi's ~2.9 sigma (1612.00266), the AEI reanalysis finding LOW SIGNIFICANCE (1712.09966), the reply (1803.08565), GWTC-1/O3 (2010.07663), O3/LVK (2309.01894), and a model-agnostic search (2512.24730). NO CONFIRMED DETECTION, the dispute live. Run repeatedly and not converged -- which is a status and not a result either way"),
 ("DIPOLE-BOUNDS-NEGMASS",+1,-1,+1, "negmass.py",
  "and negative mass is ALREADY CONSTRAINED, more tightly than expected. Trivedi & Loeb (arXiv:2605.10976): dipole radiation bounds B <~ 1e-7, while opposite gravitational charge (delta alpha = 2) gives B = 0.2083 -- 6.32 ORDERS OVER, RULED OUT. Negative mass survives only with UNIVERSAL coupling, alpha_- ~ alpha_+ across orbital dynamics, lensing and cosmology alike"),
 ("OUR-CASE-IS-M-ZERO",  +1, -1, +1, "negmass.py",
  "and they analyse OUR EXACT CONFIGURATION: their three cases are M>0/mu<0 (ANTI-CHIRP, the orbit expands while radiating), M<0 (DISPERSES), and M=0 (RUNAWAY, 'both accelerate indefinitely in the same direction'). concentric.py IS M_ADM = 0, measured -4.000e-15. THE THIRD CASE IS LITERALLY OUR DEVICE"),
 ("CONCENTRIC-BEATS-BONDI",+1,+1,+1,"negmass.py",
  "IT DOES NOT RUN AWAY, AND THE REASON IS GEOMETRY: their M = 0 case is a BINARY, a dipole; ours is CONCENTRIC. Newton's shell theorem gives zero force on an interior point at ANY displacement whatever the signs, integrated here rather than quoted with the residual shown to fall with resolution. THE BONDI RUNAWAY NEEDS A DIPOLE AND OURS HAS NONE -- an argument FOR the two-region design that this tree had never made"),
 ("L1-NEVER-NAMED",       0, -1, +1, "negmass.py",
  "but zero force is NEUTRAL, not restoring, and that exposes a mode nobody named: stability.py measured the RADIAL breathing mode and flagged l >= 2 as the top risk, while l = 1 -- THE TRANSLATION MODE -- is not mentioned anywhere in it. Neutrally stable means the failure is DRIFT TO CONTACT rather than exponential runaway: the core wanders until it reaches the shell, where the theorem stops applying. Slower than the literature's failure and still a failure. Annotated in place; the GR version is NOT-RUN"),
 ("SAFE-MEANS-INVISIBLE",+1, -1, +1, "negmass.py",
  "AND THE DESIGN CREATES ITS OWN DETECTION PROBLEM: M_ADM = 0 means gravitationally invisible at range -- no lensing, no microlensing, no orbital perturbation, no dipole radiation, and Trivedi & Loeb's anti-chirp channel is silent on us because it belongs to M>0/mu<0. THE PROPERTY THAT MAKES THE DESIGN SAFE, SATISFYING THE POSITIVE MASS THEOREM, IS THE PROPERTY THAT MAKES IT UNFINDABLE"),
 ("TARGET-ISNT-DESIGN",  +1, -1, +1, "negmass.py",
  "which separates two objects the project had been treating as one: detect.py's SEARCH TARGET is a 1193 km throat at 32.13 SOLAR MASSES in the LIGO band, and concentric.py's DESIGN is M_ADM = 0. THE ONE WE COULD FIND IS NOT THE ONE WE DESIGNED -- and if the route is 'find one and enlarge it', the thing to look for HAS a mass, and the mass IS the signal"),
 # chain.py -- the binary chain, and what a binary can and cannot give a geometry.
 ("BINARY-IS-A-FUNCTION",+1, +1, +1, "chain.py",
  "M's binary chain and register 1173's binary are the same object and NOT by a match of counts, which is the failure unified.py caught on eight. A BINARY CHAIN IS A FUNCTION c : {0..n-1} -> {+1,-1}: 1173 supplies the CODOMAIN, the chain supplies the DOMAIN, and the geometry is the PUSHFORWARD, M_l = sum_i c(i) z(i)^l. Exact rather than suggestive, and immediately falsifiable"),
 ("CITATION-NOT-BINARY", +1, -1, +1, "chain.py",
  "and the falsification takes half the sentence: THE BINARY GIVES NOTHING. Cite any code at a single point and every moment above the monopole is identically zero -- measured for alternating, Thue-Morse and an arbitrary code. A CODE WITH NO CITATION HAS NO GEOMETRY, not a small one, none. M's own word CITATION is the operative one and the noun it attaches to is not: it is the PLACEMENT that carries the geometry"),
 ("ZERO-SEPARATION-IS-ONE-FACT",+1,+1,+1,"chain.py",
  "which collapses two negmass.py findings into one. The device HAS the binary -- a negative core inside a positive shell is two signs -- and what it lacks is a SEPARATION, since concentric means coincident centroids. THE DEVICE IS A BINARY CITED AT ZERO SEPARATION, and that single fact is why it does not run away (no dipole for Bondi) and why it cannot be seen (no dipole radiation, no monopole). Safe and invisible were reported as two facts; they are one"),
 ("THUE-MORSE-IS-THE-CODE",+1,+1,+1,"chain.py",
  "and the code really does choose the geometry, provably. Thue-Morse -- c(i) = (-1)^popcount(i), the parity of the bits of the index and nothing else, a PURE LOGIC CITATION OF THE BINARY -- suppresses every moment below l at length 2^l, asserted in EXACT INTEGER ARITHMETIC for k = 1..8. Exhaustive search over all 2^n codes at n = 2,4,8,16 (65,536 at the top) finds NONE BETTER. That is M's sentence, measured, and true"),
 ("SYMMETRY-BEATS-CODE",  +1, -1, +1, "chain.py",
  "but the refusal is ONLY: read the optimum backwards and suppression through order l costs a chain of 2^l elements, exponential. A SYMMETRIC PAIR KILLS MOMENTS 1,3,5,7,9 WITH TWO ELEMENTS where the best possible code needs 512, and Newton's shell theorem kills the interior field outright. Symmetry and code are the two mechanisms for quieting a configuration and SYMMETRY IS EXPONENTIALLY CHEAPER. A code earns its place where symmetry is unavailable, and here it is available"),
 ("BINARY-MINIMAL-NOT-NECESSARY",0,-1,+1,"chain.py",
  "and a second, smaller refusal of ONLY: q-ary Prouhet does the same job for any alphabet size, verified for q = 3 at k = 1..4. BINARY IS SUFFICIENT AND MINIMAL, NOT NECESSARY -- and Shannon says it from the other side, that any alphabet encodes in binary, so 'only binary' is a NORMALISATION rather than a physical restriction. The physical content was never in the alphabet"),
 ("EARNSHAW-CLOSES-L1",  +1, +1, +1, "chain.py",
  "and the chain question forces the general version of negmass.py's open mode, which is a theorem. The Hessian of 1/r is TRACELESS away from the source, so the potential of any point sources is harmonic WHATEVER THE SIGNS -- negating m flips U = m phi and -phi is harmonic too -- and a harmonic function has no strict minimum. NO STATIC CONFIGURATION OF POINT MASSES IS STABLY IN EQUILIBRIUM, for any signs, any code, any placement"),
 ("NEUTRAL-IS-THE-CEILING",+1,+1,+1,"chain.py",
  "and Earnshaw EXPLAINS negmass.py rather than contradicting it. Its one escape is the DEGENERATE case, constant potential with the Hessian identically zero, and Newton's shell theorem delivers precisely that inside a uniform shell. The concentric device is sitting in THE ONLY SEAT EARNSHAW LEAVES. So 'drift to contact' is not a defect of this design to engineer out -- IT IS THE NEWTONIAN CEILING. Any restoring force must come from outside Newtonian statics: GR, time dependence, or a non-gravitational channel. l = 1 CLOSED in Newtonian gravity with the answer 'neutral is optimal'; the GR version stays NOT-RUN"),
 # pair.py -- the conservation ledger a wormhole/black hole pair would need.
 ("EMITTER-IS-THE-HOLE", +1, -1, +1, "pair.py",
  "the polarity is inverted. A black hole EMITS -- Hawking T = hbar c^3/(8 pi G M k_B), 6.17e-8 K at a solar mass and 1.92e-9 K at detect.py's 32.13-solar-mass target -- while a horizonless wormhole has no surface gravity, no temperature and no emission at all. The contrast being reached for is real and it is detect.py's ABSORB-VERSUS-TRANSMIT, not absorb-versus-emit"),
 ("ER-BRIDGE-IS-THE-PICTURE",+1,-1,+1,"pair.py",
  "and 'a tunnel with a black hole at the far end' is not hypothetical: it is the maximally extended Schwarzschild solution, the EINSTEIN-ROSEN BRIDGE, in vacuum, needing no exotic matter -- with a WHITE hole at the far end, since a horizon is one-way by definition and nothing exits through a black hole. MEASURED IMPASSABLE: the X=0 throat falls from r=2M at Kruskal T=0 to zero at T=1, and every leftward null ray T = c - X meets the singularity at X_s=(c^2-1)/2c, T_s=(c^2+1)/2c with |X_s| < T_s because |1-c^2| < 1+c^2 for EVERY c>0. Scanned over 200,000 starting points, strictly negative margin at each. That is why Morris-Thorne had to add the exotic matter"),
 ("CHARGE-PAIRS-MASS-DOESNT",+1,+1,+1,"pair.py",
  "and the pairing principle is a STANDARD THEOREM about the wrong quantity. Wheeler's CHARGE WITHOUT CHARGE: thread a wormhole with field lines and the mouths are +Q and -Q with no charged matter anywhere, ledger closing exactly. But the mass that goes with a charge goes as Q SQUARED and is therefore SIGN-BLIND: the mouths carry opposite charge and the SAME POSITIVE mass, so the mass ledger does not cancel, IT DOUBLES. A quantity pairs +- IFF it is sign-symmetric"),
 ("RIGIDITY-DERIVES-THE-EXOTIC",+1,+1,+1,"pair.py",
  "THE FINDING. Balance pushed through the positive mass theorem gives not (+E,-E) but M_ADM = 0 -- which IS concentric.py, measured -4.000e-15 -- and then the theorem's SECOND half fires, the RIGIDITY clause this tree had never used: M_ADM = 0 under the DEC implies the spacetime is MINKOWSKI. The device is not Minkowski. THEREFORE ITS MATTER CANNOT SATISFY THE DEC. Negative energy is not an assumption of this design, it is DERIVED from the design's own M_ADM = 0, by a theorem, with no appeal to any magnitude. concentric.py caution 1 said ASSUMED and is superseded in place"),
 ("BALANCE-PROVES-THE-BILL",+1,-1,+1,"pair.py",
  "which inverts what the principle looked like it bought. The closed index admits no defect and the positive mass theorem AGREES -- then charges for it: THE ONLY BALANCED, NON-TRIVIAL CONFIGURATION IS ONE THAT VIOLATES THE DOMINANT ENERGY CONDITION. Balance does not remove the exotic-matter bill. IT IS THE PROOF THAT THE BILL IS UNAVOIDABLE"),
 ("CLOSED-ENERGY-UNDEFINED", 0, -1, +1, "pair.py",
  "and at cosmological scale the principle is true and EMPTY. ADM mass is a surface integral at spatial infinity and a spatially closed universe has none, so the total energy of a closed universe is not zero -- it is UNDEFINED. A quantity that does not exist cannot be out of balance, and cannot pair two objects inside the universe either. A definitional refusal, filed as one and not as a measurement"),
 ("SIGNBLIND-PAIRS",     +1, +1, +1, "pair.py",
  "and what survives is one line worth keeping: A SIGN-BLIND QUANTITY PAIRS; A SIGN-COMMITTED ONE DOES NOT. Charge pairs because it is sign-symmetric, energy does not because the positive mass theorem commits it -- and that is dichotomy.py's split arriving from a completely different direction, Weyl focusing sign-blind with both signs seating against Ricci focusing sign-committed with only one. TWO INDEPENDENT ROUTES TO THE SAME DISCRIMINATOR"),
 ("LEDGER",          0, -1,  0, "obstruct.py",
  "of thirty-five obstructions six dissolved, FOUR relocated, seventeen closed negative, seven conditional, ONE open and none untested"),
]

# Support points: they correct or enable other cells but answer no directive.
# Kept out of the index deliberately -- a method note is not a finding.
SUPPORT = [
 ("NEC-FIX",   "NEC-CORRECTION.md", "index lowered with the wrong metric; ceiling was an artefact"),
 ("SCALE-FIX", "THE-DRIVE.md",      "the 10^31 gap was a 20 m artefact; size was never varied"),
 ("ADM-FIX",   "COUPLING.md",       "ADM was over-applied to coupling mechanisms; withdrawn"),
 ("SRC-READ",  "SOURCE-CODE.md",    "reading Warp Factory found two of this series' inferences wrong"),
 ("LOOP",      "kerr.py",           "the index looped because 9 papers were never seated; guard added"),
 ("BETA3-FIX", "person.py",         "the beta^3 mass floor passed at a/3, where the bend is 1.2 deg; gain overstated 116x"),
 ("LIT-FIX",   "stationkeep.py",    "the bound-return theorem assumed a static field; Zhang Sec 3.3 and Shipley-Dolan refute it"),
 ("AR-VALID",  "stationkeep.py",    "this tree's kinematics reproduce A&R's three printed Sgr A* figures to 0.2%"),
 ("EDGE-LIST", "necladder.py",      "the edge list the compendium says is printed nowhere is in extracted/; it gives 2,370"),
 ("SAIL-FIX",  "beamed.py",         "the sail integrated in distance is singular at beta=0 and gave efficiency > 100%; time-domain"),
 ("CARVE-OUT", "restatus.py",       "Rodal's own Sec 3.3 excludes analogue models from his no-go; the one hard closure carves it out"),
 ("COUPLE-FIX","door.py",           "'does not couple to real spacetime' withdrawn: it is h ~ 4.5e-24, and Sec 17.1 was written past"),
 ("SMOL-GAP",  "neclab.py",         "Smolyaninov asserts energy conditions are not a problem and never computes it; neclab.py does"),
 ("BOUNDARY",  "device.py",         "safe_beta bisects to ZERO margin; a bisected boundary is not a design point, so a 5% safety factor"),
 ("CASCADE",   "device.py",         "TEST 4 failed AGAIN when the cell shrank; ring radius and substrate are now derived, not assumed"),
 ("SPHERE-FIX","device.py",         "the figure drew a spherical bubble; the mapping is 1+1D and the geometry is a stack"),
 ("LOSS-FIX",  "device.py",         "a single Q for the whole block was the wrong model; the ferrite carries 90% and dominates the loss"),
 ("PROVES-FIX","device.py",         "the analogue was seated as a bench PROOF; TEST 16 shows it confirms the medium, not the metric"),
 ("HORIZON-FIX","twist.py",         "TEST 16 was read as the wall; the horizon was never required, and the real wall is that 1+1D is flat"),
 ("BBV-CHECK",  "twist.py",         "this tree's twist reproduces BBV Eq (3.47c) to ten digits and their Thm III.15 independently"),
 ("SSV-ERRATA", "warpshell.py",     "BBV report minor errors in Santiago-Schuster-Visser itself, at their Errors 9 and 29"),
 ("GEODESIC-VERTEX","pathmetric.py",  "M's lattice metric misglosses st=0 as betweenness; the geodesic set is the box's VERTICES, up to 6,561x smaller"),
 ("NOT-LENGTH-SPACE","pathmetric.py", "log(|D|+1) is concave, so an index penalises subdivision and its first step costs log 2: not a length space"),
 ("RADIAL-CONFIRMED","wall.py",       "this tree's beta^2_crit converts to LeMaitre-Poisson's Gamma_1 to 1e-15 at every x: independent derivation, same answer"),
 ("HUND-CHECK", "materials.py",     "Hund's rules against the 108 seated NIST ground terms: 74/78 term symbols, 78/78 on J -- the four differ in notation only"),
 ("SUBSTRATE",  "materials.py",     "a linewidth table alone picks the wrong substrate: YSGG beats GGG on dB and loses on merit, because Ms is halved"),
 ("GAIN-MOOT",  "dispersive.py",    "the gain exemption was not needed: passivity was never the problem, staticity was, and passive dispersion is free"),
 ("NO-EVIDENCE","shape.py",         "the shape has earned nothing yet: the four hits are the sample it was fitted to, and its only test is a prediction that lands"),
 ("SHAPE-WRONG","shape.py",         "and its first tested prediction FAILED: the dynamical form of the energy condition is stricter, not looser; evidence back to 0"),
 ("HEADLINE-OUT","nullbound.py",    "this session's headline is withdrawn -- one sampling width is not a scan, and the loosest one was chosen"),
 ("QUAD-CAUGHT", "smearing.py",     "widening the integration window COARSENED the uniform grid until the core was sampled by under one point; the answer drifted and then flipped SIGN at X=3e5. Short window, fine grid, convergence asserted against the closed form"),
 ("OVERWRITE-CAUGHT","anecscope.py",  "this file was first written as selfconsistent.py, silently overwriting a tracked 251-line instrument of that name; obstruct.py's import of its SCOPE dict failed and exposed it. Restored byte-exact from git and renamed. Check the tree before claiming a filename"),
 ("FLAT-VS-VACUUM","achronal.py",  "its flat-space control read 'no conjugate point' off ONE affine length and then asserted the lemma 'applies trivially to vacuum' -- which anecscope.py had just shown is where the lemma is WRONG. Hardened to length-independence (400/4000/40000 steps) and corrected: FLAT means Riemann = 0, VACUUM means only R_kk = 0 and includes the exterior of a mass where Weyl focuses. The lemma cannot tell them apart because it only ever sees T_kk"),
 ("SIMPSON-ODD","gate.py",        "two quadrature faults in one measurement: a uniform grid across an INTEGRABLE SINGULARITY at the throat overstated the interior by 2.7x and would have made the claim look partly true; and the substituted check then used n = 20001, an ODD interval count, mis-weighting the last interval by h*f(U)/3 = 0.034. Both fixed, an even-n assert added, and the tree's other Simpson calls audited -- unharmed because their integrands vanish at the limit (smearing.py 1.9e-21, phase1.py 0.0)"),
 ("NULL-CAUGHT","shape.py",         "NO-EVIDENCE was first seated as a finding at (0,0,0); the index refused it, because the null cell is declared not a finding"),
]

AXES = ("X: identify warp energy", "Y: drive possible", "Z: specs derivable")

def coords(f):
    return (f[1], f[2], f[3])

def on_all_three(f):
    """A cell with no zero: it sits on all three axes.  2.17.3's 'coordinate'."""
    return all(v != 0 for v in coords(f))

def join(a, b):
    return tuple(max(p, q) for p, q in zip(a, b))

def meet(a, b):
    return tuple(min(p, q) for p, q in zip(a, b))

NULL = (0, 0, 0)   # silent on all three directives: the index's zero, not a finding

def closure(cells):
    """R(X): closure under meet and join, iterated to a fixed point."""
    R = set(cells)
    while True:
        new = {c for a, b in itertools.combinations(sorted(R), 2)
                 for c in (join(a, b), meet(a, b)) if c not in R}
        if not new:
            return R
        R |= new

def defect(cells):
    """E(X) = |R(X)| - |X|, and the cells the closure demands.

    Section 25.6: the number of predictions an index can make is E(X), and a
    COMPLETE index (E = 0) makes none.  NULL is excluded by declaration: a cell
    silent on every directive is the lattice bottom, not a claim about anything.
    """
    X = set(cells)
    pred = sorted(closure(X) - X - {NULL})
    return len(pred), pred

def closure_failures(cells):
    """Count pairs whose join / meet is not itself an occupied cell.

    This is the same test the three-body project ran on the triangle form
    (caps_table.py): join failures against meet failures, on K_3.
    """
    occ = set(cells)
    jf = mf = 0
    for a, b in itertools.combinations(sorted(occ), 2):
        if join(a, b) not in occ: jf += 1
        if meet(a, b) not in occ: mf += 1
    return jf, mf

def neighbours(target, cells):
    """Occupied cells at Hamming-1 in coordinate value: the supporting points."""
    out = []
    for f in FINDINGS:
        cq = coords(f)
        if cq == target: continue
        if sum(1 for p, q in zip(cq, target) if p != q) == 1:
            out.append(f)
    return out

def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("Provenance -- every cell must cite a file that exists")
    here = os.path.dirname(os.path.abspath(__file__))
    missing = [f[4] for f in FINDINGS + [(0,0,0,0,s[1]) for s in SUPPORT]
               if not os.path.exists(os.path.join(here, f[4]))]
    chk("findings citing a missing file", missing, [])

    print("\nCoordinates are well formed")
    bad = [f[0] for f in FINDINGS if any(v not in (-1,0,1) for v in coords(f))]
    chk("cells with an out-of-range coordinate", bad, [])
    chk("number of findings indexed", len(FINDINGS), 397)
    chk("distinct occupied cells", len({coords(f) for f in FINDINGS}), 15)
    # TYPE-IV opened (+1,-1,-1) -- identified, and unbuildable BECAUSE identified.
    # 130 findings had never occupied it; it is the cell for a positive answer on
    # X that is the reason for the negative answers on Y and Z.
    # TYPE-IV opened (+1,-1,-1) and ANEC-VIOLATED joined it.  Both surviving
    # objections share a coordinate, and it is the right one: warp energy is
    # identified, and what identifies it is what forbids the build and the spec.
    # The cell has kept filling, and what fills it is the point: every hard
    # objection this project has met sits at (+1,-1,-1) -- warp energy
    # IDENTIFIED, and what identifies it is what forbids the build and the spec.
    # The two newest are about the core, not about ANEC, and they landed here
    # anyway.
    chk("the cell TYPE-IV opened holds every hard objection, old and new",
        sorted(f[0] for f in FINDINGS if coords(f) == (1, -1, -1)),
        ['ACHRONAL', 'ANEC-VIOLATED', 'BANK-LOAN-THEOREM', 'CHARGE-NO-LEAD', 'GAP-WIDENS', 'NO-ACHIEVABLE-CORE', 'TYPE-IV'])
    chk("cells possible in {-1,0,1}^3", 3**3, 27)

    print("\nThe corpus's own Law 3 prediction, tested on this index")
    print("  K_3 needs strong 3-consistency; the closure operator delivers 2, so")
    print("  the join should close and the meet should fail.")
    jf, mf = closure_failures({coords(f) for f in FINDINGS})
    chk("join failures after seating the predicted cell", jf, 0)
    chk("meet failures > 0 (certainty dies downward)", mf > 0, True)

    print("\nThe question the index exists to answer")
    triple = [f[0] for f in FINDINGS if on_all_three(f)]
    # Only cells with NO zero.  T2-ADM and SWIMMER are (0,-1,-1) -- they carry a
    # zero on X and so do NOT sit on all three, which my first hand list got wrong.
    chk("cells sitting on all three axes", sorted(triple), sorted([
                "A-CANCELS","ABSORB-VS-TRANSMIT","ACHRONAL","ALREADY-LARGE-ENOUGH","ANEC-CROSS-CHECKED","ANEC-RELOCATES","ANEC-VIOLATED","AREA-OVER-THICK","BALANCE-PROVES-THE-BILL","BANK-LOAN-THEOREM","BH-IS-WRONG-SIGN","BINARY-IS-A-FUNCTION","BOTH-SIGNS-SEAT-FREE","BUILT-SOURCE","CASIMIR-ROUTE","CATALOGUE","CHANGE-OF-KIND","CHARGE-NO-LEAD","CHARGE-PAIRS-MASS-DOESNT","CITATION-NOT-BINARY","CLASSICAL-WINS","COLLAPSE-BINDS-RICCI","CONCENTRIC-BEATS-BONDI","CONTAINER-IS-SOLVED","CONTRACTION-LAW","CONVERSION-IS-DONE","CORE-IS-TYPE-I","CORES-REPRODUCE-RATE","CORRIDOR-NOT-A-BH","COST-DOES-NOT-CLOSE-IT","COST-IS-ONE-NUMBER","COST-STOPS-SCALING","COUNTING-CLOSES-IT","CREATE-IS-NOT-CONTAIN","CREATION-IGNORES-SOURCE","D-CANCELS","DAMPING-READS-B-PRIME","DESIGN-EQUATION","DEVICE-IS-CLASSICAL","DEVICE-NOT-RETRACTED","DEVICE-SEATS-LEADS","DEVICE-SPLITS","DIPOLE-BOUNDS-NEGMASS","DISSENT-IS-VALUE","EARNSHAW-CLOSES-L1","EC-TAKEN","EFFICIENCY-CANNOT","EM-GAP","EM-IS-ORDINARY","EMITTER-IS-THE-HOLE","ENLARGE-DONT-CREATE","ENTANGLEMENT-IS-IT","ENTROPY-IS-PLANCK-DENOMINATED","ER-BRIDGE-IS-THE-PICTURE","ESCAPES-LEAVE-GR","ESCAPES-TYPE-I","EXCHANGE-RATE","EXTERNAL-PATH-ESCAPE","FLYBY","FOCUS-DESCRIPTION-STANDS","FORD-ROMAN-DERIVED","GAIN-SATURATES","GAP-IS-THE-LEVER","GAP-WIDENS","GATE-FAILS-D2","GATE-IS-A-RETURN-TICKET","GATE-WINS","GEOMETRY-NOT-PERMISSION","GJW-IS-EXISTENCE-PROOF","INSTRUMENT-LIMIT","KAPPA-IS-THE-ONLY-LEVER","KERR-FLYBY","KNOBS-DECOUPLE","LANDS-ON-FREE-HALF","LAUNCHER","LEAD-IS-INTERIOR","LENSING-IS-THE-SEAT","LIMIT-DISSOLVES","LOG-AGAINST-LINEAR","LOG-COORDINATE","LONG-AND-WEAK","LOOP-OBSERVABLE","MAGNITUDE-REACHED","NARROWER-CLOSING","NEUTRAL-IS-THE-CEILING","NO-ACHIEVABLE-CORE","NO-ACHRONAL-VIOLATOR","NO-BUCHDAHL","NO-EXOTIC","NO-GEOMETRY-LEFT","NO-HORIZON","NO-MOMENTUM-FLUX","NO-NULL-QI","NO-PHOTON-SPHERE","NO-THROAT","NOT-BIGGER-INSIDE","NOT-POWERED","NOTHING-STRUCTURAL","OBJ-CEILING","OBSERVED-ENGINE","ONE-AXIS-FLAT","ONE-NAME-AGAIN","ONE-OBSTACLE","ONE-SIGN-EXOTIC","OPEN-GATE","ORDER-MOVED","ORDINARY-MATTER","OUR-CASE-IS-M-ZERO","PACKAGING-IS-FREE","PERMISSION-NOT-DISCOUNT","PHASE-1-CLOSES","PLANCK-FACTOR-CANCELS","PLANCK-FOURTH-TIME","PLANCK-THIRD-TIME","POWER-MAKES-IT-WORSE","PRESSURE-CAPPED","PRINCIPLED-VS-BUILDABLE","PROPER-IS-THE-ACT","PROPER-IS-THE-QUANTITY","QNEC-HAS-NO-WEYL","QNEC-IS-THE-MEETING","RELIC-NOT-CONSTRUCTION","RIGIDITY-DERIVES-THE-EXOTIC","SAFE-MEANS-INVISIBLE","SAME-2PI2-AGAIN","SAVING-DOESNT-SCALE","SCALE-THEOREM","SCOPE-DROPS-LEAD","SEARCH-NEEDS-NO-DETECTOR","SEAT-IS-OBSERVED","SEAT-IS-THE-ESCAPE","SEAT-VS-CONTRACTION","SEATS-AND-EARLY","SECOND-COSTS-1E4-SUNS","SHEAR-CLAIM-INVERTED","SHELL-IS-ORDINARY","SHELL-THEOREM-SPLIT","SHIFTED-MODE","SHORTCUT-NOT-ROOM","SIGN-IS-THE-ONLY-QUESTION","SIGN-NOT-POWER","SIGN-STRUCTURE-3","SIGNBLIND-BOTH-ENDS","SIGNBLIND-PAIRS","SINGULARITY-NO-ESCAPE","SLINGSHOT","SMALLER-HOLDS-MORE","SNEC-INHERITS-ANEC","SPACE-TIME-ONE","STABLE-FOR-FREE","STANDING-COUPLING","STATE-NOT-ELEMENT","STATIC-IS-THE-SPLIT","STIFF-WALL","STIFFNESS-IS-THE-COST","STURM-IMPLIES-COLLAPSE","SUPERSESSION-SWEEP","SYMMETRY-BEATS-CODE","TARGET-ISNT-DESIGN","THE-DICHOTOMY","THE-DOOR","THE-SPLIT","THE-TRADE","THE-WINDOW","THEOREM-IS-FREE","THEOREM-REPRODUCES","THREE-ARE-ONE","THREE-CROSSINGS-AGREE","THREE-ROWS-ADMIT","THREE-WANT-A-THROAT","THROAT-IS-A-BOTTLENECK","THROAT-WANTS-LARGE","THUE-MORSE-IS-THE-CODE","TIME-CHEAPER-METRIC","TIME-HALF-IS-FREE","TRANSITION-DEFINED","TRANSITION-EQUATION","TWENTY-NOT-65-ORDERS","TWO-CONSTANTS-AGREE","TWO-INSTRUMENTS-LOCKED","TWO-ROUTES-AGREE","TWO-SYMMETRIES","TYPE-IV","UNIVERSAL-SEAT","VACUUM-DEMONSTRATION","VACUUM-FORCES-WEYL","VACUUM-NOT-MATERIAL","VACUUM-PATH","VACUUM-SATURATES-QNEC","VALUE-IS-AMORTISED","WEYL-IS-SIGNBLIND","WINDOW-GROWS","ZERO-ADM-DEVICE","ZERO-POINT-IS-THE-FLOOR","ZERO-SEPARATION-IS-ONE-FACT"]))
    aff = [f[0] for f in FINDINGS if coords(f) == (1,1,1)]
    chk("cells affirmative on all three", sorted(aff), sorted([
                "ABSORB-VS-TRANSMIT","ALREADY-LARGE-ENOUGH","ANEC-CROSS-CHECKED","BH-IS-WRONG-SIGN","BINARY-IS-A-FUNCTION","BOTH-SIGNS-SEAT-FREE","BUILT-SOURCE","CASIMIR-ROUTE","CATALOGUE","CHANGE-OF-KIND","CHARGE-PAIRS-MASS-DOESNT","CLASSICAL-WINS","COLLAPSE-BINDS-RICCI","CONCENTRIC-BEATS-BONDI","CONTAINER-IS-SOLVED","CONTRACTION-LAW","CORE-IS-TYPE-I","CORES-REPRODUCE-RATE","CORRIDOR-NOT-A-BH","COST-DOES-NOT-CLOSE-IT","COST-IS-ONE-NUMBER","COST-STOPS-SCALING","CREATE-IS-NOT-CONTAIN","D-CANCELS","DAMPING-READS-B-PRIME","DESIGN-EQUATION","DEVICE-IS-CLASSICAL","DEVICE-NOT-RETRACTED","DISSENT-IS-VALUE","EARNSHAW-CLOSES-L1","EC-TAKEN","EM-IS-ORDINARY","ENLARGE-DONT-CREATE","ENTANGLEMENT-IS-IT","ENTROPY-IS-PLANCK-DENOMINATED","ESCAPES-TYPE-I","EXTERNAL-PATH-ESCAPE","FLYBY","FOCUS-DESCRIPTION-STANDS","FORD-ROMAN-DERIVED","GATE-FAILS-D2","GATE-WINS","GJW-IS-EXISTENCE-PROOF","INSTRUMENT-LIMIT","KERR-FLYBY","KNOBS-DECOUPLE","LENSING-IS-THE-SEAT","LIMIT-DISSOLVES","LOG-COORDINATE","LONG-AND-WEAK","LOOP-OBSERVABLE","MAGNITUDE-REACHED","NEUTRAL-IS-THE-CEILING","NO-ACHRONAL-VIOLATOR","NO-BUCHDAHL","NO-EXOTIC","NO-HORIZON","NO-MOMENTUM-FLUX","NO-NULL-QI","NO-PHOTON-SPHERE","NO-THROAT","NOT-POWERED","NOTHING-STRUCTURAL","OBSERVED-ENGINE","ONE-SIGN-EXOTIC","ORDER-MOVED","ORDINARY-MATTER","PLANCK-FACTOR-CANCELS","PLANCK-FOURTH-TIME","PLANCK-THIRD-TIME","PRESSURE-CAPPED","PRINCIPLED-VS-BUILDABLE","PROPER-IS-THE-ACT","PROPER-IS-THE-QUANTITY","QNEC-IS-THE-MEETING","RELIC-NOT-CONSTRUCTION","RIGIDITY-DERIVES-THE-EXOTIC","SAME-2PI2-AGAIN","SCALE-THEOREM","SCOPE-DROPS-LEAD","SEARCH-NEEDS-NO-DETECTOR","SEAT-IS-OBSERVED","SEAT-IS-THE-ESCAPE","SEAT-VS-CONTRACTION","SEATS-AND-EARLY","SHEAR-CLAIM-INVERTED","SHELL-IS-ORDINARY","SHELL-THEOREM-SPLIT","SHIFTED-MODE","SHORTCUT-NOT-ROOM","SIGN-IS-THE-ONLY-QUESTION","SIGN-STRUCTURE-3","SIGNBLIND-BOTH-ENDS","SIGNBLIND-PAIRS","SLINGSHOT","SMALLER-HOLDS-MORE","SPACE-TIME-ONE","STABLE-FOR-FREE","STANDING-COUPLING","STATE-NOT-ELEMENT","STATIC-IS-THE-SPLIT","STIFF-WALL","SUPERSESSION-SWEEP","THE-DOOR","THE-SPLIT","THE-WINDOW","THEOREM-IS-FREE","THEOREM-REPRODUCES","THREE-CROSSINGS-AGREE","THREE-ROWS-ADMIT","THUE-MORSE-IS-THE-CODE","TIME-CHEAPER-METRIC","TIME-HALF-IS-FREE","TRANSITION-DEFINED","TRANSITION-EQUATION","TWENTY-NOT-65-ORDERS","TWO-CONSTANTS-AGREE","TWO-INSTRUMENTS-LOCKED","TWO-ROUTES-AGREE","TWO-SYMMETRIES","UNIVERSAL-SEAT","VACUUM-DEMONSTRATION","VACUUM-FORCES-WEYL","VACUUM-NOT-MATERIAL","VACUUM-PATH","VACUUM-SATURATES-QNEC","VALUE-IS-AMORTISED","WEYL-IS-SIGNBLIND","WINDOW-GROWS","ZERO-ADM-DEVICE","ZERO-SEPARATION-IS-ONE-FACT"]))
    shell = [f[0] for f in FINDINGS if f[0] in ("T1-STATE","SCALE","CIRCULATION")]
    chk("shell family is silent on Y", {coords(f)[1] for f in FINDINGS
        if f[0] in shell}, {0})

    print("\nCoverage -- the guard against looping")
    here = os.path.dirname(os.path.abspath(__file__))
    cited = {f[4] for f in FINDINGS} | {s[1] for s in SUPPORT}
    papers = sorted(os.path.basename(q) for q in glob.glob(os.path.join(here, "*.md")))
    uncited = [d for d in papers if d not in cited]
    ok &= (uncited == [])
    print("  %-58s %14s" % ("papers with no cell (must be empty)", uncited if uncited else "[]"))
    print("  %-58s %14s %14s  %s" % ("every paper is indexed", not uncited, True,
                                     "ok" if not uncited else "FAIL"))
    print("""  A finding the index does not hold cannot be predicted by its own closure.
  E(X) = 0 over an incomplete X measures the bookkeeping, not the knowledge --
  which is exactly how ROTATING-SHELL's J result was walked past and rederived.""")

    print("\nCompleteness (2.25.6)")
    cells = {coords(f) for f in FINDINGS}
    E, pred = defect(cells)
    chk("cells the closure demands, excluding the null", pred, [])
    chk("E(X) = 0 -- the index is complete", E, 0)
    chk("null cell is demanded (lattice bottom, declared not a finding)",
        NULL in closure(cells), True)
    chk("a complete index makes no predictions", E == 0, True)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE PROJECT AS A CLOSED INDEX ON ITS OWN THREE DIRECTIVES")
    print("="*78)
    for i, a in enumerate(AXES):
        print("   %s" % a)
    print("\n   +1 affirmative    0 silent    -1 a bound (P8: still an answer)\n")
    print("  %-12s %3s %3s %3s  %s" % ("cell","X","Y","Z","claim"))
    print("  " + "-"*74)
    for f in sorted(FINDINGS, key=lambda g: (-sum(1 for v in coords(g) if v!=0), g[0])):
        mark = "  <== all three" if on_all_three(f) else ""
        print("  %-12s %+3d %+3d %+3d  %s%s" % (f[0], f[1], f[2], f[3], f[5][:52], mark))

    print("\n-- Cells sitting on all three axes (2.17.3: a coordinate) ------------------")
    for f in FINDINGS:
        if on_all_three(f):
            print("   %-12s (%+d,%+d,%+d)  %s" % (f[0], f[1], f[2], f[3], f[5][:56]))

    print("\n-- Affirmative on all three: the answer ------------------------------------")
    tgt = (1,1,1)
    hits = [f for f in FINDINGS if coords(f) == tgt]
    for f in hits:
        print("   %-12s %s" % (f[0], f[5]))
        print("   %-12s source: %s" % ("", f[4]))
    print("\n   Supporting points (Hamming-1 neighbours, each supplying one coordinate):")
    for f in neighbours(tgt, FINDINGS):
        z = [i for i,(p,q) in enumerate(zip(coords(f), tgt)) if p!=q][0]
        print("     %-12s (%+d,%+d,%+d)  differs on %s" % (f[0], f[1], f[2], f[3], AXES[z].split(':')[0]))

    print("\n-- Where the shell family sits ---------------------------------------------")
    for f in FINDINGS:
        if f[0] in ("T1-STATE","SCALE","CIRCULATION","T2-ADM"):
            print("   %-12s (%+d,%+d,%+d)  %s" % (f[0], f[1], f[2], f[3], f[5][:56]))
    print("""
   T1-STATE, SCALE and CIRCULATION are all (+1, 0, +1): complete on X and Z,
   EMPTY ON Y.  Fifteen papers filled in what warp energy is and what the object
   would look like, and never once occupied the middle axis.  T2-ADM then fills
   that hole with -1.  The shell family reads: we know what it is, we know what
   it would be made of, and it cannot be a drive.""")

    cells = {coords(f) for f in FINDINGS}
    E, pred = defect(cells)
    print("\n-- Completeness -------------------------------------------------------------")
    print("   |X| = %d occupied   |R(X)| = %d   E(X) = %d   (null cell declared, not a finding)"
          % (len(cells), len(closure(cells)), E))
    print("""   2.25.6: the number of predictions an index can make is E(X), and a complete
   index makes none.  E = 0 here, so THE INDEX DEMANDS NO FURTHER FINDING.  It
   got there by demanding four and having each one turn out to exist already,
   buried inside an entangled result: CM-THEOREM, NO-EXOTIC, FREE-FALL, PROFILE.
   Every one was real and none was new physics.  That is the finding about the
   METHOD of this project -- it produces entangled results, and the index keeps
   asking for them disentangled.""")

    jf, mf = closure_failures({coords(f) for f in FINDINGS})
    print("\n-- Closure ------------------------------------------------------------------")
    print("   join failures %d   meet failures %d   occupied %d of 27 cells"
          % (jf, mf, len({coords(f) for f in FINDINGS})))
    print("""   Exactly Law 3 (Chapter 36): three coupled axes are K_3, needing strong
   3-consistency where the closure operator delivers 2.  The join closes; the
   meet does not.  Certainty survives upward and dies downward -- so this index
   may say what the project CANNOT FAIL to have shown, and may not refine to a
   single point.  The defect is not a fault in the index; it is the shape of
   three-ness, and the corpus measured it before this project existed.""")

    print("\n-- Support points (correct other cells; answer no directive) ----------------")
    for s in SUPPORT:
        print("   %-12s %s" % (s[0], s[2]))
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
