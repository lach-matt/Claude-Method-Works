#!/usr/bin/env python3
"""
DOCKET 67 -- audit of 'dominant-energy-condition' (DEC) as the warp board uses it.

Owners: research/warp-drive/axial.py (scan admissibility test, lines 74-91,190,197,216-220,443-449)
        research/warp-drive/concentric.py (DEC as hypothesis of PMT rigidity, lines 51-53,122-138,365)

Checks (every one computed here; nothing declared):
  A  z3:    Hawking-Ellis DEC (T(t,t) >= 0 and flux -T.t causal, all timelike t) on a
            type-I tensor diag(rho,p1,p2,p3)  <=>  rho >= |p_i|  (the form 2105.03079 eq 5.9
            prints; the covariant form 2505.02210 Sec II.A prints).  Both directions.
  B  sympy: static cylindrical metric of axial.py: T^a_b is diagonal (type I at every point,
            so the DEC is exactly u >= |p_r|,|p_z|,|p_phi|); axial.py's identity
            8 pi u W = -(W Psi')' - W Psi'^2 - W''  (Lambda = 0) and Phi absent from u.
  C  numeric: consequence for the scans -- under axial.py's two boundary conditions
            INT 8 pi u W = -INT W Psi'^2, so u >= 0 everywhere forces u == 0 and Psi' == 0:
            no non-vacuum DEC matter exists in the class at all, contracting or not.
            Shown on profiles: with Psi' == 0 and W != r, u changes sign; with Psi' != 0, u < 0 somewhere.
            And: Minkowski (u = 0, p = 0) satisfies the DEC but fails axial.py's strict 'u > 0' test.
  D  sympy: concentric.py -- the Plummer core of mass -m has rho < 0 everywhere (so the
            DEC fails directly, rigidity not needed); the linearised metric has p_i = O(eps^2);
            time-symmetric Hamiltonian constraint R_g = 16 pi mu, so rigidity needs mu >= 0
            only, which the DEC implies (DEC is the stronger hypothesis; conclusion weaker).
"""
import sys, math
import sympy as sp
import z3

FAIL = []
def chk(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAIL.append(label)

# ---------------------------------------------------------------- A: DEC <=> rho >= |p_i|
print("A. DEC on a type-I tensor, both directions (z3)")
rho, p1, p2, p3, t0, t1, t2, t3 = z3.Reals("rho p1 p2 p3 t0 t1 t2 t3")
P = [p1, p2, p3]; T = [t1, t2, t3]
timelike_future = z3.And(t0 > 0, -t0 * t0 + t1 * t1 + t2 * t2 + t3 * t3 < 0)
energy = rho * t0 * t0 + p1 * t1 * t1 + p2 * t2 * t2 + p3 * t3 * t3        # T_ab t^a t^b
# F^a = -T^a_b t^b = (rho t0, -p_i t_i) in an orthonormal frame, signature (-+++)
flux_norm = -(rho * t0) ** 2 + sum((P[i] * T[i]) ** 2 for i in range(3))   # g(F,F)
flux_future = rho * t0 >= 0
dec_at_t = z3.And(energy >= 0, flux_norm <= 0)                             # 2505.02210 form
typeI = z3.And(*[z3.And(rho >= P[i], rho >= -P[i]) for i in range(3)])

s = z3.Solver()
s.add(typeI, timelike_future, z3.Not(z3.And(dec_at_t, flux_future)))
r = s.check()
chk("A1 rho >= |p_i|  =>  DEC at every future timelike t  (negation %s)" % r, r == z3.unsat)

# converse, by explicit witnesses: rho < 0 -> t=(1,0,0,0); 0 <= rho < |p1| -> t=(1,s,0,0),
# s^2 = ((rho/p1)^2 + 1)/2, which is < 1 (timelike) and > (rho/p1)^2 (flux spacelike)
s = z3.Solver()
ss = z3.Real("ss")                                                          # ss = s^2
s.add(rho >= 0, z3.Or(rho < p1, rho < -p1), p1 != 0,
      ss * p1 * p1 * 2 == rho * rho + p1 * p1)
s.add(z3.Not(z3.And(ss < 1, ss >= 0, -(rho) ** 2 + p1 * p1 * ss > 0)))
r = s.check()
chk("A2 0 <= rho < |p1|  =>  witness t=(1,s,0,0) timelike with spacelike flux  (negation %s)" % r,
    r == z3.unsat)
s = z3.Solver(); s.add(rho < 0, z3.Not(rho * 1 * 1 < 0)); r = s.check()
chk("A3 rho < 0  =>  t=(1,0,0,0) gives T(t,t) = rho < 0  (negation %s)" % r, r == z3.unsat)
# the covariant 'flux causal' clause alone already forces future-directedness when energy >= 0
s = z3.Solver()
s.add(timelike_future, energy >= 0, flux_norm <= 0, z3.Not(z3.Or(rho * t0 > 0,
      z3.And(rho == 0, *[P[i] * T[i] == 0 for i in range(3)]))))
r = s.check()
chk("A4 energy >= 0 & flux causal  =>  flux future-directed or zero  (negation %s)" % r, r == z3.unsat)
# DEC => WEC energy part rho >= 0 ; strict 'u > 0' is NOT implied by DEC (u = p = 0 satisfies it)
s = z3.Solver(); s.add(typeI, rho < 0); r = s.check()
chk("A5 DEC (type-I form) => rho >= 0  (negation %s)" % r, r == z3.unsat)
s = z3.Solver(); s.add(typeI, z3.Not(rho > 0)); r = s.check()
chk("A6 DEC does NOT imply rho > 0 strictly (sat: %s, e.g. vacuum)" % r, r == z3.sat)

# ---------------------------------------------------------------- B: axial.py's metric
print("\nB. static cylindrical metric (sympy)")
t, rr, z, ph = sp.symbols("t r z phi")
Phi, Lam, Psi, W = [sp.Function(n)(rr) for n in ("Phi", "Lambda", "Psi", "W")]
X = [t, rr, z, ph]
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), sp.exp(2 * Psi), W ** 2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
        - sp.diff(g[b, c], X[d])) for d in range(n)) / 2) for c in range(n)] for b in range(n)]
       for a in range(n)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                 for d in range(n)) for a in range(n)))
