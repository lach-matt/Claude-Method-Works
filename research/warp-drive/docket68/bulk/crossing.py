#!/usr/bin/env python3
"""
crossing.py -- O6 (BULK-O2): entering and leaving the corridor, as three states -- LEAVING, STASIS IN THE CORRIDOR,
ARRIVING -- with what must cross at each, and at what rate; worked BY DEDUCTION FROM FIRST PRINCIPLES.

Not seated; verified once (2026-10-05), findings applied (HISTORY below).  M's orders: item 59 ("4, then 3 please.");
item 61 ("Fold into O6 (Recommended)": H-DETACH and H-CORRIDOR-STASIS as three states); item 64 ("1, but I want you to
consider using deduction and first principle as we continue forward in to the unobserved. Such will be the best method
to both determine and fill our gaps": M-DEDUCE); item 66 ("Premises of O6 (Recommended)"); item 67 (speed "relative not
to the information traveling but to the two positions observing from two perspectives at the same time": item 65's
H-INFO-RELATIVE-SPEED corrected to H-POSITION-RELATIVE-SPEED).  All of M's hypotheses are carried as hypotheses, never
as results.  O9 stays OPEN.

    python3 crossing.py              report
    python3 crossing.py --selftest   checks, with CONTROLS
    python3 crossing.py --json       the numbers as JSON

THE METHOD (M-DEDUCE, read with the charter).  Every claim is a PREMISE -- READ at source (printed page), COMPUTED by a
board owner, or a NAMED hypothesis -- or a DEDUCTION, labelled with the premises it uses.  A gap no deduction closes is
OPEN.  SCOPE: D1, D2, D4, D5, D7 and D8 are Randall-Sundrum-specific (H-RS1, H-RS1-WARP, H-K-PLANCK, H-SAME-LAGRANGIAN,
H-OBSERVED-FRAME, bulk.py's); D3's and D6's information floors do not depend on the geometry.

PREMISES
  P-CONF   (READ, Randall & Sundrum hep-ph/9905221v1) The action is S_gravity + S_vis + S_hid (eq. 4, p.2): each plane
           carries its own Lagrangian; the bulk, as written, only -Lambda + 2 M^3 R.  'two three-branes, one of which
           contains the Standard Model fields' (abstract).  NAMED H-CONFINED: CMS (arXiv:2103.02708, printed p.1) notes
           RS variants in which SM fields propagate in the bulk.  RS leave the modulus unstabilised ('this problem is not
           yet solved', p.4); Goldberger-Wise stabilisation (DHR p.2) adds a bulk scalar (H-UNSTABILISED for D2).
  P-KK     (READ, DHR hep-ph/9909255 eq. 10, p.5) one term couples the graviton tower to our plane:
           -(1/M_Pl-bar) T h^(0) - (1/Lambda_pi) T sum_n h^(n); the radion is not in it.  DHR assume 'the first
           excitation only decays into SM states' (p.7).
  P-KKPROF (READ, DHR eqs. 6-8, pp.4-5) chi_n(phi) = (e^{2 sigma}/N_n)[J_2(z_n) + alpha_n Y_2(z_n)], z_n = m_n e^{sigma}/k,
           N_n ~ e^{k r_c pi} J_2(x_n)/sqrt(k r_c), J_1(x_n) = 0.
  P-TENS   (READ, RS eq. 11, p.3) V_hid = -V_vis = 24 M^3 k, Lambda = -24 M^3 k^2, 'required in order to obtain a solution
           that respects four-dimensional Poincare invariance' (p.4); 'The compactification radius r_c is effectively an
           arbitrary integration constant for this solution' (p.4).  Transcribed and matched from RS eqs. 7-10 (check 1).
  P-SCALE  (READ, RS eq. 21, pp.5-6) a visible mass parameter is e^{-k r_c pi} m_0 'when measured with the metric g-bar',
           'since all operators get rescaled according to their four-dimensional conformal weight'; g_hid = g-bar.
  P-VIEW   (READ, RS p.6) the TeV scale may equally be regarded as fundamental -- 'the one naturally taken by a
           four-dimensional observer residing on the visible brane'.
  P-MPL    (READ, RS eq. 16) M_Pl-bar^2 = (M^3/k)(1 - e^{-2 k r_c pi}).  Matched (check 2).
  P-JUMP   (COMPUTED, bulk.py) the jump reads hbar / (k e^{-k r_c pi}) on our clock (H-OBSERVED-FRAME); a hidden clock of
           the same physics reads e^{k r_c pi} times as many ticks (H-SAME-LAGRANGIAN).
  P-ML     (READ, Margolus & Levitin quant-ph/9710043v2) at most 2E/h orthogonal states per unit time in a long sequence
           (eq. 2, p.3); at least h/(4E) to reach one orthogonal state (eq. 4, p.4; attainment by eq. 10's state checked,
           check 3; the bound READ); energies of non-interacting subsystems add and so do their rates (p.8); they bound
           orthogonal states, NOT bits (p.2): H-ONE-STEP-PER-BIT (one local orthogonal step per bit written).
  P-BITS   (COMPUTED, measure.py) the information defining a 70 kg body under NAMED counts: 9.5e27 to 1.1e29 bits;
           Bekenstein's floor and Landauer's cost are measure.py's (READ there; R = 1 m is measure.py's default; 310 K is
           its H-TBODY).
  P-MOVE   (COMPUTED, transit.py) the teleported state arrives at B with fidelity 1 on all four outcomes, and B holds
           I/2 without the classical bits; no-cloning (NAMED; transit.py's move flag is declared) means A cannot also
           keep an UNKNOWN state (H-UNKNOWN-STATE).
  M's      H-DETACH, H-CORRIDOR-STASIS (item 60); H-POSITION-RELATIVE-SPEED (item 67, correcting item 65),
           H-TWO-PERSPECTIVE-TENSION (item 65); H-NO-SPEED, H-HIGHER-CORRIDOR (item 57); H-UNOBSERVED-UNBUILT (item 62).

DEDUCTIONS
  D1 LEAVING: WHAT CROSSES IS NOT THE MATTER.  [P-CONF, H-CONFINED]  A field on a plane has its action only on that
     plane, so a body made of such fields cannot enter the bulk; whatever crosses is a bulk-field excitation carrying
     the defining information.  -- H-DETACH has a physical counterpart that follows from H-CONFINED: the information
     leaves; the matter stays.
  D2 THE CARRIERS.  [P-CONF as written, H-UNSTABILISED, H-GRAVITATIONAL-CARRIER]  In RS1 as written the bulk holds only
     the metric: the KK gravitons (loaded through P-KK's term), the massless zero mode (the same term, at 1/M_Pl-bar;
     stable), or the radion (a separate coupling, not P-KK's).  With Goldberger-Wise stabilisation a bulk scalar's modes
     are also candidates (OPEN).
  D3 WHAT HAPPENS TO THE ORIGINAL.  [D1, P-MOVE, P-BITS]  A classical pattern is copied, not separated, unless A is
     erased (Landauer); an UNKNOWN quantum pattern is forcibly separated -- a move.  -- H-DETACH's 'let go' has its
     counterpart in the quantum case.  Which the defining information is: OPEN (new; related to S1B-O1).
  D4 STASIS: NO SM-MATTER FORM IN THE BULK.  [D1, D2]  While it is in the bulk no plane's SM fields hold it; it is a
     gravitational excitation (which our plane would see as a massive spin-2 particle, RS p.2) -- H-CORRIDOR-STASIS's
     'cannot take physical form', read as no SM-matter form.
  D5 HOW LONG STASIS LASTS.  [P-KK, P-KKPROF, H-STATIC-COUPLING, an open decay channel]  A carrier loaded at A returns
     to A no later than its A-width allows, tau <= hbar / Gamma_A, whatever its coupling at B.  One term loads and
     unloads at A, so both scale as 1/Lambda_pi^2 at fixed m_1: a longer stay at A costs a slower loading there.
     Measured in jump times, tau / jump = 1 / (x_1 Gamma/m_1) depends on the coupling alone: >= 2 wherever DHR's
     narrow-width treatment holds (k/M_Pl-bar <~ 0.3, p.7), 18 at CMS's edge, 0.27 at bulk.py's point (outside the width
     law's validity, H-WIDTH-LAW).  The KK modes couple ~1e-30 as strongly at the hidden plane (DEDUCED from P-KKPROF,
     with alpha_n from the Neumann condition at phi = 0), so they return to ours.  A lasting stasis needs a
     kinematically stable carrier -- the zero mode, loaded only at gravitational strength -- or a coupling switched
     after loading.  M RULED (item 68) "the first" -- the zero mode -- and set the switched coupling aside as
     "impossible but to the very definition of the transition... There is no in-between..." (M's ruling under
     H-HIGHER-CORRIDOR, not a board refutation; first written as 'OPEN; a device question beside
     H-UNOBSERVED-UNBUILT').
  D6 ARRIVING.  [P-CONF at B, P-BITS, H-NO-MATERIALISATION]  A bulk mode that decays at B makes particle pairs there
     (RS p.2, DHR: seen via decay products); delivering the PATTERN into a body needs matter at B (Step 1b's B stock)
     unless materialisation supplies >= mc^2 and the conserved numbers (H-NO-MATERIALISATION).  A holder of radius R
     with I bits has E >= I hbar c ln2 / (2 pi R) (Bekenstein, a floor -- non-binding: any 70 kg stock carries ~6e18 J);
     resetting a non-blank stock costs >= k T ln 2 per bit (Landauer, H-RESET-STOCK).  If B is on the hidden plane these
     are in B's own units (x 1e15 in ours).
  D7 THE RATE IS RELATIVE TO THE TWO POSITIONS.  [P-SCALE, P-JUMP, P-ML, dimensional analysis]  A bit count and E t / h
     are dimensionless and are not rescaled; both ends count the same I.  The two clocks read the same crossing as
     durations e^{k r_c pi} = 1e15 apart, so no rate is shared by both ends' clocks: the factor is the clock ratio,
     common to every process, NOT specific to information -- consistent with H-POSITION-RELATIVE-SPEED (relative to
     the two positions observing at the same time, item 67).  With H-ONE-STEP-PER-BIT and H-WRITE-IN-JUMP (all I bits
     written within one jump time): E t >= h I / 4 (parallel, one step per subsystem: eq. 4 with p.8) or h I / 2
     (sequential, eq. 2) -- ONE requirement, read in each end's units; ML's E is energy held during the write, not
     spent.  A single collective transition to an orthogonal pattern needs only h / (4 t) whatever I: H-ONE-STEP-PER-BIT
     is load-bearing.
  D8 THE TENSIONS FROM TWO POSITIONS.  [P-TENS, P-SCALE, P-MPL, H-SAME-LAGRANGIAN]  In each plane's OWN units (as P-JUMP
     and D7) the two vacuum energies are equal and opposite, +-(4.88 TeV)^4; each plane reads the OTHER's as e^{4 k r_c
     pi} = 1e60 off (ours reads theirs +5.7e74 GeV^4; theirs reads ours -5.7e-46 of its own GeV^4).  The inhomogeneity
     is between the two perspectives at the same time, not between the planes (check 4).  The pair is required for each
     plane to be flat and static (P-TENS); it does not fix the distance between them, an unstabilised modulus (RS
     p.4).  -- a CANDIDATE for H-TWO-PERSPECTIVE-TENSION, not shown to be it.  'At the same time' is defined: static
     RS has a global time (BULK.md section 6).

NAMED HYPOTHESES
  H-CONFINED, H-UNSTABILISED, H-GRAVITATIONAL-CARRIER (bulk.py), H-STATIC-COUPLING, H-ONE-STEP-PER-BIT, H-WRITE-IN-JUMP,
  H-UNKNOWN-STATE, H-NO-MATERIALISATION, H-RESET-STOCK, H-WIDTH-LAW (searches.py); bulk.py's H-RS1, H-RS1-WARP,
  H-K-PLANCK, H-SAME-LAGRANGIAN, H-OBSERVED-FRAME, H-STATIC-SLICING; measure.py's counting hypotheses and H-TBODY; and
  M's, as listed.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * D8 first said 'the hidden plane reads +24 M^3 k and ours reads -24 M^3 k e^{-4 k r_c pi}: opposite in sign and
    e^{4 k r_c pi} = 1e60 apart' as 'each read in its own plane's units' -- the hidden value was in g-bar (OUR) units;
    in each plane's own units they are equal and opposite, and the 1e60 is between perspectives.
  * D8 first said 'P-TENS says the pair is what holds the two planes in a static, flat relation' -- RS leave the
    separation an unstabilised modulus.
  * D5 first said 'A way out would be a carrier coupled differently at the two planes' -- tau <= hbar/Gamma_A whatever
    the B coupling; the asymmetry is deduced (~1e-30) and the real escapes are a stable carrier or a switched coupling.
    Its lifetimes were compared with a jump at a different parameter point; now tau/jump per coupling.
  * D2 first named 'the KK gravitons, or the radion' as loaded by one term; the radion is not in it, the zero mode is,
    and stabilisation adds a scalar.
  * D3 first said 'Either way, LEAVING is a separation of information from matter' and pointed at S1B-O1 for
    classical/quantum; a classical copy separates nothing unless A is erased, and S1B-O1 is H-WHICH-COUNT.
  * D6 first said the destination's fields are ones 'which the bulk cannot supply'; decays do make particles there --
    H-NO-MATERIALISATION is now named.
  * D7 first gave E t >= h I / 2 only, called the invariance 'P-ML's invariant', said 'never a single speed', and
    tabled 9.6e21 J against 9.6e6 J as different needs; it was carried under H-INFO-RELATIVE-SPEED ('relative to the
    information travelling'), which M corrected (item 67) to H-POSITION-RELATIVE-SPEED.
  * P-MOVE was printed as 'a move = True' from a declared flag; now transit.py's computed fidelity and B's state.
  * check 1's control (the s = -1 root) was near-tautological; now the orbifold doubling dropped.
"""
import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


