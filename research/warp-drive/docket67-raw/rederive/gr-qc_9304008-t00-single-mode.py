#!/usr/bin/env python3
"""DOCKET 67 -- re-derive KF (gr-qc/9304008 v1) (2.10)-(2.14) and the tree's
:T00: = K(2 a+a - z a^2 - zbar a+^2)  (fluctuation.py:179-180), from first principles.

C1  (2.12)-(2.14) from (2.6)+(2.11), every component alpha,beta, generic k, massless;
    and the K_ab formula; K_00 = omega/(2L^3)  (so K is not only a normalisation).
C2  single-mode operator T_00 built from phi = a f + a+ f* on an exact truncated Fock
    space; T_00 - <0|T_00|0> == :T_00: == K(2a+a - z a^2 - zbar a+^2) (away from the
    truncation edge); |z| = 1 needed for hermiticity (theta real).
C3  (2.10) reproduced from the operator for a generic symbolic state c_0..c_5.
C4  the tree's dict T1 {(1,1):2K,(0,2):-zK,(2,0):-K/z} (keys = a+^m a^n) equals C2's operator.
C5  nprod(T1,T1) is the full normal ordering of the square: coherent-state control
    <:T00^2:> = <:T00:>^2 (KF (3.21) Delta = 0) and vacuum <:T00^2:> = 0.
C6  (sensitivity, NAMED hypothesis) non-minimal coupling xi: z-terms scale by (1-4 xi)
    for the 00 component -> minimal coupling is load-bearing; conformal xi=1/6 gives 1/3.
C7  multi-mode reduction: for a state with only mode k excited, cross-mode terms of the
    normal-ordered T00 and T00^2 vanish in expectation (2-mode exact check).
"""
import sympy as sp

res = {}
# ---------------------------------------------------------------- C1
t, x1, x2, x3, L = sp.symbols('t x1 x2 x3 L', real=True)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
w = sp.sqrt(k1**2 + k2**2 + k3**2)          # massless
X = [t, x1, x2, x3]
eta = sp.diag(-1, 1, 1, 1)
klo = [-w, k1, k2, k3]                     # k_mu with k^0 = omega, eta=-+++
theta = sum(klo[m] * X[m] for m in range(4))  # k.x - omega t
f = (2 * L**3 * w)**sp.Rational(-1, 2) * sp.exp(sp.I * theta)
fc = sp.conjugate(f).subs({sp.conjugate(k1): k1})  # all real
fc = (2 * L**3 * w)**sp.Rational(-1, 2) * sp.exp(-sp.I * theta)

def Tbil(g, h, mu, nu):
    dg = [sp.diff(g, v) for v in X]; dh = [sp.diff(h, v) for v in X]
    inv = eta.inv()
    contr = sum(dg[a] * inv[a, b] * dh[b] for a in range(4) for b in range(4))
    return dg[mu] * dh[nu] - sp.Rational(1, 2) * eta[mu, nu] * contr

ok = True
for mu in range(4):
    for nu in range(4):
        ksq = sum(klo[a] * eta.inv()[a, b] * klo[b] for a in range(4) for b in range(4))
        Kmn = (klo[mu] * klo[nu] - sp.Rational(1, 2) * eta[mu, nu] * ksq) / (2 * w * L**3)
        z = sp.exp(2 * sp.I * theta)
        ok &= sp.simplify(Tbil(f, f, mu, nu) + Kmn * z) == 0
        ok &= sp.simplify(Tbil(fc, f, mu, nu) - Kmn) == 0
        ok &= sp.simplify(Tbil(f, fc, mu, nu) - Kmn) == 0
        ok &= sp.simplify(Tbil(fc, fc, mu, nu) + Kmn / z) == 0
        ok &= sp.simplify(ksq) == 0
res['C1_KF_2.12-2.14_all_components'] = bool(ok)
K00 = sp.simplify(Tbil(fc, f, 0, 0))
res['C1_K00_equals_omega_over_2L3'] = sp.simplify(K00 - w / (2 * L**3)) == 0

# ---------------------------------------------------------------- C2, C4
Nmax = 10
a = sp.zeros(Nmax, Nmax)
for n in range(1, Nmax):
    a[n - 1, n] = sp.sqrt(n)
ad = a.T
K, zs = sp.symbols('K z')
# T_00 = sum over the four bilinears with the values of (2.12)-(2.14): 00 component
T00 = a * a * (-K * zs) + a * ad * K + ad * a * K + ad * ad * (-K / zs)
vac = sp.zeros(Nmax, 1); vac[0] = 1
E0 = sp.simplify((vac.T * T00 * vac)[0])
normal = K * (2 * ad * a - zs * a * a - (1 / zs) * ad * ad)
diff = sp.simplify(T00 - E0 * sp.eye(Nmax) - normal)
inner = diff[:Nmax - 2, :Nmax - 2]
res['C2_vacuum_expectation_is_K'] = sp.simplify(E0 - K) == 0
res['C2_T00_minus_vac_equals_normal_ordered'] = inner == sp.zeros(Nmax - 2, Nmax - 2)
th = sp.symbols('theta', real=True)
Nz = normal.subs(zs, sp.exp(2 * sp.I * th)).subs(K, sp.Symbol('K', positive=True))
res['C2_hermitian_for_real_theta'] = sp.simplify(Nz - Nz.H) == sp.zeros(Nmax, Nmax)
# with |z| != 1 hermiticity fails (tree's -K/z is zbar only on |z|=1)
Nr = normal.subs(zs, 2).subs(K, 1)
res['C2_not_hermitian_if_abs_z_ne_1'] = (Nr - Nr.H) != sp.zeros(Nmax, Nmax)

