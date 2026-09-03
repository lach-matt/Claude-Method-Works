#!/usr/bin/env python3
"""r3-wl2.py — R3 class WL (16z-01) RE-TAKEN. BUILD92 -> BUILD93 main.

Successor to the seated `r3-wl.py`, which is never edited in place (chat 68: instruments travel as
bundle members). HANDOFF-152-RESUME section 6 item 1 owes this instrument: the withdrawn-law class
re-taken on numbers that clear 1797.

WHY A RE-TAKE. r3-wl claimed Register entries 1793-1794. Chat 152's cypher audit claimed the same
two numbers and was seated first, carried forward by chat 151-R under M's Ruling A. The wording M
approved at chat 128 is unchanged; only the entry numbers move.

NUMBERING. Highest seated entry is 1796 (MEASURED). 1797 is STAGED, not seated, in
REGISTER-QUEUE-APPEND-cypher-audit.md for chat 152's unseated audit_math.py, so it is left alone
rather than taken -- a fifth collision is exactly what this instrument exists to avoid. This class
takes 1798 and 1799.

WHAT THIS DOES NOT DO. r3-wl also repaired the Register's front-matter counts and recomputed the
kinds table. **M's Ruling A parks that repair: the entries stand, the repair waits.** So:
  - the two count sites are NOT touched;
  - `kinds.py --write` is NOT run;
  - main L7373's extent phrase is NOT touched.
The staleness those leave is a FINDING, already carried as reg1-04, and this instrument SCORES it
rather than asserting it. r3-wl exits 1 on the current gate precisely because it asserts the extent
as an invariant; extent is data (HANDOFF-152-RESUME section 5).

Usage:  python3 r3-wl2.py            dry run: everything in memory, nothing written
        python3 r3-wl2.py --write    writes /home/claude/build93/<members> and the BUILD93 bundle
"""
import os, re, sys, hashlib, tempfile

MEM = '/home/claude/members/'; HOME = '/home/claude/'
OLD_BUNDLE = HOME + 'The_Method_1_6_BUILD92_main_and_register.md'
OLD_MD5 = 'ac49200f5a8a02511865260202e75cbb'
NEW_BUNDLE = HOME + 'The_Method_1_6_BUILD93_main_and_register.md'
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
OUT = HOME + 'build93/' if WRITE else tempfile.mkdtemp(prefix='r3wl2-dry-') + '/'
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

old_main = open(MEM + MAIN, 'rb').read(); old_reg = open(MEM + REG, 'rb').read()
m = old_main.decode('utf-8'); r = old_reg.decode('utf-8'); ML = m.split('\n')
print(f'old {MAIN}  {len(old_main):,} B  md5 {md5(old_main)}  {old_main.count(chr(10).encode()):,} lines')
print(f'old {REG}  {len(old_reg):,} B  md5 {md5(old_reg)}  {old_reg.count(chr(10).encode()):,} lines')

def S(L, n, must):
    l = L[n - 1]; assert must in l, f'L{n} does not carry {must!r}: {l[:90]!r}'; return l
def col(l, old, new):
    assert l.count(old) == 1, (old, l[:80]); return l.replace(old, new)
def wrap(s, w=98):
    import textwrap
    return '\n'.join(textwrap.wrap(s, width=w, break_long_words=False, break_on_hyphens=False))

# ---------------------------------------------------------------- numbering, MEASURED not assumed
seated = sorted(int(x) for x in re.findall(r'^### (\d+)$', r, re.M))
HI = max(seated)
assert HI == 1796, f'highest seated entry is {HI}, not 1796 — re-read the numbering before running'
A, B = 1798, 1799
assert not re.search(r'^### 179[789]\b', r, re.M), '1797/1798/1799 already seated'
print(f'entries seated: {len(seated)}  highest: {HI}  1797 left staged  this class takes: {A}, {B}')

# ---------------------------------------------------------------- the sites, asserted by content
PARA = wrap("**Status.** The ν rule is a form, the first the corridor was applied to, and not a law: register 1460 "
            "deactivates it as a law and retains it as a form. Placed at each step's own corridor it reproduces 99 of "
            "106 steps (registers 1437, 1438); held out — *a* placed only from corridors already revealed — it "
            "reproduces 90, against 96 for Madelung's rule with no parameter at all (register 1445), and that is how "
            "its standing is quoted. What survives untouched is the corridor: non-empty at every one of the 106 steps, "
            "which is a statement about the form (registers 1445, 1463). The derivation that answers Löwdin is "
            "Chapter 35's.")
