#!/usr/bin/env python3
"""b1_matter.py -- four lemmas of the Warp Theorem re-based off input F2 (the matter-free plane), which M's item 184
rules out: "There are no matter free planes".  Input F2 itself is not greened; it stays ruled out, and the lemmas that
rested on it are re-done with each plane carrying its own universe's matter and the corridor adding none (184 with
129 (1), 130 (1)):
  B1'   edits B1   the FRW plane with its matter meets Gauss and Codazzi exactly when ...   PROVED, green
  B2'   edits B2   a local vacuum bulk off such a plane, unique among analytic ones          PROVED, green
  Z3    split      Z3'a away from the corridor, through today: DERIVED, green (a part only);
                   Z3'b rays meeting or beside the corridor: OPEN;  Z3'c the future, sparse regions: NATURE
  B5    split      B5'a the composite's positivity, as a conditional: DERIVED, green (a part only);
                   B5'p position 2's matter meets its antecedent: OPEN;  B5'b a smooth wall with matter: OPEN
So Z3 and B5 do NOT go green; B1 does; of B2, B2' does and its corridor-carrying instance B2t (F1-AUDIT.md's lemma, on
M1, carried here) does not.  Computed, READ and deduced; the build was checked by two separate AI sessions in this project
(one to refute, one for overclaim -- not an outside review) and their findings are applied here; the applied version is
not re-checked; not seated; 2026-10-09.  Note: lemmas/B1-MATTER.md.

CLI:  --selftest  (every check, each able to fail; about 25 s, most of it the bulk series in y)
      --mutants   (every named mutation of every check, each shown to make its check FAIL; exit 1 if any passes)
      --json PATH (writes compute(): every row labelled)

LABELS.  Every result row carries one of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  M's words are quoted verbatim, typing kept, from M-RULINGS-2026-10-03.md; guard G1 checks
each quote inside M's own spans of that item (after "M, verbatim:" or "M chose:", up to "Recorded as given"), never the
board's title or narrative.  The board's readings are named H-... and kept apart from them.  A lemma is GREEN only if its
status is PROVED, DERIVED or AXIOM and no input it rests on is non-green (OPEN, READING or NATURE).

M'S WORDS USED (verbatim, typing kept; M_WORDS below):
  129 (1), 130 (1) (excerpt), 184, 183 (choice), 187 (3) (choice), 117 and 120 (excerpts), 127 (1), 139 (1)-(2),
  141 (excerpt), 138 (excerpt), 196.
THE SEATED CLAUSE (Z) is the board's wording, which M seated by choosing "Seat both" (187 (3)): it is the criterion
  these lemmas are measured against (STRUCTURAL), never an input to them -- 187 says "The lemmas under (G) and (Z) keep
  their own statuses".  The AXIOM content is M's 117/120 ("An NEC is never violated") with 183's choice.

THE BOARD'S READINGS (named; withdrawn if M says otherwise):
  H-OUR-PLANE-IS-FRW   our plane, with its observed matter, is the homogeneous isotropic plane Planck fits (base LCDM,
           flat: READ Omega_K = 0.001 +- 0.002), and a Z2 Randall-Sundrum brane over a vacuum bulk; the board's model of
           "this current universe" (129 (1)).  B1' does not rest on it (an instance, A8); observation cannot tell it
           from four-dimensional gravity, the brane terms being ~1e-61 of the rest (A8).
  H-DE-IN-TAU          dark energy at w = -1 is carried in the plane's matter tau (p = -rho), leaving the plane at the
           Randall-Sundrum tension; SMS p.3 (READ) calls the split ambiguous, and check A7 shows both splits give the same
           four-dimensional equation exactly, so nothing rests on it.
  H-P2-AS-OURS         the board's example of position 2's matter: a universe whose matter measures as ours (138's
           words), used only to exhibit one configuration meeting B5'a's antecedent; not a claim about position 2.
  H-EXPANSION-IN-SURFACE  our plane's expansion a(t) is its surface's own movement (141's words).  The plane sits at
           y = 0 in the Gaussian-normal chart built on it -- STRUCTURAL, true of every hypersurface by construction of
           that chart, so it cannot by itself support reading 141's "static".  In AdS5's static chart an FRW plane is a
           moving surface (standard-not-READ).  It conflicts with BULK-BALANCE.md's H-STATIC-SCALE (141 read as
           R = const); neither reading is M's, and no lemma here rests on either.
  H-CYPHER-MATTER-INDEX  how this run's questions are encoded as indices for tools/cypher.py (196).  The encoding is the
           board's; every roster in cypher.py is run, none chosen; NOT-RUN is never counted as silent.
  WITHDRAWN in verification: H-NET-OVER-COMPONENTS (summing cosmological components under (Z)'s "net along each light
  ray").  It stretched 183, whose "net" concerns a negative member paired along the same rays, and it is not needed:
  the null energy condition is a condition on the total stress-energy (standard-not-READ), which check C3 computes
  directly, all components at one point.

WHAT IS COMPUTED HERE
  B1' (A1-A8).  Plane: FRW, q = -dt^2 + a(t)^2 (spatial curvature k_c), carrying a perfect fluid (rho, p).  Israel with
     Z2, SMS eq. (16) (READ p.3): K^t_t = -(kappa^2/6)(lambda - 2 rho - 3 p), K^i_i = -(kappa^2/6)(lambda + rho) (A1).
     Codazzi, SMS eq. (2)/(10) (READ p.2), vacuum bulk: D_nu K^nu_t - d_t K = (kappa^2/2)(rho' + 3H(rho + p)) =
     -(kappa^2/2) D_nu tau^nu_t, zero iff the fluid is conserved (SMS eq. (21), READ p.4); a non-conserved control
     fails (A2).  Gauss, R(4) = 2 Lambda5 + K^2 - K.K (localbulk.py's form): holds identically, for every rho, p, k_c,
     lambda, Lambda5 and every constant C, on the plane obeying H^2 = Lambda4/3 + kappa^4 lambda rho/18 + kappa^4 rho^2/36
     - k_c/a^2 + C/a^4, Lambda4 = (Lambda5 + kappa^4 lambda^2/6)/2 (SMS eq. (18), READ p.3); conversely Gauss with
     Codazzi gives d/dt[a^4(H^2 + k_c/a^2 - Lambda4/3 - kappa^4 lambda rho/18 - kappa^4 rho^2/36)] = (a^3 a'/3) x (Gauss
     residual), so the Friedmann equation with a dark-radiation constant C is the first integral (A3).  The trace of
     SMS eq. (17) equals the Gauss constraint for EVERY symmetric tau (generic tau, 10 entries); SMS (28) follows from
     (20); on FRW, E^mu_nu is traceless, proportional to C, zero iff C = 0 (A4).  The matter-free plane is the limit
     rho, p -> 0: the right side becomes localbulk.gauss_rhs(-kappa^2 lambda/6, Lambda5), imported by path, zero at the
     RS tension, H = 0, R(4) = 0 -- B1 exactly (A5).  Each side its own ell (no Z2): per-side Gauss and Codazzi hold;
     Israel's jump gives a conserved fluid; matter-free, lambda = (3/kappa^2)(1/ell_+ + 1/ell_-) (A6).  Dark energy as
     tension or as tau (A7).  The instance (H-OUR-PLANE-IS-FRW, not an input): Planck's H0 and Omega_m (cosmo.py,
     imported) give eps = rho/lambda_RS = Omega (H0 ell/c)^2/2 at the table-top ell; A8 prints eps_total (all of tau,
     under H-DE-IN-TAU) and eps_matter (A8).
  B2' (B1-B4).  READ: Dahia-Romero gr-qc/0109076v2 Lemma 1 (constraint propagation, PDF pp.8-9), the Cauchy-Kowalewski
     theorem as stated there (PDF p.10), Lemma 2 and Theorem 2 (PDF p.12): analytic (g, Omega) with their (39) [Codazzi]
     and (40) [Gauss] give a unique analytic Einstein space (Gaussian normal gauge).  Computed on the FRW model plane with
     dust (w = 0), C symbolic, expanded in y to order 6: the evolution residuals vanish through y^4 and the two
     constraints (yy, ty) through y^5; the observed-LCDM model plane (dust + w = -1) to order 4, the same (B1).
     Uniqueness at each order is STRUCTURAL: in Gaussian-normal gauge the evolution equations are already solved for the
     second y-derivatives (Kovalevskaya normal form), so the per-order determinants (9a^2, ...) carry no data and cannot
     fail; CK and Dahia-Romero (READ) carry uniqueness.  Controls that fail -- analytic data with matter that violate
     Gauss or Codazzi: doubled matter in K, the GR Friedmann equation with SMS's Israel data, a non-conserved fluid --
     each leaves an order-0 constraint residual (B2).  C = 0 exactly: a = a0 [cosh(y/ell) - (1 + ell sigma) sinh(y/ell)],
     n = cosh(y/ell) - (1 + ell sigma - 3 ell sum (1+w_i) sigma_i) sinh(y/ell), sigma = kappa^2 rho/6: every component of
     G + Lambda5 g vanishes, it equals the series through order 6, and all 55 bivector-pair components of R_abcd +
     (g_ac g_bd - g_ad g_bc)/ell^2 vanish (13 not identically zero under the ansatz): pure AdS5 (B3).  The dust plane
     explicit, analytic for t > 0 (B4).  F1 (eq. (17) on the plane) is not used.
  Z3'a, Z3'b, Z3'c (C1-C3, C5).  The bulk: R(k,k) = 0 wherever the bulk is the model's vacuum (axioms.py's derive_z3,
     imported; it evaluates (2 Lambda/3) g(k,k) for a null k, so it says nothing about a region carrying stress) (C1).
     The plane: S(k,k) = (lambda + rho) k_y^2 + (rho + p)|k_space|^2 for a 5D null k (C2).  Observed (READ Planck 2018,
     DESI DR2): the total null stress of the matter every fit measures, all components at one point, is positive at
     every epoch a in [1e-4, 1]; dark energy by itself is NOT shown to obey the NEC; in the future (a in (1, 100]) it
     stays positive in six fits and turns negative in the two constant-phantom fits, at a_x = [Omega_m/(|1+w|(1 -
     Omega_m))]^(1/(3|w|)) (closed form, deduced; grid, computed) -- so Z3'c is nature's; a uniform phantom dark energy
     would also outweigh matter locally wherever matter falls below a computed fraction of its mean (C3).  Beside the
     corridor: a flat plane held at fixed scale (H = 0 and H' = 0) beside positive dark radiation C has rho < 0, and its
     5D null stress is negative for some null k on either branch (rho + p < 0 on the branch near the RS tension,
     lambda + rho < 0 on the other) (C5; BULK-BALANCE.md's sign, recovered).
  B5'a, B5'p, B5'b (C4).  At coincidence (127) the summed tension +lambda_RS (b5_positive.py's B5a, imported) with both
     universes' matter: (lambda_RS + rho_1 + rho_2) k_y^2 + sum (rho + p)|k_space|^2, non-negative iff rho_1 + rho_2 >=
     -lambda_RS and sum (rho + p) >= 0 -- the conditional B5'a; with position 2's matter measuring as ours (H-P2-AS-OURS,
     an example) both hold; position 2's plane alone is negative for crossing rays; a thickening with one shared profile
     keeps it at every depth, a per-component one with phantom dark energy does not (control).  These thickenings are
     algebra, not Einstein solutions: the smooth wall with matter (B5'b) is OPEN.
  THE COUNT (G2, deduced from the live cypher audit's lemma list): the chain's own lemmas green, before and after these
     edits, under the audit's rule (DEFINITION counted green) and under the strict rule (PROVED, DERIVED, AXIOM only).
  THE CYPHER (196; H-CYPHER-MATTER-INDEX).  tools/cypher.py imported by path, every roster run.  Q1: plane states
     (sigma, C) with the bulk's coefficients (A3, N3) and the order-0 Gauss residual; Q2: the READ fits through today with
     the dark-energy and net null-stress signs, and the same fits in the future.  The binaries are computed by
     determined() (b6p_scale.py's, imported by path) on the board's encoding -- the board's stand-in for logic as the
     mechanism (register 1173); Q1's law binaries restate Part B (A3, N3 are polynomials in (sigma, C) by construction),
     and only the controls flip them.  Stated plainly: the measured languages (order, algebra, geometry, information,
     statistics) return E > 0 and disagree on every index, so tools/cypher.py itself separated no law from its control;
     documentary is silent by construction; roster 20.2's four unmapped names stay NOT-RUN.
Imports by path (never copied): bulk/localbulk.py (gauss_rhs only), lemmas/axioms.py (derive_z3), lemmas/b5_positive.py
(b5a, b5b), lemmas/b6p_scale.py (determined), ../cosmo.py (H0, OMEGA_M), copy/exactE.py (C_SI, G_SI),
lemmas/b4d_stage2.py (TABLETOP), tools/cypher.py; warptheorem.py (LEMMAS, read only for an informational cross-check of
the count's statuses).  Stdlib + sympy.  python3 b1_matter.py [--selftest] [--mutants] [--json PATH]
"""
import argparse
import contextlib
import importlib.util
import io
import itertools
import json
import math
import os
import re
import sys
import time as _wall
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
REPO = os.path.dirname(os.path.dirname(WD))
CYPHER_PATH = os.path.join(REPO, "tools", "cypher.py")
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")

LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
STATUSES = ("PROVED", "DERIVED", "AXIOM", "DEFINITION", "READING", "NATURE", "OPEN")
GREEN = ("PROVED", "DERIVED", "AXIOM")
GREEN_INPUT = GREEN + ("READ", "computed")

# ------------------------------------------------------------------------------------------------ M's words (verbatim)
M_WORDS = {
    "129 (1)": "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because "
               "the corridor is a bridge, so it adds nothing to either position.",
    "130 (1) (excerpt)": "1 - i - no added matter. And in my model a black hole is not matter, it is what the mouth at "
                         "position 1 looks like.",
    "184": "There are no matter free planes",
    "183 (choice)": "Yes: never violated as a pair",
    "187 (3) (choice)": "(3) \"Seat both\"",
    "117 (excerpt)": "An NEC is never violated",
    "120 (excerpt)": "it was an methaphor to describe that the NEC only ever appears to break, but never does",
    "127 (1)": "1 - yes",
    "139 (1)-(2)": "1 - yes 2 - positive, and you have to prove it.",
    "141 (excerpt)": "If planes are constantly in motion around each other, a stable throat cannot form. I suggest the "
                     "planes are static, but their surfaces contain their own movements from within their own contained "
                     "dimensions",
    "138 (excerpt)": "That is not to say there aren't 118 completely different ones in another universe that measure "
                     "exactly as are ours do.",
    "196": "Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher",
}
# The seated clause (Z): the BOARD's wording in its question of item 187 (3), which M seated by choosing "Seat both".
# It is the criterion the lemmas are measured against (STRUCTURAL), never an input; G1 checks it inside 187's question.
SEATED_WORDING = {
    "187 (3) (Z), the board's wording M seated": "(Z) \\\"null energy never violated\\\" holds net along each light ray (183)",
}

