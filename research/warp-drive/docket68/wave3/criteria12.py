#!/usr/bin/env python3
"""
criteria12.py -- DOCKET 68 wave 3, W3B: the twelve criteria at A and at B (M-RULINGS items 23-24).

Not seated.  stdlib + numpy.  The twelve are IMPORTED from settle.H12 (each as the taxonomy PDF defines it, with its
class and its READ bound), the potentials from step1b/compensate.py, the stock gate from seat.py; outside results READ
with the route recorded.

    python3 criteria12.py              report
    python3 criteria12.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 criteria12.py --json       the numbers as JSON

M'S WORDS (M-RULINGS-2026-10-03.md, verbatim)
  item 23: "Each one is a physics condition that governs an aspect of the reconstruction at seating. These 12 allow for
           the predetermination of seat compatibility based on the starting state - entanglement at 12 criteria."
  item 24: "The 12 conditions only need to supply enough for the object to reconstruct in the new environment, based on
           the stock of available matter, whether or not the environment is habitable/hospitable by the object, is not
           a factor."  (H-12Q: the twelve are "literally quantum-correlated between the positions".)

WHAT IT COMPUTES
  (1) THE TWELVE BY KIND, from settle.H12's class column: EMERGENT (M, R: readouts of other constants), MATERIAL PROPERTY
      (K, T), and eight others whose H12 classes are LAGRANGIAN PARAMETER (CP, alpha_s, G_theta), DERIVED (Z0), 'CONSTANT
      in GR; a field only if dark energy is dynamical' (Lambda), COUPLING of the metric field (G), LAGRANGIAN-DERIVED
      (G_F) and EXPECTATION VALUE OF A BOSONIC FIELD (v).  'constant' below is this file's residual label for those
      eight, not an H12 class; they are not independent (Z0, M and R reduce to alpha; G_F is tied to v at tree level).
  (2) CAN EACH DIFFER BETWEEN A (EARTH) AND B (PROXIMA b)?  A and B are joined at one moment (corridors.py's H-FRAME),
      so a TIME drift bound is not the question; a SPATIAL one is.  The only READ bound on how a criterion depends on
      place is Z0's (alpha's) coupling to the gravitational potential, (c^2/alpha) d alpha / d Phi = 14(11)e-9
      (settle.H12, 2010.06620v2 Table II, READ by the board).  That coefficient was measured on the ANNUAL variation of
      the Sun's potential at Earth (Delta Phi/c^2 ~ 1.65e-10, Lange et al. p.4, as the W3B verifier READ); applying it to
      the potential difference between Earth's surface and Proxima b (compensate.eps_A / eps_B, imported; -1.5e-8 c^2,
      about 91x the measured lever arm, and from other sources of potential) needs H-LINEAR-PHI.  Under it:
      |Delta alpha / alpha| <= 25e-9 |Delta Phi| / c^2 = 3.8e-16 at the 1-sigma upper end of the READ value (5.4e-16 at
      2 sigma; the central value -2.1e-16, itself 1.3 sigma from zero).  M and R, readouts of alpha, inherit it.  For
      the other seven no READ spatial bound exists here: they are equal at A and B under H-UNIFORM-CONSTANTS.
  (3) WHAT 'LITERALLY QUANTUM-CORRELATED' CAN MEAN (H-12Q).  A criterion with a definite value at both seats is a product
      of definite values: its mutual information and its entanglement are 0 (computed).  A criterion that is uncertain
      but EQUAL at both seats (classical shared values -- the reading M set aside in item 24) has mutual information
      1 bit and entanglement 0 (CONTROL).  A Bell pair has quantum mutual information 2 bits and entanglement 1
      (CONTROL).  So H-12Q, as M chose it, needs a criterion that is a quantum observable at each seat.  settle.H12's
      carrier column marks alpha_s, Z0, G, G_F and v as field carriers ('YES' in KR form) and CP, Lambda, G_theta as
      CONDITIONAL: under H-CONSTANTS-ARE-FIELDS those eight can be quantum observables.  The board already carries a
      live route of this kind: settle.py's H-12-CARRIER, a constant whose value depends on the quantum state, with NO
      READ state-dependent bound for alpha_s, G or v (settle.H12_UNBOUNDED, imported).  It is the nearest thing on the
      board to M's 'predetermination ... based on the starting state', and it is NOT excluded.
      Fields' vacua are entangled between separated regions, and extractably at ANY separation, in amounts that fall
      with L/T: Reznik, Retzker & Silman, 'Violating Bell's inequalities in the vacuum', quant-ph/0310058v2 (READ via
      alphaXiv): correlations 'between arbitrarily far-apart regions of the vacuum ... cannot be reproduced by a local
      hidden-variable model' (abstract, p.1); negativity N >= e^-(L/cT)^3 (eq. 8, p.3), numerically N >= e^-(L/T)^2
      (p.3); after local filtering the CHSH inequality is violated 'for every separation distance, L' (p.3); their
      detectors satisfy cT << L (p.2).  Computed at the Proxima span with T = 1 yr: N >= e^-(L/T)^2 ~ 1.5e-8, tiny but
      not zero.  What decays is the EXTRACTED amount -- a lower bound on vacuum entanglement (Reznik 2003 p.3: a '(lower
      bound) measure for vacuum entanglement'), not the vacuum entanglement itself.  Reznik, 'Entanglement from the
      vacuum', quant-ph/0212044v2 (READ): field correlations fall as 1/L^2 (p.2); for HIS cos^2 window with gap
      Omega ~ 9.5/T (pp.11-12, Figs. 1-2) inertial probes extract entanglement only for 1 <= L/T < 1.1, i.e. at the
      Proxima span 3.86 <= T < 4.25 yr (T < L/c keeps the probes causally disconnected, p.10); accelerated probes
      extract at any L, with exponentially small amplitudes (p.10).
  (4) THE PREDETERMINATION TEST (M, item 23).  Compatibility is reconstructibility from B's stock (item 24).  UNDER
      H-UNIFORM-CONSTANTS, H-LINEAR-PHI, H-SAME-COMPOSITION and H-SAME-ISOTOPES, and with H-12-CARRIER false, the ten
      non-material criteria are the same at B and decide nothing between seats, and the two MATERIAL criteria equal A's
      when the object is rebuilt from B's stock -- so the test reduces to the stock gate.  This is assigned from those
      hypotheses, not derived (the selftest prints it STRUCTURAL).  The gate is computed from the starting state: the
      object's elements against a stock, seat.per_element_stock, on the board's CI-chondrite proxy for a primitive body
      (seat.py's stock; H-CI-PROXY).  At Proxima it is OPEN: the binder P is measured nowhere in the system
      (seat.P_MEASURED_IN_PROXIMA_SYSTEM).  With H-12-CARRIER true, a state-dependent criterion could distinguish
      seats: that branch is OPEN.

NAMED HYPOTHESES
  H-12Q                  (M, item 24) the twelve are literally quantum-correlated between the positions.
  H-UNIFORM-CONSTANTS    a constant with no READ spatial bound has the same value at A and B (standard physics).
  H-LINEAR-PHI           alpha couples linearly to the total Newtonian potential, whatever its source, beyond the
                         annual-modulation range on which its coefficient was measured.
  H-CONSTANTS-ARE-FIELDS a constant is a dynamical field (H12's YES and CONDITIONAL carriers); only then can it be a
                         quantum observable at each seat.
  H-12-CARRIER           (settle.py) a constant's value depends on the quantum state; for alpha_s, G, v no READ bound.
  H-REZNIK-WINDOW        L/T < 1.1 is Reznik 2003's cos^2 window with Omega ~ 9.5/T only; other windows extract at any L
                         (Reznik-Retzker-Silman, READ above).
  H-CI-PROXY             B's stock is represented by the board's CI-chondrite composition (seat.py).
  H-SAME-COMPOSITION, H-SAME-ISOTOPES (step1b/balance.py).

HISTORY (first said, corrected after the W3B verifier, 2026-10-05):
  - 'the entanglement two inertial probes extract persists only for L/T < 1.1' and H-REZNIK-WINDOW's 'another choice
    moves the number, not the fact that extraction ends at finite L/T' -- declared, and contradicted at source by
    Reznik-Retzker-Silman (READ): extraction at any L.  'the least switching time is L/(1.1 c)' is now two-sided.
  - H-12Q was scoped to 'settle.H12's CONDITIONAL rows'; H12 marks five more as field carriers, and settle's
    H-12-CARRIER route was not carried.
  - the alpha bound was applied to the Earth-Proxima b potential without naming H-LINEAR-PHI.
  - 'fixed numbers of physics' and '8 constants by settle.H12's own classes' -- 'constant' is this file's label.
  - the ten-criteria reduction to the stock gate was counted as a check; it is assigned from hypotheses.
  - the docstring quoted Reznik p.12 as 'the probes must be'; the source prints 'the probed must be' [sic].
"""
import contextlib
import io
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.abspath(os.path.join(HERE, ".."))
WD = os.path.abspath(os.path.join(D68, ".."))
for _p in (os.path.join(WD, "step1b"), WD, D68):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import settle
    import seat
    import compensate

RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
M_WORDS_23 = ("Each one is a physics condition that governs an aspect of the reconstruction at seating. These 12 allow "
              "for the predetermination of seat compatibility based on the starting state - entanglement at 12 "
              "criteria.")
C = compensate.C
ALPHA_PHI = (14e-9, 11e-9)          # settle.H12's Z0 row, READ by the board (2010.06620v2 Table II)
RRS_2004 = {"source": "quant-ph/0310058v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-4",
            "used": "abstract: arbitrarily far-apart regions, no LHV model; eq. 8 N >= e^-(L/cT)^3; numerically "
                    "N >= e^-(L/T)^2 (p.3); CHSH violated for every L after filtering (p.3); cT << L (p.2)"}
REZNIK_2003 = {"source": "quant-ph/0212044v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-13",
               "field_correlation_falloff": "1/L^2 (massless, 3+1 D; p.2)", "L_over_T_max": 1.1, "gap_OmegaT": 9.5,
               "quote_p12": "the probed must be \"contained\" in the space-like range of a single coherent vacuum "
                            "fluctuation"}


# ============================================================================ (1) the twelve by kind
def kind(cls):
    if cls.startswith("EMERGENT"):
        return "emergent"
    if cls.startswith("MATERIAL PROPERTY"):
        return "material"
    return "constant"


