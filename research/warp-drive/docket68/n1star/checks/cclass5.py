"""cclass5.py -- SETTLE-GLAM5 round 5: the coefficients b and c of Lemma 11.0's F_1 with an envelope on the wave
(the round-4 verifier's minors m1 and m8), computed on the full five-dimensional gauge-fixed operator with the
machinery of f1lemma5.py (imported, not copied). C2 follows the verifier's scratch script c_class.py.

Setting as f1lemma5.py: g0 := eta + mu r^-2 k k (mu = 4/5), F_1(u_1) = -Ric^H(g0 + U3 + u_1; g0) - (1/2) g^ab d_a d_b u_1
at u_1 = 0, its first variation tested on a value field K0 (coefficient c) and on gradient fields (coefficient b).
The wave now carries an envelope: U3 := lam r^(-3/2) env(v) sin(v/lam) P, env := 2 + sin v.

  C1 (computed, 50 digits) F1b with the envelope: D F_1[K0] - (1/2) lam^-1 K0(ell, ell) A env sin(v/lam) stays
     bounded for lam = 1e-2, 1e-3, 1e-4 while the lam^-1 term grows more than 100-fold beyond it (two points).
     Control (the wave mutated to the non-oscillating lam A env): the same test fails.
  C2 (computed, 50 digits) the class of c's remainder: along a ray at fixed v (r = 4, 16, 64, 256, lam = 1e-3) the
     remainder rem := D F_1[K0] - lead decays like r^(-3/2) with the envelope (fitted slopes below 1.75: E_(3/2),
     not E_2), and like r^(-5/2) once the predicted lam^0 term pred := -K0(ell, ell) A env' cos(v/lam) (the
     -(.)(ell, ell)[d_v d_th W_TT] of the envelope's v-dependence) is subtracted, and without the envelope (slopes
     above 2.25). Control (pred with the opposite sign): the slope stays below 1.75.
  C3 (computed, 50 digits) the wave's part of b: b_W := D F_1[k_grad](g0 + U3) - D F_1[k_grad](g0) is of lam-order 0,
     bounded and bounded away from 0 for lam = 1e-2, 1e-3, 1e-4 (two points). Control (the wave's amplitude
     mutated from lam to lam^2): b_W falls with lam and the test fails. (f1lemma5's F1c shows only b != 0: it passes
     with the amplitude lam^2, b then coming from Gamma[g0].)
Labels: computed (mpmath at 50 digits on sympy-differentiated metrics, central differences in eps).

    python3 checks/cclass5.py
"""
import os
import random
import sys

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f1lemma5 as F  # noqa: E402

FAIL = []


def check(name, ok, msg=""):
    F.print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


V = F.t + F.RR


def wave_env(osc=True, amp=1):
    s = sp.sin(V/F.lam) if osc else sp.Integer(1)
    return F.lam**amp*F.RR**sp.Rational(-3, 2)*(2 + sp.sin(V))*s*F.PMAT


def geo(Jw, X):
    gi = Jw[0]**-1
    r = mp.sqrt(sum(c**2 for c in X[1:]))
    dv = mp.matrix([1] + [c/r for c in X[1:]])
    return gi*dv, r


def lead(Jw, X, lv, K0):
    ell, r = geo(Jw, X)
    v = X[0] + r
    A = mp.matrix(F.PMAT.tolist())*r**mp.mpf(-1.5)
    return (ell.T*K0*ell)[0]*A*(2 + mp.sin(v))*mp.sin(v/lv)/(2*lv)


def pred(Jw, X, lv, K0, sign=1):
    ell, r = geo(Jw, X)
    v = X[0] + r
    A = mp.matrix(F.PMAT.tolist())*r**mp.mpf(-1.5)
    return -sign*(ell.T*K0*ell)[0]*A*mp.cos(v)*mp.cos(v/lv)


