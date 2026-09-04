# READ-gaps13 — the thirteen Register numbers seated in neither register, answered from the record (RUL-153 Q3). RECORDED; no number reissued, no entry moved.

**The question.** 132 numbers in 1..1792 have no entry in the Register; 119 are relocated to WORKING-REGISTER.md under an
`<!-- EXCISED N : reason -->` marker (REGISTER-GAPS, exact both ways); thirteen are in neither: 176, 177, 661, 662, 663, 670,
671, 672, 682, 683, 687, 688, 1138. M ruled (4 September 2026) that the answer lies in the chat transcripts and the prose
only they hold, which `drive/chats/` and `REGISTER-GAPS.tsv` on the consolidation branch make readable. Read here: every
shard naming one of the thirteen as a register (`git grep` over 352 conversations), the two repository files the branch's
census names, and every mirrored main build from BUILD9 (highest entry 1760) to BUILD90.

**No mirrored build ever seated any of the thirteen.** BUILD9, the earliest main bundle in the mirror, already lacks all
thirteen while holding 1137 and 1139 and every neighbour; so does every later build. Whatever happened to them happened
before the first press the mirror holds.

## The answers, each with its witness

| number | answer | witness |
|---:|---|---|
| **176, 177** | **never issued** | named as a register in no conversation (the two hits are *math register 177 objects*, a count, and a truncated *register 177x*), in no build, in no file; entry 175's body narrates them (r2-reg4a) |
| **661** | **issued in a working file, never seated** | heads `COLLECTION-LOG.md` (spectra collection, phase 1): *Register 661. Collect everything before any analysis or write-in.* |
| **662** | issued in a working file, never seated | the same log: *Register 662. The Handbook publishes an ASCII variant of every table…* |
| **663** | issued in a working file, never seated | `reader_audit.py` L4: *Register 663. The twenty-two prime audits read the SOURCE and pass.* |
| **670, 671, 672** | issued in a working file, never seated | the same log: the web-search route (670), Ar II from ASD 5.12 (671), Si I / Si II / Sc III / Sc IV / Ba III / Bi II counts (672) |
| **682** | issued in a working file, never seated | `spectra_raw/BaLII.tsv` L6: *…no quantum defect can be computed. Register 682.* |
| **683, 687, 688** | issued in a working file, never seated | the same log: Sansonetti & Curry 2010 free full text (683), *a lead rather than a document* (687), TOPbase (688) |
| **1138** | **cited in conversation as an entry, never seated** | conversation `3851d6dc` (*The Method 1.6*, 8 August 2026), messages 1088, 1098, 1100: *"incomparable" — register 1138* and *the fault register 1138 found, where φ(charge \| Z) refused N VI because sulphur was the only element we held at charge 6*; neither claim is in the Register under any number |

The ten in 661–688 belong to one episode: the spectra collection that the Register's own 673 (*the channel table is completed
from what is on hand*), 674, 681, 684, 686 and 689 continue. The collection log numbered its findings as register entries as
it went — retrieval routes, the ASCII variant, the Ar II arrival, the free full text, the TOPbase lead — and the entries that
reached the Register begin at 673. Their bodies exist, in the log and the two files, under
`extracted/archives/method16-rp-b-data/` and `extracted/archives/restore-point-2-13/`.

## What follows, and what does not

- **Nothing is reissued, renumbered or moved.** M's recommendation-as-ruled: 176 and 177 never issued; the rest recorded with
  a one-line reason in the Working Register. This reading is that record; W-220 carries the table's one-line form.
- **Whether the ten log entries should be seated as Register entries is not decided here.** They are subject matter (routes
  tried, sources found) and would enter only by an entry of M's; the bodies are held and named.
- **1138's two claims** survive only in one conversation's prose. Whether either is true of the current index is a reading
  of Chapter 24's alphabet construction, not of this file.
- The consolidation branch's `REGISTER-GAPS.tsv` classes hold (`UNSEATED-NO-TRACE` for 176/177, `UNSEATED-CITED-IN-REPO` for
  the ten, `UNSEATED-CITED-IN-CHAT` for 1138); its *chat_mentions 0* for the ten is right for prose and wrong for the
  tool-call bodies, which is where the log was written.
