# STORE-152-PENDING — read this before anything else when chat 152 resumes

Chat 152 was paused mid-flight. **The store moved underneath it.** Nothing chat 152 was doing was
undone, and nothing it owes has been taken from it, but the figures it carries for the gate are
stale and its `--old` bundle no longer exists under that name. This file is the delta, MEASURED,
and the list of what chat 152 still owes.

Written by the repository session of 3 September 2026 (Cowork) — not a Method chat. No section was
read, no census row closed, no volume touched.

---

## 1. The store moved: BUILD180 → BUILD181

| | old | new |
|---|---|---|
| compendia bundle | `The_Method_1_6_BUILD180_compendia_papers_audits.md` | `The_Method_1_6_BUILD181_compendia_papers_audits.md` |
| bytes | 5,757,241 | **5,989,282** |
| md5 | `ea5becc40e13debe4faaf6c7e0cde960` | **`1b783954aec8af8f1ff53a9184b35487`** |
| lines | 65,420 | **70,653** |
| members | 341 | **347** |
| main bundle | `BUILD90` · `49065309b0c4fe8e055f693aed295cca` · 1,983,081 B · 18,470 lines · 2 members | **unchanged** |
| members in all | 343 | **349** |
| WORKING-REGISTER.md ends | W-189 | **W-190** |

`method/verify.py` is repointed at BUILD181 and reports **VERIFY OK**. BUILD180 is retired from
`method/` and is recoverable from git history.

**Expect at the §0 gate (MEASURED, 3 September 2026):**

```
members checked: 349  mismatched: 0
BUILD90_main           2 members spliced -> md5 49065309b0c4fe8e055f693aed295cca OK
BUILD181_compendia   347 members spliced -> md5 1b783954aec8af8f1ff53a9184b35487 OK
VERIFY OK

WORKING-REGISTER.md   915,403 B  ae416100  7,981 lines  ending W-190
DEFERRED.md           395,944 B  b636a88c  3,427 lines  ending the 3 Sept repository-session block
RULINGS-R2.md          17,684 B  d42790bb    171 lines  ending the chat-128 block   <-- UNCHANGED
DOCKET.md              52,004 B  db539aad    377 lines  ending the chat-150 delta   <-- UNCHANGED
MANIFEST.tsv           23,377 B  e8b5ff4d    349 lines
```

## 2. What did NOT change, and the proof

Only **three** old members changed in the close — `WORKING-REGISTER.md`, `DEFERRED.md` and
`MANIFEST.tsv` — and `close.py`'s guard refuses any other. The reverse guard recovered BUILD180's
`ea5becc4` exactly.

**Every reader-facing volume is byte-identical.** `RUL-152-PENDING.md`'s extents table was measured
on the BUILD180 members; it was **re-measured on the BUILD181 members and holds byte-exact**:

| volume | lines | bytes | on BUILD181 |
|---|---:|---:|---|
| The Register | 6,611 | 1,203,491 | OK |
| Mathematical Compendium | 3,802 | 309,403 | OK |
| The Physics Compendium | 878 | 61,366 | OK |
| The Index of Indices | 2,093 | 118,373 | OK |
| Spectra Compendium | 1,159 | 100,790 | OK |
| **total** | **14,543** | **1,793,423** | **OK** |

**So `RUL-152-PENDING.md` needs no re-measurement and is valid as written.**

Also untouched: the Register (1 to 1792), `RULINGS-R2.md`, `DOCKET.md`, the chat-67 hold, and
**DEF-143 item 11's order — 26b-02/-03, then 27a-02's seven entries, 28a-06's author-and-year
match, 28b-06's reading of Register 1721 — which is exactly where W-189 left it.**

## 3. What chat 152 still owes, unchanged

**`RUL-152-PENDING.md` is NOT seated.** It is chat 152's ruling and belongs to chat 152's close. It
sits in `method/`, 2,541 B, beginning `## Chat 152 (3 September 2026)` and ending `.\n`.

Two mechanical notes for seating it, both MEASURED:

1. `RULINGS-R2.md` ends `.\n` and `RUL-152-PENDING.md` begins `## Chat 152`, so **the append text
   needs a leading blank line** or the two blocks run together. Stage a copy with a leading `\n`.
2. `close.py` contains an f-string whose expression part includes a backslash and **does not parse
   under Python 3.11**. Run it as `./method/bin/python3 method/members/close.py …`.

