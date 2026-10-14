#!/usr/bin/env python3
"""core_face.py -- item 420: the two points item 419 left unproved, closed or stated exactly.

M, 420, quoting the board's report after 419 ("What is not proved: the large end's 5D core is crossed with completeness
but its curvature growth is not computed there; the face is traced as static from the arrival's end"): "What is not
proved: - what about these?"  Labels: computed (exact unless marked), deduced, READ, estimate, M's.

Point (2), the face static from v = w on (the verifier's qualification at 348 (Q3)).
  A1 (M's 418; deduced) Whatever crosses our face is README, so the README's arrival ends where crossing ends: mu(v)
     is constant after v = w by definition of w, and the face is the static hole's from there (Birkhoff on the
     symmetric forms; Figueras and Wiseman's static brane hole at the large end, READ in the record).
  A2 (computed) It does not rest on 418 alone.  An arrival that adds mass after v = w (mu' >= 0, README or not) gives
     every outgoing ray dr/dv = f/2 a smaller slope (f falls as mu rises), so by comparison the trapped region only
     grows: the face is born no later, and parts already hidden stay hidden.  Checked on the traces of focusing_parts
     F5.  It does not rescue a slow arrival: 4D order 1 at w = 10, past the threshold 8, the face is still born at the
     onset with half the mass again arriving after (computed).  F5's widths stay the requirement.
  A3 (computed; estimate in the coefficient) The one thing that lowers the mass after v = w is the hole's own Hawking
     flux (negative energy going in, d_evap's record; under 136 G the README's own energy leaving).  With the blackbody
     power hbar c^6/(15360 pi G^2 M^2) (species and greybody factors move it by about tenfold, not included), the face
     moves at |dr_h/dv| = l_P^2/(1920 pi r0^2) and the mass lost over the widest arrival, 8 clocks of r0/c, is
     l_P^2/(240 pi r0^2): 4.4e-66 at r0 = 20 ell, 4.4e-69 at the Earth cap.  Its ingoing flux breaks F4's R_kk >= 0 by
     a part in l_P^2/r0^2 against the focusing term at the face (estimate), and inside by quantum_onset Q2's x.
  So point (2) closes: by 418, and independently by A2 and A3.

Point (1), the large end's 5D core.
  B1 (computed) The onset, x = l5^2 sqrt(K) = 1, on the 5D form with the README's mass, mu5 = (8/(3 pi)) m ell
     (b4d_stage1, m = r0/2), is at r_q = (72 mu5^2 l5^4)^(1/8): 4.27e-15 m at r0 = 20 ell, 1.01e-14 m at the Earth cap,
     r_q/ell = 3.1e-10 and 7.3e-10.  On the 4D form it would be deeper still.  Either way the onset lies far inside
     ell: the core's onset is five-dimensional.
  B2 (computed) Where the 4D stretch hands over to the core, r = ell, x is 1e-38 to 3e-37 on either form: the
     transition region is deeply classical, its curvature finite whatever its exact geometry.
  B3 (computed, exact) The equatorial hypersurface of the 5D form, chi = pi/2, any mu and lam, interior included, has
     zero extrinsic curvature.  So a tensionless Z2 brane through the centre fits it exactly: the mass already at the
     centre (the README's earlier parts) makes exactly the SO(4) field the small end uses (arrival_small V1).  The
     brane alone does not break the symmetric form.  What breaks it is the tension (Israel then needs |K| = 1/ell,
     against the core's 1/r: relative r/ell, about 1e-10 at the onset, estimate) and Lambda5 ((r_q/ell)^2, about 1e-19,
     estimate), both made where the core is -- and the transition region at r ~ ell, where the geometry is neither
     form and differs from both at order one (estimate).
  B4 (computed, exact, on a proxy) How a deviation made at r ~ ell reaches the centre.  Static zonal modes of a massless
     scalar on the 5D form reduce exactly to Legendre's equation in xi = 2 r^2/mu - 1, degree nu = l/2.  A smooth face
     admits only P_nu (Q_nu is logarithmic at xi = 1).  The Z2 keeps the even-l harmonics (C_l^1(cos chi) has parity
     (-1)^l), so nu is an integer and P_nu is a polynomial: finite at the centre, xi = -1.  On the proxy a deviation
     made at r ~ ell neither fades toward the centre (as a locally sourced r/ell correction would) nor grows: it is
     carried in at its own size.  The gravitational modes are not computed, and the transition's deviation is order
     one, beyond any linear statement.
  So point (1) does not close.  The 5D symmetric law 72 mu^2/r^8 holds near the focus up to corrections of 1e-10 made
  there, but the deviation carried in from the transition is of order one and, on the proxy, survives to the centre.
  Point (1) is the open core of item 414 again -- (b2) no inner horizon and (c2) the onset reached at the centre --
  now located: the core r << ell inside the face, entered from a classical transition region.

python3 core_face.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
_C = {}


def _load(name, alias):
    if alias not in _C:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _C[alias] = m
    return _C[alias]


# ---------------------------------------------------------------------------------------------- point (2)
def birth(D, n, w, extra=0.0, w2=None):
    """the face's birth in clocks of r_h/c (negative: before the onset; 0: at it) for the arrival s(v/w) of
    focusing_parts F5, followed by a second arrival adding `extra` of the mass over w2; extra = 0 is face_born"""
    from scipy.integrate import solve_ivp
    FP = _load("focusing_parts.py", "cf_fp")
    w2 = w if w2 is None else w2
    sg = -1.0 if "loss" in MUT else 1.0
    def mu(v):
        if v <= w:
            return FP.smoothstep(n, v / w)
        return 1.0 + sg * extra * FP.smoothstep(n, (v - w) / w2)
    def rhs(v, y):
        r = max(y[0], 1e-100)
        return [0.5 * (1 - mu(v) / r ** (D - 3))]
    vend = w + (w2 if extra else 0.0); rend = (1.0 + sg * extra) ** (1.0 / (D - 3))
    e1, e2 = 1e-5 * w, 1e-8 * w
    r1, r2 = (solve_ivp(rhs, (vend, e), [rend], method="LSODA", rtol=1e-12, atol=1e-16, max_step=w / 20).y[0, -1]
              for e in (e1, e2))
    if r2 <= 0:
        return 0.0
    X = (r1 - r2) / (e1 - e2); r0 = r2 - X * e2
    return -2 * r0 if r0 > 1e-9 else 0.0


def evaporation():
    """A3: the face's rate and the mass lost over 8 clocks, at r0 = 20 ell and at the Earth cap"""
    QO = _load("quantum_onset.py", "cf_qo"); EC = _load("earth_cap.py", "cf_ec")
    o = QO.onset_4d(); lP, ell = o["lP"], o["ell"]
    out = {}
    for name, r0 in (("r0 = 20 ell", 20 * ell), ("the Earth cap", EC.compute()["r0"])):
        rate = lP ** 2 / (1920 * math.pi * r0 ** 2)
        out[name] = dict(r0=r0, rate=rate, lost=8 * rate, flux=lP ** 2 / r0 ** 2)
    return out


