#!/usr/bin/env python3
"""sim2_passage.py -- B4d simulation, phase 2, second instrument (M-RULINGS items 168, 173, 174, 176, 177): E-PASS,
the passage through the corridor object's own horizon into the plane's second end (u < 0), which the board reads as
the far end of our own plane within one universe (H-END-2-IS-OUR-PLANE, the board's reading, OPEN: see X1).
Computed, READ and deduced; not verified; not seated.  First headed "... not verified; not seated" (2026-10-09).
Fix round 2026-10-09: the verification's findings (lemmas/EPASS-VERIFY-RECOVERED.md; 70 findings, the list with
verdicts in the fix round's scratch) applied once per substance; then the two audits of that fix (refutation RF-1 to
RF-11, overclaim OC-1 to OC-17) applied where reproduced.  Rulings since the instrument: 179/180, 183 and 184 applied
below; 181 and 182 noted; 187 and 188, recorded after the fix, noted.  The fixed instrument is not re-verified and not
seated.  Integration 2026-10-09: X11-X25 appended after X10 (the [FREE] sections from two owners imported by path, the
[PLANE] sections deferred); X1-X10 unchanged; the integration is not verified and not seated.

M's words (verbatim in the rulings file; quoted in SIM2-PASSAGE.md; never paraphrased as M's):
173 "Go ahead with E-PASS next"; 172 (1) "Yes, it may" and (2) "Yes, that is coinciding" (the board's question in (2)
read "(so it never actually touches)"); 174 "For the math" (three times); 177 "Yes, that is the appearance"; 170 (the
clocks; it bears on X8's hold reading but is not used); 132 and 143 A (one way; what can cross); 117/120 (the NEC
"appears broken, but is not"); 155 (2) "Yes, in bits"; 139 (2) "positive, and you have to prove it." and (4); 101 (7);
129 (1) "the corridor is a bridge, so it adds nothing to either position."; 159 "test both options"; 160 "the
corridor and the opening are the same object"; 161 "my inclination is yes"; 162 (the whole chain object "only every
takes on the size that contains the README upon opening"); 163 "All together, one whole".  176's
H-PAIRING-IS-ENTANGLEMENT is the board's.

RULINGS SINCE THE INSTRUMENT (read verbatim; applied here).
  179/180  "We know the corridor doesn't not sit on either position's plane, it only bridges them. So one could surmise
      that the corridor is exclusive to the bulk." (typing kept; 180, M's correction: "*does not sit on either
      position's plane").  Carried as M's: H-CORRIDOR-IN-BULK.  X1-X10 describe the board's configuration (eq. (17) as
      our plane's own metric); under 179-180 re-read (H-CORRIDOR-IN-BULK).
  181/182  181 "this bears directly on B4d, and requires priority" (the two-plane balance first): it orders the work and
      changes nothing in X1-X10.  182, M's guess, not a ruling: "If I had to guess, I would go with C"
      (H-TWO-SIDED-BRIDGE: a two-sided bridge in the bulk, our plane on one side and position 2's on the other).  It
      bears on X1's H-END-2-IS-OUR-PLANE and is not decided here.
  183  M chose "Yes: never violated as a pair" (carried as M's: H-NEC-NEVER-VIOLATED-AS-PAIR; the board re-reads axiom
      Z3 as net per light ray, and 187 (3) has since SEATED clause (Z) so worded).  So X10 (e)'s exclusion of a negative
      energy DENSITY within one universe rests on H-POSITIVE-ON-P2 (the board's reading of 139 (2)), a positivity
      ruling, not on the NEC, and its earlier "put to M" is withdrawn (item 178 records M's thought on it; 183 records
      the re-read).  X8's refutation refutes only the route with no second sheet (SIM2-FACING S14's E-PASS, "no second
      sheet"; the design spec's section 2, Lemma 0).  E-PASS as a whole is OPEN through 177/183
      (H-PARTNER-IS-THE-COUPLING, the board's): it is never called refuted.
  184  "There are no matter free planes" (carried as M's: H-NO-MATTER-FREE-PLANES; with 129 (1), each plane carries its
      own universe's matter and the corridor adds none).  Every matter-free result here is a LIMIT, never M's
      configuration: P1 under clause (B) in full ("The plane is free of matter", the board's theorem clause, 172's
      carry), so eq. (17) on P1 and every X1-X10 result where P1's data enter -- among them X10 (a)-(e), the vacuum data
      of X10 (c) and S15's zero-net pair -- and Schwarzschild's control.  (184 speaks of planes; the vacuum Lambda_5
      bulk is clause (B)'s premise, carried as such.)
  187 (3)  M chose "Seat both": clause (G) is SEATED as the board worded it, "the corridor sits in the bulk, on neither
      plane (179/180), with eq. (17) kept only as a plane's possible reading of the corridor's mouth" (WARPTHEOREM.md:
      H-PLANE-READS-MOUTH, the board's, OPEN).  X10 (c)-(d) cite (G) as worded before 187 (eq. (17) at r0 = 2m on the
      plane): the board's configuration, re-read with the 179-180 line above.
  188  M's thought, offered for the math (H-PARTNER-AS-ENTANGLED-REFLECTION: the negative partner "along the lines of a
      posotron", typing kept).  It bears on what supplies 183's partner (OPEN below); nothing here uses it.
  So X10 (c)'s last sentence keeps its text and carries the design spec's note (X10 (c) below; item 178 cites X10, so
  X1-X10 are never renumbered or deleted).

THE SETUP.  Units m = 1, e = m/ell.  Over the throat r = 2m the static bulk grown from eq. (17) on our plane is SIM2's
throat bulk (sim2_facing S6-S7), Kaus-Reall's ODEs (2.4)-(2.7) with their Israel data (2.16)-(2.17) at Q = 0 (READ in
the ground stage, PDF pp.4-6; staticity is assumed there: "It is natural to assume that the bulk will also be static",
PDF p.4); the identity with sim2_facing's system is X1 here (C2):
    ds^2 = dy^2 + alpha(y)^2 [-(x/2) dt^2 + dx^2/x^2] + 4 beta(y)^2 dOmega^2,   x = r - 2m,
alpha = beta = 1, p = q = -e at the plane y = 0, alpha -> 0 at y_s^th (a curvature singularity).  It is an exact 5D
vacuum solution in its own right (the near-horizon limit), and the owner's bulk tends to it as x -> 0 at O(x)
(sim2_facing S8, x_valid).  The README's crossing is the event P_c where the plane (y = 0) meets the object's horizon,
at advanced coordinate v_c; the README is a test event there (no backreaction; SIM1 S3b not addressed: see OPEN).
Owners imported by path, never copied -- with one exception: the Hamiltonian constraint, which is a line and not a
function in sim2_facing, is written out once here (_constraint) and checked against the 5D vacuum equations by C2.
Imported: sim2_facing.py (throat_bulk, throat_rhs, kret_throat, x_valid, _ystar, _yK, wec_window, piece_stress,
_profile, _smooth_g2, _kind_name, CO_KINDS, DT_LAMS, DT_C, _ricci_diag, BANNED_ARGS, S5.k_bs, B4._eq17,
B4._schwarzschild), o3_write.py (the write's floor, t_min(3) at the example README: 2.0e5 clocks); and, for X13-X18
only, epass_pairing.py and epass_frames.py (their own selftest(), CHECKS and compute output, called by path).

  X1  THE CHART (computed, sympy).  x = u^2, t = v + 2 sqrt2/u turns the throat metric into
      dy^2 + alpha^2 [-(u^2/2) dv^2 + 2 sqrt2 dv du] + 4 beta^2 dOmega^2 (AdS2's ingoing Eddington-Finkelstein form),
      regular through u = 0 ON THE EXACT AdS2-SYMMETRIC THROAT (with Lambda < 0, generic perturbations of an extremal
      horizon have diverging tidal forces: Horowitz-Kolanowski-Santos, READ in the ground stage, PDF p.1, "When the
      cosmological constant is negative, we show that (in almost all cases) tidal forces diverge as one crosses the
      horizon", and PDF p.4, "Smoothness of the known exact solutions is an artifact of the symmetry rather than a
      basic physical feature"; E-AN, OPEN).  Near P_c the plane's Cauchy data are analytic across u = 0 (eq. (17) at
      r0 = 2m in the ingoing chart: g_vv = -u^2/(u^2 + 2), g_vu = sqrt(4u^2 + 2); the verification's computation,
      reproduced in scratch, not an output here), so Cauchy-Kovalevskaya gives an analytic bulk near P_c with these
      data (existence, unique among analytic solutions; standard-not-READ).  That the bulk IS this one needs uniqueness
      among smooth solutions, which for data on the timelike plane across u = 0 is not established here (OPEN; X10 (c):
      the unique continuation used there covers the static region off the horizon only).  Under that uniqueness HKS's
      caution bears toward y_s, where the analytic class is assumed (E-AN); without it, at P_c as well (deduced).  In
      this chart the 5D vacuum equations depend on y only and reproduce sim2_facing's P, Q and constraint exactly.
      u < 0 is the plane's second end in eq. (17)'s analytic extension (plane.py P1's position-2 side; in the throat
      metric the S2 radius is 2 beta(y), and "r = 2m + u^2" belongs to the plane's eq. (17)).  That it is the far end
      of OUR OWN plane within one universe is a global identification no instrument here computes:
      H-END-2-IS-OUR-PLANE, the board's reading under its theorem clause (B) ("The plane's two ends are one end of the
      bulk"), OPEN; 182's guess (M's) bears on it and is not decided here.  What bears on it (READ in the ground
      stage): Simpson-Visser, for the closest 4D analogue (the ground stage's deduction), label the maximal extension's
      far side "Copy of our universe" (PDF p.6, Fig. 2), and their alternative construction -- "we can identify the past
      null bounce at r = 0 with the future null bounce at r = 0 yielding the 'looped' Carter-Penrose diagram of figure
      3" (PDF p.5) -- is what the ground stage reads as the one-universe version; it may close causal curves, against
      128 (deduced and OPEN, the ground stage's; SV do not discuss it).  In 4D, two mouths in one ambient space give a
      non-trivial pi_1, which topological censorship forbids classically (deduced; standard); Maldacena-Milekhin say so
      and resolve it in 5D (READ, PDF p.12): "The topological censorship theorems say that in classical general
      relativity we cannot have a non-trivial first homotopy group, pi_1. This is allowed when quantum effects are
      included. However, what looks like a quantum Casimir energy in four dimensions is actually a classical effect in
      five dimensions (the negative classical energy of AdS3). So in five dimensions the topological censorship should
      work. It indeed works because the classical geometry in five dimensions has a trivial pi_1. ... This is possible
      by moving the light ray into the fifth dimension."  Their construction, which fills the loop, rests on that AdS3
      region (a 5D U(1) field with magnetic flux, charged mouths: X10 (a)), which clause (B)'s vacuum bulk excludes
      (X10 (c)).  Whether this vacuum bulk fills the loop is OPEN (the ground stage, deduced: in 5D a passage between
      two regions of one plane is compatible with topological censorship when the bulk makes it homotopic to a path in
      the plane).  X7-X8 do not use the identification (their J^-(P_c) lies in u >= 0); X9's one-universe placement
      and E-PASS's definition do.
  X2  THE HORIZON (computed).  xi = d_v has norm -alpha^2 u^2/2; g^uu = u^2/(4 alpha^2), g^yu = 0; so u = 0 is a null
      hypersurface generated by d_v at every depth, and kappa^2 = -(1/2) (nabla xi)^2 = u^2 (4 alpha'^2 + 1)/8 vanishes
      on it at every y < y_s^th: a Killing horizon, VERTICAL and DEGENERATE at every depth, exact on the AdS2-symmetric
      throat only.  kappa = 0 identically, so Racz-Wald's singularity theorem, which needs kappa != 0 on a generator,
      does not apply, and the horizon is in their class of horizons with kappa = 0, on whose regularity their abstract
      decides nothing (CQG 9 (1992) 2643, the abstract as two verifiers quote it from the SciSpace record and the IOP
      page; not re-read here; the full text NOT READ; cited before through Karasik et al., READ in the ground stage,
      p.3).  Control: the non-degenerate g_vv = -alpha^2 (u^2 - h^2)/2 gives kappa != 0 on its horizon u = h.
  X3  ONE WAY (deduced from the computed null directions).  From ef_metric's (v, u) block: the radial null directions are
      dv = 0 (ingoing; -d_u is future-directed since g(d_v, d_u) = sqrt2 alpha^2 > 0) and du/dv = u^2/(4 sqrt2) >= 0; on
      u < 0 the second reaches u = 0 only as v -> infinity.  So the hypersurface u = 0 is crossed only from u > 0 into
      u < 0 (132).  At r0 = 2m this computation is the evidence; plane.py P1 covers the neighbouring non-degenerate
      members r0 < 2m, whose two horizons have x timelike between them.
  X4  THE SINGULAR END IS KASNER (deduced, then computed).  Near y_s put alpha ~ delta^a, beta ~ delta^b (delta = y_s - y;
      p = -a/delta, q = -b/delta).  The two evolution equations' leading balance gives a + b = 1/2 (each gives it once);
      the Hamiltonian constraint gives (a + b)^2 + 2ab = 0, so ab = -1/8 (1/(4 alpha^2) ~ delta^(-2a) and 1/(4 beta^2)
      are subleading since a < 1): a, b = (1 +- sqrt3)/4 = 0.6830, -0.1830, derived here from the coded system (sympy).
      The swapped pair is also a leading balance; alpha -> 0 (a > 0) is the computed branch.  The exponents
      (a, a, b, b) sum to 1 and their squares to 1.  Computed by fitting at the nine ell.  Control: a mutated ODE
      (2pq -> 3pq) gives other exponents (a = 1.002).
  X5  THE SINGULAR SURFACE IS TIMELIKE AND AT FINITE CONFORMAL DEPTH (deduced, computed).  The radial metric is
      alpha^2 (d eta^2 + g_AdS2(radius 2)), eta = int dy/alpha; since a < 1, eta_s = eta(y_s) is finite, so the
      singular surface is the boundary {eta_s} x AdS2 of a product with a line: timelike, and reachable by causal
      curves.  eta is integrated as an ODE variable to alpha = 1e-9 with the Kasner tail added ONCE (the first version
      counted it twice: every eta_s was 1.4-2.7e-4 too high); an independent integration with eta as the independent
      variable to alpha = 1e-12 agrees to 1e-11 (C6).  Control (computed): the same eta_of run on the mutated ODE of
      X4's control (2pq -> 3pq, alpha ~ delta^1.002, i.e. exponent 1): eta's increment per three decades of alpha
      stays ~9.8 (it diverges, logarithmically to the fit's precision), while the true system's shrinks ~25-fold.
  X6  THE CAUSAL PAST OF THE CROSSING (deduced; checked by integrating geodesics).  In the conformal frame
      d eta^2 + 4(-dt^2 + d zeta^2)/zeta^2 (zeta = 2 sqrt2/u, v = t - zeta), a point q = (eta, zeta_q, v_q) at P_c's
      angle lies in J^-(P_c) iff  v_c - v_q >= zeta_q * 2 sin^2(eta/4)  (eta < 2 pi); at another angle the inequality
      is necessary only (a causal curve projects to a causal curve of the radial factor; angular motion only adds).
      Points of end 2 and of the horizon at depth > 0 are never in it.  Checked: along past-directed null geodesics
      from P_c the equality holds to the integrator's tolerance -- one ray up to AdS2's dilatation (v -> lambda v,
      w -> w/lambda), so the eight rays check the integrator, not eight cases; past-directed timelike geodesics land
      strictly inside (the interior); the control sin^2(eta/2) fails.
  X7  THE CONE BUDGET (deduced, computed).  A causal curve from conformal depth eta to P_c that stays where the throat
      geometry holds (x <= x_lim, zeta >= zeta_lim = 2 sqrt2/sqrt(x_lim)) needs the static bulk to have stood an
      advanced-coordinate hold v_c - v_open of at least zeta_lim 2 sin^2(eta/4) -- attained for eta <= pi; for eta > pi
      the confined minimum is zeta_lim [1 + (eta - pi)/2] (the ground stage's g, deduced there; reproduced numerically,
      to 1.3%, by an independent dynamic programme, C9) -- and at most zeta_lim eta/2 (an explicit curve at fixed zeta,
      then the plane's ingoing null leg, which costs no advanced coordinate).  lower <= upper is STRUCTURAL
      (1 - cos(eta/2) <= eta/2).  The budgets are computed on the zeroth-order throat; the upper curve is null there at
      x = x_lim, where the O(x) terms reach 10%, a rescaling the margins below absorb.
      Computed: every layer up to K = 1e10 K_bs lies in J^-(P_c) within the O(x) range (x_lim the least x_valid over
      the layer's depths, O(x) <= 0.1): at most 389.3 clocks over the nine ell (the claimed rows, C8).  Deeper, the
      per-decade scan (ell = inf, 8m, m) still places layers in J^-(P_c) within O(x): by the upper budget (the explicit
      curve) to K = 1e31 K_bs at ell = inf and 8m and to 1e32 K_bs at ell = m, and by the confined minimum to 1e32 K_bs
      at all three.  The budget grows (upper ~ K^0.126 fitted between 1e15 and 1e30 K_bs, near the verification's
      K^(1/8)) and is unbounded at the singular surface: the layer's LOWER budget passes the write's floor between
      K = 1e32 and 1e33 K_bs (ell = inf, 8m; at ell = m the full system ends at alpha = 1e-6 before it).  Part of the
      shrinking O(x) range is a shift of the singular depth with x (y_s(x) ~ y_s + s1 x, the verification's
      computation, not computed here), so this says the instrument does not reach the singular surface within O(x);
      it does not say the surface is outside J^-(P_c).
      The singular surface itself lies in J^-(P_c) only in the exact near-horizon solution held to y_s at a fixed
      x_lim: below the floor for x_lim >= 1e-8 (the floor is 2.47 times the upper budget at 1e-8, ell = inf), above it
      past the computed crossover (upper below x_lim = 1.64e-9, lower below 7.72e-10, ell = inf).  Those rows
      illustrate the x_lim^(-1/2) law; they are not O(x)-supported evidence about the singular surface.
      The comparison is v_c - v_open >= budget.  It holds with v_c - v_open >= 2.0e5 when the crossing ends the write
      (H-WRITE-IS-ARRIVAL, the board's, o3_write W3, on which the gas bound rests; 162's record set it aside, 163's keeps
      the gas bound and 115 (c), the README carried in) and the fixed-size corridor stands, static, from its opening
      through the write (162: the whole chain object takes its size "upon opening"; 163's chosen option, in the board's
      wording that M chose: "B4d must keep the fixed-size corridor regular for that long"; static:
      H-QUASI-STATIC-CORRIDOR, the board's).  That placement is o3_write W4's reading (ii) as 160's record re-reads it
      (M's 160: the opening is the corridor), with the static-hold mechanics W4 gave reading (i)
      (H-WRITE-IN-STATIC-HOLD, the board's; 159 keeps both readings live), whose hold distinct from the opening 160's
      record dissolves (the board's record, to be worked).  It is not W4's own (ii), where under H-PULL-IS-COST "the
      corridor of mass m does not exist until the README has arrived" (an ingoing Vaidya opening, non-static; 160's
      record: no longer the opening's model).  There no static corridor stands before v_c, and X7-X8 neither refute
      nor save the route (OPEN; 159).
  X8  WITHOUT A SECOND SHEET (deduced).  So stage 6's cone premise refutes the route with no second sheet -- SIM2-FACING
      S14's E-PASS ("no second sheet"), the design spec's Lemma 0 -- on its own, on the conjunction: the exact throat
      geometry down to y_s held at x_lim >= 1e-8 (within O(x) the claimed rows place layers to 1e10 K_bs in J^-(P_c)
      and the scan to 1e31-1e32 K_bs, X7; the singular surface itself only in the exact near-horizon solution at
      x_lim >= 1e-8 -- below x_lim = 1.64e-9 its upper budget passes the floor, ell = inf); 174 (1)'s strict rule as
      the board decided it (a curvature singularity in the corridor's causal past counts against it); static bulk
      through the hold (H-QUASI-STATIC-CORRIDOR, the board's); eq. (17) on P1 at our tension, clause (B) in full on P1
      (a matter-free limit under 184); vacuum Lambda_5 and the analytic class; the throat ODE and its O(x) correction as
      evidence; the hold measured in advanced coordinate (H-HOLD-IN-ADVANCED-TIME, the board's: the write floor's own
      frame, "T the write's length in clocks (advanced time, H-HOLD-FRAME)", o3_write W3; it coincides with O3-WRITE's
      gloss of H-HOLD-FRAME (the board's), "T is measured in advanced time (H-HOLD-FRAME)", and departs from
      B4D-STAGE5's, "the far-time frame (H-HOLD-FRAME)"; which gloss stands is not decided here, OPEN; on the plane's
      static clock the crossing lies at t = +infinity, outside every finite hold, and on such a hold X1-X10 neither
      refute nor save the route -- the spec's far-time X11 is to take that half up, not in this file);
      H-WRITE-IS-ARRIVAL with the corridor standing static from its opening (X7; not o3_write W4's own (ii)); a write
      of >= 2.0e5 clocks (o3_write W3, kept by 163); the README as a test event (no backreaction; SIM1 S3b not
      addressed).  H-END-2-IS-OUR-PLANE (X1, OPEN) is not a conjunct.  E-PASS as a whole is NOT refuted: under 183
      (H-NEC-NEVER-VIOLATED-AS-PAIR, M's) its stationary crossing is OPEN through 177 (H-PARTNER-IS-THE-COUPLING, the
      board's).  Near the throat position 2's piece keeps the singular layer out of the crossing's past only for the
      depth and profile pairs X9 passes (the level surface at d >= y*; the smooth family at every sampled depth; every
      sampled profile at 0.1 y_s, d_+ and depth 0; all at amplitude c = 0.05); it does not for the 11 sampled
      power-law cases at y* or the band's midpoint with ell <= m, and on the power-law coincidence P2's own stress
      diverges at P_c along the regular null frame (C11b).
  X9  WITH POSITION 2'S PIECE AT DEPTH d < y_s (computed, deduced).  With P2 mirrored (H-Z2-PIECES, the board's) and
      carrying the README's stress (H-README-ON-P2, M's 172 (1) "Yes, it may"), the slab is bounded by P1 (y = 0) and
      P2: y = d + f(x), a level surface (f = 0) only where W1(d) >= 0 (d >= y*), otherwise S7's class (f > 0 at x > 0:
      the power law c x^lam, 0 < lam < 1/2, or the smooth family g1 sqrt(x) + g2 x).  Which profile and amplitude is
      P2's is not answered (172: "Not answered: which part of position 2's stress is its law"); the rows sample four
      profiles at one amplitude, c = g1 = 0.05 (sim2_facing.DT_C; lam 0.1, 0.25, 0.4, and the smooth family).  No slab
      is cut at d: near the throat J^-(P_c) holds slab points down to P2's own depth d + f(x) over its part of P2 (x
      from u_min^2 to x_valid(d)), so "no singular layer" needs d + f(x) < y_s^th there.  Computed (C11a): it holds for
      every sampled profile at 0.1 y_s, at d_+ (ell = 32m) and in the coinciding limit at every ell, and for the
      smooth family at every row (every failure is a power law); for the level surface at every d >= y* row it holds
      by construction (STRUCTURAL: every row is shallower than y_s^th); it
      FAILS for the sampled power laws at y* or the band's midpoint at ell <= m (ell = m: lam 0.1 at the band's
      midpoint; m/2: lam 0.1, 0.25 at both; m/4: all three lam at both -- each reaches y_s^th inside x_valid(d) and
      inside J^-(P_c)).
      The margins depend on the amplitude: a power law keeps its margin iff c < c* = (y_s^th - d)/x_valid(d)^lam
      (deduced: f rises with x; computed per row).  At depth 0, 0.1 y_s and d_+, c* >= 0.48 (ell = m/4, 0.1 y_s,
      lam 0.1), about ten times the sampled 0.05; at y* and the band's midpoint c* runs from 9.0e-4 (ell = m/4) to 3.9
      (ell = inf).  Unmirrored (E-ASYM, phase 3) P2's outer side is its own bulk, so the cut does not by itself remove
      the singular layer (deduced, the board's; not computed here).  Away from the throat "no singular layer" needs P2
      above y_s(r) on all of J^-(P_c), which reaches every r with v <= v_c: OPEN (E-G, E-FAR; for the band case P2 is
      deeper near the horizon than at its nearest point).  P2's own points with u > 0 enter J^-(P_c) down to
      u_min = 4 sqrt2 sin^2(eta(d)/4)/Delta_v (to leading order in f); its horizon line at d > 0 is not in J^-(P_c).
      The coinciding limit d -> 0 (M's 172 (2) "Yes, that is coinciding"): K -> 2(80 e^4 + 3)/(160 e^4 + 3) K_bs, and
      the slab pinches along the plane's horizon line, which contains P_c.  On the power-law profiles P2's stress in the
      crosser's frame diverges at P_c (computed, C11b: along the null direction n = -d_u, regular across u = 0, the
      sheet reads 4 alpha^2 (rho + p_r)/x, which grows as x^(lam - 1)), while its static-frame rho, rho + p_r and
      rho + p_th stay finite (rho + p_r -> 0 as x^lam; computed): a divergence along the regular null frame only, a
      parallelly-propagated divergence of P2's sheet with finite static-frame components (compare HKS's horizons, whose
      tidal forces diverge while "all scalar curvature invariants remain finite", ground stage READ, PDF p.1; by analogy
      only).  174 (1)'s strict rule was decided for curvature singularities; counting this divergence under it is the
      board's reading.  Only the smooth family stays finite (S7; computed).  Restricted to the smooth family, the
      README's crossing event is the coincidence event.  It is reached at finite advanced coordinate, at finite proper
      time by a radial timelike observer on the plane (computed: u'^2 = E^2/2 - u^2/4, so u' = -E/sqrt2 at u = 0) and
      at finite affine parameter by the null README (H-README-AS-NULL-DUST, the board's: the E-PASS design's name for
      opening.py's null-dust convention, whose own reading is R-VAIDYA-HOLDS; dv = 0), never on any static slice (X3,
      X6); compare Emparan-Horowitz-Myers on RS2's AdS5 Poincare horizons, by analogy only (READ in the ground stage,
      PDF p.2): "... can be reached by observers in finite proper time (just like the horizons of extreme charged black
      holes). The linearized modes studied in [1] turn out to be singular on these horizons [5]."
      Separately, the board's reading, not derived: 172 (2)'s question said "(so it never actually touches)", and the
      carry H-COINCIDE-DOWN-THE-THROAT's "never a reached point" is the board's wording, not M's; the board reads it as
      "on no static slice", while the crosser does reach the event (H-REACHED-ONLY-BY-THE-CROSSER, the board's) -- an
      inversion of the question's wording, not decided under 149, put to M with the E-PASS report.  On positive energy
      at finite ell exact coincidence is not available within one universe (174 (3)): on H-SPLIT-AT-OUR-TENSION (the
      board's decision under 174) it costs P2 rho_m -> -2 sigma_RS at every finite ell (sim2_facing S15).  Held at an
      approach depth (facing on H-APPROACH-AT-DEPTH, the board's, adopted under 174) in P2's positive-energy window
      [d_+, top] (ell = 32m: [0.8395m, 1.5352m]; such a window exists only for ell > 27.07m), P2's energy is positive
      (S15, on H-SPLIT-AT-OUR-TENSION), and near the throat the slab holds no curvature singularity of the bulk (it is
      the throat bulk above its singular depth) at any d > 0 whose profile keeps its margin (C11a).  At d_+ itself only
      power laws with lam < lam_max = 0.342 (32m) hold (S15): non-smooth at u = 0, where their stress grows as above,
      but P2's horizon line at d_+ > 0 is outside J^-(P_c) and its points enter only down to u_min > 0.  At ell = inf,
      d_+ = 0 is exact coincidence, the flat limit, where the coincidence caveat above applies.  The smooth family
      continued through u = 0 meets P1 just past the horizon on end 2's side (ground stage, scratch: u_x -> -d/g1).
      The README is a test event here too (SIM1 S3b, OPEN).
  X10 E-Q, ITEM 177 (computed, deduced).  (a) The 5D bulk is vacuum with Lambda_5 (clause (B)'s premise), so
      R_kk = -(4/ell^2) g_kk = 0 for every 5D null k (deduced).  On a vacuum piece at the RS tension (P1) the plane's
      Einstein tensor is minus the projected bulk Weyl term, so any negative null energy read on P1 is that
      term: Shiromizu-Maeda-Sasaki (standard-not-READ), as Bronnikov-Kim relay it (READ, gr-qc/0212112v1 PDF p.1): "In
      vacuum, when matter on the brane is absent and the 4-dimensional cosmological constant is zero ..., these
      equations reduce to G_mu nu = -E_mu nu, (1) where ... E_mu nu is the projection of the 5-dimensional Weyl tensor
      onto the brane. ... Due to its geometric origin, E_mu nu does not necessarily satisfy the energy conditions
      applicable to ordinary matter. Thus, examples are known [29] when negative energies on the brane are induced by
      gravitational waves or black strings in the bulk." (READ this round, PDF p.1).  On P2, which carries the README's
      stress (172 (1)), the quadratic term pi_kk enters too (for a perfect fluid (1/6) rho (rho + p)(u.k)^2,
      standard-not-READ; negative when rho < 0).  Maldacena-Milekhin is a precedent only (READ, PDF p.12): "what looks
      like a quantum Casimir energy in four dimensions is actually a classical effect in five dimensions (the negative
      classical energy of AdS3)" -- under hypotheses this bulk does not meet (READ this round): a dark sector, "Our
      construction needs a dark sector consisting of a four dimensional conformal field theory with a U(1) symmetry
      that is gauged by a four dimensional (dark) gauge field" (PDF p.2), holographic, "it has an AdS5 dual described by
      five dimensional gravity and a five dimensional U(1) gauge field" (PDF p.3); their 5D action carries that field,
      "- 1/(4 g_5^2) int d^5x sqrt(g) F_mu nu F^mu nu" (eq. (3.17), PDF p.8), with "a magnetic flux at the boundary of
      AdS5" (PDF p.9), mouths of opposite magnetic charge ("two black holes with opposite charges", PDF p.4), and no
      horizon ("Since g_tt never vanishes", PDF p.12).
      (b) Computed: eq. (17)'s own plane (a matter-free limit under 184) reads negative integrated null energy along the
      ingoing radial null ray from far out to the throat, exactly (sqrt3 ln(2 + sqrt3) - 6)/(36 pi) = -0.0328828437...
      (sympy's exact integral equals this closed form to 60 digits; reduced by hand with r = 2 + s^2, s = tan(th)/sqrt2,
      w = sin th to -(1/(2 pi)) int_0^1 (1 - w^2)/(4 - 3 w^2) dw; Wolfram 15 gives (-6 + Sqrt[3] ArcCosh[2])/(36 Pi));
      Schwarzschild's is exactly zero (the control).  The end-2 half, by the (v, u) -> (-v, -u) isometry, gives the same
      value, so the full ray carries twice this (deduced; the second half uses end 2).  This is eq. (17)'s induced Weyl
      fluid, not P1's surface stress.
      (c) The static throat bulk is fixed by the plane's data WITHIN THE STATIC AdS2 x S2-SYMMETRIC REDUCTION (an
      initial-value problem in y for the cohomogeneity-one ODEs: Picard-Lindelof, deduced): a static symmetric coupling
      that leaves the plane's data unchanged changes nothing there, and a change of the plane's data is a sheet or
      matter (computed: p(0) moved along the constraint surface, q(0) solved from the yy constraint, moves y_s both
      ways, the constraint held to ~1e-14 along the run).  For static data that break the AdS2 x S2 symmetry,
      uniqueness in the static region off the horizon is unique continuation for the Riemannian section (a static
      vacuum metric with Lambda_5 Wick-rotates to a Riemannian Einstein metric with the same constant:
      standard-not-READ; the plane its boundary, with eq. (17)'s metric and the Israel data as (gamma, A): deduced).
      Anderson-Herzlich, arXiv:0710.1305v2 (READ this round): Thm 1.1, for "a C^{3,alpha} metric on a compact manifold
      with boundary" with "Ric_g = lambda g" (PDF p.1; their class is "Riemannian metrics"), "Then (M, g) is uniquely
      determined up to local isometry and inclusion, by the Cauchy data (gamma, A) on an arbitrary open set U of dM",
      and "the proofs are local, and these results hold for metrics defined on an open manifold with boundary" (PDF p.2)
      [math transcribed].  Across u = 0 the static quotient degenerates (the lapse vanishes on the Killing horizon,
      which lies at infinite distance on a static slice: X2), so uniqueness there is NOT covered: OPEN (with HKS, X1).
      Existence off the reduction needs the analytic class (Cauchy-Kovalevskaya; E-AN, OPEN); non-static changes
      (E-NS) and motion inside the planes (E-ROT: "K not diagonal (your 141's internal motion)", SIM2-FACING S14) are
      not covered: OPEN.  Maldacena-Milekhin's own classical-5D route needs a 5D U(1) gauge field and charged mouths
      (X10 (a)): clause (B)'s vacuum bulk excludes the field; the charged mouths were excluded too by (G) as worded
      before 187 (eq. (17), a vacuum-plane metric with no Maxwell field), which 187's (G) keeps only as a plane's
      possible reading of the mouth.  [Kept as written:] So E-Q, realised classically in five dimensions, is a change of
      the bulk, and the change E-PASS needs is position 2's sheet: the coupled ends are the slab, whose coincident pair
      carries zero net surface stress (sim2_facing S15), the +sigma/-sigma pairing of 176.  [Labels:] "the coupled ends
      are the slab" is the board's reading under H-PAIRING-IS-ENTANGLEMENT (176, the board's, put to M); S15's zero net
      is a computed fact with no reading attached, a total of zero, never "positive"; and by (e) the slab carries no
      negative null energy, so the identification does not by itself realise 177's appearance.  [Note:] superseded in
      part by X13: position 2's piece regularises the crossing's past; it does not pay the crossing (Lemma S).
      [Pointer:] on the depths and profiles X9 passes (X8).
      (d) Maldacena-Qi's horizonless link (global AdS2, READ) would remove the degenerate horizon: a two-way passage,
      against clause (O) and 132.  Any horizonless plane metric departs from eq. (17) at r0 = 2m (the board's
      configuration: (G) before 187; under 187's (G) a plane's possible reading of the mouth, OPEN), whose
      g_tt = -(1 - 2m/r) vanishes at the throat (computed); within eq. (17)'s family that is Bronnikov-Kim's wormhole
      branch (READ, PDF p.4: "This is evidently a symmetric wormhole geometry for any r0 > 2m >= 0, or for any r0 > 0
      in case m < 0." [math transcribed]), whose near-throat geometry at r0 = 2m + delta is global AdS2 (deduced:
      -(x/2) dt^2 + dx^2/(x(x - delta)), x = delta/cos^2 chi).  So the coupling the corridor admits keeps the horizon
      (deduced; Gao-Jafferis-Wall's protocol NOT READ).
      (e) At coincidence P2's matter obeys the NEC only marginally (rho_m + p_m -> 0) and, on H-SPLIT-AT-OUR-TENSION
      (the board's), its energy density is negative: 177 speaks of negative NULL energy, so as worded it does not reach
      this negative density.  Under 183 (H-NEC-NEVER-VIOLATED-AS-PAIR, M's; axiom Z3 re-read as net per light ray) the
      exclusion of a negative energy DENSITY within one universe rests on H-POSITIVE-ON-P2 (the board's reading of
      139 (2)), a positivity ruling, not on the NEC.  This point's earlier "put to M" is withdrawn (item 178 records M's
      thought on it, item 183 the re-read); the board's reading of 178 (lemmas/ITEM178-NULL-PAIRS.md, re-read under 183)
      is still to go to M with the E-PASS report, as 178's record says.  At exact coincidence the 5D null energy along
      a ray crossing the coincident sheets sums to zero (per-sheet -sigma_RS k_y^2 for position 2's piece and
      +sigma_RS k_y^2 for ours, bookkeeping whose sign follows the owner's orientation: ITEM178-NULL-PAIRS.md section 5,
      deduced there); the board reads that zero as meeting H-NEC-NEVER-VIOLATED-AS-PAIR exactly.  A zero total is not
      "positive".
  OPEN (every item found, plainly).  Crossing regularity off the exact AdS2-symmetric throat (HKS; E-AN; X1, X2, X9).
      Uniqueness of the bulk among smooth solutions near P_c and across u = 0 (X1, X10 (c)).  The global P2: P2 above
      y_s(r) on all of J^-(P_c) (E-G, E-FAR; X9).  P2's law: which profile and amplitude (172's "Not answered"; X9's
      margins are sampled at c = 0.05).  Whether a parallelly-propagated divergence of P2's sheet counts under
      174 (1) (X9; the board's reading).  Topology and one universe: H-END-2-IS-OUR-PLANE, with 182's guess bearing on
      it (X1).  The README as a test event: SIM1 S3b (a horizon that keeps its size absorbs nothing in one spacetime
      when the flux obeys the NEC) bars the crossing unless a negative R_kk supplies it; under 183 that negative member
      is the appearance (H-NEC-NEVER-VIOLATED-AS-PAIR, M's) and its supply is OPEN through 177
      (H-PARTNER-IS-THE-COUPLING, the board's; the spec's Lemma S; 188's thought bears on it), so E-PASS's stationary
      crossing is OPEN.  o3_write W4's own reading (ii), the Vaidya opening, which 159 keeps live: X7-X8 show nothing
      there.  The far-time (static-clock) half of the no-second-sheet refutation (X8; the spec's X11), and which gloss
      of H-HOLD-FRAME stands (X8).  Symmetry-breaking static bulk changes, non-static bulk changes and motion inside the
      planes (E-AN, E-NS, E-ROT (141); X10 (c)).  X10 (c)-(d) under 187's clause (G) (H-PLANE-READS-MOUTH, OPEN).
      H-REACHED-ONLY-BY-THE-CROSSER, put to M (X9).  H-PAIRING-IS-ENTANGLEMENT, put to M (176; X10 (c)).  The board's
      reading of item 178, to go to M with the E-PASS report (X10 (e)).  The singular surface within O(x) (X7).
  X11-X25 THE INTEGRATION (2026-10-09; the [FREE] sections computed by two owners, imported by path, never copied; the
      [PLANE] sections DEFERRED; not verified as integrated; not seated).  The design spec (lemmas/EPASS-DESIGN-SPEC.md,
      a design document, not verified) tags each section [FREE] (it holds whatever carries the corridor: a plane, a
      sheet, or the bulk alone) or [PLANE] (it uses eq. (17) as our plane's own metric, the board's pre-179
      configuration).  Under 179-181 its recommendation stands: the [FREE] sections are built, the [PLANE] sections wait
      for the 179 re-read.  The two owners were each built, then refuted and overclaim-checked once by separate AI
      sessions inside this project (not an outside review), findings applied, the fixes not re-verified:
      lemmas/epass_pairing.py (X13, X14; md5 152621fa...; its own selftest 11/11, its own --mutants 33/33) and
      lemmas/epass_frames.py (X17's stationary half and X18; md5 97bbfff9...; 16/16 and 30/30).  epass_frames was
      verified against the pairing owner BEFORE that owner's blocker fix (see X17).  Checks C15-C19 and C26-C31 below
      call the owners' own selftests and fail if an owner fails or is missing.  Every value quoted in X13-X18 is copied
      from the owner's output, given with the owner's label and its [FREE]/[PLANE] tag; C35a requires the 107 values
      listed in DOC_QUOTES to equal the owner's live output (the md5 prefixes included).  The few other values quoted
      here (u_H = 1/3, eps = 1/10 and v = 3/10, the 1000-row counts, r = 3m, the PDF pages, the Wolfram agreement) are
      not in DOC_QUOTES and are not machine-checked.  Nothing in X13-X18 is re-derived here.
  X11 DEFERRED [PLANE] -- Lemma 0's far-time half: the README's own pre-crossing events on end 1 (r = 2.02-2.2m) on the
      plane's static clock, from stage 5's owner columns.  Until it is built, X8's refutation of the route with no
      second sheet rests on its advanced-time half (X7) and the static-clock half stays OPEN (X8).
  X12 DEFERRED [PLANE] -- footprint, ceiling, Lemma X (excision) and the far gate, from the owner bank's columns on
      our plane.
  X13 LEMMA S, THE PAIRING LAW AT A HORIZON OF FIXED SIZE [FREE] (owner epass_pairing; computed as identities;
      deduced).  (b) BULK FORM, primary under 179/180 (computed): on D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2 (A, B, C,
      D arbitrary functions of (y, u); g_vv = -A u^2, degenerate, or -A u, non-degenerate; no g_uu, no cross terms, no
      rotation), with no field equation, R(xi,xi)|_{u=0} = 0 on the stationary members and on a non-stationary member
      that keeps u = 0 null.  THE PREMISE IS NOT STATIONARITY -- the owner's verification found this as a blocker, and
      it is applied there: the Raychaudhuri route agrees with the Riemann route on every variant,
      R(xi,xi)|_H = -dtheta/dv + kappa theta - theta^2/3 - sigma^2 (computed), so on a horizon that does not expand
      (theta = 0) R(xi,xi) = -sigma^2 <= 0; shear at fixed volume gives -0.014138938637006316 (eps = 1/10, v = 3/10, on
      the owner's stand-in functions; Wolfram 15.0.1 agreed, computed by the owner's fix session, not run here).  With
      Einstein + Lambda_5, kappa_5^2 T5(xi,xi) = R(xi,xi) on H (deduced).  So across a horizon that keeps its size --
      162's H-FIXED-SIZE (M's) read as theta = 0 through H-FIXED-SIZE-AS-THETA-ZERO (the board's, put to M, unanswered)
      -- kappa_5^2 T5(xi,xi) = -sigma^2 pointwise on H, and the net 5D null energy along each generator is
      -int sigma^2 dv / kappa_5^2: zero or negative, never above zero.  The partner is at least as large as the README,
      exactly as large only if the horizon is unsheared (deduced).  With 183 (H-NEC-NEVER-VIOLATED-AS-PAIR, carried as
      M's: the option he chose, "Yes: never violated as a pair", which the board glossed as zero net along each light
      ray; seated clause (Z), 187 (3), read as a net not below zero along each light ray, gives the same) the horizon
      must be unsheared and the pair exact (deduced).
      (a) SHEET FORM, on whichever sheet carries the README (172 (1)) (computed): K(xi,xi)|_H = 0 for sheets y = F(u),
      F arbitrary, in the throat metric and on (b)'s family, degenerate (u_H = 0) and non-degenerate (u_H = 1/3), also
      on non-stationary members that keep u_H null and on a horizon whose section grows: the sheet form is blind to
      stationarity and to growth.  Its premise is u = u_H null at every depth with the sheet tangent to xi: a sheet
      tilted off xi gives K(xi,xi) = -kappa n.xi, witness 0.01166 where kappa != 0 and 0 where kappa = 0.
      S(xi,xi) = -nu K(xi,xi) on H (deduced, g(xi,xi)|_H = 0): T^c(xi,xi) = -T^R(xi,xi) on the README's own sheet,
      generator by generator, at any tension or law, with held matter (184) -- matter held on the sheet, so that
      T^m(xi,xi)|_H = 0, as a regular held stress has (below); matter flowing across the horizon enters the ledger as
      T^c(xi,xi) = -T^R(xi,xi) - T^m(xi,xi) (X17's matter premise).  A regular held AdS2-invariant stress has
      tau(xi,xi) = pi(xi,xi) = 0 on H, so held stress cannot be the partner: it must be a genuine negative null flux
      (deduced).
      (c) THE WEYL TERM GIVES NOTHING [FREE] (computed; READ SMS eq. (A10), PDF p.6, as the owner transcribes it):
      E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0 on (b)'s family's horizon, stationary or null-preserving
      non-stationary, both unsheared (a growing section gives E != 0; a sheared one, where R(xi,xi) = -sigma^2 enters
      E = E~ - R(xi,xi)/3, is not computed).  [PLANE]: on eq. (17)'s data R4(xi,xi) = 0 at r = 2m (computed), and
      E(xi,xi) = 0 there under SMS's eq. (17) with Z2 (H-Z2-PIECES, the board's) (deduced).
      (d) THE PAIR [PLANE] (computed; deduced): README member T^R(xi,xi) = 2 per mu in eq. (17)'s ingoing chart
      (l.xi = -sqrt2), partner -2, net 0 BY CONSTRUCTION (the partner is defined as -T^R: not a finding).  A null-dust
      partner tilted by b along the sphere gives pi(xi,xi) = -b^2 mu^2/2 by two routes (SMS eq. (20); the null-dust
      algebra), independent of a static held stress.  With SMS (17) under Z2 (H-Z2-PIECES, the board's), a static held
      stress, R4(xi,xi) = 0, E(xi,xi) = 0 from the bulk side (the bulk near the plane taken in (b)'s family,
      non-expanding and shear-free) and tau(xi,xi) = 0, pi(xi,xi) = 0 forces b = 0.  So among null-dust partners, with
      no held momentum flux along the sphere (one would enter pi(xi,xi) and could cancel it at b != 0: the owner's
      C19c mutation), the only admitted null partner is the README's exact reverse, and the pair's total stress tensor
      is then ZERO -- the README's stress is cancelled outright, a plain negative (135) (deduced).  A zero total is not
      "positive".
  X14 LEMMA K, A NET-FLUX CROSSING KINKS THE BULK HORIZON [FREE for sheets] (owner epass_pairing; computed; deduced):
      in Gaussian normal coordinates the null geodesic tangent to the sheet along the horizon generator obeys
      y'' = K_vv by two routes (the connection; (1/2) Lie_n g_vv with no Christoffel symbol), with K_vv = -S_vv/nu.
      Integrated: S_vv = 0 stays on the sheet to 1e-12; S_vv = +1 leaves the kept side (y_end = -0.5572, leading order
      -1/2); S_vv = -1 leaves the sheet into the bulk (y_end = 0.4832).  So a bulk horizon C^2 up to the sheet, with the
      brane horizon as its trace, carries no net flux there, and a net-flux crossing is a five-dimensional event
      (E-NS): it creases the bulk horizon at the sheet or separates it from the brane horizon (deduced).  WITHDRAWN:
      the smooth-horizon identity's B_start budget and design 4's "q >= 0 absorbs classically"; that identity's algebra
      is kept only as the owner's C15 (contracted Gauss, SMS eq. (3)) and C16 (transport, Raychaudhuri).
  X15 DEFERRED [PLANE] -- Lemmas L and Q and the absorbing band: Lemma L is the brane ledger of a changing crossing
      (SMS) with eq. (17)'s data on our plane, Lemma Q is stated at our plane's law, and the band (d_beta, d_+, q(d_+))
      is S15's slab.  X17's changing half (Lemma L's coefficient times P1's; the spec, a design document not verified,
      gives 5.912 at 32m tending to 5: not computed here) waits with it.
  X16 DEFERRED [PLANE] -- the crossable class at the horizon (S7's profiles on the throat bulk at our plane;
      H-CROSSABLE-HORIZON, the board's, put to M).
  X17 THE DEMANDS, STATIONARY HALF (owner epass_frames; computed; deduced; STRUCTURAL; READ; OPEN).
      [PLANE]-conditional (eq. (17) as P1's metric; under 184 a vacuum-plane limit; under 172 (1) P1 is not the README's
      sheet, so this is a normalisation reference only): r_h = 2m with surface gravity kappa = 0 (Schwarzschild control
      1/4; v affine); W1 (STRUCTURAL): E = m c^2 crossing uniformly over the S^2; kappa_4^2 int T_vv dv = 1/(2m) per
      generator (computed, sympy), so the partner's is -1/(2m).
      [FREE], gated on the Lemma S owner's zeros (deduced; on H-STATIONARY-CROSSING, the board's): bulk form,
      T5^c(xi,xi) = -T5^R(xi,xi) - T5^m(xi,xi) along every generator, = -T5^R on the matter premise T^m(xi,xi)|_H = 0
      (the planes' matter held static across the horizon); its 5D normalisation is OPEN (the bulk horizon's section is
      the bulk balance's, 181).  Sheet form, the same on the README's own sheet, which under 172 (1) is position 2's
      piece, in a normalisation not computed (OPEN).  The pair's net per generator is the owner's zero: neither
      positive nor negative.  NOT RECONCILED WITH THE FIXED X13 (recorded, the owner not edited here): epass_frames was
      verified at c2e08b0 against the pairing owner before its blocker fix (md5 b8603300, then headed "the stationary
      pairing law"), and its stationary rows still carry that reading.  Their "refused, it becomes E-NS" is superseded
      by X13: refused while the size is kept, the pair is still demanded (at least as large as the README, exact
      unsheared or under 183), and only expansion, or a crease or separation of the bulk horizon at the sheet,
      releases it.  Their pointer "R(xi,xi) = 0 on any Killing horizon" is the spec's pre-fix statement, and their C26e
      mutation, the pairing owner's non_stationary(), breaks nullness, not stationarity (the pairing owner relabels it
      off_null).  The exact demand above stands as the stationary subcase (sigma = theta = 0).  epass_frames is listed
      for a re-read against epass_pairing md5 152621fa.
      SI (computed; u(G) standard-not-READ, CODATA 2018; W1 STRUCTURAL): at o3_write's example README E = 2.40588e16 J,
      m = G E/c^4 = 1.98791e-28 m and 1/(2m) = 2.51521e27 m^-1; at item 155's E = 3.8e22 J (the board's figure)
      m = 3.13983e-22 m and 1/(2m) = 1.59244e21 m^-1.  E and m [FREE], 1/(2m) [PLANE]-conditional.  E ~ G^(-1/2), read
      from the owner's own form, so u_r(m) = 1.12e-5 at the example README and 2.25e-5 at the fixed E.  These hold at
      our G.  187 (2) left gravity's strength per universe "For the math"; ITEM186 decided it provisionally under 149
      (one law of gravity in the bulk, H-ONE-G5; each universe's G from its own plane, H-G4-FROM-THE-PLANE; not
      seated; provisional until the closed-wall energy is computed, OPEN).
      158 (4): stationary, nothing net is absorbed (Lemma S); changing, into the bulk's Weyl field and the creased bulk
      horizon, a necessary condition only (deduced; OPEN).
      Set beside the demand, never a supply (READ, as the owner transcribes them): Gao-Jafferis-Wall 1608.05687v3, PDF
      p.2, "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes", and
      PDF p.4, "T_UU in the modified state along U > 0 will exactly cancel that along U < 0" (their non-traversable
      case); Maldacena-Stanford-Yang 1704.05333v1, PDF p.13, "we cannot send more information through the wormhole than
      we transferred in order to set up the OO interaction" (a one-sided parametric bound, set against 122 (4); not
      decided).  GJW's prerequisite is net-negative null energy of the TOTAL; under 183 Lemma S's pair totals zero,
      which is GJW's cancelling case: a tension, OPEN -- GJW's horizon is bifurcate and their analysis linearised, the
      corridor's is degenerate.  Within X13's premise (theta = 0) a net below zero along the generators needs shear.
      With kappa = 0, a crossing during which the horizon changes size between two moments of zero expansion (E-NS)
      also nets below zero: the computed identity integrates to int R(xi,xi) dv = -int (theta^2/3 + sigma^2) dv.  183
      (zero net per light ray, as the board glossed the option M chose) excludes every net-negative branch (deduced,
      here, from X13's identity; read by no separate session).  Which null geodesics GJW's criterion would apply to
      (theirs is ANEC along null geodesics through the wormhole), and whether it carries over to the corridor's horizon
      generators, is not checked (OPEN).
  X18 ENDS, GENERATORS, LEMMA P (owner epass_frames; computed; READ; deduced; OPEN).
      [FREE]: on global AdS2 (its induced metric equals Maldacena-Qi (2.1), READ PDF p.5; the parametrisation is
      standard-not-READ) d_T is elliptic, components (1, 1), with xi.xi = -1/sin^2 sigma < 0 (no Killing horizon);
      B_origin hyperbolic, (-cos T, cos T); K hyperbolic, (sin T, -sin T); J + K and J - K parabolic; J - B_origin (the
      Poincare d_t) parabolic, (1 + cos T, 1 - cos T).  x = 8/z^2 gives 4(-dt^2 + dz^2)/z^2 with z = 2 sqrt2/u, and the
      throat's d_v pushes forward to J - B_origin.
      [FREE given kappa = 0] -- kappa = 0 comes here from eq. (17) at r0 = 2m, so for the corridor these rows are
      [PLANE]-conditional, and under 179 whether the bulk corridor's horizon is degenerate is OPEN: the throat's d_v has
      Q = 0, parabolic (the owner's non-degenerate mutation turns it hyperbolic); the ingoing chart is smooth through
      u = 0, with end 1 (u > 0) on sigma=0, end 2 (u < 0) on sigma=pi, and u = 0 patch 1's future and patch 2's past
      horizon -- the shape of 122 (3)/132 only if patch 2 is position 2's side (OPEN).
      [FREE given AdS2]: on -(x/2)dt^2 + dx^2/(x(x - delta)), R = -1/2 and Q = delta/8 -- delta < 0 hyperbolic (the
      thermofield double, no passage, MQ PDF p.7), delta = 0 parabolic, delta > 0 elliptic (Maldacena-Qi's coupled
      wormhole, two-way, MQ PDF p.3).  An AdS2 throat alone does not fix the class; given kappa = 0 the corridor is the
      extremal member, delta = 0 (deduced).
      LEMMA P: (i) [FREE] a delta-stress S = s delta reads -s for every observer (1000 exact rational Lorentz
      transformations; s = 1, -1, 3/7).  (ii) [PLANE]-conditional: eq. (17)'s Weyl fluid at r = 3m, 8 pi rho = 1/81 and
      8 pi (rho + p_r) = -2/81, reads below zero for observers boosted beyond v* = 1/sqrt3 (rapidity 0.658479), and
      tends to -oo as v -> 1; NEC matter gives rho' >= rho (1000 exact rows); along S15's approach (rho tends to
      -sigma_RS, with rho + p bounded by 9.4e-7 sigma_RS: a bound, not a value), wherever rho < 0 < rho + p a boost
      reads the density above zero beyond v* = sqrt(-rho/p); at the bound itself (rho = -sigma_RS, rho + p =
      eps sigma_RS, eps = 9.4e-7) v* = 1/sqrt(1 + eps), with gamma^2 v^2 = 1/eps = 1.0638e6 at v*, and below the bound
      the boost needed is larger.  v is an observer's boost parameter, never a speed.  (iii) [FREE given AdS2]
      the boundary Killing charge flips under B_origin only; it does not flip under J, J + K, J - K or J - B_origin.
      DEDUCED: at the coincidence limit (never reached, 172 (2)) S15's -sigma_RS is a delta-stress, the same in every
      tangent frame.  The board's own 176 sentence ("position 2's -1 would be the partner's sign seen from our side")
      fails WITHIN ONE UNIVERSE at the limit under four premises (S15's [PLANE] sheet at our tension; the limit;
      kappa = 0; position 2's side taken as the opposite AdS2 boundary, OPEN); its between-universes clause is OPEN, so
      it is not refuted as a whole.  139 (2)'s "positive" can be met only as each piece's own-frame density
      (H-POSITIVE-IN-OWN-FRAME, the board's, put to M), and along the approach S15 computes that density negative
      (H-POSITIVE-ON-P2 fails there).
  X19 DEFERRED [PLANE] -- three phases of a coupling, across eq. (17)'s family at r0 = 2m.
  X20 DEFERRED [PLANE] -- the classical placements of E-Q (the plane's data, the conformal layer, the Bronnikov-Kim
      gap).
  X21 DEFERRED [PLANE] -- the transverse reading and the two pairs for 177 and 178 (Lemma S's own pair: its
      cancellation is [FREE], X13 (a)-(b); its [PLANE] ledger and tensor are X13 (d)).
  X22 DEFERRED [PLANE] -- the cap: the README held on P1 at the throat (conditional on H-README-AT-THE-THROAT, the
      board's; a held configuration, not a passage; the spec builds it after the core).
  X23 DEFERRED [PLANE] -- Kaus-Reall reproduced (support for the [PLANE] rows).
  X24 DEFERRED [PLANE] -- the between-universes column for phase 3 (Lemma S's law-independence, [FREE], already holds
      there: X13).
      WHY THE TEN WAIT: each takes eq. (17) as a plane's own metric -- the board's configuration, which 179/180
      (H-CORRIDOR-IN-BULK, M's) re-reads and clause (G), SEATED on M's "Seat both" (187 (3)), keeps only as a plane's
      possible reading of the corridor's mouth (H-PLANE-READS-MOUTH, the board's, OPEN); 181 puts the bulk balance
      first; under 184 a matter-free plane is a limit only.  The spec recommends building them only after the 179
      re-read decides whether the plane configuration stays as the board's comparison case.  That re-read is not made.
  X25 THE DECISION TABLE, RESTRICTED TO WHAT IS NOW COMPUTED [mixed] (deduced from X1-X10, X13, X14, X17's stationary
      half, X18 and sim2_facing S15; a row or cell that needs a deferred section is left out and named).  Gates:
      G1 REGULAR PAST (174 (1)); G2 POSITIVE (139 (2), in its own frame: H-POSITIVE-ON-P2, H-POSITIVE-IN-OWN-FRAME, the
      board's); G3 NEC (117/120; 183: net along each light ray); G4 CROSSES AT FIXED SIZE (143 A, 132, 162, 163: Lemma
      S, and Lemma K for a net-flux crossing).
      R0 no second sheet, README on P1 [PLANE]: G1 fails (X7-X8: within O(x) every claimed layer lies in J^-(P_c) below
         the write's floor; the far-time half, X11, DEFERRED); G4 needs a partner at least as large as the README along
         each generator, exact under 183 (X13), and no classical, NEC-obeying matter supplies one (deduced).  The route
         with no second sheet is REFUTED on X8's conjunction (G1 alone suffices); E-PASS as a whole is not.
      R2-R3 position 2's piece shallower than d_+ [PLANE]: G2 fails (S15: outside the positive-energy window
         [d_+, top]; X9).  The band's split at d_beta is X15's, DEFERRED.
      R4 position 2's piece in [d_+, top] (ell > 27.07m only) [PLANE]: G1 holds near the throat for the profiles X9
         passes, the cover and the far field OPEN (E-G, E-FAR); G2 and G3 hold classically (S15); G4, stationary: the
         exact pair (X13), with no classical partner (deduced), OPEN through 177/183 as H-PARTNER-IS-THE-COUPLING (the
         supply not computed); changing: a five-dimensional event (X14), its coefficient X15's, DEFERRED.  No classical
         crossing; OPEN only as 177's partner or as E-NS.
      R5 coinciding, depth -> 0 [PLANE]: G1, the slab pinches along the horizon line through P_c and power-law P2
         stress diverges along the regular null frame (X9, C11b); G2 fails at every finite ell (S15: rho_m -> -2
         sigma_RS; X10 (e)), and at the limit, never reached, -sigma_RS is a delta-stress, the same in every tangent
         frame (X18, Lemma P (i)); G3 marginal (X10 (e)).  Fails G2 within one universe at finite ell (174 (3)); at
         ell = inf a limit (flat, no RS localisation).
      R6 classical E-Q: on the unsheared horizon of (b)'s family the bulk Weyl term gives nothing along the
         generators, E(xi,xi) = 0 ([FREE], X13 (c); a sheared horizon is not computed); a static
         symmetric coupling that leaves the plane's data unchanged changes nothing, and a horizonless link removes the
         horizon against 132 ([PLANE], X10 (c)-(d)); the conformal layer and the BK gap are X20's, DEFERRED.  Pays
         nothing along the generators.
      R7 coupled ends, quantum (177): a negative partner along each generator at least as large as the README, exact
         under 183, sheet or bulk form (X13); at [PLANE], among null-dust partners with no held momentum flux, only the
         README's exact reverse, with a zero total stress (X13 (d)); GJW's net-negative prerequisite
         stands against Lemma S's zero total (X17): a tension, OPEN; given kappa = 0 the corridor is the extremal,
         parabolic member (X18).  OPEN: the demand exact, the supply beyond the board's instruments.
      R8 changing corridor (E-NS; 152 (2), 160): needs expansion (theta != 0, against 162 as read through
         H-FIXED-SIZE-AS-THETA-ZERO) or a crease or separation of the bulk horizon at the sheet (X14); its number,
         Lemma L's, is X15's, DEFERRED.  OPEN, to phase 2b-ii.
      R9 between universes: Lemma S is law-independent, so the pair is still demanded (X13); X24 DEFERRED.  Handed to
         phase 3.
      LEFT OUT (deferred): R1, the cap (X22); R2-R3's split at d_beta (X15); the far gate (X12).
      COMBINED, restricted (deduced): within one universe at our tension no configuration computed here carries the
      README across the corridor object's horizon with a regular past through the write.  Position 2's near-coinciding
      piece regularises the crossing's past near the throat (X9) and does not pay the crossing (X13).  A horizon that
      keeps its size takes a partner at least as large as the README along each generator, exactly as large only if
      unsheared, and under 183 exactly as large (X13).  A net-flux crossing is a five-dimensional event (X14).  The
      classical Weyl term pays nothing on the unsheared horizon computed; quantum E-Q could supply only the partner
      (exact under 183), which the board cannot compute, and GJW's net-negative prerequisite stands against that zero
      total (OPEN).
  OPEN (X11-X25, plainly).  The partner's supply (177; H-PARTNER-IS-THE-COUPLING, the board's; 188's
      H-PARTNER-AS-ENTANGLED-REFLECTION, M's, offered for the math, bears on it and is not used).  GJW's net-negative
      prerequisite against Lemma S's zero total.  The bulk-form demand's 5D normalisation (181) and the demand on
      position 2's piece in its own normalisation (172 (1)).  Whether 162's fixed size is zero expansion
      (H-FIXED-SIZE-AS-THETA-ZERO) and which sheets 143 admits (H-CROSSABLE-HORIZON): put to M.  Whether the crossing
      is stationary (H-STATIONARY-CROSSING) is NOT put to M: 158 (3) left whether the bulk is static during the hold to
      the math, and 139 (3) asked the board not to re-ask the static question; after the fix it is not Lemma S's
      premise, and the board decides it under 149 where a result needs it.  Whether the bulk corridor's horizon is
      degenerate under 179 (kappa = 0 comes from eq. (17) here), on which the parabolic class rests.  Which boundary is
      position 2's side (H-END-2-IS-OUR-PLANE, X1; epass_frames names it H-END-2-IS-OUR-FAR-END).  The 176 sentence
      between universes, and 139 (2)'s positivity in position 2's own frame (phase 3).  MSY's parametric bound against
      122 (4) (reported, not decided).  Gravity's strength per universe (187 (2); provisional in ITEM186, OPEN).
      epass_frames' stationary rows, to be re-read against the fixed X13 (X17).  The ten [PLANE] sections, after the
      179 re-read.
  SINCE THE SPEC (noted; nothing decided here): 185, the matter round (lemmas/ITEM185-MATTER-ROUND.md); 186, k per
      corridor (H-K-PER-CORRIDOR, M's, conditional; lemmas/ITEM186-K-PER-CORRIDOR.md; set aside as the working
      assumption by 191's record) -- both notes were being written when this integration began and are since headed
      "verified once, findings applied"; 187 (3), clauses (G) and (Z) SEATED as the board worded them; 188, M's thought
      on the partner as a positron, an entangled reflection (H-PARTNER-AS-ENTANGLED-REFLECTION; lemmas/ITEM188-PARTNER.md,
      since headed "verified once, findings applied", proposes restating X25's R7 as "no READ construction supplies it
      at kappa = 0; beyond READ constructions, OPEN" -- noted, not applied here).  Recorded while this integration ran,
      and only noted: 189, "the bond" (H-PAIRING-HELD-AS-TENSION, M's: 188's tension is the bond holding the pair, not
      the partner); 190, "Information is energy" (H-INFORMATION-IS-ENERGY, M's; the board's reading, to be worked:
      where the README's information crosses, its energy crosses, so Lemma S's partner is needed); 191 and 192, k's
      scale (H-K-LIKE-GRAVITY; H-K-TIE-TO-THE-CYPHER); 193, the pair as an axiom (H-PAIR-AXIOM), WITHDRAWN by M at 194,
      which puts the pair's question to the cypher and returns input F5 (the exact +/- null pair) to OPEN; 195, "The
      README is not a pair" (H-README-NOT-A-PAIR, M's; the board's reading, to be computed: the README is HELD by the
      corridor's horizon rather than crossing it, in which case Lemma S asks no partner, and the crossing framing used
      here is the board's, not M's); 196, every question through the cypher (M-ALL-QUESTIONS-THROUGH-THE-CYPHER, M's),
      which bears on how the readings put to M are worked.  None of 189-196 changes a computed row here.
  It is necessary, not sufficient, and never B4d green.  No value here is the corridor's length (155 (2): in bits), a
  distance between the positions or anything the device sees (101 (7)), or a speed (139 (4)): the depths d and y are
  locations in the bulk and ell its curvature length, all in units of m, and the budgets are holds for the cone
  premise, as stage 5 F3's.

python3 sim2_passage.py [--selftest] [--mutants] [--json PATH]
  (needs sympy, numpy, scipy, mpmath, python-flint, and the two owners' own owners; --selftest about two minutes, the
  owners' own selftests included; --mutants several minutes: for every check a named mutation of the instrument's own
  input (for C15-C19 and C26-C31, of the owner's) that the check must FAIL under, then each owner's own --mutants run
  as a subprocess and its count reported; exit 1 if any mutation survives or raises, or an owner's --mutants fails)
"""
import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as Fr
from math import gcd

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
F_LAYERS = (1e2, 1e4, 1e6, 1e10)            # layers K = F K_bs (the claimed rows, within O(x))
F_SCAN = (1e15, 1e20, 1e25, 1e30, 1e31, 1e32, 1e33)   # past the claimed rows: where the layer budget passes the floor
X_LIMS = (1e-2, 1e-4, 1e-6, 1e-8)          # throat-region bounds for X7's exact-throat rows (the tested range)
X_LIMS_PAST = (1e-9, 1e-10)                # past the tested range: the exact-throat bracket crosses the floor here
ELL_SHOW = (Fr(0), Fr(1, 8), Fr(1))        # ell = inf, 8m, m: the ground stage's three columns
GROUND_ETA = {"0": 5.726, "1/32": 5.466, "1/16": 5.242, "1/8": 4.876, "1/4": 4.344, "1/2": 3.680, "1": 2.969,
              "2": 2.302, "4": 1.733}      # the ground stage's eta_s (scratch, not board evidence): a cross-check only
