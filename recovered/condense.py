#!/usr/bin/env python3
"""condense.py -- THE STANDING SEAL-TIME OPERATION (s58, M's ruling).

Runs ONCE, when a handoff is sealed.  Replaces: per-session manifests, per-session
verify scripts, and the practice of re-proving the whole chain at every open.

    python3 pack58/condense.py N            # dry run: report, change nothing
    python3 pack58/condense.py N --seal     # write LINEAGE line, fold scaffolding
    python3 pack58/condense.py N --check    # verify current tree against LINEAGE s-N

WHAT IT ENFORCES

  1. RETIREMENT IS DECLARED.  Every path sealed in session N-1 and absent at N must
     appear in pack<N>/RETIRE.txt with a reason.  An undeclared disappearance HALTS
     the seal.  Three files were lost silently before s58 (F58.2); that cannot recur.

  2. SCAFFOLDING DOES NOT ACCUMULATE.  MANIFEST-HANDOFF-*, verify*.sh and
     README-HANDOFF-* older than the current session are folded into LINEAGE.txt
     and removed from the seal.  Their root hashes remain checkable forever.

  3. rt/ IS NEVER SEALED.  It is a derived overlay, rebuilt from packs at every open.
     Any rt/ file that is NOT reconstructible from a sealed pack is reported --
     that is unsealed state masquerading as runtime.

  4. SHADOWING IS REPORTED.  Basenames present in more than one pack with differing
     content are listed with the pack that WINS the flat rt/ overlay.  The overlay
     resolves them silently; this makes the resolution visible.

The seal is GENERATED here and only here.  Never sed a verify script (F57.6).
"""
import sys, os, re, hashlib, shutil

SCAFFOLD = re.compile(r'^(MANIFEST-HANDOFF-\d+\.txt|verify\d*\.sh|README-HANDOFF-\d+\.md)$')
SKIP_DIR = ('rt', 'attic', '.git', '__pycache__')


def sha(fn):
    h = hashlib.sha256()
    with open(fn, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def tree(root='.'):
    """Every sealable file: packs + live root docs.  rt/ and attic/ excluded."""
    out = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIR and not d.startswith('.')]
        for f in fn:
            p = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/')
            if p.startswith('LOWDIN-HANDOFF') or p == 'LINEAGE.txt':
                continue
            out[p] = sha(os.path.join(root, p))
    return out


def root_hash(paths):
    body = '\n'.join('%s  %s' % (paths[p], p) for p in sorted(paths))
    return hashlib.sha256(body.encode()).hexdigest()


def lineage_rows(fn='LINEAGE.txt'):
    rows = {}
    if os.path.exists(fn):
        for ln in open(fn):
            m = re.match(r'^(\d+)\s+(\d+)\s+([0-9a-f]{64})\s*$', ln)
            if m:
                rows[int(m.group(1))] = (int(m.group(2)), m.group(3))
    return rows


def prev_paths(N):
    """Paths sealed at N-1: from that manifest if still present, else from attic."""
    for c in ('MANIFEST-HANDOFF-%d.txt' % (N - 1),
              'attic/MANIFEST-HANDOFF-%d.txt' % (N - 1)):
        if os.path.exists(c):
            out = {}
            for ln in open(c, encoding='utf-8', errors='replace'):
                p = ln.split()
                if len(p) >= 2:
                    out[p[-1].lstrip('./')] = p[0]
            return out
    return None


def shadow_report(paths):
    by = {}
    for p in paths:
        if p.startswith('pack'):
            by.setdefault(os.path.basename(p), []).append(p)
    out = []
    for bn, ps in sorted(by.items()):
        if len(ps) < 2:
            continue
        if len({paths[p] for p in ps}) < 2:
            continue
        win = max(ps, key=lambda x: int(re.match(r'pack(\d+)', x).group(1)))
        out.append((bn, len(ps), win.split('/')[0]))
    return out


