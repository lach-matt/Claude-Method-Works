#!/usr/bin/env python3
"""b6p_scale.py -- Warp Theorem lemma B6'' (a proposed edit of B6', k's scale): k's scale tied to our G and the plane's
tension through one bulk law (M-RULINGS items 191, 192).  Computed, READ and deduced; verified once by two separate AI
sessions of this project (a refute pass and an overclaim pass), whose findings are applied here; not seated; 2026-10-09.
Note: lemmas/B6P-SCALE.md.

B6'' AS APPLIED (section S6; the rows are PROPOSED_ROWS):
  B6''a0  the relation on ONE Z2 plane (SMS's premise): ell^2 = 3 c^4/(4 pi G sigma - Lambda_4 c^4), exactly (SMS eqs.
          (18)-(19)); at Lambda_4 = 0 it is MK eq. (25).  DERIVED from READ physics.  A limit (one plane), not M's
          configuration (138).
  B6''a   the tie in the chain's configuration: the planes coinciding (r = 0, the separation held, no radion: 127, 141,
          chain lemma B5) in multiplane.py's Lykken-Randall family.  The composite is one RS plane at k_R, so
          ell_R^2 = 3 c^4/(4 pi G sigma_sum), sigma_sum = sigma_1 + sigma_2 = (3/4) sigma_1 (139 (1)), with G the measured
          G (the composite's zero mode).  READING: it rests on the board's H-LR-ZERO-MODE (radion removed) and H-ONE-G5.
  B6''a2  a two-sided plane (k_a != k_b): (G, sigma) fix only the product k_a k_b.  READING (Israel's junction,
          standard-not-READ; H-ZERO-MODE-NORM, the board's).
  B6''b   sigma's value: NATURE (136 (8) rules k to measurement; carried to sigma through B6''a, deduced).
  B6''c   the tie at a finite static separation (our current state too, if its separation is not zero: 127's
          coincidence is carried "while the corridor exists", and with the radion removed gamma no longer bounds it), or
          in M's general multi-plane bulk (138): k is fixed only together with every separation.  OPEN.
STATUS (stated plainly, 135): B6'' is NOT GREEN (READ and standard-not-READ premises, the board's readings, a NATURE
value), and it carries one OPEN row, B6''c, which B6' did not carry.  The cypher CLASSIFIES (S1); it derives nothing.

CLI:  --selftest (every check, each able to fail; the wall time is printed by the run)
      --mutants  (every named mutation of every check, each shown to make its check FAIL; exit 1 if any passes)
      --json PATH (writes compute(), every row labelled)

LABELS.  Every result carries one of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  M's words are quoted verbatim, typing kept, from M-RULINGS-2026-10-03.md; the board's
readings are named H-... and kept apart from them.  Lemma statuses follow warptheorem.py's taxonomy; GREEN is the stated
rule (PROVED, DERIVED or AXIOM, with no non-green input), under which a READ input is a named premise, not green.

M'S WORDS USED (verbatim, typing kept):
  57       "If two points, each on a different spacetime plane, are connected by a corridor through a higher dimension,
           then speed cannot exist in the dimension below the corridor as you are at position 1 then position 2, with
           no in between, which means no travel, no speed"
  129 (1)  "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because the
           corridor is a bridge, so it adds nothing to either position."
  136 (8)  "8 - leave it to measurement. But we can accurately hypothesize it first. Measurement would confirm."
  138      "In the standard one-plane bulk  - the problem is that you assume the bulk is contained to a single plain. It
           is not. I keep saying, it is multi-universal."
  139 (1)  "1 - yes" (position 2's plane negative, a quarter of ours; ours positive)
  139 (4)  "4 - why are you still chasing distance/speed? This was ruled out"
  140      "If k helps define the bulk, the math in our work should give you pieces to both derive and prove k. Our math
           is not dependent on k, k is dependent on our work."
  141      "If planes are constantly in motion around each other, a stable throat cannot form. I suggest the planes are
           static, but their surfaces contain their own movements from within their own contained dimensions"
  184      "There are no matter free planes"
  187 (2)  M chose "For the math" (whether each universe, and a corridor's region, has its own Newton's constant)
  191      "Based on the results of gravity, let's assume the same interaction for k"
  192      "this appears to be a question to put to the math language hierarchy cypher"
  196      "Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher"

THE BOARD'S READINGS (named; withdrawn if M says otherwise):
  H-CYPHER-COUPLING-INDEX  how each question is encoded as an index for tools/cypher.py (S1).  The encoding is the
           board's; the roster stays data (every roster in cypher.py is run, none chosen).
  H-ONE-K-LAW  the board's reading of 191, as worded in 191's record: one five-dimensional curvature law; each
           universe's k follows from its own plane; no k of its own for a corridor's region; and so a tie that does not
           grow with the README.  Used only for B6'' to be the whole of "k's scale", and for the README caps in S4.
  H-ONE-G5  the board's provisional 187 (2) decision (ITEM186 sec. 6): one 5D coupling for the bulk (one M across the
           Lykken-Randall regions).
  H-ZERO-MODE-NORM  the board's model for a two-sided plane's G: the zero mode normalised over two infinite AdS sides
           (its Z2 limit checked against MK eq. (27), READ).
  H-LR-ZERO-MODE  the board's (bulk/MULTIPLANE.md): Lykken-Randall at linear order, zero modes only; used here, as in
           bulk/STATIC.md, with the radion removed (141, B5) rather than unstabilized.
  (H-MEASURED-G-IS-LOCAL, carried by the build, is withdrawn by the board in this pass: its Cassini grade needed the
  ghost radion that 141 and B5 remove.  On the composite the measured G is the composite's G, deduced; beyond it, B6''c.)

WHAT IS COMPUTED HERE
  S1 THE CYPHER (computed; H-CYPHER-COUPLING-INDEX; it classifies, it is not a physical derivation).  tools/cypher.py
     imported by path, every roster run.  The "fixed by" binaries come from this instrument's own helper determined()
     (the board's functional-dependence test), never from cypher.py, and are labelled so.
  S2 THE RELATION (computed, sympy; READ SMS eqs. (18), (19), p.3; MK eqs. (19), (25), (27), pp.8-9).
  S3 LAMBDA_4 (computed; READ SMS p.3-4, MK p.9), and through the cypher with a control (196).
  S4 THE WINDOW (computed; READ Adelberger et al. p.3, MK pp.10-11), scoped: 68% CL, MK eq. (41)'s one-plane law;
     the composite's window; the README caps under H-ONE-K-LAW; and the N-free ties run folded in (S4b).
  S5 WHICH G, WHICH k (computed from bulk/multiplane.py, imported; READ MK p.9, Will 1403.7377v1 p.43).
  S6 STATUS (STRUCTURAL): the board's accounting of its own labels -- what B6'' earns, on what; C15 checks the labels'
     consistency, not their truth.

Imports by path (never copied): tools/cypher.py; copy/exactE.py (E per sqrt bit, constants, the example README);
lemmas/sim2_facing.py (ell_w_class, the down-the-throat edge) and its bank lemmas/sim2_bank.json (ell_W, read as
data); bulk/multiplane.py (lr(), gamma_from_c0(): the Lykken-Randall two-plane law, PRZ); ../cosmo.py (H0, Omega_m).
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
              "RS 2-brane: There are two branes in this model [362], at y = 0 and y = L, with Z2-symmetry "
              "identifications y <-> -y, y + L <-> L - y. (24) The branes have equal and opposite tensions +-lambda, "
              "where lambda = 3 M_p^2 / (4 pi ell^2). (25)"),
    "MK_radion": ("Maartens, Koyama, 1004.3962v2", 9,
                  "In order to recover 4D general relativity at low energies, a mechanism is required to stabilize the "
                  "inter-brane distance, which corresponds to a scalar field degree of freedom known as the radion"),
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
BETA3_MAX = 1.3e-4             # READ ADEL_T1 (68% CL, k = 3)
E_README_155 = 3.8e22          # J: the board's figure quoted in item 155's question ("an exact README needs E >= 3.8e22 J")
V_EW_GEV = 246.22              # GeV, the electroweak scale from G_F: standard-not-READ (carried from item 191's ties run)
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
    """The board's functional-dependence helper (NOT tools/cypher.py): does the tuple of coordinates `by` fix `target`
    on these cells?  Its binaries are reported apart from the cypher's verdicts."""
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


