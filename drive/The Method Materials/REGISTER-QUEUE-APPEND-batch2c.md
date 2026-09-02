# REGISTER QUEUE APPEND — B-list Batch 2 close + Batch 3 opening (chat 58, BUILD58 → BUILD59)
# Append to OWED-REGISTER-EXPANSIONS.md after the batch2b append. Numbers await Register 1.1 (append-only; Ruling 27).

## SUBJECT-REGISTER CORRECTION SLIP (queue after slip B2-C2)

SLIP B2-C3 — THE BOX COUNT'S CLOSED FORM WAS ASSERTED FROM THE TREE AND IS NOW PROVED, IN BOTH
DIRECTIONS, WITH THE LEAF CONVENTION STATED. The `L.box` object carried a one-sentence statement
("factorises because the constraint graph is a tree; no Möbius sieve needed") at grade COMPUTED,
and §10.4 states the factorisation with its two closed-form leaves, verified on eight random
intervals. Measured in chat 58: the factorisation agrees with direct enumeration on every box
[x∧y, x∨y] of Λ at the base caps — 475,800 unordered pairs and 976 singletons, 116,138 distinct
boxes, zero discrepancies — and the full peel of the caterpillar, one coordinate per step, carries
a message of one argument at every step and agrees with enumeration on 100 random boxes at each
of 976, 8,847 and 25,748 cells; the argument uses no cap. The converse is Freuder's: width 1 if
and only if the constraint graph is a forest, so a cycle forces a two-coordinate message and the
Rota sieve with its signs — witnessed on Λ by closing the triangle k—q—2S with 2S ≤ q+1 (976
cells to 911; elimination width 2; tree-style count wrong on 9 of 40 boxes, eight-term sieve right
on 40 of 40; box lo = (2,1,2,0,2,0,0,0), hi = (3,1,3,2,3,1,1,3): 280 against 240, the 40 being the
box's points of Λ violating the closing constraint). Reader-facing ambiguity recorded, not edited:
§10.4 writes the leaves as hi₇/lo₇ (2S) and hi₆/lo₆ (g), which is coordinate position counted
from zero in the order (n, ℓ, k, q, e, f, g, 2S); the book elsewhere counts eight coordinates from
one. The object now states the convention; the main volume is untouched pending M's ruling.
Grade COMPUTED → PROVED. Cites the `L.box` object, `L.tree`, `L.void`, `L.voidfrac`, and §10.4.
Both states preserved.

## WORKING-REGISTER ENTRY (editorial; never enters the books)

W-B2c — MC-11 CLOSED; BATCH 2 COMPLETE (MC-07..11, 5 OF 5).
chat 58, BUILD58 → BUILD59. §0 gate passed on the files (main 18,446 / 5292fce8…; compendia
32,451 / 0832b5a9…; every presence check, the three BUILD58 discriminators, five PROVED grades);
Λ₈ rebuilt from lam8.py, 976 / 1,654. All claims computationally verified before writing (mc11.py,
mc11b.py; banked with the chat-57 six as chat58-instruments.tar.gz).

 VERIFIED (measured, mc11.py): eight random intervals reproduced 8/8; exhaustive factorised-vs-direct
 over 116,138 distinct boxes covering 476,776 pairs+singletons, 0 failures; 340,929 of those pairs
 have void > 0, void-free 28.49 % including singletons — (476,776 × 0.2849 − 976)/475,800 = 28.35 %,
 MC-10's joint figure, cross-checked.
 VERIFIED (measured, mc11b.py a): leaf-first elimination, max message arity 1 at all three caps
 (976 / 8,847 / 25,748 cells), 100 boxes each, 0 count failures. An earlier run reported arity 2 on
 the tree — an ordering artefact (min-factor-count tie-break peeled q before it was a leaf); the
 rule was corrected to "at most one live neighbour" and re-measured. Recorded so the artefact is not
 mistaken for a finding.
 VERIFIED (measured, mc11b.py b): closing constraint 2S ≤ q+1 non-redundant (976 → 911); width 2;
 tree-style count wrong 9/40; 8-term sieve correct 40/40; exhibit 280/240/40.

 AUTHORED: `L.box` statement (full expansion), condition (convention + caps + scope of the converse),
 grade COMPUTED → PROVED, source adds Lauritzen 1996, prior-art line (Freuder both directions, Rota
 for the sieve, Lauritzen for the chain rule); bibliography row 1996 Lauritzen gains `L.box`.
 Dependencies unchanged (`L.tree`, depth 3) — `L.void` is cited in text, not added as an edge, so
 no dependent-count line elsewhere moves. No new bibliography row (Freuder 1982 covers width 1 ⟺
 tree). Guard (measured substitute; guard.py still unbanked): diff(BUILD58, BUILD59 compendia) =
 exactly 5 hunks, 14525/14527/14529/14531 (the L.box block) and 16670 (bibliography); lines
 32,451 → 32,451. All prior discriminators re-measured = 1; `` `K.decay` `K.markov` `L.voidfrac` ``
 now 0 by design (row grew), replaced by `` `K.decay` `K.markov` `L.box` `L.voidfrac` `` = 1.

 NOT EXAMINED (named): the audit record at compendia line 25237 ("COMPUTED 114 · PROVED 66") is a
 dated audit finding, not a live census; MC-07..11 have moved five objects COMPUTED → PROVED and
 that line was not, and should not be, edited. If a live grade census exists in front matter it was
 not found by grep; a later pass should confirm.

Volume identity: BUILD59 main = BUILD56 main, UNTOUCHED (18,446 lines, md5
 5292fce89637c6b495363f76f99a4885); compendia 32,451 lines, 2,366,993 B, md5
 d7448858e09af0b5bfff2c0d36f275ba.
OWED-EXPANSIONS-2: row 11 DONE. Batch-2 authorised MC-07..11: 5 of 5 done — no shortfall.
M's ruling (chat 58): main-volume slip QUEUED, to be executed when the prose rewrite reaches source
 Chapter 10 "The void" (reader Chapter 8) — not before.

## DEFERRED MAIN-VOLUME ITEM (execute in the prose run at source Ch 10 / reader Ch 8; M ruling, chat 58)

MV-DEF-01 — §10.4 LEAF SUBSCRIPTS: the two closed-form leaves are written hi₇/lo₇ (2S) and
hi₆/lo₆ (g), i.e. coordinate position counted from zero in (n, ℓ, k, q, e, f, g, 2S), while the
book elsewhere counts the eight coordinates from one. When the rewrite reaches §10.4, either state
the convention in place or renumber the leaves to hi₈/lo₈ (2S) and hi₇/lo₇ (g) to match the rest
of the book — M's choice at that point. The `L.box` object (BUILD59) already states the zero-based
convention and must be kept in agreement with whichever form §10.4 takes. Press-time SUBS pair, not
a source edit, per standing practice. Enters the subject Register as a correction citing §10.4 and
`L.box` when executed; both states preserved.


## SUBJECT-REGISTER CORRECTION SLIP (queue after slip B2-C3) — BATCH 3

SLIP B3-C1 — THE BINARY LANGUAGE'S CUT IS EXACT AS A SET, NOT ONLY AS A COUNT, AND "DEPTH FIVE"
NAMES ONE OF THREE CIRCUITS. §11.1.1 states that the twenty cover-implications cut 131,072 words
to exactly 976 and that the circuit accepts at a depth of five; `L.bits` and `L.circuit` carried
both at grade COMPUTED. Measured in chat 58: J(Λ) has 17 generators and 20 covering relations;
cell ↦ word is injective on all 976 cells; join is bitwise OR and meet bitwise AND with zero
failures over all 475,800 unordered pairs; the twenty implications accept exactly 976 of the
131,072 words AND the accepted set is equal as a set to the image of Λ, which the record had
asserted only as a count; 17 bits carried, log₂976 = 9.93 needed, 7.07 surplus, occupancy
0.7446 %. The depth figure is reading-dependent and all three are now recorded: unbounded fan-in
2; two-input accept circuit ⌈log₂20⌉ = 5 above the implication level, 6 in total; downward
forcing circuit 4 covering steps along the longest chain of 5 generators. The book's five is the
AND-tree reading and the objects now say so. Grades COMPUTED → PROVED on both objects; `L.circuit`
gains `L.birk` as a dependency and Birkhoff 1937 as a source, the cut being the down-set theorem.
Nothing withdrawn. Cites `L.bits`, `L.circuit`, `L.birk`, and §11.1.1. Both states preserved.

## WORKING-REGISTER ENTRY (editorial; never enters the books)

W-B3a — MC-12 CLOSED; BATCH 3 OPENED (MC-12..16, 1 OF 5).
chat 58, continuing BUILD59. Verified before writing (mc12.py, banked in chat58-instruments.tar.gz).
 VERIFIED (measured): |Λ| 976, bottom (1,0,1,0,1,0,0,0), |J(Λ)| 17, covers 20; bijection OK;
 475,800 pairs, 0 OR failures, 0 AND failures; 2¹⁷ = 131,072 enumerated, 976 accepted, accepted
 set == image of Λ (set equality, not count equality); longest chain in J(Λ) 5 vertices / 4 edges;
 AND-tree depth 5, total 6, unbounded fan-in 2; max forcing fan-in 3, max fan-out 3;
 9.93 / 7.07 / 0.7446 % all reproduce.
 AUTHORED: `L.bits` and `L.circuit` full expansions, both COMPUTED → PROVED; `L.circuit` source
 gains Birkhoff 1937, depends gains `L.birk`; prior-art lines rewritten. Guard (measured
 substitute): diff(BUILD58, BUILD59 compendia) after MC-11 + MC-12 = exactly 11 hunks —
 14515/14519 (L.bits), 14525/14527/14529/14531 (L.box), 14635/14637/14639/14641 (L.circuit),
 16670 (bibliography); lines 32,451 → 32,451; all prior discriminators = 1.
 NOT DONE, named: MC-13, MC-14, MC-15, MC-16 remain open — Batch 3 is 1 of 5. MC-13/14/15 have
 NO existing compendium home (grep found no object carrying P21's ten combinations, the 2S
 leaf-detachment, or the three-facts theorem); they will need new objects on the `K.bracket` /
 `S.gen` precedent, which is a heavier operation than authoring into an existing object and
 should open a segment of its own. MC-16 has a home (`L.Fm1`, with `L.pal` and `L.rankpoly`).

Volume identity after MC-11 + MC-12: BUILD59 main = BUILD56 main, UNTOUCHED (18,446 lines, md5
 5292fce89637c6b495363f76f99a4885); compendia 32,451 lines, 2,369,651 B, md5
 2ad6eae4b896b3198ca975b4286ac96b.
