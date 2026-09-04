#!/usr/bin/env python3
# r2-23a2.py — R3 (chat 153-R) — SUCCESSOR to r2-23a.py after §D.2 gained its sixth status value at BUILD95
# (register 1801, "unwitnessed", between verified and proved) and §D.5.10 printed it of a fibre at BUILD98
# (register 1806). r2-23a hard-coded the five-value status list and raises ValueError on the sixth. The successor
# reads the status order from §D.2's own declaration — the line it already parses and prints — so the list is
# DATA; verification and precedent orders are read the same way. Identical measurements otherwise. Provable by
# proveanchor on the pre-BUILD95 bundles only where the declaration then read the five; on BUILD98 and later the
# predecessor cannot run at all, so this successor's golden is banked by running.
# r2-23a is seated and never edited in place (chat 68); it is superseded, not withdrawn.
# r2-23a.py — chat 146 (Cowork) — 23a-03 (DEF-143 item 11's second re-derivation; DEF-136 item 6; docket 37 / 38):
# Appendix D.5.9's first-run E = 4 (three cells in formula · analysis, one in theorem · analysis), second-run E = 2 (the two
# named formula · analysis cells) and third-run E = 0; D.5.5's fibration table (kind × language 0 / kind only 2 / language
# only 3 / none 4) with Register 233's *2 by kind*; the narrated first runs of D.5.6, D.5.8 and D.5.10; every fibre count
# and total the D.5 chain prints. The index is rebuilt from the volume's own tables (D.5.2, D.5.4's prose, D.5.6–D.5.10) and
# closed under the book's OWN operator — r2lib.Rset, §6.1 L1540: φ̂ᵢⱼ(v) = max{xᵢ : xⱼ ≤ v} (a running maximum), ambient
# ∏ Âᵢ(X) — imported by path, never copied. Rival conventions are named and scored beside it: chat 136's equality bound
# (φ(v) = max{xᵢ : xⱼ = v}, the reconstruction r2-ch23a.py §4 used), the interval hull, and D.3's two constraints applied
# to the ambient. Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness. A re-derivation
# that disagrees with the record is a finding about the re-derivation (G0c); the record stands until the original instrument
# (the appendix's own, not a member — docket 38) is found. Every convention is named before a figure is scored.
import os, re, sys, hashlib, importlib.util, itertools
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'; PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
IOI = 'The_Method_1_6___The_Index_of_Indices-2.md'; SC = 'The_Method_1_6___Spectra_Compendium-2.md'
VOLS = {'main': MAIN, 'reg': REG, 'mc': MC, 'pc': PC, 'ioi': IOI, 'sc': SC}
M = rd(MAIN); R = rd(REG); TXT = {k: rd(v) for k, v in VOLS.items()}
def hr(t): print('\n' + '=' * 100 + '\n' + t + '\n' + '=' * 100)

def rbody(n):   # copied verbatim from r2-21a.py (there from r2-scf.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-21a.py (there from r2-scf.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-21a.py (there from r2-scf.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

def bounded(f): return re.compile(r'(?<![\d.,])' + re.escape(f) + r'(?![\d])')   # chat-145 convention: digit-bounded on both sides
def sites(f, vol='main'): return [i for i, l in enumerate(TXT[vol], 1) if bounded(f).search(l)]

hr('§0 members and the unit (lettered headings; body = LAST hit; a `### D.x` unit ends at the next heading of any rank)')
for k, v in VOLS.items(): print('   %-4s %-52s md5 %s  %d lines' % (k, v, md5(v), len(TXT[k])))
def drange(tag):
    h = lettered(M, tag); s = h[-1]
    e = next(i for i in range(s + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1]))
    return (s, e)
UNITS = {t: drange(t) for t in ('D.2', 'D.3', 'D.5', 'D.5.2', 'D.5.4', 'D.5.5', 'D.5.6', 'D.5.7', 'D.5.8', 'D.5.9', 'D.5.10')}
for t, (s, e) in UNITS.items(): print('   %-6s hits %s  body L%d–L%d (%d lines)  %s' % (t, lettered(M, t), s, e - 1, e - s, M[s - 1].strip()[:70]))
appD = lettered(M, 'Appendix D'); print('   `## Appendix D` hits', appD, '(the contents line and the body; body = LAST) ; `## Appendix E` hits', lettered(M, 'Appendix E'))
print('   heading_line (numeric-only resolver) on "D.5.9":', r2lib.heading_line(M, 'D.5.9'), '— the numeric resolver does not see a lettered heading; `lettered` governs (chat-129 convention)')

