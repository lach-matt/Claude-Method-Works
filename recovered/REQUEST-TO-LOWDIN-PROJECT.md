# REQUEST TO THE METHOD — LÖWDIN PROJECT
## From: The Method 1.6 build (chat 32, BUILD-32). One open item. 2026-08-26.

### What is being asked for, in one line

**The per-row member selection for 126 channel rows in the Spectra Compendium — or the rule that produced it — because the selection is not blind-reproducible from `spectra_raw`.**

---

### 1. The exact rows

126 rows, eight species. Counted from the Spectra Compendium's channel table today, not from a
carried figure:

| species | untested rows |
|---|---|
| Ne II | 37 |
| Ar II | 34 |
| Si I | 26 |
| Ba III | 11 |
| Ca I | 7 |
| Ca II | 6 |
| Ne I | 3 |
| Zn I | 2 |
| **total** | **126** |

Each prints `bracket = untested` in the table. The table as a whole currently reads
**1,577 of 1,738 cells tested across 392 rows, 78 no-triple, 126 untested, refusals zero.**

---

### 2. Why they are untested — the precise blocker

The bracket instrument (`run489.py`, run unmodified under Ruling 26: strict interval membership,
quotation floor as the only ε, §22.5 admissibility) needs, for each channel row, **the identified
member levels** — the specific levels selected into that series.

For 392 rows those members reproduce from the level bank. **For these 126 they do not.** The
selection cannot be regenerated blind from `spectra_raw`, so the rows cannot be tested without the
selection itself or the rule that made it.

This is a recorded negative finding, not a guess. **Register 1767:** the two stores delivered
earlier (`MEASUREMENTS-DERIVED`, `STORE-RECONSTRUCT`) cover 24 species and **the intersection with
these eight is empty.** Where that delivery did meet the table — Al I, Ga I, Na I, fifteen rows —
all fifteen limits agreed exactly with both the generated and the stored column. So the earlier
delivery was correct and simply does not cover these species.

---

### 3. What would close it — any ONE of these three

**(a) The per-row member lists.** For each of the 126 rows: species, channel/series designation, and
the level identifiers selected as its members. Any stable format — TSV, CSV, JSON. This is the
smallest sufficient answer and the one least likely to be ambiguous.

**(b) The selection rule, stated to the point of reproducibility.** How members were chosen from the
raw levels for these series — the ordering, the admissibility cut, the treatment of J-resolved
versus centroid levels, and the tie-break. If the rule is stated exactly, the selection can be
re-derived here and checked against the row count.

**(c) `store_gen.py`.** The generator itself. It was absent from the earlier delivery's MANIFEST and
absent from Drive when searched at chat 10. With it the selection can be re-run blind, which is the
strongest form of the answer because it is verifiable rather than asserted.

**Also useful if it exists separately:** the series limit used per row for these eight species. If
the limits travel inside (a) or (c), nothing extra is needed.

---

### 4. What is NOT being asked for — already held and verified here

- `spectra_selection_and_levels.zip` and its 15 extracted members — fetched, hash-verified against
  the MANIFEST, all matching. Do not resend.
- The six post-restore-point species (Bi III, C I, Cd II, Hg II, N I, Sc III). **Those 45 rows are
  closed** — register 1768, reconciled member-for-member, zero anomalies.
- `restore-point-2_13.tar.gz` — held, sha256 `80577094`, 708 files.
- The sealed bracket instrument — held and running unmodified.

---

### 5. Delivery constraints, learned the hard way here

- **Send a MANIFEST with sha256 per file.** Every file will be hash-verified on disk before a single
  cell is computed. A delivery without hashes can be read but cannot be trusted.
- **Under ~60 KB: fine by any route.**
- **Roughly 100 KB to 1 MB is the worst band** — the Drive connector returns anything below ~1 MB
  inline as base64, which cannot be written to disk. Files in that band should be **uploaded
  directly to the chat**, not shared via Drive.
- **Over 1 MB spills to disk and is safe via Drive.** Over 10 MB the connector refuses outright —
  direct upload only.
- Plain text beats archives. A single TSV is better than a zip of many.

---

### 6. If the answer is that the data does not exist

That is an acceptable answer and should be said plainly. **These 126 rows are currently printed as
`untested`, which is honest and correct**, and the work does not misstate itself by leaving them so.
If the selection is genuinely unrecoverable, the rows stay untested, a Register entry records why,
and the matter closes permanently rather than being carried open for another twenty sessions.
