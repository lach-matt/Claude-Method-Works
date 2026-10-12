#!/usr/bin/env python3
"""pair_math.py -- item 318: "For the math".  273's chosen option promised the bounce's negative null energy "(to be
paired per ray under 183)"; 183 rules "zero net null energy along each light ray"; the C5 verifier (item 317, Q1)
showed by Raychaudhuri's identity that no matter on a ray the bounce turns brings its net to zero.  M put the choice
-- 177's appearance, 183 governing classical rays only, 183 everywhere and no bounce -- to the mathematics (149).
Worked in the conversation (computed with sympy and mpmath, exact where marked; READ where marked; deduced where
marked; not verified by a separate session; not seated); 2026-10-12.

  P0 (read) M's item-318 words, and the words of 177, 183 and 273 the question turns on, verbatim in the rulings file.
  P1 (computed, exact; numerically on c4_residue R6's family) Every radial null ray that enters converging and leaves
     diverging carries net negative null energy, whatever lies on it.  Raychaudhuri's identity for the radial null
     congruence in 5D, d theta/d lambda = -theta^2/3 - sigma^2 - R_kk (twist-free; shear only adds), integrates to
     integral R_kk d lambda = theta_in - theta_out - integral (theta^2/3 + sigma^2) d lambda, which is negative whenever
     theta_in < 0 < theta_out (computed: the sign, symbolically).  R_kk = 8 pi G5 T_kk counts all the null energy on the
     ray -- the README's included.  It needs no asymptotics: a ray from far out on our side (theta = -3/r < 0) to far out
     on position 2's (theta = +3/r > 0) is such a ray, as is any ray through the core.  On R6's family, R(T) =
     sqrt(1/100 + T^2), r_h = 1, E~ = 1, from R = 1/2 through the bounce to R = 1/2: integral R_kk d lambda =
     -15.0364559951, equal to theta_in - theta_out - integral theta^2/3 to every digit, theta = -/+3.39411 (computed;
     the C5 verifier's figure reproduced with independent code).
  P2 (computed, exact) Outside the quantum region every ray segment keeps 183.  Tangherlini's f = 1 - r_h^2/r^2 is
     Ricci-flat, so R_kk = 0 on every null ray there (computed); the README's matter carries T_kk >= 0 -- a null shell
     mu l^a l^b gives mu (l.k)^2 >= 0 (b_interior B5) -- so on every classical segment the net null energy is >= 0, zero
     where it is vacuum: "never violated" holds there.  The negative that P1 requires sits wholly inside the region 273
     already marks as giving up "classical GR there".
  P3 (deduced; READ where marked) "183 everywhere" is excluded by M's own rulings.  With zero net along every whole ray,
     P1 forbids any continuation with a metric along the ray that turns the radial congruence from converging to
     diverging: the bounce, and the classical shell too, whose radial ray gathers -6/(kappa^2 r0) < 0 (b_interior B5).
     Penrose's theorem (READ in b_interior B1) leaves only giving up a Cauchy surface -- the inner horizon -- whose cell
     is neither complete nor README-only (b_interior B6, computed from its cells).  So no complete, README-only passage
     into position 2 would remain, against 273 (M chose the option reading "One-way, complete, README only") and 270 and
     276 (the one-way passage).  Friedman, Schleich and Witt state the general form for causal curves (READ, Phys. Rev.
     Lett. 71, 1486, Theorem 1: "If an asymptotically flat, globally hyperbolic spacetime (M,g,b) satisfies the averaged
     null energy condition, then every causal curve from J- to J+ is deformable to gamma_0 rel J"); P3 rests on P1, which
     needs neither their asymptotic flatness nor their global hyperbolicity.
  P4 (deduced) The other two coincide in content.  On "183 governs classical rays, not the quantum region" and on
     "177's appearance" alike, the negative is confined to the quantum region (P2), every classical ray keeps 183, and
     along each whole passing ray the net is negative (P1) -- which is exactly what any passage from one exterior to
     another requires (P1, P3), the role 177 names: negative null energy from "coupling the two entangled ends (the
     mechanism that makes an entangled bridge traversable ...)", "the appearance".  No figure, clause or claim of the
     record turns on which of the two names it takes.  The board's reading, to be overruled by M at any point: 183
     governs every classical ray; the passage's negative inside the quantum region is 177's appearance.
  P5 (deduced) What follows.  273 stands (H-BOUNCE-TO-P2); its option text's "(to be paired per ray under 183)" -- the
     board's words -- is corrected to "the negative confined to the quantum region, every classical ray keeping 183, the
     passage's net negative 177's appearance".  The README pairs nothing; b_bounce Q5's comparison stays withdrawn
     (item 317).  C1, C4, C5 and C7 stand on 273 as before; C7's one open premise (c7_oneway V11 (Q1)) is closed.

What this does not show.
  - The quantum region's own form: P1 says only what any metric through it must do.
  - Which of P4's two names M prefers; the board's reading is given.

Imports c4_residue.py (its ricci_diag) and b_interior.py by path.  Stdlib + sympy + mpmath.
python3 pair_math.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = {"318": "For the math", "183": "zero net null energy along each light ray",
         "177": "the mechanism that makes an entangled bridge traversable", "273": "One-way, complete, README only",
         "273b": "classical GR there"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def p1():
    """Raychaudhuri's sign, and its integral on R6's family"""
    ti, to, F, sh = sp.symbols("theta_in theta_out F sigma2", positive=True)       # theta_in = -ti, theta_out = +to
    net = -ti - to - F - sh
    if MUT.get("readme_outside_Rkk"):
        net = net + sp.Symbol("readme", positive=True)   # the mutant: the README's null energy kept out of R_kk
    sign = bool(sp.ask(sp.Q.negative(net), sp.Q.positive(ti) & sp.Q.positive(to) & sp.Q.positive(F) & sp.Q.positive(sh)))
    CR = _load("c4_residue.py", "pm_cr")
    T, t, th, ph, ps = sp.symbols("T t theta phi psi", real=True)
    R = sp.sqrt(sp.Rational(1, 100) + T ** 2)
    G = 1 / R ** 2 - 1
    g = sp.diag(-1, G, R ** 2, R ** 2 * sp.sin(th) ** 2, R ** 2 * sp.sin(th) ** 2 * sp.sin(ph) ** 2)
    Ric, _ = CR.ricci_diag(g, [T, t, th, ph, ps])
    Tdot, tdot = 1 / sp.sqrt(G), 1 / G                    # E~ = 1: G t' = 1, T'^2 = 1/G on a radial null ray
    Rkk = sp.simplify(Ric[0, 0] * Tdot ** 2 + Ric[1, 1] * tdot ** 2)
    theta = 3 * sp.diff(R, T) * Tdot / R
    fR = sp.lambdify(T, Rkk / Tdot, "mpmath")
    f2 = sp.lambdify(T, theta ** 2 / 3 / Tdot, "mpmath")
    ft = sp.lambdify(T, theta, "mpmath")
    with mp.workdps(30):
        T1 = -mp.sqrt(mp.mpf("0.25") - mp.mpf("0.01"))
        I, F2 = mp.quad(fR, [T1, 0, -T1]), mp.quad(f2, [T1, 0, -T1])
        th_in, th_out = ft(T1), ft(-T1)
        ident = abs(I - (th_in - th_out - F2)) < mp.mpf("1e-20")
        return dict(sign=sign, integral=float(I), th_in=float(th_in), th_out=float(th_out), ident=ident)


def p2():
    """Tangherlini Ricci-flat; the README's null shell T_kk >= 0"""
    CR = _load("c4_residue.py", "pm_cr2")
    tt, r, th, ph, ps = sp.symbols("t r theta phi psi", positive=True)
    f = 1 - 1 / r ** 2
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2, r ** 2 * sp.sin(th) ** 2 * sp.sin(ph) ** 2)
    Ric, _ = CR.ricci_diag(g, [tt, r, th, ph, ps])
    flat = all(sp.simplify(Ric[i, i]) == 0 for i in range(5))
    mu, lk = sp.symbols("mu lk", real=True)
    shell = mu * lk ** 2
    if MUT.get("readme_negative"):
        shell = -mu * lk ** 2                              # the mutant: the README's matter with negative null energy
    nonneg = bool(sp.ask(sp.Q.nonnegative(shell), sp.Q.nonnegative(mu) & sp.Q.real(lk)))
    return dict(flat=flat, nonneg=nonneg)


