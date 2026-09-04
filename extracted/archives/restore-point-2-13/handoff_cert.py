#!/usr/bin/env python3
"""§H.8 — the handoff certificate. Seven clauses, each capable of failing.

Usage:  python3 handoff_cert.py <bank.tar.gz> <bridge.md>
Prints the seven with evidence and exits non-zero if any fails.
"""
import csv, os, re, subprocess, sys, tarfile

WORK = os.path.dirname(os.path.abspath(__file__))
BANK = sys.argv[1] if len(sys.argv) > 1 else None
BRIDGE = sys.argv[2] if len(sys.argv) > 2 else None
res = []

def clause(cid, name, ok, evidence):
    res.append((cid, name, ok, evidence))

# C1 — both gates pass
def run(script):
    p = subprocess.run(['timeout', '900', 'python3', script], cwd=WORK,
                       capture_output=True, text=True)
    return p.stdout + p.stderr
try:
    a = run('The_Method_1_6_audits.py'); r = run('roundtrip.py')
    ok = ('ALL TWENTY-FIVE PASS' in a) and ('5 of 5 round-trip' in r)
    n_fail = r.count('FAIL')
    clause('C1', 'both gates pass', ok,
           f"audits: {'ALL TWENTY-FIVE PASS' if 'ALL TWENTY-FIVE PASS' in a else 'NOT CLEAN'} · "
           f"round-trip: {'5 of 5' if '5 of 5 round-trip' in r else f'{n_fail} FAIL'}")
except Exception as e:
    clause('C1', 'both gates pass', False, f'gate run errored: {e}')

# C2 — register rebuilds, count read not recited
try:
    p = subprocess.run(['timeout', '900', 'python3', 'register_gen.py'], cwd=WORK,
                       capture_output=True, text=True)
    m = re.search(r'([0-9,]+) entries', p.stdout)
    held = open(os.path.join(WORK, 'REGISTER.md'), encoding='utf-8').read()
    mh = re.search(r'([0-9,]+) entries', held)
    ok = bool(m and mh and m.group(1) == mh.group(1)) and p.returncode == 0
    clause('C2', 'register rebuilds; count read from it', ok,
           f"generated {m.group(1) if m else '?'} · held {mh.group(1) if mh else '?'}")
except Exception as e:
    clause('C2', 'register rebuilds; count read from it', False, str(e))

# C3 — generated artefacts regenerate identically (round-trip already tests it; report per file)
try:
    r = run('roundtrip.py')
    per = re.findall(r'(\S+\.md)\s+(PASS|FAIL)', r)
    ok = all(v == 'PASS' for _, v in per) and len(per) >= 5
    clause('C3', 'every generated artefact regenerates', ok,
           ' · '.join(f'{k} {v}' for k, v in per) or 'no artefacts reported')
except Exception as e:
    clause('C3', 'every generated artefact regenerates', False, str(e))

# C4 — the bank lists at the expected file count
try:
    tree = sum(1 for root, dirs, files in os.walk(WORK)
               for f in files
               if '.zeno' not in root and '__pycache__' not in root)
    if BANK and os.path.exists(BANK):
        with tarfile.open(BANK) as t:
            inbank = sum(1 for m in t.getmembers() if m.isfile())
        ok = inbank >= tree
        clause('C4', 'bank lists at the tree count', ok,
               f'tree {tree} files · bank {inbank} files')
    else:
        clause('C4', 'bank lists at the tree count', False, f'bank not found: {BANK}')
except Exception as e:
    clause('C4', 'bank lists at the tree count', False, str(e))

# C5 — transcripts and journal inside the bank
try:
    if BANK and os.path.exists(BANK):
        with tarfile.open(BANK) as t:
            names = t.getnames()
        tx = [n for n in names if '/transcripts/' in n or n.startswith('./transcripts/')]
        has_journal = any(n.endswith('journal.txt') for n in tx)
        ok = len(tx) >= 2 and has_journal
        clause('C5', 'transcripts and journal in the bank', ok,
               f'{len([n for n in tx if n.endswith(".txt")])} files, journal {"yes" if has_journal else "NO"}')
    else:
        clause('C5', 'transcripts and journal in the bank', False, 'no bank')
except Exception as e:
    clause('C5', 'transcripts and journal in the bank', False, str(e))

# C6 — the bridge names every open thread with an owner
try:
    b = open(BRIDGE, encoding='utf-8').read() if BRIDGE else ''
    # A thread is found by its NUMBER ALONE. Owner is tested separately and per
    # thread — otherwise the clause's stated failure mode (a thread with no owner)
    # is undetectable, because an ownerless thread simply fails to match at all.
    # R 1671: C6 passed on 3 of 5 threads; T6 and T7 end in '?' not '.'.
    blocks = re.findall(r'\*\*T(\d+)\s*·\s*(.*?)\*\*(.*?)(?=\n\*\*T\d+\s*·|\Z)', b, re.S)
    owned = []
    for n, head, body in blocks:
        m = re.search(r'Owner:\s*([^.*]+)', head + body)
        owned.append((n, m.group(1).strip() if m else None))
    ok = len(owned) > 0 and all(o for _, o in owned)
    clause('C6', 'open threads carry owners', ok,
           f'{len(owned)} threads · ' + ' · '.join(
               f'T{n} → {o or "NO OWNER"}' for n, o in owned) or 'none found')
except Exception as e:
    clause('C6', 'open threads carry owners', False, str(e))

# C7 — the bridge names what is unread
try:
    b = open(BRIDGE, encoding='utf-8').read() if BRIDGE else ''
    d = open(os.path.join(WORK, 'DIGEST.md'), encoding='utf-8').read()
    ok = ('Unread' in b or 'unread' in b) and ('NOT READ' in d or 'not read' in d or 'Unread' in d)
    clause('C7', 'the unread is named', ok,
           f"bridge {'names it' if 'nread' in b else 'SILENT'} · digest {'names it' if 'ot read' in d.lower() or 'nread' in d else 'SILENT'}")
except Exception as e:
    clause('C7', 'the unread is named', False, str(e))

print('=== §H.8 HANDOFF CERTIFICATE ===')
for cid, name, ok, ev in res:
    print(f'  {cid}  {"PASS" if ok else "FAIL"}  {name}')
    print(f'        {ev}')
passed = sum(1 for *_, ok, _ in [(c, n, o, e) for c, n, o, e in res] if ok)
print(f'\n{passed} of {len(res)} clauses pass')
if passed != len(res):
    print('HANDOFF INCOMPLETE — a session that ends without a certificate has not ended.')
    sys.exit(1)
print('HANDOFF COMPLETE.')
