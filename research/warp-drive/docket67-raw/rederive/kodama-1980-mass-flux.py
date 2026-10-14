#!/usr/bin/env python3
"""
DOCKET 67 / pass S / 13 of 36 -- kodama-1980-mass-flux.

Independent re-derivation (no import of any research/warp-drive module) of
the Kodama 1980 results as restated by Hayward gr-qc/9408002 App. B
(eqs B1-B8) and Abreu-Visser arXiv:1004.1456 secs III, VIII, IX, and of the
tree's use in formation.py:136,155:

    K(R) = INT 4 pi R^2 j W dtau = R (W_1^2 - 1)/2 = -m_1(R)      (U = 0)
    "the Kodama mass it leaves is exactly the jump of m_1 at the shell"

Metric: ds^2 = -e^{2Phi(t,r)}dt^2 + e^{2Lam(t,r)}dr^2 + R(t,r)^2 dOmega^2,
Einstein tensor computed here from Christoffels.  Conventions: G = c = 1,
G_ab = 8 pi T_ab, u = e^{-Phi} d_t (Eulerian), n = e^{-Lam} d_r (outward),
j = -T(u,n) (outward radial energy flux; the tree's convention),
U = u(R), W = n(R), m = (R/2)(1 - W^2 + U^2)  (Misner-Sharp).
Kodama vector (Hayward B1/B4a orientation, future-pointing when untrapped):
k = e^{-Phi-Lam} (R' d_t - Rdot d_r).   Kodama current (Hayward B2): J^a = -T^a_b k^b.

Run: python3 kodama-1980-mass-flux.py      exits 0 with 'ALL PASS'.
"""
import sys
import sympy as sp
import mpmath as mpm

RES = []


def chk(tag, desc, ok):
    RES.append((tag, desc, bool(ok)))
    print("%-4s %-6s %s" % (tag, "PASS" if ok else "FAIL", desc))


def z(e):
    return sp.simplify(sp.expand(e)) == 0


t, r, th, ph_ = sp.symbols("t r theta phi")
X = [t, r, th, ph_]
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lam")(t, r)
R = sp.Function("R")(t, r)
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
gi = g.inv()
N = 4


def einstein(g, gi):
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                        - sp.diff(g[b, c], X[d])) for d in range(N)) / 2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    Ric = sp.zeros(N)
    for b in range(N):
        for c in range(N):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) for a in range(N))
                                    - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(N))
                                    + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(N) for d in range(N))
                                    - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(N) for d in range(N)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(N) for b in range(N)))
    return sp.simplify(Ric - Rs * g / 2)


G = einstein(g, gi)                       # G_ab (lower)
T = G / (8 * sp.pi)                       # H_EFE
Tud = sp.simplify(gi * T)                 # T^a_b
sqrtg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)


def div(V):
    return sp.simplify(sum(sp.diff(sqrtg * V[a], X[a]) for a in range(N)) / sqrtg)


Rd, Rp = sp.diff(R, t), sp.diff(R, r)
U = sp.exp(-Phi) * Rd
W = sp.exp(-Lam) * Rp
m = R / 2 * (1 - W**2 + U**2)
u = [sp.exp(-Phi), 0, 0, 0]
n = [0, sp.exp(-Lam), 0, 0]
Tab = lambda A, B: sum(T[a, b] * A[a] * B[b] for a in range(N) for b in range(N))
j = -Tab(u, n)
rho = Tab(u, u)
p_r = Tab(n, n)
Dt = lambda e: sp.exp(-Phi) * sp.diff(e, t)
Dr = lambda e: sp.exp(-Lam) * sp.diff(e, r)
k = [sp.exp(-Phi - Lam) * Rp, -sp.exp(-Phi - Lam) * Rd, 0, 0]
gdot = lambda A, B: sp.simplify(sum(g[a, b] * A[a] * B[b] for a in range(N) for b in range(N)))

print("=== C1-C5: Kodama's vector and current, general spherical metric (no field equation used)")
chk("C1a", "k(R) = 0: Kodama vector tangent to constant-R surfaces (Hayward B5a)",
    z(k[0] * Rd + k[1] * Rp))
chk("C1b", "g(k,k) = 2m/R - 1 (Hayward B3)", z(gdot(k, k) - (2 * m / R - 1)))
chk("C2", "Div k = 0 (Hayward B7a; Abreu-Visser eq.30)", z(div(k)))
J = [sp.simplify(-sum(Tud[a, b] * k[b] for b in range(N))) for a in range(N)]
chk("C3", "Div J = 0 identically, J = -G.k/8pi, NO field equation (AV eq.31, 'purely geometrical')",
    z(div(J)))
km = [sp.exp(-Phi - Lam) * sp.diff(m, r), -sp.exp(-Phi - Lam) * sp.diff(m, t), 0, 0]
chk("C4", "4 pi R^2 J = curl m  (Hayward B6; = AV eq.39 up to sign convention of J)",
    all(z(4 * sp.pi * R**2 * J[a] - km[a]) for a in range(2)) and J[2] == 0 and J[3] == 0)