# ---------------------------------------------------------------------------------------------- point (1)
def core_scales():
    """B1-B2: the onset on the 5D and 4D forms, and x at r = ell, at r0 = 20 ell and at the Earth cap"""
    QO = _load("quantum_onset.py", "cf_qo"); EC = _load("earth_cap.py", "cf_ec"); B1 = _load("b4d_stage1.py", "cf_b1")
    o = QO.onset_4d(); l5, ell = o["l5"], o["ell"]
    out = {}
    for name, r0 in (("r0 = 20 ell", 20 * ell), ("the Earth cap", EC.compute()["r0"])):
        m = r0 / 2
        mu5 = m ** 2 * B1.hole_radius(ell / m) ** 2                      # r_h^2 = (8/(3 pi)) m ell
        if "mu4" in MUT:
            mu5 = r0 ** 2
        rq5 = (72 * mu5 ** 2 * l5 ** 4) ** (1 / 8); rq4 = (12 * r0 ** 2 * l5 ** 4) ** (1 / 6)
        out[name] = dict(r0=r0, mu5=mu5, rq5=rq5, rq4=rq4, rq_ell=rq5 / ell, lam=(rq5 / ell) ** 2,
                         x5_ell=l5 ** 2 * math.sqrt(72) * mu5 / ell ** 4, x4_ell=l5 ** 2 * math.sqrt(12) * r0 / ell ** 3)
    return out


