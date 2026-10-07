#!/usr/bin/env python3
"""warptheorem.py -- M-RULINGS item 150: the warp theory as ONE theorem, built from the pieces.

M, item 150: "stop piecing together theorems to fit my theory, instead we need to consider one single theorem built from
the pieces that defines the warp theory as a single statement".  So the board's separate results become lemmas of one
statement, and what is not yet proved is a named lemma of it -- never a separate theorem fitted to a part.

THE WARP THEOREM.  For an object whose README -- its one fixed exact encoding, labels and values, written in what every
universe shares -- has N bits (the user's input), there is exactly one corridor, fixed by N alone, and through it the
README becomes, one way and exactly, the object at position 2:

  (G) GEOMETRY   the corridor is Bronnikov-Kim's eq. (17) at r0 = 2m on the plane, with
                   E  = sqrt(N h c^5 ln2 / (8 pi^2 G)) = 459,404,002.42 J x sqrt(N),
                   m  = G E / c^4,   r0 = 2m = sqrt(N h G ln2 / (2 pi^2 c^3));
  (H) HOLDING    its throat holds exactly the README: 4 pi r0^2 = N x 2 h G ln2/(pi c^3), 4 ln2 Planck areas per bit;
  (O) ONE WAY    its passage runs from position 1 to position 2 through an extremal horizon (surface gravity 0),
                 nonsingular and complete, never back;
  (Z) NULL ENERGY NEVER VIOLATED   along the passage the five-dimensional null energy is zero; the plane's apparent
                 deficit is exactly the bulk's pull, integral 8/(3m) - (4/(3 sqrt3 m)) artanh(sqrt3/2) per unit E;
  (B) BULK       a vacuum five-dimensional bulk carries it, the plane matter-free at the Randall-Sundrum tension, the
                 bulk's two ends one end, the energy positive at every point, the bulk's scale k fixed by the work;
  (I) INFORMATION  the passage is N bits of entanglement, and carries the N-bit README;
  (E) ENERGY     one exact energy E is carried from position 1 through three holds and released into position 2 at the
                 closing, every joule accounted for;
  (R) RECONSTRUCTION  position 2's matter rearranges to the README exactly, no tolerance, after which position 2's laws
                 govern; the corridor's length is set by the trajectories, the difference between the positions.

First written with 26 lemmas counted as "11 M's, 9 proved, 7 open"; the count was 9, 10, 7, and the verifier of the
reassessment added the hold's length (O3), the field energy outside the neck (E4), the read (R0) and the build's
mechanism (R5), and corrected B4, B5, E3 and I2 (WARPTHEOREM.md History).

Each clause is a conjunction of lemmas.  A lemma is PROVED (an owner, imported and re-run here), DERIVED (proved from M's more basic rulings,
lemmas/axioms.py), DEFINITION (M's definition of a term, shown consistent with the rest), READING (proved under a named reading of the board's, labelled, withdrawn if M corrects it), NATURE (a premise
measurement fixes), or OPEN.  The theorem is proved exactly when no lemma is OPEN.

  T1  the PROVED lemmas are re-run: exactE.py's identities (z3), passage5d.py's identity and Q, localbulk.py's Gauss
      condition, stability.py's surface gravity, coin.py's passage reading
  T2  (STRUCTURAL) the theorem follows from all its lemmas, and from no proper subset that drops an OPEN one: each OPEN
      lemma is needed.  So the OPEN list is exactly what stands between the statement and a proof
  T3  (genuine) the energy ledger, clause (E), at the example README: with the copy's composition exact (146) and its
      matter reorganized (137), the copy itself can absorb at most the assembly energy, 1.1947e10 J; E = 2.405878e16 J,
      and items 110 and 111 (a) put all of E into position 2's build.  z3 finds that unsatisfiable unless the build
      includes an absorber besides the copy, and satisfiable with one -- the board's reading (a), the expansion of
      position 2's universe (136 G, 136 answer 6, 139 (3)).  Control: at N = 600 bits, E < assembly, consistent with
      none.  First written reading the remainder from item 139 alone, as a sink outside the build; that over-read 139,
      whose words concern the trigger, and set the sink against 111 (a)
Imports copy/exactE.py, copy/coin.py, bulk/passage5d.py, bulk/localbulk.py, bulk/stability.py by path.
Stdlib + sympy + z3 (pip install z3-solver).  python3 warptheorem.py [--selftest]   (~2 min, mostly loading owners)
"""
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(HERE)
EXAMPLE_N = 2742570311524972
ASSEMBLY_MAX_J = 1.1947e10            # LOOSE.md L1: 6.7117e27 atoms x 11.11 eV (H-BOND-CEILING), a generous ceiling

