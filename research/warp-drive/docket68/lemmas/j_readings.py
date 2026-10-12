#!/usr/bin/env python3
"""j_readings.py -- item 278: "Compute the 2 readings".  The two readings the proof of 139 (2) rested on (h_oneway,
i_oneway) computed rather than read: (i) 276's one-way junction -- our sheet's junction carries our stress alone,
position 2's carries ours, received, and its own; (ii) 139 (3)'s expansion read as unbounded.  Worked in the
conversation (computed with sympy, exact where marked; deduced where marked; estimates marked; not verified by a
separate session; not seated); 2026-10-12.

  J0 (read) M's item-278 words and 139 (3)'s, verbatim in the rulings file.
  J1 (computed, exact) Reading (i) at the corridor, from the one-way object's causal structure.  Its charts: our
     exterior (U < 0 < V) and our future interior (U, V > 0) on our sheet of the double cover; position 2's past
     interior (U, V < 0) and its exterior (V < 0 < U) on position 2's sheet (b_bounce Q1); the only join between the
     sheets is the bounce, from our future interior into position 2's past interior (H-BOUNCE-TO-P2).  Along future
     causal curves U and V never decrease, so a chart reaches its neighbour across U = 0 or V = 0 only in the increasing
     direction.  The reachability computed: ours reaches position 2's exterior; position 2's exterior reaches nothing
     on our sheet, and the causal past of our exterior is our exterior alone.  So nothing of position 2's -- its
     stress, its gravity -- is in the causal past of our sheet's junction there, while ours is in the causal past of
     position 2's.  On the eternal Kruskal manifold (position 2's exterior beside our future interior across V = 0) it
     would reach our interior: the reverse passage.
  J2 (computed, exact) Reading (i) away from the corridor, where the sheets coincide (275) and no causal structure
     separates them: take any linear junction, ours carrying S1 + chi S2, position 2's tau S1 + S2.  Our expansion,
     H1^2/c^2 = (kappa^2 (sigma + chi S2)/6)^2 - k^2 (S1 = sigma = 6k/kappa^2), is independent of S2 for every S2 exactly
     when chi = 0: 276 ("one-way in all aspects") forces chi = 0, and that half is not a reading.  What 276 leaves open
     is tau, how much of ours position 2 receives.  For every tau in [0, 1] position 2's late-time expansion has the sign
     of (tau sigma + S2 - sigma)(tau sigma + S2 + sigma), the second factor positive for rho_m >= 0, so unbounded
     expansion needs S2 >= (1 - tau) sigma >= 0: positivity holds for every tau, and is strictest when nothing is
     received.
  J3 (computed, exact) Reading (ii) from 139 (3)'s own words: "Absorbing of the README into position 2 is an expansion
     of that universe which means the README/information itself is the trigger".  A trigger starts an expansion: before
     the README position 2 is not expanding.  With H2^2/c^2 = F(S2) + C2/a^4 and C2 >= 0, dH2^2/da = -4 C2/a^5 <= 0: a
     contracting universe never turns to expanding (its scale factor has maxima, no minima).  The only non-expanding
     state an expansion can start from is static -- H2 = 0 and dH2^2/da = 0 -- which needs C2 = 0 and F(S2) = 0, so S2 =
     (1 - tau) sigma (the root -(1 + tau) sigma needs rho_m < 0).  There F'(S2) = (kappa^4/18) sigma > 0: the README's
     positive energy, raising S2, starts an expansion that is unbounded.  So the unbounded expansion follows from M's
     trigger, not from a reading; before the README position 2 sits at rho_m = sigma/4 + (1 - tau) sigma, after it above.
  J4 (deduced) The proof of 139 (2) on the one-way object, no reading left but tau, which J2 covers: position 2's total
     S2 >= (1 - tau) sigma >= 0 before the README and above it after; rho_m >= sigma/4 -- equal only when position 2
     receives all of ours (tau = 1) and only before the README, where its total is zero.  "Positive" (139 (2)) holds
     from the README on.
  J5 (the cypher NOT-RUN, stated) J1-J3 are exact identities, not cells to choose among: laid on an index their
     columns (trigger possible, unbounded after, S2 >= 0) coincide row for row, which index_audit reads as a one-hot
     code and voids (211), as h_oneway's first run showed.  Not run, and said.

What this does not show.
  - The value of tau: J2 shows the conclusion holds for all of it.
  - The README's trigger as a local event on an infinite sheet: its energy over the sheet is nil on the homogeneous
    scale; within 2.0e-15 m it exceeds sigma/4 (e_positive E7).  That the static state is unstable (F' > 0) is what
    lets a local trigger start it -- how it spreads is not computed (estimate).
  - Reading (i) away from the corridor rests on 276 for chi = 0; no causal structure computes it there.

Imports h_oneway.py by path.  Stdlib + sympy.  python3 j_readings.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M278 = "Compute the 2 readings"
M139 = "Absorbing of the README into position 2 is an expansion of that universe which means the README/information " \
       "itself is the trigger"
# chart: (sheet, sign of U, sign of V)
CHARTS = {"our exterior": ("ours", -1, 1), "our future interior": ("ours", 1, 1),
          "position 2's past interior": ("p2", -1, -1), "position 2's exterior": ("p2", 1, -1)}
GLUE = [("our future interior", "position 2's past interior")]          # the bounce, H-BOUNCE-TO-P2


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def causal():
    """J1: future-directed edges between charts, from U and V non-decreasing, plus the glue; then reachability"""
    u, v, kap = sp.symbols("u v kappa", real=True)
    inc_U = sp.simplify(sp.diff(-sp.exp(-kap * u), u) / (kap * sp.exp(-kap * u))) == 1
    inc_V = sp.simplify(sp.diff(sp.exp(kap * v), v) / (kap * sp.exp(kap * v))) == 1
    charts = dict(CHARTS)
    if MUT.get("eternal_adjacency"):
        charts["position 2's exterior"] = ("ours", 1, -1)  # the mutant puts it beside our future interior (V = 0)
    edges = set(GLUE)
    for a, (sa, ua, va) in charts.items():
        for b, (sb, ub, vb) in charts.items():
            if a == b or sa != sb or (ua != ub) + (va != vb) != 1:
                continue                                   # same sheet, one shared boundary
            if (ua < ub and inc_U) or (va < vb and inc_V):
                edges.add((a, b))                          # crossing in the increasing direction only

    def reach(start):
        seen, todo = {start}, [start]
        while todo:
            x = todo.pop()
            for (p, q) in edges:
                if p == x and q not in seen:
                    seen.add(q)
                    todo.append(q)
        return seen

    past_ours = {c for c in charts if "our exterior" in reach(c)}
    return dict(edges=sorted(edges), reach_ours=sorted(reach("our exterior")),
                reach_p2=sorted(reach("position 2's exterior")), past_ours=sorted(past_ours))


def junction():
    """J2: chi from 276; the late-time sign for every tau"""
    kap2, sig, S2, chi, tau = sp.symbols("kappa5sq sigma S_2 chi tau", real=True)
    k = kap2 * sig / 6
    H1 = (kap2 * (sig + chi * S2) / 6) ** 2 - k ** 2
    if MUT.get("chi_back"):
        H1 = H1.subs(chi, sp.Rational(1, 10))              # the mutant lets position 2 reach our junction
    dH1 = sp.simplify(sp.diff(H1, S2))
    chi_sol = sp.solve(sp.Poly(sp.expand(dH1), S2).coeffs(), chi, dict=True) if dH1.has(chi) else []
    late = sp.expand((kap2 * (tau * sig + S2) / 6) ** 2 - k ** 2)
    fact = sp.simplify(late - kap2 ** 2 / 36 * (tau * sig + S2 - sig) * (tau * sig + S2 + sig)) == 0
    floor_ok = True
    for t in (sp.Integer(0), sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), sp.Integer(1)):
        lt = late.subs({kap2: 1, sig: 1, tau: t})
        for s2 in (-sp.Rational(1, 4), (1 - t) / 2, 1 - t, 1 - t + sp.Rational(1, 100), 2):
            pos = bool(lt.subs(S2, s2) > 0)
            floor_ok &= pos == bool(s2 > 1 - t)
        floor_ok &= bool((t + S2 + 1).subs(S2, -sp.Rational(1, 4)) > 0)    # the second factor at rho_m = 0
    return dict(dH1=dH1, chi_sol=chi_sol, fact=fact, floor_ok=floor_ok, H1_free=not dH1.has(S2) and dH1 == 0)


def trigger():
    """J3: no turning from contraction; the static state; its instability"""
    kap2, sig, S2, C2, a, tau = sp.symbols("kappa5sq sigma S_2 C_2 a tau", positive=True)
    F = kap2 ** 2 / 36 * ((tau * sig + S2) ** 2 - sig ** 2)
    H2 = F + C2 / a ** 4
    dHa = sp.diff(H2, a)
    if MUT.get("turn_allowed"):
        dHa = -dHa                                         # the mutant lets a contracting universe turn
    no_turn = bool(sp.simplify(dHa + 4 * C2 / a ** 5) == 0)
    S2r = sp.Symbol("S_2", real=True)
    Fr = F.subs(S2, S2r)
    roots = sp.solve(sp.Eq(Fr, 0), S2r)
    Fp = sp.simplify(sp.diff(Fr, S2r).subs(S2r, (1 - tau) * sig))
    return dict(no_turn=no_turn, roots=sorted(roots, key=str), Fp=Fp,
                static_root=any(sp.simplify(r - (1 - tau) * sig) == 0 for r in roots),
                other_root=any(sp.simplify(r + (1 + tau) * sig) == 0 for r in roots),
                unstable=sp.simplify(Fp - kap2 ** 2 * sig / 18) == 0)


def compute():
    return dict(c=causal(), j=junction(), t=trigger())


def report(o):
    print("j_readings.py -- item 278: the two readings computed\n")
    c = o["c"]
    print("J1 edges %s" % c["edges"])
    print("   from our exterior: %s; from position 2's exterior: %s; causal past of our exterior: %s" % (
        c["reach_ours"], c["reach_p2"], c["past_ours"]))
    j = o["j"]
    print("J2 dH1^2/dS2 = %s, zero for every S2 iff %s; late-time sign factorises: %s; floor S2 > (1 - tau) sigma at "
          "tau = 0, 1/4, 1/2, 3/4, 1: %s" % (j["dH1"], j["chi_sol"], j["fact"], j["floor_ok"]))
    t = o["t"]
    print("J3 dH2^2/da = -4 C2/a^5 (no turning): %s; F(S2) = 0 at %s; F' at the static root = %s" % (
        t["no_turn"], t["roots"], t["Fp"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("J0 M's item-278 and 139 (3) words verbatim in the rulings file", M278 in rul and M139 in rul)
    c = o["c"]
    ok = "position 2's exterior" in c["reach_ours"] and not ({"our exterior", "our future interior"} &
                                                             set(c["reach_p2"]))
    ok &= c["past_ours"] == ["our exterior"]
    add("J1 ours reaches position 2's exterior; position 2's exterior reaches nothing on our sheet; our exterior's "
        "causal past is itself", ok)
    j = o["j"]
    ok = j["chi_sol"] == [{sp.Symbol("chi", real=True): 0}] and j["fact"] and j["floor_ok"]
    add("J2 our expansion is free of S2 exactly when chi = 0 (276); for every tau in [0, 1] unbounded expansion needs "
        "S2 > (1 - tau) sigma", ok)
    t = o["t"]
    add("J3 no turning from contraction (dH2^2/da = -4 C2/a^5); the static state S2 = (1 - tau) sigma; F' = "
        "(kappa^4/18) sigma > 0 there", t["no_turn"] and t["static_root"] and t["other_root"] and t["unstable"])
    return res


MUTANTS = {"eternal_adjacency": "position 2's exterior put beside our future interior",
           "chi_back": "position 2 let reach our junction",
           "turn_allowed": "a contracting universe let turn to expanding"}


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
        print("  mutant %-18s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