KASNER_A = (1 + math.sqrt(3)) / 4          # X4's deduced exponent (the Kasner tail's)
ALPHA_CUT = 1e-9                           # eta_of's y-integration stops here; the tail is added once
ALPHA_CUT_B = 1e-12                        # the independent integration (eta as the variable) stops here
ETA_CUTS = (1e-3, 1e-6)                    # the control's intermediate cuts (with ALPHA_CUT)
DP_GRID = (480, 240, 6)                    # C9's dynamic programme: eta cells, w cells, stencil reach
BANNED_KEYS = ("dist", "separation", "time", "redshift", "speed", "velocity", "length", "clock", "arrival")

# The instrument's own inputs that --mutants mutates (one named mutation per check; the defaults are the instrument).
CHART_SHIFT = 2                            # X1: t = v + CHART_SHIFT sqrt2/u
G_VU = sp.sqrt(2)                          # X1-X3: g_vu = G_VU alpha^2
GVV_POWER = 2                              # X2: g_vv = -alpha^2 (u^P - hh^P)/2
KASNER_MUT = 0.0                           # X4's fits: p' gets -(2 + KASNER_MUT) p q
KASNER_CONS_PQ = 4                         # X4's leading balance: the constraint's 4pq
ETA_TAIL_COUNT = 1                         # X5: the Kasner tail is added this many times
ETA_CONTROL_MUT = 1.0                      # X5's control: the mutated ODE's 2pq -> (2 + this) pq
ADS2_R2 = 4                                # X6, X7: the conformal AdS2 factor's radius squared
COINCIDE_FRAC = 0.0                        # X9: the coinciding limit is taken at depth COINCIDE_FRAC y_s
PLANE_DATA = "eq17"                        # X10 (b): the plane's data
DATA_CONSTRAINED = True                    # X10 (c): q(0) solved from the yy constraint
INJECT_KEY = None                          # C14's mutation: a key added to the output


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


