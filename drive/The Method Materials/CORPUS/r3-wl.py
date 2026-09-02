#!/usr/bin/env python3
"""r3-wl.py — R3 class WL (16z-01), the withdrawn-law status repair: BUILD90 -> BUILD91 main (chat 128).

Executes RULINGS-R2.md chat-127 item 4 on M's approval in chat 128 ("Approved": R3-CLASS-WL.md items 1-6 as put,
item 7 for L9731-L9732 and L9742 added in chat 128; the L9664 clause measured against register 1437, eight of ten).
Status sentences only; no mathematics is rewritten. Count-asserted substitutions (build.py's sweep discipline, G0x)
on the two main-bundle members; the Register grown by 1793-1794 in the Register's own entry form; kinds.py --write
recounts the kinds table; the extent and count sites are driven to their fixed point; a reverse guard recovers
each old member's md5 and the old bundle's md5 from the new bytes before anything is written.

Usage:  python3 r3-wl.py            dry run: everything in memory, kinds recount on a /tmp copy, nothing under /home/claude written
        python3 r3-wl.py --write    writes /home/claude/build91/<members> and the BUILD91 bundle (refuses to overwrite)
Reads MEMBERS from /home/claude/members (BUILD90 state); line numbers below are BUILD90 line numbers, asserted by content.
"""
import os, re, sys, hashlib, subprocess, textwrap, tempfile
MEM = '/home/claude/members/'; HOME = '/home/claude/'
OLD_BUNDLE = HOME + 'The_Method_1_6_BUILD90_main_and_register.md'; OLD_MD5 = '49065309b0c4fe8e055f693aed295cca'
NEW_BUNDLE = HOME + 'The_Method_1_6_BUILD91_main_and_register.md'
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
VOLS = [MAIN, REG, 'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md']
WRITE = '--write' in sys.argv
OUT = HOME + 'build91/' if WRITE else tempfile.mkdtemp(prefix='r3wl-dry-') + '/'   # dry run: a fresh scratch dir each run
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

old_main = open(MEM + MAIN, 'rb').read(); old_reg = open(MEM + REG, 'rb').read()
m = old_main.decode('utf-8'); r = old_reg.decode('utf-8'); ML = m.split('\n'); RL = r.split('\n')
print(f'old {MAIN}  {len(old_main):,} B  md5 {md5(old_main)}  {old_main.count(b"\n"):,} lines')
print(f'old {REG}  {len(old_reg):,} B  md5 {md5(old_reg)}  {old_reg.count(b"\n"):,} lines')

def S(L, n, must):
    l = L[n - 1]; assert must in l, f'L{n} does not carry {must!r}: {l[:90]!r}'; return l
def col(l, old, new):
    assert l.count(old) == 1, (old, l[:80]); return l.replace(old, new)
def wrap(s, w=98):
    return '\n'.join(textwrap.wrap(s, width=w, break_long_words=False, break_on_hyphens=False))

# ---------------------------------------------------------------- main volume: the sites, asserted by content
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
l7373 = S(ML, 7373, '1,635 entries, 1 to 1792, at this build (2026-08-29)')
for n, l in ((9608, ML[9607]), (9660, ML[9659]), (9662, ML[9661]), (9665, ML[9664])): assert l == '', f'L{n} not blank'

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
 ('extent  main L7373', l7373 + '\n', col(l7373, '1,635 entries, 1 to 1792, at this build (2026-08-29)', '1,637 entries, 1 to 1794, at this build (2026-09-01)') + '\n'),
]

# ---------------------------------------------------------------- Register: count/extent sites and the two entries
l6 = S(RL, 6, '**1635 entries, 1 to 1792.**')
l65 = S(RL, 65, '**1635 entries, 1 to 1792** (genesis 1–94, superseded 95–164, mature record 165–1792)')
E1793 = ("### 1793\n\n**CHAPTER 34'S STATUS CORRECTED TO THE RECORD'S.** *The chapter printed ν as the law and its walk as "
         "exceptionless on 106 elements; registers 1437, 1438, 1445 and 1460 had measured 99 in sample and 90 held out "
         "against Madelung's 96 and deactivated ν as a law. Corrected at §34.4, §34.8, §34.9 and §35's opening; the "
         "corridor's non-emptiness at 106 of 106 stands as a result about the form (1445, 1463).* "
         "Registers 1350; 1437; 1438; 1445; 1460; 1463. (a correction.)\n")
