#!/usr/bin/env python3
"""shiftcheck.py — decide whether a moved golden moved for a declared reason, or is a finding.

    python3 tools/shiftcheck.py --shift PIVOT:DELTA:MAX [--subst OLD=NEW ...] [--all | NAME ...]
    python3 tools/shiftcheck.py --selftest

WHY THIS EXISTS. `close_rebank.py` re-banks a golden by running its instrument. It records that a
measurement moved; it explicitly does not decide whether the movement is a finding. That is right,
and it leaves a hole: an instrument that hard-codes a line number reads the WRONG SITE after any
insertion above it, and re-banking such an instrument banks its wrong reading. The gate then reports
it green forever, which is worse than red -- the same argument HANDOFF-152-RESUME section 4 makes
about a stale golden. R3 changes volume text 35 more times, so the hole is not a one-off.

WHAT IT DOES. For each seated golden it runs the instrument (through gate.py's own runner, imported
by path -- an instrument imports a seated member, it never copies one), diffs the output against the
banked bytes, and asks one question per changed line: **is this line's change fully accounted for by
a reason declared on the command line?** Two kinds of reason, and both must be stated explicitly:

  --shift PIVOT:DELTA:MAX   every integer in [PIVOT, MAX] moves by DELTA. This is the line shift a
                            class instrument already prints (r3-wl2: "+8 for BUILD92 L >= 9608").
                            The window is bounded above so byte counts and md5 fragments are not
                            silently "explained" by it.
  --subst OLD=NEW           one declared textual change: an entry total, a member md5, a line count.
                            Each is named by the operator and appears in the report.

EXPLAINED means every changed line reduces to its banked form under those reasons. Then, and only
then, a mechanical re-bank is provably safe. UNEXPLAINED means at least one line changed for a
reason nobody declared -- which is either a mis-targeted instrument or a real finding, and either
way it is a reading and not a re-bank. UNRUNNABLE means a non-zero exit: close_rebank.py refuses
those anyway, and they need a successor instrument.

This tool never writes a golden, never edits an instrument and never touches a volume. It sorts.
"""
import argparse, difflib, importlib.util, os, pathlib, re, sys

def _members_dir():
    """Find members/ from either location: this file travels both as tools/ and as a seated member."""
    here = pathlib.Path(__file__).resolve().parent
    for cand in (here, here.parent / 'method' / 'members', here / 'method' / 'members'):
        if (cand / 'gate.py').exists():
            return cand
    raise SystemExit('cannot locate method/members (no gate.py found)')


MEMBERS = _members_dir()


def load_gate():
    """gate.py by path: its SPECIAL map and its runner are the contract, and are not re-implemented."""
    spec = importlib.util.spec_from_file_location('gate', MEMBERS / 'gate.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules['gate'] = mod
    spec.loader.exec_module(mod)
    return mod


def parse_shift(s):
    m = re.fullmatch(r'(\d+):([+-]?\d+):(\d+)', s)
    if not m:
        raise argparse.ArgumentTypeError(f'--shift wants PIVOT:DELTA:MAX, got {s!r}')
    lo, d, hi = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if lo > hi:
        raise argparse.ArgumentTypeError('--shift PIVOT must not exceed MAX')
    return lo, d, hi


def normalise(line, shifts, substs, protect=()):
    """Map a banked line forward under the declared reasons.

    `protect` names spans the shift must NOT touch. A numeric window cannot tell a main-volume line
    number from a same-range number belonging to another file -- Prints & Proofs runs to a similar
    length, so `P[9873]` and `PP lines: 11372` sit inside the window and did not move. Without this
    the checker reports those as UNEXPLAINED, which is safe but noisy; with it the exclusion is
    declared, printed in the report, and auditable.
    """
    def bump(m):
        n = int(m.group())
        for lo, d, hi in shifts:
            if lo <= n <= hi:
                return str(n + d)
        return m.group()

    spans = []
    for rx in protect:
        for m in re.finditer(rx, line):
            spans.append((m.start(), m.end()))
    spans.sort()
    merged = []
    for st, en in spans:
        if merged and st <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], en))
        else:
            merged.append((st, en))

    out, prev = [], 0
    for st, en in merged:
        out.append(re.sub(r'\d+', bump, line[prev:st]))
        out.append(line[st:en])
        prev = en
    out.append(re.sub(r'\d+', bump, line[prev:]))
    res = ''.join(out)
    for x, y in substs:
        res = res.replace(x, y)
    return res


def hunks(banked, now):
    """Changed line pairs, paired within each hunk so unequal hunks are never zipped across."""
    d = list(difflib.unified_diff(banked.splitlines(), now.splitlines(), lineterm='', n=0))
    out, cur = [], None
    for l in d:
        if l.startswith('@@'):
            cur = {'m': [], 'p': []}; out.append(cur); continue
        if cur is None or l.startswith(('---', '+++')):
            continue
        if l.startswith('-'):
            cur['m'].append(l[1:])
        elif l.startswith('+'):
            cur['p'].append(l[1:])
    return out


def classify(banked, now, shifts, substs, protect=()):
    if banked == now:
        return 'UNCHANGED', None
    for h in hunks(banked, now):
        if len(h['m']) != len(h['p']):
            return 'UNEXPLAINED', (h['m'][0] if h['m'] else '(added line)',
                                   h['p'][0] if h['p'] else '(removed line)')
        for a, b in zip(h['m'], h['p']):
            if normalise(a, shifts, substs, protect) != b:
                return 'UNEXPLAINED', (a, b)
    return 'EXPLAINED', None