hr('§1 the Register: the entries the unit cites, their headings, WARNING lines; the family figures grepped in six volumes')
def ent(n):
    i = next((i for i, l in enumerate(R, 1) if l.strip() == '### %d' % n), None)
    if i is None: return (n, None, None, None)
    e = next((j for j in range(i + 1, len(R) + 1) if re.match(r'^#{1,4} ', R[j - 1])), len(R) + 1)
    warn = [j for j in range(i, e) if 'WARNING' in R[j - 1]]
    return (n, i, e - 1, warn)
for n in (222, 230, 232, 233, 248, 282, 305, 361, 1718, 1726, 1734):
    q, i, e, w = ent(n); print('   %5d heading L%s body L%s–L%s WARNING lines %s :: %s' % (n, i, i, e, w, (rbody(n) or '')[:150]))
regnums = [int(m.group(1)) for l in M[UNITS['D.5.9'][0] - 1:UNITS['D.5.9'][1] - 1] for m in re.finditer(r'[Rr]egisters?\s+(\d+)', l)]
print('   register pointers inside D.5.9:', regnums)
for tok in ('E = 4', 'E = 2', 'sixty-five', 'twenty-two fibres', '3B.five', '3B.pot', '650', 'formula · analysis'):
    hits = {k: [i for i, l in enumerate(TXT[k], 1) if tok in l] for k in VOLS}
    print('   %-20s' % repr(tok), {k: (len(v), v[:6]) for k, v in hits.items() if v})
print('   Register lines naming *D.5.9*:', [i for i, l in enumerate(R, 1) if 'D.5.9' in l], '; lines with "E = 4":', [i for i, l in enumerate(R, 1) if bounded('4').search(l) and 'E = 4' in l])

hr('§2 census: every numeral printed in D.5.5 (fibration table) and D.5.9 (member line numbers)')
NUM = re.compile(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])')
for t in ('D.5.5', 'D.5.9'):
    s, e = UNITS[t]; cnt = 0; lines = 0
    for i in range(s, e):
        ns = NUM.findall(M[i - 1])
        if ns: cnt += len(ns); lines += 1; print('   L%d %s' % (i, ' '.join(ns)))
    print('   %s: %d numerals on %d lines' % (t, cnt, lines))

hr('§3 the index rebuilt from the volume\'s own tables (D.2 coordinates L%d–; D.5.2; D.5.4 prose; D.5.6–D.5.10 tables)' % UNITS['D.2'][0])
d2_pre = M[UNITS['D.2'][0]:UNITS['D.2'][1] - 1]
def declared(coord):
    l = [x for x in d2_pre if re.match(r'^\s{2}%s\b' % coord, x)][0]
    return [t.strip() for t in re.search(r'^\s{2}%s\s+(.+?)\s{2,}' % coord, l).group(1).split(' < ')]
ST, VE, PR = declared('status'), declared('verification'), declared('precedent')
print('   §D.2 declares status %s | verification %s | precedent %s (read as DATA; r2-23a hard-coded five status values)' % (ST, VE, PR))
KINDS = 'definition|mechanism|formula|theorem|law|method|measurement'; LANGS = 'order|combinatorics|analysis|complexity|physics|algebraic geometry'
d2 = M[UNITS['D.2'][0]:UNITS['D.2'][1] - 1]
print('   D.2 rows:', [l.split()[0] for l in d2 if re.match(r'^\s{2}\w', l)], '; status order read:', re.search(r'status\s+(.+?)\s{2,}', [l for l in d2 if 'status' in l][0]).group(1))
def coords(s):
    s = s.replace('**', '').strip(); a, b, c = [x.strip() for x in s.split(' · ')][:3]; c = c.split(' (')[0]
    return (ST.index(a), VE.index(b), PR.index(c))
