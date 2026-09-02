# READ-26b.md — chat 150 (Cowork) — 26b-04, the reading of the Register for F.3's rule

DEF-143 item 11's **fifth** re-derivation. Instrument `r2-26b.py`, golden `r2-26b.out`. Members read: the main volume
and **the Register in full through its entry index**; the four compendia and the Index of Indices searched for the
rule's words. Line numbers are MEMBER line numbers, measured this chat, never carried.

**What was owed.** Chat 139 recorded 26b-04 against F.3 L11298–L11299 — *The work applies this without exception, and
several of the corrections the Register carries are exactly this rule firing* — on a probe of the rule's words that
returned **0** Register matches, and said in terms that a token probe is not a reading. DEF-139 item 6 owed R3 a
**reading of the Register for the rule's firings before the sentence is scored**. This is that reading.

## A — deviations

- **26b-04 is REVERSED. The sentence measures TRUE, and the earlier record was a finding about the probe.**
  The rule was scored as a MECHANISM, not as a phrase. F.3 prints it in two forms: **RULE-H** (L11295, *A constraint
  refuted by its own extent is dead*) and **RULE-E** (L11296–L11298, *if … computing its extent on that ground returns
  the empty set or the whole of it … not weakened, not pending, dead*). A candidate pool of **69** Register entries was
  enumerated by three named nets (the elaboration's outcomes in the entry's own words; the headline or a citation of
  F.3; the named class §4.6 and registers 777 / 784 / 900 / 1383), and **every one of the 69 was scored with a deciding
  phrase the instrument asserts is present in that entry's own text**. Result: **15 firings over constraints proper**
  (365, 412, 443, 522, 843, 1174, 1310, 1424, 1463, 1513, 1605, 1617, 1661, 1683, 1686), **21 more over the checks and
  tests of the same class** (181, 189, 422, 598, 613, 775, 784, 797, 798, 801, 803, 840, 845, 849, 851, 1383, 1448,
  1469, 1582, 1618, 1671), **1 under the headline form only** (1729), **5 counter-cases where the rule was applied and
  the object survived** (390, 439, 462, 900, 1061), **3 undecidable, carried as an upper bound** (333, 810, 1504) and
  **24 another mechanism**. *several* was scored under BAND — STRICT ≥ 3, LOOSE ≥ 2 — and is reached in **every cell of
  both conventions**, the smallest cell being **15 of a Register of 1,628 entries (2.27 %)**. The population needed no
  assumption: register 1762, restated at 1784, defines an entry as *one withdrawn claim for each entry this register
  holds*, so **every** entry is a correction.
- **26b-11 — NEW, and the finding that survives the reversal. The one instance the book names is not an instance of
  the rule as F.3 elaborates it.** E.1.5 L11024 (*A constraint refuted by its own extent is dead, which is F.3's rule,
  and it dies here: R occupies a cell the constraint refused*) and Register 1729 (*F.3's rule applies and it is
  dropped*) both cite the rule for item R against the code's constraint *obstacle = buildable ⟹ cost ≤ days*. That
  constraint is refuted by a **counterexample** — R is buildable and unbounded because counting closed sets is
  #P-complete — and its extent on the fourteen is **neither the empty set nor the whole of them**. It satisfies RULE-H
  and fails RULE-E. **F.3 prints two forms of one rule whose extents differ, and states nowhere which is meant.**
  Docket 34 (an unstated convention) / 9(b).
- **26b-08 — NEW.** Register L3113 (entry 845): *§784's pattern, fifth sighting*. A **Register number printed with a §
  sigil**; §784 resolves to no section in any of the six volumes (one site, MEASURED). Docket 9(c) / 28.
- **26b-09 — NEW.** Register L6299 (entry 1686): *Thm 11.1 makes T — not a function of (Z, charge, ℓ, mult) — a new
  measurement*. **Theorem 11.1 is printed in none of the six volumes** (MEASURED, both forms *Theorem* and *Thm*). The
  citation carries the weight of the entry's verdict and has no target. Docket 9(c) / docket 2.
