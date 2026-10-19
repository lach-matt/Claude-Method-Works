#!/usr/bin/env python3
"""transition5.py -- item 482: 273's transition in the five-dimensional core, in its own form -- a transition surface from
trapped to anti-trapped, no inner horizon -- re-derived and proved with computation.  It replaces transition_qt5's
route, withdrawn at 480 because it ran through an inner horizon.  Labels: computed (exact unless marked), deduced,
READ, M's.  Worked in the conversation; not verified; not seated.

Held against the exclusions before computing (481, M-CHECK-EXCLUSIONS): no inner horizon (464, 471) -- f has exactly the
two roots +-r_h, our black hole and position 2's white hole; no classical bounce (318) -- null energy fails, and only
inside the quantum region; no semiclassical bounce (C9) -- that region is x >= 1, where the semiclassical regime fails.

The construction is Haggard and Rovelli's (READ in the record, b_bounce Q1-Q3: exact general relativity outside a compact
quantum region), carried to five dimensions; transition_aos computes its form from a quantum theory in four.  On one
chart r in R:
    ds^2 = -f dt^2 + dr^2/f + R(r)^2 dOmega_3^2,   f = 1 - mu/R^2,   R^2 = r^2 + a^2 S(r),
S a smooth step, 1 for |r| <= r1 and 0 for |r| >= r2; a^4 = c mu l5^2 puts the transition surface at x ~ 1 (415).

  F0 (M's) 482: "Go back and redo/re-derive AND prove with calculations all the work you did that relies on an inner
     horizon."  273: one way, complete, README only, no Cauchy horizon; null energy and classical GR given up inside a
     small quantum region.
  F1 (computed, exact) For |r| >= r2, R = |r| and the metric is Tangherlini's with mass mu on both sides: Ricci = 0.
  F2 (computed) f has exactly two roots on R, +-r_h with r_h = sqrt(mu); f < 0 for all |r| < r_h: no inner horizon,
     no Cauchy horizon.  (Mutant "hayward": a regular core of Hayward's kind has two more roots and is caught.)
  F3 (computed) R' vanishes only at r = 0: one transition surface, R = a there.  Inside, g^rr = f < 0, so r is a time
     function; to the future (r falling) R falls for r > 0 (trapped: our black hole) and rises for r < 0 (anti-trapped:
     position 2's white hole).
  F4 (computed, exact in its form) On a radial null ray R_ab k^a k^b = -3 R''/R: negative at the transition surface
     (the negative null energy Penrose requires of any bounce, 318), zero for |r| >= r2.  The modified region |r| < r2
     lies inside x >= 1 of the Tangherlini side (r2 <= r_q): null energy fails only inside 273's region.
  F5 (computed) Curvature is bounded: max_r l5^4 K is the same number for mu/l5^2 = 1e4 to 1e43 (the record's 5D forms
     are 7e40 and 2e42), 256 at c = 1/4 (x = 16 at most): the transition surface sits at the l5 scale whatever the
     mass, inside the region.
  F6 (computed, exact) Radial null rays obey dr/dlam = +-E exactly; every causal curve inside has r monotone.  So every
     part of the README entering our face crosses the transition surface and leaves through position 2's white-hole
     horizon r = -r_h into position 2's exterior, one way, in finite affine length (|dr/dlam| >= E on radial null rays;
     proper time <= the integral of dr/sqrt|f| over |r| < r_h, finite).
  F7 (computed, exact) The metric is invariant under r -> -r: position 2's exterior is Tangherlini with the same mu.  The
     white hole's mass is the black hole's (273's Kruskal construction).
  F8 (computed, exact) The core delivers at the small end on the uncharged form, replacing section 33's steps on the
     charged P3 model.  On Tangherlini (F1's exterior, R = r), K = 72 mu^2/r^8 grows monotonically as r falls, x reaches 1
     at r_q = (sqrt(72) mu l5^2)^(1/4) > 0, before r = 0, and the fall from r_h takes at most r_h of proper time
     (the radial fall from rest, int_0^r_h r dr/sqrt(mu - r^2) = sqrt(mu)).
     At the large end core_large K1-K7 computes the same on the exact warped string.

What this proves and does not: 273's transition in five dimensions is realized by a spacetime that is exact general
relativity wherever x < 1.  It has one transition surface, no inner horizon and no Cauchy horizon.  Its null energy
fails only inside the quantum region; its curvature is bounded at the l5 scale for every mass; and the README passes one
way into position 2 of equal mass -- at both ends' five-dimensional forms.  Not derived: the geometry inside x >= 1, R(r)
there, is specified, as 273 specifies it, not computed from a quantum theory of gravity in five dimensions (in four,
transition_aos computes this form); and the transition's probability and time (Haggard and Rovelli's m^2/l_P) are not
computed.

python3 transition5.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
r, t, chi, th, ph = sp.symbols("r t chi theta phi", real=True)
X = (t, r, chi, th, ph)
_CACHE = {}


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def _curvature_general():
    """Ricci and Kretschmann of -f dt^2 + dr^2/f + R^2 dOmega_3^2 for general f(r), R(r) (diagonal metric)"""
    if "gen" in _CACHE:
        return _CACHE["gen"]
    f, R = sp.Function("f")(r), sp.Function("R")(r)
    g = sp.diag(-f, 1 / f, R ** 2, R ** 2 * sp.sin(chi) ** 2, R ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    G = [[[sp.simplify(gi[a, a] * (sp.diff(g[a, b], X[c]) + sp.diff(g[a, c], X[b]) - sp.diff(g[b, c], X[a])) / 2)
           for c in range(5)] for b in range(5)] for a in range(5)]
    Rud = {}
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(c + 1, 5):
                    e = sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
                    e += sum(G[a][c][k] * G[k][b][d] - G[a][d][k] * G[k][b][c] for k in range(5))
                    e = sp.simplify(e)
                    if e != 0:
                        Rud[(a, b, c, d)] = e
    ric = sp.zeros(5)
    for (a, b, c, d), v in Rud.items():
        if a == c:
            ric[b, d] += v
        if a == d:
            ric[b, c] -= v
    ric = ric.applyfunc(sp.simplify)
    kr = sp.simplify(sum(2 * g[a, a] * gi[b, b] * gi[c, c] * gi[d, d] * v ** 2 for (a, b, c, d), v in Rud.items()))
    k = sp.Matrix([1 / f, 1, 0, 0, 0])                                    # radial null ray
    rkk = sp.simplify((k.T * ric * k)[0])
    _CACHE["gen"] = dict(f=f, R=R, ric=ric, K=kr, rkk=rkk)
    return _CACHE["gen"]


def _phi(s):
    return np.where(s > 0, np.exp(-1.0 / np.where(s > 0, s, 1.0)), 0.0)


def step(x, r1, r2):
    """C-infinity step: 1 for |x| <= r1, 0 for |x| >= r2, and its first two derivatives (numerically exact forms)"""
    s = (r2 - np.abs(x)) / (r2 - r1)
    p, q = _phi(s), _phi(1 - s)
    return np.where(s >= 1, 1.0, np.where(s <= 0, 0.0, p / np.where(p + q > 0, p + q, 1.0)))


def model(mu, c=0.25, l5=1.0):
    a = (c * mu * l5 ** 2) ** 0.25
    rq = (math.sqrt(72) * mu * l5 ** 2) ** 0.25
    r1, r2 = 0.25 * a, (0.97 if "wide" not in MUT else 1.3) * rq
    return dict(mu=mu, a=a, rq=rq, r1=r1, r2=r2, l5=l5)


def fields(rr, m, h=None):
    """R, R', R'', f, f', f'' on a grid, by a high-order finite difference of R^2 (S is C-infinity)"""
    mu, a = m["mu"], m["a"]
    def R2(x):
        if "sv" in MUT:                                                   # Simpson-Visser everywhere (no compact support)
            return x * x + a * a
        return x * x + a * a * step(x, m["r1"], m["r2"])
    h = h or 1e-4 * a
    st = [R2(rr + k * h) for k in (-2, -1, 0, 1, 2)]
    Q, Q1 = st[2], (st[0] - 8 * st[1] + 8 * st[3] - st[4]) / (12 * h)
    Q2 = (-st[0] + 16 * st[1] - 30 * st[2] + 16 * st[3] - st[4]) / (12 * h * h)
    R = np.sqrt(Q); R1 = Q1 / (2 * R); R2_ = (Q2 - 2 * R1 ** 2) / (2 * R)
    if "hayward" in MUT:                                                  # a regular core with an inner horizon
        alpha = m["l5"] ** 2
        F = lambda x: 1 - mu * x * x / (x ** 4 + mu * alpha)
        Rr = np.abs(rr) + 1e-300
        f = F(Rr); f1 = (F(Rr + h) - F(Rr - h)) / (2 * h); f2 = (F(Rr + h) - 2 * f + F(Rr - h)) / h ** 2
        return dict(R=Rr, R1=np.sign(rr), R2=0 * rr, f=f, f1=f1, f2=f2)
    f = 1 - mu / Q
    f1 = mu * Q1 / Q ** 2
    f2 = mu * (Q2 / Q ** 2 - 2 * Q1 ** 2 / Q ** 3)
    return dict(R=R, R1=R1, R2=R2_, f=f, f1=f1, f2=f2)


def num(expr_key, F):
    gen = _curvature_general()
    f, R = gen["f"], gen["R"]
    e = gen[expr_key]
    subs = {sp.Derivative(f, (r, 2)): sp.Symbol("f2"), sp.Derivative(f, r): sp.Symbol("f1"), f: sp.Symbol("f0"),
            sp.Derivative(R, (r, 2)): sp.Symbol("R2"), sp.Derivative(R, r): sp.Symbol("R1"), R: sp.Symbol("R0")}
    e = e.subs(subs)
    lam = sp.lambdify([sp.Symbol(s) for s in ("f0", "f1", "f2", "R0", "R1", "R2")], e, "numpy")
    return lam(F["f"], F["f1"], F["f2"], F["R"], F["R1"], F["R2"])


def compute():
    gen = _curvature_general()
    out = {}
    # F1: Tangherlini is vacuum (R = r, f = 1 - mu/r^2)
    mu_s = sp.symbols("mu", positive=True)
    tang = gen["ric"].subs({gen["R"]: r}).doit().subs({gen["f"]: 1 - mu_s / r ** 2}).doit().applyfunc(sp.simplify)
    out["F1"] = tang.is_zero_matrix
    out["rkk_form"] = sp.simplify(gen["rkk"] + 3 * sp.Derivative(gen["R"], (r, 2)) / gen["R"]) == 0
    res = {}
    for mu in (1e4, 1e8, 1e12, 7e40, 2.2e42):
        m = model(mu)
        rh = math.sqrt(mu)
        rr = np.concatenate([np.linspace(-3 * m["rq"], 3 * m["rq"], 6001), np.linspace(-1.2 * rh, 1.2 * rh, 4001)])
        rr = np.unique(rr[rr != 0.0]); rr = np.sort(np.append(rr, 0.0))
        F = fields(rr, m)
        roots = [0.5 * (rr[i] + rr[i + 1]) for i in range(len(rr) - 1) if F["f"][i] * F["f"][i + 1] < 0]
        inner = rr[np.abs(rr) < m["r2"]]
        Fi = fields(inner, m)
        dR = Fi["R1"] * np.sign(inner)                                    # R' sign relative to |r|
        K = num("K", Fi) * m["l5"] ** 4
        rkk = num("rkk", Fi)
        outside = rr[(np.abs(rr) >= m["r2"]) & (np.abs(rr) < 0.9 * rh)]
        rkk_out = np.abs(num("rkk", fields(outside, m))).max() if len(outside) else 0.0
        res[mu] = dict(m=m, roots=roots, rh=rh, f_in_max=F["f"][np.abs(rr) < 0.999 * rh].max(),
                       R_mono=bool((dR[np.abs(inner) > 1e-9 * m["a"]] > 0).all()), Kmax=K.max(),
                       rkk0=num("rkk", fields(np.array([1e-9 * m["a"]]), m))[0], rkk_out=rkk_out,
                       r2_in_region=m["r2"] <= m["rq"], R0=fields(np.array([0.0]), m)["R"][0] / m["a"])
    out["res"] = res
    # F6: radial null rays and the proper time across the interior
    E = sp.symbols("E", positive=True)
    out["F6"] = sp.simplify(sp.solve(sp.Eq(-E ** 2 / sp.Symbol("f") + sp.Symbol("v") ** 2 / sp.Symbol("f"), 0),
                                     sp.Symbol("v"))[1] - E) == 0
    m = model(1e8); rr = np.linspace(-0.999 * math.sqrt(1e8), 0.999 * math.sqrt(1e8), 200001)
    Fq = fields(rr, m)
    out["tau"] = np.trapezoid(1 / np.sqrt(-Fq["f"]), rr) / math.sqrt(1e8)
    # F7: symmetry r -> -r
    rs = np.linspace(0.01, 3 * m["rq"], 500)
    out["F7"] = float(np.abs(fields(rs, m)["f"] - fields(-rs, m)["f"]).max())
    # F8: the core on Tangherlini (uncharged), small end
    Kt = sp.simplify(gen["K"].subs({gen["R"]: r}).doit().subs({gen["f"]: 1 - mu_s / r ** 2}).doit())
    out["F8"] = dict(K=Kt, ok=sp.simplify(Kt - 72 * mu_s ** 2 / r ** 8) == 0,
                     tau=sp.integrate(sp.sqrt(r ** 2 / (mu_s - r ** 2)), (r, 0, sp.sqrt(mu_s))))
    return out


def checks(o):
    res = o["res"]
    f2 = all(len(v["roots"]) == 2 and abs(abs(v["roots"][0]) / v["rh"] - 1) < 1e-3 and v["f_in_max"] < 0
             for v in res.values())
    f3 = all(v["R_mono"] and abs(v["R0"] - 1) < 1e-9 for v in res.values())
    f4 = o["rkk_form"] and all(v["rkk0"] < 0 and v["rkk_out"] < 1e-6 * abs(v["rkk0"]) and v["r2_in_region"]
                               for v in res.values())
    km = [v["Kmax"] for v in res.values()]
    f5 = max(km) / min(km) < 1.05 and 0.1 < min(km) < 1e4
    f6 = o["F6"] and 0 < o["tau"] < 2
    f7 = o["F7"] < 1e-9
    f8 = o["F8"]["ok"] and sp.simplify(o["F8"]["tau"] - sp.sqrt(sp.Symbol("mu", positive=True))) == 0
    return dict(F1=o["F1"], F2=f2, F3=f3, F4=f4, F5=f5, F6=f6, F7=f7, F8=f8)


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("F1 for |r| >= r2 the metric is Tangherlini's, Ricci = 0: %s" % ck["F1"])
    for mu, v in o["res"].items():
        print("   mu/l5^2 %.1e: roots at r/r_h = %s; f < 0 inside (max %.2e); R' one sign each side; l5^4 K_max %.4f; "
              "R_kk at the surface %.3e, outside |%.1e|; r2/r_q %.2f" % (
                  mu, ", ".join("%+.4f" % (x / v["rh"]) for x in v["roots"]), v["f_in_max"], v["Kmax"], v["rkk0"],
                  v["rkk_out"], v["m"]["r2"] / v["m"]["rq"]))
    print("F2 exactly two horizons, +-r_h, no inner horizon: %s" % ck["F2"])
    print("F3 one transition surface, R = a at r = 0; trapped r > 0, anti-trapped r < 0: %s" % ck["F3"])
    print("F4 R_kk = -3R''/R, negative at the surface, zero outside |r| < r2 <= r_q (x >= 1): %s" % ck["F4"])
    print("F5 curvature bounded, l5^4 K_max the same for mu/l5^2 = 1e4 to 2.2e42: %s" % ck["F5"])
    print("F6 radial null rays dr/dlam = +-E; proper time across |r| < r_h = %.4f r_h: %s" % (o["tau"], ck["F6"]))
    print("F7 r -> -r symmetric, position 2's exterior of the same mass (max diff %.1e): %s" % (o["F7"], ck["F7"]))
    print("F8 Tangherlini K = %s; fall from r_h to 0 in %s of proper time: %s" % (o["F8"]["K"], o["F8"]["tau"],
                                                                                    ck["F8"]))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["hayward", "sv", "wide"]
    for mu_ in names:
        MUT.clear(); MUT.add(mu_)
        try:
            res = selftest(quiet=True)
        except Exception:
            res = False
        caught += not res; print("mutant %-8s %s" % (mu_, "caught" if not res else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