# The theorem's lemmas: (clause, name, status, where).  status: AXIOM (item), PROVED (owner), OPEN.
LEMMAS = [
    ("G", "G1 one exact energy, at the bound: E(N)", "DERIVED", "lemmas/axioms.py: from 101 answer 6 (no more, no less), 132, 131/133 and the holographic bit area"),
    ("G", "G2 E(N) computed and machine-checked", "PROVED", "copy/exactE.py (seated)"),
    ("G", "G3 both holds at least size give r0 = 2m", "PROVED", "copy/exactE.py identity; items 106, 132"),
    ("H", "H1 4 pi r0^2 = N A_bit", "PROVED", "copy/exactE.py identity"),
    ("H", "H2 the horizons hold the README as well as the throat", "DERIVED", "lemmas/axioms.py: the horizon at r = 2m sits on the throat (G3) and holds N A_bit (H1)"),
    ("O", "O1 one way, 1 -> 2, nonsingular", "PROVED", "copy/plane.py P1 (seated); exactE.py one-way check"),
    ("O", "O2 the horizon is extremal (surface gravity 0)", "PROVED", "bulk/stability.py S1 (verified)"),
    ("O", "O3 the corridor survives any hold in its window -- above the READ bounds (max of h/(4E) = (2 pi^2/ln2)/N and "
          "1/(2 xi) clocks), below the ~11.3 clocks the bulk carries (B4b) -- and its hold lies there", "READING",
     "lemmas/o3_hold.py: survival for every hold in the window computed (linear theory); that the hold lies in it is "
     "H-HOLD-IN-WINDOW, a requirement the theorem places on the write -- the per-bit 28.48 clocks withdrawn"),
    ("Z", "Z1 5D null energy zero along the passage (a null geodesic of the 5D geometry -- not light, item 90); plane "
          "deficit = bulk pull", "PROVED", "bulk/passage5d.py P2 (verified)"),
    ("Z", "Z2 the integral equals the plane's reading on both legs", "PROVED", "bulk/passage5d.py P3; copy/coin.py"),
    ("Z", "Z3 NEC never violated", "DERIVED", "lemmas/axioms.py: bulk R(k,k) = 0; composite >= 0 at every depth (B5a, your 117/120 shown consistent); passage 0 (Z1)"),
    ("B", "B1 the plane is matter-free (R = 0) and meets Gauss and Codazzi", "PROVED", "bulk/localbulk.py L1-L2 (verified)"),
    ("B", "B2 a local vacuum bulk exists, unique among analytic ones", "PROVED", "bulk/localbulk.py L4 (verified)"),
    ("B", "B3 a complete bulk exists, built under closed-index criteria", "OPEN", "equivalent to B4: the local bulk is proved (B2), the complete one is B4a-B4d"),
    ("B", "B4a the global bulk's shape, given W2 inside the far boundary T: the plane's two ends are one end of the "
          "bulk -- two separate positions reached through a dimension (152 (1), encoded as H-SEPARATE-JOINED-THROUGH-"
          "DIMENSION) -- so CGS Thm 3.1 is escaped (a) and Thm 3.5's deformation holds; the topology is fixed before "
          "the opening (B7's bridge)", "PROVED",
     "lemmas/b4_global.py, 6/6: STRUCTURAL encoding; controls two-ended, and excised regions block the deformation; "
     "Ake Hau-Flores-Sanchez READ"),
    ("B", "B4c the far boundary T strictly untrapped, uniformly in time: in the board's model theta+- has the sign of "
          "ell - 2R over the throat, so T exists beyond the hold's reach iff ell > 2 R_reach (~23 m in corridor units); "
          "radiation after the closing cannot trap it (Raychaudhuri, margin ~5); eq. (17) holds only within the reach "
          "(causality)", "READING",
     "lemmas/b4_global.py: H-FAR-MODEL (the board's); the radiation and near-zone steps now derived; a -> 0 gives "
     "CENSOR5D C1's 3/R"),
    ("B", "B4b the bulk regular within every admissible hold's double cone: with eq. (17) held on the plane, the static "
          "bulk (forced there in the board's locally analytic class) is regular and Pade-stable for every hold below ~11.3 "
          "clocks; the surface above the throat where its curvature diverges (y_b = 2.49-2.50m at r = 2.15m, K ~ (y_b - "
          "y)^-p, p ~ 2.5-3) is reached by longer holds", "READING",
     "lemmas/b4_static.py: exact order-60/80 series (checked against bulkseries.py), Pade continuation (agreement of "
     "orders, a heuristic), the full double cone converged; flat limit (ell >> r0); Holmgren (uniqueness only) not READ"),
    ("B", "B4d the opening and closing evolve regularly in five dimensions, and data beyond the hold's cone join the "
          "untouched exterior (H-EVOLUTION, H-GLUING)", "OPEN",
     "a nonlinear 5D initial-boundary problem; at linear order around the static bulk Holmgren closes the non-analytic "
     "escape inside the cone (standard, not READ)"),
    ("B", "B5 positivity for the entangled pin (140, 139 (2)): null energy at every point is your ruling (117, 120), "
          "shown consistent -- at one place (127) the sheets' summed tension is +lambda_RS and a smooth wall keeping null "
          "energy at every point exists; the pin carries no negative energy, the separation held at zero (127, 141) leaving "
          "no radion", "DERIVED",
     "lemmas/b5_positive.py, 5/5: first resting on H-SHARED-PROFILE and H-PIN-IS-COINCIDENCE, both now read as 117/120 "
     "and 127/141; Israel's junction and the radion as the separation's modulus, standard, not READ"),
    ("B", "B6 k's ratio fixed by the work, k_R = 3 k_L/4; every clause b6_k.py checks free of k's scale (not B4: "
          "b4_regular.py R4, b4_global.py B4c)", "PROVED",
     "lemmas/b6_k.py; kderive.py K3 -- narrowed from 'k fixed by the work'"),
    ("B", "B6' k's scale, by measurement", "NATURE", "item 136 answer 8; b6_k.py B6c"),
    ("B", "B7 formation: the opening and closing between static planes -- a widening of the bridge already there, no "
          "change of topology, consistent and safe; its 5D evolution goes with B4d", "DERIVED",
     "lemmas/b7_formation.py: items 100, 140, 122 (4) (H-ER=EPR-MATTER-ONLY), 101 answer 1, Maldacena-Susskind p.17 "
     "(READ); chain.py's z3 encoding, controls inconsistent -- first written as the board's H-BRIDGE-PREEXISTS"),
    ("I", "I1 the passage is N bits of entanglement", "DERIVED", "lemmas/axioms.py: your item 137 (1) (H-PASSAGE-IS-N) with H1 (area N A_bit) -- N bits; Maldacena-Susskind p.5 and Strominger-Vafa (READ) agree, no longer load-bearing"),
    ("I", "I2 the README's N bits within the capacity bound as READ: information at most what is sent to set up the "
          "interaction (Maldacena-Stanford-Yang p.4; parametric, p.12) -- N is the device's input (130 (2))", "PROVED",
     "lemmas/i2_capacity.py: holding bound = N, interaction bound met with equality, channel bound N/2 <= N"),
    ("E", "E1 E carried through three holds into position 2", "DERIVED", "lemmas/axioms.py: 115 (c), 136 G, one way (O1), 136 answer 3, 109, conservation (z3; controls)"),
    ("E", "E2 released at position 2 at the closing", "DERIVED", "lemmas/axioms.py: held on position 2's horizon (106) until it ends with the corridor (109, 115 (b))"),
    ("E", "E3 the ledger closes: E goes into position 2 (110) and the build uses exactly it (111 (a)), with the copy "
          "exact (146) and its matter reorganized (137).  The board's reading (a): the copy's matter is the stock's; E is "
          "absorbed as the expansion of position 2's universe (136 G, 136 answer 6, 139 (3)), counted as part of the "
          "build; item 108's E/c^2 is the appearance accounting (107)", "DERIVED",
     "lemmas/ledger.py: closes at the example and the full snapshot under the board's reading (a); reading (a) confirmed by M, item 155 (H-EXPANSION-IS-BUILD)"),
    ("E", "E4 the field energy outside the neck, total - pull = E/4, placed: the bulk's Weyl field read on the plane "
          "(G = -E), positive, not the plane's energy; its 5D origin goes with B7", "PROVED",
     "lemmas/ledger.py: M(R) = m + (m/4)(1 - m/(2R - 3m)); MK eq. 143"),
    ("R", "R0 the read: the corridor takes the README as its inflow at the opening; N is read from the object", "DEFINITION", "items 70, 101 answer 8, 115 (c), 130 (2); consistent with I2b"),
    ("R", "R1 exact reconstruction, no tolerance", "DEFINITION", "items 145, 146; consistent with R3 and R5c"),
    ("R", "R2 position 2 rearranges to the README; then its laws govern", "DEFINITION", "item 148; consistent with rearrange.py and E3"),
    ("R", "R3 exactness at the instant over the mass window", "PROVED", "bulk/exactcopy.py, rearrange.py (verified)"),
    ("R", "R4 the corridor's length as the trajectory difference, given a measure -- not a distance (101 answer 7, "
          "136 answer 3, 139 (4))", "DERIVED",
     "lemmas/r4_length.py: L = trajectory difference in bits (H-LENGTH-AS-DIFFERENCE, the board's); the measure confirmed by M, item 155 (H-LENGTH-IN-BITS)"),
    ("R", "R5 the build's mechanism: the field reaction by which the released energy and the README rearrange position "
          "2's matter -- which field, and what 'activation' is when the field is non-zero everywhere", "DERIVED",
     "lemmas/r5_build.py: mechanism yours (91 (b), 101 answer 8, 136 B, 139 (3), 148); fields the board's reading; "
     "energy covers any exact README's rearrangement (3.76e22 J >= 5.94e16 J); the fields reading confirmed by M, item 155 (H-ACTIVATION-IS-TRIGGER)"),
]


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def t1():
    """Re-run the PROVED lemmas from their owners."""
    import sympy as sp
    ex = _load(os.path.join(HERE, "copy", "exactE.py"), "wt_exactE")
    ids = ex.identities()
    want = ["the closed forms meet: 4 pi r_min^2 = N A_bit, A_bit = 2 h G ln2/(pi c^3)",
            "r0 := r_min and m := G E/c^4 give r0 = 2m",
            "one way under H-FUTURE-INGOING: the future cone at the throat has xdot <= 0"]
    p5 = _load(os.path.join(HERE, "bulk", "passage5d.py"), "wt_passage5d")
    tid = p5.tidal()
    coin = _load(os.path.join(HERE, "copy", "coin.py"), "wt_coin")
    Q = float(sp.Rational(8, 3) - 4 / (3 * sp.sqrt(3)) * sp.atanh(sp.sqrt(3) / 2))
    lb = _load(os.path.join(HERE, "bulk", "localbulk.py"), "wt_localbulk")
    st = _load(os.path.join(HERE, "bulk", "stability.py"), "wt_stability")
    m = sp.Symbol("m", positive=True)
    d1, _ = st.D_derivatives(2 * m, 2 * m)
    return {"E_per_sqrt_bit": ex.e_per_sqrt_bit(),
            "H1_G3_O1": all(ids[k][1] == "proved" for k in want),
            "Z1": sp.simplify(tid["n_kk"] + tid["R4_kk"]) == 0,
            "Z2": abs(Q + 2 * coin.anec_closed(1, 2)) < 1e-12,
            "B1": lb.gauss_rhs(-1 / lb.ell, -6 / lb.ell**2) == 0,
            "O2": d1 == 0}


