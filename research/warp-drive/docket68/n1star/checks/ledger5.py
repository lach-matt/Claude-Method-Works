#!/usr/bin/env python3
"""ledger5.py -- four bookkeeping steps of the paper RESPONSE-HL-5D.md as exponent and term ledgers.

The author's rule: everything derived is proved with computational support. Four steps of the paper rested on counting
alone; each is computed here, every check with a negative control that must fail. The style is support5.py's C5: the
exponents are derived from the supplement's stated rules, not typed, and then held against each requirement.

  L1 (exact, sympy; beta0, K, lam symbolic) section 3's 'How Theorem 2 is proved', supplement section 9.4,
     Propositions 9.8-9.9: N = K + 4 + ceil(4 beta0), K' = N - 1. (i) int_(t >= lam^-2) lam^-1 t^(-3/2) dt = 2,
     independent of lam (the 1/lam coupling integrates to a constant); (ii) Lemma 9.3's gain: sqrt(r_in^-3) with r_in
     >= t is t^(-3/2), so E <= lam^K' t^(-1/2) gives |w| <= lam^(K'-3) t^-2, |d w| <= lam^(K'-4) t^-2, inside the
     margin lam t^(-3/2) <= eps t^(-5/4); (iii) Gronwall: lam^(2K'-5) <= lam^(K'+1); (iv) the near-region integrals
     int_t^T t'^(-1-a) (T/t')^b dt' <= t^-a (T/t)^b/(b + a) and log(T/t) <= (T/t)^b/b; (v) the weight's cost (T/t)^beta0
     at t = 1 is lam^(-2 beta0); (vi) the nonlinear terms lam^-5 (lam^(-2 beta0 - 1))^2 lam^-1 = lam^(-8 - 4 beta0) and
     K' > 8 + 4 beta0 for every K >= 6, beta0 > 0; (vii) K' - 2 beta0 - 1 >= K + 2. Each inequality is reduced to a
     polynomial with non-negative coefficients in non-negative variables (K = 6 + kap, ceil(4 beta0) = 4 beta0 + del).
     Control: the split at t = lam^-1 (the integral is 2 lam^(-1/2), not O(1)), and K' = K + 3 (K' > 8 + 4 beta0 fails
     for beta0 > (1 + kappa)/4, beta0 >= 1/4 at K = 6); each variant must fail one requirement.
  L2 (exact, sympy; k, K symbolic) paper section 8.7, supplement section 10.51: support5.py C5's bootstrap ledger with
     the derivative order k symbolic. C5's function holds its rules inside it, so they are restated here and support5.c5
     is imported and run as the cross-check: at (k, K) = (6, 6) both pass and at K = 5 both fail. With k = 6 + a, K = 6 +
     b (a, b >= 0) every requirement is a polynomial with non-negative coefficients (all are linear in k and K), and it
     is also evaluated for k = 6..30, K = 6..12. Control: K = 5 fails (Step 4's 2K - 5 >= K + 1), whatever k is.
  L3 (exact, sympy; numerical integration, stdlib) paper section 3's 'How Theorem 3 is proved', supplement Lemma 11.2
     and Proposition 11.1: the ledger of eight steps J = 3..10 from u_1 in E_2 (Lemma 11.0). The rules of Lemma 11.2:
     the source of a remainder in E_(q-1) has leading term r^-q; the new term is r^(1-q) F, F = (2/(2q - 5)) int S_q
     (checked: -(1/2)(3 - 2(q - 1)) (2/(2q - 5)) = 1); the rest of the source is in E_(3/2) E_(q-1) = E_(q+1/2); its L^2
     norm on the slices (volume r^3) is t^(1-q), the energy integral t^(2-q)/(q - 2), Lemma 9.3 costs t^(-3/2), so the
     new remainder is in E_(q-1/2). Derived per step: monotone gain 1/2, the terms r^(-k/2), k = 4..11, contiguous after
     G_3 (an expansion in r^(-1/2)), G_k's coefficient 2/(k - 3), q > 5/2 at every step (no logarithm, the data term
     -> 0), and the ell-gain E_(3/2+j) E_(q-1/2+m-1-j) = E_(q+m). The outgoing generators of g0 (Vaidya, dr/dv = (1 -
     mu(v)/r^2)/2) are integrated back from points of the far region P cap {t >= lam^-2} (section 9.1's P with sample
     constants) to v = v_start: they stay in it, with r' in [r - (v - v_start)/2, r] and the transport factor at most
     e^(3 d1/(2 r')); for constant mu the tortoise solution is checked exactly. Control: a step with no gain (the
     metric's perturbation in E_1 in place of E_(3/2)) leaves the exponent unchanged and the expansion stalls.
  L4 (exact, sympy) paper sections 8.1 and 8.7, supplement section 10.50(a) with Lemmas 5.1, 5.3 and 6.2: the induction
     over stages m = 2..6. Each stage's oscillating source, Pi_osc (Wm(m_m, phi_m) + K_m), is enumerated by Lemma 5.1's
     weight rule (W weight 1, gh_i weight i, m_i weight i, a derivative lam^-1 dv d_th weight -1 or dphi_i d_th weight i
     - 1, at most two derivatives, d_th acting on an oscillating factor, order m), and the data terms of Lemma 6.2
     (bilinear with d_th W or built from earlier oscillating quantities). Where env = 0 (W = 0 there, and gh_i = 0 for i
     <= m by the hypothesis) every term's Pi_osc is computed to vanish: a term with an oscillating factor is zero, one
     without is th-independent. That holds by construction once the enumeration is right: what L4 adds is the enumeration
     itself; that Lemma 5.1's rule produces every source term, and that W and gh_i are the only oscillating factors, is
     deduced, not computed. ell = g0^-1 dv = d_r is tangent to {v = const}, and the transport with zero source and zero
     data has the zero solution only; so gh_(m+1) = 0 there and the induction proceeds. Control: an envelope-free
     oscillating term (cos 2 th times a mean) in a stage's source survives.

Labels: computed (exact sympy identities and inequalities; L3's generators by RK4). Reach: these are the counts the
steps state; the estimates they count are the supplement's (deduced) and are not recomputed here.

Run: python3 checks/ledger5.py   (about forty seconds)
"""
import contextlib
import io
import itertools
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def holds(expr, syms, strict=False):
    """expr >= 0 (> 0 if strict) for all syms >= 0: a polynomial in syms with non-negative coefficients (positive
    constant term if strict). Sufficient, and exact for the linear ledgers here."""
    p = sp.Poly(sp.expand(expr), *syms)
    if any(c < 0 for c in p.coeffs()):
        return False
    const = p.coeff_monomial(1)
    return const > 0 if strict else True


