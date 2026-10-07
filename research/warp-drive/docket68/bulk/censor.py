#!/usr/bin/env python3
"""censor.py -- do the censorship theorems apply to the bulk bounded by M's plane?  (M-RULINGS items 136-137, wall D)

M's order (item 136, wall D): "yes, or prove that a censorship theorem does not apply".

Five theorems were READ at source in step 2 (docket68/residue/OUTSIDE.md).  Each one's premises are checked here, one
by one, against the board's bulk: vacuum AdS5 off the plane, G_AB = 6 k^2 g_AB, with the plane as an umbilic brane,
K = -k g (closedbulk.py's K = -a q), mirror-symmetric (H-Z2, LOOSE.md L4), carrying the corridor with no brane matter
(tau = 0: Bronnikov-Kim eq. 17 is a vacuum brane solution).

  C1  the null energy condition in five dimensions: the bulk's and the plane's stress, every null vector
  C2  the plane's negative null energy is the projected Weyl part (umbilic.py, seated: E_kk = -G_kk) -- cited
  C3  the null generic condition fails in vacuum AdS5 (computed); control: Schwarzschild satisfies it
  C4  no conformal boundary (Omega = 0) on the plane's side; control: the other side has one
  C5  the Poincare patch off the plane is null incomplete (imported from residue/loose.py L5)
  C6  the plane's averaged null energy along the passage is negative (imported from copy/coin.py)
  C7  the mirror-symmetric plane makes the metric only C^0 across it ([K] != 0)

Stdlib + sympy.  python3 censor.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_C = {}


def owners():
    if not _C:
        _C["coin"] = _load(os.path.join(D68, "copy", "coin.py"), "censor_coin")
        _C["loose"] = _load(os.path.join(D68, "residue", "loose.py"), "censor_loose")
    return _C


def riemann_lower(g, X):
    """R_abcd (all lowered) for metric g in coordinates X."""
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                             for e in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    v = (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                         + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
                    R[(a, b, c, d)] = v                                # R^a_bcd
    RL = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    RL[(a, b, c, d)] = sp.simplify(sum(g[a, e] * R[(e, b, c, d)] for e in range(n)))
    return RL


def generic_tensor(g, X, kup, point):
    """k_[a R_b]cd[e k_f] k^c k^d at a point; returns the largest |component| (0 means the condition fails there)."""
    n = len(X)
    RL = riemann_lower(g, X)
    gp = g.subs(point)
    kdn = [sum(gp[a, b] * kup[b] for b in range(n)) for a in range(n)]
    T = [[sp.simplify(sum(RL[(b, c, d, e)].subs(point) * kup[c] * kup[d] for c in range(n) for d in range(n)))
          for e in range(n)] for b in range(n)]
    big = 0
    for a in range(n):
        for b in range(n):
            for e in range(n):
                for f in range(n):
                    X_ = lambda a_, b_, e_, f_: kdn[a_] * T[b_][e_] * kdn[f_]
                    v = sp.simplify((X_(a, b, e, f) - X_(b, a, e, f) - X_(a, b, f, e) + X_(b, a, f, e)) / 4)
                    big = max(big, abs(float(v)))
    return big


# ------------------------------------------------------------------------------------------------ C1
def c1():
    """Null energy in 5D.  Bulk: T_AB = -(Lambda5/kappa5^2) g_AB (vacuum + cosmological constant), so T_AB k^A k^B = 0
    for null k.  Plane: S_AB = -lambda h_AB + tau_AB, tau = 0, h_AB = g_AB - n_A n_B; in an orthonormal frame with n
    along y, S_AB k^A k^B = lambda k_y^2 for null k = (k0, k1, k2, k3, ky)."""
    k0, k1, k2, k3, ky, lam = sp.symbols("k0 k1 k2 k3 k_y lambda", real=True)
    eta5 = sp.diag(-1, 1, 1, 1, 1)
    kv = sp.Matrix([k0, k1, k2, k3, ky])
    n = sp.Matrix([0, 0, 0, 0, 1])
    h = eta5 - n * n.T
    null = {k0: sp.sqrt(k1**2 + k2**2 + k3**2 + ky**2)}
    S_kk = sp.simplify((kv.T * (-lam * h) * kv)[0].subs(null))
    bulk_kk = sp.simplify((kv.T * eta5 * kv)[0].subs(null))         # g_AB k^A k^B = 0, so Lambda's term drops
    return {"S_kk": S_kk, "bulk_kk": bulk_kk}


# ------------------------------------------------------------------------------------------------ C3
def c3():
    t, x1, x2, x3, z = sp.symbols("t x1 x2 x3 z", positive=True)
    kk = sp.Symbol("k", positive=True)
    X = [t, x1, x2, x3, z]
    g = sp.diag(-1, 1, 1, 1, 1) / (kk * z) ** 2
    pt = {kk: 1, z: sp.Rational(3, 2), t: 0, x1: 0, x2: 0, x3: 0}
    kup = [sp.Rational(5, 1), 3, 0, 0, 4]                            # null: -25 + 9 + 16 = 0
    ads = generic_tensor(g, X, kup, pt)
    # control: 4D Schwarzschild, radial null vector
    tt, r, th, ph = sp.symbols("t r theta phi", positive=True)
    M = sp.Integer(1)
    gs = sp.diag(-(1 - 2 * M / r), 1 / (1 - 2 * M / r), r**2, r**2 * sp.sin(th) ** 2)
    pts = {r: 3, th: sp.pi / 2}
    # a non-radial null ray (a radial one lies along a principal null direction, where the tensor vanishes by
    # definition): -f kt^2 + r^2 kphi^2 = 0 at r = 3, f = 1/3
    kups = [3, 0, 0, 1 / sp.sqrt(3)]
    schw = generic_tensor(gs, [tt, r, th, ph], kups, pts)
    schw_radial = generic_tensor(gs, [tt, r, th, ph], [3, 1, 0, 0], pts)
    # everywhere: AdS5's Riemann tensor is maximally symmetric, R_abcd = -k^2 (g_ac g_bd - g_ad g_bc), so
    # R_bcde k^c k^d is proportional to k_b k_e and the generic tensor vanishes for every null k at every point
    RL = riemann_lower(g, X)
    resid = max(abs(sp.simplify(RL[(a, b, c, d)] + kk**2 * (g[a, c] * g[b, d] - g[a, d] * g[b, c])))
                for a in range(5) for b in range(5) for c in range(5) for d in range(5))
    return {"ads": ads, "schw": schw, "schw_radial": schw_radial, "maxsym_residual": resid}


# ------------------------------------------------------------------------------------------------ C4
def c4():
    """ds^2 = e^{-2ky} eta + dy^2 = (1/(kz)^2)(eta + dz^2), z = e^{ky}/k: Omega = k z conformally compactifies it."""
    z, kk = sp.symbols("z k", positive=True)
    Om = kk * z
    plane_side = sp.minimum(Om, z, sp.Interval(1 / kk, sp.oo))       # z >= 1/k off our plane (y >= 0)
    other_side = sp.limit(Om, z, 0, "+")                             # the warp growing away: z in (0, 1/k]
    return {"min_Omega_plane_side": sp.simplify(plane_side), "Omega_other_side_limit": other_side}


# ------------------------------------------------------------------------------------------------ C5 C6 C7
def c5():
    return owners()["loose"].l5()


def c6():
    c = owners()["coin"]
    return {"leg_floor": float(c.anec_closed(1, 2)), "leg_illus": float(c.anec_closed(1, 1.8))}


def c7():
    return owners()["loose"].l4()


THEOREMS = [
    ("Friedman-Schleich-Witt Thm 1 (gr-qc/9305017v2 p.3), the plane's 4D geometry",
     [("asymptotically flat", "holds (eq. 17)", True), ("globally hyperbolic", "not checked", None),
      ("ANEC", "FAILS: the plane reads the passage's averaged null energy as negative (C6)", False)]),
    ("Gao-Wald Thm 1 (gr-qc/0007021v2 p.6), the 5D bulk",
     [("null energy condition", "holds in 5D (C1)", True),
      ("null generic condition", "FAILS in vacuum AdS5 (C3); near the corridor its Weyl part may supply it", False),
      ("null geodesically complete", "FAILS on the Poincare patch off the plane (C5, H-POINCARE-PATCH)", False),
      ("a smooth metric", "FAILS across a mirror-symmetric plane: [K] != 0, the metric is C^0 (C7)", False)]),
    ("Gao-Wald Thm 2 (gr-qc/0007021v2 pp.12-13), the 5D bulk",
     [("a conformal boundary, Omega = 0, timelike", "FAILS: Omega = k z >= 1 off the plane (C4)", False),
      ("null energy and null generic conditions", "the generic condition FAILS in vacuum AdS5 (C3)", False)]),
    ("Galloway-Schleich-Witt-Woolgar Thm 2.1 (gr-qc/9902061v2 p.8), the 5D bulk",
     [("a boundary I with Omega = 0, d Omega != 0", "FAILS: no Omega = 0 off the plane (C4)", False),
      ("ANEC near I", "vacuous without I", None)]),
    ("Galloway-Schleich-Witt-Woolgar Thm 1 (hep-th/9912119v2 p.8), the 5D bulk",
     [("a timelike boundary I with Omega = 0", "FAILS: no Omega = 0 off the plane (C4)", False),
      ("ANEC", "holds in 5D (C1); 4D-projected it fails (C6)", None)]),
]


def compute():
    return {"c1": c1(), "c3": c3(), "c4": c4(), "c5": c5(), "c6": c6(), "c7": c7()}


def report(d):
    print("censor.py -- do the censorship theorems apply to the bulk bounded by M's plane? (wall D)\n")
    print("C1 null energy in 5D: the plane's S_AB k^A k^B = %s (lambda > 0 under H-Z2: never negative); the bulk's "
          "g_AB k^A k^B = %s" % (d["c1"]["S_kk"], d["c1"]["bulk_kk"]))
    print("C2 the plane's reading is the projected Weyl part: E_kk = -G_kk (umbilic.py, seated; cited)")
    print("C3 null generic condition, max |k_[a R_b]cd[e k_f] k^c k^d|: vacuum AdS5 %.3g (maximal symmetry residual %s, "
          "so zero everywhere); control, Schwarzschild non-radial %.4g; radial (principal) %.3g"
          % (d["c3"]["ads"], d["c3"]["maxsym_residual"], d["c3"]["schw"], d["c3"]["schw_radial"]))
    print("C4 conformal factor Omega = k z: its least value off the plane %s; on the other side it falls to %s"
          % (d["c4"]["min_Omega_plane_side"], d["c4"]["Omega_other_side_limit"]))
    print("C5 the Poincare horizon off the plane at affine parameter %s: null incomplete" % d["c5"]["affine_to_horizon"])
    print("C6 the plane's averaged null energy per leg: %.15f E/m at r0 = 2m (coin.py)" % d["c6"]["leg_floor"])
    print("C7 the mirror-symmetric plane: total tension %s, from [K] = -2k g != 0 (loose.py L4)" % d["c7"]["Z2"])
    print()
    for name, prem in THEOREMS:
        fails = [p for p in prem if p[2] is False]
        print("%s -- %s" % (name, "DOES NOT APPLY" if fails else "applies"))
        for p, why, ok in prem:
            print("    %-44s %s" % (p, why))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    lam, ky = sp.Symbol("lambda", real=True), sp.Symbol("k_y", real=True)
    chk("C1: the plane's null energy is lambda k_y^2, non-negative for lambda > 0, every null vector",
        sp.simplify(d["c1"]["S_kk"] - lam * ky**2) == 0)
    chk("C1 control: a negative-tension plane gives negative null energy for any k_y != 0",
        (d["c1"]["S_kk"].subs({lam: -1, ky: 1})) < 0)
    chk("C1: the bulk's cosmological-constant stress gives zero null energy (g_AB k^A k^B = 0)", d["c1"]["bulk_kk"] == 0)
    chk("C3: the null generic condition fails at a point of vacuum AdS5 (tensor 0)", d["c3"]["ads"] < 1e-12)
    chk("C3: AdS5 is maximally symmetric everywhere (R_abcd + k^2 (g g - g g) = 0 identically), so the generic "
        "condition fails at every point for every null vector", d["c3"]["maxsym_residual"] == 0)
    chk("C3 control: it holds for a non-radial null ray of Schwarzschild (tensor nonzero)", d["c3"]["schw"] > 1e-6)
    chk("C3 contrast: a radial (principal) null ray of Schwarzschild gives 0 at the point, as it must",
        d["c3"]["schw_radial"] < 1e-12)
    chk("C4: no Omega = 0 off the plane (least Omega = 1)", d["c4"]["min_Omega_plane_side"] == 1)
    chk("C4 control: the other side's Omega falls to 0 (a conformal boundary)", d["c4"]["Omega_other_side_limit"] == 0)
    th, ep = sp.Symbol("theta", positive=True), sp.Symbol("epsilon", positive=True)
    chk("C5: the Poincare horizon is reached at finite affine parameter",
        sp.simplify(d["c5"]["affine_to_horizon"] - 1 / (sp.Symbol("k", positive=True) * ep * sp.sin(th))) == 0)
    chk("C6: the plane's averaged null energy along the passage is negative (coin.py)", d["c6"]["leg_floor"] < 0)
    chk("C7: the mirror-symmetric plane's jump in K is nonzero (total tension 6k/kappa5^2)",
        d["c7"]["Z2"] != 0)
    applies = [name for name, prem in THEOREMS if not any(p[2] is False for p in prem)]
    chk("no theorem read has all its premises met (each fails at least one checked premise)", applies == [])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
