#!/usr/bin/env python3
"""mots545.py -- item 545: the inner marginally trapped surface the record's scheme shows at the physical wavelength,
investigated.  Labels: computed (exact unless marked), deduced, READ, M's.

  M0 (M's) 545, verbatim: "Does 519 cover this? - no it does not. Please investigate this exhaustively, and report back
     the findings, how it affects the rest of the theorem, and how to mitigate it if it does, or determine if it
     applies at all".
  M1 (deduced; computed exact) The expansion of any T^2-invariant cross-section of the scheme's null slice.  On the
     slice v = const of hf_mirror5's metric (base metric in (v, y, x) as hf_mirror5_derive.einstein writes it, r = y^-2,
     x = cos 2 th, the circles e^{2 Q1}, e^{2 Q2}), the surface y = Y(x) has the null normals l = d_y (tangent to the
     slice, ingoing) and k = d_v + a d_y + b d_x with b = V + 8 Y Y' (1 - x^2) E and a = -Y^3 W/4 + 4 Y'^2 Y (1 - x^2) E,
     E = e^{2(beta + S)}, S = P1 + P2 = y^3 (c^2 G + s^2 F)/3.  Its area element is r^3/4 for every Y, so
         theta_l = -6/y < 0,
         theta_k[Y] = (3/2) Y^2 W + V_x + Y' V_y + 8 E [(1 - x^2)(Y Y'' - 2 Y'^2) - 2 x Y Y'] + 8 Y Y' (1 - x^2)(E_x + E_y Y'),
     every field at (Y(x), x), no v-derivative.  At Y' = 0 it is hf_mirror5 X10's round-sphere expansion exactly
     (checked on slices).  Every zero of theta_k is a marginally trapped surface (theta_l < 0 always).  On Tangherlini
     the round MOTS r = sqrt(mu) is strictly stable: theta_k's linearization about it is -6 Y0 + 8 Y0 (Legendre operator),
     every eigenvalue negative (checked).
  M2 (deduced) The comparison principle.  At a point where Y is greatest (the surface's innermost point), Y' = 0 and
     Y'' <= 0, so theta_k <= the round sphere's expansion there; at its least, >=.  So any MOTS other than the outer one
     has its innermost point where the round spheres are locally untrapped, and where the round spheres are trapped in
     every column of a band, no MOTS has its innermost point in the band.  On Tangherlini, with W < 0 inside, there is
     no MOTS but r = sqrt(mu) among the graphs over the sphere.
  M3 (computed, numerical) The finder.  Newton collocation on the scheme's own Chebyshev x-grid (Nx + 1 points, axes
     included, where the Legendre operator's regularity is automatic), each field interpolated in y along its column by
     its Chebyshev interpolant; converged when |theta_k| < 1e-9 at every node.  Its principal stability eigenvalue, for
     outward deformations, is lambda_1 = -max Re eig(d theta_k/dY): a stable (outermost-type) MOTS has lambda_1 > 0.
     Searched from the outer guess Y = mu^(-1/4), from constant guesses spanning the slice inside it, and from the
     round spheres' inner zero curve where there is one.
  M4 (computed, numerical; pinned) The slices.  The record's scheme is run with growth5's code at the points where it
     reported a second zero: the N1* session's two at 10 l5 (L = 100 and 1000) and derived_go's three at lam_P (copper,
     the example README, r0 = 20 ell).  At each captured slice the round spheres' zero count, the outer MOTS and every
     inner MOTS found are recorded.

Usage: python3 mots545.py --selftest | --mutants | --scan NAME | --report
"""
import importlib.util, json, math, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
G5 = os.path.join(HERE, "..", "n1star", "growth5.py")
DATA = os.path.join(HERE, "data", "mots545_scans.json")
LAM_P = (64*math.pi**2/3)**(1/3)
POINTS = {"L100_10l5": (100.0, 1.0), "L1000_10l5": (1000.0, 10/math.sqrt(1000)),
          "copper": (102.4, LAM_P/math.sqrt(102.4)), "example": (60.9, LAM_P/math.sqrt(60.9)),
          "r0=20ell": (808.5, LAM_P/math.sqrt(808.5))}
FIELDS = ("w", "w_y", "w_x", "q", "q_y", "q_x", "b", "b_y", "b_x", "F", "F_y", "F_x", "G", "G_y", "G_x")
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


