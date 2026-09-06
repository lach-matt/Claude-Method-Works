
## Chat 97 — deferred out of the Chapter 23 third read (main L6434–L6548)

- **A banked golden may not read a bundle** (gate fault, chat 96's r2-ch14l / r2-ch14m). Both name
  `The_Method_1_6_BUILD124_compendia_papers_audits.md` and died at chat 97's gate. Two reasons, and
  the second is the one that matters: the bundle's name carries a build number that changes every
  chat, **and the bundle comes to contain the instrument's own banked output**, so a whole-bundle
  census is self-poisoning and cannot reproduce even under a correct path. R3 and every future
  instrument read the six volume **members** by name. The two chat-96 goldens still reproduce
  byte-identically when BUILD124 is supplied, so nothing they recorded is in doubt; but they are
  un-rerunnable without a retired build, which is a reason to keep BUILD124 on Drive until R3 has
  either re-banked them against members or accepted them as historical.
- **The Register has no entry for the correction two main-volume sites cite** (14n-A3). L6455 *the
  correction is recorded at 96–98* and L6484 *withdrawn at correction 97*. Registers 96, 97, 98 are
  each the single line *SUPERSEDED (Λ₈ successor development); see register 313*, and 313 is about
  iteration in Λ₉. MEASURED across the Register: "V = 2" 0 sites, "Figure 23.3" 0 sites, "matched
  order" 0 sites. Append-only, so this is a **missing entry**, not a wrong one — the same shape as
  the §18.4.1 item, and it joins that item in the set written when the chat-67 hold lifts. R3 must
  decide whether the missing entry is authored to what §23.10.2 already says or whether the two
  citations are dropped; note the caption citation is also a Ruling 45 item (14n-A12), so the two
  repairs interact.
- **The pointer-off-by-one class now has three members in one chapter.** 14n-A1 (§23.13 cited for
  what §23.14 L6585 carries), 14n-A2 (§23.11 cited twice for what §23.15 carries in four places),
  14n-A7 (§25.5 cited for a figure at L6958, §25.4, four lines above the named section). Chat 95's
  14k-01 and chat 96's 14m-01 are the same class. R3 should sweep **every §-pointer in the six
  volumes against the claim rather than the heading**, and the sweep is cheap now that
  `enclosing` resolves a line to its section: the test is *find the claim's sites, resolve each to
  its section, compare with the section cited*. This is the single largest recurring class of the
  phase and it has never yet been swept as a class.
- **The ν_V docket, half closed** (chat 95's 14k-01). All fifteen main-volume ν_V sites are now
  resolved to their sections and are in READ-ch14n B/A2; §23.11 carries ν_V, ceiling, granularity,
  quotation, curvature and resolve zero times each. **What remains for chat 98:** read §23.15 as
  its own section, test L6270's *Al I at n = 51 and Ga I at n = 53* against §23.15's failing cells
  (chat 96 measured Al I nf as n = 48, 51, 53, 54 with no ν_V printed for Ga I anywhere), and close
  the Ga I attribution (14k-02). Note §23.11.1 L6538 **does** name Ga I — 15 members, one refusal,
  a bifurcation — so the Ga I question is not "does §23.11 mention Ga I" but "does any section give
  Ga I a ν_V".
- **The classifier's vocabulary does not survive its own first application** (14n-A8, 14n-A9). The
  §23.11 table offers five verdicts from four refusal patterns; the heading says four verdicts and
  the prose says four patterns, so the heading is the wrong one of the two. Then §23.11.1 returns
  *repeated structure*, which is none of the five and occurs once in six volumes. R3 repairs the
  heading with one word and must then decide whether Li I's six irregular refusals are the table's
  *chaotic* row or whether the table owes a sixth row — a subject-matter decision that the six
  refusals' spacing settles, not a preference.
- **The unprinted-input class reaches nine** (14n-A13). §23.10.3's displacement row reproduces
  exactly as *the distance from the value to the nearer bracket end* — 0.128732 → 0.129 and
  4.2675 × 10⁻⁶ → 4.3 × 10⁻⁶ — and the definition is nowhere printed. Unlike chat 96's §23.9.3
  member, this one reproduces once the definition is guessed, so it is the cosmetic repair of the
  two the class now contains. The census R3 owes is unchanged: every site in the six volumes that
  prints a derived figure beside its inputs.
- **Two unsourced counts in one sentence** (14n-A6, 14n-A7). L6517's *619 refusals* matches no entry
  and no sum in the table above it (19 + 101 + 145 = 265), and its *1,061 order-1 bounds* sits
  against the same table's 499 admitted at order 1. R3 cannot repair either without recomputing the
  collection at matched order; this is the first item of the phase that needs a **recomputation of
  the collection**, not a correction of a printed figure, and it should be sized before it is
  scheduled.
- **The "held" column** (14n-A5) repeats "admitted" in all three rows of L6507–L6511. Either the
  unresolved count was never computed or it was lost in production; the Prints & Proofs original
  settles which, and under the chat-95 ruling that folder is read before the question is asked.
  Chat 98 or R3 should read it there in the same call that answers anything else owed from
  Chapter 23.
- **Truncation printed as equality, third and fourth sites** (14n-A10, extending chat 96's 14l-02
  and 14l-03). L6497 prints *V = 4ν/3*, which is the asymptote of the book's own exact
  V = 4r³/(3r²−1) — 53.344447 against 53.333333 at ν = 40. The sweep chat 96 set — every display
  equation whose own table disagrees with it — should now also catch every site printing 4ν/3.
- **Method notes for chat 98, from this chat's eleven faults.** (1) **Re-read every verdict against
  the numbers the instrument printed below it**, not only above it — 14n-05 asserted a figure
  unreproducible two lines above its own reproduction. (2) **A sign convention is not a magnitude**:
  an error term carried as −0.128598 was reported as reproducing 0.129 and poisoned two ratios
  downstream. (3) **A token count cannot settle a pointer** — resolve to the section's own claim
  lines and print them. (4) `r2lib.heading_line` requires a trailing space after the number, so
  bare `### 96` Register headings return None; locate Register entries with an explicit
  `^#{1,4}\s*N\s*$` match until r2lib is lifted again. (5) A truncated print is a lost measurement:
  two citing sites cut at 150 characters hid the evidence they carried.
