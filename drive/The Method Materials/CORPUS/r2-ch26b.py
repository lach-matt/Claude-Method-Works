# r2-ch26b.py — Appendix F (main `## Appendix F` to `## Appendix G`), the PROSE / POINTER / PP claims (chat 139).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic. Every pointer resolved to the CLAIM under both
# resolvers; every citer INTO the unit tested against the unit's content; PP diff with section numbers stripped BOTH sides.
import os, re, importlib.util
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')
P = L.read_member('PP_The_Method_1_6.md').split('\n') if os.path.exists(os.path.join(H, 'PP_The_Method_1_6.md')) else open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
def hr(t): print('\n== ' + t)
def rbody(n):   # copied verbatim from r2-ch25a.py (there from r2-ch24a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def body_range(M, sec):   # copied verbatim from r2-ch25a.py (there from r2-ch24a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def lettered(M, tag):   # copied verbatim from r2-ch25a.py (there from r2-ch24a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def lrange(tag):   # this instrument's own: lettered heading (LAST hit) to the next heading of any rank
    s = lettered(M, tag)[-1]
    e = next(i for i in range(s + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1]))
    return (s, e)
def enc(ln):
    return next('L%d %s' % (j, M[j - 1][:60]) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s', M[j - 1]))
def cnt(lines, pat, flags=re.I): return sum(len(re.findall(pat, l, flags)) for l in lines)
def join(lines): return re.sub(r'\s+', ' ', re.sub(r'[*_`>]', '', ' '.join(lines)))
F = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix F\b', l)][-1]
G = [i + 1 for i, l in enumerate(M) if re.match(r'^## Appendix G\b', l)][-1]
U = M[F - 1:G - 1]; UJ = join(U)

hr('§0 pre-PP diff: PP `# Appendix F` (LAST hit) to the next `# ` heading; headings with section numbers stripped BOTH sides; body lines shared / only-main / only-PP')
pf = [i + 1 for i, l in enumerate(P) if re.match(r'^\s*#{1,4}\s*Appendix F\b', l)][-1]
pe = next(i + 1 for i in range(pf, len(P)) if re.match(r'^#\s', P[i]))
PU = P[pf - 1:pe - 1]
print('  PP P%d–P%d (%d lines; next `# ` heading P%d %s); Appendix G in PP: %s' % (pf, pe - 1, len(PU), pe, P[pe - 1][:30], [i + 1 for i, l in enumerate(P) if 'Appendix G' in l] or 'NONE — Appendix G is post-PP'))
def strip(h): return re.sub(r'^\s*#{1,4}\s*(Appendix\s+)?[A-Z]?\.?\d*(\.\d+)*\s*[—-]?\s*', '', h).strip()
mh = [l for l in U if re.match(r'^#{1,4}\s', l)]
ph = [l for l in PU if re.match(r'^\s*(#{1,4}\s*)?F\.\d+(\.\d+)*\s+[A-Z]', l) or re.match(r'^\s*#{1,4}\s', l)]
print('  main headings %d; PP heading-form lines %d (marked or unmarked, leading space admitted):' % (len(mh), len(ph)))
for l in ph: print('    PP  %s' % l.strip()[:90])
ms, ps = {strip(h) for h in mh}, {strip(h) for h in ph}
print('  shared heading texts %d; only-main %s; only-PP %s' % (len(ms & ps), sorted(ms - ps), sorted(ps - ms)))
mb = {l.strip() for l in U if l.strip() and not l.startswith('#')}; pb = {l.strip() for l in PU if l.strip() and not re.match(r'^\s*#', l)}
print('  body lines: main %d, PP %d, shared %d, only-main %d, only-PP %d' % (len(mb), len(pb), len(mb & pb), len(mb - pb), len(pb - mb)))
print('  shared body lines (printed): %s' % sorted(mb & pb))
print('  Register 1780 (post-PP): "%s"' % (rbody(1780) or '')[:120])
print('  the PP appendix is the withdrawn numbers-index; its only-PP lines are the rebuild\'s removals under 1780 (a recorded change, not silent); a duplicate-section test of the unit against the volume is at §6')

hr('§1 pointers OUT of the unit, resolved to the CLAIM')
i79 = next(i for i, l in enumerate(R) if l.strip() == '### 1779'); e79 = R[i79 + 1:next(j for j in range(i79 + 1, len(R)) if re.match(r'^#{1,4}\s*\d+\s*$', R[j]))]
print('  L11269 (register 1779): heading %s; 1779 carries "electron count" %d, "7,260" %d (the (iii) claim is r2-ch26a §2\'s; fault 1: a literal 0 stood here)' % (rbody(1779) is not None, cnt(e79, r'electron count'), cnt(e79, r'7,260')))
s, e = body_range(M, '2.21'); sp = section_span(M, '2.21')
print('  L11321 "Chapter 2\'s distinction … held by the law … stable structure": §2.21 body_range %s section_span %s; "By the law" %d, "stable structure" %d, "F.3.1" %d in range' % ((s, e), sp, cnt(M[s - 1:e - 1], r'By the law'), cnt(M[s - 1:e - 1], r'stable structure'), cnt(M[s - 1:e - 1], r'F\.3\.1')))
ch2 = (heading_line(M, '2'), heading_line(M, '3')); print('  Chapter 2 span L%d–L%d carries "stable structure" %d (all in §2.21: %s)' % (ch2[0], ch2[1], cnt(M[ch2[0] - 1:ch2[1] - 1], r'stable structure'), all(s <= i + 1 < e for i, l in enumerate(M) if ch2[0] <= i + 1 < ch2[1] and 'stable structure' in l)))
print('  L11292–L11293 "Chapters 6, 12 and 24 state their central measurements to this standard explicitly and say so": every main site naming F.3 outside the unit, with its enclosing heading:')
citers = [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.3(?!\.\d)\b', l)]
chap = defaultdict(list)
for ln in citers:
    h = enc(ln); m = re.search(r'L\d+ #{1,4}\s*([A-Z]?\d*)', h); chap[re.match(r'([A-Z]|\d+)', m.group(1)).group(1)].append(ln); print('    L%d [%s] %s' % (ln, h, M[ln - 1].strip()[:110]))
print('  chapters that cite F.3 by name: %s; Chapter 24 cites F.3: %s; Chapter 22 does: %s' % (dict(chap), '24' in chap, '22' in chap))
c24 = (heading_line(M, '24'), heading_line(M, '25'))
print('  Chapter 24 span L%d–L%d: "F.3" %d, "four columns" %d, "highest standard" %d, "the standard" %d, "refutation" %d, "the test that would" %d' % (c24[0], c24[1], cnt(M[c24[0] - 1:c24[1] - 1], r'\bF\.3\b'), cnt(M[c24[0] - 1:c24[1] - 1], r'four columns'), cnt(M[c24[0] - 1:c24[1] - 1], r'highest standard'), cnt(M[c24[0] - 1:c24[1] - 1], r'the standard'), cnt(M[c24[0] - 1:c24[1] - 1], r'refutation'), cnt(M[c24[0] - 1:c24[1] - 1], r'the test that would')))
for ln in [i + 1 for i, l in enumerate(M) if c24[0] <= i + 1 < c24[1] and re.search(r'highest standard|four columns|the test that would', l)]: print('    L%d %s' % (ln, M[ln - 1].strip()[:120]))
c22 = (heading_line(M, '22'), heading_line(M, '23')); print('  Chapter 22 span L%d–L%d: "F.3" %d at %s' % (c22[0], c22[1], cnt(M[c22[0] - 1:c22[1] - 1], r'\bF\.3\b'), [i + 1 for i, l in enumerate(M) if c22[0] <= i + 1 < c22[1] and 'F.3' in l]))
print('  L11250 / L11345 F.1 ↔ F.4.3 mutual: F.1 names F.4.3 %s; F.4.3 names F.1 %s; F.4.3 names F.2 (iii) %s' % (cnt(M[F + 12:F + 30], r'F\.4\.3') > 0, cnt(M[F + 120:G], r'F\.1\b') > 0, cnt(M[F + 120:G], r'F\.2') > 0 and 'third clause' in UJ))
print('  L11313 "The rule, stated as the chapters cite it: Assert the law, compute the extent" — sites of the phrase in the volume: %s' % [(i + 1, enc(i + 1)[:26]) for i, l in enumerate(M) if re.search(r'assert the law, compute the extent', l, re.I)])
s1, e1 = body_range(M, '12.11.3.1'); sp1 = section_span(M, '12.11.3.1')
seg = M[s1 - 1:e1 - 1]
print('  §12.11.3.1 (24b-06 C item, re-probed on its OWN words): body_range %s section_span %s; "law" %d, "extent" %d, "assert" %d, "compute" %d; the rule in its words:' % ((s1, e1), sp1, cnt(seg, r'\blaw\b'), cnt(seg, r'\bextent\b'), cnt(seg, r'assert'), cnt(seg, r'compute')))
for i in range(s1 - 1, e1 - 1):
    if re.search(r'closes exactly|closes only|price of describing', M[i]): print('    L%d %s' % (i + 1, M[i].strip()[:130]))
print('  L11334 "under the ruling that separates the record of the work from the work": Register entries naming Ruling 45 or "the record of the work": %s' % [i + 1 for i, l in enumerate(R) if re.search(r'record of the work from the work|separates the record', l)][:6])

hr('§2 citers INTO the unit, tested against the unit\'s content (a label that resolves is not a claim that resolves)')
def probe(rng, pats): return {p: cnt(M[rng[0] - 1:rng[1] - 1], p) for p in pats}
f31 = lrange('F.3.1'); f41 = lrange('F.4.1'); f42 = lrange('F.4.2'); f43 = lrange('F.4.3'); f3 = (lettered(M, 'F.3')[-1], f31[0]); f2 = lrange('F.2')
print('  F.3.1 = L%d–L%d; F.4.1 = L%d–L%d; F.4.2 = L%d–L%d; F.4.3 = L%d–L%d; F.3 own body L%d–L%d' % (f31 + f41 + f42 + f43 + f3))
for ln in [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.3\.1\b', l)]:
    print('  F.3.1 citer L%d [%s]: %s' % (ln, enc(ln)[:24], M[ln - 1].strip()[:120]))
print('  F.3.1 carries: %s' % probe(f31, [r'\bnine\b', r'\bcells?\b', r'stable', r'\bprose\b', r'cannot be (stated|printed)', r'unstable by construction', r'names the cells', r'\bcount\b']))
print('    → "nine stable cells, named at F.3.1" (E.1.2 L10955; E.3 L11119): the unit names NO cell and prints no "nine"; "the cells where that structure holds" are named nowhere in Appendix F (witness: "cells" in the whole unit %d, all at L%s)' % (cnt(U, r'\bcells?\b'), [F + k for k, l in enumerate(U) if re.search(r'\bcells?\b', l)]))
print('    → "a count computed from the book cannot be printed as prose" (E.1.3 L10965; §2.21 L1082): F.3.1 L11303 "cannot be stated as a figure", L11310 "unstable by construction" — the claim resolves in other words')
for ln in [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.4\.1\b', l)]:
    print('  F.4.1 citer L%d [%s]: %s' % (ln, enc(ln)[:24], M[ln - 1].strip()[:120]))
print('  F.4.1 carries: %s' % probe(f41, [r'withdrawal ratio', r'method ratio', r'\bratio', r'withdrawn as content', r'Register']))
print('    → §32.1.3 L8961 "§F.4.1\'s withdrawal ratio measures and does not excuse. Registers 320 and 321" and §32.1.4.1 L9023 "the ratios of F.4.1" cite F.4.1 for content F.4.1 declares withdrawn (L11332); the ratios live at Register 296 / 320 / 321 / 1762: 296 "%s"' % (rbody(296) or '')[:90])
for ln in [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.4\.2\b', l)]: print('  F.4.2 citer L%d: %s' % (ln, M[ln - 1].strip()[:100]))
print('  F.4.2 citers in main outside the unit: %d; Register 1762 names F.4.2\'s withdrawal ratio 4.21 : 1 — the value is not in the unit (r2-ch26a §3)' % cnt([l for i, l in enumerate(M) if not (F <= i + 1 < G)], r'\bF\.4\.2\b'))
for ln in [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.4\.3\b', l)]:
    print('  F.4.3 citer L%d [%s]: %s' % (ln, enc(ln)[:24], M[ln - 1].strip()[:120]))
print('  F.4.3 carries: %s' % probe(f43, [r'\bdate\b', r'Λ', r'\bclock\b', r'keyed by a date', r'Register']))
print('    → §6.2 L1659 "a date must never enter Λ" ⇐ L11345 "A date is admitted nowhere in Λ" / L11355; §32.1.3 L8936 "the clock §F.4.3 identifies" ⇐ L11357 "ordered by exactly that clock": both resolve')
for ln in [i + 1 for i, l in enumerate(M) if not (F <= i + 1 < G) and re.search(r'\bF\.2\b', l)]: print('  F.2 citer L%d [%s]: %s' % (ln, enc(ln)[:24], M[ln - 1].strip()[:120]))
print('  D.5.3 L10616 "Clause (iii) is the boundary between this appendix and Appendix F": F.2 (iii) L11263 "a function of the ground alone"; D.5.3 "(iii)" %d' % cnt(M[10604:10700], r'\(iii\)'))
print('  E.1.5 L11024 "A constraint refuted by its own extent is dead, which is F.3\'s rule": F.3 own body carries the sentence %s (L%s)' % (cnt(M[f3[0] - 1:f3[1] - 1], r'refuted by its own extent is dead') > 0, [i + 1 for i in range(f3[0] - 1, f3[1] - 1) if 'refuted by its own extent' in M[i]]))
print('  §32.1.4 L8974 row "Appendix F, the numbers … 3  33  thirty-three": the rebuilt appendix prints 3 body numerals (r2-ch26a §3: 6, 12, 24 — chapter numbers); the row counts the withdrawn appendix; §32.1.4.1 L9023 "the counts of Appendices D, E and F" likewise')
print('  §32.1.4 row\'s context (L8972–L8976):'); [print('    L%d %s' % (i + 1, M[i].rstrip()[:110])) for i in range(8971, 8976)]

hr('§3 first-person, Ruling 45 and Ruling 46 probes on the unit')
fp = [(F + k, l.strip()[:80]) for k, l in enumerate(U) if re.search(r'\b(I|my|me|mine|myself|we|our|us)\b', l) and not re.search(r'\b[A-Z][a-z]? (I|II|III|IV|V|VI)\b', l)]
print('  first-person (mine, myself carried; species numerals excluded; "(i)" clause markers are lowercase and not matched): %s' % (fp or 'none'))
r45 = [(F + k, l.strip()[:90]) for k, l in enumerate(U) if re.search(r'this book prints about itself|the appendix first took|wrong one|withdrawn as content|Retained as a reference|the ruling that|the record of the work|the making of the volume|entries that established|census and its ruled row|this work added|the label is kept', l)]
print('  Ruling 45 candidates (build / editorial-process prose in a reader-facing volume): %d' % len(r45)); [print('    L%d %s' % x) for x in r45]
print('  Ruling 46 candidates (script names, build numbers, file names): %s' % ([(F + k, l.strip()[:60]) for k, l in enumerate(U) if re.search(r'\.py\b|BUILD\d|\.md\b|\.csv\b|\.tsv\b', l)] or 'none'))
print('  "coordinate file" / "coordinate table" (L11268, L11270) name the data companion as an object, not a file name: %s' % [F + k for k, l in enumerate(U) if 'coordinate' in l])

hr('§4 count words and quantifier words in the unit, each with its witness')
for w, pat, wit in [('Six kinds L11238', r'Six kinds', 'r2-ch26a §1: 6 DATA rows'), ('seventh candidate L11250/L11345', r'seventh', 'r2-ch26a §1: 6 + 1'), ('four columns L11280', r'four columns', 'r2-ch26a §1: 4 DATA rows'), ('fewer than four L11281', r'fewer than four', 'the same table'), ('The fourth column L11291', r'fourth column', 'row 4 = the refutation'), ('Two ratios L11330/L11332', r'Two ratios', 'Register 296: the withdrawal ratio and the method ratio'), ('one case L11233 / One class L11303', r'one case|One class', 'F.3.1 is the single sub-section of F.3'), ('third clause L11358', r'third clause', 'F.2 (iii)'), ('several of the corrections L11299', r'several of the corrections', 'r2-ch26a §5: Register entries matching the rule\'s words = 0 (token probe; a reading is owed)'), ('without exception L11298', r'without exception', 'census 1228; the rule\'s own scope statement'), ('Chapters 6, 12 and 24 L11293', r'Chapters 6, 12 and 24', '§1 above: F.3 cited from Chapters 2, 6, 12, 22, E; not 24')]:
    print('  %s: %d × (raw) / %d × (join) — %s' % (w, cnt(U, pat), len(re.findall(pat, UJ, re.I)), wit))   # fault 2: "Chapters 6, 12 and 24" wraps at L11292–L11293; a wrapped phrase is read on the join
print('  Register 296\'s two ratios: "withdrawal ratio" %d, "method ratio" %d in its body' % (('withdrawal ratio' in (rbody(296) or '').lower()), ('method ratio' in (rbody(296) or '').lower())))

hr('§5 census rows in range (DEFECT-CENSUS.tsv, member main, L11222–L11360)')
for l in L.read_member('DEFECT-CENSUS.tsv').split('\n'):
    f = l.split('\t')
    if len(f) > 4 and f[2] == 'main' and f[3].isdigit() and F <= int(f[3]) < G: print('  %s %s L%s "%s" — %s' % (f[0], f[1], f[3], f[4], f[5][:80]))
print('  verdicts: 1226 / 1227 / 1229 (never) and 1228 (without exception) state the definition F.1–F.3 lays down — the section\'s own claim, precedent 678 / 1217 → not a defect; 1230 is a heading word (F.4.1\'s title) → not a defect; the "several" of L11299 is scored at §4, not here')

hr('§6 docket 27 — duplicated-section test: each unit paragraph\'s first 70 characters against the rest of the volume (markup stripped)')
paras = []; cur = []
for k, l in enumerate(U):
    if not l.strip() or l.startswith('#'):
        if cur: paras.append(cur); cur = []
    else: cur.append((F + k, l))
if cur: paras.append(cur)
rest = join([l for i, l in enumerate(M) if not (F <= i + 1 < G)])
dup = [(p[0][0], join([x[1] for x in p])[:70]) for p in paras if len(join([x[1] for x in p])) > 60 and join([x[1] for x in p])[:70] in rest]
print('  paragraphs %d (a paragraph start is a non-blank line after a blank or after the heading); duplicated openings: %s' % (len(paras), dup or 'none — 0 of %d' % len(paras)))
print('  PP-only lines of the withdrawn appendix are NOT tested for duplication (they are removals under 1780, not text in the volume)')
