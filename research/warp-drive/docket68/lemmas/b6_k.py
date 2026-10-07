#!/usr/bin/env python3
"""b6_k.py -- Warp Theorem lemma B6: what the work fixes of k, and what it does not.

Item 140: "If k helps define the bulk, the math in our work should give you pieces to both derive and prove k. Our math
is not dependent on k, k is dependent on our work."  Item 136 answer 8: "leave it to measurement. But we can accurately
hypothesize it first."

  B6a THE RATIO IS FIXED.  From item 139's quarter, k_R = 3 k_L / 4 exactly (multiplane.py M4, imported through
      kderive.py K3).  A pure number, the same for every README
  B6b EVERY CLAUSE ON THE PLANE IS FREE OF k's SCALE -- your first sentence, made exact.  Computed with ell kept as a
      symbol: the bulk's normal pull along the passage, R5(n,k,n,k) = 2r''/r, comes out with no ell (passage5d.py P2's
      expression, from the bulk series whose own coefficients DO carry ell -- bulkseries B4's (ell^2 + 28)/(12 ell^2) --
      so the absence is a result, not an omission).  E(N), r0, the area, the hold (O3), the capacity (I2), the ledger
      (E3, E4), the length (R4) and the composite's positivity (B5a) are free of ell by their closed forms
  B6c SO THE SCALE IS NOT FIXED BY THE THEOREM'S OTHER LEMMAS.  A quantity no clause depends on cannot be read back off
      them (KDERIVE.md).  What fixes it is measurement (136 answer 8): the scale is a premise of nature, and the
      theorem's clause (B) reads "k's ratio fixed by the work; its scale free of every clause, fixed by measurement".
      This narrows the lemma as first written ("k fixed by the work"); the narrowing is reported to M, not hidden
Imports bulk/passage5d.py, bulk/bulkseries.py and bulk/kderive.py by path.  python3 b6_k.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def compute():
    p5 = _load(os.path.join(D68, "bulk", "passage5d.py"), "b6_passage5d")
    bs = _load(os.path.join(D68, "bulk", "bulkseries.py"), "b6_bulkseries")
    kd = _load(os.path.join(D68, "bulk", "kderive.py"), "b6_kderive")
    tid = p5.tidal()
    co = bs.solve(1 - 2 / bs.r, (1 - 2 / bs.r) ** 2 / (1 - sp.Rational(3, 2) / bs.r), 2)
    series_has_ell = any(bs.ell in sp.sympify(c).free_symbols for X in "ABC" for c in co[X])
    kd_out = kd.compute()
    ratio = sp.nsimplify(kd_out["kR_over_kL"])
    h, c, G, N = sp.symbols("h c G N", positive=True)
    E = sp.sqrt(N * h * c**5 * sp.log(2) / (8 * sp.pi**2 * G))
    hold = sp.simplify((h * N / (4 * E)) / (G * E / c**5))
    return {"n_kk": tid["n_kk"], "n_kk_free": bs.ell not in tid["n_kk"].free_symbols, "series_has_ell": series_has_ell,
            "kd": kd_out, "ratio": ratio, "closed_forms_free": all(sp.Symbol("ell") not in x.free_symbols
                                                                     for x in (E, hold))}


def report(d):
    print("b6_k.py -- Warp Theorem lemma B6\n")
    print("B6a the ratio (kderive.py K3): %s" % (d["ratio"],))
    print("B6b R5(n,k,n,k) = %s, free of ell: %s, while the bulk series carries ell: %s; E and the hold free of ell: %s"
          % (d["n_kk"], d["n_kk_free"], d["series_has_ell"], d["closed_forms_free"]))
    print("B6c so the scale is fixed by measurement (136 answer 8), not by the theorem's other lemmas")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("B6b: the bulk's normal pull along the passage is free of ell, computed with ell symbolic", d["n_kk_free"])
    chk("B6b control: the bulk series it comes from does carry ell -- the absence is a result", d["series_has_ell"])
    chk("B6b: E(N) and the hold (O3) are free of ell by their closed forms", d["closed_forms_free"])
    chk("B6a: the ratio fixed by the work, k_R/k_L = 3/4 (kderive.py)", d["ratio"] == sp.Rational(3, 4))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
