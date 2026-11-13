#!/usr/bin/env python3
"""lamconst5.py -- the constants of lambda_25 written out (EQUALITY5-LAYER.md, Round 9, R9.1-R9.3).

Proposition L.25'' (a)'s threshold lambda_25(delta) = min(lam_rec, 10^(-E_25)) (R8.3, `lam25_5.py`) takes six inputs
besides certified numbers: C_L1 (Lemma L.1), C_L3 (L.3 (b), the means), C_L4 (L.4'), C_L4P (L.4_P), C_rho (the reach
rho_w <= C_rho lam of L.4' and L.4_P) and lam_rec (below which g_lam exists and L.3 (b), L.4', L.4_P hold).  R5.5 wrote
C_L4 as a formula in lambda0's leaves (`constL5.py`).  This program writes the other five, each from the proof of its
lemma, step by step, and checks:

  C1 (certified) C_L1.  Lemma L.1's identity g^-1 = g0^-1 - g0^-1 k g0^-1 + g0^-1 k g0^-1 k g^-1 (N0), contracted with
     dPhi0 twice, gives |g^-1(dPhi0, dPhi0) + m0| <= C_L1 |k|, |k| the operator norm of the Cartesian components (at most
     the Frobenius norm, the norm of L.4's energies), with
         C_L1 := |Phi0#|^2 + |Phi0#| |dPhi0| n^2 eps1/(1 - n eps1) = |Phi0#|^2 + (3/5) |Phi0#| |dPhi0|,
     n := 1 + 2 mu_end/a^2 >= sup |g0^-1| and eps1 = (3/5)/(n^2 + (3/5) n) >= |k| for lam <= lambda0 (CONSTANTS5 1.4,
     Step 3 of lambda0's proof); n^2 eps1/(1 - n eps1) = 3/5 exactly.  |Phi0#|^2 = (1 - beta0)^2 + beta0^2 (Phi0# = d_v +
     beta0 d_r = (1 - beta0) d_tau + beta0 xhat.d_x), |dPhi0|^2 = r_q'^2 + (1 - r_q')^2 <= 1, beta0 in [-(sqrt(mu_end/mu0)
     - 1) - A^2 c^2/(18 sqrt mu0), 0], r_q' in [0, A^2 c^2/(18 sqrt mu0)], c <= 1.3241035 the envelope's peak (R4.5).
     Evaluated at P* in interval arithmetic.  Then 400 boundary points (mu in [mu0, mu_end], mu' in [0, (2/9) A^2 c^2],
     the Kerr-Schild metric in Cartesian components) with random and adversarial k (|k| = eps1, k = -+eps1 u u^T, u along
     Phi0#): the exact ratio |g^-1(dPhi0, dPhi0) + m0|/|k| is at most the pointwise C_L1 and the uniform one, and |g0^-1|
     <= n there.  Control: C_L1 without its quadratic term (pointwise |Phi0#|^2) is exceeded at an adversarial k.
  C2 (computed) Theorem 1's.  C_L3 := max_(m<=N) Cb_m, R5.5's node for L.3 (b) (`constL5.py`'s DAG; R5.5 lists it and
     does not name it); C1 := n (n + 3/5) (C_app + 2 C_inf M lambda0^(K-4)) (EQUALITY5 section 0: |g - g0| <= C lam with
     C from Step 3 of lambda0's proof, and |g^-1 - g0^-1| <= n^2 |k|/(1 - n |k|)); C_rho1 := 2 C1 (tau_end - tau0) (L.4's
     region {v + 2 C1 lam (tau - tau0) <= v1} contains the boundary point at tau <= tau_end); lam_rec1 := min(lambda0,
     1/(2 C1)) (Theorem 1's g_lam; L.4 step 1 needs s = C1 lam <= 1/2; L.3 (b)'s U-ball condition 4 C_b C0 lam^(N-3)
     eps_(2N+2) <= 1 is lambda0's ninth term, since eps_(2N+2)(v1) <= eps_(M_P)(v1) <= lam^3 <= 1 by (H2)).  Every leaf is
     one of lambda0's leaves or nodes, a certified number or a constant of the seed; increasing (decreasing for
     lam_rec1) in every leaf.  Control: a node needing a leaf outside the set (Theorem P's C_R) is detected.
  C3 (computed) Theorem 2's: C_P, C_rhoP, C_L3P, C_L4P and lambda_P as a DAG in Theorem P's leaves, transcribed from
     L.3_P, L.4_P and the proofs of Propositions 9.8, 9.9 and Theorem P (N1STAR-PROOF.md, sections 9.1-9.4):
       beta0 := max(2, 4 C_9 + 1), N_P := K + 4 + ceil(4 beta0), K' := N_P - 1,
       M_F := 4 C_F e^(6 C_F) C_R + 1,  M_N := 8 C_9 C' (M_F + C_R + 1),  C_Piii := C_93 max(2 M_F, M_N (1 + C_kP)),
       M_EP := C3 (M_N + 1 + C_RO) + 1  (Theorem E's M at the trace data, N_P(tau0) <= M_N lam^(K' - 2 beta0)),
       C_P := n (n + 3/5) (C_kP + max(C_Piii, 2 C_inf M_EP)),  C_rhoP := 2 C_P (2 + tau_end - tau0),
       C_dP := C_E5 K_P^(N_P+1) (1 + S_aP + S_bP)^(N_P+1)/(N_P - 2)!,  C_E5 := pi sqrt(2 d1) (E5: an E_3 profile has
               L^2 norm <= C_E5 t^(-3/2) on A_P(tau), r >= t + a1, thickness <= d1 := V_P - v_s),
       C_L3P := max_m Cb_m^P, C_dOP := L.3 (d)'s Cd, both from L.3's recursion on Omega with the stage-m slice data
               replaced by L.3_P's traces Tr_m (and P6 by Theorem A_P's P6P),
       C_L4P := C_S e^(C2 (1 + M_EP + K_OP) T) (2 C_95 e^(2 C_95 C_k4) C_dP + T C_dOP),
       lambda_P := min{lam1, d0/20, 1, lam_F, lam_mF, lam_N, lam_abs, lam_mN, lam_EP} with
         lam_F = (8 C_F^2 e^(6 C_F) M_F)^(-1/(K'-5)) (9.8's bootstrap closes), lam_mF = min(eps_P/(2 n (n + 3/5)
         C_kP), (eps_P/(4 n (n + 3/5) C_93 M_F))^(1/(K'-3))) (Lemma 9.1 (f)'s margin), lam_N = (4 C_9 M_N)^(-1/(K' - 8
         - 4 beta0)) (9.9's nonlinear terms), lam_abs = 1/(8 C_abs) (9.9's absorbed g_j, j >= 3), lam_mN = (eps_P/(2 n
         (n + 3/5) C_93 M_N (1 + C_kP)))^(1/(K' - 3 - 2 beta0)) (the margin on the near region), lam_EP = min(eps1/(2
         C_kP), (min(eps1, eps2)/(4 C_inf M_EP))^(1/(K-3)), (2 C_dw M_EP)^(-1/(K-4)), 1/(C3 C_nl M_EP^2)) (Theorem E on
         Omega, (P-iv): lambda0's Steps 3 and 7 with M_EP; Proposition 6.5 has no part there).
     Checks: every leaf is Theorem P's (listed with its source), lambda0's, certified or the seed's (control: a planted
     leaf detected); C_P, C_rhoP, C_L3P, C_L4P increasing and every term of lambda_P positive and decreasing in every
     leaf at fixed beta0 except eps_P; an independent transcription agrees at 20 random points (controls: the kernel
     integral 2 dropped from C_L4P, and lam_N's exponent with 4 beta0 -> 2 beta0, are each detected).  None of Theorem
     P's leaves is certified in the record (CONSTANTS5 treats Theorem 1 only; no program computes Theorem A_P's profiles).
  C4 (computed) the census of sections 9.1-9.4 of N1STAR-PROOF.md (located by content, from "## 9. Theorem P" to
     "### 9.5"): every line with a threshold phrase (lam_X, "small", "absorb", eps_P, eps_U, lam1, d0/20, "lam <= 1",
     "there is/are", "margin of Lemma 9.1", "Theorem E with this K") is classified, T (a term of lambda_P, named) or X
     (no threshold on lam), and every term of lambda_P has a T line.  Control: a planted "for lam small enough by
     compactness" line is left unclassified (detected).
  C5 (certified) lambda_25's status.  The conditions of R8.3 whose gamma involves no uncertified leaf -- (H1), (H2),
     (Lh), (Tl), and (J) with gamma_J = log10(4 pi + C_rho) >= log10(4 pi) -- give E_cf(delta) <= E_25(delta) whatever
     the leaves are, so lambda_25(delta) <= 10^(-E_cf(delta)), certified; (H2) and (Tl) are evaluated at beta0 = 2, the
     least beta0 allows, and E_H2 increases with beta0 (computed at beta0 = 2, 9/4, 3, 5).  Direct evaluation at 200
     points beyond E_cf (actual n, h_n): those conditions hold.  The illustration (every uncertified leaf 1, lambda0 =
     0.00244; beta0 = 5 then, N_P = 30) prints E_25 and lam_rec: a value of the formula, not a bound.  Control: (W1)
     admitted to the constant-free set is rejected (its gamma depends on C_L4's leaves).

Labels: C1, C5 certified (interval arithmetic, mpmath.iv), C1's samples computed (mpmath); C2-C4 computed (exact
sympy and rationals); the formulas deduced, each from the proof step named beside it.
Run: python3 checks/lamconst5.py   (a few minutes)
"""
import hashlib
import os
import random
import re
import sys
import textwrap

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import constL5 as CL                                                              # noqa: E402
import lam25_5 as L25                                                             # noqa: E402

