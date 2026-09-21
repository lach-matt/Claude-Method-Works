# SOURCES.md — provenance map for 07-wall-janet (not published)

Paper: `PAPER.md`, "The Parent-Term Wall and the Janet Collapse". Drafted 2026-09-21, resuming a
`check.py` left complete at 90 obligations by an earlier run. Every number in the paper is produced
by `check.py` — **101 of 101 obligations pass** (EXHAUSTIVE 85, GUARD 3, MACHINE-CHECKED 13);
`python3 check.py --selftest` adds four negative controls, all refuted, for 105 — or is CITED.

Run it with `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH` first; it takes about
six minutes, most of it the 7×18 Z3 obligation.

## What this run changed in the inherited `check.py`

The inherited file ran clean on `python3 check.py` (90/90) but **`--selftest` failed one negative
control**, and that failure is a bug in the check, not a claim of the source that does not
reproduce. The control built `janet_cells(JANET_ROWS_118) + [(3, 13)]` and asserted E > 0; E is 0.
Reading the construction: appending (3, 13) to the left-step index leaves it a **chain** — (3, 13)
is above every cell of rows 1–3 and below (4, 13) — and Theorem 1 says a chain is closed, so the
perturbed set was no perturbation at all. The control now *moves* a cell instead: it deletes
(5, 30) and inserts (2, 30), which breaks the chain and gives E = 54, and is refuted as a control
must be. The fact the broken control accidentally established is kept as a positive obligation in
section C ("appending (3, 13) leaves a chain of 119 cells and E stays 0"), and the paper prints it
in §4 as *closure follows the shape, not the count*. Nothing was weakened to make a discrepancy
vanish: the assertion the control makes is strictly stronger than before.

Ten further obligations were added for material the paper needed:

| added obligation | why |
|---|---|
| the table holds both extreme corners (1, 18) and (7, 1) | the hypothesis of Lemma 3, on its own object |
| appending (3, 13) keeps the chain and E = 0 / moving (5, 30) to row 2 gives E = 54 | §4's shape-not-count paragraph |
| the five label conventions: 80 / 9 / 20 / 30 / 457 | the brief requires the conventions a parent may be written in, and `label_form` had lumped jj pairs with run-on configurations |
| the dotted-pattern census reports 80 of 139, undercounting by 59 | the narrow-pattern point, stated as a number |
| the four two-limit species carry 99 rows, split per limit | Figure 5 and §7's table |
| exactly two outer labels are printed at two limits, one of them a parent case | the witness for Proposition 3's necessity direction — Ba III `nd 2[3/2]* J=2` at both limits |
| the highest spectrum number with a multi-level core is IV (Al IV), once | §7's ceiling paragraph (see the discrepancy below) |
| no core in the table has more than one open subshell; the six open shapes are s¹, p¹, p², p⁴, p⁵, d¹ | `core_terms` multiplies per-subshell term counts, which is the configuration's count only when at most one subshell is open — this is the obligation that makes the census exact rather than approximate |
| each Si I identical-key pair differs in exactly two of eleven columns | §8's third kind of repeat, stated with its numbers |
| 4,395 − 1,755 = 2,640 and 139 − 80 = 59; 9,756 + 11,605 + 5,280 = 26,641 | three arithmetic facts the paper prints |

## Where each section draws from

All paths below are under `/home/user/Claude-Method-Works/`.

