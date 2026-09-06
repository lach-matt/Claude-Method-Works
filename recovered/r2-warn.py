# r2-warn.py — the Register WARNING sweep (RUL-128 item 3 (ii), first half; chat 142).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic; Decimal, never round().
# §0 conventions and fresh counts; §1 every `WARNING:` marker with its entry; §2 every citer of a WARNING'd entry across the six volumes,
# tested on the markup-stripped two-line join for the qualification (a token probe, stated as such); §3 the unheaded-entry class under BOTH
# heading conventions (bare `### N` and grouped `### N, N, …`) and every absent number cited in a Register phrase anywhere; §4 the six items
# named in HANDOFF-94 (1,748 vs 1,738; 1779; 1786; 1778 / IoI L2021; 1403 at G 10.4c; 344 / 1710 in ranges).
import os, re, importlib.util
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
MC = L.read_member('The_Method_1_6___Mathematical_Compendium-2.md').split('\n')
PC = L.read_member('The_Method_1_6___The_Physics_Compendium-2.md').split('\n')
IOI = L.read_member('The_Method_1_6___The_Index_of_Indices-2.md').split('\n')
SC = L.read_member('The_Method_1_6___Spectra_Compendium-2.md').split('\n')
VOL = [('main', M), ('reg', R), ('mc', MC), ('pc', PC), ('ioi', IOI), ('sc', SC)]
def hr(t): print('\n== ' + t)
def pct(a, b): return str((Decimal(a) * 100 / Decimal(b)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)) + ' % (ROUND_HALF_UP, 1 dp)'
def rbody(n):   # copied verbatim from r2-ch28b.py (there from r2-ch27b.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def body_range(M, sec):   # copied verbatim from r2-ch28b.py (there from r2-ch27b.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def lettered(M, tag):   # copied verbatim from r2-ch28b.py (there from r2-ch27b.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def strip_md(s): return re.sub(r'\s+', ' ', re.sub(r'[*_`]+', '', s)).strip()
def join2(V, i): return strip_md(V[i - 1] + ' ' + (V[i] if i < len(V) else ''))   # markup-stripped join of line i (1-based) with the next
def numsites(V, s):   # digit-bounded numeral sites (a trailing non-thousands comma admitted by the boundary itself)
    return [i for i, l in enumerate(V, 1) if re.search(r'(?<![\d,])' + re.escape(s) + r'(?![\d,]\d)', l)]

hr('§0 CONVENTIONS AND FRESH COUNTS')
print('Register member lines', len(R), '| main', len(M), '| MC', len(MC), '| PC', len(PC), '| IoI', len(IOI), '| SC', len(SC))
BARE = {}; GROUP = {}
for i, l in enumerate(R, 1):
    m = re.match(r'^#{1,4}\s*(\d+)\s*$', l)
    if m: BARE.setdefault(int(m.group(1)), i)
    m = re.match(r'^#{1,4}\s*(\d+(?:\s*,\s*\d+)+)\s*$', l)
    if m:
        for n in re.findall(r'\d+', m.group(1)): GROUP.setdefault(int(n), i)
EXT = 1792
print('Heading convention A (bare `^#{1,4}\\s*N\\s*$`):', len(BARE), 'entries; max', max(BARE))
print('Heading convention B (grouped `^#{1,4}\\s*N, N, …\\s*$`):', len(GROUP), 'numbers on', len(set(GROUP.values())), 'lines:', sorted(set(GROUP.values())))
absentA = [n for n in range(1, EXT + 1) if n not in BARE]; absentAB = [n for n in absentA if n not in GROUP]
print('Absent under A (1..%d):' % EXT, len(absentA), '| absent under A and B:', len(absentAB))
print('WARNING marker convention: raw case-sensitive `WARNING:` (the colon excludes headline words such as 1463\'s FISHBURN\'S WARNING); raw `WARNING` lines:',
      sum(1 for l in R if 'WARNING' in l), '| `WARNING:` lines:', sum(1 for l in R if 'WARNING:' in l), '| markers:', sum(l.count('WARNING:') for l in R))
HL = sorted((i, n) for n, i in BARE.items()); HLG = sorted(set((i, n) for n, i in GROUP.items()))
ALLH = sorted(set(i for i, _ in HL) | set(i for i, _ in HLG))
def entry_of(i):   # enclosing heading (either convention); a grouped heading is reported by its line
    e = None
    for hi in ALLH:
        if hi <= i: e = hi
        else: break
    if e is None: return None
    bare = [n for (hi, n) in HL if hi == e]
    return bare[0] if bare else 'group@L%d' % e

