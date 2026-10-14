"""DOCKET 67 -- audit of 'linearised-weak-field-metric' (composite.py:35-36, 99-104, 128-138;
concentric.py:139-141, 149-151, 171-174).  Reads research/warp-drive, writes nothing there.

R1  sympy: ds^2 = -(1+2Phi)dt^2 + (1-2Phi)dx^2, Phi=-M/r, solves the LINEARISED vacuum
    Einstein equations (O(M) Ricci = 0), and is the O(M) truncation of exact Schwarzschild in
    isotropic coordinates -- for M of either sign (the expansion is analytic in M).
    The O(M^2) terms it drops are printed.
R2  sympy: its exact Ricci is O(M^2); the fixed-point trace residue composite.py:326-327
    attributes to 'the metric's own O(Phi^2)' is recomputed exactly and decomposed.
R3  mpmath: light deflection, linearised metric vs exact isotropic Schwarzschild, both signs:
    second-order coefficient of (M/b)^2.
R4  scipy: composite.py's WINDOW (b=0.3, x0=-40, lam=75) re-run with an independent integrator
    (analytic Christoffels, conjugate points from neighbouring geodesics, not from Riemann),
    on the linearised metric AND on exact negative-mass Schwarzschild (isotropic), and both
    window edges located by bisection in each.
R5  concentric.py: |Phi| along its corridor ray versus Phi_max at the core centre.
"""
import math, sys
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

OUT = []
def rec(tag, msg):
    OUT.append((tag, msg)); print("[%s] %s" % (tag, msg))

# ------------------------------------------------------------------ R1, R2 (sympy)
t, x, y, z, M, eps = sp.symbols('t x y z M epsilon', real=True)
X = (t, x, y, z)
r = sp.sqrt(x**2 + y**2 + z**2)

