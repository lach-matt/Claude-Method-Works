#!/usr/bin/env python3
"""arrival_small.py -- items 338, 340: the ARRIVAL row at the family's small end, on the one-way object. M: "Continue"
(to the board's report of items 336-337, which named ARRIVAL next in item 335's order: CLOSE, then ARRIVAL and FAR, with
B3 and B4d resting on them). The row: "the README forms the corridor as it comes in (198, M's guess); how the bits
rebuild and take their room" (284 (d), 285 (d)). Its first half was computed only at the large end, in four dimensions
(README-HELD.md 2-3, readme_held.py). At the small end write_small's verifier recorded it as not computed: "reading (ii)
is not computed" (264). Worked in the conversation (computed with sympy and a Dormand-Prince integrator written here,
exact where marked; READ where marked; deduced where marked; not verified by a separate session; not seated);
2026-10-13.

  V0 (read) The words the row rests on, verbatim in the rulings file: 198, "My guess would be 1." (the board's option
     (a): the README comes in while the corridor forms, with no partner, the size growing as it comes in and fixed once
     the whole README is in); 94, "The corridor is a single channel that grows in size to accommodate the size of the
     README"; 162, "It is and always will be only the size that is needed to hold the object once and at once"; 163,
     "All together, one whole"; 109, "A horizon cannot exist without the object of which it needs to exist"; 136 (1),
     "1 - yes" (H-EXACT-ENERGY-AT-BOUND: the one exact energy is E(N) at the bound); 136 (2), "released at position two
     at the closing of the horizon, which activates the higgs field forming the mass defined in the README"; 136 (6),
     "the bits are absorbed by position 2, and rebuild is likely instantaneous"; 136 G, "G - the README is the energy,
     not separate"; 158 (2), "Exactly as long as the write needs"; 240, "the object is built from the bulk at position
     2 as an exact copy under the laws and conditions of position 2"; 285, "It is an exact copy of the object of
     position 1, but it now obeys laws of position 2"; 336, "I think it is B"; 338, "Continue".
  V1 (computed, exact) The flux, the one E, the curvature.  On our side's five-dimensional ingoing form the only
     Einstein component is G_vv = 3 mu'(v)/(2 r^3) (close_small K1, re-run): an arrival that only adds energy, mu' >=
     0, has non-negative null energy on every ray, so it forms our face with no partner and keeps (Z) classically --
     nothing to pair, 183 not called on.  After it the Misner-Sharp mass is mu0 = r_h^2, E = 3 pi mu0/(8 G5) (K4's
     identity): the README's E is the hole's, one E, as 136 G has it ("the README is the energy").  On reading (i) --
     a face of the README's size standing through the write, the README crossing it (S4; 264) -- the hole ends with E
     besides the README's: 2E, a face of 2^(1/2) r_h holding 2^(3/2) N = 2.83 N bits, not "only the size that is needed"
     (162) and not 136 G's one energy; write_small's verifier recorded that 2E as reading (i)'s open question.  The
     Kretschmann scalar is 72 mu^2/r^8, mu' entering nowhere (computed, exact).
  V2 (computed; H-BITS-WITH-ENERGY, the board's, for the bit counts) The face as the README arrives, reading (ii). The
     arrival mu(v) = r_h^2 s(v/w), s the smoothstep of onset order n (s ~ x^n), width w in clocks of r_h/c, the event
     horizon traced back from r_h (Dormand-Prince 5(4), rtol 1e-10). For w <= 4 at every order n = 1-4 the face is born
     before the README's first part arrives -- 1.76 to 0.26 clocks before it, in the flat region -- holding
     (|v_born|/2)^3 N at the onset: 0.43-0.46 N at w = 1, 0.67-0.68 N at w = 0.5. From w = 8 at orders 3 and 4, and from
     w = 9 at order 2 (V3), it is born at the onset itself; at order 1 always before it, by 0.003 clocks at w = 1000.
     The trapping horizon r^2 = mu holds e^(3/2) N at a fraction e of E -- short of the e N that have come in by
     e^(1/2), so it holds the README only whole (computed, exact): 163's "all together, one whole", the record's
     H-WHOLE-AS-G1, here in five dimensions (README-HELD 3 found f^(3/2) N by deduction).
  V3 (computed, exact) The centre at the onset, for radial null dust. Self-similar onset mu = lambda v^2: outgoing rays
     r = x v obey 2 x^3 - x^2 + lambda = 0, with a positive root, an escaping ray from the singular onset, iff lambda <=
     1/27 (the four-dimensional 1/16's counterpart). The order-2 smoothstep has lambda = 3/w^2: naked from w = 9. Order
     1 (a finite flux at the onset): no outgoing ray leaves the onset point (deduced: where r^2 < mu the outgoing rays
     fall inward; the face is born before the onset in every order-1 run). Order 3: an escaping ray r ~ v/2 sees K ~
     v^-2 -- the five-dimensional counterpart of README-HELD 5's cubic onset. Order 4: K bounded along it. An arrival
     whose face is born before its onset (V2) puts the onset behind the face whatever its order: the quantum region
     (273) stays inside our face. Born at the onset, an order-2 arrival from w = 9 or an order-3 arrival shows the onset
     to our exterior (deduced: the escaping ray r ~ v/2 runs outside the face, which leaves the onset as r ~ mu^(1/2),
     v^(3/2) at order 3).
  V4 (READ; computed) The second law along the arrival.  READ: Bousso, hep-th/0203101v2, sec. II.A.3, eq. (2.3),
     Bekenstein's generalized second law, "dS_total >= 0", the total "black hole entropy and matter entropy"; sec. II.C.1
     (the Susskind process), "the initial entropy must not exceed the final entropy", whence S_matter <= A/4 (2.22); and
     sec. VII.B.3, "one cannot collapse more entropy through a (temporary) black hole horizon than it already has".
     READ: Wall, arXiv:1105.3445v6, abstract and sec. 1, the law proved "for semiclassical quantum fields falling across
     a causal horizon" with S_out "the von Neumann entropy of the matter fields restricted to the region outside of the
     horizon" (eq. (3)).  Two counts, and they part:
       the fine count (Wall's): the README one fixed exact encoding (136 (5)) is a definite state, so its own von
         Neumann entropy adds nothing beyond the vacuum's, and the law reduces to the area theorem -- which every run
         keeps, the face's area never falling (computed);
       the coarse count (Bousso's "thermodynamic system"): the README's carrier, a free gas holding 2^N states
         (write_small S3, H-BITS-ARE-STATES), has S = (4/3) a^(1/4) V^(1/4) E^(3/4), growing with V at fixed E
         (computed), equal to N ln2 at the write's floor ball (S3's construction) and more beyond it, while the face it
         forms holds exactly N ln2 at E(N) (136 (1); C2's construction, write_small S1). So the Susskind bound
         saturates, the carrier must start in the floor's ball exactly -- 158 (2)'s "exactly as long as the write needs"
         (deduced) -- and along the arrival the total S_gen(v) = (N - b) + C_face (bits in units of N, b the bits
         crossed) never falls below its start only for w up to 4.83, 5.75, 5.28, 4.82 clocks at orders 1-4 (computed,
         bisection), falling toward the spread limit min(e^(3/2) - e) = -4/27 N at e = 4/9 (computed, exact). And in
         every run dS_gen/dv < 0 somewhere (computed): the face grows ahead of the README (an event horizon's
         teleology), so at exact saturation the total rises and falls. On the coarse count (2.3) holds instant by
         instant for no arrival at 136 (1)'s exact energy, only as a limit (deduced, and so in every run: a face born
         before the onset lifts the total above its start, and it must come back to it at the end; one born at the onset
         holds e^(3/2) N < e N from the first).
  V5 (deduced) The write on reading (ii).  write_small S3's floor, 66,980 clocks at Z = 106.75 (imported), rests on
     H-WRITE-IS-ARRIVAL, H-FLAT-START, H-README-ALONE, H-FREE-GAS and H-BITS-ARE-STATES, not on S4's standing hole.  On
     reading (ii) the start is flat exactly (no face stands before the README) and the README's E is the only energy
     exactly (V1), so the floor carries unchanged and reading (i)'s 2E does not arise.  The 66,980 clocks are the
     README's approach in our exterior; its arrival onto the face is the width w, compact (V2-V4: w <= 4.79 clocks keeps
     both the onset behind the face and the coarse total at or above its start, at every order computed).  A converging
     carrier can arrive together from a ball of radius (1 + T) r_h if its inner parts wait (moving at most at c, the
     outer parts take T clocks); the state count of such a converging flow is not computed (does not claim).
  V6 (computed, exact) Position 2's release at the small end.  At the small end E and the face's capacity carry G5
     alone, no ell (C3 F4; write_small S3): E = 3 pi r_h^2/(8 G5), N ln2 = 2 pi^2 r_h^3/(4 G5).  Each destination's own
     G5 (bulk5_index: 2^(1/2) of ours at 2b and 2c, 2^(3/2) at 2P and 2a + 2P, 4 at 2b + 2P and 2c + 2P, ours at 2a):
       240 (b)'s reading -- position 2's face holds exactly the README at its own bit area -- gives r_h2/r_h =
         (G5_2/G5)^(1/3) and E2/E = (G5/G5_2)^(1/3): 1, 0.891, 0.707, 0.630 (computed), against the large end's
         (G/G2)^(1/2), 1, 0.707, 0.707, 0.5 (copy_p2 C1);
       the glued object read as one Kruskal geometry, one r_h for both faces (b_bounce Q1's isometry; O1c's core, 337
         (Q10)), gives E2/E = G5/G5_2 and a capacity N G5/G5_2: 1, 0.707, 0.354, 0.25 -- short of N at nine of the
         twelve, the README not fitting there.
     The two agree only where G5_2 = G5: ours, 2a-min and 2a-mirror (computed).  The board's reading, to be overruled
     by M at any point: 240 governs ("The mass on position 2's side is not equal to ours"), so at the nine destinations
     the two faces' radii differ and the bounce joins them through the quantum region, which gives up classical GR
     there (273); the isometric gluing is the case G5_2 = G5.  B5a's side total needs no single kappa (b5a_residue A6,
     339 (Q5)); this is the faces', not the planes'.
  V7 (computed from banked numbers) The room.  The copy has the original's atoms (285 (b): an exact copy), so a
     pure-metal object's copy fills (a0_law/a0_ours)^3 of its volume (p2_matter X3, PBE, the law RECONSTRUCTED): copper
     0.9387 / 0.8837, silver 0.8127 / 0.7106, gold 0.9898 / 0.9677, chromium 1.0469 / 1.0627 under position 2a's min /
     mirror readings -- 285 (b)'s eight figures, computed in conversation there and seated here.  Every destination of
     our matter law (2b, 2P, 2b + 2P) gives 1: G moves no atom's size (copy_p2 C2).  It takes room by displacing what is
     there (284 (2)) and stays as the new whole of position 2 (285, R6).
  V8 (deduced; M's statements named) The rebuild, step by step, and what each rests on.  (1) Our face forms as the
     README arrives, compact, all together, and each part falls to the bounce's region within a clock (V2; hold_small
     L1, L5) -- computed.  (2) The bounce carries it to position 2's face (273; O1c verified, 337).  (3) Position 2's
     face is open at most 33.6 of its clocks (c_junction J1) -- computed; the README emerges there (m1p2x_oneway O4;
     c5_oneway U12 (Q3)).  The compact arrival's width, at most 4.79 of our clocks, is shorter than that open period,
     so even a bounce that kept the span would fit it (computed comparison); J3's asymmetry is not needed for the
     README's crossing.  (4) Position 2 absorbs the bits (136 (6)) -- M's.  (5) Position 2's face closes, releasing
     position 2's own energy (110, 111 (a), 240; 336 K9), E2 as in V6 -- computed on a reading; it activates the Higgs
     field forming the mass the README defines (136 (2)), the build's need being that activation (239) -- M's.  (6) The
     copy is built from position 2's bulk as an exact copy under position 2's laws (240, 285), its mass position 2's
     own -- rest masses the shared SI's, binding moving them by at most 3.7e-11 (copy_p2 C2) -- and what can be built is
     set by position 2's material laws (136 H): under the mirror law Cu2 holds no bound minimum (p2_matter X2), so a
     copy that needs that bond as such is not built there, while the metals' solids bind under all three laws (X3).
     (7) It takes its room (V7) and stays.  (8) The rebuild "likely instantaneous" (136 (6)) -- M's, with 94's
     H-INSTANTANEOUS.  How bits become matter is M's statement, not a configuration: the cypher NOT-RUN for it (an index
     of steps would carry the answer as a key, 211); copy_p2 C5 already ran the destinations' variances through it.
  V9 (computed) ARRIVAL's question through the calculator, clause by clause in the form C4's stands in (291; c4_residue
     R9, R12): the classes t, the arrival compact (within V4's widths) or spread, and m, the README or other matter --
     no arrival, a README on a standing face (reading (i)), the README with 183's exact partner (README-HELD 2: no face
     forms), other matter arriving alone.  f1, "forms our face with no partner, (Z) kept, its own one E": {(1, 1): {1},
     (0, 1): {1}, (1, 0): {0, 1}, (0, 0): {0, 1}} -- 1 at orders 2 and 3 under all 96 codings, asked at the compact
     README and at the spread.  f2, "the onset behind the face or regular": {(1, 1): {1}, (0, 1): {0, 1}, (1, 0): {1},
     (0, 0): {0, 1}} from V2-V3 -- 1 at orders 2 and 3 for the compact README; for the spread, "both" at order 2 and 1 at
     order 3, the order-3 answer a read-back of the other cells, the spread's own population {0, 1} computed and
     deciding.  211's audit clean on every question.  As for C4, B5a and C8, the 1s add nothing to V1-V3.
  V10 (put to M) The fork that remains.  On reading (ii) -- 198, M's guess -- the README's own E forms our face as it
     arrives, one energy, compact, the face born about a clock before the README crosses and standing for the hole's
     life after (336); the write's 66,980 clocks are the approach.  That reads 334's "the face stands at least 66,980
     clocks while the write runs" (W5 (b)) as the write's arrival.  On reading (i) -- 334's wording as written -- a face
     of the README's size stands through the write, the README crossing it part by part, and the hole carries 2E.
     Which holds is M's: the record carries 198 as a guess and 334 as confirmed, and they part here.
     [Item 340, M's answer, verbatim: "C, but my guess is A" -- for the math, M's guess the board's option (A). Worked
     in V11.]
  V11 (item 340; computed; deduced) For the math, M's guess A. (a) Reading (i) against M's statements: its 2E against
     one exact energy, E(N) at the bound (136 (1)) and the README as the energy, not separate (136 G); its face holding
     2^(3/2) N = 2.83 N against "only the size that is needed to hold the object" (162; V1, computed); and a face
     standing before the object it needs (109). Reading (ii) meets all four (V1). So the math, on M's statements, gives
     reading (ii), M's guess A (deduced). (b) Within (ii), compact against spread. 162, "The throat doesn't change
     size": a compact arrival -- the widest that keeps the onset behind the face and the coarse count at every order, w
     = 4.79 clocks -- changes the face's size over at most w - v_born = 5.39 clocks (order 1; 5.07, 4.90 and 4.79 at
     orders 2-4), 8.0e-5 of the write's 66,980 (computed), and a spread one over the whole write. 163, "All together,
     one whole": a compact arrival crosses within 4.79 clocks, a spread one over the write, part after part. The second
     law: the fine count (136 (5), the README a definite state) does not decide; the coarse count gives compact (V4).
     Censorship admits a spread arrival only at onset orders 1 and 4 and above (V3). So the math, on 162 and 163, gives
     A with a compact arrival (deduced) -- the board's reading, to be overruled by M at any point. (c) What it re-reads:
     334's W5 (b) consequence, "the face stands at least 66,980 clocks while the write runs", becomes "the face stands
     from the README's arrival through the hole's life" (336), the write's 66,980 clocks its approach;
     M-HOLD-IS-THE-FACE's core -- the hold is the face standing, not how long the README stays within the horizon -- is
     unchanged. 198's option text, "the size growing as it comes in", holds over the arrival's few clocks.

What this does not claim.
  - That a carrier of the README's states can converge compactly: V5's choreography is allowed by causality, its state
    count is not computed.
  - The arrival beyond spherical symmetry and radial null dust, or in the bulk away from r_h << ell: the hole is
    Tangherlini at the small end (C1-C3), R/ell = 5.4e-11 at the write's start (write_small S3).
  - Which count of the second law governs: V4 computes both; the fine count is the board's reading of 136 (5).
  - The mechanism by which bits become matter (V8 (4)-(8)): M's statements, named.
  - The large end: there the record's ARRIVAL stands (arrival_cypher, README-HELD.md).

Imports close_small.py, write_small.py, bulk5_index.py, p2_matter.py, c4_residue.py and index_audit.py by path.
Stdlib + sympy.  python3 arrival_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from collections import Counter
from math import comb

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("My guess would be 1.", "The corridor is a single channel that grows in size to accommodate the size of the "
         "README", "It is and always will be only the size that is needed to hold the object once and at once",
         "All together, one whole", "A horizon cannot exist without the object of which it needs to exist",
         "released at position two at the closing of the horizon, which activates the higgs field forming the mass "
         "defined in the README", "the bits are absorbed by position 2, and rebuild is likely instantaneous",
         "G - the README is the energy, not separate", "1 - yes",
         "the object is built from the bulk at position 2 as an exact copy under the laws and conditions of position 2",
         "It is an exact copy of the object of position 1, but it now obeys laws of position 2",
         "Exactly as long as the write needs", "I think it is B", '"Continue"', "C, but my guess is A",
         "The throat doesn't change size")
ORDERS = (1, 2, 3, 4)                        # the arrival's onset orders: s ~ x^n at the start
WIDTHS = (0.5, 1, 2, 4, 8, 16, 64, 1000)     # the arrival's width, clocks of r_h/c
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    path = os.path.join(HERE, name)
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


# ================================================================================ the arrival in five dimensions
def profile(n):
    """the smoothstep of onset order n on [0, 1]: s ~ x^n at 0 and 1 - s ~ (1 - x)^n at 1, C^(n-1)"""
    c = math.factorial(2 * n - 1) / math.factorial(n - 1) ** 2

    def s(x):
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        return x ** n * sum(comb(n - 1 + k, k) * (1 - x) ** k for k in range(n))

    def ds(x):
        if x <= 0 or x >= 1:
            return 0.0
        return c * x ** (n - 1) * (1 - x) ** (n - 1)
    return s, ds


_A = [[], [1 / 5], [3 / 40, 9 / 40], [44 / 45, -56 / 15, 32 / 9],
      [19372 / 6561, -25360 / 2187, 64448 / 6561, -212 / 729],
      [9017 / 3168, -355 / 33, 46732 / 5247, 49 / 176, -5103 / 18656],
      [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84]]
_C = [0, 1 / 5, 3 / 10, 4 / 5, 8 / 9, 1, 1]
_B5 = [35 / 384, 0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84, 0]
_B4 = [5179 / 57600, 0, 7571 / 16695, 393 / 640, -92097 / 339200, 187 / 2100, 1 / 40]


def dopri(f, t0, y0, t1, rtol=1e-10, atol=1e-12, hmax=None, stop=None):
    """Dormand-Prince 5(4) for a scalar y' = f(t, y), either direction; the accepted points; stops when stop(t, y)"""
    sgn = 1.0 if t1 > t0 else -1.0
    h = sgn * min(abs(t1 - t0) / 100.0, hmax or 1e9)
    t, y, out = t0, y0, [(t0, y0)]
    while sgn * (t1 - t) > 1e-15:
        if sgn * (t + h - t1) > 0:
            h = t1 - t
        k = []
        for i in range(7):
            k.append(f(t + _C[i] * h, y + h * sum(_A[i][j] * k[j] for j in range(i))))
        y5 = y + h * sum(_B5[i] * k[i] for i in range(7))
        y4 = y + h * sum(_B4[i] * k[i] for i in range(7))
        err = abs(y5 - y4) / (atol + rtol * max(abs(y), abs(y5)))
        if err <= 1.0:
            t, y = t + h, y5
            out.append((t, y))
            if stop and stop(t, y):
                break
        h *= min(5.0, max(0.2, 0.9 * (1.0 / max(err, 1e-10)) ** 0.2))
        if hmax and abs(h) > hmax:
            h = sgn * hmax
    return out


