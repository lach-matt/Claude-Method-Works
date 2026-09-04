#!/usr/bin/env python3
"""reanchor.py — write a successor that resolves a predecessor's literal main-volume line numbers by CONTENT.

    python3 tools/reanchor.py --pred NAME --succ NAME2 --old-tree DIR [--keep N,N,...] [--write]

THE CLASS. A positional instrument pins a unit "measured by heading scan in this chat" as a literal —
`LO, HI = 8575, 8699`, `MAIN[9507 - 1]`, `range(9171, 9180)` — and reads the wrong site after any build that
moves a line above it (W-207, DEF-153N). The repair for each such literal is the same: replace the number by
the line it pointed at, found by its own text. This tool does that mechanically and prints what it did, so
the operator reviews every literal and the proof is left to `proveanchor.py`.

WHAT IT DOES. Every NUMBER token in the predecessor's CODE (never in a string or a comment) whose value lies
inside the old main member's line range, and is not on the --keep list, is looked up in the OLD main member
(the tree the golden was banked against): the text of that line becomes the anchor, `_L(text)`, when the
line is non-blank and unique in both the old member and the live one; otherwise the nearest unique non-blank
line within six lines becomes the anchor and the literal becomes `_L(text) + d`; otherwise the literal is
left and flagged MANUAL. `_L` is defined at the top of the successor and reads the main member from the
successor's own directory, so proveanchor's scratch tree and the live tree each resolve against their own
bytes. Nothing else in the predecessor changes: measurements, prose, the print format, the verdict.

WHAT IT CANNOT DECIDE, and why --keep exists. A number in the same range that is NOT a line — a Register entry
number, a cell count, a cap — would be anchored to the text of that line and drift with the volume; on the
old bytes it resolves to itself, so proveanchor would pass it. The operator reads the printed table and names
those on --keep. That is the blind spot DEF-153N records, stated here as the tool's contract.
"""
import argparse, io, os, re, sys, tokenize

MAIN = 'The_Method_1_6-2.md'
HELPER = '''
# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
'''

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--pred', required=True); ap.add_argument('--succ', required=True)
    ap.add_argument('--old-tree', required=True); ap.add_argument('--keep', default=''); ap.add_argument('--write', action='store_true')
    ap.add_argument('--live', default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'method', 'members'))
    a = ap.parse_args()
    keep = {int(x) for x in a.keep.split(',') if x.strip()}
    old = open(os.path.join(a.old_tree, MAIN), encoding='utf-8').read().split('\n')
    live = open(os.path.join(a.live, MAIN), encoding='utf-8').read().split('\n')
    src = open(os.path.join(a.live, a.pred + '.py'), encoding='utf-8').read()
    lines = src.split('\n')
    def uniq(t): return t.strip() != '' and old.count(t) == 1 and live.count(t) == 1
    edits = []  # (row, col_start, col_end, replacement, note)
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type != tokenize.NUMBER or not re.fullmatch(r'\d{4,5}', tok.string): continue
        v = int(tok.string)
        if v < 1000 or v > len(old): continue
        row, c0 = tok.start; _, c1 = tok.end
        ctx = lines[row - 1].strip()
        if v in keep: print('KEEP   %5d  %s' % (v, ctx[:100])); continue
        # entry-number contexts are never lines: a line that reads the Register by entry — rbody(N), ent[N],
        # entry(N), span(N), IDX[N], regtext — or seeds a generator, Random(N). Every literal below 1900 on
        # such a line is auto-kept and printed for review; a main-volume line below 1900 on the same line
        # would be missed, so the operator reads the table.
        if v < 1900 and re.search(r'rbody|ent\[|entry\(|span\(|Random\(|blk\(|regtext|IDX\[|\bR\[|REG\[|1701|1713', lines[row - 1]):
            print('AUTO-KEEP %5d  %s' % (v, ctx[:100])); continue
        if uniq(old[v - 1]):
            rep = '_L(%r)' % old[v - 1]; note = 'exact'
        else:
            rep = None
            for d in (1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6):
                j = v - d
                if 1 <= j <= len(old) and uniq(old[j - 1]):
                    rep = '_L(%r, %d)' % (old[j - 1], d); note = 'offset %+d from L%d' % (d, j); break
            if rep is None:
                print('MANUAL %5d  %s   (old line %r is not unique and no unique neighbour within 6)' % (v, ctx[:80], old[v - 1][:40])); continue
        print('ANCHOR %5d  %-9s old L%d %-50r  <- %s' % (v, note, v, old[v - 1][:48], ctx[:70]))
        edits.append((row, c0, c1, rep))
    if not a.write:
        print('\nDRY RUN: %d anchors. Re-run with --write (and --keep for any number above that is not a line).' % len(edits)); return
    for row, c0, c1, rep in sorted(edits, key=lambda e: (e[0], -e[1])):
        l = lines[row - 1]; lines[row - 1] = l[:c0] + rep + l[c1:]
    out = '\n'.join(lines)
    # header: after the shebang and the predecessor's leading comment block
    head = ('# %s.py — R3 (chat 153-R) — SUCCESSOR to %s.py, re-anchored by tools/reanchor.py: every main-volume line the\n'
            '# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was\n'
            '# banked against (%d anchors); nothing else changes. %s.py is seated and never edited in place (chat 68).\n'
            '# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.\n'
            '# PROVEANCHOR: pending\n') % (a.succ, a.pred, len(edits), a.pred)
    first_code = next(i for i, l in enumerate(lines) if l.strip() and not l.startswith('#'))
    out = '\n'.join(lines[:first_code]) + '\n' + head + HELPER + '\n'.join(lines[first_code:])
    if lines[0].startswith('#!'): pass
    open(os.path.join(a.live, a.succ + '.py'), 'w', encoding='utf-8').write(out)
    print('\nwritten %s.py with %d anchors' % (a.succ, len(edits)))

if __name__ == '__main__':
    main()
