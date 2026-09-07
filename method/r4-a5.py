#!/usr/bin/env python3
"""r4-a5.py — R3 completion, item A6 of `docs/R3-REPAIR-PLAN.md`, and the entry item A8 owes.
BUILD114 -> BUILD115 main and BUILD240 -> BUILD241 compendia, in one build.

A6. Two sites print "not a lattice" where the evidence offered is componentwise: main §12.11.2's
"The exact coupling region is not a lattice in any presentation tried" with its five failure counts,
and the three-body paper's Law 3 table row, which imports the clause by citation. A componentwise
meet failure refutes SUBLATTICE-hood of the product; it does not refute lattice-hood, which asks
whether a pair has a greatest lower bound INSIDE the set. FINDING-R4-02 measured the difference on
the chapter's own triangle region -- thousands of broken componentwise meets, every one of them with
a glb inside the region -- and FINDING-R4-25 reproduced six of six of that region's printed figures.
The repair needs no reconstruction of the five presentations: whatever they are, their counts are
counts of componentwise failures, and that is a sublattice statement.

A8. Register 314's general claim survives and only its supporting evidence falls. The main volume's
table says Lambda-10 does not compose "no source seniority exists" and that Lambda-9 "sits alone";
the Mathematical Compendium measures composability peaking AT Lambda-10, 0.8087, and
method/proofs/composab.py reproduces that fraction using the same source and target shapes that make
Lambda-9 work, along with three more of the compendium's six. Two predicates wear one word. The
volume sites are left to the prose pass on register 1790's own precedent for exactly this shape;
this build records the measurement.

TWO BUNDLES IN ONE BUILD, because a volume may not change unless a Register entry in the same build
records it, and the three-body paper is a compendia member while the Register is a main member.
Each substitution is asserted unique IN ITS OWN MEMBER.

Usage:  python3 r4-a5.py            dry run (asserts everything, writes nothing)
        python3 r4-a5.py --write    writes BUILD115 main + BUILD241 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD114_main_and_register.md')
OLD_M_MD5 = '51656eeafd454d307dcced5b332eca5d'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD115_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD240_compendia_papers_audits.md')
OLD_C_MD5 = 'd629b420250ce86a306b38bdfbd56a80'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD241_compendia_papers_audits.md')
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
TB = 'The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the four substitutions, count-asserted IN THEIR OWN MEMBER --------------------------------------
CSUBS = {
    TB: [("the exact three-body region is not a lattice",
          "the exact three-body region is not a sublattice of the product"),
         ("the exact region is not a lattice",
          "the exact region is not a sublattice of the product")],
}
MSUBS = [("The exact coupling region is not a lattice in any",
          "The exact coupling region is not a sublattice of the product in any")]

ENTRY_NS = (1840, 1841)
ENTRIES = """

### 1840

**"NOT A LATTICE" IS THE WRONG PHRASE FOR A COMPONENTWISE MEET FAILURE, AND THE CHAPTER PROVES IT ON ITS OWN NEXT PARAGRAPH.** *§12.11.2 prints* **"The exact coupling region is not a lattice in any presentation tried: as 2S′ (50,592 failures), as parity alone (52,080), as the min-cap (17,856), as pair count (7,254), as (2S,2L,2J) (2,443 meets)"** *, and the three-body paper's Law 3 table imports the clause by citation, unhedged. Every one of those counts is a count of COMPONENTWISE failures — the componentwise minimum of two members falling outside the set. That refutes SUBLATTICE-hood of the product. It does not refute lattice-hood, which asks whether a pair has a greatest lower bound INSIDE the set, and the second is strictly stronger than the first.* **The chapter's own next paragraph is the demonstration: the region {|2L−2S| ≤ 2J ≤ 2L+2S} is meet-broken by 2,862, 12,489, 40,887 and 110,229 componentwise meets at caps 6, 8, 10 and 12 — all four reproduced exactly at this build, with the join closure exact at every cap, the 1,848 parity-variant failures, and the sentence about the first failing meet manufacturing J = ½ from S = L = 0 returned as (0,1,1) ∧ (1,0,1) = (0,0,1), six of six — and every one of those thousands of broken meets has a greatest lower bound inside the region. The region IS a lattice. Appendix A, which calls the same object "join-closed and meet-broken" and "a sublattice", was right all along and needs nothing.** *So the repair needs no reconstruction of the five presentations, and that is why it can be made: whatever those five are, their counts are counts of componentwise failures, and the narrower word is the one the evidence supports. Both sites now read* **"is not a sublattice of the product"** *, the hedge "in any presentation tried" is kept where the volume had it, and the counts are untouched. The five presentation counts remain unreproduced — no instrument in this repository prints any of them and the five presentations are named in the prose and defined nowhere — and that is recorded, not repaired; 31 divides four of the five, which is a lead and nothing is built on it.* **Measured at this build by a standard-library instrument seated with this entry; Appendix A's regions were measured for a greatest lower bound at every pair whose componentwise minimum falls outside them, and the region's own printed 12,654 at cap 8 reproduces exactly, which is how the right object was identified.** Registers 402. (a correction.)

