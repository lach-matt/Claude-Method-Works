#!/usr/bin/env python3
"""open_index.py -- item 247: the infinite bulk index is not closed and never can be; whatever can be imagined is
plausible.  M, on the board's "not shown: that the whole infinite index is closed": "it is not closed and never can be.
This comes back to first principles and observation with imagine being a legitimate perception of reality. Thus , if it
can be imagined, it exists within plausibility."  Seated as M's ruling; taken through the cypher (196) as a
demonstration, not a proof.  Worked in the conversation (computed, exact where marked; deduced where marked; not
verified by a separate session; not seated beyond M's ruling); 2026-10-11.

  O0 (read) M's item-247 words, and item 121's and item 233's, verbatim in the rulings file.
  O1 (computed; the cypher, roster 1173, 5D basis, each axis ordered away from ours) Imagined universes reopen the
     index.  Start from the closed unit cell (item 246, twenty-four, E = 0).  Imagine a universe it does not hold and
     add it: half a 2P step (G x 2^(1/2), tension x 2^-1).  Order and algebra E rise to 5: the index is open.  The
     cypher closes it by admitting five more (thirty cells, E = 0) -- and the step the closed index now needs along 2P
     is a sixth.  Imagine a fifth of a 2P step: open again (E 2), closed at thirty-three, the step a thirtieth.  A
     seventh: open (E 2), closed at thirty-six, a 210th.  Half a 2b step: open (E 20), closed at fifty-seven, 2b now
     in halves.  A matter law between min and mirror (item 233 K7: the law is continuous, three values computed): open,
     E 18.  An offset's ratio no member carries, at one universe: open.  Every imagined universe reopened the index, and
     every closure the cypher found was only until the next.
  O2 (deduced) Why never.  By M's ruling whatever can be imagined is plausible, and the continuous axes (G, the tension,
     the offset's ratio, the matter law) have no least step and no last value that imagination respects: between any
     two imagined values another can be imagined, and beyond any, another.  A closed index is fixed by its alphabet and
     its envelopes (§15.2, X = ℛ(X)); each round of O1 is one imagined value outside the alphabet the last closure
     fixed, and it reopens the index.  Since imagination always supplies another, no closure is the last.  This shows
     M's ruling consistent with The Method's own definition of a closed index; it does not prove M's principle, which
     is M's.
  O3 (computed) Closed cells, open whole.  Each imagined universe of O1 is itself a closed cell (item 8, item 244):
     every constant with a form holds on it (closed_bounds' evaluator, 1e-12) and its own index is closed under its own
     conditions in both regime readings (cell_closure's test).  The whole never closes; every cell does.
  O4 (computed; the reading of item 247 (a)) Plausibility and the theorem's conditions.  Plausibility is everything
     imaginable; what bulk5_index K3-K4 and the instruments after it called "plausible" is the set within the theorem's
     conditions (its top, floors and capacity).  The imagined universes of O1 lie within the theorem's conditions (each
     has a window); an imagined G x 2^99 lies outside them -- its tension can sit under no top -- and is plausible all
     the same.  Every constant holds on it; its own index under the theorem's conditions is empty.
  O5 (the board's reading of item 247 (b)) Item 121's "closed index criteria, self referencing and self defending" are
     met cell by cell (item 244) and never by the whole; Theorem row B3's "complete bulk" is B4a-B4d's global
     spacetime, not a closed totality.  No status moves.

What this does not show.
  - That imagination is a perception of reality: M's first principle, taken as given.
  - The rounds are four imagined steps, one law and one offset; O2's "never" is the deduction, not the count.

Imports unit_cell.py (and through it bulk5_index.py), closed_bounds.py, cell_closure.py and tools/cypher.py by path.
Stdlib.  python3 open_index.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M247 = ("That the whole infinite index is closed. - it is not closed and never can be. This comes back to first principles "
        "and observation with imagine being a legitimate perception of reality. Thus , if it can be imagined, it exists "
        "within plausibility.")
M121 = "yes. And we build it under closed index criteria, self referencing and self defending"
M233 = "The 5D bulk should contain every plausible and possible statistical universe"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
LAWS = ("ours", "min", "mirror")


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


UC = _load(os.path.join(HERE, "unit_cell.py"), "oi_uc")
B5 = UC.B5
PP = B5.PP

# (name, i 2b-steps, j 2P-steps): universes the unit cell does not hold, imagined in turn
IMAGINED = [("half a 2P step", F(0), F(1, 2)), ("a fifth of a 2P step", F(0), F(1, 5)),
            ("a seventh of a 2P step", F(0), F(1, 7)), ("half a 2b step", F(1, 2), F(0))]
FAR = ("G x 2^99", F(99), F(0))


def c5(law, g, s, offset=None):
    """5D basis (matter, 3 ell/l5, kappa5^4) for any (g, s); with offset, the offset's ratio as a fourth coordinate"""
    c = (F(law), -(2 * g + s), g - s)
    return c if offset is None else c + (F(offset),)


