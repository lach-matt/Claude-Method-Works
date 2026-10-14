#!/usr/bin/env python3
"""DOCKET 67 re-derivation: zeta-pi-enclosures (noise.py:123-128, 730-747, 1054-1066).

Checks, each independently of the tree's code:
 E1  zeta(6) = pi^6/945 from Euler's formula (arXiv:2307.08063 eq (3)/(17)) with B_6
     computed exactly from the Bernoulli recurrence (same paper p.4); cross-checked
     against mpmath zeta(6) at 60 digits and sympy.zeta(6).
 E2  333/106 < pi < 355/113 PROVED with exact rationals: Machin's formula
     pi = 16 atan(1/5) - 4 atan(1/239), alternating-series truncation gives a rigorous
     rational enclosure [PL, PU]; then 333/106 < PL and PU < 355/113.  The continued
     fraction of pi is computed from the enclosure (partial quotients on which PL and
     PU agree), and 333/106, 355/113 are shown to be its 3rd and 4th convergents.
 E3  0 <= zeta(7) - sum_{n<=30} n^-7 <= 1/(6*30^6): integral comparison, exact in sympy;
     and the true tail (mpmath) sits between 1/(6*31^6) and 1/(6*30^6).
 E4  The Hoelder bound B(tau=beta) = 108000 (zeta6-zeta7)/(sqrt(2pi) pi^7) < 1/2:
     (a) 108000 = (2/3)*180*900 arithmetic; (b) exact-rational BOX proof (no z3) using
     monotonicity of each side; (c) independent z3 re-run of the tree's query and of
     its vacuity guard; (d) the tree's own functions imported read-only and run;
     (e) margins: value at tau=beta, crossing tau*, weakest pi / zeta7 bounds that
     still prove the claim.
Exit 0 iff every check passes.
"""
import sys, os
sys.dont_write_bytecode = True
from fractions import Fraction as Fr
from math import isqrt
import sympy as sp
import mpmath as mp
mp.mp.dps = 60
FAIL = []
def chk(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + str(info)) if info != "" else ""))
    if not ok: FAIL.append(name)

# ---------------- E1 zeta(6) ----------------
def bernoulli_numbers(nmax):
    # B_0..B_nmax from sum_{k=0}^{n} C(n+1,k) B_k = 0 (n>=1), B_0 = 1 (B_1 = -1/2 convention)
    B = [Fr(1)]
    for n in range(1, nmax + 1):
        s = sum(sp.binomial(n + 1, k) * B[k] for k in range(n))
        B.append(Fr(-int(s.numerator if hasattr(s,'numerator') else s), 1) / (n + 1) if False else -Fr(s) / (n + 1))
    return B
B = bernoulli_numbers(6)
chk("E1 B_2=1/6, B_4=-1/30, B_6=1/42 (recurrence, exact)", (B[2], B[4], B[6]) == (Fr(1,6), Fr(-1,30), Fr(1,42)), (B[2],B[4],B[6]))
k = 3
# zeta(2k) = (-1)^{k-1} 2^{2k-1} pi^{2k} B_{2k}/(2k)!   (2307.08063 eq (3))
c6 = Fr((-1)**(k-1) * 2**(2*k-1), 1) * B[2*k] / sp.factorial(2*k)
c6 = Fr(int(c6.numerator), int(c6.denominator)) if not isinstance(c6, Fr) else c6
chk("E1 Euler's formula at k=3 gives zeta(6)/pi^6 = 1/945 exactly", c6 == Fr(1,945), c6)
chk("E1 cross-check: mpmath zeta(6) - pi^6/945 = 0 to 55 digits", abs(mp.zeta(6) - mp.pi**6/945) < mp.mpf(10)**-55, mp.nstr(mp.zeta(6),30))
chk("E1 cross-check: sympy.zeta(6) == pi^6/945 symbolically", sp.simplify(sp.zeta(6) - sp.pi**6/945) == 0)
chk("E1 the tree's route: nsimplify(zeta(6)/pi^6) = 1/945", sp.nsimplify(sp.zeta(6)/sp.pi**6) == sp.Rational(1,945))
# also k=1,2 as controls
for kk, want in ((1, Fr(1,6)), (2, Fr(1,90))):
    Bk = bernoulli_numbers(2*kk)[2*kk]
    v = Fr((-1)**(kk-1) * 2**(2*kk-1), 1) * Bk / int(sp.factorial(2*kk))
    chk("E1 CONTROL k=%d: zeta(%d)/pi^%d = %s" % (kk, 2*kk, 2*kk, want), v == want, v)

# ---------------- E2 pi enclosure ----------------
def atan_inv_bounds(x, terms):
    # atan(1/x) = sum (-1)^j / ((2j+1) x^{2j+1}); alternating with decreasing terms:
    # partial sums S_{2m-1} < atan < S_{2m}
    s = Fr(0); partial = []
    for j in range(terms):
        s += Fr((-1)**j, (2*j+1) * x**(2*j+1)); partial.append(s)
    lo = max(p for i, p in enumerate(partial) if i % 2 == 1)
    hi = min(p for i, p in enumerate(partial) if i % 2 == 0)
    return lo, hi
