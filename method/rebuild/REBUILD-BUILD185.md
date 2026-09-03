# REBUILD-BUILD185.md — what BUILD185 adds to BUILD184, and how to rebuild it

Written by **chat 151-R** — a Claude Code session on the repository, not a Method chat. Unlike BUILD181
through BUILD184 this build was **made here, not carried**: its inputs are all in the repository and
none of it passed through Drive. The document exists so that a chat working from Drive can rebase on
it, or rebuild it, without this container.

## Inputs

| object | where | bytes | md5 |
|---|---|---:|---|
| BUILD90 main | `method/` | 1,983,081 | `49065309b0c4fe8e055f693aed295cca` |
| BUILD184 compendia | rebuilt per `REBUILD-BUILD184.md` | 5,977,919 | `d4350094449e3a4bf488315e21199bd4` |
| W-194.md | this build's W text | 7,561 | see git history at the seating commit |
| RUL-151R.md | `--append` into RULINGS-R2.md | 3,011 | " |
| DEF-151r.md | `--append` into DEFERRED.md | 5,494 | " |
| DOCKET-151r.md | `--append` into DOCKET.md | 3,372 | " |
| 57 new members | `method/members/`, all in git | — | listed in `MEMBER-INDEX.tsv` |

The 57 are the thirteen Register census-closure files, the fourteen `READ-reg*` records, the fourteen
Register instruments with their goldens (28 files), `r3-em.py` / `r3-em.out`, `R3-CLASS-EM.md` and
`WITHDRAWN-RECOVERED.md`.

## Steps

0. Rebuild BUILD184 first, per `REBUILD-BUILD184.md` and its chain back through 183, 182, 181, 180 —
   **assert `d4350094449e3a4bf488315e21199bd4`.** Everything below is on top of it.
1. **Regenerate every golden by running its instrument**, never by copying:
   `gate.py bank r2-reg1a` … `r2-reg12`, `r2-regsweep`, `r3-em`. All fourteen are deterministic — no
   wall clock, no randomness — and all fourteen reproduce byte-exact in this container. Stop if any
   differs.
2. Put the thirteen `CENSUS-CLOSURES-reg*.tsv`, the fourteen `READ-reg*.md`, `R3-CLASS-EM.md` and
   `WITHDRAWN-RECOVERED.md` in `members/` unchanged.
3. Run the close, `--append` before `--members`:

```
python3 members/close.py \
  --old  The_Method_1_6_BUILD184_compendia_papers_audits.md \
  --new  The_Method_1_6_BUILD185_compendia_papers_audits.md \
  --w    W-194.md \
  --append RULINGS-R2.md RUL-151R.md \
  --append DEFERRED.md   DEF-151r.md \
  --append DOCKET.md     DOCKET-151r.md \
  --members <the 57, sorted>
```

4. **Assert the result: 6,465,999 B, md5 `e0f94372e918a59525031cdf9a9a2e98`, 72,675 lines, 414
   members.** `close.py`'s own reverse guard must report that stripping the appended text recovers
   `d4350094449e3a4bf488315e21199bd4`. Any mismatch stops with a report; nothing here is to be patched
   into agreement.

Expected inside the rebuilt bundle: MANIFEST.tsv 27,875 B / `5595922c82da8c71f7438b90aab98f0e` / 416
lines (415 listed); WORKING-REGISTER.md 939,801 B / `c00d13437a127c4ba44c15f9376f921f` / 8,029 lines,
195 W entries ending W-194.

## What this build seats

**The Register read end to end, entries 1–1792** — thirteen source-order units under the chat-81
cadence plus a whole-volume mechanical baseline — together with **M's scope ruling of 3 September**
(the Register in full, the other four compendia by class sweep), which had been staged unseated since
chat 151-B. Findings reg1-01…reg1-06, reg2-01, reg3-01, reg4-01, reg7-01/-02, reg8-01/-03,
reg12-01…reg12-03, reg13-01; reg8-02 withdrawn as false. Units 5, 6, 9, 10 and 11 recorded zero
deviations. **Nothing is applied to any reader-facing volume**; the chat-67 hold stands.

## Two hazards this build records and does not resolve

1. **A fork on the Register.** Branch `claude/cypher-analysis-method-books-826x0x` seats entries
   **1793–1796** while this read worked 1–1792. Two lines of work on one volume, to be reconciled
   before R3 touches it.
2. **Numbering.** This build is closed **in the repository** while chat 152 works R3 from Drive's
   BUILD184. **If chat 152 also closes a BUILD185 the two are different bundles under one name.** This
   document states exactly what BUILD185 adds so that either can be rebased on the other; the reverse
   guard makes the rebase checkable rather than a matter of judgement.
