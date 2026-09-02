#!/usr/bin/env python3
# r2-tb1.py — chat 130 — Segment A intake: THREEBODY-DELIVERY-1 (RUL-128 item 4; DEF-129 item 7; docket 38).
# Reads MEMBERS only: TB1-* (the delivery's fifteen text files, bytes unchanged under a prefix) and the Register member.
# The five PNGs are NOT members (binary); their md5s are the MANIFEST's rows and are reported, not re-rendered here.
# Every delivered instrument is a LABELLED RECONSTRUCTION (no original md5 exists): a match here is the reconstruction
# reproducing the record, never the record reproducing itself. Conventions named before verdicts; Decimal, never round();
# a count word counts DATA rows; every negative carries its witness.
import os, re, io, sys, hashlib, subprocess, itertools, contextlib
from decimal import Decimal as D, getcontext, ROUND_HALF_UP
getcontext().prec = 40
import numpy as np, sympy as sp
H = os.path.dirname(os.path.abspath(__file__))
md5 = lambda b: hashlib.md5(b).hexdigest()
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
R = rd('The_Method_1_6___The_Register-2.md')
def rbody(n):   # copied verbatim from r2-ch17c.py (there from r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))

hr('§1 THE DELIVERY AS BYTES — TB1-MANIFEST.tsv rows against the TB1-* members (convention: bytes AND md5 must match; PNG rows reported, not members)')
rows = [l.split('\t') for l in rd('TB1-MANIFEST.tsv') if l.strip()][1:]
print('  MANIFEST DATA rows:', len(rows), '(README says 20 zip members = 19 rows + MANIFEST.tsv itself)')
ok = 0; png = 0
for name, nbytes, m, purpose in rows:
    if name.endswith('.png'):
        png += 1; print(f'  {name:28s} {int(nbytes):8,} B  {m}  PNG not a member — md5 as manifested; chat 130 measured the re-render byte-identical (W-170)'); continue
    b = open(os.path.join(H, 'TB1-' + name), 'rb').read(); v = (len(b) == int(nbytes) and md5(b) == m); ok += v
    print(f'  {name:28s} {len(b):8,} B  {md5(b)}  {"OK" if v else "MISMATCH"}   {purpose[:70]}')
print(f'  verdict: {ok}/{len(rows) - png} text files reproduce bytes and md5; {png} PNG rows reported')
print('  RECONSTRUCTED rows (the word in the purpose column):', sum('RECONSTRUCTED' in r[3] for r in rows), '; new thin drivers:', sum('new' in r[3] for r in rows))

hr('§2 THE DELIVERED INSTRUMENTS RUN AS DELIVERED — stdout against the delivered logs (convention: byte identity; caps_table on its five data columns, its sixth is wall-clock)')
for inst in ('audit', 'audit_state1_failing', 'n8_check', 'routh_check'):
    p = subprocess.run([sys.executable, os.path.join(H, f'TB1-{inst}.py')], cwd=H, capture_output=True, timeout=200)
    gold = open(os.path.join(H, f'TB1-{inst}.log'), 'rb').read()
    print(f'  {inst:22s} rc {p.returncode}  stdout {len(p.stdout):5,} B md5 {md5(p.stdout)[:8]}  log md5 {md5(gold)[:8]}  byte-identical: {p.stdout == gold}  stderr empty: {p.stderr == b""}')
src = open(os.path.join(H, 'TB1-audit.py'), encoding='utf-8').read().split('print("case')[0]   # the delivery's own split convention (caps_table.py, figs.py)
ns = {}; exec(src, ns)                                                                          # the delivered closure operator, as delivered
caps = list(range(3, 13)); rows_d = [ns['closure_test'](c) for c in caps]
ct = [l.split('\t') for l in rd('TB1-caps_table.log') if l.strip()][1:]
mine = [[str(c), str(n), str(mf), str(jf), str(tf)] for c, (n, mf, jf, tf) in zip(caps, rows_d)]
print('  caps_table.log DATA rows:', len(ct), '; five data columns equal to the delivered operator re-run:', [r[:5] for r in ct] == mine)
figs_line = str([(c,) + r for c, r in zip(caps, rows_d)])
print('  figs.log (the caps list figs.py prints; figs.py itself not run — matplotlib, binary output) equals the re-run string:', rd('TB1-figs.log')[0] == figs_line)
print('  audit_state1_failing.py vs audit.py: differing lines (convention: unified diff, non-comment):')
d1, d2 = rd('TB1-audit_state1_failing.py'), rd('TB1-audit.py')
for i, (a, b) in enumerate(zip(d1, d2), 1):
    if a != b: print(f'    L{i}: {a.strip()[:90]}  ->  {b.strip()[:90]}')

