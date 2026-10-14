#!/usr/bin/env python3
"""throatbulk.py -- C, first part: the corridor read on one static plane, and what that says of k.

M (item 141): the planes are static and a stable throat forms; (item 140) "k is dependent on our work"; (item 127) r0,
E and k are coefficients.  static.py: static and face to face, the pair is one Randall-Sundrum II plane at long range
(zero modes).  This reads the corridor -- Bronnikov-Kim eq. (17) at r0 = 2m, H-BK-CORRIDOR (the board's) -- on that one
static plane (H-RS2-ONE-PLANE, the board's; it stands against M's item 138, which says the bulk is not one plane).

First written with a numeric window, k r_min(N) in [1, 1.633], and a throat that "widens off the plane".  The verifier
showed the window came from a far-field form used at the throat, and the widening ignored the warp factor; both are
withdrawn (THROATBULK.md History).

READ: Maartens-Koyama, Living Rev. Rel. 13 (2010) 5, arXiv:1004.3962v2 ("MK"):
  eq. (143) p.26  a vacuum on the plane obeys R_mu nu = -E_mu nu, R = 0 = E^mu_mu
  eqs. (150)-(152) p.27  E for -F dt^2 + dr^2/H + r^2 dOmega^2.  (151) is misprinted: it fails MK's own eq. (160) at
                  F = H; with a factor H on F'/F it agrees with (160) and with tracelessness
  eq. (148) p.27  the bulk off a vacuum plane, in g~ = e^{2|y|/ell} g:  g~(y) = g~ - E y^2 - (2/ell) E |y|^3 + O(y^4)
  eqs. (40),(41) p.10  V = G M ell/r^2 (r << ell); V = (G M/r)(1 + 2 ell^2/3r^2) (r >> ell)

  T1  (STRUCTURAL/READ) eq. (17) is a no-matter plane solution: R = 0.  MK's printed (151) fails their eq. (160) at
      F = H; the corrected form passes it and agrees with tracelessness on eq. (17)
  T2  the corridor's bulk reading at its throat is unsuppressed: E^theta_theta(r0) = -1/r0^2, the throat's own
      curvature scale.  On one static plane a vacuum region of curvature scale L >> ell reads E of order ell^2/L^4
      (MK 41's correction; Figueras-Wiseman's leading-order statement, READ in KSCALE.md).  So r0 >> ell is excluded.
      Control: the Schwarzschild member reads E = 0
  T3  (heuristic, MK's own style) below ell the field is five-dimensional: MK's leading forms meet at r = ell, so a
      four-dimensional throat needs r0 not << ell (the transfer from small black holes to a throat is the board's)
  T4  so, on one static plane, ell is of order r0 = r_min(N); read per README (H-K-PER-README, the board's), k is of
      order 1/r_min(N).  Order of magnitude only
  T5  classical validity: ell/l5 = (ell/l_P)^(2/3), large for many bits, below one at one bit; the light-crossing
      time of ell is ~1e-36 s at the example README, so a static treatment is self-consistent for a near-instantaneous
      hold
  T6  just off the throat (MK eq. 148): in g~ the throat's sphere grows, g~_thth(r0, y) = 4m^2 + y^2 + 2y^3/ell, where a
      large black hole's shrinks (contrast); the PHYSICAL sphere e^{-2|y|/ell} g~ shrinks at first order, 4m^2 - 8m^2 y/ell
Imports exactE.py and kderive.py (by path); stdlib + sympy.  python3 throatbulk.py [--selftest]
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
EXAMPLE_N = 2742570311524972

t, r, th, ph = sp.symbols("t r theta phi", positive=True)
m, r0, ell = sp.symbols("m r0 ell", positive=True)


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


def FH(r0v):
    """Eq. (17) (plane.py's transcription of Bronnikov-Kim p.4) as -F dt^2 + dr^2/H + r^2 dOmega^2."""
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) * (1 - r0v / r) / (1 - sp.Rational(3, 2) * m / r)
    return F, H


