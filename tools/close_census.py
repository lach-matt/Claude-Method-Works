#!/usr/bin/env python3
"""close_census.py — the guarded regeneration of DEFECT-CENSUS.tsv, the one derived member that is not a golden.

    python3 members/close_census.py --old OLD --new NEW --w W-NNN.md [--append NAME PATH ...] [--main MAIN]

`close.py` seats new members and appends to append-only ones. `close_rebank.py` re-banks a golden by
running its instrument. Neither can touch `DEFECT-CENSUS.tsv`: it is a seated member DERIVED from the
volumes by `census.py`, it is not `NAME.out`, and `close.py`'s change-set assertion refuses it. It
went stale the moment BUILD92 seated four Register entries, and `gate.py census` — a §0 gate step —
has failed since. This is the route it lacked, to the same discipline.

THE GUARD THAT MATTERS IS ID STABILITY. Census ids are cited by every `CENSUS-CLOSURES-*.tsv` and by
the READ records. If a regeneration renumbered them, every closure in the store would silently point
at a different row and the audit record would be quietly destroyed. So this tool refuses unless:

  * every id in the seated census is still present in the regenerated one — none may disappear;
  * every surviving id keeps its CLASS, VOLUME and LINE — an id is an address, not a position;
  * the new ids form a contiguous run above the seated maximum — new rows are appended, never spliced.

A row whose free text changed (a site count, say) is permitted and is reported. Everything else is
close.py's discipline unchanged: the W text appended to WORKING-REGISTER.md, MANIFEST.tsv recomputed,
the change set asserted, and a reverse guard that restores the old census and must reproduce the OLD
bundle's own md5 before anything is written.
"""
import sys, os, re, hashlib, subprocess

MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()
H = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(H)
CENSUS = 'DEFECT-CENSUS.tsv'

def arg(k, d=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
def parse(t):
    ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(t)]
    assert len(set(n for n, _ in ms)) == len(ms), 'duplicate member name'; return ms
def blk(n, b): return b'<<<FILE: ' + n.encode() + b'>>>\n' + b + b'<<<END FILE: ' + n.encode() + b'>>>\n'
def manifest_text(main_ms, comp_ms):
    rows = ['bundle\tname\tbytes\tmd5\tlines']
    for tag, ms in (('main', main_ms), ('compendia', comp_ms)):
        for n, b in sorted(ms):
            if n == 'MANIFEST.tsv': continue
            rows.append(f'{tag}\t{n}\t{len(b)}\t{md5(b)}\t{b.count(b"\n")}')
    return ('\n'.join(rows) + '\n').encode('utf-8')
def index(text):
    out = {}
    for line in text.decode('utf-8').splitlines():
        if not line.strip(): continue
        f = line.split('\t')
        if not f[0].isdigit(): continue
        out[int(f[0])] = (f[1], f[2], f[3], line)     # class, volume, line, whole row
    return out

old_p, new_p, w_p = arg('--old'), arg('--new'), arg('--w')
main_p = arg('--main')
appends = [(sys.argv[i + 1], open(sys.argv[i + 2], 'rb').read()) for i, a in enumerate(sys.argv) if a == '--append']
assert old_p and new_p and w_p and main_p, 'need --old --new --w --main'
assert not os.path.exists(new_p), f'{new_p} exists — never overwrite'

old = open(old_p, 'rb').read(); old_ms = parse(old); od = dict(old_ms); old_names = [n for n, _ in old_ms]
assert CENSUS in od, f'{CENSUS} is not a seated member'
main_ms = parse(open(main_p, 'rb').read())
W = open(w_p, 'rb').read()
assert W.startswith(b'### W-') and W.endswith(b'\n\n'), 'W text must begin "### W-" and end with a blank line'

# regenerate by RUNNING census.py — never copied, never hand-edited
target = os.path.join(HOME, CENSUS)
before = open(target, 'rb').read() if os.path.exists(target) else None
p = subprocess.run(['python3', 'census.py'], cwd=H, capture_output=True)
assert p.returncode == 0, f'census.py exit {p.returncode} — REFUSED\n' + p.stderr.decode()[-800:]
assert os.path.exists(target), f'census.py did not write {target}'
fresh = open(target, 'rb').read()
assert fresh != od[CENSUS], f'{CENSUS} is unchanged — REFUSED, there is nothing to regenerate'

