#!/usr/bin/env python3
"""Independent check (not the author's code): extrinsic curvature of R = a in
ds^2 = -f dt^2 + dR^2/f + R^2 dOmega_k^2 (5D), Israel stress, J1 identity, RS control.
Convention (standard, Israel 1966 / e.g. Poisson 'Relativist's Toolkit' 3.7):
  n from V- to V+, [K] = K(V+) - K(V-),  [K_ab] - h_ab [K] = -kappa^2 S_ab.
Equivalent: sum over sides i with normal pointing INTO side i:  S = -(1/kappa^2) sum_i (K_i - h tr K_i).
"""
import sympy as sp

t, th, ph, ps = sp.symbols('t theta phi psi'); R = sp.Symbol('R', positive=True)
k = sp.Symbol('k')
f = sp.Function('f')(R)
eta = sp.Symbol('eta')  # +1: region at R > a (normal points to increasing R); -1: region at R < a

# 3-space of constant curvature k: dchi^2 + S(chi)^2 dOmega_2 ; we use generic metric functions via
# coordinates x = (t, R, chi, th, ph) with S(chi) symbolic; extrinsic curvature only needs Gamma^R_ab.
chi = sp.Symbol('chi')
S = sp.Function('S')(chi)
X = [t, R, chi, th, ph]
g = sp.diag(-f, 1/f, R**2, R**2*S**2, R**2*S**2*sp.sin(th)**2)
ginv = g.inv()

def Gamma(a, b, c):
    return sp.simplify(sum(ginv[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(5))/2)

# unit normal n_mu = eta/sqrt(f) delta^R_mu ; K_ab = nabla_a n_b = d_a n_b - Gamma^c_ab n_c  (a,b tangential)
n_low = [0, eta/sp.sqrt(f), 0, 0, 0]
tang = [0, 2, 3, 4]
K = {}
for a in tang:
    for b in tang:
        val = sp.diff(n_low[b], X[a]) - sum(Gamma(c, a, b)*n_low[c] for c in range(5))
        K[(a, b)] = sp.simplify(val)
Kmix = {a: sp.simplify(ginv[a, a]*K[(a, a)]) for a in tang}
offdiag = [K[(a, b)] for a in tang for b in tang if a != b]
print("off-diagonal K all zero:", all(sp.simplify(x) == 0 for x in offdiag))
print("K^t_t   =", sp.simplify(Kmix[0]))
print("K^chi_chi =", sp.simplify(Kmix[2]), " K^th_th =", sp.simplify(Kmix[3]), " K^ph_ph =", sp.simplify(Kmix[4]))
fp = sp.diff(f, R)
assert sp.simplify(Kmix[0] - eta*fp/(2*sp.sqrt(f))) == 0
for a in (2, 3, 4):
    assert sp.simplify(Kmix[a] - eta*sp.sqrt(f)/R) == 0
print("J0 verified: K^t_t = eta f'/(2 sqrt f), K^i_i = eta sqrt(f)/a (independent of k and S(chi))")

# J1: two sides with f1, f2 (each its own mu, L), eta1, eta2.  Sum of K_i (normal into side i).
a_ = sp.Symbol('a', positive=True)
kap = sp.Symbol('kappa', positive=True)
def side(fi, ei):
    Kt = ei*sp.diff(fi, R)/(2*sp.sqrt(fi))
    Ks = ei*sp.sqrt(fi)/R
    return Kt, Ks
f1 = sp.Function('f1')(R); f2 = sp.Function('f2')(R)
e1, e2 = sp.symbols('e1 e2')
Kt = side(f1, e1)[0] + side(f2, e2)[0]
Ks = side(f1, e1)[1] + side(f2, e2)[1]
tr = Kt + 3*Ks
St = -(Kt - tr)/kap**2      # S^t_t
Ss = -(Ks - tr)/kap**2      # S^i_i
rho = -St; p = Ss
Phi = (e1*sp.sqrt(f1) + e2*sp.sqrt(f2))/R
print("rho + (3/kappa^2) Phi =", sp.simplify(rho + 3*Phi/kap**2))
print("p - (a Phi' + 3 Phi)/kappa^2 =", sp.simplify(p - (R*sp.diff(Phi, R) + 3*Phi)/kap**2))

# RS control: k=0, mu=0, f = R^2/L^2, mirrored, region R<a (eta=-1) both sides.
L = sp.Symbol('L', positive=True)
fRS = R**2/L**2
Kt0 = 2*(-1)*sp.diff(fRS, R)/(2*sp.sqrt(fRS)); Ks0 = 2*(-1)*sp.sqrt(fRS)/R
tr0 = Kt0 + 3*Ks0
St0 = sp.simplify(-(Kt0 - tr0)/kap**2); Ss0 = sp.simplify(-(Ks0 - tr0)/kap**2)
print("RS control (mirrored, decaying, k=0, mu=0): S^t_t =", St0, " S^i_i =", Ss0,
      "-> pure tension sigma =", sp.simplify(-St0), "= 6/(kappa^2 L):", sp.simplify(-St0 - 6/(kap**2*L)) == 0)
# mutation: wrong trace (spatial only) should break the RS control's isotropy/pure-tension form
trm = 3*Ks0
Stm = sp.simplify(-(Kt0 - trm)/kap**2); Ssm = sp.simplify(-(Ks0 - trm)/kap**2)
print("mutation trace-from-spatial: S^t_t =", Stm, " S^i_i =", Ssm, " pure tension?", sp.simplify(Stm - Ssm) == 0)
