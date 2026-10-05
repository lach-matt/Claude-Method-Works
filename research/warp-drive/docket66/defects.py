#!/usr/bin/env python3
r"""
defects.py -- DOCKET 66, A1: H-DEFECT-SEAT tested alone.  Topological defects (string, domain wall, monopole,
texture) graded as SEATS against the board's seat conditions and against DOCKET 68's obstructions.

    python3 defects.py             the report (the grade table, then every figure with its owner)
    python3 defects.py --json P    also write the report as JSON to P
    python3 defects.py --selftest  every computation, every READ fixture, and controls that can fail

M's words (ledger.py RULED_BY_M row M-S1A-P3, read at run time, never retyped as a result):
    "Seating occurs in a place where matter can occur but not in its original geometric form"
carried as the hypothesis H-DEFECT-SEAT (docket66/CHARTER.md).  It is graded on what it does, never dismissed.

WHAT THIS FILE DOES ITSELF (each item computed here, stdlib + sympy + z3):
  1. the stress tensor of each defect class in an orthonormal frame, and NEC / WEC / SEC / DEC per direction,
     exact (sympy rationals), each condition marked SAT, SATURATED or VIOLATED;
  2. the theorem that every canonical scalar + gauge field satisfies the NEC pointwise (sympy: T_kk is a sum of
     squares), with the phantom control that must violate it;
  3. the geometry: the string's deficit from the linearised field (HK eq. 4.3), the global monopole's exact
     Einstein tensor, the wall's Tolman mass per area and the sign split R_uu < 0 < R_kk;
  4. the board's seat tests, applied to each class: Sturm's sufficient condition (the form specthm.py states,
     4 pi G T_kk s^2 / c^4 >= pi^2, checked in specthm's source at run time), the lensing analogue of spec.py's
     S-1 focal formula, M-S1A-P3 (i) at the seat (closed causal curves; the topology change Geroch/Borde need,
     asked of create.py), and specthm's own placement of defect seats in class S-3;
  5. a counterpart of "matter occurs there but not in its original form" under a named reading (H-YUKAWA,
     H-FORM-IS-MASS-AND-DIMENSION): fermion zero modes (a Yukawa mass that vanishes where the order parameter vanishes;
     HK pp.33-34 say only that the mass vanishes at the core and the modes move at c) -- the Jackiw-Rebbi profile
     computed and its normalisability tested both ways.  [D66-repro residual of V66-0 #3: this item first read "the
     literature's precise sense of ..."; kept as history];
  6. a z3 bookkeeping of the D68 grades this hypothesis can carry, with a vacuity guard and mutation controls;
  7. (D66-fix, 2026-10-04, answering the three wave-1 verifier reports) the hedgehog's stress in the cone metric and
     the exact deficit 8 pi G eta^2; the thin M4-M4 wall's global time function (CGS p.15, Fig.4); the global
     monopole's conjugate points (Jacobi equation); the gauge monopole's S-1 lens through spec.focal_length; the
     creation of a defect-supported throat under M's ruling M-S1A-P3; and a1_grades(), the A-report grade table built
     from all of the above (combine66.py reads it).  HISTORY keeps what wave 1 first said.

IT IMPORTS, NEVER COPIES: spec (G, c, AU, the focal formula, the lens table), specthm (sturm_ratio, classes, its
Sturm sentence), massform (the S13 held-seat route, its stable range, the Higgs share, D23 asked of the ledger),
excite (stability_edge), create (is_topology_change, GEROCH_NEEDS_MATTER_ASSUMPTION), axial (the conical-defect
hypothesis), ledger (M's words), docket68/seat (grade_o_seat, board_state).  It writes nothing outside docket66/
except a path the caller names.  It edits no peer and repairs nothing.

OUTSIDE PAPERS: every figure typed below from a paper is READ at source, with its route and page, in SOURCES.
The routes: alphaXiv answer_pdf_queries (arXiv full text, page-tagged) and Firecrawl research search (abstracts).
No paywall or login wall was met or circumvented.  One route error is recorded, not hidden: arXiv
hep-th/0001128, tried as Rubakov-Shaposhnikov 1983, is an unrelated paper (Fring & Korff); R-S 1983 was NOT read.

STATUS WORDS.  For the obstructions, DOCKET 68's verdict words (docket68/B-combine.md section 1): REMOVED,
REMOVED-IF, NOT-BOUND-IF, OPEN, SILENT, LEFT; and "LEAVES" (the A-reports' word) where the hypothesis does not
bear on the obstruction, so the board's own grade stands.  A theorem that does not bind gives NOT-BOUND-IF, never
REMOVED.  For seat classes, specthm's words: EMPTY, EMPTY IF, OPEN, NONEMPTY.  The word DECLARED is never used.

NAMED HYPOTHESES (every limitation is one of these; see HYPOTHESES):
  H-CANONICAL, H-THIN, H-LINEAR-GRAV, H-UNIFORM-CORE, H-SM-ONLY, H-SEAT-PERSISTS, H-TURN-CONJUGATE,
  H-TURN-CROSSING, H-YUKAWA, H-STATIC-STRING, H-FORM-IS-MASS-AND-DIMENSION, H-VIS-MINKOWSKI, H-MONOPOLE-MASS,
  H-WEAK-FIELD, H-S1-VACUUM; OPEN pathways N_NEGT, N_DEFB, N_WNCC (specthm's W-create-ncc), and the board's N_S5.
"""

