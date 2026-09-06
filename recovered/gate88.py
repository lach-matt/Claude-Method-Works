"""gate88.py -- s53. CLAUSE 3 LOCKED.
Scores the c=137.035999 restart control against PREDICTION-CTRL137.md and the
chained-reference c=1e6 induction against PREDICTION-INDUCTION.md, both filed before
their first row. Can-fail: flip any expectation below and this must report FAIL.
usage: python3 gate88.py [ctrl.jsonl] [induct.jsonl]
"""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, '..', 'rt')); os.chdir(os.path.join(D, '..', 'rt'))
import ground as G, nlchain as NC

NLf = lambda k: (int(k[:-1]), 'spdfg'.index(k[-1]))
CT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ctrl137.jsonl'
IN = sys.argv[2] if len(sys.argv) > 2 else '/tmp/induct.jsonl'

sealed = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
cinf   = {d['Z']: d for d in map(json.loads, open(os.path.join(D, 'cinf.jsonl')))}
ctrl   = {d['Z']: d for d in map(json.loads, open(CT))}
ind    = {d['Z']: d for d in map(json.loads, open(IN))}

CONF = [Z for Z in range(2, 109)
        if sorted(map(tuple, G.expand(Z-1))) != sorted(map(tuple, NC.cfg_from_chain(Z-1, sealed)))]
CLEAN = [Z for Z in range(2, 109) if Z not in CONF]

fails = []
def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<34} got {got}  want {want}")
    if not ok: fails.append(name)

chk('partition sizes', (len(CLEAN), len(CONF)), (73, 34))

# ---- CT-1  the 11 disagreements are reference-borne, not c-borne -------------
dis = sorted(Z for Z in CLEAN + CONF if cinf[Z]['ent'] != sealed[Z]['ent'])
chk('CT disagreeing steps', dis, [25, 30, 47, 48, 60, 61, 62, 71, 80, 103, 104])
chk('CT-1 ctrl==cinf entrant', sum(1 for Z in dis if ctrl[Z]['ent'] == cinf[Z]['ent']), len(dis))
chk('CT-1 c-attributed changes', [Z for Z in dis if ctrl[Z]['ent'] != cinf[Z]['ent']], [])
chk('CT-4 control rungs', sorted({r for c in ctrl.values() for r in c['rungs']}), [0])

# ---- the 73 clean steps: c=1e6 restart vs c=137 chain, same reference --------
chk('clean-subset entrant differences', [Z for Z in CLEAN if cinf[Z]['ent'] != sealed[Z]['ent']], [])

# ---- IN-1  DECISIVE: chained reference at c=1e6 reproduces the sealed entrant -
have = [Z for Z in CONF if Z in ind]
chk('IN rows present', len(have), 34)
bad = [Z for Z in have if ind[Z]['ent'] != sealed[Z]['ent']]
chk('IN-1 chained-ref c=1e6 == sealed', bad, [])

# ---- IN-2  no ordering failure at any induction row -------------------------
ov = []
for Z in have:
    r = ind[Z]; nl = sum(r['ent_nl'])
    for k, v in dict(r['order']).items():
        if sum(NLf(k)) < nl and v > r['D_ent']: ov.append(Z)
chk('IN-2 ordering failures', sorted(set(ov)), [])

# ---- IN-3  no tie-break failure inside this set ------------------------------
tv = []
for Z in have:
    r = ind[Z]; e = tuple(r['ent_nl']); nl = sum(e)
    for k, v in dict(r['order']).items():
        if NLf(k)[0]+NLf(k)[1] == nl and NLf(k)[0] < e[0] and v > r['D_ent']: tv.append(Z)
chk('IN-3 tiebreak failures', sorted(set(tv)), [])

# ---- IN-5  every row at rung 0 ----------------------------------------------
chk('IN-5 rungs', sorted({r for x in ind.values() for r in x['rungs']}), [0])

# ---- THE INDUCTION, STATED AS THE GATE IT IS --------------------------------
covered = sorted(set(CLEAN) | set(have))
chk('induction covers Z=2..108', covered == list(range(2, 109)), True)
closed = (not bad) and not [Z for Z in CLEAN if cinf[Z]['ent'] != sealed[Z]['ent']]
chk('CLAUSE 3 INDUCTION CLOSES', closed, True)

print()
print('GATE88: ' + ('PASS -- all clauses' if not fails else 'FAIL -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)
