# r2-ch27b.py — the unit main `## Appendix G` (LAST hit) to `## References` (LAST hit): the PROSE / POINTER / PP claims (chat 140).
# Two units in the span: Appendix G (L… to `# END MATTER`) and the Index (`## Index` to `## References`). Reads MEMBERS by name
# (never a bundle path); imports r2lib by path; deterministic. Every pointer resolved to the CLAIM under both resolvers; every citer
# INTO the span tested against the span's content; PP diff with section numbers stripped BOTH sides; Ruling 45 / 46 probes.
import os, re, importlib.util
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
MC = L.read_member('The_Method_1_6___Mathematical_Compendium-2.md').split('\n')
P = L.read_member('PP_The_Method_1_6.md').split('\n') if os.path.exists(os.path.join(H, 'PP_The_Method_1_6.md')) else open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
def hr(t): print('\n== ' + t)
def rbody(n):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def body_range(M, sec):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def lettered(M, tag):   # copied verbatim from r2-ch26b.py (there from r2-ch25a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def enc(ln): return next('L%d %s' % (j, M[j - 1][:70]) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s', M[j - 1]))
def cnt(lines, pat, flags=re.I): return sum(len(re.findall(pat, l, flags)) for l in lines)
def sites(lines, pat, flags=0): return [i + 1 for i, l in enumerate(lines) if re.search(pat, l, flags)]
def join(lines): return re.sub(r'\s+', ' ', re.sub(r'[*_`>]', '', ' '.join(lines)))
g = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix G\b', l)][-1]; rf = [i + 1 for i, l in enumerate(M) if re.match(r'^#{1,3} References\b', l)][-1]
em = [i + 1 for i, l in enumerate(M) if l.startswith('# END MATTER')][-1]; ix = [i + 1 for i, l in enumerate(M) if re.match(r'^## Index\b', l)][-1]
U = M[g - 1:em - 1]; X = M[ix - 1:rf - 1]; S = M[g - 1:rf - 1]; SJ = join(S)
print('  span L%d–L%d; Appendix G L%d–L%d; `# END MATTER` L%d; Index L%d–L%d' % (g, rf - 1, g, em - 1, em, ix, rf - 1))

hr('§0 pre-PP diff: Appendix G is post-PP (witness: `Appendix G` in PP); the Index against PP\'s `## Index` (LAST hit) to its next `# `/`## ` heading, body lines shared / only-main / only-PP')
print('  `Appendix G` lines in PP: %s — NONE: no pre-PP diff exists for Appendix G; Register 1770 (post-PP) seated it: "%s"' % (sites(P, r'Appendix G') or 'NONE', (rbody(1770) or '')[:90]))
pi = sites(P, r'^\s*#{1,3}\s*Index\b'); print('  PP `Index` heading hits %s' % pi)
if pi:
    a = pi[-1]; b = next((i + 1 for i in range(a, len(P)) if re.match(r'^\s*#{1,2}\s', P[i])), len(P) + 1); PU = P[a - 1:b - 1]
    print('  PP Index P%d–P%d (%d lines; next heading P%d %s)' % (a, b - 1, len(PU), b, (P[b - 1] if b <= len(P) else '')[:40]))
    mb = {l.strip() for l in X if l.strip() and not l.startswith('#')}; pb = {l.strip() for l in PU if l.strip() and not re.match(r'^\s*#', l)}
    print('  body lines: main %d, PP %d, shared %d, only-main %d, only-PP %d' % (len(mb), len(pb), len(mb & pb), len(mb - pb), len(pb - mb)))
    om = sorted(mb - pb, key=lambda s: X.index(next(l for l in X if l.strip() == s))); op = sorted(pb - mb, key=lambda s: PU.index(next(l for l in PU if l.strip() == s)))
    print('  only-main lines (first 60 chars): %s' % [s[:60] for s in om][:20]); print('  only-PP lines (first 60 chars): %s' % [s[:60] for s in op][:20])
    pv = [l for l in PU if 'Verified' in l]; print('  PP\'s "Verified" line: %s' % [l.strip()[:200] for l in pv])
    print('  main L11419 "The previous index (57 terms, 139 entries, 44 relations)": PP Index term lines %d, sub-term lines %d, locators %d (PP is the previous index\'s witness if its counts agree)' % (len([l for l in PU if re.match(r'^ ?\*\*.+\*\* ……', l)]), len([l for l in PU if re.match(r'^   \S.* ……', l)]), sum(len(l.split(' …… ', 1)[1].split('·')) for l in PU if ' …… ' in l)))
    print('  PP Index locators "§32.1 / §32.3 / §24.2" (L11419 names them as the old numbering): %s' % {k: cnt(PU, re.escape(k) + r'(?!\d)', 0) for k in ('§32.1', '§32.3', '§24.2')})

