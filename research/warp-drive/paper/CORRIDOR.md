# The chirality of a stationary axisymmetric corridor

### What the metric cannot tell you, what electromagnetism can, and why the answer is a relation

**M. Lach** · with a computing collaborator, under the protocols of The Method v1.6
Draft v1.0, 12 September 2026

> **Reading status.** Every claim below carries a promotion status from `proofs.py` and an
> attribution from `provenance.py`, both runnable. **The headline of the last section is prior
> art** — see §8 and §9. Nothing here moves the energy cost of any spacetime engineering, and
> §10 says so explicitly rather than leaving it to be inferred.

---

## Abstract

For a stationary axisymmetric metric, four of the five nonzero Boyer–Lindquist components are even
under reversal of the rotation parameter and exactly one, `g_tφ`, is odd. We prove that the
consequence is a strict no-go: **no function whatever of the even components returns any odd power
of `g_tφ`**, so the *sense* of rotation is not recoverable from the even sector at any precision.
We give the closed form the even sector *does* determine — `g_tφ² = r²(1+g_tt)²(1/g_rr + g_tt)` for
equatorial Kerr, and `a² = Σ/g_rr − r² + Σ(1+g_tt)` for Kerr–Newman at every polar angle — and show
the map `(M,a) ↦ (even sector)` has full rank with a two-point fibre, so the obstruction is a
**covering, not a degeneracy**, and no local or perturbative method can see it.

We then locate the obstruction in one object. Writing `z = r − ia cos θ`, Kerr's whole spin
dependence is the Newman–Janis complex shift; the Kretschmann and Chern–Pontryagin scalars are the
real and imaginary parts of the single complex invariant `48M²/z⁶`; `|z|² = g_θθ` is even and
`arg z` is odd. **The entire odd content of the curvature is a phase**, and it vanishes identically
on the equatorial plane, where Kerr's polynomial curvature invariants coincide with Schwarzschild's.
The modulus performs its function *by* pairing the two chiralities — `z̄(a) = z(−a)` exactly — so the
operation that builds it is the operation that destroys the sign.

Electromagnetism breaks the degeneracy because it carries a parity the metric does not: the metric
sees only `Q²`, while `A_t` is odd in `Q` and `A_φ` is odd in both `Q` and `a`. Using Carter's
`μ = Qa`, the map `(M,a,Q) ↦ (even sector, A_t, A_φ)` is **injective iff `Q ≠ 0` or `a = 0`** — it
fails exactly on the uncharged spinning case.

Finally, we interpret the fibre. For any metric even in `r` — the condition for a two-sided
geometry — the reflection `P : (r,φ) → (−r,−φ)` fixes the even sector and flips `g_tφ`, acting
identically to `a → −a`. **The two sheets of the fibre are the two mouths**, its deck group is the
mouth exchange, and the unrecoverable sign is a *mouth label*. The recovered sign is therefore
chart-relative; what is invariant is `sgn(a₊)·sgn(a₋) = −1`. **That the two mouths see opposite
rotation is published** (Volkov, arXiv:2605.27600, who also corrects two earlier papers on the
point); the identification of it with the fibre of the inversion problem is what we add.

---

## 1. Setting and notation

Boyer–Lindquist coordinates `(t, r, θ, φ)` [bl67]. Kerr–Newman [ncc65]:

```
Σ = r² + a²cos²θ            Δ = r² − 2Mr + a² + Q²          P = 2Mr − Q²
g_tt  = −(1 − P/Σ)          g_rr = Σ/Δ          g_θθ = Σ
g_φφ  = (r² + a² + P a² sin²θ/Σ) sin²θ          g_tφ = −P a sin²θ/Σ
A_t   = −Qr/Σ                                   A_φ  = Qra sin²θ/Σ
```

Write `y = a cos θ` and `s² = sin²θ`. **Every identity below is polynomial in `(M, a, r, Q, y, s²)`
after clearing denominators**, which is what makes the verification in `proofs.py` exact rather than
numerical: those are the variables the grid runs over, in `Fraction` arithmetic.

