#!/usr/bin/env python3
r"""
hpscentre.py -- O5, DOCKET 64 LINE 2.  HOCHBERG-POPOV-SUSHKOV WITH A REGULAR CENTRE.

    python3 hpscentre.py             the reading (computes everything; ~1.5 min)
    python3 hpscentre.py --selftest  every control; sympy + numpy + scipy; ~2 min
    python3 hpscentre.py --full      the reading, plus the far-zone window sweep
                                     carried out to x = 1e5 K (~2 more min)

Run from any directory: this file's own directory is APPENDED to sys.path
(never prepended), so nothing in it can shadow the stdlib, and throatmass.py is
IMPORTED for the two HPS figures, not copied.  Import is stdlib-only; sympy,
numpy, scipy and mpmath are imported inside the functions that use them
(numpy and scipy are recorded in PROOF-ASSISTANT.md's dependency table).

SEATED UNDER DOCKET 64'S RULING (sections A2, B2) AND THE verify-hps VERDICT.
Everything the ruling or the verifier withdrew is KEPT below, marked
WITHDRAWN, with the reason; WITHDRAWN (the tuple) carries the same list for
the ledger.

===============================================================================
0.  THE QUESTION, AND THE ANSWER
===============================================================================

O5 asks whether a self-consistent static semiclassical solution with m(r) < 0
exists at all.  throatmass.py recorded that every non-perturbative construction
in print is a throat, that a throat has m = r_0/2 > 0, and that nobody had run
HPS's system with a regular centre.  This file runs it, and it runs HPS's own
throat through its flare as well.

    YES -- WITHIN HPS'S MODEL SYSTEM, TAKEN IN ITS ONE CONSERVED READING, m < 0
    IS REALISED, AT A REGULAR CENTRE AND ON HPS'S OWN eq. (9) THROAT DATA.  NO
    INSTANCE HAS BEEN SHOWN TO LIE IN THE DOMAIN IN WHICH THE AHS APPROXIMATION
    HAS BEEN DERIVED OR ESTABLISHED.  O5 STAYS OPEN.

  "Self-consistent" means a solution of HPS's model system (G = 8 pi <T>, <T>
  the AHS analytic approximation for the massless conformal scalar), not of
  exact semiclassical gravity: no exact <T_ab> is known on these metrics.

  (a) REGULAR CENTRE, FORMAL SERIES -- THEOREM (sympy, all orders).  With the
      smooth-centre data r = l + c3 l^3 + ..., f = f0(1 + b2 l^2 + ...), the
      series recursion's determinant is -512 p (3 L0 + 4)(p - 2)^2 (p - 1)
      (p + 1)^3, L0 = ln f(0).  So WHEN 3 L0 + 4 != 0 the free data are exactly
      (L0, b2, c3) and every higher coefficient is fixed.  At 3 L0 + 4 = 0 the
      recursion is singular at every order; that case is NOT ANALYSED (it could
      mean non-uniqueness or no series at all).  And m = -3 c3 l^3 + O(l^5):
      c3 > 0 is free, so m < 0 at the centre on an open set of data.
        WITHDRAWN: "every higher coefficient is fixed IFF 3 L0 + 4 != 0".  Only
        the "if" direction is proved.

  (b) REGULAR CENTRE, LINEARISED -- THEOREM, FOR THE LINEARISED SYSTEM ONLY.
      About flat space the two regular-centre modes are phi = A sin(kl)/l,
      rho' = B (sin kl - kl cos kl)/l with k^2 = 1/(16 K^2) (A = -2B) or
      k^2 = 1/(16 K^2 (3 L0 + 4)) (A = 4B).  THESE ARE HPS's OWN omega_1^2 AND
      omega_2^2, printed for the far zone of their throat, recovered here at
      the centre from their printed equations.  For 3 L0 + 4 > 0 and L0 != -1:
      EVERY non-flat analytic regular-centre solution OF THE LINEARISED SYSTEM
      has m < 0 somewhere, has m > 0 somewhere, and is NOT asymptotically flat
      (2m/r does not tend to 0).

  (c) REGULAR CENTRE, NONLINEAR -- MEASURED.  Integrated from the series; the
      deviation from (b) falls tenfold per decade of amplitude (the control),
      the ll constraint holds to 1e-10, m < 0 from the centre out for c3 > 0,
      and m < 0 first at the linear-theory radius for c3 < 0.  At large
      amplitude the solution runs into 3 ln f + 4 = 0, where the system's
      fourth-order determinant -256 (3 ln f + 4) vanishes.
      NON-FLATNESS OF THE NONLINEAR SOLUTIONS IS MEASURED ONLY for c3 K^2 =
      1e-4 out to x = 300 K (2m/r not decaying there), and for the
      large-amplitude runs that end at 3 ln f + 4 = 0.  WHETHER THE NONLINEAR
      SMALL-AMPLITUDE SOLUTIONS ARE ASYMPTOTICALLY FLAT IS OPEN
      (NONLINEAR_CENTRE_ASYMPTOTICS).  Theorem (b) does not reach them.
        WITHDRAWN: "by (b), no non-flat regular-centre solution is
        asymptotically flat" applied to the NONLINEAR runs (failure mode 4:
        (b) is a statement about the linearised system).

  (d) HPS's OWN THROAT, CONSERVED SYSTEM -- MEASURED.  From their eq. (9) data,
      ln f(0) = -2/3, the flare has r' > 1, so m < 0, from l < 8 K onward (the
      reading prints the root; FIRST_NEGATIVE_M_THROAT_LP is its fixture, in
      l_P, pinned by the selftest from first_negative), reproduced by three
      integrators (DOP853, Radau, LSODA), and it recurs in EVERY 8 pi K window
      between 50 K and 1e4 K (the reading prints the count).  The row's "0 of
      6 families with m < 0" was a statement about what was REPORTED; it is
      not true of the conserved solution.
        WITHDRAWN: "in BOTH the printed and the conserved system".  The printed
        reading has NO solution of all three field equations from these data
        (section 2); the printed trajectory solves tt and thth only.

  SCALE.  Every m < 0 region begins at a few K, K = 1/sqrt(5760 pi) l_P
  (K_in_planck() owns the figure; it is never typed).  At a regular centre the
  first sign change of the L0-independent mode is at zeta_1 x 4K, zeta_1 the
  first root of tan y = y; the other mode scales as sqrt(3 L0 + 4), and the
  reading computes its bound over HPS_LNF0_RANGE.

  DOMAIN.  Every instance fails a hypothesis under which the AHS approximation
  has been DERIVED OR ESTABLISHED: asymptotic flatness (Popov hep-th/0302039
  p.1, eq. (70), Sec. VI).  This is NOT a showing that the approximation is
  invalid there -- Popov (p.2, Sec. IV) shows the high-frequency part, which is
  the AHS expression, does not depend on the state; asymptotic flatness enters
  through the low-frequency part.  For the throat the failure is HPS's own
  statement ("the metric as a whole is not asymptotically flat") plus the
  measurement; for linear centre solutions it is theorem (b); for the
  nonlinear centre runs it is measured only where (c) says.  Popov's truncated
  L-scale (his eq. (21), printed terms) is BELOW l_P where each m < 0 region
  FIRST appears (throat flare, large-amplitude centre) -- but NOT at every
  m < 0 point: along the throat's far shells and at small amplitude it passes
  l_P.  So sub-Planck size is reported as a measurement and is NOT the ground
  of the verdict.
    WITHDRAWN: "outside the approximation's domain of VALIDITY".  Nothing here
    shows invalidity; what fails is the hypothesis it was established under.

===============================================================================
1.  SOURCES, AS READ (alphaXiv, full text)
===============================================================================

  HPS      gr-qc/9701064 v1, PRL 78 2050 -- READ IN FULL: eqs. (2), (5)-(9), the
           asymptotic omega_1, omega_2, a = 5.3, b = 25.5, footnote [20].  The
           arXiv PDF TEXT LAYER was read; the journal PRL text was NOT.
  POPOV    hep-th/0302039 v2 -- READ: eqs. (21), (55), (70), (83), Sec. IV,
           Sec. VI, Appendix B (B1)-(B3).  Popov states his (T)^(4) IS the AHS
           analytic approximation (after eq. (67)); it is the independent
           second printing of HPS's source term used below.
  TSH      gr-qc/9608036 (Taylor-Hiscock-Anderson) -- READ: p.3, the massless
           analytic approximations "contain an arbitrary parameter whose value
           cannot be fixed except by experiment".
  AHL      gr-qc/9504019 (Anderson-Hiscock-Loranz) -- READ: eq. (6), alpha =
           beta = 1/(2880 pi^2) for the conformal scalar (the trace fixture);
           eq. (4) and Figs. 3-4: AHS's analytic approximation predicts a
           horizon divergence the exact numerics do not have.
  AHS      PRD 51 4337 -- NOT-REACHED.  Searched: alphaXiv title search (twice),
           author search, one arXiv-id probe; AHL (April 1995) cites it as
           "Physical Review D (in press)" with no gr-qc number.  Its hypotheses
           are taken ONLY as Popov, TSH and AHL state them.

===============================================================================
2.  THE SYSTEM.  THE TWO PRINTINGS DISAGREE AT THREE PLACES, AND
    CONSERVATION DECIDES THEM
===============================================================================

  HPS (5)-(7) and Popov (B1)-(B3) at xi = 1/6, m = 0 are transcribed
  INDEPENDENTLY below.  Mapping: 8 pi / (46080 pi^2) = K^2, and Popov's
  ln|4u0^2/(m_DS^2 r^2)| = ln(4 w0^2/(m_DS^2 f)), so HPS's ln f coefficient is
  MINUS Popov's.  All three non-log parts agree EXACTLY.  The log parts differ
  at THREE places (the selftest counts them from printed_differences()):

    M1  HPS (5), ln f bracket: the text layer reads 16 f'^2 f''/f^3; Popov's
        (B1) gives 116.
    M2  HPS (6), ln f bracket: the text layer reads -4 f'^2 r'^2/(f^2 r) -- NOT
        HOMOGENEOUS (every other term scales as length^-4); Popov's (B2) gives
        /(f^2 r^2).
    M3  Popov (B3): -21 r^8 f'^4 is printed INSIDE the (xi - 1/6)^2 bracket;
        HPS's (7) carries +21 f'^4/f^4 ln f.

  M1 and M2 are in HPS; M3 is in Popov.
    WITHDRAWN: the count "two misprints and two errors" (the report's typed
    heading).  The count is three disagreements, and it is computed.

  CONSERVATION DECIDES ALL THREE.  Of the four readings of M1 x M3, exactly one
  -- (116, 21) -- is conserved identically (d_l T^l_l + (f'/2f)(T^l_l - T^t_t)
  + (2r'/r)(T^l_l - T^th_th) = 0 for arbitrary f, r); the other three leave
  residuals.  (verify-hps/v1 solved for the two coefficients as UNKNOWNS and
  found (116, 21) unique, with no conserving pair at the printed r^1 slot;
  qeihps.repair_scan finds the same two HPS repairs by an independent
  single-change scan.)  The same reading, and only it, makes the ln f part
  TRACELESS, as a mu-dependent term must be.  The non-log trace is then
      8 pi T^a_a = 16 K^2 [C^2 + (R_ab R^ab - R^2/3) + box R],
  whose last two coefficients are AHL eq. (6)'s alpha = beta = 1/(2880 pi^2).

  WHICH SYSTEM DID HPS INTEGRATE?  NOT DETERMINED
  (HPS_INTEGRATED_THE_PRINTED_SYSTEM = "NOT DETERMINED").  HPS's far-zone law
  sqrt F = a ln l - b is a two-parameter log fit, and on these integrations
  the fitted (a, b) depend on the fitting window and on the sampling, and a
  has not converged to a constant in either system: it keeps rising with the
  window.  The reading prints the (a, b) spread over FAR_ZONE_WINDOWS for both
  systems (--full carries it to 1e5 K); attribution() claims a system only if
  it alone matches HPS's (5.3, 25.5) in EVERY window, and on the computed sweep
  it claims neither.  HPS do not state the window they fitted over.
    WITHDRAWN: "HPS integrated the PRINTED system: the printed M1 reproduces
    a, b within 5 % while the conserved one misses a by > 20 %"
    (HPS_INTEGRATED_THE_PRINTED_SYSTEM = True).  That held in ONE window,
    [2000, 1e4] K sampled linearly; the selftest reproduces that single-window
    verdict and shows the sweep refuses it.

  THE PRINTED READING HAS NO SOLUTION OF ALL THREE EQUATIONS FROM THESE DATA
  (MEASURED).  Its source is not conserved (the divergence is printed).  From
  eq. (9)'s data, tt and thth determine the trajectory uniquely (the 4th-order
  determinant -256 (3 ln f + 4)/(f r) stays away from 0 along the run -- the
  hypothesis is checked, not assumed), so a three-equation solution from these
  data would have to be that trajectory; and on it the ll equation fails by
  ORDER ONE relative to the Einstein-side scale |f'r'/fr| + r'^2/r^2 + 1/r^2
  (the reading prints median and max, under the M2 slot read both ways).  The
  conserved run holds ll below 1e-6 relative by the same measure (printed).
    WITHDRAWN: "ll constraint drift 7.8e-5" as the printed system's figure.
    It is an ABSOLUTE maximum taken mostly near the throat, and it hid the
    order-one relative violation.

===============================================================================
3.  THE CONTROL: HPS's PUBLISHED THROATS, REPRODUCED
===============================================================================

  (i)   Eq. (8) is RE-DERIVED from eq. (6) at l = 0 with r' = f' = 0 (sympy),
        and its two printed cases return throatmass.hps_quartic()'s roots
        EXACTLY: sqrt(15)/(90 sqrt(pi)) l_P and 12 sqrt(10 pi) l_P.
        Eq. (9)'s r(0) = sqrt(-16 K^2 ln f(0)) is a root of it.
  (ii)  At eq. (9)'s data r''''(0) = 7 sqrt(6)/768 K^-3 > 0: the throat is a
        minimum, as HPS's Fig. 2a shows.
  (iii) The ripple: r' extrema are spaced pi/omega_1 = 4 pi K to 1 %.
  (iv)  The far zone: see section 2 -- the window sweep, which decides nothing
        about attribution.
          WITHDRAWN: "the control discriminates" (the > 20 % control).
  The case-2 throat (12 sqrt(10 pi) l_P) is reproduced at (i) only; it is not
  integrated.

===============================================================================
4.  WHAT THIS DOES TO O5
===============================================================================

  O5 stays OPEN.  Its NOT-FOUND is replaced: m < 0 is FOUND in HPS's model
  system (conserved reading), at a regular centre and on the published throat
  data -- and FOUND ONLY OUTSIDE the domain in which the approximation that
  defines the system has been established.  The open question is therefore
  no longer "does the system allow m < 0" (it does, generically) but "does
  semiclassical gravity allow m < 0 where its approximation is established",
  which no instrument here reaches: it needs a <T_ab> established at a
  non-asymptotically-flat regular centre, or an asymptotically flat solution
  with m < 0 (O5_ANSWERED_BY).  No requirement on the device moves: D1 still
  demands m < 0; this row prices where the only model that supplies it holds.
"""

