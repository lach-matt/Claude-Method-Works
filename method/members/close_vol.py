#!/usr/bin/env python3
"""close_vol.py — the guarded repair of a reader-facing VOLUME in the compendia bundle.

    python3 tools/close_vol.py --old OLD --new NEW --w W-NNN.md --subs SUBS.json
                              [--main MAIN_BUNDLE]

THE FOURTH MISSING ROUTE, and it exists for the reason the other three did.

`close.py` builds the compendia bundle and its change-set assertion refuses, BY DESIGN, to let any
seated member change: the only members that may differ are `WORKING-REGISTER.md`, `MANIFEST.tsv`
and the `--append` targets, and each of those must equal old body PLUS appended text. That is *no
silent change* and it is right. It also assumed a reader-facing volume never moves, which was true
while the chat-67 hold froze them and false the moment M approves a repair.

`close_main.py` writes the MAIN bundle's Register and its counts. `close_rebank.py` regenerates a
golden BY RUNNING its instrument. `close_census.py` regenerates the derived census. **None of the
four writes a compendium.** So a repair M has approved had no way into the store of record, exactly
as a Register entry had none before chat 152 and a golden had none before W-2xx.

This is that route, to the same discipline, and it refuses more than it permits:

  1  NEW must not exist, and the old bundle's md5 is asserted against `--subs`'s own `old_md5`.
  2  EVERY SUBSTITUTION CARRIES ITS OWN OCCURRENCE COUNT and the count is asserted before any byte
     moves.  A substitution whose anchor is absent, or present a different number of times, refuses
     the whole build.  A substitution that is a no-op refuses it too, because rewriting a member to
     the bytes it already had hides that nothing happened.
  3  IT ADDS AND REMOVES NO MEMBER, and it never touches the main bundle — that is `close_main.py`'s
     contract and this tool reads main only to compute the manifest, as `close.py` does.
  4  THE W TEXT IS APPENDED to `WORKING-REGISTER.md`, so no volume may move without the working
     register recording it in the same build.  That is *no silent change* for volumes.
  5  MANIFEST.tsv is regenerated, because a volume's md5 and line count have moved.
  6  CHANGE SET: exactly the named volumes, `WORKING-REGISTER.md` and `MANIFEST.tsv`.  Any other
     member differing refuses the build.
  7  REVERSE GUARD: every substitution is reversed, the W text stripped and the old manifest body
     restored, and the result must reproduce the OLD BUNDLE'S OWN md5.  Nothing is written until it
     does.
  8  Only then is NEW written.

WHAT IT DOES NOT DO, and will not be extended to do.  It does not decide what a repair is: the
substitutions are data, written by hand into a spec a human reads, and the tool never derives one.
It does not re-bank a golden — a volume that moves may move a golden, and `close_rebank.py` is that
route, run AFTER this one and after the moved goldens are triaged.  It does not regenerate the
census; `close_census2.py` is that route, and W-274 records that the census close must come BEFORE
the golden re-bank.  It does not add a Register entry: if the repair is one the Register must
record, `close_main.py` runs beside it.

THE SPEC.  `--subs` is JSON:

    {"old_md5": "…",
     "subs": {"MEMBER-NAME.md": [[count, "old text", "new text"], …], …}}

`count` is the number of occurrences of `old text` the member must hold.  Text is exact and may
span lines.  A member named here must be a member of the old bundle and must not be
`WORKING-REGISTER.md` or `MANIFEST.tsv`.
"""
import hashlib
import json
import os
import re
import sys

MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
# A newline as a NAME, so no f-string in this file needs a backslash in its
# expression part.  That is the whole of what puts twenty-three seated members
# out of reach of Python 3.11, and there is no reason for a new tool to join them.
NL = b'\n'
md5 = lambda b: hashlib.md5(b).hexdigest()


def arg(k, default=None):
    return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else default


def parse(t):
    ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(t)]
    assert len(set(n for n, _ in ms)) == len(ms), 'duplicate member name'
    return ms


def manifest_text(main_members, comp_members):
    rows = ['bundle\tname\tbytes\tmd5\tlines']
    for tag, ms in (('main', main_members), ('compendia', comp_members)):
        for n, b in sorted(ms):
            if n == 'MANIFEST.tsv':
                continue
            rows.append('%s\t%s\t%d\t%s\t%d' % (tag, n, len(b), md5(b), b.count(NL)))
    return ('\n'.join(rows) + '\n').encode('utf-8')


def block(name, body):
    return b'<<<FILE: ' + name.encode() + b'>>>\n' + body + b'<<<END FILE: ' + name.encode() + b'>>>\n'


