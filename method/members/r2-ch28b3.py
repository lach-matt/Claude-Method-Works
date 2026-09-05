# r2-ch28b3.py — successor of r2-ch28b2.py (md5 8ebe3662ea4e02920f37f5a7411f4fbb), W-235 / DEF-153N: the predecessor's range(1701, 1713) of REGISTER
# NUMBERS had its 1701 turned into _L(<main-volume text at L1701>) by tools/reanchor.py (its documented blind spot — a number
# in the line range that is not a line), so when main moved +5 above L1452 the range began at 1706 and the banked counts
# over registers 1701–1712 fell from the original r2-ch28b's 2 and 1 to 1 and 0. One replacement: the numbers are numbers
# again. Nothing else changes.
# r2-ch28b.py — the unit main `## References` (LAST hit) to the end of the member: the PROSE / ATTRIBUTION / PP / FORMATTING claims (chat 141).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic. Docket 36 both directions (every name cited in the six
# volumes against the References body; every References surname against the six volumes); PP `# References` diffed with numbers stripped BOTH
# sides; Ruling 45 / 46 / first-person probes (`mine`, `myself` carried; a species Roman numeral excluded); narrated-past-state probes;
# section taxonomy (subject keys per R.n); entry formatting (blank-line-split entries, inline ` · ` separators, bold vs plain author names).
# r2-ch28b2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch28b.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (2 anchors); nothing else changes. r2-ch28b.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch28b.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
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
PC = L.read_member('The_Method_1_6___The_Physics_Compendium-2.md').split('\n')
IOI = L.read_member('The_Method_1_6___The_Index_of_Indices-2.md').split('\n')
SC = L.read_member('The_Method_1_6___Spectra_Compendium-2.md').split('\n')
P = L.read_member('PP_The_Method_1_6.md').split('\n') if os.path.exists(os.path.join(H, 'PP_The_Method_1_6.md')) else open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
def hr(t): print('\n== ' + t)
def rbody(n):   # copied verbatim from r2-ch27b.py (there from r2-ch26b.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def body_range(M, sec):   # copied verbatim from r2-ch27b.py (there from r2-ch26b.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def lettered(M, tag):   # copied verbatim from r2-ch27b.py (there from r2-ch26b.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def cnt(lines, pat, flags=re.I): return sum(len(re.findall(pat, l, flags)) for l in lines)
def sites(lines, pat, flags=0): return [i + 1 for i, l in enumerate(lines) if re.search(pat, l, flags)]
def join(lines): return re.sub(r'\s+', ' ', re.sub(r'[*_`>]', '', ' '.join(lines)))
def enc(ln): return next('L%d %s' % (j, M[j - 1][:60]) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s', M[j - 1]))
rf = [i + 1 for i, l in enumerate(M) if re.match(r'^#{1,3} References\b', l)]; s = rf[-1]; U = M[s - 1:]; UJ = join(U); MAIN = M[:s - 1]
VOL = {'main': MAIN, 'reg': R, 'mc': MC, 'pc': PC, 'ioi': IOI, 'sc': SC}
print('  unit L%d–L%d (%d lines); the volumes tested: main (outside the unit), reg, mc, pc, ioi, sc' % (s, len(M), len(U)))

hr('§0 PP `# References` (LAST hit) to the end of PP, diffed with section numbers stripped BOTH sides; PP\'s R.n headings and entry counts')
pr = [i + 1 for i, l in enumerate(P) if re.match(r'^\s*#{1,3}\s*References\b', l)]; a = pr[-1]; PU = P[a - 1:]
strip = lambda l: re.sub(r'\s+', ' ', re.sub(r'§+\s*[\dA-Z][\d.]*', '§', re.sub(r'[*_`]', '', l))).strip()
mb = {strip(l) for l in U if l.strip() and not l.startswith('#')}; pb = {strip(l) for l in PU if l.strip() and not re.match(r'^\s*#', l)}
print('  PP References P%d–P%d (%d lines); body lines main %d, PP %d, shared %d, only-main %d, only-PP %d' % (a, len(P), len(PU), len(mb), len(pb), len(mb & pb), len(mb - pb), len(pb - mb)))
om = [(s + i, U[i].strip()[:64]) for i in range(len(U)) if U[i].strip() and not U[i].startswith('#') and strip(U[i]) not in pb]
op = [(a + i, PU[i].strip()[:64]) for i in range(len(PU)) if PU[i].strip() and not re.match(r'^\s*#', PU[i]) and strip(PU[i]) not in mb]
print('  only-main lines (%d): %s' % (len(om), om))
print('  only-PP lines (%d): %s' % (len(op), op))
ph = [(a + i, PU[i].strip()[:50]) for i in range(len(PU)) if re.match(r'^\s*#{1,4}\s', PU[i])]; print('  PP headings in its References: %s' % ph)
def paras(lines, lo):
    A = []
    for j, l in enumerate(lines):
        if not l.strip() or l.lstrip().startswith('#'): continue
        if j == 0 or not lines[j - 1].strip() or lines[j - 1].lstrip().startswith('#'):
            if not re.match(r'^\s{2,}\S', l) or re.match(r'^\s*[·•]', l): A.append(lo + j)
    return A
r5p = [i for i, t in ph if t.startswith('### R.5')]
if r5p:
    e5 = next((i for i, t in ph if i > r5p[0]), len(P) + 1); pp5 = paras(P[r5p[0]:e5 - 1], r5p[0] + 1)
    print('  PP R.5 P%d–P%d paragraph entries %d; PP lines carrying `thirteen` in R.5: %s' % (r5p[0], e5 - 1, len(pp5), [(i, P[i - 1].strip()[:70]) for i in range(r5p[0], e5) if 'thirteen' in P[i - 1]]))
print('  PP\'s lead-in line position: %s (main L11554 sits AFTER two bold blocks and BEFORE R.1)' % [(a + i, PU[i].strip()[:60]) for i in range(len(PU)) if 'Every work cited' in PU[i]])
print('  PP lines carrying `Atomic coupling schemes` / `Constraint satisfaction, consistency`: %s' % [(a + i, PU[i].strip()[:50]) for i in range(len(PU)) if re.search(r'Atomic coupling schemes|Constraint satisfaction, consistency', PU[i])])

hr('§1 docket 36, direction 1: every name owed by the docket (chats 113–140) against the References body; sites outside the unit per volume (word-bounded, case-sensitive)')
OWED = ['Habib', 'Nourine', 'Thierry', 'Kurucz', 'VALD', 'BRASS', 'Hasse', 'QSAR', 'NextClosure', 'Roche', 'Titius', 'Bode', 'Regge', 'Hagedorn', 'Gröbner', 'Klemm', 'Knaster', 'Tarski',
        'Schrödinger', 'Demkov', 'Ostrovsky', 'Klechkovskii', 'Pauli', 'Seaton', 'Pulay', 'Griffin', 'Andrew', 'Cowan', 'Xia', 'Routh', 'Fourier', 'Motzkin', 'Borchers', 'Wiesbrock', 'Hadamard', 'Rota', 'Birkhoff', 'Freuder', 'Montanari']
for nm in OWED:
    inu = cnt(U, r'(?<![A-Za-z])' + nm + r'(?![a-z])', 0); outs = {k: cnt(v, r'(?<![A-Za-z])' + nm + r'(?![a-z])', 0) for k, v in VOL.items()}
    print('  %-13s References body %d; outside %s %s' % (nm, inu, {k: v for k, v in outs.items() if v}, '← OWED (cited, unbibliographed)' if inu == 0 and sum(outs.values()) else ('present' if inu else 'not cited anywhere')))

hr('§2 docket 36, direction 2: every surname in the References body against the six volumes (a surname followed by an initial, `&`, `and`, a comma, an en dash or a year bracket; markup stripped); names cited nowhere else')
def surnames(lines):
    c = Counter()
    for l in lines:
        for m in re.finditer(r"(?<![A-Za-z'’\-])([A-Z][a-zäöüéèçøÅ'’\-]{2,})(?=\s*(?:,\s*[A-Z]\.|\(|&|and\b|,|–|—|\s+\d{4}))", re.sub(r'[*_`]', '', l)): c[m.group(1)] += 1
    return c
STOP = {'Cited', 'Entered', 'Every', 'Also', 'The', 'Registers', 'Register', 'Queried', 'Its', 'Located', 'Retrieved', 'That', 'Different', 'Seniority', 'This', 'Those', 'Springer', 'Berlin', 'Leipzig', 'Glasgow', 'Physics', 'Data', 'Ref', 'Chem', 'Phys', 'Rev', 'Lett', 'Math', 'Ann', 'Sci', 'Proc', 'Soc', 'Amer', 'Trans', 'Discrete', 'Algebra', 'Universalis', 'Order', 'Information', 'Sciences', 'Artificial', 'Intelligence', 'Nature', 'Interval', 'Analysis', 'Partial', 'Identification', 'Probability', 'Distributions', 'Interior', 'Point', 'Polynomial', 'Algorithms', 'Convex', 'Programming', 'Duke', 'Combinatorial', 'Semigroup', 'Forum', 'Formal', 'Concept', 'Universal', 'Computer', 'Science', 'Counting', 'Complexity', 'Master', 'University', 'Waterloo', 'Doubly', 'Characterizations', 'Totally', 'Networks', 'From', 'Constraint', 'Coupling', 'Some', 'Comments', 'Novi', 'Comm', 'Acad', 'Petrop', 'Prix', 'Roy', 'Paris', 'Vorlesungen', 'Dynamik', 'Invent', 'Sbornik', 'Moscow', 'Celest', 'Mech', 'Inf', 'Artif', 'Intell', 'Alg', 'Disc', 'Meth', 'Comput', 'Syst', 'Combin', 'Theory', 'Pacific', 'Handbuch', 'Physik', 'Encyclopedia', 'Encyklopädie', 'Mathematischen', 'Wissenschaften', 'Seriengesetze', 'Linienspektren', 'Linienspektra', 'Spektren', 'Elemente', 'Wie', 'Serie', 'Grenze', 'Triadophilia', 'Hodge', 'Hill', 'Frattini', 'Maximal', 'Embeddings', 'Deciding', 'Characterising', 'Subregion', 'Type', 'Galois', 'Boolean', 'Chinese', 'Double', 'Lemma', 'Physical', 'Mathematical', 'Compendium', 'Fifty', 'Rydberg', 'Chapter', 'Part', 'Term', 'Anthropic', 'Claude', 'Indexing', 'Muon', 'Catalysed', 'Fusion', 'Matter', 'Time', 'Travel', 'Three', 'Body', 'Problem', 'Unknown', 'Masses', 'Solution', 'Löwdin', 'Springer', 'Cambridge', 'Prentice', 'Hall', 'Comptes', 'Rendus', 'Norm', 'Sup', 'Mém', 'Jacobi', 'Kolmogorov', 'Arnold', 'Moser', 'Alekseev', 'Brudno', 'Bergman', 'Boole', 'Nörlund', 'Steffensen', 'Seki', 'Kōwa', 'Janet', 'Racah', 'Maupertuis', 'Painlevé', 'Poincaré', 'Gödel', 'Lagrange', 'Euler', 'Dilworth', 'Nash', 'Sansonetti', 'Kramida', 'Sugar', 'Kaufman', 'Kimura', 'Madelung', 'Gerratt', 'Ritz', 'Edlén', 'Aitken', 'Shanks', 'Shannon', 'Manski', 'Moore'}
sn = surnames([l for l in U if not l.startswith('#')])
names = sorted(n for n in sn if n not in STOP or n in {'Hill', 'Moore', 'Janet', 'Racah', 'Rydberg', 'Ritz', 'Edlén', 'Aitken', 'Shanks', 'Shannon', 'Manski', 'Dilworth', 'Euler', 'Lagrange', 'Gödel', 'Poincaré', 'Painlevé', 'Maupertuis', 'Jacobi', 'Kolmogorov', 'Arnold', 'Moser', 'Alekseev', 'Brudno', 'Bergman', 'Boole', 'Nörlund', 'Steffensen', 'Seki', 'Nash', 'Sansonetti', 'Kramida', 'Sugar', 'Kaufman', 'Kimura', 'Madelung', 'Gerratt', 'Löwdin'})
print('  surnames extracted %d (convention above; a STOP list of journal/title words is applied and printed in the source)' % len(names))
nowhere = []
for nm in names:
    outs = {k: cnt(v, r'(?<![A-Za-z])' + re.escape(nm) + r'(?![a-z])', 0) for k, v in VOL.items()}
    if sum(outs.values()) == 0: nowhere.append(nm)
print('  cited in the References and NOWHERE in the six volumes (%d): %s' % (len(nowhere), nowhere))
ART = [n for n in nowhere if n in ('Physikers', 'Std', 'Team', 'Archives', 'Atomic', 'August')]; print('  extraction artefacts among them (title/organisation words, not surnames): %s' % ART)
for nm in ('Huang', 'Taylor', 'Duquenne', 'Guigues', 'Nash', 'Ralchenko', 'Reader', 'Sharp', 'Stephen', 'Kimura', 'Makino', 'Dunz', 'Runge', 'Paschen', 'Götze', 'Manski', 'Nörlund', 'Steffensen', 'Seki', 'Larson', 'Tucker', 'Lubiw', 'Hoffman', 'Kandula', 'Drake'):
    print('    %-11s outside the unit: %s' % (nm, {k: v for k, v in {k: cnt(v, r'(?<![A-Za-z])' + re.escape(nm) + r'(?![a-z])', 0) for k, v in VOL.items()}.items() if v} or 'NONE'))
print('  the rest, cited somewhere: %s' % {nm: {k: v for k, v in {k: cnt(v, r'(?<![A-Za-z])' + re.escape(nm) + r'(?![a-z])', 0) for k, v in VOL.items()}.items() if v} for nm in names if nm not in nowhere})

hr('§3 L11818 "Hill 1878, Poincaré 1890, Freuder 1982 and Mardling & Aarseth 2001 are cited above and reused"; R.7 Löwdin block vs the chapter; R.7 three-body names vs Chapter 36 and Register 1713–1724')
for nm, yr in (('Hill', '1878'), ('Poincaré', '1890'), ('Freuder', '1982'), ('Mardling', '2001')):
    above = [s + i for i in range(len(U)) if s + i < _L(' **The three-body problem.** Entered at registers 1713–1724. Hill 1878, Poincaré 1890, Freuder 1982 and Mardling & Aarseth 2001 are cited above and reused.') and nm in U[i] and yr in U[i]]; print('  %-9s %s: above L11818 at %s' % (nm, yr, above))
ap = [i + 1 for i, l in enumerate(M) if l.startswith('# APPENDICES')][-1]   # chat-130 convention: Chapter 36 ends at `# APPENDICES`, never at the member's end
c35, c36 = section_span(M, '35'), (heading_line(M, '36'), ap); j35, j36 = join(M[c35[0] - 1:c35[1] - 1]), join(M[c36[0] - 1:c36[1] - 1])
print('  Chapter 36 bounded L%d–L%d by `# APPENDICES` L%d (section_span would give %s — wrong, it runs to the member\'s end)' % (c36[0], c36[1] - 1, ap, section_span(M, '36')))
for nm in ('Löwdin', 'Koelling', 'Harmon', 'Griffin', 'Andrew', 'Cowan', 'Pulay', 'Gerratt', 'Mills', 'Madelung'):
    print('  Löwdin block %-9s Chapter 35 %s %d; Register 1701–1712 %d' % (nm, c35, len(re.findall(r'(?<![A-Za-z])' + nm + r'(?![a-z])', j35)), sum(1 for i in range(len(R)) if nm in R[i] and any(R[k].strip() == '### %d' % n for n in range(1701, 1713) for k in range(max(0, i - 3), i + 1)))))
for nm in ('Montgomery', 'Chenciner', 'Hsiang', 'Straume', 'Chazy', 'Saari', 'Fleischer', 'Knauf', 'Painlevé', 'McGehee', 'Kolmogorov', 'Arnold', 'Moser', 'Alekseev', 'Brudno', 'Marchal', 'Bozis', 'Monaghan', 'Nash', 'Stone', 'Leigh', 'Kol', 'Moore', 'Maupertuis', 'Jacobi', 'Euler', 'Lagrange'):
    rr = sorted({int(re.sub(r'\D', '', R[max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k]))])) for i in sites(R, r'(?<![A-Za-z])' + nm + r'(?![a-z])') if 1713 <= int(re.sub(r'\D', '', R[max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k]))])) <= 1724})
    print('  three-body block %-11s Chapter 36 %s %d; Register 1713–1724 entries %s' % (nm, c36, len(re.findall(r'(?<![A-Za-z])' + nm + r'(?![a-z])', j36)), rr))
