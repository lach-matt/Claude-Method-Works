#!/usr/bin/env python3
"""
openterms.py -- Step 1b: pricing the balanced equation's three OPEN energy terms, as far as physics and the board allow.

Not seated.  Nothing here edits the board: figures are IMPORTED from their owners (balance, measure, massform, seat,
gravity, ledger); outside numbers are READ, with the route recorded.  M (2026-10-05): "Continue by necessity to the
current place of work" -- the current place is Step 1b, whose energy column balance.py refuses to total because three
terms are OPEN: reading I at A (IN-A-READ), retiring A's instance (OUT-A-RESIDUE, H-RETIRE-A, M item 32) and
assembling at B (IN-B-ASSEMBLE, E_rec).

    python3 openterms.py              report
    python3 openterms.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 openterms.py --json       the numbers as JSON

WHAT IT COMPUTES
  (T1) READING AT A.
       Theorem floor: 0.  Measurement can be done reversibly; only the logically irreversible step -- erasing the
       record -- has a Landauer price (Bennett, physics/0210005v2 p.1, READ by measure.py; its H-ERASE).  That price is
       already in the equation (OUT-A-RECORD / OUT-A-COPY).  So no theorem makes reading cost more than 0.
       Probe floor, under H-PROBE: to locate each atom to a pitch delta (measure.GRID_PITCHES) a probe of wavelength
       <= delta must reach it -- at least one quantum per atom (H-ONE-QUANTUM).  Per quantum: photon h c / delta;
       electron h^2 / (2 m_e delta^2); neutron h^2 / (2 m_n delta^2) (non-relativistic, checked).  Totals over the
       object's atoms (measure.atom_counts).
  (T2) RETIRING A'S INSTANCE (H-RETIRE-A).  A chemical rearrangement into stock.  Its SIGN depends on the stock's form
       (H-STOCK-FORM): retiring into oxidised stock releases energy, into free elements costs it.  Its SIZE is bounded:
       |E_chem| <= (v_max/2) D_max per atom (H-VALENCE, restated per atom: the atomisation energy per atom is at most
       v_max/2 x D_max = 33.5 eV; NAMED-NOT-READ -- literal bond counts exceed 6 for Ca in apatite or metals, but real
       atomisation and cohesive energies stay far below 33.5 eV per atom, so the per-atom ceiling holds; a difference
       between two neutral forms is bounded by the larger atomisation energy) and D_max the strongest bond in a neutral molecule, carbon monoxide's (READ,
       two values: 1077 kJ/mol = 11.16 eV, Wikipedia 'Bond dissociation energy', and 1072 kJ/mol, PMC4635358; both
       via Firecrawl search excerpts; the larger is used, so the bound is a ceiling either way).
       SUBSUMED (M, item 31), under H-PROBE and H-ABSORB: a photon or electron probe at atomic pitch carries more
       energy per quantum than D_max, and the read's total exceeds the whole chemical ceiling (4.5x to 3,700x) -- so if
       the read's quanta are absorbed in the object, the read supplies more than the energy to retire A: the retire
       cost is subsumed by a larger cost, not cancelled (the total is the larger of the two, and the excess leaves A as
       heat, balance.py OUT-A-HEAT).  CONSEQUENCE, computed: absorbed, the photon read at 1 A deposits ~1.9e11 Gy in
       70 kg -- the object is destroyed while it is being read, so the absorption that 'supplies' the retire also
       scrambles what is being read (H-READ-BEFORE-DAMAGE: the read completes before the damage scrambles it), and the
       plasma left is stock in neither H-STOCK-FORM form.  A neutron probe at 1 A carries less than D_max per quantum:
       not subsumed (CONTROL).  Near-field reads (scanning-probe microscopy, ~eV per quantum) evade H-PROBE's
       wavelength floor altogether (H-NEAR-FIELD).
  HISTORY: the first selftest asserted the ratio below 1e-4 at every beta; at beta 0.01 it is 1.14e-4 -- the guessed
  threshold failed, the finding did not; the check now asserts what is shown (below 1 at every beta) and prints it.
  HISTORY (Step 1b verifier, 2026-10-05): 'the retire term is dissolved by the read term' (subsumed, not cancelled;
  absorption destroys the object -- now computed and named); H-VALENCE stated per bond count (now per atom); the global
  cancellation counted as a check and printed STRUCTURAL (double count); the theorem floor and the None 'control' are
  literals (now STRUCTURAL).
  (T3) ASSEMBLING AT B (E_rec).  Its parts: (a) chemistry, inside [-ceiling, +ceiling] by H-STOCK-FORM at B; (b) B's
       register reset, already OUT-B-HEAT (H-RESET); (c) placement: no floor is established here (placement can in
       principle be reversible), so it stays OPEN.  The chemical ceiling is compared with seat.erec_ceiling -- the
       E_rec below which reconstruction from B's stock can ever pay back against shipping the payload at beta c.
       GLOBAL COMPENSATION (M, item 31): if A's residue and B's stock are in the same form, the chemistry at A and at B
       are the same rearrangement in opposite directions, and they cancel in the global column; LOCALLY A is left a
       surplus and B a deficit, which B's surroundings must supply (OPEN: the board holds no supply at B).

HISTORY: first written as step1b/terms.py (d79aa3b); renamed 2026-10-05 because the board already holds a terms.py,
which shadowed this file when bsupply.py imported it.  Nothing in it changed with the rename.

NAMED HYPOTHESES
  H-PROBE        locating an atom to delta needs a probe of wavelength <= delta (the diffraction scale).
  H-ONE-QUANTUM  one probe quantum per atom: a floor; scattering cross-sections make the real count larger.
  H-ABSORB       the probe's quanta are absorbed in the object (otherwise they pass, and deposit nothing).
  H-VALENCE      atomisation energy per atom <= (v_max/2) D_max, v_max = 6; NAMED-NOT-READ (per atom, not per bond).
  H-READ-BEFORE-DAMAGE the read completes before an absorbed probe's damage scrambles the configuration being read.
  H-NEAR-FIELD   scanning-probe reads at ~eV per quantum evade H-PROBE's wavelength floor.
  H-STOCK-FORM   the chemical form of A's residue and of B's stock; it sets the sign of T2 and T3(a).
  H-RETIRE-A     (M, item 32) carried as M's hypothesis.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
for _p in (os.path.join(WD, "docket68"), WD, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import balance
    import measure
    import massform
    import seat
    import gravity
    import ledger

H_PLANCK = gravity.H_PLANCK
M_E = gravity.M_E
M_N = ledger.M_NEUTRON_KG
EV = gravity.EV_J
C = seat.C
N_AVOGADRO = 6.02214076e23          # SI-exact (2019 definition)
V_MAX = 6                           # H-VALENCE, NAMED-NOT-READ

CO_BOND = {
    "values_kJ_mol": (1077.0, 1072.0), "value_eV_printed": 11.16,
    "sources": ("Wikipedia, 'Bond dissociation energy', table 'Representative bond enthalpies' (C≡O, 1077 kJ/mol, "
                "11.16 eV/bond, 'Strongest bond in neutral molecule')",
                "PMC4635358, 'Intriguing Electrostatic Potential of CO' ('The bond dissociation energy of CO (1072 "
                "kJ/mol) is the strongest chemical bond')"),
    "route": "READ via Firecrawl search excerpts (2026-10-05); the two disagree by 5 kJ/mol (0.5 %), a discrepancy "
             "recorded, not adjudicated; the larger is used for a ceiling",
}


def d_max_j():
    return max(CO_BOND["values_kJ_mol"]) * 1e3 / N_AVOGADRO


def atoms():
    N, _ = measure.atom_counts()
    return sum(N.values())


# ============================================================================ (T1) reading at A
def probe_quantum_j(delta, carrier):
    if carrier == "photon":
        return H_PLANCK * C / delta
    m = M_E if carrier == "electron" else M_N
    return H_PLANCK ** 2 / (2.0 * m * delta ** 2)


def nonrelativistic_ok(delta, carrier, frac=0.1):
    """The non-relativistic kinetic energy is below frac x rest energy (else the formula is not the floor)."""
    m = M_E if carrier == "electron" else M_N
    return probe_quantum_j(delta, carrier) < frac * m * C ** 2


def read_terms():
    n = atoms()
    rows = []
    for delta in measure.GRID_PITCHES:
        for car in ("photon", "electron", "neutron"):
            e = probe_quantum_j(delta, car)
            rows.append({"delta_m": delta, "carrier": car, "per_quantum_eV": e / EV, "total_J": n * e,
                         "exceeds_D_max": e > d_max_j(),
                         "nonrel_ok": True if car == "photon" else nonrelativistic_ok(delta, car)})
    return {"theorem_floor_J": 0.0, "atoms": n, "probe_floor": rows}


# ============================================================================ (T2) retiring A, and (T3) assembling at B
def chem_ceiling_j():
    """|E_chem| <= (v_max N_atoms / 2) D_max (H-VALENCE)."""
    return V_MAX * atoms() / 2.0 * d_max_j()


def retire_term():
    c = chem_ceiling_j()
    rt = read_terms()["probe_floor"]
    comp = [{"delta_m": r["delta_m"], "carrier": r["carrier"], "read_over_ceiling": r["total_J"] / c,
             "dissolves_retire": r["exceeds_D_max"] and r["total_J"] >= c,
             "dose_Gy_if_absorbed": r["total_J"] / measure.atom_counts()[1]} for r in rt]
    return {"range_J": (-c, c), "ceiling_J": c, "compensation_by_read": comp}


def assemble_term():
    c = chem_ceiling_j()
    ceil = seat.erec_ceiling()
    return {"chem_range_J": (-c, c), "reset_floor_J": [x[4] for x in balance.equation(balance.counts()[0][1],
                                                                                      "R-QUANTUM")
                                                       if x[0] == "OUT-B-HEAT"][0],
            "placement": "OPEN (no floor established here)",
            "erec_payback_ceiling_J": ceil, "chem_ceiling_over_payback": {b: c / v for b, v in ceil.items()}}


def global_chem(e_retire_a, same_form=True):
    """Chemistry at A (retire) and B (assemble): the same rearrangement reversed when the forms match."""
    e_assemble_b = -e_retire_a if same_form else None
    return {"A_J": e_retire_a, "B_J": e_assemble_b,
            "global_J": (e_retire_a + e_assemble_b) if same_form else None,
            "local_deficit_at_B_J": max(0.0, e_assemble_b) if same_form else None}


def collect():
    return {"D_max_J": d_max_j(), "D_max_eV": d_max_j() / EV, "CO_BOND": CO_BOND, "read": read_terms(),
            "retire": retire_term(), "assemble": assemble_term(),
            "global_example": global_chem(-chem_ceiling_j())}


def report():
    d = collect()
    print("Step 1b -- pricing the three OPEN energy terms")
    print("  D_max (CO, READ, the larger of two values) = %.4g J = %.3f eV; H-VALENCE v_max = %d" %
          (d["D_max_J"], d["D_max_eV"], V_MAX))
    r = d["read"]
    print("\n(T1) READING AT A: theorem floor %.0f J (reversible measurement; erasure already priced)" % r["theorem_floor_J"])
    print("     probe floor (H-PROBE, H-ONE-QUANTUM), %.4g atoms:" % r["atoms"])
    for x in r["probe_floor"]:
        print("       pitch %.0e m  %-8s %10.4g eV/quantum  total %.4g J  > D_max: %-5s  non-rel ok: %s"
              % (x["delta_m"], x["carrier"], x["per_quantum_eV"], x["total_J"], x["exceeds_D_max"], x["nonrel_ok"]))
    t = d["retire"]
    print("\n(T2) RETIRING A (H-RETIRE-A): chemistry within +-%.4g J (sign by H-STOCK-FORM)" % t["ceiling_J"])
    for x in t["compensation_by_read"]:
        print("       pitch %.0e m  %-8s read / chemical ceiling = %.4g  -> retire subsumed by the read (H-ABSORB): %-5s"
              " dose if absorbed %.3g Gy" % (x["delta_m"], x["carrier"], x["read_over_ceiling"], x["dissolves_retire"],
                                             x["dose_Gy_if_absorbed"]))
    a = d["assemble"]
    print("\n(T3) ASSEMBLING AT B (E_rec): chemistry within +-%.4g J; reset floor %.4g J (H-RESET); placement %s"
          % (a["chem_range_J"][1], a["reset_floor_J"], a["placement"]))
    for b, v in a["erec_payback_ceiling_J"].items():
        print("       payback ceiling at beta %.2f: %.4g J; chemical ceiling / it = %.3g"
              % (b, v, a["chem_ceiling_over_payback"][b]))
    g = d["global_example"]
    print("     global (same stock form): A %.4g J, B %.4g J, global %.4g J; B's local deficit %.4g J -- OPEN supply at B"
          % (g["A_J"], g["B_J"], g["global_J"], g["local_deficit_at_B_J"]))


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("openterms.py selftest")
    chk("D_max from 1077 kJ/mol reproduces Wikipedia's printed 11.16 eV to 0.01 eV",
        abs(1077e3 / N_AVOGADRO / EV - CO_BOND["value_eV_printed"]) < 0.01, True)
    chk("the ceiling uses the larger of the two READ values", d_max_j() == 1077e3 / N_AVOGADRO, True)
    chk("photon at 1 A: 12.40 keV per quantum (hc/lambda) to 0.01 keV",
        abs(probe_quantum_j(1e-10, "photon") / EV / 1e3 - 12.398) < 0.01, True)
    chk("electron at 1 A: 150.4 eV (h^2/2 m_e lambda^2) to 0.5 eV", abs(probe_quantum_j(1e-10, "electron") / EV - 150.4)
        < 0.5, True)
    chk("neutron at 1 A: 81.8 meV to 0.5 meV", abs(probe_quantum_j(1e-10, "neutron") / EV - 0.0818) < 5e-4, True)
    chk("every massive-probe row is non-relativistic (formula valid)",
        all(x["nonrel_ok"] for x in read_terms()["probe_floor"]), True)
    chk("photon and electron quanta exceed D_max at both pitches; the neutron at 1 A does not",
        [(x["carrier"], x["delta_m"], x["exceeds_D_max"]) for x in read_terms()["probe_floor"]
         if (x["carrier"], x["delta_m"]) in (("photon", 1e-10), ("electron", 1e-10), ("neutron", 1e-10))],
        [("photon", 1e-10, True), ("electron", 1e-10, True), ("neutron", 1e-10, False)])
    comp = {(x["carrier"], x["delta_m"]): x["dissolves_retire"] for x in retire_term()["compensation_by_read"]}
    chk("SUBSUMED: a photon read at 1 A exceeds the whole retire ceiling (read >= chemical ceiling, quantum > D_max)",
        comp[("photon", 1e-10)], True)
    chk("CONTROL: a neutron read at 1 A does not (quantum below D_max)", comp[("neutron", 1e-10)], False, ctl=True)
    _r = assemble_term()["chem_ceiling_over_payback"]
    chk("the chemical ceiling lies below the E_rec payback ceiling at every beta seat.py lists (largest ratio "
        "%.3g, at beta %.2f)" % (max(_r.values()), min(_r)), all(v < 1.0 for v in _r.values()), True)
    dose = {(x["carrier"], x["delta_m"]): x["dose_Gy_if_absorbed"] for x in retire_term()["compensation_by_read"]}
    chk("absorbed, the photon read at 1 A deposits ~1.9e11 Gy in the object (to 5%) -- the object is destroyed",
        abs(dose[("photon", 1e-10)] / 1.9e11 - 1) < 0.05, True)
    g = global_chem(-chem_ceiling_j())
    structural.append("theorem floor on reading %.0f J and the None returned for different stock forms are literals "
                      "of the code; B's local deficit equals the ceiling by construction (%s)"
                      % (read_terms()["theorem_floor_J"], abs(g["local_deficit_at_B_J"] - chem_ceiling_j()) < 1e-6))
    structural.append("the global cancellation for matching stock forms is built in (B's term is defined as A's "
                      "reversed): printed, not counted; what is computed is the ceiling and B's local deficit")
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
