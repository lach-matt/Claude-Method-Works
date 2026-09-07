#!/usr/bin/env python3
"""r4-b1.py — Phase 1's first seven entries: the subject matter its instruments settled.
BUILD121 -> BUILD122 main.

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
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD121_main_and_register.md')
OLD_M_MD5 = 'b8bd8573e4de422b190f7a40660d3aab'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD122_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build122') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = tuple(range(1871, 1875))
ENTRIES = """
### 1871

**§23.10.2 SAYS ITS CORRECTION IS RECORDED AT 96–98 AND ALL THREE ARE SUPERSESSION STUBS POINTING AT AN ENTRY ABOUT SOMETHING ELSE.** *§23.10.2 withdraws an earlier reading —* **"An earlier draft claimed V stays near 2 at matched order and that Q9's conclusion — bounds becoming relatively worthless as data accumulates — was an artefact. That was wrong twice over, and the correction is recorded at 96–98."** *Registers 96, 97 and 98 read, all three identically:* **"SUPERSEDED (Λ₈ successor development); see register 313."** *They carry no correction of V, of matched order or of Q9.* **And register 313 is "TIME MUST NOT ENTER Λ WAS A MISSTATEMENT" — refuted by computation, about Λ₈ carrying time and Λ₉ composing.** *Nothing to do with either claim §23.10.2 withdraws.* **The same section cites the same run again, twenty-nine lines later, as "withdrawn at correction 97".** *So a withdrawal is announced twice against a three-entry range, the range is three stubs, and the entry they forward to is on another subject: the correction §23.10.2 rests on is recorded nowhere. Recorded, not repaired; which entry should carry it is subject matter.* Registers 96; 97; 98; 313. (a finding.)

### 1872

**§34.6 SAYS EACH SUBSHELL FILLS AT CONSTANT `a` AND THREE SUBSHELLS DO NOT; THE DOCKET'S OWN INSTANCE OF THE FAULT IS AT AN ELEMENT WHERE NOTHING MOVES.** *§34.6 states both halves in one breath:* **"It never resets mid-subshell, which is why each subshell fills at constant `a`."** *Measured on the seated walk, the two halves part company.* **The first is true of the entering subshell: eight of the nine real moves are at the entrant's own opening and the ninth is Hg, a return from an exception.** *The second is false.* **The 5d shell carries a real move at Ce 58, the 6d at Pa 91 and again at Lr 103; every other subshell is constant.** *So `a` does move inside a subshell — three times — and it never moves inside the subshell it is entering, which is the distinction the sentence collapses.* **And the docket names the wrong elements**: it carries the fault as failing at Mo 42 and Rh 45, and at molybdenum the recalibration is a boundary touch with `a` unchanged. *The claim that fails is the second, at three elements the docket does not name. Measured by `walkresets.py` against the seated ground configurations.* Registers 1333; 1350. (a correction.)

### 1873

**THE ORDERING LAW NAMES THREE EXCEPTIONS AND THE SEATED CONFIGURATIONS GIVE TWO.** *The law is printed as* **"A channel of smaller n+ℓ opens before a channel of larger n+ℓ without exception; at equal n+ℓ, smaller n first, except at exactly La, Ac and Th."** *Walked over the 108 seated ground configurations, recording the element at which each subshell first opens:* **the first clause holds with no exception at all, and the second is violated exactly twice — 5d opens at La 57 before 4f at Ce 58, both n+ℓ = 7; and 6d opens at Ac 89 before 5f at Pa 91, both n+ℓ = 8.** *Thorium produces no ordering violation.* **Its anomaly is of another kind and the law's clause does not describe it**: *thorium's ground configuration carries no 5f at all, so it delays an opening rather than reordering two. Naming it beside La and Ac reads a second phenomenon into a clause about the first.* **The law's own claim that the exceptions are derived rather than excused is untouched** — *all three are f-openings and the collapse condition is stated for all three; what falls is "exactly", and with it the count. Measured against `LW1-ground.py`, the seated observed configurations.* Registers 1873. (a correction.)

### 1874

**§12.11.1 CITES ITSELF FOR A NOMINAL VALUE IT NEVER STATES, AND REGISTER 241 CARRIES THE CITATION FORWARD.** *Inside §12.11.1, at L3146, the volume reads* **"converging on the ⅔ that §12.11.1 states as its nominal value"**. *The section runs L3037 to L3367.* **In the whole of it the character ⅔ occurs twice, and both occurrences are inside that one sentence — the reference to §12.11.1 stating a nominal value, and the comparison against it in the next clause.** *§12.11.1 states no nominal value anywhere.* **So a section cites itself for a claim it does not make**, *which a pointer audit cannot catch because the target section exists and the pointer resolves to it.* **Register 241 repeats the citation** — *"THE THIRTEENTH AXIS'S DENSITY RISES WITH THE CAPS — 64.4, 64.5, 65.7, 66.1% — TOWARD THE ⅔ §12.11.1 STATES AS NOMINAL"* — *so the record now carries a figure attributed to a site that does not hold it. The four measured densities are not in question and neither is their trend; what has no home is the value they are said to approach.* Registers 241. (a finding.)
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
print('BUILD121 -> BUILD122: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD116 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
