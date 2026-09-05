#!/usr/bin/env python3
"""shiftcheck2.py — shiftcheck's successor for a REGISTER line shift: the window applies only in a line-reference context.

    python3 tools/shiftcheck2.py --shift PIVOT:DELTA:MAX [--subst OLD=NEW ...] [--load DIR] [--banked DIR] [--all | NAME ...]
    python3 tools/shiftcheck2.py --selftest

WHY. `shiftcheck.py` bumps EVERY integer in its window and so cannot sort a Register shift: a Register line number and a
same-range count sit on the same output line (*six-volume sites 137* beside `'reg': [120, …]`), and the unchanged count
then fails the check — 132 of 136 changed goldens UNEXPLAINED at W-234's `--shift 50:2:6800`. This tool keeps
shiftcheck's contract (a declared shift, declared substitutions, EXPLAINED means every changed line reduces to its banked
form) and adds the one thing it lacked: an integer is a candidate for the shift ONLY where the text around it says it is a
Register line reference — after `L`, `reg`, `Register`, `register`, `R`, `heading`, `unit = L`, `->`, an en-dash range
`L…–L…`, at the start of a line, or inside a bracket list or tuple — and only when its own change is exactly the declared delta from at or above
the pivot. An unchanged integer is never touched. A count that moved by exactly the delta in such a context would be
explained wrongly; every shift-explained integer that is not in an L/reg/Register context is therefore PRINTED for the
reader (`bare`), which is the price of the context rule and is paid visibly. Verdicts: UNCHANGED, EXPLAINED (with the
bare list), RESIDUE (the first unexplained change, quoted), UNRUNNABLE (no output). It writes nothing into method/.
"""
import argparse, os, re, subprocess, sys, tempfile, difflib, importlib.util
H = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'method', 'members')
NUM = re.compile(r'(?<![\[\d,])\d{1,3}(?:,\d{3})+(?![\d,])|\d+')   # a thousands group, unless it sits in a comma-joined list
CTX = re.compile(r"(L|reg|Register|register|R\d+ L|heading|unit = L|–L|\[|,|\(|'reg': \[|lines: \[|L\d+[-–]|->|\bR|^\s*)\s*$")
STRONG = re.compile(r"(L|reg|Register|register|R\d+ L|heading|unit = L|–L|'reg': \[|lines: \[|L\d+[-–])\s*$")
def parse_shift(s):
    m = re.fullmatch(r'(\d+):([+-]?\d+):(\d+)', s)
    if not m: raise argparse.ArgumentTypeError('--shift wants PIVOT:DELTA:MAX')
    return int(m.group(1)), int(m.group(2)), int(m.group(3))
ISNUM = lambda t: bool(NUM.fullmatch(t))
def explain_line(a, b, shifts, substs):
    """(kind, detail): kind in 'same' | 'decl' | 'shift' | 'residue'; detail lists bare shift sites.
    A numeric substitution (1832=1835) is matched token by token, never as a substring — '14=16' must not touch 1442;
    a non-numeric one (an md5 prefix) is a substring."""
    for x, y in substs:
        if not (ISNUM(x) and ISNUM(y)): a = a.replace(x, y)
    if a == b: return 'decl', []
    ta, tb = NUM.split(a), NUM.split(b)
    if ta != tb: return 'residue', ['text differs: %r' % b.strip()[:100]]
    kinds, bare = set(), []
    for x, y, m in zip(NUM.findall(a), NUM.findall(b), NUM.finditer(a)):
        if x == y: continue
        if (x, y) in substs: kinds.add('decl'); continue
        pre = a[:m.start()][-16:]
        try: xi, yi = int(x.replace(',', '')), int(y.replace(',', ''))
        except ValueError: return 'residue', ['%s -> %s' % (x, y)]
        ok = any(lo <= xi <= hi and yi == xi + d for lo, d, hi in shifts) and ',' not in x and CTX.search(pre)
        if not ok: return 'residue', ['%s -> %s in %r' % (x, y, (pre + x)[-40:])]
        kinds.add('shift')
        if not STRONG.search(pre): bare.append('%s->%s after %r' % (x, y, pre.strip()[-12:]))
    return ('shift' if 'shift' in kinds else 'decl'), bare
def classify(banked, now, shifts, substs):
    if banked == now: return 'UNCHANGED', []
    bl, nl = banked.split('\n'), now.split('\n')
    if len(bl) != len(nl): return 'RESIDUE', ['line count %d -> %d' % (len(bl), len(nl))]
    bare = []
    for a, b in zip(bl, nl):
        if a == b: continue
        k, d = explain_line(a, b, shifts, substs)
        if k == 'residue': return 'RESIDUE', d
        bare += d
    return 'EXPLAINED', bare
