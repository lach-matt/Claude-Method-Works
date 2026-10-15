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

Item 424, the gate (330; verify_ledger's INTERIOR column): M finalized the large end's interior for its verifier
("Yes", 424).  The earlier verifications that bear on it are carried here; the rest do not bear, each with its reason
in the ledger.  G1-G2 compute the two that move or bound a number.
  (254 (Q2)) the 4D forms hold for r >> ell and the 5D forms for r << ell; at r ~ ell neither holds (B3).
  (261 (Q1)-(Q2)) the large end's lower edge is the two-end construct's convention: the 4D forms are controlled for
     r0 > 10 ell, which r0 = 20 ell and the Earth cap meet (G2); between 1.25 ell and 10 ell F5's 4D widths are an
     estimate.
  (261 (Q3)) the plane is four-dimensional Schwarzschild with corrections O(ell^2/r0^2), surface gravity 1/(4M):
     F5's 4D traces carry those corrections, 2.5e-3 at r0 = 20 ell (G2).
  (267 (Q2)-(Q4)) greybody 0.93 and brane dominance enter A3's coefficient only, inside its tenfold.
  (267 (Q5)) the hole is collapse-formed and evaporates: A3's flux is the Unruh state's, no bath, no second exterior.
  (271 (Q3), 319 (Q1)) position 2's side by time reversal is the geometry only: its white-hole face's blueshift is
     C8's, bounded over its open period.
  (304 (Q5)) the bounce's own (B) is a board reading at 304: this object stops at x = 1 and claims nothing inside.
  (310 (Q1)) the README leaves by position 2's face on a quantum region of 273's kind, which this object does not model.
  (310 (outside G5), 319 (Q2), 348 (Q6)) under the G5 readings, (3/2) G ell and G ell/2, r_q moves as G5^(5/12), by
     1.184 and 0.749, and quantum_onset's r_q/R_5 as G5^(2/9), by 1.094 and 0.857 (G1): r_q/ell stays below 1e-9.
  (310 (Q3), 355 (Q10)) position 2's side carries its own mass, m2/m = (G2/G)^(1/2) = 1, 1.41 or 2: its time reverse
     sits at its own r_s2.
  (317 (Q3)) position 2's side as the time reverse is the construction's time symmetry (M's 273), not READ.
  (317 (Q4), 355 (Q1)) mu(v) never exceeds the README's whole mass, given spherical symmetry and positive energy: A2's
     arrivals rise monotonically to it.
  (317 (Q8)) warp order enters the core's near field at first order, r/ell (B3's tension), not its square.
  (319 (Q5)-(Q7)) B3's tensionless equator is a limit, the tension's correction r/ell beside it.
  (332 (Q1)) the Gauss-Bonnet coupling is zero under 328 (M-ONE-LIGHT-CONE): quantum_onset's P2 cites 324-328.
  (337 (Q1)) the faces' own generators end where the faces close (CLOSE): not claimed by O1c here.
  (337 (Q2), (Q7), (Q8)) the README's parts as radial null flux is RDUST's form (386, 2'); whether the written README
     comes in that way is SOURCE's; the parts' own worldlines are the flux's rays (F2).
  (337 (Q3), (Q4)) classical GR is given up inside 273's region; Einstein's law is exact at the two-derivative order.
  (337 (Q5), (Q6)) the bulk's own content (320 (b)-(c)) enters at its own order, not computed here.
  (337 (Q9)-(Q11)) 273's quantum region is the option text M chose.
  (339 (Q4)) F1's null energy is classical; the quantum flux is A3's, read under 120.
  (348 (Q1)) F5 claims no censorship: past its widths the face is born at the onset, whose rays escape along the
     trapping horizon where K diverges at orders >= 3; the widths are a requirement on SOURCE.
  (348 (Q2)) the hole's mass is the README's whole E: a lossless collapse.
  (348 (Q3)) the face static from v = w: A1-A3 above.
  (348 (Q5), 355 (Q13)) the rests-on: 270 (a) and 273 (a) (M's construction, as the board reads it), 320 (b)-(c),
     226 with tension, 418, 422, and quantum_onset's P1-P4.
  (348 (outside)) on the 4D onset K = 48 m^2/r^6 diverges along r = 2m when the face is born at the onset: F5's 4D
     widths are what keep it behind our face.
  (355 (Q4)) the Hawking negative ingoing flux lies near the horizon and partly outside it; A3's bound is its total.
  (355 (Q8)) Figueras and Wiseman's far Poincare horizon is their boundary condition, not their result.
  (355 (Q11)) F5's widths are for a spherical arrival; a collimated pulse focuses locally and is not traced.
  (355 (Q14)) every round surface is trapped at the large end for N > 1.13 N_L, met from its start (ell/m = 1.596).
  G1 (computed) the G5 readings: r_q = (72 mu5^2 l5^4)^(1/8) with mu5 and l5^3 each proportional to G5, so r_q goes as
     G5^(5/12); r_q/R_5 = (l5/ell)^(2/3) as G5^(2/9).
  G2 (computed) r0 = 20 ell and the Earth cap lie above 10 ell, (ell/r0)^2 = 2.5e-3 and 2.5e-6.

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


def gate_numbers():
    """G1-G2: the G5 readings' factors on r_q and r_q/R_5, and the 4D forms' control at the two reference holes"""
    p5, p9 = (sp.Rational(4, 12) if "g5_power" in MUT else sp.Rational(5, 12)), sp.Rational(2, 9)
    G5, mu0, l0 = sp.symbols("G5 mu0 l0", positive=True)
    rq = (72 * (mu0 * G5) ** 2 * (l0 * G5 ** sp.Rational(1, 3)) ** 4) ** sp.Rational(1, 8)
    power = sp.simplify(sp.log(rq.subs(G5, sp.E) / rq.subs(G5, 1)))
    fac = {g: (float(g ** p5), float(g ** p9)) for g in (1.5, 0.5)}
    cs = core_scales()
    worst = max(c["rq_ell"] for c in cs.values()) * max(f[0] for f in fac.values())
    ctrl = {k: (c["r0"] / _load("quantum_onset.py", "cf_qo").onset_4d()["ell"]) for k, c in cs.items()}
    return dict(power=power, p5=p5, fac=fac, worst=worst, ctrl=ctrl,
                corr={k: 1 / v ** 2 for k, v in ctrl.items()})


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
    gn = gate_numbers()
    print("G1 r_q goes as G5^%s; under (3/2) G ell and G ell/2: r_q x %.3f, %.3f; r_q/R_5 x %.3f, %.3f; worst r_q/ell "
          "%.2g" % (gn["power"], gn["fac"][1.5][0], gn["fac"][0.5][0], gn["fac"][1.5][1], gn["fac"][0.5][1],
                    gn["worst"]))
    print("G2 r0/ell: %s; (ell/r0)^2: %s" % ({k: round(v, 1) for k, v in gn["ctrl"].items()},
                                             {k: "%.2g" % v for k, v in gn["corr"].items()}))
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
    gn = gate_numbers()
    g1 = (gn["power"] == sp.Rational(5, 12) and gn["p5"] == sp.Rational(5, 12)
          and abs(gn["fac"][1.5][0] - 1.184) < 1e-3 and abs(gn["fac"][0.5][0] - 0.749) < 1e-3
          and abs(gn["fac"][1.5][1] - 1.094) < 1e-3 and abs(gn["fac"][0.5][1] - 0.857) < 1e-3 and gn["worst"] < 1e-9)
    ok.append(g1); say("G1 (item 424) r_q as G5^(5/12): x %.3f and %.3f under the G5 readings, r_q/ell below 1e-9: "
                       "%s" % (
        gn["fac"][1.5][0], gn["fac"][0.5][0], g1))
    g2 = (all(v > 10 for v in gn["ctrl"].values()) and abs(gn["corr"]["r0 = 20 ell"] - 2.5e-3) < 1e-6
          and abs(gn["ctrl"]["the Earth cap"] - 635.2) < 0.1)
    ok.append(g2); say("G2 (item 424) both reference holes above 10 ell (20, %.1f), (ell/r0)^2 = 2.5e-3 at 20 ell: "
                       "%s" % (
        gn["ctrl"]["the Earth cap"], g2))
    ok.append(b4); say("B4 proxy: Legendre with nu = l/2, C_l^1 of parity (-1)^l, the Z2-even modes finite at the "
                       "centre and the odd ones logarithmic: %s" % b4)
    return all(ok)


def mutants():
    caught = 0; names = ["loss", "mu4", "offequator", "oddl", "g5_power"]
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
