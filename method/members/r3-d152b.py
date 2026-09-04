#!/usr/bin/env python3
"""r3-d152b.py — R3: DEF-152's rulings executed, part two — Appendix G's rows re-taken, and the readout class qualified.
BUILD99 -> BUILD100 main.

  items 2, 3  27a-02 under M's ruling (a), 27a-07 and 27a-08 with it. The Register pointers of rows 8.2, 8.4
              and 10.4c are re-taken by reading under CONVENTION DEP (r2-27a3, READ-27a3): 8 pairs asserted,
              0 kept; 12 written, 0 from a probe. The question M left to R3 — whether the compendium's set
              1019 / 1020 / 1022 / 1035 / 1483 / 1484 becomes row 10.4c's — is ruled NO: none rests on C1's
              factorisation; 1035, 1483 and 1484 rest on §10.4e's dimensional ledger, the row the compendium's
              own block names as its source, and row 10.4e takes them. 1019 and 1020 are NEAR and not written.
              1403 rests on no row, so its citation is dropped: 27a-08 discharged by docket 35's second route.
                                                                                     -> four rows, entry 1812
  item 9      32a-03: every §2.21 build readout carries the docket-38 qualification that its instrument is not
              held. The class is stated once in full at §2.21 and pointed to from the other six sites the sweep
              found — §32.1's two, §32.1.4's table, §32.1.4.1, §32.6.1 and §D.5's census. The seventh readout,
              the register's span, is printed only in the Register's front matter, which Ruling A holds
              untouched; it waits with reg1-04 and the entry says so.      -> seven sites, entry 1813

Line shift: main +5 (§2.21 +3, §32.6.1 +1, §D.5 +1), reported not hidden. Register +8 (two entries).
Ruling A holds: the Register's front-matter counts are untouched.

Usage:  python3 r3-d152b.py            dry run
        python3 r3-d152b.py --write    writes staging members + the BUILD100 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD99_main_and_register.md')
OLD_MD5 = '196acc456adad97fd3bb8cbfe91fc3bf'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD100_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build100') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')

SUBS = [
 # Appendix G, the third column of four rows — exactly as r2-27a3 §7 prints them
 ('| `W.jur`; Chapter 12; Register 1375, 1519, 1523, 1535, 1551 |\n', '| `W.jur`; Chapter 12; Register 543, 584, 585, 588, 592 |\n'),
 ('| `W.rel`; Chapter 12; Register 1375 |\n', '| `W.rel`; Chapter 12; Register 543, 544 |\n'),
 ('| `M.C1`; Register 1399, 1403 |\n', '| `M.C1`; Register 549, 550 |\n'),
 ('| `M.ledger` |\n', '| `M.ledger`; Register 1035, 1483, 1484 |\n'),
 # the readout class — §2.21 states it
 (' every build. **These are readouts and are marked as such** — a number the artefact computes about\n'
  ' itself is evidence of a state, not a claim about the work.\n',
  ' every build. **These are readouts and are marked as such** — a number the artefact computes about\n'
  ' itself is evidence of a state, not a claim about the work. And a readout is checkable only while its\n'
  ' instrument is held: the scripts that compute these — numbers-index.py and its companions — are not\n'
  ' members of this build, so each stands as a record-carried figure, true of the state it names and not\n'
  ' recomputable from the artefact as delivered (register 1813).\n'),
 # §32.1, two sites
 ('the unfibred value being a build readout per §2.21. Only E(Λ) = 0 is computed unfibred',
  'the unfibred value being a build readout per §2.21, by an instrument this build does not hold (register 1813). Only E(Λ) = 0 is computed unfibred'),
 ('E(Q) unfibred as the press reports it at each build,\n', 'E(Q) unfibred as the press reports it at each build (instrument not held, register 1813),\n'),
 # §32.1.4's table
 ('                                                       **a build readout**\n',
  '                                                       **a build readout; instrument not held (register 1813)**\n'),
 # §32.1.4.1
 (' state, and the state is named. The press recomputes the two that move fastest at every build. **Three\n'
  ' more are asserted here and should not be**, which is the work register 373 leaves open rather than\n'
  ' does.\n',
  ' state, and the state is named. The press recomputes the two that move fastest at every build, by\n'
  ' instruments this build does not hold (register 1813). **Three more are asserted here and should not\n'
  ' be**, which is the work register 373 leaves open rather than does.\n'),
 # §32.6.1
 (' answer rather than an opinion. At the build that produced this page the press prints\n **E(Λ) = 0, E(audits) = 16',
  ' answer rather than an opinion. At the build that produced this page the press printed, by\n instruments this build does not hold (register 1813),\n **E(Λ) = 0, E(audits) = 16'),
 # §D.5's census
 ('    press at every build, per §2.21. No combination of status, verification and\n',
  '    press at every build, per §2.21, by an instrument this build does not hold (register 1813). No\n'
  '    combination of status, verification and\n'),
]
for i, (o, n) in enumerate(SUBS, 1):
    c = m.count(o); print('site %2d: anchor occurs %d time(s)' % (i, c)); assert c == 1
    m = m.replace(o, n)

ENTRIES = """

