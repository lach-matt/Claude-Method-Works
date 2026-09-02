# BATCH 10 — CERTIFICATE (IoI-01…03, Index of Indices) — PARTIAL: string PF build OPEN

## Result so far: 2 bound + 2 authored/seated + 1 bound-to-existing; 1 OPEN (string partition function build).
Base at B10 open: BUILD71 (32,749 lines, md5 fdff5f035c6bcb7b7420fb232452fc67).
Current: BUILD74 compendia — 32,771 lines, md5 eb52dd43f5ee7a4685676d211f94f7a4.
Main volume: BUILD56 (md5 5292fce89637c6b495363f76f99a4885) — untouched.

## IoI-01 (EM quotient as a named index) — BOUND (already seated)
Seated in IoI §V as "## The electromagnetic quotient": quotient not subset, E=0 vacuous (complete
rectangle), the crossing (11.6% vs 40.7% within an atom, reversing to 89.7% vs 77.9% across elements).
Nothing to author.

## IoI-02 (languages as coordinate systems) — BOUND (already seated)
Seated in IoI §V as "## The languages": a language is a coordinate system, translation is
re-coordinatisation, E is the cost; six agree on Λ at 976, ten pairs hold; statistics qualifies with
a caveat (E=0 on periodic table where ℛ gives 36 — marginals cannot see a hole). Nothing to author.

## IoI-03 — four indexes. Three closed, one open.
1. NUCLEON INDEX — AUTHORED + SEATED (IoI §V "## The nucleon index"). E=9, coords (Z,N).
   *** E=9 was an OPEN DEFECT at B10 open (R-1550 reconstruction gave E=2); RESOLVED this session. ***
   See NUCLEON-E9-RESOLVED.md. §6.2/§6.2.1 states the inclusion rule (particle-bound, low-Z, input
   PRINTED, recomputed at 4 cutoffs) and names the nine cells: He-5,He-7,Li-10,Be-8,Be-13,B-9,B-16,
   B-18,C-21 (pairing + clustering terms of the mass formula). VERIFIED by direct computation this
   session (nuclide_verify.py): Z≤6 reconstruction gives E=8 with those eight cells + zero spurious;
   C-21 appears at Z≤7 — reproduces the book's §6.2.1 table cell-for-cell. R-1550's E=2 measured a
   DIFFERENT object (full extrapolated AME2020 across all Z, not particle-bound low-Z). Finding was
   about the reconstruction, per the standing rule. `E.nuclide` number UNCHANGED (correct). The
   "COUNT NOT REPRODUCED" note is superseded — close via a NEW append-only Register entry citing
   R-1550 at the Register pass.  Entry authored then TIGHTENED per M (pictorial/editorial phrases cut).
2. KREUZER–SKARKE FRONTIER — AUTHORED + SEATED (IoI §V "## The Kreuzer–Skarke frontier").
   Coords (h¹¹,h²¹). E=540 on the exactly-specified χ=±6 slice (Candelas-de la Ossa-He-Szendroi 2008,
   208 cells). VERIFIED this session (ks_verify.py) cell-for-cell: |slice|=208, E=540 (498 join +
   498 meet failures of 21,528 pairs), χ∈{0,±2,±4}, 112 diagonal cells (13,13)..(131,131), h¹¹+h²¹
   range 26..262 — ALL match the book. Authored at the tightened standard (no pictorial prose).
3. APPENDIX D / THE LANGUAGE INDEX (index of the book's own mathematics) — BOUND (already seated).
   M RULING: this is reader-facing subject matter, NOT workshop self-audit — it is the concept tool
   that built the project's foundations (underlies the language chapter and all math-language subject
   matter; tells the reader how the mathematics communicates across the work). Seated in IoI §V table
   "## The book's own indexes" as the row: the mathematics | 77 | 0 | fibred, 24 fibres (main §D.5.10).
   Bind to that row; nothing to author.
4. STRING PARTITION FUNCTION — *** OPEN: MUST BE BUILT *** (next segment).
   M RULING (core to the IoI): any index NAMED must be BUILT — no exceptions; "named and not built"
   is a backlog to clear, not a resting category. The string PF is named in main §31.2.3 ("the
   partition function is Λ's expression with counts") but has NO built entry with coordinates + a
   measured E. It must be CONSTRUCTED: define its coordinates and cell set from §31.2.3, compute E on
   the rebuilt structure (nuclide_E.py-style 2-coord closure, or the tower instrument as fits), verify,
   author as an IoI §V entry, seat with a guard. This is a from-scratch index build — its own segment.
   FIRST STEP next session: read main §31.2 / §31.2.3 in full for what coordinates the partition
   function index carries and how "Λ's expression with counts" specifies a cell set.

## Guards this session (all measured-diff, all PURE unless noted)
- nucleon insert: BUILD71→BUILD72, +11/−0 at 18620.
- nucleon tighten: BUILD72→BUILD73, 1 line replaced at 18629 (same-length paragraph edit).
- K-S insert: BUILD73→BUILD74, +11/−0 at 18630.

## Still open after B10-partial
- STRING PARTITION FUNCTION build (the one remaining B10 deliverable).
- Token resolution [IoI-NN]/etc.→§-citations: LAST step (main carries no tokens yet).
- Nucleon: new Register entry citing R-1550 (append-only) at Register pass.
- Three deferred Register items from B6; Register 1.1 numbering; final tower reorder (MC-40/41 exempt).
- After B10: batches complete → prose rewrite → renumbering → bibliography audit → reader audits (A4/A5/A6) → final draft.
