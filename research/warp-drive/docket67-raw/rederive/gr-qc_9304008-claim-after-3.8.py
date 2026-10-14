#!/usr/bin/env python3
r"""
DOCKET 67 -- audit of key gr-qc/9304008-claim-after-3.8.

Kuo & Ford, arXiv gr-qc/9304008 v1, p.6, after (3.8):
  "From Eq.(2.16), it follows that the condition for the expectation value of
   energy density to be negative is cos(2 theta) > sqrt2 eps.  In this case we
   have Delta(x) > 1."
with (3.2)  Delta = | (<:T00^2:> - <:T00:>^2) / <:T00^2:> |
and  (3.8)  Delta = (10 eps + sqrt2 cos 2theta) / (12 eps)   [as printed, v1 text layer]

Independent of research/warp-drive/fluctuation.py (no import, no shared code).
Every check prints PASS/FAIL; exit 0 iff all pass.

  C1  :T00: for one massless box mode, derived from (2.11)
  C2  exact <:T00:>, <:T00^2:> in (|0>+eps|2>)/sqrt(1+eps^2) by truncated Fock matrices
  C3  exact Delta = |1 - X^2/(3N)|, X = 2eps - sqrt2 cos2th, N = 1+eps^2
  C4  z3: exact Delta <= 1 for EVERY real eps, theta (equality only at rho > 0)
  C5  z3: rho < 0  ==>  Delta < 1 everywhere -> the claim fails at EVERY rho<0 point
  C6  z3: rho < 0  ==>  Delta > 1/3; both bounds tight (sequences)
  C7  z3: with any of the 4 combinations of KF's printed/exact rho and <:T^2:>,
          rho < 0 still gives Delta < 1 -- only (3.8) itself yields Delta > 1
  C8  z3: GIVEN (3.8), rho<0 ==> Delta_38 > 1 for all real eps != 0 (inference valid)
  C9  (3.8) = 1 - X/(12 eps): consistent with (eps X) left unsquared in rho^2
  C10 KF's sign condition cos2th > sqrt2 eps is exact for eps > 0, reversed for eps < 0
  C11 witness eps = 1/10, theta = 0: exact 0.5134, (3.8) 2.0118
  C12 numeric sweep (2e5 random points): max exact Delta on rho<0 region < 1
"""
import sys, random, math
import sympy as sp
import z3

