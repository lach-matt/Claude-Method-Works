# The Löwdin challenge

> **DRAFT — UNFINISHED, AND DELIBERATELY SO.**
> This chapter records where the work stands, not where it will end. It
> supersedes §34 of *The Method 1.6*, which was written before register 1460
> deactivated ν as a law and still presents ν as the solution. Everything
> below is registered; the register numbers are given so any claim can be
> checked against its own computation. Written at register 1569.

---

## 1 · The challenge, and its standing

In 1969 Per-Olov Löwdin asked for a derivation of the n+ℓ filling rule from
the Schrödinger equation. It has stood since.

**It is open by consensus, and we did not establish that ourselves — we found
it out late.** Scerri, *Phil. Trans. R. Soc. A* **378**, 20190300 (2020):
numerous authors claim to have met the challenge, and the generally held
opinion is that none has succeeded as Löwdin intended it (R 1450). *A
precedent search was owed from the beginning of this work and was run near
its end. That order was the wrong way round and the register says so.*

## 2 · The wrong target, and this is the chapter's firmest result

**The n+ℓ rule is not what atoms obey.**

Read from the observed ground configurations of all 108 neutrals, the sequence
in which subshells OPEN is

> 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **5d 4f** 6p 7s **6d 5f** 7p

**Madelung's rule inverts 5d/4f and 6d/5f.** Lanthanum opens 5d at Z = 57 and
4f does not appear until cerium; actinium opens 6d at Z = 89 and 5f not until
protactinium. Seventeen of nineteen openings agree; two do not.

**So deriving n+ℓ exactly would mean deriving something false at two
elements.** The target is the ORDER. n+ℓ is a name for that order which is
about 89% accurate, and a derivation of the name is not a derivation of the
thing.

*This survives everything that follows. It does not depend on ν, on the
corridor, or on any fitted quantity.*

**Verified against NIST's own ground-state listing (R 1594).** The ionisation
fetch of register 1593 carried ground configurations for all 108 elements, and
they were read for a different purpose:

    Z = 57  La   [Xe]5d 6s²        opens 5d — NOT 4f
    Z = 58  Ce   [Xe]4f 5d 6s²     4f appears HERE, one step later
    Z = 89  Ac   [Rn]6d 7s²        opens 6d — NOT 5f
    Z = 91  Pa   [Rn]5f² 6d 7s²    5f appears HERE, two steps later

*A capture made to select reading targets confirms the chapter's target
correction. Madelung's rule is false at two elements, from the source.*

## 3 · ν, and its deactivation

The work's central construction was

> **ν(n, ℓ, q) = n − a·√( n − ℓ − 1 + q/2(2ℓ+1) )**
>
> the incoming electron occupies the subshell of least ν among those with
> q < 2(2ℓ+1).

**Both Pauli quantities appear**: the capacity 2(2ℓ+1) governs admissibility
and also sits inside the radicand, which counts the states below — complete
lower shells of the same ℓ, plus the fraction of the current one already
filled. **The occupancy enters only through Pauli**, and with the fraction in
the radicand the scatter in a within a subshell falls from 0.187 to 0.041 at
3p, 0.119 to 0.028 at 4p, 0.088 to 0.018 at 5p. Raw occupancy makes every one
worse.

**ν IS DEACTIVATED AS A LAW AND RETAINED AS A FORM (R 1460).** Three findings
forced this and each is independent of the others.

**(a) The score was fitted.** `scorer.py` placed a using each step's own
corridor — and a corridor is built by `brack.py` FROM the observed entrant at
that step. The answer was setting the parameter that produced the answer.
**Held out, the walk scores 90 against plain Madelung's 96** (R 1445). *A
construction that loses to the rule it was built to explain has not explained
it.*

**(b) The physical reading is structurally impossible, not merely wrong.**
The connection δ = a√p would give ν a derivation. It cannot: **δ is bounded as
n → ∞ and a√p diverges** (R 1457–1458). The held series are flat to five per
cent where √p demands a factor of six. And the Tietz potential has no Coulomb
tail, so no defect can be derived from it even in principle. *There is no
route from the walk to δ.*

**(c) It was already known.** Register 1303 had established the impossibility
before register 1341 reopened the question. **The register caught its own
repetition**, which is what it is for.

**What ν retains: it ORDERS, and does not MEASURE.** As an ordering functional
it is intact. As an effective quantum number it is refuted. *The corridor —
the instrument built to test ν — survives entirely, and is the more useful
object.*

## 4 · What the form still recovers

**Five of Madelung's ten exceptions**, using principled placement: the
geometric mean of the binding ceilings of the current and next groups. *No
parameter is fitted at this step.* Against Madelung's own 96, the fitted form
reached 99 and the held-out form 90 — but the five exceptions are recovered by
a rule stated in advance, and that is a different kind of result from a score.