def curvature(g):
    gi = sp.simplify(g.inv())
    n = 4
    G = [[[sp.simplify(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                            for e in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    def Rup(a, b, c, d):
        return (sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
                + sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(n)))
    return G, Rup

def lin_metric(Mv):
    Phi = -Mv / r
    return sp.diag(-(1 + 2*Phi), 1 - 2*Phi, 1 - 2*Phi, 1 - 2*Phi)

g = lin_metric(M)
G, Rup = curvature(g)
# Ricci R_bd = R^a_{b a d}
Ric = sp.zeros(4, 4)
for b in range(4):
    for d in range(b, 4):
        Ric[b, d] = sp.simplify(sum(Rup(a, b, a, d) for a in range(4)))
        Ric[d, b] = Ric[b, d]
ord1 = [sp.simplify(sp.diff(Ric[i, j], M).subs(M, 0)) for i in range(4) for j in range(4)]
rec("R1", "O(M) part of Ricci of the linearised metric, all 16 components: %s"
    % ("ALL ZERO" if all(e == 0 for e in ord1) else ord1))
ord2 = sp.simplify(sp.diff(Ric[0, 0], M, 2).subs(M, 0) / 2)
rec("R1", "O(M^2) part of R_tt of the linearised metric: %s  (nonzero: the form is not an exact vacuum solution)" % ord2)

# exact Schwarzschild isotropic expansion
rr = sp.symbols('r', positive=True)
A_ex = ((1 - M/(2*rr))/(1 + M/(2*rr)))**2
B_ex = (1 + M/(2*rr))**4
sA = sp.series(A_ex, M, 0, 3).removeO()
sB = sp.series(B_ex, M, 0, 3).removeO()
rec("R1", "exact isotropic Schwarzschild: -g_tt = %s + O(M^3);  g_ii = %s + O(M^3)" % (sp.expand(sA), sp.expand(sB)))
ok1 = sp.simplify(sA.coeff(M, 1) - (-2/rr)) == 0 and sp.simplify(sB.coeff(M, 1) - (2/rr)) == 0
rec("R1", "O(M) coefficients equal the linearised metric's (-2/r, +2/r): %s; dropped O(M^2): g_tt %s, g_ii %s"
    % (ok1, sp.simplify(-sA.coeff(M, 2)), sp.simplify(sB.coeff(M, 2))))
# exact Schwarzschild isotropic is a vacuum solution for M<0 too (check Ricci symbolic)
gS = sp.diag(-A_ex.subs(rr, r), B_ex.subs(rr, r), B_ex.subs(rr, r), B_ex.subs(rr, r))
GS, RupS = curvature(gS)
pt = {x: sp.Rational(1, 10), y: sp.Rational(3, 10), z: sp.Rational(1, 7)}
ricS = [sp.N(sum(RupS(a, b, a, b) for a in range(4)).subs(pt).subs(M, sp.Rational(-4, 100)), 30) for b in range(4)]
rec("R1", "exact isotropic Schwarzschild, M=-0.04, Ricci diagonal at a sample point: %s  (vacuum for M<0 as for M>0)"
    % [sp.nsimplify(v, tolerance=1e-25) for v in ricS])

# R2: composite.py fixed-point trace residue
def Rlow_num(gm, Rupf, Mv, p, k, e):
    """R_{m a n b} k^m e^a k^n e^b at point p, exact."""
    sub = {M: Mv, t: 0, x: p[0], y: p[1], z: p[2]}
    gnum = gm.subs(sub)
    tot = 0
    for m in range(4):
        if k[m] == 0: continue
        for a in range(4):
            if e[a] == 0: continue
            for nn in range(4):
                if k[nn] == 0: continue
                for bb in range(4):
                    if e[bb] == 0: continue
                    Rl = sum(gnum[m, q]*Rupf(q, a, nn, bb).subs(sub) for q in range(4))
                    tot += Rl*k[m]*e[a]*k[nn]*e[bb]
    return sp.N(tot, 30)

Mv = sp.Rational(-2, 1000); p = (0, sp.Rational(3, 10), 0)
kc = [1, 1, 0, 0]; e1 = [0, 0, 1, 0]; e2 = [0, 0, 0, 1]
T11 = -Rlow_num(g, Rup, Mv, p, kc, e1); T22 = -Rlow_num(g, Rup, Mv, p, kc, e2)
ratio_comp = abs(T11 + T22)/max(abs(T11), abs(T22))
rec("R2", "composite's fixed-point tidal (k=(1,1,0,0), coordinate e_y,e_z, linearised metric, M=-2e-3, b=0.3), EXACT: "
    "T_yy=%.6e T_zz=%.6e |trace|/max=%.4e  (composite prints 1.6e-4 residue, tolerance 5e-4)" % (T11, T22, ratio_comp))
# proper null k and orthonormal screen at that point
Phi0 = -Mv/sp.Rational(3, 10)
kn = [1, sp.sqrt((1 + 2*Phi0)/(1 - 2*Phi0)), 0, 0]
nrm = 1/sp.sqrt(1 - 2*Phi0)
T11n = -Rlow_num(g, Rup, Mv, p, kn, [0, 0, nrm, 0]); T22n = -Rlow_num(g, Rup, Mv, p, kn, [0, 0, 0, nrm])
ratio_null = abs(T11n + T22n)/max(abs(T11n), abs(T22n))
# R_kk of the linearised metric with the null k
Rkk = sp.N(sum(Ric[i, j].subs({M: Mv, t: 0, x: 0, y: p[1], z: 0})*kn[i]*kn[j] for i in range(4) for j in range(4)), 30)
rec("R2", "same point with a TRUE null k and an orthonormal screen: |trace|/max=%.4e;  R_kk (exact, linearised metric)=%.4e;"
    " Weyl scale 3|M|/b^3=%.4e; ratio R_kk/max|T| = %.4e" % (ratio_null, Rkk, 3*abs(Mv)/sp.Rational(27, 1000), abs(Rkk)/max(abs(T11n), abs(T22n))))
# same with exact Schwarzschild
T11s = -Rlow_num(gS, RupS, Mv, p, [1, sp.sqrt(A_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv)/B_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv)), 0, 0], [0, 0, 1/sp.sqrt(B_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv)), 0])
T22s = -Rlow_num(gS, RupS, Mv, p, [1, sp.sqrt(A_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv)/B_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv)), 0, 0], [0, 0, 0, 1/sp.sqrt(B_ex.subs(rr, sp.Rational(3, 10)).subs(M, Mv))])
rec("R2", "exact Schwarzschild, null k, orthonormal screen: |trace|/max=%.3e (vacuum: exactly traceless)" % (abs(T11s + T22s)/max(abs(T11s), abs(T22s))))
R2 = dict(comp=float(ratio_comp), null=float(ratio_null), Rkk=float(Rkk))

