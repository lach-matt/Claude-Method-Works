#!/usr/bin/env python3
"""AMENDMENT 2 PAIR WRITER (Ruling 46 / Ruling 61).

Appends (anchor, replacement) pairs to build.py's SUBS list for one volume.

WHY THIS EXISTS AS A TREE MEMBER: chats 44 and 45 kept this writer in
/home/claude/work, which is scratch and does not survive a session. Chat 46's
handoff instructed the next session to "reuse it"; it was gone. A tool named in
a handoff must be a bundle member or it is not a tool, it is a memory.

CONTRACT
  amd2_write.py PAIRSFILE [--write]
PAIRSFILE is a python literal: {'<volume filename>': [(anchor, replacement), ...]}

GUARANTEES, in this order, before anything is written:
  1. every anchor is asserted exactly once against the RUNNING press text,
     applied in list order, i.e. sweep() is simulated in position (G0q);
  2. the append anchor in build.py is asserted exactly once (G0f);
  3. only then is build.py opened for writing.
No source .md is ever opened for writing. Register stays append-only.
"""
import sys, os, re, ast, importlib.util

B = os.path.dirname(os.path.abspath(__file__))

def load_build():
    spec = importlib.util.spec_from_file_location('b', os.path.join(B, 'build.py'))
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m

def press(m, src):
    """The text as the reader meets it: source with every existing pair applied."""
    t = open(os.path.join(B, src), encoding='utf-8').read()
    return m.sweep(src, t)

def validate(m, new):
    """Simulate sweep() in position with the new pairs appended. Returns report."""
    ok = True
    for src, pairs in new.items():
        t = open(os.path.join(B, src), encoding='utf-8').read()
        seq = list(m.SUBS.get(src, [])) + list(pairs)
        for i, (a, b) in enumerate(seq):
            n = t.count(a)
            tag = 'existing' if i < len(m.SUBS.get(src, [])) else 'NEW'
            if n != 1:
                ok = False
                print(f'  FAIL [{i}] {tag} count={n} :: {a[:72]!r}')
            t = t.replace(a, b)
        print(f'  {src}: {len(seq)} pairs applied in position, '
              f'{len(t.splitlines())} split-lines')
    return ok

def append(new):
    p = os.path.join(B, 'build.py')
    T = open(p, encoding='utf-8').read()
    for src, pairs in new.items():
        # append at the END of this volume's list: the list closes with " ],\n"
        # followed by the next key, or by "}" if it is the last volume.
        key = f" '{src}': [\n"
        assert T.count(key) == 1, f'volume key not unique: {src}'
        start = T.index(key) + len(key)
        end = T.index('\n ],\n', start)
        block = ''.join(
            '  (%r,\n   %r),\n' % (a, b) for a, b in pairs)
        T = T[:end + 1] + block + T[end + 1:]
    open(p, 'w', encoding='utf-8').write(T)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    new = ast.literal_eval(open(sys.argv[1], encoding='utf-8').read())
    m = load_build()
    print('SUBS before:', sum(len(v) for v in m.SUBS.values()))
    print('--- sequential validation (G0q) ---')
    if not validate(m, new):
        print('VALIDATION FAILED. NOTHING WRITTEN.')
        sys.exit(1)
    print('all pairs assert exactly once in position.')
    if '--write' not in sys.argv:
        print('DRY RUN. pass --write to append.')
        return
    append(new)
    m2 = load_build()
    print('SUBS after :', sum(len(v) for v in m2.SUBS.values()))
    print('--- revalidation from disk ---')
    for src in m2.SUBS:
        t = open(os.path.join(B, src), encoding='utf-8').read()
        m2.sweep(src, t)
    print('press clean, 0 raises.')

if __name__ == '__main__':
    main()