# charge on a t = const slice between two spheres: density -g(J,u) times 4 pi R^2 e^Lam dr
dens = sp.simplify(-gdot(J, u) * 4 * sp.pi * R**2 * sp.exp(Lam))
chk("C5", "Gauss: charge density on t=const slice = dm/dr, so Q_J between spheres = Delta m (Hayward B8b)",
    z(dens - sp.diff(m, r)))

print("=== C6: the flux across a sphere's world-tube: where H_U0 enters")
flux_n = sp.simplify(gdot(J, n))          # outward flux density through r = const
chk("C6a", "g(J,n) = j W + p_r U  (outward Kodama flux through the r = const tube; k = W u - U n)",
    z(flux_n - (j * W + p_r * U)))
chk("C6b", "MS-t: D_t m = -4 pi R^2 (p_r U + j W)  (= -4 pi R^2 g(J,n))",
    z(Dt(m) + 4 * sp.pi * R**2 * (p_r * U + j * W)))
U0 = {sp.Derivative(R, t): 0}
chk("C6c", "at U = 0: k = W u exactly (Eulerian observer = Kodama observer)",
    z(k[0].subs(U0) - (W * u[0])) and z(k[1].subs(U0)))
chk("C6d", "at U = 0: D_t m = -4 pi R^2 j W  (the tree's integrand, formation.py:132)",
    z((Dt(m) + 4 * sp.pi * R**2 * j * W).subs(U0).doit()))
# CONTROL: without U = 0 the tree's integrand misses -4 pi R^2 p_r U: exhibit a nonzero residual
Rtest = r * (1 + t)
resid = (Dt(m) + 4 * sp.pi * R**2 * j * W).subs(R, Rtest).subs({Phi: 0, Lam: 0}).doit()
chk("C6e", "CONTROL: with U != 0 (R = r(1+t), flat lapse) D_t m + 4 pi R^2 j W != 0 -> H_U0 load-bearing",
    sp.simplify(resid) != 0)

print("=== C7: the tree's family  (Phi = f phi, Lam = (1-f) ln h' - f phi, R = h = r e^{-phi})")
f = sp.Function("f")(t)
vph = sp.Function("varphi")(r)
W1 = 1 - r * sp.diff(vph, r)
h = r * sp.exp(-vph)
om = sp.log(W1)
lnhp = sp.log(W1) - vph                   # ln h' for W1 > 0
fam = {Phi: f * vph, Lam: (1 - f) * lnhp - f * vph, R: h}
S = lambda e: sp.simplify(sp.expand_log(e.subs(fam).doit(), force=True))
Wf, mf, jf, Uf = S(W), S(m), S(j), S(U)
chk("C7a", "family: U = 0", z(Uf))
chk("C7b", "family: W = W_1^f", z(sp.expand_log(Wf - sp.exp(f * om), force=True)) or
    sp.simplify(Wf / sp.exp(f * om) - 1) == 0)
chk("C7c", "family: m = (R/2)(1 - W_1^{2f})", sp.simplify(sp.expand_log(mf - h * (1 - sp.exp(2 * f * om)) / 2, force=True)) == 0)
fd = sp.diff(f, t)
chk("C7d", "family: j = fdot omega W_1^f e^{-f phi}/(4 pi R)",
    sp.simplify(sp.expand_log(jf - fd * om * sp.exp(f * om) * sp.exp(-f * vph) / (4 * sp.pi * h), force=True)) == 0)
fs = sp.Symbol("f_s")
# d tau = e^{f phi} dt, and every integrand is fdot x (function of f): the t-integral is an f-integral
Kint_df = sp.simplify(4 * sp.pi * h**2 * jf * Wf * sp.exp(f * vph) / fd)
Eint_df = sp.simplify(4 * sp.pi * h**2 * jf * sp.exp(f * vph) / fd)
chk("C7e", "integrand per df carries no fdot/fddot: any route, any speed, any lapse",
    not Kint_df.has(fd) and not Eint_df.has(fd))
K = sp.integrate(Kint_df.subs(f, fs), (fs, 0, 1))
E = sp.integrate(Eint_df.subs(f, fs), (fs, 0, 1))
chk("C7f", "K(R) = INT 4 pi R^2 j W dtau = R (W_1^2 - 1)/2", sp.simplify(K - h * (W1**2 - 1) / 2) == 0)
m1 = sp.simplify(mf.subs(f, 1))
m0 = sp.simplify(mf.subs(f, 0))
chk("C7g", "m at f = 0 is 0 (flat start, H_ENDS)", m0 == 0)
chk("C7h", "K(R) = m_0 - m_1 = -m_1  (Kodama flux out = loss of Misner-Sharp charge)", sp.simplify(K + m1) == 0)
chk("C7i", "E(R) = INT 4 pi R^2 j dtau = R (W_1 - 1)", sp.simplify(E - h * (W1 - 1)) == 0)
Kbad = sp.integrate((Eint_df).subs(f, fs), (fs, 0, 1))
chk("C7j", "VACUITY GUARD: dropping the W factor (Eulerian flux) does NOT give -m_1",
    sp.simplify(Kbad + m1) != 0)