R_ = sp.Matrix(n, n, lambda b, c: Ric(b, c))
Rs = sp.simplify(sum(gi[a, b] * R_[a, b] for a in range(n) for b in range(n)))
G = sp.simplify(R_ - Rs * g / 2)
Tmix = sp.simplify(gi * G / (8 * sp.pi))                   # T^a_b
offdiag = [Tmix[a, b] for a in range(n) for b in range(n) if a != b]
chk("B1 T^a_b diagonal (off-diagonal all 0): type I at every point", all(sp.simplify(e) == 0 for e in offdiag))
u = sp.simplify(-Tmix[0, 0]); pr = sp.simplify(Tmix[1, 1]); pz = sp.simplify(Tmix[2, 2]); pphi = sp.simplify(Tmix[3, 3])
chk("B2 u independent of Phi", not u.has(Phi))
u0 = sp.simplify(u.subs(Lam, 0).doit())
ident = sp.simplify(8 * sp.pi * u0 * W - (-sp.diff(W * sp.diff(Psi, rr), rr) - W * sp.diff(Psi, rr) ** 2 - sp.diff(W, rr, 2)))
chk("B3 axial.py identity 8 pi u W = -(W Psi')' - W Psi'^2 - W'' (Lambda=0), residual %s" % ident, ident == 0)
print("     u(Lambda=0) =", sp.simplify(u0))

# ---------------------------------------------------------------- C: what DEC can do in that class
print("\nC. under W(0)=0, W'(0)=1, W'->1, W Psi'->0: u >= 0 forces vacuum (numeric)")
psi0, a_, w0, c_ = sp.symbols("psi0 a w0 c", real=True)
Wp = rr + w0 * rr ** 3 * sp.exp(-(rr / c_) ** 2)
Psip = -psi0 * sp.exp(-(rr / a_) ** 2)
u_prof = u0.subs({W: Wp, Psi: Psip}).doit()  # unsimplified: simplify moves exp() into denominators and overflows
u_num = sp.lambdify((rr, psi0, a_, w0, c_), u_prof, "math")
W_num = sp.lambdify((rr, w0, c_), Wp, "math")
Psid_num = sp.lambdify((rr, psi0, a_), sp.diff(Psip, rr), "math")
def scan(pars, rmax=30.0, N=60001):
    h = rmax / (N - 1); us = []; I_u = 0.0; I_p = 0.0
    for k in range(N):
        x = k * h if k else 1e-9
        uu = u_num(x, *pars); us.append(uu)
        wgt = 1 if k in (0, N - 1) else (4 if k % 2 else 2)
        I_u += wgt * 8 * math.pi * uu * W_num(x, pars[2], pars[3])
        I_p += wgt * W_num(x, pars[2], pars[3]) * Psid_num(x, pars[0], pars[1]) ** 2
    return min(us), max(us), I_u * h / 3, -I_p * h / 3
