# READ-ch12v — Phase R2, main volume §12.11.1.3 "An index has a time column exactly when its cells are moves" (chat 77)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L3233–L3268 (36 lines, none over 106 characters; §12.11.1.4 opens at L3269), read in full against §12.11.0 (L2535; the composability of Λ₉, r2-ch12f), Register 313 (R L1163–1165), the companion's threshold table (Transitions.md L554–559; IoI L110–117), the Register (620 at R L2317; 622 at R L2323–2325; 623 at R L2327–2329; 624 at R L2331; 625 at R L2335–2337) and the segment instrument r2-ch12v.py (r2lib by path; build9/src/tgt of r2-ch12f; every Λ₈ and Λ₉ cell). Pointers: §12.11.0 (L3235, L3262) resolves to the heading and to the composability finding; lowercase `register 313` (L3235) resolves to R L1163 and to the exact claim (`Λ already carries time — source, transfer, target`, `its target carrying three coordinates against a source's four`); Registers 622–623 (L3267) and 625 (L3265) resolve; 622 restates the table, 623 and 625 inherit 12v-01/12v-02. No `A.N` in range. Census rows in range: 0 — CENSUS-CLOSURES-ch12v.tsv is header only.

## A. Deviations (both texts)

**12v-01 · subject matter — "The twenty-point jump" heads a seventy-point jump.** L3261: `**The twenty-point jump.** Λ₈ composes **not at all** — zero of 976 … adding the single axis 2S′ ≤ g takes Λ₉ to **70.7%.**`; L3263–3264: `it is the whole distance from nothing to seven-tenths`. MEASURED (r2-ch12v): 0 → 70.7 is a 70.7-point jump; twenty (20.4) is the jump from the withdrawn 50.3 % (L3264: `An earlier form of this paragraph said 50.3%`) to 70.7. The bold lead-in is residue of the withdrawn computation, contradicted by its own paragraph two lines later. Register 623's headline carries the same residue — `AND THE AXIS THAT MAKES THE TOWER A CATEGORY IS WORTH TWENTY POINTS` over a body that prints `Λ₈ is **0%** composable … takes Λ₉ to **70.7%**`.

**12v-02 · record — Register 625 attributes the withdrawn figure to Register 623, whose printed body does not carry it.** Register 625 (R L2337): `Register 623's 50.3% for Λ₈ used a three-against-three signature chosen for convenience`; Register 623 as printed (R L2327–2329) states `Λ₈ is **0%** composable — four coordinates against three` and contains no 50.3. The main volume (L3264–3265) attributes the earlier 50.3 % to `this paragraph` and cites Register 625. As the record stands the correction chain is broken: the corrected value appears in the entry the correcting entry cites as carrying the withdrawn one — either 623 was changed after 625 cited it (against append-only) or 625's attribution is to a state 623 never printed. The withdrawn figure itself reproduces on the convenience signature (491 of 976 = 50.3 %, MEASURED), confirming 625's account of the method. Both texts recorded; no withdrawal; for the Register segment and R3.

## B. Verified (all MEASURED unless marked; r2-ch12v.py)

- L3240 / L3261 Λ₈: 0 of 976 composable under the book's own signatures — source (n, ℓ, k, 2S), four coordinates, against target (e, f, g), three (register 313's `three coordinates against a source's four` read literally; no 3-tuple equals a 4-tuple).
- L3241 / L3262 Λ₉: 1,169 of 1,654 = 0.7068 → prints 0.707 and 70.7 %.
- L3242 the violation index: 2,370 cells, 1,410 reachable, 0.5949 → prints 0.595 — record-carried from the companion's threshold table, which Transitions.md L554–559 and IoI L110–117 both print; internally consistent by Register 620's differencing (NEC = 0: 174 cells, reachable drop 0, all unreachable; NEC = 1: 276 of 432 = 63.9 %; NEC = 2: 396 of 618 = 64.1 %; the slices sum to 2,370). Register 624 records that the reachable column needs the companion's edge list, which the work does not have (main L5652: `what is NOT` printed) — so the row is record-carried by design, not un-measured.
- L3243–3244 the periodic table (90 cells) and the calendar (365) as state indexes with no second column — definitional (one position, nothing to compose); counts record-carried.
- L3250–3252 `The second column exists exactly when the first column's cells are moves` — holds of the five rows as printed.
- L3264–3265 the withdrawn 50.3 % reproduces on the three-against-three convenience signature (491 of 976), as Register 625 describes.
- L3258 the periodic table's E = 36 and Λ's E = 0 — record-carried (4 sites of `E = 36` in the main volume; Λ's closure banked at r2-ch12r).

## C. Incidental

- Register 620's `exactly 64% of NEC = 1 cells and 64% of NEC = 2 cells` is 63.9 % and 64.1 % — rounding, noted for the Register segment.
- L3239–3244 the table is a column-dump and L3246–3248 / L3257–3259 4-space paragraphs render as code — production class.
- L3236 `The companion's threshold table prints the same pair` — it prints the pair (2,370, 1,410) as its first row; `the same pair` refers to cells/composable, resolved.
