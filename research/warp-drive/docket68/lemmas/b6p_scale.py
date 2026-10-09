#!/usr/bin/env python3
"""b6p_scale.py -- Warp Theorem lemma B6'' (a proposed edit of B6', k's scale): k's scale tied to our G and our plane's
tension through one bulk law (M-RULINGS items 191, 192).  Computed, READ and deduced; not verified; not seated;
2026-10-09.  Note: lemmas/B6P-SCALE.md.

B6'' AS BUILT HERE.  k's scale is fixed by our G and our plane's tension sigma:
      ell^2 = 3 c^4 / (4 pi G sigma)                     (the Randall-Sundrum tuning; MK eq. (25))
      ell^2 = 3 / (4 pi G sigma / c^4 - Lambda_4)        (exact, SMS eqs. (18)-(19), any Lambda_4)
  (one bulk law, 191; one axis, 192); sigma by measurement (136 (8)).
STATUS EARNED (section S6): the relation DERIVED; sigma's value NATURE.  B6'' as a whole is NATURE (its weakest
conjunct) -- not GREEN in the strict sense (GREEN = PROVED, DERIVED or AXIOM with no non-green input), and not OPEN,
so the theorem's own condition ("proved exactly when no lemma is OPEN") is met by B6'' exactly as it was by B6'.
Stated plainly (135): the cypher supplies k's tie, not k's value; the value stays measurement's, by M's 136 (8).

CLI:  --selftest (every check, each able to fail; ~80 s, most of it exactE.py's coefficient table)
      --mutants  (every named mutation of every check, each shown to make its check FAIL; exit 1 if any passes)
      --json PATH (writes compute(), every row labelled)

LABELS.  Every result carries one of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  M's words are quoted verbatim, typing kept, from M-RULINGS-2026-10-03.md; the board's
readings are named H-... and kept apart from them.

M'S WORDS USED (verbatim, typing kept):
  57       "If two points, each on a different spacetime plane, are connected by a corridor through a higher dimension,
           then speed cannot exist in the dimension below the corridor as you are at position 1 then position 2, with
           no in between, which means no travel, no speed"
  129 (1)  "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because the
           corridor is a bridge, so it adds nothing to either position."
  136 (8)  "8 - leave it to measurement. But we can accurately hypothesize it first. Measurement would confirm."
  139 (4)  "4 - why are you still chasing distance/speed? This was ruled out"
  140      "If k helps define the bulk, the math in our work should give you pieces to both derive and prove k. Our math
           is not dependent on k, k is dependent on our work."
  141      "If planes are constantly in motion around each other, a stable throat cannot form. I suggest the planes are
           static, but their surfaces contain their own movements from within their own contained dimensions"
  184      "There are no matter free planes"
  187 (2)  M chose "For the math" (whether each universe, and a corridor's region, has its own Newton's constant)
  191      "Based on the results of gravity, let's assume the same interaction for k"
  192      "this appears to be a question to put to the math language hierarchy cypher"

THE BOARD'S READINGS (named; withdrawn if M says otherwise):
  H-CYPHER-COUPLING-INDEX  how 192's question is encoded as indices for tools/cypher.py (section S1): cells are
           planes (or bulk states) under one five-dimensional coupling, coordinates the curvatures on a plane's two
           sides, its tension and its G; for the G5 question, exponent coordinates (N, G, sigma, l_P, G5).  The
           encoding is the board's; the roster stays data (every roster in cypher.py is run, none chosen).
  H-ONE-K-LAW  the board's reading of 191, as worded in 191's record: one five-dimensional curvature law; each
           universe's k follows from its own plane; no k of its own for a corridor's region (H-K-PER-CORRIDOR, 186,
           set aside as the working assumption).  B6'' does NOT need it to derive the relation; it needs it only for
           B6'' to be the whole of "k's scale" (no third, corridor curvature left to fix).
  H-ONE-G5  the board's provisional 187 (2) decision (ITEM186 sec. 6): one 5D coupling for the bulk.
  H-ZERO-MODE-NORM  the board's model choice for a two-sided plane's G: the zero mode normalised over two infinite
           AdS sides (the Z2 limit checked against MK eq. (27), READ).
  H-MEASURED-G-IS-LOCAL  our measured G is SMS's local G_N on our plane.  Deduced to < 1e-4 within the Lykken-Randall
           family (multiplane.py's model) from Cassini's gamma; the board's in general (S5).

WHAT IS COMPUTED HERE
  S1 THE CYPHER (computed; H-CYPHER-COUPLING-INDEX).  tools/cypher.py imported by path, every roster run:
     Z2 planes: every operator-bearing language E = 0, all agree, information flags k_a, k_b, sigma, G each a KEY,
     not an axis (register 1356): one axis.  Two-sided planes: G adds nothing beyond (k_a, k_b) (information; logic's
     binary), the nonlinear law gives E > 0.  Control, a second coupling: information's binary on G flips.  G5: fixed
     by (G, sigma), by no subset of {N, G, l_P}; control G5 = G N flips it.  The radion: with the planes' separation
     free, G is a second axis; fixed (127/141, or our current state), one axis again.
  S2 THE RELATION (computed, sympy; READ SMS eqs. (18), (19), p.3; MK eqs. (19), (25), (27), pp.8-9).  Lambda_4 =
     4 pi G sigma - 3/ell^2 exactly; at Lambda_4 = 0 it is MK eq. (25); SMS's k = kappa5^2 lambda/6 = 1/ell; G5 = G ell
     and G5^2 = 3G/(4 pi sigma).  Two-sided: sigma G = 3 k_a k_b/(4 pi), ell_a ell_b = 3/(4 pi G sigma).  Controls
     that fail: a wrong tuning coefficient misses MK (25); SMS's own scaling (p.4) keeps G and moves ell, so G alone
     fixes nothing; lambda < 0 gives G < 0 (SMS p.3).
  S3 LAMBDA_4 (computed; READ SMS p.3-4, MK p.9).  Lambda_4 = (kappa5^4/12)(sigma^2 - sigma_RS^2) = (4 pi G/c^4)(sigma
     - 3c^4/(4 pi G ell^2)): it fixes only the departure sigma - sigma_RS, never sigma -- one equation in (sigma, ell).
  S4 THE WINDOW (computed; READ Adelberger et al. p.3, MK pp.10-11).  ell <= 13.964 um gives sigma >= 1.48e53 J/m^3
     (sigma^(1/4) >= 9.2 TeV); the lower edges in m(N) cap sigma at 3c^4/(4 pi G c_e^2 m1^2 N), and under one k they
     cap the README at N <= (ell/(c_e m1))^2; the classical floor ell > l_P (= ell > l5 under one coupling) is N-free.
  S5 WHICH G, WHICH k (computed from bulk/multiplane.py, imported; READ Will 1403.7377v1 p.43).
  S6 STATUS (STRUCTURAL): what B6'' earns, on what, and whether it counts green.

Imports by path (never copied): tools/cypher.py; copy/exactE.py (E per sqrt bit, constants, the example README);
lemmas/sim2_facing.py (ell_w_class, the down-the-throat edge) and its bank lemmas/sim2_bank.json (ell_W, read as
data); bulk/multiplane.py (lr(), the Lykken-Randall two-plane law, PRZ); ../cosmo.py (H0, Omega_m).
Stdlib + sympy.  python3 b6p_scale.py [--selftest] [--mutants] [--json PATH]
"""
import argparse
import contextlib
import importlib.util
import io
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
REPO = os.path.dirname(os.path.dirname(WD))
CYPHER_PATH = os.path.join(REPO, "tools", "cypher.py")