E1794 = ("### 1794\n\n**THE APPENDIX ROWS FOLLOW THE STATUS.** *Appendix rows for the nineteen surds and the necessity of "
         "state carried 'measured' and 'verified'; the first demotes with ν (1460) and the second is stated at 1332 and not "
         "independently reproducible (1448). Status columns corrected.* Registers 1332; 1448; 1460. (a correction.)\n")
if '--as-put' in sys.argv:   # the wording exactly as approved, before the L10851 'measured' correction was raised
    E1794 = E1794.replace("carried 'measured' and 'verified'", "carried 'verified'")
TAIL = '\n' + E1793 + '\n' + E1794
SUBS_REG = [
 ('extent  Register L6', l6 + '\n', col(col(l6, '**1635 entries, 1 to 1792.**', '**1637 entries, 1 to 1794.**'),
                                        'and 165 to 1791, 1,470 entries, are the mature record', 'and 165 to 1794, 1,472 entries, are the mature record') + '\n'),
 ('extent  Register L65', l65 + '\n', col(l65, '**1635 entries, 1 to 1792** (genesis 1–94, superseded 95–164, mature record 165–1792)',
                                          '**1637 entries, 1 to 1794** (genesis 1–94, superseded 95–164, mature record 165–1794)') + '\n'),
]
assert r.endswith('(a correction.)\n') and not r.endswith('\n\n'), 'Register tail form changed'
assert not re.search(r'^### 179[34]\b', r, re.M), 'entries 1793/1794 already exist'

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
new_r = apply(r, SUBS_REG) + TAIL
assert new_r.endswith(TAIL) and md5(reverse(new_r[:-len(TAIL)], SUBS_REG).encode('utf-8')) == md5(old_reg), 'Register reverse FAILED'
print(f'main: {len(SUBS_MAIN)} substitutions, reverse recovers md5 {md5(old_main)} == old: True')
print(f'Register: {len(SUBS_REG)} substitutions + 2 entries, reverse recovers md5 {md5(old_reg)} == old: True')
NL = new_m.split('\n'); k = len(NL) - len(ML); print(f'main line shift: +{k} for BUILD90 L >= 9608 (PARA is {PARA.count(chr(10)) + 1} lines + 1 blank)')
pre = [i + 1 for i in range(9607) if NL[i] != ML[i]]; assert pre == [7373], f'unexpected pre-shift changes {pre}'
diff = [i + 1 for i in range(9607 + k, len(NL)) if NL[i] != ML[i - k]]
print('changed lines before the shift:', pre, '; after the shift (BUILD91 numbering = BUILD90 + %d):' % k, diff)

# ---------------------------------------------------------------- write the member copies; kinds.py --write on the new Register copy
if WRITE: assert not os.path.exists(OUT), f'{OUT} exists'; os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m.encode('utf-8')); open(OUT + REG, 'wb').write(new_r.encode('utf-8'))
p = subprocess.run(['python3', MEM + 'kinds.py', OUT + REG, '--write'], capture_output=True, text=True, timeout=200)
print('kinds.py --write:', p.stdout.strip(), p.stderr.strip()[-300:])
assert p.returncode == 0
p0 = subprocess.run(['python3', MEM + 'kinds.py', MEM + REG], capture_output=True, text=True, timeout=200)
print('kinds.py on BUILD90:', p0.stdout.strip())
final_r = open(OUT + REG, 'rb').read().decode('utf-8'); FL = final_r.split('\n'); NR = new_r.split('\n')
assert len(FL) == len(NR)
kdiff = [i + 1 for i in range(len(NR)) if FL[i] != NR[i]]
print('kinds.py changed Register lines:', kdiff)
for i in kdiff: print(f'   L{i}: {NR[i-1][:70]!r} -> {FL[i-1][:70]!r}')
assert all(re.match(r'\| \*\*', NR[i - 1]) or 'entry headings' in NR[i - 1] for i in kdiff), 'kinds.py touched a line outside its table'
# reverse from the final Register bytes: restore kinds lines, strip the tail, reverse the two substitutions
rev = FL[:]
for i in kdiff: rev[i - 1] = NR[i - 1]
rev = '\n'.join(rev); assert rev == new_r
assert md5(reverse(rev[:-len(TAIL)], SUBS_REG).encode('utf-8')) == md5(old_reg)
final_reg_b = final_r.encode('utf-8'); new_main_b = new_m.encode('utf-8')
print(f'Register (final): reverse from the written bytes recovers md5 {md5(old_reg)} == old: True')

