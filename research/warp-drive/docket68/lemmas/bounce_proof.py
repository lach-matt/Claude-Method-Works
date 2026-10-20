#!/usr/bin/env python3
"""bounce_proof.py -- item 538: the steps of BOUNCE-PROOF.md that a machine checks.  M: "What still rests beyond
established physics - let's work these out. If we cannot prove them, we can at least build them and compute them as
COMPUTED-THEORIZED."; "anything COMPUTED-THEORIZED should have a complete proof for the computations".  The proof of
the quantum bounce (QB) is written in BOUNCE-PROOF.md; bounce_qm.py and bounce_close.py check its exact algebra and its
grid; this instrument checks the identities the written proof adds, and the theorem that removes the second premise:
no row depends on where the bounce sits, provided it sits well inside the horizon.  Labels: computed (exact unless
marked), deduced, READ, M's.  Worked in the conversation; not verified; not seated.  2026-10-20.

  P0 (M's) 538.
  P1 (computed, exact) The minisuperspace metric 12 Y dxi dY is dxi dw with w = 6 Y^2: null coordinates of the flat
     plane, so its curvature vanishes and the Laplace-Beltrami operator is (1/3Y) d_xi d_Y with no curvature term.
  P2 (computed; the series proof checked) The integral that carries every expectation value:
     int |y|^a exp(-s^2 (y+T)^2) dy = Gamma((1+a)/2) s^(-1-a) 1F1(-a/2, 1/2, -s^2 T^2), proved in BOUNCE-PROOF L6 by
     expanding the cosh and Kummer's transformation; checked against quadrature to 1e-20 for a = 1/2, 1, 2.
  P3 (computed) Monotone in |T|: d/dz 1F1(-a/2, 1/2, -z) = a 1F1(1 - a/2, 3/2, -z) = a e^(-z) 1F1((1+a)/2, 3/2, z) > 0
     (every coefficient of the last series positive), checked numerically.
  P4 (computed) The departure before the bounce: 1F1(-1/4, 1/2, -z) Gamma(3/4)/(Gamma(1/2) z^(1/4)) = 1 - 1/(16z)
     + O(z^-2) (DLMF 13.7.1, the second sum; the sign negative), checked at z = 1e2 to 1e4.
  P5 (computed, exact) The effective metric's Kretschmann scalar is a polynomial in xi, xi', xi'' and the Y-derivatives
     over a power of Y alone: it is finite wherever Y > 0, the horizons xi = 0 included, and <Y> >= <Y>(0) > 0 by P3.
  P6 (computed) The place does not matter.  For every bounce well inside the horizon (x_b from 0.3 to 100, against the
     horizon's x_h = 8.5e-10 here), the state keeps its probability, comes out a white hole of the same mass, has
     exactly two horizons, a curvature maximum 0.7424 x_b^2 l5^-4 (bounded), a proper time across 2 r_h to within
     0.3 Y_min/r_h^2 (plus the state's own width, 3 (sigma_k/k_c)^2), and departs from the classical radius before
     the bounce by 0.2736 (x/x_b)^2 <= x.  So no row needs
     x_b = 1: it needs x_b >> x_h, which effective field theory with order-one coefficients gives (x_b >= 0.27;
     Donoghue, READ) -- naturalness, its coefficients unmeasured -- and the candidate theory gives (x_b = 1).

python3 bounce_proof.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
mp.mp.dps = 30


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


BQ = _load("bounce_qm.py", "bp_bq")


def flat():
    """P1"""
    xi, Y = sp.symbols("xi Y", positive=True)
    w = 6 * Y ** 2
    return sp.simplify(sp.diff(w, Y) - 12 * Y) == 0


def integral():
    """P2"""
    err = 0
    for a in (mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2)):
        for s in (mp.mpf("0.3"), mp.mpf(2)):
            for T in (mp.mpf(0), mp.mpf("0.7"), mp.mpf(-3)):
                pts = sorted(set([mp.mpf(0), -T]))
                q = mp.quad(lambda y: abs(y) ** a * mp.e ** (-(s * (y + T)) ** 2), [-mp.inf] + pts + [mp.inf])
                cf = mp.gamma((1 + a) / 2) * s ** (-1 - a) * mp.hyp1f1(-a / 2, 0.5, -(s * T) ** 2)
                if "integral" in MUT:
                    cf = mp.gamma((1 + a) / 2) * s ** (-1 - a) * mp.hyp1f1(-a / 2, 0.5, (s * T) ** 2)
                # the series route: e^-z 1F1((a+1)/2, 1/2, z) (Kummer) gives the same
                z = (s * T) ** 2
                ser = mp.gamma((1 + a) / 2) * s ** (-1 - a) * mp.e ** (-z) * mp.hyp1f1((a + 1) / 2, 0.5, z)
                err = max(err, abs(q / cf - 1), abs(ser / cf - 1))
    return err


def monotone():
    """P3"""
    ok = True
    for a in (mp.mpf(1) / 2, mp.mpf(1)):
        for z in (mp.mpf("0.01"), mp.mpf(1), mp.mpf(30), mp.mpf(1000)):
            d = mp.diff(lambda zz: mp.hyp1f1(-a / 2, 0.5, -zz), z)
            f1 = a * mp.hyp1f1(1 - a / 2, 1.5, -z)
            f2 = a * mp.e ** (-z) * mp.hyp1f1((1 + a) / 2, 1.5, z)
            ok = ok and abs(d / f1 - 1) < 1e-15 and abs(f2 / f1 - 1) < 1e-15 and f1 > 0
    return ok


def asymptotic():
    """P4"""
    rows = []
    for z in (mp.mpf(100), mp.mpf(1000), mp.mpf(10000)):
        v = mp.hyp1f1(-mp.mpf(1) / 4, 0.5, -z) * mp.gamma(0.75) / (mp.gamma(0.5) * z ** 0.25)
        rows.append((v - 1) * z)
    return rows


def kretschmann_form():
    """P5: the denominator of K is a power of Y alone"""
    T, z, c, th, ph = sp.symbols("T z chi theta phi")
    xi, Y = sp.Function("xi")(T), sp.Function("Y")(T)
    X = (T, z, c, th, ph)
    g = sp.diag(-1 / (4 * xi * Y ** 2), xi / Y, Y, Y * sp.sin(c) ** 2, Y * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi, G, riem = BQ._curv(g, X)
    K = 0
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                for d in range(cc + 1, 5):
                    r = sp.simplify(riem(a, b, cc, d))
                    if r != 0:
                        K += 2 * g[a, a] * gi[b, b] * gi[cc, cc] * gi[d, d] * r ** 2
    s = sp.symbols("x0 x1 x2 y0 y1 y2")
    K = sp.simplify(K.subs({sp.sin(c): 1, sp.sin(th): 1}))
    K = K.subs({sp.diff(xi, T, 2): s[2], sp.diff(Y, T, 2): s[5]}).subs({sp.diff(xi, T): s[1], sp.diff(Y, T): s[4]})
    K = sp.together(sp.expand(K.subs({xi: s[0], Y: s[3]})))
    num, den = sp.fraction(K)
    den_free = not den.has(s[0]) and not den.has(s[1]) and not den.has(s[2])
    poly_y = sp.Poly(den, s[3]).is_monomial if den.has(s[3]) else True
    return dict(den_free_of_xi=den_free, den_monomial_in_Y=poly_y, den=str(sp.factor(den)))


def place():
    """P6: the row-relevant properties for bounces from x_b = 0.3 to 100, l5 = 1, mu = 1e10 (code units)"""
    Kf = BQ.kretschmann_eff()
    base = dict(kc=300.0, sk=0.5, Lc=0.0, xi0=1e6)
    kv = {a: BQ.kav(a, base) for a in (0.5, -1, -1.5)}
    mu = base["xi0"] * BQ.kav(2, base) / 9
    xh = math.sqrt(72) / mu                                     # x at the horizon, Y = mu, l5 = 1
    rows = []
    for xb in (0.3, 1.0, 3.0, 10.0, 100.0):
        Ymin = (math.sqrt(72) * mu / xb) ** 0.5                 # x_b = sqrt(72) mu / Y_min^2
        sg = (2.0 / 3) * float(kv[0.5]) ** 2 * math.gamma(0.75) ** 2 / (math.pi * Ymin ** 2)
        if "place_sigma" in MUT:
            sg *= 1e12
        p = dict(base, sg=sg)
        xf = lambda T: BQ.xicf(T, p, kv); yf = lambda T: BQ.Ycf(T, p, kv)
        Y0 = yf(0)
        Th = mp.findroot(xf, 3 * mu ** 2 / (2 * p["kc"]))
        zeros = (xf(0) > 0) and (xf(2 * Th) < 0) and (xf(-2 * Th) < 0)
        d = [mp.diff(xf, 0, n) for n in (0, 1, 2)] + [mp.diff(yf, 0, n) for n in (0, 1, 2)]
        Kr = abs(Kf(*d)) / (72 * mu ** 2 / Y0 ** 4)
        tau = 2 * mp.quad(lambda T: 1 / (2 * mp.sqrt(xf(T)) * yf(T)), [0, Th / 1e6, Th / 1e3, Th / 8, Th / 2, Th])
        # the departure before the bounce at x = x_b/10
        Tq = 3 * (Ymin * math.sqrt(10)) ** 2 / (2 * p["kc"])
        Ycl = mp.sqrt(mp.mpf(2) / 3) * kv[0.5] * mp.sqrt(Tq)
        dev = abs(yf(Tq) / Ycl - 1)
        rows.append(dict(xb=xb, xb_meas=math.sqrt(72) * mu / Y0 ** 2, Ymin_mu=Y0 / mu, zeros=zeros,
                         sym=abs(xf(Th / 2) - xf(-Th / 2)) == 0,
                         Kr=Kr, tau=tau / (2 * mp.sqrt(mu)), dev=dev, x=xb / 10))
    return dict(rows=rows, xh=xh)


def compute():
    return dict(flat=flat(), integral=integral(), monotone=monotone(), asym=asymptotic(), K=kretschmann_form(),
                place=place())


def checks(o):
    p1 = o["flat"]
    p2 = o["integral"] < 1e-20
    p3 = o["monotone"]
    p4 = all(abs(r + mp.mpf(1) / 16) < 0.03 for r in o["asym"]) and abs(o["asym"][-1] + mp.mpf(1) / 16) < 1e-3
    p5 = o["K"]["den_free_of_xi"] and o["K"]["den_monomial_in_Y"]
    pl = o["place"]
    p6 = all(r["zeros"] and r["sym"] and abs(r["xb_meas"] / r["xb"] - 1) < 1e-6 and abs(r["Kr"] - 0.7424) < 3e-3
             and r["tau"] < 1
             and 1 - r["tau"] < 0.3 * r["Ymin_mu"] + 3 * (0.5 / 300) ** 2 and r["dev"] <= r["x"]
             for r in pl["rows"]) and pl["xh"] < 1e-8
    return dict(P1=p1, P2=p2, P3=p3, P4=p4, P5=p5, P6=p6)


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("P0 (M's) 538: what rests beyond established physics, worked out; COMPUTED-THEORIZED carries a complete proof")
    print("P1 the minisuperspace metric is d xi d(6 Y^2), flat: %s" % ck["P1"])
    print("P2 the expectation-value integral, closed form and series against quadrature, worst %.1e: %s"
          % (o["integral"], ck["P2"]))
    print("P3 d/dz 1F1(-a/2,1/2,-z) = a 1F1(1-a/2,3/2,-z) = a e^-z 1F1((1+a)/2,3/2,z) > 0: %s" % ck["P3"])
    print("P4 (1F1 z^-1/4 Gamma(3/4)/Gamma(1/2) - 1) z at z = 1e2, 1e3, 1e4: %s (-1/16 = -0.0625): %s"
          % (", ".join("%.5f" % float(r) for r in o["asym"]), ck["P4"]))
    print("P5 Kretschmann's denominator %s, free of xi: %s" % (o["K"]["den"], ck["P5"]))
    for r in o["place"]["rows"]:
        print("   x_b %6.1f: Y_min/r_h^2 %.2e, two horizons %s, symmetric %s, K_max/K_cl(Y_min) %.4f, tau/2r_h %.8f, "
              "departure at x_b/10 %.2e <= %.2f" % (r["xb"], r["Ymin_mu"], r["zeros"], r["sym"], r["Kr"], r["tau"],
                                                  r["dev"], r["x"]))
    print("P6 the rows hold wherever the bounce sits well inside the horizon (x_h %.1e here): %s"
          % (o["place"]["xh"], ck["P6"]))
    return ck


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0
    for m in ("integral", "place_sigma"):
        MUT.clear(); MUT.add(m)
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-11s %s" % (m, "caught" if not ok else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--selftest" in sys.argv:
        r = selftest(); print("selftest:", "PASS" if r else "FAIL"); sys.exit(0 if r else 1)
    report()
