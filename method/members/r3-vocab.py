#!/usr/bin/env python3
"""r3-vocab.py — R3: the sixth status value. BUILD94 -> BUILD95 main.

M's ruling, this session. Appendix D's `status` coordinate is an ORDERED scale defined at §D.2 on five
values. A sixth, **unwitnessed**, is added between `verified` and `proved`, for a result that is measured,
verified and exhaustive over everything the index can reach while no cell inside it witnesses the claim.
M: it "ranks higher in rank as something other than proven", and its largest use is the Löwdin spectra
index above Z = 108, where the cells are computed and the elements are not yet observed.

FOUR SITES, all content or prose ruled by M, none of them chosen here:
  1. §D.2 L10354      the definition line — the value inserted in the ordered chain, realigned to the
                      header's own column so the table's alignment is measured and not guessed.
  2. L10748–L10753    the paragraph that states the scale. "five values" -> "six values"; the chain
                      restated; "nothing was ever merely conjectured" -> "...without the intention to
                      prove or withdraw" (M's wording, which makes the sentence a claim about METHOD, so
                      the two standing conjectures at L10741 and L10865 sit inside it rather than
                      falsifying it — NO ROW CHANGES); the slack = kernel sentence removed on M's ruling
                      that the index is calibrated to the periodic elements and holds no idle conjecture;
                      and the value introduced with its own invitation.
  3. L10858           the corridor row -> unwitnessed (M, question 1).
  4. L10859           the nineteen surds row -> unwitnessed (M, question 2, option (a)).

NOT DONE HERE: L10864, the necessity of state. Its disposition waits on M — register 1448 is to be marked
proven and tied to 1332, and the Register carries no status coordinate, so what that attaches to is open.

RULING A still holds: the Register's front-matter counts are NOT touched, and kinds.py is NOT run. Entry
1801 is appended; the count drift it widens is scored, never repaired, and reg1-04 carries it.

Every anchor is the site's own text, so the two row edits are order-independent of the paragraph edit that
shifts them. The paragraph grows by 2 lines: everything below L10753 moves +2, and that is reported, not
hidden — the instrument estate is re-anchored against it.

Usage:  python3 r3-vocab.py            dry run
        python3 r3-vocab.py --write    writes /home/claude/build95/<members> and the BUILD95 bundle
"""
import os, re, sys, hashlib, tempfile, textwrap

MEM = '/home/claude/members/'; HOME = '/home/claude/'
OLD_BUNDLE = HOME + 'The_Method_1_6_BUILD94_main_and_register.md'
OLD_MD5 = '6079e066b5e480db6c47f754660a9b6e'
NEW_BUNDLE = HOME + 'The_Method_1_6_BUILD95_main_and_register.md'
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
OUT = HOME + 'build95/' if WRITE else tempfile.mkdtemp(prefix='r3vocab-dry-') + '/'
md5 = lambda b: hashlib.md5(b).hexdigest()
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

old_main = open(MEM + MAIN, 'rb').read(); old_reg = open(MEM + REG, 'rb').read()
m = old_main.decode('utf-8'); r = old_reg.decode('utf-8'); ML = m.split('\n')
print(f'old {MAIN}  {len(old_main):,} B  md5 {md5(old_main)}  {old_main.count(chr(10).encode()):,} lines')
print(f'old {REG}   {len(old_reg):,} B  md5 {md5(old_reg)}  {old_reg.count(chr(10).encode()):,} lines')

# ---------------------------------------------------------------- 1. the §D.2 definition line
DEF_OLD = '  status              withdrawn < conjectured < measured < verified < proved                         ordered'
assert m.count(DEF_OLD) == 1, 'the §D.2 status line is not unique'
_hdr = next(l for l in ML if 'coordinate' in l and 'values' in l and 'kind' in l)
_kind_col = _hdr.index('kind', _hdr.index('values'))
_vals_col = DEF_OLD.index('withdrawn')
_chain = 'withdrawn < conjectured < measured < verified < unwitnessed < proved'
_pad = _kind_col - (_vals_col + len(_chain))
assert _pad > 0, 'the new chain does not fit the table column'
DEF_NEW = DEF_OLD[:_vals_col] + _chain + (' ' * _pad) + 'ordered'
assert DEF_NEW.index('ordered') == _kind_col, 'realignment failed against the header'
print(f'§D.2 realigned: "ordered" stays at column {_kind_col} (measured from the header, not assumed)')

