# R2-P-40-sem: confirming reading of the application of R-P-40-sem (m1, m2, m3, n1)

The tree was read at HEAD a903f977. The application commit is 06988e45 ("Reader's edition: R-P-40-sem ..."). HEAD moved
by one snapshot commit, which touches only chapters 36, 38 and 45 and proofs/P-U71-small.md. `git diff 06988e45 HEAD`
is empty on chapters 40 and 41, so the lines read are those of the application. Line numbers are those of HEAD. The
parent commit is 4b07d38a. No repository file was edited.

## Verdict

**CONFIRMED**: Major 0, minor 0, nit 1.

All four items are resolved, and each is applied in the reviewer's words over exactly the line range named. The new
text is true where it stands, and every label it cites resolves to the result it means. The quantifier order of m2 is
consistent with "d fixed throughout", with lem:iii-i7-2-5 (c) and with lem:iii-j2-2-3, and every use of
prop:iii-i8-4-1 (i) in chapters 40–44 still follows. The meaning m3 gives to "F_j → F in 𝒴" is what the proof of
lem:iii-i7-4-1 needs and what its use supplies. The one nit (N1) carries that meaning to 𝒴(α), where the induction of
prop:iii-i8-4-1 (ii) already relies on it.

## One row per item

| item | site at HEAD | resolved | true where it stands, labels checked | range exact, joins clean |
|---|---|---|---|---|
| m1 | 41:1428–1434, 41:1460–1462 | yes | yes: thm:iii-i11-4-1 = Theorem 33.18, lem:iii-i11-3-2 = Lemma 33.16, lem:iii-i12-2-1–lem:iii-i12-2-4 = Lemmas 33.20–33.23 | yes: old 1428–1433 (6 lines) became 7 lines, old 1459–1461 became 3 |
| m2 | 40:1143–1147, 40:752–758 | yes | yes: eq:iii-i8-4-2 = (32.26), sec:iii-i8-1 = Section 32.6, prop:iii-i8-4-1 = Proposition 32.29, lem:iii-i8-2-6 = Lemma 32.24, lem:s21-motions-at-b = Lemma 32.25, lem:iii-i8-3-2 = Lemma 32.27 | yes: old 1137–1140 became 5 lines, old 748–752 became 7 |
| m3 | 40:493–498 | yes | yes: sec:iii-i7-1 = Section 32.1, lem:iii-i7-2-5 = Lemma 32.9, lem:iii-i7-3-1 = Lemma 32.10, lem:iii-i7-4-1 = Lemma 32.12 | yes: old 493–495 became 6 lines |
| n1 | 40:589–592 | yes | yes: lem:iii-i7-2-5 = Lemma 32.9, lem:iii-i7-3-1 = Lemma 32.10 | yes: old 586–588 became 4 lines |

## The application

- **Exact text.** Each of the six replacement blocks of R-P-40-sem (as committed in 06988e45) occurs verbatim in the
  chapters at HEAD: m1 at 41:1428 and 41:1460, the statement of m2 at 40:1143, sec:iii-i8-1 of m2 at 40:752, m3 at
  40:493 and n1 at 40:589.
- **Exact ranges.** I took the parent files and replaced 40:493–495, 586–588, 748–752 and 1137–1140, and
  41:1428–1433 and 1459–1461, with the six blocks. The result is equal, byte for byte, to chapters 40 and 41 at HEAD.
  So nothing else in either chapter changed, and no other line was touched.
