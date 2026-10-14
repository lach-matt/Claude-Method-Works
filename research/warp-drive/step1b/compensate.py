#!/usr/bin/env python3
"""
compensate.py -- Step 1b, compensation in the balanced equation (M, rulings item 31).

Not seated.  Nothing here edits the board: board figures are IMPORTED from their owners (balance, measure, massform,
seat, settle, foliation, ladder, nopath); outside numbers are READ at source, with the route recorded beside each.

    python3 compensate.py              report
    python3 compensate.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 compensate.py --json       the numbers as JSON

M'S WORDS (docket68/M-RULINGS-2026-10-03.md item 31, verbatim)
  "Be sure to account for compensation in the physics.... Let's say mass energy density is different at the seat, but
  some other discrepancy makes up of that and dissolves the defect..."
Carried as H-COMPENSATION: a discrepancy in one term between the first and second positions may be dissolved by an
opposite discrepancy in another term, so the balance holds without each term matching on its own.

WHAT IT COMPUTES -- four places where the physics itself compensates, each tested, and the rule that bounds them
  (C1) FRAME.  The object's rest mass is the same at A and B (an invariant), but its energy in one common frame (the
       Sun's) is not: the specific energy  eps = v^2/2 + Phi  differs between Earth's surface and Proxima b's.  The
       defect m (eps_B - eps_A) is COMPUTED, as a range, in the Sun's frame (H-SUN-FRAME; Earth's rotation, about
       +-1.4e7 J/kg, under 1 % of the range, omitted: H-NO-ROTATION).  It is AVOIDED by B's stock -- nothing crosses,
       so there is no defect to compensate in any frame (avoidance, not an opposite discrepancy): the stock already moves with B
       and sits in B's potential, so an object built from it carries eps_B with no transfer term, and the frame column
       closes at zero (printed STRUCTURAL).  Illustration (not a control: it cannot fail): the same object SHIPPED from A
       must be supplied m (eps_B - eps_A).
       READ: Kervella, Thevenin & Lovis 2017 (arXiv:1611.03495v3, via alphaXiv): Proxima's heliocentric Galactic
       velocity (U, V, W) = (-29.390, +1.883, +13.777) km/s (Table B.1, p.6); alpha Cen A+B 2.0429 M_sun (Table 1,
       p.3) at 12 947 au from Proxima (p.3).  Proxima's mass and b's orbit and minimum mass: seat.FARIA_2022 (READ by
       the board).  b's radius range: seat.BRUGGER_2016 (READ by the board).
  (C2) NEGATIVE ENERGY AT THE SEAT: QUANTUM INTEREST.  If the seat's energy density is driven negative, the physics
       compensates it -- but never exactly.  Ford & Roman, "The quantum interest conjecture", gr-qc/9901074v1 (READ via
       alphaXiv): a negative pulse must be followed by a positive pulse that OVERcompensates by a fraction eps > 0
       (pp.9-10: exact compensation, eps = 0, admits no non-trivial pulse), within a maximum separation
       T_max = (pi/16)^(2/3) (A/|E|)^(1/3) ~ 0.338 (A/|E|)^(1/3) (eq. 29, p.8, 4D, compactly supported g of eq. 27);
       for small T, eps >= (4/27) (|E| T^3 / (C A))^2 (eq. 39, p.10, Lorentzian g; C = 3/(32 pi^2) in the earlier
       Ford-Roman bound, 27/(2048 pi^2) in Fewster-Eveson's, p.9).  COMPUTED here: eq. 39's limit re-derived by
       minimising F(alpha) = (1 + alpha^2)/(alpha^3 (1 - eps alpha^2)) numerically (eqs. 33-37); T_max and eps in SI
       for given |E| and A.  So M's compensation is what the physics does to a negative-energy defect; the defect is
       dissolved only by MORE positive energy, which is an input that must appear in output (item 29).
  (C3) THE VALUE ITSELF: REDUNDANCY.  The value is information (item 30).  A channel that flips each bit with
       probability p makes a defect in I(B); redundancy compensates it: Shannon's binary symmetric channel needs at
       least I / (1 - h2(p)) channel bits (capacity 1 - h2(p); h2 from measure.H).  The redundant bits are an input,
       discarded at B -- an output (kept, or erased with a Landauer floor, measure.landauer_j).
  (C4) WHAT CAN AND CANNOT COMPENSATE WHAT (computed, not declared).  Energy and bits DO compensate each other -- bits
       are not conserved: more power buys more bits through the channel (the board's LNM 1D law, seat.lnm_rate_1d:
       rate grows as sqrt(P)), so a bit-rate defect is dissolved by energy; and a bit of information about a system buys
       up to kT ln 2 of work (Szilard; Bennett and del Rio et al. READ by measure.py; measure.landauer_j).  A defect in
       baryon number, lepton number or charge at B cannot be dissolved by any energy term while those
       are conserved -- making baryons from energy makes antibaryons too (massform.pair_floor_j, a THEOREM on B and L
       conservation, imported).  At B such a defect is dissolved only by stock carrying that charge: D25's gate again.

NAMED HYPOTHESES
  H-COMPENSATION   (M, item 31) carried as M's hypothesis.
  H-NEWTON-FRAME   specific energy to first order (v << c, |Phi| << c^2); GR's exact Killing energy is not used.
  H-CIRCULAR       Earth's heliocentric speed taken as 2 pi AU / year (a circular orbit).
  H-R-EARTH        Earth's radius 6.371e6 m, NAMED-NOT-READ (the board holds no READ value); it sets Earth's own
                   surface potential and Brugger's radii (given in Earth radii).
  H-ORBIT-PHASE    the angle between Proxima's space velocity and b's orbital velocity is unknown: the full range is
                   carried; the planet's rotation is ignored.
  H-MSINI          b's mass is a MINIMUM (no transit); its potential magnitude is a floor, with no ceiling here.
  H-QI-SCOPE       quantum interest is proved for delta-function pulses of a massless scalar in flat 2D and 4D
                   spacetime (gr-qc/9901074v1 p.14); the seat is neither, so (C2) is the physics' compensation in that
                   scope, carried to the seat as a hypothesis.
  H-BSC            the channel's errors are independent bit flips at rate p.
  H-SUN-FRAME      (C1)'s energies are taken in the Sun's frame; the defect's size is frame-dependent.
  H-NO-ROTATION    Earth's rotation omitted from eps_A (under 1 % of the range).

HISTORY (corrected after the Step 1b verifier, 2026-10-05): C1 'DISSOLVED by B's stock' (avoided: nothing crosses) and
its shipped 'CONTROL' (cannot fail); C4 'compensation runs only within one conserved currency' (declared, and false for
bits and energy -- now computed); the from-stock residual counted as a check and printed STRUCTURAL (double count);
the T^6 and |E|^(-1/3) checks test the code's own formula (now STRUCTURAL); the 1 J over 1 m^2 quantum-interest example
lies far outside Ford-Roman's causal-contact condition A < T^2 (fn. 34, which the paper notes is sometimes imposed and
otherwise leaves A arbitrary) -- now printed beside it.
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
    import settle
    import foliation
    import ladder
    import nopath

M_WORDS_31 = ("Be sure to account for compensation in the physics.... Let's say mass energy density is different at "
              "the seat, but some other discrepancy makes up of that and dissolves the defect...")
G = foliation.G_NEWTON
M_SUN = foliation.M_SUN
AU = settle.AU_M
YEAR_S = seat.YEAR_S
M_EARTH = ladder.M_EARTH
D_PROX = seat.D_PROXIMA
C = nopath.C
HBAR = nopath.HBAR
R_EARTH = 6.371e6                      # H-R-EARTH, NAMED-NOT-READ
PAYLOAD = massform.PAYLOAD_KG

KERVELLA_2017 = {
    "source": "arXiv:1611.03495v3", "route": "READ via alphaXiv (answer_pdf_queries), Table B.1 p.6, Table 1 p.3, p.3",
    "UVW_proxima_kms": (-29.390, 1.883, 13.777), "UVW_sigma_kms": (0.027, 0.018, 0.009),
    "M_alphaCen_AB_sun": 2.0429, "d_alphaCen_proxima_au": 12947.0,
}
FORD_ROMAN_1999 = {
    "source": "gr-qc/9901074v1", "route": "READ via alphaXiv (answer_pdf_queries), pp.1, 7-10, 14-15",
    "Tmax_coef_4d": (math.pi / 16.0) ** (2.0 / 3.0), "Tmax_coef_printed": 0.338,
    "Tmax_coef_2d": math.pi / 24.0, "Tmax_coef_2d_printed": 0.131,
    "C_FR": 3.0 / (32.0 * math.pi ** 2), "C_FE": 27.0 / (2048.0 * math.pi ** 2),
    "eq39_coef": 4.0 / 27.0,
}


# ============================================================================ (C1) the frame
def eps_A():
    """Earth's surface, heliocentric: v^2/2 - G M_sun/AU - G M_E/R_E (H-CIRCULAR, H-R-EARTH)."""
    v = 2.0 * math.pi * AU / YEAR_S
    return {"v_ms": v, "kin": v * v / 2.0, "phi_sun": -G * M_SUN / AU, "phi_self": -G * M_EARTH / R_EARTH,
            "eps": v * v / 2.0 - G * M_SUN / AU - G * M_EARTH / R_EARTH}


