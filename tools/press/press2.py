"""Press a volume to a reading PDF, naming every press substitution that could not be applied.

build.py is a seated member and is never edited. Its SUBS table carries anchors that the volumes have
moved past (DOCKET D-31: five dead Register anchors; J-07: one anchor that moves with a date). sweep()
asserts every anchor occurs exactly once, so those volumes cannot be pressed at all. This wrapper keeps
build.py's transformations untouched and only DECLINES the anchors that no longer match, printing each
one, so a reading copy can be made and the reader knows exactly which press-time repairs are missing.
It is a reading copy, not the edition: the edition needs a build.py successor with the anchors repaired.
"""
import sys, importlib.util, os
spec = importlib.util.spec_from_file_location('press_build', '/home/user/Claude-Method-Works/method/members/build.py')
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
src, out, title, depth = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
strip = 'strip' in sys.argv[5:]
text = open(b.B + src, encoding='utf-8').read()
keep, dead, ambig = [], [], []
for a, r in b.SUBS.get(src, []):
    c = text.count(a)
    (keep if c == 1 else dead if c == 0 else ambig).append((a, r, c))
b.SUBS[src] = [(a, r) for a, r, _ in keep]
print('press anchors: %d applied, %d dead (0 matches), %d ambiguous (>1)' % (len(keep), len(dead), len(ambig)))
for a, r, c in dead + ambig:
    print('  DECLINED (%d matches): %s' % (c, a[:110].replace('\n', ' ')))
b.build(src, out + '.docx', title, toc_depth=depth, strip_contents=strip)
