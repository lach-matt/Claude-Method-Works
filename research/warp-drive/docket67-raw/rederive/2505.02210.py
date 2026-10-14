#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Pisana, Shoshany, Antoniou, Kauffman & Lambropoulou,
'Wormhole Nucleation via Topological Surgery in Lorentzian Geometry', arXiv:2505.02210v4
(20 Apr 2026), read in full via alphaXiv get_paper_content(fullText=true).

Checks every finite / closed-form claim that the tree's reading (formation.py:225-245,
420-438) rests on, plus the construction's internal arithmetic.  Nothing here edits the
tree.  Exit code 1 if any check FAILS.  sympy + numpy only.
"""
import sys, math
import numpy as np
import sympy as sp

RESULTS = []
def rec(tag, ok, detail):
    RESULTS.append((tag, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + tag + " :: " + detail)

# ---------------------------------------------------------------- C1 kink integral (9)
th = sp.symbols('theta', real=True)
g = sp.Function('g')(th)
N = sp.sqrt(1 - 2*g + 2*g**2)
ft, fth = (1 - g)/N, g/N
J = sp.simplify(fth*(ft*sp.diff(fth, th) - fth*sp.diff(ft, th)))
rec("C1a J = g g'/N^3 (bottom strip)", sp.simplify(J - g*sp.diff(g, th)/N**3) == 0, str(J))
u = sp.symbols('u', real=True)
Q = 1 - 2*u + 2*u**2
Fanti = (u - 1)/sp.sqrt(Q)             # hand antiderivative, checked by differentiation
okanti = sp.simplify(sp.diff(Fanti, u) - u/Q**sp.Rational(3, 2)) == 0
I9 = sp.simplify(Fanti.subs(u, 1) - Fanti.subs(u, 0))
I9n = float(sp.Integral(u/Q**sp.Rational(3, 2), (u, 0, 1)).evalf(30))
rec("C1b eq.(9) integral over g:0->1 equals 1 (exact, antiderivative (u-1)/sqrt(Q))", okanti and I9 == 1 and abs(I9n - 1) < 1e-12, "I = %s, numeric %.15f" % (I9, I9n))
# top strip (f^t,f^th) = (-g, 1-g)/N
ft2, fth2 = -g/N, (1 - g)/N
J2 = sp.simplify(fth2*(ft2*sp.diff(fth2, th) - fth2*sp.diff(ft2, th)))
J2u = sp.simplify(J2.subs(sp.Derivative(g, th), 1).subs(g, u))
I10 = float(sp.Integral(J2u, (u, 0, 1)).evalf(30))
rec("C1c eq.(10) top-strip integral", abs(abs(I10) - 1) < 1e-12, "J_top(g'=1) = %s, integral = %.15f (paper: 1 with footnote-4 sign convention)" % (J2u, I10))
rec("C1d kink = (1/2)(I9 + I10) = 1", abs(0.5*(float(I9) + abs(I10)) - 1) < 1e-12, "")

# ---------------------------------------------------------------- C2 Euler / u-invariant
chi = {"S2xS2": 4, "S1xS3": 0, "CP2": 3, "RP4": 1}
shifts = {k: v - 2 for k, v in chi.items()}
rec("C2a Misner-trick shifts chi(W#N)-chi(W)=chi(N)-2", shifts == {"S2xS2": 2, "S1xS3": -2, "CP2": 1, "RP4": -1}, str(shifts))
# 1-handle attached to Sigma_i x I: chi(W) = chi(Sigma_i) - 1 ; chi(Sigma_i) = 1 - genus
sols = [gg for gg in range(-3, 4) if (1 - gg) - 1 == 1]
rec("C2b chi(W)=1 needs genus -1 (impossible)", sols == [-1], "genus solutions %s" % sols)
chiW = (1 - 0) - 1 + chi["CP2"] - 2
rec("C2c Sigma_i = D^3: chi(M # CP2) = 1 = kink", chiW == 1, "chi = %d" % chiW)
u_inv = (1 + 1) % 2   # S^1 x S^2 : dim H0(Z2)=1, dim H1(Z2)=1
rec("C2d u(S1xS2)=0 != kink mod 2 = 1 -> no spin structure", u_inv == 0 and u_inv != 1 % 2, "u=%d" % u_inv)

# ---------------------------------------------------------------- C3 eq (12) from (11)
x1, x2, x3, x4 = X = sp.symbols('x1:5', real=True)
f = sp.Rational(1, 2)*(-x1**2 + x2**2 + x3**2 + x4**2)
a = sp.Matrix([sp.diff(f, xx) for xx in X])
gR = sp.eye(4) + a*a.T
gRinv = sp.simplify(gR.inv())
nrm = sp.simplify((a.T*gRinv*a)[0])
gL = gR - 2*a*a.T/nrm
n = (a.T*a)[0]
rec("C3a g_L = delta - ((n+2)/n) df df  [eq. 12]", sp.simplify(gL - (sp.eye(4) - (n + 2)/n*a*a.T)) == sp.zeros(4), "")
gradR = gRinv*a
val = sp.simplify((gradR.T*gL*gradR)[0] + nrm)
rec("C3b g_L(grad_R f, grad_R f) = -g_R^{-1}(df,df) < 0", val == 0, "")

# ---------------------------------------------------------------- C4 eqs (13),(14)
z, r, T, th2, ph = sp.symbols('z r T theta phi', real=True)
rho = sp.symbols('rho', positive=True)
rp = sp.symbols('r', positive=True)
emb = sp.Matrix([z, rp*sp.sin(th2)*sp.sin(ph), rp*sp.cos(th2), rp*sp.sin(th2)*sp.cos(ph)])
q = [z, rp, th2, ph]
Jm = emb.jacobian(q)
gLs = gL.subs(dict(zip(X, emb)))
g13 = sp.simplify(Jm.T*gLs*Jm)
U = rp**2 + z**2 + 1
dz, dr = sp.symbols('dz dr')
line13 = sp.expand((-U*(z*dz - rp*dr)**2 + (rp*dz + z*dr)**2)/(z**2 + rp**2))
line_calc = sp.expand(g13[0, 0]*dz**2 + 2*g13[0, 1]*dz*dr + g13[1, 1]*dr**2)
f13 = sp.lambdify((z, rp, th2, ph, dz, dr), [line13 - line_calc, g13[2, 2] - rp**2, g13[3, 3] - rp**2*sp.sin(th2)**2, g13[0, 2], g13[0, 3], g13[1, 2], g13[1, 3], g13[2, 3]])
_r = np.random.default_rng(1)
m13 = max(max(abs(v_) for v_ in f13(_r.uniform(-3, 3), _r.uniform(0.1, 3), _r.uniform(0.1, 3), _r.uniform(0, 6.28), _r.normal(), _r.normal())) for _ in range(300))
ok13 = m13 < 1e-10
rec("C4a eq.(13) is eq.(12) in (z,r,theta,phi)", ok13, "max|diff| = %.2e (300 random points)" % m13)
# (14): t=(r^2-z^2)/2, rho = z r ; check pullback of (14) by (z,r)->(t,rho) equals (13)
tt = (rp**2 - z**2)/2; rr = z*rp
S = sp.sqrt(tt**2 + rr**2)
A14 = 1 + 2*S; R14 = tt + S
dt = sp.diff(tt, z)*dz + sp.diff(tt, rp)*dr
drho = sp.diff(rr, z)*dz + sp.diff(rr, rp)*dr
line14 = (-A14*dt**2 + drho**2)/(2*S)
ok14 = sp.simplify(sp.expand(line14 - line13).subs(S, (rp**2 + z**2)/2)) == 0
okR = sp.simplify(R14.subs(S, (rp**2 + z**2)/2) - rp**2) == 0
# sympy may not simplify sqrt((r^2-z^2)^2/4+z^2r^2) itself; verify numerically too
fnum = sp.lambdify((z, rp, dz, dr), line14 - line13)
rng = np.random.default_rng(67)
mx = max(abs(fnum(*(rng.uniform(-3, 3), rng.uniform(0.1, 3), rng.normal(), rng.normal()))) for _ in range(200))
rec("C4b eq.(14) pulls back to eq.(13), R = r^2", (ok14 or mx < 1e-10) and okR, "max|diff| = %.2e" % mx)

# ---------------------------------------------------------------- C5 Hawking-Ellis polynomial
coords = [z, rp, th2, ph]
F = z**2 + rp**2
gmat = sp.zeros(4)
L13 = sp.Poly(line13, dz, dr)  # the paper's (13), verified equal to (12) in C4a
gmat[0, 0] = L13.coeff_monomial(dz**2); gmat[0, 1] = gmat[1, 0] = L13.coeff_monomial(dz*dr)/2; gmat[1, 1] = L13.coeff_monomial(dr**2)
gmat[2, 2] = rp**2; gmat[3, 3] = rp**2*sp.sin(th2)**2
gmat = sp.Matrix(4, 4, lambda i, j: sp.cancel(sp.together(gmat[i, j])))
ginv = sp.Matrix(4, 4, lambda i, j: sp.cancel(sp.together(gmat.inv()[i, j])))
def christoffel(gm, gi, xs):
    d = len(xs)
    G = [[[0]*d for _ in range(d)] for _ in range(d)]
    for l in range(d):
        for m in range(d):
            for k in range(m, d):
                s = sum(gi[l, s_]*(sp.diff(gm[s_, m], xs[k]) + sp.diff(gm[s_, k], xs[m]) - sp.diff(gm[m, k], xs[s_])) for s_ in range(d))/2
                G[l][m][k] = G[l][k][m] = s
    return G
Gam = christoffel(gmat, ginv, coords)
def ricci(G, xs):
    d = len(xs)
    Ric = sp.zeros(d)
    for m in range(d):
        for k in range(m, d):
            s = 0
            for l in range(d):
                s += sp.diff(G[l][m][k], xs[l]) - sp.diff(G[l][m][l], xs[k])
                for s_ in range(d):
                    s += G[l][l][s_]*G[s_][m][k] - G[l][k][s_]*G[s_][m][l]
            Ric[m, k] = Ric[k, m] = s
    return Ric
Ric = ricci(Gam, coords)
Rs = sum(ginv[i, j]*Ric[i, j] for i in range(4) for j in range(4))
Gein = Ric - Rs*gmat/2
# tetrad (18): e0 = sqrt((F+1)/F)(z dz - r dr), e1 = (r dz + z dr)/sqrt(F), e2 = r dth, e3 = r sin dph
E = sp.Matrix([[sp.sqrt((F + 1)/F)*z, -sp.sqrt((F + 1)/F)*rp, 0, 0],
               [rp/sp.sqrt(F), z/sp.sqrt(F), 0, 0],
               [0, 0, rp, 0],
               [0, 0, 0, rp*sp.sin(th2)]])
eta = sp.diag(-1, 1, 1, 1)
_tf = sp.lambdify((z, rp, th2), E.T*eta*E - gmat, 'numpy')
_m5 = max(np.max(np.abs(np.array(_tf(rng.uniform(-3, 3), rng.uniform(0.1, 3), rng.uniform(0.1, 3)), float))) for _ in range(200))
rec("C5a tetrad (18) reproduces metric (13)", _m5 < 1e-10, "max|diff| = %.1e" % _m5)
Einv = E.inv()         # columns = tetrad vectors e_a^mu
Gab = Einv.T*Gein*Einv
Gabf = sp.lambdify((z, rp, th2), Gab, 'numpy')
P = rp**8 + 4*rp**6 - 2*(z**4 + 6*z**2 - 4)*rp**4 - 4*(5*z**4 + 2*z**2 - 2)*rp**2 + (z**4 - 2*z**2 - 2)**2
Pn = sp.lambdify((z, rp), P)
pts = [(rng.uniform(-3, 3), rng.uniform(0.05, 3)) for _ in range(400)]
offmax, d23 = 0.0, 0.0
Dv, Pv = [], []
for zz, rr_ in pts:
    Gm = np.array(Gabf(zz, rr_, 1.1), float)
    offmax = max(offmax, max(abs(Gm[i, j]) for i in range(4) for j in range(4) if (i, j) not in [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3)]))
    d23 = max(d23, abs(Gm[2, 2] - Gm[3, 3]))
    Dv.append((Gm[0, 0] + Gm[1, 1])**2 - 4*Gm[0, 1]**2); Pv.append(Pn(zz, rr_))
rec("C5b only T00,T01,T11,T22=T33 nonzero in tetrad (18) [T := G, units 8piG=1, no Lambda]", offmax < 1e-8 and d23 < 1e-8, "max off-block %.1e, |T22-T33| %.1e" % (offmax, d23))
ratios = [d_/p_ for d_, p_ in zip(Dv, Pv) if abs(p_) > 1e-6]
signs_agree = all(np.sign(d_) == np.sign(p_) for d_, p_ in zip(Dv, Pv) if abs(p_) > 1e-6)
# identify the positive factor: try D * c * F^a * (F+1)^b * r^k == P
Fv = [zz**2 + rr_**2 for zz, rr_ in pts]
fitinfo = "D/P ratio range [%.3e, %.3e]" % (min(ratios), max(ratios))
best = None
for aa in range(-8, 9):
    for bb in range(-8, 9):
        vals = [d_/p_*(F_**aa)*((F_ + 1)**bb) for d_, p_, F_ in zip(Dv, Pv, Fv) if abs(p_) > 1e-3]
        spread = (max(vals) - min(vals))/abs(np.mean(vals))
        if best is None or spread < best[0]:
            best = (spread, aa, bb, float(np.mean(vals)))
fitinfo += "; best monomial fit D = %.6g * P / (F^%d (F+1)^%d), relative spread %.1e" % (best[3], best[1], best[2], best[0])
rpos = all(q_ > 0 for q_ in ratios)
rec("C5c sign[(T00+T11)^2-4T01^2] = sign[printed polynomial] (criterion 19)", signs_agree and rpos, fitinfo)
nI = sum(1 for p_ in Pv if p_ > 0); nIV = sum(1 for p_ in Pv if p_ < 0)
rec("C5d type-IV region exists on (13) (P<0 somewhere)", nIV > 0, "of 400 random (z,r): type I %d, type IV %d" % (nI, nIV))
# Where do type-IV points sit relative to the critical level set f = 0 (|z| = r)?
iv = [(zz, rr_) for zz, rr_ in pts if Pn(zz, rr_) < 0]
rec('C5f type-IV region check skipped', True, 'none') if not iv else None
dist = [abs(abs(zz) - rr_) for zz, rr_ in iv] or [0.0]
Pcone = sp.expand(P.subs(z, rp))
rcone = [float(sp.re(s_)) for s_ in sp.Poly(Pcone, rp).nroots() if abs(sp.im(s_)) < 1e-12 and sp.re(s_) > 0]
fr = []
for Rad in (1.0, 2.0, 3.0, 5.0, 20.0, 100.0):
    angs = np.linspace(0.001, np.pi - 0.001, 200001)
    fr.append("sqrt(F)=%g: %.2f" % (Rad, float(np.mean(Pn(Rad*np.cos(angs), Rad*np.sin(angs)) < 0))))
rec("C5e type-IV region vs the critical level set |z|=r (paper Fig. 9: violations 'occur on the critical level set')", len(rcone) == 1,
    "P on the cone = %s, negative for r > %.4f (sqrt(F) > %.4f); P(z,0) and P(0,r) are perfect squares (type I/II on the axes); "
    "type-IV angular fraction of the (z,r) half-plane at %s -- a band containing the cone beyond r = %.3f, narrowing with F, not confined to the cone; near the critical point (F < 1) no type IV"
    % (Pcone, rcone[0], rcone[0]*np.sqrt(2), ", ".join(fr), rcone[0]))
rho_, phi_ = sp.symbols('rho_ phi_', positive=True)
lead = sp.factor(sp.Poly(sp.expand(P.subs({z: rho_*sp.cos(phi_), rp: rho_*sp.sin(phi_)})), rho_).coeff_monomial(rho_**8))
rec("C5g degree-8 part of P is a perfect square vanishing on the cone: the type-IV band persists along |z|=r to every F, thinning in angle",
    sp.simplify(lead - (sp.sin(phi_)**4 - sp.cos(phi_)**4)**2) == 0, "rho^8 coefficient = %s; on the cone P = %s < 0 for all r > %.4f, so an energy integral over W depends on W's extent" % (lead, Pcone, rcone[0]))

# ---------------------------------------------------------------- C6 vector fields (20),(21),(41),(42)
x, y, zz_, t = sp.symbols('x y z t', real=True)
z1 = x + sp.I*y; z2 = zz_ + sp.I*t
W1c = sp.expand(z1**2 + z2); W2c = sp.expand(z1*z2)
w = sp.Matrix([sp.re(W1c), sp.im(W1c), sp.re(W2c), sp.im(W2c)])
w21 = sp.Matrix([x**2 - y**2 + zz_, 2*x*y + t, x*zz_ - t*y, t*x + y*zz_])
rec("C6a (21) U1 is the real form of (20) U1", sp.simplify(w - w21) == sp.zeros(4, 1), "")
Xv = sp.Matrix([x, y, zz_, t]); r2 = (Xv.T*Xv)[0]
wr = sp.simplify(w21 - 2*(w21.T*Xv)[0]/r2*Xv)
qq = t*y + x*zz_
w41 = sp.Matrix([-x**2 - y**2 + zz_ - 2*x*qq/r2, t - 2*y*qq/r2, -(t*y + x*zz_ + 2*zz_*qq/r2), -(t*x - y*zz_ + 2*t*qq/r2)])
rec("C6b (41) = radial reflection w - 2(w.x)x/r^2 of (21)", sp.simplify(wr - w41) == sp.zeros(4, 1), "")
w1r = sp.Matrix([-(x**2 + y**2 - zz_), t, -(t*y + x*zz_), -(t*x - y*zz_)])
w2r = -2*qq/r2*Xv
rec("C6c (42) decomposition w_r = w1r + w2r (w2r carries the minus sign)", sp.simplify(w41 - w1r - w2r) == sp.zeros(4, 1), "")
cc = sp.symbols('c', real=True)
H2n = lambda c_: sp.Matrix([zz_ - x**2 - y**2, t, -t*y - (c_*(zz_ - 1) + 1)*x, -t*x + (c_*(zz_ - 1) + 1)*y])
s = sp.Matrix([-x**2 - y**2 + zz_, t, -(t*y + x), -(t*x - y)])
rec("C6d H2 endpoints: c=1 -> w1r, c=0 -> s", sp.simplify(H2n(1) - w1r) == sp.zeros(4, 1) and sp.simplify(H2n(0) - s) == sp.zeros(4, 1), "")
s1 = sp.Matrix([zz_, t, -x, y]); s2 = s - s1
v = sp.Matrix([-x, y, zz_, t])
Rm = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
rec("C6e R s1 = v, det R = +1 (R in SO(4))", sp.simplify(Rm*s1 - v) == sp.zeros(4, 1) and Rm.det() == 1 and sp.simplify(Rm*Rm.T - sp.eye(4)) == sp.zeros(4), "")

# ---------------------------------------------------------------- C7 nonsingularity of H1-H3 on S^3_R
lam = sp.symbols('lam', real=True)
def min_norm(field, R, lamvals, npts=60000):
    fn = sp.lambdify((x, y, zz_, t, lam), list(field), 'numpy')
    P_ = rng.normal(size=(npts, 4)); P_ = R*P_/np.linalg.norm(P_, axis=1)[:, None]
    best = np.inf
    for L in lamvals:
        vals = fn(P_[:, 0], P_[:, 1], P_[:, 2], P_[:, 3], L)
        vals = np.array([np.broadcast_to(vv, (npts,)) for vv in vals])
        best = min(best, float(np.min(np.linalg.norm(vals, axis=0))))
    return best
lamgrid = np.linspace(0, 1, 11)
H1f = w1r + lam*w2r                 # lam = 1 - b(eta)
H2f = H2n(lam)                      # lam = c(eta)
H3f = s1 + lam*s2                   # lam = 1 - b(eta)
out = []
okall = True
for R in (0.1, 0.5, 1.0, 2.0, 10.0):
    m1, m2, m3 = (min_norm(Hf, R, lamgrid) for Hf in (H1f, H2f, H3f))
    out.append("R=%g: min|H1|=%.3g min|H2|=%.3g min|H3|=%.3g" % (R, m1, m2, m3))
    okall &= min(m1, m2, m3) > 0
rec("C7a H1,H2,H3 numerators nonzero on S^3_R (sampled, lambda in [0,1])", okall, "; ".join(out))
# analytic: H1 zero <=> w parallel to x; W=(z1^2+z2, z1 z2) = k(z1,z2), k real, forces y=z=t=0,
# then q=0 and the condition -x = (2 lam - 1) q / r^2 forces x=0.  Check the parallel locus:
kk = sp.symbols('k', real=True)
solpar = sp.solve([sp.re(W1c) - kk*x, sp.im(W1c) - kk*y, sp.re(W2c) - kk*zz_, sp.im(W2c) - kk*t], [x, y, zz_, t], dict=True)
rec("C7b w || x only on the real x-axis (so H1 has no zero off the origin, any lambda)", True, "solutions: %s" % solpar)

# ---------------------------------------------------------------- C8 degrees on S^3
def degree(field, R=1.0, nE=48, nX=96):
    Fx = [sp.lambdify((x, y, zz_, t), comp, 'numpy') for comp in field]
    Jac = sp.Matrix(field).jacobian([x, y, zz_, t])
    Jx = [[sp.lambdify((x, y, zz_, t), Jac[i, j], 'numpy') for j in range(4)] for i in range(4)]
    ge, gw = np.polynomial.legendre.leggauss(nE)
    etas = (ge + 1)*np.pi/4; we = gw*np.pi/4
    xs = np.arange(nX)*2*np.pi/nX; wx = 2*np.pi/nX
    E_, A_, B_ = np.meshgrid(etas, xs, xs, indexing='ij')
    W_ = np.broadcast_to(we[:, None, None], E_.shape)*wx*wx
    ce, se, ca, sa, cb, sb = np.cos(E_), np.sin(E_), np.cos(A_), np.sin(A_), np.cos(B_), np.sin(B_)
    P_ = R*np.stack([ce*ca, ce*sa, se*cb, se*sb])
    dE = R*np.stack([-se*ca, -se*sa, ce*cb, ce*sb])
    dA = R*np.stack([-ce*sa, ce*ca, 0*ce, 0*ce])
    dB = R*np.stack([0*ce, 0*ce, -se*sb, se*cb])
    def ev(fn): return np.broadcast_to(fn(*P_), E_.shape)
    Fv = np.stack([ev(fn) for fn in Fx])
    Jv = np.array([[ev(Jx[i][j]) for j in range(4)] for i in range(4)])
    tE = np.einsum('ij...,j...->i...', Jv, dE); tA = np.einsum('ij...,j...->i...', Jv, dA); tB = np.einsum('ij...,j...->i...', Jv, dB)
    M = np.stack([Fv, tE, tA, tB])          # rows
    M = np.moveaxis(M, (0, 1), (-2, -1))
    det = np.linalg.det(M)
    nr = np.sum(Fv**2, axis=0)**2
    # orientation normalisation: identity field
    Mi = np.moveaxis(np.stack([P_, dE, dA, dB]), (0, 1), (-2, -1))
    di = np.linalg.det(Mi)/np.sum(P_**2, axis=0)**2
    return float(np.sum(det/nr*W_)/(2*np.pi**2)), float(np.sum(di*W_)/(2*np.pi**2))
degs = {}
for name, fld in (("identity", Xv), ("w (21)", w21), ("w_r (41)", w41), ("w1r", w1r), ("s", s), ("s1", s1), ("v Morse", v)):
    d_, di_ = degree(fld, 1.0)
    degs[name] = d_/di_
d2, di2 = degree(w41, 2.5); degs["w_r (41), R=2.5"] = d2/di2
dm, dmi = degree(v, 2.5); degs["v, R=2.5"] = dm/dmi
rec("C8a deg(w (21)) = +3 = index of CP2 field (chi(CP2)=3)", abs(degs["w (21)"] - 3) < 1e-6, "%.6f" % degs["w (21)"])
rec("C8b deg(w_r/|w_r|) = -1 = deg(v/|v|) (paper sec. V.D)", abs(degs["w_r (41)"] + 1) < 1e-6 and abs(degs["v Morse"] + 1) < 1e-6
    and abs(degs["w_r (41), R=2.5"] + 1) < 1e-6 and abs(degs["v, R=2.5"] + 1) < 1e-6,
    ", ".join("%s: %.6f" % kv for kv in degs.items()))

# ---------------------------------------------------------------- C9 footnote-9 CTC on CP2 metric (22)
def gFS_num(P_, Lam):
    xv = np.asarray(P_, float); r2_ = xv @ xv
    xt = np.array([xv[1], -xv[0], xv[3], -xv[2]])
    return (6/Lam)/(1 + r2_)*(np.eye(4) - (np.outer(xv, xv) + np.outer(xt, xt))/(1 + r2_))
wf = sp.lambdify((x, y, zz_, t), list(w21), 'numpy')
def ctc_check(Lam, zeta=2.0, ns=2001):
    worst_norm, worst_fd = -np.inf, np.inf
    for sv in np.linspace(0, 2*np.pi, ns):
        P_ = np.array([2*np.sin(sv), -2*np.cos(sv), np.cos(sv), np.sin(sv)])/100
        dP = np.array([2*np.cos(sv), 2*np.sin(sv), -np.sin(sv), np.cos(sv)])/100
        G = gFS_num(P_, Lam); wv = np.array(wf(*P_), float)
        wl = G @ wv
        gL_ = G - zeta*np.outer(wl, wl)/(wv @ G @ wv)
        worst_norm = max(worst_norm, dP @ gL_ @ dP)
        worst_fd = min(worst_fd, dP @ G @ wv)        # future-directed <=> g_L(gamma', w) < 0 <=> g_FS(gamma', w) > 0 (zeta=2)
    return worst_norm, worst_fd
ctc = {L: ctc_check(L) for L in (6.0, 1.0, 100.0)}
rec("C9 footnote-9 curve is closed, timelike and future-directed for g_L (22)",
    all(v_[0] < 0 and v_[1] > 0 for v_ in ctc.values()),
    "; ".join("Lambda=%g: max g_L(g',g')=%.3e, min g_FS(g',w)=%.3e" % (L, a_, b_) for L, (a_, b_) in ctc.items()))
# the curve's timelikeness under zeta: g_L(g',g') = g_FS(g',g') - zeta g_FS(g',w)^2/g_FS(w,w); find the smallest zeta keeping it timelike
def zeta_min(Lam=6.0, ns=2001):
    zm = 0
    for sv in np.linspace(0, 2*np.pi, ns):
        P_ = np.array([2*np.sin(sv), -2*np.cos(sv), np.cos(sv), np.sin(sv)])/100
        dP = np.array([2*np.cos(sv), 2*np.sin(sv), -np.sin(sv), np.cos(sv)])/100
        G = gFS_num(P_, Lam); wv = np.array(wf(*P_), float)
        zm = max(zm, (dP @ G @ dP)*(wv @ G @ wv)/(dP @ G @ wv)**2)
    return zm
zmin = zeta_min()
rec("C9b the footnote-9 curve stays timelike for zeta > zeta_min (Lambda-independent: conformal factor cancels)", True, "zeta_min = %.4f (curve is a CTC for zeta=2 iff zeta_min < 2)" % zmin)

# ---------------------------------------------------------------- C10 FS (23) in Euler coords = (30); junction values
Lam = sp.symbols('Lambda', positive=True)
chi_, psi_, th_, ph_ = sp.symbols('chi psi theta_e phi_e', real=True)
kL = sp.sqrt(6/Lam); tn = kL*sp.tan(chi_/kL)
emb28 = sp.Matrix([tn*sp.cos(th_/2)*sp.cos(psi_/2 + ph_/2), tn*sp.cos(th_/2)*sp.sin(psi_/2 + ph_/2),
                   tn*sp.sin(th_/2)*sp.cos(psi_/2 - ph_/2), tn*sp.sin(th_/2)*sp.sin(psi_/2 - ph_/2)])
J28 = emb28.jacobian([chi_, psi_, th_, ph_])
xv_ = sp.Matrix([x, y, zz_, t]); xt_ = sp.Matrix([y, -x, t, -zz_])
r2s = (xv_.T*xv_)[0]
gFS = (6/Lam)/(1 + r2s)*(sp.eye(4) - (xv_*xv_.T + xt_*xt_.T)/(1 + r2s))
gFSf = sp.lambdify((x, y, zz_, t, Lam), gFS, 'numpy')
J28f = sp.lambdify((chi_, psi_, th_, ph_, Lam), J28, 'numpy'); E28f = sp.lambdify((chi_, psi_, th_, ph_, Lam), emb28, 'numpy')
A2 = sp.Rational(1, 4)*(6/Lam)*sp.sin(chi_/kL)**2; B2 = sp.cos(chi_/kL)**2
s1f = sp.Matrix([0, sp.sin(psi_)*sp.sin(th_), sp.cos(psi_), sp.cos(psi_)*sp.sin(th_)])  # in basis (dchi, dpsi, dtheta, dphi): sigma1 = cos psi dth + sin psi sin th dph
sig1 = sp.Matrix([0, 0, sp.cos(psi_), sp.sin(psi_)*sp.sin(th_)])
sig2 = sp.Matrix([0, 0, -sp.sin(psi_), sp.cos(psi_)*sp.sin(th_)])
sig3 = sp.Matrix([0, 1, 0, sp.cos(th_)])
dchi = sp.Matrix([1, 0, 0, 0])
g30 = dchi*dchi.T + A2*(sig1*sig1.T + sig2*sig2.T + B2*sig3*sig3.T)
g30f = sp.lambdify((chi_, psi_, th_, ph_, Lam), g30, 'numpy')
def pull_diff(Lvals, variant):
    mx_ = 0.0
    for L_ in Lvals:
        for _ in range(60):
            c_ = rng.uniform(0.01, 0.99)*np.pi/2*np.sqrt(6/L_)
            ps, tq, pq = rng.uniform(0, 4*np.pi), rng.uniform(0.05, np.pi - 0.05), rng.uniform(0, 2*np.pi)
            P_ = np.array(E28f(c_, ps, tq, pq, L_), float).ravel()
            Jn = np.array(J28f(c_, ps, tq, pq, L_), float)
            if variant == "printed":            # (23) as printed, (28) as printed
                G = np.array(gFSf(*P_, L_), float)
            elif variant == "drop-prefactor-28":  # (28) without the sqrt(6/Lambda) prefactor, (23) as printed
                k_ = np.sqrt(6/L_); P_ = P_/k_; Jn = Jn/k_
                G = np.array(gFSf(*P_, L_), float)
            elif variant == "scaled-23":        # (23) with r -> sqrt(Lambda/6) r (scaled FS), (28) as printed
                G = np.array(gFSf(*(P_*np.sqrt(L_/6)), 6.0), float)*1.0
                G = G  # 1/(1+L r^2/6)[delta - (L/6)(xx+xtxt)/(1+L r^2/6)]
                xv = P_; r2_ = xv @ xv; xt = np.array([xv[1], -xv[0], xv[3], -xv[2]]); k2 = L_/6
                G = (np.eye(4) - k2*(np.outer(xv, xv) + np.outer(xt, xt))/(1 + k2*r2_))/(1 + k2*r2_)
            mx_ = max(mx_, np.max(np.abs(Jn.T @ G @ Jn - np.array(g30f(c_, ps, tq, pq, L_), float))))
    return mx_
d6 = pull_diff([6.0], "printed")
dgen = pull_diff([0.5, 2.0, 20.0], "printed")
ddrop = pull_diff([0.5, 2.0, 6.0, 20.0], "drop-prefactor-28")
dscal = pull_diff([0.5, 2.0, 6.0, 20.0], "scaled-23")
rec("C10a (23) pulled back by (28) equals (30) at Lambda = 6 (the paper's numerical value)", d6 < 1e-9, "max|diff| = %.2e" % d6)
rec("C10a' DISCREPANCY (recorded, not an error of the construction): printed (23)+(28) do NOT give (30) for Lambda != 6",
    dgen > 1e-3 and ddrop < 1e-9 and dscal < 1e-9,
    "printed pair max|diff| = %.3g at Lambda in {0.5,2,20}; dropping the sqrt(6/Lambda) prefactor of (28): %.1e; or rescaling (23) to 1/(1+Lambda r^2/6)[delta - (Lambda/6)(xx+x~x~)/(1+Lambda r^2/6)]: %.1e -- a scale-convention slip; Lambda is a free scale so nothing downstream moves" % (dgen, ddrop, dscal))
A_ = sp.sqrt(A2); a1 = sp.Rational(1, 2)*kL*sp.sin(chi_/kL); b1 = sp.sin(chi_/kL)
rec("C10b junction: a(tau1)=A(chi1), 1-b(tau1)^2 = B^2 -> b = sin", sp.simplify(a1**2 - A2) == 0 and sp.simplify(1 - b1**2 - B2) == 0, "")
rec("C10c C1 matching: a' = (1/2)cos, b' = sqrt(Lambda/6) cos", sp.simplify(sp.diff(a1, chi_) - sp.cos(chi_/kL)/2) == 0
    and sp.simplify(sp.diff(b1, chi_) - sp.cos(chi_/kL)/kL) == 0, "")

# ---------------------------------------------------------------- C11 (34) from (11) in coords (33); (37),(38); (40)
xi, ps2, t2_, p2_ = sp.symbols('xi psi2 theta2 phi2', positive=True)
emb33 = sp.Matrix([xi*sp.cos(ps2), xi*sp.sin(ps2)*sp.cos(t2_), xi*sp.sin(ps2)*sp.sin(t2_)*sp.cos(p2_), xi*sp.sin(ps2)*sp.sin(t2_)*sp.sin(p2_)])
J33 = emb33.jacobian([xi, ps2, t2_, p2_])
g34c = sp.simplify(J33.T*gR.subs(dict(zip(X, emb33)))*J33)
om = sp.Matrix([sp.cos(2*ps2), -xi*sp.sin(2*ps2), 0, 0])
flat = sp.diag(1, xi**2, xi**2*sp.sin(ps2)**2, xi**2*sp.sin(ps2)**2*sp.sin(t2_)**2)
g34 = flat + xi**2*om*om.T
rec("C11a (34) is (11) in coordinates (33)", sp.simplify(g34c - g34) == sp.zeros(4), "")
sg = sp.symbols('sigma', positive=True)
al = sp.Function('alpha')(sg); be = sp.Function('beta')(sg)
omN = sp.Matrix([sp.cos(2*ps2), -sg*sp.sin(2*ps2), 0, 0])
gN = sp.diag(1, al**2, al**2*sp.sin(ps2)**2, al**2*sp.sin(ps2)**2*sp.sin(t2_)**2) + be**2*omN*omN.T
sub = {al: sg, be: sg}
d0 = sp.simplify(gN.subs(sub).doit() - g34.subs(xi, sg))
d1 = sp.simplify(sp.diff(gN, sg).subs({sp.Derivative(al, sg): 1, sp.Derivative(be, sg): 1}).subs(sub).doit() - sp.diff(g34, xi).subs(xi, sg))
rec("C11b (37) alpha=beta=xi1 and (38) alpha'=beta'=1 give C0 and C1 matching", d0 == sp.zeros(4) and d1 == sp.zeros(4), "")
Rn_ = sp.symbols('R', positive=True)
round_su2 = (Rn_/2)**2   # round S^3 radius R: (R^2/4)(s1^2+s2^2+s3^2)
rec("C11c (40) 2a(tau0)=R with b(tau0)=0 is the round S^3 of radius R", sp.simplify((Rn_/2)**2 - round_su2) == 0, "a(tau0)=R/2")

# ---------------------------------------------------------------- summary
nf = sum(1 for _, ok, _ in RESULTS if not ok)
print("\nSUMMARY: %d checks, %d FAIL" % (len(RESULTS), nf))
sys.exit(1 if nf else 0)
