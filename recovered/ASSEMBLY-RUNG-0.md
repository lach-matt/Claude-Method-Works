# RUNG 0 — THE REVERSE CHAIN
# FROM THE EXACT MANY-ELECTRON SCHRODINGER EQUATION TO `nlchain.step`
# Löwdin Project, Session 63. The deliverable of Challenge criterion 1.
# Every link carries a line-level receipt into the sealed runtime.
# The only number ever entered into this chain is c = 137.035999.

---

## 0 · WHAT THIS DOCUMENT IS, AND WHAT IT IS NOT

The 1969 Löwdin Challenge asks for a derivation of the Madelung n+l rule from the
Schrödinger equation. Sixty-two sessions of this project built and tested a
parameter-free scalar-relativistic Hartree-Fock walk that reproduces the filling
order. **Until this document, the walk existed and the derivation did not.** A
working program is not a derivation; it is an artefact that a derivation must
account for. This is that accounting, written in reverse: from the object that
produces the answer, back to the equation it is supposed to have come from,
naming at every link what was assumed, what was derived, and what it cost.

It is a bridge, not a proof of the rule as a theorem. The distinction is kept
throughout and it is the honest one: **what is derived here is that the ordering
follows from the field, not that the ordering follows from an inequality on n and
l that can be written down without solving anything.**

---

## 1 · THE CHAIN, LINK BY LINK, IN REVERSE

### L12 · `nlchain.main` — THE WALK
    cfg(1) = 1s;  cfg(Z) = cfg(Z-1) + argmin_c D(c)
`nlchain.py:132-137`. Each configuration is built from the chain's own previous
choice. Nothing is read from `ground.py` except a comparison column that enters no
computation (`nlchain.py:88-96`). The walk runs to Z=120, past Z=108 where any
measured configuration ceases to exist.
**CLASSIFICATION: the construction under test.** Its output is the periodic table.

### L11 · `nlchain.candidates` — THE CANDIDATE SPACE
    occ(c) < 2(2l+1),  n <= N+1,  0 <= l <= min(n-1,4),  N = max n occupied
`nlchain.py:41-49`. The Pauli capacity 2(2l+1) is derived: 2 spin states times
(2l+1) magnetic substates, both of which follow from the angular momentum algebra
of the Schrödinger equation, not from the periodic table.
**CLASSIFICATION: TRUNCATION, defended as a boundary argument (Rung 9, s62).**
The closest excluded channel lies 0.08664 Ha above the winner at Z=19 and 0.15674
Ha at Z=39 — wider at the heavier row — and the excluded region recedes
monotonically in l at fixed n. **COST, STATED: the `order` column is not a complete
ordering of all channels.** At Z=19 the excluded 5s binds at -0.06110, below the
in-space 3d at -0.05807. The entrant is untouched (5s loses by 87 mHa) but this
document may not be read as ranking every conceivable channel. It resolves the
WINNER within a bounded candidate space.

### L10 · `nlchain.step` — THE ENTRANT CRITERION
    D(c) = E_HF(cfg(Z-1)+c ; nuclear charge Z) - E_HF(cfg(Z-1) ; nuclear charge Z)
    entrant = argmin_c D(c)
`nlchain.py:65-84`. **Both terms are evaluated at nuclear charge Z** (F40.1): the
reference is the cation of element Z carrying Z-1 electrons, not the neutral atom
of element Z-1. Built the other way, D is a difference between two different atoms
and not a binding energy at all. This is the single most load-bearing convention in
the walk and it was a registered fault before it was a convention.
**CLASSIFICATION: DERIVED.** D is the binding energy of the differentiating
electron; argmin is the variational statement that it occupies the channel in which
it binds most strongly. No rule about n or l enters here.
**THIS LINK ANSWERS CHALLENGE CRITERION 2, THE FILLING AMBIGUITY, EXPLICITLY:**
the walk governs **the differentiating electron**, not the simultaneous ground-state
filling of all electrons. It answers "where does the next electron go", and it
answers it at fixed nuclear charge. Every claim below is a claim about that
quantity and about nothing else.

