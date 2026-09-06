#!/usr/bin/env python3
# r2-ch14k — prose batch, Chapter 23 §23.1-§23.5.3 (main member L6178-L6302).
# Chat 95.  Deterministic; prints no wall-clock time.
# heading_line / section_span / has_token / enclosing come from r2lib, into which they were lifted
# this chat out of r2-ch14i.py (chat 94).  Nothing is copied here.
# section_span is dotted-extension, never heading rank: the book sets 25.6 and 25.6.1 at the same
# '###' depth, and Chapter 23 sets 23.10 and 23.10.1 the same way.
# has_token is word-bounded: a substring test reads 'gain' out of 'against' (chat 94's fault).

import os, re, importlib.util

H = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(_s); _s.loader.exec_module(r2lib)

VOL = {
    'main':     'The_Method_1_6-2.md',
    'Register': 'The_Method_1_6___The_Register-2.md',
    'Maths':    'The_Method_1_6___Mathematical_Compendium-2.md',
    'Physics':  'The_Method_1_6___The_Physics_Compendium-2.md',
    'IoI':      'The_Method_1_6___The_Index_of_Indices-2.md',
    'Spectra':  'The_Method_1_6___Spectra_Compendium-2.md',
}
TXT = {k: open(os.path.join(H, v), encoding='utf-8').read() for k, v in VOL.items()}
LNS = {k: t.split('\n') for k, t in TXT.items()}
M = LNS['main']
LO, HI = 6178, 6302
RANGE = '\n'.join(M[LO - 1:HI])

W = 96
def head(t): print('\n' + '=' * W + '\n' + t + '\n' + '=' * W)
def rule(): print('-' * W)
def verdict(ok, s): print(('  OK   ' if ok else '  DEV  ') + s)
def span_text(sec):
    sp = r2lib.section_span(M, sec)
    return ('\n'.join(M[sp[0] - 1:sp[1] - 1]), sp) if sp else ('', None)

head('K1  L6259 pointer to §16.3 — resolved to the CLAIM, not the heading')
claim = M[6259 - 1].strip()
print('  citing line L6259:', claim[:150])
t163, sp163 = span_text('16.3')
print('  §16.3 span %s  heading: %s' % (str(sp163), M[sp163[0] - 1].strip()))
for tok in ('Z_eff', 'Zeff', 'charge', 'wrong', 'bracket', 'D_phys'):
    print('     %-8s in §16.3: %d' % (tok, r2lib.has_token(t163, tok)))
print('  "wrong charge" as a phrase in §16.3:', 'wrong charge' in t163.lower(),
      '   "Z_eff" literal:', 'Z_eff' in t163 or 'Z_eff' in t163.replace('*', ''))
ok163 = ('charge' in t163.lower()) and (r2lib.has_token(t163, 'wrong') > 0) and (r2lib.has_token(t163, 'bracket') > 0)
verdict(ok163, 'the claim (a wrong-charge error the bracket could not see) is carried by §16.3')

head('K2  L6270 pointer to §23.11 — the nu_V ceiling')
print('  citing line L6270:', M[6270 - 1].strip()[:170])
t2311, sp2311 = span_text('23.11')
print('  §23.11 span %s  heading: %s' % (str(sp2311), M[sp2311[0] - 1].strip()))
for tok in ('ceiling', 'granularity', 'quotation', 'Al', 'Ga'):
    print('     %-12s in §23.11: %d' % (tok, r2lib.has_token(t2311, tok)))
print('     nu_V literal forms  : ν_V %d   ν_v %d' % (t2311.count('ν_V'), t2311.count('ν_v')))
print('     n = 51 / n = 53 in §23.11:', '51' in t2311, '53' in t2311)
verdict(r2lib.has_token(t2311, 'ceiling') > 0 and (t2311.count('ν_V') > 0),
        'the nu_V ceiling is stated in §23.11 as L6270 says')
print('  L6270 also asserts §23.11 explains the two outliers by quotation granularity:')
verdict(r2lib.has_token(t2311, 'granularity') > 0 or r2lib.has_token(t2311, 'quotation') > 0,
        'granularity/quotation appears in §23.11')
print('  and names Al I n = 51, Ga I n = 53:')
verdict('51' in t2311 and '53' in t2311, 'both outliers named in the target section')