def ricci_scalar(F, H):
    g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th)**2)
    X = [t, r, th, ph]
    gi = g.inv()
    n = 4
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = [sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) - sp.diff(Gam[a][b][a], X[b])
                           + sum(Gam[a][a][d] * Gam[d][b][b] - Gam[a][b][d] * Gam[d][b][a] for d in range(n))
                           for a in range(n))) for b in range(n)]
    return sp.simplify(sum(gi[i, i] * Ric[i] for i in range(n)))


def E_mk(F, H, printed_151=False):
    E00 = F / r * (sp.diff(H, r) - (1 - H) / r)                                     # MK (150)
    Fp = sp.diff(F, r) / F
    Err = -1 / (r * H) * ((Fp if printed_151 else H * Fp) - (1 - H) / r)           # MK (151), printed / corrected
    Eth = -1 + H + r / 2 * H * (sp.diff(F, r) / F + sp.diff(H, r) / H)              # MK (152)
    return E00, Err, Eth


def t1():
    F, H = FH(2 * m)
    R = ricci_scalar(F, H)
    # MK eq. (160): F = H = 1 - 2GM/r + 2 G ell Q/r^2  ->  E_rr = -(2 G ell Q/r^4) * (-2) * g_rr  (u u - 2 r r + h)
    G_, M_, Q_ = sp.symbols("G M Q", real=True)
    Ft = 1 - 2 * G_ * M_ / r + 2 * G_ * ell * Q_ / r**2
    E160_rr = -(2 * G_ * ell * Q_ / r**4) * (-2 + 1) / Ft                            # r_r r_r = g_rr, h_rr = g_rr
    printed = sp.simplify(E_mk(Ft, Ft, printed_151=True)[1] - E160_rr)
    corrected = sp.simplify(E_mk(Ft, Ft)[1] - E160_rr)
    E00, Err, Eth = E_mk(F, H)
    trace = sp.simplify(-E00 / F + H * Err + 2 * Eth / r**2)
    return {"R": R, "printed_151_vs_160": printed, "corrected_151_vs_160": corrected, "trace_eq17": trace}


def t2():
    F, H = FH(2 * m)
    Eth = sp.simplify(E_mk(F, H)[2])
    mixed_r0 = sp.simplify((Eth / r**2).subs(r, 2 * m))
    Fs, Hs = FH(sp.Rational(3, 2) * m)
    schw = [sp.simplify(x) for x in E_mk(Fs, Hs)]
    return {"Eth": Eth, "mixed_r0": mixed_r0, "throat_curv": -1 / (2 * m)**2, "schw": schw}


def t3():
    G, M = sp.symbols("G M", positive=True)
    return {"cross": [s for s in sp.solve(sp.Eq(G * M / r, G * M * ell / r**2), r) if s.is_positive][0]}


def t45():
    kd = _load(os.path.join(HERE, "kderive.py"), "tb_kderive")
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "tb_exactE")
    lP = sp.sqrt(kd.HBAR * kd.G / kd.C**3)
    r1 = sp.N(lP * sp.sqrt(sp.log(2) / sp.pi), 30)
    r1_owner = 2 * kd.G * sp.Float(ex.e_per_sqrt_bit()) / kd.C**4
    rN = sp.sqrt(EXAMPLE_N) * r1
    return {"r1": r1, "r1_owner": r1_owner, "rN": rN, "k_order": 1 / rN,
            "ell_l5_example": sp.N((rN / lP) ** sp.Rational(2, 3), 6), "ell_l5_onebit": sp.N((r1 / lP) ** sp.Rational(2, 3), 6),
            "crossing_s": sp.N(rN / kd.C, 4)}


def t6():
    y = sp.Symbol("y", nonnegative=True)
    F, H = FH(2 * m)
    Eth_r0 = sp.limit(sp.simplify(E_mk(F, H)[2]), r, 2 * m)
    gt = (2 * m)**2 - Eth_r0 * y**2 - 2 / ell * Eth_r0 * y**3                       # MK eq. 148, theta-theta
    phys = sp.series(sp.exp(-2 * y / ell) * gt, y, 0, 2).removeO()
    # contrast: a large black hole, H = 1 - 2m/r - 4 m ell^2/(3 r^3) (MK 155), F = 1 - 2m/r to that order
    Hb = 1 - 2 * m / r - 4 * m * ell**2 / (3 * r**3)
    Eth_big = sp.series(sp.simplify(E_mk(1 - 2 * m / r, Hb)[2]), ell, 0, 3).removeO()
    return {"Eth_r0": Eth_r0, "g_tilde": sp.expand(gt), "phys_first": sp.expand(phys), "Eth_big": sp.simplify(Eth_big),
            "Eth_big_far": sp.limit(Eth_big * r**3, r, sp.oo)}


