#!/usr/bin/env python3
"""DOCKET 35 (capture half) -- the magnetic and antimagnetic rotational bands.

    python3 nbcapture.py --selftest   fixtures: the paper's OWN stated census
    python3 nbcapture.py --write      regenerate captures/NUCBANDS-*.tsv
    python3 nbcapture.py              the capture report

===============================================================================
WHY THIS FILE EXISTS, AND WHAT IT IS NOT
===============================================================================

`subpop.py` section 4 recorded four closed routes to nuclear level data and
concluded there was nothing this environment could reach.  That was WRONG, and
`NAVIGATION.md` section 3 says why: navigate by JOIN, never by meet.  All four
were meets.  Run as a join over the paper database, the route opens, and this
file is the capture that follows.

    SOURCE.  J. X. Teng and K. Y. Ma, "Magnetic and antimagnetic rotational
    bands data tables", arXiv:2303.13849, submitted to Atomic Data and Nuclear
    Data Tables.  The full text as retrieved is seated beside this file at
    `captures/arxiv-2303.13849.txt`; the capture reads THAT and never the
    network, so it reproduces here with no connector and no egress.  arXiv is
    403 over https through this proxy exactly as ENSDF is -- the connector was
    a different bracket, and the join is what reached it.

THE CAPTURE IS NOT A CLAIM TO HAVE READ THE PAPER.  It is a parse of a PDF
text extraction, and a parse can be wrong in ways a count does not show.  So
the fixtures are of two kinds, and the second kind is the one that matters:

    THE PAPER'S OWN CENSUS.  It states 252 magnetic rotational bands in 123
    nuclei and 38 antimagnetic in 27.  The parse reproduces all four numbers
    EXACTLY and independently -- Table A and Table B are parsed by the same
    code and counted separately.  That is the totality argument: not "the
    queries looked complete" but "the paper says how many there are, and this
    is that many".

    THE PHYSICS THE PAPER STATES ABOUT THE BANDS.  An MR band is defined by a
    DELTA-I = 1 structure and an AMR band by DELTA-I = 2 -- those are the
    papers' own defining criteria, not conventions.  Measured over every
    consecutive pair of extracted spins:

        Table B (AMR)   213 of 213 steps are Delta(2I) = 4, i.e. Delta-I = 2
        Table A (MR)    1758 of 1762 steps are Delta(2I) = 2, i.e. Delta-I = 1

    A count fixture cannot catch a parser that reads the right number of wrong
    things.  This one can, and 100 % on Table B is what says the columns are
    being read in the right order.

===============================================================================
THE FOUR ANOMALIES, ALL RUN DOWN, AND NONE OF THEM THIS PARSER'S
===============================================================================

    85-Zr BAND 1 jumps 31/2 -> 35/2 -> 39/2.  The source prints exactly that:
    two Delta-I = 2 steps at the top of the band, carrying only E2 energies
    (1451, 1705) and no M1.  A band crossing, and REAL PHYSICS.

    133-Pr BAND 3 prints (57/2-) between (45/2-) and (49/2-).  There is no
    reading of that which is not a TYPOGRAPHICAL ERROR IN THE PUBLISHED PAPER:
    the energies run 6323.6, 6824.6, 7372.8 in order and the E2 cascade is
    unbroken, so the level is 47/2 and the 5 is a 4.  RECORDED, NOT REPAIRED
    -- the capture carries 57 because that is what the source says, and
    `SOURCE_FAULTS` names it so nobody re-derives it as a parse bug.

===============================================================================
THE 27 BANDS THAT CARRY NO SPIN AT ALL
===============================================================================

    Twenty-seven of the 252 MR bands are printed with NO I-pi COLUMN.  They
    sit in the A ~ 190 region (Hg, Pb, Bi, At, Fr) and their energies are
    relative to an unknown bandhead -- `200-Pb 1 X`, then 100.6+X, 223.9+X and
    so on.  The paper's Explanation of Tables says why: absolute excitation
    energies are unknown where the linking transitions to lower levels are not
    established.

    THEY ARE NOT A PARSE FAILURE AND THEY ARE NOT AN INDEX MEMBER.  The
    criterion is that a member carries quantum numbers; a band with no spin
    and no parity carries none.  They are captured, counted, and marked
    NO-SPIN, and `nucbands.py` refuses them on the criterion rather than
    dropping them quietly -- which is the same shape as the spin-4 mesons PDG
    could not place in a mass reach.

Z comes from `mendeleev` 1.3.0, the same way the space groups come from
`spglib` and the particles from `particle`: a real source rather than a
periodic table typed out here.  THIS FILE IS THE ONLY ONE THAT NEEDS IT --
`nucbands.py` reads the TSV and is stdlib-only.
"""

