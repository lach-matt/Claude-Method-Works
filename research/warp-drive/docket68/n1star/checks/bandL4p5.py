#!/usr/bin/env python3
"""bandL4p5.py -- the band 6 <= K <= 9 is an artefact of Lemma L.4's hypothesis (EQUALITY5-LAYER.md, Round 4, R4.3:
Lemma L.4', and Proposition L.12 for every K >= 6).

Lemma L.4 assumes eps_(M*)(v1) <= lam^3 only to make |d^j g_app| <= C for j <= 4.  In the commuted equations at level i
(the energy E_i of d^i w) the large coefficients d^3 g_app, d^4 g_app (sizes lam^-2 eps_3, lam^-3 eps_4) multiply lower
derivatives of w only, so a triangular Gronwall (E_0, then E_1, then E_2, each lower energy a source of the next)
needs only eps_4(v1) <= lam, and returns the same bound |w| <= C lam^(N-5) eps_(M*)(v1).

  H1 (exact rationals) The ledger of every term of d^i of the remainder's equation, i = 0, 1, 2 (Lemma L.4's steps 2-4
     and 6): the commutator d^p g_lam^-1 d^(i-p+2) w (1 <= p <= i), the source part d^(i-p) w d^(p+2) g_app (0 <= p <=
     i), the Q-difference d^(1+a) g_app d^(1+b) w and d^(1+a) g_app d^(1+b) g_app d^c w (a + b (+ c) = i), each
     coefficient of size lam^e with e = min(0, 1 - j + h) for d^j g_app under eps_4 <= lam^h (g0's own derivatives
     O(1); d^j w, j <= 3, bounded by Theorem E for K >= 6), and the term admissible when e >= max(k, 1) - i - 1, k the
     order of w in it (that is, it is at most C lam^(N-3-i) eps given E_j <= C lam^(N-3-j) eps for j < i, and, at the
     top, a bounded Gronwall coefficient).  Every term is admissible at h = 1.  Controls (mutations of the computed
     path): h = 1/2 fails (at level 0, lam^-1 eps_2 is a large Gronwall coefficient); the non-triangular rule (every
     coefficient into Gronwall, e >= 0) fails at h = 1 and holds only from h = 3, which is Lemma L.4's hypothesis.
  H2 (exact rationals; amended in round 5 on the verifier of round 4's MAJOR 2 and MINOR 5) Proposition L.12 with
     Lemma L.4' (N = K + 3, M = 2N + 8, m := max(56 M, 4 P M, ceil(4 M/delta)), P = 50 and 200) on the delta-grid
     {1/1000, 1/100, 1/20, 1/10, 1/5, 1/4, 3/10, 2/5, 49/100}, each comparison made pointwise (every error at the level
     E = lam^s against the margin c E^(2 + 1/m) at the same E, all exponents linear in s, so checked at the ends of
     each range): (i) the upper layer E >= lam^(3 - delta) is spacelike for every K in [6, 40]: where eps_4 <= lam (s
     >= s_A = (1 + delta)/(1 - 4/m)) the margin beats the signal, lam^4 eps, lam eps^2 and L.4''s w = lam^(N - 5) eps
     on s in [s_A, 3 - delta]; for s <= s_A Theorem E's w = lam^(K - 3) as in layerband5 B2 (i), on s in [delta/2, s_A]
     (below lam^(delta/2), E is above every power the proof uses), which needs s_A <= (K - 3)/2 - delta/2; (iii) the
     band lam^(3 + delta) <= E <= lam^(3 - delta): every error below lam^gamma times the margin at the same level, with
     gamma(delta, K) := min(1/10, half the least slack), printed, and L.4''s hypothesis s (1 - 4/m) > 1 on the band.
     Controls: K = 5 fails (iii); Theorem E's w in place of L.4''s fails (iii) at K = 9; round 4's level-mixed
     comparison (errors at E = lam^(3 - delta) against the margin at lam^(3 + delta), m = 56 M) fails at delta = 1/4.
  H3 (computed, mpmath; layerband5 B3's model with unit constants, env = exp(-1/x), M = 26) The regime map at lam =
     10^-1000 and 10^-3000 with Lemma L.4' (windows: eps_4 <= lam; the remainder lam^(N-5) eps_26 wherever eps_4 <=
     lam, Theorem E's lam^(K-3) elsewhere): K = 6 covers [x_deep, x_top] with no gap.  Control: with Lemma L.4's rule
     (B3's) K = 6 is not covered (B3's result reproduced).
  H4 (exact rationals; the verifier of round 3's M1) Theorem L's conditions (e1)-(e8) at a level lam^p are linear in
     p; they hold at p = 3 + delta and p = P, generic and at the double root rho* (signal lam^3 y^(1 + 2/kappa)), for
     every K in [6, 40], delta in {1/100, 1/20, 1/10, 1/4, 1/2} and P in {50, 200}, under L.4's hypothesis (e6) p (1 -
     M/m) > 3 and under L.4''s p (1 - 4/m) > 1, once m := max(56 M, 4 P M, 4 M/delta) and kappa := max(64, 8 P,
     8/delta).  Control: round 3's m = 56 M, kappa = 64 fail ((e6) at delta = 1/20; (e1), (e2), (e4) at rho*).

Labels: H1, H2 computed (exact; H1 checks the bookkeeping of a deduced lemma, not the lemma); H3 a model with unit
constants.  Run: python3 checks/bandL4p5.py   (about three minutes; imports layerband5.py)
"""
import os
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layerband5 as LB                                                           # noqa: E402


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ H1
def coef_g(j, h):
    """exponent of the size of d^j g_lam's non-seed part, eps_4 <= lam^h: lam^(1-j) eps_j <= lam^(1-j+h); g0's O(1)"""
    return min(Fr(0), Fr(1 - j) + h)


