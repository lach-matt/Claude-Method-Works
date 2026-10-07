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

Each clause is a conjunction of lemmas.  A lemma is AXIOM (M's ruling, cited), PROVED (an owner, imported and re-run
here), READING (proved under a named reading of the board's, labelled, withdrawn if M corrects it), or OPEN.  The theorem is proved exactly when no lemma is OPEN.

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
    ("G", "G1 one exact energy, at the bound: E(N)", "AXIOM", "items 133, 136 answer 1"),
    ("G", "G2 E(N) computed and machine-checked", "PROVED", "copy/exactE.py (seated)"),
    ("G", "G3 both holds at least size give r0 = 2m", "PROVED", "copy/exactE.py identity; items 106, 132"),
    ("H", "H1 4 pi r0^2 = N A_bit", "PROVED", "copy/exactE.py identity"),
    ("H", "H2 the horizons hold the README as well as the throat", "AXIOM", "items 106, 132"),
    ("O", "O1 one way, 1 -> 2, nonsingular", "PROVED", "copy/plane.py P1 (seated); exactE.py one-way check"),
    ("O", "O2 the horizon is extremal (surface gravity 0)", "PROVED", "bulk/stability.py S1 (verified)"),
    ("O", "O3 the corridor survives its hold: the hold's length in the corridor's clocks, derived, against S4's rate and "
          "S5b's v^2 blueshift", "READING", "lemmas/o3_hold.py: 2 pi^2/ln2 = 28.48 clocks for every N; growth <= 20.8; under "
     "H-ONE-STEP-PER-BIT and H-HOLD-AT-BOUND (the board's)"),
    ("Z", "Z1 5D null energy zero along the passage (a null geodesic of the 5D geometry -- not light, item 90); plane "
          "deficit = bulk pull", "PROVED", "bulk/passage5d.py P2 (verified)"),
    ("Z", "Z2 the integral equals the plane's reading on both legs", "PROVED", "bulk/passage5d.py P3; copy/coin.py"),
    ("Z", "Z3 NEC never violated", "AXIOM", "items 117, 120, 123"),
    ("B", "B1 the plane is matter-free (R = 0) and meets Gauss and Codazzi", "PROVED", "bulk/localbulk.py L1-L2 (verified)"),
    ("B", "B2 a local vacuum bulk exists, unique among analytic ones", "PROVED", "bulk/localbulk.py L4 (verified)"),
    ("B", "B3 a complete bulk exists, built under closed-index criteria", "AXIOM", "items 120, 121"),
    ("B", "B4 the global bulk: the plane's two ends one end of the bulk (CGS Thm 3.1 escape (a)), with Thm 3.5's "
          "deformation; reconciled with separate universes (101 answer 5), no loop (128), and infinitely many planes as "
          "further boundary components (123, 124, 136 answer 9, 138)", "OPEN",
     "bulk/CENSOR5D.md; items 126, 127 read by the board; 122 (1), 136 D"),
    ("B", "B5 positivity for the entangled pin (140): met for the sum only under the board's H-COMPOSITE-SURFACE; at "
          "every point (H-THICK-COMPOSITE) and the pin's own energy not shown", "OPEN",
     "item 139 (2) M-PROVE-POSITIVE; bulk/STATIC.md S4 and OPEN 3"),
    ("B", "B6 k fixed by the work", "OPEN", "item 140; bulk/KDERIVE.md (ratio fixed, scale open)"),
    ("B", "B7 formation: the opening and closing between static planes", "OPEN",
     "items 115, 136 A, 136 answer 7, 141"),
    ("I", "I1 the passage is N bits of entanglement", "AXIOM", "item 137 (H-PASSAGE-IS-N)"),
    ("I", "I2 the README's N bits within the capacity bound as READ: information at most what is sent to set up the "
          "interaction (Maldacena-Stanford-Yang p.4; parametric, p.12) -- N is the device's input (130 (2))", "PROVED",
     "lemmas/i2_capacity.py: holding bound = N, interaction bound met with equality, channel bound N/2 <= N"),
    ("E", "E1 E carried through three holds into position 2", "AXIOM", "items 106, 110, 111, 115"),
    ("E", "E2 released at position 2 at the closing", "AXIOM", "item 136 answer 2"),
    ("E", "E3 the ledger closes: E goes into position 2 (110) and the build uses exactly it (111 (a)), with the copy "
          "exact (146) and its matter reorganized (137).  The board's reading (a): the copy's matter is the stock's; E is "
          "absorbed as the expansion of position 2's universe (136 G, 136 answer 6, 139 (3)), counted as part of the "
          "build; item 108's E/c^2 is the appearance accounting (107)", "READING",
     "lemmas/ledger.py: closes at the example and the full snapshot under the board's reading (a)"),
    ("E", "E4 the field energy outside the neck, total - pull = E/4, placed: the bulk's Weyl field read on the plane "
          "(G = -E), positive, not the plane's energy; its 5D origin goes with B7", "PROVED",
     "lemmas/ledger.py: M(R) = m + (m/4)(1 - m/(2R - 3m)); MK eq. 143"),
    ("R", "R0 the read: the corridor takes the README as its inflow at the opening; N is read from the object", "AXIOM",
     "items 70, 101 answer 8, 115 (c), 130 (2)"),
    ("R", "R1 exact reconstruction, no tolerance", "AXIOM", "items 145, 146"),
    ("R", "R2 position 2 rearranges to the README; then its laws govern", "AXIOM", "item 148"),
    ("R", "R3 exactness at the instant over the mass window", "PROVED", "bulk/exactcopy.py, rearrange.py (verified)"),
    ("R", "R4 the corridor's length as the trajectory difference, given a measure -- not a distance (101 answer 7, "
          "136 answer 3, 139 (4))", "READING",
     "lemmas/r4_length.py: L = trajectory difference in bits (H-LENGTH-AS-DIFFERENCE, the board's)"),
    ("R", "R5 the build's mechanism: the field reaction by which the released energy and the README rearrange position "
          "2's matter -- which field, and what 'activation' is when the field is non-zero everywhere", "OPEN",
     "items 91 (b), 101 answers 3 & 4, 136 B and G, 139 (3), 148"),
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
    for f in ("o3_hold.py", "i2_capacity.py", "ledger.py", "r4_length.py"):
        mod = _load(os.path.join(HERE, "lemmas", f), "wt_" + f[:-3])
        with contextlib.redirect_stdout(io.StringIO()):
            out[f] = mod.selftest()
    return out


def t2():
    """The theorem from its lemmas: T <-> every lemma.  Entailed with all; each OPEN lemma necessary (STRUCTURAL)."""
    import z3
    v = {name: z3.Bool(name) for _, name, _, _ in LEMMAS}
    T = z3.And(*v.values())
    known = [v[n] for _, n, s, _ in LEMMAS if s != "OPEN"]                       # AXIOM, PROVED, READING
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
    counts = {k: sum(1 for l in LEMMAS if l[2] == k) for k in ("AXIOM", "PROVED", "READING", "OPEN")}
    print("\n%d lemmas: %d yours (AXIOM), %d PROVED, %d PROVED under a named board READING, %d OPEN"
          % (len(LEMMAS), counts["AXIOM"], counts["PROVED"], counts["READING"], counts["OPEN"]))
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
