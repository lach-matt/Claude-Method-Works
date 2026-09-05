#!/usr/bin/env python3
# r2-reg8a2.py — SUCCESSOR of r2-reg8a.py (predecessor md5 80b7def8bef9f863848c8afac0fa693f), class DEF-153N
# (the positional class: a literal line read whose content moved), W-234. The Register's front matter grew by two
# lines at BUILD110 (two rows added to the load-bearing table at L50-L51), so the predecessor's fixed window
# RL[:74] no longer covers the front matter (now 79 lines) and its reg8-B list dropped the "411 entries are cited"
# line at L75. Replacements made, and nothing else changed (no print, order or wording):
#   1. line 79 of the predecessor, `fm = '\n'.join(RL[:74])` -> the front matter keyed on content: every line before
#      the first entry heading (the first line matching ^### \d), `RL[:FM_END]`.
# The members directory was already resolved from the script's own location (H = dirname(abspath(__file__))) and
# is kept; the archive path (ARCH) is kept as the predecessor had it. Every other Register/archive read in the
# predecessor is already content-keyed (AL[apos[n] + 1], RL[pos[h] + 1] index by entry heading).
# Rule G0c: this successor reproduces the predecessor's banked golden byte-exact on the pre-shift (BUILD109) members.
# r2-reg8a.py — the Register read, unit 8: THE WITHDRAWN ENTRIES, taken at M's direction after the
# front matter was found to cite four entries that do not exist (reg1-05).
#
# WHAT WAS OWED. reg1-05 recorded that registers 1725, 1732, 1744 and 1756 -- the front matter's own
# provenance citations -- have no heading in the seated Register, and inferred nothing about why.
# This unit replaces that silence with a measurement, against the archive rather than against a
# reconstruction: the mirrored BUILD9 and BUILD10 main bundles are earlier states of this same
# volume, and they are read here as the witness Ruling 56 makes them.
#
# THE ANSWER IS NOT "NEVER WRITTEN". All four were written, seated, and later removed with their
# content. Entry 1782 discloses the practice in aggregate -- "132 are absent -- the thirteen never
# assigned, together with those withdrawn with their content" -- and names none of them.
#
# WHAT IS SCORED AND WHAT IS NOT. The WITHDRAWAL is not scored: Ruling 45 forbids build and
# editorial-process remarks in a reader-facing volume, and every entry examined here is exactly that,
# so removing them is consistent with a ruling in force. What IS scored is that the front matter
# still cites them, and that the diagnosis one of them carried was removed while the defect it
# diagnosed was not repaired.
# Deterministic: no wall clock, no randomness.
import os, re

H = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(os.path.dirname(os.path.dirname(H)), 'drive', 'The Method Materials',
                    'The_Method_1_6_BUILD10_main_and_register.md')
