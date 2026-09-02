"""r2-ch16i --- PROSE batch, chat 119, main L8700-L8789 (§31.3 - §31.3.4).

Pointers under both resolvers, the stale 24.3.4.x sub-numbering, attributions against the BODY
occurrence of ## References and R.7, count words against their own bodies, the §30.4.2 charge
against the section it charges, Rulings 45 and 46, a digit-bounded numeral SITE sweep over six
volumes, the duplicated-section sweep, census rows in range, and Prints & Proofs anchored on its
own text.  r2lib by path; members read, never a bundle.
"""
import importlib.util, re

spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing

LO, HI = 8700, 8789
VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open('/home/claude/members/' + f, encoding='utf-8').read().split('\n') for k, f in VOL.items()}
M = V['main']
R = V['reg']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
NUMB = r'(?<![\d.,])%s(?!\d)(?!,\d)(?!\.\d)'          # both boundaries corrected, chats 116-117


def body_range(Mx, sec):
    """[start, end) of a section's OWN body.  Owed to r2lib; provenance chat 108."""
    s = heading_line(Mx, sec)
    if s is None:
        return None
    for i in range(s + 1, len(Mx) + 1):
        if re.match(r'^#{1,4} ', Mx[i - 1].strip()):
            return (s, i)
    return (s, len(Mx) + 1)


def last_md_heading(Mx, title):
    """LAST line whose heading text is exactly `title` --- the BODY occurrence.  Owed to r2lib."""
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(title) + r'\s*$', t.strip())]
    return hits[-1] if hits else None


def lettered_heading(Mx, label):
    hits = [i for i, t in enumerate(Mx, 1)
            if re.match(r'^#{1,4}\s+' + re.escape(label) + r'[ .]', t.strip())]
    return hits[-1] if hits else None


def stemlines(L, s):
    """Left-bounded only: has_token is letter-bounded on BOTH sides.  Provenance chat 113."""
    return [i for i, t in enumerate(L, 1) if re.search(r'(?<![A-Za-z])' + re.escape(s), t, re.I)]


def numsites(pat):
    """Every SITE of a numeral, six volumes.  A count alone cannot be witnessed."""
    out = {}
    for k, L in V.items():
        s = [i for i, t in enumerate(L, 1) if re.search(NUMB % re.escape(pat), t)]
        if s: out[k] = s
    return out


print('=' * 100)
print('r2-ch16i  PROSE  chat 119  main L%d-L%d  (§31.3 - §31.3.4)' % (LO, HI))
print('=' * 100)

# ------------------------------------------------------------------ 1. pointers
print('\n## 1  EVERY POINTER IN THE UNIT, under body_range AND section_span, resolved to the CLAIM')
ptr = set()
for i in range(LO, HI + 1):
    for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)', M[i - 1]):
        ptr.add((m.group(1), i))
    for m in re.finditer(r'§([A-Z]\.\d+(?:\.\d+)*)', M[i - 1]):
        ptr.add((m.group(1), i))
for sec, at in sorted(ptr):
    br = body_range(M, sec)
    try:
        sp = section_span(M, sec) if sec.count('.') == 0 else None
    except Exception:
        sp = None
    print('   §%-9s cited at L%d   body_range %s   section_span %s%s'
          % (sec, at, br, sp, '   (COINCIDE)' if (br and sp and br == sp) else ''))
    if br:
        body = [(j, M[j - 1].strip()) for j in range(br[0] + 1, br[1]) if M[j - 1].strip()]
        for j, t in body[:6]:
            print('        L%-6d %s' % (j, t[:104]))
        if len(body) > 6:
            print('        ... %d further body lines' % (len(body) - 6))

print('\n   Word-pointers in the unit (no § sign), resolved by hand-named target:')
for lab, pat in (('Chapter 6', r'Chapter 6\b'), ('§10 / "what §10 says"', r'§10\b'),
                 ('item D', r'item D\b'), ('the fourth falsification test', r'fourth falsification')):
    hits = [i for i in range(LO, HI + 1) if re.search(pat, M[i - 1])]
    print('      %-30s sites in unit %s' % (lab, hits))

# ------------------------------------------------------------------ 2. the stale sub-numbering
print('\n## 2  THE SUB-NUMBERING INSIDE §31.3.4  --- 24.3.4.x IN CHAPTER 31')
sub = [(i, M[i - 1].rstrip()) for i in range(LO, HI + 1) if re.match(r'^\s*\d+\.\d+\.\d+\.\d+\s', M[i - 1])]
for i, t in sub:
    print('   L%-6d %r' % (i, t[:96]))
    print('          markdown heading? %s' % bool(re.match(r'^#{1,6}\s', t.strip())))
