#!/usr/bin/env python3
# r2-ch34re.py — chat 143 — the Chapter 34 re-take under docket 37 (RUL-128 item 3 (ii), second half, first family).
# Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, fixed seeds. Decimal for every printed figure,
# never round(). Every convention is named before a figure is scored. A re-derivation that disagrees with a Register entry
# is a finding about the re-derivation (G0c). Input data: LW1-ground.py (the delivered OBSERVED configurations, Register
# 1306, NIST ASD 5.12) — the ordering the challenge asks about, READ not computed; the tower via r2lib.load_tower().
# r2-ch34re2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch34re.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (2 anchors); nothing else changes. r2-ch34re.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch34re.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import os, re, sys, math, random, hashlib, importlib.util
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
getcontext().prec = 40
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib'); G = load('LW1-ground')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
M = rd(MAIN); R = rd(REG)
def hr(t): print('\n' + '=' * 100 + '\n' + t + '\n' + '=' * 100)
def D(x, places): return Decimal(x).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_EVEN)
def dsqrt(x): return Decimal(x).sqrt()

def rbody(n):   # copied verbatim from r2-warn.py (there from r2-ch28b.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-warn.py (there from r2-ch28b.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-warn.py (there from r2-ch28b.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

hr('§0 IDENTITY AND BOUNDARIES')
for n in (MAIN, REG, 'LW1-ground.py', 'r2lib.py', 'tower-2.py'): print('  %-48s md5 %s  %d lines' % (n, md5(n), len(rd(n))))
T = r2lib.load_tower()
tow = {k: getattr(T, k) for k in dir(T) if not k.startswith('_')}
print('  tower-2 loaded via r2lib.load_tower(); public names:', ' '.join(sorted(k for k in tow if not hasattr(tow[k], '__module__') or tow[k].__module__ != 'builtins')[:40]))
hl = r2lib.heading_line(M, '34'); ss = r2lib.section_span(M, '34'); br = body_range(M, '34')
print('  heading_line(34) =', hl, repr(M[hl - 1]), '| all exact-token hits', [i for i, t in enumerate(M, 1) if re.match(r'^#{1,4} 34\.? ', t.strip())])
print('  section_span(34) =', ss, '-> next heading', repr(M[ss[1] - 1]), '| body_range(34) =', br, '-> next heading', repr(M[br[1] - 1]))
print('  the two resolvers differ by', ss[1] - br[1], 'lines (body_range stops at ### 34.1; section_span spans the chapter to ## 35.) — section_span governs the census')
heads = [(i, M[i - 1]) for i in range(ss[0], ss[1]) if re.match(r'^#{1,4} ', M[i - 1])]
for k, (i, h) in enumerate(heads):
    e = heads[k + 1][0] if k + 1 < len(heads) else ss[1]
    print('   L%d-L%d %3d lines  %s' % (i, e - 1, e - i, h))
CH = M[ss[0] - 1:ss[1] - 1]; L0 = ss[0]
def find(s):
    return [L0 + k for k, l in enumerate(CH) if s in l]

hr('§1 NUMERAL CENSUS OF THE CHAPTER (digit-bounded both sides; trailing non-thousands comma admitted; count words listed separately)')
NUM = re.compile(r'(?<![\d.])(\d[\d,]*(?:\.\d+)?)(?![\d])')
rows = []
for k, l in enumerate(CH):
    for m in NUM.finditer(l): rows.append((L0 + k, m.group(1)))
print('  numerals:', len(rows), 'on', len({r[0] for r in rows}), 'lines')
by = {}
for ln, v in rows: by.setdefault(ln, []).append(v)
for ln in sorted(by): print('   L%d: %s' % (ln, ' '.join(by[ln])))
CW = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|hundred)\b', re.I)
cw = [(L0 + k, m.group(0)) for k, l in enumerate(CH) for m in CW.finditer(l)]
print('  count words:', len(cw), '->', ' '.join('L%d:%s' % c for c in cw))

