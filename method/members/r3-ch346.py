#!/usr/bin/env python3
"""r3-ch346.py — R3: §34.6 rewritten. BUILD95 -> BUILD96 main.

M approved the prose this session. §34.6 carried three defects, and the third was found only by
the main-volume sweep:

  1. "104 of 106 steps" reproduces under NO convention. Measured on the corpus's own instrument:
     62 (node-only, a real), 71 (finished, a real), 79 and 85 under a > 0. That is register 1448's
     objection — the placement was fixed from the case it judges — and docket 37 already records
     the figure as not reconstructible. The repair is to DROP the count, not reconcile it.

  2. "two to four" has the wrong ceiling. The measured range is two to six, and the steps outside
     the bracket are outside because they admit FIVE or SIX — more ambiguity, not less. The unit
     read the sign of its own residue backwards.

  3. "resets eighteen times" stood as the table's cost. Register 1580 certifies the minimum at
     THREE by Gallai duality — B, La and Lr have pairwise disjoint corridors — so eighteen is the
     cost of walking Z in order. Qualified, not removed: the eighteen are still what the walk does.

And the conclusion is refuted four paragraphs above it. §34.4's Status paragraph already records
Madelung's memoryless rule at 96 of 106 with no parameter (register 1445) against the held-out
walk's 90, so "the periodic table is not computable from a single atom's configuration" is
contradicted by the unit's own chapter. It is removed rather than rescoped: unrestricted over
rules it is false as quantified, since a lookup table is a memoryless function of one
configuration.

WHAT REPLACES IT is smaller than what it says now. The ambiguity is named as geometry — ν is
affine in a, each subshell is the point (√r, n), only lower-hull vertices are ever selected — and
what is NOT geometry is that the observed subshell is among them at all 106 steps. That is the
corridor, and register 1460 already placed it: a statement about the FORM, and non-emptiness
confirms nothing.

TWO SITES: main §34.6, and Register entry 1804 appended. Ruling A holds — the Register's
front-matter counts are NOT touched and kinds.py is NOT run; the drift entry 1804 widens is scored,
never repaired.

The unit grows by 20 lines: everything below §34.6 moves +20, reported and not hidden. The
Register grows by 4.

Usage:  python3 r3-ch346.py            dry run
        python3 r3-ch346.py --write    writes staging members + the BUILD96 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD95_main_and_register.md')
OLD_MD5 = '6551e685267852b85acbd9985d030113'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD96_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build96') + os.sep
MAIN = 'The_Method_1_6-2.md'
REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')

OLD = """**And the state is necessary.** With no carried value, 104 of 106 steps admit two
to four self-consistent subshells. *The observed one is always among them and
never uniquely determined. The periodic table is not computable from a single
atom's configuration.*"""

NEW = """*But eighteen is the cost of walking Z in order, not the cost of the table.*
Read as an arrangement of intervals, the 106 corridors are pierced by **three**
values of `a`, and three are forced: boron, lanthanum and lawrencium have
pairwise disjoint corridors, so no two of them can share one. The largest
disjoint set and the smallest piercing set agree at three, which certifies both
(register 1580).

**And the state is necessary — to the form.** With no carried value every step
admits more than one self-consistent subshell: two to six across the table, and
one never. *The observed one is always among them and never uniquely
determined.* **That much is geometry.** In the plane where each subshell is the
point (√r, n), ν takes whichever point a line of slope `a` reaches first, and a
point set with two distinct abscissae always offers more than one such point, at
every neutral atom there is. **What is not geometry is that the observed subshell
is among them at all 106 steps.** That is the corridor, and it is what survives
the form's demotion (§34.4; registers 1445, 1460, 1463).

**And the carried value is what the ordering costs.** In that same plane the
Madelung number is **M = 2n − p − 1** (register 1460) — with x = √p, the parabola
**M = 2y − x² − 1**, where ν sweeps straight lines. No single slope follows a
parabola, which is why no fixed `a` reaches it and why a re-set one does: **the
number carried between elements is the price of reading a quadratic order off a
linear form**, and the Madelung pick lies inside the corridor at every one of the
106 steps."""

c = m.count(OLD); print('§34.6 anchor occurs %d time(s)' % c); assert c == 1
m = m.replace(OLD, NEW)

E1804 = """

### 1804

**§34.6 CLAIMED THE WRONG THING, AND THE FIGURE IT CLAIMED IT WITH REPRODUCES UNDER NO CONVENTION.** *The unit stated ‘104 of 106 steps admit two to four self-consistent subshells’ and concluded that the periodic table is not computable from a single atom's configuration. Measured on the corpus's own instrument the range is two to six and no step admits fewer than two; 104 reproduces under none of the four conventions — 62 and 71 with `a` real, 79 and 85 with `a` > 0 — which is register 1448's objection, and the repair is to drop the count rather than reconcile it. The unit also read the sign of its own residue backwards: the steps outside the bracket are outside because they admit FIVE or SIX, which is more ambiguity and not less.* **And the conclusion is refuted four paragraphs above it — §34.4 records Madelung's memoryless rule at 96 of 106 with no parameter at all (register 1445) against the held-out walk's 90, so a rule reading one atom's configuration does better than the carried one.** *Rewritten. The ambiguity is stated as what it is, geometry: ν is affine in `a`, each admissible subshell is the point (√r, n), and only vertices of the lower convex hull are ever selected, so a point set with two distinct abscissae always offers more than one — at every neutral atom below 124 electrons. What is NOT geometry is that the observed subshell is among them at all 106 steps, and that is the corridor, which survives the form's demotion at register 1460 and confirms nothing by being non-empty.* **Two figures enter. Register 1580's certified three — B, La and Lr have pairwise disjoint corridors, so eighteen resets is the cost of walking Z in order and not the cost of the table. And register 1460's surviving arithmetic M = 2n − p − 1, which in that plane is the parabola M = 2y − x² − 1 where ν sweeps lines, so the carried number is the price of reading a quadratic order off a linear form.** Registers 1332; 1445; 1448; 1460; 1580. (a correction.)"""

assert r.count('### 1804') == 0, 'entry 1804 already exists'
assert r.rstrip().endswith('(a correction.)'), 'Register tail is not where it was'
r = r.rstrip() + E1804 + '\n'

for probe, want in (('104 of 106', 0), ('not computable from a single', 0),
                    ('two to six across the table', 1), ('M = 2n − p − 1', 1)):
    got = m.count(probe); print('  main after: %-32s %d (want %d)' % (repr(probe), got, want))
    assert got == want, 'post-condition failed on %r' % probe

new_m = m.encode('utf-8'); new_r = r.encode('utf-8')
print('main  %d B -> %d B, lines %+d' % (len(old_main), len(new_m),
      m.count('\n') - old_main.decode('utf-8').count('\n')))
print('reg   %d B -> %d B, lines %+d' % (len(old_reg), len(new_r),
      r.count('\n') - old_reg.decode('utf-8').count('\n')))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, old_main.decode('utf-8'), m), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:44], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved))
    assert not moved, 'this edit changed a press anchor'

if WRITE:
    assert not os.path.exists(OUT), '%s exists' % OUT
    os.makedirs(OUT)
elif not os.path.isdir(OUT):
    os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD95 md5 mismatch'
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
print('new BUILD96  %s B  md5 %s  %s lines  %d members'
      % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE), '%s exists — never overwrite' % NEW_BUNDLE
    open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE, 'and', OUT)
else:
    print('DRY RUN — nothing installed')
