#!/usr/bin/env python3
"""r4-a3.py — R4 Batch A item 3: the four sites outside §35 that ruling 12's own rule reaches.
BUILD112 -> BUILD113 main and BUILD235 -> BUILD236 compendia, in one build.

Ruling 12 (M, 6 September 2026) states the rule and not only the site: "where two true statements
differ only in reach, the volume takes the more expanded one." W-241's census found the four sites
without being asked — C6-NUMBERS-NOT-IN-SOURCE at Mathematical Compendium L3178, whose entry cites
§35 and register 1704 and still printed the old bound. M, on the question being put: "this is
obviously yes, and did not require a ruling from me."

TWO BUNDLES IN ONE BUILD, because the rule that governs it is one: a volume may not change unless a
Register entry in the same build records it. The four repairs are compendia members; entry 1838 and
the count classes are main members. Each bundle is reverse-guarded to its own predecessor's md5.

SCOPE. Four substitutions, each asserted unique IN ITS OWN MEMBER — never in the bundle, because
WORKING-REGISTER.md's W-241 quotes one of these sentences verbatim as the record of what stood
before, and the audit log is not a volume and is never edited.

Usage:  python3 r4-a3.py            dry run (asserts everything, writes nothing)
        python3 r4-a3.py --write    writes BUILD113 main + BUILD236 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD112_main_and_register.md')
OLD_M_MD5 = 'b4ba96c2693fda0fd97f08e79e6b4ad6'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD113_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD235_compendia_papers_audits.md')
OLD_C_MD5 = 'd59d82da23ccde3ec427560bd65d7048'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD236_compendia_papers_audits.md')
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
LW = 'THE-LOWDIN-SOLUTION-2.md'; MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the four substitutions, count-asserted IN THEIR OWN MEMBER --------------------------------------
CSUBS = {
    LW: [("no g block exists anywhere below Z = 121", "no g block exists anywhere through Z = 125"),
         ("there is no g block anywhere below Z = 121", "there is no g block anywhere through Z = 125"),
         ("The absence of a g block below Z = 121", "The absence of a g block through Z = 125")],
    MC: [("the nonexistence of a g period below Z = 121", "the nonexistence of a g period through Z = 125")],
}

ENTRY_N = 1838
ENTRY = """

### 1838

**THE BOUND WAS WIDENED IN §35 AND THE COMPANION AND THE COMPENDIUM STILL PRINTED THE OLD ONE; THE CENSUS FOUND THAT BEFORE ANYONE ASKED.** *Register 1837 widened §35's g-block absence from* **below Z = 121** *to* **through Z = 125** *and recorded that four sites outside §35 still carried the old figure, left standing as a question. The census regenerated at that build answered it without being asked:* **C6-NUMBERS-NOT-IN-SOURCE, Mathematical Compendium L3178, "The pinned-channel theorem (no g block)", 1 of 3: 121, sources §35 R1704** *— the entry names §35 and register 1704 as its sources and printed a figure neither of them any longer carried. A compendium entry whose figure is not in the source it cites is a defect of exactly the class the census exists to find, and it was created by repairing §35 alone.* **The four are repaired here to the same bound: the Löwdin companion at its abstract, at its statement of the derived absences, and at §V.3's own sentence, and the Mathematical Compendium's pinned-channel theorem.** *Each substitution was asserted unique in its own member rather than in the bundle, because WORKING-REGISTER.md quotes one of these sentences verbatim as the record of what stood before — the audit log is not a volume and is never edited. Both bundles are reverse-guarded to their own predecessors' md5s in the one build, because the rule that requires this entry is that a volume may not change unless a Register entry in the same build records it, and the sites and the entry are in different bundles.* **The governing rule is ruling 12's own, and it is why no further ruling was needed: where two true statements differ only in reach, the volume takes the more expanded one.** *M, on the question being put back: "this is obviously yes, and did not require a ruling from me."* **One consequence is recorded and not repaired: register 1704 crosses to seven citations at this build, because 1837 and 1838 both cite it, so the front matter's table of entries cited seven times or more gains a row — and that row carries 1704's own headline, which states the superseded bound. That is the append-only Register working as designed: both states preserved, the correcting entries cited from the corrected one.** Registers 1704; 1837. (a correction.)"""