# ------------------------------------------------------------------------------------------------ READ at source
# Verbatim from each PDF's text layer (math linearised as the text layer gives it); page = PDF page.
READS = {
    "SMS_13_14": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "T_mu nu = -Lambda g_mu nu + S_mu nu delta(chi), (13) where S_mu nu = -lambda q_mu nu + tau_mu nu, (14) "
                  "... Lambda is the cosmological constant of the bulk spacetime. lambda and tau_mu nu are the vacuum "
                  "energy and the energy-momentum tensor, respectively, in the brane world. Note that lambda is the "
                  "tension of the brane in 5 dimensions."),
    "SMS_18_19": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "Lambda_4 = 1/2 kappa_5^2 (Lambda + 1/6 kappa_5^2 lambda^2), (18)  G_N = kappa_5^4 lambda / 48 pi, (19)"),
    "SMS_sign": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                 "Furthermore, we would have the wrong sign of G_N if lambda < 0"),
    "SMS_split": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "It should be noted that the decomposition of S_mu nu into lambda q_mu nu and tau_mu nu can be "
                  "ambiguous, particularly in cosmological contexts."),
    "SMS_Z2": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
               "Now we impose the Z2-symmetry on this spacetime, with the brane as the fixed point."),
    "SMS_k": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 4,
              "where r is the distance between the two bodies and k = kappa_5^2 lambda/6."),
    "SMS_scaling": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 4,
                    "We set kappa_5^-2 = M_G^3 and lambda = M_lambda^4 ... One can scale them as M_G -> f^2 M_G and "
                    "M_lambda -> f^3 M_lambda, where f is an arbitrary constant, while keeping the gravitational "
                    "constant G_N unchaged."),
    "SMS_L4_free": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 4,
                    "It is assumed that Lambda < 0. Hence Lambda_4 may take arbitrary value as one may wish by "
                    "appropriately specifying the values of Lambda and lambda."),
    "MK_3": ("Maartens, Koyama, 1004.3962v2", 3,
             "kappa^2_{4+d} = 8 pi G_{4+d} = 8 pi / M^{2+d}_{4+d}, (3)"),
    "MK_19_22": ("Maartens, Koyama, 1004.3962v2", 8,
                 "Lambda_5 = -6/ell^2 = -6 mu^2, (19) where ell is the curvature radius of AdS5 ... "
                 "(5)G_AB = -Lambda_5 (5)g_AB, (22)"),
    "MK_25": ("Maartens, Koyama, 1004.3962v2", 8,
              "The branes have equal and opposite tensions +-lambda, where lambda = 3 M_p^2 / (4 pi ell^2). (25)"),
    "MK_27": ("Maartens, Koyama, 1004.3962v2", 9,
              "Then the energy scales are related via M_5^3 = M_p^2 / ell. (27)"),
    "MK_tuning": ("Maartens, Koyama, 1004.3962v2", 9,
                  "The fine-tuning in Equation (25) ensures that there is a zero effective cosmological constant on "
                  "the brane, so that the brane has the induced geometry of Minkowski spacetime."),
    "MK_41": ("Maartens, Koyama, 1004.3962v2", 10, "For r >> ell, V(r) ~ GM/r (1 + 2 ell^2/(3 r^2)), (41)"),
    "MK_42": ("Maartens, Koyama, 1004.3962v2", 11,
              "Table-top tests of Newton's laws currently find no deviations down to O(10^-1 mm), so that ell <~ 0.1 "
              "mm in Equation (41). Then by Equations (25) and (27), this leads to lower limits on the brane tension "
              "and the fundamental scale of the RS 1-brane model: lambda > (1 TeV)^4, M5 > 10^5 TeV. (42) These "
              "limits do not apply to the 2-brane case."),
    "ADEL_18": ("Adelberger et al., hep-ph/0611223v3", 3,
                "V^k_ab(r) = -G M_a M_b / r beta_k (1 mm / r)^(k-1) (18)"),
    "ADEL_T1": ("Adelberger et al., hep-ph/0611223v3", 3,
                "TABLE I: 68% confidence laboratory constraints on power-law potentials from this work and "
                "previous[14, 15] results. ... k = 3: |beta_k| (this work) 1.3 x 10^-4"),
    "GRS": ("Gregory, Rubakov, Sibiryakov, hep-th/0002072v2", 3,
            "The constant k is related to sigma and Lambda as follows: sigma = 3k/(4 pi G5), Lambda = -sigma k, where "
            "G5 is the five-dimensional Newton constant."),
    "WILL_CASSINI": ("Will, 1403.7377v1", 43,
                     "A significant improvement was reported in 2003 from Doppler tracking of the Cassini spacecraft "
                     "while it was on its way to Saturn [38], with a result gamma - 1 = (2.1 +- 2.3) x 10^-5."),
}
BETA3_MAX = 1.3e-4             # READ ADEL_T1 (68%, k = 3)
GAMMA_M1, GAMMA_SIG = 2.1e-5, 2.3e-5    # READ WILL_CASSINI
MK42_ELL_M, MK42_TEV4 = 1e-4, 1.0       # READ MK_42: ell <~ 0.1 mm -> lambda > (1 TeV)^4
EV_J = 1.602176634e-19         # SI 2019 exact (definition)

# ------------------------------------------------------------------------------------------------ owners
_CACHE = {}


def _load(path, key, register=False):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        if register:                       # cypher.py's @dataclass resolves through sys.modules (cf. necindex.py)
            sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def cypher():
    if "cypher" not in _CACHE:
        _CACHE["cypher"] = _load(CYPHER_PATH, "b6pp_cypher", register=True)
    return _CACHE["cypher"]


def base():
    """Owner values, computed once: E per sqrt bit and constants (exactE.py), the SIM2 edges (sim2_facing.py and its
    bank), the Lykken-Randall law (multiplane.py), H0 and Omega_m (cosmo.py)."""
    if "base" in _CACHE:
        return _CACHE["base"]
    t0 = time.perf_counter()
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "b6pp_exactE")
    E1 = ex.e_per_sqrt_bit()
    G, c, h = float(ex.G_SI), float(ex.C_SI), float(ex.H_SI)
    sf = _load(os.path.join(HERE, "sim2_facing.py"), "b6pp_sim2_facing")
    with contextlib.redirect_stdout(io.StringIO()):
        wc = sf.ell_w_class()
    bank = json.load(open(os.path.join(HERE, "sim2_bank.json")))
    mpl = _load(os.path.join(D68, "bulk", "multiplane.py"), "b6pp_multiplane")
    cosmo = _load(os.path.join(WD, "cosmo.py"), "b6pp_cosmo")
    _CACHE["base"] = {
        "E1_J": E1, "G": G, "c": c, "h": h, "hbar": h / (2 * math.pi), "m1_m": G * E1 / c**4,
        "N_example": ex.N_EXAMPLE, "ell_class": wc["ell"], "ell_W": bank["throat"]["ell_W"],
        "mpl": mpl, "H0": cosmo.H0(), "Omega_m": cosmo.OMEGA_M, "load_s": time.perf_counter() - t0}
    return _CACHE["base"]


# ------------------------------------------------------------------------------------------------ S1 the cypher
K = (1, 2, 3, 4)
OPTS = {"statistics_order": 2, "algebra_budget": 20000}


def determined(cells, coords, by, target):
    """Logic's binary: does the tuple of coordinates `by` fix `target` on these cells?"""
    seen = {}
    ti = coords.index(target)
    for cl in cells:
        key = tuple(cl[coords.index(b)] for b in by)
        seen.setdefault(key, set()).add(cl[ti])
    return all(len(v) == 1 for v in seen.values())


