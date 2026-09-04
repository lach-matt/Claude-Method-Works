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
         "< proved — and until now the enumeration occupied three of them. Everything in this book was measured, "
         "verified, or proved, with and without witness; nothing was ever merely conjectured without the "
         "intention to prove or withdraw, and nothing withdrawn survived to be listed. An unwitnessed result "
         "is measured, verified, "
         "and exhaustive over everything the index can reach — and no cell inside it witnesses the claim. What "
         "it lacks is an observation. Where the observation does not yet exist the value is the ceiling — "
         "above verified, and short of proved until something is seen.")
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

SUBS_MAIN = [
    ('§D.2 L10354 the ordered scale', DEF_OLD + '\n', DEF_NEW + '\n'),
    ('L10748–L10753 the scale paragraph', PARA_OLD, PARA_NEW),
    ('the corridor row', R1[0], R1[1]),
    ('the nineteen surds row', R2[0], R2[1]),
]

# ---------------------------------------------------------------- the Register entry (subject matter)
seated = sorted(int(x) for x in re.findall(r'^### (\d+)$', r, re.M))
N = max(seated) + 1
assert N == 1801, f'expected to take 1801, next free is {N}'
E = (f"### {N}\n\n**THE STATUS COORDINATE TAKES A SIXTH VALUE: *UNWITNESSED*, ABOVE *VERIFIED* AND BELOW "
     "*PROVED*.** *§D.2 defined status on five values. A result can be measured, verified and exhaustive over "
     "everything the index reaches while no cell inside it witnesses the claim; that is not a doubt and not a "
     "demotion, and the five values had no room for it. The corridor is the first to take the value — "
     "non-empty at every one of the 106 steps and saying nothing about any element of the table it ranges "
     "over (1445, 1463) — and the nineteen surds follow it, true of ν as a form and of nothing in the "
     "periodic table (1460). Where an observation does not yet exist the value is the ceiling, and it is what "
     "the spectra index needs above Z = 108. Neither row is withdrawn and nothing is deleted.* "
     "Registers 1445; 1460; 1463. (a new protocol.)\n")
TAIL = '\n' + E
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
new_r = r + TAIL; assert new_r[:-len(TAIL)] == r, 'Register is not old + tail'
print(f'main: {len(SUBS_MAIN)} substitutions, reverse recovers md5 {md5(old_main)} == old: True')
print(f'Register: 0 substitutions + entry {N} appended, old bytes untouched: True')

# ---------------------------------------------------------------- what must NOT have moved
NL = new_m.split('\n')
# every line above the paragraph (L10748) must be identical except the §D.2 definition at L10354
_above = [i + 1 for i in range(10747) if NL[i] != ML[i]]
assert _above == [10354], f'lines above the paragraph moved: {_above}'
for probe in ('nothing withdrawn survived to be listed', 'the observability boundary, tested once',
              'slack = kernel, §18.4.1'):
    assert new_m.count(probe) == m.count(probe), f'{probe!r} count moved'
assert 'slack = kernel conjecture occupies' not in new_m, 'the slack sentence was not removed'
assert new_m.count('**conjectured** · sampled · none found') == m.count('**conjectured** · sampled · none found')
print('rows untouched: slack = kernel and the observability boundary keep their status (M: no row changes)')

# ---------------------------------------------------------------- Ruling A: the parked counts, scored
for pat in (r'\*\*1635 entries, 1 to 1792\.\*\*', r'\| \*\*a correction\*\* \| ([\d,]+) \|'):
    assert re.search(pat, new_r), f'count site {pat} moved — Ruling A parks it'
print(f'PARKED (Ruling A): entries now 1 to {N}; the front matter still prints its BUILD180 extent — reg1-04 carries it')

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
