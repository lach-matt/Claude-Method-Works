#!/usr/bin/env python3
"""transition5r.py -- item 485 (M's item 3): what the ten rows on 273 rest on -- loop quantum gravity's effective
dynamics carried to five dimensions, its scales fixed by 415 (transition5q.py H1-H10) -- proved: (a) derived from its
quantum theory, and (b) held against the choices particular to loop quantum gravity, each choice computed.  Labels:
computed (exact unless marked), deduced, READ, M's.  Worked in the conversation; not verified; not seated.

Held against the exclusions first (481, M-CHECK-EXCLUSIONS; 484, M-NO-CAUCHY): every interior computed below, for
every choice, is checked to have two horizons only (no inner horizon, 464, 471), a sphere radius bounded away from zero
with a finite positive lapse (no centre, no Cauchy horizon, H10's argument per case), a bounce that needs the quantum
term (not classical, 318) and in which the correction is order one (not semiclassical, C9).

  R0 (M's) 485: "do 3 first" -- item 3 of the map's "What comes next": prove what the ten rows rest on.
  R1 (computed) The sphere sector quantized as loop quantum gravity quantizes it (polymer representation: P_c on a
     lattice of spacing d_c hbar, holonomies e^(i d_c Pi_c) shifting it; H_c = (P_c S + S P_c)/2 d_c, S = sin(d_c
     Pi_c)): a Gaussian state evolved exactly (Chebyshev) from our horizon through the transition surface to position
     2's.  The norm is kept to 1e-12 (probability 1, now on the lattice); <P_c> stays above the effective minimum (a
     quantum bounce) and follows the effective trajectory with a deviation proportional to hbar -- 0.163 hbar/mu at
     d_c = 1/15, halving exactly as hbar halves: the effective equations are the quantum theory's hbar -> 0 limit.
  R2 (computed, exact) The b sector, with Pi_b = 6 b and P_b = (i hbar/6) d/db, H_b = (3/2)(G P_b + P_b G): the
     Schroedinger equation is d|psi|^2/dT = d/db (G |psi|^2/2) identically -- the quantum b sector transports its
     probability along the effective flow db/dT = -G/2, so every b observable's quantum distribution is the effective
     flow's push-forward: no loss through the transition (probability 1) and <cos(d_b b)> on the effective value to
     O(sigma^2) (computed: quartering as sigma halves).
  R3 (computed) A second, independent integrator for any holonomy function g and any scale coefficients (each sector
     by quadrature: T_c(w) = ln(3 d_c) - ln w - int_0^w (1/g - 1/s) ds, T_b(z) = -2 int_0^z g/(g^2 + d_b^2) dz; 415's
     two conditions generalized: the sphere's minimum at the classical curvature 1/l5^4, the b sector's maximum there)
     reproduces transition5q for g = sin: d_b = sqrt(6 d_c), T_WH = 2 T_T, m_WH = m_BH, l5^4 K_max 0.292, tau 2 r_h.
  R4 (computed) Holonomy function -- the representation the holonomies are taken in: j = 1/2 (sin x), j = 1 (sin 2x/2),
     j = 3/2 ((sin x + 3 sin 3x)/10), j = 2 ((sin 2x + 2 sin 4x)/10), and Chiou and Li's higher-order holonomy
     ((8 sin x - sin 2x)/6).  In every one: two horizons only with A > 0 between, one transition surface, curvature
     bounded at the l5 scale, the sphere bounded away from zero, our side classical (where x = 1e-9, Ric^2/K below 1e-9
     and K r^8/72 m^2 within 2e-6 of 1; the departure falls as sqrt(x), the b sector's correction (d_b b)^2).
     Position 2's side is classical only for the single harmonic (j = 1/2 and j = 1, identical physics): for every
     higher representation the white hole's side keeps an effective stress where the curvature is 1e-9 of l5's --
     Ric^2/K of order 1e-5 to 1e-2 that does not fall as x falls, and K r^8/72 m^2 far from 1.  General relativity is
     established there (low curvature), so those representations are excluded by established physics, not by a ruling;
     the single harmonic is what the lowest representations give.
  R5 (computed) Scale coefficients d_c -> l_c d_c, d_b -> l_b d_b: the structure of R4 holds for every pair; the white
     hole's mass moves as m_WH/m_BH = l_c^2/l_b^4 (computed to 1e-4).  A change of the one scale l5 -- l_c = L, l_b =
     sqrt(L) -- leaves it 1: the equal mass rests on one onset curvature shared by both sectors, whatever its value,
     not on l5's value.  That sharing is 415's premise (P1-P4): the correction a function of the curvature x alone,
     order one at one x.  The time across the interior is r_h(BH) + r_h(WH), to 1e-3 for every pair: 2 r_h/c when the
     masses are equal.
  R6 (computed) The size of the quantum correction to the effective trajectory in the physical case: hbar_eff/mu =
     8 l5^3/(pi L_x mu) with the fiducial length L_x = r_h; times R1's coefficient it is below 1e-60 at r0 = 20 ell and
     at the Earth cap.

What this proves and does not: the effective dynamics that computes 273 (transition5q) is the hbar -> 0 limit of its
polymer quantum theory in both sectors, computed, with the correction measured and negligible for every hole the
theorem uses; its consequences -- the transition surface, no inner horizon, no Cauchy horizon, bounded curvature,
probability 1 -- do not depend on the holonomy representation or the scale coefficients.  Two consequences do: the
classical white hole needs the single-harmonic holonomy (higher representations fail general relativity at low
curvature, so established physics selects it), and the white hole's equal mass needs one onset curvature for both
sectors (415's premise; a relative coefficient pair moves the mass as l_c^2/l_b^4).  Loop quantum gravity exists in
five dimensions (Bodendorfer, Thiemann and Thurn, arXiv 1105.3703-5, READ; Zhang's higher-dimensional loop quantum
cosmology, arXiv 1506.05597, READ: a bounce in every dimension); the mass's dependence on the polymerization is the 4D
prior art's too (Corichi and Singh 2016: m_WH ~ m_BH^3; Olmedo, Saini and Singh, arXiv 1707.07333: a symmetric bounce,
identical masses, under a condition on the loops; READ).  Neither the full theory in five dimensions nor any
established theory computes the pair of onsets; that is the one premise left, named.

python3 transition5r.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import numpy as np
import sympy as sp
import scipy.sparse as sps
import scipy.special as ssp
import scipy.integrate as si
import scipy.optimize as so

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


# ---------------------------------------------------------------- R1: the sphere sector on the polymer lattice
def _cheb(H, c, r, phi, tau):
    """phi -> exp(-i H tau) phi, H's spectrum inside [c - r, c + r] (Chebyshev, to machine precision)"""
    x = r * abs(tau); z = -1j * np.sign(tau)
    K = int(x + 10 * x ** (1 / 3) + 30)
    J = ssp.jv(np.arange(K), x)
    Hs = lambda v: (H @ v - c * v) / r
    t0, t1 = phi, Hs(phi)
    acc = J[0] * t0 + 2 * z * J[1] * t1
    for kk in range(2, K):
        t0, t1 = t1, 2 * Hs(t1) - t0
        acc = acc + 2 * z ** kk * J[kk] * t1
        if kk > x and abs(J[kk]) < 1e-17:
            break
    return np.exp(-1j * c * tau) * acc


