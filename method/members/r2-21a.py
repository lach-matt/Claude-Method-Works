#!/usr/bin/env python3
# r2-21a.py — chat 145 — the Sc VI bracket family (DEF-143 item 11's first re-derivation: 21a-02 / 21a-03 with E.3's bracket
# site; DEF-134 items 2–3, DEF-138 item 12): §25.2's limit 892,700 ± 400, §25.6.1–§25.6.6's bracket and point estimates,
# §32.5.1's recomputation table, Appendix C.3 L10299–L10303, Appendix E.3 item A, and every other main-volume Sc VI site.
# Every printed figure censused and re-derived on the instruments the bundle holds. Reads MEMBERS by name (never a bundle
# path). Deterministic: no wall clock, no randomness. Decimal for every printed figure, never round(). Every convention is
# named before a figure is scored. A re-derivation that disagrees with the record is a finding about the re-derivation
# (G0c); a figure whose instrument is not held is UNREPRODUCIBLE with a stated budget, never withdrawn. Held inputs: the
# two measured defects and the limit AS PRINTED (main §25.6.1, §25.2), R∞ and hc/e (CODATA 2018, imported constants —
# the book's own "R* is the only import", L9183), tower-2 via r2lib.load_tower().
import os, re, sys, hashlib, importlib.util
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
getcontext().prec = 40
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
def D(x, places): return Decimal(x).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)
def Dc(x): return '{:,}'.format(int(D(x, 0)))   # printed integer form with thousands comma

def rbody(n):   # copied verbatim from r2-scf.py (there from r2-ch34re.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-scf.py (there from r2-ch34re.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-scf.py (there from r2-ch34re.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

def bounded(f): return re.compile(r'(?<![\d.,])' + re.escape(f) + r'(?![\d])')   # a digit-bounded figure probe: 11,520 does not hit 1,520
def sites(f, vol='main'): return [i for i, l in enumerate(TXT[vol], 1) if bounded(f).search(l)]
def encl_reg(i):
    for j in range(i, 0, -1):
        m = re.match(r'^###\s+(\S+)', R[j - 1])
        if m: return m.group(1)
    return '?'

hr('§0 IDENTITY AND BOUNDARIES')
for n in (MAIN, REG, MC, PC, IOI, SC, 'r2lib.py', 'tower-2.py'): print('  %-52s md5 %s  %d lines' % (n, md5(n), len(rd(n))))
T = r2lib.load_tower(); print('  tower-2 loaded via r2lib.load_tower():', 'tower2' in repr(T))
SPANS = {}
for sec in ('25.2', '25.6', '25.6.1', '25.6.2', '25.6.3', '25.6.4', '25.6.5', '25.6.6', '32.5.1', '18.6.3', '22.2.1', '28.9'):
    hl = r2lib.heading_line(M, sec); ss = r2lib.section_span(M, sec); br = body_range(M, sec)
    hits = [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4} ' + re.escape(sec) + r'\.? ', t.strip())]
    print('  §%-7s heading_line %5d %-60s hits %s | section_span %s | body_range %s | differ by %d' % (sec, hl, repr(M[hl - 1][:58]), hits, ss, br, ss[1] - br[1]))
    SPANS[sec] = ss
for tag in ('C.3', 'C.4', 'E.3', 'E.4', 'E.5'):
    h = lettered(M, tag); print('  lettered(%s) = %s %s' % (tag, h, repr(M[h[-1] - 1][:70]) if h else '(no heading line — E.4 is 24b-02\'s unmarked line)'))
C3 = (lettered(M, 'C.3')[-1], lettered(M, 'C.4')[-1]); E3 = (lettered(M, 'E.3')[-1], lettered(M, 'E.5')[-1])
E4u = [i for i in range(E3[0], E3[1]) if re.match(r'^\s*E\.4\s+[A-Z]', M[i - 1])]
print('  C.3 span by lettered heading', C3, '| E.3 span to E.5', E3, '| E.4 unmarked heading candidate inside it', E4u, '(E.3 proper ends there; item A is L%d–L%d)' % (E3[0] + 4, E3[0] + 6))
print('  the census spans: §25.2, §25.6 (section_span, six subsections), §32.5.1, C.3 (to C.4), E.3 item A, plus every other main-volume line naming Sc VI')

