#!/usr/bin/env python3
"""manyplanes.py -- DOCKET 68, M-RULINGS items 123-128: infinitely many spacetime planes in a closed dimension, as the
bulk's layers (A) and as separate sheets (B), both.  Deduced, computed and READ; verified once; not seated.  Write-up:
MANYPLANES.md.  First headed "items 123-124 ... not verified".

M's words (verbatim in the rulings file): item 123 "by closed I mean every plausibility, possibility, eventuality,
every position infinitely possible as a closed dimension." and "A second plane exists. In a closed infinite multiverse
dimension, there are infinite spacetime planes"; item 124 "Both A and B"; item 125 M-EXACT-VALUES (no general
coefficients); item 126 the corridor uses "the shortest distance needed"; item 127 "1 - yes" (the planes coincide) and
H-COEFF-FROM-CURRENT (a coefficient = its current value + the counterfactual difference).

THE TOOL.  R5_mn = R4_mn - d_y K_mn + 2 K_ma K^a_n - K K_mn (K = (1/2) d_y g, lower indices), checked exactly for any
metric -A dt^2 + B dr^2 + C dOmega^2 + dy^2, A, B, C arbitrary functions of (r, y) (sympy; the flipped quadratic sign
fails -- control).  Maartens gr-qc/0312059v2 eq. 3.9 p.9 (READ by the verifiers).  In a vacuum bulk R5_kk = 0 along each
layer's own light rays, so a layer reads R4_kk = d_y K_kk - 2 (K K)_kk + K K_kk.

WHAT THE WORK FINDS
  (A) THE LAYERS (closedbulk.py's bulk through y^4; H-NEAR-PLANE).
    A1 Every coefficient of A/A0, B/B0 and C/C0 through y^4 has poles only at r = 0 and r = 3m/2 (STRUCTURAL: it cannot
       fail for r0 != 3m/2, no control): on each nearby layer A vanishes at 2m (the horizon) and B keeps its 1/(r - r0)
       pole with C regular (the areal-radius minimum, the throat, at r0), to O(y^4).  First counted, A and B only.
    A2 Each layer's own reading along its own radial light ray, exactly: L(y) = G_kk (1 + 4a y) + [8 a^2 G_kk + R2] y^2
       + ..., the 4a and 8a^2 the warp's rescaling of each layer's light cone, R2 independent of a and carrying
       (2 r0 - 3m) -- the layers' own departure from the warp (Maartens' -E y^2, the bulk's response to the plane's Weyl
       curvature).  Integrated along each layer's passage: I0 + I1 y + I2 y^2 with I1 = 2a I0 and I2 = 2 a^2 I0 + J2,
       J2 = the integral of R2, POSITIVE -- the first computed sign of the layers turning toward positive.
       At the README's exact m (current.py) with r0 = 3m/2 + Delta, I0 and J2 are printed across Delta from the current
       state outward; the bulk scale a = k stays a coefficient off our plane (asked of M).  First written at the
       illustrative member m = 1, r0 = 1.8, a = 1 (-1.914712 - 3.829424 y - 3.467761 y^2 E/m, "each term negative") --
       general coefficients (item 125), and "each term negative" held only for a m > 0.3073.
    A3 (STRUCTURAL, H-NEAR-PLANE, first order, G_kk < 0) on layer y, K_kk = y G_kk + ...: a ray along a nearby layer is
       drawn toward our plane.
  (B) THE SHEETS.  The junction at a sheet: Maartens eq. 3.17 p.9, "K+ - K- = -kappa5^2(T^brane - (1/3) T^brane g)"
     (READ by the verifier; first cited as "standard, NOT READ").  For a fixed coordinate vector k, the identity gives
     d_y(K_kk) = R4_kk - R5_kk + 2 (KK)_kk - K K_kk between sheets.  On an open dimension -- M's item 128: no loop,
     "A genuine loop would me creating a paradox of transition from position 1 to position 1" -- the ledger keeps its
     ends: kappa^2 SUM_sheets (tau - (tau/3) h)_kk = INTEGRAL d_y(K_kk) dy (smooth part) - [K_kk(far) - K_kk(near)]
     (STRUCTURAL).  Nothing forces the bending to turn positive anywhere; the ends can carry it.  The integrand is
     d_y K_kk for a fixed k; it equals G_kk only at our plane.  Our plane's null jump is zero, tension included; another
     sheet's tension enters through h_kk(y_i).  A sheet keeping the NEC makes K_kk jump down.  First written with a loop
     (H-CLOSED-AS-LOOP, H-GN-GLOBAL -- the board's, put in so the integral would close; GKL hep-th/0011225v2 p.4's
     compact "closed") and "d_y K_kk ... must be positive somewhere": withdrawn by item 128.  H-Z2 is dropped for (B).
     First written: "every sheet's matter ... is fixed by every layer's reading" and "the layers around the closed
     dimension integrate to exactly zero against our corridor's contribution" -- our plane is one layer, of zero measure.
  WITH ITEM 127 (the planes coincide).  The second plane occupies our plane's place.  What that does is not computed:
     two sheets at one place have no bulk gap, so their junction is not closedbulk.py's B3, and the board's
     opposite-tension sheets at one place fail the bulk's yy constraint unless k = 0 (current.py X4).  First written
     "its null matter is zero ... and the corridor's readings on our plane need no k" -- withdrawn.

NAMED HYPOTHESES
  M's: H-CLOSED-AS-TOTALITY, H-SECOND-PLANE-EXISTS, H-INFINITE-PLANES, H-NEC-NEVER-VIOLATED (123); H-PLANES-AS-LAYERS,
    H-PLANES-AS-SHEETS (124); M-EXACT-VALUES (125); H-SHORTEST-DISTANCE, H-COLOCATED-REALIZATION (126);
    H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120).
  The board's: closedbulk.py's H-VACUUM-BULK, H-NEAR-PLANE, H-OUR-TENSION, H-Z2 (for (A) only); H-BK-CORRIDOR;
    H-CLOSED-AS-LOOP, H-GN-GLOBAL (withdrawn, item 128); current.py's H-CURRENT-IS-SCHWARZSCHILD.

USAGE
    python3 manyplanes.py | --selftest | --json      (sympy, mpmath; about three minutes)
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
    passage integral)."""
    if not _CACHE:
        _CACHE["closedbulk"] = _load(os.path.join(HERE, "closedbulk.py"), "d68_closedbulk_manyplanes")
        _CACHE["pairing"] = _CACHE["closedbulk"].owners()["pairing"]
        _CACHE["coin"] = _CACHE["closedbulk"].owners()["coin"]
    return _CACHE


