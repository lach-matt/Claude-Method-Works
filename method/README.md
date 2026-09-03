# `method/` — The Method 1.6, read from the repository

This directory is the **store of record** for The Method 1.6. Before chat 151 the store was Google
Drive and every chat opened by fetching two bundles through the Drive connector. It is now this
tree, and nothing is fetched from Drive to open a chat.

## What is here

| Path | What it is |
| --- | --- |
| `The_Method_1_6_BUILD92_main_and_register.md` | Live main bundle — 1,987,447 B · `ac49200f5a8a02511865260202e75cbb` · 18,485 lines · 2 members |
| `The_Method_1_6_BUILD191_compendia_papers_audits.md` | Live compendia bundle — 6,640,248 B · `072cc2b825eb52102a23ab657e680ccd` · 75,219 lines · 422 members |
| `members/` | All 424 members extracted from those two bundles, byte-exact. Instruments read these by name. |
| `MEMBER-INDEX.tsv` | Per member: bundle, extension, size, md5, and byte offset in its bundle |
| `verify.py` | The witness check — see below |
| `CLAUDE.md` | The project instruction and the §0 gate |
| `bin/python3` | Interpreter shim — the instruments need Python ≥ 3.12 |
| `bin/stage-gate` | Stages the tree at `/home/claude` so `gate.py census` can run |
| `rebuild/` | `REBUILD-BUILD181…191.md` — how each build is derived from its predecessor, with every md5 to assert |

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

Current state: `members checked: 424  mismatched: 0`, both bundles recovered, `VERIFY OK`.

Exactly one compendia bundle lives here at a time. `BUILD180` through `BUILD190` were each
removed once its successor was asserted — all remain in git history, and all are re-derivable from
Drive through their `REBUILD-BUILDNNN.md`. Keeping a superseded bundle beside the live one is not
merely untidy: `gate.py manifest` refuses to guess which is live and stops until one remains.

## Running the gate

```sh
./method/bin/stage-gate                                   # once per container
export PATH="$(pwd)/method/bin:$PATH"                     # python3 -> 3.12
python3 method/verify.py                                  # 424 members, both bundles
cd /home/claude/members
rm -rf __pycache__ && python3 gate.py census              # byte-identical to the member
rm -rf __pycache__ && python3 gate.py run --core          # tower-2, kinds, minmax, r2-tools-constants, extent
rm -rf __pycache__ && python3 gate.py manifest --main ../The_Method_1_6_BUILD92_main_and_register.md   # 423 / 424
rm -rf __pycache__ && python3 gate.py run --all           # all 86 goldens, one line each (~13 min)
```

All of the above was run in this container and passed: **86 of 86 goldens reproduce byte-exact.**

One caveat, measured and not worked around: `r2-ch23b` takes **300 s** here against `gate.py`'s own
270 s per-instrument ceiling, so `run --all` reports it `TIMEOUT`. Run alone it reproduces its golden
byte-exact. That is an environment note about this container, not a fault in the instrument or the
bundle — and `run --all` reporting 85 OK plus that one timeout is the expected result here.

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

## How BUILD184 got here

Chat 151-B closed BUILD181 through BUILD184 in Drive, not here, and it had no choice: from Cowork the
GitHub App token 404s this private repository and no `add_repo` is provisioned, so at that chat's
open **M suspended the chat-150 "repository is the store of record" ruling for as long as GitHub is
unreachable from Cowork** (`W-190`). `BUILDNNN-PARTS` came back with it — the Drive connector takes
content inline only, so a 5.9 MB bundle cannot be uploaded whole.

All four were **rebuilt here, not transcribed**, from BUILD180 plus the parts, following
`REBUILD-BUILD181.md` through `REBUILD-BUILD184.md` in turn (kept at `rebuild/`). Every part was
fetched through the Drive connector and checked against the md5 those documents publish —
**37 of 37 byte-exact** — and every assertion in them was then re-checked:

* `r2-26c.py` 16,897 B · `6f1062f07b0108ee6d2dd395bd232ef0`; `r2-27a.py` 15,219 B · `103078f4bf922ce6b9e9d5cad1b30224`; `r2-28a2.py` 16,676 B · `c7eafbaf76e9ddc908a3cc8af1423a32`; `r2-28b2.py` 17,057 B · `ccb9fc499e8d20e953936f472dab34b2`
* `gate.py bank` regenerated all four goldens byte-exact — `r2-26c.out` 13,613 B · `c1e19648…` · 156 lines, `r2-27a.out` 10,142 B · `38e11288…` · 125 lines, `r2-28a2.out` 12,319 B · `ef7253ed…` · 184 lines, `r2-28b2.out` 14,026 B · `553c84c9…` · 165 lines
* `close.py` produced BUILD181 `2fbcd461…` · 345 members, BUILD182 `27e66a61…` · 349 members, BUILD183 `d215c184aee08b884d8748fb6d79c0cb` · 353 members, BUILD184 5,977,919 B · `d4350094449e3a4bf488315e21199bd4` · 67,533 lines · 357 members
* each reverse guard recovered its predecessor — `ea5becc4…`, `2fbcd461…`, `27e66a61…`, `d215c184…`

The goldens are the point: they were **regenerated by running the instruments here**, not copied.
A bundle that reproduces them is a derivation, not a plausible copy.