print('  L11820 "every structural object of Chapter 36 is his or older": `Montgomery` sites in main outside the unit %s; in MC %s' % (sites(MAIN, r'Montgomery')[:8], sites(MC, r'Montgomery')[:8]))

hr('§4 Ruling 45 / 46 / narrated-past-state / first-person probes on the unit')
for pat, why in ((r'\w+\.py\b', 'script name (R46)'), (r'\d{1,2} [A-Z][a-z]+ 20\d\d', 'a date (R45 candidate; a database query date is bibliographic)'), (r'previously attributed', 'narrated past state (docket 15)'),
                 (r'had been crediting', 'narrated past state (docket 15)'), (r'went unused for four cycles', 'editorial-process remark (R45)'), (r'An earlier draft', 'narrated past state (docket 15)'),
                 (r'withdrawn and reinstated', 'editorial-process remark (R45)'), (r'walked into', 'narrated process (R45 candidate)'), (r'recomputed here', 'process statement (verification claim)'),
                 (r'closing search', 'process remark (R45)'), (r'until §2\.23', 'narrated past state (docket 15)'), (r'\[F\]|\[S\]', 'reading-status marks (undefined in the unit)'), (r'not read directly|not read in full|was not read', 'reading-status statement'),
                 (r'\(Anthropic\)', 'the AI collaborator named as author (noted, not scored)'), (r'this book previously|this volume', '—')):
    h = sites(U, pat); print('  %-44s %s → %s' % (pat, why, ['L%d' % (s + i - 1) for i in h]))
