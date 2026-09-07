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
 # The narrowing stationkeep.py applied here is WITHDRAWN with the theorem that
 # motivated it.  The identity was never in question; the mission is back.
 ("CATALOGUE",   +1, +1, +1, "person.py",
  "a person at 50 Msun and a proton at 1.2e9 kg are the SAME mission: the deflector is catalogued"),
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
    chk("number of findings indexed", len(FINDINGS), 57)
    chk("distinct occupied cells", len({coords(f) for f in FINDINGS}), 14)
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
    chk("cells sitting on all three axes", sorted(triple),
        sorted(["EM-GAP","FLYBY","SLINGSHOT","LAUNCHER","OPEN-GATE","OBJ-CEILING","KERR-FLYBY",
                "OBSERVED-ENGINE","CATALOGUE"]))
    aff = [f[0] for f in FINDINGS if coords(f) == (1,1,1)]
    chk("cells affirmative on all three", sorted(aff),
        sorted(["FLYBY","SLINGSHOT","KERR-FLYBY","OBSERVED-ENGINE","CATALOGUE"]))
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
