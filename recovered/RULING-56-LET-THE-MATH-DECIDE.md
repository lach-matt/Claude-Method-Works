# M'S RULING, s56 CLOSE — BOTH OPEN QUESTIONS ARE MEASUREMENTS, NOT OPINIONS

Filed AFTER LOWDIN-HANDOFF-56.tar.gz was sealed. NOT in MANIFEST-HANDOFF-56.
It is a LOOSE deliverable and must be folded into pack57 and hashed there.

M's directive: "For questions 1 and 2. I suggest letting the math tell us what the answers are."
Both §7 item 2 questions are hereby WITHDRAWN AS RULINGS and RE-ISSUED AS INSTRUMENTS.
Neither is to be answered by assertion. R 1449 applies: predictions filed before either runs.

---

## INSTRUMENT A — THE WIDTH RULE, DECIDED BY BASE RATE

The proposed rule ("a width is never established from one end") was offered as an assertion.
It is instead an empirical claim about this chain's own error history, and it is measurable.

**THE TRAP, NAMED FIRST.** F44.2, F55.2 and F56.3 are a FOUND-FAULT sample. They are known
because they were checked. Quoting "3 of 3 one-ended claims were wrong" would be selection
bias of exactly the kind register 1445 forbids. The denominator must include one-ended claims
that were NEVER checked.

    A-1  ENUMERATE every count/width/lag claim in the sealed chain and in Deliverables 1-4.
         For each, record: (i) does it assert a NUMBER OF STEPS or a WIDTH?
                           (ii) was evidence computed at the LOWER end (the loss)?
                           (iii) was evidence computed at the UPPER end (the win)?
    A-2  Partition into TWO-ENDED, ONE-ENDED-CHECKED, ONE-ENDED-UNCHECKED.
    A-3  MEASURE: of ONE-ENDED-CHECKED, what fraction changed when the missing end was run?
         Known so far: F44.2 changed, F55.2 changed, F56.3 SURVIVED. That is 2 of 3 -- but
         3 is not the denominator until A-1 has run.
    A-4  DECIDE: adopt the rule iff the ONE-ENDED failure rate materially exceeds the
         TWO-ENDED failure rate. If it does not, the rule is not adopted and F44.2/F55.2/F56.3
         are three unlucky draws, not a pattern.

**A-1's BY-PRODUCT IS THE POINT.** The ONE-ENDED-UNCHECKED list is a list of claims that may
be wrong and have never been tested. It is worth more than the ruling.

Cost: pure read of sealed text and rows. No solve. One session segment.

---

## INSTRUMENT B — CLAUSE 3, DECIDED BY COVERAGE, NOT BY SAMPLE SIZE

"Is 12 adversarial rows enough?" is the wrong question. The right one: **how many of the 107
rows can the field PROVE safe without being walked, and what is the residue?**

    B-1  THE FREE ELIMINATION (pure read, no solve).
         F55.2's theorem: a reversal between two channels of EQUAL n+l cannot reach the
         ordering clause -- it is a within-shell event, i.e. tie-break only.
         For all 107 rows compute n+l(entrant) and n+l(runner-up) from the sealed `order`.
         Rows where they are EQUAL are ORDERING-IMMUNE BY CONSTRUCTION, whatever c does.
         Remove them. Call the remainder the EXPOSED SET, size N_exp.
         PREDICT N_exp BEFORE COUNTING IT.

    B-2  THE BOUND, PARAMETER-FREE.
         Measured c=1e6 differentials now in hand:
              Z=57  0.09741      Z=89  0.10400      Z=90  0.18300      Z=91  0.21400
         Take B = the MAXIMUM measured differential (0.21400), applied uniformly. Crude,
         conservative, and contains no fitted constant. A Z-dependent envelope would be a
         fit and is REFUSED unless it is derived.

    B-3  THE COVERAGE COUNT.
         Every EXPOSED row whose sealed margin EXCEEDS B is PROVED safe: no differential
         of the measured size can reverse it. Count them.
         RESIDUE = exposed rows with margin <= B, minus the 12 already walked.

    B-4  THE ANSWER IS THE RESIDUE, AND IT IS A NUMBER.
         RESIDUE = 0   -> CLAUSE 3 IS CLOSED. No walk owed. The sample question never arises.
         RESIDUE = k   -> exactly k rows are owed, named individually, and the full 107-row
                          walk is NOT owed. Cost falls from ~107 x 150 s to k x 150 s.

**B-1 ALONE MAY CLOSE IT.** If most rows have entrant and runner-up sharing n+l, the exposed
set is small and the residue may be empty before any bound is applied. That would make Clause 3
closed by an ARGUMENT rather than by a walk -- the stronger outcome, and free.

**FAILURE MODE TO WATCH.** If B-2's uniform bound leaves a large residue, do NOT reach for a
Z-dependent fit to shrink it. Walk the residue, or derive the envelope. A fitted envelope
would put a constant into a chain whose only entered number is c = 137.035999.

---

## STANDING

Neither instrument touches the sealed chain. Both are reads plus, at most, a residue walk.
Both must be predicted before they are run. Whichever answer the count returns is the ruling.