#!/usr/bin/env python3
"""settle.py -- DOCKET 68, work item A1-settle.  H-SETTLE (deterministic drift) alone, H-12's carriers as
drifting parameters, and the stochastic (collapse-type) control.  Not seated.  Write-up: A1-settle.md.

M's definition (CHARTER.md): quantum easing / quantum settling is DETERMINISTIC DRIFT -- "the state's own value
steers its evolution, smoothly and the same every time".  Carried as a hypothesis, never as a result.

WHAT THIS FILE COMPUTES (every number below is computed here, or READ at the locator given):
  A. The signal Bob receives under nlcontrol.py's drift H = eps <X> Z (imported, never copied), versus eps and T.
     EXACT LAW, derived here and checked against nlcontrol's own integrator: for Alice's x-basis ensemble Bob's
     <sigma_y> = tanh(2 eps T); for her z-basis ensemble it is 0.  General closed form for any Bloch vector:
       y(T) = rho_perp * tanh(atanh(y0/rho_perp) + 2 eps rho_perp T),  x keeps its sign,  z constant.
  B. What that signal is worth: bits per pair (mutual information, channel capacity, Holevo chi), the rate per
     pair-second, and the pairs needed per teleported qubit (two classical bits, transit.py).
  C. The published bounds, by FAMILY:
       KR family (Kaplan-Rajendran causal nonlinearity, 2106.10576v2): |eps_gamma| < 1.15e-12 (2411.09611v1),
         4.7e-11 (2204.11875v1), 5.4e-12 (2206.12976v1) -- all READ.  KR's evolution of separated systems
         factorises (2106.10576v2 sec. 2.3, pp.7-8): Bob's statistics move only through retarded Green's functions.
         => the largest SUPERLUMINAL signal this family permits at Bob is 0 for every eps.  O-BITS untouched.
       Weinberg family (deterministic, local on pure states -- the family Gisin's theorem covers and nlcontrol's
         drift belongs to): Majumder et al. 1990 (201Hg) ||eps||/2 pi hbar < 3.8 uHz (= 2.0e-27 B/A), Walsworth et
         al. 1990 (H maser) 3.7e-20 eV (8.9 uHz), Bollinger et al. 1989 (9Be+) 4e-27 B/A, Chupp & Hoare 1990 (21Ne)
         1.6e-26 B/A.  D68 WAVE 2 (W2A-limits): all four READ (abstract) via Firecrawl scrapes of the publisher's
         public abstract pages; Bollinger's and Chupp-Hoare's frequencies (6.25, 30.8 uHz) DERIVED-FROM-READ under
         H-BEFRAC, checked on Majumder's own pair.  Waves 1-4 said: 'NAMED-NOT-READ: PRLs not on arXiv; the figures
         are from abstract metadata seen through a search index (pmid 10042736, 10041761) ... Bollinger 1989 (9Be+)
         and Chupp-Hoare 1990 (21Ne): value OPEN'.  Every number derived from them is CONDITIONAL on H-MAP etc.
  D. The collapse-model control: a stochastic norm-preserving nonlinear equation (QMUPL form, 1204.4325v3
     eq. 23, READ) whose ensemble obeys the LINEAR Lindblad equation (1204.4325v3 p.89, READ) -- must NOT signal,
     while each trajectory changes nonlinearly (vacuity guard).  Must-signal controls: deterministic drift, and
     deterministic drift WITH collapse noise (noise does not launder a deterministic nonlinearity).
  E. H-12: which of V = [M, R, K, T, CP, alpha_s, Z0, Lambda, G, G_F, G_theta, v] could carry a state-dependent
     drift at all, and the measured bound on each one's variation where a READ source has it.
  F. H-SETTLE x H-FRAME: corridors.py imported -- signals keyed to ONE frame close no causal curve.

NAMED HYPOTHESES (every limitation is one):
  H-MAP      the bounded state-dependent precession shift is nlcontrol's 2 eps (full swing of <X>); reading A
             eps = 2 pi f, reading B eps = pi f.  Both reported; neither favoured.
  H-TRANSFER a bound measured on a nuclear/atomic spin applies to Bob's carrier.
  H-SPIN     Weinberg's experiments used spins > 1/2; whether a qubit can carry Weinberg's nonlinearity is OPEN
             here (nlcontrol's eps<X>Z is not rotation-invariant; it is a torsion-class term, cf. 2112.09005v3
             eq. 99 and p.23 "frequency 2 J1 x", READ).
  H-FRAME3b  Gisin's protocol needs the remote preparation on a fixed spacelike hypersurface (2412.20854v1 p.6,
             assumption (3b), READ) -- a preferred slicing.  WAVE 3 (RV-0 #2): a preferred slicing IS M's 'a preferred
             frame exists' (H-FRAME clause 1, F1), so H-FRAME3b PRESUPPOSES F1 (or clause 2b's cosmic clock): the O-BITS
             removal is W2 x F1's, not H-SETTLE-W's alone.  Corroborated: 2511.15935v1 p.1-3 (READ wave 3) -- a
             Weinberg-type term keeps foliation independence only under microcausality, which "cannot be consistently
             maintained" under state-dependent evolution (p.2).  Wave 2 first said 'H-SETTLE alone removes O-BITS ...
             with a preferred slicing built in'.
  H-COHERE   Bob holds coherence for the drift time T.
  H-DILUTION KR p.13 (READ): nonlinear effects can be diluted by cosmic history (eps -> eps/N).
  H-SIG-COR  a signal keyed to a frame is modelled as latticectc's identification (corridors.py's model choice).
  H-C2       (= frame.py's H-DCTC-CONVENTION C2) the drift acts on Bob's per-BRANCH pure state.  M's definition
             ("the state's own value steers its evolution") does not say which state.  Under C1 (the drift acts on
             Bob's REDUCED state) there is NO signal: frame.settle_under_C1 gives 2.2e-16.  2412.20854v1 p.4, p.7
             (READ): Gisin's theorem covers local maps on PURE states only; maps defined on mixed states can be
             nonlinear and non-signalling (their refs [40, 41]).  Every signal below is conditional on H-C2.
  H-BORN-AT-BOB  Bob's final readout is a Born-rule measurement of his drifted system, so Holevo's bound (a theorem
             of linear QM, READ in A3: quant-ph/9611023v1 pp.2-3) applies to that last step only: chi <= log2 of the
             drifted system's dimension.  Wave 2 first said 'of his drifted qubit', which silently added H-QUBIT-DRIFT.
  H-QUBIT-DRIFT  (wave 3, RV-1 #0) the drift acts on Bob's received qubit and nothing else.  Only under it is the
             readout ceiling 1 bit per pair (the 'qubit-only subclass').  Without it (an Alice-independent ancilla
             beside the qubit) w2_ancilla_flow computes a member at 2 bits per pair, zero error, finite T.
  H-EXTEND   (wave 3) the field computed on w2_ancilla_flow's disjoint curves extends to a smooth field on the whole
             state space (DERIVED from their separation by a bump-function extension; not computed).
  H-BLOCK    (wave 3, RV-0 #0) reliable transfer of the 2 bits is block-coded over many teleported qubits at a rate
             below capacity, error -> 0 only as block length -> infinity.  N x C >= 2 (Shannon's converse) is
             necessary, not sufficient: every pair count from it is a FLOOR; where the zero-error capacity is 0
             (zero_error_table) no finite per-qubit N delivers the bits with certainty.
  H-C2 rule  (wave 3, RV-0 #11) part of H-C2: before Alice's measurement in the chosen slicing there is no branch, so
             the drift acts on Bob's reduced state; frame.drift_ordering's 'Bob first gives 0' is this rule's output.
  H-NLCONTROL-FORM  the drift is nlcontrol's single Hamiltonian eps <X> Z.  CMAX = log2(1.25), 6.21 pairs per
             teleported qubit and 'N >= 7' are properties of THIS Hamiltonian, not of the W2 class.
  H-12-CARRIER / H-12-W  (wave 2) Bob's carrier is one of the twelve with no state-dependent bound of any kind
             (alpha_s, G, v), and that carrier drifts in Weinberg (per-branch, non-causal) form rather than KR form.
             No READ source gives a model of either; both are named so the case can be computed.
  H-BEFRAC   (D68 wave 2) a limit printed as a fraction of the binding energy per nucleon is the frequency
             frac x (B/A)/h, with B/A from AME2020 (gravity.nuclides, imported).  CHECKED on Majumder's pair (G31: 3.819
             vs 3.8 uHz) -- which confirms the NORMALISATION (B/A, not B or m_u c^2: control G32), not the nuclide (B/A
             is flat to ~1% for A ~ 20-200, so 21Ne's would also pass); the papers' own B/A tables (1989-90) are not read -- an AME2020-vs-then difference is assumed
             negligible against the one or two printed digits.
  H-SAME-EPS (D68 wave 2) the four experiments bound one common parameter, so the tightest applies to every carrier.
             Without it each bound covers its own system; it moves exactly one window (G36).
  H-ERRATUM  (D68 wave 2) Chupp & Hoare's Erratum (PRL 66, 120, 1991; public page has no abstract) does not change
             the 1.6e-26 figure.  NAMED-NOT-READ; the figure is not the tightest, so no window rests on it alone except
             under not-H-SAME-EPS at 1 AU, N = 1e3, reading A.
  The bound is an UPPER LIMIT measured consistent with ZERO: "not excluded" is never "found".

WAVE 2 (repair after three adversarial verifications, 2026-10-03).  Wave 1 first said: '>= 6.21 pairs per teleported
qubit for this protocol; Holevo caps any qubit protocol at 1 bit per pair (NAMED-NOT-READ)', 'Bob holds each pair for
T = L/2c', and D6 'CONTROL (must signal): pure deterministic drift' fed a hand-typed vector to the detector.  Now:
  * capacity_two_axis / W2_CLASS_CEILING: a second W2 Hamiltonian, eps(<X>Z + <Z>X), reaches 1 bit per pair as
    D -> 1; under H-BORN-AT-BOB no per-branch drift on a qubit exceeds 1 bit per pair (Holevo at the readout), and
    at finite T none reaches it (a flow is injective, so each choice's mixture has rank 2).  So the W2 class needs
    > 2 pairs per teleported qubit (>= 3 per qubit at finite T); 6.21 is nlcontrol's.  Without H-BORN-AT-BOB the
    class capacity is OPEN (the D-CTC analogue breaks Holevo: BHW 0811.1209v2 p.4, READ; frame.bb84_c2_table).
  * drift_time_needed: T = atanh(D_N)/(2 eps) does not depend on distance.  eps_any_advantage: the eps above which
    the read precedes light is exactly half the T = L/2c figure (frac = 0.5 was a DECLARED choice, kept only so
    wave-1 numbers can be compared).
  * first_transit_times: one-end distribution and the midpoint source (LEDGER D23 as corrected in DOCKET 67).
  * window_given (M-apply, 2026-10-03; V3 residual 3): M's rule applied both ways.  An EMPTY window from the unread
    Majumder value makes the cell OPEN (N_WREAD, wave 4); an OPEN window from the same value is ADMISSIBLE GIVEN W_W2,
    flagged and not settled, naming the unread bound and the two OPEN ones (Bollinger 1989, Chupp-Hoare 1990, never
    checked).  The tightening that would close each open window is printed as CONTEXT, not evidence: 655x (A) / 328x
    (B) at 1 ly, N = 7; 7.2x / 3.6x at 1 AU, N = 1e6.  Support 2 has no window (UNEVALUATED).  No verdict moves.
  * h12_carrier_case: H-SETTLE x H-12 adds nothing under H-TRANSFER; with an unbounded carrier (H-12-CARRIER,
    H-12-W) N_EPS is not excluded at 1 AU either -- computed, and 'not excluded' is still not evidence.
  * D6 now runs the drift through sde_ensemble with lambda = 0 and must reproduce tanh(2 eps T).
  * Checks that cannot fail by construction are printed STRUCTURAL and are not counted as evidence.

WAVE 3 (repair after the two re-verifications RV-0 AGAINST M, RV-1 FOR M; 2026-10-03):
  * pair counts from N x C >= 2 are FLOORS; zero_error_table shows the zero-error capacity is 0 for D < 1 (and for
    nlcontrol's Z-channel at every D); H-BLOCK named.  Wave 2 first said '7 if each qubit is coded alone'.
  * H-QUBIT-DRIFT named; w2_ancilla_flow: without it, a W2 member carries 2 bits per pair with zero error at finite
    T (1 pair per teleported qubit), so the qubit-only floor (> 2, >= 3) is that subclass's.  Not evidence of a drift.
  * H-FRAME3b presupposes F1: H-SETTLE-W alone LEAVES O-BITS; the removal is W2 x F1's.
  * O-LOOP for corridors is the geometry's (H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL), credited to no
    hypothesis; wave 2 first credited it to H-SETTLE-W alone.
  * G6a, G7, G8 and G12b are printed STRUCTURAL (identities); G6b and G12a keep the content-bearing halves.

WAVE 4 (R3-alone, repair after the second pair of re-verifications V2-0 AGAINST M, V2-1 FOR M; 2026-10-03):
  * w2_ancilla_flow_k (G21-G25): the same construction with k axes and an m-qubit ancilla reaches chi = log2 k =
    log2 d - 1 bits per pair with zero error -- k = 4, 8, 16, 32 give 1, 2/3, 1/2, 0.4 pairs per teleported qubit.
    So the class has NO positive floor on pairs per qubit in the computed range; "1 pair per teleported qubit" is
    the four-axis instance's figure, not the class's.  The curves' separation shrinks with k (0.39, 0.34, 0.18,
    0.12 rad), so H-EXTEND asks for a field varying on ever finer scales while max ||H|| T stays ~1.4-1.6.
    Controls: antipodal axes collide (chi 2, not 3, at k = 8); a state-independent unitary gives 0.  Not evidence
    that any such drift exists.
  * The summary line now prints the count with STRUCTURAL checks excluded.

D68 WAVE 2 (W2A-limits, 2026-10-04; M's order "1 then 2 then 3 then 4", step 2): the Weinberg-family limits READ at
source (publisher's public abstract pages, Firecrawl; abstract only) -- BOUNDS_WEINBERG; the wave-4 dict is kept as
BOUNDS_WEINBERG_WAVE4 and window_given() still defaults to it (history; combine.py's wave-5 grounds import it).
window_read(): the W2 x F1 window at 1 AU, 1 ly, 4.2465 ly x N = 7, 1e3, 1e6 on the READ values, given W_W2R =
{H-MAP, H-TRANSFER, H-SPIN, H-DILUTION}: 14 of 18 (cell, reading) windows OPEN, 4 EMPTY (1 AU, N = 7 and 1e3, both
readings); one window (1 AU, N = 1e3, A) depends on H-SAME-EPS.  Checks G31-G39.

W2-FIX (2026-10-04, the two re-verifications W2V-0 / W2V-1 of wave2/WAVE2-RESULT.json, key result.verify): the Proxima
cell's distance is IMPORTED from phase1.L_PROXIMA (Gaia DR3, READ via restatement, DOCKET 67), never typed; Faria 2022
Table 1 p.2's READ 768.50 +- 0.20 mas (4.2439 ly) is recorded beside it with the discrepancy computed
(proxima_distances: 0.056 %, 2.17 sigma on Faria's error alone; no window moves).  Checks G40-G42.  Wave 2 first said
"4.2465 ly is the figure the task gives (Proxima Centauri's distance is NAMED-NOT-READ here)".  H-MAP's wording: the
full texts (login wall, not read) MAY carry each paper's eps convention -- what they contain is not known here.

Run:  python3 settle.py            (report)
      python3 settle.py --selftest (fixtures computed or READ; controls that must fail do)
      python3 settle.py --json PATH
"""
import contextlib
import io
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))
with contextlib.redirect_stdout(io.StringIO()):      # the pre-docket scripts print at import; keep the report clean
    import nlcontrol as NL                           # H = eps <X> Z, its integrator and ensembles
    import corridors as CO                           # latticectc's THEOREM applied to corridors
    import gravity as GR                             # AME2020 Table I capture (nuclides), for B/A (wave 2, W2A)

X, Y, Z = NL.X, NL.Y, NL.Z
LN2 = math.log(2.0)

# ----------------------------------------------------------------------------------------------- constants
# SI-2019 exact h, e, c; alpha CODATA 2018 -- all via scipy.constants (the restatement D67 recorded as READ).
try:
    import scipy.constants as SC
    H_PLANCK, E_CHARGE, C_LIGHT, ALPHA = SC.h, SC.e, SC.c, SC.fine_structure
    Z0_SCIPY = SC.physical_constants["characteristic impedance of vacuum"][0]
    AU_M, LY_M, YEAR_S = SC.au, SC.light_year, SC.Julian_year
except Exception:                                    # pragma: no cover -- the values themselves, same source
    H_PLANCK, E_CHARGE, C_LIGHT, ALPHA = 6.62607015e-34, 1.602176634e-19, 299792458.0, 7.2973525643e-3
    Z0_SCIPY, AU_M, LY_M, YEAR_S = 376.730313412, 1.495978707e11, 9.4607304725808e15, 365.25 * 86400

