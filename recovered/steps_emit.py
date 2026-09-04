#!/usr/bin/env python3
"""steps_emit.py -- emit the step table that brack.py builds internally.

The candidate/rival construction is COPIED VERBATIM from brack.py lines 8-29 so
that the emitted table is the project's own object and not a reconstruction.
Source of configurations: ground.py (NIST ASD 5.12, DOI 10.18434/T4W30F,
retrieved 2026-08-09, register 1306) -- read, not computed.

Emits one row per (step, rival):
    Z, element, entrant_n, entrant_l, entrant_p, rival_n, rival_l, rival_p, dn
where p = n - l - 1 is the node count and dn = n_rival - n_entrant.
"""
import sys, math, csv
sys.path.insert(0, "/home/claude/bank")
import ground as G

L = "spdfg"
def cap(l): return 2 * (2 * l + 1)

rows = []
steps = 0
for Z in range(3, 109):
    pr = {(n, l): o for n, l, o in G.expand(Z - 1)}
    cu = {(n, l): o for n, l, o in G.expand(Z)}
    got = [k for k in cu if cu[k] > pr.get(k, 0)]
    if len(got) != 1:
        continue
    gn, gl = got[0]
    cand = []
    for l in range(5):
        for n in range(l + 1, 9):
            if pr.get((n, l), 0) >= cap(l):
                continue
            cand.append((n, l))
            if pr.get((n, l), 0) == 0:
                break
    if (gn, gl) not in cand or len(cand) < 2:
        continue
    steps += 1
    gp = gn - gl - 1
    for (n, l) in cand:
        if (n, l) == (gn, gl):
            continue
        rows.append(dict(Z=Z, element=G.GROUND[Z][0],
                         entrant_n=gn, entrant_l=gl, entrant_subshell=f"{gn}{L[gl]}",
                         entrant_p=gp,
                         rival_n=n, rival_l=l, rival_subshell=f"{n}{L[l]}",
                         rival_p=n - l - 1, dn=n - gn))

with open("/home/claude/out/STEPS-2_13.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

print(f"steps emitted      : {steps}")
print(f"(step,rival) rows  : {len(rows)}")
print(f"distinct Z         : {len(set(r['Z'] for r in rows))}")
print(f"node counts seen   : {sorted(set([r['entrant_p'] for r in rows] + [r['rival_p'] for r in rows]))}")