def _q(x):
    x = Fr(x)
    return sp.Rational(x.numerator, x.denominator)


def _resid_sigmaG(cl):
    """Residual of a (k_a, k_b, sigma-ordinal, G) cell against S2's independently derived law sigma G = 3 k_a k_b/(4 pi)
    (two_sided(), sympy; sigma = 3 sigma_ord/(8 pi) at kappa5^2 = 8 pi).  The law holds at any kappa5."""
    if "sigmaG" not in _CACHE:
        _CACHE["sigmaG"] = two_sided()["sigma_G"]
    a, b_ = sp.symbols("k_a k_b", positive=True)
    law = _CACHE["sigmaG"].subs({a: _q(cl[0]), b_: _q(cl[1])})
    return sp.simplify(sp.Rational(3, 8) / sp.pi * _q(cl[2]) * _q(cl[3]) - law)


def _resid_g5(cl):
    """Residual of an exponent cell (n, g, s, l_P, g5) against S2's G5^2 = 3G/(4 pi sigma) (derive(): G5 = G ell at the
    tuning), evaluated at G = 2^g, sigma = 2^s; g5 is the doubled exponent with the constant log2(3/(4 pi)) dropped."""
    if "g5law" not in _CACHE:
        d = derive()
        lam, G = sp.symbols("lambda G", positive=True)
        _CACHE["g5law"] = sp.lambdify((G, lam), (G * sp.sqrt(d["ell2_rs"])) ** 2, "math")
    n, g, s, lp, g5 = (float(v) for v in cl)
    pred = math.log2(_CACHE["g5law"](2.0 ** g, 2.0 ** s)) - math.log2(3 / (4 * math.pi))
    return max(abs(g5 - pred), abs(lp - g))


def _resid_lambda4(cl):
    """Residual of a (3k^2, sigma, Lambda_4) cell against S2's exact Lambda_4 = 4 pi G sigma - 3/ell^2 (derive()'s
    L4_in_G, from SMS (18)-(19)), at 4 pi G = 1 and 3/ell^2 = 3k^2."""
    if "L4law" not in _CACHE:
        _CACHE["L4law"] = derive()["L4_in_G"]
    lam, ell, G = sp.symbols("lambda ell G", positive=True)
    val = _CACHE["L4law"].subs({G: 1 / (4 * sp.pi), lam: _q(cl[1]), ell: sp.sqrt(3 / _q(cl[0]))})
    return sp.simplify(_q(cl[2]) - val)


def _declare(cells, resid, what):
    """Analysis's declaration: it speaks only when the computed residual against the independent law is zero on every
    cell (F5: a witness is computed, never a static string)."""
    rs = [resid(cl) for cl in cells]
    zero = sum(1 for r in rs if abs(float(r)) < 1e-12)
    return {"analysis": {"speaks": zero == len(cells),
                         "witness": "%s; residual 0 on %d/%d cells (computed)" % (what, zero, len(cells))}}


def idx_spec(name, mut=None):
    """The board's indices (H-CYPHER-COUPLING-INDEX).  Returns (name, coords, cells, declared)."""
    co4 = ["k_a", "k_b", "sigma", "G"]
    s2law = "S2's law sigma G = 3 k_a k_b/(4 pi) (two_sided(), sympy)"
    if name == "z2":
        cells = [law_two_sided(k, k) for k in K]
        if mut == "anti_monotone":                       # swap G at k = 2, 3 (a law that is not one chain)
            cells[1][3], cells[2][3] = cells[2][3], cells[1][3]
        if mut == "second_coupling":
            cells += [law_two_sided(k, k, 2) for k in K]
        return ("Z2 planes, the coupling's value known (kappa5 fixed by units)", co4, cells,
                _declare(cells, _resid_sigmaG, s2law))
    if name == "z2_g5free":
        g5s = (1,) if mut == "g5_fixed" else (1, 2)
        # Z2 at coupling G5: sigma = 3k/(4 pi G5) -> ordinal 2k/G5 (= k_a + k_b at G5 = 1); G = G5 k (MK (27))
        cells = [[k, k, Fr(2 * k) if mut == "sigma_carries_no_g5" else Fr(2 * k, g5), Fr(g5 * k)]
                 for g5 in g5s for k in K]
        return ("CONTROL: Z2 planes, the coupling's value free (G5 in {1, 2})", co4, cells,
                _declare(cells, _resid_sigmaG, s2law))
    if name == "two_sided":
        lams = (1, 2) if mut == "second_coupling" else (1,)
        if mut == "z2_only":
            cells = [law_two_sided(k, k) for k in K]
        else:
            cells = [law_two_sided(a, b, l) for a, b in itertools.product(K, K) for l in lams]
        return "two-sided planes, the coupling's value known", co4, cells, _declare(cells, _resid_sigmaG, s2law)
    if name == "control":
        lams = (1,) if mut == "lam_one" else (1, 2)
        cells = [law_two_sided(a, b, l) for a, b in itertools.product(K, K) for l in lams]
        return "CONTROL: G with a coupling of its own", co4, cells, _declare(cells, _resid_sigmaG, s2law)
    co5 = ["N", "G", "sigma", "l_P", "G5"]
    grid = list(itertools.product((0, 1, 2), repeat=3))
    g5law = "S2's G5^2 = 3G/(4 pi sigma) (derive(), sympy) in exponent form, and l_P^2 = hbar G/c^3"
    if name == "g5":
        # exponent coordinates (log base 2, doubled): G5^2 = 3G/(4 pi sigma) -> g5 = g - s (+ const); l_P^2 = hbar G/c^3
        rule = {"tied_to_N": lambda n, g, s: g + n, "G_only": lambda n, g, s: g}.get(mut, lambda n, g, s: g - s)
        cells = [[n, g, s, g, rule(n, g, s)] for n, g, s in grid]
        return "G5 under one bulk law", co5, cells, _declare(cells, _resid_g5, g5law)
    if name == "g5_control":
        rule = (lambda n, g, s: g - s) if mut == "law_cells" else (lambda n, g, s: g + n)
        cells = [[n, g, s, g, rule(n, g, s)] for n, g, s in grid]
        return "CONTROL: G5 tied to the README (G5 = G N)", co5, cells, _declare(cells, _resid_g5, g5law)
    if name == "separation":
        r0 = sp.Rational(which_g()["ratio_r0"] if mut != "no_warp_change" else 1)
        r0 = Fr(int(r0.p), int(r0.q))
        coR = ["k_L", "sep", "sigma1", "G"]
        # sep 0: coincident (127, B5's r = 0); sep 1: far (X -> 0).  sigma1 = 24 M^3 k_L -> ordinal k_L; G_loc
        # proportional to k_L (SMS (19) at the tuning); the measured G = G_loc x ratio(sep), the radion removed (S5)
        cells = [[k, s, Fr(k), Fr(k) * (r0 if s == 0 else 1)] for k in K for s in (0, 1)]
        xsep = {0: sp.Rational(1, 3), 1: sp.Integer(0)}          # X = (k_L - k_R)/k_R at B6's ratio; 0 far apart
        return ("the separation: two planes, its value free", coR, cells,
                _declare(cells, lambda cl: sp.simplify(_q(cl[3]) - _q(cl[0]) / (1 + xsep[cl[1]])),
                         "G_meas = G_loc(k_L)/(1 + X), X = e^(-2 k_L r)(k_L - k_R)/k_R (S5, the radion removed)"))
    co3 = ["3k^2", "sigma", "Lambda4"]
    l4law = "S2's Lambda_4 = 4 pi G sigma - 3/ell^2 (derive(), from SMS (18)-(19)) at 4 pi G = 1"
    if name == "lambda4":
        bulk = (1,) if mut == "one_bulk_scale" else (1, 2, 3)
        cells = [[u, s, Fr(s) - (0 if mut == "drop_bulk_term" else u)] for u in bulk for s in (1, 2, 3)]
        return "Lambda_4 against sigma (S3)", co3, cells, _declare(cells, _resid_lambda4, l4law)
    if name == "lambda4_control":
        cells = [[u, s, Fr(s)] for u in (1, 2, 3) for s in (1, 2, 3)]
        return "CONTROL: Lambda_4 with no bulk term", co3, cells, _declare(cells, _resid_lambda4, l4law)
    raise KeyError(name)


