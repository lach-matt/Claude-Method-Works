# READ-reg13.md — the Register: the word-by-word C9 pass, and what it found

The 223 `C9-OVERGENERALISATION-WORD` rows left engaged at reg12 are read **word by word** and closed
in `CENSUS-CLOSURES-reg13.tsv`, each with its own line, its own flagged token and its own context —
not on a class judgement.

## The tokens

| token | rows |
|---|---:|
| never | 192 |
| always | 21 |
| without exception | 5 |
| in every case | 3 |
| at every cap | 2 |

**All 223 close *not a defect*.** In every case the flagged token is bounded by its own sentence: a
stated rule (*"entry bodies are never edited"*, *"T may enter the value store as a column; never as
an axis"*), a measured result carrying its scope (*"23 of 23 monotone at ℓ ≤ 1, without exception —
He, Li, Be…"*, *"zero at every cap setting from 216 cells to 1,636"*), a mathematical consequence
(*"the penetration term is always negative, so it can never produce δ > B"*), or a fact about a named
object. That is **243 C9 rows closed across the whole read, every one not a defect.**

Two sub-kinds are worth naming because a future sweep will meet them again:

- **The token is part of a name, not a claim.** Rows 1359/1360 flag *"always"* inside the strategy
  names `always-lower` and `always-upper`. There is no assertion there at all.
- **The token is a claim being refuted.** Row 1409 flags *"a defect nearly always follows an
  ionisation energy"* — which the entry quotes **in order to say it does not hold**. Row 1250 does
  the same with an objection. Stating a universal to knock it down is not asserting it.

## A — the finding this pass turned up

**reg13-01 — the emphasis class was diagnosed, repaired, recorded, and then recurred sixteen times;
and the instrument that would have held the repair is not a member.**

Census rows 1420/1421 led to **entry 1617**, which is **live**, and which does what unit 7 did:

> *"PR4 is closed: all eight entries carried an italic body-span opened after a bold close and never
> shut, and the register's own alternating convention makes the fix unambiguous. **Thirteen
> unbalanced entries become five.** AND THE FIVE THAT REMAIN ARE NOTATION CASES EXACTLY — Λ-star, a
> wildcard tuple, Python's bracket-w-star-n, a jK parity marker, and the glob vi-star. An asterisk
> that IS the symbol cannot be balanced as markup without changing what it says, so PR5's skip list
> is those five and it is now written into `register_review.py`."*

Three things follow, all MEASURED:

1. **The notation exception this read reached independently at unit 7 is entry 1617's skip list.**
   Unit 7 separated notation from breakage by hand — `2P*`, `φ*`, the wildcard `(3, 0, 1, 1, *, 0, 1,
   1)` — and 1617 names the same kinds. Two readings, one conclusion.
2. **The repair did not hold.** The seated Register carries **22** unbalanced entries where 1617 left
   five, and **16 of the 22 were written after entry 1617** — 1642, 1643, 1646, 1648, 1649, 1652,
   1653, 1657, 1673, 1674, 1677, 1681, 1682, 1694, 1699, 1774. Three more — **313, 604, 747** —
   stand *before* 1617 and still carry the split shape, so the repair did not reach them either.
3. **`register_review.py` is not a seated member.** MEASURED: it is not in `members/`. The chat-68
   ruling is that instruments travel as bundle members; this one does not, so the checker and its
   five-case skip list are outside the bundle and no gate runs them.

**This supersedes the framing of reg7-01 and reg8-03.** The class is not merely one the record
diagnosed and lost (1743/1744, withdrawn). It is one the record diagnosed, **repaired**, recorded the
repair for in a live entry, and then re-accumulated immediately — because the instrument that
enforced it never entered the bundle. `R3-CLASS-EM.md` should cite **1617** as the prior repair and
its skip list as the prior notation ruling, and R3 should seat `register_review.py` or an equivalent
into the gate, or the repair will not hold the second time either.

## Census

**223 rows engaged, 223 closed**, each individually in `CENSUS-CLOSURES-reg13.tsv` with its context.
Nothing is left open.
