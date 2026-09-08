#!/usr/bin/env python3
"""r4-a8.py — register 1880's owed expansion is not owed, and the entry that says it is stands.
BUILD129 -> BUILD130 main and BUILD305 -> BUILD306 compendia, in one build.

THE FINDING.  Register 1880 closes: "the Mathematical Compendium prints no object for the bracket
system -- an expansion owed there and not written here."  The compendium prints it.  The object is
`The tower's two ends joined`, family K, and its headline carries every figure 1880 names: the
gap-free interval with both endpoints monotone across all 199,130 cells, the directed system
chi(L13) -> ... -> chi(L8), composition with slack <= 2 rank units, ranks 3 through 20 covered
without gap, the 1D chain as terminal object, the 14D direction as limit, and the strict map form
refuted with branching 4, 4, 6, 8, 9.  Its grade line reads "on the rebuilt tower and its bracket
system".

AND IT WAS PRINTED BEFORE 1880 WAS WRITTEN.  Traced through the archived compendia series, the
object's first appearance is roughly a hundred and ninety compendia builds before the build that
seated 1880, and it is present in every archived build from there to the last one held.

WHY NOTHING CAUGHT IT.  The audit that tested 1880's claim searched object HEADINGS in families B
and T for the words `stage-bracket|bracket system|rank value|fibre`.  The object is in family K, so
it was outside the search, and it is NAMED FOR ITS RESULT RATHER THAN ITS MECHANISM, so it matches
none of those words.  The test looked for the object by the name it would have had if it did not
exist -- a pattern narrower than the material, which is the third instance of that fault this leg.

NOTHING IS OWED IN THE VOLUMES, so this build moves no volume byte.  A REGISTER ENTRY IS NEVER
EDITED, so 1880 stands with its clause and register 1892 supersedes that clause alone: the rest of
1880 is its measurements, and those are the object's own.

Usage:  python3 r4-a8.py            dry run
        python3 r4-a8.py --write    writes BUILD130 main + BUILD306 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD129_main_and_register.md')
OLD_M_MD5 = '0f9473f09a8d412c2ad9539432390b6d'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD130_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD305_compendia_papers_audits.md')
OLD_C_MD5 = '411f9a5a33a924b5320b8571df209250'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD306_compendia_papers_audits.md')
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
WR = 'WORKING-REGISTER.md'
W_PATH = os.path.join(REPO, 'method', 'W-311.md')
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the five substitutions, count-asserted IN THEIR OWN MEMBER ---------------------------------------
MSUBS = {MAIN: []}
CSUBS = {}

ENTRY_N = 1892
ENTRY = """

### 1892

