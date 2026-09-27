import json
D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
rv = "cd /tmp && PYTHONDONTWRITEBYTECODE=1 python3 %s/rederive/2604.05980-radial-gamma1.py  # expect 27 PASS, 'ALL PASS', exit 0; and: grep -n '3.16\\|footnote\\|(2.6)\\|(2.7)' is replaced by: sed -n 640,823p %s/src/casmag/all/2604.05980v1.txt" % (D, D)
r = {
 "key": "2604.05980-radial-gamma1",
 "name": "Pitre, Schneider & Poisson (arXiv:2604.05980) Eq (3.16c): radial criterion Gamma >= Gamma_1 = (4 - 6C + 2 sqrt(1-2C))/(4(1-2C)), and Eq (2.7) Gamma = beta^2 (mu + p)/p",
 "source": {
  "located": "arXiv:2604.05980v1 [gr-qc], 7 Apr 2026 (dated April 8, 2026): T. Pitre, B. Schneider, E. Poisson, 'Self-gravitating thin shells are dynamically unstable on all angular scales' (Univ. Guelph). Eq (2.6) and (2.7) on p.7; Eqs (3.11)-(3.18) and footnote 1 on p.9; Newtonian (10.16)-(10.17) on p.37; Ref [34] = P. LeMaitre and E. Poisson, Am. J. Phys. 87, 961 (2019), p.47.",
  "read_status": "READ",
  "via": "alphaXiv page text. The live alphaXiv tools (answer_pdf_queries, get_paper_content, discover_papers) all returned 'alphaXiv assistant quota exceeded' in this stage, so the page text was read from the harvested cache of earlier alphaXiv tool results in this project's transcripts: " + D + "/src/casmag/all/2604.05980v1.txt (md5 9916ebc75c7859da12c37c59acc4458f; harvester src/casmag/allpages.py). Pages present: 1-4, 6, 7, 9, 23, 37, 41, 47; every equation this entry uses is on a present page (p.7, p.9, p.37). Page 8 (Eqs 3.1-3.10, the derivation of 3.11-3.12) is absent; 3.11-3.12 were instead re-derived here from the junction condition (V(R0) = V'(R0) = 0 in the script). LeMaitre-Poisson 2019 itself: NAMED-NOT-READ (its Eq (34) is known here only through PSP footnote 1)."
 },
 "published_statement": "p.9: 'If we follow M(sigma) along the equilibrium sequence, taking into account that dp = Gamma(p/sigma) dsigma and dmu = [(mu + p)/sigma] dsigma, we find that dM/dsigma >= 0 whenever Gamma >= Gamma_1, where Gamma_1 := 3/2 + 4(p/mu) + 4(p/mu)^2 (3.16a) = (1 + 2 sqrt(F) + 3F)/(4F) (3.16b) = (4 - 6C + 2 sqrt(1 - 2C))/(4(1 - 2C)) (3.16c), where C := M/R is the shell's compactness. When C << 1 ... Gamma_1 = 3/2 + C + 7/4 C^2 + O(C^3) (3.17). The point along the sequence at which dM/dsigma = 0 is the configuration of maximum mass for the specified equation of state, and this point also marks the onset of a radial instability -- the shell becomes dynamically unstable against time-dependent, spherically-symmetric perturbations [34].' Footnote 1: 'The criterion appears to be different from the one given in Eq. (34) of Ref. [34]. The reason has to do with inequivalent definitions of the adiabatic index. In Ref. [34] it was defined as d ln p/d ln mu, whereas it is d ln p/d ln sigma here. To maximize confusion, mu was denoted sigma in Ref. [34].' p.7: 'The adiabatic index Gamma is defined by Gamma := (sigma/p) dp/dsigma (2.6), and in general it is a function of sigma. The first law then implies that dp = Gamma p/(mu + p) dmu (2.7).' p.37 (Newtonian): 'It is known [34] that these equilibrium configurations are radially stable whenever Gamma >= 3/2.'",
 "published_hypotheses": [
  "Infinitesimally thin shell tracing a timelike hypersurface; static and spherically symmetric unperturbed state (p.2, p.7).",
  "Minkowski spacetime inside, Schwarzschild outside; vacuum on both sides (p.2, p.7 'We assume that there is no matter inside and outside the shell').",
  "Shell matter is a perfect fluid (isotropic surface pressure), S^ab = mu u^a u^b + p(h^ab + u^a u^b), Eq (2.2).",
  "Barotropic equations of state mu = sigma + eps(sigma), p = p(sigma), Eq (2.4); sigma = rest-mass (number x rest mass) areal density, mu = areal energy density.",
  "Isentropic fluid obeying the first law dmu = (mu + p)/sigma dsigma, Eq (2.5) -- this is what Eq (2.7) rests on.",
  "Gamma := d ln p/d ln sigma (rest-mass density), Eq (2.6), in general sigma-dependent (introduction uses a constant-Gamma polytrope, Eq (1.1), for the mode calculations).",
  "Israel junction conditions, Eq (2.10); general relativity.",
  "The criterion is a turning-point criterion on the equilibrium sequence (dM/dsigma >= 0); its identification with the onset of dynamical radial instability is cited to Ref. [34] (LeMaitre-Poisson 2019), not derived in this paper, and is stated under the supposition 'that the sequence begins at low sigma with Gamma(sigma) > Gamma_1' (p.9)."
 ],
 "hypothesis_drift": [
  "ATTRIBUTION (discrepancy, not a content error): wall.py:112 writes the (3.16c) form followed by '(LeMaitre-Poisson 2019)', and wall.py:445 docstrings gamma1_published as 'LeMaitre-Poisson 2019 / Pitre et al Eq (3.16c)'. PSP footnote 1 (p.9) says the criterion 'appears to be different from the one given in Eq. (34) of Ref. [34]' because LeMaitre-Poisson define Gamma as d ln p/d ln mu (energy density). The printed (3.16c) formula is PSP's, in PSP's convention; LeMaitre-Poisson's printed threshold is in another variable. Computed here, in the d ln p/d ln mu convention the same threshold is (3s^2+2s+1)/(s(3s+1)), s = sqrt(1-2C), Newtonian limit also 3/2 -- LP Eq (34) was NOT read, so this is not asserted to match it. The physics attributed is the same; the formula is not LP's as printed.",
  "DROPPED from the canonical hypothesis list (wall.py:109-117, canonical.json hypotheses): 'perfect fluid, barotropic p = p(sigma), isentropic, first law dmu = (mu+p)/sigma dsigma' (PSP Eqs 2.2, 2.4, 2.5). The Eq (2.7) conversion Gamma = beta^2 (mu+p)/p that wall.py:114-115 uses is exactly the first law; without it the conversion is not defined. Not conclusion-moving for this entry: wall.py's own dynamics (sigma_of_R, wall.py:316-, p linear in energy density with sigma' = -(2/R)(sigma+p)) is barotropic, and the tree's counter-rotating (Vlasov) matter (wall.py:404-412) is barotropic ALONG SPHERICAL MOTION (n ~ R^-2, u = gamma v ~ R^-1, so mu and p are functions of R alone, and dmu/dsigma_rest = mu'/sigma_rest' = (mu+p)/sigma_rest follows from the conservation law) -- by-hand argument, recorded; for NON-radial motion a collisionless shell is not a perfect fluid, which bears on the separate non-radial key, not this one.",
  "WEAKENED/RE-READ: the source states a turning-point condition (dM/dsigma >= 0 iff Gamma >= Gamma_1) and cites [34] for its being the onset of radial instability, under the supposition that the sequence starts stable at low sigma (p.9). The tree reads it as the pointwise dynamical criterion 'stable iff beta^2 > beta^2_crit' (wall.py:109-117). The tree's own derivation (V''(R0) > 0, wall.py:281-284, 305-310) supplies the dynamical reading; the script derives V'' independently from the junction condition and shows its threshold, converted by Eq (2.7), equals Gamma_1 IDENTICALLY in s, with dV''/dbeta^2 = 2(3s+1)/R^2 > 0 (so the direction 'stable above' also agrees). The drift is therefore closed by computation, not by quotation.",
  "NUMERIC SENTENCE (discrepancy in the tree, not the source): wall.py:113-114 says 'Converted, the two agree to 1e-15 at every x from 1e-6 to 0.8'. The mathematical agreement is exact (sympy identity), but the double-precision gamma_crit (wall.py:448-452) disagrees with 40-digit (3.16c) by up to 9.8e-11 relative on [1e-6, 0.8] (6.0e-11 at x = 1e-6; 8.9e-5 at x = 1e-12, outside the stated range), because wall.statics (wall.py:249-256) forms (1 - s) naively -- the cancellation wall.one_minus_s (wall.py:275-279) exists to avoid. Forming (1-s) as x/(1+s) brings it to 5.4e-16. The tree's selftest checks at tolerance 1e-9 (wall.py:617-621) and passes; gamma_crit is used only in those checks, so no conclusion moves. Recorded, not repaired.",
  "UNVERIFIED DATUM: wall.py:110 says '(arXiv:2604.05980, Phys. Rev. D)'. The arXiv v1 text read carries no journal reference; publication in Phys. Rev. D is not checked here (live alphaXiv quota exhausted). Not a finding either way.",
  "SCOPE, no drift: wall.py:124-125 'a static thin shell, Minkowski inside, Schwarzschild outside -- LE'S STATIC ANCHOR EXACTLY' matches PSP p.2/p.7; the Newtonian limit 3/2 (wall.py:115, 621) matches (3.17) and p.37."
 ],
 "data_at_publication": [
  {
   "quantity": "Empirical inputs to Gamma_1 (constants, measurements)",
   "value_then": "none: Gamma_1 is a closed-form function of C = M/R alone, from GR junction conditions plus the first law (Eqs 2.5-2.7, 3.11-3.16); G = c = 1 units",
   "value_now": "none",
   "source_now": "PSP pp.7, 9 (read); re-derived symbolically in rederive/2604.05980-radial-gamma1.py",
   "moves_conclusion": "No -- there is no datum to move. Units: C = GM/(Rc^2) in SI; CODATA G and exact c do not enter the functional form."
  },
  {
   "quantity": "Range over which the tree's conversion was checked",
   "value_then": "tree: 6 sample points x = 1e-6, 0.05, 0.2, 0.3, 0.5, 0.8 at tolerance 1e-9 (wall.py:617-620); sentence claims 1e-15 at every x in [1e-6, 0.8] (wall.py:113)",
   "value_now": "exact symbolic identity for all 0 < s < 1 (i.e. 0 < x < 1); double-precision residual 9.8e-11 max on 806 points in [1e-6, 0.8] from wall.statics' naive (1-s)",
   "source_now": "rederive/2604.05980-radial-gamma1.py output (rederive/2604.05980-radial-gamma1.out)",
   "moves_conclusion": "No -- strengthens the agreement from sampled to identical; the 1e-15 wording is a recorded discrepancy in the tree's numeric sentence only."
  },
  {
   "quantity": "Causal-boundary cross-check (beta^2_crit = 1) against Brady-Louko-Poisson 1991",
   "value_then": "R/m+ ~ 2.37 at P'/sigma' = 1, m- -> 0 (BLP 1991 NAMED-NOT-READ; restated by Ishak & Lake gr-qc/0108058 per the sibling audit dust-shell-radial-instability-textbook.json, not re-read here)",
   "value_now": "R/M = 2.370393 from 15s^3 + 3s^2 - s - 1 = 0 (s* = 0.395295, x* = 0.843742)",
   "source_now": "rederive/2604.05980-radial-gamma1.py section (i)",
   "moves_conclusion": "No -- a third, older published number agrees with the V'' side of the equivalence."
  }
 ],
 "rederivation": {
  "method": "sympy",
  "script_path": D + "/rederive/2604.05980-radial-gamma1.py",
  "outcome": "27 PASS, 0 FAIL, exit 0 (output saved to rederive/2604.05980-radial-gamma1.out). Symbolically: (3.11)/(3.12) equal wall.statics; the Newtonian limits under (3.12) hold; (3.16a) = (3.16b) = (3.16c); (3.13) inverts (3.11)-(3.12); the turning point of M(mu,p) under dp = Gamma p/sigma dsigma, dmu = (mu+p)/sigma dsigma has the unique root Gamma = 3/2 + 4q + 4q^2 with dM/dsigma increasing in Gamma; INDEPENDENTLY, V(R) = 1 - (k/2 + M/(Rk))^2, k = 4 pi R mu, with mu' = -(2/R)(mu+p), p' = beta^2 mu', gives V(R0) = V'(R0) = 0 and a unique V'' root beta^2_crit = (1-s)(3s^2+2s+1)/(4s^2(1+3s)) = wall.beta2_crit, dV''/dbeta^2 = 2(3s+1)/R^2 > 0; converted by Eq (2.7) it equals Gamma_1 identically in s; (3.17) series exact to O(C^2); (3.18) inverts (3.16b) numerically; Newtonian turning point Gamma = 3/2 from (10.16); beta^2_crit = 1 gives R/M = 2.370393 (BLP 1991 ~2.37). wall.gamma1_published is (3.16c) with C = x/2 to 3.4e-16; wall.gamma_crit's float residual up to 9.8e-11 (recorded discrepancy in wall.py:113's '1e-15', cause located in wall.statics' naive 1-s). The tree's own selftest (python3 wall.py --selftest) exits 0.",
  "agrees_with_source": "yes"
 },
 "later_literature": [
  {
   "ref": "A. T. Le, 'Radiative steering of warp shells', arXiv:2606.22531v4 (13 Sep 2026)",
   "effect": "confirms",
   "what": "Cites PSP as [19] only for the non-radial result ('the fully coupled study [19] finds growing even-parity modes at all sampled multipoles l >= 2 ... Its constitutive assumptions differ from those of the radiating shell considered here'); says nothing contradicting Eq (3.16c) or Eq (2.7). Neutral on this entry; recorded as the only later citing work in hand, and flagged 'confirms' only in the weak sense of no contradiction.",
   "read_status": "READ (cached alphaXiv page text, src/casmag/all/2606.22531v4.txt, lines 82-92 and ref [19] at 1951-1952)"
  },
  {
   "ref": "P. LeMaitre & E. Poisson, Am. J. Phys. 87, 961 (2019), Eq (34)",
   "effect": "confirms",
   "what": "The source of the dynamical-instability identification PSP cite; per PSP footnote 1 its printed criterion uses Gamma = d ln p/d ln mu, so it differs in form, not substance. Earlier, not later, literature; listed because the tree attributes the formula to it.",
   "read_status": "NAMED-NOT-READ (known only through PSP footnote 1 and PSP p.37)"
  },
  {
   "ref": "discover_papers (later-literature search, keywords thin shell / radial stability / adiabatic index)",
   "effect": "contested",
   "what": "NOT RUN: the one permitted discover_papers call returned 'alphaXiv assistant quota exceeded'. Later literature beyond the cached Le 2026 paper is unsearched in this stage -- recorded as a gap, not as evidence either way. The 'contested' tag is forced by the schema and means 'unknown', not that anything contests the result.",
   "read_status": "NOT-READ (tool quota)"
  }
 ],
 "lacked_data": "M's hypothesis tested for this result. What the authors had: nothing empirical is needed -- Gamma_1 is a theorem of GR (Israel junction conditions, Minkowski/Schwarzschild vacuum) plus surface thermodynamics (first law, barotropic isentropic perfect fluid). Published 2026, it is the newest result in this chain and post-dates every datum that could bear on it. What came later: nothing in hand bears on it (Le 2606.22531v4 cites PSP only for the non-radial mode); the later-literature search could not run. Evidence the conclusion does not move with data: it is re-derived here along two independent routes (static turning point from Eq 3.13; dynamical V'' from the junction equation of motion) that agree identically in s, and a third, older published number (BLP 1991's R/m ~ 2.37 at the causal boundary) is reproduced to 2.370393. The only 'earlier-physicist' discrepancy found is definitional, and the source itself names it: LeMaitre-Poisson 2019 used d ln p/d ln mu, PSP use d ln p/d ln sigma (footnote 1) -- the two forms are the same threshold in different variables (computed: (3s^2+2s+1)/(s(3s+1)) vs Gamma_1), so no earlier result was wrong. What COULD move the conclusion is not data but a named hypothesis: a shell of finite thickness, anisotropic surface stress, non-isentropic or non-barotropic matter (e.g. a collisionless shell under non-radial motion), matter inside or outside, or a theory other than GR. None of those is a datum the authors lacked; each is outside the class the result is stated on. M's hypothesis is therefore not supported for this result, and the evidence against it is computed, not presumed.",
 "grade": "STANDS",
 "grade_evidence": "Statement and hypotheses read at source (PSP pp.7, 9, 37, via cached alphaXiv page text). The tree uses the result on exactly the source's configuration (static thin shell, Minkowski in, Schwarzschild out, radial) and with the source's Gamma definition (d ln p/d ln sigma, rest-mass density). The rederivation agrees: all three forms of (3.16), the turning-point criterion, and an independent dynamical V'' criterion converted by Eq (2.7) coincide identically in s (sympy), with the correct direction (dV''/dbeta^2 > 0, dM/dsigma increasing in Gamma); (3.17), (3.18) and the Newtonian 3/2 check; 27/27 PASS. No datum enters. Recorded discrepancies, none conclusion-moving and none in the source: (i) the tree's attribution of the (3.16c) form to LeMaitre-Poisson 2019 (wall.py:112, 445) against PSP footnote 1; (ii) the tree's canonical hypothesis list drops 'barotropic isentropic perfect fluid obeying the first law', which Eq (2.7) needs -- satisfied by the tree's own matter models along radial motion; (iii) wall.py:113's '1e-15 at every x' is 9.8e-11 in double precision at small x, from wall.statics' naive (1-s); (iv) 'Phys. Rev. D' at wall.py:110 unverified. Later-literature search could not run (quota); that is a gap, not a grade input.",
 "what_would_change_the_grade": "To NARROWED: a showing that the tree applies Gamma_1 to matter that is not barotropic/isentropic along the perturbation it considers (e.g. if a reading established that the counter-rotating shell's radial response is not captured by a single dp/dmu), or to a configuration with interior/exterior matter or finite thickness. To WRONG: a computed counterexample to the identity V''-threshold == Gamma_1 (the script shows none exists for 0 < s < 1), or a published correction to PSP Eq (3.16)/(2.7) -- none found, but the later-literature search did not run. To OPEN: loss of the cached page text with no live alphaXiv read available. Reading LeMaitre-Poisson 2019 Eq (34) would settle the attribution discrepancy (i); a live alphaXiv/journal lookup would settle (iv).",
 "reverify_command": rv,
 "report_path": D + "/audits/2604.05980-radial-gamma1.json"
}
r["reverify_command"] = ("cd /tmp && PYTHONDONTWRITEBYTECODE=1 python3 %s/rederive/2604.05980-radial-gamma1.py  # expect 27 PASS, ALL PASS, exit 0; "
                         "source text: sed -n 640,823p %s/src/casmag/all/2604.05980v1.txt  # (3.11)-(3.18), footnote 1; sed -n 520,560p same file for (2.6)-(2.7); "
                         "tree: cd /home/user/Claude-Method-Works/research/warp-drive && PYTHONDONTWRITEBYTECODE=1 python3 wall.py --selftest" % (D, D))
json.dump(r, open(r["report_path"], "w"), indent=1, ensure_ascii=False)
print("written", r["report_path"])
