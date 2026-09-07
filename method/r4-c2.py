#!/usr/bin/env python3
"""r4-c2.py — ruling 3(b): the withdrawals that were never seated.
BUILD125 -> BUILD126 main.

M ruled on 7 September 2026 (`RULINGS-R4g.md` §3) that a chat transcript IS a source a
repair may be made from, provided the chat is reviewed exhaustively, and that findings are
recorded AND repaired. DEF-153P-PENDING filed twelve entries as asserting what a chat
withdrew. `method/proofs/withdrawn.py` (32/32) reads the class the other way round — the
store's rule is that an entry is never edited and the repair is a NEW APPENDED ENTRY, so a
correctly repaired entry carries no marker inside itself, which is what the branch's test
looked for.

  TEN OF THE TWELVE WERE ALREADY REPAIRED, each by a later entry carrying the correction's
  own figure: 230 by 1819, 314 by 1841, 599 by 601, 602 by 1820, 807 by 823, 1395 by 1426,
  1450 by 1839, 1461 by 1463, 1595 and 1628 by 1629.

  THREE WERE NOT — 500, 502 and 1148 — and the kappa withdrawal is wider than the list: the
  same chat message withdraws 497, 498 and 499 in the same table and marks 501 as surviving.

  1886  the kappa apparatus: 497, 498, 499, 500 and 502 withdrawn, 501 survives.
  1887  register 1148's structural flaw at Sr I nd, which is not there.

WHAT IS NOT CLAIMED. Neither replacement figure is re-derivable from anything this
repository holds — the thirteen-base refit under a second heuristic, and the 311-channel
defect table — and both entries say so on their face. What IS re-derived is the arithmetic
that makes each retraction true at all, and `withdrawn.py` carries it.

NO VOLUME CHANGES. Batch B: a Register entry is never edited and nothing is repaired in a
volume by it. The count classes are re-taken in the same build.

Usage:  python3 r4-c2.py            dry run
        python3 r4-c2.py --write    writes staging members + BUILD126 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD125_main_and_register.md')
OLD_M_MD5 = '9c03bd27fa8c8f6d384d5341260d1874'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD126_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build126') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = (1886, 1887)
ENTRIES = """
### 1886

**THE κ APPARATUS DOES NOT SURVIVE A SECOND HEURISTIC: FIVE ENTRIES ARE WITHDRAWN, THE +0.980 CORRELATION IS AN ARTEFACT OF ONE ALGORITHM'S FAILURE MODE, AND WHAT REMAINS IS THE TIGHTNESS IDENTITY.** *Registers 497 (the seed cost of an axis is driven by its parent count, one-parent axes at +1 and +2 against two-parent at +10 and +11), 498 (a two-parent axis costs a + 4), 499 (cost = a + κ(base)), 500 (κ = S/4 − 1 at a correlation of +0.980) and 502 (the second variable is the base's alphabet depth) are* **WITHDRAWN**. *Register 501 —* **2S is the tight-pair count** *— survives, exact and independent of any seed measurement.* **MEASURED UNDER GREEDY SET COVER, A TWO-PARENT AXIS COSTS ONE OR TWO CELLS, WHICH IS WHAT A ONE-PARENT AXIS COSTS: +2, +2, +2 on the down-set base at d = 3, c = 3, and +1, +1, +2 on those at d = 4 and d = 5 — against the +7 to +11 the earlier heuristic returned on the same bases.** *Refitting κ against S under the second algorithm gives a coefficient of* **−0.079 at rms 0.999**, *against register 500's slope of 0.2506 at rms 0.62.* **The +0.980 was tracking the first heuristic's failure mode, which worsens where the base is tighter — so it correlated with the envelope-step count because the algorithm degrades there, not because the seed grows.** *The cause is one sentence and it is a rule of the method violated: twelve cycles of fitting to a single algorithm's output, every fit confirmed against numbers from that same source. That is §4.6's forbidden shape, sustained through six consecutive cycles, and it was caught only when the definition — G is a seed exactly when φ̂(G) = φ̂(X) — forced a different algorithm to be written.* **WHAT SURVIVES IS NAMED SO THE WITHDRAWAL IS NOT READ AS A DEMOLITION**: the definition itself, the set-cover reading, linearity in d with slope one over both families (down-set d + c − 1, box d + c − 2), the Carathéodory lower bound, seed(ℛ(X)) + E for open indexes, and seed(Λ₈) between 5 and 7. *The refit over the thirteen bases is not re-derivable from what this store holds, and this entry does not claim it is; the figures above are the measurement that withdrew the five, recorded as such.* Registers 497; 498; 499; 500; 501; 502. (a withdrawal.)

### 1887

**THE STRUCTURAL FLAW AT Sr I nd IS NOT THERE: THE BOUND IS ON THE INTEGER PART, ⌊2.38⌋ = 2 = B, AND THE REPAIR BUILT FOR IT WAS A REPAIR FOR NOTHING.** *Register 1148 recorded Sr I nd as a structural flaw because its measured defect δ = 2.38 exceeds B = 2, and recorded in the same breath that the version built to fix it failed — rms 0.3105 against 0.2321, with the polarisability driven negative at a degenerate corner.* **BOTH HALVES FALL TOGETHER, AND REGISTER 910 IS WHY: δ mod 1 is the Schrödinger observable and the integer part is assigned convention, the solution depending only on cos πδ and sin πδ. The bound is a bound on ⌊δ⌋.** *And ⌊2.38⌋ = 2 = B, so it is satisfied.* **COUNTED OVER THE COMPENDIUM'S CHANNELS: δ exceeds B at 176 of 311; ⌊δ⌋ exceeds B at 0 of 311; ⌊δ⌋ equals B exactly at 178 of 311, 57 %; and ⌊δ⌋ ≤ B at 311 of 311.** *So δ runs above B whenever ⌊δ⌋ = B and the fraction is positive, which happens in more than half the compendium and violates nothing. The entry compared δ against a bound on ⌊δ⌋ and called the mismatch a flaw, then built a repair for it.* **AND WHAT REPLACES THE FLAW IS SHARPER THAN THE FLAW WAS.** *Fitting δ mod 1 — the observable, on [0,1) — gives a circular rms of* **0.274 against about 0.29 for guessing uniformly**, *so the equation's apparent success at rms 0.244 and R² 0.924 is mostly the integer part, which the Pauli bound supplies for nothing.* **The integer part is nearly determined — 57 % exact, 100 % bounded — and the fraction, which is where the physics is, is not predicted at all.** *The 311-channel table is not held here and those figures are the measurement's own; what is re-derived at this build is the arithmetic the retraction turns on.* Registers 910; 1148. (a withdrawal.)
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
stage = tempfile.mkdtemp(prefix='r4-c2-')
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD125 md5 mismatch'
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
print('BUILD125 -> BUILD126: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD126 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
