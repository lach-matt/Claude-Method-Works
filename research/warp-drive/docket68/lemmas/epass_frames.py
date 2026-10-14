#!/usr/bin/env python3
"""epass_frames.py -- E-PASS fix round, a standalone owner: the demands (spec X17, stationary half) and the frames (spec
X18: the corridor's generator classes, its two ends, and Lemma P).  Build specification: lemmas/EPASS-DESIGN-SPEC.md,
X17 (stationary half only), X18, checks C26, C30, C31 of its section 8.  sim2_passage.py imports this module by path
for those X-sections; it is never copied there.
Computed, READ and deduced; not verified; not seated; 2026-10-09.  Fix round applied the same day: the in-project
REFUTE and OVERCLAIM readings' findings (FIX_ROUND below lists each and what was done).

CLI:  --selftest     (every check; each able to fail)
      --mutants      (runs every named mutation of every check and shows that the check FAILS under it; exit 1 if any
                      mutation passes)
      --json PATH    (writes compute(): every value X17 and X18 need, each row labelled)
      --full-owner   (loads exactE's owners in full (cmb/cmbframe.py alone takes 70-100 s) and compares E with the
                      seeded route used by default)
      (no flag)      prints the report

LABELS.  Every result row carries one or more of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  G3 checks every token of every label and that no result row is unlabelled.  The board's
readings are named H-... and kept apart from M's words, quoted verbatim (typing kept) from M-RULINGS-2026-10-03.md;
G2 checks each quote inside its own numbered item.  A negative result is reported as plainly as a positive one
(M-IRREFUTABLE, 135).
TAGS.  [FREE]: holds whatever carries the corridor (a plane, a sheet, the bulk alone).  [PLANE] or [PLANE]-conditional:
uses eq. (17) as a plane's own metric, the board's pre-179 configuration.  Under 179/180 and clause (G), seated on M's
"Seat both" (187 (3)), eq. (17) is at most a plane's possible reading of the corridor's mouth (H-PLANE-READS-MOUTH, the
board's, OPEN), and under 184 its vacuum plane is a limit only.  [FREE given kappa = 0]: holds for any degenerate
(kappa = 0) AdS2 throat; the throat's kappa = 0 here comes only from eq. (17) at r0 = 2m (C26a computes it), so for the
corridor such rows are [PLANE]-conditional, and under 179 whether the bulk corridor's horizon is degenerate is OPEN.

M'S WORDS USED: verbatim in M_WORDS (23 entries of M's words, items 117-187), each checked by G2 inside its own
item.  Not M's words, and marked so: item 155's figure "E >= 3.8e22 J" (the board's, kept in M_WORDS under a key that
says so and checked inside item 155) and the board's own 176 sentence (BOARD_WORDS, quoted in full, checked inside
item 176).  Items named by the board's description only: 162 (H-FIXED-SIZE), 185 (the matter round).

READINGS.  M's, as carried in the rulings file: H-CORRIDOR-IN-BULK (179/180), H-README-ON-P2 (172 (1)),
H-COINCIDE-DOWN-THE-THROAT (172 (2)), H-SIDES-AS-HORIZON-PAIR (122 (3)), H-ONE-WAY-BY-NATURE (132), H-FIXED-SIZE
(162), H-COUPLING-IS-THE-APPEARANCE (177), H-NEC-NEVER-VIOLATED-AS-PAIR (183; "Carried as M's" in the rulings file; its
gloss "zero net null energy along each light ray" is the wording of the option the board put and M chose; clause (Z),
seated in 187 (3)), H-NO-MATTER-FREE-PLANES (184).  The board's: H-PARTNER-IS-THE-COUPLING (177 covers the exact
negative partner Lemma S demands; admitted under 183), H-PLANE-READS-MOUTH, H-PAIRING-IS-ENTANGLEMENT (176),
H-README-AS-NULL-DUST, H-POSITIVE-IN-OWN-FRAME (spec 4.3), H-POSITIVE-ON-P2, H-STATIONARY-CROSSING (spec 4.3; refused,
it becomes E-NS), H-SPLIT-AT-OUR-TENSION, H-FIXED-SIZE-AS-THETA-ZERO, H-END-2-IS-OUR-FAR-END (that end 2 is our own
plane's far end; OPEN, RI-6/PA-6).

X17 THE DEMANDS (stationary half).
  readme_flux_P1(): sympy, [PLANE]-conditional.  r_h is the root of eq. (17)'s F (owner b4_static via sim2_facing.B4,
    by path): r_h = 2m; its surface gravity is computed, kappa = 0 (the Schwarzschild control gives 1/4), so the
    Killing parameter v is affine.  W1 (STRUCTURAL): E = m c^2 of the hole of N bits, crossing uniformly over the S^2.
    kappa4^2 int T_vv dv = 8 pi m/(4 pi (2m)^2) = 1/(2m) per generator.  Mutations: r^2 -> r; Schwarzschild data.
    Under 172 (1) (H-README-ON-P2, M's) P1 is not the README's sheet: this number is a normalisation reference.
  stationary_demand(): Lemma S, owner lemmas/epass_pairing.py by path (bulk and sheet, degenerate and non-degenerate);
    the demand rows are gated on the owner's computed zeros and fall back to "OPEN (pointer only)".  On
    H-STATIONARY-CROSSING (the board's).  BULK FORM PRIMARY (179/180), [FREE]: T5^c(xi,xi) = -T5^R(xi,xi) -
    T5^m(xi,xi) on the stationary bulk horizon (R(xi,xi) = 0 with no field equation; T5 from the 5D Einstein equation
    with Lambda_5), = -T5^R on the premise T^m(xi,xi)|_H = 0 (matter held static across the horizon); 5D normalisation
    OPEN.  SHEET FORM, [FREE] (Israel): the same on the README's own sheet, which under 172 (1) is position 2's piece,
    not computed here (OPEN); P1's -1/(2m) is quoted as a reference only.  The pair's net is the owner's zero -- never
    "positive" (spec pitfall 13).  Under 183 the exact pair is admitted (H-PARTNER-IS-THE-COUPLING): the stationary
    crossing is OPEN, NOT refuted.  GJW's criterion (READ) is set beside it as a tension, OPEN.  Lemma S is independent
    of the planes' stress law and tension, given the 5D Einstein equation (and Israel for the sheet form), so it holds
    with matter on both planes (184); matter-free results are limits only.
  demand_si(): E = exactE.e_per_sqrt_bit() * sqrt(N) at o3_write.EXAMPLE_N (both by path), G and c as banked in
    o3_write: E = 2.40588e16 J, m = G E/c^4 = 1.98791e-28 m, 1/(2m) = 2.51521e27 m^-1; at item 155's E = 3.8e22 J (the
    board's figure): m = 3.13983e-22 m, 1/(2m) = 1.59244e21 m^-1.  E and m [FREE]; 1/(2m) [PLANE]-conditional.  G's
    exponent in E is read from the owner's own form and measured on the owner's computation at G(1 +- 1e-6): -1/2; so m
    and 1/(2m) carry u_r(G)/2 = 1.12e-5 at the N example and u_r(G) = 2.25e-5 at the fixed E (u(G): CODATA 2018,
    standard-not-READ).  Our universe's G; 187 (2) left a per-universe G "For the math" (OPEN).
  reads_beside(): GJW, MSY, MQ READs (PDF page, printed page), beside the demands, never a supply.
  answer_158_4(): stationary -- nothing net is absorbed (Lemma S, on H-STATIONARY-CROSSING); changing -- into the bulk's
    Weyl field and the creased bulk horizon, a necessary condition only.  Lemma L ([PLANE]) is NOT built here.

X18 ENDS, GENERATORS, LEMMA P.
  generator_classes() [FREE]: global AdS2, Y^-1 = cos T/sin s, Y^0 = sin T/sin s, Y^1 = -cos s/sin s (the
    parametrisation is standard-not-READ; its induced metric is computed equal to MQ (2.1), READ PDF p.5); so(2,1)
    matrices; each Killing field by projection, its Killing equation verified, its class found two ways (eigenvalues /
    nilpotency, and Q = (nabla xi)^2/2 - xi.xi/L^2 with Q = -tr(M^2)/2 checked): d_T elliptic, components (1, 1),
    xi.xi = -1/sin^2 s < 0 everywhere (no Killing horizon); B_origin hyperbolic, (-cos T, +cos T); K hyperbolic,
    (+sin T, -sin T); J +- K parabolic, (1 +- sin T, 1 -+ sin T); J - B_origin parabolic, (1 + cos T, 1 - cos T).
  poincare_map(), embedding_generator(), throat_dv_pushforward() [FREE]: x = 8/z^2 gives 4(-dt^2 + dz^2)/z^2, z =
    2 sqrt2/u; the Poincare d_t is the unique so(2,1) matrix J - B_origin (nilpotent: parabolic), and the throat's d_v
    pushes forward to it along the EF chart.  throat_generator() [FREE given kappa = 0]: on the EF block Q = 0,
    parabolic; a non-degenerate g_vv gives Q = -1/72, hyperbolic.
  ends_map(): smooth through u = 0; end 1 on sigma = 0, end 2 on sigma = pi; u = 0 is patch 1's future and patch 2's
    past horizon (computed).  The same shape as 122 (3)/132 only if patch 2 is position 2's side, which is OPEN.
  ads2_family_classes(): on -(x/2)dt^2 + dx^2/(x(x - delta)), R = -1/2 for every delta and Q = delta/8: an AdS2
    throat alone does not fix the class; kappa = 0 puts the corridor at delta = 0.
  lemma_p(n=1000, seed=5): (i) [FREE] S = s delta reads -s for every observer (1000 exact rational Lorentz
    transformations, three s); (ii) [PLANE]-conditional: eq. (17)'s Weyl fluid at r = 3m, rho' < 0 beyond v* = 1/sqrt3
    (rapidity 0.658479), -> -infinity as v -> 1; v is an OBSERVER'S boost parameter, never a speed; NEC matter gives
    rho' >= rho, and where rho < 0 < rho + p a boost beyond v* = sqrt(-rho/p) reads it positive; (iii) [FREE given
    AdS2]: the boundary charge sin(sigma)(-xi.n), the same quantity as C30a's components read as a charge, flips under
    B_origin and not under J, J +- K, J - B_origin.
  deduced_x18(): S15's coincident delta-stress (frame-invariant at the limit only, never reached; along the approach a
    boosted observer can read positive wherever rho + p_i > 0); the board's 176 sentence fails WITHIN ONE UNIVERSE at
    the limit under four named premises, and its between-universes clause is OPEN (not refuted as a whole); the
    corridor as the extremal member given kappa = 0.

CHECKS (each calls this module's computing function on the mutated input; --mutants shows each fails):
  C26a 1/(2m), r_h = 2m, kappa(eq17) = 0 vs control 1/4 [r^2->r, schwarzschild-data];  C26b SI values [r^2->r,
  c^4->c^2];  C26c READ transcriptions and design-stage pages [altered-quote, page-99];  C26d E's G-exponent: the
  owner's form = the owner's computation = the owner's banked u_r(E) = dimensional analysis, carried into demand_si
  [E-as-J*m, form-G->G^2];  C26e Lemma S owner zeros gate the demand [non-stationary-gvv];  C30a classes, components,
  (2.1), J's norm [J+2K, Y-scaled-by-2];  C30b Poincare, throat d_v, embedding and pushforward [non-degenerate-gvv,
  x=8/z, dilatation-for-d_t];  C30c the ends [outgoing-chart, mirror-identification];  C30d the AdS2 family
  [delta-sign-flipped];  C31a delta-density under 1000 boosts [dust-added];  C31b v* = 1/sqrt3 and the v -> 1 limit
  [p_r-sign-flipped];  C31c NEC rows and the approach counterpart [NEC-violating];  C31d the flip [xi.xi-for-xi.n,
  J+2K];  G1 keys/args vs BANNED_KEYS/BANNED_ARGS [planted-key-hold_time, planted-arg-gap];  G2 quotes inside their
  own items [altered-M-quote, swapped-items];  G3 labels, unlabelled rows, pages [planted-label,
  computed-and-verified, row-without-label, READ-without-page].

Owners imported by path, never copied: sim2_facing.py (BANNED_KEYS, BANNED_ARGS, B4._eq17, B4._schwarzschild,
_ricci_diag, r_hat), copy/exactE.py (e_per_sqrt_bit, U_R_G, its chain.py's coefficients(); by default exactE's and
chain's owner caches are seeded with only the owners those functions' own source reads, located through the owners'
own path tables -- cmb/cmbframe.py is not loaded; --full-owner loads everything), lemmas/o3_write.py (EXAMPLE_N, G_SI,
C_SI), lemmas/epass_pairing.py (Lemma S: bulk_gvv, sheet_gvv, non_stationary, pairing_bulk, pairing_sheet).  Data only
(never evidence): EPASS-DESIGN-SPEC.md section 10 and epass_ground.json (design-stage READ transcriptions),
M-RULINGS-2026-10-03.md.  It is necessary, not sufficient, and never B4d green.  No value here is a length (155 (2):
bits), a distance, a speed (139 (4)) or anything the device sees (101 (7)).
python3 epass_frames.py [--selftest] [--mutants] [--json PATH] [--full-owner]   (stdlib + sympy; python 3.11)
"""
import contextlib
import functools
import importlib.util
import inspect
import io
import json
import math
import os
import random
import re
import sys
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy.parsing.sympy_parser import implicit_multiplication_application, parse_expr, standard_transformations

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
SPEC = os.path.join(HERE, "EPASS-DESIGN-SPEC.md")
GROUND = os.path.join(HERE, "epass_ground.json")
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
PAIRING = os.path.join(HERE, "epass_pairing.py")
PASSAGE = os.path.join(HERE, "sim2_passage.py")
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
G_U_CODATA = 0.00015e-11           # CODATA 2018 standard uncertainty of G (m^3 kg^-1 s^-2): standard-not-READ
E_ITEM155 = 3.8e22                 # J: the board's figure as put in item 155 ("an exact README needs E >= 3.8e22 J")
SI_EXPECTED = {"E_N_J": 2.40588e16, "m_N": 1.98791e-28, "inv2m_N": 2.51521e27,   # the spec's X17 numbers (to be met)
               "m_155": 3.13983e-22, "inv2m_155": 1.59244e21}
SI_TOL = 1e-5
S15_NEC_BOUND = sp.Rational(94, 10**8)   # SIM2-FACING S15: (rho + p_i)/sigma_RS <= 9.4e-7 at x = 1e-14 (computed there)

