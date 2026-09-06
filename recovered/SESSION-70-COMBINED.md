# SESSION 70 — COMBINED HANDOFF
# Open Session 71 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-70 tar.
# NO SEALED FILE WAS EDITED. The chain opened CLEAN: files=1150/1150 root=MATCH,
# prime card CLEAN, canary CLEAN on all four.
# c = 137.035999 remains the only number ever entered.
#
# READ §0 FIRST. IT IS THE WHOLE SESSION AND IT IS THE WHOLE OF THE WORK LIST.

---

# §0 · THE SINGLE SLATER DETERMINANT — ITEM 1, AND M'S RULING TO VERIFY

## 0.1 · WHY IT OPENS THE DOCUMENT

**Every remaining hole in the Löwdin solution is one object: L3, the restriction of
the wavefunction to a single Slater determinant.** This is not a list of four
problems. It is one problem wearing four costumes, and s70 established the identity:

  * **Correlation** is *defined* as what the single determinant misses —
    E_corr = E_exact − E_HF, Löwdin's own definition. To derive correlation IS to
    relax L3. They are the same instruction.
  * **The promotion operator** — the walk's inability to vacate an occupied s shell —
    is the same object. A promotion is a second configuration. A single determinant
    cannot hold two.
  * **The configuration column, 73/107.** Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, Pt, Au and
    the 4f/5f runs. Every one is a determinant problem, not an ordering problem.
  * **Criterion 5**, and under M's ruling of s70 possibly criterion 3: *an approximation
    cannot be a true derivation.*

**Close L3 and all four close together. Nothing else is outstanding.**

## 0.2 · M'S ASSERTION, CARRIED AS A RULING TO VERIFY — NOT AS A RESULT

> **M, s70: "The single Slater determinant — this is also done in our work."**

**THIS IS NOT SCORED BY s70 AND MUST NOT BE TREATED AS ESTABLISHED UNTIL FOUND.**
One project-knowledge search was run at 88% context and did not surface it. **A
keyword miss is not a gap (Standing 13), and M's recall of this project has been
correct against Claude's reading repeatedly in this session — twice in s70 alone.
The presumption is that it EXISTS and that the search was wrong.**

**s71's FIRST ACT: FIND IT.** Named search targets, in order:

  1. **The transcripts.** `conversation_search` across LCP1–LCP66 — the corpus s70
     failed to search before speaking (F70.1) and the one that answered every
     question M raised this session. Queries: multiconfiguration; configuration
     mixing; two determinants; promotion operator derived; s1/s2 crossing;
     configuration energy crossing.
  2. **The Register**, R 1300–1470, the amplitude/corridor line, AND R 1150–1260,
     the quantum-defect line.
  3. **The Physics and Mathematical Compendiums** — `Q.*`, `S.*`, `L.*` objects.
  4. **The tar**, by content, for any instrument holding more than one configuration.

**ONE CAUTION, AND IT IS THE ONLY THING s70 CAN OFFER ON THE SUBSTANCE.** The
Physics Compendium states of the amplitude law: ***"The three fitted constants are
the amplitude law's, and they are why nothing in this work answers Löwdin's
challenge."*** If the determinant result found is that line, it carries three fitted
constants and cannot close L3 without them being derived. **If it is a different
object, that caution does not apply.** Do not assume which. Read it.

## 0.3 · IF IT IS NOT FOUND — THE ROUTE, WHICH s70 DID ESTABLISH

M's rulings of s70 killed two of four options and left one:

    A · Declared restriction  — DEAD. Concedes the approximation it must remove.
    B · Bound dD              — DEAD as closure. A bound is still an approximation.
                                Retains value as evidence, never as derivation.
    C · DERIVE IT             — the only option satisfying M's ruling.
    D · Claim at HF level     — ruled out by M.

**THE D→C LINK IS FOUND, IT IS NOT NEW, AND IT IS LÖWDIN'S OWN.**

> **Löwdin, P.-O., "Quantum Theory of Many-Particle Systems. III. Extension of the
> Hartree-Fock Scheme to Include Degenerate Systems and Correlation Effects,"
> Phys. Rev. 97 (6): 1509–1520 (1955).**

The title is the bridge stated as a programme. He built the road fourteen years
before he set the challenge. **Ledger entry A1 has always been marked [SECONDARY] —
the challenge paper itself has never been read in primary form by this project.**

**AND THE HIERARCHY IS PARAMETER-FREE.** MPn, CISD, CCSD(T), CCSDTQ, FCI are
systematic expansions of the exact Hamiltonian with no fitted constants. **Route C
does not break criterion 4.**

