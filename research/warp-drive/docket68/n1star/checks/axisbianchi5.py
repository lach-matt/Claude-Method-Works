#!/usr/bin/env python3
"""axisbianchi5.py -- CERTIFY-10L5-RESULT.md round 4 (task 1): the curvature pairs of the axis chart, in its double-
null frame, reduced; the pair's energy inequality on the whole section, the axis included.  Labels: deduced (each
equation found by a linear fit at random jets and then verified exactly at fresh jets; the inequality deduced from
them with axis5.py X3).

The metric is axis5.py's chart, ghat = -2 Om^2 (du dv + dv du) + gg (dx - b du)^2 + Y^2 dphi^2, general (Om, gg, b, Y
functions of (u, v, x)), off shell: Ric is the metric's own.  Frame e4 = Om^-1 d_v, e3 = Om^-1 (d_u + b d_x),
e1 = gg^-1/2 d_x, e2 = Y^-1 d_phi.  Curvature: Riemann by hand from the Christoffel symbols, the Weyl tensor by
[Wu26]'s formula (READ, p. 5), beta = (1/2) W(e1, e4, e3, e4), betab = (1/2) W(e1, e3, e3, e4), rho = (1/4) W(e4, e3,
e4, e3), K = -Y^-1 e1 e1 Y, and [Wu26] (2.12)'s renormalised beta^r = beta - (1/2) Ric_41, betab^r = betab +
(1/2) Ric_31.  The reduced Ricci coefficients are axis5.py X2's (tr chi, chih, tr chib, chibh, eta, etab, omega,
omegab), and on S: div of a one-form component f is (Y sqrt gg)^-1 d_x(Y f), grad is e1.

  B1 (exact) sigma = (1/4) *W(e4, e3, e4, e3) vanishes: W(e1, e2, e3, e4) = 0; and W(e1, e2, e1, e4) = W(e1, e2, e1, e3)
     = 0 (the twist-free components).
  B2 (fit, then exact) Gauss: K = -rho + c1 R + c2 Ric_34 + c3 chih chibh + c4 tr chi tr chib (expected [Wu26] (2.8):
     1/3 ... with chih . chibh = 2 chih chibh in the reduced components).  The fitted coefficients are printed.
  B3 (fit, then exact) the pair: [Wu26] (2.13) Om e4 K + Om tr chi K = c div(Om beta^r) + (lower order), and (2.14)
     Om e3 beta^r + Om (tr chib - 2 omegab) beta^r = c' Om e1 K + (lower order), the lower order found in a library of
     products and angular derivatives of products (printed).  The pair is an energy pair iff c = c' (then
     K c div(Om beta) + beta c' Om e1 K is axis5.py X3's exact derivative).  Control: with beta in place of beta^r
     (no renormalisation) the fit leaves a residual (alpha enters).
  B4 (deduced from B3 and axis5.py X3) Lemma 8.A6, the pair inequality on the whole section: on [u0, u] x [v0, v] x S,
        int_{H_u} beta^2 dmu dv + int_{Hb_v} K^2 dmu du <= (data) + int int (2 |beta| |F_beta| + 2 |K| |F_K|
            + |tr chib - 2 omegab ...| beta^2 + |tr chi ...| K^2) Om dmu du dv,
     with F_beta, F_K the lower-order terms of B3 and the measure terms of axis5.py X3; the axis gives no boundary term.

  python3 checks/axisbianchi5.py
"""
import os, sys, time, random
import mpmath as mp
import sympy as sp
from sympy.core.function import AppliedUndef

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 40
u, v, x, ph = sp.symbols('u v x phi', real=True)
C4 = [u, v, x, ph]


def print(*a, **k):
    import builtins, textwrap
    s = (k.pop('sep', ' ')).join(str(q) for q in a)
    out = []
    for ln in s.split('\n'):
        if len(ln) <= 121:
            out.append(ln)
        else:
            ind = len(ln) - len(ln.lstrip()) + 4
            out.extend(textwrap.wrap(ln, 121, subsequent_indent=' ' * ind, break_on_hyphens=False))
    builtins.print('\n'.join(out), **k)


Om, gg, b, Y = [sp.Function(n)(u, v, x) for n in ('Om', 'gg', 'b', 'Y')]


