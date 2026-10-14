"""DOCKET 67 audit: energy-conditions-definitions.
Re-derives, independently of certify.py's finite-difference pipeline:
 (A) the logical relations among the pointwise ECs as published (Curiel 1405.0403 s2.1,
     Martin-Moruno & Visser 1702.05915 s2), machine-checked with z3 over type-I stress tensors;
 (B) the SEC contraction w + T/2 for unit timelike V (sympy);
 (C) exact (sympy) orthonormal rho, p_r, p_t for certify.py's conformastatic metric, and the
     signs/values of the table in certify.py:76-82 and the r=1 / m<0 figures.
Read-only with respect to the repository: it imports nothing from research/.
"""
import math, sys
import sympy as sp
import z3

ok = True
def rep(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-70s %s %s" % (label, "ok" if cond else "FAIL", detail))

print("(A) z3: implications among type-I effective forms (Martin-Moruno & Visser table, Curiel s2.1)")
rho, p1, p2, p3 = z3.Reals("rho p1 p2 p3")
P = [p1, p2, p3]
NEC = z3.And(*[rho + p >= 0 for p in P])
WEC = z3.And(rho >= 0, NEC)
SEC = z3.And(NEC, rho + p1 + p2 + p3 >= 0)
DEC = z3.And(rho >= 0, *[z3.And(p <= rho, -p <= rho) for p in P])
FEC = z3.And(*[rho*rho >= p*p for p in P])    # flux condition alone (MM&V eq 4.3, type I)
def valid(f):
    s = z3.Solver(); s.add(z3.Not(f)); return s.check() == z3.unsat
def cex(f):
    s = z3.Solver(); s.add(z3.Not(f)); r = s.check()
    return None if r == z3.unsat else s.model()
rep("DEC => WEC  (the tree's 'the DEC requires the WEC')", valid(z3.Implies(DEC, WEC)))
rep("WEC => NEC", valid(z3.Implies(WEC, NEC)))
rep("SEC => NEC", valid(z3.Implies(SEC, NEC)))
m = cex(z3.Implies(SEC, WEC)); rep("SEC does NOT imply WEC (counterexample exists)", m is not None, str(m))
m = cex(z3.Implies(WEC, DEC)); rep("WEC does NOT imply DEC: dec_holds(wec>=0) is necessary, not sufficient", m is not None, str(m))
m = cex(z3.Implies(FEC, WEC)); rep("flux-only 'DEC' (FEC) does NOT imply WEC", m is not None, str(m))
rep("not WEC => not DEC (the only direction certify.py uses)", valid(z3.Implies(z3.Not(WEC), z3.Not(DEC))))

print("\n(A') covariant check: DEC (H-E: T(V,V)>=0 and flux causal) => WEC, over a boosted type-I T, sampled")
# covariant definition, numerically, over random type-I tensors: DEC_cov true => WEC_cov true
import random
random.seed(67)
def boost_obs(s, u):
    g = 1/math.sqrt(1-s*s); return (g, g*s*u[0], g*s*u[1], g*s*u[2])
ETA = (-1, 1, 1, 1)
bad = 0; nDEC = 0
for trial in range(4000):
    r_ = random.uniform(-1, 1); ps = [random.uniform(-1.5, 1.5) for _ in range(3)]
    T = [[0]*4 for _ in range(4)]; T[0][0] = r_
    for i in range(3): T[i+1][i+1] = ps[i]
    dec_c = True; wec_c = True
    for _ in range(60):
        v = [random.gauss(0,1) for _ in range(3)]; n = math.sqrt(sum(x*x for x in v)); u = [x/n for x in v]
        V = boost_obs(random.uniform(0, 0.99), u)
        w = sum(T[a][b]*V[a]*V[b] for a in range(4) for b in range(4))
        F = [-sum(ETA[a]*T[a][b]*V[b] for b in range(4)) for a in range(4)]  # F^a = -T^a_b V^b
        FF = sum(ETA[a]*F[a]*F[a] for a in range(4))
        if w < 0: wec_c = False
        if w < 0 or FF > 1e-12 or F[0] < -1e-12: dec_c = False
    if dec_c:
        nDEC += 1
        if not wec_c: bad += 1
rep("covariant DEC-true samples that fail WEC", bad == 0, "(%d DEC-true of 4000, %d bad)" % (nDEC, bad))

print("\n(B) sympy: SEC contraction for unit timelike V equals w + T/2")
s_, th = sp.symbols("s th", real=True)
Tm = sp.Matrix(4, 4, lambda i, j: sp.Symbol("T%d%d" % (min(i,j), max(i,j)), real=True))
eta = sp.diag(-1, 1, 1, 1)
gam = 1/sp.sqrt(1 - s_**2)
V = sp.Matrix([gam, gam*s_*sp.cos(th), gam*s_*sp.sin(th), 0])
rep("V.V = -1", sp.simplify((V.T*eta*V)[0]) == -1)
trace = sum(eta[i, i]*Tm[i, i] for i in range(4))
lhs = ((Tm - sp.Rational(1, 2)*trace*eta).applyfunc(lambda x: x))
sec = sp.simplify((V.T*lhs*V)[0] - ((V.T*Tm*V)[0] + trace/2))
rep("(T_ab - T g_ab/2) V^a V^b - (w + T/2) == 0  (certify.py:351)", sec == 0)

print("\n(C) sympy: exact Einstein tensor of g = diag(-e^{2F}, e^{-2F}(dr^2 + r^2 dOmega^2))")
t, r, th2, ph = sp.symbols("t r theta phi", positive=True)
F = sp.Function("F")(r)
X = [t, r, th2, ph]
g = sp.diag(-sp.exp(2*F), sp.exp(-2*F), sp.exp(-2*F)*r**2, sp.exp(-2*F)*r**2*sp.sin(th2)**2)
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
         for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(4))
                           for a in range(4)))
R = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs = sp.simplify(sum(gi[a, b]*R[a, b] for a in range(4) for b in range(4)))
G = sp.simplify(R - Rs*g/2)
rho_e = sp.simplify(G[0, 0]/(-g[0, 0]))
pr_e = sp.simplify(G[1, 1]/g[1, 1])
pt_e = sp.simplify(G[2, 2]/g[2, 2])
off = [sp.simplify(G[i, j]) for i in range(4) for j in range(4) if i != j]
rep("Einstein tensor diagonal in the static orthonormal frame (type I)", all(o == 0 for o in off))
Fp, Fpp = sp.diff(F, r), sp.diff(F, r, 2)
lapl = Fpp + 2*Fp/r
rho_claim = sp.exp(2*F)*(2*lapl - Fp**2)
print("     rho   =", sp.simplify(rho_e))
print("     p_r   =", sp.simplify(pr_e))
print("     p_t   =", sp.simplify(pt_e))
rep("rho == e^{2F}(2 lap F - |grad F|^2)", sp.simplify(rho_e - rho_claim) == 0)

# closed-form sign identities (type I, radial/tangential principal pressures)
rep("rho + p_r == 2 e^{2F}(lap F - F'^2)", sp.simplify(rho_e + pr_e - 2*sp.exp(2*F)*(lapl - Fp**2)) == 0)
rep("rho + p_t == 2 e^{2F} lap F", sp.simplify(rho_e + pt_e - 2*sp.exp(2*F)*lapl) == 0)
rep("rho + p_r + 2 p_t (SEC) == 2 e^{2F} lap F", sp.simplify(rho_e + pr_e + 2*pt_e - 2*sp.exp(2*F)*lapl) == 0)
mm, aa, rr = sp.symbols("m a r", positive=True)
Pl = mm/sp.sqrt(rr**2 + aa**2)
lapPl = sp.simplify(sp.diff(Pl, rr, 2) + 2*sp.diff(Pl, rr)/rr)
rep("lap(m/sqrt(r^2+a^2)) == -3 m a^2/(r^2+a^2)^(5/2) < 0 for m>0: NEC(radial), NEC(tangential), SEC, WEC fail for ALL 0<r<R_s",
    sp.simplify(lapPl + 3*mm*aa**2/(rr**2 + aa**2)**sp.Rational(5, 2)) == 0)

m_, a_, Rsh = sp.Rational(2, 100), sp.Rational(2, 100), 200
Phi = m_/sp.sqrt(r**2 + a_**2) - m_/Rsh      # r < R_s branch of certify.py:204
subsd = lambda e, PhiExpr: e.subs(sp.Derivative(F, (r, 2)), sp.diff(PhiExpr, r, 2)).subs(
    sp.Derivative(F, r), sp.diff(PhiExpr, r)).subs(F, PhiExpr)
rho_f = sp.lambdify(r, subsd(rho_e, Phi), "mpmath")
pr_f = sp.lambdify(r, subsd(pr_e, Phi), "mpmath")
pt_f = sp.lambdify(r, subsd(pt_e, Phi), "mpmath")
import mpmath as mp
mp.mp.dps = 30

def dirs(n=200):
    out = []
    for i in range(n):
        z = 1 - 2*(i + 0.5)/n; rr = math.sqrt(max(0, 1 - z*z)); tt = math.pi*(1 + 5**0.5)*i
        out.append((rr*math.cos(tt), rr*math.sin(tt), z))
    return out
D = dirs()
def ec(rho, pr, pt):
    # radial direction = x-axis (certify samples the point (r,0,0))
    nec = wec = sec = float("inf"); tr = -rho + pr + 2*pt
    for u in D:
        pu = pr*u[0]**2 + pt*(u[1]**2 + u[2]**2)
        nec = min(nec, rho + pu)
        for j in range(1, 11):
            s = j/11; g2 = 1/(1 - s*s); w = g2*(rho + s*s*pu)
            wec = min(wec, w); sec = min(sec, w + tr/2)
    return nec, wec, sec