def l1(control=False):
    lam, t, tt, T, b0, kap, de, a, b, x = sp.symbols("lam t tt T beta0 kappa delta a b x", positive=True)
    K = 6 + kap                                         # K >= 6
    c4 = 4 * b0 + de                                    # ceil(4 beta0), 0 <= del < 1
    variants = [("as stated", lam**-2, K + 3 + c4)]
    if control:
        variants = [("split at lam^-1", lam**-1, K + 3 + c4), ("K' = K + 3", lam**-2, K + 3)]
    results = []
    for name, split, Kp in variants:
        rows = []
        I = sp.integrate(lam**-1 * t**sp.Rational(-3, 2), (t, split, sp.oo))
        rows.append(("(i) int_(t >= split) lam^-1 t^(-3/2) dt = %s, independent of lam" % I,
                     sp.simplify(sp.diff(I, lam)) == 0))
        gain = sp.sqrt(t**-3)                            # Lemma 9.3(a): int |.|^2 <= r_in^-3 int |.|^2 r^3, r_in >= t
        e_w = (Kp, -sp.Rational(1, 2))                   # E <= lam^K' t^(-1/2)
        w0 = (e_w[0] - 3, e_w[1] + sp.log(gain, t).simplify().expand(force=True))
        w1 = (e_w[0] - 4, w0[1])
        rows.append(("(ii) Lemma 9.3's gain t^(-3/2): |w| <= lam^(%s) t^(%s), |d w| <= lam^(%s) t^(%s)"
                     % ("K'-3", w0[1], "K'-4", w1[1]),
                     sp.simplify(gain - t**sp.Rational(-3, 2)) == 0 and w0[1] == -2))
        rows.append(("(ii) margin: lam^(K'-3) t^-2 <= lam t^(-3/2) <= eps t^(-5/4) (t >= 1, lam <= 1)",
                     holds(w0[0] - 1, (kap, de, b0)) and w0[1] <= sp.Rational(-3, 2) <= sp.Rational(-5, 4)))
        rows.append(("(iii) Gronwall: lam^(2K'-5) M^2 <= M lam^(K'+1), 2K' - 5 >= K' + 1",
                     holds((2 * Kp - 5) - (Kp + 1), (kap, de, b0))))
        J = sp.integrate(tt**(-1 - a) * (T / tt)**b, (tt, t, T), conds="none")
        bound = t**-a * (T / t)**b / (b + a)
        # bound - J = T^b T^(-a-b)/(a + b) >= 0 exactly (a + b > 0)
        rows.append(("(iv) int_t^T t'^(-1-a) (T/t')^b dt' <= t^-a (T/t)^b/(b + a): the difference is T^(-a)/(a + b)",
                     sp.simplify(bound - J - T**-a / (a + b)) == 0))
        y = sp.Symbol("y", positive=True)                # log x <= x^b/b <=> log y <= y, y = x^b; y - log y >= 1
        h = y - sp.log(y)
        crit = sp.solve(sp.diff(h, y), y)
        rows.append(("(iv) log(T/t) <= (T/t)^b/b: y - log y has its minimum 1 at y = 1",
                     crit == [1] and sp.diff(h, y, 2).subs(y, 1) > 0 and h.subs(y, 1) == 1))
        cost = sp.powsimp((lam**-2 / 1)**b0, force=True)
        rows.append(("(v) the weight (T/t)^beta0 at t = 1: %s" % cost, sp.simplify(cost - lam**(-2 * b0)) == 0))
        e_boot = -2 * b0 + sp.log(sp.sqrt(lam**-2), lam).expand(force=True)    # t^(1/2) <= T^(1/2) = lam^-1
        e_nl = -5 + 2 * e_boot - 1                       # R_nl lam^-5 t^(-3/2) Q^2, log T <= C lam^-1
        rows.append(("(vi) nonlinear: lam^-5 (lam^(%s))^2 lam^-1 = lam^(%s)" % (e_boot, sp.expand(e_nl)),
                     sp.expand(e_nl - (-8 - 4 * b0)) == 0))
        rows.append(("(vi) small against B: K' - 8 - 4 beta0 > 0 (K >= 6)", holds(Kp + e_nl, (kap, de, b0), True)))
        rows.append(("(vii) data at tau0: K' - 2 beta0 - 1 >= K + 2", holds(Kp - 2 * b0 - 1 - (K + 2), (kap, de, b0))))
        if not control:                                  # concrete beta0 with sympy's ceiling, K = 6
            for bv in (2, sp.Rational(9, 4), sp.Rational(53, 10), 7):
                kp = 6 + 3 + sp.ceiling(4 * bv)
                rows.append(("     beta0 = %s, K = 6: K' = %s > 8 + 4 beta0 = %s; K' - 2 beta0 - 1 = %s >= 8"
                             % (bv, kp, 8 + 4 * bv, kp - 2 * bv - 1), kp > 8 + 4 * bv and kp - 2 * bv - 1 >= 8))
        ok = all(v for _, v in rows)
        results.append(ok)
        if not control:
            print("  L1: Theorem 2's past ledger, N = K + 4 + ceil(4 beta0), K' = N - 1 (beta0, K >= 6 symbolic):",
                  flush=True)
            for nm, v in rows:
                print("      %-108s %s" % (nm, v), flush=True)
        else:
            bad = [nm.split(",")[0] if nm.startswith("(i) ") else nm.split(":")[0] for nm, v in rows if not v]
            print("  L1 control (%s): fails %s" % (name, "; ".join(bad) if bad else "nothing"), flush=True)
    return any(results) if control else all(results)


