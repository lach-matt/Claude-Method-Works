#!/usr/bin/env python3
"""close_cypher.py -- the chain's input CLOSE put to the cypher: can a closing end the horizon with (Z) kept and no
partner?  (computed by import, deduced, READ; the cypher classifies, it does not derive; not verified by a separate
session; not seated; 2026-10-10)

WHAT IS ASKED.  chain_cypher.py's input CLOSE, verbatim (check Q1): "the closing's negative null flux: ending the
horizon and moving the hold need its area to shrink (README-HELD; area theorem; OPEN)".  The horizon whose area must
shrink is position 1's -- the horizon the README forms as it comes in (README-HELD.md 4: "the hold's move needs
horizon 1's area to shrink"; H-ARRIVAL-FORMS-THE-HORIZON).  Target T1: position 1's horizon ENDED, with (Z) kept
and NO partner, in either trajectory class.  Contrast T2: the same of position 2's horizon.

M'S WORDS (verbatim, checked inside the rulings file by Q1; kept apart from every reading below)
  109 "A horizon cannot exist without the object of which it needs to exist"
  115 (a) "It ends; energy moved"
  106 (b) "upon the corridor closing the bits are then held only at the horizon of position 2"
  136 (2) "2 - released at position two at the closing of the horizon"
  132 "the passage is one way by nature, a black hole in and a white hole out, side views of the same corridor object
      *different views of the same object"   (199: "For the record, I did suggest a white hole earlier on")
  183 "Yes: never violated as a pair"     195 "The README is not a pair"     198 "My guess would be 1."
  168 "My sense: positions, one universe"  (the two trajectory classes: one universe, then between universes)
  (Z) as seated on 187 (WARPTHEOREM.md, the board's wording M seated; checked by Q1): '"Never violated" holds net along
      each light ray (183): a negative member paired along the same light rays is the appearance (117/120).'

FACTS
  F1 (computed, imported close_flux.py K1) ingoing Vaidya losing mass has T_vv < 0 along the horizon's generators: the
     black-hole side's shrink is a negative influx; outgoing Vaidya losing mass has T_uu > 0: the white-hole side's
     release is positive (132's two views; OPENING.md O1: every pointwise energy condition holds for the outgoing piece
     when its mass falls)
  F2 (computed, imported close_flux.py K2) Raychaudhuri from theta = 0: positive R(k,k) shrinks the surface's area, zero
     keeps it (to 1e-12), negative grows it
  F3 (deduced, imported close_flux.py K3; standard-not-READ) within one universe position 1's horizon is no event
     horizon, so the area theorem does not bind it; between universes it is universe 1's event horizon and binds it
  F4 (deduced from (Z)'s seated wording; the board's reading H-NO-PARTNER-IS-POINTWISE) a negative member on a light ray
     is allowed only paired; with no partner there is none, so "(Z) kept, no partner" means R(k,k) >= 0 pointwise on the
     generators -- the premise the area theorem uses (standard-not-READ).  So between universes the target is excluded
     by F3 (deduced).  R(k,k) is geometric and reads as energy only under the field equation; on a plane the effective
     equations add a projected Weyl term (README-HELD 1, standard-not-READ) -- see F9
  F5 (deduced from computed: close_flux K2 'zero'; readme_held.py C7 'pre_partner', theta = 0, end area 1) a 183 pair
     cancelling pointwise along the same rays leaves R(k,k) = 0 on the generators and the area held: (Z) is kept, and
     nothing closes.  A pair ORDERED along one generator (the positive member first) is computed by no instrument and is
     not entered (OPEN)
  F6 (the record, Q5) no computed or deduced arrangement ends position 1's horizon: OPENING.md OPEN 2 ("A dynamical
     model in which both happen is OPEN"), CLOSE-FLUX.md "What it does not show" ("A closing that works ... B4d's").
     Position 2's horizon ends in OPENING.md's outgoing Vaidya piece -- imposed by m -> 0 (O4), a model choice, with the
     apparent horizon shrinking as (1 - f)^2 N (O7)
  F7 (cypher, roster 1173; the encoding is the board's, H-CYPHER-CLOSE-INDEX) six coordinates -- side (1, 2), class (one
     universe, between universes), area (grows, held, shrinks), z_kept, partner_free, ends_horizon -- with U = 9 the
     code for what nobody computed.  side and class are nominal: every run is repeated under both orders of
     each and with U above 1 and below 0 (8 codings).  Results (Q6-Q11):
       - statistics REFUSES T1 in both classes under every coding; the one unseen pair is (side 1, ends 1) -- the
         refusal is F6, the record's gap, not the area theorem.  Its one admitted cell beyond the data is (side 1,
         between universes, shrinks, (Z) kept, no partner, ending U): the very cell F3-F4 exclude, which pairwise
         support cannot see
       - order, algebra, geometry and information each ADMIT T1 under some codings and refuse it under others: 6, 6,
         4 and 4 of the 8, the same in both classes.  All four refuse with side 1 ordered first and U below 0; with U
         above 1 (the house default) order, algebra and geometry read an unknown side-1 ending as reached -- A1's OR
         A3's, either one alone: A1's ending set to 0 leaves every T1 verdict of the four unchanged under all 8
         codings, and so does A3's set to 0 (the 'trapping' variant, whose one side-1 unknown is A3's, gives the same
         6, 6, 4, 4); only both set to 0 removes the side-1-first admissions (computed, Q11; the zeros are probes, not
         readings).  With both at 0, order, algebra and information still admit T1 in the 4 codings with side 2 ordered
         first, under either placing of U -- the nominal side axis's ordering alone -- and geometry in none: all 4 of
         geometry's admissions come from the unknowns.  The verdict moves with the coding: an artefact of ordering a
         nominal axis and of where the unknowns sit, not a reading
       - T2 is data (the white-hole release), admitted by all five: forced, not informative
       - CONTROL: the decisive unknown -- whether B4d's one-universe positive closing ends the horizon (A1's U) -- set
         to 1: T1 (one universe) becomes data and all five admit it.  Statistics then ALSO admits T1 between universes,
         which F3-F4 exclude: the area theorem's exclusion is a four-way constraint (side, class, (Z) without partner,
         shrink) that order-2 marginal support cannot carry.  With the white-hole release confined to one universe
         (close_flux's own coding) statistics refuses it again: that verdict moves with an encoding choice, an
         artefact.  In the control order, algebra and geometry admit T1 between universes under all 8 codings,
         information under 6
  F8 (READ; deduced; recorded, not repaired) K2's area is that of a null surface leaving the hold's section, not
     necessarily the horizon's.  Under positive inflow README-HELD's own computed horizons grow: the trapping horizon
     r = 2M(v) holds f^2 N bits at a fraction f of E (readme_held.py C15) and the event horizon has theta > 0 throughout
     (C7).  Hayward, arXiv:gr-qc/9303006v3, abstract (READ, arXiv abstract page), verbatim: "The future outer trapping
     horizon provides the definition of a black hole." and "Future outer trapping horizons have non-decreasing area
     form, constant only in the null case---the `second law'." (the energy condition the law assumes is in the body,
     not READ: standard-not-READ).  Its marginal surfaces are "of one of four non-degenerate types".  So on the board's
     own reading H-SIZE-IS-TRAPPING-HORIZON (README-HELD 3) CLOSE-FLUX's one-universe dissolution
     (H-CLOSE-SPLITS-BY-CLASS) holds for K2's surface, not for a future outer trapping horizon; it survives only if
     position 1's horizon is degenerate (eq. (17)'s extremal horizon, surface gravity 0, clause (O)) or not outer.
     Run as the variant 'trapping': A1 replaced by the trapping horizon's computed growth; statistics still refuses
     T1, no unknown is left on a side-1 cell with (Z) kept and no partner, and the other four over-reach exactly as in
     the main run (6, 6, 4, 4 of 8) -- on A3's unknown ending alone (F7)
  F9 (STRUCTURAL; OPEN; not entered, since nothing is computed) the one route the cells leave untouched: the plane's
     reading of the closing.  The board's appearance mechanism (117/120; WARPTHEOREM (Z): "the plane's apparent
     deficit is exactly the bulk's pull") puts a negative R(k,k) on the plane through the projected Weyl term with no
     negative null energy and no partner in five dimensions.  Whether that shrinks and ends the plane's reading of
     position 1's horizon is computed by no instrument.  In the vacuum bulk R(k,k) = 0 for every null k (axioms.py Z3,
     computed), so a five-dimensional event horizon meets the area theorem's premise (deduced, standard-not-READ): the
     route needs the plane's horizon to close while the bulk's does not end, or the corridor's horizon not to be a bulk
     event horizon
NAMED READINGS (the board's, never M's): H-CYPHER-CLOSE-INDEX (the encoding); H-NO-PARTNER-IS-POINTWISE (F4);
H-RELEASE-ANY-CLASS (the outgoing-Vaidya release, computed in a model that names no class, entered in both classes);
carried: H-CLOSE-SPLITS-BY-CLASS, H-CYPHER-CLOSE (CLOSE-FLUX.md), H-SIZE-IS-TRAPPING-HORIZON,
H-ARRIVAL-FORMS-THE-HORIZON (README-HELD.md).
SO: no closing computed or deduced ends position 1's horizon, with or without (Z); statistics refuses the target on
that gap, and the other four's admissions move with the coding.  Between universes the area theorem (with F4)
excludes it outright; within one universe it waits on B4d, and on H-SIZE-IS-TRAPPING-HORIZON with a non-degenerate
horizon the second law excludes it too.  Position 2's horizon closes
lawfully (positive release, 132), which is the asymmetry M's "a black hole in and a white hole out" carries.
No question for M: 149 ("I have given you everything I can. You have to work the math now") lets the board decide
this; an ordered pair, if ever computed to close, would reopen 195/198, and F9 is B4d's.
Imports tools/cypher.py, close_flux.py and chain_cypher.py by path.  Stdlib + sympy.
python3 close_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
MUT = {}
_CACHE = {}
U = 9                                                             # not computed
LANGS = ("order", "algebra", "geometry", "information", "statistics")
C = ["side", "class", "area", "z_kept", "partner_free", "ends_horizon"]
# side 1 position 1's horizon (black-hole side, formed by the README), 2 position 2's (white-hole side, 132)
# class 0 two positions, one universe; 1 between universes (167, 168; close_flux K3)
# area 0 grows, 1 held, 2 shrinks | z_kept (Z) net per light ray | partner_free 1 no partner | ends_horizon 1 it ends
QUESTION = ("the closing's negative null flux: ending the horizon and moving the hold need its area to shrink "
            "(README-HELD; area theorem; OPEN)")
WORDS = {"109": "A horizon cannot exist without the object of which it needs to exist",
         "115 (a)": "It ends; energy moved",
         "106 (b)": "upon the corridor closing the bits are then held only at the horizon of position 2",
         "136 (2)": "2 - released at position two at the closing of the horizon",
         "132": "the passage is one way by nature, a black hole in and a white hole out, side views of the same "
                "corridor object *different views of the same object",
         "199": "For the record, I did suggest a white hole earlier on",
         "183": "Yes: never violated as a pair", "195": "The README is not a pair", "198": "My guess would be 1.",
         "168": "My sense: positions, one universe",
         "149": "I have given you everything I can. You have to work the math now"}
Z_SEATED = ('"Never violated" holds net along each light ray (183): a negative member paired along the same light rays '
            'is the appearance (117/120).')
Z_PULL = "the plane's apparent deficit is exactly the bulk's pull"            # WARPTHEOREM.md (Z), quoted in F9
T1 = {c: (1, c, 2, 1, 1, 1) for c in (0, 1)}                      # position 1's horizon ended, (Z) kept, no partner
T2 = {c: (2, c, 2, 1, 1, 1) for c in (0, 1)}                      # position 2's


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def owners():
    if not _CACHE:
        _CACHE["cy"] = _load(os.path.join(ROOT, "tools", "cypher.py"), "clc_cypher")
        _CACHE["cf"] = _load(os.path.join(HERE, "close_flux.py"), "clc_close_flux")
        _CACHE["ch"] = _load(os.path.join(HERE, "chain_cypher.py"), "clc_chain_cypher")
    return _CACHE


def _norm(path):
    with open(path, encoding="utf-8") as fh:
        return re.sub(r"\s+", " ", fh.read())


# ---------------------------------------------------------------------------------------------------------- F1-F3
def physics():
    cf = owners()["cf"]
    cf.MUT.clear()
    for k in ("exit_ignored", "ray_sign"):
        if MUT.get(k):
            cf.MUT[k] = True
    try:
        v = cf.vaidya()
        ray = {"positive": cf.raychaudhuri(0.5 if not cf.MUT.get("ray_sign") else -0.5),
               "zero": cf.raychaudhuri(0.0), "negative": cf.raychaudhuri(-0.5)}
        one, two = cf.event_horizon("one universe"), cf.event_horizon("between universes")
    finally:
        cf.MUT.clear()
    return {"vaidya": v, "ray": ray, "one": one, "two": two}


def _area(res):
    """close_flux.raychaudhuri's (theta_end, area ratio) -> 0 grows, 1 held, 2 shrinks"""
    a = res[1]
    return 1 if abs(a - 1) < 1e-9 else (2 if a < 1 else 0)