ROW52 = re.compile(r'^\s*(' + KINDS + r') · (' + LANGS + r')\s{2,}(.+?)\s{2,}(\S.*? · .*? · .*?)\s*$')
ROWN = re.compile(r'^\s*(.+?)\s{2,}(' + KINDS + r') · (' + LANGS + r')\s{2,}(.+?)\s*$')
elems = []   # (stage, name, kind, language, (status, verification, precedent), line)
s, e = UNITS['D.5.2']
for i in range(s + 1, e):
    m = ROW52.match(M[i - 1])
    if m: elems.append(('D.5.2', m.group(3).strip(), m.group(1), m.group(2), coords(m.group(4)), i))
print('   D.5.2 DATA rows parsed:', len(elems), '(printed twenty-seven); first/last:', elems[0][1], '/', elems[-1][1])
# D.5.4's five (hand-entered from the prose of D.5.4, L10634–L10645 at chat 136; re-taken here by grep): all theorem · order;
# A.5 proved · sampled as printed at L10644 (23a-01: Register 222 says *now exhaustive*)
s4, e4 = UNITS['D.5.4']
a5 = [i for i in range(s4, e4) if 'proved · sampled, not proved · exhaustive' in M[i - 1]]
print('   D.5.4 line *proved · sampled, not proved · exhaustive* (A.5, the paragraph opens at L%d):' % (a5[0] - 1 if a5 else -1), a5, '::', (M[a5[0] - 1].strip()[:140] if a5 else None))
five = [('A.4 ⅅ ≥ dim q − dim p', (4, 2, 0)), ('A.5 χ_Λ is total', (4, 1, 0)), ('A.11 ν is inadmissible as an axis', (4, 2, 0)), ('Theorem 18.1 definability', (4, 2, 0)), ('Theorem 18.2 σ-algebra of predicates', (4, 2, 0))]
for nm, co in five: elems.append(('D.5.4', nm, 'theorem', 'order', co, a5[0] if nm.startswith('A.5') else s4))
for sec in ('D.5.6', 'D.5.7', 'D.5.8', 'D.5.9', 'D.5.10'):
    lo, hi = UNITS[sec]; k = 0
    for i in range(lo + 1, hi):
        m = ROWN.match(M[i - 1])
        if m and m.group(1).strip() not in ('new element', 'element'):
            elems.append((sec, m.group(1).strip(), m.group(2), m.group(3), coords(m.group(4)), i)); k += 1
    print('   %-6s DATA rows %d' % (sec, k), '(printed %s)' % {'D.5.6': 'four', 'D.5.7': 'four', 'D.5.8': 'eight', 'D.5.9': 'seventeen', 'D.5.10': 'twelve'}[sec])
stages = ['D.5.2', 'D.5.4', 'D.5.6', 'D.5.7', 'D.5.8', 'D.5.9', 'D.5.10']
cum = {s: [x for x in elems if stages.index(x[0]) <= stages.index(s)] for s in stages}
print('   running totals:', {s: len(cum[s]) for s in stages}, '(printed 27 / 32 / 36 / 40 / 48 / 65 / 77) ; fibres:', {s: len({(x[2], x[3]) for x in cum[s]}) for s in stages}, '(printed 16 / 16 / 16 / 16 / 16 / 22 / 24)')
d59 = [x for x in elems if x[0] == 'D.5.9']
print('   D.5.9 rows: LS', sum(1 for x in d59 if x[1].startswith('LS.')), '3B', sum(1 for x in d59 if x[1].startswith('3B.')), '; fibres new at D.5.9:', sorted(set((x[2], x[3]) for x in cum['D.5.9']) - set((x[2], x[3]) for x in cum['D.5.8'])), '(printed six: mechanism · physics, law · physics, theorem · physics, definition · analysis, theorem · algebraic geometry, theorem · complexity)')
for nm in ('3B.five', '3B.pot'):
    x = next(x for x in d59 if x[1].startswith(nm)); print('   %s as printed: %s · %s :: %s · %s · %s  (L%d)' % (nm, x[2], x[3], ST[x[4][0]], VE[x[4][1]], PR[x[4][2]], x[5]))
