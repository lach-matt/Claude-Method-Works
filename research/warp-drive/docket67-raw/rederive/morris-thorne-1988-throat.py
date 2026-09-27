#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Morris-Thorne (1988) throat, as used by tolman.py
(V18a/V18, wormhole_throat, section 1 non-find (b), section 2 withdrawal (i)).
Independent of tolman.py: the Einstein tensor is computed here from the metric.
G = c = 1.  Source equations as restated in Lobo arXiv:0710.4474 eqs (1),(10),(26)-(33),(39),(40)."""
import sympy as sp
import z3

t, r, th, ph = sp.symbols('t r theta phi')
r0, c, rho0 = sp.symbols('r_0 c rho_0', positive=True)
Phi = sp.Function('Phi')(r)
b = sp.Function('b')(r)
x = [t, r, th, ph]
g = sp.diag(-sp.exp(2*Phi), 1/(1 - b/r), r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b_], x[c_]) + sp.diff(g[d, c_], x[b_])
         - sp.diff(g[b_, c_], x[d])) for d in range(n))/2) for c_ in range(n)] for b_ in range(n)] for a in range(n)]
def Ric(b_, c_):
    return sp.simplify(sum(sp.diff(Gam[a][b_][c_], x[a]) - sp.diff(Gam[a][b_][a], x[c_])
        + sum(Gam[a][a][d]*Gam[d][b_][c_] - Gam[a][c_][d]*Gam[d][b_][a] for d in range(n)) for a in range(n)))
R = sp.Matrix(n, n, lambda i, j: Ric(i, j))
Rs = sp.simplify(sum(gi[i, j]*R[i, j] for i in range(n) for j in range(n)))
Gmix = sp.simplify(gi*(R - Rs*g/2))      # G^mu_nu
rho = sp.simplify(-Gmix[0, 0]/(8*sp.pi))
pr = sp.simplify(Gmix[1, 1]/(8*sp.pi))
m = b/2                                   # Misner-Sharp: 1 - 2m/r = g^rr
res = []
def row(name, val, want=0):
    v = sp.simplify(val - want)
    ok = (v == 0)
    res.append(ok)
    print(('PASS ' if ok else 'FAIL ') + name + '   residual: ' + str(v))

# R1. Lobo (26),(27) = MT field equations
row("R1a rho = b'/(8 pi r^2)  [Lobo 26]", rho, sp.diff(b, r)/(8*sp.pi*r**2))
row("R1b p_r = -tau = -(b/r^3 - 2(1-b/r)Phi'/r)/(8 pi)  [Lobo 27]",
    pr, -(b/r**3 - 2*(1 - b/r)*sp.diff(Phi, r)/r)/(8*sp.pi))
# R2. tree's V9-shape: Phi' = (m + 4 pi r^3 p_r)/(r(r-2m))
row("R2 Phi' = (m + 4pi r^3 p_r)/(r(r-2m)) from computed G^r_r",
    sp.diff(Phi, r), (m + 4*sp.pi*r**3*pr)/(r*(r - 2*m)))
# R3. tree V18a: Phi' == 0 everywhere -> 4 pi r^3 p_r = -m everywhere
row("R3 (tree V18a) Phi'=0 => 4 pi r^3 p_r + m = 0",
    (4*sp.pi*r**3*pr + m).subs(sp.Derivative(Phi, r), 0))
# R4. THE THROAT WITHOUT Phi'=0: 4 pi r^3 p_r + m = r(r-b)Phi' -> 0 at b = r for finite Phi'
K = sp.simplify(4*sp.pi*r**3*pr + m)
row("R4a 4 pi r^3 p_r + m = r (r - b) Phi'  (general Phi)", K, r*(r - b)*sp.diff(Phi, r))
bb, dP = sp.symbols('b_val dPhi')
Kthroat = K.subs(sp.Derivative(Phi, r), dP).subs(b, bb).subs(bb, r)
row("R4b at b(r_0) = r_0 with Phi'(r_0) = ANY finite value: 4 pi r_0^3 p_r + m = 0", Kthroat)
prth = pr.subs(sp.Derivative(Phi, r), dP).subs(b, r0).subs(r, r0)
row("R4c p_r(r_0) = -1/(8 pi r_0^2) for ANY finite Phi'(r_0)  [Lobo 30]", prth, -1/(8*sp.pi*r0**2))
# R4d: Phi' divergent but (1-b/r)Phi' -> 0: Phi = c*sqrt(1 - r0/r) (finite Phi, smooth in l), b = r0^2/r
bcat = r0**2/r
Phic = c*sp.sqrt(1 - r0/r)
prc = pr.subs(sp.Derivative(Phi, r), sp.diff(Phic, r)).subs(b, bcat).doit()
row("R4d Phi = c sqrt(1 - r_0/r) (Phi'(r_0) DIVERGES, Phi finite): lim p_r(r_0) = -1/(8 pi r_0^2)",
    sp.limit(prc, r, r0, '+'), -1/(8*sp.pi*r0**2))
# R5. fixture of tolman.py selftest: r_0 = 3
prf = -1/(8*sp.pi*9); mf = sp.Rational(3, 2)
row("R5 fixture r_0 = 3: 4 pi r_0^3 p_r = -3/2 = -m", 4*sp.pi*27*prf, -mf)
# R6. flare-out is a SEPARATE condition.  Einstein static universe: Phi = 0, rho = rho0 const,
# b = (8 pi rho0/3) r^3 ; equator r_e^2 = 3/(8 pi rho0) has b(r_e) = r_e, Phi' = 0, 4pi r^3 p_r = -m,
# but b'(r_e) = 3 > 1: NOT a flare-out throat (a maximal sphere).  Regular centre, not a wormhole.
besu = 8*sp.pi*rho0*r**3/3
re = sp.sqrt(3/(8*sp.pi*rho0))
prE = pr.subs(sp.Derivative(Phi, r), 0).subs(b, besu).doit()
row("R6a ESU p_r = -rho0/3 everywhere", prE, -rho0/3)
row("R6b ESU equator b(r_e) = r_e", besu.subs(r, re), re)
row("R6c ESU equator 4 pi r^3 p_r = -m holds", (4*sp.pi*r**3*prE + besu/2).subs(r, re))
row("R6d ESU equator b'(r_e) = 3  (flare-out b'<1 FAILS)", sp.diff(besu, r).subs(r, re), 3)
# R7. flare-out with m > 0 at the throat: catenary b = r0^2/r (MT's own example, Lobo (40)-(41))
row("R7a catenary b'(r_0) = -1 < 1 (flare-out holds)", sp.diff(bcat, r).subs(r, r0), -1)
row("R7b catenary m(r_0) = r_0/2 > 0 (Misner-Sharp mass positive at a flaring throat)",
    (bcat/2).subs(r, r0), r0/2)
xi0 = sp.simplify(((-pr) - rho).subs(sp.Derivative(Phi, r), 0).subs(b, bcat).doit().subs(r, r0))
row("R7c catenary tau_0 - rho_0 = 2/(8 pi r_0^2) > 0 (MT exoticity, Lobo 39)", xi0, 2/(8*sp.pi*r0**2))
# R8. tree V33 negative control: wrong-sign residual
row("R8 wrong-sign throat residual 4pi r^3 p_r - m = -2m (Phi'=0)",
    (4*sp.pi*r**3*pr - m).subs(sp.Derivative(Phi, r), 0), -2*m)

# Z3: at a throat (b = r > 0) with ANY finite Phi' and ANY b' (flare-out or not), the identity
# m = 4 pi r^3 p_r is impossible: from R4a, 8 pi p_r = -b/r^3 + 2(1-b/r)Phi'/r.
s = z3.Solver()
R_, B_, D_, P_, M_, PI = z3.Reals('r b dPhi p_r m pi')
s.add(PI > 3, PI < 4, R_ > 0, B_ == R_, M_ == B_/2,
      8*PI*P_*R_**3 == -B_ + 2*(R_ - B_)*D_*R_,   # 8 pi p_r r^3 = -b + 2 r (r-b) Phi'
      M_ == 4*PI*R_**3*P_)
z1 = s.check()
print(("PASS " if z1 == z3.unsat else "FAIL ") + "Z1 throat + identity m = 4 pi r^3 p_r: " + str(z1) + " (want unsat)")
res.append(z1 == z3.unsat)
# vacuity guard: drop the identity -> sat
s2 = z3.Solver()
s2.add(PI > 3, PI < 4, R_ > 0, B_ == R_, M_ == B_/2, 8*PI*P_*R_**3 == -B_ + 2*(R_ - B_)*D_*R_)
z2 = s2.check()
print(("PASS " if z2 == z3.sat else "FAIL ") + "Z2 vacuity guard (throat alone satisfiable): " + str(z2))
res.append(z2 == z3.sat)
# Z3: m < 0 at a throat impossible (b = r > 0 => m = r/2 > 0) -- 'flare-out iff m<0' cannot hold at the throat
s3 = z3.Solver(); s3.add(R_ > 0, B_ == R_, M_ == B_/2, M_ < 0)
z3r = s3.check()
print(("PASS " if z3r == z3.unsat else "FAIL ") + "Z3 throat with negative Misner-Sharp mass: " + str(z3r) + " (want unsat)")
res.append(z3r == z3.unsat)
# N1. SI restoration (the tree uses G = c = 1; this is the only place a datum could enter).
# tau_0 = c^4/(8 pi G r_0^2).  c exact; G = 6.67430(15)e-11 (CODATA 2022, arXiv:2409.03787 Table XXXII, READ).
# The spread of the 16 G inputs in CODATA 2022 Table XXX (READ): 6.67191e-11 (LENS-14) .. 6.67559e-11 (BIPM-01).
import math
cc = 299792458.0
for Gv, lab in ((6.67430e-11, 'CODATA2022'), (6.67191e-11, 'min input'), (6.67559e-11, 'max input')):
    tau10 = cc**4/(8*math.pi*Gv*10.0**2)
    print('INFO N1 tau_0(r_0 = 10 m) with G=%s (%s): %.6e Pa = %.6e dyn/cm^2' % (Gv, lab, tau10, tau10*10))
spread = (6.67559 - 6.67191)/6.67430
print('INFO N1 fractional spread of G inputs: %.3e -> tau_0 moves by the same fraction; the SIGN and the identity 4 pi r_0^3 p_r = -m are G-independent' % spread)
res.append(spread < 1e-3)

print("\n%d/%d checks pass" % (sum(res), len(res)))
raise SystemExit(0 if all(res) else 1)