l9607 = S(ML, 9607, 'reproduces the order.'); l9609 = S(ML, 9609, '### 34.5 The corridor')
l9659 = S(ML, 9659, '**No parameter is fitted.**'); l9661 = S(ML, 9661, '### 34.9 Domain, stated by the law itself')
l9663 = S(ML, 9663, '**Exceptionless on 106 elements**, Z = 3 to 108, including every aufbau anomaly,')
l9664 = S(ML, 9664, '**and right where n+ℓ is wrong.**')
l9718 = S(ML, 9718, '*Chapter 34 stated the law that names the order — the corridor, the walk, and the')
l9731 = S(ML, 9731, 'operator.* Chapter 34 then measured the consequence — with no carried state, 104')
l9732 = S(ML, 9732, 'of 106 steps admit two to four self-consistent subshells, so **the table is not')
l9733 = S(ML, 9733, "computable from a single atom's configuration.** The solution is the operator")
l9742 = S(ML, 9742, 'Chapter 34 proved necessary is here carried by the equation itself.*')
l10850 = S(ML, 10850, 'the corridor, 106 consistent inequalities')
l10851 = S(ML, 10851, 'the nineteen surds, the complete endpoint set')
l10856 = S(ML, 10856, 'the necessity of state, 104 of 106 steps')
for n in (9608, 9660, 9662, 9665): assert ML[n - 1] == '', f'L{n} not blank'

SUBS_MAIN = [
 ('item 1  §34.4 status paragraph after L9607', l9607 + '\n\n' + l9609 + '\n', l9607 + '\n\n' + PARA + '\n\n' + l9609 + '\n'),
 ('item 2  §34.8 L9659', l9659 + '\n',
  '**No parameter is fitted in the form;** the placement of *a* along the walk is a fit (register 1445).\n'),
 ('item 3  §34.9 heading L9661', l9661 + '\n', '### 34.9 Domain, stated by the form itself\n'),
 ('item 3  §34.9 L9663-L9664', l9663 + '\n' + l9664 + '\n',
  "**A non-empty corridor at all 106 elements**, Z = 3 to 108, including every aufbau anomaly — and 99 of 106 steps reproduced when *a* is placed on each step's own corridor,\n"
  '90 held out (registers 1437, 1445), **right at eight of the ten elements where n+ℓ is wrong.**\n'),
 ('item 4  §35 L9718', l9718 + '\n',
  '*Chapter 34 stated the form that names the order, and the corridor that tests a form — the corridor, the walk, and the\n'),
 ('item 7  §35.1 L9731-L9733', l9731 + '\n' + l9732 + '\n' + l9733 + '\n',
  'operator.* Chapter 34 then stated the consequence — without carried state **the table is not\n'
  "computable from a single atom's configuration** (register 1332; the count itself is not independently\n"
  'reproducible, register 1448). The solution is the operator\n'),
 ('item 7  §35.1 L9742', l9742 + '\n', 'Chapter 34 argued necessary is here carried by the equation itself.*\n'),
 ('item 5  Appendix L10850', l10850 + '\n', col(l10850, 'verified · exhaustive · none found', 'verified as a result about the form (1445, 1463)') + '\n'),
 ('item 5  Appendix L10851', l10851 + '\n', col(l10851, 'measured · exhaustive · none found', 'withdrawn with ν at 1460') + '\n'),
 ('item 5  Appendix L10856', l10856 + '\n', col(l10856, 'verified · exhaustive · none found', 'stated at 1332; not independently reproducible (1448)') + '\n'),
]

EA = (f"### {A}\n\n**CHAPTER 34'S STATUS CORRECTED TO THE RECORD'S.** *The chapter printed ν as the law and its walk "
      "as exceptionless on 106 elements; registers 1437, 1438, 1445 and 1460 had measured 99 in sample and 90 held out "
      "against Madelung's 96 and deactivated ν as a law. Corrected at §34.4, §34.8, §34.9 and §35's opening; the "
      "corridor's non-emptiness at 106 of 106 stands as a result about the form (1445, 1463).* "
      "Registers 1350; 1437; 1438; 1445; 1460; 1463. (a correction.)\n")
EB = (f"### {B}\n\n**THE APPENDIX ROWS FOLLOW THE STATUS.** *Appendix rows for the nineteen surds and the necessity of "
      "state carried 'measured' and 'verified'; the first demotes with ν (1460) and the second is stated at 1332 and not "
      "independently reproducible (1448). Status columns corrected.* Registers 1332; 1448; 1460. (a correction.)\n")
TAIL = '\n' + EA + '\n' + EB
assert r.endswith('\n') and not r.endswith('\n\n'), 'Register tail form changed'

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

