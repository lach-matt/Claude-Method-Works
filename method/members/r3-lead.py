#!/usr/bin/env python3
"""r3-lead.py — R3: the four retraction-audit rows the volumes themselves witness, executed under RUL-153 Q1 ("a chat
transcript is a lead only"); register 66's object recorded under Q2; entry 1815's and 1816's count classes moved with the
entries. BUILD103 -> BUILD104 main; BUILD213 -> BUILD214 compendia.

THE CLASS. Each site keeps its figure and its sentence and gains a POINTER to the place in the volumes that corrects
or supersedes it — the qualification route of register 1813, the structural edit RUL-153 (chat 153) item 3 permits in
place: "adding or repairing a cross-reference or pointer". No figure, count, verdict or claim changes.

  (i)   the closure rule, one-sided as stated (register 402 states the operator is two-sided) — four sites:
        main Appendix F.4.3 row 1.8 (A.rule); the Mathematical Compendium's tightening rule; the Index of Indices' row
        1.8; Transitions §1.8. Each gains "one-sided as stated; the operator is two-sided (§2.15.2; register 402)".
  (ii)  the withdrawn 2,475 (§12.11.5 recomputed it as 15,150 at Λ₁₂ / 45,450 at Λ₁₃, 21.4 % / 22.8 %) — the four
        residue sites of DEFERRED 13a-01: §2.18.1's "costs the cylinder 2,475 cells", §12.11.3's "2,475 cells of the
        cylinder", Figure 12.4's caption "priced at 3.5%" and §12.11.4's "breaks the factorisation by 3.5%" (the same
        figure as a share of Λ₁₂'s 70,905). Each gains "the figure §12.11.5 withdraws".
  (iii) register 602's 219 minimum covers, a sample of the 24,585 the Mathematical Compendium enumerates exactly, with
        one cell common rather than four — a pointer at the end of 602's body (Ruling 29 as superseded by chat 153
        item 4: pointer addition is a Register edit class), written inside the body's closing italic and without emphasis marks of its own, so that the entry keeps its form and
        r3-em's split-emphasis population (reg7-01/02, held for R3) is not moved by it and at §14.5.12's paragraph (DEFERRED 13j-01's site).
  (iv)  register 66 — not edited. Entry 1817 records M's ruling (the object is the aufbau table) and the
        re-measurement on the observed table.
  The fifth volume-witnessed row of DEF-153P — "the whole tower" against register 1790's own stage table — is read in
  READ-lead.md and left where 1790 leaves it: the caption is owed at the prose pass.

COUNTS. Four entries are appended and three of them are cited from the volumes, so every figure of entries 1815 and 1816
moves — the front matter's total, mature record, kinds table, citation figures and load-bearing table, the main volume's
three "at this build" sentences — and is re-taken here from the seated tools run on the members AS THEY WILL STAND
(register_counts.py via close_main.recount, kinds.py, register_cites.py by runpy in a staging directory holding every
edited member). If the "seven or more" set changes membership this refuses: a new row's text is a hand act.

Usage:  python3 r3-lead.py            dry run
        python3 r3-lead.py --write    writes staging members + BUILD104 main + BUILD214 compendia
"""
import os, sys, re, hashlib, runpy, tempfile, subprocess, io, contextlib, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
TOOLS = os.path.join(REPO, 'tools') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD103_main_and_register.md'); OLD_M_MD5 = 'b4b04ac3fcadc556fe69657a5caa721f'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD104_main_and_register.md')
OLD_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD213_compendia_papers_audits.md'); OLD_C_MD5 = 'd0546bc22484804c42a252edb880305f'
NEW_C = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD214_compendia_papers_audits.md')
OUT = os.path.join(REPO, 'method', 'build104') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'; IOI = 'The_Method_1_6___The_Index_of_Indices-2.md'; TR = 'Transitions.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
g = lambda n: '{:,}'.format(n)
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG, MC, IOI, TR)}
txt = {n: old[n].decode('utf-8') for n in old}
r = txt[REG]
assert r.count('### 1817\n') == 0 and r.rstrip().endswith('Registers 1815. (a correction.)')