# ---------------------------------------------------------------- fixed-point checks over the six volumes (new texts for the two, seated for the four)
texts = {v: (new_m if v == MAIN else final_r if v == REG else open(MEM + v, encoding='utf-8').read()) for v in VOLS}
def sites(pat):
    return {v.split('___')[-1].replace(MAIN, 'main'): [i + 1 for i, l in enumerate(t.split('\n')) if re.search(pat, l)] for v, t in texts.items()}
for pat in (r'1 to 1794', r'1 to 1792', r'\b1,?635 entries\b', r'\b1,?637 entries\b', r'stated by the law itself', r'stated by the form itself',
            r'Exceptionless on 106', r'165 to 179\d|165–179\d', r'1,47[02] entries'):
    s = sites(pat); print(f'{pat!r}: ' + ' '.join(f'{v}:{n}' for v, ns in s.items() for n in ns) if any(s.values()) else f'{pat!r}: 0 sites')
# build.py press-time SUBS anchors must survive (each still exactly once in the new member texts)
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}; exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt in ((MAIN, m), (REG, r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    stale_old = [(a[:50], oldt.count(a)) for a in anchors if oldt.count(a) != 1]
    moved = [(a[:50], oldt.count(a), texts[v].count(a)) for a in anchors if oldt.count(a) != texts[v].count(a)]
    print(f'build.py SUBS anchors on {v}: {len(anchors)} checked; already not unique at BUILD90: {len(stale_old)} {stale_old}; count changed by this edit: {moved}')
    assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- the bundle: replace the two member bodies; reverse guard; write
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD90 bundle md5 mismatch'
ms = [(mm.group(1).decode(), mm.group(2)) for mm in MEMBER.finditer(old_b)]; assert [n for n, _ in ms] in ([MAIN, REG], [REG, MAIN]), [n for n, _ in ms]
assert dict(ms)[MAIN] == old_main and dict(ms)[REG] == old_reg
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
new_b = old_b
for n, nb in ((MAIN, new_main_b), (REG, final_reg_b)):
    ob = block(n, dict(ms)[n]); assert new_b.count(ob) == 1; new_b = new_b.replace(ob, block(n, nb))
rev_b = new_b
for n, nb in ((MAIN, new_main_b), (REG, final_reg_b)):
    assert rev_b.count(block(n, nb)) == 1; rev_b = rev_b.replace(block(n, nb), block(n, dict(ms)[n]))
print(f'bundle reverse recovers md5 {md5(rev_b)}  == old: {md5(rev_b) == OLD_MD5}'); assert md5(rev_b) == OLD_MD5
print(f'new {MAIN}  {len(new_main_b):,} B  md5 {md5(new_main_b)}  {new_main_b.count(b"\n"):,} lines')
print(f'new {REG}  {len(final_reg_b):,} B  md5 {md5(final_reg_b)}  {final_reg_b.count(b"\n"):,} lines')
print(f'new bundle BUILD91  {len(new_b):,} B  md5 {md5(new_b)}  {new_b.count(b"\n"):,} lines  2 members')
if WRITE:
    assert not os.path.exists(NEW_BUNDLE), f'{NEW_BUNDLE} exists — never overwrite'
    open(NEW_BUNDLE, 'wb').write(new_b); print('written', NEW_BUNDLE, 'and', OUT)
else:
    print('DRY RUN — nothing written under /home/claude; BUILD90 stays live (class HELD, chat 128)')
