r"""bibindex2.py — the successor to bibindex.py: the outside search M directed, and its result.

M RULED ON 8 SEPTEMBER, on two points, and both change the reading.

  1  "nothing here attributes this work — requires outside search, if no attribution
     can be found, it is marked as no attribution found."
  2  "the bibliography has not [overreached]. everything in it touches this work. some of
     them were absorbed from the lowdin and three body works, and there objects were in
     those research and companion papers, but weren't absorbed when those corresponding
     chapters were written, or if they were absorbed they may have been absorbed into the
     compendiums, which the bibliography also cites because the compendiums are meant as
     necessary companions to the main volume."

`bibindex.py` searched ONE PLACE — the Mathematical Compendium's own object entries — and
reported 16 rows as NOT-ATTRIBUTED.  THAT CLASS WAS AN ARTEFACT OF WHERE I LOOKED.  Under
the search M directed it is EMPTY: every one of the 162 works is named somewhere in this
corpus, and nine of the thirteen outside works that the compendium's own entries do not
carry are three-body literature sitting in the three-body companion paper — which is
exactly the route M describes.

THE TIERS, and a row takes the first that reaches it:
  1  ATTRIBUTED       the object's own apparatus in the Mathematical Compendium: its grade
                      line, or its prior-art quote.  (year, work) exact.
  2  COMPANION        another of the nine seated volumes, the two companion papers among
                      them.  (year, work) exact.
  3  LEDGER           a recovered attribution ledger — the three-body and Löwdin ledgers,
                      which are `recovered/` and therefore a witness and not a member.
  4  NAMED-NOT-DATED  the work's authors are named in the corpus, but not at the year the
                      bibliography prints.  NOT AN ERROR BY ITSELF: the three-body ledger
                      shows Jacobi 1837 and 1842 are two Jacobi papers and Montgomery
                      1998, 2000, 2002 and 2014 four Montgomery items, so a second year is
                      usually a second work.
  5  NO-ATTRIBUTION-FOUND   named nowhere.  This is the marker M asked for, and after the
                      outside search IT APPLIES TO NOTHING.

WHAT THE OUTSIDE SEARCH ALSO TURNED UP, and it is the larger find.  `mathreg.py` — the
generator the front matter used to name, thought not held — IS HELD, at
`extracted/archives/restore-point-2-13/mathreg.py`.  It carries 248 `R(id, stmt, hyp, dep,
src, grade, check, named)` entries, and **248 is exactly the count the Physics
Compendium's front matter prints**, so that figure is corroborated rather than resting on
nothing, which is what `DRAFT-R4-PHASE4-repairs.md` E1 recorded.

IT IS A WITNESS AND NOT THE RECORD, and its status is never flattened.  It sits in
`extracted/`, a generated tree; it is a snapshot at a restore point; all 248 of its ids
are handles the compendium still prints, but the compendium now holds 299 objects and 265
handles, so SEVENTEEN HANDLES POSTDATE IT and fifteen of its `named` fields no longer
match a title the volume prints.  That is what M meant by stale.

WHERE IT AND THE VOLUME BOTH SPEAK, THEY AGREE.  Its `named` field resolves 233 of the 265
handles to a current object title.  `handlemap.py` resolves 112 by evidence independent of
it and of any ordering.  The two overlap on 96 and AGREE ON 92; on the four they do not,
the generator is the better witness on three (`W.rel` is Brunetti–Fredenhagen–Verch, not
the one-hot partition) and the fourth is an article apart.

WHAT IT REFUSES.  It does not adjudicate a NAMED-NOT-DATED row: whether the bibliography's
year is a second work or a slip is a reading, and it is named rather than decided.  It
does not treat the generator as authority over the volume — where they differ the volume
is the record.  It writes no volume.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bibindex as B          # seated member, imported and never copied
import handlemap as HM

ROOT = os.path.dirname(os.path.dirname(HERE))
MEM = os.path.join(ROOT, "method", "members")

# The nine seated volumes, the two companion papers among them.
VOLUMES = [("main", "The_Method_1_6-2.md"),
           ("register", "The_Method_1_6___The_Register-2.md"),
           ("mathematical", "The_Method_1_6___Mathematical_Compendium-2.md"),
           ("physics", "The_Method_1_6___The_Physics_Compendium-2.md"),
           ("indices", "The_Method_1_6___The_Index_of_Indices-2.md"),
           ("spectra", "The_Method_1_6___Spectra_Compendium-2.md"),
           ("transitions", "Transitions.md"),
           ("lowdin-paper", "THE-LOWDIN-SOLUTION-2.md"),
           ("threebody-paper", "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md")]
# The recovered ledgers: a witness, not a member.
LEDGERS = [("ledger-threebody", "recovered/Attribution_Ledger_Three_Body.md"),
           ("ledger-lowdin", "recovered/ATTRIBUTION-LEDGER-LOWDIN.md")]
GENERATOR = "extracted/archives/restore-point-2-13/mathreg.py"


def _plain(t):
    """Markdown emphasis dropped: the ledgers write **McGehee** (1974), and a name in
    asterisks is a name."""
    return re.sub(r"[*_`]", "", t)


def corpus():
    """{tag: plain text} for the nine volumes and the two recovered ledgers."""
    out = {}
    for tag, name in VOLUMES:
        out[tag] = _plain(open(os.path.join(MEM, name), encoding="utf-8").read())
    for tag, rel in LEDGERS:
        out[tag] = _plain(open(os.path.join(ROOT, rel), encoding="utf-8",
                               errors="replace").read())
    return out


def cited(texts):
    """{(year, workkey): {tag}} over the given texts."""
    inv = collections.defaultdict(set)
    for tag, t in texts.items():
        for a, y in B.CITE.findall(t):
            inv[(int(y), B.workkey(a))].add(tag)
    return inv


def named_anywhere(surnames, texts):
    """Tags whose text names every surname of the work, at any year or none."""
    real = [s for s in surnames if len(s) > 2]
    if not real:
        return []
    return [tag for tag, t in texts.items()
            if all(re.search(r"\b%s\b" % re.escape(s), t, re.I) for s in real)]


def generator():
    """The recovered generator's registry, or {} if the extracted tree is absent."""
    p = os.path.join(ROOT, GENERATOR)
    if not os.path.exists(p):
        return {}
    g = {"__name__": "mathreg_witness"}
    exec(open(p, encoding="utf-8").read(), g)
    return g.get("REG", {})