_RUNS = {}


def arrival(w, n, rstop=1e-6):
    """our side's ingoing Vaidya form, mu(v) = r_h^2 s(v/w), r_h = 1, clocks of r_h/c: the face traced back from r = 1 at
    v = w.  Capacity in units of N is r^3 (C2: N ~ r_h^3); the bits in, if they come with the energy, mu(v) (E ~ mu)."""
    key = (w, n, rstop, bool(MUT.get("capacity_linear")), bool(MUT.get("eh_is_trapping")))
    if key in _RUNS:
        return _RUNS[key]
    s, ds = profile(n)
    mu = lambda v: s(v / w)
    f = lambda v, r: 0.5 * (1.0 - mu(v) / max(r, 1e-9) ** 2)
    pts = dopri(f, w, 1.0, -30.0, hmax=max(w, 1.0) / 200.0, stop=lambda v, r: r < rstop)[::-1]
    if MUT.get("eh_is_trapping"):                                  # the mutant: the trapping horizon taken for the face
        pts = [(v, math.sqrt(mu(v))) for v, _ in pts]
    cap = (lambda r: r) if MUT.get("capacity_linear") else (lambda r: r ** 3)   # the mutant: the 4D-like linear count
    v0, r0 = pts[0]
    born = v0 - 2 * r0 if (mu(v0) == 0.0 and r0 < 1e-3) else None  # born in the flat region before the onset
    gap = min((cap(r) - mu(v), v) for v, r in pts if v >= 0)       # S_gen(v) - S_gen(start), in N (the coarse count)
    slope = min(3 * r * r * f(v, r) - ds(v / w) / w for v, r in pts)  # d S_gen / dv, in N per clock
    area_ok = all(pts[i + 1][1] >= pts[i][1] - 1e-12 for i in range(len(pts) - 1))
    out = dict(born=born, gap=gap[0], gap_v=gap[1], slope=slope, area_ok=area_ok)
    _RUNS[key] = out
    return out


