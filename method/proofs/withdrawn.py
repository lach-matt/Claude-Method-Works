"""The twelve entries said to assert what a chat withdrew, tested one at a time.

THE CLASS AND WHERE IT CAME FROM.  DEF-153P-PENDING filed twelve Register entries
-- 230, 314, 500, 502, 599, 602, 807, 1148, 1450, 1461, 1595, 1628 -- as
"asserting what a chat withdrew", on the ground that each "carries no WITHDRAWN /
WARNING / REFUTED / SUPERSEDED marker in their first 1,500 characters"; 1395 was
listed apart because it does carry WARNING.  The branch called the class
circumstantial and said each entry needed reading in full before anything.

M ruled on 7 September 2026 that a chat transcript IS a source a repair may be
made from, provided the chat is reviewed exhaustively, and that findings are
recorded AND repaired.  This is the reading.

AND THE TEST THAT BUILT THE CLASS IS THE WRONG TEST.  The store's own governing
rule is that a Register entry is NEVER EDITED and the repair is a new appended
entry citing the superseded one.  An entry repaired correctly therefore carries no
marker inside itself -- the marker is a different entry, further down.  Looking for
a withdrawal marker in the first 1,500 characters of the entry finds nothing
exactly when the repair has been done properly.  So the class is measured here the
other way round: for each entry, is there a LATER SEATED ENTRY that cites it and
carries the correction's own distinguishing figure?

WHAT IS MEASURED
  1. The correction census: for each of the thirteen, the later entry that repairs
     it, found by citation AND by the correcting figure's own text, or none.
  2. The arithmetic of the unrepaired ones, where the chat's own correction can be
     checked without leaving this repository.
  3. Λ8 is the same object under both seated towers, which is what licenses the
     seed instrument to be run against either.

INPUT
  method/members/The_Method_1_6___The_Register-2.md -- read for every entry body.
  method/members/tower.py and tower-2.py -- imported by path, compared, never copied.

REFUSALS
  It does not re-derive the kappa refit.  Registers 497-500 and 502 were withdrawn
  on a comparison of GREEDY SET COVER against PRUNE-GREEDY over thirteen bases, and
  that refit -- coefficient -0.079, rms 0.999, against register 500's slope 0.2506
  and rms 0.62 -- is not reproducible from anything this repository holds.  The
  withdrawal is recorded on the chat's own measurement and says so.

  It does not re-derive the delta-fraction result.  Register 1148's replacement
  reports circular rms 0.274 on delta mod 1 against about 0.29 for a uniform guess;
  the 311-channel table it comes from is not held here.  What IS checked is the
  arithmetic that makes the retraction true at all -- floor(2.38) = 2 = B.

  It offers no verdict on whether an unrepaired entry should be repaired.  It says
  which are repaired, which are not, and what the chat measured.  Seating is a
  build's act and M's ruling is what authorises it.

  Nothing is repaired by this program.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, contextlib, io, os, re, runpy, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
REG = os.path.join(MEM, "The_Method_1_6___The_Register-2.md")

# entry -> (the PROSE-ONLY row, a string the CORRECTING entry must contain).
# The string is taken from the chat's own correction, never from the entry.
CLASS = {
    230:  ("PO-0019", "2,475"),
    314:  ("PO-0190", "0.8087"),
    500:  ("PO-0087", None),
    502:  ("PO-0087", None),
    599:  ("PO-0094", "Marginals cannot see a hole"),
    602:  ("PO-0015/0026", "24,585"),
    807:  ("PO-0820", "44 of 49"),
    1148: ("PO-0107", None),
    1395: ("PO-0128", "thirty-eight and twenty"),
    1450: ("PO-0051", "Kitagawara"),
    1461: ("PO-0136", "empties fourteen times"),
    1595: ("PO-0145", "no cache"),
    1628: ("PO-0145", "no cache"),
}
# 497, 498 and 499 are NOT on the branch's list and the same chat message withdraws
# them in the same table.  They are measured with the other two.
KAPPA = (497, 498, 499, 500, 502)


def entries():
    """Every seated entry as {number: body}, read from the Register itself."""
    t = open(REG, encoding="utf-8").read()
    out, cur, buf = {}, None, []
    for line in t.split("\n"):
        m = re.match(r"^### (\d+)$", line)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf)
            cur, buf = int(m.group(1)), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf)
    return out


def corrected_by(ent, n, needle):
    """The later entry that cites n and carries the correction's own text."""
    hits = []
    for m, body in sorted(ent.items()):
        if m <= n:
            continue
        # The Register cites in prose, in small caps and in a trailing list, so the
        # citation is matched case-insensitively and in all three shapes.
        if not re.search(r"register %d\b|\b%d's\b|[;:] %d[;.]" % (n, n, n), body, re.I):
            continue
        if needle is None or needle.lower() in body.lower():
            hits.append(m)
    return hits


