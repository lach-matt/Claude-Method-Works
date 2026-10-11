#!/usr/bin/env python3
"""rows_small.py -- items 251, 256, 262: the chain's rows that rested on M1 alone, re-read at the family's small end
(the localized five-dimensional hole).  The ten were B2t, E4r, G1, G3, H2tu, O1b, O1c, O2, Z1t and Z2r (chain_cypher,
item 231); O1b and O1c were restated by M's item 259.  Each row's record text is a reading of eq. (17); here each is
computed for f = 1 - r_h^2/r^2 on the plane and the Tangherlini bulk beneath it.  Worked in the conversation
(computed with sympy, exact where marked; deduced where marked; not verified by a separate session; not seated);
2026-10-11.

  R0 (read) M's item-262 words, verbatim in the rulings file.
  G1s (computed, exact) One exact energy, at the bound.  The record's three steps carry: capacity exactly N (101.6),
     now the five-dimensional count over both sides (C2 R1, verified); the horizon and the throat hold it together
     (132), the throat being the bridge's least sphere, r_h (G3s); the energy is the pull (131/133), now the hole's
     Komar mass (C4 N1).  E(N) = 3 pi c^4 r_h(N)^2/(8 G5) = (3 pi/8)(2 N ln2/pi^2)^(2/3) (hbar^2 c^6/G5)^(1/3) -- one value
     for each N at a given ell (equal to corridor_family F1's small end, computed).
  G3s (STRUCTURAL, as G3 on the record) Both holds at least size: the bridge's slice dx^2 + (r_h^2 + x^2) dOmega^2 has
     its least sphere at x = 0, radius r_h, where f = 0 -- the horizon -- so the throat and the horizon are one sphere,
     and r_h = (8 G5 E/(3 pi c^4))^(1/2) is the record's r0 = 2m at the small end.  [C1 verifier, item 254: a least
     sphere on the time-symmetric slice only -- the bridge pinches on later slices; not a static throat.]
  H2tu-s (computed, exact) The horizon's trace on each plane is r = r_h (f = 0 on the plane's metric); position 2's
     plane, the equator in the second exterior, reads the same f (the eternal solution's two exteriors are isometric,
     C1 H4) -- position 2 on our plane reads as ours.  But the record's "with area N A_bit" does not carry: the README
     is held by the horizon's 3-sphere, 2 pi^2 r_h^3 = 4 N ln2 l5^3 (C2 R1), and the trace's 2-area read in the
     plane's bits, 4 pi r_h^2/A_bit, is (pi/ln2)(r_h/l_P)^2 = 7.9e14 N at the example README (ell = 13.964 um),
     falling as N^(-1/3) ell^(2/3) -- exactly 2N/pi where r_h reaches ell (the crossover, C3 F2), so the two ends'
     holding agrees there within the pi/2 C3 already carries.
  O1b, O1c (M's item 259) The static bulk, its horizon and the bridge are regular and complete for the passage; the
     interior singularity is outside it.  Not recomputed here.
  O2s (computed, exact) The horizon is not extremal: surface gravity kappa = f'(r_h)/2 = c^2/r_h (C1 H4), temperature
     hbar c/(2 pi k r_h).  Item 251 dropped clause (O)'s "extremal"; O2 as worded ("surface gravity 0") is false at the
     small end, and every result resting on the extremal horizon (stability.py's D' = 0, Wall E's transport) does not
     carry.  The hole's linear stability is READ (Ishibashi-Kodama, via B4D-STAGE1.md), not computed here.
  Z1t-s (computed, exact) Along the mouth's radial ray, our leg: the five-dimensional null energy is zero (the bulk is
     Ricci-flat, C1 H1) and so is the plane's reading -- G^t_t = G^r_r = r_h^2/r^4, so G_ab k^a k^b = 0 on every radial
     null k.  The record's "the plane's deficit the bulk's pull" becomes: no deficit on the radial ray; the plane's
     reading on tangential rays, -2 r_h^2/r^4, is the bulk's traceless Weyl term (C1 verifier, item 254).
  Z2r-s (computed, exact) Our leg's integral within the reach equals the plane's reading -- both zero, exactly, not
     to M1-c's order.
  B2t-s (computed, from C1) The local bulk beneath the corridor: Tangherlini, Ricci-flat, the plane totally geodesic
     (C1 H1-H2, verified).
  E4r-s (computed, exact) The field energy outside the neck within the reach.  In five dimensions it is zero: the
     Komar mass is the same at every r (C4 N1), so no energy lies between the horizon and any sphere.  The plane's
     four-dimensional reading, its Einstein tensor read with G, is the Weyl term as an energy density, rho_W = -r_h^2 c^4
     /(8 pi G r^4) -- negative, where the record's E4r is positive -- with Misner-Sharp mass c^2 r_h^2/(2 G r), so
     between r_h and R it reads -(c^4 r_h/(2G))(1 - r_h/R) = -(4/(3 pi))(ell/r_h)(1 - r_h/R) E: -5.3e14 E at the example
     README (R >> r_h), its size set by ell, not by N.  At r = ell the plane's Misner-Sharp mass is (4/(3 pi)) E/c^2 =
     0.42 E/c^2 -- of the order of the hole's own, where the plane goes over to four-dimensional gravity and its 1/r tail
     (C1 H3, A4).  So within the reach the plane's 4D reading is the appearance (183, 254), not the energy: read with
     G at r << ell it overstates the field by ell/r_h, because gravity there is five-dimensional.

What this does not show.
  - The rows that rest on more than M1 (M1P2x, WRITE, ARRIVAL, CLOSE and the rows above them) -- in chain order next.
  - The plane's reading between r ~ ell and r >> ell (the numerical brane holes, C3 F5).
  - E4r's sign change moves no other row: none rests on E4r (warptheorem.py RESTS_ON, checked), and the record's own
    E4r already read "not the plane's energy".  The record's ledger (ledger.py E3/E4: the throat's m plus the Weyl
    field's m/4, ADM 5m/4) is eq. (17)'s; at the small end the five-dimensional energy is the Komar E with no field
    part, and E3 is re-read with the chain.

Imports localized_hole.py, m1_small.py and corridor_family.py by path.  Stdlib + sympy.
python3 rows_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M262 = 'C6 "Ready, verify it"; C5 "Ready, verify it"; C4 "Ready, verify it".'
N_EX = 2742570311524972

t, r, rh, G, G5, c, R, ell, N, hb = sp.symbols("t r r_h G G5 c R ell N hbar", positive=True)


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _f():
    if MUT.get("extremal"):
        return (1 - rh / r) ** 2
    if MUT.get("four_d"):
        return 1 - rh / r
    return 1 - rh ** 2 / r ** 2


def plane():
    """the plane's 4D metric -f dt^2 + dr^2/f + r^2 dOmega^2: its mixed Einstein tensor, null readings, surface gravity"""
    LH = _load("localized_hole.py", "rs_lh")
    th, ph = sp.symbols("theta phi")
    f = _f()
    g = [-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2]
    _, Ric, _ = LH.curvature(g, [t, r, th, ph])                 # diagonal metric: Ricci with indices down
    Rs = sp.simplify(sum(Ric[i][i] / g[i] for i in range(4)))
    Gmix = sp.diag(*[sp.simplify(Ric[i][i] / g[i] - Rs / 2) for i in range(4)])
    radial = sp.simplify(Gmix[0, 0] - Gmix[1, 1])               # G_ab k^a k^b on radial null k, up to (k^t)^2 f
    tangential = sp.simplify(-Gmix[0, 0] + Gmix[2, 2])          # on a tangential null k, unit normalised
    hzn = [x for x in sp.solve(sp.Eq(f, 0), r) if x.is_positive]
    kappa = sp.simplify(sp.diff(f, r).subs(r, hzn[0]) / 2)
    return dict(Gmix=Gmix, radial=radial, tangential=tangential, horizon=hzn, kappa=kappa, f=f)


