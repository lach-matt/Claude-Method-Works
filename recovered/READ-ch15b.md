# READ-ch15b — Chapter 26, *Collective sections* — main L7117–L7202

Chat 104. Boundaries MEASURED by heading scan on `The_Method_1_6-2.md` before a line was read:
`## 26. Collective sections` opens at **L7117**, `## 27. Slack` at **L7203**, so the chapter is
**L7117–L7202, 86 lines, seven `###` subsections** — inside the 141-line ceiling, so the whole
chapter is one section read and Chapter 26 closes here. `section_span(MAIN,'26')` returns
`(7117, 7203)`, agreeing with the hand scan.

**Census rows in range: zero.** DEFECT-CENSUS.tsv carries no `main` row between L7117 and L7202;
the nearest are L7266 onward, inside Chapter 27. CENSUS-CLOSURES-ch15b.tsv is therefore a header
only — MEASURED, not assumed.

Instruments: `r2-ch15b` (computable, twice rewritten, five faults self-caught) and `r2-ch15c`
(prose, once rewritten, five faults self-caught). Goldens `r2-ch15b.out` (9,045 B · a438e85b ·
125 lines) and `r2-ch15c.out` (11,439 B · bdfc010d · 156 lines).

---

## A. Deviations

**15b-01 — a spliced sentence in a reader-facing volume, and the splice's source located.**
L7156 prints:

> `      measuring C₆ to 1% fixes ν to about 0.0the searched bound of §29.8 — from 1/p_eff at n =`

The number breaks mid-digit and a foreign clause runs on without a space. **Prints & Proofs was
read before this was characterised** (Ruling 56): `The Method 1.6.md`, 738,550 B, md5
`49900cf41f818ab789bb90fc596ac977` — the same witness chat 95 used for §14.5 — carries the
identical line at **P7082**. **Authoring defect, not production loss.** The mechanism is measured,
not inferred: the string *the searched bound of §29.8* is a verbatim table cell of §29.8 itself,
at **main L8089**, inside the *claims / assessed / basis* table under `### 29.8 The other claims`.
A cell of one table has been spliced into a sentence 900 lines earlier. The lost figure is
recoverable and is not in doubt: 1/p_eff(100) = 0.087416, so the sentence read **about 0.09 %**
(0.087 % at three places). The dependent clause *roughly nine times sharper than the three-level
bracket achieves* then prices the three-level bracket at ≈ 0.787 %, a figure printed nowhere.
**Repair needs both halves: restore the figure and cut the spliced cell.**

**15b-02 — the class is bounded to one site, measured.** Sweeping all six volumes for the splice
shape (a decimal running straight into a lowercase word), with image paths, URLs and file names
excluded: **main 1 (L7156 itself), reg 4 (all URLs or archive filenames — `mass_1.mas20.txt`,
`restore-point-2_13.tar.gz`), mc 0, pc 0, ioi 0, sc 0.** The defect is isolated, not a class.
Recorded so R3 does not open a sweep that is already closed.

**15b-03 — the Aitken table is computed at a Rydberg constant the book does not use.** Under the
window (n−1, n, n+1) — the only one of four that reproduces anything — the Aitken column is
**4 of 4 exact at R = 109737.30** and **3 of 4 at the book's own R = 109737.31568**, where
T(10) prints **1097.3730** against a computed **1097.3732** under both HALF_EVEN and HALF_UP.
The T column tells the same story: at R = 109737.30 all four rows reproduce (T(20) requiring
HALF_UP, 274.343250 → 274.3433); at the book's R, T(10) fails. `gate.py run --core` holds
R = 109737.31568 as the constant, and chat 103 reproduced nine printed energies from it.
**The table's constant is unstated and is not the book's.**

**15b-04 — the T/3 column truncates where the rest of the table rounds.** T(20)/3 = 91.44775,
which is **91.4478** under HALF_EVEN and under HALF_UP alike; the table prints **91.4477**.
The other three rows do not discriminate (365.7910 and 5.7155 are exact; 22.8619 is the same
truncated or rounded). One row, one place, and it is the truncation-printed-as-equality class
(docket 12).

**15b-05 — σ₁ = 9.49 × 10¹ is unreproducible and single-witness.** L7143 states the centred
log-matrix's singular values as 9.49 × 10¹ then 1.8 × 10⁻¹⁴. **120 bases swept** — five exponent
sets × six ν grids × two centrings × two log bases — and **none returns 9.49 × 10¹**; the nearest
is 91.59 (p = 2..16, ν = 1..40, row-centred, log₁₀), and the sweep spans 11.98 to 505.1. Inverted:
row-centred, σ₁ = ‖p‖·‖v‖, so the fifteen exponents would need ‖p‖ = 17.40 on ν = 1..40 or 33.64
on ν = 10..49, against ‖p‖ = 35.21 for p = 1..15. **Neither the fifteen quantities nor the forty
ν values is printed anywhere** — the table names eight observables, not fifteen. `9.49` has
**one site in six volumes**, L7143 (dockets 10 and 17).