fp = [(s + i - 1, l.strip()[:80]) for i, l in enumerate(U, 1) if re.search(r"(?<![A-Za-z])(I|my|mine|myself|we|our|ours)(?![A-Za-z])", l) and not re.search(r'\b[A-Z][a-z]+ I\b|\bI\.|\bH I\b|\bHe I\b', l)]
print('  first person (I / my / mine / myself / we / our; a species Roman numeral and an initial `I.` excluded): %s' % (fp or 'none'))

hr('§5 taxonomy: each R.n heading\'s subject against its entries (subject keys named); entries whose text carries none of the section\'s keys')
hs = [(i + 1, M[i]) for i in range(s - 1, len(M)) if re.match(r'^### R\.\d', M[i])]
KEYS = {'R.1': ['level', 'spectra', 'spectrum', 'ionis', 'ioniz', 'NIST', 'ASD', 'Chem. Ref. Data', 'limits'], 'R.2': ['antiproton', 'Rydberg', 'exotic', 'collective'], 'R.3': ['series', 'quantum defect', 'Rydberg', 'Ritz', 'coupling', 'seniority', 'companion', 'Seriengesetze'],
        'R.4': ['bound', 'acceleration', 'rigour', 'interval', 'extrapolat', 'credibility', 'zero-error', 'decrement', 'difference'], 'R.5': ['lattice', 'sublattice', 'closure', 'order', 'poset', 'antichain', 'chain', 'matri', 'consecutive', 'Moore famil', 'convex', 'partition', 'dichotomy', 'CSP', 'projection', 'Frattini', 'interval', 'dimension', 'implication', 'closed set', 'left-step'],
        'R.6': ['three-body', 'Hill', 'incompleteness', 'equilibrium', 'polytope', 'Hodge', 'mirror', 'triple', 'transfer'], 'R.7': []}