def run_index(name, mut=None, rosters=None):
    cy = cypher()
    title, coords, cells, declared = idx_spec(name, mut)
    vo = {c: sorted({cl[i] for cl in cells}, key=float) for i, c in enumerate(coords)}
    out = {"index": title, "coords": coords, "cells": len(cells), "rosters": {},
           "analysis_witness": declared["analysis"]["witness"], "analysis_speaks": declared["analysis"]["speaks"]}
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
    """Z2 planes with the coupling's value known: every measured language E = 0 and agreeing, K.langclose holds, every
    coordinate a KEY.  That is the register 1356/1175 artefact (four monotone copies of one parameter): unit-free and
    silent about scale, reported as such and never as an answer."""
    r = run_index("z2", mut, rosters=["1173"])
    m = _measured(r)
    ok = (len(m) >= 4 and all(v["E"] == 0 for v in m) and r["rosters"]["1173"]["agree"] is True
          and r["rosters"]["1173"]["langclose"] is True and not r["rosters"]["1173"]["degenerate"]
          and sorted(r["keys"]) == sorted(r["coords"]))
    return ok, {"E": {v["language"]: v["E"] for v in m}, "keys": r["keys"], "agree": r["rosters"]["1173"]["agree"]}


def check_C1b(mut=None):
    """Control (F4): the coupling's value free.  The cypher gives E > 0 in some language, the languages disagree, no
    coordinate is a KEY; analysis speaks (sigma G = 3k^2/(4 pi) holds at any coupling).  The board's helper: G alone and
    sigma alone fix no k; (G, sigma) fix k -- one relation, two free numbers."""
    r = run_index("z2_g5free", mut, rosters=["1173"])
    m = _measured(r)
    rr = r["rosters"]["1173"]
    cells, co = r["_cells"], r["coords"]
    b = {"G": determined(cells, co, ["G"], "k_a"), "sigma": determined(cells, co, ["sigma"], "k_a"),
         "G+sigma": determined(cells, co, ["G", "sigma"], "k_a")}
    ok = (any(v["E"] > 0 for v in m) and rr["agree"] is False and not r["keys"] and r["analysis_speaks"]
          and not b["G"] and not b["sigma"] and b["G+sigma"])
    return ok, {"E": {v["language"]: v["E"] for v in m}, "agree": rr["agree"], "keys": r["keys"],
                "helper_k_fixed_by": b, "analysis": r["analysis_witness"]}


def check_C2(mut=None):
    """Two-sided: G fixed by (k_a, k_b) (the board's helper) and adds nothing (cypher, information); the nonlinear law
    gives E > 0."""
    r = run_index("two_sided", mut, rosters=["1173"])
    det = determined(r["_cells"], r["coords"], ["k_a", "k_b"], "G")
    m = _measured(r)
    ok = det and "G" in r["adds_nothing"] and any(v["E"] > 0 for v in m)
    return ok, {"helper_G_by_ka_kb": det, "adds_nothing": r["adds_nothing"], "E": {v["language"]: v["E"] for v in m}}


def check_C3(mut=None):
    """Control: a second coupling flips information's binary on G (cypher) and the helper's."""
    r = run_index("control", mut, rosters=["1173"])
    det = determined(r["_cells"], r["coords"], ["k_a", "k_b"], "G")
    ok = (not det) and "G" not in r["adds_nothing"]
    return ok, {"helper_G_by_ka_kb": det, "adds_nothing": r["adds_nothing"]}


G5_SETS = (["N"], ["G"], ["l_P"], ["G", "N"], ["G", "l_P", "N"], ["sigma"], ["G", "sigma"])


def check_C4(mut=None):
    """G5 fixed by (G, sigma), by no subset of {N, G, l_P} (the board's helper); information: sigma recoverable, N not."""
    r = run_index("g5", mut, rosters=["1173"])
    b = {"+".join(s): determined(r["_cells"], r["coords"], s, "G5") for s in G5_SETS}
    ok = (b["G+sigma"] and not any(b[k] for k in ("N", "G", "l_P", "G+N", "G+l_P+N", "sigma"))
          and "sigma" in r["adds_nothing"] and "N" not in r["adds_nothing"])
    return ok, {"helper_binaries": b, "adds_nothing": r["adds_nothing"]}


def check_C5(mut=None):
    """Control G5 = G N: the binaries flip -- fixed by (G, N), not by (G, sigma); N recoverable, sigma not."""
    r = run_index("g5_control", mut, rosters=["1173"])
    b = {"+".join(s): determined(r["_cells"], r["coords"], s, "G5") for s in G5_SETS}
    ok = b["G+N"] and not b["G+sigma"] and "N" in r["adds_nothing"] and "sigma" not in r["adds_nothing"]
    return ok, {"helper_binaries": b, "adds_nothing": r["adds_nothing"]}


def check_C6(mut=None):
    """The separation (radion removed): with its value free, G is not fixed by (k_L, sigma1) -- a second axis; at a fixed
    separation (either) it is (the board's helper)."""
    r = run_index("separation", mut, rosters=["1173"])
    free = determined(r["_cells"], r["coords"], ["k_L", "sigma1"], "G")
    fixed = all(determined([c for c in r["_cells"] if c[1] == s], r["coords"], ["k_L", "sigma1"], "G") for s in (0, 1))
    ok = (not free) and fixed
    return ok, {"helper_G_by_kL_sigma1_sep_free": free, "helper_G_by_kL_sigma1_sep_fixed": fixed}


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