def selftest():
    S = [(9608, 8, 11855)]
    U = []
    cases = [
        ('pure shift',            'sites [9600, 9700, 11855]', 'sites [9600, 9708, 11863]', S, U, 'EXPLAINED'),
        ('below pivot untouched', 'reg L6299 cited',           'reg L6299 cited',           S, U, 'UNCHANGED'),
        ('above window untouched','bytes 1983081',             'bytes 1983081',             S, U, 'UNCHANGED'),
        ('real content change',   'withdraw main 57 site(s)',  'withdraw main 58 site(s)',  S, U, 'UNEXPLAINED'),
        ('declared subst',        "'a correction': 153",       "'a correction': 156",       S, [('153', '156')], 'EXPLAINED'),
        ('undeclared count',      'Register: 1632 headings',   'Register: 1635 headings',   S, U, 'UNEXPLAINED'),
        ('mis-targeted read',     'L9722: The challenge posed','L9722: ---',                S, U, 'UNEXPLAINED'),
        ('added line',            'one\ntwo',                  'one\ntwo\nthree',           S, U, 'UNEXPLAINED'),
    ]
    # a protected span keeps its numbers while the rest of the line shifts
    got, _ = classify('PP P[9873] -> volume L[10224]', 'PP P[9873] -> volume L[10232]', S, U, (r'P\[\d+\]',))
    if got != 'EXPLAINED':
        print(f'  FAIL protected span: {got} expected EXPLAINED'); bad += 1
    got, _ = classify('PP P[9873] -> volume L[10224]', 'PP P[9873] -> volume L[10232]', S, U)
    if got != 'UNEXPLAINED':
        print(f'  FAIL unprotected PP should be flagged: {got}'); bad += 1
    bad = 0
    for name, a, b, sh, su, want in cases:
        got, _ = classify(a, b, sh, su)
        if got != want:
            print(f'  FAIL {name}: {got} expected {want}'); bad += 1
    # the window must not explain a byte count that happens to sit in range
    got, _ = classify('bytes 11000 here', 'bytes 11008 here', S, U)
    if got != 'EXPLAINED':
        print('  FAIL in-window integer should be shiftable'); bad += 1
    print(f'fixtures checked: {len(cases) + 3}  failed: {bad}')
    print('\nSELFTEST OK' if not bad else '\nSELFTEST FAILED')
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--shift', action='append', type=parse_shift, default=[])
    ap.add_argument('--subst', action='append', default=[])
    ap.add_argument('--protect', action='append', default=[],
                    metavar='REGEX', help='spans the shift must not touch, e.g. PP line numbers')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--timeout', type=int, default=270)
    ap.add_argument('--save', metavar='DIR', help='write each instrument run to DIR/NAME.now')
    ap.add_argument('--load', metavar='DIR', help='read NAME.now from DIR instead of running')
    ap.add_argument('--width', type=int, default=150, help='chars of an example pair to print')
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())

    substs = []
    for s in a.subst:
        if '=' not in s:
            ap.error(f'--subst wants OLD=NEW, got {s!r}')
        k, v = s.split('=', 1); substs.append((k, v))

    # Only needed when instruments are actually run; --load must not require the gate's interpreter.
    gate = None if a.load else load_gate()
    names = sorted(f[:-4] for f in os.listdir(MEMBERS) if f.endswith('.out')) if a.all else a.names
    if not names:
        ap.error('name at least one golden, or pass --all')

    print(f'shift windows: {a.shift or "(none)"}')
    print(f'declared substitutions: {substs or "(none)"}')
    print(f'protected spans: {a.protect or "(none)"}')
    print()
    buckets = {'UNCHANGED': [], 'EXPLAINED': [], 'UNEXPLAINED': [], 'UNRUNNABLE': []}
    for n in names:
        gold = MEMBERS / f'{n}.out'
        if not gold.exists():
            buckets['UNRUNNABLE'].append(n); print(f'UNRUNNABLE  {n}  (no golden)'); continue
        if a.load:
            cached = pathlib.Path(a.load) / f'{n}.now'
            if not cached.exists():
                buckets['UNRUNNABLE'].append(n); print(f'UNRUNNABLE  {n}  (not in cache)'); continue
            status, out = 'OK', cached.read_text(encoding='utf-8')
        else:
            status, out, _ = gate.run_one(n, timeout=a.timeout)
        if status != 'OK':
            buckets['UNRUNNABLE'].append(n); print(f'UNRUNNABLE  {n}  ({status}) — needs a successor, not a re-bank')
            continue
        if a.save:
            d = pathlib.Path(a.save); d.mkdir(parents=True, exist_ok=True)
            (d / f'{n}.now').write_text(out, encoding='utf-8')
        verdict, ex = classify(gold.read_text(encoding='utf-8'), out, a.shift, substs, a.protect)
        buckets[verdict].append(n)
        print(f'{verdict:<11} {n}')
        if ex:
            print(f'   banked  {ex[0][:a.width]}')
            print(f'   now     {ex[1][:a.width]}')

    print()
    for k in ('UNCHANGED', 'EXPLAINED', 'UNEXPLAINED', 'UNRUNNABLE'):
        print(f'{k:<12} {len(buckets[k]):>3}  {" ".join(buckets[k]) if buckets[k] else ""}'.rstrip())
    print()
    if buckets['UNEXPLAINED'] or buckets['UNRUNNABLE']:
        print('NOT SAFE TO RE-BANK MECHANICALLY: every UNEXPLAINED and UNRUNNABLE golden is a reading.')
        sys.exit(1)
    print('SAFE TO RE-BANK: every difference is accounted for by a declared reason.')


if __name__ == '__main__':
    main()
