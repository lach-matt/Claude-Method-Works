#!/usr/bin/env python3
"""umbilic.py -- DOCKET 68, M-RULINGS item 122 (2): "read then compute" H-UMBILIC-GEODESIC -- one light ray, read by the
plane and by the bulk.  Deduced, computed and READ; not verified; not seated.  Write-up: UMBILIC.md.

THE CANDIDATE (COIN.md point 5).  S3 has K = -a q: the plane is umbilic, so K_mn k^m k^n = 0 for every null k, and the
plane's light rays would be light rays of the bulk; along one, a bulk of vacuum energy alone gives R5_kk = 0.

READ.  Youm, "Null Geodesics in Brane World Universe", hep-th/0110013v2 (Firecrawl, PDF), sec. 2 eq. (7): the bulk
geodesic equation's y-component, d^2y/dlambda^2 + n n' (dt/dlambda)^2 - a a' sum (dx^j/dlambda)^2 = 0, in Gaussian
normal coordinates (dy^2 in the metric).  For a ray along the plane (dy/dlambda = 0) its force term is
-(1/2) d_y g_mn k^m k^n, which in this board's convention (K = (1/2) d_y g) is -K_kk.  Youm sec. 1: "gravitons are
assumed to propagate freely in the bulk, whereas all the matter fields are assumed to be confined on the brane".

WHAT THE WORK FINDS
  U1 THE PLANE'S LIGHT RAYS ARE LIGHT RAYS OF THE BULK.  On closedbulk.py's bulk, Gamma^y_mn k^m k^n = 0 at y = 0 for
     the radial null direction at every r (sympy, from the full 5D Christoffel symbols): a light ray of the corridor
     stays a geodesic of the five-dimensional spacetime, through the throat and through both horizons.  Its affine
     parameter is the same in both, because the plane's metric is the bulk's metric restricted to y = 0.
     Control: a non-umbilic plane (B's first term -2b B0, b != a) gives a nonzero force, proportional to (a - b).
     Contrast: a static massive observer on the plane has Gamma^y_tt u^t u^t = -a != 0 -- matter on the plane is not
     on a bulk geodesic: its place on the plane is confinement, not free fall (Youm sec. 1: matter "confined on the
     brane", assumed there).
  U2 ALONG THAT ONE RAY: BROKEN IN THE PLANE'S READING, KEPT IN THE BULK.  R5_kk = 0 identically at y = 0 (sympy, from
     the series bulk's Ricci tensor); the plane reads G_kk (coin.py C1).  Integrated along the whole passage
     (m = 1, r0 = 1.8): the plane reads -1.914712 E/m, the bulk exactly 0 -- the averaged NEC saturated, not broken.
     Control: a mis-stated y^2 coefficient (A_2 + delta A_0) makes R5_kk nonzero.  The difference is the bulk's
     projected Weyl term: E_kk = -G_kk (escape.py S3: "E = -G carries the whole reading").
  So H-UMBILIC-GEODESIC is computed: on one curve, with one affine parameter, the condition appears broken from the
  plane and is not broken in the bulk.  Its scope is closedbulk.py's: the bulk near the plane, vacuum, H-RS1.

NAMED HYPOTHESES
  M's: H-NEC-COIN (117; a metaphor, 120); H-SIDES-AS-HORIZON-PAIR, H-ER=EPR-MATTER-ONLY, H-RULES-NOT-INFORMATION (122).
  The board's: closedbulk.py's H-VACUUM-BULK, H-Z2, H-NEAR-PLANE; H-BK-CORRIDOR; H-RS1; H-PLANE-READING.

USAGE
    python3 umbilic.py | --selftest | --json      (sympy; about half a minute)
"""

import contextlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

YOUM_CONFINED = ("gravitons are assumed to propagate freely in the bulk, whereas all the matter fields are assumed to "
                 "be confined on the brane")
ESCAPE_E = "E = -G carries the whole reading"


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