**And held out properly, the walk reaches 92 (R 1580).** `trajectory.py` places
a only on corridors already revealed — the witness principle of register 1578
applied to the walk. Four placements already on record, measured honestly:

    floor    87        the fitted ordering INVERTS
    mid      83        (fitted: floor 99, mid 100, ceil 93)
    ceil     82
    STAY     92        move only when the witnessed window forces it out

**The placement using the LEAST information wins.** That is an overfitting
signature, measured rather than asserted — and the walk still loses to plain
Madelung's 96.

    the law admits          100 / 106
    plain Madelung           96 / 106
    the best honest walk     92 / 106
    the leaked figure        99 / 106   ← not admissible

**The trajectory's cost of not seeing the future is eight points.**

**Where it fails, it fails in a nameable place.** The corridor's feasible set
is empty exactly where two constraints conflict, and those places are
enumerable rather than mysterious.

## 5 · The corridor is additive representability, and this was known in 1959

The corridor construction — a system of linear inequalities in one unknown,
one per step, feasible iff a placement exists — **is an instance of additive
representability of a ranked order.** The literature is Kraft–Pratt–Seidenberg
(1959), Scott (1964), and Krantz–Luce–Suppes–Tversky (1971). **Empty feasible
sets correspond exactly to cancellation conditions.**

**Fishburn's warning is on the record and is a standing caution**: low-order
feasibility does not imply global representability. A corridor that is
feasible at every order tested may still fail at an order not tested.

## 6 · The measure: Helly, and three names for one number

**The index forecloses a family rather than supplying a mechanism, and it
returns the number three** (R 1517).

Each object here is a system of linear inequalities in d unknowns, and the
Helly number is h = d + 1. **Register 489's "one level short", Freuder's
k-consistency, and the KPS cancellation conditions are THREE NAMES FOR h.**

| object | d | h | feasible | fails at order |
|---|---|---|---|---|
| Λ | tree | 2 | **yes**, E = 0 | — |
| Löwdin | 1 | 2 | **no** | 2 — 183 disjoint pairs, minimum 3 values |
| nuclear shell | 1 effective | 2 | **no** | 2 — K(3,3), certificate one edge |
| M.C2 | ternary, decomposes | — | conditional | no defect |

**The binary mechanism is a conflict graph** (R 1521): vertices are
constraints, an edge joins two that cannot hold together, and **the maximum
clique IS the verdict.** Λ has clique 1 and closes. M.C2 has clique 1 and is
conditional. The nuclear corridor has clique 2 and is refuted. **Löwdin has
clique 3** — and the three values that cannot be reconciled are at boron 5,
lanthanum 57 and lawrencium 103.

**And three languages describe the same thing** (R 1518): geometry
(Helly, Radon, Gallai), logic (k-consistency), statistics (centrepoint,
fractional Helly). *Use the language that is NON-DEGENERATE for the object.*
For Löwdin, d = 1 and the geometry face is the live one.

## 7 · Belokolos, and what a global form with exceptions is not

Belokolos (2017) derives Madelung's first rule by requiring Coulomb behaviour
at the origin, which forces the frequency ratio α = 2. **That answers the
"guessed potential" objection** and is properly attributed.

**It does not answer Löwdin.** A global form with exceptions is not a solution
for all circumstances, and his ranking is 87 of 106 (R 1520). *The distinction
matters and is not a criticism of the paper: it answers a different question,
well.*

## 8 · What is actually open

**The challenge is not met here and the chapter says so plainly.**

- **The order is the target, not n+ℓ.** Settled, and independent of everything
  else in this chapter.
- **ν orders and does not measure.** Settled.
- **The corridor is additive representability.** Settled, with Fishburn's
  caution standing.
- **The clique-3 obstruction at B/La/Lr.** Measured. *Why those three and not
  others is not explained.*
- **P1 — what the corridor is an instrument OF.** Open. The question is no
  longer "what is a" but what class of problem the corridor measures.
- **P3 — why are the onsets exact?** K(x) = (1/6)x(x² + 2 − 3μ(x)) reproduces
  all eight Klechkovski–Hakala onsets exactly. **Nobody here knows why.**
- **P4 — a seventh placement rule for a is NOT to be attempted.** Six have
  failed. This is recorded as a prohibition, not a gap.

---

*The honest summary: the method established what the target is, refuted its own
candidate law by three independent routes, identified its instrument as a
known construction from 1959, and measured the obstruction. It did not derive
the filling order from the Schrödinger equation. Löwdin's challenge stands.*