def equator():
    """B3: the extrinsic curvature of chi = chi0 in -f dt^2 + dr^2/f + r^2 (dchi^2 + sin^2 chi dOmega_2^2)"""
    t, r, chi, th, ph, mu, lam = sp.symbols("t r chi theta phi mu lam", real=True)
    f = 1 - mu / r ** 2 - lam * r ** 2
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(chi) ** 2, r ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
    X = [t, r, chi, th, ph]
    chi0 = sp.pi / 3 if "offequator" in MUT else sp.pi / 2
    nchi = 1 / r                                                       # the unit normal, n = (1/r) d_chi
    tang = [0, 1, 3, 4]                                                # g is diagonal and n has only chi: K_ab is
    K = sp.Matrix(4, 4, lambda i, j: sp.simplify((nchi * sp.diff(g[tang[i], tang[j]], chi) / 2).subs(chi, chi0)))
    return K                                                           # (1/2) n^chi d_chi g_ab on the tangent block


def proxy():
    """B4: the static zonal scalar mode on the 5D form as Legendre's equation; parity of C_l^1; P_nu at the centre"""
    import mpmath as mp
    r, mu, l, chi = sp.symbols("r mu l chi", positive=True)
    xi = 2 * r ** 2 / mu - 1
    a = sp.Symbol("a")                         # a linear second-order identity holds iff it holds on exp(a xi):
    R = sp.exp(a * xi)                         # the coefficients of 1, a, a^2 are those of P, P', P''
    f = 1 - mu / r ** 2
    E = sp.diff(r ** 3 * f * sp.diff(R, r), r) / r ** 3 - l * (l + 2) * R / r ** 2
    leg = ((1 - xi ** 2) * a ** 2 - 2 * xi * a + l * (l + 2) / 4) * R
    legendre_ok = sp.simplify(E * r ** 2 + 4 * leg) == 0
    lap_ok, parity = {}, {}
    ls = (1, 3, 5) if "oddl" in MUT else (0, 2, 4)
    for lv in (0, 1, 2, 3, 4):
        C = sp.sin((lv + 1) * chi) / sp.sin(chi)
        lap = sp.diff(sp.sin(chi) ** 2 * sp.diff(C, chi), chi) / sp.sin(chi) ** 2      # the S^3 zonal Laplacian
        lap_ok[lv] = sp.simplify(lap + lv * (lv + 2) * C) == 0
        parity[lv] = 1 if sp.simplify(C.subs(chi, sp.pi - chi) - C) == 0 else (
            -1 if sp.simplify(C.subs(chi, sp.pi - chi) + C) == 0 else 0)
    mp.mp.dps = 40
    centre = {}
    for lv in sorted(set(ls) | {1, 3}):
        nu = mp.mpf(lv) / 2
        a, b = mp.legenp(nu, 0, -1 + mp.mpf("1e-12")), mp.legenp(nu, 0, -1 + mp.mpf("1e-24"))
        centre[lv] = dict(horizon=float(mp.legenp(nu, 0, 1)), near=float(a), nearer=float(b),
                          finite=abs(a - b) < mp.mpf("1e-8"))
    return dict(legendre=legendre_ok, laplacian=lap_ok, parity=parity, centre=centre, even=ls)


