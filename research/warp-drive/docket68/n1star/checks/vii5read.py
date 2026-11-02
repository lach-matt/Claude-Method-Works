#!/usr/bin/env python3
"""vii5read.py -- the reading (VII5) asks for, held against the census that makes it finite (vii5census.py).

Part VII Lemma 3.1 (proof5/PART-VII-ASSEMBLY.md) averages over O(4) the linear maps given by existence statements (C3),
their families in b (C3') and one complement (C4), and says the proofs of Parts III-IV use those objects "only through
the conditions stated at the sites listed". vii5census.py lists every line of Parts III-IV that names one of them by its
printed symbol outside its site. checks/VII5-READING.tsv records, for each such line, a reader's verdict:
  SITE-ONLY   only the site's conditions are used (or consequences any object meeting them shares);
  NAMING      the line names, cites or restates; no property of the choice is used;
  MORE        a property of the particular choice beyond them is used (the finding that matters);
  UNDECIDED   the reader could not tell;
  HOMONYM     the spelling names another object.
A MORE or UNDECIDED row must carry a resolution: where it is answered, or why the averaged choice still has the property.

  Q1 (computed, a census) The table's lines are exactly the census's use lines for C3, C3', the object built from C3'
     and C4 -- none missing, none extra, none twice -- each with the census's symbols, a verdict from the list above,
     a note where one is required, and the symbol still printed on that line of the file (a stale line number fails).
  Q2 (computed) Every MORE and UNDECIDED row carries a resolution. The counts per verdict are printed.
  Q3 (computed, exact) The amended (C3) takes Table 1.1's towers at b0 as delta*_(g_b0) of the averaged 1-forms; that
     is the average of the unaveraged towers because delta* commutes with O(4): on the Kerr-Schild Tangherlini metric
     g_b0 = eta + (mu/r^2) l l (mu = 3/2), for a generic stationary 1-form (quadratic polynomials plus a 1/r term, random
     rationals) and a rational rotation (Cayley transform) and a reflection, sigma^*(delta* w) = delta*(sigma^* w) and
     sigma^* g = g, at three rational points with |x| rational, exactly. Controls: delta* plus w (x)_s dx^1 (not
     natural) must fail; a shear (not an isometry) must fail.
  Controls (Q1-Q2): the table with one row dropped, with one row doubled, with a verdict misspelt, with a resolution
     removed, and the census widened by one radial cut-off (chi_9, treated as if averaged) must each fail.

Lemma 3.1's (C3) names since D608 the 1-form towers of every type, with their site PART-III-I10-CORR4.md:127-147; the
census keeps those lines as uses, and they were read as such (each NAMING, a definition).

Labels: computed (that the reading covers every listed use and is complete in form; Q3, exact); the verdicts are READ
(each reader's reading of the proof at that line), not computed. Reach: vii5census.py's -- a literal census of printed
symbols.

Run: python3 checks/vii5read.py   (about fifteen seconds)
"""
import csv
import os
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vii5census as V                                                           # noqa: E402

TABLE = os.path.join(HERE, "VII5-READING.tsv")
VERDICTS = ("SITE-ONLY", "NAMING", "MORE", "UNDECIDED", "HOMONYM")
NEED_NOTE = ("MORE", "UNDECIDED", "HOMONYM")
NEED_RES = ("MORE", "UNDECIDED")


def say(s, indent="      "):
    print("\n".join(textwrap.wrap(s, 119, subsequent_indent=indent, break_long_words=False,
                                   break_on_hyphens=False)), flush=True)


def entries(widen=False):
    out = [e for name, es in V.GROUPS if name.startswith(("C3", "C4")) for e in es]
    if widen:
        out += [e for name, es in V.GROUPS if name.startswith("C1") for e in es if e[0] == "\\chi_9"]
    return out


def uses(es):
    """{(file, line): set of symbols used there (not at their site)}"""
    hits = V.census(es, V.files())
    out = {}
    for k, v in hits.items():
        used = {s for s, site in v.items() if not site}
        if used:
            out[k] = used
    return out