hr('§1 THE FAMILY LOCATED — figure sites in six volumes, the Register grepped for a later statement, the pointers')
FIGS = ['892,700', '696,400', '648,096', '735,091', '735,092', '735,860', '737,380', '738,547', '736,688', '2,687', '1,520', '1,398',
        '784,416', '784,128', '785,209', '784,605', '1,081', '478', '1,594', '2,169', '1.0057', '0.9812', '1.0889', '0.9376', '0.9679',
        '0.9567', '0.9934', '13.5743', '13.5615', '13.5895', '91.338', '0.514', '129']
for f in FIGS:
    row = {k: sites(f, k) for k in VOLS}
    print('  %-8s' % f, ' '.join('%s %s' % (k, v) for k, v in row.items() if v) or '— no site in any volume')
scvi = {k: [i for i, l in enumerate(TXT[k], 1) if re.search(r'Sc\s?VI\b|Sc⁵⁺|Sc 5\+', l)] for k in VOLS}
print('  "Sc VI" (also Sc⁵⁺) by volume:', {k: len(v) for k, v in scvi.items()}, '| main lines', scvi['main'])
print('  scandium in the Register (any case):', sorted({encl_reg(i) for i, l in enumerate(R, 1) if re.search(r'[Ss]candium', l)}, key=int), '— none is the Sc VI channel (read: 957 spectra list, 1302/1303 Sc I ground, 1411 block openings, 1444, 1575, 1591, 1596, 1620, 1627, 1639 reading lists)')
print('  the Register prints NONE of the family\'s figures (bounded probe above, reg column empty for all %d) — the family has no Register home; "1,520" hits 1303 only as the substring of 11,520 under an unbounded probe (regex artefact, not a site)' % len(FIGS))
ptrs = []
for a, b in [SPANS['25.2'], SPANS['25.6'], SPANS['32.5.1'], C3, (E3[0], E4u[0] if E4u else E3[1]), (6110, 6118), (7483, 7487), SPANS['18.6.3']]:
    for i in range(a, b):
        for m in re.finditer(r'[Rr]egister\s+(\d+)', M[i - 1]): ptrs.append((i, int(m.group(1))))
print('  register pointers inside the family spans:', ptrs)
for _, n in sorted(set(ptrs)):
    b = rbody(n); print('  Register %d body: %s' % (n, (b or 'ABSENT')[:150])); print('    WARNING lines in entry:', sum(1 for l in R[[i for i, l in enumerate(R) if l.strip() == '### %d' % n][0]:][:40] if 'WARNING' in l and not l.startswith('### ')))
secptr = sorted({m.group(1) for a, b in [SPANS['25.2'], SPANS['25.6'], SPANS['32.5.1'], C3, (E3[0], E3[0] + 7)] for i in range(a, b) for m in re.finditer(r'§(\d+(?:\.\d+)*)(?!\d)', M[i - 1])})
print('  §-pointers printed in the family spans:', secptr)
for sec in ('24.2', '24.6', '23.11'):
    hl = r2lib.heading_line(M, sec); print('    §%s = L%d %s' % (sec, hl, repr(M[hl - 1][:80])))
print('    §24.6 cited at L7115 for "the deductive bracket" — the bracket is §25.6.1–§25.6.2\'s (a pointer finding, checked under both resolvers: §24.6 body carries none of the family figures:', [f for f in FIGS if any(bounded(f).search(M[i - 1]) for i in range(*SPANS.get('24.6', r2lib.section_span(M, '24.6'))))], ')')

hr('§2 CENSUS — every numeral printed in the family spans, one line each')
def numerals(l): return [m.group(0) for m in re.finditer(r'(?<![\w.])\d[\d,]*(?:\.\d+)?%?', l)]
tot = 0; lines = 0
for label, (a, b) in [('§25.2', SPANS['25.2']), ('§25.6', SPANS['25.6']), ('§32.5.1', SPANS['32.5.1']), ('C.3', C3), ('E.3 item A', (E3[0] + 4, E3[0] + 7)), ('§22.2.1 clause site', (6114, 6115)), ('§28 item 49', (7485, 7486)), ('§18.6.3 cell claim', (5355, 5356))]:
    for i in range(a, b):
        ns = [n for n in numerals(M[i - 1]) if not re.fullmatch(r'\d{1,2}\.\d{1,2}(\.\d+)?', n)]   # section numbers excluded
        if ns: tot += len(ns); lines += 1; print('  %-20s L%-5d %s' % (label, i, ' · '.join(ns)))