def _bisect(pred, lo, hi, it=26):
    for _ in range(it):
        m = 0.5 * (lo + hi)
        if pred(m):
            lo = m
        else:
            hi = m
    return lo


def v1():
    """the flux, the one E, and the curvature"""
    CS = _load("close_small.py", "arr_cs")
    va = CS.vaidya(5, "in")
    v, r = sp.symbols("v r")
    mu = sp.Function("mu")
    flux = sp.simplify(va["G00"] - 3 * sp.diff(mu(v), v) / (2 * r ** 3)) == 0 and va["others_zero"]
    # the Kretschmann scalar of the five-dimensional ingoing form, mu' entering nowhere
    th, ph, ps = sp.symbols("theta phi psi")
    X = [v, r, th, ph, ps]
    g = va["g"]
    gi = g.inv()
    nn = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(nn)) / 2) for c in range(nn)] for b in range(nn)] for a in range(nn)]
    R = {}
    for a in range(nn):
        for b in range(nn):
            for c in range(nn):
                for d in range(c + 1, nn):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    e += sum(Gam[a][c][kk] * Gam[kk][b][d] - Gam[a][d][kk] * Gam[kk][b][c] for kk in range(nn))
                    e = sp.simplify(e)
                    if e != 0:
                        R[(a, b, c, d)], R[(a, b, d, c)] = e, -e
    K = 0
    for a, b, c, d in itertools.product(range(nn), repeat=4):      # R_abcd R^abcd over every index, not only R^a_bcd's
        low = sum(g[a, e] * R.get((e, b, c, d), 0) for e in range(nn))
        if low == 0:
            continue
        up = sum(gi[b, f_] * gi[c, hh] * gi[d, kk] * R.get((a, f_, hh, kk), 0)
                 for f_ in range(nn) for hh in range(nn) for kk in range(nn))
        K += low * up
    K = sp.simplify(K)
    kret = sp.simplify(K - 72 * mu(v) ** 2 / r ** 8) == 0
    # one E against two: the Misner-Sharp mass after the arrival, the README's E alone (reading (ii)) or a face of E
    # standing through the write and the README's E besides (reading (i), write_small S4's verifier, 264)
    E_i = 1 if MUT.get("standing_one_E") else 2                    # the mutant: reading (i) counted with one E
    mu_i = sp.Integer(E_i)                                         # mu ~ E (K4's -3 pi mu0/(8 G5) = -E)
    return dict(flux=flux, kretschmann=kret, E_ii=1, E_i=E_i, rh_i=sp.sqrt(mu_i), cap_i=mu_i ** sp.Rational(3, 2))