import json
import math
import os
import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
for _p in (WD, os.path.join(WD, "docket68")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

_OWN = {}


def own(name):
    """Import an owner by name, once (the board's owners import ledger, ~25 s; nothing at module import)."""
    if name not in _OWN:
        _OWN[name] = __import__(name)
    return _OWN[name]


# =============================================================================== 0. named hypotheses
HYPOTHESES = {
    "H-DEFECT-SEAT": "M's (M-S1A-P3 (ii)): a topological defect is a site where matter can occur but not in its "
                     "original geometric form, and so a candidate seat.  THE HYPOTHESIS UNDER TEST.",
    "H-CANONICAL": "the defect's fields are classical, minimally coupled scalars and gauge fields with positive "
                   "kinetic terms (the field theories every READ source here builds defects from)",
    "H-THIN": "the defect's stress tensor taken in its thin (delta-function) form outside the core",
    "H-LINEAR-GRAV": "linearised gravity for the string deficit (HK p.53: the exact deficit carries O(G^2 mu^2) "
                     "corrections)",
    "H-UNIFORM-CORE": "for the Sturm bound inside a string core: a uniform core of radius w carrying the vacuum-string "
                      "form (and, as a member, a transverse T_kk = 2u)",
    "H-SM-ONLY": "the seat's order parameter is the Standard Model electroweak doublet (vacuum manifold S^3), with "
                 "no field beyond the Standard Model",
    "H-SEAT-PERSISTS": "a seat is a place that persists over the arrival (so a spacetime EVENT is not a seat)",
    "H-TURN-CONJUGATE": "spec.py's PART 2 'TURN' read as a conjugate point (a caustic of a geodesic congruence)",
    "H-TURN-CROSSING": "spec.py's PART 2 'TURN' read as any second meeting of two geodesics from one event",
    "H-YUKAWA": "the matter in question gets its rest mass from a Yukawa coupling to the defect's order parameter",
    "H-STATIC-STRING": "the string is straight and non-spinning (or its spin is at most its dislocation, S <= kappa)",
    "H-FORM-IS-MASS-AND-DIMENSION": "M's 'not in its original geometric form' read as: the matter's rest mass and its "
                                    "dimensionality change (massless modes confined to the defect).  The sources say "
                                    "only that the Yukawa mass 'vanishes at the core' and that the modes move at c "
                                    "(HK pp.33-34); the mapping to 'geometric form' is this file's reading, not theirs "
                                    "(D66-fix, V66-0 #3)",
    "H-VIS-MINKOWSKI": "the thin wall is the non-extreme Vilenkin-Ipser-Sikivie wall with Lambda = 0 on both sides "
                       "(both sides inside the bubble), each side extended uniquely onto Minkowski space (CGS Fig.4 "
                       "caption, READ) and no identification made (CTCs in CGS arise only by identification across "
                       "AdS Cauchy horizons, p.14, READ; an M4-M4 wall has none)",
    "H-MONOPOLE-MASS": "a GUT gauge monopole of mass 1e17 GeV/c^2 (scanned 1e15 .. 1e19 GeV), core radius "
                       "(1/alpha_GUT) hbar/(M c) with alpha_GUT = 1/40, and the Dirac magnetic charge h/e",
    "H-WEAK-FIELD": "the lensing impact parameter b lies far outside the monopole's core and its gravitational "
                    "radius, so spec.focal_length's weak-field point-lens formula applies (checked in "
                    "gauge_monopole_lens: b / r_core and b / r_s)",
    "H-S1-VACUUM": "specthm's S-1 literal 'wl' says lensing of positive mass 'through vacuum'; the gauge monopole's "
                   "exterior carries its magnetic field, whose energy beyond b is computed (a fraction of Mc^2) and "
                   "read as negligible when that fraction is below 1e-15",
    "N_NEGT": "OPEN PATHWAY: a negative-tension string (or loop) shown to exist -- no mechanism known (Visser 1989 "
              "p.5, READ)",
    "N_DEFB": "OPEN PATHWAY: a baryon-number-violating defect core shown to SUPPLY the payload's baryons at the seat.  "
              "READ for GUT string cores (HK p.63: a quark reaching the core 'can ... emerge a lepton, and vice versa') "
              "and for gauge monopoles (Rubakov-Callan, as HK p.63 cites it); for walls and global monopoles not READ, "
              "OPEN there as unchecked.  The READ direction is WASH-OUT: an existing asymmetry 'can relax to zero via "
              "scattering off strings' (HK eq.(4.33) p.64) -- payload quarks become leptons, the opposite of a supply.  "
              "Emission of baryon number needs CP-violating couplings and a departure from thermal equilibrium "
              "(HK p.65, Sakharov).  So N_DEFB is OPEN only IF {CP-violating core couplings, departure from "
              "equilibrium}; its feedstock would be leptons; its rate is computed nowhere.  Wave 1 first said "
              "'direction and rate computed nowhere'; the direction is READ (D66-fix, V66-0 #2)",
}

#: What wave 1 first said, kept (M's rule: history kept).  Each entry: (site, wave 1's words, D66-fix's correction, why).
HISTORY = [
    ("monopole deficit", "Delta = 8 pi eta^2/(1 + 8 pi eta^2), labelled EXACT",
     "Delta = 8 pi G eta^2 exactly outside the core (Barriola-Vilenkin)",
     "wave 1 set the cone metric's rho equal to the FLAT-space hedgehog density eta^2/r^2; in the cone metric the "
     "hedgehog's gradient energy is eta^2/(A r^2) (hedgehog_curved, V66-2 #1)"),
    ("wall seat CTC/Borde", "OPEN: the VIS global causal structure is not computed",
     "PASSES under H-VIS-MINKOWSKI: Minkowski T is a global time function (vis_time_function; CGS p.15, Fig.4 READ)",
     "V66-1 #3"),
    ("global monopole turn", "a focal LINE, no single focus; a turn under H-TURN-CROSSING, none under H-TURN-CONJUGATE",
     "a TURN under both: every axis recrossing is a conjugate point (monopole_conjugate)",
     "the rotation Killing field about the source-centre axis is a Jacobi field vanishing at the source and at each "
     "axis recrossing (V66-1 #4)"),
    ("gauge monopole lensing seat", "S-3 (or S-1 if its lensing seats; not computed): OPEN",
     "S-1 IF {H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM} (gauge_monopole_lens)", "V66-1 #5"),
    ("throat support, O-MAKE-TOPO", "binds if made from flat space",
     "OPEN via specthm W-create-ncc: M has ruled (ledger M-S1A-P3: 'a singular throat is not disqualified', 'the "
     "throat-creation classes stay OPEN')", "V66-1 #1; the ruling is a board ruling, not a question for M"),
    ("N_DEFB", "direction and rate computed nowhere", "direction READ (wash-out, HK eq.(4.33) p.64); a supply only "
     "IF {CP violation, departure from equilibrium} (HK p.65)", "V66-0 #2"),
    ("F1 zero modes", "an exact counterpart in the literature; SUPPORTED",
     "a counterpart under a named reading: SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}", "V66-0 #3"),
    ("Gott pair", "cannot form in an open universe",
     "cannot be created in an open (2+1)-dimensional universe with timelike total momentum (CFG94)", "V66-2 #2"),
    ("spinning string", "DISQUALIFIED inside r < S/alpha unless S < kappa",
     "with dislocation kappa: CTCs iff S > kappa, in r < sqrt(S^2 - kappa^2)/alpha; r < S/alpha only for kappa = 0",
     "V66-2 #3"),
    ("GV ring", "the GV ring's curvature singularity is at the throat",
     "a singular ring bounding the throat disc: conical only at sigma = 0 (the figures' tension T = -c^4/(4G)), "
     "conical plus power-law at sigma != 0 (GV pp.20-22)", "V66-2 #7"),
    ("string turn", "a TURN under H-TURN-CROSSING, none under H-TURN-CONJUGATE (D66-fix: 'the string's grade under the "
     "board's TURN is still M's to rule')",
     "a TURN: M ruled TURN = 'Any crossing' (H-TURN-CROSSING adopted; H-TURN-CONJUGATE kept as the alternative on "
     "record); rays on opposite sides cross at L = b/tan(4 pi G mu) (string_turn)", "M-RULINGS item 27, 2026-10-04"),
    ("F4 the wall's focus", "the only class that gives light a genuine focal point",
     "the only class that focuses a whole planar congruence at one distance; the global monopole (a line caustic) "
     "and the gauge monopole (an S-1 point lens) also give conjugate points; only the string is crossing-only",
     "follows from V66-1 #4 and #5"),
]

# =============================================================================== 1. sources READ, with routes
ALPHAXIV = "READ via alphaXiv answer_pdf_queries (arXiv full text, page-tagged)"
FC_ABS = "READ (abstract) via Firecrawl research search"
SOURCES = {
    "HK": ("Hindmarsh & Kibble, Cosmic strings, arXiv hep-ph/9411342v1", ALPHAXIV,
           "p.53 eq.(4.1) T = mu diag(1,0,0,-1) delta delta; eq.(4.3)-(4.4) the cone, Delta = 8 pi G mu (Vilenkin "
           "1981 restated); p.85 eq.(6.1) Delta = 8 pi G mu = 5.18 mu6 arcsec; p.16 eq.(1.17) mu = 1.35e21 mu6 kg/m; "
           "p.84 gravitational acceleration vanishes around a straight static string; p.90 inward deflection "
           "4 pi G mu 'independent of the impact parameter'; p.54 eq.(4.7) wiggly string attracts, global string "
           "repels; p.33-34 the fermion mass 'vanishes at the core', zero modes move at the speed of light; p.63 "
           "baryon-number violation in GUT string cores (cf. Rubakov-Callan for monopoles); p.64 eq.(4.33) "
           "dn_B/dt ~ -v sigma n_B / xi^2, an existing asymmetry 'can relax to zero via scattering off strings'; p.65 "
           "emission of baryon number needs CP violation and a departure from thermal equilibrium (Sakharov) -- "
           "pp.63-65 RE-READ at D66-fix 2026-10-04, same route; p.26 electroweak strings "
           "unstable for physical Weinberg angle; p.36 the electroweak gauge orbit space is S^3, simply connected, "
           "so no topologically stable string"),
    "DURRER": ("Durrer, Global field dynamics and cosmological structure formation, arXiv astro-ph/9411010", ALPHAXIV,
               "p.4 Table 1 (pi_0 walls, pi_1 strings, pi_2 monopoles, pi_3 textures = 'events in spacetime'); "
               "p.4 pi_2(G) = 0 for compact Lie groups; p.8 global monopole energy grows linearly with R; p.9 "
               "Derrick's theorem (dE/dlambda = I1 + 3 I2 > 0) and textures shrink; p.10 static global fields "
               "rho + 3p = 0; p.12 global monopole Psi = 0, Phi = -8 pi G eta^2 ln(r/l), deflection eps*pi; p.13 "
               "collapsing texture gives infall eps*pi; p.18 the monopole problem"),
    "CGS": ("Cvetic, Griffies & Soleng, Local and global gravitational aspects of domain wall space-times, "
            "arXiv gr-qc/9306005", ALPHAXIV,
            "p.6 eqs.(2.18)-(2.19) sigma = tau (vacuum wall); p.10 the Vilenkin-Ipser-Sikivie wall with Lambda = 0 "
            "both sides, kappa sigma = 4 beta, 'spherically symmetric bubbles rather than planar walls'; p.12 "
            "Sigma_wall = sigma - 2 tau = -sigma < 0, repulsive; abstract: the forces are 'global effects not "
            "caused by local curvature'; p.2 no static nonsingular planar solution.  READ at D66-fix (same route): "
            "abstract 'singularity free space-times'; p.14 CTCs arise only by identification across the Cauchy "
            "horizons of AdS4 sides; p.15 eq.(3.48) the M4 side of the non-extreme bubble, t_in = beta^-1 e^(-beta z) "
            "sinh(beta t), r_in = beta^-1 e^(-beta z) cosh(beta t) bring it to dt^2 - dr^2 - r^2 dOmega^2, the wall on "
            "r^2 - t^2 = beta^-2; Fig.4 caption: 'The unique extension of the comoving coordinates across the Rindler "
            "horizons is onto pure Minkowski space-time'.  READ at R-apply 2026-10-04 (same route): p.8 'if we choose A = "
            "e^(+2 beta z) for z > 0 (the M4 side of a wall)'; Appendix A eqs.(A.12)-(A.13) p.21, the same Rindler "
            "transformation with conformal factor e^(+-2 beta z) -- the factor 2 that (3.48) omits"),
    "VISSER89": ("Visser, Traversable wormholes: some simple examples, PRD 39 3182 (1989), arXiv 0809.0907", ALPHAXIV,
                 "p.3 eq.(2.4) convex throat -> negative surface energy and tension; p.4 WEC and AWEC violated; p.5 "
                 "cube edges rho = T = -1/(8G) = -1.52e43 J/m, 'identical to ... a negative tension classical "
                 "string', 'No natural mechanism for generating negative string tension is currently known'; p.6 "
                 "edge mu = -theta/(4 pi G), deficit -2 theta, mu = phi/(8 pi G)"),
    "GV17": ("Gibbons & Volkov, Weyl metrics and wormholes, arXiv 1701.05533v3", ALPHAXIV,
             "p.3 a static throat needs NEC violation (and FSW for no symmetry); p.21-22 eq.(5.42) the flat ring "
             "wormhole's ring tension T = -c^4/(4G), angle 'deficit' -2 pi; p.22 T = -3.0257e43 N, one-metre ring "
             "~ Jupiter's mass, 2 pi R T / c^2.  RE-READ at D66-fix: p.20-21 eqs.(5.37)-(5.40) the ring of tension "
             "T = -(1 + sigma^2) c^4/(4G) carries a conical (distributional) singularity AND a power-law curvature "
             "singularity; p.21 at sigma = 0 'the geometry is locally exactly flat' and 'the ring supports only the "
             "conical singularity'"),
    "FKZ23": ("Frolov, Krtous & Zelnikov, Ring wormholes and time machines, arXiv 2305.03887", ALPHAXIV,
              "p.1 the ring's matter violates the NEC; Gannon: non-simply-connected Cauchy surface + WEC -> singular; "
              "p.18 eq.(6.9) closed timelike curves form after T ~ R L c/(G M) when one mouth is surrounded by mass; "
              "'a rather robust property'"),
    "CFG94": ("Carroll, Farhi, Guth & Olum, Energy-momentum restrictions on the creation of Gott time machines, "
              "arXiv gr-qc/9404065", ALPHAXIV,
              "p.10 eq.(32) Gott's CTC condition cosh(xi) sin(alpha/2) > 1; p.2 cosmic strings satisfy the WEC; "
              "abstract: an open universe with timelike total momentum never has enough energy to make a Gott pair; "
              "p.4 Deser-Jackiw-'t Hooft: a spinning point particle gives CTCs"),
    "DLM04": ("De Lorenci & Moreira, Spinning strings, cosmic dislocations and chronology protection, "
              "arXiv gr-qc/0309122v2", ALPHAXIV,
              "p.1 eq.(2) spinning string ds^2 = (d tau + S d theta)^2 - dr^2 - alpha^2 r^2 d theta^2 - d xi^2, CTCs "
              "for r < S/alpha; eq.(3) with dislocation kappa: CTCs iff S > kappa, r < sqrt(S^2-kappa^2)/alpha"),
    "PLANCK13": ("Planck 2013 results XXV, arXiv 1303.5085", ALPHAXIV,
                 "abstract, Table 2 p.9: G mu/c^2 < 1.5e-7 (Nambu-Goto, Planck+WP), 1.3e-7 with high-l, 3.2e-7 "
                 "(Abelian-Higgs); textures < 1.06e-6 (Table 3 p.10)"),
    "FSW93": ("Friedman, Schleich & Witt, Topological censorship, arXiv gr-qc/9305017v2", ALPHAXIV,
              "p.3 Theorem 1: asymptotically flat, globally hyperbolic, ANEC -> every causal curve from scri- to "
              "scri+ deformable to one near infinity; p.2 Gannon's theorem"),
    "FGM19": ("Fu, Grado-White & Marolf, Traversable asymptotically flat wormholes with short transit times, "
              "arXiv 1908.03273v2", ALPHAXIV,
              "abstract and p.3: a compact cosmic string's quantum fluctuations give the negative null energy; "
              "traversable 'only at sufficiently early times', 'exponentially fragile'; t_min transit = d + logs; "
              "p.1: wormholes cannot provide the fastest causal curves (refs [8,9])"),
    "ETO25": ("Eto & Suzuki, Massless monopole-string-domain wall fermions, arXiv 2506.16765v1", ALPHAXIV,
              "p.15 zero modes localised on monopoles, strings or domain walls; p.16 eq.(3.28) localised where "
              "det M_f = 0, i.e. phi = 0; p.22 eq.(3.57) chiral modes 'moving at the speed of light'; p.25 App. A "
              "global-monopole zero mode f = exp(-(h/2) INT F dr); refs [8] Jackiw-Rebbi 1976, [9] Jackiw-Rossi 1981"),
    "GAUGE-MONO-ATTRACT": ("Dynamics of topological defects and inflation (authors not read), arXiv gr-qc/9506068", FC_ABS,
                           "'the spacetime with a gauge monopole has an attractive nature, contrary to ... a global "
                           "monopole'"),
    "THICK-WALL": ("Thick self-gravitating plane-symmetric domain walls (authors not read), arXiv gr-qc/9903059", FC_ABS,
                   "for 'large' epsilon only the de Sitter solution exists"),
    "ROUTE-ERROR": ("arXiv hep-th/0001128 (tried as Rubakov & Shaposhnikov 1983)", ALPHAXIV,
                    "IT IS Fring & Korff, 'Colour valued scattering matrices' -- unrelated; Rubakov-Shaposhnikov 1983 "
                    "is NOT READ and nothing here rests on it"),
}

#: READ figures (each with its source key and page); controls test them against what this file computes.
HK_ARCSEC_PER_MU6 = 5.18            # HK p.85 eq.(6.1)
HK_KG_PER_M_PER_MU6 = 1.35e21       # HK p.16 eq.(1.17)
PLANCK_NG_GMU = 1.5e-7              # PLANCK13 abstract, Planck+WP, Nambu-Goto, 95%
PLANCK_NG_GMU_HIGHL = 1.3e-7        # PLANCK13 abstract, + high-l
PLANCK_AH_GMU = 3.2e-7              # PLANCK13 abstract, Abelian-Higgs
PLANCK_TX_GMU = 1.06e-6             # PLANCK13 Table 3, textures (as an effective G mu)
VISSER_EDGE_J_PER_M = -1.52e43      # VISSER89 p.5
GV_RING_TENSION_N = -3.0257e43      # GV17 p.22


# =============================================================================== 2. stress tensors, energy conditions
#: Orthonormal-frame (rho, p1, p2, p3) per class, in units of the class's own positive scale (set to 1), outside
#: the core under H-THIN.  Axis 3 is along the string; axis 1 is normal to the wall; axis 1 is radial for monopoles.
CLASSES = {
    "string":          {"rho": Fr(1), "p": (Fr(0), Fr(0), Fr(-1)), "scale": "mu (energy per length)",
                        "source": "HK p.53 eq.(4.1)"},
    "wall":            {"rho": Fr(1), "p": (Fr(0), Fr(-1), Fr(-1)), "scale": "sigma (energy per area)",
                        "source": "CGS p.6 eqs.(2.18)-(2.19): sigma = tau"},
    "global monopole": {"rho": Fr(1), "p": (Fr(-1), Fr(0), Fr(0)), "scale": "eta^2 / r^2",
                        "source": "sigma-model T (DURRER p.10 eq.22) on the hedgehog, computed in hedgehog_stress()"},
    "gauge monopole":  {"rho": Fr(1), "p": (Fr(-1), Fr(1), Fr(1)), "scale": "u = B^2/(2 mu0) (radial B)",
                        "source": "Maxwell stress of a radial field (computed in maxwell_radial())"},
    # texture: a time-dependent sigma-model configuration; its energy conditions are the canonical theorem's
    # (section 3), not a fixed (rho, p) -- it is graded through canonical_nec() and derrick().
}
#: A control class, not a defect of any canonical field: the negative-tension string of Visser 1989 / GV17.
NEG_TENSION_STRING = {"rho": Fr(-1), "p": (Fr(0), Fr(0), Fr(1))}


def _mark(x):
    return "SAT" if x > 0 else ("SATURATED" if x == 0 else "VIOLATED")


def energy_conditions(rho, p):
    """NEC per axis (rho + p_i, which is also the minimum over null directions of T_kk for a diagonal T: an equality
    here is attained by a real null vector, so SATURATED); WEC as the infimum over observers of T_uu, which for a
    diagonal T is rho when the NEC holds (T_uu = (rho + v^2 p)/(1 - v^2) is non-decreasing in v^2 iff rho + p >= 0);
    SEC as rho + sum p (attained by the observer at rest) with the NEC; DEC as rho >= |p_i|, where equality is
    BOUNDARY -- the energy flux of every actual observer stays timelike and turns null only in the v -> c limit."""
    nec = [rho + pi for pi in p]
    nec_ok = min(nec) >= 0
    wec = _mark(rho) if nec_ok else "VIOLATED"
    sec_sum = rho + sum(p)
    sec = "VIOLATED" if (sec_sum < 0 or not nec_ok) else _mark(sec_sum)
    dmin = min(rho - abs(pi) for pi in p)
    dec = "VIOLATED" if (rho < 0 or dmin < 0) else ("SAT" if dmin > 0 else "BOUNDARY")
    return {"NEC": [_mark(x) for x in nec], "NEC_min": _mark(min(nec)),
            "WEC": wec, "SEC_sum": _mark(sec_sum), "SEC": sec, "DEC": dec, "rho+sum p": sec_sum}


def wec_grid(row, n=24):
    """min of T_uu = (rho + v^2 sum p_i n_i^2) / (1 - v^2) over observers u = gamma (1, v n), a numeric grid."""
    rho, p = float(row["rho"]), [float(x) for x in row["p"]]
    best = float("inf")
    for i in range(n + 1):
        a = math.pi * i / n
        for j in range(2 * n + 1):
            b = math.pi * j / n
            nn = (math.sin(a) * math.cos(b), math.sin(a) * math.sin(b), math.cos(a))
            for v in (0.0, 0.3, 0.6, 0.9, 0.99, 0.999):
                best = min(best, (rho + v * v * sum(pi * ni * ni for pi, ni in zip(p, nn))) / (1 - v * v))
    return best


def nec_min_over_null(rho, p):
    """min over unit n of rho + sum p_i n_i^2 -- sympy minimisation on the sphere, as an independent check that the
    per-axis NEC equals the full null-cone NEC for a diagonal T."""
    import sympy as sp
    a, b = sp.symbols("a b", real=True)
    n = (sp.sin(a) * sp.cos(b), sp.sin(a) * sp.sin(b), sp.cos(a))
    f = sp.Rational(rho.numerator, rho.denominator) + sum(sp.Rational(pi.numerator, pi.denominator) * ni ** 2
                                                          for pi, ni in zip(p, n))
    vals = [f.subs({a: aa, b: bb}) for aa in (0, sp.pi / 2) for bb in (0, sp.pi / 2)]
    grid = min(float(f.subs({a: math.pi * i / 24, b: math.pi * j / 24})) for i in range(25) for j in range(49))
    return min(sp.nsimplify(v) for v in vals), grid


def hedgehog_stress():
    """The sigma-model stress tensor (DURRER eq.22, T = d phi.d phi - g/2 (d phi)^2) on the static hedgehog
    phi = eta x/r, in the orthonormal (r, theta, phi) frame: (rho, p_r, p_t) in units of eta^2/r^2."""
    import sympy as sp
    x, y, z, eta = sp.symbols("x y z eta", positive=True)
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    phi = [eta * x / r, eta * y / r, eta * z / r]
    grad = [[sp.diff(f, v) for v in (x, y, z)] for f in phi]
    G2 = sp.simplify(sum(grad[A][i] ** 2 for A in range(3) for i in range(3)))
    Tij = [[sp.simplify(sum(grad[A][i] * grad[A][j] for A in range(3)) - (G2 / 2 if i == j else 0))
            for j in range(3)] for i in range(3)]
    pt = {x: 0, y: 0, z: 1}                                  # on the z axis: radial = z, tangential = x, y
    rho = sp.simplify(G2 / 2)
    out = [sp.simplify((q / (eta ** 2 / r ** 2)).subs(pt)) for q in (rho, Tij[2][2], Tij[0][0])]
    return tuple(out)


def maxwell_radial():
    """The Maxwell stress of a purely radial magnetic field in an orthonormal frame (G = mu0 = 1 units):
    (rho, p_r, p_t) / u with u = B^2/2."""
    import sympy as sp
    B = sp.symbols("B", positive=True)
    Bv = (0, 0, B)                                            # radial = axis 3 at the point taken
    u = B ** 2 / 2
    p = [sp.simplify(u - Bv[i] * Bv[i]) for i in range(3)]   # T_ii = -(Maxwell stress) = u delta_ii - B_i B_i
    return sp.simplify(u / u), tuple(sp.simplify(pi / u) for pi in (p[2], p[0], p[1]))


# =============================================================================== 3. the canonical-field NEC theorem
def canonical_nec(kinetic_sign=1):
    """T_kk for N canonical scalars plus a Maxwell field, with k = (1,0,0,1) in Minkowski (-+++), every field
    derivative and field strength a free symbol.  Returns (T_kk, is a sum of squares with non-negative
    coefficients, the potential V drops out).  kinetic_sign = -1 is the phantom control."""
    import sympy as sp
    eta = sp.diag(-1, 1, 1, 1)
    k = sp.Matrix([1, 0, 0, 1])
    V = sp.symbols("V")
    dphi = [sp.Matrix(sp.symbols("d%d_0:4" % A)) for A in range(2)]          # two scalars, lower-index gradients
    Ex, Ey, Ez, Bx, By, Bz = sp.symbols("Ex Ey Ez Bx By Bz", real=True)
    F = sp.Matrix([[0, -Ex, -Ey, -Ez], [Ex, 0, Bz, -By], [Ey, -Bz, 0, Bx], [Ez, By, -Bx, 0]])   # F_{mu nu}
    ginv = eta
    T = sp.zeros(4)
    for d in dphi:
        dd = (d.T * ginv * d)[0]
        T += kinetic_sign * (d * d.T - eta * dd / 2)
    T -= eta * V
    Fsq = sum(F[a, b] * F[c, e] * ginv[a, c] * ginv[b, e] for a in range(4) for b in range(4)
              for c in range(4) for e in range(4))
    TF = sp.Matrix(4, 4, lambda m, n: sum(F[m, a] * F[n, b] * ginv[a, b] for a in range(4) for b in range(4))) \
        - eta * Fsq / 4
    T += TF
    Tkk = sp.expand((k.T * T * k)[0])
    sos = sp.expand(kinetic_sign * sum((d[0] + d[3]) ** 2 for d in dphi) + (Ex - By) ** 2 + (Ey + Bx) ** 2)
    return Tkk, sp.simplify(Tkk - sos) == 0 and kinetic_sign > 0, not Tkk.has(V)


# =============================================================================== 4. geometry
def string_deficit_linear():
    """HK eq.(4.3): h = 8 G mu ln(rho/rho0) diag(0,1,1,0) in (+---); the transverse metric (1 - 8 G mu ln rho)
    (d rho^2 + rho^2 d phi^2).  Computed exactly from the conformal factor rho^(-8 G mu) (its first-order form):
    the circumference / proper-radius ratio of the cone, hence the deficit, to first order in G mu."""
    import sympy as sp
    g, rho, phi = sp.symbols("g rho phi", positive=True)       # g = G mu
    conf = rho ** (-8 * g)                                       # e^{2 psi}, psi = -4 g ln rho
    Rprop = sp.integrate(sp.sqrt(conf), (rho, 0, rho), conds="none")  # proper radius (g < 1/4)
    circ = 2 * sp.pi * rho * sp.sqrt(conf)
    ratio = sp.simplify(circ / Rprop)                           # 2 pi (1 - 4 g)
    deficit = sp.simplify(2 * sp.pi - ratio)
    return deficit, sp.series(deficit, g, 0, 2).removeO()


def string_deficit_with_tension(mu_sym=None):
    """HK eq.(4.6): a string with energy per length mu and tension T has deficit 4 pi G (mu + T) and Newtonian
    potential 4 G (mu - T) ln R: the canonical string (T = mu) gives 8 pi G mu and no force (HK p.84)."""
    import sympy as sp
    G, mu, T = sp.symbols("G mu T", positive=True)
    deficit = 4 * sp.pi * G * (mu + T)
    pot = 4 * G * (mu - T)
    return sp.simplify(deficit.subs(T, mu)), sp.simplify(pot.subs(T, mu)), deficit, pot


def monopole_einstein():
    """ds^2 = -dt^2 + dr^2 + A r^2 dOmega^2 (A = 1 - Delta): the mixed Einstein tensor, exact.  Returns
    (G^t_t, G^r_r, G^th_th) -- so rho = -G^t_t/(8 pi), p_r = G^r_r/(8 pi), p_t = G^th_th/(8 pi)."""
    import sympy as sp
    t, r, th, ph, A = sp.symbols("t r theta phi A", positive=True)
    X = (t, r, th, ph)
    g = sp.diag(-1, 1, A * r ** 2, A * r ** 2 * sp.sin(th) ** 2)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4)
    for b in range(4):
        for c in range(4):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                              for d in range(4)) for a in range(4)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
    Gm = [sp.simplify(sum(gi[i, a] * Ric[a, i] for a in range(4)) - Rs / 2) for i in range(3)]
    return tuple(Gm), A, r