def build():
    g = sp.zeros(4)
    g[0, 1] = g[1, 0] = -2 * Om ** 2
    g[2, 2] = gg; g[0, 2] = g[2, 0] = -gg * b; g[0, 0] = gg * b ** 2; g[3, 3] = Y ** 2
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, bb], C4[c]) + sp.diff(g[d, c], C4[bb]) - sp.diff(g[bb, c], C4[d]))
                 for d in range(4)) / 2 for c in range(4)] for bb in range(4)] for a in range(4)]
    # R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce} G^e_{db} - G^a_{de} G^e_{cb}
    Rup = {}
    def R_up(a, bb, c, d):
        key = (a, bb, c, d)
        if key not in Rup:
            Rup[key] = (sp.diff(Gam[a][d][bb], C4[c]) - sp.diff(Gam[a][c][bb], C4[d])
                        + sum(Gam[a][c][e] * Gam[e][d][bb] - Gam[a][d][e] * Gam[e][c][bb] for e in range(4)))
        return Rup[key]
    Rdn = {}
    def R_dn(a, bb, c, d):
        key = (a, bb, c, d)
        if key not in Rdn:
            Rdn[key] = sum(g[a, e] * R_up(e, bb, c, d) for e in range(4))
        return Rdn[key]
    E = {'3': [1 / Om, 0, b / Om, 0], '4': [0, 1 / Om, 0, 0], '1': [0, 0, 1 / sp.sqrt(gg), 0], '2': [0, 0, 0, 1 / Y]}
    nz = lambda V: [i for i in range(4) if V[i] != 0]
    def Rf(A, B, Cc, D):
        s_ = 0
        for a in nz(E[A]):
            for bb in nz(E[B]):
                for c in nz(E[Cc]):
                    for d in nz(E[D]):
                        s_ += R_dn(a, bb, c, d) * E[A][a] * E[B][bb] * E[Cc][c] * E[D][d]
        return s_
    # frame metric and Ricci in the frame: Ric(B, D) = sum_{A,C} eta^{AC} R(A, B, C, D)
    eta_inv = {('3', '4'): -sp.Rational(1, 2), ('4', '3'): -sp.Rational(1, 2), ('1', '1'): 1, ('2', '2'): 1}
    gf = {('3', '4'): -2, ('4', '3'): -2, ('1', '1'): 1, ('2', '2'): 1}
    def Ricf(B, D):
        return sum(val * Rf(A, B, Cc, D) for (A, Cc), val in eta_inv.items())
    Rs = sum(val * Ricf(A, Cc) for (A, Cc), val in eta_inv.items())
    gff = lambda A, B: gf.get((A, B), 0)
    def Wf(A, B, Cc, D):
        return (Rf(A, B, Cc, D) - sp.Rational(1, 2) * (Ricf(A, Cc) * gff(B, D) + gff(A, Cc) * Ricf(B, D)
                                                       - Ricf(B, Cc) * gff(A, D) - gff(B, Cc) * Ricf(A, D))
                + Rs / 6 * (gff(A, Cc) * gff(B, D) - gff(B, Cc) * gff(A, D)))
    return g, Rf, Ricf, Rs, Wf


def jet_values(exprs, rnd):
    """evaluate expressions at one random jet: every function and derivative an independent random rational"""
    atoms = set()
    for e in exprs:
        atoms |= e.atoms(sp.Derivative)
    sub = {d: sp.Rational(rnd.randint(-900, 900), rnd.randint(101, 997)) for d in atoms}
    fs = set()
    for e in exprs:
        fs |= e.atoms(AppliedUndef)
    for f in fs:
        sub[f] = sp.Rational(rnd.randint(150, 900), rnd.randint(101, 997))
    out = []
    for e in exprs:
        val = e.xreplace(sub)
        out.append(mp.mpf(sp.N(val, 45)))
    return out


def fit(lhs, lib, labels, n_extra=6, seed=1):
    """lhs = sum k_i lib_i at random jets: least squares in 40 digits, coefficients rationalised, then verified at
    fresh jets; returns (dict label -> rational, max residual at the fresh jets)"""
    rnd = random.Random(seed)
    n = len(lib)
    rows, rhs = [], []
    for _ in range(n + n_extra):
        vals = jet_values([lhs] + lib, rnd)
        rhs.append(vals[0]); rows.append(vals[1:])
    A = mp.matrix(rows); bvec = mp.matrix(rhs)
    sv = mp.svd_r(A, compute_uv=False)
    fit.cond = max(sv) / min(sv)
    sol, _ = mp.qr_solve(A, bvec)
    coef = [sp.nsimplify(float(sol[i]), rational=True, tolerance=1e-12) for i in range(n)]
    coef = [c if abs(float(c)) > 1e-10 else sp.Integer(0) for c in coef]
    rnd2 = random.Random(seed + 1000)
    worst = 0
    for _ in range(4):
        vals = jet_values([lhs] + lib, rnd2)
        res = vals[0] - sum(mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) * vv for c, vv in zip(coef, vals[1:]))
        worst = max(worst, abs(res) / max(1, max(abs(q) for q in vals)))
    return {l_: c for l_, c in zip(labels, coef) if c != 0}, worst