def polymer(h, k=0.1, Phi=1.3, num=41):
    """P_c on P_lo + d h Z (mu = 1); H_c = (P S + S P)/2d; psi_n = i^n phi_n makes it real tridiagonal (a_n = (P_n +
    P_n+1)/4d); evolved from T = 0 (our horizon, P = 1 + k^2) to T = 2 T_T (position 2's), k = 3d/2"""
    d = 2 * k / 3
    P = np.arange(0.2 * k, Phi, d * h); n = len(P)
    a = (P[:-1] + P[1:]) / (4 * d)
    H = sps.diags([a, a], [-1, 1], format="csr").astype(complex) + 3 * sps.identity(n, format="csr")   # + 3 mu: a phase
    if "nonunitary" in MUT:
        H = H - 1e-3j * sps.identity(n, format="csr")
    Tend = 2 * math.log(k)
    P0 = 1 + k * k; Pi0 = -2 / d * math.atan(k); sig = math.sqrt(h / 6)
    phi = np.exp(-(P - P0) ** 2 / (4 * sig ** 2) + 1j * Pi0 * P / h) / (1j) ** np.arange(n)
    phi /= np.sqrt(np.sum(abs(phi) ** 2))
    Ts = np.linspace(0, Tend, num); out = []
    for i, T in enumerate(Ts):
        if i:
            phi = _cheb(H, 3.0, 2 * a.max() + 1e-3, phi, (Ts[1] - Ts[0]) / h)
        p = abs(phi) ** 2; nrm = p.sum()
        out.append((T, nrm, float((P * p).sum() / nrm), math.exp(T) + k * k * math.exp(-T), float(p[:10].sum() / nrm)))
    dev = [o[2] / o[3] - 1 for o in out]
    return dict(h=h, k=k, n=n, norm=max(abs(o[1] - 1) for o in out), dev=max(map(abs, dev)),
                minP=min(o[2] for o in out) / (2 * k), edge=max(o[4] for o in out))