SF = _load(os.path.join(HERE, "sim2_facing.py"), "passage_sim2facing")
OW = _load(os.path.join(HERE, "o3_write.py"), "passage_o3write")
ES2 = SF.ES2


def write_floor():
    """o3_write's least write at the example README (Z = 108.75), in clocks: the hold E-PASS's cone premise must cover."""
    return float(OW._num(OW.t_min(3)))


# ------------------------------------------------------------------------------------------------------- X1-X3 chart
def _christoffel(g, X):
    n = len(X)
    gi = g.inv()
    return gi, [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                                  for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]


def _ricci(G, X):
    n = len(X)
    return lambda b, c: sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                                        + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a] for d in range(n))
                                        for a in range(n)))


def ef_metric(hh=0, shift=2):
    """The throat metric in the (y, v, u) chart; hh != 0 gives the non-degenerate control g_vv = -alpha^2 (u^2 - hh^2)/2.
    g_vu = G_VU alpha^2 and the power in g_vv are the instrument's inputs (C2-C4's mutations)."""
    y, v, u, th, ph = sp.symbols("y v u theta phi", real=True)
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    g = sp.zeros(5)
    g[0, 0] = 1
    g[1, 1] = -al**2 * (u**GVV_POWER - sp.sympify(hh)**GVV_POWER) / 2
    g[1, 2] = g[2, 1] = G_VU * al**2
    g[3, 3] = 4 * be**2
    g[4, 4] = 4 * be**2 * sp.sin(th)**2
    return g, [y, v, u, th, ph], al, be


def chart_identity(shift=None):
    """X1: x = u^2, t = v + shift sqrt2/u in -(x/2) dt^2 + dx^2/x^2, minus the EF form; 0 at shift = 2."""
    shift = CHART_SHIFT if shift is None else shift
    u = sp.Symbol("u", positive=True)
    dv, du = sp.symbols("dv du")
    dt = dv - shift * sp.sqrt(2) / u**2 * du
    dx = 2 * u * du
    return sp.simplify(sp.expand(-(u**2 / 2) * dt**2 + dx**2 / u**4) - (-(u**2 / 2) * dv**2 + 2 * sp.sqrt(2) * dv * du))


def _constraint(p, q, a, b, e, cons_pq=4):
    """The Hamiltonian (yy) constraint as sim2_facing's throat_row codes it.  That line is not a function there, so it is
    written out ONCE, here (the only line of an owner this file re-types), used by coded_system (symbols) and
    data_fixes_bulk (arrays), and checked against the 5D vacuum equations themselves by C2.  cons_pq != 4 mutates the
    4pq (C5's second mutation)."""
    return p * p + q * q + cons_pq * p * q - 6 * e * e - 1 / (4 * b * b) + 1 / (4 * a * a)


def coded_system(p, q, a, b, e, s2=1, cons_pq=4):
    """sim2_facing's coded zeroth-order system as expressions: P = p' and Q = q' taken from sim2_facing.throat_rhs itself
    (called on symbols, the O(x) slots zero: imported, not re-typed), and the Hamiltonian constraint C (_constraint):
    the forms X1 compares against and X4's leading balance is taken from.  s2 = -1 flips the S2 term (C2's control);
    cons_pq != 4 mutates the constraint's 4pq (C5's second mutation)."""
    P, Q = SF.throat_rhs(0, [a, b, p, q] + [sp.Integer(0)] * 6, e, sp.Integer(s2))[2:4]
    C = _constraint(p, q, a, b, e, cons_pq)
    return P, Q, C


def chart_equations(s2=1):
    """X1: the 5D vacuum equations R_ab + (4/ell^2) g_ab = 0 in the EF chart, reduced against sim2_facing's coded P, Q and
    constraint (s2 = -1 compares against the S2-flipped coded system: the control)."""
    g, X, al, be = ef_metric()
    e = sp.Symbol("e", nonnegative=True)
    gi, G = _christoffel(g, X)
    R = _ricci(G, X)
    E = {(i, j): sp.simplify(R(i, j) + 4 * e**2 * g[i, j]) for i in range(5) for j in range(i, 5)}
    nonzero = sorted(k for k, v in E.items() if v != 0)
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    sub = {sp.Derivative(al, (X[0], 2)): (P + p**2) * a, sp.Derivative(be, (X[0], 2)): (Q + q**2) * b,
           sp.Derivative(al, X[0]): p * a, sp.Derivative(be, X[0]): q * b}
    Es = {k: sp.simplify(E[k].subs(sub).subs({al: a, be: b})) for k in nonzero}
    sols = sp.solve([Es.get((1, 2), 0), Es.get((3, 3), 0)], [P, Q], dict=True)
    coded_P, coded_Q, coded_c = coded_system(p, q, a, b, e, s2)
    u = X[2]
    if not sols or P not in sols[0] or Q not in sols[0]:
        return {"nonzero": [list(k) for k in nonzero], "P": "no solution", "Q": "no solution", "vv_over_vu": None,
                "uu": Es.get((2, 2), 0), "constraint_ratio": "no solution"}
    sol = sols[0]
    cons = sp.simplify(sp.expand(Es[(0, 0)].subs(sol)) / coded_c) if (0, 0) in Es else 0
    return {"nonzero": [list(k) for k in nonzero], "P": sp.simplify(sol[P] - coded_P), "Q": sp.simplify(sol[Q] - coded_Q),
            "vv_over_vu": sp.simplify(Es[(1, 1)] / Es[(1, 2)] + u**2 / (2 * sp.sqrt(2))) if (1, 1) in Es else None,
            "uu": Es.get((2, 2), 0), "constraint_ratio": cons}


