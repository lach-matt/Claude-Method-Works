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
  "MEASURED: M = -2e-3 gives a conjugate point at lambda 56.5 AND arrives early (-3.76e-2), while +2e-3 seats at 55.2 and arrives late. Both signs seat; only the arrival flips"),
 ("THE-WINDOW",      +1, +1, +1, "composite.py",
  "bounded on both sides: below, the focal length exceeds the run and it does not seat; above, the M^2 path lengthening beats the linear Shapiro. About a decade wide at b=0.3, L=75"),
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
 ("DEVICE-SEATS-LEADS",+1,+1,+1, "concentric.py",
  "MEASURED: it seats and leads over m = 5e-3 to 4e-2, most of a decade, conjugate point 228.45 +- 0.04 over a sixfold refinement, best relative lead -6.0e-4"),
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
 ("LEDGER",          0, -1,  0, "obstruct.py",
  "of twenty-four obstructions six dissolved, three relocated, nine closed negative, four conditional, two open and none untested"),
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
    chk("number of findings indexed", len(FINDINGS), 212)
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
        ['ACHRONAL', 'ANEC-VIOLATED', 'CHARGE-NO-LEAD', 'GAP-WIDENS', 'NO-ACHIEVABLE-CORE', 'TYPE-IV'])
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
                "ACHRONAL","ANEC-VIOLATED","AREA-OVER-THICK","BUILT-SOURCE","CASIMIR-ROUTE",
                "CATALOGUE","CHANGE-OF-KIND","CHARGE-NO-LEAD","CLASSICAL-WINS","CORE-IS-TYPE-I",
                "D-CANCELS","DESIGN-EQUATION","DEVICE-IS-CLASSICAL","DEVICE-NOT-RETRACTED",
                "DEVICE-SEATS-LEADS","EC-TAKEN","EM-GAP","EM-IS-ORDINARY","ESCAPES-TYPE-I",
                "FLYBY","GAP-WIDENS","KERR-FLYBY","LAUNCHER","LENSING-IS-THE-SEAT",
                "LIMIT-DISSOLVES","LOG-COORDINATE","LONG-AND-WEAK","LOOP-OBSERVABLE",
                "MAGNITUDE-REACHED","NO-ACHIEVABLE-CORE","NO-BUCHDAHL","NO-EXOTIC","NO-NULL-QI",
                "OBJ-CEILING","OBSERVED-ENGINE","ONE-AXIS-FLAT","ONE-SIGN-EXOTIC","OPEN-GATE",
                "ORDINARY-MATTER","PLANCK-THIRD-TIME","PRESSURE-CAPPED","SCOPE-DROPS-LEAD",
                "SEATS-AND-EARLY","SHELL-IS-ORDINARY","SHELL-THEOREM-SPLIT","SIGN-STRUCTURE-3",
                "SLINGSHOT","STABLE-FOR-FREE","STATE-NOT-ELEMENT","STIFF-WALL",
                "STURM-IMPLIES-COLLAPSE","THE-DOOR","THE-SPLIT","THE-TRADE","THE-WINDOW",
                "THEOREM-IS-FREE","TWO-ROUTES-AGREE","TYPE-IV","UNIVERSAL-SEAT",
                "VACUUM-FORCES-WEYL","VACUUM-NOT-MATERIAL","VACUUM-PATH","WEYL-IS-SIGNBLIND",
                "ZERO-ADM-DEVICE"]))
    aff = [f[0] for f in FINDINGS if coords(f) == (1,1,1)]
    chk("cells affirmative on all three", sorted(aff), sorted([
                "BUILT-SOURCE","CASIMIR-ROUTE","CATALOGUE","CHANGE-OF-KIND","CLASSICAL-WINS",
                "CORE-IS-TYPE-I","D-CANCELS","DESIGN-EQUATION","DEVICE-IS-CLASSICAL",
                "DEVICE-NOT-RETRACTED","DEVICE-SEATS-LEADS","EC-TAKEN","EM-IS-ORDINARY",
                "ESCAPES-TYPE-I","FLYBY","KERR-FLYBY","LENSING-IS-THE-SEAT","LIMIT-DISSOLVES",
                "LOG-COORDINATE","LONG-AND-WEAK","LOOP-OBSERVABLE","MAGNITUDE-REACHED",
                "NO-BUCHDAHL","NO-EXOTIC","NO-NULL-QI","OBSERVED-ENGINE","ONE-SIGN-EXOTIC",
                "ORDINARY-MATTER","PLANCK-THIRD-TIME","PRESSURE-CAPPED","SCOPE-DROPS-LEAD",
                "SEATS-AND-EARLY","SHELL-IS-ORDINARY","SHELL-THEOREM-SPLIT","SIGN-STRUCTURE-3",
                "SLINGSHOT","STABLE-FOR-FREE","STATE-NOT-ELEMENT","STIFF-WALL","THE-DOOR",
                "THE-SPLIT","THE-WINDOW","THEOREM-IS-FREE","TWO-ROUTES-AGREE","UNIVERSAL-SEAT",
                "VACUUM-FORCES-WEYL","VACUUM-NOT-MATERIAL","VACUUM-PATH","WEYL-IS-SIGNBLIND",
                "ZERO-ADM-DEVICE"]))
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
