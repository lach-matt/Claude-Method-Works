# r2-ch22a.py — Appendix D part 1 (main L10320–L10461, D.1–D.4.4.3), the COMPUTABLE claims (chat 135).
# Reads MEMBERS by name (never a bundle path); imports r2lib by path; deterministic (no wall-clock).
# Appendix D is read as DATA under chat-127 item 1. Every count names its convention before it is scored.
import os, re, io, sys, importlib.util, contextlib
from decimal import Decimal as D, ROUND_HALF_UP
from collections import Counter
import numpy as np, sympy as sp
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod); return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
M = L.read_member('The_Method_1_6-2.md').split('\n')
R = L.read_member('The_Method_1_6___The_Register-2.md').split('\n')

def rbody(n):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-ch21a.py (there from r2-ch20a.py / r2-ch19a.py / r2-ch18a.py / r2-ch17e.py / r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

def pct(a, b): return D(100 * a / b).quantize(D('0.1'), ROUND_HALF_UP) if b else None   # ROUND_HALF_UP, one place
print('r2-ch22a — Appendix D part 1 (D.1–D.4.4.3), computable claims; conventions named inline')

# §1 unit boundaries, measured
d = lettered(M, 'Appendix D'); e = lettered(M, 'Appendix E'); d5 = [i for i, l in enumerate(M, 1) if re.match(r'^### D\.5 ', l)]
print('§1 `## Appendix D` hits', d, '`## Appendix E` hits', e, '`### D.5` hits', d5, '; part 1 =', d[-1], 'to', d5[-1] - 1, '=', d5[-1] - d[-1], 'lines')
sub = [(i, l) for i, l in enumerate(M, 1) if d[-1] <= i < d5[-1] and re.match(r'^#{1,4} ', l)]
print('   headings in part 1:', len(sub), [l.split(' ')[1] for i, l in sub])

# §2 λ² = (2/3)T — symbolic, then the printed sweep. Convention: T = Z²R/ν², λ² = (T′)²/T″; the sweep is
# Z = 1…30 (integers) × ν = 400 equally spaced points on [1.01, 60] = 12,000 evaluations (the only grid of that size
# the sentence admits with integer Z); R = R∞ = 109737.31568160 cm⁻¹ (scale-free in the relative error); float64.
Z, nu, Rc = sp.symbols('Z nu R', positive=True); T = Z**2 * Rc / nu**2
lam2 = sp.simplify(sp.diff(T, nu)**2 / sp.diff(T, nu, 2)); print('§2 symbolic λ² = (T′)²/T″ =', lam2, '; equals (2/3)T:', sp.simplify(lam2 - sp.Rational(2, 3) * T) == 0)
Zs = np.arange(1, 31, dtype=np.float64); nus = np.linspace(1.01, 60.0, 400); Rv = 109737.31568160
ZZ, NN = np.meshgrid(Zs, nus, indexing='ij'); Tv = ZZ**2 * Rv / NN**2; T1 = -2 * ZZ**2 * Rv / NN**3; T2 = 6 * ZZ**2 * Rv / NN**4
lv = T1**2 / T2; rel = np.abs(lv - (2 / 3) * Tv) / ((2 / 3) * Tv)
print('   sweep: evaluations', lv.size, '(30 × 400); violations of λ² ≤ (2/3)T beyond 1e-12:', int((rel > 1e-12).sum()), '; worst relative error %.2e' % rel.max(), '; printed 7.1 × 10⁻¹⁶')
for g in (300, 401, 200):   # the grid the sentence does not fix: two neighbouring conventions, for the record
    nn = np.linspace(1.01, 60.0, g); Z2, N2 = np.meshgrid(Zs, nn, indexing='ij'); t = Z2**2 * Rv / N2**2
    r2 = np.abs((-2 * Z2**2 * Rv / N2**3)**2 / (6 * Z2**2 * Rv / N2**4) - (2 / 3) * t) / ((2 / 3) * t); print('   alt grid 30 ×', g, '=', r2.size, 'worst %.2e' % r2.max())

# §3 Λ₈ rebuilt, the defining system F (Chapter 7) and the recovery operator ℛ.
with contextlib.redirect_stdout(io.StringIO()): T8 = L.load_tower()
cells = [tuple(int(v) for v in c) for c in T8.L8()]; n8 = len(cells); A = np.array(cells, dtype=np.int64); names = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S']
print('§3 |Λ₈| =', n8, '(tower-2); coordinates', names)
caps = A.max(axis=0); print('   coordinate maxima', dict(zip(names, caps.tolist())))
# F: the seven bounds of Chapter 7 (ℓ≤n−1, k≤4ℓ+2, q≤k, f≤e−1, g≤4f+2, g≤q, 2S≤k) with the caps; convention: a bound = an ordered pair (bounded, bounding)
F_edges = [('ℓ', 'n'), ('k', 'ℓ'), ('q', 'k'), ('f', 'e'), ('g', 'f'), ('g', 'q'), ('2S', 'k')]
box = [tuple(x) for x in np.array(np.meshgrid(*[np.arange(0, c + 1) for c in caps], indexing='ij')).reshape(8, -1).T.tolist()]
def inF(x):
    n, l, k, q, e, f, g, S = x
    return 1 <= n and l <= n - 1 and 1 <= k <= 4 * l + 2 and q <= k and 1 <= e and f <= e - 1 and g <= min(4 * f + 2, q) and S <= k
Fset = {x for x in box if inF(x)}; print('   box', len(box), 'cells; F (seven bounds + caps + the two floors n,k,e ≥ 1) generates', len(Fset), '; equals Λ₈:', Fset == set(cells))
# caterpillar: the bound graph of F on eight nodes
deg = Counter(); [deg.update([a, b]) for a, b in F_edges]
print('   F bound graph: 7 edges on 8 nodes, degrees', dict(deg), '; pendant at k (2S):', deg['2S'] == 1 and ('2S', 'k') in F_edges, '; path n–ℓ–k–q–g–f–e of 7 nodes:', all(deg[v] <= 3 for v in deg))
# ℛ: φ_ij(v) = max{x_i : x ∈ X, x_j = v}. Convention: an ordered pair (i, j), i ≠ j, gives one recovered bound; 8·7 = 56.
def recover(X):
    X = np.array(sorted(X), dtype=np.int64); phi = {}
    for i in range(8):
        for j in range(8):
            if i == j: continue
            phi[(i, j)] = {int(v): int(X[X[:, j] == v, i].max()) for v in np.unique(X[:, j])}
    return phi
def generate(phi, X):   # pointwise minimum over the recovered bounds, on the box of the source's coordinate maxima
    return {x for x in box if all(x[i] <= min(phi[(i, j)].get(x[j], -1) for j in range(8) if j != i) for i in range(8))}
phi = recover(cells); gen = generate(phi, cells)
print('   ℛ(Λ₈): ordered pairs i≠j =', len(phi), '; pointwise-minimum reconstruction generates', len(gen), '; = Λ₈:', gen == set(cells), '(printed 976 = 976)')
# which recovered bounds are non-trivial (non-constant in v) — the candidate reading of forty-eight
nontriv = [(i, j) for (i, j), f in phi.items() if len(set(f.values())) > 1]
print('   non-constant recovered bounds (φ_ij varies with v):', len(nontriv), '; constant:', len(phi) - len(nontriv))
# which bounds CONSTRAIN: dropping the bound (alone) enlarges the generated set — the candidate reading of sixteen
def gen_without(drop):
    return sum(1 for x in box if all(x[i] <= min([phi[(i, j)].get(x[j], -1) for j in range(8) if j != i and (i, j) != drop] or [caps[i]]) for i in range(8)))
constrain = [(i, j) for (i, j) in phi if gen_without((i, j)) != n8]
print('   bounds whose sole removal changes the generated set:', len(constrain), sorted((names[i], names[j]) for i, j in constrain), '(printed: sixteen that constrain, of fifty-six)')
# tightest bound per coordinate: convention — for cell x and coordinate i, the set of j attaining min_j φ_ij(x_j); ties credit every attaining j
tight = {i: Counter() for i in range(8)}; tie_any = 0; tie_all = 0
for x in cells:
    cell_tie = []
    for i in range(8):
        vals = {j: phi[(i, j)][x[j]] for j in range(8) if j != i}; m = min(vals.values()); att = [j for j, v in vals.items() if v == m]
        for j in att: tight[i][j] += 1
        cell_tie.append(len(att) >= 2)
    tie_any += any(cell_tie); tie_all += all(cell_tie)
for i in (6, 3):
    print('   tightest for', names[i] + ':', ', '.join('%s %s%%' % (names[j], pct(c, n8)) for j, c in tight[i].most_common()), '; every partner tightest somewhere:', len(tight[i]) == 7)
print('   printed D.4.2 for g: q 92.6, k 39.9, f 35.1, n 11.2; D.4.3 for g: q 93, k 40, f 35, ℓ 20; for q: k 100, ℓ 66, n 48')
print('   cells with two bounds tied at the minimum — some coordinate:', tie_any, 'of', n8, '(%s%%)' % pct(tie_any, n8), '; every coordinate:', tie_all, 'of', n8, '(printed 976 of 976 — 100%)')
print('   coordinates with >1 bound under ℛ:', sum(1 for i in range(8) if sum(1 for j in range(8) if j != i) > 1), 'of 8; bounds per coordinate:', sorted({sum(1 for j in range(8) if j != i) for i in range(8)}))
# idempotence: ℛ(generate(ℛ(Λ))) == ℛ(Λ), twice
phi2 = recover(gen); gen2 = generate(phi2, gen); phi3 = recover(gen2)
print('   idempotent: ℛ∘gen∘ℛ = ℛ:', phi2 == phi, '; and again:', phi3 == phi, '; generated', len(gen2))

# §4 maximal chains of Λ₈ under the product order. Convention: a chain from a minimal element to a maximal element
# through covers (y ⋖ x iff y < x componentwise and no z ∈ Λ₈ with y < z < x); count = number of such paths.
idx = {c: i for i, c in enumerate(cells)}; leq = np.all(A[:, None, :] <= A[None, :, :], axis=2); lt = leq & ~np.eye(n8, dtype=bool)
cover = lt & ~np.any(lt[:, :, None] & lt[None, :, :], axis=1)
mins = [i for i in range(n8) if not lt[:, i].any()]; maxs = [i for i in range(n8) if not lt[i].any()]
order = sorted(range(n8), key=lambda i: (int(A[i].sum()), cells[i])); paths = [0] * n8
for i in mins: paths[i] = 1
for i in order:
    for j in np.nonzero(cover[i])[0]: paths[j] += paths[i]
total = sum(paths[i] for i in maxs)
print('§4 minimal elements', [cells[i] for i in mins], '; maximal elements', len(maxs), '; covers', int(cover.sum()), '; maximal chains', f'{total:,}', '(printed 1,113,045,672 at L10442; other sites', [i for i, l in enumerate(M, 1) if '1,113,045,672' in l], ')')

# §5 pointers named in part 1, resolved to the claim under both resolvers (convention: a pointer resolves when the
# section's body_range OR its section_span carries the claim token, word-bounded, case-insensitive)
probes = [('16.7.1', ['separating', 'missing constraint', 'diagnostic']), ('11.5', ['min', 'coupling']), ('11.7', ['tree', 'closed expression', 'closed form']),
          ('12.9', ['1,113,045,672', 'maximal chain']), ('11.1', ['six', 'language'])]
for sec, toks in probes:
    br = body_range(M, sec); ss = section_span(M, sec)
    for t in toks:
        b = sum(1 for l in M[br[0]:br[1] - 1] if has_token(l, t) or t in l); s = sum(1 for l in M[ss[0]:ss[1] - 1] if has_token(l, t) or t in l)
        print('§5 §%s %s body_range %s: %d ; section_span %s: %d' % (sec, repr(t), br, b, ss, s))
c23 = [i for i, l in enumerate(M, 1) if 'Nesterov' in l]; print('   Nesterov sites (Chapter 23 citation claim, L10377):', c23, '; enclosing headings:', [next(M[k - 1][:28] for k in range(i, 0, -1) if re.match(r'^#{1,4} ', M[k - 1])) for i in c23[:3]])
print('   Figure 11.1 caption line:', [i for i, l in enumerate(M, 1) if re.search(r'Figure 11\.1\b', l)][:4], '; P21 sites:', [i for i, l in enumerate(M, 1) if re.search(r'\bP21\b', l)][:8])

# §6 Register entries naming Appendix D: heading number, WARNING line present?
hits = [i for i, l in enumerate(R, 1) if 'Appendix D' in l]
for i in hits:
    h = next((R[k - 1].strip() for k in range(i, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[k - 1])), None)
    warn = any('WARNING' in R[k] for k in range(i - 1, min(i + 40, len(R))) if not re.match(r'^#{1,4}\s*\d+\s*$', R[k]))
    print('§6 Register L%d entry %s WARNING-in-body: %s :: %s' % (i, h, warn, R[i - 1][:110]))
print('§7 forty-eight / fifty-six sites in the unit:', [i for i, l in enumerate(M, 1) if d[-1] <= i < d5[-1] and re.search(r'forty-eight|fifty-six', l)],
      '; the twin restatement at D.5.1:', [i for i, l in enumerate(M, 1) if d5[-1] <= i < e[-1] and re.search(r'92\.6|39\.9|fifty-six', l)])
print('done')
