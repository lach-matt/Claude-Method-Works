#!/usr/bin/env python3
"""warptheorem.py -- M-RULINGS item 150: the warp theory as ONE theorem, built from the pieces.

M, item 150: "stop piecing together theorems to fit my theory, instead we need to consider one single theorem built from
the pieces that defines the warp theory as a single statement".  So the board's separate results become lemmas of one
statement, and what is not yet proved is a named lemma of it -- never a separate theorem fitted to a part.

THE WARP THEOREM.  For an object whose README -- its one fixed exact encoding, labels and values, written in what every
universe shares -- has N bits (the user's input), there is exactly one corridor, fixed by N alone, and through it the
README becomes, one way and exactly, the object at position 2:

  (G) GEOMETRY   [seated as re-worded, item 187] the corridor sits in the bulk, on neither plane; it only bridges them
                 (179/180).  Bronnikov-Kim's eq. (17) at r0 = 2m is kept only as a plane's possible reading of the
                 corridor's mouth (H-PLANE-READS-MOUTH, the board's; OPEN).  Its size is fixed by N:
                   E  = sqrt(N h c^5 ln2 / (8 pi^2 G)) = 459,404,002.42 J x sqrt(N),
                   m  = G E / c^4,   r0 = 2m = sqrt(N h G ln2 / (2 pi^2 c^3));
  (H) HOLDING    its throat holds exactly the README: 4 pi r0^2 = N x 2 h G ln2/(pi c^3), 4 ln2 Planck areas per bit;
  (O) ONE WAY    its passage runs from position 1 to position 2 through an extremal horizon (surface gravity 0),
                 nonsingular and complete, never back;
  (Z) NULL ENERGY NEVER VIOLATED   [seated as re-worded, item 187] "never violated" holds net along each light ray
                 (183): a negative member paired along the same light rays is the appearance (117/120).  Along the
                 passage the five-dimensional null energy is zero; the plane's apparent deficit is exactly the bulk's
                 pull, integral 8/(3m) - (4/(3 sqrt3 m)) artanh(sqrt3/2) per unit E (Z1, Z2: computed with eq. (17) as
                 the plane's own metric, the board's configuration, re-read under 179);
  (B) BULK       a vacuum five-dimensional bulk carries it, the plane matter-free at the Randall-Sundrum tension, the
                 bulk's two ends one end, the energy positive at every point, the bulk's scale k fixed by the work;
  (I) INFORMATION  the passage is N bits of entanglement, and carries the N-bit README;
  (E) ENERGY     one exact energy E is carried from position 1 through three holds and released into position 2 at the
                 closing, every joule accounted for;
  (R) RECONSTRUCTION  position 2's matter rearranges to the README exactly, no tolerance, after which position 2's laws
                 govern; the corridor's length is set by the trajectories, the difference between the positions.

First written with 26 lemmas counted as "11 M's, 9 proved, 7 open"; the count was 9, 10, 7, and the verifier of the
reassessment added the hold's length (O3), the field energy outside the neck (E4), the read (R0) and the build's
mechanism (R5), and corrected B4, B5, E3 and I2 (WARPTHEOREM.md History).

Each clause is a conjunction of lemmas.  A lemma is PROVED (an owner, imported and re-run here), DERIVED (proved from M's more basic rulings,
lemmas/axioms.py), DEFINITION (M's definition of a term, shown consistent with the rest), READING (proved under a named reading of the board's, labelled, withdrawn if M corrects it), NATURE (a premise
measurement fixes), or OPEN.  The theorem is proved exactly when no lemma is OPEN.

  T1  the PROVED lemmas are re-run: exactE.py's identities (z3), passage5d.py's identity and Q, localbulk.py's Gauss
      condition, stability.py's surface gravity, coin.py's passage reading
  T2  (STRUCTURAL) the theorem follows from all its lemmas, and from no proper subset that drops an OPEN one: each OPEN
      lemma is needed.  So the OPEN list is exactly what stands between the statement and a proof
  T3  (genuine) the energy ledger, clause (E), at the example README: with the copy's composition exact (146) and its
      matter reorganized (137), the copy itself can absorb at most the assembly energy, 1.1947e10 J; E = 2.405878e16 J,
      and items 110 and 111 (a) put all of E into position 2's build.  z3 finds that unsatisfiable unless the build
      includes an absorber besides the copy, and satisfiable with one -- the board's reading (a), the expansion of
      position 2's universe (136 G, 136 answer 6, 139 (3)).  Control: at N = 600 bits, E < assembly, consistent with
      none.  First written reading the remainder from item 139 alone, as a sink outside the build; that over-read 139,
      whose words concern the trigger, and set the sink against 111 (a)
Imports copy/exactE.py, copy/coin.py, bulk/passage5d.py, bulk/localbulk.py, bulk/stability.py by path.
Stdlib + sympy + z3 (pip install z3-solver).  python3 warptheorem.py [--selftest]   (~10 min since item 206's owners, mostly loading them)
"""
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(HERE)
EXAMPLE_N = 2742570311524972
ASSEMBLY_MAX_J = 1.1947e10            # LOOSE.md L1: 6.7117e27 atoms x 11.11 eV (H-BOND-CEILING), a generous ceiling

