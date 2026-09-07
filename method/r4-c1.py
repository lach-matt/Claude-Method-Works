#!/usr/bin/env python3
"""r4-c1.py — the six entries M's rulings of 7 September 2026 seat.
BUILD124 -> BUILD125 main.

`RULINGS-R4g.md` carries the rulings; this is their execution. Phase 2's last eight open rows
reduced to three questions, they were put to M in question form, and these are the answers.

  1880  RULING 1. The Request-3 bracket result. Drafted for number 1836, which a later build spent;
        a Register number is assigned at seating, so it takes the next free one. UNTAGGED, which is
        ruling 1(b)'s mechanism for "both": kinds.py collapses to one kind only when a tag is
        present, and an untagged headline carrying a digit is counted a measurement AND a finding.
        Re-run at this build by the seated r3-br-measure.py; factor.py seats with it, byte-exact.

  1881  RULING 2. The agreement theorem's converse, staged as 1797 and never seated. The hole at
        1797 stays a hole: a Register number is not reused. method/proofs/agreement.py (17/17)
        reproduces every figure, and asserts R returns the book's printed E = 36 for the periodic
        table before it is trusted on anything else.

  1882  RULING 3(c). ground.py delivered and reproduced.
  1883  RULING 3(c). The three-body audit, re-run from a reconstruction.
  1884  RULING 3(c). N8 and the withdrawn polynomial.
  1885  RULING 3(c). Routh's threshold, computed.
        All four from READ-intake1.md section C, whose numbers 1795-1798 were spent. Each rests on a
        delivered script and its banked log, both seated members; method/proofs/intake.py (44/44)
        re-runs every one of them before any of these is seated.

WHAT IS NOT HERE. Ruling 3(b) — the twelve entries asserting what a chat withdrew — is a repair pass
and not a seating: each is a new appended entry citing the superseded one, and each is owed the
exhaustive chat review ruling 3(a) makes a condition. None of it is done in this build and the W text
says so.

NO VOLUME CHANGES. This is a Batch B pass: a Register entry is never edited and nothing is repaired
in a volume by it. The count classes are re-taken in the same build.

Usage:  python3 r4-c1.py            dry run (asserts everything, writes nothing)
        python3 r4-c1.py --write    writes staging members + BUILD125 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD124_main_and_register.md')
OLD_M_MD5 = '0790075ae2a72859809e9ec3486ad9d2'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD125_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build125') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = (1880, 1881, 1882, 1883, 1884, 1885)
ENTRIES = """
### 1880

**REGISTER 334'S SENTENCE IS PROVED DOWN THE WHOLE TOWER: THE STRICT MAP FROM A STAGE'S RANKS TO THE NEXT IS REFUTED WITH BRANCHING FOUR TO NINE, THE BRACKET IS A GAP-FREE MONOTONE INTERVAL AT EVERY STAGE, AND THE 1D CHAIN LIES INSIDE THE IMAGE FROM Λ₁₃.** *Register 334 recorded, at Λ₁₃'s entry into a larger index, that composition seen from above is a bracket rather than a map, and §12.11.0.12 prints it; §12.11.0.11 bounds the fourteenth axis from inside. The original-works return of 2026-08-28 tested the factorisation lemma on the rebuilt tower.* **At each of the five consecutive stages, Λ₉ → Λ₈ up to Λ₁₃ → Λ₁₂, the rank below a cell — its rank less its new coordinate — is not a function of the rank above: the fibre over a rank branches 4, 4, 6, 8 and 9 ways, growing with height, so the map form of a single transition does not exist.** *Every fibre is a gap-free interval of ranks whose two endpoints are non-decreasing in the rank above, with no exception across all 199,130 cells of Λ₁₃; the five stage-brackets composed from χ(Λ₁₃) to χ(Λ₈) contain the direct bracket with slack at most 2 rank units, §22's outward rule appearing inside the tower; and the projection of Λ₁₃ onto Λ₈'s eight coordinates reaches every rank of χ(Λ₈), 3 to 20, so the 1D chain — the tower's terminal object under the rank-to-chain coarsening — lies entirely inside the image from the top, while the fourteenth direction is the same system's limit.* **THE CONNECTION BETWEEN THE TOWER'S TWO ENDS IS A BRACKET, NOT A MAP, AND IT CARRIES AT FULL RESOLUTION**: no bit-encoding enters, and the binary-only form of the thesis is refused, a reading derived from the object being a function of it. *Register 334's 44 rank values at Λ₁₃ reproduce, the counts running 18, 21, 24, 29, 36, 44 from Λ₈ up. Its prose placement belongs to the time chapter, and the Mathematical Compendium prints no object for the bracket system — an expansion owed there and not written here. Every figure above was re-derived before this entry was written, on a rebuild of the tower from its own seated generators, and the return's own script is seated beside them so that the derivation can be repeated rather than believed.* Registers 249; 315; 333; 334.

### 1881

