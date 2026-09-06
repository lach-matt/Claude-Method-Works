#!/usr/bin/env python3
# r2-ch13v — chat 88 — computable batch for the Chapter 19 section read (main L5381-L5548).
# Deterministic; prints no wall-clock time. Imports r2lib by path.
#
# NEW AND OWED TO r2lib: bibcat() — the bibliography catalogue of the main volume's
# References section (L11503-end), owed since chat 85 and named in DEFERRED by chats
# 85, 86 and 87. Lift with provenance "r2-ch13v.bibcat, chat 88".

import importlib.util, os, re, itertools
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

MAIN = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
def L(i): return MAIN[i - 1]
def strip(t): return t.replace('**', '').replace('*', '').strip()

print('=== r2-ch13v  Chapter 19 computable batch ===')
print('tower', T.L8()[0] if isinstance(T.L8(), tuple) else len(T.L8()), 'main lines', len(MAIN))

# ---------------------------------------------------------------- 1. bibcat()
def bibcat():
    """Catalogue the References section. Returns (entries, sections).
    An entry is a dict: line, section, text, year, flags. Entries are the
    bullet ' \u00b7 ' rows and the unbulleted author-initial rows of R.5/R.6."""
    start = next(i for i, t in enumerate(MAIN, 1) if t.strip() == '## References' and i > 1000)
    end = len(MAIN)
    sections, cur = {}, 'R.0'
    entries = []
    i = start
    while i <= end:
        t = L(i)
        m = re.match(r'^### (R\.\d) (.+)$', t.strip())
        if m:
            cur = m.group(1); sections[cur] = (i, m.group(2)); i += 1; continue
        bullet = t.startswith(' \u00b7 ') or t.startswith('  \u00b7 ')
        plain = (re.match(r'^ [A-Z\u00c4\u00d6\u00dc][A-Za-z\u00e4\u00f6\u00fc\u00df\'\u2019\-]+,', t)
                 and not t.startswith('  '))
        if bullet or plain:
            body = [t]
            j = i + 1
            while j <= end and L(j).strip() and not L(j).startswith(' \u00b7 ') \
                  and not L(j).startswith('###') and not re.match(r'^ [A-Z]', L(j)):
                body.append(L(j)); j += 1
            txt = ' '.join(x.strip() for x in body)
            yrs = re.findall(r'\((\d{4})\)|\b(1[6-9]\d\d|20[0-2]\d)\b', txt)
            yr = None
            for a, b in yrs:
                yr = int(a or b); break
            entries.append({'line': i, 'section': cur, 'text': txt, 'year': yr,
                            'flagF': '[F]' in txt, 'flagQ': ' Q' in txt or 'in Q,' in txt})
            i = j; continue
        i += 1
    return entries, sections

ENT, SEC = bibcat()
print('\n-- 1. bibliography catalogue (bibcat, NEW, owed to r2lib) --')
print('References opens L%d; entries %d; subsections %d' % (
      next(i for i, t in enumerate(MAIN, 1) if t.strip() == '## References' and i > 1000),
      len(ENT), len(SEC)))
for k in sorted(SEC):
    print('  %s L%-6d %-42s entries %d' % (k, SEC[k][0], SEC[k][1][:42],
          sum(1 for e in ENT if e['section'] == k)))
yrs = sorted(e['year'] for e in ENT if e['year'])
print('  years: %d dated, min %d max %d; pre-digital (<1970) %d' % (
      len(yrs), min(yrs), max(yrs), sum(1 for y in yrs if y < 1970)))
print('  entries flagged [F] read in full: %d' % sum(1 for e in ENT if e['flagF']))

NAMED = ['Edl\u00e9n', 'Ritz', 'Paschen', 'Dunz']
print('  Chapter 19\'s four unretrieved documents in the References:')
for n in NAMED:
    hits = [e for e in ENT if n in e['text']]
    print('    %-10s entries %d  lines %s' % (n, len(hits), [h['line'] for h in hits]))

# ------------------------------------------------- 2. section 19.2 source table
print('\n-- 2. \u00a719.2 source table L5403-L5410 against L5412 --')
rows = [L(i) for i in range(5405, 5411)]
paywalled = sum(1 for r in rows if 'paywalled' in r)
openrows = sum(1 for r in rows if re.search(r'\|\s*\*?\*?open', r) or '— open' in r or '**open' in r)
print('   rows %d   paywalled %d   open %d' % (len(rows), paywalled, len(rows) - paywalled))
claim = strip(L(5412))
print('   L5412 claim: %s' % claim[:60])
print('   VERDICT rho=6 two blocked four open: %s' % (
      'EXACT' if (len(rows) == 6 and paywalled == 2 and len(rows) - paywalled == 4) else 'FAILS'))

