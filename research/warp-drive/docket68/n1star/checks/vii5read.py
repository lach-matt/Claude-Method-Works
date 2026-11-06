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
import re
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


ANCHOR = re.compile(r'\{(PART-[A-Z0-9-]+\.md) \(([^)]+)\):((?: "[^"]+")+)\}')


def paragraph(fname, label, text=None):
    """the paragraph of proof5/fname that begins with '(label)', whitespace-normalised ('' if none)"""
    t = text if text is not None else open(os.path.join(V.P5, fname), encoding="utf-8").read()
    for par in re.split(r"\n\s*\n", t):
        if par.lstrip().startswith("(%s)" % label):
            return " ".join(par.split())
    return ""


def resolution_ok(res, texts=None):
    """a resolution must cite a paragraph and quote it: {FILE (LABEL): "phrase" ...}, each phrase found there"""
    found = ANCHOR.findall(res)
    if not found:
        return False, "no {FILE (LABEL): \"phrase\"} anchor"
    for fname, label, quoted in found:
        par = paragraph(fname, label, (texts or {}).get(fname))
        if not par:
            return False, "no paragraph (%s) in %s" % (label, fname)
        for ph in re.findall(r'"([^"]+)"', quoted):
            if " ".join(ph.split()) not in par:
                return False, "%s (%s) does not print %r" % (fname, label, ph)
    return True, ""


def q2(rows, show=True, texts=None):
    count = {v: 0 for v in VERDICTS}
    unres, bad = [], []
    for r in rows:
        count[r["verdict"]] = count.get(r["verdict"], 0) + 1
        if r["verdict"] in NEED_RES:
            res = r.get("resolution", "").strip()
            if not res:
                unres.append("%s:%s" % (r["file"], r["line"]))
            else:
                good, why = resolution_ok(res, texts)
                if not good:
                    bad.append("%s:%s %s" % (r["file"], r["line"], why))
    if show:
        say("  Q2: " + ", ".join("%s %d" % (v, count[v]) for v in VERDICTS) +
            "; MORE/UNDECIDED rows without a resolution: %d; resolutions whose cited text is not printed where they "
            "say: %d" % (len(unres), len(bad)))
        for x in bad[:5]:
            say("      " + x)
        for r in rows:
            if r["verdict"] in NEED_RES:
                say("      %s:%s %s [%s] %s -- resolution: %s" % (r["file"], r["line"], r["verdict"], r["symbols"],
                                                                 r["note"], r.get("resolution", "")), "        ")
    return not unres and not bad


