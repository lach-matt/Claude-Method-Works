r"""compendia2.py -- the successor to compendia.py, and the volumes' own defect list.

WHY THERE IS A SUCCESSOR AND NOT AN EDIT.  `compendia.py` was seated at BUILD275
one build ago.  A seated member is never edited in place; a corrected instrument
is a successor beside it, and the predecessor stays exactly as it was banked.
That is `r2-26b` -> `r2-26b2`'s shape and it is followed here.  W-281 carries the
corrections; W-280 stands unedited, wrong figures and all.

TWO FIGURES OF THE PREDECESSOR ARE WRONG, AND BOTH WERE WRONG IN THE SAME
DIRECTION -- a detector's premise taken for a measurement.

  1  THE SPECTRA TABLE'S ROW COUNT.  compendia.py counted eleven-cell pipe rows
     that are not separators and reported 597.  The volume states 596 and states
     it as 477 series of three or more members plus 119 two-member channels.
     The volume is RIGHT: the 597th row is the table's own HEADER, whose eleven
     cells are `species | series | n | levels | ...`.  Measured here both ways so
     the difference is visible rather than asserted.  THE NINE DUPLICATED KEYS
     ARE UNAFFECTED -- the header's key occurs once -- and they are re-measured
     here to prove it.

  2  THE HANDLE CLASS WAS UNDERCOUNTED.  compendia.py matched
     `[A-Z][a-z]?\.[a-z][a-z0-9_]*`, which requires a one- or two-character
     capitalised prefix and a LOWER-CASE first character after the dot.  That
     silently drops four whole families -- `EM.`, `LS.`, `3B.` -- and every
     handle whose suffix opens upper-case, `L.F`, `L.Fm1`, `A.F1` among them.
     It reported 221 distinct at 326 sites.

     THE DEFINITION USED HERE IS THE VOLUME'S OWN.  The Mathematical Compendium
     divides its objects into eighteen families under `## X. ... -- N objects`
     headings, and a handle is one of those eighteen codes, a dot, and an
     identifier.  Grounding the pattern in the volume's structure rather than in
     a guessed shape gives 265 distinct handles -- WHICH IS THE PLAN'S OWN
     FIGURE, and the plan was right where the instrument was not.

WHAT THE CORRECTED HANDLE COUNT CHANGES ABOUT THE RULING M IS OWED.  Not the
question, but its size and its shape.  407 of the 417 Mathematical Compendium
sites are ONE COLUMN OF ONE TABLE -- the bibliography's `objects` column, 162
rows, one row per work.  Outside that table the whole compendium prints ten.
The main volume prints 29 more, all of them Appendix G's third column.  So the
repair is not a sweep over 326 scattered sites: it is two tables.

AND THE 265 IS NOT A COINCIDENCE.  The Mathematical Compendium's cycle table
prints `closure -- objects the register holds | 265`.  265 is exactly the number
of distinct handles the bibliography's objects column names.  The volume holds
299 objects.  So the cycle table's label is wrong about what its own number
counts, and the bibliography's opening sentence -- "Every object of this
compendium names a work" -- is false by 34.

THE VOLUMES' OWN DEFECT LIST, which the census deferred.  Each row is measured,
and a row that DOES NOT REPRODUCE is reported as not reproducing rather than
quietly dropped:

  front matter (ruling 11)   299 / 265 / 248, three counts of one register
  Spectra L562               an n-range printed "41-5" against 15 levels
  IoI L2021                  a row truncated where an escaped pipe was lost
  Appendix G                 CLEAN -- the plan's three dead pointers do not reproduce
  the bracket-system object  ABSENT, as register 1880 says it is
  IoI tower rows             EXACT against the seated generators
  the 285-of-431 sentence    STALE BOTH WAYS -- the table now holds 126 of 596

REFUSALS.  It repairs nothing and it decides no editorial question.  It does not
re-run the pointer audit or the retraction audit, which are other instruments'
contracts.  It does not check the tower's `composable` column, because the
composition rule is stated in no member this instrument can import, and a figure
it cannot derive it does not judge.  A count taken by pattern is a floor.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")
VOLS = [("MC", "The_Method_1_6___Mathematical_Compendium-2.md"),
        ("PC", "The_Method_1_6___The_Physics_Compendium-2.md"),
        ("IoI", "The_Method_1_6___The_Index_of_Indices-2.md"),
        ("SC", "The_Method_1_6___Spectra_Compendium-2.md")]
MAIN = "The_Method_1_6-2.md"
REG = "The_Method_1_6___The_Register-2.md"

# The Mathematical Compendium's own family heading: the code, the title, the count.
FAMILY = re.compile(r"^## ([A-Za-z0-9]{1,3})\. (.*?) — (\d+) objects$", re.M)


def text(name):
    return open(os.path.join(MEM, name), encoding="utf-8").read()


def lines(name):
    return text(name).split("\n")


def nlines(name):
    """The store counts lines as wc -l does: newlines, not split pieces."""
    return text(name).count("\n")


def families():
    """(code, title, stated count) for each of the Mathematical Compendium's
    eighteen object families, in the order the volume prints them."""
    return [(m.group(1), m.group(2), int(m.group(3)))
            for m in FAMILY.finditer(text(VOLS[0][1]))]


def family_objects():
    """{code: [object heading, ...]} -- what the volume actually holds under each
    family, counted as `### ` headings between one family heading and the next."""
    out = collections.OrderedDict()
    code = None
    for ln in lines(VOLS[0][1]):
        m = FAMILY.match(ln)
        if m:
            code = m.group(1)
            out[code] = []
            continue
        if ln.startswith("# "):
            code = None
            continue
        if code is not None and ln.startswith("### "):
            out[code].append(ln[4:].strip())
    return out


def handle_rx():
    """The handle pattern, built from the volume's OWN family codes.

    Longest-first alternation, so `3B` and `EM` are not eaten by `B` and `E`."""
    codes = sorted((c for c, _, _ in families()), key=len, reverse=True)
    return (re.compile(r"`((?:%s)\.[A-Za-z0-9_]+)`" % "|".join(map(re.escape, codes))),
            re.compile(r"(?<![`\w.])((?:%s)\.[A-Za-z][A-Za-z0-9_]*)\b"
                       % "|".join(map(re.escape, codes))))


def handles(name):
    """(backticked sites, bare sites) in one volume, each (line, handle)."""
    tick, bare = handle_rx()
    tk, br = [], []
    for i, l in enumerate(lines(name), 1):
        tk += [(i, m.group(1)) for m in tick.finditer(l)]
        # a bare match inside backticks is already counted; drop it
        spans = [m.span() for m in tick.finditer(l)]
        for m in bare.finditer(l):
            if not any(a <= m.start() < b for a, b in spans):
                br.append((i, m.group(1)))
    return tk, br


def spectra_rows():
    """(header, data rows) of the Spectra Compendium's channel table.

    THE PREDECESSOR'S FAULT LIVES HERE.  It returned every eleven-cell
    non-separator row and called them all data.  The first such row is the
    table's header; the volume's own 596 counts the rest."""
    rows = []
    for i, l in enumerate(lines(VOLS[3][1]), 1):
        if not l.strip().startswith("|"):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) == 11 and not set("".join(cells)) <= set("-: "):
            rows.append((i, cells))
    return rows[0], rows[1:]


def duplicated_keys():
    """Duplicated (species, series) keys among the DATA rows only."""
    _, data = spectra_rows()
    seen = collections.defaultdict(list)
    for i, c in data:
        seen[(c[0], c[1])].append(i)
    return {k: v for k, v in seen.items() if len(v) > 1}


def bibliography():
    """(rows, handle occurrences, distinct handles) of the MC bibliography."""
    t = text(VOLS[0][1])
    i = t.index("\n# VII · THE BIBLIOGRAPHY")
    j = t.index("\n## The works this compendium leans on most")
    tick, _ = handle_rx()
    rows, occ = [], []
    for l in t[i:j].split("\n"):
        if not l.startswith("| ") or l.count("|") < 4:
            continue
        if l.startswith("| year |") or set(l.replace("|", "").strip()) <= set("-: "):
            continue
        rows.append(l)
        occ += tick.findall(l)
    return rows, occ, sorted(set(occ))


def stated_counts():
    """The three register counts the reader-facing front matter prints, with the
    generator and date each is stamped with.  Ruling 11's class."""
    out = []
    mc = text(VOLS[0][1])
    m = re.search(r"Generated from `(\w+\.py)` on ([\d-]+);.*?\*\*(\d+) objects", mc, re.S)
    out.append(("MC front matter", m.group(1), m.group(2), int(m.group(3)), "objects"))
    m = re.search(r"\| closure — objects the register holds \| \*\*(\d+)\*\* \|", mc)
    out.append(("MC cycle table", "—", "—", int(m.group(1)), "closure"))
    m = re.search(r"\| seed — objects nothing derives \| \*\*(\d+)\*\* \|", mc)
    seed = int(m.group(1))
    pc = text(VOLS[1][1])
    m = re.search(r"Generated from `(\w+\.py)`.*? on ([\d-]+)\. \*\*(\d+) registered objects", pc)
    out.append(("PC front matter", m.group(1), m.group(2), int(m.group(3)), "registered objects"))
    return out, seed


