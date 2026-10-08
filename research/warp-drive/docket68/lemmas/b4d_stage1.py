#!/usr/bin/env python3
"""b4d_stage1.py -- Warp Theorem lemma B4d, stage 1: what bulk can stand through the write.  Computed, READ and
deduced; verified once (findings applied, B4D-STAGE1.md History); not seated.  First headed "... not verified; not
seated".

M's words (verbatim in the rulings file): "Continue B4d as well please" (2026-10-08); item 157 "we already have at
least half the model, our current universe"; items 117 (H-NEC-COIN) and 120 ("the NEC only ever appears to break, but
never does"); item 127 (1) "yes" (the planes coincide); item 138 (the bulk is multi-universal); item 139 (position 2's
plane, negative tension); item 141 (the planes are static); item 159 "test both options".

READ
  Ishibashi & Kodama, hep-th/0305185, p.16 (Summary): higher-dimensional Schwarzschild holes "are stable with respect
    to all tensorial types of linear perturbations"; p.6, kappa = (n - 1)/(2 r_h); p.18, initial data vanishing near the
    bifurcation sphere.
  Figueras & Wiseman, 1105.2558, p.1 (abstract): static RS II holes for R4/ell in [0.07, 20], whose numerics "indicate
    the RSII black holes are dynamically stable for axisymmetric perturbations"; p.3: "small (compared to ell)
    braneworld black holes behave like 5d asymptotically flat Schwarzschild black holes"; p.4: "Small solutions are
    close to 5d Schwarzschild and should be stable".
  Gregory, hep-th/0004101, p.7: "very small mass black holes are roughly hyperspherical ... look like a five-dimensional
    black hole".  Gregory & Laflamme, hep-th/9301052, p.1 (abstract): perturbations "can be stabililized [sic] if the
    extra dimensions are compactified to a scale smaller than the minimum wavelength for which instability occurs".

  READING BY READING (item 159; o3_readings.py).  On (ii) and on (i') -- the live readings -- the corridor stands only
  after the README has arrived, so the question for the bulk is the opening: >= 2.0e5 clocks, and whether it can end
  in eq. (17).  Only on (i) as first tested (H-WRITE-IN-STATIC-HOLD, withdrawn: inconsistent with 115 (c)) must eq.
  (17)'s static bulk itself stand through the write; D3 is that reading's test.

  D1 THE REGIME (computed).  By O3-WRITE W3 the README starts spread over a ball of radius (2 + T) m (m = G E/c^4, the
     corridor's mass length; a clock ~6.6e-37 s at the example README), and light moves at most at 1: the region the
     write disturbs reaches ~T m.  B4c's far model (H-FAR-MODEL) needs ell > 2 R_reach = 4.0e5 m: ell/r0 > 1e5, the flat
     limit, where gravity at the corridor's scale is five-dimensional.
  D2 WHAT STANDS WITH ONE PLANE -- AN ENUMERATION, NOT A CLASSIFICATION (computed and READ).
     - the black string (the Vaidya opening's bulk, by construction): unstable, o3_readings.py -- under its named
       H-QUASI-STATIC-STRING, H-MASS-RISES, H-README-ALONE or H-SEED, ending in Lehner-Pretorius's extrapolated naked
       singularity;
     - eq. (17)'s static bulk: its singular surface by ~18 clocks (b4_static.py);
     - the localized hole (Tangherlini, by choice): in this regime the Z2-cut 5D Schwarzschild hole (Gregory p.7; FW's
       small limit, whose own range [0.07, 20] lies above ours, r_h/ell ~ 1e-3), linearly stable against all tensorial
       types (Ishibashi-Kodama).  Its plane slice (computed): lim r (f - 1) = 0, no 1/r tail at r << ell; surface
       gravity 1/r_h, not 0 -- O2 fails.  STRUCTURAL: its areal radius is r, so no throat.  And (deduced, standard RS
       with G4 = G5/ell, not READ) a hole carrying the README's energy has r_h^2 = (8/(3 pi)) m ell -- ~580 m at
       ell = 4e5 m, against r0 = 2 m: G3 and H1 fail too.  A Z2-symmetric extremal vacuum hole is not available (no
       regular extremal limit with one spin; a second spin breaks Z2 -- standard, not READ); extremal charged RS holes
       (Kaus-Reall, cited by FW) need matter on the plane, which clause (B) forbids.
  D3 READING (i) ONLY: A PLANE CLOSING EQ. (17)'S STATIC BULK (computed and STRUCTURAL).  One of 138's planes at y_w,
     Z2, below the singular surface.  Israel: its S_mu_nu IS its stress-energy -- localized real matter, unlike eq.
     (17)'s apparent deficit on a plane carrying none (117/120's appearances) -- and in units 2/kappa^2
     rho + p_r = -A_y/(2A) + B_y/(2B).
     STRUCTURAL at small y_w: the tensionless Z2 plane has dh/dy = 0, so d^2h/dy^2 = 2 R4 and
        rho + p_r = y_w R4_kk(radial) + O(y_w^3),   R4_kk(radial) = -2 (r - 2)/(r^2 (2r - 3)^2) < 0 for every r > 2
     (eq. (17)'s own radial null combination, opening.py O3) -- the closing plane must carry as matter the deficit the
     theorem's (Z) clause reads as the bulk's pull.  Numerically (exact series, Padé, two orders): negative at every r
     from 2.1m to 32m and every y_w to 2.3m; positive near the throat (r <= 2.05m) for y_w >~ 2 -- the control that the
     sign is not forced; one negative point per plane suffices.  A tension adds +sigma to rho and -sigma to p: no help,
     139's negative plane included.  And any closing plane within ~2.5 m leaves no room for B4c's far surface T.
  D4 A SLAB FOR THE STRING (deduced).  A closing plane on the flat-limit string carries nothing, and stops the final
     string for y_w < pi r+/mu_c = 3.59 r+ (deduced from Gregory's eq. (11), the Z2 form of GL's compactification).  But
     o3_readings.py R4 (b) stays closed under H-QUASI-STATIC-STRING: from m = 0 every allowed mode crosses the band
     (2.2e4 e-folds).  It reopens only if the early opening is not a string -- the board's H-SLAB-PHASES (a localized
     hole until it spans the slab), which denies H-QUASI-STATIC-STRING early; carried as open, not shown.  A slab is
     also excluded by H-FAR-MODEL as written; a far model for a slab is not built.  Its end is a uniform string,
     Schwarzschild on the plane -- not eq. (17).
  VERDICT  (ii), (i'): on the board's models no regular bulk through the opening ends in eq. (17); the candidates are an
     enumeration built from the board's own choices.  (i): a constant-y Z2 plane closing the static bulk must break the
     null energy condition with real matter -- structurally at small y_w, numerically to the singular surface -- and is
     excluded by H-FAR-MODEL anyway.  Not decided: H-TWO-SIDED (bulk on both sides of a plane); a curved closing wall
     y_w(r) (its bending terms may dominate the small R4_kk at large r); finite ell (B6', nature's; excluded by
     H-FAR-MODEL unless B4c's reading changes); o3_readings.py's open escapes (a) an extremal opening, (d) the opening's
     bulk not the string, (e) a late shell, (f) the short write with small seeds, and (i'); H-SLAB-PHASES.

Imports o3_write.py, o3_readings.py, b4_static.py by path.  numpy, scipy, sympy, mpmath, python-flint.  Padé at order
40 ([9/10], [10/10]) -- below the banked order 60, adequate since y_w <= 2.3 lies under every banked verified top (>= 2.36).
python3 b4d_stage1.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
WALL_R = ["201/100", "21/10", "43/20", "9/4", "5/2", "3", "4", "6", "12", "32"]
WALL_Y = [0.02, 0.25, 0.5, 1.0, 1.5, 2.0, 2.3]
ORDER = 40


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


def tangherlini_slice():
    """The Z2-cut 5D Schwarzschild hole's slice through the plane (the equator of S^3): its 1/r coefficient
    lim r (f - 1) (control: 4D Schwarzschild gives -2m), and its surface gravity."""
    r, rh, m = sp.symbols("r r_h m", positive=True)
    f = 1 - rh**2 / r**2
    kappa = sp.simplify(sp.diff(f, r).subs(r, rh) / 2)
    one_over_r = sp.limit(r * (f - 1), r, sp.oo)
    ctl = sp.limit(r * ((1 - 2 * m / r) - 1), r, sp.oo)
    return {"f": f, "kappa": kappa, "one_over_r": one_over_r, "ctl": ctl}


def hole_radius(ell_over_m):
    """Deduced, standard RS (not READ): a 5D hole of energy E, G5 = G4 ell: r_h^2 = 8 G5 E/(3 pi) = (8/(3 pi)) m ell."""
    return math.sqrt(8 / (3 * math.pi) * ell_over_m)


def r4kk(r):
    """Eq. (17)'s radial null combination at r0 = 2m, m = 1 (opening.py O3): -2 (r - 2)/(r^2 (2r - 3)^2)."""
    return -2 * (r - 2) / (r**2 * (2 * r - 3) ** 2)