def compute():
    return {"t1": t1(), "t2": t2(), "t3": t3(), "t45": t45(), "t6": t6()}


def report(D):
    a, b, c, d, f = D["t1"], D["t2"], D["t3"], D["t45"], D["t6"]
    print("throatbulk.py -- C, first part: the corridor on one static plane (items 127, 140, 141; against 138)\n")
    print("T1 eq. (17) at r0 = 2m: R = %s; MK (151) printed vs their (160) at F = H: residue %s; corrected: %s; "
          "corrected E traceless on eq. (17): %s" % (a["R"], a["printed_151_vs_160"], a["corrected_151_vs_160"],
                                                     a["trace_eq17"]))
    print("T2 at the throat E^theta_theta = %s = -1/r0^2 (the throat's own curvature: unsuppressed); Schwarzschild "
          "member E = %s" % (b["mixed_r0"], b["schw"]))
    print("T3 four- and five-dimensional leading forms meet at r = %s (heuristic)" % c["cross"])
    print("T4 on one static plane, ell ~ r0: at the example README r_min = %s m, k of order %s m^-1 (order of magnitude)"
          % (sp.N(d["rN"], 6), sp.N(d["k_order"], 3)))
    print("T5 ell/l5 with ell = r_min: example %s, one bit %s; light-crossing time of ell at the example %s s"
          % (d["ell_l5_example"], d["ell_l5_onebit"], d["crossing_s"]))
    print("T6 off the throat: E_thth(r0) = %s; g~_thth = %s (grows relative to the black string); physical to first "
          "order %s (shrinks); a large black hole's E_thth = %s, far out 2 m ell^2/(3 r^3) > 0 (g~ shrinks)"
          % (f["Eth_r0"], f["g_tilde"], f["phys_first"], f["Eth_big"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    D = compute()
    a, b, c, d, f = D["t1"], D["t2"], D["t3"], D["t45"], D["t6"]
    chk("T1 (STRUCTURAL): eq. (17) at r0 = 2m has R = 0 (how Bronnikov-Kim's family is built)", a["R"] == 0)
    chk("T1: MK's printed (151) fails their own (160) at F = H; with H on F'/F it passes",
        a["printed_151_vs_160"] != 0 and a["corrected_151_vs_160"] == 0)
    chk("T1: the corrected E is traceless on eq. (17)", a["trace_eq17"] == 0)
    chk("T2: at the throat E^theta_theta = -1/r0^2, the throat's own curvature scale (unsuppressed)",
        sp.simplify(b["mixed_r0"] - b["throat_curv"]) == 0)
    chk("T2 control: the Schwarzschild member reads E = 0", all(x == 0 for x in b["schw"]))
    chk("T3 (STRUCTURAL, heuristic): the leading four- and five-dimensional forms meet at r = ell",
        sp.simplify(c["cross"] - ell) == 0)
    chk("T4: the one-bit throat used equals exactE's to 1e-15", abs(d["r1_owner"] / d["r1"] - 1) < 1e-15)
    chk("T5: with ell ~ r_min the bulk is classical at the example README (ell/l5 > 1e4), not at one bit",
        d["ell_l5_example"] > 1e4 and d["ell_l5_onebit"] < 1)
    chk("T6: in g~ the throat's sphere grows off the plane (E_thth(r0) = -1)", f["Eth_r0"] == -1)
    chk("T6 contrast (READ): a large black hole's E_thth -> 2 m ell^2/(3 r^3) > 0 far out, so its g~ sphere shrinks",
        sp.simplify(f["Eth_big_far"] - 2 * m * ell**2 / 3) == 0)
    chk("T6 (STRUCTURAL: the warp factor): the physical sphere shrinks at first order, 4m^2 - 8 m^2 y/ell",
        sp.simplify(f["phys_first"] - (4 * m**2 - 8 * m**2 * sp.Symbol("y", nonnegative=True) / ell)) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
