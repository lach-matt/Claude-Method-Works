#!/usr/bin/env python3
"""scrirad5.py -- the radius near I+ along past causal curves of g = g_0 + h (III.K Lemma 6.1, D621).

III.K Proposition 4.2 and Lemma 2.3 apply II.F Lemma 1.3 with tau := t^flat_* to a metric g = g_0 + h, h small in
II.C's class G~^{0,(2l,0,0)}_e3b. Lemma 1.3 needs, for each p, a compact set containing J^-(p) cap {tau >= c}. Near I+
the level sets of t^flat_* reach r = oo, so a bound on r along past causal curves is needed. II.F Lemma 1.4 (a) gives
one (B := t_* + R~(r) is a time function) only for the convex combinations G_theta of g_0 and Minkowski; for g it can
fail. III.K Lemma 6.1 proves the bound for every g of the class: alpha := dt^flat_* + r^-1 dr is past timelike near
I+ on {1/2 <= t_* < T_1}, so F := t^flat_* + log r decreases towards the past, and r <= max(R_T, r(p))
e^(t^flat_*(p) - c).

The inputs are II.C Lemma 3.2's proof (PART-II-C-OPERATORS.md:392-421): near I+, rho := rho_I = t_*/r, x := rho^l,
  - in the basis rho d_t*^2, d_t* (x)_s d_r, x_I d_t* (x)_s r^-1 d_w, rho^-1 d_r^2, x_I^-1 d_r (x)_s r^-1 d_w,
    r^-1 d_w (x)_s r^-1 d_w, every coefficient of g^-1 - gbar^-1 is at most C_1 (eps_G + rho^(1-l)) rho^l <= C x,
    C := C_1 (eps_G + 1) (taken >= 1);
  - gbar^-1(dt_*, dt_*) = 0, gbar^-1(dt_*, dr) = -1, gbar^-1(dr, dr) = 1;
  - where rho <= rho_-, t^flat_* = t_* F_1(rho), dt^flat_* = A dt_* + B dr, A = 1 - (1 + l) x, B = l rho x;
  - V = t d_t + r d_r is future timelike for g on {r >= R_2}, with dt^flat_*(V) > 0 and dr(V) = r > 0.

  R1 (exact, z3) With alpha = A dt_* + B' dr, B' := B + kappa/r, kappa = 1, and the coefficients c_1, c_2, c_4 (the
     three basis elements not vanishing on alpha (x) alpha) anywhere in [-C x, C x] (c_2 in [-2 C x, 2 C x], which covers
     both conventions for (x)_s):  r g^-1(alpha, alpha) <= -1/2  whenever 0 < rho <= x <= 1 (rho^l >= rho), 0 < l <= 1/2,
     1/2 <= t_* <= T_1, C >= 1 and 37 C T_1 x <= 1.  Proved by z3 (the negation is unsat); and alpha(V) = A t_* + B r +
     kappa > 0 (unsat negation), so alpha is past timelike. Vacuity guard: the hypotheses are satisfiable (sat), also
     with every coefficient at an end of its interval. Encoding guard: the encoded
     g^-1(alpha, alpha) equals the quadratic form of the matrix gbar^-1 + sum c_i e_i (all six basis elements, in the
     coordinates (t_*, r, w)) at 200 random rational points, exactly (l = 1/2, rho a square). The form is encoded
     without r: B' = rho beta, beta := l x + kappa u, u := 1/t_*, so r g^-1(alpha, alpha) = E/u with E polynomial,
     and the claim is E <= -u/2; the encoding guard holds the matrix form against E/u.
  R2 (exact) The gap is real: the metric with g^-1 = gbar^-1 + eps x rho^-1 d_r^2 (l = 1/2; h_t*t* = -eps rho^(l-1),
     a coefficient -eps in II.C's basis, so ||h|| = eps) is Lorentzian, and at rho = eps^2/4 it has g^-1(dt, dt) = +1:
     dt = dB (r >= r'_0 + 1) is spacelike, so B is not a time function of g, for every eps > 0. At the same point
     dt^flat_* and alpha are past timelike. So II.F Lemma 1.4 (a) (and II.F section 7.4, the iota+ model) does not give
     the compact sets for g, and Lemma 6.1 does.
  R3 (numerical, floats) On that metric (eps = 1/10, g_0 = Minkowski), the past directed null curve of largest outward
     drift, dr/d(-t_*) = (1 + eps (r/t_*)^(1-l))/2, from p = (t_*, r) = (3, 10^5) down to t_* = 1: B = t_* + r increases
     towards the past (B is not monotone), F = t^flat_* + log r decreases, and r stays below the bound of Lemma 6.1 (b).
  Controls (each a mutation of the claim; each must make z3 find a counterexample, sat, not merely fail to prove):
     N1 kappa = 0 (alpha = dt^flat_* alone); N2 kappa = -1; N3 the threshold without T_1 (37 C x <= 1); N4 the class's
     decay removed (the coefficients in [-C, C], no factor x = rho^l); N5 gbar^-1(dt_*, dr) = +1.

Labels: R1 computed (exact, z3 over the reals); R2 computed (exact, sympy); R3 computed (floats; a demonstration on
one metric, not used by the proof). The constants C_1, rho_-, R_2, r'_0 of II.C are not computed; the lemma needs only
that they exist.

Run: python3 checks/scrirad5.py   (a few seconds; the saved .out is this run)
"""
import math
import random
import sys
import textwrap
from fractions import Fraction as Fr

