# r2-ch20b.py — chat 133 — R2 prose instrument for the main volume's Appendix B (`## Appendix B` to `## Appendix C`).
# Reads MEMBERS by name; imports r2lib by path; deterministic. Conventions: Ruling 45/46 probes are word-bounded and case-
# insensitive on the raw line; the first-person probe carries mine and myself and excludes the Roman numeral in a species name;
# a phrase is tested on the whitespace-normalised, markup-stripped two-line join; a `|` at line start is a table row only outside
# a 4-space code line; the docket-27 recurrence test compares whole sentences (≥ 6 words) across the six volumes; a count word
# counts DATA rows; every negative has its witness printed.
import os, re, io, sys, importlib.util, contextlib, itertools
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
PPP = '/home/claude/PP_The_Method_1_6.md'; PP = open(PPP, encoding='utf-8').read().split('\n') if os.path.exists(PPP) else None
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def rbody(n):   # copied verbatim from r2-ch19a.py (there from r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
strip_md = lambda s: re.sub(r'[*_`]+', '', s)
def sites(pat, vols=VOL, flags=re.I): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
appB = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix B ', l)][-1]; appC = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix C ', l)][-1]
unit = (appB, appC); UL = M[unit[0] - 1:unit[1] - 1]; N = len(UL)
def uline(pat, flags=re.I): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l, flags)]
joined = norm(strip_md(' '.join(UL)))
hr('§0 UNIT — `## Appendix B` L%d to `## Appendix C` L%d, %d lines (own scan)' % (unit[0], unit[1], N))
print('  headings in the unit:', [(unit[0] + i, l[:50]) for i, l in enumerate(UL) if re.match(r'^#', l)])

hr('§1 RULING 46 — script names, build numbers, internal file references; RULING 45 — build/editorial-process narration (candidates listed, not scored: docket 5/6, chat 115\'s split)')
r46 = [(i, norm(M[i - 1])[:120]) for i in uline(r'\b[\w-]+\.(py|md|tsv|json|csv|txt)\b|BUILD\d+|\bT\d+-[A-Z]\b|MANIFEST', 0)]
print('  Ruling 46 probe hits (%d):' % len(r46), r46)
print('  `COORDINATES-2.13` L%s: the delivered data companion, named by the Spectra Compendium under *The file* and by Register 1727 — a reader-facing file name, not an internal reference (recorded, not scored)' % uline(r'COORDINATES-2\.13', 0))
r45 = ['once read', 'ruling 26', 'register 1578', 'registers 630', 'hash-verified', 'owed a rebuild', 'drifted', 'the script', 'disclosed rather than reconciled', 'sealed', 'this build', 'this revision', 'earlier version', 'earlier draft']
print('  Ruling 45 candidates:', [(p, uline(re.escape(p))) for p in r45 if uline(re.escape(p))])
print('  lowercase `register(s) N` names (G0i) at:', uline(r'\bregisters? \d', 0), '; `Registers N` cites at:', uline(r'\bRegisters? \d', 0))
print('  the italic retrospective paragraph L%s–L%s: opens with `*This paragraph once read`: %s — docket 15 (narrated-past-state) kind; PP\'s B.2 was a different paragraph (§4)' % (uline(r'^\s*\*This paragraph once read')[0], uline(r'reconciled\.\*')[0], bool(uline(r'^\s*\*This paragraph once read'))))

hr('§2 FIRST PERSON — carries mine and myself; the Roman numeral in a species (He I, Li I, K I …) is excluded by the species-name guard')
fp = re.compile(r'(?<![A-Za-z])(I|my|mine|myself|we|our|ours|us)(?![A-Za-z])')
hits = []
for k, l in enumerate(UL):
    for m in fp.finditer(l):
        pre = l[max(0, m.start() - 3):m.start()]
        if m.group(1) == 'I' and re.search(r'[A-Z][a-z]? $', pre): continue   # species numeral: "He I", "Li I", "Na I", "K I"
        hits.append((unit[0] + k, m.group(1), l[max(0, m.start() - 20):m.end() + 20]))
print('  first-person hits after the species guard: %d %s' % (len(hits), hits))
print('  Roman-numeral `I` occurrences excluded (species names): %d' % sum(1 for l in UL for m in re.finditer(r'(?<![A-Za-z])I(?![A-Za-z])', l) if re.search(r'[A-Z][a-z]? $', l[max(0, m.start() - 3):m.start()])))

