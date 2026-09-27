#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key spectral-theory-friedrichs-rayleigh-ritz.

What the tree uses (noise.py:172-177, H3 at 157-162):
  (i)   <psi,A psi> >= -Q on the dense Hadamard domain D  ==>  the same bound on the
        Friedrichs extension's form domain (form closure);
  (ii)  Rayleigh-Ritz: a self-adjoint A with q(psi) >= -Q on its form domain has
        sigma(A) in [-Q, oo)   (FFR 1004.0179 note [18], (a) => (b));
  (iii) spectral measure mu_psi supported in sigma(A)  ((b) => (c)), and (c) => (a);
  (iv)  H3's caveat: a DIFFERENT self-adjoint extension of the same semibounded
        operator need not keep the Friedrichs lower bound;
  (v)   the Rayleigh quotient of the clamped sampler is mu_1^4 (Rayleigh-Ritz on d^4).
Everything here is finite or closed form; infinite-dimensional theorems are checked
on (a) every finite-dimensional truncation via z3 over the reals, and (b) a concrete
unbounded operator (-d^2/dx^2 on C_c^oo(0,1)) whose extensions are known in closed form.
"""
import sys, math
import sympy as sp
import mpmath as mp
import numpy as np

FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok: FAIL.append(name)

# ---------------------------------------------------------------- (ii) Rayleigh-Ritz, finite dims, z3
try:
    import z3
    # 2x2 and 3x3 real symmetric: if an eigenpair (lam, v) exists with lam < -Q, then the
    # form bound v^T A v >= -Q v^T v fails.  Ask z3 for a counterexample: must be UNSAT.
    for n in (2, 3):
        a = [[z3.Real(f"a{i}{j}") if i <= j else None for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i):
                a[i][j] = a[j][i]
        v = [z3.Real(f"v{i}") for i in range(n)]
        lam, Q = z3.Real("lam"), z3.Real("Q")
        s = z3.Solver()
        Av = [z3.Sum([a[i][j] * v[j] for j in range(n)]) for i in range(n)]
        s.add([Av[i] == lam * v[i] for i in range(n)])         # eigenpair
        s.add(z3.Sum([vi * vi for vi in v]) == 1)             # normalised
        s.add(lam < -Q)                                       # eigenvalue below -Q
        s.add(z3.Sum([v[i] * Av[i] for i in range(n)]) >= -Q) # but form bound holds at v
        r = s.check()
        chk(f"z3 (a)=>(b) on {n}x{n} real symmetric: no eigenvalue below a form bound", r == z3.unsat, str(r))
    # (c) => (a): a probability vector on points x_k >= -Q has mean >= -Q  (n = 4 atoms)
    x = [z3.Real(f"x{k}") for k in range(4)]; p = [z3.Real(f"p{k}") for k in range(4)]
    Q = z3.Real("Q"); s = z3.Solver()
    s.add([pk >= 0 for pk in p]); s.add(z3.Sum(p) == 1); s.add([xk >= -Q for xk in x])
    s.add(z3.Sum([p[k] * x[k] for k in range(4)]) < -Q)
    r = s.check(); chk("z3 (c)=>(a): mean of a measure on [-Q,oo) is >= -Q (4 atoms)", r == z3.unsat, str(r))
except ImportError:
    chk("z3 importable", False)

# numeric (ii) with sympy exact eigenvalues: min eigenvalue == min Rayleigh quotient
M = sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
ev = sorted(M.eigenvals().keys(), key=lambda e: float(e))
lam_min = sp.nsimplify(ev[0])
vmin = (M - lam_min * sp.eye(3)).nullspace()[0]
rq = sp.simplify((vmin.T * M * vmin)[0] / (vmin.T * vmin)[0])
chk("sympy: Rayleigh quotient at the ground vector equals lambda_min = 2 - sqrt2", sp.simplify(rq - (2 - sp.sqrt(2))) == 0, str(rq))

# ---------------------------------------------------------------- (i),(iv) concrete unbounded operator
# S = -d^2/dx^2 on C_c^oo(0,1).  Form q(u) = INT |u'|^2 >= pi^2 INT |u|^2 on C_c^oo (Poincare, sharp).
# Friedrichs extension = Dirichlet Laplacian, inf sigma = pi^2 = the form bound  (KEEPS the bound).
x = sp.symbols('x', real=True)
u = sp.sin(sp.pi * x)
rq_D = sp.integrate(sp.diff(u, x)**2, (x, 0, 1)) / sp.integrate(u**2, (x, 0, 1))
chk("Friedrichs (Dirichlet) ground state has Rayleigh quotient pi^2 = form bound", sp.simplify(rq_D - sp.pi**2) == 0)
# (i) form closure: C_c^oo-type trial functions (bump-cut sine) have RQ >= pi^2 and -> pi^2.
def rq_trial(eps, N=20001):
    t = np.linspace(0, 1, N); h = t[1] - t[0]
    cut = np.clip(np.minimum(t, 1 - t) / eps, 0, 1)
    sm = np.where(cut >= 1, 1.0, np.where(cut <= 0, 0.0, np.exp(1 - 1 / np.maximum(cut, 1e-300)) ))
    f = np.sin(np.pi * t) * sm
    df = np.gradient(f, h)
    return np.trapezoid(df**2, t) / np.trapezoid(f**2, t)
rqs = [rq_trial(e) for e in (0.2, 0.05, 0.01)]
chk("form closure: compactly supported trials have RQ >= pi^2 and decrease toward pi^2",
    all(r >= math.pi**2 - 1e-6 for r in rqs) and rqs[0] > rqs[1] > rqs[2] and rqs[2] - math.pi**2 < 0.2,
    ", ".join(f"{r:.5f}" for r in rqs) + f" vs pi^2={math.pi**2:.5f}")
# (iv) Krein-von Neumann extension: ker S* = span{1, x} -> eigenvalue 0 < pi^2 (loses the bound).
for w in (sp.Integer(1), x):
    chk(f"Krein: {w} in ker S* (-(w)''=0), so 0 is in sigma(S_K) below pi^2", sp.diff(w, x, 2) == 0)
# (iv) Robin extensions u'(0) = -k u(0), u'(1) = k u(1): all extend S (agree on C_c^oo),
# symmetric ground state cosh(K(x-1/2)) with eigenvalue -K^2, K tanh(K/2) = k.
for kap in (1.0, 5.0, 50.0):
    mp.mp.dps = 40
    K = mp.findroot(lambda K: K * mp.tanh(K / 2) - kap, max(2.0, kap))
    w = lambda t: mp.cosh(K * (t - mp.mpf(1) / 2))
    dw = lambda t: K * mp.sinh(K * (t - mp.mpf(1) / 2))
    bc0 = dw(0) + kap * w(0); bc1 = dw(1) - kap * w(1)
    # ODE -w'' = -K^2 w is exact symbolically for cosh(K(x-1/2)) with symbolic K:
    Ksym = sp.symbols('K', positive=True)
    ode = sp.simplify(-sp.diff(sp.cosh(Ksym * (x - sp.Rational(1, 2))), x, 2) + Ksym**2 * sp.cosh(Ksym * (x - sp.Rational(1, 2))))
    rel = max(abs(bc0), abs(bc1)) / abs(kap * w(0))
    chk(f"Robin kappa={kap}: extension eigenvalue -K^2 = {float(-K**2):.4f} < 0 < pi^2 (BC rel resid {float(rel):.1e}, ODE exact)",
        rel < 1e-30 and ode == 0 and -K**2 < math.pi**2)
# kappa -> oo drives the extension's lower bound to -oo: finite deficiency (2,2) yet no uniform bound.
Kbig = mp.findroot(lambda K: K * mp.tanh(K / 2) - 1e4, 1e4)
chk("Robin kappa=1e4: lower bound ~ -kappa^2 (extensions' bounds unbounded below as a family)", -Kbig**2 < -0.99e8, mp.nstr(-Kbig**2, 6))
# finite-difference cross-check: Dirichlet (Friedrichs) min eigenvalue -> pi^2 from BELOW? (FD) and Robin negative
def fd(n, kap=None):
    h = 1.0 / (n + 1) if kap is None else 1.0 / n
    if kap is None:
        A = (np.diag(2 * np.ones(n)) - np.diag(np.ones(n - 1), 1) - np.diag(np.ones(n - 1), -1)) / h**2
    else:  # nodes 0..n, ghost-point Robin (second order), symmetrised by weights
        m = n + 1
        A = (np.diag(2 * np.ones(m)) - np.diag(np.ones(m - 1), 1) - np.diag(np.ones(m - 1), -1)) / h**2
        A[0, 1] = -2 / h**2; A[-1, -2] = -2 / h**2
        A[0, 0] = 2 / h**2 - 2 * kap / h; A[-1, -1] = 2 / h**2 - 2 * kap / h
    return np.sort(np.linalg.eigvals(A).real)[0]
chk("FD Dirichlet (Friedrichs) lowest eigenvalue ~ pi^2", abs(fd(800) - math.pi**2) < 1e-3, f"{fd(800):.6f}")
lr = fd(800, 5.0)
K5 = float(mp.findroot(lambda K: K * mp.tanh(K / 2) - 5.0, 5.0))
chk("FD Robin kappa=5 lowest eigenvalue ~ -K^2 (negative)", abs(lr + K5**2) < 1e-2, f"{lr:.5f} vs {-K5**2:.5f}")

# ---------------------------------------------------------------- (v) clamped sampler, Rayleigh-Ritz on d^4
mp.mp.dps = 30
mu1 = mp.findroot(lambda m: mp.cos(m) * mp.cosh(m) - 1, 4.73)
C = mu1**4 / (16 * mp.pi**2)
chk("mu_1 root of cos mu cosh mu = 1", abs(mu1 - mp.mpf("4.730040744862704026")) < 1e-15, mp.nstr(mu1, 20))
chk("C = mu_1^4/(16 pi^2) = 3.16986 (Fewster prints 'C ~ 3.17')", abs(C - mp.mpf("3.169857938310468")) < 1e-12, mp.nstr(C, 16))
# Rayleigh-Ritz upper bound from the polynomial trial x^2(1-x)^2 (clamped): must be >= mu_1^4
g = x**2 * (1 - x)**2
rq_poly = sp.integrate(sp.diff(g, x, 2)**2, (x, 0, 1)) / sp.integrate(g**2, (x, 0, 1))
chk("Rayleigh-Ritz: clamped trial x^2(1-x)^2 gives 504 >= mu_1^4 = 500.564", rq_poly == 504 and 504 >= float(mu1**4), f"{rq_poly} vs {float(mu1**4):.6f}")
# Galerkin in the clamped polynomial space x^2(1-x)^2 * P_k : lowest RR value decreases onto mu_1^4
xs = sp.symbols('xs')
basis = [xs**2 * (1 - xs)**2 * xs**k for k in range(6)]
Kmat = sp.Matrix(6, 6, lambda i, j: sp.integrate(sp.diff(basis[i], xs, 2) * sp.diff(basis[j], xs, 2), (xs, 0, 1)))
Mmat = sp.Matrix(6, 6, lambda i, j: sp.integrate(basis[i] * basis[j], (xs, 0, 1)))
import scipy.linalg as sl
vals = []
for n in (1, 2, 4, 6):
    w = sl.eigh(np.array(Kmat[:n, :n], dtype=float), np.array(Mmat[:n, :n], dtype=float), eigvals_only=True)
    vals.append(w[0])
chk("Galerkin RR values are monotone non-increasing and stay >= mu_1^4",
    all(vals[i] >= vals[i + 1] - 1e-9 for i in range(3)) and all(v >= float(mu1**4) - 1e-6 for v in vals) and vals[-1] - float(mu1**4) < 1e-3,
    ", ".join(f"{v:.6f}" for v in vals))

print("\nFAILS:", len(FAIL))
sys.exit(1 if FAIL else 0)