def z_kept(sign, paired):
    """(Z) as seated (187): net along each light ray; a negative member is the appearance only when paired."""
    if MUT.get("z_any"):
        return 1
    return 1 if (paired or sign >= 0) else 0


# ---------------------------------------------------------------------------------------------------------- cells
def cells(ph, variant="main"):
    rk, vd = ph["ray"], ph["vaidya"]
    s_in = -1 if vd["in_neg_when_losing"] else +1                   # the black-hole side's shrink flux (K1)
    s_out = +1 if vd["out_pos_when_losing"] else -1                 # the white-hole side's release flux (K1)
    out = {}
    # A1  close_flux.py K2 'positive' (area ratio < 1 from theta = 0) with K3 'one universe' (no event horizon): the
    #     one-universe positive closing of CLOSE-FLUX.md (cell "one universe, closing").  ends U: CLOSE-FLUX.md "What
    #     it does not show": "A closing that works. ... The closing's actual evolution in five dimensions is B4d's."
    out["A1 one universe, positive focusing (K2's surface)"] = (1, 0, _area(rk["positive"]), z_kept(+1, False), 1,
                                                               1 if MUT.get("seat_target") else U)
    if variant == "trapping":
        # A1t README-HELD.md 3 / readme_held.py C15: the trapping horizon r = 2M(v) holds f^2 N at a fraction f of E,
        #     rising under positive inflow; it depends on M(v) alone (OPENING.md O7, the apparent horizon r = 2m(v)), so
        #     it is the same in either class (deduced).  On H-SIZE-IS-TRAPPING-HORIZON this is position 1's horizon.
        del out["A1 one universe, positive focusing (K2's surface)"]
        out["A1t one universe, positive inflow on the trapping horizon"] = (1, 0, 0, z_kept(+1, False), 1, 0)
    # A2  close_flux.py CELLS "one universe, the hold" (Lemma S's fixed size, 163); area by K2 'zero'
    out["A2 one universe, the hold"] = (1, 0, _area(rk["zero"]), z_kept(0, False), 1, 0)
    # A3  close_flux.py K1 ingoing (T_vv < 0 when losing) and K3 'between universes'; CELLS "between universes,
    #     closing".  (Z): an unpaired negative member.  ends U: K1 computes the sign only; OPENING.md OPEN 2
    out["A3 between universes, negative influx"] = (1, 1, 2, z_kept(s_in, False), 1, U)
    # A4  close_flux.py CELLS "between universes, the hold"
    out["A4 between universes, the hold"] = (1, 1, _area(rk["zero"]), z_kept(0, False), 1, 0)
    # A5  README-HELD.md 2, "(b) fixed size, no partner": end area 4 N A_bit, theta > 0 throughout, measured on the
    #     event horizon (readme_held.py C7 'pre_no_partner'); K3: nothing leaves, so that horizon is universe 1's kind
    out["A5 between universes, positive flux onto the event horizon"] = (1, 1, 0, z_kept(+1, False), 1, 0)
    # P0  a 183 pair cancelling pointwise along the same rays: R(k,k) = 0 on the generators, close_flux.py K2 'zero'
    out["P0 one universe, pointwise pair (183)"] = (1, 0, _area(rk["zero"]), z_kept(-1, True), 0, 0)
    # P1  README-HELD.md 2, "(b) fixed size, exact partner": end area 1, theta = 0 (readme_held.py C7 'pre_partner')
    out["P1 between universes, pointwise pair (183)"] = (1, 1, 1, z_kept(-1, True), 0, 0)
    # W0  OPENING.md O1 (outgoing G_uu = -2 m'/r^2: every pointwise energy condition holds when m falls), O4 (position
    #     2's horizon ends at m -> 0, imposed), O7 (it shrinks as (1 - f)^2 N); close_flux.py K1 outgoing (T_uu > 0) and
    #     its CELLS "white hole releasing"
    pf_w = 0 if MUT.get("release_partner") else 1
    out["W0 one universe, the white hole releasing"] = (2, 0, 2, z_kept(s_out, False), pf_w, 1)
    # W1  the same computation names no class (H-RELEASE-ANY-CLASS, the board's); 132 and 136 (2) put the release at
    #     position 2 for every passage.  close_flux.py entered it in one class only (variant 'cf')
    if variant != "cf":
        out["W1 between universes, the white hole releasing"] = (2, 1, 2, z_kept(s_out, False), pf_w, 1)
    return out


