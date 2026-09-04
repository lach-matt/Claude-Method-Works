# DRAFT for M's review — Q5 pass 2: the chat-54 B-list batch 1 slips as Register entries 1826–1828. RULED AND SEATED (W-225).

**M's ruling (4 September 2026): seat with the new instrument, proceed.** Seated as 1826, 1827, 1828 with the re-run sentences
filled from `r3-q5b-measure.py`; the draft below is kept as reviewed.

---

*The draft as reviewed:*


Source: `drive/The Method Materials/REGISTER-QUEUE-APPEND-batch1.md` (chat 54, BUILD55 → BUILD56), slips B1-C1, B1-C2,
B1-C3, "numbers await Register 1.1 (append-only; Ruling 27)". Pass 1's rulings govern (RUL-153): approved form; production
to the Working Register; every figure re-run before seating, no shortcuts.

**One question before this pass can be seated — the instrument.** Chat 54 left no instrument pack. The mirror holds
`chat57-instruments.tar.gz` and `chat58-instruments.tar.gz` (batches 2b and 2c) and `repair-pass-instruments.tar.gz`
(pass 1), but nothing for batch 1: its W-B1 record says every claim was "computationally verified on the build before
writing" and names no file. The slips' figures — width of J(Λ₈) = 7 with the seven-chain Dilworth partition and the
seven-generator antichain listed; Λ₉'s width 7; ω(N(x)) ≤ 8, tight at (2,1,3,3,2,1,3,3); the Dilworth partition of the
976 cells into 122 chains, max antichain 122 = the largest level, skew −0.43, eight reflection survivors and none fixed —
are all computable from Λ₈ as `tower.py` / `lam8.py` build it, with the standard library. **Re-running them means a new
instrument (R3's, `r3-q5b-measure.py`), not the chat's.** Under the corpus's own status rule that is RECOVERED (measured
out of the corpus's own data by an instrument that is not the one the slip ran), and each entry would say so. *Is that
acceptable under "no shortcuts", or does pass 2 wait for the chat-54 instrument to surface?* Recommended: seat with the
new instrument, the entry naming it as a re-derivation and citing the slip's own account as the original.

**One fact the entries must carry.** The slips corrected compendium *objects* by handle — `L.dim`, `L.omega`,
`L.sperner`. The live Mathematical Compendium no longer prints those objects: the handles survive only in its
bibliography's object columns (r2-bib, register 1813's class — the handle vocabulary is defined nowhere in the live
volume). The main volume carries the corrections in prose (§8.6: *Λ₈ has order dimension exactly 7*). Each entry
therefore names the object as it stood at BUILD56 and says where the correction is printed now.

---

### 1826

**THE ORDER DIMENSION OF Λ₈ IS SEVEN, NOT EIGHT; THE ASSERTED FIGURE IS CORRECTED BY THE DERIVATION IT NEVER HAD.** *Register 35 proved dim = 3 at three coordinates both ways; register 36 exhibited the standard example. The extension "dimension = coordinate count, rising by one per adjoined axis" was carried without re-running the lower-bound half at any later stage, and register 409 recorded it as the one underived quantity in Part II. The derivation now run: width of J(Λ₈) = 7, certified by a seven-chain Dilworth partition (upper) and a seven-generator antichain (lower — (1,0,1,0,1,0,0,1), (1,0,1,0,2,1,0,0), (1,0,1,0,3,0,0,0), (1,0,1,1,1,0,0,0), (1,0,2,0,1,0,0,0), (2,1,1,0,1,0,0,0), (3,0,1,0,1,0,0,0)), so dim(Λ₈) = 7 by Dilworth 1950. Mechanism: every g-raising generator lies above the q-atom because g ≤ q — the coupling welds g's order-information to q's; kin to register 1143's production rule (monotone production adds no join-irreducibles). Λ₉ also measures width 7 (|Λ₉| = 1,654 confirmed), so per-axis rise fails at the first step. Corrects the claim register 409 records; §8.6 now prints the seven; the compendium object L.dim, as it stood at BUILD56, carried the theorem, and the live compendium names the handle only in its bibliography. Drafted at chat 54 (B-list batch 1, MC-06) as slip B1-C1 and queued for a "Register 1.1"; seated under RUL-153 Q5. [RE-RUN SENTENCE — pending M's answer on the instrument.] Both states preserved.* Registers 35; 36; 409; 1143. (a correction.)

### 1827

**ω(N(x)) IS BOUNDED BY THE COORDINATE COUNT, NOT THE ORDER DIMENSION.** *The printed proof — one prime per coordinate — always proved ω ≤ 8; the bound was quoted against dim(Λ) when 8 was believed to be the dimension. With dim = 7 (register 1826) the quoted form is false — the cell (2,1,3,3,2,1,3,3) attains ω = 8 > 7 — and the corrected form ω ≤ 8 is tight at that cell. The object L.omega's dependency on L.dim is released (now L.arith, L.def), as it stood at BUILD56. Drafted at chat 54 as slip B1-C2; seated under RUL-153 Q5. [RE-RUN SENTENCE — pending.] Both states preserved.* Registers 1826. (a correction.)

### 1828

**THE PECK INHERITANCE ON L.sperner WAS OVER-BROAD; SPERNER SURVIVES BY DIRECT CERTIFICATE, SYMMETRY DOES NOT TRANSFER.** *Stanley 1980's Peck property includes rank-symmetry, which Λ measurably lacks (skew −0.43; 5 against 4 at rank 4). The register entry recording the compendium generator fix quoted the old wording ("Λ is of that form, and the property is INHERITED") — that entry stands as history; the compendium object, as it stood at BUILD56, carried the direct proof: a Dilworth partition of all 976 cells into 122 chains, max antichain = 122 = the largest level. Register 44 had stated the property (Sperner though not rank-symmetric); register 1794 later read the rank-skew and Sperner entries against each other. Drafted at chat 54 as slip B1-C3; seated under RUL-153 Q5. [RE-RUN SENTENCE — pending.] Both states preserved.* Registers 44; 1228; 1794. (a correction.)

---

The W-B1 editorial record (MC-01 … MC-06 authored and verified at BUILD56; the nine approved edits) goes to the Working
Register with the pass, as slips 09 and 10 did.
