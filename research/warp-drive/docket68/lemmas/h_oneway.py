#!/usr/bin/env python3
"""h_oneway.py -- item 276: "The passage is one-way in all aspects".  The proof 139 (2) orders, re-worked on the
one-way coincidence of items 275 and 276: our sheet's junction carries our stress alone; position 2's carries ours,
received, and its own.  Worked in the conversation (computed with sympy, exact where marked; READ where marked;
standard values marked; deduced where marked; the cypher run and audited; not verified by a separate session; not
seated); 2026-10-12.

[M, item 277: "You are forgetting that the passage is one-way only".  H6 populated two-way rows, half its index, after 276; repopulated one-way only in i_oneway.py I6.
H3's "exactly when S2 > 0" overstates: with S2 = 0 and a bulk mass C2 > 0 the expansion is unbounded too (i_oneway
I6).  Kept as written.]

  H0 (read) M's item-276 words, verbatim in the rulings file.
  H1 (deduced; the board's reading of 276) Every influence runs from ours to position 2 and none back -- energy, null
     rays, gravity and the junction.  At the coincidence (275) our sheet's junction carries our stress S1 alone;
     position 2's carries S1, received, and its own S2 = -sigma/4 + rho_m (139 (1), 268).  g_coincide's G2 and G3
     charged position 2's matter to our gamma and our expansion rate: reverse aspects (item 276's recorded error).
  H2 (computed, exact) The two sheets' expansions, each from its own junction with decaying sides of the bulk's k
     (e_positive E2): ours, H1^2/c^2 = (kappa^2 S1/6)^2 - k^2 + C1/a^4, is 0 at S1 = sigma = 6k/kappa^2 with C1 = 0
     whatever S2 is -- position 2 does not reach our expansion.  Position 2's, H2^2/c^2 = (kappa^2 (S1 + S2)/6)^2 - k^2
     + C2/a^4 = (kappa^4/36) S2 (2 sigma + S2) + C2/a^4.  At linear order (kappa^4 sigma/18) c^2 = 8 pi G/3 (exact, with
     kappa5^2 = 8 pi G ell/c^4 and sigma = 3 c^4/(4 pi G ell^2)): position 2's S2 gravitates with our Newton constant,
     as ordinary positive energy.
  H3 (computed, exact) Position 2's universe expands without bound exactly when S2 > 0 (S2 > -2 sigma).  Its late-time
     H2^2, after C2/a^4 has redshifted, has the sign of S2 (2 sigma + S2); with S2 < 0 a bulk mass C2 > 0 lets it expand
     only to a_max^4 = 36 C2/(kappa^4 |S2| (2 sigma + S2)), and then it falls back.  The matter-free -sigma/4 gives
     H2^2/c^2 = -(7/16)(kappa^2 sigma/6)^2 + C2/a^4: an anti-de Sitter universe.  Absorbing the README raises H2^2,
     dH2^2/dS2 = (kappa^4/18)(sigma + S2) c^2 > 0 for S2 > -sigma.
  H4 (deduced; the board's reading of 139 (3)) "Absorbing of the README into position 2 is an expansion of that
     universe" is read as: position 2's universe expands, and without bound.  By H3, S2 > 0: position 2's matter is
     rho_m = sigma/4 + S2 > sigma/4 at every point of its sheet where it is a Friedmann universe -- 139 (2) in 268's
     sense, position 2's sheet alone, everywhere -- with nothing charged to ours (H2).  184 follows: a matter-free
     position 2 is anti-de Sitter, not expanding.
  H5 (computed; standard H0) The excess is position 2's own cosmological content.  For position 2 to expand at our
     rate H0 (67.4 km/s/Mpc, Planck 2018, standard, not READ here), S2 = 3 H0^2 c^2/(8 pi G) = 7.7e-10 J/m^3 -- our
     critical density -- 5.2e-63 of sigma above sigma/4 = 3.7e52 J/m^3.
  H6 (computed; the cypher, roster 1173, audited) The index: influence (two-way, one-way) x rho_m (0, sigma/8, sigma/2)
     x position 2's bulk mass C2 (0, > 0) -- 12 rows, each with ours_kept (our expansion untouched by position 2),
     expands_now (H2^2 > 0 somewhere, a bulk mass allowing it for a while) and p2_expands (without bound).
     p2_expands equals S2 > 0 in every row (H3) -- kept out of the index, where the two identical columns read as a
     one-hot code (211); the first run carried both and its audit voided it.  The all-three cell is reached only
     one-way with position 2's matter above sigma/4, whatever C2; the five languages agree at E = 0 (10 of 10 pairs).
  H7 (recorded; READ via multiplane.py) Under 276 our plane's gamma comes from our sheet alone: one Randall-Sundrum II
     plane, gamma = 1 (Maartens-Koyama eq. 155, READ in multiplane.py).  multiplane M4's gamma = 5/4 on our plane, from
     which 139 (1)'s quarter was read, rests on position 2's plane acting on our propagator -- a two-way reading; the
     ruling's value stands as M's (item 276 (c)).  Recorded, not repaired.

  H8 (deduced) C8 under 276: m1p2x_oneway's one junction lies on position 2's white-hole face and none on ours (O5's
     d_ours, the object's interior at our tension), so every stress it carries is on position 2's side, as 276 has
     it; its z_net (every crossing ray's share >= 0) holds through position 2's own matter, m2 = 1, which H4 now
     proves rather than assumes (268).

What this does not show.
  - That 276 means our junction carries our stress alone (H1 is the board's reading); a one-way junction is not
    Israel's, which is symmetric -- it is M's theory, computed under, not derived.
  - 139 (3) read as momentary: with a bulk mass C2 > 0 a negative S2 expands for a while (to H3's a_max) and then
    falls back; H4 needs the expansion to be without bound.
  - m1p2x_oneway's junction law itself re-derived under 276 (H8 reads where it lies, not its law).
  - Where position 2 is not a Friedmann universe (near the corridor, the README's 2.0e-15 m; e_positive E7).

Imports p2_gravity.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 h_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
M276 = "The passage is one-way in all aspects"
PROPS = ["ours_kept", "expands_now", "p2_expands"]
FIVE = ["order", "algebra", "geometry", "information", "statistics"]
H0 = 67.4e3 / 3.0857e22                                   # Planck 2018, standard, not READ here


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def sheets(one_way=True):
    """H2: each sheet's H^2/c^2 from its own junction (like decaying sides, the bulk's k)"""
    kap2, sig, S2, C1, C2, a = sp.symbols("kappa5sq sigma S_2 C_1 C_2 a", real=True)
    k = kap2 * sig / 6                                     # sigma = 6 k/kappa^2, ours at the critical value
    S1 = sig
    ours_load = S1 if one_way else S1 + S2
    if MUT.get("reverse"):
        ours_load = S1 + S2                                # the mutant lets position 2 reach our junction
    H1 = sp.expand((kap2 * ours_load / 6) ** 2 - k ** 2) + C1 / a ** 4
    H2 = sp.expand((kap2 * (S1 + S2) / 6) ** 2 - k ** 2) + C2 / a ** 4
    return dict(H1=H1, H2=H2, kap2=kap2, sig=sig, S2=S2, C1=C1, C2=C2, a=a)


def h2_facts(s):
    kap2, sig, S2, C2, a = s["kap2"], s["sig"], s["S2"], s["C2"], s["a"]
    form = sp.simplify(s["H2"] - (kap2 ** 2 / 36 * S2 * (2 * sig + S2) + C2 / a ** 4)) == 0
    ours_free = sp.simplify(s["H1"] - s["C1"] / a ** 4) == 0
    late = sp.limit(s["H2"], a, sp.oo)                     # C2/a^4 redshifted
    amax4 = sp.solve(sp.Eq(s["H2"], 0), a ** 4)
    free = sp.simplify(s["H2"].subs({S2: -sig / 4, C2: 0}) + sp.Rational(7, 16) * (kap2 * sig / 6) ** 2)
    dH = sp.simplify(sp.diff(s["H2"], S2) - kap2 ** 2 / 18 * (sig + S2))
    G, ell, c = sp.symbols("G ell c", positive=True)
    lin = sp.simplify((kap2 ** 2 * sig / 18).subs({kap2: 8 * sp.pi * G * ell / c ** 4,
                                                   sig: 3 * c ** 4 / (4 * sp.pi * G * ell ** 2)}) * c ** 2
                      - 8 * sp.pi * G / (3 * c ** 2))
    return dict(form=form, ours_free=ours_free, late=sp.factor(late), amax4=amax4, free=free == 0, dH=dH == 0,
                lin=lin == 0)


def late_sign(S2v, sigv=1, kap2v=1):
    """the sign of position 2's late-time H^2"""
    return sp.sign(sp.Rational(kap2v ** 2, 36) * S2v * (2 * sigv + S2v))