# ---- the volumes as they stand -----------------------------------------------------------------------
oldc = {n: open(MEM + n, 'rb').read() for n in (LW, MC)}
txtc = {n: oldc[n].decode('utf-8') for n in oldc}
newc = {}
for n, subs in CSUBS.items():
    t = txtc[n]
    for a, b in subs:
        assert t.count(a) == 1, '%s: anchor not unique in the member: %r %d' % (n, a[:40], t.count(a))
        assert t.count(b) == 0, '%s: already repaired: %r' % (n, b[:40])
        t = t.replace(a, b)
    newc[n] = t
    print('%-46s %d substitution(s); "below Z = 121" left in this member: %d'
          % (n, len(subs), t.count('below Z = 121')))
assert newc[LW].count('through Z = 125') == 3 and newc[MC].count('through Z = 125') == 1

old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
new = dict(txt)
r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0 and r.count('### %d\n' % (ENTRY_N - 1)) == 1
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip())
new[REG] = r.rstrip('\n') + ENTRY + '\n'

# ---- the counts, from the seated tools on the members as they will stand -------------------------------
stage = tempfile.mkdtemp(prefix='r4-a3-')
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
# Register 1704 crosses to seven citations at this build, because 1837 and 1838 both cite it. A new row
# in the front matter's table is a hand act (r3-q6's rule) and is written here, in the sentence case the
# older rows use, from 1704's OWN headline — which still states the superseded bound, because the Register
# is append-only and preserves both states with the correcting entries cited from it.
NEW_ROWS = {1704: 'No g block below Z = 121, and the field says so without being asked'}
norm = lambda t: re.sub(r'\W', '', t).casefold()
def headline(e):
    body = new[REG].split('\n### %d\n' % e, 1)[1]
    return re.match(r'\s*\*\*(.+?)\*\*', body, re.S).group(1).strip()
for e, w in NEW_ROWS.items():
    assert norm(headline(e)).startswith(norm(w)), (e, headline(e))
assert sorted(set(what) | set(NEW_ROWS)) == sorted(n for n, _ in TOP) and not (set(what) & set(NEW_ROWS)), \
    ('the >=7 set changed beyond the hand-written row; REFUSED', sorted(what), TOP)
what.update(NEW_ROWS); print('table: +%d row(s) %s' % (len(NEW_ROWS), sorted(NEW_ROWS)))
i0 = rr.index('| entry | cited | what it established |\n|---|---|---|\n'); i1 = rr.index('\n\n', i0)
rr = rr[:i0] + '| entry | cited | what it established |\n|---|---|---|\n' + ''.join('| **%d** | %d× | %s |\n' % (n, k, what[n]) for n, k in TOP) + rr[i1 + 1:]
new[REG] = rr
mm = new[MAIN]
mm = sub1(mm, r'(\d[\d,]*) entries, 1 to (\d+), at this build \(\d{4}-\d\d-\d\d\)',
          lambda m_: '%s entries, 1 to %d, at this build (2026-09-06)' % (g(c['headings']), c['highest']), 'main: at this build')
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

nb_m = rebuild(OLD_M, OLD_M_MD5, old, new, 'BUILD112 -> BUILD113 main')
nb_c = rebuild(OLD_C, OLD_C_MD5, oldc, newc, 'BUILD235 -> BUILD236 compendia')

if WRITE:
    for p_, b_ in ((NEW_M, nb_m), (NEW_C, nb_c)):
        assert not os.path.exists(p_), '%s already exists' % p_
        open(p_, 'wb').write(b_); print('written', p_)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
