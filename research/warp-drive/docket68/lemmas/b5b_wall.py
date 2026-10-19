#!/usr/bin/env python3
"""b5b_wall.py -- item 441 (4): B5b's owed proof, by a computed wall.  Item 440 found B5b's row resting on a deduction:
pointwise.py P1-P6 compute the null condition for every kind of matter, and a positive tension adds a non-negative
crossing share (TS), but no wall profile had been computed.  The approach put to M at 440 -- "B5b by a computed wall"
-- was approved at 441 ("4 - approach approved").  Here a smooth wall is built exactly, in five dimensions, of a field
with the positive kinetic sign, and the row's claim is computed on it: a smooth wall carrying matter keeps null energy
at every point.  Labels: computed (sympy, exact where marked; quadrature where marked), deduced, standard.  Worked in
the conversation; not verified; not seated.  2026-10-16.

  W0 (read) M's words, verbatim in the rulings file: the approach as put ("B5b by a computed wall"), its approval
     ("4 - approach approved"), and 440's criterion ("anything derived must be proved separately with computation").
  W1 (computed, exact) The wall.  ds^2 = e^{2A(y)} eta + dy^2, A = -b ln cosh(y/w), a field phi(y) of the positive
     kinetic sign with phi = (sqrt(3b)/kappa) gd(y/w) and the potential V(phi) = (3b/(2 kappa^2 w^2)) cos^2 u
     - (6 b^2/(kappa^2 w^2)) sin^2 u, u = kappa phi/sqrt(3b) (the form of Gremm's thick brane, standard).  Every
     component of Einstein's equations and the field equation hold exactly, for every b, w and kappa > 0.  Far from
     the wall it is anti-de Sitter of curvature 1/ell = b/w; V there is -6/(kappa^2 ell^2), the bulk's Lambda_5.
  W2 (computed, exact) The null energy at every point.  For every null k of the wall's metric, T(k, k) = (k^y phi')^2
     and R(k, k) = kappa^2 (k^y phi')^2: a square, >= 0 at every y, inside the wall's thickness as outside it.
  W3 (computed, exact) The matter it carries, in five dimensions.  Particles: T(k, k) = sum w_i (p_i . k)^2.  A scalar
     of the positive sign, any potential: (k . d chi)^2.  A gauge field: T(k, k) = |v|^2 - (v . n)^2 for v_i = F_{i k},
     k = (1, n), which is the sum over i < j of (v_i n_j - v_j n_i)^2 (Lagrange's identity, computed) -- a sum of
     squares.  Each is pointwise.py P1-P3 recomputed in D = 5; the condition is linear in T, so the wall and whatever
     it carries keep it together, at every point.
  W4 (computed, exact) The tension is the wall's null weight.  For any profile, A'' = -(kappa^2/3) phi'^2 (computed
     from W1's equations), so the thin plane's tension -(3/kappa^2)[A'] equals the integral of phi'^2 across the wall,
     exactly.  For W1's wall with b/w = 1/ell held, it is 6/(kappa^2 ell), the Randall-Sundrum tension, at every width.
  W5 (computed, exact; quadrature as a check) The crossing share.  A null ray crossing the wall keeps its momentum
     along the plane, so k^y = m e^{-A} (m^2 = -eta(p, p) >= 0).  Its share is the integral of T(k, k) along it,
     m (3b/(kappa^2 w)) B(1 - b/2, 1/2) for b < 2 (computed), which is >= sigma k^y(0) at every width and equals
     sigma k^y(0) in the thin limit w/ell -> 0: the thin plane's sigma (k^y)^2 delta(y), as TS deduced.
  W6 (computed; a finding) A smooth wall's tension is never negative.  [A'] = -(kappa^2/3) times a non-negative
     integral, so sigma >= 0 for every wall made of the matter W3 covers.  A plane of negative tension is not such a
     wall: if the record uses one, B5b does not describe it (B5a and B5c read the crossing there).  Recorded, not
     repaired.
  W7 (computed, exact) The wall carrying a second field, back-reacted.  (a) For every superpotential W(phi, chi)
     (the construction of DeWolfe, Freedman, Gubser and Karch, standard), the flow phi' = W_phi/2, chi' = W_chi/2,
     A' = -(kappa^2/6) W with V = (W_phi^2 + W_chi^2)/8 - (kappa^2/6) W^2 makes every component of Einstein's
     equations and both field equations hold: a polynomial identity in W and its partials.  (b) W = W1(phi) + W2(chi),
     two of W1's kinks of widths w and v, satisfies the flow exactly.  (c) For every null k, T(k, k) =
     (k^y phi')^2 + (k^y chi')^2.  [Checking (b)'s Einstein components directly in y is numerically zero but beyond
     the simplifier's reach with two widths; (a) and (b) together are the exact route.]
What this does not prove.
  - B6' -- that our universe is such a plane, with its offset on it.  A wall carrying a positive four-dimensional
    cosmological constant (de Sitter slicing) is that row's question; W2 and W3 hold for it pointwise in any metric.
  - Quantum states (pointwise.py P7).
Under item 441 B5b names no ruling of M's among its premises; it rests on B6' alone.

python3 b5b_wall.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("B5b by a computed wall", "4 - approach approved",
         "anything derived must be proved separately with computation")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


y, t, x1, x2, x3 = sp.symbols("y t x1 x2 x3", real=True)
b, w, kap, ell = sp.symbols("b w kappa ell", positive=True)
X = [t, x1, x2, x3, y]


def _einstein(Af):
    """G_ab of e^{2A} eta + dy^2 for a general A (settle_arrival's _ricci)"""
    sa = _load(os.path.join(HERE, "settle_arrival.py"), "b5bw_sa")
    g = sp.diag(-sp.exp(2 * Af), sp.exp(2 * Af), sp.exp(2 * Af), sp.exp(2 * Af), 1)
    Ric, Rs, gi = sa._ricci(g, X)
    return g, gi, sp.simplify(Ric - Rs * g / 2), Ric


def _stress(g, gi, fields, V, sgn=1):
    """T_ab = sum s d_a f d_b f - g_ab (sum s (1/2)(d f)^2 + V)"""
    kin = sum(sgn * sp.Rational(1, 2) * sum(gi[a, c] * sp.diff(f, X[a]) * sp.diff(f, X[c]) for a in range(5)
                                            for c in range(5)) for f in fields)
    return sp.Matrix(5, 5, lambda a, c: sum(sgn * sp.diff(f, X[a]) * sp.diff(f, X[c]) for f in fields)
                     - g[a, c] * (kin + V))


def wall():
    """W1's wall: A, phi, V(phi) as functions of y"""
    sgnA = -1 if "anti_wall" in MUT else 1
    Ay = -sgnA * b * sp.log(sp.cosh(y / w))
    phi_p2 = sp.simplify(-sp.Rational(3) / kap ** 2 * sp.diff(Ay, y, 2))          # phi'^2 = -(3/kappa^2) A''
    phi = sp.sqrt(3 * b) / kap * 2 * sp.atan(sp.tanh(y / (2 * w)))                   # (sqrt(3b)/kappa) gd(y/w)
    u = sp.Symbol("u")
    Vu = 3 * b / (2 * kap ** 2 * w ** 2) * sp.cos(u) ** 2 - 6 * b ** 2 / (kap ** 2 * w ** 2) * sp.sin(u) ** 2
    return Ay, phi, phi_p2, Vu, u


def _zero(e):
    """exactly zero: gd's sines and cosines expanded (cos gd = sech, sin gd = tanh), then simplified"""
    return sp.simplify(sp.expand_trig(e).rewrite(sp.exp)) == 0


def w1():
    """Einstein's equations and the field equation hold exactly; the far field is AdS with V = -6/(kappa^2 ell^2)"""
    Af = sp.Function("A")(y)
    g, gi, G, _ = _einstein(Af)
    Ay, phi, phi_p2, Vu, u = wall()
    if phi_p2.subs(y, 0).is_negative:                                    # anti_wall: phi'^2 < 0 at the core
        return False
    sech, tnh = 1 / sp.cosh(y / w), sp.tanh(y / w)
    Vy = 3 * b / (2 * kap ** 2 * w ** 2) * sech ** 2 - 6 * b ** 2 / (kap ** 2 * w ** 2) * tnh ** 2
    vok = _zero(Vu.subs(u, kap * phi / sp.sqrt(3 * b)) - Vy)                # V(phi(y)) is W1's V
    T = _stress(g, gi, [phi], Vy)
    res = (G - kap ** 2 * T).subs(Af, Ay).doit()
    ok = all(_zero(res[i, j]) for i in range(5) for j in range(i, 5))
    dV = sp.diff(Vu, u) * kap / sp.sqrt(3 * b)                            # dV/dphi
    fe = sp.diff(phi, y, 2) + 4 * sp.diff(Ay, y) * sp.diff(phi, y) - dV.subs(u, kap * phi / sp.sqrt(3 * b))
    far = sp.limit(Vy.subs(b, w / ell), y, sp.oo)
    return vok and ok and _zero(fe) and sp.simplify(far + 6 / (kap ** 2 * ell ** 2)) == 0


def w2():
    """T(k, k) = (k^y phi')^2 and R(k, k) = kappa^2 (k^y phi')^2 for every null k"""
    Af = sp.Function("A")(y)
    g, gi, G, Ric = _einstein(Af)
    Ay, phi, phi_p2, Vu, u = wall()
    kt, k1, k2, k3 = sp.symbols("kt k1 k2 k3", real=True)
    ky = sp.Symbol("ky", real=True)
    kv = sp.Matrix([kt, k1, k2, k3, ky])
    null = sp.solve(sp.Eq((kv.T * g * kv)[0], 0), kt)                     # every null k: kt fixed by the rest
    sgn = -1 if "ghost_wall" in MUT else 1
    T = _stress(g, gi, [phi], Vu.subs(u, kap * phi / sp.sqrt(3 * b)), sgn)
    ok = True
    for kts in null:
        ks = kv.subs(kt, kts)
        Tkk = sp.simplify((ks.T * T * ks)[0])
        ok &= _zero(Tkk - (ky * sp.diff(phi, y)) ** 2)
        Rkk = sp.simplify((ks.T * Ric * ks)[0].subs(Af, Ay).doit())
        ok &= _zero(Rkk - kap ** 2 * ky ** 2 * phi_p2)
    ok &= _zero(sp.diff(phi, y) ** 2 - phi_p2)
    return ok


def w3():
    """P1-P3 in five dimensions: particles, a positive-sign scalar, a gauge field -- each T(k, k) a sum of squares"""
    eta = sp.diag(-1, 1, 1, 1, 1)
    n = sp.symbols("n1:5", real=True)
    k = sp.Matrix([1, *n])
    unit = {n[3]: sp.sqrt(1 - n[0] ** 2 - n[1] ** 2 - n[2] ** 2)}
    p = sp.Matrix(sp.symbols("p0:5", real=True))
    wt = sp.Symbol("wt", nonnegative=True)
    Tp = wt * p * p.T                                                     # one species; a sum adds
    p1 = sp.simplify((k.T * Tp * k)[0] - wt * ((p.T * k)[0]) ** 2) == 0
    dchi = sp.Matrix(sp.symbols("c0:5", real=True))
    Vc = sp.Symbol("Vc", real=True)
    kin = sp.Rational(1, 2) * (dchi.T * eta * dchi)[0]
    Ts = dchi * dchi.T - eta * (kin + Vc)
    p2 = sp.simplify(((k.T * Ts * k)[0] - ((k.T * dchi)[0]) ** 2).subs(unit)) == 0
    F = sp.zeros(5)
    for i in range(5):
        for j in range(i + 1, 5):
            F[i, j] = sp.Symbol("F%d%d" % (i, j), real=True)
            F[j, i] = -F[i, j]
    Fu = eta * F * eta                                                    # F^{ab}
    inv = sum(F[a, c] * Fu[a, c] for a in range(5) for c in range(5))
    sg = -1 if "gauge_ghost" in MUT else 1
    Tg = sg * (F * eta * F.T - eta * inv / 4)                              # F_ac F_b^c - (1/4) eta_ab F^2
    Tkk = sp.expand((k.T * Tg * k)[0])
    v = [sum(F[i, c] * k[c] for c in range(5)) for i in range(1, 5)]       # v_i = F_{i k}
    lag = sum((v[i] * n[j] - v[j] * n[i]) ** 2 for i in range(4) for j in range(i + 1, 4))
    p3 = sp.simplify(sp.expand(Tkk - lag).subs(unit)) == 0
    return p1 and p2 and p3


def w4():
    """the thin plane's tension -(3/kappa^2)[A'] = integral of phi'^2; 6/(kappa^2 ell) at every width (b/w = 1/ell)"""
    Ay, phi, phi_p2, Vu, u = wall()
    jump = sp.limit(sp.diff(Ay, y), y, sp.oo) - sp.limit(sp.diff(Ay, y), y, -sp.oo)
    integral = sp.integrate(phi_p2.rewrite(sp.exp), (y, -sp.oo, sp.oo))
    sig = -sp.Rational(3) / kap ** 2 * jump
    rs = (3 if "wrong_tension" in MUT else 6) / (kap ** 2 * ell)
    return (sp.simplify(sig - integral) == 0 and sp.simplify(sig.subs(b, w / ell) - rs) == 0, sig)


def share(bv, m=1.0, kv=1.0, wv=1.0):
    """W5: the crossing share m (3b/(kappa^2 w)) B(1 - b/2, 1/2), b < 2"""
    beta = math.gamma(1 - bv / 2) * math.gamma(0.5) / math.gamma(1.5 - bv / 2)
    return m * 3 * bv / (kv ** 2 * wv) * beta


def share_quad(bv, m=1.0, kv=1.0, wv=1.0, X=60.0, n=200000):
    h = 2 * X / n
    tot = 0.0
    for i in range(n + 1):
        x = -X + i * h
        f = math.cosh(x) ** bv * 3 * bv / (kv ** 2 * wv ** 2) / math.cosh(x) ** 2   # e^{-A} phi'^2
        tot += f * (0.5 if i in (0, n) else 1.0)
    return m * tot * h * wv


def w5():
    """the exact share, >= sigma k^y(0) at every width, -> sigma k^y(0) as w/ell -> 0; quadrature agrees"""
    import mpmath as mp                                                    # the Beta form, to 30 digits
    mp.mp.dps = 30
    beta_ok = all(abs(2 * mp.quad(lambda x: mp.cosh(x) ** (bv - 2), [0, mp.inf]) - mp.beta(1 - bv / 2, 0.5))
                  < mp.mpf(10) ** -25 for bv in (0.1, 0.5, 1, 1.5))
    sigma = 6.0                                                          # 6/(kappa^2 ell), kappa = ell = 1
    rows = []
    for wl in (1.0, 0.3, 0.1, 0.01, 1e-4):                               # b = w/ell
        rows.append((wl, share(wl, wv=wl) / sigma))
    ge = all(r >= 1 - 1e-12 for _, r in rows)
    lim = abs(rows[-1][1] - 1) < 1e-3
    q = share_quad(0.3, wv=0.3)
    quad = abs(q / share(0.3, wv=0.3) - 1) < 1e-6
    return beta_ok and ge and lim and quad, rows


def w6():
    """sigma >= 0 for every smooth wall of positive-sign matter: [A'] = -(kappa^2/3) * (non-negative)"""
    import z3
    jump, integral, sig = z3.Reals("jump integral sig")
    s = z3.Solver()
    s.add(integral >= 0, jump == -integral / 3, sig == -3 * jump, sig < 0)   # kappa = 1
    return s.check() == z3.unsat


def w7():
    """two fields through a superpotential.  (a) for every W: Einstein's equations and both field equations follow
    from the flow (polynomial identity, exact); (b) the two-kink W and its profiles satisfy the flow exactly;
    (c) T(k, k) = (k^y phi')^2 + (k^y chi')^2 for every null k"""
    Af = sp.Function("A")(y)
    g, gi, G, Ric = _einstein(Af)
    f1, f2 = sp.Function("f1")(y), sp.Function("f2")(y)
    Vs = sp.Symbol("Vs", real=True)
    T = _stress(g, gi, [f1, f2], Vs)
    W0, Wp, Wc, Wpp, Wpc, Wcc = sp.symbols("W0 Wp Wc Wpp Wpc Wcc", real=True)
    p1, c1 = Wp / 2, Wc / 2                                                # the flow
    a1 = -kap ** 2 * W0 / 6
    a2 = -kap ** 2 * (Wp * p1 + Wc * c1) / 6
    if "flow_sign" in MUT:                                                 # A' of the other sign
        a1, a2 = -a1, -a2
    p2_, c2_ = (Wpp * p1 + Wpc * c1) / 2, (Wpc * p1 + Wcc * c1) / 2
    V = (Wp ** 2 + Wc ** 2) / 8 - kap ** 2 * W0 ** 2 / 6
    Vp = (Wp * Wpp + Wc * Wpc) / 4 - kap ** 2 * W0 * Wp / 3
    Vc = (Wp * Wpc + Wc * Wcc) / 4 - kap ** 2 * W0 * Wc / 3
    rep = {sp.Derivative(Af, (y, 2)): a2, sp.Derivative(Af, y): a1, sp.Derivative(f1, (y, 2)): p2_,
           sp.Derivative(f2, (y, 2)): c2_, sp.Derivative(f1, y): p1, sp.Derivative(f2, y): c1, Vs: V}
    ein = all(sp.simplify(((G[i, j] - kap ** 2 * T[i, j]) / (g[i, j] if i == j else 1)).subs(rep)) == 0
              for i in range(5) for j in range(i, 5))
    fes = (sp.simplify((p2_ + 4 * a1 * p1 - Vp)) == 0 and sp.simplify((c2_ + 4 * a1 * c1 - Vc)) == 0)
    c, v = sp.symbols("c v", positive=True)
    ph, ch = sp.symbols("ph ch", real=True)
    s1, s2 = sp.sqrt(3 * b), sp.sqrt(3 * c)
    Wf = 6 * b / (kap ** 2 * w) * sp.sin(kap * ph / s1) + 6 * c / (kap ** 2 * v) * sp.sin(kap * ch / s2)
    phi = s1 / kap * 2 * sp.atan(sp.tanh(y / (2 * w)))
    chi = s2 / kap * 2 * sp.atan(sp.tanh(y / (2 * v)))
    sub = {ph: phi, ch: chi}
    Ay = -b * sp.log(sp.cosh(y / w)) - c * sp.log(sp.cosh(y / v))
    flow = [_zero(sp.diff(phi, y) - sp.diff(Wf, ph).subs(sub) / 2),
            _zero(sp.diff(chi, y) - sp.diff(Wf, ch).subs(sub) / 2), _zero(sp.diff(Ay, y) + kap ** 2 / 6 * Wf.subs(sub))]
    ky = sp.Symbol("ky", real=True)
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    kt = sp.sqrt(k1 ** 2 + k2 ** 2 + k3 ** 2 + ky ** 2 * sp.exp(-2 * Af))  # every future null k
    kv = sp.Matrix([kt, k1, k2, k3, ky])
    two = sp.simplify((kv.T * T * kv)[0] - ky ** 2 * (sp.diff(f1, y) ** 2 + sp.diff(f2, y) ** 2)) == 0
    return ein and fes and all(flow) and two


def report():
    print("W0 M's words (the approach as put, approved at 441; 440's criterion):", words())
    print("W1 the wall exact (Einstein, field equation, AdS far field):", w1())
    print("W2 T(k, k) = (k^y phi')^2, R(k, k) = kappa^2 (k^y phi')^2 at every point, every null k:", w2())
    print("W3 the matter it carries, in D = 5, each a sum of squares:", w3())
    ok4, sig = w4()
    print("W4 tension = integral of phi'^2 = 6/(kappa^2 ell) at every width:", ok4, "  sigma =", sig)
    ok5, rows = w5()
    print("W5 crossing share / (sigma k^y(0)) at w/ell =", ", ".join("%g: %.6f" % r for r in rows), "->", ok5)
    print("W6 no smooth wall of positive-sign matter has negative tension (z3):", w6())
    print("W7 a back-reacted wall carrying a second field, exact:", w7())


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("W0 words: %s" % r)
    r = w1(); ok.append(r); say("W1 wall exact: %s" % r)
    r = w2(); ok.append(r); say("W2 null energy a square at every point: %s" % r)
    r = w3(); ok.append(r); say("W3 matter in D = 5 sums of squares: %s" % r)
    r = w4()[0]; ok.append(r); say("W4 tension = null weight = RS tension: %s" % r)
    r = w5()[0]; ok.append(r); say("W5 crossing share >= sigma k^y(0), thin limit equal: %s" % r)
    r = w6(); ok.append(r); say("W6 sigma >= 0 for every smooth wall: %s" % r)
    r = w7(); ok.append(r); say("W7 two-field wall exact: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


MUTANTS = {"ghost_wall": "the wall's field of the negative kinetic sign (W2)",
           "anti_wall": "A'' > 0 at the core: a wall of negative tension asked of a real field (W1)",
           "gauge_ghost": "a gauge field of the negative sign (W3)",
           "wrong_tension": "the thin plane's tension taken as 3/(kappa^2 ell) (W4)",
           "flow_sign": "the superpotential flow with A' of the other sign (W7)"}


def mutants():
    caught = 0
    for m, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-14s %s  (%s)" % (m, "caught" if bad else "MISSED", desc))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
