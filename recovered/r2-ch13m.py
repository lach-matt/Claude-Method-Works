# r2-ch13m.py — Phase R2, chat 83. PROSE batch for the section read of Chapter 15 (main L4270-L4331):
# pointers resolved to the claim, attributions, figures restated elsewhere, self-description, captions.
# Deterministic; reads members only. Imports r2lib by path (chat 74 ruling 2).
import importlib.util, os, re, collections
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md', 'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md', 'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
L = {k: r2lib.read_member(v).split('\n') for k, v in F.items()}
M = L['main']; A, B = 4270, 4331
P = print
def body(a, b): return '\n'.join(M[a - 1:b])
def sec(name):
    """line range of a ### / ## heading, to the next heading of the same or higher level"""
    for i, l in enumerate(M, 1):
        m = re.match(r'^(#{2,4}) ' + re.escape(name) + r'(\s|$)', l)
        if m:
            lvl = len(m.group(1))
            for j in range(i + 1, len(M) + 1):
                m2 = re.match(r'^(#{2,4}) ', M[j - 1])
                if m2 and len(m2.group(1)) <= lvl: return i, j - 1
            return i, len(M)
    return None

P('=== 1. every pointer in L%d-L%d resolved to the CLAIM, not the heading ===' % (A, B))
CH = [('§2.23', 4280, '2.23', 'the envelopes are recoverable, so an expression always exists'),
      ('§18.4', 4305, '18.4', 'per-axis total orders are necessary and not sufficient above d = 2'),
      ('Ch. 30', 4327, '30.', 'for a graph with cycles S2 is open, and what is known')]
for tag, at, head, claim in CH:
    r = sec(head)
    P('%-7s cited at L%d -> %s L%d-%d  "%s"' % (tag, at, head, r[0], r[1], M[r[0] - 1][:70]))
    P('        the claim wanted: %s' % claim)
P('')
P('--- §2.23 (L1148-1156): does it carry the reciprocal? ---')
for i in range(1148, 1157):
    if '15.2' in M[i - 1] or 'envelope' in M[i - 1]: P('  L%d %s' % (i, M[i - 1].strip()[:150]))
P('--- §18.4 + §18.4.1: does either state §15.3\'s claim about per-axis ORDERS? ---')
r4 = sec('18.4'); r41 = sec('18.4.1')
txt = body(r4[0], r41[1] if r41 else r4[1])
for w in ['may precede', 'total order', 'order on', 'relabel', 'recover', 'axis', 'per-axis', 'projection', 'closure']:
    n = len(re.findall(w, txt, re.I)); P('   %-12s occurrences in §18.4+§18.4.1: %d' % (w, n))
P('   §18.4 states: %s' % M[4982].strip()[:120])
P('   §15.3 attributes to it: %s' % M[4303].strip()[:150])

P('')
P('=== 2. Appendix A: where the two theorems Chapter 15 prints are proved, and where A says they are ===')
tab = [(i, M[i - 1]) for i in range(9944, 9956) if re.match(r'^\s+A\.\d+\s', M[i - 1])]
for i, l in tab:
    m = re.match(r'\s+(A\.\d+)\s+(.+?)\s{2,}(§[\d.]+|§[\d.]+.*)$', l)
    if not m: continue
    aid, stmt, where = m.group(1), m.group(2).strip(), m.group(3).strip()
    key = re.match(r'§([\d.]+)', where).group(1).rstrip('.')
    rr = sec(key)
    P('  %-5s %-52s -> %-22s %s' % (aid, stmt[:52], where[:22], ('%s L%d "%s"' % (key, rr[0], M[rr[0] - 1][2:60])) if rr else 'UNRESOLVED'))
P('')
P('--- A.7 is "may precede is necessary". Which sections contain that proof? ---')
for k in ('main',):
    for i, l in enumerate(L[k], 1):
        if 'may precede' in l or 'may-precede' in l:
            h = [j for j in range(i, 0, -1) if M[j - 1].startswith('#')]
            P('  L%-6d under %-28s | %s' % (i, M[h[0] - 1][:28] if h else '?', l.strip()[:110]))
