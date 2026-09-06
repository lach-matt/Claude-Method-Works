# BRIDGE — THE LÖWDIN SESSION 12 (2026-08-16)
Successor to BRIDGE-LOWDIN-SESSION-11.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive: LOWDIN-HANDOFF-11 (sha 8099d49e) verify11.sh 204/204. Reproduction gate PASSED: derive_P_fix→P2_fix10→P3_fix10,
derive_P3.json BYTE-IDENTICAL to PACK-8 banked (10/10 class; Os .1502; Bk .1343; Cm .1403).
## 1 · M ruled this session
T0 YES — a derivable, no-constant collapse-curve correction to the TFD kernel is the closure run; consistency across
element/species/regime is enforced by the walk/step functions. T3b YES. T4 stands: nothing written until the derivable
Löwdin solution is true for the whole spectra index and meets the 1969 challenge — the absolute last step.
## 2 · Findings (FINDING-T0W-SESSION-12.md, PREDICTION-T0W-SESSION-12.md, RUN-T0W-SESSION-12.txt)
- Candidate run: TFD → TFDλW gradient term, λ=1/9 (Kirzhnits 1957) and λ=1 (Weizsäcker 1935); no fitted λ.
- Solver faults registered before reading: BVP-in-P (tfdw.py) yields nodeful (excited) branches only; fixed-point
  (tfdw2.py) 2-cycle / spurious nodes. Ground branch obtained by BVP in S=ln P (tfdw3.py), ψ>0 by construction.
- RESULT: PW5 fails — no single derived λ moves all four residues toward measurement. λ=1/9 repairs Sr II (flips to 5s
  ground) but moves Ce IV/Pr V the wrong way; λ=1 repairs the f-onset (Ce .163→.111, Pr flips to 4f ground) but moves
  Sr/Ra the wrong way. Holds (Ca II, Th IV) hold under both. Uniform-λ candidate RETIRED. Reading (not decided): the
  fault is region-split — Kirzhnits valid outer/slowly-varying (d-onset), full Weizsäcker demanded at the cusp (f-onset).
- Ra II unchanged in either λ; consistent with bridge-10 (≥ half s-relativity).
## 3 · Next chat, in order
T0' — Ruling owed: with uniform λ retired, is a DERIVED region-split gradient term (e.g. the Kirzhnits second-order
      expansion kept as a full series near the cusp — no constant, owners named) the next closure candidate, or is
      the collapse-curve correction to be sought elsewhere (Scott/Englert–Schwinger strongly-bound-electron term)?
T3b — Bracket test NOT begun this session (T0 took the budget): NIST Handbook <element>table5/table6.htm, Ti–Cu I 3d,
      La–Lu I 4f; ~5% context each; score PB-11.1/2/3 at ≥6 points.
T4  — Writing chat, unchanged, LAST: R 1701–1760 (bridge-11) + R 1761 T0 ruling · R 1762 TFDλW candidate & retirement
      · R 1763 nodeful-branch solver fault · R 1764 region-split reading.  Chapter 34: NOT until closure.
## 4 · Figures (§H.6)
MEASURED: none new (residue margins from T3-RESIDUES-SESSION-11). RECALLED-NOT-ENTERED: none. CHOSEN: none.
## 5 · Files (PACK-12, minimal): tfdw.py tfdw2.py tfdw3.py PREDICTION-T0W-SESSION-12.md RUN-T0W-SESSION-12.txt
FINDING-T0W-SESSION-12.md BRIDGE-LOWDIN-SESSION-12.md MANIFEST-PACK-12.txt.
Runtime = HANDOFF-11 README recipe + copy pack12/*.py into rt. Bring next: LOWDIN-HANDOFF-11 + LOWDIN-PACK-12 + project files.