def report():
    for D, n, w in ((4, 1, 4.0), (4, 1, 10.0), (5, 2, 4.0)):
        print("A2 D = %d order %d w = %g: face born at %+.3f; with half the mass again arriving after: %+.3f" % (
            D, n, w, birth(D, n, w), birth(D, n, w, 0.5)))
    for k, e in evaporation().items():
        print("A3 %s: r0 = %.4g m, |dr_h/dv| = %.2g, mass lost over 8 clocks %.2g, Hawking flux / focusing %.2g" % (
            k, e["r0"], e["rate"], e["lost"], e["flux"]))
    for k, c in core_scales().items():
        print("B1-B2 %s: mu5 = %.4g m^2, onset r_q = %.4g m (5D form; 4D form %.3g m), r_q/ell = %.3g, Lambda5 at the "
              "onset %.3g; x at r = ell: %.2g (5D form), %.2g (4D form)" % (
                  k, c["mu5"], c["rq5"], c["rq4"], c["rq_ell"], c["lam"], c["x5_ell"], c["x4_ell"]))
    print("B3 extrinsic curvature of the equator chi = pi/2:", equator().is_zero_matrix)
    p = proxy()
    print("B4 Legendre, nu = l/2: %s; parity of C_l^1: %s; P_nu at the horizon and at the centre: %s" % (
        p["legendre"], p["parity"], {l: ("%.3g" % c["horizon"], "%.4g -> %.4g" % (c["near"], c["nearer"]))
                                     for l, c in p["centre"].items()}))


def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    b0, b1 = birth(4, 1, 4.0), birth(4, 1, 4.0, 0.5)
    c0, c1 = birth(4, 1, 10.0), birth(4, 1, 10.0, 0.5)
    d0, d1 = birth(5, 2, 4.0), birth(5, 2, 4.0, 0.5)
    FP = _load("focusing_parts.py", "cf_fp")
    a2 = (abs(b0 - FP.face_born(4, 4.0, 1)) < 1e-6 and b1 < b0 < 0 and c1 <= c0 == 0 and d1 < d0 < 0)
    ok.append(a2); say("A2 later infall makes the face born no later (4D w = 4: %+.3f -> %+.3f; 5D: %+.3f -> %+.3f) "
                       "and does not rescue a slow arrival (4D w = 10: %+.3f -> %+.3f): %s" % (b0, b1, d0, d1, c0, c1,
                                                                                               a2))
    ev = evaporation(); e20, eE = ev["r0 = 20 ell"], ev["the Earth cap"]
    a3 = abs(e20["lost"] / 4.4e-66 - 1) < 0.02 and abs(eE["lost"] / 4.4e-69 - 1) < 0.02 and e20["flux"] < 1e-60
    ok.append(a3); say("A3 mass lost over 8 clocks %.3g (r0 = 20 ell), %.3g (Earth cap): %s" % (
        e20["lost"], eE["lost"], a3))
    cs = core_scales(); c20, cE = cs["r0 = 20 ell"], cs["the Earth cap"]
    b1_ = (abs(c20["rq5"] / 4.271e-15 - 1) < 2e-3 and abs(cE["rq5"] / 1.014e-14 - 1) < 2e-3
           and max(c20["rq_ell"], cE["rq_ell"]) < 1e-9 and c20["rq4"] < c20["rq5"])
    ok.append(b1_); say("B1 the onset at %.4g m and %.4g m, r_q/ell %.2g and %.2g, far inside ell: %s" % (
        c20["rq5"], cE["rq5"], c20["rq_ell"], cE["rq_ell"], b1_))
    b2 = max(c20["x5_ell"], c20["x4_ell"], cE["x5_ell"], cE["x4_ell"]) < 1e-35
    ok.append(b2); say("B2 x at r = ell below 1e-35 on both forms (%.2g, %.2g): %s" % (c20["x5_ell"], c20["x4_ell"], b2))
    b3 = equator().is_zero_matrix
    ok.append(b3); say("B3 the equator chi = pi/2 has zero extrinsic curvature, any mu and lam: %s" % b3)
    p = proxy()
    b4 = (p["legendre"] and all(p["laplacian"].values()) and p["parity"] == {0: 1, 1: -1, 2: 1, 3: -1, 4: 1}
          and all(p["centre"][l]["finite"] and abs(p["centre"][l]["horizon"] - 1) < 1e-12 for l in p["even"])
          and not p["centre"][1]["finite"] and not p["centre"][3]["finite"])
    ok.append(b4); say("B4 proxy: Legendre with nu = l/2, C_l^1 of parity (-1)^l, the Z2-even modes finite at the "
                       "centre and the odd ones logarithmic: %s" % b4)
    return all(ok)


def mutants():
    caught = 0; names = ["loss", "mu4", "offequator", "oddl"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