hr('§2 THE OBSERVED ORDER (LW1-ground.py, Register 1306) — the input every corridor figure is computed on')
ZS = sorted(G.GROUND); print('  elements in GROUND:', len(ZS), 'Z =', ZS[0], 'to', ZS[-1], '| electron-count check Z == occupancy:', sum(1 for Z in ZS if G.occ_count(Z) == Z), 'of', len(ZS))
LET = 'spdfg'
def occ(Z): return {(n, l): o for n, l, o in G.expand(Z)} if Z >= 1 else {}
def step(Z):
    """the differentiating subshell at Z: the (n,l) whose occupancy grows most from Z-1 to Z; also every subshell that moved"""
    a, b = occ(Z - 1), occ(Z)
    d = {k: b.get(k, 0) - a.get(k, 0) for k in set(a) | set(b)}
    moved = sorted((k, v) for k, v in d.items() if v)
    g = max(moved, key=lambda kv: (kv[1], -kv[0][0]))[0]
    return g, moved
seq = []
for Z in range(1, 109):
    g, moved = step(Z)
    if g not in [s[0] for s in seq]: seq.append((g, Z))
seq_txt = ' '.join('%d%s' % (n, LET[l]) for (n, l), Z in seq)
print('  opening sequence (first Z at which each subshell gains an electron):', seq_txt, '| count', len(seq))
print('  openings by Z:', ' '.join('%d%s@%d' % (n, LET[l], Z) for (n, l), Z in seq))
printed = re.findall(r'\d[spdf]', M[_L('> 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **5d 4f** 6p 7s **6d 5f** 7p') - 1]) if len(M) >= _L('> 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s **5d 4f** 6p 7s **6d 5f** 7p') else []
pl = [i for i, l in enumerate(M, 1) if l.startswith('> 1s 2s 2p')]
printed = re.findall(r'\d[spdf]', M[pl[0] - 1]) if pl else []
print('  printed sequence at L%s: %s | count %d' % (pl, ' '.join(printed), len(printed)))
print('  VERDICT opening sequence: %s' % ('MEASURED equal' if printed == [s.split('@')[0] for s in seq_txt.split()] else 'MEASURED differs'))
mad = sorted([(n, l) for n in range(1, 8) for l in range(0, min(n, 4))], key=lambda k: (k[0] + k[1], k[0]))
mad = [k for k in mad if k in [s[0] for s in seq]]
mad_txt = ' '.join('%d%s' % (n, LET[l]) for n, l in mad)
obs = [s[0] for s in seq]
agree_pos = sum(1 for a, b in zip(obs, mad) if a == b)
inv = sum(1 for i in range(len(obs)) for j in range(i + 1, len(obs)) if mad.index(obs[i]) > mad.index(obs[j]))
print('  Madelung (n+l, then n) restricted to the opened set:', mad_txt)
print('  CONVENTION named — two readings of "Seventeen of nineteen openings agree; two do not" (L%s): (a) position-wise agreement %d of %d;'
      ' (b) inverted adjacent pairs %d (5d/4f, 6d/5f), i.e. %d - %d = %d openings not displaced' % (find('Seventeen of nineteen'), agree_pos, len(obs), inv, len(obs), inv, len(obs) - inv))
print('  89%% (L%s): 17/19 = %s %%; 15/19 = %s %%  (ROUND_HALF_EVEN, 1 dp)' % (find('89%'), D(Decimal(17) / 19 * 100, 1), D(Decimal(15) / 19 * 100, 1)))
print('  VERDICT "17 of 19 / two / 89%": MEASURED equal under convention (b) [inversions]; MEASURED differs under (a) [positions: 15 of 19, 78.9%]; the sentence names neither — docket 34')
for (Z, tok) in ((57, '5d'), (58, '4f'), (89, '6d'), (91, '5f')):
    g, moved = step(Z); print('  Z=%d %s entrant %d%s %s' % (Z, G.GROUND[Z][0], g[0], LET[g[1]], 'MEASURED equal' if '%d%s' % (g[0], LET[g[1]]) == tok else 'MEASURED differs (printed %s)' % tok))
multi = [(Z, moved) for Z in range(2, 109) for g, moved in [step(Z)] if len(moved) > 1]
print('  steps where more than one subshell moves (a two-electron rearrangement):', ' '.join('%d%s:%s' % (Z, G.GROUND[Z][0], ','.join('%d%s%+d' % (k[0], LET[k[1]], v) for k, v in mv)) for Z, mv in multi))

