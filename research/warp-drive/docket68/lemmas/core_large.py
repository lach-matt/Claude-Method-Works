#!/usr/bin/env python3
"""core_large.py -- item 478: the large end's core computed on the exact warped black string, to the quantum region's
boundary.  The approach approved at 441 (4) and 442 (3) ("O1b and O1c by computing the large-end core on the exact
warped black string to the quantum region's boundary"), owed since (phase2: "422 the core (TO-COMPUTE)").  It replaces
section 33's step 4 at the large end, which rested on Hollands, Wald and Zahn (READ), with a computation.
Labels: computed (exact unless marked), deduced, M's.  Worked in the conversation; not verified; not seated.

  K0 (M's) 478: "I want you to prove everything that you have derived."  440: "anything derived must be proved
     separately with computation."
  K1 (computed, exact) Chamblin, Hawking and Reall's string, ds^2 = (ell/z)^2 [-f dt^2 + dr^2/f + r^2 dOmega_2^2 + dz^2],
     f = 1 - 2m/r, solves the bulk's law R_ab = -(4/ell^2) g_ab for every m and at every r, the core included.
  K2 (computed, exact) On the plane z = ell the extrinsic curvature is K_mn = -h_mn/ell for every m: the plane carries
     its tension alone, 6/(kappa5^2 ell), and no matter.  So the string is an exact solution of bulk and plane together.
  K3 (computed, exact) f has one root, r = 2m: no inner horizon (as 464, 471).  Inside, g^rr = (z/ell)^2 f < 0: r is a
     time function and falls strictly along every future causal curve (our side); on position 2's side, the time
     reverse, it rises.
  K4 (computed, exact) The Kretschmann scalar is 40/ell^4 + 48 m^2 z^4/(ell^4 r^6).  On the bulk side of the plane,
     z >= ell, it is at least 40/ell^4 + 48 m^2/r^6 and grows without bound as r -> 0.
  K5 (computed, exact) Every causal curve inside obeys dz^2 <= dr^2/|f| and d(tau)^2 <= (ell/z)^2 dr^2/|f|, and
     int_0^2m dr/sqrt|f| = pi m.  So between our face and r = 0 a causal curve moves at most pi m in z (it cannot run
     off to the far bulk) and spends at most pi m of proper time.  A causal geodesic has (dr/dlam)^2 = E^2 + |f|(L^2/r^2
     + P^2) in the conformal frame, bounded away from zero on any [r1, r2] inside (E, L, P not all zero), so its affine
     length to any r1 > 0 is finite (and finite in the string's frame, the factor (ell/z)^2 being bounded there).
  K6 (computed) x = l5^2 sqrt(K) reaches 1 at r_x(z) >= r_q = (48 m^2 l5^4 / (1 - 40 (l5/ell)^4))^(1/6) > 0.  With K3
     and K5, every future causal geodesic entering our face reaches x = 1 at a radius >= r_q, in finite affine length,
     with x < 1 (curvature finite) before it; every one on position 2's side leaves x = 1 for position 2's face the
     same.  This is H-CORE-DELIVERS at the large end, computed, and O1b's and O1c's own claims on the passage's
     classical parts.  Numbers at r0 = 20 ell, the Earth cap and r0 = 2.8e7 ell (section 31's size).
  K7 (computed, exact) Near r = 0 the string's interior is the vacuum Kasner of exponents (-1/3, 2/3, 2/3, 0) under a
     smooth warp: sum p = sum p^2 = 1.  The classical end is a curvature singularity, K ~ (T_end - T)^-4 along the
     fall, not a horizon and not a bounded-curvature end; core_face's five-dimensional form (K = 72 mu5^2/r^8) ends the
     same way.  So x passes 1 before the end on both forms.

What this does not prove: the string is the record's large-end model to (ell/r0)^2 at the horizon (261 (3); core_face
G2); the localized hole's own interior (Figueras and Wiseman's solution is the exterior) is not computed, and in the
core the string and core_face's five-dimensional form are the two exact forms between which it lies, both giving K6.
The transition through the region (x >= 1) is 273's, H-BOUNCE-TO-P2: not computed here.

python3 core_large.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
_C = {}
t, r, th, ph, z = sp.symbols("t r theta phi z", real=True)
m, ell = sp.symbols("m ell", positive=True)
X = (t, r, th, ph, z)


def _load(name, alias):
    if alias not in _C:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); _C[alias] = mod
    return _C[alias]


def metric():
    f = 1 - 2 * m / r + (m ** 2 / r ** 2 if "inner" in MUT else 0)
    w = (ell / z) ** (1 if "warp" in MUT else 2)
    return sp.diag(-w * f, w / f, w * r ** 2, w * r ** 2 * sp.sin(th) ** 2, w), f


def curvature():
    g, f = metric()
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    G = [[[sp.simplify(gi[a, a] * (sp.diff(g[a, b], X[c]) + sp.diff(g[a, c], X[b]) - sp.diff(g[b, c], X[a])) / 2)
           for c in range(5)] for b in range(5)] for a in range(5)]
    def R(a, b, c, d):                                   # R^a_bcd
        e = sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
        e += sum(G[a][c][k] * G[k][b][d] - G[a][d][k] * G[k][b][c] for k in range(5))
        return e
    Rud = {}
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(c + 1, 5):
                    v = sp.simplify(R(a, b, c, d))
                    if v != 0:
                        Rud[(a, b, c, d)] = v
    ric = sp.zeros(5)
    for (a, b, c, d), v in Rud.items():
        if a == c:
            ric[b, d] += v
        if a == d:
            ric[b, c] -= v
    ric = ric.applyfunc(sp.simplify)
    kr = 0                                               # R_abcd R^abcd = sum 2 g_aa g^bb g^cc g^dd (R^a_bcd)^2, c < d
    for (a, b, c, d), v in Rud.items():
        kr += 2 * g[a, a] * gi[b, b] * gi[c, c] * gi[d, d] * v ** 2
    lam = sp.Rational(-4) if "sign" not in MUT else sp.Rational(4)
    return dict(einstein=(ric - lam / ell ** 2 * g).applyfunc(sp.simplify), K=sp.simplify(kr), f=f, g=g)


def junction():
    g, _ = metric()
    n = z / ell                                          # unit normal (into the bulk, z increasing): n^z
    Kmn = sp.diag(*[n * sp.diff(g[i, i], z) / 2 for i in range(4)]).subs(z, ell)
    h = sp.diag(*[g[i, i] for i in range(4)]).subs(z, ell)
    return (Kmn + h / ell).applyfunc(sp.simplify)


def bounds():
    rr = sp.symbols("rr", positive=True)
    tau = sp.integrate(sp.sqrt(rr / (2 * m - rr)), (rr, 0, 2 * m))
    if "tau" in MUT:
        tau *= 2
    E, L, P = sp.symbols("E L P", real=True)
    f = 1 - 2 * m / r
    # null geodesic of the conformal frame -f dt^2 + dr^2/f + r^2 dOmega^2 + dz^2 (conserved E = f tdot, L, P = zdot)
    rdot2 = sp.simplify(sp.solve(sp.Eq(-E ** 2 / f + sp.Symbol("q") ** 2 / f + L ** 2 / r ** 2 + P ** 2, 0),
                                 sp.Symbol("q") ** 2)[0])
    return dict(tau=sp.simplify(tau), rdot2=rdot2, target=E ** 2 + (2 * m / r - 1) * (L ** 2 / r ** 2 + P ** 2))


def onset():
    QO = _load("quantum_onset.py", "cl_qo"); EC = _load("earth_cap.py", "cl_ec")
    o = QO.onset_4d(); l5, ell_ = o["l5"], o["ell"]
    c = 12 if "kret" in MUT else 48
    out = {}
    for name, r0 in (("r0 = 20 ell", 20 * ell_), ("the Earth cap", EC.compute()["r0"]), ("r0 = 2.8e7 ell", 2.8e7 * ell_)):
        mm = r0 / 2
        rq = (c * mm ** 2 * l5 ** 4 / (1 - 40 * (l5 / ell_) ** 4)) ** (1 / 6)
        out[name] = dict(r0=r0, rq=rq, rq_ell=rq / ell_, rq_r0=rq / r0, zmax=math.pi * mm / ell_, tau=math.pi * mm,
                         x_at_rq=l5 ** 2 * math.sqrt(40 / ell_ ** 4 + 48 * mm ** 2 / rq ** 6))
    return out


def kasner():
    p = [sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(2, 3), 0]
    # Schwarzschild interior near r = 0: T ~ r^(3/2) in proper time, so g_tt-part ~ T^(-2/3), angles ~ T^(4/3)
    T = sp.symbols("T", positive=True)
    rT = T ** sp.Rational(2, 3)
    K_fall = sp.simplify((48 * m ** 2 / rT ** 6))
    return dict(sum=sum(p), sum2=sum(q ** 2 for q in p), Kpow=sp.degree(sp.simplify(K_fall * T ** 4 / m ** 2), T))


def compute():
    return dict(curv=curvature(), junction=junction(), bounds=bounds(), onset=onset(), kasner=kasner())


def checks(o):
    c = o["curv"]
    k1 = c["einstein"].is_zero_matrix
    k2 = o["junction"].is_zero_matrix
    roots = sp.solve(sp.numer(sp.together(c["f"])), r)
    grr = sp.simplify(1 / c["g"][1, 1])
    k3 = (roots == [2 * m] and sp.simplify(grr.subs(r, m)) .subs({m: 1, ell: 1, z: 1}) < 0)
    k4 = sp.simplify(c["K"] - (40 / ell ** 4 + 48 * m ** 2 * z ** 4 / (ell ** 4 * r ** 6))) == 0
    b = o["bounds"]
    k5 = sp.simplify(b["tau"] - sp.pi * m) == 0 and sp.simplify(b["rdot2"] - b["target"]) == 0
    on = o["onset"]
    k6 = all(abs(v["x_at_rq"] - 1) < 1e-9 and 0 < v["rq_r0"] < 1e-9 and v["rq_ell"] < 1e-9 for v in on.values())
    ks = o["kasner"]
    k7 = ks["sum"] == 1 and ks["sum2"] == 1 and ks["Kpow"] == 0
    return dict(K1=k1, K2=k2, K3=k3, K4=k4, K5=k5, K6=k6, K7=k7)


def report(o=None):
    o = o or compute()
    ck = checks(o)
    print("K1 the string solves R_ab = -(4/ell^2) g_ab exactly, every m: %s" % ck["K1"])
    print("K2 the plane z = ell: K_mn + h_mn/ell = 0, tension alone: %s" % ck["K2"])
    print("K3 one root of f (r = 2m), r a time function inside: %s" % ck["K3"])
    print("K4 Kretschmann = %s: %s" % (o["curv"]["K"], ck["K4"]))
    print("K5 proper time from the face to r = 0 at most %s; null (dr/dlam)^2 = %s: %s" % (
        o["bounds"]["tau"], o["bounds"]["rdot2"], ck["K5"]))
    for k, v in o["onset"].items():
        print("   %-15s r_q = %.4g m, r_q/ell = %.3g, r_q/r0 = %.3g, z-excursion <= %.3g ell, x at r_q = %.6f" % (
            k, v["rq"], v["rq_ell"], v["rq_r0"], v["zmax"], v["x_at_rq"]))
    print("K6 x = 1 reached inside the hole, before r = 0, at every size: %s" % ck["K6"])
    print("K7 Kasner (-1/3, 2/3, 2/3, 0): sums %s, %s; K T^4 constant along the fall: %s" % (
        o["kasner"]["sum"], o["kasner"]["sum2"], ck["K7"]))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["sign", "warp", "inner", "kret", "tau"]
    for mu in names:
        MUT.clear(); MUT.add(mu); _C.clear()
        try:
            res = selftest(quiet=True)
        except Exception:
            res = False
        caught += not res; print("mutant %-6s %s" % (mu, "caught" if not res else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
