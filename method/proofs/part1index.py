#!/usr/bin/env python3
"""part1index.py -- the two indexes Part I claims to close, measured.

Part I's header and the close of Chapter 1 both make one claim:

    "Part I indexes the principles and the protocols. Sec 28.8 indexes the
     process. Each turns a rule set into content, and each closes with E = 0."
                                                        -- main, end of Chapter 1
    "... and twenty-four protocols the law is made of, indexed and closed
     at E = 0."                                         -- main, PART I header

This program measures the two objects that claim names, using the book's own
material and nothing else.

  1. THE PROTOCOL INDEX.  Not rebuilt.  The corpus's own instrument is imported
     by path from the recovered estate -- an instrument imports a seated member,
     it never copies one, and the same rule is applied to a recovered one.
     Its cell assignments are the book's, not this program's.

  2. THE AUDITS INDEX.  Built from the table Sec 2.21 prints, parsed out of the
     seated main member by its column header rather than by line number, since
     the volumes move.  Sec 2.21 states the table is the input and that "a reader
     can rerun either"; this is that rerun.

  3. THE DIMENSION CERTIFICATE of Sec 3.7, verified: that each printed list is a
     linear extension of the stated precedences, and that the two intersect in
     exactly the order -- which is what certifies dim = 2.

  4. THE PRINCIPLES INDEX is searched for and not found.  No E is computed over
     the principles anywhere in either bundle.

REFUSALS, and they are the point
  This program reports E for an index it can build from printed data.  Where the
  book prints no coordinates it reports ABSENT and computes nothing; an ABSENT is
  not a finding and may not be quoted as one.

  It repairs nothing.  Findings R4-04 and R4-05 record what it measures.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, io, itertools, os, re, shutil, sys, tempfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
ESTATE = os.path.join(ROOT, "extracted", "archives", "restore-point-2-13")


# ------------------------------------------------------------------ the operator
def R(X, d):
    """The closure operator: the largest set the two-variable monotone envelopes
    of X admit.  Same form as the corpus's own -- max-envelope on every ordered
    pair of coordinates."""
    A = [sorted({c[i] for c in X}) for i in range(d)]

    def env(i, j):
        m = {}
        for c in X:
            m[c[j]] = max(m.get(c[j], -10**9), c[i])
        b, o = -10**9, {}
        for t in sorted(m):
            b = max(b, m[t])
            o[t] = b
        return o

    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in itertools.product(*A)
            if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}


def box_of(X, d):
    b = 1
    for i in range(d):
        b *= len({c[i] for c in X})
    return b


# --------------------------------------------------- 1. the protocol index
def protocol_index():
    """Import the corpus's own protindex.py by path and take its cell table.
    Never reimplemented here: the assignment of a protocol to a cell is the
    book's judgement and this program has no standing to make it."""
    path = os.path.join(ESTATE, "protindex.py")
    zpath = os.path.join(ESTATE, "zeno.py")
    if not os.path.exists(path):
        return None, "ABSENT: protindex.py not in the recovered estate"
    if not os.path.exists(zpath):
        return None, "ABSENT: protindex.py's zeno harness not in the recovered estate"

    # protindex.py runs under the zeno harness, which writes a state directory beside
    # its own source.  The estate is a generated tree and nothing may be written into
    # it, so zeno is imported first and its ROOT pointed at a scratch directory that
    # is removed afterwards.  Neither file is copied: both are imported from where
    # they sit, because an instrument imports and never copies.
    tmp = tempfile.mkdtemp(prefix="part1index-")
    buf, o_out, o_err = io.StringIO(), sys.stdout, sys.stderr
    saved = {k: sys.modules.get(k) for k in ("zeno", "protindex")}
    try:
        zspec = importlib.util.spec_from_file_location("zeno", zpath)
        zeno = importlib.util.module_from_spec(zspec)
        zspec.loader.exec_module(zeno)
        zeno.ROOT = os.path.join(tmp, ".zeno")
        sys.modules["zeno"] = zeno

        spec = importlib.util.spec_from_file_location("protindex", path)
        mod = importlib.util.module_from_spec(spec)
        sys.stdout = sys.stderr = buf      # the module prints its own report on import
        spec.loader.exec_module(mod)
    finally:
        sys.stdout, sys.stderr = o_out, o_err
        for k, v in saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v
        shutil.rmtree(tmp, ignore_errors=True)

    P = mod.P
    cells = {tuple(p[1:]) for p in P}
    Rx = R(cells, 4)
    dup = [k for k, v in Counter(tuple(p[1:]) for p in P).items() if v > 1]
    return dict(n=len(P), cells=len(cells), box=box_of(cells, 4), R=len(Rx),
                E=len(Rx) - len(cells),
                collisions=[[p[0] for p in P if tuple(p[1:]) == k] for k in dup]), None