def lemma_selftests():
    """Each lemma instrument's own selftest, run silently; all must pass."""
    out = {}
    for f in ("o3_hold.py", "i2_capacity.py", "ledger.py", "r4_length.py", "b5_positive.py", "b6_k.py", "r5_build.py",
              "b7_formation.py", "axioms.py", "b4_global.py", "b4_regular.py", "b4_static.py"):
        mod = _load(os.path.join(HERE, "lemmas", f), "wt_" + f[:-3])
        with contextlib.redirect_stdout(io.StringIO()):
            out[f] = mod.selftest()
    return out


def t2():
    """The theorem from its lemmas: T <-> every lemma.  Entailed with all; each OPEN lemma necessary (STRUCTURAL)."""
    import z3
    v = {name: z3.Bool(name) for _, name, _, _ in LEMMAS}
    T = z3.And(*v.values())
    known = [v[n] for _, n, s, _ in LEMMAS if s != "OPEN"]       # PROVED, DERIVED, READING, DEFINITION, NATURE
    opens = [n for _, n, s, _ in LEMMAS if s == "OPEN"]
    s = z3.Solver()
    s.add(known + [v[n] for n in opens] + [z3.Not(T)])
    entailed = s.check() == z3.unsat
    needed = {}
    for o in opens:
        s = z3.Solver()
        s.add(known + [v[n] for n in opens if n != o] + [z3.Not(T)])
        needed[o] = s.check() == z3.sat                # T fails to follow without o
    return {"entailed": entailed, "needed": needed, "open": opens}