import sympy as sp
import z3

HALF = z3.RealVal("1/2")


def variables():
    return {k: z3.Real(k) for k in ("rho", "x", "u", "T1", "C", "l", "c1", "c2", "c4")}


def hyps(v, decay=True, t1=True):
    """u = 1/t_*: 1/2 <= t_* <= T_1 is 0 < u <= 2, u T_1 >= 1"""
    rho, x, u, T1, C, l, c1, c2, c4 = (v[k] for k in ("rho", "x", "u", "T1", "C", "l", "c1", "c2", "c4"))
    cx = C * x if decay else C
    return [rho > 0, rho <= x, x <= 1, l > 0, l <= HALF, u > 0, u <= 2, u * T1 >= 1, C >= 1,
            (37 * C * T1 * x <= 1) if t1 else (37 * C * x <= 1),
            c1 >= -cx, c1 <= cx, c2 >= -2 * cx, c2 <= 2 * cx, c4 >= -cx, c4 <= cx]


def form(v, kappa=1, sign_tr=-1):
    """E with r g^-1(alpha, alpha) = E/u: B' = l rho x + kappa/r = rho beta, beta := l x + kappa u, so
    g^-1(alpha, alpha) = 2 s A B' + B'^2 + c_1 rho A^2 + c_2 A B' + c_4 rho^-1 B'^2 = rho E, and r rho = t_* = 1/u"""
    rho, x, u, l, c1, c2, c4 = (v[k] for k in ("rho", "x", "u", "l", "c1", "c2", "c4"))
    A = 1 - (1 + l) * x
    beta = l * x + kappa * u
    gbar = 2 * sign_tr * A * beta + rho * beta * beta            # gbar^-1: (t*,t*) 0, (t*,r) sign_tr, (r,r) 1
    pert = c1 * A * A + c2 * A * beta + c4 * beta * beta
    return gbar + pert


def prove(kappa=1, sign_tr=-1, decay=True, t1=True):
    """(True, unsat) iff z3 proves r g^-1(alpha, alpha) <= -1/2, i.e. E <= -u/2, on the hypotheses"""
    v = variables()
    s = z3.Solver()
    s.set("timeout", 300000)
    s.add(*hyps(v, decay, t1))
    s.add(form(v, kappa, sign_tr) > -HALF * v["u"])
    res = s.check()
    return res == z3.unsat, res


def refuted(**kw):
    """a control: True iff z3 finds a counterexample (sat), not merely fails to prove"""
    return prove(**kw)[1] == z3.sat


def past_directed():
    """alpha(V) > 0 for V = t d_t + r d_r = t_* d_t* + r d_r: A t_* + B' r = t_* (A + beta) > 0 (negation unsat)"""
    v = variables()
    s = z3.Solver()
    s.add(*hyps(v))
    s.add(1 - (1 + v["l"]) * v["x"] + v["l"] * v["x"] + v["u"] <= 0)
    return s.check() == z3.unsat


