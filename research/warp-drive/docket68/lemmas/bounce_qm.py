#!/usr/bin/env python3
"""bounce_qm.py -- item 536: the bounce defined in quantum physics.  M: "The bounce needs to  connect to physics. It's a
quantum bounce, thus it has to be defined in quantum physics."  273's bounce is defined here by quantum mechanics
alone: the hole's interior is quantised from general relativity's own Hamiltonian (Wheeler-DeWitt), its states evolve
in the bulk's own clock -- the time conjugate to the cosmological constant (Henneaux and Teitelboim's unimodular form,
classically general relativity) -- and the evolution is required to be unitary.  The classical interior reaches r = 0
in a finite time of that clock, so its Hamiltonian is not self-adjoint there; unitarity forces a self-adjoint
extension, a reflection at r = 0, and the reflected wave is the white hole.  Prior art (READ, alphaXiv full text):
Gielen and Menendez-Pidal, PRL 134 (2025) 101501, arXiv 2409.03006 (planar AdS: "unitarity in unimodular time always
implies singularity resolution"); Gielen and Ried, JHEP 06 (2025) 074, arXiv 2502.10104 (four-dimensional
Schwarzschild-(A)dS: a transition from a black hole to a white hole "of the same mass"); Gotay and Demaret, PRD 28
(1983) 2402 (slow and fast clocks).  Carried here to the record's five dimensions and checked.  Labels: computed (exact
unless marked), deduced, READ, M's.  Worked in the conversation; not verified; not seated.  2026-10-20.

Held against the exclusions first (481): the quantum interior has two horizons only (Q7; no inner horizon, 464, 471,
no Cauchy horizon, 484); the bounce is not classical (318) -- it is the reflection unitarity forces -- and not
semiclassical (C9): the state is a superposition of the black and white holes there, not a smooth classical metric.

  Q0 (M's) 536.
  Q1 (computed, exact) Five-dimensional Kantowski-Sachs with the 3-sphere, ds^2 = -(N^2/xi) dt^2 + (xi/Y) dz^2
     + Y dOmega_3^2 (Y the sphere's radius squared, xi = -r^2 f): sqrt(-g)(R - 2 Lambda) reduces, up to a total
     derivative, to L = -(3/2N) xi' Y' + 6N - 2 Lambda N Y (Euler-Lagrange of the difference identically zero).  With
     Henneaux-Teitelboim's term, Lambda is the momentum of the clock T (T' = 2 sqrt(-g): twice the five-volume per
     coordinate cell), and H = 2NY (H_S + Lambda), H_S = -pi_xi pi_Y/(3Y) - 3/Y.  The minisuperspace metric is flat, so
     the Laplace-Beltrami ordering is unique: H_S = (1/3Y) d_xi d_Y - 3/Y.  Gielen and Ried's form in four
     dimensions, (1/eta^2) d_eta d_xi - 1/eta^2, with the sphere's power changed.
  Q2 (computed, exact) The classical solutions in T: Y^2 = (2k/3)(T0 - T) (k = pi_xi, conserved), xi = xi0
     + (3/k^2)(Lambda Y^2/2 - 3Y); at k = 3, xi0 = mu this is -r^2 f of Schwarzschild-AdS5,
     f = 1 - mu/r^2 - Lambda r^2/6.
     The singularity is a finite T away (a slow clock, Gotay-Demaret); the horizon xi = 0 is an interior point of the
     configuration space (xi runs over all reals).
  Q3 (computed, exact) The Wheeler-DeWitt equation is a Schroedinger equation, i d_T psi = H_S psi, solved exactly by
     psi = exp i[k xi + (3/k)(Lambda Y^2/2 - 3Y) + Lambda T].
  Q4 (computed, exact) H_S is not self-adjoint: its eigenfunctions to +i and -i, exp i[k xi - (3/k)(+-i Y^2/2 + 3Y)],
     have |phi|^2 = exp(+-3Y^2/k), normalisable only for k < 0 (+i) or k > 0 (-i): equal deficiency spaces, so
     self-adjoint extensions exist, alpha(Lambda, -k) = exp(i chi(k)) alpha(Lambda, k), chi odd -- each a reflection at
     Y = 0 joining a black-hole mode (k > 0, Y shrinking) to a white-hole mode (k < 0, Y growing).  Unitarity
     requires one of them.
  Q5 (computed) The bounce, from a brute-force wavefunction on a (xi, Y) grid: with the reflection the norm is constant
     to 1e-4 through it; the black-hole branch alone loses its norm as it reaches Y = 0 (non-unitary).  <Y>(T) =
     sqrt(2/3) <|k|^(1/2)> Gamma(3/4) 1F1(-1/4, 1/2, -sigma^2 T^2)/(sqrt(pi) sigma^(1/2)) (closed form, agreeing with
     the grid): a least value above zero, the classical branches on both sides.
  Q6 (computed) The white hole's mass.  The asymptotic xi0 out is chi'(k) - xi0 in: a state symmetric under time
     reversal (the record's 273 (a): the Kruskal isometry) comes out with the black hole's mass exactly; an asymmetric
     one does not (grid and closed form).  The extension's sign fixes the mass's sign (Gielen-Ried's beta).
  Q7 (computed, exact) Two horizons only.  <xi>(T) = beta/2 + Lambda_c <1/|k|> g_1(T) - 9 sqrt(2/3) <|k|^(-3/2)>
     g_(1/2)(T), g_a = Gamma((1+a)/2) 1F1(-a/2, 1/2, -sigma^2 T^2)/(sqrt(pi) sigma^a), each g_a strictly increasing
     in |T| (its derivative a Kummer-positive 1F1): so <xi> has exactly two zeros, the black hole's horizon and the
     white hole's, and no inner or Cauchy horizon.  The effective metric's curvature is bounded.
  Q8 (computed) The scale.  The bounce sits where the clock time left to the classical singularity is
     sqrt(2) Gamma(3/4)^2/pi = 0.676 of the clock's quantum spread -- a property of the state, which quantum mechanics
     does not fix.  The record's onset at x = 1 (415; transition5q H7) is the bounce with 72^(1/4) l5/2 = 1.456 l5 of
     proper time left, the same for every mass, and needs the clock spread sigma_Lambda = (4/(3 pi)) 0.676 l5/(L_z mu)
     in the hole's coordinate cell L_z.
  Q9 (computed) Against transition5q: one trapped region and two horizons, the white hole of the black hole's mass, the
     proper time across 2 r_h/c (the effective metric's deficit falls with Y_min/r_h^2 and is ~1e-5 at the small end),
     curvature bounded at the bounce.  Here the equal mass rests on time reversal (273 (a)), not on 415's shared onset;
     the scale rests on the clock's spread, as transition5q's rested on 415's two scales.

What this proves and does not: within canonical quantum mechanics of general relativity's own minisuperspace -- the
Wheeler-DeWitt equation, Laplace-Beltrami ordering, the clock conjugate to Lambda, unitarity -- the bounce is forced:
either the evolution is not unitary or the singularity is replaced by a reflection into the white hole (Gielen and
Menendez-Pidal's conclusion, carried to five dimensions).  The truncation to homogeneity before quantising is
minisuperspace's, the choice of clock is Gotay-Demaret's (with a fast clock no bounce is forced), the extension is a
choice within unitarity, and the bounce's place is the state's.  None of these is loop quantum gravity's.

python3 bounce_qm.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import numpy as np
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
mp.mp.dps = 30
RH_SMALL = 1.12008e-20                       # b4d_small RH: the example README's own hole (m)
C1 = math.sqrt(2) * math.gamma(0.75) ** 2 / math.pi


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


# ---------------------------------------------------------------------------------------------------- Q1-Q4, exact
def _curv(g, X):
    gi = g.inv(); n = g.shape[0]
    G = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    def riem(a, b, c, d):                                  # R^a_{bcd}
        return (sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
                + sum(G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c] for e in range(n)))
    return gi, G, riem


def reduction():
    """Q1: the reduced Lagrangian, the Hamiltonian in Schroedinger form, the minisuperspace metric flat"""
    t, z, c, th, ph, Lam = sp.symbols("t z chi theta phi Lambda")
    N, xi, Y = [sp.Function(n)(t) for n in ("N", "xi", "Y")]
    X = (t, z, c, th, ph)
    g = sp.diag(-N ** 2 / xi, xi / Y, Y, Y * sp.sin(c) ** 2, Y * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi, G, riem = _curv(g, X)
    R = sp.simplify(sum(gi[b, d] * riem(a, b, a, d) for a in range(5) for b in range(5) for d in range(5)
                        if gi[b, d] != 0))
    L = sp.simplify(N * Y * (R - 2 * Lam))
    k3 = 2 if "kinetic" in MUT else sp.Rational(3, 2)
    target = -k3 / N * sp.diff(xi, t) * sp.diff(Y, t) + 6 * N - 2 * Lam * N * Y
    from sympy.calculus.euler import euler_equations
    el = [sp.simplify(e.lhs) for e in euler_equations(sp.simplify(L - target), [N, xi, Y], t)]
    ok_L = all(e == 0 for e in el)
    # Legendre transform with the clock: L + Lambda T'
    Nn, x, y, px, py, pT = sp.symbols("N xi Y pi_xi pi_Y pi_T")
    xd, yd = sp.symbols("xid yd")
    Lp = -sp.Rational(3, 2) / Nn * xd * yd + 6 * Nn - 2 * pT * Nn * y
    sol = sp.solve([sp.diff(Lp, xd) - px, sp.diff(Lp, yd) - py], [xd, yd], dict=True)[0]
    H = sp.simplify((px * xd + py * yd - Lp).subs(sol))
    HS = -px * py / (3 * y) - 3 / y
    ok_H = sp.simplify(H - 2 * Nn * y * (HS + pT)) == 0
    # minisuperspace metric g^{xi Y} = 1/(6Y): flat; the Laplace-Beltrami operator
    gm = sp.Matrix([[0, 6 * y], [6 * y, 0]]); Xm = (x, y)
    gmi, Gm, rm = _curv(gm, Xm)
    Rm = sp.simplify(sum(gmi[b, d] * rm(a, b, a, d) for a in range(2) for b in range(2) for d in range(2)))
    f = sp.Function("f")(x, y)
    sq = sp.sqrt(-gm.det())
    lb = sp.simplify(sum(sp.diff(gmi[i, j] * sq * sp.diff(f, Xm[j]), Xm[i]) for i in range(2) for j in range(2)) / sq)
    ok_lb = sp.simplify(lb - sp.diff(f, x, y) / (3 * y)) == 0
    return dict(L=ok_L, H=ok_H, flat=Rm == 0, lb=ok_lb, Tdot=sp.diff(Lp, pT) == -2 * Nn * y)


def classical():
    """Q2: the solutions in the clock T; Schwarzschild-AdS5 at k = 3; the singularity a finite T away"""
    k, x0, Lam, s, mu, Yv = sp.symbols("k xi0 Lambda s mu Y", positive=True)
    Y = sp.sqrt(2 * k * s / 3)                                       # s = T0 - T
    xi = x0 + 3 / k ** 2 * (Lam * Y ** 2 / 2 - 3 * Y)
    piY = (3 * Lam * Y - 9) / k
    # Hamilton's equations from H_S at pi_xi = k, with d/dT = -d/ds
    eqY = sp.simplify(-sp.diff(Y, s) - (-k / (3 * Y)))
    eqx = sp.simplify(-sp.diff(xi, s) - (-piY / (3 * Y)))
    con = sp.simplify(-k * piY / (3 * Y) - 3 / Y + Lam)             # H_S + Lambda = 0
    xiY = x0 + 3 / k ** 2 * (Lam * Yv ** 2 / 2 - 3 * Yv)
    f = 1 - mu / Yv - Lam * Yv / 6
    sads = sp.simplify(xiY.subs({k: 3, x0: mu}) + Yv * f) == 0
    finite = sp.limit(Y, s, 0) == 0                                   # Y = 0 at s = 0: T0 finite
    return dict(eqY=eqY == 0, eqx=eqx == 0, con=con == 0, sads=sads, slow=finite)


def eigen():
    """Q3: the exact eigenfunctions of the Schroedinger form"""
    x, y, T, k, Lam = sp.symbols("xi Y T k Lambda", real=True)
    psi = sp.exp(sp.I * (k * x + 3 / k * (Lam * y ** 2 / 2 - 3 * y) + Lam * T))
    HS = lambda f: sp.diff(f, x, y) / (3 * y) - (4 if "ordering" in MUT else 3) / y * f
    return sp.simplify(sp.I * sp.diff(psi, T) - HS(psi)) == 0


def deficiency():
    """Q4: H_S phi = +-i phi; which are normalisable; the extensions"""
    x, y = sp.symbols("xi Y", positive=True); k = sp.symbols("k", real=True, nonzero=True)
    out = {}
    for sg in (1, -1):
        phi = sp.exp(sp.I * (k * x - 3 / k * (sg * sp.I * y ** 2 / 2 + 3 * y)))
        solves = sp.simplify(sp.diff(phi, x, y) / (3 * y) - 3 / y * phi - sg * sp.I * phi) == 0
        mod2 = sp.simplify(sp.Abs(phi) ** 2)
        norm = {}
        for kv in (2, -2):
            norm[kv] = sp.integrate(y * mod2.subs(k, kv), (y, 0, sp.oo))
        out[sg] = dict(solves=solves, normal_kpos=norm[2].is_finite, normal_kneg=norm[-2].is_finite)
    # +i: only k < 0; -i: only k > 0 -> equal deficiency spaces (k -> -k)
    ok = (out[1]["solves"] and out[-1]["solves"] and not out[1]["normal_kpos"] and out[1]["normal_kneg"]
          and out[-1]["normal_kpos"] and not out[-1]["normal_kneg"])
    return dict(detail=out, ok=ok)


# --------------------------------------------------------------------------------------------- Q5-Q7, the states
PAR = dict(kc=30.0, sk=0.5, Lc=-1.0, sg=0.15, xi0=1.0)


def _kgrid(sign, p, n=81):
    k = np.linspace(p["kc"] - 5 * p["sk"], p["kc"] + 5 * p["sk"], n); return sign * k, k[1] - k[0]


def psi(T, XI, YY, p, xin=None, drop_wh=False):
    """the state: Gaussian in Lambda (sigma) and |k| (sk); alpha(-k) = exp(i beta k) alpha(k), beta = 2 xi0"""
    beta = 2 * p["xi0"] * (-1 if "beta_neg" in MUT else 1)
    out = np.zeros(XI.shape, complex)
    for sgn in (1, -1):
        if (drop_wh or "no_wh" in MUT) and sgn < 0:
            continue
        ks, dk = _kgrid(sgn, p)
        for kk in ks:
            ak = abs(kk)
            if xin is None:
                ph = np.exp(-1j * beta * kk / 2)
            else:                                        # black hole with xi0 = xin; its reflection by the extension
                ph = np.exp(-1j * xin * kk) if kk > 0 else np.exp(1j * beta * ak) * np.exp(-1j * xin * ak)
            s = T + 3 * YY ** 2 / (2 * kk)
            out += dk * ph * np.exp(-(ak - p["kc"]) ** 2 / (2 * p["sk"] ** 2)) * np.exp(
                1j * p["Lc"] * s - p["sg"] ** 2 * s ** 2 / 2 + 1j * (kk * XI - 9 * YY / kk))
    return out


def grid():
    xi = np.linspace(-12, 9, 700); Yv = np.linspace(1e-4, 45, 560)
    XI, YY = np.meshgrid(xi, Yv, indexing="ij")
    return XI, YY, (xi[1] - xi[0]) * (Yv[1] - Yv[0])


def moments(T, p, G, **kw):
    XI, YY, dA = G
    w = np.abs(psi(T, XI, YY, p, **kw)) ** 2 * YY
    n = w.sum() * dA
    return n, (w * YY).sum() * dA / n, (w * XI).sum() * dA / n


def kav(a, p):
    k = np.linspace(p["kc"] - 8 * p["sk"], p["kc"] + 8 * p["sk"], 4001)
    w = k * np.exp(-(k - p["kc"]) ** 2 / p["sk"] ** 2)
    return np.trapezoid(w * k ** a, k) / np.trapezoid(w, k)


def g_a(a, T, sg):
    return mp.gamma((1 + a) / 2) / (mp.sqrt(mp.pi) * mp.mpf(sg) ** a) * mp.hyp1f1(-mp.mpf(a) / 2, 0.5, -(sg * T) ** 2)


def Ycf(T, p, kavs=None):
    kavs = kavs or {a: kav(a, p) for a in (0.5, -1, -1.5)}
    return mp.sqrt(mp.mpf(2) / 3) * kavs[0.5] * g_a(0.5, T, p["sg"])


def xicf(T, p, kavs=None, beta=None):
    kavs = kavs or {a: kav(a, p) for a in (0.5, -1, -1.5)}
    beta = 2 * p["xi0"] if beta is None else beta
    return beta / 2 + p["Lc"] * kavs[-1] * g_a(1, T, p["sg"]) - 9 * mp.sqrt(mp.mpf(2) / 3) * kavs[-1.5] * g_a(0.5, T,
                                                                                                         p["sg"])


def states():
    """Q5-Q6: the grid against the closed forms; unitarity; black hole to white hole; the mass"""
    p = PAR; G = grid(); kv = {a: kav(a, p) for a in (0.5, -1, -1.5)}
    rows = []
    n0 = None
    for T in (-40.0, -8.0, 0.0, 8.0, 40.0):
        n, Ym, xim = moments(T, p, G)
        n0 = n0 or n
        rows.append(dict(T=T, norm=n / n0, Y=Ym, Ycf=float(Ycf(T, p, kv)), xi=xim, xicf=float(xicf(T, p, kv))))
    bh = []                                              # the black-hole branch alone
    for T in (-40.0, 0.0, 40.0):
        n, _, _ = moments(T, p, G, drop_wh=True)
        bh.append(n / n0)
    # an asymmetric state: xi0 in = 0.7, beta = 2: out should be 1.3
    cl = lambda T: float(xicf(T, p, kv, beta=0.0))       # the classical part without xi0
    _, _, xa_in = moments(-40.0, p, G, xin=0.7)
    _, _, xa_out = moments(40.0, p, G, xin=0.7)
    return dict(rows=rows, bh=bh, asym=(xa_in - cl(-40.0), xa_out - cl(40.0)), kv=kv)


def kretschmann_eff():
    """K of ds^2 = -dT^2/(4 xi Y^2) + (xi/Y) dz^2 + Y dOmega_3^2 in xi, Y and their T-derivatives"""
    T, z, c, th, ph = sp.symbols("T z chi theta phi")
    xi, Y = sp.Function("xi")(T), sp.Function("Y")(T)
    X = (T, z, c, th, ph)
    g = sp.diag(-1 / (4 * xi * Y ** 2), xi / Y, Y, Y * sp.sin(c) ** 2, Y * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi, G, riem = _curv(g, X)
    K = 0
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                for d in range(cc + 1, 5):
                    r = sp.simplify(riem(a, b, cc, d))
                    if r != 0:
                        # R^a_{bcd} R_a^{bcd} for a diagonal metric: g_aa g^bb g^cc g^dd (R^a_bcd)^2, twice for c<d
                        K += 2 * g[a, a] * gi[b, b] * gi[cc, cc] * gi[d, d] * r ** 2
    K = sp.simplify(K.subs({sp.sin(c): 1, sp.sin(th): 1}))
    s = sp.symbols("x0 x1 x2 y0 y1 y2")
    rep = {sp.diff(xi, T, 2): s[2], sp.diff(Y, T, 2): s[5]}
    K = K.subs(rep).subs({sp.diff(xi, T): s[1], sp.diff(Y, T): s[4]}).subs({xi: s[0], Y: s[3]})
    return sp.lambdify(s, sp.simplify(K), "mpmath")


def effective(Kf, p, kv):
    """Q7: zeros of <xi>, monotone in |T|; the effective metric's curvature; proper time across"""
    xf = lambda T: xicf(T, p, kv); yf = lambda T: Ycf(T, p, kv)
    Ts = [mp.mpf(j) / 4 for j in range(-240, 241)]
    xs = [xf(T) for T in Ts]
    zeros = sum(1 for a, b in zip(xs, xs[1:]) if a * b < 0)
    mono = all(xs[i] <= xs[i + 1] for i in range(240)) and all(xs[i] >= xs[i + 1] for i in range(240, 480))
    # Kummer: d/dz 1F1(-a/2, 1/2, -z) = a 1F1(1 - a/2, 3/2, -z) = a e^-z 1F1(1/2 + a/2, 3/2, z) > 0
    kum = all(mp.hyp1f1(1 - a / 2, 1.5, -zz) > 0 for a in (0.5, 1.0) for zz in (0.1, 1, 10, 100, 1000))
    def K_at(T):
        d = [mp.diff(xf, T, n) for n in (0, 1, 2)] + [mp.diff(yf, T, n) for n in (0, 1, 2)]
        return Kf(*d)
    Kmax = max(abs(K_at(T)) for T in [mp.mpf(j) / 2 for j in range(-30, 31)])
    mu = p["xi0"] * p["kc"] ** 2 / 9
    Kcl = 72 * mu ** 2 / yf(0) ** 4
    return dict(zeros=zeros, mono=mono, kummer=kum, Kmax=Kmax, Kratio=Kmax / Kcl, xi0=xf(0), Ymin=yf(0))


