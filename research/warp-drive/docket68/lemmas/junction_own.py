#!/usr/bin/env python3
"""junction_own.py -- item 388: the junction on position 2's face where the destination's own sigma differs from
ours, and position 2's open period at each end, for the general theorem rather than 218's applied example.  M, 388:
"we do need to compute this. You're basing your decision off an applied simplified example of the warp theorem."
Worked in the conversation (computed with sympy and floats, exact where marked; deduced where marked; not verified by
a separate session; not seated); no test run; 2026-10-14.

  G0 (read) M's words, verbatim in the rulings file: 388 (above); 387, "it should carry its own σ."; 226, "Each
     position 2 carries its own universe's values".
  G1 (computed, exact; m1p2x_index Y1 called) The junction's law, mu' = lambda_minus - lambda_plus, carries the two
     tensions and nothing else: no G, no ell, no kappa.  It is the plane's own stress conservation, so it holds at
     every destination whatever its own G2 and ell2.  On position 2's face, with the object's interior at our sigma
     (d_ours; m1p2x_oneway O3, O5), mu' = sigma - sigma2.  The jump is in SI, our tension against the destination's own.
  G2 (computed, exact) What emerges sees, over position 2's horizon sphere, 4 pi r2^2 (1/kappa2) E~ mu/|V|.  With the
     start mu_0 = a sigma |V_s| and b = 1 - sigma2/sigma, that is K0 [(a + b) e^(Dtau) - b] times E~ E2, and mu >= 0
     exactly while a + b (1 - e^(-Dtau)) >= 0.  Here K0 = 4 pi r2^2 (1/kappa2) sigma/E2, Dtau is in position 2's
     e-folds, and E2 is what position 2's face reads of the README.  Under 240 (b) (arrival_small V6; copy_p2 C1):
       - small end: K0 = (8/pi)(r_h/ell) g5^(4/3), with g5 = G5_2/G5;
       - large end: K0 = 12 (r0/ell)^2 (G2/G)^2.
     With one Kruskal geometry for both faces (V6's other reading) they are (8/pi)(r_h/ell) g5 and 12 (r0/ell)^2 G2/G.
  G3 (deduced from G2) The junction's longest open period, by the sign of the jump.
     - sigma2 < sigma (b > 0): the junction rises, from any start.  It closes the face at ln(1 + 1/(K0 b)) e-folds,
       longest from a = 0 (c_junction J1's criterion: what emerges meets more energy than the README carries).
     - sigma2 = sigma: no junction.
     - sigma2 > sigma (b < 0): the junction falls.  It needs a start, or mu < 0 at once on the face where positivity is
       owed (284, 285).  Take the start as the README's energy laid on the junction, at most E2 seen (m1p2x_fifth F1's
       reading; e_positive E7, the README supplying positivity at the face).  If K0 |b| <= 1 a start a = |b| covers
       the whole face and the junction never closes it.  Otherwise mu reaches zero within -ln(1 - 1/(K0 |b|)) e-folds.
     For K0 |b| >> 1 the two signs give the same period, 1/(K0 |b|) e-folds, to order 1/(K0 b)^2.
  G4 (computed; J2 READ) Position 2's open period is the shorter of the junction's and J2's short phase.  J2 is
     (Delta u)* <~ 2 r_s/c, Barcelo, Carballo-Rubio and Garay, an order, not exact (c_junction J2): two of position 2's
     e-folds at the small end, one at the large.  In our clocks (arrival_small V14 (c)'s conversion), one of position
     2's e-folds is r2/r_h of our r_h/c at the small end, and 4 r02/r0 of our GM/c^3 at the large.
  G5 (computed) Where the junction binds.
     - Small end: only if b > 1/(K0 (e^2 - 1)), about 7.7e13 for our own G5: sigma2 below -7.7e13 sigma.  At every
       destination of the record, 139 (1)'s quarter included, the open period is J2's.  J1's 33.6 clocks never bound.
     - Large end, at r0 = 10 ell and our own G: if sigma2 is below sigma by more than 4.85e-4 sigma, or above it by
       more than 1.32e-3 sigma; the band scales as (ell/r0)^2.  Then the period is about
       (ell/r0)^2/(3 (G2/G)^(3/2) |b|) of our clocks.
  G6 (computed) Why the interior carries our sigma wherever the jump would rise.  With the interior at sigma2 the
     junction would sit on our face, which stands at least the write's floor, 66,980 clocks (write_small S3), and since
     336 the hole's life.  A rising junction there closes within the same G3 period: about 33 clocks at the small end,
     well under one e-fold at the large.  So for sigma2 < sigma, d_ours is forced at both ends.  For sigma2 > sigma at
     the small end the junction is coverable on either face, and the open period is J2's either way.
  G7 (deduced) SOURCE's item 10 for the general theorem.  The README's arrival lasts less than position 2's open period
     at its destination -- a function of the destination's own (sigma2, G2, G5_2) and, at the large end, of r0.
     - Small end: J2's short phase at every destination, 2 g5^(1/3) of our clocks under 240 (b) (2 to 3.17 over the
       record's twelve and 139 (1)'s quarter; 1.41 at the inverse 2P step).  READ, an order.
     - Large end: J2's 4 (G2/G)^(1/2) clocks where sigma2 = sigma (4 ours, 5.66 at 2b and 2c).  Elsewhere the
       junction's, a small fraction of a clock: 1.57e-3 clocks at 2P, 5.6e-4 at 2b + 2P, 2.67e-3 on 139 (1)'s
       quarter, 3.14e-3 at the inverse 2P step (falling, bound by positivity), all at r0 = 10 ell.
     The 387 deduction ("its own sigma is ours, so no junction rises") holds for 218's example and the other
     destinations at our sigma, not for the theorem.

What this does not claim.
  - What closes position 2's face where no junction binds: J2 is READ, and nothing in M's rulings bounds it.
  - The falling junction's start: F1's reading, the README's energy laid on it; what supplies it is not ruled.
  - The clock conversion across the bounce (V14 (c)'s, through the quantum region, 273) and the face readings of V6.

Stdlib + sympy.  python3 junction_own.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys
from fractions import Fraction as F

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((388, "we do need to compute this. You're basing your decision off an applied simplified example of the warp "
               "theorem."), (387, "it should carry its own σ."),
         (226, "Each position 2 carries its own universe's values"))
J2_EFOLDS = {"small": 2.0, "large": 1.0}          # (Delta u)* <~ 2 r_s/c in position 2's e-folds (c_junction J2, READ)
R0_ELL = (10.0, 100.0)                            # the large end's r0/ell, as in arrival_large A4
_CACHE = {}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _item(n):
    text = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. (.*?)(?=^\d+\. )" % n, text, re.S | re.M)
    return " ".join((m.group(1) if m else text[text.find("\n%d. " % n):]).split())


def law():
    """G1: Y1's law called; on position 2's face (O3's orientation) with the interior at s_in"""
    if "law" not in _CACHE:
        _CACHE["law"] = _load("m1p2x_index.py", "jo_mi").junction_law()
    j = _CACHE["law"]
    sig, sig2 = sp.symbols("sigma sigma2", real=True)
    s_in = sig2 if MUT.get("interior_own") else sig             # the mutant: the interior at the destination's own
    # position 2's face: [lambda] = s2 - s_in (O3), so lambda_plus = s2, lambda_minus = s_in
    mp = j["mu_prime"].subs({j["lp"]: sig2, j["lm"]: s_in})
    if MUT.get("jump_flipped"):
        mp = -mp                                                 # the mutant: the law's sign reversed
    return dict(raw=j["mu_prime"], free=j["mu_prime"].free_symbols == {j["lp"], j["lm"]}, mp=sp.simplify(mp),
                sig=sig, sig2=sig2)


def closed_form():
    """G2: the seen energy from mu(V) = mu_0 + mu' (V - V_s), V = -|V_s| e^(-Dtau), per K0 E~ E2"""
    a, b, t, Vs = sp.symbols("a b Delta_tau V_s", positive=True)
    bb = sp.Symbol("b", real=True)
    sig = sp.Symbol("sigma", positive=True)
    V = -Vs * sp.exp(-t)
    mu = a * sig * Vs + bb * sig * (V - (-Vs))
    seen = sp.simplify(mu / (-V) / sig)                          # (mu/|V|)/sigma; times K0 E~ E2
    form = (a + bb) * sp.exp(t) - bb
    pos = sp.simplify(mu / (sig * Vs) - (a + bb * (1 - sp.exp(-t))))
    return dict(ok=sp.simplify(seen - form) == 0, pos_ok=pos == 0, form=form)


def k0(end, gG, g5, reading="b"):
    """G2's K0 per unit (8/pi)(r_h/ell) at the small end or 12 (r0/ell)^2 at the large; position 2's e-fold in ours"""
    if end == "small":
        r2, e2 = (g5 ** (1 / 3), g5 ** (-1 / 3)) if reading == "b" else (1.0, 1 / g5)
        if MUT.get("e_not_e2"):
            e2 = 1.0                                             # the mutant: the README's E for what position 2 reads
        return r2 ** 3 / e2, r2
    r2, e2 = (gG ** 0.5, gG ** -0.5) if reading == "b" else (1.0, 1 / gG)
    if MUT.get("e_not_e2"):
        e2 = 1.0
    return r2 ** 3 / e2, 4.0 * r2


def period_junction(K, b):
    """G3: the junction's longest open period in position 2's e-folds (inf where it never closes the face)"""
    if b > 0:
        return math.log1p(1 / (K * b))
    if b == 0 or K * abs(b) <= 1:
        return math.inf
    return -math.log1p(-1 / (K * abs(b)))


def open_period(end, K, b):
    """G4: the shorter of the junction's and J2's, in position 2's e-folds, and which binds"""
    pj = period_junction(K, b)
    if MUT.get("no_j2"):
        return pj, "junction"
    j2 = J2_EFOLDS[end]
    return (pj, "junction") if pj < j2 else (j2, "J2")


def destinations():
    """the record's twelve (bulk5_index), 139 (1)'s quarter, and the lattice's inverse 2P step (G/2, sigma x 4)"""
    B5 = _load("bulk5_index.py", "jo_b5")
    out = {}
    for n, d in B5.five_d().items():
        out[n] = dict(gG=float(d["gf"]), x=float(d["sf"]), g5=2.0 ** float(d["e"]["G5"]))
    out["139 (1) quarter"] = dict(gG=1.0, x=-0.25, g5=1.0)
    e = B5.exps_gs(F(-1), F(2))
    out["inverse 2P (G/2, 4 sigma)"] = dict(gG=2.0 ** float(e["G"]), x=2.0 ** float(e["sigma"]),
                                            g5=2.0 ** float(e["G5"]))
    return out


def example():
    """the small end's r_h/ell (c_junction's example) and the record's two quarter periods (J1, close_large L4)"""
    if "ex" not in _CACHE:
        cj = _load("c_junction.py", "jo_cj")
        x = cj.example(cj.seen())
        cl = _load("close_large.py", "jo_cl")
        WS = _load("write_small.py", "jo_ws")
        _CACHE["ex"] = dict(rh_ell=1 / x["ell_over_rh"], j1=x["t_full"], l4=cl.l4()["clocks10"],
                            floor=float(WS.head_clocks()))
    return _CACHE["ex"]


def table(ex, bfun, reading="b"):
    rows = {}
    base_s = 8 / math.pi * ex["rh_ell"]
    for n, d in destinations().items():
        sig_k = abs(d["x"]) if MUT.get("sigma2_in_k0") else 1.0  # the mutant: the destination's own sigma in K0
        b = bfun(d["x"])                                         # b = mu'/sigma from G1's law, at sigma2 = x sigma
        ks, efs = k0("small", d["gG"], d["g5"], reading)
        p_s, w_s = open_period("small", base_s * ks * sig_k, b)
        row = dict(b=b, small=(p_s * efs, w_s), large={})
        for q in R0_ELL:
            kl, efl = k0("large", d["gG"], d["g5"], reading)
            p_l, w_l = open_period("large", 12 * q * q * kl * sig_k, b)
            row["large"][q] = (p_l * efl, w_l)
        rows[n] = row
    return rows


def compute():
    lw = law()
    ex = example()
    cf = closed_form()
    base_s = 8 / math.pi * ex["rh_ell"]
    sig, sig2 = lw["sig"], lw["sig2"]
    bfun = lambda x: float(lw["mp"].subs({sig: 1, sig2: x}))
    quarter_b = bfun(-0.25)
    rows = table(ex, bfun)
    rows_k = table(ex, bfun, "k")
    b_star_small = 1 / (base_s * (math.e ** 2 - 1))
    band = {q: (1 / (12 * q * q * (math.e - 1)), 1 / (12 * q * q * (1 - math.exp(-1)))) for q in R0_ELL}
    sym = [(period_junction(K, 1.0), period_junction(K, -1.0)) for K in (1e2, 1e4)]
    d_ours = period_junction(base_s, 0.75)                      # the rising case on our face, 2P's jump, small end
    return dict(lw=lw, sigma_jump=sp.simplify(lw["mp"] - (sig - sig2)) == 0, ex=ex, cf=cf, rows=rows, rows_k=rows_k,
                j1_re=period_junction(base_s, quarter_b), l4_re=4 * period_junction(12 * 100, quarter_b),
                b_star_small=b_star_small, band=band, sym=sym, d_ours=d_ours)


def report(o):
    print("junction_own.py -- the junction where position 2's own sigma differs from ours (item 388)\n")
    print("G1 law mu' = %s (only the two tensions: %s); on position 2's face, mu' = %s"
          % (o["lw"]["raw"], o["lw"]["free"], o["lw"]["mp"]))
    print("G2 seen/(K0 E~ E2) = %s (verified: %s; mu >= 0 form: %s)"
          % (o["cf"]["form"], o["cf"]["ok"], o["cf"]["pos_ok"]))
    print("G3 reproduced on 139 (1)'s quarter: small end %.2f clocks (J1 %.2f); large end %.3e clocks at 10 ell "
          "(close_large L4 %.3e)" % (o["j1_re"], o["ex"]["j1"], o["l4_re"], o["ex"]["l4"]))
    print("G5 small end: the junction binds only for b > %.2e; large end band (rising, falling) at r0/ell: %s"
          % (o["b_star_small"], {q: ("%.2e" % a, "%.2e" % c) for q, (a, c) in o["band"].items()}))
    print("G6 a rising junction on our face (2P's jump) closes within %.1f clocks, against the write's floor %.0f"
          % (o["d_ours"], o["ex"]["floor"]))
    print("G7 position 2's open period in our clocks (240 (b); one-r_h reading in brackets):")
    print("  %-26s %7s %18s %24s %24s" % ("destination", "b", "small end", "large, r0 = 10 ell", "large, r0 = 100 ell"))
    for n, r in o["rows"].items():
        k = o["rows_k"][n]
        f = lambda v, w: "%.3g %s" % (v, w)
        print("  %-26s %7.3g %18s %24s %24s" % (n, r["b"], f(*r["small"]) + " [%.3g]" % k["small"][0],
                                                  f(*r["large"][10.0]) + " [%.3g]" % k["large"][10.0][0],
                                                  f(*r["large"][100.0]) + " [%.3g]" % k["large"][100.0][0]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rows, ex = o["rows"], o["ex"]
    add("G0 388, 387 and 226 verbatim in their items", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("G1 the law carries the two tensions only; on position 2's face with our interior, mu' = sigma - sigma2",
        o["lw"]["free"] and o["sigma_jump"])
    add("G2 the seen energy K0 [(a + b) e^Dtau - b] and the condition mu >= 0, from mu(V) and V(tau)",
        o["cf"]["ok"] and o["cf"]["pos_ok"])
    add("G3 reproduces the record on 139 (1)'s quarter: J1's 33.6 clocks and close_large L4's 2.67e-3 at 10 ell",
        "%.1f" % o["j1_re"] == "%.1f" % ex["j1"] == "33.6" and abs(o["l4_re"] / ex["l4"] - 1) < 1e-9
        and "%.3g" % o["l4_re"] == "0.00267")
    add("G3 rising below our sigma, none at it, falling above: 2P and the quarter rise, inverse 2P falls; the two "
        "signs agree to order 1/(K0 b)^2", rows["2P"]["b"] > 0 and rows["ours"]["b"] == 0
        and rows["inverse 2P (G/2, 4 sigma)"]["b"] < 0
        and all(abs(r - f) < 2 / K ** 2 for (r, f), K in zip(o["sym"], (1e2, 1e4))))
    add("G4-G5 small end: J2 binds at every destination, the quarter included; the junction only past b = 7.7e13",
        all(r["small"][1] == "J2" for r in rows.values()) and 7e13 < o["b_star_small"] < 8e13)
    lg = {n: r["large"][10.0] for n, r in rows.items()}
    add("G5 large end at 10 ell: the junction binds wherever sigma2 differs; J2 where it does not; band 4.85e-4/1.32e-3",
        all(lg[n][1] == ("J2" if rows[n]["b"] == 0 else "junction") for n in lg)
        and "%.3g" % o["band"][10.0][0] == "0.000485" and "%.3g" % o["band"][10.0][1] == "0.00132")
    add("G6 a rising junction on our face closes within about 33 clocks, far under the write's 66,980-clock floor",
        30 < o["d_ours"] < 40 and ex["floor"] > 6e4)
    add("G7 large end at 10 ell: 2P 1.57e-3 clocks, 2b + 2P 5.6e-4, the quarter 2.67e-3; ours 4, 2b 5.66 (240 (b))",
        "%.3g" % lg["2P"][0] == "0.00157" and "%.2g" % lg["2b+2P"][0] == "0.00056"
        and "%.3g" % lg["139 (1) quarter"][0] == "0.00267" and lg["ours"][0] == 4.0
        and "%.3g" % lg["2b"][0] == "5.66")
    rec = [r["small"][0] for n, r in rows.items() if not n.startswith("inverse")]
    add("G7 small end: 2 to 3.17 of our clocks over the record's twelve and the quarter, 1.41 at inverse 2P (240 (b))",
        min(rec) == 2.0 and "%.3g" % max(rec) == "3.17"
        and "%.3g" % rows["inverse 2P (G/2, 4 sigma)"]["small"][0] == "1.41")
    return res


MUTANTS = {"jump_flipped": "the junction's law with its sign reversed (G1)",
           "interior_own": "the object's interior at the destination's own sigma, not ours (G1, G6)",
           "e_not_e2": "the README's E taken for what position 2's face reads, under 240 (b) (G2)",
           "sigma2_in_k0": "the destination's own sigma in K0 for our interior's (G2)",
           "no_j2": "the J2 short phase not taken, the junction's period alone (G4)"}


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
        print("  mutant %-13s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