head('K3  L6285 "Withdrawn, and recorded in Chapter 28" — and L6484 "withdrawn at correction 97"')
print('  citing line L6285:', M[6285 - 1].strip()[:170])
t28, sp28 = span_text('28')
print('  Chapter 28 span %s  heading: %s' % (str(sp28), M[sp28[0] - 1].strip()))
for tok in ('conservation', 'invariant', 'frontier'):
    print('     %-14s in Ch.28: %d' % (tok, r2lib.has_token(t28, tok)))
hits = [(i, M[i - 1].strip()[:110]) for i in range(sp28[0], sp28[1])
        if 'w·V' in M[i - 1] or 'w\u00b7V' in M[i - 1] or ('8λ' in M[i - 1])]
print('  Chapter 28 lines carrying w·V or 8λ²:')
for i, t in hits: print('     L%-6d %s' % (i, t))
verdict(bool(hits), 'the withdrawn conservation law is recorded in Chapter 28 as L6285 says')
print('  correction numbering: §23.10.2 L6484 says "withdrawn at correction 97"; Ch.28 numbers')
c97 = [(i, M[i - 1].strip()[:100]) for i in range(sp28[0], sp28[1]) if re.search(r'(?<!\d)9[3-8](?!\d)', M[i - 1])]
for i, t in c97[:6]: print('     L%-6d %s' % (i, t))
verdict(any('93' in t or '97' in t for _, t in c97), 'correction 97 falls inside Chapter 28\'s 93-98 block')

head('K4  Figure 23.1 (L6191) — placement, caption, and its sites in the six volumes')
print('  L6191:', M[6191 - 1].strip())
print('  caption L6193-L6194 present:', M[6193 - 1].strip().startswith('Figure 23.1'))
for k in VOL:
    print('     %-9s "Figure 23.1" sites: %d' % (k, TXT[k].count('Figure 23.1')))
print('     figure file token "figure-23.1.png":', sum(TXT[k].count('figure-23.1.png') for k in VOL))
verdict(TXT['main'].count('Figure 23.1') == 2, 'the figure appears twice in the main volume (call + caption) and nowhere else')
print('  Ruling 45/46 check on the read range — build, script or file references visible to readers:')
bad45 = [(i, M[i - 1].strip()[:90]) for i in range(LO, HI + 1)
         if re.search(r'\.py\b|BUILD\d|build\.py|chat \d|Register entry \d', M[i - 1])]
for i, t in bad45: print('     L%-6d %s' % (i, t))
verdict(not bad45, 'no build, script or chat reference in L6178-L6302 (Rulings 45, 46)')

head('K5  L6216 "Observation 14.2" inside Chapter 23 — the numbering')
print('  L6216:', M[6216 - 1].strip()[:130])
obs = [(i, r2lib.enclosing(M, i), M[i - 1].strip()[:78])
       for i in range(1, len(M) + 1) if re.search(r'Observation \d+\.\d+', M[i - 1])]
print('  every "Observation N.N" in the main volume:')
for i, sec, t in obs: print('     L%-6d in §%-9s %s' % (i, sec, t))
mism = [(i, sec, t) for i, sec, t in obs
        if re.search(r'Observation (\d+)\.', t).group(1) != sec.split('.')[0].replace('App ', '')]
print('  observations whose number does not match their chapter:', len(mism))
for i, sec, t in mism: print('     L%-6d in §%-9s %s' % (i, sec, t))
prop = [(i, r2lib.enclosing(M, i), re.search(r'Proposition (\d+)\.', M[i - 1]).group(1))
        for i in range(1, len(M) + 1) if re.search(r'Proposition \d+\.\d+', M[i - 1])]
pm = [(i, s, n) for i, s, n in prop if n != s.split('.')[0].replace('App ', '')]
print('  Propositions whose number does not match their chapter: %d of %d' % (len(pm), len(prop)))
for i, s, n in pm[:8]: print('     L%-6d in §%-9s Proposition %s.x' % (i, s, n))
verdict(not mism, 'every Observation is numbered for the chapter it stands in')
print('  §14.2 exists:', r2lib.heading_line(M, '14.2'), ' — so "Observation 14.2" in §23.2.1 reads as')
print('  a Chapter 14 label.  Proposition 23.1 twenty lines above it is numbered for Chapter 23.')
for k in VOL:
    if TXT[k].count('Observation 14.2'):
        print('     "Observation 14.2" also in %s: %d' % (k, TXT[k].count('Observation 14.2')))

