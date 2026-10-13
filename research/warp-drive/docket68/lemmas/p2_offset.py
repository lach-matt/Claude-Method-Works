#!/usr/bin/env python3
"""p2_offset.py -- item 322: "what is 139 (1)'s plane's offset? - We need to read about the vacuum decay boundary and
the confirmed mass of the higgs boson 125.09GeV".  The one question b5a_residue A2 left with M -- position 2's offset
for 139 (1)'s plane, B5a holding if and only if it exceeds -sigma/4 - delta sigma_1/2 = -3.7e52 J/m^3 -- worked from
the readings M named and from what the record already fixes.  Worked in the conversation (READ where marked; computed
with sympy and a stdlib integrator, exact where marked; deduced where marked; estimates labelled; not verified by a
separate session; not seated); 2026-10-12.

  V0 (read) The words this rests on, verbatim in the rulings file: M's item 322; 201, "Our universe is defined by its
     plane's tension and its dark-energy offset"; 226, "its plane's tension and offset among them"; 139 (1)'s "+4/3 and
     -1/3 of the one-plane value"; 136 (2), "activates the higgs field forming the mass defined in the README"; the R5
     answer, "Yes, a trigger" (H-ACTIVATION-IS-TRIGGER: the Higgs field's value unchanged); 117, "An NEC is never
     violated"; 275, "Coincident everywhere"; 276, "The passage is one-way in all aspects"; 320, "no bulk is ever
     empty"; and the C4 verifier's at 310 (not M's): "the junction fixes position 2's side total S1 + 2 S2, not tau".
  V1 (READ) The Higgs mass.  ATLAS and CMS, Run 1 combined (arXiv:1503.07589, eq. (3)): "m_H = 125.09 +- 0.24 GeV =
     125.09 +- 0.21 (stat.) +- 0.11 (syst.) GeV" -- M's figure, and the input Andreassen, Frost and Schwartz used.
  V2 (READ) The vacuum decay boundary.  In the Standard Model the Higgs quartic lambda runs negative at high field, so
     the electroweak vacuum is either the lowest (stable), a false vacuum outliving the universe (metastable), or one
     that should already have decayed (unstable); the boundaries are lines in the (m_t, m_h) plane.
     - Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio and Strumia (arXiv:1307.3536): "the measured value of M_h is
       near-critical, in the sense that it places the EW vacuum right at the border between absolute stability and
       metastability"; stability needs "M_t < (171.53 +- 0.42) GeV" (eq. (66), at M_h = 125.15, alpha_3 = 0.1184);
       lambda(M_Pl) = -0.0143 - 0.0066 (M_t/GeV - 173.34) + ... (eq. (61e)); lambda crosses zero "at a scale of about
       10^10 GeV"; the bounce action S = 8 pi^2/(3 |lambda|) and the decay probability in our past light cone p0 = 0.15
       Lambda_B^4/H0^4 e^-S (eqs. (81), (83)).
     - Andreassen, Frost and Schwartz (arXiv:1707.08124), with m_h = 125.09: absolute stability needs m_t^pole <
       171.18 + 0.12 (m_h - 125.09)/0.24 + 0.43 (alpha_s - 0.1181)/0.0011 GeV, theory +0.17 -0.35 (eq. (6.30)); the
       metastability window "171.18 < m_t^pole/GeV < 177.68" (eq. (6.29)); lambda's minimum -0.0138 at 3.11e17 GeV, S
       = 1900, and the lifetime "10^161 years" (95 %: more than 10^65).
     - PDG 2024 (Phys. Rev. D 110, 030001): top mass from direct measurements "172.57 +- 0.29 OUR AVERAGE", "usually
       interpreted as the pole mass, but the theoretical uncertainty in this interpretation is hard to quantify"; pole
       mass from cross-sections "172.4 +- 0.7 OUR AVERAGE"; alpha_s(m_Z^2) = 0.1180 +- 0.0009.
     - Froggatt and Nielsen (hep-ph/9511371): two degenerate minima, one at the Planck scale -- the critical line
       itself -- "leads to the top mass being 173 +- 5 GeV and the Higgs mass 135 +- 9 GeV".
  V3 (computed; the running READ from Buttazzo et al.'s appendix B, their weak-scale values eqs. (55), (57)-(60)) The
     couplings run at three loops (the gauge couplings' four-loop QCD term kept; the bottom and tau Yukawas left out).
     At Buttazzo et al.'s own inputs the run returns their eq. (61) to the fourth digit -- lambda(M_Pl) = -0.01436
     against -0.0143 -- and at two loops it does not (-0.0151), a control.  At M's 125.09 GeV with PDG's 172.57 GeV and
     0.1180: the running quartic crosses zero at 3.7e10 GeV (MS-bar, scheme-dependent; Buttazzo et al.'s
     gauge-invariant barrier scale is about half), reaches -0.0109 at 3.4e17 GeV and is -0.0106 at M_Pl -- metastable.
     The boundary at M's mass is m_t = 171.14 GeV (AFS (6.30) at 0.1180, READ); the running quartic's own zero line is
     170.88 GeV (computed; AFS note that line lies below the full boundary).  So our vacuum sits 1.4 GeV of top mass
     above the decay boundary (1.43 against the direct average, 1.26 against the cross-section pole mass) and 5.1 GeV
     below the instability line.  The bounce estimate S = 8 pi^2/(3 |lambda_min|) = 2412 gives p0 ~ 10^-812 (an
     estimate: the tree bounce, no fluctuation determinants; AFS's complete figure at m_t = 173.1 is 10^-606).
  V4 (computed) What the Higgs mass fixes about vacuum energy.  It fixes differences between the potential's own
     points: the electroweak vacuum lies m_h^2 v^2/8 = (104.35 GeV)^4 = 2.47e45 J/m^3 below the symmetric point (tree
     level, v = 246.22 GeV), 54.7 orders above our offset, 5.25e-10 J/m^3 (201) -- so no offset is the Higgs potential's
     value: it is the total after a cancellation the Standard Model does not compute (the cosmological-constant problem,
     standard, not READ).  Beyond the barrier the potential falls below ours, to lambda M^4/4 = -9.6e70 GeV^4 = -2.0e108
     J/m^3 at the reduced Planck mass (RG-improved tree level, the field's anomalous dimension left out; an estimate);
     with lambda < 0 all the way, the Standard Model has no second minimum below M_Pl, and where one lies is physics
     beyond it.  B5a's bound in the same units is -(6.49 TeV)^4: above the electroweak scale, far below the instability
     scale.
  V5 (computed, exact; deduced where marked) What the record fixes.  At the coincidence the two sides share one induced
     metric (275; 310's note), each with its own Gauss equation (b5a_residue A3): H^2 = (kappa^2 Sigma^-/6)^2 - k1^2 +
     C1/a^4 and H^2 = (kappa^2 Sigma^+/6)^2 - k2^2 + C2/a^4, k1 = kappa^2 sigma/6 and k2 = kappa^2 sigma/12 (the flat
     static planes of 139 (1)'s background), with our side ours alone, Sigma^- = S1, and position 2's side the total the
     junction fixes, Sigma^+ = S1 + 2 S2 (276, the board's reading (a); b5a_residue A1).  An offset enters as tension
     does (S = -delta sigma h, b5a_residue A2).  With the sheets' vacuum parts alone, C2 - C1 = a^4 (kappa^2/6)^2 B, B =
     sigma (d1 - 2 x) - 4 x (d1 + x), d1 = our offset and x = position 2's (computed, exact, from A3's formula). B is
     constant and the mass parameters of a vacuum bulk are constants (Bowcock, Charmousis and Gregory, READ in A3), so as
     a grows B = 0.  The bulk is never empty (320), and its content does not change this, because offsets are constants
     and the matter on the sheets dilutes.  A vacuum energy has Sigma + Pi = 0, so the Codazzi identity gives it no flux
     (A3, computed); our matter is conserved (276), so C1 stays constant; and for a null-dust carrier A3's own pair
     relation makes the flux position 2's bulk must carry proportional to H a^4 Q, Q = 4 B at late times -- a flux
     growing as a^4 without end, which drives C2 negative (a negative-mass bulk, against 139 (2)'s "positive", the
     board's reading) if B < 0 and breaks the null condition in position 2's bulk (Q > 0, against 117) if B > 0
     (deduced).  For a scalar carrier (A3), a constant part of its stress at the sheet is a bulk vacuum energy, which
     enters as offset (V6).  So B = 0: 4 x^2 + (4 d1 + 2 sigma) x - sigma d1 = 0, two roots (computed, exact): x+ = d1/2
     - 3 d1^2/(2 sigma) + ... = 2.625e-10 J/m^3, half ours; x- = -sigma/2 - 3 d1/2 + ... = -7.41e52 J/m^3. x- turns
     position 2's side total negative (tension part -sigma/2 - 2 d1): every ray crossing on its side would gather
     negative null energy, against 117, and it does not vanish with our offset, so it is not an offset of 139 (1)'s
     background but a different one.  So x+ (deduced).  [Item 323: M ordered the assumptions proved.  The one-way split,
     Sigma^- = S1 and Sigma^+ = S1 + 2 S2, is proved from 276 (p2_assume Q2), the curvatures k1 and k2 from 201, 202 and
     226 (Q3), the summed reading excluded by 276 (Q4); B = 0 rests on pointwise P4 and 120/137 (Q5), the appeal to 139
     (2) and to Q > 0 kept as corroboration.]  On position 2's side the effective coupling follows the side's tension,
     sigma/2, so the side total d1 + 2 x+ = 2 d1 at half the coupling gives the one H (computed).
     [Item 339 (the B5a verifier's note outside B5a): "our matter is conserved (276), so C1 stays constant" omits the
     bulk's normal stress at our sheet -- with no flux C1 is constant only if our bulk's T_nn vanishes there, which 320
     makes a limit (p2_assume's item-339 note); the verifier found no effect on x+. The Gauss pair here uses one
     five-dimensional coupling, which holds for 139 (1)'s plane as derived (339 (Q5)); A1's side total needs none
     (b5a_residue A6). And x+ = 2.625e-10 J/m^3 is the quadratic's root to 1.9e-69 J/m^3, d1/2 - 3 d1^2/(2 sigma) + ...
     its truncated series (339 (Q7)).]
  V6 (deduced) The answer.  139 (1)'s plane's offset is x+ = 2.625e-10 J/m^3 (d1/2 to one part in 10^62), positive,
     position 2's own vacuum energy (226) fixed by ours through the one induced metric -- a de Sitter offset of (1.88
     meV)^4 against our (2.24 meV)^4.  B5a holds: A2's bound, -3.7e52 J/m^3, is negative and 62 orders larger in size.
     Position 2's bulk vacuum, were it to differ from the background's, would shift k2 and enter here as offset, so x+
     counts position 2's plane's offset together with any such shift (deduced).  [Item 324: with the one constant
     relativity leaves the five-dimensional bulk, the Gauss-Bonnet coupling alpha, x+ = (d1/2)(1 - 4 alpha k1^2 + ...),
     positive for every alpha with a bulk vacuum and a positive Newton constant (relativity U4); d1/2 is its value at
     alpha = 0.]  [Item 325: alpha = 0 exactly (gb_alpha.py B2-B3, on 201's B6'), so x+ above is exact as stated, with
     no Gauss-Bonnet factor.]  [Item 326: alpha = 0 also from relativity alone (gb_cone.py C7), without 201.]
     [Item 332 (gb_cone C10 (Q1)): under M-ONE-LIGHT-CONE (328) -- U6 alone does not reach curved backgrounds.]
  V7 (computed; deduced) The readings M named, against V5.
     (a) Position 2's plane in the Higgs potential's deeper vacuum (across the decay boundary): its offset would lie at
         or below -2.0e108 J/m^3 if the Standard Model holds to the Planck scale -- no root of B = 0, and far below
         B5a's bound.  It survives only if that vacuum is degenerate with ours to (1.88 meV)^4, i.e. exactly on the
         decay boundary, Froggatt and Nielsen's multiple point; at M's 125.09 GeV that needs m_t^pole = 171.14 GeV
         (+0.17 -0.35), against the measured 172.57 +- 0.29 (direct) and 172.4 +- 0.7 (pole) -- an observable the
         reading would predict.  The record excludes it on its own terms: 136 (2) has position 2's Higgs field "forming
         the mass defined in the README" with its value unchanged (R5), and the same potential's vacuum at the Planck
         scale sets masses some 10^16 times ours (M_Pl/v, reduced); a position 2 whose couplings differ enough to undo
         that has a potential of its own, not ours across the boundary, and its offset is V6's (deduced).
     (b) The symmetric point (the Higgs not yet activated): +2.47e45 J/m^3 over ours -- no root of B = 0, and against
         R5's field value already set.
     (c) Position 2's plane as the decay boundary itself, a bubble wall: a scalar's wall carries tension integral
         sqrt(2 (V - V_false)) dphi > 0, never negative (standard), and a wall in our three dimensions is a surface
         (J/m^2), not a plane of the bulk (J/m^3), so 139 (1)'s negative plane is no Higgs wall (deduced).
     (d) What the Higgs mass does give: our vacuum is metastable, 1.4 GeV of top mass from the boundary, lifetime far
         beyond any age; position 2's offset is positive and above any deeper Higgs vacuum, so its plane sits on our
         side of the decay boundary.  If its laws are ours (202), it is a false vacuum of the same potential; if not,
         its offset is still x+.  The Higgs readings place it; they do not compute it.
  V8 (the cypher NOT-RUN, stated) The offset is a root of an equation the record fixes (V5), not a choice among
     configurations; V7's readings are each tested against that equation by computation.  An index of (reading,
     is-a-root, keeps 117, keeps R5) rows would carry the answer as its own column, a key (211), as tau_share T6 and
     pointwise P9 found.  Not run, and said.

What this does not claim.
  - That the Standard Model holds to the Planck scale: V3 and V4 take it so, as the READ sources do; new physics can
    stabilize or destabilize the potential (AFS), which moves V7 (a)'s depth and none of V5-V6.
  - A value of our offset: d1 is 201's, the measured dark-energy density, taken as given.
  - Readings other than 276's (a): under a summed reading (no one-way) only d1 + x is fixed by our expansion, and x
    alone is not; 276 rules the one-way reading, and A1's side total is the verifier's (310).
  - The lifetime as more than an estimate: p0 here is the tree bounce; the complete figure is AFS's.

Imports b5a_residue.py and p2_gravity.py by path.  Stdlib + sympy.  python3 p2_offset.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("what is 139 (1)'s plane's offset? - We need to read about the vacuum decay boundary and the confirmed mass of "
         "the higgs boson 125.09GeV", "Our universe is defined by its plane's tension and its dark-energy offset",
         "its plane's tension and offset among them", "+4/3 and -1/3 of the one-plane value",
         "activates the higgs field forming the mass", "Yes, a trigger", "An NEC is never violated",
         "Coincident everywhere", "The passage is one-way in all aspects", "no bulk is ever empty",
         "the junction fixes position 2's side total S1 + 2 S2, not tau")
READ = dict(mh=125.09, mh_stat=0.21, mh_syst=0.11, mh_tot=0.24,                 # arXiv:1503.07589 eq. (3)
            mt_direct=172.57, mt_direct_err=0.29, mt_pole=172.4, mt_pole_err=0.7,  # PDG 2024
            alphas=0.1180, alphas_err=0.0009,                                    # PDG 2024 eq. (9.25)
            b61=dict(g1=0.6154, g2=0.5055, g3=0.4873, yt=0.3825, lam=-0.0143),   # Buttazzo et al. eq. (61)
            afs=dict(mh=125.09, mt=173.1, alphas=0.1181, lam_min=-0.0138, mu_min=3.11e17, S=1900,
                     window=(171.18, 177.68), log10_p0=-606, H0=1.44e-42),      # arXiv:1707.08124 (6.19)-(6.29)
            v=246.21971)                                                         # Buttazzo et al. table 2
MPL = 1.2209e19                                     # GeV; Buttazzo et al.'s "M_Pl ~ 1.2e19 GeV"
MPL_RED = MPL / math.sqrt(8 * math.pi)
GEV4 = 1.602176634e-10 / (1.973269804e-16) ** 3    # J/m^3 per GeV^4 / (hbar c)^3, standard
OFFSET = 5.25e-10                                   # J/m^3, 201 (rho_Lambda c^2)
L1 = 1 / (16 * math.pi ** 2)


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def beta(y, loops=3):
    """Buttazzo et al. appendix B: d/d ln mu^2 of (g1^2, g2^2, g3^2, yt^2, lambda), g1 in SU(5) normalisation"""
    a, b, c, t, l = y
    top = 3 if not MUT.get("top_sign") else -3              # the mutant: the top loop's sign reversed
    d1 = a * a * L1 * 41 / 10
    d2 = b * b * L1 * -19 / 6
    d3 = c * c * L1 * -7
    dt = t * L1 * (9 * t / 2 - 8 * c - 9 * b / 4 - 17 * a / 20)
    dl = L1 * (l * (12 * l + 6 * t - 9 * b / 2 - 9 * a / 10) - top * t * t + 9 * b * b / 16 + 27 * a * a / 400
               + 9 * b * a / 40)
    if loops >= 2:
        L2 = L1 ** 2
        d1 += a * a * L2 * (44 * c / 5 + 27 * b / 10 + 199 * a / 50 - 17 * t / 10)
        d2 += b * b * L2 * (12 * c + 35 * b / 6 + 9 * a / 10 - 3 * t / 2)
        d3 += c * c * L2 * (-26 * c + 9 * b / 2 + 11 * a / 10 - 2 * t)
        dt += t * L2 * (t * (-12 * t - 12 * l + 36 * c + 225 * b / 16 + 393 * a / 80) + 6 * l * l - 108 * c * c
                        - 23 * b * b / 4 + 1187 * a * a / 600 + 9 * c * b + 19 * c * a / 15 - 9 * b * a / 20)
        dl += L2 * (l * l * (-156 * l - 72 * t + 54 * b + 54 * a / 5)
                    + l * t * (-3 * t / 2 + 40 * c + 45 * b / 4 + 17 * a / 4)
                    + l * (-73 * b * b / 16 + 1887 * a * a / 400 + 117 * b * a / 40)
                    + t * t * (15 * t - 16 * c - 4 * a / 5) + t * (-9 * b * b / 8 - 171 * a * a / 200 + 63 * b * a / 20)
                    + 305 * b ** 3 / 32 - 3411 * a ** 3 / 4000 - 289 * b * b * a / 160 - 1677 * b * a * a / 800)
    if loops >= 3:
        L3 = L1 ** 3
        d1 += a * a * L3 * (t * (189 * t / 16 - 29 * c / 5 - 471 * b / 32 - 2827 * a / 800)
                            + l * (-9 * l / 5 + 9 * b / 10 + 27 * a / 50) + 297 * c * c / 5 + 789 * b * b / 64
                            - 388613 * a * a / 24000 - 3 * c * b / 5 - 137 * c * a / 75 + 123 * b * a / 160)
        d2 += b * b * L3 * (t * (147 * t / 16 - 7 * c - 729 * b / 32 - 593 * a / 160)
                            + l * (-3 * l + 3 * b / 2 + 3 * a / 10) + 81 * c * c + 324953 * b * b / 1728
                            - 5597 * a * a / 1600 + 39 * c * b - c * a / 5 + 873 * b * a / 160)
        d3 += c * c * L3 * (t * (15 * t - 40 * c - 93 * b / 8 - 101 * a / 40) + 65 * c * c / 2 + 109 * b * b / 8
                            - 523 * a * a / 120 + 21 * c * b + 77 * c * a / 15 - 3 * b * a / 40) \
            + c ** 5 * L1 ** 4 * -2472.28
        dt += t * L3 * (t * t * (58.6028 * t + 198 * l - 157 * c - 1593 * b / 16 - 2437 * a / 80)
                        + l * t * (15 * l / 4 + 16 * c - 135 * b / 2 - 127 * a / 10)
                        + t * (363.764 * c * c + 16.990 * b * b - 24.422 * a * a + 48.370 * c * b + 18.074 * c * a
                               + 34.829 * b * a) + l * l * (-36 * l + 45 * b + 9 * a)
                        + l * (-171 * b * b / 16 - 1089 * a * a / 400 + 117 * b * a / 40)
                        - 619.35 * c ** 3 + 169.829 * b ** 3 + 16.099 * a ** 3 + 73.654 * c * c * b
                        - 15.096 * c * c * a - 21.072 * c * b * b - 22.319 * c * a * a - 321 / 20 * c * b * a
                        - 4.743 * b * b * a - 4.442 * b * a * a)
        dl += L3 * (l ** 3 * (6011.35 * l + 873 * t - 387.452 * b - 77.490 * a)
                    + l * l * t * (1768.26 * t + 160.77 * c - 359.539 * b - 63.869 * a)
                    + l * l * (-790.28 * b * b - 185.532 * a * a - 316.64 * b * a)
                    + l * t * t * (-223.382 * t - 662.866 * c - 5.470 * b - 21.015 * a)
                    + l * t * (356.968 * c * c - 319.664 * b * b - 74.8599 * a * a + 15.1443 * c * b
                               + 17.454 * c * a + 5.615 * b * a)
                    + l * b * b * (-57.144 * c + 865.483 * b + 79.638 * a)
                    + l * a * a * (-8.381 * c + 61.753 * b + 28.168 * a)
                    + t ** 3 * (-243.149 * t + 250.494 * c + 74.138 * b + 33.930 * a)
                    + t * t * (-50.201 * c * c + 15.884 * b * b + 15.948 * a * a + 13.349 * c * b + 17.570 * c * a
                               - 70.356 * b * a)
                    + t * c * (16.464 * b * b + 1.016 * a * a + 11.386 * b * a) + t * b * b * (62.500 * b + 13.041 * a)
                    + t * a * a * (10.627 * b + 11.117 * a)
                    + c * (7.536 * b ** 3 + 0.663 * a ** 3 + 1.507 * b * b * a + 1.105 * b * a * a)
                    - 114.091 * b ** 4 - 1.508 * a ** 4 - 37.889 * b ** 3 * a + 6.500 * b * b * a * a
                    - 1.543 * b * a ** 3)
    return [d1, d2, d3, dt, dl]


def start(mh, mt, a3, mw=80.384):
    """Buttazzo et al. eqs. (55), (57)-(60): MS-bar couplings at mu = M_t"""
    lam = 0.12604 + 0.00206 * (mh - 125.15) - 0.00004 * (mt - 173.34)
    if MUT.get("tree_matching"):
        lam = 0.12917                                       # the mutant: the tree-level quartic (their table 3)
    yt = 0.93690 + 0.00556 * (mt - 173.34) - 0.00042 * (a3 - 0.1184) / 0.0007
    g2 = 0.64779 + 0.00004 * (mt - 173.34) + 0.00011 * (mw - 80.384) / 0.014
    gy = 0.35830 + 0.00011 * (mt - 173.34) - 0.00020 * (mw - 80.384) / 0.014
    g3 = 1.1666 + 0.00314 * (a3 - 0.1184) / 0.0007 - 0.00046 * (mt - 173.34)
    return [5 / 3 * gy ** 2, g2 ** 2, g3 ** 2, yt ** 2, lam]


def run(mh, mt, a3, mu_end=MPL, loops=None, n=3000):
    """fourth-order Runge-Kutta in ln mu^2 from M_t; returns the end point and lambda along the way"""
    loops = loops or (2 if MUT.get("two_loop") else 3)    # the mutant: the three-loop terms dropped
    y = start(mh, mt, a3)
    t0, t1 = 2 * math.log(mt), 2 * math.log(mu_end)
    h = (t1 - t0) / n
    path, t = [], t0
    for _ in range(n):
        path.append((math.exp(t / 2), y[4]))
        k1 = beta(y, loops)
        k2 = beta([u + h / 2 * k for u, k in zip(y, k1)], loops)
        k3 = beta([u + h / 2 * k for u, k in zip(y, k2)], loops)
        k4 = beta([u + h * k for u, k in zip(y, k3)], loops)
        y = [u + h / 6 * (p + 2 * q + 2 * r + s) for u, p, q, r, s in zip(y, k1, k2, k3, k4)]
        t += h
        if abs(y[4]) > 4 * math.pi or max(y[:4]) > 16 * math.pi ** 2:
            break                                           # non-perturbative: the run stops where the theory does
    path.append((math.exp(t / 2), y[4]))
    return y, path


def quartic(mh, mt, a3, loops=None):
    y, path = run(mh, mt, a3, loops=loops)
    neg = [m for m, l in path if l < 0]
    mu_min, lam_min = min(path, key=lambda p: p[1])
    return dict(end=dict(g1=math.sqrt(y[0]), g2=math.sqrt(y[1]), g3=math.sqrt(y[2]), yt=math.sqrt(y[3]), lam=y[4]),
                cross=neg[0] if neg else None, lam_min=lam_min, mu_min=mu_min,
                lam_red=min(path, key=lambda p: abs(math.log(p[0] / MPL_RED)))[1])


def zero_line(mh, a3):
    """the top mass at which the running quartic's minimum below M_Pl touches zero (bisection)"""
    lo, hi = 168.0, 175.0
    for _ in range(30):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if quartic(mh, mid, a3)["lam_min"] < 0 else (mid, hi)
    return (lo + hi) / 2


