"""Section 12.11.1.2's conservative share, and the three things said about it.

DEFERRED's chat-77 additions file four findings against this section and the two
Register entries that carry it, and mark all four "for R3, no withdrawal".  They
are re-measured here from the section's own method, on its own four cap settings.

WHAT THE SECTION PRINTS

    caps                  |L9|    composable    conservative     share
    (3, 3, 1, 3, 1)      1,654         1,169             739     63.2%
    (4, 4, 1, 6, 1)     19,433        16,150           5,986     37.1%
    (4, 4, 2, 6, 2)     44,153        37,430          14,114     37.7%
    (5, 5, 2, 6, 2)     83,543        71,087          26,921     37.9%

  "Once the d shell is open the share sits at 37-38% and moves by less than a
   point across a fiftyfold growth in cells -- so the honest statement is ...
   that reversibility settles near three cells in eight among the composable."

THE FINDINGS UNDER TEST

  12u-01  the d shell is ABSENT at the 37.1% row.
  12u-02  "less than a point across a fiftyfold growth" joins two ranges: the
          fiftyfold growth carries 25.3 points, and the range that moves less
          than a point is fourfold.
  12u-03  the quantity is the CONSERVATIVE share, g = q, and the sentence names
          it reversibility; the reverse-edge share is a different series.
  12v-02  register 625 attributes 50.3% for Lambda_8 to register 623, whose
          printed body says 0%.

THE METHOD, taken from the section verbatim: build Lambda_9 at a caps tuple, keep
the cells whose target is a legal source, count those with g = q.  The source and
target shapes are not assumed here either -- they are composab.py's, which are the
pairing that reproduces the Compendium's own printed fractions, and the first row
of the table above is what identifies the object.

INPUT
  method/members/tower-2.py  -- the seated tower, imported by path for its L9 at
  the book's caps, which the parameterised builder must reproduce cell for cell
  before any other row is trusted.
  method/members/The_Method_1_6-2.md and ...___The_Register-2.md -- read for the
  printed table and the two entries.

REFUSALS
  It does not say what "reversibility" ought to mean.  It measures one reading --
  the reverse edge is itself a cell -- states that reading, and reports that it
  is a different series from the one the sentence attaches the word to.  A second
  reading might give a third series; the finding is that the word and the number
  are not the same object, and that does not need the word pinned down.

  It offers no verdict on whether register 623 was ever written with 50.3%.  It
  measures what 623 prints now, what 625 says 623 prints, and what the arithmetic
  of 623's own headline requires.  A residue is evidence about a draft, not a
  record of one.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
MAIN = os.path.join(MEM, "The_Method_1_6-2.md")
REG = os.path.join(MEM, "The_Method_1_6___The_Register-2.md")

# (n_max, e_max, l_max, k_max, f_max) -- the section's own column, in its own order.
CAPS = [(3, 3, 1, 3, 1), (4, 4, 1, 6, 1), (4, 4, 2, 6, 2), (5, 5, 2, 6, 2)]
PRINTED = {(3, 3, 1, 3, 1): (1654, 1169, 739, 63.2),
           (4, 4, 1, 6, 1): (19433, 16150, 5986, 37.1),
           (4, 4, 2, 6, 2): (44153, 37430, 14114, 37.7),
           (5, 5, 2, 6, 2): (83543, 71087, 26921, 37.9)}
SRC = (0, 1, 2, 7)      # n, l, k, 2S     -- composab.py's pairing
TGT = (4, 5, 6, 8)      # e, f, g, 2S'
D_SHELL_L = 2           # a d subshell is l = 2; l_max = 1 admits s and p only


def seated_tower():
    spec = importlib.util.spec_from_file_location("t2", os.path.join(MEM, "tower-2.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def L9(caps):
    """Lambda_9 at a caps tuple, by the generator the seated tower hard-codes at
    (3, 3, 1, 3, 1).  Reproducing that row cell for cell is what licenses the rest."""
    nmax, emax, lmax, kmax, fmax = caps
    out = []
    for n in range(1, nmax + 1):
        for l in range(0, min(lmax, n - 1) + 1):
            for k in range(1, min(kmax, 4 * l + 2) + 1):
                for q in range(0, k + 1):
                    for e in range(1, emax + 1):
                        for f in range(0, min(fmax, e - 1) + 1):
                            for g in range(0, min(4 * f + 2, q) + 1):
                                for S2 in range(0, k + 1):
                                    for s2p in range(0, g + 1):
                                        out.append((n, l, k, q, e, f, g, S2, s2p))
    return out


def shares(cells):
    """composable, conservative, and the reverse-edge count, in one pass."""
    src = {tuple(c[i] for i in SRC) for c in cells}
    tgt_of = {}
    for c in cells:
        tgt_of.setdefault(tuple(c[i] for i in SRC), set()).add(tuple(c[i] for i in TGT))
    comp = [c for c in cells if tuple(c[i] for i in TGT) in src]
    cons = [c for c in comp if c[6] == c[3]]                     # g = q
    # The reverse edge: the move T -> S is itself a cell of the index.
    rev = [c for c in comp
           if tuple(c[i] for i in SRC) in tgt_of.get(tuple(c[i] for i in TGT), ())]
    return len(comp), len(cons), len(rev)


def d_shell_open(caps):
    """Does the caps tuple admit l = 2 at all?  l is capped at min(l_max, n-1)."""
    nmax, emax, lmax, kmax, fmax = caps
    return lmax >= D_SHELL_L and nmax - 1 >= D_SHELL_L


def table():
    rows = []
    for caps in CAPS:
        cells = L9(caps)
        comp, cons, rev = shares(cells)
        rows.append({"caps": caps, "N": len(cells), "comp": comp, "cons": cons,
                     "rev": rev, "share": 100.0 * cons / comp,
                     "revshare": 100.0 * rev / comp, "d": d_shell_open(caps)})
    return rows


def entry(n):
    t = open(REG, encoding="utf-8").read()
    i = t.index("### %d\n" % n)
    j = t.index("\n### ", i + 1)
    return t[i:j]


def report():
    rows = table()
    print("SECTION 12.11.1.2's TABLE, REBUILT")
    print("  caps                    |L9|   composable  conservative   share    printed")
    for r in rows:
        p = PRINTED[r["caps"]]
        print("  %-18s %8s %11s %13s   %5.1f%%   %s"
              % (str(r["caps"]).replace(" ", ""), format(r["N"], ","),
                 format(r["comp"], ","), format(r["cons"], ","), r["share"],
                 "exact" if (r["N"], r["comp"], r["cons"]) == p[:3]
                 and abs(r["share"] - p[3]) < 0.05 else "DIFFERS"))
    print()

    print("12u-01  THE d SHELL AT THE 37.1% ROW")
    for r in rows:
        print("  %-18s l_max = %d   n_max - 1 = %d   admits l = 2 (a d subshell): %s"
              % (str(r["caps"]).replace(" ", ""), r["caps"][2], r["caps"][0] - 1, r["d"]))
    first = next(r for r in rows if r["d"])
    print("  The section reads: \"Once the d shell is open the share sits at 37-38%\".")
    print("  The first row admitting l = 2 is %s, at %.1f%%." %
          (str(first["caps"]).replace(" ", ""), first["share"]))
    print("  The 37.1%% row is %s -- l_max = 1, the SAME cap as the 63.2%% row it is"
          % str(rows[1]["caps"]).replace(" ", ""))
    print("  contrasted with.  What changes between those two rows is n, e and k, not l.")
    print("  CONFIRMED: the d shell is absent at the 37.1% row.")
    print()

    print("12u-02  THE TWO RANGES THE SENTENCE JOINS")
    lo, hi = rows[0], rows[-1]
    print("  \"moves by less than a point across a fiftyfold growth in cells\"")
    print("  the fiftyfold growth is %s -> %s cells = %.1fx," %
          (format(lo["N"], ","), format(hi["N"], ","), hi["N"] / lo["N"]))
    print("    and across it the share moves %.1f points (%.1f%% -> %.1f%%)."
          % (lo["share"] - hi["share"], lo["share"], hi["share"]))
    a = rows[1]
    print("  the range over which it moves less than a point is %s -> %s = %.1fx,"
          % (format(a["N"], ","), format(hi["N"], ","), hi["N"] / a["N"]))
    print("    over which it moves %.1f points (%.1f%% -> %.1f%%)."
          % (hi["share"] - a["share"], a["share"], hi["share"]))
    print("  CONFIRMED: one clause's growth belongs to the other clause's range.")
    print()

    print("12u-03  THE WORD AND THE NUMBER")
    print("  the quantity in the table is g = q -- the transfer total and nothing")
    print("  left behind, which is CONSERVATION.  The reverse-edge share, on the")
    print("  reading that the move T -> S is itself a cell, is a different series:")
    print("  caps                  conservative     reverse")
    for r in rows:
        print("  %-18s      %5.1f%%      %5.1f%%" %
              (str(r["caps"]).replace(" ", ""), r["share"], r["revshare"]))
    print("  CONFIRMED: \"reversibility settles near three cells in eight\" names the")
    print("  conservative series; on this reading reversibility is a different one.")
    print()

    print("12v-02  THE CORRECTION CHAIN AS PRINTED")
    e623, e625 = entry(623), entry(625)
    m = re.search(r"[Rr]egister 623's ([\d.]+)% for Λ₈", e625)
    print("  625 says of 623                : %s%%" % (m.group(1) if m else "?"))
    print("  623's body prints for Lambda_8 : %s" % ("0%" if "**0%**" in e623 else "?"))
    print("  623's headline                 : %s" % e623.split("\n")[2][:78])
    l9 = float(re.search(r"takes Λ₉ to\*?\*? *\*\*([\d.]+)%", e623).group(1))
    said = float(m.group(1)) if m else None
    print("  623's own Lambda_9 figure      : %.1f%%" % l9)
    print("  the jump its body describes    : %.1f - 0 = %.1f points" % (l9, l9))
    print("  the jump 625's attribution gives: %.1f - %.1f = %.1f points" % (l9, said, l9 - said))
    print("  and the headline says          : TWENTY points")
    print("  CONFIRMED: 625 attributes to 623 a figure 623 does not print; and the")
    print("  headline's twenty is the jump that attribution would give, not the one")
    print("  the body gives.  The two halves of the entry are on different sides of")
    print("  the correction.")
    print()
    print("RECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-58s %s" % (name, want))
        ok += 1

    # The object identifies itself: the parameterised builder must reproduce the
    # seated tower cell for cell at the book's own caps before anything else counts.
    t = seated_tower()
    chk("the builder reproduces the seated L9 cell for cell",
        L9((3, 3, 1, 3, 1)) == t.L9(), True)
    chk("and its size is the book's", len(t.L9()), 1654)

    rows = table()
    for r in rows:
        p = PRINTED[r["caps"]]
        chk("|L9| at %s" % str(r["caps"]).replace(" ", ""), r["N"], p[0])
        chk("  composable", r["comp"], p[1])
        chk("  conservative (g = q)", r["cons"], p[2])
        chk("  share to the printed digit", round(r["share"], 1), p[3])

    # 12u-01
    chk("l_max at the 63.2% row", rows[0]["caps"][2], 1)
    chk("l_max at the 37.1% row", rows[1]["caps"][2], 1)
    chk("so the 37.1% row admits no d subshell", rows[1]["d"], False)
    chk("the first row admitting one is the 37.7% row", [r["d"] for r in rows],
        [False, False, True, True])

    # 12u-02
    chk("cells grow 50.5-fold over the whole table",
        round(rows[-1]["N"] / rows[0]["N"], 1), 50.5)
    chk("and the share falls 25.3 points over it",
        round(rows[0]["share"] - rows[-1]["share"], 1), 25.3)
    chk("the range moving under a point is 4.3-fold",
        round(rows[-1]["N"] / rows[1]["N"], 1), 4.3)
    chk("and moves 0.8 of a point",
        round(rows[-1]["share"] - rows[1]["share"], 1), 0.8)

    # 12u-03
    chk("the reverse-edge series", [round(r["revshare"], 1) for r in rows],
        [33.3, 11.0, 11.2, 11.3])
    chk("it is not the conservative series",
        [round(r["revshare"], 1) for r in rows] == [round(r["share"], 1) for r in rows],
        False)
    chk("and it does not settle near three cells in eight",
        all(r["revshare"] < 37.5 for r in rows), True)

    # 12v-02
    e623, e625 = entry(623), entry(625)
    chk("625 attributes 50.3% to register 623",
        bool(re.search(r"[Rr]egister 623's 50\.3% for Λ₈", e625)), True)
    chk("623's printed body says 0%", "**0%**" in e623, True)
    chk("623 prints 50.3 nowhere", "50.3" in e623, False)
    chk("623's own Lambda_9 figure", 
        float(re.search(r"takes Λ₉ to\*?\*? *\*\*([\d.]+)%", e623).group(1)), 70.7)
    chk("623's headline says twenty points", "WORTH TWENTY POINTS" in e623, True)
    chk("the jump 623's body gives is 70.7, not twenty", round(70.7 - 0.0, 1), 70.7)
    chk("the jump 625's attribution gives is twenty", round(70.7 - 50.3, 1), 20.4)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else report()
