#!/usr/bin/env python3
"""far_cypher.py -- the chain input FAR put to the cypher: is there a far boundary consistent with (Z), (G), 139 (1)
and 166?  (computed by import, deduced, READ, STRUCTURAL; the cypher classifies, it does not derive; not verified by a
separate session; not seated; 2026-10-10)

WHAT IS ASKED.  chain_cypher.py's input FAR, verbatim (check Q2): "a far boundary consistent with (Z), (G), 139 (1),
166 (OPEN)"; B4c rests on it alone (its row: "B4c", "READING", "FAR").  Target T-FAR: a far model whose far surface
encloses a corridor and is strictly untrapped at every ell (B4c's own demand), in which seated (Z), seated (G),
139 (1) and 166 all hold.  Sub-target T-ZG, the part a one-plane far model can pose at all: corridor, untrapped, (Z),
(G).

M'S WORDS (verbatim, checked inside the rulings file by Q1; kept apart from every reading below)
  139 (1) "1 - yes"   (to the board's question: position 2's plane the negative-tension one, a quarter of ours, ours
          positive)
  166     M chose: "Both planes at once"
  179/180 "We know the corridor *does not sit on either position's plane, it only bridges them. So one could surmise
          that the corridor is exclusive to the bulk."
  183     M chose: "Yes: never violated as a pair"
  187 (3) "Seat both" -- (G) "the corridor sits in the bulk, on neither plane (179/180), with eq. (17) kept only as a
          plane's possible reading of the corridor's mouth"; (Z) "\"null energy never violated\" holds net along each
          light ray (183)" (the board's wording, seated by M)
  182 "If I had to guess, I would go with C"    184 "There are no matter free planes"    200 (1) "1 - Once: k_R = k_L/2"
  196 "... All questions get works through the cypher"    149 "I have given you everything I can. You have to work the
      math now"

THE CELLS (F0; each entry cited in the code to its file and check label; U = computed by no instrument, never guessed)
  coordinates: model (nominal); corridor (a corridor or join for T to enclose); untrapped (some far surface computed in
  that model is strictly untrapped at every ell, at every README size computed -- the shape may grow with the size);
  z, g, p139, c166 (seated (Z), seated (G), 139 (1), 166 met).  Values: 1 met, 0 not, U unknown (the code 2 -- not
  b4c_far's half-width U, which appears below only in "W >= sqrt3 U" and "k*(U)").
  The six far models whose far boundary IS computed (b4c_far.py, b4_global.py, censor5d.py) -- every one has ONE plane
  of positive tension:
    COL-ROUND    (1, 0, 0, 0, 0, 0)  H-FAR-MODEL's column (the board's), round T or W < sqrt3 U: trapped at small ell
    COL-ELLIPSE  (1, 1, 0, 0, 0, 0)  W >= sqrt3 U untrapped at every ell and N (X2, z3); but the column has net -pi/A
                                     per radial ray (against (Z), X9 (c)), a throat ON our plane (against (G)), one
                                     positive tension for both sheets (against 139 (1)), one plane (against 166)
    COL-POWER    (1, 1, 0, 0, 0, 0)  power-law columns (X9 (d)), excluded the same way
    COL-FIELD    (1, 1, 0, 0, 0, 0)  eq. (17)'s far field on our plane (X8), untrapped for k > k*(U)
    NOCOL        (0, 1, 1, 1, 0, 0)  a = 0, Poincare AdS5 with the RS plane (X11): untrapped, vacuum so (Z) holds, but
                                     nothing for T to enclose; (G) not contradicted (H-G-VACUOUS)
    BULKFIELD    (1, 1, U, 1, 0, 0)  a = 0 with a test field centred in the bulk (X11): untrapped, on neither plane; its
                                     null energy is computed by no instrument (a test extension, not a solution)
  The two bulks the board computed under 139 (1) and 166, whose far boundary NOBODY built:
    SLAB         (1, U, U, 0, 1, 1)  B4d stage 7: the slab between the planes is the throat; position 2's tension
                                     negative in every K4 branch; eq. (17) on a plane as its own metric -- the board's
                                     configuration by 179's carried note, so (G) 0
    BRIDGE-NEG   (1, U, U, 1, 1, 1)  model C, the two-sided bridge (182), on its off-convention branch: position 2's
                                     plane at exactly -1/4 of ours, balance and tension met (modelc.py C6, recomputed);
                                     fits 179/180 (BULK-BALANCE.md)

FACTS (each cell entry's support, re-run from its owner; every check can fail -- see --mutants)
  F1 (computed, imported b4c_far X2, X3) W >= sqrt3 U untrapped at every ell (z3, with vacuity and encoding guards); the
     round tip is (ell - 2U)/(U ell), trapped for ell < 2U
  F2 (computed, imported b4c_far X9) every column profile A(w) has R(k,k) = -2A^2/rho^4 and net -pi/A per radial ray;
     the model's throat is on our plane under one positive tension on both sheets; power-law columns are untrapped at
     p = +1, k = sqrt3 and p = -1, k = sqrt5; a = 0 is exactly AdS5
  F3 (STRUCTURAL, computed here from b4c_far's metrics) the warp ell/(ell + |w|) jumps in d_w ln only at w = 0: one
     plane; a power-law column's plane slice is u^2 + a^2; the test field's source sits at w = w_c > 0; at a = 0 there
     is no throat on the plane
  F4 (computed, imported b4c_far X11) at a = 0 every W >= U is untrapped at every ell (z3); the bulk-centred field at
     k = sqrt3 is untrapped at both README sizes with the deduced sufficient bound; the round surface is trapped
  F5 (computed, imported b4c_far X8) with eq. (17)'s far field, k*(U) = 1.862 at N = 1e3 and 1.7320586 at the example;
     1.74 is trapped at N = 1e3: the shape must grow for small READMEs; above k*(U) it is untrapped (the deduced
     sufficient bound of b4c_far X8)
  F6 (computed, imported b4d_stage7 K4) six branches, position 2's tension -1/3 or -1/6 against ours +4/3 in every one;
     each has a decaying outer bulk
  F7 (computed, imported modelc.py C6) RS on ell_s with L1 = 2 (u1 = mu = 4/3, lam = 2): one position-2 root at -1/4
     of ours, balance and tension met to 1e-40, ell_2 = 0.6623 ell_s; asked at +1/4 the plane still carries -1/4
  F8 (computed, imported p2_full.py TS; ITEM178 2 READ) a pure tension sigma crossed at angle a gives sigma sin a: a
     NEGATIVE tension gives negative null energy at every crossing angle -- the premise of H-NEG-PLANE-UNPAIRED, below;
     not a cell

THE CYPHER (cypher.py, roster 1173; the encoding is the board's, H-CYPHER-FAR-INDEX; it classifies, it does not
derive).  The model axis is nominal: every run is repeated under its 2n dihedral codings (each rotation and its
reverse) with U ranked above 1 and below 0 -- 24 runs on the six far models, 32 on all eight.
  X1 (STRUCTURAL) on the six far models with a computed far boundary T-FAR is NOT IN THE BOX: 139 (1) and 166 take only
     the value 0 there, so all five languages refuse it under every coding.  That is the record's gap (b4d_stage1.py
     D4: "a far model for a slab is not built"; B4C-FAR.md: "a negative-tension position-2 plane (139 (1)), the two
     planes of 166" not computed), not a reading
  X2 T-ZG on those six: statistics REFUSES under all 24 codings; the unseen pair is (corridor 1, (Z) 1) -- no far model
     that encloses a corridor keeps (Z).  Order, algebra and information admit it under all 24, geometry under the 12
     with U above 1.  What they invent: a corridor far model that keeps (Z) and (G) -- the vacuum NOCOL given a
     corridor, or the column COL-ELLIPSE with (Z) kept and no throat on the plane, which X9 of b4c_far excludes; the
     label carrying it moves with the coding (all six occur): an artefact of ordering a nominal axis, not a reading
  X3 all eight cells: statistics REFUSES T-FAR under all 32 codings
  X4 order, algebra and information admit T-FAR in exactly the 16 codings with U below 0, never with U above 1;
     geometry never.  What they invent: the slab or the bridge with its unknown far boundary and (Z) read as met (the
     slab's (G) 0 overridden too), or, under reversed codings, a column or vacuum far model carrying two planes
     and a negative position-2 plane.  It moves with where the unknown sits and with the coding: an artefact
  X5 CONTROL (the verdict flips on one cell): every unknown set favourable -> statistics admits T-FAR exactly as
     BRIDGE-NEG; the other four also admit SLAB, overriding its (G) 0.  With BRIDGE-NEG left out statistics refuses
     even with every unknown favourable (mutant drop_bridge)
  X6 WHAT WOULD MOVE IT: on the model axis the ONLY minimal set of unknown entries whose favourable value makes
     statistics admit T-FAR is {BRIDGE-NEG untrapped, BRIDGE-NEG (Z)}; no single entry suffices.  Unchanged when
     H-G-VACUOUS is replaced by "(G) unmet where there is no corridor"
  X7 the board's reading H-NEG-PLANE-UNPAIRED run as BRIDGE-NEG (Z) = 0: no set of the remaining unknowns moves
     statistics on the model axis.  In the projection (model axis dropped) only sets that take (Z) from SLAB do --
     pairwise support stitching two different bulks, recorded as an artefact
  X8 the projection: the unseen (1, 1) pairs are exactly (corridor, z), (untrapped, p139), (untrapped, c166), (z, p139),
     (z, c166) -- no computed far model is untrapped with a negative position-2 plane or with two planes, none with
     a corridor keeps (Z), and none keeping (Z) has two planes or a negative position-2 plane; all five refuse T-FAR
     there; its minimal sets include {SLAB untrapped, SLAB z}, which the model axis refuses because SLAB fails (G)
  X9 the board's reading H-STAGE7-AS-G (stage 7's eq. (17) on a plane read as (G)'s "possible reading of the mouth"):
     {SLAB untrapped, SLAB (Z)} becomes a second minimal set

THE BOARD'S READINGS (named, the board's; withdrawn if M corrects them; none is M's)
  H-139-BY-SIGN: 139 (1) is scored on its sign (position 2's plane negative, ours positive).  "A quarter" is the
    doubled-space count (B4D-STAGE7 K5, BULK-BALANCE 6), re-read under 200 (1); BRIDGE-NEG sits at -1/4 exactly anyway,
    SLAB at -1/3 and -1/6
  H-G-VACUOUS: with no corridor nothing sits on a plane, so (G) is not contradicted; corridor = 0 carries the absence.
    X6 holds without it
  H-STAGE7-IS-THE-BOARD'S: stage 7's eq. (17) as a plane's own metric is the board's configuration (179's carried note),
    so SLAB's (G) is 0; the other reading is X9
  H-E1C-STANDS-FOR-THE-BULK-CORRIDOR: the bulk-centred test field is the far field a bulk corridor shows T
  H-NEG-PLANE-UNPAIRED (a reading; entered only as the variant X7, never as a cell): a ray crossing a negative pure
    tension carries negative null energy (F8, ITEM178 2), and in model C a ray that enters exterior III across position
    2's plane cannot reach ours (BULK-BALANCE 7: not traversable, standard-not-READ), so nothing on it pairs the
    negative member and (Z) fails on BRIDGE-NEG.  No instrument computes it for the bridge, so the cell keeps U

SO.  Which language refuses: statistics refuses T-FAR on every index and every coding, and on the far models that
actually exist all five refuse, because none has two planes or a negative position-2 plane.  What the over-reach
invents: order, algebra and information (never geometry) admit T-FAR only when the unknown is ranked below 0, by filling
the bridge's or the slab's uncomputed far boundary and (Z) from other models' values -- or by giving a column or the
vacuum two planes; on T-ZG they invent a column far model that keeps (Z), which b4c_far X9 excludes.  What would move
the verdict: ONE far model for the two-sided bridge on its negative-P2 branch (modelc.py's off-convention branch)
returning BOTH theta+- on a far surface enclosing the bridge AND the net null energy along rays that cross position
2's negative plane; either output alone leaves statistics refusing (X6).  On H-NEG-PLANE-UNPAIRED the second output is
already negative, and then no far-boundary computation moves the verdict (X7): FAR would need a configuration in which
every ray crossing position 2's negative plane also crosses a positive member, which no computed model supplies.  FAR
stays OPEN; B4c stays READING.  The rulings let the board decide this (149): no question for M.
CAVEATS: every cell is a matter-free limit, against 184 (b4c_far X10 found our plane's matter negligible at T; the
bridge's is not computed); model C as it stands is the eternal two-sided black hole, not an admissible B4d corridor
(BULK-BALANCE 7); stage 7's outer bulks decay and are singular near the throat (K4), so a far boundary there needs W2 as
well; modelc.py is a scratch instrument (checked by a separate checker), not an owned one with its own selftest.

Imports tools/cypher.py, lemmas/b4c_far.py, lemmas/b4d_stage7.py, lemmas/kequality_scratch/two-sided/modelc.py,
lemmas/p2_full.py and lemmas/chain_cypher.py by path; reads M-RULINGS-2026-10-03.md and the board's notes cited (READ
checks).  Stdlib + sympy + mpmath + z3 (through b4c_far).  Writes nothing.
python3 far_cypher.py [--selftest | --mutants]   (selftest about 40 s; mutants about 55 s)
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
ROOT = os.path.dirname(os.path.dirname(WD))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
_MOD = {}
_FIX = {}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod_ = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod_
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod_)
    finally:
        sys.path[:] = saved
    return mod_


_PATHS = {"cypher": os.path.join(ROOT, "tools", "cypher.py"), "b4c_far": os.path.join(HERE, "b4c_far.py"),
          "stage7": os.path.join(HERE, "b4d_stage7.py"),
          "modelc": os.path.join(HERE, "kequality_scratch", "two-sided", "modelc.py"),
          "p2_full": os.path.join(HERE, "p2_full.py"), "chain": os.path.join(HERE, "chain_cypher.py")}


def mod(name):
    if name not in _MOD:
        _MOD[name] = _load(_PATHS[name], "farcy_" + name)
    return _MOD[name]


def _norm(path):
    return re.sub(r"\s+", " ", open(path, encoding="utf-8").read())


# ============================================================================================ the cells (F0)
# coordinates: model (nominal); corridor (the far model carries a corridor or join for T to enclose); untrapped (some
# far surface computed in that model is strictly untrapped at every ell, at every README size computed -- the shape may
# depend on U); z, g, p139, c166 (consistent with seated (Z), seated (G), 139 (1), 166).  U = not computed.
C = ["model", "corridor", "untrapped", "z", "g", "p139", "c166"]
U = 2
NAMES = ["COL-ROUND", "COL-ELLIPSE", "COL-POWER", "COL-FIELD", "NOCOL", "BULKFIELD", "SLAB", "BRIDGE-NEG",
         "SEATED-FAR"]
MAIN = [
    # 0 COL-ROUND -- H-FAR-MODEL (b4_global.py, the board's), join column a = 2 on our plane, round T and every W < sqrt3 U.
    #   untrapped 0: b4c_far X3 (check C4 'switch ell* = (3U^2 - W^2)/W'; the tip at W = U is (ell - 2U)/(U ell), here F1);
    #   z 0: b4c_far X9 (c) (check C10 'net per ray = -pi/A, never zero'); g 0: X9 (e) (C10 'throat on our plane');
    #   p139 0: X9 (e) (C10 'one positive tension on both sheets'); c166 0: X9 (e) STRUCTURAL 'one plane' (here F3)
    (0, 1, 0, 0, 0, 0, 0),
    # 1 COL-ELLIPSE -- H-FAR-MODEL, ellipse W >= sqrt3 U: untrapped at every ell and N (X2, check C4 'z3_Q_ge_3'; X4 C5);
    #   z, g, p139, c166 as COL-ROUND (the same model)
    (1, 1, 1, 0, 0, 0, 0),
    # 2 COL-POWER -- H-FAR-MODEL with a power-law column A = a (z/ell)^p: untrapped (X9 (d), C10 'column scans
    #   (excluded columns)': p = +1 at sqrt3, p = -1 at sqrt5); z 0 (C10 'general-profile R(k,k) = -2A^2/rho^4');
    #   g 0 (its plane slice is u^2 + a^2, here F3); p139 0, c166 0 (the same warp, one plane)
    (2, 1, 1, 0, 0, 0, 0),
    # 3 COL-FIELD -- H-FAR-MODEL with eq. (17)'s conformal far field on our plane, gamma = 5/4 (X8, check C9): untrapped
    #   for k > k*(U) = sqrt(3/(1 - 3 gamma m/U)) (C9 'k* at N = 1e3' 1.862, 'k* ... at the example' 1.7320586; deduced
    #   sufficient bound); 1.74 is trapped at N = 1e3 (C9 scans), so the shape grows for small READMEs; z, g, p139, c166 0
    (3, 1, 1, 0, 0, 0, 0),
    # 4 NOCOL -- a = 0: Poincare AdS5 with the RS plane, no corridor (X11, check C12 'z3: Q >= 3 at a = 0 for K >= 1';
    #   bulk/censor5d.py C1, 3/R): untrapped 1; z 1 (C10 'a = 0 is AdS5': vacuum, R(k,k) = 0 on every null ray);
    #   g 1 on the board's reading H-G-VACUOUS (nothing sits on a plane: model_vs_rulings('a_zero') finds no throat, F3);
    #   corridor 0 records that there is nothing for T to enclose; p139 0, c166 0
    (4, 0, 1, 1, 1, 0, 0),
    # 5 BULKFIELD -- a = 0 with a conformal test field centred at depth w_c = U/2 (X11, C12 scans and the deduced
    #   sufficient bound, both README sizes): untrapped 1 at k = sqrt3; g 1 (the field's centre w_c > 0 is in the bulk,
    #   on neither plane, F3); z U (a test extension, H-FAR-FIELD-EXTENSION, not a solution: its null energy is computed
    #   by no instrument); corridor 1 on the board's reading H-E1C-STANDS-FOR-THE-BULK-CORRIDOR; p139 0, c166 0
    (5, 1, 1, U, 1, 0, 0),
]
EXT = [
    # 6 SLAB -- B4d stage 7, the corridor across both planes (b4d_stage7.py; B4D-STAGE7.md): the slab between our plane
    #   and position 2's is 152's dimension and the throat (READ, Q2) -> corridor 1, c166 1; every K4 branch has position
    #   2's tension negative, ours +4/3 (stage7.branches(), F6) -> p139 1 (H-139-BY-SIGN, below); eq. (17) sits on a plane
    #   as its own metric, which 179's carried note reads as 'the board's configuration, not M's' (READ, Q2) -> g 0;
    #   z U (K2: position 2's plane must curve or carry matter, whose null energy per ray no instrument computes);
    #   untrapped U (b4d_stage1.py D4: 'a far model for a slab is not built', READ, Q2)
    (6, 1, U, U, 0, 1, 1),
    # 7 BRIDGE-NEG -- model C, the two-sided bridge (M's guess 182), on its off-convention branch: position 2's plane at
    #   -1/4 of ours with balance and tension met (modelc.py C6; recomputed here, F7) -> p139 1; a plane on each side of
    #   the bridge -> c166 1, corridor 1; 'Model C ... fits your 179/180 best' (BULK-BALANCE.md, READ, Q2) -> g 1;
    #   z U (bulk vacuum and planes at balance, but a ray crossing a negative pure tension carries negative null energy,
    #   ITEM178 2 and F8, and whether every such ray is paired is computed nowhere); untrapped U (no far model is built
    #   for any bridge: B4C-FAR.md 'the two planes of 166' not computed, READ, Q2)
    (7, 1, U, U, 1, 1, 1),
]


def cells(which="ext"):
    cs = list(MAIN) + (list(EXT) if which == "ext" else [])
    if MUT.get("unknown_as_one"):
        cs = [tuple(1 if (x == U and i > 0) else x for i, x in enumerate(c)) for c in cs]
    if MUT.get("seat_far") and which == "ext":
        cs.append((8, 1, 1, 1, 1, 1, 1))
    if MUT.get("slab_g1"):
        cs = [c[:4] + (1,) + c[5:] if c[0] == 6 else c for c in cs]
    if MUT.get("drop_bridge"):
        cs = [c for c in cs if c[0] != 7]
    return cs


# ============================================================================================ the cypher
LANGS = ("order", "algebra", "geometry", "information", "statistics")


def t_far(h):
    """the target: a far boundary that encloses a corridor, untrapped, with (Z), (G), 139 (1) and 166 all met"""
    return tuple(h[1:]) == (1, 1, 1, 1, 1, 1)


def t_zg(h):
    """the part the one-plane far models can pose: corridor, untrapped, (Z), (G)"""
    return tuple(h[1:5]) == (1, 1, 1, 1)


def ask(cs, tests, model_order=None, unk_low=False, coords=None):
    """Put the index to the five languages; per test, the decoded admitted cells that pass it (None if silent)."""
    cy = mod("cypher")
    coords = coords or C
    vo = {}
    for i, name in enumerate(coords):
        present = {c[i] for c in cs}
        if name == "model":
            vo[name] = [m for m in model_order if m in present]
        else:
            vo[name] = [x for x in ([U, 0, 1] if unk_low else [0, 1, U]) if x in present]
    ix = cy.Index("far", coords, [list(c) for c in cs], value_order=vo)
    res = {"_alphabets": {coords[i]: sorted(ix.decode[i][a] for a in ix.alphabets[i]) for i in range(len(coords))}}
    for lang in LANGS:
        out, _ = cy.ADMISSION[lang][0](ix, {})
        if out is None:
            res[lang] = None
            continue
        dec = {tuple(ix.decode[i][c[i]] for i in range(len(coords))) for c in out}
        res[lang] = {k: sorted(h for h in dec if t(h)) for k, t in tests.items()}
    return res


def codings(n):
    """The nominal model axis's dihedral codings: every rotation of 0..n-1 and its reverse (2n orders)."""
    base = list(range(n))
    out = []
    for k in range(n):
        rot = base[k:] + base[:k]
        out += [rot, rot[::-1]]
    return out


