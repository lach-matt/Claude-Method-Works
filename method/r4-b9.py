#!/usr/bin/env python3
"""r4-b9.py — Phase 2's last four measurable rows, and the fault reported from outside.
BUILD123 -> BUILD124 main.

FOUR ENTRIES, EACH BEHIND AN INSTRUMENT WRITTEN FOR IT.

  1876  method/proofs/geodesic.py  (17/17) — the Mathematical Compendium's gloss on the
        equality case of the multiplicative triangle inequality.  Reported by a second
        session, verified here, and its magnitude corrected: the relayed "up to 6,561x"
        is 3^8, an estimate of the box; measured over all 475,800 cell pairs the largest
        ratio is 27.  W-267 recorded it and said the entry was owed.  This is it.

  1877  method/proofs/corridors.py (28/28) — annex row A-F4, register 1517's corridor
        census, which the repository filed against register 1580.  It is 1517's; 1580 is
        cited for it in two places and does not state it.  W-264 declined this row on the
        ground that 1580's corridors and slopeaxis.py's are different objects.  That was
        right about 1580 and does not reach 1517, whose corridors ARE the slope axis's.

  1878  method/proofs/consshare.py (36/36) — annex row E-015, half: 12u-01, 12u-02 and
        12u-03 against section 12.11.1.2, whose four-row table this instrument reproduces
        exactly before saying anything about the sentence beneath it.

  1879  the same instrument, other half: 12v-01 and 12v-02, registers 623 and 625, which
        are one fault and not two.

REBUILT ONCE AT SOURCE.  The first BUILD124 seated entry 1878 with "Section 12.11.1.2"
where the Register writes the section pointer as "§12.11.1.2" in all 155 of its other
places -- the one "Section N.N" in the file would have been mine.  A pointer in the house
form is also the form the pointer instruments resolve, so this is not only style.  The
build and its compendia close were discarded and rebuilt rather than seated with it, which
is what was done at BUILD116 and BUILD121.

NO VOLUME CHANGES.  This is a Batch B pass: a Register entry is never edited and nothing
is repaired in a volume by it.  The count classes are re-taken in the same build.  Two
pointer faults are RECORDED here and neither is repaired -- the main volume's section 34.6
and register 1804 both cite 1580 for 1517's census, and Ruling 29 makes a Register pointer
unfixable in place; what a repair would need is M's.

Usage:  python3 r4-b9.py            dry run (asserts everything, writes nothing)
        python3 r4-b9.py --write    writes staging members + BUILD124 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD123_main_and_register.md')
OLD_M_MD5 = 'aa94b9557bbbd93653e7f5a0d2f2f026'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD124_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build124') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = (1876, 1877, 1878, 1879)
ENTRIES = """
### 1876

**THE MULTIPLICATIVE TRIANGLE INEQUALITY IS TIGHT ON THE CORNERS OF THE BOX, NOT ON THE BOX, AND THE ENTRY THAT PROVES IT GLOSSES ITS OWN EQUALITY CASE INTO A LARGER SET.** *The metric entry proves d(x,z) ≤ d(x,y)·d(y,z) coordinatewise with d(x,y) = ∏(|xᵢ−yᵢ|+1), and then writes* **"Equality holds on an axis iff st = 0, i.e. y lies between x and z there, so global equality iff y ∈ [x∧z, x∨z] — y on a geodesic"** *, with s = |a−b| and t = |b−c|.* **THE FIRST CLAUSE IS RIGHT AND THE i.e. IS NOT AN i.e.** *The entry's own arithmetic gives the right side as st + s + t + 1 against a left side of at most s + t + 1, so equality forces st = 0 — which says y COINCIDES with x or with z on that axis. Betweenness allows both s and t positive, and the smallest case is one line: a = 0, b = 1, c = 2 has y between, st = 1, and 3 against 4. The inequality is strict exactly where the gloss says it is tight.* **SO THE EQUALITY SET IS THE VERTEX SET OF THE ORDER INTERVAL — 2ᵏ points where k axes differ — AND NOT THE INTERVAL, WHICH HAS ∏(Δᵢ+1).** *Measured over all 475,800 pairs of Λ₈ cells the largest ratio between the two is TWENTY-SEVEN, at an interval of 6,912 against 256 vertices; and 6,912 is Λ₈'s own box, so the extreme case is the whole box against its corners.* **THE GAP IS NOT UNIFORM AND THAT IS WHY IT SURVIVED: 149,535 of the 475,800 pairs differ by at most one on every axis, and for those the two readings name the same set.** *A reader checking small examples meets no fault in about a third of them. What is NOT in question is the inequality itself, which is proved, nor the entry's sampled confirmation of it — a sample of an inequality cannot see a fault in its equality case and did not claim to.* Registers 1876. (a finding.)

### 1877

