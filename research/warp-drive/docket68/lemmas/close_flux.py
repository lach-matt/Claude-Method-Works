#!/usr/bin/env python3
"""close_flux.py -- the closing's flux, split by trajectory class (computed, deduced, standard-not-READ; not verified by
a separate session; not seated; 2026-10-10).

README-HELD.md named a new OPEN item: the corridor's closing (109, 115 (a), 136 (2)) and the move of 106's hold (E1)
need the horizon's area to shrink, "which classical positive energy forbids (the area theorem, standard-not-READ)".
This instrument asks what that theorem needs, and finds the demand splits by M's two trajectory classes (167, 168:
"two positions, one universe", then between universes).

  K1 (computed, sympy) the two views of one mass loss.  Ingoing Vaidya, m(v) decreasing: the flux along the horizon's
     generators is T_vv = m'(v)/(4 pi r^2) < 0 (a negative influx -- the black-hole side's shrink).  Outgoing Vaidya,
     m(u) decreasing: T_uu = -m'(u)/(4 pi r^2) > 0 (a positive outflow -- a white hole releasing).  132 reads position 2's
     side as the white hole and 136 (2) puts the release at position two.
  K2 (computed) Raychaudhuri on a null surface from theta = 0 (the hold, Lemma S's fixed size):
     d theta/d lambda = -theta^2/2 - sigma^2 - R(k,k).  Positive R(k,k) drives theta < 0 and the area DOWN; zero keeps it;
     negative drives it up.  So a shrink needs no negative energy -- unless the surface's generators may not converge,
     which is the event-horizon property.
  K3 (deduced; standard-not-READ: Hawking-Ellis's area theorem needs the event horizon, the boundary of the causal past
     of future null infinity, whose generators have no future endpoints) the theorem's premise by trajectory class:
       within one universe -- what crosses at position 1 emerges at position 2 in the same universe and reaches its future
         null infinity, so the region behind position 1's horizon is in that causal past: there is NO event horizon.
         The area theorem does not apply; by K2 positive energy can shrink the surface.  The closing's demand for
         negative flux DISSOLVES (what replaces it is B4d's dynamics).
       between universes -- nothing returns to universe 1 (one way, O1), so position 1's horizon is universe 1's event
         horizon; its generators cannot end and its area cannot fall under the NEC.  Closing it (109) needs negative
         null energy or a non-classical step; otherwise a horizon of area >= N A_bit stays in universe 1, against 109 and
         136 answer 3.  The demand STANDS.
  K4 (computed; the cypher CLASSIFIES -- and its cells carry K3's deduction, so it classifies the board's deduction, it
     does not test it independently) roster 1173 on H-CYPHER-CLOSE: the one-universe positive closing is admitted by
     all five (forced: data) and regrown by none when left out; the between-universes positive closing is refused by
     geometry and statistics and admitted by order, algebra and information (their closures over-reach: a caveat).
Named readings (the board's): H-CYPHER-CLOSE; H-CLOSE-SPLITS-BY-CLASS (the deduction K3).
python3 close_flux.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
MUT = {}


def einstein(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                                        for a in range(n)))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(Ric - R * g / 2)


def vaidya():
    w, r, th, ph = sp.symbols("w r theta phi", real=True)
    m = sp.Function("m")(w)
    s = 1 if not MUT.get("vaidya_sign") else -1
    out = {}
    for name, sign in (("ingoing", 1), ("outgoing", -1)):
        f = 1 - 2 * m / r
        g = sp.Matrix([[-f, sign * s, 0, 0], [sign * s, 0, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2 * sp.sin(th)**2]])
        G = einstein(g, [w, r, th, ph])
        out[name] = sp.simplify(G[0, 0] / (8 * sp.pi))            # T_ww, G = c = 1
    mp_ = sp.Derivative(m, w)
    return {"T_in": out["ingoing"], "T_out": out["outgoing"],
            "in_neg_when_losing": sp.simplify(out["ingoing"].subs(mp_, -1)).subs(r, 3) < 0,
            "out_pos_when_losing": sp.simplify(out["outgoing"].subs(mp_, -1)).subs(r, 3) > 0}


def raychaudhuri(Rkk, sigma2=0.0, lam_end=4.0, n=4000):
    """theta(0) = 0 (the hold); integrate d theta = -theta^2/2 - sigma^2 - Rkk; area ratio = exp(int theta)."""
    th, lnA, h = 0.0, 0.0, lam_end / n
    for _ in range(n):
        th += h * (-th * th / 2 - sigma2 - Rkk)
        lnA += h * th
    return th, 2.718281828459045 ** lnA


def event_horizon(cls):
    """K3, STRUCTURAL: position 1's horizon is an event horizon of universe 1 iff no point behind it reaches universe 1's
    future null infinity.  Within one universe the passage's exit (position 2) is in the same universe and reaches it."""
    exit_in_same_universe = (cls == "one universe")
    if MUT.get("exit_ignored"):
        exit_in_same_universe = False
    behind_reaches_scri = exit_in_same_universe                   # one way (O1): never back to position 1 itself
    is_EH = not behind_reaches_scri
    area_theorem_applies = is_EH
    shrink_needs_negative = area_theorem_applies if not MUT.get("theorem_always") else True
    return {"event_horizon": is_EH, "area_theorem": area_theorem_applies, "needs_negative": shrink_needs_negative}


