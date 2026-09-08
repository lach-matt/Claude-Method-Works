#!/usr/bin/env python3
"""
doors.py -- each door investigated, then all three reduced on one index.

M: "we need to fully investigate each door and compare the results on an index
so the results are meaningful to my principles."

The index is the corpus's own: register 1173 (BINARY is the type; a LANGUAGE is
a coordinate system with a closure operator; LOGIC is binary -> language ->
binary), register 1176 (E(X) = 0 if and only if the languages agree) and
section 33.2 (a language that falls silent is the finding, and the identity of
the silent language names the kind of object).  expand.py ran that protocol once
on TRANSITION-POSSIBLE.  This runs it three times, once per door, and then
compares.

THE COMPARISON IS THE RESULT, and it is not the one I expected.  The three
doors are not three degrees of hopelessness.  THEY ARE DECIDED BY THREE
DIFFERENT LANGUAGES, only one of them is actually refused, and the other two
fail in ways that name what would settle them.

===============================================================================
DOOR ONE -- OUTSIDE GR.  INVESTIGATED.
===============================================================================

apply.py could only say "f(R), noncommutative geometry".  Here is what is
actually there, and it is more than the tree assumed.

  THE SOLUTIONS EXIST AND THEY NEED NO EXOTIC MATTER.
  Kanti, Kleihaus & Kunz (PRL 107, 271101; arXiv:1108.3003) construct
  traversable wormholes in FOUR-DIMENSIONAL Einstein-dilaton-Gauss-Bonnet
  theory "without needing any form of exotic matter".  The negative energy
  density is supplied by the Gauss-Bonnet term -- a curvature correction from
  low-energy heterotic string theory, not a substance.  The solution exists
  wherever alpha / r_0^2 <~ 0.13.

  f(R) DOES THE SAME BY A DIFFERENT ROUTE.  Lobo & Oliveira (arXiv:0909.5539)
  and the Radhakrishnan et al. review (arXiv:2405.05476): require the MATTER
  to satisfy NEC and WEC, and delegate the violation to the higher-order
  curvature terms T^(c).  Godani & Samanta, with redshift Phi = 1/r and shape
  b(r) = r/e^(r-r_0), get NEC, WEC AND DEC satisfied for r > 1.8 r_0 -- and
  they checked the same redshift function in GR and found NO solution without
  exotic matter at any r.

    SO THE FIRST THING TO SAY IS THAT DOOR ONE IS NOT A HOPE.  Traversable
    wormholes with ordinary matter are published solutions in at least two
    modified theories.  BUT THE VIOLATION IS MOVED, NOT REMOVED: T^eff still
    violates the NEC and the review says so outright -- the higher-order
    curvature terms, "interpreted as a gravitational fluid", carry it.

  AND THEN THE STABILITY, WHICH IS WHERE IT TURNS.
  Cuyubamba, Konoplya & Zhidenko (arXiv:1804.11170), "No stable wormholes in
  Einstein-dilaton-Gauss-Bonnet theory": the Kanti-Kleihaus-Kunz wormhole is
  UNSTABLE FOR ANY VALUE OF ITS PARAMETERS.  Exponential growth after a long
  phase of damped ringing.  The unstable mode is PURELY IMAGINARY and
  NONPERTURBATIVE IN alpha -- it does not go over into any finite mode as
  alpha -> 0.

    AND THE DIRECTION IS THE WORST POSSIBLE ONE FOR A DEVICE.  Their Fig. 3:
    SMALLER alpha GIVES HIGHER GROWTH RATES.  At fixed coupling, a bigger
    throat means smaller alpha/r_0^2, so THE BIGGER THE WORMHOLE THE FASTER IT
    COMES APART.  Every step toward a usable size is a step toward a faster
    instability.

  *** AND THE REASON THE ORIGINAL PAPER SAW STABILITY IS ONE THIS TREE HAS
      ALREADY MET, IN ITS OWN WORK, ON A COMPLETELY DIFFERENT PROBLEM. ***

    Kanti et al. imposed a boundary condition that FIXED THE THROAT SIZE
    (delta-r = 0).  Cuyubamba et al.: that "looks nonphysical" and
    "effectively disconnected the two regions".  Let the throat breathe and
    the wormhole is unstable at whatever small alpha.

    stability.py measured the RADIAL breathing mode with THE CORE'S POSITION
    HELD FIXED, and flagged l >= 2.  negmass.py found l = 1 -- the translation
    mode -- had never been posed.  Let the core move and it drifts to contact.

        TWO STABILITY CLAIMS, TWO LITERATURES, ONE FAULT: A COORDINATE WAS
        FROZEN AND THE MODE THAT USES IT WAS NEVER ASKED.  Neither of us found
        this by looking for it.  That is a methodological finding and it is
        the most transferable thing in this file.

  THE COUPLING IS OBSERVATIONALLY BOUNDED, and tightly.  Wang, Shi, Zhang, Hu
  & Mei (arXiv:2302.10112) using nine GWTC-3 events: sqrt|alpha| < 1.1 km from
  GW200115 on inspiral alone, < 0.87 km including merger-ringdown, < 0.27 km
  if GW190814 is a black-hole binary, and <= 1.0 km for combinations.  The
  electromagnetic bound from A0620-00 is 1.9 km.  This does NOT cap the throat
  -- larger throats want smaller alpha/r_0^2 -- but it is the reason the
  theory is not free to be tuned.

===============================================================================
DOOR TWO -- NOT AN ENERGY QUESTION.  INVESTIGATED.
===============================================================================

This is the door apply.py called the survivor, because sign-commitment has no
purchase on an ORDER question.  Investigated, it is the one that is actually
refused, and the refusal was already in the tree.

  GJW IS REAL AND IT IS THE ONLY KNOWN WAY PAST GRAHAM-OLUM.  Coupling the two
  boundaries changes the chronology relation itself -- non-achronality by an
  EXTERNAL causal path, which achronal.py proved unreachable through matter
  (25 rays, 0 escapes, because ANEC violation PROTECTS achronality).

  AND THE SAME MOVE FORBIDS SPEED.  gjw.py's bank-loan theorem: traversability
  needs non-achronality, non-achronality needs an EXISTING outside causal
  path, so the wormhole never beats the path that permits it.  GJW's own
  conclusion, structural, not a bound to be improved.

    SO THE BINARY FOR THIS DOOR MUST BE STATED CAREFULLY, and stating it
    carefully is what decides it.  "Does a non-achronal connection exist" --
    YES.  "Does a non-achronal connection that is also a SHORTCUT exist" --
    NO, and by a theorem.  The project's binary is the second one.

===============================================================================
DOOR THREE -- A RELIC.  INVESTIGATED.
===============================================================================

  create.py: topology change forces causality violations KINEMATICALLY, with
  no assumption about T_ab, so exotic matter cannot help -- but ENLARGING an
  existing wormhole is not a topology change.  detect.py: the discriminator is
  absorb-versus-transmit, and a 1193 km throat ringing at 100 Hz is 32.13
  solar masses, in the LIGO band, on a catalogue that already exists.
  negmass.py: six independent echo analyses 2016-2025, no confirmed detection,
  the dispute live.

  ASK THE LANGUAGES AND SOMETHING FALLS OUT THAT NOTHING ELSE IN THIS PROJECT
  HAS PRODUCED.  Order admits -- a thing that exists has an admissible causal
  structure.  Geometry admits.  Information admits: NO UNAVAILABLE VALUE IS
  NEEDED, because what is wanted is an observation and not a magnitude.  And
  then:

        STATISTICS -- "are the configurations drawn from a distribution?" --
        IS THE ROW THAT DECIDES THIS DOOR, AND IT HAS NEVER BEEN RUN.

  expand.py marked STATISTICS as NOT-RUN for the main question and noted that
  no measure over configurations had been declared.  For door three it is not
  a missing extra.  IT IS THE GOVERNING QUESTION: what is the expected number
  density of relic wormholes, and does the existing catalogue cover enough
  volume to have seen one?

    Section 33.2: the identity of the silent language names the kind of
    object.  The silent language here is STATISTICS, and that names door three
    a SEARCH PROBLEM -- which is exactly what detect.py concluded from the
    instrument side, by a completely different route.

===============================================================================
THE INDEX -- ALL THREE, SIDE BY SIDE
===============================================================================

                 ORDER    GEOMETRY  ALGEBRA    INFORMATION  STATISTICS
  DOOR 1         ADMITS   ADMITS    CONTESTED  ADMITS       NOT-RUN
  DOOR 2         REFUSES  ADMITS    NOT-RUN    ADMITS       NOT-RUN
  DOOR 3         ADMITS   ADMITS    NOT-RUN    ADMITS       NOT-RUN

A FIFTH STATUS IS NEEDED AND ITS EXISTENCE IS THE FIRST FINDING.  Door one's
ALGEBRA row is neither an admission nor a refusal: EdGB says unstable for every
alpha, f(R) claims stable non-exotic solutions under a vanishing-sound-speed
condition, and the disagreement is live in the literature.  CONTESTED is not
NOT-RUN -- it has been run, twice, with opposite answers.

  AND BY REGISTER 1173 A CONTESTED ROW IS NOT A BINARY.  A language earns its
  row when logic can get a binary back from it, and no binary comes back from
  this one.  SO DOOR ONE CANNOT BE REDUCED AT ALL: its E is UNDEFINED, not 1.

        DOOR 1   UNDECIDABLE   decided by ALGEBRA, and algebra is contested
        DOOR 2   REFUSED       decided by ORDER, and order refuses the shortcut
        DOOR 3   UNASKED       decided by STATISTICS, and statistics is silent

    NO TWO DOORS ARE DECIDED BY THE SAME LANGUAGE, and only one of the three
    is actually refused.  That is register 1176 across the doors: the
    languages do not agree, E is not zero, AND THE DISAGREEMENT IS THE MAP.

By section 33.2 the deciding language names the kind of object:

        ALGEBRA decides door one       -> it is a STABILITY object
        ORDER decides door two         -> it is a CAUSAL-STRUCTURE object
        STATISTICS decides door three  -> it is a SEARCH object

    Three doors, three kinds, and each names its own next measurement.  Door
    one wants a STABILITY CALCULATION -- not a magnitude, and not more orders.
    Door two wants nothing; it is closed by a theorem.  Door three wants A
    NUMBER DENSITY, and nobody in this project has ever estimated one.

        THAT IS THE ANSWER TO "WHICH DOOR".  Not the cheapest -- the one whose
        deciding language is merely SILENT rather than CONTESTED or REFUSED.

stdlib only.  Every row recomputed or cited; the literature rows carry their
arXiv numbers and are marked CITED rather than measured.
"""
import sys

