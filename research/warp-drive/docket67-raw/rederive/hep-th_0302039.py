"""DOCKET 67 audit, hep-th/0302039 (Popov 2003) as used by hpscentre.py:118-155.

What this can and cannot check (Popov's own text was NOT reachable this run):
  A. Parse HPS gr-qc/9701064v1 eqs (5)-(7) INDEPENDENTLY from the cached alphaXiv
     text layer d67/src/hps/_flat0.txt and compare with the tree's transcription
     (hpscentre.build 'hps').  Confirms the HPS side of M1, M2, M3 at source.
  B. Einstein tensor of ds^2 = -f dt^2 + dl^2 + r^2 dOmega^2 from own Christoffels;
     conservation law nabla_mu T^mu_l derived here, not imported.
  C. Solve conservation for the two disputed coefficients as UNKNOWNS
     (a_tt, a_th) at ll power 2 and at the printed power 1.
  D. Trace of the non-log part vs the conformal-scalar anomaly
     (1/2880 pi^2)[C^2 + (R_ab R^ab - R^2/3) + box R], computed from the metric.
  E. Tree's Popov transcription (hpscentre.build 'popov') vs the independently
     parsed HPS: which differences the TREE's Popov text implies.  This checks the
     tree's internal consistency only; Popov's printing itself is NAMED-NOT-READ.
"""
import sys, re, importlib.util, os
sys.dont_write_bytecode = True
import sympy as sp

D67 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = os.path.join(D67, 'src', 'hps', '_flat0.txt')
TREE = '/home/user/Claude-Method-Works/research/warp-drive/hpscentre.py'

l = sp.Symbol('l', real=True)
fF, rF = sp.Function('f')(l), sp.Function('r')(l)
F = [sp.diff(fF, l, k) for k in range(5)]
R = [sp.diff(rF, l, k) for k in range(5)]
a_tt, a_th, p = sp.symbols('a_tt a_th p')
results = []
def chk(name, ok):
    results.append((name, bool(ok))); print(('PASS ' if ok else 'FAIL ') + name)

# ---------------------------------------------------------------- A. parse HPS
t = open(TXT, encoding='utf-8').read()
def bracket(start_marker, from_pos):
    i = t.index(start_marker, from_pos) + len(start_marker)
    j = t.index(')]', i)
    body = t[i:j]
    k = body.index('ln f (')
    nonlog = body[:k].rstrip()
    assert nonlog.endswith('+')            # the '+' that joins '+ ln f (' is not a term
    return nonlog[:-1], body[k + len('ln f ('):], j

def parse(s):
    s = s.replace('−', '-')
    toks = s.split()
    terms, cur = [], None
    def flush():
        if cur is not None: terms.append(cur[:2])
    i = 0
    while i < len(toks):
        tk = toks[i]
        m = re.fullmatch(r'([+-]?)(\d*)', tk)
        if m and tk not in ('',) and (m.group(1) or m.group(2)):
            # a sign and/or coefficient starts a new term (a bare number after a
            # symbol is a denominator power and is consumed below, never here).
            # A bare number right after a lone sign token is that term's coefficient.
            sign = -1 if m.group(1) == '-' else 1
            coef = int(m.group(2)) if m.group(2) else 1
            if not m.group(1) and cur is not None and len(cur) == 3:   # pending lone sign
                cur = [cur[0] * coef, sp.Integer(1)]
            elif m.group(1) and not m.group(2):                       # lone sign token
                flush(); cur = [sign, sp.Integer(1), 'sign']
            else:
                flush(); cur = [sign * coef, sp.Integer(1)]
            i += 1; continue
        if tk in ('f', 'r'):
            if cur is None: cur = [1, sp.Integer(1)]
            if len(cur) == 3: cur = cur[:2]
            base = F if tk == 'f' else R
            nxt = toks[i + 1] if i + 1 < len(toks) else ''
            pm = re.fullmatch(r"(′+)(\d*)", nxt)
            if pm:                                   # numerator: derivative^power
                order = len(pm.group(1)); pw = int(pm.group(2)) if pm.group(2) else 1
                cur[1] *= base[order] ** pw; i += 2; continue
            dm = re.fullmatch(r'\d+', nxt)
            if dm:                                   # denominator with power
                cur[1] /= base[0] ** int(nxt); i += 2; continue
            cur[1] /= base[0]; i += 1; continue      # denominator power 1
        if tk in ('+',):
            flush(); cur = [1, sp.Integer(1), 'sign']; i += 1; continue
        if tk in ('-',):
            flush(); cur = [-1, sp.Integer(1), 'sign']; i += 1; continue
        raise ValueError('unparsed token %r in %r' % (tk, s[:80]))
    flush()
    return sum(c * e for c, e in terms), len(terms)

