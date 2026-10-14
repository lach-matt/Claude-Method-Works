#!/usr/bin/env python3
"""DOCKET 67 re-derivation: schwarzschild-radius  (r_s = 2GM/c^2).

Independent of research/warp-drive: imports nothing from it, reads nothing
from it.  Exit 0 iff every check comes out as recorded.

  R1  General static spherical metric, vacuum Einstein equations solved from
      scratch (sympy dsolve):  e^{2a} = e^{-2b} = 1 - C/r  under asymptotic
      flatness.  C is a free integration constant.
  R2  Newtonian identification, three independent ways, all C = 2GM/c^2:
      (i) slow-particle radial acceleration  -c^2 Gamma^r_tt -> -GM/r^2;
      (ii) circular geodesics: Omega^2 = C c^2/(2 r^3) EXACTLY, so Kepler III
           with GM fixes C, and C/r = 2 v^2/c^2 (the 'alpha/r ~ 2 v^2' form);
      (iii) Misner-Sharp mass of the solution = C/2 (geometric units).
  R3  Horizon: g_tt = 0 = g^rr at r = C; r is the AREAL radius (2 pi r =
      proper circumference), not a proper radial distance.
  R4  Kerr-Newman family: outer horizon r_+ and its areal radius
      sqrt(r_+^2 + a^2) are both <= 2GM/c^2, equality iff a = Q = 0; at fixed
      a/M, Q/M the horizon scales linearly in M (the proportionality survives
      the dropped 'static, uncharged' hypothesis, the coefficient does not).
  R5  Numerics at the three payload masses with CODATA 2018 = 2022 G and exact
      c; the document's printed figures; which rounding rule they follow.
  R6  Data sensitivity: G +- 1 sigma and the CODATA 2014 value.
  R7  Regime of the 100 kg hole: M/M_P, r_s/l_P, Hawking lifetime against the
      light-crossing time (the quasi-static hypothesis), curvature energy scale.
"""
import math, sys
import sympy as sp

OK = True
def chk(label, cond, detail=""):
    global OK
    OK &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label + (("  ->  " + str(detail)) if detail != "" else ""))

# ------------------------------------------------------------------ geometry
t, r, th, ph = sp.symbols("t r theta phi", positive=True)
X = [t, r, th, ph]
a = sp.Function("a")(r)
b = sp.Function("b")(r)

def christoffel(g):
    gi = g.inv()
    return [[[sp.simplify(sum(gi[i, d] * (sp.diff(g[d, j], X[k]) + sp.diff(g[d, k], X[j])
              - sp.diff(g[j, k], X[d])) for d in range(4)) / 2) for k in range(4)]
              for j in range(4)] for i in range(4)], gi

def einstein(g):
    Gam, gi = christoffel(g)
    Ric = sp.zeros(4, 4)
    for j in range(4):
        for k in range(4):
            s = 0
            for i in range(4):
                s += sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                for d in range(4):
                    s += Gam[i][i][d] * Gam[d][j][k] - Gam[i][k][d] * Gam[d][j][i]
            Ric[j, k] = sp.simplify(s)
    R = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    return (Ric - R * g / 2).applyfunc(sp.simplify), Gam

print("R1  vacuum solution of the general static spherical metric")
g = sp.diag(-sp.exp(2 * a), sp.exp(2 * b), r ** 2, r ** 2 * sp.sin(th) ** 2)
G, _ = einstein(g)
# G^t_t = 0 involves b only: e^{-2b}(1 - 2 r b') = 1 ... solve for B = e^{-2b}
B = sp.Function("B")(r)
Gtt_mixed = sp.simplify(G[0, 0] / (-sp.exp(2 * a)))           # G^t_t up to sign
eqB = sp.simplify(Gtt_mixed.subs(b, -sp.log(B) / 2).doit())
solB = sp.dsolve(sp.Eq(sp.numer(sp.together(eqB)), 0), B)
C = sp.symbols("C", real=True)
Bsol = sp.simplify(solB.rhs.subs(list(solB.rhs.free_symbols - {r})[0], -C))
chk("G^t_t = 0 gives e^{-2b} = 1 - C/r (C free)", sp.simplify(Bsol - (1 - C / r)) == 0, Bsol)
# G_rr - (g_rr/(-g_tt)) G_tt = 0 gives a' + b' = 0 ; with a,b -> 0 at infinity, a = -b
comb = sp.simplify(G[1, 1] + sp.exp(2 * b - 2 * a) * G[0, 0])
chk("G_rr + (g_rr/g_tt)(-G_tt) is proportional to a' + b'",
    sp.simplify(comb / (sp.diff(a, r) + sp.diff(b, r))).free_symbols <= {r}, sp.factor(comb))
gS = sp.diag(-(1 - C / r), 1 / (1 - C / r), r ** 2, r ** 2 * sp.sin(th) ** 2)
GS, GamS = einstein(gS)
chk("Schwarzschild form is vacuum for every real C", all(sp.simplify(e) == 0 for e in GS), "G_ab = 0")

