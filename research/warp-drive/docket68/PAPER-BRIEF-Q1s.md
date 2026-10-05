# Brief for a separate session: a professional paper on signed and complex entropy (DOCKET 68, Q-1s)

M, 2026-10-03, verbatim: *"if this does prove useful, we should set up instructions for a new separate session to write
a professional paper about the complex and negative entropy findings"*. This file is those instructions. It is
self-contained: a fresh session should need nothing else to start.

## Condition (M, 2026-10-04, verbatim)

> The paper is not a priority, just an additional if the math concept is novel or introduces new theorems/proofs not
> otherwise previously published art

So the session's first task, section 3 step 1 (the prior-art search), is also the gate. If that search finds that every
item in section 2 is already published, the session reports this to M and writes no paper.

## 0. Where everything is

- Repository `lach-matt/claude-method-works`; the work is on branch `claude/warp-drive-theory-ditjk4`. Create a new
  branch from it for the paper (e.g. `claude/signed-entropy-paper`) unless M names one.
- The instrument that owns every number: `research/warp-drive/docket68/signed.py` (stdlib + numpy/sympy/z3;
  `python3 signed.py --selftest`: 120 counted checks, 26 controls, 15 STRUCTURAL printed and not counted).
- The write-up with derivations, sources and history: `research/warp-drive/docket68/Q1s-signed.md` (sections 1–10,
  "Discrepancies and history", "Named hypotheses", "OPEN"). Read it in full first.
- Its use in a measure of information: `docket68/measure.py` (Q-1, which imports signed.py).
- M's words and rulings: `docket68/CHARTER.md` (the last sections) and `docket68/M-RULINGS-2026-10-03.md`.
- Install z3 with `pip install z3-solver` (pypi is reachable; github is not).

## 1. Rules that bind the paper (M's, standing)

- Every claim accurate, true and shown: computed by an instrument in the repository, or READ at source with id,
  version and page. Nothing declared. A claim that cannot be checked is stated as OPEN.
- Every limitation is a named hypothesis. Over-representation is avoided in both directions: no novelty claimed that
  the literature already holds, and no result undersold.
- arXiv versions are the object (M-D67-2): cite the version read. A host that refuses (403) is reported, never routed
  around. Quote at most short phrases with page numbers; copyrighted text stays out of git.
- The paper reads the research tree and never writes to it. Any new computation goes in a new instrument beside the
  paper, importing `signed.py`, never copying it. Do not edit `research/warp-drive/paper/CLAIMS.md` (M's finalised
  paper) or anything under `drive/` or `method/`.
- When M must decide something, ask and pause for the answer.

## 2. Is it useful? The lead's assessment, for M to weigh

Useful, as a careful mathematical note, not as a claim of a new physical effect. The definition itself is known
(Cerf–Hertz–Van Herstraeten, arXiv 2310.19296v1, for continuous Wigner functions). The uniqueness of Re H on two
entries under signed-weight recursivity was claimed by Kontsevich in 1995 (math/0008089v1 appendix, pp.42–44, a
sketch). What the repository adds, as a floor rather than a priority claim (Q1s-signed.md §6 "Not found"):
1. The finite-set treatment: Re H, Im H = πN, the per-entry branch accounting, and the exact range of Re H for given
   (n, N). Negative Re H is forced only at n = 2; min over N of max Re H is ln(n−2); Re H has no ceiling ln n.
2. Baez–Fritz–Leinster's categorical axioms (1106.1791v3 Thm 2) restated on signed measures. The codomain [0, ∞)
   fails, with computed counterexamples. Over every continuous separable functional the axioms force c·Re H + b·N.
   With product additivity, only Re H remains; with the codomain kept, only b·N remains. The algebraic steps are
   machine-checked (z3, sympy).
3. The contrast that explains both results: N is convex-linear in BFL's sense but fails Kontsevich's signed
   recursivity, so BFL admits span{Re H, N} while Kontsevich admits Re H alone.
