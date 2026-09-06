# BRIDGE — LOWDIN SESSION 61 · RUNGS 3 AND 4 ARE CLOSED

Open Session 62 with **`bash pack58/open58.sh`** and nothing else. ~3 s.
The only number ever entered into this chain remains **c = 137.035999**.
THE ROOT IS NOT QUOTED HERE (s59 precedent). It lives in the BODY of LINEAGE.txt.
Trust the BODY, not the footer (F59.5, still unfixed — cosmetic, no physics, no hash).

## §0 · ENVIRONMENT FACTS — DO NOT REDISCOVER
1. `nohup ... &` does NOT survive the tool-call boundary. FOREGROUND only (F59.2).
2. `time` is not in this shell. Use `date -u +%H:%M:%SZ`.
3. A driver run from `pack61/` must `sys.path.insert(0, os.getcwd())` and be launched
   from `rt/`. The sealed convention `cd rt && python3 ../packN/x.py` works with that line
   and fails without it.
4. Costs measured s61: one full chain step Z=39 79 s, Z=20 56 s, Z=19 43 s; a perturbed
   seed runs FASTER (fewer channels converge). A fixed-config run2 solve is 3-7 s.

## §1 · WHAT CLOSED — RUNG 3 (SEED-INDEPENDENCE) AND RUNG 4 (LATTER CLAMP)
`pack61/SCORE-SEED-INDEPENDENCE.md`. Prediction sha 192d08537bf28e9e verified BEFORE any
result was read. Filed 17:23:49Z, first result 17:24:48Z. PHASE A ran FIRST and proved the
seed switch live (Standing 7) before any measurement was taken.

**Three seeds: A = sealed TFD/Latter qtail=1; B = same generator, qtail=6; C = bare
Coulomb -Z/r — no TFD, no clamp, no exchange, no screening, no constant.**
A->C moves the STARTING eigenvalues by up to **51.95 Ha**. It moves the CONVERGED total
energy by **0.005 mHa**. A->B moves it by 0.008-0.010 mHa.
**The SCF forgets its seed. "alpha=2/3 is seed-only" is now measured, not assumed.**

    ENTRANT UNCHANGED 3/3 rows, every converging seed:  Z=19 4s, Z=20 4s, Z=39 4d.
    Common-channel agreement <= 0.05 mHa at all three rows.
    Z=39, the 4d/5p TIE-BREAK row: margin moves 0.00001 Ha against 0.04367 Ha. 4000x.

**RUNG 4 CLOSES WITH IT.** s60 said "UNVERIFIED, do not assert either way." Verified now:
`run2` takes qtail ONLY as `self.seed(qtail)` (hfc2.py:40) and builds its own Vloc with no
`min(V,-qtail/r)` (hfc2.py:45,:64). A sixfold tail change leaves the answer at 10 microhartree.
**TFD and the Latter clamp are confined to the seed, and the seed is forgotten.**

## §2 · WHAT DID NOT HOLD — READ THIS BEFORE QUOTING §1
P3's ORDER clause FAILED as worded. The perturbed seeds make weakly-bound channels FAIL TO
CONVERGE and drop out (Z=20: nfail 1->6, and **the dropped 4p was the RUNNER-UP**).
Nothing reorders; candidates vanish.
**The seed does not move the winner. It DOES decide which candidates converge at all.**
The winner survived every seed at all three rows — the most tightly bound channel always
did — but that is an observation at three rows, NOT a theorem. A seed that killed a WINNER
would change the entrant. The sealed seed is the one with lowest nfail (0-2).
**The +0.031 Ha "dmargin" at Z=19/20 is the arithmetic of a vanished runner-up. It is NOT
a seed effect on a margin and must never be quoted as one.**

## §3 · FAULT REGISTERED — F61.1, CAUGHT BY THIS TEST'S OWN CONTROL
`pack61/FAULT-F61.1-PREGUARD-ROWS.md`. **The sealed chain is heterogeneous.**
    PRE-GUARD, no rung_ref   55 rows   Z=2..56    contiguous
    GUARDED                  64 rows   Z=57..120  contiguous
