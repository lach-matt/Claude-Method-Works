#!/usr/bin/env python3
"""r3-d152.py — R3: DEF-152's rulings executed, part one — the entries owed and the three sentences ruled.
BUILD98 -> BUILD99 main.

M's four rulings at chat 152 (RULING-DOCKET-152) and what DEF-152 carried as owed. Executed here:
  item 1  26c-02, ruling (c): the origin of each of §32.1.4's three totals, measured by r2-32a (chat 152,
          re-run on this build) — a new entry citing 332, 373 and 375 together.                 -> entry 1807
  item 8  32a-04: register 332's collapsed sentence — a new entry citing 332 states the loss.   -> entry 1808
  item 4  28a-06, ruling (a): *Fifty-nine* re-taken on the 162 rows it is printed beside: 52,
          with a new entry citing 1736, which is not withdrawn. The one question the ruling left
          open — whether the 172-row figure is kept beside the new one — is answered by 1736's own
          precedent, "the prior count kept beside it": yes.                                      -> entry 1809, main site
  item 5  28a-08: the entry does not cite the earlier instrument's 16.                           -> (by omission)
  item 6  28b-07, ruling (b): R.7's two lead-ins stop saying the chapters rest on the blocks;
          Montgomery's sentence stands.                                                          -> entry 1810, two main sites
  item 7  28b-08: the record's list of block names living only in 1721 corrected to twelve.      -> entry 1811
Deferred to part two (r3-d152b, after r2-27a3's reading): items 2, 3 (Appendix G rows) and 9 (docket 38).
Item 10 (census 293 and 387–672) is r2-bib's and closes at the compendia bundle.

MEASURED on this build before writing: r2-32a exits 0 with one deviation (32a-01); r2-28a3 prints 52 / 55 /
55 / 57 / 58 / 70 of 162; r2-28b2 prints 1721's ten owner-groups and L11839's four names.

THREE MAIN SITES, all in §R.7 / the closing paragraph of References:
  A  the Löwdin lead-in: "these are the works Chapter 35 rests on" -> "these are the works entered with Chapter 35"
  B  "Fifty-nine of them are the works listed above" -> "Fifty-two of them are the works listed above (fifty-nine
     of the 172 rows matched at register 1736, before ten rows were removed; register 1809)"
  C  "§R.7's two blocks are the works the chapters rest on" -> "the works entered with the chapters at registers
     1701–1712 and 1713–1724"
Line shift: main +2 (sites B and C each grow a line), reported not hidden. Register +20 (five entries).
Ruling A holds: the Register's front-matter counts are untouched.

Usage:  python3 r3-d152.py            dry run
        python3 r3-d152.py --write    writes staging members + the BUILD99 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD98_main_and_register.md')
OLD_MD5 = 'bf50a6c19e6f76b1f922b4552971274d'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD99_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build99') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')

SUBS = [
 # A. the Löwdin lead-in
 (' **The Löwdin solution.** Entered at registers 1701–1712. The companion paper carries the full list; these are the works Chapter 35 rests on.\n',
  ' **The Löwdin solution.** Entered at registers 1701–1712. The companion paper carries the full list; these are the works entered with Chapter 35 (register 1810).\n'),
 # B. fifty-nine -> fifty-two, the 172-row figure kept beside it
 (' objects — 162 works, 1669 to 2026, ordered by year with the objects each carries. Fifty-nine of them\n'
  ' are the works listed above; the remainder are the attributions of standard results — Newton 1669,\n',
  ' objects — 162 works, 1669 to 2026, ordered by year with the objects each carries. Fifty-two of them\n'
  ' are the works listed above (fifty-nine of the 172 rows matched at register 1736, before ten rows were\n'
  ' removed; register 1809); the remainder are the attributions of standard results — Newton 1669,\n'),
 # C. the closing sentence
 (' not repeated here (register 1736). The two companion papers carry their own reference lists; §R.7\'s\n'
  ' two blocks are the works the chapters rest on, not those lists.\n',
  ' not repeated here (register 1736). The two companion papers carry their own reference lists; §R.7\'s\n'
  ' two blocks are the works entered with the chapters at registers 1701–1712 and 1713–1724, not those\n'
  ' lists (register 1810).\n'),
]
for i, (o, n) in enumerate(SUBS, 1):
    c = m.count(o); print('site %d: anchor occurs %d time(s)' % (i, c)); assert c == 1
    m = m.replace(o, n)

ENTRIES = """