def gate_cmd(name):
    spec = importlib.util.spec_from_file_location('gate', os.path.join(H, 'gate.py')); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
    return g.SPECIAL.get(name, ['python3', name + '.py'])
def run_now(name, load):
    if load:
        p = os.path.join(load, name + '.now')
        return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else None
    r = subprocess.run(gate_cmd(name), cwd=H, capture_output=True, text=True, timeout=300)
    return r.stdout if r.returncode == 0 else None
def selftest():
    S = [(50, 2, 6800)]; U = [('1832', '1835'), ('33e10932', '87bd1b80')]
    cases = [('reg list shifts', "478      main [7058] reg [1778] ioi [858]", "478      main [7058] reg [1780] ioi [858]", 'EXPLAINED'),
             ('unchanged in-window count untouched', "18 six-volume sites 137 other volumes {'reg': [120, 146]}", "18 six-volume sites 137 other volumes {'reg': [122, 148]}", 'EXPLAINED'),
             ('a count that moved by one is a residue', 'withdraw reg 61 site(s)', 'withdraw reg 62 site(s)', 'RESIDUE'),
             ('a count below the pivot moving by the delta is a residue', '976 main:93 reg:45 mc:37', '976 main:93 reg:47 mc:37', 'RESIDUE'),
             ('declared count', 'live register: 1699 numbers, 1..1832', 'live register: 1699 numbers, 1..1835', 'EXPLAINED'),
             ('declared md5', 'md5 33e10932 6771 lines', 'md5 87bd1b80 6771 lines', 'EXPLAINED'),
             ('literal read prints other words', 'reg  L1366 ### 368', 'reg  L1366 **ITEM M …**', 'RESIDUE'),
             ('added line', 'one\ntwo', 'one\ntwo\nthree', 'RESIDUE'),
             ('unit window', 'unit = L78-L453, 376 lines', 'unit = L80-L455, 376 lines', 'EXPLAINED'),
             ('entry-line tuple', 'Register (line, entry) [(1376, 371), (6570, 1780)]', 'Register (line, entry) [(1378, 371), (6572, 1780)]', 'EXPLAINED'),
             ('arrow reference', 'register 1787 cited at L8683 -> 6594 (exact)', 'register 1787 cited at L8683 -> 6596 (exact)', 'EXPLAINED'),
             ('R-prefixed reference', '    R6566: Both rows now state', '    R6568: Both rows now state', 'EXPLAINED'),
             ('line-leading reference', '   1058 **ITEMS D AND M**', '   1060 **ITEMS D AND M**', 'EXPLAINED'),
             ('comma-joined list is not a thousands group', 'reg:5[368,400,5732]', 'reg:5[370,402,5734]', 'EXPLAINED'),
             ('a list that grew is a residue', "'reg': [686, 2360]", "'reg': [688, 2362, 6775]", 'RESIDUE')]
    bad = 0
    for name, a, b, want in cases:
        got, d = classify(a, b, S, U)
        if got != want: print('  FAIL %s: %s expected %s %s' % (name, got, want, d)); bad += 1
    got, bare = classify('main:0 reg:4[5004,6653]', 'main:0 reg:4[5006,6655]', S, U)
    if got != 'EXPLAINED' or not bare: print('  FAIL bare sites are printed: %s %s' % (got, bare)); bad += 1
    print('fixtures checked: %d  failed: %d' % (len(cases) + 1, bad)); print('\nSELFTEST OK' if not bad else '\nSELFTEST FAILED'); return bad
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('names', nargs='*'); ap.add_argument('--shift', action='append', type=parse_shift, default=[])
    ap.add_argument('--subst', action='append', default=[]); ap.add_argument('--load'); ap.add_argument('--banked', help='read NAME.out from this directory instead of members/ (a retired build\'s goldens, from git)'); ap.add_argument('--all', action='store_true'); ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    substs = [tuple(s.split('=', 1)) for s in a.subst]
    names = sorted(f[:-4] for f in os.listdir(a.banked or H) if f.endswith('.out')) if a.all else a.names
    print('shift windows:', a.shift, '| substitutions:', substs, '| load:', a.load or '(run)')
    tally = {}
    for n in names:
        banked = open(os.path.join(a.banked or H, n + '.out'), encoding='utf-8', errors='replace').read(); now = run_now(n, a.load)
        if now is None: v, d = 'UNRUNNABLE', []
        else: v, d = classify(banked, now, a.shift, substs)
        tally[v] = tally.get(v, 0) + 1; print('%-11s %s' % (v, n))
        for x in d[:4]: print('    ', x[:160])
    print('\n', ' '.join('%s %d' % kv for kv in sorted(tally.items())))
if __name__ == '__main__': main()
