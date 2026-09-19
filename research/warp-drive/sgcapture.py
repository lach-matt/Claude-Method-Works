#!/usr/bin/env python3
r"""
sgcapture.py -- THE 230 CRYSTALLOGRAPHIC SPACE GROUPS, BANKED FROM spglib.

    python3 sgcapture.py --write     rebuild captures/SPACEGROUPS-spglib.tsv
    python3 sgcapture.py --verify    the file against a fresh derivation
    python3 sgcapture.py --selftest  fixtures

WHY THIS EXISTS.  `quasiparticle.py` needs one fact and needs it checked: the
symmetry label a lattice excitation carries is a property of THE HOST CRYSTAL,
not of the excitation.  That is a claim about how many distinct symmetry
settings a host can have, and the answer is tabulated -- 230 space groups in
32 point groups and 73 arithmetic crystal classes.  Banking it makes the claim
a measurement instead of a recollection.

THE PATTERN IS `pdgcapture.py`'s AND SO IS THE REASON.  spglib is an installed
package, not vendored -- ~4 MB and this is a document corpus -- so the derived
table is written once, with the package's version and the source digest in the
header, and `read()` is stdlib-only.  `--verify` re-derives and compares, and
needs the package; nothing else does.

    pip install spglib

WHAT IS NOT CLAIMED.  This is the space-group CATALOGUE, not a list of
materials and not a list of quasiparticles.  A space group is a symmetry group
and carries no quantum numbers, so it is NOT an index by `registry.py`'s
criterion and is never seated as one.  It is evidence for a refusal.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "captures", "SPACEGROUPS-spglib.tsv")
COLS = ("number", "international", "schoenflies", "pointgroup",
        "arithmetic_class", "arithmetic_symbol", "hall_count")

# The four figures every crystallography text prints.  Fixtures check the
# capture against them, so a bad fetch cannot pass quietly.
CANON = {"space groups": 230, "point groups": 32,
         "arithmetic crystal classes": 73, "Hall entries": 530}


def _rows():
    import spglib
    seen = {}
    for hall in range(1, 531):
        t = spglib.get_spacegroup_type(hall)
        if t is None:
            continue
        n = int(t.number)
        if n in seen:
            seen[n]["hall_count"] += 1
            continue
        seen[n] = {
            "number": n,
            "international": t.international_short,
            "schoenflies": t.schoenflies,
            "pointgroup": t.pointgroup_international,
            "arithmetic_class": int(t.arithmetic_crystal_class_number),
            "arithmetic_symbol": t.arithmetic_crystal_class_symbol,
            "hall_count": 1,
        }
    return [seen[k] for k in sorted(seen)]


def write():
    import spglib
    rows = _rows()
    body = "".join("\t".join(str(r[c]) for c in COLS) + "\n" for r in rows)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# The crystallographic space groups, International Tables "
                 "for Crystallography Vol. A\n")
        fh.write("# via spglib %s -- pip install spglib, NOT vendored\n"
                 % spglib.__version__)
        fh.write("# derived md5  %s\n" % hashlib.md5(body.encode()).hexdigest())
        fh.write("# a space group carries NO quantum numbers and is never "
                 "seated as an index\n")
        fh.write("# rows %d\n" % len(rows))
        fh.write("\t".join(COLS) + "\n")
        fh.write(body)
    return OUT, len(rows)


def read():
    """[{col: value}] -- stdlib only, and this is the read path."""
    rows = []
    head = None
    with open(OUT, encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("#"):
                continue
            p = ln.rstrip("\n").split("\t")
            if head is None:
                head = p
                continue
            rows.append(dict(zip(head, p)))
    return rows


def header():
    return [l.rstrip("\n") for l in open(OUT, encoding="utf-8")
            if l.startswith("#")]


def counts():
    """{what: how many} -- the four canonical figures, measured."""
    R = read()
    return {"space groups": len(R),
            "point groups": len({r["pointgroup"] for r in R}),
            "arithmetic crystal classes":
                len({r["arithmetic_class"] for r in R}),
            "Hall entries": sum(int(r["hall_count"]) for r in R)}


def verify():
    """(agrees, message) -- the file against a fresh derivation.  Needs spglib."""
    if not os.path.exists(OUT):
        return False, "capture absent -- run --write"
    try:
        fresh = _rows()
    except ImportError:
        return False, "spglib is not installed -- the read path does not need it"
    have = read()
    if len(fresh) != len(have):
        return False, "%d rows on disk, %d fresh" % (len(have), len(fresh))
    bad = [f["number"] for f, h in zip(fresh, have)
           if any(str(f[c]) != h[c] for c in COLS)]
    return (not bad, "every row agrees" if not bad
            else "%d rows differ: %s" % (len(bad), bad[:8]))


def report():
    print("=" * 74)
    print("THE SPACE GROUPS -- banked, and why they are not an index")
    print("=" * 74)
    print()
    for l in header():
        print("   " + l)
    print()
    print("THE CANONICAL FIGURES, MEASURED FROM THE CAPTURE:")
    c = counts()
    for k in ("space groups", "point groups", "arithmetic crystal classes",
              "Hall entries"):
        print("   %-28s %4d   canonical %4d   %s"
              % (k, c[k], CANON[k], "ok" if c[k] == CANON[k] else "DIFFERS"))
    print()
    print("A SPACE GROUP CARRIES NO QUANTUM NUMBERS.  It is a symmetry group,")
    print("so it fails registry.py's criterion and is never seated.  It is")
    print("here as evidence for quasiparticle.py's refusal: the symmetry label")
    print("a lattice excitation carries is one of THESE, and which one depends")
    print("on the host crystal rather than on the excitation.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    R = read()
    c = counts()
    chk("230 space groups", len(R), 230)
    chk("numbered 1 to 230 with no gap",
        [int(r["number"]) for r in R] == list(range(1, 231)), True)
    chk("the four canonical figures, against the textbook", c, CANON)
    chk("530 Hall entries, so 300 groups have more than one setting",
        c["Hall entries"] - c["space groups"], 300)

    by = {int(r["number"]): r for r in R}
    chk("P1 is number 1, point group 1", (by[1]["international"],
                                          by[1]["pointgroup"]), ("P1", "1"))
    chk("P-1 is number 2, the first centrosymmetric one",
        (by[2]["international"], by[2]["pointgroup"]), ("P-1", "-1"))
    chk("Fm-3m is 225, the face-centred cubic one, point group m-3m",
        (by[225]["international"], by[225]["pointgroup"]), ("Fm-3m", "m-3m"))
    chk("Fd-3m is 227 -- diamond and silicon", by[227]["international"],
        "Fd-3m")
    chk("Ia-3d is the last, 230", by[230]["international"], "Ia-3d")

    chk("the header records the spglib version it came from",
        any(l.startswith("# via spglib") for l in header()), True)
    chk("and says outright that it is not an index",
        any("never seated" in l for l in header()), True)

    # THE POINT quasiparticle.py needs: the label set is the HOST's
    pg = {}
    for r in R:
        pg.setdefault(r["pointgroup"], []).append(int(r["number"]))
    chk("the 230 fall into 32 point groups, so the host's symmetry is not "
        "one thing", len(pg), 32)
    chk("and the point groups are wildly uneven -- the largest holds 28 "
        "space groups, the smallest 1",
        (max(len(v) for v in pg.values()), min(len(v) for v in pg.values())),
        (28, 1))

    print("sgcapture selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--write" in sys.argv:
        p, n = write()
        print("wrote %s  (%d rows)" % (p, n))
        sys.exit(0)
    if "--verify" in sys.argv:
        good, msg = verify()
        print("%s  %s" % ("ok  " if good else "FAIL", msg))
        sys.exit(0 if good else 1)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