# ---------------------------------------------------------------- 2. the paragraph
PARA_OLD = '\n'.join(ML[10747:10753]) + '\n'   # L10748–L10753
assert 'first conjecture this index has ever held' in PARA_OLD and 'slack = kernel conjecture' in PARA_OLD
assert m.count(PARA_OLD) == 1, 'the scale paragraph is not unique'
_text = ("**The interesting part is that one of the four is the first conjecture this index was built on.** "
         "§D.2 defines *status* on six values — withdrawn < conjectured < measured < verified < unwitnessed "
         "< proved — and until now the enumeration occupied three of them. Everything in this book was "
         "measured, verified, or proved, with and without witness; nothing was ever merely conjectured "
         "without the intention to prove or withdraw, and nothing withdrawn survived to be listed. An "
         "unwitnessed result is proved and not yet observed — measured, verified, and exhaustive over "
         "everything the index can reach, with no cell inside it witnessing the claim. Proof is a matter of "
         "mathematics and not of observation, so the value ranks below proved for a reason that is a bias "
         "and not a defect — observation.")
_w = max(len(l) for l in ML[10747:10753])
PARA_NEW = '\n'.join('  ' + l for l in textwrap.wrap(' '.join(_text.split()), width=_w - 2,
                                                     break_long_words=False, break_on_hyphens=False)) + '\n'
_shift = PARA_NEW.count('\n') - PARA_OLD.count('\n')
print(f'paragraph: {PARA_OLD.count(chr(10))} lines -> {PARA_NEW.count(chr(10))} lines  (shift {_shift:+d} for every line below L10753)')

# ---------------------------------------------------------------- 3 & 4. the two rows, anchored by their own text
def row(anchor, old_coord, new_coord):
    hits = [l for l in ML if anchor in l and old_coord in l]
    assert len(hits) == 1, f'{anchor!r}: {len(hits)} rows match, not 1'
    l = hits[0]
    assert l.count(old_coord) == 1
    return l + '\n', l.replace(old_coord, new_coord) + '\n'

R1 = row('the corridor, 106 consistent inequalities', 'verified as a result about the form (1445, 1463)',
         'unwitnessed · exhaustive · none found (a result about the form; registers 1445, 1463)')
R2 = row('the nineteen surds, the complete endpoint set', 'withdrawn with ν at 1460',
         'unwitnessed · exhaustive · none found (true of ν as a form; register 1460)')

# M's ruling: the observability boundary is not a conjecture. Register 1377 states a decidable
# criterion — does the effect modify the equation, or require its solution? — names the prior art on
# both sides (Schrödinger 1926 and its sequels; Born–Heisenberg–Jordan 1925–26; von Neumann 1927/1932)
# and EXPLAINS Λ_cross's exception rather than recording it. And M's principle: outside literature and
# prior art COUNT AS WITNESS, which is why the citations and the bibliography exist — so the precedent
# column moves from 'none found' to 'found' on the same ruling.
R3 = row('the observability boundary, tested once', 'conjectured · sampled · none found',
         'verified · sampled · found')

# §4.6 marked proved (M: A3). Proof is mathematics, not observation — the protocol is proved because
# the case it was built for arrived and it caught it. This is the one protocol of the ten that is not
# merely earned by a failure but established by one.
A46_OLD = '  4.6   **a test that could not fail** — exhibit the failure mode before trusting the pass'
A46_NEW = '  4.6   **a test that could not fail** — exhibit the failure mode before trusting the pass; a\n        criterion fixed from the case it judges cannot fail — proved by the case it was built for and\n        then caught'
assert m.count(A46_OLD + chr(10)) == 1, "the §4.6 line is not unique"

SUBS_MAIN = [
    ('§4.6 marked proved', A46_OLD + chr(10), A46_NEW + chr(10)),
    ('§D.2 L10354 the ordered scale', DEF_OLD + '\n', DEF_NEW + '\n'),
    ('L10748–L10753 the scale paragraph', PARA_OLD, PARA_NEW),
    ('the corridor row', R1[0], R1[1]),
    ('the nineteen surds row', R2[0], R2[1]),
    ('the observability boundary row', R3[0], R3[1]),
]

