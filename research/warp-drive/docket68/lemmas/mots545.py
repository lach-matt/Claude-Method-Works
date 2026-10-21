#!/usr/bin/env python3
"""mots545.py -- item 545: the inner marginally trapped surface the record's scheme was read as showing at the physical
wavelength, investigated.  Labels: computed (exact unless marked), deduced, READ, M's.  (Docstring completed below.)

Usage: python3 mots545.py --selftest | --mutants | --scan NAME v0 v1 dv [Ny [Nx]] | --report
"""
import importlib.util, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
G5 = os.path.join(HERE, "..", "n1star", "growth5.py")
DATA = os.path.join(HERE, "data", "mots545_scans.json")
SLICE = os.path.join(HERE, "data", "mots545_slice.json")
MITIG = os.path.join(HERE, "data", "mots545_mitigation.json")
LAM_P = (64*math.pi**2/3)**(1/3)
POINTS = {"L100_10l5": (100.0, 1.0), "L1000_10l5": (1000.0, 10/math.sqrt(1000)),
          "copper": (102.4, LAM_P/math.sqrt(102.4)), "example": (60.9, LAM_P/math.sqrt(60.9)),
          "r0=20ell": (808.5, LAM_P/math.sqrt(808.5))}
FIELDS = ("w", "w_y", "w_x", "q", "q_y", "q_x", "b", "b_y", "b_x", "F", "F_y", "F_x", "G", "G_y", "G_x")
NEED = ("w", "q", "q_x", "q_y", "b", "b_y", "b_x", "G", "G_y", "G_x", "F", "F_y", "F_x")
MUT = set()


def words():
    return ("Does 519 cover this? - no it does not. Please investigate this exhaustively, and report back the findings, "
            "how it affects the rest of the theorem, and how to mitigate it if it does, or determine if it applies at all")


def load_mods():
    spec = importlib.util.spec_from_file_location("m5_growth5", G5)
    g5 = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(G5))
    spec.loader.exec_module(g5)
    return g5, g5.H


# ---------------------------------------------------------------- the slice and theta_k (M1)
class Slice:
    """one null slice: the scheme's fields on its grid, with Chebyshev interpolants in y per column"""
    def __init__(s, yex, Ny, Nx, fields, v=None, mu=None):
        s.yex, s.Ny, s.Nx, s.v, s.mu = yex, Ny, Nx, v, mu
        s.t = np.cos(np.pi*np.arange(Ny + 1)/Ny)                 # y = yex (1 - t)/2
        s.x = np.cos(np.pi*np.arange(Nx + 1)/Nx)
        s.Dx = cheb_D(Nx)
        s.f = {k: np.asarray(fields[k], float) for k in FIELDS}
        s.c = {k: np.polynomial.chebyshev.chebfit(s.t, s.f[k], Ny) for k in FIELDS}   # shape (Ny+1, Nx+1)

    def tt(s, Y):
        return 1 - 2*np.asarray(Y)/s.yex

    def at(s, k, Y):
        """field k at y = Y[j] on column j"""
        tt = s.tt(Y)
        return np.array([np.polynomial.chebyshev.chebval(tt[j], s.c[k][:, j]) for j in range(s.Nx + 1)])

    def theta(s, Y):
        Y = np.asarray(Y, float); x = s.x
        Yp = s.Dx @ Y; Ypp = s.Dx @ Yp
        F = {k: s.at(k, Y) for k in NEED}
        c2, s2 = (1 + x)/2, (1 - x)/2
        W = 1 + Y**3*F["w"]
        Vx = Y**5*(-2*x*F["q"] + (1 - x**2)*F["q_x"])
        Vy = 5*Y**4*(1 - x**2)*F["q"] + Y**5*(1 - x**2)*F["q_y"]
        beta, beta_y, beta_x = Y**6*F["b"], 6*Y**5*F["b"] + Y**6*F["b_y"], Y**6*F["b_x"]
        cs = c2*F["G"] + s2*F["F"]
        S = Y**3*cs/3
        S_y = Y**2*cs + Y**3*(c2*F["G_y"] + s2*F["F_y"])/3
        S_x = Y**3*((F["G"] - F["F"])/2 + c2*F["G_x"] + s2*F["F_x"])/3
        E = np.exp(2*(beta + S))
        E_y, E_x = 2*E*(beta_y + S_y), 2*E*(beta_x + S_x)
        lap = (1 - x**2)*(Y*Ypp - 2*Yp**2) - 2*x*Y*Yp
        if "lap_sign" in MUT:
            lap = -lap
        th = 1.5*Y**2*W + Vx + Yp*Vy + 8*E*lap + 8*Y*Yp*(1 - x**2)*(E_x + E_y*Yp)
        if "drop_shift" in MUT:
            th = th - Vx - Yp*Vy
        return th

    def round_theta(s):
        """the round spheres' expansion on the grid, (3/2) y^2 [W + (2/3) y^3 d_x((1 - x^2) q)] -- X10's form"""
        y = s.yex*(1 - s.t)/2
        Yg = y[:, None]*np.ones((1, s.Nx + 1)); X = s.x[None, :]*np.ones((s.Ny + 1, 1))
        W = 1 + Yg**3*s.f["w"]
        T = W + (2/3)*Yg**3*(((1 - X**2)*s.f["q"]) @ s.Dx.T)
        return 1.5*Yg**2*T


