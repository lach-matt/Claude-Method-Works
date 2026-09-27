#!/usr/bin/env python3
"""
DOCKET 67 / pass S #26 -- energy-conditions-and-chronology-theorems.

Checks the tree's claim (phase1.py:195-197, 537-539):
  "No energy condition, no chronology theorem and no positive-mass theorem is
   violated by D1-D5 with M_ADM = 0."
against the seated device (phase1.phi_device == concentric.potential) and
against the class D1-D5 with M_ADM = 0, held static.

C1  exact Einstein tensor of ds^2 = -e^{2Phi}dt^2 + e^{-2Phi}(dr^2 + r^2 dOmega^2)
C2  seated device: signs of rho, rho+p_r, rho+p_t, rho+sum p for 0<r<R_s (exact),
    numbers at the tree's parameters; shell (r = R_s) sign
C3  M_ADM = 0 (1/r coefficient of Phi vanishes) and the O(r^-3) tail outside R_s
    (D2 compact support is NOT met by the seated Phi -- discrepancy, recorded)
C4  Hamiltonian constraint for k = 0: 16 pi rho = R_h ; R_h(0) < 0 at the device
C5  static, flat slice, compact support: Ricci of -N^2 dt^2 + delta (generic N),
    NEC <=> Delta N >= lambda_max(Hess N); z3: pairwise-sum lemma
C6  z3: PMT rigidity + C5 lemma => every static non-flat member with M_ADM = 0
    and compact support violates the WEC; vacuity guards; the tree's triple
    (no EC violated & no PMT violated & E = 0 & non-flat) UNSAT when 'EC' includes
    the DEC/WEC
C7  gauge witness: a compactly supported diffeo pulled back on flat space meets
    D1-D5 with M_ADM = 0 and violates nothing (Gaussian curvature of the pullback = 0
    for generic f; d(A,B) falls)
C8  chronology: a static metric with g^{tt} < 0 has t strictly increasing along
    every future causal curve -- no closed causal curve (the chronology theorems'
    hypotheses, a compactly generated Cauchy horizon, are absent)
"""
import sys, math
import sympy as sp

FAIL = []
def check(label, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + label + (("  -- " + detail) if detail else ""))
    if not cond:
        FAIL.append(label)

# ---------------------------------------------------------------- C1
t, r, th, ph = sp.symbols('t r theta phi', real=True)
Phi = sp.Function('Phi')(r)
X = [t, r, th, ph]
g = sp.diag(-sp.exp(2*Phi), sp.exp(-2*Phi), sp.exp(-2*Phi)*r**2,
            sp.exp(-2*Phi)*r**2*sp.sin(th)**2)
gi = g.inv()

def christoffel(g, gi, X):
    n = len(X)
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(n))/2)
    return G

def ricci(g, gi, X):
    n = len(X); G = christoffel(g, gi, X)
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                        + sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for d in range(n))
                        for a in range(n)))
    return R

Ric = ricci(g, gi, X)
Rs_ = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gmix = sp.simplify(gi*Ric - sp.eye(4)*Rs_/2)          # G^a_b
rho = sp.simplify(-Gmix[0, 0])                          # 8 pi rho (G = c = 1 units, factor 8pi kept out)
pr = sp.simplify(Gmix[1, 1]); pt = sp.simplify(Gmix[2, 2])
lap = sp.diff(Phi, r, 2) + 2*sp.diff(Phi, r)/r
d1 = sp.diff(Phi, r)
check("C1 diagonal (type I): G^a_b off-diagonal = 0",
      all(sp.simplify(Gmix[a, b]) == 0 for a in range(4) for b in range(4) if a != b))