a5 = atan_inv_bounds(5, 40); a239 = atan_inv_bounds(239, 12)
PL = 16 * a5[0] - 4 * a239[1]; PU = 16 * a5[1] - 4 * a239[0]
chk("E2 Machin enclosure is consistent with mpmath pi", PL < Fr(mp.nstr(mp.pi, 58)) < PU, float(PU - PL))
chk("E2 PROVED 333/106 < pi (333/106 < PL)", Fr(333,106) < PL, float(PL - Fr(333,106)))
chk("E2 PROVED pi < 355/113 (PU < 355/113)", PU < Fr(355,113), float(Fr(355,113) - PU))
def cf_from_enclosure(lo, hi, n):
    q = []
    for _ in range(n):
        a, b = lo.numerator // lo.denominator, hi.numerator // hi.denominator
        if a != b: break
        q.append(a); lo, hi = lo - a, hi - a
        if lo == 0 or hi == 0: break
        lo, hi = 1 / hi, 1 / lo
    return q
cf = cf_from_enclosure(PL, PU, 12)
chk("E2 continued fraction of pi begins [3;7,15,1,292,1,1,1,2,1,3,1]", cf[:12] == [3,7,15,1,292,1,1,1,2,1,3,1], cf)
conv = []; h0, h1, k0, k1 = 1, cf[0], 0, 1
conv.append(Fr(h1, k1))
for a in cf[1:6]:
    h0, h1 = h1, a*h1 + h0; k0, k1 = k1, a*k1 + k0; conv.append(Fr(h1, k1))
chk("E2 convergents 3, 22/7, 333/106, 355/113, 103993/33102", conv[:5] == [Fr(3), Fr(22,7), Fr(333,106), Fr(355,113), Fr(103993,33102)], conv[:5])
chk("E2 numerators match 2603.09719 eq (12) (A002485: 3, 22, 333, 355, 103993)", [c.numerator for c in conv[:5]] == [3,22,333,355,103993])
chk("E2 333/106 is an even-index (lower) convergent, 355/113 odd-index (upper)", conv[2] < PL and conv[3] > PU)
print("   pi - 333/106 = %s ; 355/113 - pi = %s" % (mp.nstr(mp.pi - mp.mpf(333)/106, 6), mp.nstr(mp.mpf(355)/113 - mp.pi, 6)))

# ---------------- E3 zeta(7) tail ----------------
x, n = sp.symbols('x n', positive=True)
N = 30
chk("E3 INT_30^oo x^-7 dx = 1/(6*30^6) (sympy, exact)", sp.integrate(x**-7, (x, N, sp.oo)) == sp.Rational(1, 6*N**6))
# n^-7 <= INT_{n-1}^{n} x^-7 dx for n >= 2 since x^-7 decreasing: check symbolically the difference
d = sp.integrate(x**-7, (x, n-1, n)) - n**-7
chk("E3 n^-7 <= INT_{n-1}^n x^-7 for n = 2..200 (exact)", all(d.subs(n, i) > 0 for i in range(2, 201)))
lo7 = sum(Fr(1, i**7) for i in range(1, 31)); hi7 = lo7 + Fr(1, 6*30**6)
z7 = mp.zeta(7)
tail = z7 - mp.mpf(lo7.numerator)/lo7.denominator
chk("E3 lo7 <= zeta(7) <= hi7 (mpmath, 60 digits)", mp.mpf(lo7.numerator)/lo7.denominator <= z7 <= mp.mpf(hi7.numerator)/hi7.denominator, mp.nstr(z7, 25))
chk("E3 1/(6*31^6) < true tail < 1/(6*30^6)", mp.mpf(1)/(6*31**6) < tail < mp.mpf(1)/(6*30**6), mp.nstr(tail, 8))

# ---------------- E4 the Hoelder-bound claim ----------------
chk("E4a 108000 = (2/3)*180*900 [rho^2 = pi^4/900, ||g^2||_1 = 180(z6-z7)/pi^3]", Fr(2,3)*180*900 == 108000)
coef, z6 = Fr(108000), Fr(1,945)
def Bval(t):
    return 108000 * (mp.zeta(6) - mp.zeta(7)) / (t * mp.sqrt(2*mp.pi) * mp.pi**7)
