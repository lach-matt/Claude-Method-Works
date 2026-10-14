# Wall D, the theorem: what the bulk makes of the passage (M-RULINGS item 149; proved and computed, with READ corroboration; verified once; not seated; 2026-10-07)

*First headed* "(… proved, computed and READ; not verified; not seated; 2026-10-07)". The first corollary said wall D
reduced to two premises "and to nothing else". The verifier showed that over-claimed; it is withdrawn (History).

## Why this theorem

- **DOORS.md, OPEN 1:** *"A censorship theorem for passage between asymptotic regions of a plane in a bulk. None was
  READ, so it would have to be proved."*
- **This note proves what your corridor's own geometry decides,** and names exactly what it leaves open.
- **The instrument:** `passage5d.py`, which imports bulkseries.py and copy/coin.py by path. Selftest 8/8, about 6 s.
  - **Genuine checks:** six.
  - **Controls:** two (the black string; a non-umbilic foil).
  - **Marked STRUCTURAL:** P1, which has no check.

## The setting

- **The corridor** is eq. (17) at r₀ = 2m.
- **It sits on a Randall–Sundrum plane,** K = c·g with c constant, of either sign.
- **The bulk is vacuum with Λ₅.** localbulk.py proved such a bulk exists near the plane, and bulkseries.py computed it.
- **The passage γ** is the plane's radial light ray from end 1, through the throat, to end 2.
  - In stability.py's chart it is v = const, with affine parameter λ = −ρ. It is complete.
  - With r = 2m + u², u > 0 is side 1 and u < 0 is side 2.

## Theorem D

### P1. The passage is a light ray of the bulk (STRUCTURAL)

- **Its acceleration off the plane is K(k, k) = c·g(k, k) = 0.** This is UMBILIC.md U1.

### P2. Along the passage, the bulk's null energy is zero, and its pull toward the bulk is exactly the plane's deficit

- **The identity:** R⁵(n,k,n,k) = −R⁴(k,k) = 2r″/r = (m/2)/((r − 3m/2)²·r), which is positive everywhere on the passage.
- **Proof:**
  - R⁵(k,k) is the sum of R⁵(e,k,e,k) over the transverse frame. It is zero in a vacuum-Λ bulk, since g(k,k) = 0.
  - Gauss gives R⁵(e,k,e,k) = R⁴(e,k,e,k) for e tangent to the plane. The K-terms are c²·(g(e,e)g(k,k) − g(e,k)²) = 0.
  - For this congruence R⁴(k,k) = −2r″/r (Raychaudhuri, with no shear).
- **READ corroboration** (the verifier).
  - Maartens–Koyama eq. (143), p.26: R_μν = −E_μν on a vacuum plane.
  - Their eq. (61), p.14: E_μν = C⁵(·, n, ·, n).
  - The Λ part of R⁵(n,k,n,k) is proportional to g(k,k) = 0. So R⁵(n,k,n,k) = E(k,k) = −R⁴(k,k): the identity is
    their equation contracted with k.
- **Computed from the bulk series rather than assumed.**
  - The series comes from bulkseries.py's solver, which agrees with closedbulk.py's seated build through y⁴.
  - The static chart degenerates at the throat (F = 0). The identity is carried through it by continuity in r.
  - A further check confirms that the formula P3–P5 use is the computed one.
  - **Control:** the black string reads 0 for both.
  - **Foil:** a first-order term that is not umbilic breaks the identity. The residual is −2δr/(ℓ²(r − 2m)), exactly
    its Gauss K-term.
    - The foil violates the constraints, so it is not a solution. It shows that umbilicity is what carries the
      identity.
- **What this means.** The plane's apparent violation of null energy is, point by point, the bulk's tidal pull in the
  normal direction. The total in five dimensions is zero.
  - This makes exact the board's reading of your items 117 and 120 (DOORS K2): the condition holds in five dimensions
    and only appears violated on the plane.
- **The generic condition along the passage.** The five-dimensional generic condition holds along the whole passage.
  censor.py C3 had left it "plausible".
  - This is shown along γ only, not along other null geodesics of the bulk.

