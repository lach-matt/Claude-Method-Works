#!/usr/bin/env python3
"""r3-reg1g.py — R3: reg1-G/H/I, the Register front matter's citation figures and its load-bearing table,
re-taken from the seated tool; entry 1815's count class moved with the recording entry. BUILD102 -> BUILD103 main.

READ-reg104 (ii) left this class named and untouched: the front matter's citation paragraph (L35) and table
(L37–L48) and the citation sentence at L70 are printed figures whose writer, `register_cites.py`, is a seated
member that prints and never writes. Printed: 571 entries cited by other entries, recomputed 2026-08-26; the 11
cited seven times or more; 387 / 701 / 970 for the main volume, the compendia and papers, and the whole record.
`r2-reg1a2` records them as deviations reg1-G / reg1-H / reg1-I.

THE CLASS is every figure that tool prints, and only those:
  Register L35   the cited-by-entries total, the recount date, the size of the ≥7 set
  Register L37+  the table: one row per entry cited seven times or more, its count, its own headline in sentence case
  Register L70   cited in main; counting the four compendia and the two papers; counting citations by other entries
plus entry 1815's class, which every appended entry moves and which is re-taken in the same build:
  Register L6, L65, the kinds table (register_counts.py, kinds.py); main L7378, L7663, L7666.

Every figure is the seated tool's own output — `register_cites.py` run unmodified (runpy, run_name='__main__')
in a staging directory holding the Register AS IT WILL STAND with entry 1816 appended beside the other volumes —
because the entry that records a count is itself an entry. Two of the tool's conventions the printed sentence did
not state are stated at the entry: the superseded stretch 95–164 is not counted as a citer, and a range counts
each entry it spans. The eleven printed rows keep their text (each is its entry's headline in sentence case);
the two rows the recount reaches for the first time carry their entries' headlines the same way, asserted
against the headline case-insensitively. Rows are ordered by count, then entry number.

Ruling chat-153 item 3: restating a count the record has moved is structural; the table's membership follows the
count. Both states are kept at entry 1816 (Ruling 29's purpose). The one build.py anchor the date moves is asserted
to be the only one and recorded at the entry. Line shift: none in the main volume; the Register
+2 in the table, +4 for the entry.

Usage:  python3 r3-reg1g.py            dry run
        python3 r3-reg1g.py --write    writes staging members + the BUILD103 bundle
"""
import os, sys, hashlib, re, runpy, tempfile, subprocess, io, contextlib, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD102_main_and_register.md')
OLD_MD5 = '5d7c0c9b2bc3758be14c608065deae08'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD103_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build103') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')
assert r.count('### 1816\n') == 0 and r.rstrip().endswith('Registers 1736; 1762; 1793–1796; 1813. (a correction.)')

E1816 = """

### 1816

**THE FRONT MATTER'S CITATION FIGURES AND ITS LOAD-BEARING TABLE ARE RE-TAKEN FROM THE SEATED TOOL; THE TABLE KEEPS ITS ELEVEN ROWS AND GAINS TWO.** *reg1-G / H / I, READ-reg104 (ii): the front matter printed 571 entries cited by other entries, recomputed by register_cites.py on 2026-08-26, and 387 / 701 / 970 for the main volume, the compendia and papers, and the whole record; its table printed the eleven cited seven times or more — 1460 and 1475 at 10×, 784, 1581, 1649, 1664 and 1578 at 9×, 1020 and 1445 at 8×, 1462 and 1595 at 7×. Every entry appended since that recount cited without any sentence counting it. Re-taken here by running the seated tool, unmodified, on the Register as it stands with this entry counted: 651 entries are cited by other entries, this one citing 1815; 407 in the main volume, 879 counting the four compendia and the two papers, 1,077 counting citations by other entries; thirteen entries reach seven citations — the eleven, each cited at least as often as before, and two the recount reaches for the first time, 1448 and 1526 at 8×. Two conventions of the tool the printed sentence did not state are stated now: the superseded stretch 95–164 is not counted as a citer, and a range counts each entry it spans. The prior figures stand in this entry; the table's third column is each entry's own headline in sentence case and is not rewritten for the eleven. The count sentences of entry 1815's class move with this entry, as they will with every entry, and are re-taken in the same build. One press anchor moves with the date: build.py's substitution that strips the tool's name from this sentence for the print edition anchors on the old date, and the press's anchor list is the press's to move (docket 38's class); recorded here so the print edition is not silently different.* Registers 1815. (a correction.)
"""
def with_entry(text): return text.rstrip() + E1816 + '\n'

