#!/usr/bin/env python3
"""lineage.py -- ONE-TIME FOLD (s58).

Replaces 41 MANIFEST-HANDOFF-*.txt + 40 verify*.sh with a single LINEAGE.txt:
one line per sealed handoff carrying the file count and the manifest ROOT HASH.

A manifest's root hash reproduces from the manifest itself.  Keeping 41 full
manifests to prove 41 numbers is the accretion this fold removes.

Nothing is dropped without proof it is carried.  Any path sealed in a historic
manifest and absent from the current seal is written to the RETIRED block with
the session it left at.  A silent disappearance becomes a recorded one (F58.2).

Run once.  Thereafter condense.py maintains LINEAGE.txt at seal time.
"""
import sys, os, re, hashlib

def manifest_paths(fn):
    out = {}
    for ln in open(fn, encoding='utf-8', errors='replace'):
        ln = ln.rstrip('\n')
        if not ln.strip():
            continue
        parts = ln.split()
        if len(parts) < 2:
            continue
        h, p = parts[0], parts[-1]
        out[p.lstrip('./')] = h
    return out

def root_hash(paths):
    """Order-independent root over 'sha  path' pairs."""
    body = '\n'.join('%s  %s' % (paths[p], p) for p in sorted(paths))
    return hashlib.sha256(body.encode()).hexdigest()

def main():
    root = os.path.dirname(os.path.abspath(__file__)) + '/..'
    os.chdir(root)
    mans = sorted(
        (int(re.search(r'-(\d+)\.txt$', f).group(1)), f)
        for f in os.listdir('.')
        if re.match(r'^MANIFEST-HANDOFF-\d+\.txt$', f))
    if not mans:
        print('no manifests found'); return 1

    curN, curF = mans[-1][0], mans[-1][1]
    cur = manifest_paths(curF)

    SCAFFOLD = re.compile(r'^(MANIFEST-HANDOFF-\d+\.txt|verify\d*\.sh|README-HANDOFF-\d+\.md)$')

    rows, retired = [], {}
    seen_before = set()
    for N, fn in mans:
        p = manifest_paths(fn)
        rows.append((N, len(p), root_hash(p)))
        for path in p:
            if path in cur or SCAFFOLD.match(os.path.basename(path)):
                continue
            # absent from current seal: is the content carried under another path?
            bn = os.path.basename(path)
            carried = None
            for d in sorted(os.listdir('.')):
                if d.startswith('pack') and os.path.exists(os.path.join(d, bn)):
                    carried = os.path.join(d, bn); break
            prev = retired.get(path)
            if prev is None or N > prev[0]:
                retired[path] = (N, carried)
            seen_before.add(path)

    out = ['# LINEAGE -- LOWDIN handoff chain.  One line per sealed handoff.',
           '# Folded at s58 from %d historic manifests (F58.2 recorded the losses).' % len(mans),
           '# root = sha256 over the sorted "sha  path" body of that session\'s manifest.',
           '# Verifying session N means: rebuild the body, hash it, match root.',
           '#',
           '# N     files   root_sha256',
           '']
    for N, n, h in rows:
        out.append('%-6d %-7d %s' % (N, n, h))

    lost = [(p, v) for p, v in sorted(retired.items()) if v[1] is None]
    moved = [(p, v) for p, v in sorted(retired.items()) if v[1] is not None]

    out += ['', '# RETIRED -- sealed once, not in the current seal.',
            '# CARRIED: same basename survives inside a sealed pack (root duplicate condensed).',
            '# LOST   : no copy anywhere in the archive.  F58.2.', '']
    for p, (N, c) in moved:
        out.append('CARRIED  last=s%-3d  %-46s -> %s' % (N, p, c))
    for p, (N, c) in lost:
        out.append('LOST     last=s%-3d  %-46s -> (no copy in archive)' % (N, p))

    out += ['', '# SUMMARY',
            '#   sessions folded : %d' % len(rows),
            '#   current seal    : s%d, %d files' % (curN, len(cur)),
            '#   retired CARRIED : %d' % len(moved),
            '#   retired LOST    : %d' % len(lost), '']

    open('LINEAGE.txt', 'w').write('\n'.join(out) + '\n')
    print('LINEAGE.txt written')
    print('  sessions folded : %d' % len(rows))
    print('  current seal    : s%d, %d files' % (curN, len(cur)))
    print('  retired CARRIED : %d' % len(moved))
    print('  retired LOST    : %d  <-- F58.2' % len(lost))
    for p, (N, c) in lost:
        print('      LOST last=s%-3d  %s' % (N, p))
    return 0

if __name__ == '__main__':
    sys.exit(main())
