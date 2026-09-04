#!/usr/bin/env python3
"""r3-dclose.py — R3: the necessity of state's verification, and theorem · physics closes.
BUILD96 -> BUILD97 main.

MEASURED FIRST, on M's instruction. Appendix D asserts E = 0 in every fibre. Recomputed from the
volume's own element tables under §D.2's declared value orders — 77 elements over 24 fibres, which
reconciles against four independently stated numbers — twenty-two close and two do not:

    law · physics       4 elements  3 cells  box 8   E = 3
    theorem · physics   2 elements  2 cells  box 4   E = 2

§D.5.6 IS THE PRECEDENT, and it is the same shape. There `theorem · order` admitted
`proved · sampled · none found` and held nothing there, and the repair was not a new element:
"the re-closure found a defect that was not in the index but in the evidence for one of its
elements, and the repair was to prove a thing that had been sampled." ℛ's three closure properties
were given two-line proofs and its verification moved `sampled -> exhaustive`. STATUS WAS NOT
TOUCHED. This does the same and no more.

WHY THE EVIDENCE CHANGED, which is what makes this a repair and not a promotion to fit. Register
1460 demoted this row's verification to `sampled` because §34.6's "104 of 106" was fixed from the
case it judged and was not independently reproducible (register 1448). That was right. But BUILD96
removed the count from §34.6 entirely: the section now rests on the geometry — ν is affine in `a`,
each subshell is the point (√r, n), only lower-hull vertices are ever selected — and
`tools/slopeaxis.py --selftest` asserts the corridor set equals the lower-hull vertex set at
0 mismatches over all 106 steps in BOTH forms. The sampling is no longer necessary, exactly as
ℛ's was not. The row's parenthetical still qualifies a count the volume no longer prints.

MEASURED CONSEQUENCE: with `verified · exhaustive · none found` the fibre's box falls 4 -> 2 and
E = 2 -> 0. Any status closes it so long as the verification is exhaustive; the status is left
exactly as printed because nothing here licenses moving it.

WHAT IS NOT DONE. `law · physics` still fails at E = 3 and is NOT touched. It closes only if the
observability boundary is `proved · exhaustive · found`, and nobody has proved it. Reordering is
ruled out: all 6! x 3! x 2! = 8,640 orderings of §D.2's three axes were swept and NONE closes the
appendix (DEF-153K). So the appendix closes in 23 of 24 after this, not 24, and the Register entry
says so rather than claiming the closure whole.

Usage:  python3 r3-dclose.py            dry run
        python3 r3-dclose.py --write    writes staging members + the BUILD97 bundle
"""
import os, sys, hashlib, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD96_main_and_register.md')
OLD_MD5 = '8b07978cbc2986ad4f56189d48151463'
NEW_BUNDLE = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD97_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build97') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)

old_main = open(MEM + MAIN, 'rb').read(); m = old_main.decode('utf-8')
old_reg = open(MEM + REG, 'rb').read();   r = old_reg.decode('utf-8')

OLD = ("  the necessity of state, §34.6                          theorem · physics            "
       "verified · sampled · none found (the claim stands at register 1332; its count is fixed from "
       "the case it judges and is not independently reproducible, register 1448)")
NEW = ("  the necessity of state, §34.6                          theorem · physics            "
       "verified · exhaustive · none found (register 1460 demoted the verification because the count "
       "was not reproducible; §34.6 no longer rests on a count — the ambiguity is geometry, and the "
       "corridor is the lower-hull vertex set at all 106 steps in both forms, register 1805)")

c = m.count(OLD); print('Appendix D row anchor occurs %d time(s)' % c); assert c == 1
# the coordinates column must still start where the enclosing table's header puts it
_i = m.index(OLD); _line_start = m.rfind('\n', 0, _i) + 1
_hdr = m.rfind('\n  new element', 0, _i)
_hcol = m[_hdr + 1:m.index('\n', _hdr + 1)].index('coordinates')
assert NEW.index('verified · exhaustive') == _hcol, 'new row breaks the table\'s column'
print('coordinates column %d: preserved' % _hcol)
m = m.replace(OLD, NEW)