@contextlib.contextmanager
def _wd_path():
    """measure.py imports its board owners by name at call time; WD is put on sys.path for those calls only."""
    saved = list(sys.path)
    sys.path.insert(0, WD)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            yield
    finally:
        sys.path[:] = saved


_saved_path = list(sys.path)
try:
    sys.path.insert(0, WD)
    with contextlib.redirect_stdout(io.StringIO()):
        bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))
        searches = _by_path("bulk_searches", os.path.join(HERE, "searches.py"))
        measure = _by_path("d68_measure", os.path.join(D68, "measure.py"))
        transit = _by_path("wd_transit", os.path.join(WD, "transit.py"))
finally:
    sys.path[:] = _saved_path

C = bulk.C
HBARC_GEV_M = bulk.HBARC_GEV_M
with _wd_path():
    HBAR = measure.import_board()[0].HBAR
H_PLANCK = 2 * math.pi * HBAR
GEV_J = searches.higgs.GEV_IN_J
GEV4_TO_J_M3 = GEV_J / HBARC_GEV_M ** 3          # 1 GeV^4 (natural units) as J/m^3
CMS_WIDTH_FRAC_AT_01 = searches.CMS["widths_pct"][0.1] / 100.0
CMS_LIMIT_AT_01_GEV = searches.CMS["limits"][0.1]