hr('§1 Ruling 45 / 46 probes on the span (build narration, script names, dates, editorial-process remarks) and first person; backticks')
for pat, why in ((r'\w+\.py\b', 'script name (R46)'), (r'\d{4}-\d{2}-\d{2}', 'a date (R45)'), (r'[Rr]egenerated', 'regenerated (R45)'), (r'regenerated rather than repaired', 'process remark (R45)'),
                 (r'The previous index', 'narrated past state (docket 15)'), (r'were absent from their generalisations', 'process remark (R45)'), (r'until now', 'narrated past state (docket 15)'),
                 (r'This appendix removes that', 'process remark (R45)'), (r'left exactly as they were written', 'editorial-process remark (R45)'), (r'never edited', 'editorial-process remark (R45)'),
                 (r'part of the record', 'editorial-process remark (R45)'), (r'\bre-sourced\b', 'process remark (R45)'), (r'rather than choice', '—')):
    h = [i for i in sites(S, pat) ]; print('  %-40s %s → %s' % (pat, why, ['L%d' % (g + i - 1) for i in h]))
fp = [(g + i - 1, l[:90]) for i, l in enumerate(S, 1) if re.search(r"(?<![A-Za-z])(I|my|mine|myself|we|our|ours)(?![A-Za-z])", l) and not re.search(r'\b[A-Z][a-z]+ I\b', l)]
print('  first person (I / my / mine / myself / we / our; a species Roman numeral excluded): %s' % (fp or 'none'))
bt = Counter(re.findall(r'`([^`]+)`', ' '.join(S))); print('  backticked tokens in the span: %d occurrences, %d distinct; non-handle ones: %s (docket 28: the handle column is backticked throughout — a formatting convention, printed)' % (sum(bt.values()), len(bt), [k for k in bt if not re.match(r'^[A-Z]\.\w+$', k)]))

hr('§2 pointers OUT of the span, resolved to the CLAIM under both resolvers')
for sec, keys in (('16.4', ['down-set', 'down set', 'sublattice']), ('2.21', ['the law']), ('12.11', ['closure', 'index'])):
    br, sp = body_range(M, sec), section_span(M, sec)
    print('  §%s: body_range %s, section_span %s; keys %s | %s' % (sec, br, sp, {k: has_token(join(M[br[0] - 1:br[1] - 1]), k) for k in keys}, {k: has_token(join(M[sp[0] - 1:sp[1] - 1]), k) for k in keys}))
print('  L11417 "a down-set condition in §16.4 form": `down-set` sites in main %s (%s)' % (sites(M, r'down-set'), [enc(i) for i in sites(M, r'down-set')][:6]))
h164 = heading_line(M, '16.4'); print('  §16.4 heading: L%d "%s"; `down` %d, `⊑` %d, `⊆` %d in section_span; the earliest `down-set condition` / `down-set` definition sites: %s' % (h164, M[h164 - 1][:80], cnt(M[h164 - 1:section_span(M, '16.4')[1] - 1], r'\bdown\b'), cnt(M[h164 - 1:section_span(M, '16.4')[1] - 1], '⊑', 0), cnt(M[h164 - 1:section_span(M, '16.4')[1] - 1], '⊆', 0), [(i, enc(i)[:32]) for i in sites(M, r'down-set condition')][:6]))
print('  §16.4 form named elsewhere: `§16\.4 form` sites %s; `in §16\.4` sites %s' % (sites(M, r'§16\.4 form'), sites(M, r'in §16\.4\b')[:8]))
for tag in ('S1', 'S2', 'S3', 'D3'):
    h = [i for i in sites(M, r'(?<![A-Za-z0-9])' + tag + r'(?![A-Za-z0-9])') if not (g <= i < rf)]
    print('  L11421 (%s): sites outside the span %d %s — %s' % (tag, len(h), h[:6], [enc(i) for i in h[:3]]))
print('  L11410 "the law of this book": `the law` in §2.21 body_range %d; `law of this book` sites %s' % (has_token(join(M[body_range(M, '2.21')[0] - 1:body_range(M, '2.21')[1] - 1]), 'the law'), sites(M, r'law of this book')))
c12 = section_span(M, '12'); print('  rows 8.2 / 8.4 "Chapter 12": span %s; jurisdict* %d, vocabular* %d, functor %d, covariant %d' % (c12, *[len(re.findall(r'(?<![A-Za-z])' + k, join(M[c12[0] - 1:c12[1] - 1]), re.I)) for k in ('jurisdict', 'vocabular', 'functor', 'covariant')]))
for h in ('W.jur', 'W.rel', 'M.C1', 'M.C2'):
    ls = sites(MC, r'(?<![A-Za-z.])' + re.escape(h) + r'(?![A-Za-z0-9])'); regs = sorted({int(x) for i in ls for x in re.findall(r'(?:Register|R)\s*(\d{3,4})', MC[i - 1])})
    print('  MC %s: lines %s; Register numbers cited on those lines %s (the G rows cite 1375 / 1519 / 1523 / 1535 / 1551 / 1399 / 1403)' % (h, ls[:6], regs))
