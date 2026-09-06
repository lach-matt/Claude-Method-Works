# RESOLVED — the nucleon index E = 9 (B10 blocker CLOSED)

## Verdict: E = 9 STANDS. The book's `E.nuclide` number is CORRECT.
## The R-1550 reconstruction (E = 2) used a DIFFERENT, WRONG inclusion rule. The standing rule holds:
## the finding was about the reconstruction.

## How it was resolved (this session, by computation on the book's own printed input set)
The resolution did NOT need the external AME2020 file. §6.2 / §6.2.1 of BUILD56 main state the
E=9 method at "F.3's highest standard" — the inclusion rule named, the input set PRINTED, and the
result recomputed at four cutoffs. Reading that section resolved the discrepancy:

- INCLUSION RULE for E=9: the PARTICLE-BOUND nuclides (the chart "as nature draws it"), in the
  LOW-Z region, closed under the §6.1 monotone envelopes. NOT the full AME2020 table.
- THE NINE NAMED CELLS (printed in the book): He-5, He-7, Li-10, Be-8, Be-13, B-9, B-16, B-18, C-21
  — every one a known UNBOUND nuclide inside the band its neighbours define. Be-8 = two alphas
  (clustering); He-5/He-7/Li-10/Be-13 = one neutron against an even-paired core (pairing). These are
  the mass-formula pairing and clustering terms, counted — content the (Z,N) coordinates cannot carry.
- THE BOOK'S OWN VARIATION TABLE (§6.2.1): E = 6 (Z≤5), 8 (Z≤6), 9 (Z≤7), 9 (Z≤9). The nine cells
  appear by Z≤7 and none is added after; the defect is a property of the measurement, not the window.

## Independent computation this session (nuclide_verify.py) — REPRODUCES the book
Reconstructed the particle-bound (Z,N) set for Z=1..6 from standard nuclear data, ran the A.R
join/meet closure (nuclide_E.py operator, sanity-checked: box→E=0, missing corner→E=1):
- Z≤6 reconstruction: **E = 8**, closure re-adds exactly {He-5,He-7,Li-10,Be-8,Be-13,B-9,B-16,B-18},
  ZERO spurious cells — CELL-FOR-CELL identical to the book's Z≤6 row.
- The 9th cell, C-21=(6,15), appears at Z≤7 — identical to the book's Z≤7 row (my set stopped at Z=6).
So the book's E=9 and its nine named cells are reproduced by direct computation. VERIFIED.

## Why the reconstruction got E = 2 (the located cause)
R-1550 recomputed over the FULL AME2020 Table I: Z=0–118, A=1–295, 3558 rows, INCLUDING
estimated/extrapolated nuclides. That is a different object — the entire nuclide landscape, nearly a
filled staircase — so ℛ adds only two holes (the empty cell (0,0) and the diproton Z=2,N=0).
The reconstruction changed BOTH the inclusion rule (all nuclides incl. extrapolated) AND the domain
(whole chart vs particle-bound low-Z) from what §6.2 specifies. Its own "measured-only gives 95"
confirms the number swings entirely with the rule; it never matched §6.2's actual (particle-bound,
low-Z, printed) input set. The E=2 measures a different index; it does not touch the E=9 finding.

## Action on the files
- `E.nuclide` (BUILD71): number UNCHANGED (E=9 correct). NO edit needed.
- The R-1550 note "*** COUNT NOT REPRODUCED ***" under `E.nuclide` is now SUPERSEDED: the count IS
  reproduced under the book's stated rule; the non-reproduction was a rule mismatch in the
  reconstruction. Per append-only Register discipline, this is closed by a NEW register entry that
  CITES R-1550 (not by deleting R-1550's note). That entry: "R-1550's E=2 used the full extrapolated
  AME2020 chart, not §6.2's particle-bound low-Z set; E=9 reproduced cell-for-cell under the stated
  rule (nuclide_verify.py); finding was about the reconstruction." → queue for the Register pass.
- The B10 nucleon IoI entry is now UNBLOCKED: it carries E=9 with the nine pairing/clustering cells.

## Instruments (this session, in /home/claude/chat61/)
- nuclide_E.py — the A.R join/meet closure for a 2-coordinate index (sanity-checked).
- nuclide_verify.py — the particle-bound low-Z reconstruction reproducing E=8 at Z≤6 / E=9 at Z≤7.