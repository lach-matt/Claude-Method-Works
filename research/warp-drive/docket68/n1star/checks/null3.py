#!/usr/bin/env python3
"""null3.py -- CERTIFY-10L5-RESULT.md round 3, F5: the null structure of the reduced (2+1)-dimensional system in
double-null gauge with one-dimensional sections, and the hierarchy it gives for the difference of two solutions.
Labels: deduced, every identity exact (sympy; rational functions of the jets after exp(w), exp(c) are named).

The metric (reduce5.py R2-R4: the Einstein frame of the class, or any (2+1)-metric in double-null gauge):
    h = -2 Omega^2 (du dv + dv du) + gamma (dx - b du)^2,   Omega = e^w,  gamma = e^{2c},
frame e4 = Omega^-1 d_v, e3 = Omega^-1 (d_u + b d_x), ex = gamma^-1/2 d_x, and [Wu26] (2.1)'s Ricci coefficients
(READ, p. 4), with sections of dimension one: chi = h(D_x e4, ex), chib = h(D_x e3, ex), eta = -h(D_3 ex, e4)/2,
etab = -h(D_4 ex, e3)/2, omega = -h(D_4 e3, e4)/4, omegab = -h(D_3 e4, e3)/4, zeta = h(D_x e4, e3)/2.

  N0 (exact) the frame is null/orthonormal; the coefficients are
         chi = e^-w c_v,  chib = e^-w (c_u + b c_x + b_x),  omega = e^-w w_v/2 ... (printed);  b_x enters chib only.
  N1 (exact) Raychaudhuri, both directions:  e4 chi + chi^2 + 2 omega chi = -Ric_44,  e3 chib + chib^2 + 2 omegab chib
     = -Ric_33  ([Wu26] (2.2) with |chi|^2 = chi^2).
  N2 (exact) torsion:  e4 eta = -chi (eta - etab) - Ric_x4,  e3 etab = -chib (etab - eta) - Ric_x3  ([Wu26] (2.5), with
     the dimension-three identity R_{x434} = 2 Ric_x4).
  N3 (exact) the lapse:  e4 omegab and e3 omega are quadratic in (chi, chib, eta, etab, omega, omegab) plus a fixed
     combination of Ric_34 and Ric_xx (coefficients solved for and then checked; the 4D Gauss term -K/2 of [Wu26] (2.5)
     has no analogue on a one-dimensional section).
  N4 (exact) commutators: [e4, ex], [e3, ex], [e3, e4] are combinations of the frame with Ricci coefficients as
     coefficients (solved for and checked).
  N5 (exact) the wave operator in the frame ([Wu26] (2.17) in dimension three, solved for and checked).
  N6 (exact) divergences: div e4 = chi - 2 omega, div e3 = chib - 2 omegab, div ex = eta + etab (as solved).
  N7 (exact) the two equations the hierarchy does NOT use, e4 chib and e3 chi, contain ex(etab) and ex(eta): an ansatz
     without that angular derivative has no solution, one with it does.  The angular loss lives only there.
  N8 (deduced from N0-N6) THE HIERARCHY HAS NO ANGULAR LOSS.  Each Ricci coefficient has a transport equation whose
     right side is a polynomial in the Ricci coefficients and the Ricci frame components (= sum e_a Phi e_b Phi on the
     reduced system), with no frame derivative of any Ricci coefficient: chi, eta, omegab along e4; chib, etab, omega
     along e3.  The metric follows from them by d_v c = e^w chi, d_v w = -2 e^w omega, d_v b = -2 e^{2w - c}(eta -
     etab) (N0).  The scalars obey two Bianchi-type pairs (N9).  The shift's x-derivative is inside chib, which N1
     transports along e3 without it: round 2's Y5 loss is the metric formulation's, not the class's.
  N9 (exact) the energy identities of the two pairs, for any f, a = e4 f, c = ex f, d = e3 f:
         Div(a^2 e3 + c^2 e4 - 2 a c ex) = -2 a Box f + Q1(a, c, d),
         Div(c^2 e3 + d^2 e4 - 2 c d ex) = -2 d Box f + Q2(a, c, d),
     Q1, Q2 quadratic forms whose coefficients are Ricci coefficients (printed).  Fluxes: a^2 on outgoing cones and c^2
     on ingoing ones (pair 1); c^2 on outgoing, d^2 on ingoing (pair 2).
  N10 (exact) the difference of two metrics, linearised: with the frame-component differences
         A1 = d(e4 Phi), C1 = d(ex Phi), D1 = d(e3 Phi)  (d = d/d eps at eps = 0 of the family background + eps pert),
     the linearised pair operators  d[e3 e4 Phi - ex ex Phi] - e3(A1) + ex(C1),  d[e4 ex Phi - ex e4 Phi] - e4(C1) +
     ex(A1),  d[e3 ex Phi - ex e3 Phi] - e3(C1) + ex(D1)  and the transport operators d[e4 chi] - e4(d chi) etc.
     contain NO derivative of the metric differences (dw, dc, db) and none of dPhi: only undifferentiated metric
     differences times background second derivatives.  Control: with the coordinate difference e^-c d(Phi_x) in place
     of C1, dc_x appears (the loss of an angular derivative that the frame differences avoid).

  Controls (each must fail): (k1) N1 with omega chi in place of 2 omega chi; (k2) N2 with eta in place of eta - etab;
  (k3) N7's ansatz without the angular derivative (no solution); (k4) N10's coordinate difference.

  python3 checks/null3.py
"""
import sys, time, itertools
import sympy as sp