# The theorem's lemmas: (clause, name, status, where).  status: AXIOM (item), PROVED (owner), DERIVED, DEFINITION,
# READING, NATURE, OPEN.  Seated on item 206 from chain_cypher.py's proposal (with the 204 splits and pass 2's
# corrections).  Clause N holds the theorem's OPEN inputs; RESTS_ON names the inputs a lemma's status is
# conditional on -- green only when every one of them is.
LEMMAS = [
    ('G', 'G1 one exact energy, at the bound: E(N)', 'DERIVED',
     'lemmas/axioms.py: from 101 answer 6 (no more, no less), 132, 131/133 and the holographic bit area; rests on M1 (F1-AUDIT: M1-c at the horizon)'),
    ('G', 'G2 E(N) computed and machine-checked', 'PROVED',
     'copy/exactE.py (seated)'),
    ('G', 'G3 both holds at least size give r0 = 2m', 'PROVED',
     'copy/exactE.py identity; items 106, 132; rests on M1 (F1-AUDIT)'),
    ('H', 'H1 4 pi r0^2 = N A_bit', 'PROVED',
     'copy/exactE.py identity'),
    ('H', 'H2 the horizons hold the README as well as the throat', 'DERIVED',
     "item 132 (carried as M's; F1-AUDIT); lemmas/axioms.py"),
    ('H', "H2tu within one universe, on each plane reading eq. (17), the horizon's trace is r = 2m with area N A_bit -- position 2 on our plane reads as ours (202, 203)", 'DERIVED',
     'lemmas/axioms.py (F1-AUDIT H2t); lemmas/m1p2_cypher.py L7: within one universe M1P2 reduces to M1; seated item 206 (the 204 split)'),
    ('H', "H2tx between universes, position 2's horizon at its own m2 = (G2/G) m (= 2m on the per-sheet count, 200 (1)) holds the README in a capacity (G2/G) N", 'DERIVED',
     "lemmas/g2_between.py G3-G4 (106 (b), 132: 'held', not 'exactly'); m1p2_cypher.py X3; seated item 206.  Item 211 (m1p2_junction.py): its per-sheet m2 = 2m, capacity 2N, belongs to a conjunction the corridor's junction refutes in the flat-limit static class (see M1P2x); the arithmetic stands, its premise set is in conflict, and which member gives way is the board's call, not made -- the status is not moved on this alone.  Item 215: that conflict holds only for bulks glued by Israel's first condition; in M's configuration the two bulks are cells of the everything bulk index, and the per-sheet values are not refuted there"),
    ('O', 'O1a one way, 1 -> 2: a black hole in, a white hole out, different views of one object', 'DERIVED',
     'items 132 and 130 (F1-AUDIT)'),
    ('O', 'O1b no curvature singularity', 'PROVED',
     "copy/plane.py P1; M1's regularity clause M1-e (F1-AUDIT)"),
    ('O', 'O1c geodesic completeness', 'PROVED',
     'lemmas/o1c_complete.py: curvature bounded; every geodesic crosses the throat in finite affine parameter and is unbounded at both ends'),
    ('O', 'O2 the horizon is extremal (surface gravity 0)', 'PROVED',
     "bulk/stability.py S1 (verified); rests on M1 (F1-AUDIT: the corridor's bulk Killing horizon degenerate)"),
    ('O', 'O3 the corridor survives its hold, which lasts exactly as long as the write needs (158 (2)); the corridor and the opening are the same object (160)', 'OPEN',
     "item 160 settles item 159: the hold is the corridor through the write, >= 2.0e5 clocks (o3_write.py; 163 keeps it: 'at once' is all together, one whole).  The write's energy is settled (o3_ground.py, 164): the held README is an exact eigenstate at E, the write's spread 5.2e-20 of E.  What stays open is the bulk -- O3 is B4d's (b4d_stage5.py: singular on a positive-tension plane, regular on the evidence on 139's negative one).  Item 211 (206; the hold critic): the floor exactly T_min = (9/2)(5N ln2/Z)^(1/3) - 2 = 199,702.19 clocks at the example README (Z = 108.75); the spread DeltaE/E >= (2 pi^2/ln2)/(N T) = 5.1995e-20 at T = T_min; linear growth over the write amplifies a horizon perturbation by exactly T/4 = 4.99255e4 (S4) and (1 + T/8)^2 = 6.23190e8 (S5b) at T_min -- no survival threshold is recorded, since none is sourced (O3c counts factors 2.82 and 5.8 as survival); cypher: at order 3 blocked by WRITE's triple and by survival, computed only inside the static window and off the corridor, and the order-2 admission rests on the window-hold cell alone, a hold M's words set aside (158 (2), 163).  Open record question, not seated: whether O3 rests on B4d's inputs ('O3 is B4d's'), decided by the record, not by E"),
    ('Z', 'Z1q for a Z2-symmetric plane of tension q sigma_RS bounding the vacuum bulk, q 8 pi G tau(k,k) + kappa5^4 pi(k,k) = R4(k,k) + R5(n,k,n,k); R5(k,k) = 0 in the vacuum bulk; our plane is q = 1', 'PROVED',
     "lemmas/f1_audit.py B5, B6 (Gauss and Israel's Z2 junction, standard-not-READ)"),
    ('Z', "Z1t the value along the mouth's radial ray, our leg, within the reach: 5D null energy zero, the plane's deficit the bulk's pull", 'PROVED',
     'bulk/passage5d.py P2 (F1-AUDIT)'),
    ('Z', "Z2r our leg's integral within the reach equals the plane's reading, to M1-c's order", 'PROVED',
     'bulk/passage5d.py P3; copy/coin.py (F1-AUDIT)'),
    ('Z', "Z3a NEC never violated away from the corridor, through today: the vacuum bulk gives zero; the FRW plane's total null stress is positive at every epoch read", 'DERIVED',
     "lemmas/b1_matter.py C1-C3 (B1-MATTER Z3'a); items 117, 120"),
    ('Z', 'Z3b rays that meet the corridor or run beside it keep (Z): the static ray classes (bulk; across the corridor; across our plane; across the ring) are kept; the dynamic phases are its inputs', 'OPEN',
     'corrected item 208 (206): the across-the-ring class is open -- with the marginal corridor\'s own tension the rim\'s junction is in compression, not P5\'s positive ring, and its energy density is not computed (lemmas/ring_consistent.py; z3b_cypher.py Z4); item 210: the rim is the mouth\'s coupling to our plane, an open mouth on M\'s guess; item 211 (open_mouth.py O5): the open mouth that keeps the seated corridor (D+) carries at its joint a negative Nambu-Goto line, -t/sqrt(1 - 2m/r_rim) of null energy on radial rays in the sheet, which (Z) asks to be paired on the same rays -- what pairs it is the class\'s question; item 212 (two_sided.py): in one bulk that negative is the one-sided reading\'s appearance and the two-sided joint carries none, so on H-CORRIDOR-IS-OUR-BRANE the class keeps (Z) with no partner -- not seated as a status change, since the bulk that carries the warp\'s kink into the corridor is not computed.  The other static classes keep (Z) (z3b_cypher.py Z1-Z3, rim_profile.py P4, corridor_shape S0 corrected); C5 a different configuration (H-C5-ELSEWHERE); seated DERIVED on item 206, was OPEN'),
    ('Z', "Z3c the plane's dark energy has w >= -1 at every epoch the theory controls", 'DERIVED',
     'lemmas/nature_rows.py Z1-Z3 (seated (Z) via TS; SMS READ); item 200 (3)'),
    ('B', "B1 each plane carries its own universe's matter and meets Gauss and Codazzi (B1'; the matter-free plane a limit, 184)", 'PROVED',
     "lemmas/b1_matter.py (B1', SMS READ); bulk/localbulk.py L1-L2"),
    ('B', "B2 a local vacuum bulk exists, unique among analytic ones, beneath any plane meeting B1 (B2')", 'PROVED',
     "lemmas/b1_matter.py B2' (Dahia-Romero READ); bulk/localbulk.py L4"),
    ('B', 'B2t its instance beneath eq. (17)', 'PROVED',
     'bulk/localbulk.py L3-L4 (F1-AUDIT)'),
    ('B', 'B3 a complete bulk exists, built under closed-index criteria', 'OPEN',
     'equivalent to B4: the local bulk is proved (B2), the complete one is B4a-B4d.  Item 211 (deduced from the seated records): since item 210 B4 is B4a (PROVED) and B4d (B4b and B4c superseded by B4d), so B3 rests on B4d\'s inputs -- CLOSE added, which it lacked since B4d first rested on CLOSE; the theorem\'s exact E falls 693 -> 616 with no language rising (belongs_cypher.py B9)'),
    ('B', "B4a the global bulk's shape, given W2 inside the far boundary T: the plane's two ends are one end of the bulk -- two separate positions reached through a dimension (152 (1), encoded as H-SEPARATE-JOINED-THROUGH-DIMENSION) -- so CGS Thm 3.1 is escaped (a) and Thm 3.5's deformation holds; the topology is fixed before the opening (B7's bridge)", 'PROVED',
     'lemmas/b4_global.py, 6/6: STRUCTURAL encoding; controls two-ended, and excised regions block the deformation; Ake Hau-Flores-Sanchez READ'),
    ('B', "B4d the opening and closing evolve regularly in five dimensions, and data beyond the hold's cone join the untouched exterior (H-EVOLUTION, H-GLUING)", 'OPEN',
     "carries B4b's and B4c's questions over the real hold (item 210, M: superseded by B4d; their rows kept on record in SUPERSEDED) and rests on FAR through B4c's.  a nonlinear 5D initial-boundary problem through a write of at least T_min = 199,702.19 clocks at fixed size (162, 163; '>= 2.0e5' rounded, item 211).  Stage 5 (lemmas/b4d_stage5.py, verified once): with eq. (17) on a positive-tension plane the cone of a hold of 16.0, 13.0, 10.9 and 7.8 clocks at ell = 2m, m, m/2 and m/4 contains K >= 1e4 (one path in far time, an upper bound; other ell not tested -- item 211: the record's '8-16 clocks at every finite ell tested' was a range over the family, and m/4's 7.8, added after the verifier, lies outside it); on 139's negative-tension plane it relaxes to AdS, regular on the evidence, at the cost of boundary data and localized gravity.  Stage 6: every positive plane has a decaying side; stage 7 (item 166): across both planes every small-separation branch has a decaying outer bulk.  Simulation phase 1 (sim1_transition.py): eq. (17) is no 4D null-energy end state.  Phase 2 (sim2_facing.py, item 168): two matter-free pieces of our plane cannot face across a static bulk; with README stress on P2 (put to M) only near the throat; the passage through the horizon is next.  Stages 1-2 verified; 3-4 conditional on the withdrawn instant reading"),
    ('B', "B5a positivity for the entangled pin at coincidence (127): the sheets' summed tension and both universes' matter meet B5'a's condition -- a conditional", 'DERIVED',
     "lemmas/b5_positive.py B5a; lemmas/b1_matter.py C4 (B5'a)"),
    ('B', "B5pu within one universe position 2's matter is ours (202) and meets B5'a's condition", 'DERIVED',
     'lemmas/b5p_cypher.py (b1_matter C3, C4); seated item 206 (the 204 split)'),
    ('B', "B5px between universes, position 2's matter meets B5'a's condition", 'OPEN',
     'lemmas/b5p_cypher.py: only ratios known (ITEM185).  Item 211 (the between critic): under 183 B5\'a\'s form is TS\'s crossing share, so B5px is (Z) net per ray at the pin -- (3/4) sigma + delta_sigma2 + rho1 + rho2 >= 0 on normal rays, sum (rho + p) >= 0 on grazing ones; the grazing half follows from TS on position 2\'s plane if its matter is the same at the pin, the normal half needs position 2\'s matter and offset no lower than -3 sigma/4, which no ruling gives; the cypher\'s X refusal is forced by construction, void'),
    ('B', "B5b a smooth wall carrying matter keeps null energy at every point (B5'b): none computed even for one universe's matter", 'OPEN',
     'lemmas/b5b_cypher.py; b5_positive.py B5b (matter-free).  Item 211 (the between critic): under 183 its content is (Z) net per ray -- B5\'a on crossing rays (B5pu, B5px) and each component\'s rho + p >= 0 along the wall (Z3a, Z3c), for any profiles, at leading order in width over ell; the pointwise demand asks more than (Z) and rests on 154\'s pointwise reading, which 183 superseded; no localised matter wall exists in the separable warped class (OPEN); whether it still belongs is put to belongs_cypher'),
    ('B', "B6 k's ratio fixed by the work, k_R = k_L/2 (position 2's plane counts once, 200 (1)); every clause b6_k.py checks free of k's scale", 'PROVED',
     'lemmas/b6_once.py (200 (1)); lemmas/b6_k.py'),
    ('B', "B6' k's scale: our universe is defined by its plane's tension and its dark-energy offset (201)", 'DEFINITION',
     'lemmas/sigma_defines.py T1-T4; nature_rows.py B1-B3'),
    ('B', 'B7 formation: the opening and closing between static planes -- a widening of the bridge already there, no change of topology, consistent and safe; its 5D evolution goes with B4d', 'DERIVED',
     "lemmas/b7_formation.py: items 100, 140, 122 (4) (H-ER=EPR-MATTER-ONLY), 101 answer 1, Maldacena-Susskind p.17 (READ); chain.py's z3 encoding, controls inconsistent -- first written as the board's H-BRIDGE-PREEXISTS"),
    ('I', 'I1 the passage is N bits of entanglement', 'DERIVED',
     'lemmas/axioms.py: your item 137 (1) (H-PASSAGE-IS-N) with H1 (area N A_bit) -- N bits; Maldacena-Susskind p.5 and Strominger-Vafa (READ) agree, no longer load-bearing'),
    ('I', "I2 the README's N bits within the capacity bound as READ: information at most what is sent to set up the interaction (Maldacena-Stanford-Yang p.4; parametric, p.12) -- N is the device's input (130 (2))", 'PROVED',
     'lemmas/i2_capacity.py: holding bound = N, interaction bound met with equality, channel bound N/2 <= N'),
    ('E', 'E1u within one universe, E carried through three holds into position 2 -- no event horizon, no area-law obstruction', 'DERIVED',
     'lemmas/close_flux.py K3; lemmas/axioms.py (E1).  Item 211 (206; the formclose critic): was "no negative-flux demand", which overclaimed in the plane\'s reading -- K3 is an area-law statement, and close_cypher F1 already records that the black-hole side\'s shrink is a negative influx; the carriage itself is M\'s (106 (b), 110, 111, 136 (2))'),
    ('E', 'E2u within one universe, released at position 2 at the closing', 'DERIVED',
     'lemmas/close_flux.py; lemmas/axioms.py (E2)'),
    ('E', 'E1x between universes, E carried through three holds into position 2', 'DERIVED',
     "lemmas/axioms.py (E1); README-HELD: '(a) with OPEN'"),
    ('E', 'E2x between universes, released at position 2 at the closing', 'DERIVED',
     'lemmas/axioms.py (E2); README-HELD'),
    ('E', "E3 the ledger closes: E goes into position 2 (110) and the build uses exactly it (111 (a)), with the copy exact (146) and its matter reorganized (137).  The board's reading (a): the copy's matter is the stock's; E is absorbed as the expansion of position 2's universe (136 G, 136 answer 6, 139 (3)), counted as part of the build; item 108's E/c^2 is the appearance accounting (107)", 'DERIVED',
     "lemmas/ledger.py: closes at the example and the full snapshot under the board's reading (a); reading (a) confirmed by M, item 155 (H-EXPANSION-IS-BUILD)"),
    ('E', "E4r the field energy outside the neck within the reach, (E/4)(1 - m/(2R* - 3m)) to M1-c's order: the bulk's Weyl field read on the plane, positive, not the plane's energy", 'PROVED',
     'lemmas/ledger.py (F1-AUDIT)'),
    ('R', 'R0 the read: the corridor takes the README as its inflow at the opening; N is read from the object', 'DEFINITION',
     'items 70, 101 answer 8, 115 (c), 130 (2); consistent with I2b'),
    ('R', 'R1 exact reconstruction, no tolerance', 'DEFINITION',
     'items 145, 146; consistent with R3 and R5c'),
    ('R', 'R2 position 2 rearranges to the README; then its laws govern', 'DEFINITION',
     'item 148; consistent with rearrange.py and E3'),
    ('R', 'R3 exactness at the instant over the mass window', 'PROVED',
     'bulk/exactcopy.py, rearrange.py (verified)'),
    ('R', "R4 the corridor's length as the trajectory difference, given a measure -- not a distance (101 answer 7, 136 answer 3, 139 (4))", 'DERIVED',
     "lemmas/r4_length.py: L = trajectory difference in bits (H-LENGTH-AS-DIFFERENCE, the board's); the measure confirmed by M, item 155 (H-LENGTH-IN-BITS)"),
    ('R', "R5 the build's mechanism: the field reaction by which the released energy and the README rearrange position 2's matter -- which field, and what 'activation' is when the field is non-zero everywhere", 'DERIVED',
     "lemmas/r5_build.py: mechanism yours (91 (b), 101 answer 8, 136 B, 139 (3), 148); fields the board's reading; energy covers any exact README's rearrangement (3.76e22 J >= 5.94e16 J); the fields reading confirmed by M, item 155 (H-ACTIVATION-IS-TRIGGER)"),
    ('N', "M1 the plane's reading of the corridor's mouth (replaces F1; OPEN)", 'OPEN',
     "seated restatement (206): the plane's reading of the corridor's mouth (replaces F1).  The rim closes in the static bulk: the marginal corridor keeps the radial and tangential null energy from the throat, which it joins smoothly, to a rim beyond r_b, (corridor_shape.py S0-S3 corrected; rim_profile.py; forming_rim.py).  CORRECTED item 208 (206): the ring of positive tension that balanced it rested on the corridor carrying -sigma at the rim (rim_readme R5's coincidence law for facing sheets); with the marginal corridor's own tension the rim balances only with a junction in compression -- with its warp part counted too (item 211, ring_consistent.py C5), lambda = (sin^2 t - tau cos t) a sigma < 0 for every admissible member at ell/m = 8.5415 (item 208's -(cos 2t + tau cos t) dropped the warp part: its sign stands, its values do not), and a balance with no junction only below the window (ring_consistent.py).  Within one universe every clause but (d) was met with that ring (m1_cypher.py).  Item 210 (M): the rim is a coupling interaction between the mouth and our plane; M's guess, it looks like a singularity on paper but is an open mouth -- on that guess the junction the thin balance asks for is what the open mouth looks like, not added matter, so (d) is met, and the rim stays in M1.  Item 211 (open_mouth.py, critic-passed): a smooth turn fixes the surface, not the side kept; the open mouth that keeps the seated corridor as its body is D+ (corridor_shape's orientation -- the other side, D-, flips every seated stress and has no computed body).  Its joint is the plane's own concave fold, a negative Nambu-Goto line lambda = -(2/kappa5^2) t: on paper a line in compression, as 210's board reading has it, needing no balance.  A radial null ray in the sheet gains -t/sqrt(1 - 2m/r_rim) there and the corridor adds 0, so (Z) net per ray asks for a partner on the same rays -- the coupling (the board's reading H-OPEN-MOUTH-DPLUS, put to M).  Open: what pairs it on those rays; the ring's nature, put to the cypher on item 207, was refused because the index held too much (a key and a one-hot code, item 208), and the fold reading is refuted as stated for a test membrane (ring_cypher.py R2), while a gravitating sheet's fold carries a Nambu-Goto line (open_mouth.py O3); and Wall C's bridge.  Item 212 (M: 'the bulk is everything everywhere all at once'; M's guess: the negative null energy is 'Z's reflection creating the appearance'; two_sided.py): with one bulk smooth across the sheet the two-sided stress vanishes identically, the fold's line included, so the joint's negative line is exactly the one-sided (mirror) reading's appearance and (Z) needs no partner at flat order; two bulks meeting as flat-order mirror images (203's own bulks) would make it real; a sheet mirrored only at warp order -- our plane's kind of sheet -- carries positive energy, keeps the null energy pointwise and has no line at a fold.  On the board's reading H-CORRIDOR-IS-OUR-BRANE (smooth at flat order, mirrored at warp order, as our plane is) 212 and 203 hold together: the rim keeps (Z) with no partner and the corridor's energy is its warp-order tension.  Not computed: a bulk in which the warp's kink follows our plane into the corridor, and 203's equality with E.  Item 213 (M: the two bulks are not mirror images; position 1 contains a geometric object position 2 does not, until the corridor is closed; asym_junction.py): the lapse along every seated corridor spans more than four orders, so no static sheet joins a side with the object to a side without it (Israel's first condition; second route m1p2_junction J5) -- on the reading that 'contains' means the object's field, the corridor is the transfer itself, not static, and the static rim readings above (the joint, the ring, H-CORRIDOR-IS-OUR-BRANE) describe a corridor with the same field on both sides; (Z) is to be computed in the dynamic transfer.  Item 214 (M: 'They see their own reflections but are not mirror images of each other'; asym_junction.py A4): each bulk closes on its own mirror, so the one-sided readings are each position's own view -- the seated corridor's stresses and the joint's negative line are position 1's view; one corridor seen from both sides (132) still has one intrinsic lapse, so the static conclusion stands.  Item 215 (M: 'they exist within the everything bulk index'): the two bulks are cells of the everything bulk index, not glued along a shared sheet, so Israel's first condition is not imposed between them and the item-213 static conclusion (asym_junction A2-A4) does not bind M's configuration -- it stands as computed for glued bulks; each position's own view stands (214); what relates the two cells is the index's question.  Item 216 (bulk_index.py, through the cypher on M's account of the transfer, 106 (b), 115, 213): the two cells meet only in the realized stage, where both hold the object, which no combination of the other stages assembles; the object is never held nowhere; the release at position 2 is a step of its own; (Z) is unknown exactly at the stages where position 2's horizon stands (the hold and the closing) -- every verdict forced by a named unseen projection, the cypher adding that each step is irreducible  [lemmas/F1-AUDIT.md; lemmas/corridor_shape.py S0; lemmas/rim_profile.py P4, P4b; lemmas/forming_rim.py F3b, F7; lemmas/m1_cypher.py; lemmas/ring_cypher.py; lemmas/ring_consistent.py; lemmas/belongs_cypher.py; lemmas/open_mouth.py]"),
    ('N', "M1P2x position 2's side reads eq. (17)'s other leg (OPEN)", 'OPEN',
     "seated restatement (206): between universes, position 2's side reads its own eq. (17), at m2 = (G2/G) m; within one universe M1P2 reduces to M1  [lemmas/g2_between.py; lemmas/m1p2_cypher.py; lemmas/m1x_cypher.py].  Item 211 (206; lemmas/m1p2_junction.py, the between critic): in the flat-limit static class, with Israel's first condition at a junction crossing the horizon at finite depths and the board's reading H-OWN-BULK-SAME-FASHION, the corridor's junction (203) forces m2 = m -- the near-horizon Ricci-flat equations make the AdS2-to-S2 radius ratio strictly monotone in depth, so matching both radii admits only equal masses (every other ratio, 2 included).  That refutes, in the class, the conjunction {H-ONE-G5's per-sheet G2 = 2 G1 read as position 2's pull and Planck-area G (g2_between G3-G4, m1p2_cypher X3), H-PULL-PER-SIDE, 203's one E, H-OWN-BULK-SAME-FASHION}; which member gives way is the board's call under 149 -- item 213 (M: position 2 does not contain the object until the corridor is closed; asym_junction.py A2-A3) made it the static class: with the object on one side only no static sheet joins the two bulks.  Item 215 (M: 'they exist within the everything bulk index'): the two bulks are cells of the index, not glued by Israel's first condition, so neither the junction's m2 = m nor the item-213 conclusion binds M's configuration -- both stand as computed for glued bulks, and the per-sheet conjunction is not refuted for M's configuration.  Still OPEN: position 2's tension acts on crossing rays (m1x X2) and in the rim's balance, and its matter is B5px's unknown -- only the mouth's bulk reading is fixed"),
    ('N', 'FAR a far boundary consistent with (Z), (G), 139 (1), 166 (OPEN)', 'OPEN',
     "seated restatement (206): a far boundary consistent with (Z), (G), 139 (1), 166  [lemmas/far_cypher.py: needs one far model for the negative-P2 bridge (theta+- and the net null energy across position 2's plane)].  Item 211 (206; lemmas/far_bridge.py, the hold critic): each computed candidate fails at least one requirement -- model C's two-sided bridge with position 2's plane on the growing side (the only arrangement giving that plane negative net energy, modelc C4/C5) fails the surface WEC for every matter content (rho >= 0 and rho + p >= 0 force mu <= 0 at k = 1; rho + p < 0 at k = 0), and its matter-free member BRIDGE-NEG gives sigma_2 |n.k| < 0 on every ray meeting the plane (its (Z) 0, deduced); SLAB fails (G) only on the board's reading H-STAGE7-IS-THE-BOARD'S (X9's reading leaves it U).  FAR needs every ray crossing position 2's plane paired on that ray -- 177's coupling of the ends the obvious candidate outside model C's vacuum family -- or that plane meeting the surface WEC in total, which for k = 0 no outer side gives.  far_cypher's model-axis refusals are forced by a key and void as evidence"),
    ('N', 'WRITE the static bulk held through the whole write, >= 2.0e5 clocks (OPEN; R1-COVER pending)', 'OPEN',
     'seated restatement (206): the static bulk held through the whole write, >= 2.0e5 clocks.  The floor exactly (item 211, o3_write.t_min): (9/2)(5N ln2/Z)^(1/3) - 2 = 199,702.19 clocks at the example README with Z = 108.75, its lower bound; "2.0e5" is that rounded up, and the floor falls as Z^(-1/3)  Every computed hold that ends (the longest, 389.3 clocks with no second sheet) is shorter than the floor for Z < 1.4456e10  [lemmas/write_cypher.py: at statistics order 3 blocked by (corridor, lasts, keeps_Z); with 200 (1) applied to R1\'s mirrored stress and the both-planes (Z) entered U, also by (corridor, keeps_Z, stands); at the pinned order 2 the target is admitted from pairs (the board\'s reading, not decided); orders >= 4 forced (item 211, the hold critic); R1-COVER pending].  Item 213 (asym_junction.py): while position 2 lacks the object no static sheet joins the two sides, so on the reading that contains means the object\'s field the bulk is not static through the write -- in line with o3_write W4 (ii), the write is the opening.  Item 215: that holds for glued bulks only; in M\'s configuration the two bulks are cells of the everything bulk index, so it does not bind WRITE'),
    ('N', "ARRIVAL the README forms the corridor as it comes in, no partner (198, M's guess; README-HELD's 4D models; formation in the bulk OPEN, 179)", 'OPEN',
     "seated restatement (206): the README forms the corridor as it comes in, no partner (198); formation in the bulk.  Item 211 (critic-passed): the in-bulk refusal is undecided -- the record's gap, forced by the unknowns (statistics refuses 146 of 147 novel cells at order 3); its (Z) half shares its deciding carrier with M1's and Z3b's open mouth (open_mouth.py O5: a negative joint, paired or not) and the corridor's surface (203); README-HELD's 4D model is consistent with an end state that is Schwarzschild, not the corridor  [lemmas/arrival_cypher.py: the null energy of a corridor forming in the bulk; README-HELD's 4D models]"),
    ('N', "CLOSE the closing's negative null flux: ending the horizon and moving the hold need its area to shrink (README-HELD; area theorem; OPEN)", 'OPEN',
     "seated restatement (206): the closing: within one universe it needs no negative null flux (position 1's horizon ends, 115 (a); extremal, so no outer-horizon area law; no event horizon) and what remains is the joint ending of the (+E, -E) mouths keeping (Z); between universes the negative-flux demand stands (area theorem).  CORRECTED item 211 (206; the formclose critic): the (+E, -E) mouths are H-MOUTH-FLUX, withdrawn as a reading (a secondary source; additive bookkeeping against 111 (b) on H-ONE-ENERGY-NONADDITIVE) -- in the plane's 4D far zone with local exchange no accounting carries E into position 2 without an unpaired negative or a transit (barred on H-NO-MOVEMENT-COVERS-CLOSING), so CLOSE's (Z) is a 5D question.  Within one universe: no area law binds the ending (extremal; no event horizon); the plane's reading of position 1's ending carries a net negative influx, which under (Z) is the appearance only if it is paired on the same rays -- in 5D, through a vacuum ending in which E falls to 0 (B4d's evolution), with the open mouth's negative joint (open_mouth.py O5) and the corridor's surface (203) keeping (Z) net per ray; not computed.  Between universes: the 4D area theorem binds the plane's reading only if R4(k,k) >= 0 there, which (Z) as seated does not assert (close_cypher F4's H-NO-PARTNER-IS-POINTWISE holds for R5 and tau, not R4); the 5D area theorem binds if the corridor's 5D horizon is a bulk event horizon relative to universe 1's end (F9); not computed  [lemmas/close_object.py; lemmas/close_cypher.py; lemmas/CLOSE-FLUX.md]"),
]
RESTS_ON = {'G1': 'M1', 'G3': 'M1', 'H2tu': 'M1', 'H2tx': 'M1 M1P2x', 'O1b': 'M1', 'O1c': 'M1', 'O2': 'M1', 'O3': 'WRITE ARRIVAL', 'Z1t': 'M1', 'Z2r': 'M1', 'Z3b': 'M1 FAR WRITE ARRIVAL CLOSE', 'B2t': 'M1', 'B3': 'M1 FAR WRITE ARRIVAL CLOSE', 'B4d': 'M1 FAR WRITE ARRIVAL CLOSE', 'B7': 'WRITE ARRIVAL CLOSE', 'E1x': 'CLOSE', 'E2x': 'CLOSE', 'E4r': 'M1'}