def load():
    with open(TABLE, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter="\t")]


def q1(rows, es, show=True):
    want = uses(es)
    seen, bad = {}, []
    text = {}
    for r in rows:
        k = (r["file"], int(r["line"]))
        seen[k] = seen.get(k, 0) + 1
        syms = {s.strip() for s in r["symbols"].split("|")}
        if k in want and syms != want[k]:
            bad.append("%s:%d symbols %s, census %s" % (k[0], k[1], sorted(syms), sorted(want[k])))
        if r["verdict"] not in VERDICTS:
            bad.append("%s:%d verdict %r" % (k[0], k[1], r["verdict"]))
        if r["verdict"] in NEED_NOTE and not r["note"].strip():
            bad.append("%s:%d %s without a note" % (k[0], k[1], r["verdict"]))
        if k[0] not in text:
            text[k[0]] = open(os.path.join(V.P5, k[0]), encoding="utf-8").read().split("\n")
        line = text[k[0]][k[1] - 1] if k[1] <= len(text[k[0]]) else ""
        if not all(s in line for s in syms):
            bad.append("%s:%d no longer prints %s" % (k[0], k[1], sorted(syms)))
    missing = sorted(set(want) - set(seen))
    extra = sorted(set(seen) - set(want))
    twice = sorted(k for k, n in seen.items() if n > 1)
    ok = not (missing or extra or twice or bad)
    if show:
        say("  Q1: %d census use lines (C3, C3', the built object, C4) in %d files; table rows %d; missing %d, extra %d,"
            " doubled %d, malformed %d" % (len(want), len({f for f, _ in want}), len(rows), len(missing), len(extra),
                                           len(twice), len(bad)))
        for x in (missing[:5] + extra[:5] + twice[:5]):
            print("      %s:%d" % x, flush=True)
        for x in bad[:10]:
            say("      " + x)
    return ok


def q2(rows, show=True):
    count = {v: 0 for v in VERDICTS}
    unres = []
    for r in rows:
        count[r["verdict"]] = count.get(r["verdict"], 0) + 1
        if r["verdict"] in NEED_RES and not r.get("resolution", "").strip():
            unres.append("%s:%s" % (r["file"], r["line"]))
    if show:
        say("  Q2: " + ", ".join("%s %d" % (v, count[v]) for v in VERDICTS) +
            "; MORE/UNDECIDED rows without a resolution: %d" % len(unres))
        for r in rows:
            if r["verdict"] in NEED_RES:
                say("      %s:%s %s [%s] %s -- resolution: %s" % (r["file"], r["line"], r["verdict"], r["symbols"],
                                                                 r["note"], r.get("resolution", "")), "        ")
    return not unres


