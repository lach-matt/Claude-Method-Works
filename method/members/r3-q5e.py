#!/usr/bin/env python3
"""r3-q5e.py — R3: Q5 pass 5. The chat-58 batch 2c slips B2-C3 and B3-C1 seated as registers 1831 and 1832. B2-C3's figures
are re-derived first by r3-q5e-measure.py (a standard-library re-derivation of chat 58's numpy instruments mc11.py and
mc11b.py, M's ruling for passes 4 and 5), seated beside it with its golden; B3-C1's by chat 58's own mc12.py, which is
standard-library and is seated as it is with lam8.py, the Λ₈ builder it imports. BUILD108 -> BUILD109 main.

No volume site is edited: §10.4 and §11.1.1 stand as they are; the objects the slips corrected by handle (L.box, L.bits,
L.circuit) are no longer printed by the live Mathematical Compendium. The deferred main-volume item MV-DEF-01 goes to
DOCKET.md at the close, not through this instrument. The count classes of entries 1815 and 1816 are re-taken in the same build.

Usage:  python3 r3-q5e.py            dry run (runs both measurements, builds nothing)
        python3 r3-q5e.py --write    writes staging members + BUILD109 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib, importlib.util, time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD108_main_and_register.md'); OLD_M_MD5 = '79e6c273cfc8e708562af664e1dc3dd1'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD109_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build109') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the measurements, from the seated instruments -----------------------------------------------------------------
LAM8_MD5, MC12_MD5 = 'b837a69ec7c05819b531acff665ae5da', 'e0b55118991688f5c9f1b05fcf50e8ae'   # drive/MANIFEST.tsv; extracted/LEDGER.tsv
assert md5(open(MEM + 'lam8.py', 'rb').read()) == LAM8_MD5, 'lam8.py is not the mirror\'s'
assert md5(open(MEM + 'mc12.py', 'rb').read()) == MC12_MD5, 'mc12.py is not chat 58\'s'
p = subprocess.run([sys.executable, MEM + 'r3-q5e-measure.py'], capture_output=True, text=True, cwd=MEM)
print(p.stdout.rstrip()); assert p.returncode == 0 and 'integrity checks: ALL OK' in p.stdout, 'r3-q5e-measure.py did not pass'
gold = open(MEM + 'r3-q5e-measure.out', encoding='utf-8').read(); assert p.stdout == gold, 'r3-q5e-measure.out is not this run'
import re as _re
_norm = lambda t: _re.sub(r'\s+', ' ', t)
for s_ in ('eight random intervals reproduced 8 OK', 'pairs + singletons 476776 OK', 'distinct boxes 116138 OK', 'factorised ≠ direct 0 OK',
           'pairs whose box has void > 0 340929 OK', 'void-free fraction (pairs + singletons), four decimals 0.2849 OK',
           'cells at the three caps [976, 8847, 25748] OK', 'peel = direct everywhere, message arity 1 True OK',
           '|Λ ∩ {2S ≤ q+1}| (the constraint is not redundant) 911 OK', 'max message arity with the cycle [2] OK',
           'tree-style count wrong on (9, 40) OK', 'eight-term sieve over the triangle right on (40, 40) OK',
           '|box∩Λ|=280 (tree count), |box∩Λ\'|=240; correction = 40'):
    assert s_ in _norm(p.stdout), s_
print('MEASURED at this build: every figure entry 1831 states reproduces from r3-q5e-measure.py.')
q = subprocess.run([sys.executable, MEM + 'mc12.py'], capture_output=True, text=True, cwd=MEM)
print(q.stdout.rstrip()); assert q.returncode == 0, 'mc12.py failed'
MC12_LINES = ['|Λ| = 976  bottom = (1, 0, 1, 0, 1, 0, 0, 0)  |J(Λ)| = 17', 'covering relations in J(Λ): 20', 'bijection cell↦word: OK',
              'pairs 475800: OR failures 0, AND failures 0', 'words in {0,1}^17 = 131072; accepted by the 20 implications = 976 -> exactly Λ',
              'accepted set == image of Λ: True', 'height of the generator poset J(Λ) (longest chain, in generators): 5',
              'balanced AND tree over 20 gates: depth 5; implication gate 1; total accept depth 6',
              'bits carried 17; bits needed log2(976) = 9.93; surplus 7.07', 'occupancy 976/131072 = 0.7446%']
assert q.stdout.split('\n')[:10] == MC12_LINES and q.stdout.count('\n') == 10, 'mc12.py did not print its ten lines'
print('MEASURED at this build: every figure entry 1832 states reproduces from mc12.py (chat 58, seated byte-exact).')

# ---- the volumes as they stand --------------------------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
r = txt[REG]; assert r.count('### 1831\n') == 0 and r.count('### 1832\n') == 0 and r.rstrip().endswith('Registers 347. (a correction.)')

ENTRIES = """

### 1831