def v2():
    """the face as the README arrives: born before the onset, and the second law's weak form, by width and order"""
    grid = {(n, w): arrival(w, n) for n in ORDERS for w in WIDTHS}
    gsl = {n: _bisect(lambda w, n=n: arrival(w, n)["gap"] > -1e-9, 1.0, 20.0) for n in ORDERS}
    born = {n: _bisect(lambda w, n=n: (lambda a: a["born"] is not None and a["born"] < -1e-7)(arrival(w, n)), 1.0,
                       20.0) for n in (3, 4)}
    # the trapping horizon holds e^(3/2) N at a fraction e of E: the README only whole (README-HELD 3, here in 5D)
    e = sp.Symbol("e", positive=True)
    cap_ah = (e ** sp.Rational(1, 1)) if MUT.get("capacity_linear") else e ** sp.Rational(3, 2)
    whole = sp.simplify(cap_ah / e) == sp.sqrt(e)
    return dict(grid=grid, gsl=gsl, born=born, whole=whole)


def v3():
    """the centre at the onset, for null dust: which onsets an escaping ray sees"""
    x, lam, w, c, vv = sp.symbols("x lambda w c v", positive=True)
    if MUT.get("onset_4d"):                                        # the mutant: the four-dimensional criterion
        poly = 2 * x ** 2 - x + 2 * lam
    else:
        poly = 2 * x ** 3 - x ** 2 + lam                           # r = x v in dr/dv = (1 - lambda v^2/r^2)/2
    xs = sp.solve(sp.diff(poly - lam, x), x)
    lam_c = max(sp.simplify(-(poly - lam).subs(x, xx)) for xx in xs if xx > 0)
    w_c = sp.solve(sp.Eq(3 / w ** 2, lam_c), w)[0]                 # the order-2 smoothstep s = 3 x^2 - 2 x^3
    rpow = 6 if MUT.get("kretsch_r6") else 8                       # the mutant: four-dimensional r^-6
    expo = {}
    for n in (3, 4):
        K = 72 * (c * vv ** n) ** 2 / (vv / 2) ** rpow             # along the escaping ray r ~ v/2
        expo[n] = sp.degree(sp.simplify(K * vv ** rpow), vv) - rpow
    return dict(lam_c=lam_c, w_c=w_c, expo=expo)


