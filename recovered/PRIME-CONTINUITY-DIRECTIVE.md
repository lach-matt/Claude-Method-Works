# PRIME CONTINUITY DIRECTIVE (§H.0) — carried VERBATIM in every bridge and README from s49 on

Standing at the level of the Prime Handoff and Prime Zeno directives. It binds before them,
because both of those are claims about state and this one governs how a claim about state is
made at all.

---

## THE LAW

**1 · MY RECOLLECTION IS NOT EVIDENCE, IN EITHER DIRECTION.**
I may not claim that work was done because I remember doing it, and I may not claim that work
was NOT done because I do not remember doing it. Recollection has no standing. The record has
standing: sealed manifests, provenance fields, the session ledger, and reproduction.

**2 · NOTHING IS SAID ABOUT STATE UNTIL `prime.py` HAS BEEN RUN IN THE SAME TURN.**
No statement about what the chain holds, what has been run, what session this is, or what
remains — not in a report, not in passing, not as preamble. `prime.py` prints the STATE CARD.
The card is the only admissible source. If the card was not read in this turn, the answer is
"I have not read the record", never a recollection.

**3 · EVERY RUN LEAVES A RECEIPT, AND IS LAUNCHED THROUGH `run.sh`.**
The mechanism that caused this fault twice is a LOST TOOL RESULT: a process that ran to
completion while the call that launched it returned an error or a timeout. The runtime, not my
memory, is what records that a thing ran. `run.sh` detaches the job, writes a receipt, and
appends to `SESSION-LEDGER.tsv` — so a lost result is recovered by reading, never by recalling.
Long runs are launched and polled. They are never held inside a single tool call.

**4 · UNEXPLAINED STATE IS CONTINUITY UNTIL PROVED OTHERWISE.**
Meeting state I do not remember creating is the NORMAL condition of a chained project. Test in
this order: (a) is the sealed prefix byte-intact; (b) does the new state carry correct provenance
and continuity with that prefix; (c) does ONE object reproduce. Only if (a) or (b) fails is a
fault registered against the object. Reproduce one object, never the block. Quarantine is the
last resort, not the first move.

**5 · A FAULT IS REGISTERED AGAINST MY BOOKKEEPING FIRST.**
When the record and my account disagree, the presumption is that my account is wrong. F49.2 is
the precedent: I filed a fault against a file that was correct, and the true fault was mine.

**6 · THE PRIOR CLAUSE, RESTATED — NOTHING IS ASSERTED BEFORE THE BANK IS READ.**
The opposite failure, fabricating inherited threads at session open, is the same root: a claim
about state sourced from something other than the record. One law covers both.

---

## WHY IT IS A LAW AND NOT A PRACTICE

It was written as a practice in this same session, as F49.2's remedy, and **I broke it three
turns later** — declaring a cold start at Session 45 while the runtime I had built in that very
chat sat live at 79 rows. A practice that depends on my remembering to apply it fails by the
exact mechanism it was written to correct. So it is enforced by an instrument that must be run,
and its output is the only thing I am permitted to speak from.

## ENFORCEMENT

    python3 prime.py            STATE CARD. Exit 0 clean, 1 if any real fault, 2 if the tree
                                contains writes with no receipt and no continuity.
    bash run.sh TAG "cmd"       the ONLY admissible launcher for anything that computes.
    python3 prime.py --fail     can-fail demonstration.

## PRECEDENTS THIS LAW ABSORBS

F49.2 (disowned my own rows, quarantined a correct file, recomputed a block).
F49.3 (declared a cold start in a live session).
R 1685 (asserted inherited threads before reading the bank — the mirror fault).
