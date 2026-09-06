# FINDING S76 — STEP 0(i)–(iii). THE MATHEMATICAL STATUS OF Φ.
# Session 76. Fetch/read step only. NOTHING BELOW IS A RULING.
# No sealed file edited. c = 137.035999 unchanged. 107 rows, Z=2..108.

## WHAT WAS ASKED
PLAN-PROOF-ROUTES.md STEP 0: make Φ a mathematical object.
  (i)   existence of the HF minimiser
  (ii)  SCF fixed point — uniqueness or a stated selection rule
  (iii) uniqueness of the argmin

## F76.1 · THE PLAN NAMED THE WRONG THEOREM FOR THE ANSATZ Φ USES.
SEVERITY: RECORD-AND-CORRECT. TOUCHES NO SCORED ROW. RAISED BY ME, AT FETCH.
The plan asserts "Lieb-Simon 1977: minimisers exist for N <= Z", carried as the
authority for Step 0(i). **Lieb-Simon 1977 is GENERAL Hartree-Fock (GHF): no
constraint but orthonormality, condition Z > N-1.** Φ's §3 ansatz is NOT GHF. It
fixes one radial function per (n,l) channel, spherical harmonics, spin factorised:
    phi_{jm,sigma} = (f_j(r)/r) Y_{l_j m} delta_{sigma,mu}
That is the RESTRICTED (RHF) functional. **The gap is stated in the literature in
so many words:** Lieb and Simon extend GHF to certain restricted cases in
J. Chem. Phys. 61 (1974) 735, "but their theorem does not cover the restrictions
discussed in this paper" (Hantsch, arXiv:1206.4932, §1).
**CITING LIEB-SIMON FOR Φ WOULD HAVE BEEN AN AUDIT BY NAME — R-A's own fault
shape, applied to a citation instead of a lever.**

## STEP 0(i) — EXISTENCE. SETTLED, AND BY A STRONGER THEOREM THAN THE ONE PLANNED.
**F. Hantsch, "Existence of Minimizers in Restricted Hartree-Fock Theory",
arXiv:1206.4932, Theorem 2.1.** OPEN ACCESS, PRIMARY, READ IN FULL THIS SESSION.
Its RHF functional (5) is built from orbitals of exactly Φ's form (3), with
prescribed angular momentum quantum numbers l_1..l_s0.
  * A minimiser exists for the relaxed problem for ALL Z > 0.
  * (ii) If Z >= N-1, then ||f_i|| = 1 for every shell.
  * (iii) If Z > N-1, then additionally eps_i < 0 for every shell.
**EVERY SCORED ROW IS A NEUTRAL ATOM, N = Z, hence Z = N > N-1 STRICTLY.** All 107
rows sit inside case (iii) — normalised minimiser, all shell eigenvalues bound.
Not on the boundary; not in the open case Z = N-1.

## AND AN INDEPENDENT WITNESS TO §3 THAT WE DID NOT HAVE.
Hantsch §4 derives the RHF functional from the GHF functional and obtains the
exchange kernel
    U_{l l'}(r,s) = SUM_k (l l' k; 000)^2 * min{r,s}^k / max{r,s}^{k+1}
**This is §3's c_k = (l_a k l_b; 000)^2 and Y^k_ab, in a published derivation that
has never seen this project.** §3's DERIVED label on the Euler-Lagrange equations
and the angular coefficients now has an external, primary witness. The radial Fock
operator of his (7), H_l = -d^2/dr^2 + l(l+1)/r^2 - Z/r + 2U - K_l, is §3's
operator. **This is the first time an outside source has independently written down
the object Φ solves.**

## STEP 0(ii) — SCF FIXED POINT. UNIQUENESS IS NOT AVAILABLE. A SELECTION RULE IS
## REQUIRED, AND THE LITERATURE FORBIDS ASSUMING OTHERWISE.
  * **P.-L. Lions, CMP 109 (1987) 33-97:** there exists a SEQUENCE of solutions to
    the HF equations. Critical points are not unique in general.
  * **Griesemer & Hantsch, ARMA 203 (2012) 883-900 (arXiv:1012.5179):** the HF
    ground state of a CLOSED SHELL atom is unique provided Z is sufficiently large
    COMPARED TO N — for two electrons, Z >= 35. **They give an example showing
    Z > N-1 is NOT sufficient in general, and report phase segregation at some
    Z > 1.**
**CONSEQUENCE FOR US, STATED AGAINST US: our rows are neutral (Z = N), which is the
OPPOSITE of the Z >> N regime where uniqueness is proved, and most of them are open
shell, which is outside the closed-shell hypothesis entirely. STEP 0(ii) CANNOT BE
CLOSED BY UNIQUENESS. It must be closed by a STATED SELECTION RULE.**
The convergence ladder (beta, maxit) is today a numerical control. Relevant prior
art for what it is: Cances & Le Bris, M2AN 34 (2000) 749-774, convergence of SCF
algorithms; Levitt, M2AN 46 (2012) 1321-1336, gradient-based algorithms. These
prove convergence TO A CRITICAL POINT. **They do not say WHICH.**

## STEP 0(iii) — UNIQUENESS OF THE ARGMIN. TWO SEPARATE OBJECTS, DO NOT CONFLATE.
  * **The aufbau principle as a theorem exists — in the WRONG theory.** Bach, Lieb,
    Loss & Solovej, PRL 72 (1994) 2981, "There Are No Unfilled Shells in Unrestricted
    Hartree-Fock Theory": occupied orbitals are the N lowest eigenvalues of the Fock
    operator, with a gap to the unoccupied. **Hantsch's Remark (b) to Thm 2.1 records
    that it is NOT KNOWN whether this holds in RESTRICTED HF, and that the method of
    that proof is not applicable there.** The nearest mathematical form of "the
    aufbau principle" is a theorem in UHF and OPEN in the theory Φ inhabits.
  * **BUT Φ DOES NOT SELECT BY EIGENVALUE ORDER.** §3 step 3 selects the argmin of a
    TOTAL-ENERGY difference over admissible channels. The BLLS gap theorem is
    therefore not the lemma Φ needs, and the open RHF question is not a hole beneath
    Φ. **Φ's requirement is weaker and finite: at each Z, that the argmin over a
    finite candidate set is attained once.** That is decidable row by row and is
    MEASURABLE — it is the margin column we already own.
  * NOTED AGAINST US: Lions' treatment of the restricted equations rests on the
    unproven assertion that all eigenvalues of a radial Fock operator are simple.
    **We must not import that assertion.**

## WHAT IS NOW OPEN AT STEP 0, PRECISELY
  A. A written selection rule for the SCF fixed point, replacing (beta, maxit) as a
     numerical control. NOT closed by uniqueness; uniqueness is false in our regime.
  B. Uniqueness of the argmin at all 107 rows — the min gap between winner and
     runner-up, measured, not recalled. NOT YET RUN THIS SESSION.
  C. Whether the candidate set of §3 step 1 is a definable object independent of the
     program. Route A already flags the truncation as sampled, not proved.

## PROVENANCE
arXiv:1206.4932 fetched and read in full. arXiv:1012.5179 abstract + intro read.
**Project Euclid (CMP 53, 185-194) was NOT reachable: blocked by bot protection,
NOT a paywall. Lieb-Simon 1977 remains UNREAD IN PRIMARY FORM by this project and
must be labelled [SECONDARY] exactly as A1 is — but it is no longer load-bearing,
because Hantsch Thm 2.1 replaces it.**