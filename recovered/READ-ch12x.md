# READ-ch12x — Phase R2, main volume §12.11.1.6 "The periodic table's own numbers…" and §12.11.1.7 "And the selection rules decide…" (chat 77)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L3318–L3362 (45 lines, none over 106 characters; §12.11.2 opens at L3363), read in full against the real-numbers pass (L4195–4196, `18,288 constraint tests across all 118, zero failures — register 529`), Register 529 (R L1975–1977: 247 real subshells, the nineteen anomalies, the fifteen predicted superheavies), the Register (628 at R L2347–2349; 629 at R L2351–2353), MC L2574 and the segment instrument r2-ch12x.py (arithmetic on every printed ratio, sum and difference; no tower needed). Pointers: the `118 configurations … 18,288 constraint tests` (L3321) resolves to L4195 and Register 529; Registers 628–629 (L3361) resolve and restate the section exactly. No lowercase `register NNN` or `A.N` in range. Census rows in range: 0 — CENSUS-CLOSURES-ch12x.tsv is header only.

## A. Deviations (both texts)

**12x-01 · subject matter — the population is named but printed nowhere, so none of the base counts can be re-measured from the record.** L3322: `Building cells (Z, n, ℓ, k, q, e, f, g) from real occupied subshells gives 4,325`; L3332: `E over these cells with Z as a coordinate is **972,862**; strip Z and it is **28,503**`. The input set is named (the 118 real configurations of the 18,288-test pass; Register 529 counts 247 subshells with nineteen anomalies and fifteen predicted superheavies), but the configurations and the 4,325 cells appear in no member of either bundle (MEASURED: grep across all members), so the eight base counts (4,325; 982; 3,686; 2,673 / 1,652; 606 / 3,719; and the within/across splits) and both E values are record-carried and not re-measurable — the same class as 12m-01 (a claim whose population the record does not carry), though here the population is at least specified. Every derived figure is internally exact (B). Reconstructing the configurations from outside the record would be reciting, not measuring; for R3, where M may rule the data into the record (an appendix or data member) or rule Register 529's sourcing sufficient. Registers 628–629 and MC L2574 restate the same counts and inherit.

## B. Verified (all MEASURED; r2-ch12x.py — arithmetic on the printed values)

- L3343–3348 all ten rates reproduce to the printed precision: 982/4,325 = 0.227, 3,686/4,325 = 0.852; 309/2,673 = 0.116, 2,399/2,673 = 0.897; 673/1,652 = 0.407, 1,287/1,652 = 0.779; 233/606 = 0.384, 544/606 = 0.898; 749/3,719 = 0.201, 3,142/3,719 = 0.845.
- The partitions are exact: EM-allowed + EM-forbidden and parity-conserving + parity-changing both sum to the all-row in cells (4,325), within (982) and across (3,686).
- L3324–3326: 22.71 %, 85.23 %, +2,704, +62.5 points all reproduce. L3350–3352 / L3360–3361 the percent forms (11.6, 40.7, 89.7, 77.9, 38.4, 20.1) match the table.
- L3354–3355 the crossing as stated: within 0.116 < 0.407 (refuted), across 0.897 > 0.779 (confirmed) — the printed rates carry it.
- Registers 628 and 629 restate the section's figures exactly; MC L2574 restates the four crossing rates.
- L3321's pointer: the 118-element, 18,288-test pass is at L4195 with register 529, which resolves to the claim.

## C. Incidental

- L3329 `it is six-sevenths`: 6/7 = 85.7 % against the printed 85.23 % — a loose fraction.
- The 77.9 % here is the EM-forbidden across rate (1,287/1,652) — the same numeral as §12.11.1.1's axis-11 density (10,585/13,585), distinct quantities; cross-noted against 12t-02's sites so R3 does not conflate them.
- L3324–3326 and L3343–3348 are column-dump tables; four 4-space paragraphs render as code — production class.
- With this segment, §12.11.1's whole block (§12.11.1.1–.7, L3177–3362) is read; §12.11.1 itself (L3032–3176) closed in chat 76.