# ------------------------------------------------------------------------------------------------ READ at source
# Verbatim from each PDF's text layer (math linearised as the text layer gives it); page = PDF page.
READS = {
    "SMS_codazzi": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 2,
                    "and the Codacci equation, D_nu K^nu_mu - D_mu K = (5)R_rho sigma n^sigma q^rho_mu, (2)"),
    "SMS_10": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 2,
               "From the Codacci equation (2) and the 5-dimensional Einstein equations (6), we find D_nu K^nu_mu - D_mu K "
               "= kappa_5^2 T_rho sigma n^sigma q^rho_mu. (10)"),
    "SMS_13_14": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "T_mu nu = -Lambda g_mu nu + S_mu nu delta(chi), (13) where S_mu nu = -lambda q_mu nu + tau_mu nu, (14) "
                  "with tau_mu nu n^nu = 0. Lambda is the cosmological constant of the bulk spacetime. lambda and tau_mu "
                  "nu are the vacuum energy and the energy-momentum tensor, respectively, in the brane world."),
    "SMS_split": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "It should be noted that the decomposition of S_mu nu into lambda q_mu nu and tau_mu nu can be "
                  "ambiguous, particularly in cosmological contexts."),
    "SMS_16": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
               "Now we impose the Z2-symmetry on this spacetime, with the brane as the fixed point. Interestingly the "
               "symmetry uniquely determines the extrinsic curvature of the brane in terms of the energy momentum "
               "tensor, K+_mu nu = -K-_mu nu = -1/2 kappa_5^2 (S_mu nu - 1/3 q_mu nu S). (16)"),
    "SMS_17_20": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                  "(4)G_mu nu = -Lambda_4 q_mu nu + 8 pi G_N tau_mu nu + kappa_5^4 pi_mu nu - E_mu nu, (17) where "
                  "Lambda_4 = 1/2 kappa_5^2 (Lambda + 1/6 kappa_5^2 lambda^2), (18) G_N = kappa_5^4 lambda / 48 pi, (19) "
                  "pi_mu nu = -1/4 tau_mu alpha tau^alpha_nu + 1/12 tau tau_mu nu + 1/8 q_mu nu tau_alpha beta tau^alpha "
                  "beta - 1/24 q_mu nu tau^2, (20)"),
    "SMS_sign": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 3,
                 "Furthermore, we would have the wrong sign of G_N if lambda < 0"),
    "SMS_21": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 4,
               "Together with Eq. (16), Eq. (10) implies the conservation law for the matter, D_nu K^nu_mu - D_mu K "
               "proportional to D_nu tau^nu_mu = 0. (21)"),
    "SMS_28_30": ("Shiromizu, Maeda, Sasaki, gr-qc/9910076v3", 5,
                  "tau_mu nu = rho t_mu t_nu + P h_mu nu, (27) ... pi_mu nu = 1/12 rho (rho t_mu t_nu + (rho + 2P) h_mu "
                  "nu). (28) ... This means d_i rho = 0. Hence an inhomogeneous perfect fluid is rejected."),
    "DR_lemma1": ("Dahia, Romero, gr-qc/0109076v2", (8, 9),
                  "Lemma 1. Let the functions g_ik and phi be analytic at (0, ..., 0) in Sigma_0 and satisfy the "
                  "conditions (7), (8), (9), and the equation (20) in an open set of R^(n+1) which contains (0, ..., 0, "
                  "0). If, in addition, g_ik and phi satisfy (21) and (22) at Sigma_0, then g_ik e phi also satisfy (21) "
                  "and (22) in some open set of R^(n+1) containing (0, ..., 0, 0)."),
    "DR_CK": ("Dahia, Romero, gr-qc/0109076v2", 10,
              "If the functions F^A are analytic with respect to each of their arguments around the values evaluated at "
              "the point y^1 = ... = y^n = 0, then there exists a unique solution of equations (31) which is analytic at "
              "0 in R^(n+1) and that satisfies the initial condition"),
    "DR_lemma2": ("Dahia, Romero, gr-qc/0109076v2", 12,
                  "Lemma 2. Let g_ik (y^1, ..., y^n) and Omega_ik (y^1, ..., y^n), for i, k = 1, .., n, and phi (y^1, "
                  "..., y^n, y^(n+1)), be arbitrary functions which are analytic at 0 ... Then there exists a unique set "
                  "of functions g_ik (y^1, ..., y^n, y^(n+1)), which are analytic at 0 in R^(n+1), that satisfy: i) the "
                  "conditions (7), (8) and the equation (20) in a neighborhood of 0 in R^(n+1); and ii) the initial "
                  "conditions (6) and (36)."),
    "DR_thm2": ("Dahia, Romero, gr-qc/0109076v2", 12,
                "Then, M^n has a local isometric and analytic embedding (at the point p) in a (n+1)-dimensional Einstein "
                "space with cosmological constant Lambda if and only if there exist functions Omega_ik (x^1, ..., x^n), "
                "(i, k = 1, .., n), that are analytic at 0 in R^n and such that Omega_ik = Omega_ki (38) g^jk (nabla_j "
                "Omega_ik - nabla_i Omega_jk) = 0 (39) g^ik g^jm (R_ijkm + epsilon (Omega_ik Omega_jm - Omega_jk "
                "Omega_im)) = -2 Lambda. (40)"),
    "DR_unique": ("Dahia, Romero, gr-qc/0109076v2", 16,
                  "iii) a function phi (x^1, ..., x^(n+1)) not 0, analytic at 0 in R^(n+1), is chosen; then the line "
                  "element of the embedding space as referred to in theorem 1 is unique.."),
    "DR_RS": ("Dahia, Romero, gr-qc/0109076v2", 19,
              "If Lambda is negative, then the embedding space is closely related to the so-called bulk, in the "
              "Randall-Sundrum braneworld scenario [3]."),
    "PL_abstract": ("Planck Collaboration 2018 VI, 1807.06209v4", 1,
                    "Hubble constant H0 = (67.4+-0.5) km s-1 Mpc-1; matter density parameter Omega_m = 0.315+-0.007 ... "
                    "baryon density Omega_b h2 = 0.0224 +- 0.0001 ... The joint constraint with BAO measurements on "
                    "spatial curvature is consistent with a flat universe, Omega_K = 0.001+-0.002. Also combining with "
                    "Type Ia supernovae (SNe), the dark-energy equation of state parameter is measured to be w0 = -1.03 +- "
                    "0.03, consistent with a cosmological constant."),
    "PL_49": ("Planck Collaboration 2018 VI, 1807.06209v4", 43,
              "w(a) = w0 + (1 - a)wa, (49) ... The parametric equation of state given by Eq. (49) stays out of the "
              "phantom regime (i.e., has w >= -1) at all times only in the (upper-right) unshaded region."),
    "PL_50": ("Planck Collaboration 2018 VI, 1807.06209v4", 43,
              "Fixing the evolution parameter wa = 0, we obtain the tight constraint w0 = -1.028 +- 0.031 (68 %, Planck "
              "TT,TE,EE+lowE +lensing+SNe+BAO), (50)"),
    "PL_51": ("Planck Collaboration 2018 VI, 1807.06209v4", 44,
              "and restricting to w0 > -1 (i.e., not allowing phantom equations of state), we find w0 < -0.95 (95 %, "
              "Planck TT,TE,EE+lowE +lensing+SNe+BAO). (51)"),
    "PL_T6": ("Planck Collaboration 2018 VI, 1807.06209v4", 44,
              "Table 6 ... Parameter Planck+SNe+BAO Planck+BAO/RSD+WL w0 . . . -0.957 +- 0.080 -0.76 +- 0.20 wa . . . "
              "-0.29 +0.32 -0.26 -0.72 +0.62 -0.54 ... Delta chi2 . . . -1.4 -1.4"),
    "DESI_TV": ("DESI Collaboration, DR2 Results II, 2503.14738v3", 20,
                "w0waCDM ... DESI+CMB 0.353 +- 0.021 63.6 +1.6 -2.1 -- -0.42 +- 0.21 -1.75 +- 0.58 DESI+CMB+Pantheon+ "
                "0.3114 +- 0.0057 67.51 +- 0.59 -- -0.838 +- 0.055 -0.62 +0.22 -0.19 DESI+CMB+Union3 0.3275 +- 0.0086 "
                "65.91 +- 0.84 -- -0.667 +- 0.088 -1.09 +0.31 -0.27 DESI+CMB+DESY5 0.3191 +- 0.0056 66.74 +- 0.56 -- "
                "-0.752 +- 0.057 -0.86 +0.23 -0.20"),
    "DESI_NEC": ("DESI Collaboration, DR2 Results II, 2503.14738v3", 23,
                 "crosses to the regime w(z) < -1 [133] where the null energy condition (NEC)--which requires that the "
                 "energy density of dark energy not increase with the expansion of the Universe--is violated."),
    "DESI_cross": ("DESI Collaboration, DR2 Results II, 2503.14738v3", 25,
                   "In all cases, the favored w(z) shows a phase of w > -1 at low redshifts and a phantom crossing to w < "
                   "-1 above redshifts z ≃ 0.4."),
    "DESI_sig": ("DESI Collaboration, DR2 Results II, 2503.14738v3", 24,
                 "The Delta chi2_MAP values are -10.7, -17.4, and -21.0, corresponding to preferences for the w0waCDM "
                 "model over LambdaCDM at the 2.8 sigma, 3.8 sigma, and 4.2 sigma levels, for combination with "
                 "Pantheon+, Union3 and DESY5 respectively."),
    "DESI_escape": ("DESI Collaboration, DR2 Results II, 2503.14738v3", 25,
                    "In some circumstances it may therefore be possible to construct particular models that provide "
                    "reasonable fits to the low-redshift data while still respecting w(z) >= -1 at all z"),
}
# READ values (each from the READS row named beside it)
PLANCK_H_LITTLE = Fr(674, 1000)                    # PL_abstract: H0 = 67.4
PLANCK_OMB_H2 = Fr(224, 10000)                     # PL_abstract
PLANCK_W0, PLANCK_W0_SIG = -1.028, 0.031           # PL_50
PLANCK_T6 = (-0.957, -0.29)                        # PL_T6 (w0, wa), Planck+SNe+BAO
DESI_FITS = {                                      # DESI_TV: (Omega_m, w0, wa)
    "DESI+CMB+Pantheon+": (0.3114, -0.838, -0.62),
    "DESI+CMB+Union3": (0.3275, -0.667, -1.09),
    "DESI+CMB+DESY5": (0.3191, -0.752, -0.86),
    "DESI+CMB": (0.353, -0.42, -1.75),
}

# ------------------------------------------------------------------------------------------------ owners
_CACHE = {}
_USED = set()
OWNER_PATHS = {
    "localbulk": os.path.join(D68, "bulk", "localbulk.py"),
    "axioms": os.path.join(HERE, "axioms.py"),
    "b5": os.path.join(HERE, "b5_positive.py"),
    "cosmo": os.path.join(WD, "cosmo.py"),
    "exactE": os.path.join(D68, "copy", "exactE.py"),
    "stage2": os.path.join(HERE, "b4d_stage2.py"),
    "b6p": os.path.join(HERE, "b6p_scale.py"),
    "warp": os.path.join(D68, "warptheorem.py"),
}
OWNER_ALLOW = {("localbulk", "gauss_rhs"), ("axioms", "derive_z3"), ("b5", "b5a"), ("b5", "b5b"), ("cosmo", "H0"),
               ("cosmo", "OMEGA_M"), ("exactE", "C_SI"), ("exactE", "G_SI"), ("stage2", "TABLETOP"),
               ("b6p", "determined"), ("warp", "LEMMAS")}
EQ17_CARRIERS = {("localbulk", "ricci_scalar"), ("localbulk", "compute")}   # the owner functions that carry eq. (17)


def _load(path, key, register=False):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        if register:                       # cypher.py's @dataclass resolves through sys.modules
            sys.modules[key] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def own(name, attr):
    """An owner's attribute, loaded by path; every use is recorded for guard G1 (no eq. (17) carrier is used)."""
    key = "own_" + name
    if key not in _CACHE:
        _CACHE[key] = _load(OWNER_PATHS[name], "b1m_" + name)
    _USED.add((name, attr))
    return getattr(_CACHE[key], attr)


def cypher():
    if "cypher" not in _CACHE:
        _CACHE["cypher"] = _load(CYPHER_PATH, "b1m_cypher", register=True)
    return _CACHE["cypher"]


def _z(e):
    """Exact zero test: simplify, then cancel."""
    e = sp.simplify(e)
    return e == 0 or sp.cancel(e) == 0


# ======================================================================================== PART A: B1' on the plane
T, R, TH, PH = sp.symbols("t r theta phi")
KC, KAP, LAM, L5, CDR = sp.symbols("k_c kappa lambda Lambda5 C")
ELL = sp.Symbol("ell", positive=True)
I4 = sp.eye(4)


def _frw():
    """FRW with spatial curvature k_c: metric, Christoffels, Ricci, R(4), mixed Einstein tensor (computed once)."""
    if "frw" in _CACHE:
        return _CACHE["frw"]
    a = sp.Function("a")(T)
    rho, p = sp.Function("rho")(T), sp.Function("p")(T)
    X = [T, R, TH, PH]
    g = sp.diag(-1, a**2 / (1 - KC * R**2), a**2 * R**2, a**2 * R**2 * sp.sin(TH) ** 2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[A, D] * (sp.diff(g[D, B], X[C]) + sp.diff(g[D, C], X[B]) - sp.diff(g[B, C], X[D]))
                             for D in range(n)) / 2) for C in range(n)] for B in range(n)] for A in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[A][b][c], X[A]) - sp.diff(Gam[A][b][A], X[c])
                                        + sum(Gam[A][A][D] * Gam[D][b][c] - Gam[A][c][D] * Gam[D][b][A] for D in range(n))
                                        for A in range(n)))
    R4 = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    Gmix = sp.simplify(gi * Ric - I4 * R4 / 2)
    _CACHE["frw"] = {"a": a, "rho": rho, "p": p, "X": X, "g": g, "gi": gi, "Gam": Gam, "Ric": Ric, "R4": R4,
                     "Gmix": Gmix, "H": sp.diff(a, T) / a}
    return _CACHE["frw"]


def israel(tau, lam=LAM, mut=None):
    """SMS eq. (16) (READ p.3), mixed indices: K = -(kappa^2/2)(S - I S/3), S = -lambda I + tau."""
    S = -lam * I4 + tau
    if mut == "no_trace":
        return -(KAP**2 / 2) * S
    if mut == "no_z2_half":
        return -KAP**2 * (S - I4 * S.trace() / 3)
    return -(KAP**2 / 2) * (S - I4 * S.trace() / 3)


def gauss_right(K, l5=L5, mut=None):
    """2 Lambda5 + (K^2 - K.K): the Gauss constraint's right side (localbulk.py's form, any K)."""
    q = K.trace() ** 2 - (K * K).trace()
    return 2 * l5 - q if mut == "gauss_sign" else 2 * l5 + q


def lam4(mut=None):
    return L5 / 2 if mut == "lam4_wrong" else (L5 + KAP**4 * LAM**2 / 6) / 2


def h2_friedmann(rho, a, mut=None):
    """H^2 of the plane: Lambda4/3 + kappa^4 lambda rho/18 + kappa^4 rho^2/36 - k_c/a^2 + C/a^4."""
    quad = 0 if mut == "no_rho2" else KAP**4 * rho**2 / 36
    return lam4(mut) / 3 + KAP**4 * LAM * rho / 18 + quad - KC / a**2 + CDR / a**4


def pi_sms(tau, mut=None):
    """SMS eq. (20) (READ p.3), mixed indices."""
    tt = tau.trace()
    c8 = sp.Rational(1, 4) if mut == "pi_coeff" else sp.Rational(1, 8)
    c4 = sp.Rational(1, 2) if mut == "pi_tt" else sp.Rational(1, 4)
    return -(tau * tau) * c4 + tt * tau / 12 + I4 * (tau * tau).trace() * c8 - I4 * tt**2 / 24