def v4():
    """the second law: the carrier's entropy at fixed energy, the spread limit, the two counts"""
    a, V, E = sp.symbols("a V E", positive=True)
    T = (E / (a * V)) ** sp.Rational(1, 4)                         # E = a V T^4, a free massless gas in d = 3
    S = sp.simplify(sp.Rational(4, 3) * a * V * T ** 3)
    v_exp = sp.simplify(V * sp.diff(S, V) / S)
    e = sp.Symbol("e", positive=True)
    dip = sp.minimum(e ** sp.Rational(3, 2) - e, e, sp.Interval(0, 1))
    arg = sp.solve(sp.diff(e ** sp.Rational(3, 2) - e, e), e)
    WS = _load("write_small.py", "arr_ws")
    floor = WS.head_clocks()
    return dict(v_exp=v_exp, dip=dip, dip_at=arg, floor=floor)


def v6():
    """position 2's release at the small end, for the twelve destinations, under the two readings"""
    B5 = _load("bulk5_index.py", "arr_b5")
    out = {}
    for n, d in B5.five_d().items():
        eg5, eg = d["e"]["G5"], d["e"]["G"]
        m_exp = -eg / 2 if MUT.get("release_4d") else -eg5 / 3   # the mutant: the large end's exponent
        out[n] = dict(law=d["law"], eG5=eg5, E_M=2.0 ** float(m_exp), r_M=2.0 ** float(eg5 / 3),
                      E_G=2.0 ** float(-eg5), cap_G=2.0 ** float(-eg5), E_large=2.0 ** float(-eg / 2))
    return out