p5 = t.index('the tt component')
n5, l5, e5 = bracket('K 2 [', p5)
n6, l6, e6 = bracket('K 2 [', e5)
n7, l7, e7 = bracket('K 2 [', e6)
H = {}
for key, s in (('tt_n', n5), ('tt_l', l5), ('ll_n', n6), ('ll_l', l6), ('th_n', n7), ('th_l', l7)):
    H[key], nt = parse(s)
    print('  parsed %s: %d terms' % (key, nt))
chk('HPS text layer: K^2 = 1/(5760 pi) printed', 'K 2  =  1 5760' in t)
chk('8 pi/(46080 pi^2) == 1/(5760 pi)  (tree mapping, hpscentre.py:139)',
    sp.simplify(8*sp.pi/(46080*sp.pi**2) - 1/(5760*sp.pi)) == 0)

f, f1, f2, f3, f4 = F; r, r1, r2, r3, r4 = R
# the three slots as printed, read off the parsed source
coef = lambda expr, mono: sp.Poly(sp.expand(expr * f**4 * r**4), *F[1:], *R[1:]).as_expr().coeff(sp.expand(mono * f**4 * r**4)) if False else None
def term_coeff(expr, mono):
    e = sp.expand(expr)
    return sp.simplify(sum(a for a in e.as_ordered_terms() if sp.simplify(a / mono).free_symbols <= set() and not sp.simplify(a/mono).has(fF, rF)) / mono) if True else None
c_tt = term_coeff(H['tt_l'], f1**2*f2/f**3)
c_ll_r1 = term_coeff(H['ll_l'], f1**2*r1**2/(f**2*r))
c_ll_r2 = term_coeff(H['ll_l'], f1**2*r1**2/(f**2*r**2))
c_th = term_coeff(H['th_l'], f1**4/f**4)
print('  source slots: tt ln f f\'^2f\'\'/f^3 = %s; ll ln f f\'^2r\'^2/(f^2 r) = %s, /(f^2 r^2) = %s; thth ln f f\'^4/f^4 = %s'
      % (c_tt, c_ll_r1, c_ll_r2, c_th))
chk('M1 HPS side READ at source: tt ln-f coefficient printed 16', c_tt == 16)
chk('M2 HPS side READ at source: ll ln-f term printed -4 f\'^2 r\'^2/(f^2 r), no /(f^2 r^2)', c_ll_r1 == -4 and c_ll_r2 == 0)
chk('M3 HPS side READ at source: thth ln-f carries +21 f\'^4/f^4', c_th == 21)

# compare with the tree's transcription
spec = importlib.util.spec_from_file_location('hpscentre_ro', TREE)
hc = importlib.util.module_from_spec(spec); spec.loader.exec_module(hc)
S = hc.build(sp)
sub_tree = {S['F'][k]: F[k] for k in range(5)}
sub_tree.update({S['R'][k]: R[k] for k in range(5)})
def tree_expr(e, reading):
    e = e.subs({S['a_tt']: reading[0], S['a_th']: reading[1], S['ll_pow']: reading[2]})
    return e.subs(sub_tree, simultaneous=True) if False else e.xreplace({S['l']: l})
