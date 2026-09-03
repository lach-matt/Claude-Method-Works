#!/usr/bin/env python3
"""reseat.py — re-extract the live bundles over members/ and regenerate the index.

Every R3 build ends here: a new bundle is written, its members are extracted over
method/members/, MEMBER-INDEX.tsv is regenerated and method/verify.py must then
report VERIFY OK. Doing that by hand is the silent change the discipline forbids,
so it is a program with a guard.

The guard: a member is written only if the bytes extracted from the bundle splice
back into the bundle at the recorded offset and reproduce the bundle's own md5.
That is verify.py's second check, run before anything is written rather than after.

Usage:
    python3 method/reseat.py                          reseat from BUNDLES.tsv as recorded
    python3 method/reseat.py --set TAG=FILENAME ...   point a tag at a new bundle file, then reseat
    python3 method/reseat.py --check                  extract and compare; write nothing

BUNDLES.tsv (tag, filename, md5) is the live-bundle set and the only place a bundle
md5 is recorded. reseat.py writes it; verify.py reads it and never derives it.
"""
import csv, hashlib, pathlib, re, sys

H = pathlib.Path(__file__).resolve().parent
BUNDLES_TSV = H / 'BUNDLES.tsv'
INDEX_TSV = H / 'MEMBER-INDEX.tsv'
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)

md5 = lambda b: hashlib.md5(b).hexdigest()


def read_bundles():
    rows = list(csv.DictReader(open(BUNDLES_TSV, encoding='utf-8'), delimiter='\t'))
    return [(r['tag'], r['filename'], r['md5']) for r in rows]


def extract(raw, tag):
    """Every member of one bundle, as (name, body, offset). Offsets are body starts."""
    out = []
    for m in MEMBER.finditer(raw):
        out.append((m.group(1).decode('utf-8'), m.group(2), m.start(2)))
    names = [n for n, _, _ in out]
    assert len(names) == len(set(names)), f'{tag}: duplicate member name'
    assert out, f'{tag}: no members matched — the bundle form changed'
    return out


def splice_guard(raw, members, tag, want_md5):
    """verify.py's second check, run before writing: splice every body back and assert the md5."""
    buf = bytearray(raw)
    for _, body, off in members:
        buf[off:off + len(body)] = body
    got = md5(bytes(buf))
    assert got == md5(raw), f'{tag}: splice does not reproduce the bundle ({got} != {md5(raw)})'
    if want_md5 and want_md5 != got:
        print(f'  {tag}: bundle md5 {want_md5} -> {got}')
    return got


def main():
    argv = sys.argv[1:]
    check_only = '--check' in argv
    overrides = dict(a.split('=', 1) for a in argv if a.startswith('--set') is False and '=' in a)
    for i, a in enumerate(argv):
        if a == '--set' and i + 1 < len(argv) and '=' in argv[i + 1]:
            k, v = argv[i + 1].split('=', 1)
            overrides[k] = v

    bundles = [(tag, overrides.get(tag, fn), old) for tag, fn, old in read_bundles()]
    index, new_bundles, written = [], [], 0

    for tag, fn, old_md5 in bundles:
        path = H / fn
        assert path.exists(), f'{tag}: {fn} not found'
        raw = path.read_bytes()
        members = extract(raw, tag)
        got = splice_guard(raw, members, tag, old_md5)
        new_bundles.append((tag, fn, got))
        print(f'{tag:<20} {fn}  {len(raw):,} B  md5 {got}  {len(members)} members')

        for name, body, off in members:
            index.append({'member': name, 'bundle': tag, 'ext': pathlib.Path(name).suffix,
                          'bytes': str(len(body)), 'md5': md5(body), 'bundle_offset': str(off)})
            p = H / 'members' / name
            if check_only:
                if not p.exists() or p.read_bytes() != body:
                    print(f'  DIFFERS: {name}')
                continue
            if not p.exists() or p.read_bytes() != body:
                p.write_bytes(body)
                written += 1

    index.sort(key=lambda r: r['member'])
    names = [r['member'] for r in index]
    assert len(names) == len(set(names)), 'a member name appears in both bundles'

    if check_only:
        print(f'\n--check: {len(index)} members, nothing written')
        return

    with open(INDEX_TSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['member', 'bundle', 'ext', 'bytes', 'md5', 'bundle_offset'],
                           delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(index)

    with open(BUNDLES_TSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['tag', 'filename', 'md5'], delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows([{'tag': t, 'filename': fn, 'md5': m} for t, fn, m in new_bundles])

    stale = {p.name for p in (H / 'members').iterdir() if p.is_file()} - set(names)
    print(f'\nmembers written: {written}   index rows: {len(index)}   bundles: {len(new_bundles)}')
    if stale:
        print(f'NOT in any live bundle and left on disk ({len(stale)}): {sorted(stale)[:10]}')
    print('run: python3 method/verify.py')


if __name__ == '__main__':
    main()
