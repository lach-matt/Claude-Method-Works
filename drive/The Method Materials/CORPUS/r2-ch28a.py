# r2-ch28a.py — the unit main `## References` (LAST hit) to the end of the member: the COMPUTABLE / POINTER / REGISTER / YEAR claims (chat 141).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock). Every pointer resolved to the CLAIM
# under both resolvers; every cited Register entry located by `^#{1,4}\s*N\s*$`, its body (rbody) and WARNING read; every figure
# recomputed where the data is in the bundle; count words scored on raw lines AND the join; conventions named before scoring.
import os, re, importlib.util, itertools
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
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
def q1(x): return Decimal(x).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
def rhead(n): return [i + 1 for i, l in enumerate(R) if re.match(r'^#{1,4}\s*%d\s*$' % n, l)]
def rwarn(n):
    h = rhead(n)
    if not h: return None
    e = next((j for j in range(h[-1], len(R)) if re.match(r'^#{1,4}\s*\d+\s*$', R[j])), len(R))
    return [j + 1 for j in range(h[-1], e) if 'WARNING' in R[j]]

hr('§0 the unit by my own scan: `## References` LAST hit to the end of the member; the `### R.n` heading lines; entries per section under a NAMED convention')
rf = [i + 1 for i, l in enumerate(M) if re.match(r'^#{1,3} References\b', l)]; s = rf[-1]; U = M[s - 1:]; UJ = join(U)
print('  member %d lines; `References` heading hits %s; unit L%d–L%d = %d lines, %d non-blank' % (len(M), rf, s, len(M), len(U), len([l for l in U if l.strip()])))
hs = [(i + 1, M[i]) for i in range(s - 1, len(M)) if re.match(r'^#{1,4}\s', M[i])]; print('  headings: %s' % [(i, t[:34]) for i, t in hs])
rn = [(i, t) for i, t in hs if re.match(r'^### R\.\d', t)]
# Convention A (paragraph): an entry starts at a non-blank line after a blank line or after the heading, not itself a heading, and is not a
# 2-space continuation line. Convention B (separator): entries joined inline by ` · ` on one paragraph are counted by splitting on ` · `.
def entries(lo, hi):
    A = []; B = 0
    for j in range(lo, hi):
        l = M[j - 1]
        if not l.strip() or l.startswith('#'): continue
        if (j == lo + 1) or (not M[j - 2].strip()):
            if not re.match(r'^\s{2,}\S', l) or re.match(r'^ ?[·•]', l): A.append(j)
    for a in A:
        e = next((k for k in range(a + 1, hi + 1) if k > hi or not M[k - 2].strip()), hi + 1)
        B += 1 + len(re.findall(r' · ·? ?\*\*', ' '.join(M[a - 1:e - 1])))
    return A, B
for k, (i, t) in enumerate(rn):
    hi = rn[k + 1][0] - 1 if k + 1 < len(rn) else len(M)
    A, B = entries(i, hi); print('  %s L%d–L%d: paragraph entries %d (A) / with inline ` · **` splits %d (B)' % (t[4:8], i, hi, len(A), B))
pre = entries(s, rn[0][0] - 1); print('  preamble L%d–L%d (before R.1): paragraph entries %d; bold block heads at %s' % (s, rn[0][0] - 1, len(pre[0]), sites(M[s - 1:rn[0][0] - 1], r'^ \*\*[A-Z]')))
print('  L11726 "alone among the thirteen in this section" (R.5): see the R.5 line above under both conventions; PP R.5 count in r2-ch28b §0')

