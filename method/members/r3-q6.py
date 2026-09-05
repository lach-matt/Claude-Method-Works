#!/usr/bin/env python3
"""r3-q6.py — R3: Q5 pass 6. Registers 603 and 604 corrected and 605's properties 1–3 withdrawn from the seed-cap return
(SEED-CAP-FINDING.md, EXPANSION-MC54.md in the mirror) as registers 1833, 1834 and 1835 (two corrections, one withdrawal), every figure re-derived first by r3-q6-measure.py — a
standard-library re-derivation of chat 65's seedcensus.py / seedenum3.py (numpy) / coverscheck.py, M's ruling for the
stdlib passes — seated beside it with its golden and with covers8.json, the return's enumeration, seated as the
mirror's bytes plus the closing newline the bundle format requires (M's ruling, pass 6 item 4). BUILD109 -> BUILD110 main.

No volume site is edited: §14.5.12–§14.5.14 stand as printed with register 1820's pointer at §14.5.12. The six R-rows of
OWED-REGISTER-EXPANSIONS.md seat nothing (they resolve to seated entries; W-233). The count classes of entries 1815 and
1816 are re-taken in the same build.

Usage:  python3 r3-q6.py            dry run (runs the measurement, builds nothing)
        python3 r3-q6.py --write    writes staging members + BUILD110 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib, importlib.util, time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD109_main_and_register.md'); OLD_M_MD5 = 'f138897abdf824208e5e3d9647864364'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD110_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build110') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the measurement, from the seated instrument ------------------------------------------------------------------------
COVERS8_MD5 = '5bb92ebb6cd122115b8b3a96372868e9'   # drive/MANIFEST.tsv
raw = open(MEM + 'covers8.json', 'rb').read()
assert raw.endswith(b'\n') and not raw.endswith(b'\n\n') and md5(raw[:-1]) == COVERS8_MD5, 'covers8.json is not the mirror\'s bytes plus one closing newline'
p = subprocess.run([sys.executable, MEM + 'r3-q6-measure.py'], capture_output=True, text=True, cwd=MEM)
print(p.stdout.rstrip()); assert p.returncode == 0 and 'integrity checks: ALL OK' in p.stdout, 'r3-q6-measure.py did not pass'
gold = open(MEM + 'r3-q6-measure.out', encoding='utf-8').read(); assert p.stdout == gold, 'r3-q6-measure.out is not this run'
import re as _re
_norm = lambda t: _re.sub(r'\s+', ' ', t)
for s_ in ('alphabet slots 25 OK', 'envelope steps 77 OK', 'universe 102 OK', '6-covers 0 OK', '7-covers found 24585 OK', 'distinct as sets 24585 OK',
           'the enumeration here == covers8.json, set for set True OK', 'cells common to every cover [(2, 1, 3, 3, 2, 1, 3, OK',
           'corner 3 (2,1,3,3,2,1,3,0) in every cover; corner 4 (11001100) in 13.7% (True, 13.7) OK', 'corners 1 and 2, percent of covers (register 1820\'s 59 % and 28 %) (58.9, 27.8) OK',
           'unit template by its free coordinate: covers with e = 1, e = 2, e = 3 (register 604 allows 1 or 3 only) (684, 290, 1478, True) OK',
           'the six channel conditions of register 603 over the exact covers [70.8, 100.0, 100.0, 1 OK', 'element-forced at Λ₈: s→p, p→s, p→p, null, full; s→s not [True, True, True, Tru OK',
           'covers containing all four core cells (the 519 completions) 519 OK', 'distinct completing cells; none in all; min / median / max (66, True, 3, 12, 157) OK',
           'cap (2, 2, 1, 3, 1): cells, seed decided here (328, 7) OK', 'cap (3, 3, 1, 3, 1): cells, seed decided here (976, 7) OK', 'cap (4, 4, 1, 3, 1): cells, seed decided here (1968, 7) OK',
           'greedy cover of 10 cells exhibited, so seed ≤ 10', 'cap (3, 3, 2, 6, 2): s→d, d→s, null, full forced; s→p, p→s, s→s, corner-3-type not [True, True, True, Tru OK'):
    assert s_ in _norm(p.stdout), s_
print('MEASURED at this build: every figure entries 1833–1835 state reproduces from r3-q6-measure.py; the d-shell seed 10 is named there as not re-derived.')

# ---- the volumes as they stand --------------------------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}
r = txt[REG]; assert all(r.count('### %d\n' % e) == 0 for e in (1833, 1834, 1835)) and r.rstrip().endswith('Registers 267; 331. (a correction.)')

ENTRIES = """

### 1833

