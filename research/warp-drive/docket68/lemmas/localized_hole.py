#!/usr/bin/env python3
"""localized_hole.py -- item 251: the corridor as the regular localized five-dimensional hole, our plane through its
equator and through its Einstein-Rosen bridge, the README crossing as information.  M: "Localized hole, README only"
(clause (O)'s "extremal" dropped).  The first step of item 251's order: the construction computed exactly.  Worked in
the conversation (computed with sympy, exact where marked; deduced where marked; not verified by a separate session;
not seated); 2026-10-11.

The flat limit is the record's regime (B4D-STAGE1 D1: the corridor far smaller than ell): near the corridor the bulk is
five-dimensional vacuum, the plane's tension a correction of order r_h/ell.

  H0 (read) M's item-251 words, verbatim in the rulings file.
  H1 (computed, exact) The bulk: five-dimensional Schwarzschild-Tangherlini, -f dt^2 + dr^2/f + r^2 (dchi^2 +
     sin^2 chi (dtheta^2 + sin^2 theta dphi^2)), f = 1 - r_h^2/r^2.  Its Ricci tensor vanishes identically -- a vacuum
     bulk, clause (B) as seated.  Its Kretschmann scalar is 72 r_h^4/r^8.
  H2 (computed, exact) Our plane: the equator chi = pi/2.  Its extrinsic curvature vanishes identically -- the
     surface is totally geodesic (the reflection chi -> pi - chi is an isometry and the equator its fixed set) -- so
     with the bulk mirrored across it the plane carries no stress at flat order: the matter's null energy is zero, in
     the bulk (T_AB = 0) and on the plane (S_ab = 0).  [Verifier, item 254: the plane's own four-dimensional reading is
     not zero -- its Einstein tensor is (r_h^2/r^4) diag(1, 1, -1, -1), radial null energy 0, tangential -2 r_h^2/r^4:
     a negative read on tangential rays that is the bulk's traceless Weyl term, the appearance 183 names, not matter.
     Computed here since.]
  H3 (computed, exact) What the plane reads: -f dt^2 + dr^2/f + r^2 dOmega^2 with the same f.  Its Ricci scalar is 0
     -- the plane's vacuum condition (its bulk Weyl term traceless), the class eq. (17) belongs to.  It is not eq. (17):
     lim r (f - 1) = 0 and lim r^2 (f - 1) = -r_h^2, a 1/r^2 pull, where eq. (17) has 1/r (B4D-STAGE1 D2, recomputed).
     [Verifier, item 254: the flat-limit metric holds for r << ell, so the 1/r^2 pull is the plane's reading for
     r_h << r << ell; at r >> ell the plane recovers four-dimensional gravity (Garriga-Tanaka, abstract READ by the
     verifier) and the 1/r tail of the hole's mass returns.  D2 carried "at r << ell"; item 251's "loses the 1/r tail"
     dropped it -- restored here.]
  H4 (computed, exact) Through the bridge.  Surface gravity kappa = f'(r_h)/2 = 1/r_h; tortoise r* = r + (r_h/2)
     ln|(r - r_h)/(r + r_h)|; with U = -e^(-kappa (t - r*)), V = e^(kappa (t + r*)) the (t, r) part is -F dU dV with
     F = r_h^2 (r + r_h)^2 e^(-2r/r_h) / r^2 -- smooth and positive at r = r_h, so the chart crosses the horizon.  The
     equator is untouched by the change of chart, so our plane continues through the bifurcation sphere (U = V = 0)
     into the second exterior: our plane on position 1's side, the same surface on position 2's.  On the plane's
     t = 0 slice, dr^2/f + r^2 dOmega^2 -- with r^2 = r_h^2 + x^2 exactly dx^2 + (r_h^2 + x^2) dOmega^2, x real -- r
     has a minimum r_h where the two sides join (checked).  [Verifier, item 254: that minimal sphere is the bifurcation
     sphere of a non-degenerate horizon, a minimum only on the time-symmetric slice; on later slices the minimum radius
     falls below r_h and to 0 -- the bridge pinches off -- and the second exterior exists only in the eternal solution,
     not in a hole formed by collapse.  So it is not a static throat: B4D-STAGE1 D2's conclusion ("no throat", against
     eq. (17)'s static throat) stands; its reason read the static chart alone.]  The bridge is not traversable: no
     causal curve runs from one exterior to the other -- which item 251 accepts, since only the README crosses, as
     information.  The chart is checked by pulling -F dU dV back to -f dt^2 + dr^2/f.
  H5 (computed) Regularity: the Kretschmann scalar is finite at every r > 0 -- 72/r_h^4 at the horizon and across the
     bridge -- and diverges only at r = 0, which lies in the hole's future and past interiors, never in either exterior
     nor on the bridge's slice (where r >= r_h).  Both exteriors and the bridge are regular; the interior is O1b/O1c's
     rework, the next step.
  H6 (computed) The example README (N = 2,742,570,311,524,972): E = 2.4059e16 J, r0 = 2GE/c^4 = 3.976e-28 m.  The 5D
     horizon r_h^2 = 8 G5 M / 3 pi c^2 with G5 = G ell (item 234's normalisation, 8 pi G = kappa5^2 / ell): at ell =
     13.964 um, r_h = 4.854e-17 m = 1.22e11 r0, r_h/ell = 3.5e-12, Hawking temperature hbar c / 2 pi k r_h = 7.5e12 K.
     (The Z2 factor between the 5D mass and the plane's reading is not fixed here; it moves r_h by sqrt 2 at most.)
  H7 (deduced; the warp's kink) The plane's tension sigma = 6/(kappa5^2 ell) is the warp's kink.  Near the corridor it
     enters at order r_h/ell (3.5e-12 for the example): at flat order the plane is the exact equator, and the kink rides
     on that surface through the bridge -- the kink follows our plane into the corridor and out the other side.  The
     bulk at warp order is the small brane black hole the record surveyed (F1-AUDIT: Tangherlini, KTN, FW grids; "at
     x < 0.004 the Tangherlini limit"); its first-order deformation is not computed here.

What this does not show.
  - Clause (H)'s area law, O1b/O1c's interior and the hold against the temperature: item 251's next steps.
  - The warp-order bulk (r_h/ell corrections) and the Z2 normalisation of the mass.

Stdlib + sympy.  python3 localized_hole.py [--selftest | --mutants]
"""
import importlib.util
import contextlib
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M251 = "Localized hole, README only"
N_EX = 2742570311524972