hr('§3 OWN RE-DERIVATION, INDEPENDENT OF THE DELIVERED CODE')
# 3a the triangle-form closure: cells {(a,b,c) in [1,cap]^3 : |a-b| <= c <= a+b}; meet = componentwise min, join = componentwise max
def closure(cap):
    S = {(a, b, c) for a in range(1, cap + 1) for b in range(1, cap + 1) for c in range(1, cap + 1) if abs(a - b) <= c <= a + b}
    cells = sorted(S); mf = jf = 0
    for x, y in itertools.combinations(cells, 2):
        if (min(x[0], y[0]), min(x[1], y[1]), min(x[2], y[2])) not in S: mf += 1
        if (max(x[0], y[0]), max(x[1], y[1]), max(x[2], y[2])) not in S: jf += 1
    return len(cells), mf, jf
def chain(cap):   # two-body analogue as the delivery defines it: {(a,b): 1<=b<=a<=cap}, min/max componentwise
    T = {(a, b) for a in range(1, cap + 1) for b in range(1, a + 1)}
    return sum(1 for x, y in itertools.combinations(sorted(T), 2) if (min(x[0], y[0]), min(x[1], y[1])) not in T or (max(x[0], y[0]), max(x[1], y[1])) not in T)
own = [closure(c) + (chain(c),) for c in caps]
print('  cap  cells  meet  join  chain   (own)')
for c, (n, mf, jf, tf) in zip(caps, own): print(f'  {c:3d} {n:6d} {mf:6d} {jf:5d} {tf:5d}')
print('  own == delivered operator at every cap:', [tuple(r) for r in own] == [tuple(r) for r in rows_d])
print('  cap 8: cells 344, meet 8,385, join 0, chain 0:', own[caps.index(8)] == (344, 8385, 0, 0))
print('  meet failures caps 3-12 = 12 111 477 1488 3780 8385 16812 31227 54555 90705:', [r[1] for r in own] == [12, 111, 477, 1488, 3780, 8385, 16812, 31227, 54555, 90705])
print('  join failures all 0:', all(r[2] == 0 for r in own), '; chain failures all 0:', all(r[3] == 0 for r in own))
print('  denominator named: pairs at cap 8 = C(344, 2) =', 344 * 343 // 2, '; meet-failure share', q(D(8385) / D(344 * 343 // 2), '0.0001'))
# 3b thirteen order-types = the weak orderings of three labelled masses (ordered Bell number a(3) = 13)
def weak(m): return tuple(sorted(range(3), key=lambda i: m[i])), tuple(m[i] == m[j] for i, j in ((0, 1), (1, 2), (0, 2)))
kinds = {weak(m) for m in ns['cases'].values()}
print('  delivered cases:', len(ns['cases']), '; distinct weak orderings realised:', len(kinds), '; ordered Bell number for n = 3 is 13:', len(kinds) == 13)
# name the duplicate and the missing ordering (convention: an ordering is written as the labels in ascending mass, "=" for a tie)
def word(m):
    lab = 'xyz'; order = sorted(range(3), key=lambda i: m[i]); s = lab[order[0]]
    for a_, b_ in zip(order, order[1:]): s += ('=' if m[a_] == m[b_] else '<') + lab[b_]
    return s
seen = {}
for k, m in ns['cases'].items(): seen.setdefault(word(m), []).append((k, m))
dups = {w: v for w, v in seen.items() if len(v) > 1}
allw = set()
for m in itertools.product([1, 2, 3], repeat=3): allw.add(word(m))
print('  duplicate orderings among the 13 labels:', dups)
print('  orderings of three labelled masses never realised by the 13 labels:', sorted(allw - set(seen)), '(of', len(allw), 'weak orderings)')
full = open(os.path.join(H, 'TB1-audit.py'), encoding='utf-8').read()
key = ' "x>z, z>y":(3,1,2),'; assert full.count(key) == 1
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(full.replace(key, key + ' "z<x<y (added)":(2,3,1),'), {})
extra = [l for l in buf.getvalue().split('\n') if l.startswith('z<x<y')]
print('  the missing ordering run through the delivered six checks as a 14th case (RNG draws of the 13 unchanged, it is appended):', extra)
print('  all six True for z<x<y:', bool(extra) and extra[0].count('True') == 5 and 'False' not in extra[0])
print('  FINDING ABOUT THE RECONSTRUCTION (labelled reconstruction, no original): the label "x<y, y>z" at (1,3,2) and "x<z, z<y" at (1,3,2.5) are one ordering x<z<y; z<x<y is untested. 1717\'s 13 x 6 = 78 counts labels; every check is True at all 13, so 78/78 stands as printed. Flag to the three-body project; not a book deviation without the original instrument.')
S_orders = sorted((sum(1 for p in itertools.permutations(range(3)) if all(m[p[i]] == m[i] for i in range(3))) for m in ns['cases'].values()), reverse=True)
print('  symmetry orders |S| over the 13 cases (own count of mass-preserving permutations):', S_orders, '; values {6, 2, 1}:', set(S_orders) == {6, 2, 1})
print('  checks per case 6 (A-F) x 13 = 78:', 6 * 13)
# 3c N8: the norm over (Z/2)^3 vs the withdrawn polynomial, in p, q, r
V, u1, u2, u3, p_, q_, r_ = sp.symbols('V u1 u2 u3 p q r')
P8 = sp.expand(sp.prod([V - e1 * u1 - e2 * u2 - e3 * u3 for e1, e2, e3 in itertools.product([1, -1], repeat=3)]))
sub = {p_: u1**2 + u2**2 + u3**2, q_: u1**2 * u2**2 + u2**2 * u3**2 + u3**2 * u1**2, r_: u1**2 * u2**2 * u3**2}
N8 = V**8 - 4 * p_ * V**6 + (6 * p_**2 - 8 * q_) * V**4 + (-4 * p_**3 + 16 * p_ * q_ - 64 * r_) * V**2 + (p_**2 - 4 * q_)**2
print('  N8 compact form == product over (Z/2)^3:', sp.expand(P8 - N8.subs(sub)) == 0)
S2, S4, S6, S11 = sub[p_], u1**4 + u2**4 + u3**4, u1**6 + u2**6 + u3**6, sub[q_]
wU4 = sp.expand(6 * S2**2 - 4 * S4 + 8 * S11)
print('  withdrawn U^4 coefficient 6S2^2 - 4S4 + 8S11 in p, q equals 2p^2 + 16q (1719):', sp.expand(wU4 - (2 * p_**2 + 16 * q_).subs(sub)) == 0, '; true is 6p^2 - 8q:', sp.expand(sp.Poly(N8, V).coeff_monomial(V**4) - (6 * p_**2 - 8 * q_)) == 0)
wU2 = sp.expand(-4 * (S2**3 - S2 * S4 + 2 * S6))
print('  withdrawn U^2 coefficient equals the true one:', sp.expand(wU2 - sp.Poly(N8, V).coeff_monomial(V**2).subs(sub)) == 0, '(1719: likewise wrong)')
print('  N8 at u = (3, 5, 7), V = 15 (= 3+5+7, a root by construction):', sp.expand(P8.subs({u1: 3, u2: 5, u3: 7, V: 15})))
# 3d Routh threshold, closed form and from 27 mu (1 - mu) = 1
mu = (D(9) - D(69).sqrt()) / D(18); mu2 = (D(1) - (D(1) - D(4) / D(27)).sqrt()) / D(2)
print('  Routh mu_1 = (9 - sqrt 69)/18 =', q(mu, '0.0000000001'), '; from 27 mu(1-mu) = 1:', q(mu2, '0.0000000001'), '; equal to 1e-12:', abs(mu - mu2) < D('1e-12'), '; 27 mu (1-mu) =', q(27 * mu * (1 - mu), '0.000000000001'))
print('  record prints 0.0385209 (README): agrees at 7 decimals HALF_UP:', q(mu, '0.0000001') == '0.0385209')
# 3e Euler collinear quintic: one positive real root per ordering, own root-finder (numpy) over the 13 mass cases
def euler(m):
    m1, m2, m3 = m; co = [(m1 + m2), (3 * m1 + 2 * m2), (3 * m1 + m2), -(m2 + 3 * m3), -(2 * m2 + 3 * m3), -(m2 + m3)]
    return sum(1 for r in np.roots(co) if abs(r.imag) < 1e-9 and r.real > 0)
print('  Euler quintic positive real roots per case (own numpy roots):', sorted({euler(m) for m in ns['cases'].values()}), '; one per ordering at all 13:', all(euler(m) == 1 for m in ns['cases'].values()))
print('  Descartes: the quintic has exactly one sign change in its coefficients for positive masses -> exactly one positive root (theorem; the numeric is the witness)')

hr('§4 THE REGISTER ANCHORS 1713-1724 — existence, bodies (rbody), figures, WARNING lines')
for n in (1710, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1756):
    b = rbody(n); print(f'  {n}: {"ABSENT" if b is None else "present"}' + ('' if b is None else f'  WARNING: {"WARNING" in b}  len {len(b)}'))
b16, b17, b18, b19, b20, b21 = (rbody(n) for n in (1716, 1717, 1718, 1719, 1720, 1721))
print('  1716 "344 cells" / "0 join failures" / "8,385 meet failures" / "caps 3–12" / "3B.tri" / "chain 0":', [t in b16 for t in ('344 cells', '0 join failures', '8,385 meet failures', 'caps 3–12', '3B.tri', 'chain 0')])
print('  1716 figures vs §3a (344 / 8385 / 0 / 0):', own[caps.index(8)] == (344, 8385, 0, 0))
print('  1717 "13 mass order-types × 6 checks = 78/78" / "6, 2, 1":', '78/78' in b17, '6, 2, 1' in b17, '; vs §3b:', len(kinds) == 13 and set(S_orders) == {6, 2, 1})
print('  1718 "failed 13/13" / "hyper-radius":', 'failed 13/13' in b18, 'hyper-radius' in b18, '; delivered failing log check A False at 13 rows:', sum('False' in l.split('|')[1] for l in rd('TB1-audit_state1_failing.log') if l.count('|') >= 6 and not l.startswith('case')))
print('  1719 "2p² + 16q" / "6p² − 8q" / "withdrawn":', '2p² + 16q' in b19, '6p² − 8q' in b19, 'withdrawn' in b19, '; vs §3c: True True')
print('  1720 "(ℤ/2)³" / "1770":', '(ℤ/2)³' in b20, '1770' in b20)
print('  1721 "Eight attribution questions" / "seven closed":', 'Eight attribution questions' in b21, 'seven closed' in b21, '; README: the ledger file NOT HELD; the delivery states seven + Lagrange 1770 as the eighth — the entry says seven closed; the eighth question is left as the record has it (Segment B tests main L9903)')
print('  a Register entry citing "tb_audit.py": lines', [i + 1 for i, l in enumerate(R) if 'tb_audit' in l], '(convention: substring over the Register member)')

hr('§5 STATUS OF THE TEN REQUESTED OBJECTS AS THE DELIVERY STATES THEM (TB1-README.md status table, DATA rows)')
readme = rd('TB1-README.md'); i0 = next(i for i, l in enumerate(readme) if l.startswith('| object'))
tbl = []
for l in readme[i0 + 1:]:
    if not l.startswith('|'): break
    if not l.startswith('|---'): tbl.append(l)   # the first table only, header and rule excluded
for l in tbl:
    c = [x.strip() for x in l.strip('|').split('|')]; print('  ', c[0][:52].ljust(52), '|', c[1][:60])
print('  status DATA rows:', len(tbl), '; REQUEST-THREEBODY.md numbered items:', sum(1 for l in rd('REQUEST-THREEBODY.md') if re.match(r'^\d+\. ', l)))
print('  reproduced here: objects 1, 2, 3, 4, 7 (instruments) and 9 (logs; PNGs measured out of band); derived by reading: 5; NOT HELD: 6 (never data), 8 (ledger file); 10: PDF on Drive not fetched this chat, .md member is the build\'s own.')
print('  REQUEST item 1 cites register 1756 for tb_audit.py: 1756 is ABSENT (§4); main L9903 carries the same citation — Segment B site.')