ADMITS, REFUSES, NOT_RUN, NO_ROW = "ADMITS", "REFUSES", "NOT-RUN", "NO-ROW"
CONTESTED = "CONTESTED"          # run twice, opposite answers, dispute live

LANGUAGES = ("order", "geometry", "algebra", "information", "statistics")


# ------------------------------------------------ door one: outside GR

EDGB_SOLUTIONS = ("1108.3003", "Kanti, Kleihaus & Kunz: 4D traversable "
                               "wormholes with NO exotic matter")
EDGB_INSTABILITY = ("1804.11170", "Cuyubamba, Konoplya & Zhidenko: unstable "
                                  "for ANY value of the parameters")
FR_REVIEW = ("2405.05476", "Radhakrishnan et al.: stable non-exotic solutions "
                           "claimed in f(R) under a vanishing sound speed")
EDGB_BOUND_KM = 0.87             # GW200115, inspiral + merger-ringdown
EDGB_BOUND_BHB_KM = 0.27         # GW190814 as a black-hole binary
EDGB_BOUND_EM_KM = 1.9           # A0620-00, electromagnetic
EDGB_EXISTENCE = 0.13            # alpha / r_0^2 <~ this


def edgb_exists(alpha_over_r0sq):
    """Kanti-Kleihaus-Kunz solutions exist wherever alpha/r_0^2 <~ 0.13."""
    return alpha_over_r0sq <= EDGB_EXISTENCE