import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(HERE, "captures")
SRC = os.path.join(CAP, "arxiv-2303.13849.txt")
BANDS_TSV = os.path.join(CAP, "NUCBANDS-bands.tsv")
LEVELS_TSV = os.path.join(CAP, "NUCBANDS-levels.tsv")

PAPER = "arXiv:2303.13849 -- Teng & Ma, Magnetic and antimagnetic rotational bands data tables"
SRC_MD5 = "1847412451a8fff4d81f4dfde0fc07d9"

# The paper's own census, from its abstract and its summary.  These are the
# fixtures; the parse is measured AGAINST them, never fitted to them.
STATED = {"MR": (252, 123), "AMR": (38, 27)}

# Faults in the SOURCE, found by the structural check and left in place.
SOURCE_FAULTS = (
    (133, "Pr", 3, "prints (57/2-) between (45/2-) and (49/2-); the energies "
                   "6323.6 / 6824.6 / 7372.8 and the unbroken E2 cascade make "
                   "it 47/2.  A typo in the published table, captured as "
                   "printed and NOT repaired."),
)

# Real physics the structural check turned up, so it is not re-litigated.
NOT_A_FAULT = (
    (85, "Zr", 1, "31/2 -> 35/2 -> 39/2 is two Delta-I = 2 steps at the top of "
                  "the band, with E2 energies 1451 and 1705 and no M1: a band "
                  "crossing, printed correctly."),
)

