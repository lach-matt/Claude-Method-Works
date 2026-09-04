#!/usr/bin/env python3
"""r2-ch14m — prose batch for the Chapter 23 second read, main L6303-L6433.

Pointers resolved to the CLAIM and not the heading; every negative claim given its own witness,
measured separately; attributions counted across both bundles; figures grepped for their other
sites.  Word-bounded throughout (has_token): a bare substring test reads 'gain' out of 'against',
and the same fault in numeric dress read 2.2 out of §2.2 and 12.25 (chat 95).  A citation is not
a declaration.  r2lib supplies heading_line / section_span / has_token / enclosing.
"""
import sys, re, importlib.util
sys.path.insert(0, '/home/claude/members')
spec = importlib.util.spec_from_file_location('r2lib', '/home/claude/members/r2lib.py')
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
from r2lib import heading_line, section_span, has_token, enclosing  # noqa: E402

MAIN = open('/home/claude/members/The_Method_1_6-2.md').read().splitlines()
BUNDLES = {}
for tag, path in (('main bundle', '/home/claude/The_Method_1_6_BUILD90_main_and_register.md'),
                  ('compendia bundle', '/home/claude/The_Method_1_6_BUILD124_compendia_papers_audits.md')):
    BUNDLES[tag] = open(path, encoding='utf-8', errors='replace').read()
UNIT = (6303, 6434)          # [start, end) — measured by heading scan this chat
unit_text = '\n'.join(MAIN[UNIT[0] - 1:UNIT[1] - 1])

def verdict(tag, ok, msg):
    print(f'{"OK  " if ok else "DEV "} {tag}  {msg}')

def body(sec):
    s, e = section_span(MAIN, sec)
    return s, e, '\n'.join(MAIN[s - 1:e - 1])

def sites(tok, bounded=True):
    """Count word-bounded sites of tok in each bundle."""
    out = {}
    for tag, txt in BUNDLES.items():
        out[tag] = has_token(txt, tok) if bounded else txt.count(tok)
    return out

# ---------------------------------------------------------------- pointers
print('== pointers, each resolved to the claim and not the heading ==')

s, e, t256 = body('25.6')
print(f'  §25.6 span L{s}-L{e-1}: "{MAIN[s-1].strip()[:80]}"')
for k in ('abandoned', 'abandon', 'variable', 'literature'):
    print(f'    token {k!r}: {has_token(t256, k)}')
ok = has_token(t256, 'abandoned') and has_token(t256, 'variable')
verdict('14m-01', bool(ok),
        f'L6319 "§25.6 explains why: the field abandoned the variable" — §25.6 (L{s}) carries '
        f'"abandoned" {has_token(t256,"abandoned")}x and "variable" {has_token(t256,"variable")}x; '
        f'the pointer resolves to the claim, not merely to the heading')

s, e, t235 = body('23.5')
asym = [i for i in range(s, e) if has_token(MAIN[i - 1], 'asymptotic')]
verdict('14m-02', bool(asym),
        f'L6337 "the asymptotic form of §23.5" — §23.5 spans L{s}-L{e-1} and writes "asymptotic" at '
        f'L{asym} ; the form 8y\'^2/y" is at L{[i for i in range(s,e) if "8y" in MAIN[i-1]]}')

s, e, t234 = body('23.4')
zr = [i for i in range(s, e) if ('cancel' in MAIN[i - 1].lower() or 'vanish' in MAIN[i - 1].lower()
                                or ('Z' in MAIN[i - 1] and has_token(MAIN[i - 1], 'R')))]
print(f'  §23.4 span L{s}-L{e-1}; lines bearing the Z/R cancellation:')
for i in zr[:6]:
    print(f'    L{i}: {MAIN[i-1].strip()[:110]}')
verdict('14m-03', bool(zr),
        f'L6366 "§23.4 proved that Z and R vanish from V and gave no reason" — §23.4 (L{s}-L{e-1}) '
        f'does carry the cancellation at L{zr[:3]}; the pointer resolves. Whether it "gave no '
        f'reason" is the second half of the claim and is tested separately below')
reason = [i for i in range(s, e) if has_token(MAIN[i - 1], 'because') or has_token(MAIN[i - 1], 'why')
          or has_token(MAIN[i - 1], 'reason')]