# ---------------------------------------------------------------- R2: the b sector is transport
def bsector_identity():
    b, T, hb = sp.symbols("b T hbar", positive=True)
    G = sp.Function("G")(b); u = sp.Function("u")(b, T); v = sp.Function("v")(b, T)            # all real
    psi = u + sp.I * v
    Pop = lambda f: sp.I * hb / 6 * sp.diff(f, b)
    Hpsi = sp.Rational(3, 2) * (G * Pop(psi) + Pop(G * psi)) if "ordering" not in MUT else 3 * G * Pop(psi)
    psiT = sp.expand(-sp.I / hb * Hpsi)
    vT = psiT.coeff(sp.I); uT = sp.expand(psiT - sp.I * vT)
    rhoT = 2 * (u * uT + v * vT)
    target = sp.diff(G * (u ** 2 + v ** 2) / 2, b)
    return sp.simplify(sp.expand(rhoT - target)) == 0


def bsector_pushforward(db=0.05, zbar=0.6, sigmas=(0.04, 0.02), T1=None):
    """g = sin: the flow cos z(T) = b_o tanh(atanh(cos z0/b_o) + b_o (T - T0)/2), z = d_b b; a Gaussian in z0 pushed
    through the transition (z = pi/2) to the far side; <cos z> against cos z_eff, and the pushed density's norm"""
    bo = math.sqrt(1 + db * db)
    flow = lambda z0, dT: np.arccos(np.clip(bo * np.tanh(np.arctanh(np.cos(z0) / bo) + bo * dT / 2), -1, 1))
    zeff_T = lambda dT: flow(np.array([zbar]), dT)[0]
    # the time to carry zbar to pi - zbar (symmetric about the transition)
    dT = -4 * math.atanh(math.cos(zbar) / bo) / bo if T1 is None else T1
    xg, wg = np.polynomial.hermite_e.hermegauss(80)
    out = {}
    for s_ in sigmas:
        z0 = zbar + s_ * xg; wq = wg / wg.sum()
        zq = flow(z0, dT)
        out[s_] = abs(float((wq * np.cos(zq)).sum()) - math.cos(zeff_T(dT)))
    # the pushed density's norm on a grid (Jacobian of the flow), sigma = sigmas[0]
    s_ = sigmas[0]; zz = np.linspace(1e-4, math.pi - 1e-4, 200001)
    z0 = np.arccos(np.clip(bo * np.tanh(np.arctanh(np.cos(zz) / bo) - bo * dT / 2), -1, 1))
    rho = np.exp(-(z0 - zbar) ** 2 / (2 * s_ * s_)) / (s_ * math.sqrt(2 * math.pi)) * np.abs(np.gradient(z0, zz))
    return dict(dev=out, ratio=out[sigmas[0]] / out[sigmas[1]], norm=float(np.trapezoid(rho, zz)),
                crossed=float(zeff_T(dT)) > math.pi / 2)