print('  numerals censused:', tot, 'on', lines, 'lines (section numbers excluded; every one scored in §3–§6 or named unreproducible in §7)')

hr('§3 CONVENTIONS NAMED BEFORE SCORING')
RINF = Decimal('109737.31568160'); HC = Decimal('1.239841984e-4'); ME_U = Decimal('5.48579909065e-4'); A_SC = Decimal('44.955908')
RSC = RINF / (1 + ME_U / A_SC)
I0 = Decimal('892700'); D4 = Decimal('1.0057'); D5 = Decimal('0.9812'); ZEFF = 6
print('  E(ns) = I − R·Z²/(n − δ)²  with I = 892,700 (L6914, ±400 not applied to the point values: L7018–L7019 "to be added at both edges"),')
print('  Z = 6 (L7075: Z_eff = 6 — the Rydberg electron outside Sc⁵⁺), R = R∞ = %s cm⁻¹ (CODATA 2018; L9183 "R* is the only import")' % RINF)
print('  rival R_Sc = R∞/(1 + m_e/M(⁴⁵Sc)) = %s (reduced mass, A = 44.955908) — tested as convention R2' % D(RSC, 5))
print('  δ(4s) = 1.0057, δ(5s) = 0.9812 READ from L7004 (inputs, not computed; C.3 L10287 "the input defects … not recomputed")')
print('  Ritz two-point: δ₂ = (δ₄ − δ₅)/(1/16 − 1/25), δ∞ = δ₄ − δ₂/16, δ(ns) = δ∞ + δ₂/n²; convex tangent δ(6s) ≥ 2δ(5s) − δ(4s); 7s tangent 2δ(6s) − δ(5s)')
print('  chain convention U: every δ carried unrounded (prec 40); chain convention P: each δ quantized to the 4 dp the book prints before use')
print('  Rule 4 constant defect δ̄ = (δ₄ + δ₅)/2 (L6114 "the constant form"); printed 0.9934 — 0.99345 at ROUND_HALF_EVEN → 0.9934, at half-up → 0.9935: the book\'s 4 dp is the half-even (or truncated) form')
print('  λ = 10⁷/E nm; eV = E·hc/e with hc/e = 1.239841984e-4 eV·cm; all figures quantized ROUND_HALF_EVEN at the printed precision')

hr('§4 RE-DERIVATIONS — §25.6.1 / §25.6.2 / §25.6.3 / §25.6.4 / §32.5.1 / E.3 / C.3')
def E(delta, n, Rc=RINF, I=I0): return I - Rc * ZEFF * ZEFF / (n - delta) ** 2
res = {'U': {}, 'P': {}}; CONV = ['U']
def score(name, got, printed, places=0, where=''):
    g = D(got, places); ok = (g == Decimal(printed.replace(',', '')))
    res[CONV[0]][name] = ok; print('  %-34s printed %-12s derived %-14s %s  %s' % (name, printed, '{:,}'.format(g) if places == 0 else g, 'EQUAL' if ok else 'DIFFERS', where))
