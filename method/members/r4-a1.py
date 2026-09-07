#!/usr/bin/env python3
"""r4-a1.py — R4 Batch A item 1: ruling 11 of RULINGS-R4f. §34.4's "No parameter is fitted" takes
the "in the form" qualifier §34.8 already carries five lines below it, and register 1836 records the
repair. BUILD110 -> BUILD111 main.

Ruling 11 (M, 6 September 2026): *"yes."* — "§34.4 repairs with its class. *'No parameter is fitted'*
takes the *'in the form'* that §34.8 already carries, in the withdrawn-law class held for R3."

Scope, and it is exactly the ruling's: ONE substitution at §34.4. The bare string
"No parameter is fitted" occurs three times in the main volume — §34.4 L9602, §34.8 L9693 (which
already carries the qualifier) and §35.5 L9904 (a different chapter, outside the ruling) — so the
anchor is the long form, asserted unique in the whole bundle, and the bare string is never used.
Register 1350 carries the same unqualified sentence and is append-only: it is cited by 1836, not
edited.

Usage:  python3 r4-a1.py            dry run (asserts everything, writes nothing)
        python3 r4-a1.py --write    writes staging members + BUILD111 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD110_main_and_register.md')
OLD_M_MD5 = 'e1264def2a04df9ac010db3f0ea90953'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD111_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build111') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the substitution, count-asserted -------------------------------------------------------------
SUB_OLD = "**No parameter is fitted**; the provenance of every term is §34.8's"
SUB_NEW = "**No parameter is fitted in the form**; the provenance of every term is §34.8's"

ENTRY_N = 1836
ENTRY = """

### 1836

**§34.4 SAID "NO PARAMETER IS FITTED" AND §34.8 SAID IT WITH THE QUALIFIER FIVE LINES LATER; THE RULE'S OWN SECTION NOW CARRIES IT TOO.** *§34.4 closes its derivation with* **No parameter is fitted** *unqualified, and §34.8 — the provenance table it points the reader to in the same sentence — closes with* **No parameter is fitted in the form; the placement of a along the walk is a fit (register 1445)**. *Register 1445 is what makes the difference load-bearing: placing a from each step's own corridor scores 99 of 106, held out properly it scores 90, and plain Madelung, which takes no free parameter at all, scores 96. So the unqualified sentence is the one the record has already withdrawn, and it stood in the section that states the rule. Repaired here as one guarded substitution at §34.4, the anchor asserted unique in the whole bundle before and after and the reverse substitution recovering the predecessor's md5; the form is untouched and only the qualifier moves.* **Not touched, and each for its own reason: §34.8 already carries the qualifier and is the sentence being matched; §35.5's "No parameter is fitted. No observation enters upstream of the score." is Chapter 35's claim about the walk's score and is outside this ruling; and register 1350, which prints the same unqualified sentence, is append-only and is corrected by this entry rather than edited.** *M's ruling of 6 September 2026 (RULINGS-R4f, ruling 11): the withdrawn-law class held for R3.* Registers 1350; 1445. (a correction.)"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

m = txt[MAIN]
assert m.count(SUB_OLD) == 1, 'anchor not unique in the volume: %d' % m.count(SUB_OLD)
assert m.count(SUB_NEW) == 0, 'the repair is already in place'
assert m.count('No parameter is fitted') == 3, 'the volume no longer carries three sites'
new = dict(txt)
new[MAIN] = m.replace(SUB_OLD, SUB_NEW)
assert new[MAIN].count('No parameter is fitted') == 3 and new[MAIN].count(SUB_NEW) == 1
assert len(new[MAIN]) == len(m) + len(' in the form')

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0, 'entry %d already seated' % ENTRY_N
assert r.count('### %d\n' % (ENTRY_N - 1)) == 1, 'entry %d is not seated' % (ENTRY_N - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
new[REG] = r.rstrip('\n') + ENTRY + '\n'
print('§34.4  %r' % SUB_OLD)
print('   ->  %r' % SUB_NEW)
print('main volume: 3 sites of "No parameter is fitted" before and after; §34.8 and §35.5 unchanged')

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
assert new[MAIN].count(SUB_NEW) == 1 and new[MAIN].count('No parameter is fitted') == 3, 'the §34.4 repair did not survive the count pass'

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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD110 md5 mismatch'
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
print('BUILD110 -> BUILD111: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD111 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
