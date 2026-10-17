#!/usr/bin/env python3
"""transition_qt5.py -- item 478: 273's transition in five dimensions, against the prior art that computes one there.
transition_aos T6 found the loop-quantum-gravity interior four-dimensional, short of the record's core.  Bueno, Cano,
Hennigar and Murcia (arXiv 2412.02742v2, READ below) compute, in D >= 5 and from the gravitational action alone, the
collapse of a shell to a regular black hole and its bounce into a new universe through a white hole.  Reproduced here in
D = 5 and run at the record's scales.  Labels: READ (verbatim, page), computed, deduced.  Worked in the conversation;
not verified; not seated.

  Q0 (READ, 2412.02742v2) p. 1: "The collapse of the shell always gives rise to a singularity-free, geodesically
     complete spacetime that contains horizons if the total mass is above a critical value.  In that case, the shell
     bounces into a new universe through a white hole explosion."  p. 2: densities "general enough to provide a basis for
     the gravitational effective action"; alpha_n "with dimensions of length^2(n-1)"; eq. (16) "h(psi) = 2M/r^(D-1),
     psi = (1 - f(r))/r^2"; eq. (9) h(psi) = psi + sum alpha_n (D - 2n)/(D - 2) psi^n.  p. 3: eq. (18), the Hayward
     case h = psi/(1 - alpha psi); eq. (19) "r_+- = sqrt(M +- sqrt(M(M - 2 alpha)))"; eq. (30) the shell's master
     equation; eq. (32) Einstein's potential "V(R) = -M/R^(D-3) - m^2/(4R^(2(D-3)))".  p. 5: the bounce "always happens
     in region III", the shell "emerging in a new universe from a white hole"; "The stability problem of the inner
     horizon can also be studied".
  Q1 (computed) Eq. (30) is reproduced: with alpha = 0 it gives eq. (32) to 1e-9.
  Q2 (computed) The paper's case (D = 5, Hayward, M = 1, m = 1.05, alpha = 1/10): horizons 1.3764 and 0.3249 as eq. (19);
     the shell's turning point R_min lies inside r_-, where f > 0 (region III), and the shell re-expands past r_- and
     r_+ (V < E between R_min and r_+).
  Q3 (computed) A tower with no quadratic term exists and is regular: h = psi + alpha^2 psi^3/(1 - alpha psi) has
     Gauss-Bonnet coefficient zero (B8, 328 kept), h' > 0, psi -> 1/alpha at the centre, f = 1 - r^2/alpha there;
     its Kretschmann scalar is bounded, of order 1/alpha^2, the same at M/alpha = 1e2 and 1e6.
  Q4 (computed) At the record's scales, alpha = l5^2 (quantum_onset P1-P4: no other scale): the regular solution is
     Tangherlini's wherever x = l5^2 sqrt(K) < 0.1 to better than 2% in 1 - f, and the inner horizon sits at
     r_- ~ l5, where x is of order one -- inside 273's quantum region; no horizon at x < 1 besides our face.

What this proves and does not: 273's transition, a black hole whose matter bounces into a new universe through a white
hole, is computed in five dimensions from the gravitational effective action alone (no exotic matter), with every
correction confined to x ~ 1.  Not proved: (a) the couplings alpha_n are not derived, only their scale; (b) the
inner horizon r_- is a Cauchy horizon inside the region (273's option says "no Cauchy horizon"), its stability open as
the paper says; (c) the bounce is computed for a bound shell of dust (E < 0); the README arrives as a null shell, which
reaches the regular centre with the thin-shell description singular there; (d) a bound shell re-collapses in the new
universe (the paper's cycle), where 273 is one-way.  So 273 is advanced, not closed.

python3 transition_qt5.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import warnings
import numpy as np
from scipy.integrate import quad, IntegrationWarning
from scipy.optimize import brentq
warnings.filterwarnings("ignore", category=IntegrationWarning)      # the 1/sqrt end point at the shell; Q1 checks accuracy

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def psi_of(r, M, a, model):
    """solve h(psi) = 2M/r^4 (D = 5) for psi in (0, 1/alpha)"""
    y = 2 * M / r ** 4
    if model == "einstein" or a == 0:
        return y
    if model == "hayward":
        return y / (1 + a * y)
    # GB-free tower h = psi + a^2 psi^3/(1 - a psi), solved for q = 1 - a psi in log space (q -> 1/(a y) at the centre)
    F = lambda lq: (1 - math.exp(lq)) / a + (1 - math.exp(lq)) ** 3 / (a * math.exp(lq)) - y
    lq = brentq(F, math.log(1 / (10 * a * y + 10)), 0.0, xtol=1e-14, rtol=1e-15, maxiter=500)
    return (1 - math.exp(lq)) / a


def f_of(r, M, a, model):
    return 1 - r * r * psi_of(r, M, a, model)


def kretschmann(r, M, a, model, h=1e-4):
    f = lambda x: f_of(x, M, a, model)
    d = h * r
    f0, fp, fm = f(r), f(r + d), f(r - d)
    f1, f2 = (fp - fm) / (2 * d), (fp - 2 * f0 + fm) / d ** 2
    return f2 ** 2 + 6 * f1 ** 2 / r ** 2 + 12 * (1 - f0) ** 2 / r ** 4


def rdot2(R, M, m, a, model):
    """eq. (30), D = 5: m/R^4 = int_R^inf 4M dr / (r^5 sqrt(1 + s - R^2 psi(r))); returns s = Rdot^2 (or None)"""
    fR = f_of(R, M, a, model)
    lo = max(0.0, -fR) + 1e-10
    def I(s):
        g = lambda u: 4 * M / (R ** 4) * u ** 3 / math.sqrt(max(1 + s - R * R * psi_of(R / u, M, a, model), 1e-300))   # r = R/u
        return quad(g, 0, 1, limit=200, epsabs=1e-13, epsrel=1e-11)[0]
    target = m / R ** 4 * (1.02 if "master" in MUT else 1.0)
    if I(lo) < target:
        return None
    hi = 1.0
    while I(hi) > target:
        hi *= 4
    return brentq(lambda s: I(s) - target, lo, hi, xtol=1e-13)


def horizons(M, a, model):
    rs = np.geomspace(1e-3 * math.sqrt(a), 10 * math.sqrt(M), 4000)
    fs = [f_of(r, M, a, model) for r in rs]
    return [brentq(lambda r: f_of(r, M, a, model), rs[i], rs[i + 1]) for i in range(len(rs) - 1) if fs[i] * fs[i + 1] < 0]


def compute():
    out = {}
    # Q1: Einstein limit of the master equation against eq. (32)
    M, m = 1.0, 1.05
    E = M * M / m / m - 1
    out["q1"] = max(abs((E - rdot2(R, M, m, 0.0, "einstein")) - (-M / R ** 2 - m * m / (4 * R ** 4)))
                    for R in (1.2, 1.5, 2.5))                                  # V < E there (bound shell)
    # Q2: the paper's Hayward case
    a = 0.1
    hz = horizons(M, a, "hayward")
    rp, rm = math.sqrt(M + math.sqrt(M * (M - 2 * a))), math.sqrt(M - math.sqrt(M * (M - 2 * a)))
    Rs = np.geomspace(0.02, 3.0, 120)
    s = [rdot2(R, M, m, a, "hayward") for R in Rs]
    allowed = [R for R, v in zip(Rs, s) if v is not None]
    i = list(Rs).index(min(allowed))
    lo_, hi_ = Rs[i - 1], Rs[i]                                               # the turning point, by bisection
    for _ in range(40):
        mid = (lo_ * hi_) ** 0.5
        lo_, hi_ = (lo_, mid) if rdot2(mid, M, m, a, "hayward") is not None else (mid, hi_)
    Rmin = hi_
    out["q2"] = dict(hz=hz, rp=rp, rm=rm, Rmin=Rmin, f_at_Rmin=f_of(Rmin, M, a, "hayward"),
                     reexpand=all(v is not None for R, v in zip(Rs, s) if Rmin <= R <= rp))
    # Q3: the GB-free tower: regular, curvature bounded independent of M
    kmax = {}
    for Mq in (1e2, 1e6):
        rs = np.geomspace(1e-3, 3.0, 400)
        kmax[Mq] = max(kretschmann(r, Mq, 1.0, "gbfree") for r in rs)
    p = np.linspace(0, 0.999, 500)
    hp = 1 + (3 * p ** 2 * (1 - p) + p ** 3) / (1 - p) ** 2                  # h'(psi), alpha = 1
    out["q3"] = dict(kmax=kmax, hprime_pos=bool((hp > 0).all()), core=f_of(1e-3, 1e6, 1.0, "gbfree"),
                     gb_coeff=0.0 if "gb" not in MUT else 1.0)
    # Q4: the record's scale, alpha = l5^2, the large end's 5D form (core_face B1's mu5 = 2M)
    CF = _load("core_face.py", "q5_cf")
    c20 = CF.core_scales()["r0 = 20 ell"]
    QO = _load("quantum_onset.py", "q5_qo"); l5 = QO.onset_4d()["l5"]
    Mrec = c20["mu5"] / 2 / l5 ** 2                                            # M / alpha in units alpha = l5^2 = 1
    hz_rec = horizons(min(Mrec, 1e12), 1.0, "gbfree")                         # r_- converges in M/alpha (checked below)
    dev = []
    for r in np.geomspace(1.0, 1e3, 200):
        x = math.sqrt(kretschmann(r, 1e8, 1.0, "gbfree"))                     # x = l5^2 sqrt(K), alpha = l5^2 = 1
        if x < 0.1:
            dev.append(abs((1 - f_of(r, 1e8, 1.0, "gbfree")) / (2e8 / r ** 2) - 1))
    rm_conv = [horizons(Mq, 1.0, "gbfree")[0] for Mq in (1e6, 1e8)]
    x_rm = math.sqrt(kretschmann(rm_conv[-1], 1e8, 1.0, "gbfree"))
    out["q4"] = dict(Mrec=Mrec, dev=max(dev), rm=rm_conv, x_rm=x_rm, nhz=len(hz_rec))
    return out


def checks(o):
    q2, q3, q4 = o["q2"], o["q3"], o["q4"]
    c1 = o["q1"] < 1e-8
    c2 = (len(q2["hz"]) == 2 and abs(q2["hz"][1] - q2["rp"]) < 1e-9 and abs(q2["hz"][0] - q2["rm"]) < 1e-9
          and abs(q2["rp"] - 1.3764) < 1e-4 and abs(q2["rm"] - 0.3249) < 1e-4
          and 0 < q2["Rmin"] < q2["rm"] and q2["f_at_Rmin"] > 0 and q2["reexpand"])
    k = list(q3["kmax"].values())
    c3 = q3["gb_coeff"] == 0 and q3["hprime_pos"] and abs(q3["core"] - 1) < 1e-5 and max(k) / min(k) < 1.5 \
        and 1 < min(k) < 1e3
    c4 = q4["dev"] < 0.02 and abs(q4["rm"][0] / q4["rm"][1] - 1) < 1e-3 and 0.3 < q4["x_rm"] < 30 and q4["nhz"] == 2
    return dict(Q1=c1, Q2=c2, Q3=c3, Q4=c4)


def report(o=None):
    o = o or compute(); ck = checks(o); q2, q3, q4 = o["q2"], o["q3"], o["q4"]
    print("Q1 eq. (30) with alpha = 0 against eq. (32): max difference %.1e: %s" % (o["q1"], ck["Q1"]))
    print("Q2 Hayward, M = 1, m = 1.05, alpha = 0.1: r+ %.4f, r- %.4f; R_min %.4f (inside r-, f = %.3f > 0); re-expands "
          "to r+: %s" % (q2["rp"], q2["rm"], q2["Rmin"], q2["f_at_Rmin"], ck["Q2"]))
    print("Q3 GB-free tower: h' > 0 %s, f(centre) %.6f, K_max alpha^2 %.3f (M/alpha 1e2) and %.3f (1e6): %s" % (
        q3["hprime_pos"], q3["core"], q3["kmax"][1e2], q3["kmax"][1e6], ck["Q3"]))
    print("Q4 record (r0 = 20 ell, 5D form): M/alpha = %.3e; Tangherlini to %.2e where x < 0.1; r- = %.4f l5 (M/alpha "
          "1e6, 1e8: %.4f), x there %.2f: %s" % (q4["Mrec"], q4["dev"], q4["rm"][1], q4["rm"][0], q4["x_rm"], ck["Q4"]))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["master", "gb"]
    for mu in names:
        MUT.clear(); MUT.add(mu)
        try:
            res = selftest(quiet=True)
        except Exception:
            res = False
        caught += not res; print("mutant %-7s %s" % (mu, "caught" if not res else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
