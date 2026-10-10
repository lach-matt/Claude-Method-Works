#!/usr/bin/env python3
"""b6_once.py -- lemma B6 restated on item 200 (1): position 2's plane counts once, so k_R = k_L/2 (computed; Israel's
junction standard-not-READ; not verified by a separate session; not seated; 2026-10-10).

M, item 200 (1), choosing the offered option: "Once: k_R = k_L/2".  Item 139 (1): "1 - yes" to "whether position 2's
plane is the negative-tension one, a quarter of ours, with ours positive".  B6 as first written (b6_k.py B6a, through
kderive.py K3 and multiplane.py M4) read the quarter with position 2's plane counted with its orbifold image (PRZ's
tau2/tau1, the doubled count) and got k_R = 3k_L/4.  COUNT-CYPHER.md showed only the count premise decides it; M chose
once.

  O1 (computed, sympy) warp e^{-2A(y)}, a plane's tension tau = 3[A']/kappa^2 (Israel; RS's sigma = 6k/kappa^2 is the
     control).  Our plane: k_L on both sides, [A'] = 2k_L, tau1 = 6k_L/kappa^2 = sigma_RS (clause (B)).  Position 2's
     plane, counted once: one sheet joining the slab (k_L) to its own bulk beyond (k_R; 138), [A'] = k_R - k_L,
     tau2 = 3(k_R - k_L)/kappa^2.  The quarter, tau2/tau1 = -1/4, gives k_R = k_L/2 exactly.  Controls: counted twice
     (tau2 doubled) gives 3k_L/4, b6_k.py's value; a positive quarter (+1/4) gives k_R = 3k_L/2 > k_L, a positive
     tension, against 139 (1)'s sign
  O2 (computed) the beyond bulk is AdS with k_R = k_L/2 > 0: its Lambda is a quarter of the slab's (Lambda ~ -k^2), so
     position 2's universe's bulk has its own law (138), with one five-dimensional coupling (H-ONE-G5, the board's
     reading of 191)
  O3 (imported, b6_k.py B6b) every clause on the plane stays free of k's scale -- unchanged by the count
  O4 (computed) what the count changes downstream, for re-reading (not edited here): the sheets' summed tension is
     1 - 1/4 = 3/4 of ours (as before: per-sheet -1/4); b6p_scale.py B6''a's coefficient for (ell_L, sigma_1) becomes
     1/(4 pi) (was 9/(16 pi)); multiplane.py M4's gamma(r = 0) = (2x + 1)/(4x - 1) becomes 2 at x = 1/2 (was 5/4 at
     x = 3/4) -- moot since 141 and B5c leave no radion
So B6 restated: "k's ratio fixed by the work, k_R = k_L/2", PROVED (computed) on M's 139 (1) and 200 (1).  Imports
lemmas/b6_k.py by path.  Stdlib + sympy.  python3 b6_once.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = {}


def derive():
    kL, kR, k5 = sp.symbols("k_L k_R kappa5", positive=True)
    q = sp.Rational(-1, 4) if not MUT.get("quarter_positive") else sp.Rational(1, 4)
    copies = 1 if not MUT.get("count_twice") else 2
    tau = lambda jump: 3 * jump / k5**2
    sigma_RS = tau(2 * kL)                                      # RS control: sigma = 6k/kappa^2
    tau1 = tau(2 * kL)
    tau2 = copies * tau(kR - kL)
    sol = sp.solve(sp.Eq(tau2 / tau1, q), kR)
    twice = sp.solve(sp.Eq(2 * tau(kR - kL) / tau1, sp.Rational(-1, 4)), kR)
    pos = sp.solve(sp.Eq(tau(kR - kL) / tau1, sp.Rational(1, 4)), kR)
    x = sp.Symbol("x", positive=True)
    gamma0 = (2 * x + 1) / (4 * x - 1)                          # multiplane.py M4's gamma(r = 0), x = k_R/k_L
    G, s1 = sp.symbols("G sigma_1", positive=True)
    def coef(ratio, n):                                         # ell_L^2 G sigma_1 / c^4 from B6''a's ell_R^2 = 3c^4/(4 pi G sigma_sum)
        s_sum = (1 + n * copies_sheet(ratio)) * s1
        ellR2 = 3 / (4 * sp.pi * G * s_sum)
        return sp.simplify(ratio**2 * ellR2 * G * s1)
    copies_sheet = lambda ratio: (ratio - 1) / 2                # per-sheet tau2/tau1 = (k_R - k_L)/(2 k_L)
    r_once = sol[0] / kL if sol else None
    return {"sigma_RS": sp.simplify(sigma_RS - 6 * kL / k5**2) == 0, "kR": sol, "twice": twice, "pos": pos,
            "kL": kL, "sum": sp.simplify(1 + copies * copies_sheet(r_once)) if sol else None,
            "gamma_once": gamma0.subs(x, sp.Rational(1, 2)), "gamma_twice": gamma0.subs(x, sp.Rational(3, 4)),
            "coef_once": coef(r_once, copies) if sol else None, "coef_twice": coef(sp.Rational(3, 4), 2)}


def b6b():
    spec = importlib.util.spec_from_file_location("b6o_b6k", os.path.join(HERE, "b6_k.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["b6o_b6k"] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE, os.path.dirname(HERE)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
            d = mod.compute()
    finally:
        sys.path[:] = saved
    return d


def compute():
    return {"o": derive(), "b6": b6b()}


def checks(d):
    o, b = d["o"], d["b6"]
    kL = o["kL"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("O1 tau = 3[A']/kappa^2 gives sigma_RS = 6k/kappa^2 (control); counted once, the quarter gives k_R = k_L/2",
        o["sigma_RS"] and o["kR"] == [kL / 2])
    add("O1 controls: counted twice gives 3k_L/4 (b6_k.py's value); a positive quarter gives 3k_L/2 > k_L",
        o["twice"] == [3 * kL / 4] and o["pos"] == [3 * kL / 2])
    add("O2 the beyond bulk is AdS with k_R = k_L/2 > 0 (Lambda a quarter of the slab's)",
        o["kR"] and (o["kR"][0] / kL) ** 2 == sp.Rational(1, 4))
    add("O3 b6_k.py B6b imported: the plane's clauses are free of ell; the bulk series carries ell (the absence a result)",
        b["n_kk_free"] and b["series_has_ell"] and b["closed_forms_free"])
    add("O4 downstream: summed tension 3/4 of ours; B6''a coefficient 1/(4 pi) (was 9/(16 pi)); M4's gamma(0) = 2 "
        "(was 5/4)", o["sum"] == sp.Rational(3, 4) and o["coef_once"] == 1 / (4 * sp.pi)
        and o["gamma_once"] == 2 and o["gamma_twice"] == sp.Rational(5, 4) and o["coef_twice"] == sp.Rational(9, 16) / sp.pi)
    return res


MUTANTS = {"count_twice": "position 2's plane counted twice", "quarter_positive": "the quarter taken positive"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-34s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    d = compute()
    print("b6_once.py -- B6 restated on item 200 (1)\n  k_R =", d["o"]["kR"], "  (twice:", d["o"]["twice"], ")")
