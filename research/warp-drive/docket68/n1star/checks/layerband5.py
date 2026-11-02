#!/usr/bin/env python3
"""layerband5.py -- the layer outside the window (EQUALITY5-LAYER.md, Round 3, R3.2 (b)-(d); the verifier's M1).

  B1 (sampled, mpmath) The margin from the running maximum: with E(v) := sup_(v'<=v) env and eps_1(v) := sup_(v'<=v)
     |env'|, int_(v_s)^v env^2 >= E(v)^3/(8 eps_1(v)) (deduced: env >= E/2 on [v_m - E/(2 eps_1), v_m] inside [v_s, v],
     v_m a point where env = E), checked at 400 points for three envelopes: exp(-1/x) sin^2(pi/x) (zeros accumulating at
     the edge), exp(-1/x) cos^2(30 x) (interior zeros), and the record's C_c^inf envelope (the integral by the trapezoid
     rule on a grid of step 1/8000).  So m0 is bounded below
     through E even at the zeros of env.  Control: the same with 8 replaced by 1/8 fails at some point.
  B2 (exact rationals) The exponent ledger of Proposition L.12, with N = K + 3, M = 2N + 8, m = 56 M, delta = gamma =
     1/10: (i) the upper layer E >= lam^(sigma_K - delta), sigma_K := min(3, (K - 3)/2): the margin c E^(2 + 1/m)
     exceeds the signal lam^3 E, lam^4 eps, lam eps^2 (eps <= C E^(1 - M/m)) and Theorem E's |w| <= C M lam^(K-3), for
     every K in [6, 40]; (ii) the windows at every level lam^p, p in [3 + delta, 50]: Theorem L's conditions (e1)-(e8)
     (linear in p; checked at both ends), K = 6; (iii) the band lam^(3+delta) <= E <= lam^(3-delta): every error term is
     below lam^gamma times min(margin, signal) once K >= 10.  Controls: K = 6 with sigma = 3 violates the w-condition of
     (i); p = 3 violates (e6), L.4's hypothesis (the windows do not reach the level lam^3); K = 9 violates (iii).
  B3 (computed, mpmath; unit constants, A = mu0 = 1, |nu d| = 1; env = exp(-1/x) with its exact derivatives) The
     regime map of the layer at lam = 10^-1000 and 10^-3000 (500 log-spaced points below the level lam^10, 3001
     equally spaced above it): windows (errors with Lemma L.4's w-bound below a tenth of the signal, margin below a
     tenth of it, eps_M <= lam^3), spacelike (signal, Theorem E's w and the rest below a tenth of the margin) and the band (errors below a tenth of both); M = M* = 26 derivatives, K = 6 and K = 10.  For
     K = 10 the three regimes cover [x_deep, x_top] with no gap (x_deep: where the proof's error terms with 26
     derivatives fall below the signal; x_top: m0 = 2 lam); for K = 6 a band between is undecided.  x_deep lies far
     above the very edge x_b = lam^(1/2): the record's bounds lose 26 derivatives where the expansion itself loses one
     per order.  Control: at lam = 10^-300 the map is not covered for K = 10: the degree-two error lam eps_26^2 of
     Corollary L.11 exceeds the margin in the upper layer (x^-104 lam > 1 there) -- "lam small enough" is part of the
     statement, and with the record's derivative counts it means lam below about 10^-1000 for this edge.

Labels: B1 sampled (a check of a deduced inequality, not a proof); B2 exact; B3 a model with unit constants (the record's
constants are not evaluated; R3.3).  Run: python3 checks/layerband5.py   (about half a minute)
"""
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


# ------------------------------------------------------------------------------------------------------------ B1
ENVS = {
    "exp(-1/x) sin^2(pi/x)": lambda x: mp.exp(-1/x)*mp.sin(mp.pi/x)**2,
    "exp(-1/x) cos^2(30 x)": lambda x: mp.exp(-1/x)*mp.cos(30*x)**2,
    "record C_c^inf": lambda x: mp.mpf('1.3241')*mp.sin(mp.pi*x/3)**12*mp.exp(1 - 1/((2*x/3)*(2 - 2*x/3))),
}


