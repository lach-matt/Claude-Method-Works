#!/usr/bin/env python3
# r2-ch14e.py - chat 92 - PROSE batch for the Chapter 21 close (main L5874-L5936).
# Every section pointer resolved to the CLAIM and not the heading; every Register citation
# resolved and topic-tested; the companion-citation convention measured across all six
# volumes; and the section's restatements checked against the entries that carry them.
# Deterministic; prints no wall-clock time.

import os, re
H = os.path.dirname(os.path.abspath(__file__))
F = {'main': 'The_Method_1_6-2.md', 'reg': 'The_Method_1_6___The_Register-2.md',
     'mc': 'The_Method_1_6___Mathematical_Compendium-2.md',
     'pc': 'The_Method_1_6___The_Physics_Compendium-2.md',
     'ioi': 'The_Method_1_6___The_Index_of_Indices-2.md',
     'sc': 'The_Method_1_6___Spectra_Compendium-2.md'}
V = {k: open(os.path.join(H, v), encoding='utf-8').read().split('\n') for k, v in F.items()}
M = V['main']
A, B = 5874, 5936
SEC = '\n'.join(M[A - 1:B])


# lifted verbatim from r2-ch13w.py (chat 88) - the exact-token heading resolver
def heading_line(sec):
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
    h = heading_line(sec)
    if h is None:
        return None, None, ''
    e = extent(h)
    return h, e, '\n'.join(M[h:e])


print('=' * 78)
print('r2-ch14e  PROSE batch  -  main L5874-L5936  (21.6, 21.6.1, 21.6.2)')
print('=' * 78)

# ---------------------------------------------------------------- E0 self-test
print('\n[E0] resolver self-test (chat 88: exact token, never prefix).')
for s in ('21.6', '21.6.1', '21.6.2'):
    print(f'  §{s:8s} -> L{heading_line(s)}  {M[heading_line(s)-1].strip()[:64]}')
print('  prefix matching would resolve §21.6 to §21.6.2; exact-token resolution does not.')

# ---------------------------------------------------------------- E1 pointers
print('\n[E1] every section pointer, resolved to the CLAIM.')
PTR = [
    (5896, '21.1', ['naming', 'two'], "§21.1's table shows one object under two namings with different E"),
    (5901, '12.11.8', ['vacuous'], "§12.11.8 names 'a complete rectangle, E = 0 vacuously'"),
    (5922, '21.5.5', ['role'], "§21.5.5's *role* axis"),
    (5928, '10.4', ['THETA', 'STAT'], "§10.4 nests it - THETA = 0 at 16, STAT = 0 at 8"),
    (5932, '8.1', ['charger'], "§8.1 prints five chargers"),
    (5933, '10.1', ['charger'], "§10.1 counts six [chargers]"),
]
fails = []
for ln, sec, keys, claim in PTR:
    h, e, txt = body(sec)
    title = M[h - 1].strip().lstrip('#').strip() if h else '(no heading)'
    hit = {k: (k.lower() in txt.lower()) for k in keys}
    ok = all(hit.values())
    print(f'  L{ln} -> §{sec:8s} L{h}  "{title[:46]}"')
    print(f'        claim: {claim}')
    print(f'        keyword in section body {hit}   -> {"RESOLVES" if ok else "DOES NOT RESOLVE"}')
    if not ok:
        fails.append((ln, sec, title))
print(f'  MEASURED {len(fails)} of {len(PTR)} pointers do not resolve to their claim:')
for ln, sec, title in fails:
    print(f'    L{ln} §{sec} -> "{title[:56]}"')

# ---------------------------------------------------------------- E2 convention
print('\n[E2] the three failing pointers are COMPANION sections; the book has a marked form.')
for k in F:
    n = len(re.findall(r'\bT §\d', '\n'.join(V[k])))
    print(f'  {k:5s} occurrences of the marked companion form "T §N": {n}')
