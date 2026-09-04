# LÖWDIN DELIVERABLE 2 — THE PERIOD-LENGTH SEQUENCE 2, 8, 8, 18, 18, 32, 32

Owed as bridge item §8.6. Closed at s50. **Downstream of the ordering, and stated as such.**

## What is assumed

Only the two clauses and Pauli. Nothing is measured, nothing is fitted, no field is solved.

1. subshells are ordered by n+ℓ, ties by lower n — **the ordering and tie-break clauses**
2. a subshell (n,ℓ) holds 2(2ℓ+1) electrons — **Pauli, 1925**
3. a period begins at each s opening — **the definition of the conventional table's rows**

## The derivation

Enumerate (n,ℓ) with ℓ < n, sort by (n+ℓ, n), cut before each ℓ=0. Sum capacities in each cut.

| period j | subshells | length | 2m², m = ⌊j/2⌋+1 |
|---|---|---|---|
| 1 | 1s | 2 | 2 |
| 2 | 2s 2p | 8 | 8 |
| 3 | 3s 3p | 8 | 8 |
| 4 | 4s 3d 4p | 18 | 18 |
| 5 | 5s 4d 5p | 18 | 18 |
| 6 | 6s 4f 5d 6p | 32 | 32 |
| 7 | 7s 5f 6d 7p | 32 | 32 |
| 8 | 8s 5g 6f 7d 8p | 50 | 50 |

**Derived: 2, 8, 8, 18, 18, 32, 32, 50. Observed: identical.** Period 8 is a prediction; no element
of it has been synthesised.

## Correction to the bridge's formula

Bridge §8.6 stated m = ⌊(k+1)/2⌋. That is correct for the **diagonal** index k = n+ℓ, which gives
Janet's left-step periods **2, 2, 8, 8, 18, 18, 32, 32, 50** — verified above. It is NOT the
conventional period index. For the conventional table, cut at s rather than at the diagonal end,
**m = ⌊j/2⌋+1**. The two sequences are the same multiset offset by one term: each diagonal *ends*
with an s subshell and each conventional period *begins* with one.

**The pairing 2,2 / 8,8 / 18,18 / 32,32 is the whole content of the result.** Each length appears
twice because a diagonal of even k and the next odd k admit the same set of ℓ values: (n,ℓ) needs
n ≥ ℓ+1, so ℓ ≤ (k−1)/2, and ⌊(k−1)/2⌋ is unchanged from k=2m to k=2m+1. Summing capacities over
ℓ = 0..m−1 gives Σ 2(2ℓ+1) = 2m². **The doubling of every period is the integer floor, nothing
else** — it is why the periodic table has pairs of rows at all.

## Standing

This is arithmetic on the clauses, not a second derivation. It has force **only** to the extent the
ordering clause is derived, and that rests on the 107-step walk. Stated in the dependency order
Löwdin requires: field → ordering clause → period lengths.