def terms(i, h):
    """(name, e, k): coefficient lam^e times d^k w, in d^i of the remainder's equation"""
    T = []
    for p in range(1, i + 1):                                    # commutator [d^i, g^ab] d_a d_b w
        T.append(("comm p=%d" % p, min(coef_g(p, h), Fr(0)), i - p + 2))
    for p in range(0, i + 1):                                    # d^(i-p) w d^(p+2) g_app
        T.append(("src p=%d" % p, coef_g(p + 2, h), i - p))
    for a in range(0, i + 1):                                    # Q: d^(1+a) g_app d^(1+b) w
        T.append(("Q1 a=%d" % a, coef_g(1 + a, h), 1 + i - a))
    for a in range(0, i + 1):                                    # Q: d^(1+a) g d^(1+b) g d^c w
        for b in range(0, i + 1 - a):
            T.append(("Q2 a=%d b=%d" % (a, b), coef_g(1 + a, h) + coef_g(1 + b, h), i - a - b))
    return T


def admissible(i, h, triangular=True):
    bad = []
    for nm, e, k in terms(i, h):
        need = Fr(max(k, 1) - i - 1) if triangular else Fr(0)
        if e < need:
            bad.append((nm, e, k))
    return bad


def h1(control=False):
    if control:
        weak_holds = all(not admissible(i, Fr(1, 2)) for i in range(3))
        nontri_holds = all(not admissible(i, Fr(1), triangular=False) for i in range(3))
        return weak_holds or nontri_holds
    tri = {i: admissible(i, Fr(1)) for i in range(3)}
    nontri_h = [h for h in (Fr(1), Fr(2), Fr(3)) if all(not admissible(i, h, triangular=False) for i in range(3))]
    ok = all(not b for b in tri.values()) and nontri_h == [Fr(3)]
    out("  H1 triangular ledger at h = 1 (eps_4 <= lam), %d terms over levels 0-2: every term admissible: %s; failures"
        " at h = 1/2: %s; the non-triangular rule first holds at h = %s (Lemma L.4's lam^3)"
        % (sum(len(terms(i, Fr(1))) for i in range(3)), ok,
           [(i, b[0][0]) for i in range(3) for b in [admissible(i, Fr(1, 2))] if b], nontri_h[0] if nontri_h else None))
    return ok


