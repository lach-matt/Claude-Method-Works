#!/usr/bin/env python3
"""r4-b1.py — Phase 1's first seven entries: the subject matter its instruments settled.
BUILD115 -> BUILD116 main.

Phase 1 of PLAN-R4-PUBLICATION is "every computable claim still unproven or contradicted, re-derived
by a standard-library instrument and settled by ENTRY before any prose moves ... Output: one
instrument per class, banked; one Register entry per correction or withdrawal; the count classes
re-taken."  method/PHASE1-LEDGER.md is the leg's ledger and names the instrument behind each.

WHAT IS HERE AND WHAT IS NOT. M's ruling of 7 September: "if it is work matter, it does not belong
in the volumes. if it is subject, it must be included." Seven of the sixteen disposed rows are
subject matter and are seated here. The rest -- the unnamed cap family, the record-carried
compendium counts, register 497 withdrawn and re-cited, the docket's own wrong instance at
molybdenum, and the fifty-one pointers into empty headings -- are work matter and go to the working
register, not to the Register.

NO VOLUME CHANGES. This is a Batch B pass: a Register entry is never edited and nothing is repaired
in a volume by it. The count classes are re-taken in the same build.

Usage:  python3 r4-b1.py            dry run (asserts everything, writes nothing)
        python3 r4-b1.py --write    writes staging members + BUILD116 main
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD115_main_and_register.md')
OLD_M_MD5 = '1fab5b05f6c9c09f075013eefac4de1f'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD116_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build116') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- no volume substitution: this is a Batch B append -------------------------------------------
ENTRY_NS = tuple(range(1842, 1849))
ENTRIES = """

### 1842

**§32.1.1'S SELF-INDEX NAMES AN EXTENT THE BOOK HAS OUTGROWN, AND THE INSTRUMENT THAT COMPUTED IT CANNOT SEE THE DIFFERENCE.** *§32.1.1 prints its index as* **"Recomputed at this build (2026-08-24, bookindex.py), over the thirty-five chapters and six appendices the book now has: 1,021 claims and 400 cells"**. *Measured from the volume's own headings: it has* **thirty-six chapters, numbered 1 to 36 with no gap, and seven appendices, A to G.** **And the seated instrument is bounded by the same two numbers three times over — `APP='ABCDEF'`, the reference filter `1<=r<=35`, and the box side `n=41  # 35 chapters + 6 appendices` — so no re-run of it can ever count Chapter 36 or Appendix G. Three constants, not a reading.** *The answer is a successor that reads the extent as data, which is the route this store has taken twice before (census → census2, r2-reg1a → r2-reg1a3) and never an edit to a seated instrument, which G0c forbids. Measured at this build by that successor, seated with this entry:* **the claim count is 1,021 — the printed figure, current — while cells move 400 → 410, the box 1,681 → 1,849 and E(book) 1,265 → 1,407.** *So the sentence's claim count is right and the three figures that depend on the box are stale, because the box is. The dated reading is retained as what it says it is; the extent it names is not the book's.* Registers 1815; 1816. (a correction.)

### 1843

**THE MAIN VOLUME PRINTS K I nd's REACH AS 45.7 AND THE COLLECTION IT WAS DRAWN FROM SAYS 13.** *§23's table, under* **"Curvature washes out before separation, in every channel in this work"** *, gives three channels with their quotation granularity, their ν_V and their reach:* **K I nd 0.0001 · 160 · 45.7; Na I ns 0.001 · 90 · 20.0; Al I nf 0.01 · 50.7 · 55.0.** *The Spectra Compendium's own rows for those three run* **K I nd n = 3–13 (ν 2.9–12.7), Na I ns n = 3–20 (ν 1.6–18.7), Al I nf n = 4–55 (ν 4.0–55.0)**. **The other two rows fix which column the table is quoting: Al I nf's 55.0 matches both readings, and Na I ns's 20.0 matches the n range and NOT the ν range, which is 18.7. So the column is the top of the principal quantum number range, and two of the three entries reproduce from the collection exactly.** *K I nd's own row reaches n = 13. The volume prints 45.7 — 3.5 times the larger of the two candidates, and neither of them.* **And the claim the table supports survives the correction and is strengthened by it: a channel that reaches 13 is FURTHER from its ν_V of 160 than one that reaches 45.7. The figure is wrong, not the thesis.** *Docket 14's own instruction was to resolve this member first; it is resolved from the book's own collection with no outside data.* Registers 1437. (a correction.)

### 1844