def _fluid_tau(rho, p):
    return sp.diag(-rho, p, p, p)            # tau^mu_nu of a perfect fluid at rest (t_mu t^nu = -1)


def _frw_sub(expr, mut=None, conserved=True):
    """Replace a'', a', rho' on FRW by the plane's Friedmann equation (with C) and conservation."""
    f = _frw()
    a, rho, p = f["a"], f["rho"], f["p"]
    Hs = sp.sqrt(h2_friedmann(rho, a, mut))
    ad = a * Hs
    rhod = -3 * Hs * (rho + p) if conserved else -2 * Hs * rho
    e = expr.subs(sp.Derivative(a, (T, 2)), sp.diff(ad, T))
    e = e.subs(sp.Derivative(rho, T), rhod).subs(sp.Derivative(a, T), ad)
    e = e.subs(sp.Derivative(rho, T), rhod).subs(sp.Derivative(a, T), ad)
    return e


def check_A1(mut=None):
    """B1'(a): Israel's data for a perfect fluid (SMS (16), READ p.3)."""
    f = _frw()
    K = israel(_fluid_tau(f["rho"], f["p"]), mut=mut)
    kt, kx = sp.simplify(K[0, 0]), sp.simplify(K[1, 1])
    ok = (_z(kt + KAP**2 / 6 * (LAM - 2 * f["rho"] - 3 * f["p"])) and _z(kx + KAP**2 / 6 * (LAM + f["rho"]))
          and _z(K[2, 2] - K[1, 1]) and _z(K[3, 3] - K[1, 1]))
    return ok, {"K^t_t": str(kt), "K^i_i": str(kx), "label": "computed; READ SMS (16) p.3"}


def _codazzi(K, mut=None):
    f = _frw()
    X, Gam = f["X"], f["Gam"]
    out = []
    for mu in range(4):
        s = sum(sp.diff(K[nu, mu], X[nu]) for nu in range(4))
        if mut != "drop_connection":
            s += sum(Gam[nu][nu][l] * K[l, mu] for nu in range(4) for l in range(4))
            s -= sum(Gam[l][nu][mu] * K[nu, l] for nu in range(4) for l in range(4))
        out.append(sp.simplify(s - sp.diff(K.trace(), X[mu])))
    return out


def check_A2(mut=None):
    """B1'(a): Codazzi = (kappa^2/2)(rho' + 3H(rho + p)) delta^t = -(kappa^2/2) D.tau (SMS (21)); conserved dust passes,
    non-conserved dust fails."""
    f = _frw()
    a, rho, p, H = f["a"], f["rho"], f["p"], f["H"]
    K = israel(_fluid_tau(rho, p), mut=None if mut == "drop_connection" else mut)
    cod = _codazzi(K, mut)
    form = _z(cod[0] - KAP**2 / 2 * (sp.diff(rho, T) + 3 * H * (rho + p))) and all(_z(c) for c in cod[1:])
    r0 = sp.Symbol("rho0", positive=True)
    dust = sp.simplify(cod[0].subs(p, 0).subs(rho, r0 / a**3).doit())
    bad = sp.simplify(cod[0].subs(p, 0).subs(rho, r0 / a**2).doit())
    ok = form and _z(dust) and not _z(bad)
    return ok, {"codazzi_t": str(sp.factor(cod[0])), "conserved_dust": str(dust), "control_rho_a^-2": str(bad),
                "label": "computed; READ SMS (2), (10) p.2, (21) p.4"}


def check_A3(mut=None):
    """B1'(a): Gauss holds identically on the plane obeying the brane Friedmann equation with C; conversely Gauss with
    Codazzi makes a^4(H^2 + k_c/a^2 - ...) constant (the dark-radiation C is the integration constant)."""
    f = _frw()
    a, rho, p, H = f["a"], f["rho"], f["p"], f["H"]
    K = israel(_fluid_tau(rho, p), mut=mut if mut == "no_trace" else None)
    res = sp.simplify(f["R4"] - gauss_right(K, mut=mut))
    mod = sp.simplify(_frw_sub(res, mut))
    Xq = a**4 * (H**2 - h2_friedmann(rho, a, mut) + CDR / a**4)
    dX = sp.diff(Xq, T).subs(sp.Derivative(rho, T), -3 * H * (rho + p))
    ratio = sp.simplify(dX / res) if not _z(res) else sp.Integer(0)
    ok = _z(mod) and _z(ratio - a**3 * sp.diff(a, T) / 3)
    return ok, {"gauss_mod_friedmann": str(mod), "dX/dt over residual": str(ratio),
                "friedmann_H2": str(h2_friedmann(sp.Symbol("rho"), sp.Symbol("a"), mut)),
                "label": "computed; READ SMS (18) p.3"}


def check_A4(mut=None):
    """B1'(a): trace of SMS (17) = Gauss for a generic symmetric tau; SMS (28) from (20); on FRW E^mu_nu is traceless,
    proportional to C, zero iff C = 0."""
    eta = sp.diag(-1, 1, 1, 1)
    ts = sp.symbols("t0:10")
    low = sp.zeros(4)
    for s, (i, j) in zip(ts, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]):
        low[i, j] = low[j, i] = s
    tau = eta * low
    g8 = KAP**4 * LAM / 3 if mut == "GN_wrong" else KAP**4 * LAM / 6          # 8 pi G_N, SMS (19)
    tr_rhs = -4 * lam4() + g8 * tau.trace() + KAP**4 * pi_sms(tau, mut).trace()
    trace_ok = sp.expand(-gauss_right(israel(tau)) - tr_rhs) == 0
    rh, pp = sp.symbols("rho p")
    tf = _fluid_tau(rh, pp)
    pi28 = sp.Rational(1, 12) * rh * (rh * sp.diag(-1, 0, 0, 0) + (rh + 2 * pp) * sp.diag(0, 1, 1, 1))
    ok28 = sp.simplify(pi_sms(tf, mut) - pi28) == sp.zeros(4)
    f = _frw()
    tfr = _fluid_tau(f["rho"], f["p"])
    E = -f["Gmix"] - lam4() * I4 + g8 * tfr + KAP**4 * pi_sms(tfr, mut)
    E = sp.simplify(_frw_sub(E))
    traceless = _z(E.trace())
    zero_at_C0 = all(_z(x) for x in E.subs(CDR, 0))
    Ett = sp.simplify(E[0, 0])
    ok = trace_ok and ok28 and traceless and zero_at_C0 and not _z(Ett)
    return ok, {"trace_identity_generic_tau": trace_ok, "SMS28_from_20": ok28, "E^t_t": str(Ett),
                "E^r_r": str(sp.simplify(E[1, 1])), "E_traceless": traceless, "E_zero_iff_C0": zero_at_C0,
                "label": "computed; READ SMS (17)-(20) p.3, (28) p.5"}


def check_A5(mut=None):
    """B1'(a): the matter-free plane is the limit rho, p -> 0 -- localbulk.gauss_rhs, imported, at c = -kappa^2 lambda/6;
    zero at the RS tension; H = 0 and R(4) = 0 there (B1)."""
    gauss_rhs = own("localbulk", "gauss_rhs")
    rh, pp = sp.symbols("rho p")
    mine = gauss_right(israel(_fluid_tau(rh, pp))).subs({rh: 0, pp: 0})
    c = -KAP**2 * LAM / 3 if mut == "c_wrong" else -KAP**2 * LAM / 6
    lim_ok = _z(mine - gauss_rhs(c, L5))
    rs = {LAM: 6 / (KAP**2 * ELL), L5: -6 / ELL**2}
    if mut == "off_rs":
        rs = {LAM: 7 / (KAP**2 * ELL), L5: -6 / ELL**2}
    rs_ok = _z(mine.subs(rs)) and _z(gauss_rhs(-1 / ELL, -6 / ELL**2))
    av = sp.Symbol("a", positive=True)
    h2_0 = sp.simplify(h2_friedmann(0, av).subs({CDR: 0, KC: 0}).subs(rs))
    ok = lim_ok and rs_ok and _z(h2_0)
    return ok, {"limit_rhs": str(sp.simplify(mine)), "localbulk_gauss_rhs(-1/ell,-6/ell^2)": str(gauss_rhs(-1 / ELL, -6 / ELL**2)),
                "H2_matter_free_RS": str(h2_0), "label": "computed; imported localbulk.gauss_rhs (B1's own form)"}


def check_A6(mut=None):
    """B1'(a), each side its own ell (B6's unequal sides, no Z2): per-side Gauss holds with K^x_x = -/+ sqrt(h + k_c/a^2
    + 1/ell_s^2 - C_s/a^4) and K^t_t = d(a K^x_x)/da; the jump defines a conserved fluid; matter-free: lambda = (3/kappa^2)
    (1/ell_+ + 1/ell_-), each side passing localbulk.gauss_rhs."""
    gauss_rhs = own("localbulk", "gauss_rhs")
    av = sp.Symbol("a", positive=True)
    h = sp.Function("h")(av)
    lp, lm, Cp, Cm = sp.symbols("ell_p ell_m C_p C_m", positive=True)
    R4 = 6 * (av / 2 * sp.diff(h, av) + 2 * h + KC / av**2)
    sides = {}
    for name, l, Cs, sgn in (("+", lp, Cp, -1), ("-", lm, Cm, 1 if mut != "same_sign" else -1)):
        kx = sgn * sp.sqrt(h + KC / av**2 + 1 / l**2 - Cs / av**4)
        kt = kx if mut == "kt_eq_kx" else sp.diff(av * kx, av)
        res = sp.simplify(R4 - (2 * (-6 / l**2) + 6 * kt * kx + 6 * kx**2))
        sides[name] = {"kx": kx, "kt": kt, "gauss_res": res}
    jx = sides["+"]["kx"] - sides["-"]["kx"]
    jt = sides["+"]["kt"] - sides["-"]["kt"]
    rho = -3 * jx / KAP**2 - LAM
    p = (LAM - 2 * rho + 3 * jt / KAP**2) / 3
    cons = sp.simplify(av * sp.diff(rho, av) + 3 * (rho + p))
    rho0 = sp.simplify(rho.subs(h, 0).doit().subs({KC: 0, Cp: 0, Cm: 0}))
    lam_free = sp.solve(sp.Eq(rho0, 0), LAM)
    want = 3 / KAP**2 * (1 / lp + 1 / lm)
    lim_ok = len(lam_free) == 1 and _z(lam_free[0] - want)
    each = _z(gauss_rhs(-1 / lp, -6 / lp**2)) and _z(gauss_rhs(1 / lm, -6 / lm**2))
    # the low-density coupling: kappa^2 rho/3 = F(H^2) - F(0), F = sqrt(H^2 + 1/ell_+^2) + sqrt(H^2 + 1/ell_-^2)
    x = sp.Symbol("x")
    F = sp.sqrt(x + 1 / lp**2) + sp.sqrt(x + 1 / lm**2)
    coupling = sp.simplify((KAP**2 / 3) / sp.diff(F, x).subs(x, 0))           # H^2 ~ coupling x rho
    z2 = sp.simplify(coupling.subs(lm, lp) - KAP**4 * (6 / (KAP**2 * lp)) / 18)
    ok = (all(_z(sides[s]["gauss_res"]) for s in sides) and _z(cons) and lim_ok and each and _z(z2))
    return ok, {"gauss_res_+": str(sides["+"]["gauss_res"]), "gauss_res_-": str(sides["-"]["gauss_res"]),
                "conservation_from_jump": str(cons), "lambda_matter_free": [str(v) for v in lam_free],
                "low_density_H2_per_rho": str(coupling), "B6_ratio_ell_R/ell_L=4/3": str(sp.simplify(
                    coupling.subs({lp: sp.Rational(4, 3) * lm}))), "label": "computed; imported localbulk.gauss_rhs"}


def check_A7(mut=None):
    """B1'(a): dark energy as a w = -1 part of tau at the RS tension, or as tension above it: SMS (17)'s right side is
    identical (SMS p.3 calls the split ambiguous)."""
    rh, pp, rL = sp.symbols("rho p rho_L")
    tm = _fluid_tau(rh, pp)

    def rhs(lmb, tau):
        L4 = (L5 + KAP**4 * lmb**2 / 6) / 2
        return -L4 * I4 + KAP**4 * lmb / 6 * tau + KAP**4 * pi_sms(tau)
    left = rhs(LAM, tm - rL * I4)
    right = rhs(LAM + rL, tm - rL * I4) if mut == "double_count" else rhs(LAM + rL, tm)
    ok = sp.simplify(left - right) == sp.zeros(4)
    return ok, {"identical": ok, "label": "computed; READ SMS_split p.3"}


def observed():
    """Our plane's numbers (cosmo.py's Planck H0 and Omega_m, exactE.py's c and G, b4d_stage2.py's table-top ell)."""
    if "obs" in _CACHE:
        return _CACHE["obs"]
    H0 = own("cosmo", "H0")()
    Om = own("cosmo", "OMEGA_M")
    c, G = float(own("exactE", "C_SI")), float(own("exactE", "G_SI"))
    ell = own("stage2", "TABLETOP")
    _CACHE["obs"] = {"H0": H0, "Omega_m": Om, "c": c, "G": G, "ell": ell}
    return _CACHE["obs"]


def check_A8(mut=None):
    """B1'(a): our plane's matter against its tension, eps = rho/lambda_RS = Omega (H0 ell/c)^2/2 (two routes)."""
    o = observed()
    c = o["c"] / 1000.0 if mut == "c_kms" else o["c"]
    half = 1.0 if mut == "factor_two" else 0.5
    eps_formula = half * (o["H0"] * o["ell"] / c) ** 2
    rho_c = 3 * o["H0"] ** 2 / (8 * math.pi * o["G"])
    lam_rs = 3 * o["c"] ** 4 / (4 * math.pi * o["G"] * o["ell"] ** 2)          # SMS (19) with kappa^2 lambda = 6/ell
    eps_route2 = rho_c * o["c"] ** 2 / lam_rs
    ystar = 0.5 * math.log1p(2.0 / eps_formula)                                 # y*/ell, check B3's formula
    ok = abs(eps_formula / eps_route2 - 1) < 1e-12 and eps_formula < 1e-60
    return ok, {"eps_total": eps_formula, "eps_matter": eps_formula * o["Omega_m"], "eps_route2": eps_route2,
                "lambda_RS_J_per_m3": lam_rs, "rho_c_c2_J_per_m3": rho_c * o["c"] ** 2, "ell_m": o["ell"],
                "chart_reach_y*/ell": ystar, "label": "computed (cosmo.py H0, Omega_m; exactE.py c, G; table-top ell)"}


# ======================================================================================== PART B: B2' off the plane
_TY = sp.symbols("t Y")
JET = sp.symbols("A At Att AY AYY AtY N Nt NY NYY")
JA, JAt, JAtt, JAY, JAYY, JAtY, JN, JNt, JNY, JNYY = JET
AJ, HJ = sp.symbols("a H", positive=True)


