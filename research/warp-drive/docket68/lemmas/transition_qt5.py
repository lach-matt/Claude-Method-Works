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

  Q5 (computed; READ, 2412.02740v2 p. 15, case (3): "assume that M > m ... it will reach R = 0 with finite kinetic
     energy, so that the shell will cross R = 0 in a smooth way") An unbound shell (M = 1, m = 0.5) on each of three
     towers has Rdot^2 > 0 at every radius, tending to E = M^2/m^2 - 1 at the centre and far off: no turning point, so it
     crosses the regular centre and expands without end -- out through r_- and the white hole's r_+ into the new
     universe, one way (the bound shell's cycle, Q2, needs M < m).
  Q6 (computed) The null limit, m/M -> 0, the README's own case (a null shell, 438): V(R) = E - Rdot^2 converges to a
     bounded function (m/M = 1e-2 and 1e-3 agree to 2e-2), so Rdot^2 = E - V never vanishes: the null shell crosses the
     centre and leaves the same way.  A radial null ray in any of these geometries has dr/dlam = +-E exactly (affine,
     f-free), through a centre that is smooth.
  Q7 (computed) The result is the tower's, not one choice of couplings: Hayward (h = psi/(1 - alpha psi)), the log tower
     (h = -ln(1 - alpha psi)/alpha) and the Gauss-Bonnet-free tower each give a regular core, K bounded the same at
     M/alpha = 1e2 and 1e6, two horizons with r_- of order sqrt(alpha), and a bound shell's turning point inside r_-.

  Q8 (computed; estimate in its reading) The inner horizon's surface gravity is kappa_- = 1/l5 (GB-free tower, M/alpha
     = 1e8).  The README is a long wave train (core_face: its quanta 56.96 r0 long at the large end), so its first parts,
     out through the centre, cross its later parts still falling in: counter-streaming fluxes at r_-, the setting of
     mass inflation (Poisson and Israel; for regular cores, Carballo-Rubio et al., cited by 2404.07058v2, not read here).
     By that mechanism the blueshift runs kappa_- dv = 1.0e23 e-folds at r0 = 20 ell and 1.4e29 at 2.8e7 ell: the static
     core cannot be assumed through the README's own passage.  READ, 2404.07058v2 p. 9: "inner extremal solutions only
     exist for a specific value of the mass" (kappa_- = 0, no mass inflation, in every quasi-topological theory); READ,
     2412.02740v2 p. 1: "evidence for a solution-independent upper bound on the curvature" (no singularity, if it holds).

What this proves and does not: 273's transition -- the README falling in through our face, crossing a regular centre
and leaving through a white hole into a new universe, one way -- is computed in five dimensions from the gravitational
effective action alone (no exotic matter), the shell's dynamics exact in spherical symmetry, every correction confined
to x ~ 1, for the README's own null shell (Q6) and every unbound shell (Q5), on three towers (Q7).  Two things are not
proved here: (a) that nature's higher-curvature coefficients meet the regularity conditions (READ, 2412.02742v2 p. 3:
"alpha_n (D - 2n) >= 0 for all n, lim |alpha_n|^(1/n) = C > 0 are sufficient"), which only the ultraviolet theory can
decide -- their scale is l5 by quantum_onset; and (b) the inner horizon beyond spherical symmetry: in the collapse
"the inner horizon is no longer a Cauchy horizon" (READ, 2412.02740v2 p. 18), but its stability to non-spherical
perturbations is not computed -- and Q8 shows the README's own spread is such a perturbation, 1e23 e-folds strong by
the mass-inflation mechanism; whether the README still leaves through the white hole then needs the counter-streaming
evolution in the theory's own spherical dynamics, not computed.  At the record's scales the bulk's Lambda enters the core at (l5/ell)^2 ~ 1e-40.

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
    if model == "log":                                                       # h = -ln(1 - a psi)/a
        return -math.expm1(-a * y) / a
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
    # Q5: an unbound shell (M > m): no turning point, it crosses R = 0 with Rdot^2 -> E and expands to infinity
    Rg = np.geomspace(1e-3, 30.0, 60)
    q5 = {}
    for model in ("hayward", "log", "gbfree"):
        mu = 0.5 if "bound" not in MUT else 1.05
        Eu = 1.0 / mu ** 2 - 1
        sv = [rdot2(R, 1.0, mu, 0.1, model) for R in Rg]
        q5[model] = dict(all=all(v is not None for v in sv),
                         minv=min(v for v in sv if v is not None) if any(v is not None for v in sv) else -1,
                         E=Eu, ends=(sv[0], sv[-1]))
    out["q5"] = q5
    # Q6: the null limit m/M -> 0: V(R) = E - Rdot^2 converges to a bounded function, no turning point anywhere
    Vn = {}
    for mu in (1e-2, 1e-3):
        En = 1.0 / mu ** 2 - 1
        Vn[mu] = [En - rdot2(R, 1.0, mu, 0.1, "gbfree") for R in (0.05, 0.2, 0.5, 1.0, 3.0)]
    out["q6"] = Vn
    # Q7: three towers (Hayward, log, GB-free): regular core, K bounded and mass-independent, two horizons with r- ~
    # sqrt(alpha), a bound shell's turning point inside r-
    q7 = {}
    for model in ("hayward", "log", "gbfree"):
        ks = [max(kretschmann(r, Mq, 1.0, model) for r in np.geomspace(1e-3, 3.0, 300)) for Mq in (1e2, 1e6)]
        hz7 = horizons(1e6, 1.0, model)
        sb = [rdot2(R, 1.0, 1.05, 0.1, model) for R in np.geomspace(0.02, 3.0, 80)]
        rmin7 = min(R for R, v in zip(np.geomspace(0.02, 3.0, 80), sb) if v is not None)
        q7[model] = dict(core=f_of(1e-3, 1e6, 1.0, model), k=ks, hz=hz7, rmin=rmin7, rm=horizons(1.0, 0.1, model)[0])
    out["q7"] = q7
    # Q8: the inner horizon's surface gravity at the record's scale, and the README's own spread against it
    rmq = horizons(1e8, 1.0, "gbfree")[0]
    kap = abs(f_of(rmq * (1 + 1e-6), 1e8, 1.0, "gbfree") - f_of(rmq * (1 - 1e-6), 1e8, 1.0, "gbfree")) / (4 * rmq * 1e-6)
    ell_ = QO.onset_4d()["ell"]
    out["q8"] = dict(kap=kap, efolds={k: kap * 56.96 * r0 / l5 for k, r0 in (("r0 = 20 ell", 20 * ell_),
                                                                             ("r0 = 2.8e7 ell", 2.8e7 * ell_))})
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
    q5, q6, q7 = o["q5"], o["q6"], o["q7"]
    c5 = all(v["all"] and v["minv"] > 0 and abs(v["ends"][0] / v["E"] - 1) < 0.05 and abs(v["ends"][1] / v["E"] - 1) < 0.05
             for v in q5.values())
    a6, b6 = q6[1e-2], q6[1e-3]
    c6 = all(abs(x) < 5 for x in b6) and max(abs(x - y) for x, y in zip(a6, b6)) < 2e-2
    c7 = all(abs(v["core"] - 1) < 1e-5 and max(v["k"]) / min(v["k"]) < 1.5 and len(v["hz"]) == 2 and 0.3 < v["hz"][0] < 3
             and v["rmin"] < v["rm"] for v in q7.values())
    c8 = abs(o["q8"]["kap"] - 1) < 1e-6 and min(o["q8"]["efolds"].values()) > 1e20
    return dict(Q1=c1, Q2=c2, Q3=c3, Q4=c4, Q5=c5, Q6=c6, Q7=c7, Q8=c8)