def horizon(hh=0):
    """X2: xi = d_v, its norm, g^uu, g^yu and kappa^2 = -(1/2) nabla_a xi_b nabla^a xi^b (Killing: nabla_a xi_b =
    d_[a xi_b]); evaluated on u = hh (the horizon of the metric)."""
    g, X, al, be = ef_metric(hh)
    gi = g.inv()
    xi = [g[i, 1] for i in range(5)]
    F = sp.Matrix(5, 5, lambda i, j: (sp.diff(xi[j], X[i]) - sp.diff(xi[i], X[j])) / 2)
    k2 = sp.factor(sp.simplify(-sp.Rational(1, 2) * sum(F[i, j] * sum(gi[i, k] * gi[j, l] * F[k, l] for k in range(5)
                                                                         for l in range(5))
                                                         for i in range(5) for j in range(5))))
    u = X[2]
    return {"norm": sp.factor(g[1, 1]), "g_uu_inv": sp.simplify(gi[2, 2]), "g_yu_inv": sp.simplify(gi[0, 2]),
            "kappa2": k2, "kappa2_on": sp.simplify(k2.subs(u, hh)), "norm_on": sp.simplify(g[1, 1].subs(u, hh)),
            "g_uu_inv_on": sp.simplify(gi[2, 2].subs(u, hh))}


def one_way():
    """X3, taken from ef_metric (not a hand-typed form): the radial null directions of its (v, u) block per alpha^2
    (g_uu = 0, so dv = 0 or du/dv = -g_vv/(2 g_vu)), the sign of g(d_v, d_u) per alpha^2, and X9's crossing at finite
    proper time: on the plane (alpha = 1) a radial timelike geodesic with Killing energy E = -g(d_v, x') has u'^2 as
    returned (E^2/2 - u^2/4 on the throat), so u' = -E/sqrt2 at u = 0."""
    g, X, al, be = ef_metric()
    u = X[2]
    w = sp.Symbol("w", real=True)                                         # w = du/dv
    gvv, gvu = sp.simplify(g[1, 1] / al**2), sp.simplify(g[1, 2] / al**2)
    roots = sp.solve(sp.Eq(gvv + 2 * gvu * w, 0), w)
    E, vd, ud = sp.symbols("E vdot udot", real=True)
    sols = sp.solve([sp.Eq(E, -(gvv * vd + gvu * ud)), sp.Eq(gvv * vd**2 + 2 * gvu * vd * ud, -1)], [vd, ud], dict=True)
    ud2 = sorted({str(sp.simplify(sp.expand(s_[ud]**2))) for s_ in sols})
    return {"dudv": roots, "g_v_u": gvu, "udot2": ud2}


# -------------------------------------------------------------------------------------------------- X4-X5 the throat
_TB = {}
_ETA = {}


def tb(e):
    k = str(Fr(e))
    if k not in _TB:
        _TB[k] = SF.throat_bulk(e)
    return _TB[k]


def kasner_deduced():
    """X4: the leading balance of the coded system near y_s, p = -a/delta, q = -b/delta (alpha ~ delta^a, beta ~
    delta^b), the 4e^2, 6e^2, 1/(4 alpha^2) and 1/(4 beta^2) terms subleading for a < 1, b < 1 (dropped: a, b -> oo in
    coded_system's alpha, beta slots).  The evolution equations give a + b = 1/2; the constraint gives ab = -1/8."""
    A, B, dl = sp.symbols("a b delta", real=True)
    al_, be_, e_ = sp.symbols("alpha beta e", positive=True)
    P, Q, C = coded_system(-A / dl, -B / dl, al_, be_, e_, cons_pq=KASNER_CONS_PQ)
    lead = lambda ex: sp.simplify(sp.expand(ex.subs({e_: 0}) * dl**2).subs({al_: sp.oo, be_: sp.oo}))
    eq_p = sp.factor(sp.expand(-A - lead(P)))                         # p' = -a/delta^2
    eq_q = sp.factor(sp.expand(-B - lead(Q)))
    eq_c = sp.expand(lead(C))
    sols = sp.solve([eq_p, eq_q, eq_c], [A, B], dict=True)
    sols = [s_ for s_ in sols if s_[A] != 0 and s_[B] != 0]
    s = max(sols, key=lambda d_: float(d_[A]))                        # the alpha -> 0 branch (a > 0): the computed one
    a, b = sp.nsimplify(s[A]), sp.nsimplify(s[B])
    return {"a": a, "b": b, "sum": sp.simplify(2 * a + 2 * b), "squares": sp.simplify(2 * a**2 + 2 * b**2),
            "ab": sp.simplify(a * b), "a_plus_b": sp.simplify(a + b), "evolution_p": str(eq_p), "evolution_q": str(eq_q),
            "constraint": str(eq_c), "n_branches": len(sols)}


def _zeroth(e, mutate=0.0):
    """The zeroth-order throat system (SF.throat_rhs, imported) to alpha = 1e-12 (X4's fit); mutate adds -mutate*p*q to
    p' (2pq -> (2 + mutate) pq: the control)."""
    ef = float(e)

    def rhs(y, u):
        f = SF.throat_rhs(y, list(u) + [0.0] * 6, ef)[:4]
        f[2] -= mutate * u[2] * u[3]
        return f

    def end(y, u):
        return u[0] - 1e-12
    end.terminal = True
    return solve_ivp(rhs, [0, 12], [1.0, 1.0, -ef, -ef], method="DOP853", rtol=1e-13, atol=1e-16, events=[end],
                     dense_output=True, max_step=0.005)


def kasner_fit(e, mutate=None):
    """X4: the exponents d ln alpha / d ln delta and d ln beta / d ln delta at the end, delta = y_s - y, from -p delta and
    -q delta (p = alpha'/alpha), with y_s taken where alpha = 1e-12."""
    mutate = KASNER_MUT if mutate is None else mutate
    s = _zeroth(e, mutate)
    ys = float(s.t[-1])
    out = []
    for dl in (1e-6, 1e-7):
        u = s.sol(ys - dl)
        out.append((-float(u[2]) * dl, -float(u[3]) * dl))
    return {"y_s": ys, "a": out[-1][0], "b": out[-1][1], "drift": abs(out[0][0] - out[1][0])}


def _eta_solve(e, mut=0.0):
    """X5: (alpha, beta, p, q, eta) on the zeroth-order throat system (SF.throat_rhs, imported; mut adds -mut*p*q to p',
    the control's mutation), eta' = 1/alpha integrated with the system to alpha = ALPHA_CUT, with events at ETA_CUTS."""
    key = (str(Fr(e)), float(mut))
    if key not in _ETA:
        ef = float(e)

        def rhs(y, u):
            f = SF.throat_rhs(y, list(u[:4]) + [0.0] * 6, ef)[:4]
            f[2] -= mut * u[2] * u[3]
            return f + [1.0 / u[0]]
        evs = []
        for c in ETA_CUTS:
            ev = (lambda c_: (lambda y, u: u[0] - c_))(c)
            ev.terminal = False
            evs.append(ev)

        def end(y, u):
            return u[0] - ALPHA_CUT
        end.terminal = True
        _ETA[key] = solve_ivp(rhs, [0, 40], [1.0, 1.0, -ef, -ef, 0.0], method="DOP853", rtol=1e-13, atol=1e-15,
                              events=evs + [end], dense_output=True, max_step=0.005)
    return _ETA[key]


def eta_of(e, y, mut=0.0, cut=None):
    """eta(y) = int_0^y dy/alpha on the zeroth-order throat bulk, integrated as an ODE variable (not by quadrature: the
    first version's quadrature already extrapolated to alpha -> 0 and then had the tail added again).  For y >= y_s:
    eta_s = eta(alpha = ALPHA_CUT) + the Kasner tail int_0^delta_end d delta/(alpha_end (delta/delta_end)^a)
    = delta_end/(alpha_end (1 - a)), delta_end = -a/p_end, added ETA_TAIL_COUNT times (once; C6's mutation, twice).
    cut = an alpha in ETA_CUTS + (ALPHA_CUT,): eta there, no tail (X5's control).  mut: the control's mutated ODE."""
    s = _eta_solve(e, mut)
    if cut is not None:
        cuts = list(ETA_CUTS)
        if cut in cuts:
            ev = s.y_events[cuts.index(cut)]
            return float(ev[0][4]) if len(ev) else float("nan")
        return float(s.y[4, -1])
    ys = float(s.t[-1])
    if y < ys:
        return float(s.sol(y)[4])
    al, p, eta = float(s.y[0, -1]), float(s.y[2, -1]), float(s.y[4, -1])
    d_end = -KASNER_A / p
    return eta + ETA_TAIL_COUNT * d_end / (al * (1 - KASNER_A))


def eta_independent(e):
    """X5's cross-check: eta as the independent variable, d(alpha, beta, p, q, y)/d eta = alpha (alpha p, beta q, P, Q, 1)
    (SF.throat_rhs), to alpha = ALPHA_CUT_B = 1e-12, plus the Kasner tail once."""
    ef = float(e)

    def rhs(t_, u):
        f = SF.throat_rhs(u[4], list(u[:4]) + [0.0] * 6, ef)[:4]
        return [u[0] * v_ for v_ in f] + [u[0]]

    def end(t_, u):
        return u[0] - ALPHA_CUT_B
    end.terminal = True
    s = solve_ivp(rhs, [0, 20], [1.0, 1.0, -ef, -ef, 0.0], method="DOP853", rtol=1e-13, atol=1e-16, events=[end],
                  max_step=0.01)
    al, p = float(s.y[0, -1]), float(s.y[2, -1])
    return float(s.t[-1]) + (-KASNER_A / p) / (al * (1 - KASNER_A))


def eta_control(e=Fr(1, 8)):
    """X5's control (computed through eta_of): eta at alpha = 1e-3, 1e-6, 1e-9 on the mutated ODE of X4's control
    (2pq -> (2 + ETA_CONTROL_MUT) pq: alpha ~ delta^1.002) and on the true system.  Their increments per three decades
    of alpha: the mutated's do not shrink (eta diverges), the true system's shrink."""
    cuts = list(ETA_CUTS) + [ALPHA_CUT]
    mutated = [eta_of(e, 0.0, mut=ETA_CONTROL_MUT, cut=c) for c in cuts]
    true = [eta_of(e, 0.0, mut=0.0, cut=c) for c in cuts]
    inc = lambda vs: [vs[i + 1] - vs[i] for i in range(len(vs) - 1)]
    return {"cuts": cuts, "mutated": mutated, "true": true, "mutated_inc": inc(mutated), "true_inc": inc(true)}


# ---------------------------------------------------------------------------------------------- X6 the causal past
def _conformal_geodesics():
    """Christoffels of d eta^2 + R2(-w^2 dv^2 + 2 dv dw) (w = 1/zeta; regular through the horizon w = 0; R2 = ADS2_R2 =
    4, the radius-2 AdS2), lambdified."""
    et, v, w = sp.symbols("eta v w", real=True)
    g = sp.Matrix([[1, 0, 0], [0, -ADS2_R2 * w**2, ADS2_R2], [0, ADS2_R2, 0]])
    X = [et, v, w]
    _, G = _christoffel(g, X)
    f = sp.lambdify((et, v, w), [[[G[a][b][c] for c in range(3)] for b in range(3)] for a in range(3)], "numpy")
    return f


def jminus_check(n_rays=8, eta_to=6.0, wrong=False, n_timelike=4):
    """X6: past-directed null geodesics from P_c = (eta 0, v 0, w 0); along each, the criterion's equality
    (-v) w = 2 sin^2(eta/4) (wrong=True: 2 sin^2(eta/2), the control); the rays are one orbit of the dilatation
    v -> lambda v, w -> w/lambda.  And past-directed timelike geodesics: the strict inequality, the interior.
    Returns the worst relative residual on the null rays and the least relative margin on the timelike ones."""
    G = _conformal_geodesics()

    def rhs(lam, s):
        x, d_ = s[:3], s[3:]
        Ga = np.array(G(*x), dtype=float)
        acc = [-sum(Ga[a][b][c] * d_[b] * d_[c] for b in range(3) for c in range(3)) for a in range(3)]
        return list(d_) + acc

    def stop(lam, s):
        return s[0] - eta_to
    stop.terminal = True
    crit = lambda et: 2 * math.sin(et / (2 if wrong else 4))**2

    def ray(c1, wd):
        return solve_ivp(rhs, [0, 1e4], [0.0, 0.0, 0.0, c1, -1.0, wd], method="DOP853", rtol=1e-12, atol=1e-14,
                         events=[stop], dense_output=True)
    worst = 0.0
    for k in range(n_rays):
        c1 = 0.3 + 2.7 * k / max(1, n_rays - 1)                     # d eta/d lambda; v' = -1 (past-directed)
        sol = ray(c1, c1 * c1 / (2 * ADS2_R2))                       # null at w = 0: c1^2 + 2 R2 v' w' = 0
        for lam in np.linspace(sol.t[-1] * 0.05, sol.t[-1], 40):
            et, v, w = sol.sol(lam)[:3]
            worst = max(worst, abs(-v * w - crit(et)) / max(crit(et), 1e-12))
    margin = float("inf")
    for k in range(n_timelike):
        c1 = 0.5 + 0.8 * k
        sol = ray(c1, c1 * c1 / (2 * ADS2_R2) + 0.05 * (1 + k))      # timelike: c1^2 + 2 R2 v' w' < 0
        for lam in np.linspace(sol.t[-1] * 0.05, sol.t[-1], 40):
            et, v, w = sol.sol(lam)[:3]
            margin = min(margin, (-v * w) / max(crit(et), 1e-12) - 1)
    return {"worst": worst, "interior_margin": margin}


# ---------------------------------------------------------------------------------------------- X7 the cone budget
def budget(eta, x_lim):
    """X7: the advanced-coordinate hold (clocks) a causal curve from a point at conformal depth eta, kept at x <= x_lim,
    needs to reach P_c: [lower, upper] = zeta_lim [2 sin^2(eta/4), eta/2]."""
    z = 2 * math.sqrt(2) / math.sqrt(x_lim)
    return z * 2 * math.sin(eta / 4)**2, z * eta / 2


def g_confined(eta):
    """The ground stage's confined minimum per zeta_lim: 2 sin^2(eta/4) for eta <= pi, 1 + (eta - pi)/2 beyond."""
    return 2 * math.sin(eta / 4)**2 if eta <= math.pi else 1 + (eta - math.pi) / 2


def budget_tight(eta, x_lim):
    """X7: zeta_lim g(eta), the least hold for a curve confined to x <= x_lim (C9 checks it against the programme)."""
    return 2 * math.sqrt(2) / math.sqrt(x_lim) * g_confined(eta)


def dp_confined(eta_max=6.2, grid=None):
    """C9's independent computation: a dynamic programme for the least advanced-coordinate hold v_c - v_q from
    (eta, w = 1) (zeta = zeta_lim = 1; holds scale with zeta_lim) to P_c = (0, w = 0), over causal curves of
    d eta^2 + R2(-w^2 dv^2 + 2 dv dw) confined to w <= 1.  A future causal step (d eta, dw) costs at least
    dv_+ = (d eta^2/R2)/(sqrt(dw^2 + w^2 d eta^2/R2) - dw); steps toward the plane over a stencil of reach K, free
    inward moves (dv = 0) at fixed eta.  Returns (eta grid, least hold at w = 1)."""
    n_eta, n_w, K = grid or DP_GRID
    he, hw = eta_max / n_eta, 1.0 / n_w
    W = np.arange(n_w + 1) * hw
    V = np.full((n_eta + 1, n_w + 1), np.inf)
    V[0, :] = 0.0                                                   # on the plane the ingoing null leg costs nothing
    steps = [(i, j) for i in range(1, K + 1) for j in range(-K, K + 1) if gcd(i, abs(j)) == 1]
    for i in range(1, n_eta + 1):
        best = np.full(n_w + 1, np.inf)
        for di, dj in steps:
            if di > i:
                continue
            idx = np.arange(max(0, -dj), min(n_w, n_w - dj) + 1)
            wm = (W[idx] + W[idx + dj]) / 2
            deta, dw = di * he, dj * hw
            s = np.sqrt(dw * dw + wm * wm * deta * deta / ADS2_R2)
            with np.errstate(divide="ignore", invalid="ignore"):
                cost = np.where(s - dw > 0, (deta * deta / ADS2_R2) / (s - dw), np.inf)
            best[idx] = np.minimum(best[idx], V[i - di][idx + dj] + cost)
        V[i] = np.minimum.accumulate(best)
    return np.arange(n_eta + 1) * he, V[:, -1]


def layer(e, F):
    """X7: the layer K_th = F K_bs: its depth, eta there, x_lim = min x_valid over [0, y_K] (O(x) <= 0.1), its budget
    and the confined minimum."""
    s = tb(e)
    yK = SF._yK(s, F)
    if yK is None:
        return None
    ys = np.linspace(1e-6, yK, 400)
    xl = min(SF.x_valid(s, z) for z in ys)
    et = eta_of(e, yK)
    lo, hi = budget(et, xl)
    return {"F": F, "y_K": yK, "eta": et, "x_lim": xl, "lower": lo, "upper": hi, "tight": budget_tight(et, xl)}


def layer_scan(e, floor):
    """X7, past the claimed rows: the layers at F_SCAN, the first F whose LOWER budget passes the write's floor (None if
    the full system ends first), and the fitted exponent of the upper budget in K between 1e15 and 1e30 K_bs."""
    rows = [layer(e, F) for F in F_SCAN]
    cross = next((L["F"] for L in rows if L and L["lower"] > floor), None)
    byF = {L["F"]: L for L in rows if L}
    expo = (math.log(byF[1e30]["upper"] / byF[1e15]["upper"]) / math.log(1e15)) if 1e15 in byF and 1e30 in byF else None

    def deepest(key):                      # the deepest scan row with every row up to it below the floor on `key`
        last = None
        for L in rows:
            if L is None or L[key] >= floor:
                break
            last = L["F"]
        return last
    prev = None if cross is None else (F_SCAN[F_SCAN.index(cross) - 1] if F_SCAN.index(cross) else F_LAYERS[-1])
    return {"rows": rows, "crossover_F": cross, "crossover_after_F": prev, "exponent": expo,
            "placed_F": deepest("upper"), "placed_tight_F": deepest("tight")}


# ------------------------------------------------------------------------------------------ X9 position 2's piece
def k_ratio(e, y):
    s = tb(e)
    return SF.kret_throat(s["sol"].sol(y), float(e)) / SF.S5.k_bs(float(e), 2.0, y)


def k_ratio_zero_deduced(e):
    ef = float(e)
    return 2 * (80 * ef**4 + 3) / (160 * ef**4 + 3)


SLAB_KINDS = (("level",),) + tuple(SF.CO_KINDS)       # the level surface, S7's power laws, the smooth family


def _kname(kind):
    return "level" if kind[0] == "level" else SF._kind_name(kind)


def _profile_margin(s, dep, xv, kind, W1, ys):
    """X9: y_s^th minus P2's deepest point d + f(x) over x <= x_valid(d) (the verification's convention), and where a
    power law reaches y_s^th (x_hit).  None for a level surface where W1(d) < 0 (not admissible) or at depth 0."""
    if kind[0] == "level":
        if dep <= 0 or float(W1(dep)) < -1e-9:
            return None, None
        return ys - dep, None
    g2 = SF._smooth_g2(s, dep, W1) if kind[0] == "smooth" else 0.0
    xs = np.logspace(-14, math.log10(xv), 240)
    fmax = max(SF._profile(kind, x, g2)[0] for x in xs)
    mg = ys - dep - fmax
    xh = None
    if mg < 0 and kind[0] == "pow":
        h = lambda lx: dep + SF._profile(kind, 10.0**lx, g2)[0] - ys
        if h(-14.0) >= 0:
            xh = 0.0                                   # already deeper than y_s^th at x = 1e-14, the grid's floor
        elif h(math.log10(xv)) > 0:
            xh = 10.0 ** brentq(h, -14.0, math.log10(xv), xtol=1e-12)
    return mg, xh


def slab_rows(e, dv):
    """X9: depths of P2 -- depth 0 (the coinciding limit), y*, the band's midpoint, 0.1 y_s, d_+ where it exists
    (including d_+ = 0.0 at ell = inf, the flat limit) -- with eta(d), K/K_bs at d, u_min = 4 sqrt2 sin^2(eta(d)/4)/Delta_v
    at Delta_v = the write's floor, and per profile the margin y_s^th - max(d + f) over x <= x_valid(d) (a level
    surface only where W1(d) >= 0) with, where a power law reaches y_s^th, its x_hit and whether that point is in
    J^-(P_c) (P2's points with x >= u_min^2 are in it at Delta_v = the floor; u_min taken at eta_s: x_valid(d) >=
    max(x_hit, u_min(eta_s)^2)); x_hit = 0.0 means already past y_s^th at x = 1e-14, the grid's floor."""
    s = tb(e)
    ys = s["y_s"]
    yst, W1 = SF._ystar(s)
    eta_s = eta_of(e, ys * 1.0001)
    u_min_s = 4 * math.sqrt(2) * math.sin(eta_s / 4)**2 / dv
    cand = {"zero": 0.0, "y_star": yst, "band_mid": None if yst is None else (yst + s["y_end"]) / 2, "tenth": 0.1 * ys}
    w = SF.wec_window(s)
    if w["d_plus"] is not None:                    # 0.0 at ell = inf is a row (the flat limit), not a skip
        cand["d_plus"] = w["d_plus"]
    rows = {}
    for k, dep in cand.items():
        if dep is None:
            continue
        et = eta_of(e, dep)
        xv = SF.x_valid(s, dep)
        margins, hits, ccrit = {}, {}, {}
        for kind in SLAB_KINDS:
            mg, xh = _profile_margin(s, dep, xv, kind, W1, ys)
            margins[_kname(kind)] = mg
            if xh is not None:                     # P2 is deeper than y_s^th on [x_hit, x_valid(d)]; that part
                hits[_kname(kind)] = {"x_hit": xh, "in_cone": xv >= max(xh, u_min_s**2)}   # meets J^-: x >= u_min^2
            if kind[0] == "pow":                   # f = c x^lam rises with x: the margin holds iff c < c*
                ccrit[_kname(kind)] = (ys - dep) / xv**kind[1]
        rows[k] = {"depth": dep, "eta": et, "eta_over_eta_s": et / eta_s, "K_ratio": k_ratio(e, dep),
                   "u_min": 4 * math.sqrt(2) * math.sin(et / 4)**2 / dv, "x_valid": xv,
                   "W1": float(W1(max(dep, 1e-9))), "margins": margins, "hits": hits, "c_crit": ccrit}
    return rows


def slab_window(e):
    """X9: S15's positive-energy window [d_+, top] and lam_max at d_+ (sim2_facing.wec_window)."""
    w = SF.wec_window(tb(e))
    return {"d_plus": w["d_plus"], "top": w["top"], "lam_max": w.get("lam_max")}


def crosser_frame(e, xs=(1e-4, 1e-8, 1e-12)):
    """X9 (C11b): P2's surface stress at the coinciding depth (0) as the crosser at P_c reads it, along the null
    direction n = -d_u, regular across u = 0: n = (2 alpha/u)(e_0 - e_1) in the static frame (deduced from x = u^2,
    t = v + 2 sqrt2/u), so S(n, n) = 4 alpha^2 (rho + p_r)/x, with rho + p_r from sim2_facing.piece_stress.  Per profile:
    the values along x -> 0 and their growth (last/first); and the static orthonormal frame's rho, rho + p_r and
    rho + p_th at the same points (all finite: the divergence is along the regular null frame only)."""
    s = tb(e)
    _, W1 = SF._ystar(s)
    g2 = SF._smooth_g2(s, 0.0, W1)
    out = {}
    for kind in SF.CO_KINDS:
        vals, srho, snr, snt = [], [], [], []
        for xv in xs:
            st = SF.piece_stress(s, 0.0, xv, kind, g2)
            al = float(s["sol"].sol(SF._profile(kind, xv, g2)[0])[0])
            vals.append(4 * al * al * st["nec_r"] / xv)
            srho.append(st["rho"])
            snr.append(st["nec_r"])
            snt.append(st["nec_th"])
        out[SF._kind_name(kind)] = {"values": vals, "growth": vals[-1] / vals[0], "static_rho": srho,
                                    "static_nec_r": snr, "static_nec_th": snt}
    return out