def appendix_g():
    """Appendix G's table, its handles, its Register citations and its § pointers.

    THE PLAN FILED THREE POINTERS TO ENTRIES THAT DO NOT EXIST.  Measured, every
    one resolves.  Reported as not reproducing."""
    t = text(MAIN)
    pos = [m.start() for m in re.finditer(r"\n## Appendix G — Transitions, indexed", t)]
    sec = t[pos[-1]:]
    j = sec.find("\n## ", 10)
    sec = sec[:j] if j > 0 else sec
    tick, _ = handle_rx()
    rows = [l for l in sec.split("\n") if l.startswith("|")
            and not set(l.replace("|", "").strip()) <= set("-: ")
            and not l.startswith("| § |")]
    hs = tick.findall(sec)
    cited = set()
    for m in re.finditer(r"register[s]?\s+((?:\d+[,;\s]*(?:and\s*)?)+)", sec, re.I):
        cited.update(int(x) for x in re.findall(r"\d+", m.group(1)))
    ptrs = sorted(set(re.findall(r"§\s?(\d+(?:\.\d+)*)", sec)))
    heads = {m.group(1) for m in re.finditer(r"^#{1,6}\s+(?:§\s*)?(\d+(?:\.\d+)*)", t, re.M)}
    return rows, hs, cited, ptrs, [p for p in ptrs if p not in heads]


