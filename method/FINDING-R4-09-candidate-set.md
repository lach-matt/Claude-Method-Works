# FINDING R4-09 — the one thing in Chapter 34 the data cannot settle, and it needs M. Does the law's candidate set include g subshells?

Found 6 September 2026, from M's instruction on finding R4-06 to search the repository exhaustively
before deriving. The search found more than the answer: it found that **two instruments in this
repository compute the same corridor and disagree**, and that a seated Register entry's universal is
true under one and false under the other.

`method/proofs/candidateset.py` measures both; its selftest asserts the seated instrument's own
banked corridor values.

## The two generators

| | candidate set |
|---|---|
| **`r2-ch16y.py`** — a **seated member** | every (n, ℓ) with n ≤ 7, **ℓ ≤ 3**, not at capacity. **No g subshells.** |
| **`walk.py`** — recovered, and the instrument that produced §34.6's eighteen | ℓ = **0 to 4**, **g included**: every partly-filled subshell of each ℓ, plus the first empty one. |

## They disagree at exactly one place, and it is one subshell

At protactinium the entrant is 5f, whose node count n − ℓ − 1 is **1**. A rival lies below it exactly
when its node count is smaller, which is zero. The node-count-zero subshells are 1s, 2p, 3d and 4f —
**all full at thorium** — **and 5g, which is empty**.

| | 4f at Ce 58 | **5f at Pa 91** |
|---|---|---|
| seated `r2-ch16y.py`, ℓ ≤ 3 | (−∞, 0.7071068) | **(−∞, 1.3660254)** |
| `walk.py`, ℓ ≤ 4 | (−∞, 0.7071068) | **(0, 1.3660254)** |

The 4f corridor is identical under both. **The 5f corridor is not.** Without g nothing lies below 5f
and the floor is −∞; with g, 5g lies below it and the floor is zero.

## What that one subshell decides

**1. Register 1414, and it is seated.**

> *"**THE FLOOR EXISTS EXACTLY WHEN THE ENTRANT HAS NODES: 106 OF 106, DERIVED.** … the floor is
> minus infinity exactly when the entering subshell is node-free, that is when n minus ℓ minus one
> is zero, because no rival can have a negative node count. **One hundred and six of one hundred and
> six, no exception, and derivable rather than observed.**"*

| | |
|---|---|
| with g admitted (`walk.py`) | the iff holds at **106 of 106**. The entry is **true as printed.** |
| without g (the seated instrument) | the iff **fails at eleven steps** — every 5f step from **Pa 91 to No 102**, each with L = −∞ and a node count of one. |

**2. §34.9's conclusion,** *"no rival lies below and L = −∞"* at every f opening. **True without g;
false at 5f with it**, where the floor is zero.

**3. Register 1403's** *"protactinium's L is degenerate at zero"*. That is `walk.py`'s answer. The
seated instrument's banked output prints **(−∞, 1.3660254)** at the same step.

**And one thing needs no ruling.** §34.9's *premise* — *"at any f opening p = n − ℓ − 1 = 0"* — is
false at 5f under both, because 5 − 3 − 1 = 1 either way. That is finding R4-06 and deviation
16z-05, and it stands whatever M decides here.

## Why the data cannot settle it

**No g subshell is occupied in any neutral atom in the table.** The two candidate sets therefore
agree on every observation and differ only in what the law is permitted to **consider**. That is a
statement about the law's domain, not about the elements, and no measurement reaches it.

**The seated instrument knows this and says so.** Its own comment reads:

> *"FAULT 3, self-caught: one generator convention is not a count. Sweep (NMAX, LMAX) and say
> which."*

It does sweep — n ≤ 7 and 8, ℓ ≤ 3 and 4 — and reports the endpoint counts under each. **But it
prints its one-sided corridors under ℓ ≤ 3 alone**, so the disagreement never surfaces in its
output.

## What is owed, and it is M's alone

**One ruling: does the law's candidate set include g subshells?**

Two considerations, stated without a recommendation because this is a subject-matter decision:

- **For ℓ ≤ 3.** It is the seated instrument's convention, it is the record's stated convention
  (READ-ch34re), and it matches the domain the chapter discusses. §34.9's conclusion then stands and
  only its reason changes, which is the smaller repair.
- **For ℓ ≤ 4.** The law's own admissibility test is *q < 2(2ℓ+1)*, and an empty 5g satisfies it
  with nothing said about ℓ. Excluding g is then an extra clause the law does not state. Register
  1414 stands as printed under this reading, and §34.9's conclusion needs correcting at 5f as well
  as its premise.

**Whichever way it goes, one printed statement has to change**, and the two are different
statements. That is why this cannot be deferred to the prose pass: the ruling decides which sentence
is repaired.

**Nothing is repaired here.**