# ---------------------------------------------------------------- the Register entry (subject matter)
seated = sorted(int(x) for x in re.findall(r'^### (\d+)$', r, re.M))
N = max(seated) + 1
assert N == 1801, f'expected to take 1801-1802, next free is {N}'
assert not re.search(rf'^### {N + 1}\b', r, re.M)
E1 = (f"### {N}\n\n**THE STATUS COORDINATE TAKES A SIXTH VALUE: *UNWITNESSED*, ABOVE *VERIFIED* AND BELOW "
      "*PROVED*.** *§D.2 defined status on five values. A result can be measured, verified and exhaustive over "
      "everything the index reaches while nothing witnesses the claim; that is not a doubt and not a demotion, "
      "and the five values had no room for it. Proof is a matter of mathematics and not of observation, so the "
      "new value ranks below proved for a reason that is a bias and not a defect — observation. The corridor is "
      "the first to take it (1445, 1463), and the nineteen surds follow, true of ν as a form and of nothing in "
      "the periodic table (1460). Neither is withdrawn and nothing is deleted.* "
      "**WHAT COUNTS AS A WITNESS, stated because the value is meaningless without it: that ANYONE has observed "
      "it — this work or another.** *An observation of our own and an attribution found in the literature "
      "witness equally. That is why the search for outside attribution is method and not courtesy: a search "
      "that finds one moves a result out of this value, and a search that finds none is what leaves it "
      "there. An unwitnessed result is one nobody has yet seen. Above Z = 108 the spectra index is written "
      "almost entirely in the value, and it wants only for something to be seen.* "
      "Registers 1445; 1460; 1463. (a new protocol.)\n")
E2 = (f"### {N + 1}\n\n**THE OBSERVABILITY BOUNDARY IS NOT A CONJECTURE; IT IS VERIFIED, AND ITS PRIOR ART IS "
      "ITS WITNESS.** *Appendix D ranked it conjectured with no precedent found. Register 1377 states it as a "
      "decidable criterion — does the effect modify the equation, or require its solution? — names the prior "
      "art on both sides, Schrödinger's* Quantisierung als Eigenwertproblem *(1926) and its three sequels for "
      "the enumerable half and Born–Heisenberg–Jordan with von Neumann's spectral theorem for the operator "
      "half, and EXPLAINS Λ_cross's exception rather than recording it. A criterion that decides cases and "
      "carries its literature is not a guess.* **Re-ranked verified · sampled · found: verified because it "
      "decides, sampled because it has been applied once, and found because the literature is there — and by "
      "the witness rule of the entry above, someone has seen it.** Registers 1377. (a correction.)\n")
TAIL = '\n' + E1 + '\n' + E2
assert not re.search(rf'^### {N}\b', r, re.M)

def apply(t, subs):
    for name, a, b in subs:
        assert t.count(a) == 1, f'{name}: anchor occurs {t.count(a)} times'; assert a != b; t = t.replace(a, b)
    return t
def reverse(t, subs):
    for name, a, b in reversed(subs):
        assert t.count(b) == 1, f'{name}: reverse anchor occurs {t.count(b)} times'; t = t.replace(b, a)
    return t

new_m = apply(m, SUBS_MAIN); assert md5(reverse(new_m, SUBS_MAIN).encode('utf-8')) == md5(old_main), 'main reverse FAILED'
# The tie M ruled: a WARNING on 1332 citing 1448, in the Register's own idiom (39 already exist) and
# appended to the entry's single body line, so it adds no line and shifts nothing.
_i = next(i for i, l in enumerate(r.split(chr(10))) if l.strip() == '### 1332')
_b = next(j for j in range(_i, _i + 6) if r.split(chr(10))[j].strip() and not r.split(chr(10))[j].strip().startswith('###'))
_body = r.split(chr(10))[_b]
assert 'WARNING' not in _body, '1332 already carries a WARNING'
assert r.count(_body) == 1, "1332's body line is not unique"
WARN = "  **WARNING:** Qualified at register 1448. The memoryless test set *a* to each candidate subshell's own crossing value — a criterion fixed from the case it judges, which §4.6 shows cannot fail. **The claim stands:** the observed subshell is never uniquely determined, so the table is not computable from a single atom's configuration. **The count does not:** 104 of 106 under this placement, 62 of 106 under the corridor-non-empty convention."
SUBS_REG = [('the WARNING on 1332', _body + chr(10), _body + WARN + chr(10))]
new_r = apply(r, SUBS_REG) + TAIL; assert md5(reverse(new_r[:-len(TAIL)], SUBS_REG).encode('utf-8')) == md5(old_reg), 'Register reverse FAILED'
print(f'main: {len(SUBS_MAIN)} substitutions, reverse recovers md5 {md5(old_main)} == old: True')
print(f'Register: {len(SUBS_REG)} substitution (the 1332 WARNING, +0 lines) + entries {N} and {N+1} appended, reverse recovers {md5(old_reg)}')