def kinds():
    out = {"emergent": [], "material": [], "constant": []}
    for r in settle.H12:
        out[kind(r[2])].append(r[0])
    return out


def alpha_row_bound_text():
    return [r for r in settle.H12 if r[0] == "Z0"][0][5]


# ============================================================================ (2) can each differ between A and B?
def delta_phi():
    a, b = compensate.eps_A(), compensate.eps_B()
    phiA = a["phi_sun"] + a["phi_self"]
    phiB = [b["phi_common"] + s for s in b["phi_self_range_at_msini"]]
    return phiA, phiB, [p - phiA for p in phiB]


def alpha_ab_bound():
    _, _, dphi = delta_phi()
    coef = ALPHA_PHI[0] + ALPHA_PHI[1]
    return {"dPhi_over_c2": [d / C ** 2 for d in dphi],
            "max_abs_dalpha_over_alpha": max(coef * abs(d) / C ** 2 for d in dphi),
            "max_abs_2sigma": max((ALPHA_PHI[0] + 2 * ALPHA_PHI[1]) * abs(d) / C ** 2 for d in dphi),
            "central": [ALPHA_PHI[0] * d / C ** 2 for d in dphi],
            "coef_1sigma_upper": coef, "value_over_sigma": ALPHA_PHI[0] / ALPHA_PHI[1]}