# ----------------------------------------------------------------------------------------------------- X10 E-Q
ANEC_CLOSED = (sp.sqrt(3) * sp.log(2 + sp.sqrt(3)) - 6) / (36 * sp.pi)


def plane_null_energy(data="eq17"):
    """X10 (b): on the plane's metric -F dt^2 + dr^2/H + r^2 dOmega^2, rho + p_r = (G^r_r - G^t_t)/(8 pi) and the
    integrated null energy along the ingoing radial null ray (energy 1), int (rho + p_r)/sqrt(F H) dr, from r = 2m to
    infinity, numerically (mpmath, 30 digits) and exactly (sympy, after r = 2 + s^2), with the exact value's distance
    from the closed form (sqrt3 ln(2 + sqrt3) - 6)/(36 pi) at 60 digits.  eq17: Bronnikov-Kim's eq. (17) at r0 = 2m;
    schw: Schwarzschild (the control, exactly zero).  g_tt at the throat is returned too (X10 (d))."""
    r = sp.Symbol("r", positive=True)
    t, th, ph = sp.symbols("t theta phi", real=True)
    F, H = (SF.B4._eq17 if data == "eq17" else SF.B4._schwarzschild)(r)
    g = [-F, 1 / H, r**2, r**2 * sp.sin(th)**2]
    R, gi, _ = SF._ricci_diag(g, [t, r, th, ph])
    Rt, Rr = sp.simplify(gi[0] * R(0, 0)), sp.simplify(gi[1] * R(1, 1))
    Rs = sp.simplify(sum(gi[i] * R(i, i) for i in range(4)))
    nec = sp.factor(sp.simplify((Rr - Rt) / (8 * sp.pi)))               # G^r_r - G^t_t = R^r_r - R^t_t
    bk18 = -(r - 2) * (2 - sp.Rational(3, 2)) / (r**2 * (r - sp.Rational(3, 2))**2)
    integrand = sp.simplify(nec / sp.sqrt(F * H))
    f = sp.lambdify(r, integrand, "mpmath")
    import mpmath as mp
    mp.mp.dps = 30
    val = mp.quad(f, [2, 2.001, 2.1, 3, 10, mp.inf]) if data == "eq17" else mp.quad(f, [2.5, 10, mp.inf])
    s = sp.Symbol("s", positive=True)
    gs = sp.simplify(integrand.subs(r, 2 + s**2) * 2 * s)
    exact = sp.integrate(gs, (s, 0, sp.oo))
    diff = complex(sp.N(exact - ANEC_CLOSED, 60))
    return {"R": Rs, "nec": nec, "bk18_ratio": sp.simplify(nec * 8 * sp.pi / bk18) if data == "eq17" else None,
            "anec": float(val), "integrand_s": gs, "exact_minus_closed": abs(diff), "g_tt_at_throat": sp.simplify(-F.subs(r, 2))}


def data_fixes_bulk(dp=1e-3):
    """X10 (c): the throat bulk is the solution of an initial-value problem in y from the plane's data; a change of the
    data (matter on the plane) moves y_s.  p(0) = -e -+ dp at ell = 8m, with q(0) solved from the yy constraint
    p^2 + q^2 + 4pq - 6e^2 = 0 at alpha = beta = 1 (the root through -e: q0 = -2 p0 - sqrt(3 p0^2 + 6 e^2)); with
    DATA_CONSTRAINED False (C13's mutation) q(0) is held at -e, off the constraint surface (the first version's data).
    Returns y_s (alpha = 1e-9) for the vacuum data and the two perturbations, the q0 used, and the largest relative
    constraint residual along [0, 0.95 y_s] over the three runs."""
    ef = 1 / 8

    def run(p0):
        q0 = -2 * p0 - math.sqrt(3 * p0 * p0 + 6 * ef * ef) if DATA_CONSTRAINED else -ef

        def rhs(y, u):
            return SF.throat_rhs(y, list(u) + [0.0] * 6, ef)[:4]

        def end(y, u):
            return u[0] - 1e-9
        end.terminal = True
        sol = solve_ivp(rhs, [0, 12], [1.0, 1.0, p0, q0], method="DOP853", rtol=1e-12, atol=1e-15, events=[end],
                        max_step=0.005, dense_output=True)
        ys = float(sol.t[-1])
        al, be, p, q = sol.sol(np.linspace(0, 0.95 * ys, 2000))
        cons = _constraint(p, q, al, be, ef)
        scale = p * p + q * q + 1 / (4 * al * al) + 1 / (4 * be * be) + 6 * ef * ef
        return ys, q0, float(np.max(np.abs(cons) / scale))
    v0, mi, pl = run(-ef), run(-ef - dp), run(-ef + dp)
    return {"vacuum": v0[0], "minus": mi[0], "plus": pl[0], "q0_minus": mi[1], "q0_plus": pl[1],
            "cons_max": max(v0[2], mi[2], pl[2])}


# ------------------------------------------------------------------------------- X11-X25: the two owners, by path
# The [FREE] sections X13, X14, X17 (stationary half) and X18 are computed by two owners, loaded here by path and never
# copied: their own selftest() is called (C15-C19, C26-C31) and their own compute output is read (X13-X18 rows, C35a).
OWNER_PATHS = {"epass_pairing": os.path.join(HERE, "epass_pairing.py"),
               "epass_frames": os.path.join(HERE, "epass_frames.py")}
OWNER_CHECK_IDS = {   # the owners' checks as built and verified (an owner that drops one fails C15-C19 / C26-C31)
    "epass_pairing": ("C15", "C16", "C17", "C18", "C18s", "C18b", "C18c", "C19", "C19b", "C19c", "CG"),
    "epass_frames": ("C26a", "C26b", "C26c", "C26d", "C26e", "C30a", "C30b", "C30c", "C30d", "C31a", "C31b", "C31c",
                     "C31d", "G1", "G2", "G3")}
OWNER_SECTIONS = {"epass_pairing": ("X13", "X14"), "epass_frames": ("X17", "X18")}
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
SPEC_FREE = ("X13", "X14", "X17", "X18")          # the spec's [FREE] sections (X17: its stationary half)
SPEC_PLANE = ("X11", "X12", "X15", "X16", "X19", "X20", "X21", "X22", "X23", "X24")   # the spec's [PLANE] sections
SPEC_TAG = {"X13": "[FREE]", "X14": "[FREE for sheets]", "X17": "[FREE stationary; PLANE changing]",
            "X18": "[FREE given an AdS2 throat]"}
DEFERRED = {
    "X11": "Lemma 0's far-time half: the README's own pre-crossing events on end 1 (r = 2.02-2.2m) on the plane's "
           "static clock, from stage 5's owner columns; until it is built, X8's refutation of the route with no second "
           "sheet rests on its advanced-time half (X7) and the static-clock half stays OPEN (X8)",
    "X12": "footprint, ceiling, Lemma X (excision) and the far gate, from the owner bank's columns on our plane",
    "X15": "Lemmas L and Q and the absorbing band: Lemma L is the brane ledger of a changing crossing (SMS) with eq. "
           "(17)'s data on our plane, Lemma Q is stated at our plane's law, and the band (d_beta, d_+, q(d_+)) is S15's "
           "slab; X17's changing half (Lemma L's coefficient times P1's; the spec, a design document not verified, gives "
           "5.912 at 32m tending to 5: not computed here) waits with it",
    "X16": "the crossable class at the horizon (S7's profiles on the throat bulk at our plane; H-CROSSABLE-HORIZON, the "
           "board's, put to M)",
    "X19": "three phases of a coupling, across eq. (17)'s family at r0 = 2m",
    "X20": "the classical placements of E-Q (the plane's data, the conformal layer, the Bronnikov-Kim gap)",
    "X21": "the transverse reading and the two pairs for 177 and 178 (Lemma S's own pair: its cancellation is [FREE], "
           "X13 (a)-(b); its [PLANE] ledger and tensor are X13 (d))",
    "X22": "the cap: the README held on P1 at the throat (conditional on H-README-AT-THE-THROAT, the board's; a held "
           "configuration, not a passage; the spec builds it after the core)",
    "X23": "Kaus-Reall reproduced (support for the [PLANE] rows)",
    "X24": "the between-universes column for phase 3 (Lemma S's law-independence, [FREE], already holds there: X13)",
}
DEFER_WHY = ("each takes eq. (17) as a plane's own metric -- the board's configuration, which 179/180 "
             "(H-CORRIDOR-IN-BULK, M's) re-reads and clause (G), SEATED on M's \"Seat both\" (187 (3)), keeps only as a "
             "plane's possible reading of the corridor's mouth (H-PLANE-READS-MOUTH, the board's, OPEN); 181 puts the "
             "bulk balance first; under 184 a matter-free plane is a limit only.  The spec recommends building them only "
             "after the 179 re-read decides whether the plane configuration stays as the board's comparison case.  That "
             "re-read is not made.")
# the owners' rows carried into X13-X18 (owner, path into its output, section)
PAIRING_ROWS = tuple(("epass_pairing", ("results", k), "X13") for k in (
    "X13b_bulk", "X13b_premise", "X13b_label_note", "X13a_sheet", "X13a_scope", "X13a_statement", "X13a_held_stress",
    "X13a_readme_flux", "X13c_weyl", "X13c_eq17", "X13d_pair", "X13d_pair_tensor", "X13d_readings", "X13_limit",
    "E_PASS_status")) + tuple(("epass_pairing", ("results", k), "X14") for k in (
    "X14_tangent", "X14_numeric", "X14_consequence", "X14_withdrawn", "C15_gauss", "C16_transport"))
FRAMES_ROWS = tuple(("epass_frames", ("X17", k), "X17") for k in (
    "readme_flux_P1", "stationary_demand", "demand_si", "reads_beside", "answer_158_4", "changing_half")) + tuple(
    ("epass_frames", ("X18",) + k, "X18") for k in (
        ("generator_classes",), ("induced_metric",), ("poincare_map",), ("throat_generator",), ("embedding_generator",),
        ("ends_map",), ("ads2_family",), ("lemma_p", "i_delta_stress"), ("lemma_p", "ii_weyl_fluid"),
        ("lemma_p", "iii_charge_flip"), ("deduced", "s15_delta_stress"), ("deduced", "s15_along_the_approach"),
        ("deduced", "board_176_sentence"), ("deduced", "extremal_member"), ("deduced", "end2_identification"),
        ("deduced", "positive_in_own_frame")))

# X25, restricted to what is now computed: every source is a computed section (X1-X10, the owners' X13, X14, X17's
# stationary half, X18) or sim2_facing's S15 (computed and verified there); a cell that needs a deferred section names it.
X25_COMPUTED = tuple(f"X{i}" for i in range(1, 11)) + SPEC_FREE + ("S15",)
X25_GATES = {"G1": "REGULAR PAST (174 (1))",
             "G2": "POSITIVE (139 (2), in its own frame: H-POSITIVE-ON-P2, H-POSITIVE-IN-OWN-FRAME, the board's)",
             "G3": "NEC (117/120; 183: net along each light ray)",
             "G4": "CROSSES AT FIXED SIZE (143 A, 132, 162, 163: Lemma S, and Lemma K for a net-flux crossing)"}
X25_ROWS = (
    {"row": "R0", "config": "no second sheet, README on P1", "tag": "[PLANE]",
     "G1": "fails (X7-X8: within O(x) every claimed layer lies in J^-(P_c) below the write's floor); the far-time half "
           "(X11) DEFERRED",
     "G2": "-", "G3": "-",
     "G4": "a partner at least as large as the README along each generator, exact under 183 (X13); no classical, "
           "NEC-obeying matter supplies one (deduced)",
     "verdict": "the route with no second sheet is REFUTED on X8's conjunction (G1 alone suffices); E-PASS as a whole "
                "is not", "sources": ("X7", "X8", "X13"), "deferred_parts": ("X11",)},
    {"row": "R2-R3", "config": "position 2's piece shallower than d_+", "tag": "[PLANE]",
     "G1": "as R4 near the throat (X9)", "G2": "fails (S15: outside the positive-energy window [d_+, top]; X9)",
     "G3": "holds on the samples (S15)", "G4": "as R4",
     "verdict": "fails G2; the band's split at d_beta is X15's, DEFERRED", "sources": ("X9", "S15"),
     "deferred_parts": ("X15",)},
    {"row": "R4", "config": "position 2's piece in [d_+, top] (ell > 27.07m only)", "tag": "[PLANE]",
     "G1": "holds near the throat for the profiles X9 passes; the cover and the far field OPEN (E-G, E-FAR)",
     "G2": "holds (S15)", "G3": "holds classically (S15)",
     "G4": "stationary: the exact pair (X13), with no classical partner (deduced), OPEN through 177/183 as "
           "H-PARTNER-IS-THE-COUPLING (the supply not computed); changing: a five-dimensional event (X14), its "
           "coefficient X15's, DEFERRED",
     "verdict": "no classical crossing; OPEN only as 177's partner or as E-NS", "sources": ("X9", "S15", "X13", "X14"),
     "deferred_parts": ("X15",)},
    {"row": "R5", "config": "coinciding, depth -> 0", "tag": "[PLANE]",
     "G1": "the slab pinches along the horizon line through P_c, and power-law P2 stress diverges along the regular "
           "null frame (X9, C11b)",
     "G2": "fails at every finite ell (S15: rho_m -> -2 sigma_RS; X10 (e)); at the limit, never reached, -sigma_RS is a "
           "delta-stress, the same in every tangent frame (X18, Lemma P (i))",
     "G3": "marginal (X10 (e))", "G4": "as R0's Lemma S (X13)",
     "verdict": "fails G2 within one universe at finite ell (174 (3)); at ell = inf a limit (flat, no RS localisation)",
     "sources": ("X9", "X10", "S15", "X18", "X13"), "deferred_parts": ()},
    {"row": "R6", "config": "classical E-Q", "tag": "[FREE] (the Weyl term); [PLANE] (X10 (c)-(d))",
     "G1": "-", "G2": "-", "G3": "-",
     "G4": "on the unsheared horizon of X13 (b)'s family the bulk Weyl term gives nothing along the generators, "
           "E(xi,xi) = 0 (X13 (c); a sheared horizon is not computed); a static symmetric coupling "
           "that leaves the plane's data unchanged changes nothing, and a horizonless link removes the horizon against "
           "132 (X10 (c)-(d)); the conformal layer and the BK gap are X20's, DEFERRED",
     "verdict": "pays nothing along the generators", "sources": ("X10", "X13"), "deferred_parts": ("X20",)},
    {"row": "R7", "config": "coupled ends, quantum (177)", "tag": "[FREE]; [PLANE] for the pair tensor",
     "G1": "-", "G2": "-", "G3": "admitted (183; H-PARTNER-IS-THE-COUPLING, the board's)",
     "G4": "a negative partner along each generator at least as large as the README, exact under 183, sheet or bulk "
           "form (X13); at [PLANE], among null-dust partners with no held momentum flux, only the README's exact "
           "reverse, with a zero total stress (X13 (d)); GJW's net-negative prerequisite stands against Lemma S's "
           "zero total (X17): a tension, OPEN; given kappa = 0 the corridor is the extremal, parabolic member (X18)",
     "verdict": "OPEN: the demand exact, the supply beyond the board's instruments", "sources": ("X13", "X17", "X18"),
     "deferred_parts": ()},
    {"row": "R8", "config": "changing corridor (E-NS; 152 (2), 160)", "tag": "[FREE] (Lemma K); [PLANE] (Lemma L)",
     "G1": "open", "G2": "-", "G3": "-",
     "G4": "needs expansion (theta != 0, against 162 as read through H-FIXED-SIZE-AS-THETA-ZERO) or a crease or "
           "separation of the bulk horizon at the sheet (X14); its number, Lemma L's, is X15's, DEFERRED",
     "verdict": "OPEN, to phase 2b-ii", "sources": ("X13", "X14"), "deferred_parts": ("X15",)},
    {"row": "R9", "config": "between universes", "tag": "[FREE] (Lemma S)",
     "G1": "phase 3", "G2": "-", "G3": "-",
     "G4": "Lemma S is law-independent, so the pair is still demanded (X13); X24 DEFERRED",
     "verdict": "handed to phase 3", "sources": ("X13",), "deferred_parts": ("X24",)},
)
X25_LEFT_OUT = {"R1": "the cap (X22)", "R2-R3 split at d_beta": "the band (X15)", "far gate": "X12"}
X25_COMBINED = (
    "Within one universe at our tension no configuration computed here carries the README across the corridor "
    "object's horizon with a regular past through the write.  Position 2's near-coinciding piece regularises the "
    "crossing's past near the throat (X9) and does not pay the crossing (X13).  A horizon that keeps its size takes a "
    "partner at least as large as the README along each generator, exactly as large only if unsheared, and under 183 "
    "exactly as large (X13).  A net-flux crossing is a five-dimensional event (X14).  The classical Weyl term pays "
    "nothing on the unsheared horizon computed; quantum E-Q could supply only the partner (exact under 183), which the "
    "board cannot compute, and GJW's net-negative prerequisite stands against that zero total (OPEN).")
X25_EXTRA = ()      # C35b's mutation: a row added to X25's table
X25_PLANT = ""      # C35b's mutation: a sentence planted in X25's combined answer

