# BRIDGE — THE LÖWDIN SESSION 47 (2026-08-19)
Successor to BRIDGE-LOWDIN-SESSION-46.md. Bank restore-point-2_13 (R 1700) UNCHANGED.
HANDOFF-46 verified at open **ok=965 bad=0 extra=0** (both halves; can-fail exit 1).
Gates 1-71 + PT8: **283 lines, diff = 0** against sealed GATES-46-OPEN.log (`sec` excluded).
72,73 SKIP. 77: **55 scored, 0 UNSAFE**. 78: **50/55, FIRST DIVERGENCE 25**. 79+80 PASS,
14 clauses. 81 PASS. 83 RESTATED for 55 rows and PASS 8/8. **84 NEW, ADOPTED, PASS 6/6.**
**Z=57 (La) RUN. THE OPENING PREDICTION HELD. THE COLLAPSE PREDICTION FAILED.**

## 1 · Rulings (M, s47)
(1) "**Continue**" ×2 — proceed through the order without further confirmation.
(2) "**Run**" — take La ahead of sealing. **Executed, but not before PREDICTION-OPENINGS was
    filed**: §4(b) is binding and a ruling on ORDER is not a suspension of R 1449. Stated to M
    at the time rather than resolved silently.
GENERAL carried: SUBCELL=1; predictions before runs; R 1449 flags; comparison decides; no
scans; no constant beyond c; residue is not closure; T4 LAST; the n+l walk is the solution
format; a margin never quoted without its channel (F44.2); a gate is a script that can return
non-zero (F44.1); a gate whose expectation GROWS WITH THE CHAIN must say so in its own text.

## 2 · Findings (pack47)

(1) **F46.1 CLOSED — IT WAS AN ARTEFACT, AND THE MECHANISM IS NAMED.** D_6p(54) = +0.11105 is
    not a channel energy. At the ruling β=0.4 the (Z=54,+6p) SCF enters a **limit cycle** —
    100/300/600 iterations give +0.11105/+0.11190/+0.11190, identical at 300 and 600 to six
    decimals, so it orbits rather than drifts. At β=0.2 it **converges in 72 iterations** to a
    total energy 0.19 Ha lower: **D = -0.08192**, which is exactly the 0.19 Ha the fault was
    named for. The repaired value lies on the trend: -0.07617 (52), -0.07922 (53), **-0.08192
    (54)**. 6p never unbound and never left the ladder. **The sealed Z=54 row stands** — 5p
    wins at -0.42783 against -0.08192 as comfortably as against +0.11105.

(2) **F47.2 — THE INSTRUMENT DEFECT, AND IT IS REAL.** `hfc2.run2` breaks on `dmax<tol` but
    **returns unconditionally at maxit with no error and no flag**. The node check raises;
    non-convergence does not. `nlchain.jsonl` stores `it_ref` but no per-channel `it`, so the
    record **could not have caught this from sealed data** — it required a re-run. This is the
    class s46 withdrew two false instances of. This one survives its test.

(3) **THE 5d COLLAPSE AT Ba(56) IS REAL — RE-TESTED, NOT ASSUMED.** s46's finding (4) was
    scored off the same instrument, so it was tested the same way: D_5d(56) = **-0.11818 at
    both β=0.4 (35 it) and β=0.2 (74 it)**, identical to five decimals, nowhere near the
    cycle. It is not an artefact. Class scan of all 55 sealed rows: exactly two positive D
    anywhere — 6p(54), now explained, and **6d(51) at +0.00215, marginal, non-competing,
    NOTED NOT CLOSED**.

(4) **GATE 84 ADOPTED — THE GUARD, TESTED IN BOTH DIRECTIONS.** Rung ladder (β,maxit) =
    (0.4,100) → (0.2,600) → (0.1,1200). **Rung 0 is the ruling field unchanged and is tried
    first, so every converged sealed number returns bit-for-bit.** β is a damping, not a term
    in the Hamiltonian — evidenced, not asserted, by (3)'s damping-independence. The gate
    tests one value the field gets RIGHT and must not disturb (5d56, rung 0) and one it gets
    WRONG and must repair (6p54, rung 1). **A channel that converges at no rung returns NO
    NUMBER and joins `fail`** — returning the last iterate at lower β would move F47.2, not
    repair it. PASS 6/6 exit 0; `--fail` exit 1, 3 clauses.

(5) **F47.3 — THE GUARD'S OWN COST, REGISTERED.** A step computes ONE reference and MANY
    channels, so once any channel takes rung 1, D is **mixed-rung by construction**. Measured:
    E_ref = -7443.962951 (rung 0) vs -7443.962945 (rung 1), 6e-6 apart, **both converged
    inside tol=2e-6**. D_6p(54) is therefore -0.081930 same-rung and -0.081924 mixed-rung, and
    at five stored decimals that crosses a rounding boundary. **A guarded D carries ~1e-5 of
    rung-mixing uncertainty in its last stored digit** — four orders below the 1e-2..1e-1
    margins the chain decides on, so it cannot flip an ordering. Gate 84 expects the MIXED
    value because mixed is what the chain produces.