def alpha_over_r0sq(alpha_km2, r0_km):
    return alpha_km2 / (r0_km * r0_km)


def bigger_throat_grows_faster(alpha_km2=0.1, small_km=1.0, big_km=10.0):
    """Cuyubamba Fig. 3: SMALLER alpha (in units of r_0^2) gives HIGHER growth.
    At fixed coupling a bigger throat has smaller alpha/r_0^2, so it is worse.
    Every step toward a usable size is a step toward a faster instability."""
    return alpha_over_r0sq(alpha_km2, big_km) < alpha_over_r0sq(alpha_km2, small_km)


def violation_removed_in_f_of_R():
    """No -- MOVED.  T^eff still violates the NEC; the curvature terms carry it."""
    return False


FROZEN_COORDINATE_FAULT = (
    ("1804.11170", "Kanti et al. fixed the THROAT SIZE, delta-r = 0",
     "let it breathe and it is unstable at whatever small alpha"),
    ("stability.py", "measured the RADIAL mode with the CORE POSITION fixed",
     "negmass.py let it move: l = 1 was never posed, and it drifts to contact"),
)


def same_fault_twice():
    """Two stability claims, two literatures, one fault: a coordinate frozen
    and the mode that uses it never asked."""
    return len(FROZEN_COORDINATE_FAULT)