for conv, q in (('U', lambda x: x), ('P', lambda x: D(x, 4))):
    CONV[0] = conv; print('  — chain convention', conv)
    d2 = q((D4 - D5) / (Decimal(1) / 16 - Decimal(1) / 25)); dinf = q(D4 - d2 / 16); d6 = q(dinf + d2 / 36); d7 = q(dinf + d2 / 49); dcx = q(2 * D5 - D4); dcx7 = q(2 * d6 - D5)
    score('δ₂ (L7010)', d2, '1.0889', 4); score('δ∞ (L7010, L7014)', dinf, '0.9376', 4); score('δ(6s) Ritz (L7010, L7063)', d6, '0.9679', 4); score('δ(6s) convex bound (L7025)', dcx, '0.9567', 4)
    score('E(6s) point (L7045, L7063, L9174)', E(d6, 6), '736,688'); score('E lower = E at δ(5s) (L7018, L7030)', E(D5, 6), '735,860')
    score('E upper monotone = E at δ∞ (L7018)', E(dinf, 6), '738,547'); score('E upper convex = E at 0.9567 (L7033)', E(dcx, 6), '737,380')
    score('width monotone (L7018, L7030)', E(dinf, 6) - E(D5, 6), '2,687'); score('width convex (L7033)', E(dcx, 6) - E(D5, 6), '1,520')
    score('factor tighter (L7035)', (E(dinf, 6) - E(D5, 6)) / (E(dcx, 6) - E(D5, 6)), '1.8', 1)
    score('E(7s) point (L7050)', E(d7, 7), '784,416'); score('7s lower = E at δ(6s) (L7050)', E(d6, 7), '784,128'); score('7s upper = E at δ∞ (L7050)', E(dinf, 7), '785,209')
    score('7s width (L7050)', E(dinf, 7) - E(d6, 7), '1,081'); score('7s convex upper (L7053)', E(dcx7, 7), '784,605'); score('7s convex width (L7053)', E(dcx7, 7) - E(d6, 7), '478')
    e6 = E(d6, 6)
    score('λ(6s) nm (L7045)', Decimal(10) ** 7 / e6, '13.5743', 4); score('window low nm = 10⁷/737,380 (L7046, L11059)', Decimal(10) ** 7 / E(dcx, 6), '13.5615', 4)
    score('window high nm = 10⁷/735,860 (L7046, L11059)', Decimal(10) ** 7 / E(D5, 6), '13.5895', 4); score('eV (L7046, L11059)', e6 * HC, '91.338', 3)
    dbar = q((D4 + D5) / 2); score('δ̄ Rule 4 (L6114, L7064, L7066, L7485)', dbar, '0.9934', 4)
    score('E at δ̄ (L7064, L7066, L10300)', E(dbar, 6), '735,091', 0, '(printed-δ̄ 0.9934 gives %s; unrounded 0.99345 gives %s)' % (Dc(E(D(dbar, 4), 6)), Dc(E((D4 + D5) / 2, 6))))
    score('C.3 δ from 696,400 (L10303 "0.514")', 5 - (RINF * 36 / (I0 - Decimal('696400'))).sqrt(), '0.514', 3)
    score('C.3 5s at δ = 0.9812 (L10303)', E(D5, 5), '648,096')