(6) **Z=57 (La) RUN, GUARDED. ENTRANT 5d, ok=True, margin +0.06756 over 6p (F44.2).**
    All channels converged at **rung 0** — the guard was needed nowhere at 57, which is itself
    the result that the ordering below is not guard-dependent. 104 s.

        5d -0.20585 | 6p -0.13829 | 4f -0.10556 | 7s -0.07085 | 7p -0.05126
        5g -0.02000 | 6g -0.01389 | 7g -0.01021
        FAIL (node count, not convergence): 5f, 6d, 6f, 7d, 7f
    Consistency witness: 5g/6g/7g return -1/50, -1/72, -1/98 to five decimals — exactly
    hydrogenic, i.e. unpenetrating. The instrument is behaving.

(7) **PART 3'S FIRST TEST PASSES: THE RULE IS WRONG AT La AND THE FIELD IS RIGHT.**
    4f and 5d both carry n+l = 7; clause 2 (smaller n first) names **4f**; the record and the
    field both name **5d**. This is the first of the record's two disagreeing openings and the
    first step in 57 where rule and field diverge. **The n+l tie-break's unbroken run breaks
    here, on its fifth pair, and breaks for a stated reason rather than by exception.**

(8) **AND THE COLLAPSE ARRIVED ONE PROTON EARLY, ON 4f, AT La — NOT AT Ce.**
    D_4f: -0.03136 (56) → **-0.10556 (57)**, a step of **-0.07420 = 824× the largest step in
    the sixteen-element flat baseline**. Zeff 1.001758 → **1.837912**. **The MECHANISM is
    confirmed and the PLACEMENT is refuted**: PREDICTION-4f-COLLAPSE §1 said departure from
    Zeff=1 is *discontinuous, not gradual*, and Zeff jumped straight past the 1.05–1.25 window
    the file named as its own falsifier for gradualism. The double-well account survives its
    own test while the step it was pinned to fails.

## 3 · SCORING — BOTH FILES, SCORED AS FILED

**PREDICTION-OPENINGS (filed this session, before the run):**
- **PO-1 clause HELD** — ent=5d, ok(57)=True. **PO-1 BAND FAILED**: filed [-0.20,-0.12], got
  **-0.20585**, outside by 0.006. The band was already widened below in anticipation of a
  second discontinuous step; it went deeper still. Clause and band scored separately as the
  file required.
- **PO-2 HELD** — rule names 4f, field names 5d, rule WRONG and field RIGHT at the same step.
- **PO-3 HELD, clause and band** — 6p not entrant; D_6p(57) = -0.13829, inside [-0.16,-0.10].
- **PO-4 BAND FAILED** — filed [-0.045,-0.031], got **-0.10556**. Its separate falsifier
  (4f within 0.02 Ha of 5d) did **not** trigger: the gap is 0.10029.
- **PO-5 HELD** — 5d's 56→57 step is -0.08767, larger than Ba's -0.05345, so it did not return
  to the ~0.001/proton régime. The transfer that began at Ba continues through La.
- **PO-6 HELD** — no constant, threshold or sweep entered at or near 57. Only c = 137.035999.

**PREDICTION-4f-COLLAPSE (filed s46):**
- **PC4F-2 FAILED — and it was declared THE LOAD-BEARING CLAUSE.** Filed: Zeff(57) inside
  [1.000,1.010]. Got **1.837912**. Failed by 83×.
- **PC4F-3 clause HELD** (ent=5d, ok=True); **band FAILED** as s46 logged in advance.
- **PC4F-4 HELD** — the tie-break breaks at La, as filed.
- **PC4F-6 FAILED** — filed first Zeff-1 > 0.01 in {58,59}; it is **57**, and the file names
  any Z ≤ 57 as its falsifier.
- **PC4F-5 NOT YET SCORABLE** (58 unrun) but its premise — collapse *arrives* at Ce — is
  already contradicted at 57.
- **§3's ENTIRE-ITEM FALSIFIER IS TRIPPED**: "collapse at or before 57". **Logged, not
  suppressed.** The mechanism (§1) survives; the item's placement does not.

**THE SHAPE OF THE RESULT, STATED PLAINLY: the mechanism prediction failed and the law
prediction held.** 4f collapsed a step earlier than filed, and the opening still went to 5d,
because 5d had collapsed first and by more. Part 3 is not damaged by PC4F-2's failure — it is
*confirmed* by it, since an early 4f collapse that still loses the opening is stronger evidence
that the opening is decided by 5d than a late one would have been.

