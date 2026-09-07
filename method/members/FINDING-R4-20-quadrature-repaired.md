# FINDING R4-20 — ruling 8(a) discharged. The 1 % was never the record's: `sox_qres.py` reached this repository as the snapshot from **before** the record's own numerical fix, and its own comment documents the fault. The fix is implemented from the record's sentence, lands on a sealed golden nothing here is fitted to, and converges. NOT REPAIRED.

Measured 6 September 2026 on M's ruling 8: *"they are all work. they must be repaired, worked, and then
verified/proven completely."* Item (a) was *"the g_2b quadrature runs 1.0 % low at the recovered defaults —
converge it."*

`method/proofs/soxquad.py` (new), banked `soxquad-converge.json` and `soxquad-table.json`, with the S-form tables
and all twenty rows of `fieldresidue.py` rebuilt through it. **Selftest 12 of 12 (soxquad), 106 of 106
(fieldresidue).**

## 1. The fault is the record's own, and the record had already fixed it

`FINDING-SOSEX-SESSION-32`, in the middle of a paragraph headed *"Numerical fault found and fixed BEFORE the
table"*:

> *"a uniform P_perp^2 grid leaves 1/|q+P|^2 unresolved near P_par → −q; a per-column grid uniform in
> ln(w_q^2 + v) absorbs it exactly (**was 1 % low**; now 3e-4 converged)."*

`BRIDGE-LOWDIN-SESSION-32` §4 repeats it as the session's one numerical note: *"Numerical fix before any read:
P_perp^2 grid → ln(w_q^2+v) grid (was 1 % low on g_2b)."*

**And `recovered/sox_qres.py` still lays down the uniform grid** — line 35, `v=4*(np.arange(NPV)+0.5)/NPV`, with
the file's own line-33 comment naming it: *"Pperp^2 = v uniform in (0,4)."* The recovered text **documents the
fault in its own comment**, because it is the text as it stood before the fix was typed in place.

So the deficit `FINDING-R4-15` recorded was never a limit of the record and never a limit of the reduction. It is
a limit of what the chat export carried: the session fixed the grid, ran its table on the fixed quadrature, and
the pre-fix file is what `recover.py` extracted. **This is what `CLAUDE.md` means by "parse before trusting a
recovered `.py`", one level deeper: a recovered file can be complete, parse, run, and still be superseded by its
own session.**

## 2. The deficit, measured — and it is the record's number to the digit

| | g_2b(1.44881) | vs the record |
|---|---|---|
| the recovered text at **its own defaults** (160,160,96,96) | 0.0290910 | **−0.998 %** |
| the recovered text at the record's golden mesh (80,80,64,128) | 0.0291712 | −0.725 % |
| the recovered text with the P_⊥ mesh doubled (160,160,96,192) | 0.0292317 | −0.519 % |
| the recovered text at **four times the resolution in every direction** (320,320,192,192) | 0.0292284 | **−0.530 %** |
| **the record's fix, at the record's golden mesh** | **0.0293844** | **+0.0004 %** |
| the record's own banked value, README-HANDOFF-32 gate (51) | 0.0293843 | — |

**−0.998 % is the record's own "was 1 % low", reproduced.** And rows three and four are the point. The deficit is
governed by the P_⊥ count **alone** — the two rows at NPV = 192 agree (−0.519, −0.530) while sixteen times the
work separates them — and it falls only **about half per doubling of NPV**, because a uniform v grid leaves every
column with w² ≪ Δv unresolved and that set shrinks logarithmically. Reaching the fixed grid's accuracy by brute
force would take NPV of order 10⁵. **Resolution cannot fix this integrand; only the grid can** — which is what
*"absorbs it exactly"* means, and why the record changed the variable rather than the count.

## 3. The fix, and why it is exact rather than fine

The singular factor is 1/|q+P|² = 1/(w² + v) with w = q + P_∥ and v = P_⊥². Substituting s = ln(w² + v) gives
dv = (w² + v) ds, so

> r / ((w² + v)(q w)) **dv** = r / (q w) **ds**

and the singularity is **gone from the integrand**, not resolved. The column's upper limit is set to the exact
support boundary v_max = 4 − P_∥² (|P| ≤ 2, since P = k₁ + k₂ with both |k| < 1), which replaces the recovered
text's cell-wise mask and is the second half of the same repair.

**`rho_q` — the lens pair density, the whole physical content of the reduction — is the recovered function,
called verbatim through the module.** Six lines of grid are what changed. That is the one declared departure.

