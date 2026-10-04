#!/usr/bin/env python3
"""
throatbits.py -- DOCKET 66, wave 1, work item A2-throatbits: H-THROAT-BITS made quantitative, without presuming it.

Not seated.  Nothing here edits the board.  Every board figure is IMPORTED from the instrument that owns it --
docket68/measure.py (the payload's information under named counts), docket68/geometry.py (qnec_price, r_quantum,
shape_checks and the D68 grades GRADES, which itself imports docket68/nullinfo.py), ../nopath.py (holographic_bits,
bekenstein_bits, constants), ../wormhole.py (throat_mass), ../throatmass.py (LARGEST_THROAT_M), ../massform.py
(PAYLOAD_KG, rest_energy_j), ../specthm.py (the seat and throat class verdicts, derived by z3 at run time) and
../ledger.py (M's ruling M-S1A-P3, read as text) -- never retyped.  M's hypothesis is read from CHARTER.md.

    python3 throatbits.py              report
    python3 throatbits.py --selftest   counted checks, with CONTROLS (cases built to fail, which must fail);
                                       checks that cannot fail are printed STRUCTURAL and are not counted
    python3 throatbits.py --json       the report's numbers and grades as JSON

M, verbatim (ledger M-S1A-P3, CHARTER.md): "Singular occurs in the throat where the geometry is compressed to binary
information, and then push to the seat".  Carried as H-THROAT-BITS, a hypothesis, never a result.  M's ruling is
APPLIED: a singular throat is not disqualified (the closed-causal-curve / Borde disqualifier binds at the seat only).

WHAT IT COMPUTES
  (A) the information defining the payload: measure.price_table()'s four counts (9.5e27 .. 1.1e29 bits for 70 kg),
      each under its named hypotheses; the spread is H-ALT made visible (measure.py's own words);
  (B) the holographic capacity of a throat sphere of radius r, A/(4 l_P^2 ln 2) bits (nopath.holographic_bits), and
      the radius r_fit(I) at which a count I fits -- solved by bisection on the owner's function and checked against
      the closed form l_P sqrt(I ln2/pi); the Bekenstein radius of the payload at its own Mc^2; the saturation
      identity (the two bounds meet only at Schwarzschild saturation -- nopath.bekenstein_bits' own correction):
      at r_fit the least energy Bekenstein allows a holder of I bits is r_fit c^4/(2G), so M_sat = r_fit c^2/(2G);
  (C) the QNEC price of a throat of radius r in bits (geometry.qnec_price, nullinfo's expression), and the R-QUANTUM
      fraction at r_fit (geometry.r_quantum);
  (D) the singular throat in GR, READ at source: Poisson & Visser, gr-qc/9506083v1 (thin-shell wormholes).  From
      their eqs (11)-(12), (18)-(19), (29), (33)-(34): energy conservation (13) re-derived; sigma_0 < 0 for every
      a_0 > 2M; the shell's NEC sign; the shell mass; the stability region and PV's 'always unstable' for
      0 < beta_0^2 <= 1, reproduced on a grid;
  (E) the precise counterparts of 'compressed to binary information' READ at source: Bekenstein-Hawking / generalized
      entropy and the central dogma, the bag-of-gold neck and the island formula (Almheiri-Hartman-Maldacena-
      Shaghoulian-Tajdini 2006.06872v1); traversable-wormhole teleportation (Gao-Jafferis-Wall 1608.05687v3;
      Maldacena-Stanford-Yang 1704.05333v1);
  (F) grades of H-THROAT-BITS per D68 obstruction (O-BITS, O-MAKE-TOPO, O-MAKE-DIST, O-HOLD, O-SEAT, O-LOOP) in five
      readings, in docket68/B-combine.md's vocabulary (REMOVED / REMOVED-IF / NOT-BOUND-IF / OPEN / LEFT / SILENT,
      and LEFT-IF as D68 uses it), and against the seat's own conditions (specthm's seating classes, the Sturm
      condition, M-S1A-P3 (i)).  A theorem that does not bind gives NOT-BOUND-IF, never REMOVED.

NAMED HYPOTHESES (every limitation carried by name; the D68 names imported are used in D68's sense)
  H-ALT, H-LISTED, H-GRID, H-RHO, H-THERMO, H-FAITHFUL   measure.py's, carried with each count.
  H-CAP-AT-THROAT   the A/4 capacity applies to a throat sphere.  Bousso's covariant bound (board: NARROWED) caps a
                    LIGHT-SHEET (expansion <= 0); geometry.shape_checks computes that a flare-out throat has theta = 0
                    at r0 and theta > 0 on both sides, so no light-sheet leaves the throat sphere: Bousso gives no cap
                    there.  The READ route to a cap at a neck is H-NECK-DOGMA.
  H-NECK-DOGMA      the central dogma (2006.06872 p.13: degrees of freedom = Area/4G_N; "an unproven assumption",
                    p.14) applied to a neck: Wheeler's bag of gold (p.33-34) -- the exterior's fine-grained entropy is
                    set by the neck's area.  READ for a neck that evolves into a black hole, not for a held throat.
  H-COUNT-IS-ENTROPY the payload's defining information (a count of distinguishable alternatives) is what a capacity
                    bound on ENTROPY constrains.  A capacity is a ceiling; it does not show an encoding exists.
  H-BEK-SCOPE       Bekenstein's bound holds for complete, weakly self-gravitating systems (board: NARROWED); at
                    saturation (r_fit) the holder is not weakly self-gravitating -- the identity is the meeting point
                    of two bounds, not Bekenstein in scope.
  H-QNEC-OUT-OF-SCOPE, H-CONST   geometry.qnec_price's (QNEC carried to a throat with dynamical gravity; S''/A constant
                    over a null run of length r0 from S' = 0).
  H_flat, H-PATH, H-MIN-SCALAR   geometry.r_quantum's (D68 R-QUANTUM).
  H-SINGULAR-IS-THINSHELL   'singular throat' read as Poisson-Visser's: the Einstein tensor is a Dirac distribution on
                    the throat (PV p.1), the manifold geodesically complete.  The other GR reading -- a curvature
                    singularity with incomplete geodesics (the Einstein-Rosen bridge pinching off) -- is H-SINGULAR-
                    IS-PINCH, where nothing crosses as matter.
  H-PV-STATIC       PV's linear radial stability about an assumed static solution (their sec. III), M the same on
                    both sides (their eqs (1)-(2)).
  H-GJW-COUNTERPART 'compressed to binary information, then pushed' read as traversable-wormhole teleportation
                    (GJW sec. 5; MSY sec. 2, 4.1): prior entanglement (a TFD bridge) plus a coupling carrying a few
                    bits.  H-ADS-TFD: GJW's and MSY's setting (two AdS boundaries, the thermofield double).
                    H-COUPLED: the boundary coupling is on (GJW eq.(1.2)); it is a channel between the two sides.
  N_GJW-PAYLOAD     OPEN pathway (D66-fix): a one-space traversable throat that admits the payload, outside MMP's
                    family with the SM's fields.  Wave 1 carried N_GJW-AMBIENT, GJW p.14's same-space version, 'stated,
                    not computed'; MMP 1807.04726 (READ) realises that version at sub-electroweak scale, and mmp_scales
                    computes why it does not admit the payload (binding energy below the payload's rest energy at every
                    r_e above l_P with N_f = 54).
  H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, H-MQ-LARGE-N   Maldacena-Qi's premises (READ): nearly-AdS2 (JT) gravity; the
                    two-boundary coupling on for all time; many bulk fields in the coupling (or Delta < 1/2 with
                    alternate boundary conditions for a few, p.19).
  H-MMP             MMP's construction: Einstein-Maxwell with massless charged fermions, a pair of near-extremal
                    magnetically charged black holes (q >> 1), mouths held apart by rotation, d_min (6.52) << d <<
                    q^(5/2) l_p (5.49).  H-SM-FIELDS: the SM's fields (N_f = 54, d << 1/TeV, MMP pp.25-26).
                    H-MMP-G: the hypercharge coupling 0.36 .. 0.46 (MMP's normalisation g = g'/6).  H-MMP-OOM: the
                    order-of-magnitude reading of (6.51)-(6.52) (O(1) factors as printed; Omega l = 1 at the edge).
  H-ISLAND-COUNTERPART 'compressed to binary information' read as the island formula's area term (2006.06872 eq.(8.2)).
  H-ITB             D68's ITB (H-IT as an information layer beneath geometry, no READ realisation) with N_QTOPO.
  H-SEAT-OFF-THROAT the seat is not on the throat: the throat's singular support and the seat are disjoint.
  H-INFO-SHAPE, N_S5, H-SEAT-S5   D68's (M's rulings items 1, 5, 7).

D66-FIX (2026-10-04): every problem in the three wave-1 verifier reports is resolved here or answered with a reason:
R-TELEPORT's O-HOLD re-graded (GJW alone gives an opening, not a hold; MQ and MMP READ for held throats, each with its
premises); N_GJW-AMBIENT replaced by what MMP shows (mmp_scales); M's ruling applied to the bridge's creation; the
'precise size' and 'costs GR nothing' sentences re-worded; the attribution inside a setting stated (setting_removals);
MMP's SM-embedded throat added beside the board's 300 l_P one.  HISTORY keeps what wave 1 first said.

stdlib + sympy (+ numpy, z3 via the imported owners).
"""
import contextlib
import io
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
D68 = os.path.join(WD, "docket68")
for p in (D68, WD):
    if p not in sys.path:
        sys.path.insert(0, p)

LN2 = math.log(2.0)


def _quiet_import(name):
    if name in sys.modules:
        return sys.modules[name]
    with contextlib.redirect_stdout(io.StringIO()):
        mod = __import__(name)
    return mod


