#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Friedmann equations for k = -1 dust, as used by
nonstatic.py:455-467 (open_dust_nec) and nonstatic.py:99-101, 661-666.

Independent of the tree: the Einstein tensor is computed here from the metric with this
file's own Christoffel/Ricci code (G = c = 1), not imported from nonstatic.py.  At the end
the tree's own open_dust_nec() is called read-only and compared.

Checks
  C1  open FRW Einstein tensor -> rho = 3(adot^2-1)/(8 pi a^2), p = -(2 a addot + adot^2 - 1)/(8 pi a^2)
  C2  dust (p = 0) + Lambda = 0  =>  a(adot^2 - 1) is conserved (= C) and C = 8 pi rho a^3/3,
      and addot = -C/(2 a^2): the two relations the tree substitutes (nonstatic.py:460-462)
  C3  radial null contraction T_ab k^a k^b (k = e0 + e1) = rho + p = (adot^2 - 1 - a addot)/(4 pi a^2);
      for dust this is rho = 3C/(8 pi a^3)
  C4  WITH Lambda: the null contraction is Lambda-independent (still rho_m), but the
      tree's identity 'NEC - rho = 0' with rho read off G_tt fails by -Lambda/(8 pi)
  C5  exact parametric solution a = (C/2)(cosh eta - 1), t = (C/2)(sinh eta - eta) satisfies
      adot^2 = C/a + 1 -- the witness exists for every C > 0 (Friedmann 1924 open case)
  C6  numeric: integrate adot = sqrt(C/a + 1) and compare with the parametric solution;
      evaluate NEC along it
  C7  z3: for all reals a > 0, C > 0: the substituted NEC numerator 3C/(2a) > 0 (negation unsat);
      and for C <= 0 the strict positivity fails (sat) -- C > 0 is load-bearing
  C8  the tree's own open_dust_nec() (read-only import) agrees
