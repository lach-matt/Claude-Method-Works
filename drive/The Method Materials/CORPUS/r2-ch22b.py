# r2-ch22b.py — Appendix D part 1 (main L10320–L10461, D.1–D.4.4.3), the PROSE and POINTER claims (chat 135).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic. Pre-PP unit: headings diffed
# against /home/claude/PP_The_Method_1_6.md from `# Appendix D` (PP's D.n sub-headings are UNMARKED, indented one space).
import os, re, importlib.util
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n'); R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
VOL = {'main': M, 'reg': R, 'mc': L.read_member('The_Method_1_6___Mathematical_Compendium-2.md').split('\n'), 'pc': L.read_member('The_Method_1_6___The_Physics_Compendium-2.md').split('\n'),
       'ioi': L.read_member('The_Method_1_6___The_Index_of_Indices-2.md').split('\n'), 'sc': L.read_member('The_Method_1_6___Spectra_Compendium-2.md').split('\n')}
PPp = '/home/claude/PP_The_Method_1_6.md'; PP = open(PPp, encoding='utf-8').read().split('\n') if os.path.exists(PPp) else None

def rbody(n):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch22b — Appendix D part 1 (D.1–D.4.4.3), prose and pointers')
a = lettered(M, 'Appendix D')[-1]; b = [i for i, l in enumerate(M, 1) if re.match(r'^### D\.5 ', l)][-1]; U = M[a - 1:b - 1]
print('§1 unit L%d–L%d, %d lines; blank %d; code/indented(4sp) %d; `|` table rows outside code %d' % (a, b - 1, len(U), sum(1 for l in U if not l.strip()),
      sum(1 for l in U if l.startswith('    ')), sum(1 for l in U if l.startswith('|'))))
joined = ' '.join(re.sub(r'[*_`]', '', l).strip() for l in U)   # markup-stripped join (chat-131 convention)

# §2 PP heading diff: main `### D.n title` vs PP ` D.n title`, section number stripped from BOTH sides; PP's marked-heading test
if PP:
    p0 = [i for i, l in enumerate(PP, 1) if l.startswith('# Appendix D')][-1]; p1 = [i for i, l in enumerate(PP, 1) if l.startswith('# Appendix E')][-1]
    marked = [i for i in range(p0 + 1, p1) if re.match(r'^#{1,4} ', PP[i - 1])]
    unm = [(i, PP[i - 1].strip()) for i in range(p0 + 1, p1) if re.match(r'^ ?D\.\d+(\.\d+)* ', PP[i - 1]) and not PP[i - 2].strip()]
    print('§2 PP `# Appendix D` P%d to `# Appendix E` P%d (%d lines); marked #-headings inside: %d; unmarked ` D.n` lines after a blank: %d' % (p0, p1, p1 - p0, len(marked), len(unm)))
    mh = [(i, M[i - 1]) for i in range(a, b) if re.match(r'^#{1,4} ', M[i - 1])]
    strip = lambda s: re.sub(r'^#+\s*', '', s).strip(); num = lambda s: re.sub(r'^(Appendix [A-Z] — |D\.\d+(?:\.\d+)* )', '', strip(s)).strip()
    pt = {num(t): i for i, t in unm}; pt[num(PP[p0 - 1])] = p0
    for i, l in mh:
        t = num(l); print('   L%d %-58s -> PP %s' % (i, strip(l)[:58], ('P%d' % pt[t]) if t in pt else 'ABSENT'))
    # body diff of part 1: main L a..b-1 vs PP p0..first unmarked D.5
    pd5 = next((i for i, t in unm if t.startswith('D.5 ')), p1); norm = lambda l: re.sub(r'^#+\s*', '', l.strip())   # fault 1 (chat 135): heading markers stripped on BOTH sides before the diff
    mm = [norm(l) for l in M[a - 1:b - 1] if l.strip()]; pp = [norm(l) for l in PP[p0 - 1:pd5 - 1] if l.strip()]
    mset, pset = Counter(mm), Counter(pp); only_m = [l for l in mm if pset[l] == 0]; only_p = [l for l in pp if mset[l] == 0]
    print('   part-1 body vs PP P%d–P%d: main non-blank %d, PP %d; lines only in main %d, only in PP %d' % (p0, pd5 - 1, len(mm), len(pp), len(only_m), len(only_p)))
    for l in only_m[:12]: print('      main-only:', l[:120])
    for l in only_p[:12]: print('      PP-only:  ', l[:120])
else: print('§2 BUDGET: PP not on disk; heading diff not run')

# §3 pointers: every §N, Chapter N, Figure N, Part, P-number, Appendix/D.n reference in the unit; resolve headings + claim tokens
sec_pat = re.compile(r'§(\d+(?:\.\d+)*)(?!\d)(?!\.\d)'); ch_pat = re.compile(r'\bChapter (\d+)\b'); fig_pat = re.compile(r'\bFigure (\d+\.\d+)\b')
secs = Counter(); chs = Counter(); figs = Counter()
for i, l in enumerate(U, a):
    for m in sec_pat.finditer(l): secs[(m.group(1), i)] += 1
    for m in ch_pat.finditer(l): chs[(m.group(1), i)] += 1
    for m in fig_pat.finditer(l): figs[(m.group(1), i)] += 1
print('§3 § pointers (sec, line):', sorted(secs), '; Chapter (n, line):', sorted(chs), '; Figure:', sorted(figs))
for s in sorted({s for s, _ in secs}):
    hl = heading_line(M, s); ss = section_span(M, s); print('   §%s heading L%s span %s :: %s' % (s, hl, ss, (M[hl - 1][:70] if hl else 'UNRESOLVED')))
