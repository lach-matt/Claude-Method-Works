#!/usr/bin/env python3
# r2-ch15m — chat 109, prose batch for main L7644–L7720 (§28.7.4 … §28.7.9).
# Pointers under BOTH resolvers, with the claim located when the pointer fails;
# Ruling 45 / Ruling 46 sweeps; the withdrawal-against-a-rewritten-section sweep;
# single-witness tests on the two-line join as well as the raw line.
import os, re, importlib.util

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
heading_line, section_span, has_token, enclosing = r2lib.heading_line, r2lib.section_span, r2lib.has_token, r2lib.enclosing

VOL = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
       'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
       'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
       'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
       'sp': 'The_Method_1_6___Spectra_Compendium-2.md'}
M = {t: open(os.path.join(H, f), encoding='utf-8').read().split('\n') for t, f in VOL.items()}
PP = open('/home/claude/PP_The_Method_1_6.md', encoding='utf-8').read().split('\n')
U0, U1 = 7644, 7720
UNIT = M['main'][U0 - 1:U1]
P = print

def body_range(L, sec):                       # owed to r2lib (heading -> next heading of ANY rank)
    ln = heading_line(L, sec)
    if ln is None: return None
    for j in range(ln, len(L)):
        if re.match(r'^#{1,6}\s', L[j]): return (ln, j + 1)
    return (ln, len(L) + 1)

def phrase_sites(L, phrase):                  # owed to r2lib (two-line join)
    p = re.sub(r'\s+', ' ', phrase.lower()); out = []
    for i in range(1, len(L) + 1):
        if p in re.sub(r'\s+', ' ', L[i - 1].lower()): out.append((i, 'line'))
        elif i < len(L) and p in re.sub(r'\s+', ' ', (L[i - 1] + ' ' + L[i]).lower()): out.append((i, 'join'))
    return out

def sixvol(phrase):
    return {t: phrase_sites(M[t], phrase) for t in VOL}

P('== A. every §-pointer in the unit, under BOTH resolvers, then the claim ==')
POINT = {}
for off, l in enumerate(UNIT):
    for m in re.finditer(r'§\s*(\d+(?:\.\d+)*)', l):
        POINT.setdefault(m.group(1), []).append(U0 + off)
for sec in sorted(POINT, key=lambda s: [int(x) for x in s.split('.')]):
    br = body_range(M['main'], sec); sp = section_span(M['main'], sec)
    P('  §%-8s cited at %s  body_range %s  section_span %s' % (sec, POINT[sec], br, sp))

P('\n== B. the claim each pointer is made to carry ==')
CLAIMS = [
 ('30.3',   '28.7.4 heading: the session closed it',            ['closed', 'session']),
 ('32.2',   '28.7.4 heading: the session closed it',            ['closed', 'session']),
 ('24.4',   'items 150-151: two cross-references for a theorem', ['cross-referenc', 'wildcard', 'he ii']),
 ('18.4',   'items 150-151: the theorem they point to',          ['theorem']),
 ('2.14',   'state the number before the interpretation',        ['before the interpretation', 'state the number']),
 ('3',      "§3's CONSISTENCY audit and its exhaustiveness clause", ['consistency', 'exhaustive']),
 ('2.19.1', 'states the newest-first inconsistency and why it is left', ['newest', 'order', 'inconsist']),
 ('4',      'the ten mechanisms, each stated in full',           ['ten mechanisms']),
 ('4.6',    'a test that could not fail',                        ['a test that could not fail']),
 ('32.6.1', 'one of each level in a single paragraph; forty-three cells', ['forty-three', '43', 'stale']),
 ('28.7.4', 'its own form: mechanism is the finding, instances a count', ['mechanism']),
 ('28.7.6', "three entries, in the collaborator's hand",         ['three', 'two']),
]
for sec, what, toks in CLAIMS:
    br, sp = body_range(M['main'], sec), section_span(M['main'], sec)
    verdict = []
    for name, rng in (('body_range', br), ('section_span', sp)):
        if rng is None: verdict.append((name, 'NO HEADING', [])); continue
        seg = re.sub(r'\s+', ' ', '\n'.join(M['main'][rng[0]:rng[1] - 1]).lower())
        verdict.append((name, [t for t in toks if t in seg], rng[1] - rng[0]))
    P('  §%-8s %-52s' % (sec, what))
    for name, hits, n in verdict: P('       %-13s %-4s tokens present: %s' % (name, n, hits))
    if not any(v[1] for v in verdict):
        P('       ABSENT under both resolvers -> locating the claim elsewhere:')
        for t in toks[:2]:
            for tag in VOL:
                s = phrase_sites(M[tag], t)
                if s: P('         %-5s %-28r %s' % (tag, t, s[:4]))