for k, (i, t) in enumerate(hs):
    hi = hs[k + 1][0] - 1 if k + 1 < len(hs) else len(M); tag = t[4:7]
    A = paras(M[i:hi], i + 1); miss = []
    for a in A:
        e = next((j for j in range(a + 1, hi + 2) if j > hi or not M[j - 1].strip()), hi + 1); txt = join(M[a - 1:e - 1])
        if KEYS[tag] and not any(re.search(kk, txt, re.I) for kk in KEYS[tag]): miss.append((a, txt[:70]))
    print('  %s L%d–L%d entries %d; carrying none of %s: %s' % (tag, i, hi, len(A), KEYS[tag][:4] + ['…'], miss))
print('  R.5 physics/spectroscopy entries by name (Van Isacker, Racah 1954, Chandrasekaran, Dunz, Janet) at %s' % [(s + i, U[i].strip()[:40]) for i in range(len(U)) if re.search(r'Van Isacker|Chandrasekaran|Dunz, |Janet, C', U[i])])
print('  R.1 non-spectroscopic entry (Kimura … polyhedra) at %s' % [(s + i, U[i].strip()[:60]) for i in range(len(U)) if 'Kimura' in U[i]])

hr('§6 formatting (docket 28): entries split by a blank line mid-citation; inline ` · ` separators joining several works on one paragraph; bold vs plain author names per section; missing initials; `[unread]` placement')
split_ = [(s + i, U[i].strip()[:50], U[i + 2].strip()[:30]) for i in range(len(U) - 2) if U[i].strip() and not U[i + 1].strip() and re.match(r'^\s{1,2}\d+[.,]|^\s{1,2}\d{3,4}\.', U[i + 2]) and re.search(r'\d+,\s*$', U[i])]
print('  entries split by a blank line before the page number: %s' % split_)
inl = [(s + i, len(re.findall(r' · ·? ?\*\*', U[i]))) for i in range(len(U)) if re.search(r' · ·? ?\*\*', U[i])]; print('  lines carrying inline ` · **` separators (works run together on one paragraph): %s' % inl)
for k, (i, t) in enumerate(hs):
    hi = hs[k + 1][0] - 1 if k + 1 < len(hs) else len(M); A = paras(M[i:hi], i + 1)
    bold = [a for a in A if re.match(r'^\s*(·\s*)?\*\*', M[a - 1])]; print('  %s author names bold %d / plain %d of %d entries' % (t[4:7], len(bold), len(A) - len(bold), len(A)))
print('  missing initial / dash placeholder: %s' % [(s + i, U[i].strip()[:40]) for i in range(len(U)) if re.search(r'^\s*[A-Z][a-z]+, —', U[i])])
print('  `[unread]` inside the citation (after the title) vs at the end: %s' % [(s + i, U[i].strip()[:60]) for i in range(len(U)) if '[unread]' in U[i]])
print('  bullet forms: ` · ` leading %d lines; none-leading entries %d; `**Sansonetti**`-style bold-author entries in R.1 beside plain ones (mixed within one section): see the per-section counts above' % (cnt(U, r'^\s*·\s', 0), cnt(U, r'^\s[A-Z][a-z]+,\s[A-Z]', 0)))
print('  L11592 / L11604 / L11816 / L11840 companion papers: cited with `Lach, M. & Claude (Anthropic)` %d times, `Lach, M.` alone %d times (an inconsistent author form for the same series)' % (cnt(U, r'Lach, M\. & Claude', 0), cnt(U, r'Lach, M\. \(20', 0)))