# Abreu-Visser eq.(79)-(81): the W-less fixed-r flux is the Brown-York energy
Wv, Rv = sp.symbols("W R_v", positive=True)
mv = Rv * (1 - Wv**2) / 2
U_BY = Rv * (1 - sp.sqrt(1 - 2 * mv / Rv))
chk("C7k", "AV eq.(81): E = R(W-1) is minus the Brown-York energy r(1 - sqrt(1-2m/r)) (W > 0)",
    sp.simplify(Rv * (Wv - 1) + U_BY) == 0)
chk("C7l", "AV eq.(82): m = U_BY - U_BY^2/(2R)", sp.simplify(mv - (U_BY - U_BY**2 / (2 * Rv))) == 0)

print("=== C8: numeric, on the seated object (m = a = 1/50, R_s = 200), 40 digits, independent code")
mpm.mp.dps = 40
M_, A_, RS_ = mpm.mpf(1) / 50, mpm.mpf(1) / 50, mpm.mpf(200)


def phi_side(x, side):
    s = mpm.sqrt(x**2 + A_**2)
    return M_ / s - M_ / (RS_ if side == "in" else x)


def m1(x, side):
    W1n = 1 - x * mpm.diff(lambda y: phi_side(y, side), x)
    Rn = x * mpm.exp(-phi_side(x, side))
    return Rn * (1 - W1n**2) / 2, W1n, Rn


table = {}
for x, side in ((0.005, "in"), (0.02, "in"), (1, "in"), (100, "in"), (250, "out"), (1000, "out")):
    mm, W1n, Rn = m1(mpm.mpf(x), side)
    table[(x, side)] = -mm
    print("     r=%-6s %-3s  K=-m_1 = %s" % (x, side, mpm.nstr(-mm, 8)))
# formation.py's printed table (rederive/kodama-formation-report.out lines 17-25)
printed = {(0.005, "in"): 1.11248e-04, (0.02, "in"): 4.10327e-03, (1, "in"): 1.97901e-02,
           (100, "in"): 2.00000e-02, (250, "out"): -1.92000e-10, (1000, "out"): -1.20000e-11}
chk("C8a", "K = -m_1 agrees with formation.py's printed table to its 6 printed digits",
    all(abs(table[kk] - v) <= 6e-6 * abs(v) for kk, v in printed.items()))
jump = m1(RS_, "out")[0] - m1(RS_, "in")[0]
print("     shell jump m_1(R_s+) - m_1(R_s-) = %s" % mpm.nstr(jump, 20))
chk("C8b", "shell jump = 2.00010e-02 as printed by formation.py (and > 0)",
    jump > 0 and abs(jump - mpm.mpf("2.00010e-02")) < 5e-7)
chk("C8c", "m_1(R_s+) is tiny positive (< 1e-6): the exterior carries almost nothing",
    0 < m1(RS_, "out")[0] < 1e-6)
chk("C8d", "interior K -> m = 1/50 for a << r < R_s (r = 100: |K - 1/50| < 1e-5)",
    abs(table[(100, "in")] - M_) < 1e-5)
# closed form for the jump: phi is continuous at R_s, R continuous, W1 jumps by -m/R_s
W1in, W1out = m1(RS_, "in")[1], m1(RS_, "out")[1]
chk("C8e", "W_1 jumps by exactly -m/R_s at the shell (phi' jumps by m/R_s^2): thin-shell source",
    abs((W1out - W1in) + M_ / RS_) < mpm.mpf(10)**-30)

# regular centre on the seated object: m_1 = O(R^3) (so 'enclosed' is meaningful here, Hayward p.4)
c1 = m1(mpm.mpf("1e-3"), "in"); c2 = m1(mpm.mpf("1e-4"), "in")
q1, q2 = c1[0] / c1[2]**3, c2[0] / c2[2]**3
print("     m_1/R^3 at r = 1e-3, 1e-4: %s, %s" % (mpm.nstr(q1, 8), mpm.nstr(q2, 8)))
chk("C8f", "regular centre: m_1/R^3 tends to a finite limit (ratios agree to 1%)",
    abs(q1 / q2 - 1) < 1e-2)

npass = sum(1 for x in RES if x[2])
print("\n%d/%d checks pass" % (npass, len(RES)))
print("ALL PASS" if npass == len(RES) else "FAILURES")
sys.exit(0 if npass == len(RES) else 1)
