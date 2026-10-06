#!/usr/bin/env python3
"""umbilic.py -- DOCKET 68, M-RULINGS item 122 (2): "read then compute" H-UMBILIC-GEODESIC -- one light ray, read by the
plane and by the bulk.  Deduced, computed and READ; verified once; not seated.  Write-up: UMBILIC.md.

THE CANDIDATE.  S3 has K = -a q: the plane is umbilic, so K_mn k^m k^n = 0 for every null k, and the plane's light rays
would be light rays of the bulk; along one, a bulk of vacuum energy alone gives R5_kk = 0.  (It was COIN.md point 5;
the coin metaphor is retired by item 123, and what it described stays M's: item 120 "the NEC only ever appears to
break, but never does", H-NEC-NEVER-VIOLATED.)

READ.  Youm, "Null Geodesics in Brane World Universe", hep-th/0110013v2 (Firecrawl PDF; page numbers by the verifier's
alphaXiv full text).  Sec. 2 eq. (7), p.2, for his metric ds^2 = -n^2 dt^2 + a^2 gamma dx^2 + dy^2 (FRW-type, not the
board's static one): the bulk geodesic equation's y-component.  In the board's convention (K = (1/2) d_y g, so
Gamma^y_mn = -K_mn) its term for a ray along a plane is -K_kk -- the board's translation, standard.  Sec. 1, p.1:
"gravitons are assumed to propagate freely in the bulk, whereas all the matter fields are assumed to be confined on the
brane".  Sec. 2, p.4: a ray off the plane "is observed on the hypersurface to be the timelike motion under the
additional influence of extra non-gravitational force" -- for a generic hypersurface y = y0; AT the brane, with the Z2
mirror, eqs. (21, 22), p.5: "the null bulk geodesic motion is observed on the three-brane as the timelike geodesic
motion" (the extra force appears only "if the brane universe does not possess the Z2 symmetry", abstract).

WHAT THE WORK FINDS
  U1 THE PLANE'S LIGHT RAYS ARE LIGHT RAYS OF THE BULK (STRUCTURAL).  Gamma^y_kk = -K_kk = a q_kk = 0 from the input
     K = -a q (escape.py S3) and k null; sympy confirms the code reads it.  One affine parameter for both readings
     (g_my = 0, dy/dlambda = 0: the 5D tangential equations are the plane's).  It holds for every null direction along the
     plane and at the horizons by the tensor identity (the coordinate computation is singular at r = 2m).  First written
     as a counted computation.
  U2 ALONG THAT RAY THE BULK READS 0; THE PLANE READS G_kk.  R5_kk = 0 on the plane holds by construction -- build()'s
     y^0 evolution equations set it (STRUCTURAL; first written "which closedbulk.py's constraint checks defend").  What
     is computed: the bulk's Weyl reading E_kk = R5_{kyky} (R5_kk = 0) from the series' Riemann tensor equals -G_kk
     exactly, so the plane's reading R4_kk = -E_kk = G_kk is the bulk's projected Weyl curvature (Shiromizu-Maeda-Sasaki,
     tau = 0; escape.py S3 "E = -G carries the whole reading").  Along the whole passage (m = 1, r0 = 1.8) the plane reads
     -1.914712 E/m and the bulk 0 (derived from R5_kk = 0, not set; first written as a hard-coded 0.0).  The Z2 brane's
     distributional part is proportional to S = -sigma q, so q_kk = 0 keeps it out.
  U3 LIGHT NEAR THE PLANE IS DRAWN BACK TO IT; MATTER IS PUSHED OFF IT (the verifier's finding; it follows from U2).  The
     y-deviation of a ray along the plane obeys D^2 xi^y/dlambda^2 = -R_{kyky} xi^y = +G_kk xi^y, and G_kk < 0 on the
     whole corridor: a ray displaced off the plane is pulled back -- the plane's "broken" reading is the bulk's focusing
     of light onto the plane (the board's reading).  A static massive observer (r > 2m) has d^2y/dtau^2 = +a on either
     side, away from the plane: under H-Z2 the plane is an unstable equilibrium for matter, and staying there needs
     confinement (Youm sec. 1, assumed).  First written "matter on the plane is not on a bulk geodesic" -- one-sided.
  SCOPE.  U1-U3 at y = 0 use only the exact local data (the y^0, y^1, y^2 terms): tau = 0, K = -a q, H-VACUUM-BULK,
  H-Z2 -- not H-NEAR-PLANE.  Under H-VACUUM-BULK, R5 = -4 a^2 g gives R5_kk = 0 for every null vector at every point
  off the planes, rays that leave the plane included; the averaged condition can fail only at a plane.  Only the
  plane's -1.914712 is specific to radial rays.

NAMED HYPOTHESES
  M's: H-NEC-NEVER-VIOLATED (117, 120, 123); H-SIDES-AS-HORIZON-PAIR, H-ER=EPR-MATTER-ONLY, H-RULES-NOT-INFORMATION,
    H-5D-CENSORSHIP (122, read against the coin report's numbering -- the board's reading).
  The board's: closedbulk.py's H-VACUUM-BULK, H-Z2; H-BK-CORRIDOR; H-RS1; H-PLANE-READING.

USAGE
    python3 umbilic.py | --selftest | --json      (sympy; about fifteen seconds)
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
YOUM_Z2 = "the null bulk geodesic motion is observed on the three-brane as the timelike geodesic motion"


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


def riemann_kyky(cs):
    """R5_{A y B y} k^A k^B at y = 0 for the plane's radial null k, from the series metric's own Christoffel symbols
    (R^rho_{y b y} = d_b Gamma^rho_yy - d_y Gamma^rho_by + Gamma^rho_bl Gamma^l_yy - Gamma^rho_yl Gamma^l_by)."""
    import sympy as sp
    cb = owners()["closedbulk"]
    E = cb.field_equations()
    x, u = E["x"], E["u"]
    t, th, ph = sp.symbols("t theta phi", real=True)
    X = [t, x, th, ph, u]
    g = _metric5(cs, x, th, u)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    n = 5

    def gam(r_, a_, b_):
        return sum(gi[r_, d] * (sp.diff(g[d, a_], X[b_]) + sp.diff(g[d, b_], X[a_]) - sp.diff(g[a_, b_], X[d]))
                   for d in range(n)) / 2
    A0, B0 = cs[0][0], cs[1][0]
    k = {0: 1 / A0, 1: 1 / sp.sqrt(A0 * B0)}
    tot = 0
    for rho in (0, 1):
        for b_ in (0, 1):
            R = (sp.diff(gam(rho, 4, 4), X[b_]) - sp.diff(gam(rho, b_, 4), u)
                 + sum(gam(rho, b_, l) * gam(l, 4, 4) - gam(rho, 4, l) * gam(l, b_, 4) for l in range(n)))
            for a_ in (0, 1):
                tot += g[a_, rho].subs(u, 0) * R.subs(u, 0) * k[a_] * k[b_]
    return sp.simplify(tot)


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
    accel_static = sp.simplify(-gamma_y(g, X, uvec, uvec))        # d^2 y / dtau^2 on the y > 0 side
    r5 = ricci_kk(bk["coeffs"])
    poked = cb.build(A0, B0, C0, order=2, poke=(2, sp.Symbol("delta", positive=True)))
    r5_poked = sp.factor(ricci_kk(poked["coeffs"]))
    gkk = -2 * (2 * r0 - 3 * m) * (x - 2 * m) / (x ** 2 * (2 * x - 3 * m) ** 2) / A0
    Ekk = riemann_kyky(bk["coeffs"])
    Ekk_poked = sp.factor(sp.simplify(riemann_kyky(poked["coeffs"]) + gkk))
    anec_plane = 2 * o["coin"].anec_closed(1.0, 1.8)
    src = open(o["escape"], encoding="utf-8").read()
    return {"force_null": str(force), "force_nonumbilic": str(force_non), "accel_static_y": str(accel_static),
            "R5_kk": str(r5), "R5_kk_poked": str(r5_poked), "E_kk_plus_G_kk": str(sp.simplify(Ekk + gkk)),
            "E_kk_poked_plus_G_kk": str(Ekk_poked), "deviation_coeff_minus_G_kk": str(sp.simplify(-Ekk - gkk)),
            "anec_plane_passage": anec_plane, "anec_bulk_passage": 0.0 if sp.simplify(r5) == 0 else None,
            "escape_E_in_source": ESCAPE_E in " ".join(src.split())}


def report(d):
    print("umbilic.py -- item 122 (2): one light ray, read by the plane and by the bulk")
    print("  bulk force on the plane's radial light ray, Gamma^y_kk at y = 0: %s (non-umbilic plane: %s)" % (
        d["force_null"], d["force_nonumbilic"]))
    print("  R5_kk at y = 0: %s;  E_kk + G_kk = %s;  static matter: d^2y/dtau^2 = %s" % (
        d["R5_kk"], d["E_kk_plus_G_kk"], d["accel_static_y"]))
    print("  along the whole passage (m = 1, r0 = 1.8): the plane reads %.6f E/m, the bulk %s" % (
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

    chk("U2: the bulk's Weyl reading along the ray, E_kk = R5_{kyky} from the series' Riemann tensor, is exactly -G_kk "
        "(E_kk + G_kk = %s): the plane's reading is the bulk's projected Weyl curvature" % d["E_kk_plus_G_kk"],
        d["E_kk_plus_G_kk"] == "0")
    chk("a mis-stated y^2 coefficient breaks it: E_kk + G_kk = %s" % d["E_kk_poked_plus_G_kk"],
        d["E_kk_poked_plus_G_kk"] != "0", ctl=True)
    chk("U2: along the whole passage the plane reads %.6f E/m and the bulk %s (from R5_kk = %s)" % (
        d["anec_plane_passage"], d["anec_bulk_passage"], d["R5_kk"]),
        d["anec_plane_passage"] < 0 and d["anec_bulk_passage"] == 0.0)
    structural.append("U3: a ray displaced off the plane obeys D^2 xi^y = -R_{kyky} xi^y = G_kk xi^y (difference %s) -- "
                      "U2's E_kk = -G_kk through the geodesic-deviation equation; G_kk < 0 on the corridor, so light "
                      "near the plane is drawn back to it" % d["deviation_coeff_minus_G_kk"])
    structural.append("U3: a static massive observer has d^2y/dtau^2 = %s on y > 0, away from the plane (the mirror side "
                      "alike) -- from the input K = -a q; under H-Z2 an unstable equilibrium for matter" %
                      d["accel_static_y"])
    structural.append("U1: Gamma^y_kk = -K_kk = a q_kk = %s from the input K = -a q and k null; a non-umbilic input "
                      "(b != a) gives %s -- a control on the code, not the physics (first counted)" % (
                          d["force_null"], d["force_nonumbilic"]))
    structural.append("U1: one affine parameter for both readings -- g_my = 0 and dy/dlambda = 0, so the 5D tangential "
                      "geodesic equations are the plane's")
    structural.append("U2: R5_kk = %s at y = 0 by construction (build()'s y^0 evolution equations); a mis-stated y^2 "
                      "coefficient gives %s (first counted, with a check naming the wrong defence)" % (
                          d["R5_kk"], d["R5_kk_poked"]))
    structural.append("U2: escape.py S3 '%s' is in its source: %s; the Z2 brane's distributional part is proportional "
                      "to S = -sigma q, and q_kk = 0" % (ESCAPE_E, d["escape_E_in_source"]))
    structural.append("READ: Youm hep-th/0110013v2 sec. 2 eq. (7) p.2; sec. 1 p.1 '%s'; with Z2, eqs. (21, 22) p.5 "
                      "'%s'" % (YOUM_CONFINED, YOUM_Z2))
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
