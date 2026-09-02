# r2-ch23b.py — Appendix D part 2 (main L10462–L10897, D.5–D.6), the PROSE and POINTER claims (chat 136).
# Reads MEMBERS by name (never a bundle path) and the Prints & Proofs original at /home/claude/PP_The_Method_1_6.md; imports r2lib by path; deterministic.
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
PPp = '/home/claude/PP_The_Method_1_6.md'; PP = open(PPp, encoding='utf-8').read().split('\n') if os.path.exists(PPp) else None

def rbody(n):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch22a.py (there from r2-ch21a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

print('r2-ch23b — Appendix D part 2 (D.5–D.6), prose and pointers')
d5 = [i for i, l in enumerate(M, 1) if re.match(r'^### D\.5 ', l)][-1]; e = lettered(M, 'Appendix E')[-1]; U = M[d5 - 1:e - 1]
heads = [(i, l) for i, l in enumerate(M, 1) if d5 <= i < e and re.match(r'^#{1,4} ', l)]
print('§1 unit L%d–L%d, %d lines, %d headings, %d non-blank' % (d5, e - 1, len(U), len(heads), sum(1 for l in U if l.strip())))
strip = lambda l: re.sub(r'\s+', ' ', re.sub(r'[*_`]', '', l)).strip()

# §2 pre-PP diff. PP's D.n sub-headings are unmarked (indented one space after a blank line); the section number is stripped from BOTH sides.
if PP:
    pd = [i for i, l in enumerate(PP, 1) if re.match(r'^# Appendix D\b', l)]; pe = [i for i, l in enumerate(PP, 1) if re.match(r'^# Appendix E\b', l)]
    pp_heads = [(i, l) for i, l in enumerate(PP, 1) if pd[-1] < i < pe[-1] and re.match(r'^ D\.\d', l) and not PP[i - 2].strip()]
    print('§2 PP `# Appendix D` P%s `# Appendix E` P%s; unmarked ` D.n` sub-headings %d: %s' % (pd, pe, len(pp_heads), [l.split()[0] for i, l in pp_heads]))
    pp_titles = {re.sub(r'^D\.[\d.]+\s*', '', strip(l)): i for i, l in pp_heads}
    for i, l in heads:
        t = re.sub(r'^D\.[\d.]+\s*', '', strip(l.lstrip('# '))); print('   %s L%d %s → PP %s' % (l.split()[1], i, 'PRESENT P%d' % pp_titles[t] if t in pp_titles else 'ABSENT', '' if t in pp_titles else '(post-PP: D.5.9 / D.5.10)' if l.split()[1] in ('D.5.9', 'D.5.10') else '(CHECK)'))
    p5 = pp_titles.get('The closed index'); pp_body = [strip(l) for l in PP[p5:pe[-1] - 1] if l.strip() and not re.match(r'^ D\.\d', l)]
    m_body = [strip(l) for i, l in enumerate(M, 1) if d5 <= i < e and l.strip() and not re.match(r'^#{1,4} ', l)]
    cp, cm = Counter(pp_body), Counter(m_body); only_pp = list((cp - cm).elements()); only_m = list((cm - cp).elements())
    print('   body: PP non-blank %d, main non-blank %d, shared %d; only-PP %d, only-main %d' % (len(pp_body), len(m_body), sum((cp & cm).values()), len(only_pp), len(only_m)))
    m_idx = {strip(l): i for i, l in enumerate(M, 1) if d5 <= i < e}
    print('   only-main lines by section:', Counter(next(h.split()[1] for j, h in reversed(heads) if j <= m_idx.get(t, e)) for t in only_m))
    print('   only-PP lines (first 12):'); [print('      P', t[:150]) for t in only_pp[:12]]
    print('   only-main lines outside D.5.9/D.5.10 (first 14):')
    om = [(m_idx.get(t, 0), t) for t in only_m if m_idx.get(t, 0) < [i for i, l in heads if l.split()[1] == 'D.5.9'][0]]; [print('      L%d %s' % (i, t[:150])) for i, t in om[:14]]
else: print('§2 BUDGET: PP not on disk — the pre-PP diff is not taken this run')

# §3 pointers resolved to the CLAIM under both resolvers (convention: a pointer resolves when the section's body_range OR section_span carries every listed token, case-insensitive, word-bounded or raw for a symbol)
probes = [('14.1', ['closed index'], 'D.5.2 L10565 a closed index'), ('14.2', ['closure operator'], 'D.5.2 L10567 ℛ the closure operator'), ('16.2', ['closure operator'], 'D.5.1 L10546 ℛ the closure operator (the same element, §14.2 at L10567)'),
          ('6.1', ['E(X)'], 'E(X) = |ℛ(X)| − |X|'), ('11.8', ['rank polynomial'], 'rank polynomial of Λ'), ('29.11', ['closed'], 'A.2 precedent found (§29.11)'), ('30.3.3', ['total-order'], 'A.8 precedent (§30.3.3)'), ('30.3', ['reorderab'], 'the reorderability law'),
          ('7.3', ['976'], '|Λ| = 976 with E(Λ) = 0'), ('12.9', ['1,113,045,672'], 'maximal chains'), ('31.3.4', ['540'], '540 Kreuzer–Skarke proposals'), ('32.1.1', ['unfibred'], '4 unfibred flagged'), ('32.4.1', ['idempot'], 'ℛ closure operator proved: extensivity, monotonicity, idempotence'),
          ('11.1.1', ['17'], 'Λ as 976 words in {0,1}¹⁷'), ('18.4.1', ['arity'], 'the cap-arity criterion'), ('18.4.1', ['slack'], 'slack = kernel'), ('12.11.0.1', ['occupancy clock'], ''), ('12.11.0.2', ['one arrow'], ''), ('12.11.0.3', ['bridge'], ''), ('12.11.0.4', ['separation hypothesis'], ''),
          ('12.11.0.5', ['decay'], ''), ('12.11.0.6', ['union'], ''), ('16.8.5', ['step law'], ''), ('18.4.2', ['concave'], 'meet-closure of concave sets'), ('16.5', ['30,000'], 'A.5 checked on 30,000 sampled points (21a-07 site)'), ('16.5', ['total'], 'χ_Λ is total proved'),
          ('16.7.1', ['loop'], 'L10717 §16.7.1\'s loop (22b-01 twin)'), ('2.21', ['press'], 'count recomputed by the press at every build'), ('32.1.4', ['embarrass', 'author'], 'L10785 §32.1.4 working on its author'), ('12.11', ['tower'], 'Appendix D predates §12.11'), ('35', ['entrant'], 'LS.ent the entrant operator, §35'),
          ('23', ['4ν/3'], 'V = 4ν/3, §23'), ('22', ['Rydberg'], 'the Rydberg term, §22'), ('11', ['F(z)'], 'F(z) the single expression, §11'), ('17', ['extension'], '§17 says an extension should be')]
for sec, toks, why in probes:
    try: br = body_range(M, sec); ss = section_span(M, sec)
    except Exception as ex: print('§3 §%s NO HEADING (%s) — %s' % (sec, type(ex).__name__, why)); continue
    res = []
    for t in toks:
        b = sum(1 for l in M[br[0]:br[1] - 1] if (has_token(l, t) if re.match(r'^[A-Za-z][A-Za-z -]*$', t) else t in l) or t.lower() in l.lower())
        s = sum(1 for l in M[ss[0]:ss[1] - 1] if (has_token(l, t) if re.match(r'^[A-Za-z][A-Za-z -]*$', t) else t in l) or t.lower() in l.lower())
        res.append('%r body_range%s %d / section_span%s %d' % (t, br, b, ss, s))
    print('§3 §%s :: %s :: %s' % (sec, ' ; '.join(res), why))
print('   headings of the zero-hit sections:', [(sec, M[heading_line(M, sec) - 1][:60]) for sec in ('12.11.0.1', '12.11.0.2', '12.11.0.4', '12.11.0.5', '12.11.0.6', '16.8.5', '32.1.4')])
print('   heading of §14.1 / §14.2 / §16.2:', [M[heading_line(M, s) - 1][:70] for s in ('14.1', '14.2', '16.2')])
print('   `closure operator` sites outside the appendix (first 8):', [i for i, l in enumerate(M, 1) if 'closure operator' in l and not 9937 <= i][:8])
for t, pat in [('Theorem 7.1', r'Theorem 7\.1\b'), ('Theorem 14.1', r'Theorem 14\.1\b'), ('Theorem 17.1', r'Theorem 17\.1\b'), ('Theorem 18.1', r'Theorem 18\.1\b'), ('Theorem 18.2', r'Theorem 18\.2\b'), ('P20', r'\bP20\b'), ('P23', r'\bP23\b'), ('E.4.1', r'\bE\.4\.1\b'), ('item L', r'\bitem L\b'), ('Audits 2 and 3 / 24 of 24', r'24 of 24'), ('475,800', r'475,800'), ('figure-D.1', r'figure-D\.1'), ('what the law forbids', r'what the law forbids'), ('THE LAW', r'^#.*THE LAW')]:
    print('   %-28s sites %s' % (t, [i for i, l in enumerate(M, 1) if re.search(pat, l, re.I if t in ('what the law forbids',) else 0)][:8]))
print('   Theorem 7.1 withdrawn? lines with `withdrawn` within 3 of a Theorem 7.1 site:', [i for i, l in enumerate(M, 1) if re.search(r'Theorem 7\.1\b', l) and any('withdrawn' in M[k] for k in range(max(0, i - 3), min(len(M), i + 3)))][:6])
print('   Chapter 18 heading:', [M[i - 1][:80] for i, l in enumerate(M, 1) if re.match(r'^## 18\. ', l)][:1], '; Part III heading:', [M[i - 1][:80] for i, l in enumerate(M, 1) if re.match(r'^#\s*PART III\b', l)][:2])
print('   Chapter 29 `direction` sites in Chapter 29:', [i for i, l in enumerate(M, 1) if body_range(M, '29.1')[0] <= i < heading_line(M, '30.1') and has_token(l, 'direction')][:6], '; Chapter 16 `disjoint` sites:', [i for i, l in enumerate(M, 1) if heading_line(M, '16.1') <= i < heading_line(M, '17.1') and 'disjoint' in l][:6])

# §4 bibliography (docket 36): every author named in the unit against the `## References` body
ref = [i for i, l in enumerate(M, 1) if re.match(r'^## References', l)][-1]; refbody = '\n'.join(M[ref:])
for a in ['Fourier', 'Motzkin', 'Euler', 'Lagrange', 'Montgomery', 'Kreuzer', 'Skarke']:
    print('§4 %-11s unit sites %s ; in References body: %s' % (a, [i for i, l in enumerate(M, 1) if d5 <= i < e and a in l], bool(re.search(r'\b' + a + r'\b', refbody))))

# §5 probes: first person (mine, myself carried; Roman numerals of a species excluded), R45/R46 candidates, stale *sixteen fibres* sites, numeral twins
fp = re.compile(r"\b(I|my|mine|myself|we|our|ours)\b")
print('§5 first-person sites:', [(i, fp.findall(l)) for i, l in enumerate(M, 1) if d5 <= i < e and fp.search(l) and not re.search(r'\b[A-Z][a-z]? (I|II|III|IV|V|VI)\b', l)])
r45 = re.compile(r'\b(companion paper|compendium|register(?:s|ed)?|intake|at the time of writing|press|build|author|entry is kept|Q item)\b', re.I)
print('   R45 candidate lines (process / editorial words):', [(i, sorted(set(m.lower() for m in r45.findall(l)))) for i, l in enumerate(M, 1) if d5 <= i < e and r45.search(l)])
print('   R46 candidates (script / file names):', [i for i, l in enumerate(M, 1) if d5 <= i < e and re.search(r'\.py\b|BUILD\d|\.md\b|\.png\b', l)])
print('   *sixteen fibres* / *sixteen* sites in the unit:', [(i, re.findall(r'[^.]{0,40}sixteen[^.]{0,30}', l)[:1]) for i, l in enumerate(M, 1) if d5 <= i < e and 'sixteen' in l])
print('   *thirty-two* sites in the unit:', [i for i, l in enumerate(M, 1) if d5 <= i < e and 'thirty-two' in l], '; *seventy-seven*:', [i for i, l in enumerate(M, 1) if d5 <= i < e and 'seventy-seven' in l], '; *twenty-four*:', [i for i, l in enumerate(M, 1) if d5 <= i < e and 'twenty-four' in l])
for pat in [r'(?<![\d,])30,000(?![\d])', r'(?<![\d,])1,442(?![\d])', r'4ν/3', r'(?<![\d,])3,749(?![\d])', r'(?<![\d,])650(?![\d,])', r'200 of 200', r'104 of 106', r'12 of 12', r'E = 11', r'(?<![\d,])106(?![\d,])', r'nineteen', r'20 of 20', r'fifty-five thousand', r'three hundred and seventy', r'(?<![\d,])370(?![\d,])']:
    print('   %-26s unit %s ; main total %d ; MC %d' % (pat, [i for i, l in enumerate(M, 1) if d5 <= i < e and re.search(pat, l)], sum(1 for l in M if re.search(pat, l)), sum(1 for l in MC if re.search(pat, l))))

# §6 the Mathematical Compendium's own statements the unit restates: the Löwdin-work list of twelve; LS (eight) / 3B (nine); 3B.five / 3B.pot grade PROVED with the check noted
mch = [(i, l) for i, l in enumerate(MC, 1) if re.match(r'^#{1,3} ', l) and re.search(r'L[ÖO]WDIN', l, re.I)]
print('§6 MC headings naming Löwdin:', [(i, l[:70]) for i, l in mch][:6])
print('   MC `twelve` sites near those headings:', [(i, MC[i - 1][:110]) for i, l in enumerate(MC, 1) if re.search(r'\btwelve\b', l) and any(abs(i - j) < 400 for j, _ in mch)][:6])
print('   MC LS./3B. tagged headings:', Counter(re.match(r'^#{1,4}\s*(LS|3B)\.', l).group(1) for l in MC if re.match(r'^#{1,4}\s*(LS|3B)\.', l)), '; LS.* / 3B.* tokens (distinct):', sorted({m for l in MC for m in re.findall(r'\b(LS\.[a-z]+|3B\.[a-z]+)', l)}))
for tag in ('3B.five', '3B.pot', 'five fixed points', 'potential on shape space'):
    print('   MC %-24s sites %s ; grade lines: %s' % (tag, [i for i, l in enumerate(MC, 1) if tag in l][:6], [(i, re.findall(r'\b(PROVED|MEASURED|VERIFIED|CONJECTURED)\b', MC[k]) ) for i, l in enumerate(MC, 1) if tag in l for k in range(i - 1, min(i + 25, len(MC))) if re.search(r'\b(PROVED|MEASURED|VERIFIED|CONJECTURED)\b', MC[k])][:4]))
print('   MC L3245–L3275 grade words:', [(i, re.findall(r'\b(PROVED|MEASURED|VERIFIED|CONJECTURED)\b', MC[i - 1])) for i in range(3245, 3276) if re.search(r'\b(PROVED|MEASURED|VERIFIED|CONJECTURED)\b', MC[i - 1])], '; MC lines 3250 / 3268:', MC[3249][:120], '|', MC[3267][:120])
print('   PP twin of L10546 (§16.2 / §14.2):', [(i, l.strip()[:90]) for i, l in enumerate(PP, 1) if 'closure operator' in l and 10100 <= i <= 10437] if PP else 'no PP')
print('   Register 1734 body:', (rbody(1734) or '')[:300])
print('   Register 222 body:', (rbody(222) or '')[:260])
print('   Register 248 body (the 30,000-sample test):', (rbody(248) or '')[:260])

# §7 census rows in range (id, class, member, line, item, detail): member column value `main`
rows = [l.split('\t') for l in L.read_member('DEFECT-CENSUS.tsv').split('\n')[1:] if l.strip()]
inr = [r for r in rows if len(r) > 3 and r[2] == 'main' and r[3].isdigit() and d5 <= int(r[3]) < e]
print('§7 census rows in range:', len(inr)); [print('   ', '\t'.join(r)[:230]) for r in inr]
print('done')