# ---------------------------------------------------------------- R3-R5: any holonomy function, any coefficients
_s = sp.symbols("s")
HOL = {"j=1/2": sp.sin(_s), "j=1": sp.sin(2 * _s) / 2, "j=3/2": (sp.sin(_s) + 3 * sp.sin(3 * _s)) / 10,
       "j=2": (sp.sin(2 * _s) + 2 * sp.sin(4 * _s)) / 10, "Chiou-Li": (8 * sp.sin(_s) - sp.sin(2 * _s)) / 6}


def props(e):
    f = sp.lambdify(_s, e, "numpy"); f1 = sp.lambdify(_s, sp.diff(e, _s), "numpy")
    xs = np.linspace(1e-6, 3.3, 330001); v = f(xs)
    i = int(np.argmax(v < 0)); x1 = so.brentq(f, xs[i - 1], xs[i])
    grid = np.linspace(1e-4, x1 - 1e-4, 20001); sg = np.sign(f1(grid))
    xm = so.brentq(f1, 1e-4, x1 - 1e-4)
    return dict(f=f, f1=f1, x1=x1, xm=xm, gmax=float(f(xm)), s0=float(f1(0.0)), s1=float(-f1(x1)),
                nmax=int(np.sum(np.diff(sg) != 0)), pos=bool((f(grid) > 0).all()))


def _Tc(p, dc):
    """the sphere sector by quadrature, matched to the classical solution far from the transition; parametrized by q
    so that w and x1 - w both keep their digits"""
    f, x1, s1 = p["f"], p["x1"], p["s1"]
    R = lambda t: (1 / f(t) - 1 / t - 1 / (s1 * (x1 - t))) if t > 0 else -1 / (s1 * x1)
    def T_of_q(q):
        w = x1 / (1 + math.exp(-q)); u = x1 / (1 + math.exp(q))
        I = si.quad(R, 0, w, limit=200, epsabs=1e-13, epsrel=1e-13)[0]
        return math.log(3 * dc) - math.log(w) - I + math.log(u / x1) / s1, w, u
    return T_of_q


def _Tb(p, db):
    f, x1 = p["f"], p["x1"]
    integ = lambda z: f(z) / (f(z) ** 2 + db * db)
    def T(z):
        pts = [t for t in (db, 10 * db, 100 * db, x1 - 100 * db, x1 - 10 * db, x1 - db) if 0 < t < z]
        return -2 * si.quad(integ, 0, z, points=pts or None, limit=400, epsabs=1e-14, epsrel=1e-13)[0]
    return T


def gscales(name, mu=1e12, lc=1.0, lb=1.0):
    """415 generalized: the sphere's minimum P_c = 3 mu d_c/g_max at 72 mu^2/P^4 = 1 (l5 = 1); d_b so that the b
    sector reaches its maximum when the sphere reaches its minimum; then the coefficients l_c, l_b"""
    p = props(HOL[name])
    Pmin = 72 ** 0.25 * math.sqrt(mu)
    dc = Pmin * p["gmax"] / (3 * mu)
    Tq = _Tc(p, dc)
    TT = Tq(so.brentq(lambda q: Tq(q)[1] - p["xm"], -60, 60))[0]
    if "coincidence" in MUT:
        db = 1.3 * math.sqrt(6 * dc) * p["gmax"] ** 0.5
    else:
        db = math.exp(so.brentq(lambda L: _Tb(p, math.exp(L))(p["xm"]) - TT, math.log(1e-9), math.log(1.0)))
    return dict(p=p, mu=mu, dc=dc * lc, db=db * lb, dc0=dc, db0=db, lc=lc, lb=lb, name=name)