# ---------------------------------------------------------------------------------------------------------- F7
def _orders(vals, unk_low):
    return [x for x in ([U, 0, 1, 2] if unk_low else [0, 1, 2, U]) if x in vals]


def ask(cs, side_order, class_order, unk_low):
    cy = owners()["cy"]
    cl = sorted(set(cs))
    vo = {"side": [s for s in side_order if s in {c[0] for c in cl}],
          "class": [k for k in class_order if k in {c[1] for c in cl}]}
    for i, name in enumerate(C[2:], 2):
        vo[name] = _orders({c[i] for c in cl}, unk_low)
    ix = cy.Index("close", C, [list(c) for c in cl], value_order=vo)
    targets = dict([("T1_%d" % k, t) for k, t in T1.items()] + [("T2_%d" % k, t) for k, t in T2.items()])
    res = {}
    for lang in LANGS:
        adm, _ = cy.ADMISSION[lang][0](ix, {})
        if adm is None:
            res[lang] = None
            continue
        dec = {tuple(ix.decode[i][c[i]] for i in range(len(C))) for c in adm}
        res[lang] = {name: t in dec for name, t in targets.items()}
        res[lang]["_n"] = len(adm) - len(ix.cells)
    return res


def codings():
    return [(so, ko, ul) for so in ((1, 2), (2, 1)) for ko in ((0, 1), (1, 0)) for ul in (False, True)]


