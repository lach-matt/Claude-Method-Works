#!/usr/bin/env python3
"""close_large.py -- item 356: the CLOSE row at the family's large end, on C3's large brane hole, with the four rows
that rest on it alone (E1u, E1x, E2u, E2x); worked beside the interior's build (360, the board's reading (a)).  The
small end's is close_small.py (CLOSEs, on M-ENERGY-STAYS, 336).  Worked in the conversation (computed with sympy, exact
where marked; READ where marked; estimates marked; deduced where marked; not verified by a separate session; not
seated); 2026-10-13.

  L0 (read) The words the rows rest on, verbatim in the rulings file: 336, "I think it is B", seated M-ENERGY-STAYS;
     356, "I still see a lot, including items that rest on M1 and B4d"; 358, "Once everything that doesn't rely on
     SOURCE is resolved and green"; 360, "I agree. Option 1 please".
  L1 (computed, exact; imported) The flux that moves a face, on the plane.  The large end reads four-dimensional
     Schwarzschild on the plane with corrections O(ell^2/r0^2) (C3; m1_large M4).  Its ingoing Vaidya form has the one
     Einstein component G_vv = 2 m'(v)/r^2 and the outgoing G_uu = -2 m'(u)/r^2 (close_small K1's control, imported):
     one loss of mass reads as a negative inflow at our face and a positive outflow at position 2's.
  L2 (READ; computed; imported) Which face can shrink.  Our face is a non-degenerate Killing horizon, kappa^2 =
     1/(16 M^2) (m1_large M4, imported) -- future outer, as at the small end (close_small K2, Hayward's second law,
     READ there: "If the null energy condition holds, the area form of a future outer or past inner trapping horizon is
     non-decreasing").  The null energy condition holds in the bulk, R_AB k^A k^B = 0 on every null ray of the Einstein
     bulk (m1_large M1, imported), and on the plane, whose stress is the tension alone, -sigma gamma_mn, so T k k = 0
     for every null k along it (m1_large M2; computed).  So under classical matter our face cannot shrink; only the
     emission's own negative influx ends it -- M-ENERGY-STAYS's mechanism.  Position 2's face is past outer and shrinks
     as it releases positive energy, as at the small end.
  L3 (computed; READ where marked; estimate where marked) The large hole's life.  Hawking's temperature is the
     Schwarzschild one to first order (AFPY, READ in m1_large M7), k T = hbar c^3/(8 pi G M).  An upper bound on the
     power: every one of Z = 108.75 species (the Standard Model's 106.75 and the graviton's 2, o3_write W3's Z, all
     lighter than the hole's temperature, 3.95e10 GeV at the example README) radiating as a blackbody through the
     geometric-optics capture cross-section 27 pi M^2 (standard-not-READ; it bounds the grey-body cross-sections from
     above at every frequency for the massless species, the low-frequency s-wave of a scalar reaching only the
     horizon's 16 pi M^2), P <= Z (pi^2/120) (k T)^4 x 4 x 27 pi M^2 = alpha / M^2 with alpha = 27 Z/(491520 pi)
     (computed, exact; Planck units).  So the life, M^3/(3 alpha) at least, is in clocks of GM/c^3 at least
     M^2/(3 alpha) = 2.417 N (computed; M^2 = N ln2/(4 pi), o3_write's m_squared) -- 6.63e15 clocks at the example
     README, 3.3e10 times the write's floor of 199,702.19 clocks (o3_write t_min, imported).  Across the controlled large
     end the ratio grows as N^(2/3): at its narrowest corner, r0 = 10 ell at ell = 22.4 l_P (m1_large M5's classical
     control), N = 2.27e5 and the ratio is 6.5e3 (computed).  Two channels are not the brane's: the bulk's gravitons,
     whose coupling to the plane at frequencies below 1/ell is suppressed by (k T ell/hbar c)^2 = (ell/(4 pi r0))^2 <=
     6.3e-5 at r0 >= 10 ell (estimate, standard-not-READ); and the dual CFT's O((ell/l_P)^2) degrees of freedom, whose
     classical evaporation of large holes was conjectured -- Figueras and Wiseman (1105.2558, READ): "a remarkable
     conjecture has been made in [9, 10] that static black holes can not exist in RSII for radius much greater than
     the AdS length" ... "the conjecture is based on applying free field theory intuition to the CFT, which is strongly
     coupled", and "We construct large RSII static black holes with radius up to ~20 ell" -- the static large hole
     exists (C3), so no classical channel drains it (deduced).  The life ends at the small end: as M falls, r0 crosses
     ell and the last part is close_small's, a fraction (r0'/r0)^3 of the life below a radius r0' (computed, t ~ M^3).
  L4 (computed; READ where marked; deduced where marked) Position 2's face at the large end.  Its open period depends
     on position 2's tension, as at the small end (c8_level V2-V3, imported readings): (a) position 2's plane at our
     sigma (226's 2a-2c; 218; 219) -- no junction on either face (c8_level V2), J1 does not bind, and the white-hole
     phase is Barcelo, Carballo-Rubio and Garay's short one, (Delta u)* <~ r_m <~ 2 r_s (READ in c_junction J2), at the
     large end 2 r0/c = 4 clocks of GM/c^3 (computed); (b) 139 (1)'s -sigma/4 -- the junction rises on position 2's
     face, mu' = 5 sigma/4 on its own or sigma/2 as the side total (c8_level V3), and what emerges sees, over the
     plane's horizon sphere, 4 pi r^2 (1/kappa) E~ mu/|V| (m1p2x_fifth F1, c_junction J1).  At the small end that is
     (10/pi)(r_h/ell) E~ E (e^Dtau - 1) (reproduced exactly); at the large end, with 4 pi r0^2, 1/kappa = 2 r0 and
     E = c^4 r0/(2G), it is 15 (r0/ell)^2 E~ E (e^Dtau - 1) at mu' = 5 sigma/4 and 6 (r0/ell)^2 at sigma/2 (computed,
     exact, sigma = 3 c^4/(4 pi G ell^2)).  So the face is open at most ln(1 + (ell/r0)^2/15) e-folds -- 6.7e-4 e-folds,
     2.7e-3 clocks, at r0 = 10 ell, falling as (ell/r0)^2 -- or 1.7e-3 e-folds on the side total: on 139 (1)'s quarter
     the large end's white-hole face is closed by its junction within a small fraction of one clock.  Either way the
     face closes, releasing position 2's own energy (110, 111 (a), 240; 336 (a), the board's reading).  Whether the
     README crosses within that period is the large end's ARRIVAL, which rests on SOURCE (358, reading (a)): reported
     here under reading (c), not decided.
     [Item 387: M ruled position 2's own sigma, ours at 218's destination, so reading (a) holds: no junction, and the
     open period is at most 4 clocks (READ, an order). Reading (b) is kept as written.]
     [Item 388: reading (a) covers only destinations at our sigma. For a destination with its own sigma2, the junction
     on position 2's face is sigma - sigma2, and (b)'s formula holds with that jump (junction_own G1-G3, G7).]
  L5 (deduced) The rows.  CLOSE at the large end, on M-ENERGY-STAYS: our face closes by Hawking emission over the large
     hole's life, at least 2.4 N clocks (L3), its energy ours, radiated into our universe; position 2's face closes
     within its open period (L4), on either reading of position 2's tension.  E1u and E1x: E stays (336), carried by
     the hole through its life and radiated (L3); E2u and E2x: position 2's release at its face's closing (L4), its own
     energy (110, 111 (a), 240).

What this does not claim.
  - The grey-body factors themselves: L3 bounds the power from above, so the life from below; the life is longer.
  - The bulk gravitons' and the CFT's emission beyond the estimate and the reading of Figueras and Wiseman's result.
  - The README's crossing at the large end (ARRIVAL, SOURCE's) or the quantum region's form (273).
  - The interior (O1b, O1c; interior_large/).

Imports close_small.py, m1_large.py, o3_write.py by path.  Stdlib + sympy.
python3 close_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((336, "I think it is B"), (336, "M-ENERGY-STAYS"),
         (356, "I still see a lot, including items that rest on M1 and B4d"),
         (358, "Once everything that doesn't rely on SOURCE is resolved and green"), (360, "I agree. Option 1 please"))
FW_READ = ("a remarkable conjecture has been made in [9, 10] that static black holes can not exist in RSII for radius "
           "much greater than the AdS length",
           "the conjecture is based on applying free field theory intuition to the CFT, which is strongly coupled",
           "We construct large RSII static black holes with radius up to")
N_EX = 2742570311524972
Z_SM = sp.Rational(10875, 100)
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def l1():
    cs = _load("close_small.py", "cl_cs")
    return dict(in4=cs.vaidya(4, "in"), out4=cs.vaidya(4, "out"))


def l2():
    ml = _load("m1_large.py", "cl_ml")
    o1, o2, o4 = ml.m1(), ml.m2(), ml.m4()
    M = sp.Symbol("M", positive=True)
    k2 = o4["k2"]
    if MUT.get("extremal"):
        k2 = sp.Integer(0)                                        # the mutant: our face read as extremal
    # the plane's stress, -sigma gamma, on a null vector along the plane: T k k = -sigma gamma(k, k) = 0
    sig = sp.Symbol("sigma", positive=True)
    k = sp.Matrix([1, 1, 0, 0]); gam = sp.diag(-1, 1, 1, 1)
    Tkk = (k.T * (-sig * gam) * k)[0, 0] if not MUT.get("plane_nec") else -sig
    return dict(k2=k2, kappa_ok=sp.simplify(k2 - 1 / (16 * M ** 2)) == 0, bulk_null=o1["null"], Tkk=sp.simplify(Tkk),
                kink=o2["K_is_gamma"])


def l3():
    """the life's lower bound: Z blackbody species through 27 pi M^2; in clocks of GM/c^3"""
    M, Nn = sp.symbols("M N", positive=True)
    Z = Z_SM
    T = 1 / (8 * sp.pi * M)
    sigma_abs = 27 * sp.pi * M ** 2 if not MUT.get("horizon_area") else 4 * sp.pi * (2 * M) ** 2 / 4
    P = Z * sp.pi ** 2 / 120 * T ** 4 * 4 * sigma_abs
    alpha = sp.simplify(P * M ** 2)
    ow = _load("o3_write.py", "cl_ow")
    M2 = ow.m_squared().subs(sp.Symbol("N", positive=True), Nn)
    life_clocks = sp.simplify(M2 / (3 * alpha))                    # (M^3 / 3 alpha) / M
    per_N = float(life_clocks / Nn)
    floor_expr = ow.t_min(3).subs(ow.Z, Z)
    floor_ex = float(floor_expr.subs(ow.N, N_EX))
    life_ex = per_N * N_EX
    # the narrowest controlled corner: r0 = 10 ell at ell = 22.4 l_P; N = pi r0^2 / (ln2 l_P^2)
    N_c = math.pi * (10 * 22.4) ** 2 / math.log(2)
    floor_c = float(floor_expr.subs(ow.N, N_c))
    M_ex = math.sqrt(N_EX * math.log(2) / (4 * math.pi))
    T_GeV = 1.220890e19 / (8 * math.pi * M_ex)
    kk = (1 / (40 * math.pi)) ** 2
    return dict(alpha=alpha, per_N=per_N, life_ex=life_ex, floor_ex=floor_ex, ratio_ex=life_ex / floor_ex, N_c=N_c,
                ratio_c=per_N * N_c / floor_c, T_GeV=T_GeV, kk=kk)


