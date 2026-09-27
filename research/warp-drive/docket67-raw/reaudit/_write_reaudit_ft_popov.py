"""Writes the five DOCKET 67 re-audit JSONs (F&T Sec. 7 / Candelas; AHS via restatement; Popov x3)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
R2 = '/home/user/Claude-Method-Works/research/warp-drive/docket67-raw/round2_collected.json'
first = json.load(open(R2))['audits']
FT_PY = os.path.join(D, 'fewster-teo-sec7-candelas-schwarzschild.py')
PP_PY = os.path.join(D, 'popov-hep-th_0302039.py')
CAND_TXT = os.path.join(D, 'src', 'candelas1980_gdrive_1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ.txt')
TREE = '/home/user/Claude-Method-Works/research/warp-drive'
PP_RUN = ('cd /tmp && PYTHONDONTWRITEBYTECODE=1 python3 %s   # expect "17 checks, 0 FAIL", exit 0 '
          '(imports hpscentre.build read-only)' % PP_PY)

def out(key, doc):
    doc['key'] = key
    doc['report_path'] = os.path.join(D, key.replace('/', '_').replace('#', '_') + '.json')
    doc['supersedes_grade'] = first[key]['grade']
    order = ['key', 'name', 'source', 'published_statement', 'published_hypotheses', 'hypothesis_drift',
             'data_at_publication', 'rederivation', 'later_literature', 'lacked_data', 'grade',
             'supersedes_grade', 'grade_evidence', 'what_would_change_the_grade', 'reverify_command',
             'report_path', 'pages_read']
    doc = {k: doc[k] for k in order}
    json.dump(doc, open(doc['report_path'], 'w'), indent=1, ensure_ascii=False)
    print('wrote', doc['report_path'], doc['grade'], '<-', doc['supersedes_grade'])

# =====================================================================================
# 1. fewster-teo-sec7-candelas-schwarzschild
# =====================================================================================
out('fewster-teo-sec7-candelas-schwarzschild', dict(
 name=first['fewster-teo-sec7-candelas-schwarzschild']['name'],
 source=dict(
  located=("(a) C. J. Fewster & E. Teo, 'Bounds on negative energy densities in static space-times', "
           "arXiv:gr-qc/9812032v2 (16 Feb 1999), DAMTP-1998-160 -- confirmed from its own p.1 header "
           "('arXiv:gr-qc/9812032v2 16 Feb 1999', 'DAMTP-1998-160', authors Christopher J. Fewster (York) and "
           "Edward Teo (DAMTP / NUS)). Sec. 7 'Schwarzschild space-time', pp.17-19, eqs. (7.1)-(7.11); its "
           "ref. [21] reads 'P. Candelas, Phys. Rev. D 21, 2185 (1980).' "
           "(b) P. Candelas, 'Vacuum polarization in Schwarzschild spacetime', Phys. Rev. D 21, 2185-2202 -- "
           "confirmed from the retrieved file's own pages: running head 'PH YSICAL RK VIE% 0 VOLUME 21, NUMBER 8' "
           "(OCR of 'PHYSICAL REVIEW D VOLUME 21, NUMBER 8'), '15 APRIL 1980', 'P. Candelas Center for Theoretical "
           "Physics, University of Texas at Austin, Austin, Texas 78712 (Received 10 July 1979)', page markers "
           "'21 2185' ... '2202 P. CANOE I.AS 21', and running title 'VACUUM POLARIZATION IN SCHWARZSCHILD SPACETIME'."),
  read_status=("READ (M-retrieved, Google Drive 1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ: Candelas PRD 21 2185, "
               "full text layer, OCR-garbled word order) + READ (gr-qc/9812032v2, all 23 pages, alphaXiv)"),
  via=("Candelas: mcp Google Drive read_file_content on fileId 1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ (title "
       "'vacuum polarization in schwarzschild spacetime.pdf', 53,511 characters), read in full; the text layer "
       "interleaves two-column words and drops most mathematics, so every Candelas quote below is copied "
       "exactly as the layer prints it, garbling included, and nothing is attributed to Candelas that the layer "
       "does not show. Saved at %s. F&T: alphaXiv answer_pdf_queries(gr-qc/9812032) returned all 23 pages "
       "(pp.1-23, including Sec. 2, Sec. 6, Sec. 7, the Appendix and the reference list)." % CAND_TXT)),
 published_statement=(
  "F&T Sec. 7 (READ, quoted): p.17 'For simplicity, we shall only consider a massless scalar field in this "
  "space-time. The mode functions, in the region exterior to the horizon r > 2M, take the form [20]' (7.2) "
  "[ref. 20 = DeWitt, Phys. Rep. 19, 295]; '->R_l(w|r) and <-R_l(w|r) are the outgoing and ingoing solutions to "
  "the radial part of the wave equation, respectively. Although this equation cannot be solved analytically, the "
  "asymptotic forms of the solutions are known near the horizon and at infinity.' After (7.3): 'In writing this, "
  "we are assuming that the mode functions are defined to have positive frequency with respect to the time-like "
  "Killing vector d_t. This is the Boulware vacuum.' p.18: 'in the two regions where ->R_l(w|r) and <-R_l(w|r) are "
  "known explicitly, we have [21]' (7.4): SUM(2l+1)|->R_l|^2 ~ 4w^2(1-2M/r)^-1 (r->2M), (1/r^2)SUM(2l+1)|B_l(w)|^2 "
  "(r->oo); (7.5): SUM(2l+1)|<-R_l|^2 ~ (1/4M^2)SUM(2l+1)|B_l(w)|^2 (r->2M), 4w^2 (r->oo). 'If we further assume "
  "the low-energy condition 2Mw << 1, then [22]' (7.6) B_l(w) ~ (l!)^3/((2l+1)!(2l)!) (-4iMw)^(l+1) [ref. 22 = "
  "Jensen, McLaughlin, Ottewill PRD 45 3002]. 'If (7.6) is exact to O[(Mw)^(l+2)], then only the l = 0 terms should "
  "be retained'. 'Near the horizon, the quantum inequality can be expressed in terms of the observer's proper time: "
  "tau_0 = (1-2M/r)^(1/2) t_0, (7.7)' ... (7.8) '... where the ellipsis denotes higher-order terms that have been "
  "dropped.' 'The bound in (7.8) is between 9/64 and 1/4 that in (7.9), at least in the present approximation. "
  "Note that in either case, the bound becomes arbitrarily negative near the horizon of the black hole.' 'On the "
  "other hand, the quantum inequality for an observer near infinity becomes' (7.10) rho >= -(3/(32 pi^2 tau_0^4)) "
  "(9/64)[1 - 2M/r + (2M/r)^2(1 + (16/9)(1/3)(tau_0/r)^2) - (2M/r)^3(1 + (16/9)(tau_0/r)^2) + ...]; p.19 'Again, the "
  "former bound is between 9/64 and 1/4 the latter. It gives the correct Minkowski space result in the limit r -> oo "
  "or M -> 0.' "
  "CORRECTION to the first audit's transcription: (7.10) is the NEAR-INFINITY bound, not a 'comparison form'; the "
  "'between 9/64 and 1/4' sentence is printed twice, once for the near-horizon pair (7.8)/(7.9) and once for the "
  "near-infinity pair (7.10)/(7.11). "
  "Candelas (READ, text layer verbatim): abstract '... is studied for massless fields in the region exterior ... to "
  "the horizon of a Schwarzschild ... black hole' [layer: 'is studied for massless fields in the region exterior "
  "renormalized value of ...'], 'The form of the renormalized expectation value of the stress tensor near the "
  "horizon and at infinity is discussed for each of these three states.' Boulware state: '(i) the Boulware' vacuum "
  "jB), defined by re- with quiring respect normal to the modes Killing to be vector positive s/st frequency with "
  "re- spect to which the exterior region is static' (layer order scrambled; the words are 'defined by requiring "
  "normal modes to be positive frequency with respect to the Killing vector d/dt with respect to which the exterior "
  "region is static'). Mode basis: 'a complete set of normalized basis functions ... which have R t ((d \\~the r)- "
  "asymptotic forms r 'et\"\"+ + Xt(\\~)r 'e '\"\"\\*, r -2M Rt((o\\~r)- Bt((u)r B,(\\&u)r 'e ...' followed by "
  "'is the Regge-Wheeler coordinate' -- i.e. each basis function is DEFINED by its asymptotic form at r -> 2M and "
  "at r -> oo (unit incident wave plus reflected/transmitted amplitudes A_l, B_l). The two sums: 'use Of of "
  "particular asymptotic interest forms are that the are two established asymptotic in regimes Appendix x- A: 2M, "
  "x- \\~.' Appendix A title 'APPENDIX A: ON THE ASYMPTOTIC EVALUATION OF MODE SUMS'; '(A2) The as asymptotic r- \\~ "
  "may forms of (Al) as r-2M be obtained directly by and sub- of stitution of the asymptotic forms that define the "
  "radial function. The asymptotic form of (Al) as r- \\~ may be found by use of the WKB approximation.' The layer "
  "drops the displayed formulas, so the COEFFICIENTS of (7.4)/(7.5) are read here from F&T, which attributes them "
  "to [21]; Candelas' pages confirm the structure (two families defined by horizon/infinity asymptotics, sums "
  "evaluated only in the regimes r -> 2M and r -> oo, one of them by WKB). "
  "Owner (fewsterteo.py:56-60, read): 'Their Schwarzschild bound is built on Candelas' outgoing/ingoing mode sums, "
  "whose basis is DEFINED BY HORIZON BOUNDARY CONDITIONS. With m < 0 there is no horizon: the horizon is not a "
  "caveat on Sec. 7, it is Sec. 7's mode-defining surface. Continuing (7.10) to M < 0 would be failure mode (4). "
  "NOT DONE, and pinned False.' (:170 SEC7_TRANSPLANTABLE_TO_NEGATIVE_M = False; :622 selftest check)."),
 published_hypotheses=[
  "F&T Sec. 2 (READ): 'We shall consider n+1-dimensional space-times that are globally static, with time-like Killing vector d_t' (2.1); 'free, real scalar field phi of mass mu >= 0'; 'Suppose it admits a complete, orthonormal set of positive frequency solutions.'",
  "F&T Sec. 2 (READ): the bound is on the NORMAL-ORDERED density: 'Recall that the normal-ordered energy density is the difference between the renormalised energy density in the two states |psi> and |0>.'",
  "F&T (2.7) (READ): 'f is any smooth, non-negative function decaying at least as fast as O(t^-2) at infinity, and normalised to have unit integral.' Sec. 7's closed forms use the Lorentzian (1.1) via (2.18) and the integral (6.9).",
  "F&T Sec. 7 (READ): Schwarzschild exterior r > 2M ('in the region exterior to the horizon r > 2M'), massless field, Boulware vacuum (positive frequency w.r.t. d_t), static observer (proper time via (7.7)).",
  "F&T Sec. 7 (READ): the up/in mode sums are known only asymptotically ('known near the horizon and at infinity'), so (7.8) and (7.10) are limiting forms: 'where the ellipsis denotes higher-order terms that have been dropped', 'at least in the present approximation'.",
  "F&T Sec. 7 (READ): low-energy condition 2Mw << 1 for (7.6), from ref. [22] (Jensen-McLaughlin-Ottewill), and truncation to l = 0 ('only the l = 0 terms should be retained').",
  "Candelas (READ, layer): massless fields, exterior region of Schwarzschild, Boulware state defined by positive frequency w.r.t. the static Killing vector; basis functions defined by their asymptotic forms at r -> 2M and r -> oo; the relevant mode sums evaluated only in the two asymptotic regimes (Appendix A), one by direct substitution of the defining asymptotics and one by WKB."
 ],
 hypothesis_drift=[
  "NONE DROPPED (confirmed at source). The owner's 'built on Candelas' outgoing/ingoing mode sums' is exactly F&T p.18 '[21]' for (7.4)/(7.5); M > 0 and the horizon are hypotheses of every Sec. 7 input (exterior region r > 2M; up-modes emanate from the horizon; B_l is the horizon-to-infinity transmission amplitude).",
  "WORDING, over-specific but not false: 'whose basis is DEFINED BY HORIZON BOUNDARY CONDITIONS'. Candelas defines each basis function by its asymptotic form at BOTH ends, r -> 2M and r -> oo ('which have ... asymptotic forms ... r -2M ... [and] r -> oo'); the horizon end is one of the two defining surfaces, not the only one. The mode functions (7.2) themselves are cited by F&T to DeWitt [20]; Candelas [21] supplies the asymptotic sums. The first audit's point that the sum SUM|U|^2 is basis-independent stands; what the horizon controls is the existence of the two-ended r* domain and the up-family amplitudes B_l.",
  "STRENGTHENED BY THE RE-DERIVATION (new): even the NEAR-INFINITY bound (7.10) -- the form the owner names, and the one that looks continuable because it is a regular power series in 2M/r with no pole -- carries the horizon: every (2M/r)^2 and (2M/r)^3 term of (7.10), including all (tau_0/r)^2 terms, comes from the up-family contribution (1/r^2)|B_0|^2 = 16 M^2 w^2 / r^2; with that term removed (7.10) collapses to exactly 1 - 2M/r (script checks 10-11). So continuing (7.10) to M < 0 would continue a horizon transmission coefficient to a spacetime with no horizon. |B_0|^2 is even in M, so the formula would return a number: this is precisely the 'failure mode (4)' the owner refuses.",
  "SCOPE carried: (7.10) is an asymptotic, l = 0, 2Mw << 1 expansion ('+ ...'); the tree uses it only to refuse continuation, never as an exact bound at finite r. No drift.",
  "First audit's C3 (limit-circle endpoint at r = 0 for M < 0) is an additional, independent reason not named in the tree; it is this stage's computation, not a statement of F&T or Candelas (neither discusses M < 0). Recorded, not a drift.",
  "CORRECTION of the first audit, not of the tree: the first audit described (7.10) as 'the comparison form ... because its (tau_0/r)^2 coefficients are 16/9 of Pfenning-Ford's'. At source (7.10) is the near-infinity bound; the 9/64-1/4 statement accompanies both (7.8) and (7.10)."
 ],
 data_at_publication=[dict(
  quantity="None. Sec. 7 is an asymptotic mode-sum evaluation with M a free parameter; the only input the tree's refusal turns on is sign(M) (the corridor's design, M < 0).",
  value_then="n/a", value_now="n/a", source_now="n/a",
  moves_conclusion="No datum enters.")],
 rederivation=dict(
  method="sympy (+ mpmath spot check of F&T's integral (6.9))",
  script_path=FT_PY,
  outcome=("13 checks, 0 FAIL (output %s). From F&T's own printed inputs -- (7.3), Candelas' asymptotic sums (7.4)/(7.5), "
           "B_0 from (7.6) at l = 0, the Lorentzian transform (2.18), the integral (6.9) (verified numerically at nu = 3, 5, 7) "
           "and tau_0 = F^(1/2) t_0 (7.7) -- the script REPRODUCES: (i) the near-horizon bound (7.8) exactly, bracket "
           "(1/24)(2M tau_0/r^2)^2 (1-2M/r)^-1 + (9/64)(1 + (1-2M/r)), with the pole that makes it -> -oo at r -> 2M+; "
           "(ii) the near-infinity bound (7.10) through (2M/r)^3, 1 - x + x^2(1 + (16/27) y^2) - x^3(1 + (16/9) y^2), "
           "x = 2M/r, y = tau_0/r (closed form from these inputs: (1-x)(27 + 27x^2 + 16x^2 y^2 - 32 x^3 y^2)/27); "
           "(iii) the M -> 0 Minkowski limit (9/64 of Ford-Roman); (iv) the ratios 1/24 : 1/6 = 1/4 and "
           "(9/64)(16/9) = 1/4 against Pfenning-Ford (7.9)/(7.11) as F&T print them. (v) NEW: dropping the up-family "
           "term (1/r^2)|B_0|^2 reduces (7.10) to exactly 1 - 2M/r, so all its M^2 and M^3 content is horizon "
           "transmission. Not re-derived: Candelas' asymptotic coefficients themselves (the text layer drops the "
           "displayed formulas) and Jensen-McLaughlin-Ottewill's (7.6).") % FT_PY.replace('.py', '.out'),
  agrees_with_source="yes"),
 later_literature=[
  dict(ref="P. Candelas, Phys. Rev. D 21, 2185 (1980)", effect="confirms",
       what="The primary source of (7.4)/(7.5): massless fields, exterior region, Boulware state defined by positive frequency w.r.t. the static Killing vector, basis functions defined by their asymptotic forms at r -> 2M and r -> oo, sums evaluated only in those two regimes (Appendix A). Confirms 'outgoing/ingoing' families tied to the horizon.",
       read_status="READ (M-retrieved, Google Drive 1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ; OCR text layer)"),
  dict(ref="B. P. Jensen, J. G. McLaughlin, A. C. Ottewill, Phys. Rev. D 45, 3002 (1992) (F&T ref. [22])", effect="extends",
       what="Source of the low-energy greybody amplitude (7.6) that carries all M^2, M^3 terms of (7.10). Named from F&T's reference list only.",
       read_status="NAMED-NOT-READ"),
  dict(ref="M. J. Pfenning & L. H. Ford, PRD 57 3489 (gr-qc/9710055); Pfenning thesis gr-qc/9805037 (F&T refs [12],[13])", effect="confirms",
       what="The bounds (7.9), (7.11) F&T compare against; used here only as F&T print them.",
       read_status="NAMED-NOT-READ (quoted via F&T)"),
  dict(ref="G. T. Horowitz & D. Marolf, gr-qc/9504028", effect="extends",
       what="Carried from the first audit: standard reference for essential self-adjointness at timelike singularities (bears on the first audit's C3). Not read.",
       read_status="NAMED-NOT-READ")],
 lacked_data=("M's hypothesis does not bite here. Sec. 7 is an asymptotic mode-sum evaluation with M free; nothing measured "
              "since 1980/1999 enters it. What Candelas and F&T 'lacked' is not data but a construction they never "
              "attempted: a mode basis and asymptotic sums for M < 0. The re-derivation shows why none of Sec. 7 can "
              "supply it: the M-dependence of the bound beyond O(M/r) is entirely the up-family transmission |B_0|^2, "
              "a horizon quantity. Supplying an M < 0 computation would be a different theorem (and, per the first "
              "audit's C3, would need a boundary condition at r = 0), not a correction of Sec. 7."),
 grade="STANDS",
 grade_evidence=("Both sources are now read at their own pages. F&T Sec. 7 is exactly what the owner says it is: a bound "
                 "evaluated on the Schwarzschild exterior r > 2M, in the Boulware vacuum, from Candelas' outgoing/ingoing "
                 "asymptotic sums ('[21]'), with a low-energy greybody amplitude and l = 0 truncation, as limiting forms "
                 "near the horizon and near infinity. Candelas' pages confirm the families are defined by their "
                 "asymptotics at the horizon (and at infinity) and the sums are known only in those regimes. The "
                 "re-derivation reproduces (7.8) and (7.10) from F&T's printed inputs and shows the horizon enters even "
                 "the far-zone form (7.10) through |B_0|^2, so SEC7_TRANSPLANTABLE_TO_NEGATIVE_M = False is correct at "
                 "source and by computation. The only discrepancy is wording ('defined by horizon boundary conditions' "
                 "where Candelas uses horizon AND infinity asymptotics), which narrows nothing the tree uses. Not "
                 "NARROWED: the tree drops no source hypothesis and uses (7.10) only to refuse. Not WRONG: nothing "
                 "contradicts the refusal."),
 what_would_change_the_grade=("To NARROWED: a tree site that uses (7.8) or (7.10) as an exact bound at finite r, or at l > 0, "
                              "or outside 2Mw << 1 (none found; the tree only refuses). To WRONG: a published M < 0 "
                              "analogue of Sec. 7 in which the far-zone bound's M^2 terms arise without a horizon-defined "
                              "family -- contradicted here by computation (dropping |B_0|^2 leaves 1 - 2M/r)."),
 reverify_command=("python3 %s   # expect '13 checks, 0 FAIL', exit 0; source text: %s; tree side (read-only): "
                   "sed -n 56,60p %s/fewsterteo.py; grep -n SEC7_TRANSPLANTABLE_TO_NEGATIVE_M %s/fewsterteo.py %s/ledger.py"
                   % (FT_PY, CAND_TXT, TREE, TREE, TREE)),
 pages_read=["Candelas PRD 21 2185-2202: all pages of the Google Drive text layer (1mMYUbhbhSP5nw_CJ6iq2oYNTVKxZGcJZ), incl. abstract, Secs. I-VI, Appendices A-C, references",
             "Fewster & Teo gr-qc/9812032v2: pp.1-23 (Sec. 2 pp.3-6, Sec. 6 pp.14-17, Sec. 7 pp.17-19, Appendix pp.20-21, references pp.22-23)"]
))

# =====================================================================================
# 2. ahs-1995-prd51-4337  (READ-VIA-RESTATEMENT)
# =====================================================================================
RESTATERS = ("Popov hep-th/0302039v2; Taylor-Hiscock-Anderson gr-qc/9608036v1; Hochberg-Popov-Sushkov gr-qc/9701064v1; "
             "Anderson-Hiscock-Loranz gr-qc/9504019v1; Anderson-Hiscock-Taylor gr-qc/0002007v2; Popov hep-th/0109166v1; "
             "Popov-Sushkov gr-qc/0009028v1")
out('ahs-1995-prd51-4337', dict(
 name=first['ahs-1995-prd51-4337']['name'],
 source=dict(
  located=("P. R. Anderson, W. A. Hiscock, D. A. Samuel, Phys. Rev. D 51, 4337 (1995). The paper itself was NOT obtained (M "
           "could not obtain it). Its identity is fixed by the citing papers' reference lists, each READ: Popov hep-th/0302039 "
           "ref. [4] 'P. R. Anderson, W. A. Hiscock, and D. A. Samuel, Phys. Rev. D 51, 4337 (1995).'; TSH gr-qc/9608036 ref. [12] "
           "(same); HPS gr-qc/9701064 ref. [18] (same); AHT gr-qc/0002007 ref. [17] (same); AHL gr-qc/9504019 ref. [7] 'Phys. "
           "Rev. Lett. 70, 1739 (1993); Physical Review D (in press)'. A WebSearch result summary (journals.aps.org listing) "
           "gave an abstract text; it is a search-engine summary, NOT READ, and nothing below rests on it alone."),
  read_status="READ-VIA-RESTATEMENT (%s)" % RESTATERS,
  via=("alphaXiv answer_pdf_queries on each citing paper (full page sets returned): Popov hep-th/0302039v2 pp.1-2, 4-5, 8-12, "
       "14-16; TSH gr-qc/9608036v1 pp.1-18; HPS gr-qc/9701064v1 pp.1-12; AHL gr-qc/9504019v1 pp.1-14; AHT gr-qc/0002007v2 "
       "pp.1-5; Popov hep-th/0109166v1 pp.1, 3-5, 8, 10, 12-13, 15-17, 19-21; Popov-Sushkov gr-qc/0009028v1 pp.1-11. Also "
       "read, not useful for AHS content: Jiang-Zhang arXiv:2606.01980v1 pp.1-10 (cites AHS only as a DeWitt-Schwinger "
       "source and for Fourier identities), Khusnutdinov hep-th/0304176 (does not restate AHS). arxiv.org was not contacted.")),
 published_statement=(
  "AHS as RESTATED (each quote verbatim from the citing paper named): "
  "[Popov 2003 p.1] 'Using the methods of quantum field theory the expressions for <phi^2> and <T^mu_nu> of a scalar field in "
  "static spherically symmetric asymptotically flat spacetimes have been obtained by Anderson, Hiscock, and Samuel [4]. They "
  "assumed that the field is massive or massless with an arbitrary coupling xi to the scalar curvature and in a zero temperature "
  "quantum state or a nonzero temperature thermal state. The result was presented as a sum of two parts, numerical and "
  "analytical: <T>_ren = <T>_numeric + <T>_analytic. (2) The analytical part of their expression is conserved. This has a trace "
  "equal to the trace anomaly for the conformally invariant field. For these reasons they proposed to use <T>_analytic directly as "
  "an approximation for <T>_ren.' ... 'The validity of the other approximations discussed above was investigated by the authors by "
  "means of comparison with earlier known results.' "
  "[Popov 2003 p.2, Sec. II] 'the main points of the Anderson-Hiscock-Samuel approach [4] ... The integral representation for the "
  "Euclidean Green's function ... used by Anderson et al. [4] is the following: (6) ... Above, it is assumed that the field is in a "
  "zero temperature vacuum state defined with respect to the timelike Killing vector.' "
  "[Popov 2003 p.5, Sec. III] 'This approach gives (Ref. [4]) the DeWitt-Schwinger expansions of <phi^2> and <T^mu_nu> in terms of "
  "powers of 1/(mL).' "
  "[Popov 2003 p.10] 'The quantities of the second WKB order (phi^2)^(2) and the fourth WKB order (T^mu_nu)^(4) are equivalent to "
  "the analytical approximations <phi^2>_analytic and <T^mu_nu>_analytic of Anderson, Hiscock, and Samuel [4] (the constants m_DS "
  "and w_0 are equal to mu and lambda in their expressions ...)'. "
  "[Popov 2003 p.12] 'The presence in expressions (74),(78)-(80) the arbitrary parameter u_0 = w_0 r/sqrt f is a generic feature of "
  "local approximation schemes [4, 12, 15, 18, 19]. For a conformally invariant field this parameter can be absorbed into the "
  "definition of the constant m_DS.' 'When the massless conformally coupled scalar field is in a zero temperature vacuum state and "
  "propagating in static spherically symmetric asymptotically flat spacetimes the expressions (74),(78)-(80) are equivalent to ... "
  "the analytical approximation of Anderson, Hiscock, and Samuel [4].' "
  "[TSH p.3] 'Recent work by Anderson, Hiscock, and Samuel [12] has demonstrated that the DeWitt-Schwinger approximation is quite "
  "accurate so long as the radius of curvature of the spacetime is greater than the Compton wavelength of the massive field. In "
  "contrast, the various analytic approximations for massless fields are not as robust, and, in all but Ricci flat spacetimes, "
  "contain an arbitrary parameter whose value cannot be fixed except by experiment [12].' "
  "[TSH p.6] 'Anderson, Hiscock, and Samuel [19,12] have developed a method and numerical program able to calculate the "
  "stress-energy tensor of a quantized scalar field with arbitrary curvature coupling and mass in a general static spherically "
  "symmetric spacetime. ... The approximation developed amounts to an alternate derivation of the DeWitt-Schwinger approximation "
  "utilizing a WKB expansion. ... In order to obtain the expansion to order 1/m^2 it is necessary to carry the WKB expansion out to "
  "sixth order. This approximation ... was found to be exceedingly accurate in Reissner-Nordstrom black hole spacetimes as long as "
  "the product of the mass of the field, m, and the mass of the black hole, M, was greater than unity. For example, choosing Mm = 2 "
  "gave fractional accuracy ... of order 10^-2 everywhere outside the event horizon.' "
  "[TSH pp.13-14] 'This approximation has been shown to be quite accurate and robust by direct comparison with exact numerically "
  "calculated stress-energy tensors in black hole spacetimes [12].' "
  "[HPS p.3] 'For the source term in (1) we employ the stress-energy tensor of Anderson, Hiscock and Samuel, which is calculated for "
  "a quantized scalar field in an arbitrary static and spherically symmetric spacetime [18].' [HPS p.4] 'An accurate analytic "
  "approximation to the exact numerically calculated scalar field stress energy tensor was developed in Ref. [18] and is expressed "
  "there as <T>_analytic = (T)_0 + (xi - 1/6)(T)_1 + (xi - 1/6)^2 (T)_2 + (T)_log, (4)' ... 'The last factor (T)_log was left in "
  "terms of combinations of curvature tensors and covariant derivatives [20].' Footnote [20]: 'We have also set the scalar mass and "
  "temperature to zero: m = kappa = 0. In this case, the arbitrary renormalization scale parameter mu appearing in (T)_log can be "
  "absorbed into the definition of f.' "
  "[AHL p.2] 'In four dimensions the analytic approximations of Frolov and Zel'nikov [6] and Anderson, Hiscock, and Samuel [7] "
  "predict that the stress-energy tensors for conformally invariant fields and for arbitrarily coupled massless scalar fields "
  "respectively diverge on the event horizon of an extreme Reissner-Nordstrom black hole'; eq. (4) with 'mu is an arbitrary positive "
  "constant'; p.7 'numerical calculations strongly suggest that ... those in the four dimensional analytic approximations to the "
  "stress-energy tensor do not exist in the actual four dimensional stress-energy tensor'. "
  "[AHT p.3] 'They also developed the DeWitt-Schwinger approximation <T>_DS for the stress-energy of the massive scalar field, and "
  "found that the exact values of the stress-energy components were well approximated when the black hole mass M and field mass m "
  "satisfy Mm > 2 ... As the field mass is increased, the DeWitt-Schwinger approximation rapidly becomes more accurate.' "
  "[Popov-Sushkov p.1] 'the analytical approximation for <T_mu nu>, which was derived by Anderson, Hiscock and Samuel [18] on the "
  "basis of the WKB approximation for modes of a scalar field.' "
  "[Popov 2001 p.1] 'In above mentioned work [12,13] the approximations of Frolov-Zel'nikov [21] and Anderson-Hiscock-Samuel [29] "
  "were used. But as noted in [31] in spacetime that is a direct product of the Minkowski plane and a two-dimensional sphere of "
  "fixed radius these approximations are not applicable.' ([13] = HPS PRL 78 2050; [31] = Popov & Sushkov PRD 63 044017.) "
  "Owners (read): hpscentre.py:129-132 'AHS PRD 51 4337 -- NOT-REACHED ... Its hypotheses are taken ONLY as Popov, TSH and AHL state "
  "them.'; :249 AHS_REACHED = False; qeihps.py:59-61 'Source term: the Anderson-Hiscock-Samuel ANALYTIC APPROXIMATION to <T> (PRD 51, "
  "4337), their eq. (4) -- an approximation, not the exact expectation value in a specified Hadamard state.'; qeihps.py:336 "
  "HPS_STATE_HADAMARD_ESTABLISHED = False; linstab.py:66-72 '... outside the domain in which the AHS approximation has been "
  "established ... <T> an APPROXIMATION (AHS), not AMM's (2.9) with the renormalised <T_ab> of a SPECIFIED state'; throatmass.py:97 "
  "'Read Anderson-Hiscock-Samuel PRD 51 4337 first.'"),
 published_hypotheses=[
  "Spacetime class: CONFLICT BETWEEN RESTATEMENTS. Popov 2003 p.1: 'static spherically symmetric asymptotically flat spacetimes'. TSH p.6 (same authors as AHS, minus Samuel): 'a general static spherically symmetric spacetime'. HPS p.3: 'an arbitrary static and spherically symmetric spacetime'. Popov 2003's own Sec. II presents the AHS approach 'in a general static spherically symmetric spacetime' (p.2 outline).",
  "State: 'zero temperature quantum state or a nonzero temperature thermal state' (Popov p.1); the Green's function (6) as used by AHS is for 'a zero temperature vacuum state defined with respect to the timelike Killing vector' (Popov p.2); AHS's analytic expression carries the temperature kappa as a parameter, set to zero by HPS (HPS fn [20]).",
  "Field: massive or massless, arbitrary xi (Popov p.1; TSH p.6).",
  "Method: WKB expansion of the radial modes, point-splitting renormalisation; for massive fields it reproduces DeWitt-Schwinger in powers of 1/(mL), sixth WKB order for O(1/m^2) (Popov p.5; TSH p.6; Popov-Sushkov p.1). The massless analytic approximation equals Popov's fourth-WKB-order (T)^(4) with mu = m_DS and lambda = w_0 (Popov p.10).",
  "Properties claimed by AHS: analytic part conserved, trace = anomaly for the conformal field (Popov p.1).",
  "Established accuracy: massive DS -- radius of curvature > Compton wavelength (TSH p.3), RN black holes with mM > 1, 1e-2 at Mm = 2 (TSH p.6), Mm > 2 (AHT p.3); tests in black-hole spacetimes only (TSH pp.13-14). Massless -- 'not as robust', arbitrary parameter except in Ricci-flat spacetimes (TSH p.3); spurious horizon divergence at extreme RN (AHL pp.2, 6-7)."
 ],
 hypothesis_drift=[
  "NONE (hedging carried): every tree site marks AHS NOT-REACHED and uses it only in absence-of-establishment statements; the restatements confirm each of them: approximation not exact (HPS p.4 'accurate analytic approximation to the exact numerically calculated'; Popov p.1 'proposed to use <T>_analytic directly as an approximation'); massless arbitrary parameter (TSH p.3; AHL eq. (4); Popov p.12); horizon-divergence defect (AHL pp.2, 6-7); established only against black-hole numerics (TSH pp.6, 13-14; AHT p.3).",
  "DISCREPANCY BETWEEN RESTATEMENTS, now located exactly (was 'candidate' in the first audit): 'asymptotic flatness (per Popov)' (hpscentre.py owner hypothesis) is Popov 2003 p.1 verbatim, so the tree's attribution is faithful; but TSH p.6 and HPS p.3 restate the AHS METHOD for a general/arbitrary static spherically symmetric spacetime, and Popov's own Sec. II/IV re-derivation of the same expression uses no asymptotic flatness (it enters only at Sec. V, eq. (70), for the low-frequency part). Reconciled reading: the expression is derived for general SSS; its use as an approximation to <T>_ren was established only for AF (black-hole) cases. Graded in hep-th/0302039#domain.",
  "RESOLVED (first audit's UNVERIFIABLE item): qeihps.py:59-61 'their eq. (4)' is HPS's eq. (4), which HPS print as the AHS decomposition '<T>_analytic = (T)_0 + (xi-1/6)(T)_1 + (xi-1/6)^2(T)_2 + (T)_log, (4)' (HPS p.4). Whether it is also AHS's own eq. (4) cannot be seen.",
  "WORDING (carried from the first audit, now sharper): linstab.py:70-72 'not ... the renormalised <T_ab> of a SPECIFIED state'. Via Popov p.2, the AHS-derived high-frequency part 'does not depend on the quantum state', and <T>_ren = <T>_numeric + <T>_analytic (Popov eq. (2)), the state entering through the numeric/low-frequency part; for the massless conformal field in AF spacetimes Popov shows the AHS expression IS his approximation to <T>_ren in the zero-temperature (Boulware-type) vacuum (p.12). So the sentence is right as 'an approximation, not the exact renormalised <T_ab> of any specified state'; read as 'associated with no state' it would be too strong.",
  "UNNAMED BY THE TREE, favouring the tree's hedge (new): Popov 2001 p.1 states that the AHS approximation is 'not applicable' in 'a direct product of the Minkowski plane and a two-dimensional sphere of fixed radius', explicitly about the HPS work ([13]). HPS's own throat data (HPS eq. (9), read: f'(0) = f''(0) = f'''(0) = 0, r'(0) = r''(0) = r'''(0) = 0) make the metric at the throat agree with that direct product through third order in l. This is an inference from two read texts, not a sentence of either; it strengthens 'outside the established domain' and does not favour M.",
  "UNNAMED, harmless: AHS's analytic expression carries the temperature kappa (HPS fn [20]); every tree use is at kappa = 0, matching HPS."
 ],
 data_at_publication=[
  dict(quantity="arbitrary parameter of the massless approximation (mu / m_DS; Popov's lambda = w_0 absorbed into m_DS for the conformal field)",
       value_then="arbitrary; 'cannot be fixed except by experiment' (TSH p.3); 'must be fixed by experiment or observation' (Popov p.9, below eq. (55))",
       value_now="unfixed", source_now="Popov hep-th/0302039 pp.9, 12 (READ); TSH p.3 (READ); scale part separately conserved and traceless (script P4)",
       moves_conclusion="No: selects one member of a conserved traceless family; none of the tree's absence-of-establishment statements moves."),
  dict(quantity="exact numerical <T_ab> the approximation was tested against",
       value_then="Schwarzschild and RN (TSH p.6, AHT p.3); extreme RN massless (AHL): numerics show no horizon divergence where the analytic approximation predicts one",
       value_now="no restatement read reports a test in a non-asymptotically-flat or throat geometry; Popov 2001 reports the approximation not applicable in Minkowski-plane x S^2; Jiang-Zhang 2606.01980 (READ) computes exact thermal <T> on a zero-tidal wormhole but for a massive MINIMALLY coupled field, so it does not test the massless xi = 1/6 approximation HPS use",
       source_now="TSH, AHT, AHL, Popov 2001, 2606.01980 (all READ)",
       moves_conclusion="No; if anything it narrows the established domain further, in the direction the tree already takes.")],
 rederivation=dict(
  method="sympy (shared Popov script) + carried first-audit TSH checks",
  script_path=PP_PY,
  outcome=("17 checks, 0 FAIL (output %s). What bears on AHS: P3 -- Popov's (B1)-(B3), which Popov p.10 identifies with "
           "<T>_analytic of AHS, equal HPS (5)-(7) (HPS's 'AHS' source term) at the conserved reading after the one "
           "misplaced term M3 is restored; P2/P4 -- that expression is conserved identically with a separately conserved, "
           "traceless scale part (so AHS's claimed conservation holds for the conserved reading); P5 -- in AF/Boulware the "
           "high-frequency (T)^(0) cancels the low-frequency part exactly at m = 0, leaving (T)^(4) = AHS, which is the "
           "mechanism behind Popov's p.12 equivalence statement and shows where AF enters. Carried: the first audit's TSH "
           "DS re-derivations (rederive/ahs-1995-prd51-4337.py, ALL PASS). NOT re-derivable: anything printed only in AHS "
           "itself (their equation numbering, their thermal kappa terms, their own domain sentence).") % PP_PY.replace('.py', '.out'),
  agrees_with_source="yes"),
 later_literature=[
  dict(ref="Popov hep-th/0302039 (PRD 67 044021, 2003)", effect="narrows",
       what="Re-derives the AHS massless/massive analytic expression as the fourth-WKB-order high-frequency part (p.10) in a general SSS spacetime; establishes <T>_ren ~ AHS only for AF spacetimes, zero-temperature vacuum, under lambda << sqrt(f)/w_0 << L (83).",
       read_status="READ (alphaXiv, v2)"),
  dict(ref="Popov hep-th/0109166 (PRD 64 104005, 2001)", effect="narrows",
       what="'as noted in [31] in spacetime that is a direct product of the Minkowski plane and a two-dimensional sphere of fixed radius these approximations are not applicable' -- said of the AHS approximation as used by HPS.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Popov & Sushkov gr-qc/0009028 (PRD 63 044017, 2001) = Popov 2001's ref. [31] (identified by authors, title and date; the arXiv pages read carry no journal reference)", effect="narrows",
       what="Shows the approximate result depends on the choice of zeroth-order WKB solution; with its choice the <phi^2> expression 'is not approximate but exact in the R^2 x S^2 spacetime' (p.8), and in wormhole topology the leading term 'does not coincide' with the DeWitt-Schwinger one because 'the topological structures of Minkowski and wormhole spacetimes are different' (p.7). It does not itself use the words 'not applicable' about AHS.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Anderson, Hiscock, Loranz gr-qc/9504019 (PRL 74 4365)", effect="narrows",
       what="AHS massless analytic approximation predicts a horizon divergence at extreme RN that exact numerics do not show.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Anderson, Hiscock, Taylor gr-qc/0002007 (PRL 85 2438)", effect="confirms",
       what="AHS DS approximation accurate for Mm > 2 in RN; improves with field mass.",
       read_status="READ (alphaXiv, v2)"),
  dict(ref="Taylor, Hiscock, Anderson gr-qc/9608036 (PRD 55 6116)", effect="confirms",
       what="Same group; method for general SSS; accuracy criterion; massless arbitrary parameter.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Jiang & Zhang arXiv:2606.01980 (2026)", effect="extends",
       what="Exact (Levi-Ori mode-sum) thermal <T> for a massive minimally coupled field at a zero-tidal wormhole throat; cites AHS only as a DS source; does not test the massless conformal AHS approximation.",
       read_status="READ (alphaXiv, v1)")],
 lacked_data=("What AHS lacked (as the restatements show): exact <T_ab> outside black-hole spacetimes, and a value for the massless "
              "arbitrary parameter. Neither changes the tree's conclusions, which are all 'not established' statements. The "
              "later literature read here moves in the tree's direction: Popov 2001 calls the approximation not applicable in "
              "the Minkowski-plane x S^2 geometry that HPS's throat approximates, and Popov 2003 establishes it as an "
              "approximation to <T>_ren only for AF spacetimes in a zero-temperature vacuum. No evidence that missing data make "
              "AHS wrong; the known defect (horizon divergence at extreme RN) was found by the same authors in 1995."),
 grade="STANDS",
 grade_evidence=("READ-VIA-RESTATEMENT through seven citing papers, each read at its own pages, with the part each states named "
                 "above. Every use the tree makes of AHS is confirmed: an approximation, not the exact <T_ab> (HPS p.4, Popov "
                 "p.1); conserved with anomalous trace (Popov p.1; re-derived, script P2-P4); established only against "
                 "black-hole numerics (TSH pp.6, 13-14; AHT p.3); massless form carries an arbitrary parameter (TSH p.3; Popov "
                 "p.12); horizon-divergence defect (AHL); Hadamard status never addressed in any restatement (the tree's False "
                 "records an absence, uncontradicted). The one open point -- whether AHS DERIVED their expression only for AF -- "
                 "is a conflict between restatements (Popov p.1 vs TSH p.6 / HPS p.3), which the tree already hedges by writing "
                 "'per Popov'; it is graded in hep-th/0302039#domain. The HPS-specific inapplicability statement (Popov 2001) "
                 "strengthens the tree's hedge. AHS's own text remains unread; the grade rests on what the citers say it says."),
 what_would_change_the_grade=("Reading AHS PRD 51 4337 itself: if it states an asymptotic-flatness hypothesis for the derivation, "
                              "Popov p.1 is right and TSH/HPS are loose; if it does not, the tree's 'asymptotic flatness (per "
                              "Popov)' is a faithful attribution of a loose restatement (still STANDS for every use). A published "
                              "exact <T_ab> for the massless conformal field on a non-AF or throat geometry agreeing with AHS "
                              "would narrow 'outside the established domain'; none was found."),
 reverify_command=PP_RUN + "; python3 /tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/ahs-1995-prd51-4337.py; restatements: alphaXiv answer_pdf_queries on hep-th/0302039, gr-qc/9608036, gr-qc/9701064, gr-qc/9504019, gr-qc/0002007, hep-th/0109166, gr-qc/0009028",
 pages_read=["Popov hep-th/0302039v2: pp.1, 2, 4, 5, 8, 9, 10, 11, 12, 14, 15, 16 (p.3, 6, 7, 13 not returned)",
             "Taylor-Hiscock-Anderson gr-qc/9608036v1: pp.1-18",
             "Hochberg-Popov-Sushkov gr-qc/9701064v1: pp.1-12",
             "Anderson-Hiscock-Loranz gr-qc/9504019v1: pp.1-14",
             "Anderson-Hiscock-Taylor gr-qc/0002007v2: pp.1-5",
             "Popov hep-th/0109166v1: pp.1, 3, 4, 5, 8, 10, 12, 13, 15, 16, 17, 19, 20, 21",
             "Popov-Sushkov gr-qc/0009028v1: pp.1-11",
             "Jiang-Zhang arXiv:2606.01980v1: pp.1-10 (no AHS content beyond citation)",
             "Khusnutdinov hep-th/0304176v1: pp.1-3, 13, 15, 19-23, 25, 27 (no AHS restatement)"]
))

# =====================================================================================
# 3. hep-th/0302039  (B1)-(B3)
# =====================================================================================
POPOV_LOC = ("A. A. Popov, 'Analytical approximation of the stress-energy tensor of a quantized scalar field in static spherically "
             "symmetric spacetimes', arXiv:hep-th/0302039v2 (19 Feb 2003) -- confirmed from its own p.1: header "
             "'arXiv:hep-th/0302039v2 19 Feb 2003', title as above, 'Arkady A. Popov, Department of Mathematics, Kazan State "
             "Pedagogical University, Mezhlauk 1 st., Kazan 420021, Russia', 'PACS number(s): 04.62.+v, 04.70.Dy'.")
POPOV_VIA = ("alphaXiv answer_pdf_queries(hep-th/0302039) returned v2 pp.1, 2, 4, 5, 8, 9, 10, 11, 12, 14, 15, 16 "
             "(abstract, Secs. I-VI, eqs. (1)-(8), (17)-(33), (42)-(83), Appendix A (A7)-(A8), Appendix B (B1)-(B3) in full, "
             "refs [1]-[15]); pp.3, 6, 7, 13 were not returned (eqs. (9)-(16), (34)-(41), (A1)-(A6)). HPS gr-qc/9701064v1 "
             "re-read the same way, pp.1-12.")
out('hep-th/0302039', dict(
 name=first['hep-th/0302039']['name'],
 source=dict(located=POPOV_LOC, read_status="READ (alphaXiv, hep-th/0302039v2)", via=POPOV_VIA),
 published_statement=(
  "Popov (READ): p.10, after eqs. (67)-(68): 'The quantities of the second WKB order (phi^2)^(2) and the fourth WKB order "
  "(T^mu_nu)^(4) are equivalent to the analytical approximations <phi^2>_analytic and <T^mu_nu>_analytic of Anderson, Hiscock, "
  "and Samuel [4] (the constants m_DS and w_0 are equal to mu and lambda in their expressions for <phi^2>_analytic and "
  "<T^mu_nu>_analytic, respectively). In the coordinates (3) the expressions for (T^mu_nu)^(4) are given in Appendix B.' "
  "Appendix B (B1)-(B3), pp.14-16: prefactor 1/(46080 pi^2 r^8 f^4), brackets in r^2 and its derivatives, a log "
  "ln|4u_0^2/(m_DS^2 r^2)|; with u_0 = w_0 sqrt(r^2/f) (eqs. (20), (68)). As printed: (B1)'s xi-free log bracket contains "
  "'-116f'^2 f'' r^8 f' [M1]; (B3)'s (xi - 1/6)^2 log bracket opens '(2880r^4 f^4 - 21r^8 f'^4 - 8640r^4 f^4 (r^2)'' ...' and "
  "later in the same bracket carries '+ 7020r^8 f'^4' [M3: two f'^4 terms in one bracket, the small one being the misplaced "
  "term]. (B2) is printed in (r^2)' form and is dimensionally homogeneous [so M2 is in HPS, as the tree says]. "
  "HPS (READ, p.1): authors 'David Hochberg, Arkadiy Popov and Sergey V. Sushkov', Popov at 'Department of Mathematics, Kazan "
  "State Pedagogical University' -- the same author and institution as the 2003 paper. "
  "Owner (hpscentre.py:118-121, read): 'POPOV hep-th/0302039 v2 -- READ: eqs. (21), (55), (70), (83), Sec. IV, Sec. VI, "
  "Appendix B (B1)-(B3). Popov states his (T)^(4) IS the AHS analytic approximation (after eq. (67)); it is the independent "
  "second printing of HPS's source term used below.'; :139-153 the mapping 8 pi/(46080 pi^2) = K^2, 'HPS's ln f coefficient is "
  "MINUS Popov's', three disagreements M1, M2 (in HPS), M3 (in Popov), decided by conservation."),
 published_hypotheses=[
  "Popov (READ): static spherically symmetric metric (3) ds^2 = f dtau^2 + drho^2 + r^2 dOmega^2 (Euclidean); scalar field of mass m, coupling xi; 'zero temperature vacuum state defined with respect to the timelike Killing vector' (p.2).",
  "Popov (READ): (T)^(4) is the fourth WKB order of the HIGH-FREQUENCY part (w > w_0), valid under eps_WKB = |r|/(u_0 L) << 1, u_0 >> |r|/L >= 1 (eqs. (29)-(30)); m_DS arbitrary for m = 0 (below (55)); u_0 absorbable into m_DS for the conformal field (p.12).",
  "Tree restriction (read): xi = 1/6, m = 0, so the (xi-1/6), (xi-1/6)^2 and m brackets drop (exact at that point).",
  "HPS (READ): xi = 1/6, m = kappa = 0 (fn [20]), source term AHS eq. (4)."
 ],
 hypothesis_drift=[
  "CONFIRMED AT SOURCE: the tree's transcription of Popov (B1)-(B3) at xi = 1/6, m = 0 equals an independent transcription made here from the v2 text layer, all six brackets term by term (script P1). M1 (116 in Popov) and M3 (-21 r^8 f'^4 printed inside the (xi-1/6)^2 bracket) are as the tree states (P2). The log mapping (u_0 = w_0 sqrt(r^2/f) => ln|4u_0^2/(m_DS^2 r^2)| = ln(4w_0^2/(m_DS^2 f)), hence HPS's ln f coefficient is minus Popov's) follows from Popov's own (20), (68) (P3). 'After eq. (67)' is right up to the one-line definition (68) that sits between.",
  "WEAKER THAN THE TREE SAYS (wording): 'independent second printing' / 'transcribed INDEPENDENTLY'. The two printings share an author (Arkadiy/Arkady A. Popov, Kazan State Pedagogical University, on both title pages, READ). They are separately typeset -- and differ at three places, which shows they were not copied -- but not independently derived. What this changes: nothing the tree concludes, because the adjudication is by conservation (unique conserved reading (116, 21, r^2), first audit C and script P2-P3), not by agreement between printings.",
  "'IS' vs 'equivalent to': Popov writes 'equivalent to', with the constant identification m_DS = mu, w_0 = lambda. The tree's 'IS' is accurate at xi = 1/6, m = 0 where w_0 is absorbed into m_DS (Popov p.12).",
  "Already named in the tree and still standing: M1, M2 were found in the arXiv v1 text layer of HPS, not the PRL journal text; the re-read of HPS here (v1, alphaXiv) again shows '+16 f'^2 f''/f^3' in (5)'s ln f bracket and '-4 f'^2 r'^2/(f^2 r)' in (6). Must not be quoted as errors of the journal version."
 ],
 data_at_publication=first['hep-th/0302039']['data_at_publication'][:2] + [
  dict(quantity="M1 slot (tt, f'^2 f'' ln-bracket)", value_then="16 in HPS v1 text layer (READ); 116 in Popov (B1) (READ this run)",
       value_now="116, the unique value that conserves", source_now="first-audit check C; script P2-P3", moves_conclusion="no"),
  dict(quantity="M2 slot (ll, power of r)", value_then="r^1 in HPS v1 text layer (READ); Popov (B2) homogeneous in (r^2)' form (READ)",
       value_now="r^2", source_now="script P3 (HPS at r^2 == Popov)", moves_conclusion="no"),
  dict(quantity="M3 slot (thth, f'^4 ln-bracket at xi = 1/6)", value_then="+21 in HPS (READ); Popov prints -21 r^8 f'^4 inside the (xi-1/6)^2 bracket (READ)",
       value_now="+21 (HPS sign convention), the unique value that conserves", source_now="script P2", moves_conclusion="no")],
 rederivation=dict(
  method="sympy",
  script_path=PP_PY,
  outcome=("17 checks, 0 FAIL (output %s). P1: independent transcription of Popov v2 (B1)-(B3) at xi = 1/6, m = 0 == tree's "
           "hpscentre.build popov, 6/6 brackets. P2: printed Popov not conserved; with -21 r^8 f'^4 moved to the xi-free log "
           "bracket, conserved identically; printed B1 coefficient -116. P3: HPS (5)-(7) at (116, 21, r^2) == Popov with M3 "
           "restored and log sign flipped, exactly; log mapping from (20), (68). P4: scale part conserved and traceless. P5: "
           "(T)^(0) + low-frequency part cancel at m = 0 (AF/Boulware), (T)^(2) vanishes at xi = 1/6, m = 0. The first audit's "
           "31 checks (HPS parse, Einstein side, unknown-coefficient conservation, anomaly trace) stand and are not repeated.")
          % PP_PY.replace('.py', '.out'),
  agrees_with_source="yes"),
 later_literature=[
  dict(ref="Hochberg, Popov, Sushkov gr-qc/9701064 (PRL 78 2050)", effect="confirms",
       what="The other printing; shares the author Popov; its (5)-(7) equal Popov (B1)-(B3) at the conserved reading (P3).",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Popov hep-th/0109166 (2001)", effect="narrows",
       what="States the AHS approximation (as used by HPS) is not applicable in Minkowski-plane x S^2; bears on where the source term may be used, not on the printing.",
       read_status="READ (alphaXiv, v1)")],
 lacked_data=("No datum enters: 1/(5760 pi) and 1/(2880 pi^2) are pure numbers and the three slots are fixed by conservation. What "
              "the two printings lacked was typesetting redundancy by a second, unrelated author -- the reason 'independent' is "
              "narrowed to 'separately typeset'. Nothing found moves the conclusion."),
 grade="STANDS",
 grade_evidence=("Popov v2 is now read at source, including Appendix B in full. Every claim the tree makes about it checks: the "
                 "printed coefficients equal the tree's transcription term by term (independent re-transcription), M1 = 116 and "
                 "M3's placement are as stated, the log mapping follows from Popov's (20)/(68), and the identification with AHS is "
                 "Popov's own sentence (p.10). Conservation picks the same unique reading and Popov-with-M3-restored equals HPS "
                 "exactly. The one overstatement -- 'independent' when both printings carry Popov's name -- is wording that no "
                 "conclusion rests on (conservation, not agreement, decides), so it is recorded, not graded down."),
 what_would_change_the_grade=("To NARROWED: a tree site that uses the agreement of the two printings (rather than conservation) as "
                              "evidence -- none found. Reading the PRL journal text of HPS would settle whether M1/M2 survive in the "
                              "journal version; it does not bear on Popov."),
 reverify_command=PP_RUN,
 pages_read=["Popov hep-th/0302039v2: pp.1, 2, 4, 5, 8, 9, 10, 11, 12, 14, 15, 16", "Hochberg-Popov-Sushkov gr-qc/9701064v1: pp.1-12"]
))

# =====================================================================================
# 4. hep-th/0302039#domain
# =====================================================================================
out('hep-th/0302039#domain', dict(
 name=first['hep-th/0302039#domain']['name'],
 source=dict(located=POPOV_LOC, read_status="READ (alphaXiv, hep-th/0302039v2); AHS itself READ-VIA-RESTATEMENT (see ahs-1995-prd51-4337)", via=POPOV_VIA),
 published_statement=(
  "Popov (READ), the three places the tree cites: p.1 'Using the methods of quantum field theory the expressions for <phi^2> and "
  "<T^mu_nu> of a scalar field in static spherically symmetric asymptotically flat spacetimes have been obtained by Anderson, "
  "Hiscock, and Samuel [4].' Eq. (70), Sec. V p.10: 'The behavior of low-frequency modes is determined by the boundary conditions "
  "and the topological structure of the spacetime. If the spacetime is asymptotically flat and the characteristic scale of the "
  "gravitational field inhomogeneity lambda is much less than the parameter sqrt(f)/omega_0, [(70)] the low-frequency contributions "
  "to <phi^2> and <T^mu_nu> can be expanded in terms of powers of this small parameter. ... This means that we choose the long-wave "
  "modes approximately coincident with long-wave modes of the Minkowski vacuum (... the Boulware quantum state).' Sec. VI p.12: 'In "
  "this paper, analytical approximations for <phi^2>_ren and <T^mu_nu>_ren of quantized scalar fields in static spherically "
  "symmetric asymptotically flat spacetimes have been obtained. The field is assumed to be in a zero temperature vacuum state, with "
  "mass m <~ 1/L ... The necessary conditions for the validity of the analytical approximations (74),(78)-(80) are lambda << "
  "sqrt(f(rho))/w_0 << L(rho), (83) where lambda is the characteristic scale of the gravitational field inhomogeneity in "
  "asymptotically flat spacetime'; 'When the massless conformally coupled scalar field is in a zero temperature vacuum state and "
  "propagating in static spherically symmetric asymptotically flat spacetimes the expressions (74),(78)-(80) are equivalent to ... "
  "the analytical approximation of Anderson, Hiscock, and Samuel [4].' Against these: Popov p.2 outline 'In Sec. II the expressions "
  "for the Euclidian Green's function and the unrenormalized stress-energy tensor of a scalar field with arbitrary mass and "
  "curvature coupling in a general static spherically symmetric spacetime are derived.' and Sec. IV (pp.4-5, 8-10), where the "
  "high-frequency (AHS) part is computed under eps_WKB = |r|/(u_0 L) << 1 alone, with no asymptotic-flatness condition. TSH p.6 and "
  "HPS p.3 (READ) restate AHS for 'a general' / 'an arbitrary' static spherically symmetric spacetime. "
  "Owner (hpscentre.py:94-96, :299-301, read): 'Every instance fails a hypothesis under which the AHS approximation has been DERIVED "
  "OR ESTABLISHED: asymptotic flatness (Popov hep-th/0302039 p.1, eq. (70), Sec. VI).'; DOMAIN_WORD = 'established: the AHS "
  "approximation has been derived or established only for asymptotically flat spacetimes (Popov p.1, eq. (70), Sec. VI); nothing "
  "here shows it invalid'."),
 published_hypotheses=[
  "Popov's approximation to <T>_ren (74), (78)-(80): static spherically symmetric, ASYMPTOTICALLY FLAT, zero-temperature vacuum with Boulware-type long-wave modes (Sec. V), m <~ 1/L, and (83) lambda << sqrt(f)/w_0 << L.",
  "Popov's high-frequency part (= AHS at fourth WKB order): general static spherically symmetric spacetime, eps_WKB = |r|/(u_0 L) << 1 (29), u_0 >> |r|/L (30); no asymptotic-flatness condition.",
  "Equivalence <T>_ren ~ AHS: massless, conformally coupled, zero-temperature vacuum, asymptotically flat (p.12)."
 ],
 hypothesis_drift=[
  "SUPPORTED, all three citations check: p.1 attributes asymptotic flatness to AHS; eq. (70) is the AF condition; Sec. VI states the result for AF spacetimes with validity condition (83). 'Established only for AF' is what Popov's paper establishes.",
  "NARROWER THAN 'DERIVED': on Popov's own derivation, the AHS EXPRESSION is obtained without asymptotic flatness (Sec. II 'general static spherically symmetric spacetime'; Sec. IV conditions (29)-(30) only), and AF enters at Sec. V for the low-frequency part. The script's P5 shows the mechanism: in AF/Boulware the cutoff-dependent (T)^(0) cancels the low-frequency part exactly (m = 0), leaving AHS. So what is confined to AF is the claim '<T>_ren ~ AHS', i.e. 'established', not the derivation of the expression. 'Derived ... only for AF' holds only as Popov's p.1 attribution to AHS, which TSH p.6 and HPS p.3 contradict. (This confirms the first audit's z3 finding, now at source.)",
  "DROPPED FROM DOMAIN_WORD: the state (zero-temperature vacuum; Boulware-type long-wave modes, Sec. V) and the validity window (83). Both are hypotheses of what Popov establishes, and both are extra conditions the HPS instances would also have to meet; linstab.py:417-420 carries the state separately.",
  "'ONLY' is a universal negative; the read literature supports it (all tests restated are in AF black-hole spacetimes: TSH pp.6, 13-14, AHT p.3, AHL) and nothing read establishes the approximation in a non-AF spacetime. Popov 2001 p.1 goes further: 'not applicable' in Minkowski-plane x S^2, said of HPS's use.",
  "NO DRIFT toward M: the tree claims no invalidity ('nothing here shows it invalid'); the narrowing adds hypotheses the HPS instances fail too."
 ],
 data_at_publication=[
  dict(quantity="numerical input to the domain statement", value_then="none", value_now="none", source_now="n/a", moves_conclusion="no datum"),
  dict(quantity="HPS non-flatness (the instance the domain is applied to)",
       value_then="HPS p.8 (READ): 'The redshift function however, does not approach a constant value as l -> oo, so the metric as a whole is not asymptotically flat.'",
       value_now="same", source_now="gr-qc/9701064v1 p.8 (READ this run)", moves_conclusion="no"),
  dict(quantity="M_NEGATIVE_FOUND_INSIDE_DOMAIN (tree record pin)", value_then="False", value_now="False",
       source_now="hpscentre.py:274 (read); carried from first audit (selftest OK)", moves_conclusion="no; strengthened by the extra hypotheses")],
 rederivation=dict(
  method="sympy (shared Popov script) + first-audit z3",
  script_path=PP_PY,
  outcome=("17 checks, 0 FAIL. P5 locates asymptotic flatness exactly: (T)^(0) (high-frequency, cutoff-dependent, conserved, "
           "traceless) + the AF/Boulware low-frequency part (75)-(76) = 0 identically at m = 0, and (T)^(2) = 0 at xi = 1/6, so "
           "<T>_ren -> (T)^(4) = AHS only after the AF low-frequency input. The expression (T)^(4) itself (P1-P4) is conserved "
           "with no AF input. The first audit's z3 check (rederive/hep-th_0302039_domain.py: 'derived only under AF' UNSAT, "
           "'established only under AF' SAT on the tree's Sec. IV reading) is now matched by the source text."),
  agrees_with_source="yes"),
 later_literature=[
  dict(ref="Popov hep-th/0109166 (PRD 64 104005)", effect="narrows",
       what="AHS 'not applicable' in Minkowski-plane x S^2 (about HPS's use) -- narrows the domain further, in the tree's direction.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="Taylor-Hiscock-Anderson gr-qc/9608036; Hochberg-Popov-Sushkov gr-qc/9701064", effect="contested",
       what="Restate the AHS METHOD for a general / arbitrary SSS spacetime, against Popov p.1's 'asymptotically flat'; contest the 'derived' half only.",
       read_status="READ (alphaXiv)")],
 lacked_data=("The domain statement takes no datum. What would test it -- an exact renormalised <T_ab> for the massless conformal "
              "field in a non-AF static geometry compared with AHS -- is still absent from everything read; Jiang-Zhang 2606.01980 "
              "computes exact <T> on a wormhole throat but for a massive minimally coupled field. The literature that exists "
              "(Popov 2001) narrows the domain in the tree's direction."),
 grade="NARROWED",
 grade_evidence=("Read at source. The 'established only for AF' half stands, with every cited location checked (p.1, eq. (70), Sec. VI "
                 "and (83)). But DOMAIN_WORD's 'derived or established only for asymptotically flat spacetimes' is broader than the "
                 "source on 'derived': Popov derives the AHS expression in a general static spherically symmetric spacetime and "
                 "confines only the low-frequency part -- hence the approximation <T>_ren ~ AHS -- to AF, and it attaches two further "
                 "hypotheses DOMAIN_WORD omits: the zero-temperature (Boulware-type) vacuum and the window (83). So the statement is "
                 "true only when 'derived' is read as 'established' and the state/(83) hypotheses are carried. The narrowing does "
                 "not move O5: HPS's instances fail AF (HPS p.8) and the added hypotheses only enlarge what they fail."),
 what_would_change_the_grade=("To STANDS: reword DOMAIN_WORD to 'established (as an approximation to <T>_ren) only for asymptotically "
                              "flat spacetimes in a zero-temperature vacuum, under Popov (83)', or read AHS itself and find an AF "
                              "hypothesis in AHS's derivation. To WRONG: a published establishment of the massless conformal AHS "
                              "approximation in a non-AF spacetime (none found; Popov 2001 points the other way)."),
 reverify_command=PP_RUN + "; python3 /tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/rederive/hep-th_0302039_domain.py; sed -n 94,110p %s/hpscentre.py; sed -n 299,301p %s/hpscentre.py" % (TREE, TREE),
 pages_read=["Popov hep-th/0302039v2: pp.1, 2, 4, 5, 8, 9, 10, 11, 12, 14, 15, 16",
             "Hochberg-Popov-Sushkov gr-qc/9701064v1: pp.1-12", "Taylor-Hiscock-Anderson gr-qc/9608036v1: pp.1-18",
             "Popov hep-th/0109166v1: p.1 (and pp.3-5, 8, 10)"]
))

# =====================================================================================
# 5. hep-th/0302039#seciv
# =====================================================================================
out('hep-th/0302039#seciv', dict(
 name=first['hep-th/0302039#seciv']['name'],
 source=dict(located=POPOV_LOC, read_status="READ (alphaXiv, hep-th/0302039v2)", via=POPOV_VIA),
 published_statement=(
  "Popov (READ): abstract 'The field is assumed to be both massive and massless, with an arbitrary coupling xi to the scalar "
  "curvature, and in a zero temperature vacuum state. The expressions for <phi^2> and <T^mu_nu> are divided into low- and "
  "high-frequency parts. The contributions of the high-frequency modes to these quantities are calculated for an arbitrary quantum "
  "state. As an example, the low-frequency contributions ... are calculated in asymptotically flat spacetimes in a quantum state "
  "corresponding to the Minkowski vacuum (Boulware quantum state).' p.2: 'The Anderson-Hiscock-Samuel approach [4] is used for "
  "derivation of the high-frequency contributions to these quantities. Being an ultraviolet effect, the high-frequency contribution "
  "is general in the sense that its value does not depend on the quantum state in which <phi^2>_ren and <T^mu_nu>_ren are taken. "
  "This contribution contains all the ultraviolet divergences and can be renormalized. The low-frequency contributions are "
  "determined by the quantum state and, as an example, such contributions are calculated in asymptotically flat spacetime ... Both "
  "parts of <T^mu_nu>_ren are separately conserved.' Sec. IV p.4: 'In the case r_c >~ L or for a massless field a small parameter "
  "does not exist. But we can evaluate the contribution to <T^mu_nu> of the high-frequency modes. For that it is necessary to impose "
  "a lower-limit cutoff w_0 on the integrals over w'. p.9 (59): '<T^mu_nu>_WKB = lim [<T>^HFC_unren - <T>_DS] = (T)^(0) + (T)^(2) + "
  "(T)^(4) + O(1/(u_0^2 L^4))', with (T)^(0) = u_0^4/(16 pi^2 r^4) diag(1, -1/3, -1/3) (62)-(64); p.10: '(T^mu_nu)^(4) ... "
  "equivalent to ... <T^mu_nu>_analytic of Anderson, Hiscock, and Samuel'. Sec. V p.10: 'The behavior of low-frequency modes is "
  "determined by the boundary conditions and the topological structure of the spacetime. If the spacetime is asymptotically flat "
  "... (70)'. Sec. II p.2: 'Above, it is assumed that the field is in a zero temperature vacuum state defined with respect to the "
  "timelike Killing vector.' "
  "Owner (hpscentre.py:96-99, read): 'This is NOT a showing that the approximation is invalid there -- Popov (p.2, Sec. IV) shows "
  "the high-frequency part, which is the AHS expression, does not depend on the state; asymptotic flatness enters through the "
  "low-frequency part.'"),
 published_hypotheses=[
  "Static spherically symmetric spacetime (general, Sec. II).",
  "High/low-frequency split at a cutoff w_0 on the Killing-frequency integrals (Sec. IV), with eps_WKB = |r|/(u_0 L) << 1 (29).",
  "State: the computation is set up in 'a zero temperature vacuum state defined with respect to the timelike Killing vector' (Sec. II); state-independence of the high-frequency part is ASSERTED on ultraviolet grounds ('Being an ultraviolet effect', p.2; 'calculated for an arbitrary quantum state', abstract), with no state class named.",
  "The high-frequency part is (T)^(0) + (T)^(2) + (T)^(4) + O(1/(u_0^2 L^4)); AHS = (T)^(4) (p.10).",
  "Low-frequency part: fixed by the state, boundary conditions and topology; computed only for AF, Boulware-type modes, under (70)."
 ],
 hypothesis_drift=[
  "SUPPORTED: 'does not depend on the state' is Popov's own wording ('its value does not depend on the quantum state', p.2); 'asymptotic flatness enters through the low-frequency part' is Sec. V / eq. (70) verbatim in substance; the page citation 'p.2' is exact (the Sec. IV computation follows on pp.4-5, 8-10).",
  "NARROWER THAN THE TREE (resolves the first audit's candidate 2): 'the high-frequency part, WHICH IS THE AHS EXPRESSION'. At source the high-frequency part is (T)^(0) + (T)^(2) + (T)^(4) + O(1/(u_0^2 L^4)) (59); AHS is the fourth WKB order (T)^(4) only. At xi = 1/6, m = 0, (T)^(2) vanishes (script P5) but (T)^(0) = w_0^4/(16 pi^2 f^2) diag(1, -1/3, -1/3, -1/3) does not; it is conserved and traceless and cancels against the low-frequency part only in the AF/Boulware case (P5). So 'is the AHS expression' holds up to the cutoff term (T)^(0) and the WKB remainder.",
  "'SHOWS' vs 'ASSERTS': Popov asserts state-independence on ultraviolet grounds; the paper's derivation is performed inside the zero-temperature Killing-vacuum Green's function (Sec. II eq. (6)) and does not exhibit it for a named class of states. The first audit's candidate 1 (unqualified 'the state' vs 'arbitrary quantum state') is resolved in the tree's favour on wording -- Popov is equally unqualified -- but 'shows' is stronger than what the text does.",
  "UNNAMED, harmless: AHS's analytic expression carries a temperature kappa (HPS fn [20], READ); only its kappa = 0 member can be the state-independent object; every tree use is at kappa = 0.",
  "NO DRIFT toward M: the sentence is used only to refuse 'invalid' (hpscentre.py:95-96, 108-109)."
 ],
 data_at_publication=[
  dict(quantity="numerical inputs", value_then="none (analytic mode-sum split)", value_now="none", source_now="n/a", moves_conclusion="no datum"),
  dict(quantity="cutoff w_0 (Popov) = lambda (AHS); log scale m_DS = mu",
       value_then="arbitrary", value_now="arbitrary; for the conformal field absorbed into m_DS (Popov p.12)",
       source_now="script P4 (scale part conserved, traceless), P5 ((T)^(0) conserved, traceless)", moves_conclusion="no")],
 rederivation=dict(
  method="sympy (shared Popov script)",
  script_path=PP_PY,
  outcome=("17 checks, 0 FAIL. P5: (T)^(0) conserved and traceless by itself; (T)^(0) + LFC (75)-(76) = 0 at m = 0; (T)^(2) = 0 at "
           "xi = 1/6, m = 0 -- so the high-frequency part is AHS + (T)^(0) + remainder, and AF enters exactly where the tree says. "
           "P1-P4: AHS = (T)^(4) at xi = 1/6, m = 0 contains no state symbol and is conserved (with M3 restored), a necessary "
           "condition for the state-independence reading. The first audit's flat-space thermal illustration (C4) is carried, "
           "as illustration only."),
  agrees_with_source="yes"),
 later_literature=[
  dict(ref="Hochberg-Popov-Sushkov gr-qc/9701064 fn [20]", effect="narrows",
       what="AHS's analytic expression carries the temperature kappa (set to zero by HPS): the state-independent identification applies to its kappa = 0 member.",
       read_status="READ (alphaXiv, v1)"),
  dict(ref="arXiv:1809.06182 (thermal state in a long throat)", effect="extends",
       what="Carried from the first audit: title-level only.", read_status="NAMED-NOT-READ")],
 lacked_data=("No datum enters the split. The cutoff and log scale are arbitrary then and now and carry no state (P4, P5). What "
              "would test the other half of the sentence -- an exact <T_ab> in a non-AF static geometry -- is still missing. "
              "Nothing found makes Sec. IV wrong; the narrowing is about what 'the high-frequency part' contains, not about "
              "state-independence."),
 grade="NARROWED",
 grade_evidence=("Read at source. State-independence of the high-frequency part and the entry of asymptotic flatness through the "
                 "low-frequency part are both Popov's statements (p.2; Sec. V, eq. (70)). But 'the high-frequency part, which is the "
                 "AHS expression' is stronger than the source: the high-frequency part is (T)^(0) + (T)^(2) + (T)^(4) + O(...), and "
                 "AHS is only (T)^(4); at xi = 1/6, m = 0 the cutoff term (T)^(0) remains and is removed only by the AF/Boulware "
                 "low-frequency part (verified, P5). And Popov asserts, rather than shows, the state-independence. This is the "
                 "first audit's pre-registered NARROWED case ('(T)^(4) is only a truncation of the high-frequency part'). O5 does "
                 "not move: the tree uses the sentence only to refuse 'invalid', and the narrowing makes the AF dependence sharper."),
 what_would_change_the_grade=("To STANDS: reword hpscentre.py:96-98 to 'the high-frequency part, whose fourth WKB order is the AHS "
                              "expression, is stated by Popov (p.2) not to depend on the state; asymptotic flatness enters through "
                              "the low-frequency part, which in AF/Boulware cancels the cutoff term'. To WRONG: only if asymptotic "
                              "flatness entered the high-frequency part -- it does not (Sec. IV uses (29)-(30) only)."),
 reverify_command=PP_RUN + "; sed -n 93,109p %s/hpscentre.py" % TREE,
 pages_read=["Popov hep-th/0302039v2: pp.1, 2, 4, 5, 8, 9, 10, 11, 12, 14, 15, 16", "Hochberg-Popov-Sushkov gr-qc/9701064v1: pp.1-12"]
))
