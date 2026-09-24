# The Löwdin walk, recovered — `tools/lowdin_recover.py` and `lowdin/`

*The Löwdin project's own scalar-relativistic chain — the instrument register 1701 witnesses and
`THE-LOWDIN-SOLUTION-2.md` §II.2 states — read out of the project's hundred conversations, seated as
a generated tree, run here to Z = 120, and checked against every sealed step the sessions printed.
Every value RECOVERED, never READ; and one finding about the record, recorded and not repaired.*

## What was missing, and where it was

The Löwdin project (`drive/chats/`, conversations `LCP2` to `LCP101`, sessions 4 to 104) sealed its
work session by session into `LOWDIN-HANDOFF-<N>.tgz` archives, the last of them
`LOWDIN-HANDOFF-103.tgz` (1,870 files, sha256 `05ea7bd5…`). That archive was never banked:
`LW1-README.md` records objects 1 (the entrant operator), 2 (Λ_chain), 4–8 and 10 as PENDING BANK,
`LW1-ADDENDUM-REPLY.md` measured from the project's side that the one code store it held contained
no SCF solver, and the site carried a reconstruction, `tools/lowdin_walk.py`, with the caveat that
the walk beside the paper was not the paper's code. The archive is not in Drive (searched by title
and by content), not in the mirror, and not in the export: a file uploaded to a chat has no content
there.