def classical_K(Kf):
    """the curvature function checked on Schwarzschild-AdS5: K = 72 mu^2/r^8 + 10 Lambda^2/9"""
    k, x0, Lam = mp.mpf(3), mp.mpf("2.5"), mp.mpf("-0.3")
    Yf = lambda T: mp.sqrt(-2 * k * T / 3)
    xf = lambda T: x0 + 3 / k ** 2 * (Lam * Yf(T) ** 2 / 2 - 3 * Yf(T))
    err = 0
    for T in (mp.mpf(-1), mp.mpf(-3), mp.mpf("-0.2")):
        d = [mp.diff(xf, T, n) for n in (0, 1, 2)] + [mp.diff(Yf, T, n) for n in (0, 1, 2)]
        exact = 72 * x0 ** 2 / Yf(T) ** 4 + 10 * Lam ** 2 / 9
        err = max(err, abs(Kf(*d) / exact - 1))
    return err


def crossing_time():
    """Q9: proper time horizon to horizon over 2 r_h (Lambda_c = 0, sigma r_h^2 small), as Y_min/r_h^2 falls"""
    out = []
    for mu in (1e4, 1e6, 1e8):
        p = dict(kc=30.0, sk=0.5, Lc=0.0, sg=1 / (100 * mu), xi0=mu * 9 / 900)
        kv = {a: kav(a, p) for a in (0.5, -1, -1.5)}
        xf = lambda T: xicf(T, p, kv); yf = lambda T: Ycf(T, p, kv)
        Th = mp.findroot(xf, 3 * mu ** 2 / (2 * p["kc"]))         # classical horizon at T = 3 mu^2/(2k) (Y = mu)
        tau = 2 * mp.quad(lambda T: 1 / (2 * mp.sqrt(xf(T)) * yf(T)), [0, Th / 8, Th / 2, Th])
        out.append(dict(mu=mu, ratio=yf(0) / mu, tau=tau / (2 * mp.sqrt(mu))))
    return out


