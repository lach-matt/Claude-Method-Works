# MUCF-ENERGY-AXIS — the third axis, and the chain the two gaps share

`tools/mucf.py` · run `python3 tools/mucf.py --selftest` before trusting any figure below.

## What this records

`recovered/Muon_Catalysed_Fusion_v1.0.md` §5 states two quantitative gaps between the
demonstrated d–t muon-catalysed reaction and useful power. Its §5.1 computes the energy gap
over two axes — sticking `ω_s` and density `φ` — and concludes **"two sticking levers are
required; neither suffices alone."**

That conclusion holds the muon production cost `E_μ` fixed at 5 GeV. The same paper's §4 says
of the 16.7× gap between that figure and the 0.30 GeV kinematic floor: **"None of it is
forbidden, which makes E_μ the most tractable free parameter."** The two sections never meet,
and §5.1's conclusion is an artefact of freezing the parameter §4 nominates as most movable.

A later re-derivation found this, went considerably further, and **exists in no file of this
repository.** It is in the chat export only — conversation `transitions` (2026-08,
`drive/chats/2026-08/764406b9-5552-45a2-9bf6-adb32378bf73.json`), messages 578–594. This
document banks it. Everything marked `PROSE-ONLY` below is banked here for the first time.

## The finding, in one line

**The energy gap is accelerator-dominated, not sticking-dominated — and the accelerator gap
and the flux gap are the same collection chain read at two thresholds.**

## 1. The energy gap on the E_μ axis

`Q = N·17.59 MeV / E_μ` with `N(ω_s, φ) = φλ_c / (λ₀ + ω_s·φλ_c)`. At **measured** sticking
(0.45%, SIN) — no polarisation, no J=1 mixture, no sticking work whatsoever:

| | crossover E_μ for Q = 1 | accelerator gain required |
|---|---|---|
| φ = 1.2 (within record) | 2.93 GeV | **1.70×** of 16.7× available |
| φ = 3.0 (extrapolated) | 3.45 GeV | **1.45×** |
| asymptotic ceiling N = 222 | 3.90 GeV | **1.28×** ← the prose figure |

At the 0.30 GeV kinematic floor, measured sticking gives **Q ≈ 13**. The prose states it
exactly: *"the energy gap is dominated by the 16.7× accelerator inefficiency, not by
α-sticking. The sticking levers matter only because E_μ sits at 5 GeV."*

**A reconciliation, and neither figure is flattened.** The prose crossover of 3.90 GeV (1.28×)
uses `N = 1/ω_s = 222`, the sticking ceiling — which is the asymptote as `φ → ∞` and omits
muon decay. `mucf.py` uses the decay-corrected `N`, giving 196.2 at φ = 3 and a crossover of
3.45 GeV (1.45×). The instrument's figure is the conservative one. Both are recorded.

Run: `python3 tools/mucf.py` · `python3 tools/mucf.py --band`

## 2. Q in §5.1 is heat, not work  `PROSE-ONLY`

§5.1 counts 17.59 MeV of fusion **heat** against GeV of electrical **work**. Only 50.1% is
convertible: the α's 3.5 MeV (19.9%) stays in the fuel; the neutron's 14.1 MeV (80.2%) escapes
to a blanket at 62% Carnot. **Work-breakeven is E_μ < 1.96 GeV, a 2.55× accelerator ask** —
still inside the 16.7× headroom, but twice the stated one, and it is the plant-relevant
threshold.

Run: `python3 tools/mucf.py --work`

## 3. The cryogenic branch is excluded on thermodynamics  `PROSE-ONLY`

At 20 K the fusion heat is worth no work and costs 10.4× to remove. **A μCF reactor cannot be
net-positive while cold.** Above ambient the recovered fraction is fixed by the blanket, not
the fuel. This contradicts §3.2's operating advice — *"density as high as the cryogenics
permit"* — because cryogenics is the lever that eats the output. The right lever is **pressure
at high temperature**, and the JINR scan (0.2–1.2 LHD, 20–800 K) is the only dataset spanning it.

A **temperature–density bracket** follows, with the same two-bound shape as the mass window
[119, 918] mₑ: bounded below by the formation resonance (pushes hot, λ_dtμ rises ~2 orders
toward 800 K) and above by the fluid ceasing to be dense (pushes cold). The paper gives both
ends in §3.2 as separate recommendations without naming them as opposed.

## 4. The two gaps are one chain  `PROSE-ONLY` — the load-bearing item

