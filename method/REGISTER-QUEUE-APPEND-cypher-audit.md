# REGISTER QUEUE — the cypher audit (seven entries, ALL SEATED: 1793–1796 at BUILD91, 1797–1799 at BUILD92)

**SEATED.** Entries 1793–1796 are in the store of record. `tools/close_main.py` built
BUILD90 → BUILD91: only the Register member changed, the four count sites were recomputed from
the appended Register, and the reverse guard recovered BUILD90's `49065309b0c4fe8e055f693aed295cca`
before anything was written. `python3 method/verify.py` passes — 343 members, 0 mismatched, both
bundles recovered. **The instruments are seated too**, at BUILD181, with W-190 and DEF-153; that
close also regenerated the MANIFEST rows BUILD91 had left stale. What follows is the record of what
was staged and why.

**Superseded — the state before the seat.** The bundles are untouched, `method/verify.py` still passes, and no
member has changed. This file stages four Register entries and one W entry for M's ruling, in the
forms `close.py` and the Register require. The instruments are `tools/cypher.py` and
`tools/audit_lambda.py`; the run is `python3 tools/audit_lambda.py` — 61 recorded claims about Λ,
**59 PASS, 2 FAIL**, written up in `docs/AUDIT-LAMBDA.md`.

**Family code — RULED.** `cyA-01 … cyA-04` stand as the designations. M: *"keep the current
designations"*.

**Seating — RULED.** The instruments seat as members. M: *"yes"*. See the close block at the foot,
and the blocker below it.

**The counts — RULED, and the tool now exists.** M: *"move the counts. there is supposed to be a
tool to keep the count and front matter numbers current."* There was not one. `numcheck.py` checks
an entry's numerals against a source section, `register_cites.py` checks citations, `bookindex.py`
recomputes §32.1.1 — none maintains the extent. The front matter was hand-kept and went stale,
which is entry 1796. `tools/register_counts.py` is that tool: it counts the Register, checks both
matters against it, reports drift and exits 1, and `--write` emits a corrected copy. Run now it
isolates the three drifted figures; `--appending 4` gives the post-seating targets below.

---

## The four entries, in the Register's form

### 1793

**THE RANK SKEW PRINTS −0.43 UNDER A PRIOR-ART NOTE NAMING THE THIRD STANDARDISED MOMENT, AND −0.43 IS NOT THAT MOMENT: IT IS THE CENTRE OF MASS LESS THE MIDPOINT, 11.0666 − 11.5 = −0.4334, WHILE THE MOMENT ITSELF IS +0.1372.** *The rank sequence reproduces exactly — 1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1 over ranks 3 to 20, measured this chat on the rebuilt Λ₈ at the caps of §7.4 — so the moment is fixed by it and is not in doubt: mean 11.0666, population sd 2.9720, g₁ = +0.1372, sample-corrected +0.1371, the choice immaterial at two figures. The printed number is the displacement the same sentence derives two clauses earlier, and it is correctly computed; what is wrong is its name. The two quantities carry **opposite signs**, so a reader taking the attribution at its word concludes the distribution is left-skewed when its longer tail is the right one — nine rank steps from the peak at 11 down to 20 against eight down to 3. Either the figure is renamed the centre-of-mass displacement and the Gauss attribution dropped, or the moment is computed and printed at +0.14 beside it. The measurement does not choose, and the entry's other half — centre of mass 11.0666 against midpoint 11.5 — stands.* Registers 1791; 1792. (a correction.)

### 1794

