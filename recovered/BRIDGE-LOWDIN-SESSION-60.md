# BRIDGE — LOWDIN SESSION 60 · CLAUSE 3 IS CLOSED

Open Session 61 with **`bash pack58/open58.sh`** and nothing else. ~2 s.
The only number ever entered into this chain remains **c = 137.035999** — and s60 showed
the answer does not depend on it.

**THE ROOT IS NOT QUOTED HERE (s59 precedent). IT LIVES IN THE BODY OF LINEAGE.txt.**
Trust the BODY, not the footer (F59.5, still unfixed — see §5).

## §0 · ENVIRONMENT FACTS — DO NOT REDISCOVER
1. `nohup ... &` does NOT survive the tool-call boundary. FOREGROUND only (F59.2).
2. `time` is not in this shell. Use `date -u +%H:%M:%SZ`.
3. Row costs measured s60: Z=88 **270 s** (one call failed at first attempt, succeeded on
   retry), Z=87 132 s, Z=56 125 s, Z=38 97 s, Z=55 79 s, Z=20 55 s, Z=37 50 s, Z=19 44 s,
   Z=12 27 s, Z<=11 3-11 s. **Rows below Z=40 batch safely 3-5 per call.**

## §1 · WHAT CLOSED — CLAUSE 3, AT 107/107
`pack60/SCORE-EXPOSED-13.md`. Prediction sha verified 6a04409318b8881c BEFORE any row read.
EX-2 read first, as filed: PASS (shift rises monotonically 0.00002 Ha at Z=2 -> 0.04935 Ha
at Z=88; no zero above Z=20 — the instrument is live).
**EX-1 HOLDS 13/13. Every entrant at c=1e6 is the entrant at c=137.035999.**
94 rows immune combinatorially (F55.2) + 13 walked at c -> infinity = **107/107.**
**The ordering clause is not a relativistic effect anywhere it could be one.**

EX-3 did not fire; its ranking is superseded (tightest at c=1e6 is Z=88 at 0.00881, not
Z=56). EX-4 is PARTIAL — holds 4 of 5 within-atom pairs, **FAILS at Z=19**, not reworded.

## §2 · THREE FAULTS, ALL REGISTERED AND CLOSED
    F60.1  Z=88's runner-up CHANGES IDENTITY (7p -> 6d) when c -> infinity. The 0.04935
           "narrowing" is not the 7p channel moving. F44.2's exact trap, caught this time.
           **AND 6d/7p both carry n+l=8** -- the only order change relativity's removal
           produces anywhere in the exposed set is WITHIN-SHELL, inside the immunity class
           the theorem already excludes. Deliverable 1 / D5 §1 STRENGTHENED.
    F60.2  pack53/induct.jsonl + pack54/induct34.jsonl: FAULTED, **PROVEN not presumed.**
           Receipt A: induct.patch(1e6) -> HFSR(2).c = 137.035999, unmoved (3 sites, not 4).
           Receipt B: all 55 cinf-chainref rows are BYTE-IDENTICAL in every eigenvalue to
           the sealed chain rows (21 rows Z=25-80; 34 rows Z=25-104). They are a bit-for-bit
           duplicate of nlchain.jsonl and carry ZERO information. Void as c-statements.
           **No hole opens: Clause 3 closed by the genuine route the same session.**
           UNPLANNED POSITIVE: 55 cold recomputations by a different driver in two sessions
           reproduce the sealed chain to the last digit at Z=25-104. Strongest determinism
           result the chain has. Files RETAINED as evidence, not deleted.
    F60.3  A flag raised on my OWN result and closed at zero solve cost. cinf2 rows use the
           RESTART reference (G.expand(Z-1), observed); the baseline is the CHAINED walk.
           Different constructions -> F44.2/F59.1 again if unchecked. **CHECKED: identical
           at 13/13.** The two sides of EX-1 differ in c AND IN NOTHING ELSE.

## §3 · M'S RULINGS THIS SESSION — `pack60/RULINGS-s60.md`
1. **ADOPTED: search the archive by content before declaring a gap.** STANDING RULE 6 IS
   NOW RATIFIED and binds prospectively. Paired with s59 §7.7: **search before you declare
   a gap; can-fail before you declare a control.**
2. **Name the restart reference, and can-fail CORR.** Both discharged — see §4.

