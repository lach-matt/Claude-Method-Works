# SESSION 71 — COMBINED HANDOFF
# Open Session 72 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-71 tar.
# NO SEALED FILE WAS EDITED. Chain opened CLEAN: files=1152/1152 root=MATCH, prime CLEAN,
# canary CLEAN on all four. Sealed at 1159 files, root 15885a72...
# c = 137.035999 remains the only number ever entered.

## §0 · WHAT s71 DID, IN ORDER
M's ruling: **C-c then C-b.** Both executed. s70's work list items 1 and 2 closed first.

## §1 · ITEM 1 — M'S DETERMINANT RESULT. **FOUND. M's RECALL WAS CORRECT.**
Not in the transcripts by keyword, not in the Register. **In the tar, by content.**
  * `rt/hfterm.py` + `rt/nlterm.py` (s38) — explicit determinant enumeration `dets(l,N)`
    and the Slater DIAGONAL-SUM rule computing all (S,L) terms of l^N. The lowest term is
    COMPUTED, not asserted; Hund is a comparison column, RECALLED-NOT-ENTERED.
  * `rt/pb4_terms.py` + `pb4_terms.jsonl` (s48) — **TWO-CONFIGURATION** energy competition.
        Z=59 Pr  dAVG -0.048991  dTOT -0.003844  dTERM +0.045148
        Z=64 Gd  dAVG +0.015588  dTOT -0.168558  dTERM -0.184146
    **At Gd the average-of-configuration prefers B and the determinantal correction
    reverses it by 184 mHa.** Parameter-free, sealed since s48.
  * Family: `pb4_so.py`, `t7c_cuaudit.py`, `t7c_3dhund.py`, `hfterm_table.py`.
**NOT held: configuration MIXING.** No off-diagonal element existed anywhere in the archive
before s71. At LCP37 the full determinant-basis IC was specified and NOT built.
**Counter-evidence carried:** s38 measured terms on the 13-row frontier at **12/13 -> 9/13**.
**The Physics Compendium's three-fitted-constant caution does NOT apply** — that is the
amplitude law of the Method book, a different object. This machinery carries only c.

## §2 · ITEM 2 — THE NUCLEAR MASS DERIVATION. **NOT FOUND.**
Four corpora. What exists runs the other way: `E.nuclide` is a MEASUREMENT AGAINST the mass
formula (R 298, nine defect cells = pairing and clustering), R 1544 verifies the AME
identity to 0.1 keV on the A=9 chain, and R 1550's non-reproduction (E=2 not 9) is live.
**No derivation.** It bears only on citing Savelyev as parameter-free prior art and touches
no link in the chain. Carried as attribution, not as physics.

## §3 · C-c — THE PRIMARY SOURCE. **A1 STAYS [SECONDARY]. RECORDED AS A FAILURE TO CLOSE.**
`pack71/FINDING-PRIMARY-SOURCE-S71.md`. Loewdin 1969 is paywalled at Wiley and was NOT
obtained. What was obtained is a four-way triangulation, all citing the 1969 paper:
the demand is **ab initio** — no fitted or empirical input. **No source states a
non-relativistic clause and no source states an exactness clause.** This confirms LCP61
independently. **IT DOES NOT OVERTURN M'S s70 RULING** on criterion 5; it separates what the
Challenge asks from the standard M holds this project to. Also: the D-O rejection in our
ledger is the field's own ground (potential GUESSED — Kholodenko, Thijssen & Ceulemans, and
Ostrovsky 1981 himself). Routes untried for A1: institutional library, the 1971 Torino/Rome
proceedings of the Vatican centennial, or a request to a holder.

## §4 · C-b — THE 2x2 OBJECT. SPEC, PREDICTION, AND THE ANGULAR HALF SCORED.
`pack71/SPEC-L3-CI2x2.md` · `pack71/PREDICTION-CI2x2.md` sha `bb04e6c2...`, filed and hashed
before `ci2a.py` existed · `pack71/SCORE-CI2x2-ANGULAR.md` · `pack71/ci2a.py`, `ci2a.json`.

**DERIVED BEFORE ANY NUMBER WAS READ:** V is created entirely by the departure from
average-of-configuration — a closed spectator shell, or an open one spherically averaged,
gives V = 0. **L3 and L4 are not independent: the off-diagonal element L3 needs is generated
by exactly the non-sphericity L4 removes.** And the two 3j factors force **l_A + l_B EVEN**.

**MEASURED (angular only; can-fail passed against the sealed `_c3j0sq` in both directions):**
    Cr 24, Cu 29   s<->d   NONZERO, kappa=2      CI-4 HELD
    Ce 58, Th 90   d<->f   ZERO                  CI-4 HELD -- and the spectator IS open
                                                 (5d1, 6d1). Parity, not occupancy.
    Sc 21, La 57, Ac 89    ZERO                  CI-5 HELD
    CI-1 HELD (one-body zero everywhere) · CI-3 HELD (direct zero everywhere)
    CI-2, CI-6, CI-7 NOT TESTED.

**THE RESULT.** Relaxing L3 to a two-configuration superposition cannot displace the entrant
at any channel-opening row and cannot reach a tie-break row at all. **The ordering clause,
the period lengths and the tie-break are immune to the single-determinant restriction BY
DERIVATION** — where Rung 2 (s60) reached the same partition by measurement. Two independent
routes, one empirical and one derived, agree.

## §5 · WORK LIST FOR SESSION 72
1. **CI-6 — THE MAGNITUDE OF V AT Cr 24 AND Cu 29.** The object is alive exactly there and
   nowhere else. Radial R^2(4s,3d;3d,3d) on hfterm's Y^k machinery + the 2x2 generalised
   eigenproblem. **Either answer is a result and neither may be asserted before measured.**
2. **CI-2** — the averaged-spectator control, which falsifies spec section 2(iii) if it fails.
3. Extend the selection-rule scan to all ten s<->d promotion rows (Nb, Mo, Ru, Rh, Pd, Ag,
   Pt, Au) — cheap, angular only, no SCF.
4. Only then: put the closed object to M for the criterion-5 ruling.
5. **T4 (R 1701-1966) LAST**, and only after criterion 5 closes.
**THE ALPHA THREAD REMAINS CLOSED** (s70 §5). Not to be reopened without M's ruling.

## §6 · FAULTS RAISED AT s71
**F71.1** `ci2a.py`'s first configuration parser mis-tokenised `ref_cfg` (greedy digits) and
  returned "(none open)" at every row. Caught because Cr's 3d3 is known open, not by a gate.
  **A parser that silently returns an empty set will score every clause as ZERO and every
  clause predicting ZERO would have "held".** Repaired to a left-to-right scanner. **Recorded
  because the failure mode was a FALSE PASS on CI-4 and CI-5, the two load-bearing clauses.**

## §7 · ARCHIVE STATUS
Sealed: 1159 files, root `15885a727780505c206bad4ed4260b4f141d90ea0504183b87b5aec7f83ba060`.
pack71 holds the finding, spec, prediction + sha, score, instrument and rows.
**pack67 and pack68 still do not exist**; F67.1-F67.6 remain UNVERIFIABLE and must not be
scored either way until s67's handoff is located.