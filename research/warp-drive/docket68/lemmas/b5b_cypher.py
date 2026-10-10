#!/usr/bin/env python3
"""b5b_cypher.py -- B5'b (a smooth wall carrying both universes' matter that keeps null energy at every point exists;
OPEN in B1-MATTER.md) put to the cypher: the computed walls and thickenings as cells, and which cell the cypher says is
missing.  (computed, deduced; not verified by a separate session; not seated; 2026-10-10)

THE QUESTION.  B1-MATTER.md left B5'b OPEN: "B5b's exact wall is matter-free, a limit under 184."  With matter only
algebra is shown: "These thickenings are algebra, not Einstein solutions."  Its input reads "an exact thick wall with
matter (OPEN)".  Asked here: put every wall and thickening the board has computed -- exact or algebraic, with matter or
none, null energy at every point or not -- to the cypher, and read off what is missing.

M'S WORDS (verbatim, typing kept; guard Q0 finds each inside M's own item block of M-RULINGS-2026-10-03.md):
  184  "There are no matter free planes"
  117  "An NEC is never violated"        120  "it was an methaphor to describe that the NEC only ever appears to break,
       but never does"
  183  M chose "Yes: never violated as a pair" (the option's words are the board's)     187  (3) "Seat both" -- seating
       clause (Z), the board's wording: null energy never violated holds net along each light ray
  127  "1 - yes" (the planes coincide, the extra dimension included)
  139  "2 - positive, and you have to prove it."
  202  "perhaps different values though" ... "If position 2 is on the same plane as position 1 then the energies are the
       same"
  129  "so it adds nothing to either position."
  80   "a thick brane. Each stays OPEN. - exhaustively test these"
  149  "I have given you everything I can. You have to work the math now"
  196  "All questions get works through the cypher"
The board's notes quoted here are checked where they are said to be (guard Q1).

THE OWNERS' RESULTS (imported by path; each computed or deduced there, checked here against its numbers):
  S1 (computed, b5_positive.py B5b) the scalar domain wall A = -(w/ell) ln cosh(y/w): the metric's Einstein tensor gives
     phi'^2 = -3A'' = 3 sech^2(y/w)/(w ell) > 0, so T_kk = (k.dphi)^2 >= 0 at every point; as w -> 0, A' -> -1/ell, the
     Randall-Sundrum plane.  It carries no universe's matter
  S2 (computed, b5_positive.py B5a) the summed tension +lambda_RS on one shared profile: lambda_RS f(y) k_y^2 >= 0 at every
     depth; control: the -1/3 sheet twice as wide goes negative at y = 3w (-0.009818 lambda_RS/w)
  S3 (computed, bulk/escape.py D1) for e^{2A} eta + dy^2, G_kk = -3 A'': +3 at a warp maximum, -3 at a minimum -- a
     negative-tension plane thickened breaks null energy (ESCAPE.md, READ: "Only positive tension brane configurations
     can be smoothed")
  S4 (computed, b1_matter.py C4) the thin composite at coincidence (127), summed tension 4/3 - 1/3 = 1, both universes'
     matter with position 2's as ours: coefficients 3.772e60 (k_y^2) and 0.6306 (k_space^2), units rho_c0; position 2's
     plane alone -1.257e60; one shared profile (one universe's components, DESY5 fit at a = 0.5, a tangential ray)
     1.369, 0.5037, 1.69e-4, 3.18e-16 at depths 0, 1, 3, 6 widths; per-component control (phantom dark energy twice as
     wide as the matter) -0.003571 at 3 widths
  S5 (computed, b1_matter.py B3, C1, C3) our plane alone: the closed-form bulk off a thin FRW plane carrying dust, and
     dust + Lambda, is exact (every Einstein component zero, maximally symmetric: pure AdS5); the bulk's R(k,k) = 0; the
     plane's rho + p > 0 through today in all 8 fits read
  S6 (READ from chain_cypher.py ROWS, read only) B2 PROVED, Z3a DERIVED, B5a DERIVED, B5p OPEN, B5b OPEN

THE CELLS (H-CYPHER-B5B-INDEX, the board's encoding; each cell's source is in a comment at cells()).  Coordinates:
  smooth (0 a thin sheet, 1 a profile of finite width); exact (0 a stress profile only, no metric solved; 1 a metric
  whose 5D Einstein tensor was computed exactly; U not computed); matter (0 none -- tension or the wall's scalar; 1 one
  universe's matter; 2 both universes'); nec (0 negative for some null ray somewhere, computed; 1 non-negative at every
  point computed; U not computed).  U = 9 is a distinct code, never a guess.  No per-cell key (forming_rim.py F7: a key
  makes statistics return the table itself).  Within one universe, 202 makes position 2's matter ours (b5p_cypher.py's
  H-WITHIN-IS-SAME-PLANE); between universes every null-energy value resting on that is entered U.
  TARGET, B5'b's wall: (smooth 1, exact 1, matter 2, nec 1).

WHAT THE CYPHER SAYS (computed; tools/cypher.py, roster 1173, the five operator-bearing languages; statistics is
pairwise-marginal support and coding-independent, so it carries the verdict):
  Y1 within one universe statistics refuses the target, and its only blocking pair is (exact, matter): no computed
     configuration is an exact solution carrying both universes' matter.  Every pair with null energy held is supplied
     (with smooth: S1, S2, S4's profile; with exact: S1, S5; with both matters: S4's thin composite and profile)
  Y2 at order 3 it refuses, blocking (smooth, exact, matter) and (exact, matter, nec) -- both through (exact, matter)
  Y3 over-reach, named: at order 2 statistics admits a smooth exact wall carrying ONE universe's matter and keeping null
     energy (1, 1, 1, 1), assembled from pairs of S1, S4's profile and S5; order 3 refuses it, blocked by the same
     triple (smooth, exact, matter).  The missing construction is not peculiar to two universes: no smooth exact wall
     with any matter is among the computed cells
  Y4 control on the decisive cell: the thin composite's exactness entered 1 instead of U (the board's
     H-COMPOSITE-ONE-RS-PLANE, not computed) -- order 2 then ADMITS the target (the verdict flips: an over-reach from
     pairs), order 3 still refuses, and its only blocking triple is (smooth, exact, matter), with nec in none
  Y5 between universes: order 2 blocks (exact, matter) and (matter, nec) -- the second is B5'p's unknown between
     universes (b5p_cypher.py: "Between universes B5'p stays OPEN"); order 3 adds (smooth, matter, nec).  Control:
     position 2's matter set as ours (C4's example) -- the (matter, nec) block goes and (exact, matter) stays
  Y6 statistics returns one admitted set under all 144 codings within and all 432 between (every permutation of every
     coordinate's values, forming_rim.py's _codings)
  Y7 order, algebra, geometry and information each admit the target under some codings and refuse it under others --
     within 112, 112, 80 and 48 of 144; between 240, 240, 144 and 72 of 432.  Even with every axis in its own sense the
     verdict moves: within, order, algebra and information admit it wherever U is placed and geometry only with U
     placed high; between, the first three only with U placed low and geometry never.  An artefact of ordering the
     values, not a reading
  Y8 algebra's over-reach under the natural coding is the coordinatewise join of S1's wall (exact, matter-free) and S4's
     profile with both matters (algebraic): the two halves the board has, joined by an operation with no physical
     counterpart
  L1 logic (determined(), b6p_scale.py's, through b1_matter.py): on the eleven within-one-universe cells null energy at
     every point is fixed by (summed tension sign, profile) -- positive summed tension on one profile (shared, a single
     scalar, or thin) keeps it, split profiles or a negative sheet alone break it -- and not by (smooth, exact, matter),
     nor by tension or profile alone

THE BOARD'S READINGS (named; withdrawn if M says otherwise):
  H-CYPHER-B5B-INDEX  the encoding above, and which configurations are cells
  H-P2-AS-OURS  B1-MATTER.md's example; within one universe it is 202's words (b5p_cypher.py).  The cells with both
     matters on a profile (C7, C9 at cells()) are deduced from S4 by it: position 2's components equal to ours double the
     tangential coefficient, same sign -- B1-MATTER.md says of the composite "A thickening with one shared profile stays
     positive at every depth."
  H-COMPOSITE-ONE-RS-PLANE (the Y4 control only)  under C4's doubled count the summed tension is lambda_RS itself, so the
     thin composite would be one Randall-Sundrum plane carrying the summed matter, which S5's closed form (symbolic
     density) covers -- deduced, never computed for the composite.  Under 200 (1) the summed tension is 3/4, and within
     one universe on 202 it is 2 sigma (b5p_cypher.py), where S5's balanced form does not apply; so the main index keeps
     the composite's exactness unknown
  H-B5B-POINTWISE  B5'b as worded asks null energy at every point; seated (Z) asks it net along each light ray (183,
     187).  A pointwise wall meets (Z); the converse fails -- S2's control is negative at 3w, but its two normalised
     profiles integrate along a crossing ray to (4/3 - 1/3) lambda_RS > 0 (deduced here; not entered as a cell).  The
     index's nec is pointwise, as B5'b is worded
  H-NEC-BY-PROFILE  L1 is a regularity over eleven computed cells, not a derivation: it does not compute the missing
     wall's null energy

SO (the board's decision, under 149): B5'b stays OPEN, and the cypher names what is missing: the triple (smooth, exact,
matter) -- an exact smooth solution of the 5D Einstein equations carrying matter, for one universe's matter as much as
for both.  Within one universe null energy is never the blocking coordinate: it enters a blocking tuple only through
(exact, matter), and every computed wall with positive summed tension on one profile keeps it, matter or none, exact or
algebraic.  Between universes B5'b also waits on B5'p's unknown.  No question for M: building the wall is mathematics
(149).  Proposed, not seated: B5'b's input re-worded from "an exact thick wall with matter (OPEN)" to "an exact smooth
wall carrying matter, none computed even for one universe's matter (OPEN); between universes also B5'p (OPEN)".
WHAT IT DOES NOT SHOW.  (1) Whether the wall exists: the cypher classifies the cells, it solves no field equation.
  (2) Matter is the homogeneous model's mean (C3, C4), through H-OUR-PLANE-IS-FRW (B1-MATTER.md).  (3) The profiles
  with matter are tangential rays only; their k_y^2 term was not computed, and the doubled cells are deduced, not
  computed profiles with two universes' components.  (4) S5 is the closed form at zero dark radiation (C = 0), up to the
  depth where a vanishes.  (5) The codings swept include orders against each axis's natural sense; the natural-coding
  verdicts are reported beside them.
Imports by path (never copied): lemmas/b5_positive.py (b5a, b5b), bulk/escape.py (thick_nec), lemmas/b1_matter.py
(check_B3, check_C1, check_C3, check_C4, determined), lemmas/chain_cypher.py (ROWS), lemmas/forming_rim.py (_codings),
tools/cypher.py.  Stdlib + sympy.  About 15 s.  python3 b5b_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
_CACHE = {}
LANGS = ("order", "algebra", "geometry", "information", "statistics")
ORDER_DEP = ("order", "algebra", "geometry", "information")


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod_ = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod_
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod_)
    finally:
        sys.path[:] = saved
    return mod_


def mod(name):
    paths = {"b5": os.path.join(HERE, "b5_positive.py"), "b1": os.path.join(HERE, "b1_matter.py"),
             "esc": os.path.join(D68, "bulk", "escape.py"), "cc": os.path.join(HERE, "chain_cypher.py"),
             "fr": os.path.join(HERE, "forming_rim.py"), "cy": os.path.join(ROOT, "tools", "cypher.py")}
    if name not in _CACHE:
        _CACHE[name] = _load(paths[name], "b5b_" + name)
    return _CACHE[name]


def _once(key, fn):
    """an owner's result, computed once per process; mutants act on this file's use of it, never on the owner"""
    k = "res_" + key
    if k not in _CACHE:
        with contextlib.redirect_stdout(io.StringIO()):
            _CACHE[k] = fn()
    return _CACHE[k]


# ---------------------------------------------------------------------------------------------------------- Q0, Q1
M_WORDS = {
    184: ["There are no matter free planes"],
    117: ["An NEC is never violated"],
    120: ["it was an methaphor to describe that the NEC only ever appears to break, but never does"],
    183: ["Yes: never violated as a pair"],
    187: ["Seat both"],
    127: ["1 - yes"],
    139: ["2 - positive, and you have to prove it."],
    202: ["perhaps different values though",
          "If position 2 is on the same plane as position 1 then the energies are the same"],
    129: ["so it adds nothing to either position."],
    80: ["a thick brane. Each stays OPEN. - exhaustively test these"],
    149: ["I have given you everything I can. You have to work the math now"],
    196: ["All questions get works through the cypher"],
}
NOTES = {os.path.join(HERE, "B1-MATTER.md"): ["B5b's exact wall is matter-free, a limit under 184.",
                                              "These thickenings are algebra, not Einstein solutions.",
                                              "an exact thick wall with matter (OPEN)",
                                              "A thickening with one shared profile stays positive at every depth.",
                                              "A per-component thickening with phantom dark energy goes negative "
                                              "(C4's control)."],
         os.path.join(HERE, "ITEM185-MATTER-ROUND.md"): ["Position 2's matter fixes only ratios, and nothing gives its "
                                                         "amount."],
         os.path.join(D68, "bulk", "ESCAPE.md"): ["Only positive tension brane configurations can be smoothed"],
         os.path.join(HERE, "b5p_cypher.py"): ["within one universe, 202 settles B5'p",
                                               "Between universes B5'p stays OPEN"]}
_norm = lambda s: " ".join(s.split())


def quotes_ok():
    text = open(RULINGS, encoding="utf-8").read()
    blocks, cur, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^(\d+)\. ", line)
        if m:
            if cur is not None:
                blocks[cur] = " ".join(buf)
            cur, buf = int(m.group(1)), [line]
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        blocks[cur] = " ".join(buf)
    words = {k: list(v) for k, v in M_WORDS.items()}
    if MUT.get("misquote"):
        words[184][0] = "There are no matter free walls"
    return [(k, q) for k, qs in words.items() for q in qs if k not in blocks or _norm(q) not in _norm(blocks[k])]


def notes_ok():
    bad = []
    for f, qs in NOTES.items():
        t = _norm(open(f, encoding="utf-8").read())
        bad += [(os.path.basename(f), q) for q in qs if _norm(q) not in t]
    return bad


# ---------------------------------------------------------------------------------------------------------- S1-S6
def s_b5():
    return {"a": _once("b5a", lambda: mod("b5").b5a()), "b": _once("b5b", lambda: mod("b5").b5b())}


def s_esc():
    mx = _once("esc_max", lambda: mod("esc").thick_nec())
    mn = _once("esc_min", lambda: mod("esc").thick_nec(minimum=True))
    if MUT.get("escape_max"):                      # the thick negative plane read at a warp maximum
        mn = mx
    return {"max": mx, "min": mn}


def s_c4():
    ok, c4 = _once("c4", lambda: mod("b1").check_C4())
    c4 = dict(c4)
    if MUT.get("ctrl_sign"):                       # the per-component control read without its sign
        c4["per_component_control_at_3w"] = abs(c4["per_component_control_at_3w"])
    return ok, c4


def s_ours():
    return {"B3": _once("b3", lambda: mod("b1").check_B3()), "C1": _once("c1", lambda: mod("b1").check_C1()),
            "C3": _once("c3", lambda: mod("b1").check_C3())}


def s_status():
    rows = {r[0]: (r[1], r[2]) for r in mod("cc").ROWS}
    return {k: rows.get(k) for k in ("B2", "Z3a", "B5a", "B5p", "B5b")}


# ---------------------------------------------------------------------------------------------------------- cells
C = ["smooth", "exact", "matter", "nec"]
U = 9                                                             # not computed: a distinct code
TARGET = (1, 1, 2, 1)                                             # B5'b's wall
ONE = (1, 1, 1, 1)                                                # the same wall with one universe's matter
WITH_P2 = ("C4-thin", "C4-shared-2", "C4-split-2", "C4-p2alone")  # nec rests on position 2's matter being ours


def _ours_nec(ours):
    c3 = ours["C3"][1]["fits"]
    return ours["C1"][1]["bulk_Rkk"] == "0" and len(c3) == 8 and all(r["net_min_through_today"] > 0 for r in c3.values())


def _ours_exact(ours):
    b3 = ours["B3"][1]
    return all(all(b3[n]["components_zero"].values()) and b3[n]["max_symmetric"] for n in ("dust", "LCDM"))


def cells(d, between=False, thin_exact=False, p2_as_ours=False):
    """(label, (smooth, exact, matter, nec), (summed tension sign, profile)) per configuration computed or deduced;
    the last pair is for logic (L1) only, not given to the cypher."""
    b5, esc, c4, ours = d["b5"], d["esc"], d["c4"][1], d["ours"]
    sg = lambda ok: 1 if ok else 0
    pos = lambda xs: all(x > 0 for x in xs)
    known = (not between) or p2_as_ours or MUT.get("between_known")   # 202 within one universe; unknown between
    out = [
        # S1 b5_positive.py B5b (computed): exact (phi'^2 = -3A'' from the metric), phi real, so T_kk >= 0 everywhere;
        # no universe's matter (B1-MATTER.md: "B5b's exact wall is matter-free, a limit under 184.")
        ("B5b", (1, 1, 2 if MUT.get("b5b_matter") else 0, sg(b5["b"]["einstein_rel"] and b5["b"]["phi_real"])),
         (1, "scalar")),
        # S2 b5_positive.py B5a (computed): the summed tension on one shared profile, lambda_RS f(y) k_y^2 >= 0
        ("B5a-shared", (1, 0, 0, sg(b5["a"]["shared_nonneg"])), (1, "shared")),
        # S2 b5_positive.py B5a control (computed): the negative sheet twice as wide, negative at y = 3w
        ("B5a-ctrl", (1, 0, 0, sg(not b5["a"]["diff_negative_far"])), (1, "split")),
        # S3 bulk/escape.py D1 (computed): a warp minimum, position 2's negative plane thickened: G_kk = -3 at the centre
        ("D1-min", (1, 1, 0, sg(esc["min"][1] >= 0)), (0, "scalar")),
        # S4 b1_matter.py C4 (computed): the thin composite (127) with both universes' matter, position 2's as ours
        # (H-P2-AS-OURS; 202 within one universe); the composite's exactness is not computed (U)
        ("C4-thin", (0, 1 if (thin_exact or MUT.get("thin_exact")) else (0 if MUT.get("unknown_as_zero") else U), 2,
                     sg(pos([c4["instance_coef_k_y^2"], c4["instance_coef_k_space^2"]])) if known else U), (1, "thin")),
        # S4 b1_matter.py C4 (computed): one shared profile, one universe's components, a tangential ray, 4 depths
        ("C4-shared-1", (1, 0, 1, sg(pos(c4["shared_profile_depths"]))), (1, "shared")),
        # deduced from S4 with 202 (H-P2-AS-OURS): position 2's components = ours double the coefficient, same sign
        ("C4-shared-2", (1, 0, 2, sg(pos(c4["shared_profile_depths"])) if known else U), (1, "shared")),
        # S4 b1_matter.py C4 control (computed): phantom dark energy twice as wide as the matter, negative at 3 widths
        ("C4-split-1", (1, 0, 1, sg(c4["per_component_control_at_3w"] >= 0)), (1, "split")),
        # deduced from S4's control with 202: doubled, same sign
        ("C4-split-2", (1, 0, 2, sg(c4["per_component_control_at_3w"] >= 0) if known else U), (1, "split")),
        # S5 b1_matter.py B3 (exact closed form, dust and dust + Lambda), C1 (bulk R(k,k) = 0), C3 (rho + p > 0 today)
        ("B3-ours", (0, sg(_ours_exact(ours)), 1, sg(_ours_nec(ours))), (1, "thin")),
        # S4 b1_matter.py C4 (computed): position 2's plane alone, matter as ours, negative for crossing rays;
        # its exactness not computed (U)
        ("C4-p2alone", (0, U, 1, sg(c4["p2_alone_coef_k_y^2"] >= 0) if known else U), (0, "thin")),
    ]
    if MUT.get("seat_wall"):                                      # a guess entered as data
        out.append(("seated", TARGET, (1, "scalar")))
    return out


# ---------------------------------------------------------------------------------------------------------- cypher
def _present(cs):
    return [sorted({c[1][i] for c in cs}) for i in range(len(C))]


def natural_orders(cs, unk_low):
    """each axis in its own sense (thin < smooth, algebra < exact, none < one < both, fails < holds), U placed low or high"""
    pr = _present(cs)
    vo = {}
    for i, name in enumerate(C):
        base = [v for v in pr[i] if v != U]
        vo[name] = ([U] + base if unk_low else base + [U]) if U in pr[i] else base
    return vo


def all_orders(cs):
    """every permutation of every coordinate's values (forming_rim.py's _codings, imported)"""
    pr = _present(cs)
    perms = [[[v[k] for k in p] for p in mod("fr")._codings(len(v))] for v in pr]
    for combo in itertools.product(*perms):
        yield {name: list(combo[i]) for i, name in enumerate(C)}


def ask(cs, vo, lang, opts=None):
    """the decoded admitted cells, or None if the language is silent"""
    cy = mod("cy")
    ix = cy.Index("b5b", C, [list(c[1]) for c in cs], value_order=vo)
    inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
    out, _ = cy.ADMISSION[lang][0](ix, opts or {})
    return None if out is None else {tuple(inv[i][x[i]] for i in range(len(C))) for x in out}


def blocking(cs, tgt, k):
    """the k-tuples of coordinates on which the target's projection is seen in no cell"""
    rows = [c[1] for c in cs]
    return sorted(tuple(C[i] for i in S) for S in itertools.combinations(range(len(C)), k)
                  if tuple(tgt[i] for i in S) not in {tuple(r[i] for i in S) for r in rows})


