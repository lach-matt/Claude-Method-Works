#!/usr/bin/env python3
"""sync_face.py -- item 428 (approved at 429, continued at 431): what holds the face at the README's size at the
opening, starting from synchronization (lemmas/SYNCHRONIZATION-APPROACH.md, stages 1-2).

M, 428: "what holds the face at the README's size at the opening? - for the math to decide, start will b
synchronization".  Labels: computed (exact unless marked), deduced, READ (verbatim at source, 2026-10-16), M's.
Worked in the conversation; not verified; not seated.

  S0 (read) M's words, verbatim in the rulings file: 136 (7) "The throat formation is synchronization"; 136 A "So
     opening position 1 automatically opens position 2"; 137 (1), the passage's entanglement N bits; 141 "two rubiks
     cubes solving so that their facing sides match"; 162 "only the size that is needed to hold the object once and at
     once"; 163 "All together, one whole"; 136 G "the README is the energy, not separate"; 240 "The mass on position 2's
     side is not equal to ours"; 132 the horizons hold the README; 390 closes "when there is nothing contained".
  S1 (READ) Stage 1 at source.  Ryu and Takayanagi (hep-th/0603001), eq. (1.5): "S_A = Area of gamma_A / 4 G_N^(d+2)".
     Maldacena (hep-th/0106112), eq. (2.3), the two copies' state |Psi> = Z^(-1/2) sum_n e^(-beta E_n/2) |E_n>_1 |E_n>_2,
     and after (2.4): "After doing this sum we get the thermal density matrix in the first copy ... The entropy is the
     entanglement entropy".  Van Raamsdonk (1005.3035): "as the entanglement between degrees of freedom in region A and
     region B ... drops to zero ... the area of the minimal surface separating the regions decreases to zero".
     Maldacena and Qi (1804.00491), eq. (4.26), "t_r(u) = t_l(u) = t' u, with t' = constant" -- the two boundary clocks
     locked -- and eq. (4.40), the coupled ground state's energy negative; their p. 52 (the board's MQ-53): "The full
     geometry will not contain a horizon".  Maldacena, Stanford and Yang (the board's MSY-14): N_send <= g, at most the
     bits needed to open the wormhole.
  T0 (computed, exact) On the ingoing form ds^2 = -f dv^2 + 2 dv dr + r^2 dOmega^2, g^rr = f.  The face is marginally
     trapped, g^rr = 0, so in D = 4 the Misner-Sharp mass there is exactly m = r/2 (G = c = 1) and in D = 5 mu = r^2:
     a face of the README's size at the opening encloses exactly E(N) at the opening, positive and negative alike,
     whatever holds it.  The same holds if the face is an event horizon: a null generator held at fixed r0 has dr/dv =
     f/2 = 0, so f(r0, v) = 0 and m(v) = r0/2 at every v (computed) -- a face of fixed size needs the whole E(N)
     inside it at every moment it stands, apparent or event horizon alike.
  Y1 (computed, exact) The entanglement sets the size.  With RT's normalization and 137 (1), S = N ln2 gives the area
     4 G hbar N ln2 / c^3 = N A_bit, A_bit = 4 l_P^2 ln2 = 7.2428e-70 m^2 -- exactly the record's bit area
     (trajectories.py, exactE's 4 pi r_min^2 = N A_bit).  So a face whose size is its passage's entanglement has the
     README's size from the formation, with no ramp (162).  In D = 5 the same with G5 (RT's G_N^(d+2)).
  Y2 (computed, exact; deduced) The energy is not lifted.  On the two-sided state each side's reduced state is thermal
     and its entropy is the entanglement (S1).  For a face, S = A/4G with E = M c^2, and inverting S(M) = 4 pi G M^2/
     (hbar c) at S = N ln2 gives M c^2 = E(N) = sqrt(hbar c^5 ln2/(4 pi G)) sqrt(N) = 4.594e8 J sqrt(N) -- the record's
     figure, and T0's r0 c^4/2G.  So each face holds its own E(N) from the formation: the entanglement sets the size,
     and the size brings the energy with it.  Which source of that energy survives M's rulings:
       (i) the README's energy is inside each face as one whole at the formation, and the long write is the setting of
           the README's exact state on it -- the cubes present from the start, solving until the facing sides match
           (141).  It meets 136 G (the energy is the README's own), 162 and 163 (the size and the whole held from the
           opening), 240 and E1x (each side its own energy) and 426 (the write long, read as the state's write).
           SURVIVES -- the board's reading, put to M: it reads 426's "written in" as the state, the energy whole from
           the opening.  T0 leaves no third way: a face of the README's size at the opening holds E(N) then, or the
           face is not at that size then (against 162);
       (ii) our face's E(N) supplied from position 2's side: against E1x, nothing of our E crosses.  EXCLUDED;
       (iii) a coupling's negative energy holding the area with less positive energy (GJW, Maldacena-Qi (4.40)): the
           coupled geometry has no horizon (MQ-53), against 132 and 143 A.  EXCLUDED as the holder.
  Y3 (deduced) The channel.  The two-sided state signals nothing by itself (Peres and Terno, relativity.py U5), so the
     README's state needs a channel, and what crosses is what can cross a horizon (143 A).  MSY's bound allows at most
     the bits that opened the passage: with the passage's entanglement N bits (137 (1)), N bits is the bound's limit,
     reached and not exceeded -- consistent at equality.
  Y4 (deduced) The closing.  As the entanglement goes to zero the separating area goes to zero (Van Raamsdonk): the
     faces close when the passage holds nothing, which is 390 and 109.  Spent bit by bit, the area would fall during
     the write, against 162's fixed size; held whole until the write's end (163: all together, one whole) and released
     at once, the size stays fixed and the closing is 390's.  The board's reading: released whole at the end.
  So, on synchronization: both faces form at once (136 A), each holding its own E(N) and the shared N bits, at the
  README's size by its entanglement (Y1); the README's state is written over the long write (S2's least time stands);
  the passage is held whole and released at the end, closing both faces (Y4).  What supplies our side's E(N) at the
  formation is SOURCE's (the device's input, 130 (2)) -- now posed exactly: E(N), whole, at the opening.

[Item 432, beside the text: M, "the energy is there at the opening. It is the README itself. Information is
energy in the form of a binary interaction" -- Y2 (i) is M's (M-ENERGY-AT-OPENING); and "yes" to the release
at the end -- Y4 is M's (M-RELEASE-WHOLE).  Stage 3: the object is modelled -- both faces formed at once, each
holding the README itself, E(N), from the opening; its exact state written over the long write; the passage
held whole and released at the end.]

[Item 437, beside "S2's least time stands": M, "yes, the math, always. The write time is whatever is needed for the size
of the geometric object" (M-WRITE-BY-SIZE).  S2's least time stood on H-BITS-ARE-STATES (425), which 432 (1) set aside;
the least write time by the math is Margolus-Levitin's on each bit's share, 14.24 r0/c and 9.49 r_h/c, proportional
to the face's size (encode_read E5).]

What this does not claim: that RT, derived in AdS/CFT, holds for the passage (the identification of 137 (1)'s
entanglement with RT's is the board's reading); that the README's state can be written onto a hole's own capacity
at S2's rate (stated, not derived); any page beyond those quoted.

python3 sync_face.py [--selftest | --mutants]
"""
import math, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((136, "The throat formation is synchronization"), (136, "So opening position 1 automatically opens position 2"),
         (141, "Imagine two rubiks cubes solving so that their facing sides match"),
         (162, "only every takes on the size that contains the README upon opening"), (163, "All together, one whole"),
         (136, "the README is the energy, not separate"), (240, "The mass on position 2's side is not equal to ours"),
         (390, "it closes when there is nothing contained within the corridor"))