def q3(mode=None):
    """mode None: rotation and reflection; 'extra': a non-natural operator; 'shear': a non-isometry"""
    import random
    import sympy as sp
    T, X = sp.Symbol("t"), sp.symbols("x1:5")
    C = (T,) + X
    r = sp.sqrt(sum(x**2 for x in X))
    ell = [sp.Integer(1)] + [x/r for x in X]
    eta = sp.diag(-1, 1, 1, 1, 1)
    g = sp.Matrix(5, 5, lambda a, b: eta[a, b] + sp.Rational(3, 2)/r**2*ell[a]*ell[b])
    dg = [[[sp.diff(g[a, b], C[c]) for c in range(5)] for b in range(5)] for a in range(5)]

    def at(e, p):
        return sp.simplify(e.subs({T: sp.Rational(1, 3), **{X[i]: p[i] for i in range(4)}}))

    def dstar_at(w, p, extra):
        G = sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))
        Gi = G.inv()
        D = [[[at(dg[a][b][c], p) for c in range(5)] for b in range(5)] for a in range(5)]
        Gam = [[[sum(Gi[c, d]*(D[d][a][b] + D[d][b][a] - D[a][b][d]) for d in range(5))/2 for b in range(5)]
                for a in range(5)] for c in range(5)]
        dw = [[at(sp.diff(w[b], C[a]), p) for b in range(5)] for a in range(5)]
        wp = [at(wi, p) for wi in w]
        M = sp.Matrix(5, 5, lambda a, b: (dw[a][b] + dw[b][a])/2 - sum(Gam[c][a][b]*wp[c] for c in range(5)))
        if extra:
            M += sp.Matrix(5, 5, lambda a, b: (wp[a]*int(b == 1) + wp[b]*int(a == 1))/2)
        return M

    rnd = random.Random(7)

    def q():
        return sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5))
    mono = [sp.Integer(1)] + list(X) + [X[i]*X[j] for i in range(4) for j in range(i, 4)]
    om = [sum(q()*m for m in mono) + q()/r for _ in range(5)]
    A = sp.zeros(4)
    for i in range(4):
        for j in range(i + 1, 4):
            A[i, j] = q()
            A[j, i] = -A[i, j]
    R = (sp.eye(4) - A)*(sp.eye(4) + A).inv()
    maps = [R, R*sp.diag(1, -1, 1, 1)]
    if mode == "shear":
        maps = [sp.Matrix([[1, sp.Rational(1, 2), 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])]
    ok = True
    for S in maps:
        Jm = sp.diag(1, S)
        sub = {X[i]: sum(S[i, j]*X[j] for j in range(4)) for i in range(4)}
        ws = [wi.subs(sub, simultaneous=True) for wi in om]
        pull = [sum(ws[b]*Jm[b, a] for b in range(5)) for a in range(5)]
        for p in [(1, 2, 2, 4), (2, 3, 6, 0), (4, 4, 7, 0)]:
            sp_ = tuple(sum(S[i, j]*p[j] for j in range(4)) for i in range(4))
            nat = (Jm.T*dstar_at(om, sp_, mode == "extra")*Jm - dstar_at(pull, p, mode == "extra")).is_zero_matrix
            iso = (Jm.T*sp.Matrix(5, 5, lambda a, b: at(g[a, b], sp_))*Jm
                   - sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))).is_zero_matrix
            ok = ok and bool(nat) and bool(iso)
    if mode is None:
        say("  Q3: sigma^*(delta* w) = delta*(sigma^* w) and sigma^* g_b0 = g_b0 for a rotation and a reflection at "
            "three rational points, exactly: %s" % ok)
    return ok


def control(rows):
    es = entries()
    dropped = rows[1:]
    doubled = rows + rows[:1]
    misspelt = [dict(r) for r in rows]
    misspelt[0]["verdict"] = "SITE ONLY"
    unresolved = [dict(r) for r in rows]
    tgt = [i for i, r in enumerate(unresolved) if r["verdict"] in NEED_RES]
    if tgt:
        unresolved[tgt[0]]["resolution"] = ""
    else:                                   # no MORE/UNDECIDED row: plant one without a resolution
        unresolved[0]["verdict"], unresolved[0]["note"], unresolved[0]["resolution"] = "MORE", "planted", ""
    fails = [not q1(dropped, es, False), not q1(doubled, es, False), not q1(misspelt, es, False),
             not q2(unresolved, False), not q1(rows, entries(widen=True), False)]
    say("  control: dropped row fails %s; doubled row fails %s; misspelt verdict fails %s; resolution removed fails %s;"
        " census widened by chi_9 fails %s" % tuple(fails))
    return all(fails)


def main():
    rows = load()
    a = q1(rows, entries())
    b = q2(rows)
    c = control(rows)
    d = q3()
    ce, cs = not q3("extra"), not q3("shear")
    e = ce and cs
    say("  Q3 control: delta* plus w (x)_s dx^1 fails %s; a shear fails %s" % (ce, cs))
    print("Q1 %s; Q2 %s; Q3 %s; control %s" % ("PASS" if a else "FAIL", "PASS" if b else "FAIL", "PASS" if d else "FAIL",
                                              "behaves" if c and e else "MISBEHAVES"), flush=True)
    return 0 if a and b and c and d and e else 1


if __name__ == "__main__":
    sys.exit(main())