cases = [((0.0, 1.0, 0.8, 1.4), "Psi'==0, W != r"),
         ((0.0, 1.0, -0.3, 0.9), "Psi'==0, W != r"),
         ((0.4, 1.0, 0.0, 1.0), "Psi'!=0, W = r"),
         ((1.3, 0.7, 0.8, 1.4), "Psi'!=0, W != r"),
         ((0.9, 1.7, -0.15, 2.5), "Psi'!=0, W != r")]
for pars, lab in cases:
    umin, umax, Iu, Ip = scan(pars)
    print("     %-18s pars=%s  min u=% .4e  max u=% .4e  INT8piuW=% .10f  -INT W Psi'^2=% .10f"
          % (lab, pars, umin, umax, Iu, Ip))
    chk("C  %s %s: identity holds (|diff| < 1e-8) and u < 0 somewhere (DEC fails)" % (lab, pars),
        abs(Iu - Ip) < 1e-8 and umin < 0)
chk("C  axial.py fixture (0.4,1,0,1) -> -0.0800000000 reproduced",
    abs(scan((0.4, 1.0, 0.0, 1.0))[2] + 0.08) < 1e-9)
chk("C  axial.py fixture (1.3,0.7,0.8,1.4) -> -1.0776404390 reproduced",
    abs(scan((1.3, 0.7, 0.8, 1.4))[2] + 1.0776404390) < 1e-8)
# Minkowski: u = 0, all p = 0 -> DEC holds, strict u > 0 fails
mink = {W: rr, Psi: sp.Integer(0), Phi: sp.Integer(0), Lam: sp.Integer(0)}
vals = [sp.simplify(e.subs(mink).doit()) for e in (u, pr, pz, pphi)]
chk("C  Minkowski gives u = p_r = p_z = p_phi = 0: DEC holds, 'u > 0' test fails %s" % vals,
    all(v == 0 for v in vals))

# ---------------------------------------------------------------- D: concentric.py
print("\nD. concentric.py core and the rigidity hypothesis (sympy)")
R, m, a = sp.symbols("R m a", positive=True)
Phic = m / sp.sqrt(R ** 2 + a ** 2)
rho_core = sp.simplify(sp.diff(R ** 2 * sp.diff(Phic, R), R) / R ** 2 / (4 * sp.pi))   # lap Phi = 4 pi rho
print("     rho_core(r) =", rho_core)
chk("D1 Plummer core of mass -m: rho = -3 m a^2 / (4 pi (r^2+a^2)^(5/2)) < 0 everywhere",
    sp.simplify(rho_core + 3 * m * a ** 2 / (4 * sp.pi * (R ** 2 + a ** 2) ** sp.Rational(5, 2))) == 0)
Mcore = sp.integrate(4 * sp.pi * R ** 2 * rho_core, (R, 0, sp.oo))
chk("D2 core integrates to mass -m (got %s)" % sp.simplify(Mcore), sp.simplify(Mcore + m) == 0)
# linearised metric -(1+2 eps f)dt^2 + (1-2 eps f) dx^2 : G_00 = 2 lap f + O(eps^2), G_ij = O(eps^2)
eps = sp.Symbol("eps"); x, y, zz = sp.symbols("x y zz")
f = sp.Function("f")(x, y, zz)
Y = [t, x, y, zz]
gl = sp.diag(-(1 + 2 * eps * f), 1 - 2 * eps * f, 1 - 2 * eps * f, 1 - 2 * eps * f)
gli = sp.diag(*[1 / gl[i, i] for i in range(4)])
Gl = [[[sum(gli[A, D] * (sp.diff(gl[D, B], Y[C]) + sp.diff(gl[D, C], Y[B]) - sp.diff(gl[B, C], Y[D]))
        for D in range(4)) / 2 for C in range(4)] for B in range(4)] for A in range(4)]