u, v, x = sp.symbols('u v x', real=True)
X3 = [u, v, x]
FN = ('w', 'c', 'b', 'f')
Fd = {k: sp.Function(k)(u, v, x) for k in FN}
w, c, b, f = [Fd[k] for k in FN]
Ew, Ec = sp.symbols('Ew Ec', positive=True)
SYM = {}


def jets(e, fields=None):
    fields = fields or Fd
    e = e.doit()
    sub = {}
    for d in e.atoms(sp.Derivative):
        k = str(d.expr.func)
        combo = ''.join(sorted([str(vv) for vv, n in d.variable_count for _ in range(n)], key='uvx'.index))
        sub[d] = sp.Symbol(k + '_' + combo)
    e = e.xreplace(sub).xreplace({F: sp.Symbol(k) for k, F in fields.items()})
    ws, cs = sp.Symbol('w'), sp.Symbol('c')

    def ex(arg):
        arg = sp.expand(arg)
        p, q = arg.coeff(ws), arg.coeff(cs)
        rest = sp.expand(arg - p * ws - q * cs)
        return Ew ** p * Ec ** q * sp.exp(rest)
    return e.replace(sp.exp, ex)


def num(e):
    return sp.expand(sp.numer(sp.together(sp.expand(e))))


def zero(e):
    return num(jets(e)) == 0


def metric():
    g = sp.zeros(3)
    Om2, ga = sp.exp(2 * w), sp.exp(2 * c)
    g[0, 1] = g[1, 0] = -2 * Om2; g[2, 2] = ga; g[0, 2] = g[2, 0] = -ga * b; g[0, 0] = ga * b ** 2
    return g


