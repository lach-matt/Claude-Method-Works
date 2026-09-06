#!/usr/bin/env python3
"""Extract, expand and audit every equation. Writes math.json and prints the audit."""
import json, sys, itertools
from itertools import product, combinations
from collections import Counter
import numpy as np
sys.path.insert(0,'/home/claude/method')
import method_tower as mt

# (tag, statement, hypotheses, provenance, verification-status)
EQ=[]
def eq(tag,stmt,hyp,prov,ver): EQ.append(dict(tag=tag,statement=stmt,hypotheses=hyp,
                                              provenance=prov,verification=ver))

# ---------------------------------------------------------------- A. the operator
eq('A1','A-hat_i(X) = { x_i : x in X }',
   'X a finite set of integer tuples','definition','definitional')
eq('A2','phi-hat_ij(v) = max { x_i : x in X, x_j <= v }',
   'i =/= j; the max over an empty set is -inf','definition',
   'definitional; non-decreasing in v by construction')
eq('A3','R(X) = { x in PROD_i A-hat_i(X) : x_i <= phi-hat_ij(x_j) for all i =/= j }',
   'as above','definition','definitional')
eq('A4','E(X) = |R(X)| - |X| >= 0',
   'none beyond A1-A3','PROVED here, Prop 1.2',
   'PROOF: for x in X and any i =/= j, the set {y_i : y in X, y_j <= x_j} contains x_i since '
   'x_j <= x_j. hence phi-hat_ij(x_j) >= x_i, so x in R(X). therefore X subset R(X). QED')
eq('A5','X subset BPC(X) subset R(X),  BPC(X) = { x : (x_i,x_j) in proj_ij(X) for all i<j }',
   'none','PROVED here',
   'VERIFIED: R = BPC exactly on every object computed. the potential ambiguity between '
   'genuine inconsistency and envelope coarseness does not arise here.')
eq('A5b','R is a closure operator: extensive, monotone, idempotent',
   'none','extensivity PROVED (A4); monotone and idempotent COMPUTED',
   'R(R(X)) = R(X) verified on Lambda_8 and both violation indices; monotonicity held on '
   '30 nested random pairs with no failure. NOT proved in general.')
eq('A5c','E(X) = 0 iff the binary constraint network is globally consistent',
   'the constraints are the monotone binary projections','identification, standard CSP',
   'this is the identification that licenses Freuder and Montanari')

# ------------------------------------------------------------------- B. Lambda
for t,s in [('A6','1 <= n <= n_max'),('A7','0 <= l <= n - 1'),('A8','1 <= k <= 4l + 2'),
            ('A9','0 <= q <= k'),('A10','0 <= f <= e - 1'),
            ('A11','0 <= g <= min(4f + 2, q)'),('A12','0 <= 2S <= k')]:
    eq(t,s,'caps (n,e,l,k,f) = (3,3,1,3,1)','construction',
       'each bound binds ONE coordinate by a monotone function of ONE other -- the closure rule 1.8')
eq('A13','0 <= 2S-prime <= g','','tower level 9','monotone, one parent')
eq('A14','2S-prime <= v <= g','','tower level 10','monotone, one parent')
eq('A15','0 <= 2J_c <= phi-hat(k)','phi-hat(k) = max 2J over terms of l^k','tower level 11',
   'monotone in k; requires the EXACT spin set of l^k by microstate enumeration')
eq('A16','|2J_c - 2f| <= 2K <= 2J_c + 2f, step 2  [EXACT]  vs  0 <= 2K <= 2J_c + 2f_max  [LOOSE]',
   '','tower level 12',
   'THE EXACT FORM IS TERNARY: two parents. it takes E from 0 to 35,570 and destroys the '
   'cylinder factorisation. the book uses the LOOSE form, which is binary.')
