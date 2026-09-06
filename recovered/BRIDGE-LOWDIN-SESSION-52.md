# BRIDGE — LOWDIN SESSION 52 · DELIVERABLE 1 WRITTEN, CLAUSE 2 CLOSED, CLAUSE 3 ARMED

Open Session 53 with **`bash pack52/open52.sh`** and nothing else. It differs from
open51.sh only in that **gate 86 joins the smoke list** and step 5 names the pack52
reference log. The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 52 DID

Searched the outside literature for attributions, wrote **Deliverable 1**, and closed
Löwdin clause 2 from the sealed data. Built and verified the clause-3 instrument but did
NOT run the walk — see §5.

    ORDERING CLAUSE     0 failures in 119 steps      unchanged
    DERIVATION          107 rows, Z=2..108           unchanged
    CLAUSE 2            CLOSED this session
    CLAUSE 3            instrument built, verified, prediction filed, NOT RUN

---

## §2 · THE ATTRIBUTION LEDGER — AND WHERE THIS WORK STANDS

`ATTRIBUTION-LEDGER-LOWDIN.md`, 26 entries, all fetched this session, with entries known
only through a citing source flagged [SECONDARY] per §H.6.

**The finding that matters: the reference derivation has already been rejected on OUR
ground.** Thyssen & Ceulemans (2017, p.381) state the Demkov-Ostrovsky results, though
correct, cannot be considered a solution of the Löwdin challenge, because the effective
potential WAS GUESSED. Kitagawara & Barut (1983, 84) had found flaws in the DO logic.
Every family-B descendant inherits this. Allen & Knight (2002) instead READ the ordering
off Desclaux's 1973 Dirac-Fock tables. Aruna Kumar (2026, arXiv:2606.17359, read in full)
reproduces the sequence but fixes its orbital label by minimising its own spectrum, and
disclaims many-electron status.

**This work stands at neither joint: the field is computed at each atom from nuclear
charge alone, and the entrant is predicted before it is scored.** That distinction is
now written down, which it was not before this session.

---

## §3 · CLAUSE 2 CLOSED — THE TWO COLUMNS ARE TWO OBJECTS

Scored against `PREDICTION-DELIVERABLE-1.md` (e19fc0a2…, filed before the chain was read).
Four clauses held, D1-3 FALSIFIED, D1-5 half. **The falsification is the finding.**

I predicted ok-failures would be a subset of cfg-failures. They are not. The sets are
almost DISJOINT: 34 cfg-failures, 11 ok-failures, overlap of THREE (47, 96, 103).
Thirty-one steps carry a correct differentiating electron and a wrong total
configuration; eight carry the reverse. gate 83's `disagree` = 39.

**And the structure is exceptionless and one-directional.** Every one of the eleven
ok-failures is immediately preceded by a cfg-failure at Z-1 -- all eleven. The converse
fails at 23 of 34. Reading: the entrant is wrong exactly where an EARLIER PROMOTION IS
BEING UNDONE, the observed atom refilling an s orbital the one-electron walk never
emptied. The ok-failures are RECOVERY STEPS, not independent failures of the rule.

**Therefore the derivation governs the DIFFERENTIATING ELECTRON.** Löwdin clause 2 is
answered by measurement rather than argument, reaching Scerri's and Schwarz's conclusion
by a different route and giving the promotion structure a scored form neither states.

**Gd(64) is the specimen.** Correct total configuration, wrong differentiating electron.
It splits the 4f promotion run into 59-63 and 65-70. Had the two columns been one
measurement with two error rates, Gd could not exist. A draft of Deliverable 1 wrote the
run as "59-70"; the check caught it and **the text was corrected, never the data.**

---

## §4 · DELIVERABLE 1

`DELIVERABLE-1-THE-ORDERING-CLAUSE.md`, sha256 2f353ed6af…. Seven sections: the claim;
the prior art and the joint; the ordering clause; the tie-break clause with its computed
collapse domain and the explicit refusal to cut kappa on a value; clause 2 per §3 above;
clause 7's three-way partition of every known anomaly with NO RESIDUE CLASS; and what is
owed. **Gate 86 (`gate86.py`) locks 19 numeric claims** and can-fails in both directions
(wrong count; inverted Gd claim).

---

## §5 · CLAUSE 3 — ARMED, NOT FIRED, AND WHY

The field is scalar-relativistic; the challenge specifies the non-relativistic
Schrödinger equation. This is the largest remaining exposure and M ruled it FIRST.