measure = _quiet_import("measure")
geometry = _quiet_import("geometry")
nopath = _quiet_import("nopath")
wormhole = _quiet_import("wormhole")
throatmass = _quiet_import("throatmass")
massform = _quiet_import("massform")

HBAR, C, G = nopath.HBAR, nopath.C, nopath.G

# ===================================================================================================== sources READ
# Every outside reading of THIS work item, with its route.  Short phrases only (page given); copyrighted text stays out.
ROUTE = "alphaXiv answer_pdf_queries (open arXiv full text, page-tagged), 2026-10-04; no paywall or login wall met"
READ = [
    {"key": "gr-qc/9506083v1", "who": "E. Poisson & M. Visser, 'Thin-shell wormholes: Linearization stability' (1995)",
     "route": ROUTE, "status": "READ (all 4 pages)", "board": "D67 VERIFIED-GRADES: STANDS",
     "used": ["p.1: cut-and-paste of two Schwarzschild copies at r = a > 2M; the manifold 'is geodesically complete'",
              "p.1: at the throat the Einstein tensor 'is formally singular' -- 'a Dirac distribution'",
              "p.2 eqs (11)-(12) sigma, p; (13) conservation; (14)-(17) V(a); (18)-(19) static sigma_0, p_0",
              "p.3 eq (29) 'stable if and only if'; (33)-(34) the boundary roots a_0^+-; (35)-(36) regions I, II",
              "p.3: for beta_0 in the standard range, thin-shell wormholes 'are always unstable'",
              "p.3: 'the surface energy density sigma_0 is negative' (exotic matter)"]},
    {"key": "1608.05687v3", "who": "P. Gao, D. L. Jafferis & A. C. Wall, 'Traversable Wormholes via a Double Trace "
                                   "Deformation' (2016; v3 2019)",
     "route": ROUTE, "status": "READ (pp.1-5, 10, 12-15, 18, 20 returned)", "board": "new to the board",
     "used": ["p.1 abstract: the boundary coupling gives negative average null energy; 'it cannot be used to violate "
              "causality'",
              "p.2: ANEC violation is 'a prerequisite for all traversable wormholes'",
              "p.4: with decoupled Hamiltonians 'no signal can be transmitted between the boundaries through the bulk'",
              "p.12 eq (5.1): the opening Delta V ~ h G_N / R^(D-2); p.13: open 'only ... for a small proper time'",
              "p.12: the bridge becomes 'slightly traversable' (re-read at D66-fix)",
              "p.15: the traversable window is 'just enough to let the single qubit Q pass through'",
              "p.13: the coupling 'fixes the relative time coordinate', excluding closed timelike curves",
              "p.13 fn.8: a limit on the information through the wormhole is presumed, not determined",
              "p.14: such wormholes 'do not enable one to travel faster than light over long distances'",
              "p.14: same-space version stated (coupling via the ambient spacetime, a Casimir effect) -- not computed",
              "p.14-15: the qubit is sent 'via the entanglement'; analogy to teleportation with classical bits"]},
    {"key": "1704.05333v1", "who": "J. Maldacena, D. Stanford & Z. Yang, 'Diving into traversable wormholes' (2017)",
     "route": ROUTE, "status": "READ (pp.1-4, 13-14, 22-24, 29, 36-37, 48-50 returned)", "board": "new to the board",
     "used": ["p.2: traversable wormholes are forbidden in GR -- no signal through faster than through the outside",
              "p.2: 'a few seemingly uninformative bits' plus prior entanglement transport information",
              "p.12 eq (2.21): g <~ N_bits (bits exchanged to open the wormhole); p.13 eq (2.25): N_send <~ g",
              "p.13: parametric only -- 'one would like to reproduce' that one qubit needs two classical bits",
              "p.22-23: the protocol is teleportation; the teleportee feels nothing special",
              "p.47 eq (D.92): classical-information Hayden-Preskill needs slightly more than twice the qubits"]},
    {"key": "1804.00491v3", "who": "J. Maldacena & X.-L. Qi, 'Eternal traversable wormhole' (2018)",
     "route": ROUTE + "; read at D66-fix", "status": "READ (pp.1-4, 6, 8, 19-20, 23-25, 27-28, 52-53 returned)",
     "board": "new to the board (V66-0 read it first)",
     "used": ["abstract: a nearly-AdS2 solution describing an eternal traversable wormhole",
              "p.2: negative null energy from quantum fields under an external coupling of the two boundaries",
              "p.2: a large number of quantum fields is needed; the wormhole is static and time independent",
              "p.19: with few fields in the coupling a classical wormhole needs Delta < 1/2, alternate boundary "
              "conditions",
              "p.18: at Delta = 1/2 no bound state for eta N < 1/2",
              "p.52: no causality violation, since direct interactions between the two sides are added",
              "p.52 Fig.23: two near-extremal black holes in one ambient space, a sketch",
              "p.52: challenges -- mutual attraction, gravitational-wave emission, large N, alternate boundary "
              "conditions"]},
    {"key": "1807.04726v3", "who": "J. Maldacena, A. Milekhin & F. Popov, 'Traversable wormholes in four dimensions' "
                                   "(2018; v3 2020)",
     "route": ROUTE + "; read at D66-fix", "status": "READ (pp.1-2, 4-7, 13, 16-29 returned)",
     "board": "READ by the board's D67 audits (_mk_1608.05687.py); re-read here (V66-1)",
     "used": ["abstract: a wormhole in four dimensions, Einstein-Maxwell plus charged massless fermions",
              "abstract: a long wormhole that does not lead to causality violations in the ambient space",
              "abstract: embeddable in the Standard Model with size small against the electroweak scale",
              "p.4: the mouth interaction is generated automatically by exchange of massless bulk fields",
              "eq.(2.3) r_e^2 = pi q^2 l_p^2/g^2; eq.(5.31), (7.58) throat length and binding energy",
              "eq.(6.50) Omega = 2 sqrt(r_e/d^3); (6.51) Omega l << 1; (6.52) lower bound on d; (5.49) upper",
              "p.18: too much energy sent in makes a near-extremal black hole; 'not safe for human travelers'",
              "p.20: pi l > d -- longer through the wormhole than through the ambient space",
              "p.26: SM effective N_f = 54; p.27: metastable, not completely stable"]},
    {"key": "2006.06872v1", "who": "A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian & A. Tajdini, 'The entropy "
                                   "of Hawking radiation' (2020, review)",
     "route": ROUTE, "status": "READ (pp.1-5, 9, 13-14, 16-17, 19, 21-22, 24, 26-31, 33-34, 37-39, 41-42 returned)",
     "board": "new to the board",
     "used": ["p.5 eq (2.4): S_gen = Area/(4 hbar G_N) + S_outside; Planck units l_p^2 = hbar G_N",
              "p.13: central dogma -- a black hole from outside is a quantum system with Area/(4G_N) degrees of "
              "freedom; p.14: 'an unproven assumption'",
              "p.27 eq (8.2): the island formula; p.38: it gives the entropy, not the state",
              "p.33: reconstruction from radiation is 'exceedingly complex' (roughly exponential in S_BH)",
              "p.33-34: Wheeler's bag of gold -- a narrow neck; the exterior's fine-grained entropy is the neck's area",
              "p.37: replica wormholes are Euclidean saddles computing Tr rho^n"]},
]

HISTORY = [
    ("R-TELEPORT O-HOLD", "REMOVED-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} in GJW's setting",
     "LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone; held throats READ in MQ (nearly-AdS2) "
     "and MMP (one space, sub-electroweak), each REMOVED-IF its own premises outside the board's setting", "V66-0 #1"),
    ("N_GJW-AMBIENT", "GJW p.14's same-space version, stated, not computed",
     "MMP realises it at sub-electroweak scale; for the payload LEFT-IF {H-MMP, H-SM-FIELDS}, OPEN via N_GJW-PAYLOAD "
     "outside that family (mmp_scales)", "V66-1 #2"),
    ("R-TELEPORT O-MAKE-TOPO", "NOT-BOUND-IF {H-ER=EPR} only",
     "and without ITE OPEN via W-create-ncc, M's ruling M-S1A-P3 applied", "V66-1 #1, applied consistently"),
    ("R-HOLO what it does", "gives M's mechanism a precise size",
     "r_fit is where the A/4 ceiling equals the count, IF {H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY}; no "
     "encoding at that density is constructed or READ", "V66-0 #4"),
    ("R-THINSHELL what it does", "M's ruling costs GR nothing",
     "under H-SINGULAR-IS-THINSHELL it costs GR no new structure, and still needs sigma_0 < 0; under "
     "H-SINGULAR-IS-PINCH not modelled", "V66-0 #5"),
    ("R-ISLAND what it does", "a precise sense in which geometry is compressed to binary information",
     "the area term counts fine-grained entropy, not a state or an encoding", "V66-0 #4"),
    ("member-attributed removals", "none -- credited to the premise set, not to H-THROAT-BITS",
     "none in the board's setting; inside MQ's and MMP's settings H-GJW-COUNTERPART, M's reading, is load-bearing",
     "V66-1 #8"),
    ("largest held throat", "the board's 300 l_P throat (4.08e5 bits): payload 2.3e22 .. 2.7e23 x",
     "beside it MMP's SM-embedded throat (~2.5e19 bits on V66-1's estimate): payload ~4e8 .. 4e9 x", "V66-1 #6"),
]

BOARD_READ = [  # readings this work item USES but did not make: the board's, with the owner that records them
    ("hep-th/9905177 Bousso covariant bound", "D67 NARROWED; docket68/CHARTER.md (A(B)/4 on a light-sheet)"),
    ("1509.02542 QNEC (BFKLW)", "D67 NARROWED; geometry.qnec_price (H-QNEC-OUT-OF-SCOPE)"),
    ("quant-ph/9904023 BSST p.3 FCCC >= C_E", "measure.py H-FAITHFUL (2 classical bits per qubit)"),
    ("1306.0533v2 Maldacena-Susskind fn.1, sec.3.2", "geometry.GRADES (ITE row), M-RULINGS item 14"),
    ("quant-ph/0404042 Bekenstein eq.(1)", "measure.py (BEKENSTEIN), D67 NARROWED"),
]


