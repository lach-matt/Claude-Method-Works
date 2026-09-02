#!/usr/bin/env python3
"""fill_value.py — L = fill(D_last) for every combination of the rulings the record leaves open.
Rungs (all one-parent envelopes, the tower's own style; caps declared):
  F_t   window on 2J,  half-width i = 2I_max            (hyperfine of the coupled final state)
  J_s   cap by k: 2J_s ≤ φ̂(k)                            (initial state's own J — sibling of J_c)
  F_s   window on 2J_s  — or, if J_c IS the source J, on 2J_c
  m_t, m_s   projections: 0 ≤ m ≤ 2F                     (field only)
Closed form over the joint (k, 2J_c, 2J) distribution of Λ13; box = box13 × Π value-counts.
"""
import importlib.util, math
from collections import Counter
s = importlib.util.spec_from_file_location('t', 'tower-1.py'); t = importlib.util.module_from_spec(s); s.loader.exec_module(t)
L13 = t.L13(); box13 = 47_775_744; assert len(L13) == 199_130
PHI = t.PHI; JMAX, JCMAX = 8, 5
joint = Counter((c[2], c[10], c[12]) for c in L13)
def win(j, i): return range(max(0, j - i), j + i + 1)
def chainT(j, i, proj): return sum((F + 1) if proj else 1 for F in win(j, i))
def chainS(mode, k, jc, i, proj):
    if mode == 'none': return 1
    if mode == 'F_s on J_c': return sum((F + 1) if proj else 1 for F in win(jc, i))
    return sum(sum((F + 1) if proj else 1 for F in win(js, i)) for js in range(0, PHI[k] + 1))
out = open('FILL-VALUE-RESULTS.txt', 'w')
def emit(x): print(x); out.write(x + '\n')
emit('  2I_max  I    source rungs        proj   D_last   value-counts                  cells(D_last)          L%')
for i in (14, 18):
    for mode in ('none', 'F_s on J_c', 'J_s + F_s'):
        for proj in (False, True):
            vcs = [JMAX + 1 + i] + ([] if mode == 'none' else ([JCMAX + 1 + i] if mode == 'F_s on J_c' else [JCMAX + 1, JCMAX + 1 + i]))
            if proj: vcs = vcs + [JMAX + 1 + i] + ([] if mode == 'none' else [JCMAX + 1 + i])
            cells = sum(n * chainT(j, i, proj) * chainS(mode, k, jc, i, proj) for (k, jc, j), n in joint.items())
            box = box13 * math.prod(vcs); D = 13 + len(vcs)
            emit(f'  {i:4d}  {i/2:4.1f}   {mode:16s}   {"yes" if proj else "no ":3s}     {D:2d}     {str(vcs):28s}  {cells:20,d}   {100*cells/box:.6f}')
emit(f'reference: fill13 = 0.416801%; joint (k,2J_c,2J) classes = {len(joint)}; Σ = {sum(joint.values()):,}')
out.close()