**THE RANK-SKEW ENTRY SAYS EIGHT CELLS ARE FIXED BY x ↦ max − x AND THE SPERNER ENTRY SAYS EIGHT SURVIVE IT WITH NONE FIXED; THE SECOND IS RIGHT, AND THE FIRST IS NOT MERELY WRONG BUT UNREACHABLE.** *Measured on the rebuilt Λ₈ at the caps of §7.4: eight cells have their image under x ↦ max − x again in Λ₈, and none is its own image. A fixed point requires 2xᵢ = maxᵢ in every coordinate, so every box maximum would have to be even; the maxima are (3, 1, 3, 3, 3, 1, 3, 3) and **all eight are odd**, so the fixed-point count is zero by parity before a single cell is examined. The eight are the survivors, which is what the Sperner entry says and what carries the non-self-duality; "fixed" in the rank-skew entry is a mis-naming of the same eight, and no second measurement is at issue. The two entries stand on one population and one number, read two ways.* Registers 1793. (a correction.)

### 1795

**THE MARGINAL-EXCLUSION TABLE AND THE AMBIENT BOX PRINTED BESIDE IT ARE DIFFERENT BOXES: ALL EIGHT EXCLUSIONS REPRODUCE ON A 9,216-CELL BOX WHOSE k RUNS FROM 0, AND ON THE 6,912-CELL BOX NAMED WITH THEM k ≥ 1 CANNOT FAIL AND EXCLUDES NOTHING, NOT 25.** *The table ranks the bounds by the cells that satisfy all seven others and fail only this one — g ≤ q 673, q ≤ k 575, k ≤ 4ℓ+2 564, ℓ ≤ n−1 308, 2S ≤ k 300, f ≤ e−1 200, k ≥ 1 25, g ≤ 4f+2 24 — and is described as measured on the rebuilt Λ₈ at the caps of §7.4, beside an ambient quoted at 6,912. Measured this chat: on the box whose k runs 0 to 3, 9,216 cells, **all eight reproduce exactly**; on the 6,912-cell box, whose k runs 1 to 3 because the floor is already applied, the other seven are unchanged and k ≥ 1 excludes 0. Both boxes are legitimate — 6,912 is 9,216 after the k ≥ 1 floor — and the table is right on its own population. The defect is that the population is not the one named next to it: the same class as 1791's unprinted sample, and repaired the same way, by naming the box the figures were taken on.* Registers 1791. (a correction.)

### 1796

**THE REGISTER'S FRONT MATTER GIVES ITS MATURE RECORD AS "165 TO 1791, 1,470 ENTRIES" WHERE THE BACK MATTER GIVES 165–1792; THE BACK MATTER IS CURRENT, THE FIGURE IS 1,471, AND UNDER THE PRINTED 1,470 THE FRONT MATTER'S OWN THREE PARTS DO NOT SUM TO ITS OWN TOTAL.** *Counted on the BUILD180 member: 1,628 single-number headings and 7 grouped headings — docket 30's seven, at register lines 1319, 1323, 1327, 1331, 1335, 1339 and 1343 — giving **1,635 headings, which is exactly the total both matters print**, so the total is right and the entry count is a count of headings. By that count genesis 1–94 is 94, superseded 95–164 is 70, and the mature record is 1,464 single plus the 7 grouped = **1,471**. 94 + 70 + 1,471 = 1,635; 94 + 70 + 1,470 = 1,634. The front matter is stale by exactly one entry — 1792, which the back matter already carries — and the deficit in its own arithmetic is that same one.* Registers 1792. (a correction.)

### 1797 — SEATED at BUILD92

