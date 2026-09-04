#!/usr/bin/env python3
"""r3-q5b.py — R3: Q5 pass 2. The chat-54 B-list batch 1 slips B1-C1, B1-C2, B1-C3 seated as registers 1826–1828, every
figure re-derived first by r3-q5b-measure.py (chat 54 left no instrument pack; M ruled the re-run is by an instrument of
R3's, named as a re-derivation), seated beside them with its golden. BUILD105 -> BUILD106 main.

No volume site is edited: the slips' corrections are already in the volumes (§8.6 prints the order dimension as seven)
and the compendium objects they corrected by handle (L.dim, L.omega, L.sperner) are no longer printed by the live
Mathematical Compendium, which names the handles only in its bibliography (r2-bib2, register 1813's class). The count
classes of entries 1815 and 1816 are re-taken in the same build.

Usage:  python3 r3-q5b.py            dry run (runs the measurement, builds nothing)
        python3 r3-q5b.py --write    writes staging members + BUILD106 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib, importlib.util, time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD105_main_and_register.md'); OLD_M_MD5 = 'dae0163204d1604764c45cfd0fb4f094'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD106_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build106') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the measurement, from the seated instrument ------------------------------------------------------------------------
p = subprocess.run([sys.executable, MEM + 'r3-q5b-measure.py'], capture_output=True, text=True, cwd=MEM)
print(p.stdout.rstrip()); assert p.returncode == 0 and 'integrity checks: ALL OK' in p.stdout, 'r3-q5b-measure.py did not pass'
gold = open(MEM + 'r3-q5b-measure.out', encoding='utf-8').read(); assert p.stdout == gold, 'r3-q5b-measure.out is not this run'
for s_ in ('width of J(Λ₈) = dim(Λ₈), Dilworth 1950                          7', 'seven join-irreducibles, pairwise incomparable True', 'width of J(Λ₉): per-axis rise fails at the first step            7',
           'max ω over Λ₈ = the coordinate count                             8', 'cells attaining ω = 8                                            100', 'min ω over Λ₈ (the floors n, k, e ≥ 1)                           3',
           'largest antichain of Λ₈ = size of a minimum chain partition (Dilworth) 122', 'rank skew = mean rank − centre of the span, two decimals         -0.43', 'reflection x ↦ max − x: survivors                                8'):
    assert s_ in p.stdout, s_
print('MEASURED at this build: every figure the three entries state reproduces from r3-q5b-measure.py.')

# ---- the volumes as they stand --------------------------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
r = txt[REG]; assert r.count('### 1826\n') == 0 and r.rstrip().endswith('Registers 627; 1823. (a correction.)')

RD = 'Re-derived at this build by r3-q5b-measure.py, seated with this entry with its golden — chat 54 left no instrument, and M ruled (RUL-153, pass 2) that the re-run is an instrument of R3\'s, named as such; Λ₈ is taken from the seated tower-2.py — '
ENTRIES = """

### 1826

**THE ORDER DIMENSION OF Λ₈ IS SEVEN, NOT EIGHT; THE ASSERTED FIGURE IS CORRECTED BY THE DERIVATION IT NEVER HAD.** *Register 35 proved dim = 3 at three coordinates both ways; register 36 exhibited the standard example. The extension "dimension = coordinate count, rising by one per adjoined axis" was carried without re-running the lower-bound half at any later stage, and register 409 recorded it as the one underived quantity in Part II. The derivation now run: width of J(Λ₈) = 7, certified by a seven-chain Dilworth partition (upper) and a seven-generator antichain (lower — (1,0,1,0,1,0,0,1), (1,0,1,0,2,1,0,0), (1,0,1,0,3,0,0,0), (1,0,1,1,1,0,0,0), (1,0,2,0,1,0,0,0), (2,1,1,0,1,0,0,0), (3,0,1,0,1,0,0,0)), so dim(Λ₈) = 7 by Dilworth 1950. Mechanism: every g-raising generator lies above the q-atom because g ≤ q — the coupling welds g's order-information to q's; kin to register 1143's production rule (monotone production adds no join-irreducibles). Λ₉ also measures width 7 (|Λ₉| = 1,654 confirmed), so per-axis rise fails at the first step. Corrects the claim register 409 records; §8.6 now prints the seven; the compendium object L.dim, as it stood at BUILD56, carried the theorem, and the live compendium names the handle only in its bibliography. Drafted at chat 54 (B-list batch 1, MC-06) as slip B1-C1 and queued for a "Register 1.1"; seated under RUL-153 Q5. """ + RD + """|J(Λ₈)| = 17 and its width 7, the seven listed generators join-irreducible and pairwise incomparable, |J(Λ₉)| = 20 with width 7 on 1,654 cells. Both states preserved.* Registers 35; 36; 409; 1143. (a correction.)

### 1827

**ω(N(x)) IS BOUNDED BY THE COORDINATE COUNT, NOT THE ORDER DIMENSION.** *The printed proof — one prime per coordinate — always proved ω ≤ 8; the bound was quoted against dim(Λ) when 8 was believed to be the dimension. With dim = 7 (register 1826) the quoted form is false — the cell (2,1,3,3,2,1,3,3) attains ω = 8 > 7 — and the corrected form ω ≤ 8 is tight at that cell. The object L.omega's dependency on L.dim is released (now L.arith, L.def), as it stood at BUILD56. Drafted at chat 54 as slip B1-C2; seated under RUL-153 Q5. """ + RD + """ω read as the number of coordinates at which a cell is positive: maximum 8 over Λ₈, attained at 100 cells, 8 at (2,1,3,3,2,1,3,3), minimum 3 by the floors n, k, e ≥ 1. Both states preserved.* Registers 1826. (a correction.)

### 1828

**THE PECK INHERITANCE ON L.sperner WAS OVER-BROAD; SPERNER SURVIVES BY DIRECT CERTIFICATE, SYMMETRY DOES NOT TRANSFER.** *Stanley 1980's Peck property includes rank-symmetry, which Λ measurably lacks (skew −0.43; 5 against 4 at rank 4). The register entry recording the compendium generator fix quoted the old wording ("Λ is of that form, and the property is INHERITED") — that entry stands as history; the compendium object, as it stood at BUILD56, carried the direct proof: a Dilworth partition of all 976 cells into 122 chains, max antichain = 122 = the largest level. Register 44 had stated the property (Sperner though not rank-symmetric); register 1794 later read the rank-skew and Sperner entries against each other. Drafted at chat 54 as slip B1-C3; seated under RUL-153 Q5. """ + RD + """the rank sequence 1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1 over ranks 3–20, log-concave; the largest antichain 122 by Dilworth, equal to the largest level; the mean rank 11.0666 sitting 0.43 below the centre of the span, which is the convention that reproduces the slip's skew (the third standardised moment gives +0.14 and is not it — recovered, stated); 5 against 4 at the second level from either end; eight cells surviving the reflection x ↦ max − x, none fixed. Both states preserved.* Registers 44; 1228; 1794. (a correction.)
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
print('register_cites with 1826–1828: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %s' % (CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, TOP))
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD105 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob)); nb = ob
for n in (MAIN, REG):
    assert ms[n] == old[n]; b0 = block(n, ms[n]); assert nb.count(b0) == 1; nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
rv = nb
for n in (MAIN, REG):
    b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1; rv = rv.replace(b1, block(n, ms[n]))
assert md5(rv) == OLD_M_MD5, 'reverse FAILED'
print('BUILD105 -> BUILD106: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines' % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))
if WRITE: assert not os.path.exists(NEW_M); open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else: print('DRY RUN — nothing installed')
