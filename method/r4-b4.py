#!/usr/bin/env python3
"""r4-b1.py — Phase 1's first seven entries: the subject matter its instruments settled.
BUILD118 -> BUILD119 main.

Phase 1 of PLAN-R4-PUBLICATION is "every computable claim still unproven or contradicted, re-derived
by a standard-library instrument and settled by ENTRY before any prose moves ... Output: one
instrument per class, banked; one Register entry per correction or withdrawal; the count classes
re-taken."  method/PHASE1-LEDGER.md is the leg's ledger and names the instrument behind each.

WHAT IS HERE AND WHAT IS NOT. M's ruling of 7 September: "if it is work matter, it does not belong
in the volumes. if it is subject, it must be included." Seven of the sixteen disposed rows are
subject matter and are seated here. The rest -- the unnamed cap family, the record-carried
compendium counts, register 497 withdrawn and re-cited, the docket's own wrong instance at
molybdenum, and the fifty-one pointers into empty headings -- are work matter and go to the working
register, not to the Register.

NO VOLUME CHANGES. This is a Batch B pass: a Register entry is never edited and nothing is repaired
in a volume by it. The count classes are re-taken in the same build.

Usage:  python3 r4-b1.py            dry run (asserts everything, writes nothing)
        python3 r4-b1.py --write    writes staging members + BUILD116 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD118_main_and_register.md')
OLD_M_MD5 = 'a49042af3ed417c2d772acc623ff2199'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD119_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build119') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = (1854, 1855, 1856, 1857)
ENTRIES = """

### 1854

**THE UNPRINTED-INPUT CLASS IS NOT "SIXTY MEMBERS, UNCHANGED": TWO OF ITS NAMED SEVEN ARE REPAIRED, AND WHERE IT STILL HOLDS IN §22 THE TABLE IS RIGHT AND UNVERIFIABLE RATHER THAN WRONG.** *The docket carries the class as* **"the unprinted-input class, sixty members — unchanged"** *, and names seven sites. Two no longer belong:* **§22.1.2 now prints its whole input set and says so — "The input set is printed": R = 109,737.31568 cm⁻¹, Z = 1, n from 4 to 14, and δ = 0.00, 0.35, 1.35, 2.65 — and §22.1.1.1's claim to F.3's highest standard is substantiated in that same passage.** *Where the class does still hold, what it holds is sharper than the docket says.* **§22.2.1's ablation table prints three directional figures — 446×, 0.28× and the asymptotic asymmetry 1,577 — which are mutually consistent at full precision and not one of which reproduces from the two-figure inputs printed beside it: 206/0.46 = 447.83, not 446, and 206/0.13 = 1,584.6, not 1,577. Solving the table's own ratios recovers the inputs: a median error of 0.461883 and an above-cost of 0.130628, which print as the 0.46 and the 0.13 the table already shows, and whose ratio prints as its 0.28.** *So the figures are right and the page cannot check them; the missing inputs are two, and they are recoverable from the figures themselves. The same table's other two rows do reproduce — 588/200 = 2.94 → 2.9 and 41.3/12.8 = 3.23 → 3.2 — which is what makes this a statement about four figures rather than a complaint about rounding.* **§22.4.1 is the fourth member and its input is recoverable too: n³/(2δ₂) returns the printed 4,267 at n = 8 and 1.386 × 10⁶ at n = 55 for δ₂ ≈ 0.060, and δ₂ appears nowhere in the section.** *One named member leaves the class entirely: "a factor of 17" has both its inputs printed, 0.14 and 0.008, and 0.14/0.008 = 17.5 exactly — nothing is missing there and a convention is unnamed, which is register 1855's. Measured by `unprintedinput.py`, selftest 21 of 21. The docket's sixty is a floor and it has moved; four of the seven named sites stand.* Registers 1855. (a correction.)

### 1855