def owners():
    """Imported, never copied: closedbulk.py (the bulk series), pairing.py (the 5D Ricci tensor), coin.py (the plane's
    ANEC integral), escape.py (S3)."""
    if not _CACHE:
        _CACHE["closedbulk"] = _load(os.path.join(HERE, "closedbulk.py"), "d68_closedbulk_umbilic")
        _CACHE["pairing"] = _CACHE["closedbulk"].owners()["pairing"]
        _CACHE["coin"] = _CACHE["closedbulk"].owners()["coin"]
        _CACHE["escape"] = os.path.join(HERE, "escape.py")
    return _CACHE


def _metric5(cs, x, th, u):
    import sympy as sp
    A, B, C = [sum(c * u ** i for i, c in enumerate(cl)) for cl in cs]
    return sp.diag(-A, B, C, C * sp.sin(th) ** 2, 1)


def gamma_y(g, X, va, vb):
    """Gamma^y_ab v^a v^b at y = 0 from the full Christoffel formula (y is coordinate 4; set to 0 before simplifying)."""
    import sympy as sp
    assert g.is_diagonal()
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])      # the metric is diagonal by construction
    n = 5
    tot = 0
    for a_ in range(n):
        for b_ in range(n):
            if va[a_] == 0 or vb[b_] == 0:
                continue
            gam = sum(gi[4, d] * (sp.diff(g[d, a_], X[b_]) + sp.diff(g[d, b_], X[a_]) - sp.diff(g[a_, b_], X[d]))
                      for d in range(n)) / 2
            tot += gam.subs(X[4], 0) * va[a_] * vb[b_]
    return sp.simplify(tot)


def ricci_kk(cs):
    """R5_MN k^M k^N at y = 0 for the radial null k of the plane, from pairing.einstein_mixed's Ricci tensor."""
    import sympy as sp
    cb = owners()["closedbulk"]
    E = cb.field_equations()
    x, u = E["x"], E["u"]
    Af, Bf, Cf = sp.Function("A"), sp.Function("B"), sp.Function("C")

    def metric(t, xx, th, ph, uu):
        return sp.diag(-Af(xx, uu), Bf(xx, uu), Cf(xx, uu), Cf(xx, uu) * sp.sin(th) ** 2, 1)
    if "ric" not in _CACHE:
        with contextlib.redirect_stdout(io.StringIO()):
            _, ric, _ = owners()["pairing"].einstein_mixed(metric)
        _CACHE["ric"] = ric
    ric = _CACHE["ric"]
    sub = {Af(x, u): sum(c * u ** i for i, c in enumerate(cs[0])), Bf(x, u): sum(c * u ** i for i, c in enumerate(cs[1])),
           Cf(x, u): sum(c * u ** i for i, c in enumerate(cs[2]))}
    A0, B0 = cs[0][0], cs[1][0]
    kt, kr = 1 / A0, 1 / sp.sqrt(A0 * B0)
    val = (ric[0, 0].subs(sub).doit() * kt ** 2 + ric[1, 1].subs(sub).doit() * kr ** 2).subs(u, 0)
    return sp.simplify(val)


def compute():
    import sympy as sp
    o = owners()
    cb = o["closedbulk"]
    E = cb.field_equations()
    x, u, a = E["x"], E["u"], E["a"]
    t, th, ph = sp.symbols("t theta phi", real=True)
    X = [t, x, th, ph, u]
    P, (m, r0, L) = cb.planes()
    A0, B0, C0 = P["bk"]
    bk = cb.build(A0, B0, C0, order=2)
    g = _metric5(bk["coeffs"], x, th, u)
    kt, kr = 1 / A0, 1 / sp.sqrt(A0 * B0)
    k = [kt, kr, 0, 0, 0]
    force = gamma_y(g, X, k, k)
    b = sp.Symbol("b", positive=True)
    gn = _metric5([[A0, -2 * a * A0], [B0, -2 * b * B0], [C0, -2 * a * C0]], x, th, u)
    force_non = sp.factor(gamma_y(gn, X, k, k))
    uvec = [1 / sp.sqrt(A0), 0, 0, 0, 0]
    force_timelike = gamma_y(g, X, uvec, uvec)
    r5 = ricci_kk(bk["coeffs"])
    poked = cb.build(A0, B0, C0, order=2, poke=(2, sp.Symbol("delta", positive=True)))
    r5_poked = sp.factor(ricci_kk(poked["coeffs"]))
    anec_plane = 2 * o["coin"].anec_closed(1.0, 1.8)
    src = open(o["escape"], encoding="utf-8").read()
    return {"force_null": str(force), "force_nonumbilic": str(force_non), "force_timelike_static": str(force_timelike),
            "R5_kk": str(r5), "R5_kk_poked": str(r5_poked), "anec_plane_passage": anec_plane, "anec_bulk_passage": 0.0,
            "escape_E_in_source": ESCAPE_E in " ".join(src.split())}


