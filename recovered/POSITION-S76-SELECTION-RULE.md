# POSITION S76 — THE SCF SELECTION RULE. STEP 0(ii).
# M's ruling s76 item 2: identify and derive the selection rule; check prior art first.
# THIS IS A POSITION, NOT A RULING AND NOT A RESULT.

## 1 · THE PROBLEM IS NAMED IN THE LITERATURE, IN THE LITERATURE'S OWN WORDS.
Griesemer & Hantsch, arXiv:1012.5179 §1, on the state of the field:
  * SCF algorithms (Roothaan, level-shift) are what is actually run;
  * convergence analysis has advanced, **but it is still poorly understood WHAT IS
    BEING APPROXIMATED**;
  * the HF functional for a NEUTRAL ATOM has a minimiser **and infinitely many other
    critical points**;
  * uniqueness of the minimiser is not known even where it is expected;
  * **it is not known whether distinct methods for finding critical points lead to
    distinct critical points.**
**THAT IS STEP 0(ii) VERBATIM, POSED BY THE FIELD AND OPEN THERE. We are not
discovering a private difficulty and we must not report it as one.**

## 2 · THE PRIOR ART THAT SUPPLIES THE SHAPE OF A RULE.
**Lieb's variational principle (relaxation from projections to 0 <= gamma <= 1)** is
the standard device: the infimum over the relaxed convex set equals the infimum over
rank-N projections, so the minimiser is characterised VARIATIONALLY rather than by
whatever the algorithm converges to. Review: V. Bach, "Hartree-Fock Theory, Lieb's
Variational Principle, and their Generalizations", arXiv:2209.10189.
**THE RESTRICTED ANALOGUE IS ALREADY IN OUR HAND AND IS THE ONE THAT APPLIES.**
Hantsch arXiv:1206.4932 Remark (c) to (6): the orthonormality constraints may be
relaxed to <f_i,f_j> = 0 for l_i = l_j, i != j and ||f_i|| <= 1 **WITHOUT LOWERING
THE GROUND STATE ENERGY** — E(N,Z) = Etilde(N,Z) — and Theorem 2.1 produces a
minimiser of the relaxed problem, which at Z > N-1 is normalised with every
eps_i < 0. **The relaxed problem has a minimiser; the relaxation is free.**

## 3 · THE RULE PROPOSED, IN THE FORM STEP 0 REQUIRES.
> **SELECTION RULE (PROPOSED).** For each Z and each candidate channel, the field is
> defined to be **a global minimiser of the restricted Hartree-Fock functional
> E^RHF at the fixed shell occupancies of that candidate**, over the relaxed set of
> Hantsch (8). Existence: Hantsch Theorem 2.1. Every scored row satisfies Z > N-1,
> so the minimiser is normalised with all shell eigenvalues strictly bound.
**WHAT THIS BUYS:** Φ is then defined by a VARIATIONAL PROPERTY, not by a trajectory.
**(beta, maxit) LEAVES THE DEFINITION ENTIRELY** and becomes what it always was — a
numerical scheme for approaching an independently defined object. That is exactly
what Step 0 asked for.
**WHAT IT DOES NOT BUY:** it does not make the minimiser unique. It does not have to.
A selection rule needs to name ONE object, not prove there is only one candidate.

## 4 · THE OBLIGATION THIS CREATES, AND IT IS A REAL ONE.
Defining Φ by the global minimiser transfers the burden to the code:
**THE PROGRAM MUST BE SHOWN TO REACH THE GLOBAL MINIMISER AND NOT A SADDLE OR A
LOCAL ONE.** Convergence theorems (Cances & Le Bris M2AN 34 (2000) 749; Levitt M2AN
46 (2012) 1321) deliver A CRITICAL POINT ONLY. **This obligation belongs to ROUTE C
and it is now load-bearing there, where before it was not named.**
**EVIDENCE WE ALREADY HOLD, AND ITS EXACT WEIGHT:** the seed study — TFD, Latter,
alpha = 2/3 — agrees to **0.005 mHa from 52 Ha away**. That is a THREE-START BASIN
TEST and it is the right kind of evidence. **THREE STARTS IS NOT A PROOF OF A GLOBAL
MINIMUM AND MUST NOT BE QUOTED AS ONE.** The falsifier is cheap and is not yet run:
perturb the converged solution and re-converge; a second basin at lower energy kills
the rule as stated.

## 5 · A WARNING CARRIED FROM THE READING.
Lions' treatment of the RESTRICTED equations relies on the unproven assertion that
all eigenvalues of a radial Fock operator are simple. **We do not import it.** Our
rule is stated on the ENERGY, not on the spectrum, precisely to avoid needing it.

## 6 · STATUS
IDENTIFIED and DRAFTED. **NOT DERIVED and NOT ADOPTED.** Awaiting M.
Open beneath it: whether "global minimiser at fixed occupancies" is well posed when
two occupancies are compared — that is Step 0(iii), measured separately.