#!/usr/bin/env python3
"""closedbulk.py -- DOCKET 68, M-RULINGS items 120-121: building the bulk (BULK5-O1) under The Method's closed-index
criteria, self-referencing and self-defending.  Deduced, computed and READ; not verified; not seated.  Write-up:
CLOSEDBULK.md.

M's words (verbatim in the rulings file): item 120 "yes. Science has already taught us that matter is neither created
nor destroyed, it only changes geometric state." (H-COMPLETE-BULK); item 121 "yes. And we build it under closed index
criteria, self referencing and self defending" (H-BULK-CLOSED-INDEX).

THE CRITERIA, READ (method/members/The_Method_1_6-2.md): P1 "a complete index is self-referencing", R(L) = L; P2 "a
complete index is self-defending", D = dim q - rank dPhi/dp >= 1; sec. 16.1 "Each is a test the index must pass";
sec. 16.4 "D_def is realised iff a quantity is reachable by two disjoint paths, and the defence is the DISAGREEMENT
between them"; sec. 15.5 "R(X) = X recovers alphabet and bounds for any closed index".  THE BOARD'S TRANSLATION to a
five-dimensional spacetime (named, not READ):
  H-SELFREF-AS-DETERMINED  self-referencing = the bulk is rebuilt from the plane's own data alone (its metric q, and its
                           extrinsic curvature K fixed by tau = 0 and the tension: K = -a q, escape.py S3) with no input
                           from outside it, and reads back to the plane.
  H-SELFDEF-AS-CONSTRAINTS self-defending = the surplus: the bulk's field equations are more than its unknowns.  At each
                           order in the distance y off the plane, three evolution equations (tt, rr, theta-theta) fix
                           the three new coefficients; two constraint equations (yy, ry) are then a second, disjoint
                           path that must agree.  D = 2 per order.  The contracted Bianchi identity is why they can.
  H-CLOSED-AS-COMPACT      closed = the extra dimension closes on itself with no boundary (Randall-Sundrum's S^1/Z2,
                           H-RS1): a second plane at y = y_c, with no outside to supply data.  Used in B3 only.

THE CONSTRUCTION.  Gaussian normal coordinates off the plane: ds^2 = -A dt^2 + B dr^2 + C dOmega^2 + dy^2, a bulk of
vacuum energy only (G_AB = 6 a^2 g_AB, a = 1/l), each of A, B, C a power series in y whose y^0 term is Bronnikov-Kim's
eq. (17) (gr-qc/0212112v1 p.4, READ in plane.py) and whose y^1 term is -2a times it (K = (1/2) d_y g = -a q).

WHAT THE WORK FINDS
  B1 SELF-REFERENCING.  Every coefficient through y^N is fixed uniquely by the plane's (m, r0) and a: no free function,
     no outside datum (sympy).  The bulk reads the plane's own violation back: every term beyond the warp e^{-2ay}
     carries the factor (2 r0 - 3m) -- the same factor as the plane's G_kk (coin.py C1) -- and the first y-derivative of
     the bulk's null extrinsic curvature IS the plane's reading: K_kk = y G_kk + O(y^2).
  B2 SELF-DEFENDING.  The two constraint equations vanish identically at every order computed: the evolution path and
     the constraint path agree.  Controls (the defence catching a wrong index): a plane with R != 0
     (Schwarzschild-de Sitter) fails the yy constraint at y^0 (-2 Lambda); a wrong tension (K = -2a q) fails it; a
     deliberately mis-stated y^2 coefficient fails it at y^1 -- "the check caught the check" (sec. 16.4).  Contrast: a
     Schwarzschild plane builds the pure warp, every correction zero (the black string; computed here, not READ).
  B3 CLOSED (under H-CLOSED-AS-COMPACT).  Flat planes: the closed bulk forces the second plane's tension to be exactly
     minus the first's (computed: K = -a h at every y).  With the corridor on our plane, the second plane's matter obeys
     tau2_kk = (2/kappa^2) K_kk(y_c) = (2/kappa^2)[y_c G_kk + O(y_c^2)], so along a whole null geodesic its ANEC integral
     is (2/kappa^2) y_c x (-1.914712 E/m) at leading order (m = 1, r0 = 1.8): NEGATIVE.  A bending of the second plane
     y_c -> y_c + eps(x) adds -k k grad grad eps = -d^2 eps/dlambda^2, a total derivative, to first order: it cannot
     remove the integral.  So in a closed bulk of vacuum energy, what our plane reads as geometry the other plane must
     carry as matter that breaks the averaged NEC -- the price moves to the other side (pairing.py's reading of Chung-
     Freese found the same move for a different warp).  Bulk matter keeping the NEC makes it worse, not better (derived, for the
     verifier): the null-contracted Gauss equation at the plane gives d_y K_kk = R4_kk - R5_kk (the quadratic terms
     vanish there, K = -a q and q_kk = 0), and R5_kk >= 0.  This is against H-NEC-COIN in the compact reading with a vacuum
     bulk; item 82: it is the boundary, and its escapes are named (CLOSEDBULK.md).
     To second order K_kk = G_kk (y + 5a y^2): the y^2 term is the warp's and has the same sign (computed).
  SCOPE.  The series is local: A's first term beyond the warp is m (2 r0 - 3m) y^2/(r^2 (2r - 3m)^2), of order (y/r0)^2
     near the throat, so it is trusted only for y << r0 (H-NEAR-PLANE).  For the README's corridor r0 ~ 1e-27 m, far inside any Randall-Sundrum y_c.  The global bulk, and
     whether the sign of B3 survives beyond leading order, are OPEN.

NAMED HYPOTHESES
  M's: H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120); H-BULK-CLOSED-INDEX (121); H-NEC-COIN (117, a metaphor, 120).
  The board's: H-SELFREF-AS-DETERMINED, H-SELFDEF-AS-CONSTRAINTS, H-CLOSED-AS-COMPACT (above); H-BK-CORRIDOR; H-RS1;
    H-VACUUM-BULK (G_AB = 6 a^2 g_AB, the RS fine tuning Lambda_4 = 0); H-Z2 (the orbifold mirror at each plane);
    H-NEAR-PLANE (the series' scope); H-PLANE-READING.

USAGE
    python3 closedbulk.py | --selftest | --json  [--order N]   (sympy; order 3 under a minute, order 5 ~10 min)
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
ORDER = 3                      # series through y^ORDER; constraints checked at y^0 .. y^(ORDER-2); --order N deeper
_CACHE = {}
_EQ = {}


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
    """Imported, never copied: pairing.py (the 5D Einstein tensor), coin.py (the plane's ANEC integral, closed form),
    escape.py (S3: K = -a q with tau = 0)."""
    if not _CACHE:
        _CACHE["pairing"] = _load(os.path.join(HERE, "pairing.py"), "d68_pairing_closedbulk")
        _CACHE["coin"] = _load(os.path.join(D68, "copy", "coin.py"), "copy_coin_closedbulk")
        _CACHE["escape"] = _load(os.path.join(HERE, "escape.py"), "d68_escape_closedbulk")
    return _CACHE


def field_equations():
    """G^M_N - 6 a^2 delta^M_N for ds^2 = -A dt^2 + B dr^2 + C dOmega^2 + dy^2, A, B, C functions of (r, y); pairing.py's
    coordinates (t, x, y, z, u) are read as (t, r, theta, phi, y)."""
    import sympy as sp
    if not _EQ:
        Af, Bf, Cf = sp.Function("A"), sp.Function("B"), sp.Function("C")

        def metric(t, x, th, ph, u):
            return sp.diag(-Af(x, u), Bf(x, u), Cf(x, u), Cf(x, u) * sp.sin(th) ** 2, 1)
        with contextlib.redirect_stdout(io.StringIO()):
            Gmix, _, X = owners()["pairing"].einstein_mixed(metric)
        a = sp.Symbol("a", positive=True)
        x, u = X[1], X[4]
        _EQ.update(x=x, u=u, a=a, fns=(Af(x, u), Bf(x, u), Cf(x, u)),
                   evo=[Gmix[i, i] - 6 * a ** 2 for i in (0, 1, 2)],
                   con={"yy": Gmix[4, 4] - 6 * a ** 2, "ry": Gmix[4, 1]})
    return _EQ


def build(A0, B0, C0, order=ORDER, a1=None, poke=None):
    """The bulk off a plane (A0, B0, C0 functions of x = r): first-order terms -2 a1 times the plane (a1 = a unless
    testing a wrong tension); each higher coefficient solved from the evolution equations; then the constraints
    expanded.  poke = (k, delta): add delta * A0 to A's y^k coefficient after solving (the mis-stated coefficient)."""
    import sympy as sp
    E = field_equations()
    x, u, a = E["x"], E["u"], E["a"]
    a1 = a if a1 is None else a1
    cs = [[A0, -2 * a1 * A0], [B0, -2 * a1 * B0], [C0, -2 * a1 * C0]]
    unique = True
    for n in range(order - 1):
        unk = sp.symbols("uA uB uC")
        sub = {f: sum(c * u ** i for i, c in enumerate(cl)) + w * u ** (n + 2) for f, cl, w in zip(E["fns"], cs, unk)}
        eqs = [sp.simplify(sp.diff(e.subs(sub).doit(), u, n).subs(u, 0) / sp.factorial(n)) for e in E["evo"]]
        sols = sp.solve(eqs, unk, dict=True)
        unique = unique and len(sols) == 1 and all(w in sols[0] for w in unk)
        for cl, w in zip(cs, unk):
            cl.append(sp.simplify(sols[0][w]))
    if poke:
        cs[0][poke[0]] = cs[0][poke[0]] + poke[1] * A0
    sub = {f: sum(c * u ** i for i, c in enumerate(cl)) for f, cl in zip(E["fns"], cs)}
    con = {}
    for name, e in E["con"].items():
        es = e.subs(sub).doit()
        con[name] = [sp.simplify(sp.diff(es, u, n).subs(u, 0) / sp.factorial(n)) for n in range(order - 1)]
    return {"coeffs": cs, "constraints": con, "unique": unique}


def planes():
    import sympy as sp
    E = field_equations()
    r = E["x"]
    m, r0, L = sp.symbols("m r0 Lambda", positive=True)
    f = 1 - 2 * m / r
    fl = 1 - 2 * m / r - L * r ** 2 / 3
    return {"bk": (f, (1 - sp.Rational(3, 2) * m / r) / (f * (1 - r0 / r)), r ** 2),
            "schwarzschild": (f, 1 / f, r ** 2), "sds": (fl, 1 / fl, r ** 2), "flat": (1, 1, r ** 2)}, (m, r0, L)


def kkk_series(res, nmax=3):
    """K_kk = (E^2 / 2A)(d_y B / B - d_y A / A) for the radial null direction of the induced metric at y, E = 1."""
    import sympy as sp
    E = field_equations()
    u = E["u"]
    A, B = [sum(c * u ** i for i, c in enumerate(cl)) for cl in res["coeffs"][:2]]
    s = sp.series((sp.diff(B, u) / B - sp.diff(A, u) / A) / (2 * A), u, 0, nmax).removeO()
    return [sp.simplify(s.coeff(u, i)) for i in range(nmax)]


def compute(order=None):
    import sympy as sp
    order = order or ORDER
    E = field_equations()
    a, r, u = E["a"], E["x"], E["u"]
    P, (m, r0, L) = planes()
    bk = build(*P["bk"], order=order)
    sch = build(*P["schwarzschild"], order=order)
    sds = build(*P["sds"], order=2)
    wrong = build(*P["bk"], order=2, a1=2 * a)
    poked = build(*P["bk"], order=3, poke=(2, sp.Symbol("delta", positive=True)))
    flat = build(*P["flat"], order=3)
    A0 = P["bk"][0]
    expo = lambda cl, base: [sp.simplify(c / base - (-2 * a) ** i / sp.factorial(i)) for i, c in enumerate(cl)]
    bk_dev = [expo(cl, base) for cl, base in zip(bk["coeffs"], P["bk"])]
    sch_dev = [expo(cl, base) for cl, base in zip(sch["coeffs"], P["schwarzschild"])]
    flat_dev = [expo(cl, base) for cl, base in zip(flat["coeffs"], P["flat"])]
    free = set().union(*[sp.sympify(c).free_symbols for cl in bk["coeffs"] for c in cl]) - {m, r0, a, r}
    factor_ok = all(sp.simplify(d.subs(r0, sp.Rational(3, 2) * m)) == 0 for dl in bk_dev for d in dl[2:])
    kk = kkk_series(bk)
    comb = -2 * (2 * r0 - 3 * m) * (r - 2 * m) / (r ** 2 * (2 * r - 3 * m) ** 2)
    gkk_plane = comb / A0                                        # coin.py's G_kk at E = 1
    o = owners()
    anec_passage = 2 * o["coin"].anec_closed(1.0, 1.8)
    num = {m: 1, r0: sp.Rational(9, 5)}
    dev2 = bk_dev[0][2]                                          # A's y^2 term beyond the warp, over A0
    reach = {str(rr): float(1 / sp.sqrt(abs(dev2.subs(num).subs(r, rr)))) for rr in (sp.Rational(37, 20), 2, 3)}
    k2_over_k1 = sp.simplify(kk[2] / kk[1])
    return {"order": order, "bk_dev_A": [str(sp.factor(d)) for d in bk_dev[0]],
            "bk_constraints": {k: [str(v) for v in vl] for k, vl in bk["constraints"].items()},
            "bk_unique": bk["unique"], "bk_free_symbols": sorted(str(s) for s in free), "factor_2r0_3m": factor_ok,
            "sch_dev_zero": all(sp.simplify(d) == 0 for dl in sch_dev for d in dl),
            "sch_constraints_zero": all(v == 0 for vl in sch["constraints"].values() for v in vl),
            "sds_yy": [str(v) for v in sds["constraints"]["yy"]],
            "wrong_tension_yy": [str(sp.factor(v)) for v in wrong["constraints"]["yy"]],
            "poked_yy": [str(sp.factor(v)) for v in poked["constraints"]["yy"]],
            "poked_ry": [str(sp.factor(v)) for v in poked["constraints"]["ry"]],
            "flat_dev_zero": all(sp.simplify(d) == 0 for dl in flat_dev for d in dl),
            "kkk": [str(sp.factor(c)) for c in kk], "kkk_y1_is_gkk": sp.simplify(kk[1] - gkk_plane) == 0,
            "kkk_y0": str(kk[0]), "anec_plane_passage_m1_r1p8": anec_passage,
            "plane2_anec_leading_per_yc": anec_passage, "kkk_y2_over_y1": str(k2_over_k1),
            "kkk_y2_same_sign": sp.simplify(k2_over_k1 - 5 * a) == 0, "reach_y_at_r": reach,
            "escape_K": "K = -a q" in open(os.path.join(HERE, "escape.py"), encoding="utf-8").read()}


def report(d):
    print("closedbulk.py -- items 120-121: the bulk built under closed-index criteria (series through y^%d)" % d["order"])
    print("  A's coefficients beyond the warp e^{-2ay} (divided by the plane's A):")
    for i, s in enumerate(d["bk_dev_A"]):
        print("    y^%d: %s" % (i, s))
    print("  constraints (yy, ry) at y^0 .. y^%d: %s" % (d["order"] - 2, d["bk_constraints"]))
    print("  K_kk off the plane: %s (y^1 term = the plane's G_kk: %s)" % (d["kkk"], d["kkk_y1_is_gkk"]))
    print("  second plane (closed reading): ANEC of its matter = (2/kappa^2) y_c x %.6f E/m at leading order"
          % d["plane2_anec_leading_per_yc"])
    print("  K_kk's y^2 term over its y^1 term: %s;  the series' reach 1/sqrt|A_2 dev| at r = %s: %s" % (
        d["kkk_y2_over_y1"], list(d["reach_y_at_r"]), [round(v, 3) for v in d["reach_y_at_r"].values()]))


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

    con = d["bk_constraints"]
    chk("B1: every coefficient through y^%d is fixed uniquely by the plane (m, r0) and a -- no free function, no "
        "outside datum (free symbols beyond them: %s)" % (d["order"], d["bk_free_symbols"]),
        d["bk_unique"] and d["bk_free_symbols"] == [])
    chk("B1: every term beyond the warp carries the plane's own factor (2 r0 - 3m): all vanish at r0 = 3m/2",
        d["factor_2r0_3m"])
    chk("B1: the bulk's null extrinsic curvature is K_kk = y G_kk + O(y^2) -- its first y-derivative is the plane's "
        "reading (coin.py's G_kk), and K_kk = %s on the plane" % d["kkk_y0"], d["kkk_y1_is_gkk"] and d["kkk_y0"] == "0")
    chk("B2: both constraints vanish at every order computed, y^0 .. y^%d (%s) -- the evolution path and the "
        "constraint path agree" % (d["order"] - 2, con), all(v == "0" for vl in con.values() for v in vl))
    chk("a plane with R != 0 (Schwarzschild-de Sitter) fails the yy constraint: %s" % d["sds_yy"],
        d["sds_yy"][0] != "0", ctl=True)
    chk("a wrong tension (K = -2a q) fails the yy constraint: %s" % d["wrong_tension_yy"],
        d["wrong_tension_yy"][0] != "0", ctl=True)
    chk("a mis-stated y^2 coefficient (A_2 + delta A_0) fails a constraint at y^1 (yy %s; ry %s) -- the check catches "
        "the check" % (d["poked_yy"], d["poked_ry"]), d["poked_yy"][1] != "0" or d["poked_ry"][1] != "0", ctl=True)
    chk("a Schwarzschild plane builds the pure warp e^{-2ay}: every correction zero, constraints zero (the black "
        "string)", d["sch_dev_zero"] and d["sch_constraints_zero"], contrast=True)
    chk("B3: flat planes -- K = -a h at every y, so the closed bulk's second plane has tension exactly minus the first's",
        d["flat_dev_zero"])
    chk("B3: the second plane's matter has ANEC (2/kappa^2) y_c x %.6f E/m < 0 at leading order (coin.py's closed form "
        "for the plane's passage, m = 1, r0 = 1.8)" % d["plane2_anec_leading_per_yc"], d["plane2_anec_leading_per_yc"] < 0)
    chk("B3: K_kk = G_kk (y + 5a y^2) + O(y^3) (y^2/y^1 = %s): the second order has the same sign, so it does not "
        "reverse the second plane's reading locally" % d["kkk_y2_over_y1"], d["kkk_y2_same_sign"])
    structural.append("B1: restricted to y = 0 the built bulk returns the plane exactly (by construction)")
    structural.append("B2: D = 2 per order -- five independent field equations (tt, rr, theta-theta, yy, ry; phi-phi "
                      "repeats theta-theta) against three new coefficients; the contracted Bianchi identity is why the "
                      "two surplus equations can agree")
    structural.append("B3: a bending eps(x) of the second plane adds -d^2 eps/dlambda^2 along each null geodesic to first "
                      "order, a total derivative, so it cannot change the ANEC integral (standard identity)")
    structural.append("B3: the junction tau2 - (tau2/3) h = (2/kappa^2)(K(y_c) + a h) with the Z2 mirror (H-Z2); its "
                      "null part is tau2_kk = (2/kappa^2) K_kk(y_c)")
    structural.append("scope: A's y^2 term beyond the warp is m (2 r0 - 3m)/(r^2 (2r - 3m)^2) y^2, so the series reaches "
                      "y ~ %s at r = 1.85, 2, 3 (m = 1, r0 = 1.8; units of m) -- trusted only for y << r0 "
                      "(H-NEAR-PLANE); the plane's own scale enters K_kk at y^3" %
                      [round(v, 3) for v in d["reach_y_at_r"].values()])
    structural.append("escape.py's S3 states K = -a q (string found: %s) -- the y^1 terms" % d["escape_K"])
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("closedbulk.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    order = int(argv[argv.index("--order") + 1]) if "--order" in argv else None
    d = compute(order)
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
