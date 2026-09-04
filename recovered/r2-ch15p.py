#!/usr/bin/env python3
"""r2-ch15p — computable batch for the chat-111 section read:
main L7856-L7939 (§29, §29.1, §29.2, §29.2.1, §29.2.2) with L8222-L8237 (§28.10).

Counts, figures, register-entry existence, the Q index, the eight orphaned references
and the printed section order.  Prose, pointers and rulings are r2-ch15q.

Resolvers from r2lib by path.  body_range, the grouped-aware register lookup, the
digit-bounded numeral sweep and the two-line join are carried verbatim with provenance
comments (r2lib owes all four).
"""
import importlib.util, os, re

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = (
    r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing)

VOLS = {
    'main':    'The_Method_1_6-2.md',
    'reg':     'The_Method_1_6___The_Register-2.md',
    'mc':      'The_Method_1_6___Mathematical_Compendium-2.md',
    'pc':      'The_Method_1_6___The_Physics_Compendium-2.md',
    'ioi':     'The_Method_1_6___The_Index_of_Indices-2.md',
    'spectra': 'The_Method_1_6___Spectra_Compendium-2.md',
}
V = {k: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for k, f in VOLS.items()}
M, REG = V['main'], V['reg']
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')

A0, A1 = 7856, 7939          # §29 .. §29.2.2
B0, B1 = 8222, 8237          # §28.10, printed inside chapter 29
UNIT = M[A0 - 1:A1] + M[B0 - 1:B1]


# provenance: owed to r2lib since chat 105 (heading to the NEXT heading of ANY rank).
def body_range(lines, sec):
    s = heading_line(lines, sec)
    if s is None:
        return None
    for i in range(s + 1, len(lines) + 1):
        if re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', lines[i - 1].strip()):
            return (s, i)
    return (s, len(lines) + 1)


# provenance: owed to r2lib since chat 108.  '^#{1,4}\s*N\s*$' misses '### 203, 215, 218, ...'.
def register_entry(n):
    bare = re.compile(r'^#{1,4}\s*%d\s*$' % n)
    grp = re.compile(r'^#{1,4}\s*\d+(\s*,\s*\d+)+\s*$')
    for i, t in enumerate(REG, 1):
        if bare.match(t.strip()):
            return ('bare', i)
        if grp.match(t.strip()) and n in [int(x) for x in re.findall(r'\d+', t)]:
            return ('grouped', i)
    return (None, None)


def headline(i):
    for t in REG[i:i + 8]:
        if t.strip():
            return re.sub(r'\s+', ' ', t.strip())[:118]
    return ''


# provenance: owed to r2lib since chat 109 — a numeral sweep must be digit-bounded, or
# 185 matches inside 1850 and 12.14 inside 112.14.
def numeral_sites(lines, s):
    pat = re.compile(r'(?<![\d.])' + re.escape(s) + r'(?![\d])')
    return [i for i, t in enumerate(lines, 1) if pat.search(t)]


# provenance: owed to r2lib since chat 107 — a phrase may straddle a wrapped line.
def join_sites(lines, phrase):
    p = phrase.lower()
    raw = [i for i, t in enumerate(lines, 1) if p in re.sub(r'\s+', ' ', t).lower()]
    jn = []
    for i in range(1, len(lines)):
        j = re.sub(r'\s+', ' ', lines[i - 1] + ' ' + lines[i]).lower()
        if p in j and i not in raw and (i + 1) not in raw:
            jn.append(i)
    return raw, jn


out = []
P = out.append
P('r2-ch15p — computable batch, main L7856-L7939 (§29-§29.2.2) + L8222-L8237 (§28.10)')
P('unit lines: %d + %d = %d' % (A1 - A0 + 1, B1 - B0 + 1, len(UNIT)))

# ---------------------------------------------------------------- 1. count words
P('')
P('1. COUNT WORDS AGAINST THE ITEMS THEY INTRODUCE')

# 1a. "Three things, and each has a truth value" (L7872) -> the bold leads of §29.2
leads = [(i, re.sub(r'\s+', ' ', M[i - 1].strip())[:60])
         for i in range(7872, 7904) if re.match(r'^\s*\*\*[A-Z][A-Z ,\'’]+\.?\*\*', M[i - 1])]
P('1a  L7872 "Three things"                    bold leads in §29.2 body: %d' % len(leads))
for i, t in leads:
    P('      L%-5d %s' % (i, t))

# 1b. "Four independent owners" (L7890) -> the blockquote's named owners vs the table row
quote = ' '.join(M[i - 1] for i in range(7890, 7894))
owners_quote = [n for n in ('Moore', 'Manski', 'Shannon', 'IEEE') if has_token(quote, n)]
row = M[7883 - 1]
owners_row = [n for n in ('Moore', 'Manski', 'Shannon', 'IEEE') if has_token(row, n)]
P('1b  L7890 "Four independent owners"         named in the blockquote L7890-7893: %d %s'
  % (len(owners_quote), owners_quote))
