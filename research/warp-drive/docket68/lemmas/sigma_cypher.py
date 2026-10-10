#!/usr/bin/env python3
"""sigma_cypher.py -- "what sets the tension of our universe's plane?" put to the cypher (items 196, 200 (3); M: "This
is the perfect question to ask the cypher").  Computed and deduced; the cypher CLASSIFIES, it derives nothing; not
verified by a separate session; not seated; 2026-10-10.

The plane is ours (P1).  Its tension sigma sets k: clause (B) sigma = 6 k_L/kappa5^2, with measured G
ell^2 = 3c^4/(4 pi G sigma) (b6p_scale.py B6''a0, SMS (19) READ); 139 (1) and 200 (1) then fix position 2's plane at
-sigma/4 and its bulk at k_R = k_L/2.

  W1 (computed) the window: sigma >= 1.48e53 J/m^3 (table-top, ell <= 13.964 um, B6P-SCALE) and sigma <= 2.75e112 J/m^3
     (ITEM197's positivity on P2 at the quarter tension, ell > 8.5415 m, for a 1-bit README): energy scales
     sigma^(1/4) from 9.18e3 GeV to 6.03e18 GeV
  C1 (computed; cypher) the index of what the theory fixes -- measured G and Lambda4, the README N, its energy E(N) --
     with sigma: information reports sigma as an axis (removing it merges cells) while E adds nothing (fixed by N).
     Logic's binary "is sigma fixed by what the theory fixes?": NO in every operator-bearing language, forced by the
     data (sigma varies at fixed (G, Lambda4, N)).  Control: a world-set in which sigma is a function of N flips it
  C2 (computed; cypher) the candidate setters, one at a time, each added as a known coordinate:
       a measured ell (or kappa5)       closes sigma (sigma = 3c^4/(4 pi G ell^2))
       Lambda5 with the detuning (SMS 18) closes sigma only if Lambda5 is known -- it moves the unknown, it does not fix it
       a README equality ell = c m(N)   closes sigma as a function of N -- refuted for one plane (C3)
       a particle or Planck scale       closes sigma; the window decides which are allowed (W2)
  C3 (deduced, STRUCTURAL) one plane, one tension: corridors with different N run in one universe, so a sigma set by N
     would give our one plane two tensions.  A README equality can set a corridor-local k (186), not our plane's sigma
  W2 (computed) which scales the window allows: Higgs (246 GeV) and TeV fall below it (ell ~ cm, mm: excluded by
     table-top); the Planck scale (1.22e19 GeV) falls above it (ell = 7.9e-36 m < 8.54 m(1)); an intermediate scale
     (1e11 GeV), the GUT scale (1e16 GeV) and the reduced Planck scale (2.4e18 GeV) lie inside
So the cypher's answer: nothing in the theory sets our plane's tension -- it is an independent axis, like the README's N
(N is set by the object, 130 (2); sigma by nothing yet).  Closing it takes one input of a named kind; the cypher shows
which kinds close it and the window shows which values survive, but it cannot choose among them.
Imports tools/cypher.py by path.  Stdlib only.  python3 sigma_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
c, G, hbar, eV = 299792458.0, 6.67430e-11, 1.054571817e-34, 1.602176634e-19
KAPPA = 3 * c**4 / (4 * math.pi * G)                     # sigma = KAPPA / ell^2


def _cy():
    spec = importlib.util.spec_from_file_location("sc_cypher", os.path.join(ROOT, "tools", "cypher.py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["sc_cypher"] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def window():
    lP = math.sqrt(hbar * G / c**3)
    m1 = lP * math.sqrt(math.log(2) / math.pi) / 2
    ell_max, ell_min = 13.964e-6, 8.5415 * m1
    if MUT.get("drop_positivity"):
        ell_min = lP / 100
    smin, smax = KAPPA / ell_max**2, KAPPA / ell_min**2
    scale = lambda s: (s * (hbar * c) ** 3) ** 0.25 / eV / 1e9
    cands = {"Higgs 246 GeV": 246.0, "TeV": 1e3, "intermediate 1e11 GeV": 1e11, "GUT 1e16 GeV": 1e16,
             "reduced Planck 2.435e18 GeV": 2.435e18, "Planck 1.2209e19 GeV": 1.2209e19}
    inside = {}
    for name, E in cands.items():
        s = (E * 1e9 * eV) ** 4 / (hbar * c) ** 3
        inside[name] = smin <= s <= smax
    return {"smin": smin, "smax": smax, "gev": (scale(smin), scale(smax)), "inside": inside}


def index_main(cy, sigma_of_N=False):
    cells = []
    for N in range(1, 5):
        for s in range(1, 6):
            if sigma_of_N and s != N:
                continue
            E = N                                          # E(N) = 4.594e8 J sqrt(N), binned: a function of N
            cells.append([1, 1, N, E, s])                  # G, Lambda4 measured (one value each)
    return cy.Index("sigma_main", ["G", "Lambda4", "N", "E", "sigma"], cells)


def fixed_by(cy, ix, target, by):
    """Is `target` a function of the coordinates `by` on this index?  (projection, then information's test)"""
    cols = [ix.coords.index(b) for b in by] + [ix.coords.index(target)]
    proj = sorted({tuple(cl[i] for i in cols) for cl in ix.cells})
    pix = cy.Index("proj", list(by) + [target], [list(p) for p in proj])
    rows, _ = cy.coordinate_report(pix)
    return next(r for r in rows if r["coordinate"] == target)["adds_nothing"]


def binary_by_language(cy, ix):
    """Logic's binary per language: does its admitted set hold two cells with equal (G, Lambda4, N) and different sigma?"""
    out = {}
    for lang in ("order", "algebra", "geometry", "information", "statistics"):
        adm, _ = cy.ADMISSION[lang][0](ix, {})
        if adm is None:
            out[lang] = None
            continue
        seen = {}
        varies = False
        for cl in adm:
            key = cl[:3]
            seen.setdefault(key, set()).add(cl[4])
            varies = varies or len(seen[key]) > 1
        out[lang] = not varies                             # True: sigma fixed by (G, Lambda4, N)
    return out


def candidates(cy):
    res = {}
    base = [(N, s) for N in range(1, 5) for s in range(1, 6)]
    # a measured ell: a coordinate in bijection with sigma
    ix = cy.Index("c_ell", ["G", "Lambda4", "N", "ell", "sigma"], [[1, 1, N, 6 - s, s] for N, s in base])
    res["measured ell"] = fixed_by(cy, ix, "sigma", ["G", "Lambda4", "N", "ell"])
    # Lambda5 with SMS (18): known Lambda5 fixes sigma; Lambda5 unknown leaves it free
    ix = cy.Index("c_L5", ["G", "Lambda4", "N", "Lambda5", "sigma"], [[1, 1, N, s, s] for N, s in base])
    res["Lambda5 known"] = fixed_by(cy, ix, "sigma", ["G", "Lambda4", "N", "Lambda5"])
    res["Lambda5 unknown"] = fixed_by(cy, ix, "sigma", ["G", "Lambda4", "N"])
    # a README equality ell = c m(N): sigma a function of N
    ix = index_main(cy, sigma_of_N=True)
    res["README equality"] = fixed_by(cy, ix, "sigma", ["G", "Lambda4", "N"])
    # one plane, one tension: in one universe U both corridors share sigma; the README equality gives two values
    tensions_in_one_universe = {s for (N, s) in [(n, n) for n in range(1, 5)]}   # sigma = f(N), corridors N = 1..4
    res["README equality keeps one tension"] = len(tensions_in_one_universe) == 1
    return res


def compute():
    cy = _cy()
    ix = index_main(cy)
    rows, keys = cy.coordinate_report(ix)
    dead = {r["coordinate"] for r in rows if r["adds_nothing"]}
    if MUT.get("sigma_from_E"):
        raw = [[1, 1, N, N * 10 + sg, sg] for N in range(1, 5) for sg in range(1, 6)]   # E carrying sigma
        ix = cy.Index("mut", ["G", "Lambda4", "N", "E", "sigma"], raw)
        rows, keys = cy.coordinate_report(ix)
        dead = {r["coordinate"] for r in rows if r["adds_nothing"]}
    return {"w": window(), "dead": dead, "keys": keys, "fixed_main": fixed_by(cy, ix, "sigma", ["G", "Lambda4", "N"]),
            "lang": binary_by_language(cy, ix), "lang_ctrl": binary_by_language(cy, index_main(cy, True)),
            "cand": candidates(cy)}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    w = d["w"]
    add("W1 window: sigma in [1.48e53, 2.75e112] J/m^3, scales 9.18e3 to 6.03e18 GeV",
        1.47e53 < w["smin"] < 1.49e53 and 2.7e112 < w["smax"] < 2.8e112 and 9.1e3 < w["gev"][0] < 9.3e3 and 6.0e18 < w["gev"][1] < 6.1e18)
    add("W2 Higgs and TeV below the window, Planck above it; intermediate, GUT and reduced Planck inside",
        w["inside"] == {"Higgs 246 GeV": False, "TeV": False, "intermediate 1e11 GeV": True, "GUT 1e16 GeV": True,
                        "reduced Planck 2.435e18 GeV": True, "Planck 1.2209e19 GeV": False})
    add("C1 information: sigma is an axis on the theory's index (it adds something); E adds nothing (fixed by N)",
        "sigma" not in d["dead"] and "E" in d["dead"] and not d["fixed_main"])
    add("C1 logic's binary 'sigma fixed by (G, Lambda4, N)': NO in every operator-bearing language; control "
        "(sigma a function of N): YES in every one", all(v is False for v in d["lang"].values())
        and all(v is True for v in d["lang_ctrl"].values()))
    c_ = d["cand"]
    add("C2 a measured ell closes sigma; Lambda5 closes it only when known; a README equality closes it as a function of N",
        c_["measured ell"] and c_["Lambda5 known"] and not c_["Lambda5 unknown"] and c_["README equality"])
    add("C3 one plane, one tension: a README equality gives our one plane a different tension per corridor (refuted)",
        not c_["README equality keeps one tension"])
    return res


MUTANTS = {"drop_positivity": "the window's positivity edge dropped", "sigma_from_E": "E made to carry sigma"}


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
        print("  mutant %-16s %-40s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    w = d["w"]
    print("sigma_cypher.py -- what sets the tension of our universe's plane?\n")
    print("window: sigma in [%.3e, %.3e] J/m^3; sigma^(1/4) in [%.3g, %.3g] GeV" % (w["smin"], w["smax"], *w["gev"]))
    print("  scales:", {k: ("inside" if v else "outside") for k, v in w["inside"].items()})
    print("information on the theory's index: adds nothing =", sorted(d["dead"]), "-> sigma is an axis")
    print("logic's binary 'sigma fixed by what the theory fixes', per language:", d["lang"])
    print("  control (sigma set by N):", d["lang_ctrl"])
    print("candidate setters (closes sigma?):", d["cand"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
