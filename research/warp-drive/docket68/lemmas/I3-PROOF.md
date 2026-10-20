# I3: the complete proof of its computations (I3s and I3; item 542)

*First written* 2026-10-20, on M's item 542 ("add lemmas to close these gaps. nothing gets narrowed, only expanded to
complete the statement") and item 538 ("anything COMPUTED-THEORIZED should have a complete proof for the
computations"). I3s and I3 are COMPUTED-THEORIZED. This file proves every computation they name, from i3_info.py
(I0-I9). Its section 4 names what is theorized.

Labels:
- proved: a complete argument here;
- computed (exact): an instrument's symbolic identity;
- READ: a source read at the passage quoted, in the instrument named;
- theorized: a step beyond the established core, named;
- M's: a ruling.

## 1. The theorem

**THM-I3.** After the README's release, our face radiates on our plane for the rest of its life (CLOSEs, CLOSE; M's
336). On the island formula (H3 below), at both ends:
1. the face's fine-grained entropy S_hole(t) never exceeds its Bekenstein-Hawking entropy S(t);
2. the quantum extremal surface lies inside our face's event horizon, a scrambling time back, where QB departs from the
   classical interior by at most 2.6e-18 -- so the island is in our face, in our universe, and nothing crosses to
   position 2;
3. the face is past its Page time from the release;
4. at D14's end, r_h = 2.91 l5, what is left to purify is at most the end's own 176 bits.

So our universe's evolution over the hole's life is unitary, and the information leaves in the radiation.

**Hypotheses.**
- (H1) The theorem's geometry. At the small end the face is five-dimensional Tangherlini: T = 1/(2 pi r_h), E = 3 pi
  r_h^2/(8 G5), S = pi^2 r_h^3/(2 G5), with S0 = N ln2 at the release (H1 of the register). At the large end it is
  four-dimensional Schwarzschild on the plane: T = 1/(4 pi r0), E = r0/(2G).
- (H2) The face radiates on the plane as four-dimensional black-body radiation: entropy (4/3) dE/T (passage_est Q4's
  channel).
- (H3) Theorized: the quantum extremal surface prescription, S = min over candidate surfaces of A/4G + S_bulk, with
  Penington's near-horizon treatment of the outgoing modes.
- (H4) M's rulings 336 (the energy stays in our universe) and 386 (only information travels).

## 2. Proofs

**P1 (I1; computed exact, proved).** P is proportional to r_h^2 T^4, which is proportional to r_h^-2. E is
proportional to r_h^2, so P = k/E. Then dE/dt = -k/E integrates to E^2 = E0^2 - 2kt = E0^2 (1 - t/tau), with tau =
E0^2/(2k) = E0/(2 P0), the life.
- S is proportional to r_h^3, so to E^(3/2): S/S0 = (1 - t/tau)^(3/4).
- r_h is proportional to E^(1/2): dr_h/dt = (r_h/2E) dE/dt = -r_h k/(2E^2) = -r_h/(4 tau(t)), with tau(t) = E^2/(2k)
  the life remaining.