def differ_table():
    b = alpha_ab_bound()["max_abs_dalpha_over_alpha"]
    rows = []
    for r in settle.H12:
        k = kind(r[2])
        if r[0] == "Z0":
            st = "READ coefficient, extrapolated (H-LINEAR-PHI): |d alpha/alpha| <= %.2g between A and B" % b
        elif k == "emergent":
            st = "inherits alpha's bound (a readout of alpha): <= %.2g" % b
        elif k == "material":
            st = "set by the materials, i.e. by B's stock (the predetermination test)"
        else:
            st = "no READ spatial bound: equal at A and B under H-UNIFORM-CONSTANTS"
        rows.append({"symbol": r[0], "kind": k, "A_vs_B": st})
    return rows


# ============================================================================ (3) what H-12Q can mean
def mutual_info_classical(P):
    P = np.asarray(P, float)
    pa, pb = P.sum(1), P.sum(0)
    return float(sum(P[i, j] * math.log2(P[i, j] / (pa[i] * pb[j]))
                     for i in range(P.shape[0]) for j in range(P.shape[1]) if P[i, j] > 0))


def vn(rho):
    w = np.linalg.eigvalsh(rho)
    return float(-sum(x * math.log2(x) for x in w if x > 1e-15))


def quantum_mi_pure(psi, dA=2, dB=2):
    m = psi.reshape(dA, dB)
    rA = m @ m.conj().T
    rB = m.T @ m.conj()
    return vn(rA) + vn(rB), vn(rA)


def definite_vs_bell():
    P_def = [[0, 0], [0, 1]]                      # both seats hold the same definite value
    P_shared = [[0.5, 0], [0, 0.5]]               # uncertain but equal at both seats: classical shared values
    prod = np.kron([0, 1], [0, 1]).astype(complex)
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    return {"definite_classical_MI": mutual_info_classical(P_def), "shared_classical_MI": mutual_info_classical(P_shared),
            "definite_product_QMI_ent": quantum_mi_pure(prod),
            "bell_QMI_ent": quantum_mi_pure(bell)}


def reznik_min_switch_time():
    """Reznik 2003's window only: 1 <= L/cT < 1.1, i.e. L/(1.1 c) <= T < L/c, gap Omega ~ 9.5/T."""
    L = seat.D_PROXIMA
    T = L / (REZNIK_2003["L_over_T_max"] * C)
    return {"L_m": L, "T_min_s": T, "T_min_yr": T / seat.YEAR_S, "light_time_yr": L / C / seat.YEAR_S,
            "gap_eV_at_Tmin": REZNIK_2003["gap_OmegaT"] / T * compensate.HBAR / 1.602176634e-19}


def rrs_lower_bound(T_s):
    """Reznik-Retzker-Silman's numerical lower bound on the extracted negativity, e^-(L/cT)^2, at the Proxima span."""
    x = seat.D_PROXIMA / (C * T_s)
    return {"T_s": T_s, "L_over_cT": x, "N_lower_numeric": math.exp(-x ** 2), "N_lower_eq8": math.exp(-x ** 3),
            "log10_numeric": -x ** 2 / math.log(10.0), "log10_eq8": -x ** 3 / math.log(10.0)}


def carrier_route():
    """settle.py's H-12-CARRIER: the H12 rows with no READ state-dependent bound, and H12's carrier column."""
    col = {r[0]: r[4] for r in settle.H12}
    return {"unbounded": list(settle.H12_UNBOUNDED),
            "field_carriers_yes": [k for k, v in col.items() if v.startswith("YES")],
            "conditional": [k for k, v in col.items() if v.startswith("CONDITIONAL")]}


