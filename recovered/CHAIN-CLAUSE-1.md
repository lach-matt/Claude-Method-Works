# CHAIN-CLAUSE-1 — Clause 1 as six links, walked BACKWARDS from the order to the equation.
# Written s89 FIRST, before any unit runs, on M's s88 ruling. No sealed file edited.
# c = 137.035999 is the only number ever entered. The derivation is 107 rows, Z=2..108.
#
# Each link: (i) statement (ii) limit parameter (iii) measured remainder (iv) where sealed (v) status.
# The TARGET is the observed ORDER at the width-2 frontier; "n+l" is its name (89% by count; La, Ac invert).

## L1 · ORDER <- sign of Delta g between the two frontier candidates
 (i)   At step Z-1 -> Z, the entrant is the rank-1 candidate in nu; the rival is rank 2.
       g = l + delta = n + l - nu.  Delta g/Delta l = (g2 - g1)/(l2 - l1) from the sealed ladder.
       The banked ORDER is equivalent to the sign of that difference (given nu ordering).
 (ii)  none — this is a re-labelling of the banked D values.
 (iii) none — 107/107 rows carry their ordering verdict in D1; 106/107 have Delta g > 0,
       Z=90 has Delta g = -0.293 (the sole width-2 failure; actinide 5f/6d).
 (iv)  D1 (DELIVERABLE-1-THE-ORDERING-CLAUSE.md, gate86); ladder rt/nlchain.jsonl.
 (v)   IDENTITY.

## L2 · sign Delta g <- dg/dl = 2 - J, the action in u = 1/r
 (i)   For one channel at fixed energy E in the radial field q(r) = -r V_loc:
       dg/dl = 2 - J, J = (L/pi) I, I = int du / p(u) over the OUTER allowed region,
       L = l + 1/2, with the inner-region/variable-q terms cancelling identically.
 (ii)  the semiclassical anchor (Coulomb q = const gives J = 1 exactly, 7.5e-12).
 (iii) two-channel sign: s84 §S7 6/6 rows agree (incl. the Th reversal); s84-s88 35/37,
       Z=56 a region switch (the outer-well rule and the merge). Magnitude NOT claimed.
 (iv)  s84 RESULT-S84-ITEM1-SEMICLASSICAL (R-range s84), rt/semi84.py.
 (v)   THEOREM (one-channel identity, exact in the semiclassical action).
       Two-channel passage (sign of the DIFFERENCE) is the content of L3.

## L3 · J < 2 <- convexity of S(u), mass K < 1 (tent), or the profile condition
 (i)   If the action integrand S(u) is convex with mass K = b0 + b1 < 1 then J <= J_tent(b0,b1) < 2,
       hence dg/dl > 0 for that channel. Profile route (s88): phi = direct field of a walk-drawn
       sub-core lifts the tent; 43/50 certified at the deepest accepted rung.
 (ii)  the tent mass K (K -> 0 recovers the Coulomb anchor).
 (iii) OPEN at five rows, all well-merge (collapse) rows with measured J >= 2:
         Z=40 4d (J=2.076)  Z=56 5d (2.441)  Z=89 6d (2.020)  Z=90 5f (2.102)  Z=91 5f (2.046)
       s88 T1: no one-channel bound of the J<2 kind can certify a channel with measured J >= 2.
       Therefore the open statement is TWO-CHANNEL: the sign of Delta g for the PAIR. (Unit 1a.)
 (iv)  s85 (tent, R-range s85), s86 (Gauss cut), s87 (kinetic cap), s88 (profile, 43/50).
 (v)   THEOREM where it applies; OPEN at the five rows.

## L4 · convexity of S <- Gauss: S'' = r^2 rho >= 0 (direct field)
 (i)   For the DIRECT core field, q'' in u is r^2 rho(r) >= 0 by Gauss's law, so S is convex.
       With same-shell exchange (E7) at an OCCUPIED channel, S'' = r^2 rho + X'' and X'' < 0 can
       break convexity.
 (ii)  the exchange weight (X -> 0 is the direct field).
 (iii) MEASURED: 13 refusals at P2 (s88), all occupied channels; size 0.07 at Z=24, 0.28 at Z=56 in q.
       Bound on |X''| from the 13 refused channels is Unit 1b.
 (iv)  s86 RESULT-S86-ITEM1-GAUSS-CUT; s88 RESULT-S88-ITEM1-PROFILE §refusals.
 (v)   THEOREM for the direct field; remainder MEASURED, not yet bounded.

## L5 · rho <- the scalar-relativistic HF field <- its Hamiltonian
 (i)   rho(r) and V_loc(r) are the converged frozen-core (N-1) scalar-relativistic HF field
       at Rung 0 (beta=0.4, maxit=100), fixed81.Frozen81, c = 137.035999.
 (ii)  c. The non-relativistic limit is c -> infinity (c = 1e6 operationally; lever nlguard.C0).
 (iii) Clause 3: the ORDER at Z=90 flips at c -> inf (5f selected non-relativistically, 6d
       scalar-relativistically, 253 mHa). Figures at Z=90 do not travel (standing). Unit 1c enters
       this as the remainder of L5 — no new runs.
 (iv)  Deliverable 5 (CLAUSE-3-COVERAGE), s54-s56; lever law F54.2.
 (v)   COMPUTED.

## L6 · HF field <- many-electron Schrödinger equation
 (i)   The HF field is the stationary point of <Psi|H|Psi> over single Slater determinants,
       H = sum_i (T_i - Z/r_i) + sum_{i<j} 1/r_ij (scalar-relativistic T at L5).
 (ii)  NONE. This is a VARIATIONAL restriction, not a limit with a parameter. The proof form
       must name it as such: the chain derives the order of the HF ground-state differentiating
       electron, not of the exact many-electron ground state. Correlation is the unmeasured gap.
 (iii) not measured in this project (out of scope by M's ruling; standard literature).
 (iv)  standard; attribution ledger entries (Hartree, Fock, Slater).
 (v)   VARIATIONAL.

## The proof form, read forwards (L6 -> L1)
 Schrödinger (L6, variational) -> SR-HF field rho, q (L5, c the parameter) -> S convex for the
 direct field (L4, exchange the remainder) -> J < 2 per channel where K < 1 / profile holds (L3)
 -> dg/dl > 0 (L2, identity) -> Delta g > 0 -> the banked order (L1, identity).
 Status of Clause 1 at s89 open: links L1, L2, L6 closed as labelled; L4 and L5 closed with a
 measured remainder; L3 open at five rows, all well-merge rows — the unit of work is the PAIR.

## Units ordered for s89 (prediction hashed before each)
 1a  L3 at the five rows, two-channel (both wells, Z-1,Z,Z+1; neighbourhoods 38-41, 55-57, 88-92).
 1b  L4 exchange remainder as a bound |X''| from the 13 refused channels.
 1c  L5: enter Clause 3 as the remainder; no runs.