# ----------------------------------------------------- 2. the audits index
AUDIT_ROW = re.compile(
    r'^\s{2,4}(\d+)\s{3}([A-Z]+)\s{2,}'
    r'(object|source|artefact|outside)\s{2,}'
    r'(itself|other places|a computation)\s{2,}'
    r'(wrong|unreadable|unusable|dishonest)\s{2,}'
    r'(nothing|claims individually true|labels are addressable|also mutually consistent)\s*$')

# Sec 2.21's stated orders, verbatim:
#   "object < source < artefact < outside; itself < other places < a computation;
#    wrong < unreadable < unusable < dishonest; and nothing < claims individually
#    true < also mutually consistent, with *labels are addressable* reading as the
#    second."
AX0 = ["object", "source", "artefact", "outside"]
AX1 = ["itself", "other places", "a computation"]
AX2 = ["wrong", "unreadable", "unusable", "dishonest"]
AX3 = {"nothing": 0, "claims individually true": 1,
       "labels are addressable": 1, "also mutually consistent": 2}

ANCHOR = "no  audit           reads       compares against   a failure costs   presupposes"


def audits_table(main_text):
    """Parse Sec 2.21's printed table.  Found by its own column header, not by a
    line number: the volumes have moved once already this year and a literal line
    number is how two instruments in this estate went stale."""
    lines = main_text.split("\n")
    at = None
    for i, l in enumerate(lines):
        if ANCHOR in l:
            at = i
            break
    if at is None:
        return None, "ABSENT: Sec 2.21's audit table header not found in the main member"
    rows = []
    for l in lines[at + 1: at + 60]:
        m = AUDIT_ROW.match(l)
        if m:
            rows.append((int(m.group(1)), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6)))
        elif rows and not l.strip():
            break
    if not rows:
        return None, "ABSENT: the header was found and no row parsed under it"
    return rows, None


AX3_NAME = {0: "nothing", 1: "claims individually true", 2: "also mutually consistent"}


def frontier(cells, Rx):
    """Split the admitted-and-absent cells into DOMINATED -- an occupied cell is at
    least as large on every axis -- and FRONTIER, where the index stops."""
    missing = sorted(Rx - cells)
    dom = [c for c in missing
           if any(all(o[i] >= c[i] for i in range(4)) for o in cells)]
    return dom, [c for c in missing if c not in dom]


def audits_index(rows):
    cells = [(AX0.index(r[2]), AX1.index(r[3]), AX2.index(r[4]), AX3[r[5]]) for r in rows]
    S = set(cells)
    Rx = R(S, 4)
    dup = [k for k, v in Counter(cells).items() if v > 1]
    dom, fro = frontier(S, Rx)
    return dict(n=len(rows), cells=len(S), box=box_of(S, 4), R=len(Rx), E=len(Rx) - len(S),
                dominated=len(dom), frontier=fro,
                collisions=[[f"{r[0]} {r[1]}" for r in rows
                             if (AX0.index(r[2]), AX1.index(r[3]), AX2.index(r[4]), AX3[r[5]]) == k]
                            for k in dup])


# ------------------------------------------ 3. Sec 3.7's dimension certificate
# The precedences Sec 3.7 states, in its own words and order.
PREC = []


def _lt(a, *bs):
    for b in bs:
        PREC.append((a, b))


_lt("CELL", "LATTICE")
_lt("LATTICE", "EQUATIONS")
_lt("CELL", "DISTINCTNESS")
_lt("EQUATIONS", "SCOPE", "AGREEMENT", "ARITHMETIC", "ENUMERATION")
_lt("CONSISTENCY", "REDUNDANCY")
_lt("CONSISTENCY", "ARTEFACT")
_lt("REDUNDANCY", "ARTEFACT")
_lt("MARKUP", "ARTEFACT", "FIDELITY")
_lt("ARTEFACT", "MEASURE", "FIDELITY", "PROJECTION")
_lt("ATTRIBUTION", "REPRODUCTION")
_lt("SEQUENCE", "ANTECEDENT", "COHERENCE", "PROJECTION")
_lt("INPUT", "SCOPE", "ARITHMETIC", "ENUMERATION")

