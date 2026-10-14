#!/usr/bin/env python3
"""readme_held.py -- items 195 and 196: is the README HELD by the corridor's horizon rather than crossing it, and does
it come in while that horizon forms or across one that already has its size?  Computed, READ and deduced; worked, put
through the cypher, then checked by a refute verifier and an overclaim verifier (each a separate AI session in this
project, not an outside review); their findings reproduced and applied; not seated; 2026-10-10.

PLAIN WORDS FIRST.
  M said in 195: "The README is not a pair".  The board's note under 195 (the board's reading, not M's words) asked
  whether the README is then HELD by the corridor's horizon -- its N bits the horizon's area (H1), its energy the
  horizon's mass (G1) -- RATHER THAN CROSSING it, so that Lemma S asks no partner; and whether that survives R0, 160,
  162 and 163.  This instrument computes both halves and puts them to the cypher (196).
  (1) HELD RATHER THAN CROSSING: NO, in every model computed here (stated plainly, 135).  In the 4D Vaidya family
      ([4D-VAIDYA], standard-not-READ) every shell of the README's null dust crosses the event horizon (EH).  For a
      compact inflow the EH is born 3.5 m before the README begins and already has 0.77 N A_bit when it does; 100% of
      the README's energy comes in across it, and every shell also crosses the trapping horizon r = 2M(v) at its own v.
      Lemma S asks no partner because that horizon GROWS (theta > 0 throughout; bulk form, [FREE]), not because the
      README is held.  'Held' survives only as H1/G1's count of the END state: once the README is in, the horizon's
      area is its N bits and its mass is E.  That end state is vacuum Schwarzschild, not a held stress on eq. (17).  The
      held-stress zero (a regular AdS2-invariant stress has T(xi,xi) = 0, owner Lemma S (a)) is a separate [PLANE]
      result that no computed formation reaches (S4: eq. (17) is no static end state of NEC inflow in one spacetime).
      What survives is the board's H-ARRIVAL-FORMS-THE-HORIZON: the README crosses the horizon it forms.
  (2) WHEN IT COMES IN.  Along a horizon that keeps its size theta = 0, and Raychaudhuri gives R(k,k) = -sigma^2 <= 0
      (geometric; read as energy only under the bulk's field equation, R_kk = kappa^2 T_kk): a net inflow cannot come in
      there (owner Lemma S, bulk form, [FREE]; SIM1 S3b).  Two ways in, and no third:
        (a) the README comes in WHILE its horizon forms: the horizon ends at N A_bit and mass E, the README the whole
            mass, theta > 0 throughout, no partner (computed: one C^2 quintic onset at widths 1 m and the write floor;
            the first build's C^1 cubic kept for comparison);
        (b) it crosses a horizon that ALREADY has its size: without a partner it ends at 4 N A_bit and 2E (computed),
            breaking H1, G1 and 133; with the exact partner the size stays fixed but the README's share of the mass is
            0, and the README is one member of a +/- pair.  M admitted that pair in 183 ("Yes: never violated as a
            pair").  Closing it rests on the board's reading of 195 as "not one member of a pair"
            (H-README-NOT-ONE-MEMBER), or on the board's share-1 reading of 136 G / 190.  M has not ruled that 195
            supersedes 183.
      (b) without a partner is closed by computation with H1, G1 and 133.  (b) with the partner is closed only on a board
      reading.  (a) is consistent in a 4D Vaidya model that ends in Schwarzschild, not in eq. (17) (S4) and not in the
      bulk corridor (179: formation in the bulk OPEN).
  WHAT (a) COSTS (135).
    - Which horizon.  On the trapping horizon of a compact inflow the size grows from nothing to the README's over the
      inflow's width (5.0e-6 of the write at 1 m) and holds f^2 N bits at a fraction f of E: only whole, which the board
      reads as 163's "one whole" (H-WHOLE-AS-G1).  On the event horizon of the same inflow a horizon of 0.77 N A_bit
      already stands when the README begins, born 3.5 m before any of it (against 109 if its object is read as the
      README), and its area runs AHEAD of f N.  On the event horizon of a spread inflow the area is f^2 N again, but the
      size changes over the whole write.  "One whole" together with 162's small cost holds only on the trapping
      horizon of a compact inflow (H-SIZE-IS-TRAPPING-HORIZON, the board's).
    - 162's "doesn't change size" holds from the moment the whole README is in.  M's 86 (5), 94 and 136 E bear on the
      duration ("incredibly short, maybe even immeasurable but not zero"; "instantaneously relative to the object
      teleporting"; "Instantaneous or near instantaneous") and favour a compact inflow (the board's reading).  94's
      "grows in size" pulls against 162 read strictly.  163's "All together, one whole" defines a word and rules nothing
      on duration.
    - 163's option text ("at the fixed size; the write lasts at least ~200,000 clocks; B4d must keep the fixed-size
      corridor regular for that long") is the board's wording, and M chose the option carrying it.  It is (b)'s framing
      and does not survive (a); whether M's choice endorsed that text is for M.
    - The gas bound (O3-WRITE W3).  W4 (ii) made it the opening's duration: a spread inflow.  Read instead as a lead
      before a compact crossing (H-GAS-BOUND-AS-LEAD, new, the board's), the README converges for ~2e5 clocks with no
      horizon, which sits uneasily with 160 and 70.  The small 162 cost holds only if a compact converging shell can
      carry N bits (OPEN); otherwise W4 (ii)'s spread inflow applies.
    - The closing.  "No partner" is shown for the inflow only.  The horizon's ending (109, 115 (a), 136 (2)) and the
      hold's move from horizon 1 to horizon 2 (106, E1) need its area to DECREASE, which the NEC forbids (the area
      theorem, standard-not-READ).  A negative null flux, or a non-classical mechanism, is demanded there (OPEN).
  The Vaidya figures are four-dimensional.  Under 179 the corridor is in the 5D bulk, where a static horizon's area grows
  as M^(3/2) (Tangherlini, standard-not-READ): (b) without a partner then ends at 2.83 N A_bit, still not N, and a
  forming horizon holds f^(3/2) N bits at a fraction f, still short of f N.

THE CYPHER (196; §33; tools/cypher.py imported by path, registered in sys.modules before exec_module).  Roster 1173
(order, algebra, analysis, geometry, information, statistics, documentary); logic is the mechanism that returns each
language's binary.  The index is the board's encoding (H-CYPHER-README-HELD-INDEX): nine ordinal coordinates, twelve
cells from the Vaidya family (pre-existing horizon or not; partner 0, 1/2, 1; compact or spread inflow) plus one
ASSIGNED held cell (the forming run's end state: nothing coming in, nothing crossing, the README the whole mass).
What each coordinate is: pre, partner and spread are configuration labels; mass_E, share and net are arithmetic on the
labels (mass additivity); area_N is the Birkhoff end state, (pre + net)^2 by construction from the integration's start;
moves and crosses are MEASURED on the integrated event horizon (the span over which its size changes; whether the
README's energy arrives where it already exists).  So the cypher's NOs read back the energy balance, Birkhoff's
area = mass^2 and Raychaudhuri as measured on the EH, and classify them; they derive nothing.  Its verdicts are
invariant under the partner-sign, area-law and 5D worlds (ordinal invariance, computed).  A target admitted because it
is itself a computed cell is said to be so (extensivity).  A NO is STRUCTURAL where a value or a pair of values the
target needs is never seen.  analysis answers only with a declared witness, and its state is COMPUTED from that
witness's residual on every cell.  documentary returns citations, not a binary.  NOT-RUN is never SILENT.
CONTROLS.  (i) The test-event world: every configuration re-integrated with the README carrying no gravity (RI-5's
framing as a law, not a planted cell); it must flip what the law index says.  (ii) A negative control: the lawful
computed run pre = 1/2 added; it must flip nothing.  (iii) The first build's planted test-event cell, kept for
comparison only: it is the T_GLOSS target itself and cannot fail, so its one informative flip is T_STRICT.

LABELS.  computed / READ (verbatim + page) / deduced / STRUCTURAL / standard-not-READ / OPEN.  The board's readings are
named H-... and kept apart from M's words, which are quoted verbatim (typing kept) and checked inside their own item.
Tags: [FREE] holds whatever carries the corridor; [PLANE] uses eq. (17) as a plane's own metric (the board's pre-179
configuration; under 179/180 and seated (G), at most a plane's reading of the mouth, OPEN); [4D-VAIDYA] the standard
spherically symmetric null-dust family (standard-not-READ) used as the plainest model of an inflow, units m = 1 where
m = G E/c^4 is the README's (G1); "G1 as seated (4D)" marks a result that uses G1's 4D form.  No key or argument names a
separation, a distance, a speed or a redshift (139 (4), 101 (7)); the advanced coordinate v is called v and widths are
fractions of the write.

M'S WORDS USED (verbatim, typing kept; checked inside their own items, check C10): see M_WORDS.  The board's wording in
163's option, which M chose, is quoted under a key that says it is the board's (BOARD_WORDS), never as M's.

READ (verbatim, transliterated to ASCII):
  Kehle & Unger, "Gravitational collapse to extremal black holes and the third law of black hole thermodynamics",
  arXiv:2211.15742v2, PDF p.1 (abstract): "We construct examples of black hole formation from regular, one-ended
  asymptotically flat Cauchy data for the Einstein-Maxwell-charged scalar field system in spherical symmetry which are
  exactly isometric to extremal Reissner-Nordstrom after a finite advanced time along the event horizon."  and "In
  particular, our result can be viewed as a definitive disproof of the "third law of black hole thermodynamics.""
  Read 2026-10-09 through the alphaXiv connector (full text served; the abstract, title page and contents were read,
  not the whole paper; confirmed by the overclaim verifier).  Bearing: a horizon formed by collapse CAN be exactly
  extremal after a finite advanced time -- a precedent beside reading (a), never a supply; it is Reissner-Nordstrom
  (charge), not eq. (17).
  standard-not-READ: the Vaidya metric; Raychaudhuri's equation; Birkhoff; the event horizon's teleology; the area
  theorem (an event horizon's area never decreases under the NEC); Tangherlini's 5D area law.

OWNERS IMPORTED BY PATH, NEVER COPIED: lemmas/epass_pairing.py (horizon_stress_eq17, readme_flux, pairing_bulk,
pairing_sheet, bulk_gvv, sheet_gvv, EPS, _eq17_ingoing, its geometry engine _connection/_riemann, BANNED_KEYS,
BANNED_ARGS; sim2_facing's eq. (17) and Schwarzschild data through it), lemmas/epass_frames.py (readme_flux_P1,
m_words_verbatim), lemmas/o3_write.py (m_squared, t_min, _num, EXAMPLE_N, w1), tools/cypher.py (Index, ADMISSION,
run, coordinate_report).  sim2_passage.py is never imported (another run edits it).

CLI:  --selftest (every check, each able to fail)   --mutants (every named mutation must make its check FAIL; exit 1
      if one passes)   --json PATH (compute(), every row labelled)   no flag: prints the report.
Stdlib + sympy + numpy + scipy; python 3.11.
"""
import argparse
import contextlib
import importlib.util
import inspect
import io
import json
import math
import os
import re
import sys
import time as _wall
from collections import defaultdict
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")


def _load(path, key):
    """Import an owner by path; the module is registered in sys.modules before exec_module (dataclass needs it)."""
    if key in sys.modules:
        return sys.modules[key]
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod
    finally:
        sys.path[:] = saved


P = _load(os.path.join(HERE, "epass_pairing.py"), "readme_held_pairing")
F = _load(os.path.join(HERE, "epass_frames.py"), "readme_held_frames")
O = _load(os.path.join(HERE, "o3_write.py"), "readme_held_o3write")
CY = _load(os.path.join(REPO, "tools", "cypher.py"), "readme_held_cypher")
BANNED_KEYS = tuple(P.BANNED_KEYS)
BANNED_ARGS = set(P.BANNED_ARGS)
OPB = ("order", "algebra", "geometry", "information", "statistics")   # measured operator-bearing on these indexes

