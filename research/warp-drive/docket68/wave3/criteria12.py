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
  (1) THE TWELVE BY KIND, counted from settle.H12's own class column: EMERGENT (readouts of other constants), MATERIAL
      PROPERTY (per material), and the rest -- Lagrangian parameters, couplings, a derived constant, a field's
      expectation value: fixed numbers of physics.
  (2) CAN EACH DIFFER BETWEEN A (EARTH) AND B (PROXIMA b)?  A and B are joined at one moment (corridors.py's H-FRAME),
      so a TIME drift bound is not the question; a SPATIAL one is.  The only READ bound on how a criterion depends on
      place is Z0's (alpha's) coupling to the gravitational potential, (c^2/alpha) d alpha / d Phi = 14(11)e-9
      (settle.H12, 2010.06620v2 Table II, READ by the board).  With the potential difference between Earth's surface
      and Proxima b's (compensate.eps_A / eps_B, imported): |Delta alpha / alpha| <= 25e-9 |Delta Phi| / c^2 at the
      1-sigma upper end of the READ value (the value itself is 1.3 sigma from zero).  M and R, readouts of alpha,
      inherit it.  For the other constants no READ spatial bound exists here: they are equal at A and B under
      H-UNIFORM-CONSTANTS (standard physics), not by a READ measurement.
  (3) WHAT 'LITERALLY QUANTUM-CORRELATED' CAN MEAN (H-12Q).  A criterion with a definite value at both seats is a product
      of definite values: its mutual information and its entanglement are 0 (computed); the two seats AGREE, which
      is classical equality, not entanglement.  CONTROL: a Bell pair has quantum mutual information 2 bits and
      entanglement entropy 1.  So H-12Q is non-trivial only for a criterion that is a quantum observable, uncertain at
      each seat -- a field-carried one, if the constant is itself a field (settle.H12's CONDITIONAL rows;
      H-CONSTANTS-ARE-FIELDS).  Fields' vacua ARE entangled between separated regions, but extractably only within
      limits: Reznik, 'Entanglement from the vacuum', quant-ph/0212044v2 (READ via alphaXiv): field correlations fall
      as 1/L^2 (p.2); the entanglement two inertial probes extract persists only for L/T < 1.1 (T their switching
      time; p.12) -- 'the probes must be "contained" in the space-like range of a single coherent vacuum fluctuation';
      beyond, it 'drops to zero while the classical type of correlations do not' (p.13).  Computed at the Proxima span:
      the least switching time is L / (1.1 c).
  (4) THE PREDETERMINATION TEST (M, item 23).  Compatibility is reconstructibility from B's stock (item 24).  The ten
      criteria tied to constants are the same at B (to the READ bound where one exists, under H-UNIFORM-CONSTANTS
      otherwise), so they decide nothing about one seat against another.  The two MATERIAL criteria are properties of
      the materials the object is made of; rebuilt from B's stock with the object's composition they equal A's
      (H-SAME-COMPOSITION, H-SAME-ISOTOPES).  So the twelve-criteria test at a seat reduces to the stock gate: computed
      from the starting state (the object's elements, seat.per_element_stock) against what the seat holds.  At
      Proxima it is OPEN: the binder P is measured nowhere in the system (seat.P_MEASURED_IN_PROXIMA_SYSTEM).

NAMED HYPOTHESES
  H-12Q                  (M, item 24) the twelve are literally quantum-correlated between the positions.
  H-UNIFORM-CONSTANTS    a constant with no READ spatial bound has the same value at A and B (standard physics).
  H-CONSTANTS-ARE-FIELDS a constant of nature is a dynamical field (settle.H12's CONDITIONAL rows); only then can it be
                         a quantum observable uncertain at each seat.
  H-REZNIK-WINDOW        Reznik's L/T < 1.1 is for one window function and gap (p.11-12, Figs. 1-2); another choice moves
                         the number, not the fact that extraction ends at finite L/T.
  H-SAME-COMPOSITION, H-SAME-ISOTOPES (step1b/balance.py).
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
REZNIK_2003 = {"source": "quant-ph/0212044v2", "route": "READ via alphaXiv (answer_pdf_queries), pp.1-13",
               "field_correlation_falloff": "1/L^2 (massless, 3+1 D; p.2)", "L_over_T_max": 1.1,
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
            "coef_1sigma_upper": coef, "value_over_sigma": ALPHA_PHI[0] / ALPHA_PHI[1]}


def differ_table():
    b = alpha_ab_bound()["max_abs_dalpha_over_alpha"]
    rows = []
    for r in settle.H12:
        k = kind(r[2])
        if r[0] == "Z0":
            st = "READ-bounded: |d alpha/alpha| <= %.2g between A and B" % b
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
    prod = np.kron([0, 1], [0, 1]).astype(complex)
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    return {"definite_classical_MI": mutual_info_classical(P_def), "definite_product_QMI_ent": quantum_mi_pure(prod),
            "bell_QMI_ent": quantum_mi_pure(bell)}


def reznik_min_switch_time():
    L = seat.D_PROXIMA
    T = L / (REZNIK_2003["L_over_T_max"] * C)
    return {"L_m": L, "T_min_s": T, "T_min_yr": T / seat.YEAR_S, "light_time_yr": L / C / seat.YEAR_S}


# ============================================================================ (4) the predetermination test
def predetermination(gate=None):
    k = kinds()
    gate = seat.P_MEASURED_IN_PROXIMA_SYSTEM if gate is None else gate
    binder = seat.binders()["CI chondrite"][0][0]
    return {"decide_nothing_between_seats": k["constant"] + k["emergent"], "decided_by_stock": k["material"],
            "reduces_to": "the stock gate (seat.per_element_stock against the seat's holdings)",
            "binder": binder, "binder_measured_at_proxima": gate,
            "verdict_at_proxima": "OPEN (the binder is measured nowhere in the system)" if not gate else "test"}


def collect():
    return {"kinds": kinds(), "alpha_ab": alpha_ab_bound(), "differ": differ_table(), "h12q": definite_vs_bell(),
            "reznik": reznik_min_switch_time(), "predetermination": predetermination(), "READ": [REZNIK_2003]}


def report():
    d = collect()
    print("W3B -- the twelve criteria at A and B (M-RULINGS items 23-24)")
    print('  M: "%s"' % M_WORDS_23)
    k = d["kinds"]
    print("\n(1) by kind (settle.H12's class column): constants %d %s; emergent %d %s; material %d %s"
          % (len(k["constant"]), k["constant"], len(k["emergent"]), k["emergent"], len(k["material"]), k["material"]))
    a = d["alpha_ab"]
    print("(2) A (Earth) against B (Proxima b): Delta Phi / c^2 from %.3g to %.3g; |Delta alpha / alpha| <= %.2g"
          % (a["dPhi_over_c2"][0], a["dPhi_over_c2"][1], a["max_abs_dalpha_over_alpha"]))
    for r in d["differ"]:
        print("    %-8s %-9s %s" % (r["symbol"], r["kind"], r["A_vs_B"]))
    h = d["h12q"]
    print("(3) H-12Q: a definite value at both seats -- classical MI %.1f, quantum MI and entanglement %s;"
          % (h["definite_classical_MI"], h["definite_product_QMI_ent"]))
    print("    CONTROL Bell pair -- quantum MI and entanglement %s" % (h["bell_QMI_ent"],))
    r = d["reznik"]
    print("    vacuum entanglement at the Proxima span (Reznik, READ): probes must stay switched on >= %.2f yr "
          "(light time %.2f yr)" % (r["T_min_yr"], r["light_time_yr"]))
    p = d["predetermination"]
    print("(4) predetermination: %d criteria decide nothing between seats; %s decided by the stock; it reduces to %s;"
          % (len(p["decide_nothing_between_seats"]), p["decided_by_stock"], p["reduces_to"]))
    print("    binder %s measured at Proxima: %s -> %s" % (p["binder"], p["binder_measured_at_proxima"],
                                                        p["verdict_at_proxima"]))


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
    chk("by settle.H12's own classes: 8 constants, 2 emergent (M, R), 2 material (K, T)",
        (len(k["constant"]), k["emergent"], k["material"]), (8, ["M", "R"], ["K", "T"]))
    chk("the alpha-potential coefficient used is settle.H12's Z0 row, read back ('14(11)e-9' in it)",
        "14(11)e-9" in alpha_row_bound_text(), True)
    a = alpha_ab_bound()
    chk("Delta Phi between Earth and Proxima b is of order 1e-8 c^2 (both ends of b's range, |.| in 1e-9..1e-7)",
        all(1e-9 < abs(x) < 1e-7 for x in a["dPhi_over_c2"]), True)
    chk("so alpha at B equals alpha at A to better than 1e-15 (READ coefficient x computed potential)",
        a["max_abs_dalpha_over_alpha"] < 1e-15, True)
    h = definite_vs_bell()
    chk("a definite value at both seats carries no mutual information and no entanglement",
        (h["definite_classical_MI"], h["definite_product_QMI_ent"]), (0.0, (0.0, 0.0)))
    chk("CONTROL: a Bell pair carries quantum MI 2 bits and entanglement 1 (to 1e-12)",
        (abs(h["bell_QMI_ent"][0] - 2) < 1e-12, abs(h["bell_QMI_ent"][1] - 1) < 1e-12), (True, True), ctl=True)
    r = reznik_min_switch_time()
    chk("Reznik's window at the Proxima span: switching time L/(1.1 c) is 1/1.1 of the light time (to 1e-12)",
        abs(r["T_min_yr"] * 1.1 / r["light_time_yr"] - 1) < 1e-12, True)
    p = predetermination()
    chk("ten criteria decide nothing between seats; the two material ones are decided by the stock",
        (len(p["decide_nothing_between_seats"]), p["decided_by_stock"]), (10, ["K", "T"]))
    chk("the predetermination at Proxima stays OPEN: the binder is P and P is unmeasured there",
        (p["binder"], p["binder_measured_at_proxima"]), ("P", False))
    chk("CONTROL: were P measured, the verdict would be a test, not OPEN (the logic turns on the measurement)",
        predetermination(gate=True)["verdict_at_proxima"], "test", ctl=True)
    structural.append("the material criteria equal A's when rebuilt from B's stock with the object's composition: "
                      "that is H-SAME-COMPOSITION / H-SAME-ISOTOPES, carried, not derived")
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
