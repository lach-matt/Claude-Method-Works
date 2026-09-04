# OPEN DEFECT — the nucleon index E = 9 vs E = 2 (B10 blocker)

## Status: OPEN. Not resolved. Blocks IoI-03's nucleon entry and flags possible error in seated subject matter (`E.nuclide`).

## The discrepancy (measured, from files)
- SEATED CLAIM (`E.nuclide`, BUILD71 line ~15303): the measured nuclide chart indexed by (Z, N)
  closes at **E = 9**, stable across four proton-number cutoffs; the nine cells are "the mass
  formula's pairing and clustering terms." grade COMPUTED, source M §6.2; Segre 1945.
- RECORDED RECONSTRUCTION (R 1550, note under the entry): AME2020 Table I captured
  (Chin. Phys. C 45, 030003; 3558 rows, Z=0–118, A=1–295); E recomputed with the same operator:
  **E = 2**, stable at 2 across cutoffs Z ≤ 20/50/82/92/118. Six cell-set variants tried
  (axes swapped, neutron excluded, measured-only, Z&N both positive); none gives 9;
  **measured-only gives 95**. The two E=2 defect cells: the empty cell (0,0) and Z=2 N=0
  (the DIPROTON, unbound — the textbook pairing failure). Three of four claims reproduce
  (stability, nameable-physics, pairing-term reading); the NUMBER does not. Cause UNDETERMINED.

## Rule governing the resolution (M, this session — corrects an earlier misread by the collaborator)
"When a reconstruction disagrees with the record, the finding is about the reconstruction" does
NOT mean "print E=9 and move on." An unresolved E=9-vs-E=2 gap is an OPEN DEFECT and must be
CLOSED before continuing: either E=9 is vindicated (the reconstruction used a wrong edition /
inclusion rule / arithmetic) OR the book's number is wrong and the subject matter must be corrected.

## The computation, now well-posed
Operator (A.R / A.E): ℛ(X) = join/meet closure of the (Z,N) cell set to the (≤,≤) staircase
corner; E(X) = |ℛ(X)| − |X|. Built and sanity-checked this session in nuclide_E.py
(2×2 box → E=0; L-shape missing corner → E=1, restores the corner). CORRECT.
The E-value is entirely determined by the INCLUSION RULE — which (Z,N) count as present:
  - full AME2020 incl. estimated/extrapolated (3558 rows) → E = 2 (R 1550)
  - measured-only (exclude extrapolated) → E = 95 (R 1550)
  - E = 9 corresponds to NEITHER; some intermediate principled rule.
RESOLUTION = find whether a PRINCIPLED inclusion rule yields exactly 9 AND those 9 cells are the
mass-formula pairing/clustering terms as claimed. If yes → E=9 stands, reconstruction used wrong
rule. If no principled rule gives 9 → book number is WRONG, correct `E.nuclide` to the true value.

## What it needs (could not be obtained this session)
- The AME2020 primary dataset as (Z, N) rows. Primary source located: IAEA AMDC,
  file `mass_1.mas20` (atomic masses) or `nubase_4.mas20`, at https://www-nds.iaea.org/amdc/ .
- BLOCKER: bash network is DISABLED (no wget/curl); the direct file URL is not fetchable through
  the doc tool (only URLs appearing in a search/fetch result can be fetched, and the .mas20 file
  link did not surface as fetchable). Hand-transcription of 3558 rows is impossible and is exactly
  the transcription the INTAKE protocol forbids (a number recalled is not a number sourced).
- NEXT SESSION (with network, or with the .mas20 file uploaded to Drive/uploads):
    1. Load mass_1.mas20; parse to (Z, N) integer pairs (and a measured-vs-estimated flag from the
       column that marks extrapolated values — the '#' / 'non-experimental' marker in AME format).
    2. Run nuclide_E.py's closure under each inclusion rule: full, measured-only, and any
       intermediate rule the book's §6.2 actually specifies (READ §6.2 in BUILD56 main for the
       exact inclusion rule the E=9 claim used — this is the likely origin of the 9).
    3. Identify the added cells; check whether they are the pairing/clustering terms.
    4. Close: either confirm 9 (and record which rule) or correct `E.nuclide` to the true E via a
       new Register entry that CITES the old one (append-only; no silent change; guard.py before bundle).

## CRITICAL UNREAD INPUT
§6.2 of BUILD56 main states the inclusion rule the E=9 claim used. It was NOT read this session.
That section is the first place to look next session — the 9 almost certainly comes from a
specific inclusion rule stated there, and comparing it to R 1550's rule will localise the cause.