def check_C16(mut=None):
    """S3's question through the cypher (196): does Lambda_4 fix sigma?  Law index (3k^2, sigma, Lambda_4) on SMS's exact
    form: the cypher's information finds every coordinate recoverable from the other two (one relation), no KEY,
    analysis speaks; the board's helper: Lambda_4 alone does not fix sigma, (Lambda_4, 3k^2) does.  Control (the bulk
    term dropped): the helper's binary flips (Lambda_4 fixes sigma), information's binary on 3k^2 flips (a free axis),
    and analysis falls silent on S2's law."""
    law = run_index("lambda4", mut, rosters=["1173"])
    ctl = run_index("lambda4_control", None, rosters=["1173"])
    hl = {"L4": determined(law["_cells"], law["coords"], ["Lambda4"], "sigma"),
          "L4+3k2": determined(law["_cells"], law["coords"], ["Lambda4", "3k^2"], "sigma")}
    hc = determined(ctl["_cells"], ctl["coords"], ["Lambda4"], "sigma")
    ok = (not hl["L4"] and hl["L4+3k2"] and "3k^2" in law["adds_nothing"] and not law["keys"] and law["analysis_speaks"]
          and hc and "3k^2" not in ctl["adds_nothing"] and not ctl["analysis_speaks"])
    return ok, {"law_E": {v["language"]: v["E"] for v in _measured(law)}, "law_agree": law["rosters"]["1173"]["agree"],
                "law_adds_nothing": law["adds_nothing"], "law_keys": law["keys"], "helper_law": hl,
                "control_E": {v["language"]: v["E"] for v in _measured(ctl)}, "control_adds_nothing": ctl["adds_nothing"],
                "helper_control_L4_fixes_sigma": hc, "law_analysis": law["analysis_witness"],
                "control_analysis": ctl["analysis_witness"]}


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


def window_composite(mut=None):
    """The window in the chain's configuration (deduced, on H-LR-ZERO-MODE at r = 0): the composite is one RS plane at
    k_R (S5), so MK eq. (41)'s one-plane law bounds ell_R, and ell_R <= 13.964 um gives sigma_sum >= sigma_min; with
    sigma_sum = (3/4) sigma_1 (139 (1)), sigma_1 >= (4/3) sigma_min.  (Bounding ell_L instead, with 9/(16 pi), would give
    0.75 sigma_min; ell_L has no bulk region at r = 0, so that is not the bound.)"""
    w = window()
    f = which_g()["sum_over_tau1"]                       # sigma_sum / sigma_1 = 3/4
    s1 = w["sigma_min_J_m3"] * (float(f) if mut == "composite_on_ellL" else 1 / float(f))
    return {"sigma_sum_min_J_m3": w["sigma_min_J_m3"], "sigma1_min_J_m3": s1, "sum_over_sigma1": str(f)}


def check_C12(mut=None):
    """The window on one RS plane (68% CL; MK eq. (41) is the one-plane law, and MK p.11 says these limits 'do not apply
    to the 2-brane case'), and on the chain's composite (deduced).  MK (42)'s (1 TeV)^4 at 0.1 mm is a consistency
    remark only: it is an inequality with ~1e2 slack and cannot catch a normalisation error; the pinned sigma_min can."""
    w = window(None if mut == "composite_on_ellL" else mut)
    wc = window_composite(mut)
    cap = w["N_cap"]["SIM2 down the throat (ell_w_class)"]
    ok = (abs(w["ell_max_m"] / 13.9642e-6 - 1) < 1e-4                     # ITEM185's 13.964 um
          and abs(w["sigma_min_J_m3"] / 1.4818e53 - 1) < 2e-3
          and abs(wc["sigma1_min_J_m3"] / 1.9756e53 - 1) < 2e-3            # the composite, sigma_1 = (4/3) sigma_sum
          and w["MK42_consistent"]                                         # consistency remark, not a guard
          and abs(cap / 1.85e58 - 1) < 0.01                               # ITEM186 S3's N < 1.85e58 at 13.96 um
          and floor_equivalence())
    out = {k: (v if not isinstance(v, dict) else {kk: float(vv) for kk, vv in v.items()}) for k, v in w.items()}
    out["composite"] = wc
    return ok, out


def check_C13(mut=None):
    """STRUCTURAL: the typed tie ell = sqrt(3/(4 pi G sigma)) contains no N, and the corridor control ell = c m1 sqrt(N)
    does.  sigma's own independence of N is SMS (14)'s tension/matter split (READ) with 129 (1) and 130 (1) (the corridor
    adds no matter): assumed, not tested here.  The no-growth requirement is the board's H-ONE-K-LAW, not M's words."""
    G, sig, N, c_, m1 = sp.symbols("G sigma N c m1", positive=True)
    ell_b6pp = sp.sqrt(3 / (4 * sp.pi * G * sig)) if mut != "tie_to_corridor" else c_ * m1 * sp.sqrt(N)
    ell_ctrl = c_ * m1 * sp.sqrt(N)
    ok = sp.diff(ell_b6pp, N) == 0 and sp.diff(ell_ctrl, N) != 0
    return ok, {"d_ell_dN": str(sp.diff(ell_b6pp, N)), "control_d_ell_dN": str(sp.diff(ell_ctrl, N))}


def ties_window(mut=None):
    """S4b, the N-free ties run folded in (item 191's task, a separate AI session's work, checked there; carried, not
    re-run).  Re-computed here: the window's tension scales.  Bottom: sigma^(1/4) at ell = 13.964 um.  Top: at the ell
    below which item 155's README no longer fits SIM2's down-the-throat edge, ell = 27.07 m1 sqrt(N155), with
    N155 = (3.8e22 J/E1)^2 (the board's 3.8e22 J quoted in item 155's question).  And the electroweak scale v^4
    (standard-not-READ) as a tension, which lands outside the window."""
    b, w = base(), window()
    G, c, hbar = b["G"], b["c"], b["hbar"]
    conv = 1.0 if mut == "no_hbar_c" else (hbar * c) ** 3

    def quarter_J(sig):
        return (sig * conv) ** 0.25

    N155 = (E_README_155 / b["E1_J"]) ** (1 if mut == "N_unsquared" else 2)
    ell_floor = b["ell_class"] * b["m1_m"] * math.sqrt(N155)
    s_top = 3 * c**4 / (4 * math.pi * G * ell_floor**2)
    v = (1e5 if mut == "v_inside" else V_EW_GEV) * 1e9 * EV_J
    ell_v = math.sqrt(3 * c**4 * (hbar * c) ** 3 / (4 * math.pi * G * v**4))
    bottom_GeV = quarter_J(w["sigma_min_J_m3"]) / (1e9 * EV_J)
    return {"N155": N155, "ell_floor_155_SIM2_m": ell_floor, "sigma_top_J_m3": s_top,
            "bottom_quarter_TeV": bottom_GeV / 1e3, "top_quarter_GeV": quarter_J(s_top) / (1e9 * EV_J),
            "ell_from_v4_m": ell_v, "v4_outside_window": ell_v > w["ell_max_m"] or ell_v < ell_floor,
            "bottom_over_v": bottom_GeV / (v / (1e9 * EV_J))}