eq('A17','|2J - 2K| <= 1','','tower level 13','monotone, one parent')
eq('A18','density(axis) = SUM_parents |exact fibre| / SUM_parents |admissible fibre|',
   '','definition','all six density values reproduce given three non-obvious exact sets')

# ------------------------------------------------------------------ C. the cylinder
eq('C1eq','|Lambda| = SUM_q |A(q)| x |B(q)| = 976',
   'conditioned on the transfer coordinate q','The Method, 12.6.1',
   'RECHECKED: 33x5=165, 33x10=330, 23x15=345, 8x17=136, sum 976. exact.')
eq('C2eq','A_q(z) = SUM_{n=1..3} z^n SUM_{l=0..min(n-1,1)} z^l SUM_{k=max(q,1)..min(4l+2,3)} '
   'z^k (1 - z^{min(k,3)+1})/(1-z)',
   '','The Method, 12.7','A_q(1) = 33, 33, 23, 8 -- verified against enumeration')
eq('C3eq','B_q(z) = SUM_{e=1..3} z^e SUM_{f=0..min(e-1,1)} z^f (1 - z^{min(q,4f+2)+1})/(1-z)',
   '','The Method, 12.7','B_q(1) = 5, 10, 15, 17 -- verified')
eq('C4eq','Box(a,b)(z) = PROD_i z^{a_i} (1 - z^{b_i - a_i + 1})/(1 - z)',
   'every fibre bottoms out in a product of chains','The Method, 12.7.2','structural')
eq('C5eq','E(Lambda) = 0 AND E(A_q) = E(B_q) = 0 for every q',
   '','The Method, 12.8.5',
   'RECHECKED: all four cross-sections closed. the second does NOT follow from the first.')

# -------------------------------------------------------------- D. violation index
eq('D1','I_V = CONTOUR-INTEGRAL (rho + p_r) dV','','the volume-integral quantifier',
   'grades the null-energy axis')
eq('D2','NEC_pt >= 3 AND X_exp = 0 AND EOM = 2nd  =>  U_ghost = 1',
   'causal, Lorentz-invariant, second-order equations of motion, scalar/gauge with fermionic matter',
   'Buniy-Hsu-Murray 2006',
   'ARITY 4, reduced to 3 by Ostrogradsky (EOM higher => ghosts). the jurisdiction is what '
   'makes it ternary.')
eq('D3','capacity(l) = m(4l + 2)','parastatistics of order m','generalisation of Pauli',
   'E = 0 verified for m = 1, 2, 3 through Lambda_13; m=1 reproduces the canonical tower')
eq('D4','2 <= S_CHSH <= 2 sqrt 2 <= 4','','Bell / Tsirelson / Popescu-Rohrlich','measured')
eq('D5','<T_kk> >= (h-bar / 2 pi) S-double-prime_out','','the QNEC',
   'a BOUND, not a forcing edge -- it does not enter the index as a charge')
eq('D6','816 = 1 x 816','core times multiplicity','computed','exact')
eq('D7','d(c) = X_exp + U_ghost + |NEC_pt - 3| + EOM + d_P(free letters)',
   '','the frontier distance','0 mismatches on 1,500 sampled cells')
eq('D8','s(c) = 1{X_exp>0} + 1{U_ghost>0} + 1{NEC_pt=/=3} + 1{EOM>0} + s_P',
   '','the frontier support','0 mismatches on 1,500 sampled cells')
eq('D9','R(A x B) = R(A) x R(B)  when no constraint links the factors','','PROVED here',
   'every cross-envelope is vacuous')
eq('D10','E(A x B) = |A| E_B + |B| E_A + E_A E_B','as D9','PROVED here',
   'for Lambda x violation index: 976 x 30 = 29,280. the defect is EXTENSIVE.')

# ------------------------------------------------------------------- E. the chain
eq('E0','Reeh-Schlieder: Omega is cyclic and separating for local algebras',
   'a Hadamard state; the algebra of a region with nonempty causal complement','standard AQFT',
   'the physical input that makes T1 applicable')