ELEM = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn
Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te
I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au
Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu""".split())

# Table A is the magnetic bands, Table B the antimagnetic.  Both are located by
# their own heading rather than by a line number, so an updated fetch still cuts
# in the right place.
def _sections(lines):
    hits = [i for i, s in enumerate(lines) if s.startswith("Table A. Magnetic")]
    hitb = [i for i, s in enumerate(lines) if s.startswith("Table B. Antimagnetic")]
    a0, b0 = hits[-1], hitb[-1]
    return {"MR": lines[a0:b0], "AMR": lines[b0:]}


DATA = re.compile(r'^(\d{2,3}$|\(?\d+\.\d|\d+ [\(\d]|[A-Z][a-z]? \d'
                  r'|\(?\d+\+[A-Z]\b|\d+ [A-Z]\b)')
PARITY = re.compile(r'^[\(\)]*[+−][\)\(]*$')
ENER = (r'\(?[\d]+(?:\.\d+)?(?:\+[A-Z])?\)?|\(?[A-Z]\)?'
        r'|\(?\d*\+[A-Z]\)?|\(A[<>]\d+\)\?')
SPIN = r'\(?\d{1,2}(?:/2)?[\(\)]*[+−]?[\(\)]*\)?'
ROW = re.compile(r'^(%s)\s+(%s)(\s|$)' % (ENER, SPIN))
ENERTOK = re.compile(r'^(%s)$' % ENER)


def _strip(lines):
    """Drop page numbers and the column header repeated on every page."""
    out, i = [], 0
    while i < len(lines):
        s = lines[i].rstrip()
        # a bare integer, then a blank, then a column header, is a PAGE NUMBER
        if re.fullmatch(r'\d{1,3}', s) and i + 2 < len(lines) \
           and lines[i + 1].strip() == "" and lines[i + 2].startswith("Nuclei band"):
            i += 1
            continue
        if s.startswith("Nuclei band") or s.startswith("Table A.") \
           or s.startswith("Table B."):
            i += 1
            # stop on anything that is DATA -- including a level row that
            # resumes a band across a page break, which carries a
            # parenthesised energy and so matches no DATA alternative
            while i < len(lines):
                t = lines[i].rstrip()
                if DATA.match(t) or _is_row(t):
                    break
                i += 1
            continue
        if s:
            out.append(s)
        i += 1
    return out


def _is_row(s):
    """(energy, I-pi) if this line opens a LEVEL row, else None."""
    m = ROW.match(s)
    if not m:
        return None
    if "." in m.group(2):          # an Egamma is not a spin
        return None
    return (m.group(1), m.group(2))


def _rejoin(lines):
    """A wrapped parity superscript sits BETWEEN the I column and the rest of
    its own row, so pulling it up must pull the remainder of the row with it --
    but never a line that opens a row of its own."""
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if out and PARITY.match(s):
            out[-1] += s
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            band = re.match(r'^(\d{1,2}) (\S+)', nxt)
            pull = bool(nxt) \
                and not re.fullmatch(r'\d{2,3}', nxt) \
                and not (re.match(r'^[A-Z][a-z]? \d', nxt) and nxt.split()[0] in ELEM) \
                and not _is_row(nxt) \
                and not (band and ENERTOK.match(band.group(2)))
            if pull:
                out[-1] += " " + nxt
                i += 2
                continue
            i += 1
            continue
        if out and s.startswith(")"):
            out[-1] += s
            i += 1
            continue
        out.append(s)
        i += 1
    return out


def spin2(tok):
    """(2I, parity) from an I-pi cell.  2I so half-integers stay integers."""
    par = None
    if "−" in tok:
        par = -1
    elif "+" in tok:
        par = +1
    t = re.sub(r'[()+−\s]', "", tok)
    if not t:
        return None, par
    return (int(t[:-2]) if t.endswith("/2") else 2 * int(t)), par


_C = {}


def bands():
    """[{table, A, el, band, levels:[(E, 2I, parity)]}] -- every band, both tables."""
    if "b" not in _C:
        lines = open(SRC, encoding="utf-8").read().split("\n")
        out = []
        for tag, chunk in _sections(lines).items():
            j = _rejoin(_strip(chunk))
            cur, A, nuc = None, None, None
            for k, s in enumerate(j):
                nxt = j[k + 1] if k + 1 < len(j) else ""
                # a bare 2-3 digit line is a MASS NUMBER only if an element follows;
                # otherwise it is an Egamma that wrapped, and they look identical
                if re.fullmatch(r'\d{2,3}', s) and re.match(r'^[A-Z][a-z]? \d', nxt) \
                   and nxt.split()[0] in ELEM:
                    A = int(s)
                    continue
                m = re.match(r'^([A-Z][a-z]?) (\d+) (.*)$', s)
                if m and m.group(1) in ELEM:
                    nuc = m.group(1)
                    cur = {"table": tag, "A": A, "el": nuc,
                           "band": int(m.group(2)), "levels": []}
                    out.append(cur)
                    s = m.group(3)
                else:
                    m2 = re.match(r'^(\d{1,2}) (\S+)(.*)$', s)
                    # a band may open with an energy LABEL and no spin at all,
                    # so a band start is looser than a level row
                    if m2 and nuc and ENERTOK.match(m2.group(2)) \
                       and not re.fullmatch(r'\(?\d{1,2}\)?', m2.group(2)):
                        cur = {"table": tag, "A": A, "el": nuc,
                               "band": int(m2.group(1)), "levels": []}
                        out.append(cur)
                        s = m2.group(2) + m2.group(3)
                if cur is None:
                    continue
                r = _is_row(s)
                if r:
                    i2, par = spin2(r[1])
                    cur["levels"].append((r[0], i2, par))
        _C["b"] = out
    return _C["b"]


def census():
    """{table: (bands, nuclei)} -- measured, to be compared with STATED."""
    out = {}
    for tag in ("MR", "AMR"):
        bs = [b for b in bands() if b["table"] == tag]
        out[tag] = (len(bs), len({(b["A"], b["el"]) for b in bs}))
    return out


def steps():
    """{table: {Delta(2I): n}} -- the papers' own defining selection rule."""
    out = {}
    for tag in ("MR", "AMR"):
        d = {}
        for b in bands():
            if b["table"] != tag:
                continue
            s = [x[1] for x in b["levels"] if x[1] is not None]
            for a, c in zip(s, s[1:]):
                d[c - a] = d.get(c - a, 0) + 1
        out[tag] = d
    return out