### L9 · `hfc2.HFC.run2` — THE TOTAL ENERGY
    E = 1/2 sum_a q_a (eps_a + I_a),   I_a = eps_a - <V_a> + <P_a|X_a>
`hfc2.py:66-78`. Standard Hartree-Fock total energy from converged orbitals.
`CORR=False` on the ruling path (`nlchain.py:17`), so the correlation term E_c is
identically zero and `corr_pot` returns zeros (`hfc2.py:41`).
**CLASSIFICATION: DERIVED (Rung 6 closed s60).** Correlation is OFF, by declaration,
and the solution is claimed at the Hartree-Fock level and not above it.

### L8 · THE SCF ITERATION AND ITS GUARD
`hfc2.py:41-65`, `nlguard.run_guarded`. Fixed-point iteration with linear damping
beta, LADDER = [(0.4,100), (0.2,600), (0.1,1200)], the ruling parameters tried
first so every already-sealed converged number reproduces bit-for-bit.
**CLASSIFICATION: NUMERICAL CONTROL, BOUNDED.** beta is a damping, not a term in
the Hamiltonian: it changes the path to the fixed point and cannot change the fixed
point. That is an argument, so it was measured — at (Z=56,+5d), beta=0.4/maxit=100
and beta=0.2/maxit=600 converge to -0.11818 and -0.11818.
**COST, STATED (F47.3): a guarded D carries ~1e-5 Ha of rung-mixing in its last
stored digit**, four orders below the margins the chain decides on.
**A channel that converges at no rung returns NO NUMBER and joins `fail`.** The
guard may not return a last iterate; that is the defect it exists to repair.

### L7 · THE SEED, AND THE FACT THAT IT IS FORGOTTEN
`t7b_hf.HF.seed` -> `t5_scf.scf_occ`: a Thomas-Fermi-Dirac starting potential with
a Latter tail min(V, -qtail/r) and a Gaspar-Kohn-Sham alpha=2/3 exchange form.
**THESE ARE THE ONLY NON-DERIVED FORMS ANYWHERE IN THE CHAIN, AND THEY DO NOT
SURVIVE CONVERGENCE.** Measured (Rung 3/4, s61):

    seed A  TFD, qtail=1        seed B  TFD, qtail=6        seed C  bare -Z/r
    starting eigenvalues differ by up to 51.95 Ha
    converged total energy differs by 0.005-0.010 mHa

A 52 Ha disagreement at the starting point converges to an 8 microhartree
disagreement in the answer. Seed C carries no TFD, no Latter clamp, no exchange, no
screening and no chosen constant, and it returns the sealed entrant at every row
where it converges.
**CLASSIFICATION: SEED-ONLY, MEASURED NOT ASSUMED. The chain does not inherit them.**
**COST, STATED: a worse seed costs CHANNELS, not accuracy.** nfail rises 0->2 at
Z=19 and 1->6 at Z=20; at Z=20 the casualty was the runner-up. The winner survived
every seed at all three rows tested — **that is an observation at three rows and
not a theorem.** A seed that killed a winner would change the entrant.

### L6 · `t7c_kernel.qlog` — THE SCALAR-RELATIVISTIC OPERATOR
    P'' = [l(l+1)/r^2 + 2M(V-E)]P + (M'/M)(P' - P/r),   M = 1 + (E-V)/2c^2
    P = M^{1/2} F  =>  F'' = QF,  Q = l(l+1)/r^2 + 2M(V-E) - M'/(rM) - M''/2M + 3M'^2/4M^2
Koelling & Harmon 1977: mass-velocity and Darwin terms, no spin-orbit.
**THIS IS THE ONE PLACE THE CHAIN GOES BEYOND WHAT THE CHALLENGE ASKS.** Criterion
3 says begin from the exact NON-RELATIVISTIC many-electron Schrödinger equation.
The defence is threefold and each part is checkable:
  (i) **c -> infinity returns the non-relativistic kernel term for term, identically**
      — every extra term above carries 1/c^2 and vanishes. Gated at c=1e6.
  (ii) **c = 137.035999 is CODATA, a measured property of the vacuum, not a fitted
      parameter.** It is the only number entered into this project.
  (iii) Relativity was tested against the orderings and does not create them
      (Rung 1, s60).