def christoffel(g):
    gi = g.inv()
    G = [[[sp.S(0)] * 3 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for i in range(3):
            for j in range(i, 3):
                s = sum(gi[a, d] * (sp.diff(g[d, j], X3[i]) + sp.diff(g[d, i], X3[j]) - sp.diff(g[i, j], X3[d]))
                        for d in range(3))
                G[a][i][j] = G[a][j][i] = sp.together(s / 2)
    return G


def ricci(g, G):
    R = sp.zeros(3)
    for i in range(3):
        for j in range(i, 3):
            s = 0
            for a in range(3):
                s += sp.diff(G[a][i][j], X3[a]) - sp.diff(G[a][i][a], X3[j])
                for e in range(3):
                    s += G[a][a][e] * G[e][i][j] - G[a][j][e] * G[e][i][a]
            R[i, j] = R[j, i] = s
    return R


def main():
    t0 = time.time(); ok = True
    g = metric(); G = christoffel(g)
    E4 = sp.Matrix([0, sp.exp(-w), 0]); E3 = sp.Matrix([sp.exp(-w), 0, sp.exp(-w) * b])
    EX = sp.Matrix([0, 0, sp.exp(-c)])
    ip = lambda X, Y: (X.T * g * Y)[0]
    D = lambda X, Y: sp.Matrix([sum(X[n] * sp.diff(Y[m], X3[n]) for n in range(3))
                                + sum(G[m][n][l] * X[n] * Y[l] for n in range(3) for l in range(3)) for m in range(3)])
    vec = lambda X, F_: sum(X[n] * sp.diff(F_, X3[n]) for n in range(3))
    e4, e3, ex = (lambda F_: vec(E4, F_)), (lambda F_: vec(E3, F_)), (lambda F_: vec(EX, F_))
    good = all(zero(q) for q in (ip(E4, E4), ip(E3, E3), ip(E3, E4) + 2, ip(EX, EX) - 1, ip(EX, E4), ip(EX, E3)))
    psi = {'chi': ip(D(EX, E4), EX), 'chib': ip(D(EX, E3), EX), 'eta': -ip(D(E3, EX), E4) / 2,
           'etab': -ip(D(E4, EX), E3) / 2, 'omega': -ip(D(E4, E3), E4) / 4, 'omegab': -ip(D(E3, E4), E3) / 4,
           'zeta': ip(D(EX, E4), E3) / 2}
    form = {'chi': sp.exp(-w) * sp.diff(c, v),
            'chib': sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x) + sp.diff(b, x)),
            'omega': sp.exp(-w) * sp.diff(w, v) / 2, 'omegab': sp.exp(-w) * (sp.diff(w, u) + b * sp.diff(w, x)) / 2,
            'zeta': -sp.exp(c - 2 * w) * sp.diff(b, v) / 4,
            'eta': -sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x),
            'etab': sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x)}
    res = {k: zero(psi[k] - form[k]) for k in form}
    good &= all(res.values())
    print('N0 frame null/orthonormal, and the Ricci coefficients:', 'PASS' if good else 'FAIL', res)
    print('   chi = e^-w c_v, chib = e^-w (c_u + b c_x + b_x), omega = e^-w w_v/2, omegab = e^-w (w_u + b w_x)/2,\n'
          '   zeta = -e^{c-2w} b_v/4, eta = zeta + e^-c w_x, etab = -zeta + e^-c w_x.  b_x appears in chib only.')
    ok &= good
    P = {k: psi[k] for k in psi}
    chi, chib, eta, etab, om, omb = [form[k] for k in ('chi', 'chib', 'eta', 'etab', 'omega', 'omegab')]
    print('   (%.0f s) Ricci ...' % (time.time() - t0), flush=True)
    Ric = ricci(g, G)
    fr = {'4': E4, '3': E3, 'x': EX}
    Rf = {i + j: (fr[i].T * Ric * fr[j])[0] for i in '34x' for j in '34x'}
    # N1
    n1 = zero(e4(chi) + chi ** 2 + 2 * om * chi + Rf['44'])
    n1 &= zero(e3(chib) + chib ** 2 + 2 * omb * chib + Rf['33'])
    k1 = zero(e4(chi) + chi ** 2 + om * chi + Rf['44'])
    print('N1 Raychaudhuri e4 chi + chi^2 + 2 omega chi = -Ric_44 and the e3 one:', 'PASS' if n1 else 'FAIL',
          '; control (k1) omega chi:', 'identity (bad)' if k1 else 'fails (good)')
    ok &= n1 and not k1
    n2 = zero(e4(eta) + chi * (eta - etab) + Rf['x4']) and zero(e3(etab) + chib * (etab - eta) + Rf['x3'])
    k2 = zero(e4(eta) + chi * eta + Rf['x4'])
    print('N2 e4 eta = -chi (eta - etab) - Ric_x4, e3 etab = -chib (etab - eta) - Ric_x3:', 'PASS' if n2 else 'FAIL',
          '; control (k2) eta for eta - etab:', 'identity (bad)' if k2 else 'fails (good)')
    ok &= n2 and not k2
    # N3: solve for the coefficients
    names = ['chi', 'chib', 'eta', 'etab', 'omega', 'omegab']
    quad = [(p, q) for i, p in enumerate(names) for q in names[i:]]
    cs = sp.symbols('k0:80')

    def solve_ansatz(lhs, terms, extra, tag):
        """lhs = sum k_i term_i + extra-terms; solve the k_i (linear) from the jets; return dict or None"""
        expr = lhs - sum(k * t for k, t in zip(cs, terms))
        e = num(jets(expr))
        jsyms = sorted(e.free_symbols - set(cs), key=str)
        eqs = sp.Poly(e, *jsyms).coeffs()
        sol = sp.solve(eqs, cs[:len(terms)], dict=True)
        return sol[0] if sol else None
    terms = [form[p] * form[q] for p, q in quad] + [Rf['34'], Rf['xx']]
    labels = ['%s*%s' % pq for pq in quad] + ['Ric_34', 'Ric_xx']
    out = {}
    for tag, lhs in (('e4 omegab', e4(omb)), ('e3 omega', e3(om))):
        sol = solve_ansatz(lhs, terms, None, tag)
        if sol is None:
            print('N3 %s: no solution (FAIL)' % tag); ok = False; continue
        full = {labels[i]: sol.get(cs[i], 0) for i in range(len(terms))}
        free = [cs[i] for i in range(len(terms)) if cs[i] not in sol]
        full = {k_: (vv.subs({fr_: 0 for fr_ in free}) if hasattr(vv, 'subs') else vv) for k_, vv in full.items()}
        nz = {k_: vv for k_, vv in full.items() if vv != 0}
        chk = zero(lhs - sum(full[labels[i]] * terms[i] for i in range(len(terms))))
        out[tag] = nz
        print('N3 %s =' % tag, ' + '.join('(%s) %s' % (vv, k_) for k_, vv in nz.items()), '->',
              'PASS' if chk else 'FAIL', '(free coefficients: %d)' % len(free))
        ok &= chk
    # N4 commutators on f
    fa, fc, fd = e4(f), ex(f), e3(f)
    basis = [form[p] * q for p in names for q in (fa, fc, fd)]
    blab = ['%s %s' % (p, q) for p in names for q in ('e4f', 'exf', 'e3f')]
    for tag, lhs in (('[e4, ex] f', e4(ex(f)) - ex(e4(f))), ('[e3, ex] f', e3(ex(f)) - ex(e3(f))),
                     ('[e3, e4] f', e3(e4(f)) - e4(e3(f)))):
        sol = solve_ansatz(lhs, basis, None, tag)
        if sol is None:
            print('N4 %s: no solution (FAIL)' % tag); ok = False; continue
        free = [cs[i] for i in range(len(basis)) if cs[i] not in sol]
        coef = [sp.sympify(sol.get(cs[i], 0)).subs({fr_: 0 for fr_ in free}) for i in range(len(basis))]
        chk = zero(lhs - sum(k * t for k, t in zip(coef, basis)))
        print('N4 %s =' % tag, ' + '.join('(%s) %s' % (k, l) for k, l in zip(coef, blab) if k != 0), '->',
              'PASS' if chk else 'FAIL'); ok &= chk
    # N5 the wave operator
    gi = g.inv(); sq = 2 * sp.exp(2 * w + c)
    good = zero(sq ** 2 + g.det())
    boxf = sum(sp.diff(sq * gi[i, j] * sp.diff(f, X3[j]), X3[i]) for i in range(3) for j in range(3)) / sq
    basis5 = [form[p] * q for p in names for q in (fa, fc, fd)]
    lhs = -boxf - e3(e4(f)) + ex(ex(f))
    sol = solve_ansatz(lhs, basis5, None, 'N5')
    free = [cs[i] for i in range(len(basis5)) if cs[i] not in sol] if sol else []
    coef5 = [sp.sympify(sol.get(cs[i], 0)).subs({fr_: 0 for fr_ in free}) for i in range(len(basis5))] if sol else []
    chk = sol is not None and zero(lhs - sum(k * t for k, t in zip(coef5, basis5)))
    print('N5 -Box f = e3 e4 f - ex ex f +', ' + '.join('(%s) %s' % (k, l) for k, l in zip(coef5, blab) if k != 0),
          '->', 'PASS' if (chk and good) else 'FAIL'); ok &= chk and good
    # N6 divergences
    div = lambda X: sum(sp.diff(sq * X[n], X3[n]) for n in range(3)) / sq
    n6 = zero(div(E4) - (chi - 2 * om)) and zero(div(E3) - (chib - 2 * omb)) and zero(div(EX) - (eta + etab))
    print('N6 div e4 = chi - 2 omega, div e3 = chib - 2 omegab, div ex = eta + etab:', 'PASS' if n6 else 'FAIL')
    ok &= n6
    # N7 the unused equations carry the angular derivative
    for tag, lhs, dterm in (('e4 chib', e4(chib), ex(etab)), ('e3 chi', e3(chi), ex(eta))):
        sol_no = solve_ansatz(lhs, terms, None, tag)
        sol_yes = solve_ansatz(lhs, terms + [dterm], None, tag)
        good = sol_no is None and sol_yes is not None
        kd = sol_yes.get(cs[len(terms)]) if sol_yes else None
        print('N7 %s: ansatz without ex(eta%s) solvable: %s (k3: must be False); with it: %s, coefficient %s ->' % (
            tag, 'b' if 'chib' in tag else '', sol_no is not None, sol_yes is not None, kd),
            'PASS' if good else 'FAIL')
        ok &= good
    # N9 energy identities of the pairs
    a_, c_, d_ = fa, fc, fd
    J1 = a_ ** 2 * E3 + c_ ** 2 * E4 - 2 * a_ * c_ * EX
    J2 = c_ ** 2 * E3 + d_ ** 2 * E4 - 2 * c_ * d_ * EX
    qb = [form[p] * q1 * q2 for p in names for q1, q2 in ((fa, fa), (fa, fc), (fa, fd), (fc, fc), (fc, fd), (fd, fd))]
    qlab = ['%s %s' % (p, q) for p in names for q in ('aa', 'ac', 'ad', 'cc', 'cd', 'dd')]
    for tag, J, mult in (('pair 1 (a, c)', J1, a_), ('pair 2 (c, d)', J2, d_)):
        lhs = div(J) + 2 * mult * boxf
        sol = solve_ansatz(lhs, qb, None, tag)
        free = [cs[i] for i in range(len(qb)) if cs[i] not in sol] if sol else []
        coef = [sp.sympify(sol.get(cs[i], 0)).subs({fr_: 0 for fr_ in free}) for i in range(len(qb))] if sol else []
        chk = sol is not None and zero(lhs - sum(k * t for k, t in zip(coef, qb)))
        print('N9 %s: Div J + 2 %s Box f =' % (tag, 'a' if mult is a_ else 'd'),
              ' + '.join('(%s) %s' % (k, l) for k, l in zip(coef, qlab) if k != 0), '->', 'PASS' if chk else 'FAIL')
        ok &= chk
    print('N8 (deduced) the transport equations N1-N3 used by the hierarchy have no frame derivative of a Ricci '
          'coefficient on the right (by the solved forms above); b_x lives in chib only (N0).')
    print('   (%.0f s) N10 ...' % (time.time() - t0), flush=True)
    ok &= n10()
    print('null3 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


def n10():
    """the linearised frame-difference operators contain no derivative of the metric differences"""
    eps = sp.Symbol('eps')
    nm = ['w0', 'c0', 'b0', 'F0', 'w1', 'c1', 'b1', 'F1']
    Fl = {k: sp.Function(k)(u, v, x) for k in nm}
    w0, c0, b0, F0, w1, c1, b1, F1 = [Fl[k] for k in nm]
    W_, C_, B_, Ph = w0 + eps * w1, c0 + eps * c1, b0 + eps * b1, F0 + eps * F1
    E4 = lambda F_, ww=W_: sp.exp(-ww) * sp.diff(F_, v)
    E3 = lambda F_, ww=W_, bb=B_: sp.exp(-ww) * (sp.diff(F_, u) + bb * sp.diff(F_, x))
    EX = lambda F_, cc=C_: sp.exp(-cc) * sp.diff(F_, x)
    d0 = lambda e: sp.diff(e, eps).subs(eps, 0)
    A1, C1, D1 = d0(E4(Ph)), d0(EX(Ph)), d0(E3(Ph))
    b4 = lambda F_: E4(F_, w0); b3 = lambda F_: E3(F_, w0, b0); bx = lambda F_: EX(F_, c0)
    bad = {'w1_' + s_ for s_ in ('u', 'v', 'x')} | {'c1_' + s_ for s_ in ('u', 'v', 'x')} | \
          {'b1_' + s_ for s_ in ('u', 'v', 'x')} | {'F1', 'F1_u', 'F1_v', 'F1_x'}

    def syms(e):
        e = e.doit()
        sub = {}
        for dd in e.atoms(sp.Derivative):
            k = str(dd.expr.func)
            combo = ''.join(sorted([str(vv) for vv, n in dd.variable_count for _ in range(n)], key='uvx'.index))
            sub[dd] = sp.Symbol(k + '_' + combo)
        e = sp.expand(e.xreplace(sub))
        return {str(q) for q in e.free_symbols} | {str(q.func) + '' for q in e.atoms(sp.Function)}
    ops = {'pair 1a  d[e3 e4 F - ex ex F] - e3(A1) + ex(C1)': d0(E3(E4(Ph)) - EX(EX(Ph))) - b3(A1) + bx(C1),
           'pair 1b  d[e4 ex F - ex e4 F] - e4(C1) + ex(A1)': d0(E4(EX(Ph)) - EX(E4(Ph))) - b4(C1) + bx(A1),
           'pair 2   d[e3 ex F - ex e3 F] - e3(C1) + ex(D1)': d0(E3(EX(Ph)) - EX(E3(Ph))) - b3(C1) + bx(D1)}
    chi_ = lambda cc, ww: sp.exp(-ww) * sp.diff(cc, v)
    ops['transport d[e4 chi] - e4(d chi)'] = d0(E4(chi_(C_, W_))) - b4(d0(chi_(C_, W_)))
    ok = True
    for tag, op in ops.items():
        s_ = syms(op)
        two = ('uu', 'uv', 'ux', 'vv', 'vx', 'xx')
        hit = sorted(q for q in s_ if q in bad or any(q.startswith(p) and q[len(p):] in two
                                                     for p in ('w1_', 'c1_', 'b1_', 'F1_')))
        print('N10 %s: derivatives of the differences present: %s ->' % (tag, hit or 'none'),
              'PASS' if not hit else 'FAIL')
        ok &= not hit
    # control k4: coordinate difference in place of C1
    Cc = sp.exp(-c0) * sp.diff(F1, x)
    op = d0(E3(E4(Ph)) - EX(EX(Ph))) - b3(A1) + bx(Cc)
    s_ = syms(op)
    hit = sorted(q for q in s_ if q.startswith('c1_'))
    print('   control (k4) coordinate difference e^-c0 F1_x in place of C1: derivatives of dc present: %s ->' % hit,
          'fails (good)' if hit else 'passes (bad)')
    ok &= bool(hit)
    return ok


if __name__ == '__main__':
    sys.exit(main())