def stats(cs):
    vo = natural_orders(cs, True)
    s2 = ask(cs, vo, "statistics", {"statistics_order": 2})
    s3 = ask(cs, vo, "statistics", {"statistics_order": 3})
    return {"t2": TARGET in s2, "t3": TARGET in s3, "one2": ONE in s2, "one3": ONE in s3,
            "b2": blocking(cs, TARGET, 2), "b3": blocking(cs, TARGET, 3), "one_b3": blocking(cs, ONE, 3),
            "n2": len(s2), "n3": len(s3), "ncells": len({c[1] for c in cs})}


def sweep(cs):
    """every language under every coding: does it admit the target?  And statistics' admitted set, coding by coding."""
    res = {l: [] for l in LANGS}
    stat_sets = set()
    for vo in all_orders(cs):
        for l in LANGS:
            a = ask(cs, vo, l)
            res[l].append(None if a is None else TARGET in a)
            if l == "statistics" and a is not None:
                stat_sets.add(frozenset(a))
    nat = {}
    for l in LANGS:
        nat[l] = []
        for ul in (True, False):
            a = ask(cs, natural_orders(cs, ul), l)
            nat[l].append(None if a is None else TARGET in a)
    count = {l: (sum(1 for x in r if x), sum(1 for x in r if x is False), sum(1 for x in r if x is None), len(r))
             for l, r in res.items()}
    return {"count": count, "stat_invariant": len(stat_sets) == 1, "nat": nat}