# ----------------------------------------------------------------------------------------------- fixtures
# nlcontrol.py's own printed numbers (CHARTER.md line 288, pre-docket, computed): Bob's <sigma_y>, Alice x, T = 3.
NLCONTROL_PRINTED = {1e-3: 0.00600, 1e-2: 0.05993, 1e-1: 0.53706}

BOUNDS_KR = {   # dimensionless eps_gamma, causal (KR) family -- all READ
    "Melnychuk+ 2024 (cryogenic RF)": (1.15e-12, "2411.09611v1 p.1 abstract, p.7 'new bound on |eps| set at <~1.15e-12 at 90.0% CL'"),
    "Brož+ 2022 (trapped-ion Ramsey)": (5.4e-12, "2206.12976v1 p.1 abstract, p.5 '5 +- 5.4e-12' (1 s.d.)"),
    "Polkovnikov+ 2022 (Everett phone, voltage)": (4.7e-11, "2204.11875v1 p.1, p.3 '|eps_gamma| < 4.7e-11, 90% CL'"),
    "KR 2022 ion-trap estimate (eps>0 only)": (1e-5, "2106.10576v2 p.14"),
    "KR 2022 Lamb-shift estimate (as printed in KR v2)": (1e-4, "2106.10576v2 p.14 '|eps_gamma| <~ 1e-4'"),
    "KR Lamb-shift estimate (as restated by Brož)": (1e-2, "2206.12976v1 p.2 'modest bound of |gamma| <~ 1e-2'; p.5"),
}
# HISTORY (waves 1-4, kept verbatim as the record; window_given() still defaults to it so combine.py's wave-5 grounds
# stay comparable).  Waves 1-4 said: NAMED-NOT-READ (Majumder, Walsworth), OPEN (Bollinger, Chupp-Hoare).
BOUNDS_WEINBERG_WAVE4 = {  # state-dependent precession frequency f (Hz) -- NAMED-NOT-READ, abstract metadata only
    "Majumder+ 1990, 201Hg, PRL 65 2931": {"f_Hz": 3.8e-6, "status": "NAMED-NOT-READ (abstract metadata, pmid 10042736; '|eps|/2pi <= 3.8 uHz')"},
    "Walsworth+ 1990, H maser, PRL 64 2599": {"f_Hz": 8.9e-6, "eV": 3.7e-20,
                                              "status": "NAMED-NOT-READ (abstract metadata, pmid 10041761; '3.7x10^{20} eV (8.9 uHz)' -- exponent sign lost in the text layer)"},
    "Bollinger+ 1989, 9Be+, PRL 63 1031": {"f_Hz": None, "status": "OPEN (abstract truncated before the value; not on arXiv; no READ restatement with the number)"},
    "Chupp & Hoare 1990, 21Ne, PRL 64 2261": {"f_Hz": None, "status": "OPEN (abstract carries no value; not on arXiv)"},
}

# D68 WAVE 2 (W2A-limits, 2026-10-04; M rulings items 15-16): the four Weinberg-family limits READ at source, each from
# the publisher's PUBLIC abstract page (journals.aps.org/prl/abstract/<doi>) via a Firecrawl scrape -- abstract only, no
# full text (paywalled; not circumvented), so every entry is READ (abstract).  Short phrases only, as printed.
#   'frac_BA' = the abstract's limit as a fraction of the binding energy per nucleon (B/A) of the named nuclide;
#   'f_Hz'    = the limit as a state-dependent precession frequency ||eps||/2 pi hbar.  Where the abstract prints only
#               frac_BA, f_Hz is DERIVED-FROM-READ under H-BEFRAC (f = frac_BA x B/A / h with B/A from the AME2020
#               capture, gravity.nuclides(), imported) -- a conversion CHECKED on Majumder's own pair (G31, control G32).
_APS = "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett."
WEINBERG_ROUTE = "READ (abstract) via Firecrawl scrape of the publisher's public abstract page"
BOUNDS_WEINBERG = {
    "Majumder+ 1990, 201Hg, PRL 65 2931": {
        "f_Hz": 3.8e-6, "frac_BA": 2.0e-27, "nuclide": (80, 201), "url": _APS + "65.2931",
        "printed": "'||eps||/2 pi hbar < 3.8 uHz, which corresponds to 2.0 x 10^-27 of the binding energy per nucleon'",
        "f_status": "READ (abstract): printed in Hz",
        "status": WEINBERG_ROUTE + " (" + _APS + "65.2931); re-confirmed this pass, as M item 16 recorded"},
    "Walsworth+ 1990, H maser, PRL 64 2599": {
        "f_Hz": 8.9e-6, "eV": 3.7e-20, "frac_BA": None, "nuclide": None, "url": _APS + "64.2599",
        "printed": "'a limit of 3.7x10^{20} eV (8.9 uHz) on the magnitude of a nonlinear correction to the quantum "
                   "mechanics of atomic spins' -- the exponent's minus sign is ABSENT AT SOURCE (the page's own "
                   "description metadata prints 10^{20}; the rendered abstract drops the power entirely)",
        "f_status": "READ (abstract): printed in Hz; the eV exponent -20 is DERIVED from the printed 8.9 uHz (G33)",
        "status": WEINBERG_ROUTE + " (" + _APS + "64.2599)"},
    "Bollinger+ 1989, 9Be+, PRL 63 1031": {
        "f_Hz": None, "frac_BA": 4e-27, "nuclide": (4, 9), "url": _APS + "63.1031",
        "printed": "'a limit of 4 x 10^-27 on the fraction of binding energy per nucleon of the 9Be+ nucleus that could "
                   "be due to nonlinear corrections'",
        "f_status": "DERIVED-FROM-READ under H-BEFRAC (one significant figure printed)",
        "status": WEINBERG_ROUTE + " (" + _APS + "63.1031)"},
    "Chupp & Hoare 1990, 21Ne, PRL 64 2261": {
        "f_Hz": None, "frac_BA": 1.6e-26, "nuclide": (10, 21), "url": _APS + "64.2261",
        "printed": "'less than 1.6 x 10^-26 of the binding energy per nucleon of 21Ne'; an Erratum exists, PRL 66, 120 "
                   "(1991), whose public page carries no abstract -- its content is NAMED-NOT-READ (H-ERRATUM)",
        "f_status": "DERIVED-FROM-READ under H-BEFRAC; H-ERRATUM",
        "status": WEINBERG_ROUTE + " (" + _APS + "64.2261)"},
}
# Context, READ (abstract) the same way, NOT a bound used below: Weinberg, PRL 62, 485 (1989), public abstract page:
# NBS measurements 'already set limits of order 10^-21 on the fraction of the energy of the 9Be nucleus' -- a different
# normalisation (the nucleus's energy, not B/A), superseded by Bollinger 1989.
WEINBERG_1989_CONTEXT = {"url": _APS + "62.485", "printed": "'limits of order 10^-21 on the fraction of the energy of "
                         "the 9Be nucleus'", "status": WEINBERG_ROUTE}
# Later literature searched for a restatement carrying the numbers (none found): READ via alphaXiv quant-ph/9801041v1
# p.2 (Abrams-Lloyd: cites all four as refs [13]-[16], 'all known experiments confirm the linearity of quantum mechanics
# to a high degree of accuracy', no numbers); 2206.12976v1 pp.1-2 (Brož et al.: refs [9]-[12], 'stringent bounds', and
# that they do not carry over to causal (KR) nonlinearity -- no numbers); 2506.04298v1 (does not cite them);
# 2203.10269v3 (Raizen-Gilbert-Budker: Weinberg's 2016 Lindblad extension, a different model; does not restate them).
# Firecrawl research search (two framings) and alphaXiv discovery returned no other restatement.
WEINBERG_LATER = ("quant-ph/9801041v1 p.2", "2206.12976v1 pp.1-2", "2506.04298v1", "2203.10269v3")


def binding_per_nucleon_eV(Z, A):
    """B/A in eV from the AME2020 Table I capture (gravity.nuclides(), imported, never copied): atomic mass excesses,
    B = Z Delta(1H) + N Delta(n) - Delta(Z, A).  DERIVED-FROM-READ."""
    n = {(r[0], r[2]): r[4] for r in GR.nuclides()}
    return (Z * n[(1, 1)] + (A - Z) * n[(0, 1)] - n[(Z, A)]) * 1e3 / A


def befrac_to_hz(frac, Z, A, norm="B/A"):
    """H-BEFRAC: a limit stated as a fraction of a nuclear energy, as a frequency f = frac x E / h.  norm 'B/A' is the
    abstracts' wording; 'B' (whole-nucleus binding) and 'm_u c^2' (nucleon rest energy) exist only as CONTROLS (G32)."""
    E = binding_per_nucleon_eV(Z, A)
    if norm == "B":
        E *= A
    elif norm == "m_u c^2":
        E = 931.49410242e6
    return frac * E * E_CHARGE / H_PLANCK


for _k, _d in BOUNDS_WEINBERG.items():                 # fill the DERIVED-FROM-READ frequencies (H-BEFRAC)
    if _d["f_Hz"] is None:
        _d["f_Hz"] = befrac_to_hz(_d["frac_BA"], *_d["nuclide"])


# ======================================================================================= A. the drift signal
def bob_y_exact(eps, T):
    """Bob's <sigma_y> after drift time T, Alice measured x (z gives exactly 0).  Derived in derive_law()."""
    return math.tanh(2.0 * eps * T)


def bloch_exact(r0, eps, T):
    """Closed form for H = eps <X> Z on any pure/mixed single-qubit Bloch vector r0 = (x0, y0, z0).
    rho_perp = sqrt(x0^2 + y0^2) is conserved; phi' = 2 eps rho_perp cos(phi);  y = rho_perp tanh(atanh(y0/rho_perp)
    + 2 eps rho_perp T); x keeps its sign (phi never crosses x = 0, a fixed line); z constant."""
    x0, y0, z0 = r0
    rp = math.hypot(x0, y0)
    if rp == 0.0 or x0 == 0.0:
        return (x0, y0, z0)
    s = max(-1.0 + 1e-15, min(1.0 - 1e-15, y0 / rp))
    y = rp * math.tanh(math.atanh(s) + 2.0 * eps * rp * T)
    x = math.copysign(math.sqrt(max(rp * rp - y * y, 0.0)), x0)
    return (x, y, z0)


def bloch_of(psi):
    return tuple(float(np.real(psi.conj() @ s @ psi)) for s in (X, Y, Z))


def bob_numeric(basis, eps, T, obs, lin=False, n=None):
    n = n or max(3000, int(4000 * T))
    return float(np.mean([np.real(e.conj() @ obs @ e) for e in (NL.evolve(s, eps, lin, T=T, n=n) for s in NL.ENS[basis])]))


def derive_law():
    """sympy: phi(t) = 2 atan(tanh(eps t)) solves phi' = 2 eps cos(phi), phi(0) = 0, and sin(phi) = tanh(2 eps t)."""
    import sympy as sp
    e, t = sp.symbols("epsilon t", positive=True)
    phi = 2 * sp.atan(sp.tanh(e * t))
    ode = sp.simplify(sp.diff(phi, t) - 2 * e * sp.cos(phi))
    ident = sp.simplify(sp.sin(phi) - sp.tanh(2 * e * t))
    pts = [(0.1, 3.0), (1e-3, 3.0), (0.37, 0.9), (2.0, 1.3), (5e-2, 40.0)]
    num_ode = max(abs(float(sp.diff(phi, t).subs({e: a, t: b}) - 2 * a * sp.cos(phi.subs({e: a, t: b})))) for a, b in pts)
    num_id = max(abs(float(ident.subs({e: a, t: b}))) for a, b in pts)
    return {"ode_residual_symbolic": str(ode), "identity_residual_symbolic": str(ident),
            "ode_residual_numeric": num_ode, "identity_residual_numeric": num_id}


def ensemble_mean(n_vec, eps, T):
    """Alice measures along unit vector n; Bob (singlet) is left in -n or +n, each w.p. 1/2."""
    a = bloch_exact(tuple(-c for c in n_vec), eps, T)
    b = bloch_exact(tuple(n_vec), eps, T)
    return tuple((p + q) / 2 for p, q in zip(a, b))


def best_basis(eps, T, grid=91):
    """Over Alice's measurement axes (whole sphere, grid), the largest Bob-side Bloch displacement relative to her
    z-basis ensemble (whose mean is 0 for all eps).  Trace distance = |dr|/2."""
    best = (0.0, None)
    for i in range(grid):
        th = math.pi * i / (grid - 1)
        for j in range(2 * grid):
            ph = math.pi * j / grid
            n = (math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th))
            m = ensemble_mean(n, eps, T)
            L = math.sqrt(sum(c * c for c in m))
            if L > best[0]:
                best = (L, n)
    return best


# ======================================================================================= B. what the signal is worth
def h2(p):
    return 0.0 if p <= 0.0 or p >= 1.0 else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def mi(D, q=0.5):
    """Alice picks x (prob q) or z; Bob measures sigma_y.  P(+|z) = 1/2, P(+|x) = (1 + D)/2."""
    p0, p1 = 0.5, (1 + D) / 2
    return h2(q * p1 + (1 - q) * p0) - q * h2(p1) - (1 - q) * h2(p0)


def capacity(D):
    lo, hi = 0.0, 1.0                                 # I(q) is concave in q: golden section
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a, b = hi - g * (hi - lo), lo + g * (hi - lo)
        if mi(D, a) < mi(D, b):
            lo = a
        else:
            hi = b
    q = (lo + hi) / 2
    return mi(D, q), q


def holevo(D, q=0.5):
    """chi for {z: I/2, x: Bloch (0, D, 0)} with prior q: S(avg) - sum q S."""
    S = lambda L: h2((1 + L) / 2)
    return S(q * D) - q * S(D) - (1 - q) * S(0.0)


def rate_optimum(eps, Tmax_factor=50.0):
    """Maximise capacity(tanh(2 eps T))/T over T: bits per pair per second of Bob's holding time."""
    best = (0.0, 0.0)
    for k in range(1, 4001):
        T = (Tmax_factor / eps) * k / 4000
        r = capacity(math.tanh(2 * eps * T))[0] / T
        if r > best[0]:
            best = (r, T)
    return best


CMAX = capacity(1.0)[0]                               # the D -> 1 ceiling of this two-input family


def eps_to_remove(L_m, N_pairs, frac=0.5, cap=None, cmax=None):
    """Smallest eps such that N pairs, each held for T = frac * L/c, carry >= 2 bits (one teleported qubit).
    None if N * cmax < 2 (impossible at any eps).  frac = 0.5 (T = L/2c) is a DECLARED choice, kept as the default
    only so wave-1 figures can be compared: any frac < 1 already reads before light, and the eps above which SOME
    advantage exists is eps_any_advantage (frac -> 1), exactly half of this figure.  cap: per-pair capacity as a
    function of D (default nlcontrol's Z-channel, H-NLCONTROL-FORM)."""
    cap = cap or (lambda D: capacity(D)[0])
    cmax = CMAX if cmax is None else cmax
    T = frac * L_m / C_LIGHT
    if N_pairs * cmax < 2.0:
        return None
    lo, hi = 1e-30, 1e6
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if N_pairs * cap(math.tanh(2 * mid * T)) >= 2.0:
            hi = mid
        else:
            lo = mid
    return hi


def eps_any_advantage(L_m, N_pairs, **kw):
    """The infimum eps at which N pairs carry 2 bits with drift time T < L/c: above it the read precedes light.
    At the infimum itself T = L/c (no advantage), so the condition is eps > this value."""
    return eps_to_remove(L_m, N_pairs, frac=1.0, **kw)


def D_needed(N_pairs, cap=None, cmax=None):
    """The trace distance D at which N pairs carry exactly 2 bits.  None if impossible."""
    cap = cap or (lambda D: capacity(D)[0])
    cmax = CMAX if cmax is None else cmax
    if N_pairs * cmax < 2.0:
        return None
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if N_pairs * cap(mid) >= 2.0:
            hi = mid
        else:
            lo = mid
    return hi


def drift_time_needed(N_pairs, eps, **kw):
    """T = atanh(D_N) / (2 eps): the drift time after which N pairs carry one teleported qubit's 2 bits.  It does
    NOT depend on distance (A1 wave 1 said so in words, then tabulated at T = L/2c)."""
    D = D_needed(N_pairs, **kw)
    if D is None:
        return None
    D = min(D, 1.0 - 1e-16)
    return math.atanh(D) / (2.0 * eps)


def arrival_early_fraction(L_m, N_pairs, eps, **kw):
    """1 - T/(L/c): how much earlier than light (as a fraction of the light time) the read happens, once pairs are
    in place.  Negative = later than light."""
    T = drift_time_needed(N_pairs, eps, **kw)
    return None if T is None else 1.0 - T / (L_m / C_LIGHT)


