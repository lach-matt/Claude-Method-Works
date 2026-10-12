#!/usr/bin/env python3
"""hold_small.py -- item 251's last step at the family's small end: O1b/O1c restated (item 259), and the hold against the
hole's temperature.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; estimates
marked; verified once -- item 267, CONFIRMED with qualifications, all seated below in [Verifier, item 267] notes
(205/206); not seated); 2026-10-11.  First headed "... not verified by a separate session ...".  L4 re-read on item 260
against the write's count redone at the small end (write_small.py); first written with the record's 4D count.

[Auditing agent, item 281 (the reverse passage, 270/276): L1's passage along the bridge's slice is localized_hole H4's
eternal bridge (C1); put to M with it.  Kept as written.]

  L0 (read) M's item-259 words, verbatim in the rulings file.
  L1 (computed, exact; item 259) O1b/O1c at the small end: the static bulk, its horizon and the bridge's slice are
     regular (C1 H4-H5, verified, item 254) and the passage -- the README crossing as information across the bridge's
     slice (item 251) -- needs no geodesic through the interior.  The interior is where the incompleteness lives: a body
     falling from rest at radius R reaches r = 0 in proper time R^2/(r_h c) (computed), one clock r_h/c from rest at the
     horizon -- finite, outside the passage, admitted by item 259.  [Verifier, item 267: "computed, exact" covers the
     integral only; "the passage needs no geodesic through the interior" is M's ruling (item 259), not a computation.
     On any radial free fall the horizon-to-r = 0 time is r_h/(c (1 + E~)), E~ the specific energy (computed, L5) --
     at most one clock, its E~ -> 0 limit; no body rests at the horizon.  No causal curve crosses the bridge (C1), and
     any signal entering it ends at r = 0 within r_h/c, so "outside the passage" holds on the reading where the passage
     lies along the spacelike slice.]
  L2 (computed, exact) The hole's capture radius for fields on the plane: null rays of f = 1 - r_h^2/r^2 have their
     photon sphere at r = sqrt2 r_h and critical impact parameter b_c = 2 r_h, so its geometric-optics absorption
     cross-section is pi b_c^2 = 4 pi r_h^2.
  L3 (estimate; Emparan-Horowitz-Myers, abstract READ: "Most of the energy goes into the modes on the brane"; eqs. (2.10)
     and (2.18) READ in full by the C5 verifier, item 267, which reproduce the factor 4 and r_c = 2 r_h at d = 5) The hole
     radiates mainly into the plane's own fields.  As a blackbody of cross-section 4 pi r_h^2 at T = hbar c/(2 pi k
     r_h), with g* = 106.75 (all Standard Model species, T ~ 3e16 K ~ 2.8 TeV) and greybody factors between 0.1 and 1,
     the power is P = (g*/2) sigma_SB 4 (4 pi r_h^2) T^4 x greybody.  Since P ~ r_h^-2 ~ 1/E, the lifetime is E/(2P).
     For the example README at ell = 13.964 um (C2: r_h = 1.120e-20 m, E = 1.281e9 J): P = 2.1e22 W at greybody 1,
     lifetime 3.0e-14 s (3.0e-13 s at greybody 0.1).  [Verifier, item 267: "greybody factors between 0.1 and 1" is
     overstated -- the brane greybody factors computed for f = 1 - r_h^2/r^2 (the verifier's code, checked on 4D
     Schwarzschild against Page to 1.3%) are scalar 1.003, fermion 0.999, vector 0.687 of geometric optics (Harris-
     Kanti hep-ph/0309054 Table 5, READ by the verifier, agrees), 0.93 for the Standard Model's degrees of freedom
     (combined here, L5): greybody 1 is 7% conservative and 0.1 an arbitrary tenfold margin with no source.  Brane
     dominance holds more strongly than the abstract says: the 5D graviton's five helicities emit 0.61 scalar-degree
     equivalents (Cardoso-Cavaglia-Gualtieri hep-th/0512002 Table II, READ by the verifier), 0.6% of the power (L5) --
     if gravity is the only bulk field (clause (B)'s vacuum bulk).  So the life is 3.2e-14 s, 8.57e14 clocks (L5).]
  L4 (computed, exact in its scaling) The lifetime in the hole's own clock r_h/c grows as N and carries no ell -- t / (r_h
     /c) is fixed by N alone: 8.0e14 clocks for the example (0.29 N), at every ell.  [Verifier, item 267: exactly
     t/(r_h/c) = 45 N ln2/(g* gamma), gamma the greybody (computed, L5) -- fixed by N given g* and gamma; "at every ell"
     only where the example is at the small end: r_h < 0.1 ell needs ell > 1.0e-26 m, and r_h = ell at 3.2e-28 m (L5;
     C3's w < ~140.5); the sampled ells stop at 1e-20 m, inside it.]  The write at the small end
     (write_small.py S3, item 260: T >= (3/2)(5 N ln2/Z)^(1/3) - 1 clocks of r_h/c, 66,980 for the example at Z =
     106.75) grows as N^(1/3) and carries no ell either; at ell = 13.964 um it is 2.5e-24 s.  The hole outlives the
     write's floor by 1.2e10 (greybody 1), 1.2e11 (greybody 0.1); every variant of write_small S3 fits at g* = 106.75.
     [Verifier, item 264: on reading (i) only -- the hole standing at its size through the write (162-163); on reading
     (ii) (198) the lifetime bounds only the completed hole.  "8.0e14 at every ell" holds g* at 106.75 even where the
     Hawking temperature reaches 3e8 GeV (ell = 1e-20 m) -- H-SPECIES-FINITE; with g* = Z the life falls as 1/Z and
     write_small's V3 outlasts it above Z = 6.8e12 (write_small S5).]  [First written
     with the record's 4D count, 199,702 clocks of m/c (O3-WRITE), carried into the small end's clock as 7.5e-24 s and
     outlived by 4e9 -- M, item 260: "The write's clock count is still the record's 4D derivation. Redoing it at the
     small end belongs to the WRITE row."  The record's write in its own 4D clock, 1.3e-31 s, is printed for
     comparison.]

What this does not show.
  - Species beyond the Standard Model (H-SPECIES-FINITE).  [First written "the evaporation's greybody factors ...;
    bulk graviton emission (subdominant by the abstract read)" -- both now computed or READ (L3, L5; item 267): greybody
    0.93, bulk 0.6% of the power, the life 3.2e-14 s.]
  - The WRITE row's cypher at the small end (item 260 (b)).  L4 uses write_small's count, a floor: outliving it is
    necessary, not sufficient -- a write longer than the hole's life is excluded by nothing here [verifier, item 267].
  - [Verifier, item 267, the most serious: the lifetime is an evaporating hole's, formed by collapse, which has no
    second exterior; the eternal hole that carries the bridge (C1, qualification 3) sits in a bath at its temperature
    and loses no mass.  L1's bridge and L3/L4's lifetime describe different spacetimes; no number moves.]

Imports p2_gravity.py and write_small.py by path.  Stdlib + sympy.  python3 hold_small.py [--selftest | --mutants]
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
M259 = "Admitted (Recommended)"
N_EX = 2742570311524972
G_STAR = 106.75
WRITE_CLOCKS_RECORD = 199702.19                 # the record's 4D count, clocks of m/c (O3-WRITE), for comparison


def infall():
    """proper time from rest at R to r = 0 under f = 1 - r_h^2/r^2 (units c = 1): (dr/dtau)^2 = f(R) - f(r)"""
    r, R, rh = sp.symbols("r R r_h", positive=True)
    f = lambda x: 1 - rh ** 2 / x ** 2
    integrand = 1 / sp.sqrt(f(R) - f(r))
    tau = sp.simplify(sp.integrate(sp.simplify(integrand), (r, 0, R)))
    return dict(tau=tau, at_horizon=sp.simplify(tau.subs(R, rh)))


def capture():
    r, rh = sp.symbols("r r_h", positive=True)
    f = 1 - rh ** 2 / r ** 2
    if MUT.get("four_d_sphere"):
        f = 1 - rh / r
    rps = [x for x in sp.solve(sp.diff(f / r ** 2, r), r) if x.is_positive][0]
    bc = sp.simplify(rps / sp.sqrt(f.subs(r, rps)))
    return dict(rps=sp.simplify(rps), bc=bc)


def lifetime():
    spec = importlib.util.spec_from_file_location("hs_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    G, c, hbar, kB = PG.G, PG.C, PG.HBAR, 1.380649e-23
    sigma_SB = 5.670374419e-8
    L2 = math.log(2)
    spec = importlib.util.spec_from_file_location("hs_ws", os.path.join(HERE, "write_small.py"))
    WS = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(WS)
    write_clocks = WS.head_clocks()
    out = {}
    for ell in (PG.ELL_MAX, 1e-9, 1e-20):
        G5 = G * ell
        l5 = (hbar * G5 / c ** 3) ** (1 / 3)
        rh = (2 * N_EX * L2 / math.pi ** 2) ** (1 / 3) * l5
        E = 3 * math.pi * c ** 4 * rh ** 2 / (8 * G5)
        T = hbar * c / (2 * math.pi * kB * rh)
        rows = {}
        for grey in (1.0, 0.1):
            P = (G_STAR / 2) * sigma_SB * 4 * (4 * math.pi * rh ** 2) * T ** 4 * grey
            t = E / (2 * P)
            rows[grey] = dict(P=P, t=t, clocks=t / (rh / c))
        out[ell] = dict(rh=rh, E=E, T=T, rows=rows, clock=rh / c, write_s=write_clocks * rh / c)
    m = G * PG.corridor(G)["E1"] * math.sqrt(N_EX) / c ** 4
    return dict(rows=out, ell_max=PG.ELL_MAX, write_clocks=write_clocks, write_4d_s=WRITE_CLOCKS_RECORD * m / c)


GREY_SPIN = {"scalar": (4, 1.003), "fermion": (90 * 7 / 8, 0.999), "vector": (24, 0.687)}
# item 267: the C5 verifier's computed brane greybody factors relative to geometric optics (Harris-Kanti Table 5 READ by
# the verifier agrees), with the Standard Model's degrees of freedom (4 scalar, 90 Weyl x 7/8, 24 vector: g* = 106.75)
GRAV_BULK_DOF = 0.61    # item 267: the 5D graviton's five helicities in scalar-degree equivalents (CCG Table II, READ
                        # by the verifier)


def l5_checks():
    """item 267: the general infall time from the horizon, the exact clock count, the corrected life, the ell range"""
    r, rh, Et = sp.symbols("r r_h E_t", positive=True)
    tau = sp.integrate(r / sp.sqrt((Et ** 2 - 1) * r ** 2 + rh ** 2), (r, 0, rh))
    tau = sp.cancel(sp.simplify(tau.replace(sp.polar_lift, lambda z: z)))          # E~ > 0: sqrt(E~^2) = E~
    Nn, g, gam, hb, c, k, G5 = sp.symbols("N g gamma hbar c k G5", positive=True)
    sig = sp.pi ** 2 * k ** 4 / (60 * hb ** 3 * c ** 2)
    T = hb * c / (2 * sp.pi * k * rh)
    P = g / 2 * sig * 4 * (4 * sp.pi * rh ** 2) * T ** 4 * gam
    E = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * G5)
    clocks = sp.simplify((E / (2 * P) * c / rh).subs(G5, sp.pi ** 2 * rh ** 3 * c ** 3 / (2 * hb * Nn * sp.log(2))))
    dof = sum(d for d, _ in GREY_SPIN.values())
    gamma_eff = sum(d * gm for d, gm in GREY_SPIN.values()) / dof
    bulk = GRAV_BULK_DOF / (gamma_eff * dof)
    L = lifetime()
    x = L["rows"][L["ell_max"]]
    life = x["rows"][1.0]["t"] / (gamma_eff * (1 + bulk))
    spec = importlib.util.spec_from_file_location("hs_pg5", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    rho_lp = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * (PG.HBAR * PG.G / PG.C ** 3) ** (1 / 3)
    ell_at = lambda frac: (rho_lp / frac) ** 1.5                     # r_h = frac x ell
    return dict(tau=tau, clocks=clocks, dof=dof, gamma_eff=gamma_eff, bulk=bulk, life=life,
                life_clocks=life / x["clock"], over_floor=life / x["write_s"], ell_tenth=ell_at(0.1), ell_one=ell_at(1.0))


def compute():
    return dict(inf=infall(), cap=capture(), life=lifetime(), l5=l5_checks())


def report(o):
    print("hold_small.py -- O1b/O1c restated, and the hold against the temperature (item 251, small end)\n")
    print("L1 infall from rest at R to r = 0: proper time %s; from the horizon %s" % (o["inf"]["tau"], o["inf"]["at_horizon"]))
    print("L2 photon sphere r = %s, critical impact parameter %s" % (o["cap"]["rps"], o["cap"]["bc"]))
    L = o["life"]
    for ell, x in L["rows"].items():
        print("L3 ell %.3e: r_h %.3e m, E %.3e J, T %.3e K, clock %.3e s; lifetime %.2e s (grey 1) / %.2e s (grey 0.1) = "
              "%.2e / %.2e clocks; the write's %d clocks = %.2e s" % (ell, x["rh"], x["E"], x["T"], x["clock"], x["rows"][1.0]["t"],
                                                                     x["rows"][0.1]["t"], x["rows"][1.0]["clocks"],
                                                                     x["rows"][0.1]["clocks"], L["write_clocks"],
                                                                     x["write_s"]))
    print("   for comparison, the record's 4D write (%.2f clocks of m/c) in its own clock: %.2e s" % (
        WRITE_CLOCKS_RECORD, L["write_4d_s"]))
    v = o["l5"]
    print("L5 (item 267) horizon to r = 0 with specific energy E~: %s; t/(r_h/c) = %s; greybody %.3f over %.2f dof, bulk "
          "%.2f%%: life %.3g s = %.3g clocks = %.3g x the write's floor; small end r_h < 0.1 ell for ell > %.2g m, r_h = "
          "ell at %.2g m" % (v["tau"], v["clocks"], v["gamma_eff"], v["dof"], 100 * v["bulk"], v["life"], v["life_clocks"],
                             v["over_floor"], v["ell_tenth"], v["ell_one"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("L0 M's item-259 words verbatim in the rulings file", M259 in rul)
    R, rh = sp.symbols("R r_h", positive=True)
    add("L1 infall from rest at R reaches r = 0 in proper time R^2/r_h -- one clock r_h from the horizon: finite, in the "
        "interior", sp.simplify(o["inf"]["tau"] - R ** 2 / rh) == 0 and sp.simplify(o["inf"]["at_horizon"] - rh) == 0)
    add("L2 photon sphere sqrt2 r_h, critical impact parameter 2 r_h (cross-section 4 pi r_h^2)",
        sp.simplify(o["cap"]["rps"] - sp.sqrt(2) * rh) == 0 and sp.simplify(o["cap"]["bc"] - 2 * rh) == 0)
    L = o["life"]
    x = L["rows"][L["ell_max"]]
    ok = "%.1e" % x["rows"][1.0]["t"] == "3.0e-14" and "%.1e" % x["rows"][0.1]["t"] == "3.0e-13"
    clocks = [row["rows"][1.0]["clocks"] for row in L["rows"].values()]
    ok &= max(clocks) / min(clocks) - 1 < 1e-9 and "%.1e" % clocks[0] == "8.0e+14"
    ok &= "%.2g" % (x["rows"][1.0]["t"] / x["write_s"]) == "1.2e+10" and "%.1e" % x["write_s"] == "2.5e-24"
    ok &= "%.0f" % L["write_clocks"] == "66980"
    add("L3/L4 the example's lifetime 3.0e-14 s (grey 1) to 3.0e-13 s (grey 0.1); 8.0e14 clocks at every ell; the write "
        "at the small end (write_small: 66,980 clocks = 2.5e-24 s) outlived by 1.2e10", ok)
    v = o["l5"]
    rh, Et, Nn, g, gam = sp.symbols("r_h E_t N g gamma", positive=True)
    ok = sp.simplify(v["tau"] - rh / (1 + Et)) == 0 and sp.simplify(v["clocks"] - 45 * Nn * sp.log(2) / (g * gam)) == 0
    ok &= abs(v["dof"] - 106.75) < 1e-12 and "%.2f" % v["gamma_eff"] == "0.93" and "%.1f" % (100 * v["bulk"]) == "0.6"
    ok &= "%.2g" % v["life"] == "3.2e-14" and "%.3g" % v["life_clocks"] == "8.57e+14" and "%.3g" % v["over_floor"] == "1.28e+10"
    ok &= "%.2g" % v["ell_tenth"] == "1e-26" and "%.2g" % v["ell_one"] == "3.2e-28"
    add("L5 (item 267) horizon to r = 0 in r_h/(1 + E~); t/(r_h/c) = 45 N ln2/(g* gamma) exactly; greybody 0.93 and "
        "bulk 0.6% give 3.2e-14 s = 8.57e14 clocks = 1.28e10 x the floor; small end for ell > 1e-26 m", ok)
    return res


MUTANTS = {"four_d_sphere": "the capture radius from the 4D f = 1 - r_h/r"}


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
        print("  mutant %-14s %-48s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