**CLASSIFICATION: PHYSICALLY FIXED EXTENSION with an exact non-relativistic limit.**

### L5 · `hfc2.run2` inner loop — THE RADIAL HARTREE-FOCK EQUATIONS
    [-1/2 d^2/dr^2 + l(l+1)/2r^2 + V_a] P_a - X_a = eps_a P_a
    V_a = -Z/r + sum_b (q_b - delta_ab) Y^0_bb / r
    X_a = sum_{b!=a} (q_b/2) sum_k c_k(l_a,l_b) Y^k_ab/r P_b
          + within-shell part, local, folded into V_a
    c_k = (l_a k l_b; 0 0 0)^2,   w = (2l+1)/(4l+1)
`hfc2.py:45-56`, `t7b_hf.py:18-23` (`_c3j0sq`, the 3j symbol computed from
factorials, no table).
**CLASSIFICATION: DERIVED.** These are the Euler-Lagrange equations of the
determinantal expectation value; the c_k are Wigner 3j symbols from the angular
integration, computed and not looked up.

### L5a · `_ceff` — THE SELF-INTERACTION COEFFICIENT, THE SHARPEST TEST IN THE LEDGER
    _ceff(a,Q) = Q[a] - 1.0                                   (`t7b_hf.py:105`)
An electron in shell a sees the other q_a - 1 electrons of its own shell and all
q_b of every other: the exact removal of self-interaction from the determinant.
No coefficient to fit.
**FALSIFIER, MEASURED (Rung 5, s62 — and reproduced this session):** at q=1 it
returns exactly 0.0, so a one-electron atom must carry no Hartree self-repulsion.

    Z=1, the walk's own solver     E = -0.5000080791 Ha
    exact non-relativistic hydrogen    -0.5
    the whole miss                     -8.08 microhartree
    analytic leading SR correction     -6.66 microhartree

**The walk reproduces the exact hydrogen ground state, and the entire amount by
which it misses is the relativistic correction the field is supposed to carry.**
Had `_ceff` returned Q[a] or any screening value, Z=1 would carry a spurious
self-repulsion of order 0.3 Ha, and no parameter exists that could hide it.
**CLASSIFICATION: DERIVED. There is no fitted quantity at this link.**

### L4 · THE AVERAGE-OF-CONFIGURATION RESTRICTION
The determinant is averaged over m_l and m_s within each shell, leaving shell
occupations q_{nl} and reducing the angular integrals to the c_k above.
**CLASSIFICATION: APPROXIMATION. BOUNDED AT L4a BELOW (Rung 2).**

### L3 · THE SINGLE-DETERMINANT (HARTREE-FOCK) ANSATZ
Psi -> one Slater determinant of spin-orbitals psi_i = (P_nl(r)/r) Y_lm(theta,phi) chi_s.
This is the variational restriction and it is the largest single assumption in the
chain. **CLASSIFICATION: APPROXIMATION. BOUNDED AT L4a BELOW (Rung 2).**

### L2 · BORN-OPPENHEIMER, POINT NUCLEUS, INFINITE NUCLEAR MASS
The -Z/r in every V_a. **CLASSIFICATION: APPROXIMATION, UNBOUNDED HERE.** Finite
nuclear size and mass are not modelled. Both are far below every margin the chain
decides on at the Z where the chain decides them, but this document does not
measure that and does not claim it.

### L1 · THE EXACT MANY-ELECTRON SCHRODINGER EQUATION
    H = sum_i (-1/2 grad_i^2) - sum_i Z/r_i + sum_{i<j} 1/r_ij,   H Psi = E Psi
    Psi antisymmetric under exchange of any two electrons.
**THE ORIGIN. Nothing above it.** Every term in L5 descends from a term here: the
kinetic operator to -1/2 d^2/dr^2 + l(l+1)/2r^2, the nuclear attraction to -Z/r,
and the electron repulsion — and this is the whole of the matter — to the direct
Y^0 and the exchange X.

---

## 2 · WHAT THE CHAIN PRODUCES, SCORED AGAINST A PREDICTION FILED BEFORE IT WAS READ