def higgs():
    """V1-V4: the fixture, M's mass, the boundary, the energies"""
    fx = quartic(125.15, 173.34, 0.1184)
    fx2 = quartic(125.15, 173.34, 0.1184, loops=2)
    afs = READ["afs"]
    fa = quartic(afs["mh"], afs["mt"], afs["alphas"])
    mh, mt, a3 = READ["mh"], READ["mt_direct"], READ["alphas"]
    ours = quartic(mh, mt, a3)
    bound = 171.18 + 0.12 * (mh - 125.09) / 0.24 + 0.43 * (a3 - 0.1181) / 0.0011        # AFS (6.30)
    line = zero_line(mh, a3)
    S = 8 * math.pi ** 2 / (3 * abs(ours["lam_min"]))
    S_afs = 8 * math.pi ** 2 / (3 * abs(afs["lam_min"]))
    log10_p0 = math.log10(0.15) + 4 * math.log10(ours["mu_min"] / afs["H0"]) - S / math.log(10)
    v = READ["v"]
    k = 4 if MUT.get("ew_depth_factor") else 8              # the mutant: m_h^2 v^2/4
    ew = mh ** 2 * v ** 2 / k                               # GeV^4, tree level
    deep = ours["lam_red"] * MPL_RED ** 4 / 4               # GeV^4, RG-improved tree level at the reduced Planck mass
    return dict(fx=fx, fx2=fx2, fa=fa, ours=ours, bound=bound, line=line, gap_direct=mt - bound,
                gap_pole=READ["mt_pole"] - bound, below_unstable=afs["window"][1] - mt, S=S, S_afs=S_afs,
                log10_p0=log10_p0, mh_tot=math.hypot(READ["mh_stat"], READ["mh_syst"]),
                ew=ew, ew_root=ew ** 0.25, ew_SI=ew * GEV4, deep_SI=deep * GEV4, orders=math.log10(ew * GEV4 / OFFSET))


