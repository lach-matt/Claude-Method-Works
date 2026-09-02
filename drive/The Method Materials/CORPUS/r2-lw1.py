#!/usr/bin/env python3
# r2-lw1.py — chat 130 — Segment A intake: LOWDIN-DELIVERY-1-part1 (RUL-128 item 4; DEF-129 item 7; docket 38).
# Reads MEMBERS only: LW1-* (the delivery's four text files, bytes unchanged under a prefix) and the Register member.
# Imports r2lib and r2-ch16y by path (r2-ch16y's §3 table is this project's own NIST reconstruction, banked in chat 126).
# Every convention is named before a verdict; Decimal never round(); a count word counts DATA rows; every negative
# carries its witness; the delivered instrument is run as delivered and its stdout byte-compared to the delivered log.
import os, re, io, sys, hashlib, subprocess, importlib.util, contextlib
from decimal import Decimal as D
H = os.path.dirname(os.path.abspath(__file__))
md5 = lambda b: hashlib.md5(b).hexdigest()
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
R = rd('The_Method_1_6___The_Register-2.md')
def rbody(n):   # copied verbatim from r2-ch17c.py (there from r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def tok(text, t): return len(re.findall(r'(?<![\w])' + re.escape(t) + r'(?![\w])', text))

hr('§1 THE DELIVERY AS BYTES — LW1-MANIFEST.tsv rows against the LW1-* members (convention: bytes AND md5 must match)')
rows = [l.split('\t') for l in rd('LW1-MANIFEST.tsv') if l.strip()][1:]
print('  MANIFEST DATA rows:', len(rows))
ok = 0
for name, nbytes, m, purpose in rows:
    b = open(os.path.join(H, 'LW1-' + name), 'rb').read(); v = (len(b) == int(nbytes) and md5(b) == m); ok += v
    print(f'  {name:16s} {len(b):6,} B  {md5(b)}  {"OK" if v else "MISMATCH"}   {purpose[:60]}')
print('  MANIFEST.tsv lists 3 of the zip\'s 4 files (README.md, ground.py, ground-run.log); it does not list itself — convention: the manifest is the witness, not a witnessed object')
print(f'  verdict: {ok}/{len(rows)} manifested files reproduce their bytes and md5')

hr('§2 THE DELIVERED INSTRUMENT RUN AS DELIVERED — python3 LW1-ground.py, stdout against LW1-ground-run.log (convention: byte identity)')
p = subprocess.run([sys.executable, os.path.join(H, 'LW1-ground.py')], cwd=H, capture_output=True, timeout=200)
gold = open(os.path.join(H, 'LW1-ground-run.log'), 'rb').read()
print(f'  returncode {p.returncode}; stdout {len(p.stdout):,} B md5 {md5(p.stdout)}; log {len(gold):,} B md5 {md5(gold)}')
print('  verdict: stdout == delivered log byte-for-byte:', p.stdout == gold, '(README states md5 6bc5a6196d6de9348b6618fb92d27fe4:', md5(gold) == '6bc5a6196d6de9348b6618fb92d27fe4', ')')
print('  stderr empty:', p.stderr == b'')

hr('§3 OWN RE-DERIVATION FROM THE DELIVERED TABLE (import by path; GROUND dict read, nothing computed by aufbau)')
G = load('LW1-ground', quiet=True)
Z_all = sorted(G.GROUND)
print('  Z range:', Z_all[0], 'to', Z_all[-1], '; elements:', len(Z_all))
bad = [Z for Z in Z_all if G.occ_count(Z) != Z]
print(f'  electron-count check (sum of occupancies == Z): {len(Z_all) - len(bad)}/{len(Z_all)}; mismatches: {bad}')
# opening sequence, own convention: a subshell OPENS at the least Z whose expanded configuration holds it with occupancy > 0
opening = {}
for Z in Z_all:
    for n, l, o in G.expand(Z):
        if o > 0 and (n, l) not in opening: opening[(n, l)] = Z
seq = sorted(opening, key=lambda k: opening[k]); Lc = 'spdfg'
name = lambda k: f'{k[0]}{Lc[k[1]]}'
print('  opening sequence (own convention, first Z with occupancy > 0):')
print('   ', ' '.join(name(k) for k in seq))
print('  count of subshells opened Z = 1..108:', len(seq), '(register 1307: nineteen; delivered log: 19)')
# the delivered script's own convention: a subshell is listed when its occupancy first RISES relative to Z-1 (starts at Z=2)
prev = None; seq2 = []
for Z in range(1, 109):
    cur = {(n, l): o for n, l, o in G.expand(Z)}
    if prev is not None:
        for k in cur:
            if (k not in prev or cur[k] > prev.get(k, 0)) and k not in [s for s in seq2]: seq2.append(k)
    prev = cur