### 1841

**COMPOSABILITY IS TWO PREDICATES WEARING ONE WORD, AND THE COMPENDIUM MEASURES AT ITS PEAK THE STAGE THE MAIN VOLUME SAYS DOES NOT COMPOSE.** *§12.11's table gives Λ₁₀ as* **"no — no source seniority exists"** *and its prose concludes* **"Λ₉ is the only stage of the tower that composes"** *and* **"Λ₉ sits alone at the top of the stricter grading"**. *The Mathematical Compendium prints, of the same tower,* **"composability peaks at Λ₁₀ and falls after: 0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381 across Λ₈ to Λ₁₃"**. *Both cannot describe one predicate: the first says Λ₁₀ does not compose at all, the second measures it at its maximum.* **Measured at this build on the seated tower, with the source and target coordinate pairings determined by which ones reproduce the compendium's printed fractions rather than assumed: Λ₈ 0.0000 with 0 of 976 — its target is three coordinates against a source of four; Λ₉ 0.7068 with 1,169 of 1,654; Λ₁₀ 0.8087 with 2,050 of 2,535, USING THE SAME SOURCE (n,ℓ,k,2S) AND TARGET (e,f,g,2S′) SHAPES THAT MAKE Λ₉ WORK; and Λ₁₂ 0.6592 with 46,740 of 70,905 on the shapes one axis wider. Four of the compendium's six reproduce exactly. Λ₁₁ and Λ₁₃ reproduce under no pairing an exhaustive same-size sweep tried, and that is reported rather than smoothed.** *So the table's whole-stage predicate — does the target coordinate SET match a source set — and the compendium's cell-fraction predicate — is THIS cell's target a legal source — are different questions, and Λ₁₀ is barred only under the first.* **Register 314's claim is untouched by all of this: "an axis can be exact and not composable; none is composable and not exact" does not depend on which stages compose. What falls is the supporting evidence, and only that.** *The volume's table and the sentences around it are left to the prose pass, on register 1790's own precedent for a figure whose text and whose measurement had parted company; this entry records the measurement that pass needs. Nothing is repaired in a volume by this entry.* Registers 313; 314; 1790. (a finding.)"""

# ---- the volumes as they stand -----------------------------------------------------------------------
oldc = {n: open(MEM + n, 'rb').read() for n in CSUBS}
txtc = {n: oldc[n].decode('utf-8') for n in oldc}
newc = {}
for n, subs in CSUBS.items():
    t = txtc[n]
    for a, b in subs:
        assert t.count(a) == 1, '%s: anchor not unique in the member: %r %d' % (n, a[:40], t.count(a))
        assert t.count(b) == 0, '%s: already repaired: %r' % (n, b[:40])
        t = t.replace(a, b)
    newc[n] = t
    print('%-46s %d substitution(s); "is not a lattice" left in this member: %d'
          % (n, len(subs), t.count('is not a lattice')))
assert newc[TB].count('is not a sublattice of the product') == 2 and newc[TB].count('is not a lattice') == 0

old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
new = dict(txt)
r = txt[REG]
for _n in ENTRY_NS:
    assert r.count('### %d\n' % _n) == 0, 'entry %d already seated' % _n
assert r.count('### %d\n' % (ENTRY_NS[0] - 1)) == 1, 'entry %d is not seated' % (ENTRY_NS[0] - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip())
new[REG] = r.rstrip('\n') + ENTRIES + '\n'
m0 = txt[MAIN]
for a, b in MSUBS:
    assert m0.count(a) == 1, 'main anchor not unique: %r %d' % (a[:40], m0.count(a))
    assert m0.count(b) == 0, 'main already repaired'
    m0 = m0.replace(a, b)
new[MAIN] = m0
print('%-46s %d substitution(s); "is not a lattice" left: %d' % (MAIN, len(MSUBS), new[MAIN].count('is not a lattice')))

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
print('register_cites with %s: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %d entries'
      % (str(ENTRY_NS), CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, len(TOP)))
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
NEW_ROWS = {}   # no entry crosses seven citations at this build
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
          lambda m_: '%s entries, 1 to %d, at this build (2026-09-07)' % (g(c['headings']), c['highest']), 'main: at this build')
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

nb_m = rebuild(OLD_M, OLD_M_MD5, old, new, 'BUILD114 -> BUILD115 main')
nb_c = rebuild(OLD_C, OLD_C_MD5, oldc, newc, 'BUILD240 -> BUILD241 compendia')

if WRITE:
    for p_, b_ in ((NEW_M, nb_m), (NEW_C, nb_c)):
        assert not os.path.exists(p_), '%s already exists' % p_
        open(p_, 'wb').write(b_); print('written', p_)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