def main():
    t0 = time.time(); ok = True
    g, Rf, Ricf, Rs, Wf = build()
    e4 = lambda F_: sp.diff(F_, v) / Om
    e3 = lambda F_: (sp.diff(F_, u) + b * sp.diff(F_, x)) / Om
    e1 = lambda F_: sp.diff(F_, x) / sp.sqrt(gg)
    sq = Y * sp.sqrt(gg)
    div = lambda f: sp.diff(Y * f, x) / sq
    # reduced Ricci coefficients (axis5.py X2)
    chi11, chi22 = e4(sp.log(gg) / 2), e4(sp.log(Y))
    chib11, chib22 = e3(sp.log(gg) / 2) + sp.diff(b, x) / Om, e3(sp.log(Y))
    trchi, chih = chi11 + chi22, (chi11 - chi22) / 2
    trchib, chibh = chib11 + chib22, (chib11 - chib22) / 2
    om, omb = -e4(sp.log(Om)) / 2, -e3(sp.log(Om)) / 2
    zeta = -sp.sqrt(gg) * sp.diff(b, v) / (4 * Om ** 2)
    eta, etab = zeta + e1(sp.log(Om)), -zeta + e1(sp.log(Om))
    K = -e1(e1(Y)) / Y
    # B1
    rnd = random.Random(7)
    vals = jet_values([Wf('1', '2', '3', '4'), Wf('1', '2', '1', '4'), Wf('1', '2', '1', '3'), Rf('1', '4', '3', '4')],
                      rnd)
    b1 = all(abs(q) < 1e-30 for q in vals[:3]) and abs(vals[3]) > 1e-3
    print('B1 W(e1, e2, e3, e4), W(e1, e2, e1, e4), W(e1, e2, e1, e3) at a random jet: %s (zero); R(e1, e4, e3, e4) = %s '
          '(not zero, the check is live) -> %s (%.0f s)' % (', '.join(mp.nstr(q, 3) for q in vals[:3]),
                                                           mp.nstr(vals[3], 5), 'PASS' if b1 else 'FAIL',
                                                           time.time() - t0), flush=True)
    ok &= b1
    beta = Wf('1', '4', '3', '4') / 2
    betab = Wf('1', '3', '3', '4') / 2
    rho = Wf('4', '3', '4', '3') / 4
    R41, R31, R34, R11, R22 = Ricf('4', '1'), Ricf('3', '1'), Ricf('3', '4'), Ricf('1', '1'), Ricf('2', '2')
    R44, R33 = Ricf('4', '4'), Ricf('3', '3')
    betar, betabr = beta - R41 / 2, betab + R31 / 2
    # B2 Gauss
    co, res = fit(K, [rho, Rs, R34, chih * chibh, trchi * trchib],
                  ['rho', 'R', 'Ric_34', 'chih chibh', 'tr chi tr chib'])
    b2 = res < 1e-25
    print('B2 Gauss: K = %s; residual at fresh jets %s -> %s (%.0f s)' % (
        ' + '.join('(%s) %s' % (c, l_) for l_, c in co.items()), mp.nstr(res, 3), 'PASS' if b2 else 'FAIL',
        time.time() - t0), flush=True)
    ok &= b2
    # B3 the pair: lower-order library
    rc = {'tr chi': trchi, 'chih': chih, 'tr chib': trchib, 'chibh': chibh, 'eta': eta, 'etab': etab, 'om': om,
          'omb': omb}
    curv = {'K': K, 'beta^r': betar, 'betab^r': betabr, 'rho': rho}
    ric = {'Ric_41': R41, 'Ric_31': R31, 'Ric_34': R34, 'Ric_11': R11, 'Ric_22': R22, 'Ric_44': R44, 'Ric_33': R33}
    k_ = e1(sp.log(Y))
    lib, lab = [], []
    def add(e, l_):
        lib.append(e); lab.append(l_)
    # (2.13): Om e4 K + Om tr chi K = c div(Om beta^r) + ...
    for nm_, f in (('eta tr chib', eta * trchib), ('eta chibh', eta * chibh), ('etab tr chib', etab * trchib),
                   ('etab chibh', etab * chibh), ('eta tr chi', eta * trchi), ('eta chih', eta * chih),
                   ('Ric_41', R41), ('Ric_31', R31), ('etab tr chi', etab * trchi), ('etab chih', etab * chih)):
        add(div(Om * f), 'div(Om %s)' % nm_)
    add(div(Om * betar), 'div(Om beta^r)')
    for nm_, f in (('chih', chih), ('tr chi', trchi)):
        for rn, r_ in (('Ric_34', R34), ('Ric_11', R11), ('Ric_22', R22), ('Ric_44', R44), ('Ric_33', R33)):
            add(Om * f * r_, 'Om %s %s' % (nm_, rn))
    add(Om * e4(R11 + R22), 'Om e4(Ric_11 + Ric_22)'); add(Om * e4(R34), 'Om e4 Ric_34'); add(Om * e3(R44), 'Om e3 Ric_44')
    add(Om * chibh * (R11 - R22), 'Om chibh (Ric_11 - Ric_22)'); add(Om * chih * (R11 - R22), 'Om chih (Ric_11 - Ric_22)')
    lhs13 = Om * e4(K) + Om * trchi * K
    co13, res13 = fit(lhs13, lib, lab, seed=11)
    print('B3 (2.13) Om e4 K + Om tr chi K = %s; residual %s (%.0f s)' % (
        ' + '.join('(%s) %s' % (c, l_) for l_, c in co13.items()), mp.nstr(res13, 3), time.time() - t0), flush=True)
    # (2.14): Om e3 beta^r + Om (tr chib - 2 omb) beta^r = c' Om e1 K + ...
    lib2, lab2 = [], []
    def add2(e, l_):
        lib2.append(e); lab2.append(l_)
    add2(Om * e1(K), 'Om e1 K')
    for cn, cv in (('betab^r', betabr), ('beta^r', betar)):
        for rn, r_ in rc.items():
            add2(Om * r_ * cv, 'Om %s %s' % (rn, cn))
    for rn in ('eta', 'etab'):
        add2(Om * rc[rn] * K, 'Om %s K' % rn)
    add2(Om * e1(chih * chibh), 'Om e1(chih chibh)'); add2(Om * e1(trchi * trchib), 'Om e1(tr chi tr chib)')
    for rn in ('eta', 'etab'):
        add2(Om * rc[rn] * chih * chibh, 'Om %s chih chibh' % rn); add2(Om * rc[rn] * trchi * trchib,
                                                                         'Om %s tr chi tr chib' % rn)
    add2(Om * e1(R11 + R22), 'Om e1(Ric_11 + Ric_22)'); add2(Om * e1(R11), 'Om e1 Ric_11')
    add2(Om * k_ * (R11 - R22), 'Om k (Ric_11 - Ric_22)'); add2(Om * e1(R34), 'Om e1 Ric_34')
    for rn in ('tr chib', 'chibh', 'tr chi', 'chih'):
        add2(Om * rc[rn] * R41, 'Om %s Ric_41' % rn); add2(Om * rc[rn] * R31, 'Om %s Ric_31' % rn)
    for rn in ('eta', 'etab'):
        for qn, q_ in (('Ric_34', R34), ('Ric_11', R11), ('Ric_22', R22), ('Ric_33', R33), ('Ric_44', R44)):
            add2(Om * rc[rn] * q_, 'Om %s %s' % (rn, qn))
    add2(Om * e3(R41), 'Om e3 Ric_41'); add2(Om * e4(R31), 'Om e4 Ric_31')
    lhs14 = Om * e3(betar) + Om * (trchib - 2 * omb) * betar
    co14, res14 = fit(lhs14, lib2, lab2, seed=21)
    print('B3 (2.14) Om e3 beta^r + Om (tr chib - 2 omegab) beta^r = %s; residual %s (%.0f s)' % (
        ' + '.join('(%s) %s' % (c, l_) for l_, c in co14.items()), mp.nstr(res14, 3), time.time() - t0), flush=True)
    c13 = co13.get('div(Om beta^r)', 0); c14 = co14.get('Om e1 K', 0)
    b3 = res13 < 1e-25 and res14 < 1e-25 and c13 != 0 and c13 == c14
    print('B3 both fits exact at fresh jets: %s; the principal coefficients div(Om beta^r): %s, Om e1 K: %s: an energy '
          'pair (equal): %s -> %s' % (res13 < 1e-25 and res14 < 1e-25, c13, c14, c13 == c14, 'PASS' if b3 else 'FAIL'))
    ok &= b3
    # control: beta for beta^r in (2.14)
    lhs_c = Om * e3(beta) + Om * (trchib - 2 * omb) * beta
    lib_c = [q.subs({}) for q in lib2]
    co_c, res_c = fit(lhs_c, [Om * e1(K)] + [l_ for l_, n_ in zip(lib2, lab2) if 'beta' not in n_ and 'Ric' not in n_],
                      ['Om e1 K'] + [n_ for n_ in lab2 if 'beta' not in n_ and 'Ric' not in n_], seed=31)
    ctl = res_c > 1e-10
    print('   control (beta for beta^r, the Ricci terms withheld): residual %s -> %s' % (
        mp.nstr(res_c, 3), 'fails (good)' if ctl else 'fits (bad)'))
    ok &= ctl
    print('axisbianchi5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