# ================================================================================================= (A) the payload
def payload_counts():
    rows, geo, ceilings, ob = measure.price_table()
    out = []
    for r in rows:
        out.append({"count": r["count"], "bits": r["bits"],
                    "classical_bits_if_teleported_as_qubits": r["classical_bits_to_teleport_if_qubits"]})
    return {"counts": out, "atoms": ob["atoms"], "payload_kg": massform.PAYLOAD_KG,
            "rest_energy_J": massform.rest_energy_j(), "ceilings": ceilings,
            "hypotheses": ["H-ALT", "H-LISTED", "H-GRID", "H-RHO", "H-THERMO", "H-FAITHFUL (classical column)"]}


def a3_printed():
    """The species and 0.1 A grid counts as A3-measure.md PRINTS them (read from the file, for reproduction)."""
    txt = open(os.path.join(D68, "A3-measure.md"), encoding="utf-8").read()
    sp_ = re.search(r"\| species sequence \(H-LISTED\) \| ([0-9.e+]+) \|", txt)
    gr_ = re.search(r"\| grid at 0\.1 Å \(H-GRID, H-RHO\) \| ([0-9.e+]+) \|", txt)
    return float(sp_.group(1)), float(gr_.group(1))


# ================================================================================================ (B) the capacity
def lp():
    return math.sqrt(nopath.planck_length_squared())


def r_fit(bits, cap=None):
    """Radius whose sphere's capacity cap(r) equals `bits`; bisection in log r on the owner's monotone function."""
    cap = cap or nopath.holographic_bits
    lo, hi = 1e-40, 1e10
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if cap(mid) < bits:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def r_fit_closed(bits):
    """Independent route: A/(4 l_P^2 ln2) = I  =>  r = l_P sqrt(I ln2 / pi)."""
    return lp() * math.sqrt(bits * LN2 / math.pi)


def r_bekenstein(bits, E):
    """Least radius at which Bekenstein (nopath.bekenstein_bits, linear in R) admits `bits` at energy E."""
    return bits / nopath.bekenstein_bits(1.0, E)


def saturation_identity_symbolic(drop_ln2=False):
    """sympy: Bekenstein's least energy for I(r) = pi r^2/(l_P^2 ln2) bits at radius r equals r c^4/(2G).
    CONTROL drop_ln2: count capacity in nats but Bekenstein in bits -- the identity must fail."""
    import sympy as sp
    r, hb, c, g = sp.symbols("r hbar c G", positive=True)
    lp2 = hb * g / c ** 3
    I = sp.pi * r ** 2 / (lp2 * (1 if drop_ln2 else sp.log(2)))
    E_floor = I * hb * c * sp.log(2) / (2 * sp.pi * r)        # measure.bekenstein_floor_j's expression
    return sp.simplify(E_floor - r * c ** 4 / (2 * g)) == 0


def capacity_table():
    """capacity_table_base() plus the comparison V66-1 #6 asked for: MMP's SM-embedded throat (mmp_scales)."""
    base = capacity_table_base()
    m = mmp_scales()
    base["mmp_SM_throat"] = [{"label": r["label"], "r_e_SM_max_m": r["r_e_SM_max_m"],
                              "capacity_bits": r["capacity_bits_at_r_e_SM"],
                              "payload_over_capacity": r["payload_bits_over_capacity_at_r_e_SM"]}
                             for r in m["by_coupling"]]
    return base


def capacity_table_base():
    pc = payload_counts()
    M = pc["payload_kg"]
    rs_payload = 2 * G * M / C ** 2
    rows = []
    for row in pc["counts"]:
        I = row["bits"]
        rf = r_fit(I)
        rb = r_bekenstein(I, pc["rest_energy_J"])
        e_floor = measure.bekenstein_floor_j(I, rf)
        m_sat = rf * C ** 2 / (2 * G)
        rows.append({"count": row["count"], "bits": I, "r_fit_m": rf, "r_fit_closed_m": r_fit_closed(I),
                     "r_fit_over_lP": rf / lp(), "capacity_at_r_fit": nopath.holographic_bits(rf),
                     "r_bekenstein_m": rb, "r_bek_over_r_fit": rb / rf,
                     "r_bek_over_r_s_payload": rb / rs_payload,
                     "bekenstein_floor_J_at_r_fit": e_floor, "schwarzschild_energy_J_at_r_fit": rf * C ** 4 / (2 * G),
                     "M_sat_kg": m_sat, "M_sat_over_payload": m_sat / M,
                     "throat_mass_kg_at_r_fit": wormhole.throat_mass(rf)})
    big = throatmass.LARGEST_THROAT_M
    big_cap = nopath.holographic_bits(big)
    return {"rows": rows, "bits_per_planck_area": 1.0 / (4 * LN2),
            "largest_board_throat_m": big, "largest_board_throat_over_lP": big / lp(),
            "capacity_of_largest_board_throat_bits": big_cap,
            "payload_over_that_capacity": [r["bits"] / big_cap for r in rows],
            "capacity_1m_bits": nopath.holographic_bits(1.0), "payload_schwarzschild_radius_m": rs_payload,
            "hypotheses": ["H-CAP-AT-THROAT", "H-NECK-DOGMA", "H-COUNT-IS-ENTROPY", "H-BEK-SCOPE (Bekenstein rows)"]}


# ================================================ (B') MMP's one-space traversable throat (D66-fix, V66-1 #2 and #6)
#: MMP 1807.04726v3, READ at D66-fix (alphaXiv answer_pdf_queries): eq.(2.3) r_e^2 = pi q^2 l_p^2 / g^2; eq.(7.58)
#: l = 16 r_e^3/(G_N q N_f), E_min = -G_N q^2 N_f^2/(256 r_e^3); eq.(6.50) Omega = 2 sqrt(r_e/d^3); (6.51) Omega l << 1;
#: (6.52) d >> (r_e^7/(l_p^4 q^2))^(1/3); (5.49) d << q^(5/2) l_p; p.26 the SM's effective N_f = 54 (hypercharge
#: normalised so the lowest charge is one); p.25 'r_e ... much smaller than the electroweak scale (say 1/TeV)'; p.18
#: an energy above the binding energy (5.31) makes a near-extremal black hole: 'not safe for human travelers'.
MMP_NF_SM = 54                     # MMP p.26 (H-SM-FIELDS)
#: H-MMP-G: the hypercharge coupling g' at the throat's scale, 0.36 .. 0.46 (a named range, not READ); MMP's
#: normalisation multiplies every hypercharge by 6, so their g = g'/6.  V66-1 used g = 0.36 in eq.(6.52) as printed.
MMP_GPRIME = (0.36, 0.46)


def mmp_scales(payload_J=None):
    """MMP's construction at the payload's scales, as order-of-magnitude estimates (H-MMP-OOM: O(1) factors in (6.51)
    and (6.52) as printed; Omega l = 1 taken at the edge of '<<').  Per coupling choice:
      q(r_e) = g r_e/(sqrt(pi) l_P) (2.3);  d_min parametric (6.52) = (r_e^7/(l_P^4 q^2))^(1/3);
      d_min explicit from (6.50), (6.51), (7.58): d^3 = 1024 r_e^7/(l_P^4 q^2 N_f^2);  d_max = q^(5/2) l_P (5.49);
      binding energy |E_min| = hbar c g^2 N_f^2 / (256 pi r_e) (7.58 with 2.3; (5.31) at N_f = 1 is the same -- checked);
      the SM bound: d_min(r_e) = 1/TeV solved for r_e, and its A/4 capacity (nopath.holographic_bits, H-CAP-AT-THROAT);
      the radius at which |E_min| equals the payload's rest energy, against l_P; and the N_f a throat of radius r_fit
      would need for |E_min| >= the payload's rest energy."""
    lP = lp()
    hbar_c = HBAR * C
    L_tev = hbar_c / (1e12 * 1.602176634e-19)          # hbar c / 1 TeV (the SI eV is a unit definition)
    E_pay = payload_J if payload_J is not None else massform.rest_energy_j()
    rfits = [r["r_fit_m"] for r in capacity_table_base()["rows"]]
    out = {"l_P_m": lP, "L_TeV_m": L_tev, "payload_rest_J": E_pay, "N_f_SM": MMP_NF_SM, "by_coupling": []}
    choices = [("V66-1: g = 0.36, eq.(6.52) as printed, N_f = 1", 0.36, 1, "param")]
    for gp in MMP_GPRIME:
        choices.append(("g' = %.2f, MMP normalisation g = g'/6, N_f = 54, explicit (6.50)-(6.51)-(7.58)" % gp,
                        gp / 6.0, MMP_NF_SM, "explicit"))
    for lab, g, nf, form in choices:
        def q_of(r):
            return g * r / (math.sqrt(math.pi) * lP)

        def dmin(r):
            q = q_of(r)
            if form == "param":
                return (r ** 7 / (lP ** 4 * q * q)) ** (1.0 / 3.0)
            return (1024.0 * r ** 7 / (lP ** 4 * q * q * nf * nf)) ** (1.0 / 3.0)

        def ebind(r):
            return hbar_c * g * g * nf * nf / (256.0 * math.pi * r)
        # the SM bound: dmin(r_e) = L_TeV  (dmin ~ r_e^(5/3))
        if form == "param":
            r_sm = (L_tev ** 3 * g * g * lP * lP / math.pi) ** 0.2
        else:
            r_sm = (L_tev ** 3 * lP * lP * g * g * nf * nf / (1024.0 * math.pi)) ** 0.2
        row = {"label": lab, "g": g, "N_f": nf,
               "r_e_SM_max_m": r_sm, "r_e_SM_max_over_lP": r_sm / lP, "dmin_check_at_r_e_SM": dmin(r_sm) / L_tev,
               "capacity_bits_at_r_e_SM": nopath.holographic_bits(r_sm),
               "r_e_where_binding_equals_payload_m": hbar_c * g * g * nf * nf / (256.0 * math.pi * E_pay),
               "at_r_fit": []}
        row["payload_bits_over_capacity_at_r_e_SM"] = [c["bits"] / row["capacity_bits_at_r_e_SM"]
                                                       for c in capacity_table_base()["rows"]]
        for r in rfits:
            q = q_of(r)
            row["at_r_fit"].append({"r_fit_m": r, "q": q, "d_min_m": dmin(r), "d_max_m": q ** 2.5 * lP,
                                    "d_min_over_L_TeV": dmin(r) / L_tev, "binding_J": ebind(r),
                                    "payload_over_binding": E_pay / ebind(r),
                                    "N_f_needed_for_payload": math.sqrt(256.0 * math.pi * r * E_pay / (hbar_c * g * g))})
        out["by_coupling"].append(row)
    # the two printed forms of the binding energy agree: (5.31) at N_f = 1 vs (7.58) with (2.3)
    g, r = 0.06, 1e-25
    q = g * r / (math.sqrt(math.pi) * lP)
    e531 = g ** 3 / (256.0 * math.pi ** 1.5 * q * lP) * hbar_c        # (5.31): g^3/(256 pi^(3/2) q l_p), hbar = c = 1
    e758 = (lP * lP) * q * q * 1 / (256.0 * r ** 3) * hbar_c            # (7.58): G_N q^2 N_f^2/(256 r_e^3), G_N = l_p^2
    out["binding forms (5.31) vs (7.58), ratio"] = e531 / e758
    out["CONTROL (5.31) without its pi^(3/2), ratio"] = (e531 * math.pi ** 1.5) / e758
    return out