def seated_entries():
    """Every Register number seated, grouped headings honoured."""
    s = set()
    for m in re.finditer(r"\n### ([\d,\s]+)\n", text(REG)):
        for p in re.split(r"\s*,\s*", m.group(1).strip()):
            if p.strip().isdigit():
                s.add(int(p.strip()))
    return s


def tower_rows():
    """The Index of Indices' tower table, and the same cell counts MEASURED by
    the seated generators.

    An instrument imports a seated member; it never copies one.  `tower.py` and
    `tower3.py` are run here in a scratch directory the instrument removes, and
    the counts come out of their own output and their own `tower.json`."""
    t = text(VOLS[2][1])
    i = t.index("\n# II · THE TOWER")
    j = t.index("\n---", i)
    # The volume writes the stage as a SUBSCRIPT -- Lambda-sub-8, not "Λ8" -- so a
    # plain \d read of these rows returns nothing at all rather than a wrong number.
    SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    rows = []
    for l in t[i:j].split("\n"):
        m = re.match(r"^\| \*\*Λ([₀-₉]+)\*\* \| ([\d,]+) \| (\d+) \| ([\d,]+) \| \*\*([\d.]+)\*\*", l)
        if m:
            rows.append((int(m.group(1).translate(SUB)), int(m.group(2).replace(",", "")),
                         int(m.group(3)), int(m.group(4).replace(",", "")),
                         float(m.group(5))))
    assert rows, "the tower table did not parse -- refusing to report an empty class"
    work = tempfile.mkdtemp(prefix="compendia2-")
    try:
        for n in ("tower.py", "tower3.py"):
            shutil.copy(os.path.join(MEM, n), os.path.join(work, n))
        r = subprocess.run([sys.executable, "tower.py"], cwd=work,
                           capture_output=True, text=True, timeout=600)
        assert r.returncode == 0, r.stderr[-400:]
        l8 = int(re.search(r"Λ8: cells = (\d+)", r.stdout).group(1))
        r = subprocess.run([sys.executable, "tower3.py", "bank"], cwd=work,
                           capture_output=True, text=True, timeout=600)
        assert r.returncode == 0, r.stderr[-400:]
        with open(os.path.join(work, "tower.json")) as fh:
            tj = json.load(fh)
        measured = {8: l8}
        measured.update({int(k): len(v) for k, v in tj.items()})
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return rows, measured