# ------------------------------------------------------------------ the premises transcribed and matched
def rs_eq11_from_eqs7to10(orbifold_doubling=True):
    """RS eqs. 7-10 with sigma = k r_c |phi| (eq. 9): sigma'^2 = k^2 r_c^2 gives Lambda; sigma'' = 2 k r_c [delta(phi) -
    delta(phi - pi)] (eq. 10, the orbifold doubling) gives the brane tensions.  (Lambda, V_hid, V_vis) in units of M^3."""
    import sympy as sp
    k, rc, M3 = sp.symbols("k r_c M3", positive=True)
    Lam = -24 * M3 * (k * rc) ** 2 / rc ** 2                              # eq. 7
    jump = (2 if orbifold_doubling else 1) * k * rc                         # eq. 10's coefficient of delta(phi)
    V_hid = 3 * jump / rc ** 2 * 4 * M3 * rc                                # eq. 8, delta(phi) coefficients matched
    return sp.simplify(Lam), sp.simplify(V_hid), sp.simplify(-V_hid), (k, rc, M3)


def rs_eq16_integral(abs_value=True):
    """M_Pl-bar^2 / M^3 = r_c int_{-pi}^{pi} e^{-2 k r_c |phi|} d phi (RS eq. 16), symbolic."""
    import sympy as sp
    k, rc, phi = sp.symbols("k r_c phi", positive=True)
    f = sp.exp(-2 * k * rc * (sp.Abs(phi) if abs_value else phi))
    val = rc * (2 * sp.integrate(sp.exp(-2 * k * rc * phi), (phi, 0, sp.pi)) if abs_value
                else sp.integrate(f, (phi, -sp.pi, sp.pi)))
    return sp.simplify(val), sp.simplify((1 - sp.exp(-2 * k * rc * sp.pi)) / k)


