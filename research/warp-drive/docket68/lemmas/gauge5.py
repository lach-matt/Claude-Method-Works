#!/usr/bin/env python3
"""gauge5.py -- item 516: every gauge applicable to L-UNIF', measured against its five needs.

M, 516: "Deep research all gauges applicable to our specific needs".  The needs are L-UNIF''s (hf_theorem5 F7, item
515): N1 a well-posed problem on the theorem's domain (data at scri, a spacelike outflow boundary at x = 1, five
dimensions); N2 uniform linear control of a growing 5D hole in the T^2-mirror class over the shell's 269 r_h; N3 the
high-frequency remainder; N4 the interior reached to x = 1 with no excision (505); N5 the nonlinear closure.  Labels:
computed (exact unless marked), READ (outside art, by identifier), deduced, M's.

  G0 (M's) 516, verbatim.
  G1 (computed, exact) Maximal slicing stops far outside x = 1.  A spherically symmetric maximal slice through
     Tangherlini's vacuum at radius r needs C^2 >= mu r^4 - r^6, whose maximum 4 mu^3/27 sits at r_lim^2 = 2 mu/3:
     r_lim = sqrt(2/3) r_h (4D control: 3M/2).  Independently, the interior r = const slices are CMC with
     K(r) = (3 r^2 - 2 mu)/(r^2 sqrt(mu - r^2)), zero exactly at r_lim -- the two derivations agree.  In the T^2-reduced
     2+1 Einstein frame (g~ = rho^2 g_3, the frame of Huneau-Luk's elliptic gauge) the torus adds n(ln rho) and the
     maximal r = const slice moves out to r = (2/sqrt5) r_h.  With our universe's values (hf_anchor5): r_lim = 59,410
     l5 and 65,080 l5 against r_q = 460 l5 at the end: 129 and 141 times too far out.  The standard maximal foliation and
     every stationary Bona-Masso trumpet (maximal is the f -> infinity limit) freeze there (READ 0905.0450; Estabrook et
     al. 1973 for 4D), so reaching x = 1 needs excision, which 505 excludes.
  G2 (computed, exact) CMC slicing does reach x = 1: K(r) grows monotonically inward from 0 at r_lim to 0.688 l5^-1 at
     r_q, so a York-time foliation K = t passes x = 1 at a finite, sub-Planckian mean curvature.  But a K != 0 slice is
     hyperboloidal, and at scri five dimensions radiate as r^(-3/2): half-integer, so no smooth conformal
     compactification (READ Tanabe-Kinoshita-Shiromizu 1104.0303; Hollands-Ishibashi gr-qc/0304054).  CMC trades N4
     for N1's regularity at scri.
  G3 (computed, exact) The T^2 areal gauge degenerates in the hole.  With rho = sqrt(det h) = (r^2/2) sin 2theta,
     |grad rho|^2 = r^2 - mu sin^2 2theta: null on r = r_h |sin 2theta|, which meets every interior radius (r_q at
     |sin 2theta| = 0.00632) -- rho is neither a time nor a space coordinate across the interior (Le Floch-LeFloch's
     T^2 areal gauge is for T^3 cosmologies).
  G4 (computed, exact) Five dimensions help the nonlinear closure: waves decay as t^(-(n-1)/2) = t^(-3/2) for n = 4
     space dimensions, integrable (int_1^inf = 2, any shell length) where 4D's t^(-1) is not; so no null condition is
     needed in wave coordinates (READ Choquet-Bruhat-Chrusciel-Loizelet CQG 23 7383, for Minkowski; near the hole the
     local energy decay of Laul-Metcalfe 2012 and Schlue APDE 2013 supplies it, with trapping's derivative loss).
  G5 (READ) The geometric (GCM/Teukolsky) route has no 5D engine: perturbations decouple in D > 4 only on Kundt
     spacetimes, and black holes are not Kundt (Durkee-Reall 1009.0015).  Kodama-Ishibashi master equations (hep-th/
     0305185) and Hollands-Wald canonical energy (1201.0463) control the static hole only.  The only nonlinear 5D
     black-hole stability results (Dafermos-Holzegel gr-qc/0510051, Holzegel) are cohomogeneity two in double null.
  G6 (deduced) The matrix (MATRIX) and its rule: no gauge meets all five; every gauge on the table is excluded by a
     computed or READ failure except Bondi, double null and wave-map; N2 is met by none -- the obstruction there is the
     linear engine for a slowly growing 5D hole, not the gauge.  Recommendation: Bondi stays the computation gauge (F1-F7
     live there; its v is null); double null, angularly regular (Luk-Rodnianski 2009.08968), for the shell, the high
     frequencies (one null family of oscillation, inside their two) and the interior to x = 1; a wave-map gauge relative
     to the Vaidya approximant with constraint damping (Hintz 2302.13804; Touati 2402.17530 and Huneau-Luk 2403.03470
     for high frequency in it) for the exterior's long time, where G4's integrability closes the nonlinearity.

numpy, sympy.  Imports hf_anchor5.py by path.
python3 gauge5.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()
NEEDS = ("N1 well-posed on the domain", "N2 growing 5D hole, linear, 269 r_h", "N3 high-frequency remainder",
         "N4 interior to x = 1, no excision", "N5 nonlinear closure")
# status per need: M meets, P partial (in kind, 4D, or one part), F fails (with its ground), O open
MATRIX = {
    "Bondi-Sachs (computation gauge)": (
        ("P", "free evolution weakly hyperbolic in simple norms (2111.14794); symmetric hyperbolic in a special norm "
              "about Schwarzschild, 4D (Gundlach 2404.16720); 5D Bondi mass finite with half-integer orders (1104.0303)"),
        ("O", "no Bondi stability theory"),
        ("P", "F5: hypersurface equations v-derivative-free, rate products in R_vv alone (computed, hf_theorem5)"),
        ("M", "the sequence runs to x = 1 in it (computed, hf_core5)"),
        ("O", "no nonlinear Bondi framework")),
    "double null": (
        ("P", "characteristic problem well-posed (Luk 2012, 4D); 5D used in cohomogeneity two (gr-qc/0510051)"),
        ("P", "DHRT 2104.08222 closes 4D Schwarzschild on DHR's Teukolsky engine, which 5D lacks (G5)"),
        ("P", "Luk-Rodnianski 2009.08968: angularly regular, oscillation along <= 2 null families; ours along 1"),
        ("M", "both null coordinates regular across the horizon to the spacelike r = r_q (deduced)"),
        ("P", "teleological normalisation closes 4D (2104.08222); 5D decay faster (G4)")),
    "wave-map / generalized harmonic": (
        ("M", "Cauchy problem well-posed in every dimension (Choquet-Bruhat); spacelike outflow boundary needs no data"),
        ("P", "4D: Hintz-Vasy KdS, Johnson 1810.01337, Hafner-Hintz-Vasy; relative to a background 2302.13804; 5D none"),
        ("P", "high frequency in it: Touati 2402.17530, Huneau-Luk 2403.03470 (4D)"),
        ("O", "no result inside a 5D hole"),
        ("P", "no null condition needed in D >= 5 (G4, CBCL); near the hole via local energy decay")),
    "maximal + spatial elliptic": (
        ("M", "local existence, Huneau-Luk 1706.09499 (U(1) elliptic gauge)"),
        ("O", ""),
        ("P", "elliptic metric components tame high frequencies (Huneau-Luk); 5D diagonal T^2 reduces to 2+1 Einstein-"
              "scalars, their setting (deduced)"),
        ("F", "freezes at sqrt(2/3) r_h (2/sqrt5 r_h reduced), 129x r_q (computed, G1)"),
        ("O", "")),
    "CMC (York time, hyperboloidal)": (
        ("F", "K != 0 slices reach scri, where 5D fields go as r^(-3/2): no smooth compactification (G2)"),
        ("O", ""),
        ("P", "elliptic lapse and shift, as maximal (deduced)"),
        ("M", "K reaches 0.688/l5 at r_q, finite (computed, G2)"),
        ("O", "")),
    "puncture (1+log, Gamma-driver; BSSN/CCZ4)": (
        ("P", "strongly hyperbolic; 5D numerics exist (Figueras et al. 1512.04532); no proof framework"),
        ("O", ""), ("O", ""),
        ("F", "trumpet throat at r of order r_h; maximal is its f -> infinity limit (0905.0450; G1)"),
        ("O", "")),
    "GCM / Teukolsky frame": (
        ("P", "4D Kerr (Klainerman-Szeftel 2104.11857)"),
        ("F", "no decoupling for D > 4 black holes (Durkee-Reall 1009.0015)"),
        ("O", ""), ("O", ""), ("P", "4D")),
    "gauge-invariant (Kodama-Ishibashi, canonical energy)": (
        ("P", "linear only"),
        ("P", "static Tangherlini: mode stability (hep-th/0305185); E > 0 criterion (1201.0463); not a growing hole"),
        ("O", ""),
        ("F", "linear on a fixed background: no interior evolution of the nonlinear problem"),
        ("F", "not a gauge for the nonlinear equations")),
    "T^2 areal (Le Floch-LeFloch, Gowdy)": (
        ("P", "T^3 cosmologies"), ("O", ""), ("O", ""),
        ("F", "grad rho null on r = r_h |sin 2theta| inside (computed, G3)"),
        ("O", "")),
    "conformal (Friedrich)": (
        ("F", "no smooth null infinity for radiating solutions in odd D (1104.0303, gr-qc/0304054)"),
        ("O", ""), ("O", ""), ("O", ""), ("O", "")),
}
STACK = {"Bondi-Sachs (computation gauge)": "computation: F1-F7, v null",
         "double null": "shell, high frequency, interior to x = 1",
         "wave-map / generalized harmonic": "exterior, long time, nonlinear closure"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    return "Deep research all gauges applicable to our specific needs" in open(RULINGS).read()


def g1_g3():
    """maximal limit (two derivations, two frames), CMC reach, areal degeneracy -- exact"""
    r, mu, th = sp.symbols("r mu theta", positive=True)
    f = 1 - (mu/r if "four_d_f" in MUT else mu/r**2)
    rlim2 = sp.solve(sp.diff(mu*r**4 - r**6 if "four_d_f" not in MUT else -f*r**6, r), r)[0]**2
    ccrit2 = sp.simplify((mu*r**4 - r**6).subs(r**2, rlim2)) if "four_d_f" not in MUT else None
    K5 = sp.simplify(-sp.diff(r**3*sp.sqrt(mu/r**2 - 1), r)/r**3)        # n = -sqrt|f| d_r, future inward
    tor = 0 if "no_torus" in MUT else -2*sp.sqrt(mu - r**2)/r**2           # n(ln rho), rho = r^2 sin th cos th
    Kred = sp.simplify(K5 + tor)
    rred2 = sp.solve(sp.numer(sp.together(Kred)), r)
    rred2 = [s**2 for s in rred2 if s.is_positive][0]
    rho = r**2*sp.sin(2*th)/2
    sgn = -1 if "areal_sign" in MUT else 1
    g_rho = sp.simplify(sp.expand_trig(sgn*f*sp.diff(rho, r)**2 + sp.diff(rho, th)**2/r**2))
    f4 = 1 - 2*mu/r
    four = sp.solve(sp.diff(-f4*r**4, r), r)
    return dict(rlim2=sp.simplify(rlim2), ccrit2=ccrit2, K5=sp.factor(K5), K5_at_rlim=sp.simplify(K5.subs(r**2, rlim2)),
                Kred=sp.factor(Kred), rred2=sp.simplify(rred2), g_rho=g_rho,
                g_rho_target=sp.simplify(g_rho - (r**2 - mu*sp.sin(2*th)**2)), four=four, sym=(r, mu, th))


def anchored(e):
    """our universe's values, by path from hf_anchor5"""
    A = _load("hf_anchor5.py", "g5_hf_anchor5")
    R = A.a1()
    rh = R["rh_l5"]
    r, mu, th = e["sym"]
    rq = (np.sqrt(72)*rh**2)**0.25
    rlim = float(sp.sqrt(e["rlim2"]).subs(mu, rh**2))
    rred = float(sp.sqrt(e["rred2"]).subs(mu, rh**2))
    Kf = sp.lambdify(r, sp.Abs(e["K5"]).subs(mu, rh**2))
    grid = np.geomspace(rq, rlim*(1 - 1e-9), 2000)
    Kg = np.array([Kf(x) for x in grid])
    T = R["D"]*rh
    t = sp.symbols("t", positive=True)
    p = sp.Rational(1, 1) if "no_fifth_dim" in MUT else sp.Rational(3, 2)
    return dict(rh=rh, rq=rq, rlim=rlim, rred=rred, ratio=rlim/rq, ratio_red=rred/rq, K_q=float(Kf(rq)),
                K_monotone=bool(np.all(np.diff(Kg) < 0)), sin_q=rq/rh, T=T,
                decay_int=sp.integrate(t**-p, (t, 1, sp.oo)), decay_T=float(sp.integrate(t**-p, (t, 1, T))))