def unseen_pairs(cs, target):
    out = []
    for i, j in itertools.combinations(range(len(C)), 2):
        if not any(c[i] == target[i] and c[j] == target[j] for c in cs):
            out.append(((C[i], target[i]), (C[j], target[j])))
    return out


def run_all(cs):
    return {cd: ask(list(cs), *cd) for cd in codings()}


def cypher(ph):
    main = cells(ph)
    ctrl = dict(main)
    key = "A1 one universe, positive focusing (K2's surface)"
    if not MUT.get("ctrl_noop"):
        ctrl[key] = main[key][:5] + (1,)                            # the decisive cell: B4d's closing ends the horizon
    ctrl_cf = {k: v for k, v in ctrl.items() if not k.startswith("W1")}
    # probes, not readings: each unknown side-1 ending set to 0 ('does not end') to find which unknown carries the
    # side-1-first admissions of order, algebra and geometry (F7, Q11)
    a3 = "A3 between universes, negative influx"
    ends0 = lambda cs, ks: {k: (v[:5] + (0,) if k in ks else v) for k, v in cs.items()}
    no_both = ends0(main, {key} if MUT.get("unk_partial") else {key, a3})
    trap = cells(ph, "trapping")
    cy = owners()["cy"]
    cl = sorted(set(main.values()))
    ix = cy.Index("close", C, [list(c) for c in cl], value_order={
        "side": [1, 2], "class": [0, 1], "area": _orders({c[2] for c in cl}, False),
        "z_kept": _orders({c[3] for c in cl}, False), "partner_free": _orders({c[4] for c in cl}, False),
        "ends_horizon": _orders({c[5] for c in cl}, False)})
    adm, _ = cy.ADMISSION["statistics"][0](ix, {})
    extra = sorted(tuple(ix.decode[i][c[i]] for i in range(len(C))) for c in adm if c not in set(ix.cells))
    return {"stat_extra": extra, "cells": main, "main": run_all(main.values()), "ctrl": run_all(ctrl.values()),
            "ctrl_cf": run_all(ctrl_cf.values()), "trap": run_all(trap.values()), "trap_cells": trap,
            "unseen": {k: unseen_pairs(list(main.values()), t) for k, t in T1.items()},
            "ctrl_cells": ctrl, "no_a1": run_all(ends0(main, {key}).values()),
            "no_a3": run_all(ends0(main, {a3}).values()), "no_both": run_all(no_both.values()),
            "no_both_cells": no_both}


