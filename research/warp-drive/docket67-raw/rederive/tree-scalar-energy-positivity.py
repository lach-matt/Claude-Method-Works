#!/usr/bin/env python3
"""DOCKET 67 re-derivation: tree-scalar-energy-positivity (massform.py:393-411, 752-760, 1917-1964).

Checks, each from the ACTION by metric variation (Hilbert tensor), never by quoting a formula:

 C1  minimally coupled real scalar, L = -(1/2) g^mn d_m phi d_n phi - V(phi):
     T_00 = (1/2) phi_t^2 + (1/2)|grad phi|^2 + V            [the tree's decomposition]
 C2  Mexican hat V = -(mu^2/2) phi^2 + (lam/4) phi^4, mu^2 = lam v^2, V(0) = 0:
     V(v(1-eps)) - V(v) = rho_EW eps^2 (2-eps)^2,  rho_EW = lam v^4/4 = |V(v)|   [excite.FIELD_POLY]
 C3  H-REAL: SU(2)xU(1) Yang-Mills-Higgs, generic (metric-independent) F^a_mn and D_m Phi:
     T_00 = (1/2) sum_a (|E^a|^2 + |B^a|^2) + sum_m |D_m Phi|^2 + V,  and
     V - V_min = lam (Phi^+ Phi - v^2/2)^2 >= 0 for lam > 0  (z3, all real doublets)
 C4  vacuity guards: a ghost sign on the gauge kinetic term, or lam < 0, breaks positivity (witnesses).
 C5  NON-MINIMAL COUPLING, the hypothesis the tree's theorem does not name:
     L += -(1/2) xi R phi^2  gives, in FLAT space, T_00 += -xi Lap(phi^2)  (derived from sqrt(-g) R);
     a static witness with T_00 - V(v) < 0 pointwise at xi = 1/6; its integral over a period equals
     the xi = 0 integral (a spatial divergence), so the INTEGRATED energy statement survives.
 C6  data: rho_EW at the tree's G_F and at m_H = 125.20 GeV (PDG 2024 as printed in 2401.08811),
     and the sign of every conclusion against m_H.
Exit 0 iff every check comes out as stated.
"""
import sys
import itertools
import sympy as sp

ok_all = True