def scale():
    """Q8: the bounce at x = 1 -- proper time left, and the clock spread it needs, at the record's anchors"""
    QO = _load("quantum_onset.py", "bqm_qo"); CF = _load("core_face.py", "bqm_cf")
    o = QO.onset_4d(); l5, ell = o["l5"], o["ell"]
    out = dict(c1=C1, tau_b=72 ** 0.25 / 2, coef=4 * C1 / (3 * math.pi), l5=l5, ell=ell)
    anchors = {"small end": RH_SMALL ** 2}
    anchors.update({k: v["mu5"] for k, v in CF.core_scales().items()})
    # sigma_Lambda L_z = coef l5/mu; inside the hole Lambda's spread is negligible when sigma mu << 1: L_z >> coef l5;
    # sigma << |Lambda5| = 6/ell^2 when L_z >> coef l5 ell^2/(6 mu)
    out["anchors"] = {k: dict(mu=mu, Ybound=72 ** 0.25 * l5 * math.sqrt(mu), Lz_inside=out["coef"] * l5,
                              Lz_lambda=out["coef"] * l5 * ell ** 2 / (6 * mu)) for k, mu in anchors.items()}
    return out


def compute():
    o = dict(red=reduction(), cl=classical(), eig=eigen(), dfc=deficiency())
    o["st"] = states()
    Kf = kretschmann_eff()
    o["Kcheck"] = classical_K(Kf)
    o["eff"] = effective(Kf, PAR, o["st"]["kv"])
    o["time"] = crossing_time()
    o["scale"] = scale()
    return o


