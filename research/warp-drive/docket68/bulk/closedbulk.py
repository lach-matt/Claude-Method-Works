#!/usr/bin/env python3
"""closedbulk.py -- DOCKET 68, M-RULINGS items 120-124: building the bulk (BULK5-O1) under The Method's closed-index
criteria, self-referencing and self-defending.  Deduced, computed and READ; verified once; not seated.  Write-up:
CLOSEDBULK.md.  First headed "M-RULINGS items 120-121 ... not verified".

M's words (verbatim in the rulings file): item 120 "yes. Science has already taught us that matter is neither created
nor destroyed, it only changes geometric state." (H-COMPLETE-BULK); item 121 "yes. And we build it under closed index
criteria, self referencing and self defending" (H-BULK-CLOSED-INDEX); item 123 "by closed I mean every plausibility,
possibility, eventuality, every position infinitely possible as a closed dimension" (H-CLOSED-AS-TOTALITY) and "A
second plane exists. In a closed infinite multiverse dimension, there are infinite spacetime planes"; item 124 "Both A
and B" (the planes as the bulk's layers, and as separate sheets: manyplanes.py builds both).

THE CRITERIA, READ (method/members/The_Method_1_6-2.md): P1 "a complete index is self-referencing", R(L) = L; P2 "a
complete index is self-defending", D = dim q - rank dPhi/dp >= 1; sec. 16.1 "Each is a test the index must pass";
sec. 16.2 "D = D_phys + D_def, physical relations and definitional identities"; sec. 16.4 "D_def is realised iff a
quantity is reachable by two disjoint paths, and the defence is the DISAGREEMENT between them"; sec. 15.5 "R(X) = X
recovers alphabet and bounds for any closed index, relative to a given order"; and what "closed" means there (the
claim, before Part I): "An index that is *closed* -- closed under the meet and join of its own coordinates" and "A
closed index is a fixed point of R".  The principle "allow continued expansions": "sec. 16.4-form constraints
preserve closure".
THE BOARD'S TRANSLATION to a five-dimensional spacetime (named, not READ):
  H-SELFREF-AS-DETERMINED  self-referencing = the bulk's series is fixed by the plane's own data and reads back to it.
                           The inputs are named: the plane's metric q; K = -a q (tau = 0 and the tension, escape.py S3);
                           a; H-VACUUM-BULK; H-Z2; the Gaussian-normal gauge.  A unique formal series is not a bulk:
                           "Evolution off the timelike brane in the spacelike normal direction does not in general
                           constitute a well-defined initial value problem" (Maartens gr-qc/0312059v2 p.11, READ by the
                           verifier through alphaXiv).
  H-SELFDEF-AS-CONSTRAINTS self-defending = The Method's split, sec. 16.2.  D_phys = 1: at y^0 the yy constraint reads
                           -R4/2, so the plane must have R = 0 (Bronnikov-Kim p.2: "R = 0 is an immediate consequence of
                           (1)") -- the one physical relation, which both data controls test.  D_def = 2 per order
                           >= 1: once the evolution equations and the y^0 constraints hold, the contracted Bianchi
                           identity forces both constraints at every later order -- they must agree, and checking that
                           they do catches a wrong derivation (sec. 16.4), which the mis-stated-coefficient control
                           shows.  (ry at y^0 is empty for any K proportional to q.)  This moves the board's defence
                           from the identity itself (paper/CLAIMS.md H20: "**\"Self-defending\" is exact, and it is the
                           contracted Bianchi identity.**") to the constraints the identity ties -- the board's change.
                           First written "D = 2 per order ... The contracted Bianchi identity is why they can": "can"
                           was "must", and 5 - 3 is an equation count, not The Method's rank.
  H-CLOSED-AS-COMPACT      WITHDRAWN as a reading of M (item 123) and without warrant in The Method, whose "closed"
                           is a fixed point of R.  It read closed as a dimension looping back with a second plane
                           (Randall-Sundrum's S^1/Z2).  B3 below is kept as computed for that two-plane case only.

THE CONSTRUCTION.  Gaussian normal coordinates off the plane: ds^2 = -A dt^2 + B dr^2 + C dOmega^2 + dy^2, a bulk of
vacuum energy only (G_AB = 6 a^2 g_AB, a = 1/l), each of A, B, C a power series in y whose y^0 term is Bronnikov-Kim's
eq. (17) (gr-qc/0212112v1 p.4, READ in plane.py; r0 = 1.8m is a horizon member -- BK p.4: a wormhole "for any r0 > 2m")
and whose y^1 term is -2a times it (K = (1/2) d_y g = -a q; a > 0 is positive tension, H-OUR-TENSION).

WHAT THE WORK FINDS
  B1 SELF-REFERENCING.  The series through y^N is fixed by the plane and the named inputs (STRUCTURAL: the formal
     Cauchy problem; a wrong plane is fixed uniquely too).  It agrees with the standard vacuum-brane expansion
     (Maartens eq. 4.6 p.20: g(x,y) = g(x,0) - E y^2 - (2/l) E |y|^3 + ...; eq. 4.1 p.19: R = -E; READ by the verifier),
     the plane's E carrying Bronnikov-Kim's factor (2 r0 - 3m) (BK eq. 18, p.4).  The bulk's null extrinsic curvature
     starts as the plane's reading: K_kk = G_kk (y + 5a y^2 + ...), and to first order in the plane's curvature it
     resums to K_kk = G_kk (e^{6ay} - e^{4ay})/(2a) (the verifier's derivation; checked here through y^3, where the
     remainder is second order in the plane's curvature, m and r0 scaled together; first tested in (2 r0 - 3m) alone, a
     wrong test, since the remainder carries m (2 r0 - 3m)) -- positive factor for y > 0 on either sign of the tension.
  B2 SELF-DEFENDING.  Both constraints vanish at every order computed (y^0 .. y^2 by default; y^0 .. y^3 with --order 5).
     Controls: a plane with R != 0 (Schwarzschild-de Sitter) fails yy at y^0 (-2 Lambda); a wrong tension (K = -2a q)
     fails it (18 a^2) -- D_phys; a mis-stated y^2 coefficient fails at y^1 -- D_def, "The check caught the check."
     (sec. 16.4).  Contrast: a Schwarzschild plane builds the pure warp, the black string (Maartens eqs. 4.2-4.5 p.19).
  B3 TWO PLANES (the board's former compact reading, not M's construction).  Flat planes: the second plane's tension is
     minus the first's through y^3 (exactly: RS hep-ph/9905221v1 eq. 11 p.3 "V_hid = -V_vis = 24M^3 k"; Gibbons-Kallosh-
     Linde hep-th/0011225v2 eq. 3.1 p.6, READ by the verifier).  With the corridor, tau2_kk = (2/kappa^2) K_kk(y_c) < 0
     AT EVERY POINT for every member with 2 r0 > 3m (G_kk < 0 everywhere; the resummed factor > 0), so along a whole null
     geodesic its ANEC integral is (2/kappa^2) y_c (-1.914712 E/m) at leading order (m = 1, r0 = 1.8).  A bend
     y_c -> y_c + eps adds integral (eps G_kk - eps'') dlambda to first order in eps: the eps'' part is a total
     derivative (eps' -> 0 at both ends) and eps G_kk has G_kk's sign with y_c + eps > 0 -- the sign survives.  Bulk matter
     keeping the NEC, AT THE PLANE, makes it worse: d_y K_kk = R4_kk - R5_kk at y = 0 (Maartens eq. 3.9 p.9; checked
     generically in manyplanes.py), R5_kk >= 0; reversing it needs R5_kk < G_kk < 0, a bulk NEC violation larger than
     the plane's reading.  Same move in the literature: Binetruy-Deffayet-Langlois hep-th/9905012v2 p.11-12 ("Hence the
     matter on one brane is constrained by the matter on the other"; READ by the verifier); pairing.py's Chung-Freese.
     Placement: in RS1 our atoms sit on the negative-tension plane (BULK.md P-SCALE); with K = +a q the constraints still
     vanish and K_kk = G_kk (y - 5a y^2 + ...), the resummed factor (e^{-4ay} - e^{-6ay})/(2a) still positive (computed).
  SCOPE.  A's first term beyond the warp is -m (2 r0 - 3m) y^2/(r^2 (2r - 3m)^2) (first written without the minus): the
     series needs y << r0, and -- at linear order the deformation grows like e^{4ay} (the black string's curvature,
     Maartens eq. 4.5 p.19) -- also e^{2ay} << 2a r0 (the verifier's estimate; H-NEAR-PLANE).  With the board's RS1
     values (1/k = 9.9e-35 m, SEARCHES.md; k r_c = 11.0, BULK.md) y_c = 3.42e-33 m is 8.6e-6 of the README corridor's r0
     ~ r_min = 3.98e-28 m (CHAIN.md), but a y_c = 34.6 against ln(2 a r0)/2 = 7.95: B3 does NOT reach an RS1-sized y_c.
     First written "For the README's corridor r0 ~ 1e-27 m, far inside any Randall-Sundrum y_c" -- backwards.

NAMED HYPOTHESES
  M's: H-COMPLETE-BULK, H-CONSERVATION-AS-GEOMETRY (120); H-BULK-CLOSED-INDEX (121); H-CLOSED-AS-TOTALITY,
    H-SECOND-PLANE-EXISTS, H-INFINITE-PLANES, H-NEC-NEVER-VIOLATED (123, from 117 and 120); H-PLANES-AS-LAYERS,
    H-PLANES-AS-SHEETS (124).  The coin metaphor is retired (123).
  The board's: H-SELFREF-AS-DETERMINED, H-SELFDEF-AS-CONSTRAINTS (above); H-CLOSED-AS-COMPACT (withdrawn, B3 only);
    H-BK-CORRIDOR; H-RS1; H-VACUUM-BULK (G_AB = 6 a^2 g_AB, the RS fine tuning Lambda_4 = 0); H-Z2 (the orbifold mirror at
    each plane); H-OUR-TENSION (our plane at positive tension; RS1 places our atoms at negative); H-NEAR-PLANE;
    H-PLANE-READING.

USAGE
    python3 closedbulk.py | --selftest | --json  [--order N]   (sympy; order 4 about two minutes; order 5 took 34 min
    under load)
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
ORDER = 4                      # series through y^ORDER; constraints checked at y^0 .. y^(ORDER-2); --order N deeper
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
    """K_kk = (E^2 / 2A)(d_y B / B - d_y A / A) for the radial null direction of the induced metric at y, E = 1, as a
    truncated power series in y (term-by-term arithmetic, each coefficient simplified on its own)."""
    import sympy as sp

    def norm(cl):                                     # coefficients of A / A0
        return [sp.cancel(c / cl[0]) for c in cl[:nmax + 1]]

    def logder(p):                                    # q with p' = q p, p_0 = 1
        q = []
        for n in range(nmax):
            q.append(sp.cancel((n + 1) * p[n + 1] - sum(q[k] * p[n - k] for k in range(n))))
        return q

    def inv(p):                                       # 1 / p, p_0 = 1
        w = [sp.Integer(1)]
        for n in range(1, nmax):
            w.append(sp.cancel(-sum(p[k] * w[n - k] for k in range(1, n + 1))))
        return w
    pa, pb = norm(res["coeffs"][0]), norm(res["coeffs"][1])
    d = [sp.cancel(x - y) for x, y in zip(logder(pb), logder(pa))]
    ia = inv(pa)
    A0 = res["coeffs"][0][0]
    return [sp.simplify(sum(d[k] * ia[n - k] for k in range(n + 1)) / (2 * A0)) for n in range(nmax)]


# Restated with their sources, for the scope lines only (never recomputed here):
R_MIN_COEFF = 7.59185111e-36          # m per sqrt(bit), chain.py (CHAIN.md)
N_README = 2.742570e15                # bits, the core README (CHAIN.md)
INV_K_RS1 = 9.9e-35                   # m, SEARCHES.md (1/k)
K_RC_RS1 = 11.0                       # BULK.md (k r_c)


def compute(order=None):
    import math
    import sympy as sp
    order = order or ORDER
    E = field_equations()
    a, r = E["a"], E["x"]
    P, (m, r0, L) = planes()
    bk = build(*P["bk"], order=order)
    sch = build(*P["schwarzschild"], order=order)
    sds = build(*P["sds"], order=2)
    wrong = build(*P["bk"], order=2, a1=2 * a)
    poked = build(*P["bk"], order=3, poke=(2, sp.Symbol("delta", positive=True)))
    flat = build(*P["flat"], order=order)
    neg = build(*P["bk"], order=3, a1=-a)
    expo = lambda cl, base, s=1: [sp.simplify(c / base - (-2 * s * a) ** i / sp.factorial(i)) for i, c in enumerate(cl)]
    bk_dev = [expo(cl, base) for cl, base in zip(bk["coeffs"], P["bk"])]
    sch_dev = [expo(cl, base) for cl, base in zip(sch["coeffs"], P["schwarzschild"])]
    flat_dev = [expo(cl, base) for cl, base in zip(flat["coeffs"], P["flat"])]
    free = set().union(*[sp.sympify(c).free_symbols for cl in bk["coeffs"] for c in cl]) - {m, r0, a, r}
    factor_ok = all(sp.simplify(d.subs(r0, sp.Rational(3, 2) * m)) == 0 for dl in bk_dev for d in dl[2:])
    nk = min(order, 4)
    kk = kkk_series(bk, nk)
    kn = kkk_series(neg, 3)
    comb = -2 * (2 * r0 - 3 * m) * (r - 2 * m) / (r ** 2 * (2 * r - 3 * m) ** 2)
    gkk_plane = comb / P["bk"][0]
    resum = [sp.Integer(0), sp.Integer(1), 5 * a, sp.Rational(38, 3) * a ** 2]
    resum_ok = all(sp.simplify(kk[i] - resum[i] * kk[1]) == 0 for i in range(1, min(nk, 3)))
    rem3 = None
    if nk >= 4:
        rem = sp.simplify(kk[3] - resum[3] * kk[1])
        lam = sp.Symbol("lam", positive=True)                # the plane's curvature scaled: m, r0 -> lam m, lam r0
        rem3 = sp.simplify(sp.series(rem.subs({m: lam * m, r0: lam * r0}), lam, 0, 2).removeO())
    gkk_shape = sp.simplify(kk[1] * r * (2 * r - 3 * m) ** 2 / (2 * r0 - 3 * m))
    anec_passage = 2 * owners()["coin"].anec_closed(1.0, 1.8)
    num = {m: 1, r0: sp.Rational(9, 5)}
    dev2 = bk_dev[0][2]
    reach = {str(rr): float(1 / sp.sqrt(abs(dev2.subs(num).subs(r, rr)))) for rr in (sp.Rational(37, 20), 2, 3)}
    r_min = R_MIN_COEFF * math.sqrt(N_README)
    y_c = K_RC_RS1 * math.pi * INV_K_RS1
    return {"order": order, "bk_dev_A": [str(sp.factor(d)) for d in bk_dev[0]],
            "bk_constraints": {k: [str(v) for v in vl] for k, vl in bk["constraints"].items()},
            "bk_unique": bk["unique"], "bk_free_symbols": sorted(str(s) for s in free), "factor_2r0_3m": factor_ok,
            "sch_dev_zero": all(sp.simplify(d) == 0 for dl in sch_dev for d in dl),
            "sch_constraints_zero": all(v == 0 for vl in sch["constraints"].values() for v in vl),
            "sds_yy": [str(v) for v in sds["constraints"]["yy"]], "sds_ry": [str(v) for v in sds["constraints"]["ry"]],
            "wrong_tension_yy": [str(sp.factor(v)) for v in wrong["constraints"]["yy"]],
            "poked_yy": [str(sp.factor(v)) for v in poked["constraints"]["yy"]],
            "poked_ry": [str(sp.factor(v)) for v in poked["constraints"]["ry"]],
            "flat_dev_zero": all(sp.simplify(d) == 0 for dl in flat_dev for d in dl),
            "kkk": [str(sp.factor(c)) for c in kk], "kkk_y1_is_gkk": sp.simplify(kk[1] - gkk_plane) == 0,
            "kkk_y0": str(kk[0]), "resummed_through": min(nk, 3) - 1, "resummed_ok": resum_ok,
            "y3_remainder_lam1": None if rem3 is None else str(rem3),
            "gkk_shape": str(gkk_shape),
            "neg_constraints_zero": all(v == 0 for vl in neg["constraints"].values() for v in vl),
            "neg_kkk_y2_over_y1": str(sp.simplify(kn[2] / kn[1])),
            "anec_plane_passage_m1_r1p8": anec_passage, "reach_y_at_r": reach,
            "r_min_m": r_min, "y_c_rs1_m": y_c, "yc_over_rmin": y_c / r_min, "a_yc": y_c / INV_K_RS1,
            "linear_limit_a_y": math.log(2 * r_min / INV_K_RS1) / 2,
            "escape_K": "K = -a q" in open(os.path.join(HERE, "escape.py"), encoding="utf-8").read()}


def report(d):
    print("closedbulk.py -- items 120-124: the bulk built under closed-index criteria (series through y^%d)" % d["order"])
    print("  A's coefficients beyond the warp e^{-2ay} (divided by the plane's A):")
    for i, s in enumerate(d["bk_dev_A"]):
        print("    y^%d: %s" % (i, s))
    print("  constraints (yy, ry) at y^0 .. y^%d: %s" % (d["order"] - 2, d["bk_constraints"]))
    print("  K_kk off the plane: %s" % d["kkk"])
    print("  resummed G_kk (e^{6ay} - e^{4ay})/(2a) matches through y^%d: %s; y^3 remainder through lam^1: %s" % (
        d["resummed_through"], d["resummed_ok"], d["y3_remainder_lam1"]))
    print("  negative-tension placement: constraints zero %s; K_kk y^2/y^1 = %s" % (
        d["neg_constraints_zero"], d["neg_kkk_y2_over_y1"]))
    print("  two planes (former reading): ANEC of the second plane's matter = (2/kappa^2) y_c x %.6f E/m, leading order"
          % d["anec_plane_passage_m1_r1p8"])
    print("  scope: reach 1/sqrt|A_2 dev| at r = %s: %s;  RS1 y_c = %.3e m = %.2e r_min, a y_c = %.1f against %.2f" % (
        list(d["reach_y_at_r"]), [round(v, 3) for v in d["reach_y_at_r"].values()], d["y_c_rs1_m"],
        d["yc_over_rmin"], d["a_yc"], d["linear_limit_a_y"]))


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
    chk("B1: K_kk = y G_kk + O(y^2) off the plane -- its first y-derivative is the plane's reading (coin.py's G_kk), "
        "and K_kk = %s on the plane" % d["kkk_y0"], d["kkk_y1_is_gkk"] and d["kkk_y0"] == "0")
    if d["y3_remainder_lam1"] is not None:
        chk("B1: K_kk matches the resummed G_kk (e^{6ay} - e^{4ay})/(2a) through y^%d, and at y^3 the remainder is "
            "second order in the plane's curvature (m, r0 -> lam m, lam r0; through lam^1: %s)" % (
                d["resummed_through"], d["y3_remainder_lam1"]),
            d["resummed_ok"] and d["y3_remainder_lam1"] == "0")
    chk("B2: both constraints vanish at every order computed, y^0 .. y^%d (%s)" % (d["order"] - 2, con),
        all(v == "0" for vl in con.values() for v in vl))
    chk("D_phys: a plane with R != 0 (Schwarzschild-de Sitter) fails the yy constraint: %s" % d["sds_yy"],
        d["sds_yy"][0] != "0", ctl=True)
    chk("D_phys: a wrong tension (K = -2a q) fails the yy constraint: %s" % d["wrong_tension_yy"],
        d["wrong_tension_yy"][0] != "0", ctl=True)
    chk("D_def: a mis-stated y^2 coefficient (A_2 + delta A_0) fails a constraint at y^1 (yy %s; ry %s) -- 'The check "
        "caught the check.'" % (d["poked_yy"], d["poked_ry"]), d["poked_yy"][1] != "0" or d["poked_ry"][1] != "0",
        ctl=True)
    chk("a Schwarzschild plane builds the pure warp e^{-2ay}: every correction zero, constraints zero (the black string, "
        "Maartens eqs. 4.2-4.5 p.19)", d["sch_dev_zero"] and d["sch_constraints_zero"], contrast=True)
    chk("placement (H-OUR-TENSION): with K = +a q (RS1's visible plane) the constraints still vanish and K_kk's "
        "y^2/y^1 = %s, the resummed form with a -> -a" % d["neg_kkk_y2_over_y1"],
        d["neg_constraints_zero"] and d["neg_kkk_y2_over_y1"] == "-5*a")
    chk("B3 (two planes): flat planes -- K = -a h through y^%d, so the second plane's tension is minus the first's" %
        d["order"], d["flat_dev_zero"])
    chk("B3 (two planes): G_kk = -2 (2 r0 - 3m)/(r (2r - 3m)^2) (shape %s), negative at every r > r0 for every member "
        "with 2 r0 > 3m -- the second plane's matter breaks the NEC pointwise; its ANEC (2/kappa^2) y_c x %.6f E/m" % (
            d["gkk_shape"], d["anec_plane_passage_m1_r1p8"]),
        d["gkk_shape"] == "-2" and d["anec_plane_passage_m1_r1p8"] < 0)
    structural.append("B1: every coefficient through y^%d is fixed uniquely (free symbols beyond m, r0, a, r: %s) -- the "
                      "formal Cauchy problem; a wrong plane is fixed uniquely too, so this has no control" % (
                          d["order"], d["bk_free_symbols"]))
    structural.append("B1: every term beyond the warp vanishes at r0 = 3m/2 (%s) -- the Schwarzschild contrast restated "
                      "(BK p.4: Schwarzschild 'is restored from (17) in the special case r0 = 3m/2')" % d["factor_2r0_3m"])
    structural.append("B1: restricted to y = 0 the built bulk returns the plane exactly (by construction)")
    structural.append("B2: ry at y^0 is empty for any K proportional to q (SdS ry: %s); D_phys = 1 (yy at y^0 = -R4/2); "
                      "D_def = 2 per order >= 1, forced by the contracted Bianchi identity" % d["sds_ry"])
    structural.append("B3: a bend eps adds integral (eps G_kk - eps'') dlambda to first order in eps; eps'' integrates to "
                      "zero (eps' -> 0 at both ends) and eps G_kk keeps G_kk's sign while y_c + eps > 0")
    structural.append("B3: the junction tau2 - (tau2/3) h = (2/kappa^2)(K(y_c) + a h) with the Z2 mirror (H-Z2); its "
                      "null part is tau2_kk = (2/kappa^2) K_kk(y_c)")
    structural.append("scope: A's y^2 term beyond the warp is -m (2 r0 - 3m)/(r^2 (2r - 3m)^2); reach y ~ %s at r = "
                      "1.85, 2, 3 (m = 1, r0 = 1.8)" % [round(v, 3) for v in d["reach_y_at_r"].values()])
    structural.append("scope: RS1 y_c = %.3e m (k r_c pi / k), %.2e of r_min = %.4e m; a y_c = %.1f against the linear "
                      "limit ln(2 a r0)/2 = %.2f (r0 ~ r_min): B3 does not reach an RS1-sized y_c (restated inputs)" % (
                          d["y_c_rs1_m"], d["yc_over_rmin"], d["r_min_m"], d["a_yc"], d["linear_limit_a_y"]))
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
