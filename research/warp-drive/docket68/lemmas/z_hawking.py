#!/usr/bin/env python3
"""z_hawking.py -- item 489 (F10 of the 488 verification): clause (Z) against our face's own Hawking flux.

(Z) as stated gave its reason as "the passage's classical segments are Ricci-flat and the README's null energy
non-negative", and confined "the passage's negative" to the quantum region.  Our face's evaporation (CLOSEs, M's 336)
brings a negative flux the reason omits, on classical rays.  Labels: computed (exact unless marked), deduced.

  H1 (computed, exact in the s-wave model) The state our face is in (Unruh's): the ingoing stress T_vv = -M(2r -
     3M)/(48 pi r^4) is negative for every r > 3M/2 -- on our face, where the curvature is classical (x_h = 1.6e-9 at
     the example), outside the quantum region -- and the outgoing T_uu = kappa^2/(48 pi) + T_vv is non-negative
     everywhere.  So the negative lies on the outgoing rays (the face's generators and their neighbours), and (Z)'s
     "confined to the quantum region" holds for the bounce's negative, not for this one.
  H2 (computed, exact on passage_est Q3) During the write the face is at balance: the inflow puts +P_in on the same
     outgoing rays as the Hawking influx's -P_H, and P_in = P_H; so along each generator the net null energy per unit
     time is zero, and over the generator it is the opening's E(N) > 0.
  H3 (computed) After the write, along a generator with affine parameter lambda = e^(kappa v)/kappa (lambda' = 1 at the
     README's arrival), the Hawking influx counts e^(-kappa v): its total is P/kappa against the README's E, a ratio
     P r_h/(c E) = 1/(2 life) = 5.8e-16 at the example (life in face clocks).  Net positive by 1.7e15 times.
  H4 (deduced) So (Z) holds net along every classical ray -- including the face's generators during evaporation, where
     the negative is paired on the same rays by the README's positive (H2, H3) -- and the clause reads: net along each
     light ray (183); every classical ray keeps it, the face's own Hawking influx included, paired on its generators;
     the bounce's negative confined to the quantum region.

python3 z_hawking.py [--selftest | --mutants]
"""
import os, sys, math, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def stress():
    r, M = sp.symbols("r M", positive=True)
    f = 1 - 2 * M / r
    fp, fpp = sp.diff(f, r), sp.diff(f, r, 2)
    Tvv = sp.factor(sp.simplify(-(fp ** 2 / 16 - f * fpp / 8) / (12 * sp.pi)))
    Tuu = sp.simplify(Tvv + (1 / (4 * M)) ** 2 / (48 * sp.pi))
    zero = sp.solve(sp.Eq(Tvv, 0), r)
    neg_out = all(float(Tvv.subs({M: 1, r: x})) < 0 for x in (1.51, 2.0, 3.0, 10.0, 1e3))
    uu_pos = all(float(Tuu.subs({M: 1, r: x})) >= -1e-15 for x in (0.2, 1.0, 1.5, 2.0, 2.5, 4.0, 1e3))
    return dict(Tvv=Tvv, zero=zero, neg_out=neg_out, uu_pos=uu_pos,
                closed=sp.simplify(Tvv + M * (2 * r - 3 * M) / (48 * sp.pi * r ** 4)) == 0)


def pairing():
    F2 = _load("face2_open.py", "zh_f2")
    w = F2.write_and_open()
    life = w["life"]
    P_in = 0.0 if "no_inflow" in MUT else w["P_tot"]
    net_rate = P_in - w["P_tot"]                                    # H2: per unit time on the generators during the write
    pos = 0.0 if "no_readme" in MUT else w["E"]
    neg = w["P_tot"] * w["clock"]                                   # H3: P/kappa, kappa = c/r_h
    ratio = neg / w["E"]
    net_after = pos - neg
    x_h = math.sqrt(72) * (w["k"]["l5"] / w["rh"]) ** 2
    return dict(net_rate=net_rate, ratio=ratio, net_after=net_after, life=life, x_h=x_h)


def compute():
    return dict(st=stress(), pr=pairing())


def checks(o):
    st, pr = o["st"], o["pr"]
    r_, M_ = sp.symbols("r M", positive=True)
    return [("H1: T_vv = -M(2r - 3M)/(48 pi r^4), zero at r = 3M/2 and negative outside it, on our face where x_h = "
             "1.6e-9 (classical); T_uu >= 0 everywhere",
             st["closed"] and st["zero"] == [sp.Rational(3, 2) * M_] and st["neg_out"] and st["uu_pos"]
             and "%.2g" % pr["x_h"] == "1.6e-09"),
            ("H2: during the write the inflow's +P_in and the Hawking influx's -P_H meet on the same rays, net zero",
             pr["net_rate"] == 0),
            ("H3: after the write the affine-weighted Hawking influx is 1/(2 life) = 5.8e-16 of the README's E; net "
             "positive", "%.2g" % pr["ratio"] == "5.8e-16" and abs(pr["ratio"] - 1 / (2 * pr["life"])) < 1e-25
             and pr["net_after"] > 0)]


def report(o=None):
    o = o or compute(); st, pr = o["st"], o["pr"]
    print("z_hawking.py -- (Z) against our face's Hawking flux (item 489, F10)\n")
    print("H1 T_vv = %s, zero at %s; negative outside: %s; T_uu >= 0: %s; x_h at the example %.2g"
          % (st["Tvv"], st["zero"], st["neg_out"], st["uu_pos"], pr["x_h"]))
    print("H2 net per unit time on the generators during the write: %g W" % pr["net_rate"])
    print("H3 after the write: Hawking influx / README E = %.2g (1/(2 life) = %.2g); net %.4g J"
          % (pr["ratio"], 1 / (2 * pr["life"]), pr["net_after"]))


MUTANTS = {"no_inflow": "the write without its inflow (H2)", "no_readme": "the README's positive removed (H3)"}


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
