#!/usr/bin/env python3
"""zeno_method.py -- item 392: Zeno's halves as the method for a computation over a very large range, checked first
where the answer is exact.  M, 392: "The zeno paradox describes halves and their halved segmentation. This can be a
useful model for run such a large size computation".  Worked in the conversation (computed, stdlib only; exact where
marked; deduced where marked; not verified by a separate session; not seated); 2026-10-14.

  Z0 (read) M's 392, verbatim in the rulings file.
  Z1 (deduced) The method.  A run must cross a range whose ends differ by a large factor -- the large end's 5D stretch
     runs from R_5 to 273's region, about 4.95e-14 R_5, some 44 halvings (interior_large I2).
     - Cut the remaining distance to the end in halves: segment k runs from R_k = 2^(-k) R_0 to R_k/2.
     - Rescale each segment to one size, R = R_k rho with rho in [1/2, 1], and time by the segment's own scale.
     - Give every segment the same fixed effort (here N steps).
     - In rescaled form the equations depend on k only through dimensionless parameters, which settle as k grows, so
       the rescaled segments converge to one limiting form.
     - Once they have, the remaining halves follow from that form, and their sum is a geometric series that converges:
       Zeno's sum, with its tail bounded.
     The run then costs the number of halvings, not the ratio of the ends.  Each segment is one short run with its own
     question, criterion and time (377).
  Z2 (computed; exact solution known) Checked on the 4D interior, dR/dT = -sqrt(r0/R - 1), from R = r0/2 inward
     (interior_large I1).  Its exact time is r0 (arcsin sqrt(x) - sqrt(x (1 - x))), with x = R/r0.
     - Zeno: 45 segments of 40 RK4 steps each reach R = 2^-46 r0 (1.4e-14), every segment with relative error in time
       below 1e-10.
     - Uniform steps, with the same 1,800 steps over the same time, lose 1e-6 accuracy once R falls to about 0.01 r0,
       twelve orders short of the end.
     - The rescaled durations converge to the scale-free limit (2/3)(1 - 2^(-3/2)) = 0.4310, with T = R_k^(3/2) tau.
       The time per halving falls by 2^(-3/2) each step: Kasner's exponent, measured from the segments themselves.
     - The tail after the last segment, bounded from that ratio, matches the exact remainder to 1e-9.
  Z3 (computed; exact solution known) The same on the small end's 5D interior, dR/dT = -sqrt(r_h^2/R^2 - 1)
     (o1c_oneway Z2): time per halving falls by 2^-2, and the curvature per halving rises by 2^8 (K = 72 r_h^4/R^8),
     against 2^6 in 4D.  The per-halving ratios are what the segments measure.
  Z4 (deduced) What the segments measure in the 5D stretch, against INTERIOR-REQUIRED (a)-(c).
     - (a) The proper time to 273's region is the sum over segments. It is finite when the per-halving ratio settles
       below 1, and the settled ratio gives the tail.
     - (b) No inner horizon: the clock stays monotone in every segment. A ratio that stalls at 1 is the sign of one.
     - (c) Curvature finite in each segment, its per-halving growth measured, until the bulk's Planck boundary.
  Z5 (deduced) Where it applies to the record's interior runs (interior_large/README.md, items 360-367).  Those runs
     lost x-resolution toward the brane, and their chart ends at finite proper time (B5, B6, C1).  The same halving
     applies three ways:
     - in time, halving the proper time left to the chart's end, with each segment re-sliced, rescaled by B6's fitted
       power laws and re-gridded;
     - in the bulk coordinate, a halving mesh toward the brane: [0, 1/2], [1/2, 3/4], [3/4, 7/8], ..., with the same
       points in each part;
     - in the hole's size, sampling r0/ell = 1, 2, 4, 8, 16 and testing whether the measured ratios settle as r0 doubles.

What this does not claim.
  - Anything about the 5D stretch itself: Z2-Z3 check the method where the answer is known.
  - That the rescaled segments of the 5D interior converge: that is what the first segments would measure.

Stdlib only.  python3 zeno_method.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((392, "The zeno paradox describes halves and their halved segmentation. This can be a useful model for run "
               "such a large size computation"),)
K_SEG, N_STEP = 45, 40


def _item(n):
    text = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. (.*?)(?=^\d+\. )" % n, text, re.S | re.M)
    return " ".join((m.group(1) if m else text[text.find("\n%d. " % n):]).split())


def t_exact4(x):
    """4D: time from R = x (r0 = 1) along dR/dT = -sqrt(1/R - 1), measured from R = 0: arcsin sqrt(x) - sqrt(x (1 -
    x)); below x = 0.01 its series sum_n binom(2n, n) 4^-n x^(n + 3/2)/(n + 3/2), free of the cancellation"""
    if x >= 0.01:
        return math.asin(math.sqrt(x)) - math.sqrt(x * (1 - x))
    tot, c, n = 0.0, 1.0, 0
    while True:
        term = c * x ** (n + 1.5) / (n + 1.5)
        tot += term
        if term < 1e-18 * tot:
            return tot
        n += 1
        c *= (2 * n - 1) / (2 * n)


def t_exact5(x):
    """5D: time from R = x (r_h = 1) along dR/dT = -sqrt(1/R^2 - 1), measured from R = 0: 1 - sqrt(1 - x^2)"""
    return x * x / (1 + math.sqrt(1 - x * x))


def rk4(f, y, a, b, n):
    h = (b - a) / n
    for i in range(n):
        x = a + i * h
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def zeno(dim, K=K_SEG, n=N_STEP):
    """segments k = 0..K-1 from R_k = 2^-(k+1) to R_k/2; in each, rho = R/R_k in [1/2, 1] is the independent variable
    and tau = T/R_k^p the rescaled time, p = 3/2 (4D) or 2 (5D): dtau/drho = -R_k^(1-p)/sqrt(...)"""
    p = 1.5 if dim == 4 else 2.0
    if MUT.get("kasner_wrong"):
        p = 1.0                                                  # the mutant: time scaled by R_k, not its Kasner power
    out, T = [], 0.0
    for k in range(K):
        Rk = 2.0 ** -(k + 1)
        if dim == 4:
            g = lambda rho, Rk=Rk: -Rk ** (1 - p) / math.sqrt(1 / (Rk * rho) - 1)
        else:
            g = lambda rho, Rk=Rk: -Rk ** (1 - p) / math.sqrt(1 / (Rk * rho) ** 2 - 1)
        if MUT.get("no_rescale"):
            # the mutant: the same N steps per segment but taken in T itself, uniform over the whole range
            return None
        dtau = rk4(lambda rho, y, g=g: -g(rho), 0.0, 0.5, 1.0, n)  # tau elapsed going inward from rho = 1 to 1/2
        dT = Rk ** p * dtau
        T += dT
        te = t_exact4 if dim == 4 else t_exact5
        exact = te(Rk) - te(Rk / 2)
        out.append(dict(k=k, Rk=Rk, dtau=dtau, dT=dT, rel=abs(dT - exact) / exact, T=T))
    return out


def uniform4(n_total, R_stop=2.0 ** -46):
    """uniform RK4 steps in T over the same time, from R = 1/2: the smallest R reached with relative error <= 1e-6"""
    T_end = t_exact4(0.5) - t_exact4(R_stop)
    h = T_end / n_total
    f = lambda t, R: -math.sqrt(max(1 / R - 1, 0.0)) if R > 0 else float("nan")
    R, t, good = 0.5, 0.0, 0.5
    for i in range(n_total):
        try:
            R = rk4(f, R, t, t + h, 1)
        except (ValueError, ZeroDivisionError):
            break
        t += h
        if not (R > 0) or R != R:
            break
        ex = t_exact4(0.5) - t
        if ex <= 0:
            break
        # the exact R at this time, by bisection on t_exact4
        lo, hi = 0.0, 0.5
        for _ in range(200):
            mid = (lo + hi) / 2
            (lo, hi) = (mid, hi) if t_exact4(mid) < ex else (lo, mid)
        Rex = (lo + hi) / 2
        if abs(R - Rex) / Rex > 1e-6:
            break
        good = R
    return good


def compute():
    z4, z5 = zeno(4), zeno(5)
    if z4 is None:
        return dict(z4=None, z5=None)
    lim4 = (2 / 3) * (1 - 2 ** -1.5)
    ratio4 = [z4[k + 1]["dT"] / z4[k]["dT"] for k in range(len(z4) - 1)]
    ratio5 = [z5[k + 1]["dT"] / z5[k]["dT"] for k in range(len(z5) - 1)]
    q = ratio4[-1]
    if MUT.get("tail_half"):
        q = 0.5                                                  # the mutant: Zeno's 1/2 for the measured ratio
    RK = z4[-1]["Rk"] / 2
    tail_bound = z4[-1]["dT"] * q / (1 - q)
    tail_exact = t_exact4(RK)
    uni = uniform4(K_SEG * N_STEP)
    K5 = [72 / (2.0 ** -(k + 1)) ** 8 for k in range(3)]
    K4 = [12 / (2.0 ** -(k + 1)) ** 6 for k in range(3)]
    return dict(z4=z4, z5=z5, lim4=lim4, ratio4=ratio4, ratio5=ratio5, tail_bound=tail_bound, tail_exact=tail_exact,
                uni=uni, RK=RK, k_ratio5=K5[1] / K5[0], k_ratio4=K4[1] / K4[0])


def report(o):
    print("zeno_method.py -- Zeno's halves, checked where the answer is exact (item 392)\n")
    if o["z4"] is None:
        print("no rescaled segments (mutant)")
        return
    z4 = o["z4"]
    print("Z2 4D: %d segments x %d steps reach R = %.3g r0; worst segment relative error %.2e; last rescaled duration "
          "%.6f (limit %.6f)" % (len(z4), N_STEP, o["RK"], max(s["rel"] for s in z4), z4[-1]["dtau"], o["lim4"]))
    print("Z2 time per halving falls by %.6f at the end (2^-3/2 = %.6f); tail bound %.6e against exact %.6e"
          % (o["ratio4"][-1], 2 ** -1.5, o["tail_bound"], o["tail_exact"]))
    print("Z2 uniform steps, the same %d over the same time: accurate to 1e-6 only down to R = %.3g r0"
          % (K_SEG * N_STEP, o["uni"]))
    print("Z3 5D: time per halving falls by %.6f (2^-2); worst segment relative error %.2e; curvature per halving "
          "x%g (5D) against x%g (4D)" % (o["ratio5"][-1], max(s["rel"] for s in o["z5"]), o["k_ratio5"], o["k_ratio4"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("Z0 392 verbatim in its item", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    if o["z4"] is None:
        add("Z2 rescaled segments exist", False)
        return res
    z4, z5 = o["z4"], o["z5"]
    add("Z2 45 segments x 40 steps reach R = 2^-46 r0 with every segment's time to 1e-10",
        len(z4) == 45 and abs(o["RK"] - 2.0 ** -46) < 1e-30 and max(s["rel"] for s in z4) < 1e-10)
    add("Z2 the rescaled durations converge to (2/3)(1 - 2^-3/2); time per halving falls by 2^-3/2 (Kasner)",
        abs(z4[-1]["dtau"] - o["lim4"]) < 1e-9 and abs(o["ratio4"][-1] - 2 ** -1.5) < 1e-9)
    add("Z2 the tail bounded from the measured ratio matches the exact remainder to 1e-9 relative",
        abs(o["tail_bound"] / o["tail_exact"] - 1) < 1e-9)
    add("Z2 uniform steps with the same count lose 1e-6 accuracy by R ~ 0.01 r0, twelve orders short of the end",
        1e-3 < o["uni"] < 0.05)
    add("Z3 5D: time per halving falls by 2^-2, every segment to 1e-9; curvature per halving 2^8 against 2^6",
        abs(o["ratio5"][-1] - 0.25) < 1e-9 and max(s["rel"] for s in z5) < 1e-9 and o["k_ratio5"] == 256.0
        and o["k_ratio4"] == 64.0)
    return res


MUTANTS = {"kasner_wrong": "each segment's time scaled by R_k, not by its Kasner power (Z1)",
           "no_rescale": "no rescaled segments: the same steps taken uniformly (Z1)",
           "tail_half": "the tail summed with Zeno's 1/2 in place of the measured ratio (Z2)"}


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
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-13s %-66s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