def q3(mode=None, show=True):
    """mode None: the computation; 'extra': delta* plus a non-natural term; 'shear': a non-isometry; 'nochr': delta*
    without its Christoffel term; 'flip': with the Christoffel term's sign flipped. Returns {part: bool}."""
    import random
    import sympy as sp
    T, X = sp.Symbol("t"), sp.symbols("x1:5")
    C = (T,) + X
    r = sp.sqrt(sum(x**2 for x in X))
    mu = sp.Rational(3, 2)
    ell = [sp.Integer(1)] + [x/r for x in X]
    eta = sp.diag(-1, 1, 1, 1, 1)
    g = sp.Matrix(5, 5, lambda a, b: eta[a, b] + mu/r**2*ell[a]*ell[b])
    lsh = [-ell[0]] + ell[1:]                                       # eta^-1 l; l is null for eta
    ginv = sp.Matrix(5, 5, lambda a, b: eta[a, b] - mu/r**2*lsh[a]*lsh[b])   # Kerr-Schild inverse, checked below
    dg = [[[sp.diff(g[a, b], C[c]) for c in range(5)] for b in range(5)] for a in range(5)]
    chr_sign = {"nochr": 0, "flip": -1}.get(mode, 1)

    def at(e, p):
        return sp.simplify(sp.sympify(e).subs({T: sp.Rational(1, 3), **{X[i]: p[i] for i in range(4)}}))

    def dstar_at(w, p, extra):
        G = sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))
        Gi = G.inv()
        D = [[[at(dg[a][b][c], p) for c in range(5)] for b in range(5)] for a in range(5)]
        Gam = [[[sum(Gi[c, d]*(D[d][a][b] + D[d][b][a] - D[a][b][d]) for d in range(5))/2 for b in range(5)]
                for a in range(5)] for c in range(5)]
        dw = [[at(sp.diff(w[b], C[a]), p) for b in range(5)] for a in range(5)]
        wp = [at(wi, p) for wi in w]
        M = sp.Matrix(5, 5, lambda a, b: (dw[a][b] + dw[b][a])/2 - chr_sign*sum(Gam[c][a][b]*wp[c] for c in range(5)))
        if extra:
            M += sp.Matrix(5, 5, lambda a, b: (wp[a]*int(b == 1) + wp[b]*int(a == 1))/2)
        return M

    def lie_half_at(w, p):
        """(1/2) L_X g, X = g^-1 w: X^c d_c g_ab + g_cb d_a X^c + g_ac d_b X^c, no Christoffel symbol"""
        Xv = [sum(ginv[c, d]*w[d] for d in range(5)) for c in range(5)]
        dX = [[at(sp.diff(Xv[c], C[a]), p) for a in range(5)] for c in range(5)]
        Xp = [at(xc, p) for xc in Xv]
        G = sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))
        D = [[[at(dg[a][b][c], p) for c in range(5)] for b in range(5)] for a in range(5)]
        return sp.Matrix(5, 5, lambda a, b: (sum(Xp[c]*D[a][b][c] for c in range(5)) + sum(G[c, b]*dX[c][a] for c in
                                             range(5)) + sum(G[a, c]*dX[c][b] for c in range(5)))/2)

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
    pts = [(1, 2, 2, 4), (2, 3, 6, 0), (4, 4, 7, 0)]
    nat = True
    for S in maps:
        Jm = sp.diag(1, S)
        sub = {X[i]: sum(S[i, j]*X[j] for j in range(4)) for i in range(4)}
        ws = [wi.subs(sub, simultaneous=True) for wi in om]
        pull = [sum(ws[b]*Jm[b, a] for b in range(5)) for a in range(5)]
        for p in pts:
            sp_ = tuple(sum(S[i, j]*p[j] for j in range(4)) for i in range(4))
            n_ = (Jm.T*dstar_at(om, sp_, mode == "extra")*Jm - dstar_at(pull, p, mode == "extra")).is_zero_matrix
            iso = (Jm.T*sp.Matrix(5, 5, lambda a, b: at(g[a, b], sp_))*Jm
                   - sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))).is_zero_matrix
            nat = nat and bool(n_) and bool(iso)
    out = {"nat": nat}
    if mode in (None, "nochr", "flip"):
        inv_ok = all((sp.Matrix(5, 5, lambda a, b: at(g[a, b], p))*sp.Matrix(5, 5, lambda a, b: at(ginv[a, b], p))
                      - sp.eye(5)).is_zero_matrix for p in pts + [(1, 2, 2, 0)])
        lie = inv_ok and all((dstar_at(om, p, False) - lie_half_at(om, p)).is_zero_matrix for p in pts)
        dt = [sp.Integer(1), 0, 0, 0, 0]
        hand_val = dstar_at(dt, (1, 2, 2, 0), False)[0, 0]
        hand = hand_val == -mu**2/3**5                              # (delta* dt)_00 = -mu^2/r^5 at r = 3: -1/108
        rot = [0, -X[1], X[0], 0, 0]                                # x1 d_2 - x2 d_1 (components)
        kill = all(dstar_at([sum(g[a, b]*v[b] for b in range(5)) for a in range(5)], p, False).is_zero_matrix
                   for v in ([1, 0, 0, 0, 0], rot) for p in pts)
        out.update({"lie": lie, "hand": hand, "kill": kill, "hand_val": hand_val})
    if show and mode is None:
        say("  Q3: (a) sigma^*(delta* w) = delta*(sigma^* w) and sigma^* g_b0 = g_b0 for a rotation and a reflection at "
            "three rational points, exactly: %s; (b) delta* w = (1/2) L_(w^#) g_b0, the Christoffel-free formula "
            "(Kerr-Schild inverse checked), at the same points: %s; (c) the hand value (delta* dt)_00 = -mu^2/r^5 = "
            "-1/108 at x = (1, 2, 2, 0): %s (computed %s); (d) delta* of the Killing 1-forms g(d_t, .) and "
            "g(x^1 d_2 - x^2 d_1, .) vanishes there: %s" % (out["nat"], out["lie"], out["hand"], out["hand_val"],
                                                             out["kill"]))
    return out


Q4_C3 = ["of every type $\\tau\\in\\mathcal T$", "are taken as $\\delta^*_{g_{b_0}}$ of the averaged 1-forms",
         "as a map of all of $\\mathcal V_1$"]
WORDS = {"none": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
         "nine": 9, "ten": 10}
COUNTS = re.compile(r"(\d+) use only the site's conditions, (\d+) only name the object, (\d+) name another object spelt "
                    r"the same, (none|\d+) uses? more")


