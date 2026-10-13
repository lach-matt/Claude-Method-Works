#!/usr/bin/env python3
"""c_junction.py -- item 272's owed items (c) and (a) on the bounce of item 273: the junction's start and end, and the
white-hole face's blueshift (Eardley).  They are one question: on position 2's white-hole face the junction's energy,
seen by what emerges, grows as e^(clocks), and so does any inflow's.  Worked in the conversation (computed with sympy,
exact where marked; READ where marked; estimates marked; deduced where marked; not verified by a separate session; not
seated); 2026-10-12.

[M, item 277: "You are forgetting that the passage is one-way only".  J2's perturbations and J5's inflow onto the white-hole face are a passage from position 2 into the
corridor, item 270's own example; J1 (what emerges sees the junction) is outflow and stands.  Kept as written; the
one-way re-closure is i_oneway.py.]

  J0 (read) M's item-273 words, verbatim in the rulings file.
  J1 (computed, exact) The junction seen on position 2's face.  The face is U = 0, V < 0, generator d_V; position 2's
     forward time runs V = -|V_s| e^(-(tau_2 - tau_s)) toward 0 (m1p2x_oneway O1).  Matter emerging across the face at V
     with Killing energy E~ sees the junction's surface energy mu E~/(kappa |V|) (m1p2x_fifth F1 with U and V
     exchanged), over the plane's horizon sphere 4 pi r_h^3 E~ mu/|V|.  With the interior at our tension the junction
     rises, mu = mu_0 + (5/4) sigma (V - V_s) (m1p2x_oneway O3); from mu_0 = 0 the seen energy is (10/pi)(r_h/ell) E~ E
     (e^(Delta tau_2) - 1) -- it reaches E~ E at Delta tau_2 = ln(1 + (pi/10)(ell/r_h)) = 33.6 clocks at the example
     README.  Past that, what emerges meets more energy in the junction than the README carries: position 2's
     white-hole face can stay open at most 33.6 of position 2's clocks.
  J2 (READ) Barcelo, Carballo-Rubio & Garay, arXiv:1511.00633: "transitions with long characteristic time scales are
     pathologically unstable: occasional perturbations away from the perfect vacuum around these compact objects, even
     if being imperceptibly small, suffocate the white-hole explosion" (abstract); for short ones the white-hole horizon
     lasts (Delta u)* <~ r_m <~ 2 r_s (eq. (30), p.17), and inhibiting it needs (Delta M)* >~ 0.28 M (eq. (25), p.15);
     the long (Haggard-Rovelli) scale t_P (M/m_P)^2 against the short t_P (M/m_P) (eqs. (32)-(33), p.20).  So both J1
     and the literature say position 2's white hole must be brief.
  J3 (deduced; H-ASYMMETRIC-BOUNCE, the board's) The bounce is asymmetric: a long black-hole phase on our side -- the
     hold, at least the write's floor (66,980 clocks, write_small S3) -- and a brief white-hole phase on position 2's.
     b_bounce Q1's isometry gives the two views; it does not make their durations equal, because the faces lie in
     different exteriors whose Killing times are joined only through the quantum region (m1p2x_oneway O1).  A strictly
     time-symmetric bounce (Haggard and Rovelli's) would open position 2's white hole for as long as our hold: J1's
     junction would outweigh the README e^66980-fold and J2's instability would close it.
     [Item 338 (with item 340), seated after C8's verdict (its verifier loaded this file): since 336 our face stands the
     hole's life, 8.57e14 clocks; since 340 the board reads the README's arrival as compact, within 4.79 clocks
     (arrival_small V2, V11), so even a bounce that kept the span would carry the README's crossing within position 2's
     33.6-clock open period -- the asymmetry is not needed for the crossing (arrival_small V8 (3)). It stays for the
     faces' durations, ours the life and position 2's at most 33.6 clocks (the board's, named at 341 (Q10)).]
  J4 (computed) The junction's ends.  Start: position 2's face opens where the quantum region releases the white
     hole; any mu_0 >= 0 serves, the junction only rising.  End: the closing, within J1's 33.6 clocks; at J2's short
     duration (about two clocks) the junction's seen energy is (10/pi)(r_h/ell)(e^2 - 1) E~ E = 1.6e-14 E~ E -- what
     position 2 receives with the README at the closing beside E itself (E1, E2), drawn from the plane's change of
     tension.  Our black-hole face carries no junction (the interior at our tension, m1p2x_oneway O5); its ends are the
     formation and the bounce.
  J5 (computed; J2's criterion) The white-hole blueshift closed.  Any inflow from position 2 meeting the face is
     blueshifted at most e^(33.6) = 3.9e14 = (pi/10)(ell/r_h) over J1's open period -- not C7's e^66980 (item 271 (3)),
     which took the face open for the write's floor.  J2's short-scale threshold is an inflow of 0.28 E; position 2's
     ambient radiation onto the face's sphere over the open period, as blackbody flux, is 9.1e-72 J at 3 K and 1.1e-33 J
     at 1e10 K -- 80 and 41 orders of magnitude below it at the example (E = 1.281e9 J; clock 3.74e-29 s).
     [Item 341 (the C8 verifier's (Q3)): J5's inflow was marked at item 277 a passage from position 2 into the corridor
     (this file's item-277 note); the C7 verifier's critic re-admitted its bound at 319, as what rays hugging the face,
     never crossing it, could deliver to what emerges, and 330 seated it -- a board reading, not M's. Barcelo's 0.28 M
     (their eq. (25)) is a threshold for white-hole horizons lasting about 2 r_s; at the 33.6-e-fold face their eqs.
     (17) and (20) give about 1e-15 E, which the unblueshifted bath still clears by 65 and 27 orders. Under the G5
     readings with sigma fixed the bound is e^34.53 = 9.9e14 (c8_level V10).]

What this does not show.
  - The asymmetric bounce as a metric (J3 names it); the quantum region's near-horizon part (b_bounce Q6).
  - Where the junction's 1.6e-14 E comes from in the energy ledger beyond "the plane's change of tension" (E1's E_P2 =
    E exactly is then exceeded by that amount).
  - Position 2's ambient fields other than a blackbody bath.

Imports write_small.py and p2_gravity.py by path.  Stdlib + sympy.  python3 c_junction.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M273 = "Quantum bounce to pos 2 (Recommended)"
N_EX = 2742570311524972


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def seen():
    """the junction's seen energy on position 2's face, from mu_0 = 0, over E~ E, against position 2's forward time"""
    rh, ell, dt = sp.symbols("r_h ell Delta_tau", positive=True)
    jump = sp.Rational(5, 4)
    if MUT.get("falling"):
        jump = -jump                                       # the mutant lets the junction fall on position 2's face
    # E_obs/E~ = 4 pi r_h^3 mu/|V|, mu = jump sigma (|V_s| - |V|), |V| = |V_s| e^(-dt); sigma = 3 c^4/(4 pi G ell^2),
    # E = 3 pi c^4 r_h^2/(8 G ell): 4 pi r_h^3 (5/4) sigma / E = (10/pi)(r_h/ell)
    prefactor = sp.simplify(4 * sp.pi * rh ** 3 * jump * (3 / (4 * sp.pi * ell ** 2)) / (3 * sp.pi * rh ** 2 / (8 * ell)))
    ratio = prefactor * (sp.exp(dt) - 1)
    t_full = sp.solve(sp.Eq(ratio, 1), dt)
    return dict(prefactor=prefactor, ratio=ratio, t_full=[sp.simplify(x) for x in t_full], rh=rh, ell=ell, dt=dt)