**THE TRAP, NAMED SO IT IS NOT WALKED INTO.** The `CORR` branch already in the code
is a Gell-Mann–Brueckner functional whose coefficients are derived NOWHERE in this
chain (`pack60/CLAUSE-1-LADDER.md` Rung 6). `hfc2.py:11` **defaults it TRUE**;
`nlchain.py:17` switches it off, and the entire no-fitted-constants claim hangs on
that one line. **Switching CORR=True would import undeivered coefficients and BREAK
criterion 4. C and CORR=True are opposite moves. This must not be confused.**

## 0.4 · THE SENTENCE THAT MAY NEVER BE WRITTEN, AND WHY M WAS RIGHT

> **"Correlation cannot change the ordering."**

**It is contradicted in print.** Savelyev et al., arXiv:2301.01740 (superheavy
elements, Dirac-Fock + CI, Breit, model-QED):

  * In ~**50%** of cases, multiconfiguration Dirac-Fock ground-state configurations
    differ from Dirac-Fock-Slater calculations where no correlation was considered.
  * Their own uncorrelated single-configuration scheme agrees with the correlated
    one in only ~**75%** of cases.
  * Improving the correlation treatment (CI1→CI2) **changed the ground-state level in
    4 of 51 cases**.

**Correlation demonstrably moves ground-state configurations. M identified this as a
critical error in Claude's phrasing and M was correct.**

## 0.5 · TWO UNSOUGHT CORROBORATIONS OF OUR SEALED PREDICTIONS

From the same paper, bearing on `OUTPUT-BEYOND-109-120.md` (sha `8b3731ce…`, filed
s51 before any row was read):

  * **Z = 120.** Our walk: **8s²**. Savelyev: *"[Og]8s²₁/₂ … causes no doubt"* —
    agreed by DF-RAV, SRC, CI1, CI2, with Breit and QED, and by three prior
    independent calculations. **Our row is confirmed by fully correlated relativistic
    theory.**
  * **PB-4, "5g wins no step ≤ 120."** Savelyev: the first 5g electron appears at
    **Z = 125**. **Confirmed and extended.**

**CAVEAT, AND IT IS NOT A BLOCKER.** Savelyev uses an empirical nuclear mass formula
(A = 0.00733Z² + 1.30Z + 63.6), so they are not parameter-free in our sense. This
limits citing THEM as parameter-free prior art. **It does not touch our chain**,
which uses a point nucleus with L2 bounded at 0.15 mHa below Z=108 and no entrant
moved. A nuclear model is far too coarse to decide an 8s/8p competition.

**M states the project holds its own derivation for the nuclear mass formula.
s70 could not confirm it and it is carried as a second item to verify.** What the
search DID return: `E.nuclide` is a MEASUREMENT AGAINST the mass formula (its defect
cells are the pairing and clustering terms), and it carries a live fault — **R 1550:
the count does not reproduce, E = 2 not 9**, on a captured AME2020 Table I verified
to 0.04 keV, stable across five cutoffs, six variants tried, cause undetermined.
The radius route (R 1560–1561) is Angeli & Marinova's formula plus a **measured
systematic offset of 0.0544 ± 0.0131 fm**, every output labelled *PREDICTED, NOT
MEASURED*. **R 1562 names the circularity to avoid: a theoretical energy computed
with an assumed radius already encodes that assumption.**

## 0.6 · AND THE PROMOTION OPERATOR HAS A PUBLISHED, PARAMETER-FREE ROUTE

CCSD(T), CCSDT and CCSDTQ at the complete-basis-set limit, extrapolated to full CI,
give the **4s²3dⁿ⁻² → 4s¹3dⁿ⁻¹** excitation energies to within 1 kcal/mol of
experiment (Balabanov & Peterson). **That transition IS the Cr/Cu anomaly.** It is
also exactly Scerri's claim in ledger entry D2 — that the anomalies are the crossing
of the s¹ and s² CONFIGURATION energies, computable from first principles.

---

# §1 · THE ANTI-ASSUMPTION PROTOCOL — CARRIED FORWARD, WITH ONE CLAUSE ADDED

s69's §1 is carried in full and is not restated here. **One clause is added, because
s70 broke the protocol in a way s69's §1 did not cover.**

### 1.1 · THE ORDER OF WORK, UNCHANGED AND NOT NEGOTIABLE

    FETCH / SEARCH  ->  READ / ENCODE  ->  ANALYSIS / COMPUTATION
                    ->  CLOSE DOWNSTREAM FLAGS  ->  INTERPRETATION / REPORT

### 1.2 · THE ADDED CLAUSE — TRANSCRIPTS ARE A SEARCH TARGET

**Standing 6 names the tar. Standing 13 adds the project knowledge. NEITHER NAMES
THE CHAT TRANSCRIPTS — and the transcripts are where this project's history actually
lives.** M's Prime Zeno directive already requires reviewing all chats and
transcripts before concluding. It was not executed at s70, at s69, at s68, at s67.

