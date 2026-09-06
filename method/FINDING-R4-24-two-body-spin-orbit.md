# FINDING R4-24 — ruling 1 discharged. The two-body spin–orbit term is **built**, its angular reduction **derived rather than looked up**, and validated at every step. It does not close the six measured intervals — and **Blume & Watson report that exact behaviour**, for exactly the shells where it happens. The object is corroborated by the one result that looked like its refutation. NOT REPAIRED.

Measured 6 September 2026 on M's ruling of that date, given on `FINDING-R4-21`'s question — *"1 - build it."*

`method/proofs/sooterm.py` (new), banked `sooterm.json`, `sooterm-exchange.json`, `sooterm.out`.
**Selftest 9 of 9.**

## 1. Two things derived before any code, and they decided the build

**(1) For a closed core the spin–other–orbit has no direct part.** Its Hartree average needs either Σ_j⟨**s**_j⟩ over
the core — zero for a closed shell — or the core's net orbital current, also zero. **The entire effect is
exchange.** That is why no local potential can carry it, and it vindicates `so94.py`'s own declaration that
*"the nonlocal HF exchange has no dV/dr."*

**(2) The direct spin–own–orbit is exactly one Marvin integral per core shell.** From V_b's own form,
(1/r)dV_b/dr = −N_b r⁻³∫₀^r P_b², so

> (α²/2)⟨a|(1/r)dV_b/dr|a⟩ = **−(α²/2) N_b M⁰(ab)** exactly, with M^k(ab) = ∫dr₁ P_a² r₁^−(k+3) ∫₀^{r₁} dr₂ P_b² r₂^k

**This fixes the Marvin convention with no appeal to memory, and it is the anchor everything else stands on.**

## 2. The coefficients: found by M's route, and cross-checked three ways

Blume & Watson's own papers are paywalled. M: *"there is still another way. search for others who have referenced
these papers."* That worked where stopping at the sources had not — the mean-field working equation is stated in
the open, and the ORCA 6.1 manual's form is the one carried here:

> h^SOC_pq = (p|ĥ^1e|q) + Σ_rs P_rs [ (pq|ĝ|rs) − (3/2)(pr|ĝ|sq) − (3/2)(sq|ĝ|pr) ]

**A discrepancy was caught rather than smoothed.** `arXiv:2404.04716` Eq. (15) as extracted puts the two exchange
terms at *opposite* signs; read literally with its own index convention they become identical at p = q, which is
the diagonal that carries ζ — so the exchange contribution would cancel identically, which cannot be right. **The
form was refused on that test**, and the ORCA form, whose two index patterns genuinely differ, was carried
instead.

**The 3/2 is confirmed three ways**: both literature statements give it, and 3/2 = 1 + 2×(½) is exactly the
spin-own-orbit to spin-other-orbit weight the Breit–Pauli operator fixes on its own.

## 3. The angular reduction, derived

No stated closed-shell reduction exists in reachable literature — the atomic-structure code papers publish their
machinery and cite Blume & Watson for this. So it was derived: the multipole expansion of 1/r₁₂, the gradient
split using r̂ × ∇_Ω = iL̂,

> ĝ^ξ = i[ (∂F/∂r₁)(i/r₁) L̂₁ + (1/r₁)(∇_Ω₁F × ∇₁) ]_ξ

and the three resulting angular integrals by Gauss–Legendre quadrature in cos θ. **No remembered angular formula
enters anywhere.**

## 4. Validated at every step

| check | result |
|---|---|
| the three-term decomposition against **brute-force numerical differentiation** on a 3-D grid | **1.4 × 10⁻⁴**, grid-limited |
| R_k against direct double integration, every k | **exact to 10⁻¹⁵** |
| Unsöld's theorem through the angular machinery | **3 × 10⁻¹⁴** |
| ζ independent of m_a, as Wigner–Eckart requires | **5 × 10⁻¹⁵** |
| **the Coulomb channel of the general reduction against the Marvin M⁰ sum** | **5 × 10⁻¹⁵** |
| the chain's radial machinery in the hydrogenic limit | ⟨1/r³⟩ to **0.04–1.3 %** |