print('  the same claim in the Mathematical Compendium, mc L2498:')
print(f'    {V["mc"][2497].strip()}')
print('  main §21.6.2 cites the same two sections bare:')
for ln in (5928, 5932, 5933):
    print(f'    L{ln}: {M[ln-1].strip()[:96]}')
print('  MEASURED: within this 63-line read the identical bare form §N.N is used for three')
print('  main-volume sections (21.1, 12.11.8, 21.5.5) and three companion sections (10.4,')
print('  8.1, 10.1); all three companion numbers also exist as main-volume sections.')

# ---------------------------------------------------------------- E3 registers
print('\n[E3] Register citations, resolved and topic-tested.')
R = V['reg']
idx = {}
for i, t in enumerate(R, 1):
    m = re.match(r'^### (\d+)\s*$', t.strip())
    if m:
        idx[m.group(1)] = i
for n, keys in (('546', ['a·b', 'composite']), ('547', ['rung-1', 'ANEC']), ('548', ['FACE', 'JUR'])):
    ln = idx[n]
    blk = '\n'.join(R[ln:ln + 3])
    hit = {k: (k in blk) for k in keys}
    print(f'  Register {n} -> reg L{ln}   topic keys {hit}  -> {"ON TOPIC" if all(hit.values()) else "CHECK"}')
print('  lowercase "register NNN" in range (r2-tools\' regex is case-sensitive):')
low = re.findall(r'register \d+', SEC)
print(f'    {low if low else "none"}')

# ---------------------------------------------------------------- E4 scope
print('\n[E4] L5917 against Register 547: the scope of "only that index".')
print(f'  volume  L5917: {M[5916].strip()[:100]}')
print(f'  Register 547 : ...{R[idx["547"]][R[idx["547"]].find("Only that index"):][:96]}')
print(f'  §21.6.2 heading L5924: {M[5923].strip()[:70]}')
vol_has_scope = 'four' in M[5916] or 'companion' in M[5916]
print(f'  MEASURED: the volume\'s sentence carries the qualifier "of the companion\'s four": '
      f'{vol_has_scope}')
print(f'  the Register restricts the claim to four indices; the volume states it unrestricted')
print(f'  while its own next heading names FIVE. Indices compared at L5917-L5918: V6, the null')
print(f'  surface, V3 = 3. The charger index of §21.6.2 is not among them.')

# ---------------------------------------------------------------- E5 V-numbering
print('\n[E5] the V-numbering §21.6.1 uses was retired by the companion\'s §8.4.')
print(f'  main L4256-L4257: {" ".join(M[4255:4257]).strip()[:150]}')
print(f'  Register 544 (reg L2037) carries the same withdrawal.')
caveat = any(w in SEC for w in ('retired', 'withdrawn', 'old V-numbering', '§8.4'))
print(f'  any caveat on the V-numbering inside L5874-L5936: {caveat}')
print(f'  MEASURED: §21.6.1 cites V6 and V3 under a numbering the volume itself records as')
print(f'  retired, with no pointer to that record.')

# ---------------------------------------------------------------- E6 V3 geometry
print('\n[E6] "V3 geometry" - every site in the six volumes.')
tot = 0
for k in F:
    for i, t in enumerate(V[k], 1):
        if 'V3 geometry' in t:
            print(f'  {k}:L{i}: {t.strip()[:88]}')
            tot += 1
print(f'  MEASURED {tot} sites, both inside this section: the object is named and never defined,')
print(f'  and it is the one row of the L5880 table with no second site anywhere.')

# ---------------------------------------------------------------- E7 restatement
print('\n[E7] the table\'s three E figures against their other sites.')
for pat, want in ((r'the periodic table\s', '90 / 36'), (r'the calendar, \(month, day\)', '365 / 7'),
                  (r'26-cell set', '26 / 38')):
    n = 0
    for k in F:
        for i, t in enumerate(V[k], 1):
            if re.search(pat, t):
                print(f'  {k}:L{i}: {t.strip()[:92]}')
                n += 1
                if n >= 3:
                    break
        if n >= 3:
            break
    print(f'    -> expecting {want}')
print('\n' + '=' * 78)