iv = mp.iv
iv.dps = 50
mp.mp.dps = 50
PROOF = os.path.join(HERE, '..', 'N1STAR-PROOF.md')


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def ivq(x):
    x = sp.Rational(x)
    return iv.mpf(int(x.p))/iv.mpf(int(x.q))


def up(p, d=6):
    with mp.workdps(50):
        return mp.nstr(mp.ceil(mp.mpf(p._mpi_[1])*10**d)/10**d, 15)


def dn(p, d=6):
    with mp.workdps(50):
        return mp.nstr(mp.floor(mp.mpf(p._mpi_[0])*10**d)/10**d, 15)


# ------------------------------------------------------------------------------------------------------------ P*
MU0, AMP = 1, 1                                          # P*: mu0 = 1, A = 1 (CONSTANTS5 1.1)
Q0 = (ivq(sp.Rational(9, 1250)))**(iv.mpf(1)/8)          # q0^8 = 9/1250
A_IN = Q0/2                                              # a = delta0 = q0/2
MU_END = ivq(sp.Rational(227, 192))
N_IV = 1 + 2*MU_END/A_IN**2                              # n >= sup |g0^-1|_op (CONSTANTS5 1.4)
EPS1 = (iv.mpf(3)/5)/(N_IV**2 + iv.mpf(3)/5*N_IV)        # eps1 in the operator norm
CPEAK = iv.mpf('1.3241035')                              # the envelope's peak (CONSTANTS5 R2.2 (i) (a), R4.5)
T_IV = iv.mpf('5.937208254')                             # tau_end - tau0 (CONSTANTS5 1.4)
V_P = iv.mpf('4.5') + 1 + T_IV + iv.mpf('0.5')           # V_P := V + 1 + (tau_end - tau0) + kappa, V = v_end + T
D1 = V_P - iv.mpf('0.5')                                 # d1 := V_P - v_start
D0 = V_P - iv.mpf('0.5') - iv.mpf('0.5')                 # d0 := V_P - kappa - v_start
LAM1 = A_IN/10                                           # lam1 = min(1, delta0)/10
CE5 = iv.pi*iv.sqrt(2*D1)


def cl1_parts():
    rq = iv.mpf(AMP)**2*CPEAK**2/(18*iv.sqrt(MU0))       # sup r_q' = mu0^(1/4) mu^(-3/4) mu'/4 <= A^2 c^2/(18 sqrt mu0)
    beta = (iv.sqrt(MU_END/MU0) - 1) + rq                # sup |beta0|
    phi2 = (1 + beta)**2 + beta**2
    dphi2 = iv.mpf(1)                                    # (1 - r_q')^2 + r_q'^2 <= 1 for 0 <= r_q' <= 1
    quad = N_IV**2*EPS1/(1 - N_IV*EPS1)
    return rq, beta, phi2, dphi2, quad


def cl1_value():
    rq, beta, phi2, dphi2, quad = cl1_parts()
    return phi2 + iv.sqrt(phi2)*iv.sqrt(dphi2)*quad


# ------------------------------------------------------------------------------------------------------------ C1
def ks_metric(mu, r, om):
    """g0 = eta + (mu/r^2) l (x) l, l = dtau + xhat.dx, in Cartesian (tau, x1..x4)"""
    lv = mp.matrix([1] + list(om))
    g = mp.diag([-1, 1, 1, 1, 1])
    return g + (mu/r**2)*(lv*lv.T)


def opnorm(Mx):
    """the operator norm of a symmetric matrix: its largest absolute eigenvalue"""
    return max(abs(e) for e in mp.eigsy((Mx + Mx.T)/2)[0])