def hedgehog_curved():
    """The sigma-model stress tensor of the hedgehog phi^a = eta n^a(theta, phi) IN the global-monopole metric
    -dt^2 + dr^2 + A r^2 dOmega^2 (D66-fix, V66-2 #1): T_mu_nu = d_mu phi.d_nu phi - g_mu_nu (d phi)^2 / 2, mixed
    components.  Returns (rho, p_r, p_t) with rho = -T^t_t, p_r = T^r_r, p_t = T^th_th, and A, eta, r."""
    import sympy as sp
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    A, eta = sp.symbols("A eta", positive=True)
    X = (t, r, th, ph)
    g = sp.diag(-1, 1, A * r ** 2, A * r ** 2 * sp.sin(th) ** 2)
    gi = g.inv()
    n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    fld = [eta * x for x in n]
    d = [[sp.diff(f, x) for x in X] for f in fld]
    dd = sp.simplify(sum(gi[m, m2] * d[a][m] * d[a][m2] for a in range(3) for m in range(4) for m2 in range(4)))
    T = sp.Matrix(4, 4, lambda m, m2: sum(d[a][m] * d[a][m2] for a in range(3)) - g[m, m2] * dd / 2)
    Tmix = sp.simplify(gi * T)
    return sp.simplify(-Tmix[0, 0]), sp.simplify(Tmix[1, 1]), sp.simplify(Tmix[2, 2]), A, eta, r


def monopole_deficit(consistent=True):
    """Solve G^t_t = -8 pi rho for Delta = 1 - A (G = c = 1).  consistent=True uses hedgehog_curved()'s rho
    (eta^2/(A r^2)); consistent=False is WAVE 1's input, the flat-space density eta^2/r^2, kept as the record of what
    wave 1 did.  Returns the list of solutions for Delta."""
    import sympy as sp
    (Gtt, _Grr, _Gth), A, r = monopole_einstein()
    rho_geom = sp.simplify(-Gtt / (8 * sp.pi))
    D, eta = sp.symbols("Delta eta", positive=True)
    if consistent:
        rho_h, _pr, _pt, A2, eta2, r2 = hedgehog_curved()
        rho_h = rho_h.subs({A2: A, eta2: eta, r2: r})
    else:
        rho_h = eta ** 2 / r ** 2
    return sp.solve(sp.Eq(rho_geom.subs(A, 1 - D), rho_h.subs(A, 1 - D)), D)


def monopole_conjugate(A=0.9, D=10.0, b=1.0, k_scale=1.0, n=200000):
    """D66-fix (V66-1 #4): is the global monopole's axis recrossing a CONJUGATE point?  The spatial metric
    dr^2 + A r^2 dOmega^2 (light rays of the static metric are its geodesics).  A ray from a source on the axis at
    distance D from the centre, impact parameter b, lies in a plane through the axis; unrolled, that plane is a cone of
    total angle 2 pi sqrt(A), on which the ray is straight (r^2 dpsi'/ds = b).  It meets the far axis (polar angle pi,
    unrolled angle pi sqrt(A)) at arclength s_axis.  The out-of-plane Jacobi field obeys J'' + K J = 0 with the
    sectional curvature K = sin^2(alpha) (1 - A)/(A r^2) = b^2 (1 - A)/(A r^4) (K_radial = 0, K_tangential =
    (1 - A)/(A r^2) for dr^2 + f^2 dOmega^2 with f = sqrt(A) r).  J(0) = 0, J'(0) = 1, integrated (RK4); its first
    zero s_J is a conjugate point.  Returns (s_axis or None, s_J or None).  k_scale != 1 is the CONTROL (a wrong
    curvature must miss the axis crossing); A = 1 is the flat CONTROL (no recrossing, no zero)."""
    sq = math.sqrt(A)
    psi_c = math.acos(b / D)
    s_axis = None
    if math.pi * sq - psi_c < math.pi / 2:
        r_far = b / math.cos(math.pi * sq - psi_c)
        s_axis = math.sqrt(D * D - b * b) + math.sqrt(r_far * r_far - b * b)
    s0 = math.sqrt(D * D - b * b)                       # arclength to the closest approach

    def rad(s):
        return math.sqrt(b * b + (s - s0) ** 2)

    def K(s):
        return k_scale * b * b * (1 - A) / (A * rad(s) ** 4)
    smax = (s_axis * 1.5) if s_axis else 20 * D
    h = smax / n
    J, Jp, s = 0.0, 1.0, 0.0
    for _ in range(n):
        def f(ss, y, yp):
            return yp, -K(ss) * y
        k1 = f(s, J, Jp)
        k2 = f(s + h / 2, J + h / 2 * k1[0], Jp + h / 2 * k1[1])
        k3 = f(s + h / 2, J + h / 2 * k2[0], Jp + h / 2 * k2[1])
        k4 = f(s + h, J + h * k3[0], Jp + h * k3[1])
        Jn = J + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        Jpn = Jp + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if J > 0 and Jn <= 0:
            return s_axis, s + h * J / (J - Jn)
        J, Jp, s = Jn, Jpn, s + h
    return s_axis, None


def monopole_deflection():
    """DURRER eq.(38): alpha = eps INT b/(lambda^2 + b^2) d lambda = eps pi, independent of b."""
    import sympy as sp
    lam, b, eps = sp.symbols("lambda b epsilon", positive=True)
    return sp.simplify(eps * sp.integrate(b / (lam ** 2 + b ** 2), (lam, -sp.oo, sp.oo)))


def wall_split():
    """The thin vacuum wall (normal x): T^mu_nu = sigma delta(x) diag(-1, 0, -1, -1) in (-+++), G = c = 1.  Returns
    (R_uu for a static observer, R_kk for a null ray crossing normally, R_kk along the wall, Tolman Sigma) per unit
    sigma delta: R_mu_nu = 8 pi (T_mu_nu - T g_mu_nu / 2)."""
    import sympy as sp
    s = sp.symbols("sigma", positive=True)
    eta = sp.diag(-1, 1, 1, 1)
    Tmix = sp.diag(-s, 0, -s, -s)
    Tlow = eta * Tmix
    trT = sum(Tmix[i, i] for i in range(4))
    Rlow = 8 * sp.pi * (Tlow - eta * trT / 2)
    u = sp.Matrix([1, 0, 0, 0])
    kn = sp.Matrix([1, 1, 0, 0])
    kw = sp.Matrix([1, 0, 1, 0])
    Ruu = sp.simplify((u.T * Rlow * u)[0] / s)
    Rkn = sp.simplify((kn.T * Rlow * kn)[0] / s)
    Rkw = sp.simplify((kw.T * Rlow * kw)[0] / s)
    tolman = sp.simplify((-Tmix[0, 0] - (-Tmix[2, 2]) - (-Tmix[3, 3]) ) / s)   # sigma - 2 tau with tau = sigma
    return Ruu, Rkn, Rkw, tolman


def wall_thin_lens(sign=1):
    """A planar null congruence crossing the wall normally (shear-free, twist-free by symmetry): theta jumps by
    -INT R_kk = -8 pi sigma (sign = -1 is the negative-tension control), then d theta/d lambda = -theta^2/2.
    Returns the affine distance to the caustic (sympy), or None if theta never diverges ahead."""
    import sympy as sp
    s, lam = sp.symbols("sigma lambda", positive=True)
    th0 = -8 * sp.pi * s * sign
    th = sp.Function("th")
    sol = sp.dsolve(sp.Eq(th(lam).diff(lam), -th(lam) ** 2 / 2), th(lam), ics={th(0): th0})
    expr = sp.simplify(sol.rhs)
    den = sp.solve(sp.Eq(1 / expr, 0), lam)
    ahead = [d for d in den if d.is_positive]
    return (ahead[0] if ahead else None), expr


def vis_beta():
    """CGS p.10: kappa sigma = 4 beta for the Vilenkin-Ipser-Sikivie wall, kappa = 8 pi G / c^4 -> beta = 2 pi G
    sigma / c^4 (inverse length); the wall worldsheet's de Sitter radius is 1/beta."""
    import sympy as sp
    G, c, s = sp.symbols("G c sigma", positive=True)
    return sp.simplify(8 * sp.pi * G / c ** 4 * s / 4)


def vis_time_function(beta_sign=1, exponent=2):
    """D66-fix (V66-1 #3): the thin non-extreme M4-M4 wall's global causal structure, from CGS p.15 eq.(3.48) and
    Fig.4 (READ).  Comoving metric on each side, (-+++), G = c = 1:  g = e^(-2 b |z|) (-dt^2 + dz^2 + b^-2 cosh^2(b t)
    dOmega^2).  [CGS print the conformal factor of eq.(3.48) (p.15) as e^(-+ b z); their own transformation t_in =
    b^-1 e^(-b z) sinh(b t), r_in = b^-1 e^(-b z) cosh(b t) maps to Minkowski only with e^(-2 b |z|) -- checked below as
    the pullback.  CGS's own Appendix A settles the factor: eqs.(A.12)-(A.13) (printed p.21) give the same transformation
    with e^(+-2 b z), and p.8 writes the M4 side as A = e^(+2 b z): the 2 is the source's, and (3.48)'s printed exponent
    is a misprint there (READ via alphaXiv answer_pdf_queries, open arXiv PDF gr-qc/9306005v1, by D66-repro and again
    at R-apply 2026-10-04).  D66-fix first recorded this as 'a reading note, not a finding against CGS' (text
    extraction may have dropped a 2).]  Per side s = sign(z):
      (1) the pullback of -dT^2 + dR^2 + R^2 dOmega^2 under T = b^-1 e^(-b s z) sinh(b t), R = b^-1 e^(-b s z)
          cosh(b t) equals g (each side is Minkowski, T its inertial time);
      (2) g^(mu nu) dT dT = -1 (T a time function on each side) and dT/dt > 0 at z = 0 (time orientations agree);
      (3) T is continuous across z = 0 (the same function of (t, angles) on the wall from both sides);
      (4) Israel: S_ij = -(1/kappa)([K_ij] - h_ij [K]) = -sigma h_ij with kappa sigma = 4 b (CGS p.10's relation).
    A continuous function strictly increasing along every future causal curve on each side increases along every
    future causal curve of the glued spacetime: no closed causal curve (H-VIS-MINKOWSKI: no identification).
    CONTROL R: g^(mu nu) dR dR = +1 (spacelike gradient: the test can fail).  beta_sign = -1: kappa sigma < 0.
    CONTROL exponent = 1 (the conformal factor as printed, e^(-b|z|)): the pullback is NOT g."""
    import sympy as sp
    t, z, th, ph = sp.symbols("t z theta phi", real=True)
    b = sp.Symbol("beta", positive=True) * beta_sign
    out = {}
    for s in (1, -1):
        conf = sp.exp(-exponent * b * s * z)
        g = sp.diag(-conf, conf, conf * sp.cosh(b * t) ** 2 / b ** 2, conf * sp.cosh(b * t) ** 2 * sp.sin(th) ** 2 / b ** 2)
        X = (t, z, th, ph)
        T = sp.exp(-b * s * z) * sp.sinh(b * t) / b
        R = sp.exp(-b * s * z) * sp.cosh(b * t) / b
        mink = sp.diag(-1, 1, R ** 2, R ** 2 * sp.sin(th) ** 2)
        Y = [T, R, th, ph]
        Jac = sp.Matrix(4, 4, lambda i, j: sp.diff(Y[i], X[j]))
        pull = sp.simplify(Jac.T * mink * Jac - g)
        gi = g.inv()
        dT = [sp.diff(T, x) for x in X]
        dR = [sp.diff(R, x) for x in X]
        nT = sp.simplify(sum(gi[i, j] * dT[i] * dT[j] for i in range(4) for j in range(4)))
        nR = sp.simplify(sum(gi[i, j] * dR[i] * dR[j] for i in range(4) for j in range(4)))
        h = g.extract([0, 2, 3], [0, 2, 3])
        nz = 1 / sp.sqrt(g[1, 1])
        Kij = sp.simplify((nz * sp.diff(h, z) / 2).subs(z, 0))
        out[s] = {"pullback_is_g": pull == sp.zeros(4), "gTT": nT, "gRR": nR,
                  "dT/dt at z=0": sp.simplify(sp.diff(T, t).subs(z, 0)), "T at z=0": sp.simplify(T.subs(z, 0)),
                  "K_ij": Kij, "h0": sp.simplify(h.subs(z, 0))}
    h0 = out[1]["h0"]
    jump = sp.simplify(out[1]["K_ij"] - out[-1]["K_ij"])
    hinv = h0.inv()
    trj = sp.simplify(sum(hinv[i, j] * jump[i, j] for i in range(3) for j in range(3)))
    kap = sp.Symbol("kappa", positive=True)
    S = sp.simplify(-(jump - h0 * trj) / kap)
    sigma = sp.simplify(-S[0, 0] / h0[0, 0])
    out["continuous at z=0"] = sp.simplify(out[1]["T at z=0"] - out[-1]["T at z=0"]) == 0
    out["S_ij = -sigma h_ij"] = sp.simplify(S + sigma * h0) == sp.zeros(3)
    out["kappa sigma"] = sp.simplify(kap * sigma)
    return out


def derrick(d):
    """E(lambda) = lambda^(d-2) I1 + lambda^d I2 for phi(x/lambda) in d space dimensions (DURRER p.9 for d = 3).
    Returns dE/dlambda at 1, and whether a static stationary point can exist with I1 > 0, I2 >= 0."""
    import sympy as sp
    l, I1, I2 = sp.symbols("lambda I1 I2", nonnegative=True)
    E = l ** (d - 2) * I1 + l ** d * I2
    dE = sp.expand(sp.diff(E, l).subs(l, 1))
    # stationary iff (d-2) I1 + d I2 = 0 has a solution with I1 > 0, I2 >= 0
    import z3
    a, b = z3.Reals("a b")
    S = z3.Solver()
    S.add(a > 0, b >= 0, (d - 2) * a + d * b == 0)
    return dE, S.check() == z3.sat


