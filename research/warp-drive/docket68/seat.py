#!/usr/bin/env python3
"""seat.py -- DOCKET 68 wave 2, work item W2C-seat: the S5 seat route made as concrete as the board allows.

Not seated.  Nothing here edits the board: every board figure is IMPORTED from the instrument that owns it (stock,
stockgate, formation, massform, foliation, transit, nopath, ladder, branelink; docket68's measure and settle), never
retyped.  Outside numbers are READ at source with the route recorded beside each (M-RULINGS items 15-16).

    python3 seat.py              report
    python3 seat.py --selftest   checks: CONTROL (built so that a wrong input fails), GROUND (a board value read and
                                 compared), STRUCTURAL (cannot fail by construction: printed, never counted)
    python3 seat.py --json       the report's numbers as JSON

THE QUESTION (M-RULINGS item 7, verbatim M: "S5 counts (Recommended)").  O-SEAT -- the supply of substance at the seat
(O-MATTER relocated by M's ruling item 5, "Yes, from the seat") -- is OPEN via S5 (reconstruction from stock at the
destination) and the D25 stock gate, until both are shown.  This file asks, for the 70 kg payload (stock.HUMAN) at
Proxima, what each half of that pathway would have to be, on the board's data and on outside data READ this pass.

WHAT IT COMPUTES
  A. What the destination must hold, element by element: 70 kg x stock.HUMAN's mass fractions (grams per element), the
     stock mass each element alone demands at each of the board's stocks (stockgate.DESTS), and the binder.  Beside it,
     what is MEASURED for each element anywhere in the Proxima system in the sources READ: nothing for any body; for
     the stars, Proxima's iron only (a spread), alpha Cen AB's 21 species (Morel 2018), and -- W2-fix -- N in alpha
     Cen A, which the literature summarised by Porto de Mello, Lyra & Keller 2008 finds solar ([N/Fe] ~ 0; READ p.12,
     Fig. 8 p.14; the primary studies NAMED-NOT-READ).  The binder P is measured in no star of the system and in no
     body in the sources read; N is measured in no body.  Wave 2 first said: 'The binder P and the CI runner-up N are
     measured in no star of the system and in no body' -- wrong for N in alpha Cen A.
  B. D25's gate at Proxima, conjunct by conjunct (stockgate.GATE; formation.gate imported), with Proxima b's MINIMUM
     mass m sin i READ at source (Faria 2022; the inclination is unknown, the planet does not transit, so every ratio
     built on it is a floor) and Brugger 2016's interior range READ (water only: it models core, mantles and water, no
     C, N or P, so it leaves the primitive conjunct unconstrained); and, element by element, which elements fail
     the CI mass threshold if the body is DEVOLATILISED rather than primitive (stockgate's crust as the board's only
     devolatilised stock).
  C. The fabricator, survey and receiver (D23): their earliest arrival (the light time), the survey's earliest report
     home, and the amortisation identity -- with the reconstruction's energy E_rec and the setup mass m_set both OPEN,
     the number of later reconstructions at which S5 beats sending the payload at the same speed is
     k* = m_set (gamma-1) c^2 / (m_pay (gamma-1) c^2 - E_rec), which reduces to m_set / m_pay as E_rec -> 0 (sympy);
     and there is no k* at all once E_rec >= m_pay (gamma-1) c^2.  That ceiling is the one number DOCKET 56's instrument
     would have to come in under.
  D. The information that must arrive (measure.price_table, imported) against the channels: teleportation (transit:
     2 classical bits per qubit, at c), and the drift channel (settle, imported: pairs per teleported qubit, the
     window on the READ Weinberg-family limits, first-transit times).  And a FLOOR on the classical channel's RECEIVED
     energy for N bits over a DECLARED time T, from Lachmann-Newman-Moore eq. (8) (READ) -- at one polarisation it is
     exactly the channel law the O6/O7 pass used for S5 (branelink.py's A(N), read from its source) -- with LNM's
     eq. (6) beside it as context (outside its many-mode regime at Proxima with 100 m dishes).
  E. DOCKET 56's owed instrument, stated as the list of quantities it would have to compute, each marked COMPUTED-HERE
     (conditional), IMPORTED, or NOT COMPUTED ANYWHERE.
  F. O-SEAT's grade, by a predicate whose control can move it.

NAMED HYPOTHESES (every limitation carried by name)
  H-PAYLOAD      the payload is stock.HUMAN (14 elements, ICRP Reference Man as the board holds it) x 70 kg.  stockgate's
                 'as-composed 59' (the D25 row's own payload) is computed beside it; the binder agrees (P).
  H-STOCK-PROXY  a body at Proxima has the composition of one of the board's stocks (CI chondrite, the Sun's hybrid
                 photosphere, Earth's continental crust).  No composition of any Proxima-system body is measured.
  H-ACEN-RATIO   (only in the alpha-Cen-adjusted CI column) a primitive body at Proxima carries CI composition scaled by
                 alpha Cen A's [X/Fe] where Morel 2018 measures it; for N, [N/Fe] ~ 0 as MEASURED (literature, 'solar':
                 Porto de Mello et al. 2008 p.12, READ; W2-fix); and [X/Fe] = 0 as an assumption where nothing is
                 measured (P among them).  Wave 2 first said N was 'unmeasured, set 0'; the number is the same (0), its
                 status is not.  Rests on
                 H-CONATAL (Proxima co-natal with alpha Cen AB: Kervella 2017 READ (abstract) shows the triple BOUND;
                 Morel 2018 p.16 says co-natal formation is 'still not completely settled').
  H-BODY-ACCESS  the 'accessible mass' of a planet is unmeasured; a planet's total mass is not its accessible mass.
  H-DEVOL-PROXY  stockgate's CRUST stands in for a devolatilised body (the board's only devolatilised stock).
  H-KINETIC      the comparator 'send the payload at v' costs (gamma-1) m c^2 and the setup the same per kg; no
                 deceleration, no propellant (the rocket equation would raise BOTH sides; neither is favoured here).
  H-EM-CARRIER   the classical channel is electromagnetic, optimally coded (Lachmann-Newman-Moore's ideal, an upper
                 limit on rate, so a lower limit on energy), with DECLARED apertures (branelink.DISH_D, the board's EM
                 control-link dish, 100 m, at both ends) and a DECLARED transmission time T.
  H-ONE-POL      branelink's A(N) is LNM eq. (8) with ONE polarisation (half LNM's mode density); LNM count two.
  H-FEW-MODES    the 1D figures floor the RECEIVED energy only if the link uses at most one transverse mode (true of
                 free space at 100 m dishes and Proxima's distance, computed); transmitted energy, diffraction loss
                 included, is not floored here.
  H-MODE-CONTINUUM  LNM eq. (6)'s assumption (a continuum of transverse modes); it fails at Proxima with 100 m dishes.
  H-CHECK-AT-ORIGIN  the gate is checked at the origin before a specification is committed (then the survey report must
                 come home: 2 D / c).  If the fabricator decides locally, the report need not travel back.
  H-C2, H-MAP, H-TRANSFER, H-SPIN, H-DILUTION, F1   the drift channel's own hypotheses, carried from settle.py unchanged.
  H-FAITHFUL, H-GRID, H-THERMO, H-RHO, H-ERASE      measure.py's counting hypotheses, carried unchanged.

READ THIS PASS (routes recorded; short phrases only, page given)
  Faria et al. 2022, arXiv:2202.05188v1 -- READ via alphaXiv, Table C.1 p.17 and p.9: Proxima b m_p sin i
      '1.07 +0.06 -0.06' M_earth (TM RVs, adopted), a = '0.04856' au, P = 11.1868 d; Proxima d (candidate)
      0.26 +- 0.05 M_earth at 0.02885 au; Table 1 p.2: M_star = 0.1221 +- 0.0022 M_sun; p.9: Proxima b 'has not been
      found to transit'.
  Brugger, Mousis, Deleuil & Lunine 2016, arXiv:1609.09757v3 -- READ via alphaXiv, pp.1-5: radius '0.94-1.40 R_earth'
      for a solid Proxima b; water mass fraction from 0 to 50 % (their cap); 'Lacking detailed elementary abundances of
      the host star ... we base our model on solar system values' (p.1); a completely dry planet only for in-situ pebble
      accretion, the other scenarios 'predict a planet containing a significant amount of water and/or volatiles' (p.5);
      the star's [Fe/H] = 0.21 as they quote it (p.5).
  Morel 2018, arXiv:1805.00929v1 -- READ via alphaXiv, Table 1 p.7 (alpha Cen A and B, [X/Fe] before GCE), p.8 (C/O
      1.18 and Mg/Si 0.98 / 1.02 relative to solar), p.16 (Proxima's [Fe/H] in four studies, +0.16 to -0.07; Pavlenko
      2017's Na, Ti, Fe 'roughly consistent with solar'; co-natal formation 'not completely settled').  The 21 species
      do NOT include P, N, S, K or Cl.
  Kervella, Thevenin & Lovis 2017, arXiv:1611.03495 -- READ (abstract) via Firecrawl research inspect: Proxima and
      alpha Cen 'are gravitationally bound with a high degree of confidence'; period ~550 000 yr.
  Lachmann, Newman & Moore 1999, arXiv:cond-mat/9907500v1 -- READ via alphaXiv, eq. (6) p.6 (three-dimensional:
      rate from power, apertures and distance; '1.61 x 10^21 bits per second' at 1 m^2, 1 m, 1 J/s) and eq. (8) p.7
      (one-dimensional: '2.03 x 10^17 bits per second' at 1 J/s); both are upper limits on rate for a given power.
  Bekenstein 1981, PRL 46, 623 -- READ (abstract) via Firecrawl scrape of the publisher's public abstract page: the
      bound 'prescribes the minimum energy cost for information transferred over a given time interval'.  The abstract
      prints no coefficient; the coefficient used here is LNM's (READ), not Bekenstein's.

  W2-fix (2026-10-04; the re-verifications W2V-0 / W2V-1 of wave2/WAVE2-RESULT.json, key result.verify), READ via
  alphaXiv: Porto de Mello, Lyra & Keller 2008, arXiv:0804.3712v2, p.12 ('C, N and O abundance ratios of alpha Cen A
      are solar', a literature summary), Table 4 p.12 (their own species: no N, no P), Fig. 8 p.14 (N plotted for
      alpha Cen A); Hinkel & Kane 2013, arXiv:1304.0450v1, p.2 (Laird 1985 measured C and N in A and B; [N/Fe] offset
      -0.65 dex, excluded) and Table 1 p.4 (no N, no P); Brugger 2016 re-READ (p.1 the five layers -- no C, N, P;
      Table 1 p.2 Earth's parameters; p.1 and p.3 masses 1.10-1.46 M_earth at sin i = 1); Faria 2022 Table 1 p.2
      re-READ (parallax 768.50 +- 0.20 mas, 1.3012 +- 0.0003 pc, ref. Gaia Collaboration 2016).

HISTORY KEPT.  Wave 5 (M-combine) graded O-SEAT 'LEFT' in every variant with the {S10, S13} restriction unnamed; wave 6
(F-alone) named that restriction H-SEAT-ROUTES and graded O-SEAT OPEN via N_S5; M then ruled 'S5 counts' (item 7).
measure.seat_route_s5 already priced the D25 mass conjunct for stockgate's 59-element payload (749.1 kg CI, 1.338e5 kg
photosphere); this file does not re-price it, it asks what the rest of the pathway needs.  formation.py carries Proxima
b at 1.3 M_earth (Anglada 2017 sec. 1, second-hand; 'kept as read'); this pass READS Faria 2022 at source (1.07).
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
for _p in (WD, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import stock
    import stockgate
    import formation
    import massform
    import foliation
    import transit
    import nopath
    import ladder
    import branelink
    import measure
    import settle

LN2 = math.log(2.0)
C = foliation.C_LIGHT
G = foliation.G_NEWTON
M_SUN = foliation.M_SUN
LY = foliation.LY
D_PROXIMA = settle.L_PROXIMA_PHASE1        # phase1.L_PROXIMA via settle (W2-fix); wave 2: foliation.proxima_span_m()
YEAR_S = LY / C                      # the Julian year implied by the light-year the board uses
HBAR = branelink.HBAR
H = branelink.HPL
M_EARTH = ladder.M_EARTH
AU = settle.AU_M
PAYLOAD_KG = massform.PAYLOAD_KG     # 70.0, asked of stock.feedstock_kg's default by massform

# ============================================================================ READ data (routes above)
FARIA_2022 = {
    "source": "arXiv:2202.05188v1", "route": "READ via alphaXiv, Table C.1 p.17, Table 1 p.2, p.9",
    # 'b_msini_earth' is M_p sin i, the MINIMUM mass (Table C.1 p.17; p.9 'the minimum mass of this planet is estimated
    # as 1.07 +- 0.06'); the inclination is unknown (no transit, p.9), so the true mass is >= it.
    "b_mass_is_minimum": True,
    "parallax_mas": (768.50, 0.20), "distance_pc": (1.3012, 0.0003),   # Table 1 p.2 (ref. Gaia Collaboration 2016)
    "b_msini_earth": (1.07, 0.06), "b_a_au": 0.04856, "b_P_days": 11.1868,
    "d_msini_earth": (0.26, 0.05), "d_a_au": 0.02885, "d_status": "candidate",
    "M_star_sun": (0.1221, 0.0022), "b_transits": False,
}
BRUGGER_2016 = {
    "source": "arXiv:1609.09757v3", "route": "READ via alphaXiv, pp.1-5 (re-READ W2-fix: p.1 layers, Table 1 p.2, p.3)",
    "radius_earth": (0.94, 1.40), "water_mass_fraction": (0.0, 0.50),
    # W2-fix: the model's layers are a Fe/FeS core, two silicate mantles, high-pressure ice and liquid water (p.1-2),
    # with Earth's compositional parameters (Table 1 p.2): it carries NO C, N or P, so it neither admits nor excludes
    # the CI volatile budget the primitive conjunct tests.  Its radii are computed at m = 1.10-1.46 M_earth with
    # sin i = 1 (p.1, p.3: Anglada 2016's minimum mass), not at Faria's 1.07.
    "layers": ("core: Fe + FeS", "lower mantle: perovskite + magnesiowustite", "upper mantle: olivine + enstatite",
               "high-pressure water ice", "liquid water"),
    "models_C_N_P": False, "masses_modelled_earth": (1.10, 1.27, 1.46), "sin_i_set": 1.0,
    "host_abundances_used": False,     # 'Lacking detailed elementary abundances of the host star' (p.1)
    "dry_only_if": "in-situ pebble accretion (one of four formation scenarios, p.5)",
}
#: W2-fix: Proxima's distance is IMPORTED from the board's owner, phase1.L_PROXIMA (Gaia DR3 parallax 768.066539 mas,
#: READ via restatement, DOCKET 67), through settle (one import, never typed).  Wave 2 first used foliation's 4.2465 ly
#: (phase1's value rounded to four decimals).  Faria 2022 Table 1 p.2 prints 768.50 +- 0.20 mas (4.2441 ly from that
#: parallax) and 1.3012 pc (4.2439 ly, rounded): both READ values are recorded in settle.PROXIMA_DISTANCES_READ, the
#: discrepancy (0.056 % from Faria's parallax, 2.17 sigma on Faria's error alone; 0.059 % against the printed pc)
#: computed by settle.proxima_distances().  W2-fix first wrote '(1.3012 pc, 4.2439 ly)' beside the 0.056 %.
#: Porto de Mello, Lyra & Keller 2008, arXiv:0804.3712v2 -- READ via alphaXiv (W2-fix, 2026-10-04): p.12 'The available
#: literature data also suggests that the C, N and O abundance ratios of alpha Cen A are solar'; Fig. 8 p.14 (alpha Cen
#: A, six studies, N plotted; caption: 'C, N, O ... are normal'); their own Table 4 p.12 carries no N and no P.
#: Hinkel & Kane 2013, arXiv:1304.0450v1 -- READ via alphaXiv: p.2 Laird (1985) 'determined the carbon and nitrogen
#: abundances' in both stars, with '[N/Fe] by -0.65 dex' offset 'as a result of their stellar atmospheres being too cool',
#: and excluded it; their five-catalog Table 1 p.4 carries no N and no P.
PORTO_DE_MELLO_2008 = {
    "source": "arXiv:0804.3712v2", "route": "READ via alphaXiv (answer_pdf_queries), p.12, Table 4 p.12, Fig. 8 p.14",
    "N_alphaCenA": "solar ([N/Fe] ~ 0) -- 'the available literature data also suggests' (a summary of others' "
                   "measurements; the primary studies, e.g. Edvardsson 1988 in Fig. 8, NAMED-NOT-READ)",
    "N_XFe_carried": 0.0, "N_status": "MEASURED in the literature (qualitative 'solar'; no number printed in the text)",
    "own_table_has_N": False, "own_table_has_P": False}
HINKEL_KANE_2013 = {
    "source": "arXiv:1304.0450v1", "route": "READ via alphaXiv (answer_pdf_queries), p.2, Table 1 p.4",
    "Laird_1985": "C and N in alpha Cen A and B (primary NAMED-NOT-READ); [N/Fe] offset -0.65 dex (atmospheres too "
                  "cool), excluded by Hinkel & Kane", "table1_has_N": False, "table1_has_P": False}
#: P in the Proxima system: absent from every source read (Morel 2018 Table 1; Porto de Mello 2008 Table 4; Hinkel &
#: Kane 2013 Table 1).  The verifier W2V-1 also READ Maas 2017 (1704.08282, Table 1: no P) and a Hypatia P sample
#: (2608.30484 p.3: 11-463 pc, so no alpha Cen); those two are cited as the verifier's reads, not re-read here.
P_MEASURED_IN_PROXIMA_SYSTEM = False
#: Morel 2018 Table 1 p.7, [X/Fe] BEFORE the GCE correction, and [Fe/H].  None = not measured for that star.
MOREL_2018 = {
    "source": "arXiv:1805.00929v1", "route": "READ via alphaXiv, Table 1 p.7; p.8; p.16",
    "FeH": {"A": 0.237, "B": 0.221},
    "XFe": {"C": (0.025, -0.001), "O": (-0.046, -0.074), "Na": (0.094, 0.128), "Mg": (0.013, 0.044),
            "Al": (0.044, 0.077), "Si": (0.024, 0.034), "Ca": (-0.020, 0.001), "Sc": (0.029, 0.036),
            "Ti": (0.016, 0.063), "V": (0.019, 0.073), "Cr": (0.011, 0.043), "Mn": (0.034, None),
            "Co": (0.051, -0.019), "Ni": (0.049, 0.057), "Cu": (0.058, 0.070), "Zn": (0.029, 0.075),
            "Y": (-0.034, 0.047), "Zr": (0.033, 0.122), "Ba": (-0.052, -0.042), "Ce": (-0.065, None)},
    "printed_C_over_O": {"A": 1.18, "B": 1.18}, "printed_Mg_over_Si": {"A": 0.98, "B": 1.02},
    "proxima_FeH_studies": {"Neves+2014": (0.16, 0.20), "Maldonado+2015": (-0.03, 0.09),
                            "Passegger+2016": (-0.07, 0.14), "Zhao+2018": (0.08, 0.12)},
    "proxima_FeH_status": "restated by Morel 2018 p.16 (the four studies themselves NAMED-NOT-READ)",
    "proxima_other": "Na, Ti, Fe 'roughly consistent with solar' (Pavlenko 2017, restated p.16; NAMED-NOT-READ)",
}
KERVELLA_2017 = {"source": "arXiv:1611.03495", "route": "READ (abstract) via Firecrawl research inspect",
                 "bound": True, "period_yr": 550000}
LNM_1999 = {"source": "arXiv:cond-mat/9907500v1", "route": "READ via alphaXiv, eq. (6) p.6, eq. (8) p.7",
            "eq6_fixture_bits_s": 1.61e21, "eq8_fixture_bits_s": 2.03e17}
BEKENSTEIN_1981 = {"source": "PRL 46, 623 (1981)", "route": "READ (abstract) via Firecrawl scrape of the "
                   "publisher's public abstract page (journals.aps.org/prl/abstract/10.1103/PhysRevLett.46.623)",
                   "coefficient_printed_in_abstract": False}


# ============================================================================ A. what the destination must hold
def payload_grams(payload=None, kg=PAYLOAD_KG):
    p = stock.HUMAN if payload is None else payload
    return {e: f * kg * 1000.0 for e, f in p.items()}


def per_element_stock(payload=None, kg=PAYLOAD_KG):
    """{dest: {element: kg of that stock which element e alone demands}} on stockgate's destinations (imported).
    inf where the stock lacks the element (a different failure from scarcity, stock.processing_factors' rule)."""
    p = stock.HUMAN if payload is None else payload
    out = {}
    for d in ("CI chondrite", "stellar photosphere", "Earth cont. crust", "Jupiter (3x solar)"):
        f = stock.processing_factors(p, stockgate.DESTS[d]())
        out[d] = {e: kg * v for e, v in f.items()}
    return out


def binders(payload=None):
    p = stock.HUMAN if payload is None else payload
    rows = {}
    for d in ("CI chondrite", "stellar photosphere", "Earth cont. crust", "Jupiter (3x solar)"):
        ranked = sorted(stock.processing_factors(p, stockgate.DESTS[d]()).items(), key=lambda kv: -kv[1])
        rows[d] = ranked[:3]
    return rows


def proxima_measured():
    """For each payload element: is it measured in Proxima's photosphere, in alpha Cen A/B, in any Proxima-system body,
    on the sources READ?  (Stars are not the gate's stock -- the gate's first conjunct excludes gas -- so a stellar
    abundance only constrains what a body might hold, through H-CONATAL and a formation model.)"""
    rows = {}
    for e in stock.HUMAN:
        acen = e == "Fe" or e in MOREL_2018["XFe"]
        rows[e] = {"proxima_photosphere": "Fe (four studies, +0.16 to -0.07, restated)" if e == "Fe" else
                   ("'roughly solar' (restated, NAMED-NOT-READ)" if e == "Na" else "not measured in sources read"),
                   "alpha_Cen_AB": "measured (Morel 2018)" if acen else
                   ("reference element (H)" if e == "H" else
                    ("measured in alpha Cen A in the literature: solar, [N/Fe] ~ 0 -- a qualitative literature "
                     "summary, which the source says the data 'suggests' (Porto de Mello et al. 2008 p.12, READ; "
                     "primaries NAMED-NOT-READ); in conflict, Laird 1985 measured N in A and B with [N/Fe] offset "
                     "-0.65 dex, which Hinkel & Kane 2013 p.2 (READ) attribute to atmospheres too cool and exclude "
                     "(Laird's primary NAMED-NOT-READ). NOT among Morel 2018's 21 species" if e == "N" else
                     "NOT measured in any source read (not among Morel 2018's 21 species, Porto de Mello 2008 "
                     "Table 4 or Hinkel & Kane 2013 Table 1)")),
                   "any_body": "not measured (no composition of any Proxima-system body exists in the sources read)"}
    return rows


def acen_adjusted_ci(star="A"):
    """H-ACEN-RATIO: CI scaled by alpha Cen [X/Fe] (Morel 2018, READ) where measured, 0 elsewhere; renormalised.
    Returns stock.HUMAN's factors against it and the unadjusted ones."""
    i = 0 if star == "A" else 1
    ci = stockgate.DESTS["CI chondrite"]()
    adj = {}
    for e, s in ci.items():
        x = MOREL_2018["XFe"].get(e, (0.0, 0.0))[i]
        adj[e] = s * 10.0 ** (x if x is not None else 0.0)
    t = sum(adj.values())
    adj = {e: v / t for e, v in adj.items()}
    return stock.processing_factors(stock.HUMAN, adj), stock.processing_factors(stock.HUMAN, ci)


# ============================================================================ B. D25's gate at Proxima
def gate_conjuncts():
    """The gate's conjuncts at Proxima on the board's data and on READ data.  True / False / None (= unmeasured)."""
    need = {d: stock.feedstock_kg(PAYLOAD_KG, stock.HUMAN, stockgate.DESTS[d]())
            for d in ("CI chondrite", "stellar photosphere")}
    b_kg = FARIA_2022["b_msini_earth"][0] * M_EARTH
    return {
        "aperture": formation.APERTURE_STATUS,
        "condensed body named": formation.SURVEY_CONDENSED_BODY_FOUND,
        "condensed body (READ this pass)": "Proxima b, m sin i = %.2f +- %.2f M_earth at a = %.5f au (Faria 2022); "
                                           "Proxima d candidate %.2f M_earth at %.5f au" % (
                                               *FARIA_2022["b_msini_earth"], FARIA_2022["b_a_au"],
                                               FARIA_2022["d_msini_earth"][0], FARIA_2022["d_a_au"]),
        "primitive": None, "primitive (board)": formation.SURVEY_PRIMITIVE_MEASURED,
        "primitive (READ)": "unmeasured and UNCONSTRAINED by Brugger 2016: it admits a water mass fraction 0-50 % "
                            "(dry only for in-situ pebble accretion) but models water only -- core, mantles, ice, "
                            "liquid water, no C, N or P -- so it neither admits nor excludes the CI volatile budget "
                            "the primitive conjunct tests (its radii are at 1.10-1.46 M_earth with sin i = 1, not "
                            "Faria's 1.07).  Wave 2 first said 'both a primitive and a devolatilised body remain "
                            "admitted'",
        "accessible": None, "accessible (board)": formation.SURVEY_ACCESSIBLE_MEASURED,
        "mass threshold kg (stock.HUMAN, CI / photosphere)": need,
        "Proxima b minimum mass m sin i kg (READ; true mass >= it)": b_kg,
        "minimum mass over CI threshold, a floor (NOT accessible mass: H-BODY-ACCESS)": b_kg / need["CI chondrite"],
        "composition of any body": None,
        "formation.gate, synthetic aperture around b": formation.gate(
            (FARIA_2022["b_a_au"], 0.01), [(FARIA_2022["b_a_au"], True, None, b_kg)],
            pkind="as-composed 59", dkind="CI chondrite"),
        "formation.gate, no aperture": formation.gate(None, [(FARIA_2022["b_a_au"], True, None, b_kg)]),
    }


def devolatilised_failures(budget_dest="CI chondrite", body_dest="Earth cont. crust"):
    """H-DEVOL-PROXY: at the budget the gate sets for a PRIMITIVE (CI) body, which payload elements a DEVOLATILISED body
    of the same accessible mass fails to supply.  Each failing element with its factor and its Lodders T_c
    (stockgate.TCOND, imported).  This is the primitive conjunct's content, element by element."""
    budget = stock.binding_element(stock.HUMAN, stockgate.DESTS[budget_dest]())[1]
    f = stock.processing_factors(stock.HUMAN, stockgate.DESTS[body_dest]())
    fails = sorted(((e, v, stockgate.TCOND.get(e)) for e, v in f.items() if v > budget), key=lambda r: -r[1])
    return budget, fails


# ============================================================================ C. fabricator, survey, receiver (D23)
def setup_times(v_fracs=(1.0, 0.2, 0.1, 0.01)):
    """Earliest arrival of anything sent from the origin at speed v = beta c (D23: at <= c).  beta values below 1 are
    DECLARED illustrations, not designs."""
    rows = []
    for b in v_fracs:
        t = D_PROXIMA / (b * C) / YEAR_S
        rows.append({"beta": b, "arrival_yr": t, "survey_report_home_yr (H-CHECK-AT-ORIGIN)": t + D_PROXIMA / C / YEAR_S})
    return rows


def breakeven_symbolic():
    """k* from  m_set K + k E_rec < k m_pay K,  K = (gamma-1) c^2 (H-KINETIC).  sympy: the solution and its limit."""
    import sympy as sp
    k, ms, mp, K, E = sp.symbols("k m_set m_pay K E_rec", positive=True)
    kstar = sp.solve(sp.Eq(ms * K + k * E, k * mp * K), k)[0]
    lim = sp.limit(kstar, E, 0)
    return kstar, lim, sp.simplify(lim - ms / mp) == 0


def breakeven(m_set, beta, E_rec):
    """Numeric k* (None if E_rec >= the per-trip comparator: S5 never pays back)."""
    K = (1.0 / math.sqrt(1.0 - beta ** 2) - 1.0) * C ** 2
    per_trip = PAYLOAD_KG * K
    if E_rec >= per_trip:
        return None
    return m_set * K / (per_trip - E_rec)


def erec_ceiling(betas=(0.2, 0.1, 0.01)):
    """The per-reconstruction energy below which S5 can ever pay back against sending the payload at beta c."""
    return {b: PAYLOAD_KG * (1.0 / math.sqrt(1.0 - b ** 2) - 1.0) * C ** 2 for b in betas}


def receiver_and_fabricator():
    rows, _, _, ob = measure.price_table()
    return {"atoms_to_place": ob["atoms"], "species_bits_per_atom": ob["species_bits_per_atom"],
            "counts": [{k: r[k] for k in ("count", "bits", "bekenstein_floor_J_R1m", "landauer_J_310K",
                                          "classical_bits_to_teleport_if_qubits")} for r in rows],
            "payload_rest_energy_J": massform.rest_energy_j()}


# ============================================================================ D. information against the channels
def n_pairs_min():
    """Smallest number of drift pairs that can carry one teleported qubit's 2 bits (settle.D_needed, imported)."""
    n = 1
    while settle.D_needed(n) is None:
        n += 1
    return n


def drift_window_proxima():
    try:
        w = settle.window_read(L_list=(("Proxima (foliation span)", D_PROXIMA),), N_list=(n_pairs_min(),))
        return [{k: r[k] for k in ("L", "N", "reading", "window", "eps_any", "eps_max", "bound_used")}
                for r in w["rows"]]
    except Exception as exc:          # settle is shared with a concurrent wave-2 item; report, never mask
        return [{"error": repr(exc)}]


def information_vs_channels():
    rows, _, _, _ = measure.price_table()
    npair = n_pairs_min()
    out = []
    for r in rows:
        q = r["bits"]                                  # read as qubits under H-FAITHFUL (log2 d >= bits)
        out.append({"count": r["count"], "bits": q,
                    "teleport_classical_bits": r["classical_bits_to_teleport_if_qubits"],
                    "teleport_ebits_predistributed": q,
                    "drift_pairs_total (1 + N_min per qubit)": q * (1 + npair)})
    one_end = settle.first_transit_times(D_PROXIMA, 0.0, source="one-end")
    mid = settle.first_transit_times(D_PROXIMA, 0.0, source="midpoint")
    # the drift time at the LARGEST eps the tightest READ (abstract) Weinberg-family limit permits, both H-MAP readings
    # (settle.drift_time_needed, imported): an upper limit measured consistent with zero, so this is the SHORTEST drift
    # time not excluded, never a found one.
    tdrift = {}
    try:
        f = min(v["f_Hz"] for v in settle.BOUNDS_WEINBERG.values() if v.get("f_Hz"))
        for lab, eps in settle.eps_readings(f).items():
            tdrift[lab] = settle.drift_time_needed(npair, eps)
    except Exception as exc:
        tdrift["error"] = repr(exc)
    # S5's case (D23 as corrected): every resource starts at ONE end.  A midpoint source must itself first be carried
    # to the midpoint at <= c, so the earliest read is D/2c (source) + D/2c (pairs) + T_drift >= D/c.
    shipped_mid_read_s = D_PROXIMA / (2 * C) + D_PROXIMA / (2 * C)
    return {"per_count": out, "N_min_pairs_per_qubit": npair, "CMAX_bits_per_pair": settle.CMAX,
            "teleport_arrival_after_sending_yr": transit.arrival_time(D_PROXIMA) / YEAR_S,
            "teleport_advantage_over_light_s": transit.advantage_over_light(D_PROXIMA),
            "first_transit_one_end_zero_drift": one_end, "first_transit_midpoint_zero_drift": mid,
            "drift_time_at_READ_eps_max_s": tdrift,
            "midpoint_source_shipped_from_origin_earliest_read_yr (+ T_drift)": shipped_mid_read_s / YEAR_S,
            "drift_window_on_READ_limits": drift_window_proxima()}


# ---- the classical channel's energy floor (LNM, READ)
def lnm_rate_1d(P, pol=2):
    """LNM eq. (8): dS/dt = sqrt(4 pi^2 P / (3 h)) nats/s for two polarisations; per polarisation the mode density
    halves (H-ONE-POL), dS/dt = sqrt(2 pi^2 P / (3 h)) (pol=1).  Returned in bits/s."""
    return math.sqrt(2.0 * pol * math.pi ** 2 * P / (3.0 * H)) / LN2


def lnm_rate_3d(P, At, Ar, d):
    """LNM eq. (6): dS/dt = [512 pi^4 / (1215 h^3 c^2) * At Ar / d^2 * P^3]^(1/4) nats/s, returned in bits/s."""
    return (512.0 * math.pi ** 4 / (1215.0 * H ** 3 * C ** 2) * At * Ar / d ** 2 * P ** 3) ** 0.25 / LN2


def lnm_temperature_3d(P, At, Ar, d):
    """LNM eq. (5): T^4 = 15 h^3 c^2 / (2 pi^4) * d^2 / (At Ar) * P, the apparent temperature (energy units)."""
    return (15.0 * H ** 3 * C ** 2 / (2.0 * math.pi ** 4) * d ** 2 / (At * Ar) * P) ** 0.25


def power_for_rate(rate_bits, fn, lo=1e-40, hi=1e60, **kw):
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if fn(mid, **kw) >= rate_bits:
            hi = mid
        else:
            lo = mid
    return hi


def channel_floor(N_bits, T_s, dish=branelink.DISH_D, d=D_PROXIMA):
    """Energy (J) to send N bits in time T at distance d (H-EM-CARRIER).
      1D (LNM eq. 8; one polarisation = H-ONE-POL, the O6/O7 pass's law; two = LNM as printed): a FLOOR on the energy
         RECEIVED, provided the link uses at most one transverse mode (H-FEW-MODES) -- which free space at these dishes
         enforces: the mode count at LNM's apparent temperature is below 1 in every case computed.
      3D (LNM eq. 6, two dishes of diameter `dish`): LNM's geometric bound; it assumes a continuum of transverse modes
         (H-MODE-CONTINUUM), which FAILS here (< 1 mode), so it is printed as CONTEXT, not as a floor.  What the
         TRANSMITTED energy must be at these dishes (diffraction loss included) is NOT established here.
    Every figure is for that T only: E falls as T grows (1D as 1/T, 3D as T^(-1/3)) -- it prices a schedule, not the
    route, and S5's transfer has no energy floor independent of T."""
    A = math.pi * (dish / 2.0) ** 2
    R = N_bits / T_s
    P1 = power_for_rate(R, lnm_rate_1d, pol=1)
    P2 = power_for_rate(R, lnm_rate_1d, pol=2)
    P3 = power_for_rate(R, lnm_rate_3d, At=A, Ar=A, d=d)
    kT = lnm_temperature_3d(P3, A, A, d)
    modes = A * A * kT ** 2 / (d ** 2 * H ** 2 * C ** 2)      # LNM p.5: rho(eps) per polarisation x eps, at eps = kT
    return {"N_bits": N_bits, "T_s": T_s, "E_1d_one_pol_J": P1 * T_s, "E_1d_two_pol_J": P2 * T_s,
            "E_3d_J": P3 * T_s, "kT_3d_MeV": kT / (1.602176634e-13), "transverse_modes_at_kT": modes, "dish_m": dish}


def branelink_law_matches_one_pol():
    """Read branelink.py's A(N) expression from its SOURCE (never retyped) and compare, symbolically, with LNM eq. (8)
    at one polarisation: E T = A, N bits in T  =>  A = 3 hbar N^2 ln^2 2 / pi."""
    import sympy as sp
    src = open(os.path.join(WD, "branelink.py"), encoding="utf-8").read()
    m = re.search(r"A_of_N = lambda n: (.+)\n", src)
    if not m:
        return None, None
    n, hb = sp.symbols("n hbar", positive=True)
    expr = sp.sympify(m.group(1).replace("sp.", ""), locals={"hb": hb, "n": n, "log": sp.log, "pi": sp.pi})
    P, T, h = sp.symbols("P T h", positive=True)
    # one polarisation: (n ln2 / T)^2 = 2 pi^2 P / (3 h)  ->  P;  A = P T^2;  h = 2 pi hbar
    Psol = sp.solve(sp.Eq((n * sp.log(2) / T) ** 2, 2 * sp.pi ** 2 * P / (3 * h)), P)[0]
    A_lnm = sp.simplify((Psol * T ** 2).subs(h, 2 * sp.pi * hb))
    return m.group(1).strip(), sp.simplify(A_lnm - expr) == 0


# ============================================================================ E. DOCKET 56's owed instrument
DOCKET56_OWED = (
    ("N(spec): the bits in the specification, computed FROM the specification (never by inverting a channel law -- "
     "branelink's round-trip A(N(A)) = A proves nothing)",
     "COMPUTED-HERE (imported from measure.object_bits): 9.51e27 (species sequence) to 1.09e29 (0.1 A grid) classical "
     "bits under named counts; a quantum definition needs 2 classical bits and 1 ebit per qubit (H-FAITHFUL).  WHICH count "
     "is the specification is H-ALT: a choice, not computed."),
    ("E_tx(N, T, d, apertures): the energy to send N bits to Proxima in time T",
     "COMPUTED-HERE as a FLOOR for a DECLARED T and DECLARED apertures (LNM eqs. 6 and 8, READ).  It falls without "
     "limit as T grows, so it prices a schedule, not the route."),
    ("E_fab: the energy to separate M(p,s) x 70 kg of feedstock into elements and assemble 6.7e27 atoms to the "
     "specification",
     "NOT COMPUTED ANYWHERE ON THE BOARD (stockgate refuses separation energy; no assembly model exists).  Landauer's "
     "erasure floor of the specification register is imported from measure (H-ERASE) and is not E_fab."),
    ("E_hold: the receiver's holding cost", "IMPORTED as a floor only (measure.bekenstein_floor_j; a property of the "
     "holder, satisfied by any 70 kg body: Mc^2 exceeds it by > 10^14)"),
    ("m_set: the mass of fabricator + survey + receiver sent at <= c (D23)", "NOT SPECIFIED ANYWHERE: OPEN"),
    ("k*: the number of later reconstructions at which S5 beats sending the payload",
     "COMPUTED-HERE as an identity in m_set and E_rec = E_tx + E_fab (+ erasure): k* = m_set K / (m_pay K - E_rec), "
     "-> m_set/m_pay as E_rec -> 0; no k* once E_rec >= m_pay K (H-KINETIC)."),
)


# ============================================================================ F. the grade
def grade_o_seat(state):
    """O-SEAT under H-SEAT-S5.  Removable (and then only pending seating and M) iff S5's supply is SHOWN (its price per
    reconstruction computed and the fabricator/receiver specified) AND every gate conjunct is True for some body.
    LEFT on the S5 pathway iff a conjunct is False for every candidate body, or S5 is refused.  OPEN otherwise."""
    s5 = state.get("S5 shown")
    conj = [state.get(k) for k in ("aperture", "condensed", "primitive", "accessible", "mass", "composition")]
    if s5 is False or any(c is False for c in conj):
        return "LEFT on the S5 pathway"
    if s5 is True and all(c is True for c in conj):
        return "REMOVABLE (pending seating and M)"
    return "OPEN"


def board_state():
    """The state the board and the READ sources support, today."""
    return {"S5 shown": None,                        # LEDGER S5 OPEN; DOCKET 56 owed
            "aperture": None,                        # formation: NOT EVALUABLE
            "condensed": formation.SURVEY_CONDENSED_BODY_FOUND,
            "primitive": None, "accessible": None,
            "mass": None,                            # total mass is not accessible mass (H-BODY-ACCESS)
            "composition": None}                     # no body composition measured; P measured in no star of the
                                                     # system (sources read); N only in alpha Cen A, as 'solar' 


def collect():
    kstar, lim, lim_ok = breakeven_symbolic()
    sel = {}
    for r in measure.price_table()[0]:
        for T_yr in (1.0, 100.0):
            sel[(r["count"], T_yr)] = channel_floor(r["bits"], T_yr * YEAR_S)
    budget, fails = devolatilised_failures()
    return {
        "ledger": {k: measure.ledger_row(k)[0] for k in ("S5", "D23", "D25", "S10", "S13")},
        "A_payload_grams": payload_grams(),
        "A_per_element_stock_kg": per_element_stock(),
        "A_binders_top3": binders(),
        "A_binder_as_composed_59_CI": stockgate.binding_under("as-composed 59", "CI chondrite"),
        "A_proxima_measured": proxima_measured(),
        "A_acen_adjusted_CI_factors": acen_adjusted_ci("A"),
        "B_gate": gate_conjuncts(),
        "B_devolatilised_budget_kg_per_kg": budget, "B_devolatilised_failures": fails,
        "C_setup": setup_times(), "C_kstar": str(kstar), "C_kstar_limit": str(lim), "C_limit_is_mass_ratio": lim_ok,
        "C_Erec_ceiling_J": erec_ceiling(), "C_receiver_fabricator": receiver_and_fabricator(),
        "D_information": information_vs_channels(),
        "D_channel_floor": {f"{k[0]} | T = {k[1]:g} yr": v for k, v in sel.items()},
        "D_branelink_law": branelink_law_matches_one_pol(),
        "E_docket56_owed": DOCKET56_OWED,
        "F_grade": grade_o_seat(board_state()), "F_state": board_state(),
        "READ": [FARIA_2022, BRUGGER_2016, {k: v for k, v in MOREL_2018.items() if k != "XFe"}, KERVELLA_2017,
                 LNM_1999, BEKENSTEIN_1981, PORTO_DE_MELLO_2008, HINKEL_KANE_2013],
        "proxima_distances (settle, W2-fix)": settle.proxima_distances(),
    }


def report():
    R = collect()
    print(__doc__.split("NAMED HYPOTHESES")[0].strip())
    print("\nLEDGER rows READ (status):", R["ledger"])
    print("\nA. WHAT THE DESTINATION MUST HOLD -- 70 kg x stock.HUMAN (H-PAYLOAD), element by element")
    ps = R["A_per_element_stock_kg"]
    print(f"   {'el':3s} {'grams':>10s} {'CI kg':>10s} {'photosph kg':>12s} {'crust kg':>10s}   Proxima system (READ)")
    for e, g in sorted(R["A_payload_grams"].items(), key=lambda kv: -kv[1]):
        pm = R["A_proxima_measured"][e]
        print(f"   {e:3s} {g:10.4g} {ps['CI chondrite'][e]:10.4g} {ps['stellar photosphere'][e]:12.4g} "
              f"{ps['Earth cont. crust'][e]:10.4g}   aCen: {pm['alpha_Cen_AB']}; body: not measured")
    for d, top in R["A_binders_top3"].items():
        print(f"   binder at {d:22s}: " + ", ".join(f"{e} {v:.4g} kg/kg" for e, v in top))
    print("   stockgate 'as-composed 59' at CI (D25's own payload): %s %.4f kg/kg" % R["A_binder_as_composed_59_CI"])
    adj, raw = R["A_acen_adjusted_CI_factors"]
    print("   H-ACEN-RATIO (CI x alpha Cen A [X/Fe]): P %.4f (unadjusted %.4f; [P/Fe] UNMEASURED, set 0), N %.4f "
          "([N/Fe] ~ 0 MEASURED in the literature, Porto de Mello 2008), C %.4f" % (adj["P"], raw["P"], adj["N"], adj["C"]))
    print("   -> the binder P is measured in NO star of the Proxima system in the sources read and in NO body; the CI "
          "runner-up N is measured in alpha Cen A ('solar') and in no body.")
    print("\nB. D25's GATE AT PROXIMA (stockgate.GATE)")
    for k, v in R["B_gate"].items():
        print(f"   {k}: {v}")
    print(f"   H-DEVOL-PROXY: at the CI budget ({R['B_devolatilised_budget_kg_per_kg']:.3f} kg/kg) a devolatilised body "
          "(crust) fails on: " + ", ".join(f"{e} ({v:.4g} kg/kg, T_c {t} K)" for e, v, t in R["B_devolatilised_failures"]))
    print("\nC. FABRICATOR, SURVEY, RECEIVER (D23)")
    for r in R["C_setup"]:
        print("   beta %-5g arrival %8.3f yr; survey report home (H-CHECK-AT-ORIGIN) %8.3f yr"
              % (r["beta"], r["arrival_yr"], r["survey_report_home_yr (H-CHECK-AT-ORIGIN)"]))
    print(f"   k* = {R['C_kstar']};  E_rec -> 0: k* -> {R['C_kstar_limit']} (mass ratio: {R['C_limit_is_mass_ratio']})")
    print("   E_rec ceiling (no k* above it): " + ", ".join(f"beta {b}: {v:.4g} J" for b, v in R["C_Erec_ceiling_J"].items()))
    rf = R["C_receiver_fabricator"]
    print(f"   fabricator places {rf['atoms_to_place']:.4g} atoms (rate, energy: NOT COMPUTED); receiver floors:")
    for c in rf["counts"]:
        print(f"     {c['count']:42s} {c['bits']:.4g} bits; Bekenstein floor {c['bekenstein_floor_J_R1m']:.3g} J; "
              f"Landauer (erase, 310 K) {c['landauer_J_310K']:.3g} J")
    print("\nD. THE INFORMATION THAT MUST ARRIVE, AGAINST THE CHANNELS")
    I = R["D_information"]
    print(f"   teleportation: arrival {I['teleport_arrival_after_sending_yr']:.4f} yr after sending; advantage "
          f"{I['teleport_advantage_over_light_s']} s; drift: >= {I['N_min_pairs_per_qubit']} pairs per qubit "
          f"(CMAX {I['CMAX_bits_per_pair']:.4f} bits/pair)")
    for r in I["per_count"]:
        print(f"     {r['count']:42s} classical {r['teleport_classical_bits']:.4g}, ebits {r['teleport_ebits_predistributed']:.4g}, "
              f"drift pairs {r['drift_pairs_total (1 + N_min per qubit)']:.4g}")
    for r in I["drift_window_on_READ_limits"]:
        print("     window:", r)
    print("     one-end source, zero drift: read at %.4g yr (beats light launched at firing: %s); midpoint: %.4g yr (%s)"
          % (I["first_transit_one_end_zero_drift"]["t_read"] / YEAR_S,
             I["first_transit_one_end_zero_drift"]["beats_light_launched_at_firing"],
             I["first_transit_midpoint_zero_drift"]["t_read"] / YEAR_S,
             I["first_transit_midpoint_zero_drift"]["beats_light_launched_at_firing"]))
    print("     drift time at the READ eps_max (shortest not excluded):", I["drift_time_at_READ_eps_max_s"])
    print("     midpoint source shipped from the origin (S5's one-end case): earliest read %.4f yr + T_drift"
          % I["midpoint_source_shipped_from_origin_earliest_read_yr (+ T_drift)"])
    print("   classical-channel energy FLOOR at Proxima (H-EM-CARRIER; DECLARED T and 100 m dishes):")
    for k, v in R["D_channel_floor"].items():
        print(f"     {k:52s} received floor 1D {v['E_1d_two_pol_J']:.3g}-{v['E_1d_one_pol_J']:.3g} J; LNM eq.6 {v['E_3d_J']:.3g} J "
              f"(kT {v['kT_3d_MeV']:.3g} MeV, {v['transverse_modes_at_kT']:.2g} transverse modes: outside eq.6's regime)")
    print("   branelink's A(N) is LNM eq. (8) at one polarisation:", R["D_branelink_law"])
    print("\nE. DOCKET 56's OWED INSTRUMENT -- what it would have to compute")
    for q, s in R["E_docket56_owed"]:
        print(f"   - {q}\n       {s}")
    print("\nF. O-SEAT:", R["F_grade"], "-- state", R["F_state"])


def selftest():
    res = []

    def chk(name, ok, detail="", kind="CONTROL"):
        res.append((name, bool(ok), kind))
        print(f"  {'ok  ' if ok else 'FAIL'} [{kind}] {name}  {detail}")

    print("READ fixtures")
    a = (G * FARIA_2022["M_star_sun"][0] * M_SUN * (FARIA_2022["b_P_days"] * 86400) ** 2 / (4 * math.pi ** 2)) ** (1 / 3) / AU
    chk("Faria: Kepler III from the READ M_star and P reproduces the READ a = 0.04856 au", abs(a - FARIA_2022["b_a_au"]) < 2e-4,
        f"{a:.5f}")
    a1 = (G * 1.0 * M_SUN * (FARIA_2022["b_P_days"] * 86400) ** 2 / (4 * math.pi ** 2)) ** (1 / 3) / AU
    chk("  control: a solar-mass host does NOT reproduce it", abs(a1 - FARIA_2022["b_a_au"]) > 2e-4, f"{a1:.4f}")
    for s in ("A", "B"):
        i = 0 if s == "A" else 1
        x = MOREL_2018["XFe"]
        co = 10 ** (x["C"][i] - x["O"][i]); ms = 10 ** (x["Mg"][i] - x["Si"][i])
        chk(f"Morel Table 1 (alpha Cen {s}) reproduces the printed C/O and Mg/Si (p.8)",
            abs(co - MOREL_2018["printed_C_over_O"][s]) < 0.01 and abs(ms - MOREL_2018["printed_Mg_over_Si"][s]) < 0.01,
            f"C/O {co:.3f}, Mg/Si {ms:.3f}")
    co_sw = 10 ** (MOREL_2018["XFe"]["O"][0] - MOREL_2018["XFe"]["C"][0])
    chk("  control: C and O swapped does NOT reproduce C/O = 1.18", abs(co_sw - 1.18) > 0.05, f"{co_sw:.3f}")
    chk("Morel: 21 species (Fe + 20 ratios) as typed here", 1 + len(MOREL_2018["XFe"]) == 21, "", "STRUCTURAL")
    r6 = lnm_rate_3d(1.0, 1.0, 1.0, 1.0); r8 = lnm_rate_1d(1.0, pol=2)
    chk("LNM eq. (6) reproduces its printed 1.61e21 bits/s (1 m^2, 1 m, 1 J/s)", abs(r6 / 1.61e21 - 1) < 0.005, f"{r6:.4g}")
    chk("LNM eq. (8) reproduces its printed 2.03e17 bits/s (1 J/s)", abs(r8 / 2.03e17 - 1) < 0.005, f"{r8:.4g}")
    r8h = math.sqrt(4 * math.pi ** 2 / (3 * HBAR)) / LN2
    chk("  control: hbar in place of h does NOT reproduce eq. (8)", abs(r8h / 2.03e17 - 1) > 0.1, f"{r8h:.3g}")
    chk("  control: one polarisation does NOT reproduce LNM's printed eq. (8)",
        abs(lnm_rate_1d(1.0, pol=1) / 2.03e17 - 1) > 0.1, f"{lnm_rate_1d(1.0, pol=1):.3g}")
    expr, same = branelink_law_matches_one_pol()
    chk("branelink's A(N) (read from its source) equals LNM eq. (8) at ONE polarisation (sympy)", same is True, f"'{expr}'")
    import sympy as sp
    n, hb, T, P = sp.symbols("n hbar T P", positive=True)
    A2 = sp.simplify((sp.solve(sp.Eq((n * sp.log(2) / T) ** 2, 4 * sp.pi ** 2 * P / (3 * 2 * sp.pi * hb)), P)[0] * T ** 2))
    chk("  control: at TWO polarisations the law differs from branelink's by a factor 2",
        sp.simplify(sp.sympify(expr.replace("sp.", ""), locals={"hb": hb, "n": n}) / A2) == 2, "")

    print("\nA. requirement")
    g = payload_grams()
    chk("grams sum to 70 kg (stock.HUMAN sums to 1 within its rounding)", abs(sum(g.values()) / 70000 - 1) < 1e-4,
        f"{sum(g.values()):.2f} g", "GROUND")
    e, f = stock.binding_element(stock.HUMAN, stockgate.DESTS["CI chondrite"]())
    chk("binder at CI is P, ~10.7 kg/kg (stock.binding_element, imported)", e == "P" and abs(f - 10.70) < 0.02,
        f"{e} {f:.4f}", "GROUND")
    chk("stockgate's 59-element payload binds on the same element at CI", stockgate.binding_under("as-composed 59",
        "CI chondrite")[0] == e, "", "GROUND")
    tot = sum(per_element_stock()["CI chondrite"].values())
    chk("  control: a SUM over elements is not the gate's MAX (sum > max x 3)", tot > 3 * 70 * f, f"sum {tot:.4g} kg")
    adj, raw = acen_adjusted_ci("A")
    mv = max(raw, key=lambda k: abs(adj[k] / raw[k] - 1))
    chk("H-ACEN-RATIO leaves the binder P, moved only by renormalisation (< 5 %; [P/Fe] unmeasured, set 0)",
        max(adj, key=adj.get) == "P" and abs(adj["P"] / raw["P"] - 1) < 0.05,
        f"P {raw['P']:.4f} -> {adj['P']:.4f}; largest move {mv} {adj[mv] / raw[mv] - 1:+.1%}")
    unmeasured = sorted(k for k in stock.HUMAN if k not in MOREL_2018["XFe"] and k not in ("Fe", "H"))
    chk("P and N are among the payload elements Morel 2018 does not measure", {"P", "N"} <= set(unmeasured),
        str(unmeasured), "GROUND")

    print("\nB. gate")
    gc = gate_conjuncts()
    chk("formation.gate at Proxima b (synthetic aperture; primitive unmeasured) is UNDETERMINED",
        gc["formation.gate, synthetic aperture around b"] == formation.UNDETERMINED, "", "GROUND")
    chk("formation.gate with no aperture is NOT-EVALUABLE", gc["formation.gate, no aperture"] == "NOT-EVALUABLE", "",
        "GROUND")
    chk("  control: the same gate with b measured devolatilised returns False", formation.gate(
        (FARIA_2022["b_a_au"], 0.01), [(FARIA_2022["b_a_au"], True, False, 1e24)]) is False, "")
    budget, fails = devolatilised_failures()
    names = [x[0] for x in fails]
    chk("H-DEVOL-PROXY: a devolatilised body fails N first at the CI budget", names and names[0] == "N",
        ", ".join(names))
    chk("  control: a CI body at its own budget fails on nothing", devolatilised_failures(body_dest="CI chondrite")[1]
        == [], "", "STRUCTURAL")
    chk("Proxima b's MINIMUM mass (m sin i) exceeds the CI threshold by > 1e21, a floor (it is not the accessible mass)",
        gc["minimum mass over CI threshold, a floor (NOT accessible mass: H-BODY-ACCESS)"] > 1e21
        and FARIA_2022["b_mass_is_minimum"],
        f"{gc['minimum mass over CI threshold, a floor (NOT accessible mass: H-BODY-ACCESS)']:.3g}", "GROUND")
    chk("Brugger 2016 (READ) models no C, N or P: the primitive conjunct stays None (unconstrained), never True or False",
        BRUGGER_2016["models_C_N_P"] is False and board_state()["primitive"] is None, "", "GROUND")
    pm = proxima_measured()
    chk("W2-fix: N is measured in alpha Cen A (Porto de Mello 2008, READ) and P is not, in the sources read -- the table "
        "tells the two apart", pm["N"]["alpha_Cen_AB"].startswith("measured in alpha Cen A")
        and pm["P"]["alpha_Cen_AB"].startswith("NOT") and P_MEASURED_IN_PROXIMA_SYSTEM is False, "", "GROUND")

    print("\nC. setup and amortisation")
    st = setup_times()
    chk("earliest arrival equals phase1's span in light years (D23's 4.2465 yr)",
        abs(st[0]["arrival_yr"] - settle.L_PROXIMA_PHASE1 / LY) < 1e-9, f"{st[0]['arrival_yr']:.5f}", "STRUCTURAL")
    chk("W2-fix: foliation's 4.2465 ly is phase1.L_PROXIMA rounded (agree to 1e-5); Faria 2022's READ parallax gives a "
        "distance 0.056 % shorter (settle.proxima_distances)", abs(foliation.PROXIMA_LY / (settle.L_PROXIMA_PHASE1 / LY) - 1)
        < 1e-5 and abs(1000.0 / FARIA_2022["parallax_mas"][0] - FARIA_2022["distance_pc"][0]) < 5e-5, "", "GROUND")
    kstar, lim, ok = breakeven_symbolic()
    chk("sympy: k* -> m_set/m_pay as E_rec -> 0", ok, str(lim))
    K = (1 / math.sqrt(1 - 0.1 ** 2) - 1) * C ** 2
    num = breakeven(700.0, 0.1, 0.0)
    chk("numeric k* = m_set/m_pay at E_rec = 0 (700 kg setup, illustrative)", abs(num - 10.0) < 1e-9, f"{num}")
    chk("  control: E_rec at the ceiling gives no k*", breakeven(700.0, 0.1, PAYLOAD_KG * K) is None, "")
    chk("  control: E_rec > 0 raises k* above the mass ratio", breakeven(700.0, 0.1, 0.5 * PAYLOAD_KG * K) > 10.0, "")

    print("\nD. information and channels")
    npm = n_pairs_min()
    chk("N_min pairs per qubit is the first N with N x CMAX >= 2 (settle, imported)",
        npm * settle.CMAX >= 2 and (npm - 1) * settle.CMAX < 2, f"N_min = {npm}")
    I = information_vs_channels()
    chk("teleportation advantage over light at Proxima is 0 (transit, imported)",
        I["teleport_advantage_over_light_s"] == 0.0, "", "GROUND")
    chk("one-end distribution (S5's case) does not beat light launched at firing (settle.first_transit_times)",
        I["first_transit_one_end_zero_drift"]["beats_light_launched_at_firing"] is False, "", "GROUND")
    chk("a midpoint source shipped from the origin reads no earlier than the light time (S5's one-end case)",
        abs(I["midpoint_source_shipped_from_origin_earliest_read_yr (+ T_drift)"] - settle.L_PROXIMA_PHASE1 / LY) < 1e-9, "",
        "STRUCTURAL")
    td = I["drift_time_at_READ_eps_max_s"]
    chk("drift time at the READ eps_max is finite and below 2 days for both H-MAP readings (settle, imported)",
        "error" not in td and all(0 < v < 2 * 86400 for v in td.values()), str({k: round(v) for k, v in td.items()
                                                                          if isinstance(v, float)}), "GROUND")
    N = 1e28
    e1 = channel_floor(N, YEAR_S); e2 = channel_floor(2 * N, YEAR_S); e3 = channel_floor(N, 8 * YEAR_S)
    chk("1D floor scales as N^2 at fixed T", abs(e2["E_1d_one_pol_J"] / e1["E_1d_one_pol_J"] - 4) < 1e-6, "")
    chk("3D floor scales as N^(4/3) at fixed T", abs(e2["E_3d_J"] / e1["E_3d_J"] - 2 ** (4 / 3)) < 1e-6, "")
    chk("  control: the floor FALLS as T grows (8x T: 1D /8, 3D /2) -- it prices a schedule",
        abs(e1["E_1d_one_pol_J"] / e3["E_1d_one_pol_J"] - 8) < 1e-6 and abs(e1["E_3d_J"] / e3["E_3d_J"] - 2) < 1e-6, "")
    allm = [channel_floor(r["bits"], T * YEAR_S)["transverse_modes_at_kT"] for r in measure.price_table()[0]
            for T in (1.0, 100.0)]
    chk("H-FEW-MODES holds and H-MODE-CONTINUUM fails: < 1 transverse mode in every case computed", max(allm) < 1.0,
        f"max {max(allm):.3g}", "GROUND")
    chk("1D one-pol floor = branelink's A(N)/T numerically",
        abs(e1["E_1d_one_pol_J"] / (3 * HBAR * N ** 2 * LN2 ** 2 / (math.pi * YEAR_S)) - 1) < 1e-6, "", "STRUCTURAL")
    rows = measure.price_table()[0]
    chk("Bekenstein floor (measure, imported) is < 1e-14 of the payload's Mc^2 for every count",
        all(r["bekenstein_floor_J_R1m"] < 1e-14 * massform.rest_energy_j() for r in rows), "", "GROUND")

    print("\nF. grade")
    gr = grade_o_seat(board_state())
    chk("O-SEAT reads OPEN on today's state", gr == "OPEN", gr)
    allt = {k: True for k in board_state()}
    chk("  control: every conjunct and S5 shown -> REMOVABLE", grade_o_seat(allt).startswith("REMOVABLE"), "")
    chk("  control: primitive measured False (sole body) -> LEFT", grade_o_seat({**board_state(), "primitive": False})
        .startswith("LEFT"), "")
    chk("LEDGER S5, D23, D25 read OPEN", all(measure.ledger_row(k)[0] == "OPEN" for k in ("S5", "D23", "D25")), "",
        "GROUND")

    n_ctrl = sum(1 for _, ok, k in res if k == "CONTROL")
    bad = [n for n, ok, _ in res if not ok]
    print(f"\n{len(res) - len(bad)}/{len(res)} pass; CONTROL {n_ctrl}, GROUND "
          f"{sum(1 for r in res if r[2] == 'GROUND')}, STRUCTURAL {sum(1 for r in res if r[2] == 'STRUCTURAL')} (not counted)")
    return not bad


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
