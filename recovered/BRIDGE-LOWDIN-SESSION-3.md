# BRIDGE — THE LÖWDIN SESSION 3 (2026-08-15/16)

*Successor to `BRIDGE-LOWDIN-SESSION-2.md` (uploaded, read). Bank in force: restore-point-2_13
(R 1700). Nothing written to register, chapter, store or generated artefact. This chat's
project folder held only the register and compendia; the isolate, STEPS and CODE were NOT
available. Context at handoff ~85%.*

## 1 · What M ruled this session, in order
1. Provide not a global solution but the only solution that can answer the global question.
2. No novelty claimed: the solution is the COMBINATION of published works.
3. **The real target (final ruling):** an equation that populates the spectra index with the
   same values NIST captures give — for everything in the index, to Z = 120 (Janet) — and
   then, from the whole index, derive n+ℓ. Work backwards.

## 2 · Artefacts produced (all in outputs, none banked)
- `LOWDIN-SOLUTION-STATEMENT.md` — the two-level decomposition (global E=0 skeleton +
  local one-variable placement); why nothing without the split can answer.
- `windows.py` — corridors on a concave diagonal are partition cells; amplitude windows:
  Cs I 4f/5d/6p/7s cells (0,.411)/(.411,.887)/(.887,2.18)/(2.18,∞) [gate: reproduces bridge];
  Fr I M=8: 6d needs a<0.854, 7p 0.854<a<2.10.
- `iso.py` — RUNG 5 TEST: a=1, ν=n*, δ read at the ion of nuclear charge Z over the closed
  core (R 1304's charge dependence, NOT R 1457's neutral-core object). 9/9 on record data
  (K Ca Sc Rb Sr Y Cs Ba Fr) + La ✓ Ce ✓ Ac ✓ Th ✗ from published ground states → 12/13.
  Prediction (Th miss) stated before sourcing.
- `LOWDIN-ASSEMBLY.md` — every rung with its published source; boundary: Th (many-electron),
  Gd/Cm (open core), Lr (relativistic — Desclaux & Fricke 1980, Eliav 1995, verified).

## 3 · Answers given to M's two direct questions (stand as stated)
- Does it meet Löwdin's criteria as posed / as intended? **No** — target changed to the
  order; potentials are TF/focusing (guessed-potential objection, R 1450); reads measured δ;
  boundary at Th, Gd, Cm, Lr; scored 12/13 on closed-core steps, not 106.
- Does it populate the index? **No** — it consumes measured δ, adds no cell (R 1458 stands).

## 4 · THE PROGRAMME THAT MEETS M's TARGET (next chat's work)
**Step 1 — the equation of the index = a one-electron potential solver, not a closed form.**
Radial Schrödinger in a self-consistent screened potential (Latter 1955 TF/TFD with
unit-charge tail; Theodosiou–Inokuti–Manson 1986; Seaton threshold). Output δ(Z, charge, ℓ).
GATE: reproduce measured Na I, K I, Sc III, Y III, Cs I, Ba II, Fr I δ to the standard the
record already accepts (Theodosiou matched K I to 0.001, R 1552). If the gate fails, the
fitted `Q.final` (rms 0.14) is what the index has and "same values" is not met — say so.
**Step 2 — regenerate the `computed` grade to Z=120** with the solver (currently Q.final).
Every write to COORDINATES: regenerate all artefacts, both gates.
**Step 3 — entrants from the index:** at each Z, least n* among Pauli-admissible cells at
(Z, charge = Z − N_core). Score on all 106 steps, held out. Record the boundary.
**Step 4 — n+ℓ from the entrant table:** diagonal skeleton (D-O; Klechkovsky/Belokolos).
Needs: ISOLATE-LOWDIN-3 (measured rows, store_gen), STEPS-2_13.csv, CODE-LOWDIN-2_13.txt.
None was in this chat. scipy present; bash network OFF.

## 5 · Faults registered this session
- `ie.pl` fetch returned destination `spectra=H-DS+i` (neutrals) for an ion query — R 1526's
  cache rule; not retried. The served table confirmed ground.py neutrals incl. Lr 7p.
- Opening turn: built `cfg.py` from memory before the bank landed (R 1697 shape); discarded.

## 6 · Owed to the writing chat
R 1710 statement · R 1711 partition windows · R 1712 the assembly, 12/13, Th boundary,
ie.pl fault · FLAG 2: narrow R 1458, annotate R 1457 (its "ν is not n*" was against the
neutral core's δ; at the ion of charge Z, ν = n*) · allocation ruling on R 1701–1709 ·
CHAPTER-LOWDIN §8 rewrite. Still owed outside: Ra II nf (facet 4); Ac III 6d–5f interval
witnessed at source; Latter's crossing tables read, not cited from abstract.