`pack63/PREDICTION-RUNG-0-ASSEMBLY.md`, sha256 cdc0d2b129d398fb…, filed
18:12:13Z; first chain row read 18:12:36Z. Scorer `pack63/asm0.py`, can-failed in
two directions before use.

### THE PERIOD LENGTHS — **DERIVED. CHALLENGE CRITERION 2.**
Defining a new period as the first entry of an ns channel with n greater than any
previously entered — a definition applied to the chain's own entrant column, with
`ground.py` never consulted —

    period starts   Z = 1, 3, 11, 19, 37, 55, 87, 119
    period lengths  **2, 8, 8, 18, 18, 32, 32**

This is the exact sequence the Challenge names, and it was predicted before the
column was read. **`nlchain.py` contains no notion of a period anywhere**; no shell
capacity sequence is imposed, no boundary is defined. The lengths are an output.
CONTROL: forcing a single s-channel change at Z=19 returns 2,8,8,36,32,32. The
result is not vacuous.

### THE ORDERING CLAUSE OF MADELUNG — **DERIVED. ZERO INVERSIONS IN 119 ROWS.**
Ordering channels by the Z at which each is first entered, **n+l is non-decreasing
along the entire sequence.** Zero exceptions. The scorer goes red on an injected
inversion.

### THE TIE-BREAK CLAUSE — **HOLDS TO n+l = 6. FAILS AT n+l = 7 AND 8, AND THE
### FAILURE IS CORRECT PHYSICS. THIS IS THE MOST IMPORTANT RESULT IN THE DOCUMENT.**
The prediction asserted the textbook string and it was wrong:

    predicted  1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **4f 5d** 6p 7s **5f 6d** 7p 8s
    derived    1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **5d 4f** 6p 7s **6d 5f** 7p 8s

The chain enters 5d before 4f, and 6d before 5f. Madelung's tie-break says the
lower n comes first and would have 4f before 5d. **The walk disagrees with the rule
at exactly two places, and at both of them the walk agrees with measurement:**

    5d first entered at Z=57   La   observed differentiating electron 5d   ok=True
    4f first entered at Z=58   Ce   observed 4f                            ok=True
    6d first entered at Z=89   Ac   observed 6d                            ok=True
    5f first entered at Z=91   Pa   observed 5f                            ok=True

La and Ac are among the best-known failures of the Madelung rule in the measured
periodic table. **The derivation reproduces them without being told about them.**
The tie-break holds exactly in every block the field and the rule agree on
(n+l = 3, 4, 5, 6 — the pairs 2p/3s, 3p/4s, 3d/4p/5s, 4d/5p/6s) and departs in
both blocks where nature departs. Prior sessions verified the tie-break over 26
steps and three pairs; **all three lie at n+l <= 6, so blocks 7 and 8 had never
been tested and the discipline of predicting before reading is what exposed it.**

**THE CONSEQUENT RESTATEMENT, WHICH THIS DOCUMENT ADOPTS:**
The n+l rule is TWO laws and they do not have the same standing.
  * **THE ORDERING CLAUSE IS DERIVABLE AND DERIVED.** It follows from channel
    depths at each atom and holds without exception across the whole walk.
  * **THE TIE-BREAK CLAUSE IS AN EMPIRICAL REGULARITY OF THE LIGHT BLOCKS, NOT A
    LAW.** It is a property of the filling sequence, cannot be read off any single
    atom's spectrum, holds where n+l <= 6, and is false at n+l = 7 and 8 — where
    the field is right and the rule is wrong.
This is a stronger result than reproducing Madelung, and it is a different one. It
must not be reported as "the Madelung rule is derived" without this paragraph
attached.

### THE EXCEPTIONS — **CHALLENGE CRITERION 7, ANSWERED AND BOUNDED.**
11 of 107 scored rows disagree with the observed differentiating electron:
Z = 25, 30, 43, 47, 48, 64, 71, 80, 96, 103, 104. Entrant blocks: 6 d, 5 f. Every
one is an element whose observed ground state differs from the aufbau
configuration by the promotion of an ALREADY-PLACED electron (Cr/Cu type). **A
one-electron walk has no move for a promotion of an electron it placed at an
earlier Z. The format fails at these elements; the ordering rule does not.**