ENTRIES = """

### 1817

**REGISTER 66'S OBJECT IS THE AUFBAU TABLE, BY M'S RULING; ON THE OBSERVED TABLE THE OCCUPIED SET IS NOT DOWNWARD CLOSED.** *Asked which object register 66 quantifies over, M ruled (4 September 2026): the aufbau table. The entry stands as written about that object; its "ground-state configuration" is the aufbau one. Run on the observed ground configurations register 1306 seats (LW1-ground.py, NIST ASD 5.12, Z = 1–108) by the consolidation branch's tools/orderideal.py — not a member at this build, register 1813's class; its conventions RECOVERED from registers 11 and 12 and from 66's own wording, its ℓ-ordering permutation RECONSTRUCTED — the occupied set has 98 cells, 197 downward-closure violations, five subshells with an occupancy gap (3d without k = 4 and 9, 4d without 3, 6 and 9, 4f without 2 and 8, 5d without 8, 5f without 1, 5 and 8), six Z-order breaks (Rh→Pd, Ce→Pr, Gd→Tb, Np→Pu, Cm→Bk, Lr→Rf), and 0 of 120 ℓ-orderings admissible against 66's 1 of 120. The four holes the anomalies force — Cr 3d⁵ with nothing at 3d⁴, Cu 3d¹⁰ at 3d⁹, Pd 4d¹⁰ at 4d⁹, Pt 5d⁹ at 5d⁸ — are the corrections 1306 records against the aufbau table. An unbanked re-measurement in conversation (110 cells, 172 violations, 0 of 120) agrees on the property and not on the count; the three counts quantify over three element ranges. Register 66 is not edited; its object is named here.* Registers 11; 12; 66; 1306. (a measurement.)

### 1818

**THE CLOSURE RULE IS PRINTED ONE-SIDED AT FOUR SITES REGISTER 402 CORRECTS, AND EACH NOW POINTS AT THE CORRECTION.** *Register 402: the closure rule was one-sided and the operator is two-sided, the correct characterisation being §2.15.2's. The rule stands as first stated — a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other — at Appendix F.4.3's row 1.8 (A.rule), the Mathematical Compendium's tightening rule, the Index of Indices' row 1.8 and Transitions §1.8, none marked. Under RUL-153 Q1 a transcript is a lead only; the witness here is the Register itself. A pointer added at each of the four — one-sided as stated; the operator is two-sided (§2.15.2; register 402) — the sentence unchanged. The lead was the consolidation branch's retraction audit (PO-0081), verified on the volumes.* Registers 402. (a correction.)

### 1819

**THE WITHDRAWN 2,475 STANDS AT FOUR SITES THE WITHDRAWAL DID NOT REACH, TWICE AS A FIGURE AND TWICE AS 3.5%, AND EACH NOW CARRIES IT.** *§12.11.5 recomputed the cost of the tight two-parent K — 15,150 cells at Λ₁₂ and 45,450 at Λ₁₃, 21.4% and 22.8% of the product — and withdrew the 2,475 previously printed there. §2.18.1 (the tight K has two parents and costs the cylinder 2,475 cells) and §12.11.3 (§A.15 and register 230 record what it costs, 2,475 cells of the cylinder) still print the figure as current, and neither §A.15 nor register 230 prints it; Figure 12.4's caption (the forbidden f···K bridge, priced at 3.5%) and §12.11.4 (breaks the factorisation by 3.5%) print the same cost as a share of Λ₁₂'s 70,905 cells. DEFERRED 13a-01 named the four; READ-ch2-B D2.1 read the first. A pointer at each: the figure §12.11.5 withdraws. The figures are left standing at every site, as the book keeps what it corrects.* Registers 230. (a correction.)

### 1820

**REGISTER 602'S 219 MINIMUM COVERS ARE A SAMPLE OF THE 24,585 ENUMERATED EXACTLY, AND THE ENTRY AND §14.5.12 NOW POINT AT THE EXACT COUNT.** *The Mathematical Compendium (The seed's forced set, corrected): exact enumeration gives 24,585 minimum covers at the Λ₈ cap with exactly one cell common to all of them — corner 3 — and the four-corner universality of the 219-cover sample is refuted. Register 602 (219 distinct minimum covers; the same four cells appear in every one) and §14.5.12 (four cells in 219 of 219 covers) print the sample as the finding, unmarked; DEFERRED 13j-01 records it, and its reading READ-ch13j is archived at ARCHIVE1. A pointer at each, the figures unchanged. §14.5.12's heading, What every minimum seed contains, is false as printed — three of the four cells are in 59%, 28% and 14% of the minimum covers — and is the prose pass's (13j-01), not this entry's.* Registers 602. (a correction.)
"""
def with_entries(t): return t.rstrip() + ENTRIES + '\n'