def c1(control=False):
    mp.mp.dps = 50
    rq, beta, phi2, dphi2, quad = cl1_parts()
    CL1 = cl1_value()
    nmax = mp.mpf(N_IV._mpi_[1])
    eps1 = mp.mpf(EPS1._mpi_[0])
    rng = random.Random(9)
    worst_pt, worst_uni, worst_n, ctl_exceeded = mp.mpf(0), mp.mpf(0), mp.mpf(0), False
    cpk = mp.mpf('1.3241035')
    for _ in range(400):
        mu = 1 + (mp.mpf(227)/192 - 1)*mp.mpf(rng.random())
        mup = mp.mpf(2)/9*cpk**2*mp.mpf(rng.random())
        rqv = (MU0*mu)**mp.mpf(0.25)
        rqp = rqv*mup/(4*mu)
        v = [mp.mpf(rng.gauss(0, 1)) for _ in range(4)]
        nv = mp.sqrt(sum(x*x for x in v))
        om = [x/nv for x in v]
        g0 = ks_metric(mu, rqv, om)
        g0i = g0**-1
        xh = mp.matrix([0] + om)
        dPhi = xh - rqp*mp.matrix([1] + om)                  # dr - r_q' dv, dv = dtau + dr
        Phs = g0i*dPhi                                       # Phi0# = g0^-1 dPhi0
        m0 = -(dPhi.T*g0i*dPhi)[0]
        nX = opnorm(g0i)
        worst_n = max(worst_n, nX/nmax)
        pPh, pdP = mp.norm(Phs), mp.norm(dPhi)
        cl1_pt = pPh**2 + pPh*pdP*nX**2*eps1/(1 - nX*eps1)
        u = Phs/pPh
        ks = []
        for s in (eps1, -eps1):
            ks.append(s*(u*u.T))
        for _k in range(2):
            Rm = mp.matrix(5, 5)
            for i in range(5):
                for j in range(i, 5):
                    Rm[i, j] = Rm[j, i] = mp.mpf(rng.gauss(0, 1))
            ks.append(Rm*(eps1/opnorm(Rm)))
        for k in ks:
            gl = g0 + k
            val = (dPhi.T*(gl**-1)*dPhi)[0] + m0
            ratio = abs(val)/opnorm(k)
            worst_pt = max(worst_pt, ratio/cl1_pt)
            worst_uni = max(worst_uni, ratio/mp.mpf(CL1._mpi_[1]))
            if ratio > pPh**2*(1 + mp.mpf(10)**-30):
                ctl_exceeded = True
    if control:
        return not ctl_exceeded                               # the control "passes" if the mutated bound survives
    ok = worst_pt <= 1 and worst_uni <= 1 and worst_n <= 1
    out("  C1 C_L1 = |Phi0#|^2 + |Phi0#||dPhi0| n^2 eps1/(1 - n eps1) at P*: sup r_q' <= %s, sup |beta0| <= %s, |Phi0#|^2"
        " <= %s, |dPhi0| <= 1, n <= %s, eps1 >= %s, n^2 eps1/(1 - n eps1) in [%s, %s] (= 3/5); C_L1 in [%s, %s], log10"
        " C_L1 <= %s (certified).  400 boundary points, 4 k each (adversarial -+eps1 u u^T and random, |k| = eps1): max"
        " ratio/pointwise C_L1 = %s, max ratio/uniform C_L1 = %s, max |g0^-1|/n = %s: %s"
        % (up(rq, 7), up(beta, 7), up(phi2, 6), up(N_IV, 4), dn(EPS1, 10), dn(quad, 12), up(quad, 12), dn(CL1, 5),
           up(CL1, 5), up(iv.log(CL1)/iv.log(10), 5), mp.nstr(worst_pt, 8), mp.nstr(worst_uni, 6),
           mp.nstr(worst_n, 6), ok))
    return ok


# ------------------------------------------------------------------------------------------------------------ C2
C_app, C_inf, C_dw, C3s, C_nl, eps2 = sp.symbols('C_app C_inf C_dw C3 C_nl eps2', positive=True)
n_s, e1_s = sp.symbols('n eps1', positive=True)
LAMBDA0 = set(CL.LEAVES) | {C_app, C_inf, C_dw, C3s, C_nl, eps2}      # lambda0's leaves and nodes (CONSTANTS5 1.3, 1.5)
CERT2 = dict(CL.CERT)
CERT2.update({n_s: sp.Rational(str(mp.nstr(mp.mpf(N_IV._mpi_[1]), 20))), e1_s: sp.Rational(str(mp.nstr(mp.mpf(
    EPS1._mpi_[0]), 20)))})
K_EX = 6


def build1(mutate=None):
    d, C11, C4 = CL.build()
    cbs = [s_ for s_, _ in d.defs if re.fullmatch(r'Cb\d+', str(s_))]
    CL3 = d("C_L3", sp.Max(*cbs))                                                  # L.3 (b): every stage's means
    extra = sp.Symbol('C_R', positive=True) if mutate == "leaf" else 0
    C1 = d("C1", n_s*(n_s + sp.Rational(3, 5))*(C_app + 2*C_inf*CL.M*CL.lam0**(K_EX - 4) + extra))     # EQUALITY5 0
    Crho1 = d("C_rho1", 2*C1*CL.T)                                                 # L.4's region, tau <= tau_end
    inv = d("inv2C1", 1/(2*C1))
    return d, CL3, C1, Crho1, C4, inv


def c2(control=False):
    d, CL3, C1, Crho1, C4, inv = build1(mutate="leaf" if control else None)
    allowed = LAMBDA0 | set(CERT2) | CL.SEED
    extra = d.leaves() - allowed
    if control:
        return not extra
    structural = all(CL.positive_tree(e.subs(CERT2)) for s_, e in d.defs if s_ != inv)
    rng = random.Random(21)
    leaves = sorted(d.leaves() - set(CERT2), key=str)
    fd = True
    for _ in range(30):
        pt = dict(CERT2)
        pt.update({s_: sp.Rational(rng.randint(5, 150), 100) for s_ in leaves})
        k = rng.choice(leaves)
        pt2 = dict(pt)
        pt2[k] = pt[k]*sp.Rational(101, 100)
        v1, v2 = d.value(pt), d.value(pt2)
        fd &= all(v2[c] - v1[c] >= 0 for c in (CL3, C1, Crho1)) and v2[inv] - v1[inv] <= 0
    ill = dict(CERT2)
    ill.update({s_: 1 for s_ in leaves})
    ill[CL.lam0] = sp.Rational(244, 100000)
    vals = d.value(ill)
    lg = lambda x: mp.nstr(mp.log10(mp.mpf(sp.N(vals[x], 30))), 6)                 # noqa: E731
    lrec = min(sp.N(vals[inv], 30), sp.Rational(244, 100000))
    ok = not extra and structural and fd
    out("  C2 Theorem 1's: C_L3 := max_m Cb_m (R5.5's node for L.3 (b)), C1 = n (n + 3/5)(C_app + 2 C_inf M lambda0^2),"
        " C_rho1 = 2 C1 (tau_end - tau0), lam_rec1 = min(lambda0, 1/(2 C1)): leaves %s, none outside lambda0's leaves,"
        " the certified numbers and the seed's constants: %s; increasing (1/(2 C1) decreasing) in every remaining leaf,"
        " structurally %s and by finite differences %s; illustration (leaves 1, lambda0 = 0.00244): log10 C_L3 = %s,"
        " log10 C1 = %s, log10 C_rho1 = %s, lam_rec1 = %s"
        % (sorted(map(str, d.leaves() - set(CERT2))), not extra, structural, fd, lg(CL3), lg(C1), lg(Crho1),
           mp.nstr(mp.mpf(sp.N(lrec, 30)), 5)))
    return ok


