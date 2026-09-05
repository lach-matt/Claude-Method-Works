# `method/` — The Method 1.6, read from the repository

This directory is the **store of record** for The Method 1.6. Before chat 151 the store was Google
Drive and every chat opened by fetching two bundles through the Drive connector. It is now this
tree, and nothing is fetched from Drive to open a chat.

## What is here

| Path | What it is |
| --- | --- |
| `The_Method_1_6_BUILD110_main_and_register.md` | Live main bundle — 2,054,674 B · `e1264def2a04df9ac010db3f0ea90953` · 18,692 lines · 2 members |
| `The_Method_1_6_BUILD228_compendia_papers_audits.md` | Live compendia bundle — 14,574,369 B · `5c74cdac6cc662681bc99c1f4e53d134` · 113,562 lines · 642 members |
| `members/` | All 644 members extracted from those two bundles, byte-exact. Instruments read these by name. |
| `MEMBER-INDEX.tsv` | Per member: bundle, extension, size, md5, and byte offset in its bundle |
| `verify.py` | The witness check — see below |
| `CLAUDE.md` | The project instruction and the §0 gate |
| `bin/python3` | Interpreter shim — the instruments need Python ≥ 3.12 |
| `bin/stage-gate` | Stages the tree at `/home/claude` so `gate.py census` and the path-bound instruments can run |
| `rebuild/` | `REBUILD-BUILD181…191.md` — how those builds were derived from their predecessors, with every md5 to assert |
| `DEF-153*-PENDING.md`, `RUL-153-PENDING.md`, `DRAFT-*.md` | R3's notes to M: the deferred items, the rulings asked and given, and every Register entry drafted for review before it was seated |

The bundles sit beside `members/` rather than in a subdirectory because `gate.py` derives its
`HOME` as the parent of the members directory. `gate.py` is a seated bundle member and is never
edited in place, so the tree matches the tool.

**Where the store stands (5 September 2026, W-235).** The Register runs 1 to 1835; R3's Q5 is
complete — the five Register queue documents and the owed-expansions document parked in the mirror
for a "Register 1.1" are seated as entries 1821–1835 or resolved to entries already seated, every
figure re-derived by a standard-library instrument before its entry was written. The main bundle is
built by an instrument per pass (`r3-q5a.py` … `r3-q6.py`), each asserting its predecessor's md5,
appending the entries, re-taking the count classes and reverse-guarding to the old bundle; the
compendia bundle by `close.py` (seating), `close_rebank.py` (re-banking a golden by running it) and
`close_census.py` (the derived census). `WORKING-REGISTER.md` ends at W-235 and records every one of
those closes, and `DEF-153O-PENDING.md` is the running account of what R3 executed and what it left.

## Verifying

```sh
python3 method/verify.py
```

Two independent checks, and a mismatch is a hard failure that is reported, never repaired:

1. Every member matches its recorded size and md5 in `MEMBER-INDEX.tsv`.
2. Every member is spliced back into its bundle at its recorded offset and the **bundle's own md5**
   is asserted. This is what makes the extracted tree a witness rather than a plausible copy: a tree
   that passes provably reproduces what the old Drive gate used to extract.

Current state: `members checked: 644  mismatched: 0`, both bundles recovered, `VERIFY OK`.

Exactly one bundle of each kind lives here at a time; a superseded one is removed once its successor
is asserted and stays in git history. `tools/restage.py --bundle main=… --bundle compendia=…`
re-extracts the members and retargets `verify.py` after every close.

## Running the gate

```sh
sh method/bin/stage-gate                                  # once per container
export PATH="$(pwd)/method/bin:$PATH"                     # python3 -> 3.12
python3 method/verify.py                                  # every member, both bundles
cd method/members
rm -rf __pycache__ && python3 gate.py run --core          # tower-2, kinds, minmax, r2-tools-constants, extent
rm -rf __pycache__ && python3 gate.py manifest --main ../The_Method_1_6_BUILD110_main_and_register.md
cd ../.. && python3 tools/gate_live.py --list             # the live goldens, and why each other one is left out
python3 tools/gate_live.py                                # gate.py run over the live set (~10 min)
```

`gate.py run --all` walks every `NAME.out` alphabetically, and the store now carries the
superseded predecessors of every re-anchored or content-keyed successor beside them — they fail as
DEF-153B and DEF-153N record, several running to the timeout, and a full walk reports nothing the
held list does not. `tools/gate_live.py` is the walk over the goldens the store treats as live:
every `NAME.out` without a seated successor (trailing-digit rule, one recorded rename) and not on
its HELD table, the core five always included; `--list` prints the set and the reason for each
exclusion. Its verdict after each re-bank is recorded in `DEF-153O-PENDING.md`.

After a build that moves lines, three tools sort the moved goldens before any re-bank, and each
refuses to decide what it cannot see: `tools/shiftinv.py --all` (a verdict per golden — SHIFT, COUNT
or TEXT — from the words and the integers that changed), `tools/shiftcheck2.py` (a declared shift
applied only in a Register line-reference context, declared counts matched token by token, and every
bare shift-explained integer printed for the reader; `--selftest`), and `tools/reanchor.py` with
`tools/proveanchor.py` for the positional class — whose documented blind spot, a number in the line
range that is not a line, was found realised in nine instruments at W-235 and repaired by
content-keyed successors. `census.py` is a seated member that hard-codes `/home/claude/members/`
and `/home/claude/DEFECT-CENSUS.tsv`; seated members are never edited in place, so `stage-gate`
symlinks the tree to where the tool expects it, links the Prints & Proofs witness and the coordinate
file out of `drive/`, and everything written during a chat lands back in the repository.

### Environment

`numpy` is required (`r2lib` imports it) and `sympy` for one instrument; the R3 instruments
(`r3-*`) are standard-library by ruling. `gate.py` and several instruments contain f-strings whose
expression part includes a backslash, which does not parse under Python 3.11 — hence `bin/python3`.
`gate.py` runs instruments as `python3 NAME.py`, so the shim must be on `PATH`, not merely used to
launch `gate.py`.

```sh
python3.12 -m pip install --break-system-packages numpy sympy
```

**Every banked instrument runs here** (an earlier note repeating `HANDOFF-97` §0a's claim that five
could not was never measured and was struck at `W-190`); `r2-ch23b` alone exceeds `gate.py`'s 270 s
ceiling in this container and reproduces its golden run alone.

## History: how the store got here

The sections below are the record of the store's first weeks — BUILD184 carried back from Drive,
the collisions of 3 September, and what the first main build broke. They are kept as written; the
state they describe is superseded by the paragraph above.

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
