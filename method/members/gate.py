#!/usr/bin/env python3
"""gate.py — the §0 gate as an instrument (chat 74, ruling 2). Every step must be able to fail.
Steps (each its own tool call, `timeout 280`):
  manifest [--main PATH] [--comp PATH]   verify every member of BOTH bundles against MANIFEST.tsv (bytes, md5, lines),
                                         and every extracted file in members/ against the bundle text
  run NAME...  | run --core | run --all  run instruments and diff stdout against the banked NAME.out (prints only mismatches)
  census                                 run census.py, compare /home/claude/DEFECT-CENSUS.tsv to the member byte for byte
  extent-sites                           print the "1 to N" / "1 to N-1" sites of the six reader-facing volumes (N from Register L6)
  bank NAME...                           run and write NAME.out (refuses to overwrite) — used at close for new instruments
  cert CHAT                              write /home/claude/GATE-chCHAT.txt from the log; PASS only if every step passed
Commands: NAME.out ↔ `python3 NAME.py` in members/, except SPECIAL below. Log: /home/claude/gate-log.tsv (append-only)."""
import sys, os, re, hashlib, subprocess, time, difflib
H = os.path.dirname(os.path.abspath(__file__))            # /home/claude/members
HOME = os.path.dirname(H)                                 # /home/claude
MAIN = os.path.join(HOME, 'The_Method_1_6_BUILD90_main_and_register.md')
LOG = os.path.join(HOME, 'gate-log.tsv')
VOLS = ['The_Method_1_6-2.md', 'The_Method_1_6___The_Register-2.md', 'The_Method_1_6___Mathematical_Compendium-2.md',
        'The_Method_1_6___The_Physics_Compendium-2.md', 'The_Method_1_6___The_Index_of_Indices-2.md', 'The_Method_1_6___Spectra_Compendium-2.md']
SPECIAL = {'tower-2': ['python3', 'tower-2.py'], 'kinds': ['python3', 'kinds.py', 'The_Method_1_6___The_Register-2.md'],
           'minmax': ['python3', 'minmax.py'], 'r2-tools-constants': ['python3', 'r2-tools.py', 'constants'],
           'extent': ['python3', 'gate.py', 'extent-sites']}
CORE = ['tower-2', 'kinds', 'minmax', 'r2-tools-constants', 'extent']
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()

def members_of(path):
    t = open(path, 'rb').read()
    ms = [(m.group(1).decode(), m.group(2)) for m in MEMBER.finditer(t)]
    assert len(set(n for n, _ in ms)) == len(ms), 'duplicate member name'
    return t, ms

def log(step, name, status, secs=''):
    with open(LOG, 'a', encoding='utf-8') as f: f.write(f'{step}\t{name}\t{status}\t{secs}\n')

def comp_path(argv):
    if '--comp' in argv: return argv[argv.index('--comp') + 1]
    c = sorted(f for f in os.listdir(HOME) if re.match(r'The_Method_1_6_BUILD\d+_compendia', f))
    assert len(c) == 1, f'name the compendia bundle with --comp (found {c})'
    return os.path.join(HOME, c[0])

def manifest(argv):
    main = argv[argv.index('--main') + 1] if '--main' in argv else MAIN
    comp = comp_path(argv)
    ok = True; rows = {}
    for tag, path in (('main', main), ('compendia', comp)):
        t, ms = members_of(path)
        print(f'{tag}: {os.path.basename(path)}  {len(t):,} B  md5 {md5(t)}  {t.count(b"\n"):,} lines  {len(ms)} members')
        for n, b in ms: rows[(tag, n)] = (len(b), md5(b), b.count(b'\n'), b)
    man = rows.get(('compendia', 'MANIFEST.tsv'))
    if man is None: print('FAIL: no MANIFEST.tsv member'); log('manifest', 'MANIFEST.tsv', 'FAIL'); return
    print(f'MANIFEST.tsv  {man[0]:,} B  md5 {man[1]}')
    listed = {}
    for line in man[3].decode('utf-8').splitlines()[1:]:
        tag, n, by, h, ln = line.split('\t'); listed[(tag, n)] = (int(by), h, int(ln))
    for key, (by, h, ln, _) in sorted(rows.items()):
        if key == ('compendia', 'MANIFEST.tsv'): continue
        if key not in listed: print('FAIL unlisted member', key); ok = False; continue
        if listed[key] != (by, h, ln): print('FAIL mismatch', key, 'bundle', (by, h, ln), 'manifest', listed[key]); ok = False
    for key in listed:
        if key not in rows: print('FAIL listed but absent', key); ok = False
    # extracted files
    ext = [f for f in os.listdir(H) if os.path.isfile(os.path.join(H, f))]
    for (tag, n), (by, h, ln, b) in rows.items():
        p = os.path.join(H, n)
        if not os.path.exists(p): print('FAIL not extracted', n); ok = False
        elif open(p, 'rb').read() != b: print('FAIL extracted file differs from bundle', n); ok = False
    extra = set(ext) - {n for _, n in rows}
    if extra: print('note: files in members/ not in any bundle:', sorted(extra))
    print(f'{"MANIFEST OK" if ok else "MANIFEST FAIL"}: {len(listed)} members listed, {len(ext)} files extracted')
    log('manifest', f'{md5(open(main,"rb").read())} {md5(open(comp,"rb").read())} {man[1]}', 'OK' if ok else 'FAIL')