def ml_overlap(t_over_h_over_4E, E=1.0):
    """|<psi_0|psi_t>| for Margolus-Levitin's two-level state (|0> + |2E>)/sqrt 2 (eq. 10), h = 1."""
    t = t_over_h_over_4E / (4 * E)
    s = 0.5 * (1 + complex(math.cos(2 * math.pi * 2 * E * t), -math.sin(2 * math.pi * 2 * E * t)))
    return abs(s)


def tensions(own_units=True):
    """(hidden, ours) vacuum energies in GeV^4.  own_units: each plane in its own units (H-SAME-LAGRANGIAN: the hidden
    plane's unit of energy is e^{k r_c pi} times ours); otherwise both in g-bar (our) units."""
    x = bulk.rs_geometry()["k_pi_rc"]
    mpl = searches.m_pl_bar_gev()
    k = bulk.RS["k_GeV"]
    M3 = mpl ** 2 * k / (1 - math.exp(-2 * x))
    v_hid_gbar = 24 * M3 * k
    v_vis_gbar = -24 * M3 * k * math.exp(-4 * x)
    return (v_hid_gbar * math.exp(-4 * x) if own_units else v_hid_gbar), v_vis_gbar


def hidden_coupling_ratio():
    """|coupling of KK mode 1 at the hidden plane| / |at ours| from DHR eqs. 6-8 (P-KKPROF): the Neumann condition at
    phi = 0 gives alpha_1 = -J_1(z0)/Y_1(z0) ~ (pi/4) z0^2, so chi_1(0) ~ -1/N_1 to O(z0^2), z0 = x_1 e^{-k r_c pi}
    ~ 4e-15; at our plane chi_1(pi) = e^{2 k r_c pi} J_2(x_1)/N_1.  Both couple through 1/M^{3/2} chi/sqrt(r_c):
    ratio = e^{-2 k r_c pi} / J_2(x_1)."""
    x = bulk.rs_geometry()["k_pi_rc"]
    return math.exp(-2 * x) / abs(searches.bessel_j(2, searches.X1))