### 1807

**§32.1.4's THREE TOTALS HAVE THREE ORIGINS, AND THE ENTRY THAT CARRIES THE 47 IS THE ONE THE SECTION ALREADY CITES.** *M's ruling on 26c-02 was (c): find where each total came from before choosing between the section and register 375. Measured (r2-32a, chat 152; re-run on this build). The fifty-five at §32.1.4 is the section's own table, 4 + 1 + 33 + 17, and it is the ONLY total of the three that one assignment of printed values reaches. The 48 of §32.1.4.1 and register 373 is 4 + 4 + 23 + 17 — two components moved, two carried at their §32.1.4 values and not restated — and three printed assignments reach it. The 47 enters the record at REGISTER 332, the entry §32.1.4 cites on a pointer that wraps a line break: a readout the press prints at every build, 47 at the time of writing, having been 55. Register 375 restates it and does not originate it.* **So the record's sequence is 55, 47, 48, 47, and it is not monotone: the total stood at 47 before it stood at 48.** *Two printed assignments reach 47, and the only one that agrees with the shape sentence 332 and 375 both assert — D 4, Q 5, numbers 21, audits 17 — mixes two states of the book: the numbers index at 21 is §32.1.4.1's before-compression column and E(Q) at 5 is §32.6.1's readout after it. A readout is reproducible only if its inputs are printed at one state, and these are not.* **Neither §32.1.4 nor 375 is corrected, since neither was ruled: 375's 'no longer written as a number' remains false as printed — the section still writes the total as a word — and is recorded here, not repaired.** *The shape sentence has two sites, 332 and 375, and §32.1.4 carries neither; 26c-02's 'appears in no volume' scored the volume where the finding meant the section. And the total's instrument is not held: numbers-index.py computes the largest component, register 435 records it absent and rebuilt from the printed rules, and it is not a member of this build — docket 38, not docket 12.* Registers 332; 373; 375; 435. (a correction.)

### 1808

**REGISTER 332 LOST A SENTENCE BETWEEN *INDICES* AND *SINCE*, AND THE FIGURE IT WOULD HAVE CARRIED IS HELD NOWHERE.** *Read entire, 332's body runs 'Across its six indicessince been confirmed by occupants arriving' — two sentences collapsed, with the text between them lost at exactly the point where the entry would state how many of the named cells have since been filled. That is the figure §32.1.4's 'confirmed three times' paragraph rests on, and the three it names — registers 285, 294 and 278 — are the nearest printed datum and not the lost sentence. The figure appears in no volume and not in Prints & Proofs.* **This entry states the loss and does not fill it: a number the record does not print may not be supplied to close a sentence, any more than an arithmetic.** *332 is not edited.* Registers 332; 1807. (a correction.)

### 1809

**FIFTY-NINE WAS A 172-ROW DATUM PRINTED BESIDE A 162-ROW COUNT; RE-TAKEN ON THE LIST IT SITS BESIDE, IT IS FIFTY-TWO.** *M's ruling on 28a-06 was (a): the figure is re-taken on the list it is printed beside. Under CONVENTION AY — the works listed above are the References from their heading to the line before the claim, matched by surname paired with the row's own year — the 162 rows of the Mathematical Compendium's bibliography share 52 works with the References. The figure is bracketed: 52 exact, 55 at a year tolerance of ±1 and ±2, 57 at ±3, 58 at ±5, and 70 with the year dropped. No author-and-year reading of the 162 rows reaches fifty-nine.* **Register 1736 is not withdrawn, and what it remains right about is stated in its own terms: its fifty-nine was matched by author and year against '172 works, 1669–2026', before the ten rows it removed, and it kept the prior count beside the new one.** *§R.7 now does the same for this pair — fifty-two on the 162 rows, with the fifty-nine of the 172 named beside it as 1736's — which is the one question the ruling left to R3, answered by 1736's own precedent.* Registers 1736. (a correction.)