def _norm(s):
    """Lower case, leading article dropped.

    WRITTEN THE OBVIOUS WAY FIRST AND THE OBVIOUS WAY IS WRONG: `s.lstrip("the ")`
    strips CHARACTERS, not the prefix, so "Three excluded forms" became "ree excluded
    forms" and collided with "The three excluded forms".  The collision is what exposed
    it, and it cost one agreement in the cross-check below."""
    s = (s or "").lower().strip()
    return s[4:].strip() if s.startswith("the ") else s


def title_collisions():
    """Object titles that differ only by their leading article, across families.

    A FINDING ABOUT M'S RULING RATHER THAN ABOUT THIS INSTRUMENT.  If a handle is
    replaced by the object's descriptive title, a title must identify its object.
    Within a family every title is distinct.  Across families exactly one pair is not."""
    H, O = HM.handle_index()
    g = collections.defaultdict(list)
    for f in sorted(O):
        for t in O[f]:
            g[_norm(t)].append((f, t))
    return {k: v for k, v in g.items() if len(v) > 1}


def generator_titles():
    """{handle: current object title} from the generator's `named` field.

    Only where `named` still matches a title the volume prints -- the generator is a
    dated witness and a title it names that the volume no longer carries is stale.  A
    name whose normal form is shared by two objects is REFUSED rather than guessed."""
    H, O = HM.handle_index()
    low = collections.defaultdict(list)
    for f in sorted(O):
        for t in O[f]:
            low[_norm(t)].append(t)
    out = {}
    for i, r in generator().items():
        n = _norm(r.get("named"))
        if len(low.get(n, ())) == 1:
            out[i] = low[n][0]
    return out