import math
import os
import sys

#: This file's own directory (research/warp-drive wherever the repository is
#: checked out) -- never an absolute path (DOCKET 64 ruling B1/B2).
TREE = os.path.dirname(os.path.abspath(__file__))
if TREE not in sys.path:
    sys.path.append(TREE)            # appended, never prepended

import throatmass                    # noqa: E402  (hps_quartic, planck_length)

# ---------------------------------------------------------------------------
# READ data -- printed figures, used ONLY as fixtures to compare against.
# ---------------------------------------------------------------------------
HPS_ARXIV = "gr-qc/9701064"
HPS_A_PRINTED, HPS_B_PRINTED = 5.3, 25.5      # F(l) ~ (a ln l - b)^2, HPS p.8
HPS_LNF0_RUN = (-2, 3)                        # ln f(0) = -2/3, HPS eq. (9)
HPS_LNF0_RANGE = (-1.0, 0.0)                  # -1 <= ln f(0) < 0, HPS eq. (9)
AHL_ALPHA_BETA_TIMES_2880PI2 = 1              # AHL gr-qc/9504019 eq. (6)
AHS_REACHED = False                           # NOT-REACHED -- see section 1

# ---------------------------------------------------------------------------
# The far-zone window sweep (section 2).  (lo, hi, sampling) in K; HPS do not
# state their window.  MATCH_TOL is the old control's own 5 %; a system
# "matches" HPS in a window when BOTH a and b are within it.
# ---------------------------------------------------------------------------
FAR_ZONE_WINDOWS = ((500, 2000, "lin"), (500, 2000, "log"), (1000, 10000, "lin"),
                    (2000, 5000, "lin"), (2000, 10000, "lin"), (2000, 10000, "log"),
                    (5000, 10000, "lin"))
FAR_ZONE_WINDOWS_FULL = ((10000, 30000, "log"), (30000, 100000, "log"),
                         (2000, 100000, "log"))           # --full only
#: The window the withdrawn attribution was read in.
WITHDRAWN_ATTRIBUTION_WINDOW = (2000, 10000, "lin")
MATCH_TOL = 0.05
#: Width of a ripple-count window, in K: two ripple periods, 2 pi/omega_1.
RIPPLE_WINDOW_K = 8 * math.pi
RIPPLE_COUNT_RANGE_K = (50, 10000)
#: The regular-centre runs are made at this ln f(0) (and b2 = 0).
CENTRE_L0 = 0

STATUS = "MEASURED"                           # the line; (a), (b) are THEOREM
O5_CLOSED = False
#: True on the CONSERVED reading; the selftest re-derives it from the runs.
M_NEGATIVE_FOUND_IN_HPS_SYSTEM = True
M_NEGATIVE_FOUND_INSIDE_DOMAIN = False
#: The throat m < 0 claim is confined to this reading (section 0 (d)).
THROAT_M_NEGATIVE_READING = "CONSERVED"
#: DOCKET 64 ruling B2 (BLOCKING): the attribution is withdrawn.  The selftest
#: computes attribution() over FAR_ZONE_WINDOWS and requires it to equal this.
HPS_INTEGRATED_THE_PRINTED_SYSTEM = "NOT DETERMINED"
#: MEASURED: the printed reading's tt+thth trajectory from eq. (9)'s data
#: breaks ll by order one relative, and that trajectory is unique.
PRINTED_READING_HAS_THREE_EQUATION_SOLUTION_FROM_EQ9 = False
#: The number of places the two printings' log parts disagree -- a fixture;
#: the selftest counts it from printed_differences().
PRINTED_DISAGREEMENTS = 3
#: FIXTURE, in l_P: first m < 0 on HPS's eq. (9) throat, conserved reading.
#: Pinned by the selftest from first_negative() x K_in_planck(), to 4 places.
FIRST_NEGATIVE_M_THROAT_LP = 0.0516
#: The centre expansion of the Misner-Sharp mass; the selftest rebuilds this
#: string from order_zero()'s series.
CENTRE_M_LEADING = "m = -3 c3 l^3 + O(l^5)"
RECURSION_DIRECTION = ("IF: 3 L0 + 4 != 0 fixes every coefficient beyond "
                       "(L0, b2, c3); 3 L0 + 4 = 0 is singular and NOT ANALYSED")
LINEAR_CENTRE_THEOREM_SCOPE = "the LINEARISED system about flat space"
NONLINEAR_CENTRE_NONFLATNESS = ("MEASURED for c3 K^2 = 1e-4 out to x = 300 K, and "
                                "for the large-amplitude runs ending at "
                                "3 ln f + 4 = 0; not measured elsewhere")
NONLINEAR_CENTRE_ASYMPTOTICS = "OPEN"
DOMAIN_WORD = ("established: the AHS approximation has been derived or established "
               "only for asymptotically flat spacetimes (Popov p.1, eq. (70), "
               "Sec. VI); nothing here shows it invalid")
CHANGES_A_REQUIREMENT = False
O5_ANSWERED_BY = ("a <T_ab> established at a centre that is not asymptotically "
                  "flat, or an asymptotically flat self-consistent solution with "
                  "m < 0; FO Thm 4.2 evaluated on HPS (needs a reference Hadamard "
                  "state and <:Phi^2:> there; qeihps.FO_ON_HPS); the nonlinear "
                  "regular-centre existence theorem.  Read AHS PRD 51 4337 "
                  "(NOT-REACHED)")
#: Kept, never deleted: every claim DOCKET 64 withdrew from this line, with why.
WITHDRAWN = (
    ("HPS_INTEGRATED_THE_PRINTED_SYSTEM = True: 'HPS integrated the PRINTED, "
     "non-conserved system'",
     "the far-zone fit depends on the window and has not converged "
     "(verify-hps v4; ruling A2, B2 BLOCKING); now NOT DETERMINED"),
    ("CONTROL 'the conserved system MISSES HPS's a by > 20 %' (the discriminating "
     "control)", "holds in one window only; replaced by the window sweep and "
     "attribution()"),
    ("'m < 0 on the throat holds in BOTH the printed and the conserved system'",
     "the printed trajectory breaks ll by order one relative; confined to the "
     "conserved reading"),
    ("'ll constraint drift 7.8e-5' as the printed system's figure",
     "an absolute maximum; the relative residual is order one"),
    ("'TWO MISPRINTS AND TWO ERRORS'", "three disagreements (M1, M2 in HPS; M3 "
     "in Popov), counted"),
    ("'every higher coefficient is fixed IFF 3 L0 + 4 != 0'", "only 'if' is "
     "proved; 3 L0 + 4 = 0 not analysed"),
    ("'by (b), no non-flat regular-centre solution is asymptotically flat' for "
     "the NONLINEAR solutions", "(b) is about the linearised system; nonlinear "
     "asymptotics OPEN"),
    ("'outside the approximation's domain of VALIDITY'", "outside the domain in "
     "which it has been ESTABLISHED"),
    ("'HPS (5) prints 16'", "the PDF text layer reads 16; the journal text was "
     "not read"),
    ("the typed 'K = 0.0074335 l_P'", "wrong in the fifth digit; K_in_planck() "
     "owns K and nothing types it"),
)