def energies(p):
    """E(N) from the Komar mass at r_h(N); the plane's Weyl reading and its Misner-Sharp mass (SI symbols, 8 pi G)"""
    MS = _load("m1_small.py", "rs_m1")
    CF = _load("corridor_family.py", "rs_cf")
    M = MS.komar(5)["M"].subs(MS.G5, G5)                         # 3 pi r_h^2/(8 G5), r-independent (C4 N1)
    l5 = (hb * G5 / c ** 3) ** sp.Rational(1, 3)
    rhN = (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3) * l5
    E_N = sp.simplify(c ** 4 * M.subs(rh, rhN))
    e_cf = CF.ends()["Es"].subs({CF.N: N, CF.G: G5 / ell, CF.ell: ell, CF.hb: hb, CF.c: c})
    rho_W = sp.simplify(-p["Gmix"][0, 0] * c ** 4 / (8 * sp.pi * G))  # T^t_t = -rho, G^t_t = 8 pi G T^t_t / c^4
    msharp = sp.simplify(c ** 2 * r / (2 * G) * (1 - p["f"]))
    field = sp.simplify(sp.integrate(rho_W * 4 * sp.pi * r ** 2, (r, rh, R)))
    E = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * G * ell)               # the small end's E with G5 = G ell
    return dict(M=M, E_N=E_N, E_cf=sp.simplify(e_cf), rho_W=rho_W, msharp=msharp, field=field,
                field_over_E=sp.simplify(field / E), ms_at_ell_over_E=sp.simplify(msharp.subs(r, ell) * c ** 2 / E))


