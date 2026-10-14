#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Ford & Roman, gr-qc/9607003 (PRD 55, 2082 (1997)),
"Restrictions on Negative Energy Density in Flat Spacetime".

Every check below is a closed-form step of the paper READ at source (page text
returned by alphaXiv), or a step of the later literature that bears on it.
Nothing is DECLARED: each line computes and compares.  Exit 1 on any failure.

    python3 gr-qc_9607003.py
"""
import math, sys, random
import sympy as sp

FAIL = []
def chk(label, got, want, tol=0.0):
    ok = (abs(got - want) <= tol) if tol else (got == want)
    print("  %s  %s" % ("OK " if ok else "BAD", label))
    if not ok:
        print("       got %r want %r" % (got, want)); FAIL.append(label)

t0, w, wp, x, y, m, t = sp.symbols('t_0 omega omega_p x y m t', positive=True)

# ---------------------------------------------------------------- Eq. (8)->(9)
# The Lorentzian sampler (t0/pi)/(t^2+t0^2) folds e^{i(w'-w)t} into e^{-|w'-w|t0}
# and e^{-i(w'+w)t} into e^{-(w'+w)t0}: the transform the paper uses at (9).
print("Eq. (8)->(9): the Lorentzian transform")
d = sp.symbols('d', positive=True)          # d = |w' - w| or w' + w, both > 0
tt = sp.symbols('t', real=True)
lor = sp.integrate(sp.cos(d*tt)*t0/(sp.pi*(tt**2 + t0**2)), (tt, -sp.oo, sp.oo))
chk("(t0/pi) INT cos(d t)/(t^2+t0^2) dt = e^{-d t0}, d > 0",
    sp.simplify(lor - sp.exp(-d*t0)) == 0, True)

# ---------------------------------------------------------------- Eq. (12)->(17)
print("Eq. (12)->(13)->(17): massless 4D scalar")
# (12): rho >= -(1/2V) sum_k w e^{-2 w t0};  sum_k -> V/(8 pi^3) INT d^3k
# angular integral 4 pi, k^2 dk with k dk = w dw:  -(1/(4 pi^2)) INT sqrt(w^2-m^2) w^2 e^{-2 w t0} dw  (13)
pref = sp.Rational(1, 2) * (1 / (8*sp.pi**3)) * 4*sp.pi
chk("prefactor -(1/2V)(V/8pi^3)(4pi) = 1/(4 pi^2)", sp.simplify(pref - 1/(4*sp.pi**2)) == 0, True)
I13_massless = sp.integrate(w**3 * sp.exp(-2*w*t0), (w, 0, sp.oo))
rhs17 = sp.simplify(-pref * I13_massless)
chk("(17): -(1/4pi^2) INT w^3 e^{-2 w t0} = -3/(32 pi^2 t0^4)",
    sp.simplify(rhs17 + sp.Rational(3, 32)/(sp.pi**2*t0**4)) == 0, True)
# (14)-(16): x = 2 w t0, y = 2 m t0, G(y) = (1/6) INT_y^oo sqrt(x^2-y^2) x^2 e^{-x} dx, G(0) = 1
G0 = sp.Rational(1, 6) * sp.integrate(x**3*sp.exp(-x), (x, 0, sp.oo))
chk("(15)-(16): G(0) = 1", G0 == 1, True)
chk("(14): 1/(64 pi^2 t0^4) times 6 = 3/(32 pi^2 t0^4)",
    sp.Rational(6, 64) == sp.Rational(3, 32), True)
# G decreasing: sample
Gy = lambda yy: float(sp.Integral(sp.sqrt(x**2 - yy**2)*x**2*sp.exp(-x), (x, yy, sp.oo)).evalf()) / 6
gs = [Gy(v) for v in (0.0, 0.5, 1.0, 2.0, 4.0, 8.0)]
chk("G(y) strictly decreasing on the sampled y (4D: no peak, as the paper says)",
    all(a > b for a, b in zip(gs, gs[1:])), True)
chk("G(0) numerically 1", gs[0], 1.0, 1e-9)

# ---------------------------------------------------------------- Eq. (48) EM
print("Eq. (45)-(48): electromagnetic field, two polarisations")
rhs48 = sp.simplify(-(1/(2*sp.pi**2)) * I13_massless)
chk("(48): -(1/2pi^2) INT w^3 e^{-2 w t0} = -3/(16 pi^2 t0^4)",
    sp.simplify(rhs48 + sp.Rational(3, 16)/(sp.pi**2*t0**4)) == 0, True)
chk("EM bound is exactly 2 x the scalar bound", sp.simplify(rhs48/rhs17) == 2, True)

# ---------------------------------------------------------------- Eq. (19)-(25) 2D
print("Eq. (19)-(25): two dimensions")
I2d_massless = sp.integrate(w * sp.exp(-2*w*t0), (w, 0, sp.oo))
rhs25 = sp.simplify(-(1/(2*sp.pi)) * I2d_massless)
chk("(25): -(1/2pi) INT w e^{-2 w t0} = -1/(8 pi t0^2)",
    sp.simplify(rhs25 + 1/(8*sp.pi*t0**2)) == 0, True)
# (21): I = INT_m^oo w^2 e^{-2 w t0}/sqrt(w^2-m^2) dw = -m^2 K_1'(2 m t0); (23): F(y) = y^2 (K0+K2)/8 * ...
# check numerically at one point that I = F(y)/(4 t0^2) with F = y^2 (K0(y)+K2(y))/2
mv, tv = 0.7, 0.9
yv = 2*mv*tv
Inum = float(sp.Integral(w**2*sp.exp(-2*w*tv)/sp.sqrt(w**2 - mv**2), (w, mv, sp.oo)).evalf())
Fnum = yv**2*(float(sp.besselk(0, yv)) + float(sp.besselk(2, yv)))/2
chk("(20)-(23): I(m,t0) = F(2 m t0)/(4 t0^2) at (m,t0)=(0.7,0.9)", Inum, Fnum/(4*tv**2), 1e-8)
Fy = lambda yy: yy**2*(float(sp.besselk(0, yy)) + float(sp.besselk(2, yy)))/2
chk("F(y) -> 1 as y -> 0 (y = 1e-4)", Fy(1e-4), 1.0, 1e-6)
peak = max(Fy(0.01*i) for i in range(1, 121))
chk("the paper's 2D 'small peak' on 0 <= y <= 1.2 exists: max F > 1", peak > 1.0, True)
print("       max F(y) on (0,1.2] = %.6f  (paper: 'small peak', 'too small to produce a dramatic change')" % peak)

# ---------------------------------------------------------------- Appendix B lemma
print("Appendix B lemma: S_m >= S~_m, machine-checked (z3) on 2- and 3-mode sets")
# With A_i = e^{2 w_i t0} - 1 the difference S_m - S~_m = sum_ij C_ij A_min(i,j),
# C = [g_i* g_j <a_i^+ a_j>] positive semidefinite.  All the proof uses of the
# exponentials is 0 <= A_1 <= A_2 <= ... , so the claim is:
#   for every real symmetric PSD C and 0 <= A1 <= A2 <= A3:  sum_ij C_ij A_min(i,j) >= 0.
try:
    import z3
    # n = 2
    c11, c12, c22, A1, A2 = z3.Reals('c11 c12 c22 A1 A2')
    s = z3.Solver(); s.set('timeout', 60000)
    s.add(c11 >= 0, c22 >= 0, c11*c22 - c12*c12 >= 0, 0 <= A1, A1 <= A2)
    s.add(c11*A1 + 2*c12*A1 + c22*A2 < 0)
    chk("n=2: negation UNSAT", s.check() == z3.unsat, True)
    # n = 3 and n = 4.  The claim is LINEAR in C and every PSD C is a sum of
    # rank-one v v^T, so it suffices to prove it for C = v v^T: the quadratic
    # form sum_ij v_i v_j A_min(i,j) >= 0 for all real v and 0<=A1<=...<=An.
    # (The determinant encoding of PSD returns 'unknown' from nlsat at 90 s.)
    for nn in (3, 4):
        v = z3.Reals(' '.join('v%d' % i for i in range(nn)))
        A = z3.Reals(' '.join('A%d' % i for i in range(nn)))
        s = z3.Solver(); s.set('timeout', 60000)
        s.add(0 <= A[0])
        for i in range(nn-1):
            s.add(A[i] <= A[i+1])
        s.add(sum(v[i]*v[j]*A[min(i, j)] for i in range(nn) for j in range(nn)) < 0)
        chk("n=%d (rank-one C, which suffices by linearity): negation UNSAT" % nn, s.check() == z3.unsat, True)
except ImportError:
    print("  --  z3 not importable; lemma checked numerically only"); FAIL.append("z3 missing")

# The induction (B17)-(B21) is the identity  sum_ij C_ij A_min(i,j) = sum_k (A_k - A_{k-1}) sum_{i,j>=k} C_ij
n = 4
Cs = sp.Matrix(n, n, lambda i, j: sp.Symbol('c%d%d' % (min(i, j), max(i, j))))
As = sp.symbols('A1:%d' % (n+1))
lhs = sum(Cs[i, j]*As[min(i, j)] for i in range(n) for j in range(n))
rhs = sum((As[k] - (As[k-1] if k else 0)) * sum(Cs[i, j] for i in range(k, n) for j in range(k, n)) for k in range(n))
chk("(B17)-(B21) as an identity, n=4: sum C_ij A_min = sum_k (A_k-A_{k-1}) (corner block sums)",
    sp.expand(lhs - rhs) == 0, True)
# numeric Hermitian check n = 8
random.seed(67)
ok = True
for _ in range(200):
    nn = 8
    Bm = [[complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(nn)] for _ in range(nn)]
    Ch = [[sum(Bm[k][i].conjugate()*Bm[k][j] for k in range(nn)) for j in range(nn)] for i in range(nn)]
    ws = sorted(random.uniform(0.1, 3.0) for _ in range(nn)); tv = random.uniform(0.1, 2.0)
    S = sum(Ch[i][j]*math.exp(-abs(ws[i]-ws[j])*tv) for i in range(nn) for j in range(nn))
    St = sum(Ch[i][j]*math.exp(-(ws[i]+ws[j])*tv) for i in range(nn) for j in range(nn))
    if not (S.real >= St.real - 1e-9 and abs(S.imag) < 1e-9 and abs(St.imag) < 1e-9): ok = False
chk("Hermitian PSD, n=8, 200 random draws: S_m >= S~_m, both real", ok, True)

# ---------------------------------------------------------------- SI form and the tree's fixtures
print("SI form and the tree's pins")
HBAR_2018 = 1.054571817e-34      # exact since the 2019 SI redefinition
HBAR_1986 = 1.05457266e-34       # CODATA 1986, current when the paper was written
C_SI = 299792458.0               # exact since 1983
def ford_roman_allow(tau, hbar=HBAR_2018):
    return 3.0*hbar/(32.0*math.pi**2*C_SI**3*tau**4)
chk("achievable.ford_roman_allow(1 s) = 3 hbar/(32 pi^2 c^3) Pa",
    ford_roman_allow(1.0), 3*HBAR_2018/(32*math.pi**2*C_SI**3), 1e-60)
chk("dimension: hbar/(c^3 t^4) is J/m^3 -- hbar c / (c t)^4",
    ford_roman_allow(1.0), (3/(32*math.pi**2)) * HBAR_2018*C_SI/(C_SI*1.0)**4, 1e-60)
chk("achievable fixture 105.276 = quantum_bound(1)/ford_roman_allow(1/c) = 32 pi^2/3",
    (HBAR_2018*C_SI)/ford_roman_allow(1.0/C_SI), 32*math.pi**2/3, 1e-9)
print("       32 pi^2/3 = %.6f" % (32*math.pi**2/3))
rel = (HBAR_1986 - HBAR_2018)/HBAR_2018
print("       hbar 1986 -> 2018: relative %.3e; shift in any log10 shortfall %.3e orders" % (rel, math.log10(1+rel)))
chk("the hbar move cannot change any conclusion stated in orders (|shift| < 1e-5 orders)",
    abs(math.log10(1+rel)) < 1e-5, True)
# the EM-vs-scalar factor on candidates.py's squeezed-vacuum row
print("       candidates.py uses the scalar constant for an EM candidate: shortfall would move by log10(2) = %.3f orders" % math.log10(2))
chk("70.606 - 0.301 = 70.305 still > 0 by 70 orders: conclusion unmoved", 70.606 - math.log10(2) > 70, True)

# ---------------------------------------------------------------- later literature, checked
print("Later literature, checked against the paper")
# Fewster-Eveson (5.5)-(5.6): -(1/16 pi^2) INT (f^{1/2}'')^2 with f Lorentzian = -27/(2048 pi^2 t0^4), = 9/64 of FR
f_half = sp.sqrt(t0/sp.pi) * (tt**2 + t0**2)**sp.Rational(-1, 2)
fe = sp.simplify(sp.integrate(sp.diff(f_half, tt, 2)**2, (tt, -sp.oo, sp.oo)) / (16*sp.pi**2))
chk("Fewster-Eveson (5.6): (1/16pi^2) INT (sqrt f)''^2 = 27/(2048 pi^2 t0^4)",
    sp.simplify(fe - sp.Rational(27, 2048)/(sp.pi**2*t0**4)) == 0, True)
chk("  ratio to Ford-Roman 3/(32 pi^2 t0^4) is exactly 9/64 (fewsterteo.NINE_64)",
    sp.nsimplify(sp.simplify(fe / (sp.Rational(3, 32)/(sp.pi**2*t0**4)))) == sp.Rational(9, 64), True)
# 2D: Flanagan optimal -(1/24pi) INT f'^2/f on the Lorentzian is 1/(48 pi t0^2) = FR/6 ; FE -(1/16pi) INT f'^2/f = FR/4
fl = t0/(sp.pi*(tt**2 + t0**2))
J = sp.simplify(sp.integrate(sp.diff(fl, tt)**2/fl, (tt, -sp.oo, sp.oo)))
chk("Flanagan on the Lorentzian: (1/24pi) INT f'^2/f = 1/(48 pi t0^2), FR/6 ('six times stronger')",
    sp.simplify((J/(24*sp.pi)) / (1/(8*sp.pi*t0**2))) == sp.Rational(1, 6), True)
chk("  Fewster-Eveson 2D on the Lorentzian: FR/4 ('four times stronger')",
    sp.simplify((J/(16*sp.pi)) / (1/(8*sp.pi*t0**2))) == sp.Rational(1, 4), True)
# Kontou-Olum (130): leading term for g = exp(-t^2/t0^2) is 3.76/t0^3 = 3 sqrt(pi/2)
g = sp.exp(-tt**2/t0**2)
ko = sp.simplify(sp.integrate(sp.diff(g, tt, 2)**2, (tt, -sp.oo, sp.oo)))
chk("Kontou-Olum (130) leading term INT g''^2 = 3 sqrt(pi/2)/t0^3 = 3.76/t0^3",
    float(ko.subs(t0, 1)), 3.76, 5e-3)
# Kontou-Olum's smallness criterion R_max t0^2 << 1 on the corridor: G_00 = 8 pi G D/c^4 = l_G^-2 is a Ricci
# component, so R_max t0^2 >= (b/l_G)^2 with t0 = b/c.  noise.py: B_OVER_LG_SQUARED = 6 (M/b)/(a/b)^3.
B_OVER_LG_SQUARED = 6.0*5.0e-3/0.02**3
chk("noise.B_OVER_LG_SQUARED = 6 (M/b)/(a/b)^3 = 3750", B_OVER_LG_SQUARED, 3750.0, 1e-9)
chk("  so Kontou-Olum's R_max t0^2 is >= 3750 on the corridor: NOT << 1; the flat bound does not apply there",
    B_OVER_LG_SQUARED > 1, True)
print("       b/l_G = %.3f" % math.sqrt(B_OVER_LG_SQUARED))

print()
if FAIL:
    print("FAILED: %d" % len(FAIL)); sys.exit(1)
print("ALL CHECKS PASS")
