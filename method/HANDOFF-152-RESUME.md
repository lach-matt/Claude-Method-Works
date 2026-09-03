# HANDOFF-152-RESUME.md — what chat 152 must know before it resumes

Written by **chat 151-R** at its close, for the session M paused. Not a seated member: a staging
document, like `REGISTER-QUEUE-APPEND-cypher-audit.md`.

## 1. Open from this branch, not from your own

`claude/cypher-analysis-method-books-826x0x` is **superseded**. The store is
`claude/book-builder-audit-progress-54wzox` at **BUILD92 main + BUILD191 compendia**, 424 members.
Your work is all in it. Your branch remains in git history and nothing on it is lost.

```
python3 method/verify.py     # 424 members, both bundles, VERIFY OK
```

## 2. Three of your numbers were re-keyed, all on M's rulings

| yours | now | why |
|---|---|---|
| *"chat 153"* in your W entry | **chat 152** | M: there is no chat 153 |
| `W-190` | **W-195** | chat 151-B had already seated a different W-190 |
| `BUILD181` `bfa0d975…` | **retired** | 151-B's BUILD181 `2fbcd461…` is the chain; yours is a sibling from the same BUILD180 parent |
| `BUILD91` main `7ff88249…` | **retired** | superseded by BUILD92; the name 91 is skipped so no two bundles share one |
| Register entries **1793/1794** | **kept by you** | `r3-wl` (approved at chat 128) also claimed them and **re-takes** |

**Your W entry is seated verbatim and unedited.** Its internal `153` and `DEF-153` labels stand as you
wrote them; the corrections are in the framing above it. Your six members — `cypher.py`,
`audit_lambda.py`, `close_main.py`, `register_counts.py`, `CYPHER.md`, `AUDIT-LAMBDA.md` — are seated
byte-identical at BUILD186.

## 3. Your BUILD91 was split, and only half was taken

M ruled the chat-67 hold against it: **the entries stand, the repair waits.** `close_main.py` was run
**without `--recount`**, so BUILD92 carries 1793–1796 and the Register's two count sites are exactly
as they were. **Do not run `register_counts.py --write` under the hold.** `reg1-04` now stands as a
finding that the front matter is stale by **five** entries, and R3 repairs it with its class.

**Your entry 1796 created a defect.** Census **1557**, `C13-HANDLE-LEAK` at reg L6626: it prints
`BUILD180` in a reader-facing volume. Closed as a defect on the standing ruling (26b-10 / ruling 46 /
docket 28; precedents 1536, 1556). No new ruling; R3 repairs it with its class.

## 4. What your build broke, and what now exists because of it

Seating four Register entries was the **first thing since chat 62 to move the main bundle**, and the
store assumed it never would. **28 of 86 goldens moved.** Twenty-five were re-banked at BUILD188;
`DEFECT-CENSUS.tsv` went stale and had no route at all. Two new tools exist, siblings of your
`close_main.py` and built to its discipline:

* **`close_rebank.py`** — re-banks a golden by **running its instrument**. Refuses a copy, a non-zero
  exit, or an unchanged output.
* **`close_census.py`** — regenerates `DEFECT-CENSUS.tsv`. Its guard is **id stability**: census ids
  are cited by every `CENSUS-CLOSURES-*.tsv`, so it refuses unless every id survives with its class,
  volume and line and new ids run contiguously above the old maximum. **An id is an address, not a
  position.**

**Re-bank in two passes.** The census is itself an input to instruments: regenerating it moved
`r2-ch16t` and `r2-reg12` a second time. One pass leaves the second set silently stale, and a stale
golden is worse than a red one because the gate reports it green.

## 5. The gate, and what is known red

```
./method/bin/stage-gate
export PATH="$PWD/method/bin:$PATH"
cd /home/claude/members
python3 gate.py census
python3 gate.py run --core
python3 gate.py manifest --main ../The_Method_1_6_BUILD92_main_and_register.md
python3 gate.py run --all
```

**`gate.py manifest` must be given `--main`.** Its `MAIN` constant still names BUILD90; that constant
is a **default** and line 42 takes the flag. Nothing is patched to make this work. (Line 37 already
resolves the compendia bundle by glob — the same file holds both the right pattern and the wrong one.)

**`run --all` is 82 of 86, and the four are known:**

* `r2-26b` exits 1, `r3-wl` exits 1, `r2-regsweep` exits 0 while printing `INSTRUMENT FAULT - STOP`.
  All three **assert the Register's extent as an invariant** rather than scoring it as a claim.
  **Extent is data.**
* `r2-ch23b` TIMEOUTs at 300 s against `gate.py`'s own 270 s ceiling and reproduces byte-exact run
  alone. An environment note about this container, not a fault.

## 6. What is owed, and the order

1. **`r3-wl2`** — the withdrawn-law class re-taken on numbers that clear **1797**, which your own queue
   stages for `audit_math.py`. `r3-wl` is seated and is never edited in place.
2. **`r2-regsweep2`** and **`r2-26b2`** — successors that score the extent instead of asserting it.
3. **Neither `audit_math.py` nor entry 1797 is seated.** They are yours to seat or to withdraw.

All three successors are **readings, not re-banks**, and until they exist the gate carries three
known-red instruments — which is how a real failure gets missed.

## 7. Standing, unchanged

The chat-67 hold; **RUL-128 item 1 — the mathematics first, then the prose, then the appendices**;
the chat-81 cadence; the chat-95 escalation bar; instruments travel as bundle members (chat 68);
Register entries append-only; no silent change. M's **hybrid** store ruling: Drive for Cowork chats,
the repository for Claude Code sessions, one session that reaches both reconciles. **Drive stands at
BUILD184**; this tree is ahead of it, and the next reconciliation is owed before either surface
advances two more builds.
