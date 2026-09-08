#!/usr/bin/env python3
"""gate_live.py — the gate over the LIVE goldens only.

    python3 tools/gate_live.py            run gate.py on every live golden (in members/, through gate.py's own runner)
    python3 tools/gate_live.py --list     print the live set and the reason each other golden is left out; run nothing
    python3 tools/gate_live.py --census   the census step alone: close_census2.py --dry must find the seated census a fixed point

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

THE CENSUS STEP. `gate.py census` runs `census.py`, which reads /home/claude and carries the Register's extent as a literal,
so it has been red since BUILD98 and stays red by construction (DEF-153O). The live step is `close_census2.py --dry`: it
runs `census2.py`, matches the fresh rows onto the seated ids by content, and must report the seated member a FIXED POINT —
every row exact, nothing NEW, nothing GONE, the retired rows carried — printing "== the seated member". The default walk
runs it first, then the live goldens.
"""
import os, re, subprocess, sys
_here = os.path.dirname(os.path.abspath(__file__))
H = _here if os.path.basename(_here) == 'members' else os.path.join(os.path.dirname(_here), 'method', 'members')   # from tools/ or from a seated copy
CORE = ['tower-2', 'kinds', 'minmax', 'r2-tools-constants', 'extent']
HELD = {  # name: the record that holds it (a golden with a seated successor needs no entry — the name rule finds it)
    'r2-reg11a2': 'W-224: census rows by Register line', 'r2-reg12b': 'W-224: census rows by Register line',
    'r2-ch18b': 'DEF-153B: a reading, not a re-bank', 'r2-ch23b': 'DEF-153B: a reading', 'r2-26b': 'DEF-153B: UNRUNNABLE, successor r2-26b2 owed',
    'r2-26c2': 'W-260: the record outgrew its pinned list \u2014 register 1868 names the method ratio and so joins 296 in it; successor r2-26c3 owed, carrying 26b-02, 26b-03, 26c-02 and 26c-03 unchanged',
    'r3-wl': 'chat 153: re-taken by r3-wl2', 'r2-ch23a': 'DEF-153B: a reading', 'r2-ch28a': 'DEF-153B: a reading',
    'r2-bib2': 'W-308: its integrity check pins "the table prints 162 data rows, as the volume states", which register 1891 restates at 156, and it EXITS NONZERO on that check — successor r2-bib3 owed',
    'r2-28a4': 'W-306: three check() calls pin "162 works" and the 162 data rows, which register 1891 restates at 156; the checks RECORD rather than raise, so a re-bank would bank its own EXPECTED 162 lines as the golden — successor r2-28a5 owed',
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
def census():
    p = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'close_census2.py'), '--dry'], capture_output=True, text=True)
    tail = [l for l in p.stdout.splitlines() if l.strip().startswith(('seated ', 'renumbered '))]
    ok = p.returncode == 0 and any('== the seated member' in l for l in tail)
    print(('OK  ' if ok else 'FAIL') + ' census: ' + (' / '.join(l.strip() for l in tail) or (p.stderr.strip().splitlines() or ['no output'])[-1]))
    return ok
if __name__ == '__main__':
    keep, left = live()
    if '--census' in sys.argv: sys.exit(0 if census() else 1)
    if '--list' in sys.argv:
        print('LIVE (%d):' % len(keep)); print('  ' + ' '.join(keep)); print('LEFT OUT (%d):' % len(left))
        for n, why in left.items(): print('  %-14s %s' % (n, why))
        sys.exit(0)
    names = [a for a in sys.argv[1:] if not a.startswith('--')]
    c = True if names else census()
    sys.exit(subprocess.call([sys.executable, 'gate.py', 'run'] + (names or keep), cwd=H) or (0 if c else 1))