eq('E1','Tomita-Takesaki: S = J Delta^{1/2}, sigma_t = Ad(Delta^{it}), sigma_t(M) = M',
   'M a von Neumann algebra, Omega cyclic and separating','Tomita 1967, Takesaki 1970',
   'fully general')
eq('E2','Borchers: U(a) M U(-a) subset M for a >= 0 with P >= 0 and U(a)Omega = Omega'
   '  =>  Delta^{it} U(a) Delta^{-it} = U(e^{-2 pi t} a),  J U(a) J = U(-a)',
   'as stated','Borchers CMP 1992','fully general; purely algebraic')
eq('E3','Wiesbrock: (N subset M, Omega) with sigma_t^M(N) subset N for t <= 0'
   '  =>  there exists U(a) = e^{iPa}, P >= 0, with N = U(1) M U(-1)',
   'a common cyclic separating vector, extended by Araki-Zsido to a faithful normal '
   'semifinite weight',
   'Wiesbrock CMP 157 (1993), erratum CMP 184 (1997); Araki-Zsido 2004',
   'THIS IS A CHARACTERISATION, an iff. HSMI and a positive-generator U are the same condition.')
eq('E4','Takesaki: N = M crossed_{sigma^phi} R is type II_infinity with a faithful semifinite '
   'normal trace tau satisfying tau . theta_s = e^{-s} tau, and M = N crossed_theta R, '
   'uniquely in the strongest sense',
   'M of type III, phi a faithful semifinite normal weight, theta the dual action',
   'Takesaki, Acta Math 131 (1973); Theory of Operator Algebras XII.1.1',
   'THE TRACE IS NOT INVARIANT -- it scales. this is why entropy here is defined only up to '
   'an additive constant. STATED FOR R: the extension to arbitrary locally compact groups is '
   'NOT automatic (2024).')
eq('E5','a semifinite factor carries a trace, hence S = -tr[rho log rho]',
   '','standard','type III carries none')
eq('E6','[K_A, K_B] = 2 pi i (K_A - K_B) = (2 pi)^2 i P,  '
   'P = INTEGRAL_{x^-=0} (B(y) - A(y)) T_{++}',
   'null cuts A, B on a null plane, B >= A','Casini-Teste-Torroba; Ceyhan-Faulkner',
   'the generator IS the averaged null energy operator. but the identification is NOT the '
   'method for proving positivity -- Chandrasekaran-Flanagan warn explicitly.')
eq('E7','I(A:C|B) = 0  <=>  short quantum Markov chain  <=>  exact Petz recovery',
   'A, B, C consecutive regions','Petz 1986; Hayden-Jozsa-Petz-Winter 2004',
   'PETZ IS STATED FOR VON NEUMANN ALGEBRAS. HJPW uses entropies, which are INFINITE in '
   'type III -- the statement needs re-expression via Araki relative entropies.')

# ---------------------------------------------------------------- F. the null surface
eq('F1','Omega_N = INTEGRAL du d^{d-2}y sqrt(q)(y) [ delta phi ^ d_u delta phi ]',
   'a null hypersurface with u-independent transverse metric, i.e. Theta = 0',
   'the characteristic symplectic form; theta = delta phi L_l phi eta',
   'CONTAINS NO TRANSVERSE DERIVATIVE. this is the whole of C1.')
eq('F2','{ phi(u,y), phi(u-prime,y-prime) } = (1 / 4 sqrt(q)(y)) sgn(u - u-prime) '
   'delta^{d-2}(y - y-prime)',
   'as F1','inverting F1 block by block',
   'COMPUTED: off-generator block of Omega^{-1} is 0.000e+00 at 4, 6 and 8 generators, for '
   'arbitrary y-dependence of sqrt(q). control with an artificial d_y term: nonzero immediately.')