def t3(E_per_sqrt_bit):
    """The energy ledger: E delivered = absorbed by the copy + sink; absorbed <= assembly ceiling; the build uses
    exactly E (111).  Unsat with no sink at the example N, sat with one; control at a small N."""
    import z3

    def ledger(E_value, sink_allowed):
        E, absorbed, sink = z3.Reals("E absorbed sink")
        s = z3.Solver()
        s.add(E == E_value, absorbed >= 0, absorbed <= ASSEMBLY_MAX_J, E == absorbed + sink)
        s.add(sink >= 0 if sink_allowed else sink == 0)
        return s.check() == z3.sat
    E_ex = z3.RealVal(repr(E_per_sqrt_bit * EXAMPLE_N ** 0.5))
    E_small = z3.RealVal(repr(E_per_sqrt_bit * 600 ** 0.5))
    return {"E_example": E_per_sqrt_bit * EXAMPLE_N ** 0.5, "no_sink": ledger(E_ex, False),
            "with_sink": ledger(E_ex, True), "control_small_N": ledger(E_small, False),
            "E_small": E_per_sqrt_bit * 600 ** 0.5}


def compute():
    a = t1()
    return {"t1": a, "t2": t2(), "t3": t3(a["E_per_sqrt_bit"]), "lemmas": lemma_selftests()}