def _bulk5():
    """Generic 5D Gaussian-normal metric -n^2 dt^2 + a^2 dx^2 + dY^2 with n(t, Y), a(t, Y): Christoffels, Ricci, Einstein
    (+ Lambda5 g), as polynomial numerators in the jet symbols (computed once)."""
    if "b5d" in _CACHE:
        return _CACHE["b5d"]
    t, Y = _TY
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    Af, Nf = sp.Function("A")(t, Y), sp.Function("N")(t, Y)
    X = [t, x1, x2, x3, Y]
    g = sp.diag(-Nf**2, Af**2, Af**2, Af**2, 1)
    gi = g.inv()
    n = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]

    def ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                               for a in range(n)))
    Ric = sp.zeros(n)
    for i in range(n):
        for j in range(i, n):
            Ric[i, j] = Ric[j, i] = ric(i, j)
    Rs = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(n)))
    Ein = sp.simplify(Ric - Rs / 2 * g + L5 * g)
    rep = {sp.Derivative(Af, (t, 2)): JAtt, sp.Derivative(Af, (Y, 2)): JAYY, sp.Derivative(Af, Y, t): JAtY,
           sp.Derivative(Af, t, Y): JAtY, sp.Derivative(Af, t): JAt, sp.Derivative(Af, Y): JAY,
           sp.Derivative(Nf, (Y, 2)): JNYY, sp.Derivative(Nf, t): JNt, sp.Derivative(Nf, Y): JNY}

    def J(e):
        return e.subs(rep).subs({Af: JA, Nf: JN})
    gj = sp.diag(-JN**2, JA**2, JA**2, JA**2, 1)
    comps = {}
    for name, (i, j), kind in (("E00", (0, 0), "E"), ("E11", (1, 1), "E"), ("E44", (4, 4), "E"), ("E04", (0, 4), "E"),
                               ("R00", (0, 0), "R"), ("R11", (1, 1), "R")):
        e = J(Ein[i, j]) if kind == "E" else J(Ric[i, j]) - (2 * L5 / 3) * gj[i, j]
        num, _den = sp.fraction(sp.together(sp.factor(e)))
        comps[name] = sp.expand(num)
    _CACHE["b5d"] = {"comps": comps, "Gam": Gam, "g": g, "gi": gi, "X": X, "Af": Af, "Nf": Nf}
    return _CACHE["b5d"]


