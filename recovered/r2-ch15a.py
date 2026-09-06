#!/usr/bin/env python3
# r2-ch15a.py -- prose batch for the chat-103 section read: main L6991-L7116 (25.6 - 25.6.6).
# Pointers resolved to the CLAIM and not the heading; every token test runs on the RAW line,
# case-insensitively where a heading may carry the word capitalised, and word-bounded.
# Reads MEMBERS only, never a BUILDnnn bundle path. Imports r2lib by path; copies nothing.
# Rewritten once, four faults self-caught in the first version:
#   (a) head-truncated display hid the matched clause on long lines -- now a match window;
#   (b) 'thirty-five' was contaminated by "one thousand six hundred and thirty-five";
#   (c) the Register numeral sweep tested only the comma form -- now both;
#   (d) a failed token test located no alternative target -- claim-locators added at 1b.
import importlib.util, re

spec = importlib.util.spec_from_file_location("r2lib", "/home/claude/members/r2lib.py")
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
read_member, heading_line, section_span, enclosing = (
    r2lib.read_member, r2lib.heading_line, r2lib.section_span, r2lib.enclosing)

MAIN = read_member("The_Method_1_6-2.md").split("\n")
VOLS = [("main", MAIN)]
for tag, nm in (("register", "The_Method_1_6___The_Register-2.md"),
                ("math", "The_Method_1_6___Mathematical_Compendium-2.md"),
                ("physics", "The_Method_1_6___The_Physics_Compendium-2.md"),
                ("ioi", "The_Method_1_6___The_Index_of_Indices-2.md"),
                ("spectra", "The_Method_1_6___Spectra_Compendium-2.md")):
    VOLS.append((tag, read_member(nm).split("\n")))

U0, U1 = 6991, 7116                     # the unit, MEASURED by heading scan this chat

out = []
P = out.append


def hits(lines, pat, lo=1, hi=10 ** 9, flags=re.I):
    rx = re.compile(pat, flags)
    return [i for i, l in enumerate(lines, 1) if lo <= i <= hi and rx.search(l)]