# ---------------------------------------------------------------------------------------------------------- run
def compute():
    o = owners()
    ph = physics()
    return {"question": o["ch"].INPUTS.get("CLOSE"), "ph": ph, "cy": cypher(ph),
            "rulings": _norm(os.path.join(D68, "M-RULINGS-2026-10-03.md")),
            "warp": _norm(os.path.join(D68, "WARPTHEOREM.md"))}


def _all(runs, lang, tgt, val):
    return all(r[lang] is not None and r[lang][tgt] is val for r in runs.values())


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Q1 the question is chain_cypher.py's input CLOSE verbatim; M's words (109, 115 (a), 106 (b), 136 (2), 132, "
        "199, 183, 195, 198, 168, 149) occur verbatim in the rulings file; (Z)'s seated wording and F9's quote occur in "
        "WARPTHEOREM.md", d["question"] == QUESTION and all(q in d["rulings"] for q in WORDS.values())
        and Z_SEATED in d["warp"] and Z_PULL in d["warp"])
    ph = d["ph"]
    add("Q2 F1 (close_flux K1): ingoing Vaidya losing mass has T_vv < 0, outgoing has T_uu > 0 -- so the black-hole "
        "side's unpaired shrink breaks (Z) net per ray (A3) and the white-hole release keeps it (W0, W1)",
        ph["vaidya"]["in_neg_when_losing"] and ph["vaidya"]["out_pos_when_losing"]
        and d["cy"]["cells"]["A3 between universes, negative influx"][3] == 0
        and d["cy"]["cells"]["W0 one universe, the white hole releasing"][3] == 1)
    rk = ph["ray"]
    add("Q3 F2 (close_flux K2): from theta = 0 positive R(k,k) shrinks the surface (A1's area 2), zero keeps it to "
        "1e-12 (the holds and the pointwise pairs), negative grows it", _area(rk["positive"]) == 2
        and abs(rk["zero"][1] - 1) < 1e-12 and _area(rk["negative"]) == 0)
    cs = d["cy"]["cells"]
    add("Q4 F3-F4 (close_flux K3): one universe no event horizon, no negative demand; between universes an event "
        "horizon and the demand stands; and no between-universes cell of position 1 shrinks with (Z) kept and no partner",
        not ph["one"]["event_horizon"] and not ph["one"]["needs_negative"] and ph["two"]["event_horizon"]
        and ph["two"]["needs_negative"]
        and not any(c[0] == 1 and c[1] == 1 and c[2] == 2 and c[3] == 1 and c[4] == 1 for c in cs.values()))
    s1 = [c for c in cs.values() if c[0] == 1]
    add("Q5 F6 the record: no cell ends position 1's horizon (every side-1 ends value 0 or U; the U's are A1, B4d's, "
        "and A3); both white-hole cells end position 2's (imposed, O4)", all(c[5] in (0, U) for c in s1)
        and sorted(k[:2] for k, c in cs.items() if c[0] == 1 and c[5] == U) == ["A1", "A3"]
        and all(c[5] == 1 for c in cs.values() if c[0] == 2) and len([c for c in cs.values() if c[0] == 2]) == 2)
    m = d["cy"]["main"]
    one_pair = [((("side", 1), ("ends_horizon", 1)),)]
    add("Q6 F7 statistics refuses T1 in both classes under all 8 codings; the only unseen pair of each is "
        "(side 1, ends 1); its one admitted cell beyond the data is (1, between, shrinks, (Z), no partner, U) -- the "
        "cell F3-F4 exclude, which order-2 support cannot see", _all(m, "statistics", "T1_0", False)
        and _all(m, "statistics", "T1_1", False) and [tuple(d["cy"]["unseen"][k]) for k in (0, 1)] == one_pair * 2
        and d["cy"]["stat_extra"] == [(1, 1, 2, 1, 1, U)])
    cnt = {l: [sum(r[l][t] for r in m.values()) for t in ("T1_0", "T1_1")] for l in ("order", "algebra", "geometry",
                                                                                   "information")}
    low = [cd for cd in m if cd[0] == (1, 2) and cd[2]]
    add("Q7 F7 order, algebra, geometry and information admit T1 under some codings and refuse it under others -- 6, "
        "6, 4 and 4 of 8, the same in both classes; all four refuse with side 1 ordered first and U below 0: the verdict "
        "moves with the coding (an artefact of ordering a nominal axis and of where the unknowns sit), not a reading",
        cnt == {"order": [6, 6], "algebra": [6, 6], "geometry": [4, 4], "information": [4, 4]}
        and all(not m[cd][l][t] for cd in low for l in cnt for t in ("T1_0", "T1_1")))
    add("Q8 contrast: T2 (position 2's horizon ended by the positive release) admitted by all five under every coding "
        "(forced: data)", all(_all(m, l, t, True) for l in LANGS for t in ("T2_0", "T2_1")))
    c, cc = d["cy"]["ctrl"], d["cy"]["ctrl_cf"]
    add("Q9 CONTROL: A1's unknown ending set to 1 -> T1 (one universe) admitted by all five under every coding; "
        "statistics then also admits T1 between universes (over-reach against F3-F4: a four-way constraint), as do "
        "order, algebra, geometry (8 of 8) and information (6 of 8); statistics refuses it once the release is confined "
        "to one universe (close_flux's coding) -- an encoding artefact",
        all(_all(c, l, "T1_0", True) for l in LANGS) and _all(c, "statistics", "T1_1", True)
        and [sum(r[l]["T1_1"] for r in c.values()) for l in ("order", "algebra", "geometry", "information")]
        == [8, 8, 8, 6] and _all(cc, "statistics", "T1_1", False))
    t = d["cy"]["trap"]
    tc = d["cy"]["trap_cells"]
    add("Q10 F8 variant 'trapping' (H-SIZE-IS-TRAPPING-HORIZON): statistics refuses T1 in both classes under every "
        "coding, no side-1 cell with (Z) kept and no partner keeps an unknown, and the other four admit T1 under 6, 6, "
        "4 and 4 codings as in the main run", _all(t, "statistics", "T1_0", False)
        and _all(t, "statistics", "T1_1", False)
        and not any(c[0] == 1 and c[3] == 1 and c[4] == 1 and U in c for c in tc.values())
        and {l: [sum(r[l][x] for r in t.values()) for x in ("T1_0", "T1_1")] for l in cnt} == cnt)
    t1s = ("T1_0", "T1_1")
    verdicts = lambda runs: {cd: {l: tuple(bool(r[l][x]) for x in t1s) for l in cnt} for cd, r in runs.items()}
    hi1 = [cd for cd in m if cd[0] == (1, 2) and not cd[2]]
    nb = d["cy"]["no_both"]
    add("Q11 F7 which unknown carries the over-reach: with side 1 ordered first and U above 1, order, algebra and "
        "geometry admit T1 and information does not, and geometry admits only with U above 1; A1's ending set to 0 "
        "alone, or A3's alone, leaves every T1 verdict of the four unchanged under all 8 codings (either unknown "
        "suffices); both set to 0 leaves no side-1 unknown and order, algebra and information admitting only with "
        "side 2 ordered first (4 of 8, under either placing of U), geometry nowhere; the 'trapping' variant's one "
        "side-1 unknown is A3's", all(m[cd][l][x] is (l != "information") for cd in hi1 for l in cnt for x in t1s)
        and all(m[cd]["geometry"][x] is (not cd[2]) for cd in m for x in t1s)
        and verdicts(d["cy"]["no_a1"]) == verdicts(m) and verdicts(d["cy"]["no_a3"]) == verdicts(m)
        and not any(c[0] == 1 and c[5] == U for c in d["cy"]["no_both_cells"].values())
        and {l: [sum(r[l][x] for r in nb.values()) for x in t1s] for l in cnt}
        == {"order": [4, 4], "algebra": [4, 4], "geometry": [0, 0], "information": [4, 4]}
        and all(nb[cd][l][x] is (cd[0] == (2, 1)) for cd in nb for l in ("order", "algebra", "information")
                for x in t1s)
        and sorted(k[:2] for k, c in tc.items() if c[0] == 1 and c[5] == U) == ["A3"])
    return res