class Jet:
    """The plane's homogeneous data as a jet in (a, H, sigma_i): d/dt a = aH, d/dt sigma_i = -3H(1 + w_i) sigma_i,
    H^2 by the plane's Friedmann equation (sigma = kappa^2 rho/6, RS tension, flat): (sum sigma + 1/ell)^2 - 1/ell^2
    + C/a^4.  mode 'gr' drops the sigma^2 term (GR's Friedmann); 'nonconserved' gives dust sigma' = -2H sigma."""

    def __init__(self, ws, C=CDR, mode=None):
        self.ws = list(ws)
        self.sig = sp.symbols("sigma0:%d" % len(self.ws), positive=True)
        self.C = C
        S = sum(self.sig)
        self.h2 = (2 * S / ELL + self.C / AJ**4) if mode == "gr" else ((S + 1 / ELL) ** 2 - 1 / ELL**2 + self.C / AJ**4)
        rate = -2 if mode == "nonconserved" else -3
        self.sdot = [rate * HJ * (1 + w) * s if mode != "nonconserved" else rate * HJ * s
                     for s, w in zip(self.sig, self.ws)]
        num = sp.diff(self.h2, AJ) * AJ * HJ + sum(sp.diff(self.h2, s) * sd for s, sd in zip(self.sig, self.sdot))
        self.hdot = sp.simplify(num / (2 * HJ))

    def red(self, e):
        e = sp.expand(e)
        if not e.has(HJ):
            return e
        P = sp.Poly(e, HJ)
        out = 0
        for (k,), c in P.terms():
            out += c * self.h2 ** (k // 2) * HJ ** (k % 2)
        return sp.expand(out)

    def D(self, f):
        e = sp.diff(f, AJ) * AJ * HJ + sp.diff(f, HJ) * self.hdot
        e += sum(sp.diff(f, s) * sd for s, sd in zip(self.sig, self.sdot))
        return self.red(e)

    def S(self):
        return sum(self.sig)

    def israel_data(self, factor=1, mut=None):
        """(A1, N1) = (a K^x_x, K^t_t) from SMS (16): K^x_x = -(1/ell + sum sigma), K^t_t = -(1/ell - sum (2+3w) sigma)."""
        if mut == "kx_no_matter":
            return AJ * (-1 / ELL), -1 / ELL
        kx = -(1 / ELL + factor * self.S())
        kt = -(1 / ELL - factor * sum((2 + 3 * w) * s for s, w in zip(self.sig, self.ws)))
        return AJ * kx, kt


def _mul(jet, x, y, M):
    return [jet.red(sum(x[i] * y[k - i] for i in range(k + 1))) for k in range(M + 1)]


def _evalpoly(jet, expr, F, M):
    total = [0] * (M + 1)
    for term in sp.Add.make_args(sp.expand(expr)):
        c, factors = term.as_coeff_mul()
        ser = [c] + [0] * M
        for fct in factors:
            b, ex = (fct.args if fct.is_Pow else (fct, 1))
            if b in F:
                for _ in range(int(ex)):
                    ser = _mul(jet, ser, F[b], M)
            else:
                ser = [jet.red(q * fct) for q in ser]
        total = [total[k] + ser[k] for k in range(M + 1)]
    return [jet.red(q) for q in total]


def _fields(jet, Ac, Nc, M):
    def ser(c):
        return [c[k] / sp.factorial(k) if k < len(c) else 0 for k in range(M + 1)]
    return {JA: ser(Ac), JN: ser(Nc), JAY: ser(Ac[1:]), JAYY: ser(Ac[2:]), JNY: ser(Nc[1:]), JNYY: ser(Nc[2:]),
            JAt: ser([jet.D(q) for q in Ac]), JAtt: ser([jet.D(jet.D(q)) for q in Ac]),
            JAtY: ser([jet.D(q) for q in Ac[1:]]), JNt: ser([jet.D(q) for q in Nc])}


def _comps(l5):
    return {k: v.subs(L5, l5) for k, v in _bulk5()["comps"].items()}


def ck_series(jet, N, data=None, mut=None, l5=None):
    """Cauchy-Kowalewski in y, order by order: a = sum A_k y^k/k!, n = sum N_k y^k/k!, A_0 = a, N_0 = 1, (A_1, N_1) the
    Israel data; A_{j+2}, N_{j+2} from the evolution equations R_tt, R_xx = (2 Lambda5/3) g at order y^j."""
    comps = _comps(-6 / ELL**2 if l5 is None else l5)
    A1, N1 = data if data is not None else jet.israel_data(mut=mut)
    Ac, Nc, dets = [AJ, A1], [sp.Integer(1), N1], []
    u, v = sp.symbols("u_new v_new")
    for j in range(N - 1):
        F = _fields(jet, Ac + [u], Nc + [v], j)
        e1 = _evalpoly(jet, comps["R00"], F, j)[j]
        e2 = _evalpoly(jet, comps["R11"], F, j)[j]
        Jm = sp.Matrix([[sp.diff(e1, u), sp.diff(e1, v)], [sp.diff(e2, u), sp.diff(e2, v)]])
        dets.append(sp.simplify(Jm.det()))
        if mut == "skip_solve":
            su, sv = sp.Integer(0), sp.Integer(0)
        else:
            sol = sp.solve([e1, e2], [u, v], dict=True)
            su, sv = sol[0][u], sol[0][v]
        Ac.append(jet.red(sp.together(su)))
        Nc.append(jet.red(sp.together(sv)))
    return Ac, Nc, dets


def ck_residuals(jet, Ac, Nc, N, l5=None):
    """All four components through the orders they determine: evolution (E00, E11) through y^(N-2), constraints (E44, E04)
    through y^(N-1)."""
    comps = _comps(-6 / ELL**2 if l5 is None else l5)
    F = _fields(jet, Ac, Nc, N - 1)
    out = {}
    for name, top in (("E00", N - 2), ("E11", N - 2), ("E44", N - 1), ("E04", N - 1)):
        ser = _evalpoly(jet, comps[name], F, top)
        out[name] = [_z(q) for q in ser[:top + 1]]
    return out


def dust_series6():
    """The dust plane's series to order 6, C symbolic, unmutated (computed once; B1 checks it, B3 compares it)."""
    if "dust6" not in _CACHE:
        _CACHE["dust6"] = ck_series(Jet((0,)), 6)
    return _CACHE["dust6"]


def check_B1(mut=None):
    """B2': the FRW plane with dust (C symbolic) to order 6 and the observed LCDM plane (dust + w = -1) to order 4: unique
    Taylor series (invertible coefficient matrix at every order), evolution residuals 0 through y^(N-2), the yy and ty
    constraints 0 through y^(N-1)."""
    l5 = 6 / ELL**2 if mut == "L5_sign" else None
    rows = {}
    for name, ws, N in (("dust", (0,), 6), ("LCDM", (0, -1), 4)):
        jet = Jet(ws)
        if name == "dust" and mut is None:
            Ac, Nc, dets = dust_series6()
        else:
            Ac, Nc, dets = ck_series(jet, N, mut=mut, l5=l5)
        res = ck_residuals(jet, Ac, Nc, N, l5=l5)
        rows[name] = {"order": N, "dets": [str(d) for d in dets], "dets_nonzero": all(not _z(d) for d in dets),
                      "dets_label": "STRUCTURAL: Kovalevskaya normal form in Gaussian-normal gauge; cannot fail; CK and "
                                    "Dahia-Romero (READ) carry uniqueness",
                      "residuals_zero": {k: all(v) for k, v in res.items()},
                      "A2": str(sp.factor(Ac[2])), "N2": str(sp.factor(Nc[2])), "A3": str(sp.factor(Ac[3])),
                      "N3": str(sp.factor(Nc[3]))}
        if not all(rows[name]["residuals_zero"].values()):
            break
    ok = all(all(r["residuals_zero"].values()) for r in rows.values()) and len(rows) == 2
    return ok, {"rows": rows, "label": "computed; READ Dahia-Romero Lemma 1 pp.8-9, CK p.10, Lemma 2/Thm 2 p.12"}


def _order0_constraints(jet, data):
    comps = _comps(-6 / ELL**2)
    A1, N1 = data
    F = _fields(jet, [AJ, A1], [sp.Integer(1), N1], 0)
    return {k: sp.simplify(_evalpoly(jet, comps[k], F, 0)[0]) for k in ("E44", "E04")}


def check_B2(mut=None):
    """B2' controls that must FAIL (inconsistent Israel data): doubled matter in K; GR's Friedmann (no sigma^2) with SMS's
    Israel data; a non-conserved dust.  Each leaves an order-0 constraint residual; the consistent data leave none."""
    good = Jet((0,))
    base = _order0_constraints(good, good.israel_data())
    fac = 1 if mut == "control_made_consistent" else 2
    doubled = _order0_constraints(good, good.israel_data(factor=fac))
    gr = Jet((0,), mode="gr")
    grr = _order0_constraints(gr, gr.israel_data())
    nc = Jet((0,), mode="nonconserved")
    ncr = _order0_constraints(nc, nc.israel_data())
    fails = {"doubled_matter": not all(_z(v) for v in doubled.values()),
             "GR_friedmann": not all(_z(v) for v in grr.values()),
             "non_conserved": not all(_z(v) for v in ncr.values())}
    ok = all(_z(v) for v in base.values()) and all(fails.values())
    return ok, {"consistent": {k: str(v) for k, v in base.items()}, "controls_fail": fails,
                "doubled": {k: str(sp.factor(v)) for k, v in doubled.items()},
                "GR": {k: str(sp.factor(v)) for k, v in grr.items()},
                "non_conserved": {k: str(sp.factor(v)) for k, v in ncr.items()}, "label": "computed"}


def closed_form(jet, mut=None):
    """C = 0: a = a0 [cosh(y/ell) + beta sinh(y/ell)], n = cosh(y/ell) + nb sinh(y/ell), in X = e^(y/ell)."""
    Xs = sp.Symbol("X", positive=True)
    ch, sh = (Xs + 1 / Xs) / 2, (Xs - 1 / Xs) / 2
    S = jet.S()
    beta = -1 if mut == "beta_no_rho" else -(1 + ELL * S)
    nb = beta if mut == "n_static" else beta + 3 * ELL * sum((1 + w) * s for s, w in zip(jet.sig, jet.ws))
    return Xs, AJ * (ch + beta * sh), ch + nb * sh, beta, nb


def check_B3(mut=None):
    """B2', C = 0: the closed bulk is exact (every component zero), equals the dust series through order 6, is maximally
    symmetric (pure AdS5, Kretschmann 40/ell^4); a(t, y*) = 0 at y* = (ell/2) ln(1 + 2/(ell sigma))."""
    b5 = _bulk5()
    out = {}
    ok = True
    for name, ws in (("dust", (0,)), ("LCDM", (0, -1))):
        jet = Jet(ws, C=0)
        Xs, Aex, Nex, beta, nb = closed_form(jet, mut)

        def dY(fn):
            return sp.diff(fn, Xs) * Xs / ELL
        vals = {JA: Aex, JN: Nex, JAY: dY(Aex), JAYY: dY(dY(Aex)), JNY: dY(Nex), JNYY: dY(dY(Nex)), JAt: jet.D(Aex),
                JAtt: jet.D(jet.D(Aex)), JAtY: jet.D(dY(Aex)), JNt: jet.D(Nex)}
        zero = {}
        for k in ("E00", "E11", "E44", "E04"):
            e = _comps(-6 / ELL**2)[k].subs(vals)
            zero[k] = _z(jet.red(sp.expand(sp.numer(sp.together(e)))))
        # maximal symmetry: R_abcd + (g_ac g_bd - g_ad g_bc)/ell^2 = 0 component by component
        scale = 2 * ELL if mut == "curv_scale" else ELL
        t, Y = _TY
        Af, Nf, X, Gam, g = b5["Af"], b5["Nf"], b5["X"], b5["Gam"], b5["g"]
        maxsym = True
        ncomp = npair = 0
        for a_, b_, c_, d_ in itertools.product(range(5), repeat=4):
            if not (a_ < b_ and c_ < d_ and (a_, b_) <= (c_, d_)):
                continue
            npair += 1
            rr = (sp.diff(Gam[a_][b_][d_], X[c_]) - sp.diff(Gam[a_][b_][c_], X[d_])
                  + sum(Gam[a_][c_][f_] * Gam[f_][b_][d_] - Gam[a_][d_][f_] * Gam[f_][b_][c_] for f_ in range(5)))
            rr = sp.simplify(g[a_, a_] * rr + (g[a_, c_] * g[b_, d_] - g[a_, d_] * g[b_, c_]) / scale**2)
            if rr == 0:
                continue
            ncomp += 1
            sub = {}
            for dv in sorted(rr.atoms(sp.Derivative), key=lambda d: -len(d.variables)):
                ex = Aex if dv.expr.func == Af.func else Nex
                for vv in dv.variables:
                    ex = jet.D(ex) if vv == t else dY(ex)
                sub[dv] = ex
            e = rr.subs(sub).subs({Af: Aex, Nf: Nex})
            maxsym = maxsym and _z(jet.red(sp.expand(sp.numer(sp.together(e)))))
        # y*: a = 0 at X^2 = 1 + 2/(ell S) when beta = -(1 + ell S)
        Q = 1 + 2 / (ELL * jet.S())                                     # X*^2
        num = sp.expand(sp.numer(sp.together(Aex / AJ)))                 # a polynomial in X
        reach = (mut != "beta_no_rho" and not num.subs(Xs, 0) == num
                 and _z(sp.expand(num.subs(Xs, sp.sqrt(Q)))))
        out[name] = {"components_zero": zero, "max_symmetric": maxsym, "pairs_examined": npair,
                     "pairs_not_identically_zero_under_ansatz": ncomp,
                     "a_zero_at_y*": reach, "beta": str(beta), "n_coefficient": str(nb)}
        ok = ok and all(zero.values()) and maxsym and reach
    # the series at C = 0 equals the closed form through order 6 (dust)
    jet = Jet((0,), C=0)
    Ac, Nc, _d = dust_series6()
    Ac = [sp.simplify(q.subs(CDR, 0)) for q in Ac]
    Nc = [sp.simplify(q.subs(CDR, 0)) for q in Nc]
    S = jet.S()
    beta = -(1 + ELL * S)
    nb = beta + 3 * ELL * S
    match = all(_z(Ac[k] - AJ * (1 if k % 2 == 0 else beta) / ELL**k) and _z(Nc[k] - (1 if k % 2 == 0 else nb) / ELL**k)
                for k in range(7))
    out["series_equals_closed_form_order6"] = match
    out["kretschmann"] = "40/ell^4 (constant curvature -1/ell^2 in 5D: 2 n (n - 1)/ell^4, n = 5; deduced)"
    ok = ok and match
    return ok, {**out, "label": "computed (exact, sympy); deduced (Kretschmann from maximal symmetry)"}


def check_B4(mut=None):
    """B2': the dust plane explicit -- a^3 = (9 s0 a0^3/(2 ell)) t^2 + 3 s0 a0^3 t solves H^2 = 2 sigma/ell + sigma^2,
    sigma = s0 (a0/a)^3; analytic for t > 0."""
    s0, a0 = sp.symbols("s0 a0", positive=True)
    lin = 0 if mut == "gr_dust" else 3 * s0 * a0**3 * T
    a3 = 9 * s0 * a0**3 / (2 * ELL) * T**2 + lin
    a = a3 ** sp.Rational(1, 3)
    sig = s0 * a0**3 / a3
    res = sp.simplify((sp.diff(a, T) / a) ** 2 - (2 * sig / ELL + sig**2))
    ok = _z(res)
    return ok, {"a^3": str(a3), "friedmann_residual": str(res), "label": "computed"}


# ======================================================================================== PART C: Z3' and B5' with matter
def check_C1(mut=None):
    """Z3'a: R(k,k) = 0 for null k wherever the bulk is the model's vacuum (axioms.py's derive_z3, imported: it evaluates
    (2 Lambda/3) g(k,k), so it says nothing about a region carrying stress, the corridor's included); control: a timelike
    k gives (2 Lambda/3) g(k,k) != 0, so the zero is the null vector's."""
    d = own("axioms", "derive_z3")()
    lam = sp.Symbol("Lambda")
    g = sp.diag(-1, 1, 1, 1, 1)
    k = sp.Matrix([1, sp.Rational(3, 5), sp.Rational(4, 5), 0, 0]) if mut == "control_null" else sp.Matrix([1, 0, 0, 0, 0])
    ctl = sp.simplify((k.T * (2 * lam / 3 * g) * k)[0])
    ok = d["bulk_Rkk"] == 0 and d["null"] and not _z(ctl)
    return ok, {"bulk_Rkk": str(d["bulk_Rkk"]), "control_timelike": str(ctl), "label": "computed (imported axioms.py)"}


def check_C2(mut=None):
    """Z3': the plane's 5D null stress S(k,k) = (lambda + rho) k_y^2 + (rho + p)|k_space|^2 for every 5D null k; SMS's
    pi(k,k) = (1/6) rho (rho + p)(t.k)^2 for a 4D null k."""
    lam, rh, pp = sp.symbols("lambda rho p")
    s, u1, u2, u3 = sp.symbols("s u1 u2 u3", real=True)
    kt = sp.sqrt(s**2 + u1**2 + u2**2 + u3**2)
    k4 = sp.Matrix([kt, u1, u2, u3])                    # k^mu on the plane; k^y = s; -kt^2 + |u|^2 + s^2 = 0
    eta = sp.diag(-1, 1, 1, 1)
    sgn = 1 if mut == "lambda_sign" else -1
    S_low = sgn * lam * eta + sp.diag(rh, pp, pp, pp)
    Skk = sp.expand((k4.T * S_low * k4)[0])
    form = sp.expand((lam + rh) * s**2 + (rh + pp) * (u1**2 + u2**2 + u3**2))
    ok1 = sp.simplify(Skk - form) == 0
    k0 = sp.Matrix([sp.sqrt(u1**2 + u2**2 + u3**2), u1, u2, u3])
    pim = pi_sms(_fluid_tau(rh, pp), mut)
    pikk = sp.simplify((k0.T * (eta * pim) * k0)[0])
    ok2 = _z(pikk - rh * (rh + pp) / 6 * (u1**2 + u2**2 + u3**2))
    return (ok1 and ok2), {"S(k,k)": str(sp.factor(Skk)), "pi(k,k)": str(sp.factor(pikk)),
                           "blind": "STRUCTURAL: a null k sees none of SMS (20)'s q_mu nu terms (1/8, 1/24); A4's trace "
                                    "check sees them",
                           "label": "computed; READ SMS (13)-(14), (20) p.3"}


def _cpl_density():
    """rho_DE(a)/rho_DE0 for w(a) = w0 + (1 - a) wa (Planck eq. (49), READ) from d rho/da = -3 (1 + w) rho/a (computed)."""
    if "cpl" in _CACHE:
        return _CACHE["cpl"]
    av, x = sp.symbols("a x", positive=True)
    w0, wa = sp.symbols("w0 wa", real=True)
    lnf = sp.integrate(-3 * (1 + w0 + (1 - x) * wa) / x, (x, 1, av))
    f = sp.lambdify((av, w0, wa), sp.exp(sp.simplify(lnf)), "math")
    _CACHE["cpl"] = (f, str(sp.simplify(sp.exp(lnf))))
    return _CACHE["cpl"]


def net_rows(mut=None):
    """The total null stress of the mean matter per (t.k)^2 / rho_c0, all components at one point (flat; radiation,
    positive, omitted: a lower bound), and dark energy's own share: through today on a grid of a in [1e-4, 1], and in the
    future on a grid of a in (1, 100].  For a constant w < -1 the closed-form zero a_x = [Omega_m/(|1+w|(1 - Omega_m))]
    ^(1/(3|w|)) (deduced) and the matter fraction of its mean below which a uniform dark energy outweighs matter at
    a = 1, f_min = |1+w|(1 - Omega_m)/Omega_m (deduced)."""
    f, _form = _cpl_density()
    Om_pl = observed()["Omega_m"]
    fits = {"Planck18 base LCDM (w = -1)": (Om_pl, -1.0, 0.0),
            "Planck18 w0 eq. (50) central": (Om_pl, PLANCK_W0, 0.0),
            "Planck18 w0 eq. (50) -3 sigma": (Om_pl, PLANCK_W0 - 3 * PLANCK_W0_SIG, 0.0),
            "Planck18 Table 6 Planck+SNe+BAO": (Om_pl, PLANCK_T6[0], PLANCK_T6[1])}
    fits.update(DESI_FITS)
    past = [math.exp(math.log(1e-4) * (1 - i / 4000)) for i in range(4001)]
    future = [] if mut == "today_only" else [math.exp(math.log(100.0) * i / 4000) for i in range(1, 4001)]
    out = {}
    for name, (Om, w0, wa) in fits.items():
        if mut == "flip_w":
            w0, wa = -w0 - 2, -wa
        mins, de_min, fmin, first_neg = float("inf"), float("inf"), float("inf"), None
        for av in past:
            w = w0 + (1 - av) * wa
            de = (1 + w) * (1 - Om) * f(av, w0, wa)
            net = (0.0 if mut == "omit_matter" else Om * av**-3) + de
            mins = min(mins, net)
            de_min = min(de_min, de)
        for av in future:
            w = w0 + (1 - av) * wa
            de = (1 + w) * (1 - Om) * f(av, w0, wa)
            net = (0.0 if mut == "omit_matter" else Om * av**-3) + de
            fmin = min(fmin, net)
            if net < 0 and first_neg is None:
                first_neg = av
        de_at_half = (1 + w0 + 0.5 * wa) * (1 - Om) * f(0.5, w0, wa)
        cross = None
        if wa != 0 and -1 < 1 + (1 + w0) / wa < 1 and (1 + w0) * wa < 0:
            ac = 1 + (1 + w0) / wa
            cross = 1 / ac - 1
        a_x = f_min = None
        if wa == 0 and w0 < -1:
            expo = 1 / 3 if mut == "ax_exponent" else 1 / (3 * abs(w0))
            a_x = (Om / (abs(1 + w0) * (1 - Om))) ** expo
            f_min = abs(1 + w0) * (1 - Om) / Om
        out[name] = {"Omega_m": Om, "w0": w0, "wa": wa, "net_min_through_today": mins, "de_min": de_min,
                     "de_at_a_0.5": de_at_half, "z_phantom_crossing": cross,
                     "net_min_future_a_to_100": fmin if future else None, "future_first_negative_a": first_neg,
                     "a_x_closed_form": a_x, "void_fraction_f_min_at_a_1": f_min}
    return out


PHANTOM_CONST = ("Planck18 w0 eq. (50) central", "Planck18 w0 eq. (50) -3 sigma")


def check_C3(mut=None):
    """Z3'a observed, Z3'c: the total null stress of the mean matter is positive through today (a <= 1) in every READ fit;
    dark energy's own null stress is negative in some (per-component NEC not established); in the future it stays
    positive in six fits and turns negative in exactly the two constant-phantom fits, at the closed-form a_x (grid and
    formula agree); at a = 1 a region whose matter is below f_min of the mean is outweighed by a uniform phantom w."""
    rows = net_rows(mut)
    today = all(r["net_min_through_today"] > 0 for r in rows.values())
    honest = rows["DESI+CMB+DESY5"]["de_at_a_0.5"] < 0 and rows["Planck18 w0 eq. (50) central"]["de_min"] < 0
    neg_future = sorted(n for n, r in rows.items() if r["net_min_future_a_to_100"] is not None
                        and r["net_min_future_a_to_100"] < 0)
    pos_future = [n for n, r in rows.items() if r["net_min_future_a_to_100"] is not None
                  and r["net_min_future_a_to_100"] > 0]
    future_ok = neg_future == sorted(PHANTOM_CONST) and len(pos_future) == 6
    ax_ok = all(rows[n]["a_x_closed_form"] is not None and rows[n]["future_first_negative_a"] is not None
                and abs(rows[n]["future_first_negative_a"] / rows[n]["a_x_closed_form"] - 1) < 2e-3 for n in PHANTOM_CONST)
    w = PLANCK_W0
    thr = -(1 + w) / (-w)
    thr3 = -(1 + w - 3 * PLANCK_W0_SIG) / (-(w - 3 * PLANCK_W0_SIG))
    omb = float(PLANCK_OMB_H2 / PLANCK_H_LITTLE**2)
    ok = today and honest and future_ok and ax_ok and omb > thr and observed()["Omega_m"] > thr3
    return ok, {"fits": rows, "negative_in_future": neg_future, "positive_in_future": len(pos_future),
                "Omega_m_threshold_w0_central_at_a_1": thr, "Omega_m_threshold_w0_-3sigma_at_a_1": thr3,
                "Omega_b_alone": omb, "cpl_density": _cpl_density()[1],
                "label": "computed from READ (Planck 2018 pp.1, 43-44; DESI DR2 pp.20, 23-25); closed forms deduced; "
                         "radiation omitted; mean (homogeneous) densities"}


def check_C4(mut=None):
    """B5': the composite at coincidence (127) with both universes' matter: summed tension +lambda_RS (b5_positive's
    B5a, imported, with its own control); 5D null stress (lambda_c + rho_1 + rho_2) k_y^2 + sum (rho + p)|k_space|^2;
    position 2 as ours: positive; position 2's plane alone negative for crossing rays; a shared-profile thickening
    keeps it at every depth, a per-component one with phantom dark energy does not (control); B5b's smooth wall
    (imported) still tends to the RS plane."""
    b5a = own("b5", "b5a")()
    b5b = own("b5", "b5b")()
    owner_ok = (b5a["shared_nonneg"] and b5a["diff_negative_far"]
                and sp.simplify(b5b["thin_limit_Aprime"] + 1 / sp.Symbol("ell", positive=True)) == 0)
    lamRS, r1, p1, r2, p2 = sp.symbols("lambda_RS rho_1 p_1 rho_2 p_2")
    s, u = sp.symbols("s u", real=True)
    tens = (sp.Rational(4, 3) + sp.Rational(1, 3)) if mut == "sum_wrong" else (sp.Rational(4, 3) - sp.Rational(1, 3))
    kt = sp.sqrt(s**2 + u**2)
    k4 = sp.Matrix([kt, u, 0, 0])
    eta = sp.diag(-1, 1, 1, 1)
    S_low = -tens * lamRS * eta + sp.diag(r1 + r2, p1 + p2, p1 + p2, p1 + p2)
    Skk = sp.expand((k4.T * S_low * k4)[0])
    form_ok = sp.simplify(Skk - ((lamRS + r1 + r2) * s**2 + (r1 + p1 + r2 + p2) * u**2)) == 0
    o = observed()
    eps = 0.5 * (o["H0"] * o["ell"] / o["c"]) ** 2
    Om = o["Omega_m"]
    ours = {"rho": 1.0, "rho_plus_p": Om}                        # units rho_c0, base LCDM (w = -1)
    p2m = {"rho": 1.0, "rho_plus_p": -2 * Om} if mut == "p2_phantom" else dict(ours)   # H-P2-AS-OURS
    coef_s = 1 / eps + ours["rho"] + p2m["rho"]                   # lambda_RS/rho_c0 = 1/eps
    coef_u = ours["rho_plus_p"] + p2m["rho_plus_p"]
    inst_ok = coef_s > 0 and coef_u > 0
    p2_alone = -1 / (3 * eps) + p2m["rho"]                       # position 2's plane alone: -lambda_RS/3 + rho_2
    # thickening: Gaussian profiles of width wd; per-component control: phantom dark energy (DESY5 at a = 0.5) twice as
    # wide as the matter, a tangential ray at depth 3 wd
    f, _ = _cpl_density()
    Omd, w0, wa = DESI_FITS["DESI+CMB+DESY5"]
    wph = w0 + 0.5 * wa
    rm, rde = Omd * 0.5**-3, (1 - Omd) * f(0.5, w0, wa)

    def prof(y, wd):
        return math.exp(-y * y / (wd * wd)) / (wd * math.sqrt(math.pi))
    wde = 1.0 if mut == "control_shared" else 2.0
    ctrl = prof(3.0, 1.0) * rm + prof(3.0, wde) * (1 + wph) * rde
    shared = [prof(y, 1.0) * (rm + (1 + wph) * rde) for y in (0.0, 1.0, 3.0, 6.0)]
    ok = owner_ok and form_ok and inst_ok and p2_alone < 0 and ctrl < 0 and all(x > 0 for x in shared)
    return ok, {"summed_tension": str(tens), "S(k,k)": str(sp.factor(Skk)), "owner_B5a_B5b": owner_ok,
                "instance_coef_k_y^2": coef_s, "instance_coef_k_space^2": coef_u, "p2_alone_coef_k_y^2": p2_alone,
                "per_component_control_at_3w": ctrl, "shared_profile_depths": shared, "w_phantom_used": wph,
                "label": "computed (imported b5_positive.py B5a, B5b); deduced"}


def check_C5(mut=None):
    """Z3'b, against BULK-BALANCE.md result 2: a flat plane beside a bulk of positive dark radiation C that stays static
    (H = 0 and H' = 0).  H' = 0 alone gives (1 + w) sigma = (k_c/a^2 - 2C/a^4) ell/(3 (1 + ell sigma)); H = 0 adds
    sigma^2 + 2 sigma/ell + C/a^4 = 0, so sigma = -1/ell +- sqrt(1/ell^2 - C/a^4) < 0: rho < 0 on both branches; on the
    branch near the RS tension rho + p < 0, on the other lambda + rho < 0 -- either way the 5D null stress
    (lambda + rho) k_y^2 + (rho + p)|k_space|^2 is negative for some null k.  Not our plane's case (READ H0 > 0), but the
    corridor's neighbourhood is left OPEN by it."""
    av, sg, w, kc, C = sp.symbols("a sigma w k_c C", real=True)
    csign = -1 if mut == "c_sign" else 1
    h2 = (sg + 1 / ELL) ** 2 - 1 / ELL**2 + csign * C / av**4 - kc / av**2
    hdot = av / 2 * sp.diff(h2, av) - sp.Rational(3, 2) * (1 + w) * sg * sp.diff(h2, sg)
    x = sp.Symbol("x")                                        # x = (1 + w) sigma = kappa^2 (rho + p)/6
    sol = sp.solve(sp.Eq(sp.expand(hdot).subs(w * sg, x - sg), 0), x)
    want = (kc / av**2 - 2 * C / av**4) * ELL / (3 * (1 + ELL * sg))
    form = len(sol) == 1 and _z(sol[0] - want)
    # H = 0 as well (flat): the two branches of sigma, at a sample point C a^-4 ell^2 = 1/2 (a = ell = 1, C = 1/2)
    pt = {C: sp.Rational(1, 2), av: 1, ELL: 1, kc: 0}
    branches = [] if mut == "no_static" else sp.solve(sp.Eq(h2.subs(pt), 0), sg)
    rows, every_branch_negative = [], len(branches) == 2
    for b in branches:
        xb = sp.nsimplify(sol[0].subs(pt).subs(sg, b)) if sol else sp.nan    # kappa^2 (rho + p)/6
        lam_plus_rho = 1 / sp.Integer(1) + b                                 # kappa^2 (lambda_RS + rho)/6, sigma_lambda = 1/ell
        neg_rho = bool(b < 0)
        some_null_negative = bool(xb < 0) or bool(lam_plus_rho < 0)
        every_branch_negative = every_branch_negative and neg_rho and some_null_negative
        rows.append({"sigma": str(sp.nsimplify(b)), "rho_sign": "negative" if neg_rho else "non-negative",
                     "(1+w)sigma": str(xb), "lambda+rho (units 6/kappa^2)": str(sp.nsimplify(lam_plus_rho))})
    flat = sol[0].subs(kc, 0) if sol else sp.nan
    neg = bool(sp.simplify(flat.subs({C: 1, av: 1, ELL: 1, sg: sp.Rational(1, 10)})) < 0) if sol else False
    ok = form and neg and every_branch_negative
    return ok, {"(1+w)sigma at H'=0": str(sp.factor(sol[0])) if sol else None, "flat_C>0_sign_H'=0_only": "negative"
                if neg else "not negative", "static_branches_H=0_and_H'=0": rows,
                "our_plane": "H0 > 0 (READ PL_abstract): not static in its own Gaussian-normal chart; whether it is "
                             "'static' in 141's sense depends on the chart and is not decided here",
                "label": "computed; deduced (BULK-BALANCE.md result 2 recovered and sharpened)"}


# ======================================================================================== THE CYPHER (196)
CY_OPTS = {"statistics_order": 2, "algebra_budget": 20000}


def determined(cells, coords, by, target):
    """Logic's binary (b6p_scale.py's determined(), imported by path, never copied): does the tuple of coordinates `by`
    fix `target` on these cells?  by = [] asks for one value."""
    return own("b6p", "determined")(cells, coords, by, target)


def _q1_series():
    """Bulk coefficients A3, N3 and the order-0 Gauss residual (E44 at y^0), dust, ell = 1, a = 1, from Part B's series
    (exact sympy expressions; evaluated exactly on the cells)."""
    if "q1" in _CACHE:
        return _CACHE["q1"]
    jet = Jet((0,))
    Ac, Nc, _d = dust_series6()
    s0 = jet.sig[0]
    sub = {AJ: 1, ELL: 1}
    gr = Jet((0,), mode="gr")
    e44gr = _order0_constraints(gr, gr.israel_data())["E44"].subs(sub)
    e44 = _order0_constraints(jet, jet.israel_data())["E44"].subs(sub)
    _CACHE["q1"] = {"s0": s0, "A3": sp.factor(Ac[3].subs(sub)), "N3": sp.factor(Nc[3].subs(sub)), "E44": e44,
                    "E44_gr": e44gr}
    return _CACHE["q1"]


def _fr(e):
    e = sp.nsimplify(sp.simplify(e))
    if not e.is_Rational:
        raise ValueError("not rational: %s" % e)
    return Fr(int(e.p), int(e.q))


def q1_cells(kind, mut=None):
    q = _q1_series()
    s0 = q["s0"]
    cells = []
    for s_ in (0, 1, 2, 3):
        for c_ in (0, 1, 2):
            at = {s0: s_, CDR: c_}
            A3, N3 = _fr(q["A3"].subs(at)), _fr(q["N3"].subs(at))
            use_gr = kind == "gr" or (kind == "law" and mut == "gr_as_law")
            g = _fr((q["E44_gr"] if use_gr else q["E44"]).subs(at))
            if kind == "free":
                for extra in ((0,) if mut == "control_free_off" else (0, 1)):
                    cells.append([Fr(s_), Fr(c_), A3 + extra, N3, g])
            else:
                cells.append([Fr(s_), Fr(c_), A3, N3, g])
    return ["sigma", "C", "A3", "N3", "gauss0"], cells


def q2_cells(kind, mut=None, when="today"):
    rows = net_rows("omit_matter" if (kind == "control" or mut == "omit_matter_in_law") else None)
    f, _ = _cpl_density()
    cells = set()
    grid = (1.0, 0.75, 0.5, 0.25, 0.1) if when == "today" else (1.5, 2.0, 3.0, 5.0)
    if when == "future" and mut == "future_as_today":
        grid = (1.0, 0.75, 0.5, 0.25, 0.1)
    for name, r in rows.items():
        for av in grid:
            w = r["w0"] + (1 - av) * r["wa"]
            de = (1 + w) * (1 - r["Omega_m"]) * f(av, r["w0"], r["wa"])
            mat = 0.0 if (kind == "control" or mut == "omit_matter_in_law") else r["Omega_m"] * av**-3
            fm = r["Omega_m"] * av**-3 / (r["Omega_m"] * av**-3 + (1 - r["Omega_m"]) * f(av, r["w0"], r["wa"]))
            sg = (lambda x: 0 if abs(x) < 1e-12 else (1 if x > 0 else -1))
            cells.add((Fr(w).limit_denominator(1000), Fr(fm).limit_denominator(1000), sg(de), sg(mat + de)))
    return ["w", "f_matter", "de_sign", "net_sign"], [list(c) for c in sorted(cells)]


def run_index(title, coords, cells, witness, rosters=None):
    cy = cypher()
    vo = {c: sorted({cl[i] for cl in cells}, key=float) for i, c in enumerate(coords)}
    out = {"index": title, "coords": coords, "cells": len(cells), "rosters": {}}
    rows = keys = None
    for rn in (rosters or sorted(cy.ROSTERS)):
        ix = cy.Index(title, coords, cells, vo, {"analysis": {"speaks": True, "witness": witness}})
        res = cy.run(ix, rn, CY_OPTS)
        rows, keys = cy.coordinate_report(ix)
        out["rosters"][rn] = {
            "verdicts": [{"language": v.language, "state": v.state, "status": v.status, "admitted": v.admitted,
                          "E": v.E} for v in res["_verdicts"]],
            "agree": res["languages_agree"], "all_E_zero": res["all_E_zero"], "degenerate": res["degenerate"],
            "bearing": res["operator_bearing_measured"]}
    out["adds_nothing"] = [r["coordinate"] for r in rows if r["adds_nothing"]]
    out["keys"] = keys
    return out


def _notrun_kept(r):
    st = r["rosters"].get("20.2")
    if not st:
        return False
    states = {v["language"]: v["state"] for v in st["verdicts"]}
    return all(states.get(l) == "NOT-RUN" for l in ("arithmetic", "calculus", "logic", "constraint-language"))


def check_Q1(mut=None):
    """The cypher, Q1 (B1', B2'): does each plane's own data fix the bulk off it, with Gauss met?  Law: (A3, N3) fixed by
    (sigma, C), by neither alone; gauss0 = 0 on every cell.  Controls: a bulk datum of its own flips the first; GR's
    Friedmann flips the second.  Every roster run; NOT-RUN kept."""
    co, law = q1_cells("law", mut)
    _, free = q1_cells("free", mut)
    _, gr = q1_cells("gr", mut)
    q = _q1_series()
    wl = ("continuous law: A3 = %s, N3 = %s, gauss0 = 0, polynomials in (sigma, C), exact on every cell (Part B, "
          "computed)" % (q["A3"], q["N3"]))
    rl = run_index("Q1 bulk from the plane's data (dust, ell = a = 1)", co, law, wl)
    rf = run_index("Q1 control: a bulk datum of its own", co, free,
                   "the same law with A3 + q, q in {0, 1} a bulk datum on no plane coordinate (two bulks per state)")
    rg = run_index("Q1 control: GR's Friedmann data", co, gr,
                   "the same A3, N3; gauss0 = %s, the order-0 Gauss residual of GR-Friedmann data" % q["E44_gr"])
    b = {"A3,N3 by sigma,C (law)": determined(law, co, ["sigma", "C"], "A3") and determined(law, co, ["sigma", "C"], "N3"),
         "A3 by sigma alone (law)": determined(law, co, ["sigma"], "A3"),
         "A3 by C alone (law)": determined(law, co, ["C"], "A3"),
         "gauss0 one value (law)": determined(law, co, [], "gauss0") and law[0][4] == 0,
         "A3 by sigma,C (free control)": determined(free, co, ["sigma", "C"], "A3"),
         "gauss0 one value zero (GR control)": determined(gr, co, [], "gauss0") and gr[0][4] == 0}
    every = all(set(r["rosters"]) == set(cypher().ROSTERS) for r in (rl, rf, rg))
    ok = (b["A3,N3 by sigma,C (law)"] and not b["A3 by sigma alone (law)"] and not b["A3 by C alone (law)"]
          and b["gauss0 one value (law)"] and not b["A3 by sigma,C (free control)"]
          and not b["gauss0 one value zero (GR control)"] and every and _notrun_kept(rl))
    return ok, {"binaries": b, "law": _cy_brief(rl), "free_control": _cy_brief(rf), "gr_control": _cy_brief(rg),
                "A3": str(_q1_series()["A3"]), "N3": str(_q1_series()["N3"]),
                "label": "computed (tools/cypher.py imported; binaries by b6p_scale.py's determined(), imported; "
                         "H-CYPHER-MATTER-INDEX, the board's encoding)"}


def check_Q2(mut=None):
    """The cypher, Q2 (Z3'a, Z3'c): is the sign of the total null stress one value on the READ fits through today, whatever
    dark energy's own sign?  Law: net_sign one value (+1), de_sign not; control (matter omitted): net_sign varies.  The
    future (a in {1.5, 2, 3, 5}): net_sign is NOT one value, and every negative cell has w < -1 (Z3'c is nature's)."""
    co, law = q2_cells("law", mut)
    _, ctl = q2_cells("control", mut)
    _, fut = q2_cells("law", mut, when="future")
    lawtxt = ("continuous law in a: net(a) = Omega_m a^-3 + (1 + w(a))(1 - Omega_m) %s, w(a) = w0 + (1 - a) wa "
              "(READ fits; computed)" % _cpl_density()[1])
    rl = run_index("Q2 total null stress on the READ fits, through today", co, law, lawtxt)
    rc = run_index("Q2 control: matter omitted", co, ctl, "the same law with the matter term removed (control)")
    rf = run_index("Q2 the same fits in the future (a = 1.5 to 5)", co, fut, lawtxt)
    b = {"net_sign one value (law, through today)": determined(law, co, [], "net_sign"),
         "net_sign value (law, through today)": sorted({c[3] for c in law}),
         "de_sign one value (law)": determined(law, co, [], "de_sign"),
         "net_sign one value (control)": determined(ctl, co, [], "net_sign"),
         "net_sign one value (future)": determined(fut, co, [], "net_sign"),
         "every future negative cell has w < -1": all(c[0] < -1 for c in fut if c[3] < 0) and any(c[3] < 0 for c in fut)}
    every = all(set(r["rosters"]) == set(cypher().ROSTERS) for r in (rl, rc, rf))
    ok = (b["net_sign one value (law, through today)"] and b["net_sign value (law, through today)"] == [1]
          and not b["de_sign one value (law)"] and not b["net_sign one value (control)"]
          and not b["net_sign one value (future)"] and b["every future negative cell has w < -1"]
          and every and _notrun_kept(rl))
    return ok, {"binaries": b, "law": _cy_brief(rl), "control": _cy_brief(rc), "future": _cy_brief(rf),
                "label": "computed (tools/cypher.py imported; binaries by b6p_scale.py's determined(), imported; "
                         "H-CYPHER-MATTER-INDEX, the board's encoding)"}


def _cy_brief(r):
    return {"cells": r["cells"], "adds_nothing": r["adds_nothing"], "keys": r["keys"],
            "1173": {v["language"]: (v["state"], v["E"]) for v in r["rosters"]["1173"]["verdicts"]},
            "20.2": {v["language"]: v["state"] for v in r["rosters"]["20.2"]["verdicts"]},
            "agree_1173": r["rosters"]["1173"]["agree"], "degenerate": r["rosters"]["1173"]["degenerate"]}


# ======================================================================================== the lemmas, as edited
# Each lemma: its status, the claim the status is for ("statement"), every input that claim rests on with its status,
# and, apart from the claim, what applying it to our plane or to position 2 needs ("instance").  Every board reading
# (H-...) named in a statement must be a declared input (guard G1); an instance's readings are not part of the claim.
BOARD_READINGS = {"H-OUR-PLANE-IS-FRW": "READING", "H-DE-IN-TAU": "READING", "H-P2-AS-OURS": "READING",
                  "H-EXPANSION-IN-SURFACE": "READING", "H-CYPHER-MATTER-INDEX": "READING", "H-README-HELD": "OPEN"}
AXIOM_ITEMS = {117, 120, 127, 129, 130, 139, 183, 184}          # M's rulings used as axioms here (141, 187 never)
LEMMAS = [
    {"name": "B1'", "edits": "B1", "status": "PROVED",
     "statement": "a plane carrying a perfect fluid on the FRW metric (any spatial curvature, any dark-radiation constant "
                  "C; Z2, or each side its own ell) meets Codazzi iff its matter is conserved (SMS (21)) and meets Gauss "
                  "iff it obeys its brane Friedmann equation, the trace of SMS (17) for any tau; the matter-free plane "
                  "is the limit rho -> 0, where the Gauss right side is localbulk.gauss_rhs and R(4) = 0 (B1); with 184, "
                  "129 (1), 130 (1): each plane carries its own universe's matter and the corridor adds none",
     "instance": "that our plane with its observed matter is such a plane is H-OUR-PLANE-IS-FRW (READING); "
                 "observation cannot tell it from four-dimensional gravity: the brane terms are eps_total = 2.65e-61 "
                 "of the tension at the table-top ell (all of tau, under H-DE-IN-TAU), eps_matter = 8.36e-62 (A8)",
     "inputs": [("SMS eqs. (2), (10), (13)-(21), (28)", "READ"), ("184 with 129 (1), 130 (1)", "AXIOM"),
                ("localbulk.gauss_rhs (B1's own Gauss form)", "PROVED"), ("checks A1-A7", "computed")],
     "where": "lemmas/b1_matter.py A1-A8 (with the cypher's Q1)"},
    {"name": "B2'", "edits": "B2", "status": "PROVED",
     "statement": "for analytic plane data meeting B1''s conditions (Z2 Israel data, conserved matter, the brane "
                  "Friedmann equation) -- e.g. the FRW model plane with dust, or dust + w = -1 -- a local vacuum bulk "
                  "off the plane exists and is unique among analytic ones (Dahia-Romero Lemmas 1-2, Theorem 2, READ); "
                  "computed to order 6 in y (constraints 0 through y^5), three controls with inconsistent Israel data "
                  "failing; for C = 0, exactly: the bulk off the FRW model plane is pure AdS5, with no corridor in it",
     "instance": "for our real plane (inhomogeneous, not known to be analytic) existence is OPEN; that the FRW model "
                 "plane is ours is H-OUR-PLANE-IS-FRW (READING); the corridor's own local bulk is B2t's",
     "inputs": [("B1'", "PROVED"), ("Dahia-Romero gr-qc/0109076v2 pp.8-12, 16", "READ"), ("checks B1-B4", "computed")],
     "where": "lemmas/b1_matter.py B1-B4 (with the cypher's Q1)"},
    {"name": "B2t", "edits": "B2", "status": "PROVED",
     "statement": "B2's instance for the corridor-carrying plane: the local bulk beneath eq. (17) read on the plane as the "
                  "corridor's mouth -- F1-AUDIT.md's lemma (localbulk.py L3-L4), carried here, not computed here; "
                  "PROVED as a conditional on M1",
     "instance": "", "carried": "lemmas/F1-AUDIT.md (B2t)",
     "inputs": [("F1 / M1: eq. (17) as the plane's reading of the corridor's mouth (seated (G), 187)", "OPEN"),
                ("localbulk.py L3-L4", "PROVED")],
     "where": "lemmas/F1-AUDIT.md, lemmas/f1_audit.py (not this instrument)"},
    {"name": "Z3'a", "edits": "Z3 (a part)", "status": "DERIVED",
     "statement": "away from the corridor and through today: the vacuum bulk gives R(k,k) = 0 for every null k (axioms.py's "
                  "Z3); the FRW model plane's 5D null stress is (lambda + rho) k_y^2 + (rho + p)|k_space|^2, non-negative "
                  "for every null k iff lambda + rho >= 0 and rho + p >= 0 for its total stress-energy; the mean matter "
                  "of every READ fit (Planck 2018, DESI DR2) has rho + p > 0 at every a in [1e-4, 1] -- so 117/120's "
                  "'An NEC is never violated' is consistent there; dark energy by itself is not shown to obey it",
     "instance": "applied to our plane through H-OUR-PLANE-IS-FRW (READING); the criterion is the null stress of all "
                 "the stress present at each point, the one axioms.py's Z3 evaluates (the per-component reading and "
                 "the withdrawn H-NET-OVER-COMPONENTS are not used)",
     "inputs": [("117, 120: An NEC is never violated", "AXIOM"),
                ("axioms.py derive_z3: the vacuum bulk's R(k,k) = 0", "DERIVED"),
                ("B1' (the FRW plane with its matter)", "PROVED"), ("Planck 2018, DESI DR2 fits", "READ"),
                ("checks C1-C3 (consistency checks)", "computed")],
     "where": "lemmas/b1_matter.py C1-C3 (with the cypher's Q2)"},
    {"name": "Z3'b", "edits": "Z3 (a part)", "status": "OPEN",
     "statement": "rays that meet the corridor or run beside it: zero net null energy along each such ray (183, 'never "
                  "violated as a pair') needs a vacuum bulk carrying the corridor (B3/B4) and either the exact partner "
                  "(F5, OPEN again since 194 withdrew 193) or the README held by the horizon (H-README-HELD, 195, to be "
                  "computed); and a flat plane static beside positive dark radiation has rho < 0 and a negative 5D null "
                  "stress for some null k (C5)",
     "instance": "",
     "inputs": [("183: never violated as a pair", "AXIOM"), ("B3/B4: a vacuum bulk carrying the corridor", "OPEN"),
                ("F5: the exact +/- null pair (194)", "OPEN"), ("H-README-HELD (195: to be computed)", "OPEN"),
                ("C5's configuration beside the corridor (BULK-BALANCE, E-PASS)", "OPEN"), ("check C5", "computed")],
     "where": "lemmas/b1_matter.py C5; BULK-BALANCE.md, E-PASS"},
    {"name": "Z3'c", "edits": "Z3 (a part)", "status": "NATURE",
     "statement": "the FRW model plane's total null stress in the future and in sparse regions today: positive for every a "
                  "in (1, 100] in six READ fits; negative in the two constant-phantom fits beyond a_x = 2.48 (Planck eq. "
                  "(50) central) and 1.49 (its -3 sigma), and eventually for every constant w < -1 (deduced); at a = 1 a "
                  "region whose matter is below 6.1% (central) or 26% (-3 sigma) of the mean is outweighed by a uniform "
                  "phantom dark energy -- there Z3 rests on w_DE >= -1, a premise nature fixes",
     "instance": "",
     "inputs": [("w_DE >= -1 (asymptotically, and wherever matter is sparse)", "NATURE"),
                ("Planck 2018, DESI DR2 fits", "READ"), ("checks C3, Q2", "computed")],
     "where": "lemmas/b1_matter.py C3 (with the cypher's Q2)"},
    {"name": "B5'a", "edits": "B5 (a part)", "status": "DERIVED",
     "statement": "at coincidence (127) the summed tension +lambda_RS (B5a) with both universes' matter gives the 5D null "
                  "stress (lambda_RS + rho_1 + rho_2) k_y^2 + sum (rho + p)|k_space|^2, non-negative for every null k iff "
                  "rho_1 + rho_2 >= -lambda_RS and sum (rho + p) >= 0 -- a conditional; it does not by itself discharge "
                  "139 (2)'s 'positive, and you have to prove it'",
     "instance": "exhibited with position 2's matter measuring as ours (H-P2-AS-OURS, an example only); position 2's "
                 "plane alone is negative for crossing rays",
     "inputs": [("127 (1), 139 (1), 184", "AXIOM"), ("b5_positive.py B5a", "DERIVED"), ("check C4", "computed")],
     "where": "lemmas/b1_matter.py C4"},
    {"name": "B5'p", "edits": "B5 (a part)", "status": "OPEN",
     "statement": "position 2's matter meets B5'a's antecedent (summed with ours, rho + p >= 0 along each ray and the "
                  "density above -lambda_RS): position 2's matter is unknown; only ratios are known (ITEM185)",
     "instance": "",
     "inputs": [("position 2's matter (ITEM185: only ratios known)", "OPEN"), ("B5'a", "DERIVED")],
     "where": "lemmas/ITEM185-MATTER-ROUND.md"},
    {"name": "B5'b", "edits": "B5 (a part)", "status": "OPEN",
     "statement": "a smooth wall carrying both universes' matter that keeps null energy at every point exists: B5b's exact "
                  "wall is matter-free (a limit under 184); with matter only algebraic one-profile thickenings are shown, "
                  "not Einstein solutions, and a per-component thickening with phantom dark energy goes negative (C4)",
     "instance": "",
     "inputs": [("an exact thick wall with matter", "OPEN"), ("b5_positive.py B5b (matter-free)", "DERIVED"),
                ("check C4", "computed")],
     "where": "lemmas/b1_matter.py C4; b5_positive.py B5b"},
]
SLOTS = {"B1": ["B1'"], "B2": ["B2'", "B2t"], "Z3": ["Z3'a", "Z3'b", "Z3'c"], "B5": ["B5'a", "B5'p", "B5'b"]}
EXPECT_GREEN = {"B1'": True, "B2'": True, "B2t": False, "Z3'a": True, "Z3'b": False, "Z3'c": False, "B5'a": True,
                "B5'p": False, "B5'b": False}
STILL_ON_F2 = {"B3": "OPEN (equivalent to B4)", "B4d": "OPEN (its matter-free stages are limits under 184)"}
F1_STILL = ["H2", "O1", "O2", "Z1", "Z2", "E4", "B4b", "B3", "B4d", "B2t (the corridor's own local bulk)"]
H_TOKEN = re.compile(r"H-[A-Z0-9]+(?:-[A-Z0-9]+)*")


def green_of(lem, extra_inputs=()):
    inputs = list(lem["inputs"]) + list(extra_inputs)
    return lem["status"] in GREEN and all(st in GREEN_INPUT for _, st in inputs)


def check_G1(mut=None):
    """Guards (STRUCTURAL bookkeeping over declared inputs, not a computation of greenness): every M quote verbatim inside
    M's own spans of its item ("M, verbatim:" / "M chose:" up to "Recorded as given"), the seated (Z) wording inside 187's
    question; every READ row has a source, page(s) and a quote; statuses from the allowed set; every board reading named
    in a lemma's statement is a declared input, and every one named in an instance is a registered reading; AXIOM inputs
    cite only M's rulings (never 141's suggestion or 187's seating); the green map is the expected one (the OPEN and
    NATURE parts non-green); no green lemma has an F1 or F2 input; no owner attribute outside the allowlist and no
    eq. (17) carrier used; every row's label from the allowed set."""
    spans, blocks = ruling_spans(), ruling_blocks()
    words = dict(M_WORDS)
    if mut == "planted_mword":
        words["184"] = "There are no matter-free planes"
    if mut == "mword_from_narrative":
        words["184"] = "H-NO-MATTER-FREE-PLANES (every plane carries matter"
    bad_words = [k for k, v in words.items()
                 if re.sub(r"\s+", " ", v) not in spans.get(int(re.match(r"\d+", k).group()), "")]
    q187 = blocks.get(187, "").split("M chose:")[0]
    bad_seated = [k for k, v in SEATED_WORDING.items() if re.sub(r"\s+", " ", v) not in q187]
    bad_reads = [k for k, (src, pg, q) in READS.items()
                 if not (src and q and (isinstance(pg, int) and pg > 0 or isinstance(pg, tuple) and pg
                                        and all(isinstance(x, int) and x > 0 for x in pg)))]
    lems = [dict(l, inputs=list(l["inputs"])) for l in LEMMAS]
    by = {l["name"]: l for l in lems}
    if mut == "planted_F2":
        by["B1'"]["inputs"].append(("F2: the plane matter-free", "OPEN"))
    if mut == "planted_status":
        by["B2'"]["status"] = "GREEN"
    if mut == "drop_reading":
        by["Z3'b"]["inputs"] = [i for i in by["Z3'b"]["inputs"] if not i[0].startswith("H-README-HELD")]
    if mut == "drop_open_input":
        by["B2t"]["inputs"] = [i for i in by["B2t"]["inputs"] if i[1] != "OPEN"]
    if mut == "axiom_187":
        by["Z3'a"]["inputs"].append(("seated (Z) (183, 187 (3))", "AXIOM"))
    if mut == "axiom_141":
        by["B5'a"]["inputs"].append(("141: the planes static", "AXIOM"))
    bad_status = [l["name"] for l in lems if l["status"] not in STATUSES]
    undeclared = sorted({(l["name"], h) for l in lems for h in H_TOKEN.findall(l["statement"])
                         if not any(n.startswith(h) for n, _ in l["inputs"])})
    unregistered = sorted({(l["name"], h) for l in lems for h in H_TOKEN.findall(l.get("instance", ""))
                           if h not in BOARD_READINGS and h != "H-NET-OVER-COMPONENTS"})
    bad_axioms = [(l["name"], n) for l in lems for n, st in l["inputs"] if st == "AXIOM"
                  and not set(int(x) for x in re.findall(r"\b(\d{3})\b", n)) <= AXIOM_ITEMS]
    greens = {l["name"]: green_of(l) for l in lems}
    f12 = [l["name"] for l in lems if greens[l["name"]] and any(n.startswith(("F1", "F2")) for n, _ in l["inputs"])]
    f2_any = [l["name"] for l in lems if any(n.startswith("F2") for n, _ in l["inputs"])]
    used = set(_USED)
    if mut == "planted_eq17":
        used.add(("localbulk", "ricci_scalar"))
    outside = sorted(used - OWNER_ALLOW)
    eq17 = sorted(used & EQ17_CARRIERS)
    rows = compute_rows_labels()
    if mut == "planted_label":
        rows = rows + ["positive"]
    bad_labels = [r for r in rows if not any(r.startswith(l) for l in LABELS)]
    ok = (not bad_words and not bad_seated and not bad_reads and not bad_status and not undeclared and not unregistered
          and not bad_axioms and greens == EXPECT_GREEN and not f12 and not f2_any and not outside and not eq17
          and not bad_labels)
    return ok, {"bad_words": bad_words, "bad_seated": bad_seated, "bad_reads": bad_reads, "bad_status": bad_status,
                "undeclared_readings": undeclared, "unregistered_readings": unregistered, "bad_axioms": bad_axioms,
                "green": greens, "green_as_expected": greens == EXPECT_GREEN, "F1_or_F2_in_green": f12,
                "F2_anywhere": f2_any, "owner_attrs_used": sorted(used), "outside_allowlist": outside,
                "eq17_carriers_used": eq17, "bad_labels": bad_labels,
                "label": "STRUCTURAL (bookkeeping over the declared inputs)"}


# ---------------------------------------------------------------------------------------- G2: the count
# The board's reading of each lemma's foundational inputs, as the item-192 cypher audit recorded it (its own scratch
# list; inputs F1-F6 there, all non-green).  Statuses are cross-checked against warptheorem.py's LEMMAS, imported by path.
AUDIT_INPUTS = {
    "G1": "", "G2": "", "G3": "", "H1": "", "H2": "F1", "O1": "F1", "O2": "F1", "O3": "F4 F5", "Z1": "F1", "Z2": "F1",
    "Z3": "F2", "B1": "F1 F2", "B2": "F1 F2", "B3": "F1 F3 F4 F5", "B4a": "", "B4c": "F3", "B4b": "F1 F4",
    "B4d": "F1 F2 F4 F5", "B5": "F2", "B6": "", "B6'": "F6", "B7": "F4 F5", "I1": "", "I2": "", "E1": "", "E2": "",
    "E3": "", "E4": "F1", "R0": "", "R1": "", "R2": "", "R3": "", "R4": "", "R5": ""}
AUDIT_STATUS = {
    "G1": "DERIVED", "G2": "PROVED", "G3": "PROVED", "H1": "PROVED", "H2": "DERIVED", "O1": "PROVED", "O2": "PROVED",
    "O3": "OPEN", "Z1": "PROVED", "Z2": "PROVED", "Z3": "DERIVED", "B1": "PROVED", "B2": "PROVED", "B3": "OPEN",
    "B4a": "PROVED", "B4c": "READING", "B4b": "READING", "B4d": "OPEN", "B5": "DERIVED", "B6": "PROVED", "B6'": "NATURE",
    "B7": "DERIVED", "I1": "DERIVED", "I2": "PROVED", "E1": "DERIVED", "E2": "DERIVED", "E3": "DERIVED", "E4": "PROVED",
    "R0": "DEFINITION", "R1": "DEFINITION", "R2": "DEFINITION", "R3": "PROVED", "R4": "DERIVED", "R5": "DERIVED"}
EXPECT_COUNT = {"before_audit_rule": (17, 34), "before_strict": (14, 34), "per_slot_audit_rule": (18, 34),
                "per_slot_strict": (15, 34), "after_splits_audit_rule": (21, 39), "after_splits_strict": (18, 39)}


def chain_count(mut=None):
    rules = {"audit_rule": GREEN + ("DEFINITION",), "strict": GREEN}
    if mut == "definition_strict":
        rules["strict"] = GREEN + ("DEFINITION",)
    by = {l["name"]: l for l in LEMMAS}
    new = {n: green_of(by[n]) for n in by}
    if mut == "b2t_green":
        new["B2t"] = True
    out = {}
    for rn, rule in rules.items():
        old = {n: AUDIT_STATUS[n] in rule and not AUDIT_INPUTS[n].split() for n in AUDIT_STATUS}
        out["before_" + rn] = (sum(old.values()), len(old))
        slot = dict(old)
        for s_, parts in SLOTS.items():
            slot[s_] = (any if mut == "slot_any" else all)(new[p] for p in parts)
        out["per_slot_" + rn] = (sum(slot.values()), len(slot))
        split = {n: g for n, g in old.items() if n not in SLOTS}
        split.update({p: new[p] for parts in SLOTS.values() for p in parts})
        out["after_splits_" + rn] = (sum(split.values()), len(split))
    return out


def check_G2(mut=None):
    """The count (deduced from the item-192 audit's list): the chain's lemmas green before and after these edits, under
    the audit's rule (DEFINITION counted green) and the strict rule (PROVED, DERIVED, AXIOM only); per original slot (a
    slot green only if every part is green) and per lemma after the splits.  warptheorem.py's statuses cross-checked
    (informational: an integration elsewhere may move them)."""
    cnt = chain_count(mut)
    wt = {}
    try:
        for row in own("warp", "LEMMAS"):
            wt[row[1].split()[0]] = row[2]
    except Exception as exc:                                         # informational only
        wt = {"error": repr(exc)[:120]}
    diff = {n: (AUDIT_STATUS[n], wt.get(n)) for n in AUDIT_STATUS if wt.get(n) != AUDIT_STATUS[n]}
    ok = cnt == EXPECT_COUNT
    return ok, {"count": {k: "%d of %d" % v for k, v in cnt.items()},
                "warptheorem_status_differences": diff or "none",
                "label": "deduced (the audit's inputs are the board's reading); statuses STRUCTURAL"}


def ruling_spans():
    """M's own words in each numbered item: the text after "M, verbatim:" or "M chose:" up to "Recorded as given",
    whitespace normalised (the board's title, question and narrative excluded)."""
    out = {}
    for k, v in ruling_blocks().items():
        parts = []
        for m in re.finditer(r"(?:M, verbatim:|M chose:)(.*?)(?:Recorded as given|$)", v):
            parts.append(m.group(1))
        out[k] = " ".join(parts)
    return out


def ruling_blocks():
    """Each numbered item of the rulings file, its bold title removed (the board's), whitespace normalised."""
    blocks, cur, buf = {}, None, []
    for line in open(RULINGS, encoding="utf-8"):
        m = re.match(r"^\s*(\d+)\. \*\*", line)
        if m:
            if cur is not None:
                blocks[cur] = " ".join(buf)
            cur, buf = int(m.group(1)), [re.sub(r"^\s*\d+\. \*\*.*?\*\*", "", line)]
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        blocks[cur] = " ".join(buf)
    return {k: re.sub(r"\s+", " ", v) for k, v in blocks.items()}


def compute_rows_labels():
    return [CHECKS[c][3] for c in CHECKS]


CHECKS = {
    "A1": (check_A1, "B1': Israel data for a perfect fluid (SMS (16))",
           [("no_trace", "the 1/3 trace term dropped from SMS (16)"), ("no_z2_half", "Z2's 1/2 dropped (the full jump)")],
           "computed; READ SMS (16) p.3"),
    "A2": (check_A2, "B1': Codazzi = -(kappa^2/2) D.tau; conserved dust passes, rho ~ a^-2 fails",
           [("drop_connection", "the divergence taken without its Christoffel terms"),
            ("no_trace", "Israel without the trace term")],
           "computed; READ SMS (2), (10), (21)"),
    "A3": (check_A3, "B1': Gauss identically on the brane-Friedmann plane (any C); its first integral",
           [("no_rho2", "the Friedmann equation without kappa^4 rho^2/36"), ("gauss_sign", "the K terms' sign flipped"),
            ("lam4_wrong", "Lambda4 = Lambda5/2 (the tension's square dropped)"), ("no_trace", "Israel without trace")],
           "computed; READ SMS (18)"),
    "A4": (check_A4, "B1': trace of SMS (17) = Gauss (generic tau); SMS (28) from (20); E on FRW traceless, ~ C",
           [("pi_coeff", "SMS (20)'s 1/8 replaced by 1/4"), ("GN_wrong", "8 pi G_N = kappa^4 lambda/3")],
           "computed; READ SMS (17)-(20), (28)"),
    "A5": (check_A5, "B1': the matter-free limit is localbulk.gauss_rhs (imported); R(4) = 0 at the RS tension",
           [("c_wrong", "compared at c = -kappa^2 lambda/3"), ("off_rs", "the tension off the RS value")],
           "computed; imported localbulk.gauss_rhs"),
    "A6": (check_A6, "B1': each side its own ell -- per-side Gauss, conserved jump, lambda = (3/kappa^2)(1/ell_+ + 1/ell_-)",
           [("kt_eq_kx", "K^t_t := K^x_x (Codazzi dropped)"), ("same_sign", "both sides' K with one sign")],
           "computed; imported localbulk.gauss_rhs"),
    "A7": (check_A7, "B1': dark energy in tau (w = -1) or in the tension: one equation",
           [("double_count", "dark energy counted in both")], "computed; READ SMS p.3"),
    "A8": (check_A8, "B1': our plane's matter is eps = Omega (H0 ell/c)^2/2 of its tension (two routes; < 1e-60)",
           [("factor_two", "the 1/2 dropped from the formula"), ("c_kms", "c in km/s")],
           "computed (cosmo.py, exactE.py, b4d_stage2.py)"),
    "B1": (check_B1, "B2': dust to order 6, LCDM to order 4 -- constraints 0 through y^(N-1) (uniqueness STRUCTURAL)",
           [("skip_solve", "A_(j+2), N_(j+2) set to 0 instead of solved"),
            ("kx_no_matter", "Israel data without the matter (inconsistent)"), ("L5_sign", "Lambda5 = +6/ell^2")],
           "computed; READ Dahia-Romero pp.8-12"),
    "B2": (check_B2, "B2' controls: doubled matter, GR Friedmann, non-conserved -- each fails a constraint",
           [("control_made_consistent", "the doubled-matter control given single matter")], "computed"),
    "B3": (check_B3, "B2' C = 0: exact closed bulk, = series to order 6, maximally symmetric (AdS5); a = 0 at y*",
           [("beta_no_rho", "beta = -1 (the matter dropped)"), ("n_static", "the lapse's (1 + w) term dropped"),
            ("curv_scale", "compared with curvature -1/(2 ell)^2")],
           "computed (exact, sympy); deduced"),
    "B4": (check_B4, "B2': the dust plane a(t) explicit", [("gr_dust", "GR's dust a^3 ~ t^2 used")], "computed"),
    "C1": (check_C1, "Z3'a: vacuum bulk R(k,k) = 0 (axioms.py, imported); a timelike control is not 0",
           [("control_null", "the control given a null vector")], "computed (imported axioms.py)"),
    "C2": (check_C2, "Z3'a: S(k,k) = (lambda + rho) k_y^2 + (rho + p)|k|^2; pi(k,k) = rho (rho + p)(t.k)^2/6",
           [("lambda_sign", "the tension's sign flipped in S"), ("pi_tt", "SMS (20)'s -1/4 tau tau replaced by -1/2")],
           "computed; READ SMS"),
    "C3": (check_C3, "Z3'a/Z3'c: total null stress positive through today in every READ fit (dark energy alone is "
                     "not); future negative in exactly the two constant-phantom fits, at the closed-form a_x",
           [("omit_matter", "the matter left out of the net"), ("flip_w", "w reflected about -1"),
            ("today_only", "the future grid dropped"), ("ax_exponent", "a_x's exponent 1/3 instead of 1/(3|w|)")],
           "computed from READ Planck 2018, DESI DR2"),
    "C4": (check_C4, "B5'a: composite with both universes' matter; p2 alone negative; B5'b: shared vs per-component",
           [("sum_wrong", "the tensions summed as 4/3 + 1/3"), ("control_shared", "the per-component control shared"),
            ("p2_phantom", "position 2's matter net-negative, twice ours")],
           "computed (imported b5_positive.py); deduced"),
    "C5": (check_C5, "Z3'b vs BULK-BALANCE: a flat plane static (H = 0, H' = 0) beside C > 0 has rho < 0 and a "
                     "negative 5D null stress on both branches",
           [("c_sign", "the dark radiation's sign flipped"), ("no_static", "H = 0 not imposed")], "computed; deduced"),
    "Q1": (check_Q1, "the cypher Q1: the bulk fixed by the plane's data; Gauss met; controls flip",
           [("control_free_off", "the free-bulk control without its extra datum"),
            ("gr_as_law", "GR-Friedmann data used in the law index")],
           "computed (tools/cypher.py, imported); the encoding the board's"),
    "Q2": (check_Q2, "the cypher Q2: total null-stress sign one value through today, dark energy's not; the future not",
           [("omit_matter_in_law", "matter omitted in the law index"),
            ("future_as_today", "the future index given today's epochs")],
           "computed (tools/cypher.py, imported); the encoding the board's"),
    "G1": (check_G1, "guards: M's words in M's spans; READ pages; statuses; readings declared; axioms M's; green map; "
                     "no eq. (17) carrier",
           [("planted_mword", "184 re-typed with a hyphen"),
            ("mword_from_narrative", "a 'quote' taken from the board's narrative of 184"),
            ("planted_F2", "F2 planted among B1''s inputs"),
            ("planted_status", "B2' given status 'GREEN'"), ("planted_eq17", "localbulk.ricci_scalar recorded as used"),
            ("planted_label", "a row labelled 'positive'"),
            ("drop_reading", "H-README-HELD dropped from Z3'b's inputs while its statement names it"),
            ("drop_open_input", "B2t's OPEN input (F1 / M1) dropped, so it would turn green"),
            ("axiom_187", "187 (3)'s seating planted as an AXIOM input of Z3'a"),
            ("axiom_141", "141's suggestion planted as an AXIOM input of B5'a")],
           "STRUCTURAL"),
    "G2": (check_G2, "the count: before and after, per slot and after the splits, under the audit's and the strict rule",
           [("b2t_green", "B2t counted green"), ("definition_strict", "DEFINITION counted under the strict rule"),
            ("slot_any", "a slot counted green if any part is")],
           "deduced (the audit's inputs the board's reading)"),
}


def _clean(x):
    if isinstance(x, dict):
        return {str(k): _clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_clean(v) for v in x]
    if isinstance(x, (bool, int, float, str)) or x is None:
        return x
    if isinstance(x, Fr):
        return str(x)
    return str(x)


def compute():
    out = {"checks": {}, "lemmas": [], "reads": READS, "m_words": M_WORDS, "seated_wording": SEATED_WORDING,
           "board_readings": BOARD_READINGS}
    for cid, (fn, what, _m, label) in CHECKS.items():
        ok, det = fn(None)
        out["checks"][cid] = {"ok": ok, "what": what, "label": label, "detail": _clean(det)}
    for l in LEMMAS:
        out["lemmas"].append({"name": l["name"], "edits": l["edits"], "status": l["status"], "green": green_of(l),
                              "statement": l["statement"], "instance": l.get("instance", ""), "inputs": l["inputs"],
                              "where": l["where"], "label": "STRUCTURAL (status from the checks above)"})
    out["slots"] = {s_: {"parts": p, "green": all(green_of(next(l for l in LEMMAS if l["name"] == q)) for q in p)}
                    for s_, p in SLOTS.items()}
    out["F1"] = {"enters": ["B2t (directly)", "Z3'b (through B3/B4)"],
                 "enters_none_of": ["B1'", "B2'", "Z3'a", "Z3'c", "B5'a", "B5'p", "B5'b"],
                 "still_rests_on_F1": F1_STILL,
                 "label": "STRUCTURAL (guard G1: no eq. (17) carrier among the owner attributes used; B2t carried)"}
    out["F2_still"] = {"lemmas": STILL_ON_F2, "label": "STRUCTURAL (not edited here; both OPEN by status)"}
    return out


def report(d):
    print("b1_matter.py -- four lemmas re-based off input F2: there are no matter-free planes (184)\n")
    for cid, c in d["checks"].items():
        print("  %-3s %-4s %s  [%s]" % (cid, "ok" if c["ok"] else "FAIL", c["what"], c["label"]))
    print("\nThe edited lemmas:")
    for l in d["lemmas"]:
        print("  %-5s (edits %s) %-8s green=%s  %s" % (l["name"], l["edits"], l["status"], l["green"], l["statement"]))
    print("\nSlots: %s" % "; ".join("%s %s" % (k, "green" if v["green"] else "NOT green") for k, v in d["slots"].items()))
    print("F1 (eq. (17) on the plane) enters B2t directly and Z3'b through B3/B4, none of the other parts; it still "
          "enters: %s" % ", ".join(F1_STILL))
    print("Still on F2, not edited here: %s" % "; ".join("%s %s" % kv for kv in STILL_ON_F2.items()))


def selftest():
    t0 = _wall.perf_counter()
    allok = True
    print("b1_matter selftest (computed, READ and deduced; the build checked by two separate AI sessions in this project, "
          "findings applied; the applied version not re-checked; not seated)")
    for cid, (fn, what, _m, _label) in CHECKS.items():
        ok, det = fn(None)
        allok = allok and ok
        print("%-3s %s  %s\n      %s" % (cid, "PASS" if ok else "FAIL", what, json.dumps(_clean(det))[:600]))
    print("selftest %s: %d checks, wall %.1f s" % ("PASSED" if allok else "FAILED", len(CHECKS), _wall.perf_counter() - t0))
    return allok


def mutants():
    t0 = _wall.perf_counter()
    passed, n = [], 0
    print("b1_matter --mutants: each named mutation must make its check FAIL")
    for cid, (fn, what, muts, _label) in CHECKS.items():
        for name, desc in muts:
            n += 1
            try:
                ok, det = fn(name)
            except Exception as exc:                         # a mutation that breaks the computation also fails it
                ok, det = False, {"raised": repr(exc)[:200]}
            if ok:
                passed.append((cid, name))
            print("%-3s [%s] %s: %s" % (cid, name, desc, "check FAILS (as required)" if not ok else
                                        "MUTATION PASSES (the check cannot fail this way)"))
    print("mutants: %d run, %d caught, %d passed %s; wall %.1f s" % (n, n - len(passed), len(passed), passed,
                                                                    _wall.perf_counter() - t0))
    return not passed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mutants", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    a = ap.parse_args(argv)
    rc = 0
    if a.selftest:
        rc |= 0 if selftest() else 1
    if a.mutants:
        rc |= 0 if mutants() else 1
    if a.json:
        with open(a.json, "w") as fh:
            json.dump(_clean(compute()), fh, indent=1)
        print("wrote %s" % a.json)
    if not (a.selftest or a.mutants or a.json):
        report(compute())
    return rc


if __name__ == "__main__":
    sys.exit(main())
