#!/usr/bin/env python3
"""r3-arith-01.py — R3 arithmetic class, item 153-01: the Mathematical Compendium's penetration
percentage against its own count. BUILD91 -> BUILD92 main, BUILD180 -> BUILD181 compendia.

The finding (FINDINGS-153-PENDING.md, 153-01, MEASURED by tools/arith.py --roster volumes and read
at the site): the Mathematical Compendium prints *penetration (|d|>=0.1) falls 146 of 163 = 92%*.
146/163 = 89.57%, which quantizes to 90% (Decimal.quantize, ROUND_HALF_EVEN, convention named; the
standing method forbids round()). Register 1048 states the same claim as 146 of 163, 90%, and in the
same line gives 92% its own object -- the combined two-claim figure at 198 of 215 (92.09% -> 92%).

Which of the two the compendium's 92% came from -- the claim's own superseded value or the combined
figure printed beside it -- is NOT decided here. Either reading leaves 92% as not the percentage of
146 of 163, and the Register's 90% governs the site.

One numeral is changed. No mathematics is rewritten and no count is touched.

Usage:  python3 r3-arith-01.py            dry run: everything in memory, nothing written
        python3 r3-arith-01.py --write    writes /home/claude/build92/<members> and both new bundles
"""
import os, re, sys, hashlib, subprocess, tempfile
from decimal import Decimal, ROUND_HALF_EVEN

