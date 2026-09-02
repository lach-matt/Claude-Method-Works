#!/usr/bin/env python3
# r2-24a.py — chat 147 (Cowork) — 24a-05 (DEF-143 item 11's third re-derivation; DEF-137 item 9, DEF-138 item 11; docket 37 / 38 / 34):
# Appendix E's E(Q) chain — the thirteen-state *E(Q) = 0 in all four domain fibres and 1 unfibred* (E.1.2 L10961–L10962, E.1.5, E.4.1,
# Register 256 / 1729 / 235), the eleven-state *the unfibred figure is 4* (E.1.3, Register 372) with *Eleven items: one nonexistent, two
# buildable, eight retrievable* (E.1.4, Register 382), E.1.4's *grows the ambient box from 18 cells to 24 and takes E from 4 to 10*, Register
# 465's *4 to 3* on entering R as nothing · buildable · unbounded, and E.1.5's fourteen-state (fibred 0; R as nothing: the mathematical fibre
# admits exactly one cell). The set is rebuilt from E.1.2's table; the closed items' coordinates, which Appendix E does not print (DEF-138),
# are taken from the sites in the volume that DO print them (§12.11.0.5, §12.11.0.6, §29.2.1, Register 371 / 1353) and the remainder is
# ENUMERATED under a stated budget. Closed under the book's OWN operator — r2lib.Rset, §6.1 L1540: φ̂ᵢⱼ(v) = max{xᵢ : xⱼ ≤ v} (a running
# maximum), ambient ∏ Âᵢ(X) — imported by path, never copied. Rivals named and scored beside it: chat 137's equality bound (r2-ch24a.py §4's
# E_R: φ(v) = max{xᵢ : xⱼ = v}), the naive box defect |box| − |X|, the box complement |box| − |ℛ(X)|, and the code's constraint
# *buildable ⟹ cost ≤ days* applied to ℛ(X). Reads MEMBERS by name (never a bundle path). Deterministic: no wall clock, no randomness.
# A re-derivation that disagrees with the record is a finding about the re-derivation (G0c); the record stands until the original
# instrument (Register 256's code, not a member — docket 38) is found. Every convention is named before a figure is scored.
import os, re, sys, hashlib, importlib.util, itertools
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
def load(name):
    s = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
r2lib = load('r2lib')
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
def md5(n): return hashlib.md5(open(os.path.join(H, n), 'rb').read()).hexdigest()[:8]
MAIN = 'The_Method_1_6-2.md'; REG = 'The_Method_1_6___The_Register-2.md'
MC = 'The_Method_1_6___Mathematical_Compendium-2.md'; PC = 'The_Method_1_6___The_Physics_Compendium-2.md'
IOI = 'The_Method_1_6___The_Index_of_Indices-2.md'; SC = 'The_Method_1_6___Spectra_Compendium-2.md'
VOLS = {'main': MAIN, 'reg': REG, 'mc': MC, 'pc': PC, 'ioi': IOI, 'sc': SC}
M = rd(MAIN); R = rd(REG); TXT = {k: rd(v) for k, v in VOLS.items()}
def hr(t): print('\n' + '=' * 100 + '\n' + t + '\n' + '=' * 100)

def rbody(n):   # copied verbatim from r2-23a.py (there from r2-21a.py … r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())

def body_range(M, sec):   # copied verbatim from r2-23a.py (there from r2-21a.py … r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = r2lib.heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)

def lettered(M, tag):   # copied verbatim from r2-23a.py (there from r2-21a.py … r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits

def bounded(f): return re.compile(r'(?<![\d.,])' + re.escape(f) + r'(?![\d])')   # chat-145 convention: digit-bounded on both sides
def sites(f, vol='main'): return [i for i, l in enumerate(TXT[vol], 1) if bounded(f).search(l)]

hr('§0 members and the units (lettered E.x headings, body = LAST hit; a `### E.x` unit ends at the next heading of any rank; E.4 has no heading line)')
for k, v in VOLS.items(): print('   %-4s %-52s md5 %s  %d lines' % (k, v, md5(v), len(TXT[k])))
def lrange(tag):
    h = lettered(M, tag); s = h[-1]
    e = next(i for i in range(s + 1, len(M) + 1) if re.match(r'^#{1,4} ', M[i - 1]))
    return (s, e)