def b1(control=False):
    mp.mp.dps = 30
    const = Fr(1, 8) if control else Fr(8)
    worst = {}
    for name, f in ENVS.items():
        xs = [mp.mpf(k)/800 for k in range(40, 441)]
        fine = [mp.mpf(k)/8000 for k in range(1, 4411)]
        vals = [f(x) for x in fine]
        dvals = [abs(mp.diff(f, x)) for x in fine]
        cum = [mp.mpf(0)]
        for k in range(1, len(fine)):
            cum.append(cum[-1] + (vals[k - 1]**2 + vals[k]**2)/2*(fine[k] - fine[k - 1]))
        ratio = mp.inf
        for x in xs:
            n = int(x*8000)
            E = max(vals[:n])
            e1 = max(dvals[:n])
            ratio = min(ratio, cum[n - 1]/(E**3/(const*e1)))
        worst[name] = ratio
    if control:
        return all(w >= 1 for w in worst.values())
    out("  B1 min over 400 points of int env^2/(E^3/(8 eps_1)): " + "; ".join(
        "%s %s" % (k, mp.nstr(w, 4)) for k, w in worst.items()))
    return all(w >= 1 for w in worst.values())


# ------------------------------------------------------------------------------------------------------------ B2
def ledger_upper(K, sigma, delta=Fr(1, 10)):
    N = K + 3
    M = 2*N + 8
    m = 56*M
    s = sigma - delta
    return {"u1 signal": s*(1 + Fr(1, m)) < 3, "u2 lam^4 eps": s*(1 + Fr(M + 1, m)) < 4,
            "u3 lam eps^2": s*Fr(2*M + 1, m) < 1, "u4 w (Theorem E)": s*(2 + Fr(1, m)) < K - 3}


def ledger_window(K, p):
    N = K + 3
    M = 2*N + 8
    m = Fr(56*M)
    p = Fr(p)
    e = 1 - M/m
    s = p
    return {"e1": 2*p > 3 + s, "e2": 4 + p*e > 3 + s, "e3": 1 + 2*p*e > 3 + s, "e4": N - 5 + p*e > 3 + s,
            "e5": p/m < 1, "e6": p*e > 3, "e7": 4 + 2*p*e > 3 + s, "e8": 2*p > 1}


def ledger_band(K, delta=Fr(1, 10), gamma=Fr(1, 10)):
    N = K + 3
    M = 2*N + 8
    m = Fr(56*M)
    floor = (3 + delta)*(2 + 1/m) + gamma         # min(margin, signal) >= lam^((3 + delta)(2 + 1/m)), times lam^gamma
    return {"b1 lam^4 eps": 4 + (3 - delta)*(1 - M/m) > floor, "b2 lam eps^2": 1 + 2*(3 - delta)*(1 - M/m) > floor,
            "b3 w": K - 3 > floor}


def b2(control=False):
    if control:
        c1 = all(ledger_upper(6, Fr(3)).values())
        c2 = all(ledger_window(6, 3).values())
        c3 = all(ledger_band(9).values())
        return c1 or c2 or c3
    up = all(all(ledger_upper(K, min(Fr(3), Fr(K - 3, 2))).values()) for K in range(6, 41))
    win = all(all(ledger_window(6, p).values()) for p in (Fr(31, 10), Fr(50)))
    band = all(all(ledger_band(K).values()) for K in range(10, 41))
    out("  B2 (i) upper layer, every K in [6, 40] at sigma_K: %s; (ii) windows at p = 31/10 and 50 (K = 6): %s;"
        " (iii) band, every K in [10, 40]: %s; at K = 9: %s" % (up, win, band, ledger_band(9)))
    return up and win and band


