# r2-ch21a.py — chat 134 — R2 computable instrument for the main volume's Appendix C (`## Appendix C` to `## Appendix D`).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock). Appendix C is PRE-PP:
# headings and Statement lines are diffed against the Prints & Proofs original at /home/claude/PP_The_Method_1_6.md (fetched
# at the gate; section number stripped from BOTH sides; PP's C.n sub-headings are unmarked plain lines found by scan).
# Conventions named before scoring: a numeral is digit-bounded both sides and admits a trailing non-thousands comma; a count of
# separator-delimited items is taken on the whitespace-normalised join of the paragraph split on the middle dot ` · `; the C.1
# table's DATA rows are the lines of the whitespace-aligned table whose first non-space token is not a header word and that
# begin at the conclusion column (continuation lines, which begin deeper, are joined to the row above) — the DATA-row set is
# fixed and printed before any count word is scored; Decimal.quantize ROUND_HALF_UP for every rounding; a Register entry body is
# the first non-blank line after `### N`; every negative carries its witness (the sweep and what it covered).
import os, re, io, sys, importlib.util, contextlib
from decimal import Decimal as D, ROUND_HALF_UP, getcontext
from collections import Counter
getcontext().prec = 28
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); S = rd('The_Method_1_6___Spectra_Compendium-2.md')
PPP = '/home/claude/PP_The_Method_1_6.md'
PP = open(PPP, encoding='utf-8').read().split('\n') if os.path.exists(PPP) else None
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': S}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch20a.py (there from r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch20a.py (there from r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def lettered(M, tag):   # copied verbatim from r2-ch20a.py (there from r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def hd(i):
    for j in range(i, 0, -1):
        if re.match(r'^#{1,4} ', M[j - 1]): return '%s L%d' % (M[j - 1].split(' ')[1] if len(M[j - 1].split(' ')) > 1 else '?', j)
NUM = r'(?<![\d,.])\d{1,3}(?:,\d{3})+(?!\d)(?!,\d{3})|(?<![\d,.])\d+(?!\d)(?!,\d{3})'

hr('§0 BOUNDARY — own heading scan; the unit is `## Appendix C` (body = last hit) to `## Appendix D` (body = last hit)')
appC = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix C ', l)]; appD = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix D ', l)]
unit = (appC[-1], appD[-1]); UL = M[unit[0] - 1:unit[1] - 1]
Cn = [(i, l) for i, l in enumerate(M, 1) if unit[0] < i < unit[1] and re.match(r'^#{2,4}\s*C\.\d', l)]
print('  `## Appendix C`', appC, '; `## Appendix D`', appD, '; unit L%d–L%d = %d lines; C.n headings:' % (unit[0], unit[1] - 1, unit[1] - unit[0]), [(i, l.split()[1]) for i, l in Cn])
print('  lettered(M, "C.%d") =' % 1, [lettered(M, 'C.%d' % k) for k in (1, 2, 3, 4)], '; unmarked-heading test (blank line above + `C.n ` start):', [unit[0] + k for k, l in enumerate(UL) if k and not UL[k - 1].strip() and re.match(r'^\s*C\.\d+ ', l)])
print('  main volume read to L%d of %d = %s (HALF_UP 3 places); lines 9937 `# APPENDICES` =' % (unit[1] - 1, len(M), q(D(unit[1] - 1) / D(len(M)), '0.001')), [i for i, l in enumerate(M, 1) if l.startswith('# APPENDICES')])
def uline(pat): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l)]
nums_unit = Counter(n for l in UL for n in re.findall(NUM, l))
print('  numerals in the unit (digit-bounded both sides, comma groups kept, trailing non-thousands comma admitted):', sorted(nums_unit.items(), key=lambda t: -int(t[0].replace(',', '')))[:60])