def identity_check(sign=1):
    """R5_mn - [R4_mn - d_y K_mn + sign (2 K_ma K^a_n - K K_mn)] for each diagonal component, A, B, C arbitrary."""
    import sympy as sp
    E = owners()["closedbulk"].field_equations()
    x, u = E["x"], E["u"]
    Af, Bf, Cf = sp.Function("A"), sp.Function("B"), sp.Function("C")

    def metric(t, xx, th, ph, uu):
        return sp.diag(-Af(xx, uu), Bf(xx, uu), Cf(xx, uu), Cf(xx, uu) * sp.sin(th) ** 2, 1)
    if "ric5" not in _CACHE:
        with contextlib.redirect_stdout(io.StringIO()):
            _, ric5, X = owners()["pairing"].einstein_mixed(metric)
        _CACHE["ric5"], _CACHE["X"] = ric5, X
    ric5, X = _CACHE["ric5"], _CACHE["X"]
    t, th = X[0], X[2]
    h = sp.diag(-Af(x, u), Bf(x, u), Cf(x, u), Cf(x, u) * sp.sin(th) ** 2)
    X4 = [t, x, th, X[3]]
    hi = sp.diag(*[1 / h[i, i] for i in range(4)])
    n = 4
    gam = [[[sum(hi[a_, d] * (sp.diff(h[d, b_], X4[c]) + sp.diff(h[d, c], X4[b_]) - sp.diff(h[b_, c], X4[d]))
                 for d in range(n)) / 2 for c in range(n)] for b_ in range(n)] for a_ in range(n)]
    R4 = [sp.simplify(sum(sp.diff(gam[a_][b_][b_], X4[a_]) - sp.diff(gam[a_][b_][a_], X4[b_])
                          + sum(gam[a_][a_][d] * gam[d][b_][b_] - gam[a_][b_][d] * gam[d][b_][a_] for d in range(n))
                          for a_ in range(n))) for b_ in range(n)]
    K = sp.diff(h, u) / 2
    Km = hi * K
    trK = sum(Km[i, i] for i in range(4))
    return [str(sp.simplify(ric5[i, i] - (R4[i] - sp.diff(K[i, i], u) + sign * (2 * (K * Km)[i, i] - trK * K[i, i]))))
            for i in range(4)]


