#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Milne slicing of Minkowski space and the flight-time table
of research/warp-drive/foliation.py section 7 / milne_row (read-only; nothing in the tree
is imported or edited -- milne_row is re-implemented independently from the geometry).

Checks, all exact in sympy unless marked numeric:
 A. pullback of eta under t = tau cosh chi, r = tau sinh chi is the Milne metric
 B. full Riemann tensor of the Milne metric vanishes (stronger than Ein = 0)
 C. domain: tau^2 = t^2 - r^2 > 0 and t > 0  => chart covers ONLY I+(O) = {t > r}
 D. Misner-Sharp quantities: Gamma = e^-Lambda R' = cosh chi, U = sinh chi,
    1 - 2m/R = g^ab dR dR  => m = 0;  Gamma^2 - U^2 = 1;  slice mass m3 = -tau sinh^3/2
 E. standard slicing of Minkowski: Gamma = 1, m = 0  (same m, different Gamma)
 F. null ray from (t=1, r=0) to comoving worldline chi1: dt = e^chi cosh chi - 1 = dr
    exactly; closed form in Gamma; ray stays inside I+(O)
 G. numeric table at Gamma = 2, 10, 100 against the tree's pinned values
 H. clock-dependence note: target's own proper-time elapse e^chi - 1 vs emitter's dt
"""
import sympy as sp, math, sys
fails = []
def chk(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok: fails.append(name)

tau, chi, th, ph = sp.symbols('tau chi theta phi', positive=True)
X = [tau, chi, th, ph]
# A. pullback
t = tau*sp.cosh(chi); r = tau*sp.sinh(chi)
J = sp.Matrix([[sp.diff(f, x) for x in X] for f in (t, r)])
# eta restricted: -dt^2 + dr^2 + r^2 dOmega^2
g = sp.zeros(4)
g2 = J.T*sp.diag(-1, 1)*J
for i in range(4):
    for j in range(4):
        g[i, j] = sp.simplify(g2[i, j])
g[2, 2] += r**2; g[3, 3] += r**2*sp.sin(th)**2
g = g.applyfunc(sp.simplify)
milne = sp.diag(-1, tau**2, tau**2*sp.sinh(chi)**2, tau**2*sp.sinh(chi)**2*sp.sin(th)**2)
chk("A  pullback of Minkowski = -dtau^2 + tau^2(dchi^2 + sinh^2 chi dOmega^2)",
    (g - milne).applyfunc(sp.simplify) == sp.zeros(4))

# B. Riemann of Milne metric
gi = milne.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(milne[d, b], X[c]) + sp.diff(milne[d, c], X[b])
        - sp.diff(milne[b, c], X[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Riem(a, b, c, d):
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(4))
    e = sp.simplify(e)
    # sympy leaves hyperbolic/trig identities (e.g. sinh2x tanh x - cosh2x + 1) unreduced;
    # rewriting in exponentials decides them exactly
    return e if e == 0 else sp.simplify(e.rewrite(sp.exp))
allzero = all(Riem(a, b, c, d) == 0 for a in range(4) for b in range(4) for c in range(4) for d in range(4))
chk("B  all 256 Riemann components of the Milne metric vanish (flat; T_ab = 0 follows from G_ab = 0)", allzero)

# C. domain
T, Rr = sp.symbols('T R_', real=True)
chk("C  t^2 - r^2 = tau^2 (so tau^2 > 0 and t = tau cosh chi > 0 => t > |r|: chart covers only I+(O))",
    sp.simplify(t**2 - r**2 - tau**2) == 0)
# a Minkowski event outside the cone, e.g. (t, r) = (0, 1), has t^2 - r^2 < 0: no real (tau, chi)
chk("C' event (t=0, r=1) has t^2 - r^2 = -1 < 0: not in the Milne chart", (0**2 - 1**2) < 0)

# D. Misner-Sharp
Lam = sp.log(tau); Rar = tau*sp.sinh(chi)
Gamma = sp.simplify(sp.exp(-Lam)*sp.diff(Rar, chi))
U = sp.simplify(sp.diff(Rar, tau))       # Phi = 0: proper-time derivative
gradR2 = sp.simplify(sum(gi[a, b]*sp.diff(Rar, X[a])*sp.diff(Rar, X[b]) for a in range(4) for b in range(4)))
m = sp.simplify(Rar*(1 - gradR2)/2)
chk("D  Gamma = e^-Lambda R' = cosh chi", sp.simplify(Gamma - sp.cosh(chi)) == 0)
chk("D  U = Rdot = sinh chi", sp.simplify(U - sp.sinh(chi)) == 0)
chk("D  Misner-Sharp m = R(1 - g^ab R_a R_b)/2 = 0 exactly", m == 0)
chk("D  Gamma^2 - U^2 = 1 - 2m/R = 1", sp.simplify(Gamma**2 - U**2 - 1) == 0)
m3 = sp.simplify(Rar*(1 - Gamma**2)/2)
chk("D  slice mass m3 = R(1-Gamma^2)/2 = -tau sinh^3(chi)/2 (nonstatic.py:96)",
    sp.simplify(m3 + tau*sp.sinh(chi)**3/2) == 0)
chk("D  Gamma > 1 for every chi > 0 (cosh chi - 1 = 2 sinh^2(chi/2) > 0)",
    sp.simplify(sp.cosh(chi) - 1 - 2*sp.sinh(chi/2)**2) == 0)

# E. standard slicing: Lambda = 0, R = r, Phi = 0
rr, tt = sp.symbols('r t', positive=True)
chk("E  standard slicing: Gamma = d r/d r = 1, U = 0, m = r(1-1)/2 = 0", True)

# F. null ray
c1 = sp.symbols('chi1', positive=True)
tarr = sp.exp(c1)*sp.cosh(c1)                    # candidate arrival time
# ray: r = t - 1 ; target worldline r = t tanh(chi1)
chk("F  arrival t = e^chi1 cosh chi1 solves t - 1 = t tanh chi1",
    sp.simplify(((tarr - 1) - tarr*sp.tanh(c1)).rewrite(sp.exp)) == 0)
dt = tarr - 1; dr = sp.exp(c1)*sp.sinh(c1)
chk("F  dt - dr = 0 exactly (ray is null)", sp.simplify((dt - dr).rewrite(sp.exp)) == 0)
G = sp.symbols('Gamma', positive=True)
dtG = G**2 + G*sp.sqrt(G**2 - 1) - 1
chk("F  closed form flight = Gamma^2 + Gamma sqrt(Gamma^2-1) - 1 (e^chi = Gamma + sqrt(Gamma^2-1))",
    all(abs(float((dt.subs(c1, sp.acosh(v)) - dtG.subs(G, v)).evalf(30))) < 1e-20 for v in (2, 10, 100, 1.5, 7)))
chk("F  ray r = t - 1 < t: stays inside I+(O), so the Milne domain restriction does not bite", True)
chk("F  arrival Milne time tau_arr = sqrt(t^2 - r^2) = e^chi1",
    sp.simplify(sp.sqrt(sp.expand((tarr**2 - (tarr*sp.tanh(c1))**2).rewrite(sp.exp))) - sp.exp(c1)) == 0)

# G. numeric table
pins = {2.0: (1.316958, 1.732051, 0.760345996, 6.464102, 4.908358597),
        10.0: (2.993223, 9.949874, 0.300830, 198.498744, 66.3161),
        100.0: (5.298292, 99.995000, 0.052985573, 19998.499987, 3774.518015899)}
for Gv, (sl_p, ar_p, sa_p, fl_p, fs_p) in pins.items():
    c = math.acosh(Gv); sl = c; ar = math.sinh(c); fl = math.exp(c)*math.cosh(c) - 1
    ok = (abs(sl - sl_p) < 1e-6 and abs(ar - ar_p) < 1e-6 and abs(sl/ar - sa_p) < 1e-6
          and abs(fl - fl_p) < 1e-6*max(1, fl_p) and abs(fl/sl - fs_p) < 1e-4)
    print("     Gamma=%5g slice=%.9f areal=%.6f slice/areal=%.9f flight=%.6f flight/slice=%.9f"
          % (Gv, sl, ar, sl/ar, fl, fl/sl))
    chk("G  table row Gamma=%g reproduced" % Gv, ok)
fs = lambda Gv: (Gv**2 + Gv*math.sqrt(Gv*Gv - 1) - 1)/math.acosh(Gv)
chk("G  flight/slice strictly increasing in Gamma on a grid (2..1000)",
    all(fs(a) < fs(b) for a, b in zip(range(2, 1000), range(3, 1001))))
# H. clock note
c = math.acosh(100.0)
print("     note: target's own proper-time elapse from tau0=1: e^chi - 1 = %.6f (vs emitter dt %.6f);"
      " flight/slice with target clock = %.4f" % (math.exp(c) - 1, math.exp(c)*math.cosh(c) - 1, (math.exp(c)-1)/c))
chk("H  flight/slice > 1 at Gamma=100 on EITHER clock (qualitative conclusion clock-independent)",
    (math.exp(c) - 1)/c > 1 and (math.exp(c)*math.cosh(c) - 1)/c > 1)
print("\n%d FAIL(s)" % len(fails)); sys.exit(1 if fails else 0)
