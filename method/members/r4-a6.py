#!/usr/bin/env python3
"""r4-a6.py — one paper's second author, wrong at six sites in four volumes.
BUILD127 -> BUILD128 main and BUILD296 -> BUILD297 compendia, in one build.

THE FINDING.  The corpus cites *Constraint satisfaction over connected row-convex constraints*,
Artificial Intelligence 109(1-2) (1999) 243-271, under TWO different second authors.  Sixteen sites
give Barette; six give Barták, who is a different person -- Roman Barták, a real and prominent
constraint-programming researcher, which is why the substitution reads without a flinch and why it
survived every pass.

THE EVIDENCE IS HELD IN THIS REPOSITORY, AND WAS HELD BEFORE THE SIX SITES WERE WRITTEN.
`drive/chats/2026-08/764406b9-5552-45a2-9bf6-adb32378bf73.json` -- conversation "transitions", 777
messages, md5 3cf127ea816e288eab05a8f78f9960bd, captured 2026-08-02 -- carries THREE independently
captured reference lists, each from a different peer-reviewed publication, each citing this paper:

    Kong, Li, Li & Long, On tree-preserving constraints, Ann. Math. AI (2017), via Springer:
        "Deville, Y., Barette, O., Hentenryck, P.V.: Constraint satisfaction over connected row
         convex constraints. Artif. Intell. 109(1-2), 243-271 (1999)"
    Zhang & Freuder, Tractable Tree Convex Constraint Networks, AAAI-04:
        "Deville, Y.; Barette, O.; and Van Hentenryck, P."
    Exploring Directional Path-Consistency for Solving Constraint Networks, arXiv 1708.05522:
        "Deville, Y., Barette, O., van Hentenryck, P. ... Artificial Intelligence 109(1-2),
         243-271 (1999)"

Three independent typesettings -- Hentenryck, P.V. / Van Hentenryck, P. / van Hentenryck, P. --
agreeing on Barette, O. and on volume, issue, year and pages.  Searched over all 352 conversations,
NOT ONE captured source anywhere in this repository gives Barták for this paper: every Barták
occurrence in the export is the corpus's own prose.  Three captured sources to zero.

WHY NOTHING CAUGHT IT.  Every pass that touched these sites verified the INTERNAL TRIANGLE -- text,
References, Register -- and none checked the author list.  `recovered/READ-ch13g.md` records for this
citation only that it "is in the References and cited for the staircase class; Register 401 records
it", and W-117 summarised the segment as "consistent across text, References and Registers 224, 400,
401".  Two bullets earlier in that same file, Freuder 1982 was found credited with Dechter 1992's
theorem and corrected at register 400 -- the corpus corrected the wrong theorem attributed to the
right paper, and never checked the right theorem's author list.  BUILD12 already carries both
spellings, so nothing later introduced it.

TWO BUNDLES IN ONE BUILD, because the rule that governs it is one: a volume may not change unless a
Register entry in the same build records it.  Five sites are volume members across both bundles;
entry 1890 and the count classes are main members.  Each bundle is reverse-guarded to its own
predecessor's md5.

THE REGISTER'S OWN SITE IS NOT EDITED.  Register 401 prints the wrong spelling in its headline.  A
Register entry is never edited -- the repair is a new appended entry citing the superseded one --
so 401 stands and 1890 supersedes it.  Both states are preserved, which is the point.

Usage:  python3 r4-a6.py            dry run (asserts everything, writes nothing)
        python3 r4-a6.py --write    writes BUILD128 main + BUILD297 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD127_main_and_register.md')
OLD_M_MD5 = 'dad1af971146d2979314fe622e1f7c9f'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD128_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD296_compendia_papers_audits.md')
OLD_C_MD5 = 'cd849e40fdd37acb8828c38b1fa356b7'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD297_compendia_papers_audits.md')
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
WR = 'WORKING-REGISTER.md'
W_PATH = os.path.join(REPO, 'method', 'W-302.md')
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the five substitutions, count-asserted IN THEIR OWN MEMBER ---------------------------------------
MSUBS = {
    MAIN: [("Deville, Barták and Van Hentenryck,",
            "Deville, Barette and Van Hentenryck,"),
           ("Deville, Y., Barták, R. and Van Hentenryck, P. (1999)",
            "Deville, Y., Barette, O. and Van Hentenryck, P. (1999)")],
}
CSUBS = {
    MC: [("Cited — Deville, Barták, Van Hentenryck 1999.",
          "Cited — Deville, Barette, Van Hentenryck 1999."),
         ("Deville, Barták & Van Hentenryck (1999) — the staircase constraint class",
          "Deville, Barette & Van Hentenryck (1999) — the staircase constraint class")],
    PC: [("**Deville, Barták & Van Hentenryck (1999)**",
          "**Deville, Barette & Van Hentenryck (1999)**")],
}

ENTRY_N = 1890
ENTRY = """

### 1890