def p3():
    """183 everywhere: the continuations left, read from b_interior's cells"""
    cells = _load("b_interior.py", "pm_bi").cells()
    # a continuation survives "183 everywhere" only if it turns no radial ray with a metric: no bounce, no shell
    survivors = {k: v for k, v in cells.items() if k[1] == "none" and k[2] == "pos2"}
    if MUT.get("inner_complete"):
        survivors = {k: dict(v, complete=1, readme_only=1) for k, v in survivors.items()}
    passage = any(v["one_way"] and v["complete"] and v["readme_only"] for v in survivors.values())
    shell_neg = True                                       # b_interior B5: -6/(kappa^2 r0) < 0 on the shell's radial ray
    return dict(survivors=sorted(survivors), passage=passage, shell_neg=shell_neg)


def compute():
    return dict(p1=p1(), p2=p2(), p3=p3())


def report(o):
    print("pair_math.py -- 273 against 183, for the math (item 318)\n")
    a = o["p1"]
    print("P1 integral R_kk < 0 when theta_in < 0 < theta_out: %s; on R6's family %.10f (theta %.5f -> %.5f), the "
          "identity holding: %s" % (a["sign"], a["integral"], a["th_in"], a["th_out"], a["ident"]))
    print("P2 Tangherlini Ricci-flat: %s; the README's null shell T_kk >= 0: %s" % (o["p2"]["flat"], o["p2"]["nonneg"]))
    print("P3 under 183 everywhere the continuations left %s; a complete, README-only passage among them: %s" % (
        o["p3"]["survivors"], o["p3"]["passage"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("P0 M's words at 318, 183, 177 and 273 verbatim in the rulings file", all(w in rul for w in WORDS.values()))
    a = o["p1"]
    add("P1 a ray entering converging and leaving diverging carries net negative null energy, the README's included; "
        "-15.0364559951 on R6's family, the identity exact", a["sign"] and a["ident"]
        and "%.10f" % a["integral"] == "-15.0364559951" and "%.5f" % a["th_out"] == "3.39411")
    add("P2 every classical segment keeps 183: Tangherlini Ricci-flat, the README's T_kk >= 0",
        o["p2"]["flat"] and o["p2"]["nonneg"])
    add("P3 under 183 everywhere only the inner horizon survives, and no complete, README-only passage into position 2 "
        "remains -- against 273, 270 and 276", o["p3"]["survivors"] == [(1, "none", "pos2")] and not o["p3"]["passage"]
        and o["p3"]["shell_neg"])
    return res


MUTANTS = {"readme_outside_Rkk": "the README's null energy kept out of R_kk (b_bounce Q5's error)",
           "readme_negative": "the README's matter with negative null energy",
           "inner_complete": "the inner horizon read as complete and README-only"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-20s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