if not os.path.exists(ARCH):
    ARCH = '/home/user/Claude-Method-Works/drive/The Method Materials/The_Method_1_6_BUILD10_main_and_register.md'
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read()
def hr(t): print('\n== ' + t)
R = rd('The_Method_1_6___The_Register-2.md'); RL = R.split('\n')
A = open(ARCH, encoding='utf-8', errors='replace').read(); AL = A.split('\n')
FAIL = []; DEV = []
def check(tag, got, exp):
    ok = got == exp
    print('   %-56s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def note(t, tag, got):
    DEV.append((t, tag, got)); print('   %-56s %-26s FINDING (%s)' % (tag, repr(got)[:26], t))

live = {int(x) for h in re.findall(r'^### ([\d, ]+)$', R, re.M) for x in h.split(',')}
apos = {}
for i, l in enumerate(AL, 1):
    m = re.match(r'^### (\d+)$', l)
    if m: apos.setdefault(int(m.group(1)), i)

hr('0  THE WITNESS')
print('   archive: BUILD10 main_and_register, %d B' % len(A.encode()))
check('the archive holds a register', len(apos) > 1000, True)
print('   BUILD10 register: %d numbers, %d..%d' % (len(apos), min(apos), max(apos)))
print('   live    register: %d numbers, %d..%d' % (len(live), min(live), max(live)))

hr('1  THE FOUR PROVENANCE POINTERS WERE WRITTEN, SEATED, AND REMOVED')
for n in (1725, 1732, 1744, 1756, 1710, 1743):
    inA, inL = n in apos, n in live
    head = re.sub(r'\s+', ' ', AL[apos[n] + 1])[:96] if inA else ''
    print('   %-5d archive %-5s live %-5s  %s' % (n, inA, inL, head))
check('all four front-matter pointers exist in the archive',
      all(n in apos for n in (1725, 1732, 1744, 1756)), True)
check('and none survives in the live register',
      any(n in live for n in (1725, 1732, 1744, 1756)), False)

hr('2  IT IS A REMOVAL, NOT A RENUMBERING')
key = 'NORMALISED TO ITS OWN SETTLED FORM'
print('   entry 1725\'s headline: "%s"' % key)
vols = ['The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md',
        'The_Method_1_6___Mathematical_Compendium-2.md', 'The_Method_1_6___The_Physics_Compendium-2.md',
        'The_Method_1_6___Spectra_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md']
hits = [v for v in vols if key in rd(v)]
check('that content appears in any live volume, under any number', hits, [])
print('   So it was not moved. It was withdrawn with its content, which is what entry 1782 says')
print('   happened to an unnamed subset of the 132 absent numbers.')

hr('3  THE SCALE')
lost = sorted(n for n in apos if n not in live)
note('reg8-A', 'entries in the archive and not in the live register', len(lost))
print('   %s' % lost)

hr('4  WHAT THE FRONT MATTER STILL POINTS AT')
FM_END = next(i for i, l in enumerate(RL) if re.match(r'^### \d', l))  # DEF-153N: the front matter is every line before the first entry heading (was RL[:74])
fm = '\n'.join(RL[:FM_END])
cited = [n for n in lost if re.search(r'\b%d\b' % n, fm)]
print('   numbers from the withdrawn set appearing in the front matter: %s' % cited)
print('   571 is the load-bearing COUNT ("571 entries are cited by other entries"), not a pointer,')
print('   and is excluded. The remaining four are citations, and all four are provenance:')
note('reg8-B', 'front-matter provenance pointers that were withdrawn', [n for n in cited if n != 571])
print('     1725  the settled form, the ruling-C normalisation')
print('     1732  the citation counts recomputed and the load-bearing table regenerated')
print('     1744  the asterisk residues -- "THE REGISTER\'S TANGLES WERE SPLIT DELIMITERS"')
print('     1756  the carried residue computed out')
body_cites = [n for n in lost if re.search(r'(?i)registers?\s+%d\b' % n, R)]
check('any OTHER part of the live register cites a withdrawn entry', body_cites, [])
print('   The front matter is the only place in the volume that points at a withdrawn entry.')

hr('5  THE DIAGNOSIS THAT WAS REMOVED WHILE THE DEFECT STAYED')
print('   archive 1744: %s' % re.sub(r'\s+', ' ', AL[apos[1744] + 1])[:290])
print('   archive 1743: %s' % re.sub(r'\s+', ' ', AL[apos[1743] + 1])[:150])
check('1743, the count 1744 rests on, is also withdrawn', 1743 in live, False)
SPLIT = re.compile(r'(?<![*\s])\* \*(?!\*)')
pos = {}
for i, l in enumerate(RL, 1):
    m = re.match(r'^### ([\d, ]+)$', l)
    if m: pos.setdefault(m.group(1), i)
still = [h for h in pos if SPLIT.search(RL[pos[h] + 1])]
note('reg8-C', 'entries still carrying the split delimiters 1744 named', len(still))
print('   The register diagnosed this class itself, counted it, and the entries carrying the')
print('   diagnosis were withdrawn. reg7-01 rediscovered it independently at %d entries / %d sites.'
      % (len(still), sum(len(SPLIT.findall(RL[pos[h] + 1])) for h in still)))

hr('6  WHY THE WITHDRAWAL ITSELF IS NOT SCORED')
print('   Ruling 45 forbids build and editorial-process remarks in any reader-facing volume, and')
print('   every entry examined here is exactly that -- 1743 names build.py and the press pipeline,')
print('   1732 the citation parser, 1725 the generator\'s retirement. Removing them from a')
print('   reader-facing volume is consistent with a ruling in force, so the removal is NOT a')
print('   finding. What is a finding is that the citations to them were left standing, and that')
print('   the front matter which cites them still carries the script names and build handles')
print('   Ruling 46 forbids (reg1-06). The cleanup took the entries and left both loose ends.')

hr('SUMMARY')
print('   instrument checks failed : %d %s' % (len(FAIL), FAIL if FAIL else ''))
print('   findings recorded        : %d' % len(DEV))
for t, tag, got in DEV: print('     %-9s %-52s %s' % (t, tag, repr(got)[:40]))
print('\n   ALL INSTRUMENT CHECKS OK' if not FAIL else '\n   INSTRUMENT FAULT - STOP')
