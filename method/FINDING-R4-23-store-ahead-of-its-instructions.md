# FINDING R4-23 — the store is ahead of the document that governs it. The live bundles are **BUILD110 main and BUILD232 compendia**, 667 members; `method/CLAUDE.md` §3 states BUILD94 and BUILD194, 427 members, and two md5s that are not the ones on disk. **The tree is right and the sentences are old** — but R3's stated preconditions are stated against the older pair, so no R3 class is started on them. NOT REPAIRED.

Measured 6 September 2026, at the close of ruling 8, before beginning the R3 corrections rulings 2, 3, 9, 10, 11
and 12 authorise. `python3 method/verify.py` and `md5sum`.

## 1. Measured

| | on disk | `method/CLAUDE.md` §3 says |
|---|---|---|
| main bundle | `The_Method_1_6_BUILD110_main_and_register.md`, md5 **e1264def2a04df9ac010db3f0ea90953** | BUILD94, md5 6079e066b5e480db6c47f754660a9b6e |
| compendia bundle | `The_Method_1_6_BUILD232_compendia_papers_audits.md`, md5 **199df6336b30801dfe6567c39cd98485** | BUILD194, md5 d7f362b32f7caa0158ef4c20ea6b6620 |
| members | **667** (2 + 665), `MEMBER-INDEX.tsv` 668 lines | 427 |

Root `CLAUDE.md` states **343** members, and `tools/docfigures.py` already flags that row STALE (measured 667),
along with the Register's extent (states 1,660 entries, measured 1,702) — **15 of its 59 pinned figures have
drifted**, none of them from this pass.

**`python3 method/verify.py` reports VERIFY OK on the pair that is actually there**: every member matches its
recorded size and md5, and both bundles are recovered by splicing. So the store is coherent and the *documents
describing it* are behind — precisely the class of drift `docfigures.py` exists to catch, here at the level of
the project instructions themselves.

## 2. Why this stops the next item rather than being a footnote

`RULINGS-R4f` §5 puts the R3 corrections third, after ruling 8. `method/CLAUDE.md` §3 states a precondition on
them in terms of the older pair:

> *"Next work: **the 56 readings** (44 UNEXPLAINED, 12 UNRUNNABLE) **before any further R3 class lands**"* —
> measured by `shiftcheck.py` **on BUILD94/BUILD194**.

Sixteen main builds and thirty-eight compendia builds have landed since. **Whether those 56 readings are still
56, already discharged, or a different set entirely is not knowable from the document**, and the R3 mechanic is
built on exactly this kind of assertion: `close.py` reverse-guards to its predecessor's md5, and the predecessor
md5s recorded in the instructions are not the ones on disk. **Starting an R3 class against a stale precondition
is the one thing the guarded-build discipline exists to prevent.**

## 3. What is not claimed

That anything is wrong. The bundles verify, the members verify, and the builds between BUILD94 and BUILD110 (and
BUILD194 to BUILD232) were presumably made by the same guarded route. **What is claimed is only that the
governing document no longer describes the store**, and that the next item of work depends on figures in it.

## 4. What would settle it

Re-measuring §3 against the live pair — the gate's own steps, `gate.py census`, `gate.py run --all`, and
`shiftcheck.py` on BUILD110/BUILD232 — and rewriting §3's "Current state" from the result. That is a pass over
the project instructions and the volumes' own state, and under `CLAUDE.md`'s standing rule (*"State exactly which
files you would touch and what the change is, then wait for confirmation before any pass that spans more than one
file"*) it is put to M rather than begun.

Nothing is repaired. Every figure here is MEASURED by the command named beside it.