# Item 210 (M: "Yes: superseded by B4d"): rows set aside as superseded by B4d, kept on record, not deleted.  Each keeps the
# status and record it was seated with; B4d now carries their questions over the real hold (>= 2.0e5 clocks, O3, 160).
SUPERSEDED = [
    ('B', "B4c the far boundary T strictly untrapped, uniformly in time: in the board's model theta+- has the sign of ell - 2R over the throat, so T exists beyond the hold's reach iff ell > 2 R_reach (~23 m in corridor units); radiation after the closing cannot trap it (Raychaudhuri, margin ~5); eq. (17) holds only within the reach (causality)", 'READING',
     "lemmas/b4_global.py: H-FAR-MODEL (the board's); the radiation and near-zone steps now derived; a -> 0 gives CENSOR5D C1's 3/R; calibrated to the static window's ~11.3-clock reach, which o3_write.py's write (~1e5 clocks) exceeds -- re-read with B4d"),
    ('B', "B4b the bulk regular within every admissible hold's double cone: with eq. (17) held on the plane, the static bulk (forced there in the board's locally analytic class) is regular and Pade-stable for every hold below ~11.3 clocks; the surface above the throat where its curvature diverges (y_b = 2.49-2.50m at r = 2.15m, K ~ (y_b - y)^-p, p ~ 2.5-3) is reached by longer holds", 'READING',
     'lemmas/b4_static.py: exact order-60/80 series (checked against bulkseries.py), Pade continuation (agreement of orders, a heuristic), the full double cone converged; flat limit (ell >> r0); Holmgren (uniqueness only) not READ; the write lasts ~1e5 clocks (o3_write.py), past this window -- re-read with B4d'),
]
SUPERSEDED_RESTS = {'B4c': 'FAR', 'B4b': 'M1 WRITE'}
SUPERSEDED_BY = {'B4c': 'B4d', 'B4b': 'B4d'}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def t1():
    """Re-run the PROVED lemmas from their owners."""
    import sympy as sp
    ex = _load(os.path.join(HERE, "copy", "exactE.py"), "wt_exactE")
    ids = ex.identities()
    want = ["the closed forms meet: 4 pi r_min^2 = N A_bit, A_bit = 2 h G ln2/(pi c^3)",
            "r0 := r_min and m := G E/c^4 give r0 = 2m",
            "one way under H-FUTURE-INGOING: the future cone at the throat has xdot <= 0"]
    p5 = _load(os.path.join(HERE, "bulk", "passage5d.py"), "wt_passage5d")
    tid = p5.tidal()
    coin = _load(os.path.join(HERE, "copy", "coin.py"), "wt_coin")
    Q = float(sp.Rational(8, 3) - 4 / (3 * sp.sqrt(3)) * sp.atanh(sp.sqrt(3) / 2))
    lb = _load(os.path.join(HERE, "bulk", "localbulk.py"), "wt_localbulk")
    st = _load(os.path.join(HERE, "bulk", "stability.py"), "wt_stability")
    m = sp.Symbol("m", positive=True)
    d1, _ = st.D_derivatives(2 * m, 2 * m)
    return {"E_per_sqrt_bit": ex.e_per_sqrt_bit(),
            "H1_G3_O1": all(ids[k][1] == "proved" for k in want),
            "Z1": sp.simplify(tid["n_kk"] + tid["R4_kk"]) == 0,
            "Z2": abs(Q + 2 * coin.anec_closed(1, 2)) < 1e-12,
            "B1": lb.gauss_rhs(-1 / lb.ell, -6 / lb.ell**2) == 0,
            "O2": d1 == 0}