### 1810

**§R.7's TWO LEAD-INS SAID THE CHAPTERS REST ON THE BLOCKS; THEY NOW SAY WHAT IS TRUE AS PRINTED.** *M's ruling on 28b-07 was (b). Under CONVENTION PROV the sentence on Montgomery's line — every structural object of Chapter 36 is his or older — is TRUE over the ten works Chapter 36 names, the newest of them 2015 and Montgomery's own, and it stands as written. What over-reached was the container: 'these are the works Chapter 35 rests on' and '§R.7's two blocks are the works the chapters rest on' asserted a dependence six three-body works and Madelung do not satisfy, the six appearing in no part of Chapter 36 and Madelung in neither Chapter 35 nor registers 1701–1712.* **Both lead-ins are re-worded to the works entered with the chapters at registers 1701–1712 and 1713–1724, which is what the block records and asserts no dependence.** *Carried deliberately: the six post-2015 works and Madelung stay in the blocks, and the scope question does not recur, because the block no longer claims what they were failing to satisfy.* Registers 1701–1724. (a correction.)

### 1811

**THE BLOCK NAMES LIVING ONLY IN REGISTER 1721 NUMBER TWELVE, NOT EIGHT.** *The record listed eight three-body works whose only home in registers 1713–1724 is entry 1721 — Marchal, Bozis, Monaghan, Stone, Leigh, Kol, Moser, Alekseev. Measured across the run, the list is a subset: Baker, Dechter, Montanari and Pixley — the block's constraint-consistency line — sit in 1721's tenth owner-group, in no other entry of 1713–1724, and in no part of Chapter 36. Twelve in all.* **Under ruling (b) the record's list is corrected by this entry and the block is not narrowed to fit it.** *Engaged and not scored: 1721 prints ten owner-groups against its stated seven closures. A question may close to more than one owner, and the audit-7 ledger that maps question to owner is not a member of this build, so the reading cannot decide it; §36.2's eight closed and §36.3's seven belonged to others reconcile, the eighth being the withdrawn degree-8 polynomial given to Lagrange's resolvent at register 1720.* Registers 1719; 1720; 1721; 1810. (a correction.)"""

for n in range(1807, 1812): assert r.count('### %d\n' % n) == 0, n
assert r.rstrip().endswith('(a correction.)')
r = r.rstrip() + ENTRIES + '\n'

for probe, want in (('Fifty-nine of them', 0), ('works Chapter 35 rests on', 0), ('works the chapters rest on', 0),
                    ('Fifty-two of them', 1), ('entered with the chapters at registers 1701–1712 and 1713–1724', 1)):
    got = m.count(probe); print('  main after: %-64s %d (want %d)' % (repr(probe), got, want)); assert got == want
for n in range(1807, 1812): assert r.count('\n### %d\n' % n) == 1

new_m = m.encode('utf-8'); new_r = r.encode('utf-8')
print('main %d -> %d B, lines %+d' % (len(old_main), len(new_m), m.count('\n') - old_main.decode('utf-8').count('\n')))
print('reg  %d -> %d B, lines %+d' % (len(old_reg), len(new_r), r.count('\n') - old_reg.decode('utf-8').count('\n')))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, old_main.decode('utf-8'), m), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved)); assert not moved

if WRITE:
    assert not os.path.exists(OUT); os.makedirs(OUT)
elif not os.path.isdir(OUT):
    os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD98 md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(old_b))
assert ms[MAIN] == old_main and ms[REG] == old_reg
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
nb = old_b
for n_, body in ((MAIN, new_m), (REG, new_r)):
    ob = block(n_, ms[n_]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n_, body))
rv = nb
for n_, body in ((MAIN, new_m), (REG, new_r)):
    assert rv.count(block(n_, body)) == 1; rv = rv.replace(block(n_, body), block(n_, ms[n_]))
assert md5(rv) == OLD_MD5, 'bundle reverse FAILED'
print('bundle reverse recovers md5 %s == old: True' % md5(rv))
print('new BUILD99  %s B  md5 %s  %s lines  %d members' % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE); open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else:
    print('DRY RUN — nothing installed')