- **Joins.** I compared the word sequences of the parent and HEAD over each hunk with three lines either side. Every
  context line is equal. The only differences are the reviewer's intended ones:
  - m3: "Forcings converge in" became "F_j → F in 𝒴 means convergence in each of". The clause "up to a regularity that
    d, being large, allows" and the sentence "It is not convergence in ‖·‖_𝒴 alone … through a forward solution" were
    added. "For α and α_+ as above let" still ends the paragraph before "𝒴^S_(α,α_+) := …".
  - n1: "the norm" became "a norm", "u_1 below" became "u_1 of the count below", and "|Ṡ…(F) − Ṡ…(F)| ≤" became
    "Ṡ…(F) − Ṡ…(F) has norm at most". "And for F_1, F_2 ∈ 𝒴 …" follows unchanged.
  - m2 in sec:iii-i8-1: "which depends on the seminorm of the solution bounded and is" was inserted, and "its proof"
    became "the proof". "For each seminorm that (i) bounds these choices are finitely many and are made first;" was
    inserted, "d is taken" became "d is then taken", and "the bounds by ‖h‖ used below hold in these seminorms" became
    "the bounds used below hold in them, uniformly for h small". "(b)" became "(b)–(c)". The heading of sec:iii-i8-2
    follows after the blank line.
  - m2 in the statement: ", d being large for ‖·‖_(α) ([[sec:iii-i8-1]])" was inserted before "; (ii)". The rest was
    reflowed.
  - m1, Step 6: "C‖F‖_(𝒴⁰(α))." became "C‖F‖, ‖F‖ being the seminorm of 𝒴⁰(α) of large enough regularity at the end
    of the proof of [[thm:iii-i11-4-1]]."; "the proof of [[thm:iii-i11-4-1]]:" became "that proof:"; "C‖F‖_(𝒴⁰(α))"
    became "C‖F‖"; and "in that proof," became "there,". The old 1434 ("every coefficient and ũ …") follows unchanged.
  - m1, remark: "C‖F‖_(𝒴⁰(α));" became "C‖F‖, with ‖F‖ a seminorm of 𝒴⁰(α) of larger regularity, as there;", and
    "C‖F‖_(𝒴⁰(α))," became "C‖F‖,". The heading of sec:iii-i13-1 follows.
- No sentence is lost or duplicated at any join.

## m1 and n1, true where they stand

- **m1, Step 6 (41:1428–1434).**
  - The forcing f′ = G(W⃗) − (L_(h,p⃗) − L_(b_0))u_0 of Step 0 is bounded by C‖F‖. The next sentence gives the reason:
    ‖G(W⃗)‖_(𝒴⁰(α)) and ‖u_0‖_(w_(α′)) are at most C‖F‖ (41:1040), and the count of Step 0 of the proof of
    lem:iii-i11-3-2 applies (41:890–893).
  - w_(α′) = min(α′ − 2, λ_♯ − 1) is the w_0 of the proof of thm:iii-i11-4-1 (41:967), and α′ ∈ (2, 3) is the level
    fixed there (41:966).
  - "the seminorm of 𝒴⁰(α) of large enough regularity at the end of the proof" is 41:1035–1037. No seminorm now appears
    on both sides, so the cycle the reviewer read in the old wording is gone.
- **m1, remark (41:1460–1462).**
  - The three terms are C‖G‖_(𝒴⁰(α)), C(‖h‖ + |p⃗|)‖u_0‖_(w) and C Σ|W_ν|, with |W_ν| ≤ |p⃗′|. Each is at most C‖F‖.
  - "of larger regularity" is right. ‖F‖ bounds ‖F‖^+_(𝒴(α′)). That seminorm bounds the solution in ‖·‖_(α′), whose
    regularity is at least that of ‖·‖_(w) (41:935–936). ‖·‖_(w) is two orders above ‖·‖_(𝒴⁰(α)) (Step 0 of
    lem:iii-i11-3-2), and a forward solution gains at most one derivative. So ‖F‖ lies strictly above ‖·‖_(𝒴⁰(α)).
  - The statement of thm:iii-i12-3-1 ("bounds uniform") is untouched.
  - No other "C‖F‖_(𝒴⁰(α))" remains in chapters 40–46. The three "‖F‖_(𝒴(α))" in lem:iii-i8-3-2 (40:1002, 1096,
    1098) are the fixed pair, as intended.