def decode(c):
    g = (c[2] - c[1]) / 3
    s = g - c[2]
    return (c[0], g, s)


def run(cy, held):
    d = len(held[0])
    coords = ["matter", "ell_l5_x3", "kappa5_4", "offset"][:d]
    vals = [sorted({c[x] for c in held}, key=lambda t: (abs(t), t)) for x in range(d)]
    ix = cy.Index("open", coords, [list(c) for c in held], value_order={coords[x]: vals[x] for x in range(d)})
    adm = {}
    for lg in ("order", "algebra"):
        a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
        adm[lg] = {tuple(ix.decode[x][c[x]] for x in range(d)) for c in a}
    return adm


def cell():
    return {c5(LAWS.index(l), g, s) for l, g, s in B5.UNIT_CELL.values()}


def rounds(cy):
    held = set(cell())
    out = []
    E0 = {lg: len(a) - len(held) for lg, a in run(cy, sorted(held)).items()}
    for name, i, j in IMAGINED:
        if MUT.get("no_reopen"):
            i, j = F(0), F(1, 3)
        g, s = i + j, -2 * j
        h = sorted(held | {c5(0, g, s)})
        adm = run(cy, h)
        E = {lg: len(a) - len(h) for lg, a in adm.items()}
        closed = sorted(adm["order"] | adm["algebra"])
        Ec = {lg: len(a) - len(closed) for lg, a in run(cy, closed).items()}
        step_j = math.lcm(*[(-decode(c)[2] / 2).denominator for c in closed])
        step_i = math.lcm(*[(decode(c)[1] + decode(c)[2] / 2).denominator for c in closed])
        out.append(dict(name=name, i=i, j=j, E=E, closed=len(closed), E_closed=Ec, step_j=step_j, step_i=step_i))
        held = set(closed)
    law = F(3, 2) if not MUT.get("law_on_grid") else F(2)
    h = sorted(held | {c5(0, 0, 0)[:0] + (law, F(0), F(0))})
    E_law = {lg: len(a) - len(h) for lg, a in run(cy, h).items()}
    h4 = sorted({c + (F(0),) for c in held} | {(F(0), F(0), F(0), F(1))})
    E_off = {lg: len(a) - len(h4) for lg, a in run(cy, h4).items()}
    return dict(E0=E0, rounds=out, E_law=E_law, E_off=E_off, final=len(held))


