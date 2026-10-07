#!/usr/bin/env python3
"""throatbulk.py -- C, first part: what a static bulk asks of the corridor, and what the corridor asks of k.

M (item 141): the planes are static and a stable throat forms between them; (item 140) "k is dependent on our work";
(item 127) r0, E and k are coefficients, a variable solution.  static.py: static and face to face, the two planes are
one Randall-Sundrum II plane at long range.  So the corridor -- Bronnikov-Kim eq. (17) at r0 = 2m -- is read here on
one static RS II plane, with its throat stable (H-STABLE-THROAT, the board's reading of item 141).

READ: Maartens-Koyama, Living Rev. Rel. 13 (2010) 5, arXiv:1004.3962v2 ("MK"):
  eq. (143) p.26  a vacuum on the plane obeys R_mu nu = -E_mu nu, R = 0 = E^mu_mu (E the bulk's Weyl reading)
  eqs. (150),(152) p.27  E_00 and E_thth for -F dt^2 + dr^2/H + r^2 dOmega^2  ((151) as read does not reproduce
                  R_rr for eq. (17); not used -- E_rr is taken from tracelessness instead)
  eq. (154) p.27  the plane's sphere off the plane: g_thth(r, y) = r^2 - psi'(1 + 2|y|/ell) y^2 + O(y^4),
                  with H = 1 - 2m/r + psi
  eq. (155) p.27  for a large object on one static plane, psi = -4 m ell^2/(3 r^3)
  eqs. (40),(41) p.10  V = G M ell / r^2 for r << ell (five-dimensional); V = (G M/r)(1 + 2 ell^2/3r^2) for r >> ell

  T1  eq. (17) is a vacuum-plane solution: R = 0, and its Ricci tensor is exactly -E with E from MK (150), (152) and
      tracelessness.  Control: the no-throat member r0 = 3m/2 (Schwarzschild, BK p.4) has E = 0
  T2  how far the corridor's own field can reach: its psi falls as -m/(2r) (the far-field gamma = 5/4, STRUCTURAL);
      one static plane supplies psi = -4 m ell^2/(3 r^3).  The ratio is 3 r^2/(8 ell^2): they meet at
      r_x = sqrt(8/3) ell, and beyond it eq. (17) asks for more Weyl field than the plane gives, growing as r^2.
      Control: the Schwarzschild member asks for none
  T3  where the field turns five-dimensional: MK's two leading forms meet at r = ell
  T4  the window this gives (indicative -- both edges are leading-order forms used at their crossovers): the throat
      inside the corridor's own zone (r0 <= r_x) and on the four-dimensional side (r0 >= ell):
      sqrt(3/8) <= ell/r0 <= 1, so k r_min(N) is between 1 and sqrt(8/3) = 1.633.  k = c / r_min(N) with c of order one
  T5  classical validity of that bulk: ell/l5 = (ell/l_P)^(2/3), large for many bits, below one at one bit
  T6  the bulk just off the throat (MK eq. 154): the throat's sphere WIDENS away from the plane,
      g_thth(r0, y) = r0^2 + (1/(2m))(1 + 2|y|/ell) y^2 + ... ; contrast (READ): a large black hole's sphere shrinks
      away from it (MK: "pancake-like")
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
K_MEASURED_FLOOR = sp.Float("1.25e4")                             # m^-1, the strongest bound read (OUTSIDE.md)

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


def ricci_diag(F, H):
    g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th)**2)
    X = [t, r, th, ph]
    gi = g.inv()
    n = 4
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = [sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) - sp.diff(Gam[a][b][a], X[b])
                           + sum(Gam[a][a][d] * Gam[d][b][b] - Gam[a][b][d] * Gam[d][b][a] for d in range(n))
                           for a in range(n))) for b in range(n)]
    Rs = sp.simplify(sum(gi[i, i] * Ric[i] for i in range(n)))
    return Ric, Rs


def weyl_mk(F, H):
    """MK eqs. (150), (152); E_rr from E^mu_mu = 0 (MK 143)."""
    E00 = F / r * (sp.diff(H, r) - (1 - H) / r)
    Ethth = -1 + H + r / 2 * H * (sp.diff(F, r) / F + sp.diff(H, r) / H)
    Err = (E00 / F - 2 * Ethth / r**2) / H
    return sp.simplify(E00), sp.simplify(Err), sp.simplify(Ethth)


def t1():
    F, H = FH(2 * m)
    Ric, Rs = ricci_diag(F, H)
    E00, Err, Ethth = weyl_mk(F, H)
    match = [sp.simplify(Ric[0] + E00) == 0, sp.simplify(Ric[1] + Err) == 0, sp.simplify(Ric[2] + Ethth) == 0]
    Fs, Hs = FH(sp.Rational(3, 2) * m)
    E00s, Errs, Eths = weyl_mk(Fs, Hs)
    return {"R": Rs, "match": match, "E00": E00, "schw_E": [E00s, Errs, Eths]}


def psi_of(r0v):
    F, H = FH(r0v)
    return sp.simplify(H - 1 + 2 * m / r)


def t2():
    psi = psi_of(2 * m)
    lead = sp.limit(psi * r, r, sp.oo)                               # the 1/r coefficient
    psi_plane = -4 * m * ell**2 / (3 * r**3)                         # MK eq. 155
    ratio = sp.simplify((lead / r) / psi_plane)
    rx = [s for s in sp.solve(sp.Eq(ratio, 1), r) if s.is_positive][0]
    lead_schw = sp.limit(psi_of(sp.Rational(3, 2) * m) * r, r, sp.oo)
    return {"psi": psi, "lead": lead, "ratio": ratio, "rx": sp.simplify(rx / ell), "lead_schw": lead_schw}


def t3():
    G, M = sp.symbols("G M", positive=True)
    v4, v5 = G * M / r, G * M * ell / r**2                           # MK eqs. 41 and 40, leading terms
    return {"cross": [s for s in sp.solve(sp.Eq(v4, v5), r) if s.is_positive][0]}


def t4(rx_over_ell):
    lo, hi = 1 / rx_over_ell, sp.Integer(1)                          # ell/r0 between these
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "tb_exactE")
    kd = _load(os.path.join(HERE, "kderive.py"), "tb_kderive")
    r1 = sp.N(sp.sqrt(kd.HBAR * kd.G / kd.C**3) * sp.sqrt(sp.log(2) / sp.pi), 30)
    rN = sp.sqrt(EXAMPLE_N) * r1
    e1 = sp.Float(ex.e_per_sqrt_bit())
    r1_owner = 2 * kd.G * e1 / kd.C**4
    k_lo, k_hi = 1 / (hi * rN), 1 / (lo * rN)
    return {"ell_over_r0": (lo, hi), "c": (1 / hi, 1 / lo), "rN": rN, "k": (k_lo, k_hi), "r1": r1,
            "r1_owner": r1_owner, "lP": sp.sqrt(kd.HBAR * kd.G / kd.C**3)}


def t5(d4):
    lP = d4["lP"]
    out = {}
    for label, rr in (("example", d4["rN"]), ("one bit", d4["r1"])):
        out[label] = [sp.N((c * rr / lP) ** sp.Rational(2, 3), 6) for c in (d4["ell_over_r0"][0], 1)]
    return out


def t6():
    y = sp.Symbol("y", nonnegative=True)
    psi = psi_of(2 * m)
    dpsi_r0 = sp.simplify(sp.diff(psi, r).subs(r, 2 * m))
    gthth = (2 * m)**2 - dpsi_r0 * (1 + 2 * y / ell) * y**2               # MK eq. 154, to y^3
    big = -4 * m * ell**2 / (3 * r**3)                                    # MK eq. 155: a large black hole
    dbig = sp.simplify(sp.diff(big, r))
    return {"dpsi_r0": dpsi_r0, "gthth": sp.expand(gthth), "dpsi_bigBH": dbig}


def compute():
    a, b, c = t1(), t2(), t3()
    d = t4(b["rx"])
    return {"t1": a, "t2": b, "t3": c, "t4": d, "t5": t5(d), "t6": t6()}


def report(D):
    a, b, c, d, e, f = D["t1"], D["t2"], D["t3"], D["t4"], D["t5"], D["t6"]
    print("throatbulk.py -- C, first part: the corridor on one static plane (items 127, 140, 141)\n")
    print("T1 eq. (17) at r0 = 2m: R = %s; R_mu nu = -E_mu nu (MK 150, 152, traceless) for tt, rr, thth: %s; "
          "Schwarzschild member E = %s" % (a["R"], a["match"], a["schw_E"]))
    print("   E_tt = %s" % a["E00"])
    print("T2 corridor psi = %s, far field %s/r; one static plane psi = -4 m ell^2/(3 r^3) (MK 155); ratio %s; they "
          "meet at r = %s ell = %.4f ell; Schwarzschild member's 1/r term: %s"
          % (b["psi"], b["lead"], b["ratio"], b["rx"], float(b["rx"]), b["lead_schw"]))
    print("T3 four- and five-dimensional leading forms meet at r = %s" % c["cross"])
    print("T4 window (indicative): %.4f <= ell/r0 <= %s, so k = c / r_min(N), c between %s and %.4f"
          % (float(d["ell_over_r0"][0]), d["ell_over_r0"][1], d["c"][0], float(d["c"][1])))
    print("   at the example README: r_min = %s m; k between %s and %s m^-1 (measured floor %s m^-1)"
          % (sp.N(d["rN"], 6), sp.N(d["k"][0], 4), sp.N(d["k"][1], 4), K_MEASURED_FLOOR))
    print("T5 ell / l5 at the window's edges: example README %s; one bit %s" % (e["example"], e["one bit"]))
    print("T6 off the throat: psi'(r0) = %s, so g_thth(r0, y) = %s (widens); a large black hole's psi' = %s > 0 "
          "(shrinks)" % (f["dpsi_r0"], f["gthth"], f["dpsi_bigBH"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    D = compute()
    a, b, c, d, e, f = D["t1"], D["t2"], D["t3"], D["t4"], D["t5"], D["t6"]
    chk("T1: eq. (17) at r0 = 2m has R = 0 and its Ricci tensor equals -E from MK (150), (152) and tracelessness",
        a["R"] == 0 and all(a["match"]))
    chk("T1 control: the Schwarzschild member (r0 = 3m/2) has E = 0", all(x == 0 for x in a["schw_E"]))
    chk("T2 (STRUCTURAL): the corridor's far-field psi is -m/(2r), gamma = 5/4", b["lead"] == -m / 2)
    chk("T2: the corridor's psi and one static plane's meet at r_x = sqrt(8/3) ell; beyond, the ratio grows as r^2",
        sp.simplify(b["rx"] - sp.sqrt(sp.Rational(8, 3))) == 0 and sp.simplify(b["ratio"] - 3 * r**2 / (8 * ell**2)) == 0)
    chk("T2 control: the Schwarzschild member asks for no 1/r Weyl field", b["lead_schw"] == 0)
    chk("T3: the four- and five-dimensional leading forms meet at r = ell", sp.simplify(c["cross"] - ell) == 0)
    chk("T4: the window sqrt(3/8) <= ell/r0 <= 1 puts k r_min(N) between 1 and 1.633",
        abs(float(d["c"][1]) - 1.632993) < 1e-6 and d["c"][0] == 1)
    chk("T4: the one-bit throat used here equals exactE's to 1e-15 (K1)", abs(d["r1_owner"] / d["r1"] - 1) < 1e-15)
    chk("T4: at the example README the window's k lies far above the measured floor",
        d["k"][0] > K_MEASURED_FLOOR * 10**20)
    chk("T5: the bulk is classical (ell/l5 >> 1) at the example README, not at one bit",
        min(e["example"]) > 1e4 and max(e["one bit"]) < 1)
    chk("T6: off the throat the sphere widens (psi'(r0) = -1/(2m) < 0)", sp.simplify(f["dpsi_r0"] + 1 / (2 * m)) == 0)
    chk("T6 contrast (READ): a large black hole's sphere shrinks off the plane (psi' > 0)",
        sp.simplify(f["dpsi_bigBH"] - 4 * m * ell**2 / r**4) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