## 4 · Faults registered this session
**F47.1 — README-HANDOFF-46.md IS BYTE-IDENTICAL TO README-HANDOFF-45.md.** The s46 README was
  never written; the s45 recipe travelled under an s46 name and self-identifies as HANDOFF-45
  in its first line. Four clauses were stale: layering `19..45` (correct: **19..46** — would
  have loaded pack45's 53-row nlchain.jsonl as terminal and **silently lost Cs and Ba**);
  `verify45.sh`; gate 83's expectations as (45,53)/(48,53); the diff target. **Caught because
  the session ran from the BRIDGE, which was accurate on every point the README was stale on,
  and because the row count was CHECKED at layering rather than assumed.**
**F47.2, F47.3** — see §2(2) and §2(5).
**MY FAULT: I violated F42.2 in my own first diagnostic**, rebuilding the reference config by
  re-parsing `ref_cfg` instead of through `nlchain.add`. Shell order is load-bearing and the
  solver raised inside `solve_one`. Caught by the crash, not by reading the fault I had just
  quoted in the session open. Repaired to `NC.cfg_from_chain`. **Second instance this project
  of a registered fault being committed by the session that recited it.**
**AND A READING FAULT: I twice reported `$?` from a piped `tail`, not from the gate.** F44.1
  requires a gate's real exit. Re-read unpiped: gate 84 exit 0, `--fail` exit 1. The earlier
  "RC=0" lines in this session's transcript are `tail`'s and mean nothing.

## 5 · Next chat, in order
(1) **DECIDE WHETHER Z=57 IS APPENDED TO nlchain.jsonl.** It is computed but **NOT SEALED** —
    `pack47/Z57-CANDIDATE-ROW.json`, flagged UNSEALED-CANDIDATE. It was produced by
    `nlstep47.py` (guarded) rather than `nlchain.py`, so appending it mixes instruments in one
    file. **M's ruling owed.** Cleanest route: re-run 57 through `nlchain.py` with the guard
    wired into `step()`, confirm it reproduces §2(6) exactly, and let the chain write its own
    row. Gate 83 and 78 must then be restated for 56 rows.
(2) **RUN Z=58 (Ce).** Scores PC4F-5. 4f is already collapsed, so the record's 4f1 5d1 6s2 is
    now a **test of whether the walk can place a SECOND channel** — a different question from
    the one s46 filed.
(3) Wire the guard into `nlchain.step` and add per-channel `it`/`rung` to the stored row, so
    F47.2 cannot recur unobserved. (4) 6d(51)'s +0.00215. (5) Extend Z=59..108 in Zeno
    segments. (6) Name the channel failures via t7g_exc.HFCN — 5f/6d/6f/7d/7f all fail on node
    count at 57. (7) The PROMOTION OPERATOR — M's ruling not yet given. (8) PV-3.
    (9) Z=109..120. (10) Reverse derivation to Schrödinger. (11) T4 LAST: R 1701-1966.

## 6 · Figures (§H.6)
MEASURED: the Z=57 ordering and every D in §2(6); D_6p(54) at four (β,maxit) settings;
D_5d(56) at two. DERIVED: Zeff from Zeff=sqrt(-32D); all steps and margins.
RECALLED-NOT-ENTERED: La(57)=[Xe]5d1 6s2, Ce(58)=[Xe]4f1 5d1 6s2, and the record's 19 subshell
openings with its two disagreements. CHOSEN: unchanged from s46 (seed, candidate rule, grid
4000/2e-5, qtail 1/2, frozen avg-of-config, **HF β=0.4 maxit=100 — now rung 0 of the guard,
unchanged as the ruling field**). **No constant entered beyond c = 137.035999.**

## 7 · Files (pack47)
nlguard.py (gate 84) · nlcfg.py (gate 83 restated for 55 rows) · PREDICTION-OPENINGS.md ·
nlstep47.py · f461_diag.py · f461_close.py · f461_5d56.py · Z57-CANDIDATE-ROW.json ·
GATES-47-OPEN.log · CENSUS-SESSION-47-OPEN.txt · gates_run47.sh · this bridge.
**OWED TO s48: gate 83 restated AGAIN if Z=57 is sealed — (48,56)/(51,56) if La passes both
columns. Gate 84's expectations are chain-length-INVARIANT and must not drift.**

## 8 · Unread / owed
Unchanged (R 1668; Dabo 2010, Borghi 2014; 2603.23283; Grüneis-Kresse 2009 / Ren 2013).
Owed: T4; PR3; PN-3; La 4f+corr; PN4 s' channels; PV-3; the promotion operator; the node-count
channel failures; 6d(51); **PREDICTION-OPENINGS again before Z=89 (this file does not cover
Ac)**; the Z=57 sealing ruling.
Known: bash egress DENIES network. Known: ground.py caps at Z=108 (R 1426).
Known (F40.1): nlchain's reference is the previous NEUTRAL's configuration on the CURRENT
nucleus. Known (F42.2): build configs via nlchain.add — shell order is load-bearing, and I
broke this again this session.
Known (F44.2): `margin` does not name its runner-up — read `order[1]`.
Known (F44.1): read a gate's exit code UNPIPED.
Known (F45.1): the gate recipe's sed targets a SESSION-NAMED COPY at the ARCHIVE ROOT.
Known (F47.1): **do not trust README-HANDOFF-N's header — check it against the bridge.**