class SliceC(Slice):
    """past the core boundary each field continues by its value there: a test leaf may pass the boundary, and only its
    part in the domain is ever compared with a marginally trapped surface, which lies in the domain (M6)"""
    def tt(s, Y):
        return np.maximum(1 - 2*np.asarray(Y)/s.yex, -1.0)


def cheb_D(N):
    x = np.cos(np.pi*np.arange(N + 1)/N)
    c = np.array([2.0] + [1.0]*(N - 1) + [2.0])*(-1)**np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    D = np.outer(c, 1/c)/(X - X.T + np.eye(N + 1))
    return D - np.diag(D.sum(axis=1))


def round_profile(S, ny=2000):
    """the round spheres' expansion on a fine y-grid per column: (yy, T[j, i]) and the outer zero per column"""
    T = S.round_theta()
    yy = np.linspace(0.3, S.yex, ny); tt = 1 - 2*yy/S.yex
    Tc = np.array([np.polynomial.chebyshev.chebval(tt, np.polynomial.chebyshev.chebfit(S.t, T[:, j], S.Ny))
                   for j in range(S.Nx + 1)])
    outer = []
    for j in range(S.Nx + 1):
        sg = np.sign(Tc[j]); i = np.nonzero(sg[1:] != sg[:-1])[0]
        outer.append(yy[i[0]] if len(i) else np.nan)
    return yy, Tc, np.array(outer)


def zeros_per_column(S):
    """count of sign changes of the round spheres' expansion along y in each column, on a fine sampling"""
    T = S.round_theta()
    tt = np.linspace(-1, 1, 4001)
    out = []
    for j in range(S.Nx + 1):
        f = np.polynomial.chebyshev.chebval(tt, np.polynomial.chebyshev.chebfit(S.t, T[:, j], S.Ny))
        out.append(int((np.sign(f[1:]) != np.sign(f[:-1])).sum()))
    return out


