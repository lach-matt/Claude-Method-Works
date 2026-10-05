#!/usr/bin/env python3
"""
crossing.py -- O6 (BULK-O2): entering and leaving the corridor, as three states -- LEAVING, STASIS IN THE CORRIDOR,
ARRIVING -- with what must cross at each, and at what rate; worked BY DEDUCTION FROM FIRST PRINCIPLES.

Not seated; not yet verified.  M's orders: item 59 ("4, then 3 please.": the pairing shape, then entering and leaving);
item 61 ("Fold into O6 (Recommended)": H-DETACH and H-CORRIDOR-STASIS as three states); item 64 ("1, but I want you to
consider using deduction and first principle as we continue forward in to the unobserved. Such will be the best method
to both determine and fill our gaps": M-DEDUCE); item 66 ("Premises of O6 (Recommended)": H-INFO-RELATIVE-SPEED and
H-TWO-PERSPECTIVE-TENSION as premises).  All of M's hypotheses are carried as hypotheses, never as results.  O9 stays
OPEN.

    python3 crossing.py              report
    python3 crossing.py --selftest   checks, with CONTROLS
    python3 crossing.py --json       the numbers as JSON

THE METHOD (M-DEDUCE, read with the charter).  Every claim below is either a PREMISE -- READ at source (route and page),
COMPUTED by a board owner, or a NAMED hypothesis -- or a DEDUCTION, labelled DEDUCED and listing the premises it uses.
A gap no deduction closes is OPEN.  The geometry is Randall-Sundrum's two planes as bulk.py seats them (H-RS1); the
deductions that depend on that choice say so.

PREMISES
  P-CONF   (READ, Randall & Sundrum hep-ph/9905221v1) The action is S_gravity + S_vis + S_hid (eq. 4, p.2): each plane
           carries its own Lagrangian, and the bulk carries only gravity.  The set-up has 'two three-branes, one of which
           contains the Standard Model fields' (abstract).  Of the flat-dimension case: the SM particles and forces 'with
           the exception of gravity are confined' to the 3-brane (p.1).  NAMED as H-CONFINED: CMS (arXiv:2103.02708 p.3)
           notes RS variants in which SM fields propagate in the bulk, so confinement is the model's choice.
  P-KK     (READ, RS p.2 and p.6; Davoudiasl-Hewett-Rizzo hep-ph/9909255 eq. 10, p.5) The bulk's modes couple to matter
           on our plane through ONE term, L = -(1/M_Pl-bar) T h^(0) - (1/Lambda_pi) T sum_n h^(n): the zero mode at
           gravitational strength, each massive mode at Energy/TeV.
  P-TENS   (READ, RS eq. 11, p.3) V_hid = -V_vis = 24 M^3 k, Lambda = -24 M^3 k^2; 'These relations between the boundary
           and bulk cosmological terms are required in order to obtain a solution that respects four-dimensional
           Poincare invariance' (p.4).  Re-derived here from RS eqs. 7-9 (check 1).
  P-SCALE  (READ, RS eq. 21, p.5-6) a visible mass parameter m_0 is the physical mass e^{-k r_c pi} m_0 'when measured
           with the metric g-bar', 'since all operators get rescaled according to their four-dimensional conformal
           weight'; g_hid = g-bar (p.5).
  P-VIEW   (READ, RS p.6) the TeV scale may equally be regarded as fundamental -- 'the one naturally taken by a
           four-dimensional observer residing on the visible brane'.
  P-MPL    (READ, RS eq. 16, p.5) M_Pl-bar^2 = (M^3 / k)(1 - e^{-2 k r_c pi}).  Re-derived here (check 2).
  P-JUMP   (COMPUTED, bulk.py, seated 8i) between bulk-paired points our clock reads hbar / (k e^{-k r_c pi}); a hidden
           clock of the same physics reads e^{k r_c pi} times as many ticks (H-SAME-LAGRANGIAN).
  P-ML     (READ, Margolus & Levitin quant-ph/9710043v2) a system of average energy E above its ground state passes
           through at most 2E/h mutually orthogonal states per unit time in a long sequence (eq. 2, p.3), and needs at
           least h/(4E) to reach one orthogonal state (eq. 4, p.4; checked here, check 3); 'E t ... tells us the number of
           distinct states that a system with energy E can pass through in time t' (p.10); 'useful' dynamics are
           counted in the rest frame, where E_r t_r is an invariant (p.9).  They bound orthogonal states, NOT bits
           (p.2): one orthogonal step per bit written is NAMED, H-ONE-STEP-PER-BIT.
  P-BITS   (COMPUTED, measure.py) the information defining a 70 kg body under NAMED counts (H-LISTED, H-GRID, H-RHO,
           H-THERMO): 9.5e27 to 1.1e29 bits.  Bekenstein's floor on a holder's energy, E >= I hbar c ln2 / (2 pi R), and
           Landauer's k T ln 2 per bit, are measure.py's (READ there).
  P-MOVE   (COMPUTED, transit.py) teleporting an unknown quantum state is a MOVE, not a copy: A's qubit ends maximally
           mixed; no-cloning is enforced by the protocol.
  M's      H-DETACH, H-CORRIDOR-STASIS (item 60); H-INFO-RELATIVE-SPEED, H-TWO-PERSPECTIVE-TENSION (item 65);
           H-NO-SPEED, H-HIGHER-CORRIDOR (item 57); H-UNOBSERVED-UNBUILT (item 62).

DEDUCTIONS (each DEDUCED from the premises named)
  D1 LEAVING: WHAT CROSSES IS NOT THE MATTER.  [P-CONF]  A field on a plane has its action only on that plane (eq. 4),
     so a body made of such fields cannot itself enter the bulk.  Whatever crosses is an excitation of a bulk field
     carrying the body's defining information.  -- H-DETACH's physical reading: the information leaves; the matter
     stays.
  D2 THE CARRIER IS GRAVITATIONAL.  [P-CONF, P-KK]  In RS1 the bulk holds only the metric, so the carrier is a
     gravitational mode (the KK gravitons, or the radion) and it is loaded through P-KK's one term.
  D3 WHAT HAPPENS TO THE ORIGINAL.  [D1, P-MOVE, P-BITS]  The matter at A keeps its pattern unless something removes it.
     If the defining information is classical it may be copied, and A is left intact (a duplicate, not a departure)
     unless it is erased at Landauer's price; if it is quantum, no-cloning forces the original's state to be given up in
     the transfer (a move).  Either way, LEAVING is a separation of information from matter -- for a quantum pattern a
     forced one.  -- H-DETACH's 'let go' has this counterpart; whether the defining information is classical or quantum
     is OPEN (S1B-O1, H-WHICH-COUNT).
  D4 STASIS: THE INFORMATION HAS NO MATTER FORM IN THE BULK.  [D1, D2]  While it is in the bulk, no plane's Lagrangian
     holds it: it exists only as a gravitational excitation.  -- H-CORRIDOR-STASIS's physical reading ('cannot take
     physical form').
  D5 STASIS DOES NOT HOLD ITSELF.  [P-KK]  One term loads and unloads: the same coupling that writes the information
     into a massive mode decays it back into our plane's matter, and both rates scale as 1/Lambda_pi^2.  So at one plane
     a longer stasis costs a slower loading; an indefinite stasis needs a carrier that does not couple back -- and then
     it cannot be loaded there either.  Computed: the first KK mode's lifetime at CMS's edge (coupling 0.1, 4.78 TeV,
     width 1.42 %, READ) and at bulk.py's point (ATLAS's width law, H-WIDTH-LAW).  A way out would be a carrier coupled
     differently at the two planes; the hidden plane's KK couplings are not READ (OPEN).
  D6 ARRIVING NEEDS MATTER WAITING AT B.  [P-CONF at B, P-BITS]  The information must be written into fields of the
     destination plane, which the bulk cannot supply: B must hold the stock (Step 1b's B stock).  A holder of radius R
     with I bits has E >= I hbar c ln2 / (2 pi R) (Bekenstein, a floor); preparing a stock that is not blank costs at
     least k T ln 2 per bit (Landauer, H-RESET-STOCK).
  D7 TWO PERSPECTIVES AT ONCE: THE COUNT IS SHARED, THE RATE IS NOT.  [P-SCALE, P-JUMP, P-ML]  A bit count is
     dimensionless (conformal weight 0), so both planes count the same information I and the same number of
     orthogonal steps N = 2 E t / h (P-ML's invariant).  Their clocks read the same crossing as different durations
     (P-JUMP, a factor e^{k r_c pi} = 1e15 apart), so the RATE -- information per own unit of time -- differs by that
     factor, at the same moment, between the two ends.  -- H-INFO-RELATIVE-SPEED's computed counterpart: a rate exists,
     relative to the information and to the reading position, never a single speed.  With H-ONE-STEP-PER-BIT, E t >=
     h I / 2 from both ends; at our clock's jump time that needs E >= h I / (2 t).
  D8 TWO PERSPECTIVES AT ONCE: THE TENSIONS.  [P-TENS, P-SCALE, P-MPL]  Each plane carries a vacuum energy: in the 5D
     frame equal and opposite (+-24 M^3 k); each read in its own plane's units (vacuum energy has conformal weight 4)
     the hidden plane reads +24 M^3 k and ours reads -24 M^3 k e^{-4 k r_c pi}: opposite in sign and e^{4 k r_c pi} =
     1e60 apart in magnitude -- an inhomogeneous pair -- and P-TENS says the pair is what holds the two planes in a
     static, flat relation.  -- a CANDIDATE for H-TWO-PERSPECTIVE-TENSION, not shown to be it.  'At the same time' is
     defined here: static RS has a global time (BULK.md section 6).

NAMED HYPOTHESES
  H-CONFINED, H-ONE-STEP-PER-BIT, H-RESET-STOCK (above); H-WIDTH-LAW (searches.py); with bulk.py's H-RS1, H-K-PLANCK,
  H-SAME-LAGRANGIAN, H-STATIC-SLICING; measure.py's counting hypotheses; and M's, as listed.
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


# ------------------------------------------------------------------ the premises re-derived (checks 1 and 2)
def rs_eq11_from_eqs7to9():
    """RS eqs. 7-8 with sigma = k r_c |phi| (eq. 9): sigma'^2 = k^2 r_c^2 gives Lambda; sigma'' = 2 k r_c [delta(phi) -
    delta(phi - pi)] gives the brane tensions.  Returns (Lambda, V_hid, V_vis) in units of M^3, as sympy expressions."""
    import sympy as sp
    k, rc, M3, sgn = sp.symbols("k r_c M3 s", real=True)
    # eq. 7: 6 sigma'^2 / r_c^2 = -Lambda / (4 M^3)
    Lam = -24 * M3 * (sgn * k * rc) ** 2 / rc ** 2
    # eq. 8: 3 sigma'' / r_c^2 = V_hid/(4M^3 r_c) delta(phi) + V_vis/(4M^3 r_c) delta(phi-pi), with sigma'' = 2 s k r_c
    # [delta(phi) - delta(phi-pi)]: match the delta coefficients
    V_hid = 3 * (2 * sgn * k * rc) / rc ** 2 * 4 * M3 * rc
    V_vis = -V_hid
    return sp.simplify(Lam), sp.simplify(V_hid), sp.simplify(V_vis), (k, rc, M3, sgn)


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


# ------------------------------------------------------------------ the deductions' numbers
def compute():
    g = bulk.rs_geometry()
    j = bulk.rs_jump(g)
    x = g["k_pi_rc"]
    warp = math.exp(x)
    mpl = searches.m_pl_bar_gev()
    k = bulk.RS["k_GeV"]
    M3 = mpl ** 2 * k / (1 - math.exp(-2 * x))                         # P-MPL
    v_hid = 24 * M3 * k                                                  # P-TENS, GeV^4
    v_vis_5d = -v_hid
    v_vis_own = v_vis_5d * math.exp(-4 * x)                              # D8: conformal weight 4
    with _wd_path():
        ob = measure.object_bits()
    counts = {"species sequence (H-LISTED)": ob["species_sequence_bits"],
              "grid 1 A (H-GRID, H-RHO)": ob["grid"][1e-10]["bits"],
              "grid 0.1 A (H-GRID, H-RHO)": ob["grid"][1e-11]["bits"],
              "thermal entropy (H-THERMO)": ob["thermo_bits"]}
    I_lo, I_hi = min(counts.values()), max(counts.values())
    t_ours, t_hid = j["ours_s"], j["hidden_own_s"]
    et_lo = H_PLANCK * I_lo / 2                                          # D7: E t >= h I / 2 (H-ONE-STEP-PER-BIT)
    body_j = 70.0 * C ** 2
    # D5: stasis lifetimes
    gam_cms = CMS_WIDTH_FRAC_AT_01 * CMS_LIMIT_AT_01_GEV
    q = searches.compute()["board_rs"]
    gam_board = q["width_frac_atlas_law"] * q["m1_GeV"]
    hbar_gev_s = HBARC_GEV_M / C
    return {
        "warp": warp, "k_pi_rc": x,
        "jump_ours_s": t_ours, "jump_hidden_own_s": t_hid, "rate_ratio_two_ends": t_hid / t_ours,
        "M3_GeV3": M3, "V_hid_GeV4": v_hid, "V_vis_5d_GeV4": v_vis_5d, "V_vis_own_GeV4": v_vis_own,
        "V_hid_J_m3": v_hid * GEV4_TO_J_M3, "V_vis_own_J_m3": v_vis_own * GEV4_TO_J_M3,
        "V_vis_own_fourth_root_TeV": abs(v_vis_own) ** 0.25 / 1e3, "tension_ratio": abs(v_hid / v_vis_own),
        "bits": counts, "I_lo": I_lo, "I_hi": I_hi,
        "Et_min_Js": et_lo,
        "E_min_at_our_jump_J": et_lo / t_ours, "E_min_at_hidden_jump_J_own": et_lo / t_hid,
        "E_min_at_1s_J": et_lo / 1.0, "body_mc2_J": body_j,
        "E_min_at_our_jump_over_body": et_lo / t_ours / body_j,
        "stasis_life_cms_edge_s": hbar_gev_s / gam_cms, "stasis_life_board_s": hbar_gev_s / gam_board,
        "board_width_frac": q["width_frac_atlas_law"],
        "transit_is_a_move": transit.IT_IS_A_MOVE_NOT_A_COPY,
    } | _holder_prices(I_lo)


def _holder_prices(I):
    with _wd_path():
        return {"bekenstein_floor_B_J_R1m": measure.bekenstein_floor_j(I, 1.0),
                "landauer_B_J_310K": measure.landauer_j(I, measure.T_BODY)}


def report():
    d = compute()
    print("crossing.py -- O6: leaving, stasis in the corridor, arriving -- by deduction (not verified; not seated)\n")
    print("LEAVING (D1-D3): what crosses is the information, not the matter (H-CONFINED); the carrier is gravitational "
          "(RS1); the original is left intact (a classical copy), erased at Landauer's price, or -- for a quantum "
          "pattern -- given up by no-cloning (transit.py: a move = %s)" % d["transit_is_a_move"])
    print("STASIS (D4-D5): no matter form in the bulk; but one term loads and unloads, so the carrier decays back: "
          "first KK mode lives %.1e s at CMS's edge (0.1, 4.78 TeV, 1.42 %%), %.1e s at bulk.py's point "
          "(width %.0f %% by H-WIDTH-LAW) -- against the jump's %.2e s on our clock" % (
              d["stasis_life_cms_edge_s"], d["stasis_life_board_s"], 100 * d["board_width_frac"], d["jump_ours_s"]))
    print("ARRIVING (D6): B must hold the matter; for I = %.2e bits a 1 m holder needs E >= %.2e J (Bekenstein floor); "
          "resetting a non-blank stock at 310 K costs >= %.2e J (Landauer, H-RESET-STOCK)" % (
              d["I_lo"], d["bekenstein_floor_B_J_R1m"], d["landauer_B_J_310K"]))
    print("\nTWO PERSPECTIVES (D7): both ends count the same I and the same E t >= h I/2 = %.2e J s; the crossing reads "
          "%.2e s on our clock and %.2e s on a hidden clock, so the rate differs by %.0e between the ends at once" % (
              d["Et_min_Js"], d["jump_ours_s"], d["jump_hidden_own_s"], d["rate_ratio_two_ends"]))
    print("    at our jump time: E >= %.2e J (%.0f x the body's mc^2); at the hidden clock's own reading: E >= %.2e J in "
          "its own units; at 1 s: E >= %.2e J" % (d["E_min_at_our_jump_J"], d["E_min_at_our_jump_over_body"],
                                                d["E_min_at_hidden_jump_J_own"], d["E_min_at_1s_J"]))
    print("TWO PERSPECTIVES (D8): tensions +24M^3k = %.2e GeV^4 (hidden, own units), -24M^3k e^{-4 k pi r_c} = %.2e "
          "GeV^4 = -(%.2f TeV)^4 (ours, own units): opposite in sign, %.0e apart -- a CANDIDATE for "
          "H-TWO-PERSPECTIVE-TENSION" % (d["V_hid_GeV4"], d["V_vis_own_GeV4"], d["V_vis_own_fourth_root_TeV"],
                                         d["tension_ratio"]))


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
    Lam, Vh, Vv, (k, rc, M3, sgn) = rs_eq11_from_eqs7to9()
    ok11 = (sp.simplify(Lam.subs(sgn, 1) + 24 * M3 * k ** 2) == 0 and sp.simplify(Vh.subs(sgn, 1) - 24 * M3 * k) == 0
            and sp.simplify(Vv.subs(sgn, 1) + 24 * M3 * k) == 0)
    chk("RS eq. 11 re-derived from RS eqs. 7-9: Lambda = %s, V_hid = %s, V_vis = %s (READ: -24M^3k^2, +24M^3k, -24M^3k)"
        % (Lam.subs(sgn, 1), Vh.subs(sgn, 1), Vv.subs(sgn, 1)), ok11)
    chk("the derivation is sign-sensitive: with sigma = -k r_c |phi| the hidden tension comes out %s, not +24M^3k" %
        Vh.subs(sgn, -1), sp.simplify(Vh.subs(sgn, -1) + 24 * M3 * k) == 0, ctl=True)
    got, want = rs_eq16_integral(True)
    chk("RS eq. 16 re-derived: r_c int e^{-2 k r_c |phi|} d phi = %s (READ: (1 - e^{-2 k r_c pi}) / k)" % got,
        sp.simplify(got - want) == 0)
    got_n, _ = rs_eq16_integral(False)
    chk("dropping the |phi| changes it (%s), so the check can fail" % sp.simplify(got_n),
        sp.simplify(got_n - want) != 0, ctl=True)
    chk("Margolus-Levitin's two-level state (|0> + |2E>)/sqrt 2 is orthogonal at t = h/4E (|S| = %.1e), eq. 4 attained"
        % ml_overlap(1.0), ml_overlap(1.0) < 1e-12)
    chk("and not before: at t = 0.9 h/4E |S| = %.3f" % ml_overlap(0.9), ml_overlap(0.9) > 0.1, ctl=True)
    d = compute()
    structural.append("D7's count invariance is algebra on P-SCALE and P-JUMP (E and t rescale by inverse factors), "
                      "not a measurement; the two ends' rates differ by %.0e" % d["rate_ratio_two_ends"])
    structural.append("D5's 'one term loads and unloads' is read off DHR eq. 10's single interaction term at tree "
                      "level; the stasis lifetimes are hbar / width with READ (CMS) and law-extrapolated (H-WIDTH-LAW) "
                      "widths")
    structural.append("D8 is a CANDIDATE correspondence for H-TWO-PERSPECTIVE-TENSION: an inhomogeneous pair of "
                      "tensions exists and holds the planes static; that it is M's tension is not shown")
    structural.append("every deduction is conditional on H-RS1 and H-CONFINED; in a geometry whose bulk carries matter "
                      "fields, D1-D4 change")
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