- The bulk channel, r_h^3 T^5, is also proportional to r_h^-2, so the same law holds whichever channel carries the
  energy (I1's second check).
- Control: the four-dimensional E proportional to r_h gives a different exponent (mutant "eofr", caught).

**P2 (I2; computed exact, proved).** The first law gives the hole dS = dE/T. Four-dimensional black-body radiation has
entropy density s = (4/3) u/T, so radiation emitted at the hole's temperature carries dS_rad = (4/3)|dE|/T =
(4/3)|dS|. Integrating from the release gives S_H(t) = (4/3)(S0 - S(t)).
- Page's crossing S_H = S is at (4/3)(1 - s) = s, s = S/S0 = 4/7.
- By P1, t_P/tau = 1 - (4/7)^(4/3) = 0.52581.
- At the example README, S0 = N ln2 = 1.90100e15 nats, so the crossing value is (4/7) S0 = 1.08629e15 nats.
- Control: radiation carrying only the hole's own entropy (ratio 1) gives s = 1/2 and puts the surface on the horizon
  (mutant "ratio1", caught).

**P3 (I3; READ, computed exact, proved).** Penington (1905.08255v3, READ) gives the surface's radius in an
evaporating hole, his (66):

    r_hor - r = (2 G beta / (pi (d-1) Omega r^(d-2))) [beta dM/dv + dS_out/dv - dS_in/dv]

with r_hor = r_s + (beta/2pi) dr_s/dv (his (16)), where r_s is the apparent horizon.
- With no infall, dS_in = 0.
- The first law gives beta dM/dv = dS_BH/dv = ((d-1) Omega r^(d-2)/(4G)) dr_s/dv, which is negative.
- The radiation carries dS_out/dv = q |dS_BH/dv|.
- So the bracket is (q - 1)(d-1) Omega r^(d-2) |dr_s/dv|/(4G), and

    r_hor - r_QES = (q - 1)(beta/2pi)|dr_s/dv|,    r_s - r_QES = q (beta/2pi)|dr_s/dv|.

At q = 2, Penington's two-dimensional case, the second is (beta/pi)|dr_s/dv|: his (42) exactly ("twice as far inside
the apparent horizon as the event horizon", p. 22, READ). This is i3_info's check twoD = (1, 2). Dropping (d - 1) breaks
it (mutant "dfac", caught).

At the small end, beta/2pi = 1/(2 pi T) = r_h, |dr_h/dv| = r_h/(4 tau) (P1) and q = 4/3 (P2). With the life tau =
8.57e14 clocks of r_h/c (hold_small, computed there):
- inside the event horizon: (r_hor - r_QES)/r_h = (1/3)/(4 x 8.57e14) = 9.72e-17;
- inside the apparent horizon: (r_s - r_QES)/r_h = (4/3)/(4 x 8.57e14) = 3.89e-16.

The surface's infalling time is v = -(beta/2pi) log(S_BH/c_evap) + O(beta) (his (41), (44)), so it lies r_h ln(S0/c_evap)
back: 35.18 r_h at c_evap = 1 and 30.58 r_h at c_evap = 100.

There the curvature place is x_h to one part in 1e16, and QB departs from the classical interior by (x_h/x_b)^2 =
2.6e-18 (z3q Q5; BOUNCE-PROOF.md). So (66), derived on the classical near-horizon metric, applies, and the island
inside the surface lies in our face's classical interior. Position 2's face closed at the release, at most 2 r_h/c
after the write (face2_release). So the island is our face's, in our universe: nothing crosses (336, 386).

**P4 (I4; READ, proved on H3).** Through the write, the inflow is the plane's radiation at T_H (passage_est Q4), so T'
= T. Penington, Appendix B (READ): "When the infalling modes are at the same temperature as the black hole, the
Ryu-Takayanagi surface lies exactly on the event horizon", and "the black hole entanglement entropy stays constant".

Before the surface takes over, the hole's entanglement with what lies outside it is the empty surface's bulk entropy:
- it grows by the outflow's entropy, N ln2 over the write: at the balance E_out = E_in, so (4/3) E_out/T = N ln2 (Q4);
  with the bulk gravitons it is (1 + b) N ln2, b = 0.0062;
- it grows by the inflow's entropy as well, if the inflow is counted thermal, entangled with its source.

Either way it reaches S0 by the release:
- at 1/2 of the write if the inflow is thermal;
- at 1/(1 + b) = 0.9938 of it if the README arrives as a pure state.

From there the quantum extremal surface, on the horizon at T' = T, gives S0 and holds it. So the face's entanglement
entropy at the release is S0, never more.

**P5 (I5; proved).** By Penington's (2), S = min(S_rad, A_hor/4G). With entanglement S_init carried in from before the
release, the empty surface's generalized entropy after it is S_init + S_H(t), so

    S_hole(t) = min(S_init + S_H(t), S(t)).

- With S_init = S0 (P4): S0 + S_H(t) >= S0 >= S(t), so S_hole(t) = S(t) for all t >= 0. The face is past its Page
  time from the release, and every quantum it radiates carries information out.
- The bracket's other end, S_init = 0, gives P2's Page time 0.526 tau.
- In both cases S_hole(t) <= S(t), on i3_info's grid and identically.

**P6 (I6; computed exact, proved).** At D14's end, r_h = 72^(1/4) l5 (b4d_small D13): S = 2 pi^2 r_h^3/(4 l5^3) =
(pi^2/2) 72^(3/4) = 121.97 nats = 175.97 bits, D14's 176.
- By P5, at the end the radiation's fine-grained entropy equals S_hole <= 176 bits. What completes the end, complete
  evaporation or a remnant of at most 2.05 J (D14), has at most its own capacity left to purify.
- Read semiclassically, without the island, the end would have to purify N ln2 = 1.901e15 nats: 1.56e13 times its
  capacity.

**P9 (I9; computed exact, proved).** At the large end E = r0/(2G) and T = 1/(4 pi r0), so P is proportional to r0^2 T^4,
which is proportional to r0^-2 = E^-2.
- dE/dt = -k/E^2 gives E^3 = E0^3 (1 - t/tau), tau = E0^3/(3k).
- S is proportional to E^2, so S/S0 = (1 - t/tau)^(2/3).
- Page at s = 4/7 (P2): t_P/tau = 1 - (4/7)^(3/2) = 0.56804.
- beta/2pi = 2 r0, and dr0/dt = (r0/E) dE/dt = -r0/(3 tau(t)).
- By P3 the surface lies inside the event horizon by (1/3)(2 r0)(r0/(3 tau)) = (2/9)(r0/tau) of r0, and inside the
  apparent horizon by (8/9)(r0/tau).
- The life is at least 2.417 N clocks of GM/c^3 (close_large L3), that is 1.2085 N light-crossings of r0. So the
  offsets are at most 0.184/N and 0.736/N of r0, a scrambling time 2 r0 ln S0 back.
- There QB departs by (x_h/x_b)^2 = 1.4e-80 (z3q Q5).

As the large face shrinks it passes, one member for each N, through GMID's family into the small end. There P1-P6
carry it to its end.

## 3. Numerical computations

None beyond the evaluation of closed forms. The life, 8.57e14 clocks, is hold_small's (computed there, cited). The
figures above are i3_info's outputs.

## 4. Theorized, named

- **(T1) The island formula in our setting.** Penington derives it in AdS/CFT with absorbing boundary conditions, the
  radiation extracted into a reservoir. Penington himself (p. 6, n. 7, READ): "The Page curve cannot be found using the
  semiclassical bulk description alone, because it results from the build-up of non-perturbatively small effects".
  Geng and Karch (2006.02438v2, READ): "All reliable calculations of the Page curve in more than 2+1 spacetime
  dimensions have been performed in systems with massive gravitons ... if one attempts to take the limit of zero
  graviton mass, any contribution from the islands disappears". Our plane carries a massless graviton, so this bears on
  us directly. Laddha, Prabhu, Raju and Shrivastava (2002.02448v2, READ): the fine-grained entropy of a segment of null
  infinity is independent of its end, "very different from the oft-discussed Page curve". On their reading the
  evolution is unitary too, with the information outside throughout and no Page curve.
- **(T2) Penington's near-horizon treatment carried to our face.** His outgoing modes are a two-dimensional s-wave
  field with evaporation rate c_evap. Carried to a five-dimensional hole radiating on the plane, it can move the
  offsets by order-one factors and the logarithm's argument by c_evap. It does not move P5's bound.
- **(T3) The ratio 4/3.** It is the black body's. Greybody factors move it by an order-one fraction, and the Page time
  and the offsets move with it. P5's bound S_hole <= S(t), and P6, do not depend on it.

## 5. What the theorem then states

Clause (I) is expanded, not narrowed. Over the hole's life after the release, our universe's evolution stays unitary
on the island formula: the face's fine-grained entropy never exceeds its area's, the information leaves in its
radiation, the island lies inside our face on the classical interior, nothing crosses, and the end holds at most its
own 176 bits. D14's choice, complete evaporation or a remnant of at most 2.05 J, stays the quantum region's, and either
is consistent with it.