def newton(S, Y0, c=0.0, tol=1e-9, it=60, ymax=None):
    """collocation Newton for theta_k[Y] = c on the scheme's x-grid (axes included)"""
    ymax = S.yex*1.0000001 if ymax is None else ymax
    Y = np.array(Y0, float)
    for _ in range(it):
        r = S.theta(Y) - c
        if not np.all(np.isfinite(r)):
            return None
        if np.max(np.abs(r)) < tol:
            return Y
        J = np.empty((len(Y), len(Y))); h = 1e-7
        for k in range(len(Y)):
            Yk = Y.copy(); Yk[k] += h
            J[:, k] = (S.theta(Yk) - c - r)/h
        try:
            dY = np.linalg.solve(J, -r)
        except np.linalg.LinAlgError:
            return None
        lam = 1.0
        while lam > 1e-4:
            Yn = Y + lam*dY
            if np.all(Yn > 0) and np.all(Yn < ymax):
                rn = S.theta(Yn) - c
                if np.all(np.isfinite(rn)) and np.max(np.abs(rn)) < np.max(np.abs(r)):
                    break
            lam /= 2
        else:
            return None
        Y = Yn
    return Y if np.max(np.abs(S.theta(Y) - c)) < tol else None


def stability(S, Y):
    """lambda_1 = -max Re eig(d theta_k/dY): > 0 for a strictly stable (outermost-type) surface"""
    h = 1e-7
    r = S.theta(Y)
    J = np.empty((len(Y), len(Y)))
    for k in range(len(Y)):
        Yk = Y.copy(); Yk[k] += h
        J[:, k] = (S.theta(Yk) - r)/h
    return float(-np.max(np.linalg.eigvals(J).real))


# ---------------------------------------------------------------- the exhaustive search by shooting (M5)
class Field2:
    """every needed field as one tensor Chebyshev interpolant in (t, x) -- the scheme's own representation"""
    def __init__(s, S):
        s.S = S
        V = lambda z, N: np.cos(np.outer(np.arccos(np.clip(z, -1, 1)), np.arange(N + 1)))
        It, Ix = np.linalg.inv(V(S.t, S.Ny)), np.linalg.inv(V(S.x, S.Nx))
        s.C = np.array([It @ S.f[k] @ Ix.T for k in NEED])

    def eval(s, Y, x):
        t = 1 - 2*np.asarray(Y)/s.S.yex
        n = np.arange(s.S.Ny + 1)
        Tt = np.cos(np.outer(np.arccos(np.clip(t, -1, 1)), n))
        out = np.abs(t) > 1
        if out.any():
            Tt[out] = np.sign(t[out])[:, None]**n*np.cosh(np.outer(np.arccosh(np.abs(t[out])), n))
        Tx = np.cos(np.arccos(np.clip(x, -1, 1))*np.arange(s.S.Nx + 1))
        return (s.C @ Tx) @ Tt.T


def parts(F2, Y, psi):
    x = -np.cos(psi); sn = np.sin(psi)
    w, q, q_x, q_y, b, b_y, b_x, G, G_y, G_x, Fm, F_y, F_x = F2.eval(Y, x)
    W = 1 + Y**3*w
    Vx = Y**5*(-2*x*q + (1 - x**2)*q_x)
    Vyt = 5*Y**4*q + Y**5*q_y
    c2, s2 = (1 + x)/2, (1 - x)/2
    cs = c2*G + s2*Fm
    Sx = Y**3*cs/3
    S_y = Y**2*cs + Y**3*(c2*G_y + s2*F_y)/3
    S_x = Y**3*((G - Fm)/2 + c2*G_x + s2*F_x)/3
    beta = Y**6*b; beta_y = 6*Y**5*b + Y**6*b_y; beta_x = Y**6*b_x
    E = np.exp(2*(beta + Sx)); E_y = 2*E*(beta_y + S_y); E_x = 2*E*(beta_x + S_x)
    return x, sn, W, Vx, Vyt, E, E_x, E_y


def _rhs(F2, psi, Y, P, c):
    """theta_k = c as Y_psipsi, x = -cos psi: 8 E Y (Y_psipsi + cot psi Y_psi) = c - (3/2) Y^2 W - V_x - ..."""
    x, sn, W, Vx, Vyt, E, E_x, E_y = parts(F2, Y, psi)
    br = c - 1.5*Y**2*W - Vx - P*sn*Vyt + 16*E*P**2 - 8*Y*P*(sn*E_x + E_y*P)
    return br/(8*E*Y) - (np.cos(psi)/sn)*P