def check(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("%-4s %s %s" % ("PASS" if cond else "FAIL", name, detail))


# ------------------------------------------------------------------ C1 + C5 via lapse perturbation
t, x, y, z, eps, xi = sp.symbols("t x y z epsilon xi", real=True)
X = (t, x, y, z)
phi = sp.Function("phi")(*X)
f = sp.Function("f")(*X)
Vf = sp.Function("V")
N = 1 + eps * f
g = sp.diag(-N**2, 1, 1, 1)          # g_00 = -N^2 ; g^00 = -1/N^2 = -1 + 2 eps f + O(eps^2)
ginv = g.inv()
sqrtg = N                               # sqrt(-det g)


def ricci_scalar(g, ginv, X):
    n = 4
    Gam = [[[sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                            + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                            for a in range(n))
    return sp.simplify(sum(ginv[b, c] * Ric[b, c] for b in range(n) for c in range(n)))


R = ricci_scalar(g, ginv, X)
kin = sum(ginv[m, n] * sp.diff(phi, X[m]) * sp.diff(phi, X[n]) for m in range(4) for n in range(4))
Lden = sqrtg * (-sp.Rational(1, 2) * kin - Vf(phi) - sp.Rational(1, 2) * xi * R * phi**2)
L1 = sp.expand(sp.diff(Lden, eps).subs(eps, 0))   # linear in f and its derivatives
# Euler operator w.r.t. f (up to second derivatives)
E = sp.diff(L1, f)
for a in range(4):
    E -= sp.diff(sp.diff(L1, sp.diff(f, X[a])), X[a])
for a in range(4):
    for b in range(a, 4):
        d2 = sp.diff(f, X[a], X[b])
        E += sp.diff(sp.diff(L1, d2), X[a], X[b])
# delta g^00 = 2 eps f  =>  dS/dg^00 = E/2 ; T_00 = -2/sqrt(-g) dS/dg^00 = -E at flat
T00 = sp.simplify(sp.expand(-E))
grad2 = sum(sp.diff(phi, X[i])**2 for i in (1, 2, 3))
lap_phi2 = sum(sp.diff(phi**2, X[i], 2) for i in (1, 2, 3))
want_min = sp.Rational(1, 2) * sp.diff(phi, t)**2 + sp.Rational(1, 2) * grad2 + Vf(phi)
check("C1 minimal scalar: Hilbert T_00 = phi_t^2/2 + |grad phi|^2/2 + V",
      sp.simplify(sp.expand(T00.subs(xi, 0) - want_min)) == 0)
check("C5a nonminimal: flat-space Hilbert T_00 = [C1] - xi Lap(phi^2)",
      sp.simplify(sp.expand(T00 - want_min + xi * lap_phi2)) == 0)

# ------------------------------------------------------------------ C2 Mexican hat
lam, v, e = sp.symbols("lambda v e", positive=True)
ph = sp.symbols("ph", real=True)
Vh = -lam * v**2 / 2 * ph**2 + lam / 4 * ph**4
rho = lam * v**4 / 4
check("C2a V(v) = -rho_EW (V(0)=0), so rho_EW = |V_min|", sp.simplify(Vh.subs(ph, v) + rho) == 0)
check("C2b V(v(1-eps)) - V(v) = rho_EW eps^2 (2-eps)^2",
      sp.expand(Vh.subs(ph, v * (1 - e)) - Vh.subs(ph, v) - rho * e**2 * (2 - e)**2) == 0)
check("C2c zero set of eps^2(2-eps)^2 is {0, 2} (|phi| = v)",
      set(sp.solve(sp.Symbol("q")**2 * (2 - sp.Symbol("q"))**2, sp.Symbol("q"))) == {0, 2})

# ------------------------------------------------------------------ C3 H-REAL, SU(2)xU(1) + doublet
# Inverse metric G^{mn} = eta + s * delta^{m0} delta^{n0}; F_{mn}, D_m Phi carry lower indices only
# and are metric-independent (F^a = dA^a + g f^{abc} A^b A^c; D = d - i g A.T - i g' Y B), so the
# couplings drop out of the variation.
s = sp.symbols("s")
eta = sp.diag(-1, 1, 1, 1)
G = eta + sp.Matrix(4, 4, lambda m, n: s if (m == 0 and n == 0) else 0)
gl = G.inv()
Fs = {}
for a in range(4):                       # 3 SU(2) + 1 U(1)
    for m, n in itertools.combinations(range(4), 2):
        Fs[(a, m, n)] = sp.Symbol("F%d_%d%d" % (a, m, n), real=True)


def F(a, m, n):
    if m == n:
        return 0
    return Fs[(a, m, n)] if m < n else -Fs[(a, n, m)]


P = [[sp.Symbol("p%d_%d" % (m, k), real=True) + sp.I * sp.Symbol("q%d_%d" % (m, k), real=True)
      for k in range(2)] for m in range(4)]
h = [sp.Symbol("h%d" % k, real=True) for k in range(4)]   # doublet components (real, imag, real, imag)
PhiPhi = sum(c**2 for c in h)
Vd = lam * (PhiPhi - v**2 / 2)**2 - lam * v**4 / 4


def lagr(G, ghost_gauge=False):
    sg = -1 if ghost_gauge else 1
    LF = -sp.Rational(1, 4) * sg * sum(G[m, al] * G[n, be] * F(a, m, n) * F(a, al, be)
                                       for a in range(4) for m in range(4) for n in range(4)
                                       for al in range(4) for be in range(4))
    LD = -sum(G[m, n] * sp.re(sp.expand(sp.conjugate(P[m][k]) * P[n][k]))
              for m in range(4) for n in range(4) for k in range(2))
    return LF + LD - Vd


def t00(ghost_gauge=False):
    L = lagr(G, ghost_gauge)
    dL = sp.diff(L, s).subs(s, 0)
    L0 = L.subs(s, 0)
    return sp.expand(-2 * dL + gl[0, 0].subs(s, 0) * L0)   # T_00 = -2 dL/dg^00 + g_00 L


T00g = t00()
Esq = sum(F(a, 0, i)**2 for a in range(4) for i in (1, 2, 3))
Bsq = sum(F(a, i, j)**2 for a in range(4) for i, j in ((1, 2), (1, 3), (2, 3)))
Dsq = sum(sp.expand(sp.conjugate(P[m][k]) * P[m][k]) for m in range(4) for k in range(2))
want = sp.expand(sp.Rational(1, 2) * (Esq + Bsq) + Dsq + Vd)
check("C3a SU(2)xU(1)+doublet Hilbert T_00 = (E^2+B^2)/2 + sum_m |D_m Phi|^2 + V",
      sp.simplify(T00g - want) == 0)

try:
    import z3
    hz = [z3.Real("h%d" % k) for k in range(4)]
    lz, vz = z3.Real("lam"), z3.Real("v")
    pp = sum(c * c for c in hz)
    Vz = lz * (pp - vz * vz / 2) * (pp - vz * vz / 2) - lz * vz**4 / 4
    sol = z3.Solver()
    sol.add(lz > 0, Vz < -lz * vz**4 / 4)            # any doublet below V_min?
    r = sol.check()
    check("C3b z3: no real doublet has V < V_min when lam > 0", r == z3.unsat, str(r))
    sol2 = z3.Solver()
    sol2.add(lz < 0, Vz < -lz * vz**4 / 4)
    r2 = sol2.check()
    check("C4b vacuity guard (z3): lam < 0 admits V < V_min", r2 == z3.sat, str(r2))
except ImportError:
    check("C3b z3 not available", False)

# ghost-sign vacuity guard on the gauge kinetic term: exhibit a negative T_00 - V
T00ghost = t00(ghost_gauge=True)
sub = {sym: 0 for sym in T00ghost.free_symbols}
sub[Fs[(0, 0, 1)]] = 1
sub.update({lam: 1, v: 1, h[0]: sp.sqrt(sp.Rational(1, 2))})
val = (T00ghost - Vd).subs(sub)
check("C4a vacuity guard: ghost-sign gauge term gives T_00 - V < 0", val < 0, "value %s" % val)

# ------------------------------------------------------------------ C5b witness, xi = 1/6
xx = sp.symbols("xx", real=True)
a_, k_ = sp.Rational(1, 10), 1
lamv, vv = 1, 1
phis = vv + a_ * sp.cos(k_ * xx)
Vs = lambda p: -sp.Rational(lamv * vv**2, 2) * p**2 + sp.Rational(lamv, 4) * p**4
dens = lambda X_: (sp.Rational(1, 2) * sp.diff(phis, xx)**2 + Vs(phis) - Vs(vv)
                   - X_ * sp.diff(phis**2, xx, 2))
w = dens(sp.Rational(1, 6)).subs(xx, sp.pi)
check("C5b static witness at xi=1/6, phi = v + a cos kx, x = pi/k: T_00 - V(v) < 0",
      w < 0, "value %s = %.6f (v=lam=k=1, a=1/10)" % (sp.nsimplify(w), float(w)))
w0 = dens(0).subs(xx, sp.pi)
check("C5c same point at xi=0 is >= 0 (the tree's theorem)", w0 >= 0, "value %.6f" % float(w0))
I1 = sp.integrate(dens(sp.Rational(1, 6)), (xx, 0, 2 * sp.pi))
I0 = sp.integrate(dens(0), (xx, 0, 2 * sp.pi))
check("C5d integral over a period: xi=1/6 equals xi=0, and is > 0",
      sp.simplify(I1 - I0) == 0 and I0 > 0, "I = %.6f" % float(I0))

# ------------------------------------------------------------------ C6 data
import math
GF = 1.1663788e-5          # GeV^-2, the tree's G_FERMI (PDG value; unchanged in PDG 2024)
vev = 1 / math.sqrt(math.sqrt(2) * GF)
for mh, tag in ((125.20, "PDG 2024 as printed in 2401.08811 p.(table)"), (125.25, "PDG 2023"),
                (125.15, "1307.3536 Table 3 input")):
    lam_ = mh**2 / (2 * vev**2)
    rho_ = lam_ * vev**4 / 4
    print("DATA m_H=%.2f (%s): v=%.4f GeV lambda=%.5f rho_EW=%.5e GeV^4" % (mh, tag, vev, lam_, rho_))
check("C6 sign: rho_EW > 0 for every m_H^2 > 0 (positivity does not move with m_H)",
      sp.simplify(sp.Symbol("m", positive=True)**2 * v**2 / 8) .is_positive)

print("ALL PASS" if ok_all else "SOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