print("R2  identification of C with the mass")
Gc, M_, c_ = sp.symbols("G M c", positive=True)
# (i) slow particle: d^2 r/dt^2 = -c^2 Gamma^r_{tt} with x^0 = c t
acc = -c_ ** 2 * GamS[1][0][0]
lead = sp.limit(acc * r ** 2, r, sp.oo)
chk("(i) far-field radial acceleration = -(C c^2/2)/r^2", sp.simplify(lead + C * c_ ** 2 / 2) == 0, lead)
Csol_i = sp.solve(sp.Eq(lead, -Gc * M_), C)[0]
chk("(i) matching Newton -GM/r^2 gives C = 2GM/c^2", sp.simplify(Csol_i - 2 * Gc * M_ / c_ ** 2) == 0, Csol_i)
# (ii) circular geodesic: Omega^2 = (dphi/dt)^2 from Gamma^r_tt c^2 + Gamma^r_phph Omega^2 = 0 at theta = pi/2
Om2 = sp.symbols("Omega2", positive=True)
eq = sp.Eq(GamS[1][0][0] * c_ ** 2 + GamS[1][3][3].subs(th, sp.pi / 2) * Om2, 0)
Om2sol = sp.simplify(sp.solve(eq, Om2)[0])
chk("(ii) circular orbits: Omega^2 = C c^2/(2 r^3) exactly (all r > 3C/2 stable or not)",
    sp.simplify(Om2sol - C * c_ ** 2 / (2 * r ** 3)) == 0, Om2sol)
chk("(ii) Kepler III (Omega^2 = GM/r^3) forces C = 2GM/c^2",
    sp.simplify(sp.solve(sp.Eq(Om2sol, Gc * M_ / r ** 3), C)[0] - 2 * Gc * M_ / c_ ** 2) == 0)
v2 = Om2sol * r ** 2
chk("(ii) C/r = 2 v^2/c^2 with v = Omega r (the source's 'alpha/r ~ 2 v^2')",
    sp.simplify(C / r - 2 * v2 / c_ ** 2) == 0)
# (iii) Misner-Sharp: m = (r/2)(1 - g^{rr}) ; g^rr = 1 - C/r
mMS = sp.simplify(r / 2 * (1 - (1 - C / r)))
chk("(iii) Misner-Sharp mass = C/2 (so C = 2 G M/c^2 in SI)", sp.simplify(mMS - C / 2) == 0, mMS)

print("R3  horizon and the meaning of 'radius'")
chk("g_tt = 0 and g^rr = 0 at r = C only", sp.solve(sp.Eq(1 - C / r, 0), r) == [C])
circ = sp.integrate(sp.sqrt(gS[3, 3].subs(th, sp.pi / 2)), (ph, 0, 2 * sp.pi))
chk("proper circumference at coordinate r is 2 pi r (areal radius)", sp.simplify(circ - 2 * sp.pi * r) == 0, circ)
Cn = sp.Rational(1)
prop = sp.integrate(1 / sp.sqrt(1 - Cn / r), (r, Cn, 2 * Cn))
chk("proper radial distance r_s -> 2 r_s is not r_s (= %.6f r_s)" % float(prop), abs(float(prop) - 1) > 0.1, float(prop))

print("R4  Kerr-Newman: dropping 'non-rotating, uncharged'")
m, aa, q = sp.symbols("m a q", nonnegative=True)   # geometric: m = GM/c^2, a = J/(Mc), q = r_Q
rp = m + sp.sqrt(m ** 2 - aa ** 2 - q ** 2)
import random
random.seed(67)
okKN = True
for _ in range(2000):
    mv = 1.0
    av = random.random(); qv = random.random() * math.sqrt(max(0.0, 1 - av * av))
    rpv = mv + math.sqrt(max(0.0, mv * mv - av * av - qv * qv))
    areal = math.sqrt(rpv * rpv + av * av)
    okKN &= (rpv <= 2 * mv + 1e-15) and (areal <= 2 * mv + 1e-15)
chk("r_+ <= 2m and sqrt(r_+^2 + a^2) <= 2m on 2000 random sub-extremal (a,q)", okKN)
# exact: areal^2 = 2 m r_+ - q^2 <= 4 m^2
areal2 = sp.expand(rp ** 2 + aa ** 2)
chk("identity r_+^2 + a^2 = 2 m r_+ - q^2", sp.simplify(areal2 - (2 * m * rp - q ** 2)) == 0)
lam = sp.symbols("lambda", positive=True)
chk("homogeneous degree 1: r_+(lam m, lam a, lam q) = lam r_+",
    sp.simplify(rp.subs({m: lam * m, aa: lam * aa, q: lam * q}, simultaneous=True) - lam * rp) == 0)

