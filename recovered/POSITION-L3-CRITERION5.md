# THE POSITION ON L3 AND CRITERION 5, ASSEMBLED FROM THE RECORD. SESSION 75.
# A READ, NOT A BUILD. No sealed file edited. No new computation run.

## 1 · L3 IS NOT UNWORKED. IT IS WORKED IN TWO HALVES, AND BOTH ARE HELD.
s70 SS0.1 states L3 as one object in four costumes and says nothing else is
outstanding. What s70 did NOT have, and s71-s73 supplied:

**HALF ONE - BEYOND AVERAGE-OF-CONFIGURATION (the L4 costume). HELD, SEALED s38/s48.**
  rt/hfterm.py + rt/nlterm.py: explicit determinant enumeration dets(l,N) and the
  Slater DIAGONAL-SUM rule computing every (S,L) term of l^N. **The lowest term is
  COMPUTED, not asserted. Hund is a comparison column, RECALLED-NOT-ENTERED.**
  rt/pb4_terms.py: TWO-CONFIGURATION energy competition. At Z=64 Gd the
  average-of-configuration prefers B and the determinantal correction REVERSES IT
  BY 184 mHa. Parameter-free, carries only c. (s71 SS1; M's recall was correct.)

**HALF TWO - CONFIGURATION MIXING, THE OFF-DIAGONAL (the true L3 costume).**
  No off-diagonal element existed anywhere in the archive before s71. Built and
  scored as PREDICTION-CI2x2: CI-1,3,4,5 (s71), CI-2,6,7 (s73). CI-8 assessed at
  s74 as NOT REQUIRED by any criterion.
  **THE LOAD-BEARING RESULT: V IS ZERO AT EVERY FIRST-ENTRY ROW BY OCCUPANCY, AND
  AT EVERY d<->f TIE-BREAK ROW BY PARITY.** Zero by SELECTION RULE, not by
  smallness. CI-2: spectator spherically averaged -> V machine zero, worst
  1.7e-15 mHa. CI-7: S = I as derived, the 2x2 is ordinary symmetric.

## 2 · WHAT THAT BUYS, AT THE STRENGTH s73 ITSELF STATED.
Criterion 6 **DEFENDED, not advanced** - the single-determinant objection to
Deliverable 1 is answered by derivation at exactly the rows that carry the
ordering clause. Criterion 7 **NARROWED, not met** - one mechanism eliminated at
three exceptions is an elimination, not an explanation.
**CRITERION 5: UNTOUCHED. And s73 was right to say so.** A demonstration that the
approximation does not BITE at the deciding rows is s70's Option B - a bound - and
M ruled Option B DEAD AS CLOSURE. It is evidence. It is not derivation.

## 3 · THE THING THAT IS ACTUALLY BLOCKING, AND IT IS NOT COMPUTATIONAL.
**TWO STANDARDS ARE IN THE RECORD AND ONLY ONE OF THEM IS THE CHALLENGE'S.**
  (a) **THE CHALLENGE AS DOCUMENTED.** s71 SS3, four-way triangulation, every source
      citing Loewdin 1969: the demand is **ab initio** - no fitted or empirical
      input - and **HARTREE-FOCK IS INSIDE IT. No source states an exactness
      clause. No source states a non-relativistic clause.** Under (a) criterion 5
      is MET by the chain as it stands.
  (b) **M's STANDARD, s70:** *an approximation cannot be a true derivation.* Under
      (b) no HF chain can meet criterion 5 at any amount of further work, because
      L3 is a variational restriction by construction. Only the FCI limit meets it.
s71 SS3 named this separation explicitly and **DID NOT RESOLVE IT**, on the correct
ground that it is M's to resolve: *"it separates what the Challenge asks from the
standard M holds this project to."* **IT HAS BEEN UNRESOLVED SINCE s70. IT IS THE
ONLY THING BETWEEN THE PROJECT AND T4.**
**A1 IS STILL [SECONDARY].** Loewdin 1969 is paywalled at Wiley and has never been
read in primary form. Under (a) that matters, because (a) rests on triangulation.

## 4 · IF M HOLDS (b) - THE ONE ROUTE THAT IS DERIVATION AND NOT BOUND.
Not "compute FCI for 107 atoms" - unnecessary and impossible. The claim needed is
**THE ARGMIN IS INVARIANT UNDER RELAXATION OF L3, TO ALL ORDERS.**
CI-2x2 laid the first stone: the deciding-row V vanishes by OCCUPANCY and PARITY,
which are statements about matrix elements of the EXACT Hamiltonian, not about HF.
**THE HONEST DIFFICULTY, NAMED NOW SO IT IS NOT MET AS A SURPRISE:** the argument
does not extend naively. Parity forbids the odd orders; **TWO excitations restore
parity**, so second order is not killed by the same rule. Any all-orders claim must
be made on the ARGMIN MARGIN, not on the individual element. Whether it survives
is precisely the thing to test, and it is a derivation-shaped test, not a walk.
**THE TRAP, CARRIED FORWARD FROM s70 SS0.3:** the CORR branch in the code is a
Gell-Mann-Brueckner functional whose coefficients are derived nowhere in this
chain; hfc2.py:11 defaults it TRUE and nlchain.py:17 switches it off. **CORR=True
IMPORTS UNDERIVED COEFFICIENTS AND BREAKS CRITERION 4. Route C and CORR=True are
OPPOSITE MOVES.**