def holding():
    """H2tu: the trace's 2-area in the plane's bits against N; the 3-area against 4 N ln2 l5^3"""
    l5 = (hb * G * ell / c ** 3) ** sp.Rational(1, 3)
    rhN = (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3) * l5
    lP2 = hb * G / c ** 3
    bits2 = sp.simplify(4 * sp.pi * rhN ** 2 / (4 * sp.log(2) * lP2))
    three = sp.simplify(2 * sp.pi ** 2 * rhN ** 3 - 4 * N * sp.log(2) * l5 ** 3)
    Ns = sp.pi ** 2 * ell ** 2 / (2 * sp.log(2) * lP2)               # the crossover (C3 F2): r_h = ell
    at_cross = sp.simplify((bits2 / N).subs(N, Ns))
    return dict(bits2_over_N=sp.simplify(bits2 / N), three=three, at_cross=at_cross)


def example():
    PG = _load("p2_gravity.py", "rs_pg")
    Gs, cs, hbs, ell_ = PG.G, PG.C, PG.HBAR, PG.ELL_MAX
    l5 = (hbs * Gs * ell_ / cs ** 3) ** (1 / 3)
    rh_ = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    lP2 = hbs * Gs / cs ** 3
    return dict(bits2_over_N=4 * math.pi * rh_ ** 2 / (4 * math.log(2) * lP2) / N_EX, ell_over_rh=ell_ / rh_,
                field_over_E=-(4 / (3 * math.pi)) * ell_ / rh_)


def compute():
    p = plane()
    return dict(p=p, e=energies(p), h=holding(), ex=example())


