# `method/` — The Method 1.6, read from the repository

This directory is the **store of record** for The Method 1.6. Before chat 151 the store was Google
Drive and every chat opened by fetching two bundles through the Drive connector. It is now this
tree, and nothing is fetched from Drive to open a chat.

## What is here

| Path | What it is |
| --- | --- |
| `The_Method_1_6_BUILD90_main_and_register.md` | Live main bundle — 1,983,081 B · `49065309b0c4fe8e055f693aed295cca` · 18,470 lines · 2 members |
| `The_Method_1_6_BUILD182_compendia_papers_audits.md` | Live compendia bundle — 5,864,276 B · `27e66a61061cec78283c4a88d53ba964` · 66,440 lines · 349 members |
| `members/` | All 351 members extracted from those two bundles, byte-exact. Instruments read these by name. |
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

Current state: `members checked: 351  mismatched: 0`, both bundles recovered, `VERIFY OK`.

Exactly one compendia bundle lives here at a time. `BUILD180` and `BUILD181` were removed once
`BUILD182` was asserted — both remain in git history, and both are re-derivable from Drive through
their `REBUILD-BUILDNNN.md`. Keeping a superseded bundle beside the live one is not merely untidy:
`gate.py manifest` refuses to guess which is live and stops until one remains.

## Running the gate

```sh
./method/bin/stage-gate                                   # once per container
export PATH="$(pwd)/method/bin:$PATH"                     # python3 -> 3.12
python3 method/verify.py                                  # 351 members, both bundles
cd /home/claude/members
rm -rf __pycache__ && python3 gate.py census              # byte-identical to the member
rm -rf __pycache__ && python3 gate.py run --core          # tower-2, kinds, minmax, r2-tools-constants, extent
rm -rf __pycache__ && python3 gate.py manifest            # 350 listed / 351 extracted
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

**Every banked instrument runs here.** An earlier note in this file repeated `HANDOFF-97` §0a's
claim that `r2-ch16n/s/t/u` and `r2-ch17c` cannot run in a container of this shape. That was never
measured, and it is wrong: §0a was struck at `W-190`, and all five reproduce their goldens
byte-exact. Three of them were only ever missing an input — the Prints & Proofs witness — and
`r2-ch20a`/`r2-ch26a` likewise need the coordinate file. `bin/stage-gate` now links both out of
`drive/`, so a fresh container runs the whole set with nothing done by hand.

## How BUILD182 got here

Chat 151-B closed BUILD181 and BUILD182 in Drive, not here, and it had no choice: from Cowork the
GitHub App token 404s this private repository and no `add_repo` is provisioned, so at that chat's
open **M suspended the chat-150 "repository is the store of record" ruling for as long as GitHub is
unreachable from Cowork** (`W-190`). `BUILDNNN-PARTS` came back with it — the Drive connector takes
content inline only, so a 5.9 MB bundle cannot be uploaded whole.

Neither bundle is in Drive as a file. Both were **rebuilt here, not transcribed**, from BUILD180
plus the parts, following `REBUILD-BUILD181.md` and `REBUILD-BUILD182.md`. Every part was fetched
through the Drive connector and checked against the md5 those documents publish — 15 of 15
byte-exact — and every assertion in them was then re-checked:

* `r2-26c.py` concatenates to 16,897 B · `6f1062f07b0108ee6d2dd395bd232ef0`; `r2-27a.py` to 15,219 B · `103078f4bf922ce6b9e9d5cad1b30224`
* `gate.py bank` regenerated both goldens byte-exact — `r2-26c.out` 13,613 B · `c1e19648b3d258166e9d6d977baee88f` · 156 lines, `r2-27a.out` 10,142 B · `38e112883a8ce6b581e471b3f866f2c1` · 125 lines
* `close.py` produced BUILD181 at 5,814,601 B · `2fbcd461cf0af81e3dcbbb0510e705c7` · 345 members, then BUILD182 at 5,864,276 B · `27e66a61061cec78283c4a88d53ba964` · 66,440 lines · 349 members
* each reverse guard recovered its predecessor — `ea5becc4…` then `2fbcd461…`

The goldens are the point: they were **regenerated by running the instruments here**, not copied.
A bundle that reproduces them is a derivation, not a plausible copy.

This is a bridge, not a fix. It works only because this container reaches both Drive and GitHub,
which the Cowork container does not. Until that access is settled, the chain advances in Drive and
someone has to carry it back — and `BUILD183` is already waiting there.

## Relationship to `drive/`

`drive/` is a read-only mirror of the Drive folders and remains the archive and the original-input
witness (Ruling 56). It is not on the read path. `drive/The Method Materials/CLAUDE.md` is the
pre-chat-151 gate, kept as the mirror records it; `method/CLAUDE.md` is the live one.
