# PROVENANCE — what in this tree is original, and what is not

*Written 2026-08-10, at the close of the bridge from The Method 1.6.1.*

**Why this file exists.** This tree was assembled from a restore point complete
through register 1370 plus sixty-three registers carried across as prose. Some of
what sits here is the original artefact; some was recovered verbatim from a
transcript; some was rebuilt from the registers that describe it; and some is
still absent. **A reader cannot tell these apart by looking at the files**, and
the difference matters to every claim that rests on them. Register 1373's fault
in its general form is an artefact whose status is not declared, so this file
declares it.

**The event that forced it.** The 1.6.1 container reverted to register 1370. Its
`COMPENDIUM-TAIL.md`, `QUEUE.md`, `xray_index.py`, `traj_index.py`, the captures,
the twelve scripts of the span and the staged `restore-point-1_6q.tar.gz` are all
gone. **What survived is exactly what had been written into a transcript as
prose.** That is the register, and it survived because the register is where the
reasoning was put rather than where the output was stored.

---

## RESTORED — original, from `restore-point-1_6.tar.gz`, unmodified

Everything not named below. 449 files through register 1370, gates passing on
arrival and unchanged since.

## RESTORED — original, extracted from the artefact it was embedded in

| file | how | verification |
|---|---|---|
| `COMPENDIUM-TAIL.md` | diffed `compendium.py`'s regeneration against the held copy | 6,659 bytes / 6,466 chars, matching register 1373's figure (which quotes BYTES) |
| `INDICES-TAIL.md` | same, after zeno's log was moved off stdout | 12,695 chars, matching register 1386 exactly |
| `PHYSICS-TAIL.md` | same, generator run in a scratch copy so the held file was never touched | 7,242 chars, matching register 1388 exactly |

*These three are original text. Only their location changed.*

## RECOVERED VERBATIM — from The Method 1.6.1's transcript

| file | what | note |
|---|---|---|
| `ladder_index.py` | the canonical merged index, R 1384 | reproduces R 1427's E = 0 at nine cells and R 1428's five shared cells independently |
| `INDICES-TAIL.md` § IX | Λ_xray in full, Λ_ladder rebuilt, R 1387 then R 1427–1429 | applied as two ordered edits with every anchor asserted |
| `COMPENDIUM-TAIL.md` § Λ_spectra | the eleven-cell table and rival = donor, R 1395–1398, corrected at R 1426 | **one deviation**: anchored before "Attributions" because R 1392's Janet-boundary heading was never recovered |

## REBUILT FROM THE REGISTERS — not original text

| file | from | status |
|---|---|---|
| `roundtrip.py` | R 1389, R 1433 | passes 5 of 5; the original is gone and there is nothing to diff against |
| `contingency.py` | R 1383 | both worked examples report FORCED, reproducing R 1375's 0 of 60 |
| `sixpair_screen.py` | R 1371, 1372, 1394 | identity exact on all six pairs; all three controls correctly empty |
| `bridge_transpose.py` | — | the tool that put the sixty-three registers into canonical form |
| `bridge_indices_tail.py` | — | the tool that applied the recovered section IX |
| `bridge_compendium_tail.py` | — | the tool that applied the recovered Λ_spectra section |

*These four scripts do what their registers say. They are NOT the originals, and
any figure they produce should be treated as recomputed rather than reproduced.*

## CAPTURED LIVE — fetched from source, not from any archive

`LADDER-H-Ar-I-III.tsv` · `XRAY-KL3.tsv` · `XRAY-KL2.tsv` ·
`XRAY-L1M3.tsv` · `XRAY-L1M2.tsv` · `XRAY-L1M.tsv` (derived, joined on key)

NIST ASD and NIST XrayTrans, retrieved 2026-08-10. Row counts verified against
NIST's own stated totals; flags, blends and blank fields preserved rather than
filled. `XRAY-KL3.tsv` reproduces register 1380's eighty-seven measured rows
exactly under the exclusion rule 98 − 1 absent − 7 interpolated − 3 faulty.

## ABSENT — known missing, not reconstructible, NOT to be silently written

| what | register | why it cannot be restored |
|---|---|---|
| `COMPENDIUM-TAIL.md` § the Janet boundary | 1392 | authored prose, held only on disk |
| `COMPENDIUM-TAIL.md` § the Nilsson narrowing | 1393 | as above |
| `COMPENDIUM-TAIL.md` § the C3 falsifier | 1430 | as above; delta change 6's second insertion |
| `QUEUE.md` as it stood at 1433 | — | this tree holds the pre-1371 copy |
| `xray_index.py` | 1378, 1379 | fully specified by its registers; buildable, not recoverable |
| `traj_index.py` | 1417–1420 | fully specified by its registers; buildable, not recoverable |
| eight further scripts of the span | — | `rival_pull.py`, `block_ascent.py`, `isotopic_null.py`, `hydrogenic_test.py`, `merged_index.py`, `merged_triples.py`, `corridor_identity.py`, and one unnamed |
| AME2020 mass data | — | cited in five places, held nowhere; **E.nuclide = 9 cannot be reproduced** |

**If any of the three compendium sections is written from its register, it must be
labelled REWRITTEN and not restored.** The register states what the passage
concluded; it does not contain the passage.

---

## THE STANDING GAP THIS EXPOSED

**The book trails the register by 208 entries.** `The Method 1.6.md` cites no
register above **1225** and mentions none of Λ_xray, Λ_traj, Nilsson, the six
pairs, the parent-term ladder or Moseley. 145 of those 208 predate the bridge, so
this is not a 1.6.1 gap — the bridge only extended it.

## THE LESSON, STATED ONCE

Everything held only in a generated file was lost. Everything written into a
transcript as prose survived. **An artefact whose content exists only in a file is
not durable**, and the compendia are recoverable from the register precisely
because the register is where the reasoning was put rather than where the output
was stored. That is register 1373 at the scale of the whole project rather than of
one build.
