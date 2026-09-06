# FINDING R4-14 — the 5f binding energy at protactinium is in the corpus, its producer runs again from the repository, and with the entrant's own electron the entry point sits at √(ℓ(ℓ+1)/2) within one percent at p, d and f alike. NOT REPAIRED.

Measured 6 September 2026, on M's direction: *"I'm certain that we can produce exactly what we are
looking for and prove it with everything we have avail to us … remember that one of the laws of a
closed index is that there are no more questions left to be had or asked about its subject matter."*
`method/proofs/fieldentry.py`, its banked output `fieldentry.out`, and the field file
`fieldentry-field.json` it writes; selftest 30 of 30.

## 1. What R4-13 said, and what was wrong with it

R4-13 ran the f test on protactinium's first ionisation energy (+4.0 %), then said the point reads
the wrong electron — an actinide ionises from 7s — and closed with *"a subshell-resolved binding
energy for the 5f electron at protactinium … Not in the corpus."*

**It is in the corpus, six times.** The Löwdin work's derived field — the sealed chain,
scalar-relativistic Hartree–Fock on the ruling field (hfc2, SR, CORR=False, c = 137.035999),
reference the cation of Z carrying config(Z−1) — carries the 5f channel's energy at Z = 91 as its
entrant row, **D = −0.30535 Ha**, quoted at `BRIDGE-LOWDIN-SESSION-55.md:71`,
`SCORE-TIEBREAK-CONTROLS.md:28`, `PREDICTION-Z90CONFIRM.md:9`, `DELIVERABLE-4-THE-TRANSIT-WIDTH.md:39`,
`DELIVERABLE-3-COLLAPSE-CONDITION.md:49` and `BRIDGE-LOWDIN-SESSION-49.md:34`. And DELIVERABLE-3 §3
had already converted it: **n\* = 1/√(−2D) = 1.2796, δ = n − n\* = 3.7204** — which is exactly
a_meas for 5f at Pa, since p = 1. The record computed the entry-point quantity from its own field
and used it for the collapse condition, never for t. The same is true of every sealed p and d
opening row: 4p at Ga, 5p at In, 4d at Y, 5d at La are all quoted, and 3p at Al and 6p at Tl are
quoted nowhere.

## 2. The producer, rebuilt from the repository, and the proof that it is the same producer

The sealed runtime (packs 5–48 layered into `rt/`) is not in the repository; what is here is the
chat-extracted text of its modules under `recovered/`, several of them earlier drafts than the ones
that ran. `fieldentry.py` loads them **by path, in dependency order, registered under their own
names** so their bare-name imports resolve — `tfd rad step2_run eigen_fix derive_P ground
(= LW1-ground.py, a seated member) hfs t5_scf t7b_hf t7c_kernel t7c_hfsr hfc2 nlchain` — compiles
the C Numerov from `recovered/shoot_x.c` into a temporary directory, and departs from the recovered
text in exactly four places, each declared in the instrument's docstring and each gated:

| | departure | status | gate |
|---|---|---|---|
| (a) | nlchain's reference is the **cation** of Z carrying config(Z−1); the recovered file is the first build, whose reference sat at nuclear charge Z−1 | the record's own fix, `FINDING-CHAIN-SESSION-40` §1 (F40.1) | Li 2s −0.19629 |
| (b) | t7c_hfsr calls a **14-argument** shoot_x — two doubles seeding the inward particular branch — that the session-18 `shoot_x.c` (12 arguments, the only C file recovered) lacks; written here as that routine with the seeds replacing its adiabatic start | RECONSTRUCTED | He 1s at c = 1e6 → **−0.91796** (the record's G1) |
| (c) | the seed bisections ride `rad._shoot`, which rescales by 10²⁰⁰ and integrates on into the region h²q/12 > 1, where the Numerov recursion flips sign every step and the bisection returns its bracket cap for every 1s at Z ≥ 10 (−50.0 at Z = 10, −4140.5 at Z = 91); the outward integration now stops at \|y\| > 10¹⁵⁰, which always precedes that region; the sealed runtime rode a C `shoot.c` that is not here | RECONSTRUCTED | hydrogen's defects vanish (2 × 10⁻¹⁰); H 1s and Z = 70 1s land on Dirac (the kernel's own gates); TFD seeds node-clean to Z = 91 |
| (d) | the recovered `derive_P.numerov_wf` lacks the forbidden-region tail clean that `t7c_kernel.numerov_wf_sr` carries *"as hfs.numerov_wf"*; the clean is appended verbatim | RECONSTRUCTED | the same seeds |