---

## 3 · RUNG 2 — THE SINGLE-CONFIGURATION BOUND ON THE ORDERING. **CLOSED HERE.**

Rung 2 asks what L3 and L4 — the single determinant and the configuration average
— cost the ORDERING. It is answered with an instrument already sealed in pack53
and found by searching the archive rather than built (Standing 6): `ctrl137.jsonl`,
11 rows walked in `restart` mode, which replaces the chain's self-built reference
configuration with the OBSERVED configuration of Z-1 — the physical, multi-
configuration-influenced occupation — at c = 137.035999.

**RESULT 1 — THE ANOMALIES ARE A PROPERTY OF THE REFERENCE CONFIGURATION.**
Of the 11 chained anomalies, 8 have a restart control. **All 8 repair.**

    Z=25 3d->4s  Z=30 3d->4s  Z=47 4d->5s  Z=48 4d->5s
    Z=71 4f->5d  Z=80 5d->6s  Z=103 5f->7p  Z=104 5f->6d      8/8 now ok=True

Given the physically correct reference configuration, the field selects the
observed differentiating electron at every row tested. **The energy criterion of
L10 is not what fails at these elements. The configuration handed to it is.**

**RESULT 2 — THE SUBSTITUTION IS NOT FREE, AND THIS IS REPORTED AS COUNTER-EVIDENCE.**
Three restart rows FAIL where the chained walk SUCCEEDS: Z=60, 61, 62 (Nd, Pm, Sm)
return 5d where observation gives 4f, at margins of 30.3, 15.0 and 2.4 mHa — all
above the 0.05 mHa working floor, so all physics rather than numerics.
**The single-configuration approximation therefore cannot be bounded to zero on
individual rows. It repairs 8 and breaks 3. Its row-level effect is real and
bidirectional.**

**RESULT 3 — AND IT IS THE ONE RUNG 2 ACTUALLY TURNS ON. THE ORDERING IS IMMUNE.**

    first-entry rows  1 3 5 11 13 19 21 31 37 39 49 55 57 58 81 87 89 91 113 119
    anomaly rows      25 30 43 47 48 64 71 80 96 103 104
    INTERSECTION      EMPTY

**No anomaly is a first-entry row.** Every one occurs part-way through a block, on
an electron added to a channel already open. The period lengths, the n+l ordering
clause and the tie-break are all properties of the FIRST-ENTRY sequence, and the
single-configuration approximation does not touch a single member of it.

**RUNG 2 CLOSES AS A BOUND ON THE ORDERING AND ONLY ON THE ORDERING:** the
single-determinant, average-of-configuration restriction displaces the entrant at
11 of 107 rows, never at a row that opens a channel, and therefore changes nothing
in the derived filling order. It is NOT closed as a bound on the row-by-row
configuration, where its effect is measured above and is not small.

---