Call `{g_tt, g_rr, g_θθ, g_φφ}` the **even sector** and `g_tφ` the **intersection thread**.

---

## 2. What the even sector determines

**Proposition 1** (equatorial Kerr). `g_tφ² = r²(1 + g_tt)²(1/g_rr + g_tt)`.

*Proof.* `1 + g_tt = 2M/r`; and `1/g_rr + g_tt = Δ/r² − (r−2M)/r = a²/r²`, the `−2Mr` in `Δ`
cancelling the `2M/r` in `g_tt`. Hence RHS `= r²·(4M²/r²)·(a²/r²) = 4M²a²/r² = (−2Ma/r)²`. ∎

**Proposition 2** (Kerr–Newman, all `θ`). `a² = Σ/g_rr − r² + Σ(1+g_tt)` and `2Mr = Σ(1+g_tt) + Q²`.

*Proof.* `Σ(1+g_tt) = P` and `Σ/g_rr = Δ`; then `Δ − r² + P = a²`. ∎

Proposition 2 matters because the obvious route — reading `a²` out of `g_θθ = Σ` and dividing by
`cos²θ` — is `0/0` on the equatorial plane. The route through `Δ` carries no `θ` and is valid
everywhere. *(This corrects `modulus.py`, whose fibre computation used the first route; nothing it
printed was equatorial, so nothing it printed was wrong.)*

**Both propositions are verified exactly** over rational grids exceeding the polynomial degree in
each variable — 175 and 21,875 points respectively — so they are proved, not sampled.

---

## 3. The parity theorem

**Theorem 3.** Under `a → −a`, the components `g_tt`, `g_rr`, `g_θθ`, `g_φφ` are invariant and
`g_tφ` is negated.

*Proof.* `Σ`, `Δ` and `P` contain `a` only through `a²` (and `y` only through `y²`, and `y → −y`
with `a`). Hence all three are invariant, so `g_tt`, `g_rr`, `g_θθ` are; `g_φφ` contains `a` only as
`a²`; `g_tφ` carries one explicit factor of `a`. ∎

**Corollary 4 (the no-go).** Any function of the even components is invariant under `a → −a`; any
odd power of `g_tφ` is negated. A function that is both is identically zero. **Therefore no
expression in the even components equals any odd power of `g_tφ` wherever that power is nonzero.**

Corollary 4 is the whole obstruction, and it disposes of the natural attempt to defeat it. Since
`g_tφ = −(1+g_tt)a`, one has `g_tφ³ = sgn·(g_tφ²)^{3/2}` **exactly**: the cube carries the square's
content plus one bit and nothing else, and `g_tφ³/g_tφ² = g_tφ`, so *knowing the cube is knowing the
thread*. **A parity is not defeated by a higher power.**

**Proposition 5 (the fibre).** At fixed `(r, θ)` the map `E : (M,a) ↦ (even sector)` has Jacobian of
rank 2 for `a ≠ 0`, and fibre `{+a, −a}`; at `a = 0` the rank drops to 1 and the fibre is a point.

Rank 2 with a two-point fibre is a **covering, not a degeneracy**: `|a|` is locally determined and
perfectly so, and no derivative distinguishes the sheets. **No perturbative method can see a deck
transformation** — and the map is singular exactly where the question is empty.

---

## 4. The obstruction is one complex phase

Kerr is Schwarzschild at complex radius `z = r − ia cos θ` — the Newman–Janis shift [nj65], made the
title of a paper by Schiffer, Adler, Mark and Sheffield [sams73]. For Kerr,
`Ψ₂ = −M/z³` ([an14] eq. 2.28 at `Q = 0`).

**Proposition 6.** `48M²/z⁶ = K − (i/2)·*RR`, where `K = 48 Re(Ψ₂²)` and `*RR = −96 Im(Ψ₂²)`.

