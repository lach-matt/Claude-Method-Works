# REGISTER QUEUE APPEND — B-list Batch 1 (chat 54, BUILD56)
# Append to OWED-REGISTER-EXPANSIONS.md. Numbers await Register 1.1 (append-only; Ruling 27).

## SUBJECT-REGISTER CORRECTION SLIPS (queue after slips 05–12)

SLIP B1-C1 — THE ORDER DIMENSION OF Λ₈ IS SEVEN, NOT EIGHT; THE ASSERTED FIGURE IS CORRECTED BY
THE DERIVATION IT NEVER HAD. Register 35 proved dim = 3 at three coordinates both ways; register 36
exhibited the standard example. The extension "dimension = coordinate count, rising by one per
adjoined axis" was carried without re-running the lower-bound half at any later stage, and register
409 recorded it as the one underived quantity in Part II. The derivation now run: width of J(Λ₈) = 7,
certified by a seven-chain Dilworth partition (upper) and a seven-generator antichain (lower —
(1,0,1,0,1,0,0,1),(1,0,1,0,2,1,0,0),(1,0,1,0,3,0,0,0),(1,0,1,1,1,0,0,0),(1,0,2,0,1,0,0,0),
(2,1,1,0,1,0,0,0),(3,0,1,0,1,0,0,0)), so dim(Λ₈) = 7 by Dilworth 1950. Mechanism: every g-raising
generator lies above the q-atom because g ≤ q — the coupling welds g's order-information to q's; kin
to R 1143's production rule (monotone production adds no join-irreducibles). Λ₉ also measures width
7 (|Λ₉| = 1,654 confirmed), so per-axis rise fails at the first step. Corrects the claim of register
409's subject; cites 35, 36, 409, R 1143. Both states preserved.

SLIP B1-C2 — ω(N(x)) IS BOUNDED BY THE COORDINATE COUNT, NOT THE ORDER DIMENSION. The printed proof
(one prime per coordinate) always proved ω ≤ 8; the bound was quoted against dim(Λ) when 8 was
believed to be the dimension. With dim = 7 (B1-C1) the quoted form is false — the cell
(2,1,3,3,2,1,3,3) attains ω = 8 > 7 — and the corrected form ω ≤ 8 is tight at that cell.
`L.omega`'s dependency on `L.dim` is released (now `L.arith`, `L.def`).

SLIP B1-C3 — THE PECK INHERITANCE ON `L.sperner` WAS OVER-BROAD; SPERNER SURVIVES BY DIRECT
CERTIFICATE, SYMMETRY DOES NOT TRANSFER. Stanley 1980's Peck property includes rank-symmetry, which
Λ measurably lacks (skew −0.43; 5 against 4 at rank 4). The register entry recording the compendium
generator fix quoted the old wording ("Λ is of that form, and the property is INHERITED") — that
entry stands as history; the compendium object now carries the direct proof: Dilworth partition of
all 976 cells into 122 chains, max antichain = 122 = largest level. Cites the generator-fix entry.

## WORKING-REGISTER ENTRY (editorial; never enters the books)

W-B1 — B-LIST BATCH 1 AUTHORED AND VERIFIED (MC-01..06), chat 54, BUILD55 → BUILD56.
Every claim computationally verified on the build before writing (HANDOFF-6 rule):
 MC-01 L.closed  — 475,800 pairs, 0 join/meet failures; worked two-branch proof authored.
 MC-02 L.dist    — exact by pointwise identity + L.closed; 4,000 triples, 0 failures.
 MC-03 L.modular — 475,800 pairs, 0 failures; derivation authored; grade COMPUTED → PROVED.
 MC-04 L.birk    — 17 J, 20 covers; all 2^17 subsets enumerated, exactly 976 down-sets; fifteen
                   support-patterns identical at caps (3,3,1,3,1),(4,4,2,4,1),(4,4,2,6,2),
                   (5,5,2,6,2) with generators 17/24/33/35; grade → PROVED.
 MC-05 L.sperner — sequence 1,5,15,34,59,87,108,121,122,115,100,79,57,37,21,10,4,1 (ranks 3–20)
                   log-concave; Dilworth certificate 122; skew −0.43; 8 reflection survivors, 0
                   fixed; terms(p^k)=1,1,3,3,3,1,1 symmetric; grade → PROVED; Peck note corrected
                   (B1-C3).
 MC-06 L.dim     — REFUTED-as-stated and authored as the theorem dim = 7 (B1-C1); L.omega fixed
                   (B1-C2); main §8.6 rewritten; main ω-bound sentence fixed; main audit-hierarchy
                   parallel fixed ("dimension seven", casualty-swept clear, M-approved).
Volume identity: BUILD56 main 18,446 lines md5 5292fce89637c6b495363f76f99a4885; compendia 32,451
lines md5 4fb5b6b361e8568db968ba7610326a72. Guard substitute: diff(BUILD55, BUILD56) = exactly the
nine approved edits (3 main sites + 6 compendium objects); no other line touched.
OWED-EXPANSIONS-2 rows 1–6: mark DONE (row 6 DONE-with-correction). Token resolution remains LAST.
Next: Batch 2, MC-07..11.