print('  — convention R2 (reduced-mass R_Sc) on the point value:', Dc(E(dinf + d2 / 36, 6)), 'vs printed 736,688 —', 'EQUAL' if D(E(dinf + d2 / 36, 6), 0) == 736688 else 'DIFFERS', '; R∞ is the constant the book used (L9183)')
print('  — E(6s) under R∞ but Z = 5 (a rival charge convention):', Dc(I0 - RINF * 25 / (6 - d6) ** 2), '— DIFFERS; Z_eff = 6 as L7075 states')
six = [k for k in res['U'] if any(s in k for s in ('E(6s) point', 'E lower', 'E upper', 'width monotone', 'width convex'))]
print('  §32.5.1\'s six of six (L9174–L9179): 736,688 · 735,860 · 738,547 · 2,687 · 737,380 · 1,520 — under U:', sum(res['U'][k] for k in six), 'of', len(six), 'EQUAL; under P:', sum(res['P'][k] for k in six), 'of', len(six), '(the book carried δ unrounded: U is its convention)')
print('  E.3 item A (L11058–L11059) = §25.6.3\'s bracket, window and eV token for token:', all(bounded(f).search(M[11057]) or bounded(f).search(M[11058]) for f in ('735,860', '737,380', '13.5615', '13.5895', '91.338')), '| the point value 736,688 is absent from E.3 (DEF-138 item 12 re-measured):', not any(bounded('736,688').search(M[i - 1]) for i in range(E3[0], E3[1])))
print('  C.3 L10300–L10301 "735,091 against 735,092": 735,091 = §25.6.4\'s δ̄ row (retired at L7066); 735,092 has no site outside C.3 (§1) —')
print('    the two differ by the δ̄ rounding: E(δ̄ = 0.9934) = %s, E(δ̄ = 0.99345) = %s (R∞); under R_Sc: %s / %s' % (Dc(E(Decimal('0.9934'), 6)), Dc(E(Decimal('0.99345'), 6)), Dc(E(Decimal('0.9934'), 6, RSC)), Dc(E(Decimal('0.99345'), 6, RSC))))
print('  735,092 under rival conventions — δ̄ half-up 0.9935:', Dc(E(Decimal('0.9935'), 6)), '; δ̄ 0.99345 with R∞ at 6 dp 109,737.316:', Dc(I0 - Decimal('109737.316') * 36 / (6 - Decimal('0.99345')) ** 2), '; with R = 109,737 exactly:', Dc(I0 - Decimal('109737') * 36 / (6 - Decimal('0.99345')) ** 2), '; with R_Sc:', Dc(E(Decimal('0.99345'), 6, RSC)), '; truncation instead of half-even of 735,091.4:', Dc(E(Decimal('0.99345'), 6)), '→ 735,092 reproduces under exactly one rival tried: R = 109,737 (R∞ at integer precision) — C.3\'s "independent" 735,092 and §25.6.4\'s 735,091 differ by the constant\'s precision alone; 735,092 stays unsited outside C.3 (21a-03 re-measured; a convention datum for docket 34)')
print('  the "± 1,398" of L7066 (an earlier version\'s spread) and §25.6.6\'s "± 1,594" / "± 2,169" (L7105–L7106): conventions tried —')
dEdd = 2 * RINF * 36 / (6 - Decimal('0.9679')) ** 3
for lab, val in (('half the monotone width 2,687/2', Decimal('2687') / 2), ('half the δ̄-form miss: |735,091 − 736,688|', abs(Decimal('735091') - Decimal('736688'))),
                 ('dE/dδ · 3.5 % of δ(6s)', dEdd * Decimal('0.035') * Decimal('0.9679')), ('dE/dδ · 3.5 % of δ(5s)', dEdd * Decimal('0.035') * D5), ('dE/dδ · (δ₄ − δ₅)', dEdd * (D4 - D5)),
                 ('dE/dδ · half (δ₄ − δ₅)', dEdd * (D4 - D5) / 2), ('E(δ₅) − E(δ̄) spread of the Rule-4 form', E(D5, 6) - E(Decimal('0.9934'), 6)), ('E(δ∞)−E(δ̄)', E(dinf, 6) - E(Decimal('0.9934'), 6))):
    print('    %-48s %s' % (lab, Dc(val)))
print('    none gives 1,398, 1,594 or 2,169 at printed precision → the three spreads are UNREPRODUCIBLE from the page (their convention is unprinted; §7 budget)')

hr('§5 THE TOWER — L5355 "the Sc VI 6s cell of §25.6 is in Λ — its coordinates are ordinary integers"')
L8 = T.L8(); print('  Λ₈ at the book\'s caps (n_max 3):', len(L8), 'cells; n ranges', sorted({c[0] for c in L8}), '— a 6s cell (n = 6) lies outside the capped rebuild by construction (caps (3,3,1,3,1), CLAUDE.md §2)')
print('  L5355 prints no coordinates for the cell; convention: the seven constraints of the generator with the caps lifted to n_max = e_max = 6 admit any 8-tuple with n = 6, ℓ = 0 iff 1 ≤ k ≤ 2, 0 ≤ q ≤ k, 1 ≤ e, 0 ≤ f ≤ min(1, e−1), 0 ≤ g ≤ min(4f+2, q), 0 ≤ 2S ≤ k')
cnt = 0
for k in range(1, 3):
    for q in range(0, k + 1):
        for e in range(1, 7):
            for f in range(0, min(1, e - 1) + 1):
                for g in range(0, min(4 * f + 2, q) + 1):
                    for S2 in range(0, k + 1): cnt += 1
print('  cells with (n, ℓ) = (6, 0) admitted under those constraints:', cnt, '(> 0: the claim "in Λ" holds for every completion; which completion is Sc VI\'s is unprinted — INFERRED reading, unscored)')
print('  membership of the printed 4s / 5s / 6s coordinates cannot be tested cell by cell: no 8-tuple is printed at L5355, §25.6 or E.3 (MEASURED: no parenthesised 8-tuple of integers in those spans:', not any(re.search(r'\(\s*\d+(\s*,\s*\d+){7}\s*\)', M[i - 1]) for a, b in (SPANS['25.6'], (5355, 5356), E3) for i in range(a, b)), ')')