b1 = Bval(1); tstar = mp.findroot(lambda t: Bval(t) - mp.mpf(1)/2, 0.25)
print("   B(tau=beta) = %s ; B(beta/10) = %s ; crossing tau*/beta = %s" % (mp.nstr(b1, 12), mp.nstr(Bval(mp.mpf(1)/10), 8), mp.nstr(tstar, 10)))
chk("E4e B(tau=beta) < 1/2 numerically", b1 < 0.5, mp.nstr(b1, 10))
chk("E4e B(tau=beta/10) > 1/2 numerically (so the beta/10 'guard' query is FALSE, not merely unproved)", Bval(mp.mpf(1)/10) > 0.5)
def box_proof(T, plo, phi, z7lo, coef=coef, z6=z6):
    # goal: 2 coef (z6 p^6 - z7) < T r p^7, r = sqrt(2p), on plo<p<phi, z7>=z7lo.
    # LHS increasing in p, decreasing in z7; RHS increasing in p. Sufficient:
    # 2 coef (z6 phi^6 - z7lo) <= T s plo^7 with s <= sqrt(2 plo) rational.
    D = 10**12
    s = Fr(isqrt((2*plo*D*D).numerator // (2*plo*D*D).denominator), D)  # floor(sqrt(2plo)*D)/D
    assert s*s <= 2*plo
    return 2*coef*(z6*phi**6 - z7lo) < T*s*plo**7
chk("E4b EXACT BOX PROOF (no z3): claim holds on the tree's box at tau = beta", box_proof(Fr(1), Fr(333,106), Fr(355,113), lo7))
chk("E4b CONTROL: box proof fails at tau = beta/10", not box_proof(Fr(1,10), Fr(333,106), Fr(355,113), lo7))
chk("E4b CONTROL: box proof fails with coefficient x10", not box_proof(Fr(1), Fr(333,106), Fr(355,113), lo7, coef=coef*10))
# robustness: weaker inputs
chk("E4e ROBUST: pi in (3, 22/7) with z7 >= 1 (N=1, no tail) still proves at tau = beta", box_proof(Fr(1), Fr(3), Fr(22,7), Fr(1)))
def weakest_phi(plo, z7lo):
    a, b = Fr(314159,100000), Fr(4)
    for _ in range(60):
        m = (a + b) / 2
        if box_proof(Fr(1), plo, m, z7lo): a = m
        else: b = m
    return a
w1 = weakest_phi(Fr(333,106), lo7); w2 = weakest_phi(Fr(3), Fr(1))
print("   weakest upper bound on pi the crude box proof tolerates: %.6f (lower 333/106, lo7); %.6f (lower 3, z7>=1)" % (float(w1), float(w2)))
chk("E4e MEASURED margin: the box proof tolerates an upper bound on pi >= 22/7 in both settings", w1 > Fr(22,7) and w2 > Fr(22,7), (float(w1), float(w2)))
chk("E4e the z7 UPPER bound (the 1/(6*30^6) tail) is not used by the proof -- LHS decreases in z7", True)
try:
    import z3
    def tree_query(T, coef=coef, lo=Fr(333,106), hi=Fr(355,113), l7=lo7, h7=hi7, use_upper=True):
        p, zz, r = z3.Reals('p z7 r')
        H = [p > z3.RealVal(str(lo)), p < z3.RealVal(str(hi)), zz >= z3.RealVal(str(l7)), r > 0, r*r == 2*p]
        if use_upper: H.append(zz <= z3.RealVal(str(h7)))
        goal = 2*z3.RealVal(str(coef))*(z3.RealVal(str(z6))*p**6 - zz) < z3.RealVal(str(T))*r*p**7
        s = z3.Solver(); s.add(*H); s.add(z3.Not(goal)); proved = s.check() == z3.unsat
        s2 = z3.Solver(); s2.add(*H); sat = s2.check() == z3.sat
        return proved, sat
    chk("E4c z3 (independent encoding) proves the claim at tau = beta; hypotheses sat", tree_query(Fr(1)) == (True, True))
    chk("E4c z3: NOT provable at tau = beta/10", tree_query(Fr(1,10))[0] is False)
    chk("E4c z3: NOT provable with coefficient x10", tree_query(Fr(1), coef=coef*10)[0] is False)
    chk("E4c z3: still proves WITHOUT the z7 upper bound (tail hypothesis idle for the proof)", tree_query(Fr(1), use_upper=False)[0] is True)
    # rational witness for the vacuity guard: r rational, p = r^2/2
    rw = Fr(25066, 10000); pw = rw*rw/2
    chk("E4c exact witness of satisfiability: r=2.5066, p=r^2/2 in (333/106,355/113), z7=lo7", Fr(333,106) < pw < Fr(355,113), float(pw))
except ImportError:
    chk("E4c z3 importable", False, "pip install z3-solver")
# (d) the tree's own functions, imported read-only
WD = "/home/user/Claude-Method-Works/research/warp-drive"
try:
    sys.path.insert(0, WD)
    import noise
    import z3
    cf_, z6_ = noise.hoelder_bound_constants(sp)
    chk("E4d tree's hoelder_bound_constants -> (108000, 1/945)", (cf_, z6_) == (108000, sp.Rational(1,945)), (cf_, z6_))
    r1 = noise.hoelder_bound_proof(z3, 1, cf_, z6_); r01 = noise.hoelder_bound_proof(z3, sp.Rational(1,10), cf_, z6_)
    chk("E4d tree's hoelder_bound_proof(tau=beta) = (True, True)", r1 == (True, True), r1)
    chk("E4d tree's hoelder_bound_proof(tau=beta/10)[0] = False", r01[0] is False, r01)
except Exception as e:
    chk("E4d import of the tree's noise.py (read-only)", False, repr(e))
print("\n%d FAIL" % len(FAIL)); sys.exit(1 if FAIL else 0)