# ------------------------------------------------------------------------------------------------------------ C3
PLEAVES = {   # Theorem P's constants, each named by the proof that produces it (N1STAR-PROOF.md, by content)
    'C_kP': "Theorem A_P / 9.4: g_app^-1 - g0^-1 in lam E_(3/2); |g_app - g0| <= C_kP lam t^(-3/2) on P, C_kP lam on Omega",
    'C_R': "Theorem A_P: |Ric^H(g_app)|_(k,P) <= C_R lam^(N-1) t^(-3/2)",
    'C_RO': "Theorem A_P on Omega: (E1)-(E3) hold on Omega; the residual constant (E4) there",
    'C_F': "Proposition 9.8: Gronwall: E(tau) <= C e^(6C) (2 C_R lam^K' + C M_F^2 lam^(2K'-5))",
    'C_93': "Lemma 9.3 (a): ||f||_inf <= C t^(-3/2) sum ||d_r^i Omega^beta f||",
    'C_9': "Proposition 9.9: C the sum of the constants of each line of (9.9)",
    'C_pr': "Proposition 9.9: N_P(tau_T) <= C' E(tau_T)",
    'C_abs': "Proposition 9.9: every term with a profile g_j, j >= 3, carries a factor lam and is absorbed",
    'eps_P': "Lemma 9.1 (f): |g^-1 - g0^-1| <= eps_P t^(-5/4)",
    'C_95': "Lemma 9.5: ||d u(tau)|| <= C exp(C int k)(||d u(tau1)|| + int ||f||)",
    'C_k4': "L.4_P (3): the Gronwall kernel C t^(-3/2) on P (d g_lam, d^2 g_app, Theorem P's bounds on d^j w)",
    'K_P': "L.3_P (d_P): the coefficient bound of a monomial's factors on P",
    'S_aP': "L.3_P (a_P), (c_P): the sum of the oscillating profiles' class constants on P",
    'S_bP': "L.3_P (b_P): the sum of the means' and phases' class constants on P",
    'P6P': "Theorem A_P on Omega: sup |d^6 g_j| of the continued profiles",
}
PS = {k: sp.Symbol(k, positive=True) for k in PLEAVES}


def trace_leaves(NP):
    return [sp.Symbol('Tr%d' % m, positive=True) for m in range(1, NP + 1)]


def beta0_of(c9):
    return max(2, 4*c9 + 1)


def NP_of(c9):
    return K_EX + 4 + int(mp.ceil(4*mp.mpf(beta0_of(c9))))


def build_P(NP, beta0, mutate=None):
    """Theorem 2's constants at a fixed N_P and beta0 (the consistency N_P = K + 4 + ceil(4 beta0) is checked by the
    caller); the DAG of constL5's class"""
    d = CL.Dag()
    S = PS
    Kp = NP - 1
    if mutate == "leaf":
        S = dict(PS)
        S['C_R'] = PS['C_R'] + sp.Symbol('C_planted', positive=True)
    M_F = d("M_F", 4*S['C_F']*sp.exp(6*S['C_F'])*S['C_R'] + 1)                      # Proposition 9.8
    M_N = d("M_N", 8*S['C_9']*S['C_pr']*(M_F + S['C_R'] + 1))                      # Proposition 9.9: B = M_N lam^K'
    CPiii = d("C_Piii", S['C_93']*sp.Max(2*M_F, M_N*(1 + S['C_kP'])))              # (P-iii) by Lemma 9.3 (a)
    M_EP = d("M_EP", C3s*(M_N + 1 + S['C_RO']) + 1)                                # Theorem E's M at the traces
    C_P = d("C_P", n_s*(n_s + sp.Rational(3, 5))*(S['C_kP'] + sp.Max(CPiii, 2*C_inf*M_EP)))     # L.4_P's C_P
    CrhoP = d("C_rhoP", 2*C_P*(2 + CL.T))                                          # L.4_P's region, psi <= 2 + T
    CE5s = sp.Symbol('C_E5', positive=True)
    C_dP = d("C_dP", CE5s*S['K_P']**(NP + 1)*(1 + S['S_aP'] + S['S_bP'])**(NP + 1)/sp.factorial(NP - 2))  # L.3_P (d_P)
    # L.3's recursion on Omega with L.3_P's traces as data (stage m's data Tr_m in place of Lemma 6.2's slice data)
    Ks, a, b, T, A = CL.Ks, CL.a, CL.b, CL.T, CL.A
    K = d("K_OP", Ks + S['P6P'])
    C_tr = d("C_trP", sp.exp(2*sp.pi*K*(b - a)))
    C_N = d("C_NP", CL.C_S3*(1 + sp.sqrt(2)*sp.sqrt(b - a)*a**sp.Rational(-3, 2)))
    Tr = trace_leaves(NP)
    Ca = {1: d("CaP1", A*Ks)}
    Cb = {}
    Cc = {1: d("CcP1", C_tr*K*(A*Ks)**2)}
    for m in range(1, NP + 1):
        sa = d("saP%d" % m, sum(Ca[l] for l in range(1, m + 1)))
        sb = d("sbP%d" % m, sum(Cb[l] for l in range(1, m))) if m > 1 else sp.Integer(0)
        F2 = d("F2P_%d" % m, K*(sa**2 + sb))
        Ca[m + 1] = d("CaP%d" % (m + 1), C_tr*(Tr[m - 1] + (b - a)*K*sa*(1 + sb)))                     # (a), traces
        Cb[m] = d("CbP%d" % m, C_N*CL.C2*sp.exp(CL.C2*T)*(Tr[m - 1] + T*F2 + T*K*Ca[m + 1]*(1 + sa)))     # (b), traces
        Cc[m + 1] = d("CcP%d" % (m + 1), C_tr*(K*(Cc[m] + Cb[m] + sa*Ca[m]) + Tr[m - 1]))                # (c), traces
    sa = d("saP", sum(Ca.values()))
    sb = d("sbP", sum(Cb.values()))
    C_dOP = d("C_dOP", K**(NP + 1)*(1 + sa + sb)**(NP + 1)/sp.factorial(NP - 2))                    # (d) on Omega
    C_L3P = d("C_L3P", sp.Max(*Cb.values()))
    kern = 1 if mutate == "kern" else 2
    C_L4P = d("C_L4P", CL.C_S*sp.exp(CL.C2*(1 + M_EP + K)*T)*(kern*S['C_95']*sp.exp(2*S['C_95']*S['C_k4'])*C_dP
                                                              + T*C_dOP))         # L.4_P (1)-(4) and L.4 step 7
    nn = n_s*(n_s + sp.Rational(3, 5))
    ex_N = Kp - 8 - (2 if mutate == "expo" else 4)*beta0
    terms = {
        'lam_F': (8*S['C_F']**2*sp.exp(6*S['C_F'])*M_F)**sp.Rational(-1, Kp - 5),
        'lam_mF': sp.Min(S['eps_P']/(2*nn*S['C_kP']), (S['eps_P']/(4*nn*S['C_93']*M_F))**sp.Rational(1, Kp - 3)),
        'lam_N': (4*S['C_9']*M_N)**(-sp.Integer(1)/ex_N),
        'lam_abs': 1/(8*S['C_abs']),
        'lam_mN': (S['eps_P']/(2*nn*S['C_93']*M_N*(1 + S['C_kP'])))**(sp.Integer(1)/(Kp - 3 - 2*beta0)),
        'lam_EP': sp.Min(e1_s/(2*S['C_kP']), (sp.Min(e1_s, eps2)/(4*C_inf*M_EP))**sp.Rational(1, K_EX - 3),
                         (2*C_dw*M_EP)**sp.Rational(-1, K_EX - 4), 1/(C3s*C_nl*M_EP**2)),
    }
    tnodes = {k: d(k, v_) for k, v_ in terms.items()}
    lamP = d("lambda_P", sp.Min(sp.Symbol('lam1', positive=True), sp.Symbol('d0', positive=True)/20, 1,
                                *tnodes.values()))
    return d, dict(C_P=C_P, C_rhoP=CrhoP, C_L3P=C_L3P, C_L4P=C_L4P, lambda_P=lamP, C_dP=C_dP, M_EP=M_EP,
                   M_N=M_N, M_F=M_F, terms=tnodes)


