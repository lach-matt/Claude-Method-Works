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

Each clause is a conjunction of lemmas.  A lemma is AXIOM (M's ruling, cited), PROVED (an owner, imported and re-run
here), or OPEN.  The theorem is proved exactly when no lemma is OPEN.

  T1  the PROVED lemmas are re-run: exactE.py's identities (z3), passage5d.py's identity and Q, localbulk.py's Gauss
      condition, stability.py's surface gravity, coin.py's passage reading
  T2  (STRUCTURAL) the theorem follows from all its lemmas, and from no proper subset that drops an OPEN one: each OPEN
      lemma is needed.  So the OPEN list is exactly what stands between the statement and a proof
  T3  (genuine) the energy ledger, clause (E), at the example README: with the copy's composition exact (146) and its
      matter reorganized (137), the copy can absorb at most the assembly energy, 1.1947e10 J; E = 2.405878e16 J.  The
      axioms are then INCONSISTENT unless the remainder has somewhere to go -- z3 finds the system unsatisfiable with no
      sink, satisfiable with item 139's expansion of position 2's universe as the sink.  Control: at N = 600 bits,
      E < assembly, consistent with no sink.  So lemma E3 (where the remainder goes) is not optional
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
    ("Z", "Z1 5D null energy zero along the passage; plane deficit = bulk pull", "PROVED", "bulk/passage5d.py P2 (verified)"),
    ("Z", "Z2 the integral equals the plane's reading on both legs", "PROVED", "bulk/passage5d.py P3; copy/coin.py"),
    ("Z", "Z3 NEC never violated", "AXIOM", "items 117, 120, 123"),
    ("B", "B1 the plane is matter-free (R = 0) and meets Gauss and Codazzi", "PROVED", "bulk/localbulk.py L1-L2 (verified)"),
    ("B", "B2 a local vacuum bulk exists, unique among analytic ones", "PROVED", "bulk/localbulk.py L4 (verified)"),
    ("B", "B3 a complete bulk exists, built under closed-index criteria", "AXIOM", "items 120, 121"),
    ("B", "B4 the global bulk: the plane's two ends one end of the bulk (CGS Thm 3.1 escape (a)), with Thm 3.5's "
          "deformation", "OPEN", "bulk/CENSOR5D.md; items 126, 127 read by the board"),
    ("B", "B5 positivity at every point (a null-energy thickening of the composite)", "OPEN",
     "item 139 (2) M-PROVE-POSITIVE; bulk/STATIC.md S4 met for the sum"),
    ("B", "B6 k fixed by the work", "OPEN", "item 140; bulk/KDERIVE.md (ratio fixed, scale open)"),
    ("B", "B7 formation: the opening and closing between static planes", "OPEN",
     "items 115, 136 A, 136 answer 7, 141"),
    ("I", "I1 the passage is N bits of entanglement", "AXIOM", "item 137 (H-PASSAGE-IS-N)"),
    ("I", "I2 N bits carried by N bits of entanglement meets the capacity bound", "OPEN",
     "Gao-Jafferis-Wall (READ in STATUS wall B); to compute"),
    ("E", "E1 E carried through three holds into position 2", "AXIOM", "items 106, 110, 111, 115"),
    ("E", "E2 released at position 2 at the closing", "AXIOM", "item 136 answer 2"),
    ("E", "E3 where the remainder E - E_assembly goes, shown to close the ledger", "OPEN",
     "item 139 (3) expansion, read by the board; T3 below"),
    ("R", "R1 exact reconstruction, no tolerance", "AXIOM", "items 145, 146"),
    ("R", "R2 position 2 rearranges to the README; then its laws govern", "AXIOM", "item 148"),
    ("R", "R3 exactness at the instant over the mass window", "PROVED", "bulk/exactcopy.py, rearrange.py (verified)"),
    ("R", "R4 the corridor's length as the trajectory difference, given a measure", "OPEN", "items 114 (c), 116, 117, 136 answer 3"),
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


def t2():
    """The theorem from its lemmas: T <-> every lemma.  Entailed with all; each OPEN lemma necessary (STRUCTURAL)."""
    import z3
    v = {name: z3.Bool(name) for _, name, _, _ in LEMMAS}
    T = z3.And(*v.values())
    known = [v[n] for _, n, s, _ in LEMMAS if s != "OPEN"]
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
    return {"t1": a, "t2": t2(), "t3": t3(a["E_per_sqrt_bit"])}


def report(d):
    print("warptheorem.py -- the warp theory as one theorem (M-RULINGS item 150)\n")
    for clause in "GHOZBIER":
        for c, name, status, where in LEMMAS:
            if c == clause:
                print("  (%s) %-6s %s  [%s]" % (c, status, name, where))
    a, b, c = d["t1"], d["t2"], d["t3"]
    print("\nT1 proved lemmas re-run: E = %.8f J x sqrt(N); H1/G3/O1 %s; Z1 %s; Z2 %s; B1 %s; O2 %s"
          % (a["E_per_sqrt_bit"], a["H1_G3_O1"], a["Z1"], a["Z2"], a["B1"], a["O2"]))
    print("T2 the theorem follows from its lemmas: %s; each OPEN lemma needed: %s" % (b["entailed"],
                                                                                      all(b["needed"].values())))
    print("   OPEN (%d): %s" % (len(b["open"]), "; ".join(o.split(" ", 1)[0] for o in b["open"])))
    print("T3 energy ledger at the example README (E = %.6e J, assembly <= %.4e J): consistent with no sink: %s; with "
          "a sink (item 139's expansion): %s; control N = 600 (E = %.4e J), no sink: %s"
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
    chk("T2 (STRUCTURAL): the theorem follows from its lemmas, and each OPEN lemma is needed",
        b["entailed"] and all(b["needed"].values()))
    chk("T3: the ledger is inconsistent with no sink at the example README, consistent with one",
        (not c["no_sink"]) and c["with_sink"])
    chk("T3 control: at N = 600 bits E is below the assembly ceiling and needs no sink", c["control_small_N"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