print("R5  numerics")
c = 299792458.0                 # exact (SI 2019); CODATA 2022 Table XXXII
G22 = 6.67430e-11               # CODATA 2018 = CODATA 2022, u_r = 2.2e-5
sG = 0.00015e-11
G14 = 6.67408e-11               # CODATA 2014, as quoted in IAU 2015 Res. B3
hbar = 1.054571817e-34
kB = 1.380649e-23
rs = lambda M, GG=G22, cc=c: 2 * GG * M / cc ** 2
printed_rs = {100.0: 1.48e-25, 5000.0: 7.42e-24, 1.0e5: 1.48e-22}
printed_E = {100.0: 8.98e18, 5000.0: 4.49e20}
for M, pv in printed_rs.items():
    v = rs(M)
    print("    M = %-8g kg   r_s = %.6e m   printed %.2e   rel diff %+.4e" % (M, v, pv, pv / v - 1))
chk("tree's '1.485e-25 m at 100 kg' is r_s(100 kg) to 4 s.f.", "%.3e" % rs(100.0) == "1.485e-25", "%.6e" % rs(100.0))
chk("all three printed r_s lie within the tree's 5e-3 tolerance",
    all(abs(pv / rs(M) - 1) < 5e-3 for M, pv in printed_rs.items()),
    [round(pv / rs(M) - 1, 5) for M, pv in printed_rs.items()])
rnd = lambda x: float("%.2e" % x)
trunc = lambda x: math.floor(x / 10 ** math.floor(math.log10(x)) * 100) / 100 * 10 ** math.floor(math.log10(x))
chk("DISCREPANCY: 3-s.f. ROUNDING of r_s gives 1.49e-25, 7.43e-24, 1.49e-22 (not the printed values)",
    [rnd(rs(M)) for M in printed_rs] == [1.49e-25, 7.43e-24, 1.49e-22], [rnd(rs(M)) for M in printed_rs])
chk("printed r_s AND printed E = M c^2 are all 3-s.f. TRUNCATIONS with exact c",
    all(math.isclose(trunc(rs(M)), pv, rel_tol=1e-9) for M, pv in printed_rs.items())
    and all(math.isclose(trunc(M * c * c), pv, rel_tol=1e-9) for M, pv in printed_E.items()))
alt = [rnd(2 * 6.674e-11 * M / 9e16) for M in printed_rs]
chk("(alternative: G = 6.674e-11, c = 3e8, rounding also reproduces the printed r_s)",
    alt == [1.48e-25, 7.42e-24, 1.48e-22], alt)
chk("  ...but c = 3e8 gives E(100 kg) = 9.00e18, not the printed 8.98e18: not one convention",
    rnd(100 * 9e16) == 9.0e18)
chk("the 1e5 kg E cell: truncation of M c^2 = 8.98e21, printed 8.98e22 (mantissa right, exponent slipped)",
    math.isclose(trunc(1e5 * c * c), 8.98e21, rel_tol=1e-9))

print("R6  data sensitivity")
for lab, GG in (("G - 1 sigma", G22 - sG), ("G + 1 sigma", G22 + sG), ("CODATA 2014", G14)):
    print("    %-12s r_s(100 kg) = %.6e  shift %+.2e" % (lab, rs(100.0, GG), rs(100.0, GG) / rs(100.0) - 1))
chk("G moves (+-1 sigma, 2014 value) shift r_s by < 5e-5 relative, 100x inside the 5e-3 tolerance",
    all(abs(rs(100.0, GG) / rs(100.0) - 1) < 5e-5 for GG in (G22 - sG, G22 + sG, G14)))
chk("printed-vs-computed verdict unchanged under every G move",
    all(all(abs(pv / rs(M, GG) - 1) < 5e-3 for M, pv in printed_rs.items()) for GG in (G22 - sG, G22 + sG, G14)))

print("R7  regime of a 100 kg Schwarzschild hole")
MP = math.sqrt(hbar * c / G22); lP = math.sqrt(hbar * G22 / c ** 3)
tau = lambda M: 5120 * math.pi * G22 ** 2 * M ** 3 / (hbar * c ** 4)
TH = lambda M: hbar * c ** 3 / (8 * math.pi * G22 * M * kB)
for M in printed_rs:
    print("    M = %-8g  M/M_P = %.3e  r_s/l_P = %.3e  (l_P/r_s)^2 = %.2e  tau_evap = %.3e s  r_s/c = %.3e s  ratio = %.2e  T_H = %.2e K  hbar c/r_s = %.2e GeV"
          % (M, M / MP, rs(M) / lP, (lP / rs(M)) ** 2, tau(M), rs(M) / c, tau(M) / (rs(M) / c), TH(M),
             hbar * c / rs(M) / 1.602176634e-10))
chk("100 kg: r_s is ~1e10 Planck lengths (classical GR corrections ~(l_P/r_s)^2 ~ 1e-20)",
    1e9 < rs(100.0) / lP < 1e11)
chk("100 kg: evaporation time (photon/graviton-only formula) >> light-crossing time (quasi-static holds)",
    tau(100.0) / (rs(100.0) / c) > 1e15)
chk("100 kg: lifetime (5120 pi G^2 M^3/(hbar c^4)) is ~8e-11 s -- the hole is NOT static on laboratory time scales",
    1e-11 < tau(100.0) < 1e-10, "%.3e s" % tau(100.0))

print("\nALL AS RECORDED" if OK else "\nSOMETHING DIFFERS")
sys.exit(0 if OK else 1)