# ------------------------------------------------------------------ R3 deflection (mpmath)
mp.mp.dps = 40
def deflection(n2, b):
    # ray in optical metric n^2(dr^2 + r^2 dphi^2); n r sin(psi) = b.  turning point n(r0) r0 = b.
    f = lambda rr_: mp.sqrt(n2(rr_))*rr_ - b
    r0 = mp.findroot(f, b)
    # substitute r = r0/u, u in (0,1]
    def integrand(u):
        rr_ = r0/u
        return b/(r0*mp.sqrt(n2(rr_)*rr_**2 - b**2)) * r0  # dr/r^2 * r^2 ... see below
    # phi = int_{r0}^inf b dr / (r sqrt(n^2 r^2 - b^2)); with r=r0/u, dr = -r0 du/u^2, 1/r = u/r0
    g_ = lambda u: b/(u*mp.sqrt(n2(r0/u)*(r0/u)**2 - b**2)) * (1/u) * u  # = b /(u * sqrt(...)) * (r0 du/u^2)*(u/r0)
    val = mp.quad(lambda u: b/(u*mp.sqrt(n2(r0/u)*(r0/u)**2 - b**2)), [0, 1 - mp.mpf('1e-30')*0, 1])
    return 2*val - mp.pi

def n2_lin(Mv):
    return lambda rr_: (1 + 2*Mv/rr_)/(1 - 2*Mv/rr_)
def n2_ex(Mv):
    return lambda rr_: (1 + Mv/(2*rr_))**6/(1 - Mv/(2*rr_))**2

R3 = {}
for lab, n2f in (("linearised", n2_lin), ("exact", n2_ex)):
    for sgn in (1, -1):
        c2s = []
        for q in (mp.mpf('1e-3'), mp.mpf('5e-4')):
            Mv_ = sgn*q
            a = deflection(n2f(Mv_), mp.mpf(1))
            c2s.append((a - 4*Mv_)/Mv_**2)
        R3[(lab, sgn)] = c2s
        rec("R3", "%-10s M %s0: (alpha - 4M/b)/(M/b)^2 at M/b=1e-3, 5e-4 -> %s, %s  (15pi/4=%s)"
            % (lab, "+" if sgn > 0 else "-", mp.nstr(c2s[0], 8), mp.nstr(c2s[1], 8), mp.nstr(15*mp.pi/4, 8)))
# large |M|/b as at composite's window top (|M|=4e-2, b=0.3)
for Mv_ in (mp.mpf('-0.04'), mp.mpf('-0.01'), mp.mpf('-0.002')):
    al = deflection(n2_lin(Mv_/mp.mpf('0.3')), 1); ae = deflection(n2_ex(Mv_/mp.mpf('0.3')), 1)
    rec("R3", "M=%s b=0.3: deflection linearised %s rad, exact Schwarzschild %s rad, 4M/b %s; lin/exact-1 = %s"
        % (mp.nstr(Mv_, 3), mp.nstr(al, 8), mp.nstr(ae, 8), mp.nstr(4*Mv_/mp.mpf('0.3'), 8), mp.nstr(al/ae - 1, 4)))

# ------------------------------------------------------------------ R4 composite window, two metrics
def funcs(kind, Mv):
    if kind == "lin":
        A = lambda R: 1 - 2*Mv/R;      dA = lambda R: 2*Mv/R**2
        B = lambda R: 1 + 2*Mv/R;      dB = lambda R: -2*Mv/R**2
    else:
        q = lambda R: Mv/(2*R)
        A = lambda R: ((1 - q(R))/(1 + q(R)))**2
        dA = lambda R: 2*((1 - q(R))/(1 + q(R))) * (Mv/(2*R**2)) * 2/(1 + q(R))**2
        B = lambda R: (1 + q(R))**4
        dB = lambda R: 4*(1 + q(R))**3 * (-Mv/(2*R**2))
    return A, dA, B, dB