**THE EXPANSION REGISTER 1880 RECORDS AS OWED IS NOT OWED: THE MATHEMATICAL COMPENDIUM ALREADY PRINTS THE OBJECT, AND PRINTED IT BEFORE THAT ENTRY WAS WRITTEN.** *1880 closes* **"the Mathematical Compendium prints no object for the bracket system — an expansion owed there and not written here"**. *The object is* **The tower's two ends joined***, and it carries every figure 1880 names:* **at each consecutive stage the correspondence from a rank above to the ranks below is a gap-free interval with both endpoints monotone, with no exception across all 199,130 cells; the tower's chains form one directed system of monotone brackets from χ(Λ₁₃) down to χ(Λ₈), the five stage-brackets composing to contain the direct bracket with slack at most 2 rank units; the projection from Λ₁₃ covers every rank of χ(Λ₈), 3 through 20, without gap; the 1D chain is that system's terminal object and the fourteenth direction its limit; and the strict map form is refuted, branching 4, 4, 6, 8, 9 with height.** *Its grade line names the subject in those words — proved on the rebuilt tower and its bracket system — and the figures are 1880's own, because both were taken from the same measurement.* **Traced through the archived compendia, the object stands roughly a hundred and ninety builds before the one that seated 1880, and in every archived build from there to the last held.** *So the clause was not overtaken by later work; it was untrue when it was written.* **What made it survive is worth more than the clause.** *The reading that tested it looked in two families of objects for a heading carrying the words* **stage-bracket, bracket system, rank value** *or* **fibre***. This object sits in a third family and is* **named for its result rather than its mechanism***, so it answered to none of them: the test sought the object by the name it would have borne had it been absent. A search narrower than the material returns the absence it was shaped to find.* **1880 is not withdrawn and nothing in it is repaired.** *Its measurements are this object's, its refutation of register 334's map form stands, and only its closing clause is superseded here.* Registers 334; 1880. (a correction.)"""

# ---- the volumes as they stand -----------------------------------------------------------------------
oldc = {n: open(MEM + n, 'rb').read() for n in (MC, PC, WR)}
txtc = {n: oldc[n].decode('utf-8') for n in oldc}
newc = {}
for n, subs in CSUBS.items():
    t = txtc[n]
    for a, b in subs:
        assert t.count(a) == 1, '%s: anchor not unique in the member: %r %d' % (n, a[:40], t.count(a))
        assert b == '' or t.count(b) == 0, '%s: already repaired: %r' % (n, b[:40])
        t = t.replace(a, b)
    newc[n] = t
    print('%-46s %d substitution(s)' % (n, len(subs)))


wtext = open(W_PATH, encoding='utf-8').read()
assert wtext.startswith('### W-311 —') and wtext.endswith('\n\n'), 'W-311 form'
assert wtext not in txtc[WR], 'W-311 already appended'
newc[WR] = txtc[WR].rstrip('\n') + '\n\n' + wtext
print('%-46s W-306 appended (%d B)' % (WR, len(wtext)))

old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
new = dict(txt)
t = txt[MAIN]
for a, b in MSUBS[MAIN]:
    assert t.count(a) == 1, 'MAIN: anchor not unique: %r %d' % (a[:40], t.count(a))
    assert t.count(b) == 0, 'MAIN: already repaired: %r' % (b[:40])
    t = t.replace(a, b)
new[MAIN] = t
print('%-46s %d substitution(s)' % (MAIN, len(MSUBS[MAIN])))

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0 and r.count('### %d\n' % (ENTRY_N - 1)) == 1
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip())
new[REG] = r.rstrip('\n') + ENTRY + '\n'

# ---- the counts, from the seated tools on the members as they will stand -------------------------------
stage = tempfile.mkdtemp(prefix='r4-a6-')
allnew = dict(new); allnew.update(newc)
for f in os.listdir(MEM):
    if f.endswith('.md') and f not in allnew: os.symlink(MEM + f, os.path.join(stage, f))
for n in allnew: open(os.path.join(stage, n), 'w', encoding='utf-8').write(allnew[n])
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
    m_ = re.search(pat, t, re.M); assert m_, label + ': anchor absent'
    n = repl(m_); assert t.count(m_.group(0)) == 1, label + ': anchor not unique'
    print('%-40s %s' % (label, 'unchanged' if n == m_.group(0) else '%s -> %s' % (m_.group(0)[:52].replace('\n', ' '), n[:52].replace('\n', ' '))))
    return t.replace(m_.group(0), n)

for kind in ('a finding', 'a correction', 'a measurement', 'a new protocol', 'a withdrawal', 'prior art', 'an open question', 'a fault of mine'):
    rr = sub1(rr, r'^\| \*\*%s\*\* \| (\d[\d,]*) \| (\d+) \|' % re.escape(kind),
              lambda m_, kind=kind: '| **%s** | %s | %s |' % (kind, g(K[kind]), m_.group(2)), 'kinds row ' + kind)
rr = sub1(rr, r'by `kinds\.py` over the (\d[\d,]*) entry headings,', lambda m_: 'by `kinds.py` over the %s entry headings,' % g(K_N), 'kinds headings')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited by other entries\.\*\*', lambda m_: '**%d entries are cited by other entries.**' % CITED_BY, 'cited by entries')
rr = sub1(rr, r'the (\d+) cited seven times or more:', lambda m_: 'the %d cited seven times or more:' % len(TOP), 'the N cited')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited in the main volume\'s chapters and appendices; (\d[\d,]*) counting the four compendia and the two papers; (\d[\d,]*) counting citations by other entries\.\*\*',
          lambda m_: '**%d entries are cited in the main volume\'s chapters and appendices; %d counting the four compendia and the two papers; %s counting citations by other entries.**'
          % (CITED_MAIN, CITED_MC, g(CITED_ANY)), 'cited 3 figures')
rows = re.findall(r'^\| \*\*(\d+)\*\* \| (\d+)× \| (.*) \|$', rr, re.M)
what = {int(e): w for e, _, w in rows}
# This build adds no entry to the >= 7 table: register 1892 cites 334 and 1880, and neither crosses.
# A new row there is a hand act (r3-q6's rule) and none is written here, so the set must be unchanged.
assert sorted(what) == sorted(n for n, _ in TOP), \
    ('the >=7 set moved and no row is hand-written in this build; REFUSED', sorted(what), TOP)
i0 = rr.index('| entry | cited | what it established |\n|---|---|---|\n'); i1 = rr.index('\n\n', i0)
rr = rr[:i0] + '| entry | cited | what it established |\n|---|---|---|\n' + ''.join('| **%d** | %d× | %s |\n' % (n, k, what[n]) for n, k in TOP) + rr[i1 + 1:]
new[REG] = rr
mm = new[MAIN]
mm = sub1(mm, r'(\d[\d,]*) entries, 1 to (\d+), at this build \(\d{4}-\d\d-\d\d\)',
          lambda m_: '%s entries, 1 to %d, at this build (2026-09-08)' % (g(c['headings']), c['highest']), 'main: at this build')
mm = sub1(mm, r'436 entries when this paragraph was written, (\d[\d,]*) at this build',
          lambda m_: '436 entries when this paragraph was written, %s at this build' % g(c['headings']), 'main: N at this build')
mm = sub1(mm, r'at this build the main volume cites (\d+) entries',
          lambda m_: 'at this build the main volume cites %d entries' % CITED_MAIN, 'main: cites N')
new[MAIN] = mm
c2 = rc.count(new[REG]); p2 = rc.printed(new[REG])
assert (p2['front_total'], p2['front_highest'], p2['front_mature'], p2['front_mature_highest'], p2['back_mature_highest']) == (c2['headings'], c2['highest'], c2['mature'], c2['highest'], c2['highest']), (p2, c2)
assert c2['genesis'] + c2['superseded'] + c2['mature'] == c2['headings'] == p2['front_total']
print('the front matter sums to itself: %d + %d + %d = %d, highest %d' % (c2['genesis'], c2['superseded'], c2['mature'], c2['headings'], c2['highest']))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v in list(new) + list(newc):
    base = txt if v in txt else txtc
    tgt = new if v in new else newc
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], base[v].count(a), tgt[v].count(a)) for a in anchors if base[v].count(a) != tgt[v].count(a)]
    print('build.py SUBS anchors on %-46s %3d checked; moved: %s' % (v, len(anchors), moved)); assert not moved

# ---- the two bundles, each reverse-guarded --------------------------------------------------------------
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
def rebuild(path, want_md5, olds, news, label):
    ob = open(path, 'rb').read(); assert md5(ob) == want_md5, label + ' md5 mismatch'
    ms = {x.group(1).decode(): x.group(2) for x in MEMBER.finditer(ob)}
    nb = ob
    for n in news:
        assert ms[n] == olds[n], '%s in the bundle is not the extracted member' % n
        b0 = block(n, ms[n]); assert nb.count(b0) == 1
        nb = nb.replace(b0, block(n, news[n].encode('utf-8')))
    rv = nb
    for n in news:
        b1 = block(n, news[n].encode('utf-8')); assert rv.count(b1) == 1
        rv = rv.replace(b1, block(n, ms[n]))
    assert md5(rv) == want_md5, label + ' reverse FAILED'
    print('%s: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
          % (label, want_md5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))
    return nb

nb_m = rebuild(OLD_M, OLD_M_MD5, old, new, 'BUILD129 -> BUILD130 main')
nb_c = rebuild(OLD_C, OLD_C_MD5, oldc, newc, 'BUILD305 -> BUILD306 compendia')

if WRITE:
    for p_, b_ in ((NEW_M, nb_m), (NEW_C, nb_c)):
        assert not os.path.exists(p_), '%s already exists' % p_
        open(p_, 'wb').write(b_); print('written', p_)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
