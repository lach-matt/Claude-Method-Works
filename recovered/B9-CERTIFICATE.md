# BATCH 9 — CERTIFICATE (PC-01…04, Physics Compendium)

## Result: 3 authored + seated, 1 closed-without-work. B9 COMPLETE.
Base at B9 open: BUILD70 (32,739 lines, md5 5493c7e8aa4631491ba6345008ee84c2).
Final: BUILD71 compendia — 32,749 lines, md5 fdff5f035c6bcb7b7420fb232452fc67.
Main volume: BUILD56 (md5 5292fce89637c6b495363f76f99a4885) — untouched.
Instrument: tower.py — Λ₉ rebuilt, all figures below verified on it.

## Structural determination (from HANDOFF file structure + BUILD68 layout)
The "Physics Compendium" reader volume is ASSEMBLED/generated at press time from the physics
families (`EM.`, `P.`) that live INSIDE the combined compendia file. There is no separately-edited
Physics Compendium file. PC entries are therefore authored into the combined file's EM. family,
in descriptive-title R-FORM (handles forbidden reader-facing), matching MC-36…41. The standalone
`..._The_Physics_Compendium-*.md` is a production artifact, not the working file.

## The three authored entries (each single-hunk PURE INSERTION +10/−0, M-approved, R-FORM):
1. PC-01 "The multipole is fixed by the orbital jump and the parity" (§12.11.8/§4.6, Computed)
   — EM. family, after `EM.spin`. VERIFIED this session on Λ₉: multipole map range M1 814 / E1 840
     on the base build (|Δℓ| ≤ 1); refusal |Δℓ| > 3 by construction; E2/E3 exercised at wider caps.
     CARRIED: nine-textbook-classification validation.  (BUILD68→BUILD69, md5 8cd48fee…)
2. PC-02 "Intercombination lines: the index admits what LS coupling forbids" (§12.11.8, Computed)
   — EM. family. VERIFIED this session on Λ₉: 576 E1 cells with ΔS≠0; spin rule ΔS=0 keeps 526 at E=0.
     Physics of LS spin-rule + spin-orbit breakdown carried from record.  (BUILD69→BUILD70, md5 5493c7e8…)
3. PC-03 "The four coupling schemes as physical recoupling chains" (§12.11.8, Computed)
   — EM. family. Four chain definitions (jK/LK/LS/jj) + physical regimes + ½-spin degeneracy
     |2J−2K|≤1. EXPANDED per M ruling with a SOURCED rotational-invariance clause: rotational
     invariance ⟹ J conserved, coupled states are J²,J_z eigenstates, energy independent of M, and
     Wigner-Eckart factorises matrix elements into an orientation-fixed geometric part and an
     orientation-independent reduced part. Sources fetched this session and verified citeable:
     Wigner-Eckart is "a statement of rotational symmetry" (Colorado phys5250); factorisation into
     geometry and physics (arXiv 0804.4528); J conserved / good quantum number by Noether
     (ScienceDirect S0039368121000078). Citations added: Eckart 1930, Wigner 1931, Sakurai.
     NB on process: the "gyroscopic rigidity / vector model" framing was CONSIDERED and REJECTED —
     the vector model is non-rigorous and contradicts the Pauli equation (arXiv math-ph/0505059);
     the rigorous, on-subject replacement is rotational invariance + Wigner-Eckart, which is what
     was seated. No heuristic entered the volume.  (BUILD70→BUILD71, md5 fdff5f03…)

## PC-04 — CLOSED WITHOUT WORK (workshop matter)
PC-04 was framed as the Theorem 14.1 prior-art provenance chain. Determination:
 (a) The ATTRIBUTIONS are already seated as reader-facing prior-art in the `A.` cluster —
     `A.fix` (Bergman double-projection; Baker–Pixley 1975), `A.dechter` (Dechter 1992),
     `A.clos`/`A.staircls`/`A.env` (Moore 1910, Ward 1942, Deville-Barette-Van Hentenryck 1999,
     van Beek & Dechter 1995, Freuder 1982, Montanari 1974). 83 occurrences of the chain in BUILD71.
     Nothing owed to author.
 (b) The only remaining content is the PROVENANCE-CORRECTION NARRATIVE — the book's prior
     Freuder-for-Dechter mis-citation, "four works absent from References," "not first, for the
     third time" (R-04). This material lives in the Phase-2 audit / intake sections
     ("## A. Collisions", "## B. Additions", "## F. Register entries this intake generates"),
     and is WORKING-REGISTER matter, forbidden from the reader volumes by the standing rule.
Therefore PC-04 has no reader-facing deliverable and is closed without work.

## Still open after B9 (unchanged)
- [PC-NN]/[MC-NN]→§-citation token resolution: LAST step (main volume carries no tokens yet).
- Final tower-block reorder: LAST step (MC-40/41 exempt).
- Three deferred Register items from B6; Register 1.1 numbering; R-04 stays working-register only.
- Next batch: B10 (IoI-01…03, Index of Indices).