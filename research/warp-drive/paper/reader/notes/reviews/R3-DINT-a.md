# R3-DINT-a: confirming reading of the six nits of R2-DINT-a as applied (chapters 00, 01, 90)

Reader: R3-DINT-a (independent; changed nothing in the repository). The nits were applied in 1c871797; the tree was
read at HEAD 4c754c94, where 00, 01 and 90 are as in 1c871797 (after it, f8a5e9ff changed only 03 and 71 among the
chapters, 4c754c94 only STATUS). Read: R2-DINT-a ("New findings", "Checked and found to hold"); the diff of 1c871797
for 00, 01, 90, as a line diff and as a word diff; 00 in full, 01:140–196, 90 in full; 71 at the opening (1–31),
lem:fwd-orders and the paragraph before it (402–420), prop:fwd-calculus (898–917), the orders paragraph of
cor:fwd-near-b0 (1196–1226), thm:loss-d (1426–1482), prop:ec-delta-cap, cor:uc-two-offsets (2061–2077), prop:uc-ltf,
def:uc-choice (2276–2289), thm:uc-integer and its proof (2452–2493), def:cs-choices (3832–3851),
rem:ec-not-evaluated, rem:ec-point-outside; 84 at sec:layer-regions and prop:layer-regions with its proof
(1185–1250); 85 at thm:l-24, prop:edge-dips, rem:edge-criterion; 70 at the radial problem (31–42), thm:band,
rem:band-observed, prop:morawetz-master-potentials; 61 at cor:after-shell-every-rate (251–262) and
thm:after-shell-reach (666–688); 95 and 96 (openings); 23 at lem:ii-a-8-5 and prop:ii-a1-2-4 (statements); 25:20–40;
03 at thm:settling and the list item at 351–357; 33 at rem:s14-eps-ind-scope; 62 at rem:half-class-changes; 63:189–194;
lint.py (the forbidden list).

## Verdict

**CONFIRMED — 0 Major, 0 minor, 3 nits** (F1–F3 below; wording only, none affects the truth of a statement). All six
nits N1–N6 are resolved, every sentence of the changed text is true where it stands, and every replaced range is the
intended one.

## The six nits