P('\n== C. §4.x pointers are TABLE ROWS, not headings — the resolver cannot see them ==')
s4 = section_span(M['main'], '4')
rows = {int(m.group(1)): i for i in range(s4[0], s4[1])
        for m in [re.match(r'^\s*4\.(\d+)\s+\*\*', M['main'][i - 1])] if m}
P('  §4 rows present: %s' % sorted(rows))
for n in sorted({int(s.split('.')[1]) for s in POINT if s.startswith('4.') and s.count('.') == 1}):
    P('  §4.%-3d cited in the unit -> heading_line %s ; table row L%s'
      % (n, heading_line(M['main'], '4.%d' % n), rows.get(n)))

P('\n== D. Ruling 45 (build / editorial-process remarks) and Ruling 46 (build numbers, files, scripts) ==')
R45 = ['retained in the compendium', 'the final session', 'this session', 'in one session', 'one session',
       "collaborator's hand", 'the person operating it', 'i hardcoded', 'for an hour', 'in one hour',
       'was recorded as evidence', 'not written down', 'the session that closed']
R46 = ['build 9', 'at this build', 'this build', 'whose file', 'the file', '.py', '.md', 'script',
       'build 1', 'bundle']
for lab, toks in (('R45', R45), ('R46', R46)):
    P('  -- %s --' % lab)
    for t in toks:
        s = [i for i, _ in phrase_sites(UNIT, t)]
        if s: P('     %-28r unit lines %s' % (t, [U0 + i - 1 for i in s]))

P('\n== E. count-word and N-of-M sentences against the body they count ==')
SENT = ['thirty-one of the forty', '40 of the entries above', 'two entries are about the audits',
        "§28.7.6's three", 'wrong by a factor of twenty-eight', 'they were twenty-eight',
        'printed individually', 'all printed', 'given newest first']
for s in SENT:
    hits = sixvol(s)
    tot = sum(len(v) for v in hits.values())
    P('  %-38r sites in six volumes: %d  %s' % (s, tot, {k: [x[0] for x in v] for k, v in hits.items() if v}))

P('\n== F. withdrawal items describing another section\'s state, re-read against that section ==')
TESTS = [
 ('32.6.1', 'a stale value, a sum that never closed, an inference from a ratio that has since inverted',
  ['stale', 'sum', 'ratio', 'invert', 'forty-three']),
 ('2.19.1', 'the register is maintained newest-first since 205 and §2.19.1 says why it is left',
  ['newest', '205', 'left']),
 ('2.14', 'state the number before the interpretation', ['number', 'interpretation']),
 ('3', 'the CONSISTENCY audit and its exhaustiveness clause', ['consistency', 'exhaustive']),
]
for sec, claim, toks in TESTS:
    sp = section_span(M['main'], sec)
    if sp is None: P('  §%-8s NO HEADING in main' % sec); continue
    seg = re.sub(r'\s+', ' ', '\n'.join(M['main'][sp[0]:sp[1] - 1]).lower())
    P('  §%-8s (%d lines) claim: %s' % (sec, sp[1] - sp[0], claim))
    P('       tokens found: %s ; missing: %s'
      % ([t for t in toks if t in seg], [t for t in toks if t not in seg]))