hr('§1 PRE-PP — headings and Statement lines against Prints & Proofs (section number stripped from BOTH sides; PP C.n headings are unmarked)')
if PP:
    pa = [i for i, l in enumerate(PP, 1) if l.startswith('# Appendix C')][-1]; pb = [i for i, l in enumerate(PP, 1) if l.startswith('# Appendix D')][-1]
    ppu = PP[pa - 1:pb - 1]
    pph = [(pa + k, l) for k, l in enumerate(ppu) if k and not ppu[k - 1].strip() and re.match(r'^\s*C\.\d+ ', l)]
    strip = lambda s: norm(re.sub(r'^[#\s]*(Appendix C\s*—|C\.\d+)\s*', '', s))
    print('  PP `# Appendix C` P%d to `# Appendix D` P%d = %d lines; PP unmarked C.n headings:' % (pa, pb, pb - pa), [(i, l.split()[0]) for i, l in pph])
    mh = [(unit[0], M[unit[0] - 1])] + Cn; ph = [(pa, PP[pa - 1])] + pph
    for (mi, ml), (pi, pl) in zip(mh, ph): print('   L%d ~ P%d  equal after strip: %s  [%s]' % (mi, pi, strip(ml) == strip(pl), strip(ml)[:60]))
    st = lambda T: [(k, l) for k, l in enumerate(T) if re.match(r'^\s*\*\*Statement', l)]
    print('  Statement lines: main', st(UL), '; PP', st(ppu))
    mn = [norm(l) for l in UL if l.strip()]; pn = [norm(l) for l in ppu if l.strip()]
    print('  non-blank lines main %d vs PP %d; lines of main not in PP: %d; lines of PP not in main: %d' % (len(mn), len(pn), len([l for l in mn if l not in pn]), len([l for l in pn if l not in mn])))
    import difflib
    for d in difflib.unified_diff(pn, mn, 'PP', 'main', n=0, lineterm=''):
        if d.startswith(('+', '-')) and not d.startswith(('+++', '---')): print('   ', d[:200])
else: print('  BUDGET: PP not on disk')

hr('§2 THE C.1 TABLE — DATA-row set fixed first (rows begin at the conclusion column; deeper-indented continuation lines are joined to the row above)')
t0 = uline(r'^\s+conclusion\s+statistic\s+margin\s+breaks down at')[0]
tab = []; k = t0 + 1
col = len(M[t0 - 1]) - len(M[t0 - 1].lstrip())
while M[k - 1].strip():
    l = M[k - 1]; ind = len(l) - len(l.lstrip())
    if ind <= col + 1: tab.append([k, l])
    else: tab[-1][1] = tab[-1][1].rstrip() + ' ⏎ ' + l.strip()
    k += 1
print('  header L%d; DATA rows fixed: %d (L%d–L%d); rows:' % (t0, len(tab), tab[0][0], tab[-1][0]))
for i, l in tab: print('   L%d %s' % (i, norm(l)[:150]))
print('  *Three rows deserve a sceptic\'s attention first* L%s → the three discussed below: bracket L%s, perturbation L%s, isoelectronic L%s' % (uline(r'Three rows deserve'), uline(r'bracket.s 1,442/1,442 breaks'), uline(r'perturbation bounds are as strong'), uline(r'isoelectronic interpolation is quoted')))

hr('§3 EVERY PRINTED FIGURE OF C.1/C.2/C.3 RE-TAKEN — witness site outside the unit (six volumes; digit-bounded) or the arithmetic that reproduces it')
def out(pat, vols=VOL, flags=0):
    r = sites(pat, vols, flags); r['main'] = [i for i in r['main'] if not (unit[0] <= i < unit[1])]; return {k: v for k, v in r.items() if v}
def show(label, pat, flags=0, ctx=None):
    r = out(pat, flags=flags); print('  %-44s %s' % (label, r if r else 'ABSENT outside the unit in all six volumes'))
    if ctx and r.get('main'): print('      main:', [(i, hd(i), norm(M[i - 1])[:ctx]) for i in r['main'][:3]])