# ---------------------------------------------------------------- the slice and theta_k
class Slice:
    """one null slice: the scheme's fields on its grid, with Chebyshev interpolants in y per column"""
    def __init__(s, yex, Ny, Nx, fields, v=None, mu=None):
        s.yex, s.Ny, s.Nx, s.v, s.mu = yex, Ny, Nx, v, mu
        s.t = np.cos(np.pi*np.arange(Ny + 1)/Ny)                 # y = yex (1 - t)/2
        th = np.pi*np.arange(Nx + 1)/Nx
        s.x = np.cos(th)
        s.Dx = cheb_D(Nx)
        s.f = {k: np.asarray(fields[k], float) for k in FIELDS}
        s.c = {k: np.polynomial.chebyshev.chebfit(s.t, s.f[k], Ny) for k in FIELDS}   # shape (Ny+1, Nx+1)

    def at(s, k, Y):
        """field k at y = Y[j] on column j"""
        tt = 1 - 2*np.asarray(Y)/s.yex
        return np.array([np.polynomial.chebyshev.chebval(tt[j], s.c[k][:, j]) for j in range(s.Nx + 1)])

    def theta(s, Y):
        Y = np.asarray(Y, float); x = s.x
        Yp = s.Dx @ Y; Ypp = s.Dx @ Yp
        F = {k: s.at(k, Y) for k in FIELDS}
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


def cheb_D(N):
    x = np.cos(np.pi*np.arange(N + 1)/N)
    c = np.array([2.0] + [1.0]*(N - 1) + [2.0])*(-1)**np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    D = np.outer(c, 1/c)/(X - X.T + np.eye(N + 1))
    return D - np.diag(D.sum(axis=1))


def zeros_per_column(S):
    """count of sign changes of the round spheres' expansion along y in each column, on a fine sampling"""
    T = S.round_theta()
    tt = np.linspace(-1, 1, 4001)
    out, inner = [], []
    for j in range(S.Nx + 1):
        c = np.polynomial.chebyshev.chebfit(S.t, T[:, j], S.Ny)
        f = np.polynomial.chebyshev.chebval(tt, c)
        idx = np.nonzero(np.sign(f[1:]) != np.sign(f[:-1]))[0]
        ys = [S.yex*(1 - tt[i])/2 for i in idx]
        out.append(len(idx)); inner.append(max(ys) if ys else None)
    return out, inner


def newton(S, Y0, tol=1e-9, it=60):
    Y = np.array(Y0, float)
    for _ in range(it):
        r = S.theta(Y)
        if not np.all(np.isfinite(r)):
            return None
        if np.max(np.abs(r)) < tol:
            return Y
        J = np.empty((len(Y), len(Y)))
        h = 1e-7
        for k in range(len(Y)):
            Yk = Y.copy(); Yk[k] += h
            J[:, k] = (S.theta(Yk) - r)/h
        try:
            dY = np.linalg.solve(J, -r)
        except np.linalg.LinAlgError:
            return None
        lam = 1.0
        while lam > 1e-3:
            Yn = Y + lam*dY
            if np.all(Yn > 0) and np.all(Yn < S.yex*1.0000001):
                rn = S.theta(Yn)
                if np.all(np.isfinite(rn)) and np.max(np.abs(rn)) < np.max(np.abs(r)):
                    break
            lam /= 2
        else:
            return None
        Y = Yn
    return Y if np.max(np.abs(S.theta(Y))) < tol else None


def stability(S, Y):
    h = 1e-7
    r = S.theta(Y)
    J = np.empty((len(Y), len(Y)))
    for k in range(len(Y)):
        Yk = Y.copy(); Yk[k] += h
        J[:, k] = (S.theta(Yk) - r)/h
    return float(-np.max(np.linalg.eigvals(J).real))


def find_all(S):
    """the outer MOTS from Y = mu^(-1/4) and every other MOTS from guesses spanning the slice inside it"""
    sols = []
    def add(Y):
        if Y is None:
            return
        for Z in sols:
            if np.max(np.abs(Y - Z)) < 1e-5:
                return
        sols.append(Y)
    n = S.Nx + 1
    y_out = (S.mu if S.mu else 1.0)**-0.25
    add(newton(S, np.full(n, min(y_out, S.yex*0.999))))
    for yc in np.linspace(min(y_out, S.yex)*1.02, S.yex*0.995, 14):
        add(newton(S, np.full(n, yc)))
    zc, inner = zeros_per_column(S)
    if max(zc) > 1:
        guess = np.array([iy if iy is not None else S.yex*0.99 for iy in inner])
        add(newton(S, np.minimum(guess, S.yex*0.999)))
    out = []
    for Y in sorted(sols, key=lambda Z: Z.mean()):
        r = Y**-2
        out.append(dict(r_min=float(r.min()), r_max=float(r.max()), y_max=float(Y.max()),
                        lam1=stability(S, Y), at_excision=bool(Y.max() > S.yex*0.98)))
    return out, max(zc)


