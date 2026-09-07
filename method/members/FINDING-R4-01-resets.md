# FINDING R4-01 — WITHDRAWN, 6 September 2026. §34.6 and register 1333 are correct as printed. The error was mine.

This file first recorded a finding that main §34.6 and Register entry 1333 mis-state the breakdown of the eighteen
resets as 8 / 6 / 4 where the instrument gives 12 / 7 / 4. **That finding is withdrawn. The book is right, the
partition closes exactly, and I misread the entry.** The original text is superseded by this one; the record of the
mistake is kept, which is the discipline the Register itself is built on.

## What the volumes print, and what it means

Register entry **1333**, and §34.6 in the same words:

> *Eight at a subshell opening, six at an aufbau exception **(four of them also openings)**, and four at the RETURN
> from an exception: Tc after Mo, Tb after Gd, Bk after Cm, Hg after Au.*

**The parenthetical is the disambiguation, and I read straight past it.** It says the six exceptions include four
that are also openings. The eight is therefore not the count of all openings — it is the count of openings that are
**not** exceptions, the remainder after the six have been taken out. The three classes are disjoint by construction,
which is why they sum to eighteen without any subtraction.

## Measured

Run on the seated ground configurations (`LW1-ground.py`, byte-identical to the Löwdin delivery's object 3, the
observed NIST ASD 5.12 configurations), over `walk.py`'s eighteen resets:

| the entry's class | measured | elements |
|---|---|---|
| at a subshell opening, not an exception | **8** | Li, K, Rb, Cs, Tl, Fr, Lr, Rf |
| at an aufbau exception | **6** | Mo, Rh, Ce, Gd, Pa, Cm |
| — of those, also openings | **4** | Ce, Gd, Pa, Cm |
| at the return from an exception | **4** | Tc, Tb, Hg, Bk |
| **partition** | **18 of 18, disjoint** | |

**8 + 6 + 4 = 18.** Every figure entry 1333 prints is reproduced exactly, including the parenthetical four and the
four named returns. The chapter's eighteen and its 106 steps were already confirmed. Nothing in §34.6 is wrong.

## My error, stated plainly

Three failures, and the second is the one that matters.

1. **I read "eight at a subshell opening" as "all openings", which is twelve.** The entry never says that, and its
   own parenthetical rules it out.
2. **I then invented an arithmetic failure to support the misreading** — "8 + 6 − 4 + 4 = 14, not 18" — by
   subtracting an overlap that the entry had already excluded. The classes are disjoint as written. This is the
   worse error: a wrong reading became a wrong proof, and the proof made the reading look measured.
3. **I ran a reconstruction against the record and trusted the reconstruction.** `resets.py` reports "opens a
   subshell : 12 of 18" — a different question from the entry's, and a true answer to it. The standing rule (G0c)
   is that where a reconstruction disagrees with the record the finding is about the reconstruction. I quoted that
   rule in the withdrawn text and then did not apply it to my own arithmetic.

**What should have caught it before M saw it:** the entry's other figure, "eleven openings leave `a` unchanged",
reproduces exactly. An entry whose neighbouring figures all reproduce is not likely to be wrong in the middle of the
same sentence, and that should have sent me back to the reading rather than on to the finding.

## What survives, and is worth keeping

**The walk instruments are held.** The Working Register records `walk.py`, `brack.py` and `scorer.py` as not held and
their figures as record-carried. They are in `extracted/archives/restore-point-2-13/` with 345 others, recovered by
the consolidation pass, and their dependency `ground.py` is byte-identical to the seated `LW1-ground.py`. Run on it
they reproduce §34.6's **106 steps · 106 satisfied · 18 recalibrations**, the eighteen elements, the four returns and
the eleven non-resetting openings. **That part of the record is stale and the correction stands: before any claim in
Chapters 34 to 36 is called record-carried or unprovable, the restore point is searched.** `method/proofs/` holds the
instruments and their banked output.

## The one question that is genuinely open

**Is lawrencium an aufbau exception?** The entry places Lr among the eight openings, not the six exceptions.
`resets.py`'s Madelung comparison places it among the exceptions, giving seven. **Both partitions close at eighteen**
— 8 / 6 / 4 with Lr an opening, 7 / 7 / 4 with Lr an exception — so this is a question about the definition, not an
arithmetic fault, and neither reading is refuted by the count. Lr's ground state is 7s²7p¹ where the Madelung order
gives 6d¹, which is a relativistic reversal; the Löwdin solution's own tie-break exceptions are exactly La, Ac and
Th, and Lr is not among them. Put to M separately, on the solution and the contributing literature, not here.