UNITS = {t: lrange(t) for t in ('E.1', 'E.1.1', 'E.1.2', 'E.1.3', 'E.1.4', 'E.1.5', 'E.2', 'E.3', 'E.4.1', 'E.4.2')}
for t, (s, e) in UNITS.items(): print('   %-6s hits %s  body L%d–L%d (%d lines)  %s' % (t, lettered(M, t), s, e - 1, e - s, M[s - 1].strip()[:72]))
print('   `## Appendix E` hits', lettered(M, 'Appendix E'), '(contents line and body; body = LAST); `### E.4` hits', lettered(M, 'E.4'),
      '; unmarked heading text *E.4 The grid* at', [i for i, l in enumerate(M, 1) if l.startswith('E.4 The grid')], '(24b-02; it bounds E.3)')
E4 = [i for i, l in enumerate(M, 1) if l.startswith('E.4 The grid')][0]; UNITS['E.4'] = (E4, UNITS['E.4.1'][0]); UNITS['E.3'] = (UNITS['E.3'][0], E4)
print('   E.3 re-bounded L%d–L%d; E.4 (unmarked) L%d–L%d' % (UNITS['E.3'][0], UNITS['E.3'][1] - 1, E4, UNITS['E.4'][1] - 1))
print('   heading_line (numeric resolver) on "E.1.4":', r2lib.heading_line(M, 'E.1.4'), '— the numeric resolver does not see a lettered heading; `lettered` governs (chat-129 convention)')
# the numeric sections that print the closed items' coordinates: measured under both resolvers
NUMSEC = {'12.11.0.5': None, '12.11.0.6': None, '29.2.1': None, '32.1.4': None, '32.1.4.1': None, '32.6.1': None}   # 32.1.4.1 / 32.6.1 = r2lib.enclosing of the E(Q) table L9011 / readout L9270 (fault 1: a guessed §32.1.5 / §32.3, corrected by measurement)
for sec in NUMSEC:
    br = body_range(M, sec); sp = r2lib.section_span(M, sec); NUMSEC[sec] = (br, sp)
    print('   §%-9s body_range L%d–L%d  section_span %s  %s' % (sec, br[0], br[1] - 1, sp, M[br[0] - 1].strip()[:70]))

hr('§1 the Register: every entry the family cites — heading, WARNING lines, body; the family figures grepped in six volumes (later statements)')
def ent(n):
    i = next((i for i, l in enumerate(R, 1) if l.strip() == '### %d' % n), None)
    grouped = [i for i, l in enumerate(R, 1) if re.match(r'^### ', l) and re.search(r'(?<![\d])%d(?![\d])' % n, l)]
    if i is None: return (n, None, grouped, [])
    e = next((j for j in range(i + 1, len(R) + 1) if re.match(r'^#{1,4} ', R[j - 1])), len(R) + 1)
    warn = [j for j in range(i, e) if 'WARNING' in R[j - 1]]
    return (n, i, grouped, warn)
CITED = (211, 212, 235, 238, 239, 256, 307, 332, 364, 371, 372, 382, 384, 385, 386, 387, 396, 461, 465, 562, 563, 564, 1729)
for n in CITED:
    q, i, g, w = ent(n)
    if i is None: print('   %5d NO `### %d` heading; grouped heading line(s) %s :: %s' % (n, n, g, (R[g[0] - 1].strip() if g else '—')))
    else: print('   %5d heading L%d WARNING lines %s :: %s' % (n, i, w, (rbody(n) or '')[:140]))
# the entry that closes item O carries no number in E's text: locate it by its body
o_ent = [i for i, l in enumerate(R, 1) if l.startswith('**Q ITEM O CLOSED**')]
o_head = [max(j for j in range(1, i) if re.match(r'^### ', R[j - 1])) for i in o_ent]
print('   *Q ITEM O CLOSED* at Register L%s under heading %s' % (o_ent, [R[j - 1].strip() for j in o_head]))
print('   family figures in six volumes (digit-bounded / token probes):')
for tok in ('E(Q)', 'unfibred', 'from 4 to', '4 to 3', '18 cells', 'one nonexistent', 'eight retrievable', 'no route', 'E(Q) = 5', 'E(Q) = 2 fibred'):
    hits = {k: [i for i, l in enumerate(TXT[k], 1) if tok in l] for k in VOLS}
    print('   %-18s' % repr(tok), {k: (len(v), v[:12]) for k, v in hits.items() if v})