CELLS_C = ["class", "event_horizon", "shrink", "flux"]
# class 0 one universe, 1 between universes | event_horizon 0/1 | shrink 0 none, 1 area falls | flux 0 negative, 1 none, 2 positive
CELLS = {
    "one universe, closing: no EH, area falls under positive focusing (K2, K3)": (0, 0, 1, 2),
    "one universe, the hold: Killing horizon at fixed size, no flux (Lemma S, 163)": (0, 0, 0, 1),
    "between universes, closing: EH, area falls only with a negative influx (K1 ingoing, K3)": (1, 1, 1, 0),
    "between universes, the hold: EH at fixed size, no flux": (1, 1, 0, 1),
    "white hole releasing (outgoing Vaidya, K1): no EH of the receiving side, area falls, positive": (0, 0, 1, 2),
}
TARGET_ONE = (0, 0, 1, 2)          # within one universe, the closing with positive flux
TARGET_TWO = (1, 1, 1, 2)          # between universes, the closing with positive flux -- must be refused


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def cypher():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cf_cypher")
    cells = dict(CELLS)
    if MUT.get("seat_two_positive"):
        cells["(mutant) between universes, positive closing"] = TARGET_TWO
    leave = {k: v for k, v in cells.items() if not (v == TARGET_ONE)}

    def ask(cs, targets):
        cl = sorted(set(cs))
        ix = cy.Index("close", CELLS_C, [list(c) for c in cl])
        enc = lambda t: tuple(ix.code[i][v] if v in ix.code[i] else None for i, v in enumerate(t))
        res = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            res[lang] = None if out is None else [None not in enc(t) and enc(t) in out for t in targets]
        return res
    return {"all": ask(cells.values(), (TARGET_ONE, TARGET_TWO)), "leave": ask(leave.values(), (TARGET_ONE, TARGET_TWO))}


def compute():
    rk = {"positive": raychaudhuri(0.5), "zero": raychaudhuri(0.0), "negative": raychaudhuri(-0.5),
          "shear_only": raychaudhuri(0.0, 0.3)}
    if MUT.get("ray_sign"):
        rk["positive"] = raychaudhuri(-0.5)
    return {"vaidya": vaidya(), "ray": rk, "one": event_horizon("one universe"), "two": event_horizon("between universes"),
            "cy": cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    v = d["vaidya"]
    add("K1 ingoing Vaidya losing mass needs T_vv < 0 along the horizon (negative influx); outgoing Vaidya losing mass "
        "has T_uu > 0 (a white hole releasing with positive energy)", v["in_neg_when_losing"] and v["out_pos_when_losing"])
    rk = d["ray"]
    add("K2 from theta = 0: positive R(k,k) shrinks the area (theta < 0), zero keeps it, negative grows it, shear alone "
        "shrinks it", rk["positive"][1] < 1 and rk["positive"][0] < 0 and abs(rk["zero"][1] - 1) < 1e-12
        and rk["negative"][1] > 1 and rk["shear_only"][1] < 1)
    add("K3 within one universe there is no event horizon, the area theorem does not apply, the closing needs no "
        "negative flux; between universes it is universe 1's event horizon and the demand stands",
        not d["one"]["event_horizon"] and not d["one"]["needs_negative"]
        and d["two"]["event_horizon"] and d["two"]["needs_negative"])
    a, lo = d["cy"]["all"], d["cy"]["leave"]
    add("K4 cypher: the one-universe positive closing admitted by all five (forced: data); the between-universes "
        "positive closing refused by geometry and statistics, admitted by order, algebra and information (STRUCTURAL "
        "caveat); with the one-universe closing left out no language regrows it",
        all(a[l][0] for l in a) and a["geometry"][1] is False and a["statistics"][1] is False
        and a["order"][1] and a["algebra"][1] and a["information"][1] and not any(lo[l][0] for l in lo))
    return res


MUTANTS = {"vaidya_sign": "the cross term's sign flipped in both Vaidya metrics",
           "ray_sign": "positive energy read as defocusing",
           "exit_ignored": "position 2's exit not counted as in the same universe",
           "theorem_always": "the area theorem applied without an event horizon",
           "seat_two_positive": "a between-universes positive closing seated as data"}


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
        print("  mutant %-18s %-58s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    v = d["vaidya"]
    print("close_flux.py -- the closing's flux by trajectory class\n")
    print("K1 ingoing  T_vv =", v["T_in"], "   outgoing T_uu =", v["T_out"])
    for k, (th, A) in d["ray"].items():
        print("K2 R(k,k) %-10s theta_end = %+.4f  area ratio = %.4f" % (k, th, A))
    for cls in ("one", "two"):
        print("K3 %-4s event horizon %s, area theorem %s, closing needs negative flux %s" %
              (cls, d[cls]["event_horizon"], d[cls]["area_theorem"], d[cls]["needs_negative"]))
    for part in ("all", "leave"):
        print("K4 cypher (%s):" % part, d["cy"][part])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