hr('§1 every § pointer in the unit resolved to the CLAIM under both resolvers (body_range | section_span), key tokens on the join; lettered pointers by exact-token scan')
PTR = [('12.11.4', ['LS', 'jK', 'jj', 'LK'], 'L11509 the four coupling types rebuilt'), ('24.9', ['provenance', 'per-species'], 'L11518 per-species notes'),
       ('14.1', ['Freuder', 'Dechter'], 'L11537 §14.1 had been crediting to Freuder'), ('14.5.9', ['tightness', 'twice', 'envelope'], 'L11545 constraint tightness as a COUNT'),
       ('8.6', ['dimension', 'width', 'Dilworth'], 'L11553 order dimension'), ('14.5.3', ['840', '750', 'projection'], 'L11563 840-cell witness E = 750'),
       ('29.12', ['U1', 'decomposab'], 'L11567 §29.12 U1'), ('18.4.1', ['realisation', 'mode'], 'L11595 two realisation modes'), ('22.1.1', ['singleton', 'muon'], 'L11599 singleton bracket'),
       ('12.11.0.1', ['clock', 'occupancy'], 'L11605 occupancy clock'), ('29.9', ['Racah', 'jK'], 'L11612'), ('12.11.1', ['seniority'], 'L11615'), ('22.9', ['seniority'], 'L11615'),
       ('16.4.1', ['Edl', 'footnote'], 'L11622 footnote 78 precedent'), ('29.5', ['Edl', 'Dunz', 'route'], 'L11624 / L11713'), ('23.1', ['central difference', 'second difference', 'Boole'], 'L11632'),
       ('23.8.1', ['Aitken', 'λ²'], 'L11634'), ('26.6', ['Richardson'], 'L11638'), ('23.8.4', ['Moore', 'cost of rigour'], 'L11642'), ('23.8.2', ['Newton decrement', 'self-concordan', 'λ²'], 'L11654'),
       ('12.9', ['maximal chain', 'Birkhoff'], 'L11658'), ('30.3', ['3/4', 'three quarters', 'three-quarters', 'Rival', 'subcube', 'residue', 'obstruction', 'arity', 'reorderab', 'Stahl', 'subdirect', 'tight'], 'L11661–L11775 (R.5 §30.3 claims)'),
       ('15', ['φ_ij', 'φ'], 'L11670 recovered bound of Chapter 15'), ('18.4.2', ['dominance', 'Brylawski', 'partition'], 'L11696'), ('29.11', ['Baker', 'Pixley', 'Bergman', 'majority', 'median'], 'L11702 / L11706'),
       ('14.5.7', ['seed', 'NP'], 'L11759'), ('2.24', ['heuristic', 'spread'], 'L11759'), ('14.5.1', ['eleven', 'irredundant', 'generating'], 'L11767'), ('14.5', ['Moore famil', 'closure system', 'cryptomorph'], 'L11751 / L11754'),
       ('2.23', ['requirement', 'named'], 'L11726'), ('31.1', ['Poincar', 'non-integrab', 'touch'], 'L11783'), ('31.1.1', ['bracket', 'Lagrange', 'equilibrium'], 'L11788'), ('23.14.1', ['Hill', 'capacity'], 'L11790'),
       ('31.3.1', ['Batyrev', '248,305', '495,515', 'mirror'], 'L11795 / L11802'), ('32.2', ['unread', 'open', 'Kreuzer', '30,108'], 'L11555 / L11799'), ('29', ['searched', 'not found'], 'L11844'),
       ('7', ['exclusion', 'quantum number'], 'L11842 Chapter 7'), ('8.4', ['antichain', 'Sperner', 'largest level'], 'L11723'), ('12.11', ['jK'], 'L11611'), ('14.6', ['#P'], 'L11763 (24b-06 corrected sites)'), ('28.10', ['#P'], 'L11763')]
for sec, keys, why in PTR:
    if heading_line(M, sec) is None:
        print('  §%-9s %-42s NO HEADING in the volume (exact-token scan); `§%s` sites in main: %s' % (sec, why[:42], sec, sites(M, '§' + re.escape(sec) + r'(?!\d)(?!\.\d)')[:8])); continue
    br, sp = body_range(M, sec), section_span(M, sec); jb, js = join(M[br[0] - 1:br[1] - 1]), join(M[sp[0] - 1:sp[1] - 1])
    print('  §%-9s %-42s body_range %-14s section_span %-14s %s | %s' % (sec, why[:42], br, sp, {k: (k in jb) if not k.isalpha() else has_token(jb, k) for k in keys}, {k: (k in js) if not k.isalpha() else has_token(js, k) for k in keys}))