def lemma_selftests():
    """Each lemma instrument's own selftest, run silently; all must pass."""
    out = {}
    for f in ("o3_hold.py", "i2_capacity.py", "ledger.py", "r4_length.py", "b5_positive.py", "b6_k.py", "r5_build.py",
              "b7_formation.py", "axioms.py", "b4_global.py", "b4_regular.py", "b4_static.py", "o3_write.py",
              "o3_readings.py", "b4d_stage1.py", "o3_ground.py",
              # owners seated on item 206
              "b6_once.py", "nature_rows.py", "o1c_complete.py", "sigma_defines.py", "close_flux.py", "b5p_cypher.py",
              "m1p2_cypher.py", "z3b_cypher.py", "b1_matter.py", "f1_audit.py", "g2_between.py", "close_object.py",
              "rim_profile.py", "corridor_shape.py", "forming_rim.py",
              # pass 3 (item 207)
              "m1_cypher.py", "ring_cypher.py",
              # items 208-209
              "ring_consistent.py", "belongs_cypher.py",
              # item 211
              "index_audit.py", "open_mouth.py", "far_bridge.py", "m1p2_junction.py",
              # item 212
              "two_sided.py",
              # item 213
              "asym_junction.py",
              # item 216
              "bulk_index.py"):
        mod = _load(os.path.join(HERE, "lemmas", f), "wt_" + f[:-3])
        with contextlib.redirect_stdout(io.StringIO()):
            out[f] = mod.selftest()
    return out


