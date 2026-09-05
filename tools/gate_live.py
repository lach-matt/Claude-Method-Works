#!/usr/bin/env python3
"""gate_live.py — the gate over the LIVE goldens only.

    python3 tools/gate_live.py            run gate.py on every live golden (in members/, through gate.py's own runner)
    python3 tools/gate_live.py --list     print the live set and the reason each other golden is left out; run nothing

WHY. `gate.py run --all` walks every NAME.out alphabetically; the superseded predecessors and the held readings
(DEF-153B, DEF-153N, W-224, W-234) fail as recorded and several run long, so a full walk costs an hour and reports
nothing the held list does not. This tool decides nothing about a golden: it computes the set the store treats as
live — every NAME.out that has no seated successor and is not held — prints it, and hands it to gate.py, whose
verdict is the verdict. The core five are always included.

SUCCESSOR RULE, by name: NAME is superseded when another golden's name is NAME's stem with a later version mark —
a higher trailing digit (r2-ch16p2 → r2-ch16p3) or a trailing digit where NAME has none (r2-bib → r2-bib2). A
trailing letter is the instrument's own (r2-ch16a … r2-ch16z), so the one letter-marked successor is named in RENAMED.
Where a predecessor is held with no successor yet, the name is listed in HELD with the record that says so; edit those
tables when the record changes, never the rule.
"""
import os, re, subprocess, sys
H = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'method', 'members')
CORE = ['tower-2', 'kinds', 'minmax', 'r2-tools-constants', 'extent']
HELD = {  # name: the record that holds it (a golden with a seated successor needs no entry — the name rule finds it)
    'r2-reg11a2': 'W-224: census rows by Register line', 'r2-reg12b': 'W-224: census rows by Register line',
    'r2-ch18b': 'DEF-153B: a reading, not a re-bank', 'r2-ch23b': 'DEF-153B: a reading', 'r2-26b': 'DEF-153B: UNRUNNABLE, successor r2-26b2 owed',
    'r3-wl': 'chat 153: re-taken by r3-wl2', 'r2-ch23a': 'DEF-153B: a reading', 'r2-ch28a': 'DEF-153B: a reading',
}
def goldens():
    return sorted(f[:-4] for f in os.listdir(H) if f.endswith('.out'))
RENAMED = {'r2-reg12': 'r2-reg12b'}   # the one successor whose mark is a letter (a trailing letter is otherwise the instrument's own, r2-ch16a … r2-ch16z)
def split(n):
    m = re.fullmatch(r'(.*?\D)(\d*)', n); return m.group(1), m.group(2)
def superseded_by(n, names):
    stem, mark = split(n); out = [g for g in names if g != n and split(g)[0] == stem and split(g)[1] and (mark == '' or int(split(g)[1]) > int(mark))]
    if RENAMED.get(n) in names: out.append(RENAMED[n])
    return sorted(out)
def live():
    names = goldens(); keep, left = [], {}
    for n in names:
        succ = superseded_by(n, names)
        if n in CORE: keep.append(n)
        elif n in HELD: left[n] = 'held — ' + HELD[n]
        elif succ: left[n] = 'superseded by ' + ', '.join(succ)
        else: keep.append(n)
    return keep, left
if __name__ == '__main__':
    keep, left = live()
    if '--list' in sys.argv:
        print('LIVE (%d):' % len(keep)); print('  ' + ' '.join(keep)); print('LEFT OUT (%d):' % len(left))
        for n, why in left.items(): print('  %-14s %s' % (n, why))
        sys.exit(0)
    names = [a for a in sys.argv[1:] if not a.startswith('--')] or keep
    sys.exit(subprocess.call([sys.executable, 'gate.py', 'run'] + names, cwd=H))