"""
import sys, os
import sympy as sp

ok = True
def chk(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print("  %-72s %-10s %s" % (name, str(got)[:10], "ok" if good else "FAIL"))

t, chi, th, ph = sp.symbols("t chi theta phi", positive=True)
a = sp.Function("a", positive=True)(t)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
x = [t, chi, th, ph]
g = sp.diag(-1, a**2, a**2 * sp.sinh(chi)**2, a**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
gi = g.inv()

def einstein(g, gi, x):
    n = 4
    Gam = [[[sum(gi[i, l] * (sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j]) - sp.diff(g[j, k], x[l]))
                 for l in range(n)) / 2 for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for j in range(n):
        for k in range(n):
            s = 0
            for i in range(n):
                s += sp.diff(Gam[i][j][k], x[i]) - sp.diff(Gam[i][j][i], x[k])
                for l in range(n):
                    s += Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i]
            Ric[j, k] = sp.simplify(s)
    R = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return sp.simplify(Ric - R * g / 2)

print("C1  Einstein tensor of open (k=-1) FRW, computed here")
G = einstein(g, gi, x)
rho = sp.simplify(G[0, 0] / (8 * sp.pi))
p = sp.simplify(G[1, 1] / a**2 / (8 * sp.pi))
pT = sp.simplify(G[2, 2] / (a**2 * sp.sinh(chi)**2) / (8 * sp.pi))
chk("rho == 3(adot^2 - 1)/(8 pi a^2)", sp.simplify(rho - 3 * (ad**2 - 1) / (8 * sp.pi * a**2)), 0)
chk("p   == -(2 a addot + adot^2 - 1)/(8 pi a^2)", sp.simplify(p + (2 * a * add + ad**2 - 1) / (8 * sp.pi * a**2)), 0)
chk("isotropic: p_T == p_r", sp.simplify(pT - p), 0)
chk("G_t chi == 0 (no flux, comoving)", sp.simplify(G[0, 1]), 0)

print("C2  dust + Lambda = 0: the first integral and the acceleration equation")
Cq = a * (ad**2 - 1)
dC = sp.simplify(sp.diff(Cq, t) - ad * (-8 * sp.pi * a**2 * p))   # dC/dt = -8 pi a^2 adot p
chk("d/dt[a(adot^2-1)] == -8 pi a^2 adot p  (so == 0 iff p = 0 or adot = 0)", dC, 0)
Cs = sp.Symbol("C", positive=True)
chk("C == 8 pi rho a^3/3", sp.simplify(Cq - 8 * sp.pi * rho * a**3 / 3), 0)
# p = 0 solved for addot, with adot^2 = C/a + 1
addot_dust = sp.solve(sp.Eq(p, 0), add)[0].subs(ad**2, Cs / a + 1)
addot_dust = sp.simplify(addot_dust.subs(ad, sp.sqrt(Cs / a + 1)))
chk("p = 0 & adot^2 = C/a + 1  =>  addot == -C/(2 a^2)", sp.simplify(addot_dust + Cs / (2 * a**2)), 0)

print("C3  the NEC contraction along k = e0 + e1 (orthonormal)")
nec = sp.simplify(rho + p)
chk("rho + p == (adot^2 - 1 - a addot)/(4 pi a^2)", sp.simplify(nec - (ad**2 - 1 - a * add) / (4 * sp.pi * a**2)), 0)
sub = lambda e: sp.simplify(e.subs(add, -Cs / (2 * a**2)).subs(ad**2, Cs / a + 1))
nec_d, rho_d = sub(nec), sub(rho)
chk("dust: NEC == rho", sp.simplify(nec_d - rho_d), 0)
chk("dust: rho == 3C/(8 pi a^3)", sp.simplify(rho_d - 3 * Cs / (8 * sp.pi * a**3)), 0)

print("C4  with a cosmological constant Lambda (dust + Lambda)")
L = sp.Symbol("Lambda", real=True)
# Friedmann with Lambda: adot^2 = C/a + L a^2/3 + 1 ; addot = -C/(2a^2) + L a/3
subL = lambda e: sp.simplify(e.subs(add, -Cs / (2 * a**2) + L * a / 3).subs(ad**2, Cs / a + L * a**2 / 3 + 1))
chk("  consistency: p_total(G) == -Lambda/(8 pi) (dust + Lambda)", sp.simplify(subL(p) + L / (8 * sp.pi)), 0)
chk("  NEC contraction (adot^2-1-a addot)/(4pi a^2) == 3C/(8 pi a^3) (Lambda-free)",
    sp.simplify(subL(nec) - 3 * Cs / (8 * sp.pi * a**3)), 0)
chk("  tree identity NEC - rho(G_tt) == -Lambda/(8 pi), not 0", sp.simplify(subL(nec) - subL(rho) + L / (8 * sp.pi)), 0)

print("C5  exact parametric open-dust solution")
eta = sp.Symbol("eta", positive=True)
A = Cs / 2 * (sp.cosh(eta) - 1)
T = Cs / 2 * (sp.sinh(eta) - eta)
adot_param = sp.diff(A, eta) / sp.diff(T, eta)
chk("(dA/dt)^2 - C/A - 1 == 0", sp.simplify((adot_param**2 - Cs / A - 1).rewrite(sp.exp)), 0)
addot_param = sp.diff(adot_param, eta) / sp.diff(T, eta)
chk("d2A/dt2 + C/(2A^2) == 0", sp.simplify((addot_param + Cs / (2 * A**2)).rewrite(sp.exp)), 0)

print("C6  numeric integration vs parametric (C = 1)")
import math
def rk4(f, y, h, n):
    for _ in range(n):
        k1 = f(y); k2 = f(y + h * k1 / 2); k3 = f(y + h * k2 / 2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y
C = 1.0
e0, e1 = 1.0, 3.0
a0 = C / 2 * (math.cosh(e0) - 1); t0 = C / 2 * (math.sinh(e0) - e0)
a1 = C / 2 * (math.cosh(e1) - 1); t1 = C / 2 * (math.sinh(e1) - e1)
N = 20000
aN = rk4(lambda y: math.sqrt(C / y + 1), a0, (t1 - t0) / N, N)
chk("|a_numeric - a_param| < 1e-10 at eta = 3", abs(aN - a1) < 1e-10, True)
print("       a_numeric = %.12f  a_param = %.12f" % (aN, a1))
adn = math.sqrt(C / a1 + 1); addn = -C / (2 * a1**2)
necn = (adn**2 - 1 - a1 * addn) / (4 * math.pi * a1**2)
rhon = 3 * C / (8 * math.pi * a1**3)
chk("NEC == rho numerically at eta = 3 (rel 1e-12)", abs(necn - rhon) / rhon < 1e-12, True)
print("       NEC = rho = %.12e" % rhon)

print("C7  z3 over the reals")
try:
    import z3
    av, Cv = z3.Reals("a C")
    s = z3.Solver()
    num = (Cv / av + 1) - 1 - av * (-Cv / (2 * av * av))
    s.add(av > 0, Cv > 0, z3.Not(num > 0))
    chk("for all a>0, C>0: adot^2-1-a addot > 0  (negation unsat)", str(s.check()), "unsat")
    s2 = z3.Solver(); s2.add(av > 0, Cv > 0, num * 2 * av != 3 * Cv)
    chk("for all a>0, C>0: numerator == 3C/(2a)  (negation unsat)", str(s2.check()), "unsat")
    s3 = z3.Solver(); s3.add(av > 0, Cv <= 0, z3.Not(num > 0))
    chk("C <= 0 admits NEC numerator <= 0  (sat: C > 0 is load-bearing)", str(s3.check()), "sat")
except ImportError:
    print("  z3 not installed -- C7 skipped (pip install z3-solver)")
    ok = False

print("C9  scope: the open-dust solution is past-singular (the witness exists on t in (0, inf))")
rho_eta = sp.simplify(3 * Cs / (8 * sp.pi * A**3))
chk("t(eta -> 0+) == 0", sp.limit(T, eta, 0, "+"), 0)
chk("a(eta -> 0+) == 0", sp.limit(A, eta, 0, "+"), 0)
chk("rho(eta -> 0+) == oo  (Ricci scalar R = 8 pi rho for dust -> oo)", sp.limit(rho_eta, eta, 0, "+"), sp.oo)
Rs_dust = sp.simplify(sub(-sp.Rational(1) * 8 * sp.pi * (-(rho) + 3 * p)))   # R = -8 pi T = 8 pi (rho - 3p)
chk("Ricci scalar of open dust == 8 pi rho", sp.simplify(Rs_dust - 8 * sp.pi * rho_d), 0)
chk("adot > 0 for all eta > 0 (expands forever; no recollapse)",
    sp.simplify(adot_param - sp.sinh(eta) / (sp.cosh(eta) - 1)) == 0 and True, True)

print("C10 NEC for EVERY null direction, perfect fluid (not only radial, not only comoving k)")
# orthonormal comoving frame; general null k = w(1, n1, n2, n3), |n| = 1, any boost of the frame
w, n1, n2, n3 = sp.symbols("w n1 n2 n3", real=True)
rr, pp = sp.symbols("rho p", real=True)
eta_m = sp.diag(-1, 1, 1, 1)
Tfl = sp.diag(rr, pp, pp, pp)                           # T_ab in the fluid's orthonormal frame
kv = sp.Matrix([w, w * n1, w * n2, w * n3])
Tkk = sp.expand((kv.T * Tfl * kv)[0])
Tkk_null = sp.simplify(Tkk.subs(n3**2, 1 - n1**2 - n2**2))
chk("T_ab k^a k^b == (rho + p) w^2 for any null k (w = -u.k)", sp.simplify(Tkk_null - (rr + pp) * w**2), 0)
print("       so for dust, T_ab k^a k^b = rho (u.k)^2 > 0 for every null k and in every slicing")

print("C8  the tree's own open_dust_nec(), imported read-only")
tree = os.environ.get("WARP", "/home/user/Claude-Method-Works/research/warp-drive")
sys.path.insert(0, tree)
try:
    import nonstatic
    r, n_, d = nonstatic.open_dust_nec()
    Ct = sp.Symbol("C", positive=True)
    at = sp.Function("a", positive=True)(sp.Symbol("t", positive=True))
    chk("tree NEC - rho == 0", sp.simplify(d), 0)
    chk("tree rho == 3C/(8 pi a^3)", sp.simplify(r - 3 * Ct / (8 * sp.pi * at**3)), 0)
    print("       tree: rho = %s   NEC = %s" % (r, n_))
except Exception as e:
    print("  could not import tree: %r" % (e,))
    ok = False

print("\nRESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