def eps_B():
    """Proxima b's surface, heliocentric, as a range over H-ORBIT-PHASE and b's radius (H-MSINI: mass a minimum)."""
    f = seat.FARIA_2022
    vP = math.sqrt(sum((1e3 * u) ** 2 for u in KERVELLA_2017["UVW_proxima_kms"]))
    Mst = f["M_star_sun"][0] * M_SUN
    a_b = f["b_a_au"] * AU
    v_orb = math.sqrt(G * Mst / a_b)
    m_b = f["b_msini_earth"][0] * M_EARTH
    r_lo, r_hi = (r * R_EARTH for r in seat.BRUGGER_2016["radius_earth"])
    phi_common = (-G * M_SUN / D_PROX - G * Mst / a_b
                  - G * KERVELLA_2017["M_alphaCen_AB_sun"] * M_SUN / (KERVELLA_2017["d_alphaCen_proxima_au"] * AU))
    phi_self = (-G * m_b / r_lo, -G * m_b / r_hi)       # deepest, shallowest at the minimum mass
    kin = ((vP - v_orb) ** 2 / 2.0, (vP + v_orb) ** 2 / 2.0)
    return {"v_proxima_ms": vP, "v_orb_b_ms": v_orb, "kin_range": kin, "phi_common": phi_common,
            "phi_self_range_at_msini": phi_self,
            "eps_range": (kin[0] + phi_self[0] + phi_common, kin[1] + phi_self[1] + phi_common)}