print('   Register lines stating an E(Q) value:')
for i, l in enumerate(R, 1):
    if re.search(r'E\(Q\)\s*=|unfibred E\(Q\)|E\(Q\) unmoved', l): print('     L%d %s' % (i, re.sub(r'\*', '', l)[:150]))

hr('§2 census: every numeral printed in E.1–E.1.5, E.4 (the grid), E.4.1, E.4.2 (member line numbers)')
NUM = re.compile(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?![\w])')
for t in ('E.1', 'E.1.1', 'E.1.2', 'E.1.3', 'E.1.4', 'E.1.5', 'E.4', 'E.4.1', 'E.4.2'):
    s, e = UNITS[t]; cnt = 0; lines = 0
    for i in range(s, e):
        ns = NUM.findall(M[i - 1])
        if ns: cnt += len(ns); lines += 1; print('   L%d %s' % (i, ' '.join(ns)))
    print('   %s: %d numerals on %d lines' % (t, cnt, lines))

hr('§3 the set rebuilt: E.1.2\'s table (2-space grammar, DATA rows printed), the grid, and the closed items\' coordinates as the VOLUME prints them')
BL = ['nothing', 'novelty', 'one claim', 'a result']; OB = ['retrievable', 'buildable', 'nonexistent']; CO = ['hours', 'days', 'unbounded']
DOMS = ['physical', 'bibliographic', 'mathematical', 'computational']
print('   value orders as E.1.5 L%d–L%d prints them: blocks %s; obstacle %s; cost %s (indices 0, 1, 2, …)' % (UNITS['E.1.5'][0] + 3, UNITS['E.1.5'][0] + 4, BL, OB, CO))
s, e = UNITS['E.1.2']; Q = {}; rows = []
for i in range(s, e):
    l = M[i - 1]
    if re.match(r'^\s{2}[A-R]\s{2,}', l):
        f = re.split(r'\s{2,}', l.strip()); rows.append((i, f))
        item = f[0]; dom = f[-1]
        if 'CLOSED' in l: Q[item] = dict(closed=True, domain=dom, line=i, q=f[1])
        else: Q[item] = dict(closed=False, domain=dom, line=i, q=f[1], blocks=f[2], obstacle=f[3], cost=f[4])
for i, f in rows: print('   L%d %s | %s | %s' % (i, f[0], 'CLOSED' if Q[f[0]]['closed'] else ' · '.join(f[2:5]), Q[f[0]]['domain']))
openQ = [k for k in Q if not Q[k]['closed']]; closedQ = [k for k in Q if Q[k]['closed']]
print('   items %d; open %d %s; closed %d %s; header L%d *ten open of 14*: %s' % (len(Q), len(openQ), openQ, len(closedQ), closedQ, s, len(Q) == 14 and len(openQ) == 10))
print('   per-domain (14):', dict(Counter(Q[k]['domain'] for k in Q)), '; without R:', dict(Counter(Q[k]['domain'] for k in Q if k != 'R')), '(Register 1729: 4 / 3 / 4 / 2)')
for k in openQ: assert Q[k]['blocks'] in BL and Q[k]['obstacle'] in OB and Q[k]['cost'] in CO, (k, Q[k])
X = {k: (BL.index(Q[k]['blocks']), OB.index(Q[k]['obstacle']), CO.index(Q[k]['cost'])) for k in openQ}
# the grid (E.4, unmarked), read on the eleven
s4, e4 = UNITS['E.4']; grid = {}
for i in range(s4, e4):
    m = re.match(r'^\s{2}([A-R])\s{2,}(.+?)\s{2,}(\S.*)$', M[i - 1])
    if m: grid[m.group(1)] = (i, re.sub(r'\*', '', m.group(3)).strip())
print('   E.4 grid rows %d %s (E.4 L%d: *read when the set stood at eleven*)' % (len(grid), ''.join(sorted(grid)), s4 + 3))
for k in ('M', 'N'): print('     %s L%d first unmet requirement: %s' % (k, grid[k][0], grid[k][1]))
print('   the eleven of E.1.3 / E.1.4 / E.4 = the thirteen (A B C D F G H I K M N O P) less K and O (E.1.3 L%d *item O closed, item K closed, item M restated*)' % (UNITS['E.1.3'][0] + 5))
# the closed items' coordinates, printed OUTSIDE Appendix E (DEF-138: printed nowhere IN Appendix E — confirmed below)
print('   Appendix E lines carrying a coordinate value for K, M, N or O (E.1.2 rows print `—`):',
      [i for i in range(UNITS['E.1'][0], UNITS['E.4.2'][1]) if re.search(r'\b(K|M|N|O)\b', M[i - 1]) and re.search(r'retrievable|buildable|nonexistent|hours|days|unbounded', M[i - 1]) and not re.search(r'^\s{2}[A-R]\s{2,}', M[i - 1])])