def report(d):
    print("warptheorem.py -- the warp theory as one theorem (M-RULINGS item 150)\n")
    for clause in "GHOZBIER":
        for c, name, status, where in LEMMAS:
            if c == clause:
                print("  (%s) %-6s %s  [%s]" % (c, status, name, where))
    a, b, c = d["t1"], d["t2"], d["t3"]
    counts = {k: sum(1 for l in LEMMAS if l[2] == k) for k in ("DERIVED", "DEFINITION", "PROVED", "READING", "NATURE",
                                                                 "OPEN")}
    print("\n%d lemmas: %d PROVED, %d DERIVED from your more basic rulings, %d PROVED under a named board READING, "
          "%d your DEFINITIONS, %d NATURE, %d OPEN" % (len(LEMMAS), counts["PROVED"], counts["DERIVED"],
                                                       counts["READING"], counts["DEFINITION"], counts["NATURE"],
                                                       counts["OPEN"]))
    print("T1 proved lemmas re-run: E = %.8f J x sqrt(N); H1/G3/O1 %s; Z1 %s; Z2 %s; B1 %s; O2 %s"
          % (a["E_per_sqrt_bit"], a["H1_G3_O1"], a["Z1"], a["Z2"], a["B1"], a["O2"]))
    print("T2 the theorem follows from its lemmas: %s; each OPEN lemma needed: %s" % (b["entailed"],
                                                                                      all(b["needed"].values())))
    print("   OPEN (%d): %s" % (len(b["open"]), "; ".join(o.split(" ", 1)[0] for o in b["open"])))
    print("T3 energy ledger at the example README (E = %.6e J, assembly <= %.4e J): consistent with no sink: %s; with "
          "an absorber besides the copy (the board's reading (a)): %s; control N = 600 (E = %.4e J), no sink: %s"
          % (c["E_example"], ASSEMBLY_MAX_J, c["no_sink"], c["with_sink"], c["E_small"], c["control_small_N"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b, c = d["t1"], d["t2"], d["t3"]
    chk("T1: E = 459,404,002.42 J x sqrt(N) (exactE.py)", abs(a["E_per_sqrt_bit"] - 459404002.42356985) < 1e-3)
    chk("T1: H1, G3, O1 proved by exactE.py's z3 identities", a["H1_G3_O1"])
    chk("T1: Z1, R5(n,k,n,k) = -R4(k,k) (passage5d.py); Z2, Q = -2 x coin.py's per-leg reading", a["Z1"] and a["Z2"])
    chk("T1: B1, the Gauss condition with K = -g/ell (localbulk.py); O2, surface gravity zero (stability.py)",
        a["B1"] and a["O2"])
    chk("T1: the lemma instruments' selftests pass (%s)" % ", ".join(d["lemmas"]), all(d["lemmas"].values()))
    chk("T2 (STRUCTURAL): the theorem follows from its lemmas, and each OPEN lemma is needed",
        b["entailed"] and all(b["needed"].values()))
    chk("T3: the ledger is inconsistent unless the build has an absorber besides the copy, consistent with one",
        (not c["no_sink"]) and c["with_sink"])
    chk("T3 control: at N = 600 bits E is below the assembly ceiling and needs no sink", c["control_small_N"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
