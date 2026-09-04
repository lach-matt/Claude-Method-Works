# DEF-153G — two edits the §34.6 rewrite requires, both awaiting M. STAGED, NOT TAKEN.

## G-1  Appendix D's row now qualifies a count the volume no longer prints

Main L10889 reads:

    the necessity of state, §34.6    theorem · physics    verified · sampled · none found
      (the claim stands at register 1332; its count is fixed from the case it judges and is
       not independently reproducible, register 1448)

BUILD96 removed "104 of 106" from §34.6. The parenthetical therefore qualifies a figure that is
no longer anywhere in the main volume, and `sampled` describes a sample the unit no longer takes.

M's ruling of this session splits the object in two: the ambiguity is a THEOREM (geometry, needing
no observation) and the corridor is a LAW (about the world, and it could have failed). Both fibre
values are admitted in Appendix D — `law · physics` already carries four rows, and
`LS.law the ordering law, five clauses — law · physics — proved · exhaustive · none found`
(L10832) is the model.

PROPOSED, on M's word:

    the necessity of state, §34.6                theorem · order    proved · exhaustive · none found
    the corridor, non-empty at 106 of 106        law · physics      verified · exhaustive · none found

The theorem reaches `proved` for the reason M set at §D.2 — proof is a matter of mathematics and
not of observation. The law cannot ever reach it, because it is a statement about which
configurations nature realises, which is what `verified · exhaustive` exists to mark.

OPEN: M asked to rule whether splitting one row into two is a structural edit under his lifting of
the append-only directive, or content. Not taken either way.

## G-2  The Physics Compendium law entry — drafted, and one field cannot be computed

`kind` is settled: M ruled **derived here**, and it is `_KIND[3]` in `physics.py`'s own list.

    ### the corridor law — `the entrant is a vertex of the lower hull of (√r, n)`, exceptionless on 106

    **derived here** · from this work · valid Z = 3–108 · ⟨N⟩ objects rest on it

    **What it is.** the subshell the differentiating electron enters is always one the ν form can
    select at all — a vertex of the lower convex hull of the points (√(p + q/2(2ℓ+1)), n) over the
    Pauli-admissible subshells; equivalently, its corridor of admissible slopes is non-empty. It
    holds at all 106 steps, Z = 3 to 108, in both the node-only and the finished form, and it could
    have failed at any of them.

    **Where it comes from.** this work — §34.5; registers 1445, 1460, 1463. Observed configurations
    from NIST ASD 5.12 (register 1306). The hull form and the identity of the corridor with the
    hull-edge slopes are asserted by `tools/slopeaxis.py --selftest` at 0 mismatches over 106 steps.

    > **Where it fails.** not known past Z = 108, where NIST lists no neutral ground configuration.
    > And non-emptiness refutes nothing — register 1460: "an empty feasible set refutes the form and
    > a non-empty one does not confirm it."

**⟨N⟩ CANNOT BE COMPUTED, AND IS NOT GUESSED.** Register 1740 defines it as the seeds plus every
object depending on one of them transitively **in the compendium's own dependency graph** — and
DEF-153F item 2 establishes that `qgraph.py`, the instrument that reads that graph, returns a
0-node graph on the seated Mathematical Compendium and exits 0.

What IS readable: the seeds. Four Mathematical Compendium objects state the corridor —
**The corridor — a system of linear inequalities**, **The falsification of a selection rule**,
**The necessity of state**, and **The collapse condition**. (Two further sections name it,
*The works this compendium leans on most* and *What this work introduces, in one list*, but those
are index sections rather than objects and are excluded.)

So ⟨N⟩ ≥ 4, and the transitive part is unavailable until `qgraph.py` has a successor that parses
the compendium's current `### Title` form. Register 1400's precedent governs: quoting against a
basis the artefact forbids is a fault, and inventing one is worse. The number waits.

## Both edits go in by guarded build on the seated members

Not by regeneration. DEF-153F item 1: the restore-point generator emits 43,519 B against the
seated 61,366 B across 392 differing lines, and `params.py` still carries the pre-register-1740
counts. Regenerating would discard downstream repairs. The upstream debt — `params.py`,
`mathreg.py`, `PHYSICS-TAIL.md`, `COMPENDIUM-TAIL.md` — is named at each build and not paid here.