def v7():
    """the room: the copy's volume per element under each law, (a0_law / a0_ours)^3, and per destination"""
    PM = _load("p2_matter.py", "arr_pm")
    sol = PM.SOL_FIX
    ratio = {}
    for (el, law), row in sol.items():
        r_ = row[0] / sol[(el, "ours")][0]
        ratio[(el, law)] = r_ ** -3 if MUT.get("room_inverted") else r_ ** 3
    dest = {n: {el: ratio[(el, d["law"])] for el in ("Cu", "Ag", "Au", "Cr")} for n, d in v6().items()}
    return dict(ratio=ratio, dest=dest)


def populations():
    """the clauses per class from the runs: t, the arrival compact (within the thresholds) or spread; m, the README or
    other.  f1: forms our face with no partner, (Z) kept, its own one E.  f2: the onset behind the face or regular."""
    o2, o3 = v2(), v3()
    comp = [w for w in WIDTHS if w <= min(list(o2["gsl"].values()) + list(o2["born"].values()))]
    spread = [w for w in WIDTHS if w > max(o2["gsl"].values())]
    onset_ok = lambda n, w: bool(o2["grid"][(n, w)]["born"] is not None or n == 1
                                 or (n == 2 and w < float(o3["w_c"])) or (n >= 3 and bool(o3["expo"][n] >= 0)))
    f2_c = {int(onset_ok(n, w)) for n in ORDERS for w in comp}
    f2_s = {int(onset_ok(n, w)) for n in ORDERS for w in spread}
    if MUT.get("readme_spread_ok"):
        f2_s = {1}
    # the classes' other members: no arrival (no face: f1 0, f2 vacuous 1); a README on a standing face (reading (i):
    # no formation, two E: f1 0); the README with 183's exact partner (no face forms, README-HELD 2: f1 0); other
    # matter arriving alone (it forms its own face with its own E: f1 1, f2 as the README's of the same profile)
    F1 = {(1, 1): {1}, (0, 1): {1}, (1, 0): {0, 1}, (0, 0): {0, 1}}
    F2 = {(1, 1): f2_c, (0, 1): f2_s, (1, 0): f2_c | {1}, (0, 0): f2_s | {1}}
    return dict(f1=F1, f2=F2, compact=comp, spread=spread)


_V9 = {}