**THE ARITHMETIC-CONVENTION CLASS RESOLVES TO ONE CONVENTION AT THE TWO SITES THE PAGE CAN DECIDE, AND IT IS TRUNCATION — WHILE THE ONLY PLACE THE CORPUS EVER NAMES A CONVENTION NAMES A DIFFERENT ONE.** *The class was filed as* **"some thirty printed counts with unnamed conventions"** *, which is a complaint about silence. Two of its members can be decided from the page alone and they agree.* **§32.1.3's table gives three shares of a partition — 88/5/6, 73/23/2 and 55/25/18 — summing to 99, 98 and 98. Under round-to-nearest each share lies within a half of its true value, so three of them sum to within one and a half of 100 and the integer sum must fall in 99 to 101: 98 is unreachable. Under truncation each loses up to one, the sum falls in 97 to 100, and 98 is reachable. Two of the three rows are therefore truncated.** *And* **§22.4's "a factor of 17" divides exactly: 0.14/0.008 = 17.5, which rounds to 18 and truncates to 17. Two independent sites, one convention.** *The corroboration is what makes it worth an entry rather than a note:* **a search of all six volumes returns exactly one site naming a numeric rounding convention, and it is not a volume's own prose but a Register entry correcting the Mathematical Compendium's penetration percentage — "146 of 163 is 90% at nought decimal places, rounding half to even". So the corpus names half-to-even once, in passing, inside a correction, and practises truncation at the two sites a reader can check.** *This matters to more than the reader:* **`arith.py` scores the volumes under HALF_UP and HALF_EVEN and returns neither of these two sites, so an instrument that does not know the book truncates will score truncated figures as wrong.** *What the class needs is one sentence naming the convention, not thirty edits. Two members stay undecided and stay in the class — 16z-06's unnamed median and 16z-03's generator convention — because each needs the population it was taken over and neither volume prints it. Measured by `convention.py`, selftest 14 of 14.* Registers 1854. (a finding.)

### 1856

**THE ns/(n−1)d CROSSING TABLE PRINTS ITS OWN FORMULA AND THEN TWO VALUES THE FORMULA DOES NOT GIVE, AND THE COMPENDIUM CALLS ALL FOUR EXACT.** *Both volumes print the closed form beside the numbers, so nothing here is reconstructed:* **a_cross = (√(n−1) + √(n−4))/3**, *and both then give* **"0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4 to 7"** *— the Mathematical Compendium adding* **"four exact hits"**. *Evaluated from the printed formula:* **n = 4 gives 0.5773503 and n = 5 gives 1.0000000, both exact to the seven places printed — which is what identifies the formula beyond doubt — while n = 6 gives 1.2167605 against the printed 1.2168450, wrong from the fifth significant figure, and n = 7 gives 1.3938469 against the printed 1.3938270, wrong from the sixth.** *Two of the four hits are exact and two are misprints, so* **"four exact hits" is false as printed**. *The claim the table is making survives: the crossing is fixed by the subshell pair alone, the denominator 3 is p_g − p_r invariant across the table, and nineteen distinct surds run the whole of it — what falls is two seven-digit numerals and the word* **four**. *Two sites carry them, main §34.5 and the Mathematical Compendium; the Register's own statement of the law does not print the values and is untouched.* Registers 1330. (a correction.)

### 1857

**REGISTER 487 PRINTS "Λ'S EIGHT CONSTRAINTS" AND Λ HAS SEVEN, WHICH ITS OWN RESULT DOES NOT NEED.** *Register 487 opens* **"THE MATHEMATICS CLOSED TO 14% OPEN ON REAL NUMBERS."** *and rests it on* **"Λ's eight constraints tested against 113 real subshells across 57 elements, including all nineteen configuration anomalies — 3,964 tests, zero failures"**. *The count is seven.* **§21.5.2 prints seven constraints and its constraint graph as eight nodes and seven edges — a tree, which requires exactly n − 1 edges — and the seven printed constraints rebuild Λ₈ at exactly 976 cells, identical to the seated `tower-2.py` cell for cell, with no constraint redundant.** *The section's own triple census over all C(7,3) = 35 triples returns 0 three-bodies, 7 triples spanned by one edge, 20 by two and 8 by three, which is a census of seven and not of eight.* **Nothing in 487's result depends on the count**: 3,964 tests over 113 subshells and 57 elements with zero failures is the same measurement whether the constraint set is seven or eight, and palladium — which has no valence s-shell at all — still satisfies every one. *The entry's finding stands; its stated cardinality does not. Measured by `lambda8.py` against the seated tower.* Registers 487. (a correction.)"""

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
stage = tempfile.mkdtemp(prefix='r4-a1-')
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD115 md5 mismatch'
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
print('BUILD118 -> BUILD119: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD116 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
