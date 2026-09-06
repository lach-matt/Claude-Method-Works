# BRIDGE — LOWDIN SESSION 59 · THE c=1e6 WALK WAS NEVER AT c=1e6

Open Session 60 with **`bash pack58/open58.sh`** and nothing else. ~1 s.
The only number ever entered into this chain remains **c = 137.035999**.

---

## §0 · READ THIS BEFORE ANYTHING ELSE

**EVERY FACTUAL CLAIM BELOW ABOUT THE ARCHIVE CARRIES ITS RECEIPT — the command that
produced it. s59 lost calls because the s58 bridge asserted an archive fact
("Cost: a read, not a solve") that was false. Do not trust a bridge claim about file
contents without the receipt. This one is written so you never have to.**

**ENVIRONMENT FACTS THAT COST s59 CALLS — do not rediscover them:**
1. **`nohup ... &` DOES NOT SURVIVE THE TOOL-CALL BOUNDARY.** A detached 5-row run
   produced no rows, no log, no progress file, and cost ~3 min. **Run long work in the
   FOREGROUND, one row per call** (F59.2). A single row is 90-100 s and returns fine.
2. **`time` is not present in this shell** (`/bin/sh: 1: time: not found`). Use
   `date -u +%H:%M:%SZ` before and after.
3. A single `nlchain.py restart <Z>` row costs **~90 s** (measured: 42→96 s, 43→92 s,
   45→89 s, 46→87 s, 79→100 s).

## §1 · THE FAULT — F59.3, BLOCKING, AND IT VOIDS A SEALED DATASET

`pack53/cinf.jsonl` is labelled `"clight": 1000000.0` on all 107 rows. **It was computed
at c = 137.035999.** The label is false.

`cinf.py` sets c by rebinding the `__defaults__` of `eigen_sr`, `numerov_wf_sr`,
`scf_occ_sr`. The HF solve never reads those defaults:

    t7c_hfsr.py:6    from t7c_kernel import qlog, eigen_sr, _derivs, C0
    t7c_hfsr.py:8    def __init__(self, Z, occ, npts=4000, c=C0, srcM=True)
    t7c_hfsr.py:39   eh = float(eigen_sr(Vf, l, n, 1.0, self.Z, c, Vp=..., Vpp=...))

`C0` is bound into t7c_hfsr AT IMPORT; `HFSR.__init__` has its OWN default `c=C0`; line 39
passes it POSITIONALLY. A patched default is unreachable. `hfc2.py:84` likewise
constructs `HFC(Z, occ, c=C0)` explicitly.

**RECEIPT (reproduce in ~2 s):** apply cinf.patch(1e6) verbatim, then instantiate —
`HFSR(2,[(1,0,2.0)]).c` returns **137.035999**, unmoved. Full derivation and the
second, empirical proof are in **`pack59/FAULT-F59.3.md`**.

**WHY THE PROBE GAVE FALSE CONFIDENCE.** `cinf.py probe` calls `K.eigen_sr(V,0,1,1.0,Z)`
with NO c — the one call site that DOES use the default. **The instrument was validated
on a path the physics never takes.** That is the general lesson and it is worth more
than the fault: a control must be proven to vary the thing it controls for, BEFORE it
is used as a control.

**VOIDED:** `pack53/cinf.jsonl` (not a NR walk — a restart walk at c=137.035999);
`pack53/ctrl137.jsonl` as a *c*-control (both sides same c, so CT-1 was true by
construction — **NR-4 CANNOT be released**); DELIVERABLE-5 §4's NR-1/2/4/5 as
*c*-statements. **`pack53/induct.jsonl` and `pack54/induct34.jsonl` (mode
`cinf-chainref`) use the same driver and are PRESUMED FAULTED — NOT YET VERIFIED. OWED.**

**NOT VOIDED, AND THIS IS THE POINT:** the 94/107 immunity theorem is COMBINATORIAL —
which channels share n+l — and depends on no walk and no c. **La(57) and Ac(89) remain
IMMUNE.** Deliverable 1 and Deliverable 5 §1 stand untouched.

## §2 · WHAT CLOSED ANYWAY — THE FIVE NR-1 FLAGS ARE ATTRIBUTED

s58 item 2 asked for the five flags (Z=42,43,45,46,79) to be attributed. **They are —
and NOT by the route s58 named.** Attribution needs two comparisons:

    different c, same reference -> same flag     <-- VOID (F59.3). Never needed.
    same c, different reference -> DIFFERENT flag <-- HOLDS, on pre-existing sealed data