def sweep(cs, tests):
    models = sorted({c[0] for c in cs})
    runs = {}
    for unk_low in (False, True):
        for order in codings(len(models)):
            mo = [models[i] for i in order]
            runs[(unk_low, tuple(mo))] = ask(cs, tests, mo, unk_low)
    return runs


def unknowns(cs):
    return [(ci, i) for ci, c in enumerate(cs) for i, x in enumerate(c) if i > 0 and x == U]


def flipped(cs, S):
    out = [list(c) for c in cs]
    for ci, i in S:
        out[ci][i] = 1
    return [tuple(c) for c in out]


def minimal_sets(cs, projection=False):
    """every minimal set of unknown entries whose favourable value (1) makes statistics admit the target"""
    unk = unknowns(cs)
    mins = []
    for k in range(0, len(unk) + 1):
        for S in itertools.combinations(unk, k):
            if any(set(M) <= set(S) for M in mins):
                continue
            fc = flipped(cs, S)
            if projection:
                r = ask([c[1:] for c in fc], {"far": lambda h: tuple(h) == (1,) * 6}, None, False, C[1:])
            else:
                r = ask(fc, {"far": t_far}, sorted({c[0] for c in fc}), False)
            if r["statistics"]["far"]:
                mins.append(S)
    return [sorted((NAMES[cs[ci][0]], C[i]) for ci, i in S) for S in mins]