def wall_stress(b4, rc, ys, N=ORDER):
    """Israel stress of a Z2 plane at y = y_w closing eq. (17)'s static bulk (bulk below; normal -d_y), in units
    2/kappa^2: S^mu_nu = -(K^mu_nu - K delta), K^mu_nu = -(1/2) h^-1 dh/dy.  Two Padé orders."""
    S = b4.series(rc, N)
    n = N // 2
    out = []
    for o in [(n // 2 - 1, n // 2), (n // 2, n // 2)]:
        F = {X: b4.pade(S[X][0][0::2], *o) for X in "ABC"}

        def ev(X, y):
            p, q = F[X]
            s = y * y
            return (mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(p)], s)
                    / mp.polyval([mp.mpf(v.numerator) / v.denominator for v in reversed(q)], s))
        row = []
        for yw in ys:
            y = mp.mpf(yw)
            h = {X: ev(X, y) for X in "ABC"}
            d = {X: mp.diff(lambda t, X=X: ev(X, t), y) for X in "ABC"}
            Kt, Kr, Kq = (-d[X] / (2 * h[X]) for X in "ABC")
            K = Kt + Kr + 2 * Kq
            rho, pr, pq = Kt - K, -(Kr - K), -(Kq - K)
            row.append({"y": yw, "rho": float(rho), "pr": float(pr), "pq": float(pq), "nec_r": float(rho + pr),
                        "nec_q": float(rho + pq)})
        out.append(row)
    return out