print('  delivered convention (first rise vs Z-1, scanning from Z = 2) gives the same list:', seq == seq2, '; same length:', len(seq2))
madelung = sorted(seq, key=lambda k: (k[0] + k[1], k[0]))
diff = [(name(a), name(b)) for a, b in zip(seq, madelung) if a != b]
print('  Madelung order of the same nineteen (convention: sort by n+l, then n):')
print('   ', ' '.join(name(k) for k in madelung))
print('  positions where observed != Madelung (pairwise, observed vs Madelung):', diff, '; count', len(diff), '= two swaps of adjacent pairs:', diff == [('5d', '4f'), ('4f', '5d'), ('6d', '5f'), ('5f', '6d')])
print('  register 1307 says DIFFERS AT TWO OF NINETEEN — convention: two adjacent transpositions, four displaced positions; the entry counts transpositions.')
print(f'  La (57) opens 5d: opening[(5,2)] = {opening[(5, 2)]}; 4f first at Ce (58): {opening[(4, 3)]}; Ac (89) opens 6d: {opening[(6, 2)]}; 5f first at Pa (91): {opening[(5, 3)]}')
print('  Pd (46):', G.GROUND[46][1], '-> 4d / 5s occupancies (5s absent):', {k: o for (n, l, o) in G.expand(46) for k in [f"{n}{Lc[l]}"] if k in ('4d', '5s')})
print('  Lr (103):', G.GROUND[103][1], '-> 6d absent:', all(not (n == 6 and l == 2) for n, l, o in G.expand(103)), '; 7p present:', any(n == 7 and l == 1 and o > 0 for n, l, o in G.expand(103)))
# ground levels: every entry carries a non-empty level string
print('  ground level strings non-empty:', sum(1 for Z in Z_all if G.GROUND[Z][2]), '/', len(Z_all), '; the three bare J values (Sg 0, Bh 5/2, Hs 4) as delivered:', [G.GROUND[Z][2] for Z in (106, 107, 108)])

hr('§4 THE DELIVERED TABLE AGAINST THIS PROJECT\'S OWN RECONSTRUCTION (r2-ch16y §3 CONF, banked chat 126) — cell by cell')
Y = load('r2-ch16y', quiet=True)
mism = []
for Z in Z_all:
    mine = {f'{n}{Lc[l]}': o for n, l, o in G.expand(Z) if o > 0}
    theirs = {k: v for k, v in Y.CONF[Z].items() if v > 0}
    if mine != theirs: mism.append((Z, mine, theirs))
print(f'  Z = 1..108 configurations equal (subshell -> occupancy, zeros dropped): {108 - len(mism)}/108; mismatches: {mism}')
print('  the reconstruction was made in chat 126 without the delivered file; agreement is corroboration of the record, not of itself.')

hr('§5 THE REGISTER ANCHORS — 1306 and 1307 bodies read (rbody), figures scored against §3')
b6, b7 = rbody(1306), rbody(1307)
print('  1306 present:', b6 is not None, '; 1307 present:', b7 is not None)
print('  1306 tokens: "108 of 108" %d · "Pd" %d · "Lr" %d · "ground.py" %d · "NIST ASD 5.12" %d' % (tok(b6, '108 of 108'), tok(b6, 'Pd'), tok(b6, 'Lr'), b6.count('ground.py'), b6.count('NIST ASD 5.12')))
print('  1306 "108 of 108 electron counts validate" vs §3 108/108:', tok(b6, '108 of 108') == 1 and len(bad) == 0)
print('  1306 Pd [Kr]4d¹⁰ no 5s vs table [Kr]4d10:', G.GROUND[46][1] == '[Kr]4d10', '; Lr [Rn]5f¹⁴7s²7p vs table:', G.GROUND[103][1] == '[Rn]5f14 7s2 7p')
s7 = re.sub(r'\*', '', b7)
seqtxt = ' '.join(name(k) for k in seq)
print('  1307 prints the sequence "%s":' % seqtxt, seqtxt in re.sub(r'\s+', ' ', s7))
print('  1307 "TWO OF NINETEEN":', 'TWO OF NINETEEN' in b7, '; "La opens 5d at Z = 57":', 'La opens 5d at Z = 57' in b7, '(measured 57:', opening[(5, 2)] == 57, '); "Ac opens 6d at Z = 89":', 'Ac opens 6d at Z = 89' in b7, '(measured:', opening[(6, 2)] == 89, ')')
print('  1307 "4f does not appear until Ce" (Ce = 58):', opening[(4, 3)] == 58, '; "5f not until Pa" (Pa = 91):', opening[(5, 3)] == 91)
print('  WARNING lines on 1306 / 1307 (convention: the literal token WARNING in the body):', 'WARNING' in b6, 'WARNING' in b7)

hr('§6 STATUS OF THE TWELVE REQUESTED OBJECTS AS THE DELIVERY STATES THEM (LW1-README.md, its status table read as DATA rows)')
readme = rd('LW1-README.md'); tbl = [l for l in readme if l.startswith('|') and not l.startswith('|---') and 'status' not in l.split('|')[2]]
for l in tbl: print('  ', ' | '.join(c.strip() for c in l.strip('|').split('|')[:2]))
print('  status DATA rows:', len(tbl), '; DELIVERED rows:', sum('DELIVERED' in l for l in tbl), '; the rest are PENDING BANK / NOT HELD / PENDING M — record-carried in the book (docket 38).')
print('  the twelve objects (REQUEST-LOWDIN.md numbered items):', sum(1 for l in rd('REQUEST-LOWDIN.md') if re.match(r'^\d+\. ', l)))
print('  delivered object 3 reproduced (§2, §3, §5); objects 1, 2, 4-8, 10 pending a bank not delivered; 9 pending + not held; 11 not held; 12 pending M — reported not done, not silent.')
