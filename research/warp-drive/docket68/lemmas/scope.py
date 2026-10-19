#!/usr/bin/env python3
"""scope.py -- item 489 (F4 and F9 of the 488 verification): the theorem's domain in N, and which corridor is "exactly
one".  Labels: computed (exact unless marked), deduced, READ.

  C1 (computed, exact; READ) "Exactly one corridor, fixed by N" holds among static holes only.  At one horizon area
     (one N) the singly spinning five-dimensional Myers-Perry hole, area 2 pi^2 mu r_+ with r_+^2 = mu - a^2 and
     E = 3 pi mu c^4/(8 G5), satisfies mu sqrt(mu - a^2) = R^3 (R Tangherlini's radius): E/E_T = 1.021, 1.091, 1.466,
     4.061 at a/R = 0.25, 0.5, 1, 2, and grows without bound as a^2 -> mu.  Among static vacuum holes the hole is unique:
     Gibbons, Ida and Shiromizu, Phys. Rev. Lett. 89, 041101 (2002) (READ: a static, asymptotically flat vacuum black
     hole in higher dimensions is Schwarzschild-Tangherlini), and the plane moves the localized hole off Tangherlini by
     O((r_h/ell)^2) = 6.4e-31 at the example (Figueras-Wiseman's family continuous from it, READ at 261).  The corridor
     is static because its delivery is round: a radial null shell carries T_v phi = 0, so J = 0 exactly; the README's
     inflow over the write is round only in the mean, its random angular momentum ~ sqrt(n) hbar giving a/r_h = 7.6e-8
     and E/E_T - 1 = 1.8e-15 at the example.  So the statement reads: exactly one static (J = 0) corridor, as the round
     delivery forms; a delivery carrying angular momentum forms another member of the family, with more energy.
  C2 (computed) The domain.  The curvature scale at the horizon is x_h = l5^2 sqrt(K) = sqrt(72) (l5/r_h)^2 (K =
     72 mu^2/r^8).  A classical horizon (x_h < 0.01) needs r_h > 29.1 l5, N > 1.76e5 bits; the five-dimensional
     interior is computed for mu/l5^2 from 1e6 to 1e40 (transition5q H7), r_h >= 1e3 l5, N >= 7.12e9 bits, up to the
     large end's onset (N_L = 5.3e60), where the large end's own interior takes over.  The example README (2.74e15
     bits) lies inside; a 174-bit README (r_h = 2.90 l5, x_h = 1.01) lies outside, the corridor itself Planck-scale, and
     the theorem claims nothing there.

python3 scope.py [--selftest | --mutants]
"""
import os, sys, math, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
EXAMPLE_N = 2742570311524972


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def mu_at(a):
    """C1: mu sqrt(mu - a^2) = 1 (R = 1), by bisection"""
    lo, hi = max(1.0, a * a), 1e8
    for _ in range(300):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if m * math.sqrt(max(m - a * a, 0.0)) < 1 else (lo, m)
    return 0.5 * (lo + hi)


def uniqueness():
    table = {a: mu_at(a) for a in (0.0, 0.25, 0.5, 1.0, 2.0, 5.0)}
    # exact: at a = 0 mu = R^2; dE/da^2 > 0 at fixed area (implicit differentiation)
    m, a = sp.symbols("mu a", positive=True)
    F = m ** 2 * (m - a ** 2) - 1                                   # (mu sqrt(mu - a^2))^2 = R^6, R = 1
    dmu_da2 = sp.simplify(-sp.diff(F, a) / sp.diff(F, m) / (2 * a))
    grows = sp.simplify(dmu_da2.subs(m, 1).subs(a, 0)) > 0
    # the round shell: T_ab = rho k_a k_b with k_a = -d_a v carries no T_(v phi)
    v, r, ph = sp.symbols("v r phi")
    k = [-1, 0, 0]                                                  # (v, r, phi) components of k_a
    T_vphi = k[0] * k[2]
    # the inflow's random angular momentum at the example (passage_est's quanta)
    SS = _load("source_spec.py", "sc_ss"); kk = SS.consts(); d = SS.energy_check(kk)
    kT = kk["hbar"] * kk["c"] / (2 * math.pi * d["rh"])
    n = (d["E"] / 2) / (2.701 * kT)                                 # the plane's inflow quanta, E/2 over 2.70 kT each
    J = math.sqrt(n) * kk["hbar"] * (0 if "no_spin_noise" in MUT else 1)
    M = d["E"] / kk["c"] ** 2
    a_over_r = 1.5 * J / (M * kk["c"] * d["rh"])                    # 5D: J = (2/3) M a c
    dE = mu_at(a_over_r) - 1
    brane = (d["rh"] / kk["ell"]) ** 2
    return dict(table=table, grows=grows, T_vphi=T_vphi, a_over_r=a_over_r, dE=dE, brane=brane)