def variant(cs, name):
    """the board's readings run as variants (not the main cells)"""
    if name == "neg_unpaired":                # H-NEG-PLANE-UNPAIRED: BRIDGE-NEG's (Z) read as failed
        return [c[:3] + (0,) + c[4:] if c[0] == 7 else c for c in cs]
    if name == "slab_g":                      # stage 7's plane reading eq. (17) read as (G)'s 'possible reading'
        return [c[:4] + (1,) + c[5:] if c[0] == 6 else c for c in cs]
    if name == "nocol_g0":                    # (G) read as not met where there is no corridor
        return [c[:4] + (0,) + c[5:] if c[0] == 4 else c for c in cs]
    raise ValueError(name)


def cypher():
    tests = {"far": t_far, "zg": t_zg}
    main = sweep(cells("main"), tests)
    ext = sweep(cells("ext"), tests)
    cs = cells("ext")
    fav = [tuple(1 if (x == U and i > 0) else x for i, x in enumerate(c)) for c in cs]
    ctrl = ask(fav, {"far": t_far}, sorted({c[0] for c in fav}), False)
    proj = ask([c[1:] for c in cs], {"far": lambda h: tuple(h) == (1,) * 6}, None, False, C[1:])
    P = [c[1:] for c in cs]
    missing = [(C[1 + a], C[1 + b]) for a, b in itertools.combinations(range(6), 2)
               if not any(c[a] == 1 and c[b] == 1 for c in P)]
    PM = [c[1:5] for c in cells("main")]
    missing_main = [(C[1 + a], C[1 + b]) for a, b in itertools.combinations(range(4), 2)
                    if not any(c[a] == 1 and c[b] == 1 for c in PM)]
    var = {v: {"axis": minimal_sets(variant(cs, v)), "proj": minimal_sets(variant(cs, v), True)}
           for v in ("neg_unpaired", "slab_g", "nocol_g0")}
    return {"main": main, "ext": ext, "ctrl": ctrl, "mins": minimal_sets(cs), "mins_proj": minimal_sets(cs, True),
            "proj": proj, "missing": missing, "missing_main": missing_main, "var": var}