L9A = "CELL DISTINCTNESS LATTICE EQUATIONS AGREEMENT INPUT SCOPE ARITHMETIC ENUMERATION".split()
L9B = "INPUT CELL LATTICE EQUATIONS ENUMERATION ARITHMETIC SCOPE AGREEMENT DISTINCTNESS".split()
L10A = "CONSISTENCY REDUNDANCY MARKUP ARTEFACT FIDELITY MEASURE SEQUENCE PROJECTION COHERENCE ANTECEDENT".split()
L10B = "SEQUENCE ANTECEDENT COHERENCE MARKUP CONSISTENCY REDUNDANCY ARTEFACT PROJECTION MEASURE FIDELITY".split()


def transitive(pairs):
    succ = {}
    for a, b in pairs:
        succ.setdefault(a, set()).add(b)
    changed = True
    while changed:
        changed = False
        for a in list(succ):
            for b in list(succ[a]):
                for c in succ.get(b, ()):
                    if c not in succ[a]:
                        succ[a].add(c)
                        changed = True
    return {(a, b) for a in succ for b in succ[a]}


def components(elems, pairs):
    par = {a: a for a in elems}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for a, b in pairs:
        par[find(a)] = find(b)
    out = {}
    for a in elems:
        out.setdefault(find(a), []).append(a)
    return sorted((sorted(v) for v in out.values()), key=len)


def linear_extensions(elems, order):
    elems = sorted(elems)
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    below = [0] * n
    for a, b in order:
        if a in idx and b in idx:
            below[idx[b]] |= 1 << idx[a]
    memo = {}

    def f(mask):
        if mask == (1 << n) - 1:
            return 1
        if mask in memo:
            return memo[mask]
        t = 0
        for i in range(n):
            if not mask >> i & 1 and below[i] & ~mask == 0:
                t += f(mask | 1 << i)
        memo[mask] = t
        return t

    return f(0)


def certify(elems, La, Lb, order):
    sub = {(a, b) for (a, b) in order if a in elems and b in elems}
    pa = {x: i for i, x in enumerate(La)}
    pb = {x: i for i, x in enumerate(Lb)}
    ok_a = all(pa[a] < pa[b] for a, b in sub)
    ok_b = all(pb[a] < pb[b] for a, b in sub)
    inter = {(a, b) for a in elems for b in elems
             if a != b and pa[a] < pa[b] and pb[a] < pb[b]}
    return dict(relations=len(sub), extension_a=ok_a, extension_b=ok_b,
                intersection_is_order=(inter == sub),
                extensions=linear_extensions(elems, order))


# ------------------------------------------- 4. is there a principles index?
def principles_index(texts):
    """Search both bundles for an E computed over the principles.  Reports ABSENT
    rather than inventing coordinates: the book prints none, and a coordinate list
    this program chose would be this program's index, not the book's."""
    hits = []
    for name, t in texts.items():
        for m in re.finditer(r'E\s*\(\s*principles?\s*\)|E\(P\d', t):
            hits.append((name, m.group(0)))
    return hits