def stasis():
    """tau = hbar/Gamma and tau/jump = 1/(x_1 Gamma/m_1) at several couplings."""
    hbar_gev_s = HBARC_GEV_M / C
    mpl = searches.m_pl_bar_gev()
    out = []
    pts = [("CMS edge (k/M 0.1, 4.78 TeV, width 1.42 % READ)", CMS_WIDTH_FRAC_AT_01, CMS_LIMIT_AT_01_GEV),
           ("narrow-width limit (k/M 0.3, ATLAS law)", searches.ATLAS["width_coeff"] * 0.09, None),
           ("k/M 0.01 at warp 1e15 (ATLAS law)", searches.ATLAS["width_coeff"] * 1e-4,
            searches.X1 * 0.01 * mpl / 1e15)]
    q = searches.compute()["board_rs"]
    pts.append(("bulk.py's point (k/M 0.82, H-WIDTH-LAW outside validity)", q["width_frac_atlas_law"], q["m1_GeV"]))
    for name, w, m1 in pts:
        row = {"point": name, "width_frac": w, "tau_over_jump": 1.0 / (searches.X1 * w)}
        if m1 is not None:
            row["m1_GeV"] = m1
            row["tau_s"] = hbar_gev_s / (w * m1)
        out.append(row)
    return out


def move_facts():
    psi = [complex(math.cos(0.3), 0.0), complex(math.cos(0.7), math.sin(0.7)) * math.sin(0.3)]
    fids = [transit.fidelity(psi, v) for _, v in transit.teleport(psi)]
    rho = transit.b_state_without_bits(psi)
    return {"fidelity_min": min(fids), "fidelity_max": max(fids),
            "b_without_bits_dev_from_half_identity": max(abs(rho[0][0] - 0.5), abs(rho[1][1] - 0.5), abs(rho[0][1]))}


