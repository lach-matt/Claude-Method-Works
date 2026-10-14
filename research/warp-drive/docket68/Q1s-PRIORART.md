# The Q-1s prior-art gate (PAPER-BRIEF-Q1s.md §3 step 1; 2026-10-05)

M's condition (2026-10-04, verbatim, in the brief): *"The paper is not a priority, just an additional if the math concept
is novel or introduces new theorems/proofs not otherwise previously published art"*. The brief makes the prior-art
search the gate: "If that search finds that every item in section 2 is already published, the session reports this to
M and writes no paper." M ordered it run before H-CMB-CORRIDOR (M-RULINGS item 42, "3, then 1").

**No paper is written here.** This file grades the brief's §2 items 1–6 against what was read. Every source is listed
with id, version, pages and route. Copyrighted text is kept to short phrases with page numbers.

**How the search ran.** Three independent readers searched, one per angle: the functional-equation and polylogarithm
literature; information cohomology and categorical characterisations; signed and quasi-probability entropy. The lead
then re-read at source the four sources a verdict turns on: Brandenburger–La Mura v3, Cathelineau 1996, Im–Khovanov,
and (already in Q1s-signed.md) Kontsevich and BFL.

**A negative result is a floor.** "Not found" means not found in what was read. It is not a proof that nobody has
published it. Everything paywalled or not reached is listed in §4.

## 1. The verdict, item by item

| brief §2 item | what is already published (cite, do not claim) | what was not found (candidate contribution) | grade |
|---|---|---|---|
| **1. Finite-set Re H, Im H = πN, range for given (n, N)** | **The definition:** H with the principal complex log, Re = −∫W ln\|W\| and Im = π × the negative volume, continuous (Cerf–Hertz–Van Herstraeten 2310.19296v1 pp.5–7). **On finite sequences of reals:** H(a) := Σψ(aᵢ) − ψ(Σaᵢ) with ψ(a) = −a log\|a\| (Im–Khovanov 2409.08462v2 p.43, eq. 4.6); for Σa = 1 this is exactly Re H. Complex −Σ P log P, definition only (Li–Xu–Cao 2503.03759v1 p.9) | The exact range of Re H for given (n, N): negative Re H is forced only at n = 2; min over N of max Re H is ln(n − 2); Re H has no ceiling at ln n. The per-entry branch accounting | **PARTIAL.** The definition is prior art; the range results are a candidate |
| **2. BFL's axioms on signed measures** | **BFL itself is nonnegative only:** "All measures on a finite set X will be assumed nonnegative" (1106.1791v3 p.3); the codomain is [0, ∞) (Thm 2, p.4). **The signed category, Re H's functoriality:** Im–Khovanov extend BFL's FinProb to a category C_H of real-weighted lines, on which the entropy cocycle is additive under composition. FinProb is a subcategory, "a small part" of it (2409.08462v2 pp.70–72); whether the bigger category bears on probability is left as a question (p.72) | **The characterisation:** over continuous separable functionals the axioms force c·Re H + b·N. Product additivity leaves Re H; the codomain leaves b·N; the codomain fails with computed counterexamples. None of this is in Im–Khovanov's pages read, BFL, Baudot–Bennequin, Vigneaux, or Brandenburger–La Mura | **NARROWED, still a candidate.** That the signed category exists, and that Re H is functorial on it, must be cited (Im–Khovanov). The characterisation and the span were not found |
| **3. N is convex-linear but fails signed recursivity** | **Uniqueness of Re H on two entries over all of ℝ under signed recursivity:** Kontsevich, "only one (up to a scalar factor) nonzero continuous solution", a sketch (math/0008089v1 appendix p.43); Elbaz-Vincent–Gangl Prop. 2.13 (same paper p.10); Im–Khovanov restate it on ℝ → ℝ (2409.08462v2 p.43). **Existence on ℂ:** z log\|z\| + (1−z) log\|1−z\| satisfies the four-term equation (Cathelineau 1996, Ann. Inst. Fourier 46:1327, p.1327). **Symmetry is needed:** F(π) = π also solves the fundamental equation (Leinster 1903.06961v3 Rem. 9.6, p.27). **Without measurability, uniqueness fails:** derivation-built solutions (Im–Khovanov p.43 Rem. 4.1, p.49 Rem. 4.7) | That N meets BFL's convex linearity yet fails Kontsevich's signed recursivity. Hence BFL admits span{Re H, N} while recursivity admits Re H alone: the two axiom systems separate on signed measures | **PARTIAL.** The recursivity half is prior art; the separation is a candidate |
| **4. Brandenburger–La Mura's two weightings** | **The \|w\| half is their theorem:** signed Rényi, Theorem 1 (2410.15976v5 p.4). They exclude −Σ\|p\| log\|p\| for failing extensivity (v5 p.4; v3 p.4 Example 1) | **The signed-w half:** under the signed-weight mean-value axiom, Re H is the α = 1 member. Its conditional separation from \|w\| under H-BFL-BINDS was not found. See the discrepancy in §2 | **Candidate,** framed as completing a reading that BLM's own v3 states but does not prove |
| **5. Signed relative entropy D_s, ground-calibrated** | ∫W ln\|W/q\| against a Gaussian q, continuous (Pizzimenti et al. 2303.00880v3, as Re μ; reader-read). Contrast: Koukoulekidis–Jennings's Rényi divergences keep Gibbs and data processing (2106.15527v2; reader-read). Baez–Fritz's relative-entropy characterisation is for probability distributions only (1402.3067v2, in Q1s-signed.md) | The finite-set D_s axiom profile: it keeps additivity, convex linearity and the chain rule, and fails Gibbs non-negativity and data processing. The vanishing cross-term condition. The calibration to READ mass and binding data | **Candidate,** a narrow one: the continuous functional exists |
| **6. Triangulation (reconstruction from projections)** | Optical homodyne tomography and filtered back-projection (Lvovsky–Raymer quant-ph/0511044v2 pp.3–9). Exact discrete reconstruction (Gibbons–Hoffman–Wootters quant-ph/0401155v6 pp.23, 27) | Nothing new as principle | **PUBLISHED.** An application, as the brief already says |