_CF = {}


def curvature_fns():
    """K and R_ab R^ab of -N^2 dT^2 + A^2 dx^2 + B^2 dOmega_3^2, in terms of N, N', A, A', A'', B, B', B''"""
    if "f" in _CF:
        return _CF["f"]
    T = sp.symbols("T"); x, c, th, ph = sp.symbols("x chi theta phi")
    N, A, B = [sp.Function(n)(T) for n in ("N", "A", "B")]
    X = (T, x, c, th, ph)
    g = sp.diag(-N ** 2, A ** 2, B ** 2, B ** 2 * sp.sin(c) ** 2, B ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    Gm = [[[sp.simplify(gi[a, a] * (sp.diff(g[a, b], X[cc]) + sp.diff(g[a, cc], X[b]) - sp.diff(g[b, cc], X[a])) / 2)
            for cc in range(5)] for b in range(5)] for a in range(5)]
    Rm = {}
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                for d in range(5):
                    if cc == d:
                        continue
                    e = sp.diff(Gm[a][b][d], X[cc]) - sp.diff(Gm[a][b][cc], X[d])
                    e += sum(Gm[a][cc][kk] * Gm[kk][b][d] - Gm[a][d][kk] * Gm[kk][b][cc] for kk in range(5))
                    e = sp.simplify(e)
                    if e != 0:
                        Rm[(a, b, cc, d)] = e
    K = sp.simplify(sum(g[a, a] * gi[b, b] * gi[cc, cc] * gi[d, d] * e ** 2 for (a, b, cc, d), e in Rm.items()))
    Ric = [sp.simplify(sum(Rm.get((a, b, a, b), 0) for a in range(5))) for b in range(5)]
    Ric2 = sp.simplify(sum(gi[b, b] ** 2 * Ric[b] ** 2 for b in range(5)))
    sy = sp.symbols("N0 N1 A0 A1 A2 B0 B1 B2")
    rep = {sp.Derivative(A, (T, 2)): sy[4], sp.Derivative(B, (T, 2)): sy[7], sp.Derivative(N, T): sy[1],
           sp.Derivative(A, T): sy[3], sp.Derivative(B, T): sy[6], N: sy[0], A: sy[2], B: sy[5]}
    _CF["f"] = (sp.lambdify(sy, K.subs(rep), "numpy"), sp.lambdify(sy, Ric2.subs(rep), "numpy"))
    return _CF["f"]


def geometry_fn(name):
    """N, A, B and their T-derivatives as functions of (w, z): P_c = 3 mu d_c/g(w), P_b = mu d_b g(z)/(g^2 + d_b^2),
    B = sqrt(P_c), A = P_b/P_c, N = B d_b/2 g(z); d/dT = -g(w) d/dw - (g(z)^2 + d_b^2)/(2 g(z)) d/dz"""
    w, z, mu, dc, db = sp.symbols("w z mu d_c d_b", positive=True)
    gw, gz = HOL[name].subs(_s, w), HOL[name].subs(_s, z)
    Pc = 3 * mu * dc / gw; Pb = mu * db * gz / (gz ** 2 + db ** 2)
    B = sp.sqrt(Pc); A = Pb / Pc; N = B * db / (2 * gz)
    D = lambda f: sp.diff(f, w) * (-gw) + sp.diff(f, z) * (-(gz ** 2 + db ** 2) / (2 * gz))
    A1, B1 = D(A), D(B)
    return sp.lambdify((w, z, mu, dc, db), [N, D(N), A, A1, D(A1), B, B1, D(B1)], "numpy")


def analyse(name, mu=1e12, lc=1.0, lb=1.0):
    S = gscales(name, mu, lc, lb); p = S["p"]; dc, db = S["dc"], S["db"]
    Tq = _Tc(p, dc); Tb = _Tb(p, db)
    w_of_T = lambda T: Tq(so.brentq(lambda q: Tq(q)[0] - T, -80, 80, xtol=1e-14))
    TWH = Tb(p["x1"])
    _, w0, u0 = w_of_T(0.0); _, w1, u1 = w_of_T(TWH)
    g_at = lambda w, u: p["f"](w) if w < p["x1"] / 2 else p["f"](p["x1"] - u)
    mBH = 3 * mu * dc / g_at(w0, u0); mWH = 3 * mu * dc / g_at(w1, u1)
    TT = Tq(so.brentq(lambda q: Tq(q)[1] - p["xm"], -60, 60))[0]
    # the interior in z (regular at both horizons): T, w and the proper time tau
    def rhs(z, y):
        gz = p["f"](z); dT = -2 * gz / (gz * gz + db * db)
        Bv = math.sqrt(3 * mu * dc / p["f"](y[1]))
        return [dT, -p["f"](y[1]) * dT, Bv * db / (gz * gz + db * db)]
    sol = si.solve_ivp(rhs, (0, p["x1"]), [0.0, w0, 0.0], method="DOP853", rtol=1e-11, atol=1e-14, dense_output=True)
    tau = sol.y[2, -1] / math.sqrt(mBH)
    KF, RF = curvature_fns(); geo = geometry_fn(name)
    def at(zv):
        T, wv, _ = sol.sol(zv); v = geo(wv, zv, mu, dc, db)
        return T, wv, v, KF(*v), RF(*v)
    e = np.logspace(-7, math.log10(p["x1"] / 2), 160)
    zz = np.unique(np.concatenate([e, p["x1"] - e]))
    rows = []
    for zv in zz:
        T, wv, v, K, R2 = at(zv)
        rows.append((zv, T, v[5] ** 2, K, R2, v[2], v[0]))
    rows = np.array(rows)
    zT = so.brentq(lambda zv: sol.sol(zv)[1] - p["xm"], 1e-6, p["x1"] - 1e-6)          # z at the transition surface
    Kmax = -so.minimize_scalar(lambda zv: -at(zv)[3], bounds=(max(1e-6, zT - 0.6), min(p["x1"] - 1e-6, zT + 0.6)),
                               method="bounded", options=dict(xatol=1e-10)).fun
    cls = {}
    for side, m, sel in (("BH", mBH, rows[:, 0] < zT), ("WH", mWH, rows[:, 0] > zT)):
        sub = rows[sel]; x = math.sqrt(72) * m / sub[:, 2] ** 2
        j = int(np.argmin(abs(np.log(x / 1e-9))))
        cls[side] = dict(x=float(x[j]), V=float(sub[j, 4] / sub[j, 3]), tang=float(sub[j, 3] * sub[j, 2] ** 4 / (72 * m * m) - 1))
    gw_grid = p["f1"](np.linspace(w0, w1, 20001))
    return dict(S=S, TT=TT, TWH=TWH, ratio=mWH / mBH, tau=tau, Kmax=Kmax, cls=cls,
                Apos=bool((rows[:, 5] > 0).all()), Npos=bool(((rows[:, 6] > 0) & np.isfinite(rows[:, 6])).all()),
                Bmin=float(math.sqrt(rows[:, 2].min() / mBH)), turns=int(np.sum(np.diff(np.sign(gw_grid)) != 0)),
                gb_pos=p["pos"], quantum=abs(float(p["f1"](p["xm"]))) < 1e-9)


# ---------------------------------------------------------------- R6 and the whole
def compute():
    o = {}
    o["poly"] = [polymer(4e-3), polymer(2e-3), polymer(4e-3, k=0.05)]
    o["bid"] = bsector_identity()
    o["bpf"] = bsector_pushforward()
    o["hol"] = {nm: analyse(nm) for nm in HOL}
    o["coef"] = {(lc, lb): analyse("j=1/2", lc=lc, lb=lb)
                 for lc, lb in ((2.0, 1.0), (1.0, 2.0), (0.5, 1.0), (1.0, 0.7), (2.0, math.sqrt(2.0)), (0.25, 0.5))}
    o["mu"] = {nm: [gscales_ratio(nm, mu) for mu in (1e8, 1e12, 1e20)] for nm in ("j=3/2", "Chiou-Li")}
    QO = _load("quantum_onset.py", "t5r_qo"); CF = _load("core_face.py", "t5r_cf")
    l5 = QO.onset_4d()["l5"]
    c1 = o["poly"][1]["dev"] / o["poly"][1]["h"]
    o["phys"] = {k: 8 * l5 ** 3 / (math.pi * math.sqrt(v["mu5"]) * v["mu5"]) * c1 for k, v in CF.core_scales().items()}
    o["c1"] = c1
    # cross-check with transition5q (g = sin): its d_b, l5^4 K_max and tau
    T5 = _load("transition5q.py", "t5r_t5q")
    s5 = T5.scales(1e12)
    o["t5q"] = dict(db=float(s5["db"]), dc=float(s5["dc"]))
    return o


def gscales_ratio(name, mu):
    S = gscales(name, mu); p = S["p"]
    Tq = _Tc(p, S["dc"]); Tb = _Tb(p, S["db"])
    w_of_T = lambda T: Tq(so.brentq(lambda q: Tq(q)[0] - T, -80, 80, xtol=1e-14))
    _, w0, u0 = w_of_T(0.0); _, w1, u1 = w_of_T(Tb(p["x1"]))
    g_at = lambda w, u: p["f"](w) if w < p["x1"] / 2 else p["f"](p["x1"] - u)
    return g_at(w0, u0) / g_at(w1, u1)


def checks(o):
    P = o["poly"]
    r1 = (all(x["norm"] < 1e-10 and x["edge"] < 1e-20 for x in P) and abs(P[0]["dev"] / P[1]["dev"] - 2) < 0.02
          and P[1]["dev"] < 1e-3 and all(0 < x["minP"] - 1 < 1e-3 for x in P) and P[2]["dev"] / P[2]["h"] < 0.3)
    b = o["bpf"]
    r2 = o["bid"] and abs(b["ratio"] - 4) < 0.1 and abs(b["norm"] - 1) < 1e-6 and b["crossed"]
    s = o["hol"]["j=1/2"]
    r3 = (abs(s["S"]["db"] / o["t5q"]["db"] - 1) < 1e-6 and abs(s["S"]["dc"] / o["t5q"]["dc"] - 1) < 1e-9
          and abs(s["TWH"] / s["TT"] - 2) < 1e-6 and abs(s["ratio"] - 1) < 1e-6 and abs(s["Kmax"] - 0.2917) < 2e-3
          and abs(s["tau"] - 2) < 1e-2)
    def structural(a):                                     # the departure from vacuum falls as sqrt(x): 3e-5 at 1e-9
        return (a["Apos"] and a["gb_pos"] and a["Npos"] and a["Bmin"] > 0 and a["turns"] == 1 and a["quantum"]
                and 0 < a["Kmax"] < math.inf and a["cls"]["BH"]["V"] < 1e-6 and abs(a["cls"]["BH"]["tang"]) < 1e-4)
    classical = lambda a: a["cls"]["WH"]["V"] < 1e-6 and abs(a["cls"]["WH"]["tang"]) < 1e-4
    H = o["hol"]
    r4 = (all(structural(a) and 0.05 < a["Kmax"] < 10 for a in H.values()) and classical(H["j=1/2"]) and classical(H["j=1"])
          and not any(classical(H[k]) for k in ("j=3/2", "j=2", "Chiou-Li"))
          and abs(H["j=1"]["ratio"] - 1) < 1e-6 and abs(H["j=1"]["Kmax"] / H["j=1/2"]["Kmax"] - 1) < 1e-3
          and all(abs(v[-1] / v[-2] - 1) < 1e-2 and abs(v[-1] - 1) > 0.1 for v in o["mu"].values()))
    law = (lambda lc, lb: lc / lb ** 2) if "law" in MUT else (lambda lc, lb: lc ** 2 / lb ** 4)
    C = o["coef"]
    r5 = (all(structural(a) and classical(a) for a in C.values())
          and all(abs(a["ratio"] / law(lc, lb) - 1) < 1e-3 for (lc, lb), a in C.items())
          and abs(C[(2.0, math.sqrt(2.0))]["ratio"] - 1) < 1e-3 and abs(C[(0.25, 0.5)]["ratio"] - 1) < 1e-3
          and all(abs(C[(L, math.sqrt(L))]["Kmax"] * L ** 4 / H["j=1/2"]["Kmax"] - 1) < 1e-3 for L in (2.0, 0.25))
          and all(abs(a["tau"] - 1 - math.sqrt(a["ratio"])) < 1e-3 for a in C.values()))
    r6 = all(v < 1e-60 for v in o["phys"].values())
    return dict(R1=r1, R2=r2, R3=r3, R4=r4, R5=r5, R6=r6)


def report(o=None):
    o = o or compute(); ck = checks(o)
    for x in o["poly"]:
        print("R1 lattice d_c = %.4f, hbar/mu %.0e: %d sites; norm drift %.1e; <P_c>/P_eff - 1 max %.3e (/hbar %.4f); "
              "min <P_c> / effective min - 1 = %.1e; at the lattice's edge %.0e" % (
                  2 * x["k"] / 3, x["h"], x["n"], x["norm"], x["dev"], x["dev"] / x["h"], x["minP"] - 1, x["edge"]))
    b = o["bpf"]
    print("R2 Schroedinger -> continuity along db/dT = -G/2 identically: %s; <cos z> - cos z_eff: %s (ratio %.3f); "
          "pushed norm %.9f; crossed the transition %s" % (o["bid"], ", ".join("%.2e at sigma %.2f" % (v, k) for k, v in
                                                                              b["dev"].items()), b["ratio"], b["norm"], b["crossed"]))
    def line(lab, a):
        S = a["S"]
        return ("%-9s d_c %.3e d_b %.3e T_T %7.3f T_WH/T_T %.5f m_WH/m_BH %.6f l5^4 K_max %.4f tau %.4f r_h B_min/r_h %.2e "
                "A>0 %s N ok %s turns %d | our side x %.0e: Ric2/K %.0e, K r^8/72m^2-1 %.0e | position 2's: Ric2/K %.0e, "
                "K r^8/72m^2-1 %.0e" % (lab, S["dc"], S["db"], a["TT"], a["TWH"] / a["TT"], a["ratio"], a["Kmax"], a["tau"],
                                        a["Bmin"], a["Apos"], a["Npos"], a["turns"], a["cls"]["BH"]["x"], a["cls"]["BH"]["V"],
                                        a["cls"]["BH"]["tang"], a["cls"]["WH"]["V"], a["cls"]["WH"]["tang"]))
    for nm, a in o["hol"].items():
        print("R4 " + line(nm, a))
    for nm, v in o["mu"].items():
        print("   %s m_WH/m_BH at mu/l5^2 1e8, 1e12, 1e20: %s" % (nm, ", ".join("%.5f" % x for x in v)))
    for (lc, lb), a in o["coef"].items():
        print("R5 " + line("%.2g,%.2g" % (lc, lb), a) + "  (l_c^2/l_b^4 = %.5f)" % (lc ** 2 / lb ** 4))
    print("R6 quantum correction to the effective trajectory, hbar_eff = 8 l5^3/(pi r_h), coefficient %.3f: %s" % (
        o["c1"], ", ".join("%.1e (%s)" % (v, k) for k, v in o["phys"].items())))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["nonunitary", "ordering", "coincidence", "law"]
    for m_ in names:
        MUT.clear(); MUT.add(m_)
        try:
            r_ = selftest(quiet=True)
        except Exception:
            r_ = False
        caught += not r_; print("mutant %-12s %s" % (m_, "caught" if not r_ else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
