# READ-succ2-153R.md — R3 (chat 153-R) — the positional class re-anchored by generator: forty-four successors, each proved on the bytes its predecessor was banked against

**The class.** W-207 and DEF-153N named it: an instrument pins a unit "measured by heading scan in this chat" as a
literal — `LO, HI = 8575, 8699`, `MAIN[9507 - 1]`, `range(9171, 9180)`, a witness list of line numbers — and reads
the wrong site after any build that moves a line above it. Every instrument of the family is the same shape, so the
repair is one shape too, and it was made a tool: `tools/reanchor.py` replaces each such literal with the text of the
line it pointed at in the bundle the golden was banked against, resolved at run time by a helper that reads the main
member from the instrument's own directory; nothing else in the predecessor changes. `tools/proveanchor.py` then
proves the successor byte-exact on those bytes (G0c). Two things the tool cannot decide are stated in its docstring
and were decided by hand here: which numbers in the same range are not lines (Register entry numbers, cell counts,
caps, random seeds — a keep list per instrument, with an auto-keep for entry-number contexts after `ent[1717]` and
`rbody(1722)` slipped through the first round and failed live), and which bundle each golden was banked against.

**The banking states.** Thirty-nine goldens were banked against BUILD90 main + BUILD184 compendia; five — the
successors chat 153 seated after r3-wl2's +8 shift (`r2-ch16n2`, `r2-ch16p2`, `r2-ch16u2`, `r2-ch16v2`,
`r2-ch17e2`) — against BUILD94 main + BUILD198 compendia. Anchors taken from the wrong state prove on nothing and
fail live at the lines R3 later edited; the driver anchors and proves on each candidate pair in turn. Both pairs are
in git history; the trees are extracted by proveanchor's own extractor. Three instruments open Prints & Proofs at
`members/../`, which proveanchor's scratch tree did not carry; it links it now, as `stage-gate` does.

**Two proofs with a stated exception.** `r2-ch16b2` differs from `r2-ch16b.out` on the old bytes in exactly one
line: the instrument counts the `round()` call sites of its own source and prints their line numbers, and the
fifteen-line helper moves that from 73 to 88. `r2-ch34re2` is proved byte-exact after one change beyond
re-anchoring: its verdict line read a §34.6 sentence by first site and raised IndexError once BUILD96 removed the
sentence; `first()` prints *absent* instead and is identical on the old bytes.

**What the live goldens carry, by class.** On BUILD101 every successor runs clean, and against its predecessor's
golden its output differs by (i) line references and member statistics, (ii) counts the appended entries move —
Register sites of a name, WARNING lines, withdrawal tokens — and (iii) in seven cases the content R3 changed under
the instrument: `r2-ch16n3` and `r2-ch16p3` read §32.1's readout sentences qualified at BUILD100; `r2-ch16w2`,
`r2-ch16x2`, `r2-ch16z2` and `r2-ch34re2` read §34, rewritten at BUILD96; `r2-ch27a4` reads Appendix G's rows,
re-taken at BUILD100; `r2-ch26b2` prints §32.1.4's table, qualified at BUILD100; `r2-ch18a2` lists the Register
entries carrying a word, and 1812 carries it. Class (iii) is not drift: each is the volume as the record says it
now stands, and the golden banks it. No masked-word residual survives that is not in one of the three classes.

| successor | supersedes | proved on | anchors |
|---|---|---|---|
| `r2-21a2` | `r2-21a` | 90+184 | 15 |
| `r2-ch16a2` | `r2-ch16a` | 90+184 | 23 |
| `r2-ch16b2` | `r2-ch16b` | 90+184, except one line | 8 |
| `r2-ch16c2` | `r2-ch16c` | 90+184 | 25 |
| `r2-ch16e2` | `r2-ch16e` | 90+184 | 4 |
| `r2-ch16f2` | `r2-ch16f` | 90+184 | 25 |
| `r2-ch16h2` | `r2-ch16h` | 90+184 | 3 |
| `r2-ch16i2` | `r2-ch16i` | 90+184 | 30 |
| `r2-ch16k2` | `r2-ch16k` | 90+184 | 3 |
| `r2-ch16l2` | `r2-ch16l` | 90+184 | 15 |
| `r2-ch16m2` | `r2-ch16m` | 90+184 | 7 |
| `r2-ch16n3` | `r2-ch16n` | 94+198 | 24 |
| `r2-ch16o2` | `r2-ch16o` | 90+184 | 5 |
| `r2-ch16p3` | `r2-ch16p` | 94+198 | 16 |
| `r2-ch16q2` | `r2-ch16q` | 90+184 | 10 |
| `r2-ch16r2` | `r2-ch16r` | 90+184 | 29 |
| `r2-ch16s2` | `r2-ch16s` | 90+184 | 14 |
| `r2-ch16t2` | `r2-ch16t` | 90+184 | 36 |
| `r2-ch16u3` | `r2-ch16u` | 94+198 | 15 |
| `r2-ch16v3` | `r2-ch16v` | 94+198 | 11 |
| `r2-ch16w2` | `r2-ch16w` | 90+184 | 27 |
| `r2-ch16x2` | `r2-ch16x` | 90+184 | 11 |
| `r2-ch16z2` | `r2-ch16z` | 90+184 | 48 |
| `r2-ch17a2` | `r2-ch17a` | 90+184 | 10 |
| `r2-ch17b2` | `r2-ch17b` | 90+184 | 6 |
| `r2-ch17c2` | `r2-ch17c` | 90+184 | 15 |
| `r2-ch17d2` | `r2-ch17d` | 90+184 | 9 |
| `r2-ch17e3` | `r2-ch17e` | 94+198 | 5 |
| `r2-ch17f2` | `r2-ch17f` | 90+184 | 8 |
| `r2-ch18a2` | `r2-ch18a` | 90+184 | 6 |
| `r2-ch19a2` | `r2-ch19a` | 90+184 | 7 |
| `r2-ch19b2` | `r2-ch19b` | 90+184 | 9 |
| `r2-ch20a2` | `r2-ch20a` | 90+184 | 18 |
| `r2-ch21b2` | `r2-ch21b` | 90+184 | 37 |
| `r2-ch22b2` | `r2-ch22b` | 90+184 | 6 |
| `r2-ch24b2` | `r2-ch24b` | 90+184 | 30 |
| `r2-ch25a2` | `r2-ch25a` | 90+184 | 3 |
| `r2-ch25b2` | `r2-ch25b` | 90+184 | 8 |
| `r2-ch26b2` | `r2-ch26b` | 90+184 | 5 |
| `r2-ch27a4` | `r2-ch27a` | 90+184 | 4 |
| `r2-ch27b2` | `r2-ch27b` | 90+184 | 3 |
| `r2-ch28a4` | `r2-ch28a` | 90+184 | 2 |
| `r2-ch28b2` | `r2-ch28b` | 90+184 | 3 |
| `r2-ch34re2` | `r2-ch34re` | 90+184 | 3 |

**The predecessors** stay seated, never edited, and red on the live gate for the reason this record states; their
goldens remain the readings at the state they read. **Still held, and why:** `r2-26c2` (two listing lines not
explained by an appended entry — read next), `r2-ch18b` (reads the census by line, and the census is stale under
its guard, W-210), `r2-reg1a` and `r2-reg7a` (the front-matter count, Ruling A), `kinds`, `r2-regsweep`, `r2-26b`,
`r3-wl` (the extent as an invariant, DEF-151r3 item 5).
