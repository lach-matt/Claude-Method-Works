# BRIDGE — LOWDIN SESSION 55 · THE ORDERING CLAUSE SURVIVES c→∞; THE CONFIGURATION DOES NOT

Open Session 56 with **`bash pack55/open55.sh`** and nothing else.
The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 55 DID

Opened clean. Closed F54.3. Confirmed Z=90 independently and extended it. Found that
s54's headline misattributed the finding, corrected it, and in doing so answered an item
owed since s47.

    ORDERING CLAUSE   0 failures in 119 steps         unchanged (sealed chain)
    ORDERING CLAUSE   n+l UNCHANGED at all 11 rows tested at c=1e6   <-- NEW
    DERIVATION        107 rows, Z=2..108              unchanged
    CLAUSE 3          ANSWERED FOR THE ORDERING CLAUSE: it is NOT relativistic.
                      The CONFIGURATION at Z=90 IS. Both stated in Deliverable 1.
    TRANSIT WIDTH     §6 item 3 ANSWERED (gate 93). Owed since s47.

**NOTHING IN THE SEALED CHAIN MOVED.** No sealed file was modified. Deliverable 1 was
rewritten (§0, §6.1, §6.3); its 19-clause checker, gate 86, still passes.

---

## §2 · F55.2 — s54 ATTRIBUTED THE Z=90 REVERSAL TO THE WRONG CLAUSE

s54 §6 wrote: "**The ordering clause is NOT derivable from the non-relativistic field.
It is a scalar-relativistic result, and Z=90 is the proof.**"

**5f has n+l = 8. 6d has n+l = 8.** They are degenerate in n+l. A change of entrant
between them is a change WITHIN a shell of equal n+l and cannot reach a clause that
orders BY n+l. Checked across every c=1e6 row now in hand:

    Z     55  56  57  58  72  88  89  90  91  92  105
    n+l    6   6   7   7   7   7   8   8   8   8    8    sealed
    n+l    6   6   7   7   7   7   8   8   8   8    8    c=1e6      IDENTICAL

**THE ORDERING CLAUSE SURVIVES THE REMOVAL OF RELATIVITY AT EVERY ROW TESTED.** That is
the opposite of what s54 filed, and it is the stronger result. What the Z=90 reversal
does reach — and it genuinely does reach these — is the TIE-BREAK, the OBSERVED
CONFIGURATION, and the TRANSIT WIDTH.

This is F44.2's pattern exactly: a real number, correctly computed, attributed to the
wrong channel. It was found by asking what n+l the two competing channels carry — a
question the c3 table never asked because it recorded `ent`, not `n+l`.

**RULING: EVERY TABLE THAT COMPARES ENTRANTS ACROSS FIELDS MUST CARRY n+l FOR BOTH.**
A table that records only the channel name cannot distinguish an ordering-clause event
from a within-shell event, and the difference is the whole verdict.

## §3 · F54.3 — CLOSED (gate 90, 7/7, can-failed 3 ways)

The only rung-1 channel at Z=88 was **5f**, sixth in the ordering, 110 mHa below the
7s/6d decision. Ladder truncated to rung 0 (beta=0.4, maxit=100) and re-run:

    5f   conv=False  it=100   no rung-0 value exists   last iterate D=-0.03136
    7s   conv=True   it=34    D=-0.14359   reproduces sealed EXACTLY
    6d   conv=True   it=43    D=-0.13478   reproduces sealed EXACTLY
    ref  conv=True   it=34    rung 0

margin = 0.00881, ent = 7s, **computed with no rung-1 solve anywhere in the comparison.**

## §4 · Z=90 CONFIRMED AND ISOLATED (gate 91, 9/9, can-failed 3 ways)

Self-check fired on every launch and reproduced |dE(Z=80)| = **1206.454498 Ha** exactly.

    Z   sealed  c=1e6   m_sealed  m_c1e6    5f sealed->c1e6      6d sealed->c1e6
    89   6d      6d      0.03233  0.02223  -0.03146->-0.20036  -0.15762->-0.22259
    90   6d      5f      0.05405  0.12918  -0.13689->-0.39017  -0.19094->-0.26099  <-- REVERSAL
    91   5f      5f      0.08195  0.29609  -0.30535->-0.59532  -0.22340->-0.29923

Z=90 and Z=89 reproduce pack54/c3.jsonl **bit-for-bit**. Z=91 is new. All rung 0.

The differential (5f deepens more than 6d when relativity is removed) is uniform:
104 mHa at Z=89, 183 at Z=90, 214 at Z=91. It reverses a step only where it exceeds the
sealed gap AND opposes the sealed entrant: 89 fails on size (104 < 126), 91 fails on sign.
**Z=90 is the only crossing, and thorium is observed 6d2. The relativistic field is right
about thorium; the non-relativistic field is not.**