def domain():
    x_h = lambda rr: math.sqrt(72) / rr ** 2                        # rr = r_h / l5
    N_of = lambda rr: math.pi ** 2 / (2 * math.log(2)) * rr ** 3
    rr_cl = (math.sqrt(72) / 0.01) ** 0.5
    rr_in = 1e3                                                     # mu/l5^2 = 1e6, transition5q's lowest computed
    rr_174 = (2 * 174 * math.log(2) / math.pi ** 2) ** (1 / 3)
    rr_ex = (2 * EXAMPLE_N * math.log(2) / math.pi ** 2) ** (1 / 3)
    N_floor = N_of(rr_in) * (10 if "floor" in MUT else 1)
    return dict(rr_cl=rr_cl, N_cl=N_of(rr_cl), N_in=N_floor, rr_174=rr_174, x_174=x_h(rr_174), x_ex=x_h(rr_ex),
                N_top=N_of(1e20), ex_inside=EXAMPLE_N >= N_floor, cu_inside=174 >= N_floor)


def compute():
    return dict(u=uniqueness(), d=domain())


def checks(o):
    u, d = o["u"], o["d"]
    t = u["table"]
    out = [("C1: at one N the spinning family's energy E/E_T = 1.021, 1.091, 1.466, 4.061 at a/R = 0.25, 0.5, 1, 2, "
            "growing with a; the round shell carries T_v phi = 0 (J = 0); the inflow's random spin a/r_h = 7.6e-8, "
            "E/E_T - 1 = 1.8e-15; the plane's correction (r_h/ell)^2 = 6.4e-31",
            ["%.3f" % t[a] for a in (0.25, 0.5, 1.0, 2.0)] == ["1.021", "1.091", "1.466", "4.061"]
            and t[5.0] > t[2.0] and u["grows"] and u["T_vphi"] == 0 and "%.2g" % u["a_over_r"] == "7.6e-08"
            and 1e-15 < u["dE"] < 1e-14 and "%.2g" % u["brane"] == "6.4e-31"),
           ("C2: a classical horizon needs N > 1.76e5 (r_h > 29.1 l5); the interior is computed from N = 7.12e9 to the "
            "large end; the example inside (x_h 1.6e-9), a 174-bit README outside (r_h 2.90 l5, x_h 1.01)",
            "%.3g" % d["N_cl"] == "1.76e+05" and "%.1f" % d["rr_cl"] == "29.1" and "%.3g" % d["N_in"] == "7.12e+09"
            and d["ex_inside"] and not d["cu_inside"] and "%.2f" % d["rr_174"] == "2.90" and "%.2f" % d["x_174"] == "1.01"
            and "%.2g" % d["x_ex"] == "1.6e-09" and d["N_top"] > 5.3e60)]
    return out


def report(o=None):
    o = o or compute(); u, d = o["u"], o["d"]
    print("scope.py -- the domain in N and the one static corridor (item 489, F4 and F9)\n")
    print("C1 E/E_T at one N: " + ", ".join("a/R %g: %.4f" % (a, m) for a, m in u["table"].items())
          + "; round shell T_v phi = %s; inflow spin a/r_h %.2g, E/E_T - 1 %.2g; plane O((r_h/ell)^2) %.2g"
          % (u["T_vphi"], u["a_over_r"], u["dE"], u["brane"]))
    print("C2 classical horizon N > %.3g (r_h > %.1f l5); interior computed N >= %.3g to %.2g; 174 bits: r_h %.2f l5, "
          "x_h %.2f (outside); example x_h %.2g (inside)" % (d["N_cl"], d["rr_cl"], d["N_in"], d["N_top"], d["rr_174"],
                                                             d["x_174"], d["x_ex"]))


MUTANTS = {"no_spin_noise": "the inflow read as round at every instant (C1)",
           "floor": "the computed interior's floor moved tenfold (C2)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