def _axis(F2, Y, psi, c):
    x, sn, W, Vx, Vyt, E, E_x, E_y = parts(F2, Y, psi)
    return (c - 1.5*Y**2*W - Vx)/(16*E*Y)


def shoot(F2, Y0, c=0.0, n=3000, eps=2e-3, ymin=0.0, keep=False):
    """the regular solution from the axis x = -1 with Y(-1) = Y0, by RK4 on a mesh graded toward both axes; returns
    C, the singular solution's coefficient at x = +1 (zero exactly for a closed surface), and a status per shot
    (0 in the domain, +1 left into the core, -1 left outward, 2 not finite)"""
    Y0 = np.atleast_1d(np.asarray(Y0, float))
    a = _axis(F2, Y0, 0.0, c)
    Y = Y0 + 0.5*a*eps**2; P = a*eps
    tau = np.linspace(np.arccos(1 - 2*eps/np.pi), np.arccos(-1 + 2*eps/np.pi), n + 1)
    psis = np.pi*(1 - np.cos(tau))/2
    st = np.zeros(len(Y0), int)
    path = [Y.copy()] if keep else None
    for k in range(n):
        p0, p1 = psis[k], psis[k + 1]; h = p1 - p0; pm = 0.5*(p0 + p1)
        ok = st == 0
        if not ok.any():
            break
        y, pp = Y[ok], P[ok]
        k1y, k1p = pp, _rhs(F2, p0, y, pp, c)
        k2y, k2p = pp + 0.5*h*k1p, _rhs(F2, pm, y + 0.5*h*k1y, pp + 0.5*h*k1p, c)
        k3y, k3p = pp + 0.5*h*k2p, _rhs(F2, pm, y + 0.5*h*k2y, pp + 0.5*h*k2p, c)
        k4y, k4p = pp + h*k3p, _rhs(F2, p1, y + h*k3y, pp + h*k3p, c)
        Y[ok] = y + h/6*(k1y + 2*k2y + 2*k3y + k4y)
        P[ok] = pp + h/6*(k1p + 2*k2p + 2*k3p + k4p)
        bad = ~np.isfinite(Y) | ~np.isfinite(P)
        st[ok & (Y > F2.S.yex)] = 1; st[ok & (Y < ymin)] = -1; st[bad & (st == 0)] = 2
        if keep:
            path.append(Y.copy())
    pe = psis[-1]
    C = np.sin(pe)*(P - _axis(F2, Y, np.pi, c)*(pe - np.pi))
    C[st != 0] = np.nan
    return (C, st, psis, np.array(path)) if keep else (C, st)