hr('§6 §25.2\'s OTHER FIGURES — spectra data, not tower arithmetic')
for f, where in (('79%', 'L6898 Sr I node coverage'), ('100%', 'L6898 away from node, 11 cells'), ('60', 'L6895 collapse factor'), ('58.8%', 'L6905 Rule 3 coverage, 17 cells'), ('35.3%', 'L6907 earlier version'), ('41.2%', 'L6907 directional bracket'),
                 ('23', 'L6910 Ti I channels'), ('26', 'L6910 Ti I members'), ('55,000', 'L6911 Ti I limit'), ('42,000', 'L6911'), ('892,700', 'L6914 Sc VI limit'), ('400', 'L6914 ± limit'), ('6', 'L6914 channels'), ('10', 'L6914 configurations')):
    print('  %-8s %-40s sites main %-28s SC %s' % (f, where, sites(f)[:6], sites(f, 'sc')[:6]))
print('  the coverages (79 %, 100 % on 11, 58.8 %, 35.3 %, 41.2 %, 2 of 7 / 2 of 6 / 3 of 6) need Sr I, Ca II, Ba II level tables and the bracket code; the Ti I inventory (23 / 26) and Sc VI\'s 6 channels / 10 configurations need their ASD captures —')
print('  held in the bundle: Sc VI level table? no member names Sc VI or ScVI (MEASURED:', [n for n in os.listdir(H) if re.search(r'Sc\s?VI|ScVI', n)], '); the Spectra Compendium names Sc VI at', scvi['sc'], 'lines → UNREPRODUCIBLE, budget: the ASD captures of DEF-133 (COORDINATES-2_13.csv, not attached — HANDOFF-97 §0a) and the bracket instrument (not a member)')
print('  the 17-cell denominators: 58.8 % = 10/17 =', D(Decimal(10) / 17 * 100, 1), '; 35.3 % = 6/17 =', D(Decimal(6) / 17 * 100, 1), '; 41.2 % = 7/17 =', D(Decimal(7) / 17 * 100, 1), '— all three are k/17 at printed precision (EQUAL as fractions; the numerators are the bracket code\'s); the 2 + 2 + 3 = 7 reversing steps equal the directional bracket\'s numerator 7 — INFERRED coincidence, recorded unscored; the 17 cells themselves need the three series\' member counts, unprinted')
print('  79 % on the Sr I node: no k/N with N ≤ 20 at printed precision except', [(k, N) for N in range(1, 21) for k in range(N + 1) if D(Decimal(k) / N * 100, 0) == 79], '→ the cell count of the node span is unprinted; 100 % on 11 cells = 11/11')
print('  L7550 (§28 item 69) "129× worse": T-bracket width / δ-bracket width relative:', D((Decimal('1520') / Decimal('736688')) / (Decimal('0.0245') / Decimal('0.9679')), 1), '; absolute cm⁻¹ per unit δ at 6s:', Dc(dEdd), '; neither is 129 → UNREPRODUCIBLE from the page (the convention is unprinted; §28 was read at chat 116 — out of family, recorded)')

hr('§7 SUMMARY')
for c in ('U', 'P'):
    eq = sum(1 for v in res[c].values() if v); print('  convention %s: scored re-derivations %d, EQUAL %d, DIFFERS %d;' % (c, len(res[c]), eq, len(res[c]) - eq), 'DIFFERS rows:', [k for k, v in res[c].items() if not v] or 'none')
print('  a DIFFERS under P alone is a convention datum (the book carried δ unrounded), not a defect; a DIFFERS under U would be a finding about this instrument first (G0c)')
print('  UNREPRODUCIBLE with budget (record-carried, never withdrawn): 1,398 · 1,594 · 2,169 (spread conventions unprinted); the §25.2 coverages and inventories (spectra captures + bracket code); 129× (L7550)')
print('  the family\'s Register home: NONE (§1) — every figure of §25.6 / §32.5.1 / C.3 / E.3 lives only in the main volume; the one register pointer in the spans is 384 (E.3\'s own audit); docket 9(c)/30 gains the class "a committed prediction with no Register entry"')