P('      table row L7883                        names: %d %s' % (len(owners_row), owners_row))

# 1c. "Those five are checkable" (L7902) -> the frame table rows
frame = [i for i in range(7896, 7902) if M[i - 1].strip().startswith('does it')]
P('1c  L7902 "Those five are checkable"        rows beginning "does it": %d (L%s)'
  % (len(frame), ','.join(str(x) for x in frame)))

# 1d. "Eight references were orphaned" (L8224) -> the names listed
names = ['Lubiw', 'Anstee', 'Kuznetsov', 'Caspard', 'Colomb', 'Hoffman',
         'Van Isacker', 'Chandrasekaran & Flanagan']
listed = ' '.join(M[i - 1] for i in range(8224, 8227))
found = [n for n in names if n.lower() in re.sub(r'\s+', ' ', listed).lower()]
P('1d  L8224 "Eight references were orphaned"  names listed: %d of %d %s'
  % (len(found), len(names), '' if len(found) == len(names) else set(names) - set(found)))

# 1e. "six of the eleven items in Q" (L7911) -> the letters listed
letters = re.findall(r'\b([A-Z])\b', M[7912 - 1] + ' ' + M[7913 - 1])
letters = [c for c in letters if c not in ('Q', 'E')]
P('1e  L7911 "six of the eleven items in Q"    letters printed: %d %s' % (len(letters), letters))

# ---------------------------------------------------------------- 2. the Q index
P('')
P('2. THE Q INDEX — does it have eleven items, and are B, C, F, G, K, N among them?')
qsites = []
for k, lines in V.items():
    for i, t in enumerate(lines, 1):
        if re.search(r'\bQ\b', t) and re.search(r'\b(eleven|open question)', t, re.I):
            qsites.append((k, i, re.sub(r'\s+', ' ', t.strip())[:104]))
for k, i, t in qsites[:14]:
    P('  %-8s L%-6d %s' % (k, i, t))
# the item lettering, wherever Q's items are enumerated
qitem = re.compile(r'^\s*\**([A-Z])\**[.)]\s')
for k in ('ioi', 'main'):
    lines = V[k]
    for i, t in enumerate(lines, 1):
        if re.search(r'index of open questions|\bQ\b.{0,40}\bitems\b', t, re.I):
            blk = [qitem.match(x).group(1) for x in lines[i:i + 40] if qitem.match(x)]
            if blk:
                P('  %-8s L%-6d item letters after this line: %d %s' % (k, i, len(blk), blk))
            break

# ---------------------------------------------------------------- 3. the search figures
P('')
P('3. THE SEARCH FIGURES OF L7867 AND L7874 AGAINST THE CHAPTER ITSELF')
for sec, want in (('29.6', 'three documents we could not reach'),
                  ('29.7', 'entered literatures'),
                  ('29.10', 'two searches run'),
                  ('29.12', 'five unlocated results')):
    hl = heading_line(M, sec)
    br = body_range(M, sec)
    P('  §%-6s heading L%-6s body %s   %s' % (sec, hl, br, re.sub(r'\s+', ' ', M[hl - 1].strip())[:70]))
for fig, claim in (('Nine', 'literatures entered'), ('nine', 'further named and unentered'),
                   ('six', 'targets not found'), ('seven', 'prior results found incidentally')):
    raw, jn = join_sites(M, claim)
    P('  "%s %s"  sites: raw %s  join %s' % (fig, claim, raw[:6], jn[:6]))
# the entered literatures, enumerated in §29.7
b = body_range(M, '29.7')
if b:
    ent = [i for i in range(b[0], b[1]) if re.match(r'^\s*\**\d+[.)]', M[i - 1])]
    P('  §29.7 body L%d-%d: numbered lines %d %s' % (b[0], b[1] - 1, len(ent), ent[:12]))

# ---------------------------------------------------------------- 4. attribution table
P('')
P('4. THE ATTRIBUTION TABLE (L7876 "Every component of this work has an owner")')
rows = [i for i in range(7878, 7890)
        if M[i - 1].startswith('  ') and M[i - 1].strip() and not M[i - 1].strip().startswith('**')]
P('  indented table lines L7878-L7889: %d' % len(rows))
cont = [i for i in rows if not re.search(r'\S\s\s+\S', M[i - 1])]
P('  lines with no second column (continuations): %s' % cont)
P('  component rows = %d' % (len(rows) - len(cont) - 1))
for i in rows:
    P('    L%-5d %s' % (i, re.sub(r'\s\s+', ' | ', M[i - 1].strip())[:96]))