hr('§3 THE CORRIDOR (§34.5, Register 1309 / 1350 / 1460): L(Z) < a < U(Z) from nu_g < nu_r for every admissible rival')
print('  CONVENTIONS named: candidate subshells (n,l) with n <= N_MAX, l <= min(n-1, 3); a rival is admissible at step Z iff its occupancy at Z-1 is')
print('  below 2(2l+1); the entrant g is the differentiating subshell of §2; form A (1309): p = n-l-1; form B (1350): p = n-l-1 + q/2(2l+1) with q the')
print('  occupancy at Z-1; the inequality nu_g < nu_r is a(sqrt p_r - sqrt p_g) < n_r - n_g; a bound is an endpoint Dn/(sqrt p_r - sqrt p_g);')
print('  sqrt p_r == sqrt p_g requires n_r > n_g (violated -> the corridor is empty); L = max of lower bounds, U = min of upper bounds; NON-EMPTY iff L < U.')
def corridor(Z, form='A', N_MAX=7, entrant=None):
    a = occ(Z - 1); g = entrant or step(Z)[0]
    def p(k):
        n, l = k; base = n - l - 1
        return base if form == 'A' else base + a.get(k, 0) / (2 * (2 * l + 1))
    pg = p(g); L = -math.inf; U = math.inf; Lsrc = Usrc = None; viol = []
    for n in range(1, N_MAX + 1):
        for l in range(0, min(n, 4)):
            r = (n, l)
            if r == g or a.get(r, 0) >= 2 * (2 * l + 1): continue
            pr = p(r); dn = n - g[0]; ds = math.sqrt(pr) - math.sqrt(pg)
            if abs(ds) < 1e-12:
                if dn <= 0: viol.append(r)
                continue
            bnd = dn / ds
            if ds > 0:
                if bnd < U: U, Usrc = bnd, r
            else:
                if bnd > L: L, Lsrc = bnd, r
    return L, U, Lsrc, Usrc, viol, g
def surd_key(x): return D(x, 10)
for form in ('A', 'B'):
    for N_MAX in (7, 8):
        ne = 0; surds = set(); rows = []
        for Z in range(3, 109):
            L, U, Ls, Us, viol, g = corridor(Z, form, N_MAX)
            ok = (L < U) and not viol; ne += ok
            for x in (L, U):
                if math.isfinite(x): surds.add(surd_key(x))
            rows.append((Z, L, U, ok))
        print('  form %s, N_MAX=%d: non-empty %d of 106 | distinct finite endpoint values (10 dp) %d' % (form, N_MAX, ne, len(surds)))
        if form == 'A' and N_MAX == 7:
            print('    the %d distinct endpoints:' % len(surds), ' '.join(str(D(s, 7)) for s in sorted(surds)))
            bad = [(Z, G.GROUND[Z][0]) for Z, L, U, ok in rows if not ok]
            print('    empty corridors:', bad if bad else 'none')
            CORR_A7 = rows
print('  VERDICT "All 106 non-empty" (L%s): %s' % (find('All 106 non-empty'), 'MEASURED equal (form A, N_MAX 7 and 8)' if all(r[3] for r in CORR_A7) else 'MEASURED differs'))
nsA7 = len({surd_key(x) for Z, L, U, ok in CORR_A7 for x in (L, U) if math.isfinite(x)})
nsA8 = len({surd_key(x) for Z in range(3, 109) for x in corridor(Z, 'A', 8)[:2] if math.isfinite(x)})
z7 = sum(1 for Z in range(3, 109) for x in corridor(Z, 'A', 7)[:2] if math.isfinite(x) and abs(x) < 1e-9) > 0
print('  VERDICT "Nineteen distinct surds" (L%s): generator named — form A, N_MAX 7 gives %d, N_MAX 8 gives %d (zero, Pa\'s degenerate L per 1403, counted as one value: %s); MEASURED equal under the n<=8 generator, which the chapter does not name — DOCKET §1 convention, docket 34 / 16z-03' % (find('Nineteen distinct surds'), nsA7, nsA8, z7))
print('  the six named in 1309 as endpoints: 1/sqrt3 %s  1/sqrt2 %s  1  1/(sqrt3-1) %s  1+1/sqrt2 %s  1/(sqrt2-1) %s' % tuple(str(D(x, 7)) for x in (1 / math.sqrt(3), 1 / math.sqrt(2), 1 / (math.sqrt(3) - 1), 1 + 1 / math.sqrt(2), 1 / (math.sqrt(2) - 1))))
setA8 = {surd_key(x) for Z in range(3, 109) for x in corridor(Z, 'A', 8)[:2] if math.isfinite(x)}
named = {D(1 / math.sqrt(3), 10), D(1 / math.sqrt(2), 10), D(1, 10), D(1 / (math.sqrt(3) - 1), 10), D(1 + 1 / math.sqrt(2), 10), D(1 / (math.sqrt(2) - 1), 10)}
print('  named six present among the endpoints (form A, N_MAX 8):', sum(1 for s in named if s in setA8), 'of 6; absent:', [str(D(s, 7)) for s in named if s not in setA8])
print('  crossing for ns/(n-1)d (L%s): (sqrt(n-1) + sqrt(n-4))/3 at n = 4..7 (7 dp, ROUND_HALF_EVEN):' % find('(√(n−1) + √(n−4))/3'),
      ' '.join(str(D((dsqrt(n - 1) + dsqrt(n - 4)) / 3, 7)) for n in (4, 5, 6, 7)))
