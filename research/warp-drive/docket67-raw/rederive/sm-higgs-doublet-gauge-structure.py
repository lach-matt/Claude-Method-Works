"""DOCKET 67 re-derivation: sm-higgs-doublet-gauge-structure.
Claims (excite.py D19 / V14 / selftest line 1487):
  (C1) exp(i theta sigma_a), a = T1,T2,T3,Y(=identity), leaves H^dag H invariant, any theta, any complex H.
  (C2) in the doublet, -v is gauge-equivalent to +v.
Checks added here (scope, not repair):
  (S1) SU(2) acts transitively on each sphere H^dag H = r^2, so every function of H ALONE that is gauge invariant is a
       function of H^dag H (the orbit is the whole level set).
  (S2) gauge-boson mass-matrix eigenvalues M^2_ab = H^dag {t_a,t_b} H depend on H only through H^dag H.
  (S3) the element mapping H -> -H survives the SM global quotient (SU(3)xSU(2)xU(1))/Z6: it acts nontrivially on H,
       so it is not in the kernel; the Z6 generator acts trivially on every SM field.
  (S4) CONTROL: a mixed derivative-free invariant psi^dag H (the shape of a Yukawa L-bar H e) CHANGES if H alone is
       rotated at fixed psi, and is invariant only if psi rotates with H -- the scope of 'no derivative-free
       gauge-invariant local observable changes'.
  (S5) the Pythagorean point used by the selftest is exactly unit; the 4 generators move the vev along only 3
       independent directions (orbit S^3 is 3-dimensional; Q = T3 + Y annihilates the vev).
"""
import sympy as sp
from fractions import Fraction as F
ok = []
def chk(lab, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + lab)

th = sp.symbols('theta', real=True)
a, b, c, d = sp.symbols('a b c d', real=True)
H = sp.Matrix([a + sp.I*b, c + sp.I*d])
hh = sp.expand((H.H*H)[0])
s = {"T1": sp.Matrix([[0,1],[1,0]]), "T2": sp.Matrix([[0,-sp.I],[sp.I,0]]),
     "T3": sp.Matrix([[1,0],[0,-1]]), "Y": sp.eye(2)}
# C1
for g, m in s.items():
    U = sp.cos(th)*sp.eye(2) + sp.I*sp.sin(th)*m
    chk("C1 %s: U = exp(i th sigma) (matrix exponential agrees)" % g,
        sp.simplify((sp.exp(sp.I*th*m) - U).rewrite(sp.cos)) == sp.zeros(2))
    chk("C1 %s: U unitary" % g, sp.simplify(U.H*U - sp.eye(2)) == sp.zeros(2))
    chk("C1 %s: (UH)^dag(UH) - H^dag H == 0, any theta, any H" % g,
        sp.simplify(sp.expand(((U*H).H*(U*H))[0] - hh)) == 0)
# physical hypercharge normalisation exp(i alpha Y), Y_H = 1/2
al = sp.symbols('alpha', real=True)
UY = sp.exp(sp.I*al/2)*sp.eye(2)
chk("C1 Y physical normalisation exp(i alpha/2): H^dag H invariant",
    sp.simplify(((UY*H).H*(UY*H))[0] - hh) == 0)
# C2
mI = -sp.eye(2)
chk("C2 -I is in SU(2): unitary and det = 1", mI.H*mI == sp.eye(2) and mI.det() == 1)
chk("C2 -I = exp(i pi sigma3) (an SU(2) element)", sp.simplify(sp.exp(sp.I*sp.pi*s["T3"]) - mI) == sp.zeros(2))
chk("C2 -I = exp(i 2pi Y) with Y_H = 1/2 (a U(1)_Y element)", sp.simplify(UY.subs(al, 2*sp.pi) - mI) == sp.zeros(2))
v = sp.symbols('v', positive=True)
H0 = sp.Matrix([0, v/sp.sqrt(2)])
chk("C2 -I maps (0, v/sqrt2) to (0, -v/sqrt2)", mI*H0 == -H0)
# S1 transitivity: explicit SU(2) element taking any H != 0 to (0, |H|)
h1, h2 = H[0], H[1]
n = sp.sqrt(hh)
W = sp.Matrix([[h2, -h1], [sp.conjugate(h1), sp.conjugate(h2)]])/n  # rows orthonormal
Wn = W*n  # unnormalised; W unitary <=> Wn^dag Wn = (H^dag H) I
chk("S1 W unitary", sp.simplify(sp.expand(Wn.H*Wn) - hh*sp.eye(2)) == sp.zeros(2))
chk("S1 det W = 1", sp.simplify(sp.expand(W.det())) == 1)
WH = sp.simplify(sp.expand(W*H))
chk("S1 W H = (0, sqrt(H^dag H))", sp.simplify(WH[0]) == 0 and sp.simplify(WH[1] - n) == 0)
# S2 gauge boson mass matrix eigenvalues depend only on H^dag H
g1, g2 = sp.symbols('g gp', positive=True)
t = [g1*s["T1"]/2, g1*s["T2"]/2, g1*s["T3"]/2, g2*sp.eye(2)/2]
M2 = sp.zeros(4)
for i in range(4):
    for j in range(4):
        M2[i, j] = sp.expand((H.H*(t[i]*t[j] + t[j]*t[i])*H)[0])