t, r, chi, th, ph, rh = sp.symbols("t r chi theta phi r_h", positive=True)


def f_of(r_):
    return 1 - rh ** 2 / r_ ** 2 if not MUT.get("four_d_f") else 1 - rh / r_


def curvature(g, xs):
    """Christoffel, Riemann (all indices down), Ricci and Kretschmann of a diagonal metric"""
    n = len(xs)
    gi = [1 / g[i] for i in range(n)]
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(gi[a] * (sp.diff(g[a] if a == b else 0, xs[c]) * 0 + (
                    (sp.diff(g[a], xs[c]) if a == b else 0) + (sp.diff(g[a], xs[b]) if a == c else 0)
                    - (sp.diff(g[b], xs[a]) if b == c else 0)) / 2))
    def R_up(a, b, c, d):          # R^a_{bcd}
        e = sp.diff(G[a][b][d], xs[c]) - sp.diff(G[a][b][c], xs[d])
        e += sum(G[a][c][k] * G[k][b][d] - G[a][d][k] * G[k][b][c] for k in range(n))
        return e
    Ric = [[sp.simplify(sum(R_up(a, b, a, d) for a in range(n))) for d in range(n)] for b in range(n)]
    K = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Rabcd = R_up(a, b, c, d)
                    if Rabcd != 0:
                        K += (g[a] * Rabcd) ** 2 * gi[a] * gi[b] * gi[c] * gi[d]
    return G, Ric, sp.simplify(K)


def bulk():
    f = f_of(r)
    g = [-f, 1 / f, r ** 2, r ** 2 * sp.sin(chi) ** 2, r ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2]
    G, Ric, K = curvature(g, [t, r, chi, th, ph])
    ricci_zero = all(sp.simplify(Ric[i][j]) == 0 for i in range(5) for j in range(5))
    return dict(G=G, ricci_zero=ricci_zero, K=sp.simplify(K))


def plane_extrinsic(G, chi0=sp.pi / 2):
    """K_ab = -n_mu Gamma^mu_ab on chi = chi0, unit normal n_chi = r, tangential a, b in (t, r, theta, phi)"""
    if MUT.get("off_equator"):
        chi0 = sp.pi / 3
    tang = [0, 1, 3, 4]
    Kab = [[sp.simplify((-r * G[2][a][b]).subs(chi, chi0)) for b in tang] for a in tang]
    return all(e == 0 for row in Kab for e in row), Kab