def frag(lines, ln, pat, half=54):
    """the matched clause with its own context, not the head of a long line"""
    l = lines[ln - 1]
    m = re.search(pat, l, re.I)
    if not m:
        return l.strip()[:2 * half]
    a = max(0, m.start() - half // 2)
    return ("..." if a else "") + l[a:m.end() + half].strip()


def show(lines, ns, pat=r".", cap=4):
    for i in ns[:cap]:
        P("        L%-5d %s" % (i, frag(lines, i, pat)))
    if len(ns) > cap:
        P("        ... %d more" % (len(ns) - cap))


def where(lines, ns, cap=8):
    for i in ns[:cap]:
        e = enclosing(lines, i)
        P("        L%-5d in %-46s %s" % (i, str(e)[:46], frag(lines, i, r"\d", 30)[:74]))


P("r2-ch15a  prose batch  main L6991-L7116 (25.6 - 25.6.6)")
P("")

# ---- 1. every pointer in the unit, resolved to the claim --------------------------
P("1. POINTERS OUT OF THE UNIT, RESOLVED TO THE CLAIM")
POINTERS = [
    (7036, "2.13", r"committed under", [r"\bcommit", r"\bbound\b", r"before you look"]),
    (7069, "24.2", r"24\.2 records why", [r"Rule 4a", r"\bforbid", r"constant defect", r"\bwrong\b"]),
    (7097, "24.2", r"by .24\.2", [r"3\.5\s*%", r"\b17\s*%", r"tight end", r"cheap", r"isoelectronic"]),
    (7115, "24.6", r"deductive bracket", [r"\bdeductive\b", r"\bbracket\b", r"monoton"]),
]
for ln, sec, srcpat, toks in POINTERS:
    h, sp = heading_line(MAIN, sec), section_span(MAIN, sec)
    P("   L%d -> %s" % (ln, sec))
    P("        source clause: %s" % frag(MAIN, ln, srcpat, 60))
    if h is None or sp is None:
        P("        TARGET NOT RESOLVED"); continue
    lo, hi = sp
    P("        target L%d %-46s span L%d-L%d" % (h, MAIN[h - 1].strip()[:46], lo, hi))
    for t in toks:
        n = hits(MAIN, t, lo, hi)
        P("        %-18s %d site(s) in target%s" % (t, len(n), (" " + str(n[:5])) if n else ""))
P("")
P("1b. CLAIM-LOCATORS -- where the claims those pointers name actually live")
for pat, name in ((r"(?<![\d.])3\.5\s*%", "3.5%"), (r"(?<![\d.])17\s*%", "17%"),
                  (r"\bdeductive\b", "deductive"), (r"\btight end\b", "tight end")):
    n = hits(MAIN, pat)
    P("   %-10s %d main site(s):" % (name, len(n)))
    where(MAIN, n)
P("")

# ---- 2. docket 8 / 14m-01: the pointer INTO 25.6 with no target -------------------
P("2. DOCKET 8 (14m-01) -- 23.6's pointer INTO this unit")
P("   source L6319: %s" % frag(MAIN, 6319, r"abandon", 80))
for t in (r"\babandon", r"\bvariable", r"\bliterature", r"\bfield", r"\bneglect",
          r"\bdisuse", r"no longer", r"out of use", r"\bdropped", r"\bunfashionab",
          r"\bwhy\b", r"\bnobody\b"):
    n = hits(MAIN, t, U0, U1)
    P("   %-16s in 25.6: %d site(s)%s" % (t, len(n), (" " + str(n)) if n else ""))
n = hits(MAIN, r"\babandon")
P("   'abandon*' across the whole main volume: %d site(s) %s" % (len(n), n))
where(MAIN, n)
P("")

# ---- 3. docket 9 / 14x-07 live half: 'r < 5' sent to 25.6 -------------------------
P("3. 14x-07 LIVE HALF -- L6922 sends 'r < 5' to 25.6; tested in every form")
P("   source L6922: %s" % frag(MAIN, 6922, r"r < 5", 70))
for pat, name in ((r"r\s*<\s*5", "r < 5 (spaced or not)"), (r"\b5\s*:\s*1\b", "5:1"),
                  (r"\bratio\b", "ratio"), (r"\bfive\b", "five (word)"),
                  (r"\bseparat", "separat*"), (r"\bthreshold\b", "threshold"),
                  (r"\bexceeds?\b", "exceed(s)"), (r"\br\b\s*[=<>]", "r with a relation"),
                  (r"too close", "too close")):
    n = hits(MAIN, pat, U0, U1)
    P("   %-22s %d site(s) in 25.6%s" % (name, len(n), (" " + str(n)) if n else ""))
    if n and name == "five (word)":
        show(MAIN, n, r"\bfive\b", cap=3)
n = hits(MAIN, r"r\s*<\s*5")
P("   'r < 5' across the whole main volume: %d site(s) %s" % (len(n), n))
P("")

# ---- 4. the prediction / deduction vocabulary of the unit -------------------------
P("4. 'PREDICTION' AGAINST 'DEDUCTION' INSIDE THE UNIT")
for pat, name in ((r"\bpredict\w*", "predict*"), (r"\bdeduct\w*", "deduct*")):
    n = hits(MAIN, pat, U0, U1)
    P("   %-10s %d site(s): %s" % (name, len(n), n))
P("   the sites that carry a verdict on the word:")
for ln in (6991, 6992, 7039, 7040, 7042, 7087, 7093, 7111, 7115):
    P("      L%-5d %s" % (ln, MAIN[ln - 1].strip()[:112]))
P("")

# ---- 5. docket 15: the retired-basis phrases --------------------------------------
P("5. DOCKET 15 -- 'an earlier version', both cases, and the retirement phrases")
cap_ = hits(MAIN, r"An earlier version", flags=0)
low_ = hits(MAIN, r"an earlier version", flags=0)
P("   capitalised %d %s ; lower case %d %s ; case-insensitive %d"
  % (len(cap_), cap_, len(low_), low_, len(hits(MAIN, r"an earlier version"))))
for ln in sorted(set(cap_ + low_)):
    if U0 <= ln <= U1:
        P("      in this unit: L%-5d %s" % (ln, frag(MAIN, ln, r"earlier version", 70)))
for pat in (r"\bsupersed", r"\bwas wrong\b", r"\bnow forbids\b", r"\bcategory error\b",
            r"\bviolated it\b"):
    n = hits(MAIN, pat, U0, U1)
    P("   %-18s in unit: %d %s" % (pat, len(n), n))
P("")

# ---- 6. L7111's uniqueness claim, on the raw line --------------------------------
P("6. L7111 'the only place in this book where the mechanism is deployed prospectively'")
P("   L7111: %s" % MAIN[7110].strip()[:112])
dd = None
for tag, V in VOLS:
    n = [i for i, l in enumerate(V, 1) if "\u2145_def" in l]
    P("   %-9s D_def raw sites: %d%s" % (tag, len(n), (" " + str(n)) if n and len(n) <= 16 else ""))
    if tag == "main":
        dd = n
P("   where the main-volume D_def sites sit:")
where(MAIN, dd, cap=16)
n = hits(MAIN, r"prospectiv")
P("   'prospectiv*' main sites: %d %s" % (len(n), n))
show(MAIN, n, r"prospectiv", cap=4)
P("")

# ---- 7. attribution: Brudno, and Chapter 36 --------------------------------------
P("7. ATTRIBUTION (R-ATTR) -- Brudno, and the Chapter 36 pointer at L7000")
P("   L7000: %s" % MAIN[6999].strip()[:112])
for tag, V in VOLS:
    n = hits(V, r"\bBrudno\b")
    P("   %-9s Brudno: %d%s" % (tag, len(n), (" " + str(n)) if n else ""))
    show(V, n, r"Brudno", cap=2)
n = hits(MAIN, r"^#{1,3}\s*36\.")
P("   Chapter 36 headings in main: %s" % n)
n = hits(MAIN, r"E\(\u039b\u2083\)")
P("   'E(Lambda_3)' main sites: %d %s ; register %s ; math %s"
  % (len(n), n, hits(dict(VOLS)["register"], r"E\(\u039b\u2083\)"),
     hits(dict(VOLS)["math"], r"E\(\u039b\u2083\)")))
P("")

# ---- 8. the Register, before any figure is called unreproducible ------------------
P("8. THE REGISTER, GREPPED BEFORE ANY FIGURE IS CALLED UNREPRODUCIBLE")
REG = dict(VOLS)["register"]
for pat, name in ((r"735,?091", "735091/735,091"), (r"\b1,?398\b", "1398/1,398"),
                  (r"892,?700", "892700/892,700"), (r"736,?688", "736688/736,688"),
                  (r"Rule 4a", "Rule 4a"), (r"\bSc VI\b", "Sc VI"),
                  (r"\bSc\b", "Sc (word)"), (r"scandium", "scandium"),
                  (r"sulphur-like|sulfur-like", "sulphur-like")):
    n = hits(REG, pat)
    P("   register %-16s %d site(s)%s" % (name, len(n), (" " + str(n[:8])) if n else ""))
P("   the same numerals in the main volume, for contrast:")
for pat in (r"735,?091", r"\b1,?398\b", r"892,?700", r"Rule 4a"):
    P("      main %-12s %s" % (pat, hits(MAIN, pat)))
P("")

# ---- 9. single-witness sweep for this unit's figures ------------------------------
P("9. SINGLE-WITNESS SWEEP (six volumes, digit-bounded)")
FIGS = [r"892,700", r"1,594", r"2,169", r"1,398", r"736,688", r"735,860", r"737,380",
        r"738,547", r"784,416", r"785,209", r"784,128", r"784,605", r"735,091",
        r"2,687", r"1,520", r"1,081", r"13\.5743", r"91\.338", r"1\.0057", r"0\.9812",
        r"0\.9679", r"0\.9567", r"0\.9934", r"1\.0889", r"0\.9376"]
for pat in FIGS:
    tot = []
    for tag, V in VOLS:
        n = hits(V, r"(?<![\d,.])" + pat + r"(?![\d])")
        if n:
            tot.append("%s%s" % (tag, n if len(n) <= 6 else "[%d sites]" % len(n)))
    P("   %-10s %s" % (pat.replace("\\", ""), "; ".join(tot) or "NO SITE ANYWHERE"))
P("")

# ---- 10. 'thirty-five other species' -- decontaminated ---------------------------
P("10. L7005 'thirty-five other species' (compound numbers excluded)")
for tag, V in VOLS:
    n = [i for i in hits(V, r"thirty-five")
         if not re.search(r"(hundred and|thousand[^.]{0,24})thirty-five", V[i - 1], re.I)]
    P("   %-9s %d standalone site(s) %s" % (tag, len(n), n))
    show(V, n, r"thirty-five", cap=4)
P("")

# ---- 11. Ruling 45 class inside the unit ----------------------------------------
P("11. RULING 45 CLASS -- build or editorial-process remarks in a reader-facing volume")
for pat in (r"\breferee\b", r"the book states", r"\bthis work reported\b",
            r"\bstated here\b", r"\bcalling it one\b", r"\bthe book's own\b",
            r"\bnow stands\b", r"\bviolated it\b", r"\bthis book\b"):
    n = hits(MAIN, pat, U0, U1)
    if n:
        P("   %-24s -> %s" % (pat, n))
        show(MAIN, n, pat, cap=3)
P("")

# ---- 12. the two terms, and docket 18 -------------------------------------------
P("12. THE TERM OF THE TARGET LEVEL AGAINST THE TERM THE SECOND ROUTE USES")
for pat, name in ((r"\u00b3S\u00b0", "3S-odd (triplet)"), (r"\u2075S\u00b0", "5S-odd (quintet)"),
                  (r"\u2074S\u00b0", "4S-odd (the core)")):
    n = hits(MAIN, pat, U0, U1)
    P("   %-18s in unit: %d %s" % (name, len(n), n))
    show(MAIN, n, pat, cap=4)
P("   is the series term of d(4s) and d(5s) stated anywhere in the unit?")
n = hits(MAIN, r"\u03b4\(4s\)|\u03b4\(5s\)", U0, U1)
P("      d(4s)/d(5s) sites: %s" % n)
show(MAIN, n, r"\u03b4\(4s\)", cap=4)
P("   docket 18 -- do any of the seven headings finish their sentence in the body?")
for h in (6991, 7003, 7021, 7039, 7059, 7071, 7093):
    P("      L%-5d %-50s | next: %s" % (h, MAIN[h - 1].strip()[:50], MAIN[h].strip()[:52]))
P("")

# ---- 13. the figure asset ------------------------------------------------------
P("13. FIGURE 25.2 (L7085) -- asset and caption")
P("   L7085: %s" % MAIN[7084].strip())
for nm in ("FIGURE_ASSETS.md", "FIGURE_MAP.md"):
    t = read_member(nm).split("\n")
    n = [i for i, l in enumerate(t, 1) if "25.2" in l]
    P("   %-18s names figure 25.2 at %s" % (nm, n or "NO LINE"))
    show(t, n, r"25\.2", cap=2)
P("   MEASURED image line in the main member: %s" % hits(MAIN, r"figure-25\.2\.png"))
P("")
P("end r2-ch15a")
print("\n".join(out))
