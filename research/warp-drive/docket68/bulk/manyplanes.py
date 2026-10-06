#!/usr/bin/env python3
"""manyplanes.py -- DOCKET 68, M-RULINGS items 123-124: infinitely many spacetime planes in a closed dimension, as the
bulk's layers (A) and as separate sheets (B), both.  Deduced and computed; not verified; not seated.  Write-up:
MANYPLANES.md.

M's words (verbatim in the rulings file): item 123 "by closed I mean every plausibility, possibility, eventuality,
every position infinitely possible as a closed dimension." and "A second plane exists. In a closed infinite multiverse
dimension, there are infinite spacetime planes"; item 124 "Both A and B" -- (A) every position of the extra dimension
is a spacetime plane, the bulk's own layers; (B) separate sheets at distinct positions, each with its own matter.

THE TOOL.  The null-contracted Gauss-Codazzi-Ricci identity in Gaussian normal coordinates (K = (1/2) d_y g),
    R5_mn = R4_mn - d_y K_mn + 2 K_ma K^a_n - K K_mn,
checked here exactly for any metric -A dt^2 + B dr^2 + C dOmega^2 + dy^2 with A, B, C arbitrary functions of (r, y)
(sympy; the flipped quadratic sign fails -- control).  It is Maartens gr-qc/0312059v2 eq. 3.9 p.9 (READ by
closedbulk.py's verifier).  In a bulk of vacuum energy R5_mn = -4 a^2 g_mn, so for each layer's own light-like k,
R5_kk = 0 and the layer's reading of its spacetime is R4_kk = d_y K_kk - 2 (K K)_kk + K K_kk.

WHAT THE WORK FINDS
  (A) THE LAYERS.  On closedbulk.py's bulk (series through y^4):
    A1 THE CORRIDOR IS ON EVERY NEARBY LAYER.  Every coefficient of A/A0 and B/B0 through y^4 is finite and its
       denominator nonzero at the throat r = r0 and at the horizon r = 2m: each layer has the throat at r0 and the
       horizon at 2m, to this order.
    A2 EVERY NEARBY LAYER READS THE PASSAGE NEGATIVE.  Each layer's own reading along its own radial light ray is
       L(y) = G_kk (1 + 4a y) + L_2 y^2 + ... (the 4a is the warp's rescaling of the layer's light-cone normalization);
       integrated along the layer's whole passage (m = 1, r0 = 1.8, a = 1): -1.914712 - 3.829424 y - 3.467761 y^2 E/m --
       each term negative; the warp alone would give -1.914712 (1 + 2y + 2y^2), the rest is the plane's curvature.
       Contrast: a Schwarzschild plane's layers read 0 at every order.
    A3 (STRUCTURAL, from closedbulk.py B1 and umbilic.py U3) only our layer is umbilic: on layer y, K_kk = y G_kk + ...,
       so a ray along a nearby layer feels d^2y/dlambda^2 = K_kk < 0 for y > 0 (and > 0 for y < 0 under H-Z2): drawn
       toward our plane.
  (B) THE SHEETS.  At a sheet the bulk's K jumps by the sheet's matter (Israel; standard, NOT READ here):
       [K_mn] = -kappa^2 (tau_mn - (tau/3) h_mn).  Around a closed dimension the jumps and the smooth change of K add to
       zero, so for any fixed vector k (exact, from the identity; H-CONVERGES for an infinite closed dimension):
           kappa^2 SUM_sheets (tau - (tau/3) h)_kk  =  CLOSED-INTEGRAL dy [ R4_kk - R5_kk + 2 (K K)_kk - K K_kk ].
       At our plane the integrand is the corridor's reading, G_kk (STRUCTURAL: R5_kk = 0 and K = -a q there).  So every
       sheet's matter, summed over all of them, is fixed by every layer's reading, summed over the whole closed
       dimension -- the totality's one ledger.  If our plane is the only sheet with anything in the light-like direction
       (its tension drops out: h_kk = 0 for its k), the layers around the closed dimension integrate to exactly zero
       against our corridor's contribution: what our plane reads as negative, the rest of the closed dimension reads as
       positive, in total exactly (derived).  This is the board's reading of M's item 120 ("matter is neither created
       nor destroyed, it only changes geometric state") in this setting, not M's words.
  SCOPE.  A1-A2 are closedbulk.py's near-plane series (H-NEAR-PLANE).  The sum rule is exact given the identity and a
  closed dimension; which sheets exist, where, and what they carry is not computed.

NAMED HYPOTHESES
  M's: H-CLOSED-AS-TOTALITY, H-SECOND-PLANE-EXISTS, H-INFINITE-PLANES, H-NEC-NEVER-VIOLATED (123); H-PLANES-AS-LAYERS,
    H-PLANES-AS-SHEETS (124); H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120).
  The board's: closedbulk.py's H-VACUUM-BULK, H-Z2, H-NEAR-PLANE, H-OUR-TENSION; H-BK-CORRIDOR; H-ISRAEL (the junction
    at a sheet, no mirror at a generic sheet); H-CONVERGES (the closed integral exists in an infinite dimension).

USAGE
    python3 manyplanes.py | --selftest | --json      (sympy, mpmath; about two minutes)
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


def compute():
    import sympy as sp
    o = owners()
    cb = o["closedbulk"]
    E = cb.field_equations()
    a, x = E["a"], E["x"]
    P, (m, r0, L_) = cb.planes()
    bk = cb.build(*P["bk"], order=4)
    sch = cb.build(*P["schwarzschild"], order=4)
    ratios = [sp.together(sp.cancel(c / cl[0])) for cl in bk["coeffs"][:2] for c in cl[1:]]
    persist = all(sp.simplify(sp.denom(rt).subs(x, pt)) != 0 for rt in ratios for pt in (r0, 2 * m))
    L, s = layer_reading(bk["coeffs"], 3)
    Ls, _ = layer_reading(sch["coeffs"], 3)
    gkk = -2 * (2 * r0 - 3 * m) / (x * (2 * x - 3 * m) ** 2)
    passage = layer_passage(L, s, m, r0, a, x)
    ident = identity_check(1)
    ident_flip = identity_check(-1)
    return {"throat_horizon_persist": persist, "L0_minus_gkk": str(sp.simplify(L[0] - gkk)),
            "L1_over_gkk": str(sp.simplify(L[1] / gkk)), "L2": str(sp.factor(L[2])),
            "schwarzschild_layers": [str(c) for c in Ls], "layer_passage_coeffs": passage,
            "anec_plane": 2 * o["coin"].anec_closed(1.0, 1.8),
            "identity": ident, "identity_flipped": ident_flip}


def report(d):
    print("manyplanes.py -- items 123-124: the planes as layers (A) and as sheets (B)")
    print("  (A) throat at r0 and horizon at 2m on every nearby layer (through y^4): %s" % d["throat_horizon_persist"])
    print("      each layer's reading: L0 - G_kk = %s;  L1 / G_kk = %s" % (d["L0_minus_gkk"], d["L1_over_gkk"]))
    c = d["layer_passage_coeffs"]
    print("      each layer's passage (m = 1, r0 = 1.8, a = 1): %.6f + %.6f y + %.6f y^2 E/m" % tuple(c))
    for y in (0.05, 0.1, 0.2):
        print("        y = %.2f: %.6f" % (y, c[0] + c[1] * y + c[2] * y * y))
    print("  (B) the identity R5 = R4 - d_y K + 2KK - K K, every diagonal component: %s (flipped sign: %s)" % (
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

    c = d["layer_passage_coeffs"]
    chk("A1: every coefficient of A/A0 and B/B0 through y^4 is finite at the throat r0 and the horizon 2m -- the "
        "corridor is on every nearby layer, to this order", d["throat_horizon_persist"])
    chk("A2: each layer's own reading is L(y) = G_kk (1 + 4a y) + O(y^2) (L0 - G_kk = %s, L1/G_kk = %s)" % (
        d["L0_minus_gkk"], d["L1_over_gkk"]), d["L0_minus_gkk"] == "0" and d["L1_over_gkk"] == "4*a")
    chk("A2: integrated along each layer's whole passage: %.6f + %.6f y + %.6f y^2 E/m -- every term negative, the y^0 "
        "term our plane's %.6f, the y^1 term the warp's 2a" % (c[0], c[1], c[2], d["anec_plane"]),
        all(v < 0 for v in c) and abs(c[0] - d["anec_plane"]) < 1e-9 and abs(c[1] / c[0] - 2) < 1e-9)
    chk("a Schwarzschild plane's layers read 0 at every order computed (%s)" % d["schwarzschild_layers"],
        all(v == "0" for v in d["schwarzschild_layers"]), contrast=True)
    chk("(B) the identity R5_mn = R4_mn - d_y K_mn + 2 K_ma K^a_n - K K_mn holds exactly for arbitrary A, B, C (%s)" %
        d["identity"], all(v == "0" for v in d["identity"]))
    chk("the identity with the quadratic sign flipped fails", any(v != "0" for v in d["identity_flipped"]), ctl=True)
    structural.append("A2: y^2 of the layer passage over y^0 = %.4f; the warp alone gives 2 -- the rest is the plane's "
                      "curvature (a = 1, m = 1 units)" % (c[2] / c[0]))
    structural.append("A3: only our layer is umbilic; on layer y, K_kk = y G_kk + ..., so a ray along a nearby layer is "
                      "drawn toward our plane (closedbulk.py B1, umbilic.py U3)")
    structural.append("(B) the sum rule: kappa^2 SUM_sheets (tau - (tau/3) h)_kk = closed integral of [R4_kk - R5_kk + "
                      "2 (KK)_kk - K K_kk] dy, for any fixed k -- the identity plus a closed dimension (H-ISRAEL, "
                      "H-CONVERGES)")
    structural.append("(B) at our plane the integrand is G_kk (R5_kk = 0 by construction, K = -a q, q_kk = 0); with no "
                      "other sheet carrying anything along k, the closed integral is exactly zero against it")
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
