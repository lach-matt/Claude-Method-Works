#!/usr/bin/env python3
"""DOCKET 67 -- gr-qc/9701064 supplementary check C10.
Is HPS's ln f bracket (eqs. (5)-(7)), under the conserved reading (116, 21, r^2),
proportional to the Bach tensor, i.e. the Euler-Lagrange tensor of int sqrt(-g) C^2?
That is the geometric tensor a mu-dependent (log) term of a conformal scalar's
renormalized <T_ab> must be (mu enters only through the C^2 counterterm; the Euler
density is topological).  Computed by varying the reduced action
S = int sqrt(f h) r^2 C^2 dl for ds^2 = -f dt^2 + h dl^2 + r^2 dOmega^2, then h = 1.
Transcription of the log bracket is taken from gr-qc_9701064.py (text layer)."""
import sys, os
sys.dont_write_bytecode = True
import sympy as sp
l = sp.Symbol('l', real=True)
t, th, ph = sp.symbols('t theta phi')
fF, hF, rF = [sp.Function(n)(l) for n in ('f', 'h', 'r')]
X = [t, l, th, ph]
g = sp.diag(-fF, hF, rF**2, rF**2*sp.sin(th)**2)
gi = g.inv(); N = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(N))/2) for c in range(N)] for b in range(N)] for a in range(N)]
def riem(a, b, c, d):
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(N))
    return sp.simplify(e)
R4 = [[[[riem(a, b, c, d) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
Ric = sp.Matrix(N, N, lambda b, d: sp.simplify(sum(R4[a][b][a][d] for a in range(N))))
Rs = sp.simplify(sum(gi[a, a]*Ric[a, a] for a in range(N)))
riem2 = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            for d in range(N):
                lo = sum(g[a, e]*R4[e][b][c][d] for e in range(N))
                if lo != 0:
                    riem2 += lo**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
ric2 = sum(Ric[a, a]**2*gi[a, a]**2 for a in range(N))
C2 = sp.simplify(riem2 - 2*ric2 + Rs**2/3)
Lag = sp.sqrt(fF*hF)*rF**2*C2
from sympy.calculus.euler import euler_equations
def EL(q):
    # Euler-Lagrange expression dL/dq - d/dl dL/dq' + d2/dl2 dL/dq'' ...
    e = 0
    for k in range(0, 5):
        dq = sp.diff(q, l, k) if k else q
        e += (-1)**k*sp.diff(sp.diff(Lag, dq), l, k)
    return e
Ef, Eh, Er = EL(fF), EL(hF), EL(rF)
sq = sp.sqrt(fF*hF)*rF**2
# mixed components from delta S = int (sqrt(-g)/2) B^ab delta g_ab:
#   B^t_t = 2 f E_f/sq, B^l_l = 2 h E_h/sq, B^th_th = r E_r/(2 sq)   (theta and phi both carry r^2)
# common factor 2 dropped: (f E_f, h E_h, r E_r/4)/sq
Btt = fF*Ef/sq; Bll = hF*Eh/sq; Bth = rF*Er/(4*sq)
set1 = lambda e: sp.simplify(e.subs(hF, 1).doit())
Btt, Bll, Bth = set1(Btt), set1(Bll), set1(Bth)
f, f1, f2, f3, f4 = [sp.diff(fF, l, k) for k in range(5)]
r, r1, r2, r3, r4 = [sp.diff(rF, l, k) for k in range(5)]
TT_L = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2) - 16*r1**4/r**4 + 116*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2 + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3 + 16*f2*r2/(f*r) + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r) - 16*f1*r3/(f*r) - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r)
LL_L = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r**2) + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3 + 48*f1*r1*f2/(f**2*r) - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 16*f1**2*r2/(f**2*r) + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r) - 16*r2**2/r**2 + 8*f1*f3/f**2 - 16*r1*f3/(f*r) - 16*f1*r3/(f*r) + 32*r1*r3/r**2)
TH_L = (-16/r**4 + 21*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2) - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3 + 28*f1*r1*f2/(f**2*r) + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2 + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3 - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r) + 16*f1*r3/(f*r) - 8*f4/f + 16*r4/r)
lam = sp.Symbol('lam')
# fix lam from the 16/r^4-free comparison: solve TT_L = lam*Btt identically
res = [sp.simplify(sp.expand(TT_L - lam*Btt)), sp.simplify(sp.expand(LL_L - lam*Bll)), sp.simplify(sp.expand(TH_L - lam*Bth))]
# lam from a numeric point, then verify identically
pt = {}
lamv = sp.solve(sp.together(res[0]).as_numer_denom()[0].subs({f4: 0, r4: 1, f3: 0, r3: 0, f2: 0, r2: 0, f1: 0, r1: 0}).subs({fF: 1, rF: 1}), lam)
print("lambda candidates:", lamv)
ok = False
for lv in lamv:
    z = [sp.simplify(e.subs(lam, lv)) for e in res]
    print("residuals with lam =", lv, ":", z)
    if z == [0, 0, 0]:
        ok = True
print("PASS" if ok else "FAIL", "C10 conserved-reading ln f bracket == lambda * Bach (EL tensor of sqrt(-g) C^2)")
# printed reading residual
TT_P = TT_L - 100*f1**2*f2/f**3
LL_P = LL_L + 4*f1**2*r1**2/(f**2*r**2) - 4*f1**2*r1**2/(f**2*r)
if ok:
    zp = [sp.simplify(TT_P - lamv[0]*Btt), sp.simplify(LL_P - lamv[0]*Bll)]
    print("printed-reading residuals (tt, ll):", zp)
sys.exit(0 if ok else 1)