**THE CORRIDOR CENSUS REPRODUCES IN ITS HEADLINE AND ITS WITNESSES AND FAILS IN TWO FIGURES, AND IT IS CITED TWICE UNDER THE WRONG NUMBER.** *Register 1517 prints* **"73 fully bounded, 7 bounded below only, 26 above only, none unbounded ... the maximum set of PAIRWISE DISJOINT corridors is THREE, at B 5, La 57 and Lr 103; and the minimum number of stabbing points is also THREE ... Gallai duality holds exactly"** *. Re-measured on the slope axis in both forms of the law and under both candidate-set conventions — four cells, none merged.* **WHAT STANDS. Three, forced by boron, lanthanum and lawrencium, with Gallai duality exact, reproduces in the node-only form under BOTH candidate sets, witnesses and all; lanthanum's endpoints reproduce to the digit in all four cells; and at ℓ ≤ 4 node-only two of the census's three numbers are exact — twenty-six bounded above only, and eighty carrying a lower bound.** *What does not.* **1517 leaves SEVEN of those eighty open above where the measurement leaves THREE — in every one of the four cells — and it closes lawrencium's corridor at 2.4409 where it is open above in every cell, a value that is an endpoint of no corridor in the family.** *No fifth convention was sought: six were tried, and a convention reverse-engineered to fit a figure is not a reproduction. The finished form gives FOUR disjoint corridors, not three, and the entry named no form.* **AND THE CENSUS IS CITED TWICE AS REGISTER 1580's — once in the occupation-law chapter and once at register 1804 — where 1580 states no census at all and carries the held-out walk.** *Both pointers resolve and their target says something else, which is the class recorded at registers 1861, 1871 and 1874. The chapter's repair is a pointer; register 1804's is not available, since a Register entry is never edited. Recorded, not repaired.* Registers 1517; 1580; 1804; 1861; 1871; 1874. (a finding.)

### 1878

**THE CONSERVATIVE SHARE'S TABLE IS EXACT IN ALL SIXTEEN OF ITS NUMBERS AND THE SENTENCE BENEATH IT IS WRONG IN THREE WAYS.** *§12.11.1.2 builds Λ₉ at four cap settings and counts the composable cells with g = q. Rebuilt from its own stated method — and the builder is proved against the seated tower cell for cell at the book's caps before any other row is read — every figure returns exactly: 1,654 / 1,169 / 739 / 63.2 %, 19,433 / 16,150 / 5,986 / 37.1 %, 44,153 / 37,430 / 14,114 / 37.7 %, 83,543 / 71,087 / 26,921 / 37.9 %.* **THEN THE d SHELL. The section reads "Once the d shell is open the share sits at 37–38 %" and takes 37.1 % as its first instance. The 37.1 % row is capped at ℓ_max = 1 — s and p only, the SAME cap as the 63.2 % row it is being contrasted with — so no d subshell exists in it. What changes between those two rows is n, e and k. The first row admitting ℓ = 2 is the 37.7 % row.** *Then the two ranges.* **"Moves by less than a point across a fiftyfold growth in cells" joins a growth to a range that is not its own: the fiftyfold growth is 1,654 to 83,543 = 50.5×, and across THAT the share moves 25.3 points; the range over which it moves 0.8 of a point is 19,433 to 83,543, which is 4.3×.** *And then the word.* **The quantity counted is g = q — the transfer total with nothing left behind, which is CONSERVATION — and the sentence calls it reversibility. On the reading that the reverse move is itself a cell, reversibility is a different series entirely: 33.3, 11.0, 11.2 and 11.3 %, which settles near one cell in nine and not three in eight.** *What "reversibility" ought to mean is not settled here; the finding is that the word and the number are not the same object, and that does not need the word pinned down. Registers 389 and 392 restate the sentence, 393 repairs its denominator and not this. Recorded, not repaired.* Registers 389; 392; 393. (a finding.)

### 1879

**REGISTERS 623 AND 625 ARE ONE FAULT AND NOT TWO, AND ITS ARITHMETIC NAMES THE FIGURE THAT WAS WITHDRAWN.** *Register 623 is headed* **"AND THE AXIS THAT MAKES THE TOWER A CATEGORY IS WORTH TWENTY POINTS"** *and its body prints Λ₈ at* **0 %** *composable and Λ₉ at* **70.7 %** *. The jump the body describes is 70.7 points, and the headline says twenty.* **AND REGISTER 625 SAYS "REGISTER 623's 50.3 % FOR Λ₈", WHICH 623 DOES NOT PRINT ANYWHERE.** *625's own correction is stated and correct — a three-against-three signature was replaced by source (n, ℓ, k, 2S) against target (e, f, g), four against three, under which nothing composes — but it cites for the superseded value an entry whose printed body already carries the corrected one.* **THE TWO HALVES SIT ON DIFFERENT SIDES OF THE CORRECTION, AND THE HEADLINE'S ARITHMETIC PROVES WHICH SIDE IT IS ON: 70.7 − 50.3 = 20.4, and twenty is that jump and no other.** *So the headline is a residue of the superseded figure and the attribution in 625 is a citation of the same residue — one fault with two symptoms, filed in the repository as two. Nothing here withdraws 625's measurement, which stands; what is broken is the chain as printed, and under Ruling 29 a Register pointer is not repairable in place. Recorded, not repaired.* Registers 313; 623; 625. (a finding.)
"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