for sec in ('12.11.4', '32.2', '14.5.3'):
    br = body_range(M, sec); print('  §%s printed (short section, body_range L%d–L%d):' % (sec, br[0], br[1] - 1)); [print('    L%d %s' % (j, M[j - 1][:230])) for j in range(br[0], br[1]) if M[j - 1].strip()]
print('  homes located by grep: `840-cell`/`840 cells` main %s; `E(ℛ) = 750`/`750` main %s; `tightness` main %s (L11545 says since §14.5.9); `Richardson` main %s (L11638 says §26.6); `Q item` main sites %s; `item R` main %s' % (sites(M, r'840[- ]cell')[:6], sites(M, r'(?<![\d,.])750(?![\d,])')[:8], sites(M, r'\btightness\b')[:8], sites(M, r'Richardson')[:8], sites(M, r'Q item')[:8], sites(M, r'\bitem R\b')[:6]))
aa = lettered(M, 'A'); print('  Appendix A heading hits %s; `A.2` item sites in main (grep by hand, docket rule) %s' % ([i for i in aa][:4], [(i, M[i - 1].strip()[:50]) for i in sites(M, r'(?<![A-Za-z0-9§])A\.2(?![\d.])')][:6]))
for tag, keys, why in (('E.3', ['chain decomposition', 'J(Λ)', 'Birkhoff'], 'L11658'), ('E.6', ['Adams', 'Dwinger', 'Schmid', 'maximal sublattice'], 'L11686'), ('A.9', ['Möbius', 'crosscut', 'Boolean'], 'L11665'),
                      ('A.2', ['Baker', 'Pixley', 'binary projection', 'majority'], 'L11701'), ('E.1.5', ['#P'], 'L11763'), ('R.7', [], 'L11853 §R.7')):
    h = lettered(M, tag); print('  %-6s hits %s (body = LAST) %s' % (tag, h, ({k: (k in join(M[h[-1] - 1:h[-1] + 80])) for k in keys} if h else 'NO HEADING')))
print('  `P20` sites in main (L11786 "P20\'s bound"): %s' % [(i, M[i - 1].strip()[:60]) for i in sites(M, r'(?<![A-Za-z0-9])P20(?![0-9])')][:6])
print('  `§R\\.` form sites in main (a lettered pointer written with §): %s' % sites(M, r'§R\.\d'))
print('  `Q item [A-Z]` letters in the unit %s; in §32.2 (section_span) %s' % (sorted(set(re.findall(r'Q item ([A-Z])', UJ))), sorted(set(re.findall(r'item ([A-Z])\b', join(M[section_span(M, '32.2')[0] - 1:section_span(M, '32.2')[1] - 1]))))))

hr('§2 every Register entry the unit cites: heading located by `^#{1,4}\\s*N\\s*$`, body (first non-blank line), WARNING lines in the entry')
cited = sorted({int(x) for x in re.findall(r'[Rr]egisters? (\d{3,4})', UJ)} | {int(x) for a, b in re.findall(r'[Rr]egisters (\d{3,4})[–-](\d{3,4})', UJ) for x in range(int(a), int(b) + 1)} | {int(x) for x in re.findall(r'[Rr]egisters \d{3,4} and (\d{3,4})', UJ)})
print('  cited numbers (%d): %s' % (len(cited), cited))
for n in cited:
    h = rhead(n); w = rwarn(n); b = rbody(n)
    print('  %4d heading %-9s WARNING %-10s body: %s' % (n, ('L%d' % h[-1]) if h else 'ABSENT', ('L%s' % w) if w else ('none' if h else '—'), (b or '')[:95]))
print('  `Register 344` / `344` sites in the six volumes: main %s reg %s mc %s' % (sites(M, r'(?<!\d)344(?!\d)')[:6], sites(R, r'(?<!\d)344(?!\d)')[:6], sites(MC, r'(?<!\d)344(?!\d)')[:6]))