def seen_over_E(end):
    """position 2's face, 139 (1)'s quarter: the junction seen over the plane's horizon sphere, per E~ E (e^Dtau - 1)"""
    G, ell, r, G5 = sp.symbols("G ell r G5", positive=True)
    sigma = 3 / (4 * sp.pi * G * ell ** 2)
    if end == "small":
        area, inv_kappa, E = 4 * sp.pi * r ** 2, r, 3 * sp.pi * r ** 2 / (8 * G * ell)      # G5 = G ell
    else:
        area, inv_kappa, E = 4 * sp.pi * r ** 2, 2 * r, r / (2 * G)
        if MUT.get("kappa_small"):
            inv_kappa = r                                        # the mutant: the small end's 1/kappa at the large
    return {k: sp.simplify(area * inv_kappa * mu * sigma / E) for k, mu in (("own", sp.Rational(5, 4)),
                                                                         ("side", sp.Rational(1, 2)))}, (r, ell)


def l4():
    small, (r, ell) = seen_over_E("small")
    large, _ = seen_over_E("large")
    x = sp.Symbol("x", positive=True)                            # x = ell / r0
    period = {k: sp.log(1 + 1 / (v.subs(r, ell / x))) for k, v in large.items()}
    at10 = {k: float(v.subs(x, sp.Rational(1, 10))) for k, v in period.items()}
    cj = _load("c_junction.py", "cl_cj")
    small_t = cj.example(cj.seen())["t_full"]
    return dict(small=small, large=large, at10=at10, clocks10=4 * at10["own"], small_t=small_t, short=4)