def vacuity():
    v = variables()
    s = z3.Solver()
    s.add(*hyps(v))
    a = s.check() == z3.sat
    s.add(v["c1"] == v["C"] * v["x"], v["c2"] == 2 * v["C"] * v["x"], v["c4"] == v["C"] * v["x"])
    b = s.check() == z3.sat
    return a and b


def encoding_guard(n=200):
    """r g^-1(alpha, alpha) from the matrix gbar^-1 + sum c_i e_i in (t_*, r, w) against E/u, exactly, at l = 1/2"""
    rnd = random.Random(621)
    for _ in range(n):
        q = Fr(rnd.randint(1, 40), rnd.randint(41, 400))
        rho = q * q                                                 # x = rho^(1/2) = q
        x, l = q, Fr(1, 2)
        t = Fr(rnd.randint(5, 60), 10)
        r = t / rho
        xI = q                                                      # x_I = rho^(1/2)
        c = [Fr(rnd.randint(-50, 50), 50) * x for _ in range(6)]
        # basis elements as symmetric matrices on (dt_*, dr, dw); (x)_s as a (x) b + b (x) a
        E = [[[Fr(0)] * 3 for _ in range(3)] for _ in range(6)]
        E[0][0][0] = rho
        E[1][0][1] = E[1][1][0] = Fr(1)
        E[2][0][2] = E[2][2][0] = xI / r
        E[3][1][1] = 1 / rho
        E[4][1][2] = E[4][2][1] = 1 / (xI * r)
        E[5][2][2] = 1 / (r * r)
        G = [[Fr(0), Fr(-1), Fr(0)], [Fr(-1), Fr(1), Fr(0)], [Fr(0), Fr(0), 1 / (r * r)]]
        for i in range(6):
            for a in range(3):
                for b in range(3):
                    G[a][b] += c[i] * E[i][a][b]
        A = 1 - (1 + l) * x
        al = [A, l * rho * x + 1 / r, Fr(0)]                       # alpha = dt^flat_* + r^-1 dr
        mat = sum(al[a] * G[a][b] * al[b] for a in range(3) for b in range(3)) * r
        u = 1 / t
        beta = l * x + u
        enc = (-2 * A * beta + rho * beta * beta + c[0] * A * A + 2 * c[1] * A * beta + c[3] * beta * beta) / u
        if mat != enc:
            return False
    return True


def r2():
    eps = sp.Symbol("epsilon", positive=True)
    rho = eps**2 / 4
    x = sp.sqrt(rho)                                                # l = 1/2
    s = eps * x / rho                                               # the coefficient eps x of rho^-1 d_r^2
    Ginv = sp.Matrix([[0, -1], [-1, 1 + s]])                        # (t_*, r) block; the angular block is gbar's
    g = Ginv.inv()
    lorentz = sp.simplify(Ginv.det()) == -1
    h_tt = sp.simplify(g[0, 0] - (-1))                              # gbar_t*t* = -1
    coeff = sp.simplify(h_tt / rho**sp.Rational(-1, 2))             # II.C's basis: h_t*t* = c rho^(l-1)
    dt = sp.Matrix([1, 1])                                          # dt = dt_* + dr
    gdt = sp.simplify((dt.T * Ginv * dt)[0])
    l = sp.Rational(1, 2)
    t_ = sp.Integer(2)
    r_ = t_ / rho
    A, B = 1 - (1 + l) * x, l * rho * x
    dtf = sp.Matrix([A, B])
    al = sp.Matrix([A, B + 1 / r_])
    gtf = sp.simplify((dtf.T * Ginv * dtf)[0])
    gal = sp.simplify((al.T * Ginv * al)[0])
    ok_b = sp.simplify(gdt - 1) == 0
    small = [sp.Rational(1, 10), sp.Rational(1, 1000)]
    ok_f = all(bool(gtf.subs(eps, e0) < 0) and bool(gal.subs(eps, e0) < 0) for e0 in small)
    return lorentz and coeff == -eps and ok_b and ok_f, (lorentz, coeff, gdt, ok_f)


