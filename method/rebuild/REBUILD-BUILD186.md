# REBUILD-BUILD186.md — what BUILD186 adds to BUILD185, and how to rebuild it

Written by **chat 151-R**. Like BUILD185 this build was **made here, not carried**; its inputs are all
in the repository. It seats the six members of a third line — **chat 152**, the cypher session on
branch `claude/cypher-analysis-method-books-826x0x` — and resolves the numbering collision between
that line and chat 151-B's.

## Inputs

| object | where | bytes | md5 |
|---|---|---:|---|
| BUILD90 main | `method/` | 1,983,081 | `49065309b0c4fe8e055f693aed295cca` |
| BUILD185 compendia | per `REBUILD-BUILD185.md` | 6,465,999 | `e0f94372e918a59525031cdf9a9a2e98` |
| `cypher.py` | chat 152's `method/members/` | 45,232 | `6a7ffede…` |
| `audit_lambda.py` | " | 10,875 | `504c6a84…` |
| `close_main.py` | " | 10,111 | `e75d871c…` |
| `register_counts.py` | " | 9,691 | `6152fd71…` |
| `CYPHER.md` | " | 21,608 | `e0aadc48…` |
| `AUDIT-LAMBDA.md` | " | 5,905 | `b3dd3400…` |

None of the six collides by name with any of BUILD185's 416 members.

## Steps

0. Rebuild BUILD185 first, per `REBUILD-BUILD185.md` and its chain — **assert
   `e0f94372e918a59525031cdf9a9a2e98`.**
1. Take the six members from `claude/cypher-analysis-method-books-826x0x` at `61813ba` and put them in
   `members/` unchanged. **Assert every md5 above.**
2. **Bank no goldens.** `audit_lambda.py` and `register_counts.py` exit 1 by design while their
   findings stand, and `gate.py run` reports a non-zero exit as ERROR, so a `.out` for either would
   break the sweep. `cypher.py` takes arguments and `gate.py`'s SPECIAL table is inside a seated
   member. Chat 152 banked none either. Measured instead: `cypher.py --selftest` returns **SELFTEST
   OK, exit 0**.
3. Run the close, `--append` before `--members`:

```
python3 members/close.py \
  --old  The_Method_1_6_BUILD185_compendia_papers_audits.md \
  --new  The_Method_1_6_BUILD186_compendia_papers_audits.md \
  --w    W-195.md \
  --append DEFERRED.md DEF-152c.md \
  --append DOCKET.md   DOCKET-152c.md \
  --members members/cypher.py members/audit_lambda.py members/close_main.py \
            members/register_counts.py members/CYPHER.md members/AUDIT-LAMBDA.md
```

4. **Assert the result: 6,590,914 B, md5 `7144d18deb508e5f43852b74648885af`, 74,800 lines, 420
   members.** The reverse guard must report that stripping the appended text recovers
   `e0f94372e918a59525031cdf9a9a2e98`.

Expected inside: MANIFEST.tsv 28,275 B / `14ba7f724f6d1b198446d369ab9c51cf` / 422 lines (421 listed);
WORKING-REGISTER.md 952,117 B / `d8b8be22809c486e77ff3ba2b2a0eb2a` / 8,047 lines, 196 W entries
ending W-195.

## What this build resolves

**Two numbering collisions, both ruled by M.**

1. **There is no chat 153.** The carried entry heads itself *"W-190 — chat 153"* and names its
   deferred block *DEF-153*. M ruled it is **chat 152**. The body is carried **verbatim and
   unedited** — rewriting another session's entry would falsify a record — and the correction is
   made in the framing above it.
2. **W-190 and BUILD181 were each spent twice.** Chat 151-B: W-190 (26b-02/-03) and BUILD181
   `2fbcd461…` · 345 members. Chat 152: a different W-190 and BUILD181 `bfa0d975…` · 347 members.
   Both descend from BUILD180 `ea5becc4…` — **siblings, not a chain**. M ruled **the Drive chain
   keeps the numbers**: 151-B's stand, chat 152's entry becomes **W-195**, and its BUILD181 is
   retired as a sibling that remains in git history.

## What this build deliberately does NOT do

**BUILD91 is not carried.** Chat 152 also advanced the *main* bundle — appending Register entries
1793–1796 and **repairing the front-matter counts**. The chat-67 hold forbids editing, corrections
and Register entries until the review closes, and BUILD91 does all three. **M has parked it pending a
ruling on the hold.** The main bundle here stays BUILD90.

Measured in advance, for whenever that ruling comes: `r2-reg8a`, `r2-reg12` and `r2-regsweep`
re-bank mechanically under BUILD91; **`r2-reg1a` must be re-TAKEN**, because its printed-value
constants are BUILD90's. `r3-em` needs nothing — 246 repairs, 29 declines, +360 B either way.

`tools/audit_math.py` and Register entry **1797**, staged in
`method/REGISTER-QUEUE-APPEND-cypher-audit.md`, are **not seated** and are not this build's to seat.
