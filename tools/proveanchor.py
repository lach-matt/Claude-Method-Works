#!/usr/bin/env python3
"""proveanchor.py — prove a re-anchored successor reproduces its predecessor on the OLD bytes.

    python3 tools/proveanchor.py --old-bundle PATH [--old-bundle PATH ...] \
                                 --pred NAME --succ NAME2 [--pred ... --succ ...]

WHY. R3's first volume change mis-targeted every instrument that hard-codes a main-volume line
number, so each needs a successor that resolves its site by content instead. Re-anchoring is the
risky kind of change: altering how an instrument finds its site can silently alter WHAT it measures,
which is precisely G0c -- never change an instrument to make a discrepancy disappear.

THE GUARD. A successor is trustworthy only if, run against the corpus as it stood BEFORE the shift,
it reproduces its predecessor's banked golden **byte-exact**. Then the re-anchoring provably changed
addressing and nothing else, and its output on the new corpus can be trusted. If it cannot reproduce
the old reading on the old bytes, the re-anchor is wrong -- or the difference is a finding, and
either way it is not a re-bank.

HOW. The old bundles are extracted to a scratch tree and `/home/claude/members` is pointed at it for
the duration, because seated instruments hard-code that path. The live tree is never modified: the
symlink is restored on exit, including on failure. Nothing is written into method/.

Exit 0 only if every pair reproduces byte-exact.
"""
import argparse, hashlib, os, pathlib, re, shutil, subprocess, sys, tempfile

MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
CLAUDE = pathlib.Path('/home/claude/members')
md5 = lambda b: hashlib.md5(b).hexdigest()


def extract(bundles, dest):
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    for b in bundles:
        raw = pathlib.Path(b).read_bytes()
        buf = bytearray(raw)
        found = list(MEMBER.finditer(raw))
        if not found:
            sys.exit(f'{b}: no members matched — bundle form changed')
        for m in found:
            (dest / m.group(1).decode()).write_bytes(m.group(2))
            buf[m.start(2):m.start(2) + len(m.group(2))] = m.group(2)
            n += 1
        if md5(bytes(buf)) != md5(raw):
            sys.exit(f'{b}: splice guard failed')
        print(f'  extracted {len(found)} members from {pathlib.Path(b).name}  md5 {md5(raw)}')
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--old-bundle', action='append', required=True)
    ap.add_argument('--pred', action='append', required=True)
    ap.add_argument('--succ', action='append', required=True)
    ap.add_argument('--timeout', type=int, default=270)
    a = ap.parse_args()
    if len(a.pred) != len(a.succ):
        ap.error('--pred and --succ must pair up')

    live = pathlib.Path(os.readlink(CLAUDE)) if CLAUDE.is_symlink() else None
    if live is None:
        sys.exit('/home/claude/members is not a symlink — run method/bin/stage-gate first')

    scratch = pathlib.Path(tempfile.mkdtemp(prefix='proveanchor-'))
    old = scratch / 'members'
    print(f'old tree: {old}')
    total = extract(a.old_bundle, old)
    print(f'  {total} members\n')
    # Prints & Proofs is not a member: three instruments open it at members/../ and two at /home/claude/, as
    # stage-gate links it. The scratch tree gets the same links, or those instruments fail for a missing file
    # and the failure would be misread as a re-anchor that changed the measurement.
    pp = pathlib.Path('/home/claude/PP_The_Method_1_6.md')
    if pp.exists():
        for where in (scratch / 'PP_The_Method_1_6.md', old / 'PP_The_Method_1_6.md'):
            if not where.exists(): where.symlink_to(pp.resolve())

    # The successors are not in the old bundles; copy them in from the live tree.
    for s in a.succ:
        src = live / f'{s}.py'
        if not src.exists():
            shutil.rmtree(scratch, ignore_errors=True)
            sys.exit(f'{s}.py not found in the live tree')
        shutil.copy2(src, old / f'{s}.py')

    failures = []
    try:
        CLAUDE.unlink()
        CLAUDE.symlink_to(old)
        for pred, succ in zip(a.pred, a.succ):
            gold = old / f'{pred}.out'
            if not gold.exists():
                failures.append((succ, f'no banked {pred}.out in the old bundles')); continue
            p = subprocess.run(['python3', f'{succ}.py'], cwd=old, capture_output=True, timeout=a.timeout)
            if p.returncode != 0:
                failures.append((succ, f'exit {p.returncode}: {p.stderr.decode()[-200:]}')); continue
            got, want = p.stdout.decode('utf-8', 'replace'), gold.read_text(encoding='utf-8')
            if got == want:
                print(f'PROVED     {succ} reproduces {pred}.out byte-exact on the old bytes')
            else:
                failures.append((succ, f'differs from {pred}.out ({md5(got.encode())[:8]} vs {md5(want.encode())[:8]})'))
    finally:
        CLAUDE.unlink(missing_ok=True)
        CLAUDE.symlink_to(live)
        print(f'\nrestored /home/claude/members -> {live}')
        shutil.rmtree(scratch, ignore_errors=True)

    for s, why in failures:
        print(f'NOT PROVED {s}: {why}')
    if failures:
        print('\nA successor that cannot reproduce its predecessor on the old bytes is not a re-anchor.')
        sys.exit(1)
    print('\nALL PROVED')


if __name__ == '__main__':
    main()