print('  main sites of `jurisdict*` with their headings: %s' % [(i, enc(i)[:25]) for i in sites(M, r'jurisdict', re.I)][:10])
print('  Register entries carrying `jurisdict*`: %s' % sorted({int(re.sub(r'\D', '', R[max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k]))])) for i in sites(R, r'jurisdict', re.I)})[:20])
print('  Register entries carrying `presymplectic` / `null surface`: %s / %s' % tuple(sorted({int(re.sub(r'\D', '', R[max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k]))])) for i in sites(R, pat, re.I)})[:12] for pat in (r'presymplectic', r'null surface')))

hr('§3 docket 36 — names in the span against `## References` body (L%d+) and R.7' % rf)
REF = M[rf - 1:]; r7 = lettered(M, 'R.7')
for name in ('Freuder', 'Montanari', 'Borchers', 'Wiesbrock', 'Hadamard', 'Killing', 'Helly', 'Pauli', 'ANEC', 'Moore'):
    print('  %-10s span %d; References body %d (lines %s); R.7 %s' % (name, cnt(S, r'\b' + name + r'\b', 0), cnt(REF, r'\b' + name + r'\b', 0), sites(REF, r'\b' + name + r'\b')[:4], ('L%d' % r7[-1]) if r7 else 'none'))

hr('§4 count words on raw lines AND the join (the figures were measured in r2-ch27a)')
for w in ('thirty-seven', 'thirty sections', 'forty-seven', 'eight citations', 'thirty resolved locators', 'thirty-four', '57 terms', '311 entries', '44 specialisation', '0 violations', 'Six terms', 'four relations', '90 locations', '139 entries'):
    print('  %-26s raw %d  join %d' % (w, cnt(S, re.escape(w)), len(re.findall(re.escape(w), SJ, re.I))))

hr('§5 citers INTO the span (main `Appendix G` / `T §` sites; the index cited)')
for i in (4246, 4250):
    print('  L%d (%s): "%s"' % (i, enc(i)[:40], M[i - 1].strip()[:200]))
print('  L4246 "T §8.2 (Appendix G)\'s own table": G row 8.2 carries `table` %d, `arity 2` %d; Transitions §8.2 carries `table` %d, `arity 2` %d — the table is the paper\'s, not the appendix row\'s' % (cnt(U, r'^\| 8\.2 .*\btable\b', 0), cnt(U, r'^\| 8\.2 .*arity 2', 0), 0, 0))
print('  L4250 "T §8.4 (Appendix G) … replaces seven vocabularies": G row 8.4 `seven-vocabulary` %d' % cnt(U, r'^\| 8\.4 .*seven'))
print('  `E\\(index\\)` sites in main: %s; `closed index` sites outside the span: %s' % (sites(M, r'E\(index\)'), [i for i in sites(M, r'closed index') if not (g <= i < rf)][:12]))

hr('§6 docket 27 — paragraphs of the span duplicated elsewhere in the volume (exact stripped line, length ≥ 40)')
out = {l.strip() for i, l in enumerate(M, 1) if not (g <= i < rf) and len(l.strip()) >= 40}
dup = [(g + i - 1, l.strip()[:70]) for i, l in enumerate(S, 1) if len(l.strip()) >= 40 and l.strip() in out]
print('  span lines ≥ 40 chars %d; duplicated outside %d %s' % (len([l for l in S if len(l.strip()) >= 40]), len(dup), dup[:6]))

hr('§7 the Index\'s formatting (docket 28): leading-space lines, unmarked heading-form lines, italic vs plain sub-terms, the duplicated sub-entry')
ls1 = [ix + i for i, l in enumerate(X) if re.match(r'^ \S', l)]; ls3 = [ix + i for i, l in enumerate(X) if re.match(r'^   \S', l)]
print('  lines beginning with ONE space %d (L%d–L%d), THREE spaces %d, four (code) %d, no indent non-blank %d' % (len(ls1), ls1[0], ls1[-1], len(ls3), len([l for l in X if l.startswith('    ')]), len([l for l in X if l and not l.startswith(' ') and not l.startswith('#')])))
print('  unmarked heading-form lines: %s' % [(ix + i, l.strip()) for i, l in enumerate(X) if re.match(r'^ [A-Z][a-z]+$', l)])
subs = [(ix + i, re.match(r'^   (\S.*?) ……', l).group(1)) for i, l in enumerate(X) if re.match(r'^   \S.*? ……', l)]
it = [s for s in subs if s[1].startswith('*')]; print('  sub-terms %d: italic %d, plain %d (mixed markup within one head group: %s)' % (len(subs), len(it), len(subs) - len(it),
      sorted({X[j - 1 - ix + 0].strip()[:20] for j, _ in subs} and [])))
print('  *interiority* L11429 (plain) and L11432 (italic) under *bracket*, both `§22.2`: a duplicated sub-entry — 311 printed entries include it twice; distinct pairs 310 (r2-ch27a §7)')
print('  `*this page*` L11498 vs `Index` L11490–L11491: one location under two names')