# ============================================================================ (4) the predetermination test
def predetermination(gate=None):
    k = kinds()
    gate = seat.P_MEASURED_IN_PROXIMA_SYSTEM if gate is None else gate
    binder = seat.binders()["CI chondrite"][0][0]
    per = seat.per_element_stock()["CI chondrite"]
    return {"decide_nothing_between_seats": k["constant"] + k["emergent"], "decided_by_stock": k["material"],
            "reduces_to": "the stock gate (seat.per_element_stock against the seat's holdings), under the hypotheses "
                          "named in (4) and with H-12-CARRIER false",
            "ci_stock_needed_kg": max(per.values()), "ci_stock_by_element_kg": per,
            "binder": binder, "binder_measured_at_proxima": gate,
            "verdict_at_proxima": "OPEN (the binder is measured nowhere in the system)" if not gate else "test"}


def collect():
    return {"kinds": kinds(), "alpha_ab": alpha_ab_bound(), "differ": differ_table(), "h12q": definite_vs_bell(),
            "reznik": reznik_min_switch_time(), "rrs": [rrs_lower_bound(f * seat.YEAR_S) for f in (0.1, 0.5, 1.0)],
            "carrier_route": carrier_route(), "predetermination": predetermination(), "READ": [REZNIK_2003, RRS_2004]}