old_p, new_p, w_p, subs_p = arg('--old'), arg('--new'), arg('--w'), arg('--subs')
main_p = arg('--main')
assert old_p and new_p and w_p and subs_p, 'need --old --new --w --subs'
assert main_p, 'need --main: the manifest records the main bundle rows'
assert not os.path.exists(new_p), f'{new_p} exists — never overwrite'

old = open(old_p, 'rb').read()
old_ms = parse(old)
od = dict(old_ms)
main_ms = parse(open(main_p, 'rb').read())

spec = json.load(open(subs_p, encoding='utf-8'))
assert md5(old) == spec['old_md5'], \
    f"the spec is against md5 {spec['old_md5']}, this bundle is {md5(old)}"

W = open(w_p, 'rb').read()
assert W.startswith(b'### W-') and W.endswith(b'\n\n'), \
    'W text must begin "### W-" and end with a blank line'

# (2) every substitution asserted before a byte moves
SUBS = spec['subs']
assert SUBS, 'the spec names no substitution — refusing an empty build'
newbodies = {}
for name, rules in SUBS.items():
    assert name in od, f'{name} is not a member of the old bundle'
    assert name not in ('WORKING-REGISTER.md', 'MANIFEST.tsv'), \
        f'{name} is not a volume — close.py owns it'
    body = od[name].decode('utf-8')
    for count, a, b in rules:
        assert a != b, f'{name}: a substitution that changes nothing — REFUSED'
        got = body.count(a)
        assert got == count, f'{name}: anchor occurs {got}x, spec says {count}x: {a[:60]!r}'
        body = body.replace(a, b)
    nb = body.encode('utf-8')
    assert nb != od[name], f'{name}: the member did not change — REFUSED'
    newbodies[name] = nb
    print('%s  %s -> %s B  lines %+d  %d substitution(s)'
          % (name, format(len(od[name]), ','), format(len(nb), ','),
             nb.count(NL) - od[name].count(NL), len(rules)))

# (3) apply: the volumes, then the W text, then the manifest
new = old
for name, nb in newbodies.items():
    b0 = block(name, od[name])
    assert new.count(b0) == 1, f'{name}: member block not unique'
    new = new.replace(b0, block(name, nb))

end = b'<<<END FILE: WORKING-REGISTER.md>>>\n'
assert new.count(end) == 1
i = new.index(end)
assert new[i - 2:i] == b'\n\n', 'WR body must end with a blank line'
new = new[:i] + W + new[i:]

had_manifest = 'MANIFEST.tsv' in od
assert had_manifest, 'the old bundle has no MANIFEST.tsv — close.py seats it'
man_old = od['MANIFEST.tsv']
man = manifest_text(main_ms, parse(new))
ob = block('MANIFEST.tsv', man_old)
assert new.count(ob) == 1
new = new.replace(ob, block('MANIFEST.tsv', man))

# (5) measure
new_ms = parse(new)
nd = dict(new_ms)
print('old %s  %s B  md5 %s  %s lines  %d members'
      % (os.path.basename(old_p), format(len(old), ','), md5(old),
         format(old.count(NL), ','), len(old_ms)))
print('new %s  %s B  md5 %s  %s lines  %d members'
      % (os.path.basename(new_p), format(len(new), ','), md5(new),
         format(new.count(NL), ','), len(new_ms)))
print(f'MANIFEST.tsv  {len(man):,} B  md5 {md5(man)};  '
      f'WORKING-REGISTER.md  {len(nd["WORKING-REGISTER.md"]):,} B  '
      f'md5 {md5(nd["WORKING-REGISTER.md"])}')

# (6) change set
changed = [n for n, _ in old_ms if nd[n] != od[n]]
expect = set(SUBS) | {'WORKING-REGISTER.md', 'MANIFEST.tsv'}
assert set(changed) == expect, f'change set is {sorted(changed)}, expected {sorted(expect)}'
assert [n for n, _ in new_ms] == [n for n, _ in old_ms], 'the member list moved — REFUSED'
assert nd['WORKING-REGISTER.md'] == od['WORKING-REGISTER.md'] + W, 'WR is not old + W'
print(f'changed members: {sorted(changed)};  added/removed: none')

# (7) reverse guard
rev = new
rev = rev.replace(block('MANIFEST.tsv', man), block('MANIFEST.tsv', man_old))
assert rev.count(W + end) == 1
rev = rev.replace(W + end, end)
for name, nb in newbodies.items():
    b1 = block(name, nb)
    assert rev.count(b1) == 1
    rev = rev.replace(b1, block(name, od[name]))
print(f'reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}')
assert md5(rev) == md5(old), 'REVERSE GUARD FAILED — nothing written'

# (8) write
open(new_p, 'wb').write(new)
print('written', new_p)