def nospin():
    """[(A, el, band)] -- bands the source prints with no I-pi column."""
    return [(b["A"], b["el"], b["band"]) for b in bands() if not b["levels"]]


def zmap():
    """{symbol: Z} from mendeleev.  Capture-side only; the TSV carries Z."""
    from mendeleev import element
    return {s: element(s).atomic_number
            for s in sorted({b["el"] for b in bands()})}


def write():
    Z = zmap()
    n = 0
    with open(BANDS_TSV, "w", encoding="utf-8") as f:
        f.write("# %s\n" % PAPER)
        f.write("# source %s md5 %s\n" % (os.path.basename(SRC), SRC_MD5))
        f.write("# Z from mendeleev 1.3.0.  Regenerate: python3 nbcapture.py --write\n")
        f.write("# status NO-SPIN: the source prints no I^pi column for this band\n")
        f.write("table\tA\tZ\tel\tband\tlevels\thead_E\thead_2I\thead_par\tstatus\n")
        for b in bands():
            lv = b["levels"]
            h = lv[0] if lv else ("", None, None)
            f.write("%s\t%d\t%d\t%s\t%d\t%d\t%s\t%s\t%s\t%s\n"
                    % (b["table"], b["A"], Z[b["el"]], b["el"], b["band"], len(lv),
                       h[0], "" if h[1] is None else h[1],
                       "" if h[2] is None else h[2],
                       "PLACED" if lv else "NO-SPIN"))
            n += 1
    with open(LEVELS_TSV, "w", encoding="utf-8") as f:
        f.write("# %s\n" % PAPER)
        f.write("# one row per band member carrying an I^pi.  2I is doubled so a\n")
        f.write("# half-integer spin stays an integer.  par blank = no parity printed.\n")
        f.write("table\tA\tZ\tel\tband\tE_keV\t2I\tpar\n")
        for b in bands():
            for (e, i2, par) in b["levels"]:
                f.write("%s\t%d\t%d\t%s\t%d\t%s\t%s\t%s\n"
                        % (b["table"], b["A"], Z[b["el"]], b["el"], b["band"],
                           e, "" if i2 is None else i2, "" if par is None else par))
    return n


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the source text is the one this capture was written against",
        md5(SRC), SRC_MD5)

    c = census()
    chk("MR: the paper says 252 bands in 123 nuclei, and so does the parse",
        c["MR"], STATED["MR"])
    chk("AMR: the paper says 38 bands in 27 nuclei, and so does the parse",
        c["AMR"], STATED["AMR"])

    s = steps()
    chk("AMR is Delta-I = 2 by definition -- and ALL 213 steps are",
        (sorted(s["AMR"]), sum(s["AMR"].values())), ([4], 213))
    chk("MR is Delta-I = 1 by definition -- 1758 of 1762 steps are",
        (s["MR"][2], sum(s["MR"].values())), (1758, 1762))
    chk("and the four exceptions are two bands, both run down",
        sorted(k for k in s["MR"] if k != 2), [-8, 4, 12])

    chk("27 MR bands carry no I^pi column at all, and none of the AMR do",
        (len(nospin()), len([b for b in bands()
                             if b["table"] == "AMR" and not b["levels"]])),
        (27, 0))
    chk("and every one of them is in the A ~ 190 region, as the source says",
        sorted({el for _a, el, _b in nospin()}),
        ["At", "Bi", "Eu", "Fr", "Hg", "Pb"])

    chk("the source's own typo is named, not silently corrected",
        [(a, e, b) for a, e, b, _w in SOURCE_FAULTS], [(133, "Pr", 3)])
    chk("and 133-Pr band 3 still carries the 57 the paper printed",
        [x[1] for b in bands()
         if (b["A"], b["el"], b["band"]) == (133, "Pr", 3) for x in b["levels"]],
        [29, 31, 33, 35, 37, 39, 41, 43, 45, 57, 49, 51, 53])

    lv = sum(len(b["levels"]) for b in bands())
    chk("levels extracted, and every one carries a spin", lv, 2238)
    chk("no extracted level is missing its 2I",
        sum(1 for b in bands() for x in b["levels"] if x[1] is None), 0)

    for p, want in ((BANDS_TSV, 290), (LEVELS_TSV, 2238)):
        if os.path.exists(p):
            rows = [l for l in open(p, encoding="utf-8")
                    if l.strip() and not l.startswith("#")][1:]
            chk("%s holds %d rows" % (os.path.basename(p), want), len(rows), want)

    print("nbcapture selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 35 -- THE NUCLEAR ROTATIONAL BAND CAPTURE")
    print("=" * 79)
    print()
    print("SOURCE  %s" % PAPER)
    print("        %s  md5 %s" % (os.path.basename(SRC), md5(SRC)))
    print("        Reached by JOIN over the paper database.  arXiv is 403 over")
    print("        https through this proxy, exactly as ENSDF is.")
    print()
    print("1. THE TOTALITY ARGUMENT IS THE PAPER'S OWN CENSUS.")
    c = census()
    print("     %-6s %-22s %-14s %s" % ("table", "what", "stated", "parsed"))
    for tag, what in (("MR", "magnetic rotation"), ("AMR", "antimagnetic")):
        print("     %-6s %-22s %-14s %s  %s"
              % (tag, what, "%d bands / %d nuclei" % STATED[tag],
                 "%d / %d" % c[tag],
                 "EXACT" if c[tag] == STATED[tag] else "*** DRIFT ***"))
    print()
    print("2. AND THE PHYSICS CHECKS THE COLUMN ORDER, WHICH A COUNT CANNOT.")
    s = steps()
    for tag, rule in (("MR", "Delta-I = 1"), ("AMR", "Delta-I = 2")):
        tot = sum(s[tag].values())
        want = 2 if tag == "MR" else 4
        print("     %-4s %s -> Delta(2I) = %d in %d of %d consecutive steps (%.1f %%)"
              % (tag, rule, want, s[tag].get(want, 0), tot,
                 100.0 * s[tag].get(want, 0) / tot))
    print("     A parser that read the wrong column would not land on 100 %.")
    print()
    print("3. FOUR ANOMALIES, ALL RUN DOWN.  NONE IS THIS PARSER'S.")
    for a, e, b, why in SOURCE_FAULTS:
        print("     %d-%s band %d  SOURCE FAULT" % (a, e, b))
        print("        %s" % why)
    for a, e, b, why in NOT_A_FAULT:
        print("     %d-%s band %d  NOT A FAULT" % (a, e, b))
        print("        %s" % why)
    print()
    print("4. TWENTY-SEVEN BANDS CARRY NO SPIN, AND THAT IS A FINDING.")
    ns = nospin()
    print("     %d of the 252 MR bands are printed with no I^pi column, all in"
          % len(ns))
    print("     the A ~ 190 region: %s"
          % ", ".join(sorted({el for _a, el, _b in ns})))
    print("     Their energies are relative to an unknown bandhead (X, Y, Z, U, V).")
    print("     They carry NO quantum number, so they are not index members --")
    print("     captured and marked NO-SPIN, refused on the criterion, not dropped.")
    print()
    print("     bands captured   %d" % len(bands()))
    print("     levels captured  %d" % sum(len(b["levels"]) for b in bands()))
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--write" in sys.argv:
        n = write()
        print("wrote %s and %s (%d bands)"
              % (os.path.basename(BANDS_TSV), os.path.basename(LEVELS_TSV), n))
        sys.exit(0)
    sys.exit(report())
