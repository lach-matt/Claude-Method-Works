#!/usr/bin/env python3
# r2-reg1a3.py — R3 (chat 153-R) — SUCCESSOR to r2-reg1a2.py, one token wider: the citation sentence's three figures are
# read as `\d[\d,]*` (with the comma-stripping every other printed figure already had), because reg1-G/H/I's repair
# (register 1816, BUILD103) prints "1,077 counting citations by other entries" in the front matter's own thousands
# convention and the predecessor's `\d+` refused it. Every measurement is identical; on BUILD102 this file's output
# differs from r2-reg1a2.out in exactly the lines the other two changes explain. THREE changes, all re-takes of what
# the predecessor carried as a constant or read from a clipped print: (1) the citation sentence's figures as above;
# (2) the "cited seven times or more" set is taken from register_cites.py's own counter, run unmodified by runpy,
# not from the `top 12` line it prints, which clips the set at twelve — on BUILD102 the predecessor therefore
# scored 1595 as None and "the 11" as 12 where the tool's counter holds 1595 at 7 and thirteen at seven or more,
# a floor of the print and not a fact of the Register; (3) the front matter's bound is its own scan (`### 1` is the
# first heading) and not the literal 75, which reg1-G/H/I's two added table rows moved to 77 (the positional class,
# W-207 / DEF-153N). r2-reg1a2 is seated and never edited in place (chat 68).
# r2-reg1a2.py — R3 (chat 153-R) — SUCCESSOR to r2-reg1a.py, re-TAKEN as DOCKET required: every figure the predecessor
# carried as a printed-value constant (1,635 / 1,792 / 1,470 / 1,565 / the kinds column / 571 / the load-bearing table /
# 387 / 701 / 970) is now READ from the front matter it scores, so the instrument scores the volume against itself at
# any build. Every measurement is identical. On BUILD90 the read figures are the predecessor's constants; on BUILD102,
# after reg1-04's repair (register 1815), the size figures agree and the citation figures the front matter still
# prints from an earlier state are the deviations that remain. r2-reg1a is seated and never edited in place (chat 68).
# r2-reg1a.py — the Register read, unit 1: the FRONT MATTER (Register L1-L74), computable batch.
#
# Opened under M's compendia-scope ruling (staged as the chat-151-B RULINGS block, not yet seated):
# the Register is read in full, in source order, under the chat-81 cadence; the other four compendia
# close by class sweep. This is the first unit of that read and it takes the front matter, because the
# front matter is what every later entry is read against: it fixes the extent, the block boundaries,
# the entry form, the kinds table and the load-bearing table.
#
# The front matter states of itself that its figures are RECOMPUTED AT EVERY PRESS -- "What is
# recomputed from this file at every press is stated where it is printed -- the citation counts and
# the load-bearing table (register_cites.py, 1732), the kinds table below (kinds.py, 1756), and the
# entry form (build.py, 1744)". So the standard this unit scores against is the book's own: a figure
# the book says is recomputed must equal the recomputation. The recomputation is done by the book's
# OWN instruments (kinds.py, register_cites.py) run here, never by an operator of this instrument's
# invention.
#
# CONVENTION ENTRY (docket 30, and stated before anything is scored): an ENTRY is a heading line
# `^### N` or `^### N, N, ...`. On that convention the register holds 1,635 entries -- 1,628 bare and
# 7 grouped -- addressing 1,660 distinct numbers. Counts below are of HEADINGS unless a line says
# "numbers". Getting this wrong is the difference between 1,635 and 1,660 and between 1,470 and 1,495.
#
# FAULTS SELF-CAUGHT AND NAMED (this instrument's, not the book's):
#   fault 1: the mature-record count was first taken over DISTINCT NUMBERS, giving 1,495 for 165-1791
#            against the printed 1,470, and would have recorded a deviation where the book is right.
#            The book counts headings. Both are printed below and the heading convention is the one
#            scored -- it is the convention docket 30 already fixed for "1,635".
#   fault 2: the grouped-heading count was first read off the prose ("the ten grouped headings")
#            rather than measured, which is the error the paragraph itself contains. Measured: 7.
#
# Book-versus-record deviations go through score() and never through the integrity checker check().
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
import os, re, sys, hashlib, subprocess, collections

H = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
def hr(t): print('\n== ' + t)

REG  = 'The_Method_1_6___The_Register-2.md'
MAIN = 'The_Method_1_6-2.md'
VOLS = [MAIN, REG, 'The_Method_1_6___Mathematical_Compendium-2.md',
        'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md',
        'The_Method_1_6___The_Index_of_Indices-2.md']
R = rd(REG); RL = R.split('\n')

FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-58s %-26s %s' % (tag, repr(got), 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def score(tag, got, printed, tagno):
    ok = got == printed
    print('   %-58s %-26s %s' % (tag, repr(got), 'as printed' if ok else 'DEVIATION (%s) - printed %s' % (tagno, repr(printed))))
    if not ok: DEV.append((tagno, tag, got, printed))

hr('0  PROVENANCE')
for n in (REG, MAIN, 'kinds.py', 'register_cites.py'):
    print('   %-46s %8d B  md5 %s' % (n, len(rd(n).encode()), md5(n)))
print('   register lines: %d' % len(RL))

hr('1  THE UNIT, BOUNDED BY ITS OWN SCAN')
first_entry = next(i for i, l in enumerate(RL, 1) if re.match(r'^### 1$', l))
check('front matter runs L1 to the line before the first entry (### 1 is the first heading)', next(i for i, l in enumerate(RL, 1) if re.match(r'^### \d', l)), first_entry)
FM = '\n'.join(RL[:first_entry - 1])
print('   unit = L1-L%d, %d lines, %d B' % (first_entry - 1, first_entry - 1, len(FM.encode())))

# --- the printed figures are DATA, read from the front matter (DOCKET: "r2-reg1a must be re-TAKEN, not re-banked") ---
def _fm_int(pat, text, default=None):
    m = re.search(pat, text); return int(m.group(1).replace(',', '')) if m else default
P_TOTAL   = _fm_int(r'\*\*(\d[\d,]*) entries, 1 to \d+\.\*\*', FM)
P_HIGH    = _fm_int(r'\*\*\d[\d,]* entries, 1 to (\d+)\.\*\*', FM)
P_MAT_HI  = _fm_int(r'and 165 to (\d+), \d[\d,]* entries, are the mature record', FM)
P_MATURE  = _fm_int(r'and 165 to \d+, (\d[\d,]*) entries, are the mature record', FM)
P_BACK_HI = _fm_int(r'mature record 165[–-](\d+)\)', R)
P_KINDS_N = _fm_int(r'over the (\d[\d,]*) entry headings', FM)
P_KINDS   = {k: int(v.replace(',', '')) for k, v in re.findall(r'^\| \*\*(a finding|a correction|a measurement|prior art|a new protocol|a withdrawal|a fault of mine|an open question)\*\* \| (\d[\d,]*) \|', FM, re.M)}
P_BYENT   = _fm_int(r'\*\*(\d[\d,]*) entries are cited by other entries\.\*\*', FM)
P_TABLE   = [(int(e), int(c)) for e, c in re.findall(r'^\| \*\*(\d+)\*\* \| (\d+)× \|', FM, re.M)]
P_MAIN, P_COMP, P_ANY = [int(x.replace(',', '')) for x in re.search(r'\*\*(\d[\d,]*) entries are cited in the main volume\'s chapters and appendices; (\d[\d,]*) counting the four compendia and the two papers; (\d[\d,]*) counting citations by other entries\.\*\*', FM).groups()]
print('   printed, read as data: total %s to %s | mature 165-%s at %s (back matter 165-%s) | kinds over %s | cited-by-entries %s | table %d rows | cited %s / %s / %s'
      % (P_TOTAL, P_HIGH, P_MAT_HI, P_MATURE, P_BACK_HI, P_KINDS_N, P_BYENT, len(P_TABLE), P_MAIN, P_COMP, P_ANY))