def ledger(k, K):
    """support5.py C5's rules with k and K free: (name, lhs - rhs, strict). s0 = 4//2 + 1 (four spatial dimensions)."""
    n_sp = 4
    s0 = n_sp // 2 + 1
    imax = k + 1 - s0
    e_inf = lambda i: -s0 - i
    e_dwk = -1
    e_quad = e_inf(0) + 2 * e_dwk
    e_quad0 = e_inf(0)
    return [
        ("Step 1 (10.51(a)): L^inf bounds to i <= k - 2 exist (k + 1 - s0 >= k - 2)", imax - (k - 2), False),
        ("Step 3: the L^inf bounds i = 0, 1 exist (k + 1 - s0 >= 1)", imax - 1, False),
        ("Step 4's split at k - 2: the L^inf factor needs 2 + 1 + s0 <= k + 1", k + 1 - (2 + 1 + s0), False),
        ("Step 4: the scaled product bound |d w d w|_k <= C lam^-s0 |d w|_k^2 needs k >= s0", k - s0, False),
        ("Step 8: [DS23] Theorem 2.4 needs k > n/2 + 1", k - (n_sp // 2 + 1), True),
        ("Step 3: |w|_inf <= C M lam^(K-3) small", K + e_inf(0), True),
        ("Step 3: |d w|_inf <= C M lam^(K-4) <= C M lam^2", K + e_inf(1) - 2, False),
        ("Step 4: the w part of the commutators C M lam^(K-4) N <= C N", K + e_inf(1), False),
        ("Step 4: the worst nonlinear term lam^(%d) N^2 <= C M^2 lam^(K+1)" % e_quad, 2 * K + e_quad - (K + 1), False),
        ("Step 4: the lower nonlinear term lam^(%d) N^2 <= C M^2 lam^(K+1)" % e_quad0, 2 * K + e_quad0 - (K + 1),
         False),
        ("the residual lam^(N_st - 1), N_st = K + 3, within C_R lam^K", (K + 3) - 1 - K, False),
        ("10.51(c): Data(w) at order k is O(lam^(N - 3)) = O(lam^K), N = K + 3", (K + 3) - 3 - K, False),
        ("Step 7: the nonlinear term one power above lam^K", 2 * K + e_quad - K, True),
    ]


def l2(control=False):
    a, b = sp.symbols("a b", nonnegative=True, integer=True)
    sys.path.insert(0, HERE)
    import support5
    with contextlib.redirect_stdout(io.StringIO()):
        c5_66, c5_65 = support5.c5(), support5.c5(control=True)
    Kc = 5
    rows = ledger(6 + a, Kc if control else 6 + b)
    sym = [(nm, holds(e, (a, b), st)) for nm, e, st in rows]
    grid = all((e > 0 if st else e >= 0) for k in range(6, 31) for K in ([Kc] if control else range(6, 13))
               for _, e, st in ledger(k, K))
    here66 = all((e > 0 if st else e >= 0) for _, e, st in ledger(6, 6))
    here65 = all((e > 0 if st else e >= 0) for _, e, st in ledger(6, 5))
    agree = c5_66 == here66 and c5_65 == here65 and c5_66 and not c5_65
    linear = all(sp.Poly(sp.expand(e), a, b).total_degree() <= 1 for _, e, _ in rows)
    ok = all(v for _, v in sym) and grid
    if control:
        bad = [nm for nm, v in sym if not v]
        print("  L2 control (K = 5, k symbolic): fails\n      %s" % ";\n      ".join(bad), flush=True)
        return ok
    print("  L2: C5's ledger with k = 6 + a, K = 6 + b symbolic (a, b >= 0; s0 = 3):", flush=True)
    for nm, v in sym:
        print("      %-108s %s" % (nm, v), flush=True)
    print("      every row linear in (k, K): %s; k = 6..30 x K = 6..12: %s; support5.c5 agrees at (6, 6) and (6, 5): %s"
          % (linear, grid, agree), flush=True)
    return ok and linear and agree


def l3(control=False):
    q, t, tt = sp.symbols("q t tt", positive=True)
    half = sp.Rational(1, 2)
    metric = 1 if control else sp.Rational(3, 2)        # g_lam^-1 - g0^-1 in E_(3/2) (Lemma 11.1); control E_1
    coef = sp.simplify(-half * (3 - 2 * (q - 1)) * 2 / (2 * q - 5))
    rem, rows, terms, ok_steps = sp.Integer(2), [], [3], []    # u_1 in E_2 (Lemma 11.0); G_3 from lam W_TT
    for J in range(3, 11):
        qJ = rem + 1                                     # u~ in E_(q-1): the source leads with r^-q
        lead = qJ - 1                                    # r^(1-q) F
        src = sp.Min(qJ + half, metric + (qJ - 1))       # S~ in E_(q+1/2); (g^-1 - g0^-1) d^2 (r^(1-q) F)
        l2n = sp.Rational(3, 2) - src                    # ||E_p|| on A_P(tau), volume r^3 ~ t^3: t^(3/2 - p)
        en = sp.integrate(tt**l2n, (tt, t, sp.oo), conds="none")    # int from past null infinity, t' >= t
        conv = en.is_finite is not False and not en.has(sp.oo, sp.zoo, sp.nan)
        e_en = sp.simplify(t * sp.diff(en, t) / en)      # the energy's power of t
        ok_steps.append(conv)
        e_pt = e_en - sp.Rational(3, 2)                  # Lemma 9.3: t^(-3/2) times the energy
        new = -e_pt
        rows.append((J, qJ, lead, src, l2n + 1, e_pt, new))
        terms.append(int(2 * lead))
        rem = new
    gains = [r[6] - (r[1] - 1) for r in rows]
    mono = all(g == half for g in gains)
    contiguous = terms == list(range(3, 12))
    nolog = all(r[1] > sp.Rational(5, 2) for r in rows)
    gk = all(sp.simplify(2 / (2 * r[1] - 5) - 2 / (int(2 * r[2]) - 3)) == 0 for r in rows)
    jj, m = sp.symbols("j m")
    ellgain = sp.expand((sp.Rational(3, 2) + jj) + (q - half + m - 1 - jj) - (q + m)) == 0
    if control:
        print("  L3 control (metric in E_1): gains %s, terms r^(-k/2) k = %s" % (gains, terms), flush=True)
        return mono and contiguous
    print("  L3: Lemma 11.2's step: -(1/2)(3 - 2(q - 1)) (2/(2q - 5)) = %s; steps (J, q, term exponent, S' class,\n"
          "      energy exponent, pointwise exponent, new remainder class):" % coef, flush=True)
    for r in rows:
        print("      J = %2d: q = %-4s term r^(-%s), S' in E_(%s), ||d u~~|| <= t^(%s), |u~~| <= t^(%s), E_(%s)"
              % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]), flush=True)
    print("      gain 1/2 at every step: %s; terms r^(-k/2), k = %s, contiguous: %s;\n"
          "      q > 5/2 (no log): %s; G_k = (2/(k - 3)) int S_(k/2+1): %s; E_(3/2+j) E_(q-1/2+m-1-j) = E_(q+m): %s"
          % (mono, terms, contiguous, nolog, gk, ellgain), flush=True)
    gen = generators()
    return coef == 1 and mono and contiguous and nolog and gk and ellgain and all(ok_steps) and gen