new_m = apply(m, SUBS_MAIN); assert md5(reverse(new_m, SUBS_MAIN).encode('utf-8')) == md5(old_main), 'main reverse FAILED'
new_r = r + TAIL
assert new_r[:-len(TAIL)] == r, 'Register is not old + tail'
print(f'main: {len(SUBS_MAIN)} substitutions, reverse recovers md5 {md5(old_main)} == old: True')
print(f'Register: 0 substitutions + 2 entries appended, old bytes untouched: True')

NL = new_m.split('\n'); k = len(NL) - len(ML)
print(f'main line shift: +{k} for BUILD92 L >= 9608')
pre = [i + 1 for i in range(9607) if NL[i] != ML[i]]
assert pre == [], f'no pre-shift change is permitted under Ruling A; got {pre}'
print('changed lines after the shift (BUILD93 = BUILD92 + %d):' % k,
      [i + 1 for i in range(9607 + k, len(NL)) if NL[i] != ML[i - k]])

# ---------------------------------------------------------------- the parked repair: SCORED, never asserted
def count_sites(text):
    return {n: l for n, l in enumerate(text.split('\n'), 1) if re.search(r'\d[\d,]* entries, 1 to \d+|entries, 1 to', l)}
kinds_printed = int(re.search(r'\| \*\*a correction\*\* \| ([\d,]+) \|', new_r).group(1).replace(',', ''))
# Ask the seated instrument for the count; never reimplement its rule (it imports, it does not copy).
import subprocess
_tmp = tempfile.mkdtemp(prefix='r3wl2-kinds-') + '/REG-for-kinds.md'
open(_tmp, 'w', encoding='utf-8').write(new_r)
_k = subprocess.run(['python3', MEM + 'kinds.py', _tmp], capture_output=True, text=True, timeout=200)
assert _k.returncode == 0, _k.stderr[-300:]
counted = int(re.search(r"'a correction': (\d+)", _k.stdout).group(1))
os.remove(_tmp)
print(f'PARKED (Ruling A), scored not repaired:')
print(f'  entries now 1 to {B}; the front matter still prints its BUILD180 extent — reg1-04 carries this')
print(f'  kinds table prints "a correction" {kinds_printed}; kinds.py counts {counted} on the new member — stale by {counted - kinds_printed}')
for n, l in sorted(count_sites(new_r).items())[:3]:
    print(f'  count site L{n}: {l[:96]}')
assert 'a correction' in new_r, 'kinds table missing'

# ---------------------------------------------------------------- press anchors must survive
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, m, new_m), (REG, r, new_r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:44], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print(f'build.py SUBS anchors on {v}: {len(anchors)} checked; count changed by this edit: {moved}')
    assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- the bundle
if WRITE: assert not os.path.exists(OUT), f'{OUT} exists'; os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
new_main_b = new_m.encode('utf-8'); new_reg_b = new_r.encode('utf-8')
open(OUT + MAIN, 'wb').write(new_main_b); open(OUT + REG, 'wb').write(new_reg_b)

old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD92 bundle md5 mismatch'
ms = dict((mm.group(1).decode(), mm.group(2)) for mm in MEMBER.finditer(old_b))
assert ms[MAIN] == old_main and ms[REG] == old_reg, 'seated bodies are not the ones edited'
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
new_b = old_b
for n, nb in ((MAIN, new_main_b), (REG, new_reg_b)):
    ob = block(n, ms[n]); assert new_b.count(ob) == 1; new_b = new_b.replace(ob, block(n, nb))
rev_b = new_b
for n, nb in ((MAIN, new_main_b), (REG, new_reg_b)):
    assert rev_b.count(block(n, nb)) == 1; rev_b = rev_b.replace(block(n, nb), block(n, ms[n]))
assert md5(rev_b) == OLD_MD5, 'bundle reverse FAILED'
print(f'bundle reverse recovers md5 {md5(rev_b)}  == old: True')
print(f'new {MAIN}  {len(new_main_b):,} B  md5 {md5(new_main_b)}')
print(f'new {REG}  {len(new_reg_b):,} B  md5 {md5(new_reg_b)}')
print(f'new bundle BUILD93  {len(new_b):,} B  md5 {md5(new_b)}  {new_b.count(chr(10).encode()):,} lines  {len(ms)} members')
if WRITE:
    assert not os.path.exists(NEW_BUNDLE), f'{NEW_BUNDLE} exists — never overwrite'
    open(NEW_BUNDLE, 'wb').write(new_b); print('written', NEW_BUNDLE, 'and', OUT)
else:
    print('DRY RUN — nothing written under /home/claude')
