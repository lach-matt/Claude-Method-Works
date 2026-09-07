"""Register 1176's agreement theorem, and the counterexample staged as 1797.

WHAT 1176 STATES

    "E(X) = 0 IF AND ONLY IF THE LANGUAGES AGREE.  Six indexes, three operators
     -- order, statistics and geometry -- and the agreement tracks closure
     without exception."

WHAT THE STAGED ENTRY STATES

    the grading (status, verification, precedent) over the 77 elements of
    dclose.py holds 11 cells of a 16-cell box, every one of the five
    operator-bearing languages admits the same 13, and E = 2.

    So the languages agree in the strongest sense the method has -- identical
    admitted sets -- while E is not zero.  The "if" half is untouched; the
    "only if" half has a counterexample, and it is one of the book's own objects.

The entry was staged by the cypher-audit queue, its siblings 1793-1796 were
seated, and it was not; 1797 has stood as a hole in the Register ever since, with
1796 and 1798 both seated and no EXCISED marker covering it, which Ruling 27 does
not allow.  M ruled on 7 September 2026 that it seats at the next free number.
This program is what it is seated on.

THE ORDER IS DECLARED, NOT INFERRED, AND THAT IS THE WHOLE CARE OF IT.  R depends
on the value order of each coordinate, and cypher.py warns when it has to fall
back to lexicographic.  All three coordinates here are ordinal by construction --
withdrawn < conjectured < measured < verified < proved; cited < sampled <
exhaustive; none found < found -- so the order is declared and the run carries no
fallback warning.  A reading that rested on alphabetical order would be an
artefact of the labels.

INPUT
  method/members/dclose.py -- the seated instrument, read for its own element
  lists; 65 + 12 = 77, which its own run prints.
  tools/cypher.py -- imported by path for R and the other operators; the
  operator is never reimplemented here.

REFUSALS
  It does not repair 1176.  The entry is a correction that cites it; a Register
  entry is never edited.

  It does not claim the "if" half fails.  Only the converse is tested, and the
  program says which half it is on every line it prints.

  It reports `documentary` and `analysis` as the special rows they are and counts
  neither among the five: documentary returns a citation rather than a binary,
  and analysis is declared-only.  That is register 1173's division as the corpus
  measured it, not a choice made here.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, itertools, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEM = os.path.join(ROOT, "method", "members")
TOOLS = os.path.join(ROOT, "tools")

# The three coordinates, ordinal by construction -- dclose.py's own dictionaries.
STATUS = ["withdrawn", "conjectured", "measured", "verified", "proved"]
VERIF = ["cited", "sampled", "exhaustive"]
PREC = ["none found", "found"]
FIVE = ["order", "algebra", "geometry", "information", "statistics"]
SPECIAL = {"documentary": "returns a citation, not a binary",
           "analysis": "declared-only; returns a magnitude, not a cell decision"}


def load_cypher():
    spec = importlib.util.spec_from_file_location("cypher", os.path.join(TOOLS, "cypher.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules["cypher"] = m
    spec.loader.exec_module(m)
    return m


def elements():
    """dclose.py's own element lists, read from the seated member rather than retyped."""
    src = open(os.path.join(MEM, "dclose.py"), encoding="utf-8").read()
    out = []
    for name in ("E65", "NEW"):
        m = re.search(r'%s="""(.*?)"""' % name, src, re.S)
        assert m, "dclose.py: %s not found" % name
        rows = [l for l in m.group(1).strip().split("\n") if l.strip()]
        out.append(rows)
    return out


def gradings(rows):
    """The (status, verification, precedent) cell of each element, as labels."""
    return [tuple(x.strip() for x in l.split("|")[2].split("·")) for l in rows]


def index_of(cy, cells):
    return cy.Index("dclose gradings", ["status", "verification", "precedent"], cells,
                    value_order={"status": STATUS, "verification": VERIF, "precedent": PREC})


def admitted(cy, ix):
    """Each language's admitted set, and the note when it is silent."""
    out = {}
    for name, (op, _, _) in cy.ADMISSION.items():
        got, note = op(ix, {})
        out[name] = (got, note)
    return out