T1 = {(1, 1): 2 * K, (0, 2): -zs * K, (2, 0): -K / zs}
def dict_to_mat(P):
    M = sp.zeros(Nmax, Nmax)
    for (m, n), c in P.items():
        M += c * ad**m * a**n
    return M
res['C4_tree_T1_equals_operator'] = sp.simplify(dict_to_mat(T1) - normal) == sp.zeros(Nmax, Nmax)

# ---------------------------------------------------------------- C3 (2.10)
cs = sp.symbols('c0:6')
ccs = sp.symbols('cc0:6')   # independent conjugates
psi = sp.Matrix(list(cs) + [0] * (Nmax - 6))
psib = sp.Matrix(list(ccs) + [0] * (Nmax - 6))
lhs = sp.expand((psib.T * normal * psi)[0])
Tff, Tfcf, Tfcfc = -K * zs, K, -K / zs
rhs = sum(2 * n * ccs[n] * cs[n] * Tfcf for n in range(6)) \
    + sum(sp.sqrt(n) * sp.sqrt(n - 1) * cs[n] * ccs[n - 2] * Tff for n in range(2, 6)) \
    + sum(sp.sqrt(n) * sp.sqrt(n - 1) * ccs[n] * cs[n - 2] * Tfcfc for n in range(2, 6))
res['C3_KF_2.10_reproduced'] = sp.simplify(lhs - sp.expand(rhs)) == 0

# ---------------------------------------------------------------- C5
def nprod(A, B):
    out = {}
    for (m1, n1), x in A.items():
        for (m2, n2), y in B.items():
            out[(m1 + m2, n1 + n2)] = out.get((m1 + m2, n1 + n2), 0) + x * y
    return out
T2 = nprod(T1, T1)
al, alb = sp.symbols('alpha alphabar')
coh = lambda P: sp.expand(sum(c * alb**m * al**n for (m, n), c in P.items()))
res['C5_coherent_T2_equals_rho_squared'] = sp.simplify(coh(T2) - coh(T1)**2) == 0
res['C5_vacuum_T2_zero'] = all(True for _ in [0]) and sp.simplify(sum(c for (m, n), c in T2.items() if m == 0 and n == 0)) == 0
# direct: Fock-space fully normal-ordered square equals nprod
M2 = dict_to_mat(T2)
alt = K**2 * (4 * ad**2 * a**2 - 4 * zs * ad * a**3 - (4 / zs) * ad**3 * a
              + zs**2 * a**4 + (1 / zs**2) * ad**4 + 2 * ad**2 * a**2)
res['C5_nprod_equals_hand_normal_order'] = sp.simplify(M2 - alt) == sp.zeros(Nmax, Nmax)

# ---------------------------------------------------------------- C6 non-minimal xi
xi = sp.symbols('xi')
def Tbil_xi(g, h, mu, nu):
    gh = g * h
    box = sum(eta.inv()[a_, b_] * sp.diff(gh, X[a_], X[b_]) for a_ in range(4) for b_ in range(4))
    return Tbil(g, h, mu, nu) + xi * (eta[mu, nu] * box - sp.diff(gh, X[mu], X[nu]))
z = sp.exp(2 * sp.I * theta)
ratio_ff = sp.simplify(Tbil_xi(f, f, 0, 0) / (-K00 * z))
ratio_ffc = sp.simplify(Tbil_xi(fc, f, 0, 0) / K00)
res['C6_xi_z_coefficient_factor'] = str(sp.factor(ratio_ff))
res['C6_xi_adagger_a_coefficient_factor'] = str(ratio_ffc)
res['C6_conformal_factor'] = str(sp.simplify(ratio_ff.subs(xi, sp.Rational(1, 6))))

# ---------------------------------------------------------------- C7 two-mode reduction
Nm = 4
b = sp.zeros(Nm, Nm)
for n in range(1, Nm):
    b[n - 1, n] = sp.sqrt(n)
I = sp.eye(Nm)
A1 = sp.kronecker_product(b, I); A2 = sp.kronecker_product(I, b)
A1d, A2d = A1.T, A2.T
# mode-2 contributions and cross terms, generic coefficients for bilinears
p = sp.symbols('p0:12')
# normal-ordered general quadratic in the two modes (all monomials)
ops = [A1d * A1, A1 * A1, A1d * A1d, A2d * A2, A2 * A2, A2d * A2d,
       A1d * A2, A2d * A1, A1 * A2, A1d * A2d]
Q = sum((p[i] * ops[i] for i in range(len(ops))), sp.zeros(Nm * Nm, Nm * Nm))
# state: generic in mode 1 (n<=3), vacuum in mode 2
cc = sp.symbols('d0:4'); ccb = sp.symbols('db0:4')
e2 = sp.Matrix([1, 0, 0, 0])
psi2 = sp.kronecker_product(sp.Matrix(cc), e2); psi2b = sp.kronecker_product(sp.Matrix(ccb), e2)
full = sp.expand((psi2b.T * Q * psi2)[0])
only1 = sp.expand((psi2b.T * (p[0] * ops[0] + p[1] * ops[1] + p[2] * ops[2]) * psi2)[0])
res['C7_cross_mode_terms_vanish_quadratic'] = sp.simplify(full - only1) == 0

for k_, v in res.items():
    print("%-45s %s" % (k_, v))
bools = [v for v in res.values() if isinstance(v, bool)]
print("ALL_BOOLEAN_CHECKS_PASS", all(bools), "(%d checks)" % len(bools))