def geometry():
    """V5-V6: the one induced metric's two Gauss equations with the sheets' vacuum parts; B = 0 and its roots"""
    BR = _load(os.path.join(HERE, "b5a_residue.py"), "p2o_b5a")
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "p2o_pg")
    kap, sig, a, H = sp.symbols("kappa sigma a H", positive=True)
    r1, p1, r2, p2 = sp.symbols("rho1 p1 rho2 p2", real=True)
    d1, x = sp.symbols("d1 x", real=True)
    k1, k2 = kap ** 2 * sig / 6, kap ** 2 * sig / 12
    w2 = 1 if MUT.get("side_once") else 2                  # the mutant: position 2's plane counted once on its side
    Sm, Sp = sig + d1, sig / 2 + d1 + w2 * x
    c = (kap ** 2 / 6) ** 2
    gap = sp.expand((c * Sm ** 2 - k1 ** 2) - (c * Sp ** 2 - k2 ** 2))       # (C2 - C1)/a^4
    B = sp.expand(gap / c)
    formula = sp.expand(sig * (d1 - 2 * x) - 4 * x * (d1 + x))
    from_A3 = sp.simplify(B - formula) == 0                # A3's C2 - C1 formula with rho -> offsets
    Qa3 = BR.a3()["Q"]
    Qv = sp.expand(Qa3.subs({p1: -r1, p2: -r2}).subs({r1: d1, r2: x}))
    q_is_4B = sp.simplify(Qv - 4 * formula) == 0           # A3's Q for vacuum parts is 4 B
    roots = sp.solve(sp.Eq(B, 0), x)
    eps = sp.Symbol("epsilon", positive=True)
    ser = [sp.series(r.subs(d1, eps * d1), eps, 0, 3).removeO().subs(eps, 1) for r in roots]
    plus = [r for r, s in zip(roots, ser) if sp.simplify(s.subs(d1, 0)) == 0]
    minus = [r for r, s in zip(roots, ser) if sp.simplify(s.subs(d1, 0)) != 0]
    xp, xm = (minus[0], plus[0]) if MUT.get("branch_minus") else (plus[0], minus[0])   # the mutant: the other root
    sp_plus = sp.series(xp.subs(d1, eps * d1), eps, 0, 3).removeO().subs(eps, 1)
    side_tension = lambda r: sp.simplify((sig / 2 + d1 + w2 * r).subs(d1, 0))       # the side's tension part
    sigma_SI = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    d1v = -OFFSET if MUT.get("offset_sign") else OFFSET   # the mutant: our offset read negative
    num = lambda r: float(sp.N(r.subs({sig: sp.Rational(sigma_SI), d1: sp.Rational(d1v)}), 150))  # 1e-63 apart
    xp_SI, xm_SI = num(xp), num(xm)
    bound_SI = -sigma_SI / 4 - d1v / 2                     # b5a_residue A2's strictest reading
    one_H = sp.simplify(sp.expand((Sm ** 2 - sig ** 2) - (Sp ** 2 - sig ** 2 / 4)).subs(x, d1 / 2)
                        .subs(d1, eps * d1).series(eps, 0, 2).removeO()) == 0  # first order: 2 d1 at half the coupling
    return dict(from_A3=from_A3, q_is_4B=q_is_4B, roots=roots, plus_series=sp.expand(sp_plus), xp_SI=xp_SI, xm_SI=xm_SI,
                xp_side=side_tension(xp), xm_side=side_tension(xm), sigma_SI=sigma_SI, bound_SI=bound_SI,
                b5a_plus=xp_SI > bound_SI, b5a_minus=xm_SI > bound_SI, one_H=one_H,
                xp_root=(xp_SI / GEV4) ** 0.25 * 1e12 if xp_SI > 0 else None, d1_root=(OFFSET / GEV4) ** 0.25 * 1e12,
                bound_root=(-bound_SI / GEV4) ** 0.25 / 1e3)


