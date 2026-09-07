#!/usr/bin/env python3
"""r4-b1.py — Phase 1's first seven entries: the subject matter its instruments settled.
BUILD120 -> BUILD121 main.

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
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD120_main_and_register.md')
OLD_M_MD5 = 'addfb824ea550ca7753766641c107757'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD121_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build121') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = tuple(range(1865, 1871))
ENTRIES = """
### 1865

**A CORRECTION TO §18.5 IS ANNOUNCED IN CHAPTER 22, §18.5 SAYS NOTHING OF IT, AND THE REGISTER DOES NOT MENTION §18.5 AT ALL.** *The three-body work closes a derivation with* **"Which corrects §18.5. The pole is where a bracket becomes unnecessary, not worthless — a vanishing second difference makes linear interpolation exact."** *§18.5 reads, unchanged:* **"The cost of a guarantee, derived in Chapter 23, has a pole at p = 1 — the exponent at which an observable is linear. A straight line has no curvature. There is no interpolation error to price, so a guarantee…"** *— the pole stated without the correction's reading of it.* **And the string "18.5" occurs zero times in the Register.** *So a volume announces a correction of its own section, the corrected section carries no notice, and the record holds neither. This is the inverse of the store's own rule that no volume may change without an entry recording it: here an entry is owed for a change the volume already announces.* Registers 1865. (a finding.)

### 1866

**THE INDEX OF INDICES PRINTS ROW 1.7 TRUNCATED AT AN ESCAPED PIPE, AND THE MAIN VOLUME PRINTS THE SAME ROW WHOLE.** *The main volume's table gives it complete:* **"1.7 | Six blindnesses of the closure. A derived coordinate cannot repair it: the box grows by that coordinate's value count while \|X\| stays fixed. | `A.derived`"** *— the cardinality bars escaped, as a Markdown table requires.* **The Index of Indices carries the same row as "…the box grows by that coordinate's value count while \" and stops there.** *The escape was lost, the first bar was read as a cell boundary, and the sentence ends mid-clause with a stray backslash on the page.* **What is missing is the operative half of the claim** *— that |X| stays fixed while the box grows is the whole reason a derived coordinate cannot repair a blindness, and the Index prints the premise without it. One row, one volume, and the correct text is already in the other.* Registers 1866. (a correction.)

### 1867

**THE Sc VI PREDICTION IS COMMITTED AT THREE SITES OF THE MAIN VOLUME AND THE REGISTER HAS NO ENTRY FOR IT.** *The prediction is falsifiable and stated as such:* **"E(Sc VI 3s²3p³(⁴S°)6s ³S°₁) = 736,688 cm⁻¹ bracketed in [735,860, 737,380] cm⁻¹"**, *carried again in the two-point Ritz row and a third time in the E(6s) estimate table.* **The figure 736,688 occurs three times in the main volume and zero times in the Register.** *A committed prediction is the one kind of claim the record exists to hold — it is what a later measurement is checked against, and if it is refuted the Register is where the refutation attaches. It has nowhere to attach.* **This is not a defect in the prediction, which is stated with its bracket and its method**; *it is a gap in the record, and it is the gap that matters most, because the volume can be revised and a prediction cannot be un-made.* Registers 1867. (a finding.)

### 1868

