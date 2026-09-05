#!/usr/bin/env python3
# r3-br-measure.py — R3 (a lead outside Q5, M's direction of 5 September): the Request-3 return of 2026-08-28
# (03-1D-lands-inside-14D.md in the mirror) re-run from the seated instruments. The tower is rebuilt by the seated
# tower.py (Λ₈ with its seven fingerprints, L8.json) and tower3.py (Λ₉ … Λ₁₃, tower.json), and the bracket system is
# measured by factor.py — chat 58's own script, standard-library, seated byte-exact beside this instrument — exactly as
# the return ran them, in a scratch directory the instrument removes; nothing is written into method/. Each printed
# figure is checked against the return's: rank-value counts 18, 21, 24, 29, 36, 44 (register 334's chain of 44),
# the strict map refuted at every stage with branching 4, 4, 6, 8, 9, bracket endpoints monotone and fibres gap-free
# at every stage, the composed bracket χ(Λ₁₃) → χ(Λ₈) not equal to the direct one with slack at most 2, the image of
# Λ₁₃ in χ(Λ₈) the whole chain 3 … 20.
import os, sys, re, shutil, subprocess, tempfile, hashlib
H = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-72s %-22s %s' % (tag, repr(got)[:22], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
MD5 = {'tower.py': None, 'tower3.py': None, 'factor.py': '55c518c9e0d267d9ce6fd95d1e42dbde'}   # factor.py: drive/MANIFEST.tsv
work = tempfile.mkdtemp(prefix='r3-br-')
try:
    for n, m in MD5.items():
        src = os.path.join(H, n)
        if not os.path.exists(src) and n == 'factor.py':   # before seating: the mirror's copy, asserted
            src = os.path.join(os.path.dirname(os.path.dirname(H)), 'drive', 'The Method Materials', n)
        b = open(src, 'rb').read()
        if m: check('%s is the return\'s script (md5 %s…)' % (n, m[:8]), hashlib.md5(b).hexdigest(), m)
        open(os.path.join(work, n), 'wb').write(b)
    run = lambda *a: subprocess.run([sys.executable] + list(a), cwd=work, capture_output=True, text=True, timeout=600)
    t = run('tower.py'); assert t.returncode == 0, t.stderr[-500:]
    print('== tower.py (Λ₈ and its seven fingerprints)')
    for l in t.stdout.rstrip().split('\n'): print('   ' + l[:150])
    check('Λ₈: E = 0', 'Λ8: E = 0' in t.stdout, True)
    check('rank sequence forwards / backwards, mean rank, F(−1)', all(s in t.stdout for s in ('fwd [1, 5, 15, 34, 59, 87]', 'bwd [1, 4, 10, 21, 37, 57]', 'mean rank=11.0666', 'F(-1)=2')), True)
    check('L8.json written', os.path.exists(os.path.join(work, 'L8.json')), True)
    t3 = run('tower3.py', 'bank'); assert t3.returncode == 0, t3.stderr[-500:]
    print('== tower3.py bank (Λ₁₀ … Λ₁₃)')
    for l in t3.stdout.rstrip().split('\n'): print('   ' + l[:150])
    check('the printed counts 2,535 / 13,585 / 70,905 / 199,130 and #{2K = 0 in Λ₁₂} = 13,585', all(s in t3.stdout for s in ('Λ10 = 2535', 'Λ11 = 13585', 'Λ12 = 70905', 'Λ13 = 199130', 'cells with 2K=0 in Λ12 = 13585')), True)
    check('tower.json written', os.path.exists(os.path.join(work, 'tower.json')), True)
    f = run('factor.py'); assert f.returncode == 0, f.stderr[-500:]
    print('== factor.py (the bracket system)')
    for l in f.stdout.rstrip().split('\n'): print('   ' + l[:160])
    out = f.stdout
    counts = eval(re.search(r'rank-value counts per stage: (\{.*\})', out).group(1))
    check('rank-value counts per stage (χ(Λ₁₃) carries 44, register 334)', [counts[d] for d in (8, 9, 10, 11, 12, 13)], [18, 21, 24, 29, 36, 44])
    rows = re.findall(r'Λ(\d+)→Λ(\d+): strict map: (\w+) \| max branching: (\d+) \| bracket endpoints monotone: (\w+) \| fibres gap-free intervals: (\w+)', out)
    check('five stages, top to bottom', [(int(a), int(b)) for a, b, *_ in rows], [(9, 8), (10, 9), (11, 10), (12, 11), (13, 12)])
    check('the strict map refuted at every stage', [r[2] for r in rows], ['False'] * 5)
    check('branching 4, 4, 6, 8, 9', [int(r[3]) for r in rows], [4, 4, 6, 8, 9])
    check('bracket endpoints monotone at every stage', [r[4] for r in rows], ['True'] * 5)
    check('fibres gap-free intervals at every stage', [r[5] for r in rows], ['True'] * 5)
    m = re.search(r'composite bracket χ\(Λ13\)→χ\(Λ8\): equals direct bracket: (\w+) \| max slack: (\d+)', out)
    check('composed bracket ≠ direct bracket, slack at most 2', (m.group(1), int(m.group(2))), ('False', 2))
    m = re.search(r'image of Λ13 under projection to Λ8 ranks: (\d+)\.\.(\d+) \| covers all of χ\(Λ8\): (\w+)', out)
    check('image of Λ₁₃ in χ(Λ₈): ranks 3 … 20, the whole chain', (int(m.group(1)), int(m.group(2)), m.group(3)), (3, 20, 'True'))
finally:
    shutil.rmtree(work, ignore_errors=True)
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(0 if not FAIL else 1)