def layer_reading(cs, nterms=3):
    """Each layer's own R4_kk along its own radial light ray (k^t = 1/A(y), E = 1), as a power series in y, from
    R4_kk = d_y K_kk - 2 (K K)_kk + K K_kk (vacuum bulk), by term-by-term series arithmetic; also sqrt(A B / A0 B0)."""
    import sympy as sp
    n = nterms + 1
    A0 = cs[0][0]
    P = [[sp.cancel(c / cl[0]) for c in cl[:n + 1]] for cl in cs]

    def mul(p, q, k):
        return [sp.cancel(sum(p[j] * q[i - j] for j in range(i + 1))) for i in range(k)]

    def inv(p, k):
        w = [sp.Integer(1)]
        for i in range(1, k):
            w.append(sp.cancel(-sum(p[j] * w[i - j] for j in range(1, i + 1))))
        return w

    def der(p):
        return [(i + 1) * p[i + 1] for i in range(len(p) - 1)]

    def sqrt_ser(p, k):
        s = [sp.Integer(1)]
        for i in range(1, k):
            s.append(sp.cancel((p[i] - sum(s[j] * s[i - j] for j in range(1, i))) / 2))
        return s
    lA, lB, lC = [mul(der(p), inv(p, n), n) for p in P]                  # (ln A)', (ln B)', (ln C)'
    Kt, Kr, Kc = [[c / 2 for c in l] for l in (lA, lB, lC)]             # mixed K^t_t, K^r_r, K^th_th
    trK = [sp.cancel(Kt[i] + Kr[i] + 2 * Kc[i]) for i in range(n)]
    dKt = [sp.cancel(d + e) for d, e in zip(der(Kt), mul(lA, Kt, n - 1))]     # d_y K_tt / (-A)
    dKr = [sp.cancel(d + e) for d, e in zip(der(Kr), mul(lB, Kr, n - 1))]     # d_y K_rr / B
    T_dK = [sp.cancel(-dKt[i] + dKr[i]) for i in range(n - 1)]                # (M_tt / A + M_rr / B), M = d_y K
    T_KK = [sp.cancel(-p + q) for p, q in zip(mul(Kt, Kt, n), mul(Kr, Kr, n))]
    T_K = [sp.cancel(-Kt[i] + Kr[i]) for i in range(n)]
    T_trKK = mul(trK, T_K, n)
    T = [sp.cancel(T_dK[i] - 2 * T_KK[i] + T_trKK[i]) for i in range(n - 1)]
    iA = inv(P[0], n)
    L = [sp.simplify(sum(T[j] * iA[i - j] for j in range(i + 1)) / A0) for i in range(nterms)]
    s = sqrt_ser(mul(P[0], P[1], n), n)
    return L, s