def rs_control():
    """RS1's second brane: h = e^(-2y/ell) eta at y = y_w, bulk below: negative tension, rho + p = 0."""
    y, ell = sp.symbols("y ell", positive=True)
    h = sp.exp(-2 * y / ell)
    K1 = -sp.diff(h, y) / (2 * h)
    K = 4 * K1
    rho, p = sp.simplify(K1 - K), sp.simplify(-(K1 - K))
    return rho, p


def string_control():
    """The flat-limit black string: h independent of y, so a closing plane carries nothing."""
    r, y, m = sp.symbols("r y m", positive=True)
    hs = [1 - 2 * m / r, 1 / (1 - 2 * m / r), r**2]
    return [sp.simplify(sp.diff(x, y)) for x in hs]


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "b4d_o3write")
    orr = _load(os.path.join(HERE, "o3_readings.py"), "b4d_readings")
    b4 = _load(os.path.join(HERE, "b4_static.py"), "b4d_b4static")
    T = ow._num(ow.t_min(3))
    m1, m2 = 0.86, 0.865
    o1, o2 = orr.growth(m1, lo=1e-4, hi=0.01, n=30), orr.growth(m2, lo=1e-4, hi=0.01, n=30)
    mu_c = m2 + o2 * (m2 - m1) / (o1 - o2)
    walls = {rc: wall_stress(b4, rc, WALL_Y) for rc in WALL_R}
    pade_gap = max(abs(a["nec_r"] - b["nec_r"]) for w in walls.values() for a, b in zip(*w))
    nec_r = {rc: [c["nec_r"] for c in w[1]] for rc, w in walls.items()}
    away = [rc for rc in WALL_R if float(sp.Rational(rc)) >= 2.1]
    away_fails = all(v < 0 for rc in away for v in nec_r[rc])
    near_positive = nec_r["201/100"][-1] > 0
    gap_ok = all(abs(a["nec_r"] - b["nec_r"]) < 0.1 * abs(b["nec_r"])
                 for rc in away for a, b in zip(*walls[rc]))
    every_plane_bad = all(any(nec_r[rc][k] < 0 for rc in WALL_R) for k in range(len(WALL_Y)))
    slope = {rc: (nec_r[rc][0] / WALL_Y[0], r4kk(float(sp.Rational(rc)))) for rc in WALL_R}
    rho_c, p_c = rs_control()
    ell = 2 * (T + 2)
    return {"T": T, "ell_min": ell, "tang": tangherlini_slice(), "rh": hole_radius(ell), "mu_c": mu_c,
            "slab": math.pi / mu_c, "walls": walls, "nec_r": nec_r, "away_fails": away_fails,
            "near_positive": near_positive, "gap_ok": gap_ok, "every_plane_bad": every_plane_bad, "pade_gap": pade_gap,
            "min_abs": min(abs(v) for rc in away for v in nec_r[rc]), "slope": slope,
            "rs": (rho_c, p_c), "string": string_control()}