def generators():
    """the outgoing generators of five-dimensional Vaidya, dv/dsig = 2, dr/dsig = 1 - mu(v)/r^2, from points of the far
    region back to v_start; section 9.1's P with sample constants (v_start = 0, tau0 = -3, mu0 = 1, V_P = 4, kappa =
    1/2, lam = 1/10, T = lam^-2), mu(v) = mu0 + (2/9) A^2 int_0^v env^2, env = sin^2(pi v/2) on [0, 2], A = 1"""
    r_, mu_ = sp.symbols("r mu", positive=True)
    rstar = r_ + sp.sqrt(mu_) / 2 * sp.log((r_ - sp.sqrt(mu_)) / (r_ + sp.sqrt(mu_)))
    tort = sp.simplify(sp.diff(rstar, r_) - 1 / (1 - mu_ / r_**2)) == 0        # constant mu: v - 2 r* is constant
    vs, tau0, mu0, VP, kap, T = 0.0, -3.0, 1.0, 4.0, 0.5, 100.0
    d1 = VP - vs
    E2 = lambda v: math.sin(math.pi * v / 2)**4 if 0 <= v <= 2 else 0.0
    n_int = 2000
    cum = [0.0]                                       # int_0^v env^2 on a grid of [0, VP]
    for i in range(n_int):
        h = VP / n_int
        v0 = i * h
        cum.append(cum[-1] + h / 6 * (E2(v0) + 4 * E2(v0 + h / 2) + E2(v0 + h)))
    mu = lambda v: mu0 + 2.0 / 9.0 * cum[min(n_int, max(0, int(round(v / VP * n_int))))]
    mu_end = mu(VP)
    ok, worst = True, 0.0
    for tau in (-102.0, -300.0, -2000.0):
        for v in (0.25, 1.0, 1.7, 2.5, 3.4):
            r = v - tau
            hh = kap * (1 + tau0 - tau)**-0.25
            if v + hh > VP or 1 + tau0 - tau < T:
                continue
            n = 4000
            dv = (v - vs) / n
            rr, vv, phase = r, v, 0.0
            for _ in range(n):                        # RK4 backward in v: dr/dv = (1 - mu/r^2)/2, sigma = v/2
                f = lambda vq, rq: (1 - mu(vq) / rq**2) / 2
                k1 = f(vv, rr)
                k2 = f(vv - dv / 2, rr - dv / 2 * k1)
                k3 = f(vv - dv / 2, rr - dv / 2 * k2)
                k4 = f(vv - dv, rr - dv * k3)
                phase += 3.0 / rr * dv / 2
                rr -= dv / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                vv -= dv
                tq = 1 + tau0 - (vv - rr)
                hq = kap * tq**-0.25
                ok &= rr**2 > mu_end and tq >= T and vv + hq <= VP + 1e-12 and rr >= vs - tau0 - 1 + tq - 1e-9
            ok &= r - (v - vs) / 2 - 1e-9 <= rr <= r and phase <= 3 * d1 / (2 * rr)
            worst = max(worst, r - rr)
    print("  L3: tortoise r* = r + (sqrt mu/2) log((r - sqrt mu)/(r + sqrt mu)), dr*/dr = 1/(1 - mu/r^2): %s;\n"
          "      Vaidya generators (mu_end = %.4f) from 15 points of P cap {t >= T} back to v_start stay in it, f > 0,\n"
          "      r' in [r - (v - v_start)/2, r] (largest drop %.4f <= d1/2 = %.1f), factor <= e^(3 d1/(2 r')): %s"
          % (tort, mu_end, worst, d1 / 2, ok), flush=True)
    return tort and ok


