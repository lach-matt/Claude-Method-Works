# REQUEST — provenance of the §10.2 void-free / correlation measurement (for MC-10)

**From:** book-construction project, chat 57 (B-list Batch-2 completion, HANDOFF-8)
**To:** the project in which the volumes were built
**Concerns:** main volume Chapter 10 "The void," §10.2 "Its size, and its stability" (source line 2050, BUILD56 main); Figure 10.1; Mathematical Compendium object `L.voidfrac` (BUILD57 compendia line 14833)

## What the book records

> "The void-free fraction is 27.7–30.1% across 776 million pairs and a seventeenfold range in cell count."
> "Satisfied individually 67–94%; their product is 20.19%; the joint figure is **30.13%** — a factor of **1.49** above independence, over the same 776 million pairs."

The 1.49 factor stands as recorded. The compendium expansion MC-10 owes its derivation. The derivation is done and exact (see §3 below), but the numeric figures cannot be reproduced because **the population they were measured on is not recorded anywhere** — not in §10.2, not in `L.voidfrac`, not in the Register, not in Figure 10.1's caption, not in REWRITE-chapter10-void.md.

## What was measured here (chat 57, rebuilt Λ₈ from the HANDOFF-8 recipe)

| population | cells | pairs | individual range | product | joint | factor |
|---|---|---|---|---|---|---|
| base caps (n,e,ℓ,k,f)=(3,3,1,3,1), all unordered pairs | 976 | 475,800 | 69.95–98.06% | 20.13% | 28.35% | **1.4081** |
| (4,4,1,3,1) | 1,968 | 1,935,528 | 69.9–97.9% | 22.44% | 30.78% | 1.372 |
| (4,4,2,5,1) sampled | 8,847 | 39.1M | 68.3–90.3% | 20.90% | 28.54% | 1.366 |
| (5,5,2,6,1) sampled | 25,748 | 331M | 68.7–92.4% | 23.47% | 31.12% | 1.326 |
| (5,5,2,8,2) sampled | 55,682 | 1.55B | 65.0–87.4% | 14.19% | 21.64% | 1.526 |
| (6,6,3,10,2) sampled | 234,340 | 27.5B | 65.4–85.1% | 15.93% | 23.20% | 1.456 |

The factor is cap-dependent (1.33–1.66 observed). 1.49 is consistent with this behaviour but no single cap or one-parameter family from the base reproduces "776 million pairs"; the largest one-parameter family sums to 32M pairs, and hundreds of unrelated cap settings give ~776M. The cap set cannot be inferred; it must be read from the instrument that produced it.

## What is requested — in order of usefulness

1. **The script that produced the 776M-pair run** (the instrument behind Figure 10.1 / §10.2), verbatim, with any driver or cap list it was called with. This alone resolves everything.
2. Failing the script: **the cap list** — every (capn, cape, capℓ, capk, capf) setting included in the run, and whether pairs were ordered, unordered, or included the diagonal (x = x). "776 million" must be recoverable as the sum of pair counts over that list.
3. **Figure 10.1's plot data** — the (cell count, void-free fraction) points it draws, so the "seventeenfold" (§10.2, rewrite caption) versus "hundredfold" (main-volume caption, audit table line 10253 "100×") discrepancy can be settled from the data rather than by editorial choice.
4. **The Register entry number** that records this measurement, if one exists. A grep of the Register for `776`, `20.19`, `30.13`, `1.49`, `void-free` finds only the §10.2 sentence and its mirrors — no originating entry.
5. Per-constraint individual satisfaction rates at that population (the seven numbers summarised as "67–94%"), if retained.

## What this unblocks

MC-10 (`L.voidfrac`, COMPUTED → PROVED) will carry: (i) the exact structural theorem — the factor is the product over the constraint tree's edges of conditional lifts; constraints are conditionally independent given the shared coordinate's interval (measured lift 1.0000 in every stratum, five shared pairs); non-adjacent pairs have lift ≈ 1; the sign is positive because box containment hiᵢ ≤ φ(loⱼ) is a narrowness condition in every coordinate it touches, so two constraints reading the same coordinate read the same width — and (ii) the numeric instance. Item (ii) must be verified before it is written. With the instrument or cap list, the recorded 1.49 / 30.13% / 20.19% are reproduced and authored as recorded. Without them, the expansion carries the reproducible base-cap instance (1.4081 at 976 cells) and cites the book's 1.49 as a measurement at an unnamed larger population, which weakens the object and leaves a discrepancy in the record.

## Standing rules honoured

Nothing has been edited. No recorded finding is withdrawn: the reconstruction differs from the record, so the finding is about the reconstruction (a population mismatch), not about the record. All figures above are measured (scripts `lam8.py`, `mc10.py`, `mc10b.py`, `mc10c.py`, `mc10d.py`, chat 57); nothing here is inferred.
