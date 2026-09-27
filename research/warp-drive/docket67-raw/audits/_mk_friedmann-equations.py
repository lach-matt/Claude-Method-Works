import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
rep = {
 "key": "friedmann-equations",
 "name": "Friedmann constraint and acceleration (Raychaudhuri-form) equations for FLRW",
 "source": {
  "located": "Classic: A. Friedmann, Z. Phys. 10 (1922) 377 (k>0, dust, Lambda) and Z. Phys. 21 (1924) 326 (k<0); pressure added by Lemaitre (1927) -- no arXiv copy, NAMED-NOT-READ. Read through two exact arXiv restatements: (i) S. M. Carroll, 'Lecture Notes on General Relativity', gr-qc/9712019v1 (1997), printed pp.220-223 (pdf 227-230): FLRW Ricci (8.13), R (8.14), perfect fluid T^mu_nu = diag(-rho,p,p,p) with U^mu = (1,0,0,0) (8.15)-(8.18), energy conservation 0 = nabla_mu T^mu_0 = -d_0 rho - 3(adot/a)(rho+p) (8.20), p = w rho with 'w is a constant independent of time' (8.21)-(8.23), Lambda as the w = -1 fluid rho = -p = Lambda/(8 pi G) (8.29)-(8.31), and the Friedmann equations (8.35) addot/a = -(4 pi G/3)(rho+3p), (8.36) (adot/a)^2 = (8 pi G/3) rho - k/a^2; (ii) G. F. R. Ellis & H. van Elst, 'Cosmological models (Cargese lectures 1998)', gr-qc/9812046v5, p.13 sec 2.5 and p.22 sec 4.2 eqs (106)-(107).",
  "read_status": "READ-VIA-RESTATEMENT",
  "via": "alphaXiv page text of gr-qc/9712019v1 (pdf 227-230) from the session harvest " + D + "/src/gr-qc_9712019.alphaxiv_pages.json; alphaXiv page text of gr-qc/9812046v5 (pp.1,2,7,9,10,12,13,15,18,19,21-26,35,37,38,46,71,74,78,79) harvested verbatim this stage from earlier DOCKET-67 workflow transcripts of session 6d820e7d into " + D + "/src/gr-qc_9812046.harvest.txt (each page tagged with its transcript file and line). This stage's own alphaXiv calls (answer_pdf_queries x1 on gr-qc/9812046, discover_papers x2) returned 'alphaXiv assistant quota exceeded'. Friedmann 1922/1924 and Lemaitre 1927: NAMED-NOT-READ. Owner re-read at HEAD b8b929b: permute.py:99-120, 279-332, 445-463, 499-512."
 },
 "published_statement": "Carroll gr-qc/9712019 p.223: 'The mu nu = 00 equation is -3 addot/a = 4 pi G(rho + 3p), (8.33) and the mu nu = ij equations give addot/a + 2(adot/a)^2 + 2k/a^2 = 4 pi G(rho - p). (8.34) ... We can use (8.33) to eliminate second derivatives in (8.34), and do a little cleaning up to obtain addot/a = -(4 pi G/3)(rho + 3p), (8.35) and (adot/a)^2 = (8 pi G/3) rho - k/a^2. (8.36) Together these are known as the Friedmann equations, and metrics of the form (8.7) which obey these equations define Friedmann-Robertson-Walker (FRW) universes.' Ellis & van Elst gr-qc/9812046v5 p.22 sec 4.2: 'The remaining non-trivial equations are the energy equation (37), the Raychaudhuri equation (29), which now takes the form 3 Sddot/S + (1/2)(mu + 3p) = 0, (106) and the Friedmann equation that follows from (55): 3R = 2mu - (2/3)Theta^2 = 6k/S^2, (107) where k is a constant. Any two of these equations imply the third if Sdot != 0 (the latter equation being a first integral of the other two).' p.13: 'when omega_a = 0, the generalised Friedmann equation (55) is an integral of the Raychaudhuri equation (29) and energy equation (37).'",
 "published_hypotheses": [
  "General relativity: Einstein's field equations G_mu_nu = 8 pi G T_mu_nu (- Lambda g_mu_nu), Levi-Civita connection (Carroll 8.29, 8.32; Ellis-van Elst eq.(1)-(2): 'the twice-contracted Bianchi identities which, by Einstein's field equations (1), imply the conservation equations (2)', p.10)",
  "FLRW metric: spatially homogeneous and isotropic, ds^2 = -dt^2 + a^2(t)[dr^2/(1-kr^2) + r^2 dOmega^2], k a constant (Carroll 8.7, 8.12-8.14; Ellis-van Elst (107) 'where k is a constant')",
  "Perfect fluid comoving with the cosmic frame, U^mu = (1,0,0,0), T^mu_nu = diag(-rho,p,p,p) (Carroll 8.15-8.18); Ellis-van Elst: perfect fluid with p = p(mu), sums of such fluids, or a scalar field (p.22)",
  "Equation of state (for integrating continuity): p = w rho, 'w is a constant independent of time' (Carroll 8.21) -- not needed for the Friedmann pair itself",
  "Cosmological constant: equivalent to a vacuum fluid rho = -p = Lambda/(8 pi G), w = -1 (Carroll 8.29-8.31)",
  "Interdependence: the energy equation, Raychaudhuri equation and Friedmann equation -- 'any two ... imply the third if Sdot != 0' (Ellis-van Elst p.22); the Friedmann equation is a first integral (integration constant k) of the other two; in the general 1+3 setting this requires vorticity omega_a = 0 (p.13), automatic in FLRW"
 ],
 "hypothesis_drift": [
  "NONE DROPPED on the direction the tree uses. The source's one conditional hypothesis (Ellis-van Elst p.22, 'if Sdot != 0') attaches to the direction constraint + continuity => acceleration; the tree uses constraint + acceleration => continuity (permute.py:115-116, 290-297), which is a polynomial identity in (a, adot, k, w) with no division by adot (rederive C3b, C3d; z3 C5a unsat with vacuity guard C5b sat). The condition is shown necessary for the other direction by a static counterexample (C4b: a = 1, k = 1/4, w = 1/3 satisfies constraint and continuity, violates acceleration).",
  "UNITS (permute.py:280, 285-287): 8 pi G/3 = 1 => 4 pi G/3 = 1/2, so addot = -(1/2)(rho + 3p) a -- exactly permute._accel's -0.5*(rho + 3*w*rho)*a (C1g). No drift.",
  "LAMBDA (canonical hypothesis 'Lambda set to zero except as the w = -1 fluid'): identical to Carroll 8.29-8.31 (C1h). No drift.",
  "EQUATION OF STATE (permute.py:115-117, 445-451 fixture w in {1/3, 0, -1, -1/3}): the tree uses constant w; the source allows p = p(mu); the identity the tree measures holds for ANY pressure P, barotropic or not (C3c). The tree's class is narrower than the source's -- not a drift against the source.",
  "CURVATURE NORMALISATION (permute.py:117, 300-303): k = 0, +/-1/4 with a0 = 1 is a rescaling of Carroll's k in {-1,0,+1}; the equations are invariant under a -> lambda a, k -> lambda^2 k. The fixture's adot0 = sqrt(1 - k) a0 requires 1 - k/a0^2 > 0, and the code raises ValueError otherwise (permute.py:302-303). No drift.",
  "GR / EINSTEIN EQUATIONS: not listed among the canonical hypotheses, but the owner states it (permute.py:107 'Couple it to Einstein's equation and it FORCES grad_mu T^mu-nu = 0'). Kept implicitly; named here so it is not lost: minimally coupled matter, Levi-Civita connection, no modified gravity.",
  "EVIDENTIAL STATUS, owner permute.py:115-120 ('MEASURED HERE ... It holds anyway, at 1e-16 ... the residual DOES NOT FALL WITH STEP SIZE ... The flatness is the evidence'): the residual is an algebraic identity at EVERY phase-space point, on or off a trajectory -- 20,000 random (a, adot, k, w) points give the same rounding-level residual with no integration at all (C6c, worst 1.1e-13 scaled; tree fixture worst 7.2e-16, C6a; 500 vs 8000 steps 6.0e-16 vs 5.9e-16, C6b). So the RK4 integration does no work and the dt-flatness would appear for any integrator. This is consistent with the owner's own words ('AN IDENTITY DOES NOT' shrink) and is recorded as a named qualifier, not a drift against the tree: what the flatness evidences is the FLRW algebraic identity, not a numerical property of the trajectory.",
  "SCOPE, owner permute.py:103-107 and scorecard 509-510 ('the contracted Bianchi identity, measured at 1e-16 and flat in dt'): the demonstration covers the FLRW reduction only -- a one-function family a(t) with constant k, where nabla_mu G^mu_0 = 0 is the single non-trivial component (C2a, C2b). It is a special case of, not evidence for, the 'every metric' statement at permute.py:105-106; that general statement is audited separately (contracted-bianchi-identity: NARROWED, for the Levi-Civita/smoothness hypotheses it drops)."
 ],
 "data_at_publication": [
  {
   "quantity": "Newton's G (and c)",
   "value_then": "enters only as the unit convention 8 pi G/3 = 1, c = 1 (permute.py:280)",
   "value_now": "CODATA 2022 G = 6.67430(15)e-11 m^3 kg^-1 s^-2 (not re-read this stage)",
   "source_now": "not needed: G is absorbed into the units",
   "moves_conclusion": "No, computed: the residual rhodot + 3H(rho+p) is identically zero for every value of the coupling (C1e-C1g carry G symbolically; C3b in the tree's units)."
  },
  {
   "quantity": "fixture initial data a0, adot0",
   "value_then": "a0 = 1, adot0 = sqrt(1 - k) (so rho0 = 1), k in {0, +1/4, -1/4}, w in {1/3, 0, -1, -1/3}, tmax = 0.30, steps 500..8000 (permute.py:300-328, 445-459)",
   "value_now": "same (fixture, not a measurement)",
   "source_now": "permute.py at HEAD b8b929b",
   "moves_conclusion": "No, computed: the identity holds at 20,000 random (a, adot, k, w) points (C6c) and for arbitrary P (C3c); no choice of initial data can make it fail (z3 C5a unsat over all a > 0, adot, k, p)."
  },
  {
   "quantity": "equation of state w (constant) vs evolving dark energy",
   "value_then": "Carroll 1997: w constant (8.21); Lambda = w = -1 (8.31)",
   "value_now": "DESI DR2 (2503.14738v3, READ from the session cache src/casmag/all/2503.14738v3.txt): w0waCDM with w0 > -1, wa < 0 'preferred over LCDM at 3.1 sigma for ... DESI BAO and CMB', '2.8 - 4.2 sigma depending on which SNe sample'; the same paper states 'Assuming that general relativity (GR) correctly describes the dynamics of expansion, the evolution of H(z) is governed by the Friedmann equation'",
   "source_now": D + "/src/casmag/all/2503.14738v3.txt lines 498-507, 818-828",
   "moves_conclusion": "No, computed: constraint + acceleration => continuity holds for any pressure history P(t), barotropic or not (C3c); an evolving w changes rho(a), not the identity."
  },
  {
   "quantity": "H_0 (context only; not an input of this result)",
   "value_then": "Carroll 1997 p.223: 'measurements falling in the range of 40 to 90 km/sec/Mpc'; Friedmann 1922 had no expansion measurement at all",
   "value_now": "Planck 2018 67.36 +/- 0.54; SH0ES 73.04 +/- 1.04; DESI DR2+BBN 68.51 +/- 0.58 (all READ by sibling stage audits/1807.06209.json)",
   "source_now": D + "/audits/1807.06209.json",
   "moves_conclusion": "No: H_0 does not enter the Friedmann pair or the continuity identity; the fixture is dimensionless."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/friedmann-equations.py",
  "outcome": "22/22 PASS, exit 0 (sympy 1.14.0, z3 5.1.0). C1a-h: Christoffels, Ricci and Einstein tensor of FLRW computed from the metric reproduce Carroll (8.13), (8.14), (8.35), (8.36); in units 8piG/3 = 1 the acceleration coefficient is exactly the tree's 1/2; Lambda equals the w = -1 fluid. C2a-b: nabla_mu G^mu_0 = 0 identically for arbitrary a(t), k -- the FLRW reduction of the contracted Bianchi identity -- so rho_G, p_G read off G^mu_nu obey continuity for any a(t). C3a: the tree's rhodot formula (permute.py:293-297) equals the chain-rule derivative of the constraint along the flow. C3b-d: constraint + acceleration => continuity is a polynomial identity in (a, adot, k, w), and in (a, adot, k, P) for arbitrary pressure, with no adot != 0 condition. C4a: acceleration + continuity make adot^2 - rho a^2 a constant of motion (= -k): the constraint is a first integral, as Ellis-van Elst say. C4b-c: constraint + continuity imply acceleration only when adot != 0 -- static counterexample a=1, k=1/4, w=1/3 -- which is exactly the source's 'if Sdot != 0'. C5a-b: z3 finds no a > 0, adot, k, p violating continuity when built from the tree's raw formulas (unsat); vacuity guard with coefficient 0.49 is sat. C6a-c: the tree's own functions (permute.py imported read-only) give worst scaled residual 7.2e-16 over 4 fluids x 3 curvatures, 6.0e-16 at 500 steps vs 5.9e-16 at 8000, and <=1.1e-13 at 20,000 random off-trajectory phase-space points.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "G. F. R. Ellis & H. van Elst, 'Cosmological models (Cargese lectures 1998)', gr-qc/9812046v5",
   "effect": "confirms",
   "what": "States the three FLRW equations and their interdependence: 'Any two of these equations imply the third if Sdot != 0 (the latter equation being a first integral of the other two)' (p.22); in the general 1+3 case the generalised Friedmann equation is an integral of Raychaudhuri + energy only when omega_a = 0 (p.13). Adds the Sdot != 0 condition, which C4b shows is necessary for one direction and C3d shows is not needed for the direction the tree uses.",
   "read_status": "READ (alphaXiv page text harvested from session transcripts, pp.13, 22)"
  },
  {
   "ref": "DESI Collaboration, 'DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints', arXiv 2503.14738v3 (2025)",
   "effect": "confirms",
   "what": "Uses the Friedmann equation as the background law 'assuming that general relativity (GR) correctly describes the dynamics of expansion' and reports a 2.8-4.2 sigma preference for evolving dark energy (w0 > -1, wa < 0). Evolving w is inside the class where the tree's identity holds (C3c: any P(t)); it questions LCDM's matter content, not the Friedmann equations' derivation.",
   "read_status": "READ (session cache src/casmag/all/2503.14738v3.txt, lines 498-507, 818-828)"
  },
  {
   "ref": "K. Enqvist, 'Lemaitre-Tolman-Bondi model and accelerating expansion', arXiv 0709.2044v1 (2007)",
   "effect": "narrows",
   "what": "Applicability, not validity: for the real inhomogeneous universe, averaging gives 'averaged, effective Einstein equations which, in addition to the terms found in the usual homogeneous case, include new terms that represent the effect of the inhomogeneities' (backreaction; Buchert GRG 32 (2000) 105, NAMED-NOT-READ). The Friedmann equations are exact for FLRW; whether our universe's averages obey them is an empirical question. The tree uses FLRW as an exact model (permute.py:115-117), so this does not narrow the use.",
   "read_status": "READ (session cache src/casmag/all/0709.2044v1.txt, pp.1-4)"
  },
  {
   "ref": "Later-literature discovery call (discover_papers) for work contradicting or extending the continuity/Friedmann interdependence (modified gravity, matter non-conservation, Rastall/unimodular, backreaction)",
   "effect": "contested",
   "what": "NOT RUN: both discover_papers calls returned 'alphaXiv assistant quota exceeded'. Theories that relax nabla_mu T^mu_nu = 0 (e.g. Rastall, unimodular with non-conserved T) change the field equations, i.e. drop the GR hypothesis named above; none was READ this stage, so no claim about them is made.",
   "read_status": "NAMED-NOT-READ (tool quota)"
  }
 ],
 "lacked_data": "What the authors lacked: Friedmann (1922/1924) had no expansion measurement (Hubble 1929), no CMB, no dark energy, and treated dust (pressure added by Lemaitre 1927 -- both NAMED-NOT-READ); Carroll (1997) quotes H_0 as 40-90 km/s/Mpc and predates the 1998 acceleration discovery; nobody before 2025 had DESI's evolving-w preference. Does having it change the conclusion? No, and the evidence is computed rather than presumed: the Friedmann equations are consequences of Einstein's equations plus FLRW symmetry plus a perfect-fluid source (C1a-f, from the metric), and the only property the tree rests on -- constraint + acceleration => continuity -- is an algebraic identity valid for every value of G, every a(t), every k, and every pressure history P(t) (C2, C3b-c, z3 C5a). No datum enters it, so no moved datum can move it. What data CAN do is test whether our universe satisfies the hypotheses (GR, homogeneity/isotropy, perfect fluid, Lambda vs evolving w): DESI DR2's 2.8-4.2 sigma evolving-w preference (READ) and the backreaction debate (Enqvist, READ) bear on applicability to the real universe, not on the theorem, and the tree uses it as an exact FLRW model. Evidence against M's hypothesis here: the source's own later restatement (Ellis-van Elst) ADDS a hypothesis (Sdot != 0) that sharpens rather than overturns, and C4b shows it matters only for a direction the tree does not use.",
 "grade": "STANDS",
 "grade_evidence": "Statement: the tree's _rho and _accel (permute.py:279-287) are Carroll (8.36) and (8.35) in units 8piG/3 = 1, re-derived here from the FLRW metric (C1a-g). Hypotheses: every one the tree uses (FLRW, curvature k, perfect fluid p = w rho, Lambda as the w = -1 fluid, 8piG/3 = 1, c = 1) is a source hypothesis; none dropped; GR is implicit and stated by the owner at permute.py:107. The source's conditional 'if Sdot != 0' (Ellis-van Elst p.22) attaches only to constraint + continuity => acceleration (necessary there: C4b); the tree's direction constraint + acceleration => continuity holds unconditionally, as a polynomial identity (C3b-d), machine-checked by z3 over all reals with a > 0 (C5a unsat, vacuity guard C5b sat). Re-derivation agrees (22/22). Data: no datum enters; G is a unit, the fixture is dimensionless, and the identity holds at arbitrary phase-space points and for arbitrary P(t) (C3c, C6c), so DESI's evolving w and the H_0 tension do not move it. Named qualifiers, not over-represented in either direction: (i) the '1e-16 ... flat in dt' measurement (permute.py:115-120) evidences a POINTWISE algebraic identity -- the integrator does no work (C6c) -- consistent with the owner's own 'an identity does not [shrink]'; (ii) the demonstration is the FLRW reduction of the contracted Bianchi identity (C2a-b), not evidence for the 'every metric' statement at permute.py:105-106, which is graded separately (contracted-bianchi-identity.json: NARROWED); (iii) applicability to the real, inhomogeneous universe is an empirical question (backreaction, Enqvist 0709.2044) that the tree does not claim. The classic sources Friedmann 1922/1924 and Lemaitre 1927 are NAMED-NOT-READ; the grade rests on the READ restatements and on the independent derivation from the metric.",
 "what_would_change_the_grade": "NARROWED if the tree used the converse (constraint + continuity => acceleration) through a turning point adot = 0 (C4b), or applied the pair outside GR/FLRW/perfect fluid (e.g. with anisotropic stress, vorticity, a non-minimally coupled field, or averaged inhomogeneous cosmology with backreaction), or cited the FLRW demonstration as proof of the general-metric Bianchi identity. WRONG only if a (a, adot, k, P) with a > 0 violating the continuity identity were exhibited -- z3 C5a says none exists. OPEN would apply if the restatements could not be read; they were (harvested alphaXiv page text), though the 1922/1924 originals remain NAMED-NOT-READ and a direct read of an English translation (GRG 31 (1999) 1991, no arXiv copy) would upgrade the source status without, by C1, changing the grade.",
 "reverify_command": "cd /tmp && PYTHONDONTWRITEBYTECODE=1 python3 " + D + "/rederive/friedmann-equations.py  # expect 22 checks, ALL PASS, exit 0; then: grep -n 'Any two of these equations imply the third' " + D + "/src/gr-qc_9812046.harvest.txt  # expect one hit (p.22); cd /home/user/Claude-Method-Works && git status --short research  # expect clean",
 "report_path": D + "/audits/friedmann-equations.json"
}
json.dump(rep, open(D + "/audits/friedmann-equations.json", "w"), indent=1)
print("ok")