def certP():
    c = dict(CERT2)
    c.update({sp.Symbol('C_E5', positive=True): sp.Rational(str(mp.nstr(mp.mpf(CE5._mpi_[1]), 20))),
              sp.Symbol('lam1', positive=True): sp.Rational(str(mp.nstr(mp.mpf(LAM1._mpi_[0]), 20))),
              sp.Symbol('d0', positive=True): sp.Rational(str(mp.nstr(mp.mpf(D0._mpi_[0]), 20)))})
    return c


def tableP(leaf, NP, beta0):
    """an independent transcription (mpmath, written from R9.1's display line by line)"""
    mp.mp.dps = 40
    g = lambda nm: mp.mpf(sp.N(leaf[sp.Symbol(nm, positive=True)], 40))           # noqa: E731
    n, e1, Tn, Cs, C2, Ks, a, b, CS3, A, C3v, Ci, Cdw, Cnl, e2 = [g(x) for x in (
        'n', 'eps1', 'T', 'C_S', 'C2', 'K_s', 'a', 'b', 'C_S3', 'A', 'C3', 'C_inf', 'C_dw', 'C_nl', 'eps2')]
    P = {k: g(k) for k in PLEAVES}
    CE5v, lam1, d0 = g('C_E5'), g('lam1'), g('d0')
    Kp = NP - 1
    MF = 4*P['C_F']*mp.exp(6*P['C_F'])*P['C_R'] + 1                               # 9.8: M_F := 4 C e^(6C) C_R + 1
    MN = 8*P['C_9']*P['C_pr']*(MF + P['C_R'] + 1)                                 # 9.9: B := 8 C C' (M_F + C_R + 1)
    Piii = P['C_93']*max(2*MF, MN*(1 + P['C_kP']))                                # (P-iii): Lemma 9.3 (a)
    MEP = C3v*(MN + 1 + P['C_RO']) + 1                                            # Theorem E's M, data M_N
    nn = n*(n + mp.mpf(3)/5)                                                      # n^2/(1 - n eps1)
    CP = nn*(P['C_kP'] + max(Piii, 2*Ci*MEP))
    CrhoP = 2*CP*(2 + Tn)
    CdP = CE5v*P['K_P']**(NP + 1)*(1 + P['S_aP'] + P['S_bP'])**(NP + 1)/mp.factorial(NP - 2)
    K = Ks + P['P6P']
    Ctr = mp.exp(2*mp.pi*K*(b - a))
    CN = CS3*(1 + mp.sqrt(2)*mp.sqrt(b - a)*a**mp.mpf(-1.5))
    Ca, Cb, Cc = {1: A*Ks}, {}, {1: Ctr*K*(A*Ks)**2}
    for m in range(1, NP + 1):
        tr = g('Tr%d' % m)
        sa = sum(Ca[l] for l in range(1, m + 1))
        sb = sum(Cb[l] for l in range(1, m))
        Ca[m + 1] = Ctr*(tr + (b - a)*K*sa*(1 + sb))
        Cb[m] = CN*C2*mp.exp(C2*Tn)*(tr + Tn*K*(sa**2 + sb) + Tn*K*Ca[m + 1]*(1 + sa))
        Cc[m + 1] = Ctr*(K*(Cc[m] + Cb[m] + sa*Ca[m]) + tr)
    sa, sb = sum(Ca.values()), sum(Cb.values())
    CdO = K**(NP + 1)*(1 + sa + sb)**(NP + 1)/mp.factorial(NP - 2)
    CL3P = max(Cb.values())
    CL4P = Cs*mp.exp(C2*(1 + MEP + K)*Tn)*(2*P['C_95']*mp.exp(2*P['C_95']*P['C_k4'])*CdP + Tn*CdO)
    lamF = (8*P['C_F']**2*mp.exp(6*P['C_F'])*MF)**(-mp.mpf(1)/(Kp - 5))
    lamMF = min(P['eps_P']/(2*nn*P['C_kP']), (P['eps_P']/(4*nn*P['C_93']*MF))**(mp.mpf(1)/(Kp - 3)))
    lamN = (4*P['C_9']*MN)**(-1/(Kp - 8 - 4*mp.mpf(beta0)))
    lamAbs = 1/(8*P['C_abs'])
    lamMN = (P['eps_P']/(2*nn*P['C_93']*MN*(1 + P['C_kP'])))**(1/(Kp - 3 - 2*mp.mpf(beta0)))
    lamEP = min(e1/(2*P['C_kP']), (min(e1, e2)/(4*Ci*MEP))**(mp.mpf(1)/3), (2*Cdw*MEP)**(-mp.mpf(1)/2),
                1/(C3v*Cnl*MEP**2))
    lamP = min(lam1, d0/20, 1, lamF, lamMF, lamN, lamAbs, lamMN, lamEP)
    return dict(C_P=CP, C_rhoP=CrhoP, C_L3P=CL3P, C_L4P=CL4P, lambda_P=lamP)