`t7c_cuaudit.py`, which hfc2 imports at module level, is absent; it is reached only through the
correlation path, which the chain runs with CORR=False, and a stub that raises if called stands in.

**The gate on all four together is reproduction of the sealed rows, and a seed cannot change a
converged Hartree–Fock energy.** Every row the record quotes that the instrument can reach was
regenerated, and every one lands to the fifth decimal:

| Z | row | sealed | regenerated | diff |
|---|---|---|---|---|
| 11 | 3s (PC-0) | −0.18217 | −0.18217 | 0 |
| 19 | 4s · 4p · 3d (PC-0) | −0.14774 · −0.09363 · −0.05807 | −0.14774 · −0.09363 · −0.05807 | 0 · 0 · 0 |
| 31 | 4p | −0.20007 | −0.20007 | 0 |
| 49 | 5p | −0.18833 | −0.18833 | 0 |
| 39 | 4d | −0.195614 | −0.19561 | 4 × 10⁻⁶ |
| 57 | 5d | −0.20585 | −0.20585 | 0 |
| 58 | 4f | −0.36700 | −0.36700 | 0 |
| 91 | 5f · 6d, the chain's step, margin 81.95 mHa | −0.30535 · −0.22340 | −0.30535 · −0.22340 | 0 · 0 |

Nine sealed rows from Z = 11 to 91, all reproduced. **The producer here is the producer there in
every respect that reaches a number.** The chain's step at Pa also returns what the record did not
print: 7p −0.13748, 8s −0.07563, 8p −0.05189.

## 3. What is new: three field values the record never had

| Z | opening | D (Ha) | eV | how |
|---|---|---|---|---|
| 13 | 3p at Al | **−0.20171** | 5.489 | the 3p removal from the observed ground; quoted nowhere |
| 81 | 6p at Tl | **−0.17934** | 4.880 | the 6p removal from the observed ground; quoted nowhere |
| 91 | 5f at Pa, **the atom as it is** | **−0.18054** | 4.913 | the 5f removal from the observed ground 5f² 6d¹ 7s² → 5f¹ 6d¹ 7s² |

The third is the number M asked for. It differs from the chain's row because they are different
quantities: the chain's −0.30535 is the energy of *adding* a 5f electron to the thorium-configured
cation 6d² 7s² — the walk's decision quantity, on a configuration (5f¹ 6d² 7s²) that is not
protactinium's — while −0.18054 is the energy of *removing* a 5f electron from protactinium's
observed ground. At every other opening the two coincide, because the entrant shell holds one
electron there; only at Pa, an aufbau exception (register 1333), do they part. Register 1337 reads
the atom as it is — its own first ionisation energy — so the like-for-like right-electron reading
is the observed-ground one.

## 4. The entry point, two readings at every two-sided opening

| opening | first IE t | t / form | entrant's own electron, t | t / form | source of D |
|---|---|---|---|---|---|
| 3p Al | 1.0925 | 1.0925 | 1.0436 | 1.0436 | here |
| 4p Ga | 1.0331 | 1.0331 | 1.0020 | 1.0020 | sealed |
| 5p In | 1.0124 | 1.0124 | 0.9730 | 0.9730 | sealed |
| 6p Tl | 1.0237 | 1.0237 | 0.9513 | 0.9513 | here |
| 4d Y | 1.8453 | 1.0654 | 1.7578 | 1.0149 | sealed |
| 5d La | 1.7240 | 0.9953 | 1.7264 | 0.9967 | sealed |
| 5f Pa | 2.5476 | 1.0401 | **2.4420** | **0.9970** | here, observed ground |
| 5f Pa, the chain's row | | | 2.7235 | 1.1119 | sealed |

| | first IE | entrant's own electron |
|---|---|---|
| p, four openings | +4.04 % | **−0.75 %** |
| d, two openings | +3.04 % | **+0.58 %** |
| f, one opening | +4.01 % (wrong electron) | **−0.30 %** |

**With the right electron the three ℓ values agree with √(ℓ(ℓ+1)/2) and with each other to within
a percent.** The drift R4-13 reported — 1.028, 1.030, 1.040 — was the f point reading the 7s
electron; read on its own electron, f sits closer to the form than either p or d. The 5f point
under the finished form, with one 5f already present in the radicand (1 + 1/14), is 2.3592
(−3.7 %); the node-only form is register 1337's convention and is the one tabulated.

