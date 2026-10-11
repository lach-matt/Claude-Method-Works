#!/usr/bin/env python3
"""m1p2x_sixth.py -- item 268: the sixth coordinate, position 2's plane's own matter (184), its total surface energy --
tension -sigma/4 plus matter -- positive (139 (2), H-P2-TOTAL-POSITIVE), added to m1p2x_index's populated index, the
index repopulated and the cypher run.  M: "Yes, tension plus matter".  Worked in the conversation (computed with
sympy, exact where marked; deduced where marked; the cypher run and audited; not verified by a separate session; not
seated); 2026-10-11.

  W0 (read) M's item-268 words, verbatim in the rulings file.
  W1 (computed, exact) A ray crossing a plane of total surface energy e and pressure P at angle a picks up e sin a + (e
     + P) cos^2 a / sin a, non-negative on every ray iff e >= 0 and e + P >= 0 (m1x_cypher X2's condition, here for an
     isotropic plane).  Position 2's pure tension (e = -sigma/4, P = +sigma/4) fails it; with its own matter of surface
     energy rho >= sigma/4 and rho + p >= 0 it passes -- the total positive, as 139 (2) and item 268 have it.
  W2 (computed, exact) Static matter cannot stand at a horizon: for a static observer of f, (u.l)^2 = 1/f for the
     ingoing null l with l.xi = -1, so a static fluid's null stress (e + P)(u.l)^2 diverges at r_h unless e + P = 0.
     Position 2's matter near the hole therefore either falls through position 2's horizons -- crossing without a jump,
     so it leaves m1p2x_index Y1's junction law, mu' = -[lambda], unchanged (deduced) -- or is tension-like, e = -P.
  W3 (computed, exact) Tension-like matter, S = -m h, is more tension: the junction's law becomes mu' = -[lambda + m],
     and the junction vanishes iff lambda + m is continuous -- for position 2's -sigma/4 against our +sigma, m =
     5 sigma/4, total +sigma: position 2's plane's whole stress is then ours, reading (A) of m1p2x_small under another
     name.  Whether vacuum-like matter on position 2's plane is "matter" or "tension" is a definition (202: "the same
     definitions as we do, perhaps different values"), not a computation.
  W4 (computed; the cypher, roster 1173, audited) The index with the sixth coordinate m2 in {0: none, 1: matter that
     falls (rho >= sigma/4, rho + p >= 0), 2: tension-like (m = 5 sigma/4)} on every -sigma/4 piece: 48 cells.  Over
     (keeps139, reads_leg, d_ours, z_net) the all-four cell is REACHED -- by m2 = 1 with the hole's interiors at our
     tension and position 2's plane through the bridge (the junctions on position 2's horizons, none on ours; every
     crossing ray's share non-negative), and by m2 = 2 in every cell keeping 139 (1) and the leg.  The cypher's
     predicted member of m1p2x_index is found: position 2's plane with its own matter, total positive.
     Over the five properties with the junctions' own null energy (junction_ok: none, or mu >= 0 along every one) the
     all-five cell is reached only by m2 = 2 -- reading (A) renamed.  With matter that falls (m2 = 1) the junction on
     position 2's future horizon still falls: an in-plane ray crossing it late sees -(10/pi)(r_h/ell) E~ E
     (m1p2x_fifth F1), whether position 2's own infalling matter pairs it on those rays (183) not computed.

What this does not show.
  - The proof 139 (2) orders: that position 2's matter has rho >= sigma/4 -- sigma/4 = 3 c^4/(16 pi G ell^2) = 3.7e52
    J/m^3 at ell = 13.964 um (computed, W5), 1.8e18 times nuclear matter's 2.07e34 J/m^3 (2.3e17 kg/m^3 c^2): the
    plane's own scale, not ordinary matter's.  The index places the requirement; it does not meet it.
  - The pairing of the falling junction by position 2's infalling matter along in-plane rays (183).
  - Which value of m2 M takes; 202 bears on m2 = 2.

Imports m1p2x_index.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 m1p2x_sixth.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M268 = "Yes, tension plus matter"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
NEG, POS = sp.Rational(-1, 4), sp.Integer(1)
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


def crossing_share():
    a = sp.Symbol("a", positive=True)
    e, P = sp.symbols("e P", real=True)
    share = sp.simplify((e + P * sp.cos(a) ** 2) / sp.sin(a))       # S(k_par, k_par)/|n.k|, k = (1, cos a, sin a)
    form = sp.simplify(share - (e * sp.sin(a) + (e + P) * sp.cos(a) ** 2 / sp.sin(a)))
    lim_normal = sp.limit(share, a, sp.pi / 2)                        # -> e
    lim_graze = sp.limit(share * sp.sin(a), a, 0)                     # -> e + P
    sig = sp.Symbol("sigma", positive=True)
    rho, p = sp.symbols("rho p", real=True)
    pure = share.subs({e: -sig / 4, P: sig / 4})
    with_matter = dict(e=-sig / 4 + rho, P=sig / 4 + p)
    return dict(share=share, form=form, lim_normal=lim_normal, lim_graze=lim_graze, pure=sp.simplify(pure),
                with_matter=with_matter)


def static_blueshift():
    r, rh = sp.symbols("r r_h", positive=True)
    f = 1 - rh ** 2 / r ** 2
    # static u = d_t / sqrt(f); ingoing null l with l.xi = -1: l^t = 1/f, l^r = -1; u.l = g_tt u^t l^t = -f (1/sqrt f)(1/f)
    ul = -f * (1 / sp.sqrt(f)) * (1 / f)
    return dict(ul2=sp.simplify(ul ** 2), at_horizon=sp.limit(ul ** 2, r, rh, dir="+"))


def populate(MI, law):
    s = law["mu_prime"]
    rows = {}
    for s2, sF, sP, apart, m2 in itertools.product((NEG, POS), (NEG, POS), (NEG, POS), (0, 1), (0, 1, 2)):
        lam = dict(I=POS, II=s2, F=sF, P=sP)
        m_tl = sp.Rational(5, 4) if (m2 == 2 and not MUT.get("tl_wrong")) else (sp.Rational(1, 2) if m2 == 2 else 0)
        eff = {k: v + (m_tl if v == NEG else 0) for k, v in lam.items()}   # W3: tension-like matter adds to tension
        js = {}
        for name, (plus, minus, kind) in MI.BORDERS.items():
            jump = eff[plus] - eff[minus]
            if jump == 0:
                continue
            mp = s.subs({law["lp"]: eff[plus], law["lm"]: eff[minus]})
            js[name] = bool(mp >= 0) if kind == "future" else bool(mp <= 0)
        neg_pieces = [v for v in (s2, sF, sP) if v == NEG] + ([NEG] if apart else [])
        z_net = int(all(m2 >= 1 for _ in neg_pieces)) if not MUT.get("matter_ignored") else int(not neg_pieces)
        rows[(s2, sF, sP, apart, m2)] = dict(
            keeps139=int(s2 == NEG or apart == 1), reads_leg=int(s2 == NEG),
            d_ours=int(not any(n.startswith("our") for n in js)), z_net=z_net, junction_ok=int(all(js.values())),
            junctions=js)
    return rows


def cypher(rows, coords, tag):
    held = sorted({tuple(p[c] for c in coords) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "m6_cy_" + tag)
    ia = _load(os.path.join(HERE, "index_audit.py"), "m6_ia_" + tag)
    ix = cy.Index("m1p2x6_" + tag, coords, [list(c) for c in held], value_order={c: [0, 1] for c in coords})
    run = cy.run(ix, "1173", dict(OPTS))
    target = tuple([1] * len(coords))
    return dict(held=held, reached=target in held, E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(coords, held),
                holders=sorted(c for c, p in rows.items() if tuple(p[x] for x in coords) == target))


def scale():
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "m6_pg")
    q = 3 * PG.C ** 4 / (16 * 3.141592653589793 * PG.G * PG.ELL_MAX ** 2)    # sigma/4, J/m^3 (p2_planck, offset dropped)
    nuclear = 2.3e17 * PG.C ** 2
    return dict(quarter=q, nuclear=nuclear, ratio=q / nuclear)


def compute():
    MI = _load(os.path.join(HERE, "m1p2x_index.py"), "m6_mi")
    law = MI.junction_law()
    rows = populate(MI, law)
    c4 = cypher(rows, ["keeps139", "reads_leg", "d_ours", "z_net"], "four")
    c5 = cypher(rows, ["keeps139", "reads_leg", "d_ours", "z_net", "junction_ok"], "five")
    return dict(w1=crossing_share(), w2=static_blueshift(), rows=rows, c4=c4, c5=c5, w5=scale())


def report(o):
    print("m1p2x_sixth.py -- the sixth coordinate: position 2's plane's own matter (item 268)\n")
    w = o["w1"]
    print("W1 crossing share %s; at a -> pi/2: %s; grazing: %s; position 2's pure tension: %s" % (
        w["share"], w["lim_normal"], w["lim_graze"], w["pure"]))
    print("W2 a static observer's (u.l)^2 = %s, at the horizon %s" % (o["w2"]["ul2"], o["w2"]["at_horizon"]))
    print("W5 sigma/4 = %.3g J/m^3 at the table-top ell, %.3g x nuclear matter" % (o["w5"]["quarter"], o["w5"]["ratio"]))
    for k in ("c4", "c5"):
        c = o[k]
        print("W4 %s: profiles %d, all reached %s, E %s, audit %s" % (k, len(c["held"]), c["reached"], c["E"], c["audit"]))
        for h in c["holders"]:
            print("     holder s2 %s sF %s sP %s apart %d m2 %d" % h)


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("W0 M's item-268 words verbatim in the rulings file", M268 in rul)
    w = o["w1"]
    e, P = sp.symbols("e P", real=True)
    sig = sp.Symbol("sigma", positive=True)
    a = sp.Symbol("a", positive=True)
    ok = w["form"] == 0 and sp.simplify(w["lim_normal"] - e) == 0 and sp.simplify(w["lim_graze"] - (e + P)) == 0
    ok &= sp.simplify(w["pure"] + sig * sp.sin(a) / 4) == 0
    add("W1 crossing share e sin a + (e + P) cos^2 a/sin a: non-negative iff e >= 0, e + P >= 0; position 2's pure "
        "tension gives -sigma sin a/4", ok)
    r, rh = sp.symbols("r r_h", positive=True)
    add("W2 static matter's (u.l)^2 = 1/f diverges at the horizon", sp.simplify(o["w2"]["ul2"] - 1 / (1 - rh ** 2 / r ** 2))
        == 0 and o["w2"]["at_horizon"] == sp.oo)
    c4, c5 = o["c4"], o["c5"]
    ok = c4["reached"] and (NEG, POS, POS, 0, 1) in c4["holders"] and (NEG, POS, POS, 1, 1) in c4["holders"]
    ok &= all(h[4] >= 1 for h in c4["holders"]) and not any(h[4] == 0 for h in c4["holders"])
    add("W4 the all-four cell is reached: m2 = 1 with the interiors at our tension (and every m2 = 2 cell keeping 139 "
        "(1) and the leg); never with m2 = 0", ok)
    ok = c5["reached"] and all(h[4] == 2 for h in c5["holders"])
    add("W4 the all-five cell (with the junctions' own null energy) only by m2 = 2 -- reading (A) renamed", ok)
    add("W5 sigma/4 = 3.7e52 J/m^3 at ell = 13.964 um, 1.8e18 x nuclear matter",
        "%.2g" % o["w5"]["quarter"] == "3.7e+52" and "%.2g" % o["w5"]["ratio"] == "1.8e+18")
    return res


MUTANTS = {"matter_ignored": "position 2's matter left out of the crossing share",
           "tl_wrong": "tension-like matter of the wrong amount (sigma/2, not 5 sigma/4)"}


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
        print("  mutant %-14s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