def check_C17(mut=None):
    """S4b: the window admits tension scales from (9.18 TeV)^4 to about (3.7e11 GeV)^4; v^4 gives ell = 1.94 cm, outside,
    with v about 37 times below the bottom (the ties run's figures, re-computed)."""
    d = ties_window(mut)
    ok = (abs(d["N155"] / 6.8419e27 - 1) < 1e-3 and abs(d["bottom_quarter_TeV"] / 9.1812 - 1) < 1e-3
          and abs(d["top_quarter_GeV"] / 3.7217e11 - 1) < 2e-3 and d["v4_outside_window"]
          and abs(d["ell_from_v4_m"] / 1.94166e-2 - 1) < 1e-3 and abs(d["bottom_over_v"] / 37.29 - 1) < 2e-3)
    return ok, d


# ------------------------------------------------------------------------------------------------ S5 which G, which k
def which_g(mut=None):
    """From multiplane.lr() (PRZ eqs. 2.16-3.4 as transcribed there).  PRZ's c0 is the Einstein zero mode plus the radion:
    c0 = -1 + 8 Mhat^2/C_r (PRZ (3.3) with (3.4)).  The lemma's premise removes the radion (141 holds the separation; B5:
    no radion), so c0 = -1: G_meas/G_loc = 1/(1 + X) and gamma = 1 for every X.  At r = 0 the composite is one RS plane at
    k_R (summed tension 24 M^3 k_R, B5a; 1/Mhat^2 = k_R/M^3): ell_R^2 G sigma_sum = 3/(4 pi), ell_L^2 G sigma_1 = 9/(16 pi).
    The radion-kept branch (PRZ's c0, a dynamical ghost radion that 141, B5 and 139 (2) exclude) is computed only for
    the negative result: 2/3, gamma = 5/4 at r = 0, and a Cassini bound that would exclude B5's r = 0.
    Newtonian strength ~ (1/Mhat^2)(1 + c0/2) (deduced from multiplane's h ~ T + (c0/2) eta T for a static source),
    normalised so that far apart it is the one-plane RS value at k_L, G_loc (SMS (19), MK (27); S2)."""
    if mut is None and "which_g" in _CACHE:
        return _CACHE["which_g"]
    mpl = base()["mpl"]
    d = mpl.lr()
    kL, kR, r, M = mpl.kL, mpl.kR, mpl.r, mpl.M
    X = sp.Symbol("X", nonnegative=True)
    Xdef = sp.exp(-2 * kL * r) * (kL - kR) / kR
    kr = sp.Rational(3, 4) * kL                                           # B6: k_R = 3 k_L / 4 (139 (1)'s quarter)
    decomposition = sp.simplify(d["c0"] - (-1 + 8 * d["Mhat2"] / d["Cr"])) == 0

    def proj(c0):
        return 1 if mut == "projection_dropped" else (1 + c0 / 2)

    def ratio_of(c0):
        return sp.simplify(2 * (d["ML2"] / d["Mhat2"]) * proj(c0))

    c0p = d["c0"] if mut == "radion_kept" else sp.Integer(-1)            # the premise: the radion removed
    ratio = ratio_of(c0p)
    in_X = sp.simplify(ratio - (1 / (1 + X)).subs(X, Xdef)) == 0
    gamma = sp.simplify(mpl.gamma_from_c0(c0p))
    r0 = sp.nsimplify(sp.simplify(ratio.subs({r: 0, kR: kr})))
    far = sp.limit(ratio.subs(kR, kr), r, sp.oo)
    tau_sum = sp.simplify((d["tau1"] + d["tau2"]).subs(kR, kr))
    sum_rs = sp.simplify(tau_sum - 24 * M**3 * kr) == 0                  # B5a: the summed tension is the RS value at k_R
    f = sp.simplify(tau_sum / d["tau1"])                                  # sigma_sum / sigma_1 = 3/4
    cL = sp.nsimplify(3 * r0 / (4 * sp.pi))                               # ell_L^2 G_meas sigma_1 = (3/(4 pi)) ratio
    cR_sum = sp.nsimplify(cL * sp.Rational(16, 9) * (1 if mut == "sigma1_for_sum" else f))   # ell_R^2 G_meas sigma_sum
    # the radion-kept branch (conditional; for the negative result only)
    ratio_r = ratio_of(d["c0"])
    in_X_r = sp.simplify(ratio_r - ((3 - X) / (3 * (1 + X))).subs(X, Xdef)) == 0
    r0_r = sp.nsimplify(sp.simplify(ratio_r.subs({r: 0, kR: kr})))
    g0_r = sp.simplify(d["gamma"].subs({r: 0, kR: kr}))
    cr0 = sp.simplify(d["Cr"].subs({r: 0, kR: kr}))
    cass = {}
    for lab, u in (("68% CL", GAMMA_M1 + GAMMA_SIG), ("2 sigma (the board's Gaussian reading)", GAMMA_M1 + 2 * GAMMA_SIG)):
        xm = 3 * u / (2 + u)                                              # gamma = (3 + X)/(3 - X)
        cass[lab] = {"X_max": xm, "G_dev_max": 1 - (3 - xm) / (3 * (1 + xm)), "r_min_over_ellL": -0.5 * math.log(3 * xm)}
    out = {"decomposition_c0_is_einstein_plus_radion": decomposition, "ratio": ratio, "ratio_is_1_over_1pX": in_X,
           "gamma": gamma, "ratio_r0": r0, "ratio_far": far, "tau_sum_is_RS_at_kR": sum_rs, "sum_over_tau1": f,
           "ellL2_G_sigma1_at_r0": cL, "ellR2_G_sigma_sum_at_r0": cR_sum, "ellR_over_ellL": sp.Rational(4, 3),
           "radion_kept": {"ratio_in_X": in_X_r, "ratio_r0": r0_r, "gamma_r0": g0_r, "C_r_at_r0": cr0,
                           "C_r_negative": bool(cr0.is_negative), "cassini_if_radion_kept": cass}}
    if mut is None:
        _CACHE["which_g"] = out
    return out


def check_C14(mut=None):
    d = which_g(mut)
    rk = d["radion_kept"]
    ok = (d["decomposition_c0_is_einstein_plus_radion"] and d["ratio_is_1_over_1pX"] and d["gamma"] == 1
          and d["ratio_r0"] == sp.Rational(3, 4) and d["ratio_far"] == 1 and d["tau_sum_is_RS_at_kR"]
          and d["ellR2_G_sigma_sum_at_r0"] == sp.nsimplify(3 / (4 * sp.pi))
          and d["ellL2_G_sigma1_at_r0"] == sp.nsimplify(9 / (16 * sp.pi))
          and rk["ratio_in_X"] and rk["ratio_r0"] == sp.Rational(2, 3) and rk["gamma_r0"] == sp.Rational(5, 4)
          and rk["C_r_negative"])
    return ok, {k: str(v) for k, v in d.items()}


# ------------------------------------------------------------------------------------------------ S6 status
GREEN = {"PROVED", "DERIVED", "AXIOM"}       # the stated rule (f1_audit.green_table); READ is a named premise, not green


