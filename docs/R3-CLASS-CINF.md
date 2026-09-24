# R3-CLASS-CINF.md — the c → ∞ twin class: register 1706's eleven, sites, both texts, the entry

**A specification, in the form of `R3-CLASS-WL.md`, and an instrument that executes it as a dry run.**
The author ruled on 2026-09-24 that the finding of `docs/LOWDIN-RECOVERED.md` be repaired. Everything
this repository speaks for itself is repaired in the same commit (the site, the docs, the pins). The
store is repaired by the corpus's own mechanic and not by hand — *a Register entry is never edited;
the repair is a new appended entry citing the superseded one; volume sites are repaired in place
under a guarded build with that entry* (`DEFERRED.md`, `docs/R3-REPAIR-PLAN.md`) — and this file is
what that repair is, site by site, so the wording can be approved or edited once before it is
applied. **Nothing under `method/` is changed by this commit.** `tools/r3_cinf.py` applies every
substitution below in memory, recovers each old member's md5 and both old bundles' md5 by reverse
guard, and prints the new members' and bundles' md5s (`docs/R3-CLASS-CINF.dryrun.txt`); with
`--write DIR` it writes the new members, both new bundles and a `MEMBER-INDEX.tsv` for the new tree
outside `method/`, for the close to seat.

## The finding, MEASURED (`lowdin/chain/`, the record's own instrument recovered and run)

- Register **1706** and `THE-LOWDIN-SOLUTION-2.md` §VIII state that the identical walk at c → ∞
  disagrees with Λ_chain at **Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf**, every one an error of the
  equation-without-light against nature.
- The paper's own session computed that list as `Λ_chain` against `rt/cinf.jsonl` — the table the
  project's fault record **F59.3** had voided six sessions earlier: its driver bound c where the field
  never reads it, so it walked at **c = 137.035999 in restart mode** (each step from the observed
  configuration). Both tables re-derive here (`LAMBDA-CHAIN.jsonl`, `LAMBDA-CINF-SEALED.jsonl`) and
  the eleven reproduce from them; at **eight** of the eleven (Mn, Zn, Ag, Cd, Lu, Hg, Lr, Rf) the
  restart's entrant is the observed one and the chain's is not.
- The chain re-run with the constant removed by the record's own remedy (`LAMBDA-CINF-CHAIN.jsonl`)
  differs from the chain at c = 137.035999 at **Th** (6d → 5f, away from the observed 6d), **Rf**
  (5f → 6d, the observed channel; the c = 137.035999 chain departs) and **Z = 120** (8s → 7d,
  unwitnessed), and at no other row. Silver and mercury do not move.
- The record's own scorer `nlcfg.py show` (`SCORE.tsv`): **96 of 107** steps at either setting, the
  step failures swapping Rf for Th; configurations 73 and 76 of 107. Restart rows, same mode at both
  settings, differ at Nd, Pm, Sm, Th, Lr.
- G0c is satisfied the only way it can be: the withdrawal rests on the original instrument, recovered
  and byte-checked against the sessions' sealed digests, not on a reconstruction.

## The Register's standing (both texts)

- **1706** (L6365): *ELEVEN ELEMENTS SEPARATE THE TABLE FROM ITS NON-RELATIVISTIC COUNTERFACTUAL … The
  identical walk at c → ∞ (Λ_cinf, 107 rows) disagrees with Λ_chain at Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu,
  Hg, Lr, Rf … The relativistic walk scores 107/107, so all eleven are errors of the
  equation-without-light against nature; the thorium competition inverts besides, though its entrant
  survives by path … Quarantine standing: Λ_cinf is contrast, never data.* — **stands as written; not
  edited.**
- **1701, 1703, 1712** are cited by the new entry and not touched.

## The volume sites (as printed → as proposed)

Line numbers are the seated members' (BUILD90 main, BUILD180 compendia), asserted by content in the
instrument. `N` is the entry number (below).

