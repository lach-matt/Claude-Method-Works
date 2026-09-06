#!/usr/bin/env python3
"""r4-a1.py — R4 Batch A item 1: ruling 11 of RULINGS-R4f. §34.4's "No parameter is fitted" takes
the "in the form" qualifier §34.8 already carries five lines below it, and register 1836 records the
repair. BUILD110 -> BUILD111 main.

Ruling 11 (M, 6 September 2026): *"yes."* — "§34.4 repairs with its class. *'No parameter is fitted'*
takes the *'in the form'* that §34.8 already carries, in the withdrawn-law class held for R3."

Scope, and it is exactly the ruling's: ONE substitution at §34.4. The bare string
"No parameter is fitted" occurs three times in the main volume — §34.4 L9602, §34.8 L9693 (which
already carries the qualifier) and §35.5 L9904 (a different chapter, outside the ruling) — so the
anchor is the long form, asserted unique in the whole bundle, and the bare string is never used.
Register 1350 carries the same unqualified sentence and is append-only: it is cited by 1836, not
edited.

Usage:  python3 r4-a1.py            dry run (asserts everything, writes nothing)
        python3 r4-a1.py --write    writes staging members + BUILD111 main
"""
import os, sys, re, hashlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEM = os.path.join(REPO, 'method', 'members') + os.sep
OLD_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD110_main_and_register.md')
OLD_M_MD5 = 'e1264def2a04df9ac010db3f0ea90953'
NEW_M = os.path.join(REPO, 'method', 'The_Method_1_6_BUILD111_main_and_register.md')
OUT = os.path.join(REPO, 'method', 'build111') + os.sep
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
WRITE = '--write' in sys.argv
md5 = lambda b: hashlib.md5(b).hexdigest()
def block(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'

# ---- the substitution, count-asserted -------------------------------------------------------------
SUB_OLD = "**No parameter is fitted**; the provenance of every term is §34.8's"
SUB_NEW = "**No parameter is fitted in the form**; the provenance of every term is §34.8's"

ENTRY_N = 1836
ENTRY = """

### 1836

**§34.4 SAID "NO PARAMETER IS FITTED" AND §34.8 SAID IT WITH THE QUALIFIER FIVE LINES LATER; THE RULE'S OWN SECTION NOW CARRIES IT TOO.** *§34.4 closes its derivation with* **No parameter is fitted** *unqualified, and §34.8 — the provenance table it points the reader to in the same sentence — closes with* **No parameter is fitted in the form; the placement of a along the walk is a fit (register 1445)**. *Register 1445 is what makes the difference load-bearing: placing a from each step's own corridor scores 99 of 106, held out properly it scores 90, and plain Madelung, which takes no free parameter at all, scores 96. So the unqualified sentence is the one the record has already withdrawn, and it stood in the section that states the rule. Repaired here as one guarded substitution at §34.4, the anchor asserted unique in the whole bundle before and after and the reverse substitution recovering the predecessor's md5; the form is untouched and only the qualifier moves.* **Not touched, and each for its own reason: §34.8 already carries the qualifier and is the sentence being matched; §35.5's "No parameter is fitted. No observation enters upstream of the score." is Chapter 35's claim about the walk's score and is outside this ruling; and register 1350, which prints the same unqualified sentence, is append-only and is corrected by this entry rather than edited.** *M's ruling of 6 September 2026 (RULINGS-R4f, ruling 11): the withdrawn-law class held for R3.* Registers 1350; 1445. (a correction.)"""

# ---- the volumes as they stand ---------------------------------------------------------------------
old = {n: open(MEM + n, 'rb').read() for n in (MAIN, REG)}
txt = {n: old[n].decode('utf-8') for n in old}

m = txt[MAIN]
assert m.count(SUB_OLD) == 1, 'anchor not unique in the volume: %d' % m.count(SUB_OLD)
assert m.count(SUB_NEW) == 0, 'the repair is already in place'
assert m.count('No parameter is fitted') == 3, 'the volume no longer carries three sites'
new_main = m.replace(SUB_OLD, SUB_NEW)
assert new_main.count('No parameter is fitted') == 3 and new_main.count(SUB_NEW) == 1
assert len(new_main) == len(m) + len(' in the form')

r = txt[REG]
assert r.count('### %d\n' % ENTRY_N) == 0, 'entry %d already seated' % ENTRY_N
assert r.count('### %d\n' % (ENTRY_N - 1)) == 1, 'entry %d is not seated' % (ENTRY_N - 1)
assert re.search(r'\(a (correction|withdrawal|finding|measurement)\.\)$', r.rstrip()), 'the Register does not end where expected'
new_reg = r.rstrip('\n') + ENTRY + '\n'

new = {MAIN: new_main, REG: new_reg}
print('§34.4  %r' % SUB_OLD)
print('   ->  %r' % SUB_NEW)
print('main volume: 3 sites of "No parameter is fitted" before and after; §34.8 and §35.5 unchanged')
print('register: entry %d appended, %s -> %s bytes' % (ENTRY_N, format(len(r.encode()), ','), format(len(new_reg.encode()), ',')))

# ---- the bundle, and the reverse guard ---------------------------------------------------------------
ob = open(OLD_M, 'rb').read(); assert md5(ob) == OLD_M_MD5, 'BUILD110 md5 mismatch'
MEMBER = re.compile(rb'<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S)
ms = {mm.group(1).decode(): mm.group(2) for mm in MEMBER.finditer(ob)}
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
print('BUILD110 -> BUILD111: reverse recovers md5 %s == old: True; new %s B md5 %s %s lines'
      % (OLD_M_MD5, format(len(nb), ','), md5(nb), format(nb.count(b'\n'), ',')))

if WRITE:
    os.makedirs(OUT, exist_ok=True)
    for v in new: open(OUT + v, 'wb').write(new[v].encode('utf-8'))
    assert not os.path.exists(NEW_M), 'BUILD111 already exists'
    open(NEW_M, 'wb').write(nb); print('written', NEW_M)
else:
    print('DRY RUN — nothing written.  Re-run with --write to seat the build.')
