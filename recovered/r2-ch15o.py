#!/usr/bin/env python3
"""r2-ch15o — prose batch for the chat-110 section read, main L7721-L7855
(§28.8, §28.9, §28.9.1).  Pointers, register citations, rulings 45/46, PP witness,
single-witness sweep, formatting classes.

Resolvers from r2lib by path.  body_range, the grouped-aware register lookup and the
two-line-join phrase sweep are carried verbatim with provenance comments (r2lib owes all three).
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
U0, U1 = 7721, 7855
UNIT = M[U0 - 1:U1]


# provenance: owed to r2lib since chat 105 (heading to the NEXT heading of ANY rank).
def body_range(lines, sec):
    s = heading_line(lines, sec)
    if s is None:
        return None
    for i in range(s + 1, len(lines) + 1):
        if re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', lines[i - 1].strip()):
            return (s, i)
    return (s, len(lines) + 1)


def nonblank(lines, a, b):
    return sum(1 for t in lines[a:b - 1] if t.strip())


# provenance: owed to r2lib since chat 108.  '^#{1,4}\s*N\s*$' misses '### 203, 215, 218, ...',
# which is a real Register heading form (seven of them).
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
    for j in range(i, min(i + 6, len(REG))):
        if REG[j].strip():
            return re.sub(r'\s+', ' ', REG[j].strip())[:150]
    return ''


# provenance: owed to r2lib since chat 109 (F7).  A phrase may straddle a line break; the join
# must be collapsed against the raw line or every site count doubles.
def sites(phrase):
    p = phrase.lower()
    out = []
    for k, L in V.items():
        for i, t in enumerate(L, 1):
            if p in t.lower():
                out.append((k, i, 'line'))
            elif i < len(L) and p in (t + ' ' + L[i]).lower().replace('  ', ' '):
                if p not in t.lower() and p not in L[i].lower():
                    out.append((k, i, 'join'))
    return out


def head(t):
    print('\n' + t); print('-' * len(t))


print('r2-ch15o  prose batch  main L%d-L%d  (%d lines)' % (U0, U1, U1 - U0 + 1))

# ---------------------------------------------------------------- P1  section pointers
head('P1  every §-pointer in the unit, resolved under body_range AND section_span')
ptr = sorted({m.group(1) for t in UNIT for m in re.finditer(r'§(\d+(?:\.\d+)*)', t)},
             key=lambda s: [int(x) for x in s.split('.')])
print('  pointers found: %s' % ' '.join('§' + p for p in ptr))
for p in ptr:
    br, sp = body_range(M, p), section_span(M, p)
    hl = heading_line(M, p)
    nb = nonblank(M, br[0], br[1]) if br else 0
    cites = [i for i in range(U0, U1 + 1) if re.search(r'§%s(?![\d.])' % re.escape(p), M[i - 1])]
    print('  §%-8s heading %-8s body %-14s nonblank %-4d span %-14s cited at %s'
          % (p, hl if hl else 'ABSENT', ('L%d-L%d' % (br[0], br[1] - 1)) if br else '--',
             nb, ('L%d-L%d' % (sp[0], sp[1] - 1)) if sp else '--',
             ','.join('L%d' % c for c in cites)))

head('P2  the two pointers that carry a claim into a body-less section')
for p, what in (('28.9', 'the envelope repair <= phi(corroboration)'),
                ('14.5.7', "the register's shape is its seed")):
    br = body_range(M, p)
    print('  §%s body nonblank lines = %d  (%s)'
          % (p, nonblank(M, br[0], br[1]) if br else -1, what))
env = [(k, i) for k, L in V.items() for i, t in enumerate(L, 1)
       if 'φ(corroboration)' in t or 'phi(corroboration)' in t]
print('  the envelope is printed at: %s' % ' '.join('%s:L%d' % e for e in env))
print('  §28.9 heading L%d, §28.9.1 heading L%d -> the cited claim lives in the SUBSECTION'
      % (heading_line(M, '28.9'), heading_line(M, '28.9.1')))
c1457 = [i for i, t in enumerate(M, 1) if re.search(r'§14\.5\.7(?![\d.])', t)]
print('  §14.5.7 cited in main at %d sites: %s' % (len(c1457), ','.join('L%d' % i for i in c1457)))
allc = [(k, i) for k, L in V.items() for i, t in enumerate(L, 1) if re.search(r'§?14\.5\.7(?![\d.])', t)]
print('  §14.5.7 cited across six volumes at %d sites' % len(allc))

# ---------------------------------------------------------------- P3  register citations
head('P3  every "Register N" citation in the unit: existence first, then the headline')
cit = sorted({int(m.group(1)) for t in UNIT for m in re.finditer(r'[Rr]egisters?\s+(\d+)', t)})
print('  cited: %s' % cit)
for n in cit:
    kind, i = register_entry(n)
    if kind is None:
        print('  Register %-5d NO ENTRY IN THE REGISTER' % n)
    else:
        print('  Register %-5d %-8s L%-6d %s' % (n, kind, i, headline(i)))

# ---------------------------------------------------------------- P4  ruling 45 / 46
head('P4  ruling 45 (build and editorial-process remarks) and ruling 46 (internal references)')
r45 = ['this session', 'the session', 'an earlier draft', 'earlier draft', 'this book',
       'retained in the compendium', 'had not noticed', 'arrived last', 'has spoken of them']
for w in r45:
    hit = [i for i in range(U0, U1 + 1) if w in M[i - 1].lower()]
    if hit:
        for i in hit:
            print('  R45? %-26s L%-6d %s' % (w, i, re.sub(r'\s+', ' ', M[i - 1].strip())[:78]))
r46 = ['regex', 'build ', 'script', '.py', 'file', 'classifier', 'instrument']
for w in r46:
    hit = [i for i in range(U0, U1 + 1) if w in M[i - 1].lower()]
    for i in hit:
        print('  R46? %-26s L%-6d %s' % (w, i, re.sub(r'\s+', ' ', M[i - 1].strip())[:78]))
tags = [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4} ', t) and 'retained in the compendium' in t.lower()]
print('  "retained in the compendium" heading tags in the volume: %d %s'
      % (len(tags), ','.join('L%d' % i for i in tags)))
print('  the unit\'s tag L7774 is the LAST in the volume: %s' % (tags[-1] == 7774 if tags else '?'))

# ---------------------------------------------------------------- P5  false universals
head('P5  the false-universal / superlative class, and census rows 1169 and 1170')
uni = [(i, re.sub(r'\s+', ' ', M[i - 1].strip())) for i in range(U0, U1 + 1)
       if re.search(r'\b(never|every|no entry|all |strongest|densest|only)\b', M[i - 1], re.I)]
for i, t in uni:
    print('  L%-6d %s' % (i, t[:104]))

# ---------------------------------------------------------------- P6  Prints & Proofs witness
head('P6  Prints & Proofs witness for the three sections')
for sec in ('28.8', '28.9', '28.9.1'):
    hp = heading_line(PP, sec)
    if hp is None:
        print('  §%-7s ABSENT from Prints & Proofs' % sec)
    else:
        br = body_range(PP, sec)
        print('  §%-7s PP heading P%-6d nonblank body %-4d | %s'
              % (sec, hp, nonblank(PP, br[0], br[1]), re.sub(r'\s+', ' ', PP[hp - 1].strip())[:70]))
for fig in ('319', '248', '210', '67.5', '71.4', '116'):
    pp = [i for i, t in enumerate(PP, 1) if re.search(r'(?<![\d,.])%s(?![\d,.])' % fig, t)]
    print('  PP sites for %-5s : %d %s' % (fig, len(pp), ','.join('P%d' % i for i in pp[:8])))

# ---------------------------------------------------------------- P7  formatting classes
head('P7  formatting: the split heading, the duplicated table header, punctuation, openings')
print('  L7721 heading : %s' % M[7720])
print('  L7722 next    : %s' % M[7721])
print('  contents entry L150: %s' % M[149].strip())
print('  -> the heading sentence finishes in the body (docket 18 shape, 14q-06)')
for i in (7753, 7756):
    print('  L%d table header: %s' % (i, re.sub(r'\s+', ' ', M[i - 1].strip())))
print('  -> the four-row table prints its header twice, splitting one table in two (docket 28)')
paras = []
for i in range(U0, U1 + 1):
    t = M[i - 1].rstrip()
    if t.strip() and (i == U1 or not M[i].strip()):
        paras.append((i, t.strip()))
unp = [(i, t) for i, t in paras if not re.search(r'[.:;!?\u2014)*%]$', t)]
print('  paragraph-final lines: %d ; without terminal punctuation: %d' % (len(paras), len(unp)))
for i, t in unp:
    print('    L%-6d %s' % (i, t[:92]))
low = [i for i in range(U0, U1 + 1)
       if re.match(r'^#{1,4} \d+(\.\d+)* [a-z]', M[i - 1])]
print('  lower-case section openings in the unit: %s' % (low if low else 'none'))

# ---------------------------------------------------------------- P8  duplicated-line sweep
head('P8  duplicated-passage sweep (docket 27): long unit lines recurring elsewhere')
longs = [(i, M[i - 1].strip()) for i in range(U0, U1 + 1) if len(M[i - 1].strip()) >= 60]
rec = []
for i, t in longs:
    for k, L in V.items():
        for j, u in enumerate(L, 1):
            if u.strip() == t and not (k == 'main' and j == i):
                rec.append((i, k, j))
print('  long lines in the unit: %d ; recurring elsewhere: %d %s'
      % (len(longs), len(rec), rec[:6]))

# ---------------------------------------------------------------- P9  single-witness sweep
head('P9  single-witness phrases (docket 17): one site in six volumes, line and join')
cand = ['the process index', 'visible \u2264 committed', 'a dependent choice is indexable',
        'the withdrawals register', 'the mathematics register', 'admitted-and-absent',
        'repair \u2264 \u03c6(corroboration)', 'the shapes of correction', 'its shape is its seed',
        'a protocol whose warrant']
for c in cand:
    s = sites(c)
    print('  %-34s %d site(s) %s' % (c[:34], len(s), ' '.join('%s:L%d%s' % (a, b, '' if m == 'line' else '(join)') for a, b, m in s[:6])))

# ---------------------------------------------------------------- P10 cross-volume agreement
head('P10  the same two-register claim in the compendia: does it carry 248 or 319?')
for k, ln in (('reg', 1809), ('reg', 1549), ('mc', 940)):
    t = re.sub(r'\s+', ' ', V[k][ln - 1].strip())
    print('  %-4s L%-6d %s' % (k, ln, t[:150]))
for k in ('reg', 'mc', 'ioi'):
    hits = [i for i, t in enumerate(V[k], 1)
            if re.search(r'(?<![\d,.])319(?![\d,.])', t) and re.search(r'register|withdraw', t, re.I)]
    print('  %-4s lines carrying 319 with "register/withdraw": %s' % (k, hits[:8]))
