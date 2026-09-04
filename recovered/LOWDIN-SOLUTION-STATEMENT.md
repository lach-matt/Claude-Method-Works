# THE LÖWDIN CHALLENGE — THE SOLUTION THAT ANSWERS THE GLOBAL QUESTION

*Löwdin session 3, 2026-08-15. Bank `restore-point-2_13` (R 1700), unchanged; nothing
written to register, chapter or generated artefact. Inputs: the register (R 1249–1626,
1517–1521, 1617, 1621), `FEASIBILITY-FINDING.md`, `DIAGONAL-FINDING.md`,
`FACET5-FINDING.md`, `BRIDGE-LOWDIN-SESSION-2.md`. One new computation, `windows.py`,
on numbers those findings state. M's directive: not a global solution, but the only
solution that can answer the global question.*

---

## 0 · What is claimed, and what is not

**Claimed.** The global question — *why does the n+ℓ order hold, and why does it fail
where it fails* — has one answer of the right shape, and it is a decomposition, not a
formula. Every part of that decomposition is on record and each part is either exact,
proved, or measured. Where it is measured, the measurement is stated with its gap.

**Not claimed.** A single functional of (n, ℓ) that generates the 106-step order. The
record proves none exists (§2). A one-electron derivation of the amplitude a. The record
names it as the many-electron term (R 1311) and this statement locates it, it does not
supply it.

## 1 · Why there is no global solution — three facts of record

1. **The target is not n+ℓ.** The observed opening sequence inverts 5d/4f and 6d/5f
   (La opens 5d at 57, 4f waits for Ce; Ac opens 6d, 5f waits for Pa). Seventeen of
   nineteen openings agree. Deriving n+ℓ exactly derives a false statement at two
   elements (§34, R 1306).
2. **One parameter is Helly-empty.** The 106 corridors have empty global intersection at
   (1.9841, 1.0000), 183 disjoint pairs; the conflict graph has max clique 3 at B, La, Lr,
   so any one-parameter form needs at least three values (R 1517–1521). Held out, the
   best one-parameter walk scores 92 against Madelung's 96 (R 1583).
3. **The exact n+ℓ degeneracy is a threshold statement.** Demkov–Ostrovsky's focusing
   potential gives the n+ℓ multiplet degenerate at E = 0 only, lifted below (R 1626);
   Seaton's theorem places the asymptotic quantum defect at that same energy. The rule is
   exact where no bound atom sits.

## 2 · The solution — the order is two questions, and only one of them is global

**Coordinates.** A Madelung diagonal is the D-O multiplet, M = n + ℓ, with
p = n − ℓ − 1 = 2n − M − 1 on it (R 1450; DIAGONAL §1). On a diagonal n, ℓ, p
determine each other: the ordering functional ν = n − a·v(p) becomes
**ν = const + p/2 − a·v(p), one variable** (DIAGONAL §1).

**Question A — which diagonal is live.** Exact combinatorics: the onsets (R 1617;
Belokolos L_M = 2(⌊M/2⌋+1)², R 1450). This *is* the n+ℓ statement, and it is the E = 0
skeleton every atom shares. Global, closed, and not a Löwdin gap.

**Question B — which member of the live diagonal enters.** One-variable, and it is where
every anomaly lives. Along the diagonal p steps by 2 and n by 1, so member k precedes
k+1 iff a·(v_{k+1} − v_k) > 1. Hence:

> **the corridor of member k is (1/D_k, 1/D_{k−1}), D_k = v_{k+1} − v_k, and for
> concave v these cells are consecutive, disjoint, and partition (0, ∞).**

The entrant is *the member whose cell contains the atom's a*. With linear v the cells
degenerate to endpoints — that is Madelung's second rule (lower n first) and it is why
linear forms refute exactly the six interior entrants La, Gd, Ac, Th, Cm, Lr
(DIAGONAL §1, proved). The five irredundant facets (FEASIBILITY §3) are the exact
condition on v; four are stride-2 concavity on one diagonal, facet 3 is the single
cross-diagonal chord (6p M=7 before 5f M=8 at Tl–Rn).

**The one-electron shape v is measured, and it is concave wherever it can be read**:
K I, Rb I, Sr II, Cs I, Ba II — 7/7 second differences (DIAGONAL §2); Fr I on M = 8,
facet 5 satisfied by two routes (FACET5 §3); Hg II facets 4, 5. Eight for eight. Its
physics is penetration saturating in ℓ: f centrifugally excluded, d partial, p and s
fully in — Seaton and the centrifugal barrier, attributable, not new. The shape is
charge-invariant; the *order* on it flips with charge (Rb I / Sr II, Cs I / Ba II —
R 1304 reproduced) — shape is the core's, position is the atom's.

