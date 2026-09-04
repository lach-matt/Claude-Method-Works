# REQUEST TO THE ORIGINAL METHOD PROJECT
## The tower fill-limit: settle the value, or prove it cannot be settled from the construction

**From:** the book-build project (chat 61, Mathematical Compendium authoring, MC-33)
**Re:** §12.11.0.11 "The fourteenth axis, and what can be said about it from inside" (BUILD56 main)
**Status of this item in the corpus:** open. The main text brackets it [0, 0.42%] and declines to
collapse the bracket. This request asks the method project either to close it or to certify it
closed-as-open with a proof.

---

## 1. The setup (self-contained)

The tower Λ₈ → Λ₁₃ adjoins one bounded coordinate per stage. For each stage D define

    fill(D) = cells(D) / box(D)

where box(D) is the ambient product-of-chains box (the product of each coordinate's realised
value-count) and cells(D) is the count of lattice cells. The measured sequence, verified on the
reconstruction this session:

    D    cells       box            fill(D)     stage-to-stage ratio fill(D)/fill(D−1)
    8      976         6,912        14.120%      —
    9    1,654        27,648         5.982%      0.4237
   10    2,535       110,592         2.292%      0.3832
   11   13,585       663,552         2.047%      0.8932
   12   70,905     5,308,416         1.336%      0.6524
   13  199,130    47,775,744         0.417%      0.3120

All cardinalities, boxes, and fills are exact (rebuilt from the §12.11.1 axis definitions; the
builder `tower.py` is banked with this request).

## 2. What the corpus already proves (the ceiling of current knowledge)

The main text (§12.11.0.11, line 2972) proves ONE law:

> A constrained coordinate has mean multiplicity strictly below its own value count — if it did not,
> it would be free and would carry no constraint — so each axis multiplies the ambient box by more
> than it multiplies the object.

Consequence, rigorous: fill(D+1)/fill(D) < 1 for every axis, so fill is **monotone decreasing and
bounded below by 0, hence converges** (Weierstrass). Therefore the limit L = lim fill(D) exists and
lies in [0, 0.417%]. This much is a deduction and is carried in MC-33 as a proved claim.

## 3. What is NOT proven — the exact residue

**Whether L = 0.** The proven law gives per-axis ratio *strictly* below 1; it does NOT give ratio
bounded *away* from 1 by a fixed factor. These are different, and the difference is the whole question:

- fill(D) = ∏ᵢ (fill-ratioᵢ), a product of terms in (0,1).
- Standard infinite-product criterion: ∏ aᵢ → 0  **iff**  Σ(1 − aᵢ) diverges.
- "ratioᵢ ≤ r < 1 for all i" ⟹ Σ(1 − ratioᵢ) = ∞ ⟹ L = 0.  [sufficient]
- but ratioᵢ → 1 slowly (e.g. 1 − 1/i) ALSO gives Σ(1 − ratioᵢ) = ∞ ⟹ L = 0. [so "bounded away" is not necessary]
- and ratioᵢ → 1 fast (e.g. Σ(1 − ratioᵢ) < ∞) gives L > 0.

The measured ratios (0.42, 0.38, 0.89, 0.65, 0.31) are **not monotone**, so no extrapolation from the
six built stages distinguishes these cases. Six terms cannot fix the asymptotics of an open-ended
sequence.

**Therefore the precise open question is:**

> Over all future admissible axes i = 14, 15, …, does  Σ (1 − fill-ratioᵢ)  diverge?
> Equivalently: is there a general law for the mean multiplicity of an arbitrary admissible axis,
> relative to its value-count, strong enough to decide the divergence?

If Σ diverges → L = 0 (the tower vanishes in its own ambient box).
If Σ converges → L > 0 (the tower settles at a positive fraction).

## 4. Why the book-build project cannot settle it

The build project's charter is to construct and verify the drafts from the *settled* corpus. Settling
this requires the **axis-generating law** — what the 14th, 15th, … coordinates would be and how their
multiplicity behaves — which is exactly the physics input that stopped being supplied at thirteen
(§12.11.0.11 states this is why the tower ends). That is new subject-matter, not construction.

Note the corpus already files this as ongoing method, not closed: the "fill to the limit from what
exists" cycle (register-linked, main text ~L13528–13596) carries the explicit iteration
X_{n+1} = ℛ(X_n ∪ Δ_n) with "search for identification" — i.e. the value of L is an open research
item in the corpus's own accounting. This request formalises that item.

## 5. What we are asking the method project to deliver (any ONE of these closes it)

**(A) A convergence/divergence theorem.** Prove or disprove that Σ(1 − fill-ratioᵢ) diverges over the
admissible-axis sequence, via a general law for an admissible coordinate's mean multiplicity vs its
value-count. Deliver: the law, its proof, and the resulting value of L (0, or a positive bound).

**(B) A rate law for admissibility.** Show whether the admissibility condition (the "door," §14.4 /
§14.1) *by itself* forces ratioᵢ ≤ r < 1 for a fixed r (which would give L = 0 immediately), or
exhibit an admissible coordinate whose ratio can approach 1 (which reopens L > 0). Deliver: the
strengthened admissibility statement or the counterexample.

**(C) A certified-open verdict.** If the value of L is genuinely undecidable from the construction
without further physical input (no axis-generating law is derivable), deliver a proof of *that* — a
statement that the bracket [0, 0.417%] is the strongest claim the construction supports, with the
reason. This upgrades MC-33's "left open" from an honest silence to a proved boundary.

Outcome (C) is itself a publishable result and is a fully acceptable answer. We are not asking for
L = 0; we are asking which of (A)/(B)/(C) is true.

## 6. What we will do with the answer

- If (A) or (B) returns **L = 0**: MC-33 upgrades to state the limit is zero, with the new law cited,
  and a new Register entry records it (append-only; cites §12.11.0.11 / register 333).
- If (A) or (B) returns **L > 0**: MC-33 states the positive limit and its bound; Register entry as above.
- If (C): MC-33 keeps the bracket but replaces "the question the construction leaves open" with
  "provably the strongest claim the construction supports," citing the (C) proof.

In all three cases MC-33's current draft (limit exists; value in [0, 0.417%]) remains correct and
stands until the answer arrives — nothing is blocked.

## 7. Attached / referenced

- `tower.py` — the Λ₈→Λ₁₃ builder from the §12.11.1 axis definitions (banked separately; reproduces
  every cardinality and box above exactly).
- Source section: BUILD56 main §12.11.0.11 (and the fill-law statement at line 2972).
- Prior-art already in MC-33: Weierstrass (monotone convergence), Birkhoff 1937 (join-irreducibles),
  Shannon 1948 (bits). A resolution would add whatever axis-generating / admissibility-rate result (A)/(B)
  establishes, or the (C) undecidability proof.

---

**One-line summary for the method project:** The tower's fill provably converges to some
L ∈ [0, 0.417%]; prove whether L = 0 (⟺ Σ(1 − per-axis fill-ratio) diverges over future admissible
axes), or prove that the construction alone cannot decide L. Any of the three closes the residue in MC-33.