FIX_ROUND = [
    "M1 (REFUTE): C26d no longer compares a generic constant with two banked literals. E's G-exponent is read from "
    "the owner's own form, checked to reproduce the owner's value, measured on the owner's computation at G(1 +- 1e-6), "
    "matched to the owner's banked u_r(E) and carried into demand_si's u_r rows; mutation form-G->G^2.",
    "M2 (REFUTE), OC-3 (OVERCLAIM): S15's delta-stress and the 176 sentence are no longer [FREE]; the sentence is said "
    "to fail within one universe at the coincidence limit under four named premises, its between-universes clause "
    "OPEN, quoted in full.",
    "m1: J - B_origin (the Poincare d_t) added to C30a and C31d; C31d reads (iii) as C30a's components read as a "
    "charge (identity checked); mutation J+2K added to C31d.",
    "m2: C26a computes the surface gravity: kappa(eq. 17) = 0 against the Schwarzschild control's 1/4; mutation "
    "schwarzschild-data.",
    "m3, OC-7: G3 tokenises every label and flags unlabelled rows; mutations computed-and-verified, row-without-label.",
    "m4, OC-6: the Lemma S owner is called for both bulk and sheet, degenerate and non-degenerate; the demand rows are "
    "gated on its zeros (else 'OPEN (pointer only)'); check C26e with the owner's non_stationary() mutation.",
    "m5: C30b gains the pushforward of d_v and a dilatation mutation; C30d checks the AdS2 family; C31b checks the "
    "v -> 1 limit; C26b gains c^4->c^2.",
    "m6: Lemma S stated as independent of the stress law and tension given the 5D Einstein equation (Israel for the "
    "sheet form); the demand is T^c = -T^R - T^m with T^m(xi,xi)|_H = 0 an explicit premise.",
    "m7, OC-1: P1's 1/(2m), its partner and the 1/(2m) SI column are [PLANE]-conditional; P1 is a normalisation "
    "reference, not the README's sheet under 172 (1).",
    "m8, OC-9: the parametrisation Y(T, sigma) is standard-not-READ; its induced metric is computed equal to MQ (2.1) "
    "(READ PDF p.5); mutation Y-scaled-by-2.",
    "OC-2: parabolic needs kappa = 0; corridor-specific X18 rows are [FREE given kappa = 0], with kappa = 0 from eq. "
    "(17) ([PLANE]); OPEN under 179.",
    "OC-4: 'no frame makes it positive' is said of the never-reached limit only; the approach counterpart (a boost "
    "beyond v* reads positive wherever rho + p_i > 0) is computed and checked.",
    "OC-5: GJW's ANEC criterion is about the total; Lemma S's zero total is GJW's cancelling case; reported beside 183 "
    "as a tension, OPEN (GJW PDF pp.3-4 READ in this fix round).",
    "OC-8: G2 finds each quote inside its own item; mutation swapped-items.",
    "OC-10: MQ p.53's 'no horizon' is quoted with its hedge and set beside; the elliptic member's lack of a Killing "
    "horizon is computed (d_T's norm) and MQ PDF p.7's constant-sigma boundaries READ.",
    "OC-11: MSY's one-sided parametric bound worded as an upper bound.",
    "OC-12: the stationary rows name H-STATIONARY-CROSSING (the board's; refused, E-NS).",
    "OC-13: ends_map's 122 (3)/132 shape is conditional on patch 2 being position 2's side (OPEN).",
    "OC-14: the docstring no longer lists the board's descriptions under a 'verbatim' heading.",
    "OC-15: Wolfram cross-checks are banked in the fix round's scratch directory, or not claimed.",
    "OC-16: C30c's patch-sign clause (an identity of the chart) is dropped from the check and labelled deduced; "
    "C26c is described as transcription consistency and now checks pages against the design-stage files.",
]


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


SF = _load(os.path.join(HERE, "sim2_facing.py"), "epass_frames_sim2_facing")
_OWN = {}


def _owner(name):
    if name not in _OWN:
        path = {"exactE": os.path.join(D68, "copy", "exactE.py"), "o3_write": os.path.join(HERE, "o3_write.py"),
                "pairing": PAIRING}[name]
        _OWN[name] = _load(path, "epass_frames_" + name)
    return _OWN[name]


def _passage_banned_keys():
    """sim2_passage.BANNED_KEYS read from its source text, never executed (another run edits that file)."""
    try:
        with open(PASSAGE) as fh:
            m = re.search(r"^BANNED_KEYS\s*=\s*\(([^)]*)\)", fh.read(), re.M)
        return tuple(re.findall(r"\"([^\"]+)\"", m.group(1))) if m else ()
    except OSError:
        return ()


BANNED_ARGS = set(SF.BANNED_ARGS)
BANNED_KEYS = tuple(sorted(set(SF.BANNED_KEYS) | set(_passage_banned_keys())))


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def _short(x, n=160):
    s = str(x)
    return s if len(s) <= n else s[:n] + " ..."


# ======================================================================================== M's words (verbatim; G2)
M_WORDS = {
    "117": "An NEC is never violated, between two entangled positions the NEC is like a coin, each position sits on "
           "a separate side. That action is that the coin flips. The NEC appears broken, but is not",
    "120": "it was an methaphor to describe that the NEC only ever appears to break, but never does",
    "122 (3)": "3 - your candidate is correct",
    "122 (4)": "4 - yes. The er=epr only apply to physical matter. The rules apply, but do not restrict information",
    "129 (1)": "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because "
               "the corridor is a bridge, so it adds nothing to either position.",
    "132": "yes. And the passage is one way by nature, a black hole in and a white hole out, side views of the same "
           "corridor object",
    "132 (correction)": "*different views of the same object",
    "139 (2)": "2 - positive, and you have to prove it.",
    "139 (4)": "4 - why are you still chasing distance/speed? This was ruled out",
    "158 (4)": "This too is a question for the math.",
    "162": "Although the chain illustrates a corridor, I submit that it may be more like a black hole, containing both "
           "mouths and throat at once. The throat doesn't change size because the whole chain object only every takes "
           "on the size that contains the README upon opening. It is and always will be only the size that is needed "
           "to hold the object once and at once",
    "172 (1)": "M chose: \"Yes, it may\"",
    "172 (2)": "M chose: \"Yes, that is coinciding\"",
    "176": "But what if it is in fact entanglement?",
    "177": "M chose: \"Yes, that is the appearance\"",
    "179": "Let's approach this from a different angle. We know the corridor doesn't not sit on either position's "
           "plane, it only bridges them. So one could surmise that the corridor is exclusive to the bulk.",
    "180": "We know the corridor *does not sit on either position's plane, it only bridges them.",
    "181": "this bears directly on B4d, and requires priority",
    "182": "If I had to guess, I would go with C",
    "183": "M chose: \"Yes: never violated as a pair\"",
    "184": "There are no matter free planes",
    "185": "If it has potential to solve most of the current and future work, then we should run that now",
    "187 (3)": "M chose: (1) \"For the math\"; (2) \"For the math\"; (3) \"Seat both\"",
    "155 (the board's figure, not M's words)": "an exact README needs E >= 3.8e22 J",
}
BOARD_WORDS = {   # the board's own sentences, quoted in full where a result bears on them (not M's words)
    "176 (the board's answer, not M's words)": "Taken as entanglement: position 2's -1 would be the partner's sign seen "
    "from our side, an appearance, with 139 (2)'s positivity to be shown in position 2's own frame (between universes, "
    "phase 3)",
}


@functools.lru_cache(maxsize=None)
def _rulings_items():
    """The rulings file split at its item headings '^N. **': {N: whitespace-normalised text of item N}."""
    with open(RULINGS) as fh:
        t = fh.read()
    starts = [(int(m.group(1)), m.start()) for m in re.finditer(r"^(\d+)\. \*\*", t, re.M)]
    items = {}
    for i, (n, s) in enumerate(starts):
        e = starts[i + 1][1] if i + 1 < len(starts) else len(t)
        items[n] = (items.get(n, "") + " " + _norm(t[s:e])).strip()
    return items


def m_words_verbatim(words=None):
    """G2's computation: each quote found verbatim (whitespace-normalised for line wrapping) INSIDE the item its key
    names (the key's leading number), so a quote filed under the wrong item fails.  Label: computed."""
    words = {**M_WORDS, **BOARD_WORDS} if words is None else words
    items = _rulings_items()
    return {k: (_norm(q) in items.get(int(re.match(r"\d+", k).group()), "")) for k, q in words.items()}


# ======================================================================================== READs (C26c)
READS = [
    {"id": "GJW-2", "source": "P. Gao, D. L. Jafferis, A. C. Wall, 'Traversable Wormholes via a Double Trace "
     "Deformation', arXiv:1608.05687v3", "page": "PDF p.2 (printed 2)", "status": "READ",
     "quote": "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes "
              "[37, 50, 51, 23]. It states that there must be infinite null geodesics passing through the wormhole, "
              "with tangent vector k^mu and affine parameter lambda, along which int_-inf^+inf T_munu k^mu k^nu "
              "dlambda < 0. (1.1)",
     "fragment": "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes",
     "fragment_file": "spec",
     "bearing": "beside the demand, never a supply: GJW's prerequisite is ANEC < 0 for the TOTAL stress along null "
     "geodesics through the wormhole; Lemma S's pair sums to 0 along each crossed generator, which in GJW's linearised "
     "analysis (GJW-3b, GJW-4b) is the cancelling, non-traversable case -- a tension, OPEN (stationary_demand)"},
    {"id": "GJW-3", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.3 (printed 3), after eq. (1.2)",
     "status": "READ",
     "quote": "This connects the boundaries with the same time orientation, since the t coordinate runs in opposite "
              "directions in two wedges (see Fig. 1.1a).",
     "fragment": "This connects the boundaries with the same time orientation", "fragment_file": "spec",
     "bearing": "their coupling joins the two boundaries of the thermofield double, whose Killing time is opposite in "
     "the two wedges -- the hyperbolic case of Lemma P (iii)"},
    {"id": "GJW-3b", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.3 (printed 3), before eq. (1.3)",
     "status": "READ",
     "quote": "The eternal black hole has a Killing symmetry which is time-like outside the horizon. Null rays along "
              "the horizon V = 0 pass through the bifurcation surface of the Killing vector, and asymptote to "
              "t -> -infinity on the left boundary and t -> +infinity on the right boundary (see Fig. 1.1b). Denote "
              "the affine parameter along this ray as U. In the linearized analysis around this solution, the throat "
              "will become marginally traversable if int dU T_UU < 0, where the integral is over the whole U "
              "coordinate.",
     "fragment": "the throat will become marginally traversable if", "fragment_file": "fix-round",
     "bearing": "GJW's criterion is the integral of the TOTAL T_UU over a whole horizon generator, about a bifurcate "
     "(non-degenerate) horizon, linearised: the corridor's horizon is degenerate, so carrying it over is OPEN"},
    {"id": "GJW-4", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.4 (printed 4)",
     "status": "READ",
     "quote": "In fact, |tfd> is invariant under H_R - H_L, which corresponds to the bulk Killing symmetry i d_t (note "
              "the directions are opposite in left and right wedges).",
     "fragment": "(note the directions are opposite in left and right wedges)", "fragment_file": "spec",
     "bearing": "the TFD's generator flips between the sides; Lemma P (iii) computes that the parabolic generators do "
     "not"},
    {"id": "GJW-4b", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.4 (printed 4), after eq. (1.6)",
     "status": "READ",
     "quote": "In other words, T_UU in the modified state along U > 0 will exactly cancel that along U < 0. Beyond the "
              "linearized level, one can show that the backreaction always causes the throat to lengthen [33, 44], so "
              "that it cannot be traversed in any state of the decoupled system, as expected.",
     "fragment": "T_UU in the modified state along U > 0 will exactly cancel that along U < 0",
     "fragment_file": "fix-round",
     "bearing": "a zero total along the horizon generator is GJW's non-traversable (decoupled) case; set beside Lemma "
     "S's zero pair total under 183, OPEN"},
    {"id": "GJW-4fn2", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.4 (printed 4), footnote 2",
     "status": "READ",
     "quote": "We do not consider the case of a time-independent interaction, in order to prevent the quantum state "
              "from becoming non-regular on the past horizon.",
     "fragment": "We do not consider the case of a time-independent interaction, in order to prevent the quantum state "
                 "from becoming non-regular on the past horizon.", "fragment_file": "spec",
     "bearing": "beside the STATIONARY demand: their construction avoids a time-independent coupling; the stationary "
     "partner Lemma S demands is not their case (OPEN)"},
    {"id": "GJW-13fn8", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.13 (printed 13), footnote 8",
     "status": "READ",
     "quote": "Presumably there is some limit on how much information can get through, since the black hole on the "
              "other side cannot radiate more energy than its initial mass, but determining the precise limit would "
              "require going beyond the linearized regime.",
     "fragment": "Presumably there is some limit on how much information can get through", "fragment_file": "spec",
     "bearing": "a limit named, not computed: never a number of bits"},
    {"id": "MSY-13", "source": "J. Maldacena, D. Stanford, Z. Yang, 'Diving into traversable wormholes', "
     "arXiv:1704.05333v1", "page": "PDF p.13 (printed 12), sec. 2.5", "status": "READ",
     "quote": "In this section we point out that the backreaction effect in the last section is enough to ensure that "
              "we cannot send more information through the wormhole than we transferred in order to set up the OO "
              "interaction and open the wormhole in the first place. We will not provide sharp bounds, only parametric "
              "bounds.",
     "fragment": "we cannot send more information through the wormhole than we transferred in order to set up the OO "
                 "interaction", "fragment_file": "spec",
     "bearing": "set against 122 (4) (H-RULES-NOT-INFORMATION): reported, not decided; a one-sided parametric bound, "
     "never a supply"},
    {"id": "MSY-14", "source": "Maldacena-Stanford-Yang, arXiv:1704.05333v1", "page": "PDF p.14 (printed 13), eq. (2.25)",
     "status": "READ",
     "quote": "N_send ~ p_+^total / p_+^each <= g, (2.25) ... This is good because it is less than our estimate (2.21) "
              "of the number of bits or qubits necessary to open the wormhole.",
     "fragment": "eq. (2.25)", "fragment_file": "spec",
     "bearing": "the parametric form of MSY-13 (their eq. (2.21): g <~ N_bits)"},
    {"id": "MQ-3", "source": "J. Maldacena, X.-L. Qi, 'Eternal traversable wormhole', arXiv:1804.00491v3",
     "page": "PDF p.3 (printed 2)", "status": "READ",
     "quote": "Furthermore, AdS2, viewed as a global spacetime, has two boundaries that are causally connected. We can "
              "send a signal from one boundary to the other.",
     "fragment": "AdS2, viewed as a global spacetime, has two boundaries that are causally connected.",
     "fragment_file": "spec", "bearing": "the elliptic (global) member is two-way"},
    {"id": "MQ-5", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.5 (printed 4), eqs. (2.1)-(2.2)",
     "status": "READ", "page_departure": {"design_stage": "PDF p.6", "reopened": "PDF p.5"},
     "quote": "ds^2 = (-dt^2 + dsigma^2)/sin^2 sigma, sigma in [0, pi] (2.1) ... the above coordinate systems manifest "
              "only one of them, a different generator for each of the coordinate systems. ... We can also describe "
              "AdS2 in terms of global coordinates Y^M with the constraint -(Y^-1)^2 - (Y^0)^2 + (Y^1)^2 = -1 (or, "
              "more precisely, its universal cover).",
     "fragment": "a different generator for each of the coordinate systems", "fragment_file": "spec",
     "bearing": "the global metric (2.1) and the hyperboloid constraint; MQ do not print the parametrisation Y(T, "
     "sigma) used here (standard-not-READ), whose induced metric C30a computes equal to (2.1)"},
    {"id": "MQ-7", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.7 (printed 6)", "status": "READ",
     "quote": "For this solution, the two boundary trajectories correspond to lines of constant rho in the "
              "Rindler/Thermal coordinates (2.2), and we cannot send signals between the boundaries.",
     "fragment": "we cannot send signals between the boundaries", "fragment_file": "ground",
     "bearing": "the hyperbolic (thermal) member: no passage"},
    {"id": "MQ-7b", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.7 (printed 6)", "status": "READ",
     "quote": "In this paper we are interested in creating a situation where the boundaries correspond to lines of "
              "constant sigma in the global coordinates (2.1). In this configuration we would have a t-translation "
              "invariant dilaton which grows towards both boundaries.",
     "fragment": "the boundaries correspond to lines of constant sigma in the global coordinates (2.1)",
     "fragment_file": "fix-round",
     "bearing": "MQ's coupled wormhole has the global time isometry d_T: the elliptic member"},
    {"id": "MQ-53", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.53 (printed 52), Fig. 23 and text",
     "status": "READ",
     "quote": "Figure 23: This is a sketch of an idea for producing solutions with non-trivial topology. ... The throat "
              "is supported by negative null energy (energy that contributes negatively to the integrated null "
              "energy) produced by quantum effects. ... If the resulting operator of the form (2.11) has positive "
              "sign, then we expect that a traversable wormhole, of the kind discussed here, will form. The full "
              "geometry will not contain a horizon, but will have non-trivial topology in the ambient space.",
     "fragment": "The full geometry will not contain a horizon", "fragment_file": "spec",
     "bearing": "MQ's expectation ('we expect'), in 'a sketch of an idea' (Fig. 23) of a 4D ambient set-up of two "
     "near-extremal black holes: set beside the demand (against 132, 143 A), never a supply, and not used for the 2D "
     "elliptic member"},
    {"id": "MQ-64", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.64 (printed 63), after (B.171)",
     "status": "READ",
     "quote": "at t = 0, the operator H_R - H_L can be identified with (q_+ + q_-)/2 which turns out to be the boost "
              "generator around the origin in AdS2. ... By origin we mean t = 0, sigma = pi/2 in the coordinates in "
              "(2.1).",
     "fragment": "the boost generator around the origin in AdS2", "fragment_file": "spec",
     "bearing": "the TFD's generator is the boost about the origin (the point generator_classes' B_origin fixes)"},
]
READS_NOTE = ("Page evidence: the PDFs were re-opened through alphaXiv on 2026-10-09 by the in-project REFUTE and "
              "OVERCLAIM readings (all READs then held) and, for GJW-2's extension, GJW-3b, GJW-4b, MQ-5's constraint, "
              "MQ-7b and MQ-53's hedge, by this fix round.  C26c checks transcriptions against the design-stage files "
              "(consistency between transcriptions, not a re-reading); fix-round READs have one transcription.")


