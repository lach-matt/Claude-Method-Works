# PLAN — TURNING THE DERIVATION STATEMENT INTO A PROOF. SESSION 75.
# M's ruling R-D. This is a PLAN, not a result. Nothing below is claimed as done.

## THE GAP, STATED PLAINLY.
**107 VERIFIED INSTANCES IS NOT A THEOREM.** Nothing in the Formal Derivation
Statement SS1 is proved; it is EXHIBITED. Three routes stand between the two, and
they are independent.

## R-D · M's RULING ON ORDER, s75.
**0 -> B -> A -> C. C IS ADDED AS THE FINAL CHECK.**

## STEP 0 · PHI MUST BECOME A MATHEMATICAL OBJECT, NOT AN ALGORITHM.
SS3 defines Phi by what the program does. A theorem must quantify over objects that
EXIST. Required:
  * **Existence of the HF minimiser.** Lieb-Simon 1977: minimisers exist for N <= Z.
    Parameter-free, OPEN ACCESS (A1's paywall does not block this), and it converts
    SS3 from an algorithm into a definition.
  * **Non-uniqueness of the SCF fixed point** - uniqueness, or a stated selection
    rule. The convergence ladder (beta, maxit) is today a NUMERICAL CONTROL; in a
    proof it becomes part of the definition or must be eliminated from it.
  * **Uniqueness of the argmin.** Ties excluded or handled explicitly.
**WITHOUT THIS THE THEOREM HAS NO SUBJECT.** Cheap. Required by B, A and C alike.

## ROUTE B · THE STRUCTURAL THEOREM. THE SHARP TARGET.
For the Coulomb problem n = n_r + l + 1, therefore
        **n + l  =  n_r + 2l + 1**
**THE ORDERING CLAUSE IS EXACTLY THE CLAIM THAT THE SPECTRUM ORDERS BY n_r + 2l.
THE WHOLE OF MADELUNG REDUCES TO ONE NUMBER: THE WEIGHT 2 ON l RELATIVE TO THE
RADIAL NODE COUNT.** The question becomes *why is the screening-induced
l-destabilisation exactly twice the radial-node spacing* - a question analysis can
grip, where "why n+l" is not.
**THE EFFECT IS ENTIRELY IN THE REPULSION AND SS C5 ALREADY ISOLATES IT:** at Z=1 the
shift is zero and 2s/2p agree to 2 microhartree. **SO THE 2 MUST COME OUT OF THE
REPULSION.**
**PRIOR ART INVERTED:** Demkov-Ostrovsky exhibit a potential with exact n+l
degeneracy, rejected in the ledger because the potential is GUESSED. **THE TARGET
IS TO SHOW THE DERIVED HF FIELD LIES IN THE CLASS THEY GUESSED AT.** Same object,
opposite epistemic direction: the competitor becomes a lemma.
**INSTRUMENT PRECEDENT IN THIS PROJECT:** s32 derived closed-form limits and
certified them against constant-free consequences of causality (f-sum,
compressibility). A comparison theorem (Sturm, Kato) or a sum rule on the screening
is the natural instrument here.
**M's STANDING PRINCIPLE APPLIES:** every null is a gap that may need a different
mathematical language. The DO degeneracy arises from a DYNAMICAL SYMMETRY; the
closing language may be ALGEBRAIC rather than analytic.
**RISK, STATED: THE ORDERING CLAUSE MAY NOT BE A THEOREM.** The tie-break already
turned out false when tested. A proof attempt is also a falsification attempt.

## ROUTE A · CERTIFIED EXHAUSTION. Proves exactly the statement written.
The claim is FINITE (Z=2..108), so exhaustion is legitimate proof - the
Hales/Tucker pattern.
  * Interval arithmetic replaces floating point on the radial integration, plus an
    a posteriori bound on the SCF fixed point (Newton-Kantorovich).
  * **THE CERTIFIED ENCLOSURE WIDTH MUST BE STRICTLY BELOW EACH ROW'S MARGIN. THE
    NUMBER THAT DECIDES IT IS ALREADY OWNED: TIGHTEST CHAIN MARGIN 32.33 mHa AT
    Z=89.** Today's 0.05 mHa floor is an ESTIMATE; the work is making it an
    ENCLOSURE.
  * **The candidate truncation must be PROVED, NOT SAMPLED.** "Closest excluded
    channel 87-157 mHa above the winner" is measured at some rows; a proof needs a
    bound over ALL excluded channels at ALL rows.
Limit: proves nothing above Z=108 and EXPLAINS nothing.

## ROUTE C · THE CODE MUST BE SHOWN TO COMPUTE PHI. **FINAL CHECK, M's RULING.**
A computer-assisted proof is only as strong as the claim that the program
implements the specification. That link rests today on line-level receipts and
gates. **THE BLIND WALK STOPS BEING OPTIONAL HERE:** extending it 16 -> 107 was not
a prerequisite for the derivation statement but IS load-bearing for a proof.

## THE CONDITION ON C-AS-FINAL, AND IT IS THIS PROJECT'S OWN RECURRING FAULT.
**C AT THE END IS SOUND IF AND ONLY IF ROUTE A IS EXECUTED AGAINST THE FROZEN SPEC
OF STEP 0 - THE MATHEMATICAL OBJECT - AND NOT BY INSTRUMENTING THE EXISTING CODE.**
If A is run by instrumenting the code, then C-after-A is F54.2 and F74.2 exactly:
**THE OBJECT CERTIFIED WOULD BE THE ONE THE CODE HAPPENS TO COMPUTE, NOT THE ONE
THE THEOREM NAMES**, and a certified proof of the wrong theorem is the most
dangerous artefact this project could produce (cf. R 1525: a capture that SUCCEEDS
while holding the wrong thing).
**WHY M's PLACEMENT IS NEVERTHELESS RIGHT:** checking code against a specification
still being moved by B is wasted work. **THE SPEC MUST BE FROZEN AT THE CLOSE OF B;
A CERTIFIES THE OBJECT; C THEN VERIFIES THE CODE WAS THAT OBJECT ALL ALONG.**
**FAILURE MODE OF C, DECLARED IN ADVANCE: IF C FAILS, A IS RE-RUN. A IS NOT VOID.**
And R-A binds C: an audit by name is not an audit - the lever must be poisoned and
the consumer must die.