def frame_defect(kg=PAYLOAD):
    a, b = eps_A(), eps_B()
    d = (kg * (b["eps_range"][0] - a["eps"]), kg * (b["eps_range"][1] - a["eps"]))
    return {"eps_A": a, "eps_B": b, "defect_J_range": d,
            "built_from_B_stock_transfer_J": 0.0,            # the stock already carries eps_B
            "shipped_from_A_must_supply_J_range": d}


def frame_column(defect_J, from_stock):
    """The frame column for one object: (defect at B, compensation, residual).  From B's stock the stock's own eps_B
    compensates exactly; shipped, nothing in the equation compensates it, so it stands as a term to supply."""
    comp = -defect_J if from_stock else 0.0
    return {"defect_J": defect_J, "compensation_J": comp, "residual_J": defect_J + comp}


# ============================================================================ (C2) quantum interest
def F_alpha(alpha, eps):
    return (1.0 + alpha ** 2) / (alpha ** 3 * (1.0 - eps * alpha ** 2))


def y_of_eps(eps, n=200000):
    """min over alpha in (0, 1/sqrt(eps)) of F(alpha) -- Ford-Roman eq. 36-37, computed by search (log grid + refine)."""
    hi = 1.0 / math.sqrt(eps)
    best, ab = float("inf"), None
    for i in range(1, n):
        a = hi * i / n
        v = F_alpha(a, eps)
        if v < best:
            best, ab = v, a
    return best, ab