| Nit | Status | Why |
|---|---|---|
| N1 (00:33–34, 01:154, 90:69) | Resolved | The applied text is the review's block verbatim at 00:33–37, 01:153–157 and 90:62–75 (the N2 block, which carries N1's change at 90:69). thm:uc-integer (71:2452–2455) is stated "with the index sets as constructed, the admissible choice of the weights of def:uc-choice and the free orders and inner products of def:cs-choices", and gives d_NM = d_R ≤ D_NM, an integer below 1.57157·10⁵⁰, and N_NM ≤ 21D_NM + 6, an integer below 3.30029·10⁵¹: so 90:69–70 ("for those index sets and at one admissible choice of the weights and of the free orders and inner products, d is at most an integer below …") is exact, and 01:154 is true as the existence statement it is. The abstract's two-sided bound holds at that one choice: the lower bound is eq:uc-lower (71:2470), cor:uc-two-offsets (a) at every admissible choice of the weights, its hypothesis holding for the constructed ℰ_ind by (b), and it does not depend on the free orders and inner products, since thm:loss-d (ii) uses only ℓ_tf ≥ 1, which holds at every choice (prop:uc-ltf, last line of "The losses"); at def:uc-choice itself 3R > 1.2498·10²⁴ (71:2472). def:uc-choice takes ℰ_ind and ℰ^ι_ind as constructed and ℰ^C_I, ℰ_++ least, which is what thm:uc-integer calls "the index sets as constructed"; def:cs-choices is headed "The free orders and inner products", which the "orders and inner products" of 00 and 01 abbreviate. The same old wording at 03:354 was changed to "weights, orders and inner products" by f8a5e9ff. |
| N2 (90:71–75) | Resolved | 71:28–31 (at HEAD): "No result of this chapter is used in the proof of any theorem of this paper outside it. … the indices of prop:ii-a1-2-4 and lem:ii-a-8-5, which prop:fwd-calculus proves, and the value N′ = 13 of ch:s06, which rests on lem:fwd-orders; these values are used only in this chapter." 90:72–75 now says the same. Checked independently: of the 203 labels of 71, the only references from other chapters are 01:150, 154, 187 (introduction), 03:353–357 (the list of what the remaining chapters prove), 23:1072 and 23:1470 (the explicit-index clauses in the statements of lem:ii-a-8-5 and prop:ii-a1-2-4), 25:30 (notation), 33:3236 (rem:s14-eps-ind-scope), 62:577 (rem:half-class-changes, naming the loss d; that remark is cited only at 63:194, not in a proof) and 90; none is in a proof. The values 200Θ + 100 and 200Θ + 98 occur only at 23:1071, 23:1467 and in 71; N′ = 13 only at 25:29 and 71:30, 410, 1207, 1225. lem:fwd-orders (71:415–420) gives inf 𝗌_0 = −13, whence N′ = 13 at 25:29–30; prop:fwd-calculus (71:898–915) gives M + 2 = 200T + 100 for prop:ii-a1-2-4 and d_0 = 200T + 100 for lem:ii-a-8-5 (a), (b). The clause on N′ = 13 is right. One wording point: F1. |
| N3 (90:36–44) | Resolved | Checked against prop:layer-regions (84:1193–1206). Its hypotheses are δ ∈ (0, 1/2] and P > 4, as 90:36 now says, with λ ≤ λ_U(δ, P) (F2). (i): E(v) ≥ λ^(3−δ) gives spacelike at (v, x̂), "whether or not env vanishes at v" — "above the band" is right, and since E ≥ \|env\| it is right whichever of the two the level is read in. (ii): a first-reach point v with λ^P ≤ \|env(v)\| ≤ λ^(3+δ) gives, on [v, v + 4πλ] at x̂, points where the boundary is timelike and points where it is spacelike — "points of both characters on every window of length 4πλ that starts where \|env\| first reaches a level between λ^P and λ^(3+δ)" is exactly this: the first point at which the continuous \|env\| reaches a level y is a first-reach point in the sense of 84:1187 (before it \|env\| < y on a compact range, so E < y), and conversely. (iii): the band λ^(3+δ) ≤ E ≤ λ^(3−δ) is decided where R ≥ 1 + 2λ^γ or R ≤ 1 − 2λ^γ, γ = 1/10, R the first-degree amplitude over the margin; rem:edge-criterion (85:2034–2043) says "the ratio \|S\|/m0 decides up to the factor 1 ± 2λ^γ in the band", S the amplitude of (iii). The pointwise "decides the character … on the windows" is gone. δ, now defined, also serves the following sentences (thm:l-24 and prop:edge-dips take δ ∈ (0, 1/2]). |
| N4 (90:88) | Resolved | rem:band-observed (70:1457–1467) concerns R_l(σ) = (H_l − σ²)⁻¹ with V_l of eq:rb-potential, the radial form of the scalar wave operator (70:33–41), for every l ≥ 0; its values from \|σ\| = 12 on are below the constant 11.477 of thm:band and, with their decay, "not proved here". "For the scalar wave operator" restores the antecedent. |
| N5 (90:106–110) | Resolved | thm:after-shell-reach (61:666–688): (i) a > ℓ0 and Ξ < δ/(C_1(1 + (a − ℓ0)^(−1/2))) is reached directly, and "over the admissible ℓ0 …, this covers every a > 3 (cor:after-shell-every-rate)"; (ii) for 3/2 < a ≤ ℓ0 the rate does not decide; its closing paragraph gives "applies up to the gluing" false for fixed Ξ and large R at every a ∈ (3/2, ℓ0], and "exactly those small in Hintz's class". cor:after-shell-every-rate (61:251–254) runs thm:settling with ℓ0 ∈ (3, min(a, 4)). The overlap on 3 < a ≤ ℓ0 is gone. ℓ0 itself is not introduced in 90 (F3). |
| N6 (01:194–196) | Resolved, as reworded | 95:3–12: "Each published result is cited by its source, with its number and its page where given", [DLMF] by equation number; the reworded "each cited with its number and page where the cited work gives them" says this ("cited" carries the source), and "each" ranges over the results of the literature, not over the five consequences proved there. 96:3–4 is quoted verbatim for app:tables. The deviation was needed: lint.py:45 forbids "source" followed by a space, case-insensitively. |

## Joins

Line diff and word diff of 1c871797 against its parent: in 00, 01 and 90 every word outside the six replacements is
unchanged and in order, none is doubled and none lost; the rewraps run from the first changed line to the paragraph's
end. Read three lines either side of each hunk: 00:29–37 (the paragraph ends the file, with its newline), 01:148–160
and 01:190–196 (end of file), 90:30–48, 90:61–79, 90:81–95 and 90:101–113 — each hunk starts where the previous line's
sentence continues and ends at a paragraph end. The text applied is the R2-DINT-a block verbatim for N1–N5 (each block
occurs exactly in its file; the two "replace" blocks of N1 no longer occur); N6 is the reworded text reported.

## New findings

Each replacement block is to be pasted without its 4-space indent. Every line of every block has been measured with
Python len (≤ 121), none starts with "+ ", "- ", "* ", "> ", "#", "=" or "|", and no block adds a label.