# the D.5 fibre table (printed counts) against the rebuilt seventy-seven
tab = {}
for i in range(UNITS['D.5'][0], UNITS['D.5'][1]):
    m = re.match(r'^\s{2}(' + KINDS + r')((?: · (?:' + LANGS + r'))+)\s{2,}(\d+|1 each)\s{2,}(\d)\s*$', M[i - 1])
    if m:
        for lg in m.group(2).split(' · ')[1:]: tab[(m.group(1), lg)] = (1 if m.group(3) == '1 each' else int(m.group(3)), int(m.group(4)))
reb = Counter((x[2], x[3]) for x in elems)
print('   D.5 table rows', len(tab), 'cells sum', sum(v[0] for v in tab.values()), 'E column sum', sum(v[1] for v in tab.values()), '; rebuilt == table:', {k: v[0] for k, v in tab.items()} == dict(reb), '; differences:', {k: (reb.get(k), tab.get(k, (None,))[0]) for k in set(reb) | set(tab) if reb.get(k) != tab.get(k, (None,))[0]})

hr('§4 conventions named before scoring. E(X) = |ℛ(X)| − |X| per fibre, summed (§6.1, D.1).')
print('''   BOOK  — r2lib.Rset (§6.1 L1540, lifted verbatim at chat 74): φ̂ᵢⱼ(v) = max{xᵢ : x ∈ X, xⱼ ≤ v} (running maximum), ambient ∏ Âᵢ(X).
   EQ    — chat 136's reconstruction (r2-ch23a.py §4): φ(v) = max{xᵢ : xⱼ = v} (equality, no running maximum), ambient ∏ Âᵢ(X).
   HULL  — as BOOK but the ambient is the interval hull [min, max] of each coordinate.
   +D3   — cells violating D.3's two constraints (verification = cited ⟹ precedent = found; status ≥ measured ⟹ verification ≥ sampled) removed from ℛ(X) before counting.
   Coordinates ordered as D.2 prints them: status withdrawn < conjectured < measured < verified < proved; verification cited < sampled < exhaustive; precedent none found < found.''')
def E_eq(X):
    X = sorted(set(X)); phi = {}
    for i in range(3):
        for j in range(3):
            if i != j: phi[(i, j)] = {v: max(x[i] for x in X if x[j] == v) for v in {x[j] for x in X}}
    box = itertools.product(*[sorted({x[i] for x in X}) for i in range(3)])
    return {x for x in box if all(x[i] <= phi[(i, j)][x[j]] for i in range(3) for j in range(3) if i != j)}
def E_hull(X):
    X = sorted(set(X)); phi = {}
    for i in range(3):
        for j in range(3):
            if i != j: phi[(i, j)] = lambda v, i=i, j=j: max([x[i] for x in X if x[j] <= v] or [-1])
    box = itertools.product(*[range(min(x[i] for x in X), max(x[i] for x in X) + 1) for i in range(3)])
    return {x for x in box if all(x[i] <= phi[(i, j)](x[j]) for i in range(3) for j in range(3) if i != j)}
d3ok = lambda x: (x[1] != 0 or x[2] == 1) and (x[0] < 2 or x[1] >= 1)
CONV = {'BOOK': lambda X: r2lib.Rset(X), 'EQ': E_eq, 'HULL': E_hull}
def closure(X, conv, d3):
    cl = CONV[conv](X)
    return {x for x in cl if d3ok(x)} if d3 else cl
def fibreE(els, fib=lambda x: (x[2], x[3]), conv='BOOK', d3=False):
    g = defaultdict(list); [g[fib(x)].append(x[4]) for x in els]
    return {k: (len(closure(v, conv, d3)) - len(set(v)), sorted(closure(v, conv, d3) - set(v))) for k, v in g.items()}
def E(els, **kw): return sum(v[0] for v in fibreE(els, **kw).values())
def named(c): return '%s · %s · %s' % (ST[c[0]], VE[c[1]], PR[c[2]])
def report(tag, els, **kw):
    fe = fibreE(els, **kw); print('   %-78s elements %2d fibres %2d E = %d %s' % (tag, len(els), len(fe), sum(v[0] for v in fe.values()), {' · '.join(k): [named(c) for c in v[1]] for k, v in fe.items() if v[0]}))
