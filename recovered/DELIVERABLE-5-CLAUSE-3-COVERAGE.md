# DELIVERABLE 5 — CLAUSE 3, ANSWERED BY COVERAGE AND BY A WALK THAT ALREADY EXISTED

Session 57. Scores PREDICTION-B-EXPOSED (512ae671d2fa0a8f, 15:38:25Z) and
PREDICTION-A-WIDTH (f1e2b484bc1f4e96, 15:38:25Z), both filed before any read.
The only entered number in the chain remains c = 137.035999.

---

## 1 · THE FREE ELIMINATION CLOSES 94 OF 107 ROWS (gate 97, 6/7, can-failed 3 ways)

F55.2's theorem: a reversal between two channels of EQUAL n+l is a within-shell event
and cannot reach the ORDERING clause. Applied to all 107 derivation rows:

    IMMUNE  (entrant and runner-up share n+l)   94
    EXPOSED (runner-up is cross-n+l)            13   <-- N_exp

**PREDICTED N_exp = 13, AND THE PREDICTED ROW SET WAS EXACT.**

    Z = 2, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88

**The structure is not incidental.** A row is exposed exactly when the entrant is the
LAST unfilled member of its n+l group, which forces the runner-up across a group
boundary. The last member of every group is its s channel. **Every exposed row is an
s-closing row, and every one of the 94 immune rows is inside a p, d or f block.**

**COROLLARY, AND IT IS THE ONE THAT MATTERS.** La (Z=57) and Ac (Z=89) — the two atoms
at which Madelung's own stated order is wrong — are IMMUNE. At both, entrant and
runner-up share n+l. **The two famous counterexamples cannot reach the ordering clause
under any value of c.** This is Deliverable 1's statement arrived at from a second and
independent direction.

## 2 · THE UNIFORM BOUND FAILS, AND THE FILED ENVELOPE FAILS WITH IT (F57.1)

B = 0.21400 Ha (max measured c=1e6 differential, Z=91) applied uniformly:

    PROVED SAFE by margin > B : 1   (Z=2 only, margin 0.69553)
    RESIDUE                   : 11

Prediction B-3b (proved-safe count 2 or 3) is **FALSIFIED at 1**. Li and Be sit at
0.068 and 0.096 Ha, inside a bound measured at thorium. As predicted in B-3d, the
uniform bound is not a bound on the light rows at all.

**B-3e's own falsifier FIRED.** A Z^4/c^2 envelope normalised at Z=91 does NOT contain
the Z=57 point (measured 0.09741, envelope 0.03294 — it ESCAPES). **The derived
envelope as filed is REFUSED. It is not re-normalised after the fact.** Re-choosing the
normalisation point to make a failed envelope succeed is a fit, and it is the exact
fault pattern of F44.2/F55.2/F56.3 in a fourth costume.

## 3 · THE WALK CLAUSE 3 ASKED FOR HAS BEEN SEALED SINCE SESSION 53 (F57.4)

The s56 bridge costed the full 107-row c=1e6 walk at "~107 x 150 s, several sessions"
and made the decision to run it a blocking ruling for M.

**`pack53/cinf.jsonl` IS THAT WALK. 107 rows, Z=2..108, clight = 1000000.0, mode `cinf`,
sealed in session 53, scored by gates 87 and 88, present in every manifest since.**

Clause 3 was never a question of sample size. The exhaustive dataset existed and was
not looked up. The cost estimate of several sessions was an estimate of work already done.

## 4 · WHAT THE SEALED WALK SAYS (gate 87, re-pointed)

    NR-1  ordering failures at c=1e6 : [42, 43, 45, 46, 79]
    NR-2  tiebreak failures          : [57, 60, 61, 62, 89, 90, 103]  (sealed: 57, 89, 90)
    NR-4  HELD, NOT SCORED — 11 confounded steps lack a c=137.035999 restart control
    NR-5  g channels unmoved         : PASS, max shift 1.00e-05

**THE FIVE ORDERING FAILURES ARE A RESTART-MODE ARTEFACT, NOT A c-EFFECT.** cinf.py
walks in RESTART mode, referenced to the OBSERVED configuration of Z-1. At the s->d
promotion anomalies the observed configuration leaves the lower s channel open, so it
re-enters the candidate list:

    Z   sealed ent/runner-up  n+l      cinf ent/runner-up  n+l
    42     4d / 5p            6 / 6      4d / 5s           6 / 5
    43     4d / 5p            6 / 6      4d / 5s           6 / 5
    45     4d / 5p            6 / 6      4d / 5s           6 / 5
    46     4d / 5p            6 / 6      4d / 5s           6 / 5
    79     5d / 6p            7 / 7      5d / 6s           7 / 6

Mo, Tc, Rh, Pd, Au. **All five are s->d promotions — the format failure Deliverable 1
already names.** In the sealed chain each is IMMUNE (equal n+l). In the restart walk the
runner-up is an already-filled channel of LOWER n+l, which the ordering clause must flag.

**The flag is a property of the reference configuration, not of c.** It is predicted to
reproduce identically at c = 137.035999 in restart mode. That control is `ctrl137.jsonl`,
already sealed in pack53, and it is Session 58's first item.

## 5 · STATUS OF CLAUSE 3

**NOT CLOSED, BUT NO LONGER A WALK.** The walk is done. What is owed is the
attribution of five flags, against a control that already exists.

    exhaustive c=1e6 walk        DONE and sealed (pack53)
    94 of 107 rows               IMMUNE by construction, whatever c does
    13 exposed rows              all walked at c=1e6, all in cinf.jsonl
    5 NR-1 flags                 restart-mode artefact, ATTRIBUTION OWED
    11 confounded steps          NR-4 correctly HELD by gate 87 since s53

## 6 · INSTRUMENT A — SUSPENDED, AND WHY

A-1's enumeration was begun and is suspended at the first entry, because the first
entry disposed of the instrument's own premise. **F56.3's stated ground — "Z=57 at
c=1e6 had never been run" — is false.** `pack54/c3.jsonl` contains Z=57 at c=1e6,
sealed in session 54, and pack56 re-ran it and reproduced it **bit-for-bit in every
physics field**: D_ent, margin, the full order list, it_ref, chan, rungs. Only wall-clock
`sec` differs (107.6 vs 100.5).

So s55 §6 was two-ended all along. **F56.3 was not an evidence gap. It was a search
failure**, and the same search failure that hid `cinf.jsonl`.

**A-4a is therefore answered without the base-rate measurement, and differently than
predicted.** The chain's recurring fault is not that widths are established from one
end. It is that **the archive is not searched before work is costed or a gap is
declared**. F56.3 and F57.4 are one fault, and it is not the fault the width rule
would have caught.

**RULING PROPOSED FOR M, replacing §4 of the s56 bridge:**

> Before any claim that evidence is MISSING, and before any cost estimate for
> producing it, the sealed archive must be searched for it by content — not by
> filename and not from memory of which session did what. A declared gap that
> the archive already fills is a fault against the declarer.

Instrument A as filed is not withdrawn. Its ONE-ENDED-UNCHECKED by-product is still
worth having and is carried to s58 with its prediction file intact and unscored.