# ------------------------------------------------------------------------------------------------------------ B3
U = sp.Symbol('u')


def polys(K):
    Ps = [sp.Integer(1)]
    for _ in range(K):
        Ps.append(sp.expand(U**2*(Ps[-1] - sp.diff(Ps[-1], U))))
    return [sp.lambdify(U, p, 'mpmath') for p in Ps]


PK = polys(27)


def regimes(lam, K, M=26):
    """the regime of each point of a log grid of x in the layer, for env = exp(-1/x), unit constants"""
    N = K + 3
    E = lambda x: mp.exp(-1/x)                                                       # noqa: E731
    eps = lambda x: sum(abs(PK[i](1/x)) for i in range(M + 1))*E(x)                  # eps_M(x), the sup at x near 0
    sig = lambda x: lam**3*E(x)                                                      # noqa: E731
    m0 = lambda x: (E(x)**2 + x*E(x)**2)/9                                           # noqa: E731
    xb = mp.sqrt(lam)
    # the top of the layer: m0 = 2 lam
    lo, hi = xb, mp.mpf('0.5')
    for _ in range(300):
        mid = (lo + hi)/2
        if m0(mid) < 2*lam:
            lo = mid
        else:
            hi = mid
    xtop = lo
    xlow = 1/(10*mp.log(1/lam))                       # the level lam^10
    xs = [xb*(xlow/xb)**(mp.mpf(k)/500) for k in range(500)] + [xlow + (xtop - xlow)*k/3000 for k in range(3001)]
    reg = []
    for x in xs:
        e = eps(x)
        errL4 = lam**4*e + lam*e**2 + lam**(N - 5)*e
        errE = lam**4*e + lam*e**2 + lam**(K - 3)
        if e <= lam**3 and errL4 + m0(x) <= sig(x)/10:
            reg.append('W')
        elif sig(x) + errE <= m0(x)/10:
            reg.append('S')
        elif errE <= min(sig(x), m0(x))/10:
            reg.append('B')
        else:
            reg.append('-')
    first = {c: next((xs[k] for k, r in enumerate(reg) if r == c), None) for c in 'WBS'}
    xdeep = first['W']
    covered = None
    if xdeep is not None:
        k0 = xs.index(xdeep)
        covered = all(r != '-' for r in reg[k0:])
    x31 = 1/(mp.mpf('3.1')*mp.log(1/lam))
    return {'xb': xb, 'xdeep': xdeep, 'x31': x31, 'xtop': xtop, 'first': first, 'covered': covered}


def b3(control=False):
    mp.mp.dps = 40
    if control:
        r = regimes(mp.mpf(10)**-300, 10)
        return r['covered'] is True
    rows, ok = [], True
    for e in (1000, 3000):
        lam = mp.mpf(10)**-e
        r10, r6 = regimes(lam, 10), regimes(lam, 6)
        good = (r10['covered'] is True and r6['covered'] is False and r10['xdeep'] is not None
                and r10['xb'] < r10['xdeep'] < r10['x31'] < r10['xtop'])
        ok &= good
        rows.append("lam = 1e-%d: x_b = %s, x_deep = %s, level lam^3.1 at x = %s, x_top = %s; K = 10 covers"
                    " [x_deep, x_top]: %s (first W, B, S at %s); K = 6 covers it: %s" % (
                        e, mp.nstr(r10['xb'], 3), mp.nstr(r10['xdeep'], 4), mp.nstr(r10['x31'], 4),
                        mp.nstr(r10['xtop'], 4), r10['covered'],
                        ", ".join(mp.nstr(r10['first'][c], 4) if r10['first'][c] else '-' for c in 'WBS'),
                        r6['covered']))
    out("  B3 " + "; ".join(rows))
    return ok


def main():
    ok = True
    for name, f in (("B1", b1), ("B2", b2), ("B3", b3)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("layerband5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