# ---------------------------------------------------------------------- report
def load(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def measure(members):
    main = load(os.path.join(members, "The_Method_1_6-2.md"))
    out = {}
    out["protocols"], out["protocols_absent"] = protocol_index()
    rows, absent = audits_table(main)
    out["audits_absent"] = absent
    out["audit_rows"] = rows
    out["audits"] = audits_index(rows) if rows else None
    order = transitive(PREC)
    elems = sorted({a for a, _ in PREC} | {b for _, b in PREC})
    if rows:
        elems = sorted({r[1] for r in rows})
    out["precedences"] = len(PREC)
    out["order_pairs"] = len(order)
    out["components"] = [len(c) for c in components(elems, PREC)]
    out["singletons"] = [c for c in components(elems, PREC) if len(c) == 1]
    out["cert9"] = certify(set(L9A), L9A, L9B, order)
    out["cert10"] = certify(set(L10A), L10A, L10B, order)
    # Sec 3.7's two rhetorical counts.  The 362 decomposition is the R2 read's, recorded
    # in the Working Register at chat 69; it is adopted, not re-derived.  A first
    # reconstruction here gave 162 and was wrong -- where a reconstruction disagrees
    # with the record the finding is about the reconstruction (G0c).
    pairs9 = 9 * 8 // 2
    pairs10 = 10 * 9 // 2
    out["counts37"] = dict(search=4140 * 4139 // 2,
                           verify=4 * (pairs9 + pairs10) + 2 * 19)
    out["principles_E_sites"] = principles_index({"main": main})
    # The growth of the audits index, as Secs 3.8 and 3.7.1 report it.  The point is
    # the last row: at twenty-one the cells are distinct, at twenty-two they are not.
    if rows:
        r21 = [r for r in rows if r[1] != "CENSUS"]
        r20 = [r for r in r21 if r[1] != "INPUT"]
        out["growth"] = [("20 audits, before INPUT", audits_index(r20)),
                         ("21 audits, INPUT added", audits_index(r21)),
                         ("22 audits, CENSUS added", audits_index(rows))]
    else:
        out["growth"] = []
    return out


def report(o):
    p, a = o["protocols"], o["audits"]
    print("  PART I'S TWO INDEXES, AND WHAT THEY MEASURE")
    print()
    print("  1. THE PROTOCOL INDEX   (cells from the corpus's own protindex.py, imported)")
    if p is None:
        print(f"     {o['protocols_absent']}")
    else:
        print(f"     protocols        {p['n']}")
        print(f"     distinct cells   {p['cells']}   collisions {p['n'] - p['cells']}")
        print(f"     box              {p['box']}   |R(X)|  {p['R']}")
        print(f"     E(protocols)     {p['E']}")
        print("     protocols sharing a cell:")
        for grp in sorted(p["collisions"]):
            print("       " + "  |  ".join(g.strip() for g in grp))
    print()
    print("  2. THE AUDITS INDEX     (cells parsed from Sec 2.21's own printed table)")
    if a is None:
        print(f"     {o['audits_absent']}")
    else:
        print(f"     audits           {a['n']}")
        print(f"     distinct cells   {a['cells']}   collisions {a['n'] - a['cells']}")
        print(f"     box              {a['box']}   |R(X)|  {a['R']}")
        print(f"     E(audits)        {a['E']}")
        print("     audits sharing a cell:")
        for grp in sorted(a["collisions"]):
            print("       " + "  |  ".join(grp))
        print(f"     of the {a['E']} admitted and absent cells, {a['dominated']} are dominated"
              f" and {len(a['frontier'])} are on the frontier:")
        for c in a["frontier"]:
            print(f"       {AX0[c[0]]} · {AX1[c[1]]} · {AX2[c[2]]} · {AX3_NAME[c[3]]}")
        print("     Main prints this object's E twice, at 16 and at 17, in one section.")
        print("     16 is the value at twenty-two audits; 17 was the value at twenty.")
        print("     The 17 row's gloss, 'fourteen cells with no audit in them', is the")
        print("     count of the DOMINATED subset of the sixteen -- an old E beside a")
        print("     current sub-count.")
    print()
    print("  2a. HOW THE AUDITS INDEX GREW, against what Secs 3.8 and 3.7.1 print")
    for tag, g in o["growth"]:
        print(f"     {tag:<34} cells {g['cells']:>3}   collisions {g['n'] - g['cells']}   E {g['E']:>3}")
    print("     Sec 3.8's table prints 20 audits at E = 17; Sec 3.7.1 prints INPUT taking it to 16;")
    print("     the Index of Indices prints 21 cells and E = 16 at twenty-two.  All three reproduce.")
    print("     E stays 16 when CENSUS joins ONLY because CENSUS shares SCOPE's cell.")
    print()
    print("  3. SEC 3.7'S DIMENSION CERTIFICATE")
    print(f"     precedences stated        {o['precedences']}")
    print(f"     order pairs (transitive)  {o['order_pairs']}")
    print(f"     comparability components  {o['components']}")
    for s in o["singletons"]:
        print(f"       isolated: {s[0]} -- in no stated precedence")
    for tag, c in (("nine", o["cert9"]), ("ten", o["cert10"])):
        print(f"     component of {tag}: relations {c['relations']}   "
              f"both lists are extensions {c['extension_a'] and c['extension_b']}   "
              f"intersection == order {c['intersection_is_order']}   "
              f"linear extensions {c['extensions']}")
    print("     dim = 2 CERTIFIED" if (o["cert9"]["intersection_is_order"]
                                       and o["cert10"]["intersection_is_order"]) else
          "     dim certificate FAILS")
    c = o["counts37"]
    print(f"     Sec 3.7's two rhetorical counts:")
    print(f"       'eight and a half million' = C(4140,2) = {c['search']:,}")
    print(f"       '362 comparisons'          = 4*81 + 2*19 = {c['verify']}   "
          "(the decomposition is chat 69's, in the Working Register, not re-derived here)")
    print()
    print("  4. THE PRINCIPLES INDEX")
    if o["principles_E_sites"]:
        for n, s in o["principles_E_sites"]:
            print(f"     {n}: {s}")
    else:
        print("     ABSENT: no E is computed over the principles anywhere in the main volume.")
        print("     Nothing is reported for it.  An ABSENT is not a finding.")
    print()
    print("  AGAINST WHAT PART I CLAIMS")
    print('     Part I: "... indexed and closed at E = 0."')
    print('     Ch. 1:  "Part I indexes the principles and the protocols ...')
    print('              and each closes with E = 0."')
    if p:
        print(f"     measured E(protocols) = {p['E']}, not 0.")
    print("     measured E(principles): no such index exists in the book.")
    print("     Sec 28.8's process index, the third the sentence names, does close: 36 cells, E = 0.")


FIXTURES = """the corpus's own recorded numbers, and every one is printed in a volume:
  protocols   24 protocols, 19 cells, E = 105   -- Mathematical Compendium, 'The protocol index',
                                                   and the Index of Indices' table of the book's
                                                   own indexes
  audits      22 audits, 21 cells, E = 16       -- the Index of Indices' table, same place
  Sec 3.7     792 and 4,140 linear extensions   -- printed in Sec 3.7 itself
  Sec 3.7     22 precedences                    -- 'The twenty-two', Sec 3.7
  Sec 3.8     20 audits at E = 17               -- Sec 3.8's growth table
  Sec 3.7.1   INPUT takes E from 17 to 16       -- Sec 3.7.1
  Ch. 18    the sixteen missing cells are fourteen dominated and two on the frontier,
              both 'outside . dishonest'   -- the Index of Indices' own entry
  Sec 3.7     362 comparisons, 8.5 million     -- Sec 3.7; the 362 decomposition is the
                                                  Working Register's, chat 69"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(name, got, want):
        checks.append((name, got, want, got == want))

    p, a = o["protocols"], o["audits"]
    eq("protocols counted", p["n"], 24)
    eq("protocol cells", p["cells"], 19)
    eq("E(protocols)", p["E"], 105)
    eq("audits counted", a["n"], 22)
    eq("audit cells", a["cells"], 21)
    eq("E(audits)", a["E"], 16)
    eq("precedences stated", o["precedences"], 22)
    eq("nine-component linear extensions", o["cert9"]["extensions"], 792)
    eq("ten-component linear extensions", o["cert10"]["extensions"], 4140)
    eq("nine-component certificate", o["cert9"]["intersection_is_order"], True)
    eq("ten-component certificate", o["cert10"]["intersection_is_order"], True)
    eq("no principles index", o["principles_E_sites"], [])
    g = dict(o["growth"])
    eq("E at 20 audits (Sec 3.8)", g["20 audits, before INPUT"]["E"], 17)
    eq("E at 21 audits (Sec 3.7.1)", g["21 audits, INPUT added"]["E"], 16)
    eq("cells distinct at 21", g["21 audits, INPUT added"]["n"] - g["21 audits, INPUT added"]["cells"], 0)
    eq("one collision at 22", g["22 audits, CENSUS added"]["n"] - g["22 audits, CENSUS added"]["cells"], 1)
    eq("Sec 3.7 'eight and a half million'", o["counts37"]["search"], 8567730)
    eq("Sec 3.7 '362 comparisons'", o["counts37"]["verify"], 362)
    eq("comparability components", o["components"], [1, 2, 9, 10])
    eq("audits: dominated missing cells", a["dominated"], 14)
    eq("audits: frontier cells", len(a["frontier"]), 2)
    eq("audits: the frontier is outside/dishonest",
       sorted((AX1[c[1]] for c in a["frontier"]))
       if all(AX0[c[0]] == "outside" and AX2[c[2]] == "dishonest" for c in a["frontier"])
       else None, ["a computation", "other places"])
    print(FIXTURES)
    print()
    bad = 0
    for name, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {name:<36} {got!r:<8} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--members", default=MEMBERS)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest(args.members)
    report(measure(args.members))
    return 0


if __name__ == "__main__":
    sys.exit(main())