## 5. What the field's own drift is, and that it is not the law's

The p row on the field runs 1.044 → 1.002 → 0.973 → 0.951 along n: it falls *through* 1, where
the first-ionisation row approaches it from above. The field is scalar-relativistic Hartree–Fock
with **no spin–orbit and no correlation** (`FINDING-CHAIN-SESSION-40` §7: *"No terms, no SO, no
correlation … No constant beyond c"*), and both shortfalls grow with Z. The corpus's own spectra
store measures one of them: `spectra-levels-store/deliver/queue2/TlI.tsv` lines 13–14 put Tl I's
6p ²P₃⸝₂ at 7792.7 cm⁻¹ above ²P₁⸝₂, and `MEASUREMENTS.tsv` puts the limit at 49266.66 cm⁻¹, so the
**j-averaged** 6p removal energy — the quantity a scalar-relativistic field computes — is
44071.5 cm⁻¹ = 5.4642 eV, and reads **t = 0.9888**. Of the 0.072 between the first-IE reading
(1.0237) and the field's (0.9513), 0.035 is spin–orbit and 0.037 is what the field lacks besides,
which is correlation-sized: the field underbinds the observed removal energy by 0.50 eV at Al,
0.56 at Ga, 0.66 at In and 0.58 at Tl (against the j-average). **Neither is a property of the
form.** Register 1337's *"common factor of 1.029 … not derived"* is the difference between an
observed removal energy and the field's, of order half an electron-volt, appearing in t as a few
percent — at p, at d, and, once the right electron is read, at f.

## 6. What this closes, and what it does not

**R4-13's open question is closed as far as the corpus's instruments reach.** Whether the
multiplicative factor is common across ℓ is answered: on the corpus's own field it is 1.00 ± 0.01
at p, d and f; on observed quantities it is +3 to +4 % at p and d, and f has no observed
quantity to read. The 2.9 % is not a regularity of the form and not a coincidence of two points;
it is the input. Register 1337's *"no f test — no f subshell has a two-sided corridor"* is
superseded under `RULINGS-R4e.md` §1, which admits the g channel and gives 5f a floor: the f test
exists, and it reads −0.3 %.

**What the corpus cannot do, stated so it is not asked again.** Sharpen any of these below the
percent: that needs a correlated, spin–orbit field, which the Löwdin work refused by construction,
or a measured 5f binding at protactinium, which the survey does not hold — every Z = 91 row of
`COORDINATES.tsv` is *computed, unwitnessed, "open-shell core, 119 parents"*. The survey's own
channel-equation defect for 5f at Pa, δ = 3.25918, would read t = 2.386 (−2.6 %); it is the output
of a fitted closed form whose predecessor is withdrawn (`HANDOFF-8.md`: *"fifteen objects still rest
on the withdrawn channel equation"*) and is recorded here, not used.

## 7. Owed to M, none of it done

1. **Register 1337 and §34.7 say "no f test".** Under the g ruling there is one, and it reads within
   a percent on the entrant's own electron. Whether the volume carries it is his.
2. **Two readings of one quantity.** The volume reads t on first ionisation energies; the field
   reading — the right electron, the corpus's own numbers, three ℓ values within a percent — is
   the stronger statement of the law and is not in any volume. Whether it goes beside the first, and
   whether 3p at Al and 6p at Tl (MEASURED here, never in the record) are figures for it, is his.
3. **The chain's Pa row and the atom's Pa row are different quantities** and the prose that quotes
   either must say which. Nothing in the volumes currently quotes the field at an opening.
4. **Two RECONSTRUCTED repairs stand in the instrument** — the C shoot and the tail clean — with
   the sealed C source absent. Their status is recorded in the docstring and is never flattened;
   what they touch does not reach a converged energy, and nine sealed rows say so.

## 8. Corrections to my own record

- R4-13 *"Not in the corpus"*: **withdrawn**, above.
- R4-13's q = 0 extrapolation: **withdrawn** in that file's own correction, on register 1353.
- R4-13's *"the f point is reading the wrong electron"*: right, and the right electron lands on the
  form; the sentence that followed, that nothing in the corpus could read it, was the error.
- Third time in this pass the record held what I called absent. **Read the Löwdin deliverables
  before saying a field quantity does not exist; the field was built to produce exactly these.**

Nothing is repaired. Every figure here is MEASURED by the instrument or RECORD-CARRIED with its
quote; the two RECONSTRUCTED items are named as such and gated on nine reproductions.