**THE AGREEMENT THEOREM'S "ONLY IF" HALF HAS A COUNTEREXAMPLE, AND IT IS THE BOOK'S OWN MATHEMATICAL OBJECTS: THE GRADING (STATUS, VERIFICATION, PRECEDENT) OVER THE 77 ELEMENTS OF `dclose.py` HOLDS 11 CELLS OF A 16-CELL BOX, EVERY ONE OF THE FIVE OPERATOR-BEARING LANGUAGES ADMITS THE SAME 13, AND E = 2.** *Register 1176 states E(X) = 0 if and only if the languages agree — six indexes, three operators, without exception. Measured this chat on the seated instrument's own element list, with all three coordinates ordinal by construction (withdrawn < conjectured < measured < verified < proved; cited < sampled < exhaustive; none found < found), so the reading rests on no lexicographic fallback: order, algebra, geometry, information and statistics return **identical** admitted sets, which is agreement in the strongest sense available, and the index lacks two of them —* **measured · exhaustive · found** *and* **verified · sampled · found**, *each a grading a mathematical object could carry and neither occurring among the 77. The "if" half is untouched: every index measured here that closes does have its languages agree. It is the converse that fails, and the census had already flagged the wording — row 1321, C9-OVERGENERALISATION-WORD, on this entry's* **without exception**. *Two further readings of the same elements are recorded and are not defects: with kind and discipline on axes the object is wide open at E = 492, which is register 1356's fault and not a finding; and* **all 24 fibres close at E = 0 in all five languages**, *where `dclose.py` shows order alone.* Registers 1176; 1173. (a correction.)

### 1798 — SEATED at BUILD92

**THE INDEX OF INDICES PRINTS Λ_const's FIFTH CENTRE AS 5.4 WHERE THE MATHEMATICAL AND PHYSICS COMPENDIA BOTH PRINT u₀ = 4, AND THE SENTENCE ADJUDICATES ITSELF: 5.4 IS NEITHER AN INTEGER NOR A HALF-INTEGER, SO IT FALSIFIES THE CLAIM IT IS PRINTED AS EVIDENCE FOR.** *Λ_const's role axis is defended in both volumes by the observation that every CENTRE is a small integer or half-integer and no SCALE is. The Mathematical Compendium lists them as 2 for the free shells, 2 for the gate, −1.5 for the switch, 2.5 for the ℓ-validity and* **u₀ = 4***; the Physics Compendium carries* **u₀ = 4** *in its own table — outside the collapse region, the switch local to the d-wave entry. The Index of Indices lists* **2, 2, 2.5, −1.5, 5.4** *— the same four values and a fifth that differs. This is not settled by preponderance: 2 × 4 = 8 is an integer and 2 × 5.4 = 10.8 is not, so under the claim's own test only 4 can stand in a list printed to show that every centre is a small integer or half-integer. The Index of Indices is the volume to move, and the other four centres agree across all three. Measured this chat on the seated members of the three volumes.* Registers 1797. (a correction.)

### 1799 — SEATED at BUILD92

**THE TWELVE UNWITNESSED ROWS ABOVE Z = 108 ARE OFFERED AS THEORETICALLY SECURE ON THE GROUND THAT A WORST-CASE SPIN-ORBIT NARROWING OF 0.083 HARTREE IS CLEARED BY EVERY MARGIN, AND THE TABLE PRINTED DIRECTLY ABOVE THAT SENTENCE GIVES THE MARGINS AS 0.058 TO 0.264 — SO AT LEAST ONE ROW OF THE 7p BAND DOES NOT CLEAR IT.** *The Spectra Compendium's §0′ grades Z = 109–120* **UNWITNESSED** *— "no measurement exists to meet; published falsifiable" — and its unwitnessed-twelve table gives 6d over 109–112 at margin 0.171 → 0.264, 7p over 113–118 at* **0.058 → 0.210**, *and 8s at 119 and 120 at 0.097 and 0.098. Immediately beneath it: "Worst-case spin-orbit narrowing 0.083 Ha; every margin clears it." The main volume prints both figures in ONE sentence — "margins 0.058 to 0.264 hartree, the worst-case spin-orbit narrowing 0.083 hartree clearing every one" — so the claim is refuted by the numerals beside it and needs no reconstruction at all: 0.058 < 0.083. Only the 7p band is at issue; the 6d band's least margin is 0.171 and the 8s rows are 0.097 and 0.098, and all eight of those clear.* **How many of the six 7p rows fail cannot be read off, because the table prints the band's range and not its rows** *— which is itself the repair: print the per-row margins and the exceptions can be named, or restrict the clearance claim to the rows that hold it. The grade* **UNWITNESSED** *stands and is not in question. What does not stand is the clearance argument printed with it, and therefore the half of these rows' standing that says they are theoretically secure against the narrowing. Measured this chat on the seated members of both volumes.* Registers 1712; 1798. (a correction.)