## §4 · CLAUSE 1 IS OPEN AND HAS A SPINE — `pack60/CLAUSE-1-LADDER.md`
Eleven rungs from the exact many-electron Schrodinger equation to what `nlchain.step`
solves, each with a file:line receipt and a class (DERIVED / NUMERIC / APPROX / INPUT / OFF).

**DONE as of s60:**
  Rung 1  RELATIVITY -- discharged BY §1. The ruling field is MORE than Rung 0, not less;
          at c -> infinity it reduces, and the entrant does not move. **The largest single
          thing Clause 1 needed from the walk is in hand.**
  Rung 6  CORRELATION -- **OFF, AND PROVEN OFF.** `pack60/corrcheck.py`, PASS in three
          directions on the walk's own path (nlguard.run_guarded -> HFC.run2), 17:15Z:
          CORR=False -> 0 calls; CORR=True -> 27/30 calls and dE = +0.26/+0.43 mHa;
          CORR=False again -> BIT-IDENTICAL to phase 1. The script REFUSES to pass if the
          switch changes nothing (F59.3's signature). This matters because the branch is a
          Gell-Mann-Brueckner functional whose coefficients are NOT derived in this chain.
          It is carried by ONE line: nlchain.py:17. hfc2.py:11 DEFAULTS IT TRUE.
  Rung 8  THE REFERENCE -- NAMED. **CHAINED = DERIVED, empirics-free, the mode the solution
          is claimed in. RESTART = INPUT: it reads the OBSERVED config.** Restart rows are
          admissible only for controlled comparisons where the empirical reference appears
          identically on both sides and cancels; INADMISSIBLE as evidence of derivation.
          Any future statement on restart rows must declare which it is.
  Rung 10 THE ENTRANT CRITERION -- a Delta-SCF TOTAL-ENERGY difference, not an eigenvalue.
          This is what answers Löwdin's "filling ambiguity": the differentiating electron.
  CONSTANT LEDGER -- no screening constant, no ionization energy, no fitted parameter at
          any rung. alpha=2/3 is derived AND seed-only.

**OWED, IN PRIORITY ORDER (this is the s61 work list):**
    1. **Rung 3/4 SEED-INDEPENDENCE (warm-start) against the ORDERING.** Highest value on
       the board. "Exchange is exact HF and the KS form is seed-only" is worth NOTHING
       until a converged SCF is shown to forget its seed. Also settles whether run2 applies
       the Latter clamp at all -- UNVERIFIED, do not assert either way.
    2. **Rung 7 the CONVERGENCE FLOOR for the restart walk. MEASURE IT BEFORE anyone uses
       "numerical" to explain EX-4's Z=19 failure.** That excuse is pre-emptively barred.
    3. Rung 5  classify `_ceff` (t7b_hf.py:105): DERIVED or INPUT.
    4. Rung 9  defend the candidate-space truncation (l <= 4, n <= N+1).
    5. Rung 2  bound the single-configuration approximation on the ordering.
Then: Rung 0 assembly -- the written reverse chain itself.

## §5 · CARRIED OPEN INTO s61
    F59.5   LINEAGE.txt's SUMMARY FOOTER is stale (condense.py writes the BODY correctly).
            Cosmetic, no physics, no hash. NOT FIXED -- fixing it means editing a sealed
            file. **TRUST THE BODY.** s61 may remedy via the F44.1 route or rule it cosmetic.
    EX-4 Z=19 failure; the restart-walk convergence floor (both are §4 item 2).
    Deferred, unchanged: -8.021 mHa residue at Z=59; coupled 4f2.5d SO check; the promotion
    operator as an object; the 2.88 mHa residue of s56 §5.
    **T4 (R 1701 onward) -- LAST.**

## §6 · STANDING
1. Open accepts the handoff. History is NOT re-verified. Canary DRIFT -> full replay.
2. Condense at every seal: `python3 pack58/condense.py N --seal`.
3. Retirement is declared. Undeclared removal HALTS the seal.
4. Never sed a verify script.  5. Surveys return counts, sets, diffs.
6. **RATIFIED s60: search the archive by content before declaring a gap.**
7. A control must be proven to vary the thing it controls for, BEFORE it is used as a
   control. A prediction whose falsifier cannot fire is not a prediction.
8. **NEW s60: a comparison must be proven to hold its reference fixed before any
   difference is attributed to the variable under test (F60.3, F44.2, F59.1 -- three
   sessions, one failure mode).**

Bank restore-point-2_13 (R 1700) untouched throughout s60.

SEAL: s60, 1053 files. Fresh-extract verified CLEAN (1053/1053, root MATCH).