**§24.13 MEASURES BOTH ENDS OF ITS SEQUENCES AND ONLY ONE OF THEM FAILS, AND THE SECTION SAYS SO CORRECTLY TWICE AND INCORRECTLY TWICE ON ONE PAGE.** *Holding each member of two isoelectronic sequences out in turn, §24.13's table gives* **neutral Z = 1 at 11.1% and 23.4%; Z = 2 at 1.4% and 2.4%; Z = 3 at 0.8% and 1.3%; and the other end, Z = 4, at 1.8% and 2.5%.** **The neutral end is 6.2× and 9.4× worse than the upper end, and the upper end sits INSIDE the interior's own worst case on the sodium-like sequence (1.04×) and within a quarter of it on the lithium-like (1.29×).** *The prose under the table is exact —* **"Interpolation works to about one percent. Extrapolation TO THE NEUTRAL does not"** *— and so is Figure 24.3's caption,* **"The interior is recovered to about one percent. THE NEUTRAL is not."** *The summary row and the closing blockquote are not:* **"within a sequence, AT AN END | δ not determined"** *and* **"Interior members need not be fetched. THE ENDS ALWAYS MUST — and the neutral is always an end."** **A sequence has two ends, the table measures both, and the rule that says "an end" and "the ends" generalises from one to both.** *The correct statement and the overstatement sit side by side from the start, neither superseding the other; the two sites that are right are named here so that a repair does not touch them.* Registers 1338. (a correction.)

### 1845

**V = 4ν/3 IS PRINTED WITH AN EQUALS SIGN AT TWENTY-TWO SITES AND AS AN APPROXIMATION AT ONE, AND THE ONE IS RIGHT.** *The string* **4ν/3** *occurs twenty-four times on twenty-two lines of the main volume and once in the Mathematical Compendium — in tables, in summary rows, in the chapter's thesis sentence and in a section title. §23 states the truth once:* **"The exact V is rational at every ν — 32/11, 54/13, 256/47, 250/37, 4000/299 — and 4ν/3 + 4/(9ν) is its ASYMPTOTIC form, low by 0.69% at ν = 2"** *, with the closed form two lines below,* **V = 4ν³/(h(3ν² − h²))**. **All five printed rationals reproduce exactly from that closed form at h = 1, so the object is identified beyond doubt; the two-term asymptotic is low by 0.694% at ν = 2, which is the volume's own 0.69%; and the BARE form is low by 8.33% there — twelve times the error of the form the volume itself calls asymptotic.** *The defect is not that 4ν/3 is wrong. It is that one site states the approximation with its error and twenty-two state an identity, and a reader who meets any of the twenty-two first has no way to know which he has been given.* Registers 1339. (a correction.)

### 1846

**THE SYMBOL σ CARRIES TWO DIFFERENT QUANTITIES IN ONE CHAPTER, AND §22.5's OWN NEXT SENTENCE PROVES IT.** *Rule 4 of §22.2 defines σ as an OUTPUT:* **"Fit δ locally by a Ritz expansion and take σ = 2R Z_eff² · SE_pred / ν³ from the fit's prediction standard error."** *§22.5 uses σ as an INPUT:* **"A channel is admissible when its levels are separated by more than their uncertainty: r = 2Z²R / (ν³σ) ≥ 5. r falls as ν⁻³."** **Substitute the first into the second and the ν³ cancels exactly, leaving r = Z²/(Z_eff² · SE_pred) — a constant in ν.** *So if §22.5's σ were Rule 4's σ, r would not fall as ν⁻³, it would not depend on ν at all, and §22.5's own next sentence —* **"Every channel eventually leaves the domain; the rule states where"** *— would be false.* **The two σ are necessarily different quantities: Rule 4's is the fit's prediction standard error carried into energy, and §22.5's is the levels' own measurement uncertainty, a constant of the channel.** *The chapter corroborates it two lines above Rule 4's own site:* **"This book's tightest bracket is 1.398 cm⁻¹; limit uncertainties in the collection run 0.001 to 0.4 cm⁻¹"** *— measured level uncertainties in cm⁻¹, which is exactly what makes r fall as ν⁻³. No data was needed to decide this; the two formulas decide it between them.* Registers 1340. (a finding.)

### 1847