# ============================================================================================ (C) the QNEC price
def qnec_table(bprime=0.0):
    out = []
    for row in capacity_table()["rows"]:
        q = geometry.qnec_price(row["r_fit_m"], bprime)
        rq = geometry.r_quantum(row["r_fit_m"], bprime)
        out.append({"count": row["count"], "r_fit_m": row["r_fit_m"],
                    "qnec_fraction_of_sheet_cap": q["fraction_of_sheet_cap"],
                    "qnec_dS_over_throat_bits": q["dS_over_throat_sphere_bits"],
                    "qnec_dS_over_payload_bits": q["dS_over_throat_sphere_bits"] / row["bits"],
                    "rquantum_fraction_covered": rq["fraction_covered"], "r_star_over_lP": rq["r_star_over_lP"]})
    return {"rows": out, "bprime": bprime,
            "hypotheses": ["H-QNEC-OUT-OF-SCOPE", "H-CONST", "H_flat, H-PATH, H-MIN-SCALAR (R-QUANTUM)"]}


def shape():
    return geometry.shape_checks()


# ================================================================================= (D) the singular (thin-shell) throat
def pv_symbols():
    import sympy as sp
    M, a = sp.symbols("M a", positive=True)
    f = 1 - 2 * M / a
    sigma0 = -sp.sqrt(f) / (2 * sp.pi * a)                    # PV (18)
    p0 = (1 - M / a) / (4 * sp.pi * a * sp.sqrt(f))           # PV (19)
    return sp, M, a, sigma0, p0


def pv_conservation(flip=False):
    """PV (13) d(sigma A)/dtau + p dA/dtau = 0 from (11)-(12), A = 4 pi a^2, a = a(tau).  CONTROL flip: the sign of
    the M/a term in p reversed -- the law must fail."""
    import sympy as sp
    t = sp.symbols("tau")
    M = sp.symbols("M", positive=True)
    a = sp.Function("a")(t)
    ad, add = sp.diff(a, t), sp.diff(a, t, 2)
    root = sp.sqrt(1 - 2 * M / a + ad ** 2)
    sigma = -root / (2 * sp.pi * a)                                                 # PV (11)
    mt = (M / a) if not flip else (-M / a)
    p = (1 - mt + ad ** 2 + a * add) / (4 * sp.pi * a * root)                        # PV (12)
    A = 4 * sp.pi * a ** 2
    expr = sp.diff(sigma * A, t) + p * sp.diff(A, t)
    return sp.simplify(expr) == 0


def pv_static():
    """sigma_0 < 0 for every a_0 > 2M (exact); the shell's NEC combination sigma_0 + p_0 in closed form; the shell mass
    4 pi a_0^2 sigma_0."""
    sp, M, a, s0, p0 = pv_symbols()
    nec = sp.simplify(s0 + p0)
    nec_closed = (3 * M / a - 1) / (4 * sp.pi * a * sp.sqrt(1 - 2 * M / a))
    closed_ok = sp.simplify(nec - nec_closed) == 0
    m_shell = sp.simplify(4 * sp.pi * a ** 2 * s0)
    grid = [2.0001, 2.5, 2.9, 3.0, 3.1, 4, 10, 1e3, 1e6]                           # a_0 / M
    sig = [float(s0.subs({M: 1, a: x})) for x in grid]
    necv = [float(nec.subs({M: 1, a: x})) for x in grid]
    return {"sigma0_negative_all": all(v < 0 for v in sig),
            "nec_closed_form_ok": closed_ok, "nec_closed_form": str(nec_closed),
            "nec_sign_by_a0_over_M": dict(zip(grid, ["<0" if v < 0 else (">0" if v > 0 else "=0") for v in necv])),
            "m_shell_geometric": str(m_shell),
            "m_shell_at_M0": str(sp.simplify(m_shell.subs(M, 0)))}


def pv_stab_lhs(x, b2):
    """PV (29)'s left side with x = M/a_0: stable iff < 0."""
    return 2 * x + x * x / (1 - 2 * x) + (1 + 2 * b2) * (1 - 3 * x)


def pv_roots(b2):
    """PV (34): a_0^-+ / M (minus, plus).  Real only outside (3/2 - sqrt3, 3/2 + sqrt3)."""
    disc = 4 * b2 * b2 - 12 * b2 - 3
    if disc < 0:
        return None
    num = 6 * (1 + 4 * b2)
    return num / (3 + 10 * b2 + math.sqrt(disc)), num / (3 + 10 * b2 - math.sqrt(disc))


def pv_stability_scan(b2_values, n=4000):
    """For each beta_0^2, the a_0/M in (2, 1e4] where (29) holds, on a log grid."""
    out = {}
    for b2 in b2_values:
        stable = []
        for k in range(n):
            y = 2.0 * (5000.0 ** ((k + 0.5) / n))                    # a_0/M from just above 2 to 1e4
            if pv_stab_lhs(1.0 / y, b2) < 0:
                stable.append(y)
        out[b2] = (min(stable), max(stable), len(stable)) if stable else None
    return out


def pv_root_check(b2):
    """PV (34)'s roots, transcribed, against the zeros of (29)'s left side found numerically."""
    rr = pv_roots(b2)
    if rr is None:
        return None
    return [abs(pv_stab_lhs(1.0 / y, b2)) for y in rr]


def thin_shell_at(r):
    """Shell mass at M = 0 in SI: 4 pi a^2 sigma_0 = -2a (geometric) -> -2 a c^2/G; against wormhole.throat_mass."""
    m = -2.0 * r * C ** 2 / G
    return {"r_m": r, "m_shell_kg": m, "throat_mass_kg": wormhole.throat_mass(r),
            "ratio_m_shell_over_throat_mass": m / wormhole.throat_mass(r),
            "ratio_over_M_sat": m / (r * C ** 2 / (2 * G))}


# ======================================================================================= (E) the board's rulings, read
def m_ruling_text():
    led = _quiet_import("ledger")
    for r in led.RULED_BY_M:
        if r[0] == "M-S1A-P3":
            return " ".join(r)
    return ""


def charter_hypothesis():
    txt = open(os.path.join(HERE, "CHARTER.md"), encoding="utf-8").read()
    m = re.search(r"\| H-THROAT-BITS \| (.+?) \| (.+?) \|", txt)
    return (m.group(1), m.group(2)) if m else (None, None)


_SPEC = {}


def specthm_verdicts():
    """The seat and throat class verdicts, derived by specthm's own z3 at run time (about 45 s)."""
    if not _SPEC:
        with contextlib.redirect_stdout(io.StringIO()):
            spec = _quiet_import("specthm")
            model = spec.build()
            v = spec.derive(model)
        _SPEC.update({k: v[k]["verdict"] for k in v})
        _SPEC["_M-S1A-P3_ruled"] = spec.ruled("M-S1A-P3")
        _SPEC["_sturm_member_diameter"] = spec.sturm_over_ball(min(model["F"]["soc"]))["member_diameter"]
    return dict(_SPEC)


def d68_row(prefix):
    for g in geometry.GRADES:
        if g["hypothesis"].startswith(prefix):
            return g
    raise KeyError(prefix)


# ================================================================================================== (F) the grades
VERDICT_WORDS = ("REMOVED", "REMOVED-IF", "NOT-BOUND-IF", "OPEN", "LEFT", "LEFT-IF", "SILENT")
OBSTRUCTIONS = ("O-BITS", "O-MAKE-TOPO", "O-MAKE-DIST", "O-HOLD", "O-SEAT", "O-LOOP")