## 3 · Why this is the ONLY solution that can answer the global question

Any answer to "why n+ℓ" must contain (i) the reason the diagonals are ordered — the
threshold degeneracy, and (ii) the reason members within a diagonal are ordered as they
are, including the two inversions and the interior entrants. Fact 2 of §1 says (ii)
cannot be carried by one global number. Fact 3 says the global part of the answer is
exactly (i). So the *shape* of the answer is forced: **a global E = 0 skeleton (the
diagonals, exact) plus a local one-variable placement on each diagonal (a concave
one-electron v and a per-atom amplitude a).** No form that omits the split can be a
solution, and no form that keeps the split needs more than it. That is what
"not a global solution, but the only solution that answers the global question" cashes
out to.

## 4 · The derivation line, drawn backwards, and where Schrödinger enters

| rung | content | status |
|---|---|---|
| 0 | the observed order, 108 neutrals | held (R 1306) |
| 1 | five facets, stated without naming an element | held (FEASIBILITY) |
| 2 | concavity + monotonicity ⇒ all five | proved (FEASIBILITY §4) |
| 3 | one variable | dissolves on the diagonal (DIAGONAL §1) |
| 4 | a physical v concave in p | measured 8/8; facet 4 (5f at Rn) a published-data null |
| 5 | the amplitude a from the core alone | **the many-electron term; not one-electron** |
| 6 | Schrödinger | one electron in a screened core: threshold degeneracy at fixed n+ℓ (D-O 1972 for the focusing class); quantum defects δ_ℓ falling with ℓ with diminishing increments (Seaton) — the shape rung 4 measures |

Rungs 6 → 4 → 2 → 1 → 0 form an unbroken one-electron line to *every admissible order
on each diagonal*. Rung 5 selects the observed one and is not on that line — and that
is the finding, not a hole in it: the global question's answer *includes* that the
selection is local. Lr's 7p over 6d is attributed in the field to relativistic 7p₁/₂
stabilisation (unsourced here, bridge §9.7); if that holds, the one forced clique member
at Lr lies outside non-relativistic Schrödinger, and the challenge as posed cannot reach
it in principle.

## 5 · New today — the amplitude is windowed by measurement (`windows.py`)

Corridors are partition cells, so each measured core bounds a at every step on its
diagonal. Cs I reproduces the bridge's 0.411 / 0.887 / 2.18 (gate). New:

| core | member | cell for a |
|---|---|---|
| Xe (Cs I, M=7) | 4f · 5d · 6p · 7s | (0, .411) · (.411, .887) · (.887, 2.18) · (2.18, ∞) |
| Xe (Ba II) | 4f · 5d · 6p · 7s | (0, .603) · (.603, 1.21) · (1.21, 2.80) · (2.80, ∞) |
| Kr (Rb I, M=6) | 4d · 5p · 6s | (0, .754) · (.754, 2.09) · (2.09, ∞) |
| Rn (Fr I, M=8) | 5f · 6d · 7p · 8s | (0, ?) · (?, **.854**) · (**.854, 2.10**) · (2.10, ∞) |

So on measured data: La (5d) sits in (0.41, 0.89) and Ce (4f) below 0.41 — a falls
along the period as the diagonal fills; **Ac, Th, Cm (6d) require a < 0.854 and Lr (7p)
requires 0.854 < a < 2.10** — Lr's amplitude lies above the actinide d entrants'. These
are constraints on rung 5 from the core alone, held out from the entrant, and they can
fail: an a-law that violates any cell is refuted. The 5f lower bound is the facet-4 null
(no Fr I f channel published; Ra II nf is the minimal fetch, FACET5 §4).

## 6 · What can still fail

- Facet 4 at the Rn core (published-data null; Ra II).
- The Lr attribution (relativistic 7p₁/₂) — source before registering.
- Piercing number exactly 3 on the concave sub-cone — measured 5,000/5,000, unproved.
- Any proposed a-law against §5's cells, and against R 1583's held-out 92.

## 7 · Owed to the writing chat (in addition to bridge §8's R 1703–1709)

- **R 1710** — the decomposition as the answer's forced shape: global E = 0 skeleton
  + local one-variable placement; why no form without the split can answer, and none
  with it needs more (§3).
- **R 1711** — corridors on a concave diagonal are partition cells; the amplitude windows
  of §5; Cs I gate reproduced; Lr's a above Ac/Th/Cm's on Fr I data.
- Chapter: `CHAPTER-LOWDIN.md` §8 to be rewritten to this statement (three findings
  behind at the last bridge).