def law_two_sided(ka, kb, lam=1):
    """One kappa5 (units kappa5^2 = 8 pi, G5 = 1): sigma = 3(ka + kb)/(8 pi) -> ordinal ka + kb; G = 2 ka kb/(ka + kb)
    (two-sided zero mode, H-ZERO-MODE-NORM; Z2: G = G5 k).  lam multiplies G: a second coupling (the control)."""
    return [ka, kb, Fr(ka + kb), Fr(2 * ka * kb, ka + kb) * lam]


def idx_spec(name, mut=None):
    """The board's indices (H-CYPHER-COUPLING-INDEX).  Returns (name, coords, cells, declared)."""
    co4 = ["k_a", "k_b", "sigma", "G"]
    if name == "z2":
        cells = [law_two_sided(k, k) for k in K]
        if mut == "anti_monotone":                       # swap G at k = 2, 3 (a law that is not one chain)
            cells[1][3], cells[2][3] = cells[2][3], cells[1][3]
        if mut == "second_coupling":
            cells += [law_two_sided(k, k, 2) for k in K]
        res = [cl[3] - Fr(2 * cl[0] * cl[1], cl[0] + cl[1]) for cl in cells]
        wit = ("continuous closed-form law sigma = (3/kappa5^2)(k_a + k_b), G = (kappa5^2/8 pi) 2 k_a k_b/(k_a + k_b); "
               "residual 0 on %d/%d cells (computed)" % (sum(r == 0 for r in res), len(cells)))
        return "Z2 planes under one kappa5", co4, cells, {"analysis": {"speaks": True, "witness": wit}}
    if name == "two_sided":
        lams = (1, 2) if mut == "second_coupling" else (1,)
        if mut == "z2_only":
            cells = [law_two_sided(k, k) for k in K]
        else:
            cells = [law_two_sided(a, b, l) for a, b in itertools.product(K, K) for l in lams]
        wit = "the same closed-form law as Z2, both sides free (computed residual 0)"
        return "two-sided planes under one kappa5", co4, cells, {"analysis": {"speaks": True, "witness": wit}}
    if name == "control":
        lams = (1,) if mut == "lam_one" else (1, 2)
        cells = [law_two_sided(a, b, l) for a, b in itertools.product(K, K) for l in lams]
        wit = "a law in (k_a, k_b, lambda), lambda a second coupling on no coordinate: two G per (k_a, k_b) (computed)"
        return "CONTROL: G with a coupling of its own", co4, cells, {"analysis": {"speaks": True, "witness": wit}}
    co5 = ["N", "G", "sigma", "l_P", "G5"]
    grid = list(itertools.product((0, 1, 2), repeat=3))
    if name == "g5":
        # exponent coordinates (log base b, doubled): G5^2 = 3G/(4 pi sigma) -> g5 = g - s (+ const); l_P^2 = hbar G/c^3
        rule = {"tied_to_N": lambda n, g, s: g + n, "G_only": lambda n, g, s: g}.get(mut, lambda n, g, s: g - s)
        cells = [[n, g, s, g, rule(n, g, s)] for n, g, s in grid]
        wit = "G5^2 = 3G/(4 pi sigma) (S2, from SMS (18)-(19) and MK (27)); residual 0 in exponent form (computed)"
        return "G5 under one bulk law", co5, cells, {"analysis": {"speaks": True, "witness": wit}}
    if name == "g5_control":
        rule = (lambda n, g, s: g - s) if mut == "law_cells" else (lambda n, g, s: g + n)
        cells = [[n, g, s, g, rule(n, g, s)] for n, g, s in grid]
        wit = "control law G5 = G N (a bulk constant tied to the README)"
        return "CONTROL: G5 tied to the README", co5, cells, {"analysis": {"speaks": True, "witness": wit}}
    if name == "radion":
        ratio0 = which_g()["ratio_r0"] if mut != "no_radion" else Fr(1)
        coR = ["k_L", "sep", "sigma1", "G"]
        # sep 0: coincident (127's coinciding, M4); sep 1: far (X -> 0).  sigma1 = 24 M^3 k_L -> ordinal k_L;
        # G_loc proportional to k_L (SMS (19) at the tuning); the measured G = G_loc x ratio(sep) (S5)
        cells = [[k, s, Fr(k), Fr(k) * (ratio0 if s == 0 else 1)] for k in K for s in (0, 1)]
        wit = "G = G_loc(k_L) (3 - X)/(3 (1 + X)), X = e^(-2 k_L r)/3 at B6's ratio: a law in (k_L, r) (S5, computed)"
        return "the radion: two planes, separation free", coR, cells, {"analysis": {"speaks": True, "witness": wit}}
    raise KeyError(name)


def run_index(name, mut=None, rosters=None):
    cy = cypher()
    title, coords, cells, declared = idx_spec(name, mut)
    vo = {c: sorted({cl[i] for cl in cells}, key=float) for i, c in enumerate(coords)}
    out = {"index": title, "coords": coords, "cells": len(cells), "rosters": {}}
    rows = keys = None
    for rn in (rosters or sorted(cy.ROSTERS)):
        ix = cy.Index(title, coords, cells, vo, declared)
        res = cy.run(ix, rn, OPTS)
        rows, keys = cy.coordinate_report(ix)
        out["rosters"][rn] = {
            "verdicts": [{"language": v.language, "state": v.state, "status": v.status, "admitted": v.admitted,
                          "E": v.E} for v in res["_verdicts"]],
            "agree": res["languages_agree"], "all_E_zero": res["all_E_zero"], "langclose": res["langclose_holds"],
            "degenerate": res["degenerate"], "bearing": res["operator_bearing_measured"]}
    out["adds_nothing"] = [r["coordinate"] for r in rows if r["adds_nothing"]]
    out["keys"] = keys
    out["_cells"] = cells
    return out


def _measured(r, rn="1173"):
    return [v for v in r["rosters"][rn]["verdicts"] if v["E"] is not None]


def check_C1(mut=None):
    """Z2: one axis -- every measured language E = 0 and agreeing, K.langclose holds, every coordinate a KEY."""
    r = run_index("z2", mut, rosters=["1173"])
    m = _measured(r)
    ok = (len(m) >= 4 and all(v["E"] == 0 for v in m) and r["rosters"]["1173"]["agree"] is True
          and r["rosters"]["1173"]["langclose"] is True and not r["rosters"]["1173"]["degenerate"]
          and sorted(r["keys"]) == sorted(r["coords"]))
    return ok, {"E": {v["language"]: v["E"] for v in m}, "keys": r["keys"], "agree": r["rosters"]["1173"]["agree"]}


def check_C2(mut=None):
    """Two-sided: G fixed by (k_a, k_b) (logic) and adds nothing (information); the nonlinear law gives E > 0."""
    r = run_index("two_sided", mut, rosters=["1173"])
    det = determined(r["_cells"], r["coords"], ["k_a", "k_b"], "G")
    m = _measured(r)
    ok = det and "G" in r["adds_nothing"] and any(v["E"] > 0 for v in m)
    return ok, {"G_by_ka_kb": det, "adds_nothing": r["adds_nothing"], "E": {v["language"]: v["E"] for v in m}}


def check_C3(mut=None):
    """Control: a second coupling flips information's binary on G (and logic's)."""
    r = run_index("control", mut, rosters=["1173"])
    det = determined(r["_cells"], r["coords"], ["k_a", "k_b"], "G")
    ok = (not det) and "G" not in r["adds_nothing"]
    return ok, {"G_by_ka_kb": det, "adds_nothing": r["adds_nothing"]}


G5_SETS = (["N"], ["G"], ["l_P"], ["G", "N"], ["G", "l_P", "N"], ["sigma"], ["G", "sigma"])