**Two real faults were caught by these.** Unsöld failed at first — converting a positive-order Legendre function
to negative order by hand *while also* normalising with |m| double-applies the factor, and the sum read 0.6347
where it must be 0.8463. And the Marvin inner integral was off by a **constant 0.3 % on every row** until it was
matched to the chain's own quadrature convention, `cumsum(w) − 0.5w`, read out of `t7b_hf.Yk` rather than guessed.

## 5. The result

| row | nuc | direct | exchange | total | measured | ratio | (nuc+dir alone) |
|---|---|---|---|---|---|---|---|
| 3p Al | 82.0 | −14.1 | −6.1 | 61.9 | 74.7 | **0.829** | 0.910 |
| 4p Ga | 549.0 | −45.6 | −15.8 | 487.6 | 550.8 | **0.885** | 0.914 |
| 5p In | 1484.8 | −76.3 | −26.0 | 1382.5 | 1475.1 | **0.937** | 0.955 |
| 6p Tl | 5748.5 | −165.7 | −58.1 | 5524.7 | 5195.1 | **1.063** | 1.075 |
| 4d Y | 366.8 | −104.3 | −18.2 | 244.2 | 212.1 | **1.151** | 1.237 |
| 5d La | 713.7 | −140.9 | −22.9 | 550.0 | 421.3 | **1.306** | 1.360 |

The term is negative on every row: it improves both d rows and worsens all four p rows.

## 6. And that is the literature's own result, not a fault

M: *"seems like a calculation was truncated. or an error somewhere in the derivation. this gap/residual doesn't
make sense considering everything else is true."* Every step was re-tested — §4 is that audit, and none of it was
wrong. The answer is in Blume & Watson's paper II:

> *"Excellent agreement of this theory with experiment is obtained for the 2p and 3d shell **ions**, while
> calculations using the familiar ⟨∂V/r∂r⟩ expression for the coupling constant lie 10 to 20 % too high."*

> *"For the 3p and 4p shell **atoms**, the calculated coupling constants based on the **exact theory** and on the
> ⟨∂V/r∂r⟩ expression **both tend to lie below the experimental values**, and an explanation for this disagreement
> is suggested based on the **noded nature of the outer-electron radial wave functions** for these atoms."*

**⟨(1/r)∂V/∂r⟩ is so94's form** — what `fieldresidue` uses. It comes out 9 % below at 3p and 8.6 % below at 4p;
the exact two-electron theory takes them *further* below, to 17 % and 11 %. **Both below, the full theory worse
than the approximate one, at exactly the shells Blume & Watson name.** Nothing here was fitted to that, and
reproducing a published counter-intuitive result is the strongest evidence in this pass that the reduction is
right.

**So gate (d) is not a failure of the operator.** The p rows are a limitation named in 1963 — a Hartree–Fock
orbital whose outer radial function has nodes — and `FINDING-R4-21` measured its size independently from the
other side, where the *correlated* orbital raises ζ by 7–9 % at exactly those rows. **Two routes, one cause.**

## 7. What this changes in the object, and it is nothing

`fieldresidue.py` keeps `so94`'s ζ. R4-21 measured that the choice is not decided by the six rows — worst
residual 0.00375 against 0.00381 Ha — and that the 5f figure moves **0.019 eV** across the entire range the six
rows allow. **The two-electron term is now built rather than hypothesised, and it does not move a figure.**
Recorded, not repaired.

## 8. What is owed

1. **The d rows are not explained by this.** Blume & Watson's excellent agreement is for 2p and 3d **ions**;
   Y and La are neutral atoms with one d electron outside a closed core plus s², and they remain 15 % and 31 %
   high with the full term. Whether that is the same nodal cause with the opposite sign is not established here.
2. **rad2 and rad3·A3r have no absolute anchor of their own** — the Coulomb anchor reaches only the k = 0 path.
   They are validated by the brute-force decomposition test and by m_a-independence, which is strong but is not
   the same as an independent physical anchor.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.