def report():
    d = collect()
    print("W3B -- the twelve criteria at A and B (M-RULINGS items 23-24)")
    print('  M: "%s"' % M_WORDS_23)
    k = d["kinds"]
    print("\n(1) by kind (settle.H12's class column; 'constant' is this file's residual label): other %d %s; emergent %d "
          "%s; material %d %s" % (len(k["constant"]), k["constant"], len(k["emergent"]), k["emergent"],
                                  len(k["material"]), k["material"]))
    a = d["alpha_ab"]
    print("(2) A (Earth) against B (Proxima b): Delta Phi / c^2 from %.3g to %.3g; under H-LINEAR-PHI "
          "|Delta alpha / alpha| <= %.2g (1 sigma upper end; %.2g at 2 sigma)"
          % (a["dPhi_over_c2"][0], a["dPhi_over_c2"][1], a["max_abs_dalpha_over_alpha"], a["max_abs_2sigma"]))
    for r in d["differ"]:
        print("    %-8s %-9s %s" % (r["symbol"], r["kind"], r["A_vs_B"]))
    h = d["h12q"]
    print("(3) H-12Q: definite value at both seats -- classical MI %.1f, quantum MI and entanglement %s"
          % (h["definite_classical_MI"], h["definite_product_QMI_ent"]))
    print("    CONTROL shared but uncertain value -- classical MI %.1f, entanglement 0; CONTROL Bell pair -- %s"
          % (h["shared_classical_MI"], h["bell_QMI_ent"]))
    cr = d["carrier_route"]
    print("    H12 field carriers (YES) %s, CONDITIONAL %s; H-12-CARRIER with no READ bound: %s -- NOT excluded"
          % (cr["field_carriers_yes"], cr["conditional"], cr["unbounded"]))
    for x in d["rrs"]:
        print("    vacuum entanglement at the Proxima span, any L (Reznik-Retzker-Silman, READ): T = %.3g s, L/cT = %.3g: "
              "extracted negativity >= 10^%.4g (numerical), >= 10^%.4g (eq. 8)"
              % (x["T_s"], x["L_over_cT"], x["log10_numeric"], x["log10_eq8"]))
    r = d["reznik"]
    print("    Reznik 2003's cos^2 window only: %.2f <= T < %.2f yr, gap ~ %.3g eV"
          % (r["T_min_yr"], r["light_time_yr"], r["gap_eV_at_Tmin"]))
    p = d["predetermination"]
    print("(4) predetermination: %s; CI stock needed %.4g kg (binder %s); measured at Proxima: %s -> %s"
          % (p["reduces_to"], p["ci_stock_needed_kg"], p["binder"], p["binder_measured_at_proxima"],
             p["verdict_at_proxima"]))
    print("    with H-12-CARRIER true a state-dependent criterion could distinguish seats: OPEN")


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = bool(got == want) if not isinstance(want, (list, tuple, dict)) else got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("criteria12.py selftest")
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    chk("M's item-23 words found verbatim in the rulings file", M_WORDS_23 in txt, True)
    k = kinds()
    chk("twelve criteria from settle.H12", sum(len(v) for v in k.values()), 12)
    chk("by settle.H12's class column: 8 neither EMERGENT nor MATERIAL, 2 emergent (M, R), 2 material (K, T)",
        (len(k["constant"]), k["emergent"], k["material"]), (8, ["M", "R"], ["K", "T"]))
    chk("the alpha-potential coefficient used is settle.H12's Z0 row, read back ('14(11)e-9' in it)",
        "14(11)e-9" in alpha_row_bound_text(), True)
    a = alpha_ab_bound()
    chk("Delta Phi between Earth and Proxima b is of order 1e-8 c^2 (both ends of b's range, |.| in 1e-9..1e-7)",
        all(1e-9 < abs(x) < 1e-7 for x in a["dPhi_over_c2"]), True)
    chk("under H-LINEAR-PHI alpha at B equals alpha at A to better than 1e-15 at 1 and at 2 sigma",
        (a["max_abs_dalpha_over_alpha"] < 1e-15, a["max_abs_2sigma"] < 1e-15), (True, True))
    h = definite_vs_bell()
    chk("a definite value at both seats carries no mutual information and no entanglement",
        (h["definite_classical_MI"], h["definite_product_QMI_ent"]), (0.0, (0.0, 0.0)))
    chk("CONTROL: a shared but uncertain value carries classical MI 1 bit (and no entanglement): agreement is not "
        "entanglement", abs(h["shared_classical_MI"] - 1) < 1e-12, True, ctl=True)
    chk("CONTROL: a Bell pair carries quantum MI 2 bits and entanglement 1 (to 1e-12)",
        (abs(h["bell_QMI_ent"][0] - 2) < 1e-12, abs(h["bell_QMI_ent"][1] - 1) < 1e-12), (True, True), ctl=True)
    cr = carrier_route()
    chk("settle's H-12-CARRIER rows with no READ bound (alpha_s, G, v) are all marked field carriers in H12",
        (cr["unbounded"], all(u in cr["field_carriers_yes"] for u in cr["unbounded"])), (["alpha_s", "G", "v"], True))
    rr = rrs_lower_bound(seat.YEAR_S)
    chk("RRS at the Proxima span, T = 1 yr: the numerical lower bound e^-(L/cT)^2 is positive and below 1e-7",
        0 < rr["N_lower_numeric"] < 1e-7, True)
    per = seat.per_element_stock()["CI chondrite"]
    chk("the CI stock the gate needs (max over elements of seat.per_element_stock) equals stock.feedstock_kg",
        abs(max(per.values()) - seat.stock.feedstock_kg(seat.PAYLOAD_KG, seat.stock.HUMAN,
                                                         seat.stockgate.DESTS["CI chondrite"]())) < 1e-6, True)
    p = predetermination()
    chk("the predetermination at Proxima stays OPEN: the binder is P and P is unmeasured there",
        (p["binder"], p["binder_measured_at_proxima"]), ("P", False))
    chk("CONTROL: were P measured, the verdict would be a test, not OPEN (the logic turns on the measurement)",
        predetermination(gate=True)["verdict_at_proxima"], "test", ctl=True)
    structural.append("the material criteria equal A's when rebuilt from B's stock with the object's composition: "
                      "that is H-SAME-COMPOSITION / H-SAME-ISOTOPES, carried, not derived")
    structural.append("'ten criteria decide nothing between seats' (%d listed) is assigned from H-UNIFORM-CONSTANTS, "
                      "H-LINEAR-PHI and H-12-CARRIER false -- a label lookup, not a computation"
                      % len(p["decide_nothing_between_seats"]))
    r = reznik_min_switch_time()
    structural.append("Reznik 2003's window at the Proxima span: %.2f <= T < %.2f yr (L/(1.1 c) to L/c) -- arithmetic "
                      "on the READ ratio" % (r["T_min_yr"], r["light_time_yr"]))
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