## 4 · THE CONSTANT LEDGER — CHALLENGE CRITERION 4

    c = 137.035999            PHYSICAL, CODATA. The only number entered.
    2(2l+1)                   DERIVED — spin x magnetic substates.
    q_a - 1  (`_ceff`)        DERIVED — exact self-interaction removal. Falsified
                              at q=1 against exact hydrogen to 1.4 microhartree.
    c_k = (l k l'; 000)^2     DERIVED — 3j symbols computed from factorials.
    w = (2l+1)/(4l+1)         DERIVED — Slater average energy of configuration.
    TFD / Latter / alpha=2/3  SEED-ONLY, MEASURED FORGOTTEN (0.005 mHa from 52 Ha).
    beta, maxit, tol, npts    NUMERICAL CONTROLS, BOUNDED.
    cfg(1) = 1s               **DERIVED THIS SESSION. Was labelled CHOSEN.**

**THE LAST DECLARED CHOICE IS REMOVED.** SPEC §3 seeded the walk with 1s and
labelled it CHOSEN. Solved on the ruling path at Z=1:

    1s  E = -0.5000080791    2s  E = -0.1250033510    2p  E = -0.1250013413

1s is the argmin by 375 mHa. **The seed is not a choice; it is the exactly soluble
case, and the walk gets it right.** Two further receipts fall out:
  * E(1s) reproduces s62's independently recorded -0.500008079 to **1.4e-10** — a
    fifth determinism receipt, in a fifth session, on a third instrument.
  * **E(2s) and E(2p) agree to 2 microhartree — the hydrogenic l-degeneracy.** In a
    one-electron atom the Schrödinger equation makes l exactly irrelevant, and the
    field reproduces that. **The entire n+l structure — the fact that l matters at
    all — is therefore demonstrably a consequence of electron-electron repulsion
    and of nothing else.** That is the physical content of the Madelung rule,
    exhibited by the absence of the effect where the repulsion is absent.

**NUMERICAL FLOOR, for every margin quoted anywhere above: 0.05 mHa** (Rung 7 grid
floor 0.0108 mHa; s61 seed-memory floor <= 0.05 mHa; the larger and more inclusive
of the two is taken). Against a tightest chain margin of 32.33 mHa at Z=89, that is
a factor of 650. **Margins are physics, not numerics.**

---

## 5 · WHAT IS DERIVED, WHAT IS BOUNDED, AND WHAT IS OPEN

**DERIVED**
  * The period-length sequence 2, 8, 8, 18, 18, 32, 32 — Challenge criterion 2.
  * The n+l ORDERING clause — zero inversions in 119 rows.
  * The aufbau construction itself — Challenge criterion 3 — as the argmin of a
    binding energy on a field with no empirical input.
  * The seed cfg(1) = 1s.
  * The absence of l-dependence at one electron, which locates the origin of the
    whole effect in electron-electron repulsion.

**BOUNDED, WITH THE BOUND STATED**
  * Relativity: extension with an exact c -> infinity limit; c is measured, not fitted.
  * The seed forms (TFD, Latter, alpha=2/3): forgotten to 0.005 mHa from 52 Ha away.
  * Numerics: 0.05 mHa against margins of 32 mHa and up.
  * Single configuration (Rung 2): 11 of 107 rows displaced, none of them a
    first-entry row, ordering untouched.
  * The candidate truncation (Rung 9): closest excluded channel 87-157 mHa above
    the winner, monotone, wider at heavier Z.

**FALSE AS STATED, AND THE FIELD IS RIGHT**
  * The Madelung TIE-BREAK clause at n+l = 7 and 8. The walk enters 5d before 4f
    and 6d before 5f, in agreement with La and Ac and in disagreement with the rule.

**OPEN, NAMED, NOT WORKED (M's ruling, s62)**
  * The F61.1 re-walk of Z=2..56 under the guard — cause established, repair deferred.
  * The -8.021 mHa residue at Z=59; the coupled 4f2.5d spin-orbit check; the
    2.88 mHa residue of s56; the promotion operator as an object.
  * L2: finite nuclear size and mass are not modelled and not bounded here.
  * The winner surviving every seed is an observation at three rows, not a theorem.
  * Rows above Z=108 carry PREDICTED labels and no measured configuration.
  * F62.1: the s62 seal is a declared mixed-authorship seal. Four files of
    unestablished provenance were adopted by M's explicit ruling and are attributed
    as such. **This ledger fold is that attribution, discharging the obligation
    RULING-F62.1 deferred to Rung 0 assembly.**

---

## 6 · THE ANSWER TO LÖWDIN, IN ONE PARAGRAPH

Take the exact many-electron Schrödinger equation; restrict the wavefunction to a
single determinant of central-field spin-orbitals averaged over each shell; solve
the resulting radial Hartree-Fock equations self-consistently at nuclear charge Z,
with no fitted constant and no empirical input; and ask, at each Z, which available
channel binds the differentiating electron most strongly. **The answer to that
question, taken alone and iterated from hydrogen to Z=120, generates the period
lengths 2, 8, 8, 18, 18, 32, 32; fills channels in non-decreasing n+l without a
single exception in 119 steps; and departs from the n+l tie-break at precisely and
only the two places where the measured periodic table departs from it.** The rule
is not an axiom of the theory and it is not exact. It is what the electron-electron
repulsion does to the hydrogenic degeneracy, and where the two clauses of the rule
disagree with that, the repulsion wins.