def c3(control=False):
    NP0, b00 = 18, 2                                         # beta0 = 2 (C_9 <= 1/4): N_P = K + 12, as R8.3 takes it
    if control:
        d, nodes = build_P(NP0, b00, mutate="leaf")
        allowed = LAMBDA0 | set(certP()) | CL.SEED | set(PS.values()) | set(trace_leaves(NP0))
        planted = bool(d.leaves() - allowed)
        mism = []
        for mut in ("kern", "expo"):
            d2, nodes2 = build_P(NP0, b00, mutate=mut)
            rng = random.Random(5)
            leaf = certP()
            leaf.update({s_: sp.Rational(rng.randint(20, 150), 100) for s_ in sorted(d2.leaves() - set(certP()),
                                                                                       key=str)})
            leaf[PS['C_9']] = sp.Rational(1, 5)
            v = d2.value(leaf)
            t = tableP(leaf, NP0, b00)
            mism.append(any(abs(mp.mpf(sp.N(v[nodes2[k]], 40)) - t[k]) > mp.mpf(10)**-25*abs(t[k])
                            for k in ('C_L4P', 'lambda_P')))
        return not (planted and all(mism))                   # the control passes only if something is missed
    d, nodes = build_P(NP0, b00)
    allowed = LAMBDA0 | set(certP()) | CL.SEED | set(PS.values()) | set(trace_leaves(NP0))
    extra = d.leaves() - allowed
    cp = certP()
    mono_nodes = [nodes[k] for k in ('C_P', 'C_rhoP', 'C_L3P', 'C_L4P')]
    structural = all(CL.positive_tree(e.subs(cp)) for s_, e in d.defs if s_ in set(mono_nodes) or not str(
        s_).startswith('lam'))
    termpos = True                                        # every term of lambda_P positive (checked at each point)
    rng = random.Random(33)
    leaves = sorted(d.leaves() - set(cp), key=str)
    fd = True
    for _ in range(30):
        pt = dict(cp)
        pt.update({s_: sp.Rational(rng.randint(20, 150), 100) for s_ in leaves})
        pt[PS['C_9']] = sp.Rational(rng.randint(5, 25), 100)                       # C_9 <= 1/4: beta0 = 2
        k = rng.choice(leaves)
        pt2 = dict(pt)
        pt2[k] = pt[k]*sp.Rational(101, 100)
        if k == PS['C_9'] and pt2[k] > sp.Rational(1, 4):
            continue
        v1, v2 = d.value(pt), d.value(pt2)
        termpos &= all(v1[t] > 0 for t in nodes['terms'].values())
        fd &= all(v2[c] - v1[c] >= 0 for c in mono_nodes)
        sgn = 1 if k == PS['eps_P'] else -1
        fd &= all(sgn*(v2[t] - v1[t]) >= -mp.mpf(10)**-30 for t in nodes['terms'].values())
    worst = mp.mpf(0)
    rng = random.Random(44)
    for _ in range(20):
        leaf = dict(cp)
        leaf.update({s_: sp.Rational(rng.randint(20, 150), 100) for s_ in leaves})
        leaf[PS['C_9']] = sp.Rational(rng.randint(5, 25), 100)
        v = d.value(leaf)
        t = tableP(leaf, NP0, b00)
        for k in ('C_P', 'C_rhoP', 'C_L3P', 'C_L4P', 'lambda_P'):
            worst = max(worst, abs(mp.mpf(sp.N(v[nodes[k]], 40)) - t[k])/abs(t[k]))
    trans = worst < mp.mpf(10)**-25
    # the illustration: every uncertified leaf 1 (then beta0 = 5, N_P = 30)
    NPi, b0i = NP_of(1), beta0_of(1)
    di, nodi = build_P(NPi, b0i)
    ill = dict(cp)
    ill.update({s_: 1 for s_ in di.leaves() - set(cp)})
    vi = di.value(ill)
    lg = lambda x: mp.nstr(mp.log10(mp.mpf(sp.N(vi[x], 30))), 6)                   # noqa: E731
    which = min(nodi['terms'], key=lambda k: sp.N(vi[nodi['terms'][k]], 30))
    ok = not extra and structural and termpos and fd and trans
    out("  C3 Theorem 2's constants as a DAG (%d named constants at N_P = 18): its uncertified leaves are Theorem P's %s,"
        " the traces Tr1..Tr18, lambda0's %s and the seed's %s; outside these and the certified numbers (C_E5 = pi"
        " sqrt(2 d1) <= %s, lam1 >= %s, d0 >= %s): %s; C_P, C_rhoP, C_L3P, C_L4P increasing and every term of lambda_P"
        " decreasing (eps_P: increasing) in every leaf at beta0 = 2, structurally %s, %s, by finite differences %s; an"
        " independent transcription at 20 random points: largest relative difference %s: %s.  Illustration (every"
        " uncertified leaf 1, so beta0 = 5, N_P = 30): log10 C_P = %s, log10 C_rhoP = %s, log10 C_L3P = %s, log10"
        " C_L4P = %s, lambda_P = %s (binding %s)"
        % (len(d.defs), sorted(PLEAVES), sorted(map(str, (set(leaves) & LAMBDA0))), sorted(map(str, set(leaves) &
                                                                                            CL.SEED)),
           up(CE5, 4), dn(LAM1, 6), dn(D0, 4), sorted(map(str, extra)) or "none", structural, termpos, fd,
           mp.nstr(worst, 3), trans, lg(nodi['C_P']), lg(nodi['C_rhoP']), lg(nodi['C_L3P']), lg(nodi['C_L4P']),
           mp.nstr(mp.mpf(sp.N(vi[nodi['lambda_P']], 30)), 5), which))
    return ok


# ------------------------------------------------------------------------------------------------------------ C4
CENSUS = [  # (a distinctive substring of the line, class, the term of lambda_P or the reason it sets none)
    ("There is beta0 > 0, depending on the seed", "X", "beta0's existence; its value is (9.9)'s, in N_P"),
    ("there are lam_P > 0 and C with the following", "T", "lambda_P itself: the minimum of the terms below"),
    ("eps_U > 0 so small that the class lies", "X", "the uniqueness class's constant, not a condition on lam"),
    ("eps_P, the margin's letter]", "X", "an amendment note"),
    ("(f) There is eps_P > 0 such that for every Lorentzian", "T", "eps_P: lam_mF, lam_mN"),
    ("with |g^-1 - g0^-1| <= eps_P t^(-5/4), B and", "T", "eps_P: lam_mF, lam_mN"),
    ("(delta small, the region in U)", "X", "a local continuation step in tau, no lam"),
    ("All constants depend on P (a, a1, a2, d0, d1, kappa)", "T", "lam1, d0/20"),
    ("was \"0 < lam <= lam1\"; Lemma 9.4 needs lam <= d0/20", "T", "d0/20"),
    ("satisfies (M1)-(M6) on A_P(tau) for 0 < lam <= min(lam1, d0/20)", "T", "lam1, d0/20"),
    ("the condition lam <= d0/20 added]", "T", "d0/20"),
    ("for lam <= d0/20 (|sigma0'| <= 7)", "T", "d0/20 (and lam <= 1/10, implied by lam1)"),
    ("bound uses lam/(b - a) <= 1/20; here only Delta", "T", "lam1 <= 1/10, d0/20"),
    ("eigenvalue reaches 1 - 1.4 < 0 at lam = 1/10", "T", "d0/20"),
    ("uniformly for 0 < lam <= 1, so |Ric^H(g_app)|", "T", "the term 1"),
    ("There are lam_F > 0 and M_F, independent of tau_n", "T", "lam_F, lam_mF"),
    ("lam <= lam_F and every tau_n < tau_T the solution", "T", "lam_F, lam_mF"),
    ("for M_F := 4 C e^(6C) C_R + 1 and lam small", "T", "lam_F"),
    ("so g_n has the margin of Lemma 9.1(f)", "T", "lam_mF"),
    ("There are beta0 >= 2 and lam_N > 0, M_N such that", "T", "lam_N, lam_abs, lam_mN"),
    ("< lam <= lam_N the solutions of Proposition 9.8", "T", "lam_N, lam_abs, lam_mN"),
    ("lam and is absorbed for lam <= lam_N", "T", "lam_abs"),
    ("of -(1/2) [box~, P] s has been absorbed", "X", "an identity of (9.9b), no lam"),
    ("terms are small, which they are: every bootstrap", "T", "lam_N"),
    ("small against B because K' = K + 3 + ceil(4 beta0)", "T", "lam_N"),
    ("The margin of Lemma 9.1(f) holds, by Lemma 9.3", "T", "lam_mN"),
    ("(T/t)^beta0 <= lam^(-2 beta0) being absorbed by", "X", "an exponent count (K' - 2 beta0 >= K), no threshold"),
    ("Theorem E with this K continues g_n to Omega", "T", "lam_EP"),
    ("- (P-iv) on Omega, the conclusions of Theorem E with this K", "T", "lam_EP"),
    ("Let gt be a Lorentzian metric on P with the margin of Lemma 9.1(f)", "X",
     "a hypothesis of Lemma 9.5, which lam_mF and lam_mN supply"),
    ("|g' - g_app| + |d(g' - g_app)| <= eps_U", "X", "the uniqueness class, not a condition on lam"),
]
PAT = re.compile(r'lam_[A-Za-z]|small|absorb|eps_U|eps_P|lam1|d0/20|lam <= 1|[Tt]here (is|are) |'
                 r'margin of Lemma 9\.1|Theorem E with this K')


