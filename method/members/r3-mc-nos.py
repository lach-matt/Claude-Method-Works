#!/usr/bin/env python3
"""r3-mc-nos.py — R3: the necessity of state, restated in the Mathematical Compendium.
BUILD199 -> BUILD200 compendia.

M's ruling, this session: the LAW goes to the Physics Compendium and the THEOREM to the
Mathematical Compendium, "even though it is no longer mentioned here — we still identified it in
getting to this point". This member does the second half. The Physics Compendium is NOT touched:
it is generated end to end and a new entry's "N objects rest on it" is computed at build time from
the MC dependency graph under register 1740's rule, so it waits on `mathreg.py`.

WHY THIS REGION MAY BE EDITED AT ALL. Register 1503: the compendium's Löwdin tail was authored by
hand and appended by `compendium.py`, and every rebuild silently discarded 6,659 characters of it
until it was moved to `COMPENDIUM-TAIL.md`. So this section is hand-authored BY DESIGN. The debt
that carries: the same text must reach COMPENDIUM-TAIL.md upstream, or the next regeneration drops
it. Recorded, not resolved here — `mathreg.py`, `compendium.py` and `COMPENDIUM-TAIL.md` are in
neither the store, the Drive mirror, the CORPUS tree, the chat149 archive nor the bundles' 476
embedded FILE blocks.

TWO SITES, both carrying the same defects §34.6 carries:

  1. "## The necessity of state"  — the object paragraph states "104 of 106 steps admit two to
     four", which reproduces under NO convention (register 1448: the count is fixed from the case
     it judges; docket 37). Measured on the corpus's own instrument the range is two to six and no
     step admits fewer than two. And the "This work" paragraph claims the periodic table is not
     computable from a single atom's configuration — contradicted by the compendium's own record
     that Madelung's memoryless rule scores 96 of 106 with no parameter (register 1445).
     A THEOREM paragraph is added between them, which is the half M ruled belongs here.

  2. the row in "What this work introduces, in one list" — same figure, same repair.

WHAT IS NOT CLAIMED. The theorem is about the ν-family, not about all rules; a lookup table is a
memoryless function of one configuration, so the unrestricted sentence is false as quantified and
is removed rather than rescoped. The corridor's non-emptiness is left exactly where register 1460
put it: a statement about the FORM, and non-emptiness confirms nothing.

Usage:  python3 r3-mc-nos.py            dry run
        python3 r3-mc-nos.py --write    writes staging members + the BUILD200 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD199_compendia_papers_audits.md')
OLD_MD5 = 'b480d217d5695c3f3898bc57cde00126'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD200_compendia_papers_audits.md')
OUT = os.path.join(REPO, 'method', 'build200') + os.sep
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_mc = open(MEM + MC, 'rb').read()
t = old_mc.decode('utf-8')

# ---------------------------------------------------------------- site 1: the section
OLD1 = """**The object.** For each admissible subshell, set a to that subshell's own crossing
value and ask whether it is then least-ν. **104 of 106 steps admit two to four
self-consistent subshells** — the observed one is always among them, never uniquely
determined.

**This work.** *That the periodic table is not computable from a single atom's
configuration. It requires one number carried forward: the arithmetic supplies the
values, the walk supplies the selection.*"""

NEW1 = """**The object.** For each admissible subshell, ask whether some value of `a` makes it
least-ν against its Pauli-admissible rivals. **Every step admits more than one — two to
six across the table, and one never** — the observed one always among them, never
uniquely determined.

**The theorem.** *In the plane where each admissible subshell is the point (√r, n),
ν = n − a√r takes whichever point a line of slope `a` reaches first, so only vertices of
the lower convex hull are ever taken. A point set carrying two distinct node counts has
at least two such vertices, and the unfilled set carries two below 124 electrons — every
neutral atom there is. Proved, and it needs no observation: the ambiguity is a fact about
point sets, not about atoms.*

**This work.** *One number is carried so the form stays exact. No single `a` lies in all
106 corridors and the running intersection empties eleven times; three values suffice for
the whole table and three are forced, boron, lanthanum and lawrencium having pairwise
disjoint corridors (register 1580). What is not geometry is that the observed subshell is
among the admissible ones at all 106 steps — that is the corridor, and it is what survives
the form's demotion (registers 1445, 1460, 1463).*"""

# ---------------------------------------------------------------- site 2: the list row
OLD2 = "| **the necessity of state** | 104 of 106 steps ambiguous without memory |"
NEW2 = ("| **the necessity of state** | no step admits fewer than two; the theorem is geometry, "
        "the corridor is the physics |")

for i, (o, n) in enumerate(((OLD1, NEW1), (OLD2, NEW2)), 1):
    c = t.count(o)
    print('site %d: anchor occurs %d time(s)' % (i, c))
    assert c == 1, 'site %d anchor is not unique' % i
    t = t.replace(o, n)

# the two defects must be gone from this member, and nothing else may carry them in
for probe, want in (('104 of 106', 0), ('not computable from a single', 0),
                    ('The theorem.', 1), ('two to\nsix across the table', 1)):
    got = t.count(probe)
    print('  after: %-32s %d (want %d)' % (repr(probe), got, want))
    assert got == want, 'post-condition failed on %r' % probe

new_mc = t.encode('utf-8')
d = t.count('\n') - old_mc.decode('utf-8').count('\n')
print('member %s: %d B -> %d B, lines %+d' % (MC, len(old_mc), len(new_mc), d))

# ---------------------------------------------------------------- press anchors
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
anchors = [a for a, b in ns['SUBS'].get(MC, [])]
moved = [(a[:44], old_mc.decode('utf-8').count(a), t.count(a))
         for a in anchors if old_mc.decode('utf-8').count(a) != t.count(a)]
print('build.py SUBS anchors on %s: %d checked; changed by this edit: %s' % (MC, len(anchors), moved))
assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- the bundle
if WRITE:
    assert not os.path.exists(OUT), '%s exists' % OUT
    os.makedirs(OUT)
elif not os.path.isdir(OUT):
    os.makedirs(OUT)
open(OUT + MC, 'wb').write(new_mc)
old_b = open(OLD_BUNDLE, 'rb').read()
assert md5(old_b) == OLD_MD5, 'BUILD199 bundle md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(old_b))
assert ms[MC] == old_mc, 'member does not match the copy inside the bundle'
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
ob = block(MC, ms[MC]); assert old_b.count(ob) == 1
nb = old_b.replace(ob, block(MC, new_mc))
rv = nb.replace(block(MC, new_mc), block(MC, ms[MC]))
assert md5(rv) == OLD_MD5, 'bundle reverse FAILED'
print('bundle reverse recovers md5 %s == old: True' % md5(rv))
print('new BUILD200  %s B  md5 %s  %s lines  %d members'
      % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE), '%s exists — never overwrite' % NEW_BUNDLE
    open(NEW_BUNDLE, 'wb').write(nb)
    print('written', NEW_BUNDLE, 'and', OUT)
else:
    print('DRY RUN — nothing installed')
