# DEF-153P — the consolidation branch read against R3's queue. RECORDED, nothing repaired.

Read at M's instruction on 2026-09-04, at BUILD102 main / BUILD210 compendia: `claude/consolidate-project-artifacts-ov8es9`,
thirty-two commits past the state PR #11 merged, still moving (one commit landed during the read). It touches nothing
under `method/`; a merge into the R3 branch conflicts only in `CLAUDE.md`. Every claim below was re-measured on the
current members, not taken from the branch's documents, which were measured at BUILD180 lines.

## What it delivers that bears on R3

1. **`incoming/BUILD183/184/185-PARTS` and `incoming/DOCKET-152`** — the chat-151/152 working parts, reassembled from
   Drive's `.partNN` pieces. Its `DEF-152.md` and `DOCKET-152.md` are byte-identical (md5 2b8a23f18b996c3cda6288b4f1c34e62;
   diff empty) to the copies R3 decoded and executed at BUILD98–100 (DEF-153O). W-192/193/194, READ-28a2/28b2/32a and
   r2-28a2/28b2/32a are already seated. Nothing there was missed.

2. **`RETRACTION-AUDIT.tsv` / `docs/RETRACTION-AUDIT.md`** — 391 rows asking whether a figure withdrawn *in chat prose*
   still stands in a volume: 25 `LIVE-SUPERSEDED`, 7 `CANNOT-TELL`, 1 `CORRECTION-SUPERSEDED` (the chat was stale, the
   volume right — the branch's own warning that a row is a candidate, never an instruction). Re-measured here:
   - **2,475 (PO-0019/0080)** — L914 and L3439 assert it, L3482 withdraws it. **Already R3's**: DEFERRED.md 13a-01's
     residue sites (L914, L2533, L3067, L3434 against L3477's withdrawal) and READ-ch2-A 2-16 / READ-ch2-B D2.1. The
     audit's `already_docketed` on numeric rows is a bare digit search and did not see this; the doc says so.
   - **The closure rule one-sided (PO-0081)** — *binds one coordinate by a monotone function of one other* at four sites
     (main L11426 App. F.4.3, MC L516, IoI L2022, Transitions L202), none with a marker within three lines; **register 402**
     states the correction (THE CLOSURE RULE WAS ONE-SIDED AND THE OPERATOR IS TWO-SIDED). Docket 9(a) touches the main site
     for a pointer fault only. **Not docketed for the rule. New.** Its source is a seated Register entry, not chat prose.
   - **"not a lattice" (PO-0158)** — main §14 and the three-body paper (Law 3) print lattice-hood refuted from componentwise
     meet/join failures, which refute sublattice-hood of the product. **Not docketed. New**; the argument is the branch's.
   - **"the whole tower" (PO-0091)** — main L5756 / L5778 (Figure 21.1 and §21.5.3); register 1790 endorses the scope
     while its own stage table gives Λ₈, Λ₉ cycle rank 0. Docketed for the caption's counts, not for the scope. **New.**
   - **Seven constraints' correlation (PO-0013)** — READ-ch10 10-04. Already R3's.
   - **Kitagawara 0 / Belokolos 8 (PO-0051)** — reproduced; WORKING-REGISTER measured the neighbouring fact (§ References
     carries none of 1450's four names). The priority attribution itself is not docketed. **New.**
   - **Register entries asserting what a chat withdrew** — 230, 314, 500, 502, 599, 602, 807, 1148, 1450, 1461, 1595, 1628
     carry no WITHDRAWN / WARNING / REFUTED / SUPERSEDED marker in their first 1,500 characters; 1395 carries WARNING.
     Reproduced on the current Register. Register 602's 219 covers against the MC's 24,585 is DEFERRED 13j-01 for §14.5.12,
     not for the entry. **Circumstantial, as the branch says: each entry needs reading in full before anything.**
   The class is new to R3: **a correction whose only witness is chat prose.** Chat-67 records findings from readings of the
   volumes; whether a transcript is a source R3 may repair *from* — as opposed to a lead R3 may read the volume *by* — is
   M's ruling, not mine. Until ruled, these rows are leads; the four whose evidence is inside the volumes (402 against the
   four sites; 2,475; 1790 against its own table; 24,585 against 602) can be read on the volumes alone.

3. **`REGISTER-GAPS.tsv` / `docs/REGISTER-GAPS.md`** — the 132 numbers absent in 1..1792 partition into 119 relocated to
   WORKING-REGISTER.md under `<!-- EXCISED N : reason -->` (exact both ways) and **13 seated in neither**: 176, 177, 661,
   662, 663, 670, 671, 672, 682, 683, 687, 688, 1138 — plus, above 1792, 1797 (R3's, entry 1797 staged and not seated).
   Reproduced on BUILD102's Register. `r2-regsweep2` already prints the 132 and the 13 are inside its listing; what the
   branch adds is a witness — `extracted/archives/method16-rp-b-data/COLLECTION-LOG.md` quotes *Register 661* as a live
   instruction, so 661 was an entry once. Whether 661–688 were withdrawn or reserved is M's; it joins the census
   retirement question (DEF-153O). The branch's *1,660 entries* is distinct numbers ≤ 1792; the front matter's 1,657 is
   headings to 1815; `register_counts.py` prints both units and neither corrects the other.

4. **`tools/orderideal.py` / `docs/ORDER-IDEAL.md`** — register 66's downward-closure claim (*no violations across all 118
   cells … 1 of 120 ℓ-orderings*) re-run on the seated `LW1-ground.py`: 98 cells, 197 violations, 0 of 120; an unbanked
   chat re-measurement gave 110 cells, 172 violations, 0 of 120. The instrument imports the member and states its
   RECOVERED / RECONSTRUCTED conventions. Register 66 is unmarked and **nothing in DEFERRED, DOCKET, RULINGS or any READ
   names it.** R3's route, if M rules the entry quantifies over the observed table, is an entry recording the
   re-measurement beside it (1807's shape), never an edit of 66. The narrowed question — *which object does 66 quantify
   over?* — is M's.

5. **`PROSE-ONLY.tsv` / `docs/PROSE-ONLY.md`** — 1,168 statements held only in chat prose: 40 fault ids and 178 registers
   named in prose and held nowhere; P19–P23 as Laws; the §3.3 caps (3,3,2,3) not giving 976 cells (**docketed**: DEFERRED,
   READ-ch10, READ-reg9); "the null was 96, not 28"; dim(Λ₈) = 8 false; register 695's Ca I values and `channels.py`'s
   bracket written by construction (not checked here against the census); the Λ₁₄ → 1D collapse as the reason the tower
   stops at Λ₁₃. Rows are candidates for a home, the list is a floor, and none is executable by R3 without M.

6. **Governance and tooling** — `CLAUDE.md` rewritten (drive bijection narrowed to the two mirrored roots; `drive/chats/`
   354 files; `recovered/` 2,382 files; `tools/coverage.py --chats`, `tools/docfigures.py` which exits 1 on any stale count
   in CLAUDE.md or docs/). The R3 branch's own CLAUDE.md edits (six instruments, `tools/slopeaxis.py`) are the conflict.

## Decisions taken here

- **Not merged into the R3 branch.** The branch is live and 411 MB of chat shards; the two lines share no file under
  `method/`. Land it on main by its own pull request, then merge main into R3 and resolve `CLAUDE.md` by hand, keeping
  both sides' instrument lists. Nothing in it changes the BUILD102 close (W-215, W-216).
- **The queue gains one class and three named items, none executed:** the chat-witnessed retraction class (item 2, M's
  ruling on the source); register 402 against its four sites, 1790 against its own table, and register 66 (items 2, 4),
  each readable on the volumes alone.

## Open, for M

- Whether chat prose is a source R3 may repair from, or only a lead. (Item 2.)
- Which object register 66 quantifies over. (Item 4.)
- 176, 177, 661–688, 1138: withdrawn or never issued; with the census retirement question. (Item 3.)
