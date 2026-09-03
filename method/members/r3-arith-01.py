#!/usr/bin/env python3
"""r3-arith-01.py — R3 arithmetic class, item 153-01. BUILD93 -> BUILD94 main, BUILD191 -> BUILD192 compendia.

THE FINDING (MEASURED by tools/arith.py --roster volumes, then read at the site). The Mathematical
Compendium prints *penetration (|d|>=0.1) falls 146 of 163 = 92%*. 146/163 = 89.57%, which quantizes
to 90% at nought decimal places rounding half to even (Decimal.quantize; the standing method forbids
round()). Register 1048 states the same claim as *146 of 163, 90% against 92%*, and in the same line
gives 92% its own object -- *Combined as two claims: 198 of 215 -- 92%* (198/215 = 92.09% -> 92%).

Which of the two the compendium's 92% came from -- the claim's own superseded value or the combined
figure printed beside it -- is NOT decided here, and entry 1800 says so. On either reading it is not
the percentage of 146 of 163, and 1048's 90% governs the site.

NUMBERING. This is a re-key. The item was first executed on a superseded base as entry 1795, a
number chat 152 had already spent; 1793-1796 are seated and 1797 is staged for audit_math.py.
r3-wl2 took 1798-1799, so this takes 1800.

RULING A. The entries stand, the repair waits. The Register's front-matter count sites are NOT
touched, main's extent phrase is NOT touched and kinds.py --write is NOT run. The drift those leave
is scored, not asserted, and is carried as a finding by reg1-04.

One numeral changes in a reader-facing volume. No count is touched and no mathematics is rewritten.

Usage:  python3 r3-arith-01.py            dry run
        python3 r3-arith-01.py --write    writes /home/claude/build94/<members> and both new bundles
"""
import os, re, sys, hashlib, subprocess, tempfile
from decimal import Decimal, ROUND_HALF_EVEN