# ---------------------------------------------------------------- what must NOT have moved
NL = new_m.split('\n')
# TWO shift bands now, because §4.6 is edited as well as the appendix paragraph. The reverse-md5 guard
# above is what proves the edit; this reports the bands and asserts that nothing ABOVE the first one moved.
_first = min(i + 1 for i in range(min(len(NL), len(ML))) if NL[i] != ML[i])
assert _first == 1447, f'the first changed line is L{_first}, expected §4.6 at L1447'
assert NL[:1446] == ML[:1446], 'a line above §4.6 moved'
_b1 = A46_NEW.count(chr(10)) + 1 - 1          # §4.6: one line becomes three
_b2 = PARA_NEW.count(chr(10)) - PARA_OLD.count(chr(10))
print(f'shift bands: +{_b1} for main L >= 1448 (§4.6), then a further +{_b2} below the scale paragraph')
print(f'  net: lines after the appendix paragraph move +{_b1 + _b2}; total {len(ML)} -> {len(NL)}')
for probe in ('nothing withdrawn survived to be listed', 'slack = kernel, §18.4.1'):
    assert new_m.count(probe) == m.count(probe), f'{probe!r} count moved'
assert 'slack = kernel conjecture occupies' not in new_m, 'the slack sentence was not removed'
assert new_m.count('**conjectured** · sampled · none found') == m.count('**conjectured** · sampled · none found'), \
    'slack = kernel must keep its status'
assert 'the observability boundary, tested once' in new_m and 'verified · sampled · found' in new_m
print('slack = kernel keeps conjectured (M: unchanged); the observability boundary moves to verified · sampled · found')

# ---------------------------------------------------------------- Ruling A: the parked counts, scored
for pat in (r'\*\*1635 entries, 1 to 1792\.\*\*', r'\| \*\*a correction\*\* \| ([\d,]+) \|'):
    assert re.search(pat, new_r), f'count site {pat} moved — Ruling A parks it'
print(f'PARKED (Ruling A): entries now 1 to {N+1}; the front matter still prints its BUILD180 extent — reg1-04 carries it')

# ---------------------------------------------------------------- press anchors
src = open(MEM + 'build.py', encoding='utf-8').read(); ns = {}
exec(src[src.index('SUBS = {'):src.index('\ndef sweep')], ns)
for v, oldt, newt in ((MAIN, m, new_m), (REG, r, new_r)):
    anchors = [a for a, b in ns['SUBS'].get(v, [])]
    moved = [(a[:44], oldt.count(a), newt.count(a)) for a in anchors if oldt.count(a) != newt.count(a)]
    print(f'build.py SUBS anchors on {v}: {len(anchors)} checked; changed by this edit: {moved}')
    assert not moved, 'this edit changed a press anchor'

# ---------------------------------------------------------------- the bundle
if WRITE: assert not os.path.exists(OUT), f'{OUT} exists'; os.makedirs(OUT)
elif not os.path.isdir(OUT): os.makedirs(OUT)
nm = new_m.encode('utf-8'); nr = new_r.encode('utf-8')
open(OUT + MAIN, 'wb').write(nm); open(OUT + REG, 'wb').write(nr)
old_b = open(OLD_BUNDLE, 'rb').read(); assert md5(old_b) == OLD_MD5, 'BUILD94 bundle md5 mismatch'
ms = dict((x.group(1).decode(), x.group(2)) for x in MEMBER.finditer(old_b))
assert ms[MAIN] == old_main and ms[REG] == old_reg
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
nb = old_b
for n_, body in ((MAIN, nm), (REG, nr)):
    ob = block(n_, ms[n_]); assert nb.count(ob) == 1; nb = nb.replace(ob, block(n_, body))
rv = nb
for n_, body in ((MAIN, nm), (REG, nr)):
    assert rv.count(block(n_, body)) == 1; rv = rv.replace(block(n_, body), block(n_, ms[n_]))
assert md5(rv) == OLD_MD5, 'bundle reverse FAILED'
print(f'bundle reverse recovers md5 {md5(rv)} == old: True')
print(f'new BUILD95  {len(nb):,} B  md5 {md5(nb)}  {nb.count(chr(10).encode()):,} lines  {len(ms)} members')
if WRITE:
    assert not os.path.exists(NEW_BUNDLE), f'{NEW_BUNDLE} exists — never overwrite'
    open(NEW_BUNDLE, 'wb').write(nb); print('written', NEW_BUNDLE, 'and', OUT)
else:
    print('DRY RUN — nothing written under /home/claude')
