# `method/` — The Method 1.6, read from the repository

This directory is the **store of record** for The Method 1.6. Before chat 151 the store was Google
Drive and every chat opened by fetching two bundles through the Drive connector. It is now this
tree, and nothing is fetched from Drive to open a chat.

## What is here

| Path | What it is |
| --- | --- |
| `The_Method_1_6_BUILD94_main_and_register.md` | Live main bundle — 1,999,899 B · `15f8bc07d0592968f849b884e75f25f6` · 18,514 lines · 2 members. Register 1 to 1801. |
| `The_Method_1_6_BUILD90_main_and_register.md`, `…BUILD91…`, `…BUILD92…`, `…BUILD93…` | Previous main bundles, retained as snapshots. Not live; `verify.py` targets BUILD94. |
| `The_Method_1_6_BUILD186_compendia_papers_audits.md` | Live compendia bundle — 5,936,538 B · `40bea1b0d307331177444d5c70d4a91e` · 68,592 lines · 354 members |
| `members/` | All 356 members extracted from those two bundles, byte-exact. Instruments read these by name. |
| `MEMBER-INDEX.tsv` | Per member: bundle, extension, size, md5, and byte offset in its bundle |
| `verify.py` | The witness check — see below |
| `CLAUDE.md` | The project instruction and the §0 gate |
| `bin/python3` | Interpreter shim — the instruments need Python ≥ 3.12 |
| `bin/stage-gate` | Stages the tree at `/home/claude` so `gate.py census` can run |

The bundles sit beside `members/` rather than in a subdirectory because `gate.py` derives its
`HOME` as the parent of the members directory. `gate.py` is a seated bundle member and is never
edited in place, so the tree matches the tool.

## Verifying

```sh
python3 method/verify.py
```

Two independent checks, and a mismatch is a hard failure that is reported, never repaired:

1. Every member matches its recorded size and md5 in `MEMBER-INDEX.tsv`.
2. Every member is spliced back into its bundle at its recorded offset and the **bundle's own md5**
   is asserted. This is what makes the extracted tree a witness rather than a plausible copy: a tree
   that passes provably reproduces what the old Drive gate used to extract.

Current state: `members checked: 356  mismatched: 0`, both bundles recovered, `VERIFY OK`.

## Running the gate

```sh
./method/bin/stage-gate                                   # once per container
export PATH="$(pwd)/method/bin:$PATH"                     # python3 -> 3.12
python3 method/verify.py                                  # 343 members, both bundles
cd /home/claude/members
rm -rf __pycache__ && python3 gate.py census              # byte-identical to the member
rm -rf __pycache__ && python3 gate.py run --core          # tower-2, kinds, minmax, r2-tools-constants, extent
rm -rf __pycache__ && python3 gate.py manifest            # 342 listed / 343 extracted
```

All of the above was run in this container and passed.

### Why `stage-gate` exists

`census.py` is a seated member and hard-codes `/home/claude/members/` and
`/home/claude/DEFECT-CENSUS.tsv`. Seated members are append-only and never edited in place, so the
script symlinks the tree to where the tool expects it. Everything written during a chat lands back
in the repository through those links, which is what the close then commits.

### Environment

`numpy` is required (`r2lib` imports it) and `sympy` for one instrument. `gate.py` and several
instruments contain f-strings whose expression part includes a backslash, which does not parse
under Python 3.11 — hence `bin/python3`. `gate.py` runs instruments as `python3 NAME.py`, so the
shim must be on `PATH`, not merely used to launch `gate.py`.

```sh
python3.12 -m pip install --break-system-packages numpy sympy
```

A few instruments (`r2-ch16n/s/t/u`, `r2-ch17c`) are known not to run in a container of this shape
and are not part of the gate.

## How BUILD180 got here

BUILD180 is not in Drive as a single file: a 5.7 MB bundle cannot be created through the Drive
connector, which takes content inline only. It was **rebuilt, not transcribed**, from BUILD179 plus
the ten `BUILD180-PARTS` files, following `REBUILD-BUILD180.md`, and every assertion in that
document was checked:

* the four `r2-26b.py` parts concatenate to 27,320 B · `bbcf1ed1811aea2ead6bc1559b9c2a21`
* `gate.py bank r2-26b` regenerated the golden byte-exact — 21,029 B · `d55bf6f57d6f8fb3846c9f55698e00aa` · 190 lines
* `close.py` produced 5,757,241 B · `ea5becc40e13debe4faaf6c7e0cde960` · 65,420 lines · 341 members
* the reverse guard recovered BUILD179's `6251dc1351f165aef874b9cf4d8a45c1`

`BUILDNNN-PARTS` is now retired: git holds a 5.7 MB bundle directly, so the close writes the whole
bundle and pushes it.

## Relationship to `drive/`

`drive/` is a read-only mirror of the Drive folders and remains the archive and the original-input
witness (Ruling 56). It is not on the read path. `drive/The Method Materials/CLAUDE.md` is the
pre-chat-151 gate, kept as the mirror records it; `method/CLAUDE.md` is the live one.