new = dict(txt)

r = txt[REG]
for _n in ENTRY_NS:
    assert r.count('### %d\n' % _n) == 0, 'entry %d already seated' % _n
assert r.count('### %d\n' % (ENTRY_NS[0] - 1)) == 1, 'entry %d is not seated' % (ENTRY_NS[0] - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
# Emphasis parity, asserted on each new entry's body before it is seated. Every entry here is
# written as alternating **bold** and *italic* runs; an odd asterisk total means one delimiter is
# short and the emphasis does not close on the page. The first draft of this build seated 1844 and
# 1846 with a `**`-opened quotation closed by a single `*` -- 43 and 39 asterisks -- and joined
# r2-reg7a2's pinned odd-total class of 22, which stopped that instrument (EXPECTED 22, got 24).
# The build was discarded and rebuilt; this assertion is what makes the class unreachable, and
# r2-reg7a2's 22 is untouched.
_bodies = [b for b in ENTRIES.split('\n') if b.startswith('**')]
assert len(_bodies) == len(ENTRY_NS), 'expected one body line per entry, got %d' % len(_bodies)
for _n, _b in zip(ENTRY_NS, _bodies):
    assert _b.count('*') % 2 == 0, 'entry %d: odd asterisk total %d -- an emphasis run does not close' % (_n, _b.count('*'))

new[REG] = r.rstrip('\n') + ENTRIES + '\n'

# ---- the counts, from the seated tools on the members as they will stand (entries 1815 and 1816's classes)
stage = tempfile.mkdtemp(prefix='r4-b9-')
for f in os.listdir(MEM):
    if f.endswith('.md') and f not in new: os.symlink(MEM + f, os.path.join(stage, f))
for n in new: open(os.path.join(stage, n), 'w', encoding='utf-8').write(new[n])
cwd = os.getcwd(); os.chdir(stage); buf = io.StringIO()
with contextlib.redirect_stdout(buf): G = runpy.run_path(MEM + 'register_cites.py', run_name='__main__')
os.chdir(cwd)
byent, bymain, comp = G['byent'], G['bymain'], G['comp']
CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY = len(byent), len(bymain), len(set(bymain) | set(comp)), len(byent + bymain + comp)
TOP = sorted(((n, k) for n, k in byent.items() if k >= 7), key=lambda t: (-t[1], t[0]))
kout = subprocess.run([sys.executable, MEM + 'kinds.py', os.path.join(stage, REG)], capture_output=True, text=True, cwd=MEM).stdout.split('\n')[0]
K_N = int(kout.split()[0]); K = eval(kout[kout.index('{'):])
for f in os.listdir(stage): os.unlink(os.path.join(stage, f))
os.rmdir(stage)
sys.path.insert(0, TOOLS); import close_main as cm; import register_counts as rc
print('register_cites with %s: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %d entries'
      % (str(ENTRY_NS), CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, len(TOP)))
print('kinds.py: %d %s' % (K_N, K))
rr, edits = cm.recount(new[REG]); assert edits, 'recount changed nothing'
for o, n in edits: print('recount: %s -> %s' % (o[:60], n[:60]))
c = rc.count(rr)

def sub1(t, pat, repl, label):
    mm_ = re.search(pat, t, re.M); assert mm_, label + ': anchor absent'
    n = repl(mm_); assert t.count(mm_.group(0)) == 1, label + ': anchor not unique'
    print('%-40s %s' % (label, 'unchanged' if n == mm_.group(0) else '%s -> %s' % (mm_.group(0)[:52].replace('\n', ' '), n[:52].replace('\n', ' '))))
    return t.replace(mm_.group(0), n)

for kind in ('a finding', 'a correction', 'a measurement', 'a new protocol', 'a withdrawal', 'prior art', 'an open question', 'a fault of mine'):
    rr = sub1(rr, r'^\| \*\*%s\*\* \| (\d[\d,]*) \| (\d+) \|' % re.escape(kind),
              lambda mm_, kind=kind: '| **%s** | %s | %s |' % (kind, g(K[kind]), mm_.group(2)), 'kinds row ' + kind)
rr = sub1(rr, r'by `kinds\.py` over the (\d[\d,]*) entry headings,', lambda mm_: 'by `kinds.py` over the %s entry headings,' % g(K_N), 'kinds headings')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited by other entries\.\*\*', lambda mm_: '**%d entries are cited by other entries.**' % CITED_BY, 'cited by entries')
rr = sub1(rr, r'the (\d+) cited seven times or more:', lambda mm_: 'the %d cited seven times or more:' % len(TOP), 'the N cited')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited in the main volume\'s chapters and appendices; (\d[\d,]*) counting the four compendia and the two papers; (\d[\d,]*) counting citations by other entries\.\*\*',
          lambda mm_: '**%d entries are cited in the main volume\'s chapters and appendices; %d counting the four compendia and the two papers; %s counting citations by other entries.**'
          % (CITED_MAIN, CITED_MC, g(CITED_ANY)), 'cited 3 figures')