for c in sorted({c for c, _ in chs}, key=int):
    hs = [i for i, l in enumerate(M, 1) if re.match(r'^## %s\.? ' % c, l)]; print('   Chapter %s heading lines %s :: %s' % (c, hs, M[hs[-1] - 1][:70] if hs else 'UNRESOLVED'))
# the claim-level probes that r2-ch22a left open
for pat in (r'diagnostic loop', r'separating form', r'\bexcess\b.*\bconstraint', r'means a missing constraint'):
    hits = {k: [i for i, l in enumerate(v, 1) if re.search(pat, l, re.I)] for k, v in VOL.items()}
    print('   %-30s ->' % pat, {k: v[:8] for k, v in hits.items() if v} or 'NO SITE in six volumes')
s1671 = section_span(M, '16.7.1'); print('   §16.7.1 span', s1671, 'heading:', M[s1671[0] - 1][:80], '; tokens loop/excess/separat in span:', [i for i in range(s1671[0], s1671[1]) if re.search(r'loop|excess|separat', M[i - 1], re.I)])
# PART VI title; P21; the 'seventy-seven / twenty-four / thirty-two / sixteen / forty-two' fibre figures (data table in D.5 — part 2); Register 230
print('   PART VI heading:', [(i, M[i - 1][:60]) for i, l in enumerate(M, 1) if re.match(r'^# PART VI\b', l)], '; L10321 serving line:', M[10320][:70])
p21 = [i for i, l in enumerate(M, 1) if re.search(r'\bP21\b', l)]; print('   P21 sites:', p21, '; first:', M[p21[0] - 1][:120])
print('   fibre figures (77 / 24 / 32 / 16 / 42) sites in Appendix D:', {w: [i for i in range(a, lettered(M, 'Appendix E')[-1]) if w in M[i - 1]] for w in ('seventy-seven', 'twenty-four fibres', 'Thirty-two', 'sixteen of the forty-two', 'forty-two')}, '— the DATA table that fixes them is in D.5 (part 2); carried, not scored here')
print('   7 kinds × 6 languages = %d (printed forty-two)' % (len(M[10343].split('·')) * len(M[10344].split('·'))), '; D.2 table rows with ≥3-space gap:', [i for i in range(10343, 10349) if re.search(r'\S {3,}\S', M[i - 1])])
print('   lowercase `register NNN` in unit:', [i for i, l in enumerate(U, a) if re.search(r'\bregister \d+', l)], '; `Register NNN`:', [i for i, l in enumerate(U, a) if re.search(r'\bRegister \d+', l)])

# §4 numeral sweep, digit-bounded both sides, trailing non-thousands comma admitted; every numeral with its other main sites
nums = Counter(); where = {}
for i, l in enumerate(U, a):
    for m in re.finditer(r'(?<![\d.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\d,]\d)', l): nums[m.group(1)] += 1; where.setdefault(m.group(1), []).append(i)
print('§4 numerals in unit:', len(nums), 'distinct;', ' '.join('%s×%d@%s' % (k, v, where[k][:3]) for k, v in sorted(nums.items(), key=lambda kv: where[kv[0]][0])))
for k in ('976', '12,000', '7.1', '92.6', '39.9', '35.1', '11.2', '93', '40', '35', '20', '100', '66', '48', '1,113,045,672', '1.01', '60', '30'):
    if k in where: print('   %-14s unit %s ; other main sites %s' % (k, where[k], [i for i, l in enumerate(M, 1) if re.search(r'(?<![\d.])' + re.escape(k) + r'(?![\d,]\d)', l) and not (a <= i < b)][:10]))

# §5 first-person probe (mine/myself; excludes the Roman numeral of a species), R45/R46 candidates, wording
fp = [(i, l[:90]) for i, l in enumerate(U, a) if re.search(r'(?<![A-Za-z])(I|my|me|mine|myself|we|our|us)(?![A-Za-z])', l) and not re.search(r'\b[A-Z][a-z]? (I|II|III|IV|V|VI)\b', l)]
print('§5 first-person hits:', fp)
r45 = [(i, l[:90]) for i, l in enumerate(U, a) if re.search(r'\b(build|press|draft|audit|session|chat|instrument|golden|rebuil|recomput)', l, re.I)]
r46 = [(i, l[:90]) for i, l in enumerate(U, a) if re.search(r'\.py\b|BUILD\d|\bmd5\b|numpy|python', l, re.I)]
print('   R45 candidates:', r45, '; R46 candidates:', r46)
for w in ('never been checked here', 'no precedent found', 'exhaustive', 'idempotent', 'caterpillar', 'pendant', 'normal form', 'canonical form', 'MONOTONE', 'INTERCHANGEABLE'):
    print('   %-24s unit %s ; main-elsewhere %d; mc %d; reg %d' % (w, [i for i, l in enumerate(U, a) if re.search(re.escape(w), l, re.I)], sum(1 for i, l in enumerate(M, 1) if re.search(re.escape(w), l, re.I) and not (a <= i < b)), sum(1 for l in VOL['mc'] if re.search(re.escape(w), l, re.I)), sum(1 for l in R if re.search(re.escape(w), l, re.I))))
print('   Register 230 body:', (rbody(230) or 'ABSENT')[:150]); print('   Register 385 WARNING line:', [R[i][:100] for i in range(1428, 1445) if 'WARNING' in R[i]] or 'none')
print('done')