MEM = '/home/claude/members/'; HOME = '/home/claude/'
OLD_MAIN_B = HOME + 'The_Method_1_6_BUILD93_main_and_register.md'; OLD_MAIN_MD5 = 'ec86313b865687bad00fdb66b3faf4a4'
OLD_COMP_B = HOME + 'The_Method_1_6_BUILD191_compendia_papers_audits.md'; OLD_COMP_MD5 = '072cc2b825eb52102a23ab657e680ccd'
NEW_MAIN_B = HOME + 'The_Method_1_6_BUILD94_main_and_register.md'
NEW_COMP_B = HOME + 'The_Method_1_6_BUILD192_compendia_papers_audits.md'
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
VOLS = [MAIN, REG, MC, 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md']
WRITE = '--write' in sys.argv
OUT = HOME + 'build94/' if WRITE else tempfile.mkdtemp(prefix='r3a1-dry-') + '/'
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

def pct(n, d):
    return (Decimal(n) / Decimal(d) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)
assert pct(146, 163) == 90 and pct(198, 215) == 92, 'the arithmetic this repair rests on'
print(f'146/163 -> {pct(146,163)}%   198/215 -> {pct(198,215)}%   (ROUND_HALF_EVEN, 0 dp)')

old_reg = open(MEM + REG, 'rb').read(); old_mc = open(MEM + MC, 'rb').read()
r = old_reg.decode('utf-8'); c = old_mc.decode('utf-8'); CL = c.split('\n')
for nm, b in ((REG, old_reg), (MC, old_mc)):
    print(f'old {nm}  {len(b):,} B  md5 {md5(b)}  {b.count(chr(10).encode()):,} lines')

seated = sorted(int(x) for x in re.findall(r'^### (\d+)$', r, re.M))
HI = max(seated); N = 1800
assert HI == 1799, f'highest seated entry is {HI}, not 1799 — r3-wl2 must run first'
assert not re.search(rf'^### {N}\b', r, re.M), f'entry {N} already seated'
print(f'entries seated: {len(seated)}  highest: {HI}  this item takes: {N}')

def col(l, old, new):
    assert l.count(old) == 1, (old, l[:80]); return l.replace(old, new)

c2930 = CL[2929]; assert 'penetration (|d|≥0.1) falls 146 of 163 = 92%' in c2930, c2930[:90]
SUBS_MC = [('153-01  mc L2930', c2930 + '\n', col(c2930, 'falls 146 of 163 = 92%', 'falls 146 of 163 = 90%') + '\n')]

E = (f"### {N}\n\n**THE COMPENDIUM'S PENETRATION PERCENTAGE DID NOT FOLLOW ITS OWN COUNT.** *The Mathematical "
     "Compendium printed the penetration claim as 146 of 163 = 92%. 146 of 163 is 90% at nought decimal places, "
     "rounding half to even; register 1048 states that claim as 146 of 163, 90%, and in the same line gives 92% its "
     "own object — the combined two-claim figure, 198 of 215. Which of the two the compendium's 92% came from, the "
     "claim's own superseded value or the combined figure printed beside it, is not decided; on either reading it is "
     "not the percentage of 146 of 163. Corrected to 90%; the counts are untouched.* Registers 1048. (a correction.)\n")
TAIL = '\n' + E
assert r.endswith('\n') and not r.endswith('\n\n'), 'Register tail form changed'

def apply(t, subs):
    for name, a, b in subs:
        assert t.count(a) == 1, f'{name}: anchor occurs {t.count(a)} times'; assert a != b; t = t.replace(a, b)
    return t
def reverse(t, subs):
    for name, a, b in reversed(subs):
        assert t.count(b) == 1, f'{name}: reverse anchor occurs {t.count(b)} times'; t = t.replace(b, a)
    return t

new_c = apply(c, SUBS_MC); assert md5(reverse(new_c, SUBS_MC).encode('utf-8')) == md5(old_mc), 'mc reverse FAILED'
new_r = r + TAIL; assert new_r[:-len(TAIL)] == r, 'Register is not old + tail'
print(f'mc: 1 substitution, reverse recovers md5 {md5(old_mc)} == old: True')
print(f'Register: 0 substitutions + 1 entry appended, old bytes untouched: True')
NC = new_c.split('\n'); assert len(NC) == len(CL), 'mc line count moved'
print('mc changed lines:', [i + 1 for i in range(len(NC)) if NC[i] != CL[i]])

# ---------------------------------------------------------------- Ruling A: the parked repair, scored
if not os.path.isdir(OUT): os.makedirs(OUT)
_t = tempfile.mkdtemp(prefix='r3a1-kinds-') + '/R.md'; open(_t, 'w', encoding='utf-8').write(new_r)
k = subprocess.run(['python3', MEM + 'kinds.py', _t], capture_output=True, text=True, timeout=200)
assert k.returncode == 0, k.stderr[-300:]
counted = int(re.search(r"'a correction': (\d+)", k.stdout).group(1))
printed = int(re.search(r'\| \*\*a correction\*\* \| ([\d,]+) \|', new_r).group(1).replace(',', ''))
os.remove(_t)
print('PARKED (Ruling A), scored not repaired:')
print(f'  entries now 1 to {N}; the front matter still prints its BUILD180 extent — reg1-04 carries this')
print(f'  kinds table prints "a correction" {printed}; kinds.py counts {counted} — stale by {counted - printed}')

# ---------------------------------------------------------------- fixed point over the six volumes
texts = {v: (new_r if v == REG else new_c if v == MC else open(MEM + v, encoding='utf-8').read()) for v in VOLS}
def sites(pat):
    return {v.split('___')[-1].replace(MAIN, 'main'): [i + 1 for i, l in enumerate(t.split('\n')) if re.search(pat, l)]
            for v, t in texts.items()}
for pat in (r'146 of 163 = 92%', r'146 of 163 = 90%'):
    s = sites(pat)
    print(f'{pat!r}: ' + (' '.join(f'{v}:{n}' for v, ns in s.items() for n in ns) if any(s.values()) else '0 sites'))
bad = sites(r'146 of 163 = 92%')
assert not bad[MC.split('___')[-1]], 'the mc site is not repaired'
assert sum(len(v) for kk, v in bad.items() if kk != 'The_Register-2.md') == 0, 'the figure survives outside the Register'
# The Register keeps exactly one: entry N quoting the text it corrected. A correction entry cites
# the state it supersedes and both states are preserved. Register 1048 does NOT match this literal
# -- it reads "**146 of 163**, 90% against 92%" -- so it is not among these sites.
_rs = bad['The_Register-2.md']
assert len(_rs) == 1, f'expected only entry {N}\'s quotation in the Register, got {_rs}'
_body = new_r.split(f'### {N}')[1]
assert '146 of 163 = 92%' in _body, f'the surviving site is not inside entry {N}'
print(f"the defective figure survives only at Register L{_rs[0]}, inside entry {N}, where it is quoted as superseded")

# ---------------------------------------------------------------- press anchors
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt in ((REG, r), (MC, c)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:44], oldt.count(a), texts[v].count(a)) for a in anchors if oldt.count(a) != texts[v].count(a)]
    print(f'build.py SUBS anchors on {v}: {len(anchors)} checked; count changed by this edit: {moved}')
    assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- both bundles
new_reg_b = new_r.encode('utf-8'); new_mc_b = new_c.encode('utf-8')
open(OUT + REG, 'wb').write(new_reg_b); open(OUT + MC, 'wb').write(new_mc_b)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
def rebuild(path, want, repl, label, newpath):
    raw = open(path, 'rb').read(); assert md5(raw) == want, f'{label} bundle md5 mismatch'
    ms = dict((mm.group(1).decode(), mm.group(2)) for mm in MEMBER.finditer(raw)); nb = raw
    for n, body in repl.items():
        assert ms[n] == {REG: old_reg, MC: old_mc}[n], f'{n}: seated body is not the one edited'
        ob = block(n, ms[n]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n, body))
    rv = nb
    for n, body in repl.items():
        assert rv.count(block(n, body)) == 1; rv = rv.replace(block(n, body), block(n, ms[n]))
    assert md5(rv) == want, f'{label} reverse FAILED'
    print(f'{label}: reverse recovers md5 {md5(rv)} == old: True')
    print(f'new {label}  {len(nb):,} B  md5 {md5(nb)}  {nb.count(chr(10).encode()):,} lines  {len(ms)} members')
    if WRITE:
        assert not os.path.exists(newpath), f'{newpath} exists — never overwrite'
        open(newpath, 'wb').write(nb); print('written', newpath)

rebuild(OLD_MAIN_B, OLD_MAIN_MD5, {REG: new_reg_b}, 'BUILD94 main', NEW_MAIN_B)
rebuild(OLD_COMP_B, OLD_COMP_MD5, {MC: new_mc_b}, 'BUILD192 compendia', NEW_COMP_B)
print(('written ' + OUT) if WRITE else 'DRY RUN — nothing written under /home/claude')