def rhs_factory(kind, Mv):
    A, dA, B, dB = funcs(kind, Mv)
    def rhs(lam, s):
        tt, x1, x2, x3, kt, k1, k2, k3 = s
        R = math.sqrt(x1*x1 + x2*x2 + x3*x3)
        n = (x1/R, x2/R, x3/R)
        kv = (k1, k2, k3)
        nk = n[0]*k1 + n[1]*k2 + n[2]*k3
        kk = k1*k1 + k2*k2 + k3*k3
        a_, da, b_, db = A(R), dA(R), B(R), dB(R)
        at = -(da/a_)*nk*kt
        ai = [-(da/(2*b_))*n[i]*kt*kt - (1/(2*b_))*(2*db*nk*kv[i] - db*n[i]*kk) for i in range(3)]
        return [kt, k1, k2, k3, at, ai[0], ai[1], ai[2]]
    return rhs, A, B

def launch(kind, Mv, p0, d):
    rhs, A, B = rhs_factory(kind, Mv)
    R0 = math.sqrt(sum(c*c for c in p0))
    nd = math.sqrt(sum(c*c for c in d))
    s = math.sqrt(A(R0)/B(R0))
    return rhs, [0.0, p0[0], p0[1], p0[2], 1.0, s*d[0]/nd, s*d[1]/nd, s*d[2]/nd]

def run(kind, Mv, b=0.3, x0=-40.0, lam=75.0, n=900, dth=1e-6):
    lam_end = lam*(n - 1)/n                    # composite records pts before the last step
    grid = np.linspace(0, lam_end, 6001)
    sols = {}
    for key, d in (("0", (1, 0, 0)), ("y", (1, dth, 0)), ("z", (1, 0, dth))):
        rhs, s0 = launch(kind, Mv, (x0, b, 0.0), d)
        sol = solve_ivp(rhs, (0, lam_end), s0, t_eval=grid, rtol=1e-12, atol=1e-14, method="DOP853")
        sols[key] = sol.y
    Y0 = sols["0"]
    # transverse separations, projected orthogonal to the spatial tangent of the base ray
    Jy, Jz = [], []
    for j in range(len(grid)):
        kt_ = Y0[5:8, j]; kh = kt_/np.linalg.norm(kt_)
        dy = sols["y"][1:4, j] - Y0[1:4, j]
        dz = sols["z"][1:4, j] - Y0[1:4, j]
        dyp = dy - np.dot(dy, kh)*kh
        # in-plane transverse direction (in the x-y plane, perpendicular to kh)
        ey = np.array([-kh[1], kh[0], 0.0]); ey /= np.linalg.norm(ey)
        Jy.append(np.dot(dyp, ey)); Jz.append(dz[2])
    Jy, Jz = np.array(Jy), np.array(Jz)
    det = Jy*Jz
    conj = None
    for j in range(20, len(grid)):
        if det[j] <= 0:
            conj = grid[j]; break
    dt = Y0[0, -1] - Y0[0, 0]
    dx = np.linalg.norm(Y0[1:4, -1] - Y0[1:4, 0])
    rmin = min(np.linalg.norm(Y0[1:4, j]) for j in range(len(grid)))
    return dict(conj=conj, delay=dt - dx, seats=conj is not None, early=(dt - dx) < 0, rmin=rmin)

composite_printed = {-2e-3: (56.50, -3.7618e-2), 2e-3: (55.17, 5.1227e-2), -5e-4: (None, -1.0616e-2),
                     -1e-2: (42.83, -7.9680e-2), -4e-2: (40.83, 6.1601e-1)}
R4 = {}
rec("R4", "%9s | %-28s | %-28s | %s" % ("M", "linearised: conj, t-|dx|", "exact Schw.: conj, t-|dx|", "composite printed"))
for Mv in (2e-3, -5e-4, -2e-3, -1e-2, -2e-2, -4e-2):
    L = run("lin", Mv); E = run("ex", Mv)
    R4[Mv] = (L, E)
    f = lambda rr_: ("%6.2f" % rr_["conj"] if rr_["conj"] else "  none") + " %+12.5e" % rr_["delay"]
    cp = composite_printed.get(Mv)
    rec("R4", "%9.1e | %-28s | %-28s | %s" % (Mv, f(L), f(E), cp))