show('E = 36 (periodic table not closed)', r'E\s*=\s*36\b', ctx=90)
show('seven indices', r'seven indices', ctx=100)
show('200/200 agreements / constructions', r'200/200|200 constructions|200 (random )?construct', ctx=110)
show('420 random (nonlinear) maps', r'\b420\b', ctx=110)
show('Proposition 23.1 (V > 2 monotone)', r'Proposition 23\.1\b', ctx=110)
print('    V > 2 monotone site:', out(r'V\s*>\s*2\b'))
print('    32/11 = %s (HALF_UP 6 places) ; printed 2.909091 ; 32/11 sites (docket 11):' % q(D(32) / D(11), '0.000001'), out(r'32/11'), '; 2.909 sites:', out(r'2\.909'))
show('2,513/2,513 nine functions', r'2,513', ctx=90)
show('30,000 ambient points (χ_Λ)', r'30,000', ctx=160)
show('20/20 two cap settings (order recovery, tree)', r'20/20|20 of 20', ctx=120)
print('    order recovery / tree propagation / cap settings:', out(r'order recovery'), out(r'tree propagation'), out(r'cap settings'))
show('1,442/1,442 bracket (20a-01 family; Register 783)', r'1,442/1,442|1,442 of 1,442', ctx=120)
print('    1,442 sites outside the unit:', out(r'(?<![\d,.])1,?442(?![\d,])(?!,\d{3})'), '; 783 body:', norm(rbody(783) or '')[:200])
show('1,061 perturbation bounds', r'1,061', ctx=170)
show('tightest 1.40 cm⁻¹ / 1.4 cm⁻¹ shift', r'1\.40? cm|tightest', ctx=120)
show('1.3% median (isoelectronic)', r'(?<![\d.])1\.3\s?%', ctx=140)
print('    13× = 17.3 / 1.3 = %s (HALF_UP 0 places) from L6078 row *Z, along a sequence | 17.3% | 1.3% | 2.1%*; 13× literal sites:' % q(D('17.3') / D('1.3'), '1'), out(r'13×|thirteen ?(times|fold)'))
show('2.1% hold-out / 3.5% fifth member', r'3\.5\s?% rather than the 2\.1\s?%|2\.1\s?% a hold-out', ctx=150)
show('0.06%–4.4% median (V = 4ν/3 real channels)', r'0\.06\s?%|0\.06–4\.4', ctx=120)
print('    4ν/3 median / real channels sites:', out(r'4ν/3'), '(docket 11: 24 sites); "coarse quotation":', out(r'coarse quotation'))
show('27.7–30.1% void-free', r'27\.7', ctx=160)
print('    *2.4 points* = 30.1 − 27.7 = %s ; *100× range* sites:' % q(D('30.1') - D('27.7'), '0.1'), out(r'100×|hundredfold|100-fold'), '; §10.2 says:', [norm(M[i - 1])[:150] for i in out(r'seventeenfold|17×|17-fold').get('main', [])])
show('+0.35 at low ℓ (filled-d core)', r'\+\s?0\.35|0\.35 at|filled-d', ctx=140)
print('    ℓ ≥ 3 cores converge:', out(r'ℓ ≥ 3'), out(r'cores converge'))
show('0.09σ antiprotonic two-route', r'0\.09\s*σ', ctx=100)
show('Singer et al. C₆ cost-law', r'Singer', ctx=140)
print('    Singer in `## References` body:', [i for i, l in enumerate(M, 1) if i > [k for k, x in enumerate(M, 1) if x.startswith('## References')][-1] and 'Singer' in l])
show('antisymmetric-state enumeration / census', r'antisymmetric.state|antisymmetric', ctx=120)
show('three falsification tests (§32.6)', r'three falsification|falsification tests', ctx=140)
show('external prediction (§31.3.4)', r'external prediction', ctx=140)
show('rule-ablation costs (§24.2)', r'ablation', ctx=140)
show('Sr I node coverages (§24.2)', r'Sr I', ctx=120)
show('Ti I channel inventory', r'Ti I\b', ctx=120)
show('multi-target failure counts (§16.3)', r'multi-target', ctx=140)
show('per-species medians (earlier verification)', r'per-species median|earlier verification', ctx=140)
show('fifteen figures / figure.dpi = 160 / 140–164 dpi', r'figure\.dpi|140–164', ctx=180)
sec35 = body_range(M, '3.5'); s35 = M[sec35[0] - 1:sec35[1] - 1]
fl = sorted(set(re.findall(r'\bf\d\d\b', ' '.join(s35)))); flu = re.findall(r'\bf\d\d\b', ' '.join(UL))
print('    §3.5 body L%d–L%d figure labels %s (%d) vs unit\'s list %s (%d) equal: %s ; *fifteen* printed:' % (sec35[0], sec35[1] - 1, fl, len(fl), flu, len(flu), fl == sorted(flu)), uline(r'fifteen figures'), '; §3.5 says:', [norm(l)[:120] for l in s35 if re.search(r'[Ff]ifteen|15 figures', l)])
show('735,091 / 735,092 (§25.6 arithmetic)', r'735,09[12]', ctx=200)
print('    §25.6 live figures:', [(i, norm(M[i - 1])[:150]) for i in range(heading_line(M, '25.6'), heading_line(M, '25.6') + 120) if re.search(r'735,8|737,|738,|2,169', M[i - 1])][:6])
show('696,400 (Sc VI 5s, §24.2)', r'696[, ]?400', ctx=140)
show('648,096 / 0.514 / 0.9812', r'648,096|0\.514\b|0\.9812', ctx=140)
show('1,635 (Chapter 28 count)', r'1,635|one thousand six hundred and thirty-five', ctx=170)
hdg = [i for i, l in enumerate(R, 1) if re.match(r'^#{1,4}\s*\d+\s*$', l)]; nums = sorted(int(R[i - 1].strip('# ').strip()) for i in hdg)
print('    Register `### N` headings measured: %d ; distinct numbers %d ; min %d max %d ; missing in 1..max: %s' % (len(hdg), len(set(nums)), nums[0], nums[-1], [n for n in range(1, nums[-1] + 1) if n not in set(nums)][:20]))
ch28 = [i for i, l in enumerate(M, 1) if l.startswith('## 28. ')][-1]; ch29 = [i for i, l in enumerate(M, 1) if l.startswith('## 29. ')][-1]
print('    Chapter 28 body L%d–L%d; its count lines:' % (ch28, ch29 - 1), [(i, norm(M[i - 1])[:230]) for i in range(ch28, ch29) if re.search(r'1,635|entries|errors', M[i - 1]) and re.search(r'\d{3}', M[i - 1])][:6])
show('C₆ = n¹¹(...) Singer §26.5 / 2^d corners', r'2\^d', ctx=100)