The shape, when chat 152 closes:

```sh
./method/bin/python3 method/members/close.py \
  --old method/The_Method_1_6_BUILD181_compendia_papers_audits.md \
  --new method/The_Method_1_6_BUILD182_compendia_papers_audits.md \
  --w  W-191.md \
  --main method/The_Method_1_6_BUILD90_main_and_register.md \
  --append RULINGS-R2.md <staged RUL-152 copy with a leading blank line> \
  --append DEFERRED.md   <chat 152's DEF block> \
  --members <new instruments>
```

then re-extract members over `method/members/`, regenerate `method/MEMBER-INDEX.tsv`, repoint
`method/verify.py` at the new bundle and md5, and run `python3 method/verify.py` until VERIFY OK.

## 4. What this session added to chat 152's docket

`DEFERRED.md`'s last block — *Repository session, 3 September 2026* — carries twelve items. Three
bear on chat 152 directly:

- **PHI-03 — `phi_at` is built but NOT lifted into `r2lib.py`.** `r2lib.py` L391-392 records it
  owed: *"Its companion phi_at is NOT lifted: it depends on TERMS, which is still owed."* Both are
  built and seated in the new member `phihat.py`. **The lift into `r2lib.py` itself is not done**:
  `close.py` refuses any change to an old member except `WORKING-REGISTER.md`, `MANIFEST.tsv` and
  its `--append` targets, so it needs a guarded `build.py` substitution with a count-asserted diff
  and a reverse-md5 guard. `r2lib.py` L391-392 stands as written and is still accurate.
- **PHI-01/PHI-02 — φ̂'s form, ruled by M this session.** φ̂ is the **monotone envelope** of
  `max2J(ℓ,k)`, established by testing all five candidate forms against the record rather than by
  assertion; `pointwise`, `fold` and `global-max` are refuted. **R3 corrects MC L1686 and
  Transitions A15 L1819**, which print the un-enveloped formula, **and A15 L1823's Status line
  *monotone in k* with them.** Class: **C6-NUMBERS-NOT-IN-SOURCE**, per M — the figures have never
  been witnessed and so are not verified by spectroscopic measurement; they are predictions that
  were to have been theoretically proven by the mathematics, **publishable as theoretically proven
  but not yet witnessed**, and the label travels with the number.
- **An addendum W-190 does not carry.** The close was run twice. The first BUILD181 seated a
  `buildtrace.py` that hardcoded the live compendia bundle as BUILD180, and its own fixture failed
  the moment the close made the store BUILD181 — the fixture was right, and the flaw was seating a
  self-referential constant. `buildtrace.py` now **reads** the live bundles from
  `method/verify.py`, which is the authority and changes at every close. That first BUILD181 was
  discarded, the store rolled back to BUILD180 and verified there, and the close re-run from clean.
  **W-190 records the close but not this lesson; it is owed a line at the next close.**

## 5. Six instruments are now bundle members

`cypher.py`, `arith.py`, `pointers.py`, `buildtrace.py`, `populate.py`, `phihat.py` — chat 68's
standing half, instruments travel as bundle members. Each finds the store by walking up for
`method/verify.py`, so the same file runs from `tools/` and from `method/members/`; **all six
report SELFTEST OK from both locations**. Each takes `--selftest` whose fixtures are the corpus's
own recorded numbers, and each is stdlib-only. Docs: `docs/CYPHER.md`, `docs/ARITH.md`,
`docs/POINTERS.md`, `docs/BUILDTRACE.md`, `docs/POPULATE.md`, `docs/PHIHAT.md`.

**Read a tool's doc before reading its output.** Each refuses to report certain things and the
refusals are the point: a `NOT-BOUND` in `arith.py`, an `AMBIGUOUS` in `pointers.py`, an `ABSENT`
in `buildtrace.py` and a `NOT-RUN` in `cypher.py` are **not findings** and may not be quoted as
such. Findings are recorded, never repaired — the chat-67 hold governs these reports exactly as it
governs a section read.

W-190 and the DEFERRED block carry seven findings from this session, all recorded and none
repaired, including the ARITHMETIC class's first landing (MC L2930 states `146 of 163 = 92%`; it is
89.57%) and three defects in COORDINATES-2.13's provenance.