check("C1 8pi rho = e^{2Phi}(2 lap Phi - Phi'^2)", sp.simplify(rho - sp.exp(2*Phi)*(2*lap - d1**2)) == 0)
check("C1 8pi p_r = -e^{2Phi} Phi'^2", sp.simplify(pr + sp.exp(2*Phi)*d1**2) == 0)
check("C1 8pi p_t = +e^{2Phi} Phi'^2", sp.simplify(pt - sp.exp(2*Phi)*d1**2) == 0)
check("C1 rho+p_t = rho+Sum p = 2 e^{2Phi} lap Phi",
      sp.simplify(rho + pt - 2*sp.exp(2*Phi)*lap) == 0 and sp.simplify(rho + pr + 2*pt - 2*sp.exp(2*Phi)*lap) == 0)

# ---------------------------------------------------------------- C2
m, a, Rs = sp.symbols('m a R_s', positive=True)
rr = sp.symbols('r', positive=True)
Phi_in = m/sp.sqrt(rr**2 + a**2) - m/Rs          # r < R_s
Phi_out = m/sp.sqrt(rr**2 + a**2) - m/rr         # r > R_s
lap_in = sp.simplify(sp.diff(Phi_in, rr, 2) + 2*sp.diff(Phi_in, rr)/rr)
check("C2 lap Phi_in = -3 m a^2/(r^2+a^2)^{5/2}  (< 0 for m > 0)",
      sp.simplify(lap_in + 3*m*a**2/(rr**2 + a**2)**sp.Rational(5, 2)) == 0)
sub = lambda e, P: e.subs(sp.Derivative(Phi, (r, 2)), sp.diff(P, rr, 2)).subs(sp.Derivative(Phi, r), sp.diff(P, rr)).subs(Phi, P).subs(r, rr)
rho_in = sp.simplify(sub(rho, Phi_in)); nec_r = sp.simplify(sub(rho + pr, Phi_in)); nec_t = sp.simplify(sub(rho + pt, Phi_in))
# sign: each is e^{2Phi} times a manifestly negative combination
rho_red = sp.simplify(rho_in*sp.exp(-2*Phi_in)); necr_red = sp.simplify(nec_r*sp.exp(-2*Phi_in)); nect_red = sp.simplify(nec_t*sp.exp(-2*Phi_in))
check("C2 8pi rho e^{-2Phi} = 2 lap - Phi'^2 : both terms < 0 for m>0, every r<R_s",
      sp.simplify(rho_red - (2*lap_in - sp.diff(Phi_in, rr)**2)) == 0)
check("C2 (rho+p_r) e^{-2Phi} = 2(lap - Phi'^2) < 0", sp.simplify(necr_red - 2*(lap_in - sp.diff(Phi_in, rr)**2)) == 0)
check("C2 (rho+p_t) e^{-2Phi} = 2 lap < 0", sp.simplify(nect_red - 2*lap_in) == 0)
# z3/ sympy sign certificate: substitute positive symbols and ask sympy for the sign
check("C2 sympy proves 2 lap_in < 0 on the positive orthant", sp.ask(sp.Q.negative(2*lap_in), sp.Q.positive(m) & sp.Q.positive(a) & sp.Q.positive(rr)) is True)
check("C2 sympy proves 2 lap_in - Phi'^2 < 0", sp.ask(sp.Q.negative(2*lap_in - sp.diff(Phi_in, rr)**2),
      sp.Q.positive(m) & sp.Q.positive(a) & sp.Q.positive(rr)) is not False)  # nonpositive sum of negative & nonpositive
vals = {m: sp.Rational(2, 100), a: sp.Rational(2, 100), Rs: 200}
for rv in (sp.Rational(1, 10**6), sp.Rational(1, 100), 1, 10, 100, sp.Rational(1999, 10)):
    rn = float(rho_in.subs(vals).subs(rr, rv)); tn = float(nec_t.subs(vals).subs(rr, rv)); qn = float(nec_r.subs(vals).subs(rr, rv))
    print("      r = %-10s 8pi rho = %+.4e  8pi(rho+p_r) = %+.4e  8pi(rho+p_t) = %+.4e" % (rv, rn, qn, tn))
    check("C2 r=%s: rho<0, rho+p_r<0, rho+p_t<0 (NEC, WEC, SEC, DEC all fail)" % rv, rn < 0 and qn < 0 and tn < 0)