hr('2  THE ENTRY POPULATION (docket 30 convention)')
heads = re.findall(r'^### ([\d, ]+)$', R, re.M)
bare = [h for h in heads if h.strip().isdigit()]
grouped = [h for h in heads if not h.strip().isdigit()]
nums = sorted({int(x) for h in heads for x in h.split(',')})
check('heading lines = bare + grouped', len(heads), len(bare) + len(grouped))
score('entries (headings)', len(heads), P_TOTAL, 'reg1-A')
print('   bare %d, grouped %d, distinct numbers %d, min %d, max %d'
      % (len(bare), len(grouped), len(nums), min(nums), max(nums)))
score('extent low', min(nums), 1, 'reg1-A')
score('extent high', max(nums), P_HIGH, 'reg1-A')

def heads_in(a, b):
    return len([h for h in heads if a <= min(int(x) for x in h.split(',')) <= b])
g94, g164 = heads_in(1, 94), heads_in(95, 164)
score('genesis block 1-94 (headings)', g94, 94, 'reg1-B')
score('superseded block 95-164 (headings)', g164, 70, 'reg1-B')
print('   NOTE the front matter does not print a count for 95-164; 70 is the full range and is measured, not scored.')

hr('3  THE MATURE RECORD: 165-%d / %s  AGAINST THE CLOSING LINE 165-%d' % (P_MAT_HI, format(P_MATURE, ','), P_BACK_HI))
m1791_h, m1792_h = heads_in(165, P_MAT_HI), heads_in(165, P_BACK_HI)
m1791_n = len([n for n in nums if 165 <= n <= P_MAT_HI])
m1792_n = len([n for n in nums if 165 <= n <= P_BACK_HI])
print('   headings 165-%d %d | headings 165-%d %d' % (P_MAT_HI, m1791_h, P_BACK_HI, m1792_h))
print('   numbers  165-%d %d | numbers  165-%d %d   (numbers are NOT what the book counts)' % (P_MAT_HI, m1791_n, P_BACK_HI, m1792_n))
score('mature record 165-%d, headings' % P_MAT_HI, m1791_h, P_MATURE, 'reg1-C')
l6  = [i for i, l in enumerate(RL, 1) if '165 to %d' % P_MAT_HI in l]
l65 = [i for i, l in enumerate(RL, 1) if '165–%d' % P_BACK_HI in l or '165-%d' % P_BACK_HI in l]
print('   "165 to %d" at L%s ; "165-%d" at L%s' % (P_MAT_HI, l6, P_BACK_HI, l65))
print('   READING: 1,470 is EXACT on the heading convention for 165-1791. The closing line names')
print('   165-1792 for the same block while the count printed beside it excludes 1792, which is')
print('   itself an entry. The defective half is the RANGE in the closing line, not the count.')

hr('4  THE GROUPED FAULT ENTRIES')
gnums = sorted(int(x) for h in grouped for x in h.split(','))
score('grouped fault entries, count', len(gnums), 32, 'reg1-D')
score('grouped fault entries, low', min(gnums), 203, 'reg1-D')
score('grouped fault entries, high', max(gnums), 354, 'reg1-D')
score('grouped HEADINGS ("seven of which")', len(grouped), 7, 'reg1-E')
score('grouped HEADINGS ("the ten grouped headings")', len(grouped), 10, 'reg1-E')
pos = {}
for i, l in enumerate(RL, 1):
    m = re.match(r'^### ([\d, ]+)$', l)
    if m: pos.setdefault(m.group(1), i)
p361 = pos['361']; gpos = [pos[g] for g in grouped]
check('all grouped headings printed after entry 361', all(p > p361 for p in gpos), True)
print('   entry 361 at L%d; grouped headings at L%s' % (p361, gpos))

hr('5  THE KINDS TABLE, RECOMPUTED BY kinds.py (the book\'s own operator)')
out = subprocess.run([sys.executable, os.path.join(H, 'kinds.py'), os.path.join(H, REG)],
                     capture_output=True, text=True, cwd=H).stdout.split('\n')[0]
n_head = int(out.split()[0]); got = eval(out[out.index('{'):])
score('kinds.py heading population', n_head, P_KINDS_N, 'reg1-F')
PRINTED = P_KINDS
for k, v in PRINTED.items():
    score('kinds: %s' % k, got.get(k), v, 'reg1-F')
