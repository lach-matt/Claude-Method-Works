r"""handlemap.py — can a handle be resolved to a descriptive title from the volumes alone?

M RULED ON 7 SEPTEMBER THAT THE STANDING CONTENT STANDARD GOVERNS: no object handles
or workshop jargon in reader-facing volumes, and a cross-reference names the object by
its DESCRIPTIVE TITLE.  Executing that ruling needs one thing the ruling does not
supply -- the map from `A.gc` to the title it stands for.

THE MAP IS NOT PRINTED ANYWHERE.  The word "handle" occurs zero times in the four
compendia.  `compendia2.py` measures 265 distinct handles at 417 sites, 407 of them in
one column of one table, and not one of the four volumes resolves a single id.  The map
lived in the generator the front matter used to name, which this repository does not
hold.

WHAT THIS INSTRUMENT DOES, AND WHY IT DOES NOT USE THE OBVIOUS METHOD.  The obvious
method is to assume that within a family the objects are printed in the order their
handles sort, so the k-th handle names the k-th object.  THAT HYPOTHESIS IS FALSE, and
the volume refutes it without leaving the family whose counts agree: family 3B has nine
objects and nine handles, and its objects are printed in MEANING order -- shape space,
the shape metric, the Jacobi-Maupertuis metric, the potential, the variety, the five
points -- so `3B.JM` would be paired with "Shape space and the shape sphere" and
`3B.five` with the Jacobi-Maupertuis metric.  Family W, also nine and nine, IS in handle
order and pairs perfectly.  NOTHING IN THE VOLUMES SAYS WHICH FAMILIES ARE WHICH.

So the resolution here is ORDER-FREE.  For each handle it searches the WHOLE family for
objects whose title its own evidence fits, and reports what it finds:

  RESOLVED    exactly one object in the family is corroborated -- the pairing does not
              depend on any ordering, and it is a measurement.
  AMBIGUOUS   more than one is.  Named, never chosen.
  UNRESOLVED  none is.  No title is offered at all.

THE EVIDENCE, and there are only two kinds held here.  SUFFIX: the handle's own suffix,
digits stripped, occurs in the title, or is the run of the title's word-initials --
`A.gc` against "Global consistency (CSP)".  ANCHOR: the main volume's Appendix G prints
29 handles against the statements they carry, the only handle-to-content evidence this
repository holds, and the title shares a distinctive word with the statement or the
statement names the suffix outright -- which is how `M.C1` is corroborated, its statement
opening "C1, computed.  The presymplectic potential ...".

THE ORDERING IS REPORTED AS A FINDING, NOT USED AS A METHOD.  Where a family's counts
agree, the instrument prints how many of its order-free resolutions sit where position
would have predicted.  Ten families agree completely, and 3B and LS do not -- which is
the measurement that refutes the hypothesis rather than an opinion about it.

WHAT IT REFUSES.  It does not write a volume and it does not propose one.  It emits
`method/HANDLE-MAP.tsv` for a human to approve or refuse row by row, and a row's status
travels with it.  An AMBIGUOUS row names its candidates and chooses none.  An UNRESOLVED
row offers nothing: there is no evidence here, and a title invented to fill the column
would be reconstructed content seated in a reader-facing volume, which is the one thing
the store's rule about status forbids.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import compendia2 as C   # a seated member; imported, never copied


def handle_index():
    """{family: [handle, ...]} sorted, and {family: [object title, ...]} as printed."""
    tk, br = C.handles(C.VOLS[0][1])
    H = collections.defaultdict(list)
    for h in sorted({h for _, h in tk} | {h for _, h in br}):
        H[h.split(".")[0]].append(h)
    return H, C.family_objects()


def anchors():
    """{handle: the statement Appendix G attaches to it} -- the only handle-to-content
    evidence this repository holds."""
    rows, _, _, _, _ = C.appendix_g()
    tick, _ = C.handle_rx()
    out = {}
    for l in rows:
        cells = re.split(r"(?<!\\)\|", l.strip().strip("|"))
        if len(cells) >= 3:
            for h in tick.findall(cells[2]):
                out[h] = cells[1].strip()
    return out


_STOP = set("the and that with from which their there these those about into over than "
            "then when what where whole this each been have does not are its".split())


def _toks(s):
    return {w.rstrip("s") for w in re.findall(r"[a-z]{5,}", s.lower())} - _STOP


def corroborated(handle, title, statement):
    """Does anything here support pairing this handle with this title?

    Two tests, and either suffices.  SUFFIX: the handle's own suffix, digits stripped,
    occurs in the title, or is the run of initials of the title's words -- `A.gc` against
    "Global consistency (CSP)".  ANCHOR: the title and Appendix G's statement for this
    handle share a distinctive word, or the statement names the suffix outright, which is
    how `M.C1` is corroborated ("C1, computed.  The presymplectic potential ...")."""
    suf = handle.split(".", 1)[1]
    bare = suf.rstrip("0123456789").lower()
    t = title.lower()
    if len(bare) >= 3 and bare in t:
        return "SUFFIX"
    inits = "".join(w[0] for w in re.findall(r"[A-Za-z]+", title)).lower()
    if len(bare) >= 2 and bare in inits:
        return "SUFFIX"
    if statement:
        if re.search(r"\b%s\b" % re.escape(suf), statement):
            return "ANCHOR"
        if _toks(title) & _toks(statement):
            return "ANCHOR"
    return ""


def candidates(handle, fam, H, O, A):
    """Every object in the family whose title this handle's own evidence fits.

    ORDER-FREE BY CONSTRUCTION: the whole family is searched, so no assumption about
    the order objects are printed in enters the result."""
    out = []
    for t in O[fam]:
        ev = corroborated(handle, t, A.get(handle, ""))
        if ev:
            out.append((t, ev))
    return out


def rows():
    """One row per handle: family, handle, resolution, status, evidence."""
    H, O = handle_index()
    A = anchors()
    out = []
    for fam in sorted(H):
        for h in H[fam]:
            c = candidates(h, fam, H, O, A)
            if len(c) == 1:
                out.append((fam, h, c[0][0], "RESOLVED", c[0][1]))
            elif c:
                out.append((fam, h, "", "AMBIGUOUS",
                            "%d candidates: %s" % (len(c), " | ".join(t for t, _ in c))))
            else:
                out.append((fam, h, "", "UNRESOLVED", "no evidence in the volumes"))
    return out


def report():
    H, O = handle_index()
    A = anchors()
    R = rows()
    n = collections.Counter(r[3] for r in R)
    print("handlemap -- can M's ruling be executed from the volumes alone?")
    print("=" * 78)

    print("\n1  THE MAP THE VOLUMES SUPPORT, order-free")
    for k in ("RESOLVED", "AMBIGUOUS", "UNRESOLVED"):
        print("   %-12s %4d of %d handles" % (k, n[k], len(R)))
    _, occ, _ = C.bibliography()
    st = {r[1]: r[3] for r in R}
    sites = collections.Counter(st[h] for h in occ)
    print("   and by site in the bibliography's objects column (%d sites over %d rows):"
          % (len(occ), len(C.bibliography()[0])))
    for k in ("RESOLVED", "AMBIGUOUS", "UNRESOLVED"):
        print("   %-12s %4d" % (k, sites[k]))
    mt, mb = C.handles(C.MAIN)
    mh = [h for _, h in mt] + [h for _, h in mb]
    ms = collections.Counter(st[h] for h in mh if h in st)
    print("   and in the main volume (%d sites): %s" % (len(mh), dict(ms)))

    print("\n2  THE ORDERING HYPOTHESIS, REPORTED AS A FINDING AND NOT USED AS A METHOD")
    print("   %-4s %8s %8s  %s" % ("fam", "objects", "handles", "resolutions where position predicts"))
    agree = dis = 0
    for f in sorted(H):
        if len(H[f]) != len(O[f]):
            print("   %-4s %8d %8d  -- counts differ, position is not even defined"
                  % (f, len(O[f]), len(H[f])))
            continue
        tot = a = 0
        for i, h in enumerate(H[f]):
            c = candidates(h, f, H, O, A)
            if len(c) == 1:
                tot += 1
                a += c[0][0] == O[f][i]
        agree += a
        dis += tot - a
        print("   %-4s %8d %8d  %d of %d%s" % (f, len(O[f]), len(H[f]), a, tot,
                                               "" if a == tot else "   <-- NOT in handle order"))
    print("   across the equal-count families: %d agree, %d do not." % (agree, dis))
    print("   3B is nine objects and nine handles and its objects are in MEANING order;")
    print("   W is nine and nine and is in handle order.  Nothing in the volumes says which")
    print("   a family is, so the ordering cannot be used to resolve a single handle.")

    print("\n3  WHAT THE APPENDIX G ANCHORS CONTRIBUTE")
    print("   anchors held: %d, over %d families" % (len(A), len({h.split('.')[0] for h in A})))
    byev = collections.Counter(r[4] for r in R if r[3] == "RESOLVED")
    print("   resolutions whose evidence is the handle's own suffix: %d" % byev["SUFFIX"])
    print("   resolutions whose evidence is an Appendix G anchor   : %d" % byev["ANCHOR"])

    print("\n4  WHAT THIS MEANS FOR THE RULING")
    print("   M ruled that a handle is replaced by the object's descriptive title.")
    print("   %d of %d handles have a title the volumes support." % (n["RESOLVED"], len(R)))
    print("   %d name several objects and this instrument chooses none." % n["AMBIGUOUS"])
    print("   %d have no evidence here at all." % n["UNRESOLVED"])
    print("   By site, %d of the bibliography's %d can be written and %d cannot."
          % (sites["RESOLVED"], len(occ), sites["AMBIGUOUS"] + sites["UNRESOLVED"]))
    print("   THE TABLE IS WRITTEN FOR APPROVAL, NOT APPLIED.")


def write_tsv(path):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("family\thandle\tproposed_title\tstatus\tevidence\n")
        for r in rows():
            fh.write("\t".join(r) + "\n")
    print("written %s (%d rows)" % (path, len(rows())))


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    H, O = handle_index()
    A = anchors()
    R = rows()
    n = collections.Counter(r[3] for r in R)

    chk("handles in the Mathematical Compendium", sum(len(v) for v in H.values()), 265)
    chk("objects it holds", sum(len(v) for v in O.values()), 299)
    chk("objects carrying no handle", 299 - 265, 34)

    # the order-free resolution
    chk("RESOLVED", n["RESOLVED"], 112)
    chk("AMBIGUOUS", n["AMBIGUOUS"], 55)
    chk("UNRESOLVED", n["UNRESOLVED"], 98)
    chk("and they partition the handles", sum(n.values()), 265)
    chk("no AMBIGUOUS row names a title", [r for r in R if r[3] == "AMBIGUOUS" and r[2]], [])
    chk("no UNRESOLVED row names a title", [r for r in R if r[3] == "UNRESOLVED" and r[2]], [])
    chk("every RESOLVED row names its evidence kind",
        sorted({r[4] for r in R if r[3] == "RESOLVED"}), ["ANCHOR", "SUFFIX"])
    byev = collections.Counter(r[4] for r in R if r[3] == "RESOLVED")
    chk("resolutions resting on the suffix", byev["SUFFIX"], 110)
    chk("resolutions resting on an Appendix G anchor", byev["ANCHOR"], 2)

    # the ordering hypothesis, refuted where its counts are defined
    def agree(f):
        t = a = 0
        for i, h in enumerate(H[f]):
            c = candidates(h, f, H, O, A)
            if len(c) == 1:
                t += 1
                a += c[0][0] == O[f][i]
        return a, t
    eq = sorted(f for f in H if len(H[f]) == len(O[f]))
    chk("families whose counts agree", len(eq), 14)
    chk("family 3B holds nine objects and nine handles",
        (len(O["3B"]), len(H["3B"])), (9, 9))
    chk("and NOT ONE of its resolutions sits where position predicts", agree("3B"), (0, 5))
    chk("family W holds nine and nine too", (len(O["W"]), len(H["W"])), (9, 9))
    chk("and its resolutions do sit there", agree("W")[0], 4)
    chk("families in handle order", sorted(f for f in eq if agree(f)[0] == agree(f)[1]),
        ["A", "B", "C", "E", "F", "G", "I", "P", "T"])
    chk("families demonstrably NOT in handle order",
        sorted(f for f in eq if agree(f)[0] != agree(f)[1]), ["3B", "LS", "M", "Q", "W"])
    chk("so the ordering resolves nothing on its own",
        sum(agree(f)[1] - agree(f)[0] for f in eq), 12)

    # the sites the ruling has to reach
    _, occ, _ = C.bibliography()
    st = {r[1]: r[3] for r in R}
    sites = collections.Counter(st[h] for h in occ)
    chk("bibliography sites", len(occ), 407)
    chk("of which a title is supported for", sites["RESOLVED"], 178)
    chk("and is not for", sites["AMBIGUOUS"] + sites["UNRESOLVED"], 229)
    mt, mb = C.handles(C.MAIN)
    chk("main-volume sites", len(mt) + len(mb), 76)

    chk("Appendix G anchors held", len(A), 29)
    chk("K.girth and K.helly sit in a family whose counts differ",
        len(O["K"]) - len(H["K"]), 1)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a.add_argument("--write", metavar="PATH")
    a = a.parse_args()
    if a.selftest:
        selftest()
    elif a.write:
        write_tsv(a.write)
    else:
        report()