# ---------------------------------------------------------------- 5. register size
P('')
P('5. THE REGISTER\'S OWN SIZE — L7900 prints it in words')
bare = grp = 0
nums = set()
for t in REG:
    s = t.strip()
    if re.match(r'^#{1,4}\s*\d+\s*$', s):
        bare += 1; nums.add(int(re.findall(r'\d+', s)[0]))
    elif re.match(r'^#{1,4}\s*\d+(\s*,\s*\d+)+\s*$', s):
        grp += 1; nums.update(int(x) for x in re.findall(r'\d+', s))
P('  bare headings %d · grouped headings %d · distinct entry numbers %d · max %d'
  % (bare, grp, len(nums), max(nums)))
for s in ('1,635', '1635', '1,631', '1631', '1,628', '1628', '1,660', '1660'):
    hits = {k: numeral_sites(lines, s) for k, lines in V.items()}
    hits = {k: v for k, v in hits.items() if v}
    if hits:
        P('  %-6s %s' % (s, {k: v[:6] for k, v in hits.items()}))
raw, jn = join_sites(M, 'one thousand six hundred and thirty-five')
P('  spelled form "one thousand six hundred and thirty-five": raw %s join %s' % (raw, jn))
for k, lines in V.items():
    r2, j2 = join_sites(lines, 'one thousand six hundred and thirty-five')
    if r2 or j2:
        P('    %-8s raw %s join %s' % (k, r2, j2))

# ---------------------------------------------------------------- 6. register citations
P('')
P('6. REGISTER CITATIONS MADE BY THE UNIT — existence first, then the headline')
for n in (238, 335, 658, 659):
    kind, i = register_entry(n)
    P('  register %-4d %-8s L%-7s %s' % (n, kind or 'ABSENT', i or '-', headline(i) if i else ''))

# ---------------------------------------------------------------- 7. figures
P('')
P('7. FIGURES OF §29.2.2 — other sites in six volumes')
for s in ('12.14', '185', '4ν/3'):
    hits = {}
    for k, lines in V.items():
        h = numeral_sites(lines, s) if s != '4ν/3' else [
            i for i, t in enumerate(lines, 1) if '4ν/3' in t]
        if h:
            hits[k] = h[:8]
    P('  %-7s %s' % (s, hits))

# ---------------------------------------------------------------- 8. orphaned references
P('')
P('8. THE EIGHT ORPHANED REFERENCES — "Each is now cited where its finding is" (L8226)')
homes = {'Lubiw': '30.3.9', 'Anstee': '30.3.9', 'Kuznetsov': '14.6', 'Caspard': '14.6',
         'Colomb': '14.6', 'Hoffman': '12.11', 'Van Isacker': '30.3',
         'Chandrasekaran': '12.11', 'Flanagan': '12.11'}
for nm in ('Lubiw', 'Anstee', 'Kuznetsov', 'Caspard', 'Colomb', 'Hoffman',
           'Van Isacker', 'Chandrasekaran', 'Flanagan'):
    sites = [i for i, t in enumerate(M, 1) if nm.lower() in t.lower()]
    encl = sorted({str(enclosing(M, i)) for i in sites})
    P('  %-15s main sites %-2d %s' % (nm, len(sites), sites[:8]))
    P('  %-15s enclosing  %s' % ('', encl[:8]))
P('  the four homes the sentence names:')
for sec in ('30.3.9', '14.6', '30.3', '12.11'):
    P('    §%-8s heading %s   body %s' % (sec, heading_line(M, sec), body_range(M, sec)))

# ---------------------------------------------------------------- 9. printed order
P('')
P('9. PRINTED SECTION ORDER AROUND §28.10 (docket 29)')
seq = [(i, re.sub(r'\s+', ' ', M[i - 1].strip())[:64])
       for i in range(8100, 8330) if re.match(r'^#{1,4} \d', M[i - 1])]
for i, t in seq:
    P('  L%-6d %s' % (i, t))
P('  contents list sites for chapter 28 and 29:')
for i in range(140, 160):
    if re.match(r'^#{1,4} 2[89]\.', M[i - 1]):
        P('    L%-5d %s' % (i, M[i - 1].strip()[:72]))
P('  §28.10 heading sites in main: %s' % [i for i, t in enumerate(M, 1)
                                          if re.match(r'^#{1,4}\s*28\.10\b', t)])

# ---------------------------------------------------------------- 10. PP witness
P('')
P('10. PRINTS & PROOFS WITNESS FOR THE UNIT')
for sec in ('29', '29.1', '29.2', '29.2.1', '29.2.2', '28.10'):
    hl = heading_line(PP, sec)
    br = body_range(PP, sec)
    n = None if br is None else sum(1 for t in PP[br[0]:br[1] - 1] if t.strip())
    P('  §%-7s PP heading %-7s body %-14s non-blank body lines %s' % (sec, hl, br, n))
for ph in ('one thousand six hundred and thirty-five', 'Four independent owners',
           'Eight references were orphaned', 'six of the eleven items'):
    raw, jn = join_sites(PP, ph)
    P('  PP "%s": raw %s join %s' % (ph[:44], raw, jn))

print('\n'.join(out))
