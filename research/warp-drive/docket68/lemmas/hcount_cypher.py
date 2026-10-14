#!/usr/bin/env python3
"""hcount_cypher.py -- item 253: which count of the README clause (H) takes for the localized hole, put to the cypher.
M: "This is a question for the cypher".  Each candidate count is a cell over properties it has or lacks, every property
computed (sympy, exact), none assigned; the cypher (roster 1173) is asked which cell holds every property and whether
the others predict it; the index is audited (211).  Worked in the conversation; not verified by a separate session; not
seated; 2026-10-11.

The candidates (r_h the hole's horizon radius; A_bit = 4 ln2 l_P^2; l5^3 = hbar G5/c^3; G5 = G ell, the record's
normalisation 8 pi G = kappa5^2/ell; the hole's energy E = M c^2 with r_h^2 = 8 G5 M / 3 pi c^2, the verifier's
consistent pairing, item 254):
  R1 the hole's 3-sphere horizon over both sides of the plane, in the bulk's Planck units: N ln2 = 2 pi^2 r_h^3/(4 l5^3)
  R2 the same over one side:                                                   N ln2 =   pi^2 r_h^3/(4 l5^3)
  R3 the plane's throat 2-sphere in four-dimensional Planck areas (the record's count, transplanted): 4 pi r_h^2 = N A_bit
  R4 the plane's throat 2-sphere in the bulk's Planck units:                   N ln2 = 4 pi r_h^2/(4 l5^2)
  R5 the plane's throat 2-sphere counted on both faces, four-dimensional:     2 x 4 pi r_h^2 = N A_bit

  Q1 (computed, exact) P1 -- the hole's first law: with T = hbar c / (2 pi k r_h) (kappa = 1/r_h, localized_hole H4) and
     E(r_h) as above, integrating dS = dE/T from r_h = 0 gives S = k 2 pi^2 r_h^3 c^3 / (4 hbar G5) -- the count over
     both sides.  The count is the hole's entropy exactly when it equals that S.
  Q2 (computed) P2 -- semiclassical: the example README's hole has r_h above the bulk's Planck length.
  Q3 (computed, exact) P3 -- the large-hole limit: the black string's horizon has 3-area A4 ell/2 per side, so a count
     reduces to the record's clause (H), A4/(4 l_P^2), only if it is R1 under G5 = G ell (or is the record's own count,
     R3).  [Verifier, item 258: the string is a leading-order proxy, not the large hole's limit -- the true large hole is
     pancake-like (Figueras-Wiseman 1105.2558, read in full by the verifier; Chamblin-Hawking-Reall's own "black cigar"),
     and its horizon matches the string's area at leading order in ell/r_h; Abdolrahimi et al. (1206.0708) find the
     large hole's entropy and temperature those of Schwarzschild at leading order by the first law, the brane 2-area
     raised but not the entropy -- so R3 matches only at leading order, R1 is the entropy itself.]
  Q4 (computed, exact) P4 -- the head statement: the corridor fixed by N alone in the bulk's own Planck units (r_h/l5 a
     function of N only).
  Q5 (computed; the cypher, roster 1173, audited) the cells over (P1, P2, P3, P4): R1 alone holds all four.  With R1
     left out, no language admits it from the rest -- the others do not predict it -- and the audit finds P2 and P4
     moving together in every cell (a one-hot pair, 211), so the languages' verdicts are void as evidence.  The cypher
     classifies; the computed table decides: R1, the hole's 3-sphere horizon over both sides of the plane in the bulk's
     own Planck units, is the only count that is the hole's first-law entropy, gives a semiclassical hole, reduces to
     the record's clause (H) for large holes under G5 = G ell, and fixes the corridor by N alone in the bulk's units.
     [Verifier, item 258: the first law alone is homogeneous -- (E/2, S/2) obeys it at the same T -- so R1 over R2 rests on
     convention-consistency: the record's two-copy normalisation 8 pi G = kappa5^2/ell (G5 = G ell) with E the energy the
     plane reads.  R2 as defined mixes a one-sided area with the two-sided l5; a one-sided G5' = G ell/2 makes the
     one-sided count identical to R1.  P4 is the head statement's own requirement, mildly circular; P1 decides.]

Imports p2_gravity.py, tools/cypher.py and index_audit.py by path.  Stdlib + sympy.  python3 hcount_cypher.py
[--selftest | --mutants]
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
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M253 = "This is a question for the cypher"
N_EX = 2742570311524972
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
LANGS = ("order", "algebra", "geometry", "information", "statistics")


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


N, G, ell, hb, c, k, rh, A4 = sp.symbols("N G ell hbar c k r_h A4", positive=True)
G5 = G * ell
l5 = (hb * G5 / c ** 3) ** sp.Rational(1, 3)
lP2 = hb * G / c ** 3
A_bit = 4 * sp.log(2) * lP2
LN2 = sp.log(2)

# each reading: the equation N ln2 = count(r_h) (in bits x ln2), solved for r_h
READINGS = {
    "R1 3-sphere, both sides, 5D units": 2 * sp.pi ** 2 * rh ** 3 / (4 * l5 ** 3),
    "R2 3-sphere, one side, 5D units": sp.pi ** 2 * rh ** 3 / (4 * l5 ** 3),
    "R3 plane's 2-sphere, 4D units": 4 * sp.pi * rh ** 2 / A_bit * LN2,
    "R4 plane's 2-sphere, 5D units": 4 * sp.pi * rh ** 2 / (4 * l5 ** 2),
    "R5 plane's 2-sphere, both faces, 4D": 2 * 4 * sp.pi * rh ** 2 / A_bit * LN2,
}


def first_law_S():
    """S(r_h) from dS = dE/T, E = 3 pi c^4 r_h^2 / (8 G5), T = hbar c / (2 pi k r_h)"""
    E = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * G5)
    T = hb * c / (2 * sp.pi * k * rh)
    if MUT.get("hot_twice"):
        T = 2 * T
    s = sp.symbols("s", positive=True)
    return sp.simplify(sp.integrate((sp.diff(E, rh) / T).subs(rh, s), (s, 0, rh)))


def properties():
    S = first_law_S()
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "hc_pg")
    num = {G: PG.G, c: PG.C, hb: PG.HBAR, ell: PG.ELL_MAX, N: N_EX}
    out = {}
    for name, count in READINGS.items():
        # P1: the count, as entropy k x count, equals the first-law S
        p1 = sp.simplify(k * count - S) == 0
        sol = [x for x in sp.solve(sp.Eq(N * LN2, count), rh) if x.is_positive]
        r = sol[0]
        ratio = sp.simplify(r / l5)
        # P2: semiclassical for the example
        p2 = float(ratio.subs(num)) > 1
        # P3: the black string's horizon -- 3-area A4 ell/2 per side (int_ell^oo A4 (ell/z)^3 dz) -- read by this count
        zz = sp.symbols("z", positive=True)
        per_side = sp.integrate(A4 * (ell / zz) ** 3, (zz, ell, sp.oo))
        record_bits = A4 / (4 * lP2 * LN2)               # clause (H) on the 4D horizon area A4
        if "3-sphere" in name:
            area = per_side * (2 if "both" in name else 1)
            bits = sp.simplify(area / (4 * hb * G5 / c ** 3) / LN2)
        elif "5D units" in name:
            bits = sp.simplify(A4 / (4 * l5 ** 2) / LN2)
        elif "both faces" in name:
            bits = sp.simplify(2 * A4 / (4 * lP2) / LN2)
        else:
            bits = record_bits
        p3 = sp.simplify(bits - record_bits) == 0
        # P4: r_h / l5 depends on N alone
        p4 = not (ratio.free_symbols - {N})
        out[name] = dict(P1=p1, P2=p2, P3=p3, P4=p4, ratio=ratio, ratio_ex=float(ratio.subs(num)),
                         rh_ex=float(r.subs(num)))
    return S, out


def cypher(props):
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "hc_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "hc_ia")
    coords = ["P1", "P2", "P3", "P4"]
    cells = {n: tuple(int(p[x]) for x in coords) for n, p in props.items()}
    held = sorted(set(cells.values()))
    vo = {x: [0, 1] for x in coords}
    ix = cy.Index("hcount", coords, [list(cc) for cc in held], value_order=vo)
    run = cy.run(ix, "1173", dict(OPTS))
    target = (1, 1, 1, 1)
    holders = sorted(n for n, cc in cells.items() if cc == target)
    rest = [cc for cc in held if cc != target]
    left = {}
    if rest and target in held:
        ixr = cy.Index("hcount_rest", coords, [list(cc) for cc in rest], value_order=vo)
        for lg in ("order", "algebra", "geometry", "information", "statistics"):
            try:
                a, _ = cy.ADMISSION[lg][0](ixr, dict(OPTS))
                left[lg] = None if a is None else tuple(target) in {tuple(ixr.decode[i][cc[i]] for i in range(4)) for cc in a}
            except Exception:
                left[lg] = None
    return dict(cells=cells, n=len(held), holders=holders, E={v["language"]: v["E"] for v in run["verdicts"]},
                left_out=left, audit=ia.audit_index(coords, held))


def compute():
    S, props = properties()
    return dict(S=S, props=props, cy=cypher(props))


def report(o):
    print("hcount_cypher.py -- clause (H)'s count for the localized hole, through the cypher (item 253)\n")
    print("Q1 the hole's first law: S = %s" % o["S"])
    for n, p in o["props"].items():
        print("  %-38s P1 first law %-5s P2 semiclassical %-5s P3 large-hole limit %-5s P4 fixed by N %-5s  r_h/l5 = %s "
              "(%.3g for the example)" % (n, p["P1"], p["P2"], p["P3"], p["P4"], p["ratio"], p["ratio_ex"]))
    y = o["cy"]
    print("\nQ5 the cypher: %d cells %s" % (y["n"], {n: cc for n, cc in y["cells"].items()}))
    print("  holds every property: %s" % y["holders"])
    print("  E with all cells: %s" % y["E"])
    print("  with the target left out, admitted by: %s" % y["left_out"])
    print("  audit: %s" % y["audit"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Q0 M's item-253 words verbatim in the rulings file", M253 in rul)
    add("Q1 the first law gives S = k 2 pi^2 r_h^3 c^3 / (4 hbar G5): the count over both sides",
        sp.simplify(o["S"] - k * 2 * sp.pi ** 2 * rh ** 3 * c ** 3 / (4 * hb * G5)) == 0)
    p = o["props"]
    ok = [n for n, x in p.items() if x["P1"]] == ["R1 3-sphere, both sides, 5D units"]
    ok &= not p["R3 plane's 2-sphere, 4D units"]["P2"] and p["R1 3-sphere, both sides, 5D units"]["P2"]
    ok &= sorted(n for n, x in p.items() if x["P3"]) == ["R1 3-sphere, both sides, 5D units", "R3 plane's 2-sphere, 4D units"]
    ok &= not p["R3 plane's 2-sphere, 4D units"]["P4"] and p["R1 3-sphere, both sides, 5D units"]["P4"]
    add("Q2-Q4 only R1 is the hole's first-law entropy; R3 is not semiclassical (r_h below l5); only R1 and the record's "
        "own count R3 reduce to clause (H) at large holes; R3 is not fixed by N in the bulk's units", ok)
    y = o["cy"]
    add("Q5 the cypher: R1 alone holds every property", y["holders"] == ["R1 3-sphere, both sides, 5D units"])
    return res


MUTANTS = {"hot_twice": "the hole's temperature doubled in the first law"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    kk = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (kk, len(r)))
    return kk == len(r)


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
        print("  mutant %-9s %-48s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