**ONE PAPER'S SECOND AUTHOR WAS WRONG AT SIX SITES IN FOUR VOLUMES, AND THE EVIDENCE HAD BEEN HELD IN THE CORPUS SINCE BEFORE FIVE OF THEM WERE WRITTEN.** *Constraint satisfaction over connected row-convex constraints,* **Artificial Intelligence 109(1-2) (1999) 243-271***, is cited under two different second authors: sixteen sites give* **Barette** *and six give* **Barták** *— Roman Barták, a real and prominent constraint-programming researcher, which is why it read without a flinch. The two full bibliographic records are identical in title, journal, volume, year and pages, so there is no second work and one of the two names is simply wrong.* **Three independently captured reference lists, held in the chat export and dated 2026-08-02, settle it: Springer's *On tree-preserving constraints* (Ann. Math. AI 2017), Zhang & Freuder's *Tractable Tree Convex Constraint Networks* (AAAI-04) and arXiv 1708.05522, in three different typesettings — Hentenryck, P.V. / Van Hentenryck, P. / van Hentenryck, P. — every one giving Barette, O. and the same volume, issue and pages.** *Searched across all 352 conversations, not one captured source anywhere in this repository gives Barták for this paper; every occurrence of it in the export is this work's own prose. Three sources to zero.* **Why nothing caught it is the part worth keeping: every pass that touched these sites verified the internal triangle — text, References, Register — and none checked the author list.** *`READ-ch13g` records only that the citation "is in the References and cited for the staircase class; Register 401 records it", and W-117 summarised the segment as "consistent across text, References and Registers 224, 400, 401". Two bullets earlier in that same reading, Freuder 1982 was found credited with Dechter 1992's theorem and corrected at register 400 — the corpus corrected the wrong theorem attributed to the right paper, and never checked the right theorem's authors. Consistency was verified; the name was not.* **Five sites are repaired here — the main volume's §14.1 prose and its References entry, the Mathematical Compendium's *Staircase / connected row-convex* object and the generation criterion's prior art, and the Physics Compendium's prior-art chain — and the References entry takes the initial the sources give, Barette, O.** *The sixth is register 401's own headline, and it is not repaired: a Register entry is never edited, so 401 stands with the wrong spelling and this entry supersedes it. Both states are preserved, which is what append-only is for.* **The class this belongs to is register 1736's, one step further out.** *That entry removed ten bibliography rows the generator had read out of callout text and expanded "BFMY 1983" to its full author list, by matching the compendium's works against the main volume's References by author and year. A match by author cannot see a wrong year on a real author, and it cannot see a wrong author on a real paper. Six bibliography rows of the first kind are recorded and unrepaired, and this is the first of the second kind.* Registers 400; 401; 1736. (a correction.)"""

# ---- the volumes as they stand -----------------------------------------------------------------------
oldc = {n: open(MEM + n, 'rb').read() for n in (MC, PC, WR)}
txtc = {n: oldc[n].decode('utf-8') for n in oldc}
newc = {}
for n, subs in CSUBS.items():
    t = txtc[n]
    for a, b in subs:
        assert t.count(a) == 1, '%s: anchor not unique in the member: %r %d' % (n, a[:40], t.count(a))
        assert t.count(b) == 0, '%s: already repaired: %r' % (n, b[:40])
        t = t.replace(a, b)
    assert 'Barták' not in t, '%s: a Barták site remains' % n
    newc[n] = t
    print('%-46s %d substitution(s); Barette now %d, Barták %d'
          % (n, len(subs), t.count('Barette'), t.count('Barták')))

wtext = open(W_PATH, encoding='utf-8').read()
assert wtext.startswith('### W-302 —') and wtext.endswith('\n\n'), 'W-302 form'
assert wtext not in txtc[WR], 'W-302 already appended'
newc[WR] = txtc[WR].rstrip('\n') + '\n\n' + wtext
print('%-46s W-302 appended (%d B)' % (WR, len(wtext)))

old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
new = dict(txt)
t = txt[MAIN]
for a, b in MSUBS[MAIN]:
    assert t.count(a) == 1, 'MAIN: anchor not unique: %r %d' % (a[:40], t.count(a))
    assert t.count(b) == 0, 'MAIN: already repaired: %r' % (b[:40])
    t = t.replace(a, b)
assert 'Barták' not in t, 'MAIN: a Barták site remains'
new[MAIN] = t
print('%-46s %d substitution(s); Barette now %d, Barták %d'
      % (MAIN, len(MSUBS[MAIN]), t.count('Barette'), t.count('Barták')))

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0 and r.count('### %d\n' % (ENTRY_N - 1)) == 1
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip())
assert r.count('DEVILLE, Barták AND VAN HENTENRYCK 1999') == 1, 'register 401 is not where it was'
new[REG] = r.rstrip('\n') + ENTRY + '\n'
assert new[REG].count('DEVILLE, Barták AND VAN HENTENRYCK 1999') == 1, '401 must be left exactly as it stands'

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
assert sorted(what) == sorted(n for n, _ in TOP), \
    ('the >=7 set moved; a new row is a hand act and none is written here; REFUSED', sorted(what), TOP)
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

nb_m = rebuild(OLD_M, OLD_M_MD5, old, new, 'BUILD127 -> BUILD128 main')
nb_c = rebuild(OLD_C, OLD_C_MD5, oldc, newc, 'BUILD296 -> BUILD297 compendia')

if WRITE:
    for p_, b_ in ((NEW_M, nb_m), (NEW_C, nb_c)):
        assert not os.path.exists(p_), '%s already exists' % p_
        open(p_, 'wb').write(b_); print('written', p_)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