# ------------------------------------------------------------------------------------------------------------ H2
def m_amended(M, delta, P):
    return max(Fr(56*M), Fr(4*P*M), Fr(-(-4*M//delta)))


def ledger_upper_L4p(K, delta=Fr(1, 10), P=50):
    """(i) pointwise: the margin exponent s (2 + 1/m) below every error exponent at the same level s"""
    N = K + 3
    M = 2*N + 8
    m = m_amended(M, delta, P)
    sA = (1 + delta)/(1 - 4/m)
    ok = True
    for s in (sA, 3 - delta):
        marg = s*(2 + 1/m)
        ok &= marg < 3 + s and marg < 4 + s*(1 - M/m) and marg < 1 + 2*s*(1 - M/m) and marg < N - 5 + s*(1 - M/m)
    for s in (delta/2, sA):                      # Theorem E's w = C M lam^(K - 3), and the record's eps_M terms
        marg = s*(2 + 1/m)
        ok &= marg < K - 3 and marg < 3 + s and marg < 4 + s*(1 - M/m) and marg < 1 + 2*s*(1 - M/m)
    return ok and sA <= Fr(K - 3, 2) - delta/2


def band_slacks(K, delta, P=50, w="L4p", mixed=False):
    """(iii) pointwise: least slack of the error exponents over the margin's, on s in [3 - delta, 3 + delta]"""
    N = K + 3
    M = 2*N + 8
    m = Fr(56*M) if mixed else m_amended(M, delta, P)
    sl = {}
    for s in (3 - delta, 3 + delta):
        marg = s*(2 + 1/m) if not mixed else (3 + delta)*(2 + 1/m)
        se = (3 - delta) if mixed else s
        wexp = N - 5 + se*(1 - M/m) if w == "L4p" else Fr(K - 3)
        for nm, e in (("lam^4 eps", 4 + se*(1 - M/m)), ("lam eps^2", 1 + 2*se*(1 - M/m)), ("w", wexp)):
            sl[nm] = min(sl.get(nm, e - marg), e - marg)
        sl["L.4' hypothesis"] = min(sl.get("L.4' hypothesis", s*(1 - 4/m) - 1), s*(1 - 4/m) - 1)
    return sl


DELTAS = (Fr(1, 1000), Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(3, 10), Fr(2, 5), Fr(49, 100))


def h2(control=False):
    if control:
        k5 = min(band_slacks(5, Fr(1, 10)).values()) > 0
        te = min(band_slacks(9, Fr(1, 10), w="thmE").values()) > 0
        mixed = min(band_slacks(6, Fr(1, 4), mixed=True).values()) > 0
        return k5 or te or mixed
    # (i) is monotone in delta ({E >= lam^(3 - delta)} shrinks as delta grows): it is checked at min(delta, 1/4)
    up = all(ledger_upper_L4p(K, min(d, Fr(1, 4)), P) for K in range(6, 41) for d in DELTAS for P in (50, 200))
    up_raw = sorted({(K, str(d)) for K in range(6, 41) for d in DELTAS if not ledger_upper_L4p(K, d)})
    band = True
    gam = {}
    for d in DELTAS:
        for P in (50, 200):
            for K in range(6, 41):
                least = min(band_slacks(K, d, P).values())
                band &= least > 0
                g = min(Fr(1, 10), least/2)
                gam[d] = min(gam.get(d, g), g)
    out("  H2 with Lemma L.4', pointwise, m = max(56 M, 4 P M, 4 M/delta), P in {50, 200}, every K in [6, 40] and delta"
        " in %s: (i) the upper layer (checked at min(delta, 1/4), which implies it at delta): %s (the ledger run at"
        " delta itself fails only at %s); (iii) the band, every error below lam^gamma times the margin at its own"
        " level: %s, with gamma(delta) = %s" % ([str(d) for d in DELTAS], up, up_raw, band,
                                               "; ".join("%s: %s" % (d, float(g)) for d, g in gam.items())))
    return up and band


# ------------------------------------------------------------------------------------------------------------ H3
def regimes_L4p(lam, K, M=26, rule="L4p"):
    N = K + 3
    E = lambda x: mp.exp(-1/x)                                                     # noqa: E731
    PK = LB.PK
    eps = lambda x: sum(abs(PK[i](1/x)) for i in range(M + 1))*E(x)                # noqa: E731
    eps4 = lambda x: sum(abs(PK[i](1/x)) for i in range(5))*E(x)                   # noqa: E731
    sig = lambda x: lam**3*E(x)                                                    # noqa: E731
    m0 = lambda x: (E(x)**2 + x*E(x)**2)/9                                         # noqa: E731
    xb = mp.sqrt(lam)
    lo, hi = xb, mp.mpf('0.5')
    for _ in range(300):
        mid = (lo + hi)/2
        if m0(mid) < 2*lam:
            lo = mid
        else:
            hi = mid
    xtop = lo
    xlow = 1/(10*mp.log(1/lam))
    xs = [xb*(xlow/xb)**(mp.mpf(k)/500) for k in range(500)] + [xlow + (xtop - xlow)*k/3000 for k in range(3001)]
    reg = []
    for x in xs:
        e = eps(x)
        if rule == "L4p":
            hyp = eps4(x) <= lam
        else:
            hyp = e <= lam**3
        errW = lam**4*e + lam*e**2 + lam**(N - 5)*e
        err = errW if hyp else lam**4*e + lam*e**2 + lam**(K - 3)
        if hyp and errW + m0(x) <= sig(x)/10:
            reg.append('W')
        elif sig(x) + err <= m0(x)/10:
            reg.append('S')
        elif err <= min(sig(x), m0(x))/10:
            reg.append('B')
        else:
            reg.append('-')
    first = next((k for k, rr in enumerate(reg) if rr == 'W'), None)
    covered = first is not None and all(rr != '-' for rr in reg[first:])
    return covered, (xs[first] if first is not None else None), xtop


def h3(control=False):
    mp.mp.dps = 40
    if control:
        return regimes_L4p(mp.mpf(10)**-1000, 6, rule="L4")[0]
    rows, ok = [], True
    for e in (1000, 3000):
        lam = mp.mpf(10)**-e
        cov, xdeep, xtop = regimes_L4p(lam, 6)
        ok &= cov
        rows.append("lam = 1e-%d: K = 6 covers [x_deep, x_top] = [%s, %s] with Lemma L.4': %s" % (
            e, mp.nstr(xdeep, 4) if xdeep else '-', mp.nstr(xtop, 4), cov))
    out("  H3 " + "; ".join(rows))
    return ok


# ------------------------------------------------------------------------------------------------------------ H4
def params(K, delta, P, fix=True):
    N = K + 3
    M = 2*N + 8
    if not fix:
        return N, M, 56*M, 64
    m = max(56*M, 4*P*M, -(-4*M//delta))          # ceil(4 M/delta) for a Fraction delta
    kap = max(64, 8*P, -(-8//delta))
    return N, M, int(m), int(kap)


def ledger_window_fix(K, p, delta, P, rho_star, hyp, fix=True):
    """Theorem L's conditions (e1)-(e8) at the level lam^p, generic or at rho* (signal lam^3 y^(1 + 2/kappa))"""
    N, M, m, kap = params(K, delta, P, fix)
    m = Fr(m)
    p = Fr(p)
    e = 1 - M/m
    s = p*(1 + Fr(2, kap)) if rho_star else p
    e6 = p*e > 3 if hyp == "L4" else p*(1 - 4/m) > 1
    return {"e1": 2*p > 3 + s, "e2": 4 + p*e > 3 + s, "e3": 1 + 2*p*e > 3 + s, "e4": N - 5 + p*e > 3 + s,
            "e5": p/m < 1, "e6": e6, "e7": 4 + 2*p*e > 3 + s, "e8": 2*p > 1}


def h4(control=False):
    deltas = (Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2))
    Ps = (50, 200)
    if control:
        # round 3's parameters (m = 56 M, kappa = 64): at least one case must fail (it does: e6 at delta = 1/20, L.4;
        # e2, e4 at rho* for p >= 21)
        return all(all(ledger_window_fix(6, pp, d, P, rs, "L4", fix=False).values())
                   for d in deltas for P in Ps for rs in (False, True) for pp in (3 + d, P))
    bad = []
    for K in range(6, 41):
        for d in deltas:
            for P in Ps:
                for rs in (False, True):
                    for hyp in ("L4", "L4p"):
                        for pp in (3 + d, P):
                            led = ledger_window_fix(K, pp, d, P, rs, hyp)
                            if not all(led.values()):
                                bad.append((K, d, P, rs, hyp, pp, [k for k, vv in led.items() if not vv]))
    old_fail = sorted({k for d in deltas for P in Ps for rs in (False, True) for pp in (3 + d, P)
                       for k, vv in ledger_window_fix(6, pp, d, P, rs, "L4", fix=False).items() if not vv})
    out("  H4 Theorem L's window conditions at every level lam^p, 3 + delta <= p <= P, generic and at rho*, with m ="
        " max(56 M, 4 P M, 4 M/delta) and kappa = max(64, 8 P, 8/delta), every K in [6, 40], delta in {1/100, 1/20,"
        " 1/10, 1/4, 1/2}, P in {50, 200}, under L.4 and under L.4': failures %s; with round 3's m = 56 M, kappa = 64"
        " (K = 6)"
        " the conditions failing somewhere: %s" % (bad if bad else "none", old_fail))
    return not bad


def main():
    ok = True
    for name, f in (("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("bandL4p5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