def spectra_nrange():
    """Every channel row whose printed n-range does not span its level count.

    The plan files Spectra L562.  Measured over the whole table so the row is
    found rather than trusted."""
    _, data = spectra_rows()
    bad = []
    for i, c in data:
        # A trailing dagger marks a row the volume flags; it is not part of the
        # range and it is not a defect.  Twelve rows carry one, and reading it as
        # unparsable is how a first draft of this function reported thirteen
        # faults where there is one.
        m = re.match(r"^(\d+)[–-](\d+)\s*[†*]?$", c[2].strip())
        if not m:
            bad.append((i, c[0], c[1], c[2], c[3], "unparsable"))
            continue
        lo, hi = int(m.group(1)), int(m.group(2))
        if hi < lo:
            bad.append((i, c[0], c[1], c[2], c[3], "range runs backwards"))
    return bad


def daggered_rows():
    """Channel rows whose n-range carries the volume's dagger marker."""
    _, data = spectra_rows()
    return [(i, c[0], c[1], c[2]) for i, c in data if "†" in c[2]]


def truncated_rows():
    """Table rows whose last content ends on a lone backslash -- an escaped pipe
    that lost the character it was escaping.  The plan files IoI L2021."""
    out = []
    for tag, name in VOLS:
        for i, l in enumerate(lines(name), 1):
            if not l.strip().startswith("|"):
                continue
            # SPLIT ON AN UNESCAPED PIPE ONLY.  A first draft split on every pipe
            # and reported 23, because the compendia write mathematics with
            # escaped bars -- \|X\|, \|2J - 2K\| -- and every one of those looks
            # like a cell ending in a backslash.  22 of the 23 were the splitter's
            # own premise.
            for cell in re.split(r"(?<!\\)\|", l.strip().strip("|")):
                if re.search(r"(?<!\\)\\\s*$", cell) and cell.strip() != "\\":
                    out.append((tag, i, cell.strip()[-60:]))
    return out


def channel_sentence():
    """The Physics Compendium's unverified-channel sentence, and the same two
    quantities measured on the Spectra Compendium's table as it now stands.

    The sentence names the state `channels.py` writes -- `bracket = "untested"` --
    so the like-for-like measurement is the count of table rows whose bracket
    cell reads exactly that, over the table's rows."""
    m = re.search(r"\*\*(\d+) of (\d+) channels are unverified on the compendium's "
                  r"central claim\*\*", text(VOLS[1][1]))
    _, data = spectra_rows()
    untested = sum(1 for _, c in data if c[5].strip() == "untested")
    return (int(m.group(1)), int(m.group(2))) if m else None, untested, len(data)


def bracket_system():
    """Register 1880 says the Mathematical Compendium prints no object for the
    bracket system.  Measured: does any object heading in family B or family T
    name it?"""
    objs = family_objects()
    cand = [o for fam in ("B", "T") for o in objs.get(fam, [])
            if re.search(r"stage.bracket|bracket system|rank.value|fibre", o, re.I)]
    entry = re.search(r"\n### 1880\n(.*?)\n### 1881\n", text(REG), re.S)
    claims = bool(entry) and "prints no object for the bracket system" in entry.group(1)
    return cand, claims