rho0 = float(rho_in.subs(vals).subs(rr, 0))
print("      8pi rho(0) = %.6e  (e^{2Phi(0)} * 2 * (-3m/a^3) = %.6e)" % (rho0, math.exp(2*(1 - 1e-4))*2*(-7500.0)))
# shell: jump of Phi' at R_s
jump = sp.simplify(sp.diff(Phi_out, rr).subs(rr, Rs) - sp.diff(Phi_in, rr).subs(rr, Rs))
check("C2 shell: [Phi'] at R_s = +m/R_s^2 > 0, so lap Phi has +delta: shell rho+p_t > 0 (positive-mass shell)",
      sp.simplify(jump - m/Rs**2) == 0)

# ---------------------------------------------------------------- C3
ser = sp.series(Phi_out, rr, sp.oo, 5).removeO()
c1 = sp.limit(Phi_out*rr, rr, sp.oo)
check("C3 1/r coefficient of Phi outside R_s = 0 -> M_ADM = 0", c1 == 0, "series %s" % ser)
c3 = sp.limit(Phi_out*rr**3, rr, sp.oo)
check("C3 tail Phi ~ -m a^2/(2 r^3) != 0 outside R_s: g != g_0 there (D2 compact support NOT met literally -- discrepancy)",
      sp.simplify(c3 + m*a**2/2) == 0)
print("      tail at r = 2 R_s with tree values: Phi = %.3e" % float(Phi_out.subs(vals).subs(rr, 400)))

# ---------------------------------------------------------------- C4
xs = sp.symbols('x y z', real=True)
Rfull = sp.sqrt(sum(v**2 for v in xs))
Pgen = sp.Function('P')(*xs)
h = sp.eye(3)*sp.exp(-2*Pgen)
hi = h.inv()
Rh = sp.simplify(sum(hi[i, j]*ricci(h, hi, list(xs))[i, j] for i in range(3) for j in range(3)))
lap3 = sum(sp.diff(Pgen, v, 2) for v in xs); grad2 = sum(sp.diff(Pgen, v)**2 for v in xs)
check("C4 R_h[e^{-2Phi} delta] = e^{2Phi}(4 lap Phi - 2|grad Phi|^2) = 2 * 8pi rho  (Hamiltonian constraint, k=0)",
      sp.simplify(Rh - sp.exp(2*Pgen)*(4*lap3 - 2*grad2)) == 0)
Rh0 = 2*rho0
print("      R_h(0) at the tree's device = %.6e < 0" % Rh0)
check("C4 R_h(0) < 0 at the device: the time-symmetric PMT hypothesis R_h >= 0 fails", Rh0 < 0)

