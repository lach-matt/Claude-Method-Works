#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: Painleve-Gullstrand / Lemaitre slicing of Schwarzschild.
Independent of the tree: own Christoffel/Ricci code, never imports nonstatic.py or drivensource.py.
Checks (each prints PASS/FAIL):
 L1  Lemaitre metric -dtau^2 + (rs/R) drho^2 + R^2 dOmega^2, R=(3/2(rho-tau))^(2/3) rs^(1/3), is Ricci-flat
 L2  its W = e^-Lam dR/drho = 1, U = dR/dtau = -sqrt(rs/R), Misner-Sharp m = rs/2
 L3  substituting drho = dtau + sqrt(R/rs) dR gives EXACTLY the PG line element (Martel-Poisson eq 2.7)
     -> Lemaitre time == PG time: same foliation (slicing), different spatial threading
 L4  PG time from Schwarzschild: dT/dr of Martel-Poisson eq (2.5) equals sqrt(1-f)/f (eq 2.4)
 L5  PG metric (MP 2.7) is Ricci-flat; its T=const slices are flat (induced dr^2 + r^2 dOmega^2)
 G1  E=1 radial geodesic: rdot^2 + f = E^2 -> rdot = -sqrt(2M/r)  (MP eq 2.1)
 G2  speed of E=1 observer relative to a static observer (r>2M) = sqrt(2M/r)  ('Newtonian escape velocity')
 G3  Martel-Poisson p-family: Gamma = W = 1/sqrt(p) = E~ (Killing energy): Gamma=1 <=> E~=1 <=> marginally bound
 F1  general flat-slice (generalised PG) metric -N^2dt^2+(dr+beta dt)^2+r^2dOmega^2, N,beta of (t,r):
     Misner-Sharp m = r beta^2/(2N^2);  normal areal velocity U = -beta/N so U^2 = 2m/r for ANY N;
     shift beta = N sqrt(2m/r) equals sqrt(2m/r) iff N = 1
 F2  acceleration of the normal observers a_r = d_r ln N: free fall (geodesic) iff d_r N = 0
 N1  |U| = sqrt(rs/R) > 1 iff R < rs (the tree's AREAL_VELOCITY_IS_CAPPED_AT_LIGHTSPEED = False)
 N2  numeric: sqrt(2m/R) at m=1,R=10 = 0.4472135955 (driven.py fixture); c=G=1 escape velocity sqrt(2GM/r)/c
 Z1  z3: R>0, W>0, W^2 = 1-2m/R+U^2  |-  (W=1) <=> (U^2=2m/R)   (the tree's E3)
 Z2  z3 DRIFT guard: drop W>0 and the equivalence must FAIL (W=-1 witness)
 M1  m<0 (Faraoni-Vachon 2006.10827): E=1 radial geodesic has rdot^2 = 2m/r < 0: no PG observers
"""
import sys
import sympy as sp

ok = True
def rep(tag, cond, note=""):
    global ok
    ok = ok and bool(cond)
    print("%-4s %s  %s" % (tag, "PASS" if cond else "FAIL", note))

def ricci(g, x):
    n = len(x); gi = sp.simplify(g.inv())
    G = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                            for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(G[a][b][c], x[a]) - sp.diff(G[a][b][a], x[c])
                for d in range(n):
                    s += G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a]
            R[b, c] = sp.simplify(s)
    return R

tau, rho, th, ph = sp.symbols("tau rho theta phi", real=True)
rs = sp.Symbol("r_s", positive=True)
# ---- L1/L2 Lemaitre
Rl = (sp.Rational(3, 2)*(rho - tau))**sp.Rational(2, 3)*rs**sp.Rational(1, 3)
gL = sp.diag(-1, rs/Rl, Rl**2, Rl**2*sp.sin(th)**2)
RicL = ricci(gL, [tau, rho, th, ph])
rep("L1", all(sp.simplify(e) == 0 for e in RicL), "Lemaitre Ricci tensor = 0 (vacuum)")
W = sp.simplify(sp.sqrt(Rl/rs)*sp.diff(Rl, rho))
U = sp.simplify(sp.diff(Rl, tau))
m = sp.simplify(Rl/2*(1 - W**2 + U**2))
rep("L2", sp.simplify(W - 1) == 0 and sp.simplify(U + sp.sqrt(rs/Rl)) == 0 and sp.simplify(m - rs/2) == 0,
    "W=%s  U+sqrt(rs/R)=%s  m-rs/2=%s" % (W, sp.simplify(U + sp.sqrt(rs/Rl)), sp.simplify(m - rs/2)))
# ---- L3 Lemaitre -> PG
dtau, dR = sp.symbols("dtau dR")
r = sp.Symbol("r", positive=True)
drho = dtau + sp.sqrt(r/rs)*dR          # from R^(3/2) = (3/2) sqrt(rs) (rho - tau)
# check the differential relation itself
R32 = sp.Rational(3, 2)*sp.sqrt(rs)*(rho - tau)
rel = sp.simplify(sp.diff(Rl, rho) - 1/sp.sqrt(Rl/rs)) == 0 and sp.simplify(sp.diff(Rl, tau) + 1/sp.sqrt(Rl/rs)) == 0
ds2_L = -dtau**2 + rs/r*drho**2
ds2_PG = -dtau**2 + (dR + sp.sqrt(rs/r)*dtau)**2
rep("L3", rel and sp.simplify(sp.expand(ds2_L - ds2_PG)) == 0,
    "dR = sqrt(rs/R)(drho - dtau); (rs/R) drho^2 - dtau^2 == -dtau^2 + (dR + sqrt(rs/R) dtau)^2  -> tau IS PG time")
# ---- L4 PG time from Schwarzschild (M = rs/2)
M = rs/2; f = 1 - 2*M/r
t = sp.Symbol("t")
Tpg = t + 4*M*(sp.sqrt(r/(2*M)) + sp.Rational(1, 2)*sp.log((sp.sqrt(r/(2*M)) - 1)/(sp.sqrt(r/(2*M)) + 1)))
rep("L4", sp.simplify(sp.diff(Tpg, r) - sp.sqrt(1 - f)/f) == 0, "d/dr of MP eq.(2.5) = sqrt(1-f)/f, MP eq.(2.4)")
# ---- L5 PG metric vacuum, flat slices
T = sp.Symbol("T")
bet = sp.sqrt(2*M/r)
gPG = sp.Matrix([[-1 + bet**2, bet, 0, 0], [bet, 1, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2*sp.sin(th)**2]])
RicPG = ricci(gPG, [T, r, th, ph])
rep("L5", all(sp.simplify(e) == 0 for e in RicPG) and gPG[1:, 1:] == sp.diag(1, r**2, r**2*sp.sin(th)**2),
    "PG (MP 2.7) Ricci = 0; induced metric on T=const is dr^2 + r^2 dOmega^2 (flat)")
# ---- G1/G2/G3 geodesics
E = sp.Symbol("E", positive=True)
rdot = -sp.sqrt(E**2 - f)
rep("G1", sp.simplify(rdot.subs(E, 1) + sp.sqrt(2*M/r)) == 0, "E=1: rdot = -sqrt(2M/r)")
gam_rel = E/sp.sqrt(f)       # -u.s with s static unit observer, r>2M
v_rel = sp.sqrt(1 - 1/gam_rel**2)
rep("G2", sp.simplify(v_rel.subs(E, 1) - sp.sqrt(2*M/r)) == 0, "relative speed to static observer at E=1 = sqrt(2M/r) (r > 2M only)")
p = sp.Symbol("p", positive=True)
Wp = 1/sp.sqrt(p)            # induced metric p dr^2 + r^2 dOmega^2 -> dr_areal/dl = 1/sqrt(p)
Up = -sp.sqrt(1 - p*f)/sp.sqrt(p)   # MP: rdot for this family
ident = sp.simplify(Wp**2 - (1 - 2*M/r + Up**2))
rep("G3", ident == 0 and sp.simplify(Wp - 1/sp.sqrt(p)) == 0,
    "p-family: W^2 == 1-2m/r+U^2 with W = 1/sqrt(p) = E~ ; W=1 <=> p=1 <=> E~=1 (PG); W>1 <=> E~>1 unbound")
# ---- F1/F2 generalised flat-slice metric
tt = sp.Symbol("t")
N = sp.Function("N", positive=True)(tt, r)
b = sp.Function("beta", real=True)(tt, r)
g2 = sp.Matrix([[-N**2 + b**2, b], [b, 1]])
g2i = sp.simplify(g2.inv())
grr_up = g2i[1, 1]
mMS = sp.simplify(r/2*(1 - grr_up))          # g^{ab} d_a r d_b r = g^{rr}
n_up = sp.Matrix([1/N, -b/N])               # unit normal to t=const
norm = sp.simplify((n_up.T*g2*n_up)[0])
Un = n_up[1]                                 # n^a d_a r
rep("F1", sp.simplify(mMS - r*b**2/(2*N**2)) == 0 and sp.simplify(norm + 1) == 0
    and sp.simplify(Un**2 - 2*mMS/r) == 0,
    "m_MS = r beta^2/(2N^2); n.n=-1; U_n^2 = 2m/r for ANY lapse N; shift = N sqrt(2m/r)")
# acceleration of n: a_b = n^a nabla_a n_b ; n_b = (-N, 0)
x2 = [tt, r]
n_dn = sp.Matrix([-N, 0])
Gam2 = [[[sp.simplify(sum(g2i[a, d]*(sp.diff(g2[d, bb], x2[c]) + sp.diff(g2[d, c], x2[bb]) - sp.diff(g2[bb, c], x2[d]))
                           for d in range(2))/2) for c in range(2)] for bb in range(2)] for a in range(2)]
acc = [sp.simplify(sum(n_up[a]*(sp.diff(n_dn[bb], x2[a]) - sum(Gam2[c][a][bb]*n_dn[c] for c in range(2))) for a in range(2)))
       for bb in range(2)]
rep("F2", sp.simplify(acc[1] - sp.diff(N, r)/N) == 0, "a_r = d_r N / N : normal observers geodesic iff d_r N = 0 (a_t = %s)" % acc[0])
# ---- N1/N2
Rs = sp.Symbol("R", positive=True)
rep("N1", sp.solve_univariate_inequality(sp.sqrt(rs/Rs) > 1, Rs, relational=False) == sp.Interval.open(0, rs),
    "|U| = sqrt(rs/R) > 1  <=>  0 < R < rs")
val = float(sp.sqrt(sp.Rational(2, 10)))
rep("N2", abs(val - 0.4472135955) < 1e-9, "sqrt(2*1/10) = %.10f (driven.py fixture 0.4472135955)" % val)
# ---- Z1/Z2 z3
try:
    import z3
    Uz, Wz, mz, Rz = z3.Reals("U W m R")
    s = z3.Solver(); s.add(Rz > 0, Wz > 0, Wz*Wz == 1 - 2*mz/Rz + Uz*Uz)
    s.add(z3.Not((Wz == 1) == (Uz*Uz == 2*mz/Rz)))
    r1 = s.check()
    s2 = z3.Solver(); s2.add(Rz > 0, Wz > 0, Wz*Wz == 1 - 2*mz/Rz + Uz*Uz, Wz == 1)
    vac = s2.check()
    rep("Z1", r1 == z3.unsat and vac == z3.sat, "negation unsat (%s); hypotheses+W=1 satisfiable (%s) -> not vacuous" % (r1, vac))
    s3 = z3.Solver(); s3.add(Rz > 0, Wz*Wz == 1 - 2*mz/Rz + Uz*Uz)
    s3.add(z3.Not((Wz == 1) == (Uz*Uz == 2*mz/Rz)))
    r3 = s3.check()
    rep("Z2", r3 == z3.sat, "drop W>0: counterexample exists (%s) %s" % (r3, s3.model() if r3 == z3.sat else ""))
except ImportError:
    rep("Z1", False, "z3 not installed (pip install z3-solver)")
# ---- M1
mneg = sp.Symbol("mu", positive=True)
rd2 = sp.simplify(1 - (1 + 2*mneg/r))       # E=1, f = 1 + 2|m|/r
rep("M1", rd2.is_negative, "m=-|m|: E=1 gives rdot^2 = %s < 0; the tree's threshold_speed returns None for m<0 (consistent)" % rd2)
print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