*Proof.* `K = 48M² Re(z⁻⁶)` and `*RR = −96M² Im(z⁻⁶)`; combine. ∎

**The Kretschmann and Chern–Pontryagin scalars are not two invariants — they are the real and
imaginary parts of one, and it is Schwarzschild's Kretschmann evaluated at a complex radius.**

**Corollary 7.** `|z|² = Σ = g_θθ` is even in `a`; `arg z` is odd. **The entire odd content of the
curvature is the phase.**

**Corollary 8.** On the equatorial plane `y = 0`, so `z = r` is real: `K = 48M²/r⁶`, *Schwarzschild's
value, independent of `a`*, and `*RR ≡ 0`. **The spin is absent from the polynomial curvature
invariants there entirely, not merely its sign.** *(Scope: polynomial invariants of a type D vacuum,
which are functions of `Ψ₂` alone. Differential invariants are not — `d(*RR)/dθ` at the equator is
proportional to `a` and nonzero. The spin is invisible **at** the plane and visible in the first
derivative **off** it.)*

**Corollary 9.** `arg z = −arg(K − (i/2)*RR)/6`, single-valued for `|arg z| < π/6`, i.e.
`|a cos θ|/r < 1/√3`. Beyond that the sixth power aliases and the phase is not recoverable.

---

## 5. Why a modulus cannot do it

**Proposition 10.** `z̄(r,θ,a) = z(r,θ,−a)`, hence `|z|² = z(+a)·z(−a)`.

**The modulus is the product of the two chiralities.** It does not *fail* to distinguish them — it is
*built by pairing them*, with identical weight, and a product is symmetric in its factors. The
operation that makes a modulus is the operation that destroys the sign; they are one act. The
complementary combination is `z(+a)/z(−a) = e^{2i·arg z}`: **their product is the magnitude, their
ratio is the direction.**

Geometrically: `|z| = ρ` is a circle, `Re z = r` a line. They meet in two conjugate points, collapsing
to one exactly at tangency `ρ = r`, i.e. `a cos θ = 0`. And `ρ ≥ r` always. **There is always either a
two-fold ambiguity or no spin in the plane to be ambiguous about, and never a third case.**

A further limit, and it is a whole parameter rather than a bit: `z` carries only the **product**
`a cos θ`. Geometries with `a₁cos θ₁ = a₂cos θ₂` have identical `z`, identical `Ψ₂`, and hence
identical polynomial curvature invariants at that point, with different `g_rr`. **The complex radius
is a complete description of the local curvature and an incomplete description of the geometry.**

---

## 6. Electromagnetism carries the missing parity

**Proposition 11 (parity census).** The metric is even in `a` **and even in `Q`** — it sees only `Q²`.
`A_t` is odd in `Q` and even in `a`. `A_φ` is odd in **both**.

**The electromagnetic sector supplies an odd member for each sign the metric hides.**

**Theorem 12** ([carter68]; verified, not derived here). The Kerr–Newman magnetic dipole is `μ = Qa`,
so with `J = Ma` the gyromagnetic ratio is `g = 2`, the Dirac value. *This is Carter's, 1968.*

**Proposition 13 (the inversion).** `Q = −A_t Σ/r` and `a = A_φ Σ/(Q r sin²θ)`, the second defined
only for `Q ≠ 0` and `sin θ ≠ 0`. It is **linear in `a`, hence odd**: the metric offers `a²`, the
potential offers `a`. *EM is not a better probe of the same thing; it is a probe of a different
parity.*

**Theorem 14.** `Φ : (M,a,Q) ↦ (even sector, A_t, A_φ)` is **injective iff `Q ≠ 0` or `a = 0`**.

*Proof.* If `Q ≠ 0`, Proposition 13 recovers `Q` then `a`, and Proposition 2 recovers `M`. If `Q = 0`
then `A_t = A_φ ≡ 0`, only the even sector remains, and by Theorem 3 it takes the same value at `a`
and `−a`; those are distinct iff `a ≠ 0`. ∎

