import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
rep = {
 "key": "thin-shell-conservation-law",
 "name": "Surface energy conservation for the thin shell: sigma' = -(2/R)(sigma + p), m_s' = -8 pi R p",
 "source": {
  "located": "PRIMARY: E. Poisson & M. Visser, 'Thin-shell wormholes: Linearization stability', arXiv:gr-qc/9506083v1 (30 Jun 1995), PRD 52, 7318 (1995) -- the citation wall.py:222 gives -- eqs (8), (11)-(13), (15), (16), (21). CONDITION FOR THE NO-FLUX FORM: M. Ishak & K. Lake, arXiv:gr-qc/0108058v2 (2001), PRD 65, 044011, eqs (6)-(8) (transparency [G^a_b n_a u^b] = 0) and (12) with sec. II.C ('precisely the condition that guarantees (6) at equilibrium'; away from equilibrium dc/dr = 0, 'static embeddings in the neighborhood of Sigma'). SAME CONFIGURATION AS THE TREE (Minkowski in / Schwarzschild out): Pitre, Schneider & Poisson, arXiv:2604.05980v1 (2026) sec. II p.8: 'We assume that there is no matter inside and outside the shell ... it can be shown -- see Eq. (21) of Ref. [22] [Israel 1966] -- that the conservation statement D_b S^ab = 0 is compatible with the assignment of Eq. (2.10b).' THE TREE'S TARGET OBJECT: A. T. Le, arXiv:2606.22531v3, p.2. Israel 1966 (Nuovo Cimento 44B 1, eq 21) and Lanczos 1924 are pre-arXiv: NAMED-NOT-READ, restated in PV eqs (3)-(8) and PSP eqs (2.8), (2.10).",
  "read_status": "READ",
  "via": "alphaXiv page text. The alphaXiv quota was exhausted in THIS stage (answer_pdf_queries, get_paper_content and discover_papers all returned 'quota exceeded'), so the texts were read from the verbatim alphaXiv page-text cache harvested earlier in this workflow: scratchpad/d67/src/casmag/all/gr-qc_9506083v1.txt (all 4 pages), gr-qc_0108058v2.txt (pp.1-4), 2604.05980v1.txt (pp.1-9, conservation passage p.8), 2606.22531v3.txt (p.2). Every quotation below is from those files. Israel 1966 itself: NAMED-NOT-READ (READ-VIA-RESTATEMENT in PV and PSP)."
 },
 "published_statement": "Poisson-Visser (gr-qc/9506083 v1) p.2, for a thin shell of Schwarzschild-vacuum on both sides: sigma = -(1/4 pi)[K^theta_theta], p = +(1/8 pi)([K^tau_tau] + [K^theta_theta]) (8); sigma = -(1/2 pi a) sqrt(1 - 2M/a + adot^2) (11); p = (1/4 pi a)(1 - M/a + adot^2 + a addot)/sqrt(1 - 2M/a + adot^2) (12); 'It is easy to check that these imply energy conservation: d/dtau (sigma A) + p d/dtau A = 0, (13) where A = 4 pi a^2. In this equation, the first term corresponds to a change in the throat's internal energy, while the second term corresponds to the work done by the throat's internal forces.' Recast: 'sigmadot = -2(sigma + p) adot/a (15). If we choose a particular equation of state, in the form p = p(sigma), then we can formally integrate the conservation equation and obtain ln(a) = -(1/2) INT dsigma/(sigma + p(sigma)) (16)'; and '[sigma(a) a]' = -(sigma + 2p) (21)'. Ishak-Lake (gr-qc/0108058) p.2: 'we use the transparency condition [G^alpha_beta n_alpha u^beta] = 0 (6)'; it gives (M/2R)'' = Upsilon/(2R^3)(1 + 2P'/sigma') with Upsilon = 8 pi R^2 (sigma + P) (7)-(8); m = m(R) (12) 'is precisely the condition that guarantees (6) at equilibrium. For (6) to hold away from equilibrium it follows that dc/dr = 0 ... For timelike Sigma then our assumptions require static embeddings in the neighborhood of Sigma.' Pitre-Schneider-Poisson (2604.05980) p.8: Minkowski inside, Schwarzschild outside, 'no matter inside and outside the shell', D_b S^ab = 0 compatible with the Israel condition (Israel eq 21).",
 "published_hypotheses": [
  "H1 thin (distributional) shell; the surface stress S^i_j follows from the jump [K_ij] by the Lanczos/Israel condition (PV eqs 3-8; PSP eq 2.10b)",
  "H2 spherical symmetry (PV sec. II-III; IL sec. II.A)",
  "H3 VACUUM on both sides -- PV derive (13) from (11)-(12) for Schwarzschild/Schwarzschild; PSP p.8 'no matter inside and outside the shell'; IL eq (6) transparency [G n u] = 0 with static embeddings near Sigma (eq 12, sec. II.C). Equivalently no energy flux across the shell; the general Israel identity carries a flux term otherwise (restated, Israel eq 21 NAMED-NOT-READ)",
  "H4 the ENERGY component only: (13) is the tau-component of D_b S^ab = 0; the theta-component (Euler) is identically satisfied in spherical symmetry",
  "H5 for the integrated form (16): a barotropic EOS p = p(sigma) (PV p.2); PV do NOT assume it linear -- they linearise only through beta^2 = dp/dsigma at sigma0 (eq 23)",
  "H6 sigma + p != 0 where (16) is inverted (the integrand 1/(sigma+p)); IL sec. II.D: Upsilon = 0 (sigma = -P, 'domain wall') is a separate case"
 ],
 "hypothesis_drift": [
  "KEPT, WIDENED LEGITIMATELY -- UNEQUAL MASSES: PV derive (13) only for two Schwarzschild exteriors of the same M (the wormhole). The tree (wall.py:222-224) uses Minkowski inside (M_in = 0), Schwarzschild outside. Re-derived here from the Israel condition for arbitrary static vacuum f_in = 1-2M_in/R, f_out = 1-2M_out/R: d(sigma A)/dtau + p dA/dtau = 0 IDENTICALLY in (R, Rdot, Rddot, M_in, M_out) (checks 1a, 1b); PSP 2026 p.8 states it for exactly the tree's configuration. No drift in substance; the citation 'Poisson-Visser' for the Minkowski/Schwarzschild case is a widening PV do not print, not an error.",
  "KEPT, AND NAMED BY THE TREE -- VACUUM ON BOTH SIDES (H3): wall.py:222-223 'Minkowski inside, Schwarzschild outside' and wall.py:198-200 '2. Not the flux-coupled dynamic stability of the RADIATING shell, which Le leaves open in his Sec. 15. What is closed here is the frozen-background linear radial mode'. The hypothesis is load-bearing for the object wall.py discusses: Le 2606.22531v3 p.2 matches his shell 'using the standard Lanczos junction together with flux-source balance laws [26, 27]: the timelike-shell balance laws with an external crossing flux, mandatory here because the exterior radiation is emitted at the shell'. So m_s' = -8 pi R p is exact for the frozen Minkowski/Schwarzschild anchor (wall.py:125 'LE'S STATIC ANCHOR EXACTLY') and NOT for Le's radiating warpshell; the tree says so at 198-200. Not dropped; scope carried.",
  "ADDED (a restriction, stated) -- LINEAR EOS: PV integrate (16) for general p(sigma) and linearise only at sigma0. wall.py:225-227 and 316-317 adopt p = p0 + beta^2 (sigma - sigma0) GLOBALLY to get the closed form sigma(R) = (sigma0 + K/A)(R/R0)^{-2A} - K/A. For V(R0), V'(R0), V''(R0) and the linear period this is no loss: only beta^2 at sigma0 enters to second order (checks 3a, 7b). The closed form also silently requires A = 1 + beta^2 != 0 (H6's degenerate case): at beta^2 = -1 the solution is logarithmic, sigma = sigma0 - 2(sigma0+p0) ln(R/R0) (check 4d) and wall.sigma_of_R raises ZeroDivisionError (check 4e); wall.py never calls it there (all its beta^2 >= 0). Recorded, not grade-moving.",
  "WEAKENED SCOPE IN A DOWNSTREAM CLAIM (not in the external result) -- wall.py:205-216 BONUS: 'As R -> infinity the margin tends to 2(beta^2 sigma_0 - p_0)/(1+beta^2) ... ANY STRICTLY STABLE WALL AUTOMATICALLY HAS AN UNBOUNDED DOMINANT-ENERGY BASIN' (wall.py:215). The asymptote and the gap identity are exact for the LINEAR EOS extended to all amplitudes (checks 6a-6d, z3), and sigma + p = (sigma0+p0)(R/R0)^{-2A} never changes sign so the margin is monotone (6b). But 'strictly stable' is fixed by beta^2 at sigma0 alone, while the basin depends on the EOS along the whole curve. Shown here (check 8a): p = p0 + beta^2 (sigma - sigma0) + c (sigma - sigma0)^2 with x = 0.3, beta^2 = 0.5 (strictly stable; linear basin unbounded, asymptote 0.00782 > 0), c = 400 -> sigma - p < 0 first at R/R0 = 1.2085 along the conservation curve (sigma + p stays > 0, so the curve is regular). The boxed claim is true within the file's stated linear-EOS model (wall.py:225) but the box does not repeat that hypothesis. This concerns the tree's own theorem built on the law; it does not narrow the conservation law. Reachability of R/R0 = 1.2085 by an actual orbit of that nonlinear shell is NOT checked here."
 ],
 "data_at_publication": [
  {
   "quantity": "physical numerical inputs to the conservation law",
   "value_then": "none -- (13) is an identity of the Israel equations in G = c = 1 geometric units (PV 1995); no measured constant enters",
   "value_now": "none",
   "source_now": "PSP arXiv:2604.05980 p.8 (same statement, 2026); re-derived symbolically here (check 1a)",
   "moves_conclusion": "no -- nothing to move"
  },
  {
   "quantity": "tree's own cross-check: oscillation period (units R/c) at (x, beta^2) = (0.3,0.5), (0.5,0.5), (0.3,0.2); wall.py:231-235 claims closed-form and RK4 routes agree to 2e-5 and both agree with 2 pi/sqrt(V''/2)",
   "value_then": "agreement to 2e-5 (wall.py:233)",
   "value_now": "analytic 5.170803 / 6.323029 / 9.654552; orbit through closed-form V 5.170908 / 6.322908 / 9.654489; orbit through an RK4-integrated sigma(R) 5.170908 / 6.322908 / 9.654489 (identical to printed digits); relative gap to analytic 2.0e-5 / 1.9e-5 / 6.5e-6 (finite amplitude eps = 1e-4 and step size). RK4 sigma(R) vs closed form: max rel 1.2e-13.",
   "source_now": "rederive/thin-shell-conservation-law.py checks 7a, 7b (this audit)",
   "moves_conclusion": "no -- the tree's 2e-5 claim is reproduced"
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/thin-shell-conservation-law.py",
  "outcome": "23/23 checks pass (sympy 1.14, z3). (1a) From the Israel/Lanczos surface stress (PV eq 8) for a moving shell between static vacuum regions f = 1-2M/R with M_in != M_out, d(sigma A)/dtau + p dA/dtau = 0 identically in (R, Rdot, Rddot, M_in, M_out); (1b) 200 random numeric points incl. M_in < 0, max residual 3.3e-15; (1c-1e) PV eqs (11), (12), (13) reproduced for the equal-mass wormhole. (2a-2c) the law <=> sigma' = -(2/R)(sigma+p) <=> m_s' = -8 pi R p <=> PV (21). (3a) Israel statics at M_in = 0 equal wall.statics() to 1.6e-13. (4a-4c) dsolve of the linear-EOS ODE equals wall.sigma_of_R (1.4e-14 rel); (4d, 4e) beta^2 = -1 is logarithmic and outside the closed form. (5) INDICATION only that a radiating (Vaidya) exterior adds a dM/du term; the flux law itself is READ (IL eqs 6, 12), not computed. (6a-6d) dec asymptote 2(beta^2 sigma0 - p0)/(1+beta^2), sigma+p = (sigma0+p0)(R/R0)^{-2A}, gap identity x/(4 s^2 (1+3s)) symbolic, z3 unsat for gap <= 0 on s in (0,1). (7a, 7b) RK4 and period cross-checks. (8a) nonlinear-EOS scope counterexample to the BONUS box as stated without its linear-EOS hypothesis.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "Pitre, Schneider & Poisson, 'Self-gravitating thin shells are dynamically unstable on all angular scales', arXiv:2604.05980 (2026)",
   "effect": "confirms",
   "what": "p.8: for Minkowski inside / Schwarzschild outside with 'no matter inside and outside the shell', D_b S^ab = 0 (energy and momentum) holds, citing Israel's eq (21) -- the conservation law in exactly the tree's configuration and under exactly the vacuum hypothesis. The paper's main result (non-radial l >= 2 instability) does not touch the conservation law; it narrows what radial stability means, which wall.py:110-190 already records.",
   "read_status": "READ (alphaXiv page text, cached; pp.1-9)"
  },
  {
   "ref": "Ishak & Lake, arXiv:gr-qc/0108058 (2001/2002)",
   "effect": "extends",
   "what": "Generalises PV to unequal masses and states the condition for the no-flux law: transparency [G n u] = 0 (eq 6), guaranteed at equilibrium by m = m(R) (eq 12) and away from equilibrium by static embeddings near Sigma (sec. II.C); isolates sigma + P = 0 (Upsilon = 0) as a separate domain-wall case (sec. II.D).",
   "read_status": "READ (alphaXiv page text, cached; pp.1-4)"
  },
  {
   "ref": "A. T. Le, 'Steering a warp drive without exotic matter', arXiv:2606.22531v3 (2026)",
   "effect": "narrows",
   "what": "Not a narrowing of the law but of its applicability to the tree's target: Le's radiative warpshell requires 'flux-source balance laws ... with an external crossing flux, mandatory here because the exterior radiation is emitted at the shell' (p.2), i.e. H3 fails for the radiating object; the vacuum law holds for its static Minkowski/Schwarzschild anchor. wall.py:198-200 already names this.",
   "read_status": "READ (alphaXiv page text, cached; p.2)"
  },
  {
   "ref": "discover_papers search for later work on the conservation law / flux generalisations",
   "effect": "contested",
   "what": "NOT RUN: alphaXiv quota exhausted in this stage ('assistant quota exceeded'). No later-literature search beyond the cached texts above was possible here; this is a gap in coverage, not evidence of absence. ('contested' is used only because the schema requires an effect; no contest was found.)",
   "read_status": "NOT-RUN (quota)"
  }
 ],
 "lacked_data": "M's hypothesis tested for this result: the law is an identity of the Einstein-Israel equations (the tau-component of D_b S^ab = 0 for vacuum sides), with no measured datum at all -- PV 1995 used none, and none has appeared since that could move it. The one thing PV say they lacked is a microphysical model of the exotic matter to interpret beta (PV p.3-4: 'there is no guarantee that beta_0 actually is the speed of sound. A detailed microphysical model ... would be necessary'); that bears on the EOS input, not on the conservation law, and wall.py:201-203 carries the same caveat ('beta^2 ... is a proxy'). What later work added -- the non-radial instability of PSP 2026 and Le's radiating shell -- changes the SCOPE in which the law is applied (vacuum anchor, radial mode) and wall.py already names both; it does not change the law. Evidence therefore runs against M's hypothesis for this item: re-derived identically here for the tree's configuration, and restated for the same configuration in 2026.",
 "grade": "STANDS",
 "grade_evidence": "Statement as used (wall.py:222-227, 316-325): m_s' = -8 pi R p and sigma' = -(2/R)(sigma+p) for a thin spherical shell with Minkowski inside and Schwarzschild outside, integrated in closed form for a linear EOS. Re-derived from the Israel condition identically in (R, Rdot, Rddot, M_in, M_out) (checks 1a, 1b), reproducing PV eqs (11)-(13), (21) (1c-1e, 2c); equivalent forms checked (2a, 2b); closed form = dsolve = wall.sigma_of_R (4a-4c); the tree's RK4 period claim reproduced (7a, 7b); the downstream asymptote and gap identity exact and z3-proved (6a-6d). Hypotheses as used: vacuum both sides (named, wall.py:198-200, 222-223), linear EOS (named, wall.py:225, 317). No datum enters. Recorded, not grade-moving: (a) the closed form excludes beta^2 = -1 (A = 0), never used; (b) the PV citation covers the equal-mass wormhole, the unequal-mass case is Ishak-Lake/PSP -- widening supported by re-derivation; (c) the vacuum hypothesis fails for Le's radiating shell (Le p.2) -- the tree says so; (d) the BONUS box at wall.py:215 ('ANY STRICTLY STABLE WALL ...') holds within the linear-EOS model but a nonlinear EOS with the same beta^2(sigma0) crosses dec at R/R0 = 1.2085 (check 8a) -- a scope note on the tree's own theorem, not on this external result.",
 "what_would_change_the_grade": "NARROWED if the tree applied m_s' = -8 pi R p to the radiating (flux-crossing) shell itself rather than to its frozen vacuum anchor -- it does not (wall.py:198-200); or if any caller of wall.sigma_of_R used beta^2 = -1. WRONG only on a computed failure of check 1a, which is an exact symbolic identity. The BONUS scope note (d) would become a finding about wall.py (not about this result) if a reachable orbit of a nonlinear-EOS shell with beta^2(sigma0) > beta^2_crit were shown to cross dec -- reachability is not checked here. A later-literature search (not run: quota) could add references but cannot move an identity.",
 "reverify_command": "python3 " + D + "/rederive/thin-shell-conservation-law.py  # exits 0 on 23/23; source text: " + D + "/src/casmag/all/gr-qc_9506083v1.txt (PV eqs 11-16, p.2)",
 "report_path": D + "/audits/thin-shell-conservation-law.json"
}
json.dump(rep, open(rep["report_path"], "w"), indent=1)
print("ok")
