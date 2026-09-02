# FINDING — the seed's bit-structure across caps (§14.5.14 / R 602–605 / [MC-54])
Session: working chat, 2026-08-28. No R-numbers claimed; slip to Register 1.1 to follow.
Instruments: `Rn` verbatim from bank `cycle7.py`; cell predicate L.c1–L.c8 from bank `close_L.py`;
alphabet reading (2S ∈ [0..k], no parity) fixed by measurement — it alone yields 976 cells.
Solver (envelope-step set-cover, exact B&B over signature classes) validated two-route at the Λ₈ cap:
reproduces seed = 7; 200/200 sampled exact covers close to 976 under the sealed Rn.

## The direct answer to the original-works request
**Q1 — tested at other caps?** No (R 605 verbatim; confirmed). Now it has been.
**Q2 / verdicts per property:**
- **P4 (every coordinate both 0 and 1): LAW, with proof.** `Rn` recovers its alphabet from its
  argument, so any X₀ with ℛ(X₀) = Λ must witness every alphabet value of every coordinate —
  in particular each min and max. Cap-independent by construction. Corollaries: the null (q=0)
  and full (q=k_max) channel conditions, universal and element-forced at all four caps tested.
- **P1–P3 (the complement pairings; 11001100): REFUTED, not merely open.** At the Λ₈ cap itself,
  exact enumeration finds **24,585 minimum covers** (all size 7; R 602's 219 was a biased
  randomized sample). Only ONE cell is common to all: corner 3, (2,1,3,3,2,1,3,0). Corners 1, 2, 4
  and the unit template are not universal (corner 4 in 14%, unit in 10%, s→s in 71% of covers).
  Verified two-route: covers omitting corner-1-type cells and omitting 11001100 close to all 976
  under the sealed Rn. The five-cell bit-word table of §14.5.14 describes the 219-sample, not Λ₈.
- Corner 3's own universality is **cap-specific**: it falls at the d-shell cap.

## The cap sweep (exact, four settings)
| cap (n,e,ℓ,k,f) | cells | E | seed | s→s | s→p | p→s | p→p | null q=0 | full q=k | corner-3-type |
|---|---|---|---|---|---|---|---|---|---|---|
| (2,2,1,3,1) | 328 | — | **7** | no | U* | U* | U* | U* | U* | U* |
| (3,3,1,3,1) | 976 | 0 | **7** | no | U* | U* | U* | U* | U* | U* |
| (4,4,1,3,1) | 1,968 | — | **7** | no | U* | U* | U* | U* | U* | U* |
| (3,3,2,6,2) | 7,605 | — | **10** | no | falls | falls | U(tight) | U* | U* | falls |

U* = element-forced (cover infeasible without it). U(tight) = forced at exact minimum only — flagged, not interpreted.
Seed 7→10 while |Λ| grows 7.8×: consistent with the recorded size law (seed ~1.4× per |Λ| ~31×).

## The law that replaces the described property
At the d-shell cap, s→p and p→s fall but **s→d and d→s are element-forced** (measured, both
INFEASIBLE without). The recorded channel conditions are the ℓ≤1 specialization of:
> **The envelope-step law of the seed.** A minimum seed must witness, for each envelope pair,
> the step at each coordinate's minimum with the partner's maximum attainable there —
> at (ℓ,f): ℓ-min with f-max-attainable (s→p at ℓ≤1; s→d at ℓ≤2) and ℓ-max with f-min.
Together with P4 this is the derivable, cap-independent content. R 603's moral — the constraint
is on the channel, not the cell — survives strengthened and corrected: five of six at ℓ≤1 caps,
and the six generalize as above; s→s was never forced at any cap.

## Register consequences (for Register 1.1, via slip)
1. R 602 corrected: 219 was a sample; exact count 24,585; four-corner universality refuted.
2. R 603 corrected: five of six conditions exact at Λ₈ (s→s fails, 71%); generalized law above.
3. R 604 corrected: the unit template is not forced (10% of exact covers).
4. R 605 superseded: premise (five universal cells) fails; P4 raised to LAW with proof; P1–P3
   refuted at Λ₈; corner 3 universal at ℓ≤1 caps only.
5. Compendium objects S.bits, S.channel, S.unit need reopening; [MC-54] gains the proof of P4
   and the envelope-step law instead of the described pairing.
6. Book 14A §14.5.14: the prose is not raised to a law — it is CORRECTED. The honest statement:
   the bit-word table was a property of a randomized sample; what is law is P4 + envelope steps.

## Bounds of this run (P8)
Caps (4,4,2,6,2) and (5,5,3,8,3) not run (session bound; named, not glossed). The d-shell "pp
tight-universality" is recorded unexplained. E computed at 976-cell cap only in this run's table
(E=0 gate); other caps' E not recomputed here.

## Separate recovery, same session
`archive/transitions/Transitions.md` is present in `method16_rp_A_instruments.tar.gz`
(Drive id 18RTwgMdnpN1hNdBDR4TgB7opb4buGedh, byte-exact download verified 1,005,510 bytes).
The file memory records as unrecoverable is recovered; delivery to a fresh chat per the open item.