hr('§4 THE Sc VI ARITHMETIC OF L10303 — δ from a level and a limit; two Rydberg conventions tried; the limit is looked for in the volumes')
R_inf = D('109737.31568'); m_ratio = D('1') / (D('44.955908') * D('1822.888486'))  # Sc-45 atomic mass, u per m_e (CODATA); INFERRED inputs, stated
R_Sc = R_inf / (D('1') + m_ratio); zeta = D('6')
print('  limit sites for Sc VI in the volumes:', {k: v[:6] for k, v in sites(r'Sc VI.*(limit|ionis|ioniz)|(limit|ionis|ioniz).*Sc VI').items() if v})
lim = [(v, i, norm(t[i - 1])[:150]) for v, t in VOL.items() for i, l in enumerate(t, 1) if re.search(r'Sc VI', l) and re.search(r'(?<![\d,.])(8|9)\d\d,\d{3}(?![\d,])', l)]
print('  Sc VI lines carrying an 8xx,xxx/9xx,xxx figure:', lim[:8])
for tag, Ry in (('R_inf', R_inf), ('R_Sc', R_Sc)):
    I = D('648096') + Ry * zeta ** 2 / (D('5') - D('0.9812')) ** 2
    nu = (Ry * zeta ** 2 / (I - D('696400'))).sqrt(); delta = D('5') - nu
    E5 = I - Ry * zeta ** 2 / (D('5') - D('0.514')) ** 2
    print('  %s = %s: I implied by δ(5s)=0.9812 at 648,096 → %s cm⁻¹ ; then 696,400 gives δ = %s (printed 0.514) ; δ=0.514 gives E = %s' % (tag, q(Ry, '0.001'), q(I, '1'), q(delta, '0.001'), q(E5, '1')))