def summary(runs, lang, tk):
    adm = [k for k, r in runs.items() if r[lang] and r[lang][tk]]
    inv = sorted({h for r in runs.values() if r[lang] for h in r[lang][tk]})
    return {"n": len(runs), "admits": len(adm), "high": sum(1 for k in adm if not k[0]),
            "low": sum(1 for k in adm if k[0]), "labels": sorted({NAMES[h[0]] for h in inv}), "cells": inv}


# ============================================================================================ fixtures (F1-F8, Q1-Q2)
def _cached(key, fn):
    if key not in _FIX:
        _FIX[key] = fn()
    return _FIX[key]


def fixtures():
    bf = mod("b4c_far")
    k29 = "k_below_3" if MUT.get("owner_k29") else None
    p2n = "p2_negative" if MUT.get("owner_p2_negative") else None
    f = {"C4": _cached(("C4", k29), lambda: bf.check_C4(k29)),
         "C10": _cached(("C10", p2n), lambda: bf.check_C10(p2n)),
         "C12": _cached(("C12",), lambda: bf.check_C12()),
         "C9": _cached(("C9",), lambda: bf.check_C9())}

    def structural():
        cf, _, _ = bf.closed_form()
        tip = sp.simplify(cf.subs(bf.u, 0).subs(bf.w, bf.W).subs(bf.W, bf.U))
        wr = sp.Symbol("w_r", real=True)
        lapse = bf.metric("model")[0]
        om = lapse.subs(bf.w, sp.Abs(wr))                          # the mirror w -> |w| of the model's warp
        dl = sp.diff(sp.log(om), wr)
        jump = lambda w0: sp.simplify(sp.limit(dl, wr, w0, "+") - sp.limit(dl, wr, w0, "-"))
        kinks = {str(w0): jump(w0) for w0 in (0, bf.ell, -bf.ell, 5, -sp.Rational(1, 3))}
        col_plane = sp.simplify(bf.metric("column")[3].subs(bf.w, 0) - (bf.u**2 + bf.a**2))
        fc = sp.simplify(bf.metric("E1c")[1] / bf.metric("model")[1]) - 1
        centre = sp.simplify(1 / fc).subs({bf.u: 0, bf.w: bf.wc})
        _, a0 = bf.model_vs_rulings("a_zero")
        return {"round_tip": tip, "lapse": lapse, "kinks": kinks, "atoms": om.atoms(sp.Abs), "col_plane": col_plane,
                "centre_inv": sp.simplify(centre), "wc_positive": bf.wc.is_positive,
                "a0_throat": a0["throat on our plane (against (G))"]}
    f["S"] = _cached(("S",), structural)
    f["S7"] = _cached(("S7",), lambda: mod("stage7").branches())

    def bridge(sign):
        mc = mod("modelc")
        o = mc.rs_at_ell_s(sp.Integer(2))
        return {"o": o, "target": sign * o["lam"] / 4, "sols": mc.p2_given(o["mu"], sign * o["lam"] / 4)}
    sgn = 1 if MUT.get("bridge_plus") else -1
    f["BR"] = _cached(("BR", sgn), lambda: bridge(sgn))
    f["BRc"] = _cached(("BR", 1), lambda: bridge(1))
    rho = 0.5 if MUT.get("neg_tension_plus") else -0.5
    f["TS"] = mod("p2_full").thin_shell(0.0, rho=rho)
    f["TSc"] = mod("p2_full").thin_shell(0.0, rho=0.5)
    ch = mod("chain")
    f["chain"] = {"FAR": ch.INPUTS["FAR"], "B4c": [r for r in ch.ROWS if r[0] == "B4c"]}
    return f