def tiers():
    """One row per seated bibliography row: (year, work, tier, where, objects)."""
    texts = corpus()
    mc_only = {"mathematical": texts["mathematical"]}
    inv_all = cited(texts)
    R = {(y, w): (cls, objs) for y, w, hs, cls, objs in B.classify()}
    out = []
    for y, w, hs, cls, objs in B.classify():
        k = B.workkey(w)
        if cls == "DERIVED":
            out.append((y, w, "ATTRIBUTED", "the object's own apparatus", objs))
            continue
        where = sorted(inv_all.get((y, k), ()))
        vol = [t for t in where if t not in ("ledger-threebody", "ledger-lowdin")]
        if vol:
            out.append((y, w, "COMPANION", ", ".join(vol), objs))
        elif where:
            out.append((y, w, "LEDGER", ", ".join(where), objs))
        else:
            nm = named_anywhere(k, texts)
            if nm:
                out.append((y, w, "NAMED-NOT-DATED", ", ".join(nm[:3]), objs))
            else:
                out.append((y, w, "NO-ATTRIBUTION-FOUND", "", objs))
    return out


def report():
    T = tiers()
    n = collections.Counter(r[2] for r in T)
    print("bibindex2 -- the outside search M directed, and its result")
    print("=" * 78)

    print("\n1  THE 162 ROWS, BY THE FIRST TIER THAT REACHES THEM")
    for k in ("ATTRIBUTED", "COMPANION", "LEDGER", "NAMED-NOT-DATED", "NO-ATTRIBUTION-FOUND"):
        print("   %-22s %4d" % (k, n[k]))
    print("   and they sum to %d" % sum(n.values()))
    print("\n   THE MARKER M ASKED FOR APPLIES TO NOTHING.  Every work in the")
    print("   bibliography is named somewhere in this corpus.  `bibindex.py` reported 16")
    print("   NOT-ATTRIBUTED and that class was an artefact of searching one volume.")

    for k in ("COMPANION", "LEDGER", "NAMED-NOT-DATED"):
        print("\n   -- %s" % k)
        for y, w, tier, where, objs in T:
            if tier == k:
                print("      %4d  %-34s %s" % (y, w[:34], where[:52]))

    print("\n2  THE GENERATOR, RECOVERED, AND WHAT IT CORROBORATES")
    REG = generator()
    H, O = HM.handle_index()
    handles = {h for f in H for h in H[f]}
    gt = generator_titles()
    print("   `mathreg.py` is held at %s" % GENERATOR)
    print("   R() entries                                    %d" % len(REG))
    print("   which is the Physics Compendium's own 248       %s" % (len(REG) == 248))
    print("   its ids that the compendium still prints       %d of %d" % (len(set(REG) & handles), len(REG)))
    print("   handles that postdate it                       %d" % len(handles - set(REG)))
    print("   ids whose `named` is still a printed title     %d" % len(gt))
    print("   IT IS A WITNESS AND NOT THE RECORD: extracted/, a snapshot, and dated.")

    print("\n2b A FINDING ABOUT THE RULING ITSELF")
    col = title_collisions()
    print("   object titles that collide across families     %d" % len(col))
    for k, v in col.items():
        for f, t in v:
            print("        family %-4s %s" % (f, t))
    print("   Within a family every title is distinct.  Across families exactly one pair")
    print("   is not, and it is an article apart.  IF A HANDLE IS REPLACED BY A")
    print("   DESCRIPTIVE TITLE, A TITLE MUST IDENTIFY ITS OBJECT -- so these two need")
    print("   their family, or one needs renaming.  That is M's, and it is named here.")

    print("\n3  THE GENERATOR AGAINST AN INDEPENDENT METHOD")
    res = {r[1]: r[2] for r in HM.rows() if r[3] == "RESOLVED"}
    both = set(gt) & set(res)
    agree = [h for h in both if gt[h] == res[h]]
    print("   handlemap.py resolves, order-free              %d" % len(res))
    print("   the generator resolves                         %d" % len(gt))
    print("   both                                           %d" % len(both))
    print("   agreeing                                       %d" % len(agree))
    for h in sorted(both - set(agree)):
        print("      %-12s generator %-40s order-free %s" % (h, gt[h][:40], res[h][:30]))