table = {0.005: (-9.0616e+04, -9.1505e+04, -5.2635e+05, -4.8059e+05),
         0.02: (-1.2190e+04, -1.3451e+04, -7.6240e+04, -6.9503e+04),
         0.05: (-3.0887e+02, -3.9339e+02, -2.1822e+03, -1.9847e+03),
         0.2: (-4.7451e-01, -7.6490e-01, -4.1169e+00, -3.7316e+00),
         1: (-4.6564e-04, -8.7348e-04, -4.6251e-03, -4.1844e-03),
         10: (-4.0744e-08, -8.0044e-08, -4.2191e-07, -3.8135e-07)}
print("\n     r        rho(exact)     rho+p_r      rho+p_t     NECmin      WECmin(s<=10/11)  SECmin     | table T_00  ratio")
for rv, tb in table.items():
    rho = float(rho_f(rv)); pr = float(pr_f(rv)); pt = float(pt_f(rv))
    nec, wec, sec = ec(rho, pr, pt)
    ph = float(Phi.subs(r, rv))
    print("     %-7g %12.5e %12.5e %12.5e %12.5e %12.5e %12.5e | %11.4e %7.4f  e^{-2Phi}=%.4f" %
          (rv, rho, rho+pr, rho+pt, nec, wec, sec, tb[0], tb[0]/rho, math.exp(-2*ph)))
    rep("  r=%g: rho<0, NEC, WEC, SEC all negative (exact)" % rv, rho < 0 and nec < 0 and wec < 0 and sec < 0)
    rep("  r=%g: table NEC/WEC/SEC reproduced to 0.5%%" % rv,
        all(abs(x - y) <= 5e-3*abs(y) for x, y in zip((nec, wec, sec), tb[1:])),
        "(%.4e %.4e %.4e)" % (nec, wec, sec))
    rep("  r=%g: table T_00 equals exact orthonormal rho to 0.5%%" % rv, abs(tb[0]-rho) <= 5e-3*abs(rho),
        "table/rho=%.4f" % (tb[0]/rho))

rho1 = float(rho_f(1.0))
# DISCREPANCY (recorded, not repaired): certify.py:92-93 prose and selftest :459 quote T_00(r=1) = -4.8455e-4.
# That is the COORDINATE component e^{2Phi} rho; the orthonormal rho is -4.6564e-4 (= the table at :80).
# The selftest passes only because near() uses tol*max(1,|want|) = 1e-3 ABSOLUTE for |want| < 1.
e2p1 = math.exp(2*float(Phi.subs(r, 1)))
rep("DISCREPANCY: orthonormal rho(r=1) != -4.8455e-4 (differs by >1%)", abs(rho1 + 4.8455e-4) > 1e-2*4.8455e-4, "%.6e" % rho1)
rep("  -4.8455e-4 is the coordinate T_00 = e^{2Phi} rho", abs(rho1*e2p1 + 4.8455e-4) < 1e-3*4.8455e-4, "%.6e" % (rho1*e2p1))
rep("  near() tolerance at |want|=4.8e-4 is 1e-3 absolute (check is vacuous)", abs(rho1 + 4.8455e-4) <= 1e-3*max(1.0, 4.8455e-4))
dphi = float(sp.diff(Phi, r).subs(r, 1))
rep("r=1 -|grad Phi|^2 == -3.9952e-4", abs(-dphi**2 + 3.9952e-4) < 1e-3*3.9952e-4, "%.6e ratio %.4f" % (-dphi**2, rho1/(-dphi**2)))
rep("  ratio 1.21 (certify.py:94) is coordinate/|grad|^2; orthonormal ratio is 1.1655", abs(rho1*e2p1/(-dphi**2) - 1.2128) < 1e-3 and abs(rho1/(-dphi**2) - 1.1655) < 1e-3,
    "coord %.4f orth %.4f" % (rho1*e2p1/(-dphi**2), rho1/(-dphi**2)))
Phin = -Phi
rho_n = float(subsd(rho_e, Phin).subs(r, sp.Rational(5, 100)).evalf(20))
e2 = math.exp(2*float(Phin.subs(r, 0.05)))
rep("m<0, r=0.05: orthonormal rho == +30.9245", abs(rho_n - 30.9245) < 1e-3*30.9245, "%.5f" % rho_n)
rep("m<0, r=0.05: coordinate T_00 = e^{2Phi} rho == 14.7", abs(rho_n*e2 - 14.716) < 1e-2, "%.4f" % (rho_n*e2))

print("\n(D) WEC infimum vs sampled minimum: with rho+p<0 the WEC infimum over all observers is -inf")
rho, pr, pt = float(rho_f(1.0)), float(pr_f(1.0)), float(pt_f(1.0))
for s in (10/11, 0.99, 0.999999):
    print("     s=%-10g gamma^2(rho+s^2 p_min) = %.4e" % (s, (rho + s*s*min(pr, pt))/(1-s*s)))
rep("static observer (s=0) alone already fails WEC at every table radius", all(float(rho_f(x)) < 0 for x in table))

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