def section9(text):
    i = text.index("\n## 9. Theorem P")
    j = text.index("\n### 9.5", i)
    return text[i + 1:j], text[:i + 1].count('\n') + 1


def c4(control=False):
    text = open(PROOF, encoding='utf-8').read()
    md5 = hashlib.md5(text.encode()).hexdigest()
    sec, l0 = section9(text)
    lines = sec.split('\n')
    if control:
        lines = lines + ["for lam small enough by compactness the bound holds"]
    hits = [(l0 + i, ln) for i, ln in enumerate(lines) if PAT.search(ln)]
    unclassified = [(k, ln) for k, ln in hits if not any(s_ in ln for s_, _, _ in CENSUS)]
    used = {s_ for s_, _, _ in CENSUS if any(s_ in ln for _, ln in hits)}
    stale = [s_ for s_, _, _ in CENSUS if s_ not in used]
    if control:
        return not unclassified
    names = ['lam1', 'd0/20', 'the term 1', 'lam_F', 'lam_mF', 'lam_N', 'lam_abs', 'lam_mN', 'lam_EP']
    covered = {nm: any(nm in why for s_, c, why in CENSUS if c == "T" and s_ in used) for nm in names}
    nT = sum(1 for k, ln in hits if any(s_ in ln and c == "T" for s_, c, _ in CENSUS))
    ok = not unclassified and not stale and all(covered.values())
    out("  C4 census of N1STAR-PROOF.md (md5 %s) sections 9.1-9.4, lines %d-%d (located by content): %d lines with a"
        " threshold phrase, %d of class T and %d of class X; unclassified: %s; table rows matching no line: %s; every"
        " term of lambda_P (%s) has a T line: %s"
        % (md5[:8], l0, l0 + len(lines) - 1, len(hits), nT, len(hits) - nT, unclassified or "none", stale or "none",
           ", ".join(names), all(covered.values())))
    return ok


# ------------------------------------------------------------------------------------------------------------ C5
def e_cf(delta, beta0=2, admit_w1=False):
    """E_cf(delta): the conditions of R8.3 whose gamma involves no uncertified leaf, at N_P = K + 4 + ceil(4 beta0)"""
    lB, Ib = L25.inputs()
    K = K_EX
    NP = K + 4 + int(mp.ceil(4*mp.mpf(beta0)))
    MP = 2*NP + 8
    while len(lB) <= MP:
        lB = L25.bump_bounds(MP)
        L25.CACHE['lB'] = lB
    s = iv.sqrt((3 + delta)*L25.LN10)
    L2 = L25.L2
    gam_J = iv.log(4*iv.pi)/L25.LN10                     # gamma_J = log10(4 pi + C_rho) >= log10(4 pi)
    rows = [("H1", L25.threshold(2 + delta, 4*s*L2, L2 + lB[4] + 12*L2, iv.mpf(0))),
            ("H2", L25.threshold(delta, MP*s*L2, L2 + lB[MP] + 3*MP*L2, iv.mpf(0))),
            ("J", L25.threshold(iv.mpf(1), s*L2, 3*L2, iv.mpf(0), gam_J))]
    yh = (2*iv.sqrt(3 + delta) + iv.sqrt(4*(3 + delta) + iv.mpf('1.6')))/iv.mpf('0.8')
    rows.append(("Lh", yh*yh/L25.LN10))
    nmin = ((MP + 1)*iv.log(2) - 1)/2
    rows.append(("Tl", nmin*nmin/((3 + delta)*L25.LN10)))
    if admit_w1:
        N = K + 3
        Ms = 2*N + 8
        rows.append(("W1", L25.threshold(N - iv.mpf('8.4') - delta, (Ms + 1)*s*L2,
                                         L25.lg(27/Ib) + lB[Ms] + 3*(Ms + 1)*L2, -L25.lg(iv.mpf(4)))))
    worst = max(rows, key=lambda x: x[1].b)
    return worst, rows, NP, MP


def direct_cf(E, delta, MP, lB):
    E = mp.mpf(E)
    d = mp.mpf(delta)
    n = int(mp.ceil(mp.sqrt((3 + d)*E*mp.log(10))))
    lh = -n*n/mp.log(10)
    ls = (n + 2)*mp.log10(2)
    lb = [mp.mpf(x._mpi_[1]) for x in lB]
    le = lambda k: mp.log10(2) + lh + k*ls + lb[k]                                # noqa: E731
    ok = lh >= -(mp.mpf('3.4') + d)*E and lh <= -(3 + d)*E
    ok &= mp.e**(2*n + 1) >= 2**(MP + 1)
    ok &= le(4) <= -E
    ok &= le(MP) <= -3*E
    ok &= -(n + 2)*mp.log10(2) >= mp.log10(4*mp.pi) - E
    return bool(ok)


GAMMA_DEPS = {"H1": set(), "H2": set(), "Lh": set(), "Tl": set(), "J": {"C_rho"},
              "W1": {"C_L1", "C_L4"}, "M1": {"C_L1", "C_L3"}, "W2": {"C_L1", "C_L4P"}, "M2": {"C_L1", "C_L3P"}}
UNCERT = {"C_L3", "C_L4", "C_L3P", "C_L4P"}             # C_rho enters only as log10(4 pi + C_rho) >= log10(4 pi)