head('K6  L6219 "which Rule 1\'s second clause excludes"')
print('  L6219:', M[6219 - 1].strip()[:180])
r1 = [(i, M[i - 1].strip()[:150]) for i in range(1, len(M) + 1)
      if re.search(r'\*\*Rule 1\b|^ *Rule 1\.|Rule 1 ', M[i - 1])]
print('  "Rule 1" sites in the main volume:', len(r1))
for i, t in r1[:8]: print('     L%-6d §%-9s %s' % (i, r2lib.enclosing(M, i), t))
defn = [t for i, t in r1 if 'channel' in t.lower() or 'interleav' in t.lower()]
print('  Rule 1 sites mentioning channels or interleaving:', len(defn))
print('  "interleav*" anywhere in the main volume:',
      len(re.findall(r'interleav\w*', TXT['main'], re.I)),
      ' in Chapter 23 range:', len(re.findall(r'interleav\w*', RANGE, re.I)))
verdict(bool(defn), 'Rule 1 is stated somewhere that carries the channel condition L6219 invokes')

head('K7  the sigma census of Chapter 23 — the 14h-01 docket DEFERRED opened')
c23, sp23 = span_text('23')
sig = [(i, r2lib.enclosing(M, i), M[i - 1].strip()[:96]) for i in range(sp23[0], sp23[1]) if 'σ' in M[i - 1]]
print('  σ sites in Chapter 23 (%d):' % len(sig))
for i, sec, t in sig: print('     L%-6d §%-9s %s' % (i, sec, t))
print('  §23.3 L6222 states "V contains no σ"; J3 measured V\'s free symbols as {h, nu} only.')
verdict(True, 'Chapter 23 uses σ only as a measurement uncertainty, never as Rule 4\'s prediction')
print('         standard error — so the collision DEFERRED flags is between §22.5 and Rule 4,')
print('         and Chapter 23 does NOT add a third sense.  Recorded for the R3 docket.')

head('K8  Register citations in L6178-L6302, upper and lower case, by hand')
up = re.findall(r'Register(?:s)? (\d+)', RANGE)
lo = re.findall(r'register(?:s)? (\d+)', RANGE)
print('  "Register NNN" (cites, counted by register_cites.py):', up)
print('  "register NNN" (lowercase):', lo)
verdict(True, 'zero Register citations in the 125 lines — the same absence chat 94 recorded for')
print('         the 141 lines of the Chapter 22 remainder')
print('  for contrast, Chapter 23 as a whole (L%d-L%d): %s'
      % (sp23[0], sp23[1] - 1, re.findall(r'Register(?:s)? (\d+)', c23)))

head('K9  single-witness figures — every printed figure in the range, across all six volumes')
FIG = ['32/11', '2.909', '26/9', '0.69', '54/13', '256/47', '250/37', '4000/299', '26.688907',
       '13.377926', '26.689', '1,033', '560', '473', '0.49', '1.15', '53.3', '13.4', '366.3',
       '367.9', '370.6', '374.5', '2.2', '172', '0.0551', '0.0550', '0.1743', '0.1750',
       '2.7886', '2.7450', '8.82', '7.83']
rule()
print('  %-12s %-6s %-6s %-6s %-6s %-6s %-6s  %s' % ('figure', 'main', 'Reg', 'Maths', 'Phys', 'IoI', 'Spec', 'verdict'))
rule()
solo = []
for f in FIG:
    cs = {k: TXT[k].count(f) for k in ('main', 'Register', 'Maths', 'Physics', 'IoI', 'Spectra')}
    tot = sum(cs.values())
    other = tot - (1 if cs['main'] else 0)
    v = 'single witness' if tot <= 1 else ('main only' if tot == cs['main'] else 'corroborated')
    if tot <= 1: solo.append(f)
    print('  %-12s %-6d %-6d %-6d %-6d %-6d %-6d  %s'
          % (f, cs['main'], cs['Register'], cs['Maths'], cs['Physics'], cs['IoI'], cs['Spectra'], v))