# ---- (i)–(iii): the pointers, count-asserted -----------------------------------------------------------------------
P402 = ' One-sided as stated; the operator is two-sided (§2.15.2; register 402).'
SUBS = {
 MAIN: [
  ('breaks the tree and admits only an envelope. The tight K has two parents and costs the cylinder\n 2,475 cells. A two-parent',
   'breaks the tree and admits only an envelope. The tight K has two parents and costs the cylinder\n 2,475 cells (the figure §12.11.5 withdraws; register 1819). A two-parent'),
  (' dashed and priced at 3.5%.', ' dashed and priced at 3.5% (the price §12.11.5 withdraws; register 1819).'),
  ('the same bound written with the cell\'s f has two parents and breaks the factorisation by 3.5%.',
   'the same bound written with the cell\'s f has two parents and breaks the factorisation by 3.5% (the figure §12.11.5 withdraws; register 1819).'),
  ('it costs, 2,475 cells of the cylinder. The book substitutes', 'it costs, 2,475 cells of the cylinder (the figure §12.11.5 withdraws; register 1819). The book substitutes'),
  ('| 1.8 | The closure rule. A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other. | `A.rule` |',
   '| 1.8 | The closure rule. A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.' + P402 + ' | `A.rule` |'),
  (' shuffled orders — a harder test — 219 distinct minimum covers were found, and the same four appear\n in every one.** Still nothing is forced',
   ' shuffled orders — a harder test — 219 distinct minimum covers were found, and the same four appear\n in every one.** *(A sample: exact enumeration gives 24,585 minimum covers with one cell common to all — Mathematical Compendium, The seed\'s forced set, corrected; register 1820.)* Still nothing is forced'),
 ],
 REG: [
  ('the gradient measured 13.1 conditioned and **18.2 unconditioned**, min 3, median 12, max 219.*',
   'the gradient measured 13.1 conditioned and **18.2 unconditioned**, min 3, median 12, max 219. Superseded by exact enumeration: 24,585 minimum covers, one cell common to all (Mathematical Compendium, The seed\'s forced set, corrected); register 1820.*'),
 ],
 MC: [
  ('**a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other**\n',
   '**a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other** —' + P402.replace(' One-sided', ' *one-sided').replace('(§2.15.2', '(main §2.15.2').replace('402).', '402).*') + '\n'),
 ],
 IOI: [
  ('| 1.8 | The closure rule. A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other. | **rests on it** — Appendix G |',
   '| 1.8 | The closure rule. A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.' + P402 + ' | **rests on it** — Appendix G |'),
 ],
 TR: [
  ('> **A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.**\n',
   '> **A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.** *One-sided as stated; the operator is two-sided (The Method 1.6 §2.15.2; register 402).*\n'),
 ],
}
new = dict(txt)
for v, subs in SUBS.items():
    for i, (o, n) in enumerate(subs, 1):
        k = new[v].count(o); print('%-44s site %d: anchor occurs %d time(s)' % (v, i, k)); assert k == 1 and o != n; new[v] = new[v].replace(o, n)
new[REG] = with_entries(new[REG])

# ---- the counts, from the seated tools on the members as they will stand ----------------------------------------------
stage = tempfile.mkdtemp(prefix='r3-lead-')
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
print('register_cites with 1817–1820: by entries %d | main %d | main+companions %d | anywhere %d | >=7 %s' % (CITED_BY, CITED_MAIN, CITED_MC, CITED_ANY, TOP))
print('kinds.py: %d %s' % (K_N, K))

# ---- entry 1815's class: front/back matter totals, kinds table, the main volume's "at this build" sentences -----------
rr, edits = cm.recount(new[REG]); assert edits, 'recount made no edit — the counts did not move?'
for o, n in edits: print('recount: %s -> %s' % (o[:50], n[:50]))
c = rc.count(rr); p = rc.printed(rr)
assert (p['front_total'], p['front_highest'], p['front_mature']) == (c['headings'], c['highest'], c['mature']), (p, c)
def sub1(t, pat, repl, label):
    m = re.search(pat, t, re.M); assert m, label + ': anchor absent'
    n = repl(m); assert t.count(m.group(0)) == 1, label + ': anchor not unique'
    print('%-40s %s -> %s' % (label, m.group(0)[:60].replace('\n', ' '), n[:60].replace('\n', ' ')) if n != m.group(0) else '%-40s unchanged' % label)
    return t.replace(m.group(0), n)
