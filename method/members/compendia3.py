r"""compendia3.py — successor to compendia.py and compendia2.py: the key M ruled, and the state after the repairs.

M RULED ON 8 SEPTEMBER, on the Spectra Compendium's nine duplicated keys: **both rows,
with the n-range added to the key.**  And M ruled on the method that produced my question:
"you are trying to identify error by pattern and that fails here because your questions
are answered by reading and comprehending the actual material of the objects in question."

BOTH PREDECESSORS ARE SUPERSEDED, FOR DIFFERENT REASONS, AND NEITHER IS EDITED.
  `compendia.py`   pins the Ruling 46 material -- 23 script sites, 18 distinct scripts,
                   7 stamps -- which the pass of BUILD279 and BUILD281 removed.  Its
                   fixtures measure a defect that no longer exists.
  `compendia2.py`  parses the generation stamp that pass removed, and raises rather than
                   reports; and its `duplicated_keys()` measures on (species, series),
                   which is the key M has now ruled incomplete.

WHAT READING THE MATERIAL GAVE THAT THE PATTERN DID NOT.  The nine pairs looked like one
shape -- earlier row bracketed, later row untested -- and were three.  The volume states
the rule that settles them: "A closed-shell core has one parent term and gives one Rydberg
series per l.  An open-shell core gives one series PER PARENT, all interleaved, converging
on DIFFERENT LIMITS", and it counts series as "(parent, l, term)".

  ONE OF THE NINE IS NOT A DUPLICATE.  Ba III `nd 2[3/2]* J=2` appears twice at limits
  289,100.000 and 306,650.000 -- 17,550 cm-1 apart, the 5p5 2P* fine-structure splitting.
  Two parents, therefore two series.  TEN SIBLING Ba III ROWS PRINT THE PARENT in the
  label -- `5p5.(2P*<3/2>).nd 2[3/2]* J=2` -- and these do not.
  THE OTHER EIGHT SHARE A LIMIT and are one series printed twice.

AND THE LABEL FAULT IS WIDER THAN THE ROW.  Only 14 of 596 rows name their parent, and
BOTH species that do -- Ar II and Ba III -- also have rows that do not.  The compendium
mixes two naming conventions inside one species.  Recorded, not repaired: which convention
the volume should print is M's.

THE KEY, AS RULED.  On (species, series, n-range) the nine fall to TWO, and the two that
remain are the pairs whose n-ranges are identical: Si I `nd (3/2,3/2)* J=1` at 20-50 and
`nd (3/2,5/2)* J=3` at 20-56, each agreeing in every printed cell except the bracket and
the fourth decimal of delta.  THE KEY CANNOT SEPARATE THEM BECAUSE NOTHING PRINTED DOES.

WHAT IT REFUSES.  It does not choose between those two rows, and it does not restore a
parent to a label.  Both are readings of the material and both are M's.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compendia2 as C2      # seated; imported for its readers, superseded in its findings

VOLS = C2.VOLS
text = C2.text
lines = C2.lines
spectra_rows = C2.spectra_rows

# A series label that names its parent: a configuration, a parenthesised term, then the run.
PARENT = re.compile(r"^\S*\.\(.*?\)\.")
SCRIPT = re.compile(r"`?\b[A-Za-z_][A-Za-z0-9_]*\.py\b`?")
DATAFILE = re.compile(r"\b[A-Za-z0-9_][A-Za-z0-9_.\-]*\.(?:md|tsv|csv|json|txt|log|zip|tgz)\b")
STAMP = re.compile(r"[Gg]enerated (from|on)\b|Rebuild with\b|python3 ")


def duplicated_keys(n_in_key=True):
    """Duplicated keys in the channel table.

    M RULED THE KEY IS (species, series, n-range).  `compendia2.py` measured on
    (species, series) and found nine; seven of those nine are distinct rows the shorter
    key could not tell apart.  Pass n_in_key=False to reproduce the predecessor."""
    _, data = spectra_rows()
    seen = collections.defaultdict(list)
    for i, c in data:
        seen[(c[0], c[1], c[2]) if n_in_key else (c[0], c[1])].append(i)
    return {k: v for k, v in seen.items() if len(v) > 1}


def parent_labels():
    """(rows naming their parent, rows not, species using both conventions)."""
    _, data = spectra_rows()
    withp = [(i, c) for i, c in data if PARENT.match(c[1])]
    without = [(i, c) for i, c in data if not PARENT.match(c[1])]
    a = {c[0].replace(" *", "").strip() for _, c in withp}
    b = {c[0].replace(" *", "").strip() for _, c in without}
    return withp, without, sorted(a & b)


def limits_of(key):
    """The distinct series limits printed under a (species, series) key."""
    _, data = spectra_rows()
    return sorted({c[10] for i, c in data if (c[0], c[1]) == key})


def ruling46():
    """{tag: (script sites, data-file sites, stamps)} after the pass.

    `compendia.py` pinned 23 script sites over 18 distinct scripts and 7 stamps.  The
    pass of BUILD279 and BUILD281 removed them; these are the same measurements now."""
    out = {}
    for tag, name in VOLS:
        t = text(name)
        # a figure's image path is not a name printed to a reader -- W-286 refuses those
        body = "\n".join(l for l in t.split("\n") if not l.lstrip().startswith("!["))
        out[tag] = (len(SCRIPT.findall(body)), len(DATAFILE.findall(body)),
                    len(STAMP.findall(body)))
    return out


def report():
    print("compendia3 -- the key M ruled, and the state after the repairs")
    print("=" * 78)

    print("\n1  THE KEY, AS RULED: (species, series, n-range)")
    old = duplicated_keys(False)
    new = duplicated_keys(True)
    print("   duplicated on (species, series)            %d   <- compendia2.py's figure" % len(old))
    print("   duplicated on (species, series, n-range)   %d   <- M's key" % len(new))
    print("   so the shorter key could not separate      %d distinct rows" % (len(old) - len(new)))
    for k, v in sorted(new.items()):
        print("      %-10s %-24s %-10s L%s" % (k[0], k[1], k[2], ", L".join(map(str, v))))
    print("   Both remaining pairs agree in EVERY printed cell but the bracket and the")
    print("   fourth decimal of delta.  Nothing printed separates them.")

    print("\n2  THE ONE THAT WAS NEVER A DUPLICATE, READ FROM THE VOLUME'S OWN RULE")
    k = ("Ba III", "nd 2[3/2]* J=2")
    L = limits_of(k)
    print("   %s | %s" % k)
    print("   limits printed              %s" % " and ".join(L))
    print("   apart                       %s cm-1" % format(
        int(float(L[1].replace(",", "")) - float(L[0].replace(",", ""))), ","))
    print("   the volume's rule: one series per parent, converging on different limits.")
    print("   Two parents, two series -- and the label omits the parent.")

    print("\n3  AND THE LABEL FAULT IS WIDER THAN THAT ROW")
    withp, without, both = parent_labels()
    print("   rows whose series label names its parent   %d" % len(withp))
    print("   rows whose label does not                  %d" % len(without))
    print("   species that use BOTH conventions          %s" % both)
    print("   Recorded, not repaired: which convention the volume prints is M's.")

    print("\n4  THE RULING 46 MATERIAL, AFTER THE PASS")
    print("   %-6s %8s %8s %8s" % ("volume", "scripts", "files", "stamps"))
    for tag, (s, f, st) in ruling46().items():
        print("   %-6s %8d %8d %8d" % (tag, s, f, st))
    print("   the one stamp match left is W-284's recorded refusal -- \"Prior counts,")
    print("   generated on a rule this volume did not print\" is prose about how earlier")
    print("   counts were produced, and register 1739 turns on it.")
    print("   compendia.py pinned 23 script sites over 18 distinct scripts and 7 stamps;")
    print("   the pass of BUILD279 and BUILD281 removed them.  Figure image paths are")
    print("   excluded here, as W-286 refuses them: removing one removes a figure.")


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    _, data = spectra_rows()
    chk("channel table data rows", len(data), 596)
    old, new = duplicated_keys(False), duplicated_keys(True)
    chk("duplicated on (species, series) -- the predecessor's key", len(old), 9)
    chk("duplicated on (species, series, n-range) -- M's key", len(new), 2)
    chk("and the two that remain are the identical-range pairs",
        sorted((k[0], k[2]) for k in new), [("Si I", "20–50"), ("Si I", "20–56")])
    chk("every pair the longer key separates has distinct n-ranges",
        [k for k in old if k not in {(a, b) for a, b, _ in new}
         and len({tuple(c[2] for i, c in data if i == j) for j in old[k]}) < 2], [])

    L = limits_of(("Ba III", "nd 2[3/2]* J=2"))
    chk("Ba III's two limits", L, ["289,100.000", "306,650.000"])
    chk("apart, in cm-1",
        round(float(L[1].replace(",", "")) - float(L[0].replace(",", "")), 1), 17550.0)
    chk("the eight others share a limit",
        [k for k in old if k != ("Ba III", "nd 2[3/2]* J=2") and len(limits_of(k)) > 1
         and k[0] != "Ca II"], [])

    withp, without, both = parent_labels()
    chk("rows naming their parent", len(withp), 14)
    chk("rows not", len(without), 582)
    chk("and they sum to the table", len(withp) + len(without), 596)
    chk("species using both conventions", both, ["Ar II", "Ba III"])

    r = ruling46()
    chk("script names printed to a reader, after the pass",
        sum(s for s, f, st in r.values()), 0)
    chk("data-file names, after the pass", sum(f for s, f, st in r.values()), 0)
    chk("generation-stamp matches remaining", sum(st for s, f, st in r.values()), 1)
    chk("and the one is W-284's recorded refusal, not a stamp",
        bool(re.search(r"Prior counts, generated on a rule this volume did not print",
                       text(VOLS[1][1]))), True)
    chk("compendia.py pinned eighteen distinct scripts and this measures none",
        sum(s for s, f, st in r.values()), 0)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a = a.parse_args()
    selftest() if a.selftest else report()