# ============================================================ the system
def build(sp):
    """HPS (5)-(7) and Popov (B1)-(B3), as the text layers read, plus the
    Einstein side.  Returns a dict of sympy objects in f(l), r(l)."""
    l = sp.Symbol('l', real=True)
    fF, rF = sp.Function('f')(l), sp.Function('r')(l)
    f, f1, f2, f3, f4 = [sp.diff(fF, l, k) for k in range(5)]
    r, r1, r2, r3, r4 = [sp.diff(rF, l, k) for k in range(5)]
    a_tt, a_th, ll_pow = sp.symbols('alpha_tt alpha_th ll_pow')

    # HPS eq. (5), (6), (7) -- ln f brackets carry the three disputed slots:
    #   a_tt : coefficient of f'^2 f''/f^3 in (5) (printed 16)
    #   ll_pow: power of r in the -4 f'^2 r'^2/(f^2 r^p) term of (6) (printed 1)
    #   a_th : coefficient of f'^4/f^4 in (7) (printed 21)
    tt_n = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
            - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
            - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
            - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
            + 16*f4/f - 64*r4/r)
    tt_l = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
            - 16*r1**4/r**4 + a_tt*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
            + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3 + 16*f2*r2/(f*r)
            + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r) - 16*f1*r3/(f*r) - 32*r1*r3/r**2
            + 16*f4/f - 32*r4/r)
    ll_n = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
            + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 48*f1**2*r2/(f**2*r)
            + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r) + 8*f1*f3/f**2 - 32*r1*f3/(f*r)
            - 32*f1*r3/(f*r))
    ll_l = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r**ll_pow)
            + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3 + 48*f1*r1*f2/(f**2*r)
            - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 16*f1**2*r2/(f**2*r) + 16*f1*r1*r2/(f*r**2)
            + 16*f2*r2/(f*r) - 16*r2**2/r**2 + 8*f1*f3/f**2 - 16*r1*f3/(f*r) - 16*f1*r3/(f*r)
            + 32*r1*r3/r**2)
    th_n = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3) - 52*f1**2*f2/f**3
            + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2) + 28*f2**2/f**2 + 16*f1**2*r2/(f**2*r)
            + 64*f1*r1*r2/(f*r**2) - 32*f2*r2/(f*r) + 24*f1*f3/f**2 - 48*r1*f3/(f*r)
            + 32*f1*r3/(f*r) - 16*f4/f)
    th_l = (-16/r**4 + a_th*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
            - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3 + 28*f1*r1*f2/(f**2*r)
            + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2 + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2)
            - 32*r1**2*r2/r**3 - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r)
            + 16*f1*r3/(f*r) - 8*f4/f + 16*r4/r)

    # Popov (B1)-(B3), xi = 1/6, m = 0, in q = r^2; the (xi-1/6)^2 brackets drop.
    q = r**2
    q1, q2, q3, q4 = [sp.diff(q, l, k) for k in range(1, 5)]
    d = r**8*f**4
    b1n = (32*r**4*f**4 - 32*q4*r**6*f**4 - 12*f2**2*r**8*f**2 + 56*q2**2*r**4*f**4
           + 16*f4*r**8*f**3 + 7*f1**4*r**8 - 32*f2*q2*r**6*f**3 - 16*f1*q1**3*r**2*f**3
           + 40*f1**2*q2*r**6*f**2 - 16*f1*f3*r**8*f**2 + 16*f2*q1**2*r**4*f**3
           + 4*f1**2*f2*r**8*f - 12*f1**3*q1*r**6*f - 14*f1**2*q1**2*r**4*f**2
           - 48*f1*q3*r**6*f**3 + 48*q1*q3*r**4*f**4 - 112*q1**2*q2*r**2*f**4
           + 32*f1*q2*q1*r**4*f**3 + 40*q1**4*f**4 + 32*q1*f3*r**6*f**3)
    b1l = (-16*r**4*f**4 - 20*q1**4*f**4 + 56*q1**2*q2*r**2*f**4 + 8*f1*q2*q1*r**4*f**3
           - 28*q2**2*r**4*f**4 - 16*f4*r**8*f**3 + 52*f1*f2*q1*r**6*f**2 + 16*q4*r**6*f**4
           + 36*f2**2*r**8*f**2 + 49*f1**4*r**8 - 4*f1*q1**3*r**2*f**3 - 4*f1**2*q2*r**6*f**2
           + 48*f1*f3*r**8*f**2 + 4*f2*q1**2*r**4*f**3 - 116*f1**2*f2*r**8*f
           - 22*f1**3*q1*r**6*f - 3*f1**2*q1**2*r**4*f**2 + 8*f1*q3*r**6*f**3
           - 32*q1*f3*r**6*f**3 - 24*q1*q3*r**4*f**4 - 8*f2*q2*r**6*f**3)
    b2n = (f1**4*r**8 + 32*f1*q2*q1*r**4*f**3 - 4*f1**2*f2*r**8*f - 24*f2*q1**2*r**4*f**3
           - 16*f1*q3*r**6*f**3 - 16*q1*f3*r**6*f**3 - 8*f1*q1**3*r**2*f**3
           - 24*f1**2*q2*r**6*f**2 + 12*f1**2*q1**2*r**4*f**2 + 8*f1*f3*r**8*f**2
           - 4*f2**2*r**8*f**2 + 16*f2*q2*r**6*f**3 - 8*f1**3*q1*r**6*f
           + 32*f1*f2*q1*r**6*f**2)
    b2l = (12*f2*q1**2*r**4*f**3 - 16*r**4*f**4 - 4*q1**4*f**4 + 8*f1**2*q2*r**6*f**2
           + 12*f1**2*f2*r**8*f + 8*q1*f3*r**6*f**3 - 8*f1*f3*r**8*f**2 + 8*f1*q3*r**6*f**3
           - 24*f1*f2*q1*r**6*f**2 - 3*f1**2*q1**2*r**4*f**2 + 4*f1*q1**3*r**2*f**3
           - 16*f1*q2*q1*r**4*f**3 + 8*q1**2*q2*r**2*f**4 - 8*q1*q3*r**4*f**4
           + 10*f1**3*q1*r**6*f - 7*f1**4*r**8 - 8*f2*q2*r**6*f**3 + 4*f2**2*r**8*f**2
           + 4*q2**2*r**4*f**4)
    b3n = (-8*r**4*f**3*f1*q2*q1 + 16*r**6*f**2*f1*f2*q1 + 17*r**8*f1**4 - 16*r**8*f**3*f4
           - 8*r**6*f*f1**3*q1 + 16*r**6*f**3*f1*q3 + 16*r**4*f**3*f2*q1**2
           - 52*r**8*f*f1**2*f2 + 24*r**8*f**2*f1*f3 - 4*r**4*f**2*f1**2*q1**2
           + 8*r**6*f**2*f1**2*q2 + 28*r**8*f**2*f2**2 - 24*r**6*f**3*q1*f3
           - 16*r**6*f**3*f2*q2)
    b3l = (16*r**4*f**4 - 20*r**8*f**2*f1*f3 + 12*f**4*q1**4 - 14*r**6*f**2*f1*f2*q1
           + 12*r**6*f**3*q1*f3 + 8*r**6*f**3*f2*q2 + 6*r**6*f*f1**3*q1
           - 2*r**6*f**2*f1**2*q2 - 8*r**6*f**3*f1*q3 + 12*r**4*f**4*q2**2
           - 20*r**8*f**2*f2**2 + 4*r**4*f**3*f1*q2*q1 - 8*r**4*f**3*f2*q1**2
           + 3*r**4*f**2*f1**2*q1**2 + 16*r**4*f**4*q1*q3 + 52*r**8*f*f1**2*f2
           + 8*r**8*f**3*f4 - 8*r**6*f**4*q4 - 32*r**2*f**4*q1**2*q2)

    G = (2*r2/r + r1**2/r**2 - 1/r**2,                         # HPS G^t_t
         f1*r1/(f*r) + r1**2/r**2 - 1/r**2,                    # HPS G^l_l
         f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))     # HPS G^th_th
    return dict(l=l, fF=fF, rF=rF, F=(f, f1, f2, f3, f4), R=(r, r1, r2, r3, r4),
                a_tt=a_tt, a_th=a_th, ll_pow=ll_pow, G=G,
                hps=((tt_n, tt_l), (ll_n, ll_l), (th_n, th_l)),
                popov=((b1n/d, b1l/d), (b2n/d, b2l/d), (b3n/d, b3l/d)))


PRINTED = dict(a_tt=16, a_th=21, ll_pow=1)       # HPS text layer
CONSERVED = dict(a_tt=116, a_th=21, ll_pow=2)    # the one conserved reading
#: What the throat numerics run as "printed": M1 as printed.  M2 sits in the ll
#: equation, which is the CONSTRAINT and never enters the integration; it is
#: read homogeneously (r^2) so the drift monitor measures M1's non-conservation
#: and not M2's dimensional slip.
PRINTED_M1 = dict(a_tt=16, a_th=21, ll_pow=2)


def source(sp, S, reading):
    """8 pi T^mu_nu / K^2 for (tt, ll, thth) under a reading of the three slots."""
    sub = {S['a_tt']: reading['a_tt'], S['a_th']: reading['a_th'],
           S['ll_pow']: reading['ll_pow']}
    Lf = sp.log(S['F'][0])
    return tuple(n.subs(sub) + Lf*lg.subs(sub) for n, lg in S['hps'])


def divergence(sp, S, T):
    """d_l T^l_l + (f'/2f)(T^l_l - T^t_t) + (2r'/r)(T^l_l - T^th_th)."""
    f, f1 = S['F'][0], S['F'][1]
    r, r1 = S['R'][0], S['R'][1]
    tt, ll, th = T
    return sp.simplify(sp.expand(sp.diff(ll, S['l']) + f1/(2*f)*(ll - tt) + 2*r1/r*(ll - th)))


def printed_differences(sp, S):
    """HPS-printed minus Popov-printed, non-log and (sign-flipped) log, per component."""
    sub = {S['a_tt']: PRINTED['a_tt'], S['a_th']: PRINTED['a_th'], S['ll_pow']: PRINTED['ll_pow']}
    out = []
    for (hn, hl), (pn, pl) in zip(S['hps'], S['popov']):
        out.append((sp.simplify(sp.expand(hn - pn)),
                    sp.simplify(sp.expand(hl.subs(sub) + pl))))
    return out


def homogeneity(sp, S, reading):
    """Every term of every bracket must scale as s^-4 under l -> s l, r -> s r."""
    s = sp.Symbol('s', positive=True)
    l = S['l']
    rep = {}
    for k in range(4, -1, -1):
        rep[sp.diff(S['fF'], l, k)] = sp.Symbol('F%d' % k) / s**k
        rep[sp.diff(S['rF'], l, k)] = sp.Symbol('R%d' % k) * s / s**k
    sub = {S['a_tt']: reading['a_tt'], S['a_th']: reading['a_th'], S['ll_pow']: reading['ll_pow']}
    bad = 0
    for pair in S['hps']:
        for br in pair:
            for term in sp.Add.make_args(sp.expand(br.subs(sub))):
                sc = sp.simplify(term.subs(rep) / term.subs(rep).subs(s, 1))
                bad += int(sp.simplify(sc - s**-4) != 0)
    return bad