---

## What seating these costs elsewhere

Appending 1793–1796 moves the Register's own counts, and both matters must move together or 1796
is reintroduced by the repair:

| site | now | after |
| --- | --- | --- |
| front matter, total | 1635 entries, 1 to 1792 | 1639 entries, 1 to 1796 |
| front matter, mature | 165 to 1791, 1,470 entries | 165 to 1796, 1,475 entries |
| back matter | 1635 entries, 1 to 1792 (… mature record 165–1792) | 1639 entries, 1 to 1796 (… mature record 165–1796) |

`94 + 70 + 1,475 = 1,639`, which is the check 1796 is about.

---

## The blocker M's "yes" ran into — RESOLVED by building the route

**`close.py` could not seat entries 1793–1796, and nothing else in the tree could either.**
`tools/close_main.py` is that route, built this session and used to seat them.

`The_Method_1_6___The_Register-2.md` is a member of **BUILD90_main**, which holds two members —
the main volume and the Register. `close.py` takes `--old`/`--new` on the **compendia** bundle and
reads `--main` only to build the manifest; it never writes it. Both were verified this session:
main is `49065309…` and unchanged across W-186 through W-189.

So the four entries divide:

| what | route | status |
| --- | --- | --- |
| the instruments as members | `close.py`, compendia BUILD180 → BUILD181 | ready to run |
| entries 1793–1796 | `close_main.py`, main BUILD90 → BUILD91 | **DONE** |
| the count move | `close_main.py --recount` | **DONE** — 1,639 entries, 1 to 1796, mature 1,475 |

The count move is not an append — it changes two numerals inside a member — and `close.py`'s step
(6) asserts that every changed old member equals *old body + appended text*. It would refuse, and
it is right to. `tools/register_counts.py --write` produces the corrected member; carrying it into
the store of record needs the main-bundle route that does not yet exist.

## The W entry, in `close.py`'s form

`close.py` requires the text to begin `### W-` and end with a blank line. This is that text.

### W-190 — chat 153 (Claude Code, repository session, not a Method chat) — the cypher analysis built as an instrument and Λ audited against it; instruments tools/cypher.py and tools/audit_lambda.py; NO BUILD CHANGE

