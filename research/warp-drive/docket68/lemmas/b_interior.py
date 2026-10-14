#!/usr/bin/env python3
"""b_interior.py -- item 272 (b), the first owed item: how the black-hole interior continues into the white-hole interior,
the one object of O1a ("a black hole in and a white hole out ... different views of the same object", 132) at the
family's small end.  m1p2x_oneway.py's index holds on that glued object and not on the eternal Kruskal manifold
(O2b), so this decides whether C8 stands.  Worked in the conversation (computed with sympy, exact where marked; READ
where marked; deduced where marked; the cypher run and audited; not verified by a separate session; not seated);
2026-10-12.

[M, item 277: "You are forgetting that the passage is one-way only".  B6 populated cells whose white hole exits into our exterior -- a white hole facing us, item 270's reverse
passage.  Kept as written, those cells the record of the two-way reading; the one-way re-closure is i_oneway.py.]

  B0 (read) M's item-272 words, verbatim in the rulings file.
  B1 (READ) Penrose's theorem, Senovilla & Garfinkle, arXiv:1410.5226, Theorem 2, p.10: "If the space-time contains a
     non-compact Cauchy hypersurface Sigma and a closed future-trapped surface, and if the convergence condition (6)
     holds for null u, then there are future incomplete null geodesics"; p.11, the three ways out: "(6) is violated for
     null vectors, or the concept of space-time loses its meaning at extreme conditions (maybe quantum effects), or
     some null geodesics are not complete"; p.16, the Hawking-Penrose theorem "holds in arbitrary dimension -- in
     which case the closed trapped surface is a co-dimension two trapped submanifold".
  B2 (computed, exact) The hole's interior holds closed trapped 3-spheres: inside r_h the surfaces r = const have
     angular extrinsic curvature -sqrt(r_h^2 - r^2) along the future normal -- both future null expansions negative.
     So by B1 any continuation of the black-hole interior into a white hole gives up one of three: the null energy
     condition pointwise, a Cauchy surface (an inner horizon), or completeness (no continuation: the singularity item
     259 admitted).
  B3 (READ) The inner-horizon route.  A charged or rotating hole's interior continues through an inner (Cauchy)
     horizon into a white hole opening on another exterior -- one-way by its causal structure -- but Hamilton,
     arXiv:1703.01921, p.1: "the Poisson-Israel mass inflation instability at the inner horizon of an accreting,
     rotating black hole is generically followed by Belinskii-Khalatnikov-Lifshitz oscillatory collapse to a spacelike
     singularity"; and the route needs charge or spin the README alone does not carry.
  B4 (READ) The quantum bounce.  Haggard & Rovelli, arXiv:1407.0989, p.1: "a classical metric satisfying the Einstein
     equations outside a finite spacetime region where matter collapses into a black hole and then emerges from a white
     hole"; p.2: it "is locally isometric to the Kruskal solution (outside the quantum region), but it is not a portion
     of the Kruskal solution. Rather, it is a portion of a double cover of the Kruskal solution"; p.5: the quantum
     region is one "where the classical Einstein equations and the standard energy conditions do not hold"; the white
     hole there emerges into the same exterior (assumption (vi), Minkowski causal structure), after an exterior time
     of order m^2/l_P (eq. (2)).  Its two-exterior form -- the white hole opening on position 2's exterior -- is not
     constructed there.  The board's reading of 132 for it: the image of the collapsing half under the Kruskal isometry
     (U, V) -> (-U, -V) (m1p2x_small X1), which carries our exterior and future interior onto position 2's exterior and
     past interior -- named, not constructed.
  B5 (computed, exact) The classical gluing.  Join the future interior to the past interior across the spacelike
     surface r = r0 < r_h: the future normal's extrinsic curvature flips sign, so Israel's condition puts a surface
     stress there (S_tt = -6 (r_h^2 - r0^2)^(3/2)/(kappa^2 r0^4), angular 2 (2 r0^2 - r_h^2)/(kappa^2 sqrt(r_h^2 - r0^2))).
     A radial null ray crossing it gathers -6/(kappa^2 r0): negative at every r0 < r_h -- B1's way out, explicit; an
     angular ray, negative for r0 < r_h/sqrt2.  The README as an infalling null shell cannot pair it on the ingoing
     rays it moves along: a null shell's stress mu l^a l^b gives T_ab k^a k^b = mu (l.k)^2 = 0 on k parallel to l
     (computed) -- so under 183 those rays stay unpaired by the README.
  B6 (computed; the cypher, roster 1173, audited) The continuations laid on an index -- inner horizon {0, 1}, bounce
     {none, quantum, classical shell}, white hole's exit {our exterior, position 2's} -- six physical cells, each
     populated with what B1-B5 compute or READ: one_way (the white hole opens on position 2's exterior), nec (pointwise),
     gh (no Cauchy horizon), complete (no singularity on the way), classical, readme_only (nothing added: no charge,
     spin or shell).  No cell holds all six -- B1 forbids one_way, nec, gh and complete together.  The audit flags nec
     and complete as complementary across every cell: Penrose's theorem showing in the index, so the cypher's verdicts
     are void as evidence (211), the theorem standing in their place.  The cell that gives up least among M's words is
     the quantum bounce into position 2's exterior: one_way, gh, complete, readme_only; it gives up pointwise null
     energy in the quantum region (to be paired per ray, 183) and classicality.  The classical shell into position 2's
     exterior gives up nec and readme_only.
     [Item 317 (the C5 verifier's Q1, accepted): withdrawn -- by Raychaudhuri's identity, integral R_kk d lambda =
     theta_in - theta_out - integral theta^2/3 d lambda < 0 on every ray the bounce turns, and R_kk counts the README's
     null energy too; no matter on the ray brings its net to zero.  The part was set against the total it belongs to.
     273's "paired per ray under 183" against 183's zero net per ray is put to M (c5_oneway U12 (Q1)).]

What this does not show.
  - The two-exterior bounce's construction (B4), its null energy per ray and what pairs it (183), and its time: Haggard
    and Rovelli's m^2/l_P is a 4D estimate; the 5D small hole's against the write's floor and the hold is not computed.
  - Which way out M takes.

Imports index_audit.py and tools/cypher.py by path.  Stdlib + sympy.  python3 b_interior.py [--selftest | --mutants]
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
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M272 = "Not yet, we have to close everything that is still owed"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
PROPS = ["one_way", "nec", "gh", "complete", "classical", "readme_only"]

r, rh, r0, kap2 = sp.symbols("r r_h r_0 kappa2", positive=True)


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


def _g():
    return rh ** 2 / r ** 2 - 1                           # inside the horizon f = -g, r timelike


def K(sign):
    """extrinsic curvature of r = const with n^r = sign sqrt(g): -1 the future interior (contracting), +1 the past"""
    g = _g()
    nr = sign * sp.sqrt(g)
    return sp.Rational(1, 2) * nr * sp.diff(g, r), sp.Rational(1, 2) * nr * sp.diff(r ** 2, r)


def trapped():
    return sp.simplify(K(-1)[1])


def shell():
    g = _g()
    KtF, KaF = K(-1)
    KtP, KaP = K(+1)
    if MUT.get("no_flip"):
        KtP, KaP = KtF, KaF                                # the mutant glues without the flip: no shell
    jt, ja = sp.simplify(KtP - KtF), sp.simplify(KaP - KaF)
    trK = sp.simplify(jt / g + 3 * ja / r ** 2)
    eps = -1                                               # spacelike surface
    Stt = sp.simplify(-(eps / kap2) * (jt - g * trK))
    Sang = sp.simplify(-(eps / kap2) * (ja - r ** 2 * trK))
    kn = sp.sqrt(g) / g                                    # |k.n| for the radial ray with k^r = -1, k^t = 1/g
    radial = sp.simplify((Stt * (1 / g) ** 2 / kn).subs(r, r0))
    ka2 = 1 / (g * r ** 2)                                 # angular ray with k^r = 1, k^t = 0
    angular = sp.simplify((Sang * ka2 / kn).subs(r, r0))
    return dict(Stt=Stt.subs(r, r0), Sang=Sang.subs(r, r0), radial=radial, angular=angular)


def readme_on_its_rays():
    """a null shell mu l^a l^b against a ray k parallel to l: T_ab k^a k^b = mu (l.k)^2 with l.l = 0"""
    mu = sp.Symbol("mu", positive=True)
    eta = sp.diag(-1, 1, 1, 1, 1)
    l = sp.Matrix([1, 1, 0, 0, 0])
    k = 2 * l
    lk = (l.T * eta * k)[0]
    return sp.simplify(mu * lk ** 2)


def cells():
    """the six physical cells (inner, bounce, exit) and their properties from B1-B5"""
    out = {}
    for inner, bounce, exit_ in ((0, "none", "ours"), (1, "none", "pos2"), (0, "quantum", "ours"),
                                 (0, "quantum", "pos2"), (0, "shell", "ours"), (0, "shell", "pos2")):
        one_way = int(exit_ == "pos2" and (inner == 1 or bounce != "none"))
        nec = int(bounce == "none")
        gh = int(inner == 0)
        complete = int(bounce != "none")                   # B2: no bounce, no Cauchy horizon -> singular; B3: inner ->
        if inner == 1:                                     # mass inflation -> spacelike singularity generically
            complete = 0
        if MUT.get("evade_penrose") and inner == 0 and bounce == "none":
            complete = 1                                    # the mutant ignores B1
        classical = int(bounce != "quantum")
        readme_only = int(inner == 0 and bounce != "shell")
        out[(inner, bounce, exit_)] = dict(one_way=one_way, nec=nec, gh=gh, complete=complete, classical=classical,
                                           readme_only=readme_only)
    return out


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "bi_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "bi_ia")
    ix = cy.Index("b_interior", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    return dict(held=held, all6=tuple([1] * 6) in held, E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(PROPS, held))


def penrose(rows):
    """B1 in the index: no cell has one_way, nec, gh and complete together"""
    return not any(p["one_way"] and p["nec"] and p["gh"] and p["complete"] for p in rows.values())


def compute():
    rows = cells()
    return dict(trapped=trapped(), shell=shell(), readme=readme_on_its_rays(), rows=rows, penrose=penrose(rows),
                cy=cypher(rows))


def report(o):
    print("b_interior.py -- the black-hole interior's continuation into the white-hole interior (item 272 (b))\n")
    print("B2 angular extrinsic curvature inside, future normal: %s (trapped)" % o["trapped"])
    s = o["shell"]
    print("B5 the classical gluing at r0: S_tt %s, S_angular %s; radial ray %s; angular ray %s" % (
        s["Stt"], s["Sang"], s["radial"], s["angular"]))
    print("   the README's null shell on its own rays: T_kk = %s" % o["readme"])
    print("B6 %-26s %s" % ("cell (inner, bounce, exit)", " ".join("%-11s" % p for p in PROPS)))
    for c, p in o["rows"].items():
        print("   %-26s %s" % (str(c), " ".join("%-11d" % p[q] for q in PROPS)))
    c = o["cy"]
    print("   Penrose in the index (no one_way & nec & gh & complete): %s; all six held: %s; E %s; audit %s" % (
        o["penrose"], c["all6"], c["E"], c["audit"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("B0 M's item-272 words verbatim in the rulings file", M272 in rul)
    add("B2 the interior's 3-spheres are trapped: angular K = -sqrt(r_h^2 - r^2) along the future normal",
        sp.simplify(o["trapped"] + sp.sqrt(rh ** 2 - r ** 2)) == 0)
    s = o["shell"]
    ok = sp.simplify(s["radial"] + 6 / (kap2 * r0)) == 0
    ok &= sp.simplify(s["angular"] - 2 * (2 * r0 ** 2 - rh ** 2) / (kap2 * r0 * (rh ** 2 - r0 ** 2))) == 0
    add("B5 the classical gluing: radial rays gather -6/(kappa^2 r0) < 0 at every r0 < r_h; angular rays "
        "2(2 r0^2 - r_h^2)/(kappa^2 r0 (r_h^2 - r0^2)), negative below r_h/sqrt2", ok)
    add("B5 the README's null shell gives zero null energy on the rays it moves along", o["readme"] == 0)
    c = o["cy"]
    ok = o["penrose"] and not c["all6"] and ("nec", "complete") in [tuple(x) for x in c["audit"]["onehot"]]
    q2 = o["rows"][(0, "quantum", "pos2")]
    ok &= q2["one_way"] and q2["gh"] and q2["complete"] and q2["readme_only"] and not q2["nec"] and not q2["classical"]
    add("B6 no continuation holds all six (Penrose in the index); nec and complete complementary (the audit's flag); the "
        "quantum bounce into position 2's exterior gives up only nec (pointwise) and classical", ok)
    return res


MUTANTS = {"no_flip": "the interiors glued without flipping the normal (no shell)",
           "evade_penrose": "the singular reading counted complete (B1 ignored)"}


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
        print("  mutant %-13s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
