# READ-ch13g.md — Phase R2, chat 80, segment 3: main §14.1–§14.4 (L3679–3731)

Range: `## 14. Closure` (L3679) through `### 14.4 The three consequences` and its single sentence (L3729–3731), to the line before `### 14.5` (L3732). Instrument: `r2-ch13g.py` (banked, r2-ch13g.out 2,634 B · md5 aa32f589… · ≈ 3 s). Clerical: `r2-tools.py lines|pointers|figures|census|layout 3679 3731` — census rows in range: 1 (row 693); manual grep for lowercase `register NNN`: L3700 `register 400` and L3709 `224` (both resolved below); `A.N`: A.2 at L3683, L3686, L3709. Six pointers resolved to heading **and** claim. `Rset` lifted from r2-ch12r's Rbox with provenance, returning the set ℛ(X) rather than its size, because the three axioms are statements about the set. Findings are recorded, never repaired (chat 67 hold).

## A — deviations

**13g-01 · L3724–3727 — the bundling test does not reproduce, and the sentence's evidence points against its claim.** PRINTED: `What fails is bundling. ℛ reconstructs coordinate by coordinate, so folding two chains into one non-chain coordinate hides structure from it. In tests, the same sets presented bundled and presented decomposed both gave 80/80 agreement — the theorem survives, but only when the presentation respects it.` MEASURED (r2-ch13g §4): every one of the **28** pairs of Λ₈'s coordinates folded into a single coordinate by the lexicographic rank of the pair, against the decomposed presentation's E = 0 at all of them — **26 of 28 disagree**, with defects from 8 to 554:

| bundled pair | values | E | | bundled pair | values | E |
|---|---|---|---|---|---|---|
| (n, ℓ) | 5 | 188 | | (q, e) | 12 | 159 |
| (n, k) | 8 | 526 | | (q, f) | 8 | 168 |
| (n, q) | 11 | 554 | | (q, 2S) | 16 | 125 |
| (n, e) | 9 | 172 | | (e, f) | 5 | 8 |
| (n, f) | 6 | 116 | | (e, g) | 11 | 483 |
| (n, g) | 11 | 487 | | (e, 2S) | 12 | 180 |
| (n, 2S) | 11 | 135 | | (f, g) | 7 | 297 |
| (ℓ, k) | 5 | 120 | | (f, 2S) | 8 | 180 |
| (ℓ, q) | 7 | 290 | | (g, 2S) | 16 | 225 |
| (ℓ, e) | 6 | 120 | | (k, q) | 9 | 195 |
| (ℓ, f) | 4 | 72 | | (k, e) | 9 | 162 |
| (ℓ, g) | 7 | 225 | | (k, f) | 6 | 120 |
| (ℓ, 2S) | 7 | 45 | | (k, g) | 9 | 275 |

The only two that agree are **(k, 2S)** and **(q, g)** — the two pairs joined by a constraint of §7.1, where folding loses nothing because the pair is already determined. So the mechanical reading confirms the *claim* (`bundling hides structure`) and refutes the *evidence offered for it* (`80/80 agreement`). The population of the 80 is printed in no member — as with 12x-01 and 13e-04, a witness named without its data. For R3: state which sets the 80 were, and note that agreement under bundling is the exception, not the rule; the sentence as printed reads as though bundling were harmless.

**13g-02 · §14.4 (L3729–3731) — the stub, and the four sites that lean on it. Closes 12h-01.** PRINTED, in its entirety: `### 14.4 The three consequences` / `Closure yields three properties, developed in the next three chapters:` — a colon that opens nothing, followed immediately by `### 14.5`. MEASURED: the three properties are never listed; the `next three chapters` are Chapter 15 (`Self-reference — alphabet, order, bounds`, L4270), Chapter 16 (`Self-defence — data, derivation, totality`, L4332) and Chapter 17 (`Extension — cells, axes, constraints`, L4789), so the referent is recoverable but unstated. Four sites treat §14.4 as though it carried an admissibility criterion: main L3085 `Every bound is §14.4-admissible`, L3096 `2S′ ≤ 2f+1 is §14.4-admissible`, L3367 `a symmetric non-constant function is not monotone, so §14.4 cannot carry it`, and MC L1254 `the admissibility condition (§14.4)`. The condition those four need — monotone one-parent bounds only — is printed at **§17.2 L4800–4802** (measured in chat 78), not at §14.4. For R3: either §14.4 states its three consequences and the admissibility condition, or the four sites point at §17.2.