MUTANTS = {"seat_target": "position 1's horizon's ending seated as data (A1 ends = 1)",
           "z_any": "(Z) read as kept whatever the unpaired sign",
           "exit_ignored": "close_flux K3: position 2's exit not counted in the same universe",
           "ray_sign": "close_flux K2: positive energy read as defocusing",
           "release_partner": "the white-hole release given a partner",
           "ctrl_noop": "the control leaves the decisive cell unchanged",
           "unk_partial": "the both-unknowns probe clears A1's ending only (A3's U left)"}


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
        print("  mutant %-15s %-58s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("close_cypher.py -- CLOSE put to the cypher\n")
    print("question:", d["question"])
    for k, v in d["cy"]["cells"].items():
        print("  cell %-60s %s" % (k, v))
    for part in ("main", "ctrl", "ctrl_cf", "trap", "no_a1", "no_a3", "no_both"):
        runs = d["cy"][part]
        print("\n%s:" % part)
        for lang in LANGS:
            row = {t: sum(bool(r[lang] and r[lang][t]) for r in runs.values()) for t in ("T1_0", "T1_1", "T2_0", "T2_1")}
            ns = sorted({r[lang]["_n"] for r in runs.values() if r[lang] is not None})
            print("  %-12s admitted in (of %d codings) %s  E over codings %s" % (lang, len(runs), row, ns))
    print("\nunseen pairs of T1:", d["cy"]["unseen"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