def plane_metric():
    f = f_of(r)
    g = [-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2]
    xs = [t, r, th, ph]
    G, Ric, K = curvature(g, xs)
    Rs = sp.simplify(sum(Ric[i][i] / g[i] for i in range(4)))
    # the mixed Einstein tensor G^a_a (diagonal) and the null energies of the plane's own 4D reading (orthonormal)
    Gmix = [sp.simplify(Ric[i][i] / g[i] - Rs / 2) for i in range(4)]
    rho, pr, pt = -Gmix[0], Gmix[1], Gmix[2]
    null_radial, null_tangential = sp.simplify(rho + pr), sp.simplify(rho + pt)
    tail1 = sp.limit(r * (f - 1), r, sp.oo)
    tail2 = sp.limit(r ** 2 * (f - 1), r, sp.oo)
    return dict(R=Rs, tail1=tail1, tail2=tail2, Gmix=Gmix, null_radial=null_radial, null_tangential=null_tangential)


def bridge():
    f = f_of(r)
    kappa = sp.simplify(sp.diff(f, r).subs(r, rh) / 2)
    if MUT.get("wrong_kappa"):
        kappa = kappa / 2
    rstar = r + rh / 2 * sp.log((r - rh) / (r + rh))
    F = sp.simplify(f * sp.exp(-2 * kappa * rstar) / kappa ** 2)
    Fclosed = rh ** 2 * (r + rh) ** 2 * sp.exp(-2 * r / rh) / r ** 2
    same = sp.simplify(sp.expand_log(sp.simplify(F / Fclosed), force=True)) == 1
    at_h = sp.simplify(sp.limit(F, r, rh))
    # pullback: dU = -kappa U (dt - dr*), dV = kappa V (dt + dr*), so -F dU dV = -F kappa^2 (-UV) (dt^2 - dr*^2) with
    # -UV = e^(2 kappa r*); it is -f dt^2 + dr^2/f exactly when F kappa^2 e^(2 kappa r*) = f
    pullback = sp.simplify(F * kappa ** 2 * sp.exp(2 * kappa * rstar) - f) == 0
    # the t = 0 slice: r^2 = r_h^2 + x^2 turns dr^2/f into dx^2
    x = sp.symbols("x", real=True)
    rx = sp.sqrt(rh ** 2 + x ** 2)
    slice_ok = sp.simplify(sp.diff(rx, x) ** 2 / f.subs(r, rx) - 1) == 0
    return dict(kappa=kappa, F=F, closed=same, F_at_h=at_h, finite_positive=bool(at_h.is_positive), pullback=pullback,
                throat=slice_ok)


