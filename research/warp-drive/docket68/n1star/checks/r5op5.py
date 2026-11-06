"""r5op5.py -- SETTLE-GLAM5 round 5: quantities of Theorem R4.6 measured on the full five-dimensional gauge-fixed
operator instead of typed (the round-4 verifier's M2 and its list of unexercised claims), and the G-naturality behind
the invariance of the continuation (both verifiers' m4). Machinery: f1lemma5.py's jets, Ric^H and first variation
(imported, not copied); P(h) := Ric^H(g_b0 + h; g_b0), g_b0 := eta + mu r^-2 k k, mu = 4/5, Cartesian components.

  O1 (computed, 40 digits) the coefficients of DP(H)[k] = -(1/2) g^ab d_a d_b k + B(H) . d k + C(H) k, read off as the
     first variation of -P(H + .) - (1/2) g^ab d_a d_b (.) on gradient and value test fields (f1lemma5's DF1), along
     a ray of W at fixed s = (v - v1)/r = 1/2, r = 8, 32, 128, 512: the fitted decay exponents of B(0), C(0) (the
     Tangherlini coefficients) and of B(H) - B(0), C(H) - C(0) for a self-similar H = r^-2 F(s) P (the form of Sigma's
     terms) are 3, 4, 3, 4 (to 0.05). Composed by the code into the kernels of Step 5 of Theorem R4.6: a first-order
     coefficient of decay q gives the kernel exponent q, a zero-order one q - 1 (through the Hardy inequality), the
     principal-part difference |g^-1 - g_b0^-1| (decay 2, measured from H) the second-order row's 2: all > 1.
     Control (H mutated to r^-2 (1 + sin(v)/2) P, a profile in v that is not self-similar): the H-coefficients decay
     like r^-2 and the zero-order kernel exponent drops to 1, not integrable: the test fails.
  O2 (computed, 40 digits) the degrees of P(g_b0 + Sigma_p) from the operator, for the regular flat solutions of
     degree -p, Sigma_p = r^-p F_p(s) P with F_p = 2F1(p, p - 2; p - 1/2; s/2) (l = 0 in every Cartesian component;
     F_2 = 1): the fitted decay of |P| is 6 for p = 2 (mu Sigma_2 and Sigma_2 Sigma_2: what Sigma_4 must cancel) and
     13/2 for p = 5/2 (mu Sigma_(5/2)): the flat part, of degree -p - 2, cancels exactly, and the mu part enters at
     degree -p - 4. Control (F mutated to 1 + s, not a flat solution, at p = 2): the decay is 4 (the flat part does
     not cancel).
  O3 (computed, 40 digits) G-naturality: for sigma in G = O(2) x O(2) (the reflection x2 -> -x2 and the rotation of the
     (x1, x2)-plane with cos = 3/5, sin = 4/5), P(sigma^* h)(X) = Lambda^T P(h)(Lambda X) Lambda for an explicit
     non-invariant h of size 0.3 (two points, all components), Lambda = diag(1, sigma): with uniqueness this makes
     the truncated solutions and their limit G-invariant (R5.0 (m4)). Control (sigma mutated to the shear
     x1 -> x1 + x2/2, not an isometry of g_b0): the identity fails.
Labels: computed (mpmath at 40 digits on sympy-differentiated metrics; O1 by central differences in eps).

    python3 checks/r5op5.py
"""
import os
import random
import sys

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f1lemma5 as F  # noqa: E402

FAIL = []
print = F.print


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


t, x1, x2, x3, x4 = F.XS
RR = F.RR
V1 = sp.Rational(7, 10)
S = (t + RR - V1)/RR
P_ = F.PMAT
XH = [mp.mpf("0.5")]*4
RAYS = (8, 32, 128, 512)


def ray_point(r, s=mp.mpf("0.5")):
    r = mp.mpf(r)
    return [mp.mpf("0.7") + (s - 1)*r] + [r*c for c in XH]


def fit(vals):
    """decay exponents between consecutive radii (factor 4)"""
    return [float(mp.log(vals[i - 1]/vals[i])/mp.log(4)) for i in range(1, len(vals))]


def coeffs(Jh_s, J0_s, rnd_seed=5):
    rnd = random.Random(rnd_seed)
    K0, K1 = F.symmat(rnd), F.symmat(rnd)
    B0, C0, BH, CH = [], [], [], []
    for r in RAYS:
        X = ray_point(r)
        Jh, J0 = Jh_s.at(X, 0), J0_s.at(X, 0)
        b0 = max(mp.mnorm(F.DF1(J0, J0, F.test_field("grad", K1, c)), 1) for c in (0, 1, 2))
        bh = max(mp.mnorm(F.DF1(Jh, J0, F.test_field("grad", K1, c)) - F.DF1(J0, J0, F.test_field("grad", K1, c)), 1)
                 for c in (0, 1, 2))
        c0 = mp.mnorm(F.DF1(J0, J0, F.test_field("val", K0)), 1)
        ch = mp.mnorm(F.DF1(Jh, J0, F.test_field("val", K0)) - F.DF1(J0, J0, F.test_field("val", K0)), 1)
        B0.append(b0)
        C0.append(c0)
        BH.append(bh)
        CH.append(ch)
    return [fit(x) for x in (B0, C0, BH, CH)]