def l4(control=False):
    th = sp.Symbol("theta")
    v, r, th5, rqp = sp.symbols("v r th5 rqp", real=True)
    mu = sp.Function("mu")(v)
    f = 1 - mu / r**2
    g0 = sp.zeros(5)
    g0[0, 0], g0[0, 1], g0[1, 0] = -f, 1, 1
    g0[2, 2], g0[3, 3], g0[4, 4] = r**2, r**2 * sp.cos(th5)**2, r**2 * sp.sin(th5)**2
    ell = sp.simplify(g0.inv() * sp.Matrix([1, 0, 0, 0, 0]))
    tangent = ell == sp.Matrix([0, 1, 0, 0, 0])                       # ell = d_r: dv(ell) = 0
    Z, M, s_ = sp.Function("Z"), sp.Function("M"), sp.Symbol("s")
    sol = sp.dsolve(sp.Eq(Z(s_).diff(s_), M(s_) * Z(s_)), Z(s_), ics={Z(0): 0})
    unique = sp.simplify(sol.rhs) == 0                                 # zero source, zero data: Z = 0

    def osc(name):                                                     # a zero-mean profile, generic coefficients
        a1, b1, a2 = sp.symbols("%s_a1 %s_b1 %s_a2" % (name, name, name))
        return a1 * sp.cos(th) + b1 * sp.sin(th) + a2 * sp.cos(2 * th), (a1, b1, a2)

    def pi_osc(e):
        return sp.simplify(e - sp.integrate(sp.expand(e), (th, 0, 2 * sp.pi)) / (2 * sp.pi))
    W, wc = osc("W")
    vanish = {c: 0 for c in wc}                                        # env = 0, so W = 0 (W proportional to env)
    profs = {"W": W}
    report, ok_all = [], True
    for m in range(2, 7):
        for i in range(2, m + 1):
            if "gh%d" % i not in profs:
                profs["gh%d" % i], cs = osc("gh%d" % i)
        osc_f = [("W", 1)] + [("gh%d" % i, i) for i in range(2, m + 1)]
        mean_f = [("m%d" % i, i) for i in range(1, m)]
        ders = [("d_X", 0), ("dv/lam d_th", -1)] + [("dphi%d d_th" % i, i - 1) for i in range(1, m)]
        facs = osc_f + mean_f
        terms = []
        for nf in range(1, m + 3):
            for combo in itertools.combinations_with_replacement(facs, nf):
                for nd in range(0, 3):
                    for dc in itertools.combinations_with_replacement(ders, nd):
                        if sum(w for _, w in combo) + sum(w for _, w in dc) == m:
                            terms.append((combo, dc))
        new = [((("m%d" % m, m),), (("d_X", 0),) * 2)] + \
              [((("m%d" % m, m), ("W", 1)), (("dv/lam d_th", -1),) * k_) for k_ in range(3)] + \
              [((("phi%d" % m, m), ("W", 1)), (("dv/lam d_th", -1), ("d_X", 0)))]       # Wm: m_m and phi_m with W
        data = [((("dth W", 0), (nm, w)), ()) for nm, w in facs] + [(((nm, w), ("any", 0)), ()) for nm, w in osc_f]
        n_with, n_without, ok = 0, 0, True
        dead = {c: 0 for c in vanish}                                  # env = 0 and gh_2..gh_m = 0 (the hypothesis)
        for nm in profs:
            if nm != "W":
                dead.update({sp.Symbol("%s_%s" % (nm, x_)): 0 for x_ in ("a1", "b1", "a2")})
        for combo, dc in terms + new + data:
            # the profiles' coefficients do not depend on th, so setting them to 0 commutes with d_th and Pi_osc
            e, has = sp.Integer(1), False
            for nm, _ in combo:
                if nm in profs:
                    e, has = e * profs[nm].subs(dead), True
                elif nm == "dth W":
                    e, has = e * sp.diff(W, th).subs(dead), True
                else:
                    e *= sp.Symbol(nm)
            nth = sum(1 for d, _ in dc if "d_th" in d)
            e = sp.diff(e, th, nth)                                    # d_th of a mean factor vanishes
            n_with += has
            n_without += not has
            ok &= pi_osc(e) == 0
        if control and m == 2:
            ok &= pi_osc(sp.cos(2 * th) * sp.Symbol("m1")) == 0         # an envelope-free oscillating term
        report.append((m, len(terms) + len(new), len(data), n_with, n_without, ok))
        ok_all &= ok
        if control:
            break
    if control:
        print("  L4 control (cos 2 th m_1 in stage 2's source): Pi_osc vanishes where env = 0: %s" % ok_all,
              flush=True)
        return ok_all
    print("  L4: ell = g0^-1 dv = d_r, tangent to {v = const}: %s; zero source and data give Z = 0: %s; Pi_osc where\n"
          "      env = 0 and gh_2..gh_m = 0 (terms with / without an oscillating factor):" % (tangent, unique),
          flush=True)
    for m, ns, nd, nw, nwo, ok in report:
        print("      stage m = %d: %4d source terms, %2d data terms (%4d / %3d): Pi_osc = 0: %s"
              % (m, ns, nd, nw, nwo, ok), flush=True)
    return tangent and unique and ok_all


CHECKS = [("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
