#!/usr/bin/env python3
# r2-ch13d.py — Phase R2, chat 79, segment 3: main Chapter 13 opening (L3508-3542).
# The section's claims are bibliographic rather than tower-computable; what is measurable is measured
# from the members themselves: the Register's extent and its kind counts, the numbering of the
# principles, the count of prime audits, and every site of the "one thousand six hundred and
# thirty-five" figure.  No wall-clock output.
import importlib.util, os, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)

REG = r2lib.read_member('The_Method_1_6___The_Register-2.md')
MAIN = r2lib.read_member('The_Method_1_6-2.md')

print('=== the Register, measured from the member ===')
heads = re.findall(r'^### ([0-9][0-9,\s]*)$', REG, re.M)
nums = sorted({int(n) for h in heads for n in re.findall(r'\d+', h)})
print('entry headings: %d   distinct entry numbers: %d   lowest %d   highest %d' % (
    len(heads), len(nums), nums[0], nums[-1]))
missing = [n for n in range(nums[0], nums[-1] + 1) if n not in set(nums)]
print('numbers in [%d, %d] with no heading: %d' % (nums[0], nums[-1], len(missing)))
print('extent sites "1 to NNNN" in the main volume:', sorted(set(re.findall(r'1 to (1\d{3})', MAIN))))

kinds = Counter()
for m in re.finditer(r'\*(a finding|a measurement|a withdrawal|a correction|prior art|a new protocol|an open question|a fault of mine)\*', REG):
    kinds[m.group(1)] += 1
print('kind tokens in the Register member:', dict(kinds.most_common()))

print()
print('=== L3514-3516: "one thousand six hundred and thirty-five WITHDRAWALS" ===')
for m in re.finditer(r'one thousand six hundred and thirty-five([^\n]{0,60})', MAIN):
    line = MAIN[:m.start()].count('\n') + 1
    print('   L%-6d ...one thousand six hundred and thirty-five%s' % (line, m.group(1).rstrip()))

print()
print('=== L3515: the principles, the prime audits, the protocols ===')
ps = sorted({int(p[1:]) for p in re.findall(r'\bP(?:[1-9]|1\d|2[0-3])\b', MAIN)})
print('P-numbers occurring in the main volume:', ps)
print('L233 states P1-P23 with P10, P12, P18 unassigned -> assigned count', 23 - 3)
print('unassigned per that statement present in text anyway:', [p for p in (10, 12, 18) if p in ps])
aud = re.findall(r'^## 3\. The ([a-z\-]+) prime audits', MAIN, re.M)
print('Chapter 3 heading says:', aud, '(sites %d)' % len(aud))
print('protocol sites in the main volume: "twenty-four protocols" ->',
      len(re.findall(r'twenty-four protocols', MAIN)))

print()
print('=== L3526: "E(Λ) = 0, verified at 976 cells in six languages" ===')
for m in re.finditer(r'six languages', MAIN):
    line = MAIN[:m.start()].count('\n') + 1
    seg = MAIN.split('\n')[line - 1].strip()
    print('   L%-6d %s' % (line, seg[:150]))

print()
print('=== L3531-3534 and L3537: where the four-scheme identity is actually proved ===')
for pat in (r'identical in all four schemes', r'jK, LS, LK and jj', r'four ROUTES to one object', r'2\.17'):
    for m in re.finditer(pat, MAIN):
        line = MAIN[:m.start()].count('\n') + 1
        print('   %-32s L%d' % (pat, line))