def roots(F2, lo, hi, c=0.0, n0=600, ymin=0.0, rounds=6, tol=1e-6):
    """every closed surface theta_k = c with axis value in (lo, hi): each sign change of C, a shot that leaves the
    domain counting as +-inf on its side, refined by multisection and kept only if the refined shot stays in the domain
    with |C| < tol"""
    def ext(C, st):
        Ce = C.copy(); Ce[st == 1] = np.inf; Ce[st == -1] = -np.inf; Ce[st == 2] = np.nan
        if "no_exit_inf" in MUT:
            Ce[st != 0] = np.nan
        return Ce
    Y0 = np.linspace(lo, hi, n0)
    Ce = ext(*shoot(F2, Y0, c=c, ymin=ymin))
    br = [(Y0[i], Y0[i + 1], Ce[i], Ce[i + 1]) for i in range(n0 - 1)
          if (np.isfinite(Ce[i]) or np.isfinite(Ce[i + 1])) and not np.isnan(Ce[i]) and not np.isnan(Ce[i + 1])
          and np.sign(Ce[i]) != np.sign(Ce[i + 1])]
    for _ in range(rounds):
        if not br:
            break
        pts = np.concatenate([np.linspace(a, b, 10)[1:-1] for a, b, _, _ in br])
        ce = ext(*shoot(F2, pts, c=c, ymin=ymin))
        nb = []
        for k, (a, b, ca, cb) in enumerate(br):
            ys = np.concatenate([[a], pts[8*k:8*k + 8], [b]])
            cs = np.concatenate([[ca], ce[8*k:8*k + 8], [cb]])
            for j in range(9):
                if not np.isnan(cs[j]) and not np.isnan(cs[j + 1]) and np.sign(cs[j]) != np.sign(cs[j + 1]):
                    nb.append((ys[j], ys[j + 1], cs[j], cs[j + 1])); break
        br = nb
    good = []
    for a, b, _, _ in br:
        m = 0.5*(a + b)
        cm, sm = shoot(F2, [m], c=c, ymin=ymin)
        if sm[0] == 0 and abs(cm[0]) < tol:
            good.append(m)
    return good


def leaf_nodes(S, F2, y0, c=0.0):
    """the shot from Y(-1) = y0 sampled at the scheme's x-nodes (a Newton start)"""
    C, st, psis, path = shoot(F2, [y0], c=c, keep=True)
    return np.interp(S.x, (-np.cos(psis))[::-1], path[::-1, 0])


# ---------------------------------------------------------------- the sweep (M6)
def sweep(S, Ystar, sign=-1, dc=0.05, cmax=500.0, stop_y=None, beyond=3.0):
    """closed leaves theta_k = c continued from the outer MOTS (c = 0): inward (sign -1, c < 0) until a leaf lies wholly
    past the core boundary, outward (sign +1) until a leaf lies wholly outside the least round zero (stop_y).  Each
    leaf must lie strictly beyond the last at every node; the step halves on failure down to dc/64"""
    if "leaf_sign" in MUT:
        sign = -sign
    leaves = [(0.0, Ystar.copy())]
    c, Y, h, why = 0.0, Ystar.copy(), dc, "c limit"
    while abs(c) < cmax:
        cn = c + sign*h
        guess = Y + (Y - leaves[-2][1])*(h/abs(leaves[-1][0] - leaves[-2][0])) if len(leaves) > 1 else Y
        Yn = newton(S, guess, c=cn, ymax=S.yex*beyond)
        ok = Yn is not None and (np.all(Yn > Y) if sign < 0 else np.all(Yn < Y))
        if not ok:
            if h > dc/64:
                h /= 2; continue
            why = "no further nested leaf" if Yn is None else "not nested"
            break
        leaves.append((cn, Yn)); c, Y = cn, Yn
        h = min(h*1.5, 4*dc)
        if sign > 0 and stop_y is not None and Y.max() < stop_y:
            why = "outside every round zero"; break
        if sign < 0 and Y.min() >= S.yex:
            why = "wholly past the core boundary"; break
    return leaves, why


def fine_theta(S, F2, Yn, nfine=401):
    """theta_k of a leaf (its Chebyshev interpolant through the nodes) on a fine x-grid, the fields from the tensor
    interpolant; nan where the leaf is past the core boundary"""
    cY = np.polynomial.chebyshev.chebfit(S.x, Yn, S.Nx)
    xs = np.cos(np.linspace(0, np.pi, nfine))
    Y = np.polynomial.chebyshev.chebval(xs, cY)
    Yp = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebder(cY))
    Ypp = np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebder(cY, 2))
    th = np.full(nfine, np.nan)
    inn = Y <= S.yex
    for i in np.nonzero(inn)[0]:
        x, y, yp, ypp = xs[i], Y[i], Yp[i], Ypp[i]
        _, _, W, Vx, Vyt, E, E_x, E_y = [np.atleast_1d(a)[0] for a in parts(F2, np.array([y]), np.arccos(-x))]
        th[i] = (1.5*y**2*W + Vx + yp*(1 - x**2)*Vyt + 8*E*((1 - x**2)*(y*ypp - 2*yp**2) - 2*x*y*yp)
                 + 8*y*yp*(1 - x**2)*(E_x + E_y*yp))
    return th


