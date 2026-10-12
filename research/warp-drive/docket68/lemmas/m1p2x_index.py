#!/usr/bin/env python3
"""m1p2x_index.py -- item 265: M1P2x's three readings at the small end laid on an index and every cell populated.  M:
"We're missing something(s). If we lay these results on an index we can populate more information".  The coordinates
are the configuration's own: the tension on exterior II's equator (s2), the tension on the plane inside the hole's future
and past interiors (sF, sP -- where m1p2x_small X3's change of tension falls is fixed by them), and whether a further
plane stands apart in exterior II at -sigma/4 (apart).  Ours, on exterior I, is +sigma throughout.  Worked in the
conversation (computed with sympy, exact where marked; deduced where marked; the cypher run and audited; not verified
by a separate session; not seated); 2026-10-11.

[M, item 270: "You are forgetting that the passage is one-way only".  This instrument populated the eternal hole's
half-horizons as if the corridor ran both ways -- position 2's future horizon and our past horizon (V = 0) are the
reverse passage, and its past horizons were stretched to an infinite past.  Superseded by m1p2x_oneway.py; kept as
the record of the two-way reading, its computations (the junction's law, the crossing share, the sweeps) standing.]

  Y0 (read) M's item-265 words, verbatim in the rulings file.
  Y1 (computed, exact) The junction's law.  Where the plane's tension changes across a horizon of the plane (V = 0 in
     the Kruskal form -F(UV) dU dV + r(UV)^2 dOmega^2, generator k = d/dU), conservation of the plane's stress -- its
     tension plus a null stress mu k^a k^b on the horizon -- holds only if mu'(U) = -[lambda], [lambda] the tension on
     the V > 0 side less that on the V < 0 side (the delta(V) part of the divergence, computed at V = 0; the other
     component vanishes).  So the junction is never static: its null energy density changes linearly along its
     generators at the rate the jump sets.  The generators' affine parameter grows as e^(tau c/r_h) with the Killing
     time tau (U ~ e^(kappa tau), C1 H4), so a junction whose mu falls loses its null energy within a number of clocks
     logarithmic in its starting value -- not computed further here.
  Y2 (computed, exact: the four half-horizons with their orientation) A junction keeps mu >= 0 along its whole
     half-horizon -- a future horizon runs from the bifurcation sphere to the future, a past horizon from the past to it
     -- if and only if the hole's interior beside it carries the lesser tension: lambda_F, lambda_P <= min(lambda_I,
     lambda_II) on every stressed horizon.  With 139 (1)'s +sigma | -sigma/4 that is the interiors at -sigma/4: the
     junctions then lie on OUR horizons, growing along our future horizon.
  Y3 (computed) The populated index, 16 cells.  The three readings sit in it: (A) = (1, 1, 1, 0), (C) = (1, 1, 1, 1),
     (B) = the four cells s2 = -1/4, apart = 0 -- which m1p2x_small left as one.  Populated, (B) splits by where its
     junctions fall, and two properties the three readings did not carry separate its cells: clause (d) on our side
     (no stress on our plane or its horizons) and the junctions' null energy kept along their whole horizons.  Among the
     cells keeping 139 (1) and reading the leg (s2 = -1/4), those two are exclusive: (d) on our side needs the interiors
     at +sigma, putting the junctions on position 2's horizons, where mu falls; the null energy kept needs the interiors
     at -sigma/4, putting the junctions on ours.  Read the other way, (C) is (A) with a further plane: our plane's
     continuation through the bridge stays on exterior II's equator in every cell -- a plane cannot end -- so "position
     2's plane apart" means two planes in position 2's bulk, ours continued and theirs.
  Y4 (computed; the cypher, roster 1173, audited) The cells' property profiles over (keeps139, reads_leg, d_ours,
     nec_kept) -- seven distinct -- put to the cypher.  The audit is clean: no key, no one-hot code, so the verdicts are
     evidence (211).  None of the sixteen cells holds all four, but every operator-bearing language admits the cell that
     does: order and algebra admit it among five new cells, geometry, information and statistics admit it alone (E =
     1).  The populated index is not closed, and what its closure adds is exactly the missing cell -- the cypher's way
     of saying a coordinate is missing: no setting of (s2, sF, sP, apart) reaches a profile all five languages predict.
     Candidates for the fifth coordinate (named, none computed): the junction's starting null energy over a finite
     hold -- a junction on position 2's horizons keeps mu >= 0 for as long as its start pays for the fall, so the hold's
     length and what the junction carries in (the README, 251; 139 (3): "the README/information itself is the
     trigger") enter; 183's pairing, net per ray, in place of the pointwise null energy; Y5's two.
  Y5 (named, not laid) Two coordinates the eternal index cannot carry: a hole formed by collapse has no exterior II and
     no past interior (C1 verifier, item 254), so position 2's side does not exist there -- ARRIVAL's question (198);
     and between universes position 2's bulk has its own ell_2 = 2 ell (m1x_cypher X0), so at warp order the two bulks
     meet across the bridge with a further junction in the bulk -- not computed.

What this does not show.
  - Magnitudes: the junction's starting null energy, how many clocks a falling junction lasts, and whether the README
    (E, item 251) could be that starting energy; net null energy per ray (183) across any junction or negative plane.
  - Which cell M takes.

Imports index_audit.py and tools/cypher.py by path.  Stdlib + sympy.  python3 m1p2x_index.py [--selftest | --mutants]
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
M265 = "We're missing something(s). If we lay these results on an index we can populate more information"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
NEG, POS = sp.Rational(-1, 4), sp.Integer(1)              # tensions in units of sigma; ours is POS


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


def junction_law():
    """the delta(V) part of D_a S^ab for S = -lambda(V) g^ab + mu(U) delta(V) k^a k^b (2/F), k = d/dU, at V = 0"""
    U, V, th, ph = sp.symbols("U V theta phi", real=True)
    Fz, Rz = sp.Function("F"), sp.Function("R")
    lm, lp = sp.symbols("lam_minus lam_plus", real=True)
    mu = sp.Function("mu")(U)
    F, r = Fz(U * V), Rz(U * V)
    x = [U, V, th, ph]
    g = sp.zeros(4)
    g[0, 1] = g[1, 0] = -F / 2
    g[2, 2], g[3, 3] = r ** 2, r ** 2 * sp.sin(th) ** 2
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                            for d in range(4)) / 2) for c in range(4)] for b in range(4)] for a in range(4)]
    lam = lm + (lp - lm) * sp.Heaviside(V)
    k = [1, 0, 0, 0]
    S = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            S[a, b] = -lam * gi[a, b] + mu * sp.DiracDelta(V) * k[a] * k[b] * 2 / F
    out = []
    for b in (0, 1):
        e = sum(sp.diff(S[a, b], x[a]) for a in range(4))
        e += sum(Gam[a][a][c] * S[c, b] for a in range(4) for c in range(4))
        e += sum(Gam[b][a][c] * S[a, c] for a in range(4) for c in range(4))
        out.append(sp.simplify(sp.expand(e).coeff(sp.DiracDelta(V)).subs(V, 0)))
    sol = sp.solve(sp.Eq(out[0], 0), sp.diff(mu, U))
    return dict(coeffs=out, mu_prime=sp.simplify(sol[0]) if sol else None, lm=lm, lp=lp)


# the four half-horizons of the plane: (regions on the V>0 / U>0 side and the other, future or past horizon).  For each,
# "plus" is the region on the positive side of the coordinate that vanishes there (Y1's V > 0, by the U <-> V symmetry).
BORDERS = {"our future horizon (U = 0, V > 0)": ("F", "I", "future"),
           "our past horizon (V = 0, U < 0)": ("I", "P", "past"),
           "position 2's future horizon (V = 0, U > 0)": ("F", "II", "future"),
           "position 2's past horizon (U = 0, V < 0)": ("II", "P", "past")}


def populate(law):
    s = law["mu_prime"]
    rows = {}
    for s2, sF, sP, apart in itertools.product((NEG, POS), (NEG, POS), (NEG, POS), (0, 1)):
        lam = dict(I=POS, II=s2, F=sF, P=sP)
        if MUT.get("no_interiors"):
            lam.update(F=POS, P=POS)
        js = {}
        for name, (plus, minus, kind) in BORDERS.items():
            jump = lam[plus] - lam[minus]
            if jump == 0:
                continue
            mp = s.subs({law["lp"]: lam[plus], law["lm"]: lam[minus]})
            if MUT.get("flip_sign"):
                mp = -mp
            # a future horizon runs from the bifurcation sphere forward: mu >= 0 throughout needs mu' >= 0; a past
            # horizon runs from the past into it: needs mu' <= 0
            kept = bool(mp >= 0) if kind == "future" else bool(mp <= 0)
            js[name] = dict(jump=jump, mu_prime=mp, kept=bool(kept))
        ours = [n for n in js if n.startswith("our")]
        rows[(s2, sF, sP, apart)] = dict(
            junctions=js, keeps139=int(s2 == NEG or apart == 1), reads_leg=int(s2 == NEG), d_ours=int(not ours),
            nec_kept=int(all(j["kept"] for j in js.values())), stress_free=int(not js),
            z_pointwise=int(bool(min(s2, sF, sP) > 0) and apart == 0))
    return rows


def rule(rows):
    """Y2: nec_kept iff, on every stressed horizon, the interior beside it (F or P) carries the lesser tension"""
    ok = True
    for (s2, sF, sP, apart), p in rows.items():
        lam = dict(I=POS, II=s2, F=sF, P=sP)
        pred = True
        for plus, minus, _ in BORDERS.values():
            if lam[plus] == lam[minus]:
                continue
            inner, outer = (plus, minus) if plus in ("F", "P") else (minus, plus)
            pred &= lam[inner] < lam[outer]
        ok &= pred == bool(p["nec_kept"])
    return ok


def cypher(rows):
    coords = ["keeps139", "reads_leg", "d_ours", "nec_kept"]
    held = sorted({tuple(p[c] for c in coords) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "mxi_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "mxi_ia")
    ix = cy.Index("m1p2x_index", coords, [list(c) for c in held], value_order={c: [0, 1] for c in coords})
    run = cy.run(ix, "1173", dict(OPTS))
    admits = {}
    for lg in ("order", "algebra", "geometry", "information", "statistics"):
        a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
        dec = None if a is None else {tuple(ix.decode[i][x[i]] for i in range(len(coords))) for x in a}
        admits[lg] = None if dec is None else sorted(dec - set(held))
    return dict(coords=coords, held=held, all4=(1, 1, 1, 1) in held, admits=admits,
                E={v["language"]: v["E"] for v in run["verdicts"]}, audit=ia.audit_index(coords, held))


def compute():
    law = junction_law()
    rows = populate(law)
    return dict(law=law, rows=rows, rule=rule(rows), cy=cypher(rows))


def _name(cell):
    s2, sF, sP, apart = cell
    return "s2 %5s sF %5s sP %5s apart %d" % (s2, sF, sP, apart)


def report(o):
    print("m1p2x_index.py -- M1P2x's readings laid on an index, every cell populated (item 265)\n")
    print("Y1 delta(V) coefficients at V = 0: %s; so mu'(U) = %s" % (o["law"]["coeffs"], o["law"]["mu_prime"]))
    print("Y2 the junctions keep mu >= 0 iff the interiors carry the lesser tension: %s\n" % o["rule"])
    print("Y3 %-38s %-8s %-9s %-6s %-8s %-6s  junctions" % ("cell", "keeps139", "reads_leg", "d_ours", "nec_kept",
                                                              "Z_pt"))
    for cell, p in o["rows"].items():
        js = "; ".join("%s mu' %s%s" % (n.split(" (")[0], j["mu_prime"], "" if j["kept"] else " (falls)")
                       for n, j in p["junctions"].items()) or "none"
        print("   %-38s %-8d %-9d %-6d %-8d %-6d  %s" % (_name(cell), p["keeps139"], p["reads_leg"], p["d_ours"],
                                                       p["nec_kept"], p["z_pointwise"], js))
    c = o["cy"]
    print("\nY4 property profiles %s; all four held: %s; E %s; audit %s" % (c["held"], c["all4"], c["E"], c["audit"]))
    for lg, new in c["admits"].items():
        print("   %-11s admits beyond the held: %s" % (lg, new))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Y0 M's item-265 words verbatim in the rulings file", M265 in rul)
    law = o["law"]
    add("Y1 conservation across a null junction: mu'(U) = -(lambda_plus - lambda_minus); the transverse component 0",
        law["mu_prime"] is not None and sp.simplify(law["mu_prime"] + law["lp"] - law["lm"]) == 0
        and sp.simplify(law["coeffs"][1]) == 0)
    rows = o["rows"]
    add("Y2 the junctions keep their null energy along their whole horizons iff the hole's interiors carry the lesser "
        "tension", o["rule"])
    leg = {c: p for c, p in rows.items() if p["reads_leg"] and p["keeps139"]}
    ok = len(leg) == 8 and not any(p["d_ours"] and p["nec_kept"] for p in leg.values())
    ok &= rows[(NEG, POS, POS, 0)]["d_ours"] == 1 and rows[(NEG, POS, POS, 0)]["nec_kept"] == 0
    ok &= rows[(NEG, NEG, NEG, 0)]["d_ours"] == 0 and rows[(NEG, NEG, NEG, 0)]["nec_kept"] == 1
    ok &= rows[(POS, POS, POS, 0)]["stress_free"] == 1 and rows[(POS, POS, POS, 1)]["keeps139"] == 1
    add("Y3 keeping 139 (1) and reading the leg, (d) on our side and the junctions' null energy kept are exclusive: "
        "interiors at +sigma put the junctions on position 2's horizons (falling), at -sigma/4 on ours (kept)", ok)
    c = o["cy"]
    ok = not c["all4"] and c["audit"]["keys"] == [] and c["audit"]["onehot"] == [] and len(c["held"]) == 7
    ok &= all(new is not None and (1, 1, 1, 1) in new for new in c["admits"].values())
    ok &= all(c["admits"][lg] == [(1, 1, 1, 1)] for lg in ("geometry", "information", "statistics"))
    add("Y4 no cell holds all four; the audit is clean; every language's closure admits the all-four cell (geometry, "
        "information and statistics that cell alone) -- a coordinate is missing", ok)
    return res


MUTANTS = {"flip_sign": "the junction's law with mu' = +[lambda]",
           "no_interiors": "the hole's interiors left out of the plane (tension never changes there)"}


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
        print("  mutant %-12s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