def edge(kind, pred, lo, hi, it=30):
    # pred(|M|) switches from False at lo to True at hi
    for _ in range(it):
        mid = math.sqrt(lo*hi)
        if pred(mid): hi = mid
        else: lo = mid
    return math.sqrt(lo*hi)

edges = {}
for kind in ("lin", "ex"):
    lower = edge(kind, lambda m: run(kind, -m)["seats"], 5e-4, 2e-3, it=18)
    upper = edge(kind, lambda m: not run(kind, -m)["early"], 1e-2, 4e-2, it=18)
    edges[kind] = (lower, upper)
    rec("R4", "%s: window lower edge (seats within lam) |M|=%.4e, upper edge (delay changes sign) |M|=%.4e; Phi(b) at upper edge = %.3f"
        % ("linearised" if kind == "lin" else "exact Schwarzschild (isotropic)", lower, upper, upper/0.3))
rec("R4", "edge shift exact/linearised: lower %.4f, upper %.4f" % (edges["ex"][0]/edges["lin"][0], edges["ex"][1]/edges["lin"][1]))

# ------------------------------------------------------------------ R5 concentric Phi along the ray
A_CORE, R_SH, B_RAY = 0.02, 200.0, 1.0
for m in (5e-3, 4e-2):
    phi_c = lambda rr_: m/math.sqrt(rr_*rr_ + A_CORE**2) - m/max(rr_, R_SH)
    along = max(abs(phi_c(math.hypot(xx, B_RAY))) for xx in np.linspace(-150, 150, 30001))
    rec("R5", "concentric m=%.0e: Phi at core centre %.4f (m/a - m/R_s); max |Phi| along the b=1 corridor ray %.4e"
        % (m, phi_c(0.0), along))

# ------------------------------------------------------------------ R6 concentric core: is the linearised metric Lorentzian?
mstar = 0.5/(1/A_CORE - 1/R_SH)
rec("R6", "concentric: g_ii = 1-2Phi vanishes at the core centre once m >= %.6f (Phi(0)=1/2); its stated window runs 5e-3 to 4e-2" % mstar)
for m in (5e-3, 1e-2, 2e-2, 4e-2):
    ph0 = m/A_CORE - m/R_SH
    if ph0 > 0.5:
        s_ = m/(0.5 + m/R_SH); rst = math.sqrt(max(s_*s_ - A_CORE**2, 0.0))
        rec("R6", "  m=%.0e: Phi(0)=%.4f, g_tt(0)=%.3f, g_ii(0)=%.3f -> spatial metric NEGATIVE inside r*=%.4f (ray at b=1 never enters)" % (m, ph0, -(1+2*ph0), 1-2*ph0, rst))
    else:
        rec("R6", "  m=%.0e: Phi(0)=%.4f, g_ii(0)=%.3f (Lorentzian, |Phi| not small)" % (m, ph0, 1-2*ph0))

# ------------------------------------------------------------------ R2b composite's own residue vs finite-difference step (read-only import)
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
try:
    import composite as _c
    for h in (3e-3, 1e-3, 3e-4, 1e-4):
        Rl = _c.riemann_lower((0.0, 0.3, 0.0), -2e-3, h=h)
        k_ = [1., 1., 0, 0]; E_ = ([0, 0, 1., 0], [0, 0, 0, 1.])
        T_ = [-sum(Rl[m_][a][n_][b_]*k_[m_]*E_[i][a]*k_[n_]*E_[i][b_] for m_ in range(4) for a in range(4) for n_ in range(4) for b_ in range(4)) for i in range(2)]
        rec("R2b", "composite.riemann_lower step h=%.0e: |trace|/max = %.4e  (exact limit, R2: %.4e)" % (h, abs(T_[0]+T_[1])/max(map(abs, T_)), R2["comp"]))
    rec("R2b", "composite.survey(2e-3) along-ray traceless_ratio = %.4e  (R2 proper-null-frame O(Phi^2) Ricci ratio at closest approach: %.4e)" % (_c.survey(2e-3)["traceless_ratio"], R2["null"]))
except Exception as ex:
    rec("R2b", "composite import failed: %r" % ex)
print("\nDONE")