**Proposition 15 (coverage).** The curvature channel `*RR ∝ a cos θ` is blind on the equator; the
electromagnetic channel `A_φ ∝ sin²θ` is blind on the axis. `cos` and `sin` have disjoint zeros on
`[0,π]`, so **at every `θ` at least one channel reads the bit.**

---

## 7. The fibre is the pair of mouths

**Theorem 16.** Let a stationary axisymmetric metric have every component **even in `r`** — the
condition for a two-sided geometry with a throat at `r = 0`. Then `P : (r,φ) → (−r,−φ)` fixes
`g_tt`, `g_rr`, `g_θθ`, `g_φφ` and sends `g_tφ → −g_tφ`; and `P² = 1`.

*Proof.* A reflection `φ → −φ` multiplies a component by `(−1)` per `φ` index: none for `g_tt`,
`g_rr`, `g_θθ`; one for `g_tφ`; two for `g_φφ`. The reflection `r → −r` changes nothing precisely
because each component is even in `r`. Both are involutions and they commute. ∎

**No field equation is used.** Verified on twenty randomly generated even-component metrics.

**Corollary 17.** `P` and `a → −a` have identical action on the metric (Theorem 3), so no function of
the metric distinguishes them. **The two-point fibre of Proposition 5 is the pair of mouths, its deck
group ℤ₂ is the mouth exchange, and the unrecoverable sign is the label of which mouth one occupies.**

**Corollary 18.** `A_φ` carries one `φ` index and is negated by `P` as well. So the sign recovered by
Proposition 13 is recovered **relative to the chart**, and the two mouths' natural charts disagree.
What survives is the product:

> **`sgn(a₊) · sgn(a₋) = −1`** — chart-independent, because each chart-dependence enters once per
> factor.

**The corridor's only absolute chirality fact is a relation, not a value.**

---

## 8. Prior art, and a demotion

**§7's physics is published.** Volkov [volkov26] states it in words —

> *"+J is the angular momentum measured from the x → +∞ region, while −J is the angular momentum
> measured at x → −∞… if the observer as x → ∞ sees the wormhole spin clockwise, say, then the
> observer at x → −∞ will see it spin in the opposite direction."*

— and as his eq. (8.9), `V(−x,y) = V(x,y)`, `W(−x,y) = −W(x,y)`: *symmetric under `x → −x`, up to a
flip in the sign of the rotation field.* That is Theorem 16's `P`, before us. His eq. (8.10) records
that Kerr's own `r → −r` requires `M → −M` — the candidate we tested and rejected, rejected for his
reason. His Appendix D shows the reflection is available to wormholes and not to black holes.

**And he corrects two papers that had it backwards**: Kleihaus & Kunz [kk14] and Chew, Kleihaus &
Kunz [ckk16] state `J` symmetric under `x → −x`; Volkov records that it is antisymmetric. So the
point is not merely known — **the literature has already argued it out**, and a novelty claim here
would have been false against that record.

**What survives as ours is one connection, and it is smaller than the claim it replaces:**

> the two-point fibre of the even metric sector **is** the pair of mouths; its deck group **is** the
> mouth exchange; and the sign the parity theorem forbids is therefore a **mouth label** rather than a
> missing property of a single object.

Both halves are published; the link was not found. **"Not found" is a floor, not a proof of absence** —
two queries against one database is not a literature review.

---

## 9. Promotion and attribution

`proofs.py` (`--selftest`) classifies 27 claims: **20 THEOREM** (derived here, verified exactly over
rational grids exceeding the degree bound), **3 THEOREM-CITED** (known, attributed, re-verified),
**1 DEFINITION**, **3 MEASURED** (not promoted).

`provenance.py` (`--selftest`) classifies 22 attributions against 17 sources: **7 PRIOR-ART**,
**8 OURS-AS-A-CONNECTION**, **1 OURS**, **6 ELEMENTARY**. Twelve sources were read from source in
this session; **five are named and not read**, are used for functional form or for a name only, and
are never quoted.

