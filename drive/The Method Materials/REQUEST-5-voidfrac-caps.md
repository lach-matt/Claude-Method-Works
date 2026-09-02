# REQUEST 5 to the original-works project — the cap set behind §10.2's 776 million pairs
(from The Method 1.6 chat 57, B-list Batch-2 completion / [MC-10]; successor to Request 4. Delivery as before: file to Drive Materials or direct upload, md5 stated. Scripts preferred over numbers throughout.)

## What is blocked
[MC-10] is the M-flagged "mathematical accompaniment" owed to main Chapter 10 "The void," §10.2 "Its size, and its stability" (BUILD56 main line 2050; Figure 10.1; compendium object `L.voidfrac`, BUILD57 compendia line 14833, grade COMPUTED). The book records:

> void-free fraction **27.7–30.1% across 776 million pairs** and a seventeenfold range in cell count; constraints satisfied individually **67–94%**, product **20.19%**, joint **30.13%**, factor **1.49** above independence.

The structure is derived and exact (§3 below). The numbers cannot be reproduced because **the population is not recorded**: not in §10.2, not in `L.voidfrac`'s statement or check line, not in Figure 10.1's caption, not in REWRITE-chapter10-void.md, not in the Register (grep of both volumes for `776`, `30.13`, `20.19`, `1.49`, `void-free` returns only the claim and its mirrors), and not in restore-pack A — `mathreg.py` line 252 *states* the figures but no instrument in the 340-file bank computes them.

## A. The instrument — preferred
The script that produced the 776M-pair run and Figure 10.1, verbatim, with the driver or cap list it was called with. This closes A, B and C at once.

## B. The cap list — fallback if the script is gone
1. Every cap setting `(capn, cape, capℓ, capk, capf)` in the run, so that the pair counts sum to the recorded 776 million. State whether pairs are **ordered**, **unordered**, or **include the diagonal** — the three differ by ~2× and the sum does not identify the convention.
2. The per-cap cell counts, so the **seventeenfold range** is checkable end to end.
3. The seven per-constraint satisfaction rates at that pooled population (the numbers summarised as "67–94%"), if retained.
4. Whether the joint/product/factor triple is **pooled over the whole family** or computed at **one cap** and reported alongside the family's fraction range. §10.2 reads "over the same 776 million pairs," which asserts pooled; confirmation or correction is what is wanted.

## C. Figure 10.1's plot data
The (cell count, void-free fraction) points the figure draws. §10.2 and REWRITE-chapter10-void.md say **seventeenfold**; the main-volume caption at line 2054 and the audit table at line 10253 say **hundredfold** / **100×**. Same measurement, two descriptions — settle it from the data, not editorially. (Register 1745 already records that this figure carries a pre-V16 title, "Figure 5.1", baked into the image; if it is re-rendered, that is the moment.)

## D. Register locator
The entry number recording this measurement, if one exists. If none does, say so — the finding is then that a load-bearing figure entered the volumes without a Register entry, which is itself owed a slip.

## What has been measured here (chat 57, so the answer can be checked against it)
Λ₈ rebuilt from the HANDOFF-8 recipe (976 cells, 1,654 for Λ₉, both confirmed). Box containment tested as `hi_i ≤ φ(lo_j)` per §10.3, over all 475,800 unordered pairs at caps (3,3,1,3,1):

| | individual | product | joint | factor |
|---|---|---|---|---|
| base cap, exhaustive | 69.95–98.06% | 20.13% | 28.35% | **1.4081** |

Cap dependence, sampled: (4,4,1,3,1) 1.372 · (4,4,2,5,1) 1.366 · (5,5,2,6,1) 1.326 · (5,5,2,8,2) 1.526 · (6,6,3,10,2) 1.456 · (7,7,3,14,3) 1.660. **The factor is cap-dependent over 1.33–1.66, so 1.49 is consistent but not locatable without the caps.** No one-parameter family from the base reaches 776M pairs (largest sums to 32M); hundreds of unrelated settings give ~776M, so the cap set cannot be inferred and must be read from the instrument.

The derivation itself, which does not depend on the answer: the factor equals the product of tree-ordered conditional lifts (1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022 = 1.4081, equal to joint/product to four decimals); every lift above 1 sits on a shared-coordinate edge while non-adjacent pairs measure 0.9999–1.0101; conditioned on the shared coordinate's interval every shared-coordinate lift collapses to exactly **1.0000** in every stratum (five pairs tested), so all dependence flows through shared coordinates and nowhere else; and the sign is positive because `hi_i ≤ φ(lo_j)` is a **narrowness** condition on each coordinate it touches (P = 1.000 at zero width, falling monotonically — q≤k: 1.000 / 0.599 / 0.319), so two constraints sharing a coordinate read the same width variable.

## Why the numbers and not just the structure
[MC-10] raises `L.voidfrac` COMPUTED → PROVED and must state a number under verify-before-write. With A or B, the recorded 1.49 / 30.13% / 20.19% are reproduced and authored as recorded. Without them the expansion carries the base-cap instance (1.4081 at 976 cells) and cites 1.49 as a measurement at an unnamed population — a weaker object and a live discrepancy in the record.

## Standing rules observed
Nothing edited. No recorded finding withdrawn: the reconstruction differs from the record, so the finding is about the reconstruction — a population mismatch — not about the record. Every figure above is measured (`lam8.py`, `mc10.py`, `mc10b.py`, `mc10c.py`, `mc10d.py`, chat 57); nothing is inferred. Named rather than glossed: caps (4,4,2,5,1) and larger were sampled at 400k pairs, not enumerated; Figure 10.1's underlying points were never in reach here.
