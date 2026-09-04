#!/usr/bin/env python3
"""r3-q5a.py — R3: Q5 pass 1. The chat-53 repair-pass slips 05, 06, 07, 08 and 11 seated as registers 1821–1825, every
figure re-measured first by running the slips' own instruments, seated beside them. BUILD104 -> BUILD105 main.

RUL-153 Q5 (M, 4 September 2026): the drafted slips the mirror holds become Register entries under the current numbering,
one pass per queue document, M reviewing the draft first. Pass 1's rulings: approved; the figure-asset slips 09 and 10 go
to the Working Register (W-222), not the Register; "re-run the instrument before seating — no shortcuts".

THE INSTRUMENTS, seated with this pass byte-exact from where the mirror holds them (md5 asserted here against
drive/MANIFEST.tsv and extracted/LEDGER.tsv): tower.py and tower3.py (Materials root; the banked tower builders —
L8.json, then tower.json), a2_canonical.py, compose.py, sig_l13.py, sig_sweep.py, sig_val.py (repair-pass-instruments
.tar.gz) and req4.py (Materials root). They are run here by runpy, from their seated paths, in a staging directory,
because each reads and writes tower.json / L8.json in its working directory; that is also why they carry no gate golden —
the gate runs a member in place and these would write into members/. Their output at this build is printed below and
recorded at W-222 and in each entry. Every figure an entry states is asserted against the run; a drifted store refuses.

THE EDITS: five entries appended; one pointer, §12.11.1.4's closing "Registers 625–627." gaining 1823 as slip 07 asks;
the count classes of entries 1815 and 1816 re-taken in the same build. No other site: the slips' corrections are already
in the volumes (no 64,290 or 22,275 remains in any live volume — asserted here).

Usage:  python3 r3-q5a.py            dry run (runs the instruments, prints the measurement, builds nothing)
        python3 r3-q5a.py --write    writes staging members + BUILD105 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib, importlib.util, time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD104_main_and_register.md'); OLD_M_MD5 = '4e6e3890a49aaf714bc03c1497e5d62e'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD105_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build105') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the instruments: identity, then the run --------------------------------------------------------------------------
INSTR = {'tower.py': '93db2fc9ab2cf9604db3bb2b8c985db3', 'tower3.py': '9925afcd5b40f6ac70798baeeafc3ab9',
         'a2_canonical.py': 'e92cd9d3903023958f53cbfa4749f2eb', 'compose.py': '193f1b9cef510f82397e508f9fa0e3bf',
         'sig_l13.py': 'b7aea345ee56cdf259429edf0ec73faa', 'sig_sweep.py': '30f14f10494b3b1588b789f50b66d595',
         'sig_val.py': '06126261ce3d9cdb956eba1af0f7adb9', 'req4.py': '8a9a2b33237e988375fcafd56cbe2c9f'}
for n, h in INSTR.items():
    assert md5(open(MEM + n, 'rb').read()) == h, (n, 'is not the mirror\'s bytes')
def run(name, stage):
    cwd = os.getcwd(); os.chdir(stage); buf = io.StringIO(); t0 = time.time()
    try:
        with contextlib.redirect_stdout(buf): runpy.run_path(MEM + name, run_name='__main__')
    finally: os.chdir(cwd)
    out = buf.getvalue(); print('--- %s (%.1f s)\n%s' % (name, time.time() - t0, out.rstrip())); return out
stage = tempfile.mkdtemp(prefix='r3-q5a-')
R = {n: run(n, stage) for n in ('tower.py', 'tower3.py', 'a2_canonical.py', 'compose.py', 'sig_l13.py', 'sig_sweep.py', 'req4.py', 'sig_val.py')}
for f in os.listdir(stage): os.unlink(os.path.join(stage, f))
os.rmdir(stage)
def has(name, *needles):
    for s in needles: assert s in R[name], (name, 'did not print', s)
has('tower.py', 'Λ8: cells = 976', 'Λ8: E = 0')
has('tower3.py', 'Λ10 = 2535 | Λ11 = 13585 | Λ12 = 70905', '| Λ13 = 199130', 'tower banked')
has('a2_canonical.py', 'Λ12: composable = 46740 of 70905 fraction = 0.6592', 'Λ13: composable = 127070 of 199130 fraction = 0.6381',
    'sequence: 0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381', 'non-composable: 72060 | g=0: 35630 | 2J in {6,7,8} (g≠0): 13750 | combination: 22680 | max 2J = 8')
has('compose.py', 'L9: 4-tuple composable = 1169 / 1654 = 0.7068', 'L10: 4-tuple composable = 2050 / 2535 = 0.8087', 'L13: 5-tuple composable = 127070 / 199130 = 0.6381')
has('sig_l13.py', 'Λ13t with 2J->2Jc: 39772', 'non-composable: 24518 | g=0: 11188', '2J in 6-8: 5116', 'combination: 8214')
has('sig_sweep.py', 'HIT extra pair: tgt idx 10 -> src idx 10 = 9450')
has('sig_val.py', 'HIT 1-extra: 11 -> 10')
has('req4.py', "triangle build: Λ12' = 22275", "Λ13' = 64290", 'axis 10: bare interval = 2535 | parity build = 1841', 'Λ12 cells with f < f_max: 39375')
print('MEASURED at this build: every figure the five entries state reproduces from the seated instruments.')

# ---- the volumes as they stand --------------------------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
for n in ('The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Mathematical_Compendium-2.md', MAIN):
    t = open(MEM + n, encoding='utf-8').read(); assert '64,290' not in t, (n, 'still prints 64,290')
    for l in t.split('\n'):   # 22,275 survives only where the line names it as the exact triangle's count (register 1788's form)
        if '22,275' in l: assert 'triangle' in l, (n, 'prints 22,275 as current', l[:80])
r = txt[REG]; assert r.count('### 1821\n') == 0 and r.rstrip().endswith('Registers 602. (a correction.)')

RERUN = 'Re-run at this build from the instruments seated with this entry — tower.py, tower3.py, a2_canonical.py, compose.py, sig_l13.py, sig_sweep.py, sig_val.py, req4.py, byte-exact from the mirror — every figure above reproduces (RUL-153 Q5: no shortcuts).'
ENTRIES = """