hr('§3 computable figures: recomputed where the data is in the bundle; otherwise located at their source (a location is not a re-derivation)')
print('  L11607 "739 of 1,089 joined pairs" with "33 objects": 33² = %d (ordered pairs incl. diagonal); C(33,2) = %d; 739/1089 = %s %%' % (33 ** 2, 33 * 32 // 2, q1(Decimal(739) / Decimal(1089) * 100)))
try:
    T = L.load_tower(); L9 = T.L9(); n9 = len(L9)
except Exception as e:
    n9 = None; print('  tower: %s' % e)
print('  L11608 "904 conservative cells at 54.7%%" and "675,606 of 2,735,716 cell pairs": Λ₉ = %s cells; 1654² = %d (ORDERED pairs with diagonal — the printed denominator); C(1654,2) = %d; 904/1654 = %s %% (ROUND_HALF_UP, 1 dp)' % (n9, 1654 ** 2, 1654 * 1653 // 2, q1(Decimal(904) / Decimal(1654) * 100)))
for fig in ('739', '1,089', '389', '904', '54.7', '675,606', '2,735,716', '33 objects', '8/15/10', '25,000', '43 sections'):
    print('    %-10s main sites %s; Register entries %s' % (fig, sites(M, re.escape(fig) + r'(?!\d)')[:8], sorted({int(re.sub(r'\D', '', R[max(k for k in range(i) if re.match(r'^#{1,4}\s*\d+\s*$', R[k]))])) for i in sites(R, re.escape(fig) + r'(?!\d)')})[:10]))
print('  L11600–L11602 muon figures at Register 319 / §22.1.1 (record-carried; the paper is not a member):')
for fig in ('119', '918', '2.6 × 10', '0.203', '0.262', '0.292', '11.2 m', '623 m', '7.29'):
    sp = section_span(M, '22.1.1'); print('    %-10s §22.1.1 span %d; main sites %s; Register 319 %d' % (fig, len(re.findall(re.escape(fig), join(M[sp[0] - 1:sp[1] - 1]))), sites(M, re.escape(fig))[:5], len(re.findall(re.escape(fig), ' '.join(R[rhead(319)[-1] - 1:rhead(319)[-1] + 40]))) if rhead(319) else -1))
print('  L11563 "§14.5.3 gives an 840-cell witness … E(ℛ) = 750": `840` / `750` in §14.5.3 span: %s' % {k: cnt(M[section_span(M, '14.5.3')[0] - 1:section_span(M, '14.5.3')[1] - 1], r'(?<![\d,])' + k + r'(?![\d,])', 0) for k in ('840', '750')})
print('  L11755 Moore families 1, 2, 7, 61, 2 480, 1 385 552, 75 973 751 474 (n = 0…6): brute force for n ≤ 4 (families of subsets of [n] containing [n] and closed under ∩):')
for n in range(0, 5):
    subs = list(range(1 << n)); full = (1 << n) - 1; c = 0
    for mask in range(1 << (1 << n)):
        if not (mask >> full) & 1: continue
        fam = [x for x in subs if (mask >> x) & 1]; ok = True
        for a in fam:
            for b in fam:
                if not (mask >> (a & b)) & 1: ok = False; break
            if not ok: break
        c += ok
    print('    n = %d: %d' % (n, c))
print('  L11798 / L11801 Hodge figures at their main sites: %s' % {k: sites(M, re.escape(k))[:5] for k in ('473,800,776', '30,108', '248,305', '495,515')})
print('  L11846 R = 109,737.31568 cm⁻¹: sites of `109,737.31568` main %s; other printed forms `109737.3` / `109,737.3` main %s %s; MC %s; PC %s' % (sites(M, r'109,737\.31568'), sites(M, r'109737\.3'), [i for i in sites(M, r'109,737\.3') if i not in sites(M, r'109,737\.31568')][:8], sites(MC, r'109,?737\.3')[:5], sites(PC, r'109,?737\.3')[:5]))
print('  L11767 "§14.5.1\'s eleven-cell generating set": `eleven` in §14.5.1 span %d; `11 cells` / `eleven cells` main sites %s' % (cnt(M[section_span(M, '14.5.1')[0] - 1:section_span(M, '14.5.1')[1] - 1], r'\beleven\b'), sites(M, r'\b(eleven|11)[- ]cell')[:8]))

hr('§4 the MC bibliography against L11848–L11853: "162 works, 1669 to 2026"; "Fifty-nine of them are the works listed above" (surname ∩ year convention, NAMED)')
bh = [i + 1 for i, l in enumerate(MC) if re.match(r'^#{1,3}\s.*(Bibliograph|References|Works cited)', l, re.I)]; print('  MC bibliography heading hits: %s' % [(i, MC[i - 1][:60]) for i in bh])
if bh:
    b0 = bh[-1]; b1 = next((j + 1 for j in range(b0, len(MC)) if re.match(r'^#{1,2}\s', MC[j])), len(MC) + 1); B = MC[b0 - 1:b1 - 1]
    pipe = [l for l in B if l.lstrip().startswith('|') and not l.startswith('    ')]; print('  `|` lines %d; first three: %s' % (len(pipe), [l[:110] for l in pipe[:3]]))
    cells = [[c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]] for l in pipe]
    rows = [l for l, c in zip(pipe, cells) if c and not re.match(r'^:?-+:?$', c[0]) and not re.match(r'^(Year|year|#|No\.?)$', c[0]) and re.search(r'\b(1[6-9]\d\d|20[0-2]\d)\b', l)]
    print('  DATA rows (split on unescaped `|`, header and separator excluded, carrying a year): %d' % len(rows))
    yrs = [int(y) for l in rows for y in re.findall(r'\b(1[6-9]\d\d|20[0-2]\d)\b', l)[:1]]
    print('  MC bibliography L%d–L%d: %d work rows; years %s–%s' % (b0, b1 - 1, len(rows), min(yrs) if yrs else None, max(yrs) if yrs else None))
    def surnames(lines):   # a surname is a capitalised token followed by an initial, a year bracket, `&`, `and`, `,` or `–`; markup stripped
        s = set()
        for l in lines:
            for m in re.finditer(r"(?<![A-Za-z'’\-])([A-Z][a-zäöüéèçøÅ'’\-]{2,})(?=\s*(?:,\s*[A-Z]\.|\(|&|and\b|,|–|—|\s+\d{4}))", re.sub(r'[*_`]', '', l)): s.add(m.group(1))
        return s
    mcs = surnames(rows); us = surnames([l for l in U if not l.startswith('#')])
    both = sorted(mcs & us); print('  surnames MC rows %d, unit %d, shared %d: %s' % (len(mcs), len(us), len(both), both))
    print('  MC rows whose surname is in the unit: %d of %d (the printed fifty-nine counts WORKS; this is a surname-overlap bound, stated as such)' % (sum(1 for l in rows if surnames([l]) & us), len(rows)))
    for nm in ('Newton', 'Leibniz', 'Euler', 'Gauss', 'Moore', 'Birkhoff'):
        print('    %-9s MC rows %d (years %s)' % (nm, sum(1 for l in rows if re.search(r'\b' + nm + r'\b', l)), sorted({int(y) for l in rows if re.search(r'\b' + nm + r'\b', l) for y in re.findall(r'\b(1[6-9]\d\d|20[0-2]\d)\b', l)[:1]})))
print('  Register 1736 body: %s' % (rbody(1736) or '')[:300])

hr('§5 years against the Register\'s dating (docket 16) and against the unit itself')
for nm in ('Edlén', 'Janet', 'Montgomery', 'Kimura', 'Siggers', 'Ritz', 'Rydberg', 'Seki', 'Hill', 'Poincar'):
    yu = sorted({y for l in U for y in re.findall(r'\b(1[6-9]\d\d|20[0-2]\d)\b', l) if nm in l})
    yr = Counter(y for l in R if nm in l for y in re.findall(nm + r'[^.]{0,40}?\b(1[6-9]\d\d|20[0-2]\d)\b', l))
    ym = Counter(y for i, l in enumerate(M, 1) if nm in l and i < s for y in re.findall(nm + r'[^.]{0,40}?\b(1[6-9]\d\d|20[0-2]\d)\b', l))
    print('  %-10s unit years %s; main (outside unit) name+year %s; Register name+year %s' % (nm, yu, dict(ym), dict(yr)))
print('  L11820 Montgomery "(2014) … Amer. Math. Monthly 122 (2015)": two years on one line — %s' % [l.strip()[:80] for l in U if 'Amer. Math. Monthly' in l])
print('  L11621 Edlén (1960) Handbuch der Physik 27 and L11624 Edlén (1964) Encyclopedia of Physics: `Handbuch` sites main %s; `Encyclopedia of Physics` main %s; Register lines naming both years with Edlén %s' % (sites(M, r'Handbuch'), sites(M, r'Encyclopedia of Physics'), [i for i in sites(R, r'Edlén') if '1960' in R[i - 1] and '1964' in R[i - 1]][:5]))

hr('§6 count words on raw lines AND the join; the [unread] / [F] / [S] marks against §32.2')
for w in ('thirteen', 'Fifty-nine', '162 works', '1669 to 2026', '25,000 words', '43 sections', 'four cycles', 'eleven-cell', 'four types', 'three-way', 'five equilibrium', 'five fixed points', 'five cells', 'two blocks', 'the three defects'):
    print('  %-18s raw %d  join %d' % (w, cnt(U, re.escape(w)), len(re.findall(re.escape(w), UJ, re.I))))
ur = [(s + i, U[i][:50]) for i in range(len(U)) if re.search(r'\[unread\]|\bunread\b', U[i])]; print('  [unread]/unread lines %d: %s' % (len(ur), ur))
print('  [F] %d, [S] %d lines; definitions of the marks in the unit: %s' % (cnt(U, r'\[F\]', 0), cnt(U, r'\[S\]', 0), [(s + i, U[i][:70]) for i in range(len(U)) if re.search(r'marked \[|\[F\] |\[S\] ', U[i]) and 'mean' in U[i].lower()] or 'none (marks used, not defined)'))
s322 = section_span(M, '32.2'); j322 = join(M[s322[0] - 1:s322[1] - 1])
for nm in ('Paschen', 'Götze', 'Runge', 'Adams', 'Ryter', 'Schmid', 'Sharp', 'Stephen', 'Dunz', 'Kreuzer', 'Skarke'):
    print('    %-8s in §32.2 %s (span %s); unit lines %s' % (nm, has_token(j322, nm), s322, sites(U, r'\b' + nm + r'\b')[:3]))

hr('§7 census rows in the unit\'s range and the docket-27 paragraph test')
C = L.read_member('DEFECT-CENSUS.tsv').split('\n'); hd = C[0].split('\t'); print('  census columns: %s' % hd)
rows = [l.split('\t') for l in C[1:] if l.strip()]
ci = {k: hd.index(k) for k in hd}
inr = [r for r in rows if len(r) == len(hd) and r[ci.get('member', 0)] in ('main', 'all') and re.match(r'^\d+$', r[ci.get('line', 0)] if 'line' in ci else '') and s <= int(r[ci['line']]) <= len(M)] if 'line' in ci else []
print('  rows with member main/all and line in L%d–L%d: %d %s' % (s, len(M), len(inr), [r for r in inr][:12]))
print('  L11600 printed: %s' % M[11599].strip()[:160])
out = {l.strip() for i, l in enumerate(M, 1) if i < s and len(l.strip()) >= 40}
dup = [(s + i, l.strip()[:70]) for i, l in enumerate(U) if len(l.strip()) >= 40 and l.strip() in out]
print('  docket 27: unit lines ≥ 40 chars %d; duplicated outside the unit %d %s' % (len([l for l in U if len(l.strip()) >= 40]), len(dup), dup[:6]))