def report():
    print("compendia2 -- the successor's corrections, and the volumes' own defects")
    print("=" * 78)

    print("\n1  THE SPECTRA TABLE: THE PREDECESSOR COUNTED THE HEADER AS A ROW")
    head, data = spectra_rows()
    print("   eleven-cell non-separator rows           %d   <- compendia.py's figure" % (len(data) + 1))
    print("   of which the header, L%-6d            %s" % (head[0], head[1][:4]))
    print("   DATA rows                                %d   <- the volume's own figure" % len(data))
    star = sum(1 for _, c in data if "*" in c[0])
    print("   two-member (starred) / three-or-more     %d / %d" % (star, len(data) - star))
    dups = duplicated_keys()
    print("   duplicated (species, series) keys        %d  -- UNCHANGED by the correction" % len(dups))
    for k, v in sorted(dups.items()):
        print("        %-10s %-26s L%s" % (k[0], k[1], ", L".join(map(str, v))))

    print("\n2  THE HANDLE CLASS, ON THE VOLUME'S OWN FAMILY CODES")
    fams = families()
    print("   families / stated objects                %d / %d" % (len(fams), sum(f[2] for f in fams)))
    objs = family_objects()
    bad = [(c, n, len(objs[c])) for c, _, n in fams if len(objs[c]) != n]
    print("   families whose count is not what it holds %d %s" % (len(bad), bad or ""))
    tot_t = tot_b = 0
    allh = set()
    for tag, name in VOLS:
        tk, br = handles(name)
        tot_t += len(tk)
        tot_b += len(br)
        allh |= {h for _, h in tk} | {h for _, h in br}
        if tk or br:
            print("   %-4s backticked %4d | bare %3d | distinct %3d"
                  % (tag, len(tk), len(br), len({h for _, h in tk} | {h for _, h in br})))
    mt, mb = handles(MAIN)
    print("   main backticked %4d | bare %3d | distinct %3d   <- the class is not only"
          % (len(mt), len(mb), len({h for _, h in mt} | {h for _, h in mb})))
    print("        the compendia's: the main volume prints handles BARE in running prose,")
    print("        'L.c8 is k >= 1', where no backtick even marks them as ids.")
    print("   DISTINCT HANDLES ACROSS THE FOUR         %d   (compendia.py reported 221)" % len(allh))
    print("   SITES ACROSS THE FOUR                    %d   (compendia.py reported 326)" % (tot_t + tot_b))
    rows, occ, dist = bibliography()
    print("   of which the bibliography's objects column %d sites over %d rows, %d distinct"
          % (len(occ), len(rows), len(dist)))
    print("   so OUTSIDE that one column the compendia print %d" % (tot_t + tot_b - len(occ)))
    print("   a key resolving one of them is printed in NONE of the four:")
    print("        the word 'handle' occurs %d times in the four volumes"
          % sum(text(n).lower().count("handle") for _, n in VOLS))

    print("\n3  RULING 11 -- THREE COUNTS OF ONE REGISTER, IN READER-FACING FRONT MATTER")
    sc, seed = stated_counts()
    for where, gen, date, n, what in sc:
        print("   %-16s %-12s %-11s %5d  %s" % (where, gen, date, n, what))
    print("   the eighteen roots table is printed against a seed of %d" % seed)
    print("   AND 265 IS THE BIBLIOGRAPHY'S COVERAGE, NOT THE REGISTER'S HOLDING:")
    print("        distinct handles the objects column names   %d" % len(dist))
    print("        objects the compendium holds                %d" % sum(f[2] for f in fams))
    print("        so objects that name no work                %d" % (sum(f[2] for f in fams) - len(dist)))
    print("        against the section's opening sentence: 'Every object of this")
    print("        compendium names a work.'  FALSE BY %d." % (sum(f[2] for f in fams) - len(dist)))

    print("\n4  SPECTRA L562 -- AN n-RANGE THAT DOES NOT SPAN ITS LEVEL COUNT")
    print("   rows carrying the volume's dagger marker %d -- NOT defects" % len(daggered_rows()))
    for i, sp, se, rng, lv, why in spectra_nrange():
        print("   L%-6d %-8s %-22s n-range %-8s levels %-4s  %s" % (i, sp, se, rng, lv, why))

    print("\n5  A ROW TRUNCATED WHERE AN ESCAPED PIPE LOST WHAT IT ESCAPED")
    print("   (splitting on every pipe rather than on unescaped ones reports 23 of")
    print("    these; 22 are the compendia writing mathematics as \\|X\\| and are not")
    print("    defects.  The splitter's premise, not a fault of the volumes.)")
    for tag, i, cell in truncated_rows():
        print("   %-4s L%-6d ...%s" % (tag, i, cell))
    print("   the main volume's own copy of that row is whole:")
    for l in lines(MAIN):
        if "Six blindnesses of the closure" in l:
            print("        %s" % l.strip()[-72:])

    print("\n6  APPENDIX G -- THE PLAN'S THREE DEAD POINTERS DO NOT REPRODUCE")
    rows_g, hs_g, cited, ptrs, dead = appendix_g()
    seat = seated_entries()
    print("   table rows                               %d" % len(rows_g))
    print("   handles in the third column              %d, distinct %d" % (len(hs_g), len(set(hs_g))))
    mc = text(VOLS[0][1])
    print("   of those, printed nowhere in the MC      %d"
          % len([h for h in set(hs_g) if ("`%s`" % h) not in mc]))
    print("   Register entries cited                   %d" % len(cited))
    print("   of those, not seated                     %d" % len([n for n in cited if n not in seat]))
    print("   § pointers                               %s, unresolved %d" % (ptrs, len(dead)))
    print("   VERDICT: CLEAN.  A plan row that does not reproduce is not a finding.")

    print("\n7  THE BRACKET-SYSTEM OBJECT -- REGISTER 1880'S CLAIM, TESTED")
    cand, claims = bracket_system()
    print("   register 1880 states the compendium prints no such object   %s" % claims)
    print("   objects in families B and T naming one                      %d %s" % (len(cand), cand or ""))
    print("   VERDICT: the expansion is owed, exactly as 1880 records.  Writing it")
    print("   is an editorial act and is not done here.")

    print("\n8  THE INDEX OF INDICES' TOWER ROWS, AGAINST THE SEATED GENERATORS")
    rows_t, meas = tower_rows()
    for stage, cells, axes, comp, frac in rows_t:
        got = meas.get(stage)
        f = round(comp / cells, 4) if cells else 0.0
        print("   Λ%-3d printed %8s  measured %8s  %s | fraction %.4f printed %.4f %s"
              % (stage, "{:,}".format(cells), "{:,}".format(got) if got else "—",
                 "OK" if got == cells else ("no generator" if got is None else "DIFFERS"),
                 f, frac, "OK" if abs(f - frac) < 5e-5 else "DIFFERS"))
    print("   the composable column is NOT judged: the composition rule is stated in")
    print("   no member this instrument can import, and a figure it cannot derive it")
    print("   does not grade.")

    print("\n9  THE 285-OF-431 CHANNEL SENTENCE, AGAINST THE TABLE THAT ANSWERS IT")
    stated, untested, nrows = channel_sentence()
    print("   the Physics Compendium states           %d of %d channels unverified" % stated)
    print("   the Spectra Compendium's table holds    %d of %d rows reading 'untested'"
          % (untested, nrows))
    m = re.search(r"([\d,]+) channel rows — ([\d,]+) series of three or more members and "
                  r"([\d,]+) two-member channels", text(VOLS[3][1]))
    print("   and states its own extent as            %s rows = %s + %s"
          % (m.group(1), m.group(2), m.group(3)))
    print("   BOTH NUMBERS OF THE SENTENCE ARE OVERTAKEN.  The denominator moved when")
    print("   the parent-term wall and the J-resolved rows landed -- which the Spectra")
    print("   Compendium records against itself in the same paragraph as its own count")
    print("   -- and the Physics Compendium was not re-taken with it.")

    print("\nRECORDED, NOT REPAIRED.")