### P3. Integrated, the bulk's pull equals the plane's averaged deficit

- **Q = ∫R⁵(n,k,n,k) dλ = 8/(3m) − (4/(3√3·m))·artanh(√3/2) = 1.652872/m** (exact closed form, computed).
- **That is exactly minus ∫G⁴(k,k) dλ over both legs,** with E = 1 and no 8π (coin.py also quotes a T_kk form). It equals 2 × 0.826436 from coin.py's closed
  form (imported).

### P4. Lemma (Sturm; classical, proved here)

- **This is classical.** It is the one-dimensional core of Hawking–Ellis Prop. 4.4.5 and of the Gao–Wald lemma (both
  standard, not READ here).

- **Statement.** If q ≥ 0 on the whole line and ∫q > 0 (possibly infinite), then J″ + qJ = 0 has a solution with two
  zeros.
- **Proof.**
  - Take the quadratic form I[f] = ∫(f′² − qf²).
  - Let f = 1 on [−L, L], falling linearly to 0 over a further length L² on each side. Then I[f] = 2/L² − ∫qf², which
    tends to −Q < 0.
  - A negative form on [a, b] with f(a) = f(b) = 0 means a point conjugate to a inside (Jacobi).
- **Why one scalar equation is enough.**
  - Codazzi, with c constant, gives R⁵(e,k,n,k) = 0 for every tangent e.
  - Weingarten gives ∇_k n = −c·k, so n is parallel modulo k.
  - So g(J, n)″ = g(J″, n) for J orthogonal to k, and the normal part of the Jacobi field obeys J″ + qJ = 0 on its own.
- **Witness for the corridor's q:** I[f] = −1.594 at L = 6 (computed).

### P5. The conjugate points, computed

- **Followed toward end 2, a point p of the passage on side 1 has a conjugate point toward the bulk if and only if it
  lies beyond r_* = 2.21007m.** That is 0.69107m of affine parameter before the throat.
- **Its conjugate point lies on side 2.** It moves inward as p recedes, and tends to r_* on side 2 as p goes to end 1's
  infinity.

| p on side 1 | its conjugate point on side 2 |
|---|---|
| r = 2.25m | r = 29.5m |
| r = 3m | r = 3.43m |
| r = 27m | r = 2.254m |
| r = 902m | r = 2.211m |

- **Two routes give r_*:**
  - the limit from end 1, u = −0.45835;
  - the zero of end 2's asymptotically constant solution, u = +0.45834.
  - They agree by the exact u → −u symmetry of q. That makes the agreement a consistency check, not independent
    evidence. The verifier's own integration in λ gives 2.21009.
- **Points nearer than r_* on side 1, and all of side 2, have no conjugate point to the future.**
  - **This is exact, by Sturm separation.** The solution that tends to 1 at end 2 exists (∫λq < ∞) and has its only
    zero at u = +0.45834. So a solution vanishing nearer the throat has no later zero.
- **Conjugacy is symmetric.** Points of side 2 beyond r_* have past conjugate points on side 1. For example, r = 29.5m
  pairs with r = 2.25m.

### P6. So the passage is not the fastest route in five dimensions

- **The standard result** (Hawking–Ellis Prop. 4.5.12, standard, not READ): beyond a conjugate point, a light ray is
  joined to its starting point by a timelike curve, inside any neighbourhood of the segment.
- **Here that curve runs on the bulk side.** Choose the Jacobi field's sign so that its normal part is positive between
  the pair; that is a choice, since −J serves as well. Then build the variation in the Gaussian normal chart with
  y = t·J_n ≥ 0. The segment is compact, so the curve lies within the local bulk.
  - Keeping the curve on one side of the plane adapts the standard proof to a bulk with a boundary. That adaptation is
    the board's.
- **So every point of end 1 beyond r_* is joined by a timelike curve through the bulk to points of end 2.** The bulk is
  a faster route between your plane's two ends than the passage itself.