def Rl(B, C):
    return sum(sp.diff(Gl[A][B][C], Y[A]) - sp.diff(Gl[A][B][A], Y[C])
               + sum(Gl[A][A][D] * Gl[D][B][C] - Gl[A][C][D] * Gl[D][B][A] for D in range(4))
               for A in range(4))
RL = sp.Matrix(4, 4, lambda B, C: Rl(B, C))
RSl = sum(gli[A, A] * RL[A, A] for A in range(4))
GL = RL - RSl * gl / 2
lap = sum(sp.diff(f, v, 2) for v in (x, y, zz))
G00_1 = sp.simplify(sp.series(GL[0, 0], eps, 0, 2).removeO().coeff(eps, 1))
Gxx_1 = sp.simplify(sp.series(GL[1, 1], eps, 0, 2).removeO().coeff(eps, 1))
Gxy_1 = sp.simplify(sp.series(GL[1, 2], eps, 0, 2).removeO().coeff(eps, 1))
chk("D3 linearised: G_00 = 2 eps lap(f) + O(eps^2)", sp.simplify(G00_1 - 2 * lap) == 0)
chk("D4 linearised: G_xx, G_xy vanish at O(eps): pressures are O(eps^2), so the core is type I "
    "with |p| << |rho| and DEC fails through rho < 0 alone", Gxx_1 == 0 and Gxy_1 == 0)
# time-symmetric Hamiltonian constraint on a static slice: K_ij = 0, so G(n,n) = R_h/2 -> R_h = 16 pi mu.
# Computed on the general static spherical metric -e^{2Phi}dt^2 + dr^2/(1-2M/r) + r^2 dOmega^2.
th = sp.Symbol("theta"); Ms = sp.Function("M")(rr); Ph2 = sp.Function("Phi")(rr)
Z = [t, rr, th, ph]
gs = sp.diag(-sp.exp(2 * Ph2), 1 / (1 - 2 * Ms / rr), rr ** 2, rr ** 2 * sp.sin(th) ** 2)
def ricci_scalar(gm, co):
    k = gm.shape[0]; gim = gm.inv()
    Gm = [[[sp.simplify(sum(gim[A, D] * (sp.diff(gm[D, B], co[C]) + sp.diff(gm[D, C], co[B])
            - sp.diff(gm[B, C], co[D])) for D in range(k)) / 2) for C in range(k)] for B in range(k)]
          for A in range(k)]
    Rm = sp.Matrix(k, k, lambda B, C: sp.simplify(sum(sp.diff(Gm[A][B][C], co[A]) - sp.diff(Gm[A][B][A], co[C])
           + sum(Gm[A][A][D] * Gm[D][B][C] - Gm[A][C][D] * Gm[D][B][A] for D in range(k)) for A in range(k))))
    return Rm, sp.simplify(sum(gim[A, B] * Rm[A, B] for A in range(k) for B in range(k))), gim
Rm4, Rsc4, gis = ricci_scalar(gs, Z)
G4 = Rm4 - Rsc4 * gs / 2
mu = sp.simplify(-(gis * G4)[0, 0] / (8 * sp.pi))                 # mu = T(n,n) = -T^t_t
_, Rh, _ = ricci_scalar(gs[1:, 1:], Z[1:])
chk("D5 static slice: R_h - 16 pi mu = %s (Hamiltonian constraint with K = 0)" % sp.simplify(Rh - 16 * sp.pi * mu),
    sp.simplify(Rh - 16 * sp.pi * mu) == 0)
chk("D6 mu = M'/(4 pi r^2): mu >= 0 <=> R_h >= 0, the only local input time-symmetric rigidity uses; "
    "DEC => mu >= 0 by A5, so DEC is the stronger hypothesis and 'DEC fails' the weaker conclusion",
    sp.simplify(mu - sp.diff(Ms, rr) / (4 * sp.pi * rr ** 2)) == 0)

print("\n" + ("ALL CHECKS PASS" if not FAIL else "FAILURES: %d -> %s" % (len(FAIL), FAIL)))
sys.exit(1 if FAIL else 0)