**REGISTER 603'S SIX CHANNEL CONDITIONS ARE FIVE OVER THE EXACT COVERS, AND THE FIVE ARE THE ℓ ≤ 1 FACE OF AN ENVELOPE-STEP LAW.** *Register 603 states that every minimum seed of Λ₈ contains an s→s, an s→p, a p→s and a p→p transition, a null transition with q = 0 and a full transfer with q = k, in all 219 covers of the sample register 602 recorded; §14.5.12 prints the six at 100%. Measured over the 24,585 minimum covers enumerated exactly (register 1820): s→p, p→s, p→p, q = 0 and q = k hold in every cover, and each is element-forced — some element of the 102 the seed must witness is carried only by cells of that type, so no cover exists without it; s→s holds in 70.8% and is forced by nothing, having never been a step. The five are instances of the envelope-step law (the original-works return of 2026-08-28, theorem T3): a generating set must contain, for each step of the envelope — each value t of a coordinate j's alphabet at which φ̂ᵢⱼ(t) = max{cᵢ : cⱼ ≤ t} first takes its value, the alphabet's minimum or any t where it exceeds its value at the predecessor — a cell with cⱼ ≤ t carrying cᵢ = φ̂ᵢⱼ(t), and covering every step with every alphabet value suffices; the alphabet half (theorem T2, register 1835) forces the null transition from q's alphabet and the full transfer from q's maximum with q ≤ k. At the caps (2,2,1,3,1), (3,3,1,3,1) and (4,4,1,3,1) — 328, 976 and 1,968 cells, seed 7 at each by branch and bound — the same five are element-forced and s→s is not; at the d-shell cap (3,3,2,6,2), 7,605 cells, s→p and p→s are no longer element-forced — their fall from universality there is the return's measurement — and s→d and d→s are element-forced beside q = 0 and q = k, as the law reads at ℓ ≤ 2. The moral of 603 — the constraint is on the channel, not on the cell — survives corrected: five of six at ℓ ≤ 1, and the six generalise to the steps. Returned by the original-works project (SEED-CAP-FINDING.md, EXPANSION-MC54.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with this entry with its golden and with covers8.json, the return's own enumeration — a standard-library instrument of R3's following chat 65's seedcensus.py, seedenum3.py and coverscheck.py definition by definition, that enumeration needing numpy (M's ruling, passes 4 and 5): the census of 25 alphabet slots and 77 envelope steps; no 6-cover; 24,585 seven-cell covers, equal set for set to covers8.json, every one covering all 102 elements with no redundant cell; the six conditions at 70.8 / 100 / 100 / 100 / 100 / 100%; the forcing at the four caps. Cites register 1820 for the exact count, §14.5.12 as printed, and the Mathematical Compendium's The seed's forced set, corrected. Both states preserved.* Registers 602; 603; 1820; 1835. (a correction.)

### 1834

**REGISTER 604'S UNIT TEMPLATE IS IN ONE COVER IN TEN, NOT IN EVERY ONE, AND ITS FREE COORDINATE TAKES THE MIDDLE VALUE THE ENTRY EXCLUDED.** *Register 604 states that all 219 covers contain a cell matching (3, 0, 1, 1, e, 0, 1, 1) with e free at 1 or 3, and §14.5.13 prints the fork at 157 covers with e = 3 against 62 with e = 1. Over the 24,585 minimum covers enumerated exactly (register 1820) the template appears in 2,452 — 10.0% — with e = 3 in 1,478, e = 1 in 684 and e = 2 in 290, no cover holding two of the three; the template is not forced, and what the entry read as its function — carrying the value one, the alphabet values q = 1, g = 1 and 2S = 1 among the fifteen elements the extremal corners miss — is done in every cover by some cell, because every alphabet value of every coordinate is witnessed by every seed (theorem T2, register 1835), and by this cell in one cover in ten. The sample's 219 of 219 was a biased randomised sample, the return's word, as the four corners' 140 of 140 was greedy covering's attractor (register 596). Returned by the original-works project (SEED-CAP-FINDING.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with register 1833 — the template's three cells named, 10.0%, 684 / 290 / 1,478. Cites §14.5.13 as printed and the Mathematical Compendium's The seed's forced set, corrected. Both states preserved.* Registers 596; 604; 1820; 1835. (a correction.)

### 1835