# C35a: every value the X11-X25 docstring quotes from an owner, as (id, owner, path into the owner's output, kind,
# expected, the text as the docstring prints it).  kinds: str, true, false, zero, sig (the owner's number rounded to
# the quoted significant digits equals the quote), num, prefix, contains, md5 (prefix of the owner file's md5).
_PR, _FX = ("results",), ("X17",)
_GC = ("X18", "generator_classes", "rows")
_LP = ("X18", "lemma_p")
DOC_QUOTES = (
    ("p_md5", "epass_pairing", (), "md5", "152621fa", "md5 152621fa"),
    ("p_bulk_deg", "epass_pairing", _PR + ("X13b_bulk", "cases", "degenerate", "R_xixi"), "str", "0",
     "R(xi,xi)|_{u=0} = 0 on the stationary members"),
    ("p_bulk_nondeg", "epass_pairing", _PR + ("X13b_bulk", "cases", "nondegenerate", "R_xixi"), "str", "0",
     "R(xi,xi)|_{u=0} = 0 on the stationary members"),
    ("p_bulk_nullkept", "epass_pairing", _PR + ("X13b_bulk", "cases", "degenerate", "R_xixi_nonstationary_null_kept"),
     "str", "0", "on a non-stationary member that keeps u = 0 null"),
    ("p_shear_deg", "epass_pairing", _PR + ("X13b_premise", "cases", "degenerate", "shear_fixed_volume",
                                            "R_xixi_witness"), "sig", "-0.014138938637006316", "-0.014138938637006316"),
    ("p_shear_nondeg", "epass_pairing", _PR + ("X13b_premise", "cases", "nondegenerate", "shear_fixed_volume",
                                               "R_xixi_witness"), "sig", "-0.014138938637006316",
     "-0.014138938637006316"),
    ("p_shear_theta", "epass_pairing", _PR + ("X13b_premise", "cases", "degenerate", "shear_fixed_volume", "theta"),
     "str", "0", "(theta = 0) R(xi,xi) = -sigma^2 <= 0"),
    ("p_raych", "epass_pairing", _PR + ("X13b_premise", "cases", "degenerate", "section_growth",
                                        "raychaudhuri_residual"), "str", "0",
     "the Raychaudhuri route agrees with the Riemann route on every variant"),
    ("p_sheet_deg", "epass_pairing", _PR + ("X13a_sheet", "cases", "throat_degenerate", "K_xixi"), "str", "0",
     "K(xi,xi)|_H = 0 for sheets y = F(u)"),
    ("p_sheet_nondeg", "epass_pairing", _PR + ("X13a_sheet", "cases", "general_nondegenerate", "K_xixi"), "str", "0",
     "K(xi,xi)|_H = 0 for sheets y = F(u)"),
    ("p_sheet_growth", "epass_pairing", _PR + ("X13a_scope", "K_xixi", "throat_nondegenerate_section_growth"), "str",
     "0", "on a horizon whose section grows"),
    ("p_tilt_nondeg", "epass_pairing", _PR + ("X13a_scope", "K_xixi", "throat_nondegenerate_tilted_sheet"), "sig",
     "0.01166", "witness 0.01166 where kappa != 0"),
    ("p_tilt_deg", "epass_pairing", _PR + ("X13a_scope", "K_xixi", "throat_degenerate_tilted_sheet"), "zero", 0,
     "and 0 where kappa = 0"),
    ("p_held_tau", "epass_pairing", _PR + ("X13a_held_stress", "tau_xixi_on_H"), "str", "0",
     "tau(xi,xi) = pi(xi,xi) = 0 on H"),
    ("p_held_pi", "epass_pairing", _PR + ("X13a_held_stress", "pi_xixi_on_H"), "str", "0",
     "tau(xi,xi) = pi(xi,xi) = 0 on H"),
    ("p_weyl_Et", "epass_pairing", _PR + ("X13c_weyl", "cases", "degenerate", "stationary", "Etilde_xixi"), "str", "0",
     "E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0"),
    ("p_weyl_E", "epass_pairing", _PR + ("X13c_weyl", "cases", "nondegenerate", "nonstationary_null_kept", "E_xixi"),
     "str", "0", "E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0"),
    ("p_R4", "epass_pairing", _PR + ("X13c_eq17", "R4_xixi_on_H"), "str", "0", "R4(xi,xi) = 0 at r = 2m"),
    ("p_readme", "epass_pairing", _PR + ("X13d_pair", "readme_member"), "str", "2", "T^R(xi,xi) = 2 per mu"),
    ("p_partner", "epass_pairing", _PR + ("X13d_pair", "partner_member"), "str", "-2", "partner -2"),
    ("p_net", "epass_pairing", _PR + ("X13d_pair", "net"), "str", "0", "net 0 BY CONSTRUCTION"),
    ("p_lxi", "epass_pairing", _PR + ("X13a_readme_flux", "l_dot_xi"), "str", "-sqrt(2)", "(l.xi = -sqrt2)"),
    ("p_pi_sms", "epass_pairing", _PR + ("X13d_pair_tensor", "pi_xixi_sms20"), "str", "-b**2*mu**2/2",
     "pi(xi,xi) = -b^2 mu^2/2 by two routes"),
    ("p_pi_dust", "epass_pairing", _PR + ("X13d_pair_tensor", "pi_xixi_nulldust"), "str", "-b**2*mu**2/2",
     "pi(xi,xi) = -b^2 mu^2/2 by two routes"),
    ("p_b0", "epass_pairing", _PR + ("X13d_pair_tensor", "pair_is_zero_at_b0"), "true", True,
     "the pair's total stress tensor is then ZERO"),
    ("p_b", "epass_pairing", _PR + ("X13d_pair_tensor", "pair_is_zero_at_b"), "false", False,
     "the only admitted null partner is the README's exact reverse"),
    ("p_status", "epass_pairing", _PR + ("E_PASS_status", "label"), "str", "OPEN", "OPEN through 177/183"),
    ("p_K_conn", "epass_pairing", _PR + ("X14_tangent", "ydd_connection"), "str", "K_vv", "y'' = K_vv by two routes"),
    ("p_K_lie", "epass_pairing", _PR + ("X14_tangent", "K_vv_lie"), "str", "K_vv", "y'' = K_vv by two routes"),
    ("p_K_zero", "epass_pairing", _PR + ("X14_numeric", "cases", "S_vv=0", "stays_on_sheet"), "true", True,
     "S_vv = 0 stays on the sheet to 1e-12"),
    ("p_K_plus", "epass_pairing", _PR + ("X14_numeric", "cases", "S_vv=+1", "y_end"), "sig", "-0.5572",
     "(y_end = -0.5572, leading order -1/2)"),
    ("p_K_plus_lo", "epass_pairing", _PR + ("X14_numeric", "cases", "S_vv=+1", "leading_order_y_end"), "num", -0.5,
     "leading order -1/2"),
    ("p_K_minus", "epass_pairing", _PR + ("X14_numeric", "cases", "S_vv=-1", "y_end"), "sig", "0.4832",
     "(y_end = 0.4832)"),
    ("p_K_minus_side", "epass_pairing", _PR + ("X14_numeric", "cases", "S_vv=-1", "stays_kept_side"), "true", True,
     "S_vv = -1 leaves the sheet into the bulk"),
    ("f_md5", "epass_frames", (), "md5", "97bbfff9", "md5 97bbfff9"),
    ("f_flux", "epass_frames", _FX + ("readme_flux_P1", "value"), "str", "1/(2*m)",
     "kappa_4^2 int T_vv dv = 1/(2m) per generator"),
    ("f_rh", "epass_frames", _FX + ("readme_flux_P1", "r_h_over_m"), "str", "2",
     "r_h = 2m with surface gravity kappa = 0"),
    ("f_kappa", "epass_frames", _FX + ("readme_flux_P1", "kappa_x_m"), "str", "0",
     "r_h = 2m with surface gravity kappa = 0"),
    ("f_kappa_ctl", "epass_frames", _FX + ("readme_flux_P1", "kappa_x_m_schwarzschild_control"), "str", "1/4",
     "(Schwarzschild control 1/4; v affine)"),
    ("f_partner_P1", "epass_frames", _FX + ("stationary_demand", "sheet_form", "partner_kappa4sq_int_Tvv_P1"), "str",
     "-1/(2*m)", "so the partner's is -1/(2m)"),
    ("f_gated", "epass_frames", _FX + ("stationary_demand", "gated_on_owner_zero"), "true", True,
     "gated on the Lemma S owner's zeros"),
    ("f_net", "epass_frames", _FX + ("stationary_demand", "pair_net_per_generator"), "str", "0",
     "The pair's net per generator is the owner's zero"),
    ("f_E_N", "epass_frames", _FX + ("demand_si", "rows", "N_example", "E_J"), "sig", "2.40588e16",
     "E = 2.40588e16 J"),
    ("f_m_N", "epass_frames", _FX + ("demand_si", "rows", "N_example", "m_geometric_m"), "sig", "1.98791e-28",
     "m = G E/c^4 = 1.98791e-28 m"),
    ("f_inv_N", "epass_frames", _FX + ("demand_si", "rows", "N_example", "kappa4sq_int_Tvv_per_m"), "sig", "2.51521e27",
     "1/(2m) = 2.51521e27 m^-1"),
    ("f_E_155", "epass_frames", _FX + ("demand_si", "rows", "item155", "E_J"), "sig", "3.8e22",
     "item 155's E = 3.8e22 J"),
    ("f_m_155", "epass_frames", _FX + ("demand_si", "rows", "item155", "m_geometric_m"), "sig", "3.13983e-22",
     "m = 3.13983e-22 m"),
    ("f_inv_155", "epass_frames", _FX + ("demand_si", "rows", "item155", "kappa4sq_int_Tvv_per_m"), "sig", "1.59244e21",
     "1/(2m) = 1.59244e21 m^-1"),
    ("f_gexp", "epass_frames", _FX + ("demand_si", "G_exponent_of_E"), "str", "-1/2", "E ~ G^(-1/2)"),
    ("f_ur_N", "epass_frames", _FX + ("demand_si", "rows", "N_example", "u_r_m"), "sig", "1.12e-5",
     "u_r(m) = 1.12e-5 at the example README"),
    ("f_ur_155", "epass_frames", _FX + ("demand_si", "rows", "item155", "u_r_m"), "sig", "2.25e-5",
     "2.25e-5 at the fixed E"),
    ("f_gjw2_page", "epass_frames", _FX + ("reads_beside", "reads", "id=GJW-2", "page"), "prefix", "PDF p.2 ",
     'PDF p.2, "Violation of the averaged null energy condition'),
    ("f_gjw2", "epass_frames", _FX + ("reads_beside", "reads", "id=GJW-2", "quote"), "contains",
     "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes",
     "Violation of the averaged null energy condition (ANEC) is a prerequisite for all traversable wormholes"),
    ("f_gjw4b_page", "epass_frames", _FX + ("reads_beside", "reads", "id=GJW-4b", "page"), "prefix", "PDF p.4 ",
     'PDF p.4, "T_UU in the modified state'),
    ("f_gjw4b", "epass_frames", _FX + ("reads_beside", "reads", "id=GJW-4b", "quote"), "contains",
     "T_UU in the modified state along U > 0 will exactly cancel that along U < 0",
     "T_UU in the modified state along U > 0 will exactly cancel that along U < 0"),
    ("f_msy_page", "epass_frames", _FX + ("reads_beside", "reads", "id=MSY-13", "page"), "prefix", "PDF p.13 ",
     'PDF p.13, "we cannot send more information'),
    ("f_msy", "epass_frames", _FX + ("reads_beside", "reads", "id=MSY-13", "quote"), "contains",
     "we cannot send more information through the wormhole than we transferred in order to set up the OO interaction",
     "we cannot send more information through the wormhole than we transferred in order to set up the OO interaction"),
    ("f_J", "epass_frames", _GC + ("J", "class_matrix"), "str", "elliptic", "d_T is elliptic, components (1, 1)"),
    ("f_J0", "epass_frames", _GC + ("J", "component_at_sigma0"), "str", "1", "d_T is elliptic, components (1, 1)"),
    ("f_Jpi", "epass_frames", _GC + ("J", "component_at_sigmapi"), "str", "1", "d_T is elliptic, components (1, 1)"),
    ("f_Jnorm", "epass_frames", _GC + ("J", "xi_dot_xi"), "str", "-1/sin(sigma)**2",
     "with xi.xi = -1/sin^2 sigma < 0"),
    ("f_B", "epass_frames", _GC + ("B_origin", "class_matrix"), "str", "hyperbolic",
     "B_origin hyperbolic, (-cos T, cos T)"),
    ("f_B0", "epass_frames", _GC + ("B_origin", "component_at_sigma0"), "str", "-cos(T)",
     "B_origin hyperbolic, (-cos T, cos T)"),
    ("f_Bpi", "epass_frames", _GC + ("B_origin", "component_at_sigmapi"), "str", "cos(T)",
     "B_origin hyperbolic, (-cos T, cos T)"),
    ("f_K", "epass_frames", _GC + ("K", "class_matrix"), "str", "hyperbolic", "K hyperbolic, (sin T, -sin T)"),
    ("f_K0", "epass_frames", _GC + ("K", "component_at_sigma0"), "str", "sin(T)", "K hyperbolic, (sin T, -sin T)"),
    ("f_Kpi", "epass_frames", _GC + ("K", "component_at_sigmapi"), "str", "-sin(T)", "K hyperbolic, (sin T, -sin T)"),
    ("f_JpK", "epass_frames", _GC + ("J+K", "class_matrix"), "str", "parabolic", "J + K and J - K parabolic"),
    ("f_JmK", "epass_frames", _GC + ("J-K", "class_matrix"), "str", "parabolic", "J + K and J - K parabolic"),
    ("f_JmB", "epass_frames", _GC + ("J-B_origin", "class_matrix"), "str", "parabolic",
     "J - B_origin (the Poincare d_t) parabolic, (1 + cos T, 1 - cos T)"),
    ("f_JmB0", "epass_frames", _GC + ("J-B_origin", "component_at_sigma0"), "str", "cos(T) + 1",
     "J - B_origin (the Poincare d_t) parabolic, (1 + cos T, 1 - cos T)"),
    ("f_JmBpi", "epass_frames", _GC + ("J-B_origin", "component_at_sigmapi"), "str", "1 - cos(T)",
     "J - B_origin (the Poincare d_t) parabolic, (1 + cos T, 1 - cos T)"),
    ("f_mq21", "epass_frames", ("X18", "induced_metric", "equals_MQ_2_1"), "true", True,
     "its induced metric equals Maldacena-Qi (2.1), READ PDF p.5"),
    ("f_poincare", "epass_frames", ("X18", "poincare_map", "is_poincare_radius2"), "true", True,
     "x = 8/z^2 gives 4(-dt^2 + dz^2)/z^2 with z = 2 sqrt2/u"),
    ("f_zofu", "epass_frames", ("X18", "poincare_map", "z_of_u"), "str", "['2*sqrt(2)/u']",
     "x = 8/z^2 gives 4(-dt^2 + dz^2)/z^2 with z = 2 sqrt2/u"),
    ("f_push", "epass_frames", ("X18", "embedding_generator", "equals_J_minus_B_origin"), "true", True,
     "the throat's d_v pushes forward to J - B_origin"),
    ("f_pushY", "epass_frames", ("X18", "embedding_generator", "pushforward", "dv_Y_equals_M_Y"), "true", True,
     "the throat's d_v pushes forward to J - B_origin"),
    ("f_throatQ", "epass_frames", ("X18", "throat_generator", "Q"), "str", "0", "the throat's d_v has Q = 0, parabolic"),
    ("f_throatC", "epass_frames", ("X18", "throat_generator", "class"), "str", "parabolic",
     "the throat's d_v has Q = 0, parabolic"),
    ("f_smooth", "epass_frames", ("X18", "ends_map", "smooth_through_u0"), "true", True,
     "the ingoing chart is smooth through u = 0"),
    ("f_end1", "epass_frames", ("X18", "ends_map", "end1_boundary"), "str", "sigma=0", "end 1 (u > 0) on sigma=0"),
    ("f_end2", "epass_frames", ("X18", "ends_map", "end2_boundary"), "str", "sigma=pi", "end 2 (u < 0) on sigma=pi"),
    ("f_u0", "epass_frames", ("X18", "ends_map", "u0_is_patch1_future_horizon"), "true", True,
     "u = 0 patch 1's future and patch 2's past horizon"),
    ("f_famR", "epass_frames", ("X18", "ads2_family", "R"), "str", "-1/2", "R = -1/2 and Q = delta/8"),
    ("f_famQ", "epass_frames", ("X18", "ads2_family", "Q_general"), "str", "delta/8", "R = -1/2 and Q = delta/8"),
    ("f_fam_neg", "epass_frames", ("X18", "ads2_family", "classes", "-1/9"), "str", "hyperbolic",
     "delta < 0 hyperbolic"),
    ("f_fam_zero", "epass_frames", ("X18", "ads2_family", "classes", "0"), "str", "parabolic", "delta = 0 parabolic"),
    ("f_fam_pos", "epass_frames", ("X18", "ads2_family", "classes", "1/9"), "str", "elliptic", "delta > 0 elliptic"),
    ("f_lp1", "epass_frames", _LP + ("i_delta_stress", "rows", "1", "all_equal_minus_s"), "true", True,
     "reads -s for every observer (1000 exact rational Lorentz transformations; s = 1, -1, 3/7)"),
    ("f_lp1m", "epass_frames", _LP + ("i_delta_stress", "rows", "-1", "all_equal_minus_s"), "true", True,
     "reads -s for every observer (1000 exact rational Lorentz transformations; s = 1, -1, 3/7)"),
    ("f_lp37", "epass_frames", _LP + ("i_delta_stress", "rows", "3/7", "all_equal_minus_s"), "true", True,
     "reads -s for every observer (1000 exact rational Lorentz transformations; s = 1, -1, 3/7)"),
    ("f_rho", "epass_frames", _LP + ("ii_weyl_fluid", "fluid", "8pi_rho"), "str", "1/81", "8 pi rho = 1/81"),
    ("f_nec", "epass_frames", _LP + ("ii_weyl_fluid", "fluid", "8pi_rho_plus_p_r"), "str", "-2/81",
     "8 pi (rho + p_r) = -2/81"),
    ("f_vstar", "epass_frames", _LP + ("ii_weyl_fluid", "v_star_is_one_over_sqrt3"), "true", True, "v* = 1/sqrt3"),
    ("f_rapid", "epass_frames", _LP + ("ii_weyl_fluid", "rapidity_star"), "sig", "0.658479", "rapidity 0.658479"),
    ("f_limit", "epass_frames", _LP + ("ii_weyl_fluid", "rho_prime_limit_v_to_1"), "str", "-oo",
     "tends to -oo as v -> 1"),
    ("f_necctl", "epass_frames", _LP + ("ii_weyl_fluid", "nec_control", "all_rho_prime_ge_rho"), "true", True,
     "NEC matter gives rho' >= rho (1000 exact rows)"),
    ("f_eps", "epass_frames", _LP + ("ii_weyl_fluid", "approach_counterpart", "rho_plus_p_over_sigma"), "str",
     "47/50000000", "bounded by 9.4e-7 sigma_RS"),
    ("f_g2v2", "epass_frames", _LP + ("ii_weyl_fluid", "approach_counterpart", "gamma2v2_float"), "sig", "1.0638e6",
     "gamma^2 v^2 = 1/eps = 1.0638e6"),
    ("f_g2v2_inv", "epass_frames", _LP + ("ii_weyl_fluid", "approach_counterpart", "gamma2v2_is_inv_eps"), "true", True,
     "gamma^2 v^2 = 1/eps = 1.0638e6"),
    ("f_flipB", "epass_frames", _LP + ("iii_charge_flip", "rows", "B_origin", "flips_at_all_samples"), "true", True,
     "the boundary Killing charge flips under B_origin only"),
    ("f_flipJ", "epass_frames", _LP + ("iii_charge_flip", "rows", "J", "flips_at_some_sample"), "false", False,
     "it does not flip under J, J + K, J - K or J - B_origin"),
    ("f_flipJpK", "epass_frames", _LP + ("iii_charge_flip", "rows", "J+K", "flips_at_some_sample"), "false", False,
     "it does not flip under J, J + K, J - K or J - B_origin"),
    ("f_flipJmK", "epass_frames", _LP + ("iii_charge_flip", "rows", "J-K", "flips_at_some_sample"), "false", False,
     "it does not flip under J, J + K, J - K or J - B_origin"),
    ("f_flipJmB", "epass_frames", _LP + ("iii_charge_flip", "rows", "J-B_origin", "flips_at_some_sample"), "false",
     False, "it does not flip under J, J + K, J - K or J - B_origin"),
    ("f_176", "epass_frames", ("X18", "deduced", "board_176_sentence", "verdict"), "prefix", "Not refuted as a whole",
     "so it is not refuted as a whole"),
    ("f_176_text", "epass_frames", ("X18", "deduced", "board_176_sentence", "board_sentence"), "contains",
     "position 2's -1 would be the partner's sign seen from our side",
     "position 2's -1 would be the partner's sign seen from our side"),
)
_OWN = {}


def owner_module(name):
    """lemmas/<name>.py loaded by path (never copied), once per path; FileNotFoundError when the file is absent."""
    path = OWNER_PATHS[name]
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    if path not in _OWN:
        _OWN[path] = _load(path, "passage_" + name)
    return _OWN[path]


def _md5(path):
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def _owner_ids(mod):
    return list(mod.CHECKS) if isinstance(mod.CHECKS, dict) else [row[0] for row in mod.CHECKS]


def _owner_lines(name, lines, ids):
    """Each owner check's PASS/FAIL as the owner's own selftest printed it (epass_pairing: 'C15   PASS  what';
    epass_frames: '[PASS] C26a what -- detail'); a check printed on no line is absent from the result."""
    got = {}
    for ln in lines:
        if name == "epass_pairing":
            m = re.match(r"^(\S+)\s+(PASS|FAIL)\s\s(.*)$", ln)
            cid, st, what = (m.group(1), m.group(2), m.group(3)) if m else (None, None, None)
        else:
            m = re.match(r"^\[(PASS|FAIL)\] (\S+) (.*)$", ln)
            cid, st, what = (m.group(2), m.group(1), m.group(3).split(" -- ")[0]) if m else (None, None, None)
        if cid in ids:
            got[cid] = {"status": st, "what": what}
    return got


def owner_run(name):
    """C15-C19's and C26-C31's computation: the owner loaded by path and its own selftest() called (its stdout
    captured); each owner check's PASS/FAIL as the owner printed it, the owner's verdict and check list, its md5.  An
    owner that is absent, will not load, or raises counts as failed, never as passed."""
    path = OWNER_PATHS[name]
    rec = {"owner": name, "file": os.path.basename(path), "present": os.path.exists(path), "md5": None,
           "imported": False, "verdict": False, "ids": [], "checks": {}, "summary": "", "error": None,
           "sections": list(OWNER_SECTIONS[name])}
    t0 = time.time()
    if not rec["present"]:
        rec["error"] = "owner file absent: " + path
    else:
        rec["md5"] = _md5(path)
        try:
            mod = owner_module(name)
            rec["imported"] = True
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                good = mod.selftest()
            lines = buf.getvalue().splitlines()
            rec["verdict"] = bool(good)
            rec["ids"] = _owner_ids(mod)
            rec["checks"] = _owner_lines(name, lines, rec["ids"])
            rec["summary"] = next((ln for ln in reversed(lines) if ln.startswith("selftest")), "")
            rec["selftest_text"] = "\n".join(lines)
        except Exception as ex:
            rec["error"] = f"{type(ex).__name__}: {ex}"[:400]
    rec["seconds"] = time.time() - t0
    return rec


def owner_output(name):
    """The owner's own compute() output as its selftest left it cached (epass_pairing._out(), epass_frames._output()),
    made plain JSON with the owner's own serializer; None when the owner is absent or will not run."""
    try:
        mod = owner_module(name)
        if name == "epass_pairing":
            return json.loads(json.dumps(mod._out(), default=str))
        return json.loads(json.dumps(mod._output(), default=mod._json_default))
    except Exception:
        return None


def _get(obj, path):
    """obj[path[0]][path[1]]...; an 'id=X' step picks, in a list, the dict whose 'id' is X; None when absent."""
    for step in path:
        if isinstance(obj, list) and isinstance(step, str) and step.startswith("id="):
            obj = next((r for r in obj if isinstance(r, dict) and r.get("id") == step[3:]), None)
        elif isinstance(obj, dict):
            obj = obj.get(step)
        else:
            return None
    return obj


def _norm(s):
    return re.sub(r"\s+", " ", str(s)).strip()


def _sig_equal(value, quoted):
    """The owner's number rounded to the quote's significant digits equals the quote."""
    mant = quoted.lower().split("e")[0].lstrip("-")
    digits = len(mant.replace(".", "").lstrip("0"))
    return float(f"{float(value):.{digits - 1}e}") == float(quoted)


def quote_agrees(kind, value, expected, md5=None):
    """C35a's comparison of an owner's live value with what the docstring quotes (kinds as DOC_QUOTES says)."""
    try:
        if kind == "md5":
            return bool(md5) and md5.startswith(expected)
        if value is None:
            return False
        return {"str": lambda: str(value) == expected, "true": lambda: value in (True, "True"),
                "false": lambda: value in (False, "False"), "zero": lambda: float(value) == 0.0,
                "sig": lambda: _sig_equal(value, expected),
                "num": lambda: abs(float(value) - expected) <= 1e-12 * max(1.0, abs(expected)),
                "prefix": lambda: str(value).startswith(expected),
                "contains": lambda: _norm(expected) in _norm(value)}[kind]()
    except (TypeError, ValueError, KeyError):
        return False


def _row_from_owner(name, path, sec, outp):
    """An owner's row carried whole into X13-X18: the owner's own label and tag (the spec's section tag where the
    owner's row has none, said so)."""
    r = _get(outp, path) if outp is not None else None
    if not isinstance(r, dict):
        return {"section": sec, "owner": name, "owner_row": "/".join(path), "label": "OPEN (owner output absent)",
                "tag": SPEC_TAG[sec] + " (the spec's section tag)", "content": None}
    tag = r.get("tag") or (SPEC_TAG[sec] + " (the spec's section tag; the owner's row carries none)")
    return {"section": sec, "owner": name, "owner_row": "/".join(path), "label": r.get("label", "OPEN (unlabelled)"),
            "tag": tag, "content": r}


def x11_x25():
    """The X11-X25 block as data: X13 and X14 from epass_pairing's output, X17's stationary half and X18 from
    epass_frames' output (each owner row carried whole with the owner's label and tag; nothing re-derived here); the
    ten [PLANE] sections DEFERRED with the reason; X25's table restricted to computed sources; and C35a's comparison of
    every value the docstring quotes with the owners' live output."""
    outs = {n: owner_output(n) for n in OWNER_PATHS}
    md5 = {n: (_md5(p) if os.path.exists(p) else None) for n, p in OWNER_PATHS.items()}
    rows = {}
    for name, path, sec in PAIRING_ROWS + FRAMES_ROWS:
        rows[sec + ":" + "/".join(path)] = _row_from_owner(name, path, sec, outs[name])
    for sec, what in DEFERRED.items():
        rows[sec] = {"section": sec, "status": "DEFERRED (not built)", "label": "OPEN (deferred: not built)",
                     "tag": "[PLANE]", "content": what, "why": DEFER_WHY}
    doc = _norm(__doc__)
    quotes = []
    for qid, name, path, kind, expected, text in DOC_QUOTES:
        value = None if kind == "md5" else _get(outs[name], path)
        quotes.append({"id": qid, "owner": name, "docstring_text": text, "in_docstring": _norm(text) in doc,
                       "expected": expected, "owner_value": md5[name] if kind == "md5" else value,
                       "agrees": quote_agrees(kind, value, expected, md5[name])})
    table = [dict(r, label="deduced (from the computed sections the row names)") for r in X25_ROWS + tuple(X25_EXTRA)]
    # a [FREE] section counts as built only when it has owner rows and every one of them carries the owner's content
    built = [s for s in SPEC_FREE
             if any(r["section"] == s for r in rows.values())
             and all(r["content"] is not None for r in rows.values() if r["section"] == s and "status" not in r)]
    return {"rows": rows, "built": built + ["X25"], "deferred": sorted(DEFERRED),
            "x25": {"label": "deduced (from X1-X10, X13, X14, X17's stationary half, X18 and sim2_facing S15)",
                    "tag": "[mixed]", "gates": X25_GATES, "rows": table, "left_out": X25_LEFT_OUT,
                    "combined": X25_COMBINED + ((" " + X25_PLANT) if X25_PLANT else "")},
            "quotes": quotes, "owner_md5": md5, "docstring_block": docstring_block()}


def docstring_block():
    """The X11-X25 block of this file's docstring, as printed (C35b scans it with the rows)."""
    doc = __doc__ or ""
    a, b = doc.find("X11-X25 THE INTEGRATION"), doc.find("It is necessary, not sufficient")
    return doc[a:b] if 0 <= a < b else ""


def _label_tokens(lab):
    """A label's tokens: parentheses and [tags] removed (nested ones too), split at ';' and ','."""
    s, depth, kept = str(lab), 0, ""
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif depth == 0:
            kept += ch
    return [t.strip() for t in re.split(r"[;,]", kept) if t.strip()]