def nested_fine(S, Ya, Yb, nfine=401):
    """least of Yb - Ya over a fine x-grid (both interpolated through the nodes)"""
    xs = np.cos(np.linspace(0, np.pi, nfine))
    return float(np.polynomial.chebyshev.chebval(xs, np.polynomial.chebyshev.chebfit(S.x, Yb - Ya, S.Nx)).min())


def analyse(S):
    """one slice: the round picture, every T^2-invariant MOTS (M5) and the two sweeps (M6)"""
    F2 = Field2(S)
    yy, Tc, outer = round_profile(S)
    T = S.round_theta()
    trapped = yy[(Tc < 0).all(axis=0)]
    ylo = 0.5*np.nanmin(outer)
    mots = []
    for y0 in roots(F2, ylo, S.yex*0.9999, ymin=0.25*ylo):
        Yn = newton(S, leaf_nodes(S, F2, y0))
        if Yn is None:
            mots.append(dict(y0=float(y0), polished=False)); continue
        mots.append(dict(y0=float(y0), polished=True, r_min=float((Yn**-2).min()), r_max=float((Yn**-2).max()),
                         lam1=stability(S, Yn), Y=Yn.tolist()))
    sw = None
    good = [m for m in mots if m["polished"]]
    if len(good) == 1:
        Ystar = np.array(good[0]["Y"])
        SC = SliceC(S.yex, S.Ny, S.Nx, S.f, v=S.v, mu=S.mu)
        Lin, why_in = sweep(SC, Ystar, sign=-1)
        Lout, why_out = sweep(S, Ystar, sign=+1, stop_y=np.nanmin(outer))
        th_in = [np.nanmax(np.append(fine_theta(S, F2, Y), -np.inf)) for _, Y in Lin[1:]]
        th_out = [np.nanmin(np.append(fine_theta(S, F2, Y), np.inf)) for _, Y in Lout[1:]]
        sw = dict(n_in=len(Lin) - 1, c_in=Lin[-1][0], why_in=why_in,
                  pocket=int((Lin[-1][1] < S.yex).sum()),
                  th_in=float(max(th_in)) if th_in else None,
                  gap_in=min([nested_fine(S, A, B) for (_, A), (_, B) in zip(Lin[:-1], Lin[1:])] or [np.nan]),
                  n_out=len(Lout) - 1, c_out=Lout[-1][0], why_out=why_out,
                  th_out=float(min(th_out)) if th_out else None,
                  gap_out=min([nested_fine(S, B, A) for (_, A), (_, B) in zip(Lout[:-1], Lout[1:])] or [np.nan]))
        sw["unique"] = bool(why_in == "wholly past the core boundary" and why_out == "outside every round zero"
                            and sw["th_in"] is not None and sw["th_in"] < 0 and sw["gap_in"] > 0
                            and sw["th_out"] is not None and sw["th_out"] > 0 and sw["gap_out"] > 0)
    for m in mots:
        m.pop("Y", None)
    return dict(v=S.v, mu=S.mu, nz=int(max(zeros_per_column(S))), Wex=float((1 + S.yex**3*S.f["w"][-1]).max()),
                Tex=float(T[-1].max()), band=[float(trapped.max()**-2), float(trapped.min()**-2)] if len(trapped)
                else None, r_core=float(S.yex**-2), mots=mots, sweep=sw)