def c1():
    F.print("C1  F1b with an envelope on the wave")
    mp.mp.dps = 50
    rnd = random.Random(19)
    lams = [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]
    G0 = F.gb0()
    Jw_s, J0_s, Jn_s = F.Jets(G0 + wave_env()), F.Jets(G0), F.Jets(G0 + wave_env(osc=False))
    rem_ok, grow_ok, ctl_ok, info = True, True, True, []
    for X in F.PTS:
        K0 = F.symmat(rnd)
        rems, leads, nos = [], [], []
        for lv in lams:
            Jw, J0, Jn = Jw_s.at(X, lv), J0_s.at(X, lv), Jn_s.at(X, lv)
            L = lead(Jw, X, lv, K0)
            rems.append(mp.mnorm(F.DF1(Jw, J0, F.test_field("val", K0)) - L, 1))
            leads.append(mp.mnorm(L, 1))
            nos.append(mp.mnorm(F.DF1(Jn, J0, F.test_field("val", K0)) - L, 1))
        info.append((mp.nstr(rems[0], 3), mp.nstr(rems[-1], 3), mp.nstr(leads[-1], 3)))
        rem_ok = rem_ok and max(rems) < 3*min(rems) + 1
        grow_ok = grow_ok and max(leads) > 100*max(rems)
        ctl_ok = ctl_ok and max(nos) > 100*max(rems)
    check("C1 with the envelope: D F_1[K0] - (1/2) lam^-1 K0(ell, ell) A env sin(v/lam) stays bounded "
          "(lam = 1e-2, 1e-3, 1e-4) while the lam^-1 term exceeds it 100-fold", rem_ok and grow_ok,
          "(rem at 1e-2, 1e-4; lead at 1e-4) " + str(info))
    check("C1' control (non-oscillating wave lam A env): the remainder is not bounded", ctl_ok)


def slopes(vals):
    return [float(mp.log(vals[i - 1]/vals[i])/mp.log(4)) for i in range(1, len(vals))]


def c2():
    F.print("C2  the class of c's remainder along a ray at fixed v")
    mp.mp.dps = 50
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    rnd = random.Random(3)
    K0 = F.symmat(rnd)
    xh = [mp.mpf("0.5")]*4
    vfix, lv = mp.mpf("1.3"), mp.mpf("1e-3")
    res = {}
    for name, W in (("env", wave_env()), ("noenv", F.wave())):
        Jw_s = F.Jets(G0 + W)
        r1, r2, r3 = [], [], []
        for r in (4, 16, 64, 256):
            X = [vfix - r] + [r*c for c in xh]
            Jw, J0 = Jw_s.at(X, lv), J0_s.at(X, lv)
            val = F.DF1(Jw, J0, F.test_field("val", K0))
            if name == "env":
                L = lead(Jw, X, lv, K0)
                r1.append(mp.mnorm(val - L, 1))
                r2.append(mp.mnorm(val - L - pred(Jw, X, lv, K0), 1))
                r3.append(mp.mnorm(val - L - pred(Jw, X, lv, K0, sign=-1), 1))
            else:
                L = F.lead_term(Jw, X, lv, K0)
                r1.append(mp.mnorm(val - L, 1))
        res[name] = (slopes(r1), slopes(r2) if r2 else None, slopes(r3) if r3 else None)
    s_env, s_sub, s_wrong = res["env"]
    s_no = res["noenv"][0]
    fmt = lambda s: [round(x, 2) for x in s]
    check("C2 with the envelope rem decays like r^(-3/2) (slopes < 1.75: E_(3/2), not E_2); after subtracting pred, "
          "and without the envelope, like r^(-5/2) (slopes > 2.25)",
          max(s_env[1:]) < 1.75 and min(s_sub[1:]) > 2.25 and min(s_no[1:]) > 2.25,
          f"env {fmt(s_env)}, env - pred {fmt(s_sub)}, no env {fmt(s_no)}")
    check("C2' control (pred with the opposite sign): the slope stays below 1.75", max(s_wrong[1:]) < 1.75,
          str(fmt(s_wrong)))


def c3():
    F.print("C3  the wave's part of the gradient coefficient b")
    mp.mp.dps = 50
    rnd = random.Random(23)
    lams = [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    ok, ctl, info, cinfo = True, True, [], []
    for amp, store in ((1, "ok"), (2, "ctl")):
        Jw_s = F.Jets(G0 + wave_env(amp=amp))
        for X in F.PTS:
            K1 = F.symmat(rnd)
            vals = []
            for lv in lams:
                Jw, J0 = Jw_s.at(X, lv), J0_s.at(X, lv)
                vals.append(max(mp.mnorm(F.DF1(Jw, J0, F.test_field("grad", K1, c))
                                         - F.DF1(J0, J0, F.test_field("grad", K1, c)), 1) for c in (0, 1)))
            good = max(vals) < 4*min(vals) and min(vals) > mp.mpf("0.01")
            if store == "ok":
                ok = ok and good
                info.append([mp.nstr(v, 4) for v in vals])
            else:
                ctl = ctl and not good
                cinfo.append([mp.nstr(v, 4) for v in vals])
    check("C3 b_W = b(g0 + U3) - b(g0) is of lam-order 0: bounded and bounded away from 0 (lam = 1e-2..1e-4)", ok,
          str(info))
    check("C3' control (amplitude lam^2): b_W falls with lam, the test fails", ctl, str(cinfo))


def main():
    for f in (c3, c1, c2):
        f()
    F.print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