def cells_closed():
    """O3: each imagined universe a closed cell -- the constants hold, its own index closed (both regime readings)"""
    cb = _load(os.path.join(HERE, "closed_bounds.py"), "oi_cb")
    cc = _load(os.path.join(HERE, "cell_closure.py"), "oi_cc")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "oi_cy2")
    c = {k: F(v) for k, v in cc.CB.BD.constants().items()}
    out = {}
    for name, i, j in IMAGINED + [FAR]:
        g, s = i + j, -2 * j
        hb = 2.0 if MUT.get("constants_off") and name == IMAGINED[0][0] else 1.0
        ev = cb.evaluate_sector(PP.sector(2.0 ** float(g), 2.0 ** float(s)), hb)
        holds = all(abs(x - 1) < 1e-12 for vs in ev.values() for x in vs)
        own = {}
        for rd in ("regime as a regime", "regime as a bound"):
            reg = cc.region(i, j, cc.READINGS[rd], cc.default(), c)
            own[rd] = (len(reg), bool(cc.closing_orders(cy, reg)) if reg else None)
        k = B5.constants()
        out[name] = dict(holds=holds, own=own, window=B5.w_interval(i, j, k, "rel"))
    return out


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "oi_cy")
    return dict(r=rounds(cy), cells=cells_closed())


def report(o):
    print("open_index.py -- the infinite bulk index is never closed; the imaginable is plausible (item 247)\n")
    r = o["r"]
    print("O1 the closed unit cell: E %s" % r["E0"])
    for x in r["rounds"]:
        print("  imagine %-24s (i, j) = (%s, %s): E %s -> the cypher closes it at %d cells (E %s); steps now 2b in 1/%d, "
              "2P in 1/%d" % (x["name"], x["i"], x["j"], x["E"], x["closed"], x["E_closed"], x["step_i"], x["step_j"]))
    print("  imagine a matter law between min and mirror: E %s" % r["E_law"])
    print("  imagine an offset's ratio no member carries, at one universe: E %s" % r["E_off"])
    print("\nO3/O4 each imagined universe as a cell:")
    for n, x in o["cells"].items():
        print("  %-24s constants hold %s; within the theorem's conditions %s; own index %s" % (
            n, x["holds"], x["window"] is not None,
            {rd: ("%d cells, closed %s" % v) if v[0] else "empty" for rd, v in x["own"].items()}))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("O0 M's item-247 words, and items 121's and 233's, verbatim in the rulings file",
        M247 in rul and M121 in rul and M233 in rul)
    r = o["r"]
    ok = r["E0"] == {"order": 0, "algebra": 0}
    ok &= all(x["E"]["order"] > 0 and x["E"]["algebra"] > 0 and x["E_closed"] == {"order": 0, "algebra": 0}
              for x in r["rounds"])
    ok &= [x["closed"] for x in r["rounds"]] == [30, 33, 36, 57]
    ok &= [x["step_j"] for x in r["rounds"]] == [6, 30, 210, 210] and r["rounds"][-1]["step_i"] == 2
    ok &= r["E_law"]["order"] > 0 and r["E_off"]["order"] > 0
    add("O1 every imagined universe reopens the closed index (E > 0), and each closure lasts only to the next: the cell "
        "closes at 30, 33, 36, 57 cells as half, a fifth, a seventh of 2P and half of 2b are imagined (2P's step 1/6, "
        "1/30, 1/210; 2b's 1/2); an imagined law and an imagined offset reopen it too", ok)
    cl = o["cells"]
    ok = all(x["holds"] for x in cl.values())
    ok &= all(x["window"] is not None and all(v[0] > 0 and v[1] for v in x["own"].values())
              for n, x in cl.items() if n != FAR[0])
    ok &= cl[FAR[0]]["window"] is None and all(v[0] == 0 for v in cl[FAR[0]]["own"].values())
    add("O3/O4 each imagined universe is a closed cell (the constants hold; its own index closed under both regime "
        "readings) and lies within the theorem's conditions; G x 2^99 lies outside them (no window, its own index empty) "
        "and every constant holds on it -- plausible by item 247", ok)
    return res


MUTANTS = {"no_reopen": "the imagined universe taken on the cell's own thirds (already held)",
           "law_on_grid": "the imagined law taken as the mirror law (already held)",
           "constants_off": "hbar doubled at the first imagined universe"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


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
        print("  mutant %-13s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