hr('§1 EVERY `WARNING:` MARKER, ITS ENTRY, AND THE REGISTER IT NAMES AS CORRECTOR')
WARN = {}   # entry -> list of (line, marker text, correctors named)
for i, l in enumerate(R, 1):
    for m in re.finditer(r'WARNING:', l):
        e = entry_of(i); txt = strip_md(l[m.end():m.end() + 420])
        corr = sorted(set(int(x) for x in re.findall(r'[Rr]egisters?\s+(\d{3,4})', l[m.end():])))
        WARN.setdefault(e, []).append((i, txt, corr))
        print('L%d entry %s | correctors named %s | %s' % (i, e, corr or '-', txt[:260]))
print('WARNING\'d entries:', len(WARN), sorted(WARN))
print('chat-140 five (1309, 1350, 1401, 1403, 1461) all present:', all(n in WARN for n in (1309, 1350, 1401, 1403, 1461)))

hr('§2 CITERS OF EVERY WARNING\'D ENTRY ACROSS THE SIX VOLUMES, TESTED ON THE JOIN')
# Citer convention: a `[Rr]egister(s)?` phrase = the run of numbers, ranges (– — -), commas, `and`, `to` that follows the word; every number in
# it and every number inside a range of width ≤ 100 is a citation (a wider range is an extent statement, listed in §3). The Register's own
# entries count as citers except the entry's own body. Bare `N` outside a register phrase is NOT a citation (DOCKET G0i).
PHRASE = re.compile(r'[Rr]egisters?\s+((?:\d{1,4}(?:\s*[–—-]\s*\d{1,4})?)(?:\s*(?:,|and|to|;)\s*(?:\d{1,4}(?:\s*[–—-]\s*\d{1,4})?))*)')
def cited(l):
    out = set(); wide = []
    for m in PHRASE.finditer(l):
        for tok in re.split(r'\s*(?:,|and|to|;)\s*', m.group(1)):
            r = re.match(r'(\d+)\s*[–—-]\s*(\d+)$', tok.strip())
            if r:
                a, b = int(r.group(1)), int(r.group(2))
                if 0 < b - a <= 100: out.update(range(a, b + 1))
                elif b - a > 100: wide.append((a, b))
            elif tok.strip().isdigit(): out.add(int(tok.strip()))
    return out, wide
QUAL = r'withdraw|deactivat|supersed|correct|reconstruct|qualif|sharpen|clarif|retract|overstat|retained as a form|as a form|not the solution|too strong|wrong|refuted|deprecat|revised|no longer'
print('Qualification probe (token, stated as such): stems /%s/ OR the corrector register named, on the markup-stripped two-line join.' % QUAL[:60] + '…')
CIT = defaultdict(list); WIDE = []
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if 'egister' not in l: continue
        s, w = cited(l); WIDE += [(tag, i, a, b) for a, b in w]
        for n in s:
            if n in WARN:
                if tag == 'reg' and entry_of(i) == n: continue
                CIT[n].append((tag, i))
tally = Counter()
for n in sorted(WARN):
    corr = sorted(set(c for _, _, cs in WARN[n] for c in cs))
    print('\n-- Register %s (%d citer line(s); corrector(s) %s)' % (n, len(CIT[n]), corr or 'none named'))
    for tag, i in CIT[n]:
        V = dict(VOL)[tag]; j = join2(V, i)
        stem = re.search(QUAL, j, re.I); cn = [c for c in corr if re.search(r'(?<!\d)%d(?!\d)' % c, j)]
        v = 'CARRIES' if (stem or cn) else 'SILENT'
        tally[v] += 1
        print('  %s L%d %s%s | %s' % (tag, i, v, (' (' + (stem.group(0) if stem else '') + (' +corrector ' + str(cn) if cn else '') + ')') if v == 'CARRIES' else '', j[:230]))
    if not CIT[n]: print('  no citer in any volume (witness: PHRASE regex over all six members, ranges ≤ 100 expanded)')
print('\nTally over all citer lines:', dict(tally), '| SILENT share', pct(tally['SILENT'], max(1, sum(tally.values()))))
print('Entries with ≥ 1 SILENT citer:', sorted(n for n in WARN if any(True for tag, i in CIT[n] if not re.search(QUAL, join2(dict(VOL)[tag], i), re.I) and not any(re.search(r'(?<!\d)%d(?!\d)' % c, join2(dict(VOL)[tag], i)) for _, _, cs in WARN[n] for c in cs))))

