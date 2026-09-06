# REGISTER QUEUE APPEND — B-list Batch 2, MC-11 closure (chat 58, BUILD58 → BUILD59)
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
Awaiting M's ruling on the §10.4 subscript convention (main-volume slip, or leave).