def check_C4(mut=None):
    """G5 fixed by (G, sigma), by no subset of {N, G, l_P}; information: sigma recoverable, N not."""
    r = run_index("g5", mut, rosters=["1173"])
    b = {"+".join(s): determined(r["_cells"], r["coords"], s, "G5") for s in G5_SETS}
    ok = (b["G+sigma"] and not any(b[k] for k in ("N", "G", "l_P", "G+N", "G+l_P+N", "sigma"))
          and "sigma" in r["adds_nothing"] and "N" not in r["adds_nothing"])
    return ok, {"binaries": b, "adds_nothing": r["adds_nothing"]}


def check_C5(mut=None):
    """Control G5 = G N: the binaries flip -- fixed by (G, N), not by (G, sigma); N recoverable, sigma not."""
    r = run_index("g5_control", mut, rosters=["1173"])
    b = {"+".join(s): determined(r["_cells"], r["coords"], s, "G5") for s in G5_SETS}
    ok = b["G+N"] and not b["G+sigma"] and "N" in r["adds_nothing"] and "sigma" not in r["adds_nothing"]
    return ok, {"binaries": b, "adds_nothing": r["adds_nothing"]}


def check_C6(mut=None):
    """The radion: with the separation free, G is not fixed by (k_L, sigma1) -- a second axis; at a fixed separation
    (either) it is."""
    r = run_index("radion", mut, rosters=["1173"])
    free = determined(r["_cells"], r["coords"], ["k_L", "sigma1"], "G")
    fixed = all(determined([c for c in r["_cells"] if c[1] == s], r["coords"], ["k_L", "sigma1"], "G") for s in (0, 1))
    ok = (not free) and fixed
    return ok, {"G_by_kL_sigma1_sep_free": free, "G_by_kL_sigma1_sep_fixed": fixed}


def check_C7(mut=None):
    """Every roster is run (dockets 20x-04/20x-09 open); a language the build does not implement stays NOT-RUN, never
    SILENT (register 1172); on Z2 planes every measured language of every roster has E = 0."""
    cy = cypher()
    rosters = ["1173"] if mut == "one_roster" else sorted(cy.ROSTERS)
    r = run_index("z2", None, rosters=rosters)
    states = {rn: {v["language"]: v["state"] for v in d["verdicts"]} for rn, d in r["rosters"].items()}
    if mut == "notrun_as_silent":
        states = {rn: {l: ("SILENT" if s == "NOT-RUN" else s) for l, s in d.items()} for rn, d in states.items()}
    every = set(r["rosters"]) == set(cy.ROSTERS)
    notrun_kept = (all(states["20.2"][l] == "NOT-RUN" for l in ("arithmetic", "calculus", "logic", "constraint-language"))
                   if "20.2" in states else False)
    e0 = all(v["E"] == 0 for d in r["rosters"].values() for v in d["verdicts"] if v["E"] is not None)
    ok = every and notrun_kept and e0
    return ok, {"rosters": sorted(r["rosters"]), "states_20.2": states.get("20.2"), "E0_every_roster": e0}


# ------------------------------------------------------------------------------------------------ S2 the relation
def derive(mut=None):
    """SMS eqs. (18)-(19) with MK eq. (19) (Lambda_5 = -6/ell^2) and the map kappa5^2 Lambda_SMS = Lambda_5 (deduced: SMS
    (6) with (13) gives (5)G = -kappa5^2 Lambda g in the bulk; MK (22) writes (5)G = -Lambda_5 g).  Natural units
    (c = 1 here; SI in S4)."""
    k5, lam, ell, G, f = sp.symbols("kappa5 lambda ell G f", positive=True)
    L4 = sp.Symbol("Lambda4", real=True)
    Lam5 = (6 if mut == "sign_Lambda5" else -6) / ell**2
    Lsms = Lam5 / k5**2
    coef = sp.Rational(1, 3) if mut == "lambda2_coef" else sp.Rational(1, 6)
    L4expr = sp.Rational(1, 2) * k5**2 * (Lsms + coef * k5**2 * lam**2)                  # SMS (18)
    GN = k5**4 * lam / ((24 if mut == "factor_48" else 48) * sp.pi)                       # SMS (19)
    k5sol = [s for s in sp.solve(sp.Eq(GN, G), k5) if s.is_positive is not False][0]      # (19) solved for kappa5
    L4_G = sp.simplify(L4expr.subs(k5, k5sol))
    exact = sp.simplify(L4_G - (4 * sp.pi * G * lam - 3 / ell**2)) == 0
    ell2 = sp.simplify(3 / (4 * sp.pi * G * lam - L4))                                     # the exact form
    ell2_rs = sp.simplify(ell2.subs(L4, 0))
    sol = sp.solve(sp.Eq(L4_G, 0), ell)
    ell2_solved = sp.simplify(sol[0] ** 2) if sol else None
    Mp2 = 1 / G                                                                            # MK (3), d = 0
    lam_mk = 3 * Mp2 / (4 * sp.pi * ell**2)                                                # MK (25)
    mk = ell2_solved is not None and sp.simplify(lam_mk.subs(ell, sp.sqrt(ell2_solved)) - lam) == 0
    # at the tuning: kappa5^2 lambda = 6/ell (from (18) at Lambda_4 = 0), SMS p.4's k = kappa5^2 lambda/6 = 1/ell
    tune = [t for t in sp.solve(sp.Eq(L4expr, 0), lam) if t.is_positive is not False]
    lam_t = tune[0] if tune else None
    k_sms = sp.simplify(k5**2 * lam_t / 6) if lam_t is not None else None
    G_t = sp.simplify(GN.subs(lam, lam_t)) if lam_t is not None else None
    G5 = k5**2 / (8 * sp.pi)                                                               # MK (3), d = 1
    g5_eq_Gell = G_t is not None and sp.simplify(G5 - G_t * ell) == 0                      # MK (27)
    g5sq = sp.simplify((G * sp.sqrt(ell2_rs)) ** 2 - 3 * G / (4 * sp.pi * lam)) == 0
    return {"L4_in_G": L4_G, "exact_L4": exact, "ell2_exact": ell2, "ell2_rs": ell2_rs, "ell2_solved": ell2_solved,
            "mk25": mk, "k_sms": k_sms, "k_is_1_over_ell": k_sms is not None and sp.simplify(k_sms - 1 / ell) == 0,
            "G_at_tuning": G_t, "G5_eq_G_ell": g5_eq_Gell, "G5sq": g5sq}


def derive_controls(mut=None):
    """Three controls that must fail: (a) a wrong tuning coefficient misses MK (25); (b) SMS p.4's scaling keeps G and
    moves ell -- G alone fixes nothing; (c) lambda < 0 gives G < 0 (SMS p.3)."""
    a = derive("lambda2_coef" if mut != "tuning_ok" else None)
    k5, lam, f = sp.symbols("kappa5 lambda f", positive=True)
    pw = 8 if mut == "scale_wrong" else 12                       # M_lambda -> f^3 M_lambda: lambda -> f^12 lambda
    k5f, lamf = k5 * f**-3, lam * f**pw                          # kappa5^-2 = M_G^3, M_G -> f^2 M_G: kappa5 -> f^-3 kappa5
    G = k5**4 * lam / (48 * sp.pi)
    Gf = sp.simplify(G.subs({k5: k5f, lam: lamf}, simultaneous=True))
    ell = 6 / (k5**2 * lam)                                      # at the tuning
    ellf = sp.simplify(ell.subs({k5: k5f, lam: lamf}, simultaneous=True))
    G_invariant = sp.simplify(Gf / G) == 1
    ell_moves = sp.simplify(ellf / ell) != 1
    lneg = sp.Symbol("lneg", negative=True)
    Gneg = (k5**4 * (sp.Abs(lneg) if mut == "abs_lambda" else lneg)) / (48 * sp.pi)
    return {"wrong_tuning_misses_MK25": not a["mk25"], "ell2_wrong": a["ell2_solved"],
            "G_invariant_under_SMS_scaling": G_invariant, "ell_scales_as": sp.simplify(ellf / ell),
            "ell_moves": ell_moves, "G_negative_for_negative_tension": bool(Gneg.is_negative)}


