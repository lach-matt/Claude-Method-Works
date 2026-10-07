#!/usr/bin/env python3
"""censor5d.py -- wall D, the censorship theorem for a passage between two ends of a plane in a bulk (DOORS.md OPEN 1).

READ: Chrusciel, Galloway & Solis, arXiv:0808.3233v2 ("CGS"):
  p.3   "We define the null future inwards and outwards mean curvatures theta+- of S as theta+- := tr_gamma(nabla n+-)"
  p.3-4 Theorem 3.1: "Let t be a Cauchy time function on a space-time (M, g) with timelike boundary T = U T_alpha, and
        satisfying the null energy condition (NEC) ... Suppose that there exists a component T_1 of T with compact level
        sets t|T_1 such that T_1 is weakly inner future trapped with respect to t.  If all connected components T_alpha,
        alpha != 1, of T are inner past trapped with respect to t, then J+(T_1) n J-(T_alpha) = 0 for T_alpha != T_1."
  p.4   Remark 3.2: "The condition that at least one of the defining inequalities is strict is necessary."
  p.7-8 eqs. (4.6), (4.10): far level sets are inner future AND past trapped when "+-theta+- > 0"
  p.9   "our approach to topological censorship in this work requires uniformity in time of the mean null extrinsic
        curvatures of the spheres"

THEOREM W (the board's application of CGS Theorem 3.1).  Let a five-dimensional spacetime carry the corridor's plane, and
  W1  satisfy the null energy condition everywhere: met by a positive-tension plane (DOORS K1, on H-COMPOSITE-SURFACE);
      CGS assume a smooth metric, so a thin plane is read as the limit of a thick one (H-THICK-PLANE, the board's);
  W2  be globally hyperbolic in the region M between two far boundaries T_1, T_2, with Cauchy time function t;
  W3  have the plane's end 1 and end 2 in two DISTINCT ends of the bulk, cut off by far boundaries T_1, T_2 whose level
      sets are compact and untrapped (+-theta+- > 0), uniformly in t.
  Then no causal curve runs from T_1 to T_2 (CGS Thm 3.1).  But the corridor's passage does (it crosses the far sphere of
  end 1 inward and the far sphere of end 2 outward), and passage5d.py P6 adds timelike curves through the bulk.  So the
  corridor cannot satisfy W1, W2 and W3 together.

  C1  (computed) such boundaries exist in a Randall-Sundrum II bulk: the 3-sphere centred on the plane,
      |x|^2 + w^2 = R^2 (w the conformal depth, z = ell + |w|), has +-theta+- = 3/R EXACTLY at every point, either side --
      as untrapped as a sphere in flat space; its level sets are compact (S^3).  Control: a sphere centred on the AdS
      boundary (z = 0) has theta+- = 0 everywhere -- marginal, the strictness CGS Remark 3.2 says is necessary fails
  C2  (STRUCTURAL) the passage crosses each far sphere once: on the plane r = 2m + u^2 is monotone in |u| on each side
  C3  so, with your positive tension (W1 met), the corridor needs one of:
        (a) the plane's two ends lie in ONE end of the bulk -- joined away from the corridor, through the deep bulk, where
            the bulk ends (GLOBALBULK G3 reached the same requirement from the far field);
        (b) the far boundaries are not untrapped uniformly in time;
        (c) the five-dimensional spacetime is not globally hyperbolic.
      Control (READ in censor.py): a compact extra dimension gives CGS Thm 5.2 directly, and forbids the passage
Imports doors.py and passage5d.py by path.  Stdlib + sympy.  python3 censor5d.py [--selftest]
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


def expansions(centre_depth):
    """theta+- of the 3-sphere |x|^2 + (w - centre_depth)^2 = R^2 at fixed static time t, in the Randall-Sundrum II bulk
    on the side w > 0: g = (ell/z)^2 (-dt^2 + dx^2 + dw^2), z = ell + w.  For static T (Killing) and unit outward normal
    n, tr_gamma(nabla T) = 0 and tr_gamma(nabla n) = div n - g(n, nabla_T T), so theta+- = +-(div n - a_n), with a the
    static observers' acceleration, a = d ln N, N = ell/z."""
    ell, R = sp.symbols("ell R", positive=True)
    x1, x2, x3, w = sp.symbols("x1 x2 x3 w", real=True)
    X = [x1, x2, x3, w]
    z = ell + w
    rho = sp.sqrt(x1**2 + x2**2 + x3**2 + (w - centre_depth) ** 2)
    nhat = [x1 / rho, x2 / rho, x3 / rho, (w - centre_depth) / rho]       # flat unit radial
    n = [z / ell * c for c in nhat]                                       # unit in g
    sqrtg = (ell / z) ** 5                                                # sqrt|det g| (t included)
    div_n = sp.simplify(sum(sp.diff(sqrtg * n[i], X[i]) for i in range(4)) / sqrtg)
    a_n = sp.simplify(sum(n[i] * sp.diff(sp.log(ell / z), X[i]) for i in range(4)))
    th_plus = sp.simplify(div_n - a_n)
    # evaluate on the sphere: parametrise a point by its depth w and put |x|^2 = R^2 - (w - c)^2
    s = sp.Symbol("s", positive=True)                                     # |x|
    on = th_plus.subs(x1, s).subs({x2: 0, x3: 0})
    on = sp.simplify(on.subs(s, sp.sqrt(R**2 - (w - centre_depth) ** 2)))
    return sp.simplify(on), ell, R, w


