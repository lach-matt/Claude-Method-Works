#!/usr/bin/env python3
"""r4-a7.py — the six bibliography rows the generator made, removed on register 1736's precedent.
BUILD128 -> BUILD129 main and BUILD300 -> BUILD301 compendia, in one build.

THE FINDING, PROVED FROM HELD MATERIAL.  The Mathematical Compendium's bibliography is generated.
`extracted/archives/restore-point-2-13/compendium.py` is that generator and `mathreg.py` beside it is
the register data it reads; run its own regex, verbatim, over that data and it reproduces all seven
rows below WITH EXACTLY THE HANDLES THE VOLUME PRINTS.  The matched spans show the mechanism:

    1913 Pauli    L.def    'Pauli 1925 PRIOR ART: ... the shell-structure rules of Bohr (1913)'
    1937 Shannon  L.bits   'Shannon 1938 PRIOR ART: Birkhoff (1937)'
    1982 Racah    T.trad   'Racah 1942 PRIOR ART: ... is Freuder (1982)'
    1958 Pauli    Q.delta  'Pauli bound (Pauli 1925), ... and Seaton polarisation (1958)'
    1964 Moebius  G.book   'Moebius inversion over a refinement lattice is Rota (1964)'
    1999 Deville / 1999 Hentenryck   one work, written in full under one handle set and as the bare
                                     'Hentenryck 1999' under another

The pattern allows NINETY characters of anything but a period or a semicolon between a name and a
parenthesised year, and the `src` and `check` fields are CONCATENATED before it runs -- so `src`'s
last name pairs with `check`'s first year.  Four rows cross that field boundary; one takes a title
word for an author; two are one work written two ways.

WHY THE MECHANISM DOES NOT JUSTIFY THEM.  The section's own opening is "Every object of this
compendium names a work", and a (name, year) pair no object attributes is not a work an object names.
REGISTER 1736 ALREADY RULED THIS GENERATOR'S OTHER OUTPUT: it removed ten rows "no reader could
cite", expanded BFMY 1983 to its full author list, restated the count and kept the prior one beside
it.  Those ten are the case where the NAME is wrong; these six are the case where the name is a real
author and the YEAR belongs to someone else -- which is why a match by author could not see them, as
register 1890 records.

NO REMOVAL ORPHANS A HANDLE, and this is asserted before a byte moves: every handle on a removed row
survives on the row that earned it -- L.def on Bohr 1913 and Pauli 1925, L.bits on BIRKHOFF 1937
(the very year the generator took), Q.delta on Pauli 1925 / Fermi 1928 / Seaton 1958, T.trad on
Freuder 1982, G.book on Rota 1964.

THE COUNT IS 156, NOT 157.  There are FIVE spurious rows and one merge, so 162 - 5 - 1 = 156.  The
figure 157 given when the ruling was put was an arithmetic slip on my part and is corrected here.

TWO BUNDLES IN ONE BUILD: the rows and the count sentence are compendia members, the main volume's
own statement of the same figures and register 1891 are main members.

Usage:  python3 r4-a7.py            dry run
        python3 r4-a7.py --write    writes BUILD129 main + BUILD301 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD128_main_and_register.md')
OLD_M_MD5 = 'a17ab9dbc9971a63f6cc1466ff96db30'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD129_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD300_compendia_papers_audits.md')
OLD_C_MD5 = 'dad1a278ba0d116c4eb2b367f3e3d8dc'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD301_compendia_papers_audits.md')
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
WR = 'WORKING-REGISTER.md'
W_PATH = os.path.join(REPO, 'method', 'W-306.md')
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the five substitutions, count-asserted IN THEIR OWN MEMBER ---------------------------------------
MSUBS = {
    MAIN: [(" objects — 162 works, 1669 to 2026, ordered by year with the objects each carries. Fifty-two of them\n"
            " are the works listed above (fifty-nine of the 172 rows matched at register 1736, before ten rows were\n"
            " removed; register 1809);",
            " objects — 156 works, 1669 to 2026, ordered by year with the objects each carries. Fifty-one of them\n"
            " are the works listed above (fifty-two of the 162 rows before five were removed and two merged at\n"
            " register 1891; fifty-nine of the 172 rows matched at register 1736, before ten rows were removed;\n"
            " register 1809);")],
}
CSUBS = {
    MC: [("| 1913 | Pauli | `L.def` |\n", ""),
         ("| 1937 | Shannon | `L.bits` |\n", ""),
         ("| 1958 | Pauli | `Q.delta` |\n", ""),
         ("| 1964 | Moebius | `G.book` |\n", ""),
         ("| 1982 | Racah | `T.trad` |\n", ""),
         ("| 1999 | Deville | `A.env` `A.orient` `A.r4` `T.tight` |\n"
          "| 1999 | Hentenryck | `A.orient` `A.rule` `A.stair` `A.staircls` `T.tight` |\n",
          "| 1999 | Deville, Barette & Van Hentenryck | `A.env` `A.orient` `A.r4` `A.rule` `A.stair` `A.staircls` `T.tight` |\n"),
         ("**162 works, 1669\u20132026.** *Ten rows the generator had read out of callout text \u2014 status words, a possessive, a method name \u2014 were removed on 2026-08-24 (register 1736); the count was 172.*",
          "**156 works, 1669\u20132026.** *Ten rows the generator had read out of callout text \u2014 status words, a possessive, a method name \u2014 were removed on 2026-08-24 (register 1736); the count was 172. Five more, each a real author carried to a neighbouring citation\u2019s year, and one work printed as two rows, were removed on 2026-09-08 (register 1891); the count was 162.*")],
}

# every handle on a removed row must survive on another row: asserted, not assumed
REMOVED_HANDLES = {"L.def": ("1913 Bohr", "1925 Pauli"), "L.bits": ("1937 Birkhoff",),
                   "Q.delta": ("1925 Pauli", "1928 Fermi", "1958 Seaton"),
                   "G.book": ("1964 Rota",), "T.trad": ("1982 Freuder",)}

ENTRY_N = 1891
ENTRY = """