sK = [i for i, l in enumerate(M, 1) if 'item K' in l and 'retrievable, hours' in l]
sO = [i for i, l in enumerate(M, 1) if 'item O' in l and 'buildable, days' in l] + [i for i, l in enumerate(M, 1) if l.strip().startswith('*buildable, days*')]
sN6 = [i for i, l in enumerate(M, 1) if 'B, C, F, G, K and N' in l]
rO = [i for i, l in enumerate(R, 1) if 'Q ITEM O CLOSED' in l and 'buildable, days' in l]
rM = [i for i, l in enumerate(R, 1) if 'ITEM M IS WITHDRAWN' in l and 'unbounded' in l and 'days' in l]
print('   K  *retrievable, hours* at main L%s (§12.11.0.6; heading L%d); blocks: novelty → nothing at §29.2.1 L%s (Register 238)' % (sK, NUMSEC['12.11.0.6'][0][0], sN6))
print('   O  *buildable, days* at main L%s (§12.11.0.5; heading L%d) and Register L%s; blocks NOT printed' % (sO, NUMSEC['12.11.0.5'][0][0], rO))
print('   M  cost *unbounded* rather than *days* at Register L%s (371; the eleven-state has M restated); blocks and obstacle NOT printed; the grid: %s' % (rM, grid['M'][1]))
print('   N  blocks: novelty → nothing at §29.2.1 L%s; obstacle and cost NOT printed; the grid: %s' % (sN6, grid['N'][1]))
print('   §29.2.1 L%d–L%d: *six of the eleven items in Q had novelty as their only stake — B, C, F, G, K and N … their blocks coordinate falls to nothing* — an eleven-item count at Register 238 (before N, O, P were entered at 256: a different eleven; recorded, not scored)' % (sN6[0] - 1, sN6[0] + 4))
print('   per-item obstacle over the open rows now: %s; blocks: %s' % (dict(Counter(Q[k]['obstacle'] for k in openQ)), dict(Counter(Q[k]['blocks'] for k in openQ))))

hr('§4 conventions named before scoring')
print('   E(X) = |ℛ(X)| − |X| per fibre (X the DISTINCT cells the fibre\'s items occupy), summed over fibres; unfibred = one fibre.')
print('   BOOK   = r2lib.Rset (§6.1 L1540): φ̂ᵢⱼ(v) = max{xᵢ : x ∈ X, xⱼ ≤ v}, a running maximum, ambient ∏ Âᵢ(X) (the occupied value sets) — the volume\'s own operator, imported by path.')
print('   EQ     = chat 137\'s reconstruction (r2-ch24a.py §4 E_R): φ(v) = max{xᵢ : xⱼ = v}, no running maximum, same ambient — the operator 24a-05 was measured under.')
print('   NAIVE  = |box| − |X| (the box defect); COMPL = |box| − |ℛ_BOOK(X)| (the cells the box has that the closure lacks) — the two readings of E.1.4\'s *18 cells … E from 4 to 10*.')
print('   +C     = the code\'s constraint *obstacle = buildable ⟹ cost ≤ days* (E.1.5 L%d): cells violating it removed from ℛ(X) (never from X) — as +D3 in r2-23a.py.' % (UNITS['E.1.5'][0] + 8))
print('   The fourth obstacle value *no route* is offered as index 3 (above nonexistent) and as index −1 (below retrievable); under BOOK an unoccupied value is not in the ambient — E cannot move; scored under COMPL and NAIVE.')
def E_eq(cells):   # chat 137's operator, re-stated here as the named rival (a reconstruction; not the book's)
    X = sorted(set(cells)); d = 3
    vals = [sorted({x[i] for x in X}) for i in range(d)]
    phi = {(i, j): {v: max(x[i] for x in X if x[j] == v) for v in vals[j]} for i in range(d) for j in range(d) if i != j}
    box = set(itertools.product(*vals))
    return {x for x in box if all(x[i] <= phi[(i, j)][x[j]] for i in range(d) for j in range(d) if i != j)}