def report(d):
    print("b4d_stage1.py -- B4d stage 1: what bulk can stand through the write\n")
    print("D1 the write's reach ~(2 + T) m: H-FAR-MODEL needs ell > %.3g m (corridor mass lengths) -- the flat limit"
          % d["ell_min"])
    t = d["tang"]
    print("D2 localized 5D hole: g_tt = -(%s); lim r (f - 1) = %s (4D control %s); surface gravity %s; r_h at that ell "
          "%.0f m against r0 = 2 m" % (t["f"], t["one_over_r"], t["ctl"], t["kappa"], d["rh"]))
    print("D3 (reading (i) only) a closing plane: rho + p_r (units 2/kappa^2) at y_w = %s" % WALL_Y)
    for rc, v in d["nec_r"].items():
        print("     r = %-7s %s" % (rc, "  ".join("%+.5f" % x for x in v)))
    print("     small y_w slope vs R4_kk: %s" % ", ".join("%s: %.3g/%.3g" % (rc, a, b) for rc, (a, b) in d["slope"].items()))
    print("     r >= 2.1 all negative: %s; positive near the throat: %s; every plane has a negative point: %s; Padé gap %.1e"
          % (d["away_fails"], d["near_positive"], d["every_plane_bad"], d["pade_gap"]))
    print("D4 the slab stops the final string below pi/mu_c = %.3f r+" % d["slab"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    rh, m = sp.symbols("r_h m", positive=True)
    t = d["tang"]
    chk("D1: the write's reach puts H-FAR-MODEL at ell > ~4.0e5 m -- the flat limit", 3.9e5 < d["ell_min"] < 4.1e5)
    chk("D2: the localized hole's slice has no 1/r tail (4D Schwarzschild's -2m the control), surface gravity 1/r_h "
        "(not extremal), and at that ell r_h ~ 580 m >> r0 = 2 m", t["one_over_r"] == 0
        and sp.simplify(t["ctl"] + 2 * m) == 0 and sp.simplify(t["kappa"] - 1 / rh) == 0 and 550 < d["rh"] < 610)
    chk("D3 STRUCTURAL check: at small y_w, rho + p_r = y_w R4_kk(radial) at every r computed (to 1%)",
        all(abs(a / b - 1) < 0.01 for a, b in d["slope"].values()))
    chk("D3: negative at every r from 2.1m to 32m and every y_w to 2.3m; every constant-y plane has a negative point; "
        "at each such point the two Padé orders differ by under a tenth of its value", d["away_fails"]
        and d["every_plane_bad"] and d["gap_ok"])
    chk("D3 control: the sign is not forced -- near the throat (r = 2.005m) rho + p_r > 0 at y_w = 2.3", d["near_positive"])
    chk("D3 controls: RS1's second brane is negative tension with rho + p = 0; the flat-limit string's plane carries "
        "nothing", sp.simplify(d["rs"][0] + d["rs"][1]) == 0 and sp.simplify(d["rs"][0]) != 0
        and float(d["rs"][0].subs(sp.Symbol("ell", positive=True), 1)) < 0 and all(x == 0 for x in d["string"]))
    chk("D4: a slab stops the final string below pi/mu_c = 3.59 r+", 3.55 < d["slab"] < 3.63)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