**15b-06 — σ₂ = 1.8 × 10⁻¹⁴ carries no information, and the book elsewhere says so.** log q_i =
p_i log ν + const, so row-centring leaves the outer product p ⊗ v exactly: rank is 1 and σ₂ is a
double-precision zero **for any exponent set and any grid**. Measured across the same 120 bases,
true SVD σ₂ ran 9.17 × 10⁻¹⁵ to 1.31 × 10⁻¹³ — the printed value sits inside that band and
constrains nothing. **Main L297 already states this**: *rank(log q) = 1 over fifteen Rydberg
observables — and that is a tautology once §26.1's [rule is granted]*. §26.2 presents the same
result as a measurement (*One dimension. Fifteen perspectives.*), and mc **L2078** repeats σ₂ as
a compendium finding. R3 must decide what §26.2 may claim, exactly as 14z-01 requires for §25.6.

**15b-07 — the §23.11 pointer fails, and its real target is located.** L7185: *(ΔT)²/Δ²T → T′²/T″
= (2/3)T — **exactly λ² of §23.11***. §23.11 is `The refusal pattern carries four verdicts, not
one` (L6519–L6548) and carries **zero λ characters, zero "λ²", zero "2/3", zero *Newton***.
CLAIM-LOCATOR: λ² lives at **§23.8.1 L6339–L6345**, `The quantity is the Newton decrement`, where
L6345 prints `λ² = (2Z²R/ν³)²/(6Z²R/ν⁴) = (2/3)·Z²R/ν² = (2/3)·T` — the identity L7185 cites,
verbatim. Also §23.8.4 L6381 and **App D.4.1 L10368**, `λ² = (2/3)T, proved and exhaustively
verified`. **Pointer-off-by-one class, seventeenth member; target §23.8.1 or App D.4.1.**

**15b-08 — the Mathematical Compendium sends the Aitken result to the wrong chapter.**
mc **L1932**: `Proved — M §24.6; Aitken 1926.` §24.6 is `The isoelectronic pairs` (L6710–L6724)
and carries **Aitken = 0, limit = 0, bias = 0, geometric = 0**. §26.6 carries **Aitken = 7,
limit = 4, bias = 2, geometric = 1**. A cross-volume pointer failure with a located target and a
transposed digit. **Eighteenth member of docket 9**, and the second time §24.6 has absorbed a
pointer meant elsewhere — chat 103's 14z-07 was the first.

**15b-09 — the chapter's only empirical test is priced on a species the collection does not
hold.** §26.5 tests against Singer et al. (2005) for **Rb ns–ns** and returns median 1.05 %,
maximum 1.83 %, *Bracket 66 of 66*. **Rb has zero rows in the Spectra Compendium** (rows matching
`^| Rb`: 0) and the token *Rb* appears **0 times in sc, mc, pc and ioi**; *rubidium* appears
0 times outside the Register. Docket 20 after Sr, C IV and the sulphur-like sequence.

**15b-10 — "Bracket 66 of 66" has no population of 66, and the only 66-population in the six
volumes is withdrawn.** §26.5 states nine points twice (L7168, L7170); C(9,2) = 36 and 9 × 9 = 81.
No population of 66 is printed in L7117–L7202. The phrase *66 of 66* occurs at reg **L4617**,
mc **L3370**, pc **L591** and pc **L653** — all of them the **triplet-above-singlet pair** count,
a different quantity, and pc L653 records it *Withdrawn at register 1168*.

**15b-11 — the cost law is never stated.** *cost law* / *cost-law* has **two sites in six
volumes**: L7170 itself and L10278 (*the C₆ cost-law check against Singer et al.*). Neither
defines it. Fitted as a power law A·nᵖ to Singer's own C₆ over the nine points, the residuals are
median 4.415 % / max 9.017 % with p free (fitted exponent 11.9934) and median 23.702 % / max
98.589 % at p fixed to 11 — **neither reproduces the printed 1.05 % / 1.83 %**, so the claim
consumes a law and an input set the section does not print. Both figures are single-witness.