def viol(c): return c[1] == 1 and c[2] > 1
def closure(cells, conv='BOOK', C=False):
    X = set(cells); cl = r2lib.Rset(list(X)) if conv == 'BOOK' else E_eq(X)
    if C: cl = {c for c in cl if c in X or not viol(c)}
    return cl
def E(cells, **kw): return len(closure(cells, **kw)) - len(set(cells))
def box_of(cells, extra_obstacle=()):
    vals = [sorted({c[i] for c in cells}) for i in range(3)]; vals[1] = sorted(set(vals[1]) | set(extra_obstacle)); return set(itertools.product(*vals))
def fibred(S, dom, **kw):
    return {d: E([S[k] for k in S if dom[k] == d], **kw) for d in DOMS if any(dom[k] == d for k in S)}
DOM = {k: Q[k]['domain'] for k in Q}
def nm(c): return '%s · %s · %s' % (BL[c[0]], OB[c[1]], CO[c[2]])

hr('§5 the ten open rows as printed (the only fully printed state): E under every convention; the press readouts compared')
S10 = dict(X)
for conv in ('BOOK', 'EQ'):
    for C in (False, True):
        f = fibred(S10, DOM, conv=conv, C=C); print('   %-4s%-3s unfibred %d ; fibred %s = %d' % (conv, '+C' if C else '', E(S10.values(), conv=conv, C=C), f, sum(f.values())))
print('   distinct cells %d of 10; box %d; NAIVE %d; COMPL %d' % (len(set(S10.values())), len(box_of(S10.values())), len(box_of(S10.values())) - len(set(S10.values())), len(box_of(S10.values())) - len(closure(S10.values()))))
print('   admitted and absent under BOOK, unfibred:', sorted(nm(c) for c in closure(S10.values()) - set(S10.values())))
print('   printed comparators: E.1.5 L%d *At fourteen, fibred and unconstrained, E(Q) = 0* (fibred, with K M N O carried — §7); §32.6.1 L%s *E(Q) = 5 unfibred* / Register 396 *E(Q) = 5* (a press readout at ten open items, state unprinted); §32.1.4 L%s table *Appendix E (Q), unfibred 4 1 one*; §32.1.4.1 L%s *E(Q), unfibred 1 1 4* (sections by r2lib.enclosing)' % (
      UNITS['E.1.5'][0] + 15, [i for i, l in enumerate(M, 1) if 'E(Q) = 5 unfibred' in l], [i for i, l in enumerate(M, 1) if 'Appendix E (Q), unfibred' in l], [i for i, l in enumerate(M, 1) if l.strip().startswith('E(Q), unfibred')]))

hr('§6 the eleven-state (A B C D F G H I M N P) — M and N enumerated under the budget; every printed figure scored per assignment')
print('   fixed: A–I, P as E.1.2 prints them; M cost = unbounded (Register 371); N blocks = nothing (§29.2.1). Free: M blocks (4) × M obstacle (3) × N obstacle (3) × N cost (3) = %d assignments.' % (4 * 3 * 3 * 3))
print('   printed figures to reproduce: fibred 0 (E.1.3 L%d *held at … eleven*); unfibred 4 (E.1.3 L%d; Register 372); obstacle 1 / 2 / 8 (E.1.4 L%d; Register 382); box 18 (E.1.4 L%d) → 24 with *no route*, E 4 → 10; +R (nothing · buildable · unbounded) unfibred 4 → 3 unconstrained (Register 465; E.1.5 L%d)' % (
      UNITS['E.1.3'][0] + 14, UNITS['E.1.3'][0] + 5, UNITS['E.1.4'][0] + 3, UNITS['E.1.4'][0] + 13, UNITS['E.1.5'][0] + 19))