def r3():
    eps, l, c, T = 0.1, 0.5, 1.0, 3.0
    C = 1.0                                                         # |c_4| = eps x <= C x
    T1 = T / 1.0 + 1.0                                              # g_0 = Minkowski: t^flat_* = t_* F_1, C' := 1 here
    rhoT = (37 * C * T1) ** (-1 / l)
    RT = T1 / rhoT
    tf = lambda t, r: t * (1 - (t / r) ** l)                       # noqa: E731
    t, r = 3.0, 1.0e5
    p_tf, p_r = tf(t, r), r
    Rp = max(RT, p_r) * math.exp(p_tf - c)
    B0, F0 = t + r, tf(t, r) + math.log(r)
    n = 20000
    dt_ = (t - 1.0) / n
    Bmono, Fmono, rmax = True, True, r
    Bprev, Fprev = B0, F0

    def f(t, r):
        return 0.5 * (1 + eps * (r / t) ** (1 - l))
    for _ in range(n):                                              # RK4 in u = -t_*
        k1 = f(t, r)
        k2 = f(t - dt_ / 2, r + dt_ * k1 / 2)
        k3 = f(t - dt_ / 2, r + dt_ * k2 / 2)
        k4 = f(t - dt_, r + dt_ * k3)
        r += dt_ * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t -= dt_
        B, F = t + r, tf(t, r) + math.log(r)
        Bmono = Bmono and B <= Bprev + 1e-9
        Fmono = Fmono and F <= Fprev + 1e-9
        Bprev, Fprev, rmax = B, F, max(rmax, r)
    return (not Bmono) and Fmono and rmax <= Rp, (B0, Bprev, F0, Fprev, rmax, Rp)


def say(s, indent="      "):
    print(textwrap.fill(s, 119, subsequent_indent=indent, break_long_words=False, break_on_hyphens=False), flush=True)


def main():
    ok = {}
    p, res = prove()
    pdir = past_directed()
    vac = vacuity()
    enc = encoding_guard()
    ok["R1"] = p and pdir and vac and enc
    say("  R1: r g^-1(alpha, alpha) <= -1/2 on the hypotheses: z3 %s (negation %s); alpha(V) > 0: %s; vacuity guard "
        "(hypotheses sat, also at the coefficients' ends): %s; encoding guard (the form against the matrix, 200 "
        "rational points, exactly): %s" % ("proved" if p else "NOT proved", res, pdir, vac, enc))
    a, info = r2()
    ok["R2"] = a
    say("  R2: witness g^-1 = gbar^-1 + eps x rho^-1 d_r^2: Lorentzian %s; h's coefficient in II.C's basis %s; at "
        "rho = eps^2/4, g^-1(dt, dt) = %s, so B is not a time function, for every eps > 0; dt^flat_* and alpha past "
        "timelike there (eps = 1/10, 1/1000): %s" % info)
    b, info = r3()
    ok["R3"] = b
    say("  R3: extreme past null curve from (t_*, r) = (3, 1e5) to t_* = 1 (eps = 1/10): B %.6g -> %.6g (increases "
        "towards the past), F %.6g -> %.6g (decreases), max r %.6g <= R_p = %.6g" % info)
    ctl = {}
    ctl["N1 kappa = 0"] = refuted(kappa=0)
    ctl["N2 kappa = -1"] = refuted(kappa=-1)
    ctl["N3 threshold without T_1"] = refuted(t1=False)
    ctl["N4 decay removed"] = refuted(decay=False)
    ctl["N5 gbar^-1(dt_*, dr) = +1"] = refuted(sign_tr=1)
    say("  controls (each must make z3 find a counterexample): " + "; ".join("%s %s" % (k, v) for k, v in ctl.items()))
    good = all(ok.values())
    print("R1 %s; R2 %s; R3 %s; controls %s" % tuple(["PASS" if ok[k] else "FAIL" for k in ("R1", "R2", "R3")] +
                                                     ["behave" if all(ctl.values()) else "MISBEHAVE"]), flush=True)
    return 0 if good and all(ctl.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
