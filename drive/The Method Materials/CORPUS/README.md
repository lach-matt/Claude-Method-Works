# The Method 1.6 — corpus checkout

Produced by **chat 149 (Cowork)** on 2026-09-02 so that the corpus can be indexed by
Graphify and reached from a repository checkout instead of being re-downloaded and
re-extracted from Drive at the top of every chat.

Nothing here is new subject matter. Every file is a byte-exact copy of a member of one of
the two live bundles, extracted with the standing regex and verified in both directions.

## Provenance (all MEASURED, chat 149)

| bundle | Drive fileId | bytes | md5 | lines | members |
|---|---|---:|---|---:|---:|
| `The_Method_1_6_BUILD90_main_and_register.md` | `1lJ9R3vqAz3TNriJOyxJIKJGh5HqwY7GH` | 1,983,081 | `49065309b0c4fe8e055f693aed295cca` | 18,470 | 2 |
| `The_Method_1_6_BUILD179_compendia_papers_audits.md` | `1X317KPEdk7Jvv6jTDMFEUsgXA2adhNk9` | 5,683,169 | `6251dc1351f165aef874b9cf4d8a45c1` | 64,753 | 337 |

Both md5s match HANDOFF-101. Extraction used the standing member regex
`^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n` with `re.S|re.M` on the decoded bytes
(CLAUDE.md §9), decoded with `validate=True` (G0e), into a single flat `members/`.

`CLAUDE.md` here is the Drive project instruction (13,157 B, md5
`e72d4bc9cd07e1a87f56dd69b8c8886b`), decoded from the session transcript rather than
hand-transcribed (G0e). **It is a project instruction, not a bundle member — it is
deliberately outside `members/` and must never be added to a build.**

## Round-trip guard

The tree is not merely *derived from* the bundles; it *reproduces* them. For each bundle
the build spliced every member body from this tree back into the original bundle bytes at
its recorded offset and asserted the md5 of the result:

```
BUILD90_main          1,983,081 B  49065309b0c4fe8e055f693aed295cca  members   2  roundtrip OK
BUILD179_compendia    5,683,169 B  6251dc1351f165aef874b9cf4d8a45c1  members 337  roundtrip OK
```

So a checkout of `members/` is the extraction the §0 gate produces — provably, not by
assertion.

## Layout

```
method/
  CLAUDE.md            project instruction (NOT a bundle member)
  README.md            this file
  MEMBER-INDEX.tsv     member, bundle, ext, bytes, md5, bundle_offset — one row per member
  corpus-summary.json  counts and totals by extension, and the bundle facts above
  verify.py            re-checks every member against MEMBER-INDEX.tsv
  members/             all 339 members, flat and byte-exact
```

`members/` is flat and uses the members' bare canonical names because that is how the
method addresses them everywhere ("read MEMBERS never a bundle path"), and because it is
what makes the round-trip guard above meaningful. Do not reorganise it.

339 members, 7,645,907 B:

| ext | n | bytes |
|---|---:|---:|
| `.py` | 116 | 1,356,365 |
| `.md` | 79 | 4,776,212 |
| `.out` | 67 | 1,045,694 |
| `.tsv` | 57 | 360,024 |
| `.json` | 11 | 79,441 |
| `.log` | 7 | 5,351 |
| `.txt` | 2 | 22,820 |

## Verifying a checkout

```sh
python3 method/verify.py            # from the repository root
```

It re-hashes every file in `members/`, compares against `MEMBER-INDEX.tsv`, and reports
any missing, extra, or altered member. It needs no network and no bundle.

`.gitattributes` sets `* -text` for this subtree so git performs **no** end-of-line
normalisation. Without it a checkout on another platform would silently change every
member's md5 and every round-trip guard would fail.

## What this does and does not change

- The **`.py` members are the point.** 116 instruments — `gate.py`, `close.py`, `r2lib.py`,
  `r2-tools.py`, `tower-2.py`, the `r2-ch*` family — become graph-queryable, so a symbol,
  its callers and its blast radius can be found by query instead of by extracting 7.6 MB.
- The `.md`, `.tsv`, `.out` and `.json` members are here so a checkout is *complete* and
  the round-trip holds. Graphify indexes code symbols; do not expect the Register or
  `DOCKET.md` to become graph nodes. They are reachable as files in a checkout, which is
  still strictly better than nothing.
- **Drive remains the store** (chat-68 ruling, restated chat 74 and by M in chat 147). This
  repository is an *index and a convenience*, never a second source of truth. When the two
  disagree, Drive wins and this tree is stale — regenerate it, do not repair it.
- Bundles themselves are not committed. They live in Drive; their md5s are recorded above.

## Regenerating after a new build

This tree is disposable. After the next `close.py` produces BUILD180+, rebuild it from the
new bundle rather than patching members here, and let the round-trip guard prove the result.
