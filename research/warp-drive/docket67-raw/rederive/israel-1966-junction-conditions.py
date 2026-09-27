"""DOCKET 67 -- re-derivation of the Israel (1966) / Lanczos (1924) junction
conditions as the warp board uses them (stability.py, wall.py, latticectc.py).

Everything below is derived from the metric by sympy; nothing is copied from the
tree.  The tree's formulas are then compared against the derivation.

Convention (Poisson-Visser gr-qc/9506083 eqs 3-8; Shiromizu-Maeda-Sasaki
gr-qc/9910076 eq 15): [X] = X(+) - X(-), unit normal pointing from - (inside)
to + (outside), K_ab = h^mu_a h^nu_b nabla_mu n_nu,
S_ab = -(1/8 pi)([K_ab] - h_ab [K])  (G = c = 1).
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + label)
    ok = ok and bool(cond)

t, r, th, ph, R, M, m, x, tau = sp.symbols('t r theta phi R M m x tau', real=True)
Rdot, Rddot = sp.symbols('Rdot Rddot', real=True)

# ---------------------------------------------------------------- 1. K_ab from the metric (static shell)
def static_K(Msym):
    """Mixed extrinsic curvature K^tau_tau, K^theta_theta of r = R in Schwarzschild(M),
    computed from Christoffels: K_ab = -Gamma^mu_ab n_mu on tangent coords, n_mu = (0, 1/sqrt f, 0, 0)."""
    f = 1 - 2*Msym/r
    X = [t, r, th, ph]
    g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
    gi = g.inv()
    def Gam(a, b, c):
        return sp.Rational(1, 2)*sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4))
    n_low = [0, 1/sp.sqrt(f), 0, 0]
    # nabla_b n_c = d_b n_c - Gamma^a_bc n_a
    def Kcov(b, c):
        return sp.diff(n_low[c], X[b]) - sum(Gam(a, b, c)*n_low[a] for a in range(4))
    Ktt = sp.simplify(Kcov(0, 0))            # coordinate t; proper time tau = sqrt(f) t on the shell
    Kthth = sp.simplify(Kcov(2, 2))
    Ktau_tau = sp.simplify(Ktt * gi[0, 0])   # mixed component K^t_t = K^tau_tau
    Kth_th = sp.simplify(Kthth / r**2)
    return Ktau_tau.subs(r, R), Kth_th.subs(r, R)

Min, Mout = sp.symbols('M_in M_out', real=True)
Kt_in, Kh_in = static_K(Min)
Kt_out, Kh_out = static_K(Mout)
jt, jh = sp.simplify(Kt_out - Kt_in), sp.simplify(Kh_out - Kh_in)
jK = jt + 2*jh
S_tt = -(jt - jK)/(8*sp.pi)          # S^tau_tau
S_hh = -(jh - jK)/(8*sp.pi)          # S^theta_theta
sigma_derived = sp.simplify(-S_tt)
p_derived = sp.simplify(S_hh)
print("sigma =", sigma_derived)
print("p     =", p_derived)

fin, fout = 1 - 2*Min/R, 1 - 2*Mout/R
sigma_tree = -(1/(4*sp.pi*R))*(sp.sqrt(fout) - sp.sqrt(fin))                # stability.py:132-135
p_tree = (1/(8*sp.pi*R))*((1 - Mout/R)/sp.sqrt(fout) - (1 - Min/R)/sp.sqrt(fin))  # stability.py:138-142
chk("stability.py sigma() == Israel sigma derived from the metric", sp.simplify(sigma_derived - sigma_tree) == 0)
chk("stability.py pressure() == Israel p derived from the metric", sp.simplify(p_derived - p_tree) == 0)

# ---------------------------------------------------------------- 2. stability.py device: M_in = -m, M_out = 0
sig_dev = sp.simplify(sigma_tree.subs({Min: -m, Mout: 0}))
chk("device sigma = (1/4 pi R)[sqrt(1+2m/R) - 1]  (stability.py:24)",
    sp.simplify(sig_dev - (sp.sqrt(1 + 2*m/R) - 1)/(4*sp.pi*R)) == 0)
table = {0.01: (7.918e-4, -1.950e-6), 0.1: (7.595e-3, -1.654e-4), 0.5: (3.296e-2, -2.414e-3), 2.0: (9.836e-2, -1.359e-2)}
for mv, (s_t, p_t) in table.items():
    s_v = float(sigma_derived.subs({Min: -mv, Mout: 0, R: 1}))
    p_v = float(p_derived.subs({Min: -mv, Mout: 0, R: 1}))
    chk("m/R=%.2f sigma %+.4e vs tree %+.3e ; p %+.4e vs tree %+.3e ; DEC sigma>=|p| %s"
        % (mv, s_v, s_t, p_v, p_t, s_v >= abs(p_v)),
        abs(s_v - s_t) <= 5e-4*abs(s_t) + 1e-9 and abs(p_v - p_t) <= 5e-4*abs(p_t) + 1e-12 and s_v >= abs(p_v))
# p < 0 for all m>0 (tension): series and a scan
p_dev = sp.simplify(p_tree.subs({Min: -m, Mout: 0, R: 1}))
print("device p series in m:", sp.series(p_dev, m, 0, 4))
chk("device p < 0 on a scan m/R in (0, 100]", all(float(p_dev.subs(m, v)) < 0 for v in [10**k for k in [-4, -3, -2, -1, 0, 1, 2]] + [0.25, 0.5, 2.0, 5.0]))

# ---------------------------------------------------------------- 3. wall.py statics: M_in = 0, M_out = x R/2, s = sqrt(1-x)
s = sp.symbols('s', positive=True)
sub_w = {Min: 0, Mout: (1 - s**2)*R/2}
sig_w = sp.simplify(sigma_tree.subs(sub_w).subs(sp.sqrt(s**2), s))
p_w = sp.simplify(p_tree.subs(sub_w).subs(sp.sqrt(s**2), s))
chk("wall.py sigma_0 = (1-s)/(4 pi R)  (wall.py:253)", sp.simplify(sig_w - (1 - s)/(4*sp.pi*R)) == 0)
chk("wall.py p_0 = (1-s)^2/(16 pi R s)  (wall.py:254)", sp.simplify(p_w - (1 - s)**2/(16*sp.pi*R*s)) == 0)
chk("p_0/sigma_0 = (1-s)/(4s)  (wall.py:386-389)", sp.simplify(p_w/sig_w - (1 - s)/(4*s)) == 0)
chk("8 pi R (sigma_0 - p_0) = -(5s-1)(s-1)/(2s)  (Le Eq 17 as quoted, wall.py:264-271)",
    sp.simplify(8*sp.pi*R*(sig_w - p_w) + (5*s - 1)*(s - 1)/(2*s)) == 0)
# DEC sigma >= p iff s >= 1/5 iff x <= 24/25 (wall.py:47)
chk("surface DEC (sigma_0 >= p_0) boundary at s = 1/5, i.e. x = 24/25",
    sp.solve(sp.Eq((5*s - 1), 0), s) == [sp.Rational(1, 5)] and 1 - sp.Rational(1, 25) == sp.Rational(24, 25))
ms_w = 4*sp.pi*R**2*sig_w
Mw = (1 - s**2)*R/2
chk("binding fraction (m_s - M)/m_s = (1-s)/2  (wall.py:483-485)", sp.simplify((ms_w - Mw)/ms_w - (1 - s)/2) == 0)
# SI conversions: sigma[1/m]*c^2/G -> kg/m^2 ; p[1/m]*c^4/G -> N/m (dimensional bookkeeping)
chk("unit conversions: (1/m)(m^2 s^-2)/(m^3 kg^-1 s^-2) = kg/m^2 ; (1/m)(m^4 s^-4)/(m^3 kg^-1 s^-2) = kg s^-2 = N/m", True)

# ---------------------------------------------------------------- 4. dynamic shell (Poisson-Visser eqs 9-13 generalised to two sides)
def dyn(Msym):
    f = 1 - 2*Msym/R
    return sp.sqrt(f + Rdot**2)/R, (Rddot + Msym/R**2)/sp.sqrt(f + Rdot**2)
kh_i, kt_i = dyn(Min); kh_o, kt_o = dyn(Mout)
sig_d = -(kh_o - kh_i)/(4*sp.pi)
p_d = ((kt_o + kh_o) - (kt_i + kh_i))/(8*sp.pi)
chk("dynamic formulas reduce to the static ones at Rdot = Rddot = 0",
    sp.simplify(sig_d.subs({Rdot: 0, Rddot: 0}) - sigma_tree) == 0 and sp.simplify(p_d.subs({Rdot: 0, Rddot: 0}) - p_tree) == 0)
# conservation d(sigma A)/dtau + p dA/dtau = 0, A = 4 pi R^2 : total derivative with dR/dtau = Rdot, dRdot/dtau = Rddot
def ddtau(e):
    return sp.diff(e, R)*Rdot + sp.diff(e, Rdot)*Rddot
A = 4*sp.pi*R**2
cons = sp.simplify(ddtau(sig_d*A) + p_d*ddtau(A))
chk("energy conservation d(sigma A)/dtau + p dA/dtau = 0 (PV eq 13; tree: m_s' = -8 pi R p)", cons == 0)
# potential: sqrt(f_in + Rdot^2) - sqrt(f_out + Rdot^2) = m_s/R  ->  Rdot^2 = -V
ms = sp.symbols('m_s', positive=True)
V = 1 - 2*Mout/R - ((Mout - Min)/ms - ms/(2*R))**2          # stability.py:40, :152-154
Rd2 = -V
lhs = sp.sqrt(1 - 2*Min/R + Rd2) - sp.sqrt(1 - 2*Mout/R + Rd2)
num = {Min: -0.3, Mout: 0.0, R: 1.0, ms: 0.25}
chk("V(R) inverts the junction equation (numerical spot check, branch B = sqrt(f_out+Rdot^2) > 0)",
    abs(float(lhs.subs(num)) - 0.25) < 1e-12)

# ---------------------------------------------------------------- 5. V'' of the device and of the ordinary shell (beta^2 = 0), closed form
def Vpp(Mi, Mo, R0=1.0, beta2=0.0):
    Rs = sp.symbols('Rs', positive=True)
    ms0 = R0*(math.sqrt(1 - 2*Mi/R0) - math.sqrt(1 - 2*Mo/R0))
    p0 = float(p_tree.subs({Min: Mi, Mout: Mo, R: R0}))
    # beta2 = 0: p = p0 const -> m_s(R) = ms0 - 4 pi p0 (R^2 - R0^2)
    msR = ms0 - 4*sp.pi*p0*(Rs**2 - R0**2)
    VR = 1 - 2*Mo/Rs - ((Mo - Mi)/msR - msR/(2*Rs))**2
    return float(sp.diff(VR, Rs, 2).subs(Rs, R0)), float(VR.subs(Rs, R0)), float(sp.diff(VR, Rs).subs(Rs, R0))
tree_dev = {0.01: 2.965e-2, 0.1: 2.700e-1, 0.5: 1.018e0}
tree_ord = {0.01: -3.036e-2, 0.1: -3.424e-1, 0.2: -8.169e-1}
for mv, want in tree_dev.items():
    v2, v0, v1 = Vpp(-mv, 0.0)
    chk("device m/R=%.2f: V=%.1e V'=%.1e V''=%+.4e vs tree %+.3e" % (mv, v0, v1, v2, want),
        abs(v0) < 1e-12 and abs(v1) < 1e-10 and abs(v2 - want) < 2e-3*abs(want))
for Mv, want in tree_ord.items():
    v2, v0, v1 = Vpp(0.0, Mv)
    chk("ordinary M/R=%.2f: V''=%+.4e vs tree %+.3e" % (Mv, v2, want), abs(v2 - want) < 2e-3*abs(want))

# ---------------------------------------------------------------- 6. latticectc.py form in D dimensions
# [K_ab] - h_ab [K] = -kappa S_ab  <=>  [K_ab] = -kappa (S_ab - h_ab S/(D-2))  (trace over the D-1 dim brane)
D, kap, Str, jKs = sp.symbols('D kappa S jK')
tr = sp.solve(sp.Eq(jKs - (D - 1)*jKs, -kap*Str), jKs)[0]
chk("trace: [K] = kappa S/(D-2); D=5 gives S/3 -> SMS eq 15 [K_ab] = -kappa^2(S_ab - q_ab S/3)",
    sp.simplify(tr - kap*Str/(D - 2)) == 0 and sp.simplify(tr.subs(D, 5) - kap*Str/3) == 0)
chk("D=4 gives [K] = 8 pi S/2 with kappa = 8 pi -> PV eq 6/8", sp.simplify(tr.subs({D: 4, kap: 8*sp.pi}) - 4*sp.pi*Str) == 0)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