def first_transit_times(L_m, T_drift, source="midpoint"):
    """Times measured from the moment the pair source fires.  The pairs move at c (setup at <= c, not message
    latency).  'one-end': source at Alice, Bob holds his half from L/c; 'midpoint' (LEDGER D23 as corrected in
    DOCKET 67: 'a midpoint source spans D at D/(2c)'): both hold their halves from L/(2c).  Alice measures as soon
    as she holds her half; Bob reads after the drift time T (counted from when he holds his half and Alice has
    measured: H-C2 needs the branch to exist).  Returns read time, light-from-Alice-at-firing arrival, and
    light-from-Alice-at-her-measurement arrival."""
    c = C_LIGHT
    if source == "one-end":
        t_alice, t_bob = 0.0, L_m / c
    else:
        t_alice = t_bob = L_m / (2 * c)
    t_read = max(t_alice, t_bob) + T_drift
    return {"source": source, "t_alice_measures": t_alice, "t_bob_holds": t_bob, "t_read": t_read,
            "light_from_alice_at_firing": L_m / c, "light_from_alice_at_her_measurement": t_alice + L_m / c,
            "beats_light_launched_at_firing": t_read < L_m / c,
            "beats_light_launched_at_measurement": t_read < t_alice + L_m / c}


def eps_readings(f_Hz):
    return {"A (eps = 2 pi f)": 2 * math.pi * f_Hz, "B (eps = pi f)": math.pi * f_Hz}


# ------------------------------------------------------------------------- B'. the W2 class, not one Hamiltonian
# Wave 1 carried nlcontrol's ceiling (log2 1.25 bits per pair, >= 6.21 pairs per teleported qubit) as if it were
# H-SETTLE's.  It is H-NLCONTROL-FORM's.  A second member of the same class (deterministic, per-branch, the state's
# own value steering its evolution) is H2 = eps (<X> Z + <Z> X): the Z term pulls Alice's x-branch states +-x to +y
# (nlcontrol's law), the X term pulls her z-branch states +-z to -y.  Bob measures sigma_y: a binary symmetric
# channel with crossover (1 - D)/2, D = tanh(2 eps T).  Its capacity 1 - h2((1-D)/2) -> 1 bit per pair.

def evolve_two_axis(psi, eps, T, n=None):
    """Frozen-H integrator for H2 = eps(<X> Z + <Z> X), nlcontrol.U per step (same scheme as nlcontrol.evolve)."""
    n = n or max(3000, int(2000 * T))
    p = np.array(psi, dtype=complex)
    dt = T / n
    for _ in range(n):
        ex = float(np.real(p.conj() @ X @ p))
        ez = float(np.real(p.conj() @ Z @ p))
        p = NL.U(eps * (ex * Z + ez * X), dt) @ p
        p /= np.linalg.norm(p)
    return p


def two_axis_signal(eps, T, n=None):
    """Bob's mean <sigma_y> for Alice's x choice minus her z choice, by the integrator.  Exact: 2 tanh(2 eps T)."""
    my = {b: float(np.mean([np.real(e.conj() @ Y @ e) for e in (evolve_two_axis(s, eps, T, n) for s in NL.ENS[b])]))
          for b in "xz"}
    return my["x"] - my["z"]


def capacity_bsc(D):
    """Two-axis drift: uniform prior is optimal by symmetry; the two states commute, so Holevo chi = this."""
    return 1.0 - h2((1.0 - D) / 2.0)