| # | site | as printed | as proposed |
|---|---|---|---|
| M1 | main §35 L9772–L9775 | *And the table is relativistic, visibly. The identical walk at c → ∞ misplaces eleven elements — Mn … Rf. Silver and mercury are misfiled by the non-relativistic equation. The wall chart is not a solution of the Schrödinger equation without light in it.* | *And the table is relativistic at thorium. The identical walk at c → ∞ moves its entrant at Th (6d to 5f, away from nature), at Rf (5f to 6d, the observed channel) and at Z = 120 (8s to 7d), and nowhere else. The eleven this chapter first printed — Mn … Rf — were the chain measured against a table that had run at c = 137.035999 with every step restarted from the observed configuration, and are withdrawn (register N). The actinide opening of the wall chart is not a solution of the Schrödinger equation without light in it; the rest of the chart is indifferent to it.* |
| M2 | main §35.5 L9866 | *the c → ∞ twin walk, eleven elements apart* | *the c → ∞ twin walk, three rows apart — Th, Rf, Z = 120 (register N)* |
| M3 | main Appendix L10805, row LS.twin | *measured · exhaustive · none found* | *re-measured at c → ∞: Th, Rf, Z = 120 (N)* |
| M4 | main L7373; Register L6, L65 | *1,635 entries, 1 to 1792* (extent lines) | driven to the fixed point that includes the new entry (register 1781's pattern) |
| P1 | paper abstract L13 | *and shows that the observed table is irreducibly relativistic: with the speed of light taken to infinity, the same construction misplaces eleven elements, silver and mercury among them.* | *and shows where the observed table is relativistic: with the speed of light taken to infinity, the same construction moves its entrant at thorium, away from nature, at rutherfordium, toward it, and at Z = 120, and nowhere else.* |
| P2 | paper relativistic clause L45 | *The law is scalar-relativistic in an essential way: repeating the entire construction with c → ∞ changes the entrant channel at eleven elements, and inverts the underlying channel competition at thorium besides. The observed periodic table is not a non-relativistic object.* | *The law is scalar-relativistic at one measured row: repeating the entire construction with c → ∞ inverts the channel competition at thorium and the entrant with it, moves the entrant at rutherfordium to the observed channel, and moves the first unwitnessed entrant at Z = 120; at every other row the entrant is the same at both settings.* |
| P3 | paper §VIII L156 | the paragraph *The second boundary statement is the deeper one …* | rewritten in full: the comparison as made, what it measured, the re-run's three rows with nature's side at each, the scorer's 96 of 107 at either setting, the clause resting on thorium; the text is in `tools/r3_cinf.py` |
| P4 | paper Figure 5 caption L160 | *The relativistic table against its c → ∞ counterfactual, element by element. Eleven disagreements, every one an error against nature.* | *The relativistic table against the table the project sealed as its c → ∞ counterfactual, element by element — withdrawn: the second table ran at c = 137.035999 in restart mode, so its eleven disagreements are the chain against a restart at one c, not against the constant. At a genuine c → ∞ the disagreements are thorium, rutherfordium and Z = 120.* |
| C1 | Mathematical Compendium L3216, *The twin operator, c → ∞* | *… disagrees with the c = 137.035999 operator at eleven elements — Mn … Rf — every disagreement an error against nature, since the relativistic operator scores 107/107* | *… disagrees with the c = 137.035999 operator at Th (6d → 5f, away from the observed 6d), Rf (5f → 6d, the observed channel) and Z = 120 (8s → 7d, unwitnessed), and nowhere else; the eleven first printed here (Mn … Rf) were the c = 137.035999 operator against a restart walk at the same c, and are withdrawn (register N)* |
| C2 | Physics Compendium L227, Λ_cinf *What it indexes* | *The identical walk with the one constant removed. 107 rows.* | *… removed, 119 rows. The 107-row table first sealed under this name had run at c = 137.035999 with every step restarted from the observed configuration, and is withdrawn (register N).* |
| C3 | Physics Compendium L235–L238, *Must be measured* | *eleven entrants differ from Λ_chain (Mn … Rf), and every difference is an error against nature, since the relativistic walk scores 107/107 (register 1706)* | *three entrants differ from Λ_chain — Th (6d → 5f, against nature), Rf (5f → 6d, the observed channel) and Z = 120 (8s → 7d) — and no other; register 1706's eleven were measured against the withdrawn table (register N)* |
| C4 | Physics Compendium L240–L241, *What physics does* | *It states that the observed periodic table is not a solution of the non-relativistic equation.* | *It states that the actinide opening of the observed periodic table is not a solution of the non-relativistic equation, and that the rest of the table is indifferent to c.* |
| C5 | Physics Compendium L603, *Where it fails* (c) | *… disagrees with Λ_chain at eleven elements, each an error against nature (register 1706)* | *… disagrees with Λ_chain at thorium, against nature, at rutherfordium, toward it, and at Z = 120, and nowhere else (register N)* |
| I1 | Index of Indices L1882, the table row | *that the periodic table is not a solution of the non-relativistic equation* | *that the periodic table's actinide opening is not a solution of the non-relativistic equation, and the rest of it is indifferent to c* |
| I2 | Index of Indices L1933, *What it holds* | *The identical 107-row walk at c → ∞.* | *The identical walk at c → ∞, 119 rows; the 107-row table first held here had run at c = 137.035999 in restart mode and is withdrawn (register N).* |
| I3 | Index of Indices L1939–L1942, *Role for Λ* | *eleven of its entrants differ from Λ_chain's, and all eleven are wrong against nature. It exists to state that Λ's subject is relativistic …* | *three of its entrants differ from Λ_chain's — thorium, wrong against nature; rutherfordium, the observed channel; Z = 120, unwitnessed. It exists to state where Λ's subject is relativistic …* |

Eighteen substitutions over six members, every one count-asserted. After them, *Mn, Zn, Ag, Cd, Nd,
Pm, Sm, Lu, Hg, Lr, Rf* occurs at four sites and all four name the list as withdrawn (§35, the
Mathematical Compendium, register 1706 as it stands, and the new entry); *eleven elements apart* at
none; `register N` at eight.

## The Register entry (draft; M's wording governs)

> **### N**
>
> **REGISTER 1706'S ELEVEN WERE MEASURED AGAINST THE TABLE THE PROJECT HAD ALREADY VOIDED; AT A GENUINE
> c → ∞ THE WALK'S ENTRANT MOVES AT THORIUM, RUTHERFORDIUM AND Z = 120, AND NOWHERE ELSE.** *Entry 1706
> states that the identical walk at c → ∞ (Λ_cinf, 107 rows) disagrees with Λ_chain at Mn, Zn, Ag, Cd,
> Nd, Pm, Sm, Lu, Hg, Lr, Rf, every one an error of the equation-without-light against nature. The
> instrument that walked Λ_chain, recovered whole from the project's own conversations and run again,
> reproduces every sealed step it printed; the table 1706 compared against reproduces too, and it is
> the one the project's own fault record (F59.3) had voided six sessions before the paper was written:
> its driver bound c where the field never reads it, so it walked at c = 137.035999 in restart mode,
> each step from the observed configuration. The eleven are therefore the chain's memory against a
> memoryless restart at one and the same c, and at eight of them — Mn, Zn, Ag, Cd, Lu, Hg, Lr, Rf — it
> is the restart's entrant that nature holds and the chain's that departs. The walk re-run with the
> constant removed, by the project's own remedy for that fault, differs from the walk at
> c = 137.035999 at Th (6d → 5f, away from the observed 6d), Rf (5f → 6d, the observed channel) and
> Z = 120 (8s → 7d, unwitnessed) — and at no other row; silver and mercury do not move. The project's
> own scorer returns 96 of 107 steps at either setting, the step failures swapping Rf for Th, and 73
> and 76 of 107 configurations. What 1706 stated survives at one witnessed element: the table is
> relativistic at thorium, where the equation without light files the entrant under 5f and nature has
> 6d; at rutherfordium it is the relativistic chain that departs from nature, and every other measured
> row is indifferent to c. The quarantine standing is kept and its object renamed: the sealed Λ_cinf is
> a restart walk at c = 137.035999 — contrast, never data — and the c → ∞ walk is the re-run. Corrected
> at the paper's abstract, relativistic clause, §VIII and Figure 5's caption, at §35's three sites, and
> at the twin entries of the Mathematical Compendium, the Physics Compendium and the Index of Indices;
> Figure 5 as printed drew the withdrawn comparison and stands captioned as such until it is redrawn
> from the re-run. Entry 1706 stands as written.* Registers 1701; 1703; 1706; 1712. (a correction.)

**The number.** `R3-CLASS-WL.md` (seated; HELD under RUL-128 until the Chapter 34 re-take) drafts
**1793–1794** for the withdrawn-law class. Numbers are assigned at application: this class takes
**1793** if it is applied first and **1795** if the withdrawn-law class goes first. The instrument takes
`--entry N`, asserts that N has no entry in the Register and no EXCISED marker in either bundle, and
drives the extent lines (main L7373, Register L6 and L65) and the kinds table (`kinds.py --write`,
corrections 149 → 150) to the fixed point that includes the entry.

## Figure 5

`figures/FIG6relativisticvsnonrelativistic.png` (extracted, md5 `7a328342…`) draws the withdrawn
comparison. Its generator is in no file here — not in `recovered/`, not in `extracted/` — so a redraw
from `LAMBDA-CHAIN.jsonl` against `LAMBDA-CINF-CHAIN.jsonl` is a new figure, not a regeneration; the
figure bundles are Drive artefacts. **Proposed:** keep the figure in place, captioned as withdrawn (P4),
until the author decides whether it is redrawn; the site captions it the same way now.

## What this class does not propose

- **Register 1706 itself, and 1701, 1703, 1712** — never edited.
- **`r2-scf.out`, `READ-ch17a.md`, `r2-ch17d.py`, `CENSUS-CLOSURES-scf.tsv`, `DEFECT-CENSUS.tsv`** —
  records of readings taken and goldens banked at those readings; a golden is re-banked by its
  instrument at the close that changes its input, not edited here. `r2-scf.out` still prints "the
  eleven in the observed table" and grades the family UNREPRODUCIBLE with a stated budget; both are
  true of the record as it was read.
- **The paper's 107 of 107** and register 1701's ordering-law score — a different scoring from the
  scorer's step count (`ok`, entrant = observed gain, 96 of 107), and not this class's question.
- **`recovered/`, `extracted/`, `lowdin/`** — generated trees are regenerated.

## Build procedure (both bundles move; the first main-volume change since chat 62)

1. Approve or edit the wording above, in this file and in `tools/r3_cinf.py`'s `texts()` together.
2. `python3 tools/r3_cinf.py --entry N` — the dry run; read `docs/R3-CLASS-CINF.dryrun.txt` for the
   figures it must reproduce (every reverse guard True; BUILD91 and BUILD181 md5s printed).
3. Write the W-entry for the close (draft below) to a file ending in a blank line, then
   `python3 tools/r3_cinf.py --entry N --write DIR --w W-190.md`. The tree under `DIR` carries the six
   changed members, `WORKING-REGISTER.md` grown by the W text, `MANIFEST.tsv` regenerated as `close.py`
   regenerates it, both new bundles and a `MEMBER-INDEX.tsv`.
4. Seat: copy the members over `method/members/`, the bundles beside the old ones, `MEMBER-INDEX.tsv`
   over `method/MEMBER-INDEX.tsv`; retire the old bundles as the close does; run
   `python3 method/verify.py` (343 members, both bundles recovered) and `python3 tools/docfigures.py`.
   Update `method/README.md`'s and `method/CLAUDE.md`'s bundle lines (bytes, md5, lines, "Register 1 to
   N"), which are project instructions and not members.
5. Re-run `python3 tools/webindex.py` — the site renders the paper from the seated member and measures
   its md5 at build, so the Papers page follows the store; `relativistic.repair` then agrees with the
   paper's own text and the "superseded" marks are still true of the printed edition.
6. The goldens whose inputs moved (`r2-scf.out`, the DEFECT-CENSUS rows for the twin entries) are
   re-banked by their own instruments at the next gated close, as W-168 left the WL class's.

**Draft W-entry (the audit log; the Register carries the subject matter above):**

> ### W-190 — repository session (Cowork), 2026-09-24 — R3 class CINF: register 1706's eleven corrected by entry N; BUILD90 → BUILD91, BUILD180 → BUILD181
>
> **Finding.** `docs/LOWDIN-RECOVERED.md`: the paper session computed 1706's eleven as Λ_chain against
> `rt/cinf.jsonl`, voided at F59.3 as a restart walk at c = 137.035999; re-run with the constant removed
> by the record's own instrument, recovered from the export and byte-checked against its sealed digests,
> the walk differs at Th, Rf and Z = 120 only. **Ruling (M, 2026-09-24):** repaired, not recorded only.
> **Applied:** 18 count-asserted substitutions over six members (§35 ×3 and the extent line; the paper's
> abstract, clause, §VIII, Figure 5 caption; MC twin entry; PC Λ_cinf ×4; IoI Λ_cinf ×3), entry N appended
> in the Register's form citing 1701, 1703, 1706, 1712; kinds table recounted; MANIFEST.tsv regenerated;
> member and bundle reverse guards recovered 4aef772b…, 79aaf239…, 4a06e893…, 99a616ec…, 5a964610…,
> 27d387ef… and the bundles' 49065309… and ea5becc4…. **Not done:** Figure 5 redrawn (generator absent);
> `r2-scf.out` and the DEFECT-CENSUS rows re-banked (next gated close); 1793–1794 of the WL class
> unaffected. Instrument `tools/r3_cinf.py`, dry run banked at `docs/R3-CLASS-CINF.dryrun.txt`.