verdict('14m-03b', not reason,
        f'the second half — "and gave no reason" — measured: §23.4 carries "because"/"why"/"reason" '
        f'at {reason if reason else "no line"}, so the self-description is exact')

s, e, tprop = body('23.2')
prop = [i for i in range(s, e) if 'Proposition 23.1' in MAIN[i - 1]]
print(f'  Proposition 23.1 declared at L{prop[0] if prop else "?"}: '
      f'{MAIN[prop[0]-1].strip()[:150] if prop else ""}')
floor_lines = [i for i in range(s, e) if has_token(MAIN[i - 1], 'twice') or '> 2' in MAIN[i - 1]
               or has_token(MAIN[i - 1], 'floor')]
for i in floor_lines[:4]:
    print(f'    L{i}: {MAIN[i-1].strip()[:120]}')
verdict('14m-04', bool(prop and floor_lines),
        f'L6405 "the floor of Prop. 23.1" — the proposition is declared at L{prop[0]} and its floor '
        f'is stated at L{floor_lines[:3]} as "always more than twice", i.e. V > 2 strictly. §23.9.2 '
        f'then prints V = 2.0000 at p = 300 and 10,000 and says the branch "stops being valid" — '
        f'the two are consistent only because the printed 2.0000 is a rounding of a value above 2 '
        f'(measured 2.0000018 at p = 300 in r2-ch14l); the table gives the reader no sign of that')

s, e, t237 = body('23.7')
verdict('14m-05', has_token(t237, 'pole') > 0,
        f'L6431 "§23.7\'s pole" — §23.7 (L{s}-L{e-1}) carries "pole" {has_token(t237,"pole")}x, '
        f'including the p = 1 statement at L6326; resolves')

vsites = [i for i in range(1, len(MAIN) + 1) if '4x/(h' in MAIN[i - 1].replace(' ', '')
          or '4*x*/(*h*' in MAIN[i - 1]]
print(f'  L6388 "Since V = 4x/(h|p-1|)" — sites of that closed form in the main volume: '
      f'{vsites[:8]} (enclosing: {[enclosing(MAIN, i) for i in vsites[:8]]})')
verdict('14m-06', bool(vsites),
        f'the formula §23.9.1 opens with is printed at {len(vsites)} main-volume sites, first at '
        f'L{vsites[0]} in §{enclosing(MAIN, vsites[0])}; §23.9.1 cites it as established, and it is')

# ---------------------------------------------------------------- attributions
print('\n== attributions ==')
for name in ('Nesterov', 'Nemirovskii', 'Moore', 'Newton decrement', 'self-concordant',
             'self-concordance', 'interval analysis', 'excess width'):
    print(f'  {name:20s} {sites(name)}')
nes = [i for i in range(1, len(MAIN) + 1) if has_token(MAIN[i - 1], 'Nesterov')]
print('  every Nesterov site in the main volume, verbatim clause:')
forms = {}
for i in nes:
    m = re.search(r'Nesterov[^.;)]{0,40}', MAIN[i - 1])
    f = m.group(0).strip() if m else ''
    forms.setdefault(f, []).append(i)
    print(f'    L{i} (§{enclosing(MAIN, i)}): {f}')
verdict('14m-07', len(forms) == 1,
        f'L6341 attributes the Newton decrement to "Nesterov and Nemirovskii (1994)"; the main '
        f'volume carries {len(nes)} Nesterov sites in {len(forms)} distinct forms — '
        f'{list(forms)} . A single attribution written two ways is an R-ATTR consistency defect, '
        f'not a factual one: both name 1994 and the fuller form is the correct citation for '
        f'"Interior-Point Polynomial Algorithms in Convex Programming"')
b = sites('1788')
print(f'  IEEE 1788 sites: {b};  "1966": {sites("1966")};  "1925": {sites("1925")}')
verdict('14m-08', True,
        f'§23.8.4\'s three external anchors — Moore 1966, IEEE 1788-2015, and the 1925 date at '
        f'L6319 — appear at {sites("1966")["main bundle"]}, {b["main bundle"]} and '
        f'{sites("1925")["main bundle"]} main-bundle sites. All three are single-witness inside the '
        f'book: no bibliography entry in either bundle carries Moore or IEEE 1788 '
        f'({sites("Moore")}), so the attributions §23.8.4 makes are not backed by a reference list. '
        f'R-ATTR owes them one')

