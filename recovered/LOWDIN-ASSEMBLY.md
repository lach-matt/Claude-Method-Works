# THE LÖWDIN CHALLENGE — THE SOLUTION AS AN ASSEMBLY OF PUBLISHED WORK

*Löwdin session 3, 2026-08-15/16. Companion to `LOWDIN-SOLUTION-STATEMENT.md`.
Claim of this document: NO NOVELTY. Every rung of the derived solution is a published
result; what has not been published is the combination, and the combination answers
Löwdin's global question with a stated boundary. Sources verified this session are
marked ✓; sources on record in the register are cited by R-number; one item is marked
"to verify". Nothing written to the register. Scripts: `windows.py`, `iso.py`.*

---

## 0 · The question, and what "answer" means here

Löwdin (Int. J. Quantum Chem. 3S, 331, 1969) asked for a derivation of the n+ℓ filling
rule from the Schrödinger equation. Scerri (Phil. Trans. R. Soc. A 378, 20190300, 2020)
records the consensus that no attempt has succeeded as intended (R 1450). This document
does not claim to have; it shows that the pieces of the only answer of the right shape
already exist in print, and assembles them.

## 1 · The assembly, rung by rung

| rung | statement | published source | status |
|---|---|---|---|
| A · which diagonal is live | the opening order of the diagonals M = n+ℓ is exact combinatorics; period lengths L_M = 2(⌊M/2⌋+1)² | Klechkovsky 1962; Belokolos, SIGMA 13, 038 (2017) (R 1450, R 1617) | closed |
| A′ · why the diagonal is the object | levels of equal n+ℓ are degenerate at E = 0 in the focusing potential −r⁻¹(r+R)⁻² resembling Thomas–Fermi; lifted below threshold | Demkov & Ostrovsky, Sov. Phys. JETP 35, 66 (1972) (R 1450, R 1621) | closed |
| A″ · threshold = quantum-defect limit | πμ(n→∞) = δ(E=0): the asymptotic defect is the threshold phase shift | Seaton, MNRAS 118, 504 (1958); Theodosiou et al. PRA 34, 943 (1986) (R 1552) | closed |
| B · one variable on a diagonal | on fixed M, n = (M+p+1)/2, so any ordering functional of (n,ℓ) is a function of one variable | arithmetic (DIAGONAL-FINDING §1) | proved |
| B′ · the shape is concave in ℓ | quantum defects fall with ℓ with diminishing increments: penetration saturates; f centrifugally excluded | Seaton 1958 (quantum-defect theory); Bates & Damgaard 1949; measured 8/8 in this work (DIAGONAL, FACET5) | measured |
| B″ · the entrant is a cell of a partition | with concave v the corridors (1/D_k, 1/D_{k−1}) partition the a-axis; interior entrants need concavity | lower-hull geometry (FEASIBILITY §1–3), five facets | proved |
| C · the amplitude is not free | a = 1 with δ read at nuclear charge Z along the closed-core isoelectronic sequence: the entrant is the lowest admissible orbital of the one-electron ion Z⁽ᶜ⁾ | one-electron ground states of Sc III, Y III, La III, Ce IV, Ac III, Th IV — NIST ASD / Moore; Olmschenk et al. (La III) ✓; Carvajal Gallego et al. (Ce IV) ✓; Safronova, Johnson & Safronova, PRA 76, 042504 (2007) (Fr sequence) ✓ | 12/13, miss at Th |
| C′ · why a moves with Z: orbital collapse | 3d/4f/5f contract suddenly at Z = 21, 57, 89 — the block openings | Goeppert-Mayer, Phys. Rev. 60, 184 (1941); Griffin, Andrew & Cowan, Phys. Rev. 177, 62 (1969); Q.collapse (R 1187–1190) | closed |
| D · Schrödinger | one-electron eigenvalues in the TF / TFD self-consistent potential across all Z reproduce the level order and its crossings | Latter, Phys. Rev. 99, 510 (1955) ✓; Bjerg & Solovej, arXiv 2406.19839 (2024) — periodicity of TF mean-field | published |
| E · the relativistic edge | Lr ground is 7s²7p ²P°₁/₂, not 6d, by 7p₁/₂ stabilisation | Desclaux & Fricke, J. Physique 41, 943 (1980) ✓; Eliav, Kaldor & Ishikawa, PRA 52, 291 (1995) ✓; NIST GSIE table ✓ | closed |
| F · the many-electron edge | Th enters 6d though Th IV is 5f-ground; Gd, Cm (4f⁷5d, 5f⁷6d) have no closed core to read | Safronova et al. 2007 (Th IV 5f) ✓; NIST GSIE (Th, Gd, Cm configurations) ✓ | boundary |