## §5 · THE SCREEN — 13 ROWS NOT WALKED, AND WHY (gate 92, 6/6)

s54 item 4 proposed walking Z=89..104. Every unrun row there has sealed ent=5f with
margin >= 0.12638, and the measured differential deepens 5f MORE than 6d — it acts WITH
the sealed entrant. Thirteen rows would each restate one direction.

    SCREEN: a step reverses at c=1e6 iff the differential EXCEEDS the sealed gap
            AND OPPOSES the sealed entrant.

Tested at its weakest point, Z=92 (smallest sealed margin in 92..104): ent=5f, margin
widens 0.12638 -> 0.35176, differential acts with 5f. **Z=93..104 are SCREENED, NOT
WALKED, and are labelled so wherever they appear. A screened row is never counted as a
walked row.**

## §6 · THE TRANSIT WIDTH — §6 ITEM 3 ANSWERED (gate 93, 7/7)

The owed question: why is the lag one proton at 4f and two at 5f?

    with relativity     (4f, 5f) = (1, 2)
    without relativity  (4f, 5f) = (1, 1)

Z=58 at c=1e6 gives ent=4f, margin widening 0.12115 -> 0.23960: the 4f transit is one
proton in BOTH fields. The 5f transit is two with relativity and one without.

**THE 4f/5f ASYMMETRY IS ENTIRELY RELATIVISTIC. The second proton of 5f transit is the
same 183 mHa 6d/5f differential that produces the Z=90 reversal.** §3's domain boundary
becomes, at 5f, a width DERIVED from the field rather than merely identified.
**Still owed:** the first proton, which both fields share and which is therefore not
relativistic in origin.

---

## §7 · ORDERED WORK LIST FOR SESSION 56

1. **`bash pack55/open55.sh`.** Expect verify55 clean; gates 1..71 diff to gate-6 `sec` only.
   Step 5 is now BOUNDED — poll repeatedly with `timeout 200 bash run.sh --wait GATES 180`.
2. **THE FIRST PROTON OF TRANSIT.** Both fields put one non-f proton before 4f and before
   5f. That shared proton is now the only unexplained part of the transit, and it is
   non-relativistic — so it is reachable by the same field without the c lever.
   Cheapest attack: Z=57 and Z=89 candidate spectra side by side; both are already in hand.
3. **DECIDE WHETHER CLAUSE 3 IS CLOSED.** It is answered on 11 adversarially chosen rows
   plus a screen. It is NOT answered exhaustively, and Deliverable 1 §6.1 says so in those
   words. Ruling needed: is the adversarial sample sufficient, or is a full 107-row c=1e6
   walk owed? (Cost of the full walk: ~107 x 200 s, several sessions.)
4. **Then clause 1** — the reverse chain to the many-electron Schrodinger equation.
   Reading is DONE (s53 §8 item 5); unchanged by this session.
5. Deferred: -8.021 mHa residue at Z=59; coupled 4f2.5d SO check; promotion operator as
   an object.
6. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s55.

---

## §8 · FAULTS THIS SESSION

    F55.1  O54.1's /tmp copy broke the gate runner's own dirname-relative cd;
           step 5 of the open had been SILENTLY NOT RUNNING          REMEDIED (gates_run55.sh,
                                                                     open55.sh)
    F55.2  s54 attributed the Z=90 reversal to the ORDERING clause;
           5f and 6d are both n+l=8, so it cannot reach that clause  REMEDIED (Deliverable 1
                                                                     rewritten), RULING FILED
    F55.3  gate93 v1 omitted pack54/c3.jsonl and reported a physics
           FAIL that was an input gap. It failed CLOSED, which is
           the correct direction                                     REMEDIED (gate93 v2)

F54.3 CLOSED this session (gate 90). No fault carried open into s56.

## §9 · INSTRUMENTS ADDED

    pack55/gates_run55.sh   relocation-safe full-replay runner, F55.1 remedy
    pack55/open55.sh        s56 open; bounded polling; names its own reference log
    pack55/f543.py          rung-0-truncated re-run, closes F54.3
    pack55/gate90.py        scores PREDICTION-F543.md
    pack55/gate91.py        scores PREDICTION-Z90CONFIRM.md
    pack55/gate92.py        scores PREDICTION-SCREEN.md
    pack55/gate93.py        scores PREDICTION-TRANSIT.md
    pack55/c3confirm.jsonl  Z=90,91,89 at c=1e6, chained, rung 0
    pack55/c3z92.jsonl      Z=92, the screen's weakest point
    pack55/c3z58.jsonl      Z=58, the transit-width row
    pack55/DELIVERABLE-1-REV-s55.md   replacement text, pre-image preserved