# ---------------------------------------------------------------- slices from the scheme (M8)
def capture(name, vs, Ny=20, Nx=16):
    """run the record's scheme (growth5.run) at a point and capture the accepted slices at the steps nearest vs"""
    g5, H = load_mods()
    L, lam = POINTS[name]
    targets = sorted(vs); got = {}
    orig = H.rhs
    state = {"i": 0, "n": 0}
    def rhs(g, st, v, data, *a, **k):
        out = orig(g, st, v, data, *a, **k)
        i, n = state["i"], state["n"]
        state["n"] += 1                       # growth5.run calls rhs four times a step; the first is the accepted state
        if n % 4 == 0 and i < len(targets) and v >= targets[i] - 1e-12:
            while state["i"] < len(targets) and v >= targets[state["i"]] - 1e-12:
                state["i"] += 1
            got[round(v, 6)] = dict(fields={f: np.asarray(out[1][f]).tolist() for f in FIELDS}, yex=float(g.yex),
                                    mu=float(data.mu_pred(v)))
            if state["i"] == len(targets):
                raise ValueError("captured")
        return out
    H.rhs = rhs
    try:
        g5.run(L, lam, Ny, Nx, log=lambda *a: None)
    finally:
        H.rhs = orig
    return got


def scan(name, vs, Ny=20, Nx=16):
    got = capture(name, vs, Ny, Nx)
    return [analyse(Slice(rec["yex"], Ny, Nx, rec["fields"], v=v, mu=rec["mu"])) for v, rec in sorted(got.items())]


def summary(rows):
    """per point: slices; slices with a second round zero; slices with W_ex < 0 (the scheme valid); slices where the
    exhaustive search found any MOTS but the outer one; slices where the sweeps prove the outer one unique; least
    lambda_1 of the outer one"""
    valid = [r for r in rows if r["Wex"] < 0]
    inner = sum(1 for r in rows if len(r["mots"]) != 1) if "count_all" not in MUT else len(rows)
    return dict(n=len(rows), nz2=sum(1 for r in rows if r["nz"] > 1), valid=len(valid), not_one=inner,
                unique_valid=sum(1 for r in valid if r["sweep"] and r["sweep"]["unique"]),
                lam1_min=round(min(m["lam1"] for r in rows for m in r["mots"] if m.get("polished")), 2))


# ---------------------------------------------------------------- checks
def tangherlini_slice(Ny=20, Nx=16, yex=1.3, mu=1.0):
    """Tangherlini of mass mu in the scheme's fields: w = -mu y, everything else zero"""
    t = np.cos(np.pi*np.arange(Ny + 1)/Ny); y = yex*(1 - t)/2
    f = {k: np.zeros((Ny + 1, Nx + 1)) for k in FIELDS}
    f["w"] = -mu*y[:, None]*np.ones((1, Nx + 1)); f["w_y"] = -mu*np.ones((Ny + 1, Nx + 1))
    return Slice(yex, Ny, Nx, f, v=0.0, mu=mu)


def stored_slice():
    d = json.load(open(SLICE))
    return Slice(d["yex"], d["Ny"], d["Nx"], d["fields"], v=d["v"], mu=d["mu"])


def legendre_identity():
    """u = 1/Y: Y (Lap Y) - 2 |grad Y|^2 = -u^-3 Lap u for the S^3 Laplacian on T^2-invariant functions (M4)"""
    import sympy as sp
    x = sp.symbols("x"); u = sp.Function("u")(x); Y = 1/u
    L = lambda f: 4*((1 - x**2)*sp.diff(f, x, 2) - 2*x*sp.diff(f, x))          # Lap_{S^3} on f(x), x = cos 2 th
    g2 = lambda f: 4*(1 - x**2)*sp.diff(f, x)**2                                 # |grad f|^2
    return sp.simplify(Y*L(Y) - 2*g2(Y) + L(u)/u**3) == 0


PINNED = {}
PIN_RES = {}
PIN_MIT = {}


def load(path=DATA):
    return json.load(open(path)) if os.path.exists(path) else {}


