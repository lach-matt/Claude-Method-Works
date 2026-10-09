#!/usr/bin/env python3
"""epass_frames.py -- E-PASS fix round, a standalone [FREE] owner: the demands (spec X17, stationary half) and the
frames (spec X18: the corridor's generator classes, its two ends, and Lemma P).  Build specification:
lemmas/EPASS-DESIGN-SPEC.md, X17 (stationary half only), X18, checks C26, C30, C31 of its section 8.
sim2_passage.py imports this module by path for those X-sections; it is never copied there.
Computed, READ and deduced; not verified; not seated; 2026-10-09.

CLI:  --selftest  (every check; each able to fail; budget < 90 s, the floor being exactE's 70 s owner load, which runs
                   in a forked child while the other checks run)
      --mutants   (runs every named mutation of every check and shows that the check FAILS under it; exit 1 if any
                   mutation passes)
      --json PATH (writes compute(): every value X17 and X18 need, each row labelled)
      (no flag)   prints the report

LABELS.  Every result row carries one or more of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  The board's readings are named H-... and kept apart from M's words, quoted verbatim (typing
kept) from M-RULINGS-2026-10-03.md; G2 checks every quote against that file.  A negative result is reported as plainly
as a positive one (M-IRREFUTABLE, 135).  Tags: [FREE] holds whatever carries the corridor (a plane, a sheet, the bulk
alone); [PLANE] uses eq. (17) as our plane's own metric (the board's pre-179 configuration).  Row (ii) of Lemma P is
a [PLANE]-conditional row inside this [FREE] module: under 179 eq. (17) is at most a plane's reading of the
corridor's mouth (H-PLANE-READS-MOUTH, the board's).

M'S WORDS USED (verbatim; see M_WORDS):
  129 (1) "...just not a corridor for transit because the corridor is a bridge, so it adds nothing to either position."
  132 "...the passage is one way by nature, a black hole in and a white hole out, side views of the same corridor
      object" and "*different views of the same object";  122 (3) "3 - your candidate is correct" (the board's
      candidate: P1's black-hole (future) horizon and P2's white-hole (past) horizon);  122 (4) "...The rules apply,
      but do not restrict information";  139 (2) "2 - positive, and you have to prove it.";  139 (4);  158 (4) "This
      too is a question for the math.";  162 (fixed size, "once and at once");  172 M chose "Yes, it may" and "Yes,
      that is coinciding";  176 "But what if it is in fact entanglement?";  177 M chose "Yes, that is the
      appearance";  179/180 "the corridor *does not sit on either position's plane, it only bridges them";  181
      "this bears directly on B4d, and requires priority";  182 "If I had to guess, I would go with C";  183 M chose
      "Yes: never violated as a pair";  184 "There are no matter free planes";  185 (run the matter round).

READINGS.  M's, as carried in the rulings file: H-CORRIDOR-IN-BULK (179/180), H-README-ON-P2 (172 (1)),
H-COINCIDE-DOWN-THE-THROAT (172 (2)), H-SIDES-AS-HORIZON-PAIR (122 (3)), H-ONE-WAY-BY-NATURE (132), H-FIXED-SIZE
(162), H-COUPLING-IS-THE-APPEARANCE (177), H-NEC-NEVER-VIOLATED-AS-PAIR (183; its gloss "zero net null energy along
each light ray" is the wording of the option the board put and M chose), H-NO-MATTER-FREE-PLANES (184).  The board's:
H-PARTNER-IS-THE-COUPLING (177 covers the exact negative partner Lemma S demands; admitted under 183),
H-PLANE-READS-MOUTH, H-PAIRING-IS-ENTANGLEMENT (176; its sentence on position 2's -1 is refuted below for this object),
H-README-AS-NULL-DUST, H-POSITIVE-IN-OWN-FRAME (spec 4.3), H-STATIONARY-CROSSING, H-FIXED-SIZE-AS-THETA-ZERO,
H-END-2-IS-OUR-FAR-END (new name for an old identification: that end 2 is our own plane's far end; OPEN, RI-6/PA-6).

X17 THE DEMANDS [FREE, stationary half] (computed; STRUCTURAL; deduced; READ).
  readme_flux_P1(): sympy.  The horizon is the root of eq. (17)'s F = 1 - 2m/r (owner b4_static via sim2_facing.B4,
    by path): r_h = 2m.  W1 (STRUCTURAL): E = m c^2 of the hole of N bits; the README crosses uniformly over the S^2 of
    generators (area average); with kappa = 0 the Killing parameter v is affine.  kappa4^2 int T_vv dv =
    8 pi m / int int r_h^2 sin(theta) = 8 pi m/(4 pi (2m)^2) = 1/(2m) exactly per generator.  Mutation r^2 -> r: 1.
  stationary_demand(): Lemma S (owner lemmas/epass_pairing.py, imported by path when present; else a pointer to the
    spec's X13).  BULK FORM PRIMARY (179/180: the corridor sits on neither plane): T5^c(xi,xi) = -T5^R(xi,xi) along
    every generator of the stationary bulk horizon; its 5D normalisation is OPEN (the bulk horizon's section is the
    bulk balance's, 181).  SHEET FORM on whichever sheet carries the README (172 (1)): in P1's normalisation
    kappa4^2 int T^c_vv dv = -1/(2m) per generator; on position 2's piece in that sheet's normalisation [PLANE], not
    computed here.  The pair's net is ZERO -- never "positive" (spec pitfall 13).  Under 183 the exact pair is admitted
    (H-PARTNER-IS-THE-COUPLING): the stationary crossing is OPEN (supply beyond the board's instruments), NOT refuted.
    Lemma S is law- and tension-independent, so it holds with matter on both planes (184); matter-free results are
    limits only.
  demand_si(): E = exactE.e_per_sqrt_bit() * sqrt(N) at o3_write.EXAMPLE_N (both by path), G, c as banked in o3_write:
    E = 2.40588e16 J, m = G E/c^4 = 1.98791e-28 m, 1/(2m) = 2.51521e27 m^-1; at item 155's E = 3.8e22 J (the board's
    figure in 155): m = 3.13983e-22 m, 1/(2m) = 1.59244e21 m^-1.  u_r(G) = 2.2474e-5 (CODATA 2018 u = 0.00015e-11,
    standard-not-READ; exactE banks 2.2e-5).  PROPAGATED (computed): E scales as G^(-1/2) (dimensional analysis,
    matching chain.py's banked u_r(E) = u_r(G)/2), so at the N example m and 1/(2m) carry u_r(G)/2 = 1.12e-5; at the
    fixed E = 3.8e22 J they carry u_r(G) = 2.25e-5.
  reads_beside(): GJW, MSY, MQ -- READ in this run (alphaXiv full text; PDF page, printed page), each set BESIDE the
    demands, never as a supply; each fragment also checked verbatim against the spec's section 10 / epass_ground.json.
    MSY's parametric bound set against 122 (4)'s words: reported, not decided (OPEN).
  answer_158_4(): stationary -- nothing net is absorbed; the pair cancels (under 183, "never violated" as a pair);
    changing -- into the bulk's Weyl field and the creased bulk horizon (Lemmas L, K), a necessary condition only.
    The changing half (Lemma L, the 5.912... coefficients) is [PLANE] and is NOT built here.

X18 ENDS, GENERATORS, LEMMA P [FREE given an AdS2 throat] (computed; deduced; READ).
  generator_classes(): global AdS2 Y^-1 = cos T/sin s, Y^0 = sin T/sin s, Y^1 = -cos s/sin s (MQ (2.1), READ PDF
    p.5); so(2,1) matrices; each induced Killing field obtained by projection, its Killing equation verified, and its
    class found two ways (matrix eigenvalues / nilpotency, and the 2D invariant Q = (nabla xi)^2/2 - xi.xi/L^2, with
    Q = -tr(M^2)/2 checked): d_T elliptic (+-i, 0), components 1, 1; the boost about the origin hyperbolic (+-1, 0),
    -cos T at s -> 0 and +cos T at s -> pi; the other boost K +sin T, -sin T; J +- K parabolic (M^3 = 0, M^2 != 0),
    components 1 +- sin T, 1 -+ sin T, both >= 0.
  throat_generator(), poincare_map(), embedding_generator(): x = 8/z^2 takes -(x/2)dt^2 + dx^2/x^2 to
    4(-dt^2 + dz^2)/z^2 (Poincare, radius 2), z = 2 sqrt2/u; the throat's d_v is parabolic by its EF Killing
    invariant (Q = 0) and by its embedding matrix (nilpotent).  Mutation: a non-degenerate g_vv classifies hyperbolic.
  ends_map(): the ingoing chart is smooth through u = 0 into the embedding; u > 0 is the Poincare patch on the s = 0
    boundary, u < 0 the patch on the s = pi boundary; u = 0 is patch 1's future horizon (T + s = pi) and patch 2's past
    horizon (deduced from the computed map; 122 (3), 132).  That end 2 is OUR OWN plane's far end is a global
    identification no instrument computes: H-END-2-IS-OUR-FAR-END, the board's, OPEN.
  lemma_p(n=1000, seed=5): (i) a delta-stress S = s delta reads density -s for every observer (1000 exact rational
    Lorentz transformations, three s); (ii) [PLANE]-conditional: eq. (17)'s Weyl fluid at r = 3m (rederived here from
    b4_static's data with sim2_facing._ricci_diag; cross-checked against sim2_facing.r_hat): 8 pi rho_W = 1/81,
    8 pi (rho_W + p_r) = -2/81; rho' = rho + gamma^2 v^2 (rho + p_r) < 0 beyond v* = 1/sqrt3 exactly (rapidity
    atanh(1/sqrt3) = 0.658479), an OBSERVER'S boost parameter, never a speed; rho' -> -infinity as v -> 1; NEC-obeying
    matter gives rho' >= rho; (iii) the Killing charge flips sign between the boundaries under the boost about the
    origin and not under the parabolic generators.
  deduced_x18(): S15's coincident sheet (+sigma_RS delta, rho = -sigma_RS; matter part rho_m = -2 sigma_RS) is a
    delta-stress, so no observer's frame makes it positive; the board's 176 sentence ("position 2's -1 would be the
    partner's sign seen from our side") is refuted for this object; the corridor is the extremal (parabolic) member
    between the thermofield double (hyperbolic, thermal, no passage: MQ READ PDF p.7) and MQ's coupled wormhole
    (elliptic, no horizon, two-way: MQ READ PDF pp.53, 3), computed on the AdS2 family -(x/2)dt^2 + dx^2/(x(x - delta))
    whose invariant is Q = delta/8.

CHECKS (each calls this module's computing function on the mutated input; --mutants shows each fails):
  C26a 1/(2m) exact [r^2->r];  C26b SI values to 1e-5 relative [r^2->r];  C26c READ fragments verbatim
  [altered-quote];  C26d E's G-exponent vs chain's banked u_r(E) [E-as-J*m];  C30a classes and boundary components
  [J+2K];  C30b Poincare and the throat's parabolic d_v [non-degenerate-gvv, x=8/z];  C30c the ends
  [outgoing-chart, mirror-identification];  C31a delta-density under 1000 boosts [dust-added];  C31b v* = 1/sqrt3
  [p_r-sign-flipped];  C31c NEC gives rho' >= rho [NEC-violating];  C31d the flip [xi.xi-for-xi.n];
  G1 keys/args vs BANNED_KEYS/BANNED_ARGS (names only) [planted-key-hold_time, planted-arg-gap];
  G2 M's words verbatim [altered-M-quote];  G3 labels and pages [planted-label, READ-without-page].

Owners imported by path, never copied: sim2_facing.py (BANNED_KEYS, BANNED_ARGS, B4._eq17, B4._schwarzschild,
_ricci_diag, r_hat), copy/exactE.py (e_per_sqrt_bit, U_R_G, owners()['chain'].coefficients() for the banked u_r(E)),
lemmas/o3_write.py (EXAMPLE_N, G_SI, C_SI), lemmas/epass_pairing.py (Lemma S, when present).  Data only (never
evidence): EPASS-DESIGN-SPEC.md section 10 and epass_ground.json (READ fragments), M-RULINGS-2026-10-03.md.
It is necessary, not sufficient, and never B4d green.  No value here is a length (155 (2): bits), a distance, a speed
(139 (4)) or anything the device sees (101 (7)).
python3 epass_frames.py [--selftest] [--mutants] [--json PATH]   (stdlib + sympy; python 3.11)
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
        path = {"exactE": os.path.join(D68, "copy", "exactE.py"), "o3_write": os.path.join(HERE, "o3_write.py")}[name]
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
    "155 (the board's figure, not M's words)": "an exact README needs E >= 3.8e22 J",
}


def m_words_verbatim(words=None):
    """G2's computation: each quote found verbatim (whitespace-normalised for the file's line wrapping) in the rulings
    file."""
    words = M_WORDS if words is None else words
    with open(RULINGS) as fh:
        text = _norm(fh.read())
    return {k: (_norm(q) in text) for k, q in words.items()}


# ======================================================================================== READs (this run; C26c)
READS = [
    {"id": "GJW-2", "source": "P. Gao, D. L. Jafferis, A. C. Wall, 'Traversable Wormholes via a Double Trace "
     "Deformation', arXiv:1608.05687v3", "page": "PDF p.2 (printed 2)", "status": "READ",
     "quote": "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes "
              "[37, 50, 51, 23].",
     "fragment": "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes",
     "fragment_file": "spec", "bearing": "beside the demand: the exact negative partner is ANEC-violating along the "
     "crossed generators; a prerequisite, never a supply"},
    {"id": "GJW-3", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.3 (printed 3), after eq. (1.2)",
     "status": "READ",
     "quote": "This connects the boundaries with the same time orientation, since the t coordinate runs in opposite "
              "directions in two wedges (see Fig. 1.1a).",
     "fragment": "This connects the boundaries with the same time orientation", "fragment_file": "spec",
     "bearing": "their coupling joins the two boundaries of the thermofield double, whose Killing time is opposite in "
     "the two wedges -- the hyperbolic case of Lemma P (iii)"},
    {"id": "GJW-4", "source": "Gao-Jafferis-Wall, arXiv:1608.05687v3", "page": "PDF p.4 (printed 4)",
     "status": "READ",
     "quote": "In fact, |tfd> is invariant under H_R - H_L, which corresponds to the bulk Killing symmetry i d_t (note "
              "the directions are opposite in left and right wedges).",
     "fragment": "(note the directions are opposite in left and right wedges)", "fragment_file": "spec",
     "bearing": "the TFD's generator flips between the sides; Lemma P (iii) computes that the corridor's parabolic "
     "generator does not"},
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
     "bearing": "set against 122 (4) (H-RULES-NOT-INFORMATION): reported, not decided; parametric, never a supply"},
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
     "fragment_file": "spec", "bearing": "the elliptic member is two-way"},
    {"id": "MQ-5", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.5 (printed 4), eqs. (2.1)-(2.2)",
     "status": "READ",
     "quote": "ds^2 = (-dt^2 + dsigma^2)/sin^2 sigma, sigma in [0, pi] (2.1) ... the above coordinate systems manifest "
              "only one of them, a different generator for each of the coordinate systems.",
     "fragment": "a different generator for each of the coordinate systems", "fragment_file": "spec",
     "bearing": "the global chart used by generator_classes (the spec cites PDF p.6; this run finds (2.1)-(2.2) on "
     "PDF p.5)"},
    {"id": "MQ-7", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.7 (printed 6)", "status": "READ",
     "quote": "For this solution, the two boundary trajectories correspond to lines of constant rho in the "
              "Rindler/Thermal coordinates (2.2), and we cannot send signals between the boundaries.",
     "fragment": "we cannot send signals between the boundaries", "fragment_file": "ground",
     "bearing": "the hyperbolic (thermal) member: no passage"},
    {"id": "MQ-53", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.53 (printed 52)", "status": "READ",
     "quote": "The throat is supported by negative null energy (energy that contributes negatively to the integrated "
              "null energy) produced by quantum effects. ... The full geometry will not contain a horizon, but will "
              "have non-trivial topology in the ambient space.",
     "fragment": "The full geometry will not contain a horizon", "fragment_file": "spec",
     "bearing": "beside the demand: the eternal coupled kind removes the horizon (against 132, 143 A); never a supply"},
    {"id": "MQ-64", "source": "Maldacena-Qi, arXiv:1804.00491v3", "page": "PDF p.64 (printed 63), after (B.171)",
     "status": "READ",
     "quote": "at t = 0, the operator H_R - H_L can be identified with (q_+ + q_-)/2 which turns out to be the boost "
              "generator around the origin in AdS2. ... By origin we mean t = 0, sigma = pi/2 in the coordinates in "
              "(2.1).",
     "fragment": "the boost generator around the origin in AdS2", "fragment_file": "spec",
     "bearing": "the TFD's generator is the boost about the origin (the point generator_classes' boost fixes)"},
]


def _ground_text():
    with open(GROUND) as fh:
        d = json.load(fh)
    out = []

    def walk(o):
        if isinstance(o, dict):
            for vv in o.values():
                walk(vv)
        elif isinstance(o, list):
            for vv in o:
                walk(vv)
        elif isinstance(o, str):
            out.append(o)
    walk(d)
    return _norm(" ".join(out))


def _spec_section10():
    with open(SPEC) as fh:
        t = fh.read()
    i, j = t.find("## 10. READs"), t.find("## 11.")
    return _norm(t[i:j])


def reads_found(reads=None):
    """C26c's computation: each fragment found verbatim in its declared design-stage file (spec section 10 or
    epass_ground.json) AND inside this run's verbatim quote (whitespace-normalised).  'eq. (2.25)' is a pointer
    fragment: it must be in the spec, and the quote must carry '(2.25)'."""
    reads = READS if reads is None else reads
    spec, ground = _spec_section10(), _ground_text()
    res = {}
    for r in reads:
        src = spec if r["fragment_file"] == "spec" else ground
        frag = _norm(r["fragment"])
        in_quote = (frag in _norm(r["quote"])) if not frag.startswith("eq. ") else (frag[4:] in r["quote"])
        res[r["id"]] = bool(frag in src and in_quote and r.get("page"))
    return res


# ======================================================================================== X17 the demands [FREE]
M_SYM = sp.Symbol("m", positive=True)


@functools.lru_cache(maxsize=None)
def readme_flux_P1(area_power=2):
    """kappa4^2 int T_vv dv per generator on P1 (sympy, exact).  r_h from eq. (17)'s F (owner b4_static via
    sim2_facing.B4._eq17), restored to units of m; the area integral of r_h^area_power sin(theta) over the S^2;
    W1 (STRUCTURAL): kappa4^2 E = 8 pi G M/c^4 = 8 pi m.  area_power = 1 is the spec's mutation r^2 -> r."""
    r, th, ph = sp.symbols("r theta phi", positive=True)
    F17 = SF.B4._eq17(r)[0]
    roots = sp.solve(sp.Eq(F17, 0), r)
    rs_schw = sp.solve(sp.Eq(SF.B4._schwarzschild(r)[0], 0), r)
    r_h = roots[0] * M_SYM
    area = sp.integrate(sp.integrate(r_h**area_power * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
    val = sp.simplify(8 * sp.pi * M_SYM / area)
    return {"value": val, "r_h_over_m": roots[0], "r_h_over_m_schwarzschild_control": rs_schw[0],
            "area": sp.simplify(area), "equals_one_over_2m": bool(sp.simplify(val - 1 / (2 * M_SYM)) == 0),
            "dlog_dlogm": sp.simplify(M_SYM * sp.diff(val, M_SYM) / val)}


_LS = {}


def lemma_s_owner():
    """Lemma S from lemmas/epass_pairing.py (by path), when present: its bulk form R(xi,xi)|_H and kappa5^2 T5(xi,xi)
    on the general stationary degenerate bulk, and its sheet form S(xi,xi)/nu on the degenerate throat sheet.  Any
    failure (the file is being built by another run) falls back to a pointer."""
    if _LS:
        return _LS
    out = {"owner": "lemmas/epass_pairing.py", "present": os.path.exists(PAIRING),
           "pointer": "lemmas/EPASS-DESIGN-SPEC.md X13 (Lemma S: R(xi,xi) = 0 on any Killing horizon; K(xi,xi) = 0 on "
                      "every sheet tangent to xi); axioms.py Z3 re-read under 183"}
    if out["present"]:
        try:
            P = _load(PAIRING, "epass_frames_pairing")
            b = P.pairing_bulk(*P.bulk_gvv("degenerate"))
            s = P.pairing_sheet(*P.sheet_gvv("degenerate"))
            out.update({"imported": True, "bulk_R_xixi_on_H": str(b["R_xixi"]),
                        "bulk_kappa5sq_T5_xixi_on_H": str(b["kappa2_T5_xixi"]),
                        "sheet_S_xixi_over_nu_on_H": str(s["S_xixi_over_nu"]),
                        "label": "computed (by the owner epass_pairing.py, imported by path; not re-derived here)"})
            out["owner_says_zero"] = bool(b["R_xixi"] == 0 and b["kappa2_T5_xixi"] == 0 and s["S_xixi_over_nu"] == 0)
        except Exception as ex:   # the owner is under construction: state the demand with the pointer
            out.update({"imported": False, "load_error": repr(ex)[:300]})
    else:
        out["imported"] = False
    _LS.update(out)
    return _LS


def stationary_demand(area_power=2):
    """The stationary demand of Lemma S, in its two forms (bulk primary under 179/180; sheet on whichever sheet carries
    the README, 172 (1)), with P1's number.  The pair's net is zero and is never called positive."""
    R = readme_flux_P1(area_power)
    fR = R["value"]
    fc = -fR                                   # Lemma S: T^c(xi,xi) = -T^R(xi,xi) pointwise (deduced from the owner)
    net = sp.simplify(fR + fc)
    return {
        "lemma_s": lemma_s_owner(),
        "bulk_form": {"tag": "[FREE] primary under 179/180", "label": "deduced; OPEN",
                      "statement": "T5^c(xi,xi) = -T5^R(xi,xi) along every generator of the stationary bulk horizon "
                                   "(R(xi,xi) = 0 there with no field equation; Einstein + Lambda_5)",
                      "normalisation": "OPEN: the README's 5D flux per bulk generator needs the bulk horizon's "
                                       "section, which is the bulk balance's (181); not computed here"},
        "sheet_form": {"tag": "[FREE] on whichever sheet carries the README (172 (1))", "label": "deduced; computed",
                       "readme_kappa4sq_int_Tvv_P1": str(fR), "partner_kappa4sq_int_Tvv_P1": str(fc),
                       "statement": "kappa4^2 int T^c_vv dv = %s per generator in P1's normalisation; on position 2's "
                                    "piece in that sheet's normalisation [PLANE], not computed here" % fc},
        "pair_net_per_generator": str(net),
        "pair_net_reading": "zero: neither positive nor negative (spec pitfall 13; 139 (2)'s 'positive' is not met "
                            "by a pair total)",
        "under_183": {"label": "deduced; OPEN",
                      "text": "M chose 'Yes: never violated as a pair'; H-NEC-NEVER-VIOLATED-AS-PAIR (carried as M's) "
                              "admits the exact +/- null pair through H-PARTNER-IS-THE-COUPLING (the board's): the "
                              "stationary crossing is OPEN -- the demand is exact, the supply beyond the board's "
                              "instruments -- and NOT refuted"},
        "under_184": {"label": "deduced",
                      "text": "Lemma S uses no field law and no tension, so it holds with matter on both planes; "
                              "matter-free results are limits only"},
        "label": "deduced (from Lemma S) and computed (P1's number)",
    }


@functools.lru_cache(maxsize=None)
def g_exponent_of_E(dims=(1, 2, -2)):
    """The exponent of G in an energy built from hbar, c and G alone (dimensional analysis, sympy).  dims are the
    target's (kg, m, s) exponents: (1, 2, -2) is a joule; (1, 3, -2) (J m) is C26d's mutation."""
    a, b, g = sp.symbols("a b g")
    hb, cc, GG = (1, 2, -1), (0, 1, -1), (-1, 3, -2)
    eqs = [sp.Eq(a * hb[i] + b * cc[i] + g * GG[i], dims[i]) for i in range(3)]
    s = sp.solve(eqs, [a, b, g], dict=True)[0]
    return {"hbar": s[a], "c": s[b], "G": s[g]}


_E = {}


def _e_job():
    ex = _owner("exactE")
    v = ex.e_per_sqrt_bit()
    co = ex.owners()["chain"].coefficients()["E_min_J_per_sqrt_bit"]
    return {"e_per_sqrt_bit_J": v, "u_r_E_banked": co["u_r"], "U_R_G_banked": ex.U_R_G, "form": co["form"]}


def start_e_background():
    """exactE's owner load takes about 70 s; run it in a forked child while the other checks run."""
    if "res" in _E or "async" in _E:
        return
    import multiprocessing as mpc
    try:
        _E["t0"] = time.time()
        pool = mpc.get_context("fork").Pool(1)
        _E["async"], _E["pool"] = pool.apply_async(_e_job), pool
    except Exception:
        pass


def e_owner_values():
    if "res" not in _E:
        if "async" in _E:
            _E["res"] = _E["async"].get(timeout=900)
            _E["pool"].close()
            _E["res"]["arrived_after_s"] = round(time.time() - _E["t0"], 1)
        else:
            _E["res"] = _e_job()
    return _E["res"]


def demand_si(e_sqrt=None, area_power=2):
    """The demand in SI at o3_write.EXAMPLE_N and at item 155's E, with G's uncertainty propagated.  e_sqrt may be
    passed (J per sqrt(bit)) to skip exactE's 70 s owner load; otherwise exactE.e_per_sqrt_bit() is called."""
    O = _owner("o3_write")
    G, c, N = O.G_SI, O.C_SI, O.EXAMPLE_N
    eo = e_owner_values() if e_sqrt is None else {"e_per_sqrt_bit_J": e_sqrt}
    flux = readme_flux_P1(area_power)
    f, k_m = flux["value"], flux["dlog_dlogm"]
    u_G = G_U_CODATA / G
    gE = g_exponent_of_E()["G"]
    rows = {}
    for key, E, gexp in (("N_example", eo["e_per_sqrt_bit_J"] * math.sqrt(N), gE), ("item155", E_ITEM155, 0)):
        mv = G * E / c**4
        inv = float(f.subs(M_SYM, mv)) if f.has(M_SYM) else float(f)
        u_m = float(abs(1 + gexp)) * u_G               # m = G E / c^4 with E ~ G^gexp: m ~ G^(1 + gexp)
        rows[key] = {"E_J": E, "m_geometric_m": mv, "kappa4sq_int_Tvv_per_m": inv,
                     "u_r_m": u_m, "u_r_kappa4sq_int_Tvv": abs(float(k_m)) * u_m,
                     "G_exponent_of_m": str(1 + gexp)}
    return {"rows": rows, "G_SI": G, "c_SI": c, "N": N, "u_r_G_CODATA": u_G,
            "u_r_G_banked_exactE": eo.get("U_R_G_banked"), "u_r_E_banked_chain": eo.get("u_r_E_banked"),
            "E_form": eo.get("form"), "G_exponent_of_E": str(gE),
            "label": "computed; standard-not-READ (CODATA 2018 uncertainty of G); STRUCTURAL (W1)",
            "note": "G and c as banked in o3_write; E from exactE.e_per_sqrt_bit()"}


def reads_beside():
    """The READs set beside the demands, never a supply, and MSY's bound against 122 (4)'s words."""
    return {"reads": READS,
            "msy_vs_122_4": {"label": "deduced; OPEN (reported, not decided)",
                             "M_122_4": M_WORDS["122 (4)"],
                             "MSY": READS[5]["quote"],
                             "text": "MSY bound, parametrically, the information sent through a coupled wormhole by the "
                                     "information transferred to set up the coupling (their (2.21), (2.25)).  M's "
                                     "122 (4) (H-RULES-NOT-INFORMATION) reads 'The rules apply, but do not restrict "
                                     "information'.  If MSY's bound governs the coupling 177 admits, the coupling "
                                     "exchanges about as much as it lets through; if 122 (4) exempts the README, it "
                                     "does not bind.  Not decided here; no number of bits is printed as a supply."},
            "label": "READ (this run, alphaXiv full text, PDF page with printed page)"}


def answer_158_4():
    return {"M_158_4": M_WORDS["158 (4)"],
            "question": "(4) whether the README's energy stays on the plane or is carried into the extra dimension "
                        "(the board's question, 158)",
            "stationary": {"label": "deduced (Lemma S) [FREE]",
                           "text": "nothing net is absorbed: the README's positive null flux and its partner's equal "
                                   "negative flux cancel along every crossed generator; under 183 that is 'never "
                                   "violated' as a pair"},
            "changing": {"label": "deduced; OPEN [PLANE] (Lemma L, not built here)",
                         "text": "into the bulk's Weyl field and the creased bulk horizon (Lemmas L and K): a necessary "
                                 "condition only"}}


# ======================================================================================== X18 frames [FREE given AdS2]
ETA = sp.diag(-1, -1, 1)                                       # (Y^-1, Y^0, Y^1)
T_, S_ = sp.symbols("T sigma", real=True)


def so21_generators(k_coeff=1):
    """J = d_T (rotation in Y^-1, Y^0); B, the boost about the origin (Y^0 <-> Y^1; fixes Y = (1,0,0), i.e. T = 0,
    sigma = pi/2); K, the other boost (Y^-1 <-> Y^1); J +- k K.  k_coeff = 2 is C30a's mutation."""
    J = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    B = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    K = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    return {"J": J, "B_origin": B, "K": K, "J+K": J + k_coeff * K, "J-K": J - k_coeff * K}


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


def _global_Y():
    return sp.Matrix([sp.cos(T_) / sp.sin(S_), sp.sin(T_) / sp.sin(S_), -sp.cos(S_) / sp.sin(S_)])


def global_killing_field(M):
    """The Killing field on global AdS2 (T, sigma) induced by M: xi = h^-1 J^T eta (M Y), J = dY/d(T, sigma), h the
    induced metric; returns xi, h and the tangency residual (J xi - M Y must vanish)."""
    Y = _global_Y()
    Jm = Y.jacobian([T_, S_])
    h = sp.simplify(Jm.T * ETA * Jm)
    xi = sp.simplify(h.inv() * Jm.T * ETA * (M * Y))
    resid = sp.simplify(Jm * xi - M * Y)
    return xi, h, bool(resid == sp.zeros(3, 1))


def boundary_components(xi):
    """xi^T at the two boundaries sigma -> 0+ and sigma -> pi-."""
    return (sp.simplify(sp.limit(xi[0], S_, 0, "+")), sp.simplify(sp.limit(xi[0], S_, sp.pi, "-")))


@functools.lru_cache(maxsize=None)
def generator_classes(k_coeff=1):
    """X18's table: for each generator, the matrix class, the 2D Killing invariant's class (two routes; Q = -tr M^2/2
    checked), the boundary components."""
    rows = {}
    for name, M in so21_generators(k_coeff).items():
        mc = matrix_class(M)
        xi, h, tangent = global_killing_field(M)
        kc = killing_class(h, [T_, S_], list(xi))
        b0, bpi = boundary_components(xi)
        rows[name] = {"matrix": str(M.tolist()), "eigenvalues": mc["eigenvalues"], "in_so21": mc["in_so21"],
                      "class_matrix": mc["class"], "M3_zero": mc["M3_zero"], "M2_zero": mc["M2_zero"],
                      "class_killing_invariant": kc["class"], "Q": str(kc["Q"]),
                      "Q_equals_minus_half_trM2": bool(sp.simplify(kc["Q"] + mc["trM2"] / 2) == 0),
                      "killing_equation": kc["killing"], "tangent": tangent,
                      "xi_T": str(xi[0]), "xi_sigma": str(xi[1]),
                      "component_at_sigma0": b0, "component_at_sigmapi": bpi}
    return rows


U_, V_ = sp.symbols("u v", real=True)
X_, Z_, TT_ = sp.symbols("x z t", positive=True)


@functools.lru_cache(maxsize=None)
def poincare_map(power=2):
    """x = 8/z^power in -(x/2)dt^2 + dx^2/x^2; power = 2 must give 4(-dt^2 + dz^2)/z^2 (Poincare, radius 2).
    power = 1 is a mutation.  Also z(u) from x = u^2 (u > 0)."""
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
    chart), from the Killing invariant.  Default g_vv = -u^2/2 (degenerate); C30b's mutation passes a non-degenerate
    g_vv = -(u^2 - 1/9)/2."""
    gvv = -U_**2 / 2 if gvv is None else gvv
    g = sp.Matrix([[gvv, sp.sqrt(2)], [sp.sqrt(2), 0]])
    kc = killing_class(g, [V_, U_], [1, 0])
    return {"g_vv": str(gvv), "R": str(kc["R"]), "Q": str(kc["Q"]), "class": kc["class"], "killing": kc["killing"],
            "constant": kc["constant"]}


@functools.lru_cache(maxsize=None)
def embedding_generator():
    """d_t of the Poincare chart as an so(2,1) matrix: solve M Y = d_t Y identically, with the Poincare embedding
    Y = ((1 - t^2 + z^2)/(2z), t/z, -(1 + t^2 - z^2)/(2z)) (global sigma = 0 at z = 0: t +- z = tan((T +- sigma)/2))."""
    Y = sp.Matrix([(1 - TT_**2 + Z_**2) / (2 * Z_), TT_ / Z_, -(1 + TT_**2 - Z_**2) / (2 * Z_)])
    hyper = sp.simplify(-Y[0]**2 - Y[1]**2 + Y[2]**2)
    ms = sp.symbols("m0:9")
    M = sp.Matrix(3, 3, ms)
    expr = sp.expand(2 * Z_ * (M * Y - sp.diff(Y, TT_)))
    eqs = []
    for comp in expr:
        eqs += sp.Poly(comp, TT_, Z_).coeffs()
    sol = sp.solve(eqs, ms, dict=True)
    Ms = M.subs(sol[0]) if sol else None
    return {"hyperboloid": str(hyper), "unique": bool(sol and not any(Ms.free_symbols)),
            "matrix": str(Ms.tolist()) if Ms is not None else None, **({} if Ms is None else matrix_class(Ms))}


@functools.lru_cache(maxsize=None)
def ends_map(chart="ingoing"):
    """The throat's EF chart into global AdS2 through the Poincare embedding.  ingoing: t = v + 2 sqrt2/u,
    z = 2 sqrt2/u (sim2_passage X1, continued analytically through u = 0); outgoing (mutation): t = v - 2 sqrt2/u;
    mirror (mutation): z = 2 sqrt2/|u|, t = v + z, u < 0 treated as a copy of patch 1.  Returns smoothness at u = 0,
    the boundary each asymptotic end reaches (cot sigma = -Y^1), the horizon line (cos(T + sigma) = -1: patch 1's
    future horizon and patch 2's past horizon; cos(T - sigma) = -1: patch 1's past horizon), and the patch sign
    Y^-1 - Y^1 (= 1/z) on each side."""
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
            "patch_sign_u_pos": sorted(set(int(s) for s in pp)), "patch_sign_u_neg": sorted(set(int(s) for s in pm))}


@functools.lru_cache(maxsize=None)
def ads2_family_classes(deltas=(sp.Rational(-1, 9), 0, sp.Rational(1, 9))):
    """The AdS2 family -(x/2)dt^2 + dx^2/(x(x - delta)) (radius 2; Bronnikov-Kim's near-throat form on the plane, X19,
    is its [PLANE] reading with delta = r0 - 2m): the invariant of d_t and its class."""
    dl = sp.Symbol("delta", real=True)
    g = sp.Matrix([[-X_ / 2, 0], [0, 1 / (X_ * (X_ - dl))]])
    gen = killing_class(g, [TT_, X_], [1, 0])
    rows = {str(dv): killing_class(g.subs(dl, dv), [TT_, X_], [1, 0])["class"] for dv in deltas}
    return {"Q_general": str(gen["Q"]), "R": str(gen["R"]), "classes": rows}


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
    """(i): S_ab = s eta_ab (+ dust e0 e0, the mutation) read by n exact rational observers u = L e0, for three s."""
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
    pr_sign = -1 is C31b's mutation (p_r's sign flipped)."""
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


@functools.lru_cache(maxsize=None)
def nec_rows(n=1000, seed=5, nec=1):
    """(ii)'s control: n exact rational (rho, p, v) with rho + p >= 0 (nec = 1) or < 0 (nec = -1, the mutation):
    is the boosted density >= rho for all of them?"""
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


T_SAMPLES = [sp.pi * k / 6 for k in (0, 1, 2, 4, 5, 6, 7, 8, 10, 11)]      # cos T != 0


@functools.lru_cache(maxsize=None)
def killing_charge_flip(use="xi.n"):
    """(iii): at each boundary the charge density read by the future unit normal n = sin(sigma) d_T of T = const,
    rescaled: q_b = lim sin(sigma) (-g(xi, n)); use = 'xi.xi' (the mutation) reads lim sin^2(sigma) g(xi, xi)
    instead.  Flip at T: q_0 q_pi < 0."""
    out = {}
    gens = so21_generators()
    for name in ("B_origin", "J+K", "J-K", "J"):
        xi, h, _ = global_killing_field(gens[name])
        nvec = sp.Matrix([sp.sin(S_), 0])
        if use == "xi.n":
            dens = sp.simplify(sp.sin(S_) * (-(xi.T * h * nvec)[0]))
        else:
            dens = sp.simplify(sp.sin(S_)**2 * (xi.T * h * xi)[0])
        q0, qpi = sp.simplify(sp.limit(dens, S_, 0, "+")), sp.simplify(sp.limit(dens, S_, sp.pi, "-"))
        flips = [bool((q0 * qpi).subs(T_, tv) < 0) for tv in T_SAMPLES]
        out[name] = {"q_sigma0": str(q0), "q_sigmapi": str(qpi), "flips_at_all_samples": all(flips),
                     "flips_at_some_sample": any(flips)}
    return out


def lemma_p(n=1000, seed=5):
    """Lemma P: (i) delta-stress density, (ii) eq. (17)'s Weyl fluid under boosts [PLANE]-conditional, (iii) the
    Killing-charge flip."""
    i = delta_stress_rows(n, seed)
    fl = eq17_fluid("3")
    vs = v_star(fl["8pi_rho"], fl["8pi_p_r"])
    vv = sp.Symbol("v", positive=True)
    lim1 = sp.limit(boosted_density(fl["8pi_rho"], fl["8pi_p_r"], vv), vv, 1, "-")
    return {
        "i_delta_stress": {"rows": i, "label": "computed (exact rationals)", "tag": "[FREE]"},
        "ii_weyl_fluid": {"fluid": {k: str(vv_) for k, vv_ in fl.items()}, "v_star": str(vs),
                          "v_star_is_one_over_sqrt3": bool(vs is not None and sp.simplify(vs - 1 / sp.sqrt(3)) == 0),
                          "rapidity_star": float(sp.atanh(vs)) if vs is not None else None,
                          "rho_prime_limit_v_to_1": str(lim1), "nec_control": nec_rows(n, seed),
                          "label": "computed (exact)",
                          "tag": "[PLANE]-conditional: under 179 eq. (17) is at most a plane's reading of the "
                                 "corridor's mouth (H-PLANE-READS-MOUTH, the board's); under 184 its vacuum-brane Weyl "
                                 "fluid is a matter-free plane's reading, a limit only",
                          "note": "v is an observer's boost parameter, never a speed (139 (4), 101 (7))"},
        "iii_charge_flip": {"rows": killing_charge_flip("xi.n"), "label": "computed", "tag": "[FREE given AdS2]"},
    }


def deduced_x18(fam=None):
    fam = ads2_family_classes() if fam is None else fam
    return {
        "s15_delta_stress": {"label": "deduced (from (i) and SIM2-FACING S15, computed there)", "tag": "[FREE]",
                             "text": "At coincidence position 2's surface stress tends to S^a_b = +sigma_RS delta^a_b "
                                     "(rho = -sigma_RS; its matter part, our tension subtracted, rho_m = -2 sigma_RS, is "
                                     "also of delta form).  By (i) every observer tangent to the sheet reads the same "
                                     "negative density: no observer's frame makes it positive.  Along the approach "
                                     "(and under 184, with matter) the non-delta parts transform as (ii) computes."},
        "refutes_176_sentence": {"label": "deduced (from (i) and (iii)); READ (GJW PDF p.4; MQ PDF p.64)", "tag": "[FREE]",
                                 "board_sentence": "position 2's -1 would be the partner's sign seen from our side",
                                 "text": "Refuted for this object: the coincident -sigma_RS is frame-invariant (i), and "
                                         "the corridor's generator is parabolic, whose Killing charge does not flip "
                                         "between the boundaries (iii); the thermofield-double sign reading needs the "
                                         "hyperbolic boost about the origin, whose directions are opposite in the two "
                                         "wedges (GJW PDF p.4; MQ PDF p.64)."},
        "extremal_member": {"label": "computed (classes); READ (properties); deduced (extremal)", "tag": "[FREE given "
                            "AdS2]; the delta = r0 - 2m identification is [PLANE] (X19)", "family": fam,
                            "text": "On -(x/2)dt^2 + dx^2/(x(x - delta)) the invariant of d_t is Q = delta/8: delta < 0 "
                                    "hyperbolic (Rindler/thermal: the thermofield double; no passage, MQ PDF p.7), "
                                    "delta = 0 parabolic (Poincare: the corridor's d_v), delta > 0 elliptic (global: "
                                    "MQ's coupled wormhole; no horizon, MQ PDF p.53; two-way, MQ PDF p.3).  The "
                                    "corridor is the extremal member, delta = 0, between the two."},
        "end2_identification": {"label": "OPEN", "reading": "H-END-2-IS-OUR-FAR-END (the board's)",
                                "text": "The map computes that u < 0 is the Poincare patch on the other boundary. That "
                                        "this end is our own plane's far end, within one universe, is a global "
                                        "identification no instrument here computes (RI-6/PA-6): the board's reading, "
                                        "OPEN."},
        "positive_in_own_frame": {"label": "deduced (from (ii)'s computed limit)", "reading": "H-POSITIVE-IN-OWN-FRAME "
                                  "(the board's, spec 4.3)",
                                  "text": "Where rho + p < 0 the boosted density is unbounded below as v -> 1, so 139 "
                                          "(2)'s 'positive' can be met only as each piece's own-frame density; a "
                                          "delta-stress (i) is the same in every frame, so S15's coincident sheet "
                                          "cannot meet it in any frame."},
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


def label_audit(obj, reads=None):
    """Every dict carrying 'label' uses only the six labels; every READ has a page."""
    bad = []

    def walk(o, path):
        if isinstance(o, dict):
            if "label" in o:
                lab = str(o["label"])
                while re.search(r"\([^()]*\)", lab):
                    lab = re.sub(r"\([^()]*\)", "", lab)
                parts = [p.strip().split(" ")[0] for p in lab.split(";")]
                if not parts or any(p not in LABELS for p in parts if p):
                    bad.append((path, o["label"]))
            for k, vv in o.items():
                walk(vv, path + "/" + str(k))
        elif isinstance(o, list):
            for i, vv in enumerate(o):
                walk(vv, path + "[%d]" % i)
    walk(obj, "")
    reads = READS if reads is None else reads
    nopage = [r["id"] for r in reads if r.get("status") == "READ" and not r.get("page")]
    return {"bad_labels": bad, "reads_without_page": nopage}


# ======================================================================================== compute and checks
def compute(e_sqrt=None):
    fam = ads2_family_classes()
    out = {
        "_note": "epass_frames.py (E-PASS fix round, [FREE] owner): computed, READ and deduced; not verified; not "
                 "seated; 2026-10-09",
        "X17": {
            "readme_flux_P1": {**{k: str(vv) for k, vv in readme_flux_P1().items()},
                               "label": "computed (sympy); STRUCTURAL (W1: E = mc^2 of the hole of N bits)",
                               "tag": "[FREE] sheet form, P1's normalisation"},
            "stationary_demand": stationary_demand(),
            "demand_si": demand_si(e_sqrt),
            "reads_beside": reads_beside(),
            "answer_158_4": answer_158_4(),
            "changing_half": {"label": "OPEN", "text": "Lemma L (the 5.912... coefficients) is [PLANE]; not built "
                                                       "in this [FREE] module"},
        },
        "X18": {
            "generator_classes": {"rows": generator_classes(), "label": "computed", "tag": "[FREE given AdS2]"},
            "poincare_map": {**poincare_map(), "label": "computed"},
            "throat_generator": {**throat_generator(), "label": "computed"},
            "embedding_generator": {**{k: str(vv) for k, vv in embedding_generator().items()}, "label": "computed"},
            "ends_map": {**ends_map("ingoing"), "label": "computed; deduced (122 (3), 132)"},
            "lemma_p": lemma_p(),
            "deduced": deduced_x18(fam),
        },
        "M_words": M_WORDS,
    }
    return out


def _json_default(o):
    if isinstance(o, (sp.Basic, Fr)):
        return str(o)
    return repr(o)


# Each check: (name, description, function(mut) -> (ok, detail), [mutation names]).  Every check calls this module's
# computing function on the (possibly mutated) input; none compares a constant to itself.
def chk_c26a(mut=None):
    r = readme_flux_P1(area_power=1 if mut == "r^2->r" else 2)
    ok = r["equals_one_over_2m"] and r["r_h_over_m"] == 2 and r["r_h_over_m_schwarzschild_control"] == 2
    return ok, "kappa4^2 int T_vv dv = %s per generator (r_h = %sm)" % (r["value"], r["r_h_over_m"])


def chk_c26b(mut=None):
    d = demand_si(area_power=1 if mut == "r^2->r" else 2)
    N, I = d["rows"]["N_example"], d["rows"]["item155"]
    got = {"E_N_J": N["E_J"], "m_N": N["m_geometric_m"], "inv2m_N": N["kappa4sq_int_Tvv_per_m"],
           "m_155": I["m_geometric_m"], "inv2m_155": I["kappa4sq_int_Tvv_per_m"]}
    rel = {k: abs(got[k] / SI_EXPECTED[k] - 1) for k in SI_EXPECTED}
    ok = max(rel.values()) <= SI_TOL
    return ok, "E = %.6e J, m = %.6e m, 1/(2m) = %.6e m^-1; E = 3.8e22 J: m = %.6e m, 1/(2m) = %.6e m^-1; max rel " \
               "dev %.1e; u_r: %.3e (N example), %.3e (fixed E)" % (
                   got["E_N_J"], got["m_N"], got["inv2m_N"], got["m_155"], got["inv2m_155"], max(rel.values()),
                   N["u_r_kappa4sq_int_Tvv"], I["u_r_kappa4sq_int_Tvv"])


def chk_c26c(mut=None):
    reads = [dict(r) for r in READS]
    if mut == "altered-quote":
        reads[5]["fragment"] = reads[5]["fragment"].replace("more information", "less information")
    f = reads_found(reads)
    return all(f.values()), "%d/%d READ fragments verbatim in the design-stage file and in this run's quote%s" % (
        sum(f.values()), len(f), "" if all(f.values()) else ": missing " + ", ".join(k for k, vv in f.items() if not vv))


def chk_c26d(mut=None):
    g = g_exponent_of_E(dims=(1, 3, -2) if mut == "E-as-J*m" else (1, 2, -2))["G"]
    eo = e_owner_values()
    ok = abs(abs(float(g)) * eo["U_R_G_banked"] - eo["u_r_E_banked"]) < 1e-12 and g != 0
    return ok, "E ~ G^%s (dimensional analysis); |g| u_r(G)_banked = %.2e against chain's banked u_r(E) = %.2e" % (
        g, abs(float(g)) * eo["U_R_G_banked"], eo["u_r_E_banked"])


def chk_c30a(mut=None):
    rows = generator_classes(k_coeff=2 if mut == "J+2K" else 1)
    st, ct = sp.sin(T_), sp.cos(T_)
    expect = {"J": ("elliptic", 1, 1), "B_origin": ("hyperbolic", -ct, ct), "K": ("hyperbolic", st, -st),
              "J+K": ("parabolic", 1 + st, 1 - st), "J-K": ("parabolic", 1 - st, 1 + st)}
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
    return ok, "; ".join("%s %s/%s (%s, %s)" % (k, rows[k]["class_matrix"], rows[k]["class_killing_invariant"],
                                                  rows[k]["component_at_sigma0"], rows[k]["component_at_sigmapi"])
                         for k in rows) + ("" if ok else "  FAILED: " + ", ".join(bad))


def chk_c30b(mut=None):
    pm = poincare_map(power=1 if mut == "x=8/z" else 2)
    th = throat_generator(-(U_**2 - sp.Rational(1, 9)) / 2 if mut == "non-degenerate-gvv" else None)
    em = embedding_generator()
    ok = pm["is_poincare_radius2"] and th["class"] == "parabolic" and th["killing"] and th["constant"] and \
        em["unique"] and em["class"] == "parabolic" and em["in_so21"]
    return ok, "x = 8/z^2 Poincare: %s (z = %s); throat d_v [g_vv = %s]: Q = %s, %s; embedding d_t: %s, %s" % (
        pm["is_poincare_radius2"], pm["z_of_u"], th["g_vv"], th["Q"], th["class"], em["matrix"], em["class"])


def chk_c30c(mut=None):
    chart = {"outgoing-chart": "outgoing", "mirror-identification": "mirror"}.get(mut, "ingoing")
    e = ends_map(chart)
    ok = (e["smooth_through_u0"] and e["end1_boundary"] == "sigma=0" and e["end2_boundary"] == "sigma=pi"
          and e["u0_is_patch1_future_horizon"] and e["patch_sign_u_pos"] == [1] and e["patch_sign_u_neg"] == [-1])
    return ok, "%s chart: smooth %s; end 1 on %s, end 2 on %s; u = 0: cos(T+s) = %s, cos(T-s) = %s (future horizon " \
               "of patch 1: %s); patch signs %s / %s" % (
                   chart, e["smooth_through_u0"], e["end1_boundary"], e["end2_boundary"], e["cos_T_plus_sigma_at_u0"],
                   e["cos_T_minus_sigma_at_u0"], e["u0_is_patch1_future_horizon"], e["patch_sign_u_pos"],
                   e["patch_sign_u_neg"])


def chk_c31a(mut=None):
    rows = delta_stress_rows(1000, 5, dust=Fr(1, 3) if mut == "dust-added" else Fr(0))
    ok = all(r["all_equal_minus_s"] and r["lorentz_exact"] for r in rows.values())
    return ok, "; ".join("s = %s: %d distinct densit%s %s" % (s, r["n_values"], "y" if r["n_values"] == 1 else
                                                             "ies", r["densities"]) for s, r in rows.items())


def chk_c31b(mut=None):
    fl = eq17_fluid("3", pr_sign=-1 if mut == "p_r-sign-flipped" else 1)
    vs = v_star(fl["8pi_rho"], fl["8pi_p_r"])
    ok = (vs is not None and sp.simplify(vs - 1 / sp.sqrt(3)) == 0 and fl["8pi_rho"] == sp.Rational(1, 81)
          and fl["8pi_rho_plus_p_r"] == sp.Rational(-2, 81) and fl["agrees_with_owner"])
    rap = float(sp.atanh(vs)) if vs is not None else float("nan")
    ok = ok and abs(rap - 0.658479) < 5e-7
    return ok, "8 pi rho_W = %s, 8 pi (rho_W + p_r) = %s (owner R_rad %s); v* = %s, rapidity %.6f" % (
        fl["8pi_rho"], fl["8pi_rho_plus_p_r"], fl["owner_R_rad_sim2_facing"], vs, rap)


def chk_c31c(mut=None):
    r = nec_rows(1000, 5, nec=-1 if mut == "NEC-violating" else 1)
    return r["all_rho_prime_ge_rho"], "rho' >= rho for all 1000: %s (least rho' - rho = %s)" % (
        r["all_rho_prime_ge_rho"], r["least_rho_prime_minus_rho"])


def chk_c31d(mut=None):
    f = killing_charge_flip("xi.xi" if mut == "xi.xi-for-xi.n" else "xi.n")
    ok = f["B_origin"]["flips_at_all_samples"] and not any(f[k]["flips_at_some_sample"] for k in ("J+K", "J-K", "J"))
    return ok, "; ".join("%s: (%s, %s) flips %s" % (k, r["q_sigma0"], r["q_sigmapi"], r["flips_at_some_sample"])
                         for k, r in f.items())


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
    words = dict(M_WORDS)
    if mut == "altered-M-quote":
        words["183"] = words["183"].replace("never violated", "never broken")
    f = m_words_verbatim(words)
    return all(f.values()), "%d/%d quotes verbatim in M-RULINGS-2026-10-03.md%s" % (
        sum(f.values()), len(f), "" if all(f.values()) else ": not found " + ", ".join(k for k, vv in f.items() if not vv))


def chk_g3(mut=None):
    obj = json.loads(json.dumps(_output(), default=_json_default))
    reads = [dict(r) for r in READS]
    if mut == "planted-label":
        obj = {"planted": {"label": "verified"}, **obj}
    if mut == "READ-without-page":
        reads[0]["page"] = ""
    a = label_audit(obj, reads)
    ok = not a["bad_labels"] and not a["reads_without_page"]
    return ok, "bad labels %s; READs without a page %s" % (a["bad_labels"][:3], a["reads_without_page"])


CHECKS = [
    ("C26a", "1/(2m) exact per generator on P1 (readme_flux_P1)", chk_c26a, ["r^2->r"]),
    ("C26b", "SI demands to 1e-5 relative (demand_si; exactE and o3_write by path)", chk_c26b, ["r^2->r"]),
    ("C26c", "READ fragments verbatim in spec sec. 10 / epass_ground.json and in this run's quotes", chk_c26c,
     ["altered-quote"]),
    ("C26d", "E's G-exponent (dimensional analysis) against chain.py's banked u_r(E): G's uncertainty carried",
     chk_c26d, ["E-as-J*m"]),
    ("C30a", "so(2,1) classes and boundary components, two routes", chk_c30a, ["J+2K"]),
    ("C30b", "x = 8/z^2 gives Poincare; the throat's d_v is parabolic (EF invariant and embedding matrix)", chk_c30b,
     ["non-degenerate-gvv", "x=8/z"]),
    ("C30c", "ends: u > 0 on sigma = 0, u < 0 on sigma = pi, u = 0 patch 1's future / patch 2's past horizon",
     chk_c30c, ["outgoing-chart", "mirror-identification"]),
    ("C31a", "1000 exact boosts preserve the delta-stress density -s", chk_c31a, ["dust-added"]),
    ("C31b", "eq. (17)'s Weyl fluid at r = 3m: v* = 1/sqrt3 exactly, rapidity 0.658479", chk_c31b,
     ["p_r-sign-flipped"]),
    ("C31c", "NEC-obeying matter: rho' >= rho for 1000 exact boosts", chk_c31c, ["NEC-violating"]),
    ("C31d", "the Killing charge flips under the boost about the origin, not under the parabolic generators",
     chk_c31d, ["xi.xi-for-xi.n"]),
    ("G1", "keys and argument names avoid BANNED_KEYS / BANNED_ARGS (names only)", chk_g1,
     ["planted-key-hold_time", "planted-arg-gap"]),
    ("G2", "M's words verbatim in the rulings file", chk_g2, ["altered-M-quote"]),
    ("G3", "every labelled row uses the six labels; every READ has a page", chk_g3,
     ["planted-label", "READ-without-page"]),
]


NEEDS_E = {"C26b", "C26d", "G1", "G3"}          # need exactE's owner value (G1, G3 audit compute()'s full output)


def _ordered():
    """Checks that need exactE's 70 s owner value run last, so its forked load overlaps the others."""
    return [c for c in CHECKS if c[0] not in NEEDS_E] + [c for c in CHECKS if c[0] in NEEDS_E]


def _warm():
    """Everything compute() needs except exactE's value, computed before the E-dependent checks wait on it."""
    stationary_demand()
    lemma_p()
    ads2_family_classes()
    embedding_generator()
    reads_beside()


def selftest():
    t0 = time.time()
    start_e_background()
    n_ok = 0
    for name, desc, f, _ in _ordered():
        if name in NEEDS_E and "warm" not in _E:
            _warm()
            _E["warm"] = True
        try:
            ok, detail = f()
        except Exception as ex:
            ok, detail = False, "EXCEPTION %r" % ex
        n_ok += bool(ok)
        print("[%s] %s %s -- %s" % ("PASS" if ok else "FAIL", name, desc, detail), flush=True)
    print("selftest: %d/%d passed in %.1f s (exactE's owner value arrived after %s s, from a forked child)" % (
        n_ok, len(CHECKS), time.time() - t0, _E.get("res", {}).get("arrived_after_s")), flush=True)
    return n_ok == len(CHECKS)


def mutants():
    t0 = time.time()
    start_e_background()
    total, caught = 0, 0
    for name, desc, f, muts in _ordered():
        if name in NEEDS_E and "warm" not in _E:
            _warm()
            _E["warm"] = True
        for m in muts:
            total += 1
            try:
                ok, detail = f(mut=m)
            except Exception as ex:
                ok, detail = False, "EXCEPTION %r (counts as failing)" % ex
            caught += not ok
            print("[%s] %s under mutation '%s' -- %s" % ("FAILS (good)" if not ok else "PASSES (BAD)", name, m, detail),
                  flush=True)
    print("mutants: %d/%d mutations make their check fail, in %.1f s (exactE's owner value arrived after %s s)" % (
        caught, total, time.time() - t0, _E.get("res", {}).get("arrived_after_s")), flush=True)
    return caught == total


def report(o):
    x17, x18 = o["X17"], o["X18"]
    print("epass_frames.py -- %s" % o["_note"])
    print("X17 readme_flux_P1: kappa4^2 int T_vv dv = %s per generator (r_h = %sm) [%s]" % (
        x17["readme_flux_P1"]["value"], x17["readme_flux_P1"]["r_h_over_m"], x17["readme_flux_P1"]["label"]))
    sd = x17["stationary_demand"]
    print("  stationary demand: %s; pair net %s (%s)" % (sd["sheet_form"]["statement"], sd["pair_net_per_generator"],
                                                         sd["pair_net_reading"]))
    print("  Lemma S owner: %s" % {k: vv for k, vv in sd["lemma_s"].items() if k != "pointer"})
    for k, r in x17["demand_si"]["rows"].items():
        print("  %s: E = %.6e J, m = %.6e m, 1/(2m) = %.6e m^-1, u_r = %.3e" % (
            k, r["E_J"], r["m_geometric_m"], r["kappa4sq_int_Tvv_per_m"], r["u_r_kappa4sq_int_Tvv"]))
    for name, r in x18["generator_classes"]["rows"].items():
        print("X18 %-9s %-10s eig %s, components (%s, %s), Q = %s" % (
            name, r["class_matrix"], r["eigenvalues"], r["component_at_sigma0"], r["component_at_sigmapi"], r["Q"]))
    print("  throat d_v: %s (Q = %s); embedding d_t %s; ends: %s" % (
        x18["throat_generator"]["class"], x18["throat_generator"]["Q"], x18["embedding_generator"]["class"],
        {k: x18["ends_map"][k] for k in ("end1_boundary", "end2_boundary", "u0_is_patch1_future_horizon")}))
    lp = x18["lemma_p"]
    print("  Lemma P (ii): v* = %s, rapidity %.6f, rho' -> %s as v -> 1" % (
        lp["ii_weyl_fluid"]["v_star"], lp["ii_weyl_fluid"]["rapidity_star"], lp["ii_weyl_fluid"]["rho_prime_limit_v_to_1"]))
    print("  AdS2 family: %s" % x18["deduced"]["extremal_member"]["family"])


def main(argv):
    ok = True
    if "--selftest" in argv or "--mutants" in argv:
        start_e_background()
    if "--selftest" in argv:
        ok = selftest() and ok
    if "--mutants" in argv:
        ok = mutants() and ok
    if "--json" in argv:
        start_e_background()
        path = argv[argv.index("--json") + 1]
        with open(path, "w") as fh:
            json.dump(_output(), fh, indent=1, default=_json_default)
        print("wrote %s" % path)
    if not any(a in argv for a in ("--selftest", "--mutants", "--json")):
        start_e_background()
        report(json.loads(json.dumps(_output(), default=_json_default)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