# ------------------------------------------------------------------ the deductions' numbers
def compute():
    g = bulk.rs_geometry()
    j = bulk.rs_jump(g)
    x = g["k_pi_rc"]
    th, tv = tensions(True)
    th_gbar, _ = tensions(False)
    with _wd_path():
        ob = measure.object_bits()
    counts = {"species sequence (H-LISTED)": ob["species_sequence_bits"],
              "grid 1 A (H-GRID, H-RHO)": ob["grid"][1e-10]["bits"],
              "grid 0.1 A (H-GRID, H-RHO)": ob["grid"][1e-11]["bits"],
              "thermal entropy (H-THERMO)": ob["thermo_bits"]}
    I_lo, I_hi = min(counts.values()), max(counts.values())
    t_ours, t_hid = j["ours_s"], j["hidden_own_s"]
    et_par, et_seq = H_PLANCK * I_lo / 4, H_PLANCK * I_lo / 2
    body_j = 70.0 * C ** 2
    with _wd_path():
        holder = {"bekenstein_floor_B_J_R1m": measure.bekenstein_floor_j(I_lo, 1.0),
                  "landauer_B_J_310K": measure.landauer_j(I_lo, measure.T_BODY)}
    return {"warp": math.exp(x), "k_pi_rc": x, "jump_ours_s": t_ours, "jump_hidden_own_s": t_hid,
            "clock_ratio_two_ends": t_hid / t_ours,
            "V_hid_own_GeV4": th, "V_vis_own_GeV4": tv, "V_own_fourth_root_TeV": abs(tv) ** 0.25 / 1e3,
            "V_hid_in_our_units_GeV4": th_gbar, "V_vis_in_hidden_own_units_GeV4": tv * math.exp(-4 * x),
            "cross_perspective_ratio": th_gbar / abs(th),
            "bits": counts, "I_lo": I_lo, "I_hi": I_hi,
            "Et_min_parallel_Js": et_par, "Et_min_sequential_Js": et_seq,
            "E_min_at_our_jump_parallel_J": et_par / t_ours, "E_min_at_our_jump_sequential_J": et_seq / t_ours,
            "E_min_parallel_over_body": et_par / t_ours / body_j, "E_min_at_1s_parallel_J": et_par,
            "body_mc2_J": body_j, "hidden_coupling_ratio": hidden_coupling_ratio(), "stasis": stasis(),
            "move": move_facts(), **holder}


