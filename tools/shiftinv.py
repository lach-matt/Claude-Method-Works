#!/usr/bin/env python3
"""shiftinv.py — triage a moved golden: shift-invariant, or a finding, or a literal read.

    python3 tools/shiftinv.py NAME [NAME ...]        run each instrument now, diff against its banked golden
    python3 tools/shiftinv.py --all                  every seated golden

WHY. After a build that moves lines, every golden that prints a line reference moves. `close_rebank.py`
re-banks by running and does not decide whether the movement is a finding; `shiftcheck.py` decides it
for a DECLARED shift, and the estate's drift predates any one declaration (DEF-153J). This tool asks the
question the other way round: strip every digit run from both outputs and compare the WORDS. What is
left is the residual — lines whose words changed — and beside it every integer that changed by
something other than a plausible line shift. Three verdicts, none of them a re-bank on its own:

  SHIFT     no residual words, no non-shift integer: the output moved with the volume. Re-bank only after
            reading the instrument for a literal line index (a literal read whose content moved by a
            whole line prints the same SHAPE; DEF-153N's caveat — the mask cannot see it).
  COUNT     an integer below 1,000 changed: a count moved. Explain it by name (an appended entry, a
            repaired row) before re-banking, or it is a finding.
  TEXT      words changed: the instrument reads different content — a positional window, or the
            volume changed under it. A reading, never a re-bank.

Runs each instrument through gate.py's own command table (SPECIAL), in members/, writing nothing.
W-234 (Q5 pass 6): `--all` used to enumerate only NAME.out with a NAME.py beside it, so the goldens gate.py runs
by a SPECIAL command with no .py of their own name (r2-tools-constants, extent) were never triaged, and a CORE
golden stayed stale from BUILD104 to BUILD110. `--all` now walks every NAME.out that has a .py or a SPECIAL entry,
and `--list` prints that set without running anything
into method/. Fresh outputs go to a scratch directory named on stderr.
"""
import os, re, subprocess, sys, difflib, importlib.util, tempfile, concurrent.futures as cf
from collections import Counter
H = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'method', 'members')
spec = importlib.util.spec_from_file_location('gate', os.path.join(H, 'gate.py')); gate = importlib.util.module_from_spec(spec); spec.loader.exec_module(gate)
NOW = tempfile.mkdtemp(prefix='shiftinv-'); print('fresh outputs ->', NOW, file=sys.stderr)
mask = lambda s: re.sub(r'\d[\d,]*(?:\.\d+)?', '#', s)
nums = lambda s: re.findall(r'\d[\d,]*(?:\.\d+)?', s)
def run(n):
    cmd = gate.SPECIAL.get(n, ['python3', n + '.py'])
    p = subprocess.run(cmd, cwd=H, capture_output=True, timeout=1200)
    out = p.stdout.decode('utf-8', 'replace'); open(os.path.join(NOW, n + '.out'), 'w', encoding='utf-8').write(out)
    return n, p.returncode, out
names = [f[:-4] for f in sorted(os.listdir(H)) if f.endswith('.out') and (os.path.exists(os.path.join(H, f[:-4] + '.py')) or f[:-4] in gate.SPECIAL)] if '--all' in sys.argv else [a for a in sys.argv[1:] if not a.startswith('--')]
if '--list' in sys.argv: print('\n'.join(names)); sys.exit(0)
rows = []
with cf.ThreadPoolExecutor(4) as ex:
    for n, rc, out in ex.map(run, names):
        gold = open(os.path.join(H, n + '.out'), encoding='utf-8').read()
        if rc != 0: rows.append((n, 'ERROR', rc, '', '')); continue
        if out == gold: rows.append((n, 'SAME', 0, '', '')); continue
        a, b = gold.split('\n'), out.split('\n')
        ca, cb = Counter(mask(x) for x in a), Counter(mask(x) for x in b)
        res = sum((ca - cb).values()) + sum((cb - ca).values())
        da = {mask(x): x for x in a if 'md5' not in x}; db = {mask(x): x for x in b if 'md5' not in x}
        flags = []
        for k in set(da) & set(db):
            if da[k] == db[k]: continue
            na, nb = nums(da[k]), nums(db[k])
            if len(na) != len(nb): continue
            for p, q in zip(na, nb):
                if p != q:
                    try: pv, qv = float(p.replace(',', '')), float(q.replace(',', ''))
                    except ValueError: continue
                    if pv < 1000 or qv < 1000 or abs(qv - pv) > 60: flags.append('%s->%s %s' % (p, q, da[k].strip()[:80])); break
        kind = 'TEXT' if res else ('COUNT' if flags else 'SHIFT')
        rows.append((n, kind, res, len(flags), ' | '.join(flags[:2])))
for r in sorted(rows, key=lambda r: (r[1], r[0])): print('%-14s %-6s residual %4s  non-shift ints %3s  %s' % r)