def q4(rows, text=None, show=True):
    """Part VII as printed: (C3) carries the amendment; the counts Lemma 3.1 and (VII5) print are the table's"""
    t = text if text is not None else open(os.path.join(V.P5, "PART-VII-ASSEMBLY.md"), encoding="utf-8").read()
    c3 = paragraph("PART-VII-ASSEMBLY.md", "C3", t)
    have = [" ".join(ph.split()) in c3 for ph in Q4_C3]
    pars = [" ".join(p.split()) for p in re.split(r"\n\s*\n", t)]
    lem = [p for p in pars if "a literal census finds" in p]
    vii5 = [p for p in pars if p.startswith("(VII5)")]
    n_lem = [int(x) for x in re.findall(r"(\d+) lines", lem[0])] if len(lem) == 1 else []
    n_v5 = [int(x) for x in re.findall(r"(\d+) lines", vii5[0])] if len(vii5) == 1 else []
    cnt = COUNTS.findall(vii5[0]) if len(vii5) == 1 else []
    und = re.findall(r"([A-Za-z]+|\d+) were undecided", vii5[0]) if len(vii5) == 1 else []
    count = {v: sum(r["verdict"] == v for r in rows) for v in VERDICTS}
    want = (len(rows), count["SITE-ONLY"], count["NAMING"], count["HOMONYM"], count["MORE"], count["UNDECIDED"])
    got = None
    if n_lem and n_v5 and cnt and und:
        s_, n_, h_, m_ = cnt[-1]
        u_ = und[-1].lower()
        got = (n_v5[-1], int(s_), int(n_), int(h_), WORDS.get(m_, None) if not m_.isdigit() else int(m_),
               WORDS.get(u_) if not u_.isdigit() else int(u_))
    ok = all(have) and got == want and bool(n_lem) and n_lem[-1] == len(rows)
    if show:
        say("  Q4: Part VII's (C3) prints the amendment's phrases %s: %s; Lemma 3.1 states %s lines and (VII5) %s "
            "(lines, site-only, naming, homonym, more, undecided), the table %s: %s"
            % ([ph[:24] + "..." for ph in Q4_C3], have, n_lem[-1] if n_lem else None, got, want,
               "agree" if ok else "DISAGREE"))
    return ok


def reverted_vii():
    """Part VII with Lemma 3.1's (C3) reverted to a stub (the amendment deleted), for the controls"""
    t = open(os.path.join(V.P5, "PART-VII-ASSEMBLY.md"), encoding="utf-8").read()
    pars = re.split(r"(\n\s*\n)", t)
    i = [k for k, par in enumerate(pars) if par.lstrip().startswith("(C3)")]
    assert len(i) == 1
    pars[i[0]] = "(C3) *Linear maps given by existence statements:* the solution operators (reverted)."
    return "".join(pars)


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
    emptied = [dict(r) for r in rows]       # every resolution replaced by "x" (an independent reader's mutation)
    for r in emptied:
        if r["verdict"] in NEED_RES:
            r["resolution"] = "x"
    flipped = [dict(r) for r in rows]       # an UNDECIDED row turned MORE, its resolution kept
    for r in flipped:
        if r["verdict"] == "UNDECIDED":
            r["verdict"] = "MORE"
            break
    rev = {"PART-VII-ASSEMBLY.md": reverted_vii()}
    fails = [not q1(dropped, es, False), not q1(doubled, es, False), not q1(misspelt, es, False),
             not q2(unresolved, False), not q1(rows, entries(widen=True), False), not q2(emptied, False),
             not q2(rows, False, rev), not q4(rows, rev["PART-VII-ASSEMBLY.md"], False), not q4(flipped, None, False),
             not q4(dropped, None, False)]
    say("  control: dropped row fails %s; doubled row fails %s; misspelt verdict fails %s; resolution removed fails %s;"
        " census widened by chi_9 fails %s; resolutions replaced by 'x' fail Q2 %s; Part VII's (C3) reverted fails Q2"
        " %s and Q4 %s; an UNDECIDED row turned MORE (resolution kept) fails Q4 %s; a dropped row fails Q4 %s"
        % tuple(fails))
    return all(fails)


def main():
    rows = load()
    a = q1(rows, entries())
    b = q2(rows)
    f = q4(rows)
    c = control(rows)
    q = q3()
    d = q["nat"] and q["lie"] and q["hand"] and q["kill"]
    ce, cs = not q3("extra", False)["nat"], not q3("shear", False)["nat"]
    qn, qf = q3("nochr", False), q3("flip", False)
    cn = not qn["lie"] and not qn["hand"]
    cf = not qf["lie"] and not qf["hand"]
    e = ce and cs and cn and cf
    say("  Q3 control: delta* plus w (x)_s dx^1 fails (a) %s; a shear fails (a) %s; delta* without its Christoffel "
        "term fails (b) and (c) %s (hand value then %s); with the Christoffel sign flipped fails (b) and (c) %s (%s)"
        % (ce, cs, cn, qn["hand_val"], cf, qf["hand_val"]))
    print("Q1 %s; Q2 %s; Q3 %s; Q4 %s; control %s" % tuple(["PASS" if x else "FAIL" for x in (a, b, d, f)] +
                                                         ["behaves" if c and e else "MISBEHAVES"]), flush=True)
    return 0 if a and b and c and d and e and f else 1


if __name__ == "__main__":
    sys.exit(main())