## 4. Four gates, and two of them the record did not have

**(1) The record's sealed golden.** README-HANDOFF-32 gate (51): *"python3 sox_qres.py 1.44881 … (NZ=80 NU=80
NPP=64 NPV=128) reprints g2b_Ry 0.0293843."* Nothing here is fitted to it — the grid was written from the
record's sentence, not from its number — and it returns **0.0293844**, one part in 3 × 10⁵. **That is what
identifies the grid the sentence describes**, and it recovers a value the recovered text cannot produce at any
mesh.

**(2) The ball autoconvolution**, the record's own internal check, run through the unchanged `rho_q`: max relative
error **3.2 × 10⁻⁴**, which is the record's own *"ball autoconvolution check 3e-4"*.

**(3) The analytic large-q limit — which the record does not state.** For q > 2 the lens L_q is the whole unit
ball, so ∫d³P ρ_q = |L|² = (4π/3)², and |q+P|²(q² + q·P) → q⁴, giving

> **g_2b(q) → (3/16π⁵) · 4π · (4π/3)² / q⁴ = 4/(3π² q⁴).**

Measured, the ratio to that limit is 1.114 at q = 4, 1.026 at q = 8, **1.006 at q = 16**. **It fixes the
prefactor 3/(16π⁵) independently of E0B** — the record confirmed that prefactor *by* E0B, so this is the first
check of it that does not use the constant the form is later gated on.

**(4) G-S1 against the exactly known constant** — §5.

## 5. Convergence, the two meshes separated — and the record's own +1.5 × 10⁻⁵ is identified