def v9():
    """ARRIVAL's question through the calculator, clause by clause in the form C4's stands in (291)"""
    key = bool(MUT.get("readme_spread_ok"))
    if key in _V9:
        return _V9[key]
    CR = _load("c4_residue.py", "arr_cr")
    IA = _load("index_audit.py", "arr_ia")
    P = populations()
    res = {}
    for name in ("f1", "f2"):
        F = P[name]
        for cell in ((1, 1), (0, 1)):
            out = {k: sum((CR._ask_one(("f",), F, k, tf=tf, mf=mf, c4row=cell)
                           for tf, mf in itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
            kn = CR._cells("f", dict(zip(CR.NAMES4, range(4))), F, ("quantum",) + cell, CR.A4, CR.CD4)
            au = IA.audit_index(["K", "t", "m", "f"], kn)
            res[(name, cell)] = dict(F=F, out=out, flagged=bool(au["keys"] or au["onehot"]))
    _V9[key] = res
    return res


def v11():
    """item 340: for the math -- within reading (ii), how long a compact arrival changes the face's size"""
    o2 = v2()
    wstar = min(list(o2["gsl"].values()) + list(o2["born"].values()))
    if MUT.get("spread_counted_compact"):                         # the mutant: a spread arrival taken for compact
        wstar = 1000.0
    span = {}
    for n in ORDERS:
        b = arrival(wstar, n)["born"]
        span[n] = wstar - (b if b is not None else 0.0)
    floor = v4()["floor"]
    return dict(wstar=wstar, span=span, frac=max(span.values()) / floor)


def compute():
    return dict(v1=v1(), v2=v2(), v3=v3(), v4=v4(), v6=v6(), v7=v7(), v9=v9(), v11=v11())


def report(o):
    print("arrival_small.py -- the ARRIVAL row at the small end, one-way (item 338)\n")
    a = o["v1"]
    print("V1 G_vv = 3 mu'/(2 r^3) only: %s; K = 72 mu^2/r^8: %s; reading (ii) E %s; reading (i) E %s, face r_h x %s, "
          "capacity %s N" % (a["flux"], a["kretschmann"], a["E_ii"], a["E_i"], a["rh_i"], a["cap_i"]))
    b = o["v2"]
    print("V2 the face as the README arrives (born: clocks before the onset; gap: S_gen - start in N, coarse count):")
    for n in ORDERS:
        print("   n = %d: %s" % (n, "; ".join("w %g born %s gap %+.4f" % (
            w, "%.3f" % b["grid"][(n, w)]["born"] if b["grid"][(n, w)]["born"] is not None else "--",
            b["grid"][(n, w)]["gap"]) for w in WIDTHS)))
    print("   weak form held up to w = %s; born before the onset up to w = %s (n = 2: the onset's limit, V3); the "
          "trapping horizon holds e^(3/2) N: %s" % ({n: round(x, 4) for n, x in b["gsl"].items()},
                                                   {n: round(x, 4) for n, x in b["born"].items()}, b["whole"]))
    print("   d S_gen/dv < 0 somewhere in every run: %s; the area never falls in any run: %s" % (
        all(r["slope"] < 0 for r in b["grid"].values()), all(r["area_ok"] for r in b["grid"].values())))
    c = o["v3"]
    print("V3 self-similar onset naked iff lambda <= %s; the order-2 smoothstep's w_c = %s; K along the escaping ray "
          "as v^%s (n = 3), v^%s (n = 4)" % (c["lam_c"], c["w_c"], c["expo"][3], c["expo"][4]))
    d = o["v4"]
    print("V4 the gas's S ~ V^%s at fixed E; the spread limit's dip %s N at e = %s; the write's floor %.0f clocks" % (
        d["v_exp"], d["dip"], d["dip_at"], d["floor"]))
    print("V6 position 2's release at the small end (E2/E under 240 (b), its radius; under one r_h, E2/E = capacity; "
          "the large end's):")
    for n, r in o["v6"].items():
        print("   %-13s %-6s G5 x 2^%-4s E2/E %.4f r %.4f | %.4f | large %.4f" % (
            n, r["law"], r["eG5"], r["E_M"], r["r_M"], r["E_G"], r["E_large"]))
    print("V7 the room (a0_law/a0_ours)^3: %s" % {k: round(v, 4) for k, v in o["v7"]["ratio"].items() if k[1] != "ours"})
    for (name, cell), r in o["v9"].items():
        print("V9 %s at %s: population %s; order 2 %s, order 3 %s; audit flagged %s" % (
            name, cell, r["F"], dict(r["out"][2]), dict(r["out"][3]), r["flagged"]))
    q = o["v11"]
    print("V11 (item 340) the compact arrival's width %.4f clocks changes the face's size over %s clocks, %.2g of the "
          "write" % (q["wstar"], {n: round(x, 3) for n, x in q["span"].items()}, q["frac"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("V0 198, 94, 162, 163, 109, 136 (2), (6), G and (1), 240, 285, 158 (2), 336 and 338 verbatim in the rulings "
        "file",
        all(" ".join(w.split()) in rul for w in WORDS))
    a = o["v1"]
    add("V1 our side's only Einstein component G_vv = 3 mu'/(2 r^3), non-negative iff mu' >= 0; K = 72 mu^2/r^8; "
        "reading (ii) one E, reading (i) two -- a face of 2^(1/2) r_h holding 2^(3/2) N",
        a["flux"] and a["kretschmann"] and a["E_i"] == 2 and a["rh_i"] == sp.sqrt(2)
        and a["cap_i"] == 2 * sp.sqrt(2))
    b = o["v2"]
    g = b["grid"]
    ok = all(g[(n, w)]["born"] is not None and g[(n, w)]["born"] < 0 and g[(n, w)]["gap"] > -1e-9
             for n in ORDERS for w in WIDTHS if w <= 4)
    ok &= all(g[(n, w)]["gap"] < -1e-3 for n in ORDERS for w in WIDTHS if w >= 8)
    ok &= all(4.7 < b["gsl"][n] < 5.8 for n in ORDERS) and all(4.7 < b["born"][n] < 5.4 for n in (3, 4))
    ok &= b["whole"] and abs(g[(1, 1000)]["gap"] + 4 / 27) < 2e-3
    add("V2 an arrival within 4 clocks: the face born before the onset and the generalized entropy never below its "
        "start, at every order; from 8 clocks it falls below, toward -4/27 N; the thresholds 4.8-5.8 clocks; the "
        "trapping horizon holds e^(3/2) N, the README only whole", ok)
    add("V4 (the two counts) d S_gen/dv < 0 somewhere in every run (the face's teleology at exact saturation); the area "
        "never falls in any run (the fine count's law)",
        all(r["slope"] < 0 for r in g.values()) and all(r["area_ok"] for r in g.values()))
    c = o["v3"]
    add("V3 the onset: self-similar null dust naked iff lambda <= 1/27, the order-2 smoothstep from w = 9; K along the "
        "escaping ray as v^-2 at order 3, bounded at order 4",
        c["lam_c"] == sp.Rational(1, 27) and c["w_c"] == 9 and c["expo"][3] == -2 and c["expo"][4] == 0)
    d = o["v4"]
    add("V4 the free gas's entropy at fixed E grows as V^(1/4); the spread limit's dip -4/27 N at e = 4/9; the write's "
        "floor 66,980 clocks (write_small S3)",
        d["v_exp"] == sp.Rational(1, 4) and d["dip"] == -sp.Rational(4, 27) and d["dip_at"] == [sp.Rational(4, 9)]
        and round(d["floor"]) == 66980)
    e6 = o["v6"]
    ok = abs(e6["2b"]["E_M"] - 2 ** (-1 / 6)) < 1e-12 and abs(e6["2P"]["E_M"] - 2 ** -0.5) < 1e-12
    ok &= abs(e6["2b+2P"]["E_M"] - 2 ** (-2 / 3)) < 1e-12 and abs(e6["2b+2P"]["E_large"] - 0.5) < 1e-12
    ok &= all((abs(r["E_M"] - 1) < 1e-12) == (r["eG5"] == 0) for r in e6.values())
    ok &= all((abs(r["cap_G"] - 1) < 1e-12) == (r["eG5"] == 0) and r["cap_G"] <= 1 for r in e6.values())
    add("V6 position 2's release at the small end: E2/E = (G5/G5_2)^(1/3) under 240 (b) -- 1, 0.891, 0.707, 0.630 -- "
        "against the large end's (G/G2)^(1/2); one r_h and 240 (b) agree only where G5_2 = G5", ok)
    rt = o["v7"]["ratio"]
    want = {("Cu", "min"): 0.9387, ("Cu", "mirror"): 0.8837, ("Ag", "min"): 0.8127, ("Ag", "mirror"): 0.7106,
            ("Au", "min"): 0.9898, ("Au", "mirror"): 0.9677, ("Cr", "min"): 1.0469, ("Cr", "mirror"): 1.0627}
    add("V7 the room from p2_matter's banked solids: 285 (b)'s eight figures, Cu 0.9387 / 0.8837 to Cr 1.0469 / 1.0627; "
        "every destination of our matter law 1",
        all(abs(rt[k] - v) < 6e-5 for k, v in want.items())
        and all(abs(x - 1) < 1e-12 for n, dd in o["v7"]["dest"].items() for x in dd.values()
                if o["v6"][n]["law"] == "ours"))
    z = o["v9"]
    ones = Counter({(1,): 96})
    ok = all(z[("f1", c_)]["out"][k] == ones for c_ in ((1, 1), (0, 1)) for k in (2, 3))
    ok &= all(z[("f2", (1, 1))]["out"][k] == ones for k in (2, 3))
    ok &= z[("f2", (0, 1))]["F"][(0, 1)] == {0, 1} and z[("f2", (0, 1))]["out"][2] == Counter({("both",): 96})
    ok &= not any(r["flagged"] for r in z.values())
    add("V9 the calculator: f1 (forms, no partner, (Z), its own E) 1 at orders 2 and 3 for the README compact or "
        "spread; f2 (the onset behind the face or regular) 1 for the compact README, and for the spread \"both\" at "
        "order 2, its population {0, 1} computed; audits clean", ok)
    q = o["v11"]
    add("V11 (item 340) for the math: a compact arrival (w = 4.79 clocks) changes the face's size over at most 5.39 "
        "clocks, 8.0e-5 of the write's 66,980 -- 162's throat that does not change size and 163's one whole",
        abs(q["wstar"] - 4.7857) < 1e-3 and 5.3 < max(q["span"].values()) < 5.45 and q["frac"] < 1e-4)
    return res


MUTANTS = {"capacity_linear": "the face's capacity linear in r (a four-dimensional-like count) (V2, V4)",
           "eh_is_trapping": "the trapping horizon taken for the face (V2)",
           "standing_one_E": "reading (i) counted with one E (V1)",
           "onset_4d": "the onset's self-similar criterion in four dimensions (V3)",
           "kretsch_r6": "the curvature along the escaping ray with r^-6 (V3)",
           "release_4d": "position 2's release with the large end's exponent (V6)",
           "room_inverted": "the copy's volume ratio inverted (V7)",
           "readme_spread_ok": "the spread README's onset counted always hidden (V9)",
           "spread_counted_compact": "a spread arrival taken for compact (V11, item 340)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        _RUNS.clear()
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        _RUNS.clear()
        caught += bool(failed)
        print("  mutant %-17s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