def grades(spec=None):
    spec = spec or specthm_verdicts()
    cap = capacity_table()
    q = qnec_table()
    r0 = cap["rows"][0]
    ite, itb = d68_row("H-IT read as ER=EPR"), d68_row("H-IT read as an information layer")
    mm = mmp_scales()
    mm_sm = mm["by_coupling"][1]          # g' = 0.36 in MMP's normalisation, N_f = 54 (the SM row); the others reported
    wncc = spec["W-create-ncc"]
    seat_cls = "S-1 %s, S-2 %s, S-3 %s, Rec %s" % (spec["S-1"], spec["S-2"], spec["S-3"], spec["Rec"])
    seat_common = ("specthm's seating classes are not moved (%s; derived by z3 at run time): H-THROAT-BITS supplies no "
                   "T_kk at the seat, so the Sturm condition (sufficient, on T_kk along a chord) is untouched "
                   "(specthm's recorded T_kk = 2u member ratio on a diameter %.4f, as the owner prints it). "
                   "M-S1A-P3 (i) applies at the seat (ruled: %s)." % (seat_cls, spec["_sturm_member_diameter"],
                                                                       spec["_M-S1A-P3_ruled"]))
    o_seat = ("OPEN via N_S5 (D68 unchanged: H-SEAT-S5, M-RULINGS item 7).  Under H-INFO-SHAPE what is pushed is the "
              "defining information; the substance comes 'from the seat' (M-RULINGS item 5).  H-THROAT-BITS adds no "
              "supply: SILENT on the supply itself, so the board's OPEN stands")
    G = []
    G.append({
        "reading": "R-HOLO: 'compressed to binary information' = the throat's geometry holds its information at the "
                   "holographic density, A/(4 l_P^2 ln2) bits",
        "premises": ["H-CAP-AT-THROAT", "H-NECK-DOGMA", "H-COUNT-IS-ENTROPY", "H-ALT", "H-BEK-SCOPE"],
        "per": {
            "O-BITS": "LEFT: a capacity is a ceiling on entropy, not a channel; nothing crosses (BSST via measure.py "
                      "H-FAITHFUL: %.3g classical bits if the %.3g-bit count were teleported as qubits)"
                      % (r0["bits"] * 2, r0["bits"]),
            "O-MAKE-TOPO": "OPEN via specthm W-create-ncc (%s): Tipler/Borde still bind -- what they force (a "
                           "singularity or pathology) is placed at the throat, which M-S1A-P3 (i) does not disqualify; "
                           "admitted by ruling, not shown realisable.  Not REMOVED, not NOT-BOUND" % wncc,
            "O-MAKE-DIST": "SILENT (this reading distributes nothing)",
            "O-HOLD": "LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}: computed from PV, sigma_0 < 0 at every a_0 > 2M "
                      "and sigma_0 + p_0 < 0 for a_0 > 3M; the singular throat concentrates the deficit, does not "
                      "remove it.  Priced further (H-QNEC-OUT-OF-SCOPE, H-CONST): the throat that fits the count "
                      "needs |dS| = %.3f of the count; R-QUANTUM covers %.2g of its deficit at r_fit"
                      % (q["rows"][0]["qnec_dS_over_payload_bits"], q["rows"][0]["rquantum_fraction_covered"]),
            "O-SEAT": o_seat,
            "O-LOOP": "SILENT (no loop asserted; a loop AT THE THROAT would not disqualify, M-S1A-P3 (i))"},
        "what_it_does": "r_fit is the radius at which the A/4 ceiling equals the payload's count, IF {H-CAP-AT-THROAT, "
                        "H-NECK-DOGMA, H-COUNT-IS-ENTROPY}; no mechanism that compresses or encodes at that density is "
                        "constructed or READ (a capacity is a ceiling, not an encoding).  Wave 1 first said 'a precise "
                        "size' for M's mechanism (V66-0 #4).  That radius is %.3g-%.3g m (%.3g-%.3g l_P).  At the payload's own "
                        "Mc^2, Bekenstein (in scope: R_Bek >> r_s) admits the count only at R >= %.3g-%.3g m; held at "
                        "r_fit the count needs at least the Schwarzschild energy of r_fit, M_sat = %.3g-%.3g kg "
                        "(%.3g-%.3g x the payload), where the two bounds meet.  Removes nothing."
                        % (cap["rows"][0]["r_fit_m"], cap["rows"][2]["r_fit_m"], cap["rows"][0]["r_fit_over_lP"],
                           cap["rows"][2]["r_fit_over_lP"], cap["rows"][0]["r_bekenstein_m"],
                           cap["rows"][2]["r_bekenstein_m"], cap["rows"][0]["M_sat_kg"], cap["rows"][2]["M_sat_kg"],
                           cap["rows"][0]["M_sat_over_payload"], cap["rows"][2]["M_sat_over_payload"])})
    G.append({
        "reading": "R-THINSHELL: 'singular occurs in the throat' = a Poisson-Visser thin-shell throat (distributional "
                   "curvature on a complete manifold)",
        "premises": ["H-SINGULAR-IS-THINSHELL", "H-PV-STATIC"],
        "per": {
            "O-BITS": "LEFT (a shell is geometry; it carries no channel)",
            "O-MAKE-TOPO": "OPEN via specthm W-create-ncc (%s); PV's construction is cut-and-paste, a spacetime "
                           "given, not a dynamics that makes one" % wncc,
            "O-MAKE-DIST": "SILENT",
            "O-HOLD": "LEFT-IF {H-SINGULAR-IS-THINSHELL, H-PV-STATIC}: sigma_0 < 0 (WEC fails everywhere on the shell, "
                      "PV p.3 'exotic'); NEC on the shell fails for a_0 > 3M (computed); stable only for beta_0^2 "
                      "outside (-1/2, 3/2 + sqrt3) (PV (35)-(36), reproduced); for 0 < beta_0^2 <= 1 unstable at "
                      "every a_0 (reproduced on a grid).  PV p.4 do not rule |beta_0^2| > 1 out a priori: OPEN within "
                      "PV's own caveat, as PV state it",
            "O-SEAT": o_seat,
            "O-LOOP": "SILENT (PV's manifold has two asymptotic regions and no loop)"},
        "what_it_does": "Under H-SINGULAR-IS-THINSHELL a singular throat is a standard distributional object (PV p.1: "
                        "geodesically complete; the Einstein tensor a Dirac distribution), so admitting it costs GR no "
                        "new structure; it still needs sigma_0 < 0 (computed), so the deficit is concentrated, not "
                        "removed.  Under H-SINGULAR-IS-PINCH: not modelled.  Wave 1 first said the ruling 'costs GR "
                        "nothing' (V66-0 #5).  Its shell mass at M = 0 is -2a c^2/G = -16 pi x wormhole.throat_mass(a) "
                        "(computed); at r_fit, %.3g kg." % thin_shell_at(cap["rows"][0]["r_fit_m"])["m_shell_kg"]})
    G.append({
        "reading": "R-TELEPORT: 'compressed to binary information, then pushed to the seat' = traversable-wormhole "
                   "teleportation (GJW sec.5, MSY sec.2 and 4.1)",
        "premises": ["H-GJW-COUNTERPART", "H-ADS-TFD", "H-COUPLED"],
        "per": {
            "O-BITS": "LEFT: GJW p.4 (decoupled: no signal through the bulk), p.14 (no faster than light over long "
                      "distances); MSY (2.21), (2.25): N_send <~ g <~ N_bits, parametric.  The binary information "
                      "is the coupling's, carried outside at <= c",
            "O-MAKE-TOPO": "NOT-BOUND-IF {H-ER=EPR} -- D68's ITE grade carried in (geometry.GRADES: '%s'), not added "
                           "by H-THROAT-BITS: GJW's bridge is the TFD's, present before the coupling.  Without ITE the "
                           "bridge's creation is OPEN via specthm W-create-ncc (%s): M's ruling (ledger M-S1A-P3) "
                           "places the pathology at the throat and keeps the throat-creation classes OPEN"
                           % (ite["per"]["O-MAKE-TOPO"], wncc),
            "O-MAKE-DIST": "LEFT-IF {H-GJW-COUNTERPART, MS sec.3.2 (board READ)}: the bridge is a prior shared "
                           "entanglement; D68 geometry.GRADES ITE: '%s'; D68's vacuum route stays LEFT-IF its nine "
                           "hypotheses (vacuum.GRADES)" % ite["per"]["O-MAKE-DIST"],
            "O-HOLD": "LEFT-IF {H-GJW-COUNTERPART, H-ADS-TFD, H-COUPLED} for a hold on GJW alone: GJW's bridge "
                      "becomes 'slightly traversable' (p.12), 'only open for a small proper time' (p.13), opening "
                      "Delta V ~ h G_N/R^(D-2) (eq.(5.1)); in the teleportation reading the window is 'just enough to "
                      "let the single qubit Q pass through' (p.15) -- an opening, not a hold, as A1 grades FGM's brief "
                      "opening.  Wave 1 first said REMOVED-IF on GJW alone (V66-0 #1).  A HELD throat, READ: (a) "
                      "Maldacena & Qi 1804.00491: REMOVED-IF {H-GJW-COUNTERPART, H-MQ-NADS2, H-MQ-ETERNAL-COUPLING, "
                      "H-MQ-LARGE-N} in nearly-AdS2, outside the board's one-space setting (E-ADS); (b) Maldacena, "
                      "Milekhin & Popov 1807.04726 in one asymptotically flat space: REMOVED-IF {H-GJW-COUNTERPART, "
                      "H-MMP, H-SM-FIELDS} at sub-electroweak scale (r_e <= %.2g m, holding <= %.2g bits), outside the "
                      "board's setting by scale.  In both, H-GJW-COUNTERPART (M's reading) is load-bearing in that "
                      "setting, and the hold rests on the coupling (MQ: added by hand; MMP: generated by massless bulk "
                      "fields), O-BITS's channel at <= c.  For a throat that admits the payload in one space: LEFT-IF "
                      "{H-MMP, H-SM-FIELDS}: MMP's binding energy (eqs.(5.31), (7.58)) equals the payload's rest energy "
                      "only at r_e = %.2g m, below l_P, and at r_fit a throat needs N_f >= %.2g massless charged species "
                      "(the SM has 54) with mouths d >= %.2g m apart, %.2g x 1/TeV (mmp_scales, H-MMP-OOM, H-MMP-G); "
                      "outside that family OPEN via N_GJW-PAYLOAD.  Wave 1 carried N_GJW-AMBIENT, 'stated, not "
                      "computed' (V66-1 #2)" % (mm_sm["r_e_SM_max_m"], mm_sm["capacity_bits_at_r_e_SM"],
                                                 mm_sm["r_e_where_binding_equals_payload_m"],
                                                 mm_sm["at_r_fit"][0]["N_f_needed_for_payload"],
                                                 mm_sm["at_r_fit"][0]["d_min_m"],
                                                 mm_sm["at_r_fit"][0]["d_min_over_L_TeV"]),
            "O-SEAT": o_seat + ".  Teleportation needs the receiving half at the seat (B-RECV), as H-INFO-SHAPE has",
            "O-LOOP": "SILENT (GJW p.13: the coupling fixes the relative time, excluding closed timelike curves in "
                      "their setting; no loop reintroduced)"},
        "what_it_does": "The closest READ counterpart of M's whole sentence.  It realises 'information passes the "
                        "throat' (MSY p.22-23: the teleportee feels nothing special) and shows what pays for it: a "
                        "prior bridge and bits pushed outside.  For the payload, >= %.3g-%.3g classical bits at <= c "
                        "(H-FAITHFUL; MSY's bound is parametric and does not itself give the factor 2)."
                        % (cap["rows"][0]["bits"] * 2, cap["rows"][2]["bits"] * 2)})
    G.append({
        "reading": "R-ISLAND: 'compressed to binary information' = the island formula's area term; information in the "
                   "interior encoded in the radiation after the Page time",
        "premises": ["H-ISLAND-COUNTERPART", "H-NECK-DOGMA"],
        "per": {
            "O-BITS": "LEFT-IF {H-ISLAND-COUNTERPART}: the formula gives the entropy, not the state (2006.06872 p.38); "
                      "the radiation that carries the information leaves physically; decoding is roughly exponential "
                      "in S_BH (p.33)",
            "O-MAKE-TOPO": "SILENT (replica wormholes are Euclidean saddles computing Tr rho^n, p.37; nothing is made)",
            "O-MAKE-DIST": "SILENT", "O-HOLD": "SILENT (no traversable throat in this reading)",
            "O-SEAT": o_seat, "O-LOOP": "SILENT"},
        "what_it_does": "The area term counts fine-grained entropy, not a state or an encoding (2006.06872 p.38); a "
                        "wormhole here carries information into the entanglement wedge.  Nothing is sent.  Wave 1 first "
                        "said 'a precise sense in which geometry is compressed to binary information' (V66-0 #4)."})
    G.append({
        "reading": "R-ITB: M's words taken literally under D68's ITB -- the geometry ceases at the throat and the "
                   "information continues beneath it",
        "premises": ["H-ITB (D68: H-IT as an information layer, no READ realisation)", "N_QTOPO"],
        "per": {
            "O-BITS": "LEFT (D68 geometry.GRADES ITB: '%s'); the push from throat to seat has no READ realisation; a "
                      "route exists only in combination with D68's W2 x F1 (screen candidate, not graded here)"
                      % itb["per"]["O-BITS"],
            "O-MAKE-TOPO": "NOT-BOUND-IF {N_QTOPO} -- D68's ITB grade carried in ('%s'); H-THROAT-BITS adds the "
                           "location only" % itb["per"]["O-MAKE-TOPO"],
            "O-MAKE-DIST": "LEFT (D68 ITB: '%s')" % itb["per"]["O-MAKE-DIST"],
            "O-HOLD": "NOT-BOUND-IF {N_QTOPO} in its geometric form; the layer's own holding cost OPEN (D68 ITB: '%s')"
                      % itb["per"]["O-HOLD"],
            "O-SEAT": o_seat,
            "O-LOOP": "NOT-BOUND-IF {N_QTOPO} for corridors (D68 ITB)"},
        "what_it_does": "Locates D68's two ITB non-bindings at the throat.  Adds no content of its own: every "
                        "non-binding here is H-IT's under N_QTOPO."})
    for g in G:
        g["seat_conditions"] = (seat_common + "  Seat free of a CTC / Borde pathology: SATISFIED-IF "
                                "{H-SEAT-OFF-THROAT} in R-HOLO and R-THINSHELL (PV's shell is the singular support, "
                                "the rest of the manifold is complete); R-TELEPORT adds GJW p.13 (no CTC).  Throat "
                                "creation classes unchanged (W-create-cc %s, W-create-ncc %s, W-enlarge %s)."
                                % (spec["W-create-cc"], spec["W-create-ncc"], spec["W-enlarge"]))
    return G


