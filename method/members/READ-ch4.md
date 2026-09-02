# READ-ch4 — Phase R2, main volume Chapter 4 "The failures of the assistant, and the protocol each one earns" (chat 69)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L1436–L1464 (29 lines), read in full against §28.7.8 (L7684), §28.7.9 (L7689) and Register 655 (L2425). Labels as READ-ch3. Form follows SWEEP-B-C-chat67.md. Nothing in any volume was changed.

## A. Deviations (both texts)

**4-01 · L1441–L1452 (structure).** PRINTED: the ten mechanisms as plain-line items `4.1 … 4.10`, no `###` headings. SOURCE: the volume cites `§4.1` ×1, `§4.2` ×1, `§4.4` ×1, `§4.6` ×7, `§4.7` ×1; the Register groups entries under `§4.1 —`, `§4.2 —` headings (L1319, L1323). MEASURED (grep). READING: every §4.x citation in the book resolves to an unheaded line (READ-ch3 3-23); a COHERENCE-class item, and M's to rule whether the items become headings.

**4-02 · L1448 against §28.7.9 L7696.** PRINTED 4.7: `a flag is a hypothesis — localise a detector's output before filing it as a defect`; §28.7.9's value row names the mechanism `detector artifact`. MEASURED (awk). READING: one mechanism under two names — INFERRED identity from "detector".

**4-03 · L1454–L1458 (layout).** Four-space-indented paragraph (rendered as a code block). MEASURED. Same class as READ-ch3 3-31.

**4-04 · L1462.** PRINTED: `cited as §4.1 and §4.2 throughout a book that never defined them` (history, Register 655). SOURCE: the volume now prints `§4.1` once (L1462 itself) and `§4.2` once (L1462 itself); the Register carries both as group headings. MEASURED (grep). READING: "throughout" describes the earlier form; the sentence is explicitly historical and stands.

## B. Verified

- L1438 `Ten mechanisms`: §28.7.8 L7685 `40 of the entries above are instances of 10 mechanisms, each stated in full at §4`; §28.7.9 table L7696–7700: value 3 (7 entries), derivation 3 (15), inference 4 (18) — 3 + 3 + 4 = 10, 7 + 15 + 18 = 40. L1455–1456 `Three of the ten sit at the value, three at the derivation, four at the inference` agrees. MEASURED (awk, arithmetic).
- L1454 `§28.7.9 adds a coordinate this list does not have: the LEVEL` = heading L7689 `The level a fault landed at, which is a coordinate §4 does not have`. L1456–1458 the merged pair (stale figure = value going stale; conclusion written early = inference drawn early) = §28.7.9 L7708–7710. MEASURED (grep).
- L1461–1463 Register 655 (L2425): `CHAPTER 4 WAS A HEADING WITH NO BODY, AND IT SAID SEVEN … cited §4.1 and §4.2 throughout its life and never defined them — the mechanisms lived at §28.7.8, and there are ten`. MEASURED.
- The ten names at L1441–1451 match the ten at §28.7.9 L7696–7700 except 4-02. MEASURED (read).

## C. Incidental

- §28.7.9 L7710–7711 predicts a third mechanism, `a derivation written before the output`, and identifies it with §4.6's `test that could not fail` — the pairing is read there, not in Chapter 4; nothing to record here. (A grep fragment first suggested a 4.5/4.6 mismatch; the full sentence dissolves it — recorded so the fragment is not re-read as a finding.)