def join_mechanism(cs):
    """Y8: under the natural coding, the coordinatewise join (algebra's operation) of S1's wall and S4's profile with
    both matters"""
    vo = natural_orders(cs, True)
    code = [{v: r for r, v in enumerate(vo[name])} for name in C]
    dec = [{r: v for v, r in m.items()} for m in code]
    rows = {c[0]: c[1] for c in cs}
    a, b = rows["B5b"], rows["C4-shared-2"]
    j = tuple(dec[i][max(code[i][a[i]], code[i][b[i]])] for i in range(len(C)))
    return {"join": j, "in_algebra": TARGET in (ask(cs, vo, "algebra") or set())}


def cypher_runs(d):
    w = cells(d)
    b = cells(d, between=True)
    return {"within": w, "between": b, "st_w": stats(w), "st_b": stats(b),
            "st_fav": stats(cells(d, thin_exact=True)), "st_bctl": stats(cells(d, between=True, p2_as_ours=True)),
            "sw_w": sweep(w), "sw_b": sweep(b), "join": join_mechanism(w)}


# ---------------------------------------------------------------------------------------------------------- L1
def logic(cs):
    det = mod("b1").determined                                    # b6p_scale.py's, through b1_matter.py
    coords = C + ["tension", "profile"]
    rows = [list(c[1]) + list(c[2]) for c in cs]
    return {"by_tp": det(rows, coords, ["tension", "profile"], "nec"),
            "by_sem": det(rows, coords, ["smooth", "exact", "matter"], "nec"),
            "by_t": det(rows, coords, ["tension"], "nec"), "by_p": det(rows, coords, ["profile"], "nec"),
            "keep": sorted({(r[4], r[5]) for r in rows if r[3] == 1}), "break": sorted({(r[4], r[5]) for r in rows
                                                                                       if r[3] == 0})}


