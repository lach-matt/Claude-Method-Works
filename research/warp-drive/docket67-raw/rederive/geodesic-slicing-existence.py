#!/usr/bin/env python3
r"""
DOCKET 67 -- rederive/geodesic-slicing-existence.py

External result audited: existence of geodesic slicing / Gaussian normal
coordinates (lapse N = e^Phi = 1, shift 0), as used at nonstatic.py:87-89
("in geodesic slicing (Phi = 0, always available) D_t W = 4 pi R j") and
nonstatic.py:178-183 (build energy E = R Delta W, "R held fixed").

Source READ: Gourgoulhon, gr-qc/0703035, sec 3.3.3 eq (3.18) a = D ln N;
sec 4.4.2 p.61-62 (N=1, beta=0 "in some neighbourhood [of] a given
hypersurface Sigma_0 ... In general it is not possible to get a Gaussian normal
coordinate system that covers all M"); sec 9.2.1 p.152 (geodesic slicing of the
t_S = 0 Schwarzschild slice "hits the singularity at t = pi m").

Checks (every one a residual that must be 0, or a z3 unsat, or a number):
  A  Einstein tensor of ds^2 = -dt^2 + e^{2L}dr^2 + R^2 dOmega^2 computed here;
     with Phi = 0, D_t W = 4 pi R j exactly (the tree's EV-W at Phi = 0).
  B  Eulerian acceleration of the tree's metric is a_r-hat = e^{-L} Phi'; a
     relabelling t -> f(t) sends Phi -> Phi + ln f'; so Phi can be set to 0
     WITHOUT CHANGING THE SLICES iff Phi' = 0 (z3: a nonzero Phi' cannot be
     cancelled by a function of t alone).  Otherwise geodesic slicing is a
     DIFFERENT FOLIATION.
  C  W is not slicing-invariant: under a radial boost of the normal,
     U' = g(U + vW), W' = g(W + vU), W'^2 - U'^2 = W^2 - U^2 (sympy 0).
     Two geodesic slicings of the SAME Minkowski space: standard (W = 1) and
     Milne (W = cosh chi), both Phi = 0, both j = 0 -- so "W in geodesic
     slicing" depends on which initial slice the normal geodesics leave.
  D  Non-globality, flat space: the time-reversed Milne slicing (normals to the
     past hyperboloid t = -sqrt(tau0^2 + r^2)) is a geodesic slicing whose
     normal geodesics ALL meet at the origin after proper time tau0 -- a caustic
     with T_ab = 0 identically.
  E  Non-globality, Schwarzschild (Gourgoulhon's example): radial geodesic from
     rest at R0 reaches R = 0 at tau = (pi/2) sqrt(R0^3/(2m)); at the throat
     R0 = 2m this is pi m.
  F  Build at fixed R in geodesic slicing (nonstatic.py:178-183): U = 0 held on
     the boundary sphere, with the tree's own MS-t and EV-W at Phi = 0,
     integrates to m = R(1 - W^2)/2, and EV-U demands p_r = -m/(4 pi R^3).
     At Delta W = 1 from W = 1 the enclosed Misner-Sharp mass is -3R/2.
     Proxima span evaluated in solar masses.

python3 geodesic-slicing-existence.py      prints every check, exits 1 on any failure
"""
import sys
import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + ("   " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


def einstein(g, x):
    n = len(x)
    gi = g.inv()
    Gm = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                        - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(n):
                    s += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return Gm, sp.simplify(Ric - Rs * g / 2)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]
L = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
Phi = sp.Function("Phi")(t, r)

print("A  EV-W at Phi = 0, from an Einstein tensor computed here")
g0 = sp.diag(-1, sp.exp(2 * L), R**2, R**2 * sp.sin(th)**2)
_, G0 = einstein(g0, x)
j0 = -(G0[0, 1] / (8 * sp.pi)) * sp.exp(-L)          # j = -T_ab u^a n^b, u = d_t, n = e^-L d_r
W0 = sp.exp(-L) * sp.diff(R, r)
resA = sp.simplify(sp.diff(W0, t) - 4 * sp.pi * R * j0)
chk("D_t W - 4 pi R j = 0 at Phi = 0", resA == 0, "residual = %s" % resA)