**15b-12 — Ruling 45.** L7201: *A domain restriction found by testing, and stated rather than
discovered by a reader.* Addresses the reader and describes the authoring choice, in the manner of
chat 103's L6999 (*so a referee does not have to ask*). **Nineteenth member of the Ruling 45
class.** L7189–L7190 (*which is what this book's method is for*) is adjacent and weaker — recorded
as an incidental, not a member.

---

## B. Verified — reproduced exactly, so R3 does not re-derive

1. **The assembly rule.** p = 2a + 3b on all five table rows: ⟨r⟩ 2; cross-section/C₃/quadrupole/
   diamagnetic 4; polarisability α 7; C₆ 11; C₈ 15. All exact.
2. **L7150.** (ν²)⁴/ν⁻³ = ν¹¹ — exact.
3. **L7154.** A fractional error ε at exponent k gives kε to first order; exact expansion
   (1+ε)ᵏ−1 at ε = 0.01 gives 0.020100 / 0.115668 / 0.160969 for k = 2 / 11 / 15.
4. **Singer et al. (2005), both printed values exact.** At the published Rb ns–ns coefficients
   c₀ = 11.97, c₁ = −0.8486, c₂ = 3.385 × 10⁻³, p_eff = 11 + n(c₁+2c₂n)/(c₀+c₁n+c₂n²) gives
   **12.58 at n = 35 and 11.44 at n = 100**, under both rounding conventions. Nine evenly spaced
   points across 35–100: 12.576, 12.310, 12.136, 12.001, 11.884, 11.775, 11.667, 11.556, 11.440 —
   **monotone falling**, as the text says. The coefficients themselves are printed nowhere
   (docket 10), but the figures they produce are exact.
5. **L7185's identity.** T′²/T″ = (2/3)T on T = R/ν², exact at ν = 10, 20, 40, 80 (731.582105,
   182.895526, 45.723882, 11.430970). Residue T − (2/3)T = T/3 exactly.
6. **The Aitken column's convergence.** (printed Aitken)/(printed T) = 0.332776, 0.333194,
   0.333299, 0.333322 at n = 10, 20, 40, 80; the deficit from ⅓ falls as ~1/n² (5.57 × 10⁻⁴,
   1.39 × 10⁻⁴, 3.40 × 10⁻⁵, 1.17 × 10⁻⁵). The column converges to T/3 **from below**, so L7183
   is exact as a limit and approximate at every tabulated n — which is what L7185 states.
7. **L7187's two cm⁻¹ figures.** T/3 to the unit gives **91** at n = 20 and **23** at n = 40; the
   Aitken column gives the same. Both exact.
8. **Attribution is clean — not a 14x-08 collision.** Singer is fully cited: main **L11589**
   (*Singer, K., Stanojevic, J., Weidemüller, M. & Côté, R.* (2005), *J. Phys. B* **38**, S295),
   with citation chains at main L10188 and sc L988. Aitken likewise: main **L11634**
   (*Aitken, A. C.* (1926), *Proc. R. Soc. Edinburgh* **46**, 289), mc L1926 *Aitken Δ² / Seki
   Kōwa* and mc L1934's prior-art blockquote.
9. **Figure 26.1's renumbering is clean.** Prints & Proofs captions this figure *Figure 19.1*
   (P-line equivalent of L7138); BUILD90 carries `![Figure 26.1](figures/figure-26.1.png)` at
   L7136 and the caption at L7138. **Figure 19.1 still exists and is a different, legitimate
   figure** — main L5414/L5416, *Retrieval redundancy for five target cells*. No stale citation.
   The chapter is otherwise **byte-identical to the Prints & Proofs original** apart from the
   inserted image line and the caption's number.
10. **Docket 19 gains no member.** The chapter's three universals — L7139 *Every one of them is
    the same dimension*, L7147 *Every Rydberg property is ν to a power*, L7195 *a closed-form fit
    at every n* — are claims about the algebra log q = p log ν, not about the collection, so none
    is measurable against the channel table. A negative with its witness (the rank-1 identity).
11. **14q-06 stays at three.** None of the seven headings finishes in the body; §26.7's heading
    opens with *And* but its body begins a new sentence.
12. **Ruling 46 is clean.** *build*, *script*, *md5*, *instrument* all 0 in L7117–L7202.

---

## C. Incidentals

1. **§29.8's table cell cites its own section.** L8089's row reads *bracketing rather than
   predicting | the searched bound of §29.8 | literature uniformly predictive* — a self-pointer.
   Noted for docket 9's sweep, not counted as a member.
2. **The three-level bracket is defined, its precision is not.** *three-level* resolves: L6242
   defines V from three levels at n−h, n, n+h. Only the figure the *nine times sharper* clause
   needs is absent.
3. **mc L2078 repeats σ₂ but not σ₁** — the compendium carries *rank(log q) = 1 across fifteen
   Rydberg observables; second singular value 1.8 × 10⁻¹⁴*. If R3 restates §26.2, mc L2078 moves
   with it.
4. **L7189–L7190** — *A stated, exact bias in a standard one — which is what this book's method is
   for.* Self-referential about the method rather than the build; adjacent to Ruling 45, not a
   member.
5. **L7134's scope statement is exemplary** and should survive any repair: the rule's exclusion of
   hyperfine coupling is stated with its reason (ν⁻³ through |ψ(0)|², neither a matrix element nor
   a denominator).
6. **Five instrument faults in r2-ch15b and five in r2-ch15c, all self-caught and rewritten, none
   trimmed.** The four worth carrying are in W-143.