At Z=19 the pre-guard 4p carries **-0.09363 against the guarded -0.09558, 1.95 mHa** — the
size of F47.2's repair at that channel. The other four channels are bit-identical.
Margins quoted from Z=2..56 may carry a mHa-scale artifact in any channel that needed the
guard; margins there are 39 mHa and up, so entrants are ARGUED safe, not MEASURED safe.
**This bears on EX-4's Z=19 failure (0.6-2.5 mHa, same Z, same scale). NOT CLAIMED as the
explanation — the s61 prediction bars "numerical" as an excuse until the Rung 7 floor is
measured, and that bar stands against this session's own convenient finding.**
REMEDY: baseline moved to the harness's own seed-A row (Standing 8) — done. Re-walking
Z=2..56 under the guard is a real repair at real cost; entered as owed, NOT smuggled in.

## §4 · UNPLANNED POSITIVE — A THIRD DETERMINISM RECEIPT
Seed-A re-runs at Z=20 and Z=39 reproduced the sealed rows BIT-IDENTICALLY in every channel
and in the margin (dmargin = 0.00000). After F60.2's receipt B (55 cold rows), the chain has
now been reproduced by a third driver in a third session.

## §5 · CLAUSE 1 LADDER — STATE AFTER s61
    DONE: Rung 1 (relativity, s60), Rung 3 (seed-independence, s61), Rung 4 (Latter, s61),
          Rung 6 (correlation OFF, s60), Rung 8 (reference named, s60), Rung 10 (entrant
          criterion), CONSTANT LEDGER.
    **OWED, IN PRIORITY ORDER — THIS IS THE s62 WORK LIST:**
      1. **Rung 7 THE CONVERGENCE FLOOR for the restart walk.** Now doubly owed: it must be
         measured before "numerical" may be offered for EX-4's Z=19, AND it must be
         reconciled with s61's seed-memory floor of <= 0.05 mHa, which it may not contradict
         without explanation. Vary grid (npts), tol, beta — NOT the seed; that is done.
      2. Rung 5  classify `_ceff` (t7b_hf.py:105): DERIVED or INPUT. Cheap, pure reading
         plus one can-fail. Do it early; it is the last unclassified item in the ledger.
      3. Rung 9  defend the candidate truncation (l<=4, n<=N+1). **s61 gives this new teeth:
         channels DO drop out by non-convergence, so "no excluded channel could have won"
         must now cover both the truncation AND the dropouts.**
      4. Rung 2  bound the single-configuration approximation on the ordering.
      5. F61.1 repair: re-walk Z=2..56 under the guard, compare entrants at all 55 rows.
    Then: Rung 0 assembly — the written reverse chain itself.

## §6 · CARRIED OPEN INTO s62
    F59.5 stale LINEAGE footer (cosmetic). F61.1 (§3). EX-4's Z=19 failure.
    Deferred, unchanged: -8.021 mHa residue at Z=59; coupled 4f2.5d SO check; the promotion
    operator as an object; the 2.88 mHa residue of s56 §5.
    **T4 (R 1701 onward) — LAST.**

## §7 · STANDING
1. Open accepts the handoff. History is NOT re-verified. Canary DRIFT -> full replay.
2. Condense at every seal: `python3 pack58/condense.py N --seal`.
3. Retirement is declared. Undeclared removal HALTS the seal.
4. Never sed a verify script.  5. Surveys return counts, sets, diffs.
6. Search the archive by content before declaring a gap (ratified s60 — and it ran this
   session: the warm-start test was found NAMED at s53 §7 with no code, before building).
7. A control must be proven to vary the thing it controls for, BEFORE use as a control.
8. A comparison must hold its reference fixed before any difference is attributed to the
   variable under test (F60.3, F44.2, F59.1 — **and F61.1 makes four sessions, one failure
   mode. This is the most productive rule in the register.**)

Bank restore-point-2_13 (R 1700) untouched throughout s61.