FAIL = []
def chk(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAIL.append(name)

# ---------------------------------------------------------------- C1
t, x, om, L = sp.symbols('t x omega L', positive=True)
f = sp.exp(sp.I * (om * x - om * t)) / sp.sqrt(2 * om * L**3)   # massless: |k| = omega, k along x
fc = sp.conjugate(f)
def T00(g, h):   # (2.11) T_mn[g,h] = d_m g d_n h - (1/2) eta_mn d_s g d^s h, eta = diag(-1,1,1,1)
    # T_00 = g_t h_t - (1/2)(-1)(-g_t h_t + g_x h_x) = (1/2)(g_t h_t + g_x h_x)
    return sp.Rational(1, 2) * (sp.diff(g, t) * sp.diff(h, t) + sp.diff(g, x) * sp.diff(h, x))
K = om / (2 * L**3)                  # K_00 = omega/(2L^3), KF
theta = om * x - om * t
z_expr = sp.exp(2 * sp.I * theta)
chk("C1 T00[f,f]   = -K e^{2i theta}", sp.simplify(T00(f, f) + K * z_expr) == 0)
chk("C1 T00[f*,f*] = -K e^{-2i theta}", sp.simplify(T00(fc, fc) + K / z_expr) == 0)
chk("C1 T00[f,f*] = T00[f*,f] = K", sp.simplify(T00(f, fc) - K) == 0 and sp.simplify(T00(fc, f) - K) == 0)
# phi = a f + a+ f*  =>  :T00: = K (2 a+ a - z a^2 - zbar a+^2)

# ---------------------------------------------------------------- C2
Ks, eps = sp.symbols('K epsilon', real=True)
c2 = sp.symbols('c', real=True)                  # c = cos 2theta
s2 = sp.symbols('s', real=True)                  # s = sin 2theta
z = c2 + sp.I * s2; zb = c2 - sp.I * s2
D = 8
a = sp.zeros(D, D)
for n in range(1, D):
    a[n - 1, n] = sp.sqrt(n)
ad = a.T
def mono(m, n):          # normal-ordered a+^m a^n
    return ad**m * a**n
# commuting-symbol polynomial for :T00:, then normal-order by fiat (A = a+, B = a)
A, B = sp.symbols('A B', commutative=True)
T1 = Ks * (2 * A * B - z * B**2 - zb * A**2)
def as_op(P):
    P = sp.Poly(sp.expand(P), A, B)
    M = sp.zeros(D, D)
    for (m, n), co in P.terms():
        M += co * mono(m, n)
    return M
N = 1 + eps**2
psi = sp.zeros(D, 1); psi[0] = 1 / sp.sqrt(N); psi[2] = eps / sp.sqrt(N)
def ev(M):
    return sp.simplify((psi.T * M * psi)[0].subs(s2**2, 1 - c2**2))
rho = sp.simplify(sp.expand(ev(as_op(T1))))
T2 = sp.simplify(sp.expand(ev(as_op(T1**2))))
X = 2 * eps - sp.sqrt(2) * c2
chk("C2 exact <:T00:> = 2K eps (2eps - sqrt2 cos2th)/(1+eps^2)", sp.simplify(rho - 2 * Ks * eps * X / N) == 0)
chk("C2 exact <:T00^2:> = 12 K^2 eps^2/(1+eps^2)", sp.simplify(T2 - 12 * Ks**2 * eps**2 / N) == 0)
chk("C2 truncation D=8 is exact for this state (a+^4|0> needs n=4 < 8)", D > 4)

# ---------------------------------------------------------------- C3
Delta_in = sp.simplify(1 - rho**2 / T2)
chk("C3 1 - rho^2/<:T^2:> = 1 - X^2/(3(1+eps^2))", sp.simplify(Delta_in - (1 - X**2 / (3 * N))) == 0)
print("      exact Delta = |1 - (2eps - sqrt2 cos2th)^2 / (3(1+eps^2))|   (KF (3.2) carries the absolute value)")

# ---------------------------------------------------------------- z3 set-up
e, c, q = z3.Reals('e c q')
Xz = 2 * e - q * c
Nz = 1 + e * e
base = [q > 0, q * q == 2, c >= -1, c <= 1]
rho_neg = e * Xz < 0                         # sign of rho = sign of eps X  (2K/N > 0)
def prove(hyps, goal):
    s = z3.Solver(); s.add(*hyps); s.add(z3.Not(goal)); return s.check() == z3.unsat
def sat(hyps):
    s = z3.Solver(); s.add(*hyps); return s.check() == z3.sat
chk("vacuity guard: rho < 0 is satisfiable", sat(base + [rho_neg]))
chk("vacuity guard: rho > 0 is satisfiable", sat(base + [e * Xz > 0]))
# Delta_exact > 1  <=>  |1 - X^2/(3N)| > 1  <=>  X^2 > 6N  (since X^2/(3N) >= 0)
chk("C4 exact Delta <= 1 for every real eps, theta  (X^2 <= 6N)", prove(base, Xz * Xz <= 6 * Nz))
chk("C4 equality X^2 = 6N only at (eps, cos2th) = (sqrt2, -1) or (-sqrt2, 1), both rho > 0",
    prove(base + [Xz * Xz == 6 * Nz], z3.And(z3.Or(z3.And(e == q, c == -1), z3.And(e == -q, c == 1)), e * Xz > 0)))
chk("C4 identity: 6N - X^2 = 2(eps + sqrt2 cos2th)^2 + 6(1 - cos^2 2th)",
    sp.expand(6 * N - X**2 - (2 * (eps + sp.sqrt(2) * c2)**2 + 6 * (1 - c2**2))) == 0)
chk("C5 rho < 0 ==> exact Delta < 1  (claim 'Delta > 1' false at EVERY rho<0 point)",
    prove(base + [rho_neg], Xz * Xz < 6 * Nz) and prove(base + [rho_neg], Xz * Xz > 0))
chk("C5 z3: no point with rho < 0 and Delta > 1 exists", not sat(base + [rho_neg, Xz * Xz > 6 * Nz]))
chk("C6 rho < 0 ==> exact Delta > 1/3  (X^2 < 2N)", prove(base + [rho_neg], Xz * Xz < 2 * Nz))
Dex = lambda ee, cc: abs(1 - (2 * ee - math.sqrt(2) * cc)**2 / (3 * (1 + ee * ee)))
chk("C6 1/3 approached: eps -> 0+, theta = 0", abs(Dex(1e-7, 1.0) - 1 / 3) < 1e-6)
chk("C6 1 approached: X -> 0-, eps = 0.5, cos2th -> sqrt2*0.5 from above",
    abs(Dex(0.5, math.sqrt(2) * 0.5 + 1e-9) - 1) < 1e-6)

# ---------------------------------------------------------------- C7 four combinations
# rho_final = K eps X/N (printed (2.16) final), rho_exact = 2K eps X/N;
# T2_printed = 12K^2 eps^2/N^2 ((3.7)), T2_exact = 12K^2 eps^2/N.  ratio r = rho^2/T2:
combos = {
    "final x printed(3.7)": Xz * Xz / 12,
    "final x exact":        Xz * Xz / (12 * Nz),
    "exact x printed(3.7)": Xz * Xz / 3,
    "exact x exact":        Xz * Xz / (3 * Nz),
}
for name, r in combos.items():
    # Delta = |1 - r| > 1  <=>  r > 2  (r >= 0)
    chk("C7 [%s]: rho<0 ==> Delta < 1" % name, prove(base + [rho_neg], r < 2))

# ---------------------------------------------------------------- C8
D38 = (10 * e + q * c) / (12 * e)
chk("C8 (3.8) = 1 - X/(12 eps) identically", sp.simplify(
    (10 * eps + sp.sqrt(2) * c2) / (12 * eps) - (1 - X / (12 * eps))) == 0)
chk("C8 GIVEN (3.8): rho<0 ==> Delta_38 > 1 (no abs), all real eps != 0",
    prove(base + [e != 0, rho_neg], D38 > 1))
chk("C8 GIVEN (3.8): rho<0 ==> |Delta_38| > 1", prove(base + [e != 0, rho_neg], z3.Or(D38 > 1, D38 < -1)))
chk("C8 (3.8) itself can go negative (eps small, theta = pi/2): KF print no |.|",
    sat(base + [e > 0, D38 < 0]))

# ---------------------------------------------------------------- C9
r_unsq = (Ks**2 * eps * X / N**2) / (12 * Ks**2 * eps**2 / N**2)
chk("C9 (3.8) == 1 - [K^2 (eps X)/N^2] / (3.7)  (eps X left unsquared) -- consistent-with only",
    sp.simplify((1 - r_unsq) - (10 * eps + sp.sqrt(2) * c2) / (12 * eps)) == 0)

# ---------------------------------------------------------------- C10
chk("C10 eps > 0: rho < 0 <=> cos2th > sqrt2 eps",
    prove(base + [e > 0], rho_neg == (c > q * e)))
chk("C10 eps < 0: rho < 0 <=> cos2th < sqrt2 eps  (KF's printed condition reverses)",
    prove(base + [e < 0], rho_neg == (c < q * e)))
chk("C10 eps < 0 counter-point exists: cos2th > sqrt2 eps but rho > 0",
    sat(base + [e < 0, c > q * e, e * Xz > 0]))

# ---------------------------------------------------------------- C11
at = {eps: sp.Rational(1, 10), c2: 1}
dex = float(abs(1 - X**2 / (3 * N)).subs(at))
d38 = float(((10 * eps + sp.sqrt(2) * c2) / (12 * eps)).subs(at))
print("      witness eps=1/10, theta=0: exact Delta = %.6f ; KF (3.8) = %.6f ; rho/K = %.6f"
      % (dex, d38, float((rho / Ks).subs(at))))
chk("C11 witness exact Delta = 0.5134", round(dex, 4) == 0.5134)
chk("C11 witness KF (3.8) = 2.0118", round(d38, 4) == 2.0118)

# ---------------------------------------------------------------- C12
random.seed(67)
mx, nneg = 0.0, 0
for _ in range(200000):
    ee = random.uniform(-5, 5); cc = math.cos(random.uniform(0, 2 * math.pi))
    if ee * (2 * ee - math.sqrt(2) * cc) < 0:
        nneg += 1; mx = max(mx, Dex(ee, cc))
print("      sweep: %d rho<0 points of 200000, max exact Delta there = %.9f" % (nneg, mx))
chk("C12 sweep: max exact Delta on rho<0 < 1", nneg > 0 and mx < 1)

print("\nALL CHECKS PASS" if not FAIL else "\nFAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