HBAR, G, C = 1.0545718176461565e-34, 6.6743e-11, 299792458.0
LP2 = HBAR * G / C ** 3


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def t0():
    """T0: g^rr = f on the ingoing form; at f = 0 the Misner-Sharp mass is r/2 (D = 4), mu = r^2 (D = 5)"""
    v, r, th, ph, ch = sp.symbols("v r theta phi chi", positive=True)
    out = []
    for D in (4, 5):
        mu = sp.Function("mu")(v)
        f = 1 - mu / r ** (D - 3)
        if D == 4:
            g = sp.Matrix([[-f, 1, 0, 0], [1, 0, 0, 0], [0, 0, r ** 2, 0], [0, 0, 0, r ** 2 * sp.sin(th) ** 2]])
        else:
            g = sp.Matrix([[-f, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, r ** 2, 0, 0],
                           [0, 0, 0, r ** 2 * sp.sin(ch) ** 2, 0], [0, 0, 0, 0, r ** 2 * sp.sin(ch) ** 2 *
                                                                     sp.sin(th) ** 2]])
        grr = sp.simplify(g.inv()[1, 1])
        if "wrong_grr" in MUT:
            grr = grr + mu / r ** (D - 2)
        sol = sp.solve(sp.Eq(grr, 0), mu)
        want = r if D == 4 else r ** 2
        r0 = sp.Symbol("r_0", positive=True)
        fixed = sp.solve(sp.Eq((f / 2).subs(r, r0), 0), mu)                # a generator held at r0: dr/dv = f/2 = 0
        out.append(sp.simplify(grr - f) == 0 and len(sol) == 1 and sp.simplify(sol[0] - want) == 0
                   and len(fixed) == 1 and sp.simplify(fixed[0] - want.subs(r, r0)) == 0)
    return all(out)