def swap(els, name, co): return [(x[0], x[1], x[2], x[3], co, x[5]) if x[1].startswith(name) else x for x in els]
A5X = lambda els: [x if not x[1].startswith('A.5') else (x[0], x[1], x[2], x[3], (4, 2, 0), x[5]) for x in els]   # A.5 exhaustive (Register 222)
ALL = [(c, d) for c in ('BOOK', 'EQ', 'HULL') for d in (False, True)]
def lab(c, d): return c + ('+D3' if d else '')

hr('§5 D.5.5\'s fibration table on the thirty-two (printed: kind × language 16 fibres E 0 · kind only 7 / 2 · language only 6 / 3 · none 1 / 4; Register 233 *4 in one fibre, 3 by language, 2 by kind, 0 by kind × language*)')
FIB = {'kind × language': lambda x: (x[2], x[3]), 'kind only': lambda x: x[2], 'language only': lambda x: x[3], 'none': lambda x: 0}
for a5, tag in ((cum['D.5.4'], 'A.5 sampled (as printed L10644)'), (A5X(cum['D.5.4']), 'A.5 exhaustive (Register 222)')):
    for c, d in ALL:
        print('   %-32s %-9s' % (tag, lab(c, d)), {f: (len({FIB[f](x) for x in a5}), E(a5, fib=FIB[f], conv=c, d3=d)) for f in FIB})
X = cum['D.5.4']
print('   kind-only excess by kind under BOOK, A.5 sampled:', {k: [named(c) for c in v[1]] for k, v in fibreE(X, fib=lambda x: x[2]).items() if v[0]}, '; A.5 exhaustive:', {k: [named(c) for c in v[1]] for k, v in fibreE(A5X(X), fib=lambda x: x[2]).items() if v[0]})
print('   theorem cells of the thirty-two (A.5 sampled):', sorted(Counter(named(x[4]) for x in X if x[2] == 'theorem').items()))

hr('§6 the stage closures and the narrated first runs, under every convention (E = 0 printed at every stage as closed)')
for c, d in ALL:
    print('   ' + lab(c, d) + ', A.5 exhaustive:', {s: E(A5X(cum[s]), conv=c, d3=d) for s in stages}, '; A.5 sampled:', {s: E(cum[s], conv=c, d3=d) for s in stages})
print('   narrated: D.5.6 first run E = 1 (ℛ-as-closure-operator proved · sampled · found, Register 282); D.5.8 first run E = 1 at proved · sampled · none found (separation hypothesis entered exhaustive); D.5.10 first run E = 1 in theorem · analysis at verified · exhaustive · none found (corridor entered with precedent found)')
for c, d in ALL:
    print('   ' + lab(c, d) + ':')
    report('D.5.6 first run, ℛ closure operator → proved · sampled · found', swap(A5X(cum['D.5.6']), 'ℛ is a closure operator', (4, 1, 1)), conv=c, d3=d)
    report('D.5.8 first run, separation hypothesis → proved · exhaustive · none found', swap(A5X(cum['D.5.8']), 'the separation hypothesis', (4, 2, 0)), conv=c, d3=d)
    report('D.5.10 first run, corridor → verified · exhaustive · found', swap(A5X(cum['D.5.10']), 'the corridor', (3, 2, 1)), conv=c, d3=d)

