#!/usr/bin/env python3
"""r4-a4.py — R3 completion, item B1 of `docs/R3-REPAIR-PLAN.md`: register 1450 credits Belokolos
(2017) with the period-two structure, and Kitagawara & Barut published it in 1983. Register 1839
records the priority. BUILD113 -> BUILD114 main.

M, 6 September 2026: *"complete R3 please."* B1 is the one item of the twenty-one that was ready:
twelve were already done, three corrections do not survive contact with the record, one must not be
worked because it would resolve an open ruling, two are blocked on measurements and one waits on the
ruling the plan itself asks for. See `method/R3-COMPLETION.md`.

NO VOLUME CHANGES. This is Batch B — a Register entry is never edited, and the repair is a new
appended entry citing the superseded one. The count classes are re-taken in the same build.

The attribution was verified in the outside literature rather than taken from the correction:
  Y. Kitagawara and A. O. Barut, "Period doubling in the n + l filling rule and dynamical symmetry
  of the Demkov-Ostrovsky atomic model", J. Phys. B 16 (1983) 3305-3327; and the sequel, "On the
  dynamical symmetry of the periodic table II: modified Demkov-Ostrovsky atomic model",
  J. Phys. B 17 (1984) 4251-4259.

Usage:  python3 r4-a4.py            dry run (asserts everything, writes nothing)
        python3 r4-a4.py --write    writes staging members + BUILD114 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD113_main_and_register.md')
OLD_M_MD5 = '9877ce8af55cc842e561f3febb9d1bf2'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD114_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build114') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_N = 1839
ENTRY = """

### 1839

**THE PERIOD-TWO STRUCTURE REGISTER 1450 CREDITS TO 2017 WAS PUBLISHED IN 1983, AND THE SEARCH THAT FOUND THE REST OF THE LITERATURE MISSED IT.** *Register 1450 — the precedent search on the Löwdin challenge, owed since the work began — closes:* **"Belokolos also gives the period lengths in closed form, L_M = 2(⌊M/2⌋+1)², so the period-two structure this session found from node-count invariance under (n,ℓ)→(n+1,ℓ+1) is a restatement of a published formula. Correct, and not new."** *The credit is thirty-four years late.* **Period doubling in the n + ℓ filling rule was derived, and derived from a dynamical symmetry rather than stated as a formula, by Y. Kitagawara and A. O. Barut, *"Period doubling in the n + ℓ filling rule and dynamical symmetry of the Demkov–Ostrovsky atomic model"*, J. Phys. B **16** (1983) 3305–3327, with the sequel *"On the dynamical symmetry of the periodic table II: modified Demkov–Ostrovsky atomic model"*, J. Phys. B **17** (1984) 4251–4259.** *They show that the degeneracy algebra of the Demkov–Ostrovsky equation does not close under the usual commutation relations but does under a generalised set, and that the period doubling follows from the structure of that algebra. The model is the same one register 1450 already credits to Demkov & Ostrovsky (1972) and already carries Thyssen & Ceulemans' objection to, so this attribution lands inside an entry that had done its literature search once and stopped one paper short.* **One distinction is kept rather than blurred: 1450 credits Belokolos with the CLOSED FORM L_M = 2(⌊M/2⌋+1)², and Kitagawara & Barut's result is the DOUBLING and its dynamical-symmetry origin. This entry corrects the priority of the period-two structure; it does not claim the closed form is also earlier, because that has not been checked.** *Verified in the outside literature at this build and confirmed twice, not taken from the correction that raised it; the correction was chat-witnessed and named no citation. Kitagawara appears nowhere else in this corpus. R-ATTR: all attributions that can be made are made.* Registers 1450. (a correction.)"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

new = dict(txt)

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0, 'entry %d already seated' % ENTRY_N
assert r.count('### %d\n' % (ENTRY_N - 1)) == 1, 'entry %d is not seated' % (ENTRY_N - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
new[REG] = r.rstrip('\n') + ENTRY + '\n'

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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD113 md5 mismatch'
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
print('BUILD113 -> BUILD114: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD114 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