**THE BOX COUNT'S CLOSED FORM WAS ASSERTED FROM THE TREE AND IS NOW PROVED, IN BOTH DIRECTIONS, WITH THE LEAF CONVENTION STATED.** *The L.box object carried a one-sentence statement ("factorises because the constraint graph is a tree; no Möbius sieve needed") at grade COMPUTED, and §10.4 states the factorisation with its two closed-form leaves, verified on eight random intervals. Measured in chat 58: the factorisation agrees with direct enumeration on every box [x∧y, x∨y] of Λ at the base caps — 475,800 unordered pairs and 976 singletons, 116,138 distinct boxes, zero discrepancies — and the full peel of the caterpillar, one coordinate per step, carries a message of one argument at every step and agrees with enumeration on 100 random boxes at each of 976, 8,847 and 25,748 cells; the argument uses no cap. The converse is Freuder's: width 1 if and only if the constraint graph is a forest, so a cycle forces a two-coordinate message and the Rota sieve with its signs — witnessed on Λ by closing the triangle k—q—2S with 2S ≤ q+1 (976 cells to 911; elimination width 2; tree-style count wrong on 9 of 40 boxes, eight-term sieve right on 40 of 40; box lo = (2,1,2,0,2,0,0,0), hi = (3,1,3,2,3,1,1,3): 280 against 240, the 40 being the box's points of Λ violating the closing constraint). Reader-facing ambiguity recorded, not edited: §10.4 writes the leaves as hi₇/lo₇ (2S) and hi₆/lo₆ (g), coordinate position counted from zero in the order (n, ℓ, k, q, e, f, g, 2S); the book elsewhere counts eight coordinates from one. The object stated the convention as it stood at BUILD59; the main volume is untouched pending M's ruling (MV-DEF-01, docketed with this pass). Grade COMPUTED → PROVED. Drafted at chat 58 (MC-11) as slip B2-C3; seated under RUL-153 Q5. Re-derived at this build by r3-q5e-measure.py, seated with this entry with its golden — a standard-library instrument of R3's following chat 58's mc11.py and mc11b.py definition by definition, those needing numpy (M's ruling, passes 4 and 5); Λ₈ from the seated tower-2.py, the direct count by bitsets where the pack used numpy — the eight random intervals of seed 1106 reproduced 8 of 8; 476,776 pairs and singletons, 116,138 distinct boxes, 0 discrepancies, 340,929 pairs with void, void-free 0.2849; leaf-peeling at 976, 8,847 and 25,748 cells, 100 boxes each, 0 failures, message arity 1 throughout; the closing constraint 976 to 911, arity 2, tree-style count wrong on 9 of 40, eight-term sieve right on 40 of 40, the exhibit 280 / 240 / 40. Cites the L.box object, L.tree, L.void, L.voidfrac and §10.4; register 347 for treeness as the hypothesis. Both states preserved.* Registers 347; 1830. (a correction.)

### 1832

**THE BINARY LANGUAGE'S CUT IS EXACT AS A SET, NOT ONLY AS A COUNT, AND "DEPTH FIVE" NAMES ONE OF THREE CIRCUITS.** *§11.1.1 states that the twenty cover-implications cut 131,072 words to exactly 976 and that the circuit accepts at a depth of five; L.bits and L.circuit carried both at grade COMPUTED; registers 267 and 331 state the same. Measured in chat 58: J(Λ) has 17 generators and 20 covering relations; cell ↦ word is injective on all 976 cells; join is bitwise OR and meet bitwise AND with zero failures over all 475,800 unordered pairs; the twenty implications accept exactly 976 of the 131,072 words and the accepted set is equal as a set to the image of Λ, which the record had asserted only as a count; 17 bits carried, log₂976 = 9.93 needed, 7.07 surplus, occupancy 0.7446%. The depth figure is reading-dependent and all three are now recorded: unbounded fan-in 2; two-input accept circuit ⌈log₂20⌉ = 5 above the implication level, 6 in total; downward forcing circuit 4 covering steps along the longest chain of 5 generators. The book's five is the AND-tree reading and the objects said so, as they stood at BUILD59. Grades COMPUTED → PROVED on both objects; L.circuit gained L.birk as a dependency and Birkhoff 1937 as a source, the cut being the down-set theorem. Nothing withdrawn. Drafted at chat 58 (MC-12) as slip B3-C1; seated under RUL-153 Q5. Re-run at this build by chat 58's own mc12.py, a standard-library instrument seated as it is with this entry beside lam8.py, the Λ₈ builder it imports — |J(Λ)| = 17, 20 covering relations, the bijection, 0 OR and 0 AND failures over 475,800 pairs, 976 of 131,072 accepted and the accepted set equal to the image of Λ, longest chain 5, AND-tree depth 5 and total 6, 17 / 9.93 / 7.07 / 0.7446%. Cites L.bits, L.circuit, L.birk and §11.1.1. Both states preserved.* Registers 267; 331. (a correction.)
"""
def with_entries(t): return t.rstrip() + ENTRIES + '\n'
SUBS = {}
new = dict(txt)
new[REG] = with_entries(new[REG])

# ---- the counts, from the seated tools on the members as they will stand (entries 1815 and 1816's classes) --------------
stage = tempfile.mkdtemp(prefix='r3-q5a-')
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
print('register_cites with 1831-1832: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %s' % (CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, TOP))
print('kinds.py: %d %s' % (K_N, K))
rr, edits = cm.recount(new[REG]); assert edits
for o, n in edits: print('recount: %s -> %s' % (o[:50], n[:50]))
c = rc.count(rr)
def sub1(t, pat, repl, label):
    m = re.search(pat, t, re.M); assert m, label + ': anchor absent'
    n = repl(m); assert t.count(m.group(0)) == 1, label + ': anchor not unique'
    print('%-40s %s -> %s' % (label, m.group(0)[:60].replace('\n', ' '), n[:60].replace('\n', ' ')) if n != m.group(0) else '%-40s unchanged' % label)
    return t.replace(m.group(0), n)
for kind in ('a finding', 'a correction', 'a measurement', 'a new protocol', 'a withdrawal', 'prior art', 'an open question', 'a fault of mine'):
    rr = sub1(rr, r'^\| \*\*%s\*\* \| (\d[\d,]*) \| (\d+) \|' % re.escape(kind), lambda m, kind=kind: '| **%s** | %s | %s |' % (kind, g(K[kind]), m.group(2)), 'kinds row ' + kind)
rr = sub1(rr, r'by `kinds\.py` over the (\d[\d,]*) entry headings,', lambda m: 'by `kinds.py` over the %s entry headings,' % g(K_N), 'kinds headings')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited by other entries\.\*\*', lambda m: '**%d entries are cited by other entries.**' % CITED_BY, 'cited by entries')
rr = sub1(rr, r'the (\d+) cited seven times or more:', lambda m: 'the %d cited seven times or more:' % len(TOP), 'the N cited')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited in the main volume\'s chapters and appendices; (\d[\d,]*) counting the four compendia and the two papers; (\d[\d,]*) counting citations by other entries\.\*\*',
          lambda m: '**%d entries are cited in the main volume\'s chapters and appendices; %d counting the four compendia and the two papers; %s counting citations by other entries.**' % (CITED_MAIN, CITED_MC, g(CITED_ANY)), 'cited 3 figures')
rows = re.findall(r'^\| \*\*(\d+)\*\* \| (\d+)× \| (.*) \|$', rr, re.M)
what = {int(e): w for e, _, w in rows}
# No entry is expected to reach seven citations with this pass; if one does the instrument refuses (a new row is a hand act).
NEW_ROWS = {}
norm = lambda t: re.sub(r'\W', '', t).casefold()
def headline(e):
    body = new[REG].split('\n### %d\n' % e, 1)[1]; return re.match(r'\s*\*\*(.+?)\*\*', body, re.S).group(1).strip()
for e, w in NEW_ROWS.items(): assert norm(headline(e)) == norm(w), (e, headline(e))
assert sorted(set(what) | set(NEW_ROWS)) == sorted(n for n, _ in TOP) and not (set(what) & set(NEW_ROWS)), ('the >=7 set changed beyond the hand-written rows; REFUSED', sorted(what), TOP)
what.update(NEW_ROWS); print('table: +%d row(s) %s' % (len(NEW_ROWS), sorted(NEW_ROWS)))
i0 = rr.index('| entry | cited | what it established |\n|---|---|---|\n'); i1 = rr.index('\n\n', i0)
rr = rr[:i0] + '| entry | cited | what it established |\n|---|---|---|\n' + ''.join('| **%d** | %d× | %s |\n' % (n, k, what[n]) for n, k in TOP) + rr[i1 + 1:]
new[REG] = rr
mm = new[MAIN]
mm = sub1(mm, r'(\d[\d,]*) entries, 1 to (\d+), at this build \(2026-09-04\)', lambda m: '%s entries, 1 to %d, at this build (2026-09-04)' % (g(c['headings']), c['highest']), 'main: at this build')
mm = sub1(mm, r'436 entries when this paragraph was written, (\d[\d,]*) at this build', lambda m: '436 entries when this paragraph was written, %s at this build' % g(c['headings']), 'main: N at this build')
mm = sub1(mm, r'at this build the main volume cites (\d+) entries', lambda m: 'at this build the main volume cites %d entries' % CITED_MAIN, 'main: cites N')
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
if WRITE: assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD108 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob)); nb = ob
for n in (MAIN, REG):
    assert ms[n] == old[n]; b0 = block(n, ms[n]); assert nb.count(b0) == 1; nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
rv = nb
for n in (MAIN, REG):
    b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1; rv = rv.replace(b1, block(n, ms[n]))
assert md5(rv) == OLD_M_MD5, 'reverse FAILED'
print('BUILD108 -> BUILD109: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines' % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))
if WRITE: assert not os.path.exists(NEW_M); open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else: print('DRY RUN — nothing installed')