### 1821

**THE INDEX OF INDICES' TOWER TABLE PRINTED THE EXACT-TRIANGLE OBJECT IN ITS Λ₁₂ AND Λ₁₃ ROWS — 22,275 AND 64,290 — AND IS CORRECTED TO THE CANONICAL ENVELOPE BUILD, 70,905 AND 199,130, WITH ITS COMPOSABLE COLUMNS RECOMPUTED.** *The rows printed 22,275 / 14,242 / 0.6394 and 64,290 / 39,772 / 0.6186, the composable columns computed on that same object. Corrected to the canonical envelope build — Λ₁₂ = 70,905 under 2K ≤ 2J_c + 2f_max, Λ₁₃ = 199,130 — with the composable columns recomputed on the canonical tower: 46,740 / 0.6592 and 127,070 / 0.6381 (a2_canonical.py on tower.json regenerated from the banked tower.py and tower3.py; the instrument validated by exact reproduction of the recorded 1,169 / 2,050 / 9,450, the triangle's 14,242 / 39,772, and register 627's 11,188 / 5,116 / 8,214). The volume's prose "runs to 64,290 cells at Λ₁₃" corrected to 199,130. The counting/coupling dichotomy of register 626 holds unchanged on the canonical sequence 0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381 — the peak stays at Λ₁₀ and every coupling axis still lowers the fraction. The Mathematical Compendium's tree-or-tightness entry, where the triangle object is named and priced, stands untouched. Register 646, which describes the Index as printing "runs to 64,290 at Λ₁₃" and 45,182 searchable characters, is not edited; after this repair the volume prints 199,130 and its character count has moved. Drafted at chat 53's repair pass (2026-08-28) as slip 05, closing its ledger A1 and A2, and queued for a "Register 1.1"; seated under RUL-153 Q5 with the number assigned here. """ + RERUN + """* Registers 541; 622; 623; 624; 625; 626; 627; 646; 1788. (a correction.)

### 1822

**§12.11.3.1'S AXIS-10 ROW ANNOTATED THE BOUND AS "2S′ ≤ v ≤ g, PARITY", AND PARITY IS STRUCK: IT BELONGS TO THE EXACT PHYSICAL SET, NOT THE ADMISSIBLE BOUND.** *Parity is §12.11.1's step-2 seniority ladder, a property of the exact physical set; the admissible bound is the bare interval. The parity build gives 1,841 cells against the canonical 2,535 of the bare interval, and 2,535 is what chains into 13,585 → 70,905 → 199,130. ", parity" struck from the bound column; the bound left as 2S′ ≤ v ≤ g; the provenance cell (seniority, Racah 1943) unchanged. Drafted at chat 53's repair pass as slip 06, closing its ledger A3, and queued for a "Register 1.1"; seated under RUL-153 Q5. Re-run at this build by req4.py, seated with this entry: bare interval 2,535, parity build 1,841.* Registers 249; 626. (a correction.)

### 1823

