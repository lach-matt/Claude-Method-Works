# FINDING R4-22 — ruling 8(c) settled. `t7c_cuaudit.py` is absent and will not be recovered; **its whole interface is eight names, seven pinned by held files, and the eighth pinned by a held implementation of itself.** The gate: the held `corr_ring.py`, run unmodified against the reconstruction, reproduces `FormS` **bit-identically**. NOT REPAIRED.

Measured 6 September 2026 on M's ruling 8(c): *"`t7c_cuaudit.py` is absent from the repository and its S-form
potential is reconstructed — settle it."*

`method/proofs/cuaudit.py` (new). **Selftest 16 of 16.**

## 1. The file is absent, and asking again will not produce it

- `recovered/` does not hold `t7c_cuaudit.py`.
- The record's own route to it is a **second absent file**: *"t7c_cuaudit.py = t7c_corrz.py VERBATIM + env
  FENT"* (`PREDICTION-CU-AUDIT-SESSION-24`), and `recovered/` holds only `t7c_corrz_run.py`.
- **Neither name appears anywhere in `COVERAGE.tsv`** — the bundles never cite either in filename shape, which
  is exactly the reach limit `docs/RECOVER.md` records for `recover.py`'s wanted-set. No re-run of that
  instrument can reach them, however often it is repeated.

That is the first half of settling it: the absence is explained, not merely observed.

## 2. The interface is eight names, and it is read off the held importers rather than guessed

Every consumer of the module is held. MEASURED across all three, the module is reached through **eight names and
no others** — the selftest asserts the census, so a new consumer cannot widen it silently:

| | names used |
|---|---|
| `hfc2.py` | `E0B` `LAM1` `_lam1` `_lam0` `_e0a` `v_gbz` |
| `corr_ring.py` | `E0B` `_SUBCELL` `_frac_neg` `_lam0` `_e0a` `v_gbz` |
| `hfterm.py` | `v_gbz` |

## 3. Seven of the eight are pinned by a held file

| name | pinned by | |
|---|---|---|
| `E0B` | `sox_table.py:7` = 0.0241792 Ha | the **exactly known** Onsager–Mittag–Stephen 1966 constant, which `soxquad.py` now reproduces from the corpus's own reduction to +0.047 % (`FINDING-R4-20`) |
| `_lam0(z)` | `ring_zeta.cL(z)/2` | the RPA ring integral's log coefficient, session 23 |
| `_e0a(z)` | `ring_zeta.eps_r(0.005,z)/2 − λ₀ ln 0.005` | **gated on GB-ZETA-RING-23's six recorded c₀(ζ)**, worst 4.5 × 10⁻⁶ Ha |
| `LAM1` | `hfc2.py`'s own guard `if T.LAM1` | the branch is dead in every run the record reports |
| `_lam1(z)` | reachable only through `LAM1` | never evaluated |
| `_SUBCELL` | env `SUBCELL=1`, session 28 | the setting every S-form row the record reports was run at |
| `_frac_neg` | **`cellcut.py`, held** | loaded by path, never copied |

`_e0a` **is** c₀, not c₀ − E0B: both `hfc2`'s chain form and `FormS`'s add E0B *beside* it. My first check
subtracted it and failed by 0.0242 Ha, which is E0B itself — the check was wrong, not the reconstruction, and it
is recorded here because the coincidence is exactly the kind that reads as a real discrepancy.

## 4. And the eighth — the one that was called RECONSTRUCTED — is pinned by a held implementation of itself

`corr_ring.py` is held, and its second line declares what it is:

> *"Same interface as `t7c_cuaudit.v_gbz` / `hfc2.eps_c` so it can be patched in: `T.v_gbz = v_R`;
> `H.eps_c = eps_R`."*

So a **complete, held, runnable implementation of `v_gbz`** exists — for form R. And `fieldresidue.FormS` is that
implementation with **the S table in place of the R table**, which is the one declared substitution and is what
*form S* means.

**THE GATE, and it is not circular.** This instrument supplies the seven pinned names; the held `corr_ring.py` is
then imported against it **unmodified** and run; and `FormS` is built on the **ring** table — the same table
`corr_ring` reads — and the two compared point by point over ten densities and four spin polarisations:

| | max \|difference\| |
|---|---|
| `FormS.eps` against `corr_ring.eps_R`, ζ = 0, 0.3, 0.7, 1.0 | **0.0** |
| `FormS.v` against `corr_ring.v_R`, ζ = 0, 0.3, 0.7, 1.0 | **0.0** |

**Bit-identical, both functions, every ζ.** So what was carried as a reconstruction of a *shape* is a
re-tabulation of a *held* shape. The status of the S-form potential is no longer "rebuilt from the record's own
description"; it is "the held form-R implementation, on the S table".

## 5. What remains unpinned, so it is not lost

The module's own **private text**: its docstring, its argument parsing, the `FENT` and `FOCC` environment
switches that made it *"t7c_corrz.py VERBATIM + env FENT"*, and anything else it held beyond the eight names.
None of it is reachable and none of it is used by the object.

**The status stays RECONSTRUCTED and is never flattened** — `CLAUDE.md`'s standing rule. What ruling 8(c) asked
was that it be settled, and settled means: the absence explained, the interface closed and asserted, seven names
sourced, the eighth shown bit-identical to a held implementation, and the remainder named.

## 6. Ruling 8 in full

| | |
|---|---|
| **8(a)** the g_2b quadrature | **REPAIRED, CONVERGED, PROVEN** — `FINDING-R4-20` |
| **8(b)** the spin–orbit ζ | **WORKED AND BOUNDED, NOT REPAIRED** — the fault is not the operator, and the repair needs an object the corpus does not contain; **a question is put to M** — `FINDING-R4-21` |
| **8(c)** `t7c_cuaudit.py` | **SETTLED** — this finding |

Nothing is repaired in any volume, and nothing in `recovered/` is touched. Every figure here is MEASURED by the
instrument or RECORD-CARRIED with its quote.
