#!/usr/bin/env python3
"""r4-a2.py — R4 Batch A item 2: ruling 12 of RULINGS-R4f. §35's g-block bound takes the wider reach
the forward walk measures — no g block THROUGH Z = 125, not below Z = 121 — and register 1837 records
it. BUILD111 -> BUILD112 main.

Ruling 12 (M, 6 September 2026): *"always the most expanded answer, in this case the wider bound."*
"§35's *'There is no g block below Z = 121'* takes the measured bound, **no g block through Z = 125**,
with twelve of twelve blocks above Z = 108 accepted and no reset. And the rule generalises beyond this
site: where two true statements differ only in reach, the volume takes the more expanded one."

Scope, and it is exactly §35's: TWO substitutions, the prose at §35.2 and the provenance row at §35.5,
each anchor asserted unique in the whole bundle. §35.4 says "the finding that there is no g block" with
no bound at all and Appendix D.5.9's index row is likewise unbounded — nothing to widen in either. The
four sibling sites outside §35 that DO print the bound — THE-LOWDIN-SOLUTION-2.md L13, L47 and L114,
and the Mathematical Compendium L3182 — are NOT touched here: whether ruling 12's generalising rule
reaches them is a question standing to M (DRAFT-R4-R3-CORRECTIONS §7).

Usage:  python3 r4-a2.py            dry run (asserts everything, writes nothing)
        python3 r4-a2.py --write    writes staging members + BUILD112 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD111_main_and_register.md')
OLD_M_MD5 = '3d31d58491643d1c6fdee82b18200ad2'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD112_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build112') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the substitutions, count-asserted -------------------------------------------------------------
SUBS = [
    ("There is no g block below Z = 121, and the table did not have to be",
     "There is no g block through Z = 125, and the table did not have to be"),
    ("| **no g block below 121** | the pinned channels,",
     "| **no g block through 125** | the pinned channels,"),
]

ENTRY_N = 1837
ENTRY = """

### 1837

**§35 SAID THERE IS NO G BLOCK BELOW Z = 121 BECAUSE THAT IS WHERE THE WALK STOPPED; CARRIED FORWARD AND RE-FITTED NOWHERE, IT SAYS 125.** *§35.2 and §35.5 print the absence as a bound at Z = 121, and the bound was the data's, not the law's: the listing of observed ground configurations ends at Z = 108 and the chain runs to Z = 120, so 121 was simply the first unwalked charge. Carrying* a *= 1.9840594 out of lawrencium and re-fitting it nowhere, the law walks seventeen further elements as prediction rather than description, and every row is labelled one: 6d at 109–112, 7p at 113–118, 8s at 119–120 —* **twelve of twelve blocks as the accepted table has them, and the law was fitted to none of them** *— with* a *never forced out of its corridor, no reset at all, and t running 0.0492 to 0.6791 (Z = 119 alone has no fraction, where 8s opens and nothing bounds it above).* **And the g block does not open, for a reason the form states exactly: a node-free subshell has p = 0, so ν = n and a drops out of it entirely. 5g sits at ν = 5 for ever while 7d at a = 1.98 sits at 3.03, so for 5g to win, a would have to fall below 1 — and a has risen monotonically since potassium. Through Z = 125 the law never makes a g subshell the entrant, and at 121 itself it is 7d that takes the step.** *Repaired at §35.2 and §35.5 as two guarded substitutions, each anchor asserted unique in the whole bundle before and after, the reverse recovering the predecessor's md5. The pinned-channel measurement register 1704 records — every g channel at −1/(2n²) to storage precision across a hundred protons — is untouched and is what the wider bound rests on; 1704 is append-only and is corrected by this entry rather than edited. §35.4's "the finding that there is no g block" and Appendix D.5.9's index row name no bound and are not touched. Four sites outside §35 print the Z = 121 bound — the Löwdin companion at three places and the Mathematical Compendium's pinned-channel theorem — and they are NOT repaired here; whether this ruling's rule reaches them is M's and stands open.* **M's ruling of 6 September 2026 (RULINGS-R4f, ruling 12): where two true statements differ only in reach, the volume takes the more expanded one.** Registers 1702; 1704; 1712. (a correction.)"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

m = txt[MAIN]
new = dict(txt)
mm0 = m
for a, b in SUBS:
    assert mm0.count(a) == 1, 'anchor not unique in the volume: %r %d' % (a[:40], mm0.count(a))
    assert mm0.count(b) == 0, 'the repair is already in place: %r' % b[:40]
    mm0 = mm0.replace(a, b)
new[MAIN] = mm0
for a, b in SUBS:
    assert new[MAIN].count(b) == 1 and new[MAIN].count(a) == 0
assert new[MAIN].count('below Z = 121') == 0 and new[MAIN].count('below 121') == 0, 'a Z = 121 bound survives in the main volume'
assert new[MAIN].count('through Z = 125') == 1 and new[MAIN].count('through 125') == 1

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0, 'entry %d already seated' % ENTRY_N
assert r.count('### %d\n' % (ENTRY_N - 1)) == 1, 'entry %d is not seated' % (ENTRY_N - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
new[REG] = r.rstrip('\n') + ENTRY + '\n'
for a, b in SUBS:
    print('OLD  %s\nNEW  %s' % (a, b))
print('main volume: no "below Z = 121" and no "below 121" left; §35.4 and D.5.9 name no bound and are untouched')

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
print('register_cites with %d: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %d entries'
      % (ENTRY_N, CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, len(TOP)))
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
          lambda mm_: '%s entries, 1 to %d, at this build (2026-09-06)' % (g(c['headings']), c['highest']), 'main: at this build')
mm = sub1(mm, r'436 entries when this paragraph was written, (\d[\d,]*) at this build',
          lambda mm_: '436 entries when this paragraph was written, %s at this build' % g(c['headings']), 'main: N at this build')
mm = sub1(mm, r'at this build the main volume cites (\d+) entries',
          lambda mm_: 'at this build the main volume cites %d entries' % CITED_MAIN, 'main: cites N')
new[MAIN] = mm
for a, b in SUBS:
    assert new[MAIN].count(b) == 1 and new[MAIN].count(a) == 0, 'a section 35 repair did not survive the count pass'

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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD111 md5 mismatch'
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
print('BUILD111 -> BUILD112: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD112 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