E1805 = """

### 1805

**THE NECESSITY OF STATE'S VERIFICATION IS EXHAUSTIVE NOW, AND THEOREM · PHYSICS CLOSES; LAW · PHYSICS DOES NOT AND IS LEFT OPEN.** *Appendix D asserts E = 0 in every fibre. Recomputed from the volume's own element tables under §D.2's declared value orders — seventy-seven elements over twenty-four fibres, reconciling against §D.5.10's sum, §D.5's census at twenty-one for theorem · order and its caption's four for law · physics — **twenty-two fibres close and two do not**: law · physics at E = 3 and theorem · physics at E = 2.* **§D.5.6 is the precedent and the same shape: there theorem · order admitted a cell it did not hold, and the repair was not a new element but the evidence for an old one — 'the repair was to prove a thing that had been sampled', ℛ moving from sampled to exhaustive with its status untouched.** *Register 1460 demoted this row's verification because §34.6's 104 of 106 was fixed from the case it judged (register 1448). That was right, and BUILD96 removed the count from §34.6 altogether: the section rests on the geometry — ν affine in a, each subshell the point (√r, n), only lower-hull vertices ever selected — and slopeaxis.py asserts the corridor set IS the hull-vertex set at 0 mismatches over all 106 steps in both forms. The sampling is no longer necessary. Verification alone moves, sampled → exhaustive; the box falls from four to two and E from two to zero.* **AND THE OTHER FIBRE IS NOT REPAIRED. law · physics closes only with the observability boundary at proved · exhaustive · found, and nobody has proved it; §D.5.10's caption 'Law · physics now holds four elements over three cells and closes' was false when written, and recomputing at the boundary's pre-BUILD95 coordinates it fails identically. Reordering is ruled out by measurement: all 8,640 orderings of §D.2's three axes were swept and NONE closes the appendix — 1,440 close both failing fibres and every one of them breaks a fibre that closes today.** *So the appendix closes in twenty-three of twenty-four, and this entry says so rather than claiming the closure whole. Registers 1332; 1448; 1460; and §D.5.5's own warning that E = 0 is a claim relative to a stated fibration.* (a correction.)"""

assert r.count('### 1805') == 0, 'entry 1805 already exists'
assert r.rstrip().endswith('(a correction.)'), 'Register tail moved'
r = r.rstrip() + E1805 + '\n'

for probe, want in (('verified · sampled · none found (the claim stands', 0),
                    ('verified · exhaustive · none found (register 1460 demoted', 1)):
    got = m.count(probe); print('  main after: %-52s %d (want %d)' % (repr(probe)[:52], got, want))
    assert got == want

new_m = m.encode('utf-8'); new_r = r.encode('utf-8')
print('main %d -> %d B, lines %+d' % (len(old_main), len(new_m),
      m.count('\n') - old_main.decode('utf-8').count('\n')))
print('reg  %d -> %d B, lines %+d' % (len(old_reg), len(new_r),
      r.count('\n') - old_reg.decode('utf-8').count('\n')))

src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, old_main.decode('utf-8'), m), (REG, old_reg.decode('utf-8'), r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:40], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print('build.py SUBS anchors on %s: %d checked; changed: %s' % (v, len(anchors), moved))
    assert not moved

if WRITE:
    assert not os.path.exists(OUT), '%s exists' % OUT
    os.makedirs(OUT)
elif not os.path.isdir(OUT):
    os.makedirs(OUT)
open(OUT + MAIN, 'wb').write(new_m); open(OUT + REG, 'wb').write(new_r)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD96 md5 mismatch'
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
print('new BUILD97  %s B  md5 %s  %s lines  %d members'
      % (format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ','), len(ms)))
if WRITE:
    assert not os.path.exists(NEW_BUNDLE)
    open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE)
else:
    print('DRY RUN — nothing installed')