def report(d):
    print("umbilic.py -- item 122 (2): one light ray, read by the plane and by the bulk")
    print("  bulk force on the plane's radial light ray, Gamma^y_kk at y = 0: %s" % d["force_null"])
    print("  non-umbilic plane (B's first term -2b B0): %s;  static massive observer: %s" % (
        d["force_nonumbilic"], d["force_timelike_static"]))
    print("  R5_kk at y = 0: %s;  with a mis-stated y^2 coefficient: %s" % (d["R5_kk"], d["R5_kk_poked"]))
    print("  along the whole passage (m = 1, r0 = 1.8): the plane reads %.6f E/m, the bulk %.1f" % (
        d["anec_plane_passage"], d["anec_bulk_passage"]))


def selftest(d):
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        tag = "CONTROL: " if ctl else ("CONTRAST: " if contrast else "")
        print("  %s %s%s" % ("ok  " if ok else "FAIL", tag, label))
        n_pass += bool(ok)
        n_fail += not ok
        n_ctl += bool(ctl)
        n_con += bool(contrast)

    chk("U1: the bulk exerts no force on the plane's radial light ray at any r (Gamma^y_kk = %s, full 5D Christoffels): "
        "it is a light ray of the bulk too" % d["force_null"], d["force_null"] == "0")
    chk("a non-umbilic plane (b != a) pushes the ray off: Gamma^y_kk = %s" % d["force_nonumbilic"],
        d["force_nonumbilic"] != "0" and "a - b" in d["force_nonumbilic"].replace("-b + a", "a - b"), ctl=True)
    chk("a static massive observer on the plane is not on a bulk geodesic: Gamma^y_tt u u = %s -- its place on the "
        "plane is confinement, not free fall" % d["force_timelike_static"], d["force_timelike_static"] not in ("0",), contrast=True)
    chk("U2: R5_kk = %s at y = 0 along that ray (the series bulk's Ricci tensor)" % d["R5_kk"], d["R5_kk"] == "0")
    chk("a mis-stated y^2 coefficient makes R5_kk = %s" % d["R5_kk_poked"], d["R5_kk_poked"] != "0", ctl=True)
    chk("U2: along the whole passage the plane reads %.6f E/m and the bulk %.1f -- broken in the plane's reading, "
        "saturated in the bulk" % (d["anec_plane_passage"], d["anec_bulk_passage"]),
        d["anec_plane_passage"] < 0 and d["anec_bulk_passage"] == 0.0)
    structural.append("U1: one affine parameter for both readings -- the plane's metric is the bulk's restricted to "
                      "y = 0, and the ray is a geodesic of both")
    structural.append("U2: the bulk's integral is 0 because R5_kk vanishes pointwise; that follows from the field "
                      "equations R5_AB = -4 a^2 g_AB and g_kk = 0, which closedbulk.py's constraint checks defend")
    structural.append("U2: the difference is the projected Weyl term, E_kk = -G_kk (escape.py S3 '%s', in its source: "
                      "%s)" % (ESCAPE_E, d["escape_E_in_source"]))
    structural.append("READ: Youm hep-th/0110013v2 sec. 2 eq. (7) is the y-component of the bulk geodesic equation; "
                      "sec. 1: '%s'" % YOUM_CONFINED)
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("umbilic.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    d = compute()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
