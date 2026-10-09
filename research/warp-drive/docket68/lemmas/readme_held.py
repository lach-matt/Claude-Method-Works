#!/usr/bin/env python3
"""readme_held.py -- items 195 and 196: is the README HELD by the corridor's horizon, and does it come in while that
horizon forms?  Computed, READ and deduced; not verified; not seated; 2026-10-09.

PLAIN WORDS FIRST.
  M said in 195: "The README is not a pair".  The board's reading of what that leaves (195's own note) is that the
  README is HELD by the corridor's horizon -- its N bits are the horizon's area (H1), its energy is the horizon's mass
  (G1) -- rather than crossing a horizon that already has its size.  Two questions follow, and this instrument
  computes both, then puts them to the cypher (196).
  (1) Held: a held stress that is regular on the horizon carries no null energy along it, so Lemma S asks it for no
      partner.  Computed (owner lemmas/epass_pairing.py).  The README as null dust CROSSING the horizon is the control:
      it carries 1/(2m) per generator on P1 (owner lemmas/epass_frames.py), so Lemma S asks for a partner of -1/(2m).
  (2) When it comes in.  Along a horizon that keeps its size the generators do not expand (theta = 0), and then
      Raychaudhuri gives R(k,k) = -sigma^2 <= 0: positive energy cannot come in net (owner Lemma S, bulk form, [FREE];
      SIM1 S3b).  So there are exactly two ways in, and no third:
        (a) the README comes in WHILE the horizon forms -- the horizon grows from nothing to exactly N A_bit and mass E
            as it comes in, and no partner is asked (computed below: Vaidya, Raychaudhuri, every profile tried);
        (b) the README crosses a horizon that ALREADY has the README's size -- then either a partner cancels it (the
            README becomes one member of a +/- pair, which is 194's object and what 195 says the README is not), or the
            horizon grows to 4 N A_bit and mass 2E (computed), breaking H1, G1 and 133's one exact energy.
      With 195, (b) is closed both ways; (a) is what is left.  (a) costs something, stated as plainly (135): while the
      README comes in, the horizon's size changes (from nothing to the README's), so 162's "The throat doesn't change
      size" holds from the moment the whole README is in -- at every moment only if the inflow is instantaneous, which
      163 did not choose; and the board's own wording inside the option M chose in 163 ("at the fixed size; the write
      lasts at least ~200,000 clocks; B4d must keep the fixed-size corridor regular for that long") is (b)'s framing and
      does not survive.  The gas bound survives as the opening's lead (O3-WRITE reading (ii)): it limits how early the
      README must start, not how long it takes to cross r = 2m.
  A forming horizon holds the README only as a WHOLE: with a fraction f of E in, its area is f^2 N A_bit, short of the
  f N bits in proportion (G1: E grows as sqrt N).  That is 163's "All together, one whole", computed.

THE CYPHER (196; §33; tools/cypher.py imported by path, registered in sys.modules before exec_module).  Roster 1173
(M's choice for these runs: order, algebra, analysis, geometry, information, statistics, documentary); logic is the
mechanism that returns each language's binary.  The index is the board's encoding (H-CYPHER-README-HELD-INDEX): each
cell is one COMPUTED configuration of the Vaidya family (pre-existing horizon or not; partner fraction 0, 1/2, 1;
compact or spread inflow) plus the held state of the owner's held stress; the eight ordinal coordinates are read off the
run, never assigned.  The cypher CLASSIFIES: an admitted cell is not a derived physical value, and a closure is not a
law.  A target admitted because it is itself a computed cell is said to be so.  A NO is called STRUCTURAL where a value
or a pair of values the target needs was never seen in any computed cell (no closure can admit what was never seen).
analysis answers only with a declared witness; documentary returns citations, not a binary; NOT-RUN is never SILENT;
agreement at two coordinates would be DEGENERATE (d = 8 here).  CONTROL: the board's test-event framing added as a
cell (the README absorbed by a horizon that keeps its size, mass and area, with no partner -- RI-5's framing, which
breaks the Einstein equation); it must flip what the law index says.

LABELS.  computed / READ (verbatim + page) / deduced / STRUCTURAL / standard-not-READ / OPEN.  The board's readings are
named H-... and kept apart from M's words, which are quoted verbatim (typing kept) and checked inside their own item.
Tags: [FREE] holds whatever carries the corridor; [PLANE] uses eq. (17) as a plane's own metric (the board's pre-179
configuration; under 179/180 and seated (G), at most a plane's reading of the mouth, OPEN); [4D-VAIDYA] the standard
spherically symmetric null-dust family (standard-not-READ) used as the plainest model of an inflow, units m = 1 where
m = G E/c^4 is the README's (G1).  No key or argument names a separation, a distance, a speed or a redshift (139 (4),
101 (7)); the advanced coordinate v is called v and widths are fractions of the write.

M'S WORDS USED (verbatim, typing kept; checked inside their own items, check C10): see M_WORDS.  The board's wording in
163's option, which M chose, is quoted under a key that says it is the board's (BOARD_WORDS), never as M's.

READ (verbatim, transliterated to ASCII):
  Kehle & Unger, "Gravitational collapse to extremal black holes and the third law of black hole thermodynamics",
  arXiv:2211.15742v2, PDF p.1 (abstract): "We construct examples of black hole formation from regular, one-ended
  asymptotically flat Cauchy data for the Einstein-Maxwell-charged scalar field system in spherical symmetry which are
  exactly isometric to extremal Reissner-Nordstrom after a finite advanced time along the event horizon."  and "In
  particular, our result can be viewed as a definitive disproof of the "third law of black hole thermodynamics.""
  Read 2026-10-09 through the alphaXiv connector (full text served; the abstract, title page and contents were read,
  not the whole paper).  Bearing: a horizon formed by collapse CAN be exactly extremal after a finite advanced time --
  a precedent beside reading (a), never a supply; it is Reissner-Nordstrom (charge), not eq. (17).
  standard-not-READ: the Vaidya metric; Raychaudhuri's equation; Birkhoff; the event horizon's teleology.

OWNERS IMPORTED BY PATH, NEVER COPIED: lemmas/epass_pairing.py (horizon_stress_eq17, readme_flux, pairing_bulk,
pairing_sheet, bulk_gvv, sheet_gvv, EPS, _eq17_ingoing, its geometry engine _connection/_riemann, BANNED_KEYS,
BANNED_ARGS; sim2_facing's eq. (17) and Schwarzschild data through it), lemmas/epass_frames.py (readme_flux_P1,
m_words_verbatim), lemmas/o3_write.py (m_squared, t_min, _num, EXAMPLE_N, w1), tools/cypher.py (Index, ADMISSION,
run, coordinate_report).  sim2_passage.py is never imported (another run edits it).

CLI:  --selftest (every check, each able to fail; ~1-2 min)   --mutants (every named mutation must make its check
      FAIL; exit 1 if one passes)   --json PATH (compute(), every row labelled)   no flag: prints the report.
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

# ============================================================================================ M's words (verbatim)
M_WORDS = {
    "70": "We do not feed the corridor, it takes the information it requires as a natural condition of its "
          "opening...such as with a horizon",
    "101 (6)": "6 - this is a duty of the device, assess the README size and widen the corridor to the necessary size, "
               "no more and no less.",
    "106 (b)": "Three distinct holds in one fluid wave motion, horizon position 1 only as the corridor opens, when the "
               "corridor is fully realized the bits are held on both horizons simultaneously because the corridor "
               "builds position 2 with the bits in mind, upon the corridor closing the bits are then held only at the "
               "horizon of position 2.",
    "109": "A horizon cannot exist without the object of which it needs to exist",
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
    "136 (3)": "3 - it lives in a dimension that connects the positions. It is a bridge, not a physical place. It can "
               "only facilitate transport, not indefinitely hold something.",
    "136 (7)": "7 - The throat formation is synchronization",
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


def _s(x):
    if isinstance(x, (sp.Basic,)):
        return str(x)
    if isinstance(x, Fr):
        return str(x)
    return x


# ============================================================================================ (1) HELD
def held_stress(rho_power=0):
    """A held static stress on eq. (17)'s horizon (owner P.horizon_stress_eq17 for the AdS2-invariant regular case);
    rho_power > 0 makes the static-frame density rho = rho0 / F^rho_power, singular on the horizon (the regularity
    premise's control).  tau(xi,xi) = -rho g(xi,xi) on the (v,u) block, g(xi,xi) = -F from the owner's ingoing chart,
    limit u -> 0.  Label: computed ([PLANE] chart; the zero for finite rho is STRUCTURAL: g(xi,xi)|_H = 0)."""
    own = P.horizon_stress_eq17(0, False)
    g, X4, Fv = P._eq17_ingoing()
    rho0 = sp.Symbol("rho0", positive=True)
    rho = rho0 / Fv**sp.Rational(rho_power)
    tau_xixi = sp.limit(sp.simplify(-rho * g[0, 0]), P.u, 0)
    return {"owner_tau_xixi": own["tau_xixi"], "owner_pi_xixi": own["pi_xixi"], "tau_xixi_limit": tau_xixi,
            "g_xixi_on_H": sp.simplify(g[0, 0].subs(P.u, 0)), "rho_power": rho_power}


def crossing_control(area_power=2):
    """The README as null dust CROSSING the horizon (H-README-AS-NULL-DUST, the board's): owner P.readme_flux (chart
    T^R(xi,xi) = 2 mu, [PLANE] normalisation) and owner F.readme_flux_P1 (kappa4^2 int T_vv dv = 1/(2m) per generator,
    [PLANE]-conditional).  Lemma S then asks for the partner -1/(2m).  area_power = 1 is the owner's r^2 -> r mutation."""
    p1 = F.readme_flux_P1(area_power=area_power)
    return {"chart_T_xixi": P.readme_flux(1), "P1_per_generator": p1["value"], "equals_1_over_2m":
            p1["equals_one_over_2m"], "partner_per_generator": -p1["value"], "kappa_x_m": p1["kappa_x_m"]}


def lemma_s_forms(fixed_mut=None):
    """Owner Lemma S, bulk form, degenerate family ([FREE], no field equation): fixed size (theta = 0) gives
    R(xi,xi) = 0; shear at fixed volume gives R(xi,xi) = -sigma^2 < 0; a growing section (theta > 0) gives
    R(xi,xi) > 0 with the Raychaudhuri residual 0 -- a positive null flux with no partner, only where the horizon grows.
    Sheet form (172 (1), a held stress on position 2's piece): K(xi,xi) = 0.  fixed_mut = 'grow' puts the growing case in
    the fixed slot (mutation)."""
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
    STRUCTURAL: G1 is defined as the energy of a horizon holding N bits.  m2_factor is a mutation."""
    m2 = O.m_squared() * m2_factor
    area = sp.simplify(4 * sp.pi * 4 * m2)
    return {"area_over_N_planck": sp.simplify(area / O.N), "is_4ln2": sp.simplify(area / O.N - 4 * sp.log(2)) == 0}


def whole_only(e_exponent=sp.Rational(1, 2)):
    """A horizon formed by a fraction f of the README's energy: G1 gives E proportional to N^e_exponent (1/2), so its
    area holds N_f = f^(1/e_exponent) N bits.  Against the share f of the README in (if its bits come in with its
    energy -- H-BITS-WITH-ENERGY, the board's): N_f/(f N).  < 1 for every f < 1 means the forming horizon cannot hold
    the README part by part, only whole.  e_exponent = 1 is the mutation (bit by bit would fit).
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


def vaidya_identity(drop_rkk=False):
    """[4D-VAIDYA] ds^2 = -(1 - 2M(v)/r) dv^2 + 2 dv dr + r^2 dOmega^2 (standard-not-READ), M arbitrary, owner's
    geometry engine (P._connection, P._riemann).  Outgoing null k = d_v + (f/2) d_r; kappa from nabla_k k = kappa k;
    theta = 2 k^r/r; R(k,k) from the Ricci tensor.  Returns the non-affine Raychaudhuri residual
    k(theta) - kappa theta + theta^2/2 + R(k,k) (must be 0 identically: sigma = 0 by symmetry), kappa, R(k,k).
    drop_rkk is the mutation.  Label: computed (sympy)."""
    X = [VV, RR, TH, PH]
    M = MF(VV)
    f = 1 - 2 * M / RR
    g = sp.Matrix([[-f, 1, 0, 0], [1, 0, 0, 0], [0, 0, RR**2, 0], [0, 0, 0, RR**2 * sp.sin(TH)**2]])
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


def _smooth(x):
    return 0.0 if x <= 0 else (1.0 if x >= 1 else 3 * x * x - 2 * x ** 3)


def _dsmooth(x):
    return 0.0 if (x <= 0 or x >= 1) else 6 * x - 6 * x * x


def vaidya_run(pre=0.0, partner=0.0, width=1.0, write=2.0e5, partner_sign=1.0, area_exp=2.0):
    """[4D-VAIDYA], m = 1 (the README's G E/c^4).  M(v) = pre + (1 - partner_sign*partner) s(v/width), s the C^1
    smoothstep: the README's null dust (mass 1) and a partner of the same profile along the same ingoing rays, of
    fraction `partner` (negative null energy: T_vv^c = -partner T_vv^R).  The event horizon is traced backward from
    r = 2 M_final after the inflow (stable backward); the trapping horizon is r = 2M(v).  Returns final area in units of
    N A_bit (H1: the README's horizon r = 2 has area 16 pi = N A_bit), final mass in units of E, the README's share of
    the final mass, the net inflow, the fraction of the write over which the trapping horizon's size moves while it
    exists, the least expansion of the event horizon's generators inside the inflow, a finite-difference Raychaudhuri
    residual along the event horizon, and where the event horizon is born (forming case).  partner_sign = -1 and
    area_exp are mutations.  Label: computed (scipy, rtol 1e-11)."""
    q = 1.0 - partner_sign * partner
    mfin = pre + q

    def M(v):
        return pre + q * _smooth(v / width)

    def Mp(v):
        return q * _dsmooth(v / width) / width

    out = {"pre": pre, "partner": partner, "width_over_write": width / write, "mass_E": mfin, "net": q}
    if mfin <= 1e-12:
        out.update({"horizon_forms": False, "area_N": 0.0, "share": 0.0, "moves_fraction": 0.0,
                    "eh_theta_min_in_inflow": None, "fd_raychaudhuri_rel": None, "eh_born_before_inflow_m": None})
        return out
    v_end = width + 20.0 * max(1.0, mfin)
    r_end = 2.0 * mfin

    def rhs(v, y):
        return [0.5 * (1.0 - 2.0 * M(v) / max(y[0], 1e-300))]

    def born(v, y):
        return y[0] - 1e-9
    born.terminal = True
    v_lo = -(4.0 * mfin + 50.0 * max(pre, 0.0) + 10.0)
    sol = solve_ivp(rhs, (v_end, v_lo), [r_end], dense_output=True, rtol=1e-11, atol=1e-13, events=born,
                    max_step=max(width / 400.0, 0.02))
    vb = float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
    rs = lambda v: float(sol.sol(v)[0])
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
        rhs_r = M(v) / r0**2 * t0 - t0**2 / 2 - 2.0 * Mp(v) / r0**2
        rel.append(abs(dth - rhs_r) / max(abs(dth), abs(rhs_r), 1e-30))
    area_N = (rs(v_end) / 2.0) ** area_exp
    moves = 0.0 if abs(q) < 1e-15 else width / write
    out.update({"horizon_forms": True, "area_N": area_N, "share": (q / mfin if q > 0 else 0.0),
                "moves_fraction": moves, "eh_theta_min_in_inflow": float(min(th)),
                "eh_theta_max_in_inflow": float(max(th)),
                "fd_raychaudhuri_rel": float(max(rel)), "eh_born_before_inflow_m": (None if vb is None else -vb),
                "trapping_r_at_mid_inflow": 2.0 * M(0.5 * width),
                "trapping_area_N_at_half_energy": ((2.0 * (pre + 0.5 * q)) / 2.0) ** 2 if pre == 0 else None})
    return out


def scenarios(write=None, partner_sign=1.0, area_exp=2.0):
    """The computed configurations: pre in {0 (the horizon forms with the inflow), 1 (a horizon of the README's size
    already stands)}, partner in {0, 1/2, 1}, inflow compact (width = 1 m) or spread over the whole write (the owner's
    floor).  Label: computed."""
    T = write_floor()["floor_in_m"] if write is None else write
    runs = []
    for pre in (0.0, 1.0):
        for p in (0.0, 0.5, 1.0):
            for spread, w in ((0, 1.0), (1, T)):
                r = vaidya_run(pre, p, w, T, partner_sign=partner_sign, area_exp=area_exp)
                r["spread"] = spread
                runs.append(r)
    return {"write_floor_in_m": T, "runs": runs}


def _frac(x, den=12):
    return Fr(x).limit_denominator(den)


COORDS = ["pre", "partner", "spread", "area_N", "mass_E", "share", "net", "moves"]


def _moves_code(fr):
    return 0 if fr == 0 else (1 if fr <= 1e-3 else 2)


def cells_from(sc, held=True):
    """Ordinal cells read off the runs (never assigned): area, mass, share, net rounded to small rationals; moves coded
    0 (the trapping horizon never changes), 1 (it changes only over a compact inflow, <= 1e-3 of the write), 2 (over
    the write).  The held state (owner's held stress: nothing crosses, theta = 0, no partner) is added as its own cell.
    Label: computed; the encoding is the board's (H-CYPHER-README-HELD-INDEX)."""
    cells, names = [], []
    for r in sc["runs"]:
        c = [int(r["pre"]), str(_frac(r["partner"])), r["spread"], str(_frac(r["area_N"])), str(_frac(r["mass_E"])),
             str(_frac(r["share"])), str(_frac(r["net"])), _moves_code(r["moves_fraction"])]
        cells.append(c)
        names.append(f"pre={int(r['pre'])} partner={_frac(r['partner'])} spread={r['spread']}")
    if held:
        cells.append([1, "0", 0, "1", "1", "0", "0", 0])
        names.append("held: the formed horizon holding the README, nothing crossing (owner held stress, theta = 0)")
    return cells, names


TEST_EVENT_CELL = [1, "0", 1, "1", "1", "1", "1", 0]       # RI-5's framing: absorbed with no growth, no partner
TARGETS = {
    "T_HELD (195's reading, the binary statement): forms with a compact whole inflow, no partner, area N A_bit, mass E, "
    "the README's whole mass, size moves only over the inflow": [0, "0", 0, "1", "1", "1", "1", 1],
    "T_STRICT (162 read as never changing, inflow not instantaneous)": [0, "0", 0, "1", "1", "1", "1", 0],
    "T_GLOSS (163's option text with 195: fixed size through a spread write, no partner, area N A_bit, mass E)":
        TEST_EVENT_CELL,
    "T_PAIR (163's option text with the partner: E-PASS's crossing; the README one member of a pair)":
        [1, "1", 1, "1", "1", "0", "0", 0],
}


def _spec_index(name, cells, declared):
    vo = {}
    for i, c in enumerate(COORDS):
        vals = {row_[i] for row_ in cells} | {t[i] for t in TARGETS.values()}
        vals_cells = {row_[i] for row_ in cells}
        vo[c] = sorted(vals_cells, key=lambda x: float(Fr(str(x))))
    return CY.Index(name, COORDS, cells, value_order=vo, declared=declared)


def _determined(cells, by, target, where=None):
    """logic's binary: is `target` a function of `by` on the cells satisfying `where`?  Returns (bool, values seen)."""
    idx = {c: i for i, c in enumerate(COORDS)}
    m = defaultdict(set)
    seen = set()
    for c in cells:
        if where and not all(str(c[idx[k]]) == str(v) for k, v in where.items()):
            continue
        m[tuple(c[idx[b]] for b in by)].add(c[idx[target]])
        seen.add(c[idx[target]])
    return (bool(m) and all(len(v) == 1 for v in m.values())), sorted(seen, key=lambda x: float(Fr(str(x))))


def cypher_run(control=False, sc=None):
    """Put the question to the cypher (roster 1173).  LAW index: the computed cells.  CONTROL: plus the test-event cell.
    For each language: state, admitted-set size, E; for each target: admitted or not, and whether a NO is STRUCTURAL
    (a value never seen on a coordinate, or a pair of values never seen together on two coordinates).  Logic's binaries
    L1-L4.  Label: computed; the encoding is the board's."""
    sc = sc or scenarios()
    cells, names = cells_from(sc)
    if control:
        cells = cells + [TEST_EVENT_CELL]
        names = names + ["CONTROL: the README absorbed by a horizon that keeps size and mass, no partner (RI-5)"]
        wit = {"analysis": {"speaks": False, "witness": "no continuous law in these coordinates covers the control "
               "cell: mass_E - pre - net = -1 there and 0 on every computed cell (the Einstein equation's energy "
               "balance); a law covering it needs a discrete test-event switch that is on no coordinate"}}
    else:
        wit = {"analysis": {"speaks": True, "witness": "continuous law on every cell, residual 0: mass_E = pre + net, "
               "net = 1 - partner, area_N = mass_E^2 (Vaidya end state A = 16 pi M^2), moves > 0 exactly where net > 0 "
               "(Raychaudhuri on the event horizon: least theta > 0 during a net inflow, 0 at net 0)"}}
    ix = _spec_index("README held vs crossing (" + ("CONTROL" if control else "LAW") + ")", cells, wit)
    res = CY.run(ix, "1173", {"algebra_budget": 60000})
    langs = {}
    admitted = {}
    for lang in ["order", "algebra", "geometry", "information", "statistics", "documentary"]:
        out, note = CY.ADMISSION[lang][0](ix, {"algebra_budget": 60000})
        if out is None:
            langs[lang] = {"state": "SILENT", "note": note}
            continue
        admitted[lang] = out
        langs[lang] = {"state": "SPEAKS", "admits": len(out), "E": len(out) - len(ix.cells)}
    langs["analysis"] = {"state": "SPEAKS" if wit["analysis"]["speaks"] else "SILENT", "witness":
                         wit["analysis"]["witness"], "status": "DECLARED"}
    seen_pairs = {(i, j): {(c[i], c[j]) for c in ix.cells} for i in range(ix.d) for j in range(ix.d) if i < j}
    tgt = {}
    for tname, t in TARGETS.items():
        enc = tuple(ix.code[i].get(v) for i, v in enumerate(t))
        unseen = [COORDS[i] for i, e in enumerate(enc) if e is None]
        in_cells = (None not in enc) and enc in set(ix.cells)
        unseen_pairs = []
        if not unseen:
            for (i, j), s in seen_pairs.items():
                if (enc[i], enc[j]) not in s:
                    unseen_pairs.append(f"{COORDS[i]}={t[i]} with {COORDS[j]}={t[j]}")
        per = {}
        for lang, out in admitted.items():
            per[lang] = (None not in enc) and enc in out
        per["analysis"] = ("speaks only by its declared witness; on the LAW index the target is " +
                           ("lawful" if (float(Fr(t[4])) == int(t[0]) + float(Fr(t[6])) and
                                         abs(float(Fr(t[3])) - float(Fr(t[4]))**2) < 1e-12 and
                                         ((t[7] > 0) == (float(Fr(t[6])) > 0))) else "UNLAWFUL"))
        per["documentary"] = "SILENT (citations, not a binary)"
        tgt[tname] = {"is_a_computed_cell": in_cells, "values_never_seen": unseen,
                      "value_pairs_never_seen": unseen_pairs[:6], "n_pairs_never_seen": len(unseen_pairs),
                      "admitted": per,
                      "NO_is_STRUCTURAL": bool(unseen or unseen_pairs)}
    logic = {
        "L1 with 195 (partner 0), H1 (area N A_bit) and the README coming in (net 1): is pre (when it comes in) fixed?":
            _determined(ix_cells_raw(cells), ["partner"], "pre", where={"partner": "0", "area_N": "1", "net": "1"}),
        "L2 with 195, H1 and net 1: is moves fixed (does the size change during the inflow)?":
            _determined(ix_cells_raw(cells), ["partner"], "moves", where={"partner": "0", "area_N": "1", "net": "1"}),
        "L3 is net fixed by (pre, mass_E) (energy balance)?":
            _determined(ix_cells_raw(cells), ["pre", "mass_E"], "net"),
        "L4 among net = 1 cells, is moves ever 0 (fixed size with a net inflow)?":
            _determined(ix_cells_raw(cells), ["net"], "moves", where={"net": "1"}),
    }
    rows_, keys = CY.coordinate_report(ix)
    return {"index": ix.name, "cells": len(ix.cells), "box": ix.box, "d": ix.d, "cell_names": names,
            "languages": langs, "targets": tgt, "logic": {k: {"fixed": v[0], "values": v[1]} for k, v in logic.items()},
            "information_adds_nothing": [r_["coordinate"] for r_ in rows_ if r_["adds_nothing"]],
            "information_keys": keys, "K_langclose_holds": res["langclose_holds"], "languages_agree":
            res["languages_agree"], "degenerate": res["degenerate"], "operator_bearing_measured":
            res["operator_bearing_measured"], "pairs_agreeing": res["pairs_agreeing"], "warnings": res["warnings"],
            "documentary_citations": ["Vaidya metric (standard-not-READ)", "Raychaudhuri (standard-not-READ)",
                                      "Kehle-Unger arXiv:2211.15742v2 PDF p.1 (READ)", "SIM1-TRANSITION S3b, S4",
                                      "O3-WRITE W3, W4 (ii)", "epass_pairing Lemma S (a), (b)",
                                      "epass_frames readme_flux_P1"]}


def ix_cells_raw(cells):
    return [list(c) for c in cells]


# ============================================================================================ the record
RECORD = [
    ("70", "M_WORDS", "(a)", "the corridor takes what it requires 'as a natural condition of its opening ... such as "
     "with a horizon': the taking is the opening, as a forming horizon takes what falls in (the board's reading)"),
    ("101 (6)", "M_WORDS", "both", "the size is the README's, 'no more and no less': H1 on either reading; 'widen' names "
     "a process and does not say whether the size stands before the README comes in (silent on timing)"),
    ("106 (b)", "M_WORDS", "(a)", "the first hold is on horizon 1 'only as the corridor opens': holding begins with "
     "the opening; how the hold moves to horizon 2 without a crossing flux is not computed here (OPEN; 132's 'different "
     "views of the same object' would make it a change of view -- the board's reading)"),
    ("109", "M_WORDS", "neutral", "the object 109 names is the corridor (H-HORIZON-NEEDS-OBJECT, as carried); it does "
     "not by itself forbid a horizon standing before the README is in it, and is not stretched to"),
    ("115 (b)", "M_WORDS", "(a)", "position 2's horizon comes into being 'When fully realized': a horizon forming and "
     "holding the bits from then (106); its holding without a crossing is OPEN, as for 106"),
    ("115 (c)", "M_WORDS", "(a)", "the inflow is 'The README itself' (R0): on (a) that inflow is what forms the horizon "
     "(computed: share 1)"),
    ("129 (1)", "M_WORDS", "(a)", "'it adds nothing to either position': on (a) the horizon's whole mass is the "
     "README's (share 1, computed); on (b) a mass E stands at the position before the README comes in -- energy that is "
     "not the README's (deduced, the board's reading of 129 (1) with 136 G)"),
    ("130 (1)", "M_WORDS", "both", "the black hole is what the mouth looks like: either reading"),
    ("131 (2)", "M_WORDS", "both", "the throat is sized by the README's binary information: H1 on either reading"),
    ("132", "M_WORDS", "(a)", "the horizons hold the README: (a) makes the area the README's own N bits as its own "
     "horizon; (b) holds an area of N A_bit whose mass is not the README's (computed: share 0 with the partner)"),
    ("133 (2)", "M_WORDS", "(a)", "'only one exact energy': (b) without a partner ends at mass 2E and area 4 N A_bit "
     "(computed; the owner's W1 control '2E gives 4N'); with the partner the standing E is separate from the README's "
     "+E and -E (deduced); (a) one E (computed)"),
    ("136 G", "M_WORDS", "(a)", "'the README is the energy, not separate': (a) share 1; (b) with the partner share 0 "
     "(computed)"),
    ("136 (3)", "M_WORDS", "neutral", "'not indefinitely hold': both readings hold for a finite interval"),
    ("136 (7)", "M_WORDS", "neutral", "'The throat formation is synchronization': names the formation; not computed here"),
    ("158 (2)", "M_WORDS", "(a)", "the hold lasts as long as the write needs: on (a) the write is the opening (O3-WRITE "
     "reading (ii)) and 106's first hold is 'as the corridor opens' -- the hold and the write coincide as the opening; "
     "which interval 158 (2)'s 'hold' names is the board's reading (OPEN)"),
    ("160", "M_WORDS", "(a)", "'the same object': on (a) the opening -- the README coming in and forming the horizon -- "
     "is the corridor; the board's note carried under 160 ('the corridor does not exist until the README has arrived' "
     "gives way) was the board's reading and is reversed by (a), which restores O3-WRITE reading (ii)"),
    ("161", "M_WORDS", "neutral", "'my inclination is yes' to staying regular while the README passes: on (a) no "
     "fixed-size corridor stands during the write; the regularity question moves to the formation and the held interval"),
    ("162", "M_WORDS", "(a) with a cost", "(a) keeps the size fixed from the moment the whole README is in; during a "
     "compact inflow the trapping horizon grows from nothing to the README's size over the inflow's width (computed: "
     "5e-6 of the write at width 1 m); 'always' holds at every moment only in the instantaneous limit.  (b) keeps it "
     "fixed through the write only with a partner (Lemma S) -- closed by 195"),
    ("163", "M_WORDS", "(a)", "M's words, 'All together, one whole': a forming horizon holds the README only whole "
     "(computed: f^2 of the bits at a fraction f of E)"),
    ("163 (the board's option text, not M's words)", "BOARD_WORDS", "(b)", "'at the fixed size; the write lasts at "
     "least ~200,000 clocks; B4d must keep the fixed-size corridor regular for that long' is (b)'s framing; with 195 no "
     "computed configuration has it (T_GLOSS below) -- it does not survive"),
    ("172 (1)", "M_WORDS", "(a)", "a held regular stress on position 2's piece carries no surface null flux (owner "
     "Lemma S sheet form, K(xi,xi) = 0): no partner asked"),
    ("183", "M_WORDS", "(a)", "'never violated as a pair': on (a) no negative member is asked by the README's inflow"),
    ("188", "M_WORDS", "(a)", "'always two entangled opposing forces': on (a) the README's inflow asks no partner; 188's "
     "pair is not demanded by it (the board's reading; the bond of 189 remains)"),
    ("189", "M_WORDS", "(a)", "'the bond': a tension carries zero null energy along a fixed-size horizon (ITEM188 1.9, "
     "computed there); on (a) the bond is all the held README needs"),
    ("190", "M_WORDS", "(a)", "'Information is energy': (a) has the N bits as the area and E as the mass of one object "
     "(H1 with G1, STRUCTURAL)"),
    ("195", "M_WORDS", "(a)", "'The README is not a pair': closes (b) with the partner (194's object); with Raychaudhuri "
     "and H1/G1/133 it leaves only (a) (deduced)"),
]
LEMMA_ROWS = {   # warptheorem.py's rows as they stand (read from the file by check C10b)
    "R0": "R0 the read: the corridor takes the README as its inflow at the opening; N is read from the object",
    "E1": "E1 E carried through three holds into position 2",
    "E2": "E2 released at position 2 at the closing",
    "H2": "H2 the horizons hold the README as well as the throat",
    "I1": "I1 the passage is N bits of entanglement",
}
LEMMA_VERDICTS = {
    "R0": ("(a)", "the inflow at the opening is the formation"),
    "E1": ("(a) with OPEN", "E is held, not crossing; carried by the hold moving through 106's three holds -- the "
           "mechanism of that move without a crossing flux is OPEN (B4d's)"),
    "E2": ("(a)", "held on position 2's horizon until it ends with the corridor (109, 115 (b))"),
    "H2": ("(a)", "literal on (a)"),
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
_CACHE = {}


def compute():
    if "out" in _CACHE:
        return _CACHE["out"]
    t0 = _wall.perf_counter()
    hs, hsing = held_stress(0), held_stress(1)
    cc = crossing_control()
    ls = lemma_s_forms()
    h1 = h1_per_bit()
    wo = whole_only()
    wf = write_floor()
    s4 = eq17_radial_rkk()
    vi = vaidya_identity()
    sc = scenarios(write=wf["floor_in_m"])
    law = cypher_run(False, sc)
    ctl = cypher_run(True, sc)
    rc = record_check()
    runs = {f"pre={int(r['pre'])} partner={_frac(r['partner'])} spread={r['spread']}": r for r in sc["runs"]}
    fc = runs["pre=0 partner=0 spread=0"]
    fsp = runs["pre=0 partner=0 spread=1"]
    pn = runs["pre=1 partner=0 spread=0"]
    pp = runs["pre=1 partner=1 spread=1"]
    fp = runs["pre=0 partner=1 spread=0"]
    R = {}
    R["held_stress_T_xixi"] = row({"tau_xixi": hs["owner_tau_xixi"], "pi_xixi": hs["owner_pi_xixi"],
                                   "limit_regular": hs["tau_xixi_limit"]}, "computed; STRUCTURAL",
                                  "[PLANE] chart", "owner horizon_stress_eq17: zero because g(xi,xi)|_H = 0 with finite "
                                  "rho -- a regular held stress asks Lemma S for no partner")
    R["held_stress_singular_control"] = row(hsing["tau_xixi_limit"], "computed", "[PLANE] chart",
                                            "rho = rho0/F (singular on the horizon) keeps T(xi,xi) = rho0: regularity "
                                            "is the premise")
    R["crossing_control"] = row({"chart_T_xixi": cc["chart_T_xixi"], "P1_per_generator": cc["P1_per_generator"],
                                 "partner_per_generator": cc["partner_per_generator"]}, "computed",
                                "[PLANE]-conditional", "the README as crossing null dust: 1/(2m) per generator on P1; "
                                "Lemma S asks -1/(2m)")
    R["lemma_s_bulk_and_sheet"] = row({k: ls[k] for k in ("fixed_theta", "fixed_R_xixi", "shear_R_xixi_witness",
                                                          "grow_theta", "grow_R_xixi_witness",
                                                          "grow_raychaudhuri_residual_witness", "sheet_K_xixi")},
                                      "computed", "[FREE]", "theta = 0: R(xi,xi) = -sigma^2 <= 0; growing: R(xi,xi) > 0 "
                                      "with residual 0 -- positive net null flux only where the horizon grows")
    R["H1_area_per_bit"] = row(h1["area_over_N_planck"], "STRUCTURAL", "[FREE]",
                               "the README's horizon (r = 2m, owner m^2) holds exactly 4 ln2 Planck areas per bit")
    R["whole_only"] = row({"held_bits_over_N": wo["held_bits_over_N"], "held_over_share": wo["held_over_share"],
                           "samples": wo["samples"]}, "computed; STRUCTURAL", "[FREE]",
                          "a forming horizon holds f^2 N bits at a fraction f of E: the README is held only whole "
                          "(H-BITS-WITH-ENERGY, the board's, for the comparison with f N)")
    R["write_floor"] = row(wf["floor_in_m"], "computed", "owner o3_write W3",
                           "the gas bound, in units of m: a floor on how early the README must start (the ball of "
                           "radius (2 + T) m); it does not bound the width of the inflow across r = 2m (deduced from "
                           "W3's own statement); whether a compact converging shell can carry N bits is OPEN")
    R["eq17_static_end_state"] = row({"dlnFH_dr": s4["dlnFH_dr"], "negative": s4["negative_everywhere_sampled"]},
                                     "computed", "[PLANE]", "SIM1 S4 recomputed from the owner's data: a static end "
                                     "state reached with NEC matter in one spacetime is not eq. (17)")
    R["vaidya_raychaudhuri_identity"] = row({"residual": vi["residual"], "kappa": vi["kappa"], "R_kk": vi["R_kk"]},
                                            "computed", "[4D-VAIDYA]", "k(theta) - kappa theta + theta^2/2 + R(k,k) = 0 "
                                            "identically, with R(k,k) = 2 M'/r^2 > 0 for an inflow")
    R["forming_compact"] = row({k: fc[k] for k in ("area_N", "mass_E", "share", "net", "moves_fraction",
                                                   "eh_theta_min_in_inflow", "fd_raychaudhuri_rel",
                                                   "eh_born_before_inflow_m")}, "computed", "[4D-VAIDYA]",
                               "(a): the horizon forms as the README comes in -- area N A_bit, mass E, the README's "
                               "whole mass, theta > 0 throughout the inflow, no partner")
    R["forming_spread"] = row({k: fsp[k] for k in ("area_N", "mass_E", "share", "moves_fraction",
                                                   "eh_theta_min_in_inflow", "trapping_area_N_at_half_energy")},
                              "computed", "[4D-VAIDYA]", "(a) spread over the write: the size moves over the whole "
                              "write; at half the energy in, the trapping horizon's area is 1/4 N A_bit")
    R["pre_no_partner"] = row({k: pn[k] for k in ("area_N", "mass_E", "share", "eh_theta_min_in_inflow")}, "computed",
                              "[4D-VAIDYA]", "(b) without a partner: 4 N A_bit and 2E -- H1, G1 and 133 broken, and "
                              "the size changes")
    R["pre_exact_partner_spread"] = row({k: pp[k] for k in ("area_N", "mass_E", "share", "net",
                                                            "eh_theta_min_in_inflow", "eh_theta_max_in_inflow")},
                                        "computed", "[4D-VAIDYA]", "(b) with the exact partner (163's option text): "
                                        "size fixed (theta = 0), but the README's share of the mass is 0 -- the README "
                                        "is one member of a pair (195: it is not)")
    R["forming_with_partner"] = row({"horizon_forms": fp["horizon_forms"], "area_N": fp["area_N"]}, "computed",
                                    "[4D-VAIDYA]", "a partner on a forming horizon cancels the horizon itself")
    R["cypher_LAW"] = row(law, "computed", "the board's encoding (H-CYPHER-README-HELD-INDEX)",
                          "roster 1173; the cypher classifies, it does not derive")
    R["cypher_CONTROL"] = row(ctl, "computed", "the board's encoding", "the test-event cell added (RI-5's framing)")
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


BINARY_STATEMENT = ("The README is held by the corridor's horizon -- its N bits are the horizon's area (H1) and its "
                    "energy is the horizon's mass (G1) -- and its inflow at the opening (R0) comes in as one whole "
                    "while that horizon forms, so that no net null flux crosses a horizon of fixed size and Lemma S "
                    "asks no partner.")
READINGS = {
    "M's, as carried": ["H-README-NOT-A-PAIR (195)", "H-HORIZON-AND-THROAT-HOLD (132)", "H-README-IS-ENERGY (136 G)",
                        "H-INFORMATION-IS-ENERGY (190)", "H-ONE-EXACT-ENERGY (133)", "H-FIXED-SIZE (162)",
                        "H-AT-ONCE-IS-WHOLE (163)", "H-CORRIDOR-IS-OPENING (160)", "H-INFLOW-IS-README (115 (c))",
                        "H-THREE-HOLDS (106)", "H-CORRIDOR-TAKES (70)", "H-NEC-NEVER-VIOLATED-AS-PAIR (183)",
                        "H-PAIRING-HELD-AS-TENSION (189)", "H-README-ON-P2 (172 (1))"],
    "the board's, used": ["H-README-HELD (195's note: held, not crossing)", "H-ARRIVAL-FORMS-THE-HORIZON (reading (a))",
                          "H-WRITE-AT-FIXED-SIZE (reading (b): the option text of 163)",
                          "H-SIZE-FROM-WHOLE (162's fixed size counted from the whole README's arrival)",
                          "H-WRITE-IS-THE-OPENING (O3-WRITE reading (ii), restored by (a))", "H-BITS-WITH-ENERGY",
                          "H-README-AS-NULL-DUST (the control)", "H-FIXED-SIZE-AS-THETA-ZERO",
                          "H-CYPHER-README-HELD-INDEX (the encoding)"],
}
CONSEQUENCES = {
    "F5": "On (a) the exact +/- pair along crossed generators of a fixed-size horizon is not demanded by the README: no "
          "generator of a fixed-size horizon carries its net flux.  F5 becomes moot on (a) -- neither green nor "
          "refuted -- and is replaced, for O3, B3, B4d and B7, by the input that the README's whole inflow forms the "
          "corridor and its end state is the corridor (H-ARRIVAL-FORMS-THE-HORIZON; OPEN).  On (b) F5 stays demanded, "
          "and (b) is closed by 195 with Raychaudhuri, H1, G1 and 133.",
    "E-PASS test-event framing (RI-5)": "Sharpened, not answered: the README is not a test event but the horizon's "
          "whole source (share 1).  E-PASS's crossing of a horizon of fixed size is the board's configuration (195); "
          "S3b's bar is the very reason (a) is forced.  E-PASS's 'OPEN through 177' describes the board's crossing, "
          "not the README's route.",
    "B4d": "The problem changes: from a fixed-size corridor kept regular through >= 2.0e5 clocks of write with the "
           "README crossing (stage 5, the option text of 163) to (1) the README's whole inflow forming the corridor (a "
           "collapse; the trapping horizon appears at the README's size within the inflow's width) and (2) the formed "
           "corridor staying regular while it holds until the closing.  Stage 5's computed singular surface (8-16 "
           "clocks with eq. (17) on a positive-tension plane) still bounds a held interval on that plane; the held "
           "interval's length is not fixed by the rulings (136 answer 6, 158 (2)).  End-state cautions: eq. (17) is not "
           "a static end state of NEC inflow in one spacetime (S4, [PLANE]); a forming horizon can be exactly extremal "
           "after finite advanced time (Kehle-Unger, READ; charge, not eq. (17)).  Under 179 the bulk corridor's "
           "formation is OPEN.  How the hold moves from horizon 1 to horizon 2 without a crossing flux (106, E1) is "
           "OPEN.",
    "O3": "The write's floor (>= 2.0e5 clocks) becomes the opening's lead (O3-WRITE reading (ii), restored): it limits "
          "how early the README must start, not how long a fixed-size corridor must stand.  O3 becomes: the corridor "
          "forms from the README's whole inflow and survives its held interval.  O3 stays OPEN.",
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
    return bool(w["only_whole"]), {"held_over_share": str(w["held_over_share"]), "samples": {k: str(v) for k, v in
                                                                                             w["samples"].items()}}


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
    sc = scenarios(write=2.0e5)
    cells, _ = cells_from(sc)
    if mut == "test-event-cell":
        cells = cells + [TEST_EVENT_CELL]
    bad = [c for c in cells if c[6] != "0" and c[7] == 0]
    return not bad, {"cells": len(cells), "net_positive_at_fixed_size": bad}


def check_C9(mut=None):
    sc = scenarios(write=2.0e5)
    use_ctl = mut == "control-for-law"
    law = cypher_run(use_ctl, sc)
    ctl = cypher_run(True, sc)
    tg = law["targets"][[k for k in TARGETS if k.startswith("T_GLOSS")][0]]
    th = law["targets"][[k for k in TARGETS if k.startswith("T_HELD")][0]]
    bearing = [l_ for l_ in ("order", "algebra", "geometry", "information", "statistics")
               if law["languages"][l_]["state"] == "SPEAKS"]
    no_gloss = all(tg["admitted"][l_] is False for l_ in bearing)
    yes_held = all(th["admitted"][l_] is True for l_ in bearing)
    k1 = [k for k in law["logic"] if k.startswith("L1")][0]
    flips = law["logic"][k1]["fixed"] is True and law["logic"][k1]["values"] == [0] and \
        ctl["logic"][k1]["fixed"] is False
    ctl_gloss = ctl["targets"][[k for k in TARGETS if k.startswith("T_GLOSS")][0]]["is_a_computed_cell"]
    ok = no_gloss and yes_held and flips and ctl_gloss and len(bearing) >= 3
    return ok, {"bearing": bearing, "T_GLOSS_admitted": {l_: tg["admitted"][l_] for l_ in bearing},
                "T_HELD_admitted": {l_: th["admitted"][l_] for l_ in bearing}, "L1_law": law["logic"][k1],
                "L1_control": ctl["logic"][k1]}


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
                      and k not in TARGETS and not k.startswith(("L1", "L2", "L3", "L4")))
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


CHECKS = {
    "C1": (check_C1, "held regular stress: T(xi,xi) = 0 on the horizon (owner), no partner asked",
           [("singular-held", "rho = rho0/F, singular on the horizon")]),
    "C2": (check_C2, "the control: the README as crossing null dust, 1/(2m) per generator on P1, partner -1/(2m)",
           [("r^2->r", "the owner's area-power mutation")]),
    "C3": (check_C3, "Lemma S premises [FREE]: theta = 0 -> R = 0; shear -> R < 0; growth -> R > 0, residual 0; sheet K = 0",
           [("grow-in-fixed-slot", "the growing horizon put where the fixed one belongs")]),
    "C4": (check_C4, "H1 with G1: 4 ln2 Planck areas per bit (STRUCTURAL)", [("m2-doubled", "m^2 doubled")]),
    "C5": (check_C5, "a forming horizon holds the README only whole (f^2 N bits at a fraction f of E)",
           [("E-linear-in-N", "E proportional to N instead of sqrt N")]),
    "C6": (check_C6, "Vaidya: non-affine Raychaudhuri identity, kappa = M/r^2, R(k,k) = 2M'/r^2",
           [("drop-Rkk", "the R(k,k) term dropped")]),
    "C7": (check_C7, "Vaidya runs: forming -> N A_bit, E, share 1, theta > 0; pre -> 4 N A_bit, 2E; pre + partner -> "
                     "theta = 0, share 0; forming + partner -> no horizon",
           [("partner-sign-flipped", "the partner with positive energy"), ("area-linear-in-M", "area read as M, not M^2")]),
    "C8": (check_C8, "the law in the cells: no computed cell has a net inflow at a fixed size",
           [("test-event-cell", "RI-5's test-event cell planted")]),
    "C9": (check_C9, "the cypher: T_GLOSS admitted by no operator-bearing language on LAW; T_HELD admitted (a computed "
                     "cell); logic's L1 (timing fixed to forming) flips on the CONTROL",
           [("control-for-law", "the CONTROL index run in the LAW slot")]),
    "C10": (check_C10, "M's words verbatim inside their own items; warptheorem.py's rows as quoted",
            [("altered-M-quote", "one word of 162 changed"), ("swapped-items", "160 and 161 swapped")]),
    "C11": (check_C11, "guards: no banned key or argument; every row labelled with the six labels",
            [("planted-key-hold_time", "a key naming a time"), ("row-without-label", "a row with no label")]),
    "C12": (check_C12, "the write floor is the owner's 2.0e5 (Z = 108.75); W1 control 2E gives 4N", [("Z=2", "Z = 2")]),
    "C13": (check_C13, "SIM1 S4 from owner data: eq. (17)'s d ln(F/H)/dr = -1/((r-2)(2r-3)) < 0",
            [("schwarzschild-data", "Schwarzschild data in eq. (17)'s place")]),
}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, set)):
        return [_clean(v) for v in o]
    if isinstance(o, (sp.Basic, Fr)):
        return str(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


def selftest():
    t0 = _wall.perf_counter()
    allok = True
    print("readme_held selftest (computed, READ and deduced; not verified; not seated)")
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
    print("readme_held -- items 195/196 (computed, READ and deduced; not verified; not seated)")
    for k in ("held_stress_T_xixi", "held_stress_singular_control", "crossing_control", "lemma_s_bulk_and_sheet",
              "H1_area_per_bit", "whole_only", "write_floor", "eq17_static_end_state", "vaidya_raychaudhuri_identity",
              "forming_compact", "forming_spread", "pre_no_partner", "pre_exact_partner_spread", "forming_with_partner"):
        print(f"\n{k} [{R[k]['label']}] {R[k]['tag']}\n  {json.dumps(R[k]['value'])[:900]}\n  {R[k]['note']}")
    for k in ("cypher_LAW", "cypher_CONTROL"):
        c = R[k]["value"]
        print(f"\n{k}: {c['index']}  d = {c['d']}  cells = {c['cells']}  box = {c['box']}")
        for lang, v in c["languages"].items():
            print(f"  {lang:12s} {v['state']:7s} {v.get('admits', '-')!s:>6} E={v.get('E', '-')!s:>6}  "
                  f"{v.get('note', v.get('witness', ''))[:110]}")
        print(f"  K.langclose holds: {c['K_langclose_holds']}; languages agree: {c['languages_agree']}; "
              f"information adds nothing: {c['information_adds_nothing']}; keys: {c['information_keys']}")
        for t, v in c["targets"].items():
            print(f"  {t[:70]}...\n    computed cell: {v['is_a_computed_cell']}; admitted: {v['admitted']}; "
                  f"STRUCTURAL NO possible: {v['NO_is_STRUCTURAL']} (never seen: {v['values_never_seen']}, "
                  f"{v['n_pairs_never_seen']} pairs, e.g. {v['value_pairs_never_seen'][:2]})")
        for lk, lv in c["logic"].items():
            print(f"  logic {lk}: {lv}")
    print("\nrecord:")
    for r_ in R["record"]["value"]:
        print(f"  {r_['item']:46s} {r_['reading']:16s} {r_['why'][:150]}")
    print("\nlemma rows:", json.dumps(R["lemma_rows"]["value"])[:900])
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