- **n1 (40:589–592).**
  - ‖·‖^+_𝒴 is not unique, so "a norm" is right.
  - "u_1 of the count below" names the u_1 defined at 40:598–599, with F_1 = F for the Ṡ bound.
  - The bound "Ṡ_(h,p⃗)(F) − Ṡ_(0,p⃗_b)(F) has norm at most C(‖h‖ + |p⃗ − p⃗_b|)‖F‖^+_𝒴" is proved at 40:606–608: the
    difference is Ṡ_(0,p⃗_b)(R), of size at most C‖R‖_(𝒴^S_(α,α_+)). Ṡ takes values in 𝒮_1 ≅ ℝ⁴, so "norm" is the
    absolute value.
  - "d being large enough for lem:iii-i7-3-1 (c) in it as well" is what 40:622–623 and 40:635–636 use.

## m2: the quantifier order

The order now stated is as follows. sec:iii-i8-1 (40:752–758) says: "For each seminorm that (i) bounds these choices
are finitely many and are made first; d is then taken so large that the bounds used below hold in them". The statement
(40:1145) says: "d being large for ‖·‖_(α)".

- **The chain is finite and does not depend on d.**
  - For a target ‖·‖_(α″), the step fixes ‖·‖_(𝒴(α″)) and ‖·‖_(α′) (sec:iii-i8-1, for lem:iii-i8-3-2 with the
    remainder in the target), then ‖·‖^+_(𝒴(α′)) by (i) at α′, then ‖·‖^+_(𝒴(α″)) (40:1163–1168). The recursion goes
    down to α_0, where the base takes ‖·‖^+_(𝒴(α_0)) from the continuity of the maps of cor:iii-i7-4-6 on 𝒴(α_0)
    (40:1153–1155).
  - The regularities are fixed by the losses of the solution maps, which do not depend on d once d is large. So nothing
    in the chain is circular, and the n + 1 levels give finitely many seminorms.
  - (ii) at α″ also needs one seminorm two orders above ‖·‖^+_(𝒴(α′)), and its own chain (40:1238–1241). That chain
    is determined by the fixed ‖·‖_(α′), so it is among "the bounds used below".
- **sec:iii-i7-1, "d fixed throughout" (40:165–166).** That sentence reads "A large d, at least the d of
  eq:s20-d, is fixed throughout". "Large" there is the sum of the largeness requirements the chapter states as it goes;
  the old sec:iii-i8-1 already said "d is taken so large that". With m2, (i) is a statement for those targets for which
  the one fixed d is large. The targets the paper uses are finitely many fixed seminorms, chosen before d and
  independently of it. So one d serves them all, and "fixed throughout" stands. The new "then" orders the requirement
  and does not choose d a second time.
- **lem:iii-i7-2-5 (c) (40:356–357).** It gives bounds "at each finite regularity … with constants uniform for (h, p⃗)
  small", with "h small" in 𝒳^d. Read literally with one d, that also asks for every regularity at once. The working
  order is the same as m2's: the regularity first, then d large for it. m2 states that order explicitly for (i). m3 uses
  the same order for convergence ("up to a regularity that d, being large, allows"). The two passages agree.