def c5(control=False):
    if control:
        (nm, E), rows, NP, MP = e_cf(iv.mpf(1)/2, admit_w1=True)
        dep_ok = all(not (GAMMA_DEPS[r_[0]] & UNCERT) for r_ in rows)
        return dep_ok                                     # W1 admitted: its gamma depends on C_L4, so this is False
    lines, ok = [], True
    for delta, lab in ((iv.mpf(1)/10, "1/10"), (iv.mpf(1)/2, "1/2")):
        (nm, E), rows, NP, MP = e_cf(delta)
        dep_ok = all(not (GAMMA_DEPS[r_[0]] & UNCERT) for r_ in rows)
        lB = L25.CACHE['lB']
        E0 = mp.mpf(E._mpi_[1])
        dok = all(direct_cf(E0*(1 + mp.mpf(i)/50), float(delta.a), MP, lB) for i in range(200))
        mono = []
        for b0 in (sp.Rational(9, 4), 3, 5):
            (nm2, E2), rows2, _, _ = e_cf(delta, beta0=b0)
            mono.append(dict(rows2)["H2"].a)
        h2 = dict(rows)["H2"]
        incr = h2.b <= mono[0] and all(mono[i] <= mono[i + 1] for i in range(len(mono) - 1))
        ok &= dep_ok and dok and incr
        lines.append("delta = %s: E_cf = %s (binding %s; %s), so lambda_25 <= 10^(-%s) whatever the leaves are; direct"
                     " evaluation at 200 points beyond: %s; E_H2 at beta0 = 2, 9/4, 3, 5: %s, %s, %s, %s (increasing: %s)"
                     % (lab, dn(E, 1), nm, ", ".join("%s %s" % (r_[0], up(r_[1], 1)) for r_ in rows), dn(E, 1), dok,
                        dn(h2, 1), *[mp.nstr(mp.mpf(x), 7) for x in mono], incr))
    # the illustration of the whole formula: every uncertified leaf 1, lambda0 = 0.00244
    CL1 = mp.mpf(cl1_value()._mpi_[1])
    d1, CL3, C1, Crho1, C4, inv = build1()
    ill1 = dict(CERT2)
    ill1.update({s_: 1 for s_ in d1.leaves() - set(CERT2)})
    ill1[CL.lam0] = sp.Rational(244, 100000)
    v1 = d1.value(ill1)
    NPi, b0i = NP_of(1), beta0_of(1)
    dP, nodP = build_P(NPi, b0i)
    illP = certP()
    illP.update({s_: 1 for s_ in dP.leaves() - set(certP())})
    illP[CL.lam0] = sp.Rational(244, 100000)
    vP = dP.value(illP)
    f = lambda v_, x: mp.log10(mp.mpf(sp.N(v_[x], 30)))                             # noqa: E731
    g = {"W1": iv.mpf(f(v1, C4) + mp.log10(CL1)), "M1": iv.mpf(f(v1, CL3) + mp.log10(CL1))}
    gw2, gm2 = f(vP, nodP['C_L4P']) + mp.log10(CL1), f(vP, nodP['C_L3P']) + mp.log10(CL1)
    crho = max(mp.mpf(sp.N(v1[Crho1], 30)), mp.mpf(sp.N(vP[nodP['C_rhoP']], 30)))
    lamrec = min(mp.mpf('0.00244'), mp.mpf(sp.N(v1[inv], 30)), mp.mpf(sp.N(vP[nodP['lambda_P']], 30)),
                 1/(2*mp.mpf(sp.N(vP[nodP['C_P']], 30))))
    lB, Ib = L25.inputs()
    MPi = 2*NPi + 8
    if len(lB) <= MPi:
        lB = L25.bump_bounds(MPi)
    illrows = []
    for delta, lab in ((iv.mpf(1)/10, "1/10"), (iv.mpf(1)/2, "1/2")):
        cs, s = L25.conditions(delta, K_EX, lB, Ib)
        rows = []
        for nm_, a_, b_, c_, lt in cs:
            if nm_.startswith("W2") or nm_.startswith("M2") or nm_ == "H2":
                continue                                  # Theorem 2's rows: rebuilt below at N_P = 30
            gm = g.get(nm_[:2] if nm_[0] == 'M' else nm_, iv.mpf(0))
            if nm_ == "J":
                gm = iv.log(4*iv.pi + iv.mpf(crho))/L25.LN10
            rows.append((nm_, L25.threshold(a_, b_, c_, lt, gm)))
        L2 = L25.L2
        rows.append(("W2", L25.threshold(NPi - 3 - iv.mpf('3.4') - delta, (MPi + 1)*s*L2,
                                         L25.lg(27/Ib) + lB[MPi] + 3*(MPi + 1)*L2, -L25.lg(iv.mpf(4)), iv.mpf(gw2))))
        for j in range(1, NPi + 1):
            rows.append(("M2", L25.threshold(iv.mpf(j), (4*j + 1)*s*L2, L25.lg(54/Ib) + 2*lB[2*j] + 3*(4*j + 1)*L2,
                                             -L25.lg(iv.mpf(4)) - L25.lg(iv.mpf(NPi)), iv.mpf(gm2))))
        rows.append(("H2", L25.threshold(delta, MPi*s*L2, L2 + lB[MPi] + 3*MPi*L2, iv.mpf(0))))
        yh = (2*iv.sqrt(3 + delta) + iv.sqrt(4*(3 + delta) + iv.mpf('1.6')))/iv.mpf('0.8')
        rows.append(("Lh", yh*yh/L25.LN10))
        nmin = ((MPi + 1)*iv.log(2) - 1)/2
        rows.append(("Tl", nmin*nmin/((3 + delta)*L25.LN10)))
        worst = max(rows, key=lambda x: x[1].b)
        illrows.append("delta = %s: E_25 = %s (binding %s)" % (lab, up(worst[1], 0), worst[0]))
    out("  C5 lambda_25's status: the constant-free conditions (H1, H2 and Tl at beta0 = 2, Lh, J with gamma_J >= log10"
        " 4 pi) give, certified, " + "; ".join(lines) + ".  Every other condition's gamma involves C_L3, C_L4, C_L3P or"
        " C_L4P, uncertified.  Illustration (every uncertified leaf 1, lambda0 = 0.00244; beta0 = 5, N_P = 30; C_L1"
        " certified, log10 C_L1 = %s): gamma_w = %s, gamma_m = %s, gamma_wP = %s, gamma_mP = %s, C_rho = %s, lam_rec ="
        " %s; %s (a value of the formula, not a bound)"
        % (mp.nstr(mp.log10(CL1), 5), mp.nstr(mp.mpf(g["W1"].a), 7), mp.nstr(mp.mpf(g["M1"].a), 7),
           mp.nstr(gw2, 7), mp.nstr(gm2, 7), mp.nstr(crho, 6), mp.nstr(lamrec, 5), "; ".join(illrows)))
    return ok


def main():
    ok = True
    for name, f in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4), ("C5", c5)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("lamconst5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