# ---------------------------------------------------------------------------------------------------------- run
def compute():
    d = {"q0": quotes_ok(), "q1": notes_ok(), "b5": s_b5(), "esc": s_esc(), "c4": s_c4(), "ours": s_ours(),
         "st": s_status()}
    d["cy"] = cypher_runs(d)
    d["logic"] = logic(d["cy"]["within"])
    return d


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Q0 every quote of M's is inside M's own item block of M-RULINGS-2026-10-03.md", d["q0"] == [])
    add("Q1 every sentence quoted from the board's notes is where it is said to be", d["q1"] == [])
    b = d["b5"]["b"]
    w, ell, y = sp.symbols("w ell y", positive=True)
    add("S1 b5_positive B5b (imported): phi'^2 = -3A'' from the metric, = 3 sech^2(y/w)/(w ell) > 0 everywhere; "
        "w -> 0 gives A' -> -1/ell", b["einstein_rel"] and b["phi_real"]
        and sp.simplify(b["phi_p2"] - 3 / (w * ell * sp.cosh(y / w) ** 2)) == 0
        and sp.simplify(b["thin_limit_Aprime"] + 1 / ell) == 0)
    a = d["b5"]["a"]
    lam = sp.Symbol("lambda_RS", positive=True)
    far = float(a["S_diff_far"].subs({lam: 1, w: 1}))
    add("S2 b5_positive B5a (imported): one shared profile keeps lambda_RS f(y) k_y^2 >= 0; the control (negative sheet "
        "twice as wide) is negative at y = 3w (-0.009818 lambda_RS/w)", a["shared_nonneg"] and a["diff_negative_far"]
        and abs(far + 0.009818) < 1e-6)
    e = d["esc"]
    add("S3 escape D1 (imported): G_kk = -3 A''; +3 at a warp maximum, -3 at a minimum (a negative plane thickened)",
        str(e["max"][0]) == "-3" and abs(e["max"][1] - 3.0) < 1e-9 and str(e["min"][0]) == "-3"
        and abs(e["min"][1] + 3.0) < 1e-9)
    ok4, c = d["c4"]
    dep = c["shared_profile_depths"]
    add("S4 b1_matter C4 (imported): summed tension 1; thin composite 3.772e60 and 0.6306; position 2 alone -1.257e60; "
        "shared profile 1.369, 0.5037, 1.69e-4, 3.18e-16; per-component control -0.003571",
        ok4 and c["summed_tension"] == "1" and abs(c["instance_coef_k_y^2"] / 3.772e60 - 1) < 1e-3
        and abs(c["instance_coef_k_space^2"] - 0.6306) < 1e-4 and abs(c["p2_alone_coef_k_y^2"] / -1.2573e60 - 1) < 1e-3
        and abs(dep[0] - 1.3691) < 1e-3 and abs(dep[1] - 0.50367) < 1e-4 and abs(dep[2] / 1.6896e-4 - 1) < 1e-3
        and 0 < dep[3] < 1e-15 and abs(c["per_component_control_at_3w"] + 0.0035714) < 1e-6)
    o = d["ours"]
    add("S5 b1_matter B3, C1, C3 (imported): the bulk off a thin plane with dust and with dust + Lambda is exact (every "
        "component zero, maximally symmetric); bulk R(k,k) = 0; rho + p > 0 through today in all 8 fits",
        o["B3"][0] and _ours_exact(o) and o["C1"][0] and o["C3"][0] and _ours_nec(o))
    st = d["st"]
    add("S6 chain_cypher ROWS (read only): B2 PROVED, Z3a DERIVED, B5a DERIVED, B5p OPEN, B5b OPEN",
        st == {"B2": ("PROVED", ""), "Z3a": ("DERIVED", ""), "B5a": ("DERIVED", ""), "B5p": ("OPEN", ""),
               "B5b": ("OPEN", "")})
    cy = d["cy"]
    wi = {c[0]: c[1] for c in cy["within"]}
    be = {c[0]: c[1] for c in cy["between"]}
    add("Y0 the unknowns are where the sources leave them: within, the exactness of the thin composite and of position "
        "2's plane alone; between, also every null energy resting on position 2's matter",
        [k for k, v in wi.items() if U in v] == ["C4-thin", "C4-p2alone"] and wi["C4-thin"][1] == U
        and wi["C4-p2alone"][1] == U and all(v[3] != U for v in wi.values())
        and sorted(k for k, v in be.items() if v[3] == U) == sorted(WITH_P2))
    sw = cy["st_w"]
    add("Y1 within one universe statistics (order 2) refuses B5'b's wall; the only blocking pair is (exact, matter)",
        not sw["t2"] and sw["b2"] == [("exact", "matter")])
    add("Y2 order 3 refuses it; the blocking triples are exactly (smooth, exact, matter) and (exact, matter, nec)",
        not sw["t3"] and sw["b3"] == [("exact", "matter", "nec"), ("smooth", "exact", "matter")])
    add("Y3 over-reach named: order 2 admits a smooth exact wall with ONE universe's matter keeping null energy; order 3 "
        "refuses it, blocked by (smooth, exact, matter)", sw["one2"] and not sw["one3"]
        and sw["one_b3"] == [("smooth", "exact", "matter")])
    sf = cy["st_fav"]
    add("Y4 control: the thin composite's exactness entered 1 (not computed) -- order 2 admits the target (the verdict "
        "flips); order 3 refuses, its only blocking triple (smooth, exact, matter)", sf["t2"] and sf["b2"] == []
        and not sf["t3"] and sf["b3"] == [("smooth", "exact", "matter")])
    sb, sc = cy["st_b"], cy["st_bctl"]
    add("Y5 between universes: order 2 blocks (exact, matter) and (matter, nec); order 3 adds (smooth, matter, nec); "
        "control, position 2's matter as ours: only (exact, matter) is left", not sb["t2"]
        and sb["b2"] == [("exact", "matter"), ("matter", "nec")]
        and sb["b3"] == [("exact", "matter", "nec"), ("smooth", "exact", "matter"), ("smooth", "matter", "nec")]
        and not sc["t2"] and sc["b2"] == [("exact", "matter")])
    ww, bb = cy["sw_w"], cy["sw_b"]
    add("Y6 statistics returns one admitted set under every coding (144 within, 432 between) and refuses the target in all",
        ww["stat_invariant"] and bb["stat_invariant"] and ww["count"]["statistics"] == (0, 144, 0, 144)
        and bb["count"]["statistics"] == (0, 432, 0, 432))
    add("Y7 order, algebra, geometry, information admit the target under some codings and refuse it under others (within "
        "112, 112, 80, 48 of 144; between 240, 240, 144, 72 of 432; under the natural coding it moves with U's place): "
        "an artefact, not a reading",
        [ww["count"][l][:3] for l in ORDER_DEP] == [(112, 32, 0), (112, 32, 0), (80, 64, 0), (48, 96, 0)]
        and [bb["count"][l][:3] for l in ORDER_DEP] == [(240, 192, 0), (240, 192, 0), (144, 288, 0), (72, 360, 0)]
        and [ww["nat"][l] for l in LANGS] == [[True, True], [True, True], [False, True], [True, True], [False, False]]
        and [bb["nat"][l] for l in LANGS] == [[True, False], [True, False], [False, False], [True, False], [False, False]])
    jm = cy["join"]
    add("Y8 algebra's admission under the natural coding is the join of S1's matter-free exact wall and S4's algebraic "
        "profile with both matters", jm["join"] == TARGET and jm["in_algebra"])
    lg = d["logic"]
    add("L1 logic: null energy at every point is fixed by (summed tension sign, profile), not by (smooth, exact, matter), "
        "nor by tension or profile alone; it is kept exactly on positive tension with one profile",
        lg["by_tp"] and not lg["by_sem"] and not lg["by_t"] and not lg["by_p"]
        and lg["keep"] == [(1, "scalar"), (1, "shared"), (1, "thin")]
        and lg["break"] == [(0, "scalar"), (0, "thin"), (1, "split")])
    return res