def two_sided(mut=None):
    """sigma = (3/kappa5^2)(k_a + k_b) (Israel, standard-not-READ; Z2 limit = GRS p.3, READ); G = G5 / int e^{-2k|y|}
    (H-ZERO-MODE-NORM; Z2 limit = MK (27), READ)."""
    ka, kb, k5, y, k = sp.symbols("k_a k_b kappa5 y k", positive=True)
    G5 = k5**2 / (8 * sp.pi)
    w = 4 if mut == "zero_mode_e4" else 2                        # MK (28) uses e^{-4y/ell}: the volume, not G's norm
    norm = sp.integrate(sp.exp(-w * ka * y), (y, 0, sp.oo)) + sp.integrate(sp.exp(-w * kb * y), (y, 0, sp.oo))
    Gt = sp.simplify(G5 / norm)
    sig = 3 * (ka + kb) / k5**2
    prod = sp.simplify(sig * Gt)
    z2_G = sp.simplify(Gt.subs({ka: k, kb: k}))
    z2_sig = sp.simplify(sig.subs({ka: k, kb: k}))
    grs = sp.simplify(z2_sig - 3 * k / (4 * sp.pi * G5)) == 0
    mk27 = sp.simplify(z2_G - G5 * k) == 0                       # M_p^2 = M5^3 ell <-> G = G5/ell
    return {"G_two_sided": Gt, "sigma_G": prod, "sigmaG_is_3kakb_over_4pi": sp.simplify(prod - 3 * ka * kb / (4 * sp.pi)) == 0,
            "Z2_sigma_is_GRS": grs, "Z2_G_is_MK27": mk27}


def check_C8(mut=None):
    d = derive(mut)
    ok = d["exact_L4"] and d["mk25"] and d["k_is_1_over_ell"] and d["G5_eq_G_ell"] and d["G5sq"]
    return ok, {k: str(v) for k, v in d.items()}


def check_C9(mut=None):
    d = derive_controls(mut)
    ok = d["wrong_tuning_misses_MK25"] and d["G_invariant_under_SMS_scaling"] and d["ell_moves"] and \
        d["G_negative_for_negative_tension"]
    return ok, {k: str(v) for k, v in d.items()}


def check_C10(mut=None):
    d = two_sided(mut)
    ok = d["sigmaG_is_3kakb_over_4pi"] and d["Z2_sigma_is_GRS"] and d["Z2_G_is_MK27"]
    return ok, {k: str(v) for k, v in d.items()}


# ------------------------------------------------------------------------------------------------ S3 Lambda_4
def lambda4(mut=None):
    k5, sig, ell, G = sp.symbols("kappa5 sigma ell G", positive=True)
    sig_rs = 6 / (k5**2 * ell)                                    # the tuned tension at fixed (kappa5, ell)
    L4_sms = sp.Rational(1, 2) * k5**2 * (-6 / (ell**2 * k5**2) + k5**2 * sig**2 / 6)
    form_k5 = sp.simplify(L4_sms - k5**4 * (sig**2 - sig_rs**2) / 12) == 0
    L4_G = 4 * sp.pi * G * sig - (0 if mut == "drop_ell_term" else 3 / ell**2)
    sig_rs_G = 3 / (4 * sp.pi * G * ell**2)                       # the tuned tension at fixed (G, ell)
    form_G = sp.simplify(L4_G - 4 * sp.pi * G * (sig - sig_rs_G)) == 0
    # does Lambda_4 fix sigma?  two bulk scales, the same G and Lambda_4, two tensions
    Lv, Gv = sp.Rational(1, 10**6), sp.Integer(1)
    s_of = [sp.solve(sp.Eq(L4_G.subs({G: Gv, ell: e}), Lv), sig) for e in (1, 2)]
    s_of = [s[0] if s else None for s in s_of]
    fixes_sigma = s_of[0] is not None and s_of[1] is not None and s_of[0] == s_of[1]
    b = base()
    Gs, c = b["G"], b["c"]
    if mut == "flat_omega":
        OL = 1.0
    else:
        OL = 1.0 - b["Omega_m"]                                   # flat LCDM, radiation (~1e-4) neglected: deduced
    L4num = 3 * OL * b["H0"]**2 / c**2
    rho_L = L4num * c**4 / (8 * math.pi * Gs)
    return {"form_kappa5": form_k5, "form_G": form_G, "sigma_for_ell_1_2": [str(s) for s in s_of],
            "Lambda4_fixes_sigma": fixes_sigma, "Lambda4_m2": L4num, "rho_Lambda_J_m3": rho_L, "Omega_L": OL}


PIN_L4 = {"Lambda4_m2": 1.08914e-52, "rho_Lambda_J_m3": 5.2447e-10, "rtol": 1e-3}   # this instrument's first values


def check_C11(mut=None):
    d = lambda4(mut)
    win = window()
    rel = 2 * d["rho_Lambda_J_m3"] / win["sigma_min_J_m3"]
    ok = (d["form_kappa5"] and d["form_G"] and not d["Lambda4_fixes_sigma"]
          and abs(d["Lambda4_m2"] / PIN_L4["Lambda4_m2"] - 1) < PIN_L4["rtol"]
          and abs(d["rho_Lambda_J_m3"] / PIN_L4["rho_Lambda_J_m3"] - 1) < PIN_L4["rtol"] and rel < 1e-60)
    d["departure_over_sigma_max"] = rel
    return ok, d


# ------------------------------------------------------------------------------------------------ S4 the window
def window(mut=None):
    b = base()
    G, c, hbar, m1 = b["G"], b["c"], b["hbar"], b["m1_m"]
    beta = 4.5e-4 if mut == "beta_k2" else BETA3_MAX
    ell_max = math.sqrt(1.5 * beta) * 1e-3 if mut != "inverted" else math.sqrt(beta / 1.5) * 1e-3
    c4 = 1.0 if mut == "no_c4" else c**4

    def sigma_of(ell):
        return 3 * c4 / (4 * math.pi * G * ell**2)

    tev4 = (1e12 * EV_J) ** 4 / (hbar * c) ** 3                  # (1 TeV)^4 in J/m^3
    s_min = sigma_of(ell_max)
    s_mk = sigma_of(MK42_ELL_M)
    lP = math.sqrt(hbar * G / c**3)
    s_P = sigma_of(lP)
    edges = {"SIM2 down the throat (ell_w_class)": b["ell_class"], "SIM2 reached point (ell_W)": b["ell_W"],
             "E-PASS cap (a candidate, not an edge)": 4.0}
    mpow = 1 if mut == "m1_not_squared" else 2
    caps = {k: (ell_max / (ce * m1)) ** 2 if mpow == 2 else ell_max / (ce * m1) ** 1 for k, ce in edges.items()}
    Nex = b["N_example"]
    s_max_ex = {k: sigma_of(ce * m1 * math.sqrt(Nex)) for k, ce in edges.items()}
    return {"ell_max_m": ell_max, "sigma_min_J_m3": s_min, "sigma_min_TeV4": s_min / tev4,
            "sigma_min_quarter_TeV": (s_min / tev4) ** 0.25, "sigma_at_0p1mm_TeV4": s_mk / tev4,
            "MK42_consistent": s_mk / tev4 > MK42_TEV4, "l_P_m": lP, "sigma_classical_max_J_m3": s_P,
            "m1_m": m1, "edges_in_m": edges, "N_cap": caps, "sigma_max_at_example_J_m3": s_max_ex, "N_example": Nex,
            "k_min_per_m": 1 / ell_max}