| paper section | source passages |
|---|---|
| §0, §2 D1–D4, Lemma 1, Lemma 2 | `method/members/The_Method_1_6-2.md` 1516–1560 (§6 and §6.1: the 90 / 126 / 36 table; the definition of Âᵢ, φ̂ᵢⱼ and ℛ(X); "E(X) = |ℛ(X)| − |X| is the gap"; "no outside knowledge enters"); 1607–1620 (idempotence of ℛ, and that a drawn band's closure is a theorem rather than a finding); `tools/cypher.py` `op_order` (imported by path — the staircase as the instrument computes it) |
| §3 Theorem 3, Theorem 4, Proposition 1 | main volume 1522 (the 36 named as period 1 groups 2–17 and periods 2/3 groups 3–12), 1551–1566 (§6.1.1: the decomposition 25 forbidden + 11 deferred; "1p contributes five and not six, because helium occupies group 18 itself"; helium at group 18 → E = 36, at group 2 → E = 20; "the difference is sixteen cells"), 1570–1572 (the three-convention table: 18-column 90/36, 32-column 118/106, left-step 120/0); `method/members/The_Method_1_6___The_Index_of_Indices-2.md` 1361–1372 (all 90 cells listed period by period), 1440–1444 (the periodic table as the control index) |
| §4 Theorem 5 | Index of Indices 1374–1388 (the eight rows of Janet with their atomic-number ranges and lengths 2, 2, 8, 8, 18, 18, 32, 30; "118 cells, E = 0"), 1446–1452 (118 cells in a box of 944, E = 0; Janet 1929 with the table first published 1928; the shell-length sequence by the Klechkovski–Hakala formulas; the Löwdin challenge as an open problem and "this work uses the ordering and does not explain it"); `method/members/LW1-ground.py` (imported — the tabulated ground configurations, Z = 1…108); `tools/populate.py` `janet_cell` (imported — the differentiating-electron reading, which is the one that fails at six elements); `tools/cypher.py` `_janet` (the (n+ℓ, ℓ) subshell fixture: 22 cells, box 40, E = 0) |
| §5 | `method/members/The_Method_1_6___Spectra_Compendium-2.md` 268–283 ("The Janet collapse": the 3d/4f/5f table at Z = 21, 57, 89; Ti IV nd 0.6202 against Sr II nf 0.0618; "the collapse coordinate is read from the periodic table, not fitted"; Ca I nd 0.908 at Z = 20 and Ba II nf 0.756 at 56); `method/members/The_Method_1_6___Mathematical_Compendium-2.md` 3060–3070 ("The Janet collapse" entry, with Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969 as prior art); `method/members/The_Method_1_6___The_Physics_Compendium-2.md` 478–486 ("Janet block boundary — Z = 21, 57, 89, an exact integer", and "Where it fails: as a SHARP threshold"); Spectra Compendium 40–60 (the bound column, including the three parent-count obstacles at 9,756 / 11,605 / 5,280 cells); `drive/The Method Materials/COORDINATES-2_13.csv` (the 104,832-cell index itself) |
| §6 Theorem 6, Corollaries, Proposition 3 | Mathematical Compendium 742–754 ("The parent-term wall": "an OPEN-SHELL core gives many parent terms and no separable Rydberg series"; Condon & Shortley 1935 ch. VII and Racah 1943 as prior art); Spectra Compendium 250–258 ("The parent-term wall": "A closed-shell core has one parent term and gives one Rydberg series per ℓ. An open-shell core gives one series per parent, all interleaved, converging on different limits"); Mathematical Compendium 2980–2992 ("Core angular structure": at ℓ = 3 δ splits by the core's term while its J-pairs stay together) |
| §7, §8 | Spectra Compendium 293–935 (the channel table, 596 rows) and 973–1027 (§IV: the B.1 source list; the count paragraph — 596 rows, 477 series of three or more members, 119 two-member channels, 28 elements, 70 species, 3,342 levels, 2,269 interior cells, bracket 1,577 of 1,738 on 392 rows, 78 no-triple, 126 untested); `method/proofs/compendia4.py` and `compendia3.py` (read for the conventions and imported by path for the table reader — see below) |
| §9 | Spectra Compendium 297 (the bracket column's definition and its three values); main volume 1633–1646 (an index may bracket a quantity only along an axis the quantity is monotone on; the first-ionisation-energy illustration); the companion paper `03-bracket/PAPER.md` in this series, cited in §9 by description only |

## The parsers: imported, never copied

`check.py` imports five instruments by path and copies none of them:

- `tools/cypher.py` — `Index` and `op_order`, the staircase closure. The fresh reference
  implementation `R_ref` in `check.py` is written from D3–D4 and is *not* a copy; the two agree on
  every object the paper computes, and the encoding guard compares the Z3 witness form against
  `op_order` on 300 random draws.
- `method/members/LW1-ground.py` — `expand`, `GROUND`, `CORE`: the tabulated ground configurations.
- `tools/populate.py` — `core_p`, `janet_cell`, `aufbau_config`, `pauli_bound`, `collapse_C`.
- `method/proofs/compendia4.py` (which itself imports `compendia3.py` and `compendia2.py`) — its
  `rows()` is run as an independent reader of the channel table and its row indices are compared
  against `check.py`'s own parse, row for row. `check.py` also borrows `compendia4.PREFIX` for
  label normalisation rather than re-typing the regular expression.
- `research/warp-drive/prover.py` — `cells_of`, `subset_vars`, `observed`, `in_R`, `prove`,
  `non_vacuous`.

**Where the conventions came from.** `compendia3.py`'s `PARENT` pattern is `^\S*\.\(.*?\)\.`, a
dotted configuration followed by a parenthesised group; `compendia4.py` records that this pattern
"does not see `(3P)ns 4P J=5/2` or `2s22p5(2P*3/2)nd ...`, so it UNDERCOUNTS", and prints 139
against 80. This paper's §7 takes that finding, splits the 39 rows that are parenthesised but not
dotted into 30 jj pairs and 9 run-on configurations by reading the labels, and states all five
conventions with counts. The 59-row margin between the narrowest and the widest reading is the
paper's own arithmetic on those counts.

## Reproduction — what reproduces, what does not, and what was chosen

### Reproduced exactly

E = 36 on (period, group) with the 36 cells named; the decomposition 25 forbidden (1d 10, 1p 5,
2d 10) + 11 deferred (3d 10, 1s 1); E = 20 with helium at group 2 and the 16-cell difference;
E = 106 on the 32-column layout; E = 100 with a block coordinate adjoined; E = 0 on (n+ℓ, Z) at
118 and at 120 cells, with rows 2, 2, 8, 8, 18, 18, 32, 30 and openings 1, 3, 5, 13, 21, 39, 57, 89;
E = 0 on the (n+ℓ, ℓ) subshell index at 22 cells in a box of 40; the 596-row channel table with
70 species, 28 elements, 119 starred rows, 3,342 levels, 2,269 interior cells and the bracket
column at 1,577/1,738 on 392 rows with 78 no-triple and 126 untested; the coordinate index at
104,832 cells, 13,104 keys, 7,260 pairs, grades 929/358/103,545, the 22 bound strings and their
counts, and the measurable chain 61,152 → 11,416 → 4,395 → 1,755; d⁴ = 16 LS terms, and the full
p^k, d^k, f^k term tables; the four two-limit species and the three sub-wavenumber pairs; the four
Ar II notation duplicates and the two Ba III n-window pairs (against `compendia4.py`'s own
selftest fixtures).

### Stated by a source and NOT reproduced — the paper prints the reproduced figure

**1. The Janet-collapse sample and statistics.** Both the Spectra Compendium (line 279) and the
Mathematical Compendium (line 3068) state: *"Across 116 cells with p = 0 at ℓ = 2 or 3: collapsed
median 0.637, uncollapsed 0.036, U-test p = 9.8×10⁻⁴."* Recomputed from the coordinate index with
`populate.core_p`, the figures are:

| quantity | stated | measured here |
|---|---|---|
| cells with p = 0 at ℓ = 2 or 3 | 116 | **128** (of 148 measured d and f cells) |
| collapsed median | 0.637 | **0.6202** |
| uncollapsed median | 0.036 | **0.0335** |
| two-sided p | 9.8 × 10⁻⁴ | **2.5 × 10⁻⁴** (U = 74, z = −3.66) |
| split sizes | not stated | **7 at or past, 121 below** |

The paper prints the measured figures and never the stated ones. The gap of twelve cells is the
likeliest source of the rest: the stated run predates the index's extension to Z ≤ 120 and its
last measured-cell additions, and `check.py` recomputes p from the *tabulated* ground
configuration at each core rather than from whatever list the earlier run used. This is recorded,
not repaired; `check.py` was not adjusted in either direction.

**2. The open-shell charge ceiling.** The Spectra Compendium (line 256) and the Mathematical
Compendium (line 750) both say the compilation holds *"no open-shell ion above charge 6"*. The
measurement is tighter and the statement is therefore true but not sharp: the highest spectrum
number at which a core carries **more than one level** is IV, reached once, by Al IV (core 2p⁵ ²P°).
Reading "open-shell" as "at least one unfilled subshell" rather than "more than one core level"
puts Fe XV in the class — its core is 3s ²S₁/₂, one open subshell and one level — and the ceiling
would then be XV, not 6 either. Neither reading gives 6. The paper prints the measured statement
in the form the classification supports ("no core with more than one level above spectrum number
IV") and states the two Fe species explicitly so the reader can see which reading is in force.

**3. The Fe IV series census is not reproduced, and is not printed.** Both compendia state that
Fe IV's 3d⁴ core carries sixteen LS terms, that the capture shows 13 of them across 24 distinct
(parent, ℓ, term) series, that every one of those 24 has exactly one member, and that Fe IV has
about a thousand analysed levels and no extractable defect. **The channel table holds no Fe IV
rows at all** (the only Fe species present are Fe XV and Fe XVI), and the level data behind the
claim is not in this tree, so `check.py` can reproduce only the term count: d⁴ = 16, exhaustively,
over all 210 Slater determinants of that configuration. The paper therefore states the term count
and the general corollary and omits the Fe IV measurement entirely. It is replaced, as evidence of
the same point, by two things `check.py` *can* verify: the compilation's own ceiling at spectrum
number IV, and the coordinate index's three parent-count obstacles (3 / 16 / 119 parents on
9,756 / 11,605 / 5,280 cells), each shown to equal the maximum term count of the p, d and f block
respectively.

**4. The "one series per parent" rule is CITED structure, not measured here.** The Mathematical
Compendium is explicit that this is Condon & Shortley (1935) ch. VII and Racah (1943), and that
only the Fe IV numbers are the measurement. The paper follows that division: Theorem 6 (the term
counts) is proved and EXHAUSTIVE, Corollaries 1 and 2 follow from it, and the physics that one
parent gives one series is attributed and marked CITED.

### Superseding, where a later passage governs

`compendia3.py` pins Ba III `nd 2[3/2]* J=2` as a label printed at two limits and the short-key
duplicate count at nine; `compendia4.py` supersedes both, after a relabelling that gave every row
of the four two-limit species an explicit parent. This paper measures the **current** table and so
agrees with `compendia4.py`: 139 rows naming a parent, 4 notation duplicates, 2 window pairs, 2
identical-key Si I pairs — and the stripped-label test recovers `compendia3.py`'s Ba III
observation in the form that survives the relabel, since stripping the parent prefix is exactly
what makes the two rows collide again. That is the paper's §6 witness and §8's caution.

## Interpretations chosen, and why

1. **"Ambiguous" is defined as *the species carries two limits and the row names no parent*.** That
   is the criterion `compendia4.py` records M as having ruled on, and it is the criterion Proposition
   3 proves sufficient and necessary *given the data*. A weaker reading ("the core has two levels and
   the row names no parent") would make 93 rows ambiguous; the paper reports both numbers and says
   which is which, so nothing is hidden by the choice.
2. **The sufficiency direction of Proposition 3 is about the data, not the physics.** A species may
   have a multi-level core whose second limit was never captured. The paper says so in §6 and again
   in §0's "what is not established".
3. **The three sub-wavenumber limit pairs are excluded on their magnitude, not on a judgement.**
   Ca II 0.010, Li I 0.036, Zn I 0.020 cm⁻¹: the cut is "a wavenumber or more apart", stated in the
   paper, applied by `check.py`, and it is the same cut `compendia4.py` uses.
4. **The slot rule of Theorem 4 is stated in the paper before it is used.** Reading a
   (period, group) cell as a subshell requires a convention — groups 1–2 the s slot, 3–12 the d slot,
   13–18 the p slot, n = period, f-block set aside. The source states the decomposition and its
   result; the paper states the rule that produces it, so a reader can check the 36 cases.
5. **The collapse section is presented as a coincidence of numbers plus a measured separation, not
   as a derivation.** The source is equally careful ("a measurement against Janet's boundaries, not a
   derivation of them", Index of Indices 1452), and the paper's §0 repeats the caution about the
   seven-member class.
6. **Figure 1 is the audited plate and Figures 2–5 are computed.** The plate was read as an image
   before use and its content matches the text at four points (90 blue, 36 red, 126 total, the red
   pattern row 1 groups 2–17 and rows 2–3 groups 3–12). The companion plate for the seven-index bar
   chart was read and **not** used: its numbers for the calendar, the subnet and the nuclide chart are
   outside this paper's scope and are not produced by `check.py`, and §7 of the contract forbids a
   caption number the checks do not carry.

## Public provenance

The measured levels behind the channel table and the coordinate index are NIST ASD retrievals and
the published compilations named in the paper's §7 and References (Kaufman & Martin 1991; Kramida
& Martin 1997; Sansonetti 2008a, 2008b; Theodosiou, Inokuti & Manson 1986). The ground
configurations are the NIST tabulation. Nothing in the published text points at anything else.