- **No gate.** A repository session, as RUL-152's was: the §0 gate was not run, no bundle was fetched, nothing was extracted, and no golden was banked. `method/verify.py` was the standing check and passes — 343 members, both bundles recovered. The read was from `method/members/` directly and from the `drive/` mirror's CORPUS copies.
- **Segment A — the instrument.** §33's cypher analysis built as a program. Seven languages, each carrying its status and its attribution: **order** PINNED (ℛ §32.4.1, matching the seated `rclose.py`), **statistics** PINNED (max-entropy on the order-k marginals, register 1174), **geometry**, **algebra** and **information** ADOPTED by M's ruling in this session (the two-variable polytope after Carathéodory 1911; the sublattice closure after Birkhoff; the join-irreducible closure after Birkhoff 1937), **analysis** DECLARED, **documentary** silent by construction. Three states became four: a resource cap reports REFUSED and never SILENT, because a silence is a finding and a compute limit is not. Rosters ship as data and `--roster` is required — docket 20x-04 / 20x-09 stays open — and `--pairs` **measures** the operator-bearing set rather than taking it from a roster. Measured on Λ the five are order, algebra, geometry, information and statistics, C(5,2) = 10 with all ten agreeing: register 1173's count with a different membership, statistics in and analysis out, the two special rows being analysis and documentary for two unrelated reasons.
- **Segment A — the audit.** 61 recorded claims about Λ re-derived: **59 reproduce, 2 do not**, and four findings are staged above (cyA-01 … cyA-04, code unassigned). Reproduced among others: 976 cells in a 6,912 box with E = 0 in all five languages and all ten pairs agreeing; zero join and zero meet failures over all 475,800 pairs; the rank sequence entire and log-concave at every interior rank; F(1) = 976, F(−1) = 2; the largest antichain 122 by a Dilworth partition computed as a bipartite matching, and 976 = 8 × 122; seventeen join-irreducibles; **1,113,045,672 maximal chains**; 115,162 comparable intervals of which 31,604 are boxes; 116,138 meet-join boxes; binding rates 30.0 / 28.0 / 1.9; the 319-cell projection with Σ(k+1) = 976; A_q and B_q; the triangle at 911 and 280 / 240 / 40; the tower at 1,654, 1,561 and 2,535; Λ₉'s 41,682 composable pairs and 842,206 associative triples with no failure; Λ₁₀'s 485 non-composing cells, every one at g = 0.
- **Six items book right / instrument wrong, self-caught.** The comparable-interval and box counts (the 976 singletons counted twice, 116,138 − 976 = 115,162 exactly); the binding rates (wrong population and wrong criterion — the book states both, y_u > φ(x_v) over the 475,800 pairs); the join-irreducibles (the bottom element counted, 18 − 1 = 17, Birkhoff excludes it); Λ₉′ (the tighter bound taken alone instead of conjoined — the 93 cut cells came out at (f=0, g=2, 2S′=2) as recorded); and the Register's own entry count (1,628 single headings against a printed 1,635 — the 7 grouped headings of docket 30 close it exactly). **In every case the offset was exact and nameable — 976, 976, 1, 93, 7 — which is the closed index defending itself, and is why a FAIL is read twice before it is believed.**
- **Not done, by design.** Λ_spectra's superseded state is not reconstructible (its cells are not in the tree and the index now closes at E = 0), so register 1177's geometry percentages cannot be checked at all. The violation index is not built — its cells are printed nowhere, confirmed rather than worked around, and its printed arity-3 constraint taken as a definition gives 18,792 cells at E = 648 against the recorded 2,370 at E = 30. Λ₁₁ to Λ₁₃ are not built: not for want of compute, which the pruned search now reaches, but because 2J_c ≤ φ̂(k) and 2K ≤ 2J_c + 2f_max are envelopes the volumes do not state to the precision a program needs. Λ₃ is not runnable — its coordinates are continuous and its E = 0 rests on a certificate, not on enumeration. The 3-D calendar's weekday mapping is not stated. Λ's own seed, recorded at 7, is not computed: the problem is NP-hard and a greedy search did not find a 7-cell generator, which is a limit of the search and not evidence against the 7.
- **Segment B — no close.** No BUILD was produced, no member was added or changed, no bundle was touched, and no Register entry was seated. The four entries and this text are staged in `method/REGISTER-QUEUE-APPEND-cypher-audit.md` for M's ruling. Nothing was put to M beyond the three questions this session asked and he answered: the operator scope, the placement, and the adoption of the three reconstructed operators.

---

## What would seat it

Nothing below has been run.

```sh
python3 method/members/close.py \
  --old  <BUILD180 compendia> \
  --new  <BUILD181 compendia> \
  --w    W-190.md \
  --append DEFERRED.md DEF-153.md \
  --append RULINGS-R2.md RUL-153.md \
  --members tools/cypher.py tools/audit_lambda.py docs/CYPHER.md docs/AUDIT-LAMBDA.md
```

Three things are M's to rule before it runs:

1. **The family code** — `cyA` is proposed, not assigned.
2. **Whether the instruments are seated as members at all.** They were built in `tools/` on M's
   ruling in this session ("tools/ now, seat it later via close.py"); seating them changes both
   bundle md5s and makes them store-of-record.
3. **Done.** The compendia close ran: BUILD180 → BUILD181, six members seated with W-190 and
   DEF-153, `--main` the BUILD91 path, and the MANIFEST rows current again.