def report(o=None):
    o = o or compute(); ck = checks(o); q2, q3, q4 = o["q2"], o["q3"], o["q4"]
    print("Q1 eq. (30) with alpha = 0 against eq. (32): max difference %.1e: %s" % (o["q1"], ck["Q1"]))
    print("Q2 Hayward, M = 1, m = 1.05, alpha = 0.1: r+ %.4f, r- %.4f; R_min %.4f (inside r-, f = %.3f > 0); re-expands "
          "to r+: %s" % (q2["rp"], q2["rm"], q2["Rmin"], q2["f_at_Rmin"], ck["Q2"]))
    print("Q3 GB-free tower: h' > 0 %s, f(centre) %.6f, K_max alpha^2 %.3f (M/alpha 1e2) and %.3f (1e6): %s" % (
        q3["hprime_pos"], q3["core"], q3["kmax"][1e2], q3["kmax"][1e6], ck["Q3"]))
    print("Q4 record (r0 = 20 ell, 5D form): M/alpha = %.3e; Tangherlini to %.2e where x < 0.1; r- = %.4f l5 (M/alpha "
          "1e6, 1e8: %.4f), x there %.2f: %s" % (q4["Mrec"], q4["dev"], q4["rm"][1], q4["rm"][0], q4["x_rm"], ck["Q4"]))
    for k, v in o["q5"].items():
        print("   Q5 %-7s unbound shell (M = 1, m = 0.5, E = %.0f): Rdot^2 > 0 at every R (min %.3f), -> E at R -> 0 (%.3f) "
              "and at R = 30 (%.3f)" % (k, v["E"], v["minv"], v["ends"][0], v["ends"][1]))
    print("Q5 no turning point: the shell crosses the regular centre and expands to infinity in the new universe: %s"
          % ck["Q5"])
    print("Q6 null limit, V(R) at R = 0.05, 0.2, 0.5, 1, 3: m/M = 1e-2 %s; 1e-3 %s: %s" % (
        ", ".join("%.4f" % x for x in o["q6"][1e-2]), ", ".join("%.4f" % x for x in o["q6"][1e-3]), ck["Q6"]))
    for k, v in o["q7"].items():
        print("   Q7 %-7s f(centre) %.6f, K_max alpha^2 %.2f / %.2f (M/alpha 1e2 / 1e6), r- %.4f sqrt(alpha) at 1e6, "
              "bound shell's turning point %.4f < r- %.4f" % (k, v["core"], v["k"][0], v["k"][1], v["hz"][0], v["rmin"],
                                                               v["rm"]))
    print("Q7 the same on three towers: %s" % ck["Q7"])
    print("Q8 inner horizon kappa_- = %.6f / l5; over the README's spread (56.96 r0) kappa_- dv = %s: %s" % (
        o["q8"]["kap"], ", ".join("%.2e (%s)" % (v, k) for k, v in o["q8"]["efolds"].items()), ck["Q8"]))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["master", "gb", "bound"]
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
