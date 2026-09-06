#!/usr/bin/env python3
# r2-ch14c.py - chat 91 - PROSE batch for the Chapter 21 second-part section read
# (main L5690-L5873: 21.5.1 through 21.5.5).  Every pointer resolved to the CLAIM and not the
# heading; every Register citation resolved to its entry and tested for topic; the References
# tested for the two attributions and for the four absent graph-theoretic terms; figure 21.1
# grepped across the six volumes; and 21.5.1's three-body count checked against W-107 rather
# than re-derived (executed carried state, Ruling 41).  Deterministic; prints no wall-clock time.

import os, re
H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
A, B = 5690, 5873


def L(i): return M[i - 1]


# lifted verbatim from r2-ch13w.py (chat 88) - the exact-token heading resolver
def heading_line(sec):
    """Body heading for a section number, taking the LATER match (the front-matter
    contents list at L120-L172 is not the body -- chat 87's fix)."""
    hits = []
    for i, t in enumerate(M, 1):
        m = re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec:
            hits.append(i)
    return hits[-1] if hits else None


# lifted verbatim from r2-ch13w.py (chat 88)
def extent(start):
    lvl = len(M[start - 1]) - len(M[start - 1].lstrip('#'))
    for i in range(start + 1, len(M) + 1):
        m = re.match(r'^(#{1,4}) ', M[i - 1])
        if m and len(m.group(1)) <= lvl:
            return i - 1
    return len(M)


def body(sec):
    t = heading_line(sec)
    if t is None:
        return None, None, ''
    e = extent(t)
    return t, e, '\n'.join(M[t - 1:e])


def bodylines(sec):
    t, e, _ = body(sec)
    if t is None:
        return None, None, 0
    return t, e, sum(1 for x in M[t:e] if x.strip())


print('== 1. pointers of L5690-L5873, each resolved to the CLAIM ==')
CLAIMS = [
    (5692, '32.3', 'R reaches level 2 - pairwise consistency', ['level 2', 'pairwise']),
    (5698, '24.9', 'independence turned out triadic', ['triadic']),
    (5702, '18.4.1', 'records the deficit as DOUBLING rather than growing by one', ['doubl']),
    (5705, '36.3', 'the same shortfall on a classical object - K3, treewidth 2, one level short',
     ['treewidth', 'one level']),
    (5710, '21.5.1', 'counts the shortfall in levels of consistency', ['shortfall', 'level']),
    (5754, '18.4.1', "the asymmetry says E measures SPARSITY and not structure",
     ['sparsit']),
    (5763, '21.5.2', 'gives a cycle count and no shape', ['cycle', 'tree']),
    (5799, '14.5.7', 'makes the seed a covering problem', ['cover', 'seed']),
    (5799, '21.5.3', 'measures the graph', ['girth', 'treewidth']),
    (5811, '2.24', 'the protocol that caught the greedy anomaly', ['greedy', 'exact']),
    (5827, '14.5.9', 'the covering reading of the seed', ['cover', 'seed']),
    (5831, '2.24', 'caught by 2.24 one cycle after that protocol was written', ['protocol']),
    (5837, '21.5.3', "indexes Lambda's thirteen", ['thirteen', '13']),
    (5860, '17.1', 'admits no other coordinate here', ['coordinate']),
]
for ln, sec, what, keys in CLAIMS:
    t, e, nb = bodylines(sec)
    if t is None:
        print(f'  L{ln} -> SS{sec:8s} HEADING NOT FOUND                      *** DEVIATION')
        continue
    txt = body(sec)[2].lower()
    hit = {k: (k.lower() in txt) for k in keys}
    ok = all(hit.values()) and nb > 0
    print(f'  L{ln} -> SS{sec:8s} L{t}-L{e}, {nb:3d} body lines | claim "{what[:52]}"')
    print(f'         keys {hit}  ->  {"resolves" if ok else "*** DOES NOT RESOLVE"}')

print('\n== 2. Register citations of L5690-L5873, resolved to the entry ==')
REG = V['reg']
def reg_entry(n):
    for i, t in enumerate(REG, 1):
        if re.match(r'^#{1,4}\s*' + str(n) + r'\s*$', t.strip()):
            j = i + 1
            while j <= len(REG) and not re.match(r'^#{1,4}\s*\d+\s*$', REG[j - 1].strip()):
                j += 1
            return i, '\n'.join(REG[i:j - 1])
    return None, ''


CITES = [(5704, 487, ['consisten', '4']), (5704, 488, ['consisten']), (5704, 489, ['consisten']),
         (5759, 507, ['tree', 'constraint']), (5759, 508, ['tree', 'constraint']),
         (5795, 523, ['index', 'stage']), (5795, 524, ['index', 'orientation']),
         (5833, 525, ['seed', 'shape']), (5811, 526, ['greedy', 'seed']),
         (5872, 531, ['constraint', 'operator']), (5872, 532, ['constraint', 'operator'])]
for ln, n, keys in CITES:
    i, txt = reg_entry(n)
    if i is None:
        print(f'  L{ln} -> Register {n}: ENTRY NOT FOUND                     *** DEVIATION')
        continue
    head = next((x.strip() for x in txt.split('\n') if x.strip()), '')[:92]
    hit = {k: (k.lower() in txt.lower()) for k in keys}
    print(f'  L{ln} -> Register {n} at reg L{i}: {head}')
    print(f'         topic keys {hit}  ->  {"on topic" if any(hit.values()) else "*** OFF TOPIC"}')