4. The two weightings in Brandenburger–La Mura's mean-value axiom: |w| gives signed Rényi and signed w gives Re H. They
   are separated conditionally, if BFL convex linearity binds (H-BFL-BINDS). M ruled: carry both.
5. A signed relative entropy D_s, centred at a calibrated ground state (M: mass/binding by default, from READ AME2020,
   PDG and NIST). It keeps product additivity, convex linearity and the chain rule, and fails Gibbs non-negativity and
   data processing. The ground-centred deviation is a relative entropy only when a computed cross term vanishes.
6. M's triangulation, computed: filtered back-projection recovers a signed distribution's negative region from its
   projections (IoU 1.000 at 180 angles, 0.037 at 2), with an exact discrete Wigner case. The principle is
   established (optical homodyne tomography; Lvovsky–Raymer review quant-ph/0511044v2). The paper presents it as an
   application, not a discovery.

## 3. What the session must do first, before writing a sentence of claims

1. **Finish the prior-art search** (Q1s-signed.md OPEN 4). The information-cohomology and polylogarithm literature is
   NAMED-NOT-READ: Cathelineau (1988, 1996), Baudot–Bennequin, Vigneaux, Aczél–Dhombres (1989), Lee (1964), Rényi
   (1961), Daróczy (1963). Also search for any existing work on signed or quasi-probability Shannon or Rényi entropy
   on finite sets. Re-grade items 1–4 above against what is found. **A result the literature already holds is cited,
   not claimed.**
2. Re-run `signed.py --selftest`, `measure.py --selftest` and `combine.py --selftest`. Every number in the paper is
   printed by one of them, or by a new instrument that imports them.
3. Decide with M the scope and venue: a short mathematical note (information theory / mathematical physics), or a
   longer paper including the calibrated D_s and The Method's index as an application.

## 4. Suggested structure (to be revised against the prior-art search)

1. Introduction: quasi-probabilities (Wigner functions, signed measures) and why their information content is
   ill-defined under Shannon's log. The known continuous complex Wigner entropy, and Kontsevich's equation.
2. Definitions on finite signed measures: the principal branch and the other branches, Re H, Im H = πN, M = log Σ|p|.
3. Range of Re H (the finite-set results).
4. Axiomatics: BFL on FinSigned; the separable characterisation c·Re H + b·N; product additivity; the codomain; the
   BFL-versus-recursivity contrast; the two weightings. State exactly what is proved, what is derived, and what is
   OPEN (non-separable functionals).
5. Signed relative entropy and ground-state calibration (if M includes it).
6. Reconstruction from projections (triangulation), with its controls.
7. Applications: discrete Wigner functions (the qutrit strange state, a qubit), and The Method's index under its named
   hypotheses, if M includes it.
8. Open problems: Q1s-signed.md's OPEN list, verbatim in substance, including the operational meaning of Re H once
   entries are negative (also missing in the continuous case, 2310.19296v1 p.13).

## 5. What the paper must not say

- That the complex Wigner entropy, its imaginary part as negativity, sum negativity or mana, or reconstruction
  from projections are new.
- That Re H is the unique lawful signed entropy in general. It is unique only under the stated conditions; for
  non-separable functionals under BFL's axioms it is OPEN.
- Anything about warp travel, corridors or DOCKET 68's obstruction screen. That is a separate body of work, and Q-1s
  moves no obstruction grade there.
- Any figure not printed by an instrument in the repository.

## 6. Hand-back

The session reports to M: the draft's location, the prior-art findings and how they re-graded items 1–4, every
selftest it ran, every source READ (id, version, pages), every 403 met, and every question M must rule on.

## 7. Closed (2026-10-05)

The gate ran (Q1s-PRIORART.md), and M ruled **"No paper"** (M-RULINGS item 43). This brief is kept as a record. It is no
longer an instruction for a session.