def qi_si(E_J, A_m2, T_s=None, C=None):
    """T_max (eq. 29) and, for a separation T, the least overcompensation eps (eq. 39), in SI.
    Natural units hbar = c = 1: |E| -> E / (hbar c) [1/m], T -> c T [m]."""
    C = FORD_ROMAN_1999["C_FE"] if C is None else C
    E_nat = E_J / (HBAR * C_LIGHT())
    Tmax_m = FORD_ROMAN_1999["Tmax_coef_4d"] * (A_m2 / E_nat) ** (1.0 / 3.0)
    out = {"E_J": E_J, "A_m2": A_m2, "T_max_s": Tmax_m / C_LIGHT(), "C": C}
    if T_s is not None:
        T_m = C_LIGHT() * T_s
        out["T_s"] = T_s
        out["eps_min_small_T"] = FORD_ROMAN_1999["eq39_coef"] * (E_nat * T_m ** 3 / (C * A_m2)) ** 2
        out["positive_repayment_min_J"] = E_J * (1.0 + out["eps_min_small_T"])
    return out


def C_LIGHT():
    return C


# ============================================================================ (C3) redundancy in the value
def h2(p):
    return measure.H([p, 1.0 - p]) / measure.LN2 if 0.0 < p < 1.0 else 0.0


def redundancy(bits, p):
    """Least channel bits to carry `bits` over a BSC with flip rate p (H-BSC): bits / (1 - h2(p)).  None at p = 1/2."""
    cap = 1.0 - h2(p)
    if cap <= 0.0:
        return None
    sent = bits / cap
    return {"p": p, "capacity": cap, "sent": sent, "redundant": sent - bits,
            "erase_redundant_J_310K": measure.landauer_j(sent - bits, balance.T_A)}


# ============================================================================ (C4) what cannot compensate what
CURRENCIES = ("energy", "bits", "baryon", "lepton", "charge")


def energy_buys_bits(P1=1e3, P2=4e3):
    """seat.lnm_rate_1d (LNM eq. 8, one polarisation): bits/s at two powers -- more energy, more bits."""
    return seat.lnm_rate_1d(P1, pol=1), seat.lnm_rate_1d(P2, pol=1)


def bits_buy_energy(bits=1.0, T=300.0):
    """Szilard: up to kT ln 2 of work per bit about the system (measure.landauer_j)."""
    return measure.landauer_j(bits, T)


def can_compensate(defect, by):
    """Within a currency, always.  Energy <-> bits: yes, computed (energy_buys_bits, bits_buy_energy).  Baryon, lepton
    or charge: only by itself while conserved -- energy makes particle-antiparticle pairs (massform.pair_floor_j)."""
    if defect == by:
        return True
    if {defect, by} == {"energy", "bits"}:
        e1, e2 = energy_buys_bits()
        return e2 > e1 and bits_buy_energy() > 0
    return False


def baryon_from_energy_floor():
    """massform.pair_floor_j(): the least energy to make the payload from energy with B and L conserved -- it makes the
    antibaryons too, so a baryon defect is not dissolved by it: an equal and opposite one is created."""
    return massform.pair_floor_j(), massform.rest_energy_j()


def collect():
    sp = balance.counts()[0][1]
    return {"m_words_31": M_WORDS_31, "frame": frame_defect(),
            "frame_columns": {"from_B_stock": [frame_column(d, True) for d in frame_defect()["defect_J_range"]],
                              "shipped": [frame_column(d, False) for d in frame_defect()["defect_J_range"]]},
            "quantum_interest": {"y_check": y_of_eps(1e-4),
                                 "examples": [qi_si(1.0, 1.0, 1e-19), qi_si(massform.rest_energy_j(), 1.0)]},
            "redundancy": [redundancy(sp, p) for p in (1e-6, 1e-3, 0.11, 0.5)],
            "currency_matrix": {d: {b: can_compensate(d, b) for b in CURRENCIES} for d in CURRENCIES},
            "pair_floor_J_vs_rest_J": baryon_from_energy_floor(),
            "READ": [KERVELLA_2017, {k: v for k, v in FORD_ROMAN_1999.items() if k in ("source", "route")}]}