print("B  when is Phi = 0 a relabelling, and when a new foliation")
g1 = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * L), R**2, R**2 * sp.sin(th)**2)
Gm1, _ = einstein(g1, x) if False else (None, None)
# acceleration of u = e^-Phi d_t : a^mu = u^nu nabla_nu u^mu
gi1 = g1.inv()
Gam = [[[sp.simplify(sum(gi1[a, d] * (sp.diff(g1[d, b], x[c]) + sp.diff(g1[d, c], x[b])
                                      - sp.diff(g1[b, c], x[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]
u = [sp.exp(-Phi), 0, 0, 0]
acc = [sp.simplify(sum(u[nu] * sp.diff(u[mu], x[nu]) for nu in range(4))
                   + sum(Gam[mu][a][b] * u[a] * u[b] for a in range(4) for b in range(4)))
       for mu in range(4)]
a_hat = sp.simplify(acc[1] * sp.exp(L))                 # orthonormal radial component
chk("Eulerian acceleration a_rhat = e^-Lambda d_r Phi  (Gourgoulhon 3.18, a = D ln N)",
    sp.simplify(a_hat - sp.exp(-L) * sp.diff(Phi, r)) == 0, "a_rhat = %s" % a_hat)
chk("a^t = a^theta = a^phi = 0", all(sp.simplify(acc[k]) == 0 for k in (0, 2, 3)))
# relabel t = f(T): g_TT = -e^{2Phi} f'(T)^2 -> Phi_new = Phi + ln f'
T = sp.Symbol("T")
f = sp.Function("f")(T)
Phi_new = Phi.subs(t, f) + sp.log(sp.diff(f, T))
chk("relabelling leaves d_r Phi unchanged: d_r Phi_new = (d_r Phi)|_{t=f(T)}",
    sp.simplify(sp.diff(Phi_new, r) - sp.diff(Phi, r).subs(t, f)) == 0)
import z3
# z3: at two radii on one slice, Phi_new = Phi(r) + c (c = ln f' is one number per slice);
# Phi_new = 0 at both requires Phi(r1) = Phi(r2).  Phi(r1) != Phi(r2) => unsat.
p1, p2, c = z3.Reals("p1 p2 c")
s = z3.Solver()
s.add(p1 != p2, p1 + c == 0, p2 + c == 0)
chk("z3: Phi' != 0 on a slice cannot be removed by any relabelling of t (unsat)",
    s.check() == z3.unsat, str(s.check()))

print("C  W is a component, not a scalar: radial boost of the slice normal")
U, Wv, v = sp.symbols("U W v", real=True)
gam = 1 / sp.sqrt(1 - v**2)
Up, Wp = gam * (U + v * Wv), gam * (Wv + v * U)
chk("W'^2 - U'^2 = W^2 - U^2 (Misner-Sharp scalar invariant)",
    sp.simplify(Wp**2 - Up**2 - (Wv**2 - U**2)) == 0)
chk("W' != W for v != 0 when U, W not both 0: W' - W at (U,W,v)=(0,1,1/2) = %s"
    % sp.nsimplify(Wp.subs({U: 0, Wv: 1, v: sp.Rational(1, 2)}) - 1),
    Wp.subs({U: 0, Wv: 1, v: sp.Rational(1, 2)}) != 1)
# two geodesic slicings of Minkowski
tau, chi = sp.symbols("tau chi", positive=True)
gM = sp.diag(-1, tau**2, tau**2 * sp.sinh(chi)**2, tau**2 * sp.sinh(chi)**2 * sp.sin(th)**2)
_, GM = einstein(gM, [tau, chi, th, ph])
chk("Milne slicing: lapse 1 (geodesic slicing), G_ab = 0 identically",
    all(sp.simplify(GM[a, b]) == 0 for a in range(4) for b in range(4)))
W_milne = sp.simplify((1 / tau) * sp.diff(tau * sp.sinh(chi), chi))
chk("Milne slicing: W = cosh chi; standard slicing (also lapse 1): W = 1",
    sp.simplify(W_milne - sp.cosh(chi)) == 0, "W_milne = %s" % W_milne)
chk("both: D_t W = 0 and j = 0 -- EV-W at Phi = 0 holds in each, W differs",
    sp.diff(W_milne, tau) == 0)

print("D  caustic of a geodesic slicing in FLAT space (time-reversed Milne)")
# normals to t = -sqrt(tau0^2 + rr^2): geodesic through (t, rr) = (-tau0 cosh chi, tau0 sinh chi)
# with 4-velocity (cosh chi, -sinh chi)... parametrise x(s) = (-(tau0 - s) cosh chi, (tau0 - s) sinh chi)
s_, tau0 = sp.symbols("s tau0", positive=True)
xt = -(tau0 - s_) * sp.cosh(chi)
xr = (tau0 - s_) * sp.sinh(chi)
vel = [sp.diff(xt, s_), sp.diff(xr, s_)]
chk("each is a unit timelike straight line (a geodesic): -vt^2 + vr^2 = -1",
    sp.simplify(-vel[0]**2 + vel[1]**2 + 1) == 0)
tan = [sp.diff(xt, chi).subs(s_, 0), sp.diff(xr, chi).subs(s_, 0)]   # tangent to the initial slice
chk("each leaves the slice orthogonally: eta(tangent, velocity) = 0",
    sp.simplify(-tan[0] * vel[0] + tan[1] * vel[1]) == 0)
chk("initial slice is the past hyperboloid t = -sqrt(tau0^2 + r^2)",
    sp.simplify(xt.subs(s_, 0) + sp.sqrt(tau0**2 + xr.subs(s_, 0)**2)) == 0)
chk("ALL meet at the origin at proper time s = tau0, whatever chi (caustic)",
    xt.subs(s_, tau0) == 0 and xr.subs(s_, tau0) == 0)
# induced 3-metric degenerates: (tau0 - s)^2 (dchi^2 + sinh^2 chi dOmega^2) -> 0
print("       3-metric along the slicing = (tau0 - s)^2 [dchi^2 + sinh^2 chi dOmega^2] -> 0 at s = tau0")

print("E  Schwarzschild geodesic slicing from the t_S = 0 slice (Gourgoulhon sec 9.2.1)")
m, R0, Rr = sp.symbols("m R0 Rr", positive=True)
# radial geodesic from rest at R0: (dR/dtau)^2 = 2m/R - 2m/R0
tau_fall = sp.integrate(1 / sp.sqrt(2 * m / Rr - 2 * m / R0), (Rr, 0, R0))
tau_fall = sp.simplify(tau_fall)
chk("tau(R0 -> 0) = (pi/2) sqrt(R0^3/(2m))",
    sp.simplify(tau_fall - sp.pi / 2 * sp.sqrt(R0**3 / (2 * m))) == 0, "tau = %s" % tau_fall)
chk("throat R0 = 2m: tau = pi m (the slicing hits R = 0 there)",
    sp.simplify(tau_fall.subs(R0, 2 * m) - sp.pi * m) == 0)

print("F  the build at fixed R in geodesic slicing (nonstatic.py:178-183)")
Wf = sp.Symbol("Wf", positive=True)
mW = sp.Function("mW")
# U = 0 held: MS-t dm = -4 pi R^2 j W dtau ; EV-W dW = 4 pi R j dtau  =>  dm/dW = -R W
sol = sp.dsolve(sp.Eq(sp.diff(mW(Wv), Wv), -Rr * Wv), mW(Wv), ics={mW(1): 0})
chk("dm/dW = -R W with m(W=1) = 0 gives m = R(1 - W^2)/2",
    sp.simplify(sol.rhs - Rr * (1 - Wv**2) / 2) == 0, "m(W) = %s" % sp.factor(sol.rhs))
chk("agrees with the tree's own identity W^2 = 1 - 2m/R + U^2 at U = 0",
    sp.simplify((1 - 2 * sol.rhs / Rr) - Wv**2) == 0)
pr = sp.solve(sp.Eq(0, -sol.rhs / Rr**2 - 4 * sp.pi * Rr * sp.Symbol("p_r")), sp.Symbol("p_r"))[0]
print("       EV-U at Phi = 0, U = 0 held (D_t U = 0): p_r = %s" % sp.factor(pr))
E_build = sp.integrate(Rr, (Wv, 1, 2))     # dE = R dW
chk("E = R Delta W = R at Delta W = 1", sp.simplify(E_build - Rr) == 0)
chk("enclosed Misner-Sharp mass at W = 2 is -3R/2 (NEGATIVE)",
    sp.simplify(sol.rhs.subs(Wv, 2) + sp.Rational(3, 2) * Rr) == 0)
C, G, MSUN, LY = 2.99792458e8, 6.67430e-11, 1.98840e30, 9.4607304725808e15
Rm = 4.2465 * LY
geo = Rm * C * C / G / MSUN
print("       Proxima span R = %.6e m: R c^2/G = %.6e M_sun" % (Rm, geo))
print("       E (throughput)       = %.4e M_sun c^2 (tree prints 2.72e13)" % geo)
print("       m at the boundary    = %.4e M_sun  (from U = 0 held + anchor identity)" % (-1.5 * geo))
chk("E reproduces the tree's 2.72e13 to 3 figures", abs(geo / 2.72e13 - 1) < 5e-3,
    "%.5e" % geo)

print()
print("FAILURES: %d" % len(FAIL))
sys.exit(1 if FAIL else 0)