def floor_equivalence():
    """Under one coupling G5 = G ell (MK (27)): l5^3 = hbar G5/c^3 = l_P^2 ell, so ell > l5 <=> ell > l_P (deduced)."""
    ell, lP = sp.symbols("ell l_P", positive=True)
    l5 = (lP**2 * ell) ** sp.Rational(1, 3)
    return sp.simplify((ell / l5) ** 3 - (ell / lP) ** 2) == 0


def check_C12(mut=None):
    w = window(mut)
    cap = w["N_cap"]["SIM2 down the throat (ell_w_class)"]
    ok = (abs(w["ell_max_m"] / 13.9642e-6 - 1) < 1e-4                     # ITEM185's 13.964 um
          and abs(w["sigma_min_J_m3"] / 1.4818e53 - 1) < 2e-3
          and w["MK42_consistent"]
          and abs(cap / 1.85e58 - 1) < 0.01                               # ITEM186 S3's N < 1.85e58 at 13.96 um
          and floor_equivalence())
    return ok, {k: (v if not isinstance(v, dict) else {kk: float(vv) for kk, vv in v.items()}) for k, v in w.items()}


def check_C13(mut=None):
    """The tie does not grow with the README (191's requirement; ITEM179's sqrt(N) rule): ell from (G, sigma) has no N;
    the control ell = c m1 sqrt(N) does."""
    G, sig, N, c_, m1 = sp.symbols("G sigma N c m1", positive=True)
    ell_b6pp = sp.sqrt(3 / (4 * sp.pi * G * sig)) if mut != "tie_to_corridor" else c_ * m1 * sp.sqrt(N)
    ell_ctrl = c_ * m1 * sp.sqrt(N)
    ok = sp.diff(ell_b6pp, N) == 0 and sp.diff(ell_ctrl, N) != 0
    return ok, {"d_ell_dN": str(sp.diff(ell_b6pp, N)), "control_d_ell_dN": str(sp.diff(ell_ctrl, N))}


# ------------------------------------------------------------------------------------------------ S5 which G, which k
def which_g(mut=None):
    """From multiplane.lr() (PRZ eqs. 2.16-3.3 as transcribed there): the measured (far-zone, Newtonian) G against SMS's
    local G_N on our plane.  Newtonian strength ~ (1/Mhat^2)(1 + c0/2) (deduced from multiplane's h ~ T + (c0/2) eta T
    for a static source), normalised so that far apart (r -> oo) it is the one-plane RS value, where SMS (19) and MK (27)
    agree (S2)."""
    mpl = base()["mpl"]
    d = mpl.lr()
    kL, kR, r, M = mpl.kL, mpl.kR, mpl.r, mpl.M
    X = sp.Symbol("X", nonnegative=True)
    c0 = sp.Integer(-1) if mut == "einstein_c0" else d["c0"]
    proj = 1 if mut == "no_newton_projection" else (1 + c0 / 2)
    ratio = sp.simplify(2 * (d["ML2"] / d["Mhat2"]) * proj) if mut != "no_newton_projection" else \
        sp.simplify(2 * (d["ML2"] / d["Mhat2"]) * sp.Rational(1, 2))
    Xdef = sp.exp(-2 * kL * r) * (kL - kR) / kR
    ratio_X = sp.simplify((3 - X) / (3 * (1 + X)))
    in_X = sp.simplify(ratio - ratio_X.subs(X, Xdef)) == 0
    kr = sp.Rational(3, 4) * kL                                           # B6: k_R = 3 k_L / 4
    r0 = sp.simplify(ratio.subs({r: 0, kR: kr}))
    far = sp.limit(ratio.subs(kR, kr), r, sp.oo)
    g0 = sp.simplify(d["gamma"].subs({r: 0, kR: kr}))
    u = GAMMA_M1 + GAMMA_SIG                                              # 68% upper edge of gamma - 1
    Xmax = 3 * u / (2 + u)                                                # gamma = (3 + X)/(3 - X)
    dev = 1 - float(ratio_X.subs(X, Xmax))
    r_min = -0.5 * math.log(3 * Xmax)                                     # e^{-2 k_L r}/3 <= Xmax, in units of ell_L
    # on the coincident composite (r = 0) in the measured G: ell_L^2 = 3 G_loc^-1 / (4 pi sigma1) = 3 ratio /(4 pi G sigma1)
    cL = sp.nsimplify(3 * r0 / (4 * sp.pi))
    return {"ratio": ratio, "ratio_in_X": in_X, "ratio_r0": sp.nsimplify(r0), "ratio_far": far, "gamma_r0": g0,
            "X_max_cassini": Xmax, "G_dev_max": dev, "r_min_over_ellL": r_min, "ellR_over_ellL": sp.Rational(4, 3),
            "ellL2_times_G_sigma1_at_r0": cL, "ellR2_times_G_sigma1_at_r0": sp.nsimplify(cL * sp.Rational(16, 9))}


def check_C14(mut=None):
    d = which_g(mut)
    ok = (d["ratio_in_X"] and d["ratio_r0"] == sp.Rational(2, 3) and d["ratio_far"] == 1
          and d["gamma_r0"] == sp.Rational(5, 4) and 0 < d["G_dev_max"] < 1e-4 and 4.0 < d["r_min_over_ellL"] < 4.5)
    return ok, {k: str(v) for k, v in d.items()}


# ------------------------------------------------------------------------------------------------ S6 status
GREEN = {"PROVED", "DERIVED", "AXIOM", "DEFINITION"}


def status(mut=None):
    """The board's accounting (STRUCTURAL).  B6''a: the tie (k fixed by G and sigma on one axis) and its coefficient;
    B6''b: sigma's value.  Each input carries its own label; an input counts as green when it is M's (AXIOM), DERIVED,
    PROVED, READ at source or STRUCTURAL (135's board note: a premise ruled by M, READ at source, or shown forced)."""
    ok_labels = {"AXIOM", "DERIVED", "PROVED", "DEFINITION", "READ", "STRUCTURAL"}
    tie = {   # what "k's scale is fixed by G and sigma" rests on
        "SMS (13)-(14), (17)-(19); MK (3), (19), (22), (25), (27); GRS p.3 (READ at source)": "READ",
        "Israel junction, two-sided zero mode (standard-not-READ; their Z2 limits READ, S2 C10)": "READ",
        "planes joined through a higher dimension, a bulk with our plane in it (M's 57, 58, 120, 138)": "AXIOM",
        "matter on our plane kept apart from its tension (184; SMS (14)'s split, READ, ambiguous in cosmological "
        "contexts by SMS p.3)": "AXIOM",
        "the separation fixed, so the radion is no second axis (M's 141, carried as H-STATIC-PLANES; its word is "
        "'I suggest'; S1 C6)": "AXIOM",
        "the exact Lambda_4 form, so no tuning premise is needed (S3)": "DERIVED",
    }
    coeff = {  # what the number 3/(4 pi) rests on (it enters only when sigma is measured by a route other than ell)
        "our plane the mirror point (STRUCTURAL in B6's Lykken-Randall configuration; else the two-sided "
        "ell_a ell_b form, S2)": "STRUCTURAL",
        "measured G = SMS's local G_N: deduced to < 1e-4 within the LR family from Cassini's gamma (S5)": "DERIVED",
        "the same in a general multi-plane bulk (138) beyond the LR family: H-MEASURED-G-IS-LOCAL": "OPEN",
    }
    completeness = {"no corridor k of its own: 191 (M's, 'let's assume'), read by the board as H-ONE-K-LAW": "READING"}
    green = set(GREEN)
    if mut == "nature_flattened":
        green.add("NATURE")
    if mut == "open_hidden":
        coeff = {k: v for k, v in coeff.items() if v != "OPEN"}
    stat_a, stat_b = "DERIVED", "NATURE"                    # B6''b: 136 (8), "leave it to measurement"
    tie_green = stat_a in green and all(v in ok_labels for v in tie.values())
    coeff_scope = "the Z2 one-plane reading and the LR family (our current state by Cassini)" \
        if all(v in ok_labels for v in coeff.values() if v != "OPEN") else "none"
    coeff_open = [k for k, v in coeff.items() if v == "OPEN"]
    green_b = stat_b in green
    if mut == "reading_hidden":
        completeness = {}
    return {"B6''a": stat_a, "B6''b": stat_b, "tie_green": tie_green, "coefficient_green_on": coeff_scope,
            "coefficient_open_beyond": coeff_open, "green_b": green_b, "B6''_green": tie_green and green_b,
            "B6''_open": "OPEN" in (stat_a, stat_b), "tie": tie, "coefficient": coeff, "completeness": completeness,
            "overall": "NATURE (weakest conjunct)", "theorem_condition_met": "OPEN" not in (stat_a, stat_b)}