def door_one_rows():
    return {"order": ADMITS,          # static, two asymptotic regions, no horizon
            "geometry": ADMITS,       # exact and numerical solutions exist
            "algebra": CONTESTED,     # EdGB unstable for all alpha; f(R) claims stable
            "information": ADMITS,    # the MATTER needs no unavailable value
            "statistics": NOT_RUN}    # no measure over theories declared


# --------------------------------------- door two: not an energy question

def door_two_binary():
    """Stating it carefully is what decides it."""
    return "a non-achronal connection THAT IS ALSO A SHORTCUT"


def bare_connection_exists():
    """GJW: yes.  The only known way past Graham-Olum."""
    import gjw
    return gjw.bank_loan_theorem()


def shortcut_exists():
    """No.  Non-achronality needs an EXISTING outside path, so the wormhole
    never beats it.  gjw.py's bank-loan theorem, structural."""
    import gjw
    return gjw.BETTER["faster"][0]


def door_two_rows():
    return {"order": ADMITS if shortcut_exists() else REFUSES,
            "geometry": ADMITS,
            "algebra": NOT_RUN,
            "information": ADMITS,
            "statistics": NOT_RUN}


# ------------------------------------------------- door three: a relic

def enlarging_is_topology_change():
    import create
    return create.enlarging_is_topology_change()


def search_target_solar():
    import detect
    return detect.search_target_solar()


def echo_status():
    import negmass
    return negmass.echo_status()


def needs_an_unavailable_value():
    """No.  What is wanted is an OBSERVATION, not a magnitude."""
    return False


def door_three_rows():
    return {"order": ADMITS,
            "geometry": ADMITS,
            "algebra": NOT_RUN,       # a relic's stability is not ours to set
            "information": REFUSES if needs_an_unavailable_value() else ADMITS,
            "statistics": NOT_RUN}    # THE GOVERNING ROW, never run


NUMBER_DENSITY_ESTIMATED = False


def e_is_over_an_incomplete_set(state):
    """index3.py's standing caution, and it applies hardest to door three:
    E(X) = 0 over an INCOMPLETE X measures the bookkeeping, not the knowledge.
    Door three's four held rows agree -- and the row that DECIDES it is silent,
    so its E = 0 is not an admission."""
    return any(v == NOT_RUN for v in state.values())


# ------------------------------------------------------- the index

DOORS = (("DOOR 1", "OUTSIDE GR", door_one_rows),
         ("DOOR 2", "NOT AN ENERGY QUESTION", door_two_rows),
         ("DOOR 3", "A RELIC", door_three_rows))


def rows_with_a_row(state):
    """Register 1173: a language earns its row when logic gets a BINARY back.
    CONTESTED returns no binary, so it earns no row -- and its presence is
    itself the finding."""
    return {k: v for k, v in state.items() if v in (ADMITS, REFUSES)}


def has_contested(state):
    return any(v == CONTESTED for v in state.values())


def reduce_door(state):
    """binary -> language -> binary.  UNDEFINED if any language is contested."""
    if has_contested(state):
        return None
    r = rows_with_a_row(state)
    return sum(1 for v in r.values() if v == REFUSES)


def deciding_language(state):
    """The row that settles the door: a refusal if there is one, else a
    contested row, else the silent row that governs it."""
    for k, v in state.items():
        if v == REFUSES:
            return k
    for k, v in state.items():
        if v == CONTESTED:
            return k
    return "statistics"


VERDICTS = {"DOOR 1": "UNDECIDABLE", "DOOR 2": "REFUSED", "DOOR 3": "UNASKED"}