# ============================================================================================ M's words (verbatim)
M_WORDS = {
    "70": "We do not feed the corridor, it takes the information it requires as a natural condition of its "
          "opening...such as with a horizon",
    "86 (5)": "5 - however long is dictated for the travel. I suspect it is incredibly short, maybe even immeasurable "
              "but not zero.",
    "94": "Size does not mean more channels. The corridor is a single channel that grows in size to accommodate the "
          "size of the README.",
    "94 (instantaneous)": "it is a teleportation that happens instantaneously relative to the object teleporting, AND "
                          "all observers of the same dimension of that objects existence",
    "101 (6)": "6 - this is a duty of the device, assess the README size and widen the corridor to the necessary size, "
               "no more and no less.",
    "106 (b)": "Three distinct holds in one fluid wave motion, horizon position 1 only as the corridor opens, when the "
               "corridor is fully realized the bits are held on both horizons simultaneously because the corridor "
               "builds position 2 with the bits in mind, upon the corridor closing the bits are then held only at the "
               "horizon of position 2.",
    "109": "A horizon cannot exist without the object of which it needs to exist",
    "115 (a)": "\"It ends; energy moved\"",
    "115 (b)": "\"When fully realized\"",
    "115 (c)": "\"The README itself\"",
    "129 (1)": "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because "
               "the corridor is a bridge, so it adds nothing to either position.",
    "130 (1)": "1 - i - no added matter. And in my model a black hole is not matter, it is what the mouth at position 1 "
               "looks like.",
    "131 (2)": "2 - the throat size only needs to carry the binary information defining the object in transit",
    "132": "yes. And the passage is one way by nature, a black hole in and a white hole out, side views of the same "
           "corridor object",
    "132 (correction)": "*different views of the same object",
    "133 (2)": "there is no minimum or maximum energy needed. There is only one exact energy needed for any given README",
    "136 (2)": "2 - released at position two at the closing of the horizon",
    "136 (3)": "3 - it lives in a dimension that connects the positions. It is a bridge, not a physical place. It can "
               "only facilitate transport, not indefinitely hold something.",
    "136 (7)": "7 - The throat formation is synchronization",
    "136 E": "E - previously ruled. Instantaneous or near instantaneous",
    "136 G": "G - the README is the energy, not separate",
    "158 (2)": "(2) \"Exactly as long as the write needs  I should think\"",
    "160": "the corridor and the opening are the same object",
    "161": "my inclination is yes",
    "162": "Although the chain illustrates a corridor, I submit that it may be more like a black hole, containing both "
           "mouths and throat at once. The throat doesn't change size because the whole chain object only every takes "
           "on the size that contains the README upon opening. It is and always will be only the size that is needed "
           "to hold the object once and at once",
    "163": "M chose: \"All together, one whole\"",
    "172 (1)": "M chose: \"Yes, it may\"",
    "183": "M chose: \"Yes: never violated as a pair\"",
    "188": "There are always two entangled opposing forces that balance together.",
    "189": "\"the bond\"",
    "190": "\"Information is energy\"",
    "195": "\"The README is not a pair\"",
    "196": "\"Review all tasks running. Stop any that are no longer relevant. All questions get works through the "
           "cypher\"",
}
BOARD_WORDS = {   # the board's wording inside the option M chose in 163 -- not M's words
    "163 (the board's option text, not M's words)": "\"All together, one whole\" (the README carried in by the inflow, "
    "115 (c), and held as a single whole, not bit by bit, at the fixed size; the write lasts at least ~200,000 clocks; "
    "B4d must keep the fixed-size corridor regular for that long)",
}


def row(value, label, tag="", note=""):
    return {"value": value, "label": label, "tag": tag, "note": note}


# ============================================================================================ (1) HELD
def held_stress(rho_power=0):
    """A held static stress on eq. (17)'s horizon (owner P.horizon_stress_eq17 for the AdS2-invariant regular case);
    rho_power > 0 makes the static-frame density rho = rho0 / F^rho_power, singular on the horizon (the regularity
    premise's control).  tau(xi,xi) = -rho g(xi,xi) on the (v,u) block, g(xi,xi) = -F from the owner's ingoing chart,
    limit u -> 0.  Label: computed ([PLANE] chart; the zero for finite rho is STRUCTURAL: g(xi,xi)|_H = 0).  A separate
    result: no computed formation ends in this stress (the Vaidya end state is vacuum; S4)."""
    own = P.horizon_stress_eq17(0, False)
    g, X4, Fv = P._eq17_ingoing()
    rho0 = sp.Symbol("rho0", positive=True)
    rho = rho0 / Fv**sp.Rational(rho_power)
    tau_xixi = sp.limit(sp.simplify(-rho * g[0, 0]), P.u, 0)
    return {"owner_tau_xixi": own["tau_xixi"], "owner_pi_xixi": own["pi_xixi"], "tau_xixi_limit": tau_xixi,
            "g_xixi_on_H": sp.simplify(g[0, 0].subs(P.u, 0)), "rho_power": rho_power}


def crossing_control(area_power=2):
    """The README as null dust CROSSING a horizon of FIXED size (H-README-AS-NULL-DUST, the board's): owner
    P.readme_flux (chart T^R(xi,xi) = 2 mu, [PLANE] normalisation) and owner F.readme_flux_P1 (kappa4^2 int T_vv dv =
    1/(2m) per generator, [PLANE]-conditional).  Lemma S then asks for the partner -1/(2m).  area_power = 1 is the
    owner's r^2 -> r mutation."""
    p1 = F.readme_flux_P1(area_power=area_power)
    return {"chart_T_xixi": P.readme_flux(1), "P1_per_generator": p1["value"], "equals_1_over_2m":
            p1["equals_one_over_2m"], "partner_per_generator": -p1["value"], "kappa_x_m": p1["kappa_x_m"]}


def lemma_s_forms(fixed_mut=None):
    """Owner Lemma S, bulk form, degenerate family ([FREE], no field equation): fixed size (theta = 0) gives
    R(xi,xi) = 0; shear at fixed volume gives R(xi,xi) = -sigma^2 < 0; a growing section (theta > 0) gives
    R(xi,xi) > 0 with the Raychaudhuri residual 0 -- a positive null flux with no partner, only where the horizon grows.
    R(xi,xi) is geometric; it reads as an energy only under the bulk's field equation.  Sheet form (172 (1), a held
    stress on position 2's piece): K(xi,xi) = 0.  fixed_mut = 'grow' puts the growing case in the fixed slot."""
    gb, uh = P.bulk_gvv("degenerate")
    fixed = P.pairing_bulk(gb, uh, grow=(P.EPS if fixed_mut == "grow" else 0))
    shear = P.pairing_bulk(gb, uh, shear=P.EPS)
    grow = P.pairing_bulk(gb, uh, grow=P.EPS)
    gs, us = P.sheet_gvv("degenerate")
    sheet = P.pairing_sheet(gs, us)
    return {"fixed_theta": fixed["theta"], "fixed_R_xixi": fixed["R_xixi"], "fixed_R_xixi_witness":
            fixed["R_xixi_witness"],
            "shear_theta": shear["theta"], "shear_R_xixi_witness": shear["R_xixi_witness"],
            "grow_theta": grow["theta"], "grow_R_xixi_witness": grow["R_xixi_witness"],
            "grow_raychaudhuri_residual_witness": grow["raychaudhuri_residual_witness"],
            "sheet_K_xixi": sheet["K_xixi"], "sheet_S_xixi_over_nu": sheet["S_xixi_over_nu"]}


# ============================================================================================ H1/G1 and the whole
def h1_per_bit(m2_factor=1):
    """H1 with G1 (owner O.m_squared(): m^2 = N ln2/(4 pi) in Planck units, from E^2 = N h c^5 ln2/(8 pi^2 G)):
    the horizon of the README's energy, r = 2m, has area 16 pi m^2 = N x 4 ln2 Planck areas -- exactly N A_bit.
    STRUCTURAL: G1 is defined as the energy of a horizon holding N bits (G1 as seated, 4D).  m2_factor is a mutation."""
    m2 = O.m_squared() * m2_factor
    area = sp.simplify(4 * sp.pi * 4 * m2)
    return {"area_over_N_planck": sp.simplify(area / O.N), "is_4ln2": sp.simplify(area / O.N - 4 * sp.log(2)) == 0}


def whole_only(e_exponent=sp.Rational(1, 2)):
    """A TRAPPING horizon r = 2M(v) formed by a fraction f of the README's energy: G1 gives E proportional to
    N^e_exponent (1/2 in 4D; 2/3 in 5D, Tangherlini), so its area holds N_f = f^(1/e_exponent) N bits.  Against the share
    f of the README in (if its bits come in with its energy -- H-BITS-WITH-ENERGY, the board's): N_f/(f N).  < 1 for
    every f < 1 means that horizon cannot hold the README part by part, only whole.  The event horizon does otherwise
    (vaidya_run: eh_area_N_at_f).  e_exponent = 1 is the mutation (bit by bit would fit).
    Label: computed (exact); STRUCTURAL in G1's scaling."""
    f = sp.Symbol("f", positive=True)
    held = f**(1 / sp.sympify(e_exponent))
    ratio = sp.simplify(held / f)
    samples = {str(q): sp.nsimplify(ratio.subs(f, q)) for q in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(9, 10), 1)}
    only_whole = all(sp.nsimplify(ratio.subs(f, q)) < 1 for q in (sp.Rational(1, 4), sp.Rational(1, 2),
                                                                  sp.Rational(9, 10))) and ratio.subs(f, 1) == 1
    return {"held_bits_over_N": held, "held_over_share": ratio, "samples": samples, "only_whole": only_whole}


def write_floor(z=None):
    """The write's floor from the owner (o3_write W3, d = 3, Z = 108.75 unless z is given): T >= (3645 ln2 N/(8Z))^(1/3)
    - 2, in the corridor's units of m, at the example README.  Label: computed (owner)."""
    expr = O.t_min(3)
    kw = {} if z is None else {"z": z}
    return {"floor_in_m": O._num(expr, **kw), "N": O.EXAMPLE_N, "Z": str(O.Z_HEAD) if z is None else str(z),
            "w1_2E_gives": str(O.w1()[2] / O.w1()[0])}


def eq17_radial_rkk(data="eq17"):
    """SIM1 S4's criterion from the owner's data (sim2_facing.B4 through epass_pairing): radial R_kk is (H/r) d ln(F/H)/dr
    for a static metric, so the NEC is 'F/H never decreases outward'.  eq. (17): d ln(F/H)/dr = -1/((r-2)(2r-3)) < 0
    (m = 1); Schwarzschild: 0.  So a static end state reached with NEC matter in one spacetime is not eq. (17)
    ([PLANE]).  data = 'schwarzschild' is the control/mutation."""
    r = sp.Symbol("r", positive=True)
    Fd, Hd = (P.SF.B4._eq17 if data == "eq17" else P.SF.B4._schwarzschild)(r)
    dl = sp.simplify(sp.diff(sp.log(Fd / Hd), r))
    vals = [float(dl.subs(r, q)) for q in (sp.Rational(21, 10), 3, 5, 10, 32)]
    return {"dlnFH_dr": dl, "samples": vals, "negative_everywhere_sampled": all(x < 0 for x in vals)}


# ============================================================================================ (2) TIMING: Vaidya
VV, RR, TH, PH = sp.symbols("v r theta phi", real=True)
MF = sp.Function("M")
MS = sp.Symbol("Mval", real=True)


def _vaidya_metric():
    X = [VV, RR, TH, PH]
    f = 1 - 2 * MF(VV) / RR
    return X, f, sp.Matrix([[-f, 1, 0, 0], [1, 0, 0, 0], [0, 0, RR**2, 0], [0, 0, 0, RR**2 * sp.sin(TH)**2]])


def vaidya_identity(drop_rkk=False):
    """[4D-VAIDYA] ds^2 = -(1 - 2M(v)/r) dv^2 + 2 dv dr + r^2 dOmega^2 (standard-not-READ), M arbitrary, owner's
    geometry engine (P._connection, P._riemann).  Outgoing null k = d_v + (f/2) d_r; kappa from nabla_k k = kappa k;
    theta = 2 k^r/r; R(k,k) from the Ricci tensor.  Returns the non-affine Raychaudhuri residual
    k(theta) - kappa theta + theta^2/2 + R(k,k) (must be 0 identically: sigma = 0 by symmetry), kappa, R(k,k).
    drop_rkk is the mutation.  Label: computed (sympy)."""
    X, f, g = _vaidya_metric()
    gi, G = P._connection(g, X)
    R = P._riemann(G, X)
    ric = sp.Matrix(4, 4, lambda b, c: sp.simplify(sum(R(a, b, a, c) for a in range(4))))
    k = [sp.Integer(1), f / 2, 0, 0]
    acc = [sp.simplify(sum(k[b] * sp.diff(k[a], X[b]) for b in range(4))
                       + sum(G[a][b][c] * k[b] * k[c] for b in range(4) for c in range(4))) for a in range(4)]
    kappa = sp.simplify(acc[0] / k[0])
    lin = sp.simplify(acc[1] - kappa * k[1])
    theta = 2 * k[1] / RR
    rkk = sp.simplify(sum(ric[a, b] * k[a] * k[b] for a in range(4) for b in range(4)))
    ktheta = sum(k[b] * sp.diff(theta, X[b]) for b in range(4))
    res = sp.simplify(ktheta - kappa * theta + theta**2 / 2 + (0 if drop_rkk else rkk))
    return {"residual": res, "kappa": kappa, "R_kk": rkk, "geodesic_check": lin, "theta": sp.simplify(theta)}


_CACHE = {}