for Ival in [int(x.replace(',', '')) for _, _, s in lim for x in re.findall(r'(?<![\d,.])(?:8|9)\d\d,\d{3}(?![\d,])', s)][:3]:
    for tag, Ry in (('R_inf', R_inf), ('R_Sc', R_Sc)):
        d5 = D('5') - (Ry * zeta ** 2 / (D(Ival) - D('696400'))).sqrt(); E = D(Ival) - Ry * zeta ** 2 / (D('5') - D('0.9812')) ** 2
        print('  with printed limit %d and %s: δ(696,400) = %s ; E(δ=0.9812) = %s' % (Ival, tag, q(d5, '0.0001'), q(E, '1')))

hr('§5 POINTERS — every § pointer in the unit resolved under body_range AND section_span to the CLAIM, not the heading')
ptr = sorted(set(re.findall(r'§(\d+(?:\.\d+)*)(?!\d)', ' '.join(UL))), key=lambda s: [int(x) for x in s.split('.')])
print('  pointers in the unit:', ptr, '; Chapter/Appendix/Part/Proposition words:', sorted(set(re.findall(r'(?:Chapter|Appendix|Part|Proposition) [\w.]+', ' '.join(UL)))))
CLAIM = {'25.3': r'2Z²R/ν³|ΔT', '25.4': r'never enters|failure regime', '25.6': r'3\.5\s?%|isoelectronic|sulphur-like', '24.2': r'Sc VI|Sr I|ablation|Ti I', '16.3': r'multi-target|failure', '32.6': r'three|falsification', '31.3.4': r'external|540', '3.5': r'figure\.dpi|140–164'}
for p in ptr:
    try: br = body_range(M, p); ss = section_span(M, p)
    except Exception as e: print('  §%s: resolver error %s' % (p, e)); continue
    hit = [i for i in range(br[0], br[1]) if re.search(CLAIM.get(p, r'(?!x)x'), M[i - 1])]
    print('  §%-7s body_range L%d–L%d  section_span %s  heading [%s]  claim-hits %s' % (p, br[0], br[1] - 1, ss, norm(M[br[0] - 1])[:70], hit[:5]))
for w in ('Chapter 28', 'Proposition 23.1', 'Appendix B', 'Part V', 'PART VI'):
    print('  %-16s heading sites:' % w, [(i, norm(M[i - 1])[:80]) for i, l in enumerate(M, 1) if re.match(r'^#{1,4}\s*(%s|%s)' % (re.escape(w.split()[-1] + '.'), re.escape(w.replace('PART ', 'PART ').replace('Part V', 'PART V'))), l) or (w == 'Proposition 23.1' and re.search(r'\*\*Proposition 23\.1', l))][:4])
print('  L10231 *Serving PART VI — THE RECORD AND THE REACH*; PART headings:', [(i, norm(M[i - 1])[:60]) for i, l in enumerate(M, 1) if re.match(r'^# PART (V|VI)\b', l)])

hr('§6 COUNT WORDS — C.2 *Fourteen results*, C.3 *Six results*, C.1 *Three rows*, C.3 *the six* — items on the middle-dot split of the normalised join')
def items(a, b): return [norm(x) for x in ' '.join(M[a - 1:b - 1]).split(' · ') if norm(x)]
c2 = uline(r'^ E\(X\) for seven indices')[0]; c2e = next(i for i in range(c2, unit[1]) if not M[i - 1].strip())
c3 = uline(r'^ the rule-ablation costs')[0]; c3e = next(i for i in range(c3, unit[1]) if not M[i - 1].strip())
I2 = items(c2, c2e); I3 = items(c3, c3e)
print('  C.2 L%d–L%d items = %d (printed *Fourteen*):' % (c2, c2e - 1, len(I2)), [x[:40] for x in I2])
print('  C.3 L%d–L%d items = %d (printed *Six*):' % (c3, c3e - 1, len(I3)), [x[:40] for x in I3])
print('  *the six* at L%s refers back to the six inherited results; *fifteen figures* list count %d' % (uline(r'consequential of the six'), len(flu)))
print('  1,105 / 153 sites in the unit (sites of 20a-01, not new findings):', uline(r'1,105|153 channels'), '; *earlier verification* in the unit (20a-02 site):', uline(r'earlier verification'))
print('\nEND r2-ch21a')