S11base = {k: X[k] for k in openQ if k != 'R'}; DOM11 = dict(DOM)
R465 = (0, 1, 2)
hits11 = []; tally = Counter(); t410 = defaultdict(list)
for mb, mo, no, nc in itertools.product(range(4), range(3), range(3), range(3)):
    S = dict(S11base); S['M'] = (mb, mo, 2); S['N'] = (0, no, nc)
    obs = Counter(c[1] for c in S.values()); o_ok = (obs[2], obs[1], obs[0]) == (1, 2, 8)
    f = fibred(S, DOM11); f_ok = sum(f.values()) == 0
    u = E(S.values()); u_ok = u == 4
    bx = len(box_of(S.values())); bx24 = len(box_of(S.values(), extra_obstacle=(3,))); b_ok = bx == 18 and bx24 == 24
    cl = closure(S.values()); compl18 = bx - len(cl); compl24 = bx24 - len(cl); naive18 = bx - len(set(S.values())); naive24 = bx24 - len(set(S.values()))
    S12 = dict(S); S12['R'] = R465; u12 = E(S12.values()); r_ok = u12 == 3
    key = (o_ok, f_ok, u_ok, b_ok, r_ok); tally[key] += 1
    if (compl18, compl24) == (4, 10): t410['COMPL'].append((o_ok, f_ok, u_ok, r_ok, nm((mb, mo, 2)), nm((0, no, nc))))
    if (naive18, naive24) == (4, 10): t410['NAIVE'].append((o_ok, f_ok, u_ok, r_ok, nm((mb, mo, 2)), nm((0, no, nc))))
    if all(key): hits11.append((mb, mo, no, nc, u, compl18, compl24, naive18, naive24, len(cl), len(set(S.values())), u12, E(S.values(), conv='EQ'), E(S12.values(), conv='EQ')))
print('   tally over 108 assignments of (obstacle 1/2/8, fibred 0, unfibred 4, box 18→24, +R → 3):', {''.join('1' if b else '0' for b in k): v for k, v in sorted(tally.items(), reverse=True)})
print('   assignments reproducing ALL of them: %d' % len(hits11))
print('   assignments on which E.1.4\'s 4 → 10 reproduces under COMPL (|box| − |ℛ(X)| = 4 at 18, 10 at 24): %d %s' % (len(t410['COMPL']), t410['COMPL'][:6]))
print('   … under NAIVE (|box| − |X|): %d %s (flags: obstacle 1/2/8, fibred 0, unfibred 4, +R 3)' % (len(t410['NAIVE']), t410['NAIVE'][:6]))
for h in hits11:
    mb, mo, no, nc, u, c18, c24, n18, n24, ncl, ndist, u12, ueq, u12eq = h
    print('     M = %-40s N = %-40s unfibred BOOK %d (EQ %d) | |ℛ| %d distinct %d | COMPL 18→24: %d → %d | NAIVE %d → %d | +R465 BOOK %d (EQ %d)' % (nm((mb, mo, 2)), nm((0, no, nc)), u, ueq, ncl, ndist, c18, c24, n18, n24, u12, u12eq))
if hits11:
    print('   E.1.4\'s *E from 4 to 10* under the fourth obstacle value: BOOK cannot admit an unoccupied value (ambient ∏ Âᵢ(X)) — E stays 4 in every assignment; COMPL (|box| − |ℛ(X)|) gives %s; NAIVE gives %s' % (
          sorted({(h[5], h[6]) for h in hits11}), sorted({(h[7], h[8]) for h in hits11})))
    # DECL: the running maximum of §6.1 evaluated on a DECLARED ambient that carries the offered value (a reconstruction, named; measured, not asserted)
    def E_decl(cells, amb):
        X = sorted(set(cells)); d = 3; cl = set()
        for y in itertools.product(*amb):
            ok = True
            for i in range(d):
                for j in range(d):
                    if i == j: continue
                    below = [x[i] for x in X if x[j] <= y[j]]
                    if not below or y[i] > max(below): ok = False; break
                if not ok: break
            if ok: cl.add(y)
        return len(cl) - len(X)
    for h in hits11[:1]:
        S = dict(S11base); S['M'] = (h[0], h[1], 2); S['N'] = (0, h[2], h[3]); cells = list(S.values())
        amb0 = [sorted({c[i] for c in cells}) for i in range(3)]
        top = [amb0[0], amb0[1] + [3], amb0[2]]; bot = [amb0[0], [-1] + amb0[1], amb0[2]]
        print('   DECL on the reproducing assignment: occupied ambient E = %d (= BOOK %d); *no route* offered at the top E = %d; at the bottom E = %d — the running maximum never admits a cell at an unoccupied value (E.1.4 / Register 382: *six admitted combinations*)' % (E_decl(cells, amb0), E(cells), E_decl(cells, top), E_decl(cells, bot)))
    print('   the *no route* value at the bottom of the order (index −1) changes no BOOK figure either (an unoccupied value is outside the ambient); COMPL / NAIVE depend only on |box|, not on the position — same figures.')
    for h in hits11[:1]:
        S = dict(S11base); S['M'] = (h[0], h[1], 2); S['N'] = (0, h[2], h[3])
        print('   first assignment — admitted and absent under BOOK, unfibred (%d):' % E(S.values()), sorted(nm(c) for c in closure(S.values()) - set(S.values())))
        S12 = dict(S); S12['R'] = R465
        print('   … with R as 465 entered it (%s): admitted and absent (%d):' % (nm(R465), E(S12.values())), sorted(nm(c) for c in closure(S12.values()) - set(S12.values())), '— R occupies %s, one of the four' % nm(R465))