def compute():
    brane, ell, R, w = expansions(0)                                      # centred on the plane (w = 0)
    ell2 = sp.Symbol("ell", positive=True)
    bdry, _, _, _ = expansions(-ell2)                                     # centred on the AdS boundary (z = 0)
    doors = _load(os.path.join(HERE, "doors.py"), "c5_doors").compute()
    p5 = _load(os.path.join(HERE, "passage5d.py"), "c5_passage5d")
    u = sp.Symbol("u", real=True)
    r_of_u = 2 + u**2
    return {"theta_brane": brane, "theta_bdry": bdry, "R": R, "nec_composite": doors["s4_ok"],
            "monotone": sp.simplify(sp.diff(r_of_u, u) * u) ,
            "r_star": 2 + p5.threshold() ** 2}


def report(d):
    print("censor5d.py -- wall D: Theorem W (CGS Thm 3.1 applied to the corridor)\n")
    print("C1 RS II, 3-sphere centred on the plane: theta+ = %s (= -theta-), at every point; compact level sets (S^3)"
          % d["theta_brane"])
    print("   control, sphere centred on the AdS boundary: theta+ = %s (marginal: CGS Remark 3.2's strictness fails)"
          % d["theta_bdry"])
    print("W1 null energy on the composite plane (DOORS K1): %s" % d["nec_composite"])
    print("C2 on the plane dr/du * u = %s >= 0: the passage crosses each far sphere once" % d["monotone"])
    print("   and passage5d P6: timelike bulk routes from beyond r_* = %.5f m" % d["r_star"])
    print("C3 so the corridor needs: (a) its two ends in ONE end of the bulk, (b) far spheres not untrapped uniformly in "
          "time, or (c) no global hyperbolicity")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("C1: in Randall-Sundrum II the 3-sphere centred on the plane has +-theta+- = 3/R exactly -- strictly untrapped",
        sp.simplify(d["theta_brane"] - 3 / d["R"]) == 0)
    chk("C1 control: a sphere centred on the AdS boundary is marginal, theta = 0 (strictness fails)",
        sp.simplify(d["theta_bdry"]) == 0)
    chk("W1: the composite plane keeps the null energy condition (DOORS K1, on H-COMPOSITE-SURFACE)", d["nec_composite"])
    chk("C2 (STRUCTURAL): r is monotone in |u| on each side, so the passage crosses each far sphere once",
        sp.simplify(d["monotone"] - 2 * sp.Symbol("u", real=True) ** 2) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