## B — verified

- **L3712 the three axioms.** ℛ (the φ̂ operator of §6.1) measured on a family of **150** sets — the four q-fibres, eight coordinate half-spaces, Λ₈ itself and 137 seeded random subsets of sizes 5 to 400: **extensive 150 of 150, idempotent 150 of 150**, and **monotone 75 of 75** nested pairs X ⊆ X ∪ Y (both sides tested). No failure of any axiom. The printed `150 of 150 on all three axioms` reproduces on an independently built family; the book's own 150 sets are not printed, so the agreement is of result, not of population.
- **L3714–3717 the defect.** E(Λ₈) = |ℛ(Λ₈)| − |Λ₈| = **0** against an ambient box of 6,912 cells; the periodic table's 36 is Chapter 6's figure, cited here and not recomputed in this segment.
- **L3720–3722 the scope.** Every coordinate of Λ₈ is presented as a chain — n {1,2,3}, ℓ {0,1}, k {1,2,3}, q {0..3}, e {1,2,3}, f {0,1}, g {0..3}, 2S {0..3} — so Theorem 14.1's hypothesis holds as stated, and the Birkhoff restatement is exact here: Λ₈ has **17** join-irreducibles, one chain per irreducible, matching §8.3's seventeen generators and §12.9's chain length of seventeen (13f B).
- **L3683–3691 the attribution of A.2.** Bergman's Double-projection Theorem, `itself a consequence of Baker and Pixley (1975)`, is carried identically at L8127–8129 and at §29.11 L8865, and Register **224** (Register L895) states it in the same words — `A.2 — X closed ⟺ ℛ(X) = X — is Bergman's Double-projection Theorem specialised to products of chains, itself a consequence of Baker–Pixley 1975. Correct, and fifty years late.` The References carry Baker & Pixley (1975), *Math. Z.* **143**, 165–174 (L11699) and Bergman's entry (L11704).
- **L3693–3700 the mis-citation, corrected.** Freuder 1982 is `A sufficient condition for backtrack-free search`, *JACM* **29**(1), 24–32 (References L11528), cited there `for backtrack-free search at strong (w+1)-consistency on a graph of width w. **Not** for global consistency, which this book previously attributed to it`; Montanari 1974, *Inf. Sci.* **7**, 95–132 and Dechter 1992, *Artif. Intell.* **55**(1), 87–107 are both listed, Dechter `for … decomposability — the result §14.1 had been crediting to Freuder`. Register **400** (Register L1487) records the correction in those terms. The correction chain is complete and consistent at all three places — text, References, Register.
- **L3702–3706 the constraint class.** Deville, Barták and Van Hentenryck (1999), *Artificial Intelligence* **109**, 243–271, `Constraint satisfaction over connected row-convex constraints`, is in the References and cited for the staircase class; Register **401** (Register L1491) records it. §6.1 (L1532) is the operator's home, so `the operator of §6.1 has been building a named object since Chapter 6` resolves.
- **L3708–3709 the finding's home.** `the development is at A.2; the register carries the finding at 224` — Register 224 resolves as above; A.2 is Appendix A's item 2, not a heading, which is why r2-tools reports it UNRESOLVED (the same tool artefact as §4.6 in READ-ch13e).
- **Census row 693** — C7-WITHDRAWAL-LINE-NUMBER-SURVIVES at L3700, flagged token `400`: a live Register citation (`recorded at register 400`), and Register 400 exists and carries the claim. Regex artefact by the standing precedent (678, 680–687, 1067, 1069); closed as **not a defect**.

## C — incidental

- The References entry for Bergman (L11704) gives no year and no venue, where every neighbouring entry gives both; §14.1 likewise names `Bergman's Double-projection Theorem` without a date while dating Baker and Pixley to 1975. R-ATTR asks for every attribution that can be made; the year is available (the double-projection result is G. M. Bergman's, 1977). For the References pass, not this segment.
- L3691's `The proof in §16.1 is correct and fifty years late` resolves to §16.1 `The counting argument` (L4335); the phrase `fifty years late` measures against Baker–Pixley 1975 and is the same wording as Register 224's.
- §14.1 is four dense paragraphs of prior art with no figure of its own; every number in the segment (17, 0, 36, 150, 80) is either measured above or record-carried from a named chapter.
- No layout defects in range — the first four subsections of Chapter 14 are clean prose, unlike §13.3's table.