def layer_passage(L, s, m, r0, a, x, vals=(1, 1.8, 1)):
    """Integral along each layer's whole radial passage, coefficient by coefficient in y:
    2 x int dlambda = 2 int 2 sqrt(r - 3m/2) G(r) dw with r = r0 + w^2 (the throat's 1/sqrt(r - r0) cancelled)."""
    import mpmath as mp
    import sympy as sp
    mv, rv, av = vals
    num = {m: mv, r0: sp.nsimplify(rv), a: av}
    mp.mp.dps = 25
    out = []
    for i in range(len(L)):
        G = sp.simplify(sum(L[j] * s[i - j] for j in range(i + 1)))
        f = sp.lambdify(x, G.subs(num), "mpmath")
        R0 = mp.mpf(str(rv))
        out.append(float(2 * mp.quad(lambda w: 2 * mp.sqrt(R0 + w * w - mp.mpf(1.5) * mv) * f(R0 + w * w),
                                     [0, 0.5, 2, 10, mp.inf])))
    return out


FRACTIONS = ("1/1000", "1/100", "1/10", "1/4", "1/2")       # Delta/m, r0 = 3m/2 + Delta (current.py)


def compute():
    import sympy as sp
    o = owners()
    cb = o["closedbulk"]
    E = cb.field_equations()
    a, x = E["a"], E["x"]
    P, (m, r0, L_) = cb.planes()
    bk = cb.build(*P["bk"], order=4)
    sch = cb.build(*P["schwarzschild"], order=4)
    ratios = [sp.together(sp.cancel(c / cl[0])) for cl in bk["coeffs"] for c in cl[1:]]
    poles = set()
    for rt in ratios:
        for fac, _ in sp.factor_list(sp.denom(rt))[1]:
            poles |= {str(z) for z in sp.solve(fac, x)}
    L, s = layer_reading(bk["coeffs"], 3)
    Ls, _ = layer_reading(sch["coeffs"], 3)
    gkk = -2 * (2 * r0 - 3 * m) / (x * (2 * x - 3 * m) ** 2)
    R2 = sp.simplify(L[2] - 8 * a ** 2 * gkk)
    illus = layer_passage(L, s, m, r0, a, x, vals=(1, 1.8, 1))                 # first written, general coefficients
    cur = _load(os.path.join(D68, "copy", "current.py"), "copy_current_manyplanes")
    X = cur.exact_pull()
    mS = float(sp.N(X["m"], 20))
    rows = []
    for f in FRACTIONS:
        fr = float(sp.Rational(f))
        I = layer_passage(L, s, m, r0, a, x, vals=(1, 1.5 + fr, 0))           # a = 0: I0 and J2 (geometric, m = 1)
        rows.append({"frac": f, "I0_SI": I[0] / mS, "J2_SI": I[2] / mS ** 3, "I0_geo": I[0], "J2_geo": I[2],
                     "I0_current_py": 2 * cur.leg(mS, fr)})
    ident = identity_check(1)
    ident_flip = identity_check(-1)
    return {"poles": sorted(poles), "L0_minus_gkk": str(sp.simplify(L[0] - gkk)),
            "L1_over_gkk": str(sp.simplify(L[1] / gkk)), "R2": str(sp.factor(R2)),
            "R2_free_of_a": a not in R2.free_symbols, "R2_vanishes_at_schwarzschild": sp.simplify(
                R2.subs(r0, sp.Rational(3, 2) * m)) == 0,
            "schwarzschild_layers": [str(c) for c in Ls], "illustrative_passage": illus, "m_SI": mS, "rows": rows,
            "anec_plane": 2 * o["coin"].anec_closed(1.0, 1.8), "identity": ident, "identity_flipped": ident_flip}