def _read(rid, reads=None):
    return next(r for r in (READS if reads is None else reads) if r["id"] == rid)


def _ground_rows():
    with open(GROUND) as fh:
        d = json.load(fh)
    rows = d.get("literature", {}).get("reads", []) if isinstance(d, dict) else []
    return [_norm("%s :: %s" % (r.get("page", ""), r.get("quote", ""))) for r in rows if isinstance(r, dict)]


def _spec_lines():
    with open(SPEC) as fh:
        t = fh.read()
    i, j = t.find("## 10. READs"), t.find("## 11.")
    return [_norm(ln) for ln in t[i:j].split("\n") if ln.strip()]


def _pdf_pages(s):
    out = set()
    for a, b in re.findall(r"PDF pp?\.\s*(\d+)(?:\s*[–-]\s*(\d+))?", s):
        out |= set(range(int(a), int(b or a) + 1))
    return out


def reads_found(reads=None):
    """C26c's computation (transcription consistency).  For each READ: the fragment verbatim in this run's quote and,
    for a design-stage READ, in the line of its design-stage file (spec section 10 or epass_ground.json) that carries
    it; the READ's PDF page equal to that line's page, or a recorded page departure naming it.  'eq. (2.25)' is a
    pointer fragment: the quote must carry '(2.25)'.  Label: computed."""
    reads = READS if reads is None else reads
    files = {"spec": _spec_lines(), "ground": _ground_rows()}
    res = {}
    for r in reads:
        frag = _norm(r["fragment"])
        in_quote = (frag in _norm(r["quote"])) if not frag.startswith("eq. ") else (frag[4:] in r["quote"])
        pg = _pdf_pages(r.get("page", ""))
        page = min(pg) if pg else None
        row = {"in_quote": in_quote, "page": page, "transcriptions": 1}
        if r["fragment_file"] in files:
            lines = [ln for ln in files[r["fragment_file"]] if frag in ln]
            design = set().union(*[_pdf_pages(ln) for ln in lines]) if lines else set()
            dep = r.get("page_departure")
            dep_ok = bool(dep and min(_pdf_pages(dep["design_stage"]) or {0}) in design
                          and min(_pdf_pages(dep["reopened"]) or {0}) == page)
            row.update({"in_design_file": bool(lines), "design_pages": sorted(design), "transcriptions": 2,
                        "page_agrees": bool(page in design or dep_ok), "departure": bool(dep_ok)})
            row["ok"] = bool(in_quote and lines and row["page_agrees"])
        else:
            row["ok"] = bool(in_quote and page)
        res[r["id"]] = row
    return res


# ======================================================================================== X17 the demands
M_SYM = sp.Symbol("m", positive=True)
_DATA = {"eq17": lambda r: SF.B4._eq17(r), "schwarzschild": lambda r: SF.B4._schwarzschild(r)}


def _surface_gravity(F, H, r, r_h):
    """kappa of xi = d_t for -F dt^2 + dr^2/H at the root r_h of F: kappa^2 = -(1/2) nabla_a xi_b nabla^a xi^b =
    F'^2 H/(4F), taken as r -> r_h from outside."""
    k2 = sp.limit(sp.diff(F, r)**2 * H / (4 * F), r, r_h, "+")
    return sp.sqrt(sp.simplify(k2))


