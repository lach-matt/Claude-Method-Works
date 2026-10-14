#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9304008 (Kuo & Ford 1993) Sec. V remark:
averaging fields over finite space or time intervals 'introduces an arbitrary
length or time scale into the problem' and, for an equation of the form of their
Eq.(4.3), 'there would be an inherent ambiguity in the resulting equation'.

This is a qualitative remark, not a theorem.  What IS checkable, in KF's own
single-mode flat-space model (their Sec. II/III.A, :T00: = K(2a+a - z a^2 - zbar a+^2),
z = e^{2i theta}), is whether the time-averaged analogue of KF's measure
    Delta = |<:A^2:> - <:A:>^2| / <:A^2:>
depends on the averaging time tau.  Heisenberg a(t) = a e^{-i w t}; a normalised
Gaussian window f(t) = exp(-t^2/tau^2)/(sqrt(pi) tau) gives
    int f(t) e^{-+2iwt} dt = s := exp(-w^2 tau^2),   A_s = K(2N - s z a^2 - s zbar a+^2).
Independent of fluctuation.py and noise.py (no import, no shared code).

C1  the Fourier factor s = exp(-w^2 tau^2) (sympy integral).
C2  :A_s^2:/K^2 = (4+2s^2) a+^2a^2 - 4 s z a+a^3 - 4 s zbar a+^3 a + s^2 z^2 a^4 + s^2 zbar^2 a+^4
    checked against truncated-Fock matrices (normal ordering by construction) -- two routes.
C3  coherent state: Delta_s = 0 for EVERY s  (no scale dependence -- KF (3.21) survives averaging).
C4  squeezed vacuum: Delta_s depends on s (d Delta/ds != 0); pointwise s=1 and s->0 limits.
C5  squeezed vacuum: the SIGN of the averaged energy density depends on tau:
    rho_s < 0 possible iff s > tanh r.
C6  vacuum + 2 state (KF 2.15): Delta_s depends on s.
C7  scale-free control (FFR 1004.0179 eq.22, READ in this docket): omega_0*beta = c/24 = alpha,
    tau-independent -- for a massless field in its vacuum the dimensionless shape is tau-free.