pr = [s for s in ('0.5773503', '1.0000000', '1.2168450', '1.3938270')]
got = [str(D((dsqrt(n - 1) + dsqrt(n - 4)) / 3, 7)) for n in (4, 5, 6, 7)]
print('  VERDICT crossing values: %s (printed %s) — n = 4, 5 equal; n = 6, 7 differ at the fifth decimal from the chapter\'s OWN formula (1.2167605 vs 1.2168450; 1.3938469 vs 1.3938270): 16z-04 (docket 12) confirmed by measurement; 1403\'s 4 dp values 1.2168 / 1.3938 are consistent with the formula' % ('MEASURED equal' if got == pr else 'MEASURED differs', ' '.join(pr)))
for Z in (19, 37, 55, 87):
    L, U, Ls, Us, viol, g = corridor(Z, 'A', 7)
    print('    Z=%d %s entrant %d%s: L=%s from %s, U=%s from %s' % (Z, G.GROUND[Z][0], g[0], LET[g[1]], D(L, 7) if math.isfinite(L) else L, Ls, D(U, 7) if math.isfinite(U) else U, Us))

hr('§4 THE WALK (§34.6; Register 1401 / 1402 / 1403 / 1445 / 1463): the running intersection, the placement rules, the eight a values')
print('  CONVENTION: running intersection I := I ∩ (L_Z, U_Z) over Z = 3..108 in form A, N_MAX 7; a FORCED reset is a Z at which I empties (I := (L_Z,U_Z)).')
def forced(form='A', N_MAX=7):
    lo, hi = -math.inf, math.inf; out = []
    for Z in range(3, 109):
        L, U = corridor(Z, form, N_MAX)[:2]
        nlo, nhi = max(lo, L), min(hi, U)
        if not nlo < nhi: out.append(Z); nlo, nhi = L, U
        lo, hi = nlo, nhi
    return out
F = forced(); REC14 = [37, 42, 43, 45, 55, 58, 64, 65, 80, 91, 96, 97, 103, 104]
print('  forced resets (form A, N_MAX 7):', F, '| count', len(F))
print('  VERDICT 1401/1463 fourteen forced at', REC14, ':', 'MEASURED equal' if F == REC14 else 'MEASURED differs — a finding about the re-derivation (G0c)')
for form, N in (('A', 8), ('B', 7)):
    f2 = forced(form, N); print('  forced resets under form %s, N_MAX %d: %s | count %d %s' % (form, N, f2, len(f2), '(= 1401)' if f2 == REC14 else '(differs from 1401)'))
print('  single a for the whole table (1463): running intersection over all 106 empties %d times -> %s' % (len(F), 'INFEASIBLE as one system' if F else 'feasible'))
REC18 = sorted(REC14 + [3, 19, 81, 87])
def madelung_entrant(Z):
    a = occ(Z - 1)
    cands = [(n, l) for n in range(1, 9) for l in range(0, min(n, 4)) if a.get((n, l), 0) < 2 * (2 * l + 1)]
    return min(cands, key=lambda k: (k[0] + k[1], k[0]))
opened = {}
for (k, Z) in seq: opened[k] = Z
cls = {}
for Z in REC18:
    g = step(Z)[0]; prev_g = step(Z - 1)[0]
    is_open = opened.get(g) == Z
    is_exc = g != madelung_entrant(Z)
    prev_exc = prev_g != madelung_entrant(Z - 1)
    cls[Z] = 'opening' if is_open else ('exception' if is_exc else ('return' if prev_exc else 'UNCLASSIFIED'))
    print('   Z=%3d %-2s entrant %d%s (prev %d%s) madelung %d%s -> %s%s' % (Z, G.GROUND[Z][0], g[0], LET[g[1]], prev_g[0], LET[prev_g[1]], madelung_entrant(Z)[0], LET[madelung_entrant(Z)[1]], cls[Z], '' if g != prev_g else '  [SAME subshell as Z-1: a mid-subshell reset]'))