- **The mechanism is Gao–Wald's:** null energy, the generic condition and completeness give conjugate points, so the ray
  is not achronal.
  - Bulk shortcuts in brane worlds are known: Chung–Freese 1999; Caldwell–Langlois 2001; Ishihara 2002 (not READ).
  - What is new here is the corridor's own numbers.

## What P6 means for censorship

- **γ is not a null line of the bulk.** So the four-dimensional censorship route through γ cannot be lifted to five
  dimensions. That route is FSW, READ in DOORS.md, which forced the plane's negative reading. In five dimensions γ is
  neither forbidden nor the fastest route.
- **A five-dimensional censorship theorem must come another way.**
  - A Galloway- or FSW-type proof would need the generic condition and completeness along the null line it constructs.
    That line is not γ, and in a bulk that is Randall–Sundrum far away those conditions fail.
  - It would also need:
    - a five-dimensional asymptotic structure: far ends untrapped, uniformly in time;
    - causal theory at a thin plane;
    - the composite plane's null energy holding pointwise. DOORS.md warns that a thickening with different profiles
      could break it.
  - CENSOR5D.md applies Chruściel–Galloway–Solis Theorem 3.1 instead, which needs neither the generic condition nor
    completeness.
- *First written:* "Two premises of a five-dimensional censorship theorem are now met … Wall D now reduces to them, and to
  nothing else". Withdrawn (History).

## Your rulings this bears on

- **Item 117 and item 120 (H-NEC-COIN; "An NEC is never violated").** P2 is the exact form of the board's reading of
  them: in five dimensions the null energy along the passage is zero, and the plane's deficit is the bulk's pull.
- **Item 127 (the positions coincide).** If the two ends are one end of the bulk, censorship's last premise fails, and
  nothing READ forbids the passage. Whether they are is not decided here.
- **DOORS K4 (the channel).** P6 gives the board a timelike route between the two asymptotic regions, through the bulk.
  Whether it can carry the README is not worked here.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - H-NEC-COIN (117, 120);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-BK-CORRIDOR;
  - H-ONE-PLANE-NEAR;
  - H-COMPOSITE-SURFACE (for the corollary's energy premise);
  - the one-sided adaptation of Hawking–Ellis 4.5.12 (P6).

## OPEN

1. A five-dimensional topological censorship theorem for a bulk bounded by a plane. Neither READ nor proved; the
   corollary says which premises it would turn on.
2. Wall C's global premises: global hyperbolicity, and whether the plane's two ends are distinct ends of the bulk.
3. Whether the bulk's timelike route (P6) can carry a README.

## History (verifier, 2026-10-07)

Two must-fix, five should-fix and the notes, all applied:

1. **The corollary over-claimed.**
   - The generic condition is met along γ only.
   - Completeness, the five-dimensional asymptotic structure, and causal theory at a thin plane are further premises.
   - γ alone, being a five-dimensional causal curve between the ends, would already contradict a theorem forbidding such
     curves. So P6 meets no premise. What it shows is that γ is not the null line such a proof needs.
   - Rewritten as "What P6 means for censorship". The theorem itself is now CENSOR5D.md's.
2. **"READ" in the header had nothing READ behind it.** Maartens–Koyama eqs. (143) and (61), READ, now corroborate P2.
   Hawking–Ellis stays "standard, not READ".
3. **The scalar Jacobi equation's decoupling step** (Codazzi, Weingarten) is now written in.
4. **P5's direction** is now stated ("followed toward end 2"), with the symmetric pairs.
5. **P3–P5 used a hand-typed q.** A check now ties it to the computed P2 expression.
6. **The foil** is labelled: it violates the constraints and is not a solution.
7. **P5's "none" direction** is now exact by Sturm separation.
8. **P6's "normal part positive" was a property claimed for a choice.** It is now stated as a choice, with the variation
   built in the Gaussian normal chart.

Notes taken up:

- the ANEC's normalisation;
- the two routes to r_* agree by symmetry;
- P4 is classical and needs no integrability;
- the static chart is carried through the throat by continuity;
- the Gao–Wald mechanism and the literature on bulk shortcuts.