**F1 (nit) — 90:74–75: "are used only in that chapter" follows "the value N′ = 13 of [[ch:s06]]".** The nearest chapter
before "that chapter" is now ch:s06, which N2 inserted; read so, the clause would say the values are used only in
chapter 25, which is false (they are used in 71, 71:407–410, 1207, 1225). The trailing citation of
ch:explicit-constants points the right way, but it is the place of the statement, not an antecedent.
Fix. Replace 90:72–75

    [[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the proof of any
    theorem outside that chapter; the explicit indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which
    [[prop:fwd-calculus]] proves, and the value N′ = 13 of [[ch:s06]], which rests on [[lem:fwd-orders]], are used only in
    that chapter ([[ch:explicit-constants]]).

by

    [[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the proof of any
    theorem outside that chapter; the explicit indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which
    [[prop:fwd-calculus]] proves, and the value N′ = 13 of [[ch:s06]], which rests on [[lem:fwd-orders]], are used only in
    [[ch:explicit-constants]], whose opening states both.

**F2 (nit) — 90:36: the threshold of prop:layer-regions is not stated.** prop:layer-regions holds for λ ≤ λ_U, λ_U
depending on δ and P (84:1195); the sentence fixes δ and P and says nothing of λ, whereas the same paragraph says "once
λ is small" (90:31) and "for every small λ" (90:44). With δ and P quantified first, "λ small" carries the dependence.
Fix. Replace 90:36–44 ("([[cor:layer]]). Inside the layer, … [[rem:edge-criterion]] decides nothing.") by

    ([[cor:layer]]). Inside the layer, for δ ∈ (0, 1/2], P > 4 and λ small, the boundary is spacelike above the band between
    the levels λ^(3+δ) and λ^(3−δ), and it has points of both characters on every window of length 4πλ that starts
    where |env| first reaches a level between λ^P and λ^(3+δ) ([[prop:layer-regions]]); on the band its character is decided
    up to a factor 1 ± 2λ^(1/10) in the ratio of the first-degree amplitude to the margin ([[rem:edge-criterion]]). For an
    envelope increasing at its edge with the hypothesis (H_N) of [[def:edge-hypotheses]] the band is decided by one switch
    per column ([[thm:l-24]]), and the very edge for envelopes with the edge hypotheses, which hold for env_C
    ([[thm:very-edge]], [[cor:edge-envelope]]). Some regularity of the edge is needed: for an explicit smooth envelope whose
    intervals of zeros accumulate at the edge, the boundary is spacelike throughout intervals of length 4πλ below the level
    λ^(3+δ), for every small λ ([[prop:edge-dips]]), and at a dip of a general envelope the criterion of
    [[rem:edge-criterion]] decides nothing.

(Only "and P > 4," becomes ", P > 4 and λ small,"; the rest is 90:36–44 rewrapped, "|env|" kept off the start of a
line.)

**F3 (nit) — 90:107–108: ℓ0 is used three times and not introduced in 90.** ℓ0 ∈ (3, 4) is fixed in thm:settling as
the order of the conormal remainder r^(−ℓ0) H_b^∞ of the metric in Hintz's class (03:278, 03:299–300); 90 uses it only
here, and since N5 the sentence turns on it ("a > ℓ0", "over the admissible ℓ0", "3/2 < a ≤ ℓ0").
Fix. Replace 90:106–110 by

    perturbations that (ii) reaches, directly or through gluing uniformly in the gluing radius, are exactly those small in
    Hintz's class: a perturbation of order of decay a > ℓ0, ℓ0 ∈ (3, 4) being the order of that class's conormal remainder in
    the metric ([[thm:settling]]), and of small enough size is reached directly, which over the admissible ℓ0 covers every
    a > 3 ([[cor:after-shell-every-rate]]), for 3/2 < a ≤ ℓ0 the rate does not decide, and the statement that (ii) applies up
    to the gluing is false for fixed size and large radius at every such a ([[thm:after-shell-reach]]).

## Contract

- **Checks** (from the paper directory, at HEAD 4c754c94). `python3 lint.py --chapters`, last line: "chapters: 62
  file(s), 4570 label(s) defined, 0 hit(s)". `python3 assemble.py --check`, last line: "labels 4570, computations cited
  0, problems 0". Both also passed, with the same last lines, at 1c871797.
- **Line lengths.** Every line of 00, 01 and 90 is at most 121 characters (Python len); so is every line of every
  chapter. In and around the hunks the longest lines are 121 (00:32, 90:44, 90:66, 90:72, 90:87).
- **Line starts.** The only lines of 00, 01 and 90 that start with a forbidden prefix are headings, the list items of
  01:97–118 and the block quote of 01:24–36, as before; no changed line does.
- **Language.** The added lines contain no file, program, code, computation or AI language (scanned for file, program,
  code, script, computer, computation, numerical, AI, agent and file suffixes; no hit).
- **References.** Every [[…]] in the changed text resolves (assemble: 0 problems) and was followed to its target:
  thm:uc-integer, cor:uc-two-offsets (unchanged citation), ch:explicit-constants, prop:ii-a1-2-4, lem:ii-a-8-5,
  prop:fwd-calculus, ch:s06, lem:fwd-orders, prop:layer-regions, rem:edge-criterion, rem:band-observed,
  cor:after-shell-every-rate, thm:after-shell-reach, app:standard-results, app:tables; each says what the text claims
  (table above).

During the reading the working-tree PAPER.md was rewritten and then untracked by the coordinator's commit f8a5e9ff;
neither command above writes it (assemble.py writes PAPER.md only without --check), and this reader touched no
repository file.