def selftest():
    ok = 0

    def chk(label, got, exp):
        nonlocal ok
        good = got == exp
        print("  %s  %-58s %s" % ("ok " if good else "FAIL", label, got))
        assert good, (label, got, exp)
        ok += 1

    # 1 -- the predecessor's row count, and the volume's
    head, data = spectra_rows()
    chk("eleven-cell non-separator rows, compendia.py's class", len(data) + 1, 597)
    chk("the first of them is the header", head[1][:2], ["species", "series"])
    chk("DATA rows, which is the volume's own 596", len(data), 596)
    chk("two-member (starred) channels", sum(1 for _, c in data if "*" in c[0]), 119)
    chk("series of three or more", sum(1 for _, c in data if "*" not in c[0]), 477)
    chk("and the volume prints the same three numbers",
        bool(re.search(r"596 channel rows — 477 series of three or more members and "
                       r"119 two-member channels", text(VOLS[3][1]))), True)
    dups = duplicated_keys()
    chk("duplicated keys, unchanged by the correction", len(dups), 9)
    chk("every duplicate a pair", sorted({len(v) for v in dups.values()}), [2])
    chk("in three species", sorted({k[0] for k in dups}), ["Ba III", "Ca II", "Si I"])

    # 2 -- the handle class on the volume's own codes
    fams = families()
    chk("the compendium's object families", len(fams), 18)
    chk("their stated objects sum to", sum(f[2] for f in fams), 299)
    objs = family_objects()
    chk("and each family holds what it states",
        [c for c, _, n in fams if len(objs[c]) != n], [])
    allh = set()
    tot = 0
    for _, name in VOLS:
        tk, br = handles(name)
        tot += len(tk) + len(br)
        allh |= {h for _, h in tk} | {h for _, h in br}
    chk("distinct handles in the four volumes", len(allh), 265)
    chk("which is the plan's figure, not compendia.py's 221", len(allh) == 265, True)
    chk("sites in the four volumes", tot, 417)
    mt, mb = handles(MAIN)
    chk("the main volume prints this many more", len(mt) + len(mb), 76)
    chk("of which backticked, all of them Appendix G's column", len(mt), 29)
    chk("and BARE, in running prose -- 'L.c8 is k >= 1'", len(mb), 47)
    for tag, name in VOLS[1:]:
        tk, br = handles(name)
        chk("none outside the Mathematical Compendium: " + tag, len(tk) + len(br), 0)
    rows, occ, dist = bibliography()
    chk("bibliography rows", len(rows), 162)
    chk("handle sites in its objects column", len(occ), 407)
    chk("distinct handles it names", len(dist), 265)
    chk("so outside that one column the compendia print", tot - len(occ), 10)
    chk("the word 'handle' occurs in the four volumes",
        sum(text(n).lower().count("handle") for _, n in VOLS), 0)

    # 3 -- ruling 11
    sc, seed = stated_counts()
    chk("front-matter register counts", [n for _, _, _, n, _ in sc], [299, 265, 248])
    chk("the MC and PC stamps name the same generator",
        sc[0][1] == sc[2][1] == "mathreg.py", True)
    chk("and the same date", sc[0][2] == sc[2][2] == "2026-08-12", True)
    chk("the cycle table's seed against the eighteen roots", seed, 17)
    chk("objects naming no work", 299 - len(dist), 34)

    # 4, 5
    bad = spectra_nrange()
    chk("channel rows carrying the dagger marker", len(daggered_rows()), 12)
    chk("which are not defects, and a first draft called them 13 faults",
        [b for b in bad if b[5] == "unparsable"], [])
    chk("channel rows whose n-range runs backwards", len(bad), 1)
    chk("and it is the row the plan files", (bad[0][0], bad[0][3]), (562, "41–5"))
    chk("its level count says the span should be", int(bad[0][4]), 15)
    tr = truncated_rows()
    chk("rows truncated at a lone backslash", len(tr), 1)
    chk("splitting on EVERY pipe instead would report",
        sum(1 for _, n in VOLS for l in lines(n) if l.strip().startswith("|")
            for cell in l.strip().strip("|").split("|")
            if cell.rstrip().endswith("\\") and cell.strip() != "\\"), 23)
    chk("and it is the row the plan files", (tr[0][0], tr[0][1]), ("IoI", 2021))
    chk("the main volume's copy of the same row is whole",
        "while \\|X\\| stays fixed." in text(MAIN), True)

    # 6 -- Appendix G
    rows_g, hs_g, cited, ptrs, dead = appendix_g()
    seat = seated_entries()
    mc = text(VOLS[0][1])
    chk("Appendix G data rows", len(rows_g), 30)
    chk("distinct handles in its third column", len(set(hs_g)), 29)
    chk("a pipe-split read loses one of them -- row 1.7's A.derived",
        "A.derived" in set(hs_g), True)
    chk("printed nowhere in the MC", [h for h in set(hs_g) if ("`%s`" % h) not in mc], [])
    chk("Register entries it cites", len(cited), 12)
    chk("of those, not seated -- the plan filed three", [n for n in cited if n not in seat], [])
    chk("its § pointers, all resolving", (ptrs, dead), (["2.15.2"], []))

    # 7
    cand, claims = bracket_system()
    chk("register 1880 states the object is absent", claims, True)
    chk("and families B and T name none", cand, [])

    # 8 -- the tower, measured through the seated generators
    rows_t, meas = tower_rows()
    chk("the IoI tower table's stages", [r[0] for r in rows_t], [8, 9, 10, 11, 12, 13])
    chk("printed cell counts", [r[1] for r in rows_t],
        [976, 1654, 2535, 13585, 70905, 199130])
    chk("measured by tower.py and tower3.py", [meas[r[0]] for r in rows_t],
        [976, 1654, 2535, 13585, 70905, 199130])
    chk("every printed fraction exact to four places",
        [r for r in rows_t if abs(round(r[3] / r[1], 4) - r[4]) >= 5e-5], [])

    # 9
    stated, untested, nrows = channel_sentence()
    chk("the Physics Compendium's unverified-channel sentence", stated, (285, 431))
    chk("the Spectra table's rows reading 'untested'", untested, 126)
    chk("over rows", nrows, 596)
    chk("which is the standing open item the corpus already names",
        untested == 126, True)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--selftest", action="store_true")
    a = a.parse_args()
    selftest() if a.selftest else report()