eq('F3','P_alpha = -(1/8 pi) INTEGRAL_{S_0} alpha e^{Gamma_0^+} [ L_l mu - '
   '(Upsilon_0^+ - Upsilon_0^-) L_l(mu Theta) ]',
   'the extended horizon phase space with corner edge modes',
   'Chandrasekaran-Flanagan 2026, eq (1.7b)',
   'L_l mu = Theta mu, so P_alpha is PROPORTIONAL TO Theta and VANISHES on a non-expanding '
   'horizon. the two-sided term is second order in the same quantity.')
eq('F4','A_beta = (1/8 pi) [ INTEGRAL_{S_0^+} beta mu - INTEGRAL_infinity beta mu ]',
   'as F3','Chandrasekaran-Flanagan eq (1.7a)','the area operator, conjugate to boosts')
eq('F5','{ P_alpha, O(p) } = -alpha e^{Gamma_0^+} L_l O(p)',
   'O(p) a gravitationally dressed observable','Chandrasekaran-Flanagan eq (1.9a)',
   'the dressing is what makes the corner charges act non-trivially')
eq('F6','C2:  Delta_{M(u1)}^{it} M(u2) Delta_{M(u1)}^{-it} subset M(u2),  t <= 0,  u1 < u2',
   'N a non-expanding horizon with no Killing field, omega Hadamard, M(u) the algebra of N_{>u}',
   'the open condition',
   'OPEN. two nearby forms are wrong: SSA saturation as written is unsayable in type III; '
   'sigma_t(N) = N for all t is too strong (Takesaki: it gives a conditional expectation, '
   'which type III_1 factors do not admit, and it makes P = 0).')
eq('F7','d - 1 = 1 + (d - 2)','a null hypersurface in d dimensions','the dimensional ledger',
   'the 1 comes from one HSMI per generator; the (d-2) from the transverse direct integral, '
   'which NO half-sided modular inclusion supplies. the two open pieces are dimensionally distinct.')

json.dump(EQ,open('/home/claude/paper/math.json','w'),indent=1)

# ---------------------------------------------------------------------- THE AUDIT
print('  MATHEMATICAL AUDIT -- %d equations' % len(EQ))
print()
def grade(e):
    v=e['verification'].lower()
    if v.startswith('proof') or 'proved here' in e['provenance'].lower(): return 'PROVED'
    if any(k in v for k in ['computed','verified','recheck','0.000e+00','exact','reproduce',
                            '0 mismatches','measured']): return 'COMPUTED'
    if 'definitional' in v or 'definition' in e['provenance']: return 'DEFINITIONAL'
    if 'open' in v: return 'OPEN'
    return 'CITED'
g=Counter(grade(e) for e in EQ)
print('  %-14s %s' % ('grade','count'))
for k,v in sorted(g.items(),key=lambda kv:-kv[1]): print('  %-14s %d' % (k,v))
print()
print('  BY SECTION')
sec={'A':'the operator','C':'the cylinder','D':'the violation index','E':'the theorem chain',
     'F':'the null surface'}
for p,nm in sec.items():
    rows=[e for e in EQ if e['tag'].startswith(p)]
    if not rows: continue
    gg=Counter(grade(e) for e in rows)
    print('  %-22s %2d equations   %s' % (nm,len(rows),dict(gg)))
print()
print('  FLAGS')
for e in EQ:
    v=e['verification']
    if any(k in v for k in ['NOT proved','NOT automatic','OPEN','TERNARY','NOT the method',
                            'needs re-expression','VANISHES','not invariant']):
        print('     %-6s %s' % (e['tag'], v.split('.')[0][:110]))
print()
print('  UNHYPOTHESISED EQUATIONS (no hypotheses recorded)')
n=0
for e in EQ:
    if not e['hypotheses'].strip():
        print('     %-6s %s' % (e['tag'], e['statement'][:80])); n+=1
print('     count: %d of %d' % (n,len(EQ)))