| | q = 0.05 | q = 0.516 | q = 1.44881 | q = 2.5 |
|---|---|---|---|---|
| lens mesh NZ = NU = 40 | 0.0014668 | 0.0146230 | 0.0294525 | 0.0048009 |
| **80** (the record's own) | 0.0014664 | 0.0146098 | **0.0293844** | 0.0047976 |
| 160 | 0.0014661 | 0.0146072 | 0.0293707 | 0.0047969 |
| 240 | 0.0014661 | 0.0146067 | 0.0293673 | 0.0047968 |
| P mesh (32, 64) | 0.0014645 | 0.0146004 | 0.0293876 | 0.0047976 |
| (64, 128) | 0.0014664 | 0.0146098 | 0.0293844 | 0.0047976 |
| (128, 256) | 0.0014670 | 0.0146129 | 0.0293865 | 0.0047980 |

**The P mesh is converged at the recovered (64, 128)** — doubling it moves the peak by +0.007 %. **The lens mesh
carries the whole residual**, and it converges as h²: at the peak the ladder at P = (96, 192) runs 0.0293716 →
0.0293701 → 0.0293691 for NZ = 160, 200, 240, an h² limit of **0.0293669**. The production mesh (160, 160, 96,
192) sits **+0.016 %** above it.

**So the record's own NZ = NU = 80 sits +0.060 % above that limit — and +0.06 % is exactly the residual the
record recorded on G-S1**: *"∫g_2b dq = 0.0241943 Ha vs E0B 0.0241792, +1.5e-5"*, which it called agreement to
0.06 %. **That residual is not the reduction. It is the (z, ρ) lens mesh, and it converges away.**

**And the q grid is converged too**, measured at a deliberately coarse lens mesh so the q error reads alone:
n = 101 → 201 over [0.02, 30] moves G-S1 by 0.002 %, and over [0.002, 120] by 0.010 %. The two ranges differ by
0.02 %, which is the tail convention (g ~ q below, g ~ q⁻⁴ above) and is the largest single term left in the
budget. **Error budget at the production mesh: lens +0.016 %, P mesh ~0.01 %, q grid ~0.00 %, tails ~0.02 %.**

## 6. Repaired, and it lands on the constant more closely than the record's own gate did

| ∫ dq g_2b | Ha | vs the exact E0B |
|---|---|---|
| the pre-fix table | 0.0239502 | **−0.947 %** |
| **the repaired table** | **0.0241905** | **+0.047 %** |
| the record's own reading | 0.0241943 | +0.062 % |
| **E0B, Onsager–Mittag–Stephen 1966** | **0.0241792** | — |

The table is on the pre-fix table's own 130-point q grid, so the quadrature is the only thing that changed, and
three rows recomputed through the instrument reproduce the banked values **bit for bit**.

**And PS-1 confirms it independently.** ε_2x^scr/E0B at r_s = 2 is a *screened* quantity — a different functional
of the same g_2b(q) — and the record printed it at both spins:

| | ζ = 0 | ζ = 1 |
|---|---|---|
| the pre-fix table | 0.6685 | 0.7942 |
| **the repaired table** | **0.6744** | **0.8015** |
| the record | 0.6747 | 0.8019 |

**−0.05 % at both spins**, from −0.9 %. Two independent functionals of the repaired g_2b land on the record's two
numbers at once.

## 7. What the repair moves downstream, measured after the fact rather than argued before it

`FINDING-R4-15` claimed the deficit *"costs nothing on the O path"*. That was read off the sealed rows before the
repair existed. **Now it is measured by doing the repair and re-running all twenty rows:**

| | pre-fix | repaired | move |
|---|---|---|---|
| the five sealed ΔEc_S gate rows | −0.03188 … −0.00675 | unchanged to 5 dp | **+0.002 to +0.005 mHa** |
| the six anchored openings, D_tot | | | ≤ 0.004 mHa |
| **protactinium's 5f removal** | **6.949 eV** | **6.948 eV** | **−0.001 eV** |
| **t(5f)** | **2.6359** | **2.6359** | **0** |
| ytterbium's residual | −0.11140 Ha | −0.11141 Ha | −0.01 mHa |
| the ladder's seven rows | | | ≤ 0.07 mHa |

**Every figure of `FINDING-R4-15` through `R4-19` stands.** The claim that the deficit cost nothing was true, and
it is now established by measurement instead of inference.

## 8. Two things the repair found that were not being looked for

**(a) A limit of the recovered w_q grid at large q, recorded and not repaired.** The table's last four rows
(q > 80) do not carry the analytic tail coefficient: the ratio is 1.0005 at q = 71 and 0.856 at q = 120. The cause
is measured and it is the recovered grid, not the fix. For q > 2 the lens is the whole ball, so ρ_q is nonzero
only for |P| ≤ 2 — that is w_q ∈ (q−2, q+2), a window at the **top** of the (0, 2+q) range — while the recovered
u² stretching puts the points at the **bottom**. A row therefore carries about 2/√(q(2+q)) of NPP: 40 points at
q = 4, 6 at q = 30, **under 3 above q = 80**. The coefficient holds to 1 % from q = 13 (where the asymptote is
first reached; below it the departure is the physical O(1/q²) term, +6.7 % at q = 5) to q = 71, and breaks exactly
where the points run out. **Recorded, not repaired**: repairing it would be a second departure from the recovered
text, and dropping every unresolved row moves G-S1 by 2 × 10⁻⁷ of itself.

**(b) A correction to `FINDING-R4-19` §4 — mercury, not gallium, is the ladder's worst row.** Making the report
compute its own figures instead of printing fixed text surfaced it: Hg 5d is **−0.01806 Ha** and Ga 4s
**−0.01740**. R4-19 wrote *"the ladder's worst row (gallium)"* while quoting **0.018 Ha** as the bound — and
0.018 is mercury's number, not gallium's. **The bound is right and its attribution was wrong.** Gallium is the
largest *one-sibling* residual, which is the row class protactinium belongs to and is why it was the one named;
its 3d¹⁰ reason stands for that. **The 0.47 eV bound on protactinium is unchanged**, because it was always the
larger of the two. The correction is appended to R4-19.

**Both are the same lesson, and it is the one this pass keeps re-learning:** a number that is written down rather
than computed drifts silently. The report now derives every figure in that paragraph from the table above it,
which is `docfigures.py`'s discipline applied inside an instrument.

## 9. What is owed

1. **Ruling 8(b) and 8(c) are untouched by this** and remain the standing work — the spin–orbit ζ (9 % low at p,
   36 % high at 5d against the store's measured intervals) and `t7c_cuaudit.py`'s absence.
2. **`tools/docfigures.py` reports 15 of 59 pinned figures stale**, none of them from this pass: they are the
   store-state drift (`CLAUDE.md` says 343 members against 667 measured; `docs/REGISTER-GAPS.md` says 1,660
   Register entries against 1,702). Named here because the tool was run, not repaired here.

Nothing is repaired in any volume, and nothing in `recovered/` is touched — it is a generated tree and the pre-fix
text is part of what it records. Every figure here is MEASURED by the instrument or RECORD-CARRIED with its quote.