# ---------------------------------------------------------------- slices from the scheme
def capture(name, vs, Ny=20, Nx=16):
    """run the record's scheme (growth5.run) at a point and capture the slices at the steps nearest the targets vs"""
    g5, H = load_mods()
    L, lam = POINTS[name]
    targets = sorted(vs); got = {}
    orig = H.rhs
    state = {"i": 0}
    def rhs(g, st, v, data, *a, **k):
        out = orig(g, st, v, data, *a, **k)
        i = state["i"]
        if i < len(targets) and v >= targets[i] - 1e-12:
            d = out[1]
            got[round(v, 6)] = dict(fields={f: np.asarray(d[f]).tolist() for f in FIELDS}, yex=float(g.yex),
                                    mu=float(data.mu_pred(v)))
            state["i"] += 1
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
    rows = []
    for v in sorted(got):
        rec = got[v]
        S = Slice(rec["yex"], Ny, Nx, rec["fields"], v=v, mu=rec["mu"])
        sols, nz = find_all(S)
        rows.append(dict(v=v, mu=rec["mu"], nz=int(nz), mots=sols))
    return rows


# ---------------------------------------------------------------- checks
def tangherlini_slice(Ny=20, Nx=16, yex=1.3, mu=1.0):
    """Tangherlini of mass mu in the scheme's fields: w = -mu y, everything else zero"""
    t = np.cos(np.pi*np.arange(Ny + 1)/Ny); y = yex*(1 - t)/2
    f = {k: np.zeros((Ny + 1, Nx + 1)) for k in FIELDS}
    f["w"] = -mu*y[:, None]*np.ones((1, Nx + 1)); f["w_y"] = -mu*np.ones((Ny + 1, Nx + 1))
    return Slice(yex, Ny, Nx, f, v=0.0, mu=mu)


def checks():
    ok = {}
    ok["M0 M's words, 545"] = words().startswith("Does 519 cover this?")
    T = tangherlini_slice()
    sols, nz = find_all(T)
    ok["M1 Tangherlini: one zero per column, one MOTS at r = sqrt(mu) = 1, strictly stable; no other"] = (
        nz == 1 and len(sols) == 1 and abs(sols[0]["r_min"] - 1) < 1e-7 and abs(sols[0]["r_max"] - 1) < 1e-7
        and sols[0]["lam1"] > 1)
    Tm = tangherlini_slice(mu=1.7)
    sm, _ = find_all(Tm)
    ok["M1 Tangherlini at mu = 1.7: the MOTS at r = 1.7^(1/2)"] = (
        len(sm) == 1 and abs(sm[0]["r_min"] - 1.7**0.5) < 1e-7)
    R = load()
    if PINNED:
        ok["M4 the scans read back as pinned"] = all(
            k in R and summary(R[k]) == pin for k, pin in PINNED.items())
    return ok


def summary(rows):
    """(number of slices with a second round-sphere zero, number with an inner MOTS, least lam1 of an inner MOTS)"""
    nz2 = sum(1 for r in rows if r["nz"] > 1)
    inner = [m for r in rows for m in r["mots"][1:]]
    return [nz2, sum(1 for r in rows if len(r["mots"]) > 1), round(min((m["lam1"] for m in inner), default=0.0), 3)]


PINNED = {}


def load():
    return json.load(open(DATA)) if os.path.exists(DATA) else {}


def selftest(quiet=False):
    ck = checks()
    for k, v in ck.items():
        if not quiet:
            print("[%s] %s" % ("ok" if v else "FAIL", k))
    good = all(ck.values())
    if not quiet:
        print("mots545.py: %d/%d %s" % (sum(ck.values()), len(ck), "pass" if good else "FAIL"))
    return good


def mutants():
    names = ("lap_sign", "drop_shift")
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        bad = not selftest(quiet=True)
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--scan" in sys.argv:
        i = sys.argv.index("--scan")
        name = sys.argv[i + 1]
        vs = [float(a) for a in sys.argv[i + 2:]] if len(sys.argv) > i + 2 else list(np.arange(1.30, 2.21, 0.05))
        rows = scan(name, vs)
        R = load(); R[name] = rows
        json.dump(R, open(DATA, "w"), separators=(",", ":"))
        for r in rows:
            print("v %.4f mu %.4f nz %d  MOTS: %s" % (r["v"], r["mu"], r["nz"],
                  "; ".join("r %.4f-%.4f lam1 %+.3f%s" % (m["r_min"], m["r_max"], m["lam1"],
                                                            " (at excision)" if m["at_excision"] else "")
                            for m in r["mots"])))
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    else:
        sys.exit(0 if selftest() else 1)