### 1812

**APPENDIX G's THREE ROWS NAMED ENTRIES THAT REST ON OTHER MECHANISMS; RE-TAKEN BY READING, THEY NAME NINE THAT REST ON THEIRS, AND THE COMPENDIUM's SIX GO TO THE ROW THE COMPENDIUM NAMES.** *M's ruling on 27a-02 was (a): the column 'what rests on it' names entries that rest on the section, and the Register pointers of rows 8.2, 8.4 and 10.4c are re-taken by reading under CONVENTION DEP — an entry rests on a section if it names the source at that section or if its own deciding sentence is an instance or consequence of the mechanism the section establishes, the phrase asserted present in the entry's text before any verdict, and nothing written from a token probe. The DEP-N sweep is exhaustive over the Register; DEP-M is read on the candidates and claimed no further.* **Of the eight pairs the column asserted, none rests on its section (register 1770's rows; r2-27a reproduced). Row 8.2 rests on 543, 584, 585, 588 and 592, each naming T §8.2 and turning on what it prints — the disjunction NEC ≥ 3 → (IC ∨ U ∨ X) and the conjunctive body; row 8.4 on 543 and 544; row 10.4c on 549 and 550, which close and read M.C1 at the section.** *The question the ruling left to R3 — whether the Mathematical Compendium's modular-ledger set, 1019, 1020, 1022, 1035, 1483 and 1484, becomes row 10.4c's — is answered NO: none has a deciding sentence that is an instance of C1's factorisation over generators. Three of them — 1035, 1483, 1484 — have the dimensional ledger d − 1 = 1 + (d − 2) as their deciding sentence, read, qualified and completed, and that is §10.4e's, the row the compendium's block itself names as its source; row 10.4e takes the three, and 27a-07's disagreement between the address and the compendium resolves in the compendium's favour for exactly the entries that carry the phrase. 1019 and 1020 are NEAR and are not written; 1022 is §10.4d's.* **1403 rests on no row, so its citation is dropped, and 27a-08 — the WARNING the row did not restate — is discharged by the drop, which is the second of docket 35's two routes.** *Pointer arithmetic: eight pairs asserted, none kept; twelve written, none from a probe. What the reading cannot bound is DEP-M over entries that instance a mechanism without naming the paper; NEAR is that class, and the rows say what rests on them over what was read.* Registers 543; 544; 549; 550; 584; 585; 588; 592; 1035; 1483; 1484; 1770. (a correction.)

### 1813

**SEVEN FIGURES THE BOOK PRINTS AS BUILD READOUTS ARE FIGURES NO MEMBER OF THIS BUILD CAN RECOMPUTE, AND EVERY SITE NOW SAYS SO.** *§2.21 makes computation at build the third representation of a figure about the book — E(G), the open item count, E(Q) unfibred, the register's span, the withdrawal ratio, and by register 375 Appendix D's element count and §32.1.4's total — and marks them readouts. Measured (r2-32a §7): numbers-index.py, densities.py, indices.py, appendix_audit.py, mathreg.py, compendium.py, register_gen.py and guard.py are not members of this build, register 435 records the first two as having been absent and rebuilt from the printed rules, and build.py, which is a member, is a prose-substitution press that computes none of them and whose substitution table strips the script names out of reader-facing prose.* **A build readout is not a checkable figure while its instrument is not held. This is not a defect in any of the seven; it is their standing, and it is docket 38's class — the record-carried figure — entered whole.** *DEF-152 item 9 offered two routes, the scripts becoming members or every readout carrying the qualification; the scripts in the store are the restore-point's, stale against the volumes by hundreds of lines, and seating a generator that does not reproduce what it generated would be a second record-carried figure. The qualification is taken: stated once in full at §2.21 and pointed to from the six other sites — §32.1's two, §32.1.4's table, §32.1.4.1, §32.6.1 and §D.5's census. The seventh readout, the register's span, is printed only in this Register's front matter, which Ruling A holds untouched until the readings; it waits with the count repair and is qualified here rather than there.* Registers 374; 375; 435; 1807. (a measurement.)"""

for n in (1812, 1813): assert r.count('### %d\n' % n) == 0, n
assert r.rstrip().endswith('(a correction.)')
r = r.rstrip() + ENTRIES + '\n'

for probe, want in (('Register 1375', 0), ('Register 1399, 1403', 0), ('(register 1813)', 6), ('register 1813)', 7),
                    ('| `M.ledger`; Register 1035, 1483, 1484 |', 1), ('Register 543, 584, 585, 588, 592', 1)):
    got = m.count(probe); print('  main after: %-52s %d (want %d)' % (repr(probe), got, want)); assert got == want
assert r.count('\n### 1812\n') == 1 and r.count('\n### 1813\n') == 1

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
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD99 md5 mismatch'
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
print('new BUILD100  %s B  md5 %s  %s lines  %d members' % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE); open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else:
    print('DRY RUN — nothing installed')