**"PALINDROMIC IF AND ONLY IF SELF-DUAL" IS FALSE IN ONE DIRECTION, AND THE BOOK'S ARGUMENT USES THE OTHER ONE.** *§11.7's caption to Figure 11.2 and §11.8's opening line both state:* **"A rank polynomial is palindromic if and only if the poset is self-dual."** *Self-dual ⟹ palindromic is true and immediate: an anti-automorphism sends rank r to rank M − r, so the level sizes read the same both ways.* **Palindromic ⟹ self-dual is FALSE, and a six-element counterexample is printed here so it can be checked by hand: elements 0 to 5 with 0 < 1, 0 < 2, 0 < 3, 4 < 1, 5 < 2. Every maximal chain has length one, so it is graded in the strict sense; its level sizes are (3, 3), which is palindromic; and it is not self-dual, because element 0 has three elements above it and nothing in the poset has three below it.** *Found by exhaustive search over strictly graded posets on up to seven elements, the smallest there is.* **And §11.8's conclusion stands, because it uses the claim one way only:** *the rank sequence is asymmetric — 1, 5, 15, 34, 59, 87 forwards against 1, 4, 10, 21, 37, 57 backwards — therefore the poset is not self-dual, which is the CONTRAPOSITIVE of the direction that holds.* **What does not stand is "if and only if", and with it §11.8's "they are the SAME statement": an asymmetric rank sequence IMPLIES non-self-duality and is not equivalent to it. A wording defect, not a result defect.** *Six biconditional claims were censused across Chapters 8 to 11; this is the only one that fails, and it is stated twice.* Registers 1341. (a correction.)

### 1848

**§14.3's BUNDLING CLAIM IS TRUE AND THE EXPERIMENT IT CITES DOES NOT SHOW IT; HERE IS ONE THAT DOES.** *§14.3 argues:* **"What fails is bundling. ℛ reconstructs coordinate by coordinate, so folding two chains into one non-chain coordinate hides structure from it. In tests, the same sets presented bundled and presented decomposed both gave 80/80 AGREEMENT — the theorem survives, but only when the presentation respects it."** **Eighty out of eighty both ways is a report that bundling changed nothing, offered in support of a conclusion that requires a case where it changes something.** *The claim is right and the demonstration is three cells: on the 2 × 2 × 2 box the set {(0,0,0), (0,1,1), (1,0,1)} has* **E = 1 presented as three chain coordinates and E = 0 with two of them folded** *— the cell (0,0,1) that the three-coordinate closure adds is invisible once the fold is made.* **And the reason is general, which is why no search was needed to be sure such a set exists: with TWO coordinates the only pairwise projection is the set itself, so ℛ(X) = X for every X, and any presentation bundled down to two coordinates reports closure whatever it contains.** *Verified on three thousand random sets. So bundling does not hide a defect by accident; at two coordinates it cannot do anything else. The chapter is right about the mechanism and cites the wrong experiment for it.* Registers 1342. (a finding.)"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

new = dict(txt)

r = txt[REG]
for _n in ENTRY_NS:
    assert r.count('### %d\n' % _n) == 0, 'entry %d already seated' % _n
assert r.count('### %d\n' % (ENTRY_NS[0] - 1)) == 1, 'entry %d is not seated' % (ENTRY_NS[0] - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
# Emphasis parity, asserted on each new entry's body before it is seated. Every entry here is
# written as alternating **bold** and *italic* runs; an odd asterisk total means one delimiter is
# short and the emphasis does not close on the page. The first draft of this build seated 1844 and
# 1846 with a `**`-opened quotation closed by a single `*` -- 43 and 39 asterisks -- and joined
# r2-reg7a2's pinned odd-total class of 22, which stopped that instrument (EXPECTED 22, got 24).
# The build was discarded and rebuilt; this assertion is what makes the class unreachable, and
# r2-reg7a2's 22 is untouched.
_bodies = [b for b in ENTRIES.split('\n') if b.startswith('**')]
assert len(_bodies) == len(ENTRY_NS), 'expected one body line per entry, got %d' % len(_bodies)
for _n, _b in zip(ENTRY_NS, _bodies):
    assert _b.count('*') % 2 == 0, 'entry %d: odd asterisk total %d -- an emphasis run does not close' % (_n, _b.count('*'))

new[REG] = r.rstrip('\n') + ENTRIES + '\n'

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
print('register_cites with %s: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %d entries'
      % (str(ENTRY_NS), CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, len(TOP)))
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
          lambda mm_: '%s entries, 1 to %d, at this build (2026-09-07)' % (g(c['headings']), c['highest']), 'main: at this build')
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
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD115 md5 mismatch'
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
print('BUILD115 -> BUILD116: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD116 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