def report():
    cy = load_cypher()
    e65, new = elements()
    allrows = e65 + new
    cells = gradings(allrows)
    ix = index_of(cy, cells)

    print("REGISTER 1176's AGREEMENT THEOREM, AND THE COUNTEREXAMPLE STAGED AS 1797")
    print()
    print("THE OBJECT")
    print("  dclose.py's own element lists : %d + %d = %d" % (len(e65), len(new), len(allrows)))
    print("  coordinates                   : status, verification, precedent")
    print("  values observed on each axis  : %s" % [len(a) for a in ix.alphabets])
    print("  so the box is                 : %d cells" % ix.box)
    print("  distinct gradings held        : %d" % len(ix.cells))
    lex = [w for w in ix.warnings if "lexicographic" in w]
    print("  value order declared, so no lexicographic fallback: %s" % (not lex))
    print("  the run's only warning        : %s" % (ix.warnings or "none"))
    print()

    A = admitted(cy, ix)
    print("WHAT EACH LANGUAGE ADMITS")
    sets = {}
    for name in FIVE:
        got, note = A[name]
        if got is None:
            print("  %-14s SILENT -- %s" % (name, note))
        else:
            sets[name] = frozenset(got)
            print("  %-14s admits %d" % (name, len(got)))
    for name, why in SPECIAL.items():
        got = A.get(name, (None, ""))[0]
        print("  %-14s special row: %s%s" % (name, why,
              "" if got is None else " (admits %d)" % len(got)))
    print()

    print("THE TEST")
    same = len(set(sets.values())) == 1
    n = len(next(iter(sets.values()))) if sets else 0
    print("  the five operator-bearing languages return IDENTICAL sets: %s" % same)
    print("  each admits                                             : %d" % n)
    print("  the index holds                                         : %d" % len(ix.cells))
    print("  so E = admitted - held                                  : %d" % (n - len(ix.cells)))
    print()
    missing = sorted(set(next(iter(sets.values()))) - set(ix.cells))
    print("  the cells R admits and the index lacks:")
    for c in missing:
        print("    %s" % " · ".join(ix.decode[i][v] for i, v in enumerate(c)))
    print()
    print("  Each is a grading a mathematical object could carry, and neither occurs")
    print("  among the %d.  So the languages agree in the strongest sense available" % len(allrows))
    print("  -- identical admitted sets -- and E is not zero.")
    print()

    print("WHICH HALF OF 1176 THIS TOUCHES")
    print("  the 'if' half   -- E = 0 implies agreement          : NOT TESTED HERE, untouched")
    print("  the 'only if'   -- agreement implies E = 0          : REFUTED by this object")
    print()

    print("THE OTHER TWO READINGS OF THE SAME ELEMENTS, NEITHER A DEFECT")
    print("  with kind and discipline on axes the object is wide open -- register 1356's")
    print("  fault, not a finding here.")
    fib = {}
    for l, c in zip(allrows, cells):
        fib.setdefault(l.split("|")[0], []).append(c)
    closed = 0
    for k, cs in fib.items():
        jx = index_of(cy, cs)
        got, _ = cy.ADMISSION["order"][0](jx, {}) if jx.d >= 2 else (None, "")
        if got is not None and len(got) == len(jx.cells):
            closed += 1
    print("  fibres by kind·discipline                : %d" % len(fib))
    print("  fibres closing at E = 0 under R          : %d" % closed)
    print("  which is dclose.py's own '24 fibres, E: 0' for the 77.")
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    cy = load_cypher()
    e65, new = elements()
    allrows = e65 + new
    chk("dclose.py's first list", len(e65), 65)
    chk("its second", len(new), 12)
    chk("so the object is the 77 the entry names", len(allrows), 77)

    # The operator is the corpus's own, and it must return the book's printed E = 36
    # for the periodic table before it is trusted on anything else.
    px = cy._periodic()
    pg, _ = cy.ADMISSION["order"][0](px, {})
    chk("R returns the book's printed E = 36 for the periodic table",
        len(pg) - len(px.cells), 36)

    cells = gradings(allrows)
    ix = index_of(cy, cells)
    chk("no lexicographic fallback: the order is declared",
        [w for w in ix.warnings if "lexicographic" in w], [])
    # The one warning it does carry is the duplicate collapse, and it is arithmetic:
    # 77 elements over 11 distinct gradings.
    chk("the only warning is the duplicate collapse", ix.warnings,
        ["%d duplicate cells collapsed" % (len(allrows) - 11)])
    chk("values observed per axis", [len(a) for a in ix.alphabets], [4, 2, 2])
    chk("so the box is sixteen cells", ix.box, 16)
    chk("and eleven of them are held", len(ix.cells), 11)

    A = admitted(cy, ix)
    sets = {}
    for name in FIVE:
        got, note = A[name]
        assert got is not None, "%s went silent: %s" % (name, note)
        sets[name] = frozenset(got)
    chk("all five operator-bearing languages return one set", len(set(sets.values())), 1)
    n = len(sets["order"])
    chk("and each admits thirteen", n, 13)
    chk("so E = 13 - 11 = 2", n - len(ix.cells), 2)
    chk("E is not zero, which is the counterexample", (n - len(ix.cells)) != 0, True)

    missing = sorted(set(sets["order"]) - set(ix.cells))
    lab = [" · ".join(ix.decode[i][v] for i, v in enumerate(c)) for c in missing]
    chk("the two cells the index lacks", sorted(lab),
        ["measured · exhaustive · found", "verified · sampled · found"])

    # The special rows, per register 1173 as the corpus measured it.
    chk("documentary is a special row and not one of the five",
        "documentary" in cy.ADMISSION and "documentary" not in FIVE, True)
    chk("analysis is declared-only, so not an admission operator at all",
        "analysis" in cy.DECLARED_ONLY and "analysis" not in cy.ADMISSION, True)
    chk("five operator-bearing languages", len(FIVE), 5)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