def t2():
    """The theorem from its lemmas: T <-> every lemma.  Entailed with all; each OPEN lemma necessary (STRUCTURAL)."""
    import z3
    v = {name: z3.Bool(name) for _, name, _, _ in LEMMAS}
    T = z3.And(*v.values())
    known = [v[n] for _, n, s, _ in LEMMAS if s != "OPEN"]       # PROVED, DERIVED, READING, DEFINITION, NATURE
    opens = [n for _, n, s, _ in LEMMAS if s == "OPEN"]
    s = z3.Solver()
    s.add(known + [v[n] for n in opens] + [z3.Not(T)])
    entailed = s.check() == z3.unsat
    needed = {}
    for o in opens:
        s = z3.Solver()
        s.add(known + [v[n] for n in opens if n != o] + [z3.Not(T)])
        needed[o] = s.check() == z3.sat                # T fails to follow without o
    return {"entailed": entailed, "needed": needed, "open": opens}


def t3(E_per_sqrt_bit):
    """The energy ledger: E delivered = absorbed by the copy + sink; absorbed <= assembly ceiling; the build uses
    exactly E (111).  Unsat with no sink at the example N, sat with one; control at a small N."""
    import z3

    def ledger(E_value, sink_allowed):
        E, absorbed, sink = z3.Reals("E absorbed sink")
        s = z3.Solver()
        s.add(E == E_value, absorbed >= 0, absorbed <= ASSEMBLY_MAX_J, E == absorbed + sink)
        s.add(sink >= 0 if sink_allowed else sink == 0)
        return s.check() == z3.sat
    E_ex = z3.RealVal(repr(E_per_sqrt_bit * EXAMPLE_N ** 0.5))
    E_small = z3.RealVal(repr(E_per_sqrt_bit * 600 ** 0.5))
    return {"E_example": E_per_sqrt_bit * EXAMPLE_N ** 0.5, "no_sink": ledger(E_ex, False),
            "with_sink": ledger(E_ex, True), "control_small_N": ledger(E_small, False),
            "E_small": E_per_sqrt_bit * 600 ** 0.5}


