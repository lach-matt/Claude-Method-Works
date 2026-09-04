# BRIDGE — THE LÖWDIN SESSION (single-problem chat, 2026-08-15)

*A one-problem-per-chat session run outside the main line, on M's direction, after
context exhaustion in the 1.8.x series. Bank in: `restore-point-2_13.tar.gz`
(694 files, register at R 1700, certificate 1.8.3). **Nothing was written to the
register, the chapter, the book or any generated artefact** — M ruled that writing
is handled in a separate chat of this project. Everything below is computed, with
the script behind each claim named. Two register entries and one chapter rewrite
are OWED; see §7.*

---

## 1 · WHAT THIS SESSION WAS FOR

M: *"I want to work on the Löwdin challenge solution… I have run out of context
window, so I want to try a different approach — working out individual problems from
the project, one chat at a time."*

Method adopted: one bounded problem per chat, closed to a written result, with the
next chat starting from the result rather than from reconstruction.

## 2 · WHAT WAS READ, IN ORDER (Zeno: fetch/read closed before analysis opened)

1. `DIGEST.md` in full — per R 1685, a session states nothing about the work until
   the digest is read. (R 1685 had broken three times; it did not break here.)
2. `BOARD.md` (rebuilt at R 1700) and `HANDOFF-CERTIFICATE-1_8_3.md`.
3. `CHAPTER-LOWDIN.md` in full — 206 lines, DRAFT, written at R 1569.
4. `BOARD-REEVALUATED.md`, `LOWDIN-LITERATURE.md` §7 and §8.
5. Register entries R 1517, 1521, 1586, 1614, 1617, 1621 at source.

**Scope audited before any search** (the standing correction from R 1672): 694 files,
by extension .py 336 · .tsv 205 · .md 55; the register was searched by ENTRY, not by
line, because a wrapped line beginning with digits reads as a false heading — R 1617's
own recorded fault.

## 3 · THE FIRST FINDING: §8 OF THE CHAPTER IS STALE

`CHAPTER-LOWDIN.md` §8 lists four items as open. Checked against the register:

| §8 item | true state |
|---|---|
| **P3** — why the Klechkovski–Hakala onsets are exact | **CLOSED at R 1617**, and closed NEGATIVELY for the derivation path |
| Demkov–Ostrovsky / the guessed potential | **CLOSED at R 1621** as P2; the corridor conjecture was tested and NOT supported |
| **clique-3 obstruction at B/La/Lr** | genuinely open — no register entry mentions a clique after R 1569, and it is on no board |
| **P1** — what the corridor is an instrument of | genuinely open (board row 10) |
| **P4** — a seventh placement rule for a | a PROHIBITION, not a gap |

**This is the same fault §34 of the book has**: the chapter was written at R 1569 and
two of its open items closed within fifty registers. A reader today takes settled work
for a gap. *I had recommended opening P3 before reading the file; M stopped it. The
whole recommendation came from the chat record rather than the artefact — the standing
correction "never summarise without the file behind the summary", live.*

For the record, since the chapter still misstates it: **P3's answer (R 1617)** is that
a Janet group M holds the subshells with n+ℓ = M and ℓ < n, so ℓ runs 0 to ⌊(M−1)/2⌋
and the capacity is Σ2(2ℓ+1) = 2(L+1)², because consecutive odd numbers sum to a
square. Groups come in PAIRS of equal capacity, and that pairing IS 2,2,8,8,18,18,32,32.
K(x) = x(x²+2−3μ)/6 is a closed form for that sum, verified as an identity x = 1…25.
**K is not a fit to data, and carries no information about any amplitude** — which is
why it closed negatively for R 1586's derivation path.

---

## 4 · CLIQUE-3 — CLOSED, AND IT CLOSES AS A CORRECTION
*Script: `clique3.py`. Artefact: `CLIQUE3-FINDING.md`.*

### 4.1 Reproduced at source, by two routes
The 106 corridors were rebuilt from `brack.py`'s own construction — bound =
(Δn)/(√p_rival − √p_entrant), node counts only, nothing fitted. Greedy-by-right-endpoint
(maximum disjoint set) and brute-force max clique on the conflict graph agree:

    106 corridors · 735 edges · density 0.132 · max clique 3 · 10 isolated vertices
    minimum stabbing points 3, at 0.7071, 1.7071, 2.4409