def report():
    d = collect()
    print("Step 1b -- compensation (M, item 31)")
    print('  M: "%s"\n' % M_WORDS_31)
    f = d["frame"]
    print("(C1) FRAME: rest mass invariant; energy in the Sun's frame is not (H-NEWTON-FRAME)")
    print("    A, Earth's surface: v %.4g m/s, eps %.6g J/kg" % (f["eps_A"]["v_ms"], f["eps_A"]["eps"]))
    print("    B, Proxima b: Proxima's space velocity %.4g m/s (Kervella 2017 Table B.1), b's orbital %.4g m/s; eps from "
          "%.6g to %.6g J/kg (H-ORBIT-PHASE, H-MSINI)" % (f["eps_B"]["v_proxima_ms"], f["eps_B"]["v_orb_b_ms"],
                                                      *f["eps_B"]["eps_range"]))
    print("    defect for %.0f kg: %.4g to %.4g J" % (PAYLOAD, *f["defect_J_range"]))
    print("    built from B's stock: residual %s J -- AVOIDED (nothing crosses; the stock already carries eps_B)"
          % [c["residual_J"] for c in d["frame_columns"]["from_B_stock"]])
    print("    illustration, shipped from A: residual %s J" % ["%.4g" % c["residual_J"]
                                                           for c in d["frame_columns"]["shipped"]])
    q = d["quantum_interest"]
    print("\n(C2) NEGATIVE ENERGY AT THE SEAT: quantum interest (Ford & Roman gr-qc/9901074v1; H-QI-SCOPE)")
    print("    eq. 39 re-derived: min F at eps = 1e-4 is %.6f; (3 sqrt3 / 2) sqrt(eps) = %.6f"
          % (q["y_check"][0], 1.5 * math.sqrt(3) * math.sqrt(1e-4)))
    for e in q["examples"]:
        s = "    |E| %.3g J over A %.3g m^2: repayment must arrive within T_max %.3g s" % (e["E_J"], e["A_m2"], e["T_max_s"])
        if "eps_min_small_T" in e:
            s += "; at T = %.3g s it overcompensates by at least eps = %.3g" % (e["T_s"], e["eps_min_small_T"])
        print(s)
    ex = q["examples"][0]
    print("    the 1 J over 1 m^2 example: c T_max = %.3g m against sqrt(A) = 1 m -- far outside the causal-contact "
          "condition A < T^2 (fn. 34; the paper otherwise leaves A arbitrary)" % (C * ex["T_max_s"]))
    print("    exact compensation (eps = 0) admits no non-trivial pulse (pp.9-10): the defect is dissolved only by MORE")
    print("    positive energy -- an input, accounted for in output (item 29)")
    print("\n(C3) THE VALUE: redundancy over a noisy channel (species-sequence count; H-BSC)")
    for r in d["redundancy"]:
        if r is None:
            print("    p = 0.5: capacity 0 -- no redundancy compensates")
        else:
            print("    p = %-6g capacity %.6f: send %.4g bits, %.4g redundant, erasure floor %.3g J at 310 K"
                  % (r["p"], r["capacity"], r["sent"], r["redundant"], r["erase_redundant_J_310K"]))
    e1, e2 = energy_buys_bits()
    print("\n(C4) WHAT CAN AND CANNOT COMPENSATE WHAT (computed):")
    print("    energy -> bits: LNM 1D rate %.3g bits/s at 1 kW, %.3g at 4 kW; bits -> energy: %.3g J per bit at 300 K"
          % (e1, e2, bits_buy_energy()))
    for k, v in d["currency_matrix"].items():
        print("    %-7s defect dissolved by: %s" % (k, [b for b, ok in v.items() if ok]))
    pf, rest = d["pair_floor_J_vs_rest_J"]
    print("    energy -> baryons makes antibaryons too: massform.pair_floor_j %.4g J = %.5f x Mc^2 -- not a dissolution"
          % (pf, pf / rest))


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

    print("compensate.py selftest")
    txt = " ".join(open(balance.RULINGS_FILE, encoding="utf-8").read().split())
    chk("M's words, item 31, found verbatim in the rulings file", M_WORDS_31 in txt, True)
    a, b = eps_A(), eps_B()
    chk("Earth's heliocentric speed 2 pi AU / yr lies within 29.7-29.9 km/s (H-CIRCULAR; a sanity bound)",
        29.7e3 < a["v_ms"] < 29.9e3, True)
    chk("Proxima's space speed from Kervella's (U,V,W) is 32.5 km/s to 0.1 km/s (READ, recomputed)",
        abs(b["v_proxima_ms"] - 32.51e3) < 100, True)
    chk("b's orbital speed sqrt(G M*/a) lies within 40-55 km/s (from seat.FARIA_2022's READ M* and a)",
        40e3 < b["v_orb_b_ms"] < 55e3, True)
    fd = frame_defect()
    chk("the frame defect is nonzero at both ends of its range", all(abs(x) > 0 for x in fd["defect_J_range"]), True)
    chk("Ford-Roman eq. 29's coefficient (pi/16)^(2/3) reproduces the printed 0.338; eq. 28's pi/24 the printed 0.131",
        (round(FORD_ROMAN_1999["Tmax_coef_4d"], 3), round(FORD_ROMAN_1999["Tmax_coef_2d"], 3)), (0.338, 0.131))
    chk("Fewster-Eveson's C is 9/64 of Ford-Roman's (p.9: 'the resulting bound is 9/64 of that in Eq.(1)')",
        abs(FORD_ROMAN_1999["C_FE"] / FORD_ROMAN_1999["C_FR"] - 9.0 / 64.0) < 1e-15, True)
    for e in (1e-3, 1e-5):
        y, _ = y_of_eps(e)
        chk("eq. 39 re-derived: min F(alpha) at eps = %g within 1%% of (3 sqrt3/2) sqrt(eps)" % e,
            abs(y / (1.5 * math.sqrt(3.0 * e)) - 1.0) < 0.01, True)
    chk("CONTROL: at eps -> 0 (exact compensation) F has no positive minimum -- F(alpha) -> 0 as alpha grows",
        F_alpha(1e4, 0.0) < 1e-3, True, ctl=True)
    structural.append("the quantum-interest scalings (eps ~ T^6 at small T; T_max ~ |E|^(-1/3)) are the formulas as "
                      "written, evaluated")
    sp = balance.counts()[0][1]
    r = redundancy(sp, 0.11)
    chk("redundancy at p = 0.11: capacity 1 - h2(0.11) ~ 0.5 (within 0.001), sent ~ 2x", (abs(r["capacity"] - 0.5) < 1e-3,
        abs(r["sent"] / sp - 1 / r["capacity"]) < 1e-12), (True, True))
    chk("CONTROL: at p = 1/2 no redundancy compensates (capacity 0)", redundancy(sp, 0.5), None, ctl=True)
    chk("energy and bits compensate each other (computed: more power, more bits; a bit buys kT ln 2 of work)",
        (can_compensate("bits", "energy"), can_compensate("energy", "bits")), (True, True))
    chk("energy cannot dissolve baryon, lepton or charge defects while those are conserved",
        [can_compensate(x, "energy") for x in ("baryon", "lepton", "charge")], [False, False, False])
    pf, rest = baryon_from_energy_floor()
    chk("making the payload's baryons from energy costs > 1.99 Mc^2 (massform.pair_floor_j: antibaryons too)",
        pf / rest > 1.99, True)
    structural.append("the from-stock frame residual is 0 by construction (nothing crosses); the shipped residual equals "
                      "the defect by construction; what is computed is the defect's size")
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