def grade_word(cell):
    m = re.match(r"(REMOVED-IF|REMOVED|NOT-BOUND-IF|OPEN|LEFT-IF|LEFT|SILENT)\b", cell)
    return m.group(1) if m else None


def grade_audit(G):
    """Rule checks on the grades: every cell starts with a vocabulary word; no bare REMOVED; every REMOVED-IF / LEFT-IF
    / NOT-BOUND-IF names its premises in braces; no removal is credited to H-THROAT-BITS itself."""
    bad = []
    for g in G:
        for o in OBSTRUCTIONS:
            cell = g["per"][o]
            w = grade_word(cell)
            if w is None:
                bad.append((g["reading"][:12], o, "no vocabulary word"))
            elif w == "REMOVED":
                bad.append((g["reading"][:12], o, "bare REMOVED (no premise)"))
            elif w in ("REMOVED-IF", "LEFT-IF", "NOT-BOUND-IF") and not re.match(w + r" \{[^}]+\}", cell):
                bad.append((g["reading"][:12], o, w + " without a premise set"))
            if w == "REMOVED-IF" and "not to H-THROAT-BITS" not in cell:
                bad.append((g["reading"][:12], o, "removal not attributed"))
    return bad


def member_removals(G):
    """Removals credited to H-THROAT-BITS itself IN THE BOARD'S SETTING: a cell whose leading word is REMOVED-IF and
    which does not disclaim the member.  (D66-fix: no leading REMOVED-IF remains; the setting-bound removals are listed
    by setting_removals.)"""
    return [(g["reading"][:12], o) for g in G for o in OBSTRUCTIONS
            if grade_word(g["per"][o]) == "REMOVED-IF" and "not to H-THROAT-BITS" not in g["per"][o]]


SETTING_TAGS = ("outside the board's one-space setting", "outside the board's setting by scale")


def setting_removals(G):
    """D66-fix (V66-1 #8): every REMOVED-IF clause anywhere in a cell whose premise set holds H-GJW-COUNTERPART (M's
    reading, so load-bearing there): (reading, obstruction, premises, the setting it names or None).  A clause naming no
    setting would be a member removal in the board's setting; the audit refuses it."""
    out = []
    for g in G:
        for o in OBSTRUCTIONS:
            cell = g["per"][o]
            for m in re.finditer(r"REMOVED-IF \{([^}]*)\}([^;(]*)", cell):
                if "H-GJW-COUNTERPART" in m.group(1):
                    tail = cell[m.end(1):m.end(1) + 200]
                    tag = next((t for t in SETTING_TAGS if t in tail), None)
                    out.append((g["reading"][:12], o, m.group(1), tag))
    return out


# ================================================================================================ report and checks
def report_data(spec=None):
    spec = spec or specthm_verdicts()
    cap = capacity_table()
    d = {"hypothesis": charter_hypothesis(), "payload": payload_counts(), "capacity": cap,
         "qnec": qnec_table(), "shape_checks": shape(), "pv_static": pv_static(),
         "pv_stability": {str(k): v for k, v in pv_stability_scan([0.25, 1.0, -1.0, 4.0]).items()},
         "pv_roots_b2_4": pv_roots(4.0), "thin_shell_at_r_fit": [thin_shell_at(r["r_fit_m"]) for r in cap["rows"]],
         "specthm": spec, "grades": grades(spec), "read": READ, "board_read": BOARD_READ, "mmp": mmp_scales(),
         "history": HISTORY}
    return d