def checks(o):
    red, cl, st, eff = o["red"], o["cl"], o["st"], o["eff"]
    q1 = all(red.values())
    q2 = all(cl.values())
    q3 = o["eig"]
    q4 = o["dfc"]["ok"]
    rows = st["rows"]
    q5 = (all(abs(r["norm"] - 1) < 1e-4 for r in rows) and all(abs(r["Y"] / r["Ycf"] - 1) < 1e-4 for r in rows)
          and min(r["Y"] for r in rows) == rows[2]["Y"] > 0 and st["bh"][0] > 0.999 and st["bh"][2] < 1e-6
          and abs(rows[0]["Y"] / math.sqrt(2 * PAR["kc"] * 40 / 3) - 1) < 0.02)
    a_in, a_out = st["asym"]
    q6 = (all(abs(r["xi"] - r["xicf"]) < 1e-4 for r in rows) and abs(a_in - 0.7) < 1e-2 and abs(a_out - 1.3) < 1e-2
          and abs(rows[0]["xi"] - rows[-1]["xi"]) < 1e-6 and rows[2]["xicf"] > 0 and PAR["xi0"] > 0)
    q7 = eff["zeros"] == 2 and eff["mono"] and eff["kummer"] and o["Kcheck"] < 1e-10 and eff["Kmax"] < mp.inf
    tm = o["time"]
    q9 = all(abs(r["tau"] - 1) < 3 * r["ratio"] for r in tm) and tm[-1]["ratio"] < tm[0]["ratio"] / 50 and \
        abs(tm[-1]["tau"] - 1) < 1e-2
    sc = o["scale"]
    q8 = abs(sc["c1"] - 0.6760) < 1e-3 and abs(sc["tau_b"] - 1.4565) < 1e-3 and all(
        a["Ybound"] > 0 for a in sc["anchors"].values())
    return dict(Q1=q1, Q2=q2, Q3=q3, Q4=q4, Q5=q5, Q6=q6, Q7=q7, Q8=q8, Q9=q9)