Sealed CHAINED walk: 4d/**5p** (n+l 6/6) at 42,43,45,46; 5d/**6p** (7/7) at 79 — equal
n+l, IMMUNE. Restart walk, same c, same code: 4d/**5s**, 5d/**6s** — cross-n+l, FLAGGED.
**Same c, different reference, different flag. The flag is a property of the reference
configuration.** The five are the s→d promotion format artefact Deliverable 1 names.
Scored in **`pack59/SCORE-NR1-ATTRIBUTION.md`**.

## §3 · CLAUSE 3 — WHAT IS ACTUALLY OWED IS 13 ROWS, NOT 107

Only the 13 EXPOSED rows can reach the ordering clause. All are s-closing; max Z is 88.
**At ~90 s/row this is ~20 minutes — ONE segment, not "several sessions".**

    Z   ent/runner  n+l   margin      Z   ent/runner  n+l   margin
    2   1s/2s       1/2   0.69553     37  5s/4d       5/6   0.07991
    3   2s/2p       2/3   0.06767     38  5s/5p       5/6   0.05639
    4   2s/2p       2/3   0.09634     55  6s/5d       6/7   0.06306
    11  3s/3d       3/5   0.12650     56  6s/5d       6/7   0.03914  <-- tightest
    12  3s/3p       3/4   0.09346     87  7s/6d       7/8   0.06841
    19  4s/4p       4/5   0.05411     88  7s/7p       7/8   0.05816
    20  4s/4p       4/5   0.06058

**RECEIPT:** read from `rt/nlchain.jsonl`, mode `chain`, `order[0]`/`order[1]`.

## §4 · THE INSTRUMENT IS BUILT AND CAN-FAILED — s60 RUNS ONE COMMAND

`pack59/cinf2.py` sets c at all 4 sites (3 kernel defaults + module globals
K.C0/HS.C0/H.C0 + `HFSR.__init__.__defaults__`) and **REFUSES to walk unless
`HFSR(2,[(1,0,2.0)]).c` equals the target.** No sealed file is edited (F44.1 precedent).

**CAN-FAILED 2026-08-20T16:43Z, both directions:**

    BEFORE PATCH  HFSR.self.c = 137.035999          (baseline asserted)
    PATCH OK      sites=4  HFSR.self.c=1000000.0
    Z=42  1s shift 137 vs 1e6 :  -21.7468 Ha
    Z=79  1s shift 137 vs 1e6 : -314.0830 Ha
    CANFAIL: PASS -- c moves the physics

**A patch that changes nothing IS the fault. 314 Ha at gold is the proof it bit.**

## §5 · FAULT REGISTER

    F59.1  s58 bridge item 2 asserted the control for Z=42,43,45,46,79 was already
           sealed in pack53/ctrl137.jsonl -- "a read, not a solve". That file holds
           11 rows: Z=25,30,47,48,60,61,62,71,80,103,104. A content search of all 232
           sealed .jsonl returned ZERO restart rows at the five Z.  REGISTERED.
           I then declared the gap on the strength of the search-before-declaring rule,
           which the s58 bridge itself lists as STILL OWED A RULING FROM M. Acting on
           an unratified premise is my fault, not the bridge's.  See §6 item 4.
    F59.2  nohup/& does not survive the tool-call boundary; ~3 min lost, no output.
           REMEDIED (foreground, one row per call). Recorded in §0 so it is never
           rediscovered.
    F59.3  BLOCKING. cinf.py's c-patch is a no-op on the HF path; the "c=1e6" walk ran
           at c=137.035999.  REGISTERED + INSTRUMENT REMEDIED (pack59/cinf2.py,
           can-failed).  THE 13-ROW RE-WALK IS NOT YET RUN.
    F59.4  My own PREDICTION-NR1-ATTRIBUTION was defective in two clauses: NR1-1's
           falsifier COULD NOT FIRE (it named a control without proving the control
           varied c), and NR1-4 named a field 'rung' that the rows do not carry
           ('rungs'/'rung_ref'). Recorded as prediction defects, NOT as passes.

No fault carried open into s60 except F59.3's unrun re-walk, which IS §6 item 1.

## §6 · ORDERED WORK LIST FOR SESSION 60

1. `bash pack58/open58.sh`. Expect CONDENSE-CHECK CLEAN, CANARY CLEAN.
2. `python3 pack59/cinf2.py canfail` — expect `CANFAIL: PASS`, sites=4, Z=79 shift
   -314.0830. **If this does not reproduce, STOP; the environment moved.**
3. **THE 13 EXPOSED ROWS AT A GENUINE c=1e6.** Prediction ALREADY FILED:
   `pack59/PREDICTION-EXPOSED-13.md` (sha 6a04409318b8881c, 16:44:28Z). Do not re-file.
   **FOREGROUND, ONE ROW PER CALL** (F59.2), ~90 s each:
       `python3 pack59/cinf2.py rows ../pack60/exp13.jsonl <Z>`
   Order: **56, 87, 88, 55, 37, 19, 38, 20, 12, 4, 11, 3, 2** (tightest margin first,
   so a flip surfaces early). Read EX-2 (margins must move above Z=20) BEFORE EX-1.
   **If EX-1 holds at all 13, CLAUSE 3 CLOSES.**
4. **VERIFY OR CLEAR `pack53/induct.jsonl` and `pack54/induct34.jsonl`** (mode
   `cinf-chainref`) — presumed faulted by F59.3, not yet checked. Cheap: same receipt.
5. **M's ruling owed** (s57 §6 item 5, re-owed by F59.1): search the archive by content
   before declaring a gap. **Adopt or reject.**
6. **CLAUSE 1 — the reverse chain to the many-electron Schrodinger equation.**
   Reading DONE (s53 §8 item 5). **The largest owed item in the whole solution.**
7. Deferred: -8.021 mHa residue at Z=59; coupled 4f2.5d SO check; promotion operator as
   an object; the 2.88 mHa residue of s56 §5.
8. **T4 (R 1701 onward) — LAST.**

## §7 · STANDING (s58, unchanged) + ONE ADDED

1. Open accepts the handoff. History is NOT re-verified. Canary DRIFT -> full replay.
2. Condense at every seal: `python3 pack58/condense.py N --seal`.
3. Retirement is declared. Undeclared removal HALTS the seal.
4. Never sed a verify script. 5. Surveys return counts, sets, diffs.
6. Search the archive by content before declaring a gap (STILL OWED A RULING — §6.5).
7. **NEW, from F59.3: A CONTROL MUST BE PROVEN TO VARY THE THING IT CONTROLS FOR,
   BEFORE IT IS USED AS A CONTROL. Can-fail the instrument, not just the result.
   A prediction whose falsifier cannot fire is not a prediction.**

Bank restore-point-2_13 (R 1700) untouched throughout s59.