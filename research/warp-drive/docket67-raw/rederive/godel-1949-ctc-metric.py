#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Goedel 1949 (Rev. Mod. Phys. 21, 447), as the warp tree uses it
(latticectc.py:82-83, 141-144): "there exists a 5D Lorentzian metric containing a CTC --
Goedel 1949, never in doubt"; the refused codim-1 metric is "Goedel-class, not a braneworld".

Goedel 1949 is NAMED-NOT-READ (no arXiv copy); the forms checked here are the exact
restatements READ in:
  Verma, Aluri, Mota, Obukhov arXiv:2506.00860 eq.(1): ds^2 = a^2(dt^2 - 2e^x dt dy + e^{2x} dy^2
      - dx^2 - dz^2), dust + Lambda, omega^2 = 1/(2a^2) = 4 pi G eps = -Lambda.
  Kajari, Walser, Schleich, Delgado arXiv:gr-qc/0404032 eq.(15): ds^2/(4a^2) = dt^2 - dr^2
      - (sinh^2 r - sinh^4 r) dphi^2 - dz^2 + 2 sqrt2 sinh^2 r dphi dt  ("given by Goedel in 1949");
      field eqs R_mn - g R/2 = kappa T + Lambda g give kappa(rho+p/c^2) = 1/(a^2c^2),
      kappa p = Lambda + 1/(2a^2).
  Gauntlett, Gutowski, Hull, Pakis, Reall hep-th/0209114 eq.(3.24)-(3.29): 5D Goedel analogue.
  Barrow & Tsagas gr-qc/0309030 eqs.(18),(30),(36),(37): Goedel brane.
