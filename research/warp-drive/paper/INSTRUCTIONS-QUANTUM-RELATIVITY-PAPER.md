# Instructions for a research paper: everything that can exist is subject to relativity

**For a new session.** You are commissioned to write one exhaustive, cohesive and complete research paper on a proof
already worked in this repository. These instructions are self-contained: you have not seen the conversation that
produced the proof, and you do not need it. Everything you need is in the files named here.

## 0. The commission, in the author's words

The author (M, Matthew Lach, the byline the tree's papers use) wrote on 2026-10-16, item 431 of
`research/warp-drive/docket68/M-RULINGS-2026-10-03.md`:

> "Earlier we had worked a proof proving the relation between quantum physics to relativity. Write instructions for
> another session to write a exhaustive, cohesive, and complete research paper on this proof."

## 1. What the proof is

**The thesis (item 324, M's words, verbatim):** "everything that can exist with or without mass is subject to
relativity. - this must be proved for us to continue."

The proof was worked in `research/warp-drive/docket68/lemmas/relativity.py`, entries U0-U7:

| entry | content |
|---|---|
| U1 | What can exist carries energy and momentum: matter with and without mass, vacuum, tension, geometry, and information through its carrier (Peres and Terno). |
| U2 | Special relativity holds for every kind. Computed under a boost, and tested against GW170817. |
| U3 | Gravitation is universal: the Einstein equivalence principle, Deser's consistency argument, mass-free geodesics, and the MICROSCOPE and Cassini tests. |
| U4 | The law of the one metric. Lovelock's theorem gives Einstein's law in 4D, and in 5D one more constant, the Gauss-Bonnet coupling alpha, which Charmousis and Dufaux call "the leading order quantum correction". |
| U5 | Information is subject to relativity: quantum measurement cannot violate relativistic causality, and entanglement signals nothing. |
| U6 | The statement proved. |
| U7 | Why the cypher index is not run. |

The relation to quantum physics runs through three of these:
- U1 and U5: quantum information and entanglement live inside relativity's causal structure.
- U4: the one constant relativity leaves open is the leading quantum correction.
- The evaluation of that constant, set out below.

**It was closed by four further items:**
- **325** (`gb_alpha.py` B0-B6): alpha evaluated exactly. On the definition B6' (sigma G ell^2 = 3/(4 pi)) it is alpha
  = 0 in both bulks.
- **326** (`gb_cone.py` C0-C10): alpha = 0 from relativity's own statement.
  - With alpha nonzero, gravity's waves travel on cones split from the light cone: c_T = 3 - 2A, c_V = A, c_S = 2A - 1
    on the Boulware-Deser hole, and the same on plane waves.
  - One of those cones lies outside the light cone for either sign of alpha.
  - Camanho, Edelstein, Maldacena and Zhiboedov's acausality result corroborates it.
- **327** (`sgb_cone.py` S0-S9): the four-dimensional scalar-Gauss-Bonnet theory fails the same light-cone test for
  every f' != 0.
- **328**, M's confirmation, carried as **M-ONE-LIGHT-CONE**: everything that can exist keeps the one light cone, every
  front, at every point, on every background that can exist.

**It was verified independently** at item 332, "C9 verified: CONFIRMED with qualifications, no sub-claim refuted".
Qualifications Q1-Q9 are seated in the instruments.

**The companion: where quantum corrections begin.**
- Item 415 (`quantum_onset.py` Q1-Q6) derives where classical relativity yields to quantum gravity: x = l5^2 sqrt(K) = 1.
- It uses Buckingham's theorem on {G5, hbar, c, ell, R} and the named premises P1-P4.
- It was verified at item 430 (CONFIRMED with qualifications). One computed value was refuted: Q6's counterfactual
  onset is x = l5/ell = 1.10e-20, not (l5/ell)^(1/2).
- It belongs in the paper as the chapter on the boundary of the relation: where the two-derivative law is exact, and
  where it stops.

**Decide the remaining scope from the record, and say what you decided.**
- Items 381-382 sought "the relativity object" that would force the Higgs quartic to vanish at the 5D Planck energy.
- Read what followed in the rulings file and the WARPTHEOREM.md history.
- Include that work only as far as it was proved. List anything unproved as open, never as a result.
- If a scope question would change the paper's claim, put it to M before writing that part.

## 2. Read first, in this order

1. `CLAUDE.md` (repository root) and `research/README.md`. The tree's rules bind you: `drive/` is read-only, the tree
   is not to be scanned wholesale, and a finding is recorded, not repaired.
2. The rulings file, `research/warp-drive/docket68/M-RULINGS-2026-10-03.md`.
   - Items 101, 120, 136 (answer G), 137, 183, 249, 273, 276, 320, 322-328, 332, 415, 430 and 431 in full.
   - Items 381-383 and what follows them, for the scope decision.
   - Every M quotation you print must match this file verbatim.
3. The instruments, docstrings first:
   - `relativity.py`, `gb_alpha.py`, `gb_cone.py`, `sgb_cone.py`, `quantum_onset.py`.
   - Where they reach: `p2_offset.py` V6, `p2_assume.py`, `../bulk/bulkwarp.py` W7, `../../currency.py` and
     `../../doors.py`, which carry the item-325 to item-327 notes.
   - Read every bracketed note "[Item 3NN ...]" and "[Item 430 ...]". These are the corrections, kept beside the text.
4. `research/warp-drive/docket68/WARPTHEOREM.md`: the history entries for items 323-332, 415 and 430.
5. `papers/method/PAPER-SPEC.md` and one paper directory under `papers/method/`, as the house model of a paper with a
   machine check, a source map and an audit. Also read `research/warp-drive/paper/THE-HIERARCHY-LAW.md` for the
   research tree's own paper style and byline.

Record the md5 of every file you rely on when you start. Report any file that changes under you.

## 3. Reproduce before you write

- Run every instrument's `--selftest` and `--mutants` with `PYTHONDONTWRITEBYTECODE=1`. Record the counts; do not
  copy them from this page or from the docstrings.
- sympy is needed, and z3 where an instrument uses it (`pip install z3-solver`).
- Every number the paper prints must come from a run you made, or be stated as READ with its source and page.
- Write the paper's own machine check, `research/warp-drive/paper/qr_paper_check.py` (stdlib plus sympy).
  - It imports the instruments by path (never copies them) and asserts each number and each identity the paper
    prints.
  - It has `--selftest` and `--mutants`. Every mutant must be caught for the reason it tests, and the check must be
    able to fail.

## 4. Re-READ every outside source at source

The record READ these. You must READ each again before citing it: a verbatim quotation with page or equation, from
the paper itself. arxiv.org does not answer from this container's shell. Use the Firecrawl scrape tool on the
`arxiv.org/abs/<id>` page for abstracts, and alphaXiv's `get_paper_content` (with `fullText`) for full text.

| source | id | used for |
|---|---|---|
| Peres and Terno | quant-ph/0212023 | information needs a material carrier; no superluminal signalling |
| LIGO-Virgo, Fermi, INTEGRAL (GW170817) | 1710.05834 | one speed for gravity and light; Shapiro delay for gravitational waves |
| Will | 1403.7377 | the Einstein equivalence principle and metric theories |
| Deser | gr-qc/0411023 | universal coupling from consistency |
| MICROSCOPE | 2209.15487 | the universality of free fall to 1e-15 |
| Navarro and Navarro (Lovelock's theorem) | 1005.2386 | the second-order natural tensors |
| Charmousis and Dufaux | hep-th/0202107 | the 5D Gauss-Bonnet braneworld, eq. (22); "the leading order quantum correction" |
| Reall, Tanahashi and Way | 1406.3379 | gravitons' characteristic cones in Lovelock theories |
| Camanho, Edelstein, Maldacena and Zhiboedov | 1407.5597 | the Gauss-Bonnet causality violation |
| Reall | 2101.11623 | the effective metric, eq. (91) |
| Serra, Serra, Trincherini and Trombetta | 2205.08551 | scalar-Gauss-Bonnet causality |
| (cited at 332) | 1904.13091 | the scalar-Gauss-Bonnet theories with V = 0 |
| Ida | gr-qc/9912002 | Israel's junction between two bulks |
| Haggard and Rovelli | 1407.0989 | the quantum-gravity criterion q = l_P R tau (430 (Q4)) |

Cite nothing the record did not READ unless you READ it yourself, and say so. A failed or partial read is said, not
filled.

## 5. Claims stay inside their evidence (the qualifications you must carry)

**From the C9 verification (332):**
- **Q1.** "Relativity alone" is valid only under M-ONE-LIGHT-CONE (328). U6's "keeps the light cone in every frame" is
  U2's: flat-space boost invariance and GW170817's near-flat speed. It proves nothing of curved backgrounds' cones.
  State M-ONE-LIGHT-CONE as a postulate of the paper, the author's, named.
- **Q2.** CEMZ constrain alpha >> l_P5^2 only, at tree level. They corroborate the cone result in that range only.
- **Q3.** C5's divisor vanishes at 8 alpha k1^2 = 1. "For either sign" holds within the existence range.
- **Q4.** The cone split is computed on the families named (static pair-diagonal bulks, type N waves) and is generic
  per RTW. It is not shown wherever the Weyl curvature is nonzero.
- **Q5.** sgb_cone's "every f' != 0" needs V(phi0) = V'(phi0) = 0.
- **Q6.** S3's "either sign of f'" is a reflection; the sign of c_T^2 - 1 is set by f.. and f. (8 f.. = 1363/11525)
- **Q8.** gb_alpha B2-B5 are exact as an evaluation of definitions, and B5 is vacuous.
- **Q9.** The minor items as listed.

**From the interior verification (430), for the quantum-onset chapter:**
- **Q1.** Q6's value is wrong as written. The conclusion holds a fortiori.
- **Q2.** "Each term a positive power of x" is an assumption about the form of the expansion.
- **Q3.** The 4D placement holds only where the 4D form holds.
- **Q4.** Haggard and Rovelli's criterion is q = l_P R tau. "Only x decides" stands by x ~ 31 q^2, not by Q4's
  comparison of times.
- **Q5.** A bound on K is not a bound on all curvature.

**From the instruments' own "does not prove" lists:**
- The experiments bound departures only to their precision.
- Lovelock's and Deser's theorems hold on their premises (locality, second order, consistency).
- Einsteinian cubic gravity and f(R) were not cone-tested.
- A kind of thing with no energy and momentum is outside the claim.

**Labels.** Every statement carries its status: computed (exact unless marked), deduced, READ, estimate, or the
author's postulate. M's rulings enter as the author's postulates, each named and quoted. They are never presented as
derived results.

## 6. The paper

**Location.** `research/warp-drive/paper/`, as Markdown beside the tree's two existing papers, with the check script.
A PDF render is optional and comes after the audit.

**Title.** Propose one; titles are the author's to settle. Mark yours "proposed".

**A structure to adapt, not a template to fill:**
1. **Abstract.** The thesis, the method (kind-by-kind proof, exact computation, outside results READ), the two results:
   relativity as a consequence, and alpha = 0. The boundary where quantum corrections begin. The limits.
2. **Introduction.** The question of how quantum physics relates to relativity, posed as the author poses it. What is
   proved and what is postulated.
3. **Postulates and definitions.** Each of M's rulings used, quoted and named.
4. **What can exist** (U1).
5. **Special relativity for every kind** (U2), with the computations and the tests.
6. **The universality of gravitation** (U3).
7. **The law of the one metric** (U4): Lovelock in four and five dimensions; the Gauss-Bonnet coupling as the leading
   quantum correction.
8. **Information and entanglement** (U5): quantum measurement within relativistic causality; information as energy
   and as area.
9. **The statement** (U6), its exact scope, and why the cypher index is not run (U7).
10. **The coupling evaluated** (325, 326): by the definitions, and by the one light cone. The cones c_T, c_V, c_S and
    the sum rule; plane waves; CEMZ.
11. **The scalar-Gauss-Bonnet branch excluded** (327), and what that does to the older instruments' findings: they
    stand as findings about that theory, not repaired.
12. **Where quantum corrections begin** (415): x = 1, the premises P1-P4, and what P4 adds.
13. **Verification:** the two independent verifications (332, 430), what each re-derived, and every qualification.
14. **What is not proved.**
15. **Relation to the research tree:** what in the warp record rests on this proof, stated plainly, without the
    record's internal row names as evidence.
16. **References**, each READ, with identifier and page.

**Appendices:**
- (A) every computation, with the instrument entry and check that carries it;
- (B) M's words verbatim, with item numbers;
- (C) the source map: each claim mapped to file, check, run output or READ quotation;
- (D) reproduction steps and the md5 table.

"Exhaustive, cohesive, complete" means:
- every step of U0-U7, 325-327 and 415 is in the paper, with its evidence;
- every qualification is carried where its claim is made;
- the argument reads as one line from the question to the result;
- nothing the record proved is left out, and nothing it did not prove is claimed.

## 7. Audit, then report

- When the draft and its check pass, send **one** independent verifier agent (M's item 249: one verifier at a time).
  - Give it the paper, the check, the instrument files and their md5s.
  - Tell it to work read-only, to re-derive with its own code, and to re-READ the quotations.
  - Check its actual status before you report on it.
- Run a critic in the conversation on its findings. Seat every finding beside the text, or answer it with a reason.
- Then report to M:
  - what the paper claims and on what;
  - what the verifier found;
  - what is left to the author (title, any scope question).
- Work in the conversation; do not launch multi-agent workflows (M's standing rule).
- Keep lines at 121 characters or fewer in text and code. Put no model identifiers in any file.
- Commit and push on your session's designated branch, with the commit trailers your session gives you.
- Do not edit the instruments under `docket68/` or the rulings file. If you find an error there, record it in the
  paper and report it to M; the board seats corrections beside the text.