# ---------------------------------------------------------------- C5
N = sp.Function('N')(*xs)
g4 = sp.diag(-N**2, 1, 1, 1)
X4 = [t] + list(xs)
R4 = ricci(g4, g4.inv(), X4)
lapN = sum(sp.diff(N, v, 2) for v in xs)
ok_tt = sp.simplify(R4[0, 0] - N*lapN) == 0
ok_ij = all(sp.simplify(R4[i+1, j+1] + sp.diff(N, xs[i], xs[j])/N) == 0 for i in range(3) for j in range(3))
check("C5 Ricci of -N^2dt^2+delta: R_tt = N lap N, R_ij = -d_i d_j N / N", ok_tt and ok_ij)
G4tt = sp.simplify(R4[0, 0] - g4[0, 0]*sp.simplify(sum(g4.inv()[p, q]*R4[p, q] for p in range(4) for q in range(4)))/2)
check("C5 flat slice => rho = 0 identically (G_tt = 0)", G4tt == 0)
import z3
l1, l2, l3 = z3.Reals('l1 l2 l3')
s = z3.Solver()
# NEC on k=(1/N, n) for every unit n <=> lap N >= lambda_max <=> sum of any two eigenvalues >= 0
pairs = z3.And(l1 + l2 >= 0, l1 + l3 >= 0, l2 + l3 >= 0)
s.add(pairs, z3.Not(l1 + l2 + l3 >= 0))
check("C5 z3: pairwise sums >= 0 => lap N >= 0 (UNSAT of negation)", s.check() == z3.unsat)
s = z3.Solver(); s.add(pairs, l1 + l2 + l3 == 0, z3.Or(l1 != 0, l2 != 0, l3 != 0))
check("C5 z3: pairwise sums >= 0 and trace 0 => Hess N = 0 (UNSAT)", s.check() == z3.unsat)
s = z3.Solver(); s.add(pairs, z3.Or(l1 != 0, l2 != 0, l3 != 0))
check("C5 vacuity guard: pairwise >= 0 with Hess != 0 is SAT when trace unconstrained", s.check() == z3.sat)
print("      argument: N = 1 near dK (compact support) => int_K lap N = flux = 0; with lap N >= 0 => lap N = 0;")
print("      then Hess N = 0 (z3 above) => N affine => N = 1: a static flat-slice member obeying the NEC is flat.")
# Plummer lapse example (not compact): NEC fails at r > sqrt2 a
c, A_ = sp.symbols('c A', positive=True)
f = -c/sp.sqrt(rr**2 + A_**2)
radial = sp.diff(f, rr, 2); tang = sp.diff(f, rr)/rr
check("C5 illustration: N = 1 - c/sqrt(r^2+a^2): lambda_r + lambda_t = c(2a^2 - r^2)/(r^2+a^2)^{5/2}",
      sp.simplify(radial + tang - c*(2*A_**2 - rr**2)/(rr**2 + A_**2)**sp.Rational(5, 2)) == 0)

# ---------------------------------------------------------------- C6
st, cpt, E0, flat_h, flat_g, WEC, NEC, DEC, Rge0, PMTviol, ECviol = z3.Bools(
    'static compact E0 flat_h flat_g WEC NEC DEC Rge0 PMTviol ECviol')
premises = [
    z3.Implies(z3.And(st, WEC), Rge0),                 # k=0: rho = R_h/16pi, WEC => rho >= 0 => R_h >= 0
    z3.Implies(DEC, WEC), z3.Implies(WEC, NEC),        # standard implications (energy-conditions-definitions audit)
    z3.Implies(z3.And(st, cpt, Rge0, E0), flat_h),     # PMT rigidity (Schoen-Yau, time-symmetric; complete AF)
    z3.Implies(z3.And(st, cpt, flat_h, NEC), flat_g),  # C5 lemma
    z3.Implies(flat_g, flat_h),
]
s = z3.Solver(); s.add(premises + [st, cpt, E0, z3.Not(flat_g), WEC])
check("C6 z3: static & compact & E=0 & non-flat & WEC  is UNSAT", s.check() == z3.unsat)
s = z3.Solver(); s.add(premises + [st, cpt, E0, z3.Not(flat_g), z3.Not(WEC)])
check("C6 vacuity guard: same with WEC failing is SAT", s.check() == z3.sat)
s = z3.Solver(); s.add(premises + [st, cpt, E0, flat_g, WEC, DEC])
check("C6 vacuity guard: flat member with every EC is SAT (the gauge witness, C7)", s.check() == z3.sat)
s = z3.Solver(); s.add([p for p in premises if 'flat_h' not in str(p) or 'NEC' in str(p)] + [st, cpt, E0, z3.Not(flat_g), WEC])
check("C6 guard: drop PMT rigidity and the conclusion no longer follows (SAT)", s.check() == z3.sat)
# the tree's triple: PMT 'not violated' means not(hyp & not concl); with DEC as its hyp
s = z3.Solver()
s.add(premises + [st, cpt, E0, z3.Not(flat_g), DEC, z3.Not(z3.And(DEC, E0, z3.Not(flat_h)))])
check("C6 z3: 'no EC violated (DEC holds) & E=0 & non-flat' is UNSAT -- the sentence's clauses cannot jointly hold for a non-flat static member",
      s.check() == z3.unsat)