print('\n== 3. the citation VERB: "Registers N" cites, "register N" merely names (G0i) ==')
for i in range(A, B + 1):
    for m in re.finditer(r'\b([Rr]egisters?)\s+(\d[\d,\u2013\u2014 and]*)', L(i)):
        print(f'  L{i}  "{m.group(1)} {m.group(2).strip()}"  '
              f'{"CITES (counted)" if m.group(1)[0] == "R" else "lowercase - NAMES, not counted"}')

print('\n== 4. References: two attributions and four absent terms ==')
def refs_of(key):
    lines = V[key]
    st = None
    for i, t in enumerate(lines, 1):
        if re.match(r'^#{1,3}\s*(References|Bibliography)\s*$', t.strip(), re.I):
            st = i
    if st is None:
        return None, None, []
    lv = len(lines[st - 1]) - len(lines[st - 1].lstrip('#'))
    en = len(lines)
    for i in range(st + 1, len(lines) + 1):
        m = re.match(r'^(#{1,3}) ', lines[i - 1])
        if m and len(m.group(1)) <= lv:
            en = i - 1; break
    return st, en, lines[st:en]


rs, re_, R = refs_of('main')
print(f'  main References at L{rs}-L{en if (en := re_) else 0}, {sum(1 for x in R if x.strip())} '
      f'non-blank lines')
blob = '\n'.join(R).lower()
for who, keys in [('Freuder', ['freuder']),
                  ('Adams, Dwinger and Schmid', ['adams', 'dwinger', 'schmid'])]:
    print(f'  attribution "{who}": ' +
          ' '.join(f'{k}={k in blob}' for k in keys))
print('  L5757 "chordal, treewidth, tree decomposition, girth - absent from this book\'s '
      'References entirely":')
for term in ['chordal', 'treewidth', 'tree decomposition', 'girth']:
    inrefs = term in blob
    sites = []
    for k in F:
        for i, t in enumerate(V[k], 1):
            if term in t.lower():
                sites.append(f'{k}:{i}')
    print(f'    {term:20s} in References: {inrefs:5}   sites in the six volumes: {len(sites)}'
          f'   {sites[:6]}{" ..." if len(sites) > 6 else ""}')
# the attributed result itself
print('  L5757-L5758 "Adams, Dwinger and Schmid give tight <=> the digraph is acyclic":')
for k in F:
    for i, t in enumerate(V[k], 1):
        if 'dwinger' in t.lower():
            print(f'    {k}:{i}  {t.strip()[:150]}')

print('\n== 5. figure 21.1 ==')
fig = 'figures/figure-21.1.png'
print(f'  file present in the container: {os.path.exists(os.path.join(H, fig))}  '
      f'(members are extracted flat; absence is not evidence of absence in the build)')
for k in F:
    for i, t in enumerate(V[k], 1):
        if re.search(r'[Ff]igure[ -]21\.1\b', t):
            print(f'  {k}:{i}  {t.strip()[:120]}')

print('\n== 6. L5698 "(1-f)^3" - the triadic survival law, other sites ==')
n = 0
for k in F:
    for i, t in enumerate(V[k], 1):
        if re.search(r'\(1\s*[-\u2212]\s*f\)', t):
            n += 1
            if n <= 12:
                print(f'  {k}:{i}  {t.strip()[:120]}')
print(f'  total sites: {n}')

print('\n== 7. L5696 "exactly one genuinely ternary object" - checked against W-107, not re-derived ==')
W = open(os.path.join(H, 'WORKING-REGISTER.md'), encoding='utf-8').read().split('\n')
st = next((i for i, t in enumerate(W, 1) if t.strip().startswith('### W-107')), None)
if st:
    en = next((i for i in range(st + 1, len(W) + 1)
               if W[i - 1].strip().startswith('### W-')), len(W))
    blk = '\n'.join(W[st - 1:en - 1])
    print(f'  W-107 at working-register L{st}-L{en - 1}, {en - st} lines')
    for t in blk.split('\n'):
        if re.search(r'three[- ]body|ternary|3-body', t, re.I):
            print(f'    {t.strip()[:150]}')
else:
    print('  W-107 NOT FOUND in WORKING-REGISTER.md   *** DEVIATION')
print('  in-range sites of the three-body count:')
for i in range(A, B + 1):
    if re.search(r'three[- ]body|ternary|3-body', L(i), re.I):
        print(f'    L{i}  {L(i).strip()[:130]}')

print('\n== 8. L5726 "a tree is exactly a graph with no cycle" - the definition ==')
print('  A graph with no cycle is a FOREST; a TREE is a connected acyclic graph.')
print('  The conclusion is unaffected here: r2-ch14b measures the L8 constraint graph')
print('  connected (1 component, 8 nodes, 7 edges), so it is a tree and not merely a forest.')
print('  Recorded as a definitional imprecision, not a false conclusion.')

print('\n== 9. self-description in range: claims about what the book does elsewhere ==')
SELF = [(5785, 'the largest orientation cost anywhere in this book'),
        (5786, 'the first object on which the second operator is the only one that works'),
        (5696, 'This book has exactly one genuinely ternary object'),
        (5849, 'Every genuine constraint in this book is carried by one of the two operators'),
        (5757, "absent from this book's References entirely"),
        (5860, 'SS17.1 admits no other here')]
for ln, txt in SELF:
    print(f'  L{ln}  {txt}')
print('  (L5785 is measured in r2-ch14b section 7; the rest are pointer- or grep-checked above.)')