def curvature(sp, S):
    """Einstein tensor, R, Ric^2, C^2, box R of HPS eq. (2), from the metric."""
    l = S['l']
    t, th, ph = sp.symbols('t theta phi')
    X = [t, l, th, ph]
    g = sp.diag(-S['fF'], 1, S['rF']**2, S['rF']**2*sp.sin(th)**2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(n))/2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Rm = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(n))
                    Rm[a, b, c, d] = sp.simplify(e)
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rm[a, b, a, d] for a in range(n))))
    Rs = sp.simplify(sum(gi[i, i]*Ric[i, i] for i in range(n)))
    Gmix = [sp.simplify(gi[i, i]*Ric[i, i] - Rs/2) for i in range(3)]
    Riem2 = sp.simplify(sum(Rm[a, b, c, d]**2*g[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
                            for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
    Ric2 = sp.simplify(sum(Ric[a, a]**2*gi[a, a]**2 for a in range(n)))
    C2 = sp.simplify(Riem2 - 2*Ric2 + Rs**2/3)
    sg = sp.sqrt(S['fF'])*S['rF']**2
    boxR = sp.simplify(sp.diff(sg*sp.diff(Rs, l), l)/sg)
    return dict(G=Gmix, R=Rs, Ric2=Ric2, C2=C2, boxR=boxR)


def trace_fit(sp, S, C, reading):
    """Fit the non-log trace to a C^2 + b (Ric^2 - R^2/3) + c box R; log trace."""
    T = [(n.subs({S['a_tt']: reading['a_tt'], S['a_th']: reading['a_th'],
                  S['ll_pow']: reading['ll_pow']}),
          lg.subs({S['a_tt']: reading['a_tt'], S['a_th']: reading['a_th'],
                   S['ll_pow']: reading['ll_pow']})) for n, lg in S['hps']]
    trn = sp.simplify(T[0][0] + T[1][0] + 2*T[2][0])
    trl = sp.simplify(T[0][1] + T[1][1] + 2*T[2][1])
    a, b, c = sp.symbols('a b c')
    res = sp.expand(sp.simplify((trn - (a*C['C2'] + b*(C['Ric2'] - C['R']**2/3) + c*C['boxR']))
                                * S['R'][0]**4*S['F'][0]**4))
    eqs = sp.Poly(res, *(list(S['F'][1:]) + list(S['R'][1:]))).coeffs()
    sol = sp.solve(eqs, [a, b, c], dict=True)
    return (sol[0] if sol else None), trl


def flat_values(sp, S, reading):
    """RHS on f = const, r = l (must vanish) and on r = l + l^3 (must not)."""
    l = S['l']
    f0 = sp.Symbol('f_0', positive=True)
    out = []
    for rr in (l, l + l**3):
        rep = {}
        for k in range(4, -1, -1):
            rep[sp.diff(S['fF'], l, k)] = sp.diff(f0 + 0*l, l, k)
            rep[sp.diff(S['rF'], l, k)] = sp.diff(rr, l, k)
        out.append(tuple(sp.simplify(x.subs(rep)) for x in source(sp, S, reading)))
    return out


# ============================================================ the throat, eq. (8)
def quartic(sp, S):
    """Eq. (6) at l = 0 with r' = f' = 0, re-derived: the throat quartic, with
    K^2 = 1/(5760 pi); returns (quartic in r0, case-1 roots, case-2 roots, (9) check)."""
    K2 = sp.Rational(1, 5760)/sp.pi
    f0, fpp, rpp, fppp, rppp, f4, r4 = sp.symbols('f0 fpp rpp fppp rppp f4 r4')
    r0 = sp.Symbol('r_0', positive=True)
    l = S['l']
    ll = source(sp, S, CONSERVED)[1]
    rep = {}
    vals_f = (f0, 0, fpp, fppp, f4)
    vals_r = (r0, 0, rpp, rppp, r4)
    for k in range(4, -1, -1):
        rep[sp.diff(S['fF'], l, k)] = vals_f[k]
        rep[sp.diff(S['rF'], l, k)] = vals_r[k]
    E = (S['G'][1] - K2*ll).subs(rep)
    qrt = sp.expand(sp.simplify(E*r0**2/K2))
    c1 = qrt.subs({fpp: 0, rpp: 0, f0: sp.exp(sp.Rational(*HPS_LNF0_RUN))})
    c2 = qrt.subs({f0: 1, fpp: 1, rpp: 0})
    s1 = [x for x in sp.solve(sp.Eq(c1, 0), r0) if x.is_positive]
    s2 = [x for x in sp.solve(sp.Eq(sp.simplify(c2), 0), r0) if x.is_positive]
    L = sp.Symbol('L', negative=True)
    nine = sp.simplify(qrt.subs({fpp: 0, rpp: 0, f0: sp.exp(L)}).subs(r0, sp.sqrt(-16*K2*L)))
    return qrt, s1, s2, nine, (fppp, rppp, f4, r4)


# ============================================================ numerics (K = 1 units)
_NUM_CACHE = {}


def _key(reading):
    return tuple(sorted(reading.items()))


def numeric_system(sp, reading):
    """Lambdified 4th-order system in K = 1 units: tt and thth solved for
    (f'''', r''''), ll kept as the constraint.  Built once per reading."""
    if _key(reading) not in _NUM_CACHE:
        _NUM_CACHE[_key(reading)] = _numeric_system(sp, reading)
    return _NUM_CACHE[_key(reading)]


def _numeric_system(sp, reading):
    import numpy as np
    S = build(sp)
    T = source(sp, S, reading)
    Sy = sp.symbols('F0 F1 F2 F3 F4 R0 R1 R2 R3 R4')
    rep = {}
    l = S['l']
    for k in range(4, -1, -1):
        rep[sp.diff(S['fF'], l, k)] = Sy[k]
        rep[sp.diff(S['rF'], l, k)] = Sy[5+k]
    E = [(S['G'][i] - T[i]).subs(rep) for i in range(3)]
    F4, R4 = Sy[4], Sy[9]
    A = sp.Matrix([[sp.diff(E[0], F4), sp.diff(E[0], R4)], [sp.diff(E[2], F4), sp.diff(E[2], R4)]])
    b0 = sp.Matrix([E[0].subs({F4: 0, R4: 0}), E[2].subs({F4: 0, R4: 0})])
    args = list(Sy[:4]) + list(Sy[5:9])
    fA = sp.lambdify(args, A, 'numpy')
    fb = sp.lambdify(args, b0, 'numpy')
    fll = sp.lambdify(args, E[1], 'numpy')
    detA = sp.factor(sp.simplify(A.det()))

    def rhs(x, y):
        a = np.array(fA(*y), dtype=float)
        bb = np.array(fb(*y), dtype=float).ravel()
        d4 = np.linalg.solve(a, -bb)
        return [y[1], y[2], y[3], d4[0], y[5], y[6], y[7], d4[1]]
    return dict(rhs=rhs, ll=fll, E=E, Sy=Sy, detA=detA, reading=dict(reading))


def integrate(num, y0, x0, x1, rtol=1e-11, method='DOP853'):
    from scipy.integrate import solve_ivp
    return solve_ivp(num['rhs'], (x0, x1), y0, method=method, rtol=rtol,
                     atol=rtol*1e-3, dense_output=True)


def ll_scale(Y):
    """The Einstein-side scale of the ll equation, |f'r'/fr| + r'^2/r^2 + 1/r^2
    (the three terms of G^l_l, K = 1): the ll residual is reported RELATIVE to
    this, never as an absolute figure (ruling B2)."""
    import numpy as np
    f, f1, r, r1 = Y[0], Y[1], Y[4], Y[5]
    return np.abs(f1*r1/(f*r)) + r1**2/r**2 + 1/r**2


def constraint(sp, reading):
    """The ll equation (G^l_l - 8 pi T^l_l, K = 1) alone, lambdified, to
    evaluate one reading's constraint on a trajectory another reading made."""
    S = build(sp)
    T = source(sp, S, reading)
    Sy = sp.symbols('F0 F1 F2 F3 F4 R0 R1 R2 R3 R4')
    rep = {}
    for k in range(4, -1, -1):
        rep[sp.diff(S['fF'], S['l'], k)] = Sy[k]
        rep[sp.diff(S['rF'], S['l'], k)] = Sy[5+k]
    args = list(Sy[:4]) + list(Sy[5:9])
    return sp.lambdify(args, (S['G'][1] - T[1]).subs(rep), 'numpy')


def misner_sharp(Y):
    return Y[4]/2*(1 - Y[5]**2)


def first_negative(res, x0, x1, n=40001):
    """Root of m at its first sign change to negative, by brentq on dense output."""
    import numpy as np
    from scipy.optimize import brentq
    xs = np.linspace(x0, x1, n)
    m = misner_sharp(res.sol(xs))
    idx = np.where((m[:-1] >= 0) & (m[1:] < 0))[0]
    if m[0] < 0:
        return xs[0], True
    if len(idx) == 0:
        return None, False
    i = idx[0]
    return brentq(lambda x: misner_sharp(res.sol(x)), xs[i], xs[i+1], xtol=1e-12), False


def centre_series(sp, num, L0, b2, c3, order=2):
    """Regular-centre series r = x + c3 x^3 + c5 x^5 + c7 x^7, f = f0(1 + b2 x^2 +
    b4 x^4 + b6 x^6), K = 1: solve tt and ll at x^0 and x^2; return the data,
    and the thth coefficients at x^0, x^2 (must vanish -- the Bianchi control).
    Solved ONCE with c3 a symbol (per system, L0, b2), then specialised: the
    solved coefficients are polynomial in c3, and each solve costs ~15 s."""
    key = (_key(num['reading']), L0, b2)
    if key not in _SERIES_CACHE:
        c3s = sp.Symbol('c3')
        _SERIES_CACHE[key] = (c3s, _centre_series(sp, num, L0, b2, c3s))
    c3s, cs = _SERIES_CACHE[key]
    sol = {k: v.subs(c3s, c3) for k, v in cs['sol'].items()}
    x = cs['x']
    fs, rs = cs['fs'].subs(sol).subs(c3s, c3), cs['rs'].subs(sol).subs(c3s, c3)
    y0f = sp.lambdify(x, [sp.diff(fs, x, k) for k in range(4)] + [sp.diff(rs, x, k) for k in range(4)])
    return dict(y0=y0f, sol=sol, th0=sp.simplify(cs['th0'].subs(c3s, c3)),
                th2=sp.simplify(cs['th2'].subs(c3s, c3)),
                neg=[sp.simplify(v.subs(c3s, c3)) for v in cs['neg']])


_SERIES_CACHE = {}


def _centre_series(sp, num, L0, b2, c3):
    x = sp.Symbol('x', positive=True)
    b4, c5, b6, c7 = sp.symbols('b4 c5 b6 c7')
    f0 = sp.exp(L0)
    fs = f0*(1 + b2*x**2 + b4*x**4 + b6*x**6)
    rs = x + c3*x**3 + c5*x**5 + c7*x**7
    Sy, E = num['Sy'], num['E']
    ser = []
    for idx in (0, 1, 2):
        e = E[idx].subs({Sy[k]: sp.diff(fs, x, k) for k in range(5)}).subs(
            {Sy[5+k]: sp.diff(rs, x, k) for k in range(5)})
        s = sp.expand(sp.series(e, x, 0, 3).removeO())
        ser.append(s)
    neg = [sp.simplify(ser[i].coeff(x, p)) for i in range(3) for p in (-4, -3, -2, -1)]
    s0 = sp.solve([ser[0].coeff(x, 0), ser[1].coeff(x, 0)], [b4, c5], dict=True)[0]
    s2 = sp.solve([ser[0].coeff(x, 2).subs(s0), ser[1].coeff(x, 2).subs(s0)], [b6, c7], dict=True)[0]
    sol = dict(s0)
    sol.update({k: v.subs(s0) for k, v in s2.items()})
    th0 = sp.simplify(ser[2].coeff(x, 0).subs(sol))
    th2 = sp.simplify(ser[2].coeff(x, 2).subs(sol))
    return dict(x=x, fs=fs, rs=rs, sol=sol, th0=th0, th2=th2, neg=neg)


# ============================================================ exact algebra
def recursion_det(sp):
    """Series recursion: new coefficients (b_p, c_{p+1}) enter order x^(p-4)
    through the K^2 part of the linearised operator.  Its 2x2 determinant."""
    S = build(sp)
    lin = linearised(sp, S)
    p = sp.Symbol('p')
    bb, cc = sp.symbols('bb cc')
    x, phi, rho, K2 = lin['x'], lin['phi'], lin['rho'], lin['K2']
    rows = []
    for e1 in lin['eqs'][:2]:
        e = e1.coeff(K2)
        ph, rh = bb*x**p, cc*x**(p+1)
        e = e.subs({sp.Derivative(rho, (x, n)): sp.diff(rh, x, n) for n in (4, 3, 2)}).subs(
            sp.Derivative(rho, x), sp.diff(rh, x))
        e = e.subs({sp.Derivative(phi, (x, n)): sp.diff(ph, x, n) for n in (4, 3, 2)}).subs(
            sp.Derivative(phi, x), sp.diff(ph, x))
        e = sp.expand(sp.simplify(e/x**(p - 4)))
        rows.append([e.coeff(bb), e.coeff(cc)])
    return sp.factor(sp.Matrix(rows).det()), p, lin['L0']


def order_zero(sp):
    """The regular-centre analogue of eq. (8): tt and ll at x^0, all symbolic."""
    S = build(sp)
    T = source(sp, S, CONSERVED)
    K2, L0 = sp.symbols('K2 L0')
    b2, c3, b4, c5 = sp.symbols('b2 c3 b4 c5')
    x = sp.Symbol('x', positive=True)
    fs = sp.exp(L0)*(1 + b2*x**2 + b4*x**4)
    rs = x + c3*x**3 + c5*x**5
    l = S['l']
    out = []
    for i in (0, 1):
        rep = {}
        for k in range(4, -1, -1):
            rep[sp.diff(S['fF'], l, k)] = sp.diff(fs, x, k)
            rep[sp.diff(S['rF'], l, k)] = sp.diff(rs, x, k)
        e = (S['G'][i] - K2*T[i]).subs(rep).subs(sp.log(fs), L0 + sp.log(1 + b2*x**2 + b4*x**4))
        out.append(sp.factor(sp.expand(sp.series(e, x, 0, 1).removeO()).coeff(x, 0)))
    m = sp.expand(sp.series(rs/2*(1 - sp.diff(rs, x)**2), x, 0, 5).removeO())
    return out, m, (K2, L0, b2, c3, b4, c5, x)


def linearised(sp, S):
    """f = f0 (1 + eps phi), r = l + eps rho about flat space; first-order parts."""
    K2, L0, eps = sp.symbols('K2 L0 epsilon')
    x = sp.Symbol('x', positive=True)
    phi, rho = sp.Function('phi')(x), sp.Function('rho')(x)
    T = source(sp, S, CONSERVED)
    f0 = sp.exp(L0)
    l = S['l']
    eqs, bg = [], []
    for i in range(3):
        rep = {}
        for k in range(4, -1, -1):
            rep[sp.diff(S['fF'], l, k)] = sp.diff(f0*(1 + eps*phi), x, k)
            rep[sp.diff(S['rF'], l, k)] = sp.diff(x + eps*rho, x, k)
        e = (S['G'][i] - K2*T[i]).subs(rep)
        e = e.subs(sp.log(f0*(1 + eps*phi)), L0 + sp.log(1 + eps*phi))
        bg.append(sp.simplify(e.subs(eps, 0)))
        eqs.append(sp.expand(sp.simplify(sp.diff(e, eps).subs(eps, 0))))
    return dict(eqs=eqs, bg=bg, K2=K2, L0=L0, x=x, phi=phi, rho=rho)


def modes(sp):
    """The spherical-wave ansatz: conditions on (A, B, k), the dispersion roots,
    and exact residuals of the two modes."""
    S = build(sp)
    lin = linearised(sp, S)
    x, phi, rho, K2, L0 = lin['x'], lin['phi'], lin['rho'], lin['K2'], lin['L0']
    A, B, k = sp.symbols('A B k')

    def plug(e, u, ph):
        e = e.subs({sp.Derivative(rho, (x, n)): sp.diff(u, x, n - 1) for n in (4, 3, 2)}).subs(
            sp.Derivative(rho, x), u)
        e = e.subs({sp.Derivative(phi, (x, n)): sp.diff(ph, x, n) for n in (4, 3, 2)}).subs(
            sp.Derivative(phi, x), sp.diff(ph, x))
        return sp.simplify(e)
    # only derivatives of rho and phi occur -- checked: no bare rho or phi
    bare = [any((t.has(rho) or t.has(phi)) and not t.has(sp.Derivative)
                for t in sp.Add.make_args(e)) for e in lin['eqs']]
    u = B*(sp.sin(k*x) - k*x*sp.cos(k*x))/x
    ph = A*sp.sin(k*x)/x
    conds = []
    for e in lin['eqs']:
        r_ = sp.expand(sp.expand_trig(sp.expand(plug(e, u, ph)*x**5)))
        cs = sp.collect(r_, [sp.sin(k*x), sp.cos(k*x)], evaluate=False)
        for v in cs.values():
            conds.append(sp.factor(v))
    # the conditions are linear in (A, B); strip their x-power prefactors and
    # take the coefficient rows -- the matrix is DERIVED, never typed
    rows = []
    for cnd in conds:
        pa = sp.Poly(sp.expand(cnd), A, B)
        ra = [pa.coeff_monomial(A), pa.coeff_monomial(B)]
        g = sp.gcd(ra[0], ra[1])
        ra = [sp.factor(sp.cancel(v/g)) for v in ra]
        if all(sp.simplify(ra[0]*o[1] - ra[1]*o[0]) != 0 for o in rows) or not rows:
            rows.append(ra)
    M = sp.Matrix(rows[:2])
    s = sp.Symbol('s')     # s = 16 K^2 k^2
    disp = sp.factor(sp.expand(M.det().subs(k**2, s/(16*K2))))
    roots = sp.solve(disp, s)
    resid = []
    for kk2, ratio in ((1/(16*K2), -2), (1/(16*K2*(3*L0 + 4)), 4)):
        kk = sp.sqrt(kk2)
        uu = (sp.sin(kk*x) - kk*x*sp.cos(kk*x))/x
        pp = ratio*sp.sin(kk*x)/x
        resid.append([sp.simplify(plug(e, uu, pp)) for e in lin['eqs']])
    return dict(conds=conds, M=M, disp=disp, roots=roots, resid=resid, bare=bare, nrows=len(rows),
                bg=lin['bg'], K2=K2, L0=L0, A=A, B=B, k=k)


def sign_change_identities(sp):
    """The integrals the linear sign-change theorem uses, verified exactly:
      INT_0^T h      = B1 sin(k1 T) + B2 sin(k2 T)                 (bounded)
      INT_0^T h^2    = T (B1^2 k1^2 + B2^2 k2^2)/2 + W(T)            (W bounded)
    with h = B1 k1 cos(k1 x) + B2 k2 cos(k2 x), k1 != k2, and
      m(x) = x h(x) - B1 sin(k1 x) - B2 sin(k2 x)  for the linear mode sum."""
    x, T = sp.symbols('x T', positive=True)
    B1, B2 = sp.symbols('B1 B2', real=True)
    k1, k2 = sp.symbols('k1 k2', positive=True)
    h = B1*k1*sp.cos(k1*x) + B2*k2*sp.cos(k2*x)
    I1 = sp.integrate(h, (x, 0, T), conds='none')
    w = (B1**2*k1*sp.sin(2*k1*T)/4 + B2**2*k2*sp.sin(2*k2*T)/4
         + B1*B2*k1*k2*(sp.sin((k1 - k2)*T)/(k1 - k2) + sp.sin((k1 + k2)*T)/(k1 + k2)))
    I2 = sp.integrate(sp.expand(h**2), (x, 0, T), conds='none')
    I2 = I2.args[-1][0] if isinstance(I2, sp.Piecewise) else I2
    G = lambda kk, B: -B*(sp.sin(kk*x) - kk*x*sp.cos(kk*x))
    mdef = G(k1, B1) + G(k2, B2)
    return dict(I1=sp.simplify(I1 - B1*sp.sin(k1*T) - B2*sp.sin(k2*T)),
                I2=sp.simplify(sp.expand_trig(I2 - T*(B1**2*k1**2 + B2**2*k2**2)/2 - w)),
                mform=sp.simplify(mdef - (x*h - B1*sp.sin(k1*x) - B2*sp.sin(k2*x))))


def linear_m(L0, b2, c3):
    """Exact linear m(x) (K = 1) for centre data (b2, c3), 3 L0 + 4 > 0."""
    import numpy as np
    k1 = 0.25
    k2 = 0.25/math.sqrt(3*L0 + 4)
    B1 = (6*c3 + b2)/k1**3
    B2 = (3*c3 - b2)/k2**3
    return lambda x: -(B1*(np.sin(k1*x) - k1*x*np.cos(k1*x)) + B2*(np.sin(k2*x) - k2*x*np.cos(k2*x)))


def mode_data(sp):
    """Taylor data of C + A1 sin(k1 x)/x + A2 sin(k2 x)/x (phi) and of the rho
    whose derivative is B1 G1/x + B2 G2/x, with A1 = -2 B1, A2 = 4 B2: solve for
    (B1, B2, C) given f(0) = f0 (phi(0) = 0), b2 and c3.  Derived, not typed:
    linear_m() uses the result, and the selftest compares the two."""
    x = sp.Symbol('x', positive=True)
    B1, B2, C, b2, c3 = sp.symbols('B1 B2 C b2 c3')
    k1, k2 = sp.symbols('k1 k2', positive=True)
    phi = C - 2*B1*sp.sin(k1*x)/x + 4*B2*sp.sin(k2*x)/x
    rhop = B1*(sp.sin(k1*x) - k1*x*sp.cos(k1*x))/x + B2*(sp.sin(k2*x) - k2*x*sp.cos(k2*x))/x
    ps = sp.series(phi, x, 0, 4).removeO()
    rs = sp.integrate(sp.series(rhop, x, 0, 4).removeO(), x)
    sol = sp.solve([ps.coeff(x, 0), ps.coeff(x, 2) - b2, rs.coeff(x, 3) - c3], [B1, B2, C], dict=True)[0]
    return sol, (B1, B2, C, b2, c3, k1, k2)


def mode2_L0_for(length_lP):
    """The L0 at which pure mode 2's first sign change of m sits at length_lP:
    4 zeta_1 K sqrt(3 L0 + 4) = length_lP."""
    q = length_lP/(4*zeta_first()*K_in_planck())
    return (q*q - 4)/3


def popov_L(Y):
    """Popov eq. (21) truncated at the printed terms: L^-1 = max(1/r, |u'|,
    |u''|^(1/2), |u'''|^(1/3)), u = ln(f r^2).  Truncation can only RAISE L,
    so a truncated L below l_P is a true L below l_P."""
    import numpy as np
    f, f1, f2, f3, r, r1, r2, r3 = Y
    u1 = f1/f + 2*r1/r
    u2 = f2/f - f1**2/f**2 + 2*r2/r - 2*r1**2/r**2
    u3 = f3/f - 3*f1*f2/f**2 + 2*f1**3/f**3 + 2*r3/r - 6*r1*r2/r**2 + 4*r1**3/r**3
    return 1/np.maximum.reduce([1/np.abs(r), np.abs(u1), np.abs(u2)**0.5, np.abs(u3)**(1/3)])


def K_in_planck():
    """K in l_P: K^2 = 8 pi/(46080 pi^2) = 1/(5760 pi).  The ONLY place K has a
    value; nothing in this file types it."""
    return 1/math.sqrt(5760*math.pi)


def mode2_first_lp_range(lnf0_range=HPS_LNF0_RANGE):
    """First sign change of pure mode 2, 4 zeta_1 K sqrt(3 L0 + 4), in l_P, at
    the two ends of an ln f(0) range (monotone in L0, so these bound it).
    Computed from HPS_LNF0_RANGE -- the factor is never typed (ruling B2)."""
    z = 4*zeta_first()*K_in_planck()
    return tuple(z*math.sqrt(3*L + 4) for L in lnf0_range)


def zeta_first():
    """First positive root of tan y = y: where sin y - y cos y first changes sign."""
    import mpmath
    return float(mpmath.findroot(lambda y: mpmath.tan(y) - y, 4.49))


# ============================================================ the far zone
def far_zone_fit(res, lo, hi, sampling, n=200001):
    """sqrt f = a ln x - b, least squares over [lo, hi] (K), sampled linearly
    ('lin') or log-uniformly ('log').  Returns (a, b), or None if the run
    does not reach hi."""
    import numpy as np
    if hi > res.t[-1] * (1 + 1e-12):
        return None
    xs = np.linspace(lo, hi, n) if sampling == "lin" else np.geomspace(lo, hi, n)
    a, mb = np.polyfit(np.log(xs), np.sqrt(res.sol(xs)[0]), 1)
    return float(a), float(-mb)


def matches_hps(ab, tol=MATCH_TOL):
    """Both fitted coefficients within tol (relative) of HPS's printed a, b."""
    a, b = ab
    return (abs(a - HPS_A_PRINTED) / HPS_A_PRINTED <= tol
            and abs(b - HPS_B_PRINTED) / HPS_B_PRINTED <= tol)


def attribution(sweep, tol=MATCH_TOL):
    """sweep: {system: {window: (a, b)}}.  A system is CLAIMED only if, in EVERY
    window both systems were fitted in, it and it alone matches HPS's (a, b).
    Any window where neither, or both, or the other one matches makes the
    verdict "NOT DETERMINED" -- so a discrimination read in one window FAILS as
    soon as another window disagrees (ruling B2)."""
    systems = sorted(sweep)
    windows = [w for w in sweep[systems[0]]
               if all(sweep[s].get(w) is not None for s in systems)]
    if not windows:
        return "NOT DETERMINED"
    winners = set()
    for w in windows:
        hit = [s for s in systems if matches_hps(sweep[s][w], tol)]
        if len(hit) != 1:
            return "NOT DETERMINED"
        winners.add(hit[0])
    return winners.pop().upper() if len(winners) == 1 else "NOT DETERMINED"


def spread(fits):
    """(min a, max a, min b, max b) over the windows a run reached."""
    ab = [v for v in fits.values() if v is not None]
    return (min(v[0] for v in ab), max(v[0] for v in ab),
            min(v[1] for v in ab), max(v[1] for v in ab))


def ripple_count(xs, m, lo, hi, width):
    """Of the windows [e, e + width) tiling [lo, hi), how many contain m < 0."""
    import numpy as np
    edges = np.arange(lo, hi - width, width)
    i0 = np.searchsorted(xs, edges)
    i1 = np.searchsorted(xs, edges + width)
    hits = sum(bool((m[a:b] < 0).any()) for a, b in zip(i0, i1))
    return int(hits), int(len(edges))


# ============================================================ runs
def throat_runs(sp, X=10000, windows=FAR_ZONE_WINDOWS):
    """HPS eq. (9), ln f(0) = -2/3, in both readings: ripple spacing, the
    far-zone window sweep, first m < 0 (and, conserved, by two more
    integrators), the per-window m < 0 count, Popov L at m < 0 points, and the
    ll residual RELATIVE to the Einstein-side scale (the printed trajectory's
    also under M2 read as printed, r^1)."""
    import numpy as np
    out = {}
    L0 = sp.Rational(*HPS_LNF0_RUN)
    r0 = float(sp.sqrt(-16*L0))
    y0 = [math.exp(float(L0)), 0, 0, 0, r0, 0, 0, 0]
    ll_m2_printed = constraint(sp, PRINTED)
    for name, reading in (("printed", PRINTED_M1), ("conserved", CONSERVED)):
        num = numeric_system(sp, reading)
        res = integrate(num, y0, 0, X, rtol=1e-10)
        xs = np.linspace(1, res.t[-1], 400001)
        Y = res.sol(xs)
        m = misner_sharp(Y)
        r1 = Y[5]
        dd = np.diff(np.sign(np.diff(r1)))
        ext = xs[1:-1][dd != 0]
        ext = ext[(ext > 50) & (ext < 1000)]
        xneg, _ = first_negative(res, 0, 50)
        Lp = popov_L(Y)
        neg = m < 0
        onset = neg & (xs < 50)
        Ys = Y[:8, ::4000]
        rel = np.abs(num['ll'](*Ys)) / ll_scale(Ys)
        fits = {w: far_zone_fit(res, *w) for w in windows}
        hits, nwin = ripple_count(xs, m, RIPPLE_COUNT_RANGE_K[0],
                                  min(RIPPLE_COUNT_RANGE_K[1], res.t[-1]), RIPPLE_WINDOW_K)
        d = dict(status=res.status, end=float(res.t[-1]), spacing=float(np.median(np.diff(ext))),
                 fits=fits, xneg=xneg, ripple=(hits, nwin),
                 Lmax_neg=float(Lp[neg].max()), Lonset=float(Lp[onset].max()),
                 mmin=float(m.min()), r1max=float(r1.max()),
                 ll_abs=float(np.abs(num['ll'](*Ys)).max()),
                 ll_rel_max=float(rel.max()), ll_rel_median=float(np.median(rel)),
                 gap_min=float(np.abs(3*np.log(Y[0]) + 4).min()),
                 rmin=float(Y[4].min()), fmin=float(Y[0].min()))
        if name == "printed":
            relp = np.abs(ll_m2_printed(*Ys)) / ll_scale(Ys)
            d['ll_rel_median_m2_printed'] = float(np.median(relp))
            d['ll_rel_max_m2_printed'] = float(relp.max())
        else:
            d['xneg_other'] = {}
            for meth in ("Radau", "LSODA"):
                r2 = integrate(num, y0, 0, 50, rtol=1e-10, method=meth)
                d['xneg_other'][meth] = first_negative(r2, 0, 50)[0]
        out[name] = d
    out['sweep'] = {nm: out[nm]['fits'] for nm in ("printed", "conserved")}
    return out


def centre_runs(sp):
    """Regular-centre integrations at L0 = 0, b2 = 0 (K = 1)."""
    import numpy as np
    num = numeric_system(sp, CONSERVED)
    out = {'det': num['detA']}
    x0 = 0.02
    scal = []
    for e in (4, 5, 6):
        c3 = sp.Rational(1, 10**e)
        cs = centre_series(sp, num, 0, 0, c3)
        res = integrate(num, [float(v) for v in cs['y0'](x0)], x0, 60, rtol=1e-12)
        xs = np.linspace(x0, 60, 3001)
        m = misner_sharp(res.sol(xs))
        ml = linear_m(0.0, 0.0, float(c3))(xs)
        scal.append(float(abs(m - ml).max()/abs(ml).max()))
        if e == 4:
            out['series'] = cs
            out['m_near_centre'] = float(m[:50].max())
            Y = res.sol(xs)
            out['ll_c'] = float(max(abs(num['ll'](*Y[:, i])) for i in range(0, 3001, 100)))
    out['scaling'] = scal
    # c3 < 0: m > 0 at the centre; first m < 0 against the exact linear radius
    c3 = -sp.Rational(1, 10**6)
    cs = centre_series(sp, num, 0, 0, c3)
    res = integrate(num, [float(v) for v in cs['y0'](x0)], x0, 80, rtol=1e-12)
    xneg, at0 = first_negative(res, x0, 80)
    from scipy.optimize import brentq
    ml = linear_m(0.0, 0.0, float(c3))
    grid = np.linspace(1, 80, 80001)
    v = ml(grid)
    i = np.where((v[:-1] >= 0) & (v[1:] < 0))[0][0]
    xlin = brentq(ml, grid[i], grid[i+1], xtol=1e-12)
    out['neg_c3'] = (xneg, at0, xlin)
    # pure modes: first sign change of m for b2 = 3 c3 (mode 1) and b2 = -6 c3 (mode 2)
    out['mode1_first'] = zeta_first()*4
    out['mode2_first'] = zeta_first()*4*math.sqrt(3*CENTRE_L0 + 4)
    # large amplitude: termination at 3 ln f + 4 = 0; Popov L at m < 0 points
    big = {}
    for c3 in (sp.Rational(1, 100), sp.Rational(1, 10)):
        cs = centre_series(sp, num, 0, 0, c3)
        res = integrate(num, [float(v) for v in cs['y0'](x0)], x0, 300)
        y = res.y[:, -1]
        xs = np.linspace(x0, res.t[-1]*0.999, 4001)
        Y = res.sol(xs)
        m = misner_sharp(Y)
        Lp = popov_L(Y)
        big[str(c3)] = dict(status=res.status, end=float(res.t[-1]), gap=float(3*math.log(y[0]) + 4),
                            all_neg=bool((m < 0).all()), Lmax=float(Lp[m < 0].max()))
    out['big'] = big
    # small amplitude far out: the truncated Popov L is NOT uniformly sub-Planck
    cs = out['series']
    res = integrate(num, [float(v) for v in cs['y0'](x0)], x0, 300)
    xs = np.linspace(x0, 300, 20001)
    Y = res.sol(xs)
    m = misner_sharp(Y)
    out['small_Lmax_neg'] = float(popov_L(Y)[m < 0].max())
    # asymptotic flatness, measured: amplitude of 2m/r in two far windows
    w1 = (xs > 150) & (xs < 200)
    w2 = (xs > 250) & (xs < 300)
    out['twomr'] = (float(np.abs(2*m/Y[4])[w1].max()), float(np.abs(2*m/Y[4])[w2].max()))
    return out


# ============================================================ report / selftest
def _need():
    try:
        import sympy as sp
        import numpy   # noqa: F401
        import scipy   # noqa: F401
        import mpmath  # noqa: F401
    except ImportError as exc:          # pragma: no cover
        raise SystemExit("hpscentre.py needs sympy, numpy, scipy, mpmath: %s" % exc)
    return sp


def _fmt_fit(v):
    return "(%.3f, %.3f)" % v if v is not None else "(not reached)"


def print_sweep(t, Kp):
    """The window-sweep row: every window's (a, b) for both systems, the
    spread, and the attribution verdict (ruling B2)."""
    print("   far-zone sqrt f = a ln x - b, by window (K; sampling) -- HPS print (%.1f, %.1f):"
          % (HPS_A_PRINTED, HPS_B_PRINTED))
    for w in t['sweep']['printed']:
        print("     [%6d, %6d] %-3s  printed %-18s conserved %s"
              % (w[0], w[1], w[2], _fmt_fit(t['sweep']['printed'][w]),
                 _fmt_fit(t['sweep']['conserved'][w])))
    for nm in ("printed", "conserved"):
        amin, amax, bmin, bmax = spread(t['sweep'][nm])
        print("   SPREAD %-9s a in [%.3f, %.3f], b in [%.3f, %.3f]" % (nm, amin, amax, bmin, bmax))
    one = {nm: {WITHDRAWN_ATTRIBUTION_WINDOW: t['sweep'][nm][WITHDRAWN_ATTRIBUTION_WINDOW]}
           for nm in ("printed", "conserved")}
    print("   attribution, window %s alone (the WITHDRAWN reading): %s"
          % (WITHDRAWN_ATTRIBUTION_WINDOW, attribution(one)))
    print("   attribution, every window: %s   (HPS_INTEGRATED_THE_PRINTED_SYSTEM = %r)"
          % (attribution(t['sweep']), HPS_INTEGRATED_THE_PRINTED_SYSTEM))


def report(full=False):
    sp = _need()
    Kp = K_in_planck()
    lp = throatmass.planck_length()
    print(__doc__.split("=====", 1)[0].strip())
    S = build(sp)
    d = printed_differences(sp, S)
    print("\n1. PRINTED HPS minus PRINTED POPOV (non-log | log, sign-flipped):")
    for nm, (a, b) in zip(("tt", "ll", "thth"), d):
        print("   %-5s %s | %s" % (nm, a, b))
    print("   disagreements (components whose log parts differ): %d" % count_disagreements(d))
    print("   conservation residual, conserved reading: %s"
          % divergence(sp, S, source(sp, S, CONSERVED)))
    print("   conservation residual, printed reading:   %s"
          % divergence(sp, S, source(sp, S, PRINTED)))
    det, p, L0 = recursion_det(sp)
    print("\n2. REGULAR CENTRE: recursion determinant = %s" % det)
    print("   %s" % RECURSION_DIRECTION)
    md = modes(sp)
    print("   linear dispersion (s = 16 K^2 k^2): %s = 0, roots %s" % (md['disp'], md['roots']))
    X = 100000 if full else 10000
    t = throat_runs(sp, X=X, windows=FAR_ZONE_WINDOWS + (FAR_ZONE_WINDOWS_FULL if full else ()))
    print("\n3. HPS THROAT (ln f(0) = -2/3), K = 1 units, integrated to x = %g K:" % X)
    for nm in ("printed", "conserved"):
        v = t[nm]
        print("   %-9s ripple spacing %.4f (pi/omega_1 = %.4f); first m<0 at x = %.6f = %.4f l_P; "
              "max r' = %.3f; min m = %.4g" % (nm, v['spacing'], 4*math.pi, v['xneg'], v['xneg']*Kp,
                                              v['r1max'], v['mmin']))
        print("             8 pi K windows in [%g, %g] K containing m < 0: %d of %d"
              % (RIPPLE_COUNT_RANGE_K[0], min(RIPPLE_COUNT_RANGE_K[1], v['end']),
                 v['ripple'][0], v['ripple'][1]))
        print("             ll residual / Einstein-side scale: median %.3g, max %.3g "
              "(absolute max %.2g -- NOT the figure to read)"
              % (v['ll_rel_median'], v['ll_rel_max'], v['ll_abs']))
        print("             min |3 ln f + 4| along the run %.4f (uniqueness hypothesis)" % v['gap_min'])
        print("             Popov L at m<0 points: onset (x<50) <= %.3f K = %.4f l_P; all x <= %.1f K = %.3f l_P"
              % (v['Lonset'], v['Lonset']*Kp, v['Lmax_neg'], v['Lmax_neg']*Kp))
    v = t['printed']
    print("   printed, M2 read as printed (r^1): ll relative median %.3g, max %.3g"
          % (v['ll_rel_median_m2_printed'], v['ll_rel_max_m2_printed']))
    print("   => the printed reading has NO solution of all three equations from eq. (9)'s data;"
          " the throat m < 0 claim is the CONSERVED system's")
    print("   conserved first m<0 by Radau %.7f, LSODA %.7f (DOP853 %.7f)"
          % (t['conserved']['xneg_other']['Radau'], t['conserved']['xneg_other']['LSODA'],
             t['conserved']['xneg']))
    print_sweep(t, Kp)
    c = centre_runs(sp)
    print("\n4. REGULAR CENTRE, NONLINEAR (L0 = %d, b2 = 0):" % CENTRE_L0)
    print("   deviation from exact linear m at c3 = 1e-4, 1e-5, 1e-6: %s" % c['scaling'])
    print("   c3 = -1e-6: first m<0 at x = %.6f (linear theory %.6f)" % (c['neg_c3'][0], c['neg_c3'][2]))
    print("   pure mode 1 first sign change: x = %.4f K = %.4f l_P = %.3e m"
          % (c['mode1_first'], c['mode1_first']*Kp, c['mode1_first']*Kp*lp))
    lo_lp, hi_lp = mode2_first_lp_range()
    print("   pure mode 2 first sign change: x = %.4f K sqrt(3 L0 + 4); over HPS_LNF0_RANGE %s: "
          "from %.4f l_P to < %.4f l_P" % (c['mode1_first'], HPS_LNF0_RANGE, lo_lp, hi_lp))
    print("   L0 needed to put it at 1 l_P: %.4f ; at 1 m: %.4e" % (mode2_L0_for(1.0), mode2_L0_for(1/lp)))
    for k_, v in c['big'].items():
        print("   c3 = %s: stops at x = %.4f with 3 ln f + 4 = %.2e; m < 0 throughout: %s; "
              "L <= %.3f K = %.4f l_P" % (k_, v['end'], v['gap'], v['all_neg'], v['Lmax'], v['Lmax']*Kp))
    print("   c3 = 1e-4 over x <= 300: Popov L at m<0 points reaches %.2f K = %.3f l_P"
          % (c['small_Lmax_neg'], c['small_Lmax_neg']*Kp))
    print("   max |2m/r| on 150<x<200 and 250<x<300 (c3 = 1e-4 ONLY): %.3e, %.3e (not decaying)"
          % c['twomr'])
    print("   nonlinear non-flatness: %s; asymptotics %s" % (NONLINEAR_CENTRE_NONFLATNESS,
                                                          NONLINEAR_CENTRE_ASYMPTOTICS))
    print("\nWITHDRAWN (kept, with why):")
    for claim, why in WITHDRAWN:
        print("   - %s\n       %s" % (claim, why))
    print("\nO5: OPEN.  m < 0 FOUND in HPS's system, conserved reading (regular centre and"
          " eq. (9) throat data); FOUND INSIDE the domain the approximation is established in:"
          " NO.  Which system HPS integrated: %s." % HPS_INTEGRATED_THE_PRINTED_SYSTEM)
    print("WOULD BE ANSWERED BY: %s" % O5_ANSWERED_BY)
    return 0


def count_disagreements(d):
    """Components whose (sign-flipped) log parts differ between the two
    printings, the non-log parts being identical."""
    return sum(1 for nl, lg in d if nl == 0 and lg != 0)


def selftest():
    sp = _need()
    import numpy as np  # noqa: F401
    ok = True
    records = []

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-66s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        dd = abs(got - want)/max(1e-300, abs(want))
        good = dd <= tol
        ok &= good
        print("  [%s] %-66s %.10g (rel %.1e)" % ("ok" if good else "XX", label, got, dd))

    def record(label, value):
        """A RECORD PIN: a READ or ruled value printed, NOT counted as a check
        (it compares nothing computed and cannot fail)."""
        records.append(label)
        print("  [RECORD] %-62s %s" % (label, value))

    S = build(sp)
    f, f1, f2 = S['F'][:3]
    r, r1 = S['R'][:2]

    print("1. THE EINSTEIN SIDE (from the metric) AND ITS BIANCHI IDENTITY")
    C = curvature(sp, S)
    chk("G^t_t, G^l_l, G^th_th = HPS's printed left sides",
        [sp.simplify(a - b) for a, b in zip(C['G'], S['G'])], [0, 0, 0])
    chk("div G = 0 (Bianchi)", divergence(sp, S, S['G']), 0)
    bad = (S['G'][0], S['G'][1], S['G'][2] + f1**2/(4*f**2))
    chk("  CONTROL: a G^th_th missing -f'^2/4f^2 FAILS it", divergence(sp, S, bad) != 0, True)

    print("\n2. TWO INDEPENDENT PRINTINGS OF THE SOURCE (HPS 5-7, Popov B1-B3)")
    d = printed_differences(sp, S)
    chk("non-log parts identical, all three components", [x[0] for x in d], [0, 0, 0])
    chk("M1: tt log differs by exactly -100 f'^2 f''/f^3 (text layer 16 vs 116)",
        sp.simplify(d[0][1] + 100*f1**2*f2/f**3), 0)
    chk("M2: ll log differs by exactly the f^2 r / f^2 r^2 slot",
        sp.simplify(d[1][1] - (4*f1**2*r1**2/(f**2*r**2) - 4*f1**2*r1**2/(f**2*r))), 0)
    chk("M3: thth log differs by exactly +21 f'^4/f^4 (Popov drops it)",
        sp.simplify(d[2][1] - 21*f1**4/f**4), 0)
    chk("THREE disagreements, counted from the differences (fixture %d)" % PRINTED_DISAGREEMENTS,
        count_disagreements(d), PRINTED_DISAGREEMENTS)
    chk("homogeneity: printed reading has exactly 1 non-length^-4 term",
        homogeneity(sp, S, PRINTED), 1)
    chk("homogeneity: conserved reading has none", homogeneity(sp, S, CONSERVED), 0)

    print("\n3. CONSERVATION PICKS ONE READING OF FOUR")
    for att in (16, 116):
        for ath in (0, 21):
            rd = dict(a_tt=att, a_th=ath, ll_pow=2)
            res = divergence(sp, S, source(sp, S, rd))
            chk("  (a_tt, a_th) = (%3d, %2d): conserved" % (att, ath), res == 0,
                (att, ath) == (116, 21))
    chk("  the printed reading (16, 21, r^1) is NOT conserved",
        divergence(sp, S, source(sp, S, PRINTED)) != 0, True)

    print("\n4. THE TRACE")
    fit, trl = trace_fit(sp, S, C, CONSERVED)
    chk("ln f part traceless (conserved reading)", trl, 0)
    _, trl_p = trace_fit(sp, S, C, PRINTED)
    chk("  CONTROL: printed reading's ln f part is NOT traceless", trl_p != 0, True)
    a, b, c = sp.symbols('a b c')
    chk("non-log trace = 16 [C^2 + (Ric^2 - R^2/3) + box R] exactly",
        (fit[a], fit[b], fit[c]) if fit else None, (16, 16, 16))
    ahl = sp.simplify(8*sp.pi*sp.Rational(AHL_ALPHA_BETA_TIMES_2880PI2, 2880)/sp.pi**2
                      * 5760*sp.pi)
    chk("  b and c equal 8 pi alpha / K^2 at AHL eq.(6)'s alpha = beta",
        (fit[b], fit[c]) if fit else None, (ahl, ahl))

    print("\n5. FLAT SPACE")
    fv = flat_values(sp, S, CONSERVED)
    chk("source vanishes on f = f_0, r = l", list(fv[0]), [0, 0, 0])
    chk("  CONTROL: source does not vanish on r = l + l^3", any(v != 0 for v in fv[1]), True)

    print("\n6. HPS's THROAT -- eq. (8), eq. (9), and the flare")
    qrt, s1, s2, nine, _ = quartic(sp, S)
    t1, t2 = throatmass.hps_quartic(sp)
    chk("eq.(8) re-derived: case-1 root = throatmass.hps_quartic()'s, exactly",
        [sp.simplify(u - v) for u, v in zip(s1, t1)] if len(s1) == len(t1) else None, [0])
    chk("eq.(8) re-derived: case-2 root = throatmass.hps_quartic()'s, exactly",
        [sp.simplify(u - v) for u, v in zip(s2, t2)] if len(s2) == len(t2) else None, [0])
    chk("  case 1 = sqrt(15)/(90 sqrt(pi)) l_P, exactly",
        sp.simplify(s1[0] - sp.sqrt(15)/(90*sp.sqrt(sp.pi))) if s1 else None, 0)
    chk("  case 2 = 12 sqrt(10 pi) l_P, exactly",
        sp.simplify(s2[0] - 12*sp.sqrt(10*sp.pi)) if s2 else None, 0)
    chk("eq.(9) r(0) = sqrt(-16 K^2 ln f(0)) solves it for every ln f(0) < 0", nine, 0)
    num_c = numeric_system(sp, CONSERVED)
    chk("4th-order determinant is -256 (3 ln f + 4)/(f r) (K = 1)",
        sp.simplify(num_c['detA'] + 256*(3*sp.log(num_c['Sy'][0]) + 4)/(num_c['Sy'][0]*num_c['Sy'][5])), 0)
    L0 = sp.Rational(*HPS_LNF0_RUN)
    vals = {num_c['Sy'][0]: sp.exp(L0), num_c['Sy'][1]: 0, num_c['Sy'][2]: 0, num_c['Sy'][3]: 0,
            num_c['Sy'][5]: sp.sqrt(-16*L0), num_c['Sy'][6]: 0, num_c['Sy'][7]: 0, num_c['Sy'][8]: 0}
    Asub = sp.Matrix([[sp.diff(num_c['E'][i], num_c['Sy'][j]) for j in (4, 9)] for i in (0, 2)]).subs(vals)
    bsub = sp.Matrix([num_c['E'][i].subs({num_c['Sy'][4]: 0, num_c['Sy'][9]: 0}) for i in (0, 2)]).subs(vals)
    d4 = [sp.nsimplify(sp.simplify(v)) for v in Asub.solve(-bsub)]
    chk("at eq.(9) data: ll constraint holds exactly", sp.simplify(num_c['E'][1].subs(vals)), 0)
    chk("at eq.(9) data: r''''(0) = 7 sqrt(6)/768 > 0 (a minimum, as Fig. 2a)",
        sp.simplify(d4[1] - 7*sp.sqrt(6)/768), 0)
    t = throat_runs(sp)
    tc, tp = t['conserved'], t['printed']
    for nm in ("printed", "conserved"):
        near("%s: ripple spacing = pi/omega_1 = 4 pi K (1 %%)" % nm, t[nm]['spacing'], 4*math.pi, 1e-2)
    print("  -- the conserved system (the claim):")
    chk("conserved throat: r' > 1 in the flare, so m < 0 (first at x < 8 K)",
        (tc['r1max'] > 1, tc['xneg'] is not None and tc['xneg'] < 8), (True, True))
    for meth in ("Radau", "LSODA"):
        near("  first m < 0 reproduced by %s (independent integrator)" % meth,
             tc['xneg_other'][meth], tc['xneg'], 1e-7)
    chk("  FIRST_NEGATIVE_M_THROAT_LP = first_negative x K_in_planck(), 4 places",
        round(tc['xneg']*K_in_planck(), 4), FIRST_NEGATIVE_M_THROAT_LP)
    hits, nwin = tc['ripple']
    chk("  m < 0 in EVERY 8 pi K window, 50 K..1e4 K (%d of %d)" % (hits, nwin),
        (hits == nwin, nwin > 300), (True, True))
    chk("  conserved ll residual < 1e-6 of the Einstein-side scale (max)",
        tc['ll_rel_max'] < 1e-6, True)
    chk("  Popov L < l_P = 1/K where m < 0 first appears (x < 50 K)",
        tc['Lonset'] < 1/K_in_planck(), True)
    chk("  but NOT at every m < 0 point: conserved throat's far shells exceed l_P",
        tc['Lmax_neg'] > 1/K_in_planck(), True)
    chk("M_NEGATIVE_FOUND_IN_HPS_SYSTEM agrees with the conserved throat run",
        M_NEGATIVE_FOUND_IN_HPS_SYSTEM, tc['xneg'] is not None and tc['mmin'] < 0)
    print("  -- the printed reading: NO three-equation solution from eq. (9)'s data:")
    chk("  HYPOTHESIS: tt+thth uniquely determine the run (|3 ln f + 4|, r, f > 0.1)",
        (tp['gap_min'] > 0.1, tp['rmin'] > 0.1, tp['fmin'] > 0.1), (True, True, True))
    chk("  printed trajectory breaks ll by ORDER ONE: relative median > 0.1",
        tp['ll_rel_median'] > 0.1, True)
    chk("  ... and with M2 read as printed (r^1): relative median > 0.1",
        tp['ll_rel_median_m2_printed'] > 0.1, True)
    chk("  PRINTED_READING_HAS_THREE_EQUATION_SOLUTION_FROM_EQ9 agrees",
        PRINTED_READING_HAS_THREE_EQUATION_SOLUTION_FROM_EQ9,
        not (tp['ll_rel_median'] > 0.1 and tp['ll_rel_median_m2_printed'] > 0.1))
    chk("  CONTROL: the same measure on the conserved run is < 1e-6 (so it can tell)",
        tc['ll_rel_median'] < 1e-6, True)

    print("\n6b. THE FAR ZONE -- WINDOW SWEEP (which system HPS integrated)")
    for w in FAR_ZONE_WINDOWS:
        print("  [sweep] %-22s printed %-18s conserved %s"
              % (str(w), _fmt_fit(t['sweep']['printed'][w]), _fmt_fit(t['sweep']['conserved'][w])))
    for nm in ("printed", "conserved"):
        amin, amax, bmin, bmax = spread(t['sweep'][nm])
        print("  [spread] %-9s a in [%.3f, %.3f]  b in [%.3f, %.3f]" % (nm, amin, amax, bmin, bmax))
    one = {nm: {WITHDRAWN_ATTRIBUTION_WINDOW: t['sweep'][nm][WITHDRAWN_ATTRIBUTION_WINDOW]}
           for nm in ("printed", "conserved")}
    chk("WITHDRAWN BASIS REPRODUCED: window %s alone attributes PRINTED"
        % (WITHDRAWN_ATTRIBUTION_WINDOW,), attribution(one), "PRINTED")
    chk("THE SWEEP REFUSES IT: attribution over every window = the recorded flag",
        attribution(t['sweep']), HPS_INTEGRATED_THE_PRINTED_SYSTEM)
    disjoint = ((500, 2000, "lin"), (2000, 5000, "lin"), (5000, 10000, "lin"))
    for nm in ("printed", "conserved"):
        av = [t['sweep'][nm][w][0] for w in disjoint]
        chk("  %s: a rises across disjoint windows (not converged)" % nm,
            av[0] < av[1] < av[2], True)
    # CONTROLS on attribution() itself: agreeing windows are claimed; one
    # disagreeing window makes the same claim FAIL.
    good = (HPS_A_PRINTED, HPS_B_PRINTED)
    far = (2*HPS_A_PRINTED, 2*HPS_B_PRINTED)
    agree = {"printed": {1: good, 2: good}, "conserved": {1: far, 2: far}}
    split = {"printed": {1: good, 2: far}, "conserved": {1: far, 2: far}}
    swap = {"printed": {1: good, 2: far}, "conserved": {1: far, 2: good}}
    chk("  CONTROL: attribution() claims a system when every window agrees",
        attribution(agree), "PRINTED")
    chk("  CONTROL: the same claim FAILS if one window has no match",
        attribution(split), "NOT DETERMINED")
    chk("  CONTROL: ... and FAILS if the windows name different systems",
        attribution(swap), "NOT DETERMINED")

    print("\n7. REGULAR CENTRE, FORMAL SERIES -- THEOREM ('if' direction)")
    det, p, L0s = recursion_det(sp)
    chk("recursion determinant = -512 p (3L0+4)(p-2)^2 (p-1)(p+1)^3",
        sp.expand(det + 512*p*(3*L0s + 4)*(p - 2)**2*(p - 1)*(p + 1)**3), 0)
    chk("  its non-negative roots are p = 0, 1, 2 WHEN L0 != -4/3",
        sorted(v for v in sp.solve(sp.cancel(det/(3*L0s + 4)), p) if v >= 0), [0, 1, 2])
    chk("  at 3 L0 + 4 = 0 the recursion is singular at EVERY p (not analysed)",
        sp.simplify(det.subs(L0s, sp.Rational(-4, 3))), 0)
    #   p = 0 is f0; p = 2 is (b2, c3); p = 1 would put an ODD term in f and
    #   an even one in r -- excluded by the smooth-centre hypothesis, not by
    #   this determinant.  Every even p >= 4 is fixed WHEN 3 L0 + 4 != 0.
    oz, mser, sy = order_zero(sp)
    K2, L0z, b2, c3, b4, c5, x = sy
    chk("m = -3 c3 x^3 + O(x^5)", sp.expand(mser.coeff(x, 3) + 3*c3), 0)
    lead = sp.simplify(mser.coeff(x, 3)/c3)
    chk("  CENTRE_M_LEADING rebuilt from the series (x^0..x^4 otherwise zero)",
        ("m = %s c3 l^3 + O(l^5)" % lead,
         [sp.simplify(mser.coeff(x, k)) for k in (0, 1, 2, 4)]),
        (CENTRE_M_LEADING, [0, 0, 0, 0]))
    Mz = sp.Matrix([[sp.diff(e, v) for v in (b4, c5)] for e in oz])
    detz = sp.factor(Mz.det())
    chk("order x^0: (b4, c5) uniquely solvable WHEN 3 L0 + 4 != 0; singular at -4/3",
        (detz != 0, sp.solve(detz, L0z)), (True, [sp.Rational(-4, 3)]))
    chk("  and eq. (8)'s kind of constraint does not arise: (L0, b2, c3) stay free",
        sp.solve(oz, [b4, c5], dict=True) != [], True)
    cs = centre_series(sp, num_c, CENTRE_L0, 0, sp.Rational(1, 10**4))
    chk("  no negative powers in any equation at the centre", cs['neg'], [0]*12)
    chk("  thth at x^0 and x^2 vanish once tt, ll do (Bianchi)", (cs['th0'], cs['th2']), (0, 0))

    print("\n8. REGULAR CENTRE, LINEARISED -- THEOREM FOR THE LINEARISED SYSTEM ONLY")
    md = modes(sp)
    chk("flat space is a background solution", md['bg'], [0, 0, 0])
    chk("only derivatives of rho, phi enter the linear equations", md['bare'], [False]*3)
    chk("  the ansatz conditions have rank 2 (a 2x2 system in A, B)", md['nrows'], 2)
    sK = sp.Symbol('s')
    chk("dispersion: (3L0+4) s^2 - (3L0+5) s + 1 = 0",
        sp.expand(md['disp'] - ((3*md['L0'] + 4)*sK**2 - (3*md['L0'] + 5)*sK + 1)), 0)
    chk("  roots s = 1, 1/(3L0+4): HPS's omega_1^2 = 1/16K^2, omega_2^2 = 1/16K^2(4+3lnF)",
        sorted([sp.simplify(v) for v in md['roots']], key=str),
        sorted([sp.Integer(1), 1/(3*md['L0'] + 4)], key=str))
    chk("  mode 1 (A = -2B) exact residuals", md['resid'][0], [0, 0, 0])
    chk("  mode 2 (A = 4B) exact residuals", md['resid'][1], [0, 0, 0])
    sc = sign_change_identities(sp)
    chk("INT h = B1 sin k1T + B2 sin k2T, exactly", sc['I1'], 0)
    chk("INT h^2 = T(B1^2 k1^2 + B2^2 k2^2)/2 + bounded, exactly", sc['I2'], 0)
    chk("m = x h(x) - B1 sin k1x - B2 sin k2x, exactly", sc['mform'], 0)
    msol, (B1, B2, Cc, b2s, c3s, k1s, k2s) = mode_data(sp)
    chk("(b2, c3) -> (B1, B2): B1 = (6c3 + b2)/k1^3, B2 = (3c3 - b2)/k2^3 (linear_m's map)",
        (sp.simplify(msol[B1] - (6*c3s + b2s)/k1s**3), sp.simplify(msol[B2] - (3*c3s - b2s)/k2s**3)),
        (0, 0))
    chk("  the map is one-to-one: (b2, c3) = (0, 0) forces B1 = B2 = 0 (flat)",
        (msol[B1].subs({b2s: 0, c3s: 0}), msol[B2].subs({b2s: 0, c3s: 0})), (0, 0))

    print("\n9. REGULAR CENTRE, NONLINEAR -- MEASURED (asymptotics OPEN)")
    c = centre_runs(sp)
    s_ = c['scaling']
    chk("deviation from exact linear m falls 10x per decade of c3 (8x..12x)",
        all(8 < s_[i]/s_[i+1] < 12 for i in range(2)), True)
    chk("  c3 > 0: m < 0 next to the centre", c['m_near_centre'] < 0, True)
    chk("  ll constraint held to 1e-10", c['ll_c'] < 1e-10, True)
    xn, at0, xl = c['neg_c3']
    chk("c3 < 0: m > 0 at the centre (first_negative's at-start flag False)", at0, False)
    near("  first m < 0 at the exact linear radius", xn, xl, 1e-3)
    from scipy.optimize import brentq
    m1 = linear_m(CENTRE_L0, 3e-6, 1e-6)            # b2 = 3 c3: pure mode 1 (B2 = 0)
    near("pure mode 1: zeta_1 x 4K = brentq root of linear_m's pure-mode-1 m",
         c['mode1_first'], brentq(m1, 1.0, 1.4*c['mode1_first']), 1e-10)
    chk("  zeta_1 is the FIRST positive root of tan y = y (pi < zeta_1 < 3pi/2)",
        math.pi < zeta_first() < 1.5*math.pi, True)
    for k_, v in c['big'].items():
        chk("c3 = %s: stops ON 3 ln f + 4 = 0, m < 0 throughout" % k_,
            (v['status'], abs(v['gap']) < 1e-6, v['all_neg']), (-1, True, True))
    chk("small amplitude: Popov L is NOT uniformly sub-Planck far out (<0.5 l_P fails)",
        c['small_Lmax_neg']*K_in_planck() > 0.5, True)
    chk("c3 K^2 = 1e-4 ONLY, x <= 300 K: 2m/r not decaying (far >= 0.9 x near)",
        c['twomr'][1] >= 0.9*c['twomr'][0], True)
    chk("M_NEGATIVE_FOUND_IN_HPS_SYSTEM agrees with the centre run (c3 > 0)",
        M_NEGATIVE_FOUND_IN_HPS_SYSTEM, c['m_near_centre'] < 0)

    print("\n10. THE ROW -- RECORD PINS (printed, not counted: they compare nothing computed)")
    record("HPS_INTEGRATED_THE_PRINTED_SYSTEM (ruling B2; attribution() checks it above)",
           HPS_INTEGRATED_THE_PRINTED_SYSTEM)
    record("M_NEGATIVE_FOUND_INSIDE_DOMAIN (Popov p.1, eq. (70), Sec. VI; HPS)",
           M_NEGATIVE_FOUND_INSIDE_DOMAIN)
    record("O5_CLOSED", O5_CLOSED)
    record("AHS_REACHED (PRD 51 4337; hypotheses via Popov/TSH/AHL)", AHS_REACHED)
    record("NONLINEAR_CENTRE_ASYMPTOTICS", NONLINEAR_CENTRE_ASYMPTOTICS)
    record("THROAT_M_NEGATIVE_READING", THROAT_M_NEGATIVE_READING)
    record("WITHDRAWN claims kept", len(WITHDRAWN))

    print("\n  %d record pins printed and not counted as checks." % len(records))
    print("  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(report(full="--full" in sys.argv))