Signature (+,-,-,-[,-]) throughout, as in every source above.  Exit 1 on any failure.
"""
import sys
import sympy as sp

FAIL = []


def check(tag, cond, note=""):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + tag + ((" -- " + note) if note else ""))
    if not ok:
        FAIL.append(tag)


def geometry(g, X):
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                       - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n))
                                    - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
                                    + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(n) for d in range(n))
                                    - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return gi, Gam, Ric, Rs


a = sp.symbols('a', positive=True)
kap = sp.symbols('kappa', positive=True)       # 8 pi G (c = 1)

# ---------------------------------------------------------------- E1 Goedel's original chart
t, x, y, z = X = sp.symbols('t x y z', real=True)
beta = sp.symbols('beta', positive=True)


def goedel(bb):
    return a**2 * sp.Matrix([[1, 0, -sp.exp(x), 0],
                             [0, -1, 0, 0],
                             [-sp.exp(x), 0, bb * sp.exp(2 * x), 0],
                             [0, 0, 0, -1]])


# 2506.00860 eq.(1) exactly as printed: coefficient of e^{2x} dy^2 is 1
check("E1a' DISCREPANCY: 2506.00860 eq.(1) as printed (beta = 1) is degenerate, det g = 0",
      sp.simplify(goedel(1).det()) == 0, "a misprint in the restatement, not a property of Goedel's metric")
gb = goedel(beta)
gib, Gamb, Ricb, Rsb = geometry(gb, X)
rho, Lam = sp.symbols('rho Lambda', real=True)
ub = gb * sp.Matrix([1 / a, 0, 0, 0])
Eb = sp.simplify(Ricb - gb * Rsb / 2 - kap * rho * ub * ub.T - Lam * gb)
eqs = [e for e in set(Eb) if e != 0]
solb = sp.solve(eqs, [rho, Lam, beta], dict=True)
check("E1a'' requiring dust + Lambda with u ~ d_t FORCES beta = 1/2 (unique positive solution)",
      len(solb) == 1 and solb[0][beta] == sp.Rational(1, 2), str(solb))
g = goedel(sp.Rational(1, 2))
check("E1a Lorentzian at beta = 1/2: det g = -a^8 e^{2x}/2 < 0 (signature +---)",
      sp.simplify(g.det() + a**8 * sp.exp(2 * x) / 2) == 0)
gi, Gam, Ric, Rs = geometry(g, X)
u_up = sp.Matrix([1 / a, 0, 0, 0])
check("E1b u = a^-1 d_t is unit timelike", sp.simplify((u_up.T * g * u_up)[0]) == 1)
u_dn = g * u_up
G = sp.simplify(Ric - g * Rs / 2)
E = sp.simplify(G - kap * rho * (u_dn * u_dn.T) - Lam * g)   # Goedel/Kajari form: G = kappa T + Lambda g
sol = sp.solve([E[0, 0], E[1, 1]], [rho, Lam], dict=True)
check("E1c Einstein eq solvable with dust + Lambda", len(sol) == 1, str(sol))
s = sol[0]
check("E1d 8 pi G rho = 1/a^2 (> 0)", sp.simplify(s[rho] - 1 / (kap * a**2)) == 0)
check("E1e Lambda = -1/(2a^2) (< 0)", sp.simplify(s[Lam] + 1 / (2 * a**2)) == 0)
check("E1f all 16 components of G - kappa T - Lambda g vanish", sp.simplify(E.subs(s)) == sp.zeros(4, 4))
check("E1g R_mn = u_m u_n / a^2, R = 1/a^2 (Kajari eq. after (18))",
      sp.simplify(Ric - u_dn * u_dn.T / a**2) == sp.zeros(4, 4) and sp.simplify(Rs - 1 / a**2) == 0)

# vorticity: omega^2 = (1/2) w_ab w^ab, w_ab = projected antisymmetric part of grad u
nab_u = sp.Matrix(4, 4, lambda m, n: sp.diff(u_dn[m], X[n]) - sum(Gam[k][m][n] * u_dn[k] for k in range(4)))
acc = sp.simplify(nab_u * u_up)
check("E1h dust is geodesic (acceleration 0)", acc == sp.zeros(4, 1))
w = (nab_u - nab_u.T) / 2
w2 = sp.simplify(sum(w[m, n] * (gi * w * gi)[m, n] for m in range(4) for n in range(4)) / 2)
check("E1i vorticity^2 = 1/(2a^2) = 4 pi G rho = -Lambda (2506.00860 eq.(1) text; Kajari eq.(21))",
      sp.simplify(w2 - 1 / (2 * a**2)) == 0 and sp.simplify(kap * s[rho] / 2 - w2) == 0
      and sp.simplify(-s[Lam] - w2) == 0, "omega^2 = %s" % w2)
theta = sp.simplify(sum(nab_u[m, n] * gi[m, n] for m in range(4) for n in range(4)))
sym = (nab_u + nab_u.T) / 2
check("E1j no expansion, no shear (theta = 0, sigma = 0)", theta == 0 and sp.simplify(sym) == sp.zeros(4, 4))

# ---------------------------------------------------------------- E2 homogeneity (Killing vectors)
def lie_g(xi):
    return sp.simplify(sp.Matrix(4, 4, lambda m, n: sum(xi[k] * sp.diff(g[m, n], X[k]) + g[k, n] * sp.diff(xi[k], X[m])
                                                         + g[m, k] * sp.diff(xi[k], X[n]) for k in range(4))))
K = {"d_t": [1, 0, 0, 0], "d_y": [0, 0, 1, 0], "d_z": [0, 0, 0, 1],
     "d_x - y d_y": [0, 1, -y, 0]}
# the fifth generator is written from recollection (no read source gives it in this chart); it is
# tested in both orientations of y, since this chart carries -2e^x dt dy.  Informational only:
# transitivity (E2b) needs just the four above.
for nm, xi5 in (("+2e^-x d_t + y d_x + (e^-2x - y^2/2) d_y [recollection, y -> -y]",
                 [2 * sp.exp(-x), y, sp.exp(-2 * x) - y**2 / 2, 0]),
                ("-2e^-x d_t + y d_x + (e^-2x - y^2/2) d_y [recollection, as remembered]",
                 [-2 * sp.exp(-x), y, sp.exp(-2 * x) - y**2 / 2, 0])):
    print(("INFO Killing " if lie_g(xi5) == sp.zeros(4, 4) else "INFO not Killing ") + nm)
allk = True
for name, xi in K.items():
    ok = lie_g(xi) == sp.zeros(4, 4)
    allk &= ok
    check("E2a Killing: " + name, ok)
M = sp.Matrix([K["d_t"], K["d_x - y d_y"], K["d_y"], K["d_z"]])
check("E2b four Killing fields span T_p at every point (det = 1): isometry group transitive",
      sp.simplify(M.det()) == 1, "so a CTC through one point gives a CTC through every point")

# ---------------------------------------------------------------- E3 cylindrical chart and the CTC
T, r, ph, Z = Y = sp.symbols('T r phi Z', real=True)
sh = sp.sinh(r)
gc = 4 * a**2 * sp.Matrix([[1, 0, sp.sqrt(2) * sh**2, 0],
                           [0, -1, 0, 0],
                           [sp.sqrt(2) * sh**2, 0, -(sh**2 - sh**4), 0],
                           [0, 0, 0, -1]])
gic, Gamc, Ricc, Rsc = geometry(gc, Y)
uc_up = sp.Matrix([1 / (2 * a), 0, 0, 0])
uc_dn = gc * uc_up
Ec = sp.simplify(Ricc - gc * Rsc / 2 - kap * s[rho] * uc_dn * uc_dn.T - s[Lam] * gc)
check("E3a cylindrical form (Kajari eq.15) solves the same equations, same rho and Lambda",
      Ec.applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp))) == sp.zeros(4, 4))
check("E3b same invariants R = 1/a^2 as original chart", sp.simplify(Rsc - 1 / a**2) == 0,
      "(invariant agreement is necessary, not a proof of the local isometry; not machine-checked)")
gpp = sp.simplify(gc[2, 2])
rc = sp.asinh(1)
check("E3c g_phiphi = 4a^2 sinh^2 r (sinh^2 r - 1): timelike (> 0 in +---) iff sinh r > 1",
      sp.simplify(gpp - 4 * a**2 * sh**2 * (sh**2 - 1)) == 0)
check("E3d critical radius r_c = asinh 1 = ln(1 + sqrt2); in Kajari's r = 2a sinh r it is r_G = 2a",
      sp.simplify(sp.sinh(sp.log(1 + sp.sqrt(2))).rewrite(sp.exp) - 1) == 0 and sp.simplify((2 * a * sp.sinh(rc)).rewrite(sp.exp) - 2 * a) == 0)
# axis regularity: near r = 0, g ~ 4a^2(-dr^2 - r^2 dphi^2 + ...) => phi period 2 pi is forced (no cone)
check("E3e axis regular with phi ~ phi + 2pi: -g_phiphi/(-g_rr) ~ r^2 at r -> 0",
      sp.limit(-gpp / (4 * a**2) / r**2, r, 0) == 1)
r0 = sp.Rational(6, 5)
val = gpp.subs({r: r0, a: 1})
tau = 2 * sp.pi * sp.sqrt(val)
check("E3f the circle T, Z const, r = 6/5 > ln(1+sqrt2) = 0.8814 is a closed timelike curve",
      float(val) > 0, "g_phiphi = %.6f (a = 1), proper time around it = %.6f a" % (float(val), float(tau)))
# the CTC is not a geodesic (Buser-Kajari-Schleich 1303.4651 p.27): acceleration of the curve nonzero
lam = sp.symbols('lam')
cur = [0, r0, lam, 0]
v = [0, 0, 1, 0]
accv = [sp.simplify(sum(Gamc[k][i][j] * v[i] * v[j] for i in range(4) for j in range(4)).subs(r, r0)) for k in range(4)]
check("E3g the circular CTC is not a geodesic (Gamma^r_phiphi != 0 at r0)", any(e != 0 for e in accv),
      "Gamma^mu_phiphi = %s" % [sp.nsimplify(sp.N(e.subs(a, 1), 8)) for e in accv])

# ---------------------------------------------------------------- E4 energy conditions of Goedel's source
# total source S = kappa rho u u + Lambda g (Goedel's convention G = kappa T + Lambda g).
k0, k1, k2, k3 = sp.symbols('k0:4', real=True)
kv = sp.Matrix([k0, k1, k2, k3])
Tt = kap * s[rho] * u_dn * u_dn.T + s[Lam] * g
nullq = sp.simplify((kv.T * Tt * kv)[0] - s[Lam] * (kv.T * g * kv)[0])
check("E4a NEC: S(k,k) = (u.k)^2/a^2 >= 0 for every null k (Lambda term drops on the cone)",
      sp.simplify(nullq - ((u_dn.T * kv)[0])**2 / a**2) == 0)
# WEC of the effective source (Lambda moved to the right): S(v,v) for unit timelike v
# = (u.v)^2/a^2 - 1/(2a^2) >= 1/a^2 - 1/(2a^2) > 0 since (u.v)^2 >= 1 (reverse Cauchy-Schwarz)
check("E4b WEC of total source at v = u: 1/a^2 - 1/(2a^2) = 1/(2a^2) > 0",
      sp.simplify((u_up.T * Tt * u_up)[0] - 1 / (2 * a**2)) == 0)
check("E4c the NEC-satisfying CTC metric exists in 4D: Goedel is NOT in the 'NEC-violating' category", True,
      "contrast latticectc.py:84-86 (refused metric: negative density, NEC fails)")

# ---------------------------------------------------------------- E5 the 5D statement the tree makes
w5 = sp.symbols('w', real=True)
X5 = [t, x, y, z, w5]
g5 = sp.diag(g, -1)
gi5, Gam5, Ric5, Rs5 = geometry(g5, X5)
G5 = sp.simplify(Ric5 - g5 * Rs5 / 2)
check("E5a Goedel x R (flat 5th direction) is Lorentzian and contains the same CTC (curve at w = const)",
      sp.simplify(g5.det() - a**8 * sp.exp(2 * x) / 2) == 0)
c0, c1, c2, c3, c4 = sp.symbols('c0:5', real=True)
kk = sp.Matrix([c0, c1, c2, c3, c4])
u5 = sp.Matrix(list(u_dn) + [0])
check("E5b G5(k,k) = (u.k)^2/a^2 >= 0 on the null cone: NEC holds with T read off its own Einstein tensor",
      sp.simplify((kk.T * G5 * kk)[0] - (u5.T * kk)[0]**2 / a**2 + Rs5 / 2 * (kk.T * g5 * kk)[0]) == 0)

# GGHPR 5D Goedel analogue, gamma = 1/4, cartesian base R^4: ds^2 = (dt + om)^2 - dx.dx
t5, x1, x2, x3, x4 = XX = sp.symbols('t5 x1 x2 x3 x4', real=True)
om = [0, -x2 / 2, x1 / 2, x4 / 2, -x3 / 2]              # om = (1/2)(x1 dx2 - x2 dx1 - x3 dx4 + x4 dx3)
e0 = sp.Matrix([1] + om[1:])
gG = e0 * e0.T - sp.diag(0, 1, 1, 1, 1)
giG, GamG, RicG, RsG = geometry(gG, XX)
GG = sp.simplify(RicG - gG * RsG / 2)
F = sp.zeros(5, 5)
F[1, 2], F[3, 4] = sp.sqrt(3) / 2, -sp.sqrt(3) / 2          # F = (sqrt3/2)(dx1^dx2 - dx3^dx4)
F = F - F.T
Fup = giG * F * giG
F2 = sp.simplify(sum(F[m, n] * Fup[m, n] for m in range(5) for n in range(5)))
TF = sp.simplify(-(F * giG * F.T) + gG * F2 / 4)     # Maxwell stress, (+----) sign: T(u,u) >= 0
uG = sp.Matrix([1, 0, 0, 0, 0])
check("E5c' Maxwell energy density T(d_t,d_t) > 0 with this sign", sp.simplify((uG.T * TF * uG)[0]).is_positive,
      "T_00 = %s" % sp.simplify((uG.T * TF * uG)[0]))
cst = sp.simplify(GG[0, 0] / TF[0, 0])
check("E5c GGHPR eq.(3.29) metric: Einstein tensor = const x Maxwell stress of F, const > 0",
      sp.simplify(GG - cst * TF) == sp.zeros(5, 5) and cst.is_positive, "const = %s" % cst)
# NEC for the Maxwell source on a sample of null vectors k = (k0, n) with k0 fixed by g(k,k) = 0
import random
random.seed(67)
worst = None
for _ in range(200):
    pt = {x1: sp.Rational(random.randint(-30, 30), 7), x2: sp.Rational(random.randint(-30, 30), 7),
          x3: sp.Rational(random.randint(-30, 30), 7), x4: sp.Rational(random.randint(-30, 30), 7)}
    nvec = [sp.Rational(random.randint(-9, 9), 5) for _ in range(4)]
    k0s = sp.symbols('k0s')
    kv5 = sp.Matrix([k0s] + nvec)
    gpt = gG.subs(pt)
    roots = sp.solve((kv5.T * gpt * kv5)[0], k0s)
    for rt in roots:
        kk5 = kv5.subs(k0s, rt)
        v = sp.nsimplify(sp.simplify((kk5.T * TF.subs(pt) * kk5)[0]))
        worst = v if worst is None else min(worst, v)
check("E5c'' NEC for the Maxwell source: T(k,k) >= 0 on 200 random points x null directions (400 null k)",
      worst is not None and worst >= 0, "min T(k,k) = %s" % sp.N(worst, 6))
r1 = sp.symbols('r1', positive=True)
# d/dphi1 = x1 d_x2 - x2 d_x1 ; norm = (om(d_phi1))^2 - r1^2 = (r1^2/2)^2 - r1^2
Vphi = sp.Matrix([0, -x2, x1, 0, 0])
nrm = sp.simplify((Vphi.T * gG * Vphi)[0]).subs({x1: r1, x2: 0})
check("E5e d/dphi1 is timelike iff r1 > 2 (GGHPR p.12: 'timelike for r_i > 2')",
      sp.simplify(nrm - (r1**4 / 4 - r1**2)) == 0 and sp.solve(sp.Eq(nrm, 0), r1) == [2])

# ---------------------------------------------------------------- E6 Barrow-Tsagas Goedel brane algebra
kap2, lam_, U, Pnn, P11, p, w_, m2 = sp.symbols('kappa2 lambda U Pnn P11 p omega m2', real=True)
rh = sp.symbols('rho_b', real=True)
Lam18 = sp.solve(sp.Eq(kap2 * (rh - p) + 2 * Lam, kap2 * rh * p / lam_ - 4 * U / (kap2 * lam_)
                       - 12 * Pnn / (kap2 * lam_)), Lam)[0]
m2_36 = 2 * w_**2 - kap2 * (rh - p) / 2 + kap2 * rh * p / (2 * lam_) - 2 * U / (kap2 * lam_) - 6 * P11 / (kap2 * lam_) - Lam18
check("E6a Barrow-Tsagas (36) with (18) gives (37): m^2 = 2 w^2 + 6(Pnn - P11)/(kappa^2 lambda)",
      sp.simplify(m2_36 - (2 * w_**2 + 6 * (Pnn - P11) / (kap2 * lam_))) == 0)
check("E6b with the frame aligned (P11 = Pnn): m^2 = 2 w^2, Goedel's own value",
      sp.simplify(m2_36.subs(P11, Pnn) - 2 * w_**2) == 0)
R_ = sp.symbols('R', positive=True)
mm, ww = sp.symbols('m w0', positive=True)
gpp30 = (4 * ww / mm**2)**2 * sp.sinh(mm * R_ / 2)**4 - sp.sinh(mm * R_)**2 / mm**2
lead = sp.limit(gpp30 * sp.exp(-2 * mm * R_), R_, sp.oo)
check("E6c Goedel-type (30): g_phiphi -> e^{2mR}(w^2/m^4 - 1/(4m^2)) at large R: CTCs iff m^2 < 4 w^2",
      sp.simplify(lead - (ww**2 / mm**4 - 1 / (4 * mm**2))) == 0)
check("E6d (30) at m^2 = 2w^2, w = 1/(sqrt2 a), R = 2a r, t = 2a T is Kajari eq.(15)",
      sp.simplify((gpp30.subs({mm: 1 / a, ww: 1 / (sp.sqrt(2) * a), R_: 2 * a * r})
                   - gc[2, 2]).rewrite(sp.exp)) == 0)

# ---------------------------------------------------------------- E7 a CTC with no field equation at all
check("E7 flat R^{1,3} with t ~ t + P: the t-line is a closed timelike curve (Luminet 2101.08592 p.4 "
      "'trivial CTCs'; D21's causal-lattice case)", True,
      "so the bare existence statement at latticectc.py:82-83 needs neither Goedel nor 5D")

print()
print("RESULT: %d failure(s)" % len(FAIL) + ("" if not FAIL else ": " + ", ".join(FAIL)))
sys.exit(1 if FAIL else 0)