# the same enumeration under EQ, for the record: which assignments would chat 137's operator have needed
hits11eq = 0
for mb, mo, no, nc in itertools.product(range(4), range(3), range(3), range(3)):
    S = dict(S11base); S['M'] = (mb, mo, 2); S['N'] = (0, no, nc); S12 = dict(S); S12['R'] = R465
    obs = Counter(c[1] for c in S.values())
    if (obs[2], obs[1], obs[0]) == (1, 2, 8) and sum(fibred(S, DOM11, conv='EQ').values()) == 0 and E(S.values(), conv='EQ') == 4 and E(S12.values(), conv='EQ') == 3: hits11eq += 1
print('   under EQ (chat 137\'s operator) the assignments reproducing obstacle 1/2/8, fibred 0, unfibred 4 and +R → 3: %d of 108' % hits11eq)

hr('§7 the thirteen-state (A B C D F G H I K M N O P; Register 256 / 1729 / 235; E.1.2 L%d–L%d; E.4.1) and the fourteen-state (E.1.5; Register 1729) — K, O as printed; M, N under the budget' % (UNITS['E.1.2'][0] + 21, UNITS['E.1.2'][0] + 22))
print('   fixed: K = nothing · retrievable · hours (§12.11.0.6 + §29.2.1); O = ? · buildable · days (§12.11.0.5; blocks free, 4); M cost days (before 371) or unbounded (after; both scored); N blocks nothing.')
print('   free: O blocks (4) × M blocks (4) × M obstacle (3) × M cost (2) × N obstacle (3) × N cost (3) = %d assignments; each scored on: thirteen fibred 0 and unfibred 1 (BOOK, and BOOK+C — the code carried the constraint);' % (4 * 4 * 3 * 2 * 3 * 3))
print('   fourteen (+R one claim · buildable · unbounded) fibred 0 unconstrained (E.1.5 L%d); fourteen with R as nothing: mathematical fibre admits exactly {one claim · buildable · unbounded} (E.1.5 L%d–L%d); and, when M cost = unbounded, the eleven-state figures of §6 on the same M, N.' % (UNITS['E.1.5'][0] + 15, UNITS['E.1.5'][0] + 16, UNITS['E.1.5'][0] + 18))
R14 = (2, 1, 2); Rn = (0, 1, 2)
tally13 = Counter(); hits13 = []
for ob, mb, mo, mc, no, nc in itertools.product(range(4), range(4), range(3), (1, 2), range(3), range(3)):
    S = dict(S11base); S['K'] = (0, 0, 0); S['O'] = (ob, 1, 1); S['M'] = (mb, mo, mc); S['N'] = (0, no, nc)
    f = fibred(S, DOM); u = E(S.values()); uC = E(S.values(), C=True)
    t13 = sum(f.values()) == 0 and (u == 1 or uC == 1)
    S14 = dict(S); S14['R'] = R14; f14 = fibred(S14, DOM); t14 = sum(f14.values()) == 0
    S14n = dict(S); S14n['R'] = Rn; mathX = [S14n[k] for k in S14n if DOM[k] == 'mathematical']
    adm = closure(mathX) - set(mathX); tn = adm == {R14}
    # the eleven-state on the same M, N (only meaningful when M cost = unbounded, the 371 state)
    S11 = {k: v for k, v in S.items() if k not in ('K', 'O')}; S11['M'] = (mb, mo, 2)
    obs = Counter(c[1] for c in S11.values()); S12 = dict(S11); S12['R'] = Rn
    t11 = (obs[2], obs[1], obs[0]) == (1, 2, 8) and sum(fibred(S11, DOM).values()) == 0 and E(S11.values()) == 4 and E(S12.values()) == 3
    key = (t13, t14, tn, t11); tally13[key] += 1
    if all(key): hits13.append((ob, mb, mo, mc, no, nc, u, uC, sorted(nm(c) for c in closure(S.values()) - set(S.values())), sorted(nm(c) for c in closure(S.values(), C=True) - set(S.values()))))