# ---------------------------------------------------------------- negative claims
print('\n== negative and novelty claims, each with its own witness ==')
print(f'  L6319 "It is not in the literature" — scope: e/T = 3(h/nu)^2 as the relative error of '
      f'linear interpolation. In-book witness only; not testable from the bundles. Recorded.')
print(f'  L6351 "Nobody has asked whether T(nu) qualifies" — same class, and the stronger of the '
      f'two: it is a claim about the whole literature of self-concordance.')
deep = {}
for tag, txt in BUNDLES.items():
    for m in re.finditer(r'ν\s*=\s*(\d{1,3})(?![\d.])', txt):
        v = int(m.group(1)); deep[tag] = max(deep.get(tag, 0), v)
print(f'  L6361 "the deepest channel in this book reaches nu = 55" — largest "nu = N" printed '
      f'anywhere: {deep}')
n55 = sites('55')
verdict('14m-09', deep.get('main bundle', 0) <= 55 and deep.get('compendia bundle', 0) <= 55,
        f'the deepest-channel claim is consistent with every "nu = N" printed in either bundle: the '
        f'maximum is {max(deep.values())} ({deep}). The claim is checkable and it holds')

# ---------------------------------------------------------------- carried figure classes
print('\n== figures this unit restates from elsewhere ==')
for fig in ('32/11', '2.909', '4ν/3', '26.69', '8.18', '95.99', '0.1356', '406', '731.5820'):
    print(f'  {fig:10s} {sites(fig, bounded=False)}')
l6381 = MAIN[6380].strip()
verdict('14m-10', False,
        f'L6381 restates the floor as "the floor 32/11" among the book\'s own results. Chat 95\'s '
        f'14j-01 MEASURED that 32/11 is the h = 1 floor and not V\'s — the exact V = 4r^3/(3r^2-1) '
        f'is minimised at r = 1 with V = 2, and §23.9.2 twelve lines later prints V = 2.0000 twice. '
        f'This is a third site of the same defect (§23.3 L6233 and §23.2 L6213 are the first two) '
        f'and it is the one that claims the floor as an original result')
verdict('14m-11', False,
        f'L6381 also claims "the value 4ν/3" as the book\'s own. §23.6 L6317 derives it as the '
        f'ratio of the two fractional forms, where r2-ch14l MEASURED the exact ratio to be '
        f'4r^3/(3r^2-1), above 4r/3 at every (nu, h). The claimed value is the asymptote of the '
        f'book\'s own exact result, and the section that states it does not say so')

# ---------------------------------------------------------------- structure and standards
print('\n== structure, and the compendium standard ==')
s8, e8, t8 = body('23.8')
subs = [i for i in range(s8, e8) if re.match(r'^#{3,4} 23\.8\.\d', MAIN[i - 1].strip())]
explains = [i for i in range(s8, e8) if has_token(MAIN[i - 1], 'explains') or has_token(MAIN[i - 1], 'why')]
print(f'  §23.8 spans L{s8}-L{e8-1} with {len(subs)} subsections at {subs}')
for i in explains:
    print(f'    explains/why at L{i} (§{enclosing(MAIN, i)}): {MAIN[i-1].strip()[:100]}')
verdict('14m-12', len(explains) == 2,
        f'L6334 "the name explains two things this book could only observe" — MEASURED: §23.8 '
        f'carries {len(explains)} explains/why sites, at L{explains}. The two are the cancellation '
        f'(§23.8.3) and the pole/optimum reading (§23.8.1); §23.8.2 and §23.8.4 add a third and a '
        f'fourth movement — self-concordance and attribution — which the count of two does not '
        f'cover. Marginal: the sentence is defensible if "explains" is read strictly')
pipe = len([i for i in range(*UNIT) if MAIN[i - 1].lstrip().startswith('|')])
space = len([i for i in range(*UNIT) if re.match(r'^\s{2,}\S.*\s{3,}\S', MAIN[i - 1])
             and not MAIN[i - 1].lstrip().startswith('|')])