@functools.lru_cache(maxsize=None)
def readme_flux_P1(area_power=2, data_key="eq17"):
    """kappa4^2 int T_vv dv per generator on P1 (sympy, exact).  r_h from eq. (17)'s F (owner b4_static via
    sim2_facing.B4._eq17), restored to units of m; the surface gravity kappa of that horizon (the Schwarzschild control
    computed beside it); the area integral of r_h^area_power sin(theta) over the S^2; W1 (STRUCTURAL): kappa4^2 E =
    8 pi G M/c^4 = 8 pi m.  area_power = 1 is the spec's mutation r^2 -> r; data_key = 'schwarzschild' puts the other
    owner's data in eq. (17)'s place (a mutation: kappa != 0, v not affine).
    Label: computed; STRUCTURAL (W1).  Tag: [PLANE]-conditional."""
    r, th, ph = sp.symbols("r theta phi", positive=True)
    F, H = _DATA[data_key](r)
    roots = sp.solve(sp.Eq(F, 0), r)
    kap = _surface_gravity(F, H, r, roots[0])
    Fs, Hs = SF.B4._schwarzschild(r)
    kap_s = _surface_gravity(Fs, Hs, r, sp.solve(sp.Eq(Fs, 0), r)[0])
    r_h = roots[0] * M_SYM
    area = sp.integrate(sp.integrate(r_h**area_power * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
    val = sp.simplify(8 * sp.pi * M_SYM / area)
    return {"value": val, "r_h_over_m": roots[0], "kappa_x_m": kap,
            "kappa_x_m_schwarzschild_control": kap_s, "data": data_key,
            "area": sp.simplify(area), "equals_one_over_2m": bool(sp.simplify(val - 1 / (2 * M_SYM)) == 0),
            "dlog_dlogm": sp.simplify(M_SYM * sp.diff(val, M_SYM) / val)}


LEMMA_S_POINTER = ("lemmas/EPASS-DESIGN-SPEC.md X13 (Lemma S: R(xi,xi) = 0 on any Killing horizon; K(xi,xi) = 0 on "
                   "every sheet tangent to xi); axioms.py Z3 re-read under 183")


@functools.lru_cache(maxsize=None)
def lemma_s_owner(cases=("degenerate", "non-degenerate"), mutate=False):
    """Lemma S from lemmas/epass_pairing.py (by path): for each case, its bulk form R(xi,xi)|_H and kappa5^2 T5(xi,xi)|_H
    (pairing_bulk on bulk_gvv(case)) and its sheet form S(xi,xi)/nu|_H (pairing_sheet on sheet_gvv(case)).  mutate =
    True passes each g_vv through the owner's own non_stationary() (C26e's mutation).  Any failure falls back to a
    pointer.  Label: computed (by the owner, not re-derived here)."""
    out = {"owner": "lemmas/epass_pairing.py", "present": os.path.exists(PAIRING), "pointer": LEMMA_S_POINTER,
           "cases": list(cases), "mutated_non_stationary": bool(mutate)}
    if not out["present"]:
        out.update({"imported": False, "owner_says_zero": False,
                    "label": "OPEN (pointer only: the owner file is absent)"})
        return out
    try:
        P = _owner("pairing")
        rows, zero = {}, True
        for kind in cases:
            gb, ub = P.bulk_gvv(kind)
            gs, us = P.sheet_gvv(kind)
            if mutate:
                gb, gs = P.non_stationary(gb), P.non_stationary(gs)
            b = P.pairing_bulk(gb, ub)
            s = P.pairing_sheet(gs, us)
            vals = (b["R_xixi"], b["kappa2_T5_xixi"], s["S_xixi_over_nu"])
            z = all(sp.sympify(x) == 0 for x in vals)
            zero = zero and z
            rows[kind] = {"bulk_R_xixi_on_H": _short(b["R_xixi"]), "bulk_R_xixi_witness": b["R_xixi_witness"],
                          "bulk_kappa5sq_T5_xixi_on_H": _short(b["kappa2_T5_xixi"]),
                          "bulk_kappa5sq_T5_xixi_witness": b["kappa2_T5_xixi_witness"],
                          "sheet_S_xixi_over_nu_on_H": _short(s["S_xixi_over_nu"]),
                          "sheet_S_xixi_over_nu_witness": s["S_xixi_over_nu_witness"], "all_zero": z}
        out.update({"imported": True, "rows": rows, "owner_says_zero": bool(zero),
                    "label": "computed (by the owner epass_pairing.py, imported by path; not re-derived here)"})
    except Exception as ex:   # the owner is under construction: the demand falls back to the pointer
        out.update({"imported": False, "owner_says_zero": False, "load_error": repr(ex)[:300],
                    "label": "OPEN (pointer only: the owner could not be called)"})
    return out


def _gated(ls):
    return bool(ls.get("imported") and ls.get("owner_says_zero"))


STATIONARY_READING = ("on H-STATIONARY-CROSSING (the board's, spec 4.3: the corridor is stationary while the README "
                      "crosses; refused, it becomes E-NS)")


def stationary_demand(area_power=2, ls=None):
    """The stationary demand of Lemma S, in its two forms (bulk primary under 179/180; sheet on whichever sheet carries
    the README, 172 (1)), gated on the owner's computed zeros; P1's number as a [PLANE]-conditional reference.  The
    pair's net is the owner's zero and is never called positive.
    Label: deduced (Lemma S, the owner's zeros); computed (P1's number); else OPEN (pointer only)."""
    ls = lemma_s_owner() if ls is None else ls
    gated = _gated(ls)
    fR = readme_flux_P1(area_power)["value"]
    if gated:
        lab = "deduced (from Lemma S: the owner's computed zeros, bulk and sheet; %s)" % STATIONARY_READING
        net = ls["rows"][ls["cases"][0]]["sheet_S_xixi_over_nu_on_H"]
        fc = str(-fR)                  # T^c = -T^R - T^m with T^m(xi,xi)|_H = 0 (the premise below)
    else:
        lab = "OPEN (pointer only: Lemma S's owner not imported or not zero; %s)" % LEMMA_S_POINTER
        net, fc = "OPEN", "OPEN"
    return {
        "lemma_s": ls,
        "gated_on_owner_zero": gated,
        "bulk_form": {"tag": "[FREE]; primary under 179/180", "label": lab + "; OPEN (its 5D normalisation)",
                      "statement": "R(xi,xi)|_H = 0 on a stationary (Killing) horizon uses no field equation (the "
                                   "owner computes it on the general stationary bulk, degenerate and non-degenerate). "
                                   "With the 5D Einstein equation and Lambda_5 (Lambda_5 g(xi,xi) = 0 on H) it gives "
                                   "T5(xi,xi)|_H = 0, so T5^c(xi,xi) = -T5^R(xi,xi) - T5^m(xi,xi) along every "
                                   "generator, = -T5^R(xi,xi) on the matter premise.  Independent of the planes' "
                                   "stress law and tension; it needs the 5D Einstein equation.",
                      "normalisation": "OPEN: the README's 5D flux per bulk generator needs the bulk horizon's "
                                       "section, which is the bulk balance's (181); not computed here"},
        "sheet_form": {"tag": "[FREE] form; P1's number [PLANE]-conditional",
                       "label": lab + ("; computed (P1's number)" if gated else ""),
                       "statement": "Israel on the README's own sheet: K(xi,xi) = 0 on a stationary horizon gives "
                                    "S(xi,xi) = 0 (the owner computes it on the throat sheet, degenerate and "
                                    "non-degenerate), so S^c(xi,xi) = -S^R(xi,xi) - S^m(xi,xi), = -S^R(xi,xi) on the "
                                    "matter premise.  Independent of the sheet's stress law and tension; it needs "
                                    "Israel's junction condition.",
                       "readme_sheet": "Under H-README-ON-P2 (M's, 172 (1)) the README's sheet is position 2's piece; "
                                       "the demand in that sheet's own normalisation is not computed here (OPEN).",
                       "P1_reference": "P1's figure, a normalisation reference only ([PLANE]-conditional: eq. (17) "
                                       "as P1's metric, H-PLANE-READS-MOUTH, the board's; under 184 a vacuum-plane "
                                       "limit): kappa4^2 int T^R_vv dv = %s and kappa4^2 int T^c_vv dv = %s per "
                                       "generator" % (fR, fc),
                       "readme_kappa4sq_int_Tvv_P1": str(fR), "partner_kappa4sq_int_Tvv_P1": fc},
        "matter_premise": {"label": "deduced (spec X13 (a)); OPEN (for matter flowing across the horizon)",
                           "text": "With matter on both planes (184), Lemma S gives T^c(xi,xi) = -T^R(xi,xi) - "
                                   "T^m(xi,xi) on the horizon.  The demand 'partner = -README' takes T^m(xi,xi)|_H = 0 "
                                   "as a premise: it holds for the planes' own matter held static across the horizon "
                                   "(a held static stress has T(xi,xi) = 0 there, spec X13 (a)) and fails for matter "
                                   "flowing across it."},
        "pair_net_per_generator": net,
        "pair_net_reading": ("zero (the owner's): neither positive nor negative (spec pitfall 13; 139 (2)'s 'positive' "
                             "is not met by a pair total)") if gated else "OPEN (pointer only)",
        "under_183": {"label": "deduced; OPEN",
                      "text": "M chose 'Yes: never violated as a pair'; H-NEC-NEVER-VIOLATED-AS-PAIR (carried as M's; "
                              "clause (Z), seated on M's 'Seat both', 187 (3)) admits the exact +/- null pair through "
                              "H-PARTNER-IS-THE-COUPLING (the board's): the stationary crossing is OPEN -- the demand "
                              "is exact, the supply beyond the board's instruments -- and NOT refuted.  This module's "
                              "rows are not seated."},
        "gjw_beside_183": {"label": "READ (GJW PDF pp.2-4); deduced; OPEN",
                           "text": "GJW's prerequisite is ANEC violation by the TOTAL stress along null geodesics "
                                   "through the wormhole (GJW-2, PDF p.2); in their linearised analysis about a "
                                   "bifurcate horizon the throat becomes marginally traversable if the integral of "
                                   "T_UU over the whole horizon generator is negative (GJW-3b, PDF p.3), and where "
                                   "T_UU along U > 0 exactly cancels that along U < 0 it cannot be traversed (GJW-4b, "
                                   "PDF p.4).  Lemma S's pair sums to 0 along each crossed generator (the owner's "
                                   "zero): in GJW's terms the cancelling case, not the strict violation they call a "
                                   "prerequisite.  A tension, reported beside 183, not a refutation: GJW's hypotheses "
                                   "(a bifurcate, non-degenerate horizon; linearised backreaction) are not the "
                                   "corridor's degenerate horizon and are not checked here, and whether the README's "
                                   "own escaping null geodesics carry ANEC < 0 is OPEN."},
        "under_184": {"label": "deduced",
                      "text": "Lemma S is independent of the planes' stress law and tension, given the 5D Einstein "
                              "equation (bulk form) and Israel's junction condition (sheet form); it holds with matter "
                              "on both planes, on the matter premise above.  Matter-free results (P1 as a vacuum "
                              "plane; eq. (17)'s Weyl fluid) are limits only."},
        "label": (lab + "; computed (P1's number, [PLANE]-conditional)") if gated else lab,
    }


@functools.lru_cache(maxsize=None)
def g_exponent_of_E(dims=(1, 2, -2)):
    """The exponent of G in an energy built from hbar, c and G alone (dimensional analysis, sympy).  dims are the
    target's (kg, m, s) exponents: (1, 2, -2) is a joule; (1, 3, -2) (J m) is C26d's mutation.  Generic: it does not
    read exactE; C26d compares it with the owner's own form.  Label: deduced."""
    a, b, g = sp.symbols("a b g")
    hb, cc, GG = (1, 2, -1), (0, 1, -1), (-1, 3, -2)
    eqs = [sp.Eq(a * hb[i] + b * cc[i] + g * GG[i], dims[i]) for i in range(3)]
    s = sp.solve(eqs, [a, b, g], dict=True)[0]
    return {"hbar": s[a], "c": s[b], "G": s[g]}


# ------------------------------------------------------------------------------------------------ exactE, by path
_E = {}


def _owner_table(mod):
    """An owner's own path table, read from its owners() source: {name: the args its _load takes}."""
    src = inspect.getsource(mod.owners)
    out = {}
    pat = r'_CACHE\["(\w+)"\]\s*=\s*_load\(((?:"\w+",\s*)?)os\.path\.join\((\w+),\s*((?:"[^"]+"\s*,?\s*)+)\),\s*"(\w+)"\)'
    for name, has_name, base, parts, key in re.findall(pat, src):
        path = os.path.join(getattr(mod, base), *re.findall(r'"([^"]+)"', parts))
        out[name] = (name, path, key) if has_name else (path, key)
    return out


def _seed(mod, func):
    """Seed mod's owner cache with only the owners func's own source reads (owners()["x"] or o["x"]), each loaded by
    mod's own _load at mod's own path and key."""
    need = set(re.findall(r'(?:owners\(\)|\bo)\["(\w+)"\]', inspect.getsource(func)))
    table = _owner_table(mod)
    if not need or not need <= set(table):
        raise LookupError("owners %s not all in %s's table %s" % (sorted(need), mod.__name__, sorted(table)))
    mod._CACHE.clear()
    for n in sorted(need):
        mod._CACHE[n] = mod._load(*table[n])
    return sorted(need)


def _e_job(full=False):
    """exactE.e_per_sqrt_bit() and chain's coefficient record; then the owner's computation re-run at G(1 +- 1e-6)
    (chain's seat.G scaled and restored) to measure E's G-exponent on the owner's own path."""
    ex = _owner("exactE")
    t0 = time.time()
    route = "full: exactE.owners() and chain.owners()"
    ex._CACHE.clear()
    if not full:
        try:
            a = _seed(ex, ex.e_per_sqrt_bit)
            ch = ex.owners()["chain"]
            b = _seed(ch, ch.coefficients)
            route = "seeded: exactE owners %s, chain owners %s (cmb/cmbframe.py not loaded)" % (a, b)
        except Exception as e:
            ex._CACHE.clear()
            route += " (seeding failed: %r)" % e
    try:
        v = ex.e_per_sqrt_bit()
    except Exception:
        if full:
            raise
        return _e_job(full=True)
    ch = ex.owners()["chain"]
    co = ch.coefficients()["E_min_J_per_sqrt_bit"]
    g_meas, eps = None, 1e-6
    try:
        seat = ch.owners()["uses"].owners()[0]
        G0, vals = seat.G, {}
        try:
            for s in (1, -1):
                seat.G = G0 * (1 + s * eps)
                vals[s] = ex.e_per_sqrt_bit()
        finally:
            seat.G = G0
        g_meas = math.log(vals[1] / vals[-1]) / math.log((1 + eps) / (1 - eps))
        restored = ex.e_per_sqrt_bit() == v
    except Exception as e:
        restored = "not measured: %r" % e
    return {"e_per_sqrt_bit_J": v, "u_r_E_banked": co["u_r"], "U_R_G_banked": ex.U_R_G, "form": co["form"],
            "H_SI": str(ex.H_SI), "C_SI": str(ex.C_SI), "G_SI": str(ex.G_SI), "g_measured": g_meas,
            "g_measured_how": "the owner's computation at G(1 +- 1e-6): ln(E+/E-)/ln((1+eps)/(1-eps))",
            "restored_after_measurement": restored, "owner_route": route, "owner_s": round(time.time() - t0, 1)}


def start_e_background(full=False):
    """With the seeded owner route (about 1 s) nothing is forked.  full = True (--full-owner) runs the full owner load
    (70-100 s, cmb/cmbframe.py) in a forked child while the other checks run."""
    if not full or "res" in _E or "async" in _E:
        _E.setdefault("full", full)
        return
    import multiprocessing as mpc
    try:
        _E["t0"], _E["full"] = time.time(), True
        pool = mpc.get_context("fork").Pool(1)
        _E["async"], _E["pool"] = pool.apply_async(_e_job, (True,)), pool
    except Exception:
        pass


def e_owner_values():
    if "res" not in _E:
        if "async" in _E:
            _E["res"] = _E["async"].get(timeout=900)
            _E["pool"].close()
            _E["res"]["arrived_after_s"] = round(time.time() - _E["t0"], 1)
        else:
            _E["res"] = _e_job(full=_E.get("full", False))
    return _E["res"]


def e_form_exponent(form_g_power=1, eo=None):
    """E's G-exponent read from the owner's own form (chain.py coefficients()['E_min_J_per_sqrt_bit']['form'], parsed
    with sympy), and that form evaluated at exactE's constants with N = 1 against the owner's value.  form_g_power = 2
    puts G^2 for G inside the form (C26d's mutation).  Label: computed."""
    eo = e_owner_values() if eo is None else eo
    syms = {k: sp.Symbol(k, positive=True) for k in ("N", "h", "c", "G")}
    txt = eo["form"].split("=", 1)[1].replace("^", "**").replace("ln2", "log(2)")
    expr = parse_expr(txt, local_dict={**syms, "pi": sp.pi, "log": sp.log, "sqrt": sp.sqrt},
                      transformations=standard_transformations + (implicit_multiplication_application,))
    G = syms["G"]
    expr = expr.subs(G, G**form_g_power)
    g = sp.nsimplify(sp.simplify(G * sp.diff(sp.log(expr), G)))
    val = expr.subs({syms["N"]: 1, syms["h"]: sp.Rational(eo["H_SI"]), syms["c"]: sp.Rational(eo["C_SI"]),
                     G: sp.Rational(eo["G_SI"])})
    valf = float(sp.N(val, 30))
    return {"form": eo["form"], "G_exponent": g, "value_at_owner_constants_J": valf,
            "rel_dev_from_owner_value": abs(valf / eo["e_per_sqrt_bit_J"] - 1)}


def demand_si(e_sqrt=None, area_power=2, c_power=4, form_g_power=1):
    """The demand in SI at o3_write.EXAMPLE_N and at item 155's E, with G's uncertainty propagated through E's
    G-exponent read from the owner's form (C26d checks it against the owner's computation).  e_sqrt may be passed (J
    per sqrt(bit)); the exponent then comes from dimensional analysis, labelled so.  c_power = 2 (m = G E/c^2) and
    form_g_power = 2 are mutations.  Label: computed; standard-not-READ (u(G)); STRUCTURAL (W1)."""
    O = _owner("o3_write")
    G, c, N = O.G_SI, O.C_SI, O.EXAMPLE_N
    if e_sqrt is None:
        eo = e_owner_values()
        ef = e_form_exponent(form_g_power, eo)
        gE, src = ef["G_exponent"], "the owner's own form, G d ln E/dG (C26d: equal to the owner's computation)"
    else:
        eo, ef = {"e_per_sqrt_bit_J": e_sqrt}, None
        gE, src = g_exponent_of_E()["G"], "dimensional analysis (e_sqrt passed; the owner's form not read)"
    flux = readme_flux_P1(area_power)
    f, k_m = flux["value"], flux["dlog_dlogm"]
    u_G = G_U_CODATA / G
    rows = {}
    for key, E, gexp in (("N_example", eo["e_per_sqrt_bit_J"] * math.sqrt(N), gE), ("item155", E_ITEM155, 0)):
        mv = G * E / c**c_power
        inv = float(f.subs(M_SYM, mv)) if f.has(M_SYM) else float(f)
        u_m = float(abs(1 + gexp)) * u_G               # m = G E / c^4 with E ~ G^gexp: m ~ G^(1 + gexp)
        rows[key] = {"E_J": E, "m_geometric_m": mv, "kappa4sq_int_Tvv_per_m": inv,
                     "u_r_m": u_m, "u_r_kappa4sq_int_Tvv": abs(float(k_m)) * u_m,
                     "G_exponent_of_m": str(1 + gexp)}
    return {"rows": rows, "G_SI": G, "c_SI": c, "N": N, "u_r_G_CODATA": u_G,
            "u_r_G_banked_exactE": eo.get("U_R_G_banked"), "u_r_E_banked_chain": eo.get("u_r_E_banked"),
            "E_form": eo.get("form"), "G_exponent_of_E": str(gE), "G_exponent_source": src,
            "owner_route": eo.get("owner_route"),
            "tag": "E and m columns [FREE] (W1, STRUCTURAL; exactE); the kappa4sq_int_Tvv column is P1's number, "
                   "[PLANE]-conditional (eq. (17) as P1's metric; under 184 a vacuum-plane limit)",
            "label": "computed; standard-not-READ (CODATA 2018 uncertainty of G); STRUCTURAL (W1)",
            "note": "G and c as banked in o3_write (our universe's G); whether each universe, or a corridor's region of "
                    "the bulk, has its own G, M left 'For the math' (187 (2)): OPEN, and these rows hold at our G"}


def reads_beside():
    """The READs set beside the demands, never a supply, and MSY's bound against 122 (4)'s words.  Label: READ;
    deduced; OPEN."""
    return {"reads": READS, "note": READS_NOTE,
            "msy_vs_122_4": {"label": "deduced; OPEN (reported, not decided)",
                             "M_122_4": M_WORDS["122 (4)"],
                             "MSY": _read("MSY-13")["quote"],
                             "text": "MSY bound, parametrically and from above, the information sent through a coupled "
                                     "wormhole by the information transferred to set up the coupling (their (2.21), "
                                     "(2.25); 'only parametric bounds').  M's 122 (4) (H-RULES-NOT-INFORMATION) reads "
                                     "'The rules apply, but do not restrict information'.  If MSY's bound governs the "
                                     "coupling 177 admits, the coupling lets through at most (parametrically) the "
                                     "information exchanged to set it up; if 122 (4) exempts the README, it does not "
                                     "bind.  Not decided here; no number of bits is printed as a supply."},
            "label": "READ (alphaXiv full text, PDF page with printed page)"}


def answer_158_4(ls=None):
    """158 (4): where the README's energy goes.  Label: deduced; OPEN."""
    ls = lemma_s_owner() if ls is None else ls
    return {"M_158_4": M_WORDS["158 (4)"],
            "question": "(4) whether the README's energy stays on the plane or is carried into the extra dimension "
                        "(the board's question, 158)",
            "stationary": {"label": ("deduced (Lemma S, the owner's zeros)" if _gated(ls)
                                     else "OPEN (pointer only: Lemma S's owner not imported or not zero)"),
                           "reading": STATIONARY_READING, "tag": "[FREE]",
                           "text": "nothing net is absorbed: the README's positive null flux and its partner's equal "
                                   "negative flux cancel along every crossed generator (with the matter premise); "
                                   "under 183 that is 'never violated' as a pair"},
            "changing": {"label": "deduced; OPEN (Lemma L, [PLANE], not built here)",
                         "text": "into the bulk's Weyl field and the creased bulk horizon (Lemmas L and K): a necessary "
                                 "condition only"},
            "label": "deduced; OPEN"}


# ======================================================================================== X18 frames
ETA = sp.diag(-1, -1, 1)                                       # (Y^-1, Y^0, Y^1)
T_, S_ = sp.symbols("T sigma", real=True)


def so21_generators(k_coeff=1):
    """J = d_T (rotation in Y^-1, Y^0); B_origin, the boost about the origin (Y^0 <-> Y^1; fixes Y = (1,0,0), i.e.
    T = 0, sigma = pi/2); K, the other boost (Y^-1 <-> Y^1); J +- k K; J - k B_origin (the Poincare d_t).  k_coeff = 2
    is C30a's and C31d's mutation."""
    J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    B = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    K = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    return {"J": J, "B_origin": B, "K": K, "J+K": J + k_coeff * K, "J-K": J - k_coeff * K,
            "J-B_origin": J - k_coeff * B}


def matrix_class(M):
    """so(2,1) class from the matrix alone: in the algebra?, eigenvalues, nilpotency."""
    in_alg = (M.T * ETA + ETA * M) == sp.zeros(3)
    ev = [sp.nsimplify(e) for e in M.eigenvals(multiple=True)]
    M2, M3 = M * M, M * M * M
    nz = [e for e in ev if e != 0]
    if M == sp.zeros(3):
        cls = "zero"
    elif M3 == sp.zeros(3) and M2 != sp.zeros(3):
        cls = "parabolic"
    elif nz and all(sp.re(e) == 0 and sp.im(e) != 0 for e in nz):
        cls = "elliptic"
    elif nz and all(sp.im(e) == 0 for e in nz):
        cls = "hyperbolic"
    else:
        cls = "other"
    return {"in_so21": bool(in_alg), "eigenvalues": [str(e) for e in ev], "class": cls,
            "M3_zero": bool(M3 == sp.zeros(3)), "M2_zero": bool(M2 == sp.zeros(3)), "trM2": sp.simplify((M2).trace())}


def _christoffel(g, X):
    n = len(X)
    gi = g.inv()
    G = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                           for e in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    return gi, G


def killing_class(g, X, xi):
    """The class of a Killing field xi of a 2D metric g of constant negative curvature, from the invariant
    Q = (1/2) nabla_a xi_b nabla^a xi^b - xi.xi / L^2 (constant for a Killing field; R = -2/L^2): Q > 0 elliptic,
    Q = 0 parabolic, Q < 0 hyperbolic.  Verifies the Killing equation, constant curvature and constant Q."""
    n = 2
    gi, G = _christoffel(g, X)

    def ric(b, c):
        return sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                   + sum(G[a][a][e] * G[e][b][c] - G[a][c][e] * G[e][b][a] for e in range(n)) for a in range(n))
    Rs = sp.simplify(sum(gi[b, c] * ric(b, c) for b in range(n) for c in range(n)))
    xl = [sp.simplify(sum(g[a, b] * xi[b] for b in range(n))) for a in range(n)]
    nab = [[sp.diff(xl[b], X[a]) - sum(G[e][a][b] * xl[e] for e in range(n)) for b in range(n)] for a in range(n)]
    killing = all(sp.simplify(nab[a][b] + nab[b][a]) == 0 for a in range(n) for b in range(n))
    sq = sum(gi[a, c] * gi[b, d] * nab[a][b] * nab[c][d] for a in range(n) for b in range(n)
             for c in range(n) for d in range(n))
    xx = sum(xl[a] * xi[a] for a in range(n))
    L2 = -2 / Rs
    Q = sp.simplify(sq / 2 - xx / L2)
    const = all(sp.simplify(sp.diff(Q, x)) == 0 for x in X) and all(sp.simplify(sp.diff(Rs, x)) == 0 for x in X)
    sgn = sp.sign(Q) if Q.is_number else None
    cls = {1: "elliptic", 0: "parabolic", -1: "hyperbolic"}.get(int(sgn) if sgn is not None else 99, "undetermined")
    return {"R": Rs, "Q": Q, "killing": bool(killing), "constant": bool(const), "class": cls}


def _global_Y(scale=1):
    """The standard global parametrisation (standard-not-READ; MQ print (2.1) and the constraint only); scale = 2 is
    C30a's mutation (an AdS2 of radius 2, not MQ's (2.1))."""
    return scale * sp.Matrix([sp.cos(T_) / sp.sin(S_), sp.sin(T_) / sp.sin(S_), -sp.cos(S_) / sp.sin(S_)])


@functools.lru_cache(maxsize=None)
def induced_metric(scale=1):
    """The metric induced on the parametrisation by eta, against MQ (2.1) (READ PDF p.5): (-dT^2 + dsigma^2)/sin^2
    sigma; and the hyperboloid constraint Y.Y = -1.  Label: computed."""
    Y = _global_Y(scale)
    Jm = Y.jacobian([T_, S_])
    h = sp.simplify(Jm.T * ETA * Jm)
    hyper = sp.simplify((Y.T * ETA * Y)[0])
    return {"h": str(h.tolist()), "Y_dot_Y": str(hyper),
            "equals_MQ_2_1": bool(sp.simplify(h - sp.diag(-1, 1) / sp.sin(S_)**2) == sp.zeros(2)),
            "on_unit_hyperboloid": bool(sp.simplify(hyper + 1) == 0)}


@functools.lru_cache(maxsize=None)
def _gkf(Mkey, scale=1):
    M = sp.Matrix(3, 3, list(Mkey))
    Y = _global_Y(scale)
    Jm = Y.jacobian([T_, S_])
    h = sp.simplify(Jm.T * ETA * Jm)
    xi = sp.simplify(h.inv() * Jm.T * ETA * (M * Y))
    resid = sp.simplify(Jm * xi - M * Y)
    return xi.as_immutable(), h.as_immutable(), bool(resid == sp.zeros(3, 1))


def global_killing_field(M, scale=1):
    """The Killing field on global AdS2 (T, sigma) induced by M: xi = h^-1 J^T eta (M Y), J = dY/d(T, sigma), h the
    induced metric; returns xi, h and the tangency residual (J xi - M Y must vanish)."""
    xi, h, tangent = _gkf(tuple(M), scale)
    return sp.Matrix(xi), sp.Matrix(h), tangent


def boundary_components(xi):
    """xi^T at the two boundaries sigma -> 0+ and sigma -> pi-."""
    return (sp.simplify(sp.limit(xi[0], S_, 0, "+")), sp.simplify(sp.limit(xi[0], S_, sp.pi, "-")))


@functools.lru_cache(maxsize=None)
def generator_classes(k_coeff=1, scale=1):
    """X18's table: for each generator, the matrix class, the 2D Killing invariant's class (two routes; Q = -tr M^2/2
    checked), the boundary components, and the Killing norm xi.xi.  Label: computed.  Tag: [FREE]."""
    rows = {}
    for name, M in so21_generators(k_coeff).items():
        mc = matrix_class(M)
        xi, h, tangent = global_killing_field(M, scale)
        kc = killing_class(h, [T_, S_], list(xi))
        b0, bpi = boundary_components(xi)
        rows[name] = {"matrix": str(M.tolist()), "eigenvalues": mc["eigenvalues"], "in_so21": mc["in_so21"],
                      "class_matrix": mc["class"], "M3_zero": mc["M3_zero"], "M2_zero": mc["M2_zero"],
                      "class_killing_invariant": kc["class"], "Q": str(kc["Q"]),
                      "Q_equals_minus_half_trM2": bool(sp.simplify(kc["Q"] + mc["trM2"] / 2) == 0),
                      "killing_equation": kc["killing"], "tangent": tangent,
                      "xi_T": str(xi[0]), "xi_sigma": str(xi[1]), "xi_dot_xi": sp.simplify((xi.T * h * xi)[0]),
                      "component_at_sigma0": b0, "component_at_sigmapi": bpi}
    return rows


U_, V_ = sp.symbols("u v", real=True)
X_, Z_, TT_ = sp.symbols("x z t", positive=True)


@functools.lru_cache(maxsize=None)
def poincare_map(power=2):
    """x = 8/z^power in -(x/2)dt^2 + dx^2/x^2; power = 2 must give 4(-dt^2 + dz^2)/z^2 (Poincare, radius 2).
    power = 1 is a mutation.  Also z(u) from x = u^2 (u > 0).  Label: computed.  Tag: [FREE]."""
    xz = 8 / Z_**power
    g_tt = sp.simplify(-xz / 2)
    g_zz = sp.simplify(sp.diff(xz, Z_)**2 / xz**2)
    poincare = bool(sp.simplify(g_tt + 4 / Z_**2) == 0 and sp.simplify(g_zz - 4 / Z_**2) == 0)
    up = sp.Symbol("u", positive=True)
    zu = sp.solve(sp.Eq(8 / Z_**power, up**2), Z_)
    return {"g_tt": str(g_tt), "g_zz": str(g_zz), "is_poincare_radius2": poincare, "z_of_u": [str(s) for s in zu]}


@functools.lru_cache(maxsize=None)
def throat_generator(gvv=None):
    """The class of xi = d_v on the throat's 2D EF block g_vv dv^2 + 2 sqrt2 dv du (alpha = 1; sim2_passage X1's
    chart, from eq. (17) at r0 = 2m), from the Killing invariant.  Default g_vv = -u^2/2 (degenerate); C30b's mutation
    passes a non-degenerate g_vv = -(u^2 - 1/9)/2.  Label: computed.  Tag: [FREE given kappa = 0]."""
    gvv = -U_**2 / 2 if gvv is None else gvv
    g = sp.Matrix([[gvv, sp.sqrt(2)], [sp.sqrt(2), 0]])
    kc = killing_class(g, [V_, U_], [1, 0])
    return {"g_vv": str(gvv), "R": str(kc["R"]), "Q": str(kc["Q"]), "class": kc["class"], "killing": kc["killing"],
            "constant": kc["constant"]}


def _poincare_Y(t, z):
    return sp.Matrix([(1 - t**2 + z**2) / (2 * z), t / z, -(1 + t**2 - z**2) / (2 * z)])


@functools.lru_cache(maxsize=None)
def embedding_generator(field="d_t"):
    """A Poincare-chart Killing field as an so(2,1) matrix: solve M Y = X(Y) identically in (t, z), with the Poincare
    embedding Y = ((1 - t^2 + z^2)/(2z), t/z, -(1 + t^2 - z^2)/(2z)) (global sigma = 0 at z = 0: t +- z =
    tan((T +- sigma)/2)).  field = 'd_t' (the throat's d_v); 'dilatation' (t d_t + z d_z) is C30b's mutation.
    Label: computed.  Tag: [FREE]."""
    Y = _poincare_Y(TT_, Z_)
    hyper = sp.simplify(-Y[0]**2 - Y[1]**2 + Y[2]**2)
    target = sp.diff(Y, TT_) if field == "d_t" else TT_ * sp.diff(Y, TT_) + Z_ * sp.diff(Y, Z_)
    ms = sp.symbols("m0:9")
    M = sp.Matrix(3, 3, ms)
    eqs = []
    for comp in (M * Y - target):
        eqs += sp.Poly(sp.expand(sp.numer(sp.together(comp))), TT_, Z_).coeffs()
    sol = sp.solve(eqs, ms, dict=True)
    Ms = M.subs(sol[0]) if sol else None
    unique = bool(sol and not any(Ms.free_symbols))
    return {"field": field, "hyperboloid": str(hyper), "unique": unique,
            "matrix": str(Ms.tolist()) if Ms is not None else None,
            "M": Ms.as_immutable() if unique else None,
            "equals_J_minus_B_origin": bool(unique and Ms == so21_generators()["J-B_origin"]),
            **({} if Ms is None else matrix_class(Ms))}


@functools.lru_cache(maxsize=None)
def throat_dv_pushforward(field="d_t"):
    """Route 2's premise, computed: along the throat's ingoing EF chart (z = 2 sqrt2/u, t = v + z), d_v Y equals M Y
    for M = embedding_generator(field)['M'].  Label: computed."""
    M = embedding_generator(field)["M"]
    z = 2 * sp.sqrt(2) / U_
    Y = _poincare_Y(V_ + z, z)
    if M is None:
        return {"field": field, "dv_Y_equals_M_Y": False}
    resid = sp.simplify(sp.diff(Y, V_) - sp.Matrix(M) * Y)
    return {"field": field, "dv_Y_equals_M_Y": bool(resid == sp.zeros(3, 1))}


@functools.lru_cache(maxsize=None)
def ends_map(chart="ingoing"):
    """The throat's EF chart into global AdS2 through the Poincare embedding.  ingoing: t = v + 2 sqrt2/u,
    z = 2 sqrt2/u (sim2_passage X1, continued analytically through u = 0); outgoing (mutation): t = v - 2 sqrt2/u;
    mirror (mutation): z = 2 sqrt2/|u|, t = v + z, u < 0 treated as a copy of patch 1.  Returns smoothness at u = 0,
    the boundary each asymptotic end reaches (cot sigma = -Y^1), the horizon line (cos(T + sigma) = -1: patch 1's
    future horizon and patch 2's past horizon; cos(T - sigma) = -1: patch 1's past horizon), and the patch sign
    Y^-1 - Y^1 (= 1/z: an identity of the chart, deduced).  Label: computed."""
    if chart == "mirror":
        z = 2 * sp.sqrt(2) / sp.Abs(U_)
        t = V_ + z
    else:
        z = 2 * sp.sqrt(2) / U_
        t = V_ + z if chart == "ingoing" else V_ - z
    Y = [sp.simplify(sp.expand((1 - t**2 + z**2) / (2 * z))), sp.simplify(sp.expand(t / z)),
         sp.simplify(sp.expand(-(1 + t**2 - z**2) / (2 * z)))]
    smooth = True
    for comp in Y:
        for e in (comp, sp.diff(comp, U_)):
            lp, lm = sp.limit(e, U_, 0, "+"), sp.limit(e, U_, 0, "-")
            smooth = smooth and lp.is_finite is True and sp.simplify(lp - lm) == 0
    cot_end1, cot_end2 = sp.limit(-Y[2], U_, sp.oo), sp.limit(-Y[2], U_, -sp.oo)
    side = {sp.oo: "sigma=0", -sp.oo: "sigma=pi"}
    Y0 = [sp.simplify(sp.limit(c, U_, 0, "+")) for c in Y]
    s2 = 1 / (1 + Y0[2]**2)
    cpp = sp.simplify(s2 * (-Y0[0] * Y0[2] - Y0[1]))
    cpm = sp.simplify(s2 * (-Y0[0] * Y0[2] + Y0[1]))
    P = sp.simplify(Y[0] - Y[2])
    pp = [sp.sign(P.subs({U_: uu, V_: vv})) for uu in (sp.Rational(1, 3), 2, 7) for vv in (-2, 0, sp.Rational(5, 2))]
    pm = [sp.sign(P.subs({U_: -uu, V_: vv})) for uu in (sp.Rational(1, 3), 2, 7) for vv in (-2, 0, sp.Rational(5, 2))]
    return {"chart": chart, "Y_at_u0": [str(c) for c in Y0], "smooth_through_u0": bool(smooth),
            "end1_boundary": side.get(cot_end1, str(cot_end1)), "end2_boundary": side.get(cot_end2, str(cot_end2)),
            "cos_T_plus_sigma_at_u0": str(cpp), "cos_T_minus_sigma_at_u0": str(cpm),
            "u0_is_patch1_future_horizon": bool(cpp == -1 and cpm != -1),
            "u0_is_patch1_past_horizon": bool(cpm == -1 and cpp != -1),
            "patch_sign": {"u_pos": sorted(set(int(s) for s in pp)), "u_neg": sorted(set(int(s) for s in pm)),
                           "label": "deduced (an identity of the chart: Y^-1 - Y^1 = 1/z with z = 2 sqrt2/u; not "
                                    "part of C30c)"}}


@functools.lru_cache(maxsize=None)
def ads2_family_classes(deltas=(sp.Rational(-1, 9), 0, sp.Rational(1, 9)), dsign=1):
    """The AdS2 family -(x/2)dt^2 + dx^2/(x(x - delta)) (radius 2; Bronnikov-Kim's near-throat form on the plane, X19,
    is its [PLANE] reading with delta = r0 - 2m): R, the invariant Q of d_t, and its class.  dsign = -1 (x(x + delta))
    is C30d's mutation.  Label: computed.  Tag: [FREE given AdS2]."""
    dl = sp.Symbol("delta", real=True)
    g = sp.Matrix([[-X_ / 2, 0], [0, 1 / (X_ * (X_ - dsign * dl))]])
    gen = killing_class(g, [TT_, X_], [1, 0])
    rows = {str(dv): killing_class(g.subs(dl, dv), [TT_, X_], [1, 0])["class"] for dv in deltas}
    return {"Q_general": gen["Q"], "R": gen["R"], "Q_is_delta_over_8": bool(sp.simplify(gen["Q"] - dl / 8) == 0),
            "classes": rows}


# ------------------------------------------------------------------------------------------------ Lemma P
def _boost(axis, w):
    """Exact rational boost along axis (1..3): gamma = (1 + w^2)/(1 - w^2), gamma beta = 2w/(1 - w^2), |w| < 1."""
    L = [[Fr(int(i == j)) for j in range(4)] for i in range(4)]
    g, gb = (1 + w * w) / (1 - w * w), 2 * w / (1 - w * w)
    L[0][0] = L[axis][axis] = g
    L[0][axis] = L[axis][0] = gb
    return L


def _rot(i, j, a):
    L = [[Fr(int(p == q)) for q in range(4)] for p in range(4)]
    c, s = (1 - a * a) / (1 + a * a), 2 * a / (1 + a * a)
    L[i][i] = L[j][j] = c
    L[i][j], L[j][i] = -s, s
    return L


def _mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


ETA4 = [[Fr(-1) if i == j == 0 else Fr(int(i == j)) for j in range(4)] for i in range(4)]


def rational_lorentz(rng):
    """A generic exact rational Lorentz transformation (three boosts, two rotations)."""
    def rw():
        return Fr(rng.randint(-97, 97), 101)
    L = _boost(1, rw())
    for M in (_rot(1, 2, rw()), _boost(2, rw()), _rot(2, 3, rw()), _boost(3, rw())):
        L = _mm(L, M)
    return L


def sheet_density(S_low, u):
    """S_ab u^a u^b."""
    return sum(S_low[a][b] * u[a] * u[b] for a in range(4) for b in range(4))


@functools.lru_cache(maxsize=None)
def delta_stress_rows(n=1000, seed=5, dust=Fr(0)):
    """(i): S_ab = s eta_ab (+ dust e0 e0, the mutation) read by n exact rational observers u = L e0, for three s.
    Label: computed.  Tag: [FREE]."""
    rng = random.Random(seed)
    out = {}
    for s in (Fr(1), Fr(-1), Fr(3, 7)):
        S = [[s * ETA4[a][b] + (dust if a == b == 0 else 0) for b in range(4)] for a in range(4)]
        dens, lorentz_ok = set(), True
        for _ in range(n):
            L = rational_lorentz(rng)
            LtEL = [[sum(L[k][i] * ETA4[k][l] * L[l][j] for k in range(4) for l in range(4)) for j in range(4)]
                    for i in range(4)]
            lorentz_ok = lorentz_ok and LtEL == ETA4
            u = [L[a][0] for a in range(4)]
            dens.add(sheet_density(S, u))
        out[str(s)] = {"densities": sorted(str(x) for x in dens)[:3], "n_values": len(dens),
                       "all_equal_minus_s": dens == {-s}, "lorentz_exact": lorentz_ok}
    return out


@functools.lru_cache(maxsize=None)
def eq17_fluid(rc="3", pr_sign=1):
    """(ii) [PLANE]-conditional: eq. (17)'s Weyl fluid from b4_static's data (sim2_facing.B4._eq17) and
    sim2_facing._ricci_diag: 8 pi rho = -G^t_t, 8 pi p_r = G^r_r, 8 pi p_t = G^th_th at r = rc (units m = 1).
    pr_sign = -1 is C31b's mutation (p_r's sign flipped).  Label: computed."""
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    F, H = SF.B4._eq17(r)
    g = [-F, 1 / H, r**2, r**2 * sp.sin(th)**2]
    X = [t, r, th, ph]
    R, gi, _ = SF._ricci_diag(g, X)
    Rm = [sp.simplify(gi[a] * R(a, a)) for a in range(4)]
    Rs = sp.simplify(sum(Rm))
    Gm = [sp.simplify(Rm[a] - Rs / 2) for a in range(4)]
    rv = sp.Rational(rc)
    rho = sp.nsimplify(sp.simplify(-Gm[0].subs(r, rv)))
    pr = sp.nsimplify(sp.simplify(Gm[1].subs(r, rv))) * pr_sign
    pt = sp.nsimplify(sp.simplify(Gm[2].subs(r, rv)))
    owner = SF.r_hat(rc)[0]
    return {"r_over_m": str(rv), "8pi_rho": rho, "8pi_p_r": pr, "8pi_p_t": pt, "8pi_rho_plus_p_r": rho + pr,
            "owner_R_rad_sim2_facing": owner, "agrees_with_owner": bool(sp.simplify(rho + pr * pr_sign - owner) == 0)}


def boosted_density(rho, p, v):
    """T_ab u^a u^b for T = diag(rho, p) in the static orthonormal (t, r) frame and u = gamma(1, v): an observer's
    boost parameter v, never a speed of anything the device sees."""
    gam2 = 1 / (1 - v * v)
    u = (1, v)
    T = ((rho, 0), (0, p))
    return gam2 * sum(T[a][b] * u[a] * u[b] for a in range(2) for b in range(2))


def v_star(rho, p):
    """The boost parameter in (0, 1) at which the boosted density vanishes, exactly (sympy); None if there is none."""
    vv = sp.Symbol("v", positive=True)
    sols = [s for s in sp.solve(sp.Eq(sp.together(boosted_density(sp.sympify(rho), sp.sympify(p), vv)), 0), vv)
            if s.is_real and 0 < s < 1]
    return sols[0] if sols else None


def rho_prime_limit(rho, p):
    """The boosted density as the boost parameter v -> 1 (sympy limit)."""
    vv = sp.Symbol("v", positive=True)
    return sp.limit(boosted_density(sp.sympify(rho), sp.sympify(p), vv), vv, 1, "-")


@functools.lru_cache(maxsize=None)
def nec_rows(n=1000, seed=5, nec=1):
    """(ii)'s control: n exact rational (rho, p, v) with rho + p >= 0 (nec = 1) or < 0 (nec = -1, the mutation):
    is the boosted density >= rho for all of them?  Label: computed."""
    rng = random.Random(seed)
    worst = None
    ok = True
    for _ in range(n):
        rho = Fr(rng.randint(-500, 500), 97)
        q = Fr(rng.randint(0, 500), 89) if nec > 0 else -Fr(rng.randint(1, 500), 89)
        v = Fr(rng.randint(1, 999), 1000)
        d = boosted_density(rho, q - rho, v) - rho
        ok = ok and d >= 0
        worst = d if worst is None or d < worst else worst
    return {"all_rho_prime_ge_rho": ok, "least_rho_prime_minus_rho": str(worst)}


@functools.lru_cache(maxsize=None)
def approach_counterpart(nec=1, eps=S15_NEC_BOUND):
    """OC-4's counterpart, computed: a negative density rho = -1 (units of sigma_RS) with rho + p = nec*eps; nec = 1
    (NEC obeyed, eps = S15's reported bound 9.4e-7) has v* = 1/sqrt(1 + eps), beyond which a boosted observer reads a
    positive density, with gamma^2 v^2 = 1/eps at v*; nec = -1 (the mutation) has none.  Label: computed."""
    rho, p = sp.Integer(-1), 1 + nec * eps
    vs = v_star(rho, p)
    g2v2 = sp.simplify(vs**2 / (1 - vs**2)) if vs is not None else None
    return {"rho_over_sigma": str(rho), "rho_plus_p_over_sigma": str(nec * eps), "v_star": str(vs),
            "v_star_is_inv_sqrt_1_plus_eps": bool(vs is not None and sp.simplify(vs - 1 / sp.sqrt(1 + eps)) == 0),
            "gamma2v2_at_v_star": str(g2v2), "gamma2v2_float": float(g2v2) if g2v2 is not None else None,
            "gamma2v2_is_inv_eps": bool(g2v2 is not None and sp.simplify(g2v2 - 1 / eps) == 0),
            "rho_prime_limit_v_to_1": str(rho_prime_limit(rho, p))}


T_SAMPLES = [sp.pi * k / 6 for k in (0, 1, 2, 4, 5, 6, 7, 8, 10, 11)]      # cos T != 0 except where noted


@functools.lru_cache(maxsize=None)
def killing_charge_flip(use="xi.n", k_coeff=1):
    """(iii): at each boundary the charge density read by the future unit normal n = sin(sigma) d_T of T = const,
    rescaled: q_b = lim sin(sigma) (-g(xi, n)).  sin(sigma)(-g(xi, n)) = xi^T identically, so q_b is C30a's boundary
    component read as a charge (checked: identity_with_xi_T); not a second route.  use = 'xi.xi' reads lim
    sin^2(sigma) g(xi, xi) instead (a mutation); k_coeff = 2 a second.  Flip at T: q_0 q_pi < 0.  Label: computed."""
    out = {}
    gens = so21_generators(k_coeff)
    comps = generator_classes(k_coeff)
    for name in ("B_origin", "J+K", "J-K", "J-B_origin", "J"):
        xi, h, _ = global_killing_field(gens[name])
        nvec = sp.Matrix([sp.sin(S_), 0])
        xin = sp.simplify(sp.sin(S_) * (-(xi.T * h * nvec)[0]))
        dens = xin if use == "xi.n" else sp.simplify(sp.sin(S_)**2 * (xi.T * h * xi)[0])
        q0, qpi = sp.simplify(sp.limit(dens, S_, 0, "+")), sp.simplify(sp.limit(dens, S_, sp.pi, "-"))
        flips = [bool((q0 * qpi).subs(T_, tv) < 0) for tv in T_SAMPLES]
        same = bool(sp.simplify(q0 - comps[name]["component_at_sigma0"]) == 0
                    and sp.simplify(qpi - comps[name]["component_at_sigmapi"]) == 0)
        out[name] = {"q_sigma0": str(q0), "q_sigmapi": str(qpi), "flips_at_all_samples": all(flips),
                     "flips_at_some_sample": any(flips), "identity_with_xi_T": bool(sp.simplify(xin - xi[0]) == 0),
                     "equals_C30a_components": same}
    return out


def lemma_p(n=1000, seed=5):
    """Lemma P: (i) delta-stress density [FREE], (ii) eq. (17)'s Weyl fluid under boosts [PLANE]-conditional, with the
    NEC control and the approach counterpart, (iii) the Killing-charge flip [FREE given AdS2].  Label: computed."""
    i = delta_stress_rows(n, seed)
    fl = eq17_fluid("3")
    vs = v_star(fl["8pi_rho"], fl["8pi_p_r"])
    return {
        "i_delta_stress": {"rows": i, "label": "computed (exact rationals)", "tag": "[FREE]"},
        "ii_weyl_fluid": {"fluid": {k: str(vv_) for k, vv_ in fl.items()}, "v_star": str(vs),
                          "v_star_is_one_over_sqrt3": bool(vs is not None and sp.simplify(vs - 1 / sp.sqrt(3)) == 0),
                          "rapidity_star": float(sp.atanh(vs)) if vs is not None else None,
                          "rho_prime_limit_v_to_1": str(rho_prime_limit(fl["8pi_rho"], fl["8pi_p_r"])),
                          "nec_control": nec_rows(n, seed),
                          "approach_counterpart": approach_counterpart(),
                          "label": "computed (exact)",
                          "tag": "[PLANE]-conditional: under 179 eq. (17) is at most a plane's reading of the "
                                 "corridor's mouth (H-PLANE-READS-MOUTH, the board's); under 184 its vacuum-brane Weyl "
                                 "fluid is a matter-free plane's reading, a limit only.  The NEC control and the "
                                 "approach counterpart are [FREE] statements about boosted densities",
                          "note": "v is an observer's boost parameter, never a speed (139 (4), 101 (7))"},
        "iii_charge_flip": {"rows": killing_charge_flip("xi.n"),
                            "label": "computed (C30a's boundary components read as a charge; not a second route)",
                            "tag": "[FREE given AdS2]"},
    }


KAPPA_PREMISE = ("kappa = 0 (a degenerate horizon), which here comes from eq. (17) at r0 = 2m (C26a, [PLANE]); under "
                 "179 whether the bulk corridor's horizon is degenerate is OPEN")


def deduced_x18(fam=None):
    """The deductions X18 draws.  Label: deduced; each row labelled."""
    fam = ads2_family_classes() if fam is None else fam
    ap = approach_counterpart()
    return {
        "s15_delta_stress": {
            "label": "deduced (from (i), computed here, and SIM2-FACING S15, computed there)",
            "tag": "[FREE] for any delta-stress; S15's object is [PLANE] (the throat bulk at our plane, phase 2, re-read "
                   "under 179), within one universe at our tension (H-SPLIT-AT-OUR-TENSION, the board's), at the "
                   "coincidence limit; with P1 pure tension, a limit under 184",
            "text": "At the coincidence limit S15 computes position 2's surface stress S^a_b -> +sigma_RS delta^a_b "
                    "(rho = -sigma_RS; its matter part, our tension subtracted, rho_m = -2 sigma_RS with p_m = "
                    "+2 sigma_RS, also of delta form).  By (i) every observer tangent to the sheet reads the same "
                    "negative density there.  This holds at the limit only, which 172 (2) makes never reached."},
        "s15_along_the_approach": {
            "label": "computed (boosted_density at S15's reported bound, computed there); deduced",
            "tag": "[PLANE] (S15's object); the boost statement is [FREE]",
            "text": "Along the approach S15 reports every sample obeying the NEC, with (rho + p_i)/sigma_RS <= 9.4e-7 "
                    "at x = 1e-14: a bound, not a zero.  Wherever rho < 0 < rho + p_i in a tangent direction, rho' = "
                    "rho + gamma^2 v^2 (rho + p_i) turns positive beyond the boost parameter v* = sqrt(-rho/p_i): with "
                    "rho = -sigma_RS and rho + p_i = eps sigma_RS, v* = 1/sqrt(1 + eps) and gamma^2 v^2 = 1/eps at v* "
                    "(computed; at eps = 9.4e-7, gamma^2 v^2 = %.4g).  So at the depths actually reached a "
                    "sufficiently boosted observer can read a positive density wherever rho + p_i > 0; v is an "
                    "observer's boost parameter, never a speed.  What survives along the approach is own-frame: the "
                    "rest-frame density there tends to -sigma_RS, and the matter part to -2 sigma_RS, which fails "
                    "H-POSITIVE-ON-P2 (the board's reading of 139 (2)), as S15 records." % (ap["gamma2v2_float"] or 0)},
        "board_176_sentence": {
            "label": "deduced (from (i) and (iii)); READ (GJW PDF p.4; MQ PDF p.64); OPEN (between universes)",
            "tag": "[PLANE]-conditional: S15's object, kappa = 0 from eq. (17), within one universe",
            "board_sentence": BOARD_WORDS["176 (the board's answer, not M's words)"],
            "within_one_universe": "Fails for this object under four premises: (a) S15's coincident sheet, a [PLANE] "
                                   "result (the throat bulk at our plane, phase 2, re-read under 179), within one "
                                   "universe at our tension (H-SPLIT-AT-OUR-TENSION, the board's); (b) at the "
                                   "coincidence limit, never reached (172 (2)); (c) %s, so the corridor's generator "
                                   "is parabolic; (d) position 2's side taken as the AdS2 boundary opposite ours, "
                                   "which is OPEN (H-END-2-IS-OUR-FAR-END, the board's, reads that boundary as our "
                                   "own plane's far end).  Under them the coincident -sigma_RS is the same in every "
                                   "tangent Lorentz frame (i), and the parabolic generators' Killing charge does not "
                                   "flip between the boundaries (iii); the thermofield-double sign reading needs the "
                                   "hyperbolic boost about the origin, whose directions are opposite in the two "
                                   "wedges (GJW PDF p.4; MQ PDF p.64)." % KAPPA_PREMISE,
            "between_universes": "OPEN: the sentence's own clause -- 139 (2)'s positivity 'to be shown in position "
                                 "2's own frame (between universes, phase 3)' -- is not reached by this module.",
            "verdict": "Not refuted as a whole.  Within one universe, at the limit and under (a)-(d), it fails for "
                       "this object."},
        "extremal_member": {
            "label": "computed (classes, C30d; the elliptic d_T's norm, C30a); READ (MQ PDF pp.3, 7); deduced "
                     "(extremal, given kappa = 0)",
            "tag": "[FREE given AdS2] for the family; the corridor's place in it (delta = 0) is [FREE given kappa = "
                   "0], with kappa = 0 from eq. (17) ([PLANE]); OPEN under 179; delta = r0 - 2m is [PLANE] (X19)",
            "family": fam,
            "text": "On -(x/2)dt^2 + dx^2/(x(x - delta)) every member is AdS2 (R = -1/2) and the invariant of d_t is "
                    "Q = delta/8: delta < 0 hyperbolic (Rindler/thermal: the thermofield double; no passage, MQ PDF "
                    "p.7), delta = 0 parabolic (Poincare), delta > 0 elliptic (global time: MQ's coupled wormhole, "
                    "whose boundaries are lines of constant sigma, MQ PDF p.7; two-way, MQ PDF p.3; its generator d_T "
                    "has xi.xi = -1/sin^2 sigma < 0 everywhere, so no Killing horizon, computed).  An AdS2 throat "
                    "alone does not fix the class.  Given %s, the corridor is the extremal member, delta = 0, "
                    "between the two.  MQ PDF p.53's 'The full geometry will not contain a horizon' is MQ's "
                    "expectation ('we expect') in 'a sketch of an idea' (Fig. 23) of a 4D ambient set-up; it is set "
                    "beside, not used for the 2D member." % KAPPA_PREMISE},
        "end2_identification": {"label": "OPEN", "reading": "H-END-2-IS-OUR-FAR-END (the board's)",
                                "text": "The map computes that u < 0 is the Poincare patch on the other boundary. That "
                                        "this end is our own plane's far end, within one universe, is a global "
                                        "identification no instrument here computes (RI-6/PA-6): the board's reading, "
                                        "OPEN."},
        "positive_in_own_frame": {
            "label": "deduced (from (ii)'s computed limits and the approach counterpart)",
            "reading": "H-POSITIVE-IN-OWN-FRAME (the board's, spec 4.3)",
            "text": "Where rho + p < 0 the boosted density is unbounded below as v -> 1 (ii); where rho + p > 0 it is "
                    "unbounded above.  So 139 (2)'s 'positive' can be met only as each piece's own-frame density.  At "
                    "the coincidence limit (never reached, 172 (2)) S15's sheet is a delta-stress, the same in every "
                    "frame, so it cannot meet it in any frame there; along the approach the own-frame density is the "
                    "test, and S15 computes it negative (H-POSITIVE-ON-P2 fails)."},
    }


# ======================================================================================== guards
def address_guard(obj, extra_funcs=()):
    """Names only: no key of obj contains a BANNED_KEYS substring (sim2_facing's, with sim2_passage's read from its
    text) and no function of this module takes an argument named in sim2_facing.BANNED_ARGS."""
    mod = sys.modules[__name__]
    funcs = []
    for _, ob in inspect.getmembers(mod):
        f = getattr(ob, "__wrapped__", ob)                     # lru_cache wrappers unwrapped: every def is scanned
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            funcs.append(f)
    funcs += list(extra_funcs)
    bad_args = sorted({(f.__name__, p) for f in funcs for p in inspect.signature(f).parameters if p in BANNED_ARGS})
    keys = set()

    def walk(o):
        if isinstance(o, dict):
            for k, vv in o.items():
                keys.add(str(k))
                walk(vv)
        elif isinstance(o, (list, tuple)):
            for vv in o:
                walk(vv)
    walk(obj)
    bad_keys = sorted(k for k in keys if any(b in k.lower() for b in BANNED_KEYS))
    return {"n_funcs": len(funcs), "n_keys": len(keys), "bad_args": bad_args, "bad_keys": bad_keys,
            "banned_keys_used": list(BANNED_KEYS)}


CONTAINERS = ("X17", "X18", "lemma_p", "deduced")      # dicts whose every child must be a labelled row


def _label_tokens(lab):
    s = str(lab)
    while re.search(r"\([^()]*\)", s):
        s = re.sub(r"\([^()]*\)", "", s)
    s = re.sub(r"\[[^\[\]]*\]", "", s)
    return [t.strip() for t in re.split(r";|,|\band\b", s) if t.strip()]


def label_audit(obj, reads=None):
    """G3's computation: every 'label' anywhere, parentheses and [tags] stripped and split at ';', ',' and 'and', is
    made only of the six labels; every child of X17, X18 and of the containers lemma_p and deduced is a labelled row;
    every READ has a page."""
    bad, unlabelled = [], []

    def walk(o, path):
        if isinstance(o, dict):
            if "label" in o:
                toks = _label_tokens(o["label"])
                if not toks or any(t not in LABELS for t in toks):
                    bad.append((path, o["label"]))
            for k, vv in o.items():
                walk(vv, path + "/" + str(k))
        elif isinstance(o, list):
            for i, vv in enumerate(o):
                walk(vv, path + "[%d]" % i)
    walk(obj, "")

    def rows(o, path):
        for k, vv in o.items():
            p = path + "/" + str(k)
            if k in CONTAINERS and isinstance(vv, dict) and "label" not in vv:
                rows(vv, p)
            elif not (isinstance(vv, dict) and "label" in vv):
                unlabelled.append(p)
    for top in ("X17", "X18"):
        if isinstance(obj.get(top), dict):
            rows(obj[top], "/" + top)
    reads = READS if reads is None else reads
    nopage = [r["id"] for r in reads if r.get("status") == "READ" and not _pdf_pages(r.get("page", ""))]
    return {"bad_labels": bad, "unlabelled_rows": unlabelled, "reads_without_page": nopage}


# ======================================================================================== compute and checks
def compute(e_sqrt=None):
    fam = ads2_family_classes()
    out = {
        "_note": "epass_frames.py (E-PASS, the frames and demands owner): computed, READ and deduced; not verified; "
                 "not seated; 2026-10-09; fix round applied the same day",
        "_fix_round": FIX_ROUND,
        "X17": {
            "readme_flux_P1": {**{k: str(vv) for k, vv in readme_flux_P1().items()},
                               "label": "computed (sympy); STRUCTURAL (W1: E = mc^2 of the hole of N bits, crossing "
                                        "uniformly over the horizon's S^2)",
                               "tag": "[PLANE]-conditional: r_h = 2m and kappa = 0 are eq. (17)'s as P1's own metric "
                                      "(H-PLANE-READS-MOUTH, the board's; clause (G), 187 (3)); under 184 a "
                                      "vacuum-plane limit; under 172 (1) P1 is not the README's sheet -- a "
                                      "normalisation reference only"},
            "stationary_demand": stationary_demand(),
            "demand_si": demand_si(e_sqrt),
            "reads_beside": reads_beside(),
            "answer_158_4": answer_158_4(),
            "changing_half": {"label": "OPEN", "text": "Lemma L (the 5.912... coefficients) is [PLANE]; not built "
                                                       "in this module"},
        },
        "X18": {
            "generator_classes": {"rows": generator_classes(), "label": "computed", "tag": "[FREE]"},
            "induced_metric": {**induced_metric(), "label": "computed; READ (MQ (2.1) and the constraint, PDF p.5)",
                               "parametrisation": "standard-not-READ: Y^-1 = cos T/sin sigma, Y^0 = sin T/sin "
                                                  "sigma, Y^1 = -cos sigma/sin sigma (MQ print (2.1) and the "
                                                  "constraint, not this parametrisation)", "tag": "[FREE]"},
            "poincare_map": {**poincare_map(), "label": "computed", "tag": "[FREE]"},
            "throat_generator": {**throat_generator(), "label": "computed",
                                 "tag": "[FREE given kappa = 0]: the g_vv = -u^2/2 chart is sim2_passage X1's, from "
                                        "eq. (17) at r0 = 2m ([PLANE]); C30b's non-degenerate mutation shows the "
                                        "class turns on degeneracy alone"},
            "embedding_generator": {**{k: str(vv) for k, vv in embedding_generator().items()},
                                    "pushforward": throat_dv_pushforward(), "label": "computed", "tag": "[FREE]"},
            "ends_map": {**ends_map("ingoing"),
                         "label": "computed (u = 0 is patch 1's future and patch 2's past horizon); OPEN (the same "
                                  "shape as 122 (3)/132 only if patch 2 is position 2's side; the board's "
                                  "H-END-2-IS-OUR-FAR-END reads it as our own plane's far end)",
                         "tag": "[FREE given kappa = 0] (the degenerate EF chart)"},
            "ads2_family": {**fam, "label": "computed", "tag": "[FREE given AdS2]"},
            "lemma_p": lemma_p(),
            "deduced": deduced_x18(fam),
        },
        "M_words": M_WORDS,
        "board_words": BOARD_WORDS,
    }
    return out


def _json_default(o):
    if isinstance(o, (sp.Basic, Fr, sp.MatrixBase)):
        return str(o)
    return repr(o)


# Each check: (name, description, function(mut) -> (ok, detail), [mutation names]).  Every check calls this module's
# computing function on the (possibly mutated) input; none compares a constant to itself.
def chk_c26a(mut=None):
    r = readme_flux_P1(area_power=1 if mut == "r^2->r" else 2,
                       data_key="schwarzschild" if mut == "schwarzschild-data" else "eq17")
    ok = (r["equals_one_over_2m"] and r["r_h_over_m"] == 2 and r["kappa_x_m"] == 0
          and r["kappa_x_m_schwarzschild_control"] == sp.Rational(1, 4))
    return ok, "kappa4^2 int T_vv dv = %s per generator (r_h = %sm); kappa m = %s (%s data) against the Schwarzschild " \
               "control's %s" % (r["value"], r["r_h_over_m"], r["kappa_x_m"], r["data"],
                                 r["kappa_x_m_schwarzschild_control"])


def chk_c26b(mut=None):
    d = demand_si(area_power=1 if mut == "r^2->r" else 2, c_power=2 if mut == "c^4->c^2" else 4)
    N, I = d["rows"]["N_example"], d["rows"]["item155"]
    got = {"E_N_J": N["E_J"], "m_N": N["m_geometric_m"], "inv2m_N": N["kappa4sq_int_Tvv_per_m"],
           "m_155": I["m_geometric_m"], "inv2m_155": I["kappa4sq_int_Tvv_per_m"]}
    rel = {k: abs(got[k] / SI_EXPECTED[k] - 1) for k in SI_EXPECTED}
    ok = max(rel.values()) <= SI_TOL
    return ok, "E = %.6e J, m = %.6e m, 1/(2m) = %.6e m^-1; E = 3.8e22 J: m = %.6e m, 1/(2m) = %.6e m^-1; max rel " \
               "dev %.1e" % (got["E_N_J"], got["m_N"], got["inv2m_N"], got["m_155"], got["inv2m_155"],
                             max(rel.values()))


def chk_c26c(mut=None):
    reads = [dict(r) for r in READS]
    if mut == "altered-quote":
        r = _read("MSY-13", reads)
        r["fragment"] = r["fragment"].replace("more information", "less information")
    if mut == "page-99":
        _read("MQ-64", reads)["page"] = "PDF p.99 (printed 63), after (B.171)"
    f = reads_found(reads)
    bad = [k for k, vv in f.items() if not vv["ok"]]
    two = sum(1 for vv in f.values() if vv["transcriptions"] == 2)
    dep = [k for k, vv in f.items() if vv.get("departure")]
    return not bad, "%d/%d READs consistent (%d against a design-stage transcription, page agreeing; recorded page " \
                    "departure %s; %d fix-round READs single-transcription)%s" % (
                        len(f) - len(bad), len(f), two, dep, len(f) - two, "" if not bad else ": failing " + ", ".join(bad))


def chk_c26d(mut=None):
    eo = e_owner_values()
    fg = 2 if mut == "form-G->G^2" else 1
    ef = e_form_exponent(fg, eo)
    gd = g_exponent_of_E(dims=(1, 3, -2) if mut == "E-as-J*m" else (1, 2, -2))["G"]
    gf, gm = ef["G_exponent"], eo.get("g_measured")
    d = demand_si(form_g_power=fg)
    uN, u155, uG = d["rows"]["N_example"]["u_r_m"], d["rows"]["item155"]["u_r_m"], d["u_r_G_CODATA"]
    clauses = {
        "form = computation": gm is not None and gf != 0 and abs(float(gf) - gm) < 1e-6,
        "form reproduces the owner's value": ef["rel_dev_from_owner_value"] < 1e-12,
        "owner's banked u_r(E) = |g| U_R_G": abs(abs(float(gf)) * eo["U_R_G_banked"] - eo["u_r_E_banked"]) < 1e-12,
        "dimensional analysis = form": sp.simplify(gd - gf) == 0,
        "demand_si u_r(m) = |1 + g| u_r(G)": (gm is not None and abs(uN / (abs(1 + gm) * uG) - 1) < 1e-6
                                              and abs(u155 / uG - 1) < 1e-12)}
    ok = all(clauses.values())
    return ok, "G-exponent of E: owner's form %s, owner's computation %s, dimensional analysis %s; owner's banked " \
               "u_r(E) %.2e vs |g| U_R_G %.2e; form at the owner's constants rel dev %.1e; demand_si u_r(m) %.4e (N " \
               "example), %.4e (fixed E); route: %s%s" % (
                   gf, ("%.10f" % gm) if gm is not None else None, gd, eo["u_r_E_banked"],
                   abs(float(gf)) * eo["U_R_G_banked"], ef["rel_dev_from_owner_value"], uN, u155, eo["owner_route"],
                   "" if ok else "  FAILED: " + "; ".join(k for k, vv in clauses.items() if not vv))


def chk_c26e(mut=None):
    ls = lemma_s_owner(mutate=(mut == "non-stationary-gvv"))
    sd = stationary_demand(ls=ls)
    ok = bool(ls.get("imported") and ls.get("owner_says_zero") and sd["gated_on_owner_zero"]
              and sd["pair_net_per_generator"] == "0" and sd["sheet_form"]["partner_kappa4sq_int_Tvv_P1"] != "OPEN")
    rows = ls.get("rows", {})
    return ok, "owner imported %s; %s; demand gated %s, pair net %s, label '%s'" % (
        ls.get("imported"), "; ".join("%s: bulk R %s (witness %.3g), T5 witness %.3g, sheet S/nu witness %.3g" % (
            k, "0" if r["bulk_R_xixi_on_H"] == "0" else "nonzero", r["bulk_R_xixi_witness"],
            r["bulk_kappa5sq_T5_xixi_witness"], r["sheet_S_xixi_over_nu_witness"]) for k, r in rows.items()),
        sd["gated_on_owner_zero"], sd["pair_net_per_generator"], sd["label"][:48] + " ...")


def chk_c30a(mut=None):
    rows = generator_classes(k_coeff=2 if mut == "J+2K" else 1, scale=2 if mut == "Y-scaled-by-2" else 1)
    im = induced_metric(scale=2 if mut == "Y-scaled-by-2" else 1)
    st, ct = sp.sin(T_), sp.cos(T_)
    expect = {"J": ("elliptic", 1, 1), "B_origin": ("hyperbolic", -ct, ct), "K": ("hyperbolic", st, -st),
              "J+K": ("parabolic", 1 + st, 1 - st), "J-K": ("parabolic", 1 - st, 1 + st),
              "J-B_origin": ("parabolic", 1 + ct, 1 - ct)}
    ok, bad = True, []
    for name, (cls, b0, bpi) in expect.items():
        r = rows[name]
        good = (r["class_matrix"] == cls and r["class_killing_invariant"] == cls and r["Q_equals_minus_half_trM2"]
                and r["killing_equation"] and r["tangent"] and r["in_so21"]
                and sp.simplify(r["component_at_sigma0"] - b0) == 0 and sp.simplify(r["component_at_sigmapi"] - bpi) == 0)
        if cls == "parabolic":
            good = good and r["M3_zero"] and not r["M2_zero"]
        if not good:
            bad.append(name)
        ok = ok and good
    j_norm = sp.simplify(rows["J"]["xi_dot_xi"] + 1 / sp.sin(S_)**2) == 0
    bad += [lab for lab, good in (("induced metric != MQ (2.1)", im["equals_MQ_2_1"]),
                                  ("Y.Y != -1", im["on_unit_hyperboloid"]), ("J's norm", j_norm)) if not good]
    ok = ok and im["equals_MQ_2_1"] and im["on_unit_hyperboloid"] and j_norm
    return ok, "; ".join("%s %s/%s (%s, %s)" % (k, rows[k]["class_matrix"], rows[k]["class_killing_invariant"],
                                                  rows[k]["component_at_sigma0"], rows[k]["component_at_sigmapi"])
                         for k in rows) + "; induced metric = MQ (2.1): %s; J's xi.xi = %s" % (
        im["equals_MQ_2_1"], rows["J"]["xi_dot_xi"]) + ("" if ok else "  FAILED: " + ", ".join(bad))


def chk_c30b(mut=None):
    pm = poincare_map(power=1 if mut == "x=8/z" else 2)
    th = throat_generator(-(U_**2 - sp.Rational(1, 9)) / 2 if mut == "non-degenerate-gvv" else None)
    fld = "dilatation" if mut == "dilatation-for-d_t" else "d_t"
    em = embedding_generator(fld)
    pf = throat_dv_pushforward(fld)
    ok = (pm["is_poincare_radius2"] and th["class"] == "parabolic" and th["killing"] and th["constant"]
          and em["hyperboloid"] == "-1" and em["unique"] and em["class"] == "parabolic" and em["in_so21"]
          and pf["dv_Y_equals_M_Y"])
    return ok, "x = 8/z^2 Poincare: %s (z = %s); throat d_v [g_vv = %s]: Q = %s, %s; embedding %s: %s, %s; d_v Y = " \
               "M Y along the EF chart: %s" % (pm["is_poincare_radius2"], pm["z_of_u"], th["g_vv"], th["Q"], th["class"],
                                                fld, em["matrix"], em["class"], pf["dv_Y_equals_M_Y"])


def chk_c30c(mut=None):
    chart = {"outgoing-chart": "outgoing", "mirror-identification": "mirror"}.get(mut, "ingoing")
    e = ends_map(chart)
    ok = (e["smooth_through_u0"] and e["end1_boundary"] == "sigma=0" and e["end2_boundary"] == "sigma=pi"
          and e["u0_is_patch1_future_horizon"])
    return ok, "%s chart: smooth %s; end 1 on %s, end 2 on %s; u = 0: cos(T+s) = %s, cos(T-s) = %s (future horizon " \
               "of patch 1: %s)" % (chart, e["smooth_through_u0"], e["end1_boundary"], e["end2_boundary"],
                                    e["cos_T_plus_sigma_at_u0"], e["cos_T_minus_sigma_at_u0"],
                                    e["u0_is_patch1_future_horizon"])


def chk_c30d(mut=None):
    fam = ads2_family_classes(dsign=-1 if mut == "delta-sign-flipped" else 1)
    ok = (sp.simplify(fam["R"] + sp.Rational(1, 2)) == 0 and fam["Q_is_delta_over_8"]
          and fam["classes"] == {"-1/9": "hyperbolic", "0": "parabolic", "1/9": "elliptic"})
    return ok, "R = %s, Q = %s; classes %s" % (fam["R"], fam["Q_general"], fam["classes"])


def chk_c31a(mut=None):
    rows = delta_stress_rows(1000, 5, dust=Fr(1, 3) if mut == "dust-added" else Fr(0))
    ok = all(r["all_equal_minus_s"] and r["lorentz_exact"] for r in rows.values())
    return ok, "; ".join("s = %s: %d densit%s %s" % (s, r["n_values"], "y" if r["n_values"] == 1 else "ies",
                                                      r["densities"][:2]) for s, r in rows.items())


def chk_c31b(mut=None):
    fl = eq17_fluid("3", pr_sign=-1 if mut == "p_r-sign-flipped" else 1)
    vs = v_star(fl["8pi_rho"], fl["8pi_p_r"])
    lim = rho_prime_limit(fl["8pi_rho"], fl["8pi_p_r"])
    ok = (vs is not None and sp.simplify(vs - 1 / sp.sqrt(3)) == 0 and fl["8pi_rho"] == sp.Rational(1, 81)
          and fl["8pi_rho_plus_p_r"] == sp.Rational(-2, 81) and fl["agrees_with_owner"] and lim == -sp.oo)
    rap = float(sp.atanh(vs)) if vs is not None else float("nan")
    ok = ok and abs(rap - 0.658479) < 5e-7
    return ok, "8 pi rho_W = %s, 8 pi (rho_W + p_r) = %s (owner R_rad %s); v* = %s, rapidity %.6f; rho' -> %s as " \
               "v -> 1" % (fl["8pi_rho"], fl["8pi_rho_plus_p_r"], fl["owner_R_rad_sim2_facing"], vs, rap, lim)


def chk_c31c(mut=None):
    nec = -1 if mut == "NEC-violating" else 1
    r = nec_rows(1000, 5, nec=nec)
    ap = approach_counterpart(nec=nec)
    ok = r["all_rho_prime_ge_rho"] and ap["v_star_is_inv_sqrt_1_plus_eps"] and ap["gamma2v2_is_inv_eps"]
    return ok, "rho' >= rho for all 1000: %s (least rho' - rho = %s); rho = -1, rho + p = %s: v* = %s, gamma^2 v^2 " \
               "at v* = %s" % (r["all_rho_prime_ge_rho"], r["least_rho_prime_minus_rho"], ap["rho_plus_p_over_sigma"],
                               ap["v_star"], ap["gamma2v2_float"])


def chk_c31d(mut=None):
    f = killing_charge_flip("xi.xi" if mut == "xi.xi-for-xi.n" else "xi.n", k_coeff=2 if mut == "J+2K" else 1)
    ok = (f["B_origin"]["flips_at_all_samples"] and not any(f[k]["flips_at_some_sample"]
                                                            for k in ("J+K", "J-K", "J-B_origin", "J"))
          and all(r["equals_C30a_components"] for r in f.values()))
    return ok, "; ".join("%s: (%s, %s) flips %s" % (k, r["q_sigma0"], r["q_sigmapi"], r["flips_at_some_sample"])
                         for k, r in f.items()) + "; = C30a's components: %s" % all(
        r["equals_C30a_components"] for r in f.values())


_OUT = {}


def _output():
    if "o" not in _OUT:
        _OUT["o"] = compute()
    return _OUT["o"]


def chk_g1(mut=None):
    obj = json.loads(json.dumps(_output(), default=_json_default))
    extra = ()
    if mut == "planted-key-hold_time":
        obj = {"planted": {"hold_time": 1}, **obj}
    if mut == "planted-arg-gap":
        def planted(gap=0):
            return gap
        extra = (planted,)
    g = address_guard(obj, extra)
    ok = not g["bad_args"] and not g["bad_keys"]
    return ok, "%d functions, %d keys; bad args %s; bad keys %s" % (g["n_funcs"], g["n_keys"], g["bad_args"],
                                                                     g["bad_keys"])


def chk_g2(mut=None):
    words = {**M_WORDS, **BOARD_WORDS}
    if mut == "altered-M-quote":
        words["183"] = words["183"].replace("never violated", "never broken")
    if mut == "swapped-items":
        words["177"], words["183"] = words["183"], words["177"]
    f = m_words_verbatim(words)
    n_m = sum(1 for k in words if "board's" not in k)
    return all(f.values()), "%d/%d quotes verbatim inside their own items of M-RULINGS-2026-10-03.md (%d M's words, %d " \
                            "the board's)%s" % (sum(f.values()), len(f), n_m, len(f) - n_m,
                                            "" if all(f.values()) else ": not found " +
                                            ", ".join(k for k, vv in f.items() if not vv))


def chk_g3(mut=None):
    obj = json.loads(json.dumps(_output(), default=_json_default))
    reads = [dict(r) for r in READS]
    if mut == "planted-label":
        obj = {"planted": {"label": "verified"}, **obj}
    if mut == "computed-and-verified":
        obj = {"planted": {"label": "computed and verified"}, **obj}
    if mut == "row-without-label":
        obj["X17"]["planted"] = {"value": 1}
    if mut == "READ-without-page":
        reads[0]["page"] = ""
    a = label_audit(obj, reads)
    ok = not a["bad_labels"] and not a["reads_without_page"] and not a["unlabelled_rows"]
    return ok, "bad labels %s; unlabelled rows %s; READs without a page %s" % (
        a["bad_labels"][:3], a["unlabelled_rows"][:3], a["reads_without_page"])


CHECKS = [
    ("C26a", "1/(2m) per generator on P1; r_h = 2m; kappa(eq. 17) = 0 against the Schwarzschild control's 1/4",
     chk_c26a, ["r^2->r", "schwarzschild-data"]),
    ("C26b", "SI demands to 1e-5 relative (demand_si; exactE and o3_write by path)", chk_c26b, ["r^2->r", "c^4->c^2"]),
    ("C26c", "READ transcriptions consistent with the design-stage files, pages included", chk_c26c,
     ["altered-quote", "page-99"]),
    ("C26d", "E's G-exponent: the owner's form = its computation = its banked u_r(E) = dimensional analysis; carried "
     "into demand_si", chk_c26d, ["E-as-J*m", "form-G->G^2"]),
    ("C26e", "Lemma S's owner returns zero (bulk and sheet, degenerate and non-degenerate) and gates the demand",
     chk_c26e, ["non-stationary-gvv"]),
    ("C30a", "so(2,1) classes and boundary components, two routes; induced metric = MQ (2.1); J's norm", chk_c30a,
     ["J+2K", "Y-scaled-by-2"]),
    ("C30b", "x = 8/z^2 gives Poincare; the throat's d_v is parabolic (EF invariant; embedding matrix; pushforward)",
     chk_c30b, ["non-degenerate-gvv", "x=8/z", "dilatation-for-d_t"]),
    ("C30c", "ends: u > 0 on sigma = 0, u < 0 on sigma = pi, u = 0 patch 1's future / patch 2's past horizon",
     chk_c30c, ["outgoing-chart", "mirror-identification"]),
    ("C30d", "the AdS2 family: R = -1/2, Q = delta/8, three classes", chk_c30d, ["delta-sign-flipped"]),
    ("C31a", "1000 exact boosts preserve the delta-stress density -s", chk_c31a, ["dust-added"]),
    ("C31b", "eq. (17)'s Weyl fluid at r = 3m: v* = 1/sqrt3 exactly, rapidity 0.658479, rho' -> -oo", chk_c31b,
     ["p_r-sign-flipped"]),
    ("C31c", "NEC-obeying matter: rho' >= rho for 1000 exact boosts; the approach counterpart", chk_c31c,
     ["NEC-violating"]),
    ("C31d", "the Killing charge (C30a's components read as a charge) flips under B_origin only", chk_c31d,
     ["xi.xi-for-xi.n", "J+2K"]),
    ("G1", "keys and argument names avoid BANNED_KEYS / BANNED_ARGS (names only)", chk_g1,
     ["planted-key-hold_time", "planted-arg-gap"]),
    ("G2", "M's words (and the board's quoted sentence) verbatim inside their own items", chk_g2,
     ["altered-M-quote", "swapped-items"]),
    ("G3", "every label token is one of the six; no unlabelled result row; every READ has a page", chk_g3,
     ["planted-label", "computed-and-verified", "row-without-label", "READ-without-page"]),
]


def selftest():
    t0 = time.time()
    n_ok = 0
    for name, desc, f, _ in CHECKS:
        try:
            ok, detail = f()
        except Exception as ex:
            ok, detail = False, "EXCEPTION %r" % ex
        n_ok += bool(ok)
        print("[%s] %s %s -- %s" % ("PASS" if ok else "FAIL", name, desc, detail), flush=True)
    print("selftest: %d/%d passed in %.1f s (exactE's value by the %s route in %s s)" % (
        n_ok, len(CHECKS), time.time() - t0, "seeded" if not _E.get("full") else "full",
        _E.get("res", {}).get("owner_s")), flush=True)
    return n_ok == len(CHECKS)


def mutants():
    t0 = time.time()
    total, caught = 0, 0
    for name, desc, f, muts in CHECKS:
        for m in muts:
            total += 1
            try:
                ok, detail = f(mut=m)
            except Exception as ex:
                ok, detail = False, "EXCEPTION %r (counts as failing)" % ex
            caught += not ok
            print("[%s] %s under mutation '%s' -- %s" % ("FAILS (good)" if not ok else "PASSES (BAD)", name, m, detail),
                  flush=True)
    print("mutants: %d/%d mutations make their check fail, in %.1f s" % (caught, total, time.time() - t0), flush=True)
    return caught == total


def owner_route_compare():
    """--full-owner: E and the G-exponent by the full owner load and by the seeded route, compared."""
    full = _e_job(full=True)
    seeded = _e_job(full=False)
    same = full["e_per_sqrt_bit_J"] == seeded["e_per_sqrt_bit_J"] and full["form"] == seeded["form"]
    print("owner routes: full %r in %s s; seeded %r in %s s; equal: %s; g measured %.10f / %.10f" % (
        full["e_per_sqrt_bit_J"], full["owner_s"], seeded["e_per_sqrt_bit_J"], seeded["owner_s"], same,
        full["g_measured"], seeded["g_measured"]), flush=True)
    return same


def report(o):
    x17, x18 = o["X17"], o["X18"]
    print("epass_frames.py -- %s" % o["_note"])
    print("X17 readme_flux_P1: kappa4^2 int T_vv dv = %s per generator (r_h = %sm, kappa m = %s) [%s] %s" % (
        x17["readme_flux_P1"]["value"], x17["readme_flux_P1"]["r_h_over_m"],
        x17["readme_flux_P1"]["kappa_x_m"], x17["readme_flux_P1"]["label"], x17["readme_flux_P1"]["tag"]))
    sd = x17["stationary_demand"]
    print("  stationary demand (gated on the owner: %s): pair net %s (%s)" % (
        sd["gated_on_owner_zero"], sd["pair_net_per_generator"], sd["pair_net_reading"]))
    print("  %s" % sd["sheet_form"]["P1_reference"])
    for k, r in x17["demand_si"]["rows"].items():
        print("  %s: E = %.6e J, m = %.6e m, 1/(2m) = %.6e m^-1, u_r(m) = %.3e" % (
            k, r["E_J"], r["m_geometric_m"], r["kappa4sq_int_Tvv_per_m"], r["u_r_m"]))
    for name, r in x18["generator_classes"]["rows"].items():
        print("X18 %-10s %-10s eig %s, components (%s, %s), Q = %s" % (
            name, r["class_matrix"], r["eigenvalues"], r["component_at_sigma0"], r["component_at_sigmapi"], r["Q"]))
    print("  throat d_v: %s (Q = %s); embedding d_t %s %s; ends: %s" % (
        x18["throat_generator"]["class"], x18["throat_generator"]["Q"], x18["embedding_generator"]["matrix"],
        x18["embedding_generator"]["class"],
        {k: x18["ends_map"][k] for k in ("end1_boundary", "end2_boundary", "u0_is_patch1_future_horizon")}))
    lp = x18["lemma_p"]
    print("  Lemma P (ii): v* = %s, rapidity %.6f, rho' -> %s as v -> 1; approach counterpart gamma^2 v^2 = %s" % (
        lp["ii_weyl_fluid"]["v_star"], lp["ii_weyl_fluid"]["rapidity_star"], lp["ii_weyl_fluid"]["rho_prime_limit_v_to_1"],
        lp["ii_weyl_fluid"]["approach_counterpart"]["gamma2v2_float"]))
    print("  AdS2 family: %s" % x18["ads2_family"]["classes"])
    print("  176 sentence: %s" % x18["deduced"]["board_176_sentence"]["verdict"])


def main(argv):
    ok = True
    if "--full-owner" in argv:
        ok = owner_route_compare() and ok
    if "--selftest" in argv:
        ok = selftest() and ok
    if "--mutants" in argv:
        ok = mutants() and ok
    if "--json" in argv:
        path = argv[argv.index("--json") + 1]
        with open(path, "w") as fh:
            json.dump(_output(), fh, indent=1, default=_json_default)
        print("wrote %s" % path)
    if not any(a in argv for a in ("--selftest", "--mutants", "--json", "--full-owner")):
        report(json.loads(json.dumps(_output(), default=_json_default)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