**The gate result:** not every §2 item is published. The candidate contributions that survive the search are:
- item 1's range results;
- item 2's characterisation, now narrowed against Im–Khovanov;
- item 3's BFL-versus-recursivity separation;
- item 4's signed-w half;
- item 5's finite-set axiom profile.

Item 6 is published. **By M's condition the paper is therefore permitted, not required.** Scope and venue are M's
(brief §3 step 3).

How strong the case is, stated both ways:
- The surviving items are careful and modest. Item 2 is, in a reader's assessment, a fairly direct adaptation of BFL's proof. The definition, the
  signed-weight category and the two-entry uniqueness are all prior art.
- What survives is still a set of theorems not found anywhere read. Items 1 and 3 in particular are exact statements
  with machine-checked algebra in `signed.py`.

## 2. Discrepancies found (recorded, not refutations)

1. **The lead gave the readers a wrong arXiv id for Elbaz-Vincent–Gangl.** math/0101182 was in the lead's instructions
   to the readers. The paper is **math/0008089v1** (Compositio 130, 2002), the id Q1s-signed.md already cites. A reader
   caught it. No repository file states the wrong id other than this line (checked with grep over `research/`).
2. **Brandenburger–La Mura v3 (2410.15976v3, dated 06/01/25):**
   - Axiom 5, eq. (9) (p.3), is stated with the signed weight w(P) = Σpᵢ.
   - The proof's first step, eq. (41) (p.10), writes the weights as |pⱼ| and the denominator as |Σpⱼ|.
   - v5's Axiom 5′ (Q1s-signed.md: "eq. (9) with |w| and the summed denominator", pp.3–4) states the |w| form outright.
   - So v3's theorem proves the |w| reading while its axiom states the signed one. v5 aligns the axiom with the proof.
   - Read by the lead at source (alphaXiv, v3 pp.3–4 and 9–11). This is a discrepancy between an axiom and its proof
     in one version, corrected in a later one. It is not a refutation of BLM's theorem.
3. **Lee 1964's scope.**
   - Im–Khovanov cite Lee (Ann. Math. Statist. 35:415) for uniqueness "as a function R → R" (2409.08462v2 p.43).
   - Leinster's *Entropy and Diversity* (2012.02113, p.366, reader-read) places Lee's theorem on probability
     distributions.
   - Lee is paywalled and NOT READ, so which reading is right is **OPEN**. Item 3's grade does not depend on it,
     because Kontsevich and Elbaz-Vincent–Gangl already cover ℝ.

## 3. Sources read, with routes