def readings(g, h):
    """V7: each candidate vacuum against B = 0 and B5a"""
    tol = abs(g["xp_SI"]) * 1e-6
    deep, sym = h["deep_SI"], OFFSET + h["ew_SI"]
    is_root = lambda val: abs(val - g["xp_SI"]) <= tol or abs(val - g["xm_SI"]) <= abs(g["xm_SI"]) * 1e-6
    crit = g["xp_SI"] - OFFSET                              # the degeneracy the deep reading would need, J/m^3
    return dict(deep_root=is_root(deep), deep_b5a=deep > g["bound_SI"], sym_root=is_root(sym), crit=crit,
                crit_root=(abs(crit) / GEV4) ** 0.25 * 1e12, mass_ratio=MPL_RED / READ["v"])


def compute():
    h = higgs()
    g = geometry()
    return dict(h=h, g=g, r=readings(g, h))


def report(o):
    h, g, r = o["h"], o["g"], o["r"]
    print("p2_offset.py -- 139 (1)'s plane's offset (item 322)\n")
    print("V1 m_H = 125.09 GeV; stat (+) syst = %.3f against the quoted total 0.24" % h["mh_tot"])
    f = h["fx"]["end"]
    print("V3 fixture (125.15, 173.34, 0.1184) at M_Pl: g1 %.4f g2 %.4f g3 %.4f yt %.4f lambda %.5f (eq. (61): 0.6154 "
          "0.5055 0.4873 0.3825 -0.0143); two loops: lambda %.5f" % (f["g1"], f["g2"], f["g3"], f["yt"], f["lam"],
                                                                    h["fx2"]["end"]["lam"]))
    print("   AFS inputs: lambda_min %.4f at %.3g GeV (AFS: -0.0138 at 3.11e17); 8 pi^2/(3 |lambda*|) = %.0f (AFS: 1900)"
          % (h["fa"]["lam_min"], h["fa"]["mu_min"], h["S_afs"]))
    u = h["ours"]
    print("   M's 125.09 with 172.57, 0.1180: lambda = 0 at %.3g GeV, minimum %.4f at %.3g GeV, %.4f at M_Pl" % (
        u["cross"], u["lam_min"], u["mu_min"], u["end"]["lam"]))
    print("   boundary (AFS (6.30)) %.2f GeV; running-quartic zero line %.2f GeV; measured above it by %.2f (direct), "
          "%.2f (pole); below the instability line by %.2f" % (h["bound"], h["line"], h["gap_direct"], h["gap_pole"],
                                                             h["below_unstable"]))
    print("   bounce estimate S = %.0f, log10 p0 = %.0f (estimate)" % (h["S"], h["log10_p0"]))
    print("V4 EW depth m_h^2 v^2/8 = (%.2f GeV)^4 = %.3g J/m^3, %.1f orders above our offset; V at the reduced Planck "
          "mass %.2g J/m^3" % (h["ew_root"], h["ew_SI"], h["orders"], h["deep_SI"]))
    print("V5 B from A3's formula: %s; A3's Q = 4 B for vacuum parts: %s; roots %s" % (g["from_A3"], g["q_is_4B"],
                                                                                    g["roots"]))
    print("   x+ series %s; x+ = %.4g J/m^3, x- = %.4g J/m^3; side tension part at d1 = 0: x+ %s, x- %s; one H at "
          "first order: %s" % (g["plus_series"], g["xp_SI"], g["xm_SI"], g["xp_side"], g["xm_side"], g["one_H"]))
    print("V6 x+ = (%.3f meV)^4 against ours (%.3f meV)^4; B5a's bound %.3g J/m^3 = -(%.2f TeV)^4: x+ above %s, x- "
          "above %s" % (g["xp_root"] or 0, g["d1_root"], g["bound_SI"], g["bound_root"], g["b5a_plus"],
                        g["b5a_minus"]))
    print("V7 deeper vacuum a root %s, above B5a's bound %s; symmetric point a root %s; degeneracy needed (%.2f meV)^4;"
          " M_Pl/v = %.2g" % (r["deep_root"], r["deep_b5a"], r["sym_root"], r["crit_root"], r["mass_ratio"]))


