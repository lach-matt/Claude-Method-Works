# PREDICTION-CHAIN-3D (s41, item 1) — WRITTEN BEFORE nlchain.py IS POINTED AT Z=21 AND BEFORE ANY ROW IS RUN (R 1449)

Successor to PREDICTION-CHAIN-LIGHT (s40, Z=2..20). Scope: **Z = 21..30, the 3d row.**
Field: SR-HF, hfc2 / HFC.run2(), CORR=False, C0. Chain rule unchanged:
config(Z) = config(Z-1) + one electron in the deepest-binding open channel; reference = cation of Z
carrying config(Z-1). Seed and candidate rule unchanged (CHOSEN, declared in SPEC-CHAIN §3/§4).
Δ carried as a SCORED COLUMN ONLY (s40 ruling 3). F39.2 not repaired (s41 ruling); f392_guard.py rides every step.

## 0 · Machinery gate, to pass BEFORE any Z=21..30 result is read (PC-0 pattern, can-fail)
**PC3D-0.** Re-running Z=20 from the banked cfg(19) reproduces the banked ordering to 5 dp:
4s -0.18891 · 4p -0.12833 · 3d -0.09743 · 5s -0.07272. If it does not, no row below is read.

## 1 · The anchor, stated so the risk is visible
g(Z) := D(4p) − D(3d). Positive = 3d ahead. Banked: **g(19) = −0.03556, g(20) = −0.03090.**
Trailing trend +0.00466 per proton. The record puts the Z=21 electron in 3d, so g(21) must be > 0 —
a swing of +0.031 in ONE proton against a drift of +0.0047. **This requires a collapse, not a drift.**
Both Z=19 and Z=20 are clause-2 violations on the 3d/4p pair (tie at n+ℓ=5, lower n says 3d, 4p wins).

## 2 · The n+ℓ-bearing predictions — the sharp ones
**PC3D-1.** Entrant is **3d at Z=21**. RISKY: it requires the collapse above.
**PC3D-2.** The collapse is clean, not a photo-finish: **g(21) ≥ +0.02 Ha.**
**PC3D-3.** Entrant is **3d at all ten steps Z=21..30. 10/10.** No step admits 4p, 4s or 5s.
**PC3D-4.** **Clause 2 is RESTORED and stays restored: g(Z) > 0 for every Z=21..30, monotonically increasing.**
  The s39/s40 clause-2 violations at K (and Ca) are therefore a THRESHOLD effect that switches off the
  moment 3d becomes the entrant — not a standing defect of the tie-break. This is the single most
  n+ℓ-relevant claim in this file.

### If PC3D-1 fails, the mechanism is named IN ADVANCE (so the failure is scored, not explained after)
Entrant 4p at Z=21 ⇒ FIRST DIVERGENCE = Z=21. Cause, in rank order, to be tested not asserted:
(a) the frozen avg-of-config reference under-binds 3d (PV-3 UNBOUNDED, already load-bearing from s40 §2b(11));
(b) absence of correlation, which differentially stabilises the compact 3d;
(c) the avg-of-config average over 3d^1 terms, where Hund-I splitting is largest.
A failure here is NOT a failure of n+ℓ; it is a failure of the field to reach the crossover, and it
localises the missing mechanism to one pair at one Z.

## 3 · The structural prediction — the add-only chain CANNOT reach Cr and Cu
The chain only ADDS. Cr (3d⁵4s¹) and Cu (3d¹⁰4s¹) require VACATING 4s. Therefore, stated in advance:
**PC3D-5.** Chain configuration diverges from the record at **exactly Z=24 and Z=29, and nowhere else in the row.**
  Predicted chain configs: **Cr → 3d⁴4s²** (record 3d⁵4s¹); **Cu → 3d⁹4s²** (record 3d¹⁰4s¹).
**PC3D-6.** The divergence **SELF-HEALS in one step**: cfg(25) = 3d⁵4s² = record Mn; cfg(30) = 3d¹⁰4s² = record Zn.
**PC3D-7.** **THE TRAP, REGISTERED BEFORE IT IS SPRUNG.** nlchain scores `ok` on the ENTRANT CHANNEL via
  `rectag`, which counts only subshells whose occupancy INCREASES. At Cr, 3d goes 3→5 and 4s goes 2→1,
  so `recent` = [3d] alone and rectag = '3d'. The chain will therefore **score ok=True at Cr and Cu while its
  CONFIGURATION is wrong.** Predicted score: **entrant 10/10, configuration 8/10.** A 10/10 entrant score in
  this row MUST NOT be reported as "the chain reproduces the 3d row". A configuration column is REQUIRED.
**PC3D-8.** Cr and Cu are exactly where MADELUNG also fails. The chain and the rule fail at the same two
  elements, and both fail for the same reason: neither is a filling-ORDER statement. The anomalies are
  intra-configuration rearrangements (exchange / half- and full-shell stability), outside what any
  n+ℓ ordering claims. Predicted: **no ordering error at 24 or 29 — the entrant channel is right, the
  occupancy transfer is what is missing.**

## 4 · Carried columns (scored, not promoted)
**PC3D-9.** MARGIN LAW (s40 finding 3): m grows monotonically as a subshell fills, resets at each new ns
  opening. Predict **m increases monotonically across the 3d run Z=21..30, 9/9 adjacent pairs**, with the
  possible exception of Z=24 and Z=29 where the record's occupancy transfer has no chain counterpart.
  Stated exception, declared in advance: if the only two failures are 24 and 29, the law is HELD-WITH-CAUSE.
**PC3D-10.** PD-6 (s40): entrant == argmax|Δ| — the electron enters the most penetrating open channel.
  s40 expected this to break higher up. Predict **it HOLDS 10/10 across the 3d row**, and that the first
  break comes later, where the hydrogenic term begins to decide (5s/4d or 6s/4f).
**PC3D-11.** PD-4 centrifugal gate: |Δ| < 1e-3 for every channel with l ≥ l_max+2. Predict **HELD at every
  step**, with 4f/5g gated throughout Z=21..30.

## 5 · What is NOT predicted here
The absolute D values; the crossover Z for 4d/5s; anything at Z>30; the Ac 5f positive Δ (PV-3, still owed);
correlation; term/multiplet energies. No constant beyond c is introduced. No record value enters any file —
record configurations are RECALLED-NOT-ENTERED, comparison column only.

## 6 · Held
PC3D-1 and PC3D-4 are the load-bearing pair. If PC3D-4 holds, the clause-2 violation of s39/s40 is
localised to the pre-collapse threshold and the tie-break survives as a statement about the SEQUENCE.
If PC3D-4 fails, n+ℓ's tie-break is defective across the whole 3d row and that is the finding.