MUTANTS = {"misquote": "184 misquoted ('no matter free walls')",
           "b5b_matter": "B5b's wall entered as carrying both universes' matter",
           "thin_exact": "the thin composite's exactness decided in code (a guess as data)",
           "unknown_as_zero": "the composite's uncomputed exactness entered as 'algebra' (0), not unknown",
           "seat_wall": "B5'b's wall seated as a cell",
           "ctrl_sign": "C4's per-component control read without its sign",
           "escape_max": "the thick negative plane read at a warp maximum",
           "between_known": "position 2's matter between universes taken as ours"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed) and not any(f.startswith("raised") for f in failed)
        print("  mutant %-16s %-66s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed
                                           else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("b5b_cypher.py -- B5'b, the smooth wall with both universes' matter, through the cypher\n")
    print("cells (smooth, exact, matter, nec; U = %d)   [tension, profile for L1]" % U)
    for key in ("within", "between"):
        print("  %s" % key)
        for c in d["cy"][key]:
            print("     %-12s %-16s %s" % (c[0], c[1], c[2]))
    for key, nm in (("st_w", "within"), ("st_fav", "within, composite exact (control)"), ("st_b", "between"),
                    ("st_bctl", "between, position 2 as ours (control)")):
        s = d["cy"][key]
        print("statistics %-38s target order 2 / 3: %s / %s   blocking pairs %s   triples %s"
              % (nm, s["t2"], s["t3"], s["b2"], s["b3"]))
        print("           %-38s one-universe wall order 2 / 3: %s / %s   blocking triples %s"
              % ("", s["one2"], s["one3"], s["one_b3"]))
    for key in ("sw_w", "sw_b"):
        sw = d["cy"][key]
        print("coding sweep %s (admit, refuse, silent, of):" % key[-1], sw["count"], " statistics invariant:",
              sw["stat_invariant"])
        print("   natural coding, U low / high:", sw["nat"])
    print("Y8 join of B5b and C4-shared-2 under the natural coding:", d["cy"]["join"])
    print("L1 logic:", d["logic"])
    print("S6 statuses:", d["st"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