## 2 · The assembled statement

**The order of subshell openings is a two-level statement.** Between diagonals it is
exact and one-electron: the D-O threshold degeneracy names the diagonal, Klechkovsky /
Belokolos count its onset. Within a diagonal it is a one-variable ranking of the
members by the one-electron binding at nuclear charge Z over the closed core, whose
shape in ℓ is concave (Seaton) and whose position moves with Z by orbital collapse
(Goeppert-Mayer, Griffin–Andrew–Cowan). Latter (1955) is the Schrödinger computation of
exactly that: eigenvalues in a self-consistent screened potential as a function of Z,
with the 4s/3d-type crossings emerging. **That assembly reproduces the observed
entrant at every closed-core step tested — K, Ca, Sc, Rb, Sr, Y, Cs, Ba, La, Ce, Fr,
Ac (12) — including the two steps where Madelung's rule is FALSE (La 5d, Ac 6d).**

**Its boundary is also on record.** It fails at Th (6d² over 5f, decided by d–d exchange
in a many-electron configuration; the one-electron ion Th IV is 5f) and is silent at Gd,
Cm (open 4f⁷/5f⁷ cores, no one-electron sequence to read). At Lr the entrant is set by a
relativistic term outside the non-relativistic Schrödinger equation Löwdin named. So the
global question — why n+ℓ, and where does it fail — is answered as: n+ℓ is the E = 0
skeleton; the two inversions are one-electron orbital collapse at charge Z; the remaining
exceptions are many-electron (Th, Gd, Cm and the d-block s¹ cases) or relativistic (Lr).
No single global functional can carry them (Helly, R 1517–1521), and none is needed.

## 3 · The test as run this session (`iso.py` + §1 sources)

    step  core  criterion              predicted  observed  source
    K 19  Ar   K I δ                   4s         4s        Spectra Compendium
    Ca 20 Ar   Ca II δ                 4s         4s        Spectra Compendium
    Sc 21 Ar   Sc III δ (4s full)      3d         3d        Spectra Compendium
    Rb 37 Kr   Rb I δ                  5s         5s        R 1258
    Sr 38 Kr   Sr II δ                 5s         5s        R 1258
    Y 39  Kr   Y III δ (5s full)       4d         4d        R 1258
    Cs 55 Xe   Cs I δ                  6s         6s        DIAGONAL-FINDING
    Ba 56 Xe   Ba II δ                 6s         6s        DIAGONAL-FINDING
    La 57 Xe   La III ground (6s full) 5d         5d  ✓     Olmschenk et al. 2018 (5d lowest, 4f above); NIST
    Ce 58 Xe   Ce IV ground            4f         4f  ✓     Carvajal Gallego et al. 2020 ("4f ground configuration"); NIST
    Fr 87 Rn   Fr I δ                  7s         7s        FACET5-FINDING
    Ac 89 Rn   Ac III (7s full)        6d         6d  ✓     Safronova et al. 2007 (7s ground; 6d next — energy TO VERIFY at source)
    Th 90 Rn   Th IV ground            5f         6d  ✗     Safronova et al. 2007 ("first ion ... with 5f₅/₂ ground state")

Prediction (hits La, Ce, Ac; miss Th) was stated in the previous turn before any source
was read.

## 4 · What is still owed

- Ac III 6d–5f interval read at source (NIST Ac III levels or Safronova Table) — the
  Ac hit rests on 6d < 5f, which is standard but not yet witnessed in this session.
- Ra II nf series (facet 4 by measurement) — the one outside fetch, unchanged.
- Latter 1955's actual level-crossing table for the 4s/3d, 5s/4d, 6s/5d/4f, 7s/6d/5f
  sequences — cited from abstract only; the crossings themselves to be read.
- Register: R 1710–1712 (statement; partition windows; the assembly and its 12/13 with
  the Th boundary and the ie.pl cache fault, R 1526 shape). Allocation collision
  R 1701–1709 still needs M's ordering ruling before the writing chat opens.
- FLAG 2 stands: R 1458 to be narrowed (range-overlap only) and R 1457 annotated (its
  "ν is not n*" was against the neutral core's δ; at the ion of charge Z it is n*).
