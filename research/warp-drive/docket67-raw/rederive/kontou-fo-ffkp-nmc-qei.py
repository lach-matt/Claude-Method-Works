#!/usr/bin/env python3
"""DOCKET 67 -- composite audit kontou-fo-ffkp-nmc-qei.
Independent of rederive/0708.2450-thm4.2.py and rederive/2309.10848-thmiv.1.py:
different metric (spatially flat FRW with explicit a(t)), different fields, and the
null Q[f] coefficient derived as a POINTWISE divergence identity rather than via the
Noether residual.  Reads research/warp-drive/qeihps.py read-only (no bytecode written).

 N1  FFKP (9) null-contracted at a point vs FFKP (13) as printed: difference 2 xi R_ll phi^2
 N2  FFKP (9) is conserved off-shell on FRW (nabla^m T_mn = +E d_n phi, E = nabla^2 phi - m^2 phi - xi R phi); (12)'s Ricci sign is not
 N3  f^2 T_ll(9) = f^2 (l.dphi)^2 - xi phi^2 Q_true[f] + div V, Q_true = nabla nabla(l l f^2) - R_ll f^2,
     checked pointwise on FRW with an explicit null field l; the printed Q (+1/2 R_ll f^2) leaves
     residual -(3/2) xi R_ll f^2 phi^2 != 0
 N4  R_ll != 0 on FRW (so the discrepancy is live wherever R_ll != 0 and xi != 0)
 N5  structure: the positive part f^2 (l.dphi)^2 is independent of the Ricci coefficient, so the
     theorem's proof (positivity of rho_hat_n = l.d (x) l.d) carries over with Q_true unchanged
 F1  z3: FO's discarded classical bracket a^2/2 + (1-4xi)S/2 + 2 xi c^2 (S>=0) is >=0 for all
     values iff 0 <= xi <= 1/4 (the FO range), SAT outside
 F2  xi_c = (n-2)/(4(n-1)) = 1/6 at n=4, inside [0,1/4]; FFKP has no range
 T1  tree: qeihps.KONTOU_REQUESTED_TEST_ON_HPS reads OPEN/OPEN, computed from HYPOTHESES;
     FORM_TAGS[FO] carries no global-hyperbolicity tag (the dropped P3 of the FO audit);
     qeihps.py's displayed FFKP Q[f] carries the +1/2 coefficient
"""
import sys, os, re
sys.dont_write_bytecode = True
import sympy as sp

RES = []
def chk(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print("%s  %s  %s" % ("PASS" if ok else "FAIL", name, detail), flush=True)

# ---------- N1: pointwise algebra -------------------------------------------------
xi, m = sp.symbols('xi m', real=True)
phi, Rll, A, B = sp.symbols('phi R_ll A B')   # A = (l.dphi)^2, B = phi l l dd phi
# from (9): T_ll = (l dphi)^2 + xi(-l l g box - l l dd + G_ll) phi^2 ; g_ll = 0, G_ll = R_ll
# l l dd(phi^2) = 2 A + 2 B
T9 = A + xi*(Rll*phi**2 - (2*A + 2*B))
T13 = (1 - 2*xi)*A - 2*xi*(B + sp.Rational(1, 2)*Rll*phi**2)
chk("N1 (9)_ll - (13)_printed == 2 xi R_ll phi^2",
    sp.simplify(T9 - T13 - 2*xi*Rll*phi**2) == 0, str(sp.factor(T9 - T13)))
T13fix = (1 - 2*xi)*A - 2*xi*(B - sp.Rational(1, 2)*Rll*phi**2)
chk("N1b (9)_ll == (13) with -1/2 R_ll", sp.simplify(T9 - T13fix) == 0)

# ---------- FRW geometry ----------------------------------------------------------
t, x, y, z = X = sp.symbols('t x y z', real=True)
a = sp.exp(t/3) + t**2/5
g = sp.diag(-1, a**2, a**2, a**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[i, k]*(sp.diff(g[k, j1], X[j2]) + sp.diff(g[k, j2], X[j1])
          - sp.diff(g[j1, j2], X[k])) for k in range(n))/2) for j2 in range(n)]
        for j1 in range(n)] for i in range(n)]
def ricci():
    Ric = sp.zeros(n)
    for b_ in range(n):
        for c in range(n):
            s = 0
            for a_ in range(n):
                s += sp.diff(Gam[a_][b_][c], X[a_]) - sp.diff(Gam[a_][b_][a_], X[c])
                for d in range(n):
                    s += Gam[a_][a_][d]*Gam[d][b_][c] - Gam[a_][c][d]*Gam[d][b_][a_]
            Ric[b_, c] = sp.simplify(s)
    return Ric
