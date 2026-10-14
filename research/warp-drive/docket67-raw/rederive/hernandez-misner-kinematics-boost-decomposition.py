#!/usr/bin/env python3
"""DOCKET 67 re-derivation: boost decomposition of (U, Gamma) -- 'standard
Misner-Sharp-Hernandez kinematics' as used at research/warp-drive/foliation.py
:128-163, 381-382, 649-656.  Independent of foliation.py: nothing imported
from the tree.  sympy + z3 + numeric.  Exit 0 iff every check has its wanted
outcome (including the checks that are SUPPOSED to fail, marked want=False).
"""
import sys, random, math
import sympy as sp

results = []
def check(label, ok, want=True):
    good = (bool(ok) == want)
    results.append((label, bool(ok), want, good))
    print(("PASS " if good else "FAIL ") + label + ("" if want else "   [want: False]"))

t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]

# ---------------------------------------------------------------- A
# MSH comoving ('cosmic time') metric, HMM 2017 eq.(2):  a, b, R free functions
Phi = sp.Function("Phi")(t, r); Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2*Phi), sp.exp(2*Lam), R**2, R**2*sp.sin(th)**2)
gi = g.inv()
dR = sp.Matrix([sp.diff(R, v) for v in x])
u = sp.Matrix([sp.exp(-Phi), 0, 0, 0]); n = sp.Matrix([0, sp.exp(-Lam), 0, 0])
dot = lambda A, B: sp.simplify((A.T*g*B)[0, 0])
U = sp.simplify((u.T*dR)[0, 0]); G = sp.simplify((n.T*dR)[0, 0])
check("A1 U = u^a d_aR = e^{-Phi} R_t  (= D_t R, HMM eq.4; sign +)",
      sp.simplify(U - sp.exp(-Phi)*sp.diff(R, t)) == 0)
check("A2 Gamma = n^a d_aR = e^{-Lam} R_r (= D_r R, HMM eq.5)",
      sp.simplify(G - sp.exp(-Lam)*sp.diff(R, r)) == 0)
gradR2 = sp.simplify((dR.T*gi*dR)[0, 0])
check("A3 g^ab d_aR d_bR = Gamma^2 - U^2  (HMM p.6)", sp.simplify(gradR2 - (G**2 - U**2)) == 0)

# boost with a FREE rapidity function w(t,r)
w = sp.Function("w")(t, r)
up = sp.cosh(w)*u + sp.sinh(w)*n
np_ = sp.sinh(w)*u + sp.cosh(w)*n
check("A4 u'.u' = -1", sp.simplify(dot(up, up) + 1) == 0)
check("A5 n'.n' = +1", sp.simplify(dot(np_, np_) - 1) == 0)
check("A6 u'.n' = 0", sp.simplify(dot(up, np_)) == 0)
Up = sp.simplify((up.T*dR)[0, 0]); Gp = sp.simplify((np_.T*dR)[0, 0])
check("A7 U' = cosh(w) U + sinh(w) Gamma  (foliation.py:132)",
      sp.simplify(Up - (sp.cosh(w)*U + sp.sinh(w)*G)) == 0)
check("A8 Gamma' = sinh(w) U + cosh(w) Gamma  (foliation.py:133)",
      sp.simplify(Gp - (sp.sinh(w)*U + sp.cosh(w)*G)) == 0)
check("A9 Gamma'^2 - U'^2 = Gamma^2 - U^2  (foliation.py:134, INVARIANT)",
      sp.simplify(sp.expand(Gp**2 - Up**2 - (G**2 - U**2)).rewrite(sp.exp)) == 0)

# ---------------------------------------------------------------- B
# NOT only the MSH diagonal gauge: a general 2-metric on the (t,r) quotient
# with shift, h = [[-A^2 + B^2 s^2, B^2 s],[B^2 s, B^2]] (ADM form).  The unit
# normal to t = const and its orthogonal unit vector; the invariant must hold.
A_, B_, s_ = [sp.Function(nm, positive=True)(t, r) for nm in ("A", "B")] + [sp.Function("s")(t, r)]
h = sp.Matrix([[-A_**2 + B_**2*s_**2, B_**2*s_], [B_**2*s_, B_**2]])
hi = sp.simplify(h.inv())
dR2 = sp.Matrix([sp.diff(R, t), sp.diff(R, r)])
nu = sp.Matrix([1/A_, -s_/A_])           # future unit normal (contravariant)
ex = sp.Matrix([0, 1/B_])                # unit radial vector tangent to slice
d2 = lambda P, Q: sp.simplify((P.T*h*Q)[0, 0])
check("B1 ADM normal u.u = -1", sp.simplify(d2(nu, nu) + 1) == 0)
check("B2 ADM radial n.n = +1", sp.simplify(d2(ex, ex) - 1) == 0)
check("B3 u.n = 0", sp.simplify(d2(nu, ex)) == 0)
Ua = (nu.T*dR2)[0, 0]; Ga = (ex.T*dR2)[0, 0]
check("B4 with shift: g^ab d_aR d_bR = Gamma^2 - U^2 (frame identity h^-1 = -uu + nn)",
      sp.simplify((dR2.T*hi*dR2)[0, 0] - (Ga**2 - Ua**2)) == 0)

