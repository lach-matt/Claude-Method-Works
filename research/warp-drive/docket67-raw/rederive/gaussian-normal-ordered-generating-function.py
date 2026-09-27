#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the single-mode Gaussian normal-ordered generating function
used at research/warp-drive/fluctuation.py:27-31, 205-213, 241-261:

    <exp(s a+) exp(t a)> = exp(s a* + t a + N s t + M* s^2/2 + M t^2/2),
    N = <a+a> - |alpha|^2, M = <aa> - alpha^2;  squeezed: N = sinh^2 r, M = -e^{i delta} sinh r cosh r

Convention of the squeeze operator is Kuo-Ford (3.11)/(3.16): S+ a S = a cosh r - a+ e^{i delta} sinh r.
Exits 1 on any failed check.  Reads nothing from the repository.
"""
import sys, itertools
import sympy as sp
import mpmath as mp

fails = []
def chk(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok: fails.append(name)

# ---------------------------------------------------------------- 1. symbolic proof (pure squeezed vacuum)
s, t = sp.symbols('s t')
r = sp.symbols('r', positive=True)
d = sp.symbols('delta', real=True)
sh, ch = sp.sinh(r), sp.cosh(r)
E = sp.exp(sp.I*d)
N = sh**2
M = -E*sh*ch
Mc = sp.conjugate(M)
G = sp.exp(N*s*t + Mc*s**2/2 + M*t**2/2)
# annihilator of |psi> = S|0>:  b = S a S+ = a cosh r + a+ e^{i delta} sinh r  (from KF 3.16 inverted)
# so a|psi> = -kappa a+|psi>, kappa = e^{i delta} tanh r;  <psi|a+ = -conj(kappa) <psi|a
kap = E*sh/ch; kapc = sp.conjugate(kap)
# commutation: <psi| a e^{s a+} e^{t a}|psi> = dG/dt + s G ;  e^{ta} a+ = (a+ + t) e^{ta}
pde1 = sp.diff(G, s) + kapc*(sp.diff(G, t) + s*G)     # d_s G = <a+ ...> = -kappa* <a ...>
pde2 = sp.diff(G, t) + kap*(sp.diff(G, s) + t*G)      # d_t G = <... a> = -kappa <... a+>
chk("ansatz solves annihilator PDE (s)", sp.simplify(sp.expand(pde1/G)) == 0)
chk("ansatz solves annihilator PDE (t)", sp.simplify(sp.expand(pde2/G)) == 0)
# uniqueness: the two PDEs are linear in (d_s G, d_t G) with determinant 1 - |kappa|^2 = sech^2 r > 0,
# so grad log G is fixed as a linear function of (s,t); with G(0,0)=1 the solution is unique.
Gs, Gt = sp.symbols('Gs Gt')
sol = sp.solve([Gs + kapc*(Gt + s), Gt + kap*(Gs + t)], [Gs, Gt], dict=True)[0]
det = sp.simplify(1 - kap*kapc)
chk("determinant 1-|kappa|^2 = sech^2 r (nonzero)", sp.simplify(det - 1/ch**2) == 0)
chk("unique grad log G equals (N t + M* s, N s + M t)",
    sp.simplify(sol[Gs] - (N*t + Mc*s)) == 0 and sp.simplify(sol[Gt] - (N*s + M*t)) == 0)
# displacement: D+ a D = a + alpha  => factor exp(s alpha* + t alpha), and N, M are the central moments
# (checked numerically in part 2, where alpha != 0).
# pure-state constraint
chk("pure squeezed state: |M|^2 = N(N+1)", sp.simplify(sp.expand(M*Mc - N*(N+1))) == 0)

# ---------------------------------------------------------------- 2. numeric Fock control, squeezed COHERENT state
mp.mp.dps = 50
def gen_moments(alpha, NN, MM, order):
    """<a+^m a^n> from derivatives of the generating function (exact via sympy series)."""
    S_, T_ = sp.symbols('S_ T_')
    g = sp.exp(S_*sp.conjugate(alpha) + T_*alpha + NN*S_*T_ + sp.conjugate(MM)*S_**2/2 + MM*T_**2/2)
    out = {}
    for m in range(order+1):
        for n in range(order+1-m):
            out[(m, n)] = complex(sp.N(sp.diff(g, S_, m, T_, n).subs({S_: 0, T_: 0}), 30))
    return out

def fock_moments_pure(vec, order):
    def low(v): return [mp.sqrt(j+1)*v[j+1] for j in range(len(v)-1)] + [mp.mpc(0)]
    out = {}
    pw = [list(vec)]
    for k in range(order): pw.append(low(pw[-1]))
    for m in range(order+1):
        for n in range(order+1-m):
            out[(m, n)] = complex(mp.fsum(mp.conj(x)*y for x, y in zip(pw[m], pw[n])))
    return out

def squeezed_coherent_vec(alpha, rr, dd, nmax):
    # S|0> in Fock basis (KF convention), then D(alpha) applied as exp(alpha a+ - alpha* a) by matrix exp
    tt = mp.tanh(rr)
    v = [mp.mpc(0)]*(nmax+1)
    for k in range(nmax//2+1):
        v[2*k] = (-mp.exp(1j*dd)*tt)**k * mp.sqrt(mp.factorial(2*k))/(2**k*mp.factorial(k))/mp.sqrt(mp.cosh(rr))
    A = mp.matrix(nmax+1, nmax+1)
    for j in range(nmax):
        A[j, j+1] = mp.sqrt(j+1)             # a
    Ad = A.transpose_conj() if hasattr(A, 'transpose_conj') else A.H
    Dm = mp.expm(alpha*Ad - mp.conj(alpha)*A)
    w = Dm*mp.matrix(v)
    return [w[i] for i in range(nmax+1)]

rr, dd, al = mp.mpf('0.45'), mp.mpf('0.8'), mp.mpc('0.6', '-0.35')
nmax = 90
vec = squeezed_coherent_vec(al, rr, dd, nmax)
order = 6
F = fock_moments_pure(vec, order)
NN = F[(1, 1)] - abs(complex(al))**2
MM = F[(0, 2)] - complex(al)**2
chk("Fock N equals sinh^2 r", abs(NN - float(mp.sinh(rr)**2)) < 1e-12)
chk("Fock M equals -e^{i delta} sinh r cosh r (KF sign)",
    abs(MM - complex(-mp.exp(1j*dd)*mp.sinh(rr)*mp.cosh(rr))) < 1e-12)
Gm = gen_moments(sp.nsimplify(complex(al).real) + sp.I*sp.nsimplify(complex(al).imag),
                 sp.Float(NN.real, 30), sp.Float(MM.real, 30) + sp.I*sp.Float(MM.imag, 30), order)
err = max(abs(Gm[k] - F[k])/max(1, abs(F[k])) for k in F)
chk("squeezed coherent: all <a+^m a^n>, m+n<=6, generating fn = Fock (max rel err %.1e)" % err, err < 1e-10)

# ---------------------------------------------------------------- 3. mixed Gaussian (squeezed thermal) -- the general hypothesis
nb = mp.mpf('0.3'); q = nb/(1+nb); nm = 70
A = mp.matrix(nm+1, nm+1)
for j in range(nm): A[j, j+1] = mp.sqrt(j+1)
Ad = A.H
Sop = mp.expm((mp.exp(-1j*dd)*rr*A*A - mp.exp(1j*dd)*rr*Ad*Ad)/2)   # KF (3.11)
rho_th = mp.diag([(1-q)*q**k for k in range(nm+1)])
rho = Sop*rho_th*Sop.H
def tr_mom(m, n):
    X = mp.eye(nm+1)
    for _ in range(m): X = X*Ad
    for _ in range(n): X = X*A
    return complex(sum((rho*X)[i, i] for i in range(nm+1)))
# only low orders are trusted against truncation; the state is concentrated at small n
Fm = {(m, n): tr_mom(m, n) for m in range(5) for n in range(5 - m)}
N2, M2 = Fm[(1, 1)], Fm[(0, 2)]
Gm2 = gen_moments(0, sp.Float(N2.real, 30), sp.Float(M2.real, 30) + sp.I*sp.Float(M2.imag, 30), 4)
err2 = max(abs(Gm2[k] - Fm[k])/max(1, abs(Fm[k])) for k in Fm)
chk("squeezed THERMAL (mixed Gaussian), m+n<=4: generating fn = trace (max rel err %.1e)" % err2, err2 < 1e-8)
chk("  mixed: |M|^2 < N(N+1) strictly (so the result is not only the pure case)",
    abs(M2)**2 < N2.real*(N2.real+1) - 1e-6)

# ---------------------------------------------------------------- 4. negative control: a NON-Gaussian state must fail
eps = mp.mpf('0.1')
v2 = [1/mp.sqrt(1+eps**2), 0, eps/mp.sqrt(1+eps**2)] + [0]*10
F2 = fock_moments_pure([mp.mpc(x) for x in v2], 4)
Gm3 = gen_moments(0, sp.Float(F2[(1, 1)].real, 30), sp.Float(F2[(0, 2)].real, 30), 4)
err3 = max(abs(Gm3[k] - F2[k]) for k in F2)
chk("GUARD: vacuum+2 (KF 2.15, non-Gaussian) violates it (max abs dev %.3e)" % err3, err3 > 1e-3)

# ---------------------------------------------------------------- 5. downstream: zero-mean Gaussian Wick and KF (3.22)
K, z, w = sp.symbols('K z w')
S_, T_ = sp.symbols('S_ T_')
sv, cv = sp.symbols('s_v c_v', positive=True)
Nn, Mm = sv**2, -w*sv*cv
g0 = sp.exp(Nn*S_*T_ - sv*cv/w*S_**2/2 + Mm*T_**2/2)          # alpha=0, |w|=1 so M* = -s c / w
def ev(P):
    return sp.expand(sum(c*sp.diff(g0, S_, m, T_, n).subs({S_: 0, T_: 0}) for (m, n), c in P.items()))
T1 = {(1, 1): 2*K, (0, 2): -z*K, (2, 0): -K/z}
T2 = {}
for (m1, n1), a1 in T1.items():
    for (m2, n2), a2 in T1.items():
        T2[(m1+m2, n1+n2)] = T2.get((m1+m2, n1+n2), 0) + a1*a2
rho0, T20 = ev(T1), ev(T2)
kf322 = 2*K*sv*(cv*(z+1/z)/2 + sv)
chk("KF (3.22) rho reproduced at w=1", sp.simplify(sp.expand(rho0.subs(w, 1) - kf322)) == 0)
chk("zero-mean Gaussian: <:T^2:> = 3 <:T:>^2 identically (any w, s, c)",
    sp.simplify(sp.expand(T20 - 3*rho0**2)) == 0)

print()
print("RESULT:", "ALL %d CHECKS PASS" % 0 if False else ("FAILED: %s" % fails if fails else "all checks pass"))
sys.exit(1 if fails else 0)
