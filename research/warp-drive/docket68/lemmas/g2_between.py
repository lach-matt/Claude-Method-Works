#!/usr/bin/env python3
"""g2_between.py -- position 2's G between universes, and what it makes of 203's single E (m1p2_cypher X3).  Pass 2
of the cycle (items 204-206); put to the cypher (computed, deduced, READ; not verified by a separate session; not
seated; 2026-10-10).

m1p2_cypher.py X3 left a tension: the other leg of the SAME eq. (17) needs position 2's G equal to ours, while
COUNT-CYPHER.md's per-sheet law gives G2 = 2 G1, so m2 = 2m (or E/sqrt2 for N bits) against 203's single E.

  G1 (computed; READ) Shiromizu-Maeda-Sasaki's local law on one plane, G = kappa5^4 lambda / (48 pi) (SMS (19), READ
     in b1_matter.py, with "Furthermore, we would have the wrong sign of G_N if lambda < 0"): at 139 (1)'s lambda2 =
     -sigma/4 it gives G2 = -G/4.  That is the one-plane law; with both planes counted it is superseded (G2)
  G2 (READ from COUNT-CYPHER.md's table; computed there by an unbanked scratch instrument under H-ONE-G5) the per-sheet
     count -- the count 200 (1) ("position 2's plane counts once") makes the chain's (B6: k_R = k_L/2) -- gives
     G2/G1 = +2; the doubled count, set aside by 200 (1), gave +6
  G3 (computed, from axioms.py's G1 law) with E fixed by N and G, E^2 = N h c^5 ln2 / (8 pi^2 G), and 203's E read the
     same from both sides: position 2 reads m2/m = G2/G, its horizon radius 2 m2, and -- its own Planck area being
     A_bit2 = (G2/G) A_bit -- a capacity N2/N = G2/G.  Per-sheet: m2 = 2m, capacity 2N.  The local law (G2 < 0) gives
     no horizon at all: the README could not be held at position 2
  G4 (the board's decision under 149: H-HOLD-AT-P2-NOT-SATURATED) 106 (b) and 132 say position 2's horizon HOLDS the
     README ("the bits are then held only at the horizon of position 2"; "do the horizons still hold the README too ...
     - yes"), not that it holds exactly N bits; (H)'s "exactly" is the throat's (4 pi r0^2 = N A_bit at position 1).
     So between universes 200 (1), 203 and 106/132 all stand together: one E, position 2's own G twice ours, its
     horizon holding the N-bit README in a capacity of 2N.  What does NOT stand is X3's "the other leg of the SAME eq.
     (17)": position 2 reads its own eq. (17), at m2 = 2m.  M1P2 between universes is to be worded that way
  G5 (cypher) the readings as cells -- (G2 > 0, G2/G, E the same both sides, holds the README, holds exactly N, fits
     200 (1)) -- target: positive G, one E, held, fitting 200 (1).  The per-sheet reading is data: all five admit it.
     With 'exactly N' added to the target statistics and geometry refuse under every coding -- no reading gives one E,
     exactly N bits and 200 (1) together; order, algebra and information admit it under some codings only, by joining
     two readings (an artefact).  Control: the per-sheet reading removed -- statistics refuses the target
Proposal, for seating after this pass (206): M1P2x re-worded "position 2's side reads its own eq. (17), at m2 = (G2/G) m
(= 2m on the per-sheet count, 200 (1)), its horizon holding the README in a capacity (G2/G) N" -- still OPEN on the
mouth reading with (Z) on both planes (m1x_cypher).  No row turns green on it alone.
Imports tools/cypher.py by path.  Stdlib + sympy.  python3 g2_between.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
MUT = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _norm(t):
    return re.sub(r"\s+", " ", t)


def sources():
    b1 = open(os.path.join(HERE, "b1_matter.py")).read()
    cc = open(os.path.join(HERE, "COUNT-CYPHER.md")).read()
    ru = _norm(open(os.path.join(D68, "M-RULINGS-2026-10-03.md")).read())
    per = re.search(r"\*\*per-sheet count\*\* \(H-COUNT-PER-SHEET\) \| k_L/2 \| −1/4 \| — \| \+(\d+) \|", cc)
    dbl = re.search(r"\*\*doubled count\*\* \(H-COUNT-DOUBLED\) \| 3k_L/4 \| −1/8 \| −1/4 \(PRZ τ2/τ1\) \| \+(\d+) \|", cc)
    return {"sms_quote": "we would have the wrong sign of G_N if lambda < 0" in b1,
            "per_sheet": int(per.group(1)) if per else None, "doubled": int(dbl.group(1)) if dbl else None,
            "w106": "the bits are then held only at the horizon of position 2" in ru,
            "w132": "do the horizons still hold the README too" in ru, "w200": "counts once" in ru}


# ---------------------------------------------------------------------------------------------------------- G1, G3
def laws():
    k5, sig, N, h, c, G, ln2 = sp.symbols("kappa5 sigma N h c G ln2", positive=True)
    Gp = lambda lam: k5**4 * lam / (48 * sp.pi)                     # SMS (19)
    g_local = sp.simplify(Gp(-sig / 4) / Gp(sig))
    E2 = lambda Gx: N * h * c**5 * ln2 / (8 * sp.pi**2 * Gx)        # axioms.py G1, squared
    r = sp.Symbol("r", positive=True)                                # G2/G

    def read(ratio):
        G2 = ratio * G
        E_same = E2(G)                                               # 203: one E
        m2_over_m = sp.simplify(ratio)                               # m = G E / c^4
        A_bit = lambda Gx: 2 * h * Gx * ln2 / (sp.pi * c**3)
        area2 = 4 * sp.pi * (2 * G2 * sp.sqrt(E_same) / c**4) ** 2
        cap = sp.simplify(area2 / A_bit(G2) / N) if not MUT.get("own_abit_off") else sp.simplify(area2 / A_bit(G) / N)
        horizon = bool(sp.simplify(ratio) > 0)
        return {"m2": m2_over_m, "cap": cap if horizon else None, "horizon": horizon}
    return {"local": g_local, "per": read(2 if not MUT.get("per_one") else 1), "local_read": read(g_local),
            "equal": read(1)}


# ---------------------------------------------------------------------------------------------------------- G5
CO = ["reading", "g_pos", "g_ratio", "e_same", "holds", "exactly", "fits_200"]


def cells(s, L):
    per = L["per"]
    out = [
        (0, 0, 0, 1, 0, 0, 0),                                       # one-plane local law: G2 = -G/4, no horizon (G1, G3)
        (1, 1, 2, 1, 1 if per["cap"] is not None and per["cap"] >= 1 else 0,
         1 if per["cap"] == 1 else 0, 1),                            # per-sheet count: 2, one E, capacity 2N (G2, G3)
        (2, 1, 6, 1, 1, 0, 0),                                       # doubled count: set aside by 200 (1)
        (3, 1, 1, 1, 1, 1, 0),                                       # equal G: needs H-ONE-G5 withdrawn, not 200 (1)'s count
    ]
    if MUT.get("seat_exact"):
        out.append((4, 1, 2, 1, 1, 1, 1))
    return out


def cypher(cs):
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "g2_cypher")
    target = lambda h: h[1] == 1 and h[3] == 1 and h[4] == 1 and h[6] == 1
    exact = lambda h: target(h) and h[5] == 1

    def adm(cl, test, lang, k=2, order=None):
        cl = sorted(set(cl))
        vo = {n: sorted({x[i] for x in cl}) for i, n in enumerate(CO)}
        if order:
            vo["reading"] = [x for x in order if x in vo["reading"]]
        ix = cy.Index("g2", CO, [list(x) for x in cl], value_order=vo)
        out, _ = cy.ADMISSION[lang][0](ix, {"statistics_order": k} if lang == "statistics" else {})
        if out is None:
            return None
        dec = {tuple(ix.decode[i][x[i]] for i in range(len(CO))) for x in out}
        return sorted(h for h in dec if test(h))
    langs = ("order", "algebra", "geometry", "information", "statistics")
    orders = [list(p) for p in itertools.permutations(sorted({x[0] for x in cs}))]
    held = {l: all(any(h[0] == 1 for h in (adm(cs, target, l, 2, o) or [])) for o in orders) for l in langs}
    ex = {l: sum(1 for o in orders if not adm(cs, exact, l, 2, o)) for l in langs}
    ex["n"] = len(orders)
    ctrl = adm([x for x in cs if x[0] != 1], target, "statistics", 2)
    return {"held": held, "exact_refused": ex, "ctrl": ctrl}


def compute():
    s, L = sources(), laws()
    cs = cells(s, L)
    return {"src": s, "laws": L, "cells": cs, "cy": cypher(cs)}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    s, L = d["src"], d["laws"]
    add("G1 SMS's local law at lambda2 = -sigma/4 gives G2 = -G/4, and SMS's own words flag the wrong sign (READ, banked)",
        s["sms_quote"] and sp.simplify(L["local"] + sp.Rational(1, 4)) == 0)
    add("G2 COUNT-CYPHER's table: per-sheet count G2/G1 = +2 (200 (1)'s count), doubled +6", s["per_sheet"] == 2
        and s["doubled"] == 6 and s["w200"])
    p = L["per"]
    add("G3 with one E (203), the per-sheet reading gives m2 = 2m and a capacity of 2N with position 2's own Planck area; "
        "the local law gives no horizon", p["m2"] == 2 and p["cap"] == 2 and not L["local_read"]["horizon"]
        and L["equal"]["cap"] == 1)
    add("G4 106 (b) and 132 say 'held', verbatim: the board reads position 2's horizon as holding the README, not "
        "saturated by it", s["w106"] and s["w132"])
    cy = d["cy"]
    add("G5 cypher: the per-sheet reading (positive G, one E, held, fits 200 (1)) is admitted by all five under every "
        "coding of the reading axis", all(cy["held"].values()))
    e = cy["exact_refused"]
    add("G5 with 'exactly N' in the target statistics and geometry refuse under every coding; order, algebra and "
        "information admit it under some codings only -- joining the per-sheet cell's fit with equal G's exactness, an "
        "artefact of ordering the nominal reading axis", e["statistics"] == e["n"] and e["geometry"] == e["n"]
        and all(e[l] < e["n"] for l in ("order", "algebra", "information")))
    add("G5 control: the per-sheet reading removed -- statistics refuses the target", cy["ctrl"] == [])
    return res


MUTANTS = {"per_one": "the per-sheet count read as G2 = G", "own_abit_off": "position 2's capacity measured in our Planck area",
           "seat_exact": "a reading with one E, exactly N and 200 (1) seated as data"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-58s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("g2_between.py -- position 2's G between universes\n")
    print("sources", d["src"])
    print("laws", d["laws"])
    print("cells", d["cells"])
    print("cypher", d["cy"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