lam = sp.symbols('lam')
cp = sp.expand((M2 - lam*sp.eye(4)).det())
r = sp.symbols('r', positive=True)
M20 = M2.subs({a: 0, b: 0, c: r, d: 0})
cp0 = sp.expand((M20 - lam*sp.eye(4)).det())
chk("S2 char poly of M^2(H) equals that at (0, r) with r^2 = H^dag H",
    sp.simplify(sp.expand(cp - cp0.subs(r, sp.sqrt(hh)))) == 0)
ev = sp.Matrix(M20.subs(r, v/sp.sqrt(2))).eigenvals()
chk("S2 eigenvalues at vev (L = (1/2) M2_ab W^a W^b): {g^2v^2/4 (x2), (g^2+g'^2)v^2/4, 0}",
    set(sp.simplify(e) for e in ev) == {g1**2*v**2/4, (g1**2+g2**2)*v**2/4, 0} and ev.get(0) == 1)
# S3 Z6 quotient
from sympy import Rational as R
fields = {"Q": (3, 2, R(1,6)), "u": (3, 1, R(2,3)), "d": (3, 1, R(-1,3)), "L": (1, 2, R(-1,2)),
          "e": (1, 1, -1), "H": (1, 2, R(1,2))}
def act(f, k3, s2, aY):  # phase of (e^{2pi i k3/3} in SU3 center, (-1)^s2 in SU2 center, e^{i aY Y})
    n3, n2, Y = fields[f]
    ph = sp.exp(2*sp.pi*sp.I*k3/3) if n3 == 3 else 1
    ph *= (-1)**s2 if n2 == 2 else 1
    ph *= sp.exp(sp.I*aY*Y)
    return sp.simplify(ph)
chk("S3 Z6 generator (e^{2pi i/3}, -1, e^{2pi i Y}) acts trivially on Q,u,d,L,e,H",
    all(act(f, 1, 1, 2*sp.pi) == 1 for f in fields))
chk("S3 -I in SU(2) acts as -1 on H (nontrivial, so survives any quotient)", act("H", 0, 1, 0) == -1)
# S4 control
p1, p2, p3, p4 = sp.symbols('p1:5', real=True)
psi = sp.Matrix([p1 + sp.I*p2, p3 + sp.I*p4])
U1 = sp.cos(th)*sp.eye(2) + sp.I*sp.sin(th)*s["T1"]
both = sp.simplify(sp.expand(((U1*psi).H*(U1*H))[0] - (psi.H*H)[0]))
alone = sp.simplify(sp.expand((psi.H*(U1*H))[0] - (psi.H*H)[0]))
chk("S4 psi^dag H invariant when psi and H both rotate", both == 0)
chk("S4 CONTROL psi^dag H CHANGES when H alone rotates (scope limit)", alone != 0)
# S5
co, si = F(3, 5), F(4, 5)
chk("S5 (3/5)^2 + (4/5)^2 == 1 exactly", co*co + si*si == 1)
vhat = sp.Matrix([0, 1])
tang = sp.Matrix.hstack(*[sp.I*m*vhat for m in s.values()])
realtang = sp.Matrix.vstack(tang.applyfunc(sp.re), tang.applyfunc(sp.im))
chk("S5 the 4 generators span a 3-dim tangent space at the vev (rank 3)", realtang.rank() == 3)
chk("S5 Q = (I + sigma3)/2 annihilates the vev (0,1); (I - sigma3)/2 moves it",
    ((s["Y"] - s["T3"])/2*vhat)[1] == 1 and ((s["Y"] + s["T3"])/2*vhat) == sp.zeros(2, 1))
print("ALL PASS" if all(ok) else "SOME FAIL", sum(ok), "/", len(ok))