Not promoted, and named so they cannot be mistaken for results:

| claim | status | why |
|---|---|---|
| `√Λ` vs `π` (a 0.5705 % miss) | MEASURED | a near miss, refused as a finding |
| EM *supplies* the bit in a built device | MEASURED | a design claim, not a theorem |
| **the energy bill** | MEASURED | **untouched by every line above** |

---

## 10. What this does not do

**It does not move the energy cost of anything.** Every result above concerns the *sense* of a
rotation — which way, and relative to what. None of it addresses whether a throat opens, what holds
it open, or what that costs. The three figures this project has priced elsewhere —
`c⁴/(GΛ) = 1.212374×10⁴³ J/m`, `√Λ ℓ_P = 5.106580×10⁻³⁵ m`, `f_P/√Λ = 5.870709×10⁴² Hz` — stand
exactly where they stood, and nothing here should be read as having approached them.

**It does not overturn the parity theorem.** §6 adds a sector with its own odd member; that is asking
a different map, not inverting the one Corollary 4 forbids.

**And it does not hand anyone an absolute handedness**, because §7 shows there is none to hand. For a
construction the consequence is a labelling rather than a free parameter: the handedness of a driving
current does not choose a value, it chooses **which mouth is the entrance**.

---

## References

Keys match `provenance.py`. **`†` = named but not read in this session; used for functional form or
for a name, never quoted.**

- **[kerr63]** R. P. Kerr, *Phys. Rev. Lett.* **11** (1963) 237–238.
- **[nj65]** E. T. Newman and A. Janis, *J. Math. Phys.* **6** (1965) 915–917.
- **[ncc65]** E. T. Newman, R. Couch, K. Chinnapared, A. Exton, A. Prakash *et al.*, *J. Math. Phys.* **6** (1965) 918–919.
- **[bl67]** R. H. Boyer and R. W. Lindquist, *J. Math. Phys.* **8** (1967) 265.
- **[ernst68]** F. J. Ernst, *Phys. Rev.* **167** (1968) 1175.
- **[carter68]** B. Carter, *Phys. Rev.* **174** (1968) 1559–1571.
- **[sams73]** M. M. Schiffer, R. J. Adler, J. Mark and C. Sheffield, *J. Math. Phys.* **14** (1973) 52–56.
- **[an14]** T. Adamo and E. T. Newman, *Scholarpedia* **9**(10):31791, arXiv:1410.6626.
- **[kk14]** B. Kleihaus and J. Kunz, *Phys. Rev. D* **90** (2014) 121503.
- **[ckk16]** X. Y. Chew, B. Kleihaus and J. Kunz, *Phys. Rev. D* **94** (2016) 104031.
- **[gv17]** G. W. Gibbons and M. S. Volkov, *Phys. Rev. D* **96** (2017) 024053.
- **[volkov26]** M. S. Volkov, arXiv:2605.27600.
- **[sv19]**† A. Simpson and M. Visser, *JCAP* **02** (2019) 042, arXiv:1812.07114.
- **[mfl21]**† J. Mazza, E. Franzin and S. Liberati, *JCAP* **04** (2021) 082, arXiv:2102.01105.
- **[teo98]**† E. Teo, *Phys. Rev. D* **58** (1998) 024014.
- **[bpt72]**† J. M. Bardeen, W. H. Press and S. A. Teukolsky, *Astrophys. J.* **178** (1972) 347.
- **[mt88]**† M. S. Morris and K. S. Thorne, *Am. J. Phys.* **56** (1988) 395.

---

## Reproduction

```
python3.12 proofs.py            # every proof, with exact rational verification
python3.12 provenance.py        # the attribution ledger
python3.12 weave.py cube.py phase.py modulus.py iff.py corridor.py   # the measurements
```

Each takes `--selftest`. All are stdlib-only.