M_WORDS = ['"1 - yes', 'M chose: "Both planes at once"', '(3) "Seat both"',
           "(G) the corridor sits in the bulk, on neither plane (179/180), with eq. (17) kept only as a plane's possible "
           "reading of the corridor's mouth", '(Z) \\"null energy never violated\\" holds net along each light ray (183)',
           'M chose: "Yes: never violated as a pair"',
           "We know the corridor *does not sit on either position's plane, it only bridges them. So one could surmise "
           "that the corridor is exclusive to the bulk.",
           '"If I had to guess, I would go with C"', '"There are no matter free planes"', '"1 - Once: k_R = k_L/2',
           '"Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher"',
           '"I have given you everything I can. You have to work the math now"']
READS = [(os.path.join(HERE, "b4d_stage1.py"), "a far model for a slab is not built"),
         (os.path.join(HERE, "B4C-FAR.md"), "a negative-tension position-2 plane (139 (1)), the two planes of 166"),
         (os.path.join(HERE, "BULK-BALANCE.md"), "Model C, the two-sided bridge, fits your 179/180 best"),
         (os.path.join(HERE, "BULK-BALANCE.md"), "Model C as it stands is not an admissible B4d corridor"),
         (os.path.join(HERE, "b4d_stage7.py"), "between the planes, AdS radius ell_s, 152's dimension and the throat"),
         (RULINGS, "so they describe the board's configuration, not M's"),
         (os.path.join(HERE, "ITEM178-NULL-PAIRS.md"), "A light ray crossing a thin sheet sees null energy with the sign "
          "of the sheet's energy density. For a pure tension, that is the tension's sign."),
         (os.path.join(HERE, "ITEM185-MATTER-ROUND.md"), "A negative tension needs either the off-convention branch")]