def kretschmann():
    """[4D-VAIDYA] Kretschmann scalar R_abcd R^abcd from the owner's geometry engine (P._connection, P._riemann), M(v)
    arbitrary.  Label: computed (sympy); it comes out 48 M(v)^2/r^6, with no M' term."""
    if "kretschmann" in _CACHE:
        return _CACHE["kretschmann"]
    X, f, g = _vaidya_metric()
    gi, G = P._connection(g, X)
    R = P._riemann(G, X)
    n = 4
    up = [[[[sp.simplify(R(a, b, c, e)) for e in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    lo = [[[[sp.expand(sum(g[a, w] * up[w][b][c][e] for w in range(n))) for e in range(n)] for c in range(n)]
           for b in range(n)] for a in range(n)]
    nz = [(i, j) for i in range(n) for j in range(n) if gi[i, j] != 0]
    tot = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for e in range(n):
                    if lo[a][b][c][e] == 0:
                        continue
                    raised = sum(gi[a, a2] * gi[b, b2] * gi[c, c2] * gi[e, e2] * lo[a2][b2][c2][e2]
                                 for (a_, a2) in nz if a_ == a for (b_, b2) in nz if b_ == b
                                 for (c_, c2) in nz if c_ == c for (e_, e2) in nz if e_ == e)
                    tot += lo[a][b][c][e] * raised
    _CACHE["kretschmann"] = sp.simplify(tot)
    return _CACHE["kretschmann"]


PROFILE = "quintic"   # C^2 onset (M ~ v^3); the first build's C^1 cubic (M ~ v^2) is kept as the comparison


def _profile(kind):
    """The inflow's mass profile s(x), s(0) = 0, s(1) = 1, and s'(x), on x clipped to [0, 1] (scalars or arrays)."""
    if kind == "cubic":
        return (lambda x: (lambda c: 3 * c * c - 2 * c ** 3)(np.clip(x, 0.0, 1.0)),
                lambda x: (lambda c: 6 * c - 6 * c * c)(np.clip(x, 0.0, 1.0)))
    if kind == "quintic":
        return (lambda x: (lambda c: c ** 3 * (10 - 15 * c + 6 * c * c))(np.clip(x, 0.0, 1.0)),
                lambda x: (lambda c: 30 * c * c * (1 - c) ** 2)(np.clip(x, 0.0, 1.0)))
    raise ValueError(kind)


EH_EXISTS = 1e-9          # the EH is taken to exist where its radius exceeds this (its birth event)
MOVES_RATE = 1e-6         # |dr/dv| above which a horizon's size counts as changing


def vaidya_run(pre=0.0, partner=0.0, width=1.0, write=2.0e5, partner_sign=1.0, area_exp=2.0, profile=None,
               readme_gravitates=True, horizon="event", probe=()):
    """[4D-VAIDYA], m = 1 (the README's G E/c^4).  M(v) = pre + (1 - partner_sign*partner) s(v/width): the README's null
    dust (mass 1) and a partner of the same profile along the same ingoing rays, of fraction `partner` (negative null
    energy: T_vv^c = -partner T_vv^R).  readme_gravitates = False is the test-event world (the README's flux comes in but
    carries no gravity: M = pre).  The event horizon is traced backward from r = 2 M_final after the inflow (stable
    backward); the trapping horizon is r = 2M(v).  Returns: the end area in units of N A_bit (H1: r = 2 has area
    16 pi = N A_bit) -- the Birkhoff end state, fixed by the integration's start; mass and share (arithmetic on the
    labels); MEASURED on the integrated EH: the fraction of the write over which its size changes (|dr/dv| > MOVES_RATE),
    the fraction of the README's energy that arrives where it already exists (crossing it), the null flux int R(k,k) dv
    along its generator, its area when the README begins and at fractions f of E in, where it is born; the least
    expansion of its generators inside the inflow; a finite-difference Raychaudhuri residual along it.  horizon =
    'trapping' puts r = 2M(v) where the EH belongs (mutation).  partner_sign = -1 and area_exp are mutations.
    Label: computed (scipy LSODA, rtol 1e-11; backward the horizon is attracting and stiff where M is small)."""
    s, ds = _profile(profile or PROFILE)
    q = 1.0 - partner_sign * partner
    qg = q if readme_gravitates else 0.0
    mfin = pre + qg

    def M(v):
        return pre + qg * s(v / width)

    def Mp(v):
        return qg * ds(v / width) / width

    out = {"pre": pre, "partner": partner, "width_over_write": width / write, "mass_E": mfin, "net": q,
           "profile": profile or PROFILE, "readme_gravitates": bool(readme_gravitates), "horizon": horizon}
    if mfin <= 1e-12:
        out.update({"horizon_forms": False, "area_N": 0.0, "share": 0.0, "moves_fraction": 0.0,
                    "moves_fraction_trapping": 0.0, "readme_fraction_crossing_eh": 0.0, "flux_along_eh": 0.0,
                    "eh_theta_min_in_inflow": None, "fd_raychaudhuri_rel": None, "eh_born_before_inflow_m": None,
                    "eh_r_at_onset": 0.0, "eh_area_N_at_onset": 0.0, "eh_r_at_probe": [0.0 for _ in probe]})
        return out
    v_end = width + 20.0 * max(1.0, mfin)
    r_end = 2.0 * mfin

    def rhs(v, y):
        return [0.5 * (1.0 - 2.0 * M(v) / max(y[0], 1e-300))]

    def born(v, y):
        return y[0] - EH_EXISTS
    born.terminal = True
    v_lo = -(4.0 * mfin + 50.0 * max(pre, 0.0) + 10.0)
    sol = solve_ivp(rhs, (v_end, v_lo), [r_end], dense_output=True, rtol=1e-11, atol=1e-13, events=born,
                    max_step=max(width / 400.0, 0.02), method="LSODA")
    vb = float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
    t_first = float(sol.t[-1])
    if horizon == "trapping":
        def rv(va):
            return 2.0 * M(np.asarray(va, dtype=float))
        vb = 0.0 if pre == 0 else None
    else:
        def rv(va):
            va = np.asarray(va, dtype=float)
            r_ = np.asarray(sol.sol(np.clip(va, t_first, v_end))[0], dtype=float)
            return np.where(va <= (vb if vb is not None else -np.inf), 0.0, r_)

    def rs(v):
        return float(rv(np.array([v]))[0])
    # expansion of the outgoing generators (k^v = 1): theta = (1 - 2M/r)/r; kappa = M/r^2; R(k,k) = 2 M'/r^2
    g_lo = 0.05 * width if (vb is None or vb < 0.05 * width) else vb + 0.05 * (width - vb)
    grid = np.linspace(g_lo, 0.95 * width, 41)
    th = [(1.0 - 2.0 * M(v) / rs(v)) / rs(v) for v in grid]
    h = width * 1e-4
    rel = []
    for v in grid[::4]:
        tp, tm = [(1.0 - 2.0 * M(w) / rs(w)) / rs(w) for w in (v + h, v - h)]
        dth = (tp - tm) / (2 * h)
        r0, t0 = rs(v), (1.0 - 2.0 * M(v) / rs(v)) / rs(v)
        terms = (M(v) / r0**2 * t0, t0**2 / 2, 2.0 * Mp(v) / r0**2)
        rhs_r = terms[0] - terms[1] - terms[2]
        rel.append(abs(dth - rhs_r) / max(abs(dth) + sum(abs(x) for x in terms), 1e-30))
    area_N = (rs(v_end) / 2.0) ** area_exp
    # MEASURED on the horizon: where its size changes (the grid's span with |dr/dv| > MOVES_RATE)
    gv = np.linspace(max(t_first, vb if vb is not None else t_first), v_end, 8001)
    rr_ = rv(gv)
    dr = np.abs(np.gradient(rr_, gv))
    mov = gv[dr > MOVES_RATE]
    moves = 0.0 if len(mov) < 2 else float(mov[-1] - mov[0]) / write
    gt = np.linspace(-width, v_end, 8001)
    movt = gt[np.abs(Mp(gt)) > 0]
    moves_t = 0.0 if len(movt) < 2 else float(movt[-1] - movt[0]) / write
    # crossing: the README's own flux profile (mass 1) weighted by whether the horizon already exists at its v
    gx = np.linspace(0.0, width, 20001)
    wgt = ds(gx / width) / width
    ex = (rv(gx) > EH_EXISTS).astype(float)
    frac_cross = float(np.trapezoid(wgt * ex, gx) / np.trapezoid(wgt, gx))
    gf = np.linspace(0.0, width, 4001)
    rf = rv(gf)
    okf = rf > 1e-6
    flux = float(np.trapezoid(np.where(okf, 2.0 * Mp(gf) / np.where(okf, rf, 1.0) ** 2, 0.0), gf))

    def v_at(fr_):
        lo_, hi_ = 0.0, 1.0
        for _ in range(80):
            mid = 0.5 * (lo_ + hi_)
            lo_, hi_ = (mid, hi_) if float(s(mid)) < fr_ else (lo_, mid)
        return 0.5 * (lo_ + hi_) * width
    out.update({"horizon_forms": True, "area_N": area_N, "share": (q / mfin if (q > 0 and readme_gravitates) else 0.0),
                "moves_fraction": moves, "moves_fraction_trapping": moves_t,
                "readme_fraction_crossing_eh": frac_cross, "flux_along_eh": flux,
                "eh_theta_min_in_inflow": float(min(th)), "eh_theta_max_in_inflow": float(max(th)),
                "fd_raychaudhuri_rel": float(max(rel)), "eh_born_before_inflow_m": (None if vb is None else -vb),
                "eh_r_at_onset": rs(0.0), "eh_area_N_at_onset": (rs(0.0) / 2.0) ** 2,
                "eh_r_at_probe": [rs(p_) for p_ in probe],
                "trapping_r_at_mid_inflow": 2.0 * float(M(0.5 * width))})
    if pre == 0 and partner == 0 and readme_gravitates:
        out["eh_area_N_at_f"] = {str(f_): (rs(v_at(f_)) / 2.0) ** 2 for f_ in (0.1, 0.5, 0.9)}
        out["trapping_area_N_at_f"] = {str(f_): float(M(v_at(f_))) ** 2 for f_ in (0.1, 0.5, 0.9)}
    return out


def onset_regularity(profile=None, v0_frac=1e-7):
    """RH-R6: is the spread inflow's onset (r = 0, v = 0) a curvature singularity visible from outside?  An outgoing ray
    from (v0, v0/2), v0 = v0_frac of the write, integrated to the end; the Kretschmann scalar (kretschmann(), computed
    with the owner's engine) along it at v0, 10 v0, 100 v0.  A profile with M ~ v^2 at onset (the C^1 cubic) gives
    K ~ v^-2 along an escaping ray; M ~ v^3 (the C^2 quintic) keeps it bounded.  Label: computed."""
    T = write_floor()["floor_in_m"]
    s, _ = _profile(profile or PROFILE)
    Kf = sp.lambdify((MS, RR), kretschmann().subs(MF(VV), MS))
    v0 = v0_frac * T
    run = vaidya_run(0.0, 0.0, T, T, profile=profile, probe=(v0,))
    sol = solve_ivp(lambda v, y: [0.5 * (1.0 - 2.0 * float(s(v / T)) / y[0])], (v0, T + 40.0), [v0 / 2.0],
                    method="LSODA", rtol=1e-10, atol=1e-14, dense_output=True, max_step=T / 500.0)
    ks = [float(Kf(float(s(v0 * j / T)), float(sol.sol(v0 * j)[0]))) for j in (1, 10, 100)]
    r_last = float(sol.y[0][-1])
    return {"profile": profile or PROFILE, "v0_over_write": v0_frac, "ray_starts_outside_eh":
            bool(v0 / 2.0 > run["eh_r_at_probe"][0]), "r_ray_end": r_last, "escapes": bool(r_last > 1e4),
            "kretschmann_at_v0_10v0_100v0": ks, "ratio_v0_to_100v0": ks[0] / ks[2],
            "eh_born_before_inflow_m": run["eh_born_before_inflow_m"]}


def scenarios(write=None, partner_sign=1.0, area_exp=2.0, profile=None, readme_gravitates=True, horizon="event"):
    """The computed configurations: pre in {0 (the horizon forms with the inflow), 1 (a horizon of the README's size
    already stands)}, partner in {0, 1/2, 1}, inflow compact (width = 1 m) or spread over the whole write (the owner's
    floor).  Cached by its arguments (a pure function).  Label: computed."""
    T = write_floor()["floor_in_m"] if write is None else write
    key = ("sc", T, partner_sign, area_exp, profile or PROFILE, readme_gravitates, horizon)
    if key in _CACHE:
        return _CACHE[key]
    runs = []
    for pre in (0.0, 1.0):
        for p in (0.0, 0.5, 1.0):
            for spread, w in ((0, 1.0), (1, T)):
                r = vaidya_run(pre, p, w, T, partner_sign=partner_sign, area_exp=area_exp, profile=profile,
                               readme_gravitates=readme_gravitates, horizon=horizon)
                r["spread"] = spread
                runs.append(r)
    _CACHE[key] = {"write_floor_in_m": T, "runs": runs}
    return _CACHE[key]


def _frac(x, den=12):
    return Fr(x).limit_denominator(den)


COORDS = ["pre", "partner", "spread", "area_N", "mass_E", "share", "net", "moves", "crosses"]


def _moves_code(fr):
    return 0 if fr == 0 else (1 if fr <= 1e-3 else 2)


def _crosses_code(fr):
    return 1 if fr >= 1 - 1e-6 else (0 if fr <= 1e-6 else 0.5)


def cells_from(sc, held=True, held_share="1", crosses_rule="eh"):
    """Ordinal cells.  pre, partner, spread: labels.  area_N, mass_E, share, net: the Birkhoff end state and arithmetic
    on the labels, rounded to small rationals.  moves: MEASURED on the integrated EH, coded 0 (its size never changes),
    1 (it changes only over <= 1e-3 of the write), 2 (over more).  crosses: MEASURED, 1 if the README's energy arrives
    where the EH already exists, 0 if no horizon exists (0.5 flags anything between -- check C14).  The held cell is
    ASSIGNED, not integrated: the forming run's end state (a horizon of the README's size stands, the README its whole
    mass when held_share = '1', nothing coming in, nothing crossing).  crosses_rule = 'net' codes crosses from the label
    net (mutation).  Label: computed; the encoding is the board's (H-CYPHER-README-HELD-INDEX)."""
    cells, names = [], []
    for r in sc["runs"]:
        cr = (_crosses_code(r["readme_fraction_crossing_eh"]) if crosses_rule == "eh"
              else (1 if r["net"] > 1e-15 else 0))
        c = [str(_frac(r["pre"])), str(_frac(r["partner"])), r["spread"], str(_frac(r["area_N"])),
             str(_frac(r["mass_E"])), str(_frac(r["share"])), str(_frac(r["net"])), _moves_code(r["moves_fraction"]), cr]
        cells.append(c)
        names.append(f"pre={_frac(r['pre'])} partner={_frac(r['partner'])} spread={r['spread']}")
    if held:
        cells.append(["1", "0", 0, "1", "1", held_share, "0", 0, 0])
        names.append("held (ASSIGNED): the formed horizon holding the README as its mass, nothing coming in, nothing "
                     "crossing -- the Vaidya end state, vacuum")
    return cells, names


TEST_EVENT_CELL = ["1", "0", 1, "1", "1", "1", "1", 0, 1]       # the first build's planted control (= T_GLOSS)
TARGETS = {
    "T_FORMS_CROSSING (H-ARRIVAL-FORMS-THE-HORIZON: forms with a compact whole inflow that crosses it, no partner, area "
    "N A_bit, mass E, the README's whole mass, the size moving only over the inflow)": ["0", "0", 0, "1", "1", "1", "1",
                                                                                        1, 1],
    "T_IN_HELD_NOT_CROSSING (195's note as worded: the README comes in held by the forming horizon, nothing crossing)":
        ["0", "0", 0, "1", "1", "1", "1", 1, 0],
    "T_STRICT (162 read as never changing, the inflow not instantaneous)": ["0", "0", 0, "1", "1", "1", "1", 0, 1],
    "T_GLOSS (163's option text with 195: fixed size through a spread write, no partner, area N A_bit, mass E)":
        TEST_EVENT_CELL,
    "T_PAIR (163's option text with the partner: E-PASS's crossing; the README one member of a pair)":
        ["1", "1", 1, "1", "1", "0", "0", 0, 1],
}
WITNESSES = {
    "law": "mass_E = pre + net; area_N = mass_E^2 (Vaidya end state A = 16 pi M^2); moves > 0 exactly where net > 0 "
           "(Raychaudhuri on the EH: least theta > 0 during a net inflow, 0 at net 0)",
    "law+net=1-partner": "the first build's witness: the law's three clauses and net = 1 - partner (mutation)",
    "test": "the test-event world's own law: mass_E = pre; area_N = mass_E^2; moves = 0",
}


def witness_residuals(cells, clauses="law"):
    """analysis' declared witness, evaluated: the largest clause residual on each cell.  Label: computed."""
    ix_ = {c: i for i, c in enumerate(COORDS)}
    res = []
    for c in cells:
        pre, area, mass, net, mv, part = (float(Fr(str(c[ix_[k]]))) for k in ("pre", "area_N", "mass_E", "net", "moves",
                                                                              "partner"))
        if clauses == "test":
            r_ = [mass - pre, area - mass ** 2, float(mv)]
        else:
            r_ = [mass - pre - net, area - mass ** 2, float((mv > 0) != (net > 0))]
            if clauses == "law+net=1-partner":
                r_.append(net - (1 - part))
        res.append(max(r_, key=abs))
    return res


def _spec_index(name, cells, declared):
    vo = {c: sorted({row_[i] for row_ in cells}, key=lambda x: float(Fr(str(x)))) for i, c in enumerate(COORDS)}
    return CY.Index(name, COORDS, cells, value_order=vo, declared=declared)


def _determined(cells, by, target, where=None):
    """logic's binary: is `target` a function of `by` on the cells satisfying `where` (a value or a list of values per
    coordinate)?  Returns (bool, values seen)."""
    idx = {c: i for i, c in enumerate(COORDS)}
    m = defaultdict(set)
    seen = set()
    for c in cells:
        if where and not all(str(c[idx[k]]) in ([str(x) for x in v] if isinstance(v, (list, tuple)) else [str(v)])
                             for k, v in where.items()):
            continue
        m[tuple(c[idx[b]] for b in by)].add(c[idx[target]])
        seen.add(c[idx[target]])
    return (bool(m) and all(len(v) == 1 for v in m.values())), sorted(seen, key=lambda x: float(Fr(str(x))))


LOGIC = {
    "L1 timing: with 195 (partner 0), H1 (area N A_bit) and the README coming in (net 1), is pre fixed?":
        (["partner"], "pre", {"partner": "0", "area_N": "1", "net": "1"}),
    "L2 a fixed size (moves 0) takes no net null flux: is net fixed?": ([], "net", {"moves": 0}),
    "L3 energy balance: is net fixed by (pre, mass_E)?": (["pre", "mass_E"], "net", None),
    "L4 the values moves takes among net = 1 cells (0 would be a fixed size with a net inflow)":
        ([], "moves", {"net": "1"}),
    "L6 crossing: among cells with a net inflow (net 1/2 or 1), is crosses fixed?":
        ([], "crosses", {"net": ["1/2", "1"]}),
}
WORLD_NAMES = {"law": "LAW", "test-event": "CONTROL: the test-event world (the README carries no gravity)",
               "planted": "the first build's planted control (RI-5's cell = T_GLOSS)",
               "negative": "NEGATIVE CONTROL: the lawful computed run pre = 1/2 added"}


def negative_cell(write=None):
    T = write_floor()["floor_in_m"] if write is None else write
    r = vaidya_run(0.5, 0.0, 1.0, T)
    r["spread"] = 0
    return cells_from({"runs": [r]}, held=False)[0][0]


def world_cells(world, sc=None, sc_test=None, extra=None):
    if world == "test-event":
        sct = sc_test or scenarios(readme_gravitates=False)
        return cells_from(sct, held_share="0")
    cells, names = cells_from(sc or scenarios())
    if world == "planted":
        return cells + [list(TEST_EVENT_CELL)], names + ["planted: the README absorbed by a horizon that keeps size and "
                                                         "mass, no partner (RI-5)"]
    if world == "negative":
        return cells + [list(extra or negative_cell())], names + ["negative control: pre = 1/2, no partner, compact"]
    return cells, names


def cypher_run(world="law", sc=None, sc_test=None, witness="law", extra=None):
    """Put the question to the cypher (roster 1173) on one world's index.  For each language: state, admitted-set size,
    E; for each target: admitted or not, and whether a NO is STRUCTURAL; analysis' state computed from its declared
    witness's residuals; logic's binaries on the cells and on every language's admitted set.  Label: computed; the
    encoding is the board's."""
    cells, names = world_cells(world, sc, sc_test, extra)
    wkey = "test" if world == "test-event" else witness
    res_w = witness_residuals(cells, wkey)
    res_law = witness_residuals(cells, "law")
    speaks = max(abs(x) for x in res_w) < 1e-12
    wit = {"analysis": {"speaks": speaks, "witness": WITNESSES[wkey] + "; largest residual "
                        + str(max(res_w, key=abs))}}
    ix = _spec_index("README held vs crossing (" + WORLD_NAMES[world] + ")", cells, wit)
    res = CY.run(ix, "1173", {"algebra_budget": 60000})
    langs, admitted, decoded = {}, {}, {}
    for lang in list(OPB) + ["documentary"]:
        out, note = CY.ADMISSION[lang][0](ix, {"algebra_budget": 60000})
        if out is None:
            langs[lang] = {"state": "SILENT", "note": note}
            continue
        admitted[lang] = out
        decoded[lang] = [[ix.decode[i][cv] for i, cv in enumerate(cell)] for cell in out]
        langs[lang] = {"state": "SPEAKS", "admits": len(out), "E": len(out) - len(ix.cells)}
    langs["analysis"] = {"state": "SPEAKS" if speaks else "SILENT", "witness": wit["analysis"]["witness"],
                         "status": "DECLARED", "residual_max": float(max(res_w, key=abs)),
                         "law_witness_residual_max": float(max(res_law, key=abs))}
    seen_pairs = {(i, j): {(c[i], c[j]) for c in ix.cells} for i in range(ix.d) for j in range(ix.d) if i < j}
    tgt = {}
    for tname, t in TARGETS.items():
        enc = tuple(ix.code[i].get(v) for i, v in enumerate(t))
        unseen = [COORDS[i] for i, e in enumerate(enc) if e is None]
        in_cells = (None not in enc) and enc in set(ix.cells)
        unseen_pairs = []
        if not unseen:
            for (i, j), s_ in seen_pairs.items():
                if (enc[i], enc[j]) not in s_:
                    unseen_pairs.append(f"{COORDS[i]}={t[i]} with {COORDS[j]}={t[j]}")
        per = {lang: ((None not in enc) and enc in out) for lang, out in admitted.items()}
        tr = witness_residuals([t], "law")[0]
        per["analysis"] = ("answers only by its declared witness; against the law's witness the target is "
                           + ("lawful" if abs(tr) < 1e-12 else f"UNLAWFUL (residual {tr})"))
        per["documentary"] = "SILENT (citations, not a binary)"
        tgt[tname] = {"is_a_computed_cell": in_cells, "values_never_seen": unseen,
                      "value_pairs_never_seen": unseen_pairs[:6], "n_pairs_never_seen": len(unseen_pairs),
                      "admitted": per, "NO_is_STRUCTURAL": bool(unseen or unseen_pairs)}
    logic = {}
    for lk, (by, target, where) in LOGIC.items():
        fx, vals = _determined(cells, by, target, where)
        per_l = {}
        for lang, dc in decoded.items():
            fl, vl = _determined(dc, by, target, where)
            per_l[lang] = {"fixed": fl, "values": vl}
        logic[lk] = {"cells": {"fixed": fx, "values": vals}, "languages": per_l}
    rows_, keys = CY.coordinate_report(ix)
    return {"index": ix.name, "cells": len(ix.cells), "box": ix.box, "d": ix.d, "cell_names": names,
            "cell_values": cells, "languages": langs, "targets": tgt, "logic": logic,
            "information_adds_nothing": [r_["coordinate"] for r_ in rows_ if r_["adds_nothing"]],
            "information_keys": keys, "K_langclose_holds": res["langclose_holds"], "languages_agree":
            res["languages_agree"], "degenerate": res["degenerate"], "operator_bearing_measured":
            res["operator_bearing_measured"], "pairs_agreeing": res["pairs_agreeing"], "warnings": res["warnings"],
            "documentary_citations": ["Vaidya metric (standard-not-READ)", "Raychaudhuri (standard-not-READ)",
                                      "area theorem (standard-not-READ)",
                                      "Kehle-Unger arXiv:2211.15742v2 PDF p.1 (READ)", "SIM1-TRANSITION S3b, S4",
                                      "O3-WRITE W3, W4 (ii)", "epass_pairing Lemma S (a), (b)",
                                      "epass_frames readme_flux_P1"]}


def cypher_invariance(write=None, sc_test=None):
    """RH-R2: the law index rebuilt from mutated physics (partner sign flipped; area linear in M; the 5D area M^(3/2)).
    Records each world's admitted sizes and the verdicts on T_IN_HELD_NOT_CROSSING, T_STRICT, T_GLOSS, L1 and L6 on the
    cells.  Equal verdicts are a limit of the cypher (it codes rank, not value), not a finding.  Label: computed."""
    T = write_floor()["floor_in_m"] if write is None else write
    out = {}
    for nm, kw in (("partner_sign_flipped", {"partner_sign": -1.0}), ("area_linear_in_M", {"area_exp": 1.0}),
                   ("area_5D_M_3_2", {"area_exp": 1.5})):
        res = cypher_run("law", scenarios(write=T, **kw), sc_test)
        tv = {t.split(" ")[0]: {l_: res["targets"][t]["admitted"][l_] for l_ in OPB}
              for t in TARGETS if t.startswith(("T_IN_HELD", "T_STRICT", "T_GLOSS"))}
        out[nm] = {"admits": {l_: res["languages"][l_].get("admits") for l_ in OPB}, "targets": tv,
                   "L1_cells": res["logic"][[k for k in LOGIC if k.startswith("L1")][0]]["cells"],
                   "L6_cells": res["logic"][[k for k in LOGIC if k.startswith("L6")][0]]["cells"]}
    out["verdicts_all_NO"] = all(v_ is False for w in out.values() for tv in w["targets"].values()
                                 for v_ in tv.values())
    return out


# ============================================================================================ the record
RECORD = [
    ("70", "M_WORDS", "(a), with a tension", "the corridor takes what it requires 'as a natural condition of its "
     "opening ... such as with a horizon': the taking is the opening, as a forming horizon takes what falls in across it "
     "(the board's reading); under H-GAS-BOUND-AS-LEAD the README would converge for ~2e5 clocks before any horizon, "
     "which sits uneasily with 'We do not feed the corridor' (OPEN)"),
    ("86 (5)", "M_WORDS", "duration: compact", "'incredibly short, maybe even immeasurable but not zero': a short inflow; "
     "favours a compact inflow over one spread across the write (the board's reading) and pulls against the gas bound "
     "carried under 163's note; 'not zero' keeps 162's size change, over the inflow, nonzero"),
    ("94", "M_WORDS", "(a)", "'a single channel that grows in size to accommodate the size of the README': the size "
     "grows to the README's -- the forming horizon of (a); pulls against 162 read as never changing"),
    ("94 (instantaneous)", "M_WORDS", "duration: compact", "'instantaneously relative to the object teleporting': with "
     "86 (5) and 136 E, a near-instantaneous inflow (the board's reading)"),
    ("101 (6)", "M_WORDS", "both", "the size is the README's, 'no more and no less': H1 on either reading; 'widen' names "
     "a process and does not say whether the size stands before the README comes in (silent on timing)"),
    ("106 (b)", "M_WORDS", "(a) with OPEN", "the first hold is on horizon 1 'only as the corridor opens': holding begins "
     "with the opening.  The hold's move to horizon 2 needs horizon 1's area to decrease, which the NEC forbids (area "
     "theorem, standard-not-READ): a flux demand, OPEN (132's 'different views of the same object' would make it a "
     "change of view -- the board's reading)"),
    ("109", "M_WORDS", "depends on the horizon", "the object 109 names is the corridor (H-HORIZON-NEEDS-OBJECT, as "
     "carried).  On the trapping horizon no horizon stands before the README; on the event horizon of a compact inflow a "
     "horizon of 0.77 N A_bit stands 3.5 m before any README is in it (computed) -- against 109 if its object is read as "
     "the README (the board's reading, not carried), a cost of (a) on the event horizon.  Its 'ends as well' is part of "
     "the closing's cost (area theorem)"),
    ("115 (a)", "M_WORDS", "(a) with OPEN", "'It ends; energy moved': position 1's horizon ends -- its area must "
     "decrease, which the NEC forbids (area theorem): the closing's cost, OPEN"),
    ("115 (b)", "M_WORDS", "(a)", "position 2's horizon comes into being 'When fully realized': a horizon forming and "
     "holding the bits from then (106); its own formation and ending are OPEN, as for 106"),
    ("115 (c)", "M_WORDS", "(a)", "the inflow is 'The README itself' (R0): on (a) that inflow crosses and forms the "
     "horizon (computed: share 1; all of its energy across the event horizon)"),
    ("129 (1)", "M_WORDS", "(a)", "'it adds nothing to either position': on (a) the horizon's whole mass is the "
     "README's (share 1, computed); on (b) a mass E stands at the position before the README comes in -- energy that is "
     "not the README's (deduced, the board's reading of 129 (1) with 136 G)"),
    ("130 (1)", "M_WORDS", "both", "the black hole is what the mouth looks like: either reading"),
    ("131 (2)", "M_WORDS", "both", "the throat is sized by the README's binary information: H1 on either reading"),
    ("132", "M_WORDS", "(a)", "the horizons hold the README: on (a) the end state's area is the README's own N bits; on "
     "(b) with the partner the area of N A_bit has a mass that is not the README's (computed: share 0).  'Hold' is read "
     "of the end state: the README crosses the horizon on its way in (computed)"),
    ("133 (2)", "M_WORDS", "(a)", "'only one exact energy': (b) without a partner ends at mass 2E and area 4 N A_bit "
     "(computed; the owner's W1 control '2E gives 4N'); with the partner the standing E is separate from the README's "
     "+E and -E (deduced); (a) one E (computed)"),
    ("136 (2)", "M_WORDS", "(a) with OPEN", "'released at position two at the closing of the horizon': the closing needs "
     "the horizon's area to decrease (area theorem; NEC) -- OPEN"),
    ("136 G", "M_WORDS", "(a) on the share-1 reading", "'the README is the energy, not separate', read as the README's "
     "share of the horizon's mass (the board's reading): (a) share 1; (b) with the partner share 0 (computed)"),
    ("136 E", "M_WORDS", "duration: compact", "'Instantaneous or near instantaneous', answering how long the corridor "
     "must last (wall E): favours a compact inflow (the board's reading); 139 (3) records it as answered"),
    ("136 (3)", "M_WORDS", "neutral", "'not indefinitely hold': both readings hold for a finite interval"),
    ("136 (7)", "M_WORDS", "neutral", "'The throat formation is synchronization': names the formation; not computed here"),
    ("158 (2)", "M_WORDS", "OPEN", "the hold lasts as long as the write needs: which interval its 'hold' names on (a) -- "
     "the inflow, or the held interval after it -- is the board's reading (OPEN)"),
    ("160", "M_WORDS", "(a), with a tension", "'the same object': on (a) the opening -- the README coming in across the "
     "horizon it forms -- is the corridor.  Under H-GAS-BOUND-AS-LEAD the convergence before the horizon is not the "
     "corridor (OPEN).  The board's note carried under 160 ('the corridor does not exist until the README has arrived' "
     "gives way) was the board's reading; (a) reverses it on the trapping horizon, not on the event horizon"),
    ("161", "M_WORDS", "neutral", "'my inclination is yes' to staying regular while the README passes: on (a) no "
     "fixed-size corridor stands during the inflow; the regularity question moves to the formation and the held interval"),
    ("162", "M_WORDS", "(a) with a cost", "on the trapping horizon of a compact inflow the size grows from nothing to "
     "the README's over the inflow's width (computed: 5.0e-6 of the write at 1 m) and is fixed from the moment the whole "
     "README is in.  On the event horizon it changes over ~4.5 m, 3.5 m of it before the README (compact), or over the "
     "whole write (spread).  'Always' holds at every moment only in the instantaneous limit, which 86 (5), 94 and 136 E "
     "approach but do not reach ('not zero').  (b) keeps it fixed through the write only with a partner (Lemma S)"),
    ("163", "M_WORDS", "neutral on duration", "M's words, 'All together, one whole', define 'at once' and rule nothing on "
     "how long the inflow lasts.  A forming trapping horizon holds the README only whole (computed: f^2 of the bits at a "
     "fraction f of E, G1 as seated in 4D; f^(3/2) in 5D); reading that as 163's 'one whole' is the board's "
     "(H-WHOLE-AS-G1).  On the event horizon of a compact inflow the area runs ahead of f N (computed)"),
    ("163 (the board's option text, not M's words)", "BOARD_WORDS", "(b)", "'at the fixed size; the write lasts at "
     "least ~200,000 clocks; B4d must keep the fixed-size corridor regular for that long' is (b)'s framing; with no "
     "partner no computed configuration has it (T_GLOSS below) -- it does not survive (a).  M chose the option carrying "
     "this text; whether that choice endorsed it is for M; this reverses the reading carried under 163"),
    ("172 (1)", "M_WORDS", "(a)", "a held regular stress on position 2's piece carries no surface null flux (owner "
     "Lemma S sheet form, K(xi,xi) = 0): no partner asked of the held interval there"),
    ("183", "M_WORDS", "(b) with the partner: admitted", "'never violated as a pair', for the README crossing a "
     "fixed-size horizon: M admitted (b) with the partner.  It is set aside only on the board's reading of 195 as 'not "
     "one member of a pair' (H-README-NOT-ONE-MEMBER) or on the share-1 reading of 136 G / 190; M has not ruled that "
     "195 supersedes 183"),
    ("188", "M_WORDS", "neutral", "'always two entangled opposing forces': (a)'s inflow does not demand 188's pair, and "
     "(b)'s partner would be one; 188 decides neither"),
    ("189", "M_WORDS", "neutral", "'the bond': a tension carries zero null energy along a fixed-size horizon (ITEM188 "
     "1.9, computed there); it bears on the held interval, not on how the README comes in"),
    ("190", "M_WORDS", "(a) on the share-1 reading", "'Information is energy': (a) has the N bits as the area and E as "
     "the mass of one object (H1 with G1, STRUCTURAL); (b) with the partner has them on a mass that is not the README's"),
    ("195", "M_WORDS", "(a) on the board's gloss", "M's five words, 'The README is not a pair'.  Read as 'not one member "
     "of a pair' (the board's gloss, H-README-NOT-ONE-MEMBER) they close (b) with the partner (194's object), and with "
     "Raychaudhuri, H1/G1 and 133 that leaves only (a) (deduced).  Read literally -- the README is not itself a +/- pair "
     "-- they do not close it.  They do not say 'held' (the board's note)"),
]
LEMMA_ROWS = {   # warptheorem.py's rows as they stand (read from the file by check C10b)
    "R0": "R0 the read: the corridor takes the README as its inflow at the opening; N is read from the object",
    "E1": "E1 E carried through three holds into position 2",
    "E2": "E2 released at position 2 at the closing",
    "H2": "H2 the horizons hold the README as well as the throat",
    "I1": "I1 the passage is N bits of entanglement",
}
LEMMA_VERDICTS = {
    "R0": ("(a)", "the inflow at the opening crosses the horizon it forms (computed: all of the README's energy across "
           "the event horizon; theta > 0)"),
    "E1": ("(a) with OPEN", "E is the horizon's mass once the README is in; carrying it through 106's three holds needs "
           "horizon 1's area to decrease -- forbidden under the NEC (area theorem, standard-not-READ): a flux demand, "
           "OPEN (B4d's)"),
    "E2": ("(a) with OPEN", "held on position 2's horizon until it ends with the corridor (109, 115 (b)); the ending needs "
           "the area to decrease -- forbidden under the NEC: OPEN"),
    "H2": ("(a), end state", "literal on (a) once the README is in: the area is its N bits (H1)"),
    "I1": ("both", "the passage's N bits are the area's N bits (H1)"),
}


def record_check(words=None):
    words = {**M_WORDS, **BOARD_WORDS} if words is None else words
    ok = F.m_words_verbatim(words=words)
    with open(os.path.join(D68, "warptheorem.py")) as fh:
        wt = fh.read()
    lem = {k: (v in wt) for k, v in LEMMA_ROWS.items()}
    return {"quotes_found_in_own_item": ok, "all_quotes": all(ok.values()), "lemma_rows_found": lem,
            "all_lemma_rows": all(lem.values())}


# ============================================================================================ compute
def compute():
    if "out" in _CACHE:
        return _CACHE["out"]
    t0 = _wall.perf_counter()
    hs, hsing = held_stress(0), held_stress(1)
    cc = crossing_control()
    ls = lemma_s_forms()
    h1 = h1_per_bit()
    wo, wo5 = whole_only(), whole_only(sp.Rational(2, 3))
    wf = write_floor()
    T = wf["floor_in_m"]
    s4 = eq17_radial_rkk()
    vi = vaidya_identity()
    kr = kretschmann()
    sc = scenarios(write=T)
    sct = scenarios(write=T, readme_gravitates=False)
    worlds = {w: cypher_run(w, sc, sct, extra=(negative_cell(T) if w == "negative" else None))
              for w in ("law", "test-event", "planted", "negative")}
    inv = cypher_invariance(T, sct)
    on_q, on_c = onset_regularity(), onset_regularity("cubic")
    cub_c, cub_s = vaidya_run(0, 0, 1.0, T, profile="cubic"), vaidya_run(0, 0, T, T, profile="cubic")
    rc = record_check()
    runs = {f"pre={_frac(r['pre'])} partner={_frac(r['partner'])} spread={r['spread']}": r for r in sc["runs"]}
    fc = runs["pre=0 partner=0 spread=0"]
    fsp = runs["pre=0 partner=0 spread=1"]
    pn = runs["pre=1 partner=0 spread=0"]
    pp = runs["pre=1 partner=1 spread=1"]
    fp = runs["pre=0 partner=1 spread=0"]
    R = {}
    R["held_stress_T_xixi"] = row({"tau_xixi": hs["owner_tau_xixi"], "pi_xixi": hs["owner_pi_xixi"],
                                   "limit_regular": hs["tau_xixi_limit"]}, "computed; STRUCTURAL",
                                  "[PLANE] chart", "owner horizon_stress_eq17: zero because g(xi,xi)|_H = 0 with finite "
                                  "rho -- a regular held stress asks Lemma S for no partner.  A separate result: no "
                                  "computed formation ends in it (end_state_is_vacuum; S4)")
    R["held_stress_singular_control"] = row(hsing["tau_xixi_limit"], "computed", "[PLANE] chart",
                                            "rho = rho0/F (singular on the horizon) keeps T(xi,xi) = rho0: regularity "
                                            "is the premise")
    R["crossing_control"] = row({"chart_T_xixi": cc["chart_T_xixi"], "P1_per_generator": cc["P1_per_generator"],
                                 "partner_per_generator": cc["partner_per_generator"]}, "computed",
                                "[PLANE]-conditional", "the README as null dust crossing a horizon of FIXED size: "
                                "1/(2m) per generator on P1; Lemma S asks -1/(2m)")
    R["lemma_s_bulk_and_sheet"] = row({k: ls[k] for k in ("fixed_theta", "fixed_R_xixi", "shear_R_xixi_witness",
                                                          "grow_theta", "grow_R_xixi_witness",
                                                          "grow_raychaudhuri_residual_witness", "sheet_K_xixi")},
                                      "computed", "[FREE]", "theta = 0: R(xi,xi) = -sigma^2 <= 0; growing: R(xi,xi) > 0 "
                                      "with residual 0 -- positive net null flux only where the horizon grows.  R(xi,xi) "
                                      "is geometric; read as energy under the bulk's 5D field equation (on a brane the "
                                      "effective equations add a projected Weyl term, standard-not-READ)")
    R["H1_area_per_bit"] = row(h1["area_over_N_planck"], "STRUCTURAL", "G1 as seated (4D)",
                               "the README's horizon (r = 2m, owner m^2) holds exactly 4 ln2 Planck areas per bit")
    R["whole_only"] = row({"held_bits_over_N_4D": wo["held_bits_over_N"], "held_over_share_4D": wo["held_over_share"],
                           "samples_4D": wo["samples"], "held_bits_over_N_5D": wo5["held_bits_over_N"],
                           "only_whole_5D": wo5["only_whole"]}, "computed; STRUCTURAL",
                          "G1 as seated (4D); 5D beside it; the trapping horizon r = 2M(v)",
                          "a forming TRAPPING horizon holds f^2 N bits at a fraction f of E (f^(3/2) in 5D): only "
                          "whole (H-BITS-WITH-ENERGY, the board's, for the comparison with f N).  Not the event horizon: "
                          "eh_vs_trapping")
    R["write_floor"] = row(T, "computed", "owner o3_write W3",
                           "the gas bound, in units of m.  W4 (ii) made it the opening's duration (a spread inflow).  "
                           "Read as a lead before a compact crossing it is H-GAS-BOUND-AS-LEAD (new, the board's): the "
                           "README converges ~2e5 clocks with no horizon (against 160, 70: OPEN).  Whether a compact "
                           "converging shell can carry N bits is OPEN")
    R["eq17_static_end_state"] = row({"dlnFH_dr": s4["dlnFH_dr"], "negative": s4["negative_everywhere_sampled"]},
                                     "computed", "[PLANE]", "SIM1 S4 recomputed from the owner's data: a static end "
                                     "state reached with NEC matter in one spacetime is not eq. (17)")
    R["vaidya_raychaudhuri_identity"] = row({"residual": vi["residual"], "kappa": vi["kappa"], "R_kk": vi["R_kk"]},
                                            "computed", "[4D-VAIDYA]", "k(theta) - kappa theta + theta^2/2 + R(k,k) = 0 "
                                            "identically, with R(k,k) = 2 M'/r^2 > 0 for an inflow")
    R["vaidya_kretschmann"] = row(kr, "computed", "[4D-VAIDYA]", "owner engine: R_abcd R^abcd = 48 M(v)^2/r^6")
    keys_f = ("area_N", "mass_E", "share", "net", "moves_fraction", "moves_fraction_trapping",
              "readme_fraction_crossing_eh", "flux_along_eh", "eh_area_N_at_onset", "eh_born_before_inflow_m",
              "eh_theta_min_in_inflow", "fd_raychaudhuri_rel")
    R["forming_compact"] = row({k: fc[k] for k in keys_f}, "computed", "[4D-VAIDYA]; C^2 quintic onset",
                               "(a): the horizon forms as the README comes in -- area N A_bit (Birkhoff end state), mass "
                               "E, the README's whole mass, theta > 0 throughout, no partner.  The README CROSSES the "
                               "event horizon: it stands when the README begins, and all of its energy comes in across it")
    R["forming_spread"] = row({k: fsp[k] for k in keys_f}, "computed", "[4D-VAIDYA]; C^2 quintic onset",
                              "(a) spread over the write: the size moves over the whole write; the README crosses the "
                              "event horizon, born at the onset")
    R["eh_vs_trapping"] = row({"compact_eh_area_N_at_f": fc["eh_area_N_at_f"],
                               "compact_trapping_area_N_at_f": fc["trapping_area_N_at_f"],
                               "compact_eh_area_N_at_onset": fc["eh_area_N_at_onset"],
                               "compact_eh_born_before_inflow_m": fc["eh_born_before_inflow_m"],
                               "spread_eh_area_N_at_f": fsp["eh_area_N_at_f"],
                               "spread_eh_born_before_inflow_m": fsp["eh_born_before_inflow_m"],
                               "cubic_compact_eh_area_N_at_f": cub_c["eh_area_N_at_f"],
                               "cubic_compact_eh_born_before_inflow_m": cub_c["eh_born_before_inflow_m"]},
                              "computed", "[4D-VAIDYA]",
                              "which horizon: the trapping horizon holds f^2 N at a fraction f; the event horizon of a "
                              "compact inflow runs ahead of f N and stands at 0.77 N A_bit before the README; of a spread "
                              "inflow it is f^2 N but changes over the whole write.  'One whole' with 162's small cost "
                              "holds on the trapping horizon of a compact inflow only (H-SIZE-IS-TRAPPING-HORIZON)")
    R["onset_regularity"] = row({"quintic": on_q, "cubic": on_c, "cubic_spread_theta_min": cub_s["eh_theta_min_in_inflow"],
                                 "cubic_spread_eh_born_before_inflow_m": cub_s["eh_born_before_inflow_m"]},
                                "computed", "[4D-VAIDYA]",
                                "the first build's C^1 cubic (M ~ v^2 at onset) leaves a curvature singularity at the "
                                "spread inflow's onset that an escaping ray sees (K ~ v^-2; against 174 (1)'s strict "
                                "rule); the C^2 quintic (M ~ v^3) keeps K bounded -- a profile artefact, removed")
    R["crossing_by_run"] = row({k: {"crosses_eh": r["readme_fraction_crossing_eh"], "net": r["net"],
                                    "horizon_forms": r["horizon_forms"]} for k, r in runs.items()}, "computed",
                               "[4D-VAIDYA]", "wherever a horizon exists while the README comes in, all of its energy "
                               "crosses the event horizon -- with the exact partner too (net 0)")
    R["end_state_is_vacuum"] = row({"Mprime_after_inflow": 0, "R_kk_after_inflow": 0}, "deduced; standard-not-READ",
                                   "[4D-VAIDYA]", "after the inflow M' = 0, so R(k,k) = 2M'/r^2 = 0 and the exterior is "
                                   "vacuum Schwarzschild (Birkhoff): 'held' is H1/G1's count of this end state, not a "
                                   "held stress")
    R["closing_cost"] = row("the horizon's ending and the hold's transfer need its area to decrease", "deduced; "
                            "standard-not-READ; OPEN", "area theorem", "under the NEC an event horizon's area never "
                            "decreases (theta < 0 needs R(k,k) < 0 on its generators): (a) moves the demand for negative "
                            "null energy from the inflow to the closing (109, 115 (a), 136 (2), 106, E1, E2)")
    R["pre_no_partner"] = row({k: pn[k] for k in ("area_N", "mass_E", "share", "eh_theta_min_in_inflow")}, "computed",
                              "[4D-VAIDYA]", "(b) without a partner: 4 N A_bit and 2E -- H1, G1 and 133 broken, and "
                              "the size changes")
    R["pre_exact_partner_spread"] = row({k: pp[k] for k in ("area_N", "mass_E", "share", "net", "moves_fraction",
                                                            "readme_fraction_crossing_eh", "eh_theta_min_in_inflow",
                                                            "eh_theta_max_in_inflow")},
                                        "computed", "[4D-VAIDYA]", "(b) with the exact partner (163's option text): "
                                        "size fixed (theta = 0), the README crossing it, its share of the mass 0 -- one "
                                        "member of a pair; admitted by 183, set aside only on the board's reading of 195")
    R["five_dim_scaling"] = row({"area_ratio_b_without_partner_5D": 2 ** 1.5, "area_ratio_b_without_partner_4D":
                                 pn["area_N"]}, "deduced; standard-not-READ", "[FREE] law, 5D scaling",
                                "Tangherlini: area grows as M^(3/2) in five dimensions; (b) without a partner ends at "
                                "2.83 N A_bit, not N -- the factor changes, the verdict does not")
    R["forming_with_partner"] = row({"horizon_forms": fp["horizon_forms"], "area_N": fp["area_N"]}, "computed",
                                    "[4D-VAIDYA]", "a partner on a forming horizon cancels the horizon itself")
    for w, res in worlds.items():
        R["cypher_" + w.replace("-", "_")] = row(res, "computed", "the board's encoding (H-CYPHER-README-HELD-INDEX)",
                                                 WORLD_NAMES[w] + "; roster 1173; the cypher classifies, it does not "
                                                 "derive")
    R["cypher_invariance"] = row(inv, "computed", "the board's encoding", "the law index rebuilt from mutated physics: "
                                 "the verdicts do not move (ordinal invariance) -- a limit of the cypher, not a finding")
    R["record"] = row([{"item": i, "source": s, "reading": rd, "why": w} for i, s, rd, w in RECORD], "READ; deduced",
                      "", "verdicts are the board's readings; quotes verbatim (check C10)")
    R["lemma_rows"] = row({k: {"row": LEMMA_ROWS[k], "reading": v[0], "why": v[1]} for k, v in LEMMA_VERDICTS.items()},
                          "READ; deduced", "warptheorem.py", "")
    R["kehle_unger"] = row("We construct examples of black hole formation from regular, one-ended asymptotically flat "
                           "Cauchy data for the Einstein-Maxwell-charged scalar field system in spherical symmetry "
                           "which are exactly isometric to extremal Reissner-Nordstrom after a finite advanced time "
                           "along the event horizon.", "READ", "arXiv:2211.15742v2 PDF p.1",
                           "a forming horizon can be exactly extremal after a finite advanced time: a precedent beside "
                           "(a), never a supply; charge, not eq. (17)")
    R["consequences"] = row(CONSEQUENCES, "deduced; OPEN", "", "the board's readings")
    R["record_check"] = row(rc, "computed", "", "")
    out = {"results": R, "wall_s": round(_wall.perf_counter() - t0, 1),
           "binary_statement": BINARY_STATEMENT, "readings": READINGS}
    _CACHE["out"] = out
    return out


BINARY_STATEMENT = ("195's note, in two halves.  (i) HELD, NOT CROSSING: the README comes in held by the corridor's "
                    "horizon -- its N bits the horizon's area (H1), its energy the horizon's mass (G1) -- with nothing "
                    "crossing that horizon (target T_IN_HELD_NOT_CROSSING).  (ii) TIMING: its inflow at the opening "
                    "(R0) comes in as one whole while that horizon forms, so that no net null flux crosses a horizon of "
                    "fixed size and Lemma S asks no partner (target T_FORMS_CROSSING, against T_STRICT, T_GLOSS and "
                    "T_PAIR).")
READINGS = {
    "M's, as carried": ["H-README-NOT-A-PAIR (195)", "H-HORIZON-AND-THROAT-HOLD (132)", "H-README-IS-ENERGY (136 G)",
                        "H-INFORMATION-IS-ENERGY (190)", "H-ONE-EXACT-ENERGY (133)", "H-FIXED-SIZE (162)",
                        "H-AT-ONCE-IS-WHOLE (163)", "H-CORRIDOR-IS-OPENING (160)", "H-INFLOW-IS-README (115 (c))",
                        "H-THREE-HOLDS (106)", "H-CORRIDOR-TAKES (70)", "H-NEC-NEVER-VIOLATED-AS-PAIR (183)",
                        "H-PAIRING-HELD-AS-TENSION (189)", "H-README-ON-P2 (172 (1))", "H-SINGLE-CHANNEL-GROWS (94)",
                        "H-INSTANTANEOUS (94; 86 (5); 136 E)", "H-HORIZON-NEEDS-OBJECT (109)",
                        "H-P1-HORIZON-ENDS (115 (a))"],
    "the board's, refuted as worded in its own models": ["H-README-HELD (195's note: held, not crossing)"],
    "the board's, used": ["H-ARRIVAL-FORMS-THE-HORIZON (the surviving reading: the README crosses the horizon it forms)",
                          "H-README-NOT-ONE-MEMBER (195 read as 'not one member of a pair')",
                          "H-WRITE-AT-FIXED-SIZE (reading (b): the option text of 163)",
                          "H-SIZE-FROM-WHOLE (162's fixed size counted from the whole README's coming in)",
                          "H-SIZE-IS-TRAPPING-HORIZON (the corridor's 'size' read on r = 2M(v), not on the EH)",
                          "H-WHOLE-AS-G1 (163's 'one whole' read as G1's f^2 on the trapping horizon)",
                          "H-GAS-BOUND-AS-LEAD (new: W3's floor as a lead before a compact crossing; not W4 (ii))",
                          "H-BITS-WITH-ENERGY", "H-README-AS-NULL-DUST (the crossing control)",
                          "H-FIXED-SIZE-AS-THETA-ZERO", "H-CYPHER-README-HELD-INDEX (the encoding)",
                          "H-TEST-EVENT-WORLD (the control: the README carrying no gravity)"],
}
CONSEQUENCES = {
    "H-README-HELD (195's note)": "Refuted as worded, in every computed model: the README crosses the horizon it forms.  "
          "'Held' holds only of the end state (H1/G1), and that end state is vacuum Schwarzschild, not a held stress on "
          "eq. (17) (S4).  The reading to work is H-ARRIVAL-FORMS-THE-HORIZON (OPEN).",
    "F5": "For the INFLOW only: on (a) no generator of a fixed-size horizon carries the README's net flux, so the exact "
          "+/- pair is not demanded by the inflow; F5 becomes moot on (a) for the inflow -- neither green nor refuted.  "
          "On (b) with the partner F5 stays demanded; (b) is closed only on the board's reading of 195 (or the share-1 "
          "reading of 136 G / 190), not by M's words.",
    "closing and transfer (109, 115 (a), 136 (2), 106, E1, E2)": "On (a) the horizon's ending at the closing and the "
          "move of 106's hold from horizon 1 to horizon 2 need the horizon's area to DECREASE, which the NEC forbids (the "
          "area theorem, standard-not-READ; theta < 0 needs R(k,k) < 0 on its generators -- Lemma S's bulk form run in "
          "reverse).  A negative null flux, or a non-classical mechanism, is demanded there (OPEN).  (a) moves the "
          "demand for negative null energy from the inflow to the closing; it does not remove it.",
    "E-PASS test-event framing (RI-5)": "Sharpened, not answered: the README is not a test event but the horizon's "
          "whole source (share 1), and it crosses that horizon as it forms it.  E-PASS's crossing of a horizon of fixed "
          "size is the board's configuration (195, read as the board reads it); S3b's bar is the reason (a) is forced "
          "once (b) is closed.",
    "B4d": "The problem changes, on (a): from a fixed-size corridor kept regular through >= 2.0e5 clocks of write with "
           "the README crossing (stage 5, the option text of 163) to (1) the README's whole inflow forming the corridor "
           "(a collapse; the trapping horizon appears at the README's size within the inflow's width), (2) the formed "
           "corridor staying regular while it holds, and (3) its closing, which needs a negative null flux (OPEN).  "
           "Stage 5's singular surface (8-16 clocks with eq. (17) on a positive-tension plane) still bounds a held "
           "interval on that plane.  End-state cautions: eq. (17) is not a static end state of NEC inflow in one "
           "spacetime (S4, [PLANE]); a forming horizon can be exactly extremal after finite advanced time (Kehle-Unger, "
           "READ; charge, not eq. (17)).  Under 179 the bulk corridor's formation is OPEN.",
    "O3": "The write's floor (>= 2.0e5 clocks, W3).  W4 (ii) made it the opening's duration (a spread inflow).  Read as a "
          "lead before a compact crossing (H-GAS-BOUND-AS-LEAD, new, the board's), the README converges for ~2e5 clocks "
          "with no horizon, so the convergence is not the corridor -- uneasy with 160 and 70 (OPEN).  The small 162 cost "
          "holds only if a compact converging shell can carry N bits (OPEN); otherwise W4 (ii)'s spread inflow applies "
          "and the size changes across the whole write.  O3 stays OPEN.",
}


# ============================================================================================ checks
def _ok_zero(x, tol=1e-12):
    try:
        return abs(float(x)) < tol
    except TypeError:
        return False


def check_C1(mut=None):
    hs = held_stress(1 if mut == "singular-held" else 0)
    ok = hs["owner_tau_xixi"] == 0 and hs["owner_pi_xixi"] == 0 and hs["tau_xixi_limit"] == 0 and \
        hs["g_xixi_on_H"] == 0
    return ok, {"tau_xixi_limit": str(hs["tau_xixi_limit"]), "owner": [str(hs["owner_tau_xixi"]),
                                                                       str(hs["owner_pi_xixi"])]}


def check_C2(mut=None):
    cc = crossing_control(area_power=1 if mut == "r^2->r" else 2)
    m = F.M_SYM
    ok = cc["chart_T_xixi"] == 2 and sp.simplify(cc["P1_per_generator"] - 1 / (2 * m)) == 0 and \
        sp.simplify(cc["partner_per_generator"] + 1 / (2 * m)) == 0 and cc["kappa_x_m"] == 0
    return ok, {k: str(v) for k, v in cc.items()}


def check_C3(mut=None):
    ls = lemma_s_forms(fixed_mut=("grow" if mut == "grow-in-fixed-slot" else None))
    ok = (ls["fixed_theta"] == 0 and ls["fixed_R_xixi"] == 0 and _ok_zero(ls["fixed_R_xixi_witness"])
          and ls["shear_R_xixi_witness"] < -1e-6 and ls["grow_R_xixi_witness"] > 1e-6
          and _ok_zero(ls["grow_raychaudhuri_residual_witness"]) and ls["sheet_K_xixi"] == 0)
    return ok, {k: str(v) for k, v in ls.items()}


def check_C4(mut=None):
    h = h1_per_bit(m2_factor=2 if mut == "m2-doubled" else 1)
    return bool(h["is_4ln2"]), {k: str(v) for k, v in h.items()}


def check_C5(mut=None):
    w = whole_only(e_exponent=1 if mut == "E-linear-in-N" else sp.Rational(1, 2))
    w5 = whole_only(e_exponent=1 if mut == "E-linear-in-N" else sp.Rational(2, 3))
    return bool(w["only_whole"] and w5["only_whole"]), {"held_over_share_4D": str(w["held_over_share"]),
                                                        "held_bits_5D": str(w5["held_bits_over_N"]),
                                                        "samples": {k: str(v) for k, v in w["samples"].items()}}


def check_C6(mut=None):
    vi = vaidya_identity(drop_rkk=(mut == "drop-Rkk"))
    M = MF(VV)
    ok = vi["residual"] == 0 and sp.simplify(vi["kappa"] - M / RR**2) == 0 and \
        sp.simplify(vi["R_kk"] - 2 * sp.diff(M, VV) / RR**2) == 0 and vi["geodesic_check"] == 0
    return ok, {k: str(v) for k, v in vi.items()}


def check_C7(mut=None):
    T = 2.0e5
    ps = -1.0 if mut == "partner-sign-flipped" else 1.0
    ae = 1.0 if mut == "area-linear-in-M" else 2.0
    fc = vaidya_run(0, 0, 1.0, T, partner_sign=ps, area_exp=ae)
    pn = vaidya_run(1, 0, 1.0, T, partner_sign=ps, area_exp=ae)
    pp = vaidya_run(1, 1, 1.0, T, partner_sign=ps, area_exp=ae)
    fp = vaidya_run(0, 1, 1.0, T, partner_sign=ps, area_exp=ae)
    ok = (abs(fc["area_N"] - 1) < 1e-8 and abs(fc["mass_E"] - 1) < 1e-12 and abs(fc["share"] - 1) < 1e-12
          and fc["eh_theta_min_in_inflow"] > 0 and fc["fd_raychaudhuri_rel"] < 1e-4
          and abs(pn["area_N"] - 4) < 1e-8 and abs(pn["mass_E"] - 2) < 1e-12 and pn["eh_theta_min_in_inflow"] > 0
          and abs(pp["area_N"] - 1) < 1e-8 and pp["share"] == 0 and abs(pp["eh_theta_min_in_inflow"]) < 1e-9
          and fp["horizon_forms"] is False)
    return ok, {"forming": [fc["area_N"], fc["mass_E"], fc["share"], fc["eh_theta_min_in_inflow"],
                            fc["fd_raychaudhuri_rel"]], "pre_no_partner": [pn["area_N"], pn["mass_E"]],
                "pre_partner": [pp["area_N"], pp["share"], pp["eh_theta_min_in_inflow"]],
                "forming_partner_forms": fp["horizon_forms"]}


def check_C8(mut=None):
    grav = mut != "readme-no-gravity"
    sc = scenarios(write=2.0e5, readme_gravitates=grav)
    cells, _ = cells_from(sc, held_share=("1" if grav else "0"))
    if mut == "test-event-cell":
        cells = cells + [list(TEST_EVENT_CELL)]
    bad = [c for c in cells if c[6] != "0" and c[7] == 0]
    disagree = [(r_["pre"], r_["partner"], r_["spread"]) for r_ in sc["runs"]
                if _moves_code(r_["moves_fraction"]) != _moves_code(r_["moves_fraction_trapping"])]
    return not bad and not disagree, {"cells": len(cells), "net_positive_at_fixed_size": bad,
                                      "eh_vs_trapping_code_disagree": disagree}


def _tk(prefix):
    return [k for k in TARGETS if k.startswith(prefix)][0]


def _lk(prefix):
    return [k for k in LOGIC if k.startswith(prefix)][0]


def check_C9(mut=None):
    T = 2.0e5
    sc = scenarios(write=T)
    sct = scenarios(write=T, readme_gravitates=False)
    law = cypher_run("test-event" if mut == "control-for-law" else "law", sc, sct,
                     witness=("law+net=1-partner" if mut == "witness-net-clause" else "law"))
    tev = cypher_run("test-event", sc, sct)
    pla = cypher_run("planted", sc, sct)
    neg = cypher_run("negative", sc, sct,
                     extra=(list(TEST_EVENT_CELL) if mut == "planted-as-negative" else negative_cell(T)))
    bearing = [l_ for l_ in OPB if law["languages"][l_]["state"] == "SPEAKS"]
    a = (len(bearing) >= 3
         and all(law["targets"][_tk("T_IN_HELD")]["admitted"][l_] is False for l_ in bearing)
         and law["targets"][_tk("T_FORMS")]["is_a_computed_cell"]
         and all(law["targets"][_tk("T_FORMS")]["admitted"][l_] is True for l_ in bearing)
         and all(law["targets"][_tk(t)]["admitted"][l_] is False for t in ("T_STRICT", "T_GLOSS") for l_ in bearing))
    l6 = _lk("L6")
    b = (law["logic"][l6]["cells"] == {"fixed": True, "values": [1]}
         and all(law["logic"][l6]["languages"][l_] == {"fixed": True, "values": [1]} for l_ in bearing))
    c = (tev["logic"][l6]["cells"]["fixed"] is False
         and all(v_["fixed"] is False for v_ in tev["logic"][l6]["languages"].values()))
    dd = (all(neg["targets"][_tk(t)]["admitted"][l_] is False for t in ("T_STRICT", "T_GLOSS", "T_IN_HELD")
              for l_ in OPB if l_ in neg["languages"] and neg["languages"][l_]["state"] == "SPEAKS")
          and neg["logic"][_lk("L1")]["cells"] == {"fixed": True, "values": ["0"]})
    e = law["languages"]["analysis"]["state"] == "SPEAKS" and pla["languages"]["analysis"]["state"] == "SILENT"
    return a and b and c and dd and e, {"bearing": bearing, "law_targets": a, "L6_law": b, "L6_flips_on_control": c,
                                        "negative_flips_nothing": dd, "analysis_computed": e,
                                        "L6_law_languages": law["logic"][l6]["languages"],
                                        "L6_control_languages": tev["logic"][l6]["languages"]}


def check_C10(mut=None):
    words = {**M_WORDS, **BOARD_WORDS}
    if mut == "altered-M-quote":
        words["162"] = words["162"].replace("doesn't change size", "does not change size")
    if mut == "swapped-items":
        words["160"], words["161"] = words["161"], words["160"]
    rc = record_check(words)
    return rc["all_quotes"] and rc["all_lemma_rows"], {"missing": [k for k, v in rc["quotes_found_in_own_item"].items()
                                                                    if not v], "lemma_rows": rc["lemma_rows_found"]}


def _keys(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            acc.add(str(k))
            _keys(v, acc)
    elif isinstance(o, list):
        for v in o:
            _keys(v, acc)
    return acc


def check_C11(mut=None):
    out = json.loads(json.dumps(_clean(compute())))
    if mut == "planted-key-hold_time":
        out["results"]["hold_time"] = row(1, "computed")
    if mut == "row-without-label":
        out["results"]["unlabelled"] = {"value": 1}
    keys = _keys(out, set())
    bad_keys = sorted(k for k in keys if any(b in k.lower() for b in BANNED_KEYS)
                      and k not in TARGETS and not k.startswith(("L1", "L2", "L3", "L4", "L6")))
    funcs = [f for f in globals().values() if inspect.isfunction(f) and f.__module__ == __name__]
    bad_args = sorted({(f.__name__, p) for f in funcs for p in inspect.signature(f).parameters if p in BANNED_ARGS})
    bad_labels = []
    for k, r in out["results"].items():
        lab = r.get("label", "") if isinstance(r, dict) else ""
        toks = [t.strip() for t in lab.split(";") if t.strip()]
        if not toks or any(t not in LABELS for t in toks):
            bad_labels.append(k)
    return not (bad_keys or bad_args or bad_labels), {"bad_keys": bad_keys, "bad_args": bad_args,
                                                       "bad_labels": bad_labels}


def check_C12(mut=None):
    wf = write_floor(z=2 if mut == "Z=2" else None)
    ok = 1.9e5 < wf["floor_in_m"] < 2.1e5 and wf["w1_2E_gives"] == "4"
    return ok, wf


def check_C13(mut=None):
    s4 = eq17_radial_rkk(data="schwarzschild" if mut == "schwarzschild-data" else "eq17")
    ok = s4["negative_everywhere_sampled"] and sp.simplify(s4["dlnFH_dr"] + 1 / ((sp.Symbol("r", positive=True) - 2) *
                                                                               (2 * sp.Symbol("r", positive=True) - 3))) == 0
    return ok, {"dlnFH_dr": str(s4["dlnFH_dr"]), "samples": s4["samples"]}


def check_C14(mut=None):
    T = 2.0e5
    hz = "trapping" if mut == "eh-at-trapping" else "event"
    fc = vaidya_run(0, 0, 1.0, T, horizon=hz)
    cells, _ = cells_from(scenarios(write=T, horizon=hz), crosses_rule=("net" if mut == "crosses-from-net-label"
                                                                        else "eh"))
    by = {(c[0], c[1], c[2]): c for c in cells[:12]}
    ok = (fc["readme_fraction_crossing_eh"] > 1 - 1e-9 and 1.70 < fc["eh_r_at_onset"] < 1.80
          and fc["flux_along_eh"] > 0.4
          and by[("1", "1", 0)][8] == 1 and by[("1", "1", 0)][6] == "0" and by[("1", "1", 1)][8] == 1
          and by[("0", "1", 0)][8] == 0 and by[("0", "1", 1)][8] == 0
          and all(c[8] in (0, 1) for c in cells) and all(c[8] == 1 for c in cells[:12] if c[6] != "0"))
    return ok, {"crossing_fraction": fc["readme_fraction_crossing_eh"], "eh_r_at_onset": fc["eh_r_at_onset"],
                "flux_along_eh": fc["flux_along_eh"], "crosses_codes": [c[8] for c in cells]}


def check_C15(mut=None):
    T = 2.0e5
    hz = "trapping" if mut == "eh-at-trapping" else "event"
    fc = vaidya_run(0, 0, 1.0, T, horizon=hz)
    fs = vaidya_run(0, 0, T, T, horizon=hz)
    born_c = fc["eh_born_before_inflow_m"] or 0.0
    born_s = fs["eh_born_before_inflow_m"] or 0.0
    ok = (all(fc["eh_area_N_at_f"][k] > float(k) for k in fc["eh_area_N_at_f"])
          and all(abs(fc["trapping_area_N_at_f"][k] - float(k) ** 2) < 1e-9 for k in fc["trapping_area_N_at_f"])
          and born_c > 3.0
          and all(abs(fs["eh_area_N_at_f"][k] - float(k) ** 2) < 1e-3 for k in fs["eh_area_N_at_f"])
          and abs(born_s) < 1e-3 * T)
    return ok, {"compact_eh_at_f": fc["eh_area_N_at_f"], "compact_born_before": born_c,
                "spread_eh_at_f": fs["eh_area_N_at_f"], "spread_born_before": born_s}


def check_C16(mut=None):
    kr = kretschmann()
    on = onset_regularity("cubic" if mut == "cubic-default" else None)
    oc = onset_regularity("cubic")
    ok = (sp.simplify(kr - 48 * MF(VV) ** 2 / RR ** 6) == 0 and on["escapes"] and on["ray_starts_outside_eh"]
          and on["ratio_v0_to_100v0"] < 1.5 and oc["escapes"] and oc["ratio_v0_to_100v0"] > 1e3)
    return ok, {"kretschmann": str(kr), "default": {k: on[k] for k in ("profile", "ratio_v0_to_100v0", "escapes",
                                                                        "ray_starts_outside_eh")},
                "cubic_ratio": oc["ratio_v0_to_100v0"]}


CHECKS = {
    "C1": (check_C1, "held regular stress: T(xi,xi) = 0 on the horizon (owner), no partner asked ([PLANE])",
           [("singular-held", "rho = rho0/F, singular on the horizon")]),
    "C2": (check_C2, "the crossing control on a FIXED-size horizon: 1/(2m) per generator on P1, partner -1/(2m)",
           [("r^2->r", "the owner's area-power mutation")]),
    "C3": (check_C3, "Lemma S premises [FREE]: theta = 0 -> R = 0; shear -> R < 0; growth -> R > 0, residual 0; sheet K = 0",
           [("grow-in-fixed-slot", "the growing horizon put where the fixed one belongs")]),
    "C4": (check_C4, "H1 with G1: 4 ln2 Planck areas per bit (STRUCTURAL; G1 as seated, 4D)",
           [("m2-doubled", "m^2 doubled")]),
    "C5": (check_C5, "a forming trapping horizon holds the README only whole (f^2 N in 4D, f^(3/2) N in 5D)",
           [("E-linear-in-N", "E proportional to N instead of sqrt N")]),
    "C6": (check_C6, "Vaidya: non-affine Raychaudhuri identity, kappa = M/r^2, R(k,k) = 2M'/r^2",
           [("drop-Rkk", "the R(k,k) term dropped")]),
    "C7": (check_C7, "Vaidya runs: forming -> N A_bit, E, share 1, theta > 0; pre -> 4 N A_bit, 2E; pre + partner -> "
                     "theta = 0, share 0; forming + partner -> no horizon",
           [("partner-sign-flipped", "the partner with positive energy"), ("area-linear-in-M", "area read as M, not M^2")]),
    "C8": (check_C8, "measured on the EH: no cell has a net inflow at a fixed size; the EH and trapping codes agree",
           [("test-event-cell", "RI-5's test-event cell planted"),
            ("readme-no-gravity", "the runs re-integrated with the README carrying no gravity")]),
    "C9": (check_C9, "the cypher: on LAW all bearing languages refuse T_IN_HELD_NOT_CROSSING, T_STRICT, T_GLOSS and "
                     "admit T_FORMS_CROSSING (a cell); L6 fixed at 1 in every language; the test-event world flips "
                     "L6; the negative control flips nothing; analysis' state computed from its residual",
           [("control-for-law", "the test-event world run in the LAW slot"),
            ("witness-net-clause", "the first build's witness clause net = 1 - partner declared"),
            ("planted-as-negative", "the planted test-event cell put where the negative control belongs")]),
    "C10": (check_C10, "M's words verbatim inside their own items; warptheorem.py's rows as quoted",
            [("altered-M-quote", "one word of 162 changed"), ("swapped-items", "160 and 161 swapped")]),
    "C11": (check_C11, "guards: no banned key or argument; every row labelled with the six labels",
            [("planted-key-hold_time", "a key naming a time"), ("row-without-label", "a row with no label")]),
    "C12": (check_C12, "the write floor is the owner's 2.0e5 (Z = 108.75); W1 control 2E gives 4N", [("Z=2", "Z = 2")]),
    "C13": (check_C13, "SIM1 S4 from owner data: eq. (17)'s d ln(F/H)/dr = -1/((r-2)(2r-3)) < 0",
            [("schwarzschild-data", "Schwarzschild data in eq. (17)'s place")]),
    "C14": (check_C14, "crossing, measured on the EH: all of the README's energy crosses the EH it forms (r_EH = 1.75 "
                       "at onset; flux along the EH > 0); with the exact partner it crosses at net 0; no horizon, no "
                       "crossing",
            [("crosses-from-net-label", "crosses coded from the label net"),
             ("eh-at-trapping", "the trapping horizon put where the event horizon belongs")]),
    "C15": (check_C15, "which horizon: compact EH area above f N at f = 0.1, 0.5, 0.9 and born > 3 m before; trapping "
                       "f^2 N; spread EH f^2 N, born at the onset",
            [("eh-at-trapping", "the trapping horizon put where the event horizon belongs")]),
    "C16": (check_C16, "onset: Kretschmann 48 M^2/r^6 (owner engine); with the default C^2 quintic it stays bounded "
                       "along an escaping ray from the spread onset; the C^1 cubic's grows as v^-2",
            [("cubic-default", "the C^1 cubic made the default profile")]),
}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, set)):
        return [_clean(v) for v in o]
    if isinstance(o, (sp.Basic, Fr)):
        return str(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


def selftest():
    t0 = _wall.perf_counter()
    allok = True
    print("readme_held selftest (computed, READ and deduced; checked by two separate AI sessions in this project; "
          "not seated)")
    for cid, (fn, what, _m) in CHECKS.items():
        ok, det = fn(None)
        allok = allok and ok
        print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {what}\n      {json.dumps(_clean(det))[:600]}")
    print(f"selftest {'PASSED' if allok else 'FAILED'}: {len(CHECKS)} checks, wall {_wall.perf_counter() - t0:.1f} s")
    return allok


def mutants():
    t0 = _wall.perf_counter()
    passed, n = [], 0
    print("readme_held --mutants: each named mutation must make its check FAIL")
    for cid, (fn, what, muts) in CHECKS.items():
        for name, desc in muts:
            n += 1
            ok, det = fn(name)
            if ok:
                passed.append((cid, name))
            print(f"{cid:4s} [{name}] {desc}: {'check FAILS (as required)' if not ok else 'MUTATION PASSES'}\n"
                  f"      {json.dumps(_clean(det))[:400]}")
    print(f"mutants: {n} run, {n - len(passed)} caught, {len(passed)} passed {passed}; wall "
          f"{_wall.perf_counter() - t0:.1f} s")
    return not passed


def report():
    out = _clean(compute())
    R = out["results"]
    print("readme_held -- items 195/196 (computed, READ and deduced; not seated)")
    for k in ("held_stress_T_xixi", "held_stress_singular_control", "crossing_control", "lemma_s_bulk_and_sheet",
              "H1_area_per_bit", "whole_only", "write_floor", "eq17_static_end_state", "vaidya_raychaudhuri_identity",
              "vaidya_kretschmann", "forming_compact", "forming_spread", "eh_vs_trapping", "onset_regularity",
              "crossing_by_run", "end_state_is_vacuum", "closing_cost", "pre_no_partner", "pre_exact_partner_spread",
              "five_dim_scaling", "forming_with_partner"):
        print(f"\n{k} [{R[k]['label']}] {R[k]['tag']}\n  {json.dumps(R[k]['value'])[:1200]}\n  {R[k]['note']}")
    for k in ("cypher_law", "cypher_test_event", "cypher_planted", "cypher_negative"):
        c = R[k]["value"]
        print(f"\n{k}: {c['index']}  d = {c['d']}  cells = {c['cells']}  box = {c['box']}")
        for lang, v in c["languages"].items():
            print(f"  {lang:12s} {v['state']:7s} {v.get('admits', '-')!s:>6} E={v.get('E', '-')!s:>6}  "
                  f"{v.get('note', v.get('witness', ''))[:110]}")
        print(f"  K.langclose holds: {c['K_langclose_holds']}; languages agree: {c['languages_agree']}; pairs agreeing: "
              f"{c['pairs_agreeing']}; information adds nothing: {c['information_adds_nothing']}; keys: "
              f"{c['information_keys']}")
        for t, v in c["targets"].items():
            print(f"  {t[:70]}...\n    computed cell: {v['is_a_computed_cell']}; admitted: {v['admitted']}; "
                  f"STRUCTURAL NO possible: {v['NO_is_STRUCTURAL']} (never seen: {v['values_never_seen']}, "
                  f"{v['n_pairs_never_seen']} pairs, e.g. {v['value_pairs_never_seen'][:3]})")
        for lk, lv in c["logic"].items():
            print(f"  logic {lk[:60]}: cells {lv['cells']}; languages "
                  f"{ {l_: (x['fixed'], x['values']) for l_, x in lv['languages'].items()} }")
    print("\ncypher_invariance:", json.dumps(R["cypher_invariance"]["value"])[:1500])
    print("\nrecord:")
    for r_ in R["record"]["value"]:
        print(f"  {r_['item']:46s} {r_['reading']:32s} {r_['why'][:150]}")
    print("\nlemma rows:", json.dumps(R["lemma_rows"]["value"])[:1200])
    print("\nconsequences:")
    for k, v in R["consequences"]["value"].items():
        print(f"  {k}: {v}")
    print(f"\nBINARY STATEMENT: {out['binary_statement']}")
    print(f"record check: {R['record_check']['value']['all_quotes']} quotes, {R['record_check']['value']['all_lemma_rows']} rows")
    print(f"wall {out['wall_s']} s")


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
            json.dump(_clean(compute()), fh, indent=1)
        print(f"wrote {a.json}")
    if not (a.selftest or a.mutants or a.json):
        report()
    return rc


if __name__ == "__main__":
    sys.exit(main())