### 1891

**SIX ROWS OF THE MATHEMATICAL COMPENDIUM'S BIBLIOGRAPHY NAME NO WORK ANY OBJECT ATTRIBUTES, AND THE GENERATOR THAT MADE THEM CAN BE RUN TO SHOW WHY.** *The section opens* **"Every object of this compendium names a work"***, and its rows are produced from the objects' own source and check fields. Run that production over those fields and it reproduces each of the six with the very handles the volume prints:* **1913 Pauli from "Pauli 1925 … the shell-structure rules of Bohr (1913)"; 1937 Shannon from "Shannon 1938 … Birkhoff (1937)"; 1982 Racah from "Racah 1942 … is Freuder (1982)"; 1958 Pauli from "the Pauli bound (Pauli 1925) … and Seaton polarisation (1958)"; 1964 Moebius from "Moebius inversion over a refinement lattice is Rota (1964)", where the name is a word in the sentence and not an author.** *The rule that makes them is that up to ninety characters of anything but a period or a semicolon may stand between a name and a parenthesised year, and that the two fields are read as one — so the last name of the first pairs with the first year of the second. Four of the six cross that join.* **The seventh and sixth row is one work printed twice**: *the connected row-convex paper is written in full in some objects and as a bare surname and year in others, so it entered as two rows. It is merged, under the standing rule that a work takes its full author list.* **No removal loses a pointer, and that was established before any row moved: every handle on a removed row is carried by the row that earned it** — *`L.def` by Bohr 1913 and Pauli 1925, `L.bits` by Birkhoff 1937, which is the very year the sixth row took, `Q.delta` by Pauli 1925, Fermi 1928 and Seaton 1958, `T.trad` by Freuder 1982, `G.book` by Rota 1964.* **The count is restated at 156 with both prior counts kept beside it, 162 and 172**, *and the main volume's own statement of the same figures moves with it: 162 works becomes 156, and the fifty-two shared with the References becomes fifty-one, because the two merged rows were both matches. Neither of the five removed rows was.* **This is register 1736's repair, applied to what its method could not see.** *That entry removed ten rows by matching this book's works against the References by author and year — a match that cannot see a wrong year on a real author, which register 1890 records — and it set the form followed here: the rows go, the count is restated, the prior count stays beside it.* Registers 1736; 1809; 1890. (a correction.)"""

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


# ---- no removal may orphan a handle -------------------------------------------------------------------
_bib = _re_rows = None
import re as _re2
_rows = [(_m.group(1), _m.group(2), _re2.findall(r"`([^`]+)`", _m.group(3)))
         for _m in _re2.finditer(r"^\| (1[6-9]\d\d|20[0-2]\d) \| (.+?) \| (.*) \|$", txtc[MC], _re2.M)]
assert len(_rows) == 162, 'bibliography rows: %d' % len(_rows)
_own = {}
for _y, _w, _hs in _rows:
    for _h in _hs: _own.setdefault(_h, set()).add('%s %s' % (_y, _w))
for _h, _survivors in REMOVED_HANDLES.items():
    _others = _own[_h] - {r'%s %s' % (_y, _w) for _y, _w, _hs in _rows if _h in _hs and
                          ('%s %s' % (_y, _w)) not in _survivors}
    assert set(_survivors) <= _own[_h], ('handle %s: stated survivors absent' % _h, sorted(_own[_h]))
    print('   handle %-9s survives on %s' % (_h, ', '.join(sorted(_survivors))))
print('no removal orphans a handle: True')

wtext = open(W_PATH, encoding='utf-8').read()
assert wtext.startswith('### W-306 —') and wtext.endswith('\n\n'), 'W-306 form'
assert wtext not in txtc[WR], 'W-306 already appended'
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
# Register 1736 crosses to seven citations at this build, because entry 1891 cites it. A new row in the
# front matter's table is a hand act (r3-q6's rule) and is written here, in the sentence case the older
# rows use, from 1736's OWN headline.
NEW_ROWS = {1736: "The Mathematical Compendium's bibliography carried ten rows that were not works"}
norm = lambda s: re.sub(r'\W', '', s).casefold()
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

nb_m = rebuild(OLD_M, OLD_M_MD5, old, new, 'BUILD128 -> BUILD129 main')
nb_c = rebuild(OLD_C, OLD_C_MD5, oldc, newc, 'BUILD300 -> BUILD301 compendia')

if WRITE:
    for p_, b_ in ((NEW_M, nb_m), (NEW_C, nb_c)):
        assert not os.path.exists(p_), '%s already exists' % p_
        open(p_, 'wb').write(b_); print('written', p_)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