def compute():
    return {"fix": fixtures(), "cy": cypher(), "rulings": _norm(RULINGS),
            "reads": [(os.path.basename(p_), t_, t_ in _norm(p_)) for p_, t_ in READS]}


# ============================================================================================ checks
def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    f, cy = d["fix"], d["cy"]
    add("Q1 M's words verbatim in the rulings file: 139 (1), 166, 187 (3) with (G) and (Z) as seated, 183, 179/180, "
        "182, 184, 200 (1), 196, 149", all(w in d["rulings"] for w in M_WORDS))
    add("Q2 READ: the board's notes as cited (no far model for a slab; 139 (1) and 166 not computed in B4C-FAR; model C "
        "fits 179/180 and is not an admissible corridor as it stands; the slab is the throat; 179's carried note; "
        "ITEM178's crossing sign; ITEM185's negative branch) and chain_cypher's FAR input and B4c row",
        all(ok for _, _, ok in d["reads"])
        and f["chain"]["FAR"] == "a far boundary consistent with (Z), (G), 139 (1), 166 (OPEN)"
        and f["chain"]["B4c"] == [("B4c", "READING", "FAR", "B4c")])
    ok4, c4 = f["C4"]
    tip = f["S"]["round_tip"]
    ell, Uu = mod("b4c_far").ell, mod("b4c_far").U
    add("F1 computed (b4c_far X2, X3): W >= sqrt3 U untrapped at every ell (z3: Q >= 3, vacuity and encoding guards) -> "
        "COL-ELLIPSE untrapped 1; the round tip is (ell - 2U)/(U ell), trapped for ell < 2U -> COL-ROUND untrapped 0",
        ok4 and c4["z3_Q_ge_3"] and c4["vacuity_guard"] and c4["switch ell* = (3U^2 - W^2)/W"]
        and sp.simplify(tip - (ell - 2 * Uu) / (Uu * ell)) == 0 and tip.subs({ell: 1, Uu: 1}) < 0)
    ok10, c10 = f["C10"]
    mvr = c10["model against (G), 139 (1)"]
    sc = c10["column scans (excluded columns)"]
    add("F2 computed (b4c_far X9): every column profile has net -pi/A per radial ray (z 0); the model's throat is on our "
        "plane (g 0) under one positive tension on both sheets (p139 0); power-law columns untrapped at p = +1, k = sqrt3 "
        "and p = -1, k = sqrt5 (COL-POWER untrapped 1); a = 0 is AdS5 (NOCOL z 1)",
        ok10 and c10["net per ray = -pi/A, never zero"] and c10["general-profile R(k,k) = -2A^2/rho^4"]
        and mvr["throat on our plane (against (G))"] and mvr["one positive tension on both sheets (against 139 (1))"]
        and all(v > 0 for v in sc["p=+1 k=1.7321"][0]) and all(v > 0 for v in sc["p=-1 k=2.2361"][0])
        and c10["a = 0 is AdS5"])
    S = f["S"]
    add("F3 STRUCTURAL: the model's warp ell/(ell + |w|) jumps in d_w ln only at w = 0 (one plane: c166 0); a power-law "
        "column's plane slice is u^2 + a^2 (a throat on the plane: COL-POWER g 0); the bulk-centred field's source sits at "
        "w = w_c > 0, on neither plane (BULKFIELD g 1); at a = 0 there is no throat on the plane (NOCOL g vacuous)",
        sp.simplify(S["lapse"] - ell / (ell + mod("b4c_far").w)) == 0 and S["atoms"] == {sp.Abs(sp.Symbol("w_r", real=True))}
        and sp.simplify(S["kinks"]["0"] + 2 / ell) == 0 and all(v == 0 for k, v in S["kinks"].items() if k != "0")
        and S["col_plane"] == 0 and S["centre_inv"] == 0 and S["wc_positive"] is True and S["a0_throat"] is False)
    ok12, c12 = f["C12"]
    scans = c12["scans (test extension)"]
    add("F4 computed (b4c_far X11): at a = 0 every W >= U is untrapped at every ell (z3) -> NOCOL untrapped 1; the "
        "bulk-centred field at k = sqrt3 untrapped at both README sizes, with the deduced sufficient bound -> BULKFIELD "
        "untrapped 1; the round surface with the field on is trapped (the test can fail)",
        ok12 and c12["z3: Q >= 3 at a = 0 for K >= 1"]
        and all(v > 0 for k, v in scans.items() if "k=sqrt3 c=" in k)
        and all(v[0] and v[1] for k, v in scans.items() if "sufficient bound" in k)
        and all(v < 0 for k, v in scans.items() if "k=1 c=" in k))
    ok9, c9 = f["C9"]
    add("F5 computed (b4c_far X8): with eq. (17)'s far field on our plane, k*(U) is finite at both sizes (1.862 at "
        "N = 1e3, 1.7320586 at the example) -> COL-FIELD untrapped 1 for k > k*(U); 1.74 is trapped at N = 1e3 and sqrt3 at "
        "small c, so the shape must grow for small READMEs",
        ok9 and abs(c9["k* at N = 1e3"] - 1.8619) < 1e-3 and abs(c9["k* = sqrt(3/(1 - 3 gamma m/U)) at the example"]
                                                              - 1.7320586) < 1e-6
        and c9["scans"]["E1 k=1.74 c=1e-6 at N=1e3"] < 0 and c9["scans"]["E1 k=sqrt3 c=1e-6"] < 0)
    from fractions import Fraction as Fr
    br = f["S7"]
    add("F6 computed (b4d_stage7 K4): six small-separation branches, position 2's tension negative in every one "
        "(-1/3, -1/6 against ours +4/3) -> SLAB p139 1; every branch has a decaying outer bulk",
        len(br) == 6 and all(b_["s2"] < 0 for b_ in br) and {b_["s2"] for b_ in br} == {Fr(-1, 3), Fr(-1, 6)}
        and all(min(b_["a1"], b_["a2"]) < 0 for b_ in br))
    B = f["BR"]
    sols = B["sols"]
    ratio = [(s_["ten"] + B["target"]) / B["o"]["lam"] for s_ in sols]
    Bc = f["BRc"]["sols"]
    add("F7 computed (modelc.py C6, recomputed): the bridge at RS on ell_s (L1 = 2: u1 = mu = 4/3, lam = 2) has a "
        "position-2 plane at exactly -1/4 of ours with balance and tension met (to 1e-40), ell_2 = 0.6623 ell_s < 1 -> "
        "BRIDGE-NEG p139 1; control: +1/4 asked, the plane at that root still carries -1/4 (tension unmet)",
        len(sols) == 1 and all(abs(s_["bal"]) < 1e-40 and abs(s_["ten"]) < 1e-40 for s_ in sols)
        and abs(float(sols[0]["L2"]) - 0.66227) < 1e-4 and all(abs(float(r_) + 0.25) < 1e-30 for r_ in ratio)
        and all(abs(s_["ten"]) > 0.5 for s_ in Bc))
    import math
    add("F8 computed (p2_full.py TS; ITEM178 2): a pure tension crossed at angle a gives sigma sin a, so a NEGATIVE "
        "pure tension gives negative null energy at every crossing angle (the premise of H-NEG-PLANE-UNPAIRED, not a "
        "cell); control: a positive tension gives positive",
        all(v < 0 and abs(v + 0.5 * math.sin(a_)) < 1e-12 for a_, v in f["TS"])
        and all(v > 0 for _, v in f["TSc"]))
    mn = cy["main"]
    alph = next(iter(mn.values()))["_alphabets"]
    add("X1 cypher, the six far models with a computed far boundary: 139 (1) and 166 take only the value 0, so T-FAR "
        "lies outside the box and all five languages refuse it under every coding (STRUCTURAL: the record's gap)",
        alph["p139"] == [0] and alph["c166"] == [0]
        and all(r[l] is not None and r[l]["far"] == [] for r in mn.values() for l in LANGS))
    sm = {l: summary(mn, l, "zg") for l in LANGS}
    main_labels = sorted(NAMES[c[0]] for c in MAIN)
    add("X2 cypher, T-ZG (corridor, untrapped, (Z), (G)) on those six: statistics refuses under all 24 codings, the one "
        "unseen status pair being (corridor 1, (Z) 1); order, algebra, information admit under all 24 and geometry under "
        "exactly the 12 with U above 1, inventing a corridor far model that keeps (Z) and (G) under a label that moves "
        "with the coding (all six labels occur)",
        sm["statistics"]["admits"] == 0 and sm["statistics"]["n"] == 24 and cy["missing_main"] == [("corridor", "z")]
        and all(sm[l]["admits"] == 24 and sm[l]["labels"] == main_labels for l in ("order", "algebra", "information"))
        and sm["geometry"]["admits"] == 12 and sm["geometry"]["high"] == 12)
    ex = cy["ext"]
    se = {l: summary(ex, l, "far") for l in LANGS}
    add("X3 cypher, all eight cells (SLAB and BRIDGE-NEG added, their far boundary unknown): statistics refuses T-FAR "
        "under all 32 codings", se["statistics"]["n"] == 32 and se["statistics"]["admits"] == 0)
    add("X4 cypher over-reach: order, algebra, information admit T-FAR in exactly the 16 codings with the unknown ranked "
        "below 0, never above 1; geometry never; the invented label moves with the coding (all eight occur): an artefact",
        all(se[l]["admits"] == 16 and se[l]["low"] == 16 and se[l]["high"] == 0 and len(se[l]["labels"]) == 8
            for l in ("order", "algebra", "information")) and se["geometry"]["admits"] == 0)
    ct = cy["ctrl"]
    add("X5 CONTROL: every unknown set favourable -> statistics admits T-FAR exactly as BRIDGE-NEG (the verdict flips on "
        "that cell); the other four also admit SLAB with its (G) = 0 overridden",
        [NAMES[h[0]] for h in ct["statistics"]["far"]] == ["BRIDGE-NEG"]
        and all([NAMES[h[0]] for h in ct[l]["far"]] == ["SLAB", "BRIDGE-NEG"] for l in ("order", "algebra", "geometry",
                                                                                     "information")))
    want = [[("BRIDGE-NEG", "untrapped"), ("BRIDGE-NEG", "z")]]
    add("X6 WHAT MOVES IT: the only minimal set of unknown entries (model axis) whose favourable value makes statistics "
        "admit T-FAR is {BRIDGE-NEG untrapped, BRIDGE-NEG (Z)}; no single entry suffices; unchanged with H-G-VACUOUS "
        "replaced by (G) unmet where there is no corridor",
        cy["mins"] == want and cy["var"]["nocol_g0"]["axis"] == want)
    vn = cy["var"]["neg_unpaired"]
    add("X7 reading H-NEG-PLANE-UNPAIRED (BRIDGE-NEG (Z) = 0): no set of the remaining unknowns moves statistics on the "
        "model axis; in the projection only sets that take (Z) from SLAB do (pairwise stitching, an artefact)",
        vn["axis"] == [] and len(vn["proj"]) >= 1 and all(("SLAB", "z") in S_ for S_ in vn["proj"]))
    add("X8 projection (no model axis): the unseen (1, 1) pairs are exactly (corridor, z), (untrapped, p139), "
        "(untrapped, c166), (z, p139), (z, c166); every language refuses T-FAR there; its minimal sets include "
        "{SLAB untrapped, SLAB z}, which the model axis refuses (SLAB fails (G))",
        cy["missing"] == [("corridor", "z"), ("untrapped", "p139"), ("untrapped", "c166"), ("z", "p139"), ("z", "c166")]
        and all(cy["proj"][l] is not None and cy["proj"][l]["far"] == [] for l in LANGS)
        and [("SLAB", "untrapped"), ("SLAB", "z")] in cy["mins_proj"])
    add("X9 reading H-STAGE7-AS-G (SLAB's (G) read as met): {SLAB untrapped, SLAB (Z)} becomes a second minimal set",
        sorted(cy["var"]["slab_g"]["axis"]) == sorted(want + [[("SLAB", "untrapped"), ("SLAB", "z")]]))
    return res