hr('§3 THE UNHEADED-ENTRY CLASS UNDER BOTH CONVENTIONS, AND EVERY ABSENT NUMBER A REGISTER PHRASE CITES')
DOCK = [219, 220, 221, 305, 239, 256, 344, 1710]
for n in DOCK: print('  %d: bare heading %s | grouped heading %s' % (n, 'L%d' % BARE[n] if n in BARE else 'ABSENT', 'L%d' % GROUP[n] if n in GROUP else 'ABSENT'))
citedAll = defaultdict(list)
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if 'egister' not in l: continue
        s, _ = cited(l)
        for n in s:
            if n in absentAB: citedAll[n].append((tag, i))
print('Absent-under-both numbers cited in a register phrase somewhere:', len(citedAll), 'of', len(absentAB))
for n in sorted(citedAll): print('  %d ← %s' % (n, ' '.join('%s:L%d' % x for x in citedAll[n][:12]) + (' …(+%d)' % (len(citedAll[n]) - 12) if len(citedAll[n]) > 12 else '')))
print('Absent-under-both never cited in a register phrase:', [n for n in absentAB if n not in citedAll])
print('Wide ranges (> 100, extent statements, not expanded):', WIDE[:20], '… total', len(WIDE))
grpcited = defaultdict(list)
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if 'egister' in l:
            s, _ = cited(l)
            for n in s:
                if n in GROUP and n not in BARE: grpcited[n].append((tag, i))
print('Grouped-heading numbers cited in a register phrase (headed under B only):', {n: len(v) for n, v in sorted(grpcited.items())})

hr('§4 THE SIX NAMED ITEMS')
print('(a) 1,748 vs 1,738 — digit-bounded sites per volume:')
for s in ('1,748', '1748', '1,738', '1738'):
    print('  %s:' % s, {tag: numsites(V, s) for tag, V in VOL if numsites(V, s)})
for tag, V in VOL:
    for i in numsites(V, '1,748') + numsites(V, '1,738'): print('   %s L%d: %s' % (tag, i, strip_md(V[i - 1])[:200]))
print('(b) Register 1779 (heading %s): %s' % (BARE.get(1779), (rbody(1779) or '')[:300]))
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if re.search(r'Z\s*[−-]\s*charge', l): print('   `Z − charge` %s L%d: %s' % (tag, i, strip_md(l)[:200]))
print('(c) Register 1786 (heading %s): %s' % (BARE.get(1786), (rbody(1786) or '')[:300]))
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if re.search(r'never an F\.3\.1', l): print('   `never an F.3.1` %s L%d' % (tag, i))
print('(d) Register 1778 (heading %s): %s' % (BARE.get(1778), (rbody(1778) or '')[:300]))
for tag, V in VOL:
    for i, l in enumerate(V, 1):
        if 'copied unchanged' in l: print('   `copied unchanged` %s L%d: %s' % (tag, i, strip_md(l)[:160]))
gi = [i for i, l in enumerate(M, 1) if re.match(r'^\|\s*§?1\.7\b', l)]; ii = [i for i, l in enumerate(IOI, 1) if re.match(r'^\|\s*§?1\.7\b', l)]
print('   G row §1.7 main', gi, '| IoI row §1.7', ii)
for i in gi: print('   main L%d: %s' % (i, M[i - 1][:260]))
for i in ii: print('   ioi  L%d: %s' % (i, IOI[i - 1][:260]))
print('   byte-identical:', [M[a - 1] == IOI[b - 1] for a in gi for b in ii])
print('(e) 1403 at G 10.4c — rows naming 10.4c in main Appendix G and the IoI:')
for tag, V in (('main', M), ('ioi', IOI)):
    for i, l in enumerate(V, 1):
        if re.match(r'^\|\s*§?10\.4c\b', l):
            j = join2(V, i); print('   %s L%d: %s' % (tag, i, j[:300])); print('     qualification on the join:', bool(re.search(QUAL, j, re.I)), '| names 1403:', bool(re.search(r'(?<!\d)1403(?!\d)', j)))
print('   1403 WARNING text:', WARN.get(1403, [(0, '-', [])])[0][1][:200])
print('(f) 344 and 1710 inside cited ranges (any volume):')
for n in (344, 1710):
    print('   %d:' % n, ' '.join('%s:L%d' % x for x in citedAll.get(n, [])) or 'no range/list cites it', '| named as bare token in Register lines:', [i for i, l in enumerate(R, 1) if re.search(r'(?<![\d,])%d(?![\d,]\d)' % n, l) and 'egister' in l][:8])
hr('§5 TALLY'); print('WARNING\'d entries', len(WARN), '| citer lines', sum(len(v) for v in CIT.values()), '| entries with no citer', sum(1 for n in WARN if not CIT[n]),
      '| absent-under-both cited', len(citedAll), '| grouped-only cited', len(grpcited))