# ---- the seated tools, run on the Register as it will stand -------------------------------------------------
stage = tempfile.mkdtemp(prefix='r3-reg1g-')
for f in os.listdir(MEM):
    if f.endswith('.md') and f != REG: os.symlink(MEM + f, os.path.join(stage, f))
open(os.path.join(stage, REG), 'w', encoding='utf-8').write(with_entry(r))
cwd = os.getcwd(); os.chdir(stage); buf = io.StringIO()
with contextlib.redirect_stdout(buf): G = runpy.run_path(MEM + 'register_cites.py', run_name='__main__')
os.chdir(cwd)
byent, bymain, comp = G['byent'], G['bymain'], G['comp']
CITED_BY_ENTRIES = len(byent); CITED_MAIN = len(bymain); CITED_MAIN_COMP = len(set(bymain) | set(comp)); CITED_ANY = len(byent + bymain + comp)
TOP = sorted(((n, k) for n, k in byent.items() if k >= 7), key=lambda t: (-t[1], t[0]))
print('register_cites.py with 1816: cited by entries %d | main %d | main+companions %d | anywhere %d | >=7: %s' % (CITED_BY_ENTRIES, CITED_MAIN, CITED_MAIN_COMP, CITED_ANY, TOP))
spec = importlib.util.spec_from_file_location('register_counts', MEM + 'register_counts.py'); rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
c = rc.count(with_entry(r))
kout = subprocess.run([sys.executable, MEM + 'kinds.py', os.path.join(stage, REG)], capture_output=True, text=True, cwd=MEM).stdout.split('\n')[0]
K_N = int(kout.split()[0]); K = eval(kout[kout.index('{'):])
print('register_counts with 1816: headings %d, highest %d, mature %d;  kinds.py: %d %s' % (c['headings'], c['highest'], c['mature'], K_N, K))
for f in os.listdir(stage): os.unlink(os.path.join(stage, f))
os.rmdir(stage)

# ---- the measured figures, pinned so a drifted store refuses rather than prints something else ----------------
assert (CITED_BY_ENTRIES, CITED_MAIN, CITED_MAIN_COMP, CITED_ANY) == (651, 407, 879, 1077), (CITED_BY_ENTRIES, CITED_MAIN, CITED_MAIN_COMP, CITED_ANY)
assert TOP == [(1460, 21), (1445, 14), (1475, 10), (1649, 10), (784, 9), (1578, 9), (1581, 9), (1664, 9), (1020, 8), (1448, 8), (1526, 8), (1462, 7), (1595, 7)], TOP
assert (c['headings'], c['highest'], c['mature'], K_N) == (1658, 1816, 1494, 1588), (c, K_N)
assert (K['a finding'], K['a correction'], K['a measurement'], K['a new protocol']) == (1359, 169, 501, 24), K

# ---- the table: the eleven rows' text as printed, two rows from their entries' headlines -----------------------
OLD_TABLE_START = '| entry | cited | what it established |\n|---|---|---|\n'
i0 = r.index(OLD_TABLE_START); i1 = r.index('\n\n', i0)
old_table = r[i0:i1 + 1]
rows = {}
for line in old_table.strip().split('\n')[2:]:
    n, k, what = [x.strip() for x in line.strip('|').split('|')]
    rows[int(n.strip('*'))] = what
assert len(rows) == 11 and sorted(rows) == [784, 1020, 1445, 1460, 1462, 1475, 1578, 1581, 1595, 1649, 1664]
NEW_ROWS = {1448: "But the run does not generate, and the per-atom fixed point is vacuous — a check I built without asking whether it could fail",
            1526: "A user-supplied URL breaks the cache, and the second capture caught four fabricated values in the first"}