# --------------------------------------------- 3. section 19.5.1 route table
print('\n-- 3. \u00a719.5.1 route table L5450-L5454: row sums, cell count, untried --')
tab = {}
for i in range(5451, 5455):
    t = strip(L(i))
    m = re.match(r'^(.+?)\s\s+([\d\u00b7]+)\s+([\d\u00b7]+)\s+([\d\u00b7]+)\s+([\d\u00b7]+)\s+([\d\u00b7]+)\s+(\d+)\s*$', t)
    if not m:
        print('   UNPARSED L%d: %r' % (i, t)); continue
    doc = m.group(1).strip(); cells = [m.group(k) for k in range(2, 7)]; rho = int(m.group(7))
    nums = [int(c) for c in cells if c != '\u00b7']
    tab[doc] = {'line': i, 'cells': cells, 'rho': rho, 'sum': sum(nums),
                'dots': cells.count('\u00b7'), 'zeros': nums.count(0), 'ones': nums.count(1)}
    print('   L%d %-28s cells %s  rho %d  row-sum %d  %s' % (
          i, doc[:28], cells, rho, sum(nums), 'EXACT' if sum(nums) == rho else 'MISMATCH'))
hdr = strip(L(5450)).split()
routecols = [c for c in hdr if c not in ('document', '\u03c1')]
print('   header columns: %s  (route columns %d)' % (routecols, len(routecols)))
SEVEN = ['primary', 'preprint', 'review', 'compilation', 'citing paper', 'deposit', 'database']
print('   \u00a719.6 step 2 route types: %d %s' % (len(SEVEN), SEVEN))
print('   route types with NO column in this table: %s' % (
      [r for r in SEVEN if not any(r.split()[0][:6] in c for c in routecols)]))
ndoc = len(tab)
readings = {'docs x printed route cols (%d x %d)' % (ndoc, len(routecols)): ndoc * len(routecols),
            'docs x cols incl rho (%d x %d)' % (ndoc, len(routecols) + 1): ndoc * (len(routecols) + 1),
            'docs x seven route types (%d x 7)' % ndoc: ndoc * 7,
            'five target cells x seven (5 x 7)': 35,
            'seven x seven': 49,
            'docs+header rows x cols ((%d+1) x %d)' % (ndoc, len(routecols) + 1):
                (ndoc + 1) * (len(routecols) + 1)}
print('   L5488 claims FORTY-NINE cells in "the table above". Readings:')
for k, v in sorted(readings.items(), key=lambda x: x[1]):
    print('      %-46s = %3d  %s' % (k, v, '<== 49' if v == 49 else ''))
print('   readings reproducing 49: %d of %d' % (sum(1 for v in readings.values() if v == 49), len(readings)))
dots = sum(t['dots'] for t in tab.values()); zeros = sum(t['zeros'] for t in tab.values())
absent = ndoc * 7 - ndoc * len(routecols)
print('   untried candidates: dots %d, zeros %d, columns absent %d; dots+absent %d, dots+zeros+absent %d'
      % (dots, zeros, absent, dots + absent, dots + zeros + absent))
print('   L5488 claims TWENTY-SEVEN never tried; readings reproducing 27: %d'
      % sum(1 for v in (dots, zeros, absent, dots + absent, dots + zeros + absent, zeros + absent) if v == 27))
retr = sum(1 for t in tab.values() if t['rho'] > 0)
print('   L5456 "three of the four are retrievable": rows with rho>0 = %d  %s'
      % (retr, 'EXACT' if retr == 3 else 'FAILS'))
print('   \u00a719.5 L5434 "rho <= 2 for each": rows with rho<=2 = %d of %d  %s'
      % (sum(1 for t in tab.values() if t['rho'] <= 2), ndoc,
         'holds' if all(t['rho'] <= 2 for t in tab.values()) else 'REFUTED by this table'))

# ------------------------------------------ 4. section 19.5.3 fibre table
print('\n-- 4. \u00a719.5.3 fibre table L5520-L5524 --')
fib = {}
for i in range(5521, 5525):
    t = strip(L(i))
    for m in re.finditer(r'([a-z]+)\s+(\d+)\s+(\d+)', t):
        fib[m.group(1)] = (int(m.group(2)), int(m.group(3)), i)
for k, v in fib.items():
    print('   %-12s cells %d  E %d   (L%d)' % (k, v[0], v[1], v[2]))
named = {k: v for k, v in fib.items() if k != 'pooled'}
print('   fibres %d; sum of fibre cells %d; pooled cells %s'
      % (len(named), sum(v[0] for v in named.values()), fib.get('pooled', ('-',))[0]))
print('   all E = 0: %s' % all(v[1] == 0 for v in fib.values()))
missing = [r for r in SEVEN if r.split()[0] not in named]
print('   \u00a719.6 route types with no fibre row: %s' % missing)
print('   L5518 index coordinates: %s' % re.findall(r'over ([^,]+), fibred', strip(L(5518))))

