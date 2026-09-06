# PREDICTION — L2: THE FINITE NUCLEUS. THE LAST UNBOUNDED LINK.
# FILED SESSION 64, BEFORE ANY SOLVE OF THIS TEST WAS RUN AND BEFORE THE Z=120 CHAIN
# ROW WAS LOOKED AT. R 1449 / §2.13. Scored only after this file's sha is verified.

## WHAT L2 IS
`ASSEMBLY-RUNG-0.md` L2: Born-Oppenheimer, POINT NUCLEUS, INFINITE NUCLEAR MASS.
Classified APPROXIMATION, UNBOUNDED HERE. It is the only one of the twelve links
carrying no number. This file predicts the number before it is measured.

## THE THREE ATOMS, AND WHY THESE THREE AND NOT OTHERS
The two halves of L2 run in OPPOSITE directions in Z, so bounding both ends bounds
everything between and no further row need ever be run:

  * **FINITE SIZE grows steeply with Z** (as Z x R^2 x density-at-the-nucleus, and
    R itself grows as A^(1/3)). It is largest at the heaviest row.
  * **FINITE MASS shrinks with Z** (as m/M ~ 1/1836A). It is largest at the lightest.

    Z=3    Li, A=7        the LIGHTEST row where the walk makes a decision.
                          Maximum mass effect anywhere in the chain. Cheap.
    Z=89   Ac, A=227      the TIGHTEST MARGIN in the entire chain, 32.33 mHa, and a
                          first-entry row the central claim rests on. The worst case
                          for a decision being flipped by anything at all.
    Z=120  A~295          the HEAVIEST row walked. Maximum size effect anywhere.

**MONOTONICITY IS THE WHOLE POINT OF THIS CHOICE.** A pass at Z=3 for mass and at
Z=120 for size bounds every row between them, because neither effect has a maximum
in the interior. If this is right, L2 closes in one session and is never reopened.

## THE INSTRUMENT, AND THAT IT EDITS NOTHING
First-order perturbation on the CONVERGED orbitals of the sealed field:
    dE = sum_a q_a INT P_a(r)^2 [V_finite(r) - V_point(r)] dr
    V_finite = -(Z/2R)(3 - r^2/R^2) for r < R,  -Z/r for r >= R   (uniform sphere)
    R = 1.2 A^(1/3) fm = 1.2 A^(1/3) x 1.8897e-5 bohr
Evaluated on the solver's own mesh from `h.P`, `h.r`, `h.dr` after `run2()`. **No
sealed file is edited, no potential is re-derived, no SCF is modified.** The integral
form is used rather than the textbook |psi(0)|^2 x (2pi/5)ZR^2 because the scalar-
relativistic P diverges mildly at the origin (P ~ r^gamma, gamma = sqrt(1-(Z/c)^2) =
0.76 at Z=89) and the density-at-a-point form is not defined there. The integral is.

## WHAT IS PREDICTED — FINITE SIZE

**S1. THE SHIFT ON A SINGLE CONFIGURATION IS LARGE.** Not small, not negligible:
predicted **dE of order 1 Ha at Z=89** (range 0.3 to 3 Ha) and **larger still at
Z=120**, dominated almost entirely by the 1s pair, with 2s next and every l>0 orbital
contributing essentially nothing.
FALSIFIER: dE below 0.01 Ha at Z=89 -> the mesh does not resolve r < R and the whole
measurement is void, NOT a pass. **This is the prediction that guards the method.**

**S2. IT CANCELS IN THE DECISION, WHICH IS THE ONLY THING THE WALK USES.**
D(c) is a difference of two energies at the same nuclear charge, and the differentiating
electron at Z=89 and Z=120 is a d or f electron with no density at the nucleus. The
shift enters only through core relaxation.
    PREDICTED  |dD| = |dE(cfg+c) - dE(cfg)| < 0.05 mHa at BOTH rows, for BOTH the
               entrant and the runner-up
    PREDICTED  |dD| / dE < 1e-4 -- a cancellation of four orders or better
    PREDICTED  the entrant is UNCHANGED at both rows
FALSIFIER, and it is the one that matters: |dD| at or above the 0.05 mHa floor -> **L2
is not negligible, the assembly must carry it as a stated cost, and every margin
quoted anywhere in the project must be re-read against it.**
FALSIFIER, worse: |dD| above the row's margin -> the finite nucleus CHANGES THE
DERIVED FILLING ORDER and the result must be reported first, before anything else.

## WHAT IS PREDICTED — FINITE MASS

**M1. THE NORMAL MASS SHIFT CANNOT CHANGE ANY DECISION, AND THIS IS EXACT.**
Replacing m by the reduced mass mu = mM/(m+M) scales the whole non-relativistic
Coulomb Hamiltonian: every energy by mu/m, every length by m/mu. **Every channel
depth scales by the same factor, so every margin scales by the same factor, and the
argmin is invariant identically -- not to within a bound, exactly.**
    PREDICTED  numerical verification: D at Z=3 recomputed at mu/m differs from the
               sealed D by the ratio mu/m to within numerical noise, for every channel
    m/M at Z=3, A=7:  7.81e-5   ->  on D ~ 0.2 Ha, a shift of ~0.016 mHa
FALSIFIER: channels scaling by different factors -> the scaling argument is wrong and
the mass half must be measured row by row rather than argued.

**M2. THE SPECIFIC MASS SHIFT IS NOT COMPUTABLE ON THIS INSTRUMENT AND IS BOUNDED,
NOT MEASURED.** The mass-polarisation operator (1/M) sum_{i<j} p_i . p_j is a genuine
two-electron term this field does not carry. It does NOT scale uniformly.
    PREDICTED BOUND  |dD_SMS| <~ (m/M) |D|, i.e. **0.016 mHa at Z=3** and smaller at
                     every heavier row, since m/M falls faster than |D| rises
This is an order-of-magnitude bound and is declared as one. **If M wants SMS measured
rather than bounded it is a separate instrument and a separate session, and this file
says so now rather than letting a bound be read as a measurement later.**

## WHAT A PASS BUYS, STATED SO IT CANNOT BE OVERCLAIMED
A pass moves L2 from OPEN, UNBOUNDED to BOUNDED, WITH THE BOUND STATED, and the
ledger of `ASSEMBLY-RUNG-0.md` §5 then carries a number on every one of its twelve
links. It does not make the nucleus finite in the walk; the walk still runs on a point
nucleus. It bounds what that costs the answer, which is what every other approximation
in this chain is held to.