def headline(n):
    body = r.split('\n### %d\n' % n, 1)[1]
    return re.match(r'\s*\*\*(.+?)\*\*', body, re.S).group(1).strip()
norm = lambda s: re.sub(r'\W', '', s).casefold()   # case and punctuation aside (1020's row has ';' for the headline's '.')
for n, what in NEW_ROWS.items():
    assert norm(headline(n)) == norm(what), (n, headline(n))
for n, what in rows.items():   # the eleven: the printed text IS the headline in sentence case (checked, not rewritten)
    assert norm(headline(n)) == norm(what), (n, headline(n))
rows.update(NEW_ROWS)
new_table = OLD_TABLE_START + ''.join('| **%d** | %d× | %s |\n' % (n, k, rows[n]) for n, k in TOP)
assert r.count(old_table) == 1; r = r.replace(old_table, new_table)

RSUBS = [
 ('**571 entries are cited by other entries.**', '**%d entries are cited by other entries.**' % CITED_BY_ENTRIES),
 ('Recomputed from this file by `register_cites.py` (2026-08-26).*', 'Recomputed from this file by `register_cites.py` (2026-09-04).*'),
 ('the 11 cited seven times or more:', 'the %d cited seven times or more:' % len(TOP)),
 ('**387 entries are cited in the main volume\'s chapters and appendices; 701 counting the four compendia and the two papers; 970 counting citations by other entries.**',
  '**%d entries are cited in the main volume\'s chapters and appendices; %d counting the four compendia and the two papers; %s counting citations by other entries.**' % (CITED_MAIN, CITED_MAIN_COMP, g(CITED_ANY))),
 # entry 1815's class, moved by this entry
 ('**1657 entries, 1 to 1815.** *Entries 1 to 94', '**%d entries, 1 to %d.** *Entries 1 to 94' % (c['headings'], c['highest'])),
 ('and 165 to 1815, 1,493 entries, are the mature record', 'and 165 to %d, %s entries, are the mature record' % (c['highest'], g(c['mature']))),
 ('**1657 entries, 1 to 1815** (genesis 1–94, superseded 95–164, mature record 165–1815).', '**%d entries, 1 to %d** (genesis 1–94, superseded 95–164, mature record 165–%d).' % (c['headings'], c['highest'], c['highest'])),
 ('| **a correction** | 168 | 370 |', '| **a correction** | %s | 370 |' % g(K['a correction'])),
 ('by `kinds.py` over the 1,587 entry headings,', 'by `kinds.py` over the %s entry headings,' % g(K_N)),
]
MSUBS = [
 ('1,657 entries, 1 to 1815, at this build (2026-09-04)', '%s entries, 1 to %d, at this build (2026-09-04)' % (g(c['headings']), c['highest'])),
 ('436 entries when this paragraph was written, 1,657 at this build', '436 entries when this paragraph was written, %s at this build' % g(c['headings'])),
]
assert m.count('at this build the main volume cites %d entries' % CITED_MAIN) == 1, 'main L7666 cites-count moved'
for i, (o, n) in enumerate(RSUBS, 1):
    k = r.count(o); print('Register site %d: anchor occurs %d time(s) -> %s' % (i, k, n[:70])); assert k == 1 and o != n; r = r.replace(o, n)
for i, (o, n) in enumerate(MSUBS, 1):
    k = m.count(o); print('main site %d: anchor occurs %d time(s) -> %s' % (i, k, n[:70])); assert k == 1 and o != n; m = m.replace(o, n)
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
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved))
    # ONE press anchor moves by design and is recorded, not hidden: build.py L214 strips "by `register_cites.py`" from the
    # recount sentence for the print edition and anchors on the old date with it. The recount date is the figure's own
    # state and moves with the figure; the press's anchor list is the press's to move (docket 38's class; entry 1816).
    assert [x[0] for x in moved] == ([] if v == MAIN else ['Recomputed from this file by `register_c']), moved

if WRITE: assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD102 md5 mismatch'
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
print('new BUILD103  %s B  md5 %s  %s lines  %d members' % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE); open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else: print('DRY RUN — nothing installed')