def report():
    spec = specthm_verdicts()
    d = report_data(spec)
    hy = d["hypothesis"]
    print("throatbits.py -- DOCKET 66 A2-throatbits (H-THROAT-BITS).  Not seated.\n")
    print("H-THROAT-BITS (CHARTER.md):", hy[0], "--", hy[1])
    print("\n(A) the payload, %.0f kg, %.4g atoms (measure.price_table; H-ALT):" % (d["payload"]["payload_kg"],
                                                                                   d["payload"]["atoms"]))
    for r in d["payload"]["counts"]:
        print("    %-42s %.4g bits" % (r["count"], r["bits"]))
    print("\n(B) holographic fit (nopath.holographic_bits; H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY):")
    for r in d["capacity"]["rows"]:
        print("    %-42s r_fit %.4g m = %.4g l_P | Bekenstein at Mc^2: R >= %.4g m (%.4g x r_fit) | M_sat %.4g kg "
              "(%.4g x payload)" % (r["count"], r["r_fit_m"], r["r_fit_over_lP"], r["r_bekenstein_m"],
                                    r["r_bek_over_r_fit"], r["M_sat_kg"], r["M_sat_over_payload"]))
    c = d["capacity"]
    print("    largest board throat (throatmass, 300 l_P) holds %.4g bits; payload / that = %.3g .. %.3g"
          % (c["capacity_of_largest_board_throat_bits"], min(c["payload_over_that_capacity"]),
             max(c["payload_over_that_capacity"])))
    print("\n(C) QNEC price at r_fit (geometry.qnec_price; H-QNEC-OUT-OF-SCOPE, H-CONST), b'(r0) = 0:")
    for r in d["qnec"]["rows"]:
        print("    %-42s |dS| over throat = %.4g bits = %.3f of the count; R-QUANTUM covers %.3g"
              % (r["count"], r["qnec_dS_over_throat_bits"], r["qnec_dS_over_payload_bits"],
                 r["rquantum_fraction_covered"]))
    s = d["shape_checks"]
    print("    no light-sheet leaves a flare-out throat (geometry.shape_checks): theta(r0) = %s, theta(1.01 r0) = %.4f"
          % (s["b=r0^2/r"]["theta(r0)"], s["b=r0^2/r"]["theta(1.01 r0)"]))
    print("\n(D) Poisson-Visser thin-shell throat (READ gr-qc/9506083v1):")
    pv = d["pv_static"]
    print("    sigma_0 < 0 for all a_0 > 2M: %s; sigma_0 + p_0 = %s; sign by a_0/M: %s"
          % (pv["sigma0_negative_all"], pv["nec_closed_form"], pv["nec_sign_by_a0_over_M"]))
    print("    shell mass 4 pi a^2 sigma_0 = %s (M = 0: %s)" % (pv["m_shell_geometric"], pv["m_shell_at_M0"]))
    print("    stable a_0/M ranges by beta_0^2 (grid to 1e4):", d["pv_stability"])
    for t in d["thin_shell_at_r_fit"][:1]:
        print("    at r_fit %.4g m: shell mass %.4g kg = %.4f x throat_mass = %.4f x M_sat"
              % (t["r_m"], t["m_shell_kg"], t["ratio_m_shell_over_throat_mass"], t["ratio_over_M_sat"]))
    print("\n(E) specthm class verdicts (z3, run time):",
          {k: v for k, v in spec.items() if not k.startswith("_")})
    print("\n(F) grades of H-THROAT-BITS (B-combine vocabulary):")
    for g in d["grades"]:
        print("  " + g["reading"])
        print("    premises:", ", ".join(g["premises"]))
        for o in OBSTRUCTIONS:
            print("    %-12s %s" % (o, g["per"][o]))
        print("    does:", g["what_it_does"])
    print("\n  removals credited to H-THROAT-BITS in the board's setting:", member_removals(d["grades"]) or "none")
    print("  setting-bound removals (M's reading load-bearing there):")
    for x in setting_removals(d["grades"]):
        print("    %s %s REMOVED-IF {%s} -- %s" % x)
    print("\n(B') MMP 1807.04726 at the payload's scales (mmp_scales; H-MMP-OOM):")
    for r in d["mmp"]["by_coupling"]:
        print("  %s: SM bound r_e <= %.3g m (%.3g bits); binding = payload rest energy at r_e = %.3g m; at r_fit "
              "d_min %.3g m, N_f needed %.3g" % (r["label"], r["r_e_SM_max_m"], r["capacity_bits_at_r_e_SM"],
                                               r["r_e_where_binding_equals_payload_m"], r["at_r_fit"][0]["d_min_m"],
                                               r["at_r_fit"][0]["N_f_needed_for_payload"]))
    print("\nWhat wave 1 first said (HISTORY):")
    for h in HISTORY:
        print("  %s: wave 1 first said '%s'; now: %s (%s)" % h)
    print("\nREAD this work item:", ", ".join(r["key"] for r in READ), "--", ROUTE)