def rt_unsealed(paths):
    if not os.path.isdir('rt'):
        return []
    sealed = set(paths.values())
    bad = []
    for dp, dn, fn in os.walk('rt'):
        dn[:] = [d for d in dn if d != '__pycache__']
        for f in fn:
            if f.endswith(('.pyc', '.so')) or '/receipts/' in dp + '/':
                continue
            p = os.path.join(dp, f)
            if sha(p) not in sealed:
                bad.append(p)
    return bad


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    N = int(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else '--dry'
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')

    paths = tree()
    rh = root_hash(paths)
    rows = lineage_rows()

    if mode == '--check':
        if N not in rows:
            print('CONDENSE-CHECK: s%d NOT IN LINEAGE -- cannot verify' % N); return 1
        n0, h0 = rows[N]
        ok = (rh == h0 and len(paths) == n0)
        print('CONDENSE-CHECK s%d: files=%d/%d root=%s' %
              (N, len(paths), n0, 'MATCH' if rh == h0 else 'MISMATCH'))
        if not ok:
            print('  sealed root : %s' % h0)
            print('  computed    : %s' % rh)
            return 1
        print('CONDENSE-CHECK: CLEAN')
        return 0

    prev = prev_paths(N)
    added = removed = changed = []
    if prev is not None:
        prev_live = {p: h for p, h in prev.items() if not SCAFFOLD.match(os.path.basename(p))}
        added = sorted(set(paths) - set(prev_live))
        removed = sorted(set(prev_live) - set(paths))
        changed = sorted(p for p in set(paths) & set(prev_live) if paths[p] != prev_live[p])

    declared = set()
    rf = 'pack%d/RETIRE.txt' % N
    if os.path.exists(rf):
        for ln in open(rf):
            ln = ln.strip()
            if ln and not ln.startswith('#'):
                declared.add(ln.split()[0])

    undeclared = [p for p in removed if p not in declared]
    shad = shadow_report(paths)
    orphans = rt_unsealed(paths)

    print('=== CONDENSE s%d ===' % N)
    print('  sealable files      : %d' % len(paths))
    print('  root                : %s' % rh)
    if prev is not None:
        print('  vs s%-3d  added=%d  changed=%d  removed=%d' %
              (N - 1, len(added), len(changed), len(removed)))
    print('  shadowed basenames  : %d' % len(shad))
    print('  rt/ unsealed files  : %d' % len(orphans))
    for p in orphans[:10]:
        print('      UNSEALED  %s' % p)
    if undeclared:
        print('  !!! UNDECLARED RETIREMENTS : %d' % len(undeclared))
        for p in undeclared[:20]:
            print('      %s' % p)
        print('  Declare each in %s with a reason, or restore it.' % rf)
        print('CONDENSE: HALTED.  Seal not written.')
        return 1

    if mode != '--seal':
        print('CONDENSE: dry run.  Nothing written.')
        return 0

    # --- fold scaffolding older than N into attic (unsealed, kept on disk) ---
    os.makedirs('attic', exist_ok=True)
    folded = 0
    for f in sorted(os.listdir('.')):
        m = SCAFFOLD.match(f)
        if not m:
            continue
        k = re.search(r'(\d+)', f)
        if k and int(k.group(1)) < N:
            shutil.move(f, os.path.join('attic', f))
            folded += 1

    paths = tree()
    rh = root_hash(paths)

    lines = open('LINEAGE.txt').read().rstrip('\n').split('\n') if os.path.exists('LINEAGE.txt') else []
    lines = [l for l in lines if not re.match(r'^%d\s+\d+\s+[0-9a-f]{64}' % N, l)]
    ins = max(i for i, l in enumerate(lines) if re.match(r'^\d+\s+\d+\s+[0-9a-f]{64}', l)) + 1
    lines.insert(ins, '%-6d %-7d %s' % (N, len(paths), rh))
    for p in sorted(declared):
        lines.insert(ins + 1, 'RETIRED  at=s%-3d  %s' % (N, p))
    open('LINEAGE.txt', 'w').write('\n'.join(lines) + '\n')

    # --- the ONE verify script.  Generated, never edited. ---
    open('verify.sh', 'w').write(
        '#!/bin/bash\n'
        '# GENERATED by pack58/condense.py.  Do not edit; regenerate.\n'
        '# Verifies the CURRENT seal only.  History is checkable via LINEAGE.txt.\n'
        'N=${1:-%d}\n'
        'python3 pack58/condense.py $N --check\n' % N)
    os.chmod('verify.sh', 0o755)

    print('  scaffolding folded  : %d -> attic/ (unsealed, on disk)' % folded)
    print('  sealed files        : %d' % len(paths))
    print('  root                : %s' % rh)
    print('CONDENSE: LINEAGE.txt + verify.sh written.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