print('   enclosing section of these lines: §%s' % (enclosing(M, sub[0][0]) if sub else 'n/a'))
for lab in ('24.3.4', '24.3', '24.3.4.1', '31.3.4.1'):
    print('   heading_line(main, %-9s) = %s' % (lab, heading_line(M, lab)))
print('   every 24.3.4.x site in six volumes:')
for k, L in V.items():
    s = [i for i, t in enumerate(L, 1) if re.search(r'(?<![\d.])24\.3\.4\.\d', t)]
    if s:
        print('      %-5s %s' % (k, s))
print('   the same shape elsewhere in the main volume (an N.N.N.N line whose enclosing chapter')
print('   differs from its own first number):')
odd = []
for i, t in enumerate(M, 1):
    m = re.match(r'^\s*(\d+)\.\d+\.\d+\.\d+\s', t)
    if m:
        enc = enclosing(M, i)
        if enc and str(enc).split('.')[0] != m.group(1):
            odd.append((i, m.group(1), enc, t.strip()[:60]))
print('      %d such lines: %s' % (len(odd), odd[:12]))

# ------------------------------------------------------------------ 3. attributions
print('\n## 3  ATTRIBUTIONS AGAINST ## References (BODY occurrence) AND R.7')
refs = last_md_heading(M, 'References')
r7 = lettered_heading(M, 'R.7')
print('   ## References BODY occurrence L%s   (all occurrences: %s)'
      % (refs, [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4}\s+References\s*$', t.strip())]))
print('   R.7 at L%s' % r7)
refbody = range(refs, len(M) + 1) if refs else []
NAMES = ['Batyrev', 'Kreuzer', 'Skarke', 'Klemm', 'Candelas', 'Ossa', 'Szendroi', 'Triadophilia', 'ATMP']
for n in NAMES:
    inunit = [i for i in range(LO, HI + 1) if re.search(r'(?<![A-Za-z])' + n, M[i - 1], re.I)]
    inrefs = [i for i in refbody if re.search(r'(?<![A-Za-z])' + n, M[i - 1], re.I)]
    allmain = stemlines(M, n)
    print('   %-13s unit %s   References/R.7 %s   main-volume sites %d   %s'
          % (n, inunit, inrefs, len(allmain), 'BIBLIOGRAPHED' if inrefs else 'UNBIBLIOGRAPHED'))
    if not inrefs:
        other = {k: len(stemlines(L, n)) for k, L in V.items() if k != 'main' and stemlines(L, n)}
        print('        other volumes: %s' % (other or 'none'))
print('   "He" is not swept: a two-letter surname cannot be word-bounded against ordinary prose.')
print('   It is recorded as an author of the Triadophilia citation and carried with that citation.')

# ------------------------------------------------------------------ 4. count words
print('\n## 4  COUNT WORDS AGAINST THEIR OWN BODIES')
print('   L8705 "three published counts": the colon list at L8707-L8708 enumerates')
lst = M[8706].strip() + ' ' + M[8707].strip()
print('        %s' % lst[:150])
enum = [s for s in lst.split('·') if re.search(r'\d{2,3},\d{3}', s) and '=' not in s]
print('        counts enumerated before the derived 1,095: %d  -> "three published counts" %s'
      % (len(enum), 'HOLDS' if len(enum) == 3 else 'DEVIATION'))
print('        (the test is of counts published, not of DISTINCT VALUES: two of the three share')
print('         the value 248,305, and a distinct-value test would have scored this true claim')
print('         false.  Self-caught, chat 119.)')
print('   L8783 "The 24 excluded values": the same sentence lists 12 values (see r2-ch16h §3)')
print('   L8770 "two named confirmations": L8768 names %d'
      % len(re.findall(r'X[\u2080-\u2089\d,_]*', M[8767])))
print('        L8768 raw: %s' % M[8767].strip()[:120])
print('   L8748 "5 -- only 0, +/-2, +/-4": measured EXACT in r2-ch16h §5')
print('   L8755 "The fourth falsification test": every "falsification test" site in the main volume')
fs = stemlines(M, 'falsification test')
print('        %s' % fs)
for i in fs:
    print('        L%-6d %s' % (i, M[i - 1].strip()[:100]))

# ------------------------------------------------------------------ 5. the §30.4.2 charge
print('\n## 5  §30.4.2"S TABLE ROW AGAINST THE SECTION IT CHARGES  (16g-04 measured at its target)')
print('   L8604: %s' % M[8603].strip()[:140])
print('   §31.3.3 heading L8720: %s' % M[8719].strip())
for i in range(8720, 8728):
    if M[i - 1].strip():
        print('        L%-6d %s' % (i, M[i - 1].strip()[:110]))
print('   The charge is "stated against the wrong denominator"; the section it names states the')
print('   statistic against the RIGHT denominator and names the wrong one to reject it.')

# ------------------------------------------------------------------ 6. Rulings 45 and 46
print('\n## 6  RULING 45 (build / editorial-process remarks) AND RULING 46 (script, build, file refs)')
R45 = ['this session', 'this book', 'an earlier version', 'an earlier draft', 'a previous draft',
       'now states', 'has grown since', 'the audit itself', 'an afternoon', 'could not read',
       'the file is missing', 'this chapter', 'what remains of item']
for p in R45:
    s = [i for i in range(LO, HI + 1) if p in M[i - 1].lower()]
    if s:
        for i in s:
            print('   R45  L%-6d %-22s %s' % (i, '"' + p + '"', M[i - 1].strip()[:96]))
R46 = ['BUILD', '.py', '.md', '.tsv', 'gate.py', 'close.py', 'register_cites', 'tower-2']
hit46 = [(i, p) for i in range(LO, HI + 1) for p in R46 if re.search(r'(?<![A-Za-z])' + re.escape(p), M[i - 1])]
print('   R46 sites in unit (case-sensitive): %s' % (hit46 or 'ZERO'))
fp = [i for i in range(LO, HI + 1)
      if re.search(r'(?<![A-Za-z])(I|me|my|we|our|us)(?![A-Za-z])', M[i - 1])]
print('   first-person pronoun sites: %s' % (fp or 'ZERO'))
for i in fp:
    print('        L%-6d %s' % (i, M[i - 1].strip()[:100]))

# ------------------------------------------------------------------ 7. numeral sites
print('\n## 7  DIGIT-BOUNDED NUMERAL SITES, SIX VOLUMES  (sites, never counts)')
for pat in ('473,800,776', '30,108', '248,305', '495,515', '1,095', '21,528', '540', '498',
            '589', '208', '232', '112', '502', '36', '976'):
    print('   %-12s %s' % (pat, numsites(pat)))

# ------------------------------------------------------------------ 8. the 36 and the belt's six
print('\n## 8  "THE PERIODIC TABLE"S 36" AND "THE BELT"S SIX", against the book"s own statements')
for i in stemlines(M, 'periodic table')[:40]:
    if re.search(NUMB % '36', M[i - 1]):
        print('   36  L%-6d %s' % (i, M[i - 1].strip()[:110]))
belt = stemlines(M, 'belt')
print('   "belt" sites in the main volume: %s' % belt)
for i in belt[:10]:
    print('        L%-6d %s' % (i, M[i - 1].strip()[:110]))

# ------------------------------------------------------------------ 9. §31.3 as a heading
print('\n## 9  §31.3 ITSELF  --- body lines between its heading and the next')
br = body_range(M, '31.3')
print('   §31.3 body_range %s   non-blank body lines: %s'
      % (br, [j for j in range(br[0] + 1, br[1]) if M[j - 1].strip()]))
print('   comparison, the other parent sections of chapters 30-31:')
for s in ('30.4', '31.1', '31.2', '31.3'):
    b = body_range(M, s)
    print('      §%-5s %s   non-blank body lines %d' % (s, b, len([j for j in range(b[0] + 1, b[1]) if M[j - 1].strip()])))

# ------------------------------------------------------------------ 10. duplicated-section sweep
print('\n## 10  DUPLICATED-SECTION SWEEP (DEF-105 item 1) over this unit"s long lines')
longs = [(i, M[i - 1].strip()) for i in range(LO, HI + 1) if len(M[i - 1].strip()) >= 60]
dup = []
for i, t in longs:
    for k, L in V.items():
        for j, u in enumerate(L, 1):
            if u.strip() == t and not (k == 'main' and j == i):
                dup.append((i, k, j))
print('   %d long lines swept, %d recurrences: %s' % (len(longs), len(dup), dup or 'NONE'))

# ------------------------------------------------------------------ 11. census rows in range
print('\n## 11  DEFECT-CENSUS.tsv ROWS IN RANGE  (keyed on the column named `member`, every class)')
cen = open('/home/claude/members/DEFECT-CENSUS.tsv', encoding='utf-8').read().split('\n')
hdr = cen[0].split('\t')
print('   header: %s' % hdr)
mi, li = hdr.index('member'), hdr.index('line')
print('   distinct member values: %s' % sorted({r.split('\t')[mi] for r in cen[1:] if r.strip()}))
rows = []
for r in cen[1:]:
    if not r.strip():
        continue
    f = r.split('\t')
    if f[mi] in ('main', 'all') and f[li].isdigit() and LO <= int(f[li]) <= HI:
        rows.append(f)
print('   rows in L%d-L%d, classes main AND all: %d' % (LO, HI, len(rows)))
print('   (HANDOFF-70 named two rows for chat 118 and there were three: every class is swept,')
print('    not the class a handoff names.)')
for f in rows:
    print('      %s' % ' | '.join(x[:60] for x in f))

# ------------------------------------------------------------------ 12. Prints & Proofs
print('\n## 12  PRINTS & PROOFS, ANCHORED ON ITS OWN TEXT  (no global offset)')
for probe in ('The Calabi', 'Batyrev', 'Triadophilia', 'split bicubic', 'The 24 excluded values',
              '24.3.4.1', 'thinly populated', 'an afternoon'):
    mm = [i for i in range(LO, HI + 1) if probe in M[i - 1]]
    pp = [i for i, t in enumerate(PP, 1) if probe in t]
    off = [p - m for m in mm for p in pp] if (mm and pp) else []
    print('   %-24s main %s   PP %s   offset %s'
          % ('"' + probe + '"', mm, pp, sorted(set(off)) if off else ('PP ABSENT' if mm else 'no main site')))
print('   A probe scoring zero on the MAIN volume is a broken probe, not a finding (chat 118).')

# ------------------------------------------------------------------ 13. cross-site
print('\n## 13  THE SAME MATERIAL RESTATED ELSEWHERE IN THE MAIN VOLUME  (found by the numeral sweep)')
print('   Appendix item D, L11069-L11078, restates the whole slice.  Line by line against §31.3.4:')
for i in (11069, 11070, 11071, 11072, 11073, 11074, 11076):
    print('      L%-6d %s' % (i, M[i - 1].strip()[:132]))
tw = [i for i in range(1, len(M) + 1) if re.search(r'twelve exclusions', M[i - 1], re.I)]
tf = [i for i in range(1, len(M) + 1) if re.search(r'24 excluded values', M[i - 1])]
print('   "twelve exclusions" sites %s   vs   "24 excluded values" sites %s' % (tw, tf))
print('   -> CONTRADICTION INSIDE ONE VOLUME: L%d prints twelve, L%d prints 24, of one set of'
      % (tw[0], tf[0]))
print('      exclusions.  Twelve is correct (r2-ch16h §3); 24 is the cell count.')
print('   register 387 (reg L1437) is cited by L11070 for this slice; its headline reproduces')
print('   208 / 540 / 498 / 498 / 21,528 / five / 112 / 26-262 and "all three falsification')
print('   tests hold at 540 of 540" -- EXACT and on point.  Recorded as a negative witness.')

print('\n## 14  THE TRIADOPHILIA CITATION, TEXT AGAINST BIBLIOGRAPHY')
print('   text  L8732: %s' % M[8731].strip()[:150])
print('   bibl  L11804: %s' % M[11803].strip()[:150])
print('   authors named in the text but not in the bibliography entry: He, Szendroi')
print('   author named in the bibliography entry but not in the text: Rodriguez-Villegas')
print('   years: text 2008 (journal), bibliography 2007 (preprint) -- both defensible for one work;')
print('   the AUTHOR LISTS cannot both be right.  Flagged for repair, docket 16 and docket 36.')
print('   Huang & Taylor L11801 says its counts are "used in §31.3.1"; §31.3.1 L8703-L8708 names')
print('   no source for them -- the reverse-direction sweep, bibliography to text.')

print('\n## 15  TWO CITED CRITERIA, READ IN FULL AT THEIR TARGETS')
print('   §16.7.1"s criterion as printed:')
for i in (4585, 4593, 4614, 4615):
    print('      L%-6d %s' % (i, M[i - 1].strip()[:126]))
print('   §31.3.2 invokes it at L8716-L8718:')
for i in (8716, 8717, 8718):
    print('      L%-6d %s' % (i, M[i - 1].strip()[:126]))
print('   -> the printed discriminator is RE-COORDINATISATION; §31.3.2 states the absence is not')
print('      removable by re-coordinatising and still draws the "defect of the index" conclusion.')
print('   §10 (span L2021-L2074, all four subsections read) against L8785"s claim about it:')
for p in ('structural', 'accidental', 'normal form'):
    s = [i for i in range(2021, 2075) if re.search(p, M[i - 1], re.I)]
    print('      "%s" in §10: %s' % (p, s or 'ZERO SITES'))
print('      L8785: %s' % M[8784].strip()[:126])
print('   -> §10 defines the void and counts it; it makes no structural/accidental distinction and')
print('      states no normal-form behaviour.  Sweep covered the whole span, not a token probe.')
print('\n' + '=' * 100)
