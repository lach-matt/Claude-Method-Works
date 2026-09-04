# THE TWO CHAINS, AND THE GAPS BETWEEN THEM

*Written 2026-08-11. Belokolos, SIGMA 13 (2017) 038, set beside this work's own
construction. Every join is computed; every gap is stated as a question with a
test attached rather than as a deficiency.*

---

## 1 · THE TWO CHAINS SIDE BY SIDE

**BELOKOLOS — from the Hamiltonian downward**

    mean-field central potential V(r)                    [approximation]
      → any central potential carries a dynamical O(4)   [Fradkin, Mukunda]
      → frequency degeneracy q·ω_r = p·ω_θ
      → E = E(p·n_r + q·ℓ)
      → Abel's integral equation gives a potential family indexed by α = q/p
      → REQUIRING Coulomb behaviour as r → 0 FORCES α = 2
      → the Tietz potential V(r) = −Z / (r(1 + r/R)²), R = (9/2Z)^⅓
      → E = E(n_r + 2ℓ) = E(M − 1)                       [Madelung's FIRST rule]
      → the oscillation theorem orders within M           [Madelung's SECOND rule]
      → E = 0 when √(2ZR) = M, i.e. Z = M³/6              [group onset]

**THIS WORK — from the ordering upward**

    ν(n, ℓ, q) = n − a·√( (n−ℓ−1) + q/2(2ℓ+1) )          [posited]
      → the entrant is the Pauli-admissible subshell of least ν
      → each element yields a corridor L(Z) < a < U(Z) from node counts alone
      → 106 of 106 corridors NON-EMPTY                    [the form survives]
      → the same construction on the nuclear shell ordering gives an EMPTY
        feasible set                                      [the form CAN fail]
      → crossings within a Madelung group = (√p_A + √p_B)/2
      → a sits at endpoints, i.e. ON crossings
      → 93 of 100 against measurement · 90 held out · 96 the Madelung null

---

## 2 · WHERE THEY JOIN — computed, not asserted

**The coordinates are the same.** His M = n + ℓ = n_r + 2ℓ + 1; our node count
p = n − ℓ − 1 is his n_r. Therefore

> **M = 2n − p − 1**, verified on every subshell.

Madelung's number is LINEAR in this work's coordinates.

**The 2 in that form is his frequency ratio.** α = q/p = ω_r/ω_θ = 2 — the radial
oscillation running twice per revolution — forced by the nuclear singularity.
That is where this work's factor of two comes from, and it has a derivation.

**His degeneracy is our ambiguity.** At E = 0 every member of an M group is
degenerate: the group exists, its internal order does not. He lifts it by going
to E < 0; we lift it with a. And the lifting condition is exact:

> within a group, Madelung's SECOND rule holds **iff a < (√p_A + √p_B)/2**
> for every open pair. The crossings are ceilings; the smallest is binding.

**Pauli mediates.** A full subshell leaves the contest, so the binding ceiling is
computed over the members Pauli has left open. Measured against the eight
recorded a values: five sit in groups reduced to a single open member and are
unconstrained; in the three where more than one remains open — La at M = 7, Pa
and Lr at M = 8 — **a sits exactly on the binding ceiling**, 0.7071, 1.3660,
1.9841. Three for three.

**And placing a just below the ceiling reproduces him.** Scored out of sample the
group rule gives 93 of 106, flat across five orders of magnitude in the step
below the ceiling, with **nine of its thirteen misses shared with Madelung's own
ten**. It reconstructs the rule from node counts rather than beating it — which
is what the derivation says it must do.

---

## 3 · THE GAPS

### GAP 1 — ν is posited; his potential is derived. *(the largest)*

Thyssen & Ceulemans sank Demkov–Ostrovsky on a guessed potential. Belokolos
answered it by forcing α = 2. **Nothing has forced ν.** Its defence here is
falsifiability — the nuclear corridor is empty where the atomic one is not — and
that is an epistemic defence, not a derivation.

**THE TEST.** His semiclassical spectrum is

    E_{M,ℓ} = −8 (√(2ZR) − M)(ℓ + ½) / ( (3η_ℓ² − 8η_ℓ) R² ),  η_ℓ = 2ZR/(ℓ+½)²

Rank the subshells by E_{M,ℓ} at each Z and compare the ordering to ν's. **If the
two orderings agree, ν is a reparametrisation of his spectrum and acquires his
derivation.** If they disagree, the disagreement is where ν adds or loses
something, and that is equally worth having. *This is the single most valuable
open computation in the project and it requires nothing we do not hold.*

### GAP 2 — q is in ours and absent from his.

His is a one-electron problem in a mean field: V depends on Z, not on which
subshell is filling. Our radicand carries **q/2(2ℓ+1)**, the Pauli fraction of
the target. So the occupancy dependence is entirely this work's and has no
counterpart in his chain.

**Why it matters.** Every classified miss lives in that term. The half-capacity
crossing (Mn, Tc, Gd, Cm) exists only because q makes both radicands
half-integers. **If ν is to be derived from his spectrum, the q-dependence is
exactly what must be added — and a mean field cannot supply it.**

### GAP 3 — neither carries the exceptions.

He says so outright. We classify ours into four causes — half-capacity crossing,
node-free entrant, real source, and one unexplained — but classification is not
prediction. And **the trigger question is open on both sides**: nothing in either
chain says WHEN a relocation occurs, only which subshell donates once one does
(R 1397, twelve of twelve).

### GAP 4 — a has no physical identification.

His variables are Z, R = (9/2Z)^⅓, η_ℓ, and the dimensionless scalings ν_r, ε.
Our a is dimensionless and carried, ranging 0.577 to 1.984 over the walk.
**Nothing connects them.** Until a is expressible in his variables, the join at
§2 is structural rather than physical.

**THE TEST.** Fit a against √(2ZR), Z^⅓, M and (ℓ+½) at the eight recorded
values and at every corridor endpoint. A relation, if it exists, should be exact
rather than approximate — the endpoints are surds.

### GAP 5 — CLOSED 2026-08-11. The parity term is in his own §2.

Z = M³/6 against the observed block starts:

    M       3      4      5      6      7      8
    Z=M³/6  4.5   10.7   20.8   36.0   57.2   85.3
    observed  5     13     21     39     57     89
    rel err  −10%  −18%    −1%    −8%     0%    −4%

**Odd M: 3.7% mean error. Even M: 9.9%.**

**RESOLVED.** He quotes Klechkovski–Hakala in his own §2: Z = K(n+ℓ) + 1 with
K(x) = (1/6)x(x² + 2 − 3µ(x)), µ(x) = x mod 2. That reproduces every onset
EXACTLY — 1, 3, 5, 13, 21, 39, 57, 89. **Z = M³/6 is the leading asymptotic of
that same expression with the µ term dropped**: odd M loses −M/6, even M loses
+M/3, twice the magnitude and the opposite sign. So the parity is exact
combinatorics he CITES and does not DERIVE, and the 87-of-106 ranking is what
his ASYMPTOTIC achieves rather than a bound on his approach. Registers 1455,
1456.

### GAP 6 — his rigour and ours are different kinds.

His is semiclassical: Bohr–Sommerfeld quantisation, first order in ε, with the
higher terms divergent and requiring regularisation. Ours is not an approximation
of anything — ν is an ordering functional with no equation behind it. **The two
are not comparable on rigour**, and any claim that one supports the other must
say in which sense.

### GAP 7 — the O(4) premise is inherited, not checked.

"Any central potential carries a dynamical O(4) symmetry" is attributed to
Fradkin (1967), Bacry–Ruegg–Souriau (1966), Mukunda (1967). These are CLASSICAL
statements about constants of motion; the quantum content is subtler and the
step from one to the other is where a proof of this shape would be attacked.
**Not verified here.** It should be read before his conclusion is relied on.

### GAP 8 — neither generates past the record.

He predicts group onsets (Z = M³/6) but not configurations. We measure a forward
horizon of **3.9 steps** against Madelung's 6.0. Populating 109–120 needs ten.
**Neither chain reaches the unobserved table**, which is what the Löwdin
challenge was posed to achieve.

---

## 4 · WHAT WOULD CLOSE WHAT

| gap | closed by | cost |
|---|---|---|
| 1 · ν underived | ~~one script~~ **RUN** — 87 his, 99 ours, 88 agreeing; ν is NOT a reparametrisation | done |
| 2 · q absent | **PREDICTION REFUTED** — the 18 disagreements split 10 at q = 0, 8 at q > 0 | reopened |
| 3 · exceptions | a trigger rule for relocation; open on both sides | unknown |
| 4 · a unidentified | fit a against his variables at the surd endpoints | one script |
| 5 · parity | ~~unknown~~ **CLOSED** — the µ(x) term of Klechkovski–Hakala, dropped in his asymptotic | done |
| 6 · rigour | state in which sense ν approximates his spectrum | follows from 1 |
| 7 · O(4) premise | read Fradkin and Mukunda; check the quantum step | reading |
| 8 · generation | a placement rule beating 96 out of sample; six have failed | unknown |

**Gaps 1, 2, 4 and 6 are one computation and its consequences.** Gaps 3, 5 and 8
are open questions with no route in hand. Gap 7 is reading.

---

## 5 · THE HONEST SUMMARY

**He has the derivation; we have the measurement.** His chain forces the
Madelung ordering from a symmetry argument and stops before the exceptions. Ours
reproduces the second rule from node counts, lands on the same exceptions, and
has been scored out of sample against a null that neither chain beats.

The objects are now the same objects — his n_r + 2ℓ is our p and ℓ, his
degeneracy is our crossing, his frequency ratio is our factor of two, and his
group is what Pauli prunes and a orders. **That is a position from which the
gaps can be stated precisely, which is worth more than either chain alone and is
where the work now stands.**
