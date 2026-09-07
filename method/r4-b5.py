#!/usr/bin/env python3
"""r4-b1.py — Phase 1's first seven entries: the subject matter its instruments settled.
BUILD119 -> BUILD120 main.

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
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD119_main_and_register.md')
OLD_M_MD5 = '658e149bedad9fff98ee2596d2a8cc30'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD120_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build120') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = tuple(range(1858, 1865))
ENTRIES = """

### 1858

**REGISTER 1779 CALLS Z − charge THE ELECTRON COUNT AND THE SPECTRA COMPENDIUM PRINTS THE FORMULA TWO HUNDRED LINES AWAY: Nₑ = Z − charge + 1.** *Register 1779's strongest result is stated as* **"the multiplicities admitted at a pair are a function of the electron count Z − charge alone, which holds on all 7,260 pairs with no exception — the strongest of them, and it had never been tested"**. *The dependence claim is untouched and the test stands: Z − charge is a bijection with Z − charge + 1, so a function of one is a function of the other, on all 7,260 pairs.* **What is wrong is the identification.** *The Spectra Compendium defines its own column as* **"charge the ionisation stage, 1 for the neutral"** *and prints* **Nₑ = Z − charge + 1** *in as many words; 1779's own specimen row is sodium's s channel as COORD(11, 1, 0, 2), and neutral sodium has eleven electrons, which is 11 − 1 + 1 and not 11 − 1.* **So the quantity the multiplicities depend on is one less than the electron count, and the entry names it as the electron count.** *The repair is the identification, not the finding.* Registers 1779. (a correction.)

### 1859

**REGISTER 1786 SAYS THERE WAS NEVER AN F.3.1 OR AN F.3.2 AND THE ORIGINAL INPUT CARRIES BOTH, AS HEADINGS.** *1786 renumbers Appendix F and states its history:* **"The appendix ran F.1, F.2, F.3, F.3.3, F.4, F.4.1, F.4.2, F.4.3. There was never an F.3.1 or an F.3.2 — F.3 carried a single child and that child was numbered third"** *, and adds* **"Nothing anywhere referenced F.3.1 or F.3.2"**. *Measured against the Ruling 56 original-input witness:* **F.3.1 occurs three times and F.3.2 once. Both are section headings — "F.3.1 And the distribution is the finding" and "F.3.2 The tripwire" — and §F.3.1 is referenced twice in the witness's own prose, once as "§F.3.1 measures the population instead" and once as "F.3.1 gives the population it should be drawn from".** *So both historical sentences are false: the two sections existed and were referenced.* **The renumbering itself is not disturbed** *— the live volume carries F.3.1 seven times and no F.3.2 or F.3.3, which is the state 1786 produced. What falls is the account of what was there before, and the witness that refutes it is the one Ruling 56 seats as the original input.* Registers 1786. (a correction.)

### 1860

**§2.19.1 CITES REGISTER 286 FOR ITS OWN FINDING AND 286 IS A GROUPED HEADING ABOUT A DIFFERENT DEFECT.** *§2.19.1 closes its account of the false heading count — §28.7.6 titled "Three from the tower session" while holding eighty-six entries — with* **"Register 286."** *286 carries no heading of its own. It is seated only inside the grouped heading* **203, 215, 218, 259, 280, 283, 284, 286, 291**, *whose entry is* **"§4.2 — WROTE INTO A STRUCTURE WITHOUT READING IT"** *— §28.8 misplaced, contents disagreeing with the body, ledger rows written over A.8–A.11, a heading the press could not see. Structural placement, not a false count.* **The entry that carries §2.19.1's finding is 289** *—* **"§28.7.3 IS TITLED FIFTEEN MORE AND COVERS SEVENTY-FIVE ENTRY NUMBERS"** *— and* **290 is the entry that closes it: "BOTH ITEMS §2.19.1 LEFT UNREPAIRED ARE REPAIRED."** *A reader following the section's own pointer arrives at neither.* Registers 286; 289; 290. (a correction.)

### 1861