P('\n== G. the three census rows in range, tested as claims ==')
CEN = {1166: ('L7700', 'a conclusion written before the output · a reading the source never made'),
       1167: ('L7703', 'a sum that never closed'),
       1168: ('L7711', 'already recorded and never connected to either')}
for cid, (ln, txt) in CEN.items():
    P('  %d %s %r' % (cid, ln, txt))
P('  1166/1167 sit inside the level table and the §32.6.1 note: is the flagged token a LABEL?')
for t in ['a reading the source never made', 'a sum that never closed']:
    P('     %-38r sites: %s' % (t, {k: [x[0] for x in v] for k, v in sixvol(t).items() if v}))
P('  1168: does any volume connect §4.6 to §4.5/§4.10 as the third of the pair?')
for t in ['a derivation written before the output', 'the same act at two depths', 'at two depths']:
    P('     %-38r sites: %s' % (t, {k: [x[0] for x in v] for k, v in sixvol(t).items() if v}))

P('\n== H. formatting sweeps: openings, terminal punctuation, long-line recurrence, breaks ==')
opens = []
for sec in ['28.7.4', '28.7.5', '28.7.6', '28.7.7', '28.7.8', '28.7.9']:
    br = body_range(M['main'], sec)
    first = next((l for l in M['main'][br[0]:br[1] - 1] if l.strip()), '')
    if first:
        w = re.sub(r'^[\s*_>]+', '', first)[:1]
        opens.append((sec, w, w.islower()))
P('  first body character per section: %s' % opens)
blocks = [i for i in range(U0, U1 + 1) if re.match(r'^\s*\d+(\s*[–-]\s*\d+)?\.\s', M['main'][i - 1])]
for b in blocks:
    j = b
    while j < U1 and M['main'][j].strip(): j += 1
    last = M['main'][j - 1].rstrip()
    P('  item block at L%d ends L%d %r terminal-punctuated %s' % (b, j, last[-28:], last.endswith(('.', '!', '?', '—'))))
longs = [(i, re.sub(r'\s+', ' ', M['main'][i - 1]).strip()) for i in range(U0, U1 + 1)
         if len(M['main'][i - 1].strip()) >= 60]
rec = 0
for i, t in longs:
    for tag in VOL:
        for j, k in phrase_sites(M[tag], t):
            if not (tag == 'main' and j == i): rec += 1; P('  RECURS: main L%d also at %s L%d (%s)' % (i, tag, j, k))
P('  long lines swept: %d ; recurrences found: %d' % (len(longs), rec))
brk = [i for i in range(U0, U1) if M['main'][i - 1].strip() and not M['main'][i - 1].rstrip().endswith(('.', ':', '—', '**', '*', '!', '?'))
       and not M['main'][i].strip() and not re.match(r'^#', M['main'][i - 1])]
P('  paragraph-final lines ending unpunctuated (candidate mid-sentence breaks): %s' % brk)

P('\n== I. single-witness test: claims with one site in six volumes ==')
ONE = ['narration outrunning verification', 'a wildcard target', 'the direction the register has been maintained',
       'the mechanism is the finding', 'it keeps recording an index as a scalar',
       'ρ collapsed route into a number', 'detector artifact', 'claimed completion',
       'an interpretation written before the number above it was read']
for t in ONE:
    h = {k: [x[0] for x in v] for k, v in sixvol(t).items() if v}
    P('  %-52r sites %d %s' % (t, sum(len(v) for v in h.values()), h))

P('\n== J. PP witness for the unit\'s prose (which sentences post-date the input) ==')
for t in ['narration outrunning verification', 'wrong by a factor of twenty-eight',
          'the complete record', 'at this build the main volume cites', 'registers 571']:
    P('  %-42r main %s | PP %s'
      % (t, [x[0] for x in phrase_sites(M['main'], t)][:4], [x[0] for x in phrase_sites(PP, t)][:4]))