def compute():
    return dict(l1=l1(), l2=l2(), l3=l3(), l4=l4())


def report(o):
    print("close_large.py -- CLOSE at the large end, and E1u, E1x, E2u, E2x (item 356)\n")
    a = o["l1"]
    print("L1 the plane's 4D forms: ingoing G_vv = %s, outgoing G_uu = %s" % (a["in4"]["G00"], a["out4"]["G00"]))
    b = o["l2"]
    print("L2 kappa^2 = %s (non-degenerate: %s); bulk null energy %s; the plane's T(k, k) = %s" % (
        b["k2"], b["kappa_ok"], b["bulk_null"], b["Tkk"]))
    c = o["l3"]
    print("L3 alpha = %s; life >= %.4f N clocks: %.3g at the example README, %.3g x the write's floor %.2f; at the "
          "corner N = %.3g, %.3g x; T = %.3g GeV; bulk gravitons <= %.2g" % (c["alpha"], c["per_N"], c["life_ex"],
                                                                           c["ratio_ex"], c["floor_ex"], c["N_c"],
                                                                           c["ratio_c"], c["T_GeV"], c["kk"]))
    d = o["l4"]
    print("L4 seen/E~E per (e^Dtau - 1): small end %s; large end %s (own) and %s (side); open at r0 = 10 ell: %.3g "
          "e-folds (%.3g clocks), %.3g on the side total; small end %.1f clocks; reading (a) <= %d clocks" % (
              d["small"]["own"], d["large"]["own"], d["large"]["side"], d["at10"]["own"], d["clocks10"],
              d["at10"]["side"], d["small_t"], d["short"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("L0 336 (with M-ENERGY-STAYS), 356, 358 and 360 verbatim, each inside its own item",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    a = o["l1"]
    m = sp.Function("mu")
    v, u, r = sp.symbols("v u r")
    add("L1 the plane's ingoing G_vv = 2 m'/r^2 and outgoing G_uu = -2 m'/r^2 (imported)",
        sp.simplify(a["in4"]["G00"] - 2 * sp.Derivative(m(v), v) / r ** 2) == 0
        and sp.simplify(a["out4"]["G00"] + 2 * sp.Derivative(m(u), u) / r ** 2) == 0)
    b = o["l2"]
    add("L2 our face non-degenerate, kappa^2 = 1/(16 M^2); null energy zero in the bulk and on the plane: future outer, "
        "it cannot shrink under classical matter", b["kappa_ok"] and b["bulk_null"] == 0 and b["Tkk"] == 0
        and b["kink"])
    c = o["l3"]
    add("L3 the life at least 2.417 N clocks, 6.63e15 at the example README, 3.3e10 x the write's floor; 6.5e3 x at "
        "the controlled corner; the bulk gravitons <= 6.3e-5; Figueras-Wiseman's words READ",
        "%.4f" % c["per_N"] == "2.4173" and "%.3g" % c["life_ex"] == "6.63e+15" and "%.2g" % c["ratio_ex"] == "3.3e+10"
        and "%.2g" % c["ratio_c"] == "6.5e+03" and "%.2g" % c["kk"] == "6.3e-05" and "%.2f" % c["floor_ex"] ==
        "199702.19" and FW_READ[0].startswith("a remarkable"))
    d = o["l4"]
    r_, ell = sp.symbols("r ell", positive=True)
    add("L4 the junction seen at the small end (10/pi)(r_h/ell), reproduced; at the large end 15 (r0/ell)^2 (own) and "
        "6 (r0/ell)^2 (side): open <= 6.7e-4 e-folds = 2.7e-3 clocks at r0 = 10 ell (1.7e-3 on the side total); "
        "reading (a) <= 4 clocks",
        sp.simplify(d["small"]["own"] - 10 / sp.pi * r_ / ell) == 0
        and sp.simplify(d["large"]["own"] - 15 * r_ ** 2 / ell ** 2) == 0
        and sp.simplify(d["large"]["side"] - 6 * r_ ** 2 / ell ** 2) == 0 and "%.2g" % d["at10"]["own"] == "0.00067"
        and "%.2g" % d["clocks10"] == "0.0027" and "%.2g" % d["at10"]["side"] == "0.0017"
        and "%.1f" % d["small_t"] == "33.6")
    return res


MUTANTS = {"extremal": "our face read as extremal, kappa = 0, Hayward's outer law escaped (L2)",
           "plane_nec": "the plane's tension read as violating the null energy condition along it (L2)",
           "horizon_area": "the capture cross-section taken as a quarter of the horizon's area (L3)",
           "kappa_small": "the small end's 1/kappa = r carried to the large end (L4)"}


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
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-13s %-76s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