def example(s):
    PG = _load("p2_gravity.py", "cj_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    E = 3 * math.pi * PG.C ** 4 * rh ** 2 / (8 * PG.G * PG.ELL_MAX)
    clock = rh / PG.C
    sub = {s["rh"]: rh, s["ell"]: PG.ELL_MAX}
    t_full = float(s["t_full"][0].subs(sub)) if s["t_full"] and s["t_full"][0].is_real is not False else float("nan")
    short = float(s["ratio"].subs(sub).subs(s["dt"], 2))
    blue = math.exp(t_full) if t_full == t_full else float("nan")
    sigma_SB = 5.670374419e-8
    bath = {T: sigma_SB * T ** 4 * 4 * math.pi * rh ** 2 * t_full * clock for T in (3.0, 1e10)}
    WS = _load("write_small.py", "cj_ws")
    return dict(rh=rh, E=E, clock=clock, t_full=t_full, short=short, blue=blue, ell_over_rh=PG.ELL_MAX / rh,
                bath=bath, threshold=0.28 * E, floor=WS.head_clocks())


def compute():
    s = seen()
    return dict(s=s, ex=example(s))


def report(o):
    s, x = o["s"], o["ex"]
    print("c_junction.py -- the junction's ends and the white-hole blueshift on the bounce (items 272 (c), (a))\n")
    print("J1 seen junction / (E~ E) = %s; reaches 1 at Delta tau_2 = %s = %.2f clocks" % (s["ratio"], s["t_full"],
                                                                                        x["t_full"]))
    print("J4 at two clocks (J2's short duration): %.3g E~ E" % x["short"])
    print("J5 the inflow's blueshift at most e^%.1f = %.3g (pi/10 ell/r_h = %.3g); J2's threshold 0.28 E = %.3g J; a "
          "blackbody bath onto the face over the open period: %s" % (
              x["t_full"], x["blue"], math.pi / 10 * x["ell_over_rh"], x["threshold"],
              ", ".join("%.3g K -> %.2g J" % kv for kv in x["bath"].items())))
    print("   the hold on our side, at least the write's floor: %.0f clocks" % x["floor"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("J0 M's item-273 words verbatim in the rulings file", M273 in rul)
    s, x = o["s"], o["ex"]
    rh, ell = s["rh"], s["ell"]
    ok = sp.simplify(s["prefactor"] - 10 * rh / (sp.pi * ell)) == 0
    ok &= len(s["t_full"]) == 1 and sp.simplify(s["t_full"][0] - sp.log(1 + sp.pi * ell / (10 * rh))) == 0
    ok &= "%.1f" % x["t_full"] == "33.6"
    add("J1 the junction seen on position 2's face grows as (10/pi)(r_h/ell)(e^Delta tau - 1) E~ E, reaching E~ E at "
        "ln(1 + (pi/10)(ell/r_h)) = 33.6 clocks", ok)
    ok = "%.2g" % x["short"] == "1.6e-14" and "%.2g" % x["blue"] == "3.9e+14"
    ok &= abs(x["blue"] / (1 + math.pi / 10 * x["ell_over_rh"]) - 1) < 1e-9
    add("J4/J5 at two clocks the junction is 1.6e-14 E~ E; an inflow's blueshift over the open period is at most "
        "3.9e14 = 1 + (pi/10)(ell/r_h)", ok)
    ok = x["bath"][3.0] < 1e-70 and x["bath"][1e10] < 1e-30 and x["threshold"] > 1e8
    ok &= x["bath"][1e10] / x["threshold"] < 1e-40
    add("J5 a blackbody bath of position 2 onto the face over the open period is >= 40 orders below J2's 0.28 E "
        "threshold, at 3 K and at 1e10 K", ok)
    return res


MUTANTS = {"falling": "the junction taken to fall on position 2's white-hole face"}


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
        print("  mutant %-8s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