**§F.4.1 NAMES TWO RATIOS AND SAYS ENTRIES ESTABLISHED BOTH; ONE HAS AN ENTRY WITH A VALUE AND THE OTHER IS NAMED ONCE IN THE WHOLE CORPUS AND GIVEN NO FIGURE ANYWHERE.** *§F.4.1 is titled* **"Two ratios the book had never measured about itself"** *and the record says both were then measured.* **Only one was.** *Register 1762, Ruling 25, establishes the withdrawal ratio with a value —* **4.21 : 1, p 0.192, 0.705 bits** *— and cites its history back to register 297.* **The method ratio has no such entry.** *It is named exactly once in the six volumes, in register 296's own heading —* **"TWO MEASUREMENTS OF THE BOOK'S OWN SHAPE NAMED AT F.4.1 — THE WITHDRAWAL RATIO AND THE METHOD RATIO"** *— whose body says only that Appendix F* **"had not indexed the two describing the book"** *and gives neither a figure. It occurs zero times in the main volume and zero times in the four companion volumes.* **So of the two ratios the appendix names, one is established and the other is named and never measured**, *and the nineteen figures removed with the withdrawn appendix are in the same position: they left the volume and no entry records where they went.* **A caution about this entry itself, recorded rather than discovered later.** *`r2-26c2` asserts that the registers naming the method ratio are exactly* **[296]**, *which was true until this entry. Seating it makes the answer* **[296, 1868]** *and the instrument refuses. It is not wrong and this entry is not wrong: the record has outgrown a pinned list, which is the same shape as `r2-26b`'s, and the answer is a successor rather than an edit.* **`r2-26c2` is therefore held from this build with `r2-26c3` owed**, *and its four standing deviations — 26b-02, 26b-03, 26c-02 and 26c-03 — are carried into that successor unchanged.* Registers 296; 1762. (a finding.)

### 1869

**REGISTER 1755 CARRIED TWO ITEMS AS OWED; BOTH ARE CLOSED IN THE VOLUME AND ONLY ONE CLOSURE IS RECORDED.** *1755 states them exactly:* **"§34.4 'The rule' is a heading with no body between §34.3 and §34.5, and nothing in the register, the Physics Compendium or the main text says what rule it held"** *and* **"§32.4.1's '[N — pair count to be confirmed]' — the closure-under-intersection test over pairs of fixed points has no count anywhere in the record and no script, so the placeholder stands until the test is rerun."** **Both are discharged. §34.4 now carries a full body** — the ν form, what it is, how it was derived, whose it is, its function in the Löwdin solution and its status — **and that closure is recorded, by the entry that opens "RULING 24: §34.4 IS THE CANONICAL STATEMENT OF THE RULE … AND THE BODY NOW GIVES THE RULE".** *§32.4.1 now carries a full body too, on why the recursion is safe, and* **the placeholder "[N — pair count to be confirmed]" occurs nowhere in the main volume.** *No entry records that. The Register names §32.4.1 twice — in 1755 itself and in an entry about Appendix D's re-closure — and neither says the count was taken or the placeholder removed.* **So the owed list is one item shorter than the record shows, and the item that left it did so silently.** Registers 1755. (a correction.)

### 1870

**THE FALSE-UNIVERSAL CLASS HAS ONE MEMBER GONE, TWO CORRECTLY SCOPED, AND ONE THAT TURNS ON A READING THE PASSAGE ITSELF LEAVES OPEN.** *The docket names three:* **"every sequence…", "every verified cell…", "exactly one infinity…"**. *Measured:* **"every verified cell" occurs zero times in the main volume — the member is gone.** *The two "every sequence" sites are* **both scoped by their own words** *—* **"In every sequence examined here"** *and* **"every sequence in this work"** *— which is the qualification the class asks for, so neither is a false universal.* **The third does not resolve from the page.** *§27's passage argues the mathematics is finitary and states* **"There is exactly one infinity in the whole construction and it is a boundary convention — max ∅ = −∞ in §6.1's definition of φ̂"**. *A table four pages earlier prints* **"the pole, §23.7 | y″ = 0 | slack = ∞ where the function does not turn"** *— an infinity arising as a quotient, not as a boundary convention.* **Whether that falsifies the claim depends on what "the whole construction" contains, and the same passage supplies both readings**: it scopes the argument to ℛ, the envelopes and Birkhoff, which excludes §23.7 — and it says two paragraphs earlier that Chapters 6, 10, 14 and 23 "stop being four subjects and become four measurements of one thing", which includes it. *Both readings are recorded and neither is chosen here; the scope is subject matter.* Registers 1870. (a finding.)
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
NEW_ROWS = {}
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
print('BUILD120 -> BUILD121: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD116 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