def selftest():
    n = {"pass": 0, "fail": 0, "control": 0, "structural": 0}

    def chk(name, ok, control=False):
        n["pass" if ok else "fail"] += 1
        if control:
            n["control"] += 1
        print(("PASS " if ok else "FAIL ") + ("[CONTROL] " if control else "") + name)

    def structural(name, ok):
        n["structural"] += 1
        print("STRUCTURAL (not counted) %s: %s" % (name, ok))

    # (A)
    pc = payload_counts()
    sp_printed, gr_printed = a3_printed()
    bits = [r["bits"] for r in pc["counts"]]
    chk("A1 species count reproduces A3-measure.md's printed %.4g" % sp_printed, abs(bits[0] / sp_printed - 1) < 5e-4)
    chk("A2 0.1 A grid count reproduces A3-measure.md's printed %.4g" % gr_printed, abs(bits[2] / gr_printed - 1) < 5e-4)
    chk("A3 a value off by 1 % is NOT taken as a reproduction", not abs(bits[0] / (sp_printed * 1.01) - 1)
        < 5e-4, control=True)
    chk("A4 the counts span 9.5e27 .. 1.1e29 (min/max), the charter's H-ALT range",
        abs(min(bits) / 9.5e27 - 1) < 0.01 and abs(max(bits) / 1.1e29 - 1) < 0.02)
    # (B)
    cap = capacity_table()
    chk("B1 r_fit by bisection on nopath.holographic_bits = closed form l_P sqrt(I ln2/pi), all four counts",
        all(abs(r["r_fit_m"] / r["r_fit_closed_m"] - 1) < 1e-9 for r in cap["rows"]))
    wrong = lp() * math.sqrt(bits[0] / math.pi)                    # ln2 dropped
    chk("B2 a capacity counted in nats (ln2 dropped) misses r_fit (by sqrt(ln2))",
        abs(cap["rows"][0]["r_fit_m"] / wrong - 1) > 0.1, control=True)
    chk("B3 round trip: capacity at r_fit equals the count", all(abs(r["capacity_at_r_fit"] / r["bits"] - 1) < 1e-9
                                                                  for r in cap["rows"]))
    chk("B4 saturation identity (sympy): Bekenstein's least energy for I(r) bits at r is r c^4/(2G)",
        saturation_identity_symbolic())
    chk("B5 the identity fails with the capacity in nats", not saturation_identity_symbolic(True),
        control=True)
    chk("B6 numeric: measure.bekenstein_floor_j(I, r_fit) = r_fit c^4/(2G), all counts",
        all(abs(r["bekenstein_floor_J_at_r_fit"] / r["schwarzschild_energy_J_at_r_fit"] - 1) < 1e-8
            for r in cap["rows"]))
    chk("B7 R_Bek / r_fit = M_sat / M_payload (the same identity, by a second route)",
        all(abs(r["r_bek_over_r_fit"] / r["M_sat_over_payload"] - 1) < 1e-8 for r in cap["rows"]))
    chk("B8 Bekenstein at Mc^2 is in its weak-gravity scope: R_Bek >> payload r_s (> 1e6)",
        all(r["r_bek_over_r_s_payload"] > 1e6 for r in cap["rows"]))
    chk("B9 the largest board throat (300 l_P) holds < 1e-20 of the smallest count",
        max(1 / x for x in cap["payload_over_that_capacity"]) < 1e-20)
    # (B') MMP, D66-fix
    mm = mmp_scales()
    v1 = mm["by_coupling"][0]
    chk("B10 MMP eq.(2.3) + (6.52) as printed, g = 0.36 (V66-1's estimate reproduced): the SM-embedded throat has "
        "r_e <= %.3g m (V66-1: ~3.8e-26) holding %.3g bits (V66-1: ~2.5e19)" % (v1["r_e_SM_max_m"],
                                                                             v1["capacity_bits_at_r_e_SM"]),
        abs(v1["r_e_SM_max_m"] / 3.8e-26 - 1) < 0.02 and abs(v1["capacity_bits_at_r_e_SM"] / 2.5e19 - 1) < 0.05
        and abs(v1["dmin_check_at_r_e_SM"] - 1) < 1e-9)
    chk("B11 ... and at r_fit the mouths need d >> %.3g .. %.3g m (V66-1: 2.7e-12 .. 2.1e-11), far beyond 1/TeV"
        % (v1["at_r_fit"][0]["d_min_m"], v1["at_r_fit"][2]["d_min_m"]),
        abs(v1["at_r_fit"][0]["d_min_m"] / 2.7e-12 - 1) < 0.03 and abs(v1["at_r_fit"][2]["d_min_m"] / 2.1e-11 - 1) < 0.03
        and all(a["d_min_over_L_TeV"] > 1e6 for r_ in mm["by_coupling"] for a in r_["at_r_fit"]))
    chk("B12 MMP's two printed forms of the binding energy agree ((5.31) at N_f = 1 against (7.58) with (2.3)): ratio "
        "%.12f" % mm["binding forms (5.31) vs (7.58), ratio"], abs(mm["binding forms (5.31) vs (7.58), ratio"] - 1) < 1e-12)
    chk("B13 CONTROL: (5.31) with its pi^(3/2) dropped disagrees (ratio %.3f): the comparison can fail"
        % mm["CONTROL (5.31) without its pi^(3/2), ratio"],
        abs(mm["CONTROL (5.31) without its pi^(3/2), ratio"] - 1) > 0.5, control=True)
    chk("B14 in every coupling choice the throat whose binding energy equals the payload's rest energy is below l_P "
        "(MMP p.18: more energy than the binding makes a black hole), and r_fit needs N_f >= 1e13 massless charged species",
        all(r_["r_e_where_binding_equals_payload_m"] < mm["l_P_m"] for r_ in mm["by_coupling"]) and
        all(a["N_f_needed_for_payload"] > 1e13 for r_ in mm["by_coupling"] for a in r_["at_r_fit"]))
    chk("B15 CONTROL: a 1 eV wave sent into the SM-bound throat is below its binding energy (the binding test can "
        "pass as well as fail)", 1.602176634e-19 < HBAR * C * (mm["by_coupling"][1]["g"] ** 2) * 54 ** 2 /
        (256 * math.pi * mm["by_coupling"][1]["r_e_SM_max_m"]), control=True)
    sm_rows = cap["mmp_SM_throat"]
    chk("B16 the payload exceeds MMP's SM-embedded throat capacity by %.2g .. %.2g (V66-1: ~4e8 .. 4e9), not by the "
        "2.3e22 .. 2.7e23 of the board's 300 l_P throat" % (min(sm_rows[0]["payload_over_capacity"]),
                                                          max(sm_rows[0]["payload_over_capacity"])),
        3e8 < min(sm_rows[0]["payload_over_capacity"]) < 5e8 and 3e9 < max(sm_rows[0]["payload_over_capacity"]) < 5e9)
    # (C)
    q0 = qnec_table(0.0)
    q5 = qnec_table(0.5)
    chk("C1 QNEC |dS| over the throat sphere = (1 - b')/2 x capacity: 1/2 of the count at b' = 0",
        all(abs(r["qnec_dS_over_payload_bits"] - 0.5) < 1e-9 for r in q0["rows"]))
    chk("C2 ... and 1/4 at b' = 1/2 (geometry.qnec_price, nullinfo's expression)",
        all(abs(r["qnec_dS_over_payload_bits"] - 0.25) < 1e-9 for r in q5["rows"]))
    qc = geometry.qnec_price(1.0, 1.0)
    chk("C3 b'(r0) = 1 (no flare-out) prices zero", abs(qc["fraction_of_sheet_cap"]) < 1e-15, control=True)
    rq1, rq2 = geometry.r_quantum(cap["rows"][0]["r_fit_m"]), geometry.r_quantum(2 * cap["rows"][0]["r_fit_m"])
    chk("C4 R-QUANTUM fraction at r_fit < 1e-20 and scales as r^-2 (x2 radius -> /4)",
        rq1["fraction_covered"] < 1e-20 and abs(rq1["fraction_covered"] / rq2["fraction_covered"] - 4) < 1e-9)
    s = shape()
    flare = [s[k] for k in ("b=r0", "b=r0^2/r", "b=sqrt(r0 r)")]
    chk("C5 flare-out throats: theta(r0) = 0 and theta > 0 just outside (no light-sheet: H-CAP-AT-THROAT needed)",
        all(abs(f["theta(r0)"]) < 1e-12 and f["theta(1.01 r0)"] > 0 for f in flare))
    chk("C6 Minkowski ingoing congruence has theta < 0 (a light-sheet exists there)",
        s["CONTROL Minkowski ingoing theta at R=1"] < 0, control=True)
    # (D)
    chk("D1 PV (13) energy conservation re-derived from (11)-(12) (sympy)", pv_conservation())
    chk("D2 with the M/a sign in p flipped, conservation fails", not pv_conservation(True), control=True)
    pv = pv_static()
    chk("D3 sigma_0 < 0 for every sampled a_0 > 2M (PV p.3 'negative')", pv["sigma0_negative_all"])
    chk("D4 sigma_0 + p_0 = (3M/a_0 - 1)/(4 pi a_0 sqrt(1 - 2M/a_0)) exactly", pv["nec_closed_form_ok"])
    sg = pv["nec_sign_by_a0_over_M"]
    chk("D5 the shell's NEC fails for a_0 > 3M and holds for 2M < a_0 < 3M (a test that can pass both ways)",
        sg[2.5] == ">0" and sg[2.9] == ">0" and sg[3.1] == "<0" and sg[1e6] == "<0" and sg[3.0] == "=0")
    scan = pv_stability_scan([0.01, 0.25, 0.5, 1.0])
    chk("D6 PV p.3 reproduced: for 0 < beta_0^2 <= 1 no a_0/M in (2, 1e4] is stable", all(v is None
                                                                                           for v in scan.values()))
    ctrl = pv_stability_scan([-1.0, 4.0])
    chk("D7 region II (beta_0^2 = -1) and region I (beta_0^2 = 4) do contain stable radii",
        ctrl[-1.0] is not None and ctrl[4.0] is not None, control=True)
    rc = pv_root_check(4.0)
    chk("D8 PV (34)'s transcribed roots are zeros of (29)'s left side (beta_0^2 = 4)", rc is not None and
        max(rc) < 1e-9)
    lo, hi = pv_roots(4.0)
    chk("D9 region I's grid band lies inside (a_0^-, a_0^+) from (34)", lo <= ctrl[4.0][0] and ctrl[4.0][1] <= hi)
    chk("D10 discriminant of (34) real only outside (3/2 - sqrt3, 3/2 + sqrt3) (PV p.3)",
        pv_roots(3.0) is None and pv_roots(3.3) is not None and pv_roots(-0.3) is not None and pv_roots(-0.2) is None)
    ts = [thin_shell_at(r) for r in (1e-21, 1.0, 1e3)]
    chk("D11 shell mass at M = 0 is -16 pi x wormhole.throat_mass and -4 x M_sat, at three radii",
        all(abs(t["ratio_m_shell_over_throat_mass"] + 16 * math.pi) < 1e-9 and abs(t["ratio_over_M_sat"] + 4) < 1e-12
            for t in ts))
    # (E) board readings
    txt = m_ruling_text()
    chk("E1 ledger M-S1A-P3 carries M's clarification verbatim ('Singular occurs in the throat ...')",
        "Singular occurs in the throat where the geometry is compressed to binary information" in txt)
    hy = charter_hypothesis()
    chk("E2 CHARTER.md carries H-THROAT-BITS with its source M-S1A-P3", hy[0] is not None and "M-S1A-P3" in hy[1])
    spec = specthm_verdicts()
    chk("E3 specthm (z3, run time): S-1 NONEMPTY, S-2 / S-3 / Rec OPEN", spec["S-1"] == "NONEMPTY" and
        all(spec[k] == "OPEN" for k in ("S-2", "S-3", "Rec")))
    chk("E4 specthm: W-create-cc, W-create-ncc, W-enlarge OPEN; M-S1A-P3 ruled", all(
        spec[k] == "OPEN" for k in ("W-create-cc", "W-create-ncc", "W-enlarge")) and spec["_M-S1A-P3_ruled"])
    # (F) grades
    G = grades(spec)
    chk("F1 every grade cell uses the B-combine vocabulary; no bare REMOVED; every -IF names its premises",
        grade_audit(G) == [])
    planted = [dict(G[0], per=dict(G[0]["per"], **{"O-BITS": "REMOVED by throat compression"}))]
    chk("F2 a planted bare REMOVED on O-BITS is caught", grade_audit(planted) != [], control=True)
    planted2 = [dict(G[0], per=dict(G[0]["per"], **{"O-HOLD": "REMOVED-IF {H-THROAT-BITS}"}))]
    chk("F3 a planted member removal (REMOVED-IF {H-THROAT-BITS}) is caught as member-attributed",
        member_removals(planted2) != [], control=True)
    chk("F4 no removal credited to H-THROAT-BITS in the board's setting (no leading REMOVED-IF in any reading)",
        member_removals(G) == [])
    sr = setting_removals(G)
    chk("F4b the setting-bound removals (MQ in nearly-AdS2, MMP at sub-electroweak scale) each hold H-GJW-COUNTERPART "
        "-- M's reading load-bearing there -- and each names its setting (%d clauses)" % len(sr),
        len(sr) == 2 and all(x[3] is not None for x in sr) and all(x[1] == "O-HOLD" for x in sr))
    planted3 = [dict(G[2], per=dict(G[2]["per"], **{"O-HOLD": "LEFT-IF {X}; REMOVED-IF {H-GJW-COUNTERPART, Y} somewhere"}))]
    chk("F4c CONTROL a planted REMOVED-IF clause holding M's reading but naming no setting is caught",
        any(x[3] is None for x in setting_removals(planted3)), control=True)
    chk("F4d R-TELEPORT's O-HOLD leads with LEFT-IF for a hold on GJW alone (V66-0 #1), and its one-space payload clause "
        "names the OPEN pathway N_GJW-PAYLOAD", grade_word(G[2]["per"]["O-HOLD"]) == "LEFT-IF" and
        "OPEN via N_GJW-PAYLOAD" in G[2]["per"]["O-HOLD"])
    structural("F5 O-BITS is LEFT or LEFT-IF in every reading (restates the authored grades)",
               all(grade_word(g["per"]["O-BITS"]) in ("LEFT", "LEFT-IF") for g in G))
    structural("F6 O-SEAT stays OPEN (via N_S5) in every reading (restates the authored grades)",
               all(grade_word(g["per"]["O-SEAT"]) == "OPEN" and "N_S5" in g["per"]["O-SEAT"] for g in G))
    ite = d68_row("H-IT read as ER=EPR")
    chk("F7 the ITE / ITB cells quoted in R-TELEPORT / R-ITB are geometry.GRADES' own text (imported)",
        ite["per"]["O-MAKE-TOPO"] in G[2]["per"]["O-MAKE-TOPO"] and
        d68_row("H-IT read as an information layer")["per"]["O-HOLD"] in G[4]["per"]["O-HOLD"])
    # sources
    chk("F8 every outside reading records its route and status", all(r["route"] and r["status"].startswith("READ")
                                                                    for r in READ))
    longest = max(len(u.split()) for r in READ for u in r["used"])
    chk("F9 every 'used' line is short (<= 30 words; copyrighted text stays out)", longest <= 30)
    structural("the grades' seat-condition text names specthm's run-time verdicts (built from them)",
               all(spec["S-2"] in g["seat_conditions"] for g in G))
    structural("measure.py's counts are imported, so A1/A2 compare an owner with its own printed report",
               True)
    print("\n%d counted checks: %d pass, %d fail; %d controls; %d STRUCTURAL not counted"
          % (n["pass"] + n["fail"], n["pass"], n["fail"], n["control"], n["structural"]))
    return n["fail"] == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(report_data(), indent=1, default=str))
    else:
        report()