def checks(o):
    h, g, r = o["h"], o["g"], o["r"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("V0 item 322, 201, 226, 139 (1), 136 (2), R5, 117, 275, 276, 320 and 310's note verbatim in the rulings file",
        all(w in rul for w in WORDS))
    add("V1 the Higgs mass: stat and syst in quadrature give the quoted 0.24", abs(h["mh_tot"] - 0.24) < 0.005)
    b, f = READ["b61"], h["fx"]["end"]
    add("V3 the running at three loops returns Buttazzo et al.'s eq. (61); two loops does not (control)",
        all(abs(f[k] - b[k]) < 0.001 for k in ("g1", "g2", "g3", "yt")) and abs(f["lam"] - b["lam"]) < 0.0005
        and abs(h["fx2"]["end"]["lam"] - b["lam"]) > 0.0005)
    add("V3 AFS's own inputs: lambda's minimum within 0.0005 and its scale within a factor 2; S = 8 pi^2/(3|lambda|) "
        "within 1 % of 1900", abs(h["fa"]["lam_min"] - READ["afs"]["lam_min"]) < 0.0005
        and 0.5 < h["fa"]["mu_min"] / READ["afs"]["mu_min"] < 2 and abs(h["S_afs"] / 1900 - 1) < 0.01)
    u = h["ours"]
    add("V3 at 125.09 GeV: lambda turns negative between 1e10 and 1e11 GeV and stays negative to M_Pl -- metastable, "
        "the measured top above the boundary and below the instability line", u["cross"] and 1e10 < u["cross"] < 1e11
        and u["end"]["lam"] < 0 and h["gap_direct"] > 0 and h["below_unstable"] > 0 and h["line"] < h["bound"])
    add("V4 the electroweak depth m_h^2 v^2/8 = (104.35 GeV)^4 = 2.47e45 J/m^3, 54.7 orders above our offset",
        abs(h["ew_root"] - 104.35) < 0.01 and abs(h["ew_SI"] / 2.47e45 - 1) < 0.01 and abs(h["orders"] - 54.7) < 0.05)
    add("V5 B from A3's two Gauss equations is A3's formula with offsets; A3's Q for vacuum parts is 4 B",
        g["from_A3"] and g["q_is_4B"])
    d1_, sg = sp.Symbol("d1", real=True), sp.Symbol("sigma", positive=True)
    add("V5 roots: x+ = d1/2 - 3 d1^2/(2 sigma) + ..., positive; x- turns position 2's side tension part to -sigma/2",
        sp.simplify(g["plus_series"] - (d1_ / 2 - 3 * d1_ ** 2 / (2 * sg))) == 0
        and g["xp_SI"] > 0 and g["xm_side"] == -sg / 2 and g["xp_side"] == sg / 2 and g["one_H"])
    add("V6 x+ = 2.625e-10 J/m^3, (1.88 meV)^4; B5a holds at x+ and fails at x-", abs(g["xp_SI"] / 2.625e-10 - 1) < 1e-9
        and abs((g["xp_root"] or 0) - 1.88) < 0.01 and g["b5a_plus"] and not g["b5a_minus"])
    add("V7 the deeper vacuum and the symmetric point are no roots; the deeper vacuum falls below B5a's bound",
        not r["deep_root"] and not r["sym_root"] and not r["deep_b5a"] and r["crit_root"] < 2.0)
    return res


MUTANTS = {"two_loop": "the running at two loops, not three (V3)",
           "tree_matching": "the quartic at M_t taken at tree level (V3)",
           "top_sign": "the top loop in lambda's running with its sign reversed (V3)",
           "ew_depth_factor": "the electroweak depth read as m_h^2 v^2/4 (V4)",
           "side_once": "position 2's plane counted once on its side (V5)",
           "branch_minus": "the other root taken (V5, V6)",
           "offset_sign": "our offset read negative (V6)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
