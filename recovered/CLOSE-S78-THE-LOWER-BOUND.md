# CLOSE S78 — THE LOWER BOUND, FINISHED. IT IS NOT A TECHNICAL GAP. IT IS CIRCULAR.
# M instructed that this be returned to and finished, not parked. This finishes it, and
# the finish is a NEGATIVE one with a reason. THIS IS AN ARGUMENT. Nothing below is run.
# IT CORRECTS pack77/POSITION-S77-WHERE-THE-LOWER-BOUND-LIVES.md ON ITS CENTRAL POINT.

## §1 · WHAT IS ACTUALLY FREE — AN EXACT IDENTITY THAT REMOVES THE CORE MINIMUM
For a determinant with a CLOSED core {i} and ONE electron in a valence orbital v, the RHF
energy splits exactly:
      **E[Phi] = E_core[Phi_core] + <v| F_core[Phi_core] |v>**,
      F_core = h + sum_{i in core} (J_i - K_i),
because the valence self-interaction J_vv - K_vv vanishes at single occupancy. cfg_prev at
Z=89 is [Rn]7s2, closed; 6d and 6f each add ONE electron. **The identity applies exactly.**
**AND IT REMOVES E_min(cfg_prev) FROM THE PROBLEM.** The comparison that decides the row is
E_min(cfg+6f) - E_min(cfg+6d), in which the core minimum cancels. **The question was never
"how far can relaxation move a level"; it is "how far can relaxation move the DIFFERENCE
of two levels", and one whole term of s77's framing was never needed.**

## §2 · WHERE COURANT-FISCHER REACHES, AND IT IS NARROWER THAN s77 CLAIMED
POSITION-S77 §"WHERE THAT IS FREE": *"In a fixed field, more nodes means higher, and that
is a theorem, not an extrapolation."* **THAT IS TRUE ONLY WITHIN ONE ANGULAR CHANNEL.**
F_core is block-diagonal in l, and min-max orders the eigenvalues WITHIN a block. It says
nothing whatever across blocks.
**AND THE PAIR IN QUESTION STRADDLES TWO BLOCKS, WITH THE NODE COUNTS RUNNING THE WRONG WAY:**
| channel | l | nodes = n-l-1 | index in its block |
|---|---|---|---|
| **6d** | 2 | **3** | 4th |
| **6f** | 3 | **2** | 3rd |
**6f HAS FEWER NODES THAN 6d, NOT MORE.** s77's free theorem, applied to this pair, points
in the OPPOSITE direction to the thing to be proved. It is not weak here; it is adverse.
The one cross-channel statement that IS free is centrifugal monotonicity — l(l+1)/2r^2 is
monotone in l as a quadratic form, so eps_k(l+1) >= eps_k(l) for every k and any local
field. Applied here it gives **eps_3(l=3) >= eps_3(l=2)**, i.e. 6f lies above the THIRD d
eigenvalue, which is 5d, deeply bound and occupied. **True, rigorous, and useless.**

## §3 · THE FINISH. THE RESIDUAL IS THE CLAIM ITSELF.
After §1 and §2 the required statement is, exactly:
      **inf over admissible cores Phi of [ E_core[Phi] - E_core[Phi_d*] + eps_3^{l=3}(F[Phi]) ]
        >  eps_4^{l=2}(F[Phi_d*])**
Every term is a functional of one object, the core orbital set, and E_min(cfg_prev) is gone.
**BUT EVEN AT Phi = Phi_d*, WHERE THE RELAXATION TERM VANISHES BY CONSTRUCTION, THE
INEQUALITY REDUCES TO eps_3^{l=3}(F) > eps_4^{l=2}(F) AT A SINGLE FIXED FIELD — AND THAT IS
THE MADELUNG ORDERING AT Z=89, WHICH IS THE THING THE PROJECT EXISTS TO DERIVE.**
**SO THE LOWER BOUND IS NOT AN ADJUNCT TO THE DERIVATION THAT COULD BE SUPPLIED BY A
STABILITY ESTIMATE FROM OPERATOR THEORY. IT CONTAINS THE DERIVATION'S OWN CLAIM AS ITS
FIXED-FIELD SPECIAL CASE.** Any route that obtains it "for free" from spectral theory would
be obtaining the ordering for free, and no such route exists — which is precisely why
Hantsch's Remark (b) reports the gap open, and why BLLS does not transfer.

## §4 · WHAT THIS SETTLES, AND IT SETTLES SOMETHING
**s77 DIAGNOSED THE GAP AS "THE ENTIRE GAP IS THE NONLINEARITY, AND NOTHING ELSE". THAT IS
WRONG, AND THE CORRECTION IS THE RESULT.** Set the nonlinearity to zero — freeze the field
at the converged 6d solution — and the inequality does not become free. It becomes the
cross-channel ordering, unproved. **The nonlinearity is not the gap. It is an ADDITION to
the gap.** Rung C, as scoped at s77, was scoped to close the smaller half of its own problem.
**AND THE PRACTICAL CONSEQUENCE IS THE ONE M'S ORDER ASKED FOR — A TERMINUS, NOT A PARK:**
  1. **A lower bound on 6f is not to be sought as a route to the ordering.** It is the
     ordering. Route B, at this pair, is not narrower than the literature; it is the
     same statement wearing a different name, and s77's hope that it was narrower is
     withdrawn here.
  2. **What remains genuinely open and genuinely separate is the RELAXATION term alone** —
     the difference between the inequality at Phi_d* and at a general core. That IS a
     stability question, it IS what a Hessian could bound, and it is now isolated from the
     ordering claim by §1's identity rather than tangled with it.
  3. **The measured argument stands where a proof does not.** s77's five brackets place
     every non-converged channel at Z=89 more than twice the margin above rank 2. That
     remains the strongest true statement about this row and it remains not a proof.

## §5 · WHAT WOULD OVERTURN THIS
A cross-channel eigenvalue comparison for F_core derived from a structural property of the
self-consistent field that is NOT the ordering itself — a monotonicity, a convexity, or a
scaling law in the radial potential that forces eps_3^{l=3} > eps_4^{l=2} at every Z where
it is claimed. **Demkov-Ostrovsky 1972 has exactly such a property and GUESSES the
potential that carries it, which is why the attribution ledger rejects it on this project's
grounds. Deriving that property for the self-consistent F_core, rather than positing it,
IS clause 1 and is the last open deliverable. THE LOWER BOUND HAS NOW BEEN SHOWN TO BE THE
SAME OBJECT AS CLAUSE 1, AND THE TWO SHOULD NOT BE PURSUED AS SEPARATE ITEMS AGAIN.**