def _status_of(inputs):
    """warptheorem.py's taxonomy, weakest input first: any OPEN -> OPEN; any NATURE -> NATURE; any of the board's
    readings -> READING; otherwise DERIVED (from READ physics, standard-not-READ steps and M's items)."""
    labels = set(inputs.values())
    for lab in ("OPEN", "NATURE", "READING"):
        if lab in labels:
            return lab
    return "DERIVED"


def _labels_consistent(items):
    """Each input's label must match what its own text says it is: '(standard-not-READ' -> standard-not-READ; '(READ' ->
    READ; 'H-...' (the board's) -> READING.  A guard against a flattened label (F3, OC-2), not a test of truth."""
    for _st, inputs in items.values():
        for key, lab in inputs.items():
            if "(standard-not-READ" in key and lab != "standard-not-READ":
                return False
            if "(READ" in key and lab != "READ":
                return False
            if key.startswith("H-") and lab != "READING":
                return False
    return True


def status(mut=None):
    """The board's accounting of its own labels (STRUCTURAL).  Each item's status is derived from its inputs' labels, never
    typed in; GREEN = status PROVED, DERIVED or AXIOM with every input green.  C15 checks this accounting is consistent;
    it cannot check that the labels are true."""
    green = set(GREEN)
    if mut == "nature_flattened":
        green.add("NATURE")
    if mut == "read_counted_green":
        green |= {"READ", "standard-not-READ", "STRUCTURAL"}
    snr = "READ" if mut == "snr_as_read" else "standard-not-READ"
    a_inputs = {
        "B6''a0's inputs: SMS and MK (READ at source)": "READ",
        "PRZ eqs. 2.16-3.4 as transcribed in bulk/multiplane.py (READ there)": "READ",
        "H-LR-ZERO-MODE (the board's: Lykken-Randall at linear order, zero modes; the radion removed, as bulk/STATIC.md)":
            "READING",
        "H-ONE-G5 (the board's provisional 187 (2) decision: one M across both bulk regions)": "READING",
        "M's 57, 58, 120: planes joined through a higher dimension": "AXIOM",
        "M's 139 (1): position 2's plane negative, a quarter of ours (B6's k_R = 3 k_L/4, b6_k.py K3)": "AXIOM",
        "M's 127 with 141 (H-STATIC-PLANES; its word is 'I suggest'): the separation held": "AXIOM",
        "chain lemma B5, DERIVED: r = 0, no radion (it carries standard-not-READ inputs of its own)": "DERIVED",
    }
    if mut == "reading_hidden":
        a_inputs = {k: v for k, v in a_inputs.items() if not k.startswith("H-")}
    items = {
        "B6''a0": ("the relation on ONE Z2 plane: ell^2 = 3c^4/(4 pi G sigma - Lambda_4 c^4), exactly; a limit, not M's "
                   "configuration (138)",
                   {"SMS (13), (14), (18), (19) and the Z2 premise, p.3 (READ)": "READ",
                    "MK (3), (19), (22), (25), (27), pp.3, 8-9 (READ)": "READ",
                    "SMS (14)'s split of tension from matter, p.3 (READ; SMS: 'ambiguous, particularly in cosmological "
                    "contexts')": "READ",
                    "M's 184: every plane carries matter (sigma is the tension part of a plane that carries it)": "AXIOM",
                    "kappa5^2 Lambda_SMS = Lambda_5, deduced from SMS (6), (13) against MK (22)": "STRUCTURAL"}),
        "B6''a": ("the tie in the chain's configuration (planes coinciding, r = 0, separation held, no radion): the "
                  "composite is one RS plane at k_R, ell_R^2 = 3c^4/(4 pi G sigma_sum), sigma_sum = (3/4) sigma_1",
                  a_inputs),
        "B6''a2": ("a two-sided plane (k_a != k_b): (G, sigma) fix only k_a k_b, sigma G = 3 k_a k_b/(4 pi)",
                   {"Israel junction, two-sided (standard-not-READ; its Z2 limit is GRS p.3, READ)": snr,
                    "H-ZERO-MODE-NORM (the board's; its Z2 limit is MK (27), READ)": "READING"}),
        "B6''b": ("sigma's value",
                  {"M's 136 (8): k left to measurement (H-K-BY-MEASUREMENT), carried to sigma through B6''a (deduced)":
                       "AXIOM",
                   "sigma fixed by no lemma, Lambda_4 included (S3); the N-free ties are item 191's run, carried (S4b "
                   "re-computes only the window's scales and v^4): measurement fixes it": "NATURE"}),
        "B6''c": ("the tie at a finite static separation (our current state too, if its separation is not zero), or in "
                  "M's general multi-plane bulk (138; 123-124)",
                  {"k fixed only together with every separation (S1's separation index; S5)": "OPEN"}),
    }
    if mut == "open_hidden":
        items.pop("B6''c")
    out_items = {}
    for k, (stmt, inputs) in items.items():
        st = _status_of(inputs)
        out_items[k] = {"statement": stmt, "status": st, "inputs": inputs,
                        "green": st in green and all(v in green for v in inputs.values())}
    statuses = [v["status"] for v in out_items.values()]
    b6_open = ("OPEN" in ("DERIVED", "NATURE")) if mut == "open_hardcoded" else ("OPEN" in statuses)
    readings = {k.split(" ")[0] for v in items.values() for k, lab in v[1].items() if lab == "READING"}
    completeness = {"H-ONE-K-LAW (the board's reading of 191): no k of a corridor's own": "READING"}
    classification = {"H-CYPHER-COUPLING-INDEX (the board's encoding): the cypher classifies, it derives no item": "READING"}
    return {"items": out_items, "B6''_green": all(v["green"] for v in out_items.values()), "B6''_open": b6_open,
            "theorem_condition_met": not b6_open, "labels_consistent": _labels_consistent(items),
            "readings_named": sorted(readings), "completeness": completeness, "cypher": classification,
            "overall": "not GREEN; carries one OPEN row (B6''c); in the chain's configuration READING (a) and NATURE (b)"}


def check_C15(mut=None):
    s = status(mut)
    st = {k: v["status"] for k, v in s["items"].items()}
    ok = (st == {"B6''a0": "DERIVED", "B6''a": "READING", "B6''a2": "READING", "B6''b": "NATURE", "B6''c": "OPEN"}
          and not any(v["green"] for v in s["items"].values()) and not s["B6''_green"]
          and s["B6''_open"] and not s["theorem_condition_met"] and s["labels_consistent"]
          and {"H-ONE-G5", "H-LR-ZERO-MODE", "H-ZERO-MODE-NORM"} <= set(s["readings_named"])
          and "READING" in s["completeness"].values())
    return ok, {"statuses": st, "green": {k: v["green"] for k, v in s["items"].items()}, "B6''_open": s["B6''_open"],
                "labels_consistent": s["labels_consistent"], "readings_named": s["readings_named"]}