r163 = sec('16.3')
P('  §16.3 is L%d-%d "%s"' % (r163[0], r163[1], M[r163[0] - 1][2:70]))
P('  occurrences of "may precede" inside §16.3: %d' % len(re.findall('may precede', body(*r163), re.I)))
r153 = sec('15.3')
P('  occurrences of "may precede" inside §15.3: %d' % len(re.findall('may precede', body(*r153), re.I)))
P('')
P('--- does Chapter 15 attribute its Lemma (A.7) or its d = 2 criterion (A.8) to Appendix A? (R-ATTR) ---')
seg = body(A, B)
for pat in [r'Appendix A', r'\bA\.7\b', r'\bA\.8\b', r'Appendix', r'Register \d+']:
    P('   %-12s in L%d-L%d: %d' % (pat, A, B, len(re.findall(pat, seg))))

P('')
P('=== 3. the same verification stated twice, in two wordings ===')
for k, i in (('main', 4302), ('main', 9981)):
    P('  %s L%d: %s' % (k, i, L[k][i - 1].strip()[:180]))
w1 = M[4301]; w2 = M[9980]
P('  "constructed" attaches to: L4302 -> %s ; L9981 -> %s'
  % (re.search(r'constructed (\w+)', w1).group(1) if re.search(r'constructed (\w+)', w1) else 'none',
     re.search(r'constructed (\w+)', w2).group(1) if re.search(r'constructed (\w+)', w2) else 'none'))
P('  L4302 calls the 274 total orders "%s"; L9981 calls them "%s"'
  % (re.search(r'274 of 274 (\w+)', w1).group(1) if re.search(r'274 of 274 (\w+)', w1) else '?',
     re.search(r'274 of 274 (\w+)', w2).group(1) if re.search(r'274 of 274 (\w+)', w2) else '?'))

P('')
P('=== 4. "20 of 20" — three sites, how many populations? ===')
for k in L:
    for i, l in enumerate(L[k], 1):
        if '20 of 20' in l: P('  %-4s L%-6d %s' % (k, i, l.strip()[:165]))

P('')
P('=== 5. Figure 15.1: placement, registry, and caption discipline ===')
P('  placed at: %s' % [i for i, l in enumerate(M, 1) if l.startswith('![') and '15.1' in l])
for reg in ('FIGURE_MAP.md', 'FIGURE_ASSETS.md'):
    t = r2lib.read_member(reg)
    hits = [ln.strip()[:130] for ln in t.split('\n') if '15.1' in ln or 'figure-15' in ln]
    P('  %-18s rows naming figure 15.1: %d %s' % (reg, len(hits), hits[:2]))
cap = body(4321, 4323)
P('  caption L4321-4323, %d characters' % len(cap))
for w in ['invisible', 'Left', 'Centre', 'Right', 'Beneath', 'recovered', 'no external information']:
    P('     %-22s %d' % (w, cap.count(w)))

P('')
P('=== 6. census rows in range, and the S-labels ===')
rows = [l.split('\t') for l in r2lib.read_member('DEFECT-CENSUS.tsv').split('\n')[1:] if l]
for r in rows:
    if r[2] == 'main' and A <= int(r[3]) <= B: P('  row %s %s L%s token %r' % (r[0], r[1], r[3], r[4]))
P('  S-label sites, all volumes:')
for k in L:
    for i, l in enumerate(L[k], 1):
        if re.search(r'\bS[123]\b\s*[—-]\s*\w', l) or re.match(r'^#+ 15\.\d S[123]', l):
            P('    %-4s L%-6d %s' % (k, i, l.strip()[:120]))

P('')
P('=== 7. how the other volumes restate Chapter 15 ===')
for k in ('mc', 'pc', 'ioi', 'sc', 'reg'):
    hits = [(i, l) for i, l in enumerate(L[k], 1) if re.search(r'§15\b|§15\.\d|Chapter 15', l)]
    P('  %-4s sites citing Chapter 15: %d' % (k, len(hits)))
    for i, l in hits[:4]: P('       L%-6d %s' % (i, l.strip()[:150]))