R 1517 and R 1521 confirmed exactly.

### 4.2 The generating form
Write **g(p) = 1/(√(p+2) − √p)**. A corridor is CANONICAL when both binding rivals sit
at Δp = ±2 with Δn = ±1, and a canonical corridor is then exactly the band
**( g(p−2), g(p) )**. 32 of the 106 are canonical, taking only FOUR distinct intervals:

    p=0   (−∞,      0.7071)   26 members   B C N O F Ne Sc Ti V …
    p=2   (0.7071,  1.7071)    2 members   La Gd
    p=3   (1.3660,  1.9841)    3 members   Ac Th Cm
    p=5   (1.9841,  2.4409)    1 member    Lr

g increases because √ is concave, so the bands ascend; they tile only when p advances
by 2, so the even sub-chain (0,2) and the odd (3,5) interleave and p=3 overlaps p=2 on
(1.3660, 1.7071). **That overlap is why the answer is 3 and not 4.**

### 4.3 THE CORRECTION TO R 1517
R 1517 reads *"forced by three elements — boron, lanthanum and lawrencium."*
**There are 205 maximum cliques, not one.** Sorted by upper endpoint:

    slot 1   51 distinct elements interchangeable   (B is merely the first)
    slot 2    5 elements: Ac, Th, Cm (51 certificates each) · La, Gd (26 each)
    slot 3    Lr ALONE, in all 205

57 of the 106 vertices appear in some maximum clique. **Only lawrencium is forced.**

Naming B and La as the obstruction is the **object-versus-observer coordinate fault**
again — a property of a class attributed to whichever representative the greedy scan
reached first (cf. R 1578's five prior occurrences; R 1672's negative-from-scope).

Lr is different in kind: it is the sole member of the p=5 band because it is the only
entrant in the table with p = 5 bracketed at p ± 2 (7p against 6d below, 8s above).
**That is a fact about where the table ENDS, not about lawrencium** — consistent with
R 1696, where Z = 120 is a declared bound and not a discovered closure.

---

## 5 · P1 — WHAT THE CORRIDOR IS AN INSTRUMENT OF
*Scripts: `p1.py`, `p1b.py`, `p1c.py`. Artefact: `P1-FINDING.md`.*

### 5.1 The test that could fail
A one-parameter form **ν = A(n,ℓ) − a·B(n,ℓ)** turns each step into one linear
inequality in a, hence one interval. Vary B over candidate forms on the SAME observed
order. Invariant verdict ⇒ the corridor measures the atom. Moving verdict ⇒ it measures
the form. **It moves.**

### 5.2 The class is finite-dimensional
The constraints evaluate B only at integer p ∈ {0…7}, and translation and scaling
cancel in the differences. **A candidate form IS an increasing 8-vector** — so the
class can be sampled exhaustively rather than probed with named functions.

    30,000 increasing 8-vectors, uniform      2,206 feasible
      of those, clique 3 / 4 / 5              1,843 / 354 / 9
     5,000 vectors from the CONCAVE cone      5,000 feasible, clique 3 in ALL 5,000

### 5.3 WHAT SURVIVES
> **If the ordering functional is concave in the node count, the table is representable
> and requires exactly three parameter values.**

Sufficiency at 5,000/5,000, clique pinned at 3 throughout. **A proof is owed and was
not attempted.** The corridor is an instrument of the candidate form's SHAPE — not of
the atom, and (R 1621) not of the Demkov–Ostrovsky degeneracy.

**What belongs to ν alone: the stabbing points.** Under √p, 0.7071 / 1.7071 / 2.4409;
under p/(1+p), 1.5 / 7.5 / 24.0; under 1−e^(−p), 1.157 / 8.546 / 171.6. *The surds are
ν's coordinates for the number three, never the content of it.* This is R 1517's
"forecloses a family and returns three" made exact: the family is now named.