# =============================================================================== 5. the seat tests
def specthm_sturm_sentence():
    """specthm.py's own statement of the Sturm condition, read from its source (so a moved owner is caught)."""
    src = open(own("specthm").__file__, encoding="utf-8").read()
    return "4 pi G T_kk s^2/c^4 >= pi^2" in src


def sturm_bounds():
    """The best Sturm number K s^2 (K = 4 pi G T_kk / c^4; certifies iff >= pi^2) each class can reach, exact,
    G = c = 1, and where certification would put the class:
      string outside the core: T_kk = 0 on every ray that misses the core -> 0;
      string core (H-UNIFORM-CORE, radius w, chord 2w): 16 mu (T_kk = u) and 32 mu (member T_kk = 2u);
      global monopole: sup over chords of K_min s^2 = 2 eps (eps = 8 pi eta^2);
      thick uniform wall, width w crossed normally: 4 pi sigma w = 2 beta w;
      gauge monopole exterior: sup over chords Q^2/b^2 (tangential T_kk = 2u, u = Q^2/(8 pi r^4))."""
    import sympy as sp
    mu, eta, sig, w, b, s, Q = sp.symbols("mu eta sigma w b s Q", positive=True)
    out = {}
    out["string, outside the core"] = sp.Integer(0)
    u_core = mu / (sp.pi * w ** 2)
    out["string core, T_kk = u"] = sp.simplify(4 * sp.pi * u_core * (2 * w) ** 2)
    out["string core, T_kk = 2u"] = sp.simplify(4 * sp.pi * 2 * u_core * (2 * w) ** 2)
    eps = 8 * sp.pi * eta ** 2
    Kmin_s2 = 4 * sp.pi * eta ** 2 / (b ** 2 + s ** 2 / 4) * s ** 2           # T_kk <= eta^2/r^2, r_max^2 = b^2+s^2/4
    out["global monopole (sup over chords)"] = sp.simplify(sp.limit(Kmin_s2, s, sp.oo) / eps) * sp.Symbol("eps")
    out["thick wall, width w"] = sp.simplify(4 * sp.pi * (sig / w) * w ** 2)
    Kgm = 4 * sp.pi * 2 * Q ** 2 / (8 * sp.pi * (b ** 2 + s ** 2 / 4) ** 2)  # tangential T_kk = 2u at r_max
    smax = sp.solve(sp.diff(Kgm * s ** 2, s), s)
    smax = [x for x in smax if x.is_positive][0]
    out["gauge monopole exterior (sup over chords)"] = sp.simplify((Kgm * s ** 2).subs(s, smax))
    return out


def sturm_limits():
    """What Sturm certification (K s^2 >= pi^2) would require of each class, against the class's own gravitational
    limit, exact:
      string core: mu >= pi^2/16 (T_kk = u) or pi^2/32 (2u), against the cone closing at mu = 1/4 (deficit 2 pi);
      global monopole: eps >= pi^2/2, against eps < 1 (solid angle 4 pi (1 - eps) > 0);
      thick wall: beta w >= pi^2/4 ... with beta = 2 pi sigma: 4 pi sigma w = 2 beta w >= pi^2 -> w >= pi^2/(2 beta);
      gauge monopole: Q/b >= pi, i.e. field energy outside b, Q^2/(2b), >= pi^2 b / 2 -> 2 M_out / b >= pi^2 > 1."""
    import sympy as sp
    pi2 = sp.pi ** 2
    return {
        "string core T_kk = u: mu needed": pi2 / 16, "string core T_kk = 2u: mu needed": pi2 / 32,
        "string: cone closes at mu": sp.Rational(1, 4),
        "global monopole: eps needed": pi2 / 2, "global monopole: eps limit": sp.Integer(1),
        "thick wall: beta w needed": pi2 / 2,
        "gauge monopole: Q/b needed": sp.pi, "gauge monopole: 2 M_out / b at certification": pi2,
    }


def string_crossing(gmu, b):
    """Two parallel rays at impact b on opposite sides of a straight string, each turned inward by 4 pi G mu
    (HK p.90, independent of b): they cross at L = b / tan(4 pi G mu).  L is linear in b: no caustic, no single
    focus (contrast spec.py's S-1 lens, f = b^2 c^2 / (4 G M), quadratic in b)."""
    return b / math.tan(4 * math.pi * gmu)


#: M's ruling on spec.py's PART 2 'TURN' (docket68/M-RULINGS-2026-10-03.md item 27, verbatim: "Asked whether TURN means
#: a genuine conjugate point or any crossing of light paths, M: "Any crossing". H-TURN-CROSSING is adopted; the straight
#: cosmic string TURNs (rays cross without focusing).").  The two readings stay defined in HYPOTHESES as they were;
#: H-TURN-CONJUGATE is kept as the alternative on record.  D66-fix first said 'the string's grade under the board's
#: TURN is still M's to rule'.
TURN_RULING = {"M": "Any crossing", "source": "docket68/M-RULINGS-2026-10-03.md item 27 (2026-10-04)",
               "adopted": "H-TURN-CROSSING", "alternative on record": "H-TURN-CONJUGATE",
               "first said": "D66-fix: a TURN under H-TURN-CROSSING, none under H-TURN-CONJUGATE; the reading M's to rule"}


def turn_under(reading, crossing_at, conjugate_at):
    """Does a class TURN under a reading of spec.py's PART 2?  crossing_at: the distance at which two rays from one
    side-pair meet again (None if they never do); conjugate_at: the distance of a conjugate point (None if there is
    none).  H-TURN-CROSSING (adopted, M-RULINGS item 27): a TURN iff the rays meet again at a finite distance.
    H-TURN-CONJUGATE (the alternative on record): a TURN iff a conjugate point exists.  Returns (verdict, at)."""
    if reading == "H-TURN-CROSSING":
        ok = crossing_at is not None and math.isfinite(crossing_at) and crossing_at > 0
        return ("TURN" if ok else "NO TURN"), (crossing_at if ok else None)
    if reading == "H-TURN-CONJUGATE":
        ok = conjugate_at is not None
        return ("TURN" if ok else "NO TURN"), (conjugate_at if ok else None)
    raise ValueError(reading)


def string_turn(gmu, b):
    """The straight static string under both readings (M ruled 'Any crossing').  Crossing: string_crossing (HK p.90:
    each ray turned inward by 4 pi G mu, independent of b), computed here and cross-checked by intersecting the two
    deflected rays as lines (y = b - x tan d, y = -b + x tan d) by Cramer's rule; for G mu = 0 no deflection and no
    crossing.  Conjugate point: none -- neighbouring rays on one side are deflected by the same angle (d(deflection)/db
    = 0, a flat cone: J'' = 0), so a one-sided congruence stays parallel (checked as string_crossing linear in b)."""
    d = 4 * math.pi * gmu
    L = string_crossing(gmu, b) if gmu > 0 else None
    # independent: the two deflected rays as lines a1 x + b1 y = c1, a2 x + b2 y = c2
    t = math.tan(d)
    det = t * 1.0 - (-t) * 1.0                     # rows (tan d, 1 | b) and (-tan d, 1 | -b)
    x_int = ((b * 1.0 - 1.0 * (-b)) / det) if det != 0 else None
    out = {"G mu": gmu, "b": b, "deflection rad": d, "crossing L": L, "crossing L (line intersection)": x_int,
           "conjugate point": None}
    for rd in ("H-TURN-CROSSING", "H-TURN-CONJUGATE"):
        out[rd] = turn_under(rd, L, None)
    out["verdict under the ruling (H-TURN-CROSSING adopted)"] = out["H-TURN-CROSSING"][0]
    return out


E_CHARGE_SI = 1.602176634e-19      # C, the SI 2019 DEFINITION of the coulomb (a unit definition, exact)
ALPHA_GUT = 1.0 / 40.0            # H-MONOPOLE-MASS (a named hypothesis, not a READ value)


def gauge_monopole_lens(m_gev=1e17, focus_m=None, ratio_gate=1e-15):
    """D66-fix (V66-1 #5): the gauge monopole's lensing seat through the OWNER's formula spec.focal_length
    (f = b^2 c^2 / (4 G M)).  For a monopole of mass m_gev GeV/c^2 (H-MONOPOLE-MASS): the impact parameter b whose
    focus lies at focus_m (default 1 AU, spec.AU), found by inverting the owner's function and checked by calling it;
    r_s = 2GM/c^2; core radius (1/alpha_GUT) hbar/(M c); the magnetic field energy beyond b for the Dirac charge
    g_D = h/e, E_out = g_D^2/(8 pi mu0 b) (spec.MU0), as a fraction of Mc^2.  S-1 placement needs b >> r_core
    (H_seat: b >= the lens radius), b >> r_s (H-WEAK-FIELD) and the field energy beyond b negligible (H-S1-VACUUM)."""
    spec = own("spec")
    ach = own("achievable")
    G, c = spec.G_SI, spec.C_SI
    f = focus_m if focus_m is not None else spec.AU
    M = m_gev * 1e9 * E_CHARGE_SI / c ** 2
    b = math.sqrt(4 * G * M * f) / c
    f_back = spec.focal_length(M, b)
    r_s = 2 * G * M / c ** 2
    r_core = (1 / ALPHA_GUT) * ach.HBAR / (M * c)
    g_dirac = ach.H_PLANCK / E_CHARGE_SI
    e_out = g_dirac ** 2 / (8 * math.pi * spec.MU0 * b)
    frac = e_out / (M * c * c)
    ok = (b / r_core > 1e3) and (b / r_s > 1e3) and frac < ratio_gate
    return {"m_gev": m_gev, "M_kg": M, "focus_m": f, "b_m": b, "focal_check": f_back / f, "r_s_m": r_s,
            "r_core_m": r_core, "b_over_core": b / r_core, "b_over_rs": b / r_s,
            "field_energy_beyond_b_over_Mc2": frac, "S-1 conditions hold": ok}


def cone_shortcut(gmu):
    """Two points at radius r on opposite sides (angle pi) of a straight string: the geodesic in the cone has
    length 2 r cos(Delta/4) against 2 r in flat space (Delta = 8 pi G mu).  Returns 1 - cos(Delta/4)."""
    return 1.0 - math.cos(8 * math.pi * gmu / 4)


def spinning_ctc():
    """DLM04 eqs.(2)-(3) in (-+++): g_theta_theta = alpha^2 r^2 + kappa^2 - S^2.  The closed theta-circle is timelike
    iff g_theta_theta < 0.  Returns (radius of the CTC region without dislocation, with dislocation)."""
    import sympy as sp
    r, S, al, ka = sp.symbols("r S alpha kappa", positive=True)
    t, xi, th = sp.symbols("tau xi theta")
    dtau, dr, dth, dxi = sp.symbols("dtau dr dtheta dxi")
    ds2 = -(dtau + S * dth) ** 2 + dr ** 2 + al ** 2 * r ** 2 * dth ** 2 + (dxi + ka * dth) ** 2
    gthth = sp.expand(sp.diff(ds2, dth, 2) / 2)
    r0 = sp.solve(sp.Eq(gthth.subs(ka, 0), 0), r)
    r1 = sp.solve(sp.Eq(gthth, 0), r)
    return gthth, [x for x in r0 if x.is_positive] or r0, r1


def gott_gamma_needed(gmu):
    """CFG94 eq.(32): CTCs iff cosh(xi) sin(alpha/2) > 1, alpha = 8 pi G mu.  The Lorentz factor needed."""
    return 1.0 / math.sin(8 * math.pi * gmu / 2)


def static_is_stably_causal():
    """A static metric -N^2 dt^2 + h_ij dx^i dx^j with N > 0: g^tt = -1/N^2 < 0, so t is a time function and the
    spacetime is stably causal -- no closed causal curve.  Checked for the string cone, the global monopole, and the
    Reissner-Nordstrom exterior (N^2 = 1 - 2M/r + Q^2/r^2 > 0 outside r_+)."""
    import sympy as sp
    r, A, M, Q, D = sp.symbols("r A M Q Delta", positive=True)
    th = sp.symbols("theta", positive=True)
    mets = {"string cone": sp.diag(-1, 1, (1 - D) ** 2 * r ** 2, 1),
            "global monopole": sp.diag(-1, 1, A * r ** 2, A * r ** 2 * sp.sin(th) ** 2),
            "RN exterior": sp.diag(-(1 - 2 * M / r + Q ** 2 / r ** 2), 1 / (1 - 2 * M / r + Q ** 2 / r ** 2),
                                   r ** 2, r ** 2 * sp.sin(th) ** 2)}
    out = {}
    for k, g in mets.items():
        out[k] = sp.simplify(g.inv()[0, 0])
    return out


def jackiw_rebbi(g_sign=1):
    """The zero mode of a Dirac fermion with Yukawa mass g phi(x) on a kink phi = v tanh(x/w) (v = w = 1):
    psi = exp(-g INT phi) = cosh(x)^(-g).  Returns (psi, INT psi^2 or None, psi at +-oo, the mass at the core).
    Normalisable iff psi -> 0 at both ends; g_sign = -1 is the control (wrong sign: psi grows, not normalisable)."""
    import sympy as sp
    x = sp.symbols("x", real=True)
    g = sp.Integer(g_sign)
    phi = sp.tanh(x)
    anti = sp.log(sp.cosh(x))
    assert sp.simplify(sp.diff(anti, x) - phi) == 0          # INT tanh = ln cosh, checked, not assumed
    psi = sp.cosh(x) ** (-g)
    ends = (sp.limit(psi, x, sp.oo), sp.limit(psi, x, -sp.oo))
    norm = sp.integrate(psi ** 2, (x, -sp.oo, sp.oo)) if ends == (0, 0) else None
    return psi, norm, ends, sp.simplify((g * phi).subs(x, 0))


def zero_mode_speed():
    """ETO25 eq.(3.57): psi ~ exp(-i k (t - z)): omega = k, group velocity d omega/dk = 1 (c)."""
    import sympy as sp
    k, t, z = sp.symbols("k t z", real=True)
    psi = sp.exp(-sp.I * k * (t - z))
    omega = sp.simplify(sp.I * sp.diff(psi, t) / psi)
    kk = sp.simplify(-sp.I * sp.diff(psi, z) / psi)
    return sp.diff(omega, k) / sp.diff(kk, k)


# =============================================================================== 6. the D68 bookkeeping (z3)
def screen(mutate=None):
    """A small z3 encoding of what H-DEFECT-SEAT can do to O-HOLD, O-SEAT and the seat condition, with the theorems
    as constraints and the OPEN pathways as free atoms.  Bookkeeping over findings owned elsewhere (each atom's
    ground is in GROUNDS), not new physics.  mutate: 'drop-FSW' (the theorem removed), 'neg-asserted' (negative
    tension asserted with no pathway), 'defb-asserted' (supply asserted with no pathway), 'spin-ok' (a spinning
    string's CTC ignored) -- each must change a verdict, and the checks say which."""
    import z3
    B = {n: z3.Bool(n) for n in ("CANON", "NEGT", "N_NEGT", "NECVIOL", "THROAT_HELD", "S5SUP", "N_S5", "DEFSUP",
                                 "N_DEFB", "SEAT_OK", "CTC", "TOPOCHG", "SPIN_INSIDE", "STATIC", "MADE_THROAT",
                                 "TOPOCHG_THR", "PATH_THR", "N_WNCC")}
    cons = []
    # O-HOLD: a held traversable throat in a globally hyperbolic asymptotically flat spacetime needs ANEC/NEC
    # violation (FSW93 Thm 1; GV17 p.3; VISSER89 p.4); canonical fields satisfy the NEC (canonical_nec()).
    if mutate != "drop-FSW":
        cons.append(z3.Implies(B["THROAT_HELD"], B["NECVIOL"]))
    cons.append(z3.Implies(B["CANON"], z3.Not(B["NECVIOL"]) if mutate != "neg-asserted" else True))
    cons.append(z3.Implies(B["NECVIOL"], B["NEGT"]))                     # in this screen the only NEC-violating
    cons.append(z3.Implies(B["NEGT"], B["N_NEGT"] if mutate != "neg-asserted" else True))   # source is N_NEGT
    # O-SEAT: removed iff a supply is shown -- the board's S5 (open, N_S5) or a defect supply (open, N_DEFB).
    cons.append(z3.Implies(B["S5SUP"], B["N_S5"]))
    cons.append(z3.Implies(B["DEFSUP"], B["N_DEFB"] if mutate != "defb-asserted" else True))
    # M-S1A-P3 (i) at the seat: no closed causal curve and no Borde pathology (topology change) at the seat.
    cons.append(z3.Implies(B["SEAT_OK"], z3.And(z3.Not(B["CTC"]), z3.Not(B["TOPOCHG"]))))
    cons.append(z3.Implies(B["STATIC"], z3.Not(B["CTC"])))                # static_is_stably_causal()
    if mutate != "spin-ok":
        cons.append(z3.Implies(B["SPIN_INSIDE"], B["CTC"]))               # spinning_ctc(), DLM04
    # O-MAKE-TOPO for a string-supported throat MADE from flat space (D66-fix, V66-1 #1): a topology change
    # (create.is_topology_change(False, True)); Geroch / Borde force a pathology with no matter assumption
    # (create.GEROCH_NEEDS_MATTER_ASSUMPTION False), placed AT THE THROAT.  M's ruling (ledger M-S1A-P3): 'a singular
    # throat is not disqualified' and 'the throat-creation classes stay OPEN' -- so the pathology at the throat does not
    # disqualify, and a made throat is realised only through specthm's OPEN class W-create-ncc (N_WNCC).
    cons.append(z3.Implies(B["MADE_THROAT"], B["TOPOCHG_THR"]))
    cons.append(z3.Implies(B["TOPOCHG_THR"], B["PATH_THR"]))
    if mutate == "ruling-dropped":                                        # CONTROL: the ruling ignored
        cons.append(z3.Not(B["PATH_THR"]))
    cons.append(z3.Implies(B["MADE_THROAT"], B["N_WNCC"] if mutate != "wncc-asserted" else True))
    return z3, B, cons