**The instrument exists and is verified.** `c` is a DEFAULT ARGUMENT on eigen_sr,
numerov_wf_sr and scf_occ_sr; c=1e6 is this project's established non-relativistic limit,
already used as a build gate. `pack52/cinf.py` rebinds those defaults in memory --
**NO SEALED FILE IS TOUCHED** (F44.1 precedent). Verified in the strongest available
form: at Z=80 the patched kernel returns **-3200.00001601 against the exact
non-relativistic Coulomb -3200.00000000** (1.6e-5), while the SR field gives -3532.188.
The limit is real, not a no-op. Single-row walk at Z=24 completed: ent=3d, 44.9 s.

**NOT RUN, and the reason is stated rather than glossed.** 107 rows x ~45 s is ~80
minutes. A detached job does NOT survive a chat handoff -- the F49.2 remedy covers
tool-call timeouts WITHIN a session, not across sessions. Launching at this session's
context limit would have destroyed the run, not preserved it. The instruments were
sealed instead.

`PREDICTION-NONREL-CINF.md` (56c8dd6c2c…) was filed BEFORE any c=1e6 row was computed.
Six clauses, NR-1 decisive: zero ordering failures at c=1e6 over Z=2..108. NR-2 states
the falsifying outcome explicitly -- if {57, 89, 90} VANISH at c=1e6, Deliverable 3's
collapse condition is entangled with the relativistic layer and Deliverable 1 §3 reopens.

---

## §6 · FAULTS

**F52.1 — A STALE COUNT INSIDE A SEALED RULING.** Bridge 51 §7 declares
`ok=1034 bad=0 extra=0` "from a fresh extract". The instrument reports **1038**. Nothing
is missing: M51 = M50 (1018) + 20 files, all accounted for; the 1034 was read before the
last four entered the manifest (the bridge, its pack copy, verify51.sh, MANIFEST-50).
Benign in content, but it is a NUMBER QUOTED AS EVIDENCE that disagrees with the
instrument that produced it. **Counts from the instrument: 1038.** The sealed file was
NOT edited; the correction lives here. Class: R 1643's "counts from the instrument",
arriving in a bridge rather than in a chat.

**A near-miss worth recording.** I first scored the cfg column with a comparison I wrote
myself (raw string equality), which returned 107/107 and contradicted gate 83's 73/107.
The sealed comparator normalises to a multiset (F42.2). Caught by the contradiction, not
by inspection. **The lesson is R 1671's: an instrument you build to check a sealed result
must be reconciled against the sealed one before it is believed.** No fault registered --
nothing was written or read downstream from the wrong number.

---

## §7 · GATES

Gates 1..71 replayed from a fresh extract at open: **283 lines, 71 rc=0, diff to ZERO
lines** against pack51's reference, gate 6 `sec` excluded. Seven smoke gates PASS
(83, 84, 85, and the four kernels). **Gate 86 NEW, PASS, can-failed both directions.**
verify51.sh at open: ok=1038 bad=0 extra=0, both halves can-failed.

---

## §8 · ORDERED WORK LIST FOR SESSION 53

1. **`bash pack52/open52.sh`.** Expect gate 83 (73,107)/(96,107), gate 85 PASS,
   **gate 86 PASS**.
2. **FIRE CLAUSE 3, FIRST THING, DETACHED.** Everything is pre-built and the prediction
   is already filed, so this needs no setup:
       cd rt && bash run.sh CINF 'python3 ../pack52/cinf.py walk 2 108 /tmp/cinf.jsonl'
   ~80 min at ~45 s/row; poll with `run.sh --wait CINF 600`. Rows append and flush per
   step, so a timeout costs nothing -- resume at the last unreceipted Z. **Launch it
   BEFORE any other work so it runs underneath the session.**
3. **Score against PREDICTION-NONREL-CINF.md.** NR-1 decides whether clause 3 closes.
   Report the outcome whichever way it falls; NR-2's falsifying branch reopens
   Deliverable 1 §3.
4. **Then clause 1** — the reverse derivation chain, Schrödinger -> the field solved,
   each approximation named and its effect on the ordering bounded. It CANNOT close
   before clause 3, because the relativistic link is the one that needs the c=1e6 result.
5. Deferred: the transit width; the -8.021 mHa residue at Z=59; the coupled 4f2.5d SO
   check; the promotion operator as an object.
6. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s52.