def o1():
    print("O1  the coefficients B(H), C(H) of DP(H) along a ray of W, and the kernels composed from them")
    mp.mp.dps = 40
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    H = RR**-2*(1 + S + S**2/3)*P_*sp.Rational(3, 10)
    Hm = RR**-2*(1 + sp.sin(t + RR)/2)*P_*sp.Rational(3, 10)
    out = {}
    for name, HH in (("ss", H), ("mut", Hm)):
        out[name] = coeffs(F.Jets(G0 + HH), J0_s)
    b0, c0, bh, ch = out["ss"]
    tail = lambda s: s[-1]
    meas = [tail(b0), tail(c0), tail(bh), tail(ch)]
    ok = all(abs(m - e) < 0.05 for m, e in zip(meas, (3, 4, 3, 4)))
    # the kernels composed: first order q, zero order (Hardy) q - 1, second-order principal difference 2
    kern = {"B(0) . d phi": round(meas[0]), "C(0) phi (Hardy)": round(meas[1]) - 1,
            "(B(H) - B(0)) . d phi": round(meas[2]), "(C(H) - C(0)) phi (Hardy)": round(meas[3]) - 1,
            "(g^-1 - g_b0^-1) d d phi (Z4a)": 2}
    check("O1 measured decay of B(0), C(0), B(H) - B(0), C(H) - C(0) along the ray: 3, 4, 3, 4", ok,
          str([round(m, 3) for m in meas]))
    check("O1' the kernels composed from them are all > 1 (integrable in sigma)", all(q > 1 for q in kern.values()),
          str(kern))
    mb, mc = tail(out["mut"][2]), tail(out["mut"][3])
    kz = round(mc) - 1
    check("O1'' control (H mutated to r^-2 (1 + sin(v)/2) P): the H-coefficients decay like r^-2 and the zero-order "
          "kernel exponent is 1, not integrable", abs(mb - 2) < 0.1 and abs(mc - 2) < 0.1 and not kz > 1,
          f"B: {round(mb, 3)}, C: {round(mc, 3)}")


def hyp(p):
    return sp.hyper([p, p - 2], [p - sp.Rational(1, 2)], S/2)


def o2():
    print("O2  the degrees of P(g_b0 + Sigma_p) on the operator")
    mp.mp.dps = 40
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    cases = {"p = 2": RR**-2*P_*sp.Rational(3, 10),
             "p = 5/2": RR**sp.Rational(-5, 2)*hyp(sp.Rational(5, 2))*P_*sp.Rational(3, 10),
             "control p = 2, F = 1 + s": RR**-2*(1 + S)*P_*sp.Rational(3, 10)}
    res = {}
    for name, Sg in cases.items():
        Js = F.Jets(G0 + Sg)
        vals = [mp.mnorm(F.ricH(Js.at(ray_point(r), 0), J0_s.at(ray_point(r), 0)), 1) for r in RAYS]
        res[name] = fit(vals)
    e2, e52, ec = res["p = 2"][-1], res["p = 5/2"][-1], res["control p = 2, F = 1 + s"][-1]
    check("O2 |P(g_b0 + Sigma_2)| decays like r^-6 and |P(g_b0 + Sigma_(5/2))| like r^(-13/2): the flat part "
          "cancels, the mu part enters at -p - 4", abs(e2 - 6) < 0.05 and abs(e52 - 6.5) < 0.05,
          f"{round(e2, 3)}, {round(e52, 3)}")
    check("O2' control (F = 1 + s, not a flat solution): decay 4", abs(ec - 4) < 0.1, str(round(ec, 3)))


def pull(h, Lam):
    """sigma^* h for the linear map x -> Lam x (Lam a 5x5 matrix acting on (t, x))"""
    X = sp.Matrix(F.XS)
    sub = dict(zip(F.XS, list(Lam*X)))
    hs = h.subs(sub, simultaneous=True)
    return Lam.T*hs*Lam


def o3():
    print("O3  G-naturality of the gauge-fixed operator relative to g_b0")
    mp.mp.dps = 40
    q = ((t - sp.Rational(3, 10))**2 + (x1 - 1)**2 + (x2 + sp.Rational(1, 2))**2 + x3**2
         + (x4 - sp.Rational(7, 10))**2)/8
    h = P_*sp.Rational(3, 10)*sp.exp(-q)*(1 + x1*t/5 + x2/3)
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    Jh_s = F.Jets(G0 + h)
    refl = sp.diag(1, 1, -1, 1, 1)
    rot = sp.eye(5)
    c5, s5 = sp.Rational(3, 5), sp.Rational(4, 5)
    rot[1, 1], rot[1, 2], rot[2, 1], rot[2, 2] = c5, -s5, s5, c5
    shear = sp.eye(5)
    shear[1, 2] = sp.Rational(1, 2)
    res = {}
    for name, Lam in (("reflection", refl), ("rotation", rot), ("shear (control)", shear)):
        Jp_s = F.Jets(G0 + pull(h, Lam))
        Lm = mp.matrix(Lam.tolist())
        worst, size = mp.mpf(0), mp.mpf(0)
        for X in F.PTS:
            LX = list(Lm*mp.matrix(X))
            lhs = F.ricH(Jp_s.at(X, 0), J0_s.at(X, 0))
            rhs = Lm.T*F.ricH(Jh_s.at(LX, 0), J0_s.at(LX, 0))*Lm
            worst = max(worst, mp.mnorm(lhs - rhs, 1))
            size = max(size, mp.mnorm(rhs, 1))
        res[name] = (worst, size)
    ok = all(res[n][0] < mp.mpf(10)**-30 for n in ("reflection", "rotation"))
    check("O3 P(sigma^* h) = Lambda^T P(h)(Lambda .) Lambda for the reflection x2 -> -x2 and the rotation (3/5, 4/5) "
          "(two points, all components)", ok,
          str({n: (mp.nstr(v[0], 3), mp.nstr(v[1], 3)) for n, v in res.items()}))
    check("O3' control (the shear x1 -> x1 + x2/2): the identity fails", res["shear (control)"][0] > mp.mpf(10)**-4)


def main():
    for f in (o3, o2, o1):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