def report(o):
    p, e, h, x = o["p"], o["e"], o["h"], o["ex"]
    print("rows_small.py -- the rows that rested on M1 alone, at the family's small end\n")
    print("G1s E(N) = %s (Komar M = %s)" % (e["E_N"], e["M"]))
    print("H2tu-s horizon r = %s; trace's 2-area in the plane's bits / N = %s = %.3g at the example; at the crossover %s"
          % (p["horizon"], h["bits2_over_N"], x["bits2_over_N"], h["at_cross"]))
    print("O2s surface gravity %s" % p["kappa"])
    print("Z1t-s plane's G^a_b = %s; radial null %s; tangential %s" % (
        [sp.simplify(p["Gmix"][i, i]) for i in range(4)], p["radial"], p["tangential"]))
    print("E4r-s rho_W = %s; Misner-Sharp %s; field r_h..R = %s = %s E; at the example %.3g E (ell/r_h %.3g); "
          "Misner-Sharp at ell / (E/c^2) = %s = %.3f" % (e["rho_W"], e["msharp"], e["field"], e["field_over_E"],
                                                         x["field_over_E"], x["ell_over_rh"], e["ms_at_ell_over_E"],
                                                         float(e["ms_at_ell_over_E"])))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("R0 M's item-262 words verbatim in the rulings file", M262 in rul)
    p, e, h, x = o["p"], o["e"], o["h"], o["ex"]
    ok = sp.simplify(e["M"] - 3 * sp.pi * rh ** 2 / (8 * G5)) == 0
    ok &= sp.simplify(e["E_N"] - sp.Rational(3, 8) * sp.pi * (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(2, 3)
                      * (hb ** 2 * c ** 6 / G5) ** sp.Rational(1, 3)) == 0
    ok &= sp.simplify(e["E_N"] - e["E_cf"].subs(ell, G5 / G)) == 0
    add("G1s E(N) = (3 pi/8)(2 N ln2/pi^2)^(2/3) (hbar^2 c^6/G5)^(1/3), the Komar mass at r_h(N) -- corridor_family's "
        "small end", ok)
    ok = p["horizon"] == [rh] and sp.simplify(h["three"]) == 0
    ok &= sp.simplify(h["at_cross"] - 2 / sp.pi) == 0 and "%.2g" % x["bits2_over_N"] == "7.9e+14"
    add("G3s/H2tu-s the horizon (and least sphere) at r_h; its 3-area holds N (2 pi^2 r_h^3 = 4 N ln2 l5^3); the "
        "trace's 2-area holds 7.9e14 N at the example, 2N/pi at the crossover -- the record's 'area N A_bit' does not carry",
        ok)
    add("O2s surface gravity 1/r_h: not extremal (item 251)", sp.simplify(p["kappa"] - 1 / rh) == 0)
    ok = sp.simplify(p["radial"]) == 0 and sp.simplify(p["tangential"] + 2 * rh ** 2 / r ** 4) == 0
    ok &= sp.simplify(p["Gmix"][0, 0] - rh ** 2 / r ** 4) == 0 and sp.simplify(p["Gmix"].trace()) == 0
    add("Z1t-s/Z2r-s the plane's G^a_b = (r_h^2/r^4) diag(1, 1, -1, -1), traceless: radial null reading 0 exactly (the "
        "5D null energy 0 too), tangential -2 r_h^2/r^4 (the Weyl term)", ok)
    ok = sp.simplify(e["rho_W"] + rh ** 2 * c ** 4 / (8 * sp.pi * G * r ** 4)) == 0
    ok &= sp.simplify(e["field"] + c ** 4 * rh / (2 * G) * (1 - rh / R)) == 0
    ok &= sp.simplify(e["field_over_E"] + 4 * ell / (3 * sp.pi * rh) * (1 - rh / R)) == 0
    ok &= sp.simplify(e["ms_at_ell_over_E"] - 4 / (3 * sp.pi)) == 0 and "%.2g" % x["field_over_E"] == "-5.3e+14"
    add("E4r-s the plane's Weyl reading is negative, rho_W = -r_h^2 c^4/(8 pi G r^4); between r_h and R it reads -(4/(3 "
        "pi))(ell/r_h)(1 - r_h/R) E, -5.3e14 E at the example; Misner-Sharp at ell = (4/(3 pi)) E/c^2 (the 5D field "
        "energy is 0: Komar r-independent)", ok)
    return res


MUTANTS = {"extremal": "the plane read with an extremal f = (1 - r_h/r)^2",
           "four_d": "the plane read with 4D Schwarzschild f = 1 - r_h/r"}


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
        print("  mutant %-9s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