def report(o=None):
    o = o or compute()
    ck = checks(o)
    st, eff, sc = o["st"], o["eff"], o["scale"]
    print("Q0 (M's) 536: the bounce defined in quantum physics")
    print("Q1 reduction, Schroedinger form, flat minisuperspace, Laplace-Beltrami: %s %s" % (o["red"], ck["Q1"]))
    print("Q2 classical solutions in T; Schwarzschild-AdS5; the singularity a finite T away: %s %s"
          % (o["cl"], ck["Q2"]))
    print("Q3 exact eigenfunctions: %s" % ck["Q3"])
    print("Q4 deficiency: +i normalisable only for k < 0, -i only for k > 0; extensions exist: %s" % ck["Q4"])
    for r in st["rows"]:
        print("   T = %6.1f  norm %.6f  <Y> %.5f (closed %.5f)  <xi> %.5f (closed %.5f)" % (
            r["T"], r["norm"], r["Y"], r["Ycf"], r["xi"], r["xicf"]))
    print("Q5 unitary through the bounce; the black-hole branch alone keeps %.3g, %.3g, %.3g of the norm at T = -40, 0, "
          "40; <Y> least at T = 0, %.4f > 0: %s" % (tuple(st["bh"]) + (st["rows"][2]["Y"], ck["Q5"])))
    print("Q6 mass: symmetric state xi0 in = out = %.4f; asymmetric state xi0 in %.4f -> out %.4f (beta - in = 1.3): "
          "%s" % (st["rows"][0]["xi"] - float(xicf(-40.0, PAR, st["kv"], beta=0.0)), st["asym"][0], st["asym"][1],
                  ck["Q6"]))
    print("Q7 <xi>: %d zeros, monotone in |T|, Kummer positive; K max %.4g, %.3f of the classical value at Y_min; "
          "K checked on SAdS5 to %.1e: %s" % (eff["zeros"], eff["Kmax"], eff["Kratio"], o["Kcheck"], ck["Q7"]))
    print("Q8 T_left/spread at the bounce %.4f; at x = 1 the proper time left %.4f l5; sigma_Lambda L_z = %.4f l5/mu"
          % (sc["c1"], sc["tau_b"], sc["coef"]))
    for k, a in sc["anchors"].items():
        print("   %-14s mu %.4g m^2  Y_bounce %.4g m^2  inside the hole Lambda's spread negligible for L_z >> %.3g m;"
              " sigma << |Lambda5| for L_z >> %.3g m" % (k, a["mu"], a["Ybound"], a["Lz_inside"], a["Lz_lambda"]))
    print("   %s" % ck["Q8"])
    for r in o["time"]:
        print("Q9 mu %.0e: Y_min/r_h^2 %.4f, proper time across / 2 r_h %.6f" % (r["mu"], r["ratio"], r["tau"]))
    print("   %s" % ck["Q9"])
    return ck


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0
    cases = ("no_wh", "beta_neg", "ordering", "kinetic")
    for m in cases:
        MUT.clear(); MUT.add(m)
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-9s %s" % (m, "caught" if not ok else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(cases)))
    return caught == len(cases)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--selftest" in sys.argv:
        r = selftest(); print("selftest:", "PASS" if r else "FAIL"); sys.exit(0 if r else 1)
    report()
