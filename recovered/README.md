# THREEBODY-DELIVERY-1 — README

Delivered by the three-body project, 2026-09-01, in answer to REQUEST — THE METHOD 1.6 BUILD
(chat 128; BUILD90 main, BUILD157 compendia). Baseline confirmed: the project's `The_Method_1_6.md`
is 738,550 B, md5 49900cf41f818ab789bb90fc596ac977 — identical to the build's original.

## The standing fact this delivery rests on

The three-body work was one chat (`Project scope review`, id b778e075-7807-4392-8a24-2dfc864468bc),
concluded **2026-08-23 22:06:58 UTC**. Its container was never sealed and its outputs folder was never
uploaded. **Nothing from that session survives as a file** except the paper's PDF in Prints & Proofs.
Every instrument below was recovered line-by-line from the chat transcript and re-run here. They are
therefore **labelled reconstructions**, not files-as-produced, and carry no md5 of an original.
The test that they are faithful: every printed figure in the record reproduces exactly (see §Runs).
This is a finding of the three-body project, severity FOUNDATIONAL for objects 1–4 and 9.

## Status of the ten objects

| object | status | where / what |
|---|---|---|
| 1 `tb_audit.py` (1756; §36.2) | RECONSTRUCTED + RE-RUN | The record's `tb_audit.py` was named **`audit.py`** in the session. `audit.py` (corrected state) and `audit.log` (78/78). Thirteen order-types are the `cases` dict at its head; symmetry orders 6/2/1 print as `|S|=`. Inputs: none (seeded RNG 7). One seam: the comment line marked `[SEAM]` above check B was not recoverable verbatim. |
| 2 triangle-form closure (1716) | **`3B.tri` NOT A FILE** + RE-RUN | `3B.tri` is the Index of Indices object label, never a file. The closure is `audit.py::closure_test(cap)` — the project's **own** min/max operator on the integer cell set {\|a−b\| ≤ c ≤ a+b}, **not** the book's `tower-2.py`. `caps_table.py` → `caps_table.log`: caps 3–12, 12·111·477·1488·3780·8385·16812·31227·54555·90705 meet, 0 join, chain 0. |
| 3 N₈ (1719, 1720) | RECONSTRUCTED + RE-RUN | `n8_check.py` → `n8_check.log`. The withdrawn polynomial is line `claim=` **with its coefficients exactly as first written** (U⁴: 6S₂²−4S₄+8S₁₁; U²: −4(S₂³−S₂S₄+2S₆); const: (S₂²−S₄)²−64u₁²u₂²u₃²). Second route = the explicit product over (ℤ/2)³. Log prints `False` for the withdrawn form, `True` for N₈, 0 at u=(3,5,7), and isolates the two wrong terms: ΔU⁴ = −4(p²−6q) (i.e. withdrawn = 2p²+16q vs true 6p²−8q, as 1707 states). |
| 4 shape-potential audit, both states (1718, 1722, 1723) | RECONSTRUCTED + RE-RUN, BOTH | `audit_state1_failing.py` is the first-run state: line 58 `Vs=V0_shape(w,m)/R` (hyper-radius carried in); `audit_state1_failing.log` shows check A **False 13/13**, all else True. The in-session fix was `sed 's|Vs=V0_shape(w,m)/R|Vs=V0_shape(w,m)|'`, giving `audit.py` line 58. Normalisation: Montgomery 2014 — `jacobi()` eq (26), `shape()` eq (33), c_ij=(m_i m_j)^{3/2}/√(m_i+m_j), d_ij²=‖w‖−w·b_ij, identity r_ij²=d_ij²/μ_ij (numerically 1.5, 0.833, 1.333 at m=(1,2,3)). |
| 5 mass-uniformity (§36.4) | DERIVATION (no separate code) | Read off `audit.py`: masses enter only `jacobi()` (μ₁, μ₂ → the rays via `binary_rays`), `V0_shape()` (c_ij), `euler_roots()` and check D. `closure_test()` and `P8` take **no mass argument**; the metric is not coded. That is the law: masses → six numbers (three c_ij, three b_ij); S², K₃, N₈ mass-free. |
| 6 stratification as index (1713, 1714) | **NOT HELD — never data** | E(𝔉)=0 was a theorem-assembly, not a computation: exhaustive by the Chazy asymptotic classes, disjoint up to measure zero by Saari 1971/73 and Painlevé (n=3). No data object was ever built; the Brudno step is a citation. The book should label these record-carried. |
| 7 five points, threshold (§36.3) | RE-RUN + CITED→COMPUTED | Euler roots: `audit.py::euler_roots` (Euler 1767 quintic, one positive root per ordering, check C). Lagrange: check D and `figs.py` (both orientations). Routh μ<0.0385209 was **cited, never computed** in the session; `routh_check.py` now verifies it as (9−√69)/18 = 0.0385208965. |
| 8 eight attribution questions (1721) | **NOT HELD as file**; ledger recoverable in transcript only in part | The ledger file was in the lost outputs folder. The seven closures and the eighth (Lagrange 1770) are as stated in the book's 1721; the source list in the project's provisional 1709 additionally names Baker–Pixley/Montanari/Dechter/Freuder for the consistency step. Not reconstructed — text, not instrument. |
| 9 five figures | RECONSTRUCTED + RE-RUN | `figs.py` (figs 1–3, incl. the in-session `view_init` patch), `figs2.py` (figs 4–5). Data read: none — all computed from `audit.py` functions. The five PNGs here are **re-renders**; the session's PNGs are lost. One seam: Fig 4 title joined across two snippets. |
| 10 paper and record | PDF HELD ON DRIVE; .md NOT HELD | `The_Three_Body_Problem_for_Unknown_Masses_Lach.pdf`, Prints & Proofs, Drive id 151Yg3WgY-aqx24jrlHdvtPK8a-rNgMKL, 340,837 B, created 2026-08-23 22:05:27 UTC — the build should md5 the Drive bytes; this project holds no other copy. The .md source (the build's 215-line member) is not held here; no difference can be reported. Register: the project's entries were provisional **1701–1712** and the chapter **Chapter 35**; the Löwdin project used the same numbers. Timestamps: Löwdin PDF 20:17:47 UTC, three-body PDF 22:05:27 UTC, chat close 22:06:58 UTC — the build's seating (Löwdin 1701–1712, three-body 1713–1724, Chapter 36) stands. Handoff and rulings exist only as chat text. |

## Environment

Python 3.12.3 · NumPy 2.4.4 · SciPy 1.17.1 (unused) · SymPy 1.14.0 · Matplotlib 3.10.8. Ubuntu 24, no network.

## Runs (all far under the 280 s gate; no reduced case needed)

| command | output | wall |
|---|---|---|
| `python3 audit_state1_failing.py > audit_state1_failing.log` | A False 13/13; cap 8 = 344/8385/0; chain 0 | 1.2 s |
| `python3 audit.py > audit.log` | 78/78; \|S\|=6,2,1; cap 8 = 344/8385/0; chain 0 | 0.9 s |
| `python3 n8_check.py > n8_check.log` | False / True / 0 / two isolated wrong terms | 0.5 s |
| `python3 caps_table.py > caps_table.log` | per-cap table 3–12 | 2.1 s |
| `OUT=. python3 figs.py; OUT=. python3 figs2.py` | fig1–fig5 PNG + caps list on stdout | 5.7 s |
| `python3 routh_check.py > routh_check.log` | 0.0385208965 | 0.0 s |

Gates the files carry: `audit.py` prints True/False per check and case; a wrong normalisation fails A
uniformly (the 1710 protocol's own trigger); `n8_check.py` prints `False` on the withdrawn form.
PNG bytes may differ run-to-run by Matplotlib version; the logs are the bankable outputs.

## Form

Every file ≤ 10 MB. `MANIFEST.tsv`: name, bytes, md5, purpose. Drive may add a `-1` suffix; the md5
decides. The Gemini working material was reference only and appears nowhere in these files.