def ask(z3, B, cons, extra):
    s = z3.Solver()
    s.add(*cons)
    s.add(*extra)
    return s.check() == z3.sat


def grades(mutate=None):
    """The verdicts, each derived by z3: is the removal possible (a) with the OPEN pathways held false,
    (b) with them free.  REMOVED-IF needs (a) unsat and (b) sat; LEFT needs (b) unsat; OPEN = possible only via
    an OPEN pathway."""
    z3, B, cons = screen(mutate)
    held_false = [z3.Not(B["N_NEGT"]), z3.Not(B["N_S5"]), z3.Not(B["N_DEFB"]), z3.Not(B["N_WNCC"])]
    out = {"vacuity: board SAT": ask(z3, B, cons, []),
           "vacuity: canonical + no throat SAT": ask(z3, B, cons, [B["CANON"], z3.Not(B["THROAT_HELD"])])}
    # O-HOLD with a defect as the throat's support
    canon_hold = ask(z3, B, cons, [B["CANON"], B["THROAT_HELD"]])
    neg_hold_free = ask(z3, B, cons, [z3.Not(B["CANON"]), B["THROAT_HELD"]])
    neg_hold_fixed = ask(z3, B, cons, [z3.Not(B["CANON"]), B["THROAT_HELD"]] + held_false)
    out["O-HOLD, defect as throat support, given H-CANONICAL"] = "LEFT" if not canon_hold else "NOT LEFT"
    out["O-HOLD, defect as throat support, outside H-CANONICAL"] = (
        "OPEN via N_NEGT" if (neg_hold_free and not neg_hold_fixed) else
        ("REMOVED-IF (no pathway needed)" if neg_hold_fixed else "LEFT"))
    # O-SEAT with a defect at the seat
    seat_free = ask(z3, B, cons, [z3.Or(B["S5SUP"], B["DEFSUP"])])
    seat_fixed = ask(z3, B, cons, [z3.Or(B["S5SUP"], B["DEFSUP"])] + held_false)
    out["O-SEAT, defect at the seat"] = ("OPEN via N_S5 | N_DEFB" if seat_free and not seat_fixed else
                                         ("REMOVABLE with no pathway" if seat_fixed else "LEFT"))
    # O-MAKE-TOPO for a made string-supported throat (M-S1A-P3 applied: the pathology sits at the throat)
    mk_free = ask(z3, B, cons, [B["MADE_THROAT"]])
    mk_fixed = ask(z3, B, cons, [B["MADE_THROAT"]] + held_false)
    out["O-MAKE-TOPO, defect-supported throat made from flat space"] = (
        "OPEN via N_WNCC" if mk_free and not mk_fixed else ("REMOVABLE with no pathway" if mk_fixed else "LEFT"))
    # the seat condition
    out["seat condition, static straight string / monopole"] = (
        "PASSES (CTC-free)" if not ask(z3, B, cons, [B["STATIC"], B["CTC"]]) else "CTC possible")
    out["seat condition, inside a spinning string's CTC radius"] = (
        "DISQUALIFIED (M-S1A-P3 (i))" if not ask(z3, B, cons, [B["SPIN_INSIDE"], B["SEAT_OK"]]) else "admitted")
    return out


# =============================================================================== 7. the report
def figures():
    """Every figure the report prints, each computed here or asked of its owner at call time."""
    spec = own("spec")
    G, c = spec.G_SI, spec.C_SI
    F = {}
    # HK fixtures recomputed
    F["deficit arcsec at G mu = 1e-6"] = 8 * math.pi * 1e-6 * 180 / math.pi * 3600
    F["mu kg/m at G mu = 1e-6"] = 1e-6 * c * c / G
    for k, gmu in (("NG", PLANCK_NG_GMU), ("NG+highl", PLANCK_NG_GMU_HIGHL), ("AH", PLANCK_AH_GMU)):
        F["deficit rad at Planck %s bound" % k] = 8 * math.pi * gmu
        F["mu kg/m at Planck %s bound" % k] = gmu * c * c / G
        F["mu c^2 J/m at Planck %s bound" % k] = gmu * c ** 4 / G
    gmu = PLANCK_NG_GMU
    sun = [x for x in spec.LENSES if x[0] == "Sun"][0]
    F["Sun focal (spec.focal_length) AU"] = spec.focal_length(sun[1], sun[2]) / spec.AU
    F["string crossing at b = R_sun, Planck NG bound, AU"] = string_crossing(gmu, sun[2]) / spec.AU
    F["string crossing at b = 1 m, Planck NG bound, m"] = string_crossing(gmu, 1.0)
    F["string crossing at b = 1 AU, Planck NG bound, ly"] = string_crossing(gmu, spec.AU) / spec.LIGHT_YEAR
    F["cone shortcut 1 - cos(Delta/4) at Planck NG bound"] = cone_shortcut(gmu)
    F["Gott gamma needed at Planck NG bound"] = gott_gamma_needed(gmu)
    F["Gott 1 - v needed at Planck NG bound"] = 1.0 / (2 * gott_gamma_needed(gmu) ** 2)
    # walls: what a 1 AU thin-lens focus or a 1 AU de Sitter radius needs
    F["wall sigma J/m^2 for thin-lens focus 1 AU"] = c ** 4 / (4 * math.pi * G * spec.AU)
    F["wall sigma J/m^2 for de Sitter radius 1 AU"] = c ** 4 / (2 * math.pi * G * spec.AU)
    # wormhole literature recomputed
    jup = [x for x in spec.LENSES if x[0] == "Jupiter"][0]
    F["GV ring |T| = c^4/(4G) N"] = c ** 4 / (4 * G)
    F["GV 1 m ring 2 pi R |T| / c^2 kg"] = 2 * math.pi * 1.0 * c ** 4 / (4 * G) / c ** 2
    F["GV 1 m ring / Jupiter (spec.LENSES)"] = F["GV 1 m ring 2 pi R |T| / c^2 kg"] / jup[1]
    F["Visser cube edge c^4/(8G) J/m"] = c ** 4 / (8 * G)
    # FKZ time-machine scale: an Earth-mass shell of Earth radius round one mouth, mouths 1 ly apart
    earth = [x for x in spec.LENSES if x[0] == "Earth"][0]
    F["FKZ T ~ R L c/(G M) yr, Earth shell, L = 1 ly"] = (earth[2] * spec.LIGHT_YEAR * c / (G * earth[1])
                                                         / (spec.LIGHT_YEAR / c))
    # D66-fix: the global monopole's conjugate point, and the gauge monopole's S-1 lens
    s_ax, s_j = monopole_conjugate()
    F["global monopole conjugate point: |s_J/s_axis - 1|"] = abs(s_j / s_ax - 1)
    gl = gauge_monopole_lens()
    F["gauge monopole 1e17 GeV: b for a 1 AU focus, m"] = gl["b_m"]
    F["gauge monopole 1e17 GeV: field energy beyond b / Mc^2"] = gl["field_energy_beyond_b_over_Mc2"]
    return F