| | | |
|---|---|---|
| cost per muon **produced** (§4) | 5 GeV | `MEASURED` |
| cost per muon **delivered** (PSI 1.4 MW ÷ 10¹⁰ μ/s) | **874 TeV** | `PROSE-ONLY` |
| ratio | **1.75 × 10⁵** | the collection gap |
| flux gap from the other end (1.2 × 10¹⁵ ÷ 10¹⁰) | **1.2 × 10⁵** | the same number |

**The 5 GeV figure already assumes the collection chain A3–A6 is solved.** What is missing is:

- **not beam power** — PSI runs 1.4 MW;
- **not pion production** — 1 MW at 590 MeV gives ~10¹⁶ p/s and ~10¹⁵ π⁻/s, the requirement to
  within order one;
- **a collector.** No machine collects and stops a large fraction of what it produces, because
  none has ever been built wanting to. Every discard in a physics beamline — momentum spread
  dp/p ~ 1–3%, small emittance, mm beam spot, background rejection — is *deliberate*, and a
  reactor wants none of them. It wants any momentum that ranges out inside the fuel.

This supersedes §5.2's "a machine that does not exist" with something sharper and far better
posed: **the design objective is the opposite of every muon channel ever built.**

Run: `python3 tools/mucf.py --collector`

## 5. The correction this forces on the optimistic reading

A muon rate sufficient for a stated fusion **power** is not evidence of a self-sustaining
reaction. 1 W of fusion needs ~1.8 × 10⁹ delivered μ/s — inside the ~10¹⁰ /s planned for HIMB —
but costed at the 874 TeV a real beamline delivers today, that demonstration runs at
**Q ≈ 3 × 10⁻⁶**. There is no lab-scale shortcut in which Q > 1 falls out at low power.
`--flux` prints the rate and this warning together and will not print the rate alone.

## 6. Open items

1. **The collector is the whole remaining problem, and no file here holds its design or its
   per-stage budget.** The 16.7× is "distributed across pion yield, capture solid angle, decay
   acceptance, transport and stopping fraction", with capture named the largest single loss.
   *"None of it is forbidden"* is a physics statement, not an engineering one. A per-stage
   budget with a defensible ceiling on each stage is the document that decides this project.
2. **λ_c = 2.6 × 10⁸ s⁻¹ carries the widest error bar on the most load-bearing number.** It
   descends from transfer at (2.7 ± 0.9) × 10⁸ — ±33%. `--band` propagates it.
3. **φ ≥ 2 LHD is outside the scanned record** (PSI 0.01–1.5, JINR 0.2–1.2). The margin lives
   in density nobody has run — and §3 above says it must be reached by pressure, not cooling.
4. **The 0.31% J=1 sticking figure is unresolved by its source** (paper §7: initial or
   post-reactivation), and the composed 0.234% rests on it.

## 7. A finding about the paper, recorded not repaired

Table 5.1's `ω_s = 0.234%` row reproduces at `λ_c ≈ 2.69–2.74 × 10⁸`, not the 2.6 × 10⁸ the
paper pins in §3.3 — it is computed at the cap's *parent* (the unrounded transfer rate 2.7e8)
rather than at the saturation value stated beside it. At the pinned value the row reads
0.92 / 1.09 / 1.20 instead of 0.93 / 1.10 / 1.21 and still clears breakeven at φ ≥ 2. The
conclusion survives; the row is marginally optimistic against its own parameter.
`--selftest` block [1b] diagnoses this.

## What the instrument refuses

It offers **no verdict** on whether the goal is reachable, and it **will not choose** between
the paper's "two independent gaps" and the prose's "one chain" — both are the corpus's own, and
which stands is a ruling, not a measurement. It will not print a bare `Q`: every figure carries
the weakest status among its inputs (`MEASURED` / `PROJECTED` / `EXTRAPOLATED` / `PROSE-ONLY`,
and `REFUSED` below the kinematic floor). It will not collapse the transfer-rate band. It will
not report an accelerator gain as *achievable* — only as *required*.

## Provenance

- Model and Table 5.1 fixtures: `recovered/Muon_Catalysed_Fusion_v1.0.md` §§3.3, 3.4, 4, 5.1, 5.2, 7
- §§1–5 above: conversation `transitions`, messages 578–594 — `PROSE-ONLY`, banked here first
- Related banked rows: `PROSE-ONLY.tsv` PO-0897 (λ_c ceiling), PO-0898 (flux gap),
  PO-0896 (structural window), PO-0894 (ambient exclusion), PO-0411 (ash bracket),
  PO-0415 (Λ mass-blindness — the muonic atom occupies the same Λ cell as its electronic twin)
- Register 319 (main bundle) records the paper; docket **C-8** records that it is cited at
  References R.3 and **is not a member of either bundle**, leaving three of its claims
  unmeasurable by the book's own audits.
