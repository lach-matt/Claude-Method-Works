#!/usr/bin/env python3
"""r3-reg104.py — R3: reg1-04, the Register's own extent and counts, repaired with its class. BUILD101 -> BUILD102 main.

M's sequencing (DEF-153J, RUL-153): readings first, then reg1-04's front-matter count repair, which
HANDOFF-152-RESUME records as R3's to make ("R3 repairs it with its class"). The readings estate closed at
BUILD208 (W-214); Ruling A — no front-matter count touched, `kinds.py --write` not run — held until then and
is discharged here.

THE CLASS is every sentence a seated tool recomputes about the Register's size, and only those:
  Register L6   the front matter's total and extent, and its mature record   — `register_counts.py --write`
  Register L65  the back matter's total, extent and mature range              — `register_counts.py --write`
  Register L22–L26, L31  the kind-count table's Build 16 column and its heading population — `kinds.py --write`
  main L7378    Chapter 28's readout "1,635 entries, 1 to 1792, at this build (2026-08-29)" — the extent, dated
  main L7663    "1,631 at this build" — the same size at an earlier build, the same sentence form
  main L7666    "at this build the main volume cites 392 entries" — `register_cites.py`, entries cited in main
Every replacement below is the tool's own output on the Register as it will stand with entry 1815 appended
(register_counts: 1,657 headings = 1,650 single + 7 grouped, highest 1815, mature 165–1815 at 1,493; kinds:
finding 1,359, correction 168, measurement 501, new protocol 24, over 1,587 entry headings; register_cites:
407 cited in main), applied here as guarded
substitutions rather than by the tools' own writers so that the reverse guard, the build.py anchor check and
the Register entry go in as one build. The three tools keep their own units — the front matter's total counts
grouped headings, `kinds.py` counts the headings it classifies — and the volume is not made consistent between
sentences it never made consistent (register_counts.py's own rule).

NOT TOUCHED, and recorded at entry 1815: fifteen main-volume sentences that write the size in words — "one
thousand six hundred and thirty-five" — as narrative about the work (L20, L89, L104, L202, L523, L646, L3519,
L7372, L7905, L8923, L9060, L9370, L9382, L9387, L10330). §32.1.4.1's rule is that a figure about the book is
true of a state; those name no state and no tool maintains them, and re-typing fifteen sentences is a prose
pass the class does not include. Docket 35 / 38; M's to rule.

Line shift: none in the main volume (every site is a same-line substitution); Register +4 (entry 1815).

Usage:  python3 r3-reg104.py            dry run
        python3 r3-reg104.py --write    writes staging members + the BUILD102 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD101_main_and_register.md')
OLD_MD5 = '18775f12775f6daa24bc86b8bb5c4628'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD102_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build102') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')
assert r.count('### 1815\n') == 0 and r.rstrip().endswith('(a measurement.)')
E1815 = """

### 1815

**THE REGISTER'S OWN COUNTS ARE CURRENT FOR THE FIRST TIME SINCE BUILD90, AND THE THREE UNITS THE VOLUME COUNTS IN ARE NAMED SO THEY ARE NOT MISTAKEN FOR ONE.** *reg1-04, docket 30: the front matter printed 1635 entries, 1 to 1792, with a mature record 165 to 1791 at 1,470, and 94 + 70 + 1,470 = 1,634 against its own total; the back matter printed 165–1792; and every build since BUILD92 appended entries no sentence counted. M's sequencing was readings first, then this repair with its class, and Ruling A held the counts until the readings closed at BUILD208. Repaired here from the seated tools' own output on this store, applied as one guarded build: register_counts.py counts 1,657 headings — 1,650 single and 7 grouped, this entry among them, since the entry that records a count is itself an entry — with the highest entry 1815 and the mature record 165–1815 at 1,493, and the front matter now sums to itself; kinds.py's column reads finding 1,359, correction 168, measurement 501, new protocol 24, over 1,587 entry headings; register_cites.py counts 407 entries cited in the main volume. Chapter 28's dated readout reads 1,657 entries, 1 to 1815, at this build, and its two neighbouring sentences follow.* **Three units, deliberately: the front matter's total counts every heading, grouped headings included; kinds.py counts the headings it classifies; the entry index a reading instrument builds from bare headings counts 1,650. The volume was never consistent between them and is not made so — only the digits move, in each sentence's own convention (register_counts.py's rule).** *Not touched: fifteen main-volume sentences that write the size in words as narrative — one thousand six hundred and thirty-five — at no named state, which no tool maintains; re-typing them is a prose pass this class does not include and is left to M (docket 35 / 38). The three instruments that asserted the extent as an invariant — r2-regsweep, r2-26b, r3-wl — and the two that carried the printed counts as constants — r2-reg1a, r2-reg7a — take successors that read the printed figures as data, seated with this build's close.* Registers 1736; 1762; 1793–1796; 1813. (a correction.)"""