hr('§7 D.5.9 — the family. Printed L%d–L%d: first run (3B.five, 3B.pot as MEASURED) E = 4, three cells in formula · analysis and one in theorem · analysis; second run (3B.five proved, 3B.pot on its 650-triangle check = sampled) E = 2, formula · analysis admits measured · sampled · none found and verified · sampled · none found; third run (both on their derivations) E = 0' % UNITS['D.5.9'])
base65 = A5X(cum['D.5.9'])
MEAS = [(2, v, p) for v in (1, 2) for p in (0, 1)]
for c, d in ALL:
    print('   ' + lab(c, d) + ' — first run, both as measured, the four measured cells for each (sixteen pairs):')
    hits = []
    for a, b in itertools.product(MEAS, repeat=2):
        fe = fibreE(swap(swap(base65, '3B.five', a), '3B.pot', b), conv=c, d3=d); tot = sum(v[0] for v in fe.values())
        if tot == 4 and fe[('formula', 'analysis')][0] == 3 and fe[('theorem', 'analysis')][0] == 1: hits.append((a, b))
        if a == b: report('      both %s' % named(a), swap(swap(base65, '3B.five', a), '3B.pot', b), conv=c, d3=d)
    print('      pairs reproducing E = 4 as 3 (formula · analysis) + 1 (theorem · analysis):', [(named(a), named(b)) for a, b in hits] or 'NONE')
    print('   ' + lab(c, d) + ' — second run, 3B.five proved · exhaustive · found, 3B.pot on its sampled check:')
    for co in ((2, 1, 0), (3, 1, 0), (2, 1, 1), (3, 1, 1), (4, 1, 1), (4, 1, 0)):
        report('      3B.pot %s' % named(co), swap(base65, '3B.pot', co), conv=c, d3=d)
    report('   ' + lab(c, d) + ' — third run, both as printed (derivations)', base65, conv=c, d3=d)
fa = [x[4] for x in base65 if (x[2], x[3]) == ('formula', 'analysis')]; ta = [x[4] for x in base65 if (x[2], x[3]) == ('theorem', 'analysis')]
print('   formula · analysis occupants at 65 (as printed):', sorted(Counter(named(c) for c in fa).items()))
print('   theorem · analysis occupants at 65 (as printed):', sorted(Counter(named(c) for c in ta).items()))
print('   the first-run excess under BOOK with both measured · exhaustive · found, by fibre:', {' · '.join(k): [named(c) for c in v[1]] for k, v in fibreE(swap(swap(base65, '3B.five', (2, 2, 1)), '3B.pot', (2, 2, 1))).items() if v[0]})

hr('§8 the D.5.10 and L10880 statements (law · physics box) and the fibre counts at 65 / 77')
lp = [x[4] for x in elems if (x[2], x[3]) == ('law', 'physics')]
print('   law · physics: elements', len(lp), 'cells', sorted(named(c) for c in set(lp)), '; ℛ(X) − X under BOOK:', [named(c) for c in sorted(r2lib.Rset(lp) - set(lp))], '; box ∏Âᵢ − X:', [named(c) for c in sorted(set(itertools.product(*[sorted({x[i] for x in lp}) for i in range(3)])) - set(lp))], '(L10880 names conjectured · exhaustive and proved · sampled)')
print('   fibres at 65:', len({(x[2], x[3]) for x in cum['D.5.9']}), '(printed twenty-two) ; at 77:', len({(x[2], x[3]) for x in cum['D.5.10']}), '(printed twenty-four) ; fibres new at D.5.10:', sorted(set((x[2], x[3]) for x in cum['D.5.10']) - set((x[2], x[3]) for x in cum['D.5.9'])), '(printed measurement · analysis, formula · order)')
print('   D.5.9 sum: 48 + 17 =', len(cum['D.5.8']) + len(d59), '; D.5 column: 32 + 4 + 4 + 8 + 17 + 12 =', 32 + 4 + 4 + 8 + 17 + 12)

hr('§9 census rows of DEFECT-CENSUS.tsv inside D.5.5 / D.5.9 (main volume)')
try:
    rows = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]
    hdr = rows[0]; print('   header:', hdr)
    vi = next((i for i, h in enumerate(hdr) if h.lower() in ('volume', 'vol', 'file')), None); li = next((i for i, h in enumerate(hdr) if h.lower() in ('line', 'ln')), None)
    hit = []
    for r in rows[1:]:
        try:
            ln = int(r[li]); vol = r[vi] if vi is not None else ''
        except Exception: continue
        if ('main' in vol.lower() or MAIN in vol or vol == '') and any(UNITS[t][0] <= ln < UNITS[t][1] for t in ('D.5.5', 'D.5.9')): hit.append(r[:4])
    print('   rows in the two units:', hit or 'none')
except Exception as ex: print('   census read:', ex)