### 5.4 TWO SELF-CORRECTIONS, MADE IN SESSION
- **Necessity of concavity — WITHDRAWN.** I first wrote that strict concavity in p is
  NECESSARY, generalising from seven named functions. 2,928 non-concave vectors are
  feasible. This is P5 and §2.14 — compute before assuming — and it is the fault the
  book records as its most violated.
- **Local concavity at p = 2,3,5 — WITHDRAWN.** Feasible vectors are enriched for
  negative second differences exactly at the three canonical band indices (0.760, 0.655,
  0.770 against an infeasible baseline near 0.48), while p = 1,4,6 run BELOW baseline.
  Tested as a condition it admits 1,702 infeasible and misses 1,394 feasible.
  **A correlation, not the condition.** The exact condition is NOT characterised.

---

## 6 · THE SIX — ONE OBJECT SEEN TWICE

The steps that refute a linear or convex form (B = p^β, β ≥ 1; boundary exactly at
β = 1, every β < 1 feasible at all 106):

    Z= 57 La  enters 5d  p=2      Z= 89 Ac  enters 6d  p=3
    Z= 64 Gd  enters 5d  p=2      Z= 90 Th  enters 6d  p=3
                                  Z= 96 Cm  enters 6d  p=3
                                  Z=103 Lr  enters 7p  p=5

**These are exactly the members of the three upper canonical bands of §4.2** — p=2
{La, Gd}, p=3 {Ac, Th, Cm}, p=5 {Lr}. Two computations sharing no code path returned
one set of six. The bands whose disjointness forces clique 3 are the same steps that
force concavity.

And they are the named anomalies. **La and Ac are the two elements at which Madelung is
false** — the chapter's firmest result (§2, R 1594). Gd and Cm are the half-filled-f
contests; Th and Lr the remaining d and p anomalies. *The exceptions are not noise
around the rule; they are the entire measurement. The other hundred steps are silent
about the form's shape.* This meets Schwarz's objection on its own terms
(`LOWDIN-LITERATURE.md` §7, failures concentrated in d and f): the concentration is
not a symptom, it is the signal.

*Where else this object appears is not yet asked — per M's standing direction to ask
"where else does this exact object appear" whenever a piece verifies. The three
numbers {2,3,5} recur as band index, as clique slot and as binding second difference;
whether that is one object or three is UNTESTED.*

---

## 7 · WHAT IS OWED (to the writing chat — nothing was written here)

1. **R 1701** — clique-3: the generating form g(p), the four canonical bands, 205
   maximum cliques, only Lr forced. **Corrects R 1517's attribution.**
2. **R 1702** — P1: concavity sufficient, clique 3 an invariant of the cone, both
   self-corrections registered rather than dropped (the pattern of R 1672, R 1675).
3. **`CHAPTER-LOWDIN.md` §8 rewrite** — P3 and Demkov–Ostrovsky are listed open and
   were closed at R 1617 and R 1621; clique-3 and P1 now answered. §8 currently
   misstates the state of its own work, as §34 of the book does.
4. **Gate discipline**: any of the above requires `python3 register_gen.py > REGISTER.md`
   (with the redirect — R 1700's recorded failure), then 25 audits and round-trip.

## 8 · WHAT REMAINS OPEN

- **The exact feasibility condition on the 8-vector.** Concavity is sufficient only;
  neither global nor local concavity is necessary. Not characterised. *This is the
  direct successor to this session.*
- **A proof** that concavity ⇒ feasible with piercing number exactly 3. Measured at
  5,000/5,000; not proved.
- **Whether {2,3,5} is one object or three** — band index, clique slot, binding second
  difference.
- **Whether a table extended to Z = 120 realises a band above p = 5.** Not computed.
- **Whether the 74 non-canonical corridors admit a second closed family.** Not computed.
- **P4 stands as a prohibition**: a seventh placement rule for a is not to be attempted.

## 9 · THE STANDING VERDICT, UNCHANGED

**Löwdin's challenge is not met.** Concavity in the node count is a NECESSARY-SHAPE
result on the candidate form, established by refutation — not a mechanism producing
one, and not a derivation from the Schrödinger equation. What this session closed is
the account of what the instrument measures and where the obstruction sits.
The chapter's own honest summary stands.