# ---------------------------------------------------------------- C
# HMM 2017 eq.(15): dR/dtau_comoving = U + Gamma v.  The moving object's own
# proper time is dtau' = dtau/gamma, so ITS U' = gamma (U + Gamma v).  With
# v = tanh w this is the tree's boost.  Derive it, do not assume it.
v = sp.symbols("v", real=True)
Us, Gs, ww = sp.symbols("U Gamma w", real=True)
gam = 1/sp.sqrt(1 - v**2)
Uobj = gam*(Us + Gs*v)
check("C1 gamma(U + Gamma v) at v = tanh w  ==  cosh w U + sinh w Gamma",
      sp.simplify((Uobj.subs(v, sp.tanh(ww)) - (sp.cosh(ww)*Us + sp.sinh(ww)*Gs)).rewrite(sp.exp)) == 0)
# 4-velocity form: u_obj = gamma (u + v n) is unit timelike and equals the boost
uobj = gam*(u + v*n)
check("C2 gamma(u + v n) is unit timelike", sp.simplify(dot(uobj, uobj) + 1) == 0)

# ---------------------------------------------------------------- D
# Faraoni et al 1610.05822 eqs.(4.16)-(4.17): comoving vs Kodama observers,
# gamma_rel = 1/sqrt(1 - U^2/Gamma^2), |v_rel| = |U/Gamma|.  The Kodama
# observer has U_K = 0 (K.dR = 0).  Tree: Gamma = k cosh psi, U = k sinh psi.
psi, k = sp.symbols("psi k", positive=True)
GG = k*sp.cosh(psi); UU = k*sp.sinh(psi)
check("D1 tree's psi: cosh psi = Gamma/k equals Faraoni gamma_rel = (1-U^2/Gamma^2)^-1/2",
      sp.simplify(sp.cosh(psi) - 1/sp.sqrt(1 - UU**2/GG**2)) == 0)
check("D2 tanh psi = U/Gamma = Faraoni |v_rel| (psi>0)", sp.simplify(sp.tanh(psi) - UU/GG) == 0)
check("D3 boosting by -psi lands on U = 0, Gamma = k (the Kodama/anchor slice)",
      sp.simplify(sp.cosh(-psi)*UU + sp.sinh(-psi)*GG) == 0
      and sp.simplify(sp.sinh(-psi)*UU + sp.cosh(-psi)*GG - k) == 0)

# ---------------------------------------------------------------- E
# Tree's O12 transitivity witness c = (G1G2-U1U2)/k^2, s = (U2G1-U1G2)/k^2
p1, p2 = sp.symbols("psi1 psi2", real=True)
G1, U1, G2, U2 = k*sp.cosh(p1), k*sp.sinh(p1), k*sp.cosh(p2), k*sp.sinh(p2)
c = (G1*G2 - U1*U2)/k**2; s = (U2*G1 - U1*G2)/k**2
check("E1 c = cosh(psi2 - psi1) (>= 1, orthochronous)", sp.simplify((c - sp.cosh(p2 - p1)).rewrite(sp.exp)) == 0)
check("E2 s = sinh(psi2 - psi1)", sp.simplify((s - sp.sinh(p2 - p1)).rewrite(sp.exp)) == 0)
check("E3 (c,s) maps state 1 to state 2",
      sp.simplify((c*U1 + s*G1 - U2).rewrite(sp.exp)) == 0 and sp.simplify((s*U1 + c*G1 - G2).rewrite(sp.exp)) == 0)