print('   NOTE kinds.py counts %s headings, not the %s of section 2: it drops the 95-164' % (format(P_KINDS_N, ','), format(P_TOTAL, ',')))
print('   supersession stubs under the chat-52 ruling. %d - 70 = %d, and that reconciles.' % (len(heads), len(heads) - g164))

hr('6  THE LOAD-BEARING TABLE, RECOMPUTED BY register_cites.py (the book\'s own operator)')
import runpy, io, contextlib   # the tool run unmodified; its FULL counter taken, not the top-12 it prints (which clips a 13th at 7)
_cwd = os.getcwd(); os.chdir(H); _buf = io.StringIO()
with contextlib.redirect_stdout(_buf): _G = runpy.run_path(os.path.join(H, 'register_cites.py'), run_name='__main__')
os.chdir(_cwd); rc = _buf.getvalue().split('\n'); byent = dict(_G['byent'])
score('entries cited by other entries', int(rc[0].split(':')[1]), P_BYENT, 'reg1-G')
TABLE = P_TABLE
for e, c in TABLE:
    score('load-bearing %d' % e, byent.get(e), c, 'reg1-H')
seven_plus = sorted([e for e, c in byent.items() if c >= 7])
score('entries cited 7 or more times ("the %d")' % len(P_TABLE), len(seven_plus), len(P_TABLE), 'reg1-H')
missing = [e for e in seven_plus if e not in [x for x, _ in TABLE]]
print('   measured at 7+ but ABSENT from the printed table: %s' % missing)

hr('7  THE THREE CITATION FIGURES')
m = re.search(r'main: (\d+) \| in companions: (\d+) \| main∪companions: (\d+)', rc[2])
anywhere = int([l for l in rc if l.startswith('cited anywhere')][0].split(':')[1])
score('cited in the main volume', int(m.group(1)), P_MAIN, 'reg1-I')
score('counting compendia and papers', int(m.group(3)), P_COMP, 'reg1-I')
score('counting citations by other entries', anywhere, P_ANY, 'reg1-I')

hr('8  POINTERS IN THE FRONT MATTER, EVERY ONE RESOLVED TO ITS CLAIM')
for n, what in [(1725, 'the settled entry form'), (1732, 'register_cites'), (1756, 'kinds'),
                (1744, 'build.py / entry form'), (868, 'R-inf -> R_M, Bohr 1913'), (1241, 'Fowler/Pickering'),
                (1139, 'multiplicity constraint proved'), (1178, 'carried into the operator'),
                (1208, 'dependency cycle'), (1225, 'audit 24')]:
    here = n in nums
    body = ''
    if here:
        i = pos.get(str(n))
        if i: body = ' | ' + re.sub(r'\s+', ' ', '\n'.join(RL[i:i + 2]))[:74]
    print('   register %-5d %-32s %s%s' % (n, what, 'EXISTS' if here else 'ABSENT', body))
    if not here: DEV.append(('reg1-J', 'front-matter pointer %d absent' % n, False, True))

hr('9  RULING 46 AND RULING 38 IN THE FRONT MATTER')
scripts = sorted(set(re.findall(r'`([a-z_0-9]+\.py)`', FM)))
builds = sorted(set(re.findall(r'\bBuild \d+\b', FM)))
print('   script names visible to the reader : %s' % scripts)
print('   build handles visible to the reader: %s' % builds)
if scripts or builds:
    DEV.append(('reg1-K', 'Ruling 46 sites in the Register front matter',
                len(scripts) + len(builds), 0))
    print('   Ruling 46 forbids script names, build numbers and internal file references in a')
    print('   reader-facing volume. Ruling 38 makes the front matter a PURPOSE STATEMENT ONLY.')
    print('   %d script names and %d build handles stand in it. Docket 6 / 5.' % (len(scripts), len(builds)))

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   deviations recorded      : %d' % len(DEV))
for t, tag, got, exp in DEV:
    print('     %-9s %-52s measured %-14s printed %s' % (t, tag, repr(got), repr(exp)))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