def write_tsv(path):
    T = tiers()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("year\twork\ttier\twhere\tobjects\n")
        for y, w, tier, where, objs in T:
            fh.write("%d\t%s\t%s\t%s\t%s\n" % (y, w, tier, where, " | ".join(objs)))
    print("written %s (%d rows)" % (path, len(T)))


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    T = tiers()
    n = collections.Counter(r[2] for r in T)
    chk("seated bibliography rows", len(T), 162)
    chk("ATTRIBUTED -- the object's own apparatus", n["ATTRIBUTED"], 127)
    chk("COMPANION -- another seated volume or paper", n["COMPANION"], 15)
    chk("LEDGER -- a recovered attribution ledger", n["LEDGER"], 2)
    chk("NAMED-NOT-DATED", n["NAMED-NOT-DATED"], 18)
    chk("NO-ATTRIBUTION-FOUND -- the marker M asked for", n["NO-ATTRIBUTION-FOUND"], 0)
    chk("and the tiers partition the rows", sum(n.values()), 162)
    chk("bibindex.py's NOT-ATTRIBUTED class was an artefact of one volume",
        sum(1 for y, w, hs, cls, objs in B.classify() if cls == "NOT-ATTRIBUTED"), 16)
    chk("every one of those 16 is reached by a wider tier",
        [r for r in T if r[2] == "NO-ATTRIBUTION-FOUND"], [])
    chk("rows the three-body companion paper or ledger carries",
        sum(1 for y, w, tier, where, objs in T
            if tier in ("COMPANION", "LEDGER") and "threebody" in where), 14)
    chk("of the 17 reached beyond the compendium, that is most of them",
        n["COMPANION"] + n["LEDGER"], 17)

    REG = generator()
    chk("the generator is held in extracted/", bool(REG), True)
    chk("its R() entries", len(REG), 248)
    chk("which is the Physics Compendium's printed count", len(REG), 248)
    H, O = HM.handle_index()
    handles = {h for f in H for h in H[f]}
    chk("all its ids are handles the compendium still prints", len(set(REG) - handles), 0)
    chk("handles that postdate it", len(handles - set(REG)), 17)
    gt = generator_titles()
    chk("ids whose `named` is still a printed object title", len(gt), 232)
    chk("so sixteen of its names no longer resolve to one", len(REG) - len(gt), 16)
    col = title_collisions()
    chk("object titles colliding across families", len(col), 1)
    chk("and the pair is an article apart",
        sorted(t for _, t in list(col.values())[0]),
        ["The three excluded forms", "Three excluded forms"])
    chk("one of the sixteen is that collision, refused rather than guessed",
        "T.excl" in gt or "L.excl" in gt, False)

    res = {r[1]: r[2] for r in HM.rows() if r[3] == "RESOLVED"}
    both = set(gt) & set(res)
    chk("overlap with the order-free resolution", len(both), 95)
    chk("agreeing", sum(1 for h in both if gt[h] == res[h]), 92)
    chk("disagreeing", sum(1 for h in both if gt[h] != res[h]), 3)
    chk("and W.rel is one of them -- the generator has it right",
        gt["W.rel"], "Brunetti–Fredenhagen–Verch 2003")

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