# z3: the same, over the reals with no parametrisation
try:
    import z3
    zU1, zG1, zU2, zG2, zk = z3.Reals("U1 G1 U2 G2 k")
    zc, zs = z3.Reals("c s")
    hyp = z3.And(zk > 0, zG1 > 0, zG2 > 0, zG1*zG1 - zU1*zU1 == zk*zk, zG2*zG2 - zU2*zU2 == zk*zk,
                 zc*zk*zk == zG1*zG2 - zU1*zU2, zs*zk*zk == zU2*zG1 - zU1*zG2)
    concl = z3.And(zc*zc - zs*zs == 1, zc > 0, zc*zU1 + zs*zG1 == zU2, zs*zU1 + zc*zG1 == zG2)
    so = z3.Solver(); so.add(hyp, z3.Not(concl)); r1 = so.check()
    check("E4 z3: transitivity on the Gamma>0 branch (unsat of negation)", r1 == z3.unsat)
    so = z3.Solver(); so.add(hyp); check("E5 z3 vacuity guard: hypotheses satisfiable", so.check() == z3.sat)
    # Opposite branches: NO orthochronous boost joins Gamma>0 to Gamma<0
    zG2n = z3.Real("G2n")
    so = z3.Solver()
    so.add(zk > 0, zG1 > 0, zG2n < 0, zG1*zG1 - zU1*zU1 == zk*zk, zG2n*zG2n - zU2*zU2 == zk*zk,
           zc*zc - zs*zs == 1, zc > 0, zc*zU1 + zs*zG1 == zU2, zs*zU1 + zc*zG1 == zG2n)
    check("E6 z3: orthochronous boost CANNOT flip sign of Gamma (unsat)", so.check() == z3.unsat)
except ImportError:
    print("z3 absent -- E4-E6 skipped"); results.append(("E4-6 z3 skipped", False, True, False))

# ---------------------------------------------------------------- F
# ORIENTATION.  The tree's prose range 'Gamma in [k, inf)' and the biconditional
# 'Gamma > 1 in EVERY foliation <=> m < 0' (foliation.py:140-148) assume n is
# oriented so Gamma > 0.  Its z3 carries G > 0 (foliation.py:790, 843).  With n
# reversed the SAME geometry gives Gamma <= -k.
def gamma_branch(m, Rv, psi_v, sign):
    kk = math.sqrt(1 - 2*m/Rv)
    return sign*kk*math.cosh(psi_v)
m, Rv = -1.0, 10.0
outward = all(gamma_branch(m, Rv, p_, +1) > 1 for p_ in [x_/10 for x_ in range(-50, 51)])
inward = all(gamma_branch(m, Rv, p_, -1) > 1 for p_ in [x_/10 for x_ in range(-50, 51)])
absval = all(abs(gamma_branch(m, Rv, p_, -1)) > 1 for p_ in [x_/10 for x_ in range(-50, 51)])
check("F1 m<0, n outward: Gamma > 1 on every sampled foliation", outward)
check("F2 m<0, n INWARD: 'Gamma > 1 in every foliation' holds", inward, want=False)
check("F3 m<0: |Gamma| > 1 in every foliation, either orientation", absval)

# ---------------------------------------------------------------- G
# The docstring sign 'U = -u^a d_a R' (foliation.py:129) vs the code and MSH
# (U = +u^a d_a R).  With U~ = -U the boost reads U~' = cosh w U~ - sinh w Gamma,
# i.e. w -> -w; the invariant is unchanged.
Ut = -Us
check("G1 docstring sign: invariant unchanged",
      sp.simplify(Gs**2 - Ut**2 - (Gs**2 - Us**2)) == 0)
check("G2 docstring sign: tree's printed boost holds for U~ only with w -> -w",
      sp.simplify(-(sp.cosh(ww)*Us + sp.sinh(ww)*Gs) - (sp.cosh(-ww)*Ut + sp.sinh(-ww)*Gs)) == 0)

# ---------------------------------------------------------------- H
# Trapped branch (O11): U^2 - Gamma^2 = K^2 > 0: Gamma = K sinh chi covers R.
K = sp.symbols("K", positive=True); chi = sp.symbols("chi", real=True)
target = sp.symbols("T", real=True)
sol = sp.asinh(target/K)
check("H1 trapped: every real Gamma = K sinh(chi) is attained (chi = asinh(T/K))",
      sp.simplify(K*sp.sinh(sol) - target) == 0)

# ---------------------------------------------------------------- numeric spot
random.seed(67)
worst = 0.0
for _ in range(2000):
    Uv, Gv, wv = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-4, 4)
    U2v = math.cosh(wv)*Uv + math.sinh(wv)*Gv; G2v = math.sinh(wv)*Uv + math.cosh(wv)*Gv
    worst = max(worst, abs((G2v**2 - U2v**2) - (Gv**2 - Uv**2))/(1 + abs(Gv**2 - Uv**2)*math.cosh(2*wv)))
check("N1 numeric: invariant preserved to 1e-9 (relative) over 2000 random boosts", worst < 1e-9)

bad = [x_ for x_ in results if not x_[3]]
print("\n%d checks, %d with unwanted outcome" % (len(results), len(bad)))
sys.exit(1 if bad else 0)