# The rows proposed for warptheorem.py's LEMMAS (the integration is done afterwards; nothing is written there here).
PROPOSED_ROWS = [
    ("B", "B6''a k's scale tied to our G and the tension by one bulk law (191, read as H-ONE-K-LAW): in the chain's "
          "configuration (the planes coinciding, r = 0, the separation held, no radion: 127, 141, B5) the composite is "
          "one RS plane at k_R and ell_R^2 = 3c^4/(4 pi G sigma_sum), sigma_sum = sigma_1 + sigma_2 = (3/4) sigma_1 "
          "(139 (1)); exactly ell_R^2 = 3/(4 pi G sigma_sum/c^4 - Lambda_4) (SMS eqs. (18)-(19)); its one-plane limit "
          "is MK eq. (25)", "READING",
     "lemmas/b6p_scale.py S2, S5: SMS, MK, PRZ (READ); your 57, 58, 120, 127, 139 (1), 141, 184; B5; the board's "
     "H-LR-ZERO-MODE (the radion removed) and H-ONE-G5; the cypher classifies it (H-CYPHER-COUPLING-INDEX), it does not "
     "derive it"),
    ("B", "B6''b sigma, the tension, by measurement (136 (8), carried to sigma through B6''a): sigma >= 1.48e53 J/m^3 on "
          "one RS plane (68% CL; MK eq. (41), the one-plane law), i.e. sigma_sum >= 1.48e53 and sigma_1 >= 1.98e53 J/m^3 "
          "on the composite; Lambda_4 fixes only sigma - sigma_RS, never sigma; the electroweak v^4 lands outside the "
          "window (S4b; the other N-free ties are item 191's run, carried)",
     "NATURE", "item 136 answer 8; lemmas/b6p_scale.py S3-S4b; item 191's N-free ties run"),
    ("B", "B6''c the tie at a finite static separation (our current state too, if its separation is not zero), or in "
          "your general multi-plane bulk (138): k is fixed only together with every separation", "OPEN",
     "lemmas/b6p_scale.py S1 (the separation index), S5"),
]


# ------------------------------------------------------------------------------------------------ checks & CLI
CHECKS = {
    "C1": (check_C1, "S1 Z2 planes, the coupling's value known: every measured language E = 0, agreeing; every "
           "coordinate a KEY -- the register 1356/1175 artefact, unit-free and silent about scale",
           [("anti_monotone", "G swapped at k = 2, 3 (no longer one chain)"),
            ("second_coupling", "a second coupling: two G per plane")]),
    "C1b": (check_C1b, "S1 control, the coupling's value free: E > 0, languages disagree, no KEY; (G, sigma) fix k, "
            "neither alone does (helper)",
            [("g5_fixed", "the coupling's value fixed again (G5 = 1 only)"),
             ("sigma_carries_no_g5", "sigma made independent of the coupling (sigma = 2k)")]),
    "C2": (check_C2, "S1 two-sided: G fixed by (k_a, k_b) (helper), adds nothing (cypher); the nonlinear law gives E > 0",
           [("second_coupling", "a second coupling lambda in {1, 2}"), ("z2_only", "only the Z2 slice (E = 0)")]),
    "C3": (check_C3, "S1 control: a second coupling flips information's binary on G",
           [("lam_one", "the control's second coupling removed")]),
    "C4": (check_C4, "S1 G5 fixed by (G, sigma), by no subset of {N, G, l_P} (helper)",
           [("tied_to_N", "G5 = G N planted in the law"), ("G_only", "G5 = G planted in the law")]),
    "C5": (check_C5, "S1 control G5 = G N: the binaries flip", [("law_cells", "the law's cells given to the control")]),
    "C6": (check_C6, "S1 the separation (radion removed): its value free -> G a second axis; fixed -> G fixed by (k_L, sigma1) (helper)",
           [("no_warp_change", "the coincident ratio set to 1 (G no longer changes with the separation)")]),
    "C7": (check_C7, "S1 every roster run; NOT-RUN kept; Z2 E = 0 in every roster",
           [("one_roster", "only roster 1173 run"), ("notrun_as_silent", "NOT-RUN relabelled SILENT")]),
    "C8": (check_C8, "S2 Lambda_4 = 4 pi G sigma - 3/ell^2 exactly; MK (25) at the tuning; k = 1/ell; G5 = G ell; "
           "G5^2 = 3G/(4 pi sigma)",
           [("sign_Lambda5", "Lambda_5 = +6/ell^2"), ("factor_48", "SMS (19) with 24 pi"),
            ("lambda2_coef", "SMS (18)'s 1/6 as 1/3")]),
    "C9": (check_C9, "S2 controls fail as they must: wrong tuning, G alone (SMS scaling), negative tension",
           [("tuning_ok", "the control given the right coefficient"), ("scale_wrong", "lambda -> f^8 lambda"),
            ("abs_lambda", "G computed from |lambda|")]),
    "C10": (check_C10, "S2 two-sided: sigma G = 3 k_a k_b/(4 pi) (so (G, sigma) fix only k_a k_b); Z2 limits are GRS "
            "and MK (27)", [("zero_mode_e4", "G normalised with MK (28)'s volume factor e^{-4ky}")]),
    "C11": (check_C11, "S3 Lambda_4 = (kappa5^4/12)(sigma^2 - sigma_RS^2) = (4 pi G)(sigma - sigma_RS); it does not "
            "fix sigma; numbers pinned", [("drop_ell_term", "the bulk term dropped from Lambda_4"),
                                          ("flat_omega", "Omega_Lambda = 1")]),
    "C16": (check_C16, "S3 through the cypher (196): Lambda_4 alone does not fix sigma, (Lambda_4, 3k^2) do; the "
            "control with no bulk term flips",
            [("drop_bulk_term", "the law's cells built with no bulk term"),
             ("one_bulk_scale", "the law's cells at one bulk scale only")]),
    "C12": (check_C12, "S4 the window (68% CL, one-plane law): 13.964 um, sigma_min; the composite's sigma_1 >= (4/3) "
            "sigma_min; ITEM186's N cap; the l5/l_P floor; MK (42) as a remark",
            [("beta_k2", "Table I's k = 2 bound used"), ("no_c4", "c^4 dropped"),
             ("inverted", "ell = sqrt(2 beta/3) mm"), ("m1_not_squared", "the README cap not squared"),
             ("composite_on_ellL", "the composite's bound put on ell_L with 9/(16 pi)")]),
    "C13": (check_C13, "S4 STRUCTURAL: the typed tie has no N; the corridor control does",
            [("tie_to_corridor", "ell tied to c m1 sqrt(N)")]),
    "C17": (check_C17, "S4b the ties run folded in: tension scales (9.18 TeV)^4 to ~(3.7e11 GeV)^4; v^4 outside",
            [("N_unsquared", "N155 not squared"), ("no_hbar_c", "the (hbar c)^3 conversion dropped"),
             ("v_inside", "the electroweak scale replaced by 100 TeV")]),
    "C14": (check_C14, "S5 radion removed: c0 = -1 + 8 Mhat^2/C_r split; G_meas/G_loc = 1/(1 + X), gamma = 1; 3/4 at "
            "r = 0; ell_R^2 G sigma_sum = 3/(4 pi), ell_L^2 G sigma_1 = 9/(16 pi); radion kept: 2/3, 5/4, ghost",
            [("radion_kept", "PRZ's c0 (the ghost radion) used as the premise"),
             ("projection_dropped", "the Newtonian projection (1 + c0/2) dropped"),
             ("sigma1_for_sum", "sigma_1 used where the summed tension belongs")]),
    "C15": (check_C15, "S6 statuses derived from labels: a0 DERIVED, a READING, a2 READING, b NATURE, c OPEN; none "
            "green; B6'' OPEN-bearing; labels consistent; readings named",
            [("nature_flattened", "NATURE counted green"), ("read_counted_green", "READ counted green"),
             ("reading_hidden", "the board's readings left out of B6''a"), ("snr_as_read", "standard-not-READ as READ"),
             ("open_hidden", "B6''c left out"), ("open_hardcoded", "B6''_open typed in from constants")]),
}