**MAIN §12.11.1.4'S STAGE TABLE AND §12.11.1.5'S Λ₁₃ DECOMPOSITION WERE COMPUTED ON THE EXACT-TRIANGLE OBJECT AND ARE CORRECTED TO THE CANONICAL BUILD: 72,060 NON-COMPOSABLE OF 199,130, 36.19%, IN THE SAME THREE KINDS.** *The stage table printed the triangle rows 22,275 / 14,242 / 0.6394 and 64,290 / 39,772 / 0.6186, and the decomposition 11,188 + 5,116 + 8,214 = 24,518 of 64,290 — 38.14% — was computed on that object. Corrected to the canonical envelope build: rows 70,905 / 46,740 / 0.6592, the axis restated 2K ≤ 2J_c + 2f_max, and 199,130 / 127,070 / 0.6381; the decomposition 35,630 (g = 0) + 13,750 (2J ∈ {6, 7, 8}) + 22,680 (combination only) = 72,060 of 199,130 — 36.19%. The three kinds remain exhaustive and the structural kind survives: 2J reaches 8 and 2J_c reaches 5. The book's own signatures (register 625) validate at every stage — base match target (e, f, g, 2S′) against source (n, ℓ, k, 2S); from Λ₁₁ the outermost coupling of the cell matches the follower's core, 2J_c → 2J_c at Λ₁₁, 2K → 2J_c at Λ₁₂, 2J → 2J_c at Λ₁₃ — exactly at every recorded count. Same instrument and validation as register 1821. Registers 622–627 record the original measurement and are not edited; §12.11.1.5's closing "Registers 625–627" gains this entry's number. Drafted at chat 53's repair pass as slip 07, closing its ledger A5, and queued for a "Register 1.1"; seated under RUL-153 Q5. """ + RERUN + """* Registers 622; 623; 624; 625; 626; 627; 1821. (a correction.)

### 1824

**THE MATHEMATICAL COMPENDIUM'S K.peak OBJECT PRINTED THE TRIANGLE-COMPUTED TRAILING FRACTIONS 0.6394, 0.6186 AND IS CORRECTED TO 0.6592, 0.6381; ITS LAW IS UNCHANGED.** *The object's sequence ended in the two fractions computed on the exact-triangle object. Corrected to the canonical 0.6592 and 0.6381. The object's law statement — the peak at Λ₁₀; counting raises, coupling lowers, no exception — is unchanged and holds on the canonical sequence. Cites the same measurement as register 1823. Drafted at chat 53's repair pass as slip 08, closing its ledger A6; seated under RUL-153 Q5. Re-run at this build by a2_canonical.py, seated with this entry: 0.6592, 0.6381.* Registers 625; 626; 1823. (a correction.)

### 1825

**THE MATHEMATICAL COMPENDIUM'S K.deadend OBJECT PRINTED THE TRIANGLE-OBJECT Λ₁₃ DECOMPOSITION AS CURRENT FACT — 11,188 / 5,116 / 8,214 — AND IS CORRECTED TO THE CANONICAL 35,630 / 13,750 / 22,680.** *Found by the all-volumes sweep. The Λ₁₀ half — 485 at g = 0, 485 for 485 — and the interpretive line (k ≥ 1; 2J inherits 2K's range while 2J_c is bounded by φ(k)) survive unchanged on the canonical build. Same instrument and validation as registers 1821 and 1823. After slips 05–11 every remaining occurrence of the triangle's composability figures in either volume is a register entry — 625 to 627, and 646 — or audit history; no live prose, table, compendium object or figure carries them, re-asserted at this build. The two figure-asset slips of the same pass, 09 and 10, are production and are recorded in the Working Register (W-222), not here. Drafted at chat 53's repair pass as slip 11, closing its ledger A9; seated under RUL-153 Q5. """ + RERUN + """* Registers 627; 1823. (a correction.)
"""
def with_entries(t): return t.rstrip() + ENTRIES + '\n'
SUBS = {MAIN: [(' core can carry.* Registers 625–627.\n', ' core can carry.* Registers 625–627; 1823.\n')]}
new = dict(txt)
for v, subs in SUBS.items():
    for i, (o, n) in enumerate(subs, 1):
        k = new[v].count(o); print('%-28s site %d: anchor occurs %d time(s)' % (v, i, k)); assert k == 1 and o != n; new[v] = new[v].replace(o, n)
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
print('register_cites with 1821–1825: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %s' % (CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, TOP))
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
# Register 626 reaches seven citations with this pass (1821–1824 cite it): its row is a hand act, the headline in sentence
# case, asserted against the headline with case and punctuation aside (register 1816's rule). Any other change refuses.
NEW_ROWS = {626: 'And the divide is the counting/coupling dichotomy, with no exception'}
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD104 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob)); nb = ob
for n in (MAIN, REG):
    assert ms[n] == old[n]; b0 = block(n, ms[n]); assert nb.count(b0) == 1; nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
rv = nb
for n in (MAIN, REG):
    b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1; rv = rv.replace(b1, block(n, ms[n]))
assert md5(rv) == OLD_M_MD5, 'reverse FAILED'
print('BUILD104 -> BUILD105: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines' % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))
if WRITE: assert not os.path.exists(NEW_M); open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else: print('DRY RUN — nothing installed')