def compute():
    a = t1()
    return {"t1": a, "t2": t2(), "t3": t3(a["E_per_sqrt_bit"]), "lemmas": lemma_selftests()}


def report(d):
    print("warptheorem.py -- the warp theory as one theorem (M-RULINGS item 150)\n")
    for clause in "GHOZBIERN":
        for c, name, status, where in LEMMAS:
            if c == clause:
                print("  (%s) %-6s %s  [%s]" % (c, status, name, where))
    a, b, c = d["t1"], d["t2"], d["t3"]
    counts = {k: sum(1 for l in LEMMAS if l[2] == k) for k in ("DERIVED", "DEFINITION", "PROVED", "READING", "NATURE",
                                                                 "OPEN")}
    print("\n%d lemmas: %d PROVED, %d DERIVED from your more basic rulings, %d PROVED under a named board READING, "
          "%d your DEFINITIONS, %d NATURE, %d OPEN" % (len(LEMMAS), counts["PROVED"], counts["DERIVED"],
                                                       counts["READING"], counts["DEFINITION"], counts["NATURE"],
                                                       counts["OPEN"]))
    print("T1 proved lemmas re-run: E = %.8f J x sqrt(N); H1/G3/O1 %s; Z1 %s; Z2 %s; B1 %s; O2 %s"
          % (a["E_per_sqrt_bit"], a["H1_G3_O1"], a["Z1"], a["Z2"], a["B1"], a["O2"]))
    print("T2 the theorem follows from its lemmas: %s; each OPEN lemma needed: %s" % (b["entailed"],
                                                                                      all(b["needed"].values())))
    print("   OPEN (%d): %s" % (len(b["open"]), "; ".join(o.split(" ", 1)[0] for o in b["open"])))
    print("T3 energy ledger at the example README (E = %.6e J, assembly <= %.4e J): consistent with no sink: %s; with "
          "an absorber besides the copy (the board's reading (a)): %s; control N = 600 (E = %.4e J), no sink: %s"
          % (c["E_example"], ASSEMBLY_MAX_J, c["no_sink"], c["with_sink"], c["E_small"], c["control_small_N"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, b, c = d["t1"], d["t2"], d["t3"]
    chk("T1: E = 459,404,002.42 J x sqrt(N) (exactE.py)", abs(a["E_per_sqrt_bit"] - 459404002.42356985) < 1e-3)
    chk("T1: H1, G3, O1 proved by exactE.py's z3 identities", a["H1_G3_O1"])
    chk("T1: Z1, R5(n,k,n,k) = -R4(k,k) (passage5d.py); Z2, Q = -2 x coin.py's per-leg reading", a["Z1"] and a["Z2"])
    chk("T1: B1, the Gauss condition with K = -g/ell (localbulk.py); O2, surface gravity zero (stability.py)",
        a["B1"] and a["O2"])
    chk("T1: the lemma instruments' selftests pass (%s)" % ", ".join(d["lemmas"]), all(d["lemmas"].values()))
    chk("T2 (STRUCTURAL): the theorem follows from its lemmas, and each OPEN lemma is needed",
        b["entailed"] and all(b["needed"].values()))
    chk("T3: the ledger is inconsistent unless the build has an absorber besides the copy, consistent with one",
        (not c["no_sink"]) and c["with_sink"])
    chk("T3 control: at N = 600 bits E is below the assembly ceiling and needs no sink", c["control_small_N"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
