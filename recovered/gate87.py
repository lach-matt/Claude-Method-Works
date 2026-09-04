"""gate87.py -- s53. CLAUSE 3 SCORED: the c=1e6 walk against PREDICTION-NONREL-CINF.md.

WRITTEN BEFORE THE c=1e6 CHAIN WAS READ. The ordering-failure and tie-break definitions
below are LIFTED VERBATIM from the sealed gate85.py (sections D and E) -- R 1671: an
instrument built to check a sealed result must be reconciled against the sealed one.

F53.2 IS ENFORCED HERE, NOT NARRATED. The sealed chain is 'chain' mode at all 119 rows;
cinf.py walks in RESTART mode (reference = OBSERVED config(Z-1)). At 34 of 107 steps the
two reference configurations DIFFER, so at those steps a change of entrant is NOT
attributable to c. This gate partitions every disagreement into CLEAN (reference configs
identical -- c is the only difference) and CONFOUNDED (they differ -- attribution
requires a c=137.035999 restart control at that Z). It REFUSES to score NR-4 until every
confounded step carries a control row.

usage: python3 gate87.py <cinf.jsonl> [control.jsonl]
"""
import json, math, sys, os

CINF = sys.argv[1] if len(sys.argv) > 1 else '/tmp/cinf.jsonl'
CTRL = sys.argv[2] if len(sys.argv) > 2 else None

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../rt')
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../rt')
import ground as G, nlchain as NC

H  = lambda n: -1.0/(2*n*n)
NL = lambda k: (int(k[:-1]), 'spdfg'.index(k[-1]))
ns = lambda D: 1.0/math.sqrt(-2*D)

sealed = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
cinf   = {d['Z']: d for d in map(json.loads, open(CINF))}
ctrl   = {d['Z']: d for d in map(json.loads, open(CTRL))} if CTRL and os.path.exists(CTRL) else {}

fails = []
def chk(name, got, want):
    ok = (got == want)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<28} got {got}  want {want}")
    if not ok: fails.append(name)

ZS = [Z for Z in range(2, 109) if Z in cinf]
print(f"c=1e6 rows present: {len(ZS)}  (Z={min(ZS) if ZS else '-'}..{max(ZS) if ZS else '-'})")
if len(ZS) != 107:
    print("  INCOMPLETE CHAIN -- clauses are scored over the rows present and the")
    print("  denominator is stated. A partial chain does not close clause 3.")

# ---- NR-1  ORDERING FAILURES (gate85 section E, verbatim) -------------------
ov = []
for Z in ZS:
    r = cinf[Z]; nl = sum(r['ent_nl'])
    for k, v in dict(r['order']).items():
        if sum(NL(k)) < nl and v > r['D_ent']: ov.append(Z)
chk('NR-1 ordering failures', sorted(set(ov)), [])

# ---- NR-2  TIE-BREAK (gate85 section D, verbatim) ---------------------------
holds, viol = [], []
for Z in ZS:
    r = cinf[Z]; e = tuple(r['ent_nl']); nl = sum(e); od = dict(r['order'])
    if any(NL(k)[0]+NL(k)[1] == nl and NL(k)[0] > e[0] for k in od):
        holds.append(r['D_ent']/H(e[0]))
    for k, v in od.items():
        if NL(k)[0]+NL(k)[1] == nl and NL(k)[0] < e[0] and v > r['D_ent']: viol.append(Z)
chk('NR-2 tiebreak failed at', sorted(set(viol)), [57, 89, 90])
print(f"        tiebreak exercised+obeyed: {len(holds)}  (sealed: 94 over 107 rows)")

# ---- NR-5  g CHANNELS UNMOVED ----------------------------------------------
gmax = 0.0
for Z in ZS:
    a, b = dict(sealed[Z]['order']), dict(cinf[Z]['order'])
    for k in a:
        if k.endswith('g') and k in b: gmax = max(gmax, abs(a[k]-b[k]))
chk('NR-5 g channels |dD|<=1e-5', round(gmax, 8) <= 1e-5, True)
print(f"        max g shift: {gmax:.2e}")

# ---- NR-3  DEPTHS MOVE, ORDER DOES NOT -------------------------------------
agg = {}
for Z in ZS:
    a, b = dict(sealed[Z]['order']), dict(cinf[Z]['order'])
    sh = [abs(a[k]-b[k]) for k in a if k in b and not k.endswith('g')]
    if sh: agg[Z] = max(sh)
lo = [Z for Z in agg if Z < 30]
chk('NR-3 max |dD| below 1 mHa for Z<30', max((agg[Z] for Z in lo), default=0.0) < 1e-3, True)
if agg:
    zmax = max(agg, key=lambda z: agg[z])
    chk('NR-3 largest shift at Z>80', zmax > 80, True)
    print(f"        largest |dD| {agg[zmax]:.4f} Ha at Z={zmax}")

# ---- F53.2  ATTRIBUTION PARTITION ------------------------------------------
clean, confounded = [], []
for Z in ZS:
    obs = sorted(map(tuple, G.expand(Z-1)))
    ch  = sorted(map(tuple, NC.cfg_from_chain(Z-1, sealed)))
    same_ref = (obs == ch)
    if cinf[Z]['ent'] != sealed[Z]['ent']:
        (clean if same_ref else confounded).append(Z)
print(f"  entrant differs from sealed chain at: clean {clean}  confounded {confounded}")

# ---- NR-4  ANY ENTRANT CHANGE IS AT Z>=72 ----------------------------------
resolved = [Z for Z in confounded if Z in ctrl]
unresolved = [Z for Z in confounded if Z not in ctrl]
attributed = list(clean) + [Z for Z in resolved if ctrl[Z]['ent'] != cinf[Z]['ent']]
if unresolved:
    print(f"  [HELD] NR-4 NOT SCORED -- {len(unresolved)} confounded step(s) lack a")
    print(f"         c=137.035999 restart control: {unresolved}")
    fails.append('NR-4-UNRESOLVED')
else:
    chk('NR-4 all c-changes at Z>=72', all(Z >= 72 for Z in attributed), True)
    print(f"        c-attributed entrant changes: {sorted(attributed)}")

# ---- NR-6  ok SCORE ---------------------------------------------------------
okv = [Z for Z in ZS if cinf[Z]['ok'] is False]
print(f"  ok column at c=1e6: {len(ZS)-len(okv)}/{len(ZS)}   sealed 96/107")
chk('NR-6 ok within +/-3 of 96', abs((len(ZS)-len(okv)) - 96) <= 3, True)
print("  [NOT SCOREABLE] NR-6 cfg half: the sealed cfg column is built from the CHAIN's")
print("  own choices; a restart walk has no such column. Scoring it would be a rewording.")

print()
print('GATE87: ' + ('PASS -- all scoreable clauses' if not fails else 'FAIL/HELD -- ' + ', '.join(fails)))
sys.exit(1 if fails else 0)