| source (id, version) | pages | route | used for |
|---|---|---|---|
| math/0008089v1 Elbaz-Vincent, Gangl; appendix by Kontsevich | 2, 10–13, 42–44 | alphaXiv (two readers independently; already in Q1s-signed.md) | items 3, 4 |
| 1106.1791v3 Baez, Fritz, Leinster | 3–5, 7–8 | alphaXiv (two readers; already in Q1s-signed.md) | item 2 |
| 2409.08462v2 Im, Khovanov (JPAA 230, 2026) | 1–3, 43–44, 49, 51, 55, 61, 64, 66–70, 72–73, 75, 77–79 | alphaXiv, lead. Found through Cathelineau 1996's "cited by" list on centre-mersenne | items 1, 2, 3 |
| Cathelineau, Ann. Inst. Fourier 46 (1996) 1327–1347, doi 10.5802/aif.1551 | 1327–1347 (full) | centre-mersenne / Numdam open PDF, lead and reader | item 3 (existence on ℂ; char-0 presentation of β₂, Prop. 6, p.1337) |
| 2410.15976v3 Brandenburger, La Mura | 1–13 (full) | alphaXiv, lead | item 4, discrepancy 2 |
| 2410.15976v5 Brandenburger, La Mura | 3–4, 9–11 | alphaXiv (already in Q1s-signed.md); reader | item 4 |
| 2310.19296v1 Cerf, Hertz, Van Herstraeten | 5–8, 13 | alphaXiv (already in Q1s-signed.md); reader | item 1; N's product law |
| 2503.03759v1 Li, Xu, Cao | 9 | alphaXiv, reader | item 1 (definition only) |
| 1903.06961v3 Leinster, *Entropy modulo a prime* | 1–4, 8, 10, 16, 26–27 | alphaXiv, two readers | item 3 (Rem. 9.6; the mod-p contrast, Thms 5.1, 6.4) |
| 2012.02113 Leinster, *Entropy and Diversity* | 58, 366 | arXiv, open by agreement with CUP, reader | item 3; discrepancy 3 |
| Baudot, Bennequin, Entropy 17 (2015) 3253, doi 10.3390/e17053253 | Thm 1 and the simplex definition | MDPI open access, reader | item 2: positive simplex only |
| 1709.07807v4 Vigneaux; his thesis (2019, jpvigneaux.github.io); 2003.02021 | eq. 39 p.28, Thm 4.5.4; thesis Thm 3.10 p.85, fn. 5 p.20 | arXiv and the author's page, reader | item 2: [0,1] and Δ² only |
| Maksa, Ng, Publ. Math. Debrecen 33 (1986) 9–11 | full | open scan, reader | item 3: open triangle in ]0,1[ only |
| 1307.0816 Gselmann, Maksa (survey); 1307.0655 Gselmann | domains | alphaXiv, reader | item 3: every domain in [0,1] or the positive cone |
| 2303.00880v3 Pizzimenti et al. | as cited by the reader | alphaXiv, reader | item 5 |
| 2106.15527v2 Koukoulekidis, Jennings | as cited by the reader | alphaXiv, reader | item 5 (contrast) |
| quant-ph/0511044v2 Lvovsky, Raymer; quant-ph/0401155v6 Gibbons, Hoffman, Wootters | as in Q1s-signed.md | alphaXiv (earlier waves) | item 6 |

No paywall was met on any arXiv source. No 403 was met this pass.

## 4. NAMED-NOT-READ (paywalled or not reached; nothing circumvented)

- **Books:** Aczél–Daróczy (1975); Aczél–Dhombres (1989); Ebanks–Sahoo–Sander (1998). Secondary sources place their
  results on [0,1] or ]0,1[ᵏ.
- **Lee**, Ann. Math. Statist. 35 (1964) 415 (discrepancy 3).
- **Cathelineau**, Math. Scand. 63 (1988) 51–86. EuDML lists it; not fetched. Cathelineau 1996 p.1337 cites it for
  Prop. 6.
- **Paywalled journal papers:** Sander, Aeq. Math. 33 (1987); Ebanks, Aeq. Math. 51 (1996), whose keywords read
  "positive cones in ordered fields"; Kannappan–Ng (1973); Jessen–Karpf–Thorup (1968).
- **Daróczy (1970):** abstract only.
- **Not fetched:** Rényi (1961) and Daróczy (1963) (H-RD stands); Brandenburger–La Mura–Zoble, Entropy 24 (2022)
  1412.
- **Negative probability:** Feynman (1987), Bartlett, Khrennikov, Mückenheim.

## 5. What this changes

- **Q1s-signed.md OPEN 4** is answered by this file, for the search as run.
- **`paper/CLAIMS.md` is untouched.** Q-1s moves no obstruction grade, and the brief forbids DOCKET 68 material in the
  Q-1s paper.
- **If M orders the paper**, every item graded PARTIAL or NARROWED must cite its prior art in the paper's introduction.
  That means Im–Khovanov for the signed category and for H(a) on real sequences; Kontsevich, Elbaz-Vincent–Gangl and
  Cathelineau for two-entry uniqueness; Cerf–Hertz–Van Herstraeten for the definition. The brief's §5 ("what the paper
  must not say") gains one line: the signed-weight extension of BFL's category, with Re H functorial on it, is not new.

## 6. M's ruling on the gate

M-RULINGS item 43 (2026-10-05): shown this gate and asked whether to write a paper and in what form, M ruled **"No
paper"**. The Q-1s paper question is closed. The grades above stand as a record. `signed.py` and Q1s-signed.md are
unchanged, and PAPER-BRIEF-Q1s.md is kept as a record of the brief, not as an open instruction.