# the counts are taken from the tools by running them on the Register AS IT WILL STAND — with entry 1815 appended —
# because the entry that records the repair is itself an entry (the first draft counted before appending and
# printed a front matter one short of itself, caught by register_counts.py before install)
sys.path.insert(0, MEM)
import importlib.util, subprocess, tempfile
spec = importlib.util.spec_from_file_location('register_counts', MEM + 'register_counts.py'); rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
def with_entry(text): return text.rstrip() + E1815 + '\n'
c = rc.count(with_entry(r))
tmp = tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8'); tmp.write(with_entry(r)); tmp.close()
kout = subprocess.run([sys.executable, MEM + 'kinds.py', tmp.name], capture_output=True, text=True, cwd=MEM).stdout.split('\n')[0]
os.unlink(tmp.name); K_N = int(kout.split()[0]); K = eval(kout[kout.index('{'):])
cites = subprocess.run([sys.executable, MEM + 'register_cites.py'], capture_output=True, text=True, cwd=MEM).stdout
CITED_MAIN = int(re.search(r'entries cited in main: (\d+)', cites).group(1))
print('register_counts with 1815: headings %d (single %d + grouped %d), highest %d, mature %d' % (c['headings'], c['headings'] - c['grouped'], c['grouped'], c['highest'], c['mature']))
print('kinds.py with 1815: %d headings %s' % (K_N, K)); print('register_cites: cited in main %d' % CITED_MAIN)
assert (c['headings'], c['highest'], c['mature'], K_N, CITED_MAIN) == (1657, 1815, 1493, 1587, 407), (c, K_N, CITED_MAIN)
assert (K['a finding'], K['a correction'], K['a measurement'], K['a new protocol']) == (1359, 168, 501, 24), K
g = lambda n: '{:,}'.format(n)
RSUBS = [
 ('**1635 entries, 1 to 1792.** *Entries 1 to 94', '**%d entries, 1 to %d.** *Entries 1 to 94' % (c['headings'], c['highest'])),
 ('and 165 to 1791, 1,470 entries, are the mature record', 'and 165 to %d, %s entries, are the mature record' % (c['highest'], g(c['mature']))),
 ('**1635 entries, 1 to 1792** (genesis 1–94, superseded 95–164, mature record 165–1792).', '**%d entries, 1 to %d** (genesis 1–94, superseded 95–164, mature record 165–%d).' % (c['headings'], c['highest'], c['highest'])),
 ('| **a finding** | 1,356 | 796 |', '| **a finding** | %s | 796 |' % g(K['a finding'])),
 ('| **a correction** | 149 | 370 |', '| **a correction** | %s | 370 |' % g(K['a correction'])),
 ('| **a measurement** | 499 | 299 |', '| **a measurement** | %s | 299 |' % g(K['a measurement'])),
 ('| **a new protocol** | 23 | 67 |', '| **a new protocol** | %s | 67 |' % g(K['a new protocol'])),
 ('by `kinds.py` over the 1,565 entry headings,', 'by `kinds.py` over the %s entry headings,' % g(K_N)),
]
MSUBS = [
 ('1,635 entries, 1 to 1792, at this build (2026-08-29)', '%s entries, 1 to %d, at this build (2026-09-04)' % (g(c['headings']), c['highest'])),
 ('436 entries when this paragraph was written, 1,631 at this build', '436 entries when this paragraph was written, %s at this build' % g(c['headings'])),
 ('at this build the main volume cites 392 entries', 'at this build the main volume cites %d entries' % CITED_MAIN),
]
for i, (o, n) in enumerate(RSUBS, 1):
    k = r.count(o); print('Register site %d: anchor occurs %d time(s) -> %s' % (i, k, n[:60])); assert k == 1; r = r.replace(o, n)
for i, (o, n) in enumerate(MSUBS, 1):
    k = m.count(o); print('main site %d: anchor occurs %d time(s) -> %s' % (i, k, n[:60])); assert k == 1; m = m.replace(o, n)
r = with_entry(r)
p = rc.printed(r); c2 = rc.count(r)
assert (p['front_total'], p['front_highest'], p['front_mature'], p['front_mature_highest'], p['back_mature_highest']) == (c2['headings'], c2['highest'], c2['mature'], c2['highest'], c2['highest']), (p, c2)
assert c2['genesis'] + c2['superseded'] + c2['mature'] == c2['headings'] == p['front_total'], 'the front matter must sum to itself'
print('the front matter sums to itself: %d + %d + %d = %d, highest %d' % (c2['genesis'], c2['superseded'], c2['mature'], c2['headings'], c2['highest']))


new_m = m.encode('utf-8'); new_r = r.encode('utf-8')
print('main %d -> %d B, lines %+d' % (len(old_main), len(new_m), m.count('\n') - old_main.decode('utf-8').count('\n')))
print('reg  %d -> %d B, lines %+d' % (len(old_reg), len(new_r), r.count('\n') - old_reg.decode('utf-8').count('\n')))
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, old_main.decode('utf-8'), m), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved)); assert not moved

if WRITE: assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD101 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(old_b)); assert ms[MAIN] == old_main and ms[REG] == old_reg
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
nb = old_b
for n_, body in ((MAIN, new_m), (REG, new_r)):
    ob = block(n_, ms[n_]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n_, body))
rv = nb
for n_, body in ((MAIN, new_m), (REG, new_r)):
    assert rv.count(block(n_, body)) == 1; rv = rv.replace(block(n_, body), block(n_, ms[n_]))
assert md5(rv) == OLD_MD5, 'bundle reverse FAILED'
print('bundle reverse recovers md5 %s == old: True' % md5(rv))
print('new BUILD102  %s B  md5 %s  %s lines  %d members' % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE); open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else: print('DRY RUN — nothing installed')