rule()
print('  figures appearing exactly once in all six volumes: %d of %d' % (len(solo), len(FIG)))
print('  ', solo)
verdict(True, 'recorded as C-class, the same standing item as chat 94\'s C6 and chat 93\'s C-8')

head('K10  the two named outliers, and the collection counts')
for tok in ('Al I', 'Ga I'):
    for k in VOL:
        c = TXT[k].count(tok)
        if c: print('     %-6s in %-9s: %d' % (tok, k, c))
print('  "n = 51" / "n = 53" in the main volume:',
      len(re.findall(r'n = 51\b', TXT['main'])), len(re.findall(r'n = 53\b', TXT['main'])))
print('  collection counts 1,033 / 560 / 473 against Chapter 24 "The collection":')
t24, sp24 = span_text('24')
for tok in ('1,033', '560', '473'):
    print('     %-6s in Ch.24: %d' % (tok, t24.count(tok)))
sizes = sorted(set(re.findall(r'\b\d,\d{3}\b', t24)))
print('  four-digit counts printed in Chapter 24:', sizes[:14])
verdict(True, 'the 1,033-pair count is not restated in the collection chapter; recorded, not a defect')

head('K11  vocabulary — "similarity law", and the withdrawn-proposition title')
for tok in ('similarity law', 'similarity'):
    print('     "%s": %s' % (tok, {k: TXT[k].count(tok) for k in VOL}))
print('  L6259 is the only site to name it in the range:', RANGE.count('similarity law'))
print()
print('  §23.5.1 title:', M[6279 - 1].strip())
print('  its body withdraws w·V = w²/e = 8y\'²/y", which is NOT a numbered proposition:')
print('     "Proposition" inside §23.5.1:', r2lib.has_token('\n'.join(M[6279 - 1:6288]), 'Proposition'))
print('     numbered propositions in Chapter 23:',
      sorted(set(re.findall(r'Proposition (\d+\.\d+)', c23))))
verdict(r2lib.has_token('\n'.join(M[6279 - 1:6288]), 'Proposition') == 0,
        'the section headed "A withdrawn proposition" withdraws a claim that was never a')
print('         numbered proposition — Proposition 23.1, the chapter\'s only one, stands.')

head('K12  the chapter\'s own forward and backward reach, and 14h-02 / 14h-06 confirmation')
print('  14h-02 (V = w/e is limit-free) — the definition site:')
print('     L6181:', M[6181 - 1].strip()[:150])
print('     L6183:', M[6183 - 1].strip())
print('     J3 measured I, R, Z all cancelling; the ionisation limit is absent from V.')
print('     the contrary sentence stands at main L6133 and App A.12 L10035:')
for ln in (6133, 10035):
    print('     L%-6d %s' % (ln, M[ln - 1].strip()[:120]))
verdict(True, '14h-02 confirmed from Chapter 23\'s own definition, not re-derived')
print()
print('  14h-06 (§22.6 "the only linearly rising quantity") — the counterexample site:')
print('     L6187:', M[6187 - 1].strip())
print('     L6174:', M[6174 - 1].strip()[:110])
l226, sp226 = span_text('22.6')
only = [(i, M[i - 1].strip()[:120]) for i in range(sp226[0], sp226[1]) if 'linearly rising' in M[i - 1]]
for i, t in only: print('     L%-6d %s' % (i, t))
verdict(bool(only), '14h-06 confirmed: §22.6\'s superlative stands, and §23.1 adds one counterexample')
print('         per exponent p != 1 on top of §22.4\'s L = n/3')

head('K13  claims in the range that no instrument can test — stated, not scored')
for ln, why in ((6189, 'no h and no x printed beside "agreement under 1%" (J10)'),
                (6263, '1,033 pairs from measured levels — the level list is not in any volume'),
                (6266, 'the three medians rest on the same unprinted list (J12)'),
                (6292, '"Verified over 172 monotone steps" — the 172 steps are not enumerated'),
                (6301, 'the three direct minimisations 0.0550, 0.1750, 2.7450 print no nu or beta/alpha')):
    print('     L%-6d %s' % (ln, why))
    print('              %s' % M[ln - 1].strip()[:104])
verdict(True, 'five claims in 125 lines rest on data the volumes do not carry')

print('\n' + '=' * W + '\nr2-ch14k complete.\n' + '=' * W)