print('   tally over %d assignments of (thirteen 0 / 1, fourteen fibred 0, R-as-nothing → exactly the one cell, eleven-state 1/2/8 · 0 · 4 · +R 3):' % sum(tally13.values()), {''.join('1' if b else '0' for b in k): v for k, v in sorted(tally13.items(), reverse=True)})
print('   assignments reproducing ALL of them: %d' % len(hits13))
for h in hits13:
    ob, mb, mo, mc, no, nc, u, uC, adm, admC = h
    print('     O = %-36s M = %-36s N = %-36s thirteen unfibred BOOK %d (+C %d): admitted and absent %s (+C %s)' % (nm((ob, 1, 1)), nm((mb, mo, mc)), nm((0, no, nc)), u, uC, adm, admC))
uniq = {(h[2], h[4], h[5]) for h in hits13}; print('   distinct (M obstacle, N obstacle, N cost) among the hits: %s — %s' % (sorted(uniq), {(OB[a], OB[b], CO[c]) for a, b, c in uniq}))
print('   M cost values among the hits: %s (days = the 256 state, unbounded = the 371 state; %s)' % (sorted({CO[h[3]] for h in hits13}, key=CO.index), 'both reproduce — the thirteen of 1729 are not sensitive to it' if len({h[3] for h in hits13}) == 2 else 'one only'))
print('   the constraint: thirteen unfibred without +C over the hits: %s; with +C: %s (E.1.5 L%d–L%d: *the thirteen still close — E(Q) = 0 fibred was never resting on it; only the unfibred count was*)' % (sorted({h[6] for h in hits13}), sorted({h[7] for h in hits13}), UNITS['E.1.5'][0] + 12, UNITS['E.1.5'][0] + 13))
# thirteen fibred and unfibred under EQ for the first hit, for the record
if hits13:
    ob, mb, mo, mc, no, nc = hits13[0][:6]; S = dict(S11base); S['K'] = (0, 0, 0); S['O'] = (ob, 1, 1); S['M'] = (mb, mo, mc); S['N'] = (0, no, nc)
    print('   first hit under EQ: thirteen fibred %s unfibred %d; under BOOK per-fibre %s' % (fibred(S, DOM, conv='EQ'), E(S.values(), conv='EQ'), fibred(S, DOM)))
    S14 = dict(S); S14['R'] = R14; print('   fourteen (R one claim) under BOOK: fibred %s unfibred %d ; +C unfibred %d' % (fibred(S14, DOM), E(S14.values()), E(S14.values(), C=True)))
    print('   the ten open rows alone (§5) are a different set from the fourteen: the closed items carry coordinates in the code and E.1.5\'s *at fourteen* counts them.')

hr('§8 what the page does not print — the budget (record-carried states; no figure scored)')
print('   Register 212 *E(Q) = 2 fibred, 1 unfibred* (the fifteen-state; items E, J, L and the pre-371 M print no coordinates); §32.2\'s seven and E.4.1\'s eight (no rows printed anywhere: E.4 L%d *read once at eight items and the reading was never printed*); the twelve-state (E, J, L closed). Register 396 / §32.6.1\'s *E(Q) = 5 unfibred* at ten open items: a press readout whose state is not printed (§5 gives the ten printed rows\' figure). Register 256\'s code is not a member (docket 38): every reproduction here is under the book\'s stated operator, not the original instrument.' % (s4 + 2))

hr('§9 census rows in range (DEFECT-CENSUS.tsv rows whose line lies in E.1–E.4.2) — chat 137 / 138 verdicts re-tested from the file')
cen = [l.split('\t') for l in rd('DEFECT-CENSUS.tsv') if l.strip()]; hdr = cen[0]; li = hdr.index('line') if 'line' in hdr else 2
lo, hi = UNITS['E.1'][0], UNITS['E.4.2'][1] - 1
inr = [r for r in cen[1:] if r[1] == 'main' and r[li].isdigit() and lo <= int(r[li]) <= hi] if len(hdr) > 3 else []
print('   header:', hdr); print('   rows in main L%d–L%d: %s' % (lo, hi, [(r[0], r[li]) for r in inr]))
prior = {}
for f in ('CENSUS-CLOSURES-ch24a.tsv', 'CENSUS-CLOSURES-ch25a.tsv'):
    for l in rd(f)[1:]:
        if l.strip(): p = l.split('\t'); prior[p[0]] = (f, p[1])
print('   prior verdicts:', {r[0]: prior.get(r[0]) for r in inr})
print('\nEND r2-24a')