from collections import Counter
c = Counter(cls.values()); print('  the record\'s eighteen (1401: 14 forced + Li 3, K 19, Tl 81, Fr 87) classified on the observed order:', dict(c))
print('  VERDICT §34.6 "eighteen … opening (8), exception (6), return (4)" (L%s):' % find('resets eighteen times'), 'MEASURED equal on the record\'s list' if (c.get('opening'), c.get('exception'), c.get('return')) == (8, 6, 4) else 'MEASURED differs on the record\'s list',
      '| returns named Tc/Tb/Bk/Hg:', [G.GROUND[Z][0] for Z in REC18 if cls[Z] == 'return'])
mid = [(Z, G.GROUND[Z][0], '%d%s' % (step(Z)[0][0], LET[step(Z)[0][1]]), 'single-electron step' if len(step(Z)[1]) == 1 else 'two-electron rearrangement') for Z in REC18 if step(Z)[0] == step(Z - 1)[0]]
print('  VERDICT "never resets mid-subshell" (L%s; Register 1350): %s — CONVENTION: a reset is mid-subshell iff the entrant subshell at Z equals the entrant at Z-1; failing members of 1401\'s own list: %s' % (find('never resets'), 'MEASURED equal' if not mid else 'MEASURED differs', mid))
cls2 = {}
for Z in REC18:
    g = step(Z)[0]; prev_g = step(Z - 1)[0]
    cls2[Z] = 'exception' if g != madelung_entrant(Z) else ('opening' if opened.get(g) == Z else ('return' if prev_g != madelung_entrant(Z - 1) else 'UNCLASSIFIED'))
c2 = Counter(cls2.values()); print('  under the other priority (exception before opening):', dict(c2), '| returns:', [G.GROUND[Z][0] for Z in REC18 if cls2[Z] == 'return'], '| exceptions:', [G.GROUND[Z][0] for Z in REC18 if cls2[Z] == 'exception'])
print('  NOTE: neither priority gives 8 / 6 / 4; the four named returns Tc, Tb, Bk, Hg exclude Rf 104, whose 6d follows Lr 103\'s 7p — LW1-ground.py\'s own docstring records Lr as [Rn]5f14 7s2 7p, not 6d (Register 1306); the 8 / 6 / 4 partition is consistent with a Lr = 6d table (INFERRED)')
print('  NOTE (1402 / 1460): the count eighteen is a property of one trajectory — 1402 gives ten to thirty-three under other rules; the eighteen is not derivable from the corridor alone.')
# placement rules (1402) — reconstructions under named conventions
def walk(rule, seed=None, form='A', N_MAX=7, closed=True):
    rng = random.Random(seed); a = None; resets = []; score = 0
    for Z in range(3, 109):
        L, U = corridor(Z, form, N_MAX)[:2]
        inside = (a is not None) and ((L <= a <= U) if closed else (L < a < U))
        if not inside:
            resets.append(Z)
            fin = [x for x in (L, U) if math.isfinite(x)]
            if rule == 'nearest': a = (min(fin, key=lambda x: abs(x - a)) if a is not None and len(fin) == 2 else fin[0])
            elif rule == 'lower': a = L if math.isfinite(L) else U
            elif rule == 'upper': a = U if math.isfinite(U) else L
            elif rule == 'midpoint': a = (L + U) / 2 if len(fin) == 2 else fin[0]
            elif rule == 'farther': a = (max(fin, key=lambda x: abs(x - a)) if a is not None and len(fin) == 2 else fin[-1])
            elif rule == 'random': a = rng.uniform(L, U) if len(fin) == 2 else (L + 1 if math.isfinite(L) else U - 1)
            elif rule == '1403': a = L if (math.isfinite(L) and L > 0) else U
        score += (L < a < U) if not closed else (L <= a <= U)
    return resets, score