**A size check is not enough.** Fetching these parts produced two transcription faults, and one was
a single character inside a regex (`[A-YA-Th]` for `[A-ZA-Th]`) in a part whose byte count was
correct both times. Only the md5 caught it. Chat 151-B hit the same class from the other side —
two bad uploads in four attempts at ~8–10 KB of base64 — which is why it now keeps every part near
5 KB and splits even its own `REBUILD` document. Check md5s, never sizes.

This is a bridge, not a fix. It works only because this container reaches both Drive and GitHub,
which the Cowork container does not. Until that access is settled, the chain advances in Drive and
someone has to carry it back.

## BUILD185 to BUILD190, the collisions they resolved, and what the main bundle broke

BUILD185 seats the Register read end to end; BUILD186 seats chat 152's six cypher members; BUILD187
seats M's two rulings and `close_rebank.py`; BUILD188 re-banks 25 goldens; BUILD189 seats
`close_census.py`; BUILD190 regenerates the census. **BUILD92** is the first main build since chat
62. All are recorded in `rebuild/`.

### Three collisions in one day, all ruled by M

Three lines ran in parallel on 3 September — chat 151-B in Drive, chat 151-R here, chat 152 on
`claude/cypher-analysis-method-books-826x0x`:

| | claimed by | and by | M's ruling |
| --- | --- | --- | --- |
| **chat number** | chat 152's own entry, as *"chat 153"* | — | there is no chat 153 |
| **W-190, BUILD181** | chat 151-B, `2fbcd461…` · 345 members | chat 152, `bfa0d975…` · 347 members | the Drive chain keeps the numbers; chat 152's entry becomes **W-195** |
| **entries 1793/1794** | chat 152's Λ audit findings | `r3-wl`, the class approved at chat 128 | the Λ findings keep them; **r3-wl re-takes** |

A carried entry is carried **verbatim**; corrections are made in the framing above it, never by
editing another line's words.

### The hold, split

Chat 152's BUILD91 appended Register entries 1793–1796 **and** repaired the front-matter counts. M
ruled them apart: **the entries stand, the repair waits.** `close_main.py` was run without
`--recount`, so **BUILD92** carries the four entries with both count sites untouched. **reg1-04
widens** — the front matter was stale by one entry, and is now stale by five. That is the honest
price and it is recorded, not softened. Chat 152's BUILD91 is retired and the main line goes
BUILD90 → BUILD92, skipping 91 so that no two bundles ever share a name.

### What one main build broke, and why

**The store was built on the assumption that the main bundle never changes.** It held from chat 62
until BUILD92, and seating four Register entries is the first thing to test it:

* **28 of 86 goldens moved.** Twenty-five moved truthfully and were re-banked at BUILD188 by
  `close_rebank.py`, each regenerated by *running* its instrument. Three did not: `r2-26b` and
  `r3-wl` exit 1, and **`r2-regsweep` exits 0 while printing `INSTRUMENT FAULT - STOP`** — the
  dangerous shape, because a tool checking only the exit code would re-bank a self-declared fault.
  All three assert the Register's extent as an **invariant** rather than scoring it as a claim.
  **Extent is data.** Their successors — `r2-regsweep2`, `r2-26b2`, `r3-wl2` — are owed and are
  readings, not re-banks.
* **`DEFECT-CENSUS.tsv` went stale**, and being derived but not a golden it had no route at all.
  `close_census.py` is that route. Its central guard is **id stability**: census ids are cited by
  every `CENSUS-CLOSURES-*.tsv`, so it refuses unless every id survives, keeps its class, volume and
  line, and new ids form a contiguous run above the old maximum. Measured: **1,556 → 1,557 rows, no
  id lost, none moved, 1,553 byte-identical.** Every closure in the store still points at the row it
  was written against.
* **`gate.py manifest` needs `--main` named**, because its constant still says BUILD90. The constant
  is only a default — line 42 takes `--main` — so nothing is broken; the *documented invocation* was
  stale and is corrected above. Worth noting that line 37 already resolves the compendia bundle by
  glob: the same file contains both the right pattern and the wrong one, which is what an untested
  constant looks like.

Three build routes now exist that did not this morning, all because of that one assumption:
`close_main.py` (chat 152) for a Register entry, `close_rebank.py` for a golden, `close_census.py`
for a derived member. Each runs the producer rather than trusting a copy, each asserts its change
set, and each reverse-guards to its predecessor's md5.

**The second order, learned the hard way.** BUILD190 regenerated the census — which is itself an
*input* to instruments — and two goldens moved again on it, `r2-ch16t` and `r2-reg12`. `r2-reg12` had
already been re-banked at BUILD188. **A chain that touches a volume re-banks in two passes:** first the
goldens that read the volume, then, after any derived member is regenerated, the goldens that read the
derived member. One pass leaves the second set silently stale, and a stale golden is worse than a red
one because the gate reports it green.

**Known red, and named at every close until it is fixed:** `gate.py run --all` carries the three
instruments above. A known-red gate step is how a real failure gets missed.

**Drive stands at BUILD184; the repository at BUILD190 / BUILD92.** Chat 152 is paused. Under M's
hybrid ruling that split is legitimate, but the next reconciliation is owed before either surface
advances two more builds.


## Relationship to `drive/`

`drive/` is a read-only mirror of the Drive folders and remains the archive and the original-input
witness (Ruling 56). It is not on the read path. `drive/The Method Materials/CLAUDE.md` is the
pre-chat-151 gate, kept as the mirror records it; `method/CLAUDE.md` is the live one.