**APPENDIX A.15's REMARK CITES REGISTER 230 FOR A LEDGER CORRECTION THAT 230 DOES NOT CARRY.** *A.15's Remark reads* **"This corrects the ledger, which called C a join-closed sublattice. A sublattice is closed under both operations … which is a sublattice and is the reason the last coupling step is carried exactly. Register 230."** *Register 230 reads* **"APPENDIX D'S KIND COORDINATE DISAGREES WITH PART III'S TITLE — THE PART IS CALLED THE LAW AND ITS CONTENTS ARE THEOREMS. Recorded rather than resolved; promotion tested at 232."** *A coordinate's name against a part's title is not a ledger's description of a band, and 230 records no correction of C.* **The main volume makes the same attribution a second time**, at §12's discussion of the two-parent bound, where it says §A.15 and register 230 record it together. *Two sites, one pointer, and it resolves to an entry about something else.* Registers 230. (a correction.)

### 1862

**§14.5.9's TABLE PRINTS A LOWER BOUND ON THE SEED AND NO REGISTER ENTRY STATES IT.** *The table's columns are* **object · cells · prune · cover · +prune · random · reverse · LB · EXACT · spread**, *and Λ₈'s row reads* **976 · 12 · 7 · 7 · 7 · 40 · 5 · 7 · 33**. *The Register carries every figure in that row but one:* **seed(Λ₈) = 7 exactly, by branch and bound, is seated; the five heuristics 12, 7, 7, 7 and 40 are seated; the spread of thirty-three around an exact seven is seated. The lower bound of 5 is seated nowhere.** *It is the one number in the row that says what could not have been done better without the exact answer, and it is the one the Register does not hold. Recorded as a gap in the record rather than a defect in the table, which prints it correctly.* Registers 1832. (a finding.)

### 1863

**THE CITED-BUT-ABSENT REGISTER NUMBERS ARE FOUR, AND ONLY ONE OF THEM IS ON THE DOCKET'S LIST OF SIX.** *The docket names 344, 571, 1002, 1149, 1257 and 1710 as register numbers cited with no entry.* **Measured by the seated resolver over the six volumes and the companion: the cited absences are 287 at main L1503, 1000 at reg L4667, 1002 at reg L6529 and 1725 at reg L10 — four of the 133 absent numbers in the extent.** *Of the docket's six only* **1002** *is still among them; 344, 571, 1149, 1257 and 1710 are absent from the Register and cited by nothing, which the resolver's own rule declines to call a pointer failure — an uncited absence is not one. And three of the four current ones — 287, 1000, 1725 — the docket does not name.* **The class did not shrink from six to one; it moved.** *Recorded so the list is measured rather than inherited.* Registers 1725. (a correction.)

### 1864

**THE GENESIS BLOCK'S SHELL CAPACITIES ARE THE UNBOUNDED LATTICE'S AND ARE STATED AS SLICES OF Λ.** *Entry 43 reads* **"SHELL CAPACITY 2n² IS THE VOLUME OF A HORIZONTAL SLICE OF Λ. Counting admissible cells at fixed n: Σ(ℓ=0 to n−1) 2(2ℓ+1) = 2n², so the capacities 2, 8, 18, 32, 50, 72, 98 are the slice volumes"** *, and entry 50 pairs them —* **2, 2, 8, 8, 18, 18, 32, 32, 50, 50, 72, 72**. *The sum runs ℓ from 0 to n−1, which is the unbounded shell lattice.* **Λ as seated caps ℓ, and its horizontal slices are 120 at n = 1, 428 at n = 2 and 428 at n = 3 — it admits no n above 3 at all, so the capacities 32, 50, 72 and 98 are slices of nothing in it.** *Both are genesis entries, written before the index carried its caps, and the arithmetic in them is correct for the object it describes.* **What has moved is the word Λ**, *which in the mature record names the capped index and in these two entries names the lattice the caps were later imposed on. Recorded, not repaired: the entries are right about the shell lattice and the term is read differently either side of the genesis block.* Registers 43; 50. (a finding.)
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

# A row crossing seven citations is a HAND ACT and this build makes exactly one.
# Entry 1861 cites register 230 for the second time in the Register, taking it from six to
# eight across the volumes, so 230 enters the >=7 table here with the gloss written by hand.
NEW_ROWS = {230: 'Appendix D\u2019s *kind* coordinate against Part III\u2019s title, recorded rather than resolved'}
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
print('BUILD119 -> BUILD120: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD116 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