(tt_n, tt_l), (ll_n, ll_l), (th_n, th_l) = S['hps']
pairs = [('tt_n', tt_n), ('tt_l', tt_l), ('ll_n', ll_n), ('ll_l', ll_l), ('th_n', th_n), ('th_l', th_l)]
for key, te in pairs:
    te2 = tree_expr(te, (16, 21, 1))
    chk('tree transcription == independent parse of HPS text layer: %s' % key,
        sp.simplify(sp.expand(te2 - H[key])) == 0)

# ---------------------------------------------------------------- B. geometry
t_, th, ph = sp.symbols('t theta phi')
X = [t_, l, th, ph]
g = sp.diag(-fF, 1, rF**2, rF**2*sp.sin(th)**2); gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                         for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Riem(a, b, c, d):
    return (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
            + sum(Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c] for e in range(4)))
Rm = [[[[sp.simplify(Riem(a, b, c, d)) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Ric = sp.Matrix(4, 4, lambda b, d: sp.simplify(sum(Rm[a][b][a][d] for a in range(4))))
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gmix = sp.simplify(gi*Ric - Rs/2*sp.eye(4))
G_tt, G_ll, G_th = Gmix[0, 0], Gmix[1, 1], Gmix[2, 2]
chk('G^t_t = 2r\'\'/r + r\'^2/r^2 - 1/r^2 (HPS (5) LHS)', sp.simplify(G_tt - (2*r2/r + r1**2/r**2 - 1/r**2)) == 0)
chk('G^l_l = f\'r\'/(fr) + r\'^2/r^2 - 1/r^2 (HPS (6) LHS)', sp.simplify(G_ll - (f1*r1/(f*r) + r1**2/r**2 - 1/r**2)) == 0)
chk('G^th_th = f\'\'/2f + r\'\'/r + f\'r\'/2fr - f\'^2/4f^2 (HPS (7) LHS)',
    sp.simplify(G_th - (f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))) == 0)

def div_l(Ttt, Tll, Tth):
    """nabla_mu T^mu_l for T = diag(Ttt, Tll, Tth, Tth) mixed, from own Christoffels."""
    T = sp.diag(Ttt, Tll, Tth, Tth)
    nu = 1
    e = sp.diff(T[1, 1], l)
    e += sum(Gam[m][m][a]*T[a, nu] for m in range(4) for a in range(4))
    e -= sum(Gam[a][m][nu]*T[m, a] for m in range(4) for a in range(4))
    return sp.simplify(sp.expand(e))
chk('Bianchi: div G = 0 (own conservation law)', div_l(G_tt, G_ll, G_th) == 0)

# ---------------------------------------------------------------- C. conservation
Lf = sp.log(fF)
def Tsys(att, ath, pw):
    tl = H['tt_l'] + (att - 16)*f1**2*f2/f**3
    ll = H['ll_l'] + 4*f1**2*r1**2/(f**2*r) - 4*f1**2*r1**2/(f**2*r**pw)
    hl = H['th_l'] + (ath - 21)*f1**4/f**4
    return (H['tt_n'] + Lf*tl, H['ll_n'] + Lf*ll, H['th_n'] + Lf*hl)
def solve_slots(pw):
    res = sp.expand(div_l(*Tsys(a_tt, a_th, pw)) * f**6 * r**6)
    res = sp.expand(res.subs(Lf, sp.Symbol('LOG')))
    gens = [sp.Symbol('LOG')] + F[1:] + R[1:] + [fF, rF]
    eqs = sp.Poly(res, *gens).coeffs()
    return sp.solve(eqs, [a_tt, a_th], dict=True)
sol2 = solve_slots(2); sol1 = solve_slots(1)
print('  conserving (a_tt, a_th) at ll power 2:', sol2)
print('  conserving (a_tt, a_th) at ll power 1 (as printed):', sol1)
chk('conservation with slots as UNKNOWNS, ll power 2: unique (116, 21)', sol2 == [{a_tt: 116, a_th: 21}])
chk('conservation at printed ll power 1: no conserving pair', sol1 == [])
for att in (16, 116):
    for ath in (0, 21):
        ok = div_l(*Tsys(att, ath, 2)) == 0
        chk('  reading (%d, %d): conserved=%s, expected %s' % (att, ath, ok, (att, ath) == (116, 21)),
            ok == ((att, ath) == (116, 21)))

# ---------------------------------------------------------------- D. trace
Tc = Tsys(116, 21, 2)
logtrace = sp.simplify(sp.expand((Tc[0] + Tc[1] + 2*Tc[2]).coeff(Lf)))
chk('conserved reading: ln f part is TRACELESS', logtrace == 0)
Tp = Tsys(16, 21, 1)
chk('printed reading: ln f part is NOT traceless', sp.simplify(sp.expand((Tp[0] + Tp[1] + 2*Tp[2]).coeff(Lf))) != 0)
nonlog_trace = sp.simplify(H['tt_n'] + H['ll_n'] + 2*H['th_n'])     # 8 pi T / K^2
Ricmix = sp.simplify(gi*Ric)
RicSq = sp.simplify(sum(Ricmix[a, b]*Ricmix[b, a] for a in range(4) for b in range(4)))
Kret = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if Rm[a][b][c][d] != 0:
                    # R^a_bcd R_a^bcd = R^a_bcd g_ae g^bf g^cg g^dh R^e_fgh (diagonal metric)
                    Kret += Rm[a][b][c][d]**2 * g[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
Kret = sp.simplify(Kret)
Csq = sp.simplify(Kret - 2*RicSq + Rs**2/3)
sqrtg = sp.sqrt(fF)*rF**2
boxR = sp.simplify(sp.diff(sqrtg*sp.diff(Rs, l), l)/sqrtg)
anomaly = 16*(Csq + (RicSq - Rs**2/3) + boxR)   # 8 pi T / K^2 predicted, K^2 = 1/(5760 pi)
chk('non-log trace: 8 pi T^a_a = 16 K^2 [C^2 + (R_ab R^ab - R^2/3) + box R] (conformal anomaly, 1/2880 pi^2)',
    sp.simplify(sp.expand(nonlog_trace - anomaly)) == 0)
chk('prefactor: 16 K^2/(8 pi) == 1/(2880 pi^2)', sp.simplify(16/(5760*sp.pi)/(8*sp.pi) - 1/(2880*sp.pi**2)) == 0)

# ---------------------------------------------------------------- E. tree's Popov
(pn1, pl1), (pn2, pl2), (pn3, pl3) = S['popov']
P = [(pn1, pl1), (pn2, pl2), (pn3, pl3)]
Hn = [H['tt_n'], H['ll_n'], H['th_n']]
Hc = [Tc[0].coeff(Lf), Tc[1].coeff(Lf), Tc[2].coeff(Lf)]
for k, name in enumerate(('B1/tt', 'B2/ll', 'B3/thth')):
    pn = P[k][0].xreplace({S['l']: l}); pl = P[k][1].xreplace({S['l']: l})
    chk('tree-Popov %s non-log == parsed HPS non-log' % name, sp.simplify(sp.expand(pn - Hn[k])) == 0)
    dl = sp.simplify(sp.expand(-pl - Hc[k]))
    print('  tree-Popov %s log (sign-flipped) minus CONSERVED reading: %s' % (name, dl))
    results.append(('E-%s' % name, None)); globals()['dE%d' % k] = dl
chk('tree-Popov B1 log == conserved (116) tt log', dE0 == 0)
chk('tree-Popov B2 log == conserved (r^2) ll log', dE1 == 0)
chk('tree-Popov B3 log == conserved thth log minus 21 f\'^4/f^4 (M3 as the tree states)',
    sp.simplify(dE2 + 21*f1**4/f**4) == 0)

n_fail = sum(1 for n, ok in results if ok is False)
print('\n%d checks, %d FAIL' % (sum(1 for n, ok in results if ok is not None), n_fail))
sys.exit(1 if n_fail else 0)