for kind in ('a finding', 'a correction', 'a measurement', 'a new protocol', 'a withdrawal', 'prior art', 'an open question', 'a fault of mine'):
    rr = sub1(rr, r'^\| \*\*%s\*\* \| (\d[\d,]*) \| (\d+) \|' % re.escape(kind), lambda m, kind=kind: '| **%s** | %s | %s |' % (kind, g(K[kind]), m.group(2)), 'kinds row ' + kind)
rr = sub1(rr, r'by `kinds\.py` over the (\d[\d,]*) entry headings,', lambda m: 'by `kinds.py` over the %s entry headings,' % g(K_N), 'kinds headings')
# ---- entry 1816's class: the citation figures and the load-bearing table -----------------------------------------------
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited by other entries\.\*\*', lambda m: '**%d entries are cited by other entries.**' % CITED_BY, 'cited by entries')
rr = sub1(rr, r'the (\d+) cited seven times or more:', lambda m: 'the %d cited seven times or more:' % len(TOP), 'the N cited')
rr = sub1(rr, r'\*\*(\d[\d,]*) entries are cited in the main volume\'s chapters and appendices; (\d[\d,]*) counting the four compendia and the two papers; (\d[\d,]*) counting citations by other entries\.\*\*',
          lambda m: '**%d entries are cited in the main volume\'s chapters and appendices; %d counting the four compendia and the two papers; %s counting citations by other entries.**' % (CITED_MAIN, CITED_MC, g(CITED_ANY)), 'cited 3 figures')
rows = re.findall(r'^\| \*\*(\d+)\*\* \| (\d+)× \| (.*) \|$', rr, re.M)
assert sorted(int(e) for e, _, _ in rows) == sorted(n for n, _ in TOP), ('the >=7 set changed membership — a new row is a hand act; REFUSED', rows, TOP)
what = {int(e): w for e, _, w in rows}
i0 = rr.index('| entry | cited | what it established |\n|---|---|---|\n'); i1 = rr.index('\n\n', i0)
rr = rr[:i0] + '| entry | cited | what it established |\n|---|---|---|\n' + ''.join('| **%d** | %d× | %s |\n' % (n, k, what[n]) for n, k in TOP) + rr[i1 + 1:]
print('table: %d rows re-counted, order by count then entry' % len(TOP))
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

# ---- press anchors, line shifts, staging -------------------------------------------------------------------------------
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v in new:
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], txt[v].count(a), new[v].count(a)) for a in anchors if txt[v].count(a) != new[v].count(a)]
    print('build.py SUBS anchors on %-44s %3d checked; moved: %s' % (v, len(anchors), moved)); assert not moved
for v in new: print('%-44s %d -> %d B, lines %+d' % (v, len(old[v]), len(new[v].encode('utf-8')), new[v].count('\n') - txt[v].count('\n')))
if WRITE: assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))

def rebuild(old_path, old_md5, names, label):
    ob = open(old_path, 'rb').read(); assert md5(ob) == old_md5, label + ': old md5 mismatch'
    ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(ob))
    nb = ob
    for n in names:
        assert ms[n] == old[n]; b0 = block(n, ms[n]); assert nb.count(b0) == 1; nb = nb.replace(b0, block(n, new[n].encode('utf-8')))
    rv = nb
    for n in names:
        b1 = block(n, new[n].encode('utf-8')); assert rv.count(b1) == 1; rv = rv.replace(b1, block(n, ms[n]))
    assert md5(rv) == old_md5, label + ' reverse FAILED'
    print('%s: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines %d members' % (label, old_md5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
    return nb
nbm = rebuild(OLD_M, OLD_M_MD5, (MAIN, REG), 'BUILD103 -> BUILD104')
nbc = rebuild(OLD_C, OLD_C_MD5, (MC, IOI, TR), 'BUILD213 -> BUILD214')
if WRITE:
    assert not os.path.exists(NEW_M) and not os.path.exists(NEW_C)
    open(NEW_M, 'wb').write(nbm); open(NEW_C, 'wb').write(nbc); print('written', NEW_M, NEW_C)
else: print('DRY RUN — nothing installed')
