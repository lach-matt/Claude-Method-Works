# DEF-153F — findings from the compendium pass (R3). RECORDED, NOT REPAIRED.

Staged for the next close. The chat-67 hold governs: a finding is recorded, never repaired.

## F-1  The compendium generator chain is stale, and regenerating is destructive

`mathreg.py`, `compendium.py`, `physics.py`, `params.py`, `COMPENDIUM-TAIL.md`, `PHYSICS-TAIL.md`
are all present in `drive/The Method Materials/restore-point-2_13.tar.gz` (708 files) — in the
repository the whole time, inside the Löwdin project's restore point.

They no longer reproduce the store. `python3 physics.py` from that restore point emits **43,519 B
against the seated 61,366 B, 392 differing lines**. The seated text carries downstream corrections
the generator never received — `§18 (and the preface)` where it emits `§24`; `the l-collapse
(register 693)` where it emits `P.lcollapse`. And `params.py` (2026-08-09) still holds the
**pre-register-1740 counts** as typed literals: Rydberg constant `9`, where the seated compendium
prints `5`.

So register 1503's fault runs in BOTH directions. It recorded the generator discarding hand-authored
text; this records the store's own repairs never reaching the generator. Regenerating today would
discard 392 lines of corrected work.

Consequence for the Physics Compendium law entry: it is added to the seated member by guarded build,
exactly as the Mathematical Compendium's theorem was, and the upstream debt is named rather than
paid — `params.py` and `PHYSICS-TAIL.md` need the same text or the next regeneration drops it.

Correction to this session's earlier report: the Physics Compendium is NOT generated end to end.
`PHYSICS-TAIL.md` exists and `physics.py` refuses to emit without it — "a generator that cannot
produce its whole output must not produce part of it". The claim that the PC had no tail was wrong.

## F-2  `qgraph.py` returns an empty graph on the seated Mathematical Compendium, and exits 0

The seated member `qgraph.py` "walks the Mathematical Compendium's 'depends on' lines; reproduces
register 1749". It splits on `### \`name\`` and reads `depends on ... ·`.

Measured against the seated MC: **1 chunk, 0 matching headers, 0 dependency nodes.** The compendium
now writes its objects as `### Title` with no backticked id, and carries 7 occurrences of "depends
on" against 299 `###` objects. qgraph.py therefore builds a 0-node graph and exits 0 — a silent
zero, not a failure. Any count taken from it is a count of nothing.

This matters directly: register 1740's rule for "N objects rest on it" is defined as seeds plus
transitive dependents **in the compendium's own dependency graph**, and the instrument that reads
that graph cannot read it.

## F-3  The reverse-md5 guard proves invertibility, not correctness

Exhibited during the BUILD200 build. A member corrupted in a region the edit never touches
(`The observability boundary` -> `The observability Boundary`) still reverses to BUILD199's md5,
because the reverse substitution undoes whatever the forward substitution did, whatever that was.

The guard does fail correctly on a stale or mis-targeted anchor (`e6c29fbcbf0f3dfec0d7da6fe3ac1c9e`
against `b480d217d5695c3f3898bc57cde00126`). So it is a check that the substitution is *structural*
and unique — not that the new content is right. Content is guarded by the post-condition probes,
and the build docstrings should stop implying otherwise.

## F-4  Register 1580's corridor census does not reproduce

Its headline does: maximum pairwise-disjoint corridors = **3**, forced by **B5, La57, Lr103** —
the three elements it names, with La57 = (0.7071068, 1.7071068) to the digit. That stands.

Three figures in it do not, measured by `tools/slopeaxis.py`:

| register 1580 | node-only | finished |
|---|---|---|
| 73 fully bounded / 7 below-only / 26 above-only | 66 / 3 / 37 | 78 / 3 / 25 |
| Lr103 = (1.9841, **2.4409**) | (1.9840594, **+∞**) | (1.9840594, **+∞**) |
| max disjoint 3 | 3 | **4** (Ce58, La57, Cm96, Lr103) |

3 + 37 = 40 is the seated instrument's own one-sided count for the node-only form. 1580 closed an
interval that is open, and did not say which form it measured — its "three" is node-only only.