MUTANTS = {"seat_far": "a far model meeting all four seated as data",
           "unknown_as_one": "every uncomputed entry guessed favourable",
           "owner_k29": "b4c_far's theorem run at K >= 29/10 (z3 finds a counterexample)",
           "owner_p2_negative": "b4c_far's model with position 2 on a negative plane (its 139 conflict vanishes)",
           "bridge_plus": "the bridge's position-2 plane asked at +1/4 of ours",
           "slab_g1": "SLAB's (G) set met in code (the 179 re-read decided)",
           "drop_bridge": "BRIDGE-NEG left out",
           "neg_tension_plus": "the negative tension's crossing taken with the positive sign"}


def selftest():
    t0 = time.time()
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d  (%.0f s)" % (k, len(r), time.time() - t0))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s: %s" % (type(ex).__name__, ex)]
        MUT.clear()
        caught += bool(failed) and not any(x.startswith("raised") for x in failed)
        print("  mutant %-17s %-64s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("far_cypher.py -- the chain input FAR through the cypher (a classification of the board's encoding)\n")
    print("cells (model, corridor, untrapped, z, g, p139, c166; 2 = not computed):")
    for c in cells("ext"):
        print("  %-12s %s" % (NAMES[c[0]], c[1:]))
    cy = d["cy"]
    for which, tk in (("main", "far"), ("main", "zg"), ("ext", "far")):
        print("\n%s index, target %s:" % (which, tk))
        for l in LANGS:
            s_ = summary(cy[which], l, tk)
            print("  %-12s admits under %2d of %d codings (U above 1: %d, U below 0: %d); invented labels %s"
                  % (l, s_["admits"], s_["n"], s_["high"], s_["low"], s_["labels"]))
    print("\ncontrol (unknowns favourable):", {l: [NAMES[h[0]] for h in v["far"]] for l, v in cy["ctrl"].items()
                                                if l != "_alphabets"})
    print("minimal sets moving statistics (model axis):", cy["mins"])
    print("minimal sets (projection):", cy["mins_proj"])
    print("unseen (1, 1) pairs (projection):", cy["missing"])
    for v, r in cy["var"].items():
        print("variant %-13s axis %s | projection %s" % (v, r["axis"], r["proj"]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