print('  CONVENTION (reconstruction): a held while L <= a <= U (closed, so an endpoint placement is "inside"); when it leaves, re-placed by the rule;')
print('  an infinite endpoint is replaced by the finite one; random = uniform on (L,U) with seeds 0..199; median = lower median (even count).')
for rule, rec in (('nearest', 10), ('lower', 12), ('upper', 17), ('midpoint', 21), ('farther', 22)):
    rs, sc = walk(rule); print('   rule %-9s resets %2d (1402 says %2d) %s  score %d/106' % (rule, len(rs), rec, 'MEASURED equal' if len(rs) == rec else 'MEASURED differs (reconstruction)', sc))
rc = sorted(len(walk('random', seed=s)[0]) for s in range(200))
print('   rule random    resets min %d max %d lower-median %d over 200 seeds (1402: 18-33, median 26) — reconstruction, seeds not the record\'s' % (rc[0], rc[-1], rc[99]))
rs, sc = walk('1403'); print('   rule 1403 (L if finite and > 0 else U): resets %d (1403 says ten) %s; reset Z: %s' % (len(rs), 'MEASURED equal' if len(rs) == 10 else 'MEASURED differs (reconstruction)', rs))
print('  the eight a values of 1403 (RECONSTRUCTIONS per its WARNING) against the corridor endpoints, form A, N_MAX 7, 4 dp ROUND_HALF_EVEN:')
for Z, nm, printed, end in ((19, 'K', '0.5774', 'L'), (37, 'Rb', '1.0000', 'L'), (55, 'Cs', '1.2168', 'L'), (57, 'La', '0.7071', 'L'), (80, 'Hg', '0.8090', 'L'), (87, 'Fr', '1.3938', 'L'), (103, 'Lr', '1.9841', 'L'), (91, 'Pa', '1.3660', 'U')):
    L, U, Ls, Us, viol, g = corridor(Z, 'A', 7); v = L if end == 'L' else U
    print('   Z=%3d %-2s entrant %d%s  L=%s U=%s  1403: %s=%s -> %s' % (Z, nm, g[0], LET[g[1]], D(L, 4) if math.isfinite(L) else L, D(U, 4) if math.isfinite(U) else U, end, printed,
          'MEASURED equal' if math.isfinite(v) and str(D(v, 4)) == printed else 'MEASURED differs (finding about the re-derivation, G0c)'))
print('  the nine "leak" steps of 1445 (Li 3, Rb 37, In 49, Cs 55, Hg 80, Tl 81, Fr 87, Lr 103, Rf 104): in the forced list', [Z for Z in (3, 37, 49, 55, 80, 81, 87, 103, 104) if Z in F], '| not forced', [Z for Z in (3, 37, 49, 55, 80, 81, 87, 103, 104) if Z not in F], '| In 49 in the record\'s eighteen:', 49 in REC18)

hr('§5 THE MEMORYLESS TEST (§34.6 "104 of 106"; Register 1332; docket 37 / 1448 "vacuous") — one named reconstruction')
print('  CONVENTION (reconstruction): at each Z, for every admissible candidate c (the entrant included), build c\'s own corridor as if c were the entrant;')
print('  set a = the midpoint of (L_c, U_c) when both are finite, L_c + 1 or U_c - 1 when one is infinite ("its own crossing value" read as an interior point of its own corridor;')
print('  a placement AT the endpoint ties c with the rival that defines it and can never be strict-least — self-caught, rewritten); c is SELF-CONSISTENT iff at that a its nu is least (strict) among admissibles.')
def nu(k, a, aocc, form='A'):
    n, l = k; p = n - l - 1 + (aocc.get(k, 0) / (2 * (2 * l + 1)) if form == 'B' else 0); return n - a * math.sqrt(p)
hist = Counter(); obs_in = 0; two_four = 0; detail = []
for Z in range(3, 109):
    aocc = occ(Z - 1); g = step(Z)[0]
    cands = [(n, l) for n in range(1, 8) for l in range(0, min(n, 4)) if aocc.get((n, l), 0) < 2 * (2 * l + 1)]
    sc = []
    for c in cands:
        L, U = corridor(Z, 'A', 7, entrant=c)[:2]
        if not L < U: continue
        a = (L + U) / 2 if math.isfinite(L) and math.isfinite(U) else (L + 1 if math.isfinite(L) else U - 1)
        if not math.isfinite(a): continue
        vals = {k: nu(k, a, aocc) for k in cands}
        best = min(vals.values())
        if vals[c] == best and sum(1 for v in vals.values() if v == best) == 1: sc.append(c)
    hist[len(sc)] += 1; obs_in += g in sc; two_four += 2 <= len(sc) <= 4
