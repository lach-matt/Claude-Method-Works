#!/usr/bin/env python3
# r2-ch13i.py — Phase R2, chat 81, segment 2: main §14.5.2–§14.5.7 (L3798–3809), six headings with no body.
# Measures (1) that each of the six carries zero body lines, (2) every pointer into them from every
# member, with the R-FORM citation chains separated out, (3) whether the promised content sits anywhere
# in §14.5.8–§14.5.14 (L3810–4075) or elsewhere in the main volume.
# Deterministic: no wall-clock output.  Figures for the 840/526/750 witness are r2-ch13e.out's (chat 80).

import os, re

H = os.path.dirname(os.path.abspath(__file__))
def lines(name): return open(os.path.join(H, name), encoding='utf-8').read().split('\n')

MAIN = 'The_Method_1_6-2.md'
M = lines(MAIN)

print('=== (1) L3798–3809: the body of each subsection ===')
heads = [(i + 1, M[i].strip()) for i in range(3790, 3820) if M[i].startswith('### 14.5.')]
for k, (ln, txt) in enumerate(heads):
    nxt = heads[k + 1][0] if k + 1 < len(heads) else 3917
    body = [M[j] for j in range(ln, nxt - 1) if M[j].strip()]
    print('   L%-5d %-70s body lines: %d' % (ln, txt[:70], len(body)))

print('=== (2) pointers into §14.5.2 … §14.5.7, all members ===')
PAT = re.compile(r'(?<![\d.])14\.5\.([2-7])(?![\d])')
SKIP = ('READ-', 'HANDOFF', 'WORKING-REGISTER', 'DEFERRED', 'RULINGS', 'CENSUS', 'MANIFEST')
tot = {str(n): 0 for n in range(2, 8)}
per_member = {}
chains = []
for fn in sorted(os.listdir(H)):
    if not fn.endswith('.md') or any(fn.startswith(s) for s in SKIP): continue
    L = lines(fn)
    for i, l in enumerate(L):
        if fn == MAIN and l.strip().startswith('### 14.5.'): continue
        for m in PAT.finditer(l):
            tot[m.group(1)] += 1
            per_member.setdefault(fn, {}).setdefault(m.group(1), []).append(i + 1)
            if re.match(r'\s*(Proved|Computed)\s*—', l): chains.append((fn, i + 1, m.group(1), l.strip()[:90]))
for fn in sorted(per_member):
    parts = ' '.join('§14.5.%s×%d %s' % (s, len(v), v) for s, v in sorted(per_member[fn].items()))
    print('   %-46s %s' % (fn[:46], parts))
print('   TOTAL pointers by subsection: %s' % {'§14.5.' + k: v for k, v in sorted(tot.items())})
print('   TOTAL pointers into the six: %d, across %d members' % (sum(tot.values()), len(per_member)))
print('   R-FORM citation chains resolving into the six: %d' % len(chains))
for fn, ln, s, txt in chains: print('      %s L%d → §14.5.%s | %s' % (fn[:40], ln, s, txt))

print('=== (3) does the promised content sit at §14.5.8–§14.5.14 (L3810–4075), or anywhere? ===')
PROBE = {'§14.5.2 the cycle expression': r'\bcycle\b',
         '§14.5.3 two pairwise operators': r'two (pairwise )?operators|one name for both',
         '§14.5.3 the 840-cell witness': r'\b840\b',
         '§14.5.3 E(ℛ) = 750': r'\b750\b',
         '§14.5.4 what E measures': r'E measures',
         '§14.5.5 ℛ₄ / orientations': r'ℛ₄|orientation',
         '§14.5.6 localises': r'localis',
         '§14.5.7 the seed definition': r'seed iff|φ̂\(G\)',
         '§14.5.7 anti-exchange': r'anti-exchange',
         '§14.5.7 zero cells forced': r'forced'}
for nm, p in PROBE.items():
    r = re.compile(p)
    inblock = [i + 1 for i in range(3809, 4075) if r.search(M[i])]
    inmain = [i + 1 for i in range(len(M)) if r.search(M[i]) and not M[i].strip().startswith('### 14.5.')]
    print('   %-32s in L3810–4075: %-2d %-22s | whole main volume: %-3d %s'
          % (nm, len(inblock), str(inblock[:5]), len(inmain), inmain[:6]))

print('=== (4) the 840/526/750 witness: where it actually sits ===')
for ln in (3577, 3578, 3579, 5672, 5676, 11563):
    print('   L%-6d %s' % (ln, M[ln - 1].strip()[:120]))
out = open(os.path.join(H, 'r2-ch13e.out'), encoding='utf-8').read().split('\n')
for l in out:
    if '526' in l or '840' in l: print('   r2-ch13e.out (chat 80, re-run OK at this chat\'s gate): %s' % l.strip()[:110])