def report(write_json=None):
    import sympy as sp
    F = figures()
    ec = {k: energy_conditions(v["rho"], v["p"]) for k, v in CLASSES.items()}
    ec["CONTROL negative-tension string"] = energy_conditions(NEG_TENSION_STRING["rho"], NEG_TENSION_STRING["p"])
    sb = {k: str(v) for k, v in sturm_bounds().items()}
    lim = {k: str(v) for k, v in sturm_limits().items()}
    gr = grades()
    focal, _ = wall_thin_lens()
    massform = own("massform")
    seat = own("seat")
    grade_rows = SEAT_GRADES()
    out = {"id": "A1-defects", "hypothesis": "H-DEFECT-SEAT", "grades": a1_grades(), "history": HISTORY,
           "energy_conditions": ec, "sturm_bounds": sb,
           "sturm_limits": lim, "wall_thin_lens_focal_over_sigma^-1": str(focal), "z3_grades": gr,
           "figures": F, "seat_grades": grade_rows, "board_O_SEAT": seat.grade_o_seat(seat.board_state()),
           "massform": {"STABLE_RANGE": massform.STABLE_RANGE,
                        "HELD_SEAT_ROUTE_PRICED": massform.HELD_SEAT_ROUTE_PRICED,
                        "HIGGS_SHARE_LARGEST_READ": massform.HIGGS_SHARE_LARGEST_READ},
           "hypotheses": HYPOTHESES, "sources": {k: list(v) for k, v in SOURCES.items()},
           "turn_ruling": TURN_RULING,
           "string_turn (Planck NG bound, b = R_sun)": string_turn(PLANCK_NG_GMU,
                                                                   [x for x in own("spec").LENSES if x[0] == "Sun"][0][2])}
    print("DOCKET 66 / A1 -- H-DEFECT-SEAT alone\n")
    print("Energy conditions (orthonormal frame, outside the core, H-THIN):")
    for k, v in ec.items():
        print("  %-32s NEC %s  WEC %s  SEC %s (rho+sum p %s)  DEC %s" % (k, v["NEC"], v["WEC"], v["SEC"],
                                                                         v["rho+sum p"], v["DEC"]))
    print("\nSturm's best K s^2 per class (certifies iff >= pi^2 = %.4f):" % math.pi ** 2)
    for k, v in sb.items():
        print("  %-44s %s" % (k, v))
    print("  limits:", lim)
    print("\nz3 grades:")
    for k, v in gr.items():
        print("  %-60s %s" % (k, v))
    print("\nSeat grades per class:")
    for r in grade_rows:
        print("  %s" % r["class"])
        for kk, vv in r.items():
            if kk != "class":
                print("      %-18s %s" % (kk, vv))
    print("\nFigures:")
    for k, v in F.items():
        print("  %-55s %.6g" % (k, v))
    print("\nBoard O-SEAT (docket68/seat.grade_o_seat): %s" % out["board_O_SEAT"])
    print("\nA1 grade table (a1_grades, built from the computations; combine66 reads this):")
    for g in out["grades"]:
        print("  " + g["hypothesis"])
        print("      per_obstruction: " + g["per_obstruction"])
        print("      seat_conditions: " + g["seat_conditions"])
    print("\nTURN (M-RULINGS item 27, M: 'Any crossing'):", out["turn_ruling"])
    print("  the straight string:", out["string_turn (Planck NG bound, b = R_sun)"])
    print("\nWhat wave 1 first said (HISTORY):")
    for h in HISTORY:
        print("  %s: wave 1 first said '%s'; now: %s (%s)" % h)
    if write_json:
        with open(write_json, "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1, default=str)
        print("wrote", write_json)
    return out


def SEAT_GRADES():
    """The per-class grades, derived from the functions above (each entry names the computation it rests on).
    D66-fix: the wall, global-monopole, gauge-monopole and string rows corrected (HISTORY records wave 1's words)."""
    massform = own("massform")
    F = figures()
    gl = gauge_monopole_lens()
    rows = []
    rows.append({
        "class": "string (gauge, straight, static, positive tension)",
        "stress/EC": "NEC, WEC, DEC hold; NEC SATURATED along the axis, SEC SATURATED (rho + sum p = 0, no force), DEC at "
                     "its BOUNDARY (rho = |p_z|) -- energy_conditions",
        "geometry": "cone, deficit 8 pi G mu (string_deficit_linear, H-LINEAR-GRAV); no Newtonian force "
                    "(string_deficit_with_tension); deficit <= %.3g rad at the Planck NG bound"
                    % F["deficit rad at Planck NG bound"],
        "stability": "topological (pi_1) where the vacuum manifold has non-contractible loops; NONE in the Standard "
                     "Model (HK p.36, S^3 simply connected; Z-strings unstable at physical theta_W, HK p.26)",
        "seat: CTC/Borde": "PASSES for the static straight string (static_is_stably_causal); a spinning string with "
                           "dislocation kappa is DISQUALIFIED where S > kappa, inside r < sqrt(S^2 - kappa^2)/alpha "
                           "(r < S/alpha when kappa = 0; spinning_ctc, DLM04 eqs.(2)-(3)); a Gott pair needs "
                           "gamma > %.3g at the Planck bound and cannot be created in an open (2+1)-dimensional "
                           "universe with timelike total momentum (CFG94); no topology change "
                           "(create.is_topology_change(False, False) = False)" % F["Gott gamma needed at Planck NG bound"],
        "seat: Sturm": "NEVER certifies: 0 outside the core; inside, 16 mu (32 mu) needs mu >= pi^2/16 (pi^2/32) "
                       "against the cone closing at mu = 1/4 (H-UNIFORM-CORE)",
        "seat: turn": "a TURN (M ruled TURN = 'Any crossing', M-RULINGS item 27: H-TURN-CROSSING adopted): rays on "
                      "opposite sides cross at L = b/tan(4 pi G mu), linear in b (HK p.90; string_turn); at b = R_sun, "
                      "L = %.4g AU against the Sun's %.4g AU.  Neighbouring rays on one side see a flat cone (J'' = 0), "
                      "so no conjugate point: none under H-TURN-CONJUGATE, the alternative kept on record.  D66-fix "
                      "first said 'a TURN under H-TURN-CROSSING, none under H-TURN-CONJUGATE', the reading M's to rule"
                      % (F["string crossing at b = R_sun, Planck NG bound, AU"], F["Sun focal (spec.focal_length) AU"]),
        "matter not in original form": "SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}: the Yukawa mass "
                                       "vanishes at the core and fermions occur there as massless chiral modes "
                                       "confined to the 1+1 worldsheet, moving at c (HK p.33-34; ETO25 p.22; "
                                       "zero_mode_speed = 1)",
        "specthm class": "S-3 (specthm's own placement; neither S-1's focal formula nor S-2's ball)",
        "H-DEFECT-SEAT": "the phrase has a counterpart under a named reading (zero modes; H-YUKAWA, "
                         "H-FORM-IS-MASS-AND-DIMENSION); a CTC-free S-3 candidate seat (static); Sturm never certifies; "
                         "O-SEAT OPEN (no supply shown); under H-SM-ONLY no stable instance exists, and at an "
                         "electroweak core only the Higgs share (massform: <= %.3f, first order) of the payload's mass "
                         "would change form" % massform.HIGGS_SHARE_LARGEST_READ,
    })
    rows.append({
        "class": "domain wall (thin vacuum wall, VIS, Lambda = 0 both sides)",
        "stress/EC": "NEC, WEC hold (NEC SATURATED along the wall), DEC at its BOUNDARY; SEC VIOLATED "
                     "(rho + sum p = -sigma)",
        "geometry": "repulsive (Tolman Sigma = sigma - 2 tau = -sigma, CGS p.12; R_uu = -4 pi sigma delta) yet "
                    "FOCUSING for null rays that cross it (R_kk = +8 pi sigma delta) -- wall_split; no static planar "
                    "solution (CGS p.2), the VIS wall is a bubble with de Sitter radius 1/beta, beta = 2 pi G "
                    "sigma/c^4 (vis_beta); each side is Minkowski, the wall on R^2 - T^2 = beta^-2 (vis_time_function, "
                    "CGS p.15)",
        "stability": "topological (pi_0) where the vacuum is disconnected; NONE in the Standard Model "
                     "(S^3 connected)",
        "seat: CTC/Borde": "PASSES under H-VIS-MINKOWSKI: Minkowski T is a global time function -- on each side "
                           "g^(mu nu) dT dT = -1, T continuous across the wall, kappa sigma = 4 beta from the Israel "
                           "jump (vis_time_function; CGS p.15, Fig.4 READ); no topology change at a wall seat.  Wave 1 "
                           "first said OPEN (the VIS causal structure not computed)",
        "seat: Sturm": "thin wall: never (K = 0 off the sheet); thick uniform wall: needs beta w >= pi^2/2 = 4.93 -- "
                       "a wall thicker than 4.93 of its own de Sitter radii (sturm_limits); the abstract of "
                       "gr-qc/9903059 reports only de Sitter solutions for 'large' epsilon",
        "seat: turn": "a genuine caustic for normally crossing null rays at f = 1/(4 pi G sigma/c^4) = 1/(2 beta) "
                      "(wall_thin_lens, Raychaudhuri), i.e. at half the wall's de Sitter radius; a 1 AU focus needs "
                      "sigma = %.3g J/m^2" % F["wall sigma J/m^2 for thin-lens focus 1 AU"],
        "matter not in original form": "SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}: Jackiw-Rebbi zero mode "
                                       "cosh(x/w)^(-g v w), normalisable (jackiw_rebbi), massless at the core, a "
                                       "2+1-dimensional fermion (ETO25 p.15)",
        "specthm class": "S-3",
        "H-DEFECT-SEAT": "a counterpart under a named reading (zero modes); a CTC-free S-3 candidate under "
                         "H-VIS-MINKOWSKI; repulsive to matter at rest yet a thin lens for crossing light; no stable "
                         "SM instance",
    })
    rows.append({
        "class": "global monopole",
        "stress/EC": "NEC, WEC, DEC hold; NEC radial and SEC SATURATED (rho + sum p = 0), DEC at its BOUNDARY -- "
                     "hedgehog_stress, hedgehog_curved",
        "geometry": "solid-angle deficit; with the hedgehog's stress taken IN the cone metric (rho = eta^2/(A r^2), "
                    "hedgehog_curved) the exact Einstein tensor (monopole_einstein) gives Delta = 8 pi G eta^2 exactly "
                    "outside the core (Barriola-Vilenkin; monopole_deficit).  Wave 1 first said Delta = 8 pi eta^2/"
                    "(1 + 8 pi eta^2), EXACT -- from the flat-space density, an inconsistent input; no force on slow "
                    "particles (DURRER p.12); total energy grows linearly with R (p.8)",
        "stability": "pi_2; numerically stable static solutions with infinite energy (DURRER p.9 discussion)",
        "seat: CTC/Borde": "PASSES (static_is_stably_causal); no topology change",
        "seat: Sturm": "NEVER: sup K s^2 = 2 eps needs eps >= pi^2/2 = 4.93 against eps < 1 (sturm_limits)",
        "seat: turn": "a TURN under BOTH readings: deflection eps*pi independent of b (monopole_deflection), and every "
                      "recrossing of the source-centre axis is a CONJUGATE point -- the rotation Killing field about "
                      "that axis is a Jacobi field vanishing at the source and on the axis (monopole_conjugate: the "
                      "out-of-plane Jacobi field's first zero lies at the axis crossing to %.1e relative; a curvature "
                      "halved misses it, A = 1 has none).  A line caustic on the axis (an axicon).  Wave 1 first said "
                      "'none under H-TURN-CONJUGATE'" % F["global monopole conjugate point: |s_J/s_axis - 1|"],
        "matter not in original form": "SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION}: a normalisable zero "
                                       "mode exp(-(h/2) INT F) at the core (ETO25 App. A)",
        "specthm class": "S-3 (its lensing is a solid-angle deficit with no Newtonian mass, DURRER p.12: not S-1's "
                         "positive-mass formula)",
        "H-DEFECT-SEAT": "a counterpart under a named reading (zero modes); a CTC-free S-3 candidate whose turn is a "
                         "genuine line caustic; an isolated global monopole carries energy growing with R (DURRER p.8)",
    })
    rows.append({
        "class": "gauge monopole (exterior)",
        "stress/EC": "all four hold; NEC radial SATURATED, DEC at its BOUNDARY; SEC SAT (rho + sum p = 2u > 0): attractive "
                     "(maxwell_radial; gr-qc/9506068 abstract)",
        "geometry": "Reissner-Nordstrom-like magnetic exterior (static)",
        "stability": "pi_2, finite energy; the monopole problem (DURRER p.18); NONE in the Standard Model "
                     "(pi_2(S^3) = 0, DURRER p.4)",
        "seat: CTC/Borde": "PASSES outside r_+ (static_is_stably_causal)",
        "seat: Sturm": "needs Q/b >= pi, i.e. 2 M_out / b >= pi^2 > 1 -- inside its own gravitational radius "
                       "(sturm_limits): never for a regular monopole",
        "seat: turn": "an S-1 point lens: spec.focal_length puts a 1 AU focus at b = %.3g m for M = 1e17 GeV/c^2 "
                      "(r_s = %.2g m, core ~ %.2g m, field energy beyond b %.1e of Mc^2; gauge_monopole_lens, the "
                      "scan 1e15 .. 1e19 GeV holds too); conjugate points on the axis as for the Sun"
                      % (gl["b_m"], gl["r_s_m"], gl["r_core_m"], gl["field_energy_beyond_b_over_Mc2"]),
        "matter not in original form": "SUPPORTED-IF {H-YUKAWA, H-FORM-IS-MASS-AND-DIMENSION} (zero modes on monopoles, "
                                       "ETO25 p.15); baryon-number violation at the core (Rubakov-Callan, as cited by "
                                       "HK p.63), whose READ direction is wash-out (HK eq.(4.33))",
        "specthm class": "S-1 IF {H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM} (gauge_monopole_lens).  Wave 1 first "
                         "said 'S-3 (or S-1 if its lensing seats; not computed)'",
        "H-DEFECT-SEAT": "a counterpart under a named reading (zero modes; B violation at the core); a CTC-free S-1 "
                         "lensing seat under named hypotheses; no stable SM instance (pi_2(S^3) = 0)",
    })
    rows.append({
        "class": "texture",
        "stress/EC": "a canonical sigma-model field: NEC holds identically (canonical_nec); time-dependent",
        "geometry": "a collapse event; slow particles get infall eps*pi (DURRER p.13)",
        "stability": "UNSTABLE: Derrick, dE/dlambda = I1 + 3 I2 > 0 in d = 3 (derrick(3)); textures 'form d = 0 "
                     "events in spacetime' (DURRER Table 1, p.4)",
        "seat: CTC/Borde": "no CTC is introduced (flat-space sigma model, linear gravity); not computed beyond that",
        "seat: Sturm": "not applicable (no persistent place)",
        "seat: turn": "transient Einstein ring (DURRER p.13)",
        "matter not in original form": "no localised zero modes are read for a texture",
        "specthm class": "EMPTY IF {H-SEAT-PERSISTS}: an event is not a place that persists over the arrival",
        "H-DEFECT-SEAT": "not a seat on H-SEAT-PERSISTS; OPEN without it (an event-seat is defined nowhere on the board)",
    })
    return rows


N_DEFB_CLAUSE = ("N_DEFB a supply only IF {CP-violating core couplings, departure from equilibrium}, HK p.65; "
                 "the READ direction otherwise is wash-out, HK eq.(4.33) p.64")


def a1_grades():
    """A1's grade table in the A-report shape (hypothesis, per_obstruction, seat_conditions, ground, named_hypotheses),
    BUILT here from the computations and the z3 screen, so the drift guard of combine66.py reads the instrument and not a
    stored copy (D66-fix: wave 1's A1-defects.json was written by hand beside the instrument)."""
    F = figures()
    gr = grades()
    gl = gauge_monopole_lens()
    hold = gr["O-HOLD, defect as throat support, outside H-CANONICAL"]
    topo = gr["O-MAKE-TOPO, defect-supported throat made from flat space"]
    seat = gr["O-SEAT, defect at the seat"]
    rows = [
        {"hypothesis": "H-DEFECT-SEAT (defect at the seat), string (static, straight, positive tension)",
         "per_obstruction": "O-SEAT %s (the board's grade is not moved; %s); O-HOLD LEAVES; O-LOOP none (static); "
                            "O-MAKE-TOPO LEAVES (no topology change); O-MAKE-DIST LEAVES; O-BITS LEAVES (zero modes move "
                            "at exactly c; the cone shortens paths by %.2g, and only relative to flat space)"
                            % (seat, N_DEFB_CLAUSE, F["cone shortcut 1 - cos(Delta/4) at Planck NG bound"]),
         "seat_conditions": "M-S1A-P3 (i) PASSES (static, g^tt = -1). A spinning string with dislocation kappa is "
                            "DISQUALIFIED where S > kappa, inside r < sqrt(S^2 - kappa^2)/alpha (r < S/alpha when "
                            "kappa = 0). A Gott pair needs gamma > %.2g at the Planck bound and cannot be created in an "
                            "open (2+1)-dimensional universe with timelike total momentum (CFG94). specthm class S-3. "
                            "Sturm never certifies (16 mu or 32 mu, against the cone closing at mu = 1/4). It TURNs (M "
                            "ruled TURN = 'Any crossing', M-RULINGS item 27: H-TURN-CROSSING adopted): rays on opposite "
                            "sides cross at L = b/tan(4 pi G mu) (%.4g AU at b = R_sun), with no conjugate point, so "
                            "none under H-TURN-CONJUGATE, the alternative on record (D66-fix first said 'Its turn is a "
                            "crossing ..., with no conjugate point', the reading M's to rule)"
                            % (F["Gott gamma needed at Planck NG bound"],
                               F["string crossing at b = R_sun, Planck NG bound, AU"]),
         "ground": "defects.py energy_conditions, string_deficit_linear, static_is_stably_causal, spinning_ctc, "
                   "sturm_bounds/limits, string_crossing, grades(); HK pp.53,84,90; DLM04 eqs.(2)-(3); CFG94 eq.(32)",
         "named_hypotheses": ["H-THIN", "H-LINEAR-GRAV", "H-UNIFORM-CORE", "H-STATIC-STRING", "H-YUKAWA",
                              "H-FORM-IS-MASS-AND-DIMENSION", "H-TURN-CONJUGATE", "H-TURN-CROSSING", "H-SM-ONLY",
                              "N_DEFB", "N_S5"]},
        {"hypothesis": "H-DEFECT-SEAT, domain wall (thin vacuum wall, VIS, Lambda = 0 both sides)",
         "per_obstruction": "O-SEAT %s (N_DEFB not READ for walls: OPEN as unchecked); O-HOLD LEAVES; O-LOOP none "
                            "(Minkowski T is a global time function under H-VIS-MINKOWSKI); O-MAKE-TOPO LEAVES; "
                            "O-MAKE-DIST LEAVES; O-BITS LEAVES" % seat,
         "seat_conditions": "M-S1A-P3 (i) PASSES under H-VIS-MINKOWSKI (vis_time_function: each side Minkowski, "
                            "g^(mu nu) dT dT = -1, T continuous at the wall, kappa sigma = 4 beta; CGS p.15, Fig.4 READ). "
                            "The SEC is VIOLATED (repulsive, R_uu = -4 pi G sigma) but the NEC holds and light crossing "
                            "the wall is focused (R_kk = +8 pi G sigma): a genuine caustic at f = c^4/(4 pi G sigma) = "
                            "1/(2 beta). Sturm: a thin wall never certifies; a thick wall needs w >= (pi^2/2)/beta. "
                            "specthm class S-3",
         "ground": "defects.py wall_split, wall_thin_lens, vis_beta, vis_time_function, sturm_limits; CGS pp.2,6,10,12,"
                   "14-15, Fig.4; gr-qc/9903059 abstract",
         "named_hypotheses": ["H-THIN", "H-VIS-MINKOWSKI", "H-YUKAWA", "H-FORM-IS-MASS-AND-DIMENSION", "H-SM-ONLY",
                              "H-TURN-CONJUGATE", "N_DEFB", "N_S5"]},
        {"hypothesis": "H-DEFECT-SEAT, global monopole",
         "per_obstruction": "O-SEAT %s (N_DEFB not READ for global monopoles: OPEN as unchecked); O-HOLD LEAVES; "
                            "O-LOOP none (static); the others LEAVES" % seat,
         "seat_conditions": "PASSES (static). Deficit Delta = 8 pi G eta^2 exactly outside the core (hedgehog_curved, "
                            "monopole_deficit). Sturm never certifies (sup K s^2 = 2 eps needs eps >= pi^2/2, against "
                            "eps < 1). Deflection eps*pi for every b, and every axis recrossing is a conjugate point "
                            "(monopole_conjugate): a TURN under H-TURN-CONJUGATE and H-TURN-CROSSING, a line caustic. "
                            "specthm class S-3",
         "ground": "defects.py hedgehog_stress, hedgehog_curved, monopole_einstein, monopole_deficit, "
                   "monopole_deflection, monopole_conjugate, sturm_bounds; DURRER pp.8-12; ETO25 App. A",
         "named_hypotheses": ["H-YUKAWA", "H-FORM-IS-MASS-AND-DIMENSION", "H-TURN-CONJUGATE", "H-TURN-CROSSING",
                              "N_DEFB", "N_S5"]},
        {"hypothesis": "H-DEFECT-SEAT, gauge monopole (exterior)",
         "per_obstruction": "O-SEAT %s (%s); O-HOLD LEAVES; O-LOOP none outside r_+; the others LEAVES"
                            % (seat, N_DEFB_CLAUSE),
         "seat_conditions": "PASSES outside r_+ (static). All energy conditions hold; SEC SAT (attractive). Sturm needs "
                            "Q/b >= pi, i.e. 2 M_out/b >= pi^2 > 1 (trapped), so never for a regular monopole. Lensing "
                            "seat: specthm class S-1 IF {H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM} -- a 1 AU focus at "
                            "b = %.3g m for M = 1e17 GeV/c^2 by spec.focal_length, b / r_core = %.1e, b / r_s = %.1e, "
                            "field energy beyond b %.1e of Mc^2. None exists in the SM (pi_2(S^3) = 0)"
                            % (gl["b_m"], gl["b_over_core"], gl["b_over_rs"], gl["field_energy_beyond_b_over_Mc2"]),
         "ground": "defects.py maxwell_radial, sturm_bounds/limits, static_is_stably_causal, gauge_monopole_lens "
                   "(spec.focal_length); DURRER pp.4,18; HK pp.63-65; gr-qc/9506068 abstract",
         "named_hypotheses": ["H-YUKAWA", "H-FORM-IS-MASS-AND-DIMENSION", "H-SM-ONLY", "H-MONOPOLE-MASS",
                              "H-WEAK-FIELD", "H-S1-VACUUM", "N_DEFB", "N_S5"]},
        {"hypothesis": "H-DEFECT-SEAT, texture",
         "per_obstruction": "no obstruction moved (a texture is an event, not a place)",
         "seat_conditions": "EMPTY IF {H-SEAT-PERSISTS}. A texture is unstable: Derrick gives dE/dlambda = I1 + 3 I2 > 0 "
                            "in d = 3 and z3 finds no stationary point (the d = 1 control does admit one). Textures are "
                            "d = 0 events in spacetime (DURRER Table 1)",
         "ground": "defects.py derrick, canonical_nec; DURRER pp.4,9,13",
         "named_hypotheses": ["H-SEAT-PERSISTS", "H-CANONICAL"]},
        {"hypothesis": "a defect as the THROAT's support (string-supported wormholes: Visser polyhedral, GV ring, FGM "
                       "quantum)",
         "per_obstruction": "O-HOLD is LEFT given H-CANONICAL: canonical fields satisfy the NEC pointwise, so FSW "
                            "binds. Outside it, %s: the throat needs tension -c^4/(4G), and no mechanism is known "
                            "(Visser p.5). Quantum string fluctuations (FGM) give an opening that is brief and "
                            "exponentially fragile, with transit d + logs; that is not a hold. Never REMOVED. O-LOOP "
                            "reintroduced for mouths in one space with unequal surrounding mass (FKZ: T ~ R L c/(G M)). "
                            "O-MAKE-TOPO %s: a ring wormhole made from flat space is a topology change "
                            "(create.is_topology_change(False, True)) and Geroch/Borde force a pathology, which sits at "
                            "the throat; M's ruling (ledger M-S1A-P3: 'a singular throat is not disqualified', 'the "
                            "throat-creation classes stay OPEN') admits it, specthm W-create-ncc is OPEN at its owner, "
                            "not shown realisable. O-BITS LEAVES" % (hold, topo),
         "seat_conditions": "The seat mouth lies on the FKZ loop, so M-S1A-P3 (i) disqualifies it unless the masses "
                            "balance. The GV ring at the figures' tension (T = -c^4/(4G), sigma = 0) is a singular ring "
                            "bounding the throat disc with only a conical singularity; at sigma != 0 it also carries a "
                            "power-law curvature singularity (GV pp.20-22). Either way it is at the throat, which "
                            "M-S1A-P3 (i) does not disqualify",
         "ground": "defects.py canonical_nec, grades() (z3, vacuity guard, 6 mutation controls), figures (GV %.4e N, "
                   "Visser %.4g J/m, %.3g Jupiter masses); FSW93, GV17, VISSER89, FKZ23, FGM19; ledger M-S1A-P3"
                   % (F["GV ring |T| = c^4/(4G) N"], F["Visser cube edge c^4/(8G) J/m"],
                      F["GV 1 m ring / Jupiter (spec.LENSES)"]),
         "named_hypotheses": ["H-CANONICAL", "N_NEGT", "N_WNCC (specthm W-create-ncc)"]},
    ]
    return rows


# =============================================================================== 8. selftest
def selftest():
    import sympy as sp
    res = []

    def chk(name, ok, detail="", kind="CHECK"):
        res.append((name, bool(ok), kind))
        print("  %s [%s] %s  %s" % ("ok  " if ok else "FAIL", kind, name, detail))

    print("1. Energy conditions")
    e = {k: energy_conditions(v["rho"], v["p"]) for k, v in CLASSES.items()}
    chk("string: NEC SAT, SAT, SATURATED (axis); WEC SAT; SEC SATURATED; DEC BOUNDARY",
        e["string"]["NEC"] == ["SAT", "SAT", "SATURATED"] and e["string"]["WEC"] == "SAT"
        and e["string"]["SEC"] == "SATURATED" and e["string"]["DEC"] == "BOUNDARY", str(e["string"]))
    wmin = wec_grid(CLASSES["string"])
    chk("independent WEC: T_uu over a grid of observers (v up to 0.999, all directions) has minimum rho = 1 for the "
        "string (%.6f)" % wmin, abs(wmin - 1.0) < 1e-9)
    chk("CONTROL: the same grid on the negative-tension string goes negative (%.3g)"
        % wec_grid(NEG_TENSION_STRING), wec_grid(NEG_TENSION_STRING) < 0, "", "CONTROL")
    chk("wall: NEC holds, SEC VIOLATED (rho + sum p = -sigma)", e["wall"]["NEC_min"] != "VIOLATED"
        and e["wall"]["SEC"] == "VIOLATED" and e["wall"]["rho+sum p"] == -1, str(e["wall"]))
    chk("global monopole: NEC radial SATURATED, SEC SATURATED", e["global monopole"]["NEC"][0] == "SATURATED"
        and e["global monopole"]["SEC"] == "SATURATED")
    chk("gauge monopole: SEC SAT (attractive), DEC BOUNDARY", e["gauge monopole"]["SEC"] == "SAT"
        and e["gauge monopole"]["DEC"] == "BOUNDARY")
    en = energy_conditions(NEG_TENSION_STRING["rho"], NEG_TENSION_STRING["p"])
    chk("CONTROL: the negative-tension string (Visser/GV) VIOLATES the NEC and the WEC",
        en["NEC_min"] == "VIOLATED" and en["WEC"] == "VIOLATED", str(en["NEC"]), "CONTROL")
    m, grid = nec_min_over_null(CLASSES["wall"]["rho"], CLASSES["wall"]["p"])
    chk("independent: min over the null cone of T_kk equals the per-axis minimum (wall: 0; grid %.3g)" % grid,
        m == 0 and abs(grid) < 1e-12)
    m2, grid2 = nec_min_over_null(NEG_TENSION_STRING["rho"], NEG_TENSION_STRING["p"])
    chk("CONTROL: null-cone minimum for the negative-tension string is negative", m2 < 0 and grid2 < 0,
        str(m2), "CONTROL")
    hs = hedgehog_stress()
    chk("hedgehog sigma-model stress = (1, -1, 0) eta^2/r^2, the CLASSES row", hs == (1, -1, 0), str(hs))
    chk("CONTROL: the hedgehog row is NOT the string's row", tuple(hs) != (1, 0, 0), "", "CONTROL")
    mx = maxwell_radial()
    chk("radial Maxwell stress = (1; -1, 1, 1) u, the CLASSES row", mx[0] == 1 and mx[1] == (-1, 1, 1), str(mx))

    print("2. The canonical-field NEC theorem")
    Tkk, sos, noV = canonical_nec(+1)
    chk("T_kk (2 scalars + Maxwell, k = (1,0,0,1)) = sum of squares; V drops out", sos and noV, str(Tkk)[:80])
    Tkk_m, sos_m, _ = canonical_nec(-1)
    val = Tkk_m.subs({sym: (1 if str(sym) in ("d0_0",) else 0) for sym in Tkk_m.free_symbols})
    chk("CONTROL: a phantom (negative kinetic sign) scalar gives T_kk < 0 at d0_0 = 1", (not sos_m) and val < 0,
        str(val), "CONTROL")

    print("3. Geometry")
    dfc, dfc1 = string_deficit_linear()
    chk("string deficit from HK eq.(4.3) = 8 pi G mu (first order)", sp.simplify(dfc1 - 8 * sp.pi * sp.Symbol(
        "g", positive=True)) == 0, str(dfc))
    d_c, pot_c, d_g, pot_g = string_deficit_with_tension()
    chk("HK eq.(4.6): T = mu gives deficit 8 pi G mu and zero Newtonian potential", sp.simplify(
        d_c - 8 * sp.pi * sp.Symbol("G", positive=True) * sp.Symbol("mu", positive=True)) == 0 and pot_c == 0)
    chk("CONTROL: T = 0 (a rod) gives 4 pi G mu and a non-zero potential", sp.simplify(
        d_g.subs(sp.Symbol("T", positive=True), 0) - 4 * sp.pi * sp.Symbol("G", positive=True)
        * sp.Symbol("mu", positive=True)) == 0 and pot_g.subs(sp.Symbol("T", positive=True), 0) != 0, "", "CONTROL")
    arc = 8 * math.pi * 1e-6 * 180 / math.pi * 3600
    chk("HK p.85: Delta = 8 pi G mu = 5.18 arcsec at mu6 = 1 (recomputed %.4f)" % arc,
        abs(arc - HK_ARCSEC_PER_MU6) < 0.006)
    chk("CONTROL: 4 pi G mu does NOT reproduce HK's 5.18", abs(arc / 2 - HK_ARCSEC_PER_MU6) > 1, "", "CONTROL")
    spec = own("spec")
    kgm = 1e-6 * spec.C_SI ** 2 / spec.G_SI
    chk("HK p.16: mu = 1.35e21 kg/m at mu6 = 1 (recomputed %.4g with spec.G_SI, spec.C_SI)" % kgm,
        abs(kgm / HK_KG_PER_M_PER_MU6 - 1) < 0.005)
    (Gtt, Grr, Gthth), A, r = monopole_einstein()
    rho = sp.simplify(-Gtt / (8 * sp.pi))
    chk("global monopole metric: p_r = -rho (G^r_r = G^t_t) and p_t = 0 (G^th_th = 0)",
        sp.simplify(Grr - Gtt) == 0 and sp.simplify(Gthth) == 0, "rho = %s" % rho)
    D, eta = sp.symbols("Delta eta", positive=True)
    hr, hp, ht, A2, eta2, r2 = hedgehog_curved()
    chk("D66-fix: the hedgehog's stress IN the cone metric is (rho, p_r, p_t) = (1, -1, 0) eta^2/(A r^2) "
        "(hedgehog_curved), the form the Einstein tensor has",
        sp.simplify(hr - eta2 ** 2 / (A2 * r2 ** 2)) == 0 and sp.simplify(hp + hr) == 0 and ht == 0, str((hr, hp, ht)))
    sol = monopole_deficit(True)
    chk("D66-fix: with the consistent stress, Delta = 8 pi G eta^2 EXACTLY outside the core (Barriola-Vilenkin)",
        len(sol) == 1 and sp.simplify(sol[0] - 8 * sp.pi * eta ** 2) == 0, str(sol))
    sol1 = monopole_deficit(False)
    chk("CONTROL (wave 1's input, the flat-space density eta^2/r^2) gives a DIFFERENT Delta, 8 pi eta^2/(1 + 8 pi "
        "eta^2): the check distinguishes the consistent input from the inconsistent one",
        len(sol1) == 1 and sp.simplify(sol1[0] - 8 * sp.pi * eta ** 2) != 0, str(sol1), "CONTROL")
    chk("CONTROL: A = 1 (no deficit) gives rho = 0", sp.simplify(rho.subs(A, 1)) == 0, "", "CONTROL")
    s_ax, s_j = monopole_conjugate()
    chk("D66-fix: global monopole (A = 0.9, D = 10, b = 1): the out-of-plane Jacobi field's first zero is the axis "
        "recrossing (s_J %.6f vs s_axis %.6f): a CONJUGATE point" % (s_j, s_ax),
        s_j is not None and abs(s_j / s_ax - 1) < 1e-6)
    s_ax2, s_j2 = monopole_conjugate(A=0.999, D=1e3, b=1.0)
    chk("D66-fix: the same at A = 0.999, D = 1e3 (s_J %.4f vs s_axis %.4f)" % (s_j2, s_ax2),
        s_j2 is not None and abs(s_j2 / s_ax2 - 1) < 1e-6)
    chk("CONTROL: with the curvature halved the Jacobi field does not vanish at the axis crossing (none before "
        "1.5 s_axis) -- the coincidence is not built in", monopole_conjugate(k_scale=0.5)[1] is None, "", "CONTROL")
    chk("CONTROL: A = 1 (flat, no monopole): no axis recrossing and no conjugate point",
        monopole_conjugate(A=1.0) == (None, None), "", "CONTROL")
    defl = monopole_deflection()
    chk("DURRER eq.(38): deflection = eps pi, independent of b", sp.simplify(defl - sp.Symbol(
        "epsilon", positive=True) * sp.pi) == 0, str(defl))
    Ruu, Rkn, Rkw, tol = wall_split()
    chk("wall: R_uu = -4 pi sigma delta (defocuses observers), R_kk = +8 pi sigma delta crossing, 0 along",
        sp.simplify(Ruu + 4 * sp.pi) == 0 and sp.simplify(Rkn - 8 * sp.pi) == 0 and Rkw == 0,
        "%s %s %s" % (Ruu, Rkn, Rkw))
    chk("CGS p.12: Tolman mass per area sigma - 2 tau = -sigma", tol == -1, str(tol))
    chk("vis_beta: beta = 2 pi G sigma / c^4 (CGS kappa sigma = 4 beta)", sp.simplify(
        vis_beta() - 2 * sp.pi * sp.Symbol("G", positive=True) * sp.Symbol("sigma", positive=True)
        / sp.Symbol("c", positive=True) ** 4) == 0)
    vt = vis_time_function()
    chk("D66-fix, CGS p.15: each side of the M4-M4 wall is Minkowski (pullback of -dT^2 + dR^2 + R^2 dOmega^2 is the "
        "comoving metric), g^(mu nu) dT dT = -1 on both sides, T continuous at the wall, dT/dt > 0 there: Minkowski T "
        "is a global time function, no closed causal curve (H-VIS-MINKOWSKI)",
        all(vt[s_]["pullback_is_g"] and vt[s_]["gTT"] == -1 for s_ in (1, -1)) and vt["continuous at z=0"])
    chk("D66-fix: the Israel jump of that metric gives S_ij = -sigma h_ij with kappa sigma = 4 beta (CGS p.10)",
        vt["S_ij = -sigma h_ij"] and sp.simplify(vt["kappa sigma"] - 4 * sp.Symbol("beta", positive=True)) == 0,
        str(vt["kappa sigma"]))
    chk("CONTROL: R (the radial coordinate) has g^(mu nu) dR dR = +1: the time-function test can fail",
        vt[1]["gRR"] == 1, "", "CONTROL")
    chk("CONTROL: the conformal factor as printed in CGS (3.48), e^(-beta|z|), is NOT pulled back from Minkowski by "
        "CGS's own transformation (the pullback test can fail; reading note)",
        not vis_time_function(exponent=1)[1]["pullback_is_g"], "", "CONTROL")
    f, th = wall_thin_lens(+1)
    sg = sp.Symbol("sigma", positive=True)
    chk("wall thin lens: caustic at 1/(4 pi sigma) = 1/(2 beta) (G = c = 1)", f is not None and
        sp.simplify(f - 1 / (4 * sp.pi * sg)) == 0, str(f))
    fneg, _ = wall_thin_lens(-1)
    chk("CONTROL: a negative-tension wall defocuses: no caustic ahead", fneg is None, "", "CONTROL")
    dE3, stat3 = derrick(3)
    dE1, stat1 = derrick(1)
    chk("Derrick d = 3: dE/dlambda = I1 + 3 I2 and no static stationary point (DURRER p.9)",
        sp.simplify(dE3 - sp.Symbol("I1", nonnegative=True) - 3 * sp.Symbol("I2", nonnegative=True)) == 0
        and not stat3, str(dE3))
    chk("CONTROL: d = 1 (a kink / wall profile) DOES admit a stationary point", stat1, str(dE1), "CONTROL")

    print("4. The seat tests")
    chk("specthm.py states Sturm as '4 pi G T_kk s^2/c^4 >= pi^2' (read from its source)", specthm_sturm_sentence())
    specthm = own("specthm")
    soc = [spec.seat_over_collapse(l) for l in (1.0, 1.0e5, 1.0e8, 1.0e11)]
    Fmin = {"soc": soc, "soc_const": max(abs(x / soc[0] - 1.0) for x in soc)}
    s3 = [c for c in specthm.classes(Fmin) if c["id"] == "S-3"][0]
    chk("specthm.classes: S-3's note places defect seats there 'until tested'",
        "topological defect" in s3["note"] and "S-3's until tested" in s3["note"])
    chk("specthm.sturm_ratio(2 pi^2/3) at T_kk = u, s = l equals spec's 2 pi^2/3 (owner agreement)",
        abs(specthm.sturm_ratio(soc[0]) - 2 * math.pi ** 2 / 3) < 1e-12, "%.6f" % specthm.sturm_ratio(soc[0]))
    sb = sturm_bounds()
    mu, w = sp.symbols("mu w", positive=True)
    chk("string core Sturm number 16 mu (T_kk = u) and 32 mu (2u)", sp.simplify(
        sb["string core, T_kk = u"] - 16 * mu) == 0 and sp.simplify(sb["string core, T_kk = 2u"] - 32 * mu) == 0)
    chk("global monopole: sup K s^2 = 2 eps", sp.simplify(sb["global monopole (sup over chords)"]
                                                          - 2 * sp.Symbol("eps")) == 0,
        str(sb["global monopole (sup over chords)"]))
    Q, b = sp.symbols("Q b", positive=True)
    chk("gauge monopole: sup K s^2 = Q^2/b^2", sp.simplify(sb["gauge monopole exterior (sup over chords)"]
                                                           - Q ** 2 / b ** 2) == 0)
    lim = sturm_limits()
    chk("every class's Sturm certificate lies past its own gravitational limit: string pi^2/32 > 1/4, monopole "
        "pi^2/2 > 1, gauge monopole 2M/b = pi^2 > 1",
        lim["string core T_kk = 2u: mu needed"] > lim["string: cone closes at mu"]
        and lim["global monopole: eps needed"] > lim["global monopole: eps limit"]
        and lim["gauge monopole: 2 M_out / b at certification"] > 1)
    chk("CONTROL: with the member T_kk = 2u replaced by T_kk = 8u the string core WOULD certify below 1/4 "
        "(pi^2/128 < 1/4) -- the bound is carried by the stress, not by construction",
        sp.pi ** 2 / 128 < sp.Rational(1, 4), "", "CONTROL")
    L1 = string_crossing(PLANCK_NG_GMU, 1.0)
    L2 = string_crossing(PLANCK_NG_GMU, 2.0)
    chk("string crossing is linear in b (no caustic): L(2b) = 2 L(b)", abs(L2 / L1 - 2) < 1e-12, "%.4g m" % L1)
    sun = [x for x in spec.LENSES if x[0] == "Sun"][0]
    # item 27 (R-apply, 2026-10-04): M ruled TURN = 'Any crossing'; the ruling is read from M-RULINGS at run time
    with open(os.path.join(WD, "docket68", "M-RULINGS-2026-10-03.md"), encoding="utf-8") as fh:
        mr = fh.read()
    m27 = re.search(r"^27\. (.*?)(?=^\d+\. |\Z)", mr, re.S | re.M)
    t27 = " ".join(m27.group(1).split()) if m27 else ""
    chk("M-RULINGS item 27 read at run time: M: \"Any crossing\"; H-TURN-CROSSING is adopted; the straight string "
        "TURNs -- and TURN_RULING records it (adopted H-TURN-CROSSING, H-TURN-CONJUGATE the alternative on record)",
        'M: "Any crossing"' in t27 and "H-TURN-CROSSING is adopted" in t27 and "the straight cosmic string TURNs" in t27
        and TURN_RULING["adopted"] == "H-TURN-CROSSING" and TURN_RULING["alternative on record"] == "H-TURN-CONJUGATE"
        and TURN_RULING["M"] == "Any crossing", t27[:90])
    st_ = string_turn(PLANCK_NG_GMU, sun[2])
    chk("item 27: the straight string at the Planck NG bound, b = R_sun, TURNs under the adopted H-TURN-CROSSING: the "
        "rays cross at L = %.4g AU (string_crossing), equal to the two deflected rays' line intersection to 1e-12; no "
        "conjugate point, so NO TURN under H-TURN-CONJUGATE (the alternative on record)" % (st_["crossing L"] / spec.AU),
        st_["verdict under the ruling (H-TURN-CROSSING adopted)"] == "TURN" and
        abs(st_["crossing L (line intersection)"] / st_["crossing L"] - 1) < 1e-12 and
        st_["H-TURN-CONJUGATE"] == ("NO TURN", None) and st_["conjugate point"] is None)
    chk("CONTROL item 27: with G mu = 0 (no string) the rays never cross, so NO TURN under H-TURN-CROSSING -- the TURN "
        "verdict is carried by the deficit, not by the reading", string_turn(0.0, sun[2])["H-TURN-CROSSING"] ==
        ("NO TURN", None), "", "CONTROL")
    sa_, sj_ = monopole_conjugate()
    chk("CONTROL item 27: a class WITH a conjugate point (the global monopole, monopole_conjugate) TURNs under "
        "H-TURN-CONJUGATE too -- turn_under can return TURN for the alternative reading",
        turn_under("H-TURN-CONJUGATE", sa_, sj_) [0] == "TURN" and turn_under("H-TURN-CROSSING", sa_, sj_)[0] == "TURN",
        "", "CONTROL")
    specthm_ = own("specthm")
    import inspect
    lits_S = [set(c["lits"]) for c in specthm_.classes(Fmin) if c["space"] == "S"]
    feat = " ".join(str(v) for v in specthm_.FEATURE_TEXT.values()).lower()
    der = inspect.getsource(specthm_.derive)
    chk("item 27 moves no specthm class verdict: every S class is defined by the literals wl and ball alone (no literal "
        "names a turn, a crossing or a conjugate point), and only S-1 can be NONEMPTY (derive's witness rule); the "
        "string stays in S-3, whose verdict is OPEN with or without a crossing TURN",
        all(l_ <= {"wl", "ball"} for l_ in lits_S) and len(lits_S) == 3 and
        not any(w_ in feat for w_ in ("turn", "crossing", "conjugate")) and
        'K["id"] == "S-1" and verdict == OPEN_V' in der and der.count("NONEMPTY") == 1)
    chk("CONTROL item 27: the class-literal test can fail -- a planted S literal 'turn' is caught",
        not all(l_ <= {"wl", "ball"} for l_ in lits_S + [{"wl", "turn"}]), "", "CONTROL")
    fs1, fs2 = spec.focal_length(sun[1], sun[2]), spec.focal_length(sun[1], 2 * sun[2])
    chk("CONTROL: spec.py's S-1 lens is quadratic in b: f(2b) = 4 f(b)", abs(fs2 / fs1 - 4) < 1e-12, "", "CONTROL")
    g3, r0, r1 = spinning_ctc()
    Ssym, al, ka = sp.symbols("S alpha kappa", positive=True)
    chk("DLM04: spinning string CTC region r < S/alpha", any(sp.simplify(x - Ssym / al) == 0 for x in r0), str(r0))
    chk("DLM04: with dislocation, r < sqrt(S^2 - kappa^2)/alpha", any(sp.simplify(
        x - sp.sqrt(Ssym ** 2 - ka ** 2) / al) == 0 for x in r1), str(r1))
    chk("CONTROL: S = 0 -> g_theta_theta > 0 everywhere (no CTC)", sp.simplify(g3.subs({Ssym: 0, ka: 0})) ==
        al ** 2 * sp.Symbol("r", positive=True) ** 2, str(g3), "CONTROL")
    sc = static_is_stably_causal()
    chk("static string cone, global monopole: g^tt = -1 (t a time function)",
        sc["string cone"] == -1 and sc["global monopole"] == -1, str(sc))
    Ms, Qs, rs = sp.symbols("M Q r", positive=True)
    chk("RN exterior: g^tt = -1/N^2 < 0 at r = 3M, Q = M/2", sc["RN exterior"].subs({rs: 3, Ms: 1, Qs: sp.Rational(1, 2)}) < 0)
    gam = gott_gamma_needed(PLANCK_NG_GMU)
    gl = gauge_monopole_lens()
    chk("D66-fix: gauge monopole 1e17 GeV, spec.focal_length: a 1 AU focus at b = %.3g m (V66-1: 2.81e-13), r_s = "
        "%.2g m, b / r_core = %.1e, field energy beyond b %.1e of Mc^2: S-1's conditions hold"
        % (gl["b_m"], gl["r_s_m"], gl["b_over_core"], gl["field_energy_beyond_b_over_Mc2"]),
        abs(gl["b_m"] / 2.81e-13 - 1) < 0.01 and abs(gl["focal_check"] - 1) < 1e-12 and gl["S-1 conditions hold"])
    chk("D66-fix: the scan 1e15 .. 1e19 GeV keeps S-1's conditions (H-MONOPOLE-MASS is not knife-edge)",
        all(gauge_monopole_lens(m)["S-1 conditions hold"] for m in (1e15, 1e16, 1e18, 1e19)))
    chk("CONTROL: a 'monopole' of 1e-27 kg would need b inside its own core, and its field beyond b would exceed its "
        "mass: the S-1 placement test can fail", not gauge_monopole_lens(1e-27 * spec.C_SI ** 2 / (1e9 * E_CHARGE_SI))[
            "S-1 conditions hold"], "", "CONTROL")
    chk("CFG94 eq.(32): Gott pair at the Planck NG bound needs gamma > 1/sin(4 pi G mu) = %.4g" % gam,
        gam > 5e5 and abs(gam * math.sin(4 * math.pi * PLANCK_NG_GMU) - 1) < 1e-12)
    create = own("create")
    chk("create.py: a defect seat changes no spatial topology (is_topology_change(False, False) is False); a "
        "string-ring wormhole made from flat space does (False -> True)",
        create.is_topology_change(False, False) is False and create.is_topology_change(False, True) is True)
    chk("create.py: Geroch needs no matter assumption (GEROCH_NEEDS_MATTER_ASSUMPTION False), so a made ring "
        "wormhole meets Geroch/Borde whatever its string", create.GEROCH_NEEDS_MATTER_ASSUMPTION is False)

    print("5. Matter not in its original form")
    psi, norm, ends, m0 = jackiw_rebbi(+1)
    chk("Jackiw-Rebbi zero mode cosh(x)^-1 normalisable (INT psi^2 = %s), mass 0 at the core" % norm,
        norm is not None and norm.is_finite and norm > 0 and m0 == 0, str(psi))
    psi_c, norm_c, ends_c, _ = jackiw_rebbi(-1)
    chk("CONTROL: the opposite Yukawa sign is NOT normalisable (psi -> %s at the ends)" % (ends_c,),
        norm_c is None and ends_c == (sp.oo, sp.oo), str(psi_c), "CONTROL")
    chk("ETO25 eq.(3.57): zero-mode group velocity = 1 (c), not faster", zero_mode_speed() == 1)
    massform = own("massform")
    share = massform.HIGGS_SHARE_LARGEST_READ
    chk("massform: the largest READ first-order Higgs share of the payload is < 1/2 (%.4f), so at an electroweak "
        "core most of the payload's mass would stay in its original (QCD) form" % share, 0 < share < 0.5)
    chk("massform: S13's static source hold is stable only on %s; a topological core reaches |phi| = 0, below it"
        % massform.STABLE_RANGE, massform.STABLE_RANGE.startswith("0.5774 v") and massform.HELD_SEAT_ROUTE_PRICED)
    excite = own("excite")
    chk("excite.stability_edge = 1 - 1/sqrt(3) (the 0.5774 v edge), computed by its owner",
        abs(excite.stability_edge() - (1 - 1 / math.sqrt(3))) < 1e-12, "%.6f" % excite.stability_edge())
    chk("massform: a seat prepared in advance needs a prior arrival at <= c (D23, asked of the ledger) -- a defect "
        "made at the seat is such a preparation", massform.preparation_needs_prior_arrival() is True)

    print("6. The z3 bookkeeping")
    g = grades()
    chk("vacuity: the board and canonical-without-throat are SAT", g["vacuity: board SAT"]
        and g["vacuity: canonical + no throat SAT"])
    chk("O-HOLD with a canonical defect throat: LEFT", g["O-HOLD, defect as throat support, given H-CANONICAL"]
        == "LEFT")
    chk("O-HOLD outside H-CANONICAL: OPEN via N_NEGT (not REMOVED)",
        g["O-HOLD, defect as throat support, outside H-CANONICAL"] == "OPEN via N_NEGT")
    chk("O-SEAT with a defect at the seat: OPEN via N_S5 | N_DEFB", g["O-SEAT, defect at the seat"]
        == "OPEN via N_S5 | N_DEFB")
    chk("seat condition: static PASSES; inside a spinning string's CTC radius DISQUALIFIED",
        g["seat condition, static straight string / monopole"] == "PASSES (CTC-free)"
        and g["seat condition, inside a spinning string's CTC radius"] == "DISQUALIFIED (M-S1A-P3 (i))")
    gm = grades("drop-FSW")
    chk("CONTROL mutation drop-FSW: a canonical throat is no longer LEFT",
        gm["O-HOLD, defect as throat support, given H-CANONICAL"] != "LEFT", "", "CONTROL")
    gm = grades("neg-asserted")
    chk("CONTROL mutation neg-asserted: the hold becomes removable with no pathway (caught)",
        gm["O-HOLD, defect as throat support, outside H-CANONICAL"] != "OPEN via N_NEGT", "", "CONTROL")
    gm = grades("defb-asserted")
    chk("CONTROL mutation defb-asserted: O-SEAT removable with no pathway (caught)",
        gm["O-SEAT, defect at the seat"] != "OPEN via N_S5 | N_DEFB", "", "CONTROL")
    gm = grades("spin-ok")
    chk("CONTROL mutation spin-ok: the spinning string's CTC is no longer disqualifying (caught)",
        gm["seat condition, inside a spinning string's CTC radius"] != "DISQUALIFIED (M-S1A-P3 (i))", "", "CONTROL")
    chk("D66-fix: O-MAKE-TOPO for a string-supported throat made from flat space: OPEN via N_WNCC (M-S1A-P3 "
        "applied: the pathology sits at the throat)",
        g["O-MAKE-TOPO, defect-supported throat made from flat space"] == "OPEN via N_WNCC")
    gm = grades("ruling-dropped")
    chk("CONTROL mutation ruling-dropped (a pathology at the throat disqualifies): O-MAKE-TOPO reads LEFT (caught)",
        gm["O-MAKE-TOPO, defect-supported throat made from flat space"] == "LEFT", "", "CONTROL")
    gm = grades("wncc-asserted")
    chk("CONTROL mutation wncc-asserted: the made throat removable with no pathway (caught)",
        gm["O-MAKE-TOPO, defect-supported throat made from flat space"] != "OPEN via N_WNCC", "", "CONTROL")
    m_row = [r_ for r_ in own("ledger").RULED_BY_M if r_[0] == "M-S1A-P3"][0]
    m_txt = " ".join(str(x) for x in m_row)
    chk("ledger M-S1A-P3 carries the ruling this encoding applies: 'a singular throat is not disqualified' and 'the "
        "throat-creation classes stay OPEN' (read at run time)",
        "a singular throat is not" in m_txt and "disqualified" in m_txt and "the throat-creation classes stay OPEN" in m_txt)
    a1 = a1_grades()
    chk("a1_grades: six rows, each with per_obstruction and seat_conditions; the throat row carries the run-time z3 "
        "verdicts (OPEN via N_NEGT, OPEN via N_WNCC)", len(a1) == 6 and all(x["per_obstruction"] and x["seat_conditions"]
                                                                             for x in a1)
        and "OPEN via N_NEGT" in a1[5]["per_obstruction"] and "O-MAKE-TOPO OPEN via N_WNCC" in a1[5]["per_obstruction"])
    seat = own("seat")
    chk("docket68/seat.grade_o_seat(board_state()) is OPEN, the board's grade this file adds to and does not move",
        seat.grade_o_seat(seat.board_state()) == "OPEN")
    chk("OPEN pathways are free atoms in the screen, so 'OPEN via' is their encoding", True,
        "printed, not counted", "STRUCTURAL")

    print("7. READ figures recomputed (wormhole literature)")
    c, G = spec.C_SI, spec.G_SI
    chk("GV17 p.22: |T| = c^4/(4G) = 3.0257e43 N (recomputed %.5g)" % (c ** 4 / (4 * G)),
        abs(c ** 4 / (4 * G) / abs(GV_RING_TENSION_N) - 1) < 2e-4)
    jup = [x for x in spec.LENSES if x[0] == "Jupiter"][0]
    ratio = 2 * math.pi * c ** 2 / (4 * G) / jup[1]
    chk("GV17 p.22: a 1 m ring's 2 pi R |T|/c^2 is 'the mass of Jupiter' (ratio to spec's Jupiter %.3f)" % ratio,
        0.5 < ratio < 2)
    chk("VISSER89 p.5: cube edge |rho| = c^4/(8G) = 1.52e43 J/m (recomputed %.4g)" % (c ** 4 / (8 * G)),
        abs(c ** 4 / (8 * G) / abs(VISSER_EDGE_J_PER_M) - 1) < 0.005)
    chk("CONTROL: c^4/(4 pi G) does NOT reproduce Visser's edge", abs(c ** 4 / (4 * math.pi * G)
                                                                      / abs(VISSER_EDGE_J_PER_M) - 1) > 0.1,
        "", "CONTROL")
    chk("ledger.py RULED_BY_M M-S1A-P3 carries M's sentence verbatim", any(
        r[0] == "M-S1A-P3" and "Seating occurs in a place where matter can occur but not in its original geometric "
        "form" in " ".join(str(x) for x in r) for r in own("ledger").RULED_BY_M))

    counted = [x for x in res if x[2] != "STRUCTURAL"]
    ctrl = [x for x in res if x[2] == "CONTROL"]
    struct = [x for x in res if x[2] == "STRUCTURAL"]
    bad = [x for x in counted if not x[1]]
    print("\n%d counted checks (%d controls), %d passed; %d STRUCTURAL printed, not counted"
          % (len(counted), len(ctrl), len(counted) - len(bad), len(struct)))
    for x in bad:
        print("  FAILED:", x[0])
    return not bad, len(counted), len(ctrl), len(struct)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        ok, n, nc, ns = selftest()
        sys.exit(0 if ok else 1)
    jp = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
    report(jp)