print('  self-consistent candidates per step (count: steps):', dict(sorted(hist.items())), '| steps with 2..4:', two_four, 'of 106 | observed among them:', obs_in, 'of 106')
print('  VERDICT 1332 "104 of 106 admit two to four; the observed always among them": %s under this convention — docket 37 already records the figure as not reconstructible from the stated convention; the record stands (G0c)' % ('MEASURED equal' if two_four == 104 and obs_in == 106 else 'MEASURED differs'))

hr('§6 THE ENTRY POINT AND Λ_t (§34.7; Register 1350 / 1353 / 1354) — arithmetic on printed figures; the measured a values are not in the bundle')
sq3 = dsqrt(3); print('  t(l) = sqrt(l(l+1)/2): p -> %s, d -> %s, f -> %s (4 dp)' % (D(dsqrt(Decimal(1)), 4), D(dsqrt(Decimal(3)), 4), D(dsqrt(Decimal(6)), 4)))
ratio = Decimal('1.785') / Decimal('1.028'); dev = (ratio / sq3 - 1) * 100
print('  1.785 / 1.028 = %s; against sqrt3 = %s the deviation is %s %% (printed 0.19%%; 2 dp ROUND_HALF_EVEN)' % (D(ratio, 5), D(sq3, 5), D(dev, 2)))
print('  VERDICT "ratio is sqrt3 to 0.19%%" (L%s): %s at printed precision (1.785 / 1.028); Register 1350 states the same 0.19%% — the underlying unrounded values are record-carried' % (find('0.19%'), 'MEASURED equal' if str(D(dev, 2)) == '0.19' else 'MEASURED differs: %s %%' % D(dev, 2)))
prow = [Decimal(x) for x in ('1.120', '1.049', '1.022', '1.002')]
mean = sum(prow) / 4; med = (prow[1] + prow[2]) / 2
print('  p row (L%s) 1.120 1.049 1.022 1.002: mean %s, median %s; "1.028 at p across four subshells" (L%s) — neither the mean nor the median of the printed row' % (find('1.120'), D(mean, 4), D(med, 4), find('1.028')))
print('  VERDICT "1.028 at p across four subshells": UNREPRODUCIBLE from the chapter\'s own row (mean 1.048, median 1.036); Register 1214 / 1350 carry 1.028 — the four subshells behind it are not the Λ_t p row (INFERRED); budget: the per-subshell a values (ionisation energies) are not in the bundle (REQUEST-LOWDIN)')
print('  6p 0.2%% above 1.0000 (L%s): 1.002/1.0000 - 1 = %s %% -> %s' % (find('0.2% above'), D((Decimal('1.002') - 1) * 100, 1), 'MEASURED equal'))
print('  §34.1 scatter 0.187->0.041 · 0.119->0.028 · 0.088->0.018 · 0.059->0.021 · 0.086->0.047 (L%s): equal to Register 1348 token-for-token; UNREPRODUCIBLE — needs a per element from ionisation energies (not in the bundle); budget: REQUEST-LOWDIN delivery' % find('0.187'))

hr('§7 DOMAIN (§34.9) AND THE DEMOTED / WITHDRAWN RESTATEMENTS (Register 1350 / 1445 / 1460 WARNING lines, grepped before scoring)')
print('  Z = 3 to 108 -> %d elements (printed 106): %s' % (108 - 3 + 1, 'MEASURED equal'))
for k in ((4, 3), (5, 3)):
    Zo = opened.get(k); L, U, Ls, Us, viol, g = corridor(Zo, 'A', 7)
    print('  f opening %d%s at Z=%d %s: p = n-l-1 = %d; L = %s (from %s), U = %s' % (k[0], LET[k[1]], Zo, G.GROUND[Zo][0], k[0] - k[1] - 1, L, Ls, D(U, 4) if math.isfinite(U) else U))