def check_C15(mut=None):
    s = status(mut)
    ok = (s["tie_green"] and not s["green_b"] and not s["B6''_green"] and not s["B6''_open"]
          and len(s["coefficient_open_beyond"]) == 1 and "READING" in s["completeness"].values())
    return ok, {k: v for k, v in s.items() if k not in ("tie", "coefficient")}


# The rows proposed for warptheorem.py's LEMMAS (the integration is done afterwards; nothing is written there here).
PROPOSED_ROWS = [
    ("B", "B6''a k's scale tied to our G and our plane's tension by one bulk law (191; one axis, 192): ell^2 = "
          "3c^4/(4 pi G sigma) on our plane read as one mirror plane (MK eq. (25)), exactly ell^2 = 3/(4 pi G sigma/c^4 "
          "- Lambda_4) (SMS eqs. (18)-(19)); two-sided ell_a ell_b = 3c^4/(4 pi G sigma); with B6's ratio ell_R = "
          "4 ell_L/3", "DERIVED",
     "lemmas/b6p_scale.py: the tie on SMS, MK, GRS (READ) and your 57, 58, 120, 138, 141, 184; the coefficient 3/(4 pi) "
     "on the mirror-plane reading and the Lykken-Randall family (Cassini, READ), OPEN beyond it; complete as k's scale "
     "on H-ONE-K-LAW (the board's reading of 191); the cypher on H-CYPHER-COUPLING-INDEX (the board's)"),
    ("B", "B6''b sigma, our plane's tension, by measurement (136 (8)): sigma >= 1.48e53 J/m^3 (ell <= 13.964 um); "
          "Lambda_4 fixes only sigma - sigma_RS, never sigma", "NATURE", "item 136 answer 8; lemmas/b6p_scale.py S3-S4"),
]


# ------------------------------------------------------------------------------------------------ checks & CLI
CHECKS = {
    "C1": (check_C1, "S1 Z2 planes, one kappa5: every measured language E = 0, agreeing; every coordinate a KEY (one "
           "axis)", [("anti_monotone", "G swapped at k = 2, 3 (no longer one chain)"),
                     ("second_coupling", "a second coupling: two G per plane")]),
    "C2": (check_C2, "S1 two-sided: G fixed by (k_a, k_b), adds nothing; the nonlinear law gives E > 0",
           [("second_coupling", "a second coupling lambda in {1, 2}"), ("z2_only", "only the Z2 slice (E = 0)")]),
    "C3": (check_C3, "S1 control: a second coupling flips information's binary on G",
           [("lam_one", "the control's second coupling removed")]),
    "C4": (check_C4, "S1 G5 fixed by (G, sigma), by no subset of {N, G, l_P}",
           [("tied_to_N", "G5 = G N planted in the law"), ("G_only", "G5 = G planted in the law")]),
    "C5": (check_C5, "S1 control G5 = G N: the binaries flip", [("law_cells", "the law's cells given to the control")]),
    "C6": (check_C6, "S1 the radion: separation free -> G a second axis; fixed -> one axis",
           [("no_radion", "the coincident ratio set to 1 (no scalar, no warp change)")]),
    "C7": (check_C7, "S1 every roster run; NOT-RUN kept; Z2 E = 0 in every roster",
           [("one_roster", "only roster 1173 run"), ("notrun_as_silent", "NOT-RUN relabelled SILENT")]),
    "C8": (check_C8, "S2 Lambda_4 = 4 pi G sigma - 3/ell^2 exactly; MK (25) at the tuning; k = 1/ell; G5 = G ell; "
           "G5^2 = 3G/(4 pi sigma)",
           [("sign_Lambda5", "Lambda_5 = +6/ell^2"), ("factor_48", "SMS (19) with 24 pi"),
            ("lambda2_coef", "SMS (18)'s 1/6 as 1/3")]),
    "C9": (check_C9, "S2 controls fail as they must: wrong tuning, G alone (SMS scaling), negative tension",
           [("tuning_ok", "the control given the right coefficient"), ("scale_wrong", "lambda -> f^8 lambda"),
            ("abs_lambda", "G computed from |lambda|")]),
    "C10": (check_C10, "S2 two-sided: sigma G = 3 k_a k_b/(4 pi); Z2 limits are GRS and MK (27)",
            [("zero_mode_e4", "G normalised with MK (28)'s volume factor e^{-4ky}")]),
    "C11": (check_C11, "S3 Lambda_4 = (kappa5^4/12)(sigma^2 - sigma_RS^2) = (4 pi G)(sigma - sigma_RS); it does not "
            "fix sigma; numbers pinned", [("drop_ell_term", "the bulk term dropped from Lambda_4"),
                                          ("flat_omega", "Omega_Lambda = 1")]),
    "C12": (check_C12, "S4 the window: 13.964 um, sigma_min, MK (42)'s (1 TeV)^4, ITEM186's N cap, the l5/l_P floor",
            [("beta_k2", "Table I's k = 2 bound used"), ("no_c4", "c^4 dropped"),
             ("inverted", "ell = sqrt(2 beta/3) mm"), ("m1_not_squared", "the README cap not squared")]),
    "C13": (check_C13, "S4 the tie does not grow with the README; the corridor control does",
            [("tie_to_corridor", "ell tied to c m1 sqrt(N)")]),
    "C14": (check_C14, "S5 G_meas/G_loc = (3 - X)/(3(1 + X)); 2/3 and gamma = 5/4 at r = 0; Cassini < 1e-4; "
            "r >= 4.3 ell_L", [("einstein_c0", "c0 forced to -1"), ("no_newton_projection", "the (1 + c0/2) dropped")]),
    "C15": (check_C15, "S6 the tie green on its inputs; B6''b NATURE, not green; B6'' not GREEN, not OPEN; the "
            "board's reading and the coefficient's OPEN scope named",
            [("nature_flattened", "NATURE counted green"), ("reading_hidden", "the completeness reading left out"),
             ("open_hidden", "the coefficient's OPEN scope beyond the LR family left out")]),
}