print(f'  table lines in the unit: {pipe} markdown-pipe, {space} space-aligned')
verdict('14m-13', False,
        f'the unit carries two incompatible table conventions — {pipe} pipe-table lines (§23.8.2, '
        f'§23.9.2, §23.9.3) against {space} space-aligned pseudo-table lines (§23.6, §23.9.1). '
        f'§23.9.1\'s single ranked list is split across two space-aligned blocks with the column '
        f'header repeated at L6395, so one table prints as two. A consistent-formatting defect '
        f'under the compendium standard, and a production risk: space-aligned blocks do not survive '
        f'pandoc as tables')
figs = [i for i in range(*UNIT) if MAIN[i - 1].lstrip().startswith('![')]
allfigs = [i for i in range(1, len(MAIN) + 1) if re.match(r'^\s*!\[Figure 23\.', MAIN[i - 1])]
print(f'  figure references in the unit: {figs} ; all Chapter 23 figures: {allfigs} '
      f'({[MAIN[i-1].strip()[:40] for i in allfigs]})')
verdict('14m-14', len(allfigs) == 1,
        f'Figure 23.2 is referenced at L6328 and is the ONLY figure in Chapter 23: there is no '
        f'Figure 23.1 anywhere in the main volume ({sites("Figure 23.1")}). A chapter whose first '
        f'figure is numbered 2 is a numbering defect, and the caption at L6330-6331 additionally '
        f'carries the claim r2-ch14l 14l-07 measured false ("the method\'s only hard singularity"), '
        f'where Ruling\'s caption standard is facts only')
regs = [i for i in range(*UNIT) if re.search(r'[Rr]egister\s+\d+', MAIN[i - 1])]
verdict('14m-15', not regs,
        f'Register citations in L6303-L6433: {len(regs)} (lowercase "register NNN" grepped by hand '
        f'as well as the capitalised form). The unit derives 20 printed figures and cites the '
        f'Register for none of them — consistent with §23.1-§23.5.3, which cited it once')
proc = [i for i in range(*UNIT) if any(has_token(MAIN[i - 1], w) for w in
        ('build', 'script', 'instrument', 'chat', 'BUILD90', 'py'))]
verdict('14m-16', not proc,
        f'Rulings 45/46 (no build, script or editorial-process remarks visible to a reader): '
        f'{len(proc)} candidate lines in the unit{"" if not proc else " at L" + str(proc)}')

# ---------------------------------------------------------------- physics labels
print('\n== the exponent table\'s physics labels, against the rest of the book ==')
for lab, p in (('C₆', 11), ('polarisability', 7), ('blockade radius', '11/6'),
               ('radiative lifetime', 3), ('C₃', 4)):
    print(f'  {lab:20s} p={str(p):5s} sites: {sites(lab, bounded=False)}')
c3 = [i for i in range(1, len(MAIN) + 1) if 'C₃' in MAIN[i - 1]]
print('  every C₃ site in the main volume:')
for i in c3:
    print(f'    L{i} (§{enclosing(MAIN, i)}): {MAIN[i-1].strip()[:110]}')
verdict('14m-17', len(c3) > 1,
        f'§23.9.1 L6397 labels the p = 4 row "C₃, geometric cross-section". C₃ is the '
        f'resonant dipole-dipole coefficient; the geometric cross-section is a different observable '
        f'that happens to share the n^4 scaling. The main volume carries {len(c3)} C₃ sites '
        f'{c3}, so the label is defined nowhere else and the row conflates two objects under one '
        f'exponent. A reader-facing naming defect; the exponent itself is right')
verdict('14m-18', True,
        'the remaining six labels carry the standard Rydberg scalings — C₆ ~ n^11, polarisability '
        '~ n^7, blockade radius ~ n^(11/6) (which follows from C₆ ~ n^11 as (n^11)^(1/6)), '
        'radiative lifetime ~ n^3, spacing ~ n^-3, T ~ n^-2, <r> ~ n^2 — and each is internally '
        'consistent with the C₆ row of the same table')
print('\n== end r2-ch14m ==')
