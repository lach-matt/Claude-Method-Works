# `tools/idcensus.py` — which governance identifiers the chats name and the repo does not hold

`docs/PROSE-ONLY.md` records a **stage-A identifier census**: `W-` entries, rulings, dockets, faults,
registers and `MC` entries named in the chat prose, against what the repository holds. It is the
measurement behind the headline *"the governance spine is intact"* and behind *"40 numbered faults
and 178 registers are named in prose and held nowhere."*

**That census is not reproducible, and this instrument exists because of it.**

## The problem, stated plainly

The pattern set that produced the stage-A table was never banked. Every other measurement in this
repository has a program behind it — `coverage.py`, `pointers.py`, `arith.py`, `buildtrace.py` — but
this one was a pass, and only its output survived.

Re-deriving it by eye does not land on the same numbers, and not only for the categories that could
have changed:

| kind | stage A says named in prose | a fresh pattern gives |
|---|---:|---:|
| Rulings | 47 | 54 |
| `W-` entries | 164 | 200 |
| Registers | 734 | 1,244 |

**Rulings cannot have changed** — no ruling was added to the chat export between the two passes. The
difference is entirely in what each pattern counts. So the stage-A figures are a record of what one
pass found under an unstated method, and **the two censuses must not be subtracted from one
another.** A "178 → 304" would be a fabrication.

This instrument does not correct the table. It replaces the *method*, so that the next change to the
tree can be measured against a fixed thing instead of against prose.

## What it does

One pattern per identifier kind, all eight declared in `PATTERNS` where they can be argued with, and
the register floor of 165 taken from `register_cites.py` by way of `tools/pointers.py` — below it a
three-digit token is not a register citation at all.

```
python3 tools/idcensus.py --selftest    # assert the patterns and the exclusions
python3 tools/idcensus.py               # the census
python3 tools/idcensus.py --list        # and name every prose-only identifier
python3 tools/idcensus.py --kind Register
```

## What it refuses

- **It will not count the repository's own audit files as presence.** `PROSE-ONLY.tsv`,
  `RETRACTION-AUDIT.tsv`, `HANDOFF-GAP.tsv`, `REGISTER-GAPS.tsv` and their documents **quote the
  export**. Counting them makes an identifier read as held because a session wrote down that it was
  not. The exclusion list is `EXCLUDE`, in the source, where it can be disagreed with. This is the
  same trap that made an earlier verification command in `docs/PROSE-ONLY.md` match its own findings.
- **It will not call a prose-only identifier a loss.** A name in prose is not proof a file or an
  entry ever existed — the discipline `coverage.py` states for `ABSENT`, and it applies here
  unchanged.
- **It pins no total in its selftest.** A total is the thing that moves; the fixtures are the
  patterns themselves, the register floor biting at 164/165, and the exclusions being in place.

## The census as it stands

```
kind          in prose  in repo  prose-only
W-entry            185      195           0
Ruling              55       55           0
Docket              39       39           0
Fault              238      220          18
Register          1397     1071         329   (+21 above the Register's max 1792, read as line refs)
MC-entry            56       55           1
DEF                 58       65           1
HANDOFF            111      107           6
```

**The governance spine is intact, and now under a banked method.** Zero prose-only rulings, zero
dockets, zero `W-` entries. That was stage A's headline finding and it survives re-measurement — the
one result here that can be said to corroborate the earlier pass rather than merely differ from it.

Three of these numbers are only right because two spellings are handled, and both were found making
the first run of this file wrong:

- **Zero padding.** `W-001…W-027` and `W-1` are the same entry written two ways. Counting them
  separately reported **15 prose-only `W-` entries**; normalising leading zeros gives **0**, which is
  also what stage A found. `MC-entry` went 4 → 1 the same way.
- **List continuation.** `MC-07/08/09` and `registers 219, 220, 221` carry the prefix once. A pattern
  requiring it on every element reads the first and loses the rest — understating what the prose
  names and, through the repository side, overstating what is prose-only.

**A register numbered above the Register's own maximum is reported, not counted.** Twenty-one of
them: `4481` is `WORKING-REGISTER.md`'s line count and not an entry at all, as `docs/REGISTER-GAPS.md`
established. `1793` and `1794` are the two real entries drafted past the end and are *not* in that
set. Folding line references into a prose-only count would inflate it by a fifth.

## What its numbers are, and are not

They are a measurement under a declared method, taken after the `RECOVERED-BY-WRITE` pass seated 759
artefacts. They are **not** an update of the stage-A table and **not** a correction of it. Where the
two disagree, the honest reading is that two different questions were asked.

The one figure in `docs/PROSE-ONLY.md` that *was* re-measured comparably — the fault census, run
twice with the same pattern before and after the recovery — moved from 40 prose-only to 16, and that
comparison is sound because the method was held fixed across it.