def _vn_bits(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    return float(-sum(x * math.log2(x) for x in w if x > 1e-14))


def readout_holevo_check(trials=300, seed=17):
    """H-BORN-AT-BOB: whatever drift produced Bob's per-choice states, his readout is a Born measurement of one
    qubit, and Holevo's chi of any qubit ensemble is <= log2 2 = 1 bit.  Computed on random ensembles of up to 8
    'choices' with random mixed states (the theorem is READ in A3; this checks the arithmetic).  Returns max chi."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        k = int(rng.integers(2, 9))
        pr = rng.random(k); pr /= pr.sum()
        sts = []
        for _ in range(k):
            A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            r = A @ A.conj().T
            sts.append(r / np.trace(r).real)
        avg = sum(p * r for p, r in zip(pr, sts))
        worst = max(worst, _vn_bits(avg) - sum(p * _vn_bits(r) for p, r in zip(pr, sts)))
    return worst


def finite_T_rank(eps=0.3, T=3.0):
    """Why the 1-bit ceiling is not reached at finite T: a drift is a flow, hence injective, so Alice's two
    outcomes in one basis stay distinct pure states and their mixture has rank 2 -- its smallest eigenvalue is > 0,
    so the two choices' states overlap and the trace distance is < 1.  Returns (min eigenvalue of Bob's x-choice
    state, trace distance between his x- and z-choice states) for H2, by the integrator."""
    rs = {b: sum(np.outer(v, v.conj()) for v in (evolve_two_axis(s, eps, T) for s in NL.ENS[b])) / 2 for b in "xz"}
    mn = float(np.linalg.eigvalsh(rs["x"]).min())
    td = 0.5 * float(np.abs(np.linalg.eigvalsh(rs["x"] - rs["z"])).sum())
    return mn, td


W2_CLASS_CEILING_BITS_PER_PAIR = math.log2(2)  # log2 2: Holevo at a one-qubit Born readout (H-BORN-AT-BOB) -- the bound
                                          # is checked by readout_holevo_check and approached by capacity_bsc(D -> 1).
                                          # WAVE 3: this is the ceiling of the QUBIT-ONLY SUBCLASS (H-QUBIT-DRIFT: the
                                          # drift acts on Bob's received qubit and nothing else).  It is NOT the W2
                                          # class's ceiling: see w2_ancilla_flow below (RV-1 #0).


# ------------------------------------------------------------------------- B''. wave 3: floors, zero error, the class
# RV-0 #0: N x C >= 2 is Shannon's converse -- NECESSARY, not sufficient.  The pair counts it gives are FLOORS.  When
# every pair of Alice's inputs can produce a common output of Bob's, no two codewords of any length are
# non-confusable, so the ZERO-ERROR capacity is 0 (Shannon 1956, NAMED-NOT-READ; the step is DERIVED here: two
# words are confusable iff every coordinate pair is equal or confusable).  Then no finite number of pairs per qubit
# delivers the 2 bits with certainty: reliable transfer is BLOCK-CODED over many qubits at a rate below C, with the
# error (and so the teleportation infidelity) going to 0 only as the block length goes to infinity (H-BLOCK).

def zero_error_words(P, n):
    """P: transition matrix P[input][output].  Returns the largest set of length-n input words that are pairwise
    NON-confusable (a zero-error code), by exhaustive search over the 2-letter alphabets used here (n <= 4)."""
    import itertools
    k = len(P)
    conf = [[any(P[a][y] > 0 and P[b][y] > 0 for y in range(len(P[0]))) for b in range(k)] for a in range(k)]
    words = list(itertools.product(range(k), repeat=n))
    nonconf = lambda u, v: any(not conf[a][b] for a, b in zip(u, v))
    best = 1
    for r in range(len(words), 1, -1):        # largest clique of the non-confusability graph (small: 2^n words)
        if r <= best:
            break
        for S in itertools.combinations(words, r):
            if all(nonconf(u, v) for u, v in itertools.combinations(S, 2)):
                best = r
                break
    return best


def zero_error_table(n_max=3):
    """Zero-error code sizes for nlcontrol's Z-channel and H2's BSC at D < 1 and D = 1.  log2(size)/n is the
    zero-error rate per pair at block length n."""
    def zch(D):                                       # inputs (x, z); outputs (+, -) of sigma_y
        return [[(1 + D) / 2, (1 - D) / 2], [0.5, 0.5]]

    def bsc(D):
        return [[(1 + D) / 2, (1 - D) / 2], [(1 - D) / 2, (1 + D) / 2]]
    out = {}
    for name, ch in (("nlcontrol Z-channel", zch), ("H2 BSC", bsc)):
        for D in (0.9, 0.999999, 1.0):
            out[(name, D)] = [zero_error_words(ch(D), n) for n in range(1, n_max + 1)]
    return out


def hermitian_from_tangent(psi, v):
    """DERIVED in RV-1 #0 and checked here: for unit psi and v orthogonal to psi, H = i(v psi^dag - psi v^dag) is
    Hermitian and -i H psi = v.  So any velocity field on the state sphere that is horizontal is generated by a
    state-dependent Hermitian H(psi): a W2-form drift (deterministic, per branch, the state's own value steering it)."""
    H = 1j * (np.outer(v, psi.conj()) - np.outer(psi, v.conj()))
    return H, float(np.abs(H - H.conj().T).max()), float(np.abs(-1j * H @ psi - v).max())


def _bloch_ket(n):
    x, y, z = n
    th = math.acos(max(-1.0, min(1.0, z)))
    ph = math.atan2(y, x)
    return np.array([math.cos(th / 2), complex(math.cos(ph), math.sin(ph)) * math.sin(th / 2)], complex)


FOUR_AXES = ((0.0, 0.0, 1.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (3 ** -0.5, 3 ** -0.5, 3 ** -0.5))


def w2_ancilla_flow(n_steps=800, seed=5, n_grid=401, linear_control=False):
    """RV-1 #0, COMPUTED.  Drop H-QUBIT-DRIFT, keep H-BORN-AT-BOB and H-C2.  Bob's received qubit sits beside a
    two-qubit ancilla in the fixed state |00> (Alice-independent), so his per-branch state lives in C^8.  Alice
    measures her singlet half along one of four axes (FOUR_AXES; uniform prior); outcome s leaves Bob's qubit along
    -s n_b, so there are 8 distinct branch states a_j (j = 2b + s).  The drift carries each a_j along the
    Fubini-Study geodesic to the j-th vector of an orthonormal basis (a seeded random unitary's columns), in time
    T = 1.  The curves are checked to be pairwise DISJOINT AS SETS (so one autonomous field, a function of the state
    alone, is single-valued on them); the field on them is H(psi) = i(v psi^dag - psi v^dag) (hermitian_from_tangent);
    off the curves H is taken from the nearest curve point (piecewise; a SMOOTH global extension is H-EXTEND,
    DERIVED from the curves' separation, not computed).  Each branch is integrated (RK4) under H evaluated on its
    own current state only.  Bob reads by a Born measurement in the target basis.
    linear_control=True replaces the drift by one fixed unitary for every branch (state-INDEPENDENT): chi must be 0.
    Returns chi (bits per pair), Bob's P(b' | b) table, the smallest end fidelity, the smallest inter-curve distance,
    the grid step, and max ||H|| x T (= the largest geodesic angle)."""
    rng = np.random.default_rng(seed)
    anc = np.zeros(4, complex)
    anc[0] = 1
    A = [np.kron(_bloch_ket(tuple(-s * c for c in n)), anc) for n in FOUR_AXES for s in (+1, -1)]
    Q, _ = np.linalg.qr(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))
    E = [Q[:, j] for j in range(8)]
    if linear_control:
        fin = [Q @ a for a in A]
        mind = step = th_max = float("nan")
        fid = float("nan")
    else:
        G = []
        for a, e in zip(A, E):
            ov = e.conj() @ a
            e2 = e * (ov / abs(ov) if abs(ov) > 1e-14 else 1.0)
            w = e2 - a * (a.conj() @ e2)
            G.append((math.acos(min(1.0, abs(ov))), w / np.linalg.norm(w)))
        ts = np.linspace(0.0, 1.0, n_grid)
        pt = lambda j, t: math.cos(G[j][0] * t) * A[j] + math.sin(G[j][0] * t) * G[j][1]
        vel = lambda j, t: G[j][0] * (-math.sin(G[j][0] * t) * A[j] + math.cos(G[j][0] * t) * G[j][1])
        P = np.array([[pt(j, t) for t in ts] for j in range(8)])
        mind = 9.0
        for j in range(8):
            for k in range(j + 1, 8):
                ov = np.abs(np.einsum("ti,si->ts", P[j].conj(), P[k]))
                mind = min(mind, float(np.arccos(np.clip(ov.max(), 0.0, 1.0))))
        th_max = max(g[0] for g in G)
        step = th_max / (n_grid - 1)
        flatP = P.reshape(-1, 8)
        flatV = np.array([[vel(j, t) for t in ts] for j in range(8)]).reshape(-1, 8)

        def rhs(psi):
            i = int(np.argmax(np.abs(flatP.conj() @ psi)))     # the field depends on the current state ONLY
            H = 1j * (np.outer(flatV[i], flatP[i].conj()) - np.outer(flatP[i], flatV[i].conj()))
            return -1j * H @ psi
        fin = []
        dt = 1.0 / n_steps
        for j in range(8):
            psi = A[j].copy()
            for _ in range(n_steps):
                k1 = rhs(psi); k2 = rhs(psi + dt / 2 * k1); k3 = rhs(psi + dt / 2 * k2); k4 = rhs(psi + dt * k3)
                psi = psi + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                psi /= np.linalg.norm(psi)
            fin.append(psi)
        fid = min(abs(E[j].conj() @ fin[j]) ** 2 for j in range(8))
    rhos = [(np.outer(fin[2 * b], fin[2 * b].conj()) + np.outer(fin[2 * b + 1], fin[2 * b + 1].conj())) / 2 for b in range(4)]
    chi = _vn_bits(sum(rhos) / 4) - sum(_vn_bits(r) for r in rhos) / 4
    table = [[float(sum(np.real(E[2 * bb + s].conj() @ rhos[b] @ E[2 * bb + s]) for s in (0, 1))) for bb in range(4)]
             for b in range(4)]
    return {"chi_bits_per_pair": float(chi), "P(b'|b)": table, "min_end_fidelity": fid,
            "min_curve_separation_rad": mind, "grid_step_rad": step, "max_H_times_T": th_max}


def hemisphere_axes(k):
    """k distinct unit axes on the open upper hemisphere (golden spiral, z = 1 - (i + 1/2)/k), so no axis is the
    antipode of another (an antipodal pair gives Bob the same two branch states, swapped)."""
    out = []
    for i in range(k):
        z = 1.0 - (i + 0.5) / k
        r = math.sqrt(1.0 - z * z)
        ph = i * math.pi * (3.0 - math.sqrt(5.0))
        out.append((r * math.cos(ph), r * math.sin(ph), z))
    return tuple(out)


def w2_ancilla_flow_k(k, m, n_steps=300, n_grid=201, seed=5, linear_control=False, antipodal=False):
    """V2-1 (FOR M) problem 1, COMPUTED (R3-alone, 2026-10-03): w2_ancilla_flow generalised from 4 axes and a
    two-qubit ancilla to k axes (hemisphere_axes) and an m-qubit ancilla, d = 2^(1+m) >= 2k.  Same construction and
    the same premises (H-BORN-AT-BOB, H-C2, H-COHERE, no H-QUBIT-DRIFT; a smooth global field is H-EXTEND, derived and
    not computed): 2k branch states, each carried along its Fubini-Study geodesic to one vector of an orthonormal basis
    under a field that depends on the current state only.  The branches are integrated together (vectorised RK4);
    the field at each branch is read from that branch's own state.  Controls: linear_control (one state-independent
    unitary: chi = 0); antipodal (the second half of the axes are antipodes of the first: branch states coincide,
    the curves collide, chi falls below log2 k).  Returns chi, pairs per teleported qubit (2/chi), Bob's error
    probability, the smallest end fidelity, curve separation, grid step, and max ||H|| x T."""
    d = 2 ** (1 + m)
    if d < 2 * k:
        raise ValueError("need d = 2^(1+m) >= 2k")
    rng = np.random.default_rng(seed)
    anc = np.zeros(2 ** m, complex)
    anc[0] = 1
    ax = list(hemisphere_axes(k))
    if antipodal:
        ax = ax[: k // 2] + [tuple(-c for c in n) for n in ax[: k // 2]]
    A = np.array([np.kron(_bloch_ket(tuple(-s * c for c in n)), anc) for n in ax for s in (+1, -1)])
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
    E = Q[:, : 2 * k].T.copy()
    if linear_control:
        fin = (Q @ A.T).T
        fid = mind = step = th_max = float("nan")
    else:
        ths, Ws = [], []
        for a, e in zip(A, E):
            ov = e.conj() @ a
            e2 = e * (ov / abs(ov) if abs(ov) > 1e-14 else 1.0)
            w = e2 - a * (a.conj() @ e2)
            nw = np.linalg.norm(w)
            ths.append(math.acos(min(1.0, abs(ov))))
            Ws.append(w / nw if nw > 1e-14 else w)
        ths, Ws = np.array(ths), np.array(Ws)
        ts = np.linspace(0.0, 1.0, n_grid)
        c, s_ = np.cos(np.outer(ths, ts)), np.sin(np.outer(ths, ts))           # (2k, n_grid)
        P = c[:, :, None] * A[:, None, :] + s_[:, :, None] * Ws[:, None, :]
        V = ths[:, None, None] * (-s_[:, :, None] * A[:, None, :] + c[:, :, None] * Ws[:, None, :])
        mind = 9.0
        for j in range(2 * k):
            for l in range(j + 1, 2 * k):
                ov = np.abs(P[j].conj() @ P[l].T)
                mind = min(mind, float(np.arccos(np.clip(ov.max(), 0.0, 1.0))))
        th_max = float(ths.max())
        step = th_max / (n_grid - 1)
        fP, fV = P.reshape(-1, d), V.reshape(-1, d)

        def rhs(Psi):
            idx = np.argmax(np.abs(fP.conj() @ Psi.T), axis=0)        # each branch's field from its own state only
            Pp, Vv = fP[idx], fV[idx]
            return Vv * np.sum(Pp.conj() * Psi, 1)[:, None] - Pp * np.sum(Vv.conj() * Psi, 1)[:, None]
        Psi = A.copy()
        dt = 1.0 / n_steps
        for _ in range(n_steps):
            k1 = rhs(Psi); k2 = rhs(Psi + dt / 2 * k1); k3 = rhs(Psi + dt / 2 * k2); k4 = rhs(Psi + dt * k3)
            Psi = Psi + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            Psi /= np.linalg.norm(Psi, axis=1, keepdims=True)
        fin = Psi
        fid = float(min(abs(E[j].conj() @ fin[j]) ** 2 for j in range(2 * k)))
    rhos = [(np.outer(fin[2 * b], fin[2 * b].conj()) + np.outer(fin[2 * b + 1], fin[2 * b + 1].conj())) / 2
            for b in range(k)]
    chi = _vn_bits(sum(rhos) / k) - sum(_vn_bits(r) for r in rhos) / k
    table = np.array([[sum(float(np.real(E[2 * bb + s].conj() @ rhos[b] @ E[2 * bb + s])) for s in (0, 1))
                       for bb in range(k)] for b in range(k)])
    return {"k": k, "m": m, "d": d, "chi_bits_per_pair": float(chi), "log2_k": math.log2(k),
            "holevo_ceiling_log2_d": math.log2(d),
            "pairs_per_teleported_qubit": (2.0 / chi) if chi > 1e-9 else float("inf"),
            "p_error": float(1.0 - np.trace(table) / k), "min_end_fidelity": fid, "min_curve_separation_rad": mind,
            "grid_step_rad": step, "max_H_times_T": th_max}

# ------------------------------------------------------------------------- C'. H-SETTLE x H-12: an unbounded carrier
H12_UNBOUNDED = ("alpha_s", "G", "v")     # the rows of H12 below whose state-dependent eps has NO READ bound of any
                                          # kind (KR fn.5 for alpha_s; KR p.14 for G; none located for v); G_F is tied
                                          # to v at tree level (named).  Z0's only bound is in the causal KR family.


def h12_carrier_case(L_list=None, N_list=(7, 1000, 1e6)):
    """Compare H-SETTLE-W under H-TRANSFER (eps capped by the NAMED-NOT-READ Majumder figure, reading A) with
    H-SETTLE-W x H-12 under H-12-CARRIER + H-12-W (the carrier is one of H12_UNBOUNDED, drifting in Weinberg form):
    no READ bound caps eps, so a cell is excluded only if no eps works at all (N x CMAX < 2).  Returns rows and the
    number of (L, N) cells that flip from EXCLUDED to NOT EXCLUDED.  'Not excluded' is not evidence either way."""
    L_list = L_list or (("1 AU", AU_M), ("1 ly", LY_M), ("4.24 ly (illustrative)", 4.24 * LY_M))
    f = BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    emax = eps_readings(f)["A (eps = 2 pi f)"]
    rows, flips = [], 0
    for Ln, L in L_list:
        for N in N_list:
            e_any = eps_any_advantage(L, N)
            transfer_ok = e_any is not None and e_any < emax
            carrier_ok = e_any is not None
            flips += (not transfer_ok) and carrier_ok
            rows.append({"L": Ln, "N": N, "eps_any_advantage": e_any, "eps_max_transfer_A": emax,
                         "H-TRANSFER": "NOT EXCLUDED" if transfer_ok else "EXCLUDED",
                         "H-12-CARRIER": "NOT EXCLUDED (no READ bound)" if carrier_ok else "IMPOSSIBLE at any eps"})
    return rows, flips


def window_given(L_list=None, N_list=(7, 1000, 1e6), bounds=None):
    """M's rule applied BOTH ways (V3 residual 3, M-apply 2026-10-03): an unread value makes a cell OPEN in either
    direction.  For support 1 (R_W2, nlcontrol's eps mapping) at each (L, N) and each reading of H-MAP:
      EMPTY window (eps_any >= eps_max)  -> 'EMPTY GIVEN W_W2' -> the cell is OPEN (N_WREAD; wave 4);
      OPEN window  (eps_any <  eps_max)  -> 'ADMISSIBLE GIVEN W_W2' -- flagged, not settled -- with the unread and the
                                            OPEN bounds named, and the tightening that would close it (eps_max / eps_any:
                                            CONTEXT, not evidence);
    a bound whose status is READ would drop the GIVEN flag (the control passes such a bound).  Support 2 (R_W2', the
    ancilla member) has no window at all: H-MAP is not established for its field, so it reads UNEVALUATED."""
    bounds = BOUNDS_WEINBERG_WAVE4 if bounds is None else bounds     # D68 wave 2: the default is the wave-4 RECORD
    L_list = L_list or (("1 AU", AU_M), ("1 ly", LY_M))              # (unread statuses); READ values: window_read()
    key = "Majumder+ 1990, 201Hg, PRL 65 2931"
    f = bounds[key]["f_Hz"]
    used_read = bounds[key]["status"].startswith("READ")
    unread = [k for k, v in bounds.items() if v["f_Hz"] is not None and not v["status"].startswith("READ")]
    open_ = [k for k, v in bounds.items() if v["f_Hz"] is None]
    rows = []
    for Ln, L in L_list:
        for N in N_list:
            e_any = eps_any_advantage(L, N)
            for lab, emax in eps_readings(f).items():
                if e_any is None:
                    verdict, tighten = "IMPOSSIBLE at any eps (N x CMAX < 2)", None
                elif e_any < emax:
                    verdict = "ADMISSIBLE" if used_read and not open_ else "ADMISSIBLE GIVEN W_W2 (flagged, not settled)"
                    tighten = emax / e_any
                else:
                    verdict = "EXCLUDED" if used_read and not open_ else "EMPTY GIVEN W_W2 -> cell OPEN (N_WREAD)"
                    tighten = None
                rows.append({"L": Ln, "N": N, "reading": lab, "eps_any": e_any, "eps_max": emax, "support 1": verdict,
                             "tightening to close (context)": tighten,
                             "support 2": "UNEVALUATED (H-MAP not established for its field)"})
    return {"rows": rows, "unread_bounds": unread, "open_bounds": open_, "bound_used": key,
            "bound_used_status": bounds[key]["status"]}


#: the hypotheses a READ-value window still rests on: W_W2 with its unread values removed (D68 wave 2, W2A-limits).
W_W2R = ("H-MAP", "H-TRANSFER", "H-SPIN", "H-DILUTION")
#: the three distances of the D68 wave-2 work item.  W2-fix (2026-10-04, verifier W2V-1 problem 3): the third distance is
#: Proxima's, IMPORTED from the board's owner, phase1.L_PROXIMA (Gaia DR3 parallax 768.066539187357 mas, READ via
#: restatement in DOCKET 67, key gaia-dr3-proxima-distance: Reyle et al. 2021 Table 1; 1/parallax = 4.24646 ly at
#: J2016.0).  The label '4.2465 ly' is that value to four decimals, kept so every cell key stays comparable.  Wave 2
#: first said: "4.2465 ly is the figure the task gives (Proxima Centauri's distance is NAMED-NOT-READ here)" and
#: typed 4.2465 * LY_M -- both wrong: the distance is READ on the board (phase1) and READ again this pass in a second
#: source (Faria 2022 Table 1 p.2, below), and the two READ values disagree by 0.06 % (PROXIMA_DISTANCES_READ).
#: The older rows at 4.24 ly '(illustrative)' are kept unchanged as history.
with contextlib.redirect_stdout(io.StringIO()):
    import phase1 as _phase1
L_PROXIMA_PHASE1 = _phase1.L_PROXIMA
WINDOW_READ_L = (("1 AU", AU_M), ("1 ly", LY_M), ("4.2465 ly", L_PROXIMA_PHASE1))
#: The two READ values of Proxima's distance (W2-fix).  Both are recorded; phase1's is the one imported for every
#: computation (it is the board's owner and the later catalogue); Faria's is kept beside it so the discrepancy is shown.
PROXIMA_DISTANCES_READ = {
    "phase1.L_PROXIMA (board)": {
        "parallax_mas": (_phase1.GAIA_DR3_PROXIMA_PARALLAX_MAS, 0.049872905),
        "source": "Gaia EDR3 = DR3, source_id 5853498713190525696, epoch J2016.0",
        "status": "READ-VIA-RESTATEMENT (DOCKET 67, key gaia-dr3-proxima-distance: Reyle et al. 2021, arXiv:2104.14972 "
                  "Table 1; the parallax error 0.049872905 mas from audit physical-constants-and-proxima)"},
    "Faria et al. 2022, Table 1 p.2": {
        "parallax_mas": (768.50, 0.20), "distance_pc_printed": (1.3012, 0.0003),
        "source": "arXiv:2202.05188v1 Table 1 p.2, 'compiled from the literature'; reference 1 for both rows is "
                  "'Gaia Collaboration et al. (2016)' -- a Gaia DR1-era value, not DR3",
        "status": "READ via alphaXiv (answer_pdf_queries on 2202.05188v1, Table 1 p.2), W2-fix 2026-10-04"},
}


def proxima_distances():
    """Both READ values in ly (au and parsec as phase1 defines them), their difference, and the window verdicts at
    Proxima recomputed at Faria's distance (does the discrepancy move any cell?).  Computed, never typed."""
    pc_m = _phase1.AU_M * 648000.0 / math.pi
    p_b, s_b = PROXIMA_DISTANCES_READ["phase1.L_PROXIMA (board)"]["parallax_mas"]
    fa = PROXIMA_DISTANCES_READ["Faria et al. 2022, Table 1 p.2"]
    p_f, s_f = fa["parallax_mas"]
    d_b = pc_m / (p_b / 1000.0)
    d_f = pc_m / (p_f / 1000.0)
    d_fp = fa["distance_pc_printed"][0] * pc_m
    wb = window_read(L_list=(("Proxima, phase1", d_b),))["rows"]
    wf = window_read(L_list=(("Proxima, Faria", d_f),))["rows"]
    return {"phase1 ly (1/parallax)": d_b / LY_M, "phase1 equals L_PROXIMA": abs(d_b / L_PROXIMA_PHASE1 - 1) < 1e-12,
            "Faria ly (1/parallax 768.50)": d_f / LY_M, "Faria ly (printed 1.3012 pc)": d_fp / LY_M,
            "Faria ly error (printed 0.0003 pc)": fa["distance_pc_printed"][1] * pc_m / LY_M,
            "Faria pc from its own parallax": d_f / pc_m, "phase1 pc": d_b / pc_m,
            "relative difference (phase1 - Faria) / Faria, distance": (d_b - d_f) / d_f,
            "parallax difference mas": p_f - p_b, "sigma on Faria parallax error alone": (p_f - p_b) / s_f,
            "sigma on both parallax errors": (p_f - p_b) / math.hypot(s_f, s_b),
            # Faria's printed 1.3012 pc is rounded (its own parallax gives 1.30124 pc), so measured against the printed
            # distance and its printed +-0.0003 pc the same discrepancy reads larger: this is the verifier's '2.6 sigma'
            "sigma on Faria printed distance and its printed error": (d_b - d_fp) / (fa["distance_pc_printed"][1] * pc_m),
            "windows at Proxima unchanged at Faria distance": [r["window"] for r in wb] == [r["window"] for r in wf],
            "windows (phase1)": [(r["N"], r["reading"][0], r["window"]) for r in wb]}


def window_read(L_list=WINDOW_READ_L, N_list=(7, 1000, 1e6), bounds=None, scale=1.0):
    """The W2 x F1 support-1 eps window at every (L, N) cell on the READ (abstract) Weinberg-family values (D68 wave 2).
    For each cell, H-MAP reading (A: eps = 2 pi f; B: eps = pi f) and bound: OPEN window if eps_any(L, N) < eps_max,
    else EMPTY.  A verdict names W_W2R (H-MAP, H-TRANSFER, H-SPIN, H-DILUTION) -- every one a named hypothesis -- and no
    longer an unread value.  The cell verdict uses the TIGHTEST READ bound; 'robust' says whether all four READ bounds
    give the same verdict (where they do not, H-SAME-EPS -- that the four experiments bound one common parameter --
    decides which applies; where they do, it does not matter).  An OPEN window is 'not excluded', never 'found': each
    limit is an upper limit measured consistent with zero.  scale multiplies every f (CONTROL G37 only)."""
    bounds = BOUNDS_WEINBERG if bounds is None else bounds
    fs = {k: d["f_Hz"] * scale for k, d in bounds.items()}
    tight = min(fs, key=fs.get)
    rows, cells = [], []
    for Ln, L in L_list:
        for N in N_list:
            e_any = eps_any_advantage(L, N)
            for lab in ("A (eps = 2 pi f)", "B (eps = pi f)"):
                per = {}
                for k, f in fs.items():
                    emax = eps_readings(f)[lab]
                    per[k] = {"eps_max": emax, "window": ("IMPOSSIBLE (N x CMAX < 2)" if e_any is None else
                                                          "OPEN" if e_any < emax else "EMPTY"),
                              "tightening to close (context)": (emax / e_any) if (e_any is not None and e_any < emax) else None,
                              "loosening to open (context)": (e_any / emax) if (e_any is not None and e_any >= emax) else None}
                w = per[tight]["window"]
                robust = len({v["window"] for v in per.values()}) == 1
                verdict = (("ADMISSIBLE (window OPEN; not excluded, not found)" if w == "OPEN" else
                            "EXCLUDED (window EMPTY)" if w == "EMPTY" else w) +
                           " given " + ", ".join(W_W2R) + f" (H-MAP reading {lab[0]}), on the READ (abstract) value"
                           + ("" if robust else "; NOT robust across the four READ bounds -- H-SAME-EPS decides"))
                rows.append({"L": Ln, "N": N, "reading": lab, "eps_any": e_any, "bound_used": tight,
                             "eps_max": per[tight]["eps_max"], "window": w, "robust_across_READ_bounds": robust,
                             "verdict": verdict, "per_bound": per})
            cells.append((Ln, N))
    return {"rows": rows, "tightest": tight, "f_Hz": fs, "hypotheses": W_W2R,
            "statuses": {k: bounds[k]["status"] for k in bounds}}


# ======================================================================================= D. collapse control
def lindblad_super(H, A, lam):
    I2 = np.eye(2)
    A2 = A @ A
    return (-1j * (np.kron(H, I2) - np.kron(I2, H.T))
            - 0.5 * lam * (np.kron(A2, I2) + np.kron(I2, A2.T) - 2 * np.kron(A, A.T)))


def expm(M):
    nrm = np.linalg.norm(M, 1)
    s = max(0, int(math.ceil(math.log2(nrm))) + 1) if nrm > 0 else 0
    Ms = M / (2 ** s)
    out, term = np.eye(M.shape[0], dtype=complex), np.eye(M.shape[0], dtype=complex)
    for k in range(1, 30):
        term = term @ Ms / k
        out = out + term
    for _ in range(s):
        out = out @ out
    return out


def lindblad_evolve(rho, H, A, lam, T):
    v = expm(lindblad_super(H, A, lam) * T) @ rho.reshape(4)
    return v.reshape(2, 2)


def sde_ensemble(psi0, H, A, lam, T, eps=0.0, n=400, N=4000, seed=11):
    """QMUPL-form stochastic Schrodinger equation (1204.4325v3 eq. 23 with q -> A), Euler-Maruyama, renormalised,
    optionally plus nlcontrol's deterministic drift eps <X> Z.  Returns final states (N x 2)."""
    rng = np.random.default_rng(seed)
    dt = T / n
    P = np.tile(psi0.astype(complex), (N, 1))
    for _ in range(n):
        dW = rng.normal(0.0, math.sqrt(dt), N)
        m = np.real(np.einsum("ni,ij,nj->n", P.conj(), A, P))
        ex = np.real(np.einsum("ni,ij,nj->n", P.conj(), X, P))
        AP = P @ A.T - m[:, None] * P
        A2P = AP @ A.T - m[:, None] * AP
        HP = P @ H.T + eps * ex[:, None] * (P @ Z.T)
        P = P - 1j * HP * dt + math.sqrt(lam) * AP * dW[:, None] - 0.5 * lam * A2P * dt
        P /= np.linalg.norm(P, axis=1)[:, None]
    return P


def bloch_stats(P):
    vals = [np.real(np.einsum("ni,ij,nj->n", P.conj(), s, P)) for s in (X, Y, Z)]
    return [float(v.mean()) for v in vals], [float(v.std() / math.sqrt(len(v))) for v in vals], vals


def signal_detector(stats_z, stats_x):
    """Same detector for every case: largest |difference| of Bob's mean Bloch components between Alice's z and x
    choices, in units of the combined MC standard error (exact cases pass sigma = 0)."""
    (mz, sz), (mx, sx) = stats_z, stats_x
    diffs = [abs(a - b) for a, b in zip(mz, mx)]
    sig = [math.hypot(a, b) for a, b in zip(sz, sx)]
    k = int(np.argmax(diffs))
    return diffs[k], sig[k], (diffs[k] / sig[k] if sig[k] > 0 else (math.inf if diffs[k] > 1e-12 else 0.0))


def collapse_control(seed=11):
    om, lam, T = 0.7, 1.0, 2.0
    H, A = om * Y, X                                 # A = sigma_x collapse, H breaks every reflection symmetry
    states = {"0": np.array([1, 0]), "1": np.array([0, 1]),
              "+": np.array([1, 1]) / math.sqrt(2), "-": np.array([1, -1]) / math.sqrt(2)}
    rows, worst_z = {}, 0.0
    for k, psi in states.items():
        P = sde_ensemble(psi, H, A, lam, T, seed=seed + ord(k))
        mean, se, vals = bloch_stats(P)
        rho_l = lindblad_evolve(np.outer(psi, psi.conj()).astype(complex), H, A, lam, T)
        lin = [float(np.real(np.trace(rho_l @ s))) for s in (X, Y, Z)]
        zsc = max(abs(a - b) / max(s, 1e-12) for a, b, s in zip(mean, lin, se))
        worst_z = max(worst_z, zsc)
        rows[k] = {"mc_mean": mean, "mc_se": se, "lindblad": lin, "max_z": zsc,
                   "mean_abs_x_per_trajectory": float(np.mean(np.abs(vals[0])))}
    # ensemble averages for Alice's two choices
    def ens(keys):
        m = [np.mean([rows[k]["mc_mean"][i] for k in keys]) for i in range(3)]
        s = [math.sqrt(sum(rows[k]["mc_se"][i] ** 2 for k in keys)) / len(keys) for i in range(3)]
        return m, s
    det = signal_detector(ens(["0", "1"]), ens(["+", "-"]))
    # exact: Lindblad of each ensemble's average
    rz = (lindblad_evolve(np.diag([1, 0]).astype(complex), H, A, lam, T) + lindblad_evolve(np.diag([0, 1]).astype(complex), H, A, lam, T)) / 2
    pp, mm = np.outer(states["+"], states["+"]).astype(complex), np.outer(states["-"], states["-"]).astype(complex)
    rx = (lindblad_evolve(pp, H, A, lam, T) + lindblad_evolve(mm, H, A, lam, T)) / 2
    return {"params": {"omega": om, "lambda": lam, "T": T, "A": "sigma_x", "H": "omega sigma_y"},
            "per_state": rows, "worst_mc_vs_lindblad_z": worst_z,
            "exact_ensemble_difference": float(np.abs(rz - rx).max()), "mc_detector": det}


def drift_plus_collapse(seed=5, lam=0.2, N=5000):
    eps, T = 0.3, 3.0
    out = {}
    for b in ("z", "x"):
        Ps = [sde_ensemble(np.array(s), np.zeros((2, 2)), Z, lam, T, eps=eps, n=600, N=N, seed=seed + i) for i, s in enumerate(NL.ENS[b])]
        P = np.vstack(Ps)
        m, s, _ = bloch_stats(P)
        out[b] = (m, s)
    return {"params": {"eps": eps, "lambda": lam, "T": T, "A": "sigma_z"}, "z": out["z"], "x": out["x"],
            "detector": signal_detector(out["z"], out["x"]), "noise_free_tanh": math.tanh(2 * eps * T)}


# ======================================================================================= E. H-12
def z0_from_alpha():
    return 2 * ALPHA * H_PLANCK / E_CHARGE ** 2      # SI-2019: Z0 = mu0 c = 2 alpha h / e^2, so dlnZ0 = dln alpha


S_SPAN = (0.0466, 0.0935)   # Feynman-Hellmann S = sum sigma_q/m_p, board span READ via D67 audit 0705.3704


def v_drift_from_mu(mu_dot=-8e-18, mu_sig=36e-18):
    """mu = m_p/m_e, m_e ∝ v (fixed Yukawa -- named).  dln m_p/dln v = S (board H2) or 2/9 + 7S/9 (board H1)."""
    out = {}
    for hyp, kp in (("H2", lambda S: S), ("H1", lambda S: 2 / 9 + 7 * S / 9)):
        for S in S_SPAN:
            k = kp(S) - 1.0                           # dln mu / dln v
            out[f"{hyp}, S={S}"] = (mu_dot / k, mu_sig / abs(k))
    return out


H12 = [  # (symbol, what the taxonomy PDF says it is, class, carrier, can carry a state-dependent drift?, bound, source)
    ("M", "Madelung (n+l) subshell ordering (Lemma I)", "EMERGENT (many-electron atomic structure)", "none -- a readout of alpha, m_e",
     "NO independent carrier: inherits alpha and v", "inherits alpha, mu bounds below", "taxonomy PDF p.1 (Drive, READ)"),
    ("R", "relativistic inert-pair contraction (Lemma II)", "EMERGENT (function of Z alpha)", "none -- a readout of alpha",
     "NO independent carrier: inherits alpha", "inherits alpha bound", "taxonomy PDF p.1"),
    ("K", "Kondo temperature T_K (Lemma III)", "MATERIAL PROPERTY (per material, exponential in exchange x DOS)", "none",
     "NO: not a constant of nature; varies by material", "no 'variation of a constant' bound applies (category)", "taxonomy PDF p.1"),
    ("T", "TA-phonon Grueneisen parameter (Lemma IV)", "MATERIAL PROPERTY", "none",
     "NO: not a constant of nature", "no bound applies (category)", "taxonomy PDF p.1"),
    ("CP", "CKM phase delta_CP (Lemma V)", "LAGRANGIAN PARAMETER (phase of the Yukawa matrices)", "Higgs-fermion Yukawa sector",
     "CONDITIONAL: only if the Yukawa matrix is itself a field (named)", "OPEN (no READ variation bound)", "--"),
    ("alpha_s", "strong coupling (Lemma VI)", "LAGRANGIAN PARAMETER", "gluon field (KR eps_S)",
     "YES in KR form; KR fn.5: 'no non-trivial bounds can be placed' on eps_S", "proxy X_s = m_s/Lambda_QCD: |Xs_dot/Xs| < 1e-18 /yr (Oklo)",
     "0705.3704v2 p.1, p.4 (READ); 2106.10576v2 p.13 fn.5 (READ)"),
    ("Z0", "vacuum impedance sqrt(mu0/eps0) (Lemma IX)", "DERIVED: Z0 = 2 alpha h/e^2 (computed), i.e. alpha", "photon field A_mu (KR eps_gamma)",
     "YES -- the ONLY carrier with a measured STATE-DEPENDENT bound: |eps_gamma| < 1.15e-12 (90% CL)",
     "alpha_dot/alpha = 1.0(1.1)e-18 /yr; (c^2/alpha) dalpha/dPhi = 14(11)e-9",
     "2411.09611v1 p.1,7; 2010.06620v2 p.1, Table II (READ)"),
    ("Lambda", "vacuum energy density (Lemma X)", "CONSTANT in GR; a field only if dark energy is dynamical (named)", "metric / a dark-energy field",
     "CONDITIONAL", "OPEN (no READ variation bound)", "--"),
    ("G", "Newton's constant (Lemma XI)", "COUPLING of the metric field", "metric g_mu_nu (KR eps_G)",
     "YES in KR form; 'not aware of any current experimental data ... to constrain eps_G' (KR p.14)",
     "G_dot/G = (4 +- 9)e-13 /yr (LLR)", "1009.5514v1 p.71 eq.133 restating Williams-Turyshev-Boggs 2004 (READ-VIA-RESTATEMENT); 2106.10576v2 p.14"),
    ("G_F", "Fermi constant (Lemma VII)", "LAGRANGIAN-DERIVED (W exchange; tree level 1/(sqrt2 v^2), named, not READ)", "W/Z fields",
     "YES in principle (bosonic field); no KR-type bound located", "OPEN (no READ numeric bound); tied to v at tree level", "--"),
    ("G_theta", "QCD vacuum angle (Lemma XII)", "LAGRANGIAN PARAMETER; a field only if an axion exists (2001.11966 p.1 refs 10-11)", "axion (named)",
     "CONDITIONAL on an axion", "static: |d_n| < 1.8e-26 e cm (90% CL); theta-bar conversion OPEN; variation OPEN", "2001.11966v1 p.6 (READ)"),
    ("v", "Higgs vev (Lemma VIII)", "EXPECTATION VALUE OF A BOSONIC FIELD -- KR's construction applies literally (KR eq. 4, Yukawa)", "Higgs field",
     "YES in KR form; no state-dependent bound located", "via mu = m_p/m_e: mu_dot/mu = -8(36)e-18 /yr (see v_drift_from_mu)", "2010.06620v2 p.1, Table II (READ)"),
]


# ======================================================================================= report
def build():
    R = {}
    # A
    R["law"] = derive_law()
    R["nlcontrol_vs_law"] = {e: (NLCONTROL_PRINTED[e], bob_y_exact(e, 3.0)) for e in NLCONTROL_PRINTED}
    grid = []
    for e in (1e-3, 1e-2, 1e-1, 0.3):
        for T in (0.5, 3.0, 10.0):
            num = bob_numeric("x", e, T, Y) - bob_numeric("z", e, T, Y)
            grid.append((e, T, num, bob_y_exact(e, T)))
    R["grid"] = grid
    R["linear_control"] = bob_numeric("x", 0.1, 3.0, Y, lin=True) - bob_numeric("z", 0.1, 3.0, Y, lin=True)
    R["best_basis"] = best_basis(0.1, 3.0)
    # B
    R["info"] = {D: (mi(D), capacity(D), holevo(D)) for D in (1e-3, 1e-2, 0.1, 0.5, 0.9, 1.0)}
    R["CMAX"] = CMAX
    R["min_pairs_per_qubit"] = 2.0 / CMAX
    # C
    R["walsworth_check_eV"] = H_PLANCK * 8.9e-6 / E_CHARGE
    R["kr_ratio_quoted_nearly_50"] = 4.7e-11 / 1.15e-12
    cond = {}
    f = BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    for lab, eps in eps_readings(f).items():
        rows = []
        for T in (1.0, 60.0, 3600.0, 86400.0):
            D = bob_y_exact(eps, T)
            rows.append((T, D, capacity(D)[0], (3.0 / D) ** 2))
        r, Topt = rate_optimum(eps)
        rem = {}
        for Lname, L in (("1 AU", AU_M), ("1 ly", LY_M), ("4.24 ly (illustrative)", 4.24 * LY_M)):
            for N in (1, 7, 1e3, 1e6):
                em = eps_to_remove(L, N)
                rem[(Lname, N)] = (em, None if em is None else em <= eps)
        cond[lab] = {"eps_max": eps, "rows": rows, "rate_opt": (r, Topt), "removal": rem,
                     "T_half": math.atanh(0.5) / (2 * eps)}
    R["conditional"] = cond
    # D
    R["collapse"] = collapse_control()
    R["drift_collapse"] = drift_plus_collapse()
    # E
    R["Z0"] = (z0_from_alpha(), Z0_SCIPY)
    R["v_drift"] = v_drift_from_mu()
    R["alpha_dot_improvement"] = 0.8e-16 / 1.1e-18   # Flambaum 2007 sigma / Lange 2021 sigma
    # F
    R["frame"] = {"pairs_one_frame": CO.n, "closed_one_frame": CO.bad,
                  "two_frames_closed": bool(CO.L.box_has_causal(CO.E1, CO.E2)),
                  "one_corridor_closed": bool(CO.L.rank1_has_causal(CO.E1))}
    # F' (wave 2): exact flat FRW forces corridor keying (frame.py's z3 time-function lemma, imported), so
    # H-SETTLE-W alone gets O-LOOP REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, N_SIGKEY}
    with contextlib.redirect_stdout(io.StringIO()):
        import frame as FRM
    R["frw_lemma"] = FRM.frw_time_function_lemma()
    R["c1_signal"] = FRM.settle_under_C1()
    # B' (wave 2): the W2 class
    R["two_axis"] = {"signal_eps0.1_T3": two_axis_signal(0.1, 3.0), "exact": 2 * math.tanh(0.6),
                     "cap_D": {D: capacity_bsc(D) for D in (0.1, 0.5, 0.9, 0.99, 0.999999)},
                     "readout_holevo_max": readout_holevo_check(), "finite_T_rank": finite_T_rank()}
    # Wave 3 (RV-0 #0, RV-1 #0): every count from N x C >= 2 is a FLOOR (Shannon's converse); the qubit-only rows
    # are the subclass H-QUBIT-DRIFT, not the W2 class.  Wave 2 first labelled them 'nlcontrol, per qubit (integer)'
    # and 'W2 class under H-BORN-AT-BOB'.
    R["pairs_per_qubit"] = {"nlcontrol (H-NLCONTROL-FORM), average, block-coded (H-BLOCK): floor": 2.0 / CMAX,
                            "nlcontrol, one qubit coded alone: floor (no finite N is zero-error; zero-error capacity 0)": math.ceil(2.0 / CMAX),
                            "qubit-only subclass (H-BORN-AT-BOB + H-QUBIT-DRIFT), average: infimum, not attained": 2.0 / W2_CLASS_CEILING_BITS_PER_PAIR,
                            # strict: the 1-bit ceiling is not attained at finite T (finite_T_rank), so N x C = 2 needs N > 2
                            "qubit-only subclass, one qubit coded alone at finite T: floor":
                                math.floor(2.0 / W2_CLASS_CEILING_BITS_PER_PAIR) + 1}
    R["zero_error"] = zero_error_table()
    R["w2_ancilla"] = w2_ancilla_flow()
    R["w2_ancilla_linear_control"] = w2_ancilla_flow(linear_control=True)
    # wave 4 (R3-alone; V2-1 problem 1): the class has no positive floor on pairs per teleported qubit
    R["w2_k"] = [w2_ancilla_flow_k(4, 2), w2_ancilla_flow_k(8, 3), w2_ancilla_flow_k(16, 4), w2_ancilla_flow_k(32, 5)]
    R["w2_k_control_antipodal"] = w2_ancilla_flow_k(8, 3, antipodal=True)
    R["w2_k_control_linear"] = w2_ancilla_flow_k(16, 4, linear_control=True)
    rng = np.random.default_rng(23)
    herm = []
    for _ in range(50):
        psi = rng.normal(size=8) + 1j * rng.normal(size=8); psi /= np.linalg.norm(psi)
        v = rng.normal(size=8) + 1j * rng.normal(size=8); v -= psi * (psi.conj() @ v)
        herm.append(hermitian_from_tangent(psi, v)[1:])
    vbad = rng.normal(size=8) + 1j * rng.normal(size=8)          # NOT orthogonal to psi: -iH psi = v must FAIL
    R["hermitian_tangent"] = {"max_nonhermiticity": max(h[0] for h in herm), "max_residual": max(h[1] for h in herm),
                              "control_nonorthogonal_residual": hermitian_from_tangent(psi, vbad)[2]}
    # C' (wave 2): timing.  Drift time is distance-independent; eps for any advantage is half the T = L/2c figure.
    tim = {}
    for lab, eps in eps_readings(f).items():
        for N in (7, 1000):
            T = drift_time_needed(N, eps)
            tim[(lab, N)] = {"T_s": T, "T_h": T / 3600, "early_fraction_1ly": arrival_early_fraction(LY_M, N, eps),
                             "first_transit_midpoint_1ly": first_transit_times(LY_M, T, "midpoint"),
                             "first_transit_one_end_1ly": first_transit_times(LY_M, T, "one-end")}
    R["timing"] = tim
    R["eps_any_vs_half"] = {(Ln, N): (eps_any_advantage(L, N), eps_to_remove(L, N))
                            for Ln, L in (("1 AU", AU_M), ("1 ly", LY_M), ("4.24 ly (illustrative)", 4.24 * LY_M))
                            for N in (7, 1e3, 1e6)}
    R["two_axis_eps_any_1ly_N3"] = eps_any_advantage(LY_M, 3, cap=capacity_bsc, cmax=1.0)
    # C'' (wave 2): H-SETTLE x H-12 with an unbounded carrier
    R["h12_case"] = h12_carrier_case()
    R["window_given"] = window_given()                    # M-apply (V3 residual 3): the rule both ways
    R["window_given_control_read"] = window_given(bounds={  # CONTROL: the same value marked READ, nothing OPEN
        "Majumder+ 1990, 201Hg, PRL 65 2931": {"f_Hz": BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"],
                                               "status": "READ (control fixture, not a claim)"}})
    # D68 wave 2 (W2A-limits): the Weinberg-family limits READ (abstract) at source, and the window on the READ values
    R["weinberg_read"] = {k: {kk: vv for kk, vv in d.items()} for k, d in BOUNDS_WEINBERG.items()}
    R["befrac_majumder_check"] = {"B/A_201Hg_eV": binding_per_nucleon_eV(80, 201),
                                  "f_from_frac_Hz": befrac_to_hz(2.0e-27, 80, 201), "f_printed_Hz": 3.8e-6,
                                  "CONTROL f with whole-nucleus B": befrac_to_hz(2.0e-27, 80, 201, "B"),
                                  "CONTROL f with nucleon rest energy": befrac_to_hz(2.0e-27, 80, 201, "m_u c^2")}
    R["bollinger_range_Hz"] = (befrac_to_hz(3.5e-27, 4, 9), befrac_to_hz(4.5e-27, 4, 9))   # one printed digit: 3.5..4.5
    R["walsworth_plus20_Hz"] = 3.7e20 * E_CHARGE / H_PLANCK          # the exponent as printed at source (CONTROL)
    R["window_read"] = window_read()
    R["window_read_control_tighter_1e7"] = window_read(scale=1e-7)
    R["window_read_control_looser_1e3"] = window_read(scale=1e3)
    R["proxima_distances"] = proxima_distances()
    return R


def report(R):
    p = print
    p("=" * 110)
    p("settle.py -- DOCKET 68 / A1-settle: H-SETTLE (deterministic drift), the collapse control, H-12 carriers")
    p("=" * 110)
    p("\nA. THE SIGNAL AT BOB under nlcontrol's drift H = eps <X> Z (imported)")
    L = R["law"]
    p(f"   exact law <sigma_y>_x - <sigma_y>_z = tanh(2 eps T): sympy ODE residual {L['ode_residual_symbolic']}, "
      f"identity residual {L['identity_residual_symbolic']}; numeric {L['ode_residual_numeric']:.1e}, {L['identity_residual_numeric']:.1e}")
    for e, (pr, ex) in R["nlcontrol_vs_law"].items():
        p(f"   nlcontrol printed (T=3) eps={e:<6}: {pr:.5f}   tanh(2 eps T) = {ex:.6f}")
    p("   grid (nlcontrol integrator vs exact):")
    for e, T, num, ex in R["grid"]:
        p(f"     eps={e:<6} T={T:<5} numeric {num:+.6f}   exact {ex:+.6f}   diff {num - ex:+.1e}")
    p(f"   LINEAR control (H = eps Z): signal {R['linear_control']:+.2e}")
    bb = R["best_basis"]
    p(f"   best Alice axis over the sphere (eps=0.1, T=3): |dr| = {bb[0]:.6f} at n = ({bb[1][0]:+.3f},{bb[1][1]:+.3f},{bb[1][2]:+.3f});"
      f" x-basis gives {math.tanh(0.6):.6f}")
    p("\nB. WHAT IT IS WORTH (Bob measures sigma_y; Alice picks x or z)")
    for D, (m, (c, q), chi) in R["info"].items():
        p(f"   D={D:<6} I(uniform) {m:.4e} bits  capacity {c:.4e} (q*={q:.3f})  Holevo(uniform) {chi:.4e}  D^2/(8 ln2) {D*D/(8*LN2):.4e}")
    p(f"   ceiling at D -> 1: {R['CMAX']:.6f} bits/pair = log2(1.25) = {math.log2(1.25):.6f};  pairs per teleported qubit >= {R['min_pairs_per_qubit']:.3f}")
    p("   (ceiling of THIS two-choice protocol; mean y >= 0 for every Alice axis, so no antipodal letter exists.  The pair count is a")
    p("    FLOOR from Shannon's converse; this Z-channel's zero-error capacity is 0 at every D (both inputs give '+'), so reliable")
    p("    transfer is block-coded (H-BLOCK).  Wave 1 first printed here: 'Any protocol on a qubit is capped at 1 bit per pair by")
    p("    Holevo's bound -- NAMED-NOT-READ here -- so >= 2 pairs per teleported qubit always' -- Holevo is READ in A3 and binds only")
    p("    a Born readout of a QUBIT (H-BORN-AT-BOB + H-QUBIT-DRIFT); see WAVE 3 for the class without H-QUBIT-DRIFT.)")
    p("\nC. BOUNDS")
    p("   KR (causal) family -- dimensionless eps_gamma, READ:")
    for k, (v, src) in BOUNDS_KR.items():
        p(f"     {k:<52} {v:.3g}   [{src}]")
    p(f"     2411.09611 says 'nearly a factor of 50' over 4.7e-11; computed ratio {R['kr_ratio_quoted_nearly_50']:.2f}  (wording discrepancy, not a refutation)")
    p("     KR's Lamb-shift estimate: printed 1e-4 in KR v2 p.14, restated as 1e-2 by Brož p.2 -- DISCREPANCY between the two READ texts, recorded.")
    p("     => superluminal signal at Bob permitted by this family: 0 for every eps (KR sec. 2.3: evolution of separated systems factorises).")
    p("   Weinberg family -- READ (abstract) at source in D68 wave 2 (waves 1-4 said NAMED-NOT-READ / OPEN; see the last section):")
    for k, d in BOUNDS_WEINBERG.items():
        p(f"     {k:<40} f = {d['f_Hz']:.4e} Hz  [{d['f_status']}]")
    p(f"     consistency: h x 8.9 uHz = {R['walsworth_check_eV']:.3e} eV (abstract: 3.7e-20 eV)")
    for lab, c in R["conditional"].items():
        p(f"   CONDITIONAL on H-MAP reading {lab}, H-TRANSFER, H-SPIN, H-COHERE, H-FRAME3b, H-C2, H-NLCONTROL-FORM, eps AT the Majumder upper limit:")
        p(f"     eps_max = {c['eps_max']:.4e} /s;  drift time to D = 0.5: {c['T_half']:.4e} s = {c['T_half']/3600:.2f} h")
        for T, D, C, Nd in c["rows"]:
            p(f"     T = {T:>8.0f} s: D = {D:.4e}, capacity {C:.4e} bits/pair, pairs for a 3-sigma detection {Nd:.3e}")
        r, To = c["rate_opt"]
        p(f"     best rate per pair: {r:.4e} bits/s at T = {To:.4e} s ({To/3600:.2f} h)")
        for (Ln, N), (em, ok) in c["removal"].items():
            if em is None:
                p(f"     O-BITS at {Ln:<24} with N = {N:<8g}: IMPOSSIBLE at any eps (N x {CMAX:.4f} < 2 bits)")
            else:
                p(f"     O-BITS at {Ln:<24} with N = {N:<8g}: needs eps >= {em:.4e} /s at T = L/2c (wave-1 table; T = L/2c is a DECLARED choice,"
                  f" any advantage needs only half: see WAVE 2)  -> {'NOT EXCLUDED' if ok else 'EXCLUDED'} by the Majumder bound (READ (abstract) in D68 wave 2; unread in waves 1-4)")
    p("\nD. COLLAPSE-TYPE (STOCHASTIC) DRIFT -- the control that must NOT signal")
    C = R["collapse"]
    for k, r in C["per_state"].items():
        p(f"   |{k}>: MC mean {np.round(r['mc_mean'],4)}  Lindblad {np.round(r['lindblad'],4)}  max z {r['max_z']:.2f}  "
          f"per-trajectory <|x|> {r['mean_abs_x_per_trajectory']:.3f}")
    p(f"   exact (Lindblad) difference between Alice's ensembles: {C['exact_ensemble_difference']:.2e}")
    d, s, zz = C["mc_detector"]
    p(f"   MC detector: |diff| {d:.4f} +- {s:.4f}  ({zz:.2f} sigma)  -> {'NO SIGNAL' if zz < 4 else 'SIGNAL'}")
    DC = R["drift_collapse"]
    d, s, zz = DC["detector"]
    p(f"   must-signal control, drift + collapse (eps=0.3, lambda=0.2, T=3): |diff| {d:.4f} +- {s:.4f} ({zz:.1f} sigma); "
      f"noise-free tanh {DC['noise_free_tanh']:.4f}")
    p("\nE. H-12 -- which of the twelve could carry a state-dependent drift")
    p(f"   Z0 = 2 alpha h / e^2 = {R['Z0'][0]:.9f} ohm (scipy CODATA: {R['Z0'][1]:.9f}) -> Z0's variation IS alpha's.")
    for row in H12:
        p(f"   {row[0]:<8} {row[2]}\n            carrier: {row[3]} | drift: {row[4]}\n            bound: {row[5]}  [{row[6]}]")
    p("   v from mu (fixed Yukawa, named):")
    for k, (c, s) in R["v_drift"].items():
        p(f"     {k:<14}: v_dot/v = {c:+.2e} +- {s:.2e} /yr")
    p(f"   alpha_dot sigma improved {R['alpha_dot_improvement']:.0f}x from Flambaum 2007 (0.8e-16) to Lange 2021 (1.1e-18)")
    p("   NAMED LIMIT: a time-variation bound bounds a drift common to all states; it does not bound STATE-dependence.")
    p("\nF. H-SETTLE x H-FRAME (corridors.py imported)")
    F = R["frame"]
    p(f"   one corridor closes a causal curve: {F['one_corridor_closed']}; two frames: {F['two_frames_closed']}; "
      f"{F['pairs_one_frame']} one-frame pairs, closed: {F['closed_one_frame']}")
    p("   Gisin's protocol needs a fixed slicing (2412.20854 assumption 3b): keyed to ONE frame it closes no loop in this model.")
    zl = R["frw_lemma"]
    p(f"   exact flat FRW (frame.frw_time_function_lemma, imported): claim {zl['claim']} (unsat = proved), vacuity {zl['vacuity']},"
      f" control a>=0 {zl['control_a_ge_0']} -> corridor keying is FORCED by H-FRW-EXACT + H-NOT-DE-SITTER;")
    p("   O-LOOP for CORRIDORS: REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL} BY THE GEOMETRY, credited to no hypothesis")
    p("   (wave 2 first credited it to H-SETTLE-W alone, with N_SIGKEY; RV-0 #3).  For SIGNALS, which exist only where a channel")
    p("   exists (W2 with a preferred slicing): REMOVED-IF {N_SIGKEY under H-SIG-COR}.  Under ITB + N_QTOPO the lemma does not bind")
    p("   an ITB corridor (not a Lorentzian quotient): corridor O-LOOP NOT-BOUND-IF {N_QTOPO}; {N_QTOPO, N_CORR} is a premise clash.")
    p("\nWAVE 2 -- CONVENTION, CAPACITY, TIMING, H-12")
    p(f"   H-C2 named: under C1 (drift on Bob's reduced state) the signal is {R['c1_signal']:.1e} (frame.settle_under_C1) -- no channel.")
    ta = R["two_axis"]
    p(f"   second W2 Hamiltonian eps(<X>Z + <Z>X): signal at eps=0.1, T=3 = {ta['signal_eps0.1_T3']:+.6f} (exact 2 tanh 0.6 = {ta['exact']:.6f})")
    p("     capacity (BSC, uniform prior) at D: " + ", ".join(f"{D}: {c:.6f}" for D, c in ta["cap_D"].items()))
    p(f"     Holevo at a one-qubit Born readout, 300 random ensembles: max chi = {ta['readout_holevo_max']:.6f} <= 1 bit (H-BORN-AT-BOB)")
    mn, td = ta["finite_T_rank"]
    p(f"     finite T (eps=0.3, T=3): Bob's x-choice state min eigenvalue {mn:.3e} > 0, trace distance {td:.6f} < 1 -> ceiling not attained")
    for k, v in R["pairs_per_qubit"].items():
        p(f"     pairs per teleported qubit, {k}: {v if isinstance(v, int) else round(v, 4)}")
    p(f"     two-axis drift at 1 ly with N = 3: eps for any advantage {R['two_axis_eps_any_1ly_N3']:.4e} /s (H-MAP not established for this H)")
    p("   timing (drift time does not depend on distance; reading A/B at the Majumder limit -- NAMED-NOT-READ in waves 1-4, READ (abstract) in D68 wave 2):")
    for (lab, N), t in R["timing"].items():
        mp, oe = t["first_transit_midpoint_1ly"], t["first_transit_one_end_1ly"]
        p(f"     {lab}, N = {N}: T = {t['T_h']:.2f} h; later transits at 1 ly read {t['early_fraction_1ly']:.5f} of L/c early;"
          f" first transit, midpoint source: read at {mp['t_read']/YEAR_S:.6f} yr (light from Alice at firing {mp['light_from_alice_at_firing']/YEAR_S:.4f} yr:"
          f" beats it {mp['beats_light_launched_at_firing']}); one-end: {oe['t_read']/YEAR_S:.6f} yr (beats {oe['beats_light_launched_at_firing']})")
    p("   eps for ANY advantage (T -> L/c) vs wave 1's T = L/2c figure:")
    for (Ln, N), (ea, eh) in R["eps_any_vs_half"].items():
        p(f"     {Ln:<24} N = {N:<8g}: {ea:.4e} vs {eh:.4e}  (ratio {eh/ea:.4f})")
    rows, flips = R["h12_case"]
    p("   H-SETTLE x H-12 (reading A): H-TRANSFER vs H-12-CARRIER + H-12-W (alpha_s, G or v: no state-dependent bound READ):")
    for r in rows:
        p(f"     {r['L']:<24} N = {r['N']:<8g}: eps > {r['eps_any_advantage']:.3e}  {r['H-TRANSFER']:<13} | {r['H-12-CARRIER']}")
    p(f"     cells that flip EXCLUDED -> NOT EXCLUDED: {flips}  (not evidence: an absent bound is not a measurement)")
    wg = R["window_given"]
    p("   M's rule BOTH ways (M-apply, V3 residual 3) -- the WAVE-4 RECORD on the unread statuses, kept as history (combine.py imports it);")
    p("   the same window on the READ (abstract) values is the last section (D68 wave 2).  Support 2 UNEVALUATED")
    p(f"     bound used: {wg['bound_used']} [{wg['bound_used_status'][:16]}]; OPEN, never checked: {wg['open_bounds']}")
    for r in wg["rows"]:
        t = r["tightening to close (context)"]
        p(f"     {r['L']:<5} N = {r['N']:<8g} {r['reading'][:1]}: eps_any {r['eps_any']:.4e} vs eps_max {r['eps_max']:.4e} -> "
          f"{r['support 1']}" + (f"; closing it needs a bound {t:.1f}x tighter (context, not evidence)" if t else ""))
    p("\nWAVE 3 -- FLOORS, ZERO ERROR, AND THE W2 CLASS WITHOUT H-QUBIT-DRIFT")
    for (name, D), sizes in R["zero_error"].items():
        p(f"   zero-error code sizes, {name}, D = {D}: block length 1..{len(sizes)}: {sizes}  -> zero-error rate "
          f"{max(math.log2(x) / (i + 1) for i, x in enumerate(sizes)):.3f} bits/pair")
    p("   => at D < 1 (and for nlcontrol's Z-channel even at D = 1) no finite number of pairs delivers 2 bits with certainty;")
    p("      every 'pairs per qubit' figure from N x C >= 2 is a FLOOR, and reliable transfer is block-coded (H-BLOCK).")
    ht = R["hermitian_tangent"]
    p(f"   H = i(v psi^+ - psi v^+): max non-hermiticity {ht['max_nonhermiticity']:.1e}, max |-iH psi - v| {ht['max_residual']:.1e} (50 random);"
      f" CONTROL v not orthogonal to psi: residual {ht['control_nonorthogonal_residual']:.3f}")
    w = R["w2_ancilla"]
    p(f"   W2 member on qubit + 2-qubit ancilla (4 axes, H-BORN-AT-BOB, H-C2, NOT H-QUBIT-DRIFT): chi = {w['chi_bits_per_pair']:.6f} bits/pair;"
      f" end fidelity {w['min_end_fidelity']:.12f}; curves disjoint as sets, min separation {w['min_curve_separation_rad']:.4f} rad"
      f" (grid step {w['grid_step_rad']:.4f}); max ||H|| T = {w['max_H_times_T']:.4f}")
    p("     Bob's P(b'|b): " + "; ".join("[" + ", ".join(f"{x:.6f}" for x in row) + "]" for row in w["P(b'|b)"]))
    p(f"     CONTROL, one fixed unitary for every branch (state-independent): chi = {R['w2_ancilla_linear_control']['chi_bits_per_pair']:.2e}")
    p("     wave 4 (w2_ancilla_flow_k): k axes, m-qubit ancilla, d = 2^(1+m): k, d, chi, pairs per teleported qubit, P(error), "
      "min separation / grid step, max ||H|| T")
    for r in R["w2_k"]:
        p(f"       k={r['k']:>2} d={r['d']:>2}: chi {r['chi_bits_per_pair']:.6f} (log2 d - 1 = {r['holevo_ceiling_log2_d'] - 1:.0f}), "
          f"{r['pairs_per_teleported_qubit']:.4f} pairs/qubit, P(err) {r['p_error']:.1e}, sep {r['min_curve_separation_rad']:.3f} / "
          f"{r['grid_step_rad']:.4f} rad, max||H||T {r['max_H_times_T']:.3f}")
    p(f"       CONTROL antipodal k=8: chi {R['w2_k_control_antipodal']['chi_bits_per_pair']:.4f}, sep "
      f"{R['w2_k_control_antipodal']['min_curve_separation_rad']:.1e}; CONTROL linear k=16: chi "
      f"{R['w2_k_control_linear']['chi_bits_per_pair']:.1e}")
    p("     => 2 bits per pair with ZERO error at finite T: 1 pair per teleported qubit for this member (smooth global field:")
    p("        H-EXTEND, derived, not computed).  The qubit-only floor (> 2, >= 3) is H-QUBIT-DRIFT's, not the class's.")
    p("        This shows what the CLASS admits; it is not evidence that such a drift exists.")
    p("\nD68 WAVE 2 (W2A-limits) -- THE WEINBERG-FAMILY LIMITS READ AT SOURCE, AND THE W2 x F1 WINDOW ON THE READ VALUES")
    p("   route: " + WEINBERG_ROUTE + " (journals.aps.org/prl/abstract/<doi>); abstract only, full text not read (paywall, not circumvented)")
    for k, d in R["weinberg_read"].items():
        p(f"   {k}: f = {d['f_Hz']:.4e} Hz ({d['f_status']})")
        p(f"       printed: {d['printed']}")
    bc = R["befrac_majumder_check"]
    p(f"   H-BEFRAC checked on Majumder's own pair: 2.0e-27 x B/A(201Hg) = 2.0e-27 x {bc['B/A_201Hg_eV']/1e6:.6f} MeV -> "
      f"{bc['f_from_frac_Hz']*1e6:.4f} uHz vs printed 3.8 uHz;  CONTROLS: whole-nucleus B -> {bc['CONTROL f with whole-nucleus B']:.3e} Hz, "
      f"nucleon rest energy -> {bc['CONTROL f with nucleon rest energy']:.3e} Hz")
    lo, hi = R["bollinger_range_Hz"]
    p(f"   Bollinger's one printed digit (3.5..4.5e-27) -> {lo*1e6:.2f}..{hi*1e6:.2f} uHz; Walsworth's exponent as printed at source (+20) "
      f"-> {R['walsworth_plus20_Hz']:.2e} Hz, contradicting its own 8.9 uHz (so -20)")
    p("   context only: Weinberg PRL 62 485 (1989) public abstract, 'limits of order 10^-21 on the fraction of the energy of the 9Be nucleus' (other normalisation)")
    p("   later restatements searched (none carries the numbers): " + "; ".join(WEINBERG_LATER))
    W = R["window_read"]
    p(f"   window per (L, N, H-MAP reading), tightest READ bound = {W['tightest']}; verdicts given {', '.join(W['hypotheses'])}:")
    for r in W["rows"]:
        t = r["per_bound"][r["bound_used"]]
        ctx = (f"closing needs a bound {t['tightening to close (context)']:.4g}x tighter" if t["tightening to close (context)"] else
               f"opening needs a bound {t['loosening to open (context)']:.4g}x looser")
        other = "" if r["robust_across_READ_bounds"] else ("  per bound: " + ", ".join(f"{k.split(',')[0]} {v['window']}" for k, v in r["per_bound"].items()))
        p(f"     {r['L']:<9} N = {r['N']:<8g} {r['reading'][0]}: eps_any {r['eps_any']:.4e} vs eps_max {r['eps_max']:.4e} -> window {r['window']:<5}"
          f" (robust over the four READ bounds: {r['robust_across_READ_bounds']}; {ctx}, context){other}")
    nopen = sum(r["window"] == "OPEN" for r in W["rows"])
    p(f"   => {nopen} of {len(W['rows'])} (cell, reading) windows OPEN, {len(W['rows']) - nopen} EMPTY, on READ values; no longer 'given W_W2'.")
    p("      An OPEN window is 'not excluded', never 'found': every limit is an upper limit measured consistent with zero.")
    p(f"   CONTROLS: bounds 1e7 tighter -> {sum(r['window'] == 'EMPTY' for r in R['window_read_control_tighter_1e7']['rows'])} EMPTY of 18; "
      f"1e3 looser -> {sum(r['window'] == 'OPEN' for r in R['window_read_control_looser_1e3']['rows'])} OPEN of 18")
    PD = R["proxima_distances"]
    p("   Proxima's distance (W2-fix): two READ values, both recorded; phase1's imported for every computation")
    p(f"     phase1.L_PROXIMA (Gaia DR3 768.066539 mas, READ via restatement, DOCKET 67): {PD['phase1 ly (1/parallax)']:.5f} ly")
    p(f"     Faria 2022 Table 1 p.2 (768.50 +- 0.20 mas, 1.3012 +- 0.0003 pc; ref. Gaia Collaboration 2016): "
      f"{PD['Faria ly (printed 1.3012 pc)']:.4f} +- {PD['Faria ly error (printed 0.0003 pc)']:.4f} ly (printed pc), "
      f"{PD['Faria ly (1/parallax 768.50)']:.4f} ly (1/parallax)")
    p(f"     discrepancy {100 * PD['relative difference (phase1 - Faria) / Faria, distance']:.3f} %; parallaxes differ by "
      f"{PD['parallax difference mas']:.3f} mas = {PD['sigma on Faria parallax error alone']:.2f} sigma on Faria's error alone "
      f"({PD['sigma on both parallax errors']:.2f} on both; {PD['sigma on Faria printed distance and its printed error']:.2f} against "
      f"Faria's printed, rounded 1.3012 +- 0.0003 pc); the Proxima windows are the same at either distance: "
      f"{PD['windows at Proxima unchanged at Faria distance']}")


# ======================================================================================= selftest
def selftest():
    R = build()
    checks = []
    ok = lambda name, cond, detail="": checks.append((name, bool(cond), detail))
    structural = lambda name, cond, detail="": checks.append(("STRUCTURAL (cannot fail; not evidence) " + name, bool(cond), detail))
    for e, (pr, ex) in R["nlcontrol_vs_law"].items():
        rerun = bob_numeric("x", e, 3.0, Y, n=3000) - bob_numeric("z", e, 3.0, Y, n=3000)
        ok(f"A1a nlcontrol's integrator (n=3000) reproduces its printed {pr}", round(rerun, 5) == pr, f"{rerun:.7f}")
        ok(f"A1b printed {pr} vs exact tanh(2*{e}*3) within the integrator's O(dt) error",
           abs(pr - ex) < 2e-5, f"exact {ex:.7f}, offset {pr - ex:+.1e}")
    L = R["law"]
    ok("A2 sympy: phi = 2 atan(tanh(eps t)) solves phi' = 2 eps cos phi", L["ode_residual_numeric"] < 1e-12)
    ok("A2 sympy: sin(phi) = tanh(2 eps t)", L["identity_residual_numeric"] < 1e-12)
    ok("A3 grid: integrator agrees with exact law", max(abs(n - x) for _, _, n, x in R["grid"]) < 2e-3)
    # encoding-drift guard: a wrong law must be caught by the same comparison
    wrong = max(abs(n - math.tanh(e * T)) for e, T, n, _ in R["grid"])
    ok("A4 CONTROL (must fail): wrong law tanh(eps T) disagrees with the integrator", wrong > 1e-2, f"{wrong:.3f}")
    ok("A5 CONTROL: linear H = eps Z gives zero signal", abs(R["linear_control"]) < 1e-12)
    rng = np.random.default_rng(3)
    worst = 0.0
    for _ in range(12):
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        v /= np.linalg.norm(v)
        e, T = rng.uniform(0.01, 0.4), rng.uniform(0.5, 4.0)
        num = bloch_of(NL.evolve(v, e, False, T=T, n=6000))
        ex = bloch_exact(bloch_of(v), e, T)
        worst = max(worst, max(abs(a - b) for a, b in zip(num, ex)))
    ok("A6 general closed form vs nlcontrol integrator, 12 random states", worst < 2e-3, f"{worst:.1e}")
    bb = R["best_basis"]
    ok("A7 best Alice axis is the x axis (|n_x| ~ 1) and equals tanh(2 eps T)",
       abs(abs(bb[1][0]) - 1) < 1e-3 and abs(bb[0] - math.tanh(0.6)) < 1e-9, f"{bb}")
    ok("A7 z and y axes give zero signal", max(abs(c) for c in ensemble_mean((0, 0, 1), .1, 3) + ensemble_mean((0, 1, 0), .1, 3)) < 1e-15)
    ys = [ensemble_mean((math.sin(t) * math.cos(f), math.sin(t) * math.sin(f), math.cos(t)), 0.1, 3.0)[1]
          for t in np.linspace(0, math.pi, 37) for f in np.linspace(0, 2 * math.pi, 73)]
    ok("A8 Bob's mean y >= 0 for every Alice axis (tanh u + tanh v = sinh(u+v)/(cosh u cosh v))", min(ys) >= -1e-15, f"min {min(ys):.1e}")
    m, (c, q), chi = R["info"][1e-3]
    ok("B1 small-D law I = D^2/(8 ln 2)", abs(m / (1e-6 / (8 * LN2)) - 1) < 1e-3)
    ok("B2 ceiling capacity(D=1) = log2(1.25) (Z-channel, crossover 1/2)", abs(R["CMAX"] - math.log2(1.25)) < 1e-9)
    ok("B3 Holevo(uniform) = measured MI (states commute)", all(abs(v[0] - v[2]) < 1e-12 for v in R["info"].values()))
    ok("B4 capacity >= uniform MI", all(v[1][0] >= v[0] - 1e-15 for v in R["info"].values()))
    ok("B5 N < 2/log2(1.25) = 6.21 pairs per qubit is impossible", eps_to_remove(LY_M, 6) is None and eps_to_remove(LY_M, 7) is not None)
    ok("C1 Walsworth abstract: h * 8.9 uHz = 3.68e-20 eV ~ printed 3.7e-20", abs(R["walsworth_check_eV"] / 3.7e-20 - 1) < 0.02)
    ok("C2 2411.09611 'nearly a factor of 50': computed 40.87 (wording discrepancy recorded)", abs(R["kr_ratio_quoted_nearly_50"] - 40.87) < 0.01)
    structural("C3 KR Lamb-shift figure: KR v2 (1e-4) and Brož's restatement (1e-2) DIFFER -- discrepancy kept (compares two typed READ values)",
       BOUNDS_KR["KR 2022 Lamb-shift estimate (as printed in KR v2)"][0] != BOUNDS_KR["KR Lamb-shift estimate (as restated by Brož)"][0])
    for lab, cnd in R["conditional"].items():
        ems = [v[0] for (Ln, N), v in cnd["removal"].items() if v[0] is not None and Ln == "1 AU"]
        ok(f"C4 removal eps decreases with more pairs ({lab})", all(a >= b for a, b in zip(ems, ems[1:])))
    C = R["collapse"]
    ok("D1 collapse: MC ensemble average matches the LINEAR Lindblad map for every initial state (< 5 sigma)",
       C["worst_mc_vs_lindblad_z"] < 5, f"{C['worst_mc_vs_lindblad_z']:.2f}")
    ok("D2 collapse: exact ensemble difference between Alice's choices = 0", C["exact_ensemble_difference"] < 1e-12)
    ok("D3 collapse: MC detector sees no signal (< 4 sigma)", C["mc_detector"][2] < 4, f"{C['mc_detector'][2]:.2f}")
    ok("D4 VACUITY GUARD: each trajectory moves nonlinearly (per-trajectory <|x|> > 0.5 for |0>, Lindblad |x| < 0.5)",
       C["per_state"]["0"]["mean_abs_x_per_trajectory"] > 0.5 and abs(C["per_state"]["0"]["lindblad"][0]) < 0.5)
    DC = R["drift_collapse"]
    ok("D5 CONTROL (must signal): drift + collapse noise, same detector, > 10 sigma", DC["detector"][2] > 10, f"{DC['detector'][2]:.1f}")
    # D6, wave 2.  Wave 1 first said: 'D6 CONTROL (must signal): pure deterministic drift, same detector' and fed the
    # detector a hand-typed (0, tanh 0.6, 0) -- a test of detector arithmetic, not of a drift (C-verify-0 #15).  Now
    # the drift is RUN through the same SDE code path with the collapse switched off (lambda = 0) and must reproduce
    # the exact law; a broken drift term would fail it.
    d6 = drift_plus_collapse(lam=0.0, N=200)
    ok("D6 CONTROL (must signal): pure drift run through sde_ensemble (lambda = 0) reproduces tanh(2 eps T) via the same detector",
       abs(d6["detector"][0] - d6["noise_free_tanh"]) < 5e-3 and d6["detector"][0] > 0.1,
       f"{d6['detector'][0]:.5f} vs {d6['noise_free_tanh']:.5f}")
    ok("E1 Z0 = 2 alpha h / e^2 equals CODATA Z0", abs(R["Z0"][0] / R["Z0"][1] - 1) < 1e-9, f"{R['Z0']}")
    structural("E2 twelve rows in H-12, four without an independent carrier (counts the table's own typed classification)",
               len(H12) == 12 and sum(r[4].startswith("NO") for r in H12) == 4)
    F = R["frame"]
    ok("F1 corridors: one corridor no loop; two frames close; one frame never", (not F["one_corridor_closed"]) and F["two_frames_closed"]
       and F["closed_one_frame"] == 0 and F["pairs_one_frame"] > 0)
    # ---- wave 2
    ok("G1 H-C2 named: under C1 the drift gives no signal (frame.settle_under_C1 < 1e-12)", R["c1_signal"] < 1e-12, f"{R['c1_signal']:.1e}")
    ta = R["two_axis"]
    ok("G2 second W2 Hamiltonian eps(<X>Z+<Z>X): integrator matches exact 2 tanh(2 eps T)", abs(ta["signal_eps0.1_T3"] - ta["exact"]) < 2e-3,
       f"{ta['signal_eps0.1_T3']:.6f} vs {ta['exact']:.6f}")
    ok("G3 its capacity exceeds nlcontrol's ceiling and approaches 1 bit per pair", ta["cap_D"][0.9] > CMAX and ta["cap_D"][0.999999] > 0.999,
       f"{ta['cap_D'][0.999999]:.6f}")
    ok("G4 Holevo at a one-qubit readout: max chi over 300 random ensembles <= 1 bit", ta["readout_holevo_max"] <= 1.0 + 1e-12,
       f"{ta['readout_holevo_max']:.6f}")
    mn, td = ta["finite_T_rank"]
    ok("G5 finite T: Bob's per-choice state has rank 2 and trace distance < 1 (ceiling not attained)", mn > 1e-6 and td < 1.0,
       f"min eig {mn:.2e}, td {td:.6f}")
    # Wave 3 (RV-0 #10): wave 2 first printed G6 as one 'CONTROL (must fail)'.  Its first half, 2 C < 2, is 1 - h2 < 1
    # for any D < 1 and cannot fail; it is now STRUCTURAL.  The second half (3 pairs reach 2 bits at eps = 0.3, T = 3)
    # carries content and stays a check.  G7 and G8 are identities of the bisection (eps_to_remove depends only on
    # eps * frac * L): the factor 2 and the distance-independence are ANALYTIC consequences of T = atanh(D_N)/(2 eps),
    # stated as such, not evidence.
    structural("G6a 2 pairs at finite T stay below 2 bits under the 1-bit qubit ceiling (2(1 - h2) < 2 for D < 1)",
               2 * capacity_bsc(math.tanh(2 * 0.3 * 3.0)) < 2.0)
    ok("G6b 3 pairs of the two-axis drift at eps = 0.3, T = 3 reach 2 bits (Shannon floor met; zero-error is not)",
       3 * capacity_bsc(math.tanh(2 * 0.3 * 3.0)) >= 2.0, f"{3 * capacity_bsc(math.tanh(1.8)):.4f}")
    ratios = [eh / ea for ea, eh in R["eps_any_vs_half"].values()]
    structural("G7 eps for any advantage is exactly half the T = L/2c figure (identity of the bisection)", all(abs(r - 2.0) < 1e-6 for r in ratios),
               f"{min(ratios):.6f}..{max(ratios):.6f}")
    Ts = [eps_to_remove(L, 7, frac=1.0) * L for L in (AU_M, LY_M, 4.24 * LY_M)]
    structural("G8 drift time distance-independent (eps_any x L constant; identity of the bisection)", max(Ts) / min(Ts) - 1 < 1e-6)
    tA = R["timing"][("A (eps = 2 pi f)", 7)]
    ok("G9 reading A, N = 7: T = 13.38 h; 1 ly read 0.99847 L/c early (C-verify-1 #3 reproduced)",
       abs(tA["T_h"] - 13.38) < 0.01 and abs(tA["early_fraction_1ly"] - 0.99847) < 1e-5, f"{tA['T_h']:.3f} h, {tA['early_fraction_1ly']:.6f}")
    ok("G10 first transit: midpoint source beats light launched from Alice at firing; one-end distribution does not",
       tA["first_transit_midpoint_1ly"]["beats_light_launched_at_firing"] and not tA["first_transit_one_end_1ly"]["beats_light_launched_at_firing"])
    ok("G11 CONTROL (must fail): midpoint source with T > L/2c does not beat light launched at firing",
       not first_transit_times(LY_M, 0.6 * LY_M / C_LIGHT, "midpoint")["beats_light_launched_at_firing"])
    rows, flips = R["h12_case"]
    au7 = [r for r in rows if r["L"] == "1 AU" and r["N"] == 7][0]
    # Wave 3 (RV-0 #10): wave 2 first printed G12 as one check.  Its 'NOT EXCLUDED with an unbounded carrier' half is
    # carrier_ok = (N x CMAX >= 2), true by construction for N = 7; it is STRUCTURAL.  The H-TRANSFER half compares
    # eps_any with the (NAMED-NOT-READ) Majumder figure and carries content.
    ok("G12a H-TRANSFER: 1 AU, N = 7 is EXCLUDED by the Majumder figure (unread in waves 1-4; READ (abstract) in D68 wave 2); 1 ly, N = 7 is not",
       au7["H-TRANSFER"] == "EXCLUDED" and [r for r in rows if r["L"] == "1 ly" and r["N"] == 7][0]["H-TRANSFER"] == "NOT EXCLUDED")
    structural("G12b with an unbounded carrier the 1 AU, N = 7 cell is NOT EXCLUDED (carrier_ok = N x CMAX >= 2)",
               au7["H-12-CARRIER"].startswith("NOT EXCLUDED") and flips >= 1, f"flips {flips}")
    zl = R["frw_lemma"]
    ok("G13 corridor O-LOOP keying forced in exact flat FRW, credited to the geometry (frame lemma unsat, vacuity sat, control sat)",
       zl["claim"] == "unsat" and zl["vacuity"] == "sat" and zl["control_a_ge_0"] == "sat")
    # ---- wave 3
    ze = R["zero_error"]
    ok("G14 zero-error capacity 0 at D < 1: one codeword at block lengths 1-3 (nlcontrol Z-channel and H2 BSC, D = 0.9, 0.999999)",
       all(ze[(nm, D)] == [1, 1, 1] for nm in ("nlcontrol Z-channel", "H2 BSC") for D in (0.9, 0.999999)))
    ok("G15 CONTROL (must fail the zero-capacity pattern): H2's BSC at D = 1 has 2^n zero-error words",
       ze[("H2 BSC", 1.0)] == [2, 4, 8], f"{ze[('H2 BSC', 1.0)]}")
    ok("G15b nlcontrol's Z-channel stays zero-error-0 even at D = 1 (both inputs give '+')", ze[("nlcontrol Z-channel", 1.0)] == [1, 1, 1])
    ht = R["hermitian_tangent"]
    ok("G16 H = i(v psi^+ - psi v^+) is Hermitian and generates v (50 random, C^8)",
       ht["max_nonhermiticity"] < 1e-12 and ht["max_residual"] < 1e-12, f"{ht['max_residual']:.1e}")
    ok("G17 CONTROL (must fail): v not orthogonal to psi is not generated", ht["control_nonorthogonal_residual"] > 1e-2,
       f"{ht['control_nonorthogonal_residual']:.3f}")
    w = R["w2_ancilla"]
    ok("G18 W2 member on qubit + 2-qubit ancilla: curves disjoint as sets (separation >> grid step) and the state-only field reaches the targets",
       w["min_curve_separation_rad"] > 20 * w["grid_step_rad"] and w["min_end_fidelity"] > 1 - 1e-6,
       f"sep {w['min_curve_separation_rad']:.4f} rad, fidelity {w['min_end_fidelity']:.10f}")
    ok("G19 ... and carries 2 bits per pair with zero error at finite T (chi = 2, P(b'|b) = identity)",
       abs(w["chi_bits_per_pair"] - 2.0) < 1e-6 and all(abs(w["P(b'|b)"][b][bb] - (b == bb)) < 1e-6 for b in range(4) for bb in range(4)),
       f"chi {w['chi_bits_per_pair']:.8f}")
    ok("G20 CONTROL (must fail to signal): one state-independent unitary for every branch gives chi = 0",
       abs(R["w2_ancilla_linear_control"]["chi_bits_per_pair"]) < 1e-9, f"{R['w2_ancilla_linear_control']['chi_bits_per_pair']:.1e}")
    wk = {r["k"]: r for r in R["w2_k"]}
    zero_err = lambda r: r["p_error"] < 1e-9 and r["min_end_fidelity"] > 1 - 1e-6 and r["min_curve_separation_rad"] > 10 * r["grid_step_rad"]
    ok("G21 (wave 4) k = 4 axes, 2-qubit ancilla, via w2_ancilla_flow_k: reproduces G19's 2 bits per pair, zero error",
       abs(wk[4]["chi_bits_per_pair"] - 2.0) < 1e-6 and zero_err(wk[4]), f"chi {wk[4]['chi_bits_per_pair']:.8f}")
    ok("G22 (wave 4) k = 8 axes, 3-qubit ancilla (d = 16): chi = 3 bits per pair, zero error -> 2/3 pair per teleported qubit",
       abs(wk[8]["chi_bits_per_pair"] - 3.0) < 1e-6 and zero_err(wk[8]),
       f"chi {wk[8]['chi_bits_per_pair']:.8f}, sep {wk[8]['min_curve_separation_rad']:.3f} vs step {wk[8]['grid_step_rad']:.4f}")
    ok("G23 (wave 4) k = 16 (d = 32): chi = 4, zero error -> 1/2 pair; k = 32 (d = 64): chi = 5 -> 0.4 pair (no positive floor in the computed range)",
       abs(wk[16]["chi_bits_per_pair"] - 4.0) < 1e-6 and zero_err(wk[16]) and abs(wk[32]["chi_bits_per_pair"] - 5.0) < 1e-6
       and zero_err(wk[32]), f"pairs/qubit {[round(wk[k]['pairs_per_teleported_qubit'], 4) for k in (4, 8, 16, 32)]}; "
                              f"separations {[round(wk[k]['min_curve_separation_rad'], 3) for k in (4, 8, 16, 32)]} rad")
    ap = R["w2_k_control_antipodal"]
    ok("G24 CONTROL (must fail): k = 8 with antipodal axes -- branch states coincide, curves collide, chi falls below log2 k",
       ap["chi_bits_per_pair"] < 3.0 - 0.5 and ap["min_curve_separation_rad"] < 1e-9 and ap["p_error"] > 0.1,
       f"chi {ap['chi_bits_per_pair']:.4f}, sep {ap['min_curve_separation_rad']:.1e}, P(error) {ap['p_error']:.3f}")
    ok("G25 CONTROL (must fail to signal): k = 16, one state-independent unitary gives chi = 0",
       abs(R["w2_k_control_linear"]["chi_bits_per_pair"]) < 1e-9, f"{R['w2_k_control_linear']['chi_bits_per_pair']:.1e}")
    # ---- M-apply (2026-10-03): V3 residual 3, M's rule both ways
    wg = R["window_given"]
    cell = lambda L, N, rd: [r for r in wg["rows"] if r["L"] == L and r["N"] == N and r["reading"].startswith(rd)][0]
    opened = [r for r in wg["rows"] if r["eps_any"] is not None and r["eps_any"] < r["eps_max"]]
    ok("G26 (M-apply) every OPEN window computed from the unread value is flagged ADMISSIBLE GIVEN W_W2, and every EMPTY "
       "one OPEN: no cell is settled in either direction",
       opened and all(r["support 1"].startswith("ADMISSIBLE GIVEN") for r in opened) and
       all(r["support 1"].startswith(("ADMISSIBLE GIVEN", "EMPTY GIVEN", "IMPOSSIBLE")) for r in wg["rows"]),
       f"{len(opened)} open-window cells of {len(wg['rows'])}")
    ok("G27 (M-apply) the GIVEN flag names the unread bound used (Majumder; Walsworth, also NAMED-NOT-READ, is not used) "
       "and the two OPEN, never checked (Bollinger, Chupp-Hoare)",
       wg["open_bounds"] == ["Bollinger+ 1989, 9Be+, PRL 63 1031", "Chupp & Hoare 1990, 21Ne, PRL 64 2261"] and
       wg["bound_used_status"].startswith("NAMED-NOT-READ"), f"unread {len(wg['unread_bounds'])}, OPEN {len(wg['open_bounds'])}")
    c1A, c1B = cell("1 ly", 7, "A"), cell("1 ly", 7, "B")
    c6A, c6B = cell("1 AU", 1e6, "A"), cell("1 AU", 1e6, "B")
    ok("G28 (M-apply) context, not evidence: closing 1 ly N = 7 needs a bound 655x (A) / 328x (B) tighter; 1 AU N = 1e6 "
       "only 7.2x / 3.6x (V3 reproduced)",
       abs(c1A["tightening to close (context)"] - 655) < 2 and abs(c1B["tightening to close (context)"] - 328) < 1.5 and
       abs(c6A["tightening to close (context)"] - 7.16) < 0.05 and abs(c6B["tightening to close (context)"] - 3.58) < 0.05,
       f"{c1A['tightening to close (context)']:.1f} / {c1B['tightening to close (context)']:.1f}; "
       f"{c6A['tightening to close (context)']:.2f} / {c6B['tightening to close (context)']:.2f}")
    ok("G29 CONTROL (must change): with the bound marked READ and nothing OPEN, the GIVEN flag disappears",
       all(not r["support 1"].endswith("(flagged, not settled)") and "GIVEN" not in r["support 1"]
           for r in R["window_given_control_read"]["rows"]))
    structural("G30 support 2 carries no window: UNEVALUATED on every row", all(r["support 2"].startswith("UNEVALUATED")
                                                                            for r in wg["rows"]))
    # ---- D68 wave 2 (W2A-limits): the Weinberg-family limits READ (abstract) at source
    bc = R["befrac_majumder_check"]
    ok("G31 (W2A) H-BEFRAC on Majumder's own pair: 2.0e-27 x B/A(201Hg, AME2020) / h reproduces the printed 3.8 uHz within "
       "the 2.0's rounding (2.5%)", abs(bc["f_from_frac_Hz"] / 3.8e-6 - 1) < 0.025, f"{bc['f_from_frac_Hz']*1e6:.4f} uHz")
    ok("G32 CONTROL (must fail): the same fraction of the whole-nucleus binding, or of the nucleon rest energy, misses 3.8 uHz "
       "by > 50x", bc["CONTROL f with whole-nucleus B"] / 3.8e-6 > 50 and bc["CONTROL f with nucleon rest energy"] / 3.8e-6 > 50,
       f"{bc['CONTROL f with whole-nucleus B']/3.8e-6:.0f}x, {bc['CONTROL f with nucleon rest energy']/3.8e-6:.0f}x")
    ok("G33 CONTROL (must fail): Walsworth's eV exponent as printed AT SOURCE (+20) contradicts its own 8.9 uHz (> 1e30 x); "
       "the -20 reading agrees (C1)", R["walsworth_plus20_Hz"] / 8.9e-6 > 1e30 and abs(R["walsworth_check_eV"] / 3.7e-20 - 1) < 0.02,
       f"{R['walsworth_plus20_Hz']:.2e} Hz")
    fW = {k: d["f_Hz"] for k, d in BOUNDS_WEINBERG.items()}
    lo, hi = R["bollinger_range_Hz"]
    ok("G34 (W2A) Majumder is the tightest of the four READ bounds, and stays so over Bollinger's printed digit (3.5..4.5e-27)",
       min(fW, key=fW.get).startswith("Majumder") and lo > 3.8e-6,
       "; ".join(f"{k.split(',')[0]} {v*1e6:.2f}" for k, v in fW.items()) + f" uHz; Bollinger {lo*1e6:.2f}..{hi*1e6:.2f}")
    WR = R["window_read"]
    rw = lambda L, N, rd: [r for r in WR["rows"] if r["L"] == L and r["N"] == N and r["reading"].startswith(rd)][0]
    empty = {(r["L"], r["N"]) for r in WR["rows"] if r["window"] == "EMPTY"}
    ok("G35 (W2A) window on READ values: EMPTY exactly at 1 AU, N = 7 and 1 AU, N = 1e3 (both readings); OPEN at the other 7 cells "
       "(1 AU N = 1e6; every 1 ly and 4.2465 ly cell)",
       empty == {("1 AU", 7), ("1 AU", 1000)} and all(rw(L, N, rd)["window"] == "EMPTY" for L, N in empty for rd in "AB")
       and sum(r["window"] == "OPEN" for r in WR["rows"]) == 14,
       f"{sum(r['window'] == 'OPEN' for r in WR['rows'])} OPEN of {len(WR['rows'])}")
    nr = [(r["L"], r["N"], r["reading"][0]) for r in WR["rows"] if not r["robust_across_READ_bounds"]]
    ok("G36 (W2A) exactly one window depends on WHICH READ bound applies (H-SAME-EPS): 1 AU, N = 1e3, reading A -- EMPTY on "
       "Majumder, OPEN on Chupp-Hoare alone", nr == [("1 AU", 1000, "A")] and
       rw("1 AU", 1000, "A")["per_bound"]["Chupp & Hoare 1990, 21Ne, PRL 64 2261"]["window"] == "OPEN", f"{nr}")
    ok("G37 CONTROL (must change): every bound 1e7x tighter empties all 18 windows; 1e3x looser opens all 18",
       all(r["window"] == "EMPTY" for r in R["window_read_control_tighter_1e7"]["rows"]) and
       all(r["window"] == "OPEN" for r in R["window_read_control_looser_1e3"]["rows"]))
    ok("G38 (W2A) G28's context factors reproduced on READ values (1 ly N = 7: 655x / 328x; 1 AU N = 1e6: 7.16x / 3.58x)",
       abs(rw("1 ly", 7, "A")["per_bound"][WR["tightest"]]["tightening to close (context)"] - 655) < 2 and
       abs(rw("1 AU", 1e6, "B")["per_bound"][WR["tightest"]]["tightening to close (context)"] - 3.58) < 0.05)
    structural("G39 every READ-value verdict names H-MAP and H-TRANSFER and none says 'GIVEN W_W2' or 'NAMED-NOT-READ'; every "
               "bound's status is READ (abstract) (label checks)",
               all("H-MAP" in r["verdict"] and "H-TRANSFER" in r["verdict"] and "W_W2" not in r["verdict"] for r in WR["rows"])
               and all(d["status"].startswith("READ (abstract)") for d in BOUNDS_WEINBERG.values()))
    # ---- W2-fix (2026-10-04, verifier W2V-1 problem 3): Proxima's distance, two READ values, phase1's imported
    PD = R["proxima_distances"]
    ok("G40 (W2-fix) the Proxima cell is phase1.L_PROXIMA (imported, not typed) and Faria 2022's READ parallax reproduces its "
       "own printed 1.3012 pc to the printed digit",
       WINDOW_READ_L[2][1] is L_PROXIMA_PHASE1 and PD["phase1 equals L_PROXIMA"]
       and abs(PD["Faria pc from its own parallax"] - 1.3012) < 0.00005,
       f"phase1 {PD['phase1 ly (1/parallax)']:.5f} ly; Faria 1/768.50 = {PD['Faria pc from its own parallax']:.5f} pc")
    ok("G41 CONTROL (must fail): the two READ values are NOT the same distance -- phase1's parallax does not reproduce Faria's "
       "1.3012 pc within Faria's printed +-0.0003 pc; the parallaxes differ by > 2 sigma on Faria's error alone",
       abs(PD["phase1 pc"] - 1.3012) > 0.0003 and PD['sigma on Faria parallax error alone'] > 2.0,
       f"phase1 {PD['phase1 pc']:.5f} pc; {PD['sigma on Faria parallax error alone']:.2f} sigma; "
       f"{100 * PD['relative difference (phase1 - Faria) / Faria, distance']:.3f} %")
    ok("G42 (W2-fix) the discrepancy moves no window: all six (N, reading) windows at Proxima are the same at Faria's distance",
       PD['windows at Proxima unchanged at Faria distance'], f"{PD['windows (phase1)']}")
    w = max(len(n) for n, _, _ in checks)
    for n, good, det in checks:
        print(f"  [{'PASS' if good else 'FAIL'}] {n:<{w}} {det}")
    bad = [n for n, g, _ in checks if not g]
    nstr = sum(n.startswith("STRUCTURAL") for n, _, _ in checks)
    nctl = sum("CONTROL" in n and not n.startswith("STRUCTURAL") for n, _, _ in checks)
    ncount = len(checks) - nstr
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks pass ({nstr} printed STRUCTURAL, not evidence; {nctl} controls); "
          f"counted (STRUCTURAL excluded): {ncount - sum(1 for n in bad if not n.startswith('STRUCTURAL'))}/{ncount}")
    return 0 if not bad else 1


def to_jsonable(o):
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, float) and math.isinf(o):
        return "inf"
    return o


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    R = build()
    report(R)
    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        with open(path, "w") as fh:
            json.dump(to_jsonable(R), fh, indent=1)