def _labels_in(o, acc, path=""):
    """Every 'label' value anywhere in o, with its path."""
    if isinstance(o, dict):
        if "label" in o:
            acc.append((path, o["label"]))
        for k, v in o.items():
            _labels_in(v, acc, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _labels_in(v, acc, path + f"[{i}]")
    return acc


def _strings_in(o, acc):
    if isinstance(o, dict):
        for v in o.values():
            _strings_in(v, acc)
    elif isinstance(o, list):
        for v in o:
            _strings_in(v, acc)
    elif isinstance(o, str):
        acc.append(o)
    return acc


_NEG = r"(?:\bnot\b|\bnever\b|\bneither\b|\bnon-|\bno\b)"


def calls_zero_positive(text):
    """Pitfall 13, a clause-level regex guard: a clause that calls a pair total, a net or a sum 'positive' within 40
    characters (commas included), not negated within the 30 characters before it."""
    hits = []
    for clause in re.split(r"[.;:()\[\]]", text):
        for m in re.finditer(r"\bpositive\b", clause, re.I):
            before, after = clause[:m.start()], clause[m.end():]
            if re.search(_NEG + r"[^,]{0,30}$", before, re.I):
                continue
            if (re.search(r"\b(?:pair|pairs|net|total|totals|sum|sums|summed)\b.{0,40}$", before, re.I)
                    or re.match(r"^.{0,12}\b(?:total|net|sum)\b", after, re.I)):
                hits.append(clause.strip())
    return hits


_VERDICT = (r"\b(?:refuted|refutes|passed|passes|fails|failed|ruled out|disproved|disproven)"
            r"(?:\s+(?:or|and|nor)\s+(?:refuted|passed))?\b")
_NEG_NEAR = r"\b(?:not|never|nor|neither|no longer)\b(?:\W+[\w'-]+){0,2}\W*$"
_ROUTE_SUBJ = r"\broute\b(?:\W+[\w'-]+){0,8}?\W+second sheet\b(?:\W+[\w'-]+){0,2}\W*$"


def calls_epass_refuted(text):
    """A clause-level regex guard: a clause naming E-PASS with a verdict word (refuted, passed, fails, ruled out,
    disproved) counts unless a negator stands within the two words directly before that word, or the word's subject
    is the route with no second sheet ("the route with no second sheet is REFUTED").  It guards against the phrasings
    it was tested on, not against every phrasing."""
    hits = []
    for clause in re.split(r"[.;:]", text):
        if not re.search(r"\bE-PASS\b", clause):
            continue
        for m in re.finditer(_VERDICT, clause, re.I):
            before = clause[:m.start()]
            if re.search(_NEG_NEAR, before, re.I) or re.search(_ROUTE_SUBJ, before, re.I):
                continue
            hits.append(clause.strip())
            break
    return hits


# ------------------------------------------------------------------------------------------------------- compute
SECTIONS = ("chart", "horizon", "one_way", "kasner", "eta", "jminus", "budgets", "slab", "coincide", "frame", "eq",
            "data", "inject", "own_pairing", "own_frames", "x11")


def compute(only=None):
    """The instrument's output; only = a subset of SECTIONS recomputes those (--mutants)."""
    t0 = time.time()
    want = lambda k: only is None or k in only
    dv = write_floor()
    out = {"write_floor": dv}
    if want("chart"):
        out["chart"] = {"identity": str(chart_identity()), "identity_control": str(chart_identity(shift=1))}
        ce = chart_equations()
        out["chart"]["equations"] = {k: str(v) for k, v in ce.items()}
        out["chart"]["equations_control_Q"] = str(chart_equations(s2=-1)["Q"])
    if want("horizon"):
        hz, hc = horizon(), horizon(hh=sp.Rational(1, 3))
        out["horizon"] = {k: str(v) for k, v in hz.items()}
        out["horizon_control_kappa2_on"] = str(hc["kappa2_on"])
    if want("one_way"):
        ow = one_way()
        out["one_way"] = {"dudv": [str(r_) for r_ in ow["dudv"]], "g_v_u": str(ow["g_v_u"]),
                          "g_v_u_num": float(ow["g_v_u"]) if ow["g_v_u"].is_number else None, "udot2": ow["udot2"]}
    if want("kasner"):
        kd = kasner_deduced()
        out["kasner"] = {"deduced": {k: str(v) for k, v in kd.items()}, "a_num": float(kd["a"]), "b_num": float(kd["b"]),
                         "fits": {str(e): kasner_fit(e) for e in ES2}, "control": kasner_fit(Fr(1, 8), mutate=1.0)}
    if want("eta"):
        out["eta_s"] = {str(e): eta_of(e, tb(e)["y_s"] * 1.0001) for e in ES2}
        out["eta_s_independent"] = {str(e): eta_independent(e) for e in ES2}
        out["eta_ab_diff"] = max(abs(out["eta_s"][k] - out["eta_s_independent"][k]) for k in out["eta_s"])
        out["eta_control"] = eta_control()
    if want("jminus"):
        out["jminus"] = {"null": jminus_check(), "control": jminus_check(n_rays=4, wrong=True, n_timelike=0)}
    if want("budgets"):
        rows = {}
        for e in ES2:
            es = eta_of(e, tb(e)["y_s"] * 1.0001)
            rows[str(e)] = {"exact_throat": {str(x): budget(es, x) for x in X_LIMS},
                            "exact_throat_past": {str(x): budget(es, x) for x in X_LIMS_PAST},
                            "x_cross_lower": 8 * (2 * math.sin(es / 4)**2 / dv)**2,
                            "x_cross_upper": 8 * (es / 2 / dv)**2,
                            "layers": [layer(e, F) for F in F_LAYERS]}
        out["budgets"] = rows
        out["layer_scan"] = {str(e): layer_scan(e, dv) for e in ELL_SHOW}
        grid, vdp = dp_confined()
        z2 = 2 * math.sqrt(2) / math.sqrt(1e-2)
        etas = sorted({round(eta_of(e, tb(e)["y_s"] * 1.0001), 12) for e in ES2}
                      | {round(L["eta"], 12) for r_ in rows.values() for L in r_["layers"] if L})
        out["dp_check"] = [{"eta": et, "lower_n": budget(et, 1e-2)[0] / z2, "upper_n": budget(et, 1e-2)[1] / z2,
                            "dp": float(np.interp(et, grid, vdp)), "g": g_confined(et)} for et in etas]
    if want("slab"):
        out["slab"] = {str(e): slab_rows(e, dv) for e in ES2}
        out["slab_window"] = {str(e): slab_window(e) for e in ES2}
    if want("coincide"):
        out["coincide_K"] = {str(e): {"computed": float(k_ratio(e, COINCIDE_FRAC * tb(e)["y_s"])),
                                      "deduced": k_ratio_zero_deduced(e)} for e in ES2}
    if want("frame"):
        out["crosser_frame"] = {str(e): crosser_frame(e) for e in ELL_SHOW + (Fr(1, 32),)}
    if want("eq"):
        q17, qs = plane_null_energy(PLANE_DATA), plane_null_energy("schw")
        keep = lambda q: {k: (v if isinstance(v, (float, type(None))) else str(v)) for k, v in q.items()}
        out["eq"] = {"eq17": keep(q17), "schw": keep(qs), "closed": str(ANEC_CLOSED),
                     "closed_num": float(ANEC_CLOSED)}
    if want("data"):
        out.setdefault("eq", {})["data"] = data_fixes_bulk()
    if want("inject") and INJECT_KEY:
        out[INJECT_KEY] = 0
    if want("own_pairing"):                  # X13, X14: the owner's own selftest, by path (C15-C19)
        out["owner_pairing"] = owner_run("epass_pairing")
    if want("own_frames"):                   # X17 (stationary half), X18: the owner's own selftest, by path (C26-C31)
        out["owner_frames"] = owner_run("epass_frames")
    if want("x11"):                          # the X11-X25 block, from the owners' cached outputs (C35a, C35b)
        out["x11_x25"] = x11_x25()
    out["seconds"] = time.time() - t0
    return out


def _keys(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, (list, tuple)):
        for v in o:
            yield from _keys(v)


def address_guard(out):
    """No key of the output names a length, distance, time, speed, redshift, clock or arrival (155 (2), 139 (4), 101 (7)),
    and no function of this instrument takes an argument named in sim2_facing.BANNED_ARGS (a plane separation); the
    write floor and the budgets are holds for the cone premise."""
    mod = sys.modules[__name__]
    funcs = [f for _, f in inspect.getmembers(mod, inspect.isfunction) if f.__module__ == mod.__name__]
    bad_args = sorted({f"{f.__name__}({p})" for f in funcs for p in inspect.signature(f).parameters
                       if p in SF.BANNED_ARGS})
    return [k for k in _keys(out) if any(b in k.lower() for b in BANNED_KEYS)] + bad_args


def _ell(k):
    e = Fr(k)
    return "inf" if e == 0 else (f"{1/e}m" if (1 / e).denominator == 1 else f"{float(1/e)}m")


def _fails(out):
    """X9's negative result: the (ell, row, profile) at which P2 reaches y_s^th within x_valid(d)."""
    return [(e, k, kn) for e, rws in out["slab"].items() for k, r_ in rws.items()
            for kn, mg in r_["margins"].items() if mg is not None and mg <= 0]


def _xh(v):
    return "?" if v is None else ("< 1e-14" if v == 0 else f"{v:.2g}")


def report(out):
    P = print
    P("sim2_passage.py -- E-PASS, the passage through the corridor object's own horizon (not verified; not seated)")
    P("  184: every matter-free plane below (P1 under clause (B) in full, wherever its data enter, X10 (a)-(e) included; "
      "Schwarzschild's control) is a limit, not M's configuration; X1-X10 are the board's configuration, re-read under "
      "179-180 (H-CORRIDOR-IN-BULK)")
    P(f"write floor (o3_write, example README): {out['write_floor']:.4g} clocks")
    P("X1 chart identity:", out["chart"]["identity"], "| control (shift 1):", out["chart"]["identity_control"][:40], "...")
    P("X1 EF vacuum equations vs coded: P", out["chart"]["equations"]["P"], "Q", out["chart"]["equations"]["Q"],
      "constraint ratio", out["chart"]["equations"]["constraint_ratio"], "| control Q (S2 flipped):",
      out["chart"]["equations_control_Q"])
    h = out["horizon"]
    P("X2 horizon: xi^2 =", h["norm"], " g^uu =", h["g_uu_inv"], " g^yu =", h["g_yu_inv"], " kappa^2 =", h["kappa2"],
      " on u=0:", h["kappa2_on"], "| control (u^2 - 1/9) on its horizon:", out["horizon_control_kappa2_on"])
    ow = out["one_way"]
    P("X3 null directions (from ef_metric): du/dv =", ow["dudv"], "(and dv = 0); g(d_v, d_u)/alpha^2 =", ow["g_v_u"],
      "| on the plane u'^2 =", ow["udot2"])
    k = out["kasner"]
    kd = k["deduced"]
    P(f"X4 Kasner deduced (leading balance of the coded system): evolution {kd['evolution_p']} = 0, "
      f"{kd['evolution_q']} = 0 -> a + b = {kd['a_plus_b']}; constraint {kd['constraint']} = 0 -> ab = {kd['ab']}")
    P(f"    a = {kd['a']} = {k['a_num']:.6f}, b = {k['b_num']:.6f}; 2a+2b = {kd['sum']}, 2a^2+2b^2 = {kd['squares']}")
    for e, f in k["fits"].items():
        P(f"    ell = {_ell(e):>6}: a = {f['a']:.6f}, b = {f['b']:.6f}")
    P(f"    control (2pq -> 3pq): a = {k['control']['a']:.4f}, b = {k['control']['b']:.4f}")
    P("X5 eta_s (conformal depth of the singular surface; tail counted once) | independent (eta as variable) | ground:")
    for e, v in out["eta_s"].items():
        P(f"    ell = {_ell(e):>6}: eta_s = {v:.7f} | {out['eta_s_independent'][e]:.7f} | [{GROUND_ETA[e]}]  "
          f"eta_s/pi = {v/math.pi:.3f}")
    P(f"    largest |eta_s - independent|: {out['eta_ab_diff']:.1e}")
    c = out["eta_control"]
    P("    control through eta_of, eta at alpha = 1e-3, 1e-6, 1e-9 (ell = 8m): mutated ODE (alpha ~ delta^1.002)",
      [round(v, 3) for v in c["mutated"]], "increments", [round(v, 3) for v in c["mutated_inc"]], "| true system",
      [round(v, 6) for v in c["true"]], "increments", [f"{v:.2e}" for v in c["true_inc"]])
    j = out["jminus"]
    P(f"X6 J^-(P_c) criterion along null geodesics (one ray up to dilatation): worst relative residual "
      f"{j['null']['worst']:.2e}; timelike rays strictly inside, least relative margin {j['null']['interior_margin']:.3f}; "
      f"control sin^2(eta/2): {j['control']['worst']:.2e}")
    wf = out["write_floor"]
    P("X7 cone budgets [lower, upper] (confined minimum), clocks (advanced coordinate v_c - v_open):")
    for e in ELL_SHOW:
        r = out["budgets"][str(e)]
        P(f"  ell = {_ell(str(e))}:")
        for x, (lo, hi) in r["exact_throat"].items():
            P(f"    singular surface, EXACT THROAT held to y_s, x_lim = {x}: [{lo:.4g}, {hi:.4g}]  (floor/upper "
              f"{wf/hi:.3g})")
        for x, (lo, hi) in r["exact_throat_past"].items():
            P(f"    past the tested range, x_lim = {x}: [{lo:.4g}, {hi:.4g}]{'  ABOVE THE FLOOR' if hi > wf else ''}")
        P(f"    exact-throat crossover: upper passes the floor below x_lim = {r['x_cross_upper']:.3g}, lower below "
          f"{r['x_cross_lower']:.3g}")
        for L in r["layers"]:
            if L:
                P(f"    layer K = {L['F']:.0e} K_bs at y = {L['y_K']:.4f}m: x_lim {L['x_lim']:.2e}, eta {L['eta']:.3f}, "
                  f"[{L['lower']:.4g}, {L['upper']:.4g}] ({L['tight']:.4g})")
        sc = out["layer_scan"][str(e)]
        for L in sc["rows"]:
            if L:
                P(f"    deeper, K = {L['F']:.0e} K_bs: x_lim {L['x_lim']:.2e}, [{L['lower']:.4g}, {L['upper']:.4g}]"
                  f" ({L['tight']:.4g}){'  LOWER ABOVE THE FLOOR' if L['lower'] > wf else ''}")
        P(f"    budget ~ K^{sc['exponent']:.3f} (upper, 1e15-1e30 K_bs); lower passes the floor "
          + (f"between K = {sc['crossover_after_F']:.0e} and {sc['crossover_F']:.0e} K_bs (per-decade scan)"
             if sc["crossover_F"] else "-- not before the full system ends (alpha = 1e-6)"))
        P(f"    placed in J^-(P_c) within O(x): by the upper budget (an explicit curve) to K = {sc['placed_F']:.0e} K_bs; "
          f"by the confined minimum (g, numerical to 1.3%) to {sc['placed_tight_F']:.0e} K_bs")
    mx = max(L["upper"] for r in out["budgets"].values() for L in r["layers"] if L)
    P(f"    largest claimed layer budget (K <= 1e10 K_bs, within O(x)) over all nine ell: {mx:.4g} clocks, against the "
      f"write's {wf:.4g}")
    worst = max(abs(d_["dp"] - d_["g"]) / d_["g"] for d_ in out["dp_check"])
    P(f"    confined minimum by dynamic programme vs g(eta) at {len(out['dp_check'])} depths: worst relative "
      f"{worst:.2e}; bracket [2 sin^2(eta/4), eta/2] holds: "
      f"{all(d_['lower_n'] <= d_['dp'] * 1.01 + 2e-3 and d_['dp'] <= d_['upper_n'] * 1.01 for d_ in out['dp_check'])}")
    P("X9 position 2's piece at depth d (eta(d)/eta_s; K/K_bs; u_min at the write's floor; margin y_s - max(d + f) per "
      "profile within x_valid(d), '-' = not admissible):")
    for e in ELL_SHOW + (Fr(1, 32), Fr(1, 2), Fr(4)):
        for k2, v in out["slab"][str(e)].items():
            tag = " (= 0: flat limit, exact coincidence)" if k2 == "d_plus" and v["depth"] == 0 else ""
            mg = ", ".join(f"{kn} {('%+.4f' % m_) if m_ is not None else '-'}" for kn, m_ in v["margins"].items())
            P(f"    ell = {_ell(str(e)):>6} {k2:>8}{tag}: d = {v['depth']:.4f}m, eta = {v['eta']:.4f} "
              f"({v['eta_over_eta_s']:.3f}), K/K_bs = {v['K_ratio']:.4g}, u_min = {v['u_min']:.2e}; {mg}")
    P("    P2 reaches y_s^th within x_valid(d) (NEGATIVE result): "
      + "; ".join(f"ell = {_ell(e)} {k2} {kn} from x = {_xh(out['slab'][e][k2]['hits'].get(kn, {}).get('x_hit'))}"
                  f"{' (in J^-(P_c))' if out['slab'][e][k2]['hits'].get(kn, {}).get('in_cone') else ''}"
                  for e, k2, kn in _fails(out)))
    cc = [(v_, e, k2, kn) for e, rws in out["slab"].items() for k2, r_ in rws.items()
          for kn, v_ in r_["c_crit"].items()]
    rel = [t_ for t_ in cc if t_[2] in ("zero", "tenth", "d_plus")]
    oth = [t_ for t_ in cc if t_[2] not in ("zero", "tenth", "d_plus")]
    fmt = lambda t_: f"{t_[0]:.3g} (ell = {_ell(t_[1])}, {t_[2]}, {t_[3]})"
    P(f"    amplitude: a power law keeps its margin iff c < c* = (y_s - d)/x_valid(d)^lam (sampled c = {SF.DT_C}); "
      f"least c* at depth 0, 0.1 y_s, d_+: {fmt(min(rel))}; at y*/band_mid: least {fmt(min(oth))}, largest "
      f"{fmt(max(oth))}")
    sw = out["slab_window"]["1/32"]
    P(f"    positive-energy window at ell = 32m: [d_+, top] = [{sw['d_plus']:.4f}m, {sw['top']:.4f}m], lam_max at d_+ "
      f"{sw['lam_max']:.3f}; at ell = inf d_+ = {out['slab_window']['0']['d_plus']}")
    P("    coinciding limit d -> 0, K/K_bs computed vs 2(80e^4+3)/(160e^4+3):",
      [(_ell(e), round(v["computed"], 6), round(v["deduced"], 6)) for e, v in out["coincide_K"].items()])
    P("    crosser's frame at P_c, 4 alpha^2 (rho + p_r)/x at x = 1e-4, 1e-8, 1e-12 (depth 0):")
    for e, fr in out["crosser_frame"].items():
        P(f"      ell = {_ell(e):>6}: " + "; ".join(f"{kn} {[f'{v:.3g}' for v in d_['values']]}"
                                                    for kn, d_ in fr.items()))
    P("    the same points in the static orthonormal frame (rho, rho + p_r), finite -- a divergence along the regular "
      "null frame only:")
    for e in ("0", "1/8"):
        fr = out["crosser_frame"][e]
        P(f"      ell = {_ell(e):>6}: " + "; ".join(
            f"{kn} rho {[f'{v:.3g}' for v in d_['static_rho']]}, rho+p_r {[f'{v:.3g}' for v in d_['static_nec_r']]}"
            for kn, d_ in fr.items()))
    q = out["eq"]
    P("X10 (a) 5D vacuum: R_kk = 0 for every null k (Lambda_5 g_kk = 0)")
    P(f"X10 (b) eq. (17) on the plane: R = {q['eq17']['R']}; rho + p_r = {q['eq17']['nec']} (ratio to BK eq. (18) x "
      f"1/(8 pi): {q['eq17']['bk18_ratio']}); integrated null energy along the ingoing ray {q['eq17']['anec']:.12f} = "
      f"{q['closed']} exactly (|sympy exact - closed form| = {q['eq17']['exact_minus_closed']:.1e} at 60 digits); full "
      f"ray twice this; Schwarzschild control {q['schw']['anec']:.1e}")
    P(f"X10 (d) eq. (17) at r0 = 2m: g_tt at the throat = {q['eq17']['g_tt_at_throat']}")
    d = q["data"]
    P(f"X10 (c) y_s at ell = 8m: vacuum data {d['vacuum']:.6f}; p(0) -+ 1e-3 on the constraint surface (q(0) = "
      f"{d['q0_minus']:.6f}, {d['q0_plus']:.6f}): {d['minus']:.6f}, {d['plus']:.6f}; largest relative constraint residual "
      f"{d['cons_max']:.1e}")
    P("X10 (c)/(e): the coincident pair's net surface stress is zero (sim2_facing S15, computed there, not here) -- "
      "a total of zero, not positive")
    report_x11(out)
    P(f"(computed in {out['seconds']:.1f} s)")


def report_x11(out):
    """The X11-X25 block: the owners' selftests, their rows' key values (the owners' outputs, never re-derived), the
    deferred [PLANE] sections and X25, restricted."""
    P = print
    xb = out["x11_x25"]
    P("X11-X25 (the integration; [FREE] sections from two owners imported by path; [PLANE] sections DEFERRED):")
    for key in ("owner_pairing", "owner_frames"):
        r = out[key]
        st = ", ".join(f"{c} {v['status']}" for c, v in r["checks"].items())
        P(f"  owner {r['file']} ({', '.join(r['sections'])}; md5 {r['md5'] or '-'}): {r['summary'] or r['error']} "
          f"[{st}]")
    g = lambda *path: _get(xb["rows"], path)
    pr = lambda k: (g("X13:results/" + k, "content") or g("X14:results/" + k, "content") or {})
    b, pm, sh = pr("X13b_bulk"), pr("X13b_premise"), pr("X13a_sheet")
    if b:
        P(f"  X13 Lemma S [FREE], bulk form: R(xi,xi)|_H = {b['cases']['degenerate']['R_xixi']} (degenerate), "
          f"{b['cases']['nondegenerate']['R_xixi']} (non-degenerate), "
          f"{b['cases']['degenerate']['R_xixi_nonstationary_null_kept']} (non-stationary, u = 0 kept null); shear at "
          f"fixed volume: theta = "
          f"{pm['cases']['degenerate']['shear_fixed_volume']['theta']}, R(xi,xi) = "
          f"{pm['cases']['degenerate']['shear_fixed_volume']['R_xixi_witness']} = -sigma^2 [{pm['label']}]")
        P(f"      sheet form: K(xi,xi)|_H = {sh['cases']['throat_degenerate']['K_xixi']}, "
          f"{sh['cases']['throat_nondegenerate']['K_xixi']} (throat, degenerate / non-degenerate); tilted sheet "
          f"{pr('X13a_scope')['K_xixi']['throat_nondegenerate_tilted_sheet']:.4g} where kappa != 0 [{sh['label']}]")
        w, pt, pa = pr("X13c_weyl"), pr("X13d_pair_tensor"), pr("X13d_pair")
        P(f"      Weyl term: E(xi,xi) = {w['cases']['degenerate']['stationary']['E_xixi']} [FREE]; pair [PLANE]: README "
          f"{pa['readme_member']}, partner {pa['partner_member']}, net {pa['net']} ({pa['net_status']}; by "
          f"construction); tilted partner pi(xi,xi) = {pt['pi_xixi_sms20']}, zero total stress only at b = 0: "
          f"{pt['pair_is_zero_at_b0']}")
        kn = pr("X14_numeric")["cases"]
        P(f"  X14 Lemma K [FREE for sheets]: y'' = {pr('X14_tangent')['ydd_connection']}; S_vv = 0 stays "
          f"({kn['S_vv=0']['stays_on_sheet']}); +1 -> y_end {kn['S_vv=+1']['y_end']:.4f}; -1 -> y_end "
          f"{kn['S_vv=-1']['y_end']:.4f} (into the bulk)")
    fr = lambda *k: g(*k, "content") or {}
    fl, sd, si = fr("X17:X17/readme_flux_P1"), fr("X17:X17/stationary_demand"), fr("X17:X17/demand_si")
    if fl:
        P(f"  X17 stationary half: kappa_4^2 int T_vv dv = {fl['value']} per generator (r_h = {fl['r_h_over_m']}m, "
          f"kappa m = {fl['kappa_x_m']}, control {fl['kappa_x_m_schwarzschild_control']}) [{fl['tag'][:48]}...]; "
          f"pair net per generator {sd['pair_net_per_generator']} ({sd['pair_net_reading'][:60]}...)")
        for k, r in si["rows"].items():
            P(f"      {k}: E = {r['E_J']:.6g} J, m = {r['m_geometric_m']:.6g} m, 1/(2m) = "
              f"{r['kappa4sq_int_Tvv_per_m']:.6g} m^-1, u_r(m) = {r['u_r_m']:.3g}")
    gc = fr("X18:X18/generator_classes")
    if gc:
        P("  X18 [FREE] classes: " + "; ".join(f"{n} {v['class_matrix']} ({v['component_at_sigma0']}, "
                                              f"{v['component_at_sigmapi']})" for n, v in gc["rows"].items()))
        tg, em, fa = fr("X18:X18/throat_generator"), fr("X18:X18/ends_map"), fr("X18:X18/ads2_family")
        P(f"      throat d_v: Q = {tg['Q']}, {tg['class']} [{tg['tag'][:24]}...]; ends: end 1 {em['end1_boundary']}, "
          f"end 2 {em['end2_boundary']}, u = 0 patch 1's future horizon {em['u0_is_patch1_future_horizon']}; AdS2 "
          f"family Q = {fa['Q_general']}: {fa['classes']}")
        w2 = fr("X18:X18/lemma_p/ii_weyl_fluid")
        P(f"      Lemma P (ii) [PLANE]-conditional: 8 pi rho = {w2['fluid']['8pi_rho']}, 8 pi (rho + p_r) = "
          f"{w2['fluid']['8pi_rho_plus_p_r']}, v* = {w2['v_star']} (rapidity {w2['rapidity_star']:.6f}); approach "
          f"gamma^2 v^2 = {w2['approach_counterpart']['gamma2v2_float']:.5g}; 176 sentence: "
          f"{fr('X18:X18/deduced/board_176_sentence')['verdict']}")
    P("  DEFERRED [PLANE], not built: " + ", ".join(xb["deferred"]) + " -- " + DEFER_WHY[:150] + " ...")
    for r in xb["x25"]["rows"]:
        P(f"  X25 {r['row']} {r['config']} {r['tag']}: {r['verdict']}")
    P(f"  X25 left out (deferred): {xb['x25']['left_out']}")
    qs = xb["quotes"]
    P(f"  C35a: {sum(q['in_docstring'] and q['agrees'] for q in qs)}/{len(qs)} docstring values equal the owners' "
      "live output")


# ------------------------------------------------------------------------------------------------------ checks
def checks(out):
    """C1-C14 (C11 in two parts), then C15-C19 and C26-C31 (the owners' own selftests, run by path) and C35a-C35b (the
    X11-X25 block), as (id, label, ok, note); each reads only the output, and each has a mutation in MUTANTS under
    which it must fail."""
    res = []

    def ok(cid, name, cond, note=""):
        res.append((cid, name, bool(cond), note))
    c = out["chart"]
    ok("C1", "chart identity; control shift 1 non-zero", c["identity"] == "0" and c["identity_control"] != "0")
    eq = c["equations"]
    try:
        cr = sp.sympify(eq["constraint_ratio"])
        crok = cr.is_number and cr != 0
    except (sp.SympifyError, TypeError):
        crok = False
    ok("C2", "EF equations = coded P, Q, constraint; uu = 0; control (S2 flipped) differs",
       eq["P"] == "0" and eq["Q"] == "0" and crok and eq["uu"] == "0" and eq["vv_over_vu"] == "0"
       and c["equations_control_Q"] != "0")
    h = out["horizon"]
    ok("C3", "horizon at u = 0 null, kappa = 0 at every depth; control kappa != 0",
       h["kappa2_on"] == "0" and h["norm_on"] == "0" and h["g_uu_inv_on"] == "0" and h["g_yu_inv"] == "0"
       and out["horizon_control_kappa2_on"] != "0")
    ow = out["one_way"]
    uu = sp.Symbol("u", real=True)
    E_ = sp.Symbol("E", real=True)
    good4 = (len(ow["dudv"]) == 1 and sp.simplify(sp.sympify(ow["dudv"][0], locals={"u": uu}) - uu**2 / (4 * sp.sqrt(2))) == 0
             and ow["g_v_u_num"] is not None and ow["g_v_u_num"] > 0 and len(ow["udot2"]) == 1
             and sp.simplify(sp.sympify(ow["udot2"][0], locals={"u": uu, "E": E_}) - (E_**2 / 2 - uu**2 / 4)) == 0)
    ok("C4", "one way, from ef_metric: du/dv = u^2/(4 sqrt2) >= 0, g(d_v,d_u) > 0; on the plane u'^2 = E^2/2 - u^2/4",
       good4)
    k = out["kasner"]
    good = all(abs(f["a"] - k["a_num"]) < 2e-4 and abs(f["b"] - k["b_num"]) < 2e-4 for f in k["fits"].values())
    ok("C5", "Kasner: deduced from the coded leading balance (a + b = 1/2, ab = -1/8; sums 1); fits at nine ell; "
       "control differs", good and k["deduced"]["sum"] == "1" and k["deduced"]["squares"] == "1"
       and k["deduced"]["ab"] == "-1/8" and abs(k["control"]["a"] - k["a_num"]) > 1e-2)
    es = out["eta_s"]
    mono = all(es[str(ES2[i])] > es[str(ES2[i + 1])] for i in range(len(ES2) - 1))
    ge = all(abs(es[e] - GROUND_ETA[e]) <= 5e-4 + 1e-9 for e in GROUND_ETA)
    cc = out["eta_control"]
    ctl = (all(v > 0.5 * cc["mutated_inc"][0] for v in cc["mutated_inc"])
           and all(cc["true_inc"][i + 1] < 0.1 * cc["true_inc"][i] for i in range(len(cc["true_inc"]) - 1)))
    ok("C6", "eta_s finite, below 2 pi, falls with 1/ell, equals an independent integration to 1e-9 (rounds to the "
       "ground stage's 3 decimals); control through eta_of diverges, the true system converges",
       out["eta_ab_diff"] < 1e-9 and mono and ge and all(v < 2 * math.pi for v in es.values()) and ctl,
       f"|A - B| = {out['eta_ab_diff']:.1e}")
    j = out["jminus"]
    ok("C7", "J^- criterion holds along null geodesics; timelike rays strictly inside; control fails",
       j["null"]["worst"] < 1e-6 and j["null"]["interior_margin"] > 0 and j["control"]["worst"] > 1e-2)
    wf = out["write_floor"]
    claimed = [L for r in out["budgets"].values() for L in r["layers"] if L]
    scans = out["layer_scan"]
    deep = (all(scans[str(e)]["crossover_F"] is not None for e in (Fr(0), Fr(1, 8)))
            and all(0.1 < (sc["exponent"] or 0) < 0.2 for sc in scans.values())
            and all(all(a_["upper"] < b_["upper"] for a_, b_ in zip([L for L in sc["rows"] if L],
                                                                    [L for L in sc["rows"] if L][1:]))
                    for sc in scans.values()))
    ok("C8", "every claimed layer (K <= 1e10 K_bs, within O(x)) and every exact-throat row (x_lim >= 1e-8) below the "
       "floor; deeper the budget grows (K^0.1-0.2) and the lower passes the floor (ell = inf, 8m)",
       all(L["upper"] < wf for L in claimed) and len(claimed) == len(F_LAYERS) * len(ES2)
       and all(hi < wf for r in out["budgets"].values() for _, hi in r["exact_throat"].values())
       and deep and 1.9e5 < wf < 2.1e5)
    dpc = out["dp_check"]
    ok("C9", "the bracket [2 sin^2(eta/4), eta/2] contains the confined minimum of an independent dynamic programme, "
       "which equals g(eta) (2 sin^2(eta/4) to pi, 1 + (eta - pi)/2 beyond) to 1.5%",
       len(dpc) >= 20 and all(d_["lower_n"] <= d_["dp"] * 1.01 + 2e-3 and d_["dp"] <= d_["upper_n"] * 1.01
                               and abs(d_["dp"] - d_["g"]) <= 0.015 * d_["g"] + 2e-3 for d_ in dpc))
    ck = out["coincide_K"]
    ok("C10", "coinciding limit K/K_bs = 2(80e^4+3)/(160e^4+3) at nine ell",
       all(abs(v["computed"] - v["deduced"]) < 1e-9 for v in ck.values()))
    sl = out["slab"]
    relied = [mg for e, rws in sl.items() for k_, r_ in rws.items() for kn, mg in r_["margins"].items()
              if k_ in ("zero", "tenth", "d_plus") and kn != "level" and mg is not None]
    fails = _fails(out)
    confined = all(kn.startswith("lam") and k_ in ("y_star", "band_mid") and Fr(e) >= 1
                   and sl[e][k_]["hits"].get(kn, {}).get("in_cone") for e, k_, kn in fails)
    ok("C11a", "P2's profile (not a cut): every sampled profile (c = 0.05) at 0.1 y_s, d_+ and depth 0 stays shallower "
       "than y_s^th within x_valid(d); every failure is a power law at y*/band_mid with ell <= m, inside J^- (the level "
       "surface at d >= y*: STRUCTURAL, not tested)",
       len(relied) >= 70 and all(mg > 0 for mg in relied) and confined, f"{len(fails)} power-law failures")
    fr = out["crosser_frame"]
    static_fin = all(abs(d_[key][2] - d_[key][1]) <= abs(d_[key][1] - d_[key][0])     # converging along x -> 0
                     for f_ in fr.values() for kn, d_ in f_.items() if kn.startswith("lam")
                     for key in ("static_rho", "static_nec_r", "static_nec_th"))
    ok("C11b", "crosser's frame at P_c: power-law P2 stress grows without bound as x -> 0 along the regular null frame "
       "while its static-frame rho, rho + p_r, rho + p_th converge (finite); the smooth family's stays finite",
       all(d_["growth"] > 1e3 for f_ in fr.values() for kn, d_ in f_.items() if kn.startswith("lam"))
       and static_fin and all(0.5 < f_["smooth"]["growth"] < 2 for f_ in fr.values()))
    q = out["eq"]
    ok("C12", "eq. (17)'s plane: R = 0, rho + p_r = BK (18)/(8 pi), integrated null energy < 0, finite and equal to "
       "(sqrt3 ln(2+sqrt3) - 6)/(36 pi) exactly; Schwarzschild 0",
       q["eq17"]["R"] == "0" and q["eq17"]["bk18_ratio"] == "1" and -10 < q["eq17"]["anec"] < 0
       and abs(q["eq17"]["anec"] - q["closed_num"]) < 1e-12 and q["eq17"]["exact_minus_closed"] < 1e-50
       and abs(q["schw"]["anec"]) < 1e-20)
    d = q["data"]
    ok("C13", "y_s depends on the plane's data: p(0) moved on the constraint surface, y_s moves both ways; constraint "
       "held along the runs", (d["minus"] < d["vacuum"] < d["plus"] or d["plus"] < d["vacuum"] < d["minus"])
       and d["cons_max"] < 1e-10, f"constraint {d['cons_max']:.1e}")
    bad = address_guard(out)
    ok("C14", "address guard: no key names a length, distance, time, speed, clock or arrival; no banned argument",
       not bad, str(bad))
    for cid, key, name in (("C15-C19", "owner_pairing", "epass_pairing"), ("C26-C31", "owner_frames", "epass_frames")):
        r = out[key]
        st = r["checks"]
        good = (r["present"] and r["imported"] and r["verdict"] and not r["error"]
                and set(OWNER_CHECK_IDS[name]) <= set(r["ids"]) and set(st) == set(r["ids"])
                and all(v["status"] == "PASS" for v in st.values()))
        note = (f"{r['summary']}; md5 {r['md5'][:8]}" if r["md5"] else "") + (f"; {r['error']}" if r["error"] else "")
        ok(cid, f"owner {name}.py ({', '.join(OWNER_SECTIONS[name])}), by path: its own selftest passes and every one "
           f"of its checks ({len(OWNER_CHECK_IDS[name])} as verified, or more) prints PASS; fails if the owner fails, "
           "is missing or drops a check", good, note)
    xb = out["x11_x25"]
    qs = xb["quotes"]
    bad_q = [q["id"] for q in qs if not (q["in_docstring"] and q["agrees"])]
    per_owner = {n: sum(1 for q in qs if q["owner"] == n) for n in OWNER_PATHS}
    ok("C35a", "the values DOC_QUOTES lists from the X11-X25 docstring (107 as built) are each printed there and equal "
       "the owner's live output (md5 prefixes included); other values the docstring or the note quotes are not "
       "checked here",
       not bad_q and all(v >= 20 for v in per_owner.values())
       and all(any(q["id"] == f"{p}_md5" for q in qs) for p in ("p", "f")),
       f"{len(qs) - len(bad_q)}/{len(qs)} agree" + (f"; disagree: {bad_q}" if bad_q else ""))
    rows = xb["rows"]
    lab_bad = [(p, lab) for p, lab in _labels_in(xb, [])
               if not _label_tokens(lab) or any(t not in LABELS for t in _label_tokens(lab))]
    tag_bad = [k for k, r in rows.items() if not any(s in str(r.get("tag", "")) for s in ("[FREE", "[PLANE"))]
    read_bad = [k for k, r in rows.items() if "READ" in _label_tokens(r["label"]) and "PDF p" not in str(r)]
    dset = set(xb["deferred"])
    built = set(xb["built"])
    defer_ok = (dset == set(SPEC_PLANE) and built == set(SPEC_FREE) | {"X25"} and not dset & built
                and dset | built == {f"X{i}" for i in range(11, 26)}
                and all(rows[s]["status"] == "DEFERRED (not built)" and rows[s]["tag"] == "[PLANE]"
                        and rows[s]["content"] and "179" in rows[s]["why"] for s in dset)
                and {r["section"] for r in rows.values() if r["section"] not in dset} == set(SPEC_FREE))
    t_bad = [r["row"] for r in xb["x25"]["rows"]
             if not set(r["sources"]) <= set(X25_COMPUTED) or set(r["sources"]) & set(SPEC_PLANE)
             or not set(r["deferred_parts"]) <= set(SPEC_PLANE)]
    texts = _strings_in(xb, [])           # the rows, X25 and the docstring's X11-X25 block (docstring_block)
    pos_bad = [h for t_ in texts for h in calls_zero_positive(t_)]
    ref_bad = [h for t_ in texts for h in calls_epass_refuted(t_)]
    ok("C35b", "the X11-X25 rows: every label made of the six, every row tagged [FREE...] or [PLANE...], READ rows "
       "paged; the ten [PLANE] sections exactly DEFERRED with the reason and the [FREE] four built (each with its "
       "owner rows present); X25's rows draw only on computed sections; the clause-level guards find no zero total "
       "called positive and no E-PASS called refuted or passed",
       not (lab_bad or tag_bad or read_bad or t_bad or pos_bad or ref_bad) and defer_ok
       and len(xb["docstring_block"]) > 1000,
       f"labels {lab_bad[:2]}; tags {tag_bad[:2]}; READ {read_bad[:2]}; deferred/built {'ok' if defer_ok else 'WRONG'}; "
       f"X25 {t_bad}; positive {pos_bad[:2]}; refuted {ref_bad[:2]}")
    return res


def selftest():
    out = compute()
    res = checks(out)
    for cid, name, good, note in res:
        print(f"  {'PASS' if good else 'FAIL'}  {cid} {name}  {note}")
    n = sum(r[2] for r in res)
    print(f"selftest {n}/{len(res)}  ({out['seconds']:.1f} s)")
    return n == len(res)


# ------------------------------------------------------------------------------------------------------ mutants
@contextlib.contextmanager
def _patched(target, name, value):
    old = getattr(target, name)
    setattr(target, name, value)
    try:
        yield
    finally:
        setattr(target, name, old)


def _wrong_budget(eta, x_lim):
    z = 2 * math.sqrt(2) / math.sqrt(x_lim)
    return z * 2 * math.sin(eta / 2)**2, z * eta


_ORIG_PROFILE = SF._profile


def _smooth_as_power(kind, xv, g2=0.0):
    if kind[0] == "smooth":
        c, lam = SF.DT_C, 0.4
        return (c * xv**lam + g2 * xv, c * lam * xv**(lam - 1) + g2, c * lam * (lam - 1) * xv**(lam - 2),
                c * lam * lam * xv**lam + g2 * xv)
    return _ORIG_PROFILE(kind, xv, g2)


_ME = sys.modules[__name__]
MUTANTS = [
    ("C1", "chart shift 2 -> 1 (t = v + sqrt2/u)", lambda: _patched(_ME, "CHART_SHIFT", 1), ("chart",)),
    ("C2", "ef_metric's g_vu = sqrt2 alpha^2 -> 2 alpha^2", lambda: _patched(_ME, "G_VU", sp.Integer(2)), ("chart",)),
    ("C3", "g_vv = -alpha^2 u^2/2 -> -alpha^2 u/2 (a non-degenerate horizon at u = 0)",
     lambda: _patched(_ME, "GVV_POWER", 1), ("horizon",)),
    ("C4", "ef_metric's g_vu sign flipped (-sqrt2 alpha^2)", lambda: _patched(_ME, "G_VU", -sp.sqrt(2)), ("one_way",)),
    ("C5", "the throat ODE's 2pq -> 3pq in the nine fits", lambda: _patched(_ME, "KASNER_MUT", 1.0), ("kasner",)),
    ("C5", "the constraint's 4pq -> 3pq in the leading balance", lambda: _patched(_ME, "KASNER_CONS_PQ", 3),
     ("kasner",)),
    ("C6", "the Kasner tail counted twice in eta_of (the first version's double count)",
     lambda: _patched(_ME, "ETA_TAIL_COUNT", 2), ("eta",)),
    ("C6", "the control run on the unmutated ODE (no exponent-1 profile)", lambda: _patched(_ME, "ETA_CONTROL_MUT", 0.0),
     ("eta",)),
    ("C7", "the conformal AdS2 radius 2 -> 1", lambda: _patched(_ME, "ADS2_R2", 1), ("jminus",)),
    ("C8", "a layer at K = 1e33 K_bs added to the claimed rows", lambda: _patched(_ME, "F_LAYERS", F_LAYERS + (1e33,)),
     ("budgets",)),
    ("C9", "budget()'s bracket -> [z 2 sin^2(eta/2), z eta]", lambda: _patched(_ME, "budget", _wrong_budget),
     ("budgets",)),
    ("C10", "the coinciding limit taken at depth 1e-3 y_s, not 0", lambda: _patched(_ME, "COINCIDE_FRAC", 1e-3),
     ("coincide",)),
    ("C11a", "P2's profile amplitude c = 0.05 -> 50 (sim2_facing.DT_C)", lambda: _patched(SF, "DT_C", 50.0), ("slab",)),
    ("C11b", "the smooth family's sqrt(x) -> x^0.4", lambda: _patched(SF, "_profile", _smooth_as_power), ("frame",)),
    ("C12", "eq. (17) replaced by Schwarzschild on the plane", lambda: _patched(_ME, "PLANE_DATA", "schw"), ("eq",)),
    ("C13", "p(0) moved with q(0) held at -e (off the constraint surface)",
     lambda: _patched(_ME, "DATA_CONSTRAINED", False), ("data",)),
    ("C14", "a key 'arrival_hold' added to the output", lambda: _patched(_ME, "INJECT_KEY", "arrival_hold"),
     ("inject",)),
    ("C15-C19", "the owner epass_pairing.py missing (its path pointed at an absent file)",
     lambda: _patched(_ME, "OWNER_PATHS",
                      {**OWNER_PATHS, "epass_pairing": os.path.join(HERE, "absent_epass_pairing.py")}),
     ("own_pairing",)),
    ("C15-C19", "the owner's own ZERO_TOL 1e-12 -> -1 (its checks then fail, and its selftest returns False)",
     lambda: _owner_patched("epass_pairing", "ZERO_TOL", -1.0), ("own_pairing",)),
    ("C26-C31", "the owner epass_frames.py missing (its path pointed at an absent file)",
     lambda: _patched(_ME, "OWNER_PATHS",
                      {**OWNER_PATHS, "epass_frames": os.path.join(HERE, "absent_epass_frames.py")}),
     ("own_frames",)),
    ("C26-C31", "the owner's own SI_TOL 1e-5 -> 0 (its C26b then fails)",
     lambda: _owner_patched("epass_frames", "SI_TOL", 0.0), ("own_frames",)),
    ("C35a", "the frames owner's item-155 energy 3.8e22 -> 3.9e22 J, its cached output cleared (three quoted values, E, "
     "m and 1/(2m) at item 155, are then no longer the owner's)",
     lambda: _owner_patched("epass_frames", "E_ITEM155", 3.9e22, clear=True), ("x11",)),
    ("C35b", "X15 dropped from the deferred list (a [PLANE] section counted as built)",
     lambda: _patched(_ME, "DEFERRED", {k: v for k, v in DEFERRED.items() if k != "X15"}), ("x11",)),
    ("C35b", "a row drawing on the cap (X22, deferred) added to X25's table",
     lambda: _patched(_ME, "X25_EXTRA", ({"row": "R1", "config": "the cap", "tag": "[PLANE]", "G1": "near the throat",
                                         "G2": "at the throat", "G3": "fails at O(x)", "G4": "nothing crosses",
                                         "verdict": "held configuration, not a passage", "sources": ("X22",),
                                         "deferred_parts": ()},)), ("x11",)),
    ("C35b", "'E-PASS is refuted within one universe' planted in X25's combined answer",
     lambda: _patched(_ME, "X25_PLANT", "E-PASS is refuted within one universe."), ("x11",)),
    ("C35b", "'E-PASS is refuted, not merely OPEN' planted (a negator after the verdict, not before it)",
     lambda: _patched(_ME, "X25_PLANT", "E-PASS is refuted, not merely OPEN."), ("x11",)),
    ("C35b", "'The pair, summed, is positive' planted (commas between the total and the word)",
     lambda: _patched(_ME, "X25_PLANT", "The pair, summed, is positive."), ("x11",)),
    ("C35b", "the frames owner's output absent while its file is present (X17 and X18 then have no owner rows' content, "
     "so they are not built)",
     lambda: _patched(_ME, "owner_output", _output_absent_for("epass_frames")), ("x11",)),
]


def _output_absent_for(absent):
    """C35b's mutation: owner_output() returning None for one owner (its rows then carry no content)."""
    orig = owner_output

    def patched(name):
        return None if name == absent else orig(name)
    return patched


@contextlib.contextmanager
def _owner_patched(name, attr, value, clear=False):
    """A mutation of an owner's own input (the owner loaded by path): set, and restore after; clear=True empties the
    owner's cached output before and after, so its compute() runs under the mutation."""
    mod = owner_module(name)
    caches = [c for c in (getattr(mod, "_OUT", None), getattr(mod, "_OUT_CACHE", None)) if isinstance(c, dict)]
    old = getattr(mod, attr)
    setattr(mod, attr, value)
    if clear:
        for c in caches:
            c.clear()
    try:
        yield
    finally:
        setattr(mod, attr, old)
        if clear:
            for c in caches:
                c.clear()


def owner_mutants_start():
    """Each owner's own --mutants, as a subprocess (python, by path), started so it runs beside this file's own."""
    procs = {}
    for name, path in OWNER_PATHS.items():
        fh = tempfile.TemporaryFile(mode="w+")
        procs[name] = (subprocess.Popen([sys.executable, path, "--mutants"], stdout=fh, stderr=subprocess.STDOUT,
                                        cwd=HERE), fh)
    return procs


def owner_mutants_collect(procs):
    """Each owner's --mutants count, read from its own final line (epass_pairing: 'mutants: N run, K caught, P passed';
    epass_frames: 'mutants: K/N mutations make their check fail'), and its exit code."""
    res = {}
    for name, (proc, fh) in procs.items():
        rc = proc.wait()
        fh.seek(0)
        txt = fh.read()
        fh.close()
        if name == "epass_pairing":
            m = re.search(r"mutants: (\d+) run, (\d+) caught, (\d+) passed", txt)
            n_run, n_caught = (int(m.group(1)), int(m.group(2))) if m else (None, None)
        else:
            m = re.search(r"mutants: (\d+)/(\d+) mutations make their check fail", txt)
            n_caught, n_run = (int(m.group(1)), int(m.group(2))) if m else (None, None)
        res[name] = {"exit": rc, "run": n_run, "caught": n_caught,
                     "line": m.group(0) if m else (txt.strip().splitlines() or ["(no output)"])[-1],
                     "ok": rc == 0 and n_run is not None and n_run > 0 and n_caught == n_run}
    return res


def _clear():
    _TB.clear()
    _ETA.clear()


def mutants():
    """For every check, its named mutation(s) of the instrument's own input: recompute the sections the check reads
    under the mutation and require the check to FAIL.  A mutation under which the computation raises is reported as
    ERROR and is not counted as killed.  Then each owner's own --mutants (a subprocess, started first so it runs
    beside these) is collected and its count reported.  Returns True when the unmutated checks pass, every mutation is
    killed and both owners' --mutants catch every one of theirs."""
    procs = owner_mutants_start()
    base = compute()
    base_ok = {cid: good for cid, _, good, _ in checks(base)}
    print("unmutated: " + ", ".join(f"{cid} {'PASS' if g else 'FAIL'}" for cid, g in base_ok.items()))
    killed_all = all(base_ok.values())
    covered = set()
    for cid, name, patch, secs in MUTANTS:
        _clear()
        note, errored = "", False
        try:
            with patch():
                part = compute(only=secs)
                merged = dict(base)
                for k_, v_ in part.items():
                    merged[k_] = {**base["eq"], **v_} if k_ == "eq" else v_
                good = {c_: g for c_, _, g, _ in checks(merged)}[cid]
        except Exception as ex:          # a crash shows nothing about the check: ERROR, not a kill (and exit 1)
            good, errored, note = None, True, f"(raised {type(ex).__name__}: {ex})"
        _clear()
        covered.add(cid)
        killed_all = killed_all and not errored and not good
        tag = "ERROR   " if errored else ("KILLED  " if not good else "SURVIVED")
        print(f"  {tag}  {cid}  {name}  {note}")
    missing = sorted(set(base_ok) - covered)
    if missing:
        print("  checks without a mutation:", missing)
        killed_all = False
    n_k = sum(1 for _ in MUTANTS)
    print(f"mutants: {'all ' + str(n_k) + ' killed' if killed_all else 'NOT all killed'}; every check has a mutation: "
          f"{not missing}")
    own = owner_mutants_collect(procs)
    for name, r in own.items():
        print(f"  owner {name}.py --mutants (its own, run by path as a subprocess): {r['caught']}/{r['run']} caught, "
              f"exit {r['exit']} -- '{r['line']}'")
    owners_ok = all(r["ok"] for r in own.values())
    print(f"owners' --mutants: {'all caught' if owners_ok else 'NOT all caught'} "
          f"({sum(r['caught'] or 0 for r in own.values())}/{sum(r['run'] or 0 for r in own.values())})")
    return killed_all and owners_ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    o = compute()
    report(o)
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w") as fh:
            json.dump(o, fh, indent=1, default=str)