**THE AGREEMENT THEOREM'S "ONLY IF" HALF HAS A COUNTEREXAMPLE, AND IT IS THE BOOK'S OWN MATHEMATICAL OBJECTS: THE GRADING (STATUS, VERIFICATION, PRECEDENT) OVER SEVENTY-SEVEN OF THEM HOLDS 11 CELLS OF A 16-CELL BOX, EVERY ONE OF THE FIVE OPERATOR-BEARING LANGUAGES ADMITS THE SAME 13, AND E = 2.** *Register 1176 states E(X) = 0 if and only if the languages agree — six indexes, three operators, without exception.* **Measured on the seated element list, with all three coordinates ordinal by construction — withdrawn < conjectured < measured < verified < proved; cited < sampled < exhaustive; none found < found — so the reading rests on no lexicographic fallback and the run carries no such warning: order, algebra, geometry, information and statistics return IDENTICAL admitted sets, which is agreement in the strongest sense the method has, and the index lacks two of them —** *measured · exhaustive · found* **and** *verified · sampled · found*, **each a grading a mathematical object could carry and neither occurring among the seventy-seven.** *The "if" half is untouched: every index measured that closes does have its languages agree. It is the converse that fails, and the census had already flagged the wording — a marked over-generalisation on this entry's* **without exception**. *Two further readings of the same elements are recorded and are not defects: with kind and discipline on axes the object is wide open at E = 492, which is register 1356's fault and not a finding; and* **all 24 fibres close at E = 0 in all five languages**. *The operator used is the corpus's own, and it was required to return the book's printed E = 36 for the periodic table before it was trusted on this object at all.* Registers 1176; 1173. (a correction.)

### 1882

**THE OBSERVED-CONFIGURATION SCRIPT WAS DELIVERED AND REPRODUCES: THE TABLE OF REGISTER 1306 RUNS AGAIN, 108 OF 108, NINETEEN OPENINGS, TWO TRANSPOSITIONS FROM MADELUNG.** *Delivered 2026-09-01 as produced and unaltered since — the copy this book seats has the fingerprint the delivery recorded, and its printed log reproduces byte for byte when the script is run again here.* **The 108 configurations equal this book's independent reconstruction from the spectroscopic listing cell for cell, and the electron count checks at 108 of 108.** *The filling sequence read back from the configurations opens nineteen subshells across Z = 1 to 108, and the two departures from Madelung's rule are adjacent transpositions: 5d before 4f, and 6d before 5f.* **A delivery that reproduces is a different fact from a delivery that agrees**, and both hold here. Registers 1306; 1307.

### 1883

**THE THREE-BODY AUDIT RUNS AGAIN FROM A RECONSTRUCTION: 78 OF 78, CAP 8 AT 344 CELLS WITH 8,385 MEET FAILURES AND NONE OF JOIN, THE TWO-BODY CHAIN AT ZERO, AND THE FIRST-RUN FAILURE 13 OF 13 IN ONE COLUMN.** *No file of the session survives; the instruments were recovered from its transcript, seated, and re-run.* **Every printed figure of registers 1716 to 1718 reproduces: thirteen labelled mass cases against six checks each is seventy-eight, and all seventy-eight pass; the closure figures reproduce under an independent operator at every cap from 3 to 12, where the two-body chain fails nowhere.** *The first run's failure is preserved beside the corrected one and is instructive: its shape column reads false on all thirteen cases, which is one defect at one line and not thirteen defects.* **One figure in the draft this entry comes from is NOT re-derived here and is marked rather than carried:** *that the thirteen cases realise twelve orderings, the thirteenth being z < x < y. Two of the thirteen labels fix one element as extreme and leave the remaining pair open, so the count is a reading of the enumeration and not a figure the log prints; it is where that claim would have to be settled, and it is left open.* Registers 1716; 1717; 1718; 1722.

### 1884

**N₈ AND THE WITHDRAWN POLYNOMIAL, BOTH RUN: THE NORM IS THE PRODUCT OVER THE EIGHT SIGN CHOICES, AND THE WITHDRAWN QUARTIC TERM IS 2p² + 16q WHERE THE TRUE ONE IS 6p² − 8q.** *Symbolic identity, zero remainder.* **The compact form is the norm and the previously claimed form is not; the constant term factors as four squared linear forms — (u₁ − u₂ − u₃)² (u₁ − u₂ + u₃)² (u₁ + u₂ − u₃)² (u₁ + u₂ + u₃)² — which is degree eight, one factor for each of the 2³ sign choices, paired by overall sign.** *Written in p and q, the elementary symmetric functions of u₁², u₂², u₃², the withdrawn quartic coefficient is 2p² + 16q against the true 6p² − 8q, a difference of −4p² + 24q that is not zero; the quadratic term differs likewise. And N₈ vanishes at u = (3, 5, 7), V = 15.* **The p and q form was not taken from the draft**: it was reduced here from the delivery's own printed expressions, evaluated exactly on integers. Registers 1719; 1720.

### 1885

**ROUTH'S THRESHOLD, CITED IN THE RECORD, IS NOW COMPUTED: μ₁ = (9 − √69)/18 = 0.0385208965, THE ROOT OF 27μ(1 − μ) = 1 BELOW ONE HALF.** *Solved from the equation rather than quoted: 27μ − 27μ² − 1 = 0 has discriminant 621, and √621 = 3√69, so the smaller root is (9 − √69)/18 exactly.* **It agrees with the 0.0385209 the record prints at seven places, half-up, and the delivered check says so in its own log.** *A threshold the record had carried as a citation now carries a derivation.* Registers 1717. Prior art: Routh 1875.
"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

new = dict(txt)

r = txt[REG]
for _n in ENTRY_NS:
    assert r.count('### %d\n' % _n) == 0, 'entry %d already seated' % _n
assert r.count('### %d\n' % (ENTRY_NS[0] - 1)) == 1, 'entry %d is not seated' % (ENTRY_NS[0] - 1)
assert r.rstrip().split('\n')[-1].startswith('**'), 'the Register does not end on an entry body'
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
stage = tempfile.mkdtemp(prefix='r4-c1-')
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

# A row crossing seven citations is a HAND ACT and the instrument refuses to derive one.
# Any name appearing here is written by hand; an empty dict means this build claims none, and
# the assertion below stops the build if the >=7 set moved anyway.
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD124 md5 mismatch'
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
print('BUILD124 -> BUILD125: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD125 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