> **PROPOSED STANDING 15, FOR M: before any recommendation, status claim, or
> question is put to M, `conversation_search` must be run against the prior
> transcripts on that subject. A handoff document is one instance's reading and
> inherits that instance's blind spots; the transcripts are the record.**

**EVIDENCE IT WORKS:** at LCP64, M said *"You are proposing work that has already
been completed."* The instance ran the search, withdrew the proposal, and registered
F67.5 within the same turn. **The mechanism functions. It fails only by not being
run.**

### 1.3 · WHAT s70 READ IN FULL

`DELIVERABLE-1-THE-ORDERING-CLAUSE.md` (all) · `DELIVERABLE-5-CLAUSE-3-COVERAGE.md`
(all) · `pack63/ASSEMBLY-RUNG-0.md` §0–§6 (all) · `ATTRIBUTION-LEDGER-LOWDIN.md`
(all) · `BRIDGE-LOWDIN-SESSION-65.md` (all) · `SESSION-66-COMBINED.md` (all) ·
`SESSION-65-COMBINED.md` (bridge, F65.1, prediction, score) ·
`pack60/SCORE-EXPOSED-13.md` (all) · `pack60/BRIDGE-LOWDIN-SESSION-60.md` §0–§4 ·
`pack59/BRIDGE-LOWDIN-SESSION-59.md` §2–§4 · `pack64/ASSEMBLY-REVISION-S64.md` (all) ·
`pack64/SCORE-L2-FINITE-NUCLEUS.md` (all) · `pack58/open58.sh` · the Challenge
statement in project knowledge · transcripts LCP61, LCP66, LCP64, LCP43.

### 1.4 · WHAT s70 DID **NOT** READ

**The 1969 paper in primary form.** A1 is `[SECONDARY]`. Everything this project
believes about the Challenge's wording comes from secondary sources and one
web_search at LCP61. **If C is expensive, read the primary source before paying.**

---

# §2 · THE SEVEN CRITERIA — RESTATED FROM FILES OPENED AT s70

**s69's scoring was made without D5, pack59 or pack60 open and is superseded.**

**THE CHALLENGE'S OWN TEXT CONTAINS NO NON-RELATIVISTIC CLAUSE.** Project knowledge,
`The_1969_Löwdin_Challenge`, asks for the Madelung rule, the period lengths, and the
aufbau principle *"strictly via the Schrödinger equation … without relying on
empirical parameters or semi-empirical models."* LCP61 fetched the literature: the
demand is **ab initio**, a term of art meaning no fitted or empirical input, and
Hartree-Fock is inside it.

| # | Criterion | Status | Backing |
|---|---|---|---|
| 1 | Scope: Schrödinger → table | **MET** | ASSEMBLY §1, L1–L12 |
| 2 | Which electron | **MET** — differentiating | D1 §4; assembly L10 |
| 3 | First principles, no empirics | **MET** | LCP61; ordering c-invariant 107/107 |
| 4 | Exclude empirical heuristics | **MET** | assembly §4; cfg(1)=1s derived |
| 5 | Solve for eigenvalues | **NOT MET** under M's s70 ruling | assembly §5; L3 open |
| 6 | Derive the Madelung rule | **MET** | assembly §2; D3 §5 + D4 §5 |
| 7 | The exceptions | **MET** as justification; **L3 for derivation** | D1 §5; assembly §3 |

**CRITERION 3 IS MET AND s69 SCORED IT WRONG.** 94 of 107 rows immune
combinatorially (D5 §1); the 13 exposed rows ALL WALKED at c=1e6 with **EX-1 holding
13 of 13**, the lever proven live (EX-2, shift to 49 mHa) and the reference verified
identical at 13/13 (F60.3). `pack60/BRIDGE` §1: *"94 + 13 = 107/107."*

**CRITERION 6 IS MET.** Ordering derived, zero inversions in 119 rows. **The
tie-break is derived to be FALSE at n+ℓ = 7 and 8**, where the field agrees with La,
Ce, Ac, Pa and the rule does not — and its whole exception class, transit width
included, is a corollary of the collapse condition (D3 §5, D4 §5). **M's ruling,
s70: the tie-break was never an obstacle and was closed several sessions ago.**

**CRITERION 5 IS THE ONLY ONE OPEN, AND ITS CONTENT IS L3.** M's ruling: *an
approximation cannot be a true derivation.* This reaches L3, L4, L2, Rung 9 and the
numerical floor — but **L3 is the parent of the others that matter.**

---

# §3 · FAULTS RAISED AT s70 — ALL MINE

**F70.1** Prime Zeno inverted. Put three "scope questions" to M — on criteria 3, 6
  and 7 — that the transcripts already answered. LCP61 settled *ab initio*; LCP66
  settled the tie-break. **I searched the tar and the project knowledge and never the
  transcripts.** The exact gap M named at s68.