def checks(fast=False):
    ok = {}
    ok["M0 M's words, 545"] = words().startswith("Does 519 cover this?")
    T = tangherlini_slice()
    sol = analyse(T)
    ok["M4 Tangherlini: the exhaustive search finds one MOTS, r = sqrt(mu) = 1, strictly stable"] = (
        len(sol["mots"]) == 1 and abs(sol["mots"][0]["r_min"] - 1) < 1e-6 and abs(sol["mots"][0]["r_max"] - 1) < 1e-6
        and sol["mots"][0]["lam1"] > 1)
    ok["M4 Tangherlini: the sweeps leave no room for a MOTS of any shape but it"] = bool(
        sol["sweep"] and sol["sweep"]["unique"])
    ok["M4 the identity behind uniqueness on Tangherlini's null slices for every shape (sympy)"] = legendre_identity()
    S = stored_slice()
    jj = 12
    yk = S.yex*(1 - S.t[jj])/2
    rt = S.round_theta()[jj]
    ok["M1 on the record's slice (copper, v = %.3f): theta_k of a round sphere is X10's round expansion in every "
       "column, to the x-grid's aliasing" % S.v] = bool(
        np.max(np.abs(S.theta(np.full(S.Nx + 1, yk)) - rt)) < 1e-4*max(1.0, np.abs(rt).max()))
    if not fast:
        a = analyse(S)
        ok["M5-M6 on the record's slice (copper, v = %.3f, %d round zeros in a column): one MOTS, unique by the "
           "sweeps" % (S.v, a["nz"])] = (len(a["mots"]) == 1 and a["mots"][0]["lam1"] > 1 and a["nz"] >= 2
                                         and bool(a["sweep"] and a["sweep"]["unique"]))
    R = load()
    if PINNED:
        ok["M8 the five points' scans read back as pinned"] = all(
            k in R and summary(R[k]) == pin for k, pin in PINNED.items())
    if PIN_RES:
        ok["M9 the resolution scans read back as pinned"] = all(
            k in R and summary(R[k]) == pin for k, pin in PIN_RES.items())
    if PIN_MIT:
        Mt = load(MITIG)
        ok["M10 the mitigation runs read back as pinned"] = all(
            k in Mt and {kk: Mt[k][kk] for kk in pin} == pin for k, pin in PIN_MIT.items())
    return ok


def selftest(quiet=False, fast=False):
    ck = checks(fast=fast)
    for k, v in ck.items():
        if not quiet:
            print("[%s] %s" % ("ok" if v else "FAIL", k))
    good = all(ck.values())
    if not quiet:
        print("mots545.py: %d/%d %s" % (sum(ck.values()), len(ck), "pass" if good else "FAIL"))
    return good


def mutants():
    names = ("lap_sign", "drop_shift", "leaf_sign", "count_all")
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        bad = not selftest(quiet=True, fast=(m != "leaf_sign"))
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


def report():
    R = load()
    for k, rows in R.items():
        print(k, summary(rows))


if __name__ == "__main__":
    if "--scan" in sys.argv:
        i = sys.argv.index("--scan")
        name = sys.argv[i + 1]; v0, v1, dv = map(float, sys.argv[i + 2:i + 5])
        Ny = int(sys.argv[i + 5]) if len(sys.argv) > i + 5 else 20
        Nx = int(sys.argv[i + 6]) if len(sys.argv) > i + 6 else 16
        rows = scan(name, list(np.round(np.arange(v0, v1 + 1e-9, dv), 6)), Ny, Nx)
        key = name if (Ny, Nx) == (20, 16) else "%s_%dx%d" % (name, Ny, Nx)
        R = load(); R[key] = rows
        json.dump(R, open(DATA, "w"), separators=(",", ":"))
        print(key, summary(rows))
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    elif "--report" in sys.argv:
        report()
    else:
        sys.exit(0 if selftest() else 1)