# --- id stability, the guard that matters ---
A, B = index(od[CENSUS]), index(fresh)
gone = sorted(set(A) - set(B))
assert not gone, f'REFUSED: {len(gone)} census ids disappeared: {gone[:20]}'
moved = sorted(i for i in set(A) & set(B) if A[i][:3] != B[i][:3])
assert not moved, f'REFUSED: {len(moved)} ids changed their class/volume/line — an id is an address: {moved[:20]}'
added = sorted(set(B) - set(A))
if added:
    lo, hi, top = added[0], added[-1], max(A)
    assert lo == top + 1 and added == list(range(lo, hi + 1)), \
        f'REFUSED: new ids {lo}..{hi} are not a contiguous run above the seated maximum {top}'
changed = sorted(i for i in set(A) & set(B) if A[i][3] != B[i][3])
print(f'  census {len(A):,} -> {len(B):,} rows   ids unchanged: {len(A) - len(changed):,}   text changed: {len(changed)}   appended: {len(added)}')
for i in changed[:12]: print(f'    id {i:<5} text moved  ({A[i][0]} {A[i][1]} L{A[i][2]})')
for i in added[:12]:  print(f'    id {i:<5} NEW         ({B[i][0]} {B[i][1]} L{B[i][2]})')

# W text and appends
end = b'<<<END FILE: WORKING-REGISTER.md>>>\n'; assert old.count(end) == 1
i = old.index(end); assert old[i - 2:i] == b'\n\n', 'WR body must end with a blank line'
new = old[:i] + W + old[i:]
for n, txt in appends:
    e = b'<<<END FILE: ' + n.encode() + b'>>>\n'
    assert n in old_names and new.count(e) == 1, f'--append target {n} not a unique old member'
    assert txt.endswith(b'\n'), f'--append text for {n} must end with a newline'
    j = new.index(e); new = new[:j] + txt + new[j:]

ob = blk(CENSUS, od[CENSUS]); assert new.count(ob) == 1; new = new.replace(ob, blk(CENSUS, fresh))
man_old = od['MANIFEST.tsv']; man = manifest_text(main_ms, parse(new))
ob = blk('MANIFEST.tsv', man_old); assert new.count(ob) == 1; new = new.replace(ob, blk('MANIFEST.tsv', man))

new_ms = parse(new); nd = dict(new_ms)
print(f'old {os.path.basename(old_p)}  {len(old):,} B  md5 {md5(old)}  {old.count(b"\n"):,} lines  {len(old_ms)} members')
print(f'new {os.path.basename(new_p)}  {len(new):,} B  md5 {md5(new)}  {new.count(b"\n"):,} lines  {len(new_ms)} members')
print(f'MANIFEST.tsv  {len(man):,} B  md5 {md5(man)};  {CENSUS}  {len(fresh):,} B  md5 {md5(fresh)}')
allowed = {'WORKING-REGISTER.md', 'MANIFEST.tsv', CENSUS} | {n for n, _ in appends}
ch = [n for n in old_names if nd[n] != od[n]]
assert set(ch) <= allowed, f'unexpected change in old members: {sorted(set(ch) - allowed)}'
assert nd['WORKING-REGISTER.md'] == od['WORKING-REGISTER.md'] + W, 'WR is not old + W'
for n, txt in appends: assert nd[n] == od[n] + txt, f'{n} is not old + appended text'
assert [n for n, _ in new_ms] == old_names, 'member set changed — this tool adds and removes nothing'
print(f'changed old members: {sorted(ch)}; added: none; lines {new.count(b"\n") - old.count(b"\n"):+d}')

rev = new.replace(blk('MANIFEST.tsv', man), blk('MANIFEST.tsv', man_old))
nb = blk(CENSUS, fresh); assert rev.count(nb) == 1; rev = rev.replace(nb, blk(CENSUS, od[CENSUS]))
for n, txt in reversed(appends):
    e = b'<<<END FILE: ' + n.encode() + b'>>>\n'; assert rev.count(txt + e) == 1; rev = rev.replace(txt + e, e)
assert rev.count(W + end) == 1; rev = rev.replace(W + end, end)
print(f'reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}')
assert md5(rev) == md5(old), 'REVERSE GUARD FAILED — nothing written'
open(new_p, 'wb').write(new); print('written', new_p)