def report():
    d = compute()
    print("crossing.py -- O6: leaving, stasis in the corridor, arriving -- by deduction (verified once; not seated)\n")
    m = d["move"]
    print("LEAVING (D1-D3): the information crosses, the matter stays (H-CONFINED); carriers in RS1: the KK tower, the "
          "stable zero mode, the radion; a classical pattern is copied unless erased, an unknown quantum pattern is "
          "moved (transit.py: fidelity %.15f at B on all outcomes; B holds I/2 without the bits, dev %.1e)" % (
              m["fidelity_min"], m["b_without_bits_dev_from_half_identity"]))
    print("STASIS (D4-D5): tau <= hbar/Gamma_A; in jump times:")
    for r in d["stasis"]:
        print("    %-60s tau/jump = %6.2f%s" % (r["point"], r["tau_over_jump"],
                                               ("   (tau = %.1e s)" % r["tau_s"]) if "tau_s" in r else ""))
    print("    the KK modes couple %.1e as strongly at the hidden plane (DHR eqs. 6-8): they return to ours; the zero "
          "mode does not decay" % d["hidden_coupling_ratio"])
    print("ARRIVING (D6): for I = %.2e bits a 1 m holder needs E >= %.1f J (Bekenstein, non-binding); resetting a "
          "non-blank stock at 310 K costs >= %.2e J (Landauer, H-RESET-STOCK); H-NO-MATERIALISATION named" % (
              d["I_lo"], d["bekenstein_floor_B_J_R1m"], d["landauer_B_J_310K"]))
    print("\nTHE RATE (D7): both ends count the same I; their clocks read the crossing %.2e s and %.2e s -- a clock "
          "ratio of %.0e common to every process (H-POSITION-RELATIVE-SPEED); with H-WRITE-IN-JUMP, E t >= %.2e J s "
          "(parallel) or %.2e (sequential): E >= %.2e J at our jump time (%.0f x mc^2), one requirement read in each "
          "end's units" % (d["jump_ours_s"], d["jump_hidden_own_s"], d["clock_ratio_two_ends"], d["Et_min_parallel_Js"],
                           d["Et_min_sequential_Js"], d["E_min_at_our_jump_parallel_J"], d["E_min_parallel_over_body"]))
    print("THE TENSIONS (D8): in each plane's own units +%.2e and %.2e GeV^4 = +-(%.2f TeV)^4 -- equal and opposite; "
          "each reads the other's %.0e off (ours reads theirs %.2e GeV^4) -- a CANDIDATE for H-TWO-PERSPECTIVE-TENSION" % (
              d["V_hid_own_GeV4"], d["V_vis_own_GeV4"], d["V_own_fourth_root_TeV"], d["cross_perspective_ratio"],
              d["V_hid_in_our_units_GeV4"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    import sympy as sp
    Lam, Vh, Vv, (k, rc, M3) = rs_eq11_from_eqs7to10(True)
    chk("RS eq. 11 transcribed and matched from RS eqs. 7-10: Lambda = %s, V_hid = %s, V_vis = %s (READ: -24M^3k^2, "
        "+24M^3k, -24M^3k)" % (Lam, Vh, Vv),
        sp.simplify(Lam + 24 * M3 * k ** 2) == 0 and sp.simplify(Vh - 24 * M3 * k) == 0 and sp.simplify(Vv + 24 * M3 * k) == 0)
    _, Vh1, _, _ = rs_eq11_from_eqs7to10(False)
    chk("without eq. 10's orbifold doubling the hidden tension comes out %s, not 24M^3k" % Vh1,
        sp.simplify(Vh1 - 24 * M3 * k) != 0, ctl=True)
    got, want = rs_eq16_integral(True)
    chk("RS eq. 16 matched: r_c int e^{-2 k r_c |phi|} d phi = %s (READ: (1 - e^{-2 k r_c pi}) / k)" % got,
        sp.simplify(got - want) == 0)
    got_n, _ = rs_eq16_integral(False)
    chk("dropping the |phi| changes it (%s), so the check can fail" % sp.simplify(got_n),
        sp.simplify(got_n - want) != 0, ctl=True)
    chk("Margolus-Levitin eq. 4 is attained by eq. 10's state at t = h/4E (|S| = %.1e); the bound itself is READ" %
        ml_overlap(1.0), ml_overlap(1.0) < 1e-12)
    chk("and not before: at t = 0.9 h/4E |S| = %.3f" % ml_overlap(0.9), ml_overlap(0.9) > 0.1, ctl=True)
    th, tv = tensions(True)
    th_g, tv_g = tensions(False)
    chk("D8: in each plane's own units the two tensions are equal and opposite (%.6e vs %.6e GeV^4)" % (th, tv),
        abs(th + tv) / abs(tv) < 1e-12)
    chk("mixing frames (the hidden in g-bar, ours in its own) gives %.0e, the cross-perspective factor, not 1" %
        abs(th_g / tv_g), abs(th_g / tv_g) > 1e59, ctl=True)
    d = compute()
    chk("P-MOVE: transit.py's teleportation arrives at fidelity 1 on all four outcomes (min %.15f) and B holds I/2 "
        "without the bits (dev %.1e)" % (d["move"]["fidelity_min"], d["move"]["b_without_bits_dev_from_half_identity"]),
        d["move"]["fidelity_min"] > 1 - 1e-12 and d["move"]["b_without_bits_dev_from_half_identity"] < 1e-12)
    structural.append("D7's count invariance is dimensional analysis on P-SCALE (E t / h is dimensionless; hbar and c "
                      "are not rescaled); the two clocks differ by %.0e, a ratio common to every process" %
                      d["clock_ratio_two_ends"])
    structural.append("D5's tau/jump = 1/(x_1 Gamma/m_1) is arithmetic on READ widths (CMS) and the ATLAS law "
                      "(H-WIDTH-LAW); a single KK mode is a standing profile across the bulk, so the ratio compares "
                      "widths, it is not a race")
    structural.append("D5's hidden-plane coupling ratio %.1e uses the leading small-argument Bessel forms at z0 ~ 4e-15 "
                      "(DHR eqs. 6-8)" % d["hidden_coupling_ratio"])
    structural.append("D8 is a CANDIDATE correspondence for H-TWO-PERSPECTIVE-TENSION: equal and opposite in each "
                      "plane's own units, 1e60 apart across perspectives; that it is M's tension is not shown")
    structural.append("scope: D1, D2, D4, D5, D7, D8 are RS-specific (H-RS1 and bulk.py's frame hypotheses); D3's and "
                      "D6's floors are not")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("crossing.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
