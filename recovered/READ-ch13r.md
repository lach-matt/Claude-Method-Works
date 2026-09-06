# READ-ch13r.md — main volume, Chapter 17 whole (L4789–L4921), chat 86

Phase R2, chat-81 cadence: heading scan, whole-section read, claim census in two kinds, two
instrument batches (`r2-ch13r` computable, `r2-ch13s` prose), both banked. No repairs, no
Register entries — the chat-67 hold stands. Findings are for R3.

## Boundary, MEASURED (heading scan, this chat)

HANDOFF-38 gave Chapter 18 at **L4899, INFERRED**. That is wrong. MEASURED:

    L4789  ## 17. Extension — cells, axes, constraints
    L4794  ### 17.1 E1 — which cells may be added
    L4799  ### 17.2 E2 — which axes may be adjoined
    L4814  ### 17.3 E3 — which constraints may be imposed
    L4873  ### 17.4 A worked extension, and what it costs
    L4914  ### 17.5 E is derived            <-- not listed in HANDOFF-38
    L4922  ## 18. What the law forbids

Chapter 17 is **L4789–L4921, 133 lines, five sections**. This is the third handoff in a row to
misplace a chapter boundary (HANDOFF-34's L4157, HANDOFF-36's L4477, HANDOFF-38's L4899). The
scan stays mandatory.

## Claim census

**Computable (21).** K1 L4795 the E1 criterion · K2 L4797 "100 % over 288 tests" · K3 L4800 the
E2 criterion · K4 L4802 "100 % over 424 tests" · K5 L4802 the classification line (projections,
maxima, minima, constants qualify; sums, products, differences do not) · K6 L4809 "seven
functions … none repairs" · K7 L4819–4820 the interval property · K8 L4824 "zero violations on
all 1,367,031 pairs of Λ₉" for δ = f − ℓ and σ = 2S′ − 2S · K9 L4827 the convexity criterion ·
K10 L4831 "8.2 %, 10.3 % and 0.8 %" on §14.5's three ambients · K11 L4841 Janet 4 of 4, E = 0 ·
K12 L4846 "36 of 36 at two cap settings" · K13 L4860 the { h ≤ q } criterion · K14 L4862 "100 %
over 2,513 tests, nine functions" · K15 L4864 "a + b ≤ 3 can be closed where a + b ≤ 4 is not" ·
K16 L4866 "meet never breaks it" · K17 L4871 "seven constraints … none sums" · K18 L4879 "86 %
coverage ceiling" · K19 L4882–4883 the canonicalisation, zero failures · K20 L4887 "89,864 join
failures in 979,300 sampled pairs" · K21 L4891/L4901/L4906 45,690 cells; 1,040 cells and 540,280
pairs; "fifteen of forty ordered pairs are new".

**Prose (21).** P1 L4792 "three operations" against L4812 "three repair routes" · P2 L4806
Theorem 17.1's three other sites · P3 L4812 the calendar of Chapter 6 · P4 L4815 "three wrong
statements … recorded in Chapter 28" · P5 L4815's colon and its missing criterion · P6 L4831
"the three ambients of §14.5" · P7 L4834 §4.6 · P8 L4844 Register 449 and L4858 Register 440 ·
P9 L4849 §18.2 refuses ν = e − δ · P10 L4854 §12.11.2's second excluded form · P11 L4857
seniority parity at axis 10, the conjugation ceiling at axis 12 · P12 L4886/L4899 "of §16.4
form" · P13 L4894 "which §7.1 excludes" · P14 L4912 P16 · P15 L4920 Chapter 23 carries none
beyond ν · P16 L4916–4918 the S3/D3/S2 table · P17 attribution in 133 lines · P18 the restated
figures 288 / 424 / 2,513 / 86 % / 89,864 / 979,300 / 45,690 / 1,040 · P19 §11.7's self-citation
for the 89,864 · P20 inbound descriptions of Chapter 17 · P21 §17.5 in the contents list.

---

## A — deviations

**13r-01 (K20, K21). §17.4's `979,300 sampled pairs` cannot be true of the lattice §17.4 builds,
on either reading of "sampled".** L4887: *"89,864 join failures in 979,300 sampled pairs, meets
unaffected."* L4901: *"Tested exhaustively: 1,040 cells, all 540,280 pairs, zero join and zero
meet failures."* L4904: *"The map (g₁, g₂) ↦ (g₁, g₁+g₂) is a **bijection** onto an admissible
lattice."* MEASURED: the volume's all-pairs convention is C(N, 2), exact at three independent
sites — 1,367,031 = C(1654, 2) (L4824, labelled *all*), 540,280 = C(1040, 2) (L4901, labelled
*all*), 979,300 = C(1400, 2). Under that convention L4887's lattice has **1,400 cells** and
L4901's has **1,040**, while L4904's bijection forces them equal. Read instead as a true sample,
979,300 pairs cannot be drawn from a 1,040-cell lattice at all: its entire pair set is 540,280.
The 13j-01 / 13p-01 class inverted — not a sample printed as a population but a population-shaped
figure printed as a sample, and inconsistent with its own section either way. Carried in DEFERRED
since chat 74; now measured, and it closes as a **defect**.

**13r-02 (K21). §17.4's cell counts do not rebuild under any reading of the construction it
prints.** L4891 *"45,690 cells"*, L4901 *"1,040 cells"*, L4887's implied *1,400*. The
construction as printed is: Λ₈'s source coordinates; two target triples (e₁,f₁,g₁), (e₂,f₂,g₂),
each under Λ₈'s own target constraints; the canonicalisation e₁ ≤ e₂ (L4882); conservation
g₁ + g₂ ≤ q (L4886). MEASURED over **1,728 monotone readings** (n_max 1–4, ℓ_max 1–2, k_max 2–4,
e_max 2–4, f_max 1–3, g capped by q or not, canonicalisation on/off, 2S carried or not):
**no reading returns 45,690**, and the twelve that return 1,040 or 1,400 are degenerate (n_max = 1
with 2S dropped and no canonicalisation). At Λ₈'s own caps (3, 1, 3, 3, 1) the construction gives
**7,908** cells without conservation and **5,790** with it. Neither figure has a second site
anywhere in the six volumes (45,690 and 1,040 are each printed exactly once). The 13p-13 class:
recorded, not identified — R3 needs the construction stated before the counts can be disposed of.

**13r-03 (K5). §17.2's classification line is false of two of its four qualifying classes, and
the printed text names no witness.** L4802: *"Projections, maxima, minima and constants qualify;
sums, products and differences do not."* MEASURED on Λ₈ over every coordinate pair, exhaustively
(the (i, j) part of a join is (max, max) and of a meet is (min, min), so the realised value pairs
are the whole quantification): projections **8 of 8** qualify, constants **3 of 3**, sums **0 of
28**, products **0 of 28**, differences **0 of 56** — and **maxima 10 of 28, minima 10 of 28**.
The eighteen that fail include max(n,k), max(n,q), max(ℓ,q), max(k,e), max(q,f) and their minima.
In a general product of chains maxima and minima are **never** lattice homomorphisms — witness on
a 2 × 2 box, a = (1,0), b = (0,1): max gives h(a∧b) = 0 against min(h a, h b) = 1. This confirms
and sharpens the chat-67 Sweep C record carried in memory ("true of one class and false of
another, the printed text silent on which"): it is **two** classes, not one, and the qualifying
pairs are exactly those in which one coordinate bounds the other along Λ₈'s constraint tree.
**Defect.**

**13r-04 (P5). §17.3 promises its criterion with a colon and does not print one.** L4815 ends
*"The criterion is:"*; the next non-blank line, L4817, is *"**And for a constraint on a DIFFERENCE
the criterion is convexity, which is proved here.**"* — a supplementary remark opening on *And*,
not the criterion. The E3 criterion is printed at **L4860**, forty-five lines and four
sub-arguments later. A colon with no referent at the head of the section it governs. **Defect.**

**13r-05 (P13). §17.1's ban on sum bounds is attributed to §7.1, which does not state it.**
L4894: *"Conservation is a bound on a sum, which §7.1 excludes."* MEASURED: §7.1 runs
**L1750–L1763**; it is the constraint table (*"The constraints, and where each comes from"*), and
its only occurrences of *exclu* are the two **Pauli exclusion** provenance cells at L1755 and
L1758. §7.1 contains no statement about sums and no exclusion of any constraint form. The
13d-01 / 13l-03 / 13o-01 / 13p-06 class: a section attributing a rule to a neighbour that does not
carry it. The rule itself is sound and is stated at L4868 in §17.3's own body.

**13r-06 (P10). §12.11.2 says Chapter 17 excluded two constraint forms; Chapter 17 excludes
three.** Main **L3364**: *"Chapter 17 excluded two constraint forms — sums and differences. The
tower requires a third."* MEASURED against §17.2 L4802 (*sums, products and differences do not*)
and §17.3 **L4868** (*"Sums and products fail because a join raises every coordinate at once"*).
Products are excluded in Chapter 17 at both sites and are absent from §12.11.2's count, which then
calls the congruence *"a third"*. L4854's own pointer — *"§12.11.2's second excluded form"* — is
sound under §12.11.2's numbering (the second of sums and differences is differences, and
convexity is the difference criterion), so the defect is in the count at L3364, not the pointer.

**13r-07 (P11). The conjugation ceiling is placed at axis 12 in §17.3 and at seniority in Chapter
12.** L4857: *"Seniority parity at axis 10, the conjugation ceiling at axis 12, and the
electromagnetic parity rule are three instances of one criterion."* MEASURED: *conjugation
ceiling* occurs at exactly three sites — main **L3368** (*"min(g, 4f+2−g) for spin; the
conjugation ceiling for seniority"*), **L3382** (*"seniority needs the conjugation ceiling"*) and
L4857. The first two attach it to **seniority**, which this volume places at **axis 10** (L2566,
L3080, L3149), the same axis L4857 assigns to seniority *parity*. L4857 therefore either names
two distinct mechanisms on one axis and mislabels the second's index, or duplicates one mechanism
across two axes. R3 decides; the substance (three refusals are one criterion) is untouched.

**13r-08 (K2). §17.1's E1 is illustrated on an object where E1 admits nothing, and its test count
matches neither population.** L4797: *"**100 % over 288 tests.** A cell may be added exactly when
it sits in a hole whose joins and meets fall back into the lattice."* MEASURED exhaustively over
the ambient box (6,912 cells, 976 inside, **5,936 outside**): the number of cells x outside Λ₈ for
which Λ₈ ∪ {x} is closed is **zero**. Λ₈ admits no addition at all — there are no holes of the
kind the sentence describes. 288 is neither the population of the test (5,936) nor the count of
addable cells (0), and no second site prints it as this measurement. The 13j-01 / 13p-01 class: a
figure whose population is unstated and unrecoverable.

**13r-09 (K10). §17.3's three percentages reproduce exactly, but only under one of two readings
of "the convex preimages", and the section states neither.** L4829–4831: *"on the three ambients
of §14.5 the convex preimages are **8.2 %, 10.3 % and 0.8 %** of all closed subsets."* MEASURED
(§14.5's ambients 2×2×2, 3×3, 2×2×2×2; closed subsets **73 / 146 / 731**, reproducing §14.5's
table exactly with the empty set excluded): over **one** coordinate difference the convex
preimages that are closed number 6 / 15 / 6 = **8.2 % / 10.3 % / 0.8 %**, matching to the printed
decimal; over **all** coordinate differences they number 16 / 15 / 31 = 21.9 % / 10.3 % / 4.2 %.
The 3 × 3 ambient has only one difference up to sign, which is why it agrees under both and hid
the ambiguity. The figures are right; the defining term is unstated. The 13j-07 / 13l-06 /
13n-02 / 13p-11 class.

**13r-10 (P17). Chapter 17 attributes one name in 133 lines.** MEASURED: the only proper name in
L4789–L4921 is **Janet** (L4841), and it names a table rather than an authority. The chapter states
the sublattice criterion for a graph of a map, the interval-map property of a difference on a
product of chains, and the convexity criterion for preimages — all of which have prior art the
Mathematical Compendium cites elsewhere (Birkhoff 1937 at MC L1490; Freuder 1982, Rota 1964,
Lauritzen 1996 at MC L1498). The 13h-05 / 13h-06 / 13j-13 / 13l-04 / 13o-02 / C5-of-13p class,
for the references and attribution pass.

## B — verified

**B1 (K8).** The interval property holds with **zero violations on all 1,367,031 pairs of Λ₉**,
for δ = f − ℓ **and** for σ = 2S′ − 2S. |Λ₉| = 1,654 and C(1654, 2) = 1,367,031 exactly, so
"all" is literally true. Register 440's restatement of the same figure (reg L1637) agrees.

**B2 (K6).** L4809's *"Tested on seven functions including the identity and a constant; none
repairs"* — seven functions tried (identity, a constant, four projections, n + k) on a witness
verified **non-closed** before use (Λ₈ minus its top cell, 975 cells, closed = False): **none
repairs**. Theorem 17.1 itself is cleared at READ-ch13p B9 and was not re-derived.

**B3 (K16, K17).** L4866 *"meet never breaks it"* — zero meet failures over every coordinate pair
of Λ₈ and every threshold. L4871's *seven constraints* — exactly seven when g's bound is split as
the Index of Indices lists it (ℓ ≤ n−1, k ≤ 4ℓ+2, q ≤ k, 2S ≤ k, f ≤ e−1, g ≤ 4f+2, g ≤ q); every
right-hand side reads one coordinate, the two on g fold to the minimum of two, and none is a sum.

**B4 (K21).** L4906–4907's *"Fifteen of forty ordered pairs are new"* reproduces **exactly** at
q = 3: the ten cells with g₁ + g₂ ≤ 3 carry 25 ordered pairs under the componentwise order and 40
under (g₁, g₁+g₂), of which **15** are new. (At q = 2 it is 5 of 14, at q = 4 it is 35 of 90 — the
printed pair identifies its own cap.)

**B5 (K21).** L4889's counterexample verifies: a = (g₁=1, g₂=0, q=1) and b = (g₁=0, g₂=1, q=1)
each satisfy g₁+g₂ ≤ q, their join is (g₁=1, g₂=1) with g₁+g₂ = 2 > q = 1 — two transferred
having removed one.

**B6 (K15).** L4864's *"a + b ≤ 3 can be closed where a + b ≤ 4 is not"* is **true and
realisable**: of the 2,102 sublattices of the 4 × 4 box, **233** exhibit it; the smallest witness
is {(1,0), (1,3), (2,0), (2,3)}. It is realisable on **no full box** (on a box, {a+b ≤ t} is
closed only if a chain is shorter than t, which cannot hold at 3 and fail at 4) and on **none of
Λ₈'s 28 coordinate pairs** ({a+b ≤ 3} is closed for 6 of them, {a+b ≤ 4} for 13, and no pair is
closed at 3 and open at 4). The claim needs a sublattice to witness it and the chapter supplies
none.

**B7 (K9).** The sound direction of the convexity criterion holds on all three ambients: **every**
convex preimage is a closed subset, at 2×2×2, 3×3 and 2×2×2×2, over every coordinate difference.

**B8 (P16).** §17.5's table resolves exactly: **S3** is §15.2 *"S3 — the bounds"* (L4277), **D3**
is §16.5 *"D3 — totality catches a missing value"* (L4449), **S2** is §15.3 *"S2 — the order,
which is the hard one"* (L4293). All three descriptions in the table match their sections.

**B9 (P2, P8, P9, P14).** Theorem 17.1's three other sites all resolve to the claim and not the
heading (main L3587, L4534, L10558, the last giving its Appendix A tag A.6). Register 449 (reg
L1667–1669) states the closed-ambient scope condition §17.3 cites it for; Register 440 (reg
L1635–1637) states the interval-map/convexity pair §17.3 cites it for. §18.2 (L4970–4974) does
refuse ν = e − δ as an axis, for the reason L4849 gives. P16 resolves (L355, and L1503–1508 give
it as the one operation corroborated by a construction rather than a failure; L2721 already points
forward to §17.4 as its price).

**B10 (P3, P6).** L4812's *"calendar of Chapter 6"* is sound — *calendar* occurs ten times in
Chapter 6 (L1529–L1710), including the seven defect cells at L1677. L4831's *"three ambients of
§14.5"* is sound — §14.5's table (L3738–L3741) has exactly three rows.

## C — incidental

**C1.** L4834's *§4.6* is reported UNRESOLVED by r2-tools; Chapter 4's protocol rows carry no
`###` heading at that number. The handoff's standing note applies — a bare §4.6 is a protocol row,
not a defect — but it has now been reported UNRESOLVED at a second site and R3's pointer pass
should decide once whether protocol rows get headings.

**C2.** L4886 and L4899 are two more sites of *"of §16.4 form"*, whose target heading (L4407,
*"16.4 D2 — D_def catches a wrong derivation, but only under two"*) is about a defect class and
not about constraint form. MEASURED: eight sites of the phrase across the six volumes — main L261,
L653, L4525, **L4886**, **L4899**, L7740, L8803, L11417. This is 13o-01 exactly, not a new class;
chat 85 resolved L4525 to the claim at L1765 without re-deriving it, and the same resolution
serves both Chapter 17 sites.

**C3.** §11.7 cites itself by number for a figure printed in its own body: L2260–2261 read *"A sum
bound breaks the first — §11.7 measures 89,864 join failures when one is tried"*, and L2261 lies
inside §11.7 (L2251–L2274). Not wrong, but it reads as a forward reference to another section.

**C4.** 45,690 (L4891) and 1,040 (L4901) each occur exactly once in the six volumes; 979,300
occurs twice (L4887 and MC L1494, which also calls it *sampled*, at its scope line L1496 *"the
sum-bound figure sampled over composition pairs"*). 89,864 occurs three times (L2261, L4887, MC
L1494). So the only figure of §17.4's worked extension with independent corroboration is the one
the batch could not rebuild either.

**C5.** L4920's *"the cost surface of Chapter 23 carries none beyond ν"* was not resolved to a
claim: Chapter 23 (L6178–L6622) returns zero lines for *carries none*, *no independent*, *beyond
ν* and *reduces to ν*. The claim may be stated in other words; this is a pointer left open for
R3's pass, not a measured defect.

**C6.** L4879's *"86 % coverage ceiling"* prints no population and has one other site of the token
(L4368, an unrelated measurement). Not re-measurable here: the configuration catalogue it counts
against is not in r2lib. The same owing as §16.7.1's periodic-table and asteroid-belt catalogues,
recorded in DEFERRED at chat 85.

**C7.** L4797, L4802 and L4862 all print *100 %* with a bare test count (288, 424, 2,513) and no
population; none of the three counts reproduces as a population of Λ₈. K4 and K14 are therefore
recorded, not identified, alongside 13r-08 — the class sweep this chat ran over Λ₈ generates
14,366 (h, value-pair) tests, and no natural sub-count of it is 424.

**C8.** Census rows in range: 1104 (L4806 *never*) and 1105 (L4866 *never*), both C9. Both flag a
word inside a statement the batch verified — Theorem 17.1 (cleared at READ-ch13p B9) and the meet
argument (B3, zero failures over every pair and threshold). Regex artefacts, on the precedent of
rows 678, 680–687, 1067, 1069.

## Instruments

`r2-ch13r.py` (computable, ≈ 9 s), golden `r2-ch13r.out` 6,945 B · md5 71fef61e · 102 lines.
`r2-ch13s.py` (prose, ≈ 1 s), golden `r2-ch13s.out` 16,171 B · md5 5ce0795e · 198 lines.
Both deterministic; both fit any gate run list. `therm` / `untherm` are carried verbatim from
r2-ch13p with a provenance comment and remain owed to r2lib.

Three drafting faults in `r2-ch13r`, all self-caught before banking and all **rewritten, none
trimmed of coverage**: the first repair witness was a *closed* subset, which made the "none
repairs" test vacuous; the convex-preimage family swept every coordinate difference where the
book's figures use one, and included the empty set where §14.5's counts exclude it; and the
3-versus-4 test swept full boxes only, where the criterion quantifies over sublattices. The last
turned a null result into B6.