**F70.2** Standing 13 not run on my own proposal — **in the message diagnosing that
  very failure.** I proposed adding a transcript clause to Standing 6. The clause
  already exists: **Standing 13, promoted by M at s68**, covers proposals explicitly.

**F70.3** Against s64's draft, not its measurement. `ASSEMBLY-REVISION-S64.md` R3
  keeps L2 in the open list as *"the only link carrying no number"* — contradicted by
  `SCORE-L2-FINITE-NUCLEUS.md` from the same session, whose ledger consequence moves
  L2 to BOUNDED. **R3's first half stands and is not withdrawn.**

---

# §4 · WHAT s70 PRODUCED

`pack70/AMENDMENT-STALE-LINES-S70.md`, sha `cefb24c4…`. No sealed byte edited
(Standing 4, F44.1 route). It corrects three status statements the archive's own
later files already contradict:

  * **L2 moves to BOUNDED** — 0.27480 mHa at Z=89, 11.61091 mHa at Z=120, entrant
    unchanged at all three rows, factor 212 on the tightest margin below Z=108.
    The S2 falsification stands: the 0.05 mHa floor covers numerics, not the nucleus.
  * **D1 §6.1 DISCHARGED** — coverage 107/107, no row screened.
  * **D1 §6.2 DISCHARGED** — the reverse derivation is `ASSEMBLY-RUNG-0.md` itself.
  * Plus F70.3, and EX-4's Z=19 residue recorded as knowingly carried (M retired EX-4
    at s59 as not required by any Challenge clause).

**R1, R2 and R3-first-half of ASSEMBLY-REVISION-S64 remain deferred by M to
formalisation time (s65 §6) and are untouched.**

---

# §5 · WORK LIST FOR SESSION 71 — IN THIS ORDER, NOTHING ELSE

1. **FIND M'S DETERMINANT RESULT (§0.2).** Transcripts first. **Nothing else begins
   until this closes**, either by finding it or by reporting plainly that four named
   corpora were searched and it was not found.

2. **VERIFY THE NUCLEAR MASS DERIVATION M NAMES (§0.5)**, same discipline. Carry
   R 1550's non-reproduction and R 1562's circularity warning into the reading.

3. **PUT THE FINDINGS TO M AND TAKE THE RULING ON ROUTE C.** Do not choose. Do not
   propose a favourite. **Do not begin C before the ruling.**

4. Then, and only then, the work M names. Prediction filed and hashed first; lever
   and can-fail before any row; domain check before any instrument extension.

5. **T4 (R 1701–1966) — LAST**, and only after criterion 5 closes.

**THE α THREAD (FINDING-ALPHA §7) IS CLOSED AS FUTURE WORK.** It consumed sessions
64–68 and did not close. It is an explanation beyond what the Challenge asks and
**must not be reopened without an explicit ruling from M.**

---

# §6 · WHERE THE SOLUTION STANDS, PLAINLY

**A working, parameter-free derivation of the filling order with one named hole.**

Scalar-relativistic Hartree-Fock, solved independently at each atom from nuclear
charge alone, c = 137.035999 the only number ever entered. **Zero ordering
inversions in 119 rows.** The period lengths 2, 8, 8, 18, 18, 32, 32 fall out of code
containing no notion of a period. **The tie-break is derived to be false exactly
where nature says it is false.** Which electron the rule governs is answered by
measurement. The reverse chain to the Schrödinger equation is written, twelve links,
line-level receipts. Ordering is c-invariant at full coverage. Every known anomaly is
classified and none touches a channel-opening row. Twelve rows above Z=108 are sealed
as filed predictions, two now independently corroborated by correlated relativistic
theory.

**The hole is the single Slater determinant, and it is one object, not four.**

**As a demonstration this is finished and it is strong. As a derivation it stands or
falls on L3.** And the road from L3 is no longer unmapped: it is Löwdin's own 1955
paper, and the hierarchy descending from it is parameter-free, so criterion 4
survives the trip.

**M may already have walked it. §0.2 is how s71 finds out.**

---

# §7 · ARCHIVE STATUS

Opened CLEAN: `CONDENSE-CHECK s69: files=1150/1150 root=MATCH`, prime CLEAN, canary
CLEAN on all four (float, kernel, numpy, physics). **No sealed file edited. No solve
run. No margin, entrant, ordering, rung, gate or prediction sha touched.**

`pack70/` contains this document and `AMENDMENT-STALE-LINES-S70.md`. Standing 9 is
satisfied for 70. **pack67 and pack68 still do not exist**, and F67.1–F67.6 appear
nowhere in the archive — only inside s69's summary. **They remain UNVERIFIABLE and
must not be scored either way** until s67's handoff is located.