MEM = '/home/claude/members/'; HOME = '/home/claude/'
OLD_MAIN_B = HOME + 'The_Method_1_6_BUILD91_main_and_register.md'; OLD_MAIN_MD5 = '2e5e442bde421bb952e665985b0b30d2'
OLD_COMP_B = HOME + 'The_Method_1_6_BUILD180_compendia_papers_audits.md'; OLD_COMP_MD5 = 'ea5becc40e13debe4faaf6c7e0cde960'
NEW_MAIN_B = HOME + 'The_Method_1_6_BUILD92_main_and_register.md'
NEW_COMP_B = HOME + 'The_Method_1_6_BUILD181_compendia_papers_audits.md'
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
VOLS = [MAIN, REG, MC, 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md']
WRITE = '--write' in sys.argv
OUT = HOME + 'build92/' if WRITE else tempfile.mkdtemp(prefix='r3a1-dry-') + '/'
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

def pct(n, d):  # the convention, named and applied once
    return (Decimal(n) / Decimal(d) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)

assert pct(146, 163) == 90 and pct(198, 215) == 92, 'the arithmetic this repair rests on'
print(f'146/163 -> {pct(146,163)}%   198/215 -> {pct(198,215)}%   (ROUND_HALF_EVEN, 0 dp)')

old_main = open(MEM + MAIN, 'rb').read(); old_reg = open(MEM + REG, 'rb').read(); old_mc = open(MEM + MC, 'rb').read()
m = old_main.decode('utf-8'); r = old_reg.decode('utf-8'); c = old_mc.decode('utf-8')
ML = m.split('\n'); RL = r.split('\n'); CL = c.split('\n')
for nm, b in ((MAIN, old_main), (REG, old_reg), (MC, old_mc)):
    print(f'old {nm}  {len(b):,} B  md5 {md5(b)}  {b.count(b"\n"):,} lines')

def S(L, n, must):
    l = L[n - 1]; assert must in l, f'L{n} does not carry {must!r}: {l[:90]!r}'; return l
def col(l, old, new):
    assert l.count(old) == 1, (old, l[:80]); return l.replace(old, new)

# ---------------------------------------------------------------- the site, asserted by content
c2930 = S(CL, 2930, 'penetration (|d|≥0.1) falls 146 of 163 = 92%')
SUBS_MC = [('153-01  mc L2930', c2930 + '\n',
            col(c2930, 'falls 146 of 163 = 92%', 'falls 146 of 163 = 90%') + '\n')]

# ---------------------------------------------------------------- extent, driven to its fixed point
l7373 = S(ML, 7373, '1,637 entries, 1 to 1794, at this build (2026-09-01)')
SUBS_MAIN = [('extent  main L7373', l7373 + '\n',
              col(l7373, '1,637 entries, 1 to 1794, at this build (2026-09-01)',
                  '1,638 entries, 1 to 1795, at this build (2026-09-03)') + '\n')]
l6 = S(RL, 6, '**1637 entries, 1 to 1794.**'); l65 = S(RL, 65, '**1637 entries, 1 to 1794**')
SUBS_REG = [
 ('extent  Register L6', l6 + '\n', col(col(l6, '**1637 entries, 1 to 1794.**', '**1638 entries, 1 to 1795.**'),
                                        'and 165 to 1794, 1,472 entries, are the mature record',
                                        'and 165 to 1795, 1,473 entries, are the mature record') + '\n'),
 ('extent  Register L65', l65 + '\n',
  col(l65, '**1637 entries, 1 to 1794** (genesis 1–94, superseded 95–164, mature record 165–1794)',
      '**1638 entries, 1 to 1795** (genesis 1–94, superseded 95–164, mature record 165–1795)') + '\n'),
]
E1795 = ("### 1795\n\n**THE COMPENDIUM'S PENETRATION PERCENTAGE DID NOT FOLLOW ITS OWN COUNT.** *The Mathematical "
         "Compendium printed the penetration claim as 146 of 163 = 92%. 146 of 163 is 90% at nought decimal places, "
         "rounding half to even; register 1048 states that claim as 146 of 163, 90%, and in the same line gives 92% its "
         "own object — the combined two-claim figure, 198 of 215. Which of the two the compendium's 92% came from, the "
         "claim's own superseded value or the combined figure printed beside it, is not decided; on either reading it is "
         "not the percentage of 146 of 163. Corrected to 90%; the counts are untouched.* Registers 1048. (a correction.)\n")
TAIL = '\n' + E1795
assert r.endswith('(a correction.)\n') and not r.endswith('\n\n'), 'Register tail form changed'
assert not re.search(r'^### 1795\b', r, re.M), 'entry 1795 already exists'

def apply(text, subs):
    t = text
    for name, a, b in subs:
        assert t.count(a) == 1, f'{name}: anchor occurs {t.count(a)} times'; assert a != b; t = t.replace(a, b)
    return t
def reverse(text, subs):
    t = text
    for name, a, b in reversed(subs):
        assert t.count(b) == 1, f'{name}: reverse anchor occurs {t.count(b)} times'; t = t.replace(b, a)
    return t

new_c = apply(c, SUBS_MC); assert md5(reverse(new_c, SUBS_MC).encode('utf-8')) == md5(old_mc), 'mc reverse FAILED'
new_m = apply(m, SUBS_MAIN); assert md5(reverse(new_m, SUBS_MAIN).encode('utf-8')) == md5(old_main), 'main reverse FAILED'
new_r = apply(r, SUBS_REG) + TAIL
assert new_r.endswith(TAIL) and md5(reverse(new_r[:-len(TAIL)], SUBS_REG).encode('utf-8')) == md5(old_reg), 'Register reverse FAILED'
print(f'mc: {len(SUBS_MC)} substitution, reverse recovers md5 {md5(old_mc)} == old: True')
print(f'main: {len(SUBS_MAIN)} substitution, reverse recovers md5 {md5(old_main)} == old: True')
print(f'Register: {len(SUBS_REG)} substitutions + 1 entry, reverse recovers md5 {md5(old_reg)} == old: True')
for nm, oldL, newT in ((MC, CL, new_c), (MAIN, ML, new_m)):
    NL = newT.split('\n'); assert len(NL) == len(oldL), f'{nm}: line count moved'
    print(f'{nm} changed lines:', [i + 1 for i in range(len(NL)) if NL[i] != oldL[i]])

# ---------------------------------------------------------------- kinds.py recount on the new Register
if WRITE: assert not os.path.exists(OUT), f'{OUT} exists'; os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
open(OUT + MC, 'wb').write(new_c.encode('utf-8')); open(OUT + MAIN, 'wb').write(new_m.encode('utf-8'))
open(OUT + REG, 'wb').write(new_r.encode('utf-8'))
p = subprocess.run(['python3', MEM + 'kinds.py', OUT + REG, '--write'], capture_output=True, text=True, timeout=200)
print('kinds.py --write:', p.stdout.strip().split('\n')[0]); assert p.returncode == 0
final_r = open(OUT + REG, 'rb').read().decode('utf-8'); FL = final_r.split('\n'); NR = new_r.split('\n')
assert len(FL) == len(NR)
kdiff = [i + 1 for i in range(len(NR)) if FL[i] != NR[i]]
print('kinds.py changed Register lines:', kdiff)
for i in kdiff: print(f'   L{i}: {NR[i-1][:64]!r} -> {FL[i-1][:64]!r}')
assert all(re.match(r'\| \*\*', NR[i - 1]) or 'entry headings' in NR[i - 1] for i in kdiff), 'kinds.py touched a line outside its table'
rev = FL[:]
for i in kdiff: rev[i - 1] = NR[i - 1]
assert '\n'.join(rev) == new_r
assert md5(reverse(new_r[:-len(TAIL)], SUBS_REG).encode('utf-8')) == md5(old_reg)
print(f'Register (final): reverse from the written bytes recovers md5 {md5(old_reg)} == old: True')
final_reg_b = final_r.encode('utf-8'); new_main_b = new_m.encode('utf-8'); new_mc_b = new_c.encode('utf-8')

# ---------------------------------------------------------------- fixed point over the six volumes
texts = {v: (new_m if v == MAIN else final_r if v == REG else new_c if v == MC
             else open(MEM + v, encoding='utf-8').read()) for v in VOLS}
def sites(pat):
    return {v.split('___')[-1].replace(MAIN, 'main'): [i + 1 for i, l in enumerate(t.split('\n')) if re.search(pat, l)]
            for v, t in texts.items()}
for pat in (r'1 to 1795', r'1 to 1794', r'\b1,?637 entries\b', r'\b1,?638 entries\b',
            r'146 of 163 = 92%', r'146 of 163 = 90%', r'165 to 179\d|165–179\d', r'1,47[23] entries'):
    s = sites(pat)
    print(f'{pat!r}: ' + (' '.join(f'{v}:{n}' for v, ns in s.items() for n in ns) if any(s.values()) else '0 sites'))
assert not any(sites(r'1 to 1794').values()), 'extent fixed point not reached'
# The defective string must be gone from every volume EXCEPT the Register's new entry, which quotes it:
# a correction entry cites the state it supersedes and both states are preserved (standing discipline).
_bad = sites(r'146 of 163 = 92%')
assert not _bad['Mathematical_Compendium-2.md'], 'the mc site is not repaired'
assert sum(len(v) for k, v in _bad.items() if k != 'The_Register-2.md') == 0, 'the defective figure survives outside the Register'
_q = [n for n in _bad['The_Register-2.md'] if final_r.split('\n')[n - 1].startswith('**THE COMPENDIUM')]
assert _bad['The_Register-2.md'] == _q, 'a 92% site in the Register outside entry 1795'
print(f'defective figure: 0 sites outside the Register; {len(_q)} inside entry 1795, where it is quoted as superseded')

# ---------------------------------------------------------------- press anchors must survive
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt in ((MAIN, m), (REG, r), (MC, c)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:44], oldt.count(a), texts[v].count(a)) for a in anchors if oldt.count(a) != texts[v].count(a)]
    print(f'build.py SUBS anchors on {v}: {len(anchors)} checked; count changed by this edit: {moved}')
    assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- both bundles: replace, reverse-guard, write
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
def rebuild(path, want_md5, repl, label, newpath):
    raw = open(path, 'rb').read(); assert md5(raw) == want_md5, f'{label} bundle md5 mismatch'
    ms = dict((mm.group(1).decode(), mm.group(2)) for mm in MEMBER.finditer(raw))
    nb = raw
    for n, body in repl.items():
        assert ms[n] == {MAIN: old_main, REG: old_reg, MC: old_mc}[n], f'{n}: seated body is not the one edited'
        ob = block(n, ms[n]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n, body))
    rv = nb
    for n, body in repl.items():
        assert rv.count(block(n, body)) == 1; rv = rv.replace(block(n, body), block(n, ms[n]))
    assert md5(rv) == want_md5, f'{label} reverse FAILED'
    print(f'{label}: reverse recovers md5 {md5(rv)} == old: True')
    print(f'new {label}  {len(nb):,} B  md5 {md5(nb)}  {nb.count(b"\n"):,} lines  {len(ms)} members')
    if WRITE:
        assert not os.path.exists(newpath), f'{newpath} exists — never overwrite'
        open(newpath, 'wb').write(nb); print('written', newpath)
    return md5(nb)

rebuild(OLD_MAIN_B, OLD_MAIN_MD5, {MAIN: new_main_b, REG: final_reg_b}, 'BUILD92 main', NEW_MAIN_B)
rebuild(OLD_COMP_B, OLD_COMP_MD5, {MC: new_mc_b}, 'BUILD181 compendia', NEW_COMP_B)
print('written ' + OUT if WRITE else 'DRY RUN — nothing written under /home/claude')