**REGISTER 605'S PROPERTIES 1 TO 3 ARE WITHDRAWN AT Λ₈: ITS PREMISE FAILS THERE, ITS FOURTH PROPERTY IS A LAW WITH A PROOF, AND CORNER 3'S TYPE IS FORCED AT THE ℓ ≤ 1 CAPS ONLY.** *Register 605 read the five cells of the 219-cover sample as binary words — corner 1 and corner 2 exact complements on 3 bits, corner 3 and the unit cell on 3, corner 4 fully specified at 11001100 — with every coordinate spoken both ways, measured at one cap and not yet a law. Over the 24,585 minimum covers enumerated exactly (register 1820) the premise fails: corner 3, (2,1,3,3,2,1,3,0), is in every cover and is the only cell that is; corner 1 is in 58.9%, corner 2 in 27.8%, corner 4 in 13.7%, the unit template in 10.0%. So properties 1 to 3 — the two complement pairings and 11001100 as the static transition of every seed — describe the sample and are withdrawn as statements about Λ₈, refuted there rather than untested. Property 4 is a law with a proof (theorem T2 of the original-works return): ℛ recovers each coordinate's alphabet from its argument, so any X₀ with ℛ(X₀) = Λ witnesses every value of every coordinate, its minimum and maximum among them, and no cap enters the proof; where a coordinate's alphabet has at least two values its column receives both a 0 and a 1 in every seed. Corner 3's own universality is cap-specific: at the three ℓ ≤ 1 caps (328, 976 and 1,968 cells) cells of its type — ℓ, k, q, f and g at their maxima with q = k and 2S at its minimum, n and e free — are element-forced, corner 3 being the one of the four cells of that type at Λ₈ that every cover holds, and at the d-shell cap (3,3,2,6,2), 7,605 cells, they are not. The multiplicity has a name: no element of the census has fewer than four carriers, so ℛ(Λ∖{x}) = Λ for every cell x and Λ₈ has no extreme point; ℛ on Λ₈ fails the anti-exchange property maximally (Edelman 1980; Edelman and Jamison 1985: every closed set is the hull of its extreme points if and only if the closure is anti-exchange), which is what permits 24,585 minimum generating sets with one cell common to all — what the return calls Chvátal's forced set of the derived cover instance. §14.5.14's table stands as printed, now read as a description of the sample; its closing sentence — not tested at other caps, a description of Λ₈ — is superseded by this entry, the section unedited. Returned by the original-works project (SEED-CAP-FINDING.md, EXPANSION-MC54.md); seated under RUL-153 Q5. Re-derived at this build by r3-q6-measure.py, seated with register 1833: the frequencies of the four corners and the template over the enumeration; the forcing of corner 3's type at the four caps; the seed 7, 7, 7 at the ℓ ≤ 1 caps by branch and bound and at most 10 at the d-shell cap, a greedy 10-cover exhibited — that no 9-cover exists there is the return's measurement and is not re-derived here. Cites registers 602, 603, 604 and 605 as they stood, 1820, 1833 and 1834, §14.5.14 as printed, and the Mathematical Compendium's The seed's forced set, corrected. Both states preserved.* Registers 602; 603; 604; 605; 1820; 1833; 1834. (a withdrawal.)
"""
def with_entries(t): return t.rstrip() + ENTRIES + '\n'
SUBS = {}
new = dict(txt)
new[REG] = with_entries(new[REG])

# ---- the counts, from the seated tools on the members as they will stand (entries 1815 and 1816's classes) --------------
stage = tempfile.mkdtemp(prefix='r3-q6-')
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
print('register_cites with 1833-1835: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %s' % (CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, TOP))
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
# Entries the three pointers carry to seven citations or more (602, 1820): their rows are hand-written here (a new row is a hand act) and each headline asserted.
NEW_ROWS = {1820: "REGISTER 602'S 219 MINIMUM COVERS ARE A SAMPLE OF THE 24,585 ENUMERATED EXACTLY, AND THE ENTRY AND §14.5.12 NOW POINT AT THE EXACT COUNT.", 602: 'THE FOUR CORNERS SURVIVE A HARDER TEST, AND THE REDUNDANCY GRADIENT STEEPENS.'}
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
mm = sub1(mm, r'(\d[\d,]*) entries, 1 to (\d+), at this build \(\d{4}-\d\d-\d\d\)', lambda m: '%s entries, 1 to %d, at this build (2026-09-05)' % (g(c['headings']), c['highest']), 'main: at this build')   # the build lands on 5 September (UTC); the date is the sentence's
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD109 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob)); nb = ob
for n in (MAIN, REG):
    assert ms[n] == old[n]; b0 = block(n, ms[n]); assert nb.count(b0) == 1; nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
rv = nb
for n in (MAIN, REG):
    b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1; rv = rv.replace(b1, block(n, ms[n]))
assert md5(rv) == OLD_M_MD5, 'reverse FAILED'
print('BUILD109 -> BUILD110: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines' % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))
if WRITE: assert not os.path.exists(NEW_M); open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else: print('DRY RUN — nothing installed')