def numbers():
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "ho_pg")
    sigma = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    S2 = 3 * H0 ** 2 * PG.C ** 2 / (8 * math.pi * PG.G)
    return dict(sigma=sigma, quarter=sigma / 4, S2=S2, frac=S2 / sigma)


def populate():
    rows = {}
    for way, rho, C2 in itertools.product(("two", "one"), (sp.Integer(0), sp.Rational(1, 8), sp.Rational(1, 2)), (0, 1)):
        S2 = -sp.Rational(1, 4) + rho                      # in units of sigma
        s = sheets(one_way=(way == "one"))
        H1 = s["H1"].subs({s["kap2"]: 1, s["sig"]: 1, s["S2"]: S2, s["C1"]: 0})
        ours_kept = int(sp.simplify(H1) == 0)              # our expansion untouched (flat at the critical value)
        expands = int(bool(late_sign(S2) > 0))
        if MUT.get("bounded_counts") and C2:
            expands = 1                                    # the mutant counts a bounded, recollapsing expansion
        now = int(bool(expands or C2 > 0))                 # a bulk mass lets it expand for a while (H3's a_max)
        rows[(way, str(rho), C2)] = dict(ours_kept=ours_kept, expands_now=now, p2_expands=expands,
                                         p2_positive=int(bool(S2 > 0)))
    return rows


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "ho_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "ho_ia")
    ix = cy.Index("h_oneway", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    return dict(held=held, reached=(1, 1, 1) in held, E={v["language"]: v["E"] for v in run["verdicts"]},
                langclose=run["langclose_holds"], agreeing=run["pairs_agreeing"], audit=ia.audit_index(PROPS, held),
                holders=sorted(c for c, p in rows.items() if tuple(p[x] for x in PROPS) == (1, 1, 1)))


def gamma_ours():
    MP = _load(os.path.join(D68, "bulk", "multiplane.py"), "ho_mp")
    return dict(rs2=MP.gamma_from_c0(sp.Integer(-1)), m4=MP.m4()["gamma"])     # exact: Einstein, c0 = -1


def compute():
    s = sheets()
    rows = populate()
    return dict(s=s, f=h2_facts(s), n=numbers(), rows=rows, cy=cypher(rows), g=gamma_ours())


def report(o):
    print("h_oneway.py -- 139 (2) on the one-way coincidence (items 275, 276)\n")
    f = o["f"]
    print("H2 ours H1^2/c^2 = %s; position 2's H2^2/c^2 = %s" % (o["s"]["H1"], o["s"]["H2"]))
    print("   position 2's form (kappa^4/36) S2 (2 sigma + S2) + C2/a^4: %s; ours free of S2: %s; (kappa^4 sigma/18) c^2 "
          "= 8 pi G/3: %s" % (f["form"], f["ours_free"], f["lin"]))
    print("H3 late-time H2^2/c^2 = %s; a_max^4 = %s; matter-free -sigma/4 is -(7/16)(kappa^2 sigma/6)^2: %s; dH2^2/dS2 = "
          "(kappa^4/18)(sigma + S2): %s" % (f["late"], f["amax4"], f["free"], f["dH"]))
    n = o["n"]
    print("H5 position 2 at our H0: S2 = %.3g J/m^3 = %.3g sigma (sigma/4 = %.3g J/m^3)" % (n["S2"], n["frac"],
                                                                                          n["quarter"]))
    cy = o["cy"]
    print("H6 %d rows; held (ours_kept, expands_now, p2_expands): %s; all three by %s" % (len(o["rows"]), cy["held"],
                                                                                         cy["holders"]))
    print("   E %s; langclose %s, %d of 10 pairs agreeing; audit keys %s one-hot %s" % (
        cy["E"], cy["langclose"], cy["agreeing"], cy["audit"]["keys"], cy["audit"]["onehot"]))
    print("H7 our gamma from our sheet alone (Randall-Sundrum II): %s; multiplane M4's two-way reading: %s" % (
        o["g"]["rs2"], o["g"]["m4"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("H0 M's item-276 words verbatim in the rulings file", M276 in rul)
    f = o["f"]
    add("H2 ours flat at S1 = sigma whatever S2; position 2's H2^2/c^2 = (kappa^4/36) S2 (2 sigma + S2) + C2/a^4; "
        "(kappa^4 sigma/18) c^2 = 8 pi G/3", f["form"] and f["ours_free"] and f["lin"])
    s = o["s"]
    late_ok = sp.simplify(f["late"] - s["kap2"] ** 2 / 36 * s["S2"] * (2 * s["sig"] + s["S2"])) == 0
    ok = late_ok and f["free"] and f["dH"] and len(f["amax4"]) == 1
    ok &= all(late_sign(v) > 0 for v in (sp.Rational(1, 100), 1, 5)) and all(
        late_sign(v) < 0 for v in (-sp.Rational(1, 4), -sp.Rational(1, 100), -1))
    add("H3 late-time H2^2 has the sign of S2 (2 sigma + S2); a bulk mass only bounds a negative S2's expansion; "
        "matter-free -sigma/4 is anti-de Sitter; absorbing raises H2^2", ok)
    n = o["n"]
    ok = "%.2g" % n["S2"] == "7.7e-10" and "%.2g" % n["frac"] == "5.2e-63" and "%.2g" % n["quarter"] == "3.7e+52"
    add("H5 position 2 at our H0 needs S2 = 7.7e-10 J/m^3 (our critical density) = 5.2e-63 sigma", ok)
    cy, rows = o["cy"], o["rows"]
    ok = cy["reached"] and len(rows) == 12 and all(p["p2_expands"] == p["p2_positive"] for p in rows.values())
    ok &= cy["holders"] == sorted([("one", "1/2", 0), ("one", "1/2", 1)])
    ok &= not cy["audit"]["keys"] and not cy["audit"]["onehot"] and cy["langclose"]
    ok &= (0, 0, 1) not in cy["held"] and (1, 0, 1) not in cy["held"] and [cy["E"][L] for L in FIVE] == [0] * 5
    add("H6 p2_expands equals p2_positive in every row (kept out of the index, H3); the all-three cell only one-way "
        "with matter above sigma/4, whatever C2; unbounded expansion never without expansion now; audit clean", ok)
    add("H7 our gamma from our sheet alone is 1 (Randall-Sundrum II); multiplane M4's 5/4 is the two-way reading",
        o["g"]["rs2"] == 1 and o["g"]["m4"] == sp.Rational(5, 4))
    return res


MUTANTS = {"reverse": "position 2 let reach our junction",
           "bounded_counts": "a bounded, recollapsing expansion counted as expanding"}


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
        print("  mutant %-15s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