def example():
    spec = importlib.util.spec_from_file_location("lh_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    E = PG.corridor(PG.G)["E1"] * math.sqrt(N_EX)
    G, c, hbar, kB = PG.G, PG.C, PG.HBAR, 1.380649e-23
    r0 = 2 * G * E / c ** 4
    rows = {}
    for ell in (PG.ELL_MAX, 1e-6, 1e-9):
        r_h = math.sqrt(8 * G * ell * (E / c ** 2) / (3 * math.pi * c ** 2))
        rows[ell] = dict(rh=r_h, over_r0=r_h / r0, over_ell=r_h / ell, T=hbar * c / (2 * math.pi * kB * r_h))
    return dict(E=E, r0=r0, rows=rows, ell_max=PG.ELL_MAX)


def compute():
    b = bulk()
    tg, Kab = plane_extrinsic(b["G"])
    return dict(bulk=b, totally_geodesic=tg, Kab=Kab, plane=plane_metric(), bridge=bridge(), ex=example())


def report(o):
    print("localized_hole.py -- the corridor as the regular localized 5D hole (item 251)\n")
    b = o["bulk"]
    print("H1 5D Schwarzschild-Tangherlini: Ricci = 0: %s; Kretschmann = %s" % (b["ricci_zero"], b["K"]))
    print("H2 the plane chi = pi/2: extrinsic curvature identically zero: %s; the plane's 4D G^a_b %s; null energy "
          "radial %s, tangential %s" % (o["totally_geodesic"], o["plane"]["Gmix"], o["plane"]["null_radial"],
                                         o["plane"]["null_tangential"]))
    p = o["plane"]
    print("H3 the plane's metric: Ricci scalar %s; lim r(f-1) = %s; lim r^2(f-1) = %s" % (p["R"], p["tail1"], p["tail2"]))
    br = o["bridge"]
    print("H4 surface gravity %s; Kruskal F = %s (closed form agrees: %s); F at r_h = %s, finite and positive: %s; pulls "
          "back to the static metric: %s; t = 0 slice a throat: %s" % (br["kappa"], br["F"], br["closed"], br["F_at_h"],
                                                                      br["finite_positive"], br["pullback"], br["throat"]))
    K = b["K"]
    print("H5 Kretschmann at r_h = %s; at r -> 0: %s" % (sp.simplify(K.subs(r, rh)), sp.limit(K, r, 0)))
    ex = o["ex"]
    print("H6 example README: E = %.4e J, r0 = %.4e m" % (ex["E"], ex["r0"]))
    for ell, x in ex["rows"].items():
        print("   ell %.3e m: r_h = %.4e m = %.3e r0; r_h/ell = %.2e; T = %.3e K" % (ell, x["rh"], x["over_r0"], x["over_ell"],
                                                                                    x["T"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("H0 M's item-251 words verbatim in the rulings file", M251 in rul)
    b = o["bulk"]
    add("H1 the 5D Schwarzschild-Tangherlini bulk is Ricci-flat (vacuum, clause (B)); Kretschmann 72 r_h^4/r^8",
        b["ricci_zero"] and sp.simplify(b["K"] - 72 * rh ** 4 / r ** 8) == 0)
    pl = o["plane"]
    ok = o["totally_geodesic"] and [sp.simplify(e) for e in pl["Gmix"]] == [sp.simplify(e) for e in (
        rh ** 2 / r ** 4, rh ** 2 / r ** 4, -rh ** 2 / r ** 4, -rh ** 2 / r ** 4)]
    ok &= pl["null_radial"] == 0 and sp.simplify(pl["null_tangential"] + 2 * rh ** 2 / r ** 4) == 0
    add("H2 our plane, the equator, is totally geodesic: no stress at flat order, matter null energy zero; the plane's own "
        "4D reading G^a_b = (r_h^2/r^4) diag(1, 1, -1, -1) -- radial null 0, tangential -2 r_h^2/r^4, the bulk's Weyl "
        "term (verifier, 254)", ok)
    p = o["plane"]
    add("H3 the plane reads -f dt^2 + dr^2/f + r^2 dOmega^2 with Ricci scalar 0 (eq. (17)'s class), a 1/r^2 pull: "
        "lim r(f-1) = 0, lim r^2(f-1) = -r_h^2", p["R"] == 0 and p["tail1"] == 0 and sp.simplify(p["tail2"] + rh ** 2) == 0)
    br = o["bridge"]
    add("H4 surface gravity 1/r_h; Kruskal F = r_h^2 (r + r_h)^2 e^(-2r/r_h) / r^2, finite and positive at r_h, pulling "
        "back to -f dt^2 + dr^2/f; the t = 0 slice dx^2 + (r_h^2 + x^2) dOmega^2 with its minimum at r_h; the plane "
        "continues through the bifurcation sphere", sp.simplify(br["kappa"] - 1 / rh) == 0
        and br["closed"] and br["finite_positive"] and br["pullback"] and br["throat"])
    K = b["K"]
    ok = sp.simplify(K.subs(r, rh) - 72 / rh ** 4) == 0 and sp.limit(K, r, 0) == sp.oo
    add("H5 regular at every r > 0 (Kretschmann 72/r_h^4 at the horizon and the bridge); divergent only at r = 0, inside the "
        "hole", ok)
    ex = o["ex"]
    x = ex["rows"][ex["ell_max"]]
    ok = "%.4e" % ex["E"] == "2.4059e+16" and "%.3e" % ex["r0"] == "3.976e-28"
    ok &= "%.3e" % x["rh"] == "4.854e-17" and 1.2e11 < x["over_r0"] < 1.23e11 and "%.1e" % x["over_ell"] == "3.5e-12"
    ok &= 7.4e12 < x["T"] < 7.6e12
    add("H6 example README: r_h = 4.854e-17 m = 1.22e11 r0 at ell = 13.964 um; r_h/ell 3.5e-12; T 7.5e12 K", ok)
    return res


MUTANTS = {"four_d_f": "f = 1 - r_h/r (the 4D form) in five dimensions",
           "off_equator": "the plane put at chi = pi/3",
           "wrong_kappa": "half the surface gravity in the Kruskal chart"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-11s %-48s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
