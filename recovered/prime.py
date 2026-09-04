#!/usr/bin/env python3
"""prime.py -- PRIME CONTINUITY DIRECTIVE (§H.0), clauses 1, 2, 4.

Prints the STATE CARD. Nothing may be said about the state of this project that is not on the
card. Recollection has no standing; this file is the only admissible source.

    python3 prime.py          exit 0 clean | 1 real fault | 2 unreceipted write, unexplained
    python3 prime.py --fail   can-fail demonstration (plants a break in memory, must exit 1)

The card answers, from the record only:
    WHICH SESSION      read off the newest pack directory, not off memory
    SEALS              the sealed prefix of the chain, byte-compared
    CHAIN              rows held, Z range, entrant of the last rows
    BEYOND THE SEAL    rows this session added, each tested for continuity
    LEDGER             what ran in this session, from receipts -- covers lost tool results
"""
import sys, os, json, glob, subprocess

D = os.path.dirname(os.path.abspath(__file__))
os.chdir(D)
FAIL = '--fail' in sys.argv
bad = 0
unex = 0

print("=" * 72)
print("  STATE CARD -- prime.py.  Recollection has no standing; this does.")
print("=" * 72)

# ---- WHICH SESSION -------------------------------------------------------
packs = sorted(int(p[4:]) for p in os.listdir('..') if p.startswith('pack') and p[4:].isdigit())
print(f"  packs present     : pack{packs[0]} .. pack{packs[-1]}")
print(f"  session in progress: s{packs[-1]}   (read off the newest pack, not off memory)")

# ---- SEALS ---------------------------------------------------------------
seal = None
for n in sorted(packs, reverse=True):
    c = f'../pack{n}/nlchain.jsonl'
    if os.path.exists(c):
        seal = (n, c); break
S = {json.loads(l)['Z']: json.loads(l) for l in open(seal[1])}
L = {json.loads(l)['Z']: json.loads(l) for l in open('nlchain.jsonl')}
sz, lz = sorted(S), sorted(L)
print(f"  sealed chain      : pack{seal[0]}, {len(sz)} rows, Z={sz[0]}..{sz[-1]}")

for Z in sz:
    a = json.dumps(L.get(Z), sort_keys=True); b = json.dumps(S[Z], sort_keys=True)
    if FAIL and Z == sz[-1]:
        a = a.replace('"ok": true', '"ok": false', 1)
    if a != b:
        print(f"  *** SEALED PREFIX ALTERED AT Z={Z} -- THIS IS A REAL FAULT ***"); bad += 1

# ---- CHAIN ---------------------------------------------------------------
print(f"  live chain        : {len(lz)} rows, Z={lz[0]}..{lz[-1]}")
tail = ', '.join(f"{Z}:{L[Z]['ent']}" for Z in lz[-5:])
print(f"  last five entrants: {tail}")

# ---- BEYOND THE SEAL -----------------------------------------------------
extra = [Z for Z in lz if Z not in S]
if not extra:
    print("  beyond the seal   : none")
else:
    import nlchain as NC
    print(f"  beyond the seal   : {len(extra)} row(s) {extra}")
    for Z in extra:
        want = ''.join(f"{n}{'spdfg'[l]}{k}" for n, l, k in NC.cfg_from_chain(Z - 1, L))
        ok = (want == L[Z]['ref_cfg'])
        print(f"      Z={Z:<4} ent={L[Z]['ent']:<3} rung={L[Z]['rungs']} "
              f"{'CONTINUOUS' if ok else '*** BREAK -- REAL FAULT ***'}")
        bad += 0 if ok else 1

# ---- LEDGER --------------------------------------------------------------
led = 'SESSION-LEDGER.tsv'
rows = []
if os.path.exists(led):
    rows = [l.rstrip('\n').split('\t') for l in open(led)][1:]
run_now = []
for r in glob.glob('receipts/*'):
    if not os.path.exists(f'{r}/rc'):
        p = open(f'{r}/pid').read().strip() if os.path.exists(f'{r}/pid') else ''
        alive = subprocess.call(['kill', '-0', p], stderr=subprocess.DEVNULL) == 0 if p else False
        run_now.append((os.path.basename(r), p, alive))
print(f"  ledger            : {len(rows)} completed job(s) this session")
for r in rows[-6:]:
    print(f"      {r[1]:<16} rc={r[2]:<3} {r[0][11:19]}->{r[3][11:19]}  {r[4][:44]}")
for t, p, alive in run_now:
    print(f"      {t:<16} {'RUNNING' if alive else 'VANISHED -- read its log'} pid={p}")
    unex += 0 if alive else 1

# ---- VERDICT -------------------------------------------------------------
print("-" * 72)
if bad:
    print(f"  VERDICT: {bad} REAL FAULT(S). Register against the OBJECT.")
elif unex:
    print(f"  VERDICT: CLEAN chain; {unex} job(s) ended without an rc. Read the log, do not recompute.")
else:
    print("  VERDICT: CLEAN. Speak only from this card.")
print("=" * 72)
sys.exit(1 if bad else (2 if unex else 0))
