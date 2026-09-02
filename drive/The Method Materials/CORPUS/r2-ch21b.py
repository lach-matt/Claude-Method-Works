# r2-ch21b.py — chat 134 — R2 prose instrument for the main volume's Appendix C (`## Appendix C` to `## Appendix D`).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic. Readings the computable instrument
# (r2-ch21a) pointed at are PRINTED here rather than probed (a short cited passage is printed, not probed). Conventions:
# a first-person probe carries mine and myself and excludes the Roman numeral of a species (He I, Sc VI); a false-universal
# probe is word-bounded, case-insensitive, on the raw line; a Ruling 45/46 probe lists candidates for a hand reading, it does
# not score them; every negative names the sweep that produced it; passes are recorded as well as failures.
import os, re, io, sys, importlib.util, contextlib
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); S = rd('The_Method_1_6___Spectra_Compendium-2.md'); MC = rd('The_Method_1_6___Mathematical_Compendium-2.md')
VOL = {'main': M, 'reg': R, 'mc': MC, 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'), 'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': S}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def rbody(n):   # copied verbatim from r2-ch20a.py (there from r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
unit = ([i for i, l in enumerate(M, 1) if re.match(r'^## Appendix C ', l)][-1], [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix D ', l)][-1])
UL = M[unit[0] - 1:unit[1] - 1]
def uline(pat, flags=0): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l, flags)]
def P(v, a, b, w=200):
    t = VOL[v]
    for i in range(a, b + 1): print('   %s L%d %s' % (v, i, norm(t[i - 1])[:w]))
def sites(pat, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in VOL.items() if any(re.search(pat, l, flags) for l in t)}
print('unit L%d–L%d (%d lines)' % (unit[0], unit[1] - 1, unit[1] - unit[0]))

hr('§1 READINGS the computable instrument pointed at — printed, not probed')
print(' (a) §25.2 on Sc VI: the limit and the highest measured level (L10303 quotes *highest measured level is 5s at 696,400* from "§24.2")'); P('main', 6912, 6918)
print('     *highest measured* / *696* anywhere:', sites(r'highest measured'), sites(r'(?<![\d,.])696(?![\d,])'))
print(' (b) §23.10.4 supersedes the 1,061 bounds'); P('main', 6515, 6519)
print('     §25.5 heading and its 1,061 / 1.4 lines:', [(i, norm(M[i - 1])[:140]) for i in range(heading_line(M, '25.5'), heading_line(M, '25.6')) if re.search(r'1,061|1\.4 cm|tightest', M[i - 1])])
print(' (c) §10.2 the range the void-free fraction is stable over (unit: *2.4 points over a 100× range*)'); P('main', 2050, 2054)
print(' (d) §16.5 on the 30,000 samples (unit: *χ_Λ total — 30,000 ambient points — exact*; §3.3 L1242 says *until register 248*)'); P('main', 4453, 4458); print('     Register 248 body:', norm(rbody(248) or 'ABSENT')[:260]); print('     Register 248 WARNING:', [norm(l)[:200] for l in R[[i for i, l in enumerate(R) if l.strip() == '### 248'][0]:][:40] if 'WARNING' in l][:2])
print(' (e) the +0.35 sites in the Spectra Compendium (unit: *filled-d core raises δ +0.35 at low ℓ*)'); P('sc', 320, 320); P('sc', 429, 429)
print(' (f) the 200/200 sites (unit: *closure ⟺ ℛ(X) = X — 200/200 agreements* and *on 200 constructions*)'); P('main', 4678, 4681); P('mc', 600, 600)
print('     *200 constructions* / *constructions* in main:', sites(r'200 constructions'), [(i, norm(M[i - 1])[:120]) for i, l in enumerate(M, 1) if re.search(r'\b200\b.*construct|construct.*\b200\b', l) and not (unit[0] <= i < unit[1])][:4])
print(' (g) §32.6 — the three falsification tests, the book\'s own'); P('main', 9205, 9210); P('main', 9246, 9247); P('main', 9360, 9360)
print(' (h) §31.3.4 — the test of an external prediction'); P('main', 8728, 8730)
print(' (i) §16.3 — does it carry multi-target failure counts? (*target* lines in its span)'); print('    ', [(i, norm(M[i - 1])[:120]) for i in range(4359, 4407) if re.search(r'target|failure count', M[i - 1])][:6]); print('     *multi-target* anywhere:', sites(r'multi-target'))
print(' (j) §25.6.4 — the 735,091 row and the retirement sentence; §25.6 heading'); P('main', 6991, 6991); P('main', 7060, 7068)
print(' (k) §3.5 — does it give the dpi distribution?'); print('    ', [(i, norm(M[i - 1])[:160]) for i in range(1257, 1282) if re.search(r'dpi|distribution|\bf\d\d\b', M[i - 1])])
print(' (l) §22.2.1 ablation and §25.2 Sr I / Ti I — where the "§24.2" material lives'); P('main', 6055, 6057); P('main', 6894, 6894); P('main', 6910, 6910)
print(' (m) Register 783 WARNING and the 1,442 standing:', [norm(l)[:220] for l in R[[i for i, l in enumerate(R) if l.strip() == '### 783'][0]:][:30] if 'WARNING' in l or '1,442' in l][:3])
print(' (n) Chapter 28 L7373 (the 1,635) and the unit\'s *errors*'); P('main', 7371, 7374)
print(' (o) the V formula: unit L10317 *V = 4x/(h|p−1|)*; the volume\'s V definition sites:', sites(r'4x/|4\*x\*/'), [(i, norm(M[i - 1])[:140]) for i in range(heading_line(M, '23.1'), heading_line(M, '23.1') + 16) if re.search(r'V\s*=|\bV\b.*=', M[i - 1])][:4])
print(' (p) *single prediction* / *prediction* sites vs §25.6\'s title *why it is not a prediction*:', sites(r'single prediction'), sites(r'not a prediction'))

hr('§2 PROBES on the unit — first person, false universals, hedges, Ruling 45/46 candidates, formatting')
fp = [(i, norm(M[i - 1])[:120]) for i in uline(r'\b(I|my|we|our|mine|myself|us)\b') if not all(re.match(r'^(He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Y|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|I|Xe|Cs|Ba|Sc|Ti|Ne|Pt|Hg|Tl|Pb|Bi|U) (I|II|III|IV|V|VI)\b', m.group(0)) for m in re.finditer(r'\b[A-Z][a-z]? (I|II|III|IV|V|VI)\b', M[i - 1])) or re.search(r'\b(my|we|our|mine|myself|us)\b', M[i - 1])]
print('  first person (mine/myself carried; species Roman numerals excluded):', fp if fp else 'NONE in the unit')
print('  Roman-numeral species in the unit (excluded from the probe):', sorted(set(re.findall(r'\b(?:Sc|Sr|Ti|Al|He) (?:I|II|III|IV|V|VI)\b', ' '.join(UL)))))
for w in ['every', 'all', 'never', 'always', 'none', 'no', 'single', 'exactly', 'exact', 'only', 'silently', 'independently', 'unaffected']:
    h = uline(r'\b%s\b' % w, re.I)
    if h: print('  %-14s' % w, [(i, norm(M[i - 1])[:110]) for i in h][:6])
print('  Ruling 45 candidates (process / revision / session / pipeline / build words):', [(i, norm(M[i - 1])[:130]) for i in uline(r'this revision|this book|earlier plotting pipeline|sessions|earlier version|earlier form|earlier work|recorded, not regenerated|is recorded')])
print('  Ruling 46 candidates (code identifiers / file labels / software):', [(i, norm(M[i - 1])[:130]) for i in uline(r'figure\.dpi|\bf\d\d\b|Python 3|NumPy')])
print('  table form: C.1 is whitespace-aligned (no `|` rows in the unit):', [i for i in uline(r'^\s*\|')], '; markdown tables elsewhere in the appendices (`| ` rows L9937–L11408):', len([i for i, l in enumerate(M, 1) if 9937 <= i < 11409 and re.match(r'^\s*\|', l)]))
print('  Register cites in the unit (`[Rr]egister N`, `entries N`):', uline(r'[Rr]egisters? \d|entr(y|ies) \d'), '— none; witness: the sweep above on all 90 lines')
print('  wrapped-phrase check on the markup-stripped join: *13× better than at an end*, *ℓ ≥ 3, where cores converge*, *2.4 points over a 100× range*:', [bool(re.search(p, re.sub(r'\*+', '', norm(' '.join(UL))))) for p in [r'13× better than at an end', r'ℓ ≥ 3, where cores converge', r'2\.4 points over a 100× range']])

hr('§3 BIBLIOGRAPHY — every named author in the unit against the `## References` body (docket 36)')
ref = [k for k, x in enumerate(M, 1) if x.startswith('## References')][-1]
for a in sorted(set(re.findall(r'\b([A-Z][a-z]{2,})(?= et al\.| \(\d{4}\))', ' '.join(UL)))):
    print('  %-10s References body sites:' % a, [i for i, l in enumerate(M, 1) if i > ref and re.search(r'\b%s\b' % a, l)])
print('\nEND r2-ch21b')
