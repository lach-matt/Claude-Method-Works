"""gate85.py -- s51. THE COLLAPSE CONDITION AS A GATE.
Locks DELIVERABLE-3 against nlchain.jsonl. Nothing fitted: the only number is -1/(2n^2),
the Coulomb eigenvalue at Z_eff=1, which enters as a DENOMINATOR.
Can-fail: perturb any expectation below and this must report FAIL.
usage: python3 gate85.py [gate]
"""
import json, math, sys
H = lambda n: -1.0/(2*n*n)
NL = lambda k: (int(k[:-1]), 'spdfg'.index(k[-1]))
rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
fails = []
def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<22} got {got}  want {want}")
    if not ok: fails.append(name)

# A. g channels are Z-independent and exactly hydrogenic (uncollapsed, delta=0)
for g, n in (('5g',5), ('6g',6), ('7g',7), ('8g',8)):
    vs = sorted({dict(rows[Z]['order'])[g] for Z in rows if g in dict(rows[Z]['order'])})
    chk(f'{g} pinned', len(vs), 1)
    if vs: chk(f'{g} hydrogenic', round(vs[0]-H(n), 5), 0.0)

# B. the f plateaus: n* flat at ~3.998 before collapse
ns = lambda D: 1.0/math.sqrt(-2*D)
for ch, zs in (('4f', (53,54,55,56)), ('5f', (85,86,87,88,89))):
    d = [round(ns(dict(rows[Z]['order'])[ch]), 2) for Z in zs]
    chk(f'{ch} plateau n*', d, [4.0]*len(zs))

# C. the transit: n* falls by more than 1.5 in one proton at exactly 57 and 90
tr = []
for ch, zs in (('4f', range(53,63)), ('5f', range(85,95))):
    for Z in zs:
        a, b = dict(rows[Z-1]['order']).get(ch), dict(rows[Z]['order']).get(ch)
        if a and b and ns(a)-ns(b) > 1.5: tr.append(Z)
chk('transit steps', sorted(tr), [57, 90])

# D. the tie-break: exercised+obeyed count, and no obeyed step is uncollapsed
holds, viol = [], []
for Z in range(2, 109):
    r = rows[Z]; e = tuple(r['ent_nl']); nl = sum(e); od = dict(r['order'])
    if any(NL(k)[0]+NL(k)[1] == nl and NL(k)[0] > e[0] for k in od):
        holds.append(r['D_ent']/H(e[0]))
    for k, v in od.items():
        if NL(k)[0]+NL(k)[1] == nl and NL(k)[0] < e[0] and v > r['D_ent']: viol.append(Z)
chk('tiebreak obeyed', len(holds), 94)
chk('tiebreak failed at', sorted(set(viol)), [57, 89, 90])
chk('no obeyed step kappa<2', [round(k,2) for k in holds if k < 2.0], [])

# E. the ordering clause, over the full 119 rows
ov = []
for Z in range(2, 121):
    r = rows[Z]; nl = sum(r['ent_nl'])
    for k, v in dict(r['order']).items():
        if sum(NL(k)) < nl and v > r['D_ent']: ov.append(Z)
chk('ordering failures', sorted(set(ov)), [])
chk('rows walked', len(rows), 119)

print()
print('GATE85: ' + ('PASS -- all clauses' if not fails else 'FAIL -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)