def _clean(x):
    if isinstance(x, dict):
        return {str(k): _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    if isinstance(x, (bool, int, float, str)) or x is None:
        return x
    return str(x)


S1_INDICES = ("z2", "z2_g5free", "two_sided", "control", "g5", "g5_control", "separation", "lambda4", "lambda4_control")


def compute():
    b = base()
    out = {"base": {k: v for k, v in b.items() if k != "mpl"}, "reads": READS}
    out["S1"] = {n: {k: v for k, v in run_index(n).items() if k != "_cells"} for n in S1_INDICES}
    out["S2"] = {"derive": derive(), "controls": derive_controls(), "two_sided": two_sided()}
    out["S3"] = lambda4()
    out["S4"] = window()
    out["S4"]["floor_l5_iff_lP"] = floor_equivalence()
    out["S4"]["composite"] = window_composite()
    out["S4b"] = ties_window()
    out["S5"] = which_g()
    out["S6"] = status()
    out["proposed_rows"] = PROPOSED_ROWS
    return _clean(out)


def report(d):
    print("b6p_scale.py -- B6'': k's scale tied to our G and the plane's tension (items 191, 192)\n")
    print("S1 THE CYPHER (computed; it classifies, it derives nothing; encoding H-CYPHER-COUPLING-INDEX, the board's; "
          "every roster run; 'adds nothing' and KEY are cypher.py's)")
    for n, r in d["S1"].items():
        rr = r["rosters"]["1173"]
        es = {v["language"]: v["E"] for v in rr["verdicts"] if v["E"] is not None}
        print("  %-58s cells %-3s E(1173) %s agree %s | adds nothing: %s | KEY: %s | analysis speaks %s"
              % (r["index"], r["cells"], es, rr["agree"], ", ".join(r["adds_nothing"]) or "-",
                 ", ".join(r["keys"]) or "-", r["analysis_speaks"]))
    s2 = d["S2"]
    print("\nS2 THE RELATION (computed; READ SMS (18)-(19) p.3, MK (19), (25), (27) pp.8-9)")
    print("  Lambda_4 in G: %s (exact: %s); ell^2 exact = %s; at the tuning %s = MK (25): %s"
          % (s2["derive"]["L4_in_G"], s2["derive"]["exact_L4"], s2["derive"]["ell2_exact"], s2["derive"]["ell2_rs"],
             s2["derive"]["mk25"]))
    print("  SMS's k = %s (= 1/ell: %s); G5 = G ell: %s; G5^2 = 3G/(4 pi sigma): %s"
          % (s2["derive"]["k_sms"], s2["derive"]["k_is_1_over_ell"], s2["derive"]["G5_eq_G_ell"], s2["derive"]["G5sq"]))
    print("  two-sided: sigma G = %s (so (G, sigma) fix only k_a k_b); Z2 limits GRS %s, MK (27) %s"
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
    print("\nS4 THE WINDOW (68%% CL; MK (41), the one-plane law): ell <= %.6e m -> sigma >= %.4e J/m^3 = %.4g TeV^4 "
          "(sigma^1/4 >= %.3f TeV); composite: sigma_sum >= %.4e, sigma_1 >= %.4e J/m^3; at 0.1 mm %.4g TeV^4 (MK (42) "
          "> 1: %s, a remark); classical floor sigma <= %.4e J/m^3 (ell > l_P = %.4e m)"
          % (s4["ell_max_m"], s4["sigma_min_J_m3"], s4["sigma_min_TeV4"], s4["sigma_min_quarter_TeV"],
             s4["composite"]["sigma_sum_min_J_m3"], s4["composite"]["sigma1_min_J_m3"],
             s4["sigma_at_0p1mm_TeV4"], s4["MK42_consistent"], s4["sigma_classical_max_J_m3"], s4["l_P_m"]))
    for k, ce in s4["edges_in_m"].items():
        print("  %-40s c = %-10.6g README cap N <= %.4e (under H-ONE-K-LAW); sigma_max at the example README %.4e J/m^3"
              % (k, ce, s4["N_cap"][k], s4["sigma_max_at_example_J_m3"][k]))
    t = d["S4b"]
    print("  S4b (ties run folded in): tension scales from (%.4f TeV)^4 to (%.4e GeV)^4 (ell from 13.964 um down to %.4e "
          "m, item 155's README at SIM2's edge, N155 = %.5e); v^4 gives ell = %.5e m, outside: %s; bottom/v = %.2f"
          % (t["bottom_quarter_TeV"], t["top_quarter_GeV"], t["ell_floor_155_SIM2_m"], t["N155"], t["ell_from_v4_m"],
             t["v4_outside_window"], t["bottom_over_v"]))
    s5 = d["S5"]
    rk = s5["radion_kept"]
    print("\nS5 WHICH G (radion removed, 141 and B5): c0 = Einstein + radion: %s; G_meas/G_loc = %s (= 1/(1 + X): %s); "
          "gamma = %s; r = 0 (B6's ratio): %s; far: %s; summed tension = RS at k_R: %s (sigma_sum/sigma_1 = %s)"
          % (s5["decomposition_c0_is_einstein_plus_radion"], s5["ratio"], s5["ratio_is_1_over_1pX"], s5["gamma"],
             s5["ratio_r0"], s5["ratio_far"], s5["tau_sum_is_RS_at_kR"], s5["sum_over_tau1"]))
    print("  the composite at r = 0: ell_R^2 G sigma_sum = %s, ell_L^2 G sigma_1 = %s; ell_R = %s ell_L"
          % (s5["ellR2_G_sigma_sum_at_r0"], s5["ellL2_G_sigma1_at_r0"], s5["ellR_over_ellL"]))
    print("  radion kept (a dynamical ghost radion, excluded by 141, B5, 139 (2); for the negative result only): r = 0 "
          "ratio %s, gamma %s, C_r = %s; Cassini, if it were kept: %s"
          % (rk["ratio_r0"], rk["gamma_r0"], rk["C_r_at_r0"], rk["cassini_if_radion_kept"]))
    s6 = d["S6"]
    print("\nS6 STATUS (the board's accounting of its own labels):")
    for k, v in s6["items"].items():
        print("  %-7s %-8s green %-5s %s" % (k, v["status"], v["green"], v["statement"]))
    print("  B6'' GREEN: %s; carries an OPEN row: %s; theorem condition met by B6'': %s; overall: %s"
          % (s6["B6''_green"], s6["B6''_open"], s6["theorem_condition_met"], s6["overall"]))
    print("  completeness as k's scale: %s" % s6["completeness"])


def selftest():
    t0 = time.perf_counter()
    allok = True
    lines = []
    for cid, (fn, what, _m) in CHECKS.items():
        ok, det = fn(None)
        allok = allok and ok
        lines.append("%-4s %s  %s\n      %s" % (cid, "PASS" if ok else "FAIL", what, json.dumps(_clean(det))[:900]))
    print("b6p_scale selftest (computed, READ and deduced; verified once by separate AI sessions, findings applied; "
          "not seated)")
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
