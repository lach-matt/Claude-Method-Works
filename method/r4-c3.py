#!/usr/bin/env python3
"""r4-c3.py — E-012's two remaining items, the last measurable rows of Phase 2.
BUILD126 -> BUILD127 main.

DEFERRED's chat-76 line filed three sites against §12.11.1 "for R3, no withdrawal". One,
12s-02, is seated at register 1874. The other two are seated here, behind
`method/proofs/kparent.py` (20/20).

  1888  12q-03. Register 434 pairs 12.7 % against 31.4 % and calls the gap the double
        charge. The volume's own sentence pairs 12.7 % against 30.8 % and calls it
        eighteen points. 31.4 % is the density over the stage below — a different
        population from the one the numerator is computed on.

  1889  12q-04 and 12s-04, which are one reading in two places. §12.11.1 DEFINES f_max as
        the cap on f, "NOT the cell's own f", and says the bound 2K ≤ 2J_c + 2f_max "has
        one parent". The same chapter then writes "K's parents are J_c and f", and register
        1790's edge count is built on that reading — its second cycle, 2J_c–2K–f–g–q–k, is
        the edge the definition forbids.

WHAT THE CORRECTION COSTS, MEASURED ON THE SEATED GRAPH INSTRUMENT WITH ONLY THE AXIS-12
EDGE LIST SUBSTITUTED: fourteen edges become thirteen and the cycle rank falls from 2 to 1
at Λ₁₂ and Λ₁₃. **The triangle is untouched** — 2S′–g–v stands at every stage from Λ₁₀,
the hub k keeps degree 4, and §21.5.1's one-level shortfall stands. Only 2K and f change
degree at all. So register 1790's finding survives its own arithmetic error, and the entry
says so rather than letting a falling cycle rank read as a retraction.

NO VOLUME CHANGES. Batch B. The count classes are re-taken in the same build.

Usage:  python3 r4-c3.py            dry run
        python3 r4-c3.py --write    writes staging members + BUILD127 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD126_main_and_register.md')
OLD_M_MD5 = 'ba8ee92f30a623f6cbebcd32831c2e5d'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD127_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build127') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = (1888, 1889)
ENTRIES = """
### 1888

**REGISTER 434 PAIRS THE DOUBLE CHARGE WITH THE WRONG DENOMINATOR: 12.7 % AGAINST 31.4 % SETS A NUMERATOR TAKEN ON ONE POPULATION BESIDE A DENSITY TAKEN ON ANOTHER, AND THE VOLUME'S OWN SENTENCE PAIRS 12.7 % AGAINST 30.8 %.** *§12.11.1's density column needs two conditions the definition implies and the text omitted, and register 434 states both: the sum runs over the stage below rather than over Λ₈, and each envelope is priced once, so filtering axis 12's numerator on whether J_c is physically realised charges axis 11 a second time.* **Both conditions stand. What does not is the pair of numbers the entry closes on.** *31.4 % is the density of axis 12 computed over the stage below — the stated value, and the third of a percentage point per stage that runs 30.8 % over Λ₈, 31.1 % over Λ₉ and 31.4 % over Λ₁₀ is the first condition working exactly as the entry says it does.* **The 12.7 % is the double-charged figure, and it is computed over Λ₈. So the entry sets a Λ₈ numerator against a Λ₁₀ denominator and calls the difference the double charge.** *The volume's own text pairs them correctly four lines later —* **"12.7 % against 30.8 %, an eighteen-point gap that is entirely the double charge"** *— and 30.8 − 12.7 = 18.1, which is the eighteen points it names; 434's pairing gives 18.7 for a quantity it describes the same way.* **Nothing about the double charge is withdrawn and no density is re-derived here**: the correction is that the entry's closing comparison crosses two populations where the volume's does not. Registers 434. (a correction.)

### 1889

**THE CHAPTER DEFINES f_max AS A CAP AND SAYS THE BOUND HAS ONE PARENT, THEN GIVES K TWO PARENTS TWICE — AND REGISTER 1790'S EDGE COUNT IS BUILT ON THE READING ITS OWN CHAPTER FORBIDS.** *§12.11.1's vocabulary block defines the term outright:* **"f_max — the cap on f under §7.4, not the cell's own f. The distinction is the whole of §12.11.5: the bound 2K ≤ 2J_c + 2f_max has one parent and preserves the tree and the cylinder; the same bound written with the cell's f has two parents and breaks the factorisation."** *The book therefore states which reading is right. Two places then use the other one:* **the same chapter writes "K's parents are J_c and f", and register 1790's constraint graph names a second cycle 2J_c–2K–f–g–q–k, which exists only if the edge from f to K exists.** *Measured on the seated graph with nothing changed but axis 12's edge list:* **fourteen edges become thirteen, and the cycle rank falls from 2 to 1 at Λ₁₂ and at Λ₁₃ — from (0, 0, 1, 1, 2, 2) to (0, 0, 1, 1, 1, 1).** *What does not move is the finding.* **The triangle 2S′–g–v stands at every stage from Λ₁₀, the triangle count is (0, 0, 1, 1, 1, 1) under both readings, the hub k keeps degree 4 with g also at 4, and Λ₈ is a tree at seven edges either way — so §21.5.1's one-level shortfall, ℛ at level 2 against strong 3-consistency, stands untouched.** *Only 2K and f change degree at all, each from three to two.* **Register 1790's conclusion survives its own arithmetic; the second cycle does not**, and Figure 21.1 and §21.5.3's table, which 1790 already records as owed at the prose pass, are owed the corrected edge count with them. Registers 434; 1790. (a correction.)
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
stage = tempfile.mkdtemp(prefix='r4-c3-')
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD126 md5 mismatch'
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
print('BUILD126 -> BUILD127: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD127 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
