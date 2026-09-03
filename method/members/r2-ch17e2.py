#!/usr/bin/env python3
# r2-ch17e2.py — chat 153 — SUCCESSOR to r2-ch17e.py, re-anchored. Identical measurements; one address moves.
# r2-ch17e printed 'L11832 is R.7' as a LITERAL inside a string. After r3-wl2's +8 shift at main L9608 the
# literal is stale and the instrument asserts a falsehood, so re-banking it would bank that falsehood.
# WHAT 11832 ACTUALLY IS, and the first re-anchor of it was WRONG: it is not the R.7 heading, which sits at
# 11806. It is the KAM site that falls INSIDE R.7 — the third element of `kam`. The sentence reads 'the site
# at 11832 is R.7's', not 'R.7 begins at 11832'. tools/proveanchor.py refused the first attempt (it printed
# 11806) and that refusal is what located the true referent. It is now derived from `kam` and R.7's own
# heading, so both move together. r2-ch17e is seated and is never edited in place (chat 68).
# PROVED by tools/proveanchor.py: on the pre-shift bundles this reproduces r2-ch17e.out byte-exact, so the
# change is provably addressing and not measurement (G0c).
# r2-ch17e.py — chat 130 — R2 computable batch for main L9892–L9936 (Chapter 36, `## 36.` body to `# APPENDICES`), BUILD90.
# Reads MEMBERS only; imports r2lib and r2-tb1 (this chat's intake golden instrument) by path. Chapter 36 is post-PP: stated
# once in §0, never diffed. The chapter is bounded by body_range of each sub-section and the `# APPENDICES` heading —
# never by section_span('36'), which runs into the appendices. Conventions named before verdicts; Decimal, never round();
# a count word counts DATA rows; a literal string is not a test; every negative carries its witness; passes recorded.
import os, re, io, sys, importlib.util, contextlib, itertools
from decimal import Decimal as D, ROUND_HALF_UP
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md'); CP = rd('The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md')
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch17c.py (there from r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch17c.py (there from r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def lettered(M, tag):   # copied verbatim from r2-ch17c.py (owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def text(a, b): return '\n'.join(M[a - 1:b - 1])

hr('§0 BOUNDARY — own heading scan, body occurrences; the chapter bounded by body_range and `# APPENDICES`')
h36 = [i for i, l in enumerate(M, 1) if re.match(r'^## 36\. ', l)]; app = [i for i, l in enumerate(M, 1) if re.match(r'^# APPENDICES\s*$', l)]
print('  `## 36.` occurrences (contents, body):', h36, '; `# APPENDICES` occurrences:', app, '; body = last hit')
subs = {s: body_range(M, s) for s in ('36.1', '36.2', '36.3', '36.4', '36.5', '36.6')}
for s, (a, b) in subs.items(): print(f'  §{s} body_range {a}–{b - 1}')
unit = (h36[-1], app[-1]); print('  unit:', unit[0], 'to', unit[1] - 1, '=', unit[1] - unit[0], 'lines')
print('  section_span(M, "36") =', section_span(M, '36'), '(runs into the appendices — NOT used; witness for the handoff note)')
print('  sub-section ranges tile the unit after the opening italic (L%d–L%d):' % (unit[0] + 1, subs['36.1'][0] - 1), all(subs[a][1] == subs[b][0] for a, b in zip(list(subs)[:-1], list(subs)[1:])) and subs['36.6'][1] == unit[1])
print('  POST-PP: PP carries no `## 36.` body — chat 129 measured 0 occurrences (r2-ch17c §0); stated once here, the unit is not diffed.')
U = text(*unit)

hr('§1 §36.2 FIGURES AGAINST REGISTER 1716/1717/1718/1719 AND THE INTAKE GOLDEN (r2-tb1, this chat)')
T = load('r2-tb1', quiet=True)
l02 = M[subs['36.2'][0] + 1]; print('  L%d begins: %s' % (subs['36.2'][0] + 2, l02[:60]))
print('  "Thirteen mass order-types, six checks each, 78 of 78": 13 × 6 =', 13 * 6, '; r2-tb1 §3b labels 13, distinct orderings', len(T.kinds), '(intake1-01: the count is of labels)')
print('  "344 cells, 0 join failures, 8,385 meet failures" vs r2-tb1 own cap 8:', T.own[T.caps.index(8)][:3] == (344, 8385, 0))
printed = [int(x.replace(',', '')) for x in re.search(r'meet failures ((?:[\d,]+ · )+[\d,]+)', l02).group(1).split(' · ')]
print('  caps 3–12 meet failures printed:', printed, '; count', len(printed), '= 10 caps:', len(printed) == 10, '; equal to own:', printed == [r[1] for r in T.own])
print('  "join failures at 0 throughout" vs own:', all(r[2] == 0 for r in T.own), '; "Two-body chain: 0 of either kind at every cap" vs own chain:', all(r[3] == 0 for r in T.own), '(the delivered operator counts meet-or-join failures in one number — "either kind" is that convention)')
print('  1716 body carries the same cap-8 triple and "caps 3–12 as in `3B.tri`" (the per-cap list is NOT in the Register — only main L%d and the delivery print it):' % (subs['36.2'][0] + 2), '344 cells' in rbody(1716), '3B.tri' in rbody(1716), 'reg sites of "90,705":', sites(r'90,705')['reg'], 'main sites:', sites(r'90,705')['main'])
print('  "Eight attribution questions, eight closed" — 1721 says "seven closed to named owners"; L%d (§E.5 paragraph) says "Seven belonged to others; the eighth … turned out to be classical" (1720 Lagrange 1770):' % (subs['36.3'][0] + 18), 'seven closed' in rbody(1721), 'Seven belonged to others' in M[subs['36.3'][0] + 17], '— convention: eight closed = seven to others + one to prior art; both counts reproduce under their own convention (wording pair, docket 34)')
print('  "One inherited polynomial wrong, replaced" vs 1719 "withdrawn" / "Replaced by N₈":', 'withdrawn' in rbody(1719), 'Replaced by N₈' in rbody(1719))
print('  `tb_audit.py` (1756): register 1756 present:', rbody(1756) is not None, '; Register lines containing tb_audit:', [i + 1 for i, l in enumerate(R) if 'tb_audit' in l], '; the 78/78 lives at 1717:', '78/78' in rbody(1717), '— DEVIATION: a citation with no entry (docket 9c); also a script name in a reader-facing line (Ruling 46, docket 6)')

hr('§2 REGISTER EXISTENCE 1713–1724 (L%d "register entries 1713–1724 carry the record") and every entry the unit cites' % (unit[0] + 2))
ex = {n: rbody(n) is not None for n in range(1713, 1725)}; print('  1713–1724 present:', sum(ex.values()), '/ 12; absent:', [n for n, v in ex.items() if not v])
cited = sorted(set(int(x) for x in re.findall(r'(?<![\d.])(1[67]\d\d|784)(?![\d])', U)))
print('  entry numbers named in the unit:', cited, '; present:', {n: rbody(n) is not None for n in cited})
print('  "Registers" cites (counted, G0i) in the unit:', len(re.findall(r'\bRegisters? \d', U)), '; "register N" lowercase names:', len(re.findall(r'\bregister \d', U)))
print('  1722–1723 (L%d): 1722 "Uniform failure" / 1723 "A fault of mine":' % (subs['36.3'][0] + 16), 'Uniform failure' in rbody(1722), 'convention' in rbody(1723))
print('  784 "second route" mechanism (L%d): 1719 says "Caught by second route (register 784\'s mechanism)"; 784 body opens:' % (subs['36.3'][0] + 18), norm(rbody(784))[:110])

hr('§3 §36.1 / §36.3 POINTERS RESOLVED TO THE CLAIM, NOT THE HEADING')
P = {'31.1.1': ('nothing here touches Poincaré', 'Poincaré'), '12.11.2': ('three', 'excluded forms'), '21.5.1': ('treewidth', 'one level'),
     '25.6': ('E = 0', 'prediction'), '18.4.1': ('realised closure', 'certificate'), '12.11.3': ('dichotomy', 'envelope'), '12.11.1.3': ('time column', 'moves'),
     '12.11.0.2': ('clock', 'assumption'), '12.11.4': ('path-dependent', 'physics is not'), '14.5': ('seed', 'closed'), '2.14': ('computed', 'written')}
for s, toks in P.items():
    a, b = section_span(M, s); t = text(a, b)
    print(f'  §{s:10s} heading L{a} span L{a}–L{b - 1} ({b - a} lines): ' + ' · '.join(f'"{k}" {has_token(t, k)}' for k in toks) + '   ' + M[a - 1][:52])
a, b = section_span(M, '21.5.1'); t = text(a, b)
tt = t.replace('*', '')   # markup stripped (bold **level 2** in the target)
print('  §21.5.1 states K₃ treewidth 2 / strong 3-consistency / ℛ reaches level 2:', 'treewidth 2' in tt, 'strong 3-consistency' in tt, bool(re.search(r'ℛ reaches level 2', tt)), '(L5692–L5693)')
a, b = section_span(M, '25.6'); t = text(a, b)
print('  §25.6 "E(Λ) = 0" / "proposes none" / "complete index" (the unit\'s "E = 0 and makes no predictions"):', 'E(Λ) = 0' in t, 'proposes none' in t, has_token(t, 'complete index'), '; L7000 is a post-PP forward pointer to Chapter 36 itself (E(Λ₃) = 0):', 'E(Λ₃) = 0' in M[6999])
a, b = section_span(M, '12.11.2'); t = text(a, b)
print('  §12.11.2 "join-closed" / "meet-broken" / sum / difference / symmetric:', [has_token(t, k) for k in ('join-closed', 'meet-broken', 'sum', 'difference', 'symmetric')])
a, b = section_span(M, '18.4.1'); t = text(a, b)
lead = next(i for i in range(a, b) if M[i - 1].startswith(' **Exhibited and checked, on every open object'))
j = lead + 2; assert M[j - 1].strip().startswith('open object'); rows = []
for k in range(j + 1, b):
    if not M[k - 1].strip(): break
    rows.append(M[k - 1].strip()[:30])
print('  §18.4.1 open-object table L%d: header L%d, DATA rows %d: %s -> "the book\'s own five" (L%d) counts DATA rows:' % (lead, j, len(rows), rows, subs['36.3'][0] + 4), len(rows) == 5)
print('  "a fourth open object outside the book\'s own five" — the three earlier outside objects are not named in the unit; sites of "open object" + "outside" in main:', sites(r'open object.{0,60}outside|outside.{0,60}open object')['main'], '(only the unit itself: count word without a witness in the volume — INCIDENTAL, docket 17 single-witness)')
a, b = section_span(M, '31.1.1'); t = text(a, b)
print('  L%d "§31.1.1 had already named the brackets: zero-velocity surfaces, Hill regions, KAM tori" — in §31.1.1 (L%d–L%d):' % (subs['36.3'][0] + 10, a, b - 1), {k: has_token(t, k) for k in ('zero-velocity', 'Hill', 'KAM')}, '(Hill = "Hill stability" L8626, "Hill radius" L8628, L8633)')
kam = sites(r'\bKAM\b')['main']; zv = sites(r'[Zz]ero.velocity')['main']; s1841 = section_span(M, '18.4.1')
# R.7's heading by content (body occurrence is the LAST hit), then the KAM sites lying inside it.
_r7_head = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*R\.7\b', l)][-1]
_kam_in_r7 = [i for i in kam if i >= _r7_head]
assert _kam_in_r7, 'no KAM site inside R.7 — the claim this line reports has moved, which is a finding'
print('  where the three brackets ARE named together: KAM sites', kam, '; zero-velocity sites', zv, '; those inside §18.4.1 L%d–L%d:' % (s1841[0], s1841[1] - 1), [i for i in kam + zv if s1841[0] <= i < s1841[1]], '— L5155–L5156 "Jacobi\'s zero-velocity surfaces, Hill spheres and KAM tori are all brackets"; L' + ','.join(str(i) for i in _kam_in_r7) + ' is R.7. DEVIATION: the pointer\'s target says nothing of two of the three; the claim lives in §18.4.1 (docket 9b)')
print('  Routh / 0.0385209 / "threshold" in §31.1.1:', [has_token(t, k) for k in ('Routh', '0.0385209', 'threshold')], '(L8642–L8644: the threshold IS there, Routh unnamed) ; "0.0385209" sites all volumes:', {k: v for k, v in sites(r'0\.0385209').items() if v})
E5 = lettered(M, 'E.5'); print('  §E.5 heading hits:', E5, '(body = last); "audit 7": §3 body L%d–L%d has "seven" audits described (17c B5):' % section_span(M, '3'), has_token(text(*section_span(M, '3')), 'seven'))

hr('§4 COUNT WORDS AND ARITHMETIC')
l06 = M[subs['36.3'][0] + 1]
classes = re.search(r'decomposed into (.+?), the decomposition', l06).group(1)
items = [x.strip() for x in re.split(r', | and ', classes)]
print('  L%d strata list: %s -> %d items; 1713 "FIVE ASYMPTOTIC CLASSES":' % (subs['36.3'][0] + 2, items, len(items)), 'FIVE' in rbody(1713), '; equal:', len(items) == 5)
print('  L%d "Euler\'s three collinear roots and Lagrange\'s two equilateral points" = 3 + 2 = 5 = "five points":' % (subs['36.3'][0] + 12), 3 + 2 == 5, '; r2-tb1 §3e: one positive Euler root per ordering, 3 orderings -> 3 roots (theorem restated)')
print('  L%d "13 of 13 on one check" vs 1718 "failed 13/13" and the delivered failing log (13 False rows in column A):' % (subs['36.3'][0] + 16), 'failed 13/13' in rbody(1718))
print('  L%d "wrong in two coefficients"; 1719 names U⁴ (2p²+16q vs 6p²−8q) and U² ("likewise wrong") and prints the withdrawn form only to its U⁴ term:' % (subs['36.3'][0] + 18))
V, u1, u2, u3 = T.V, T.u1, T.u2, T.u3
import sympy as sp
S2 = u1**2 + u2**2 + u3**2; S4 = u1**4 + u2**4 + u3**4; S6 = u1**6 + u2**6 + u3**6; S11 = u1**2 * u2**2 + u2**2 * u3**2 + u3**2 * u1**2
claim = V**8 - 4 * S2 * V**6 + (6 * S2**2 - 4 * S4 + 8 * S11) * V**4 - 4 * (S2**3 - S2 * S4 + 2 * S6) * V**2 + (S2**2 - S4)**2 - 64 * u1**2 * u2**2 * u3**2
diffc = [k for k in (8, 6, 4, 2, 0) if sp.expand(sp.Poly(claim, V).coeff_monomial(V**k) - sp.Poly(T.P8, V).coeff_monomial(V**k)) != 0]
print('  coefficients of the RECONSTRUCTED withdrawn form (TB1-n8_check.py `claim`) that differ from the norm, by degree:', diffc, '; U⁴ and U² among them:', {4, 2} <= set(diffc), '; count', len(diffc))
print('  the reconstruction\'s constant term (S₂²−S₄)² − 64u₁²u₂²u₃² = 4q² − 64r also differs from (p²−4q)²; the record prints no constant term, so "two" is untestable against the record and the third differing degree is a finding about the reconstruction (intake1-04): flag to the three-body project')
mu = (D(9) - D(69).sqrt()) / D(18); print('  L%d "μ < 0.0385209": (9−√69)/18 =' % (subs['36.3'][0] + 14), q(mu, '0.0000001'), '(HALF_UP, 7 places) ==', '0.0385209', ':', q(mu, '0.0000001') == '0.0385209')
l26 = M[subs['36.4'][0] + 1]
print('  L%d c_ij = (m_i m_j)^{3/2}/√(m_i+m_j): the delivered audit.py codes (m[i]*m[j])**1.5/np.sqrt(m[i]+m[j]):' % (subs['36.4'][0] + 2), '(m[i]*m[j])**1.5/np.sqrt(m[i]+m[j])' in open(os.path.join(H, 'TB1-audit.py'), encoding='utf-8').read())
print('  "order 6, 2 or 1 according to how many masses coincide": r2-tb1 |S| values', sorted(set(T.S_orders), reverse=True), '; three coincide -> 6, two -> 2, none -> 1: convention = order of the mass-preserving permutation group; realised counts', {k: T.S_orders.count(k) for k in (6, 2, 1)})
print('  "six numbers": three c_ij + three rays b_ij — a ray is a unit vector on S² (two coordinates); the count "six" is of objects (3 scalars + 3 rays), stated as the convention; INCIDENTAL')
print('  "cannot create a sixth point": five fixed points for every mass triple (Euler 3 + Lagrange 2) — r2-tb1 §3e; "close a meet, or open a join": join 0 at every cap, meet > 0 at every cap for all caps 3–12 (mass-free operator):', all(r[2] == 0 and r[1] > 0 for r in T.own))
print('  L%d "Xia 1992 … n = 5": References lines with Xia:' % (subs['36.5'][0] + 2), [i + 1 for i, l in enumerate(M) if has_token(l, 'Xia') and i + 1 > 11400], '; "1992" on those lines:', [ '1992' in M[i] for i, l in enumerate(M) if has_token(l, 'Xia') and i + 1 > 11400])

hr('§5 THE COMPANION PAPER MEMBER — the unit\'s figures carried there (existence and token counts; not a diff)')
cp = '\n'.join(CP); print('  member lines:', len(CP), '; first non-blank line:', next(l for l in CP if l.strip())[:90])
for k in ('78', '344', '8,385', '8385', '90,705', '90705', '0.0385209', '13 of 13', '13/13', 'Saari', 'Painlevé', 'Brudno', 'Montgomery', 'Xia', 'Chenciner', 'Lagrange', 'Euler', 'Routh', '1756', '1717', 'tb_audit'):
    print(f'    "{k}": {len(re.findall(re.escape(k), cp))}', end='')
print()
print('  the paper names its audit checks A–F ("check A" … "check F"):', [len(re.findall(r'\bcheck ' + c + r'\b', cp)) for c in 'ABCDEF'])

hr('§6 BIBLIOGRAPHY (docket 36) — names the unit introduces, in `## References` body and R.7')
refs = [i for i, l in enumerate(M, 1) if re.match(r'^## References', l)]; r7 = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*R\.7\b', l)]
print('  `## References` hits:', refs, '(body = last); R.7 hits:', r7, '; measured this chat, not carried')
rb, r7b = refs[-1], r7[-1]; RB = '\n'.join(M[rb - 1:r7b - 1]); R7 = '\n'.join(M[r7b - 1:])
names = ('Saari', 'Painlevé', 'Brudno', 'Montgomery', 'Xia', 'Moore', 'Chenciner', 'Euler', 'Lagrange', 'Poincaré', 'Jacobi', 'Maupertuis', 'Hill', 'Routh')
for n in names:
    print(f'  {n:11s} unit {has_token(U, n):2d}  main {sum(has_token(l, n) for l in M):3d}  References-body {has_token(RB, n):2d}  R.7 {has_token(R7, n):2d}  reg {sum(has_token(l, n) for l in R):3d}')
print('  absent from the References body (convention: word-bounded, case-insensitive, body L%d–L%d):' % (rb, r7b - 1), [n for n in names if has_token(RB, n) == 0])