def towers_agree():
    """Λ8 is one object under both seated towers -- what lets either be used."""
    with contextlib.redirect_stdout(io.StringIO()):
        a = runpy.run_path(os.path.join(MEM, "tower.py"))["L8"]
        b = runpy.run_path(os.path.join(MEM, "tower-2.py"))["L8"]()
    return len(a), len(b), sorted(map(tuple, a)) == sorted(map(tuple, b))


# --- the arithmetic the chats' corrections rest on, re-derived here -------------
def sr_i_nd():
    """Register 1148 called Sr I nd a structural flaw because delta = 2.38 > B = 2.
    The bound is on the INTEGER part.  floor(2.38) = 2 = B, so it is satisfied."""
    delta, B = 2.38, 2
    return {"delta": delta, "B": B, "floor": int(delta // 1),
            "delta_exceeds_B": delta > B, "floor_exceeds_B": int(delta // 1) > B}


def lambda_spectra():
    """Register 1395 split 58 as 47 beyond / 11 within.  The correction is 38 / 20:
    the nine added are 6d7..6d10 and 7p2..7p6, needing Z = 109..118, all synthesised
    and all in the table, which register 1395's limit of Z = 108 excluded."""
    added = ["6d7", "6d8", "6d9", "6d10", "7p2", "7p3", "7p4", "7p5", "7p6"]
    total, old_within = 58, 11
    new_within = old_within + len(added)
    return {"added": added, "n_added": len(added), "total": total,
            "old": (total - old_within, old_within),
            "new": (total - new_within, new_within)}


def report():
    ent = entries()
    print("THE TWELVE ENTRIES SAID TO ASSERT WHAT A CHAT WITHDREW")
    print()
    print("THE TEST THAT BUILT THE CLASS looked for a withdrawal marker INSIDE each")
    print("entry.  The store's rule is that an entry is never edited and the repair")
    print("is a new appended entry, so a correctly repaired entry carries no marker.")
    print("Measured the other way -- is there a later entry that cites it and carries")
    print("the correction's own figure?")
    print()
    print("  entry   PROSE-ONLY      repaired by      the figure looked for")
    unrep = []
    for n in sorted(CLASS):
        po, needle = CLASS[n]
        hits = corrected_by(ent, n, needle)
        seated = "seated" if n in ent else "NOT SEATED"
        if hits:
            print("  %-6d  %-14s  %-15s  %s" % (n, po, ", ".join(map(str, hits)), needle))
        else:
            unrep.append(n)
            print("  %-6d  %-14s  %-15s  %s" % (n, po, "NONE", needle or "(no figure pinned)"))
        assert seated == "seated", n
    print()
    print("  repaired already : %d of %d" % (len(CLASS) - len(unrep), len(CLASS)))
    print("  unrepaired       : %s" % ", ".join(map(str, unrep)))
    print()

    print("AND THE KAPPA WITHDRAWAL IS WIDER THAN THE LIST")
    print("  The chat message that withdraws 500 and 502 withdraws 497, 498 and 499 in")
    print("  the same table, and marks 501 as surviving.  All five are seated and none")
    print("  is corrected anywhere in the Register:")
    for n in KAPPA:
        print("    register %-4d seated %s   corrected by %s"
              % (n, n in ent, corrected_by(ent, n, None) or "NONE"))
    print("    register 501  seated %s   -- the one the chat says SURVIVES" % (501 in ent))
    print()

    print("THE ARITHMETIC THE UNREPAIRED CORRECTIONS REST ON")
    s = sr_i_nd()
    print("  1148  Sr I nd: delta = %.2f, B = %d" % (s["delta"], s["B"]))
    print("        delta > B          : %s   <- what 1148 called a structural flaw"
          % s["delta_exceeds_B"])
    print("        floor(delta) > B   : %s   <- the bound is on the integer part"
          % s["floor_exceeds_B"])
    print("        floor(%.2f) = %d = B, so the bound is SATISFIED and the flaw is not there."
          % (s["delta"], s["floor"]))
    l = lambda_spectra()
    print("  1395  Lambda_spectra: the split of %d" % l["total"])
    print("        as printed         : %d beyond / %d within" % l["old"])
    print("        corrected          : %d beyond / %d within" % l["new"])
    print("        the %d added       : %s" % (l["n_added"], ", ".join(l["added"])))
    print("        each needs Z = 109..118, synthesised and in the table; 1395 took")
    print("        the ground table's own edge (Z = 108) for the subject's edge.")
    print("        %d + %d = %d and %d - %d = %d, so the accounting closes."
          % (l["old"][1], l["n_added"], l["new"][1], l["total"], l["new"][1], l["new"][0]))
    print()

    a, b, same = towers_agree()
    print("THE OBJECT IS ONE OBJECT UNDER BOTH SEATED TOWERS")
    print("  tower.py gives %d cells, tower-2.py gives %d, identical: %s" % (a, b, same))
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    ent = entries()
    chk("every entry of the class is seated", sorted(n for n in CLASS if n in ent),
        sorted(CLASS))

    # The corrections that ARE seated, each found by its own figure.
    for n, by in ((230, 1819), (314, 1841), (599, 601), (602, 1820), (807, 823),
                  (1395, 1426), (1450, 1839), (1461, 1463), (1595, 1629), (1628, 1629)):
        po, needle = CLASS[n]
        hits = corrected_by(ent, n, needle)
        chk("register %d is repaired, and %d is among the repairs" % (n, by),
            by in hits, True)

    # The ones that are not.
    for n in (500, 502, 1148):
        chk("register %d has no correction in the Register" % n,
            corrected_by(ent, n, None), [])
    chk("so ten of the twelve were already repaired, and three are not",
        len([n for n in CLASS if corrected_by(ent, n, CLASS[n][1])]), 10)

    # The kappa family is wider than the branch's list.
    chk("the chat withdraws five kappa entries, not two", len(KAPPA), 5)
    chk("497, 498 and 499 are seated and were never on the list",
        all(n in ent for n in (497, 498, 499)), True)
    chk("and none of the five is corrected anywhere",
        [n for n in KAPPA if corrected_by(ent, n, None)], [])
    chk("register 501, which the chat says survives, is seated", 501 in ent, True)

    # 807 is not a withdrawal at all: its PROSE-ONLY row is a MEASUREMENT that
    # extends the entry's evidence rather than contradicting it.
    chk("807's own request is what 823 says is now backed",
        "register 807's request" in ent[823], True)

    # 1148, re-derived.
    s = sr_i_nd()
    chk("1148: delta exceeds B, which is what the entry saw", s["delta_exceeds_B"], True)
    chk("1148: floor(delta) does NOT exceed B, which is the bound", s["floor_exceeds_B"], False)
    chk("1148: floor(2.38) equals B", (s["floor"], s["B"]), (2, 2))

    # 1395, re-derived.
    l = lambda_spectra()
    chk("1395: nine cells were excluded", l["n_added"], 9)
    chk("1395: they are the 6d and 7p occupancies of Z = 109..118",
        l["added"], ["6d7", "6d8", "6d9", "6d10", "7p2", "7p3", "7p4", "7p5", "7p6"])
    chk("1395: the printed split", l["old"], (47, 11))
    chk("1395: the corrected split", l["new"], (38, 20))
    chk("1395: and both split the same 58", sum(l["old"]) == sum(l["new"]) == 58, True)
    chk("1395: the entry prints 58 as E before the limit", "E = 58" in ent[1395], True)
    chk("1395: and eleven as the residual", "E = 11" in ent[1395], True)

    a, b, same = towers_agree()
    chk("both seated towers give 976 cells", (a, b), (976, 976))
    chk("and the same 976", same, True)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
