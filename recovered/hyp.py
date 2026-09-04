import json
H={
'A13':('0 <= 2S-prime <= g',
  'the target subshell is f^g in LS coupling for the target; g electrons in one subshell.',
  'a set of g electrons has maximum total spin g/2, attained when all spins align, so 2S <= g. '
  'the LOWER bound is 0 for even g and 1 for odd g; the index uses the weaker 0 <= 2S-prime, '
  'which is why the lattice is loose here.'),
'A14':('2S-prime <= v <= g',
  'Racah seniority for the configuration l^N; the pairing interaction has the eigenvalue '
  'structure (n-v)(2j+3-n-v).',
  'v counts particles not in J=0 pairs, so v <= g. and a state of total spin S has at least '
  '2S unpaired particles, giving v >= 2S-prime. BOTH bounds are one-parent and monotone.'),
'A16':('|2J_c - 2f| <= 2K <= 2J_c + 2f (step 2)  [EXACT]   vs   0 <= 2K <= 2J_c + 2f_max  [LOOSE]',
  'jK pair coupling: J_c the total angular momentum of the core, f the orbital angular '
  'momentum of the outer electron, K = J_c + f. caps (n,e,l,k,f) = (3,3,1,3,1).',
  'the EXACT form is the angular-momentum triangle rule and needs TWO parents, J_c and f. '
  'the LOOSE form replaces f by its cap f_max, giving one parent. this is the choice that '
  'keeps the tower closed: the exact form takes E from 0 to 35,570.'),
'A17':('|2J - 2K| <= 1',
  'jK coupling; the outer electron carries spin 1/2, and J = K + s with s = 1/2.',
  'adding a spin-1/2 to K gives J = K +/- 1/2, i.e. 2J = 2K +/- 1. one parent, monotone.'),
'A18':('density(axis) = SUM_parents |exact fibre| / SUM_parents |admissible fibre|',
  'the axis is formed by adjoining one coordinate to a parent cell; "exact fibre" is the set '
  'of values genuinely realised by the physics; "admissible fibre" is the set the lattice '
  'bound permits.',
  'the ratio measures how loose the bound is. it is 1 exactly when the bound is tight. three '
  'of the six values require non-obvious exact sets, and without the third, axis 11 computes '
  'to 43.1% instead of 17.0%.'),
'C2eq':('A_q(z) = SUM_{n=1..3} z^n SUM_{l=0..min(n-1,1)} z^l SUM_{k=max(q,1)..min(4l+2,3)} '
  'z^k (1 - z^{min(k,3)+1})/(1-z)',
  'caps (n,e,l,k,f) = (3,3,1,3,1); q the transfer coordinate, held FIXED; z a formal variable. '
  'the final factor is the generating function of the 2S-chain, 0 <= 2S <= min(k,3).',
  'valid for q = 0,1,2,3. A_q(1) = 33, 33, 23, 8, verified against direct enumeration. '
  'the lower limit max(q,1) encodes q <= k.'),
'C3eq':('B_q(z) = SUM_{e=1..3} z^e SUM_{f=0..min(e-1,1)} z^f (1 - z^{min(q,4f+2)+1})/(1-z)',
  'as C2eq; the final factor is the generating function of the g-chain, '
  '0 <= g <= min(4f+2, q).',
  'B_q(1) = 5, 10, 15, 17, verified. NOTE the asymmetry with A_q: the pendant 2S sits on the '
  'A side only, which is why A is a caterpillar and B is a path.'),
'C5eq':('E(Lambda) = 0  AND  E(A_q) = E(B_q) = 0 for every q',
  'the cross-sections A_q and B_q taken with their induced coordinates, at fixed q; caps as above.',
  'the second does NOT follow from the first: a closed index could in principle have defective '
  'slices whose excesses cancel in the total. here none do, and that is a separate invariant.'),
'D1':('I_V = CONTOUR-INTEGRAL (rho + p_r) dV',
  'a static spherically symmetric traversable wormhole; rho the energy density and p_r the '
  'radial pressure in the static frame; the integral taken over the region where the null '
  'energy condition is violated.',
  'Visser-Kar-Dadhich: I_V can be made arbitrarily small by shrinking that region, which is '
  'why the NEC axis is graded by SCALE and not by violation-or-not.'),
'D4':('2 <= S_CHSH <= 2 sqrt 2 <= 4',
  'two spacelike-separated parties, two measurement settings each, two outcomes each; '
  'S_CHSH the standard CHSH combination of correlators.',
  '2 is the local-realistic bound (Bell/CHSH), 2 sqrt 2 the quantum bound (Tsirelson), 4 the '
  'algebraic maximum, attained by no-signalling PR boxes. the three values are the three rungs.'),
'D5':('<T_kk> >= (h-bar / 2 pi) S-double-prime_out',
  'a null deformation of a cut of a null surface, parametrised by lambda; S_out the '
  'entanglement entropy of the region outside the cut; the double prime is the second '
  'variation with respect to lambda.',
  'a BOUND on the stress tensor by an entropy variation, not a forcing edge between coordinates. '
  'it does not enter the index as a charge, which is why it appears in the appendix and not '
  'in the edge list.'),
'D7':('d(c) = X_exp + U_ghost + |NEC_pt - 3| + EOM + d_P(free letters)',
  'the FIFTEEN-letter alphabet; the core cell (X_exp, U_ghost, NEC_pt, EOM) = (0,0,3,0); the '
  'eleven remaining letters are the "free" ones; d_P is the L1 distance from the cell\'s free '
  'letters to the nearest of the 816 excess patterns.',
  'exact on 1,500 sampled cells, 0 mismatches. the formula is alphabet-dependent: the pinned '
  'set changed from nine letters (SD dropped out, EOM came in).'),
'D8':('s(c) = 1{X_exp>0} + 1{U_ghost>0} + 1{NEC_pt=/=3} + 1{EOM>0} + s_P',
  'as D7; s_P is the Hamming distance on the free letters to the nearest excess pattern.',
  'exact on the same 1,500 cells. support, not distance: it counts HOW MANY letters differ, '
  'not by how much.'),
'D9':('R(A x B) = R(A) x R(B)',
  'A and B indices on DISJOINT coordinate sets, and no constraint of the joint index relates '
  'any coordinate of A to any coordinate of B.',
  'under that hypothesis every cross-envelope phi-hat_ij with i in A and j in B is vacuous: '
  'the max over {x_i : x_j <= v} is the global max of A_i, independent of v. so the cross '
  'conditions impose nothing and R factorises. THE HYPOTHESIS IS ESSENTIAL - a single linking '
  'constraint destroys it.'),
'E5':('a semifinite factor carries a faithful normal semifinite trace tau, hence '
  'S(psi) = -tr[rho log rho]',
  'M a semifinite von Neumann factor; rho the density matrix of psi RELATIVE TO tau, i.e. '
  'psi(x) = tau(rho x).',
  'the entropy is defined only up to an additive constant, because tau itself is fixed only '
  'up to rescaling - and Takesaki gives tau . theta_s = e^{-s} tau, so the dual action moves it. '
  'type III factors carry no such trace and no such entropy.'),
}
json.dump(H,open('hyp.json','w'),indent=1)
print('  HYPOTHESES SUPPLIED FOR %d EQUATIONS' % len(H))
print()
for k,(s,h,w) in H.items():
    print('  %s' % k)
    print('     statement  : %s' % s)
    print('     hypotheses : %s' % h)
    print('     why needed : %s' % w)
    print()
print('  RE-RUNNING THE COUNT')
import subprocess
M=json.load(open('math.json'))
still=[e['tag'] for e in M if not e['hypotheses'].strip() and e['tag'] not in H]
print('     equations with no hypotheses recorded, before : 15')
print('     supplied here                                 : %d' % len(H))
print('     remaining                                     : %d %s' % (len(still),still))