But the archive's *contents* were made in the chats. Every runtime file was written by a tool call
(`create_file`, or a `cat > file <<'EOF'` heredoc), edited by tool calls (`str_replace`, the
sessions' own in-place Python patch scripts, `sed -i`), and printed back by `cat` and `sed -n a,bp`
into tool results the export carries verbatim. `recover.py` had already taken 1,046 files out of
those chats (`recovered/LEDGER.tsv`) — but only the *creation* bodies, so its `nlchain.py` is the
first draft, not the sealed instrument. This is the other half: the edits, and the prints that
witness them.

## The route

`tools/lowdin_recover.py` reads the export structurally and rebuilds each file of the chain's runtime
closure two ways, holding the two against each other:

- **Replay.** The file's whole edit history re-executed in chat order in a sandbox: `create_file`
  bodies (the tool wrote them with a trailing newline — 79 of the 86 sealed sha256 lines the sessions
  printed match only with it), `str_replace` edits applied where the old text is unique, heredocs,
  the sessions' patch scripts (`python3 - <<'EOF' … s=open('f').read(); s=s.replace(…)`) run as
  they were with their paths rebound, `sed -i`, and `sed 'expr' a > b` derivations.
- **Prints.** Every window the sessions printed of the file after its last edit, which the rebuilt
  text must reproduce line for line; and every full print, which must equal it.
- **Sealed digests.** Where a session printed a sealed manifest line (`<sha256>  pack52/cinf.py`),
  the recovered file's digest is checked against it.

The closure is what `import nlchain` reaches, measured by importing it: 28 files — the chain
(`nlchain.py`), its field (`hfc2.py`, `t7c_hfsr.py`, `t7b_hf.py`), the Koelling–Harmon kernel
(`t7c_kernel.py`), the three C shooters (`shoot.c`, `shoot_sr.c`, `shoot_x.c`), the guard
(`nlguard.py`), the scorer (`nlcfg.py`), the c → ∞ drivers (`cinf.py`, `cinf2.py`, `runsealed.py`)
and the helpers they import. `ground.py` is the store's own `LW1-ground.py` (register 1306), which
the sessions' prints of `rt/ground.py` confirm. `eps0a_table.json` is not a file of the tree: the
runtime regenerates it with the record's own generator (`eps0a_table.py` over `ring_zeta.py`, 20 s)
and the six rows the session printed are the check, to every printed decimal.

Three exceptions are stated where they are applied, each with its ground. `t7b_hf.py`: a
`create_file` the session itself found unapplied (its next call, `wc -l`, printed the 169-line file
with the earlier header) is skipped. `nlcfg.py`: the session's own patch that rewrote the scorer's
GATE block from computed scores ran over the chain and cannot be replayed without it, so the block
is taken from the print the next session made of it and the last edit is then applied.
`t7c_cuaudit.py`: never written by a tool call (derived by `sed` from a module derived by patches
from another); its text is a composite of two prints with the session-28 patch replayed, and two
later windows show a further edit no tool call records — it serves the field's correlation potential,
which the chain never calls (`CORR = False`), and it is the one file at `RECOVERED-PARTIAL`.

**The evidence, as `lowdin/LEDGER.tsv` and `lowdin/WITNESS.tsv` carry it.** 28 files, 117,358
bytes. 23 `RECOVERED`, 3 `RECOVERED-REPLAYED` (the replay carries the file past its last print), 1
`RECOVERED-PARTIAL`, 1 `STORE`. 157 printed windows from 62 conversations, 154 reproduced; the three
not reproduced are `t7c_cuaudit.py`'s. Full verbatim prints equal the recovered text for
`nlchain.py` in three sessions, `hfc2.py` in three, `t7c_kernel.py` in two, and eleven other files.
Two sealed digests match: `pack52/cinf.py` and `rt/t7b_hf.py` — the latter a file rebuilt through
nine patch scripts and two `str_replace` edits, hashing to the byte the session sealed. And
`nlchain.py` replayed through session 48, before its session-47 edits, hashes to the sealed
`pack40/nlchain.py` line the session printed: the replay reproduces sealed bytes at two points in the
file's history. `--selftest` pins all of this.

## Running it

```
python3 tools/lowdin_recover.py --runtime DIR       # compiles the shooters, generates the table
cd DIR/rt && SIC_NOCLAMP=1 SUBCELL=1 python3 nlchain.py 2 120          # Λ_chain, appends nlchain.jsonl
cd DIR && python3 pack53/runsealed.py pack52/cinf.py walk 2 108 OUT    # the table the paper compared against
cd DIR && python3 pack59/cinf2.py canfail && python3 pack59/cinf2.py walk 2 108 OUT   # restart rows at c → ∞
```

The sessions ran Python 3.12 and numpy 2.4.4 (`ring_zeta.py` was patched by the session to numpy's
`trapezoid` name), and the runs here match that numpy. A step costs 3 s at helium and a few minutes
in the actinides; the chain to Z = 120 is hours. Its first rows reproduce the rows the sessions
printed to every decimal: Z = 2 at D = −0.86172, margin 0.69553, the order 1s, 2s, 2p at −0.86172,
−0.16619, −0.12853, 26 iterations — the row two sessions printed whole — and every printed step to
Z = 18 exactly.

## What the runs return

Four runs, all in `lowdin/chain/` with `RUNS.tsv` (command, environment, row count, md5, status)
and `CHECK.tsv` (the chain's row-by-row verdict against the sealed steps), Python 3.11 and numpy
2.4.4, 4 cores, about five hours:

| table | driver | rows | what |
| --- | --- | ---: | --- |
| `LAMBDA-CHAIN.jsonl` | `nlchain.py 2 120` | 119 | Λ_chain re-derived: the chain on its own configuration at every step, c = 137.035999 |
| `LAMBDA-CINF-SEALED.jsonl` | `cinf.py` through `runsealed.py` | 107 | the table the paper compared against, as sealed: restart rows at c = 137.035999 with the driver's false `clight` label |
| `LAMBDA-CINF2.jsonl` | `cinf2.py walk 2 108` | 107 | restart rows at a genuine c → ∞ by the record's remedy (13 rows the record's, 94 run here) |
| `LAMBDA-CINF-CHAIN.jsonl` | `nlchain.py` after `cinf2.patch` | 119 | the chain at a genuine c → ∞ — a run the record never made |

**Λ_chain against the sealed steps.** The sessions printed a `-> Z=… entrant … D … margin …` step
for 112 of the 119 Z values, and twelve rows whole (of which five are chain-mode rows comparable in
full). `CHECK.tsv`: **107 exact** (entrant, depth and margin to every printed decimal), **5
exact+order** (Z = 2, 38, 57, 79, 80: every channel's depth and the refused set), **1**
`entrant+depth (margin differs: F61.1)` — Z = 19, above — and **6 unwitnessed** (Z = 59, 60, 81, 82,
85, 86, never printed as a step). **None differ.** The rows above Z = 108 reproduce the record's own
extension of the walk to 120 (6d at 109–112, 7p at 113–118, 8s at 119–120, margins from 0.058 at
Z = 113 to 0.264 at Z = 112 — the figures register 1712 prints). The record's own scorer, `nlcfg.py`,
run over the re-derived chain, **passes its gate on every clause**: 73 of 107 configurations, 96 of
107 steps, first divergences at Z = 24 and 25, and the same failure lists it sealed. The record's
collapse gate `gate85.py` (sealed at session 51 over the pre-guard rows, in `recovered/`) passes 12
of its 16 clauses on the guarded chain — the transit steps at exactly 57 and 90, the tie-break
obeyed at 94 rows and failed at 57, 89, 90, no ordering failure, 119 rows walked — and fails four
at the fifth decimal: the 7g channel takes two values differing by 10⁻⁵ where the sealed rows had
one, and the f plateaus read n* = 3.99 at Z = 56 and Z = 89 where the sealed rows read 4.00. The
scorer's gate was pinned at session 51 to the guarded chain; the collapse gate's clauses were pinned
to the pre-guard rows. Both are reported; neither is repaired.

**The paper's comparison reproduces.** Chain against the sealed comparison table, entrant by entrant
to Z = 108: they differ at exactly **[25, 30, 47, 48, 60, 61, 62, 71, 80, 103, 104]** — the paper
session's own list, Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf. The comparison table's first row is
the row the paper session printed from `rt/cinf.jsonl` (D = −0.86172, margin 0.69553, 26 iterations,
`"clight": 1000000.0`). At eight of the eleven the comparison table's entrant is the observed one.

**At a genuine c → ∞.** Restart rows: the entrant moves at **Nd, Pm, Sm, Th and Lr** only (at Nd, Pm,
Sm from 5d to the observed 4f; at Th from 6d to 5f; at Lr from 7p to 6d), and at all 13 exposed rows
the entrant is the c = 137.035999 entrant — the record's EX-1, reproduced 13 of 13. The chain with
the constant removed: the entrant moves at **Th, Rf and Ubn** only — thorium from 6d to 5f, the
inversion the paper states, at both modes; rutherfordium from 5f to 6d; and Z = 120 from 8s to 7d
at a margin of 0.013 Ha. Mn, Zn, Ag, Cd, Lu and Hg do not move at all when c is removed: their
entrant is the chain's memory, the same at both c. The chain's entrant is the observed gain at 96 of
107 steps to Z = 108 at both c; the restart rows at 101 (c = 137.035999) and 102 (c → ∞).

## The record's own faults, met on the way

**F61.1 — the sealed rows below Z = 57 predate the guard.** At Z = 19 the recovered chain gives
margin 0.05216 where the sealed step printed 0.05411: the entrant, its depth and every other channel
agree to the last decimal, and the runner-up 4p differs by 1.95 mHa. The record found this itself
(session 61's seed test, `FAULT-F61.1-PREGUARD-ROWS.md`, in `recovered/`): the rows to Z = 56 were
walked before `nlguard` was wired in at session 48, a channel that cycled to its iteration limit had
its last iterate taken as a value, and the guarded number is the converged one. The recovered
instrument is the guarded one, so it re-derives the record's *later* measurement, not the sealed
pre-guard row; `CHECK.tsv` classifies such rows as `entrant+depth (margin differs: F61.1)`, never
as agreement.

**F59.3 — the c → ∞ walk that was never at c → ∞.** The table the project sealed at session 53
as its non-relativistic walk (`pack53/cinf.jsonl`, 107 rows) was produced by `cinf.py`, which set c
by rebinding the kernel functions' default arguments; the field never consults those defaults, so
the walk ran at c = 137.035999 in restart mode (each step from the observed configuration). The
project registered the fault at session 59 (`FAULT-F59.3.md`), voided the table, wrote the remedy
`cinf2.py` (c rebound where the field reads it, with a can-fail probe that shows gold's 1s moving by
314 Ha), and ran it on the 13 exposed rows only. No full c → ∞ walk was ever run.

## The finding: register 1706's eleven rest on the voided table

`THE-LOWDIN-SOLUTION-2.md` §VIII and register 1706 state that the identical walk at c → ∞ disagrees
with Λ_chain at eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — and that every one of
those eleven placements is an error against nature. The paper's own session (`LCP101`, session 104)
computed that list from the runtime it had: its transcript shows it searching for c → ∞ material,
finding `rt/cinf.jsonl` (the session-53 table copied into the runtime by the open procedure) and
`pack59/cinf2.py` beside it, and then comparing the sealed chain's entrant with `rt/cinf.jsonl`'s at
every Z:

```
entrant differs at Z: [25, 30, 47, 48, 60, 61, 62, 71, 80, 103, 104]
```

That is the eleven, and the table it was computed from is the one F59.3 voided six sessions earlier.
So the eleven measure the chain's memory against a memoryless restart at one and the same c, not the
constant. At eight of the eleven (Mn, Zn, Ag, Cd, Lu, Hg, Lr, Rf) the second table's entrant is the
observed one — 4s, 4s, 5s, 5s, 5d, 6s, 7p, 6d — and it is the chain's that differs from nature; at
the other three (Nd, Pm, Sm) the chain's 4f is the observed and the second table's 5d is not. The
paper's sentence has the error on the wrong side at eight of eleven, because its second table was a
restart walk that reads the observed configuration at every step.

This is recorded, not repaired. The paper's statement stands as READ, register 1706 is not edited,
and no site string says the paper is wrong: the site carries the paper's eleven as READ, the two
tables the paper session compared as RECOVERED beside them (both re-derived here by the record's
instrument, so the eleven reproduce from them), and the comparison at a genuine c → ∞ — restart rows
by the record's own remedy, and the chain itself re-run with the constant removed — as RECOVERED,
labelled as runs the record did not make. What the genuine comparison returns is in the runs
section above. The retraction audit's category for this is a withdrawn value asserted as current
(`RETRACTION-AUDIT.tsv`, `docs/R3-REPAIR-PLAN.md`); this one differs in that the withdrawing record
(F59.3) is the project's own and preceded the paper.

## What the site does with it

`tools/webindex.py`'s `record_walk_block` reads `lowdin/chain/` and carries the four tables, the
run table, the ledger's summary and the check into `data/index.js` as `relativistic.record`, with
every element's rows under every setting in its own file; the element plate gains *The walk,
recovered* above *The walk, reconstructed*, the relativistic-limit mode prints the recovered summary
before the reconstruction's, and the caveats say what changed: the construction is no longer "not
held", the reconstruction stays as the site's second measurement, and the eleven carry the finding
above as a caveat in the site's own words. The public build prints no session numbers, no register
numbers and no path into the store; the project's faults are named by their own labels (F59.3,
F61.1), which are not the books'. The reconstruction (`docs/LOWDIN-WALK.md`) is unchanged and is not
withdrawn: it is a second measurement, and where it disagrees with the recovered instrument that
disagreement is now measurable.

## What remains not held

The archive itself: its 1,870 files include run receipts, caches, the seal machinery's own
manifests and the session documents (the documents are in `recovered/`; the receipts are not).
`gate86.py`, `chain90-out.json`, `ctrl137.jsonl` and `ci2.json` are named in sealed manifest lines
and were never printed. The 13 rows the record ran at a genuine c → ∞ (`pack60/exp13.jsonl`) were
printed only as `DONE Z=… ent=…` lines — entrant and time, not the row — and the runs here recompute
them. Λ_chain's sealed rows at Z ≤ 56 are the pre-guard rows and cannot be reproduced by the guarded
instrument; twelve of them were printed whole and are in the export, the rest only as steps.