rows = re.findall(r'^\| \*\*(\d+)\*\* \| (\d+)× \| (.*) \|$', rr, re.M)
what = {int(e): w for e, _, w in rows}

# A row crossing seven citations is a HAND ACT and this build makes exactly two.
# Entry 1879 cites registers 623 and 625 together -- they are one fault and not two, which
# is the entry -- and that citation takes 625 from seven to eight and 623 from six to seven.
# Both rows are written by hand below and neither is derived from the entry that moved them.
NEW_ROWS = {
    623: 'The ninth axis is what makes the tower a category: \u039b\u2088 composes at nothing, \u039b\u2089 at 70.7 %',
    625: 'The tower\u2019s composability peaks at \u039b\u2081\u2080 and turns, on a four-against-three signature',
}
for _n, _w in NEW_ROWS.items():
    assert _n not in what, 'register %d already has a row' % _n
    assert _n in {n for n, _ in TOP}, 'register %d has not crossed seven citations' % _n
    what[_n] = _w
assert sorted(what) == sorted(n for n, _ in TOP), ('the >=7 set changed; a new row is a hand act and this build writes none; REFUSED', sorted(what), TOP)
i0 = rr.index('| entry | cited | what it established |\n|---|---|---|\n'); i1 = rr.index('\n\n', i0)
rr = rr[:i0] + '| entry | cited | what it established |\n|---|---|---|\n' + ''.join('| **%d** | %d× | %s |\n' % (n, k, what[n]) for n, k in TOP) + rr[i1 + 1:]
new[REG] = rr

mm = new[MAIN]
mm = sub1(mm, r'(\d[\d,]*) entries, 1 to (\d+), at this build \(\d{4}-\d\d-\d\d\)',
          lambda mm_: '%s entries, 1 to %d, at this build (2026-09-07)' % (g(c['headings']), c['highest']), 'main: at this build')
mm = sub1(mm, r'436 entries when this paragraph was written, (\d[\d,]*) at this build',
          lambda mm_: '436 entries when this paragraph was written, %s at this build' % g(c['headings']), 'main: N at this build')
mm = sub1(mm, r'at this build the main volume cites (\d+) entries',
          lambda mm_: 'at this build the main volume cites %d entries' % CITED_MAIN, 'main: cites N')
new[MAIN] = mm

c2 = rc.count(new[REG]); p2 = rc.printed(new[REG])
assert (p2['front_total'], p2['front_highest'], p2['front_mature'], p2['front_mature_highest'], p2['back_mature_highest']) == (c2['headings'], c2['highest'], c2['mature'], c2['highest'], c2['highest']), (p2, c2)
assert c2['genesis'] + c2['superseded'] + c2['mature'] == c2['headings'] == p2['front_total']
print('the front matter sums to itself: %d + %d + %d = %d, highest %d' % (c2['genesis'], c2['superseded'], c2['mature'], c2['headings'], c2['highest']))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v in new:
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], txt[v].count(a), new[v].count(a)) for a in anchors if txt[v].count(a) != new[v].count(a)]
    print('build.py SUBS anchors on %-36s %3d checked; moved: %s' % (v, len(anchors), moved)); assert not moved
for v in new: print('%-36s %d -> %d B, lines %+d' % (v, len(old[v]), len(new[v].encode('utf-8')), new[v].count('\n') - txt[v].count('\n')))

# ---- the bundle, and the reverse guard ---------------------------------------------------------------
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD123 md5 mismatch'
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
ms = {x.group(1).decode(): x.group(2) for x in MEMBER.finditer(ob)}
nb = ob
for n in (MAIN, REG):
    assert ms[n] == old[n], '%s in the bundle is not the extracted member' % n
    b0 = block(n, ms[n]); assert nb.count(b0) == 1
    nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
rv = nb
for n in (MAIN, REG):
    b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1
    rv = rv.replace(b1, block(n, ms[n]))
assert md5(rv) == OLD_M_MD5, 'reverse FAILED'
print('BUILD123 -> BUILD124: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD124 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