- **26b-10 — NEW.** Register L6507 (entry 1763): *run489.py, ruled\_bracket.py, RULING-TOLERANCE-489.md and the run's
  JSON go to **BUILD-10*** — a build handle and four internal file names inside a reader-facing volume. Ruling 46;
  docket 6 / 28; the same class as the 3B.\* label form at census 1536–1545.

## B — verified (measured true)

- **B-01** The rule and its claim have exactly three sites in the six volumes: main L11024 (E.1.5), L11295 (F.3's
  statement) and L11299 (the claim). The claim lies inside the F.3 unit, between `### F.3` L11278 and `### F.3.1`
  L11301.
- **B-02** Chat 139's token probe **reproduces exactly**: 0 entries carry the rule's words. The widened probe
  (*extent* with *empty* or *whole of it* in one entry) returns one entry, 1767, which is not a firing. The record of
  26b-04 was right about the probe and right to refuse to score on it.
- **B-03** The Register: **1,628 entry headings, extent 1 to 1792**, unchanged.
- **B-04** **The work applies the rule and finds it does not fire.** Five counter-cases carry their own witness: 390
  (a closure defect tested against four boundaries), 439 (*Not vacuous* — five of twenty closed indices state a verdict
  and no expression), 462 (§17.3's criterion covers 0.8–10.3 %, an extent strictly between the poles), 900 (eight
  pre-stated tests and a corrected null), 1061 (a claim at 191/191 that met a bad datum and reported it).
- **B-05** **No WARNING marker** (the colon form, chat 142's convention) stands on any entry scored as a firing. 1463
  carries *FISHBURN'S WARNING* in its own headline — an imported hazard, and the reason the entry fires — not a
  Register marker. 38 WARNING markers in the Register in all.
- **B-06** No later statement in any volume qualifies the sentence; L11299 is its single site.
- **B-07** §4's mechanism *a test that could not fail* is named at §28.7.9 L7691 and worked in the Register as
  register 784's pattern (798 *fourth sighting*, 845 *fifth sighting*, 849 at scale, 1383 as the contingency
  protocol). It is the same shape as F.3's rule stated in a second vocabulary, which is why OBJ-C and OBJ-T are
  scored separately rather than merged.

## Census

**CENSUS-CLOSURES-26b.tsv.** Engaged range: main L11278–L11327 (the F.3 unit) and L11014–L11035 (E.1.5's paragraph),
plus the Register spans of the 69 pooled entries. **31 rows engaged; 5 were closed in earlier units** (1221, 1222,
1223 in the ch24a unit; 1228, 1229 in the ch26a unit — the earlier line governs, G0b) **and 26 are closed here: four
defects** (7 — §784 as a section pointer, 26b-08; 13 — Theorem 11.1 unprinted, 26b-09; 1473 — 26b-06's *never an
F.3.1 or an F.3.2* against Prints & Proofs; 1556 — the BUILD-10 handle, 26b-10) **and twenty-two not a defect**, each
a C9 word inside the entry's own measured past-tense finding (precedents 678, 680–687, 1067, 1069, 1217).

## C — incidental

- **Candidate, recorded and not scored:** *The work applies this without exception* (L11298; census row 1228, closed
  *not a defect* in the ch26a unit as the section's own scope statement). The nearest exception the reading found is
  **register 333**: a criterion the **empty index** satisfies is weakened to *necessary for completeness and not
  sufficient for content* rather than declared dead, where RULE-E says *not weakened, not pending, dead*. One site.
  Docket 19 for R3.
- **Docket 5 / 6 candidates in the pool, recorded not scored:** the first-person register entries scored above are
  the Register's own voice and are outside this family's unit; no new Ruling 45 or 46 site was measured in the main
  volume's F.3 unit this chat.
- **Docket 27:** not a section read; no clean-unit count is engaged.
- **Conventions, two new.** (i) **TWO-FORM**: where a rule is printed as a headline and an elaboration, both are named
  and both are scored, and an instance is reported against each — the forms are not assumed to have one extent.
  (ii) **POOL**: a mechanism is read by enumerating a candidate pool from named nets and scoring **every** member with
  a deciding phrase asserted present in that member, so that a reading is checkable in the same way a count is.