def command(name):
    return SPECIAL.get(name, ['python3', name + '.py'])

def run_one(name, timeout=270):
    cmd = command(name); t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=H, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', '', time.time() - t0
    out = p.stdout.decode('utf-8', 'replace'); err = p.stderr.decode('utf-8', 'replace')
    if p.returncode != 0: return 'ERROR', out + err, time.time() - t0
    return 'OK', out, time.time() - t0

def run(argv):
    names = CORE if '--core' in argv else (sorted(f[:-4] for f in os.listdir(H) if f.endswith('.out')) if '--all' in argv else argv)
    for name in names:
        gold = os.path.join(H, name + '.out')
        if not os.path.exists(gold): print(f'FAIL {name}: no {name}.out'); log('run', name, 'FAIL'); continue
        status, out, secs = run_one(name)
        if status == 'OK':
            g = open(gold, encoding='utf-8').read()
            if out == g: print(f'OK   {name}  ({secs:.0f} s)'); log('run', name, 'OK', f'{secs:.0f}'); continue
            d = list(difflib.unified_diff(g.splitlines(), out.splitlines(), 'banked', 'now', lineterm='', n=0))
            print(f'FAIL {name}: output differs from {name}.out ({len(d)} diff lines; first 40):'); print('\n'.join(d[:40]))
            log('run', name, 'FAIL', f'{secs:.0f}')
        else:
            print(f'FAIL {name}: {status}\n{out[-1500:]}'); log('run', name, status, f'{secs:.0f}')

def bank(argv):
    for name in argv:
        gold = os.path.join(H, name + '.out')
        assert not os.path.exists(gold), f'{gold} exists — never overwrite'
        status, out, secs = run_one(name)
        assert status == 'OK', f'{name}: {status}\n{out[-1500:]}'
        open(gold, 'w', encoding='utf-8').write(out)
        print(f'banked {name}.out  {len(out.encode()):,} B  md5 {md5(out.encode())[:8]}  {out.count(chr(10))} lines  ({secs:.0f} s)')

def census():
    target = os.path.join(HOME, 'DEFECT-CENSUS.tsv')
    assert not os.path.exists(target), f'{target} exists — remove it in a delete-only call first'
    pc = os.path.join(H, '__pycache__'); assert not os.path.exists(pc), 'remove members/__pycache__ first (delete-only call)'
    status, out, secs = run_one('census')
    if status != 'OK': print(f'FAIL census: {status}\n{out[-1500:]}'); log('census', 'census.py', status); return
    same = open(target, 'rb').read() == open(os.path.join(H, 'DEFECT-CENSUS.tsv'), 'rb').read()
    print(f'{"OK  " if same else "FAIL"} census: DEFECT-CENSUS.tsv {"byte-identical to" if same else "DIFFERS from"} the member  ({secs:.0f} s)')
    log('census', 'DEFECT-CENSUS.tsv', 'OK' if same else 'FAIL', f'{secs:.0f}')

def extent_sites():
    reg = open(os.path.join(H, VOLS[1]), encoding='utf-8').read().splitlines()
    m = re.search(r'1 to (\d+)', reg[5]); assert m, 'Register L6 carries no "1 to N"'
    N = int(m.group(1)); print(f'extent from Register L6: 1 to {N}')
    for pat in (f'1 to {N}', f'1 to {N-1}'):
        sites = []
        for v in VOLS:
            for i, l in enumerate(open(os.path.join(H, v), encoding='utf-8').read().splitlines(), 1):
                if pat in l: sites.append(f'{v.split("___")[-1].replace("The_Method_1_6-2.md","main")}:L{i}')
        print(f'"{pat}": {len(sites)} sites', ' '.join(sites))

def cert(argv):
    chat = argv[0]
    rows = [l.rstrip('\n').split('\t') for l in open(LOG, encoding='utf-8')]
    steps = {(r[0], r[1]): r[2] for r in rows}
    need = [('manifest', None), ('census', 'DEFECT-CENSUS.tsv')] + [('run', n) for n in CORE]
    missing = [f'{s}:{n}' for s, n in need if not any(k[0] == s and (n is None or k[1] == n) for k in steps)]
    fails = [f'{k[0]}:{k[1]}={v}' for k, v in steps.items() if v != 'OK']
    verdict = 'PASS' if not missing and not fails else 'FAIL'
    lines = [f'GATE-ch{chat}  {time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}  verdict {verdict}']
    lines += [f'  {r[0]:9} {r[1][:90]:90} {r[2]:8} {r[3]}' for r in rows]
    if missing: lines.append('  MISSING steps: ' + ' '.join(missing))
    if fails: lines.append('  FAILED steps: ' + ' '.join(fails))
    out = os.path.join(HOME, f'GATE-ch{chat}.txt'); assert not os.path.exists(out), f'{out} exists'
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n'); print('\n'.join(lines))

if __name__ == '__main__':
    step, rest = sys.argv[1], sys.argv[2:]
    {'manifest': manifest, 'run': run, 'bank': bank, 'census': lambda a: census(), 'extent-sites': lambda a: extent_sites(), 'cert': cert}[step](rest)
