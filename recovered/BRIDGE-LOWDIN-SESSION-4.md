# BRIDGE — THE LÖWDIN SESSION 4 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-3.md (read). Bank restore-point-2_13 (R 1700) unchanged; nothing
written to register/index/store. Isolate ISOLATE-LOWDIN-3 uploaded and verified 14/14. Context at
handoff ~85%. Read SOLVER-FINDING.md in full first (7 sections); it is the record of this session.
## 1 · M ruled
NOTHING FITTED ENTERS THE INDEX. Q.final is a diagnostic: it shows what is missing after TFD.
## 2 · Done (bridge-3 §4 Step 1, and 1e)
- brack.py reproduced (La/Ac/Lr endpoints). CODE hashes verified.
- TF/Latter solver: gate FAILS, rms 0.315 biased -0.257; d-collapse yes, f-collapse never.
- TFD/Latter solver (tfd.py, rad.py): rms 0.143, bias -0.010, no parameter. Ordering held out at
  closed-core ions 11/15 entrant, 13/15 ion ground: La 5d, Ac 6d, Pa 5f, Th IV 5f (ion) all out of
  one-electron TFD; Ce 4f one Z late; Sr marginal (0.006); Lr relativistic.
- Residual structure (§7): s,p unbiased; d over-bound in neutrals; f under-bound at collapse onset;
  sign flips with charge -> missing = core polarization + neutral exchange correction (Theodosiou).
- Two solver faults found before results were read (R 1671 shape), recorded in §1.
## 3 · Next chat's work, in order
Step 2 — regenerate the `computed` grade to Z=120 from TFD (parameter-free). 103,545 rows; ~0.3 s
per eigenvalue -> BATCH by Z in Zeno segments, write per-Z files, checkpoint; do NOT run in one call.
Every write to COORDINATES: regenerate all artefacts, both gates. Keep Q.final aside as diagnostic:
emit (Q.final - TFD) per cell as a separate column/file, never merged into delta.
Step 3 — entrants from the TFD index. NEEDS M's ruling on the core at open-shell steps: (a) closed
cores only (~30 steps), (b) charge 1 with previous configuration, (c) both and report disagreements.
Step 4 — n+l from the entrant table (D-O skeleton; Klechkovsky/Belokolos).
Optional gate: add core polarization -alpha/2r^4 with PUBLISHED alpha (attributable input) and rerun
gate2 — only if M rules alpha admissible.
## 4 · Owed to the writing chat (cumulative)
R 1701-1712 (Sessions 1-3, unchanged) · R 1713 (TF gate fails 0.315; two solver faults) · R 1714
(TFD 0.143/-0.010; 11/15, 13/15; four non-hits named; Latter's crossings computed in-record) ·
R 1715 (ruling: nothing fitted; residual as diagnostic; its l/charge structure) · FLAG 2 · allocation
ruling R 1701-1709 · CHAPTER-LOWDIN §8 rewrite. Still owed outside: Ra II nf; Ac III 6d-5f at source;
Latter's tables read.
## 5 · Faults / flags this session
- Project files `Löwdin_Challenge` and `Three-Body_Problem` are generic overviews (the Löwdin one is
  population analysis — wrong Löwdin). Not record. Recommend removal; M's call.
- Rb I, Y III still absent from index measured grade (FLAG 1 pattern); values used from R 1258.
## 6 · Files (outputs): SOLVER-FINDING.md tf.py tfd.py rad.py gate.py gate2.py gate.json gate2.json
BRIDGE-LOWDIN-SESSION-4.md. Bring these + BRIDGE-3 + isolate + CODE + COORDINATES to next chat.