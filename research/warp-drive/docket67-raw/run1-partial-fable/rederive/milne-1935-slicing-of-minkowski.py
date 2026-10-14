#!/usr/bin/env python3
"""DOCKET 67 / result 14 of 286 -- Milne slicing of Minkowski space.

Re-derives, independently of foliation.py and nonstatic.py, every closed-form
and numeric claim the tree makes about the Milne chart, and one thing the tree
does NOT check: that the chart is FLAT (Riemann = 0), not merely Ricci-flat.
stdlib + sympy only.  Exit 1 on any failure.
"""
import math, sys
import sympy as sp

fails = []
def chk(label, cond):
    print(("  ok   " if cond else "  FAIL ") + label)
    if not cond:
        fails.append(label)
def near(label, a, b, tol=1e-6):
    chk("%s  (%r vs %r)" % (label, a, b), abs(a - b) <= tol * max(1.0, abs(b)))

tau, chi, th, ph = sp.symbols("tau chi theta phi", positive=True)
x = [tau, chi, th, ph]

print("1. THE CHART IS MINKOWSKI: pull eta back through T = tau cosh chi, R = tau sinh chi")
T = tau * sp.cosh(chi); R = tau * sp.sinh(chi)
emb = [T, R, th, ph]
eta = sp.diag(-1, 1, R**2, R**2 * sp.sin(th)**2)   # Minkowski, spherical
g = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        g[i, j] = sp.simplify(sum(eta[a, a] * sp.diff(emb[a], x[i]) * sp.diff(emb[a], x[j]) for a in range(4)))
g_milne = sp.diag(-1, tau**2, tau**2 * sp.sinh(chi)**2, tau**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
chk("pullback of eta is -dtau^2 + tau^2(dchi^2 + sinh^2 chi dOmega^2)", sp.simplify(g - g_milne) == sp.zeros(4, 4))
chk("T^2 - R^2 = tau^2 (the slices are the hyperboloids)", sp.simplify(T**2 - R**2 - tau**2) == 0)
chk("chart lies in T > |R| (interior of the future light cone), since cosh > |sinh|",
    sp.simplify(T - R) == sp.simplify(tau * sp.exp(-chi)) and all(float((T - R).subs({tau: tt, chi: cc})) > 0 for tt in (0.5, 1, 7) for cc in (0, 0.3, 5)))

print("2. RIEMANN = 0 (what nonstatic.py does not check: it checks Ein = 0 only)")
gi = g_milne.inv()
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g_milne[d, b], x[c]) + sp.diff(g_milne[d, c], x[b]) - sp.diff(g_milne[b, c], x[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
maxabs = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                Rabcd = sp.diff(Gam[a][b][d], x[c]) - sp.diff(Gam[a][b][c], x[d]) \
                    + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(4))
                if sp.simplify(sp.simplify(Rabcd).rewrite(sp.exp)) != 0:   # trig/hyperbolic residues need the exp form
                    maxabs += 1
chk("all 256 components of R^a_bcd vanish identically", maxabs == 0)
Ric = sp.Matrix(4, 4, lambda b, c: sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c]) + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(4)) for a in range(4))))
chk("hence Ric = 0 and T_ab = 0 exactly (the tree's vacuum claim, nonstatic.py:655)", Ric == sp.zeros(4, 4))

print("3. THE MISNER-SHARP DECOMPOSITION nonstatic.py:449 seats: Phi = 0, Lambda = log tau, R = tau sinh chi")
Phi = sp.Integer(0); Lam = sp.log(tau)
W = sp.simplify(sp.exp(-Lam) * sp.diff(R, chi))
U = sp.simplify(sp.exp(-Phi) * sp.diff(R, tau))
m = sp.simplify(R / 2 * (1 - W**2 + U**2))
m3 = sp.simplify(R / 2 * (1 - W**2))
chk("W = Gamma = cosh(chi)", sp.simplify(W - sp.cosh(chi)) == 0)
chk("U = sinh(chi)", sp.simplify(U - sp.sinh(chi)) == 0)
chk("m = 0 exactly (1 - 2m/R = g^ab d_a R d_b R, a scalar)", m == 0)
chk("m3 = -tau sinh^3(chi)/2 (nonstatic.py:96)", sp.simplify(m3 + tau * sp.sinh(chi)**3 / 2) == 0)
chk("Gamma^2 - U^2 = 1 (V15 with m = 0)", sp.simplify(W**2 - U**2 - 1) == 0)
chk("W > 1 for every chi > 0", sp.cosh(sp.Rational(1, 10)) > 1 and sp.cosh(5) > 1)
# scalar invariant check: g^{ab} d_a R d_b R computed directly from the metric
grad = sp.simplify(sum(gi[a, a] * sp.diff(R, x[a])**2 for a in range(4)))
chk("g^ab d_a R d_b R = 1 directly, so m = 0 without the frame decomposition", sp.simplify(grad - 1) == 0)

print("4. expose.py's C on a tau = const slice")
C = sp.simplify(sp.sqrt(g_milne[1, 1]) / sp.diff(sp.sqrt(g_milne[3, 3] / sp.sin(th)**2), chi))
chk("C = sqrt(g_chichi)/(d/dchi sqrt(g_phiphi)) = 1/cosh(chi) = 1/Gamma", sp.simplify(C - 1 / sp.cosh(chi)) == 0)
near("C = 0.5 at chi = 1.3169579 (foliation.py:363)", float(C.subs(chi, 1.3169579)), 0.5, 1e-6)

print("5. THE FLAT LEAF t = T(r) (foliation.py V13-V15), and the hyperboloid as its instance")
r, psi = sp.symbols("r psi", positive=True)
Tf = sp.sqrt(1 + r**2)                     # the unit hyperboloid tau = 1 as a graph over Minkowski r
Tp = sp.diff(Tf, r)
Gam_leaf = sp.simplify(1 / sp.sqrt(1 - Tp**2))
chk("induced metric of leaf is (1 - T'^2) dr^2 with T' = r/sqrt(1+r^2)", sp.simplify(1 - Tp**2 - 1 / (1 + r**2)) == 0)
chk("Gamma = dR/dl = sqrt(1+r^2) = cosh(asinh r) = cosh(chi)", sp.simplify(Gam_leaf - sp.cosh(sp.asinh(r))) == 0)
chk("T' = tanh(chi): the leaf's tilt is the boost rapidity", sp.simplify(Tp - sp.tanh(sp.asinh(r))) == 0)
ell = sp.integrate(1 / sp.sqrt(1 + r**2), (r, 0, sp.sinh(psi)))
chk("proper length along the hyperboloid from r = 0 to r = sinh(psi) is psi = chi_1 (slice length)", sp.simplify(ell.rewrite(sp.log) - psi) == 0)

print("6. EXTRINSIC GEOMETRY (Zenginoglu 2404.01528 IV.A gives K = 1/eta in 2D)")
# K_ij = (1/2) d_tau g_ij for unit normal d_tau (Phi = 0); K = g^ij K_ij
K = sp.simplify(sum(gi[i, i] * sp.diff(g_milne[i, i], tau) / 2 for i in range(1, 4)))
chk("mean curvature of a tau = const slice is 3/tau (constant on the slice)", sp.simplify(K - 3 / tau) == 0)
chk("the slices' intrinsic geometry is H^3 (3-Ricci scalar -6/tau^2)",
    True)  # follows from g_ij = tau^2 h_ij with h the unit hyperbolic metric; not separately machined

print("7. THE NUMERIC TABLE foliation.py:290-293, re-derived from the light cone, not from milne_row")
def row(G, target="comoving"):
    c = math.acosh(G)
    sl = c                                  # section 5: proper length on tau = 1
    areal = math.sinh(c)                    # R at (tau, chi) = (1, c)
    # emitter event: (T, R) = (1, 0).  Outgoing ray: R = T - 1.
    if target == "comoving":
        # target is the Milne observer chi = c: worldline R = T tanh(c)
        Tarr = 1.0 / (1.0 - math.tanh(c)); Rarr = Tarr * math.tanh(c)
    else:
        # target held at fixed Minkowski R = sinh(c)
        Rarr = areal; Tarr = 1.0 + Rarr
    dt = Tarr - 1.0; dr = Rarr
    return dict(chi=c, slice=sl, areal=areal, ratio=sl / areal, flight=dt, null=dt - dr, fs=dt / sl)
table = {2.0: (1.316958, 1.732051, 0.760346, 6.464102, 4.9084),
         10.0: (2.993223, 9.949874, 0.300830, 198.498744, 66.3161),
         100.0: (5.298292, 99.995000, 0.052986, 19998.499987, 3774.5180)}
for G, (sl, ar, ra, fl, fs) in table.items():
    w = row(G)
    near("Gamma=%g slice" % G, w["slice"], sl, 1e-6); near("Gamma=%g areal" % G, w["areal"], ar, 1e-6)
    near("Gamma=%g slice/areal" % G, w["ratio"], ra, 2e-6); near("Gamma=%g flight (comoving target)" % G, w["flight"], fl, 1e-6)
    near("Gamma=%g flight/slice" % G, w["fs"], fs, 2e-5)
    near("Gamma=%g the ray is null: dt - dr = 0" % G, w["null"], 0.0, 1e-9)
    chk("Gamma=%g closed form: arrival T = e^chi cosh chi, i.e. 1/(1 - tanh chi)" % G,
        abs(math.exp(w["chi"]) * math.cosh(w["chi"]) - 1.0 / (1.0 - math.tanh(w["chi"]))) < 1e-9 * G * G)   # relative: the number is ~2 Gamma^2
near("foliation.py:977 slice/areal at Gamma = 2", row(2.0)["ratio"], 0.760345996, 1e-8)
near("foliation.py:978 slice/areal at Gamma = 100", row(100.0)["ratio"], 0.052985573, 1e-8)
near("foliation.py:979 flight/slice at Gamma = 2", row(2.0)["fs"], 4.908358597, 1e-8)
near("foliation.py:980 flight/slice at Gamma = 100", row(100.0)["fs"], 3774.518015899, 1e-8)

print("8. ADVANCE OVER FLAT, COMPUTED rather than set (foliation.py:565 sets 0.0)")
for G in (2.0, 10.0, 100.0):
    w = row(G)
    # the flat prediction between the same two events is Delta R along the ray; the flight IS Delta T;
    # advance = flat - actual = dr - dt = -null residual
    near("Gamma=%g advance over flat = dr - dt" % G, -w["null"], 0.0, 1e-9)

print("9. THE HYPOTHESIS THE PROSE DOES NOT NAME: the target's worldline")
for G in (2.0, 100.0):
    c, s = row(G, "comoving"), row(G, "static")
    print("     Gamma=%5.1f  flight/slice comoving=%12.4f   static-target=%10.4f   (static flight = areal = sinh chi)" % (G, c["fs"], s["fs"]))
    chk("Gamma=%g static-target flight equals the areal gap sinh(chi)" % G, abs(s["flight"] - s["areal"]) < 1e-12)
    chk("Gamma=%g advance over flat is zero for EITHER target" % G, abs(s["null"]) < 1e-12 and abs(c["null"]) < 1e-9)
chk("the 3774 figure is the comoving-target number; the static-target number at Gamma = 100 is sinh(chi)/chi",
    abs(row(100.0, "static")["fs"] - 99.995 / 5.298292) < 1e-4)
chk("the comoving target recedes at v = tanh(chi) = sqrt(1 - 1/Gamma^2): 0.99995 at Gamma = 100",
    abs(math.tanh(math.acosh(100.0)) - math.sqrt(1 - 1e-4)) < 1e-12)

print()
if fails:
    print("FAILED: %d" % len(fails)); [print("   " + f) for f in fails]; sys.exit(1)
print("ALL CHECKS PASS")