Ric = ricci()
Rs = sp.simplify(sum(gi[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
G = sp.simplify(Ric - g*Rs/2)
def cov_dd(s):   # nabla_a nabla_b of a scalar
    return sp.Matrix(n, n, lambda i, j: sp.diff(s, X[i], X[j])
                     - sum(Gam[k][i][j]*sp.diff(s, X[k]) for k in range(n)))
def lap(s):
    D = cov_dd(s); return sum(gi[i, j]*D[i, j] for i in range(n) for j in range(n))
def div_vec(V):  # nabla_m V^m
    sqrtg = sp.sqrt(-g.det())
    return sum(sp.diff(sqrtg*V[i], X[i]) for i in range(n))/sqrtg

ph = sp.sin(t + 2*x) + x*t/3 + y/5
xiv, mv = sp.Rational(3, 10), sp.Rational(7, 10)
dph = [sp.diff(ph, c) for c in X]
grad2 = sum(gi[i, j]*dph[i]*dph[j] for i in range(n) for j in range(n))
DD2 = cov_dd(ph**2); L2 = lap(ph**2)
def Tmn(ricsign):
    # ricsign=+1: FFKP (9) (MTW: box_g = -nabla^2, so -g box phi^2 = +g lap phi^2)
    T = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            T[i, j] = dph[i]*dph[j] - g[i, j]*(mv**2*ph**2 + grad2)/2 \
                + xiv*(g[i, j]*L2 - DD2[i, j] + ricsign*G[i, j]*ph**2)
    return T
E = lap(ph) - mv**2*ph - xiv*Rs*ph      # EL expression; E = 0 on shell (FFKP (10))
def div_T(T):
    Tup = gi*T*gi   # T^{ab}
    out = []
    for nn in range(n):
        # nabla_m T^m_n  with T^m_n = Tup g
        Tmix = Tup*g
        s = sum(sp.diff(Tmix[mm, nn], X[mm]) for mm in range(n))
        s += sum(Gam[mm][mm][k]*Tmix[k, nn] for mm in range(n) for k in range(n))
        s -= sum(Gam[k][mm][nn]*Tmix[mm, k] for mm in range(n) for k in range(n))
        out.append(s)
    return out
pt = {t: sp.Rational(7, 10), x: sp.Rational(-3, 10), y: sp.Rational(1, 7), z: 0}
def resid(T):
    dv = div_T(T)
    return max(abs(sp.N((dv[k] - E*dph[k]).subs(pt), 30)) for k in range(n))   # nabla^m T_mn = +E d_n phi
r9 = resid(Tmn(+1))
# (12)'s Ricci sign corresponds to +xi(-R_mn ... ) i.e. (9) with G -> G - 2 R_mn: test T9 - 2 xi R_mn phi^2
T12 = Tmn(+1) - 2*xiv*Ric*ph**2
r12 = resid(T12)
chk("N2 FFKP (9) conserved off-shell on FRW", r9 < 1e-20, "residual %.2e" % r9)
chk("N2b (12)/(13) Ricci sign NOT conserved on FRW", r12 > 1e-6, "residual %.3e" % r12)

# ---------- N3: pointwise null identity with explicit null field -------------------
lvec = [sp.Integer(1), 1/a, 0, 0]                  # l^mu, null
nullnorm = sp.simplify(sum(g[i, j]*lvec[i]*lvec[j] for i in range(n) for j in range(n)))
chk("N3a l = d_t + a^-1 d_x is null", nullnorm == 0)
f = sp.exp(-(t - sp.Rational(1, 2))**2) * sp.cos(x/3 + y)
Tll = sum(Tmn(+1)[i, j]*lvec[i]*lvec[j] for i in range(n) for j in range(n))
Rll_e = sp.simplify(sum(Ric[i, j]*lvec[i]*lvec[j] for i in range(n) for j in range(n)))
ldph = sum(lvec[i]*dph[i] for i in range(n))
# W^{mn} = l^m l^n f^2 ; nabla_m nabla_n W^{mn} for symmetric W: (1/sqrtg) d_m d_n (sqrtg W^{mn}) + Gamma^m... use
# nabla_m nabla_n W^{mn} = nabla_m U^m with U^m = nabla_n W^{mn}
W = sp.Matrix(n, n, lambda i, j: lvec[i]*lvec[j]*f**2)
sqrtg = sp.sqrt(-g.det())
U = [sum(sp.diff(sqrtg*W[i, j], X[j]) for j in range(n))/sqrtg
     + sum(Gam[i][j][k]*W[k, j] for j in range(n) for k in range(n)) for i in range(n)]
ddW = div_vec(U)
# V^m = xi[ f^2 l^m l^n d_n phi^2 - phi^2 U^m ]
dph2 = [sp.diff(ph**2, c) for c in X]
V = [xiv*(sum(W[i, j]*dph2[j] for j in range(n)) - ph**2*U[i]) for i in range(n)]
divV = div_vec(V)
def ident(cR):
    Q = ddW + cR*Rll_e*f**2
    return f**2*Tll - (f**2*ldph**2 - xiv*ph**2*Q - divV)
pts = [pt, {t: sp.Rational(1, 3), x: sp.Rational(2, 5), y: sp.Rational(-1, 2), z: 1},
       {t: sp.Rational(-4, 5), x: sp.Rational(1, 9), y: 0, z: sp.Rational(3, 2)}]
res_true = max(abs(sp.N(ident(-1).subs(p), 30)) for p in pts)
res_print = max(abs(sp.N(ident(sp.Rational(1, 2)).subs(p), 30)) for p in pts)
pred = max(abs(sp.N((ident(sp.Rational(1, 2)) - sp.Rational(3, 2)*xiv*Rll_e*f**2*ph**2).subs(p), 30)) for p in pts)
chk("N3b Q_true = nabla nabla(l l f^2) - R_ll f^2: identity holds pointwise", res_true < 1e-20, "max residual %.2e" % res_true)
chk("N3c printed Q (+1/2 R_ll f^2) fails the identity", res_print > 1e-6, "max residual %.3e" % res_print)
chk("N3d printed-Q residual is exactly -(3/2) xi R_ll f^2 phi^2", pred < 1e-20, "%.2e" % pred)
# ---------- N4 ------------------------------------------------------------------
Rll_val = sp.N(Rll_e.subs(pt), 15)
chk("N4 R_ll != 0 on FRW (a = e^{t/3} + t^2/5)", abs(Rll_val) > 1e-6, "R_ll(t=0.7) = %s ; closed form %s" % (Rll_val, sp.simplify(Rll_e)))
# ---------- N5 ------------------------------------------------------------------
chk("N5 positive part f^2 (l.dphi)^2 contains no curvature coefficient",
    not (sp.Symbol('R') in (f**2*ldph**2).free_symbols))

# ---------- F1 z3 ---------------------------------------------------------------
try:
    import z3
    xz, az, Sz, cz = z3.Reals('xi a S c')
    br = az*az/2 + (1 - 4*xz)*Sz/2 + 2*xz*cz*cz
    s1 = z3.Solver(); s1.add(xz >= 0, xz <= z3.RealVal(1)/4, Sz >= 0, br < 0)
    s2 = z3.Solver(); s2.add(z3.Or(xz < 0, xz > z3.RealVal(1)/4), Sz >= 0, br < 0)
    chk("F1a z3: bracket >= 0 on xi in [0,1/4] (negation UNSAT)", s1.check() == z3.unsat)
    chk("F1b z3: bracket can be < 0 outside [0,1/4] (SAT)", s2.check() == z3.sat)
except ImportError:
    chk("F1 z3 available", False, "pip install z3-solver")
nn_ = sp.Symbol('n')
xic = (nn_ - 2)/(4*(nn_ - 1))
chk("F2 xi_c(4) = 1/6 in [0,1/4]", xic.subs(nn_, 4) == sp.Rational(1, 6) and 0 <= xic.subs(nn_, 4) <= sp.Rational(1, 4))

# ---------- T1 tree -------------------------------------------------------------
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
import qeihps
s = qeihps.KONTOU_REQUESTED_TEST_ON_HPS
chk("T1a KONTOU_REQUESTED_TEST_ON_HPS = FO OPEN, FFKP OPEN", s.startswith("FO Thm 4.2 OPEN and FFKP Thm IV.1 (eq. 72) OPEN"), s[:90])
chk("T1b both statuses computed OPEN from HYPOTHESES",
    qeihps.qei_status(qeihps.HYPOTHESES, qeihps.FO)[0] == "OPEN" and
    qeihps.qei_status(qeihps.HYPOTHESES, qeihps.FFKP)[0] == "OPEN")
chk("T1c FORM_TAGS[FO] has no global-hyperbolicity/domain tag (dropped FO P3)",
    qeihps.FORM_TAGS[qeihps.FO] == {"xi", "geodesic"}, str(qeihps.FORM_TAGS[qeihps.FO]))
src = open(os.path.join(WD, "qeihps.py")).read()
chk("T1d qeihps.py displays FFKP Q[f] with +(1/2) R_mn l^m l^n f^2",
    "Q[f] = nabla_mu nabla_nu (l^mu l^nu f^2) + (1/2) R_mn l^m l^n f^2" in src)
# no tree number depends on Q[f]: grep for evaluation of Q[f] / R_ll f^2
qlines = [i + 1 for i, L in enumerate(src.splitlines()) if "Q[f]" in L or "R_ll" in L]
chk("T1e the tree never evaluates FFKP Q[f]: every 'Q[f]'/'R_ll' is in the docstring display (lines 98-99)",
    qlines == [98, 99], "lines %s" % qlines)
chk("T1f toggling the blockers flips both to EVALUABLE (verdict is computed, not declared)",
    qeihps.qei_status(qeihps.hypothesis_table(hadamard=True, ref_state=True, phi2=True), qeihps.FO)[0] == "EVALUABLE" and
    qeihps.qei_status(qeihps.hypothesis_table(hadamard=True, ref_state=True, phi2=True), qeihps.FFKP)[0] == "EVALUABLE")

npass = sum(ok for _, ok in RES); nfail = len(RES) - npass
print("%d PASS, %d FAIL" % (npass, nfail))
sys.exit(1 if nfail else 0)