hr('§3 STRUCTURE — bold lead-ins, italic paragraphs, code lines, tables (| outside code), whitespace tables, long lines, unmarked sub-headings')
print('  bold lead-ins (line starts with ** after optional space):', uline(r'^\s*\*\*', 0))
print('  italic whole paragraphs (start with * not **, end with *):', [i for i in uline(r'^\s*\*[^*]', 0)])
code = [unit[0] + k for k, l in enumerate(UL) if l.startswith('    ')]; print('  4-space code lines: %d %s' % (len(code), code))
print('  markdown table rows (`|` at line start outside code): %s' % [unit[0] + k for k, l in enumerate(UL) if l.lstrip().startswith('|') and not l.startswith('    ')])
ws = [unit[0] + k for k, l in enumerate(UL) if re.match(r'^  \S.*\s{3,}\S', l)]; print('  whitespace-aligned table lines (2-space indent, ≥3 internal spaces): %d %s' % (len(ws), ws))
print('  B.1 table: header L%s, DATA rows (compilation lines) %s, citation lines %s, wrapped continuation L%s' % (uline(r'^  compilation', 0), uline(r'^  [A-Z][A-Za-z& ]+ {3,}[A-Z]', 0)[1:] if uline(r'^  compilation', 0) else None, uline(r'^  (\d{4}|JPCRD)', 0), uline(r'^ {28,}\S', 0)))
print('  B.3 table: header L%s, DATA rows %d %s' % (uline(r'^  species\s+channel', 0), len(uline(r'^  (Al|Li|Si) I{1,2}\s', 0)), uline(r'^  (Al|Li|Si) I{1,2}\s', 0)))
print('  lines over 400 chars:', [(unit[0] + k, len(l)) for k, l in enumerate(UL) if len(l) > 400])
print('  unmarked sub-heading test (blank above, short, no terminal punctuation):', [(unit[0] + k, l[:40]) for k, l in enumerate(UL) if k and not UL[k - 1].strip() and l.strip() and len(l.strip()) < 60 and not re.search(r'[.:;,]$', l.strip()) and not l.startswith('#') and not l.startswith('  ')])
print('  Statement / Proof / ∎ / Remark counts: %s' % {w: len(uline(r'\b' + w, 0)) for w in ('Statement', 'Proof', '∎', 'Remark', 'Verified')})
print('  backticked tokens:', sorted(set(re.findall(r'`([^`]+)`', ' '.join(UL)))))
print('  `Serving PART V — THE METHOD` L%s; the volume\'s Part V heading: %s' % (uline(r'Serving PART V', 0), [(i, M[i - 1][:40]) for i, l in enumerate(M, 1) if re.match(r'^# PART V ', l)]))

hr('§4 PRE-PP — what changed after Prints & Proofs (r2-ch20a §8 diffs the lines; here the substantive changes are named and tested)')
if PP is None: print('  PP not on disk — BUDGET')
else:
    ppB = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix B ', l)][-1]; ppC = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix C ', l)][-1]; PU = PP[ppB - 1:ppC - 1]
    pl = lambda pat: [ppB + k for k, l in enumerate(PU) if re.search(pat, l)]
    print('  PP `Serving PART IV` P%s → volume `PART V` (the Parts renumbered after PP: PP `# PART` headings %d, volume %d)' % (pl(r'Serving PART IV'), sum(1 for l in PP if re.match(r'^# PART', l)), sum(1 for l in M if re.match(r'^# PART', l))))
    print('  PP `Chapters 13 and 14` P%s → volume `Chapters 22 and 23` L%s; PP chapter 13/14 headings: %s; volume 22/23: %s' % (pl(r'Chapters 13'), uline(r'Chapters 22', 0), [(i, norm(l)[:40]) for i, l in enumerate(PP, 1) if re.match(r'^#+ 1[34]\. ', l)][-2:], [(i, norm(l)[:40]) for i, l in enumerate(M, 1) if re.match(r'^## 2[23]\. ', l)][-2:]))
    print('  PP `ionisation limits listed in B.2` P%s → volume `carried per channel in the Spectra Compendium, Part II` L%s + the COORDINATES sentence L%s (post-PP addition; Register 1727 names the file)' % (pl(r'listed in B\.2'), uline(r'carried per channel', 0), uline(r'COORDINATES', 0)))
    print('  PP `KI` P%s → volume `K I` L%s; PP `The 133 channel rows` P%s → `The channel rows` L%s; PP totals line `153 channels, 1105 cells, bracket 1105/1105` P%s — in the volume the same figures survive at the opener L%s' % (pl(r'Sansonetti 2008, +KI'), uline(r'Sansonetti 2008, +K I', 0), pl(r'The 133 channel rows'), uline(r'The channel rows', 0), pl(r'Totals: 153 channels'), uline(r'153 channels', 0)))
    print('  PP\'s B.2 count paragraph (133 rows / 869 / spectra.py) P%s → the volume\'s 596-row paragraph L%s and the italic retrospective L%s; PP\'s `stated and not tabulated` gap paragraph P%s has no volume counterpart (the twenty-channel gap is now narrated inside the retrospective L%s)' % (pl(r'generated by `spectra\.py`'), uline(r'596 channel', 0), uline(r'once read', 0), pl(r'stated and not tabulated'), uline(r'twenty-channel gap', 0)))
    print('  PP B.3 header split P%s (specie / s; δ / spread) → one line L%s (Register 1774 restores the header from the witness)' % (pl(r'^\s*specie\s'), uline(r'^\s*species\s+channel', 0)))

