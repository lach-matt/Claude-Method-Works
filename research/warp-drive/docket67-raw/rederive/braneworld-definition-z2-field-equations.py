#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key braneworld-definition-z2-field-equations.

Checks, all symbolic (sympy), exit 1 on any failure:
 C1  Einstein tensor of ds^2 = e^{-2A(y)} eta_{mu nu} dx dx + dy^2 (5D), generic A.
 C2  RS2 (hep-th/9906064 eq 4-5): A = k|y| solves G_AB + Lam g_AB = kappa^2 T_AB with
     Lam = -6k^2 (kappa-units), brane tension lambda = 6k/kappa^2; equals RS's
     V = 24 M^3 k, Lam_RS = -24 M^3 k^2 under kappa^2 = 1/(4 M^3); SMS Lambda_4 = 0.
 C3  The delta-coefficient of G_mu nu equals the Israel condition as the TREE writes it
     ([K_ab] - h_ab[K] = -8 pi G_5 S_ab, latticectc.py:79-80) and as SMS eq 15 writes it
     ([K] = -kappa^2 (S - q S/3)): the two forms are one statement (trace inversion, d=4).
 C4  Z2 is NOT needed for a solution: A = k1 y (y>0), k2 |y| (y<0), k1 != k2, solves the
     bulk equations on each side (Lam_+- = -6 k_+-^2) and the junction condition with
     tension 3(k1+k2)/kappa^2.  Z2 is an extra hypothesis (SMS: 'we impose').
 C5  Thick brane: smooth A (ln cosh) sourced by a bulk scalar with kappa^2 phi'^2 = 3 A'':
     field equations hold, NO delta source, NO junction condition, NO brane action.
 C6  NEC for this warp class <=> A'' >= 0: RS positive-tension brane satisfies it; a
     negative-tension brane (RS1's second brane) violates it at the brane.
"""
import sys
import sympy as sp

fails = []
def chk(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

t, x1, x2, x3, y = sp.symbols('t x1 x2 x3 y', real=True)
X = [t, x1, x2, x3, y]
A = sp.Function('A')(y)
eta = sp.diag(-1, 1, 1, 1)
g = sp.zeros(5)
for i in range(4):
    g[i, i] = sp.exp(-2*A)*eta[i, i]
g[4, 4] = 1
gi = g.inv()

def christoffel(g, gi):
    n = 5
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(n))/2)
    return G

Gam = christoffel(g, gi)
def ricci():
    n = 5
    R = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n))
                                  - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
                                  + sum(Gam[a][a][d]*Gam[d][b][c] for a in range(n) for d in range(n))
                                  - sum(Gam[a][c][d]*Gam[d][b][a] for a in range(n) for d in range(n)))
    return R
Ric = ricci()
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(5) for b in range(5)))
Ein = sp.simplify(Ric - Rs*g/2)
Ap, App = sp.diff(A, y), sp.diff(A, y, 2)

# C1 mixed components
Gtt_mixed = sp.simplify((gi*Ein)[0, 0])
Gyy_mixed = sp.simplify((gi*Ein)[4, 4])
chk("C1 G^mu_nu = (6A'^2 - 3A'') delta^mu_nu", sp.simplify(Gtt_mixed - (6*Ap**2 - 3*App)) == 0)
chk("C1 G^mu_nu isotropic on the brane directions",
    all(sp.simplify((gi*Ein)[i, i] - Gtt_mixed) == 0 for i in range(1, 4)))
chk("C1 G^y_y = 6A'^2", sp.simplify(Gyy_mixed - 6*Ap**2) == 0)
chk("C1 off-diagonal G vanish", all(sp.simplify(Ein[i, j]) == 0 for i in range(5) for j in range(5) if i != j))

# C2 RS2: A = k|y| -> A' = k sgn y, A'^2 = k^2, A'' = 2 k delta(y)
k, kap, M, lam = sp.symbols('k kappa M lambda', positive=True)
Lam = sp.Symbol('Lambda', real=True)
delta = sp.Symbol('delta_y', positive=True)   # formal symbol for delta(y)
Gbrane = (6*Ap**2 - 3*App).subs({App: 2*k*delta}).subs({Ap**2: k**2}).subs(Ap, k)
Gbrane = sp.expand(6*k**2 - 3*2*k*delta)
# bulk (delta part dropped): G^A_B + Lam delta^A_B = 0 on both mu and y components
LamSol = sp.solve(sp.Eq(6*k**2 + Lam, 0), Lam)[0]
chk("C2 bulk: Lam5 (kappa-units) = -6 k^2 from G^mu_nu", LamSol == -6*k**2)
chk("C2 bulk: same Lam5 from G^y_y (consistent)", sp.simplify(6*k**2 + LamSol) == 0)
# brane: delta coefficient of G^mu_nu = kappa^2 S^mu_nu with S = -lambda q
lamSol = sp.solve(sp.Eq(-6*k, kap**2*(-lam)), lam)[0]
chk("C2 brane tension lambda = 6k/kappa^2 (SMS: k = kappa^2 lambda/6)", sp.simplify(lamSol - 6*k/kap**2) == 0)
# RS normalisation: action {-Lam_RS + 2 M^3 R} => 1/(2 kappa^2) = 2 M^3
kapRS = sp.sqrt(1/(4*M**3))
chk("C2 RS eq 5: V_brane = 24 M^3 k", sp.simplify(lamSol.subs(kap, kapRS) - 24*M**3*k) == 0)
# RS bulk: 2M^3 G_AB + (Lam_RS/2) g_AB = 0 => G^mu_nu = -Lam_RS/(4M^3) = 6k^2
LamRS = sp.solve(sp.Eq(-sp.Symbol('L')/(4*M**3), 6*k**2), sp.Symbol('L'))[0]
chk("C2 RS eq 5: Lambda_RS = -24 M^3 k^2", sp.simplify(LamRS + 24*M**3*k**2) == 0)
# SMS eq 18: Lambda_4 = kappa^2/2 (Lambda + kappa^2 lambda^2/6), with T = -Lambda g => kappa^2 Lambda_SMS = 6k^2*(-1)
LamSMS = -6*k**2/kap**2
Lam4 = kap**2/2*(LamSMS + kap**2*lamSol**2/6)
chk("C2 SMS eq 18: Lambda_4 = 0 at the RS tuning", sp.simplify(Lam4) == 0)

# C3 extrinsic curvature K_mu nu = (1/2) d_y q_mu nu with n = +d_y (from - side to + side)
q = sp.Symbol('q')  # stands for q_mu nu (proportional to it)
Kfun = lambda Aprime: -Aprime            # K_mu nu = -A' q_mu nu
Kp, Km = Kfun(k), Kfun(-k)               # y->0+: A'=k ; y->0-: A'=-k
jumpK = Kp - Km                          # coefficient of q
chk("C3 Z2 RS: [K_mu nu] = -2k q_mu nu, K+ = -K-", jumpK == -2*k and Kp == -Km)
d = 4
trK = d*jumpK
S_tree = sp.solve(sp.Eq(jumpK - trK, -kap**2*sp.Symbol('s')), sp.Symbol('s'))[0]   # S_mu nu = s q
chk("C3 tree form [K]-h[K] = -kappa^2 S gives S = -(6k/kappa^2) q = -lambda q", sp.simplify(S_tree + 6*k/kap**2) == 0)
s = sp.Symbol('s')
S_trace = d*s
sms = -kap**2*(s - S_trace/3)            # SMS eq 15 coefficient of q
chk("C3 SMS eq 15 with S = -lambda q reproduces [K] = -2k q", sp.simplify(sms.subs(s, -lamSol) - jumpK) == 0)
# General equivalence in d=4 brane dims: [K]_ab - h[K] = -k2 S  <=>  [K]_ab = -k2 (S - h S/3)
Kab, Sab, trKs, trSs, h = sp.symbols('Kab Sab trK trS h')
# trace of the tree form: trK - 4 trK = -kap^2 trS -> trK = kap^2 trS / 3
trK_from_tree = sp.solve(sp.Eq(trKs - d*trKs, -kap**2*trSs), trKs)[0]
Kab_tree = -kap**2*Sab + h*trK_from_tree
chk("C3 tree form == SMS form (general, d=4)", sp.simplify(Kab_tree - (-kap**2*(Sab - h*trSs/3))) == 0)
# delta-function check: delta-coefficient of G^mu_nu (-6k) equals -([K]-h[K]) coefficient in mixed form
chk("C3 distributional G = kappa^2 S delta equals Israel (tree form)", sp.simplify(-(jumpK - trK) - (-6*k)) == 0)

# C4 non-Z2
k1, k2 = sp.symbols('k1 k2', positive=True)
Lp, Lm = -6*k1**2, -6*k2**2
chk("C4 bulk y>0: G^mu_nu + Lam_+ = 0", sp.simplify(6*k1**2 + Lp) == 0)
chk("C4 bulk y<0: G^mu_nu + Lam_- = 0", sp.simplify(6*k2**2 + Lm) == 0)
jump_asym = Kfun(k1) - Kfun(-k2)
S_asym = sp.solve(sp.Eq(jump_asym - d*jump_asym, -kap**2*s), s)[0]
chk("C4 junction solvable, tension 3(k1+k2)/kappa^2 > 0, K+ != -K- when k1 != k2",
    sp.simplify(S_asym + 3*(k1+k2)/kap**2) == 0 and sp.simplify(Kfun(k1) + Kfun(-k2)) != 0)
# delta coefficient: A'' = (k1+k2) delta -> G^mu_nu delta part = -3(k1+k2)
chk("C4 distributional check: -3(k1+k2) = kappa^2 * S coefficient", sp.simplify(-3*(k1+k2) - kap**2*S_asym) == 0)

# C4b Israel constraint S^ab {K_ab} = [T_ab n^a n^b] (no Z2 needed): {K} = average
avgK = (Kfun(k1) + Kfun(-k2))/2          # coefficient of q_ab
lhs = (S_asym)*avgK*d                     # S^ab = s q^ab ; q^ab q_ab = 4
Tnn = lambda L: -L/kap**2                 # T^y_y = -Lam/kappa^2
rhs = Tnn(Lp) - Tnn(Lm)
chk("C4b normal-normal constraint S^ab{K_ab} = [T_nn] holds for k1 != k2", sp.simplify(lhs - rhs) == 0)

# C5 thick brane, A = b ln cosh(c y)
b, c = sp.symbols('b c', positive=True)
Ath = b*sp.log(sp.cosh(c*y))
Ap_th, App_th = sp.diff(Ath, y), sp.diff(Ath, y, 2)
chk("C5 A'' = b c^2 sech^2 >= 0, smooth, no delta", sp.simplify(App_th - b*c**2/sp.cosh(c*y)**2) == 0)
# scalar: T^A_B = d^A phi d_B phi - delta (1/2 (dphi)^2 + V); T^t_t = -(phi'^2/2 + V), T^y_y = phi'^2/2 - V
phip2 = 3*App_th/kap**2
V = sp.Symbol('V')
Vsol = sp.solve(sp.Eq(6*Ap_th**2 - 3*App_th, kap**2*(-(phip2/2 + V))), V)[0]
yy_residual = sp.simplify(6*Ap_th**2 - kap**2*(phip2/2 - Vsol))
chk("C5 G^y_y = kappa^2 T^y_y with kappa^2 phi'^2 = 3A'' and V fixed by the mu-eq", yy_residual == 0)
chk("C5 phi'^2 >= 0 everywhere (real scalar)", sp.simplify(phip2 - 3*b*c**2/(kap**2*sp.cosh(c*y)**2)) == 0)

# C6 NEC: null k = (e^{A}, 0,0,0, 1): R_AB k^A k^B = G_AB k^A k^B
kvec = sp.Matrix([sp.exp(A), 0, 0, 0, 1])
chk("C6 k null", sp.simplify((kvec.T*g*kvec)[0]) == 0)
nec = sp.simplify((kvec.T*Ein*kvec)[0])
chk("C6 G_AB k^A k^B = 3 A''  (NEC <=> A'' >= 0)", sp.simplify(nec - 3*App) == 0)
chk("C6 RS positive-tension brane: A'' = 2k delta >= 0 (NEC holds); negative tension (k->-k at that brane) violates",
    (3*2*k) > 0 and (3*2*(-k)) < 0)

print()
print("FAILURES:", len(fails))
sys.exit(1 if fails else 0)