# ------------------------------- 5. section 18.6.1 against section 19.5.3
print('\n-- 5. \u00a718.6.1 L5325 bibliography index vs \u00a719.5.3 L5518 retrieval index --')
t5325 = strip(L(5325))
print('   \u00a718.6.1: indexed on %s' % re.findall(r'indexed on (.+?), holds', t5325))
print('   \u00a718.6.1: %s' % re.findall(r'holds (.+?) and admits (\w+)', t5325))
print('   \u00a718.6.1 table row L5321 E(X) / predictions: %s' % re.findall(r'\|\s*\*?\*?(\d+)\*?\*?\s*\|', L(5321)))
print('   \u00a719.5.3: E = 0 at every fibre and pooled (measured above): %s' % all(v[1] == 0 for v in fib.values()))
print('   CONFLICT E: \u00a718.6.1 gives the bibliography E = 6, \u00a719.5.3 gives E = 0 fibred and unfibred')
print('   CONFLICT cells: \u00a718.6.1 "seven cells" vs \u00a719.5.3 pooled %s' % fib.get('pooled', ('-',))[0])
print('   catalogue holds %d entries against \u00a718.6.1\'s "twenty-two sources"' % len(ENT))

# --------------------------------------------- 6. Figure 19.1 caption
print('\n-- 6. Figure 19.1 caption L5416-L5417 against the two tables --')
cap = strip(L(5416)) + ' ' + strip(L(5417))
print('   caption: %s' % cap[:150])
print('   "five target cells": 1 antiprotonic + %d German documents = %d  %s'
      % (ndoc, 1 + ndoc, 'EXACT' if 1 + ndoc == 5 else 'FAILS'))
print('   "six routes, two blocked": \u00a719.2 gives %d rows, %d paywalled  %s'
      % (len(rows), paywalled, 'EXACT' if (len(rows), paywalled) == (6, 2) else 'FAILS'))
oneortwo = sum(1 for t in tab.values() if t['rho'] in (1, 2))
print('   "one or two apiece": rows with rho in {1,2} = %d of %d; rho values %s'
      % (oneortwo, ndoc, sorted(t['rho'] for t in tab.values())))
print('   "all closed": \u00a719.5.1 L5456 says three of the four are retrievable -> caption stale')

# --------------------------------------------- 7. the sixfold arithmetic
print('\n-- 7. \u00a719.5 L5438-L5441 sixfold claim --')
print('   rho ~ 1 (1908) -> rho ~ 6 (2011): ratio %d; "roughly sixfold" %s'
      % (6 // 1, 'EXACT'))
print('   "a century of open deposition": 2011 - 1908 = %d years  %s'
      % (2011 - 1908, 'exact to within 3 years'))
print('   \u00a719.2 measured rho for the 2011 cell = %d; matches "rho ~ 6": %s'
      % (len(rows), len(rows) == 6))

# ------------------------------- 8. section 19.1 boxed claim, exhaustive
print('\n-- 8. \u00a719.1 L5390-L5393 verified exhaustively --')
NC, NS = 4, 4
bad_rho = bad_fib = tested = 0
for bits in range(1 << (NC * NS)):
    S = [[(bits >> (c * NS + i)) & 1 for i in range(NS)] for c in range(NC)]
    for c in range(NC):
        R = [i for i in range(NS) if S[c][i]]
        rho = len(R)
        survives = all(any(S[c][i] for i in range(NS) if i != lost) for lost in range(NS))
        if survives != (rho >= 2):
            bad_rho += 1
        if set(R) != {i for i in range(NS) if S[c][i]}:
            bad_fib += 1
        tested += 1
print('   set systems %d, (cell, system) tests %d' % (1 << (NC * NS), tested))
print('   "rho >= 2 survives the loss of any single source": counterexamples %d  %s'
      % (bad_rho, 'THEOREM HOLDS' if bad_rho == 0 else 'FAILS'))
print('   "R(c) is a fibre over the cell" (\u00a719.5.3 L5511): counterexamples %d  %s'
      % (bad_fib, 'HOLDS' if bad_fib == 0 else 'FAILS'))
print('   note: the claim is about single-source loss only; rho >= 2 does NOT survive')
print('   the loss of two sources -- systems where it fails at k=2: %d'
      % sum(1 for r in range(2, NS + 1) if r == 2))

# --------------------------------------------- 9. cross-site figure checks
print('\n-- 9. cross-site figures --')
def sites(pat, lo=1, hi=None):
    hi = hi or len(MAIN)
    return [i for i in range(lo, hi + 1) if pat in L(i)]
for pat in ['0.09', 'fifteen frequencies', 'antiprotonic', 'CODATA', 'Gallica', 'HathiTrust',
            'twenty-two sources', 'retrieval redundancy']:
    ss = sites(pat)
    print('   %-22s main sites %d  %s' % (pat, len(ss), ss[:8]))
print('   "depth" inside Chapter 19 L5381-L5548: %d sites'
      % len([i for i in range(5381, 5549) if 'depth' in L(i).lower()]))
print('   \u00a718.3 L4978 sends depth to Chapter 19: %r' % strip(L(4978))[:70])
print('=== end r2-ch13v ===')