- **lem:iii-j2-2-3 (43:292–322).**
  - The proof says "ch:s21 fixes 'h small' as small in 𝒳^d, d fixed, … and takes the same convention for
    prop:iii-i8-4-1 and T_(h,p⃗)" (43:302–304). It ends: "None of these orders depends on k, and d_* is their maximum"
    (43:321).
  - Under m2, the orders that (i) demands are those of the chains of the targets used. These are fixed seminorms of
    the reads, and they depend neither on k nor on d. The d of ch:s21 is one of the orders collected, so d ≤ d_*, and
    it is at least the threshold of every target used.
  - The seminorms first, then d_* as their maximum, then the d of the later chapters (44:358–361 "d and the order of
    the seminorm of q being large"; 46: d ≥ d_* + 5): this is the order m2 states. It is consistent.
- **The uses of prop:iii-i8-4-1 (i) in chapters 40–44.** I grepped for prop:iii-i8-4-1 in chapters 38a–44 and read
  every use of (i). In each, the target is a fixed seminorm chosen before d, so the proviso "d being large" is part of
  the one fixed d.
  - **40:1190–1195, 1215–1223.** These are (i) at α′ inside the step, for ‖·‖_(α′) and with ‖·‖^+_(𝒴(α′)). They
    follow.
  - **40:1238–1245, (ii) at α″.** This passage says "by (i) at α′, the w_j are bounded in each fixed seminorm …, among
    them one of regularity two above that of ‖·‖^+_(𝒴(α′))". "Each" is read with the statement's proviso, and the
    proof uses only the one named, which is among the choices made before d. It follows. Not a finding.
  - **41:918–937, lem:iii-i11-3-3.** The target ‖·‖_(α′) is chosen with regularity at least that of ‖·‖_(w)
    ("as sec:iii-i8-1 allows"), and R_j → 0 in ‖·‖^+_(𝒴(α′)). It follows.
  - **41:970–979, prop:iii-i8-4-1 for P_4.** The extra term is O(|W⃗|) in every seminorm. It follows.
  - **41:1023–1026, "Near (0, 0)".** The target is taken as in lem:iii-i11-3-3. It follows.
  - **41:1034–1041, the end of thm:iii-i11-4-1.** The target is ‖·‖_(α′) as above; ‖·‖^+_(𝒴(α′)) and ‖F‖ are of
    large enough regularity. It follows.
  - **41:1618–1621, lem:iii-i13-2-3.** "As there". It follows.
  - **42:402–416, P_5 at (h, p⃗, q).** This is a transfer with terms O(|W⃗| + ‖q‖), and "q small" in a seminorm of
    large order, after d (42:143–144). It follows.
  - **44:320–324**, the induction bound at k = 0: "the seminorms of u(p⃗′) in 𝒵_(β_k) that are used below". These are
    finitely many. It follows.
  - **44:328–331 and 44:393**, |p⃗′_(α_1)(Ψ)| ≤ C‖Ψ‖^+_(𝒴(α_1)) with (2) in that seminorm, "d and the order of the
    seminorm of q being large" (44:358–361). It follows.
  - Chapter 43 cites (i) only in inventories (43:213, 378, 396). Chapters 38a and 39 have no uses.

## m3: the meaning of "F_j → F in 𝒴"

The new text (40:493–498) says: convergence in each of the finite-regularity spaces on which lem:iii-i7-2-5 (c)
holds, up to a regularity that d allows, as lem:iii-i7-3-1 (c) gives for h → 0 in 𝒳^d; and not convergence in
‖·‖_𝒴 alone.

- **What the proof of lem:iii-i7-4-1 needs (40:510–540).**
  - In (a), Ṡ_(0,p⃗_b)(R_j) reads R_j in 𝒴^S_(α,α_+) at the regularity k at which Ṡ is bounded (lem:iii-i7-2-5 (c)).
  - R_j contains (L_j − L_0)u_j, an operator of order 2 applied to u_j (eq:iii-i-4-2). So u_j must be bounded
    uniformly at regularity k + 2, and lem:iii-i7-2-5 (c) gives that from a bound on F_j at k + 2 plus the loss.
  - F_j − F → 0 is needed at regularity k.
  - (b) is the same with Q_(0,p⃗_b) on 𝒴.
  - Convergence in every finite-regularity space up to what d allows gives both the convergence at k and the
    boundedness at k + 2 plus the loss. Convergence in ‖·‖_𝒴 alone gives neither. The new sentence describes the proof
    correctly: it "reads u_j two orders above the norm in which it reads the parameters, and bounds u_j by F_j through a
    forward solution".
- **What its use supplies.**
  - The statement is used only in the base of prop:iii-i8-4-1 (ii) (40:1157–1158), through lem:iii-i8-3-1, which
    transfers it to 𝒴(α_0) (40:959–961). 40:986–989 and the proof of prop:iii-i15-2-12 use its counts, not its
    statement. 43:303, 376 and 44:503–506, 646 are inventories, "at fixed b only".
  - In the induction, (ii) at α″ applies (ii) at α′ to Ψ_j and to F_j(S⃗_j). Their convergence comes from
    lem:iii-i8-2-6 (c) (40:1233, 1247, 1252–1253), that is, from the continuity of the sources for h_j → 0 in 𝒳^d.
  - So what reaches the base is convergence at every regularity that d allows, which is exactly the stated meaning.
    The hypothesis of (ii) at the top level supplies at least that.
- **Conclusion.** The two agree, and m3 is right.
- **N1 below.** The same meaning is needed for "F_j → F in 𝒴(α)" in prop:iii-i8-4-1 (ii). Read in the Fréchet sense
  (sec:iii-i8-1 calls 𝒴(α) a Fréchet space), the hypothesis of (ii) at α′ would ask for more than the step at α″ can
  pass down.

## Finding

### N1 (nit): chapters/40-s21-parameters.md:756–758, the convergence in 𝒴(α), and "bounds" for lem:iii-i8-2-6 (c)

**The problem.**

- m3 now fixes what "F_j → F in 𝒴" means. prop:iii-i8-4-1 (ii) (40:1146, 1225) and lem:iii-i8-3-3 (40:1105) use
  "F_j → F in 𝒴(α)".
- sec:iii-i8-1 says only that 𝒴(α) is a Fréchet space (40:745). lem:iii-i8-3-1 carries the meaning to α_0 ("with
  𝒴(α_0) in place of 𝒴"), but no sentence carries it above α_0.
- The induction relies on that meaning. The step of (ii) at α″ applies (ii) at α′ to forcings that converge only as
  lem:iii-i8-2-6 (c) allows for h_j → 0 in 𝒳^d (40:1247, 1252–1254). Read as Fréchet convergence, the hypothesis of
  (ii) at α′ would not be met.
- A smaller point: the new sentence names lem:iii-i8-2-6 (c) among "the bounds used below", but (c) is a continuity
  statement.

The reading is clear from the analogy with sec:iii-i7-4, so this is a precision, not a gap.

**Replacement for 40:756–758** (five lines for three; the blank line and the heading of sec:iii-i8-2 follow unchanged):

```
many and are made first; d is then taken so large that the bounds and the continuity used below hold in them,
uniformly for h small: those of [[lem:iii-i8-2-6]] (b)–(c) and [[lem:s21-motions-at-b]], and the count of Step 0 of
the proof of [[lem:iii-i8-3-2]]. F_j → F in 𝒴(α) is meant as F_j → F in 𝒴 is in [[sec:iii-i7-4]], at the regularities
that d allows: the step of [[prop:iii-i8-4-1]] (ii) applies (ii) at the level below to forcings that converge only as
[[lem:iii-i8-2-6]] (c) allows for h_j → 0 in 𝒳^d.
```

The lengths are 109, 115, 117, 117 and 49 characters in the source, and 109, 95, 106, 115 and 42 after label
resolution (Lemma 32.24, Lemma 32.25, Lemma 32.27, Section 32.5, Proposition 32.29). No line starts with a forbidden
marker, and there is no backslash. The old line 755 ("bound the seminorm of (i) at α′ as well as ‖·‖_(𝒴(α)). For each
seminorm that (i) bounds these choices are finitely") stays as it is.

## Observation, no action

- 40:498 is a two-word line, "above let", left by the reflow of m3 before the unchanged "𝒴^S_(α,α_+) := …". It is
  within the contract and renders as one paragraph.

## Contract and checks

- I computed lengths with assemble.py's own number() in memory, writing nothing. Every changed line of chapters 40 and
  41 is at most 121 characters in the source and after label resolution. The longest in the hunks is 118. The longest
  in either whole file is 121, at 40:1701 and 41:1753, which were not touched.
- No changed line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
- The changed lines contain no backslash and no file, program, code or AI language.

Run from the paper directory at HEAD:

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)

    $ python3 assemble.py --check
    labels 4570, computations cited 0, problems 0