def matrix_rule():
    """G6: no gauge meets all five; outside the stack every gauge has an F; the stack has none; N2 met by none"""
    mx = {g: list(v) for g, v in MATRIX.items()}
    if "teukolsky_5d" in MUT:
        mx["GCM / Teukolsky frame"][1] = ("P", "assumed")
    full = [g for g, v in mx.items() if all(s == "M" for s, _ in v)]
    excluded = {g: [NEEDS[i] for i, (s, _) in enumerate(v) if s == "F"] for g, v in mx.items() if g not in STACK}
    stack_f = {g: [NEEDS[i] for i, (s, _) in enumerate(mx[g]) if s == "F"] for g in STACK}
    best = {n: max((mx[g][i][0] for g in STACK), key="OPM".index) for i, n in enumerate(NEEDS)}
    n2 = [g for g, v in mx.items() if v[1][0] == "M"]
    return dict(full=full, excluded=excluded, stack_f=stack_f, best=best, n2=n2, rows=mx)


def compute():
    e = g1_g3()
    return dict(words=words(), e=e, a=anchored(e), m=matrix_rule())


def checks(o):
    ch = {}
    ch["G0 words of 516"] = o["words"]
    e, a = o["e"], o["a"]
    r, mu, th = e["sym"]
    ch["G1 maximal limit r_lim^2 = 2 mu/3 (C^2 max 4 mu^3/27), K(r_lim) = 0 agrees; reduced frame 4 mu/5; 4D 3M/2"] = (
        sp.simplify(e["rlim2"] - 2*mu/3) == 0 and e["ccrit2"] is not None and sp.simplify(e["ccrit2"] - 4*mu**3/27) == 0
        and e["K5_at_rlim"] == 0 and sp.simplify(e["rred2"] - 4*mu/5) == 0 and e["four"] == [3*mu/2])
    ch["G1 anchored: r_lim = 59,410 l5 and 65,080 l5 vs r_q = 460 l5 -- over 100x outside x = 1"] = (
        abs(a["rlim"] - 59410) < 2 and abs(a["rred"] - 65080) < 2 and abs(a["rq"] - 460.3) < 0.5
        and a["ratio"] > 100 and a["ratio_red"] > a["ratio"])
    ch["G2 CMC reaches x = 1: |K| rises monotonically inward to 0.688/l5 at r_q"] = (
        a["K_monotone"] and abs(a["K_q"] - 2*a["rh"]/a["rq"]**2) < 1e-3 and 0.68 < a["K_q"] < 0.70)
    ch["G3 areal gauge: |grad rho|^2 = r^2 - mu sin^2 2theta, null on r = r_h|sin 2theta| (r_q at 0.00632)"] = (
        e["g_rho_target"] == 0 and abs(a["sin_q"] - 0.00633) < 1e-4)
    ch["G4 5D decay t^(-3/2) integrable: int_1^inf = 2, bounded over the shell's 269 r_h"] = (
        a["decay_int"] == 2 and a["decay_T"] < 2)
    m = o["m"]
    ch["G6 no gauge meets all five; every gauge outside the stack fails one; the stack fails none; N2 met by none"] = (
        not m["full"] and all(m["excluded"].values()) and not any(m["stack_f"].values()) and not m["n2"]
        and m["best"][NEEDS[3]] == "M" and m["best"][NEEDS[1]] == "P")
    return ch


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-112s %s" % (k, "PASS" if v else "FAIL"))
    e, a = o["e"], o["a"]
    print("  G1 r_lim^2 = %s; C_crit^2 = %s; K5 = %s; reduced K = %s, zero at r^2 = %s" % (
        e["rlim2"], e["ccrit2"], e["K5"], e["Kred"], e["rred2"]))
    print("     r_h = %.0f l5: r_lim = %.0f l5, reduced %.0f l5; r_q = %.1f l5; ratios %.1f, %.1f" % (
        a["rh"], a["rlim"], a["rred"], a["rq"], a["ratio"], a["ratio_red"]))
    print("  G2 |K(r_q)| = %.4f / l5 (2 r_h/r_q^2 = %.4f)" % (a["K_q"], 2*a["rh"]/a["rq"]**2))
    print("  G3 |grad rho|^2 = %s; r_q met at |sin 2theta| = %.5f" % (e["g_rho"], a["sin_q"]))
    print("  G4 int_1^inf t^-3/2 = %s; over T = %.4g l5: %.6f" % (a["decay_int"], a["T"], a["decay_T"]))
    m = o["m"]
    print("  G6 matrix (M meets, P partial, F fails, O open):")
    print("     %-52s %s" % ("gauge", "  ".join("N%d" % (i + 1) for i in range(5))))
    for g, v in m["rows"].items():
        print("     %-52s %s%s" % (g, "   ".join(s for s, _ in v), "   <- " + STACK[g] if g in STACK else ""))
    for g, fs in m["excluded"].items():
        print("     excluded %-45s fails %s" % (g, "; ".join(fs)))
    print("     stack's best per need: " + "; ".join("%s %s" % (n.split()[0], s) for n, s in m["best"].items()))
    return o


MUTANTS = {"four_d_f": "4D f = 1 - mu/r in the 5D computation (G1)",
           "no_torus": "the torus's n(ln rho) dropped from the reduced frame (G1)",
           "areal_sign": "the hole's g^rr sign flipped in |grad rho|^2 (G3)",
           "no_fifth_dim": "4D decay t^-1 in place of 5D's t^-3/2 (G4)",
           "teukolsky_5d": "Teukolsky decoupling assumed in 5D (G5 -> G6)"}


def selftest():
    o = compute(); c = checks(o); report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k[:40] for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-13s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