"""
import sys
import sympy as sp

fails = []
def chk(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        fails.append(name)

t, tau, w = sp.symbols('t tau omega', positive=True)
# C1
f = sp.exp(-t**2/tau**2)/(sp.sqrt(sp.pi)*tau)
sfac = sp.simplify(sp.integrate(f*sp.exp(-2*sp.I*w*t), (t, -sp.oo, sp.oo)))
chk("C1 Gaussian-window factor s = exp(-w^2 tau^2): got %s" % sfac,
    sp.simplify(sfac - sp.exp(-w**2*tau**2)) == 0)

# Fock matrices, exact
Nmax = 40
def amat(n):
    return sp.Matrix(n, n, lambda i, j: sp.sqrt(j) if i == j-1 else 0)
s, th = sp.symbols('s theta', real=True)
z = sp.exp(2*sp.I*th)
zb = sp.exp(-2*sp.I*th)

def delta_from_moments(m):
    """m: dict of <a+^p a^q> -> Delta_s, rho_s (K=1)"""
    A1 = 2*m[(1,1)] - s*z*m[(0,2)] - s*zb*m[(2,0)]
    A2 = (4+2*s**2)*m[(2,2)] - 4*s*z*m[(1,3)] - 4*s*zb*m[(3,1)] + s**2*z**2*m[(0,4)] + s**2*zb**2*m[(4,0)]
    return A1, A2

# C2: normal-ordered square via matrices -- build :A^2: from the normal-ordered monomials and
# compare with (A^2 minus the reordering terms) computed from the plain operator square.
n = 12
a = amat(n); ad = a.H
N = ad*a
sv = sp.Rational(3, 7); zz = sp.exp(2*sp.I*sp.Rational(1, 5)); zzb = sp.conjugate(zz)
A = 2*N - sv*zz*a**2 - sv*zzb*ad**2
NO = (4+2*sv**2)*ad**2*a**2 - 4*sv*zz*ad*a**3 - 4*sv*zzb*ad**3*a + sv**2*zz**2*a**4 + sv**2*zzb**2*ad**4
# A^2 = :A^2: + (contraction terms).  Contractions [a, a+] = 1 give, by Wick for operators:
# A^2 - :A^2: = 4 N  - 4 s z a^2 * 1*? ... compute directly and check it is QUADRATIC (order <= 2)
D = sp.simplify(A*A - NO)
# expected contraction remainder: from (2a+a)(2a+a): 4 a+a ; (2a+a)(-s z a^2): 0 ; (-s z a^2)(2a+a): -4 s z a^2 ;
# (2a+a)(-s zb a+^2): -4 s zb a+^2 ; (-s zb a+^2)(2a+a): 0 ; (s z a^2)(s zb a+^2): s^2(4 a+a + 2)
exp_rem = 4*N - 4*sv*zz*a**2 - 4*sv*zzb*ad**2 + sv**2*(4*N + 2*sp.eye(n))
diff = (D - exp_rem)[:n-4, :n-4]          # truncation corrupts the last rows/cols
chk("C2 :A_s^2: normal-ordered form agrees with the operator square minus its contractions (exact, Fock n=12)",
    all(sp.nsimplify(sp.simplify(x)) == 0 for x in diff))

# C3 coherent state: <a+^p a^q> = conj(al)^p al^q
al = sp.symbols('alpha')
alc = sp.conjugate(al)
mc = {(p, q): alc**p*al**q for p in range(5) for q in range(5)}
A1, A2 = delta_from_moments(mc)
chk("C3 coherent: <:A_s^2:> - <:A_s:>^2 = 0 identically in s, theta, alpha",
    sp.simplify(sp.expand(A2 - A1**2)) == 0)

# C4 squeezed vacuum (zero-mean Gaussian, Wick): n=<a+a>=sh^2, m=<aa>=-e^{i phi} sh ch
r, ph = sp.symbols('r phi', positive=True)
sh, ch = sp.sinh(r), sp.cosh(r)
nn = sh**2; mm = -sp.exp(sp.I*ph)*sh*ch; mmc = sp.conjugate(mm)
ms = {(1,1): nn, (0,2): mm, (2,0): mmc,
      (2,2): 2*nn**2 + mm*mmc, (1,3): 3*nn*mm, (3,1): 3*nn*mmc,
      (0,4): 3*mm**2, (4,0): 3*mmc**2}
A1, A2 = delta_from_moments(ms)
Dsq = sp.simplify((A2 - A1**2)/A2)
# independent route: truncated Fock squeezed vacuum, numeric
import mpmath as mp
mp.mp.dps = 30
def sqz_vec(rv, phv, nmax=160):
    v = [mp.mpf(0)]*nmax
    for k in range(0, nmax//2):
        v[2*k] = (mp.sqrt(mp.factorial(2*k))/(2**k*mp.factorial(k))) * (-mp.e**(1j*phv)*mp.tanh(rv))**k / mp.sqrt(mp.cosh(rv))
    return v
def fock_delta(vec, sv_, thv):
    nmax = len(vec)
    def mom(p, q):   # <a+^p a^q>
        tot = 0
        for k in range(q, nmax):
            j = k - q + p
            if j >= nmax: continue
            c = mp.sqrt(mp.factorial(k)/mp.factorial(k-q))*mp.sqrt(mp.factorial(j)/mp.factorial(k-q))
            tot += mp.conj(vec[j])*vec[k]*c
        return tot
    zv = mp.e**(2j*thv); zbv = mp.conj(zv)
    A1v = 2*mom(1,1) - sv_*zv*mom(0,2) - sv_*zbv*mom(2,0)
    A2v = (4+2*sv_**2)*mom(2,2) - 4*sv_*zv*mom(1,3) - 4*sv_*zbv*mom(3,1) + sv_**2*zv**2*mom(0,4) + sv_**2*zbv**2*mom(4,0)
    return mp.re((A2v - A1v**2)/A2v), mp.re(A1v)
pts = [(0.3, 0.7, 0.2, 1.0), (0.3, 0.7, 0.2, 0.5), (0.8, 1.1, 0.4, 0.1), (0.5, 0.0, 0.0, 0.9)]
agree = True
for rv, phv, thv, svv in pts:
    fd, _ = fock_delta(sqz_vec(rv, phv), svv, thv)
    sd = complex(Dsq.subs({r: rv, ph: phv, th: thv, s: svv}).evalf(25)).real
    agree &= abs(float(fd) - sd) < 1e-12
    print("      r=%.2f phi=%.2f theta=%.2f s=%.2f  Delta_s Wick=%.12f  Fock=%.12f" % (rv, phv, thv, svv, sd, float(fd)))
chk("C4a squeezed vacuum Delta_s: Wick closed form == truncated-Fock numerics (two routes)", agree)
dD = sp.diff(Dsq, s)
val = complex(dD.subs({r: 0.5, ph: 0.3, th: 0.1, s: 0.5}).evalf()).real
chk("C4b squeezed vacuum: d Delta_s / ds != 0 (Delta depends on the averaging time): %.6f" % val, abs(val) > 1e-6)
D1 = sp.simplify(Dsq.subs(s, 1)); D0 = sp.simplify(Dsq.subs(s, 0))
print("      s=1 (pointwise): Delta =", D1)
print("      s=0 (tau->oo):   Delta =", sp.simplify(D0.rewrite(sp.exp)))
# s=0: A = 2N, :A^2: = 4 a+^2 a^2 (normal-ordered, NOT 4N^2), so
# Delta_0 = (<a+^2a^2> - n^2)/<a+^2a^2> = (n^2+|m|^2)/(2n^2+|m|^2) = (1+2 sinh^2 r)/(1+3 sinh^2 r).
# (A first draft of this check used Var(N)/<N^2>, which is the un-normal-ordered ratio; it failed and
#  was corrected -- the normal-ordered square is KF's (3.2) definition.)
chk("C4c s=0 limit = (1+2 sinh^2 r)/(1+3 sinh^2 r)  [normal-ordered, KF (3.2)]",
    sp.simplify((D0 - (1+2*sh**2)/(1+3*sh**2)).rewrite(sp.exp)) == 0)
samples = [complex(Dsq.subs({r: 0.5, ph: 0.3, th: 0.1, s: sv_}).evalf()).real for sv_ in (1.0, 0.75, 0.5, 0.25, 0.0)]
print("      r=0.5 phi=0.3 theta=0.1: Delta_s at s=1,.75,.5,.25,0 ->", ["%.6f" % x for x in samples])
chk("C4d the same state gives different Delta at different tau", max(samples) - min(samples) > 1e-3)

# C5 sign of the averaged energy density
rho_s = sp.simplify(sp.expand(A1))
# rho_s = 2 sh^2 + 2 s sh ch cos(phi + 2 theta)  (with the sign of m above)
chk("C5a rho_s = 2 sinh^2 r + 2 s sinh r cosh r cos(phi + 2 theta)",
    sp.simplify(sp.expand_complex(rho_s - (2*sh**2 + 2*s*sh*ch*sp.cos(ph+2*th)))) == 0)
# min over phase: 2 sh (sh - s ch) < 0  iff s > tanh r
rv = 0.5
for svv in (0.9, 0.3):
    mn = 2*mp.sinh(rv)*(mp.sinh(rv) - svv*mp.cosh(rv))
    print("      r=0.5 tanh r=%.6f  s=%.2f  min_phase rho_s = %.6f" % (mp.tanh(rv), svv, mn))
chk("C5b at r=0.5: rho_s can be negative at s=0.9 (short tau) and cannot at s=0.3 (long tau)",
    2*mp.sinh(rv)*(mp.sinh(rv) - 0.9*mp.cosh(rv)) < 0 and 2*mp.sinh(rv)*(mp.sinh(rv) - 0.3*mp.cosh(rv)) > 0)

# C6 vacuum+2 state (KF 2.15), exact finite Fock
eps = sp.symbols('epsilon', positive=True)
n6 = 8
a6 = amat(n6); ad6 = a6.H
psi = sp.zeros(n6, 1); psi[0] = 1/sp.sqrt(1+eps**2); psi[2] = eps/sp.sqrt(1+eps**2)
def ev(M): return sp.simplify((psi.H*M*psi)[0])
m6 = {(p, q): ev(ad6**p*a6**q) for (p, q) in [(1,1),(0,2),(2,0),(2,2),(1,3),(3,1),(0,4),(4,0)]}
A1, A2 = delta_from_moments(m6)
D6 = sp.simplify((A2 - A1**2)/A2)
vals6 = [float(sp.re(D6.subs({eps: sp.Rational(1,10), th: 0, s: sv_}).evalf())) for sv_ in (1, sp.Rational(1,2), 0)]
print("      vac+2, eps=1/10, theta=0: Delta_s at s=1, 1/2, 0 ->", ["%.6f" % x for x in vals6])
chk("C6a vac+2: s=1 reproduces the pointwise exact Delta 0.5134 recorded at fluctuation.py:62 (4 d.p.)",
    abs(vals6[0] - 0.5134) < 5e-5)
chk("C6b vac+2: Delta_s moves with s", max(vals6) - min(vals6) > 1e-3)

# C7 scale-free control, FFR 1004.0179 eq.(22)
c = sp.symbols('c', positive=True)
omega0 = c/(24*sp.pi*tau**2); beta = sp.pi*tau**2
chk("C7 FFR eq.(22): omega_0*beta = c/24 (= alpha), tau-independent", sp.simplify(omega0*beta - c/24) == 0)

print()
if fails:
    print("FAILED: %d" % len(fails)); sys.exit(1)
print("ALL CHECKS PASS")