def _clean(x):
    if isinstance(x, dict):
        return {str(k): _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    if isinstance(x, (bool, int, float, str)) or x is None:
        return x
    return str(x)


def compute():
    b = base()
    out = {"base": {k: v for k, v in b.items() if k != "mpl"}, "reads": READS}
    out["S1"] = {n: {k: v for k, v in run_index(n).items() if k != "_cells"}
                 for n in ("z2", "two_sided", "control", "g5", "g5_control", "radion")}
    out["S2"] = {"derive": derive(), "controls": derive_controls(), "two_sided": two_sided()}
    out["S3"] = lambda4()
    out["S4"] = window()
    out["S4"]["floor_l5_iff_lP"] = floor_equivalence()
    out["S5"] = which_g()
    out["S6"] = status()
    out["proposed_rows"] = PROPOSED_ROWS
    return _clean(out)


def report(d):
    print("b6p_scale.py -- B6'': k's scale tied to our G and our plane's tension (items 191, 192)\n")
    print("S1 THE CYPHER (computed; encoding H-CYPHER-COUPLING-INDEX, the board's; every roster run)")
    for n, r in d["S1"].items():
        rr = r["rosters"]["1173"]
        es = {v["language"]: v["E"] for v in rr["verdicts"] if v["E"] is not None}
        print("  %-42s cells %-3s E(1173) %s agree %s | adds nothing: %s | KEY: %s"
              % (r["index"], r["cells"], es, rr["agree"], ", ".join(r["adds_nothing"]) or "-",
                 ", ".join(r["keys"]) or "-"))
    s2 = d["S2"]
    print("\nS2 THE RELATION (computed; READ SMS (18)-(19) p.3, MK (19), (25), (27) pp.8-9)")
    print("  Lambda_4 in G: %s (exact: %s); ell^2 exact = %s; at the tuning %s = MK (25): %s"
          % (s2["derive"]["L4_in_G"], s2["derive"]["exact_L4"], s2["derive"]["ell2_exact"], s2["derive"]["ell2_rs"],
             s2["derive"]["mk25"]))
    print("  SMS's k = %s (= 1/ell: %s); G5 = G ell: %s; G5^2 = 3G/(4 pi sigma): %s"
          % (s2["derive"]["k_sms"], s2["derive"]["k_is_1_over_ell"], s2["derive"]["G5_eq_G_ell"], s2["derive"]["G5sq"]))
    print("  two-sided: sigma G = %s; Z2 limits GRS %s, MK (27) %s"
          % (s2["two_sided"]["sigma_G"], s2["two_sided"]["Z2_sigma_is_GRS"], s2["two_sided"]["Z2_G_is_MK27"]))
    print("  controls: wrong tuning misses MK (25) %s (gives %s); SMS scaling keeps G %s, ell scales as %s; lambda < 0 "
          "gives G < 0 %s" % (s2["controls"]["wrong_tuning_misses_MK25"], s2["controls"]["ell2_wrong"],
                              s2["controls"]["G_invariant_under_SMS_scaling"], s2["controls"]["ell_scales_as"],
                              s2["controls"]["G_negative_for_negative_tension"]))
    s3 = d["S3"]
    print("\nS3 LAMBDA_4: (kappa5^4/12)(sigma^2 - sigma_RS^2) %s; (4 pi G)(sigma - sigma_RS) %s; fixes sigma: %s; "
          "Lambda_4 = %.4e m^-2, rho_Lambda = %.4e J/m^3" % (s3["form_kappa5"], s3["form_G"], s3["Lambda4_fixes_sigma"],
                                                            s3["Lambda4_m2"], s3["rho_Lambda_J_m3"]))
    s4 = d["S4"]
    print("\nS4 THE WINDOW: ell <= %.6e m -> sigma >= %.4e J/m^3 = %.4g TeV^4 (sigma^1/4 >= %.3f TeV); at 0.1 mm %.4g "
          "TeV^4 (MK (42) > 1: %s); classical floor sigma <= %.4e J/m^3 (ell > l_P = %.4e m)"
          % (s4["ell_max_m"], s4["sigma_min_J_m3"], s4["sigma_min_TeV4"], s4["sigma_min_quarter_TeV"],
             s4["sigma_at_0p1mm_TeV4"], s4["MK42_consistent"], s4["sigma_classical_max_J_m3"], s4["l_P_m"]))
    for k, ce in s4["edges_in_m"].items():
        print("  %-40s c = %-10.6g README cap N <= %.4e; sigma_max at the example README %.4e J/m^3"
              % (k, ce, s4["N_cap"][k], s4["sigma_max_at_example_J_m3"][k]))
    s5 = d["S5"]
    print("\nS5 WHICH G: G_meas/G_loc = %s; r = 0 (B6's ratio): %s, gamma %s; far: %s; Cassini X <= %.3e -> |dG/G| <= "
          "%.3e; r >= %.3f ell_L; ell_R = %s ell_L" % (s5["ratio"], s5["ratio_r0"], s5["gamma_r0"], s5["ratio_far"],
                                                      s5["X_max_cassini"], s5["G_dev_max"], s5["r_min_over_ellL"],
                                                      s5["ellR_over_ellL"]))
    print("  on the coincident composite (r = 0), in the measured G: ell_L^2 G sigma1 = %s, ell_R^2 G sigma1 = %s "
          "(against 3/(4 pi) on one Z2 plane)" % (s5["ellL2_times_G_sigma1_at_r0"], s5["ellR2_times_G_sigma1_at_r0"]))
    s6 = d["S6"]
    print("\nS6 STATUS: B6''a %s (the tie green on its inputs: %s; the coefficient 3/(4 pi) on %s; OPEN beyond: %s); "
          "B6''b %s (green: %s); B6'' GREEN: %s; OPEN: %s; overall %s"
          % (s6["B6''a"], s6["tie_green"], s6["coefficient_green_on"], s6["coefficient_open_beyond"], s6["B6''b"],
             s6["green_b"], s6["B6''_green"], s6["B6''_open"], s6["overall"]))
    print("  completeness as k's scale: %s" % s6["completeness"])


def selftest():
    t0 = time.perf_counter()
    allok = True
    lines = []
    for cid, (fn, what, _m) in CHECKS.items():
        ok, det = fn(None)
        allok = allok and ok
        lines.append("%-4s %s  %s\n      %s" % (cid, "PASS" if ok else "FAIL", what, json.dumps(_clean(det))[:900]))
    print("b6p_scale selftest (computed, READ and deduced; not verified; not seated)")
    print("\n".join(lines))
    print("selftest %s: %d checks, wall %.1f s (owners %.1f s)" % ("PASSED" if allok else "FAILED", len(CHECKS),
                                                                   time.perf_counter() - t0, base()["load_s"]))
    return allok


def mutants():
    t0 = time.perf_counter()
    passed, n = [], 0
    print("b6p_scale --mutants: each named mutation must make its check FAIL")
    for cid, (fn, what, muts) in CHECKS.items():
        for name, desc in muts:
            n += 1
            raised = ""
            try:
                ok, det = fn(name)
            except Exception as e:                         # a crash is not a pass; it is reported as a crash
                ok, raised = False, " [raised %r]" % (e,)
            if ok:
                passed.append((cid, name))
            print("%-4s [%s] %s: %s%s" % (cid, name, desc, "check FAILS (as required)" if not ok else
                                          "MUTATION PASSES (the check cannot fail this way)", raised))
    print("mutants: %d run, %d caught, %d passed %s; wall %.1f s" % (n, n - len(passed), len(passed), passed,
                                                                      time.perf_counter() - t0))
    return not passed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mutants", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    a = ap.parse_args(argv)
    rc = 0
    if a.selftest:
        rc |= 0 if selftest() else 1
    if a.mutants:
        rc |= 0 if mutants() else 1
    if a.json:
        with open(a.json, "w") as fh:
            json.dump(compute(), fh, indent=1)
        print("wrote %s" % a.json)
    if not (a.selftest or a.mutants or a.json):
        report(compute())
    return rc


if __name__ == "__main__":
    sys.exit(main())
