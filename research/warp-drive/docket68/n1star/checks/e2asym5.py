#!/usr/bin/env python3
"""e2asym5.py -- E2-PILOT section 3i (D460): asymmetric multipliers for l = 0 and l = 1, and the summed H^1 constant.

Corollaries E2.11-E2.12's constant C <= 808.6 at sigma = 3 is set by l = 0: X_0 = (1 + (1 + 2m'(M' + 2|sigma|)
B_0)^(1/2))/(2m') with m' = min_I (phi' - q) = 0.00258 (section 3g, Z4), small because the symmetric tanh of width
49/50 is nearly flat at the ends of I = {r in [1.2, 4]}; l = 1 gives 675.1 over l >= 1.
Section 3g noted that a multiplier narrower
toward the horizon and wider outside gives B_1(3) of about 86 (D387, a scratch computation). Here
phi = tanh(g(r_*)), g' = 1/s(r_*), s(x) = s_L + (s_R - s_L)/(1 + e^(-(x - x_c)/kap)), so the width is s_L < 1 toward
the horizon (what the tail needs) and s_R outside, and for l = 0, q = sum_k c_k sech^2((r_* - x_k)/k_k) with the c_k
from a linear program over a dictionary (maximise min_I W_q subject to W_q >= phi'/30 and q <= theta phi'), as
section 3g did for its symmetric phi. Everything is in floating point on a grid of r_* from the horizon side
(ln(r - 1) = -60) to r = 120; the tails beyond are not checked here. Labels: computed (floating point, not certified).

  A1 control: the symmetric multipliers reproduce the certified constants within 10 % (as section 3i does, B_1 from
     the multiplier centred at V_1's peak, s = 49/50, and X_1 from the identity with the one centred at the photon
     sphere, its m' and M', the bound Y <= B_1 ||f|| being any multiplier's: B_1(3) against 264.5 and X_1(3) against
     495.9; l = 0 with section 3g's phi and a q from the same program: X_0(3) against 808.6, as the program optimises
     w_I, not X_0, and the dictionary differs).
  A2 the best asymmetric multiplier found for l = 1 (w_1 >= 0 on the grid): B_1(3), X_1(3) and
     C_1 = (X_1^2 + 3 B_1^2)^(1/2).
  A3 the same for l = 0 with q, over s_L = 49/50, the centre at x_* - 0.3, x_* and x_* + 0.3, s_R from 49/50 to 2,
     theta = 1/2 (then 0.3 and 0.7 at the best): B_0(3), X_0(3). The program is solved on a sixth of the points near
     the photon sphere and where phi alone misses the margin, then again with the points the full grid finds below
     phi'/60, at most five times (HiGHS interior point).
  A4 the summed constant at sigma = 3, max(X_0, C_1, C_2, ...) with section 3i's certified C_l for l >= 2 (C_2 = 284.9
     the largest), against 808.6.
  A5 the l = 1 multiplier, centred at x_*, at every l >= 1: it changes sign exactly where U' does (r = sqrt 2), so, as
     in section 3f, w_l = w_1 + (a - a_1)(-phi U') >= w_1 and m', M' do not depend on l; B_l, X_l, A_l and C_l for
     l = 1, ..., 6 (l >= 6 bounded by l = 6 as in section 3i), and the summed constant with them.

    python3 checks/e2asym5.py
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import linprog

SIGMA = 3.0
C_REST = {2: math.sqrt(81191), 3: math.sqrt(65709), 4: math.sqrt(57723), 5: math.sqrt(52794), 6: math.sqrt(51017)}


def rstar(r):
    return r + 0.5 * np.log((r - 1) / (r + 1))


def grid():
    """r_* and r on a grid in t = ln(r - 1), r - 1 kept separately so that the horizon side keeps its digits"""
    t = np.concatenate([np.arange(-60.0, 1.4, 0.004), np.arange(1.4, math.log(119.0), 2e-4)])
    e = np.exp(t)
    r = 1 + e
    return r + 0.5 * (t - np.log(2 + e)), r, e


X, R, EM = grid()
INI = (R >= 1.2) & (R <= 4.0)
XSTAR = float(rstar(np.sqrt(2.0)))


def pot(l):
    y = 1 / R**2; f = EM * (2 + EM) * y
    a, b = l * (l + 2) + 0.75, 2.25
    V = f * (a * y + b * y**2)
    dVdr = (2 / R**3) * (a * y + b * y**2) + f * (a + 2 * b * y) * (-2 / R**3)
    return V, f * dVdr


def multiplier(sL, sR, xc, kap=0.5):
    """phi = tanh(g), g' = 1/s(x); returns phi, phi', phi'''"""
    z = (X - xc) / kap
    e = 1 / (1 + np.exp(-np.clip(z, -700, 700)))
    s = sL + (sR - sL) * e
    s1 = (sR - sL) * e * (1 - e) / kap
    s2 = (sR - sL) * e * (1 - e) * (1 - 2 * e) / kap**2
    g1 = 1 / s; g2 = -s1 / s**2; g3 = (2 * s1**2 - s * s2) / s**3
    # g(x) = int_xc^x g1, by the trapezoidal rule on the grid (only phi's sign and size need it)
    G = np.concatenate([[0.0], np.cumsum(0.5 * (g1[1:] + g1[:-1]) * np.diff(X))])
    G -= np.interp(xc, X, G)
    T = np.tanh(G)
    S = 1 / np.cosh(np.clip(G, -350, 350))**2
    p1 = g1 * S
    p3 = g3 * S - 6 * g1 * g2 * T * S - 2 * g1**3 * S**2 + 4 * g1**3 * T**2 * S
    return T, p1, p3


def constants(mp_, Mp, wI, sigma=SIGMA):
    B = math.sqrt((2 / mp_ + (Mp + 2 * sigma)**2 / wI) / wI)
    Xc = (1 + math.sqrt(1 + 2 * mp_ * (Mp + 2 * sigma) * B)) / (2 * mp_)
    return B, Xc


def l1_case(sL, sR, xc):
    V, dV = pot(1)
    T, p1, p3 = multiplier(sL, sR, xc)
    w = -T * dV - p3 / 2
    if w.min() < -1e-14:
        return None
    mp_, Mp, wI = p1[INI].min(), p1[INI].max(), w[INI].min()
    if wI <= 0:
        return None
    B, Xc = constants(mp_, Mp, wI)
    return dict(B=B, X=Xc, C=math.sqrt(Xc**2 + 3 * B**2), m=mp_, M=Mp, w=wI)


def l0_case(sL, sR, xc, theta=0.5, offsets=np.arange(-3.0, 3.01, 0.25)):
    V, dV = pot(0)
    T, p1, p3 = multiplier(sL, sR, xc)
    w0 = -T * dV - p3 / 2
    kaps = [0.3 * sL, 0.5 * sL, 0.9 * sL]
    cols_q, cols_W = [], []
    for o in offsets:
        for k in kaps:
            u = (X - (XSTAR + o)) / k
            sech2 = 1 / np.cosh(np.clip(u, -350, 350))**2
            th = np.tanh(u)
            q = sech2
            qpp = (4 * sech2 * th**2 - 2 * sech2**2) / k**2
            cols_q.append(q); cols_W.append(qpp - 2 * q * V)
    Q = np.array(cols_q).T; Wk = np.array(cols_W).T
    # constraints where they can bind (where the bumps live, and where phi alone falls short of the margin), on a
    # coarse subset first; the points the full grid finds violated are added and the program solved again
    region = np.where((np.abs(X - XSTAR) < 6) | (w0 < p1 / 30))[0]
    n = Q.shape[1]
    sel = region[::6]
    for _ in range(5):
        Wa, Qa, w0a, p1a, Ia = Wk[sel], Q[sel], w0[sel], p1[sel], INI[sel].astype(float)
        A = np.vstack([np.hstack([-Wa, Ia[:, None]]), np.hstack([-Wa, np.zeros((len(sel), 1))]),
                       np.hstack([Qa, np.zeros((len(sel), 1))])])
        bb = np.concatenate([w0a, w0a - p1a / 30, theta * p1a])
        sc = np.maximum(np.abs(A).max(1), np.abs(bb)); sc[sc == 0] = 1          # each row normalised
        cobj = np.zeros(n + 1); cobj[-1] = -1
        res = linprog(cobj, A_ub=A / sc[:, None], b_ub=bb / sc, bounds=[(0, None)] * n + [(None, 1.0)],
                      method="highs-ipm", options={"time_limit": 120.0})
        if res.status != 0:
            return None
        c = np.round(res.x[:n], 6)
        q = Q @ c; W = w0 + Wk @ c
        bad = region[(W[region] < p1[region] / 60) | (q[region] > theta * p1[region])]
        bad = np.setdiff1d(bad, sel)
        if not len(bad):
            break
        sel = np.union1d(sel, bad)
    if W.min() < -1e-12 or (p1 - q).min() < 0:
        return None
    mp_, Mp, wI = (p1 - q)[INI].min(), np.abs(p1 - 2 * q)[INI].max(), W[INI].min()
    if wI <= 0 or mp_ <= 0:
        return None
    B, Xc = constants(mp_, Mp, wI)
    return dict(B=B, X=Xc, m=mp_, M=Mp, w=wI, theta=theta)


def main():
    ok = {}
    # A1: the symmetric controls
    V1 = pot(1)[0]
    peak = l1_case(0.98, 0.98, X[np.argmax(V1)])
    ps = l1_case(0.98, 0.98, XSTAR)
    c = ps["M"] + 2 * SIGMA
    X1 = (1 + math.sqrt(1 + 2 * ps["m"] * c * peak["B"])) / (2 * ps["m"])
    sym0 = l0_case(0.98, 0.98, XSTAR - 0.3)
    print("  A1 symmetric s = 49/50: l = 1, B_1(3) = %.1f at V_1's peak (certified 264.5), X_1(3) = %.1f with "
          "the photon sphere's m' = %.5f, M' = %.4f (certified 495.9); l = 0 at section 3g's centre: m' = %.5f, "
          "w_I = %.4f, "
          "B_0(3) = %.1f, X_0(3) = %.1f (certified 275.2, 808.6)"
          % (peak["B"], X1, ps["m"], ps["M"], sym0["m"], sym0["w"], sym0["B"], sym0["X"]), flush=True)
    ok["A1"] = (abs(peak["B"] / 264.5 - 1) < 0.1 and abs(X1 / 495.9 - 1) < 0.1
                and abs(sym0["X"] / 808.6 - 1) < 0.1)
    # A2: l = 1, asymmetric
    best1 = None
    for sL, sR, dx in itertools.product((0.6, 0.75, 0.9, 0.98), (1.0, 1.5, 2.0, 3.0, 4.0, 6.0),
                                        (-0.6, -0.3, 0.0, 0.3, 0.6)):
        rr = l1_case(sL, sR, XSTAR + dx)
        if rr and (best1 is None or rr["C"] < best1["C"]):
            best1 = dict(rr, sL=sL, sR=sR, dx=dx)
    print("  A2 l = 1: s_L = %g, s_R = %g, x_c = x_* %+g: m' = %.4f, M' = %.3f, w_I = %.4f; B_1(3) = %.1f, "
          "X_1(3) = %.1f, C_1 = %.1f (certified symmetric: 264.5, 495.9, 675.1)"
          % (best1["sL"], best1["sR"], best1["dx"], best1["m"],
                                                                    best1["M"], best1["w"], best1["B"], best1["X"],
                                                                    best1["C"]), flush=True)
    ok["A2"] = best1["C"] < 675.1
    # A3: l = 0, asymmetric, with q: a coarse pass over s_R, then the neighbours of the best
    best0 = None

    def try0(sL, sR, dx, th):
        nonlocal best0
        rr = l0_case(sL, sR, XSTAR + dx, theta=th)
        print("      l = 0, s_L %g, s_R %g, x_c - x_* %+g, theta %g: %s" % (sL, sR, dx, th, "X_0 = %.1f" % rr["X"] if rr
                                                                          else "no admissible q"), flush=True)
        if rr and (best0 is None or rr["X"] < best0["X"]):
            best0 = dict(rr, sL=sL, sR=sR, dx=dx)
    for dx, sR in itertools.product((-0.3, 0.0, 0.3), (0.98, 1.1, 1.25, 1.5, 1.75, 2.0)):
        try0(0.98, sR, dx, 0.5)
    b = dict(best0)
    for th in (0.3, 0.7):
        try0(0.98, b["sR"], b["dx"], th)
    print("  A3 l = 0: s_L = %g, s_R = %g, x_c = x_* %+g, q <= %g phi': m' = %.4f, M' = %.3f, w_I = %.4f; "
          "B_0(3) = %.1f, X_0(3) = %.1f (certified symmetric: 275.2, 808.6)"
          % (best0["sL"], best0["sR"], best0["dx"], best0["theta"], best0["m"], best0["M"], best0["w"], best0["B"],
             best0["X"]), flush=True)
    ok["A3"] = best0["X"] < 808.6
    # A4: the summed constant with section 3i's certified C_l for l >= 2
    Cs = {0: best0["X"], 1: best1["C"]}
    Cs.update(C_REST)
    lmax = max(Cs, key=Cs.get)
    print("  A4 the summed H^1 constant at sigma = 3, l >= 2 certified: C = %.1f, set by l = %d (certified: 808.6, set "
          "by l = 0); per l: %s" % (Cs[lmax], lmax, ", ".join("%d: %.1f" % (k, v) for k, v in sorted(Cs.items()))),
          flush=True)
    ok["A4"] = Cs[lmax] < 808.6
    # A5: the l = 1 multiplier at every l >= 1 (centred at x_*, it changes sign where U' does, so w_l >= w_1)
    if best1["dx"] == 0:
        T, p1, p3 = multiplier(best1["sL"], best1["sR"], XSTAR)
        mp_, Mp = p1[INI].min(), p1[INI].max()
        c = Mp + 2 * SIGMA
        C5 = {0: best0["X"]}
        mono = True
        prev = None
        for l in range(1, 7):
            V, dV = pot(l)
            w = -T * dV - p3 / 2
            wI = w[INI].min()
            mono &= w.min() >= -1e-14 and (prev is None or wI >= prev)
            prev = wI
            B, Xl = constants(mp_, Mp, wI)
            a = l * (l + 2) + 0.75
            K = 2 * Xl + c * B
            A = 3 * B * B if l == 1 else l * (l + 2) * K / (a - 3.75)
            C5[l] = math.sqrt(Xl**2 + A)
        lm = max(C5, key=C5.get)
        print("  A5 the l = 1 multiplier at every l >= 1 (w_l >= 0 and min_I w_l increasing to l = 6: %s): C_l = %s; "
              "C = %.1f, set by l = %d (l >= 6 bounded by l = 6 as in section 3i)"
              % (mono, ", ".join("%d: %.1f" % (k, v) for k, v in sorted(C5.items())), C5[lm], lm), flush=True)
        ok["A5"] = mono and C5[lm] < Cs[lmax]
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