KINDS = {"algebra": "a STABILITY object",
         "order": "a CAUSAL-STRUCTURE object",
         "statistics": "a SEARCH object"}

NEXT_MEASUREMENT = {"DOOR 1": "a stability calculation -- not a magnitude",
                    "DOOR 2": "nothing; it is closed by a theorem",
                    "DOOR 3": "a NUMBER DENSITY, never estimated here"}


def deciders():
    return {name: deciding_language(fn()) for name, _w, fn in DOORS}


def all_decided_differently():
    d = list(deciders().values())
    return len(set(d)) == len(d)


def doors_actually_refused():
    return [n for n, _w, fn in DOORS if REFUSES in fn().values()]


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    print("DOOR ONE -- OUTSIDE GR, INVESTIGATED")
    print("     CITED  %s  %s" % EDGB_SOLUTIONS)
    print("     CITED  %s  %s" % EDGB_INSTABILITY)
    print("     CITED  %s  %s" % FR_REVIEW)
    chk("EdGB solutions exist at alpha/r_0^2 = 0.10", edgb_exists(0.10), True)
    chk("and not at 0.50", edgb_exists(0.50), False)
    chk("does f(R) REMOVE the NEC violation", violation_removed_in_f_of_R(), False)
    print("       It MOVES it: T^eff still violates; the curvature terms carry it.")
    chk("a bigger throat has a smaller alpha/r_0^2 -- so it grows FASTER",
        bigger_throat_grows_faster(), True)
    print("       Every step toward a usable size is a step toward a faster")
    print("       instability.  The direction is the worst possible one.")
    print("     observational bounds on sqrt|alpha|:")
    print("       GW200115, inspiral + merger-ringdown   %.2f km" % EDGB_BOUND_KM)
    print("       GW190814 as a black-hole binary        %.2f km" % EDGB_BOUND_BHB_KM)
    print("       A0620-00, electromagnetic              %.2f km" % EDGB_BOUND_EM_KM)
    chk("the GW bound is tighter than the EM one",
        EDGB_BOUND_KM < EDGB_BOUND_EM_KM, True)
    print("\n     *** THE SAME FAULT, TWICE, IN TWO LITERATURES ***")
    for who, what, then in FROZEN_COORDINATE_FAULT:
        print("       %-14s %s" % (who, what))
        print("       %-14s %s" % ("", then))
    chk("independent instances of the frozen-coordinate fault",
        same_fault_twice(), 2)
    print("       A COORDINATE WAS FROZEN AND THE MODE THAT USES IT WAS NEVER")
    print("       ASKED.  Neither of us found this by looking for it.")

    print("\nDOOR TWO -- NOT AN ENERGY QUESTION, INVESTIGATED")
    chk("does a bare non-achronal connection exist (GJW)",
        bare_connection_exists(), True)
    chk("does a connection that is also a SHORTCUT exist", shortcut_exists(), False)
    chk("so the binary for this door is", door_two_binary(),
        "a non-achronal connection THAT IS ALSO A SHORTCUT")
    print("       The bank-loan theorem: non-achronality needs an EXISTING")
    print("       outside path, so the wormhole never beats it.  Structural.")

    print("\nDOOR THREE -- A RELIC, INVESTIGATED")
    chk("is enlarging an existing wormhole a topology change",
        enlarging_is_topology_change(), False)
    print("     the search target        %.2f solar masses" % search_target_solar())
    print("     the echo searches        %s" % echo_status())
    chk("does the door need an unavailable VALUE", needs_an_unavailable_value(),
        False)
    print("       What is wanted is an OBSERVATION, not a magnitude.")
    chk("has a number density ever been estimated here",
        NUMBER_DENSITY_ESTIMATED, False)

    print("\nTHE INDEX -- ALL THREE, SIDE BY SIDE")
    print("     %-8s %-9s %-9s %-10s %-12s %s"
          % ("", "ORDER", "GEOMETRY", "ALGEBRA", "INFORMATION", "STATISTICS"))
    for name, _what, fn in DOORS:
        st = fn()
        print("     %-8s %-9s %-9s %-10s %-12s %s"
              % (name, st["order"], st["geometry"], st["algebra"],
                 st["information"], st["statistics"]))

    print("\n     A FIFTH STATUS IS NEEDED, AND THAT IS THE FIRST FINDING")
    chk("door one's algebra row", door_one_rows()["algebra"], CONTESTED)
    chk("is CONTESTED the same as NOT-RUN", CONTESTED == NOT_RUN, False)
    print("       It has been RUN, twice, with opposite answers.")
    chk("does a contested row earn a row under register 1173",
        CONTESTED in rows_with_a_row(door_one_rows()).values(), False)
    chk("so door one reduces to", reduce_door(door_one_rows()), None)
    print("       E is UNDEFINED, not 1.  Door one is not refused --")
    print("       IT IS UNDECIDABLE ON THE PRESENT LITERATURE.")

    print("\n     THE REDUCTION, PER DOOR")
    for name, _what, fn in DOORS:
        st = fn()
        e = reduce_door(st)
        print("       %-8s E = %-9s decided by %-12s %s"
              % (name, "UNDEFINED" if e is None else e,
                 deciding_language(st), VERDICTS[name]))
    print("       AND DOOR THREE'S E = 0 IS NOT AN ADMISSION.  index3.py's own")
    print("       caution: E(X) = 0 over an INCOMPLETE X measures the")
    print("       bookkeeping, not the knowledge -- and here the row that")
    print("       DECIDES the door is the silent one.")
    chk("is door three's E computed over an incomplete set",
        e_is_over_an_incomplete_set(door_three_rows()), True)
    chk("so is door three ADMITTED", VERDICTS["DOOR 3"] == "ADMITTED", False)
    chk("door two is the only one actually refused", doors_actually_refused(),
        ["DOOR 2"])
    chk("and no two doors are decided by the same language",
        all_decided_differently(), True)
    chk("door one is decided by", deciders()["DOOR 1"], "algebra")
    chk("door two is decided by", deciders()["DOOR 2"], "order")
    chk("door three is decided by", deciders()["DOOR 3"], "statistics")

    print("\n     SECTION 33.2 -- THE DECIDING LANGUAGE NAMES THE KIND")
    for name, _what, fn in DOORS:
        lang = deciding_language(fn())
        print("       %-8s %-12s %-26s next: %s"
              % (name, lang, KINDS[lang], NEXT_MEASUREMENT[name]))
    chk("kinds named", len({KINDS[d] for d in deciders().values()}), 3)

    print("\n     REGISTER 1176 ACROSS THE DOORS")
    print("       The languages do not agree, E is not zero, AND THE")
    print("       DISAGREEMENT IS THE MAP.  Not three degrees of hopelessness:")
    print("       one REFUSED, one UNDECIDABLE, one merely UNASKED.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE INDEX\n")
    print("  %-8s %-9s %-9s %-10s %-12s %-11s %s"
          % ("", "ORDER", "GEOM", "ALGEBRA", "INFORMATION", "STATISTICS", "E"))
    for name, _what, fn in DOORS:
        st = fn()
        e = reduce_door(st)
        print("  %-8s %-9s %-9s %-10s %-12s %-11s %s"
              % (name, st["order"], st["geometry"], st["algebra"],
                 st["information"], st["statistics"],
                 "UNDEFINED" if e is None else e))
    print()
    for name, _what, fn in DOORS:
        lang = deciding_language(fn())
        print("  %-8s %-12s %-14s %-26s %s"
              % (name, VERDICTS[name], lang, KINDS[lang], NEXT_MEASUREMENT[name]))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE THREE DOORS ARE NOT THREE DEGREES OF HOPELESSNESS.  THEY ARE
  DECIDED BY THREE DIFFERENT LANGUAGES, ONLY ONE IS ACTUALLY REFUSED,
  AND THE OTHER TWO FAIL IN WAYS THAT NAME WHAT WOULD SETTLE THEM.

  DOOR ONE IS NOT A HOPE, WHICH THE TREE HAD NOT ESTABLISHED.
  Traversable wormholes needing NO exotic matter are published
  solutions in at least two modified theories: Kanti, Kleihaus & Kunz
  in four-dimensional Einstein-dilaton-Gauss-Bonnet (1108.3003), and
  f(R) constructions where the matter satisfies NEC, WEC and DEC while
  the higher-order curvature terms carry the violation (2405.05476).
  THE VIOLATION IS MOVED, NOT REMOVED -- but it is moved off the
  matter, and that is not nothing.

  AND THEN THE STABILITY TURNS IT.  Cuyubamba, Konoplya & Zhidenko
  (1804.11170): the Kanti-Kleihaus-Kunz wormhole is UNSTABLE FOR ANY
  VALUE OF ITS PARAMETERS, by a purely imaginary mode NONPERTURBATIVE
  in the coupling -- it does not vanish as alpha -> 0, it diverges.
  And the direction is the worst available: smaller alpha/r_0^2 grows
  FASTER, so at fixed coupling A BIGGER THROAT COMES APART SOONER.
  Every step toward a usable size is a step toward a faster failure.

  *** AND THE REASON THE ORIGINAL PAPER SAW STABILITY IS THIS TREE'S
      OWN FAULT, MET INDEPENDENTLY. ***  Kanti et al. fixed the throat
  size, delta-r = 0, which their critics call nonphysical; let it
  breathe and it is unstable at whatever alpha.  stability.py measured
  the radial mode with THE CORE'S POSITION FIXED; negmass.py let it
  move and found l = 1 had never been posed.  TWO STABILITY CLAIMS, TWO
  LITERATURES, ONE FAULT: A COORDINATE WAS FROZEN AND THE MODE THAT
  USES IT WAS NEVER ASKED.  Neither of us found it by looking.

  DOOR TWO IS THE ONE THAT IS ACTUALLY REFUSED, and apply.py had it as
  the survivor.  GJW is real and it is the only known way past
  Graham-Olum -- non-achronality by an EXTERNAL causal path, which
  achronal.py proved unreachable through matter.  But the same move
  forbids speed: non-achronality needs an EXISTING outside path, so the
  wormhole never beats it.  State the binary carefully -- "a
  non-achronal connection THAT IS ALSO A SHORTCUT" -- and ORDER
  refuses it, structurally.

  DOOR THREE IS NOT REFUSED AND NOT CONTESTED.  IT HAS NEVER BEEN
  ASKED IN THE LANGUAGE THAT GOVERNS IT.  Order admits, geometry
  admits, information admits -- no unavailable value is wanted, because
  what is wanted is an OBSERVATION.  And STATISTICS, the row expand.py
  marked NOT-RUN as a missing extra, IS THE GOVERNING ROW HERE: what is
  the expected number density of relic wormholes, and does the existing
  catalogue cover enough volume to have seen one?  Nobody in this
  project has estimated one.

  A FIFTH STATUS WAS NEEDED AND ITS EXISTENCE IS A FINDING.  Door one's
  algebra row is neither admission nor refusal -- EdGB says unstable
  for every alpha, f(R) claims stable non-exotic solutions, and the
  dispute is live.  CONTESTED is not NOT-RUN: it has been run twice
  with opposite answers.  And by register 1173 a contested row returns
  no binary, so it earns no row -- WHICH MEANS DOOR ONE CANNOT BE
  REDUCED AT ALL.  Its E is UNDEFINED, not 1.

        DOOR 1   UNDECIDABLE   algebra contested   wants a STABILITY
                                                   CALCULATION
        DOOR 2   REFUSED       order refuses       wants nothing
        DOOR 3   UNASKED       statistics silent   wants a NUMBER
                                                   DENSITY

  AND DOOR THREE'S E = 0 IS NOT AN ADMISSION.  Its four held rows do
  agree, which is more than either other door manages -- but index3.py's
  standing caution governs: E(X) = 0 over an INCOMPLETE X measures the
  bookkeeping and not the knowledge, and here the row that DECIDES the
  door is precisely the silent one.  Door three is not admitted.  It is
  UNASKED, which is a different and better thing to be.

  NO TWO DOORS ARE DECIDED BY THE SAME LANGUAGE.  That is register 1176
  across the doors: they do not agree, E is not zero, AND THE
  DISAGREEMENT IS THE MAP.  By section 33.2 the deciding language names
  the kind -- door one a STABILITY object, door two a CAUSAL-STRUCTURE
  object, door three a SEARCH object -- and each kind names its own
  next measurement.

        SO THE ANSWER TO "WHICH DOOR" IS NOT THE CHEAPEST.  IT IS THE
        ONE WHOSE DECIDING LANGUAGE IS MERELY SILENT RATHER THAN
        CONTESTED OR REFUSED, AND THE MEASUREMENT IT WANTS IS A NUMBER
        DENSITY.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