hr('§5 NEGATIVES AND SUPERLATIVES WITH THEIR WITNESSES')
for p in ['none is unexplained', 'No fitted parameter', 'the only inputs', 'zero cells refused', 'not of definition', 'no rows', 'cannot drift', 'Every computation', 'Every channel', 'Every number', 'Every flag']:
    print('  %-28s L%s' % (p, uline(re.escape(p), 0)))
print('  "Every computation in this book is reproducible" (L%s): a universal — recorded under docket 19 as a claim the unit cannot test (no computation is run by the appendix); its witnesses named: the level tables (SC Part II), the rules of Chapters 22–23, the COORDINATES file (r2-ch20a §6)' % uline(r'Every computation', 0))
print('  "the only inputs are measured or calculated energy levels, their stated uncertainties, and the ionisation limits" (L%s–L%s): Register 905 (SC closes stating uncertainties are supplied by five of 49 species) — read: %s' % (uline(r'the only inputs', 0), uline(r'ionisation limits', 0), norm(rbody(905))[:260]))
print('  "No fitted parameter enters at any point" across the six volumes (`fitted parameter`):', {k: v[:6] for k, v in sites(r'fitted parameter').items()})

hr('§6 DOCKET 27 — sentence recurrence across the six volumes (sentences of ≥ 6 words from the unit, markup-stripped, whitespace-normalised)')
sents = [s.strip() for s in re.split(r'(?<=[.;])\s+', joined) if len(s.split()) >= 6]
allv = {v: norm(strip_md(' '.join(t))) for v, t in VOL.items()}
rec = []
for s in sents:
    c = {v: allv[v].count(s) for v in allv}; tot = sum(c.values())
    if tot > 1 or (c.get('main', 0) == 0): rec.append((s[:90], c))
print('  sentences tested: %d; recurring (count > 1 across the six volumes, main included): %d' % (len(sents), len(rec)))
for s, c in rec: print('    ', s, {k: v for k, v in c.items() if v})
print('  B.1 and B.3 are printed twice by design (main Appendix B and SC Part IV) — Register 1774: "the Spectra Compendium\'s §B.3 and the main volume\'s are the same block"; docket 27 verdict for the unit: %s' % ('CLEAN apart from the SC Part IV copy that Register 1774 makes deliberate' if all(set(k for k, v in c.items() if v) <= {'main', 'sc'} for s, c in rec) else 'RECURRENCE OUTSIDE THE SC COPY — read the list'))

hr('§7 DOCKET 36 — authors named in the unit against the References body (word-bounded); docket 11 — 4ν/3 site')
refs = [i for i, l in enumerate(M, 1) if re.match(r'^## References', l)][-1]; refbody = '\n'.join(M[refs:])
auth = ['Kaufman', 'Martin', 'Kramida', 'Sansonetti', 'Hori', 'Korobov', 'Singer', 'Stanojevic', 'Weidemüller', 'Côté', 'Sugar', 'Corliss', 'Musgrove']
missing = [a for a in auth if has_token(refbody, a) == 0]
print('  authors named: %d; absent from the References body: %s; JPCRD (the journal, not an author) in References: %d, in main outside the unit: %s' % (len(auth), missing, has_token(refbody, 'JPCRD'), [i for i in sites(r'JPCRD', {'main': M})['main'] if not (unit[0] <= i < unit[1])][:5]))
print('  4ν/3 at L%s (docket 11 scope: the 5 %% departure criterion); `5%%` sites in the unit: %s' % (uline(r'4ν/3', 0), uline(r'5%', 0)))
print('  `T8-J` across the six volumes:', {k: v[:5] for k, v in sites(r'\bT8-J\b', flags=0).items()}, '; `ruling 26` (lowercase):', {k: v[:5] for k, v in sites(r'\bruling 26\b', flags=0).items()})

hr('§8 POINTERS — every pointer in the unit resolved to the claim, not the heading')
print('  `Chapter 24` L%s → `## 24. The collection` L%s; the union / 763 / earlier verification: r2-ch20a §3 (Chapter 24 carries 1,442 = 1,105 + 337 at L6970; no 763, no union)' % (uline(r'Chapter 24', 0), [i for i, l in enumerate(M, 1) if re.match(r'^## 24\. ', l)]))
print('  `Spectra Compendium, Part II` L%s → SC `# II · THE CHANNELS` S%s; `*The file*` L%s → SC `## The file` S%s' % (uline(r'Spectra Compendium, Part II', 0), [i for i, l in enumerate(VOL['sc'], 1) if re.match(r'^# II ', l)], uline(r'\*The file\*', 0), [i for i, l in enumerate(VOL['sc'], 1) if re.match(r'^## The file', l)]))
print('  `Chapters 22 and 23` L%s → the bracket (22.1 The rule … Rule 1 at L6040) and the cost surface (§23.10.4 the admissibility rule); r2-ch20a §6' % uline(r'Chapters 22', 0))
print('  Register pointers in the unit: %s → all present (r2-ch20a §3, §7), no WARNING on any' % sorted(set(int(x) for l in UL for x in re.findall(r'(?<![\d,.])(1[5-7]\d\d|6[0-9]\d)(?![\d,])', l) if int(x) in (630, 631, 1578, 1699, 1700, 1763, 1768))))