def report(d):
    print("manyplanes.py -- items 123-127: the planes as layers (A) and as sheets (B)")
    print("  (A) poles of every A, B, C coefficient through y^4: r = %s" % d["poles"])
    print("      each layer's reading: L0 - G_kk = %s;  L1 / G_kk = %s;  L2 = 8a^2 G_kk + R2, R2 = %s" % (
        d["L0_minus_gkk"], d["L1_over_gkk"], d["R2"]))
    print("      README corridor, m = %.14e m, r0 = 3m/2 + Delta (a = k a coefficient off our plane):" % d["m_SI"])
    for row in d["rows"]:
        print("        Delta/m = %-6s I0 = %.10e E/m   J2 = %.10e E/m^3  (I1 = 2k I0, I2 = 2k^2 I0 + J2)" % (
            row["frac"], row["I0_SI"], row["J2_SI"]))
    c = d["illustrative_passage"]
    print("      first written at m = 1, r0 = 1.8, a = 1: %.6f %+.6f y %+.6f y^2" % tuple(c))
    print("  (B) the identity, every diagonal component: %s (flipped sign: %s)" % (
        d["identity"], ["nonzero" if v != "0" else "0" for v in d["identity_flipped"]]))


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

    rows = d["rows"]
    chk("A2: each layer's own reading is L(y) = G_kk (1 + 4a y) + [8a^2 G_kk + R2] y^2 (L0 - G_kk = %s, L1/G_kk = %s), "
        "R2 free of a (%s) and zero for a Schwarzschild plane (%s)" % (
            d["L0_minus_gkk"], d["L1_over_gkk"], d["R2_free_of_a"], d["R2_vanishes_at_schwarzschild"]),
        d["L0_minus_gkk"] == "0" and d["L1_over_gkk"] == "4*a" and d["R2_free_of_a"]
        and d["R2_vanishes_at_schwarzschild"])
    worst = max(abs(row["I0_SI"] / row["I0_current_py"] - 1) for row in rows)
    chk("A2 at the README's exact m: each layer's y^0 passage I0 agrees with current.py's exact closed form at all five "
        "Delta (worst relative %.1e)" % worst, worst < 1e-9, ctl=True)
    chk("A2: J2, the layers' own departure from the warp integrated along the passage, is POSITIVE at every Delta "
        "(%s E/m^3) -- the layers turn toward positive" % [("%.4e" % row["J2_SI"]) for row in rows],
        all(row["J2_SI"] > 0 for row in rows))
    chk("a Schwarzschild plane's layers read 0 at every order computed (%s; exact at every order: the black string, "
        "Maartens p.19 after eq. 4.3)" % d["schwarzschild_layers"],
        all(v == "0" for v in d["schwarzschild_layers"]), contrast=True)
    chk("(B) the identity R5_mn = R4_mn - d_y K_mn + 2 K_ma K^a_n - K K_mn holds exactly for arbitrary A, B, C (%s)" %
        d["identity"], all(v == "0" for v in d["identity"]))
    chk("the identity with the quadratic sign flipped fails", any(v != "0" for v in d["identity_flipped"]), ctl=True)
    structural.append("A1: every A, B, C coefficient through y^4 has poles only at r = %s -- the horizon at 2m and the "
                      "throat (areal minimum, g_rr -> oo) at r0 persist on nearby layers; cannot fail for r0 != 3m/2, "
                      "no control" % d["poles"])
    structural.append("A2 first written at m = 1, r0 = 1.8, a = 1: %.6f %+.6f y %+.6f y^2 E/m (general coefficients, item "
                      "125); 'each term negative' held only for a m > 0.3073" % tuple(d["illustrative_passage"]))
    structural.append("A2: I1 = 2a I0 follows from L1 = 4a G_kk and the layer's affine rescaling -- not counted again")
    structural.append("A3: on layer y, K_kk = y G_kk + ...: a ray along a nearby layer is drawn toward our plane "
                      "(first order, G_kk < 0, H-NEAR-PLANE)")
    structural.append("(B) no loop (M's item 128): kappa^2 SUM (tau - tau h/3)_kk = integral of d_y K_kk (fixed k) - "
                      "[K_kk(far) - K_kk(near)] -- the ends kept; nothing forces d_y K_kk positive anywhere (first "
                      "written with a loop, H-CLOSED-AS-LOOP, withdrawn)")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("manyplanes.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
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