def y1():
    """Y1: RT/BH at S = N ln2 gives N A_bit, A_bit = 4 l_P^2 ln2 = the record's 7.24277891e-70 m^2"""
    N, Gs, hb, c = sp.symbols("N G hbar c", positive=True)
    area = 4 * Gs * hb * N * sp.log(2) / c ** 3
    if "half" in MUT:
        area = area / 2
    abit = 4 * (hb * Gs / c ** 3) * sp.log(2)
    ident = sp.simplify(area - N * abit) == 0
    num = 4 * LP2 * math.log(2)
    return ident and abs(num / 7.24277891e-70 - 1) < 1e-6, num


def y2():
    """Y2: S(M) = 4 pi G M^2/(hbar c) at S = N ln2 gives M c^2 = sqrt(hbar c^5 ln2/(4 pi G)) sqrt(N); 4.594e8 J"""
    N, M, Gs, hb, c = sp.symbols("N M G hbar c", positive=True)
    S = 4 * sp.pi * Gs * M ** 2 / (hb * c)
    if "entropy_r" in MUT:
        S = 4 * sp.pi * Gs * M / (hb * c)
    sol = sp.solve(sp.Eq(S, N * sp.log(2)), M)
    E = sp.simplify(sol[0] * c ** 2)
    want = sp.sqrt(hb * c ** 5 * sp.log(2) / (4 * sp.pi * Gs)) * sp.sqrt(N)
    ok = len(sol) == 1 and sp.simplify(E - want) == 0
    r0 = 2 * Gs * sol[0] / c ** 2
    ok &= sp.simplify(4 * sp.pi * r0 ** 2 - 4 * Gs * hb * N * sp.log(2) / c ** 3) == 0     # T0 and Y1 agree
    coeff = math.sqrt(HBAR * C ** 5 * math.log(2) / (4 * math.pi * G))
    return ok and abs(coeff / 4.59404002e8 - 1) < 1e-6, coeff


def report():
    print("S0 M's words inside 136, 141, 162, 163, 240, 390:", words())
    print("T0 the face marginally trapped: Misner-Sharp m = r/2 (4D), mu = r^2 (5D):", t0())
    ok1, a = y1(); print("Y1 RT at S = N ln2 gives N A_bit, A_bit = %.6e m^2 (record 7.24277891e-70): %s" % (a, ok1))
    ok2, e = y2()
    print("Y2 each face holds E(N) = %.6e J sqrt(N) (record 4.59404002e8), T0 and Y1 agreeing: %s" % (e, ok2))


def selftest(quiet=False):
    ok = []
    def say(s):
        if not quiet:
            print(s, flush=True)
    s0 = words(); ok.append(s0); say("S0 M's words verbatim inside their items: %s" % s0)
    a = t0(); ok.append(a)
    say("T0 g^rr = f; at the face, and on a generator held at r0, the mass is r/2 (4D), mu = r^2 (5D): %s" % a)
    b, _ = y1(); ok.append(b); say("Y1 the entanglement's area is N A_bit, the record's bit area: %s" % b)
    c, _ = y2(); ok.append(c); say("Y2 each face holds E(N), the record's 4.594e8 J sqrt(N), T0 and Y1 agreeing: %s" % c)
    return all(ok)


def mutants():
    names = ["wrong_grr", "half", "entropy_r"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