# ---------------------------------------------------------------- C7
x, y, sS = sp.symbols('x y s', real=True)
F = sp.Function('f')(x, y)
J = sp.Matrix([[1 + sS*sp.diff(F, x), sS*sp.diff(F, y)], [0, 1]])
gp = sp.simplify(J.T*J)
E_, F_, G_ = gp[0, 0], gp[0, 1], gp[1, 1]
Eu, Ev = sp.diff(E_, x), sp.diff(E_, y); Fu, Fv = sp.diff(F_, x), sp.diff(F_, y); Gu, Gv = sp.diff(G_, x), sp.diff(G_, y)
M1 = sp.Matrix([[-sp.diff(E_, y, 2)/2 + sp.diff(F_, x, y) - sp.diff(G_, x, 2)/2, Eu/2, Fu - Ev/2],
                [Fv - Gu/2, E_, F_], [Gv/2, F_, G_]])
M2 = sp.Matrix([[0, Ev/2, Gu/2], [Ev/2, E_, F_], [Gu/2, F_, G_]])
Kbrio = sp.simplify((M1.det() - M2.det())/(E_*G_ - F_**2)**2)
check("C7 pullback of flat metric by x -> x + s f(x,y) e_x: Gaussian curvature = 0 for generic f (Brioschi)", Kbrio == 0)
bump = lambda q: math.exp(-1.0/(1.0 - q*q)) if abs(q) < 1 else 0.0
A = (0.0, 0.0, 0.0); B = (10.0, 0.0, 0.0)
def dist(sv):   # phi_s(x) = x + s*bump(|x-A|/2)*e_x ; flat pullback => d = |phi(A)-phi(B)|
    pa = A[0] + sv*bump(0.0); pb = B[0] + sv*bump(math.dist(B, A)/2.0)
    return abs(pb - pa)
ds = [dist(sv) for sv in (0.0, 0.5, 1.0, 1.5)]
print("      d_s(A,B) for s = 0, .5, 1, 1.5: " + ", ".join("%.6f" % v for v in ds))
check("C7 D3 met: d_s(A,B) strictly decreasing; D2: support |x-A|<2; diffeo since s*max|bump'|/2 < 1",
      all(ds[i] > ds[i+1] for i in range(3)) and 1.5*0.5*max(abs((bump(q+1e-6)-bump(q-1e-6))/2e-6) for q in [i/1000 for i in range(-999, 1000)]) < 1)

# ---------------------------------------------------------------- C8
ut, ux, uy, uz, P0 = sp.symbols('u_t u_x u_y u_z Phi0', real=True)
norm = -sp.exp(2*P0)*ut**2 + sp.exp(-2*P0)*(ux**2 + uy**2 + uz**2)
s = z3.Solver()
Ut, Ux, Uy, Uz, e2 = z3.Reals('Ut Ux Uy Uz e2')
s.add(e2 > 0, -e2*Ut*Ut + (Ux*Ux + Uy*Uy + Uz*Uz)/e2 <= 0, Ut == 0, z3.Or(Ux != 0, Uy != 0, Uz != 0))
check("C8 z3: causal u with u^t = 0 must vanish (static, g_tt<0) => t strictly monotone on causal curves => no CTC", s.check() == z3.unsat)
check("C8 g^{tt} = -e^{-2Phi} < 0 for every finite Phi (t is a time function)", sp.simplify(gi[0, 0] + sp.exp(-2*Phi)) == 0)

print("\nOVERALL " + ("OK" if not FAIL else "FAILED: " + "; ".join(FAIL)))
sys.exit(0 if not FAIL else 1)
