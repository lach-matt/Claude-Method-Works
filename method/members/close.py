#!/usr/bin/env python3
"""close.py — the guarded build at a chat's close (chat 74, ruling 2).
  python3 members/close.py --old OLD_BUNDLE --new NEW_BUNDLE --w W-NNN.md [--main MAIN_BUNDLE] [--append NAME PATH ...] --members f1 f2 ...
Does, in order, and refuses on any failure: (1) asserts NEW does not exist and no new member name collides;
(2) appends the W-NNN text (must begin '### W-' and end '\\n\\n') to the WORKING-REGISTER.md body, immediately before its END marker,
    and, for each --append NAME PATH, appends PATH's text (must end '\\n') to the append-only member NAME the same way (RULINGS-R2.md, DEFERRED.md);
(3) appends each member after the last END marker as '\\n<<<FILE: name>>>\\n' + body + '<<<END FILE: name>>>\\n' (body must end '\\n');
(4) computes MANIFEST.tsv over every member of the main bundle and of the new compendia bundle (except MANIFEST.tsv itself)
    and replaces the MANIFEST.tsv member body, or appends MANIFEST.tsv as a member if the old bundle had none;
(5) measures bytes / md5 / lines / members; (6) checks that among old members only WORKING-REGISTER.md, MANIFEST.tsv and the --append members changed,
    and that each grown body = old body + appended text; (7) reverse guard: strips the appended members and the W text and restores the
    old MANIFEST body (or removes the MANIFEST member) and asserts the result's md5 equals the old bundle's; (8) writes NEW."""
import sys, os, re, hashlib
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()
def arg(k, default=None):
    return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else default
def block(name, body): return b'\n<<<FILE: ' + name.encode() + b'>>>\n' + body + b'<<<END FILE: ' + name.encode() + b'>>>\n'
def parse(t):
    ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(t)]
    assert len(set(n for n, _ in ms)) == len(ms), 'duplicate member name'; return ms
def manifest_text(main_members, comp_members):
    rows = ['bundle\tname\tbytes\tmd5\tlines']
    for tag, ms in (('main', main_members), ('compendia', comp_members)):
        for n, b in sorted(ms):
            if n == 'MANIFEST.tsv': continue
            rows.append(f'{tag}\t{n}\t{len(b)}\t{md5(b)}\t{b.count(b"\n")}')
    return ('\n'.join(rows) + '\n').encode('utf-8')

old_p, new_p, w_p = arg('--old'), arg('--new'), arg('--w')
main_p = arg('--main', '/home/claude/The_Method_1_6_BUILD90_main_and_register.md')
mem_ps = sys.argv[sys.argv.index('--members') + 1:] if '--members' in sys.argv else []
appends = [(sys.argv[i + 1], open(sys.argv[i + 2], 'rb').read()) for i, a in enumerate(sys.argv) if a == '--append']
assert old_p and new_p and w_p, 'need --old --new --w'
assert not os.path.exists(new_p), f'{new_p} exists — never overwrite'
old = open(old_p, 'rb').read(); old_ms = parse(old); old_names = [n for n, _ in old_ms]
main_ms = parse(open(main_p, 'rb').read())
W = open(w_p, 'rb').read(); assert W.startswith(b'### W-') and W.endswith(b'\n\n'), 'W text must begin "### W-" and end with a blank line'
new_members = []
for p in mem_ps:
    n = os.path.basename(p); b = open(p, 'rb').read()
    assert n not in old_names and n not in [x for x, _ in new_members], f'member name collision: {n}'
    assert b.endswith(b'\n'), f'{n}: body must end with a newline'; new_members.append((n, b))
# (2) W text into the WR body
end = b'<<<END FILE: WORKING-REGISTER.md>>>\n'; assert old.count(end) == 1
i = old.index(end); assert old[i - 2:i] == b'\n\n', 'WR body must end with a blank line'
new = old[:i] + W + old[i:]
for n, txt in appends:
    e = b'<<<END FILE: ' + n.encode() + b'>>>\n'; assert n in old_names and new.count(e) == 1, f'--append target {n} not a unique old member'
    assert txt.endswith(b'\n'), f'--append text for {n} must end with a newline'
    j = new.index(e); new = new[:j] + txt + new[j:]
# (3) append members after the last END marker
assert new.endswith(b'>>>\n'), 'bundle must end with an END marker'
for n, b in new_members: new += block(n, b)
# (4) manifest
had_manifest = 'MANIFEST.tsv' in old_names
man_old = dict(old_ms).get('MANIFEST.tsv')
comp_ms = parse(new); man = manifest_text(main_ms, comp_ms)
if had_manifest:
    ob = b'<<<FILE: MANIFEST.tsv>>>\n' + man_old + b'<<<END FILE: MANIFEST.tsv>>>\n'; assert new.count(ob) == 1
    new = new.replace(ob, b'<<<FILE: MANIFEST.tsv>>>\n' + man + b'<<<END FILE: MANIFEST.tsv>>>\n')
else:
    new += block('MANIFEST.tsv', man)
# (5) measure
new_ms = parse(new); nd = dict(new_ms); od = dict(old_ms)
print(f'old {os.path.basename(old_p)}  {len(old):,} B  md5 {md5(old)}  {old.count(b"\n"):,} lines  {len(old_ms)} members')
print(f'new {os.path.basename(new_p)}  {len(new):,} B  md5 {md5(new)}  {new.count(b"\n"):,} lines  {len(new_ms)} members')
print(f'MANIFEST.tsv  {len(man):,} B  md5 {md5(man)}  {man.count(b"\n")} lines;  WORKING-REGISTER.md  {len(nd["WORKING-REGISTER.md"]):,} B  md5 {md5(nd["WORKING-REGISTER.md"])}  {nd["WORKING-REGISTER.md"].count(b"\n"):,} lines')
# (6) change set
changed = [n for n in old_names if nd[n] != od[n]]
assert set(changed) <= {'WORKING-REGISTER.md', 'MANIFEST.tsv'} | {n for n, _ in appends}, f'unexpected change in old members: {changed}'
assert nd['WORKING-REGISTER.md'] == od['WORKING-REGISTER.md'] + W, 'WR is not old + W'
for n, txt in appends: assert nd[n] == od[n] + txt, f'{n} is not old + appended text'
added = [n for n, _ in new_ms if n not in od]
print(f'changed old members: {changed};  added members: {added};  lines +{new.count(b"\n") - old.count(b"\n")} / -0')
# (7) reverse guard
rev = new
for n, b in new_members: assert rev.count(block(n, b)) == 1; rev = rev.replace(block(n, b), b'')
if had_manifest:
    nb = b'<<<FILE: MANIFEST.tsv>>>\n' + man + b'<<<END FILE: MANIFEST.tsv>>>\n'; assert rev.count(nb) == 1
    rev = rev.replace(nb, b'<<<FILE: MANIFEST.tsv>>>\n' + man_old + b'<<<END FILE: MANIFEST.tsv>>>\n')
else:
    assert rev.count(block('MANIFEST.tsv', man)) == 1; rev = rev.replace(block('MANIFEST.tsv', man), b'')
for n, txt in reversed(appends):
    e = b'<<<END FILE: ' + n.encode() + b'>>>\n'; assert rev.count(txt + e) == 1; rev = rev.replace(txt + e, e)
assert rev.count(W + end) == 1; rev = rev.replace(W + end, end)
print(f'reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}')
assert md5(rev) == md5(old), 'REVERSE GUARD FAILED — nothing written'
# (8) write
open(new_p, 'wb').write(new); print('written', new_p)