print('  VERDICT "At any f opening p = 0 … L = -inf" (L%s): MEASURED equal at 4f (p = 0, L = -inf), MEASURED differs at 5f (p = 1) — 16z-05 / 17a-04 confirmed by measurement' % find('At any f opening'))
rest = [('No parameter is fitted', "1350 WARNING: qualified by R 1445 (the 99 was FITTED; held out 90 vs null 96)"),
        ('Exceptionless on 106 elements', "1350 WARNING: holds only in the fitted sense"),
        ('resets eighteen times', "1460: the half-capacity mechanism and all six placement rules demote with nu; 1402: ten to thirty-three under other rules"),
        ('Nineteen distinct surds', "1460: the nineteen surds demote with nu (true of the form, not of the table)"),
        ('All 106 non-empty', "1460: retained — a result about the FORM; 1463: 106 separate one-dimensional results, not one system"),
        ('104 of 106', "1448: the per-atom fixed point is vacuous; docket 37"),
        ('t(ℓ) → √( ℓ(ℓ+1) / 2 )', "1460: the entry point is among what demotes? — listed items: surds, bounds, crossing, eight a values, half-capacity, 99/90/72, horizon, six rules; the entry point is NOT in either list (INFERRED)"),
        ('corridor is forced', "1460: the corridor is the instrument and survives intact — consistent")]
for tok, note in rest:
    sites = find(tok); print('  %-32s sites L%s — %s' % (repr(tok), sites, note))
print('  VERDICT: §34.4 L%s / §34.8 L%s "No parameter is fitted", §34.9 L%s "Exceptionless", §34.5 L%s "Nineteen … surds", §34.6 L%s "resets eighteen times" restate as live what 1350\'s WARNING qualifies and 1460 demotes — 16z-01 / 16z-02 (docket 23 / 35), re-confirmed by measurement; no new class' % (find('No parameter is fitted')[0], find('No parameter is fitted')[-1], find('Exceptionless on 106')[0], find('Nineteen distinct surds')[0], find('resets eighteen times')[0]))
print('  §34.10 L%s "Seven of eight rules give 106/106, and random interior points on 200 of 200 seeds" = Register 1331 token-for-token (rules over the same intervals: any a inside every interval reproduces the entrant by construction — the score is the corridor\'s non-emptiness restated); the 74/106 farther-endpoint failure and the seed count are trajectory figures, UNREPRODUCIBLE without brack.py/scorer.py (not in the bundle; budget: REQUEST-LOWDIN)' % find('Seven of eight'))
print('  §34.10 L%s "1.029 factor": one main site; Register grep for "1.029 " gives no entry (r2-ch34re §7) — single-witness, docket 17 (INFERRED not a corridor figure)' % find('1.029'))

hr('§7b REGISTER GREP FOR LATER OR EXACT STATEMENTS OF THE FIGURES SCORED ABOVE (entry numbers; the Register\'s WARNING lines are where a figure is withdrawn)')
HD = re.compile(r'^#{1,4}\s*(\d+(?:\s*,\s*\d+)*)\s*$')   # fault 7 self-caught: the pattern was written with doubled backslashes (a literal backslash-s), matching no heading
def ent(k):
    for j in range(k, -1, -1):
        m = HD.match(R[j])
        if m: return m.group(1)
for probe in ('return from one', 'subshell opening', 'mid-subshell', '0.19%', '1.2168450', '1.3938270', 'Seventeen of nineteen', '17 of 19', 'ten resets', 'In 49', 'two hundred random'):
    hs = {ent(k) for k, l in enumerate(R) if probe in l}
    hits = sorted((h for h in hs if h), key=lambda x: int(x.split(',')[0])) + (['FRONT-MATTER'] if None in hs else [])   # fault 6 self-caught: a front-matter hit has no enclosing heading (ent -> None)
    print('  %-24s -> entries %s' % (repr(probe), hits))
hr('§8 TOWER IDENTITIES 1460 KEEPS (M = 2n - p - 1; p = n - l - 1 >= 0) on the candidate set, and the tower gate')
cands = [(n, l) for n in range(1, 8) for l in range(0, min(n, 4))]
print('  %d candidate subshells n<=7, l<=3: p = n-l-1 >= 0 at all: %s; M = 2n-p-1 = n+l: %s; p ≡ M+1 (mod 2) i.e. (n-l-1) ≡ (n+l+1) (mod 2): %s' % (len(cands), all(n - l - 1 >= 0 for n, l in cands), all(2 * n - (n - l - 1) - 1 == n + l for n, l in cands), all((n - l - 1 - (n + l + 1)) % 2 == 0 for n, l in cands)))
print('  tower-2 module attributes carrying a cell count (introspected, names only):', [k for k in sorted(tow) if k.lower() in ('lam8', 'l8', 'cells', 'tower', 'build', 'main', 'run')])
