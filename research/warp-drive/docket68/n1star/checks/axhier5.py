#!/usr/bin/env python3
"""axhier5.py -- CERTIFY-10L5-RESULT.md round 5, item 1: [Wu26]'s null structure equations in the axis chart,
reduced, off shell, the transport rows of the linearised axis hierarchy and its constraints.  Labels: deduced, verified
at random jets (each equation found by a linear fit at random rational jets of the general chart metric, at 45
digits, the coefficients rationalised, then checked at fresh jets; the library is reduced to independent members
first, as in axisbianchi5.py; the renormalised rows M1-M3 hand-derived and checked as identities at random jets).
These are probabilistic identity tests with fixed seeds, not symbolic proofs (the verifier of round 4, m11).

The metric is axis5.py's chart, general: ghat = -2 Om^2 (du dv + dv du) + gg (dx - b du)^2 + Y^2 dphi^2, with Om, gg,
b, Y arbitrary functions of (u, v, x); its own Ricci tensor is the source (no field equation is imposed).  Frame and
Ricci coefficients as in axisbianchi5.py (axis5.py X2): chi_11 = e4 log sqrt gg, chi_22 = e4 log Y, tr chi = chi_11 +
chi_22, chih = (chi_11 - chi_22)/2, likewise chib with b_x; omega = -e4 log Om/2, omegab = -e3 log Om/2; zeta =
-sqrt(gg) b_v/(4 Om^2), eta = zeta + e1 log Om, etab = -zeta + e1 log Om; k = e1 log Y; div f = e1 f + k f for a one-
form component f.  Curvature: beta, betab, rho from the Weyl tensor, beta^r = beta - Ric_41/2, betab^r = betab +
Ric_31/2, K = -Y^-1 e1 e1 Y.

  A1 Raychaudhuri, both directions:   Om e4 tr chi + (1/2) Om (tr chi)^2 = [fit],   and the e3 mirror.
  A2 the shears in the direction without alpha ([Wu26]'s route):  Om e3 chih + (1/2) Om tr chib chih = [fit] (expected:
     the traceless part of grad eta, (e1 eta - k eta)/2, quadratic terms, and the traceless Ricci part), and the mirror
     Om e4 chibh + (1/2) Om tr chi chibh = [fit].
  A3 torsion:  Om e4 eta = [fit] (beta^r), and Om e3 etab = [fit] (betab^r).
  A4 the lapse:  Om e4 omegab = [fit] (rho), and Om e3 omega = [fit].
  A5 the other traces:  Om e4 tr chib + (1/2) Om tr chi tr chib = [fit] (div etab, rho), and the mirror.
  A6 Codazzi:  e1 chih + 2 k chih = [fit] (e1 tr chi, beta^r), and the mirror for chibh (the operator of axis5.py X4 /
     Lemma 8.A4, whose regular solutions at the axis obey the r = 5 Hardy bound).
  A7 (deduced from A1-A6, printed) the structure of the rows: which frame derivatives of Ricci coefficients appear on
     each right side.  The transport rows A1, A3, A4 (and A2's partner terms) carry none; A2 carries e1 eta (resp.
     e1 etab) and A5 div etab (resp. div eta), the angular losses that [Wu26] removes through the mass aspects
     div eta - K and div etab - K; A6 is the constraint that recovers e1 chih from e1 tr chi and beta^r.
  Controls (each must fail): (c1) A1 with omega tr chi in place of 2 omega tr chi as a forced term (residual); (c2) A3
     with beta in place of beta^r and Ric_41 withheld (residual); (c3) A6 without the 2 k chih term (residual).

  python3 checks/axhier5.py
"""
import os, sys, time, importlib.util
import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('axisbianchi5', os.path.join(HERE, 'axisbianchi5.py'))
AB = importlib.util.module_from_spec(_s); _s.loader.exec_module(AB)
print = AB.print
u, v, x = AB.u, AB.v, AB.x
Om, gg, b, Y = AB.Om, AB.gg, AB.b, AB.Y


def show(co):
    return ' + '.join('(%s) %s' % (c, l_) for l_, c in co.items()) or '0'


def main():
    t0 = time.time(); ok = True
    g, Rf, Ricf, Rs, Wf = AB.build()
    e4 = lambda F_: sp.diff(F_, v) / Om
    e3 = lambda F_: (sp.diff(F_, u) + b * sp.diff(F_, x)) / Om
    e1 = lambda F_: sp.diff(F_, x) / sp.sqrt(gg)
    k = e1(sp.log(Y))
    dv1 = lambda f: e1(f) + k * f
    chi11, chi22 = e4(sp.log(gg) / 2), e4(sp.log(Y))
    chib11, chib22 = e3(sp.log(gg) / 2) + sp.diff(b, x) / Om, e3(sp.log(Y))
    trchi, chih = chi11 + chi22, (chi11 - chi22) / 2
    trchib, chibh = chib11 + chib22, (chib11 - chib22) / 2
    om, omb = -e4(sp.log(Om)) / 2, -e3(sp.log(Om)) / 2
    zeta = -sp.sqrt(gg) * sp.diff(b, v) / (4 * Om ** 2)
    eta, etab = zeta + e1(sp.log(Om)), -zeta + e1(sp.log(Om))
    K = -e1(e1(Y)) / Y
    beta = Wf('1', '4', '3', '4') / 2
    betab = Wf('1', '3', '3', '4') / 2
    rho = Wf('4', '3', '4', '3') / 4
    R41, R31, R34, R11, R22 = Ricf('4', '1'), Ricf('3', '1'), Ricf('3', '4'), Ricf('1', '1'), Ricf('2', '2')
    R44, R33 = Ricf('4', '4'), Ricf('3', '3')
    betar, betabr = beta - R41 / 2, betab + R31 / 2
    res = {}

    def run(tag, lhs, items, seed, tol=1e-25):
        lib = [e for _, e in items]; lab = [l_ for l_, _ in items]
        co, r_ = AB.fit(lhs, lib, lab, seed=seed)
        good = r_ < tol
        res[tag] = (co, r_, good)
        print('%s %s; residual at fresh jets %s; dependent members dropped: %s -> %s (%.0f s)' % (
            tag, show(co), mp.nstr(r_, 3), AB.fit.dropped or 'none', 'PASS' if good else 'FAIL', time.time() - t0),
            flush=True)
        return co, r_, good

    O = Om
    # A1
    _, _, g1 = run('A1 Om e4 tr chi + (1/2) Om (tr chi)^2 =', O * e4(trchi) + O * trchi ** 2 / 2,
                   [('Om chih^2', O * chih ** 2), ('Om omega tr chi', O * om * trchi), ('Om Ric_44', O * R44),
                    ('Om Ric_34', O * R34)], 101)
    _, _, g1b = run('A1 Om e3 tr chib + (1/2) Om (tr chib)^2 =', O * e3(trchib) + O * trchib ** 2 / 2,
                    [('Om chibh^2', O * chibh ** 2), ('Om omegab tr chib', O * omb * trchib), ('Om Ric_33', O * R33),
                     ('Om Ric_34', O * R34)], 102)
    ok &= g1 and g1b
    # A2
    lib2 = [('Om e1 eta', O * e1(eta)), ('Om k eta', O * k * eta), ('Om e1 etab', O * e1(etab)),
            ('Om k etab', O * k * etab), ('Om eta^2', O * eta ** 2), ('Om eta etab', O * eta * etab),
            ('Om etab^2', O * etab ** 2), ('Om omegab chih', O * omb * chih), ('Om omega chih', O * om * chih),
            ('Om tr chi chibh', O * trchi * chibh), ('Om tr chib chih', O * trchib * chih),
            ('Om (Ric_11 - Ric_22)', O * (R11 - R22)), ('Om Ric_34', O * R34), ('Om (Ric_11 + Ric_22)', O * (R11 + R22))]
    _, _, g2 = run('A2 Om e3 chih + (1/2) Om tr chib chih =', O * e3(chih) + O * trchib * chih / 2, lib2, 111)
    lib2b = [('Om e1 etab', O * e1(etab)), ('Om k etab', O * k * etab), ('Om e1 eta', O * e1(eta)),
             ('Om k eta', O * k * eta), ('Om etab^2', O * etab ** 2), ('Om eta etab', O * eta * etab),
             ('Om eta^2', O * eta ** 2), ('Om omega chibh', O * om * chibh), ('Om omegab chibh', O * omb * chibh),
             ('Om tr chib chih', O * trchib * chih), ('Om tr chi chibh', O * trchi * chibh),
             ('Om (Ric_11 - Ric_22)', O * (R11 - R22)), ('Om Ric_34', O * R34),
             ('Om (Ric_11 + Ric_22)', O * (R11 + R22))]
    _, _, g2b = run('A2 Om e4 chibh + (1/2) Om tr chi chibh =', O * e4(chibh) + O * trchi * chibh / 2, lib2b, 112)
    ok &= g2 and g2b
    # A3
    lib3 = [('Om tr chi eta', O * trchi * eta), ('Om chih eta', O * chih * eta), ('Om tr chi etab', O * trchi * etab),
            ('Om chih etab', O * chih * etab), ('Om beta^r', O * betar), ('Om Ric_41', O * R41),
            ('Om omega eta', O * om * eta), ('Om omega etab', O * om * etab)]
    _, _, g3 = run('A3 Om e4 eta =', O * e4(eta), lib3, 121)
    lib3b = [('Om tr chib etab', O * trchib * etab), ('Om chibh etab', O * chibh * etab),
             ('Om tr chib eta', O * trchib * eta), ('Om chibh eta', O * chibh * eta), ('Om betab^r', O * betabr),
             ('Om Ric_31', O * R31), ('Om omegab etab', O * omb * etab), ('Om omegab eta', O * omb * eta)]
    _, _, g3b = run('A3 Om e3 etab =', O * e3(etab), lib3b, 122)
    ok &= g3 and g3b
    # A4
    lib4 = [('Om omega omegab', O * om * omb), ('Om eta^2', O * eta ** 2), ('Om eta etab', O * eta * etab),
            ('Om etab^2', O * etab ** 2), ('Om rho', O * rho), ('Om Ric_34', O * R34),
            ('Om (Ric_11 + Ric_22)', O * (R11 + R22)), ('Om R', O * Rs), ('Om chih chibh', O * chih * chibh),
            ('Om tr chi tr chib', O * trchi * trchib)]
    _, _, g4 = run('A4 Om e4 omegab =', O * e4(omb), lib4, 131)
    _, _, g4b = run('A4 Om e3 omega =', O * e3(om), lib4, 132)
    ok &= g4 and g4b
    # A5
    lib5 = [('Om omega tr chib', O * om * trchib), ('Om omegab tr chib', O * omb * trchib), ('Om rho', O * rho),
            ('Om chih chibh', O * chih * chibh), ('Om div etab', O * dv1(etab)), ('Om div eta', O * dv1(eta)),
            ('Om etab^2', O * etab ** 2), ('Om eta etab', O * eta * etab), ('Om eta^2', O * eta ** 2),
            ('Om Ric_34', O * R34), ('Om (Ric_11 + Ric_22)', O * (R11 + R22)), ('Om R', O * Rs)]
    _, _, g5 = run('A5 Om e4 tr chib + (1/2) Om tr chi tr chib =', O * e4(trchib) + O * trchi * trchib / 2, lib5, 141)
    lib5b = [('Om omegab tr chi', O * omb * trchi), ('Om omega tr chi', O * om * trchi), ('Om rho', O * rho),
             ('Om chih chibh', O * chih * chibh), ('Om div eta', O * dv1(eta)), ('Om div etab', O * dv1(etab)),
             ('Om eta^2', O * eta ** 2), ('Om eta etab', O * eta * etab), ('Om etab^2', O * etab ** 2),
             ('Om Ric_34', O * R34), ('Om (Ric_11 + Ric_22)', O * (R11 + R22)), ('Om R', O * Rs)]
    _, _, g5b = run('A5 Om e3 tr chi + (1/2) Om tr chib tr chi =', O * e3(trchi) + O * trchib * trchi / 2, lib5b, 142)
    ok &= g5 and g5b
    # A6 Codazzi
    lib6 = [('e1 tr chi', e1(trchi)), ('zeta tr chi', zeta * trchi), ('zeta chih', zeta * chih),
            ('beta^r', betar), ('Ric_41', R41), ('eta tr chi', eta * trchi), ('eta chih', eta * chih)]
    _, _, g6 = run('A6 e1 chih + 2 k chih =', e1(chih) + 2 * k * chih, lib6, 151)
    lib6b = [('e1 tr chib', e1(trchib)), ('zeta tr chib', zeta * trchib), ('zeta chibh', zeta * chibh),
             ('betab^r', betabr), ('Ric_31', R31), ('etab tr chib', etab * trchib), ('etab chibh', etab * chibh)]
    _, _, g6b = run('A6 e1 chibh + 2 k chibh =', e1(chibh) + 2 * k * chibh, lib6b, 152)
    ok &= g6 and g6b
    # A7: structure
    deriv = {tag: [l_ for l_ in co if ('e1' in l_ or 'div' in l_)] for tag, (co, _, _) in res.items()}
    print('A7 (deduced) frame derivatives of Ricci coefficients on the right sides:')
    for tag, dl in deriv.items():
        print('   %s ... : %s' % (tag.split(' =')[0], ', '.join(dl) or 'none'))
    trans = [t_ for t_ in res if t_.startswith(('A1', 'A3', 'A4'))]
    a7 = all(not deriv[t_] for t_ in trans) and all(deriv[t_] for t_ in res if t_.startswith(('A2', 'A5', 'A6')))
    print('A7 the transport rows A1, A3, A4 carry none; A2 and A5 carry the angular derivatives of eta/etab (the losses '
          'the mass aspects remove), A6 carries e1 tr chi -> %s' % ('PASS' if a7 else 'FAIL'))
    ok &= a7
    # M: the renormalised rows, hand-derived from A1-A6 and axisbianchi5.py B2-B3b, checked as identities
    l1O = e1(sp.log(O))
    c11, c22 = trchi / 2 + chih, trchi / 2 - chih
    cb11, cb22 = trchib / 2 + chibh, trchib / 2 - chibh
    e4k = e1(c22) - c11 * k + l1O * c22
    e3k = e1(cb22) - cb11 * k + l1O * cb22
    mu, mub = dv1(eta) - K, dv1(etab) - K
    rhsM1 = (-dv1(c11 * (eta - etab)) - dv1(R41) - c11 * e1(eta) - l1O * (c11 * (eta - etab) + R41) + e4k * eta
             + trchi * K - dv1(etab * chih) - l1O * etab * chih + dv1(etab * trchi) / 2 + l1O * etab * trchi / 2)
    rhsM1b = (-dv1(cb11 * (etab - eta)) - dv1(R31) - cb11 * e1(etab) - l1O * (cb11 * (etab - eta) + R31)
              + e3k * etab + trchib * K - dv1(eta * chibh) - l1O * eta * chibh + dv1(eta * trchib) / 2
              + l1O * eta * trchib / 2)
    e4trchi = -trchi ** 2 / 2 - 2 * chih ** 2 - 2 * om * trchi - R44
    e3trchib = -trchib ** 2 / 2 - 2 * chibh ** 2 - 2 * omb * trchib - R33
    rhsM2 = e1(e4trchi) - c11 * e1(trchi) + l1O * e4trchi
    rhsM2b = e1(e3trchib) - cb11 * e1(trchib) + l1O * e3trchib
    G_ = Rs / 3 + R34 / 2 + chih * chibh - trchi * trchib / 4            # rho = -K + G_ (B2)
    e3om_K = 2 * om * omb - eta * etab + etab ** 2 / 2 + R34 / 6 + (R11 + R22) / 12      # e3 omega minus rho/2 (A4)
    e4omb_K = 2 * om * omb + eta ** 2 / 2 - eta * etab + R34 / 6 + (R11 + R22) / 12      # e4 omegab minus rho/2 (A4)
    e3br_K = (-(trchib - 2 * omb) * betar + 2 * chih * betabr - 3 * eta * K + e1(chih * chibh) - e1(trchi * trchib) / 4
              + 3 * eta * chih * chibh - 3 * eta * trchi * trchib / 4 + e1(R11 + R22) - e1(R11) - k * (R11 - R22)
              + trchi * R31 / 2 - chih * R31 + eta * R22)                     # e3 beta^r + e1 K (B3)
    e4bbr_K = (-(trchi - 2 * om) * betabr + 2 * chibh * betar + 3 * etab * K - e1(chih * chibh)
               + e1(trchi * trchib) / 4 - 3 * etab * chih * chibh + 3 * etab * trchi * trchib / 4 - e1(R11 + R22)
               + e1(R11) + k * (R11 - R22) - trchib * R41 / 2 + chibh * R41 - etab * R22)   # e4 betab^r - e1 K (B3b)
    kap, kapb = e1(om) - betar / 2, e1(omb) + betabr / 2
    rhsM3 = (e1(e3om_K) + e1(G_) / 2 - cb11 * e1(om) + l1O * (e3om_K + (-K + G_) / 2) - e3br_K / 2)
    rhsM3b = (e1(e4omb_K) + e1(G_) / 2 - c11 * e1(omb) + l1O * (e4omb_K + (-K + G_) / 2) + e4bbr_K / 2)
    rnd = AB.random.Random(171)

    def ident(tag, lhs, rhs, n=3, control=False):
        worst = 0
        for _ in range(n):
            d_, l_ = AB.jet_values([lhs - rhs, lhs], rnd)
            worst = max(worst, abs(d_) / max(1, abs(l_)))
        good = worst < 1e-30
        verdict = ('holds (bad)' if good else 'fails (good)') if control else ('PASS' if good else 'FAIL')
        print('%s: identity at %d random jets, relative residual %s -> %s (%.0f s)' % (
            tag, n, mp.nstr(worst, 3), verdict, time.time() - t0), flush=True)
        return good, worst
    gm = [ident('M1 e4 mu = R_M1, mu = div eta - K (div beta^r cancels; no e1 K, no e1 beta)', e4(mu), rhsM1)[0],
          ident('M1 e3 mub = R_M1b, mub = div etab - K (the mirror)', e3(mub), rhsM1b)[0],
          ident('M2 e4 (e1 tr chi) = e1(e4 tr chi) - chi_11 e1 tr chi + (e1 log Om) e4 tr chi (A1 commuted)',
                e4(e1(trchi)), rhsM2)[0],
          ident('M2 e3 (e1 tr chib) (the mirror)', e3(e1(trchib)), rhsM2b)[0],
          ident('M3 e3 kappa = R_M3, kappa = e1 omega - beta^r/2 (e1 K cancels between e1 rho/2 and -e3 beta^r/2)',
                e3(kap), rhsM3)[0],
          ident('M3 e4 kappab = R_M3b, kappab = e1 omegab + betab^r/2 (the mirror)', e4(kapb), rhsM3b)[0]]
    ok &= all(gm)
    _, wc4 = ident('control (c4) kappa with +beta^r/2 against the same right side', e3(e1(om) + betar / 2), rhsM3, 2,
                   control=True)
    ok &= wc4 > 1e-10
    print('M4 (deduced) the right sides R_M1..R_M3b contain, besides the unknowns: e1 eta, e1 etab, e1 chih, e1 chibh, '
          'e1 tr chi, e1 tr chib, e1 omega, e1 omegab and first angular derivatives of Ric; no e1 K and no derivative '
          'of beta^r or betab^r (by construction of the right sides above, which are checked identities).')
    # S: the scalar's two pairs in the chart (N9's analogue in four dimensions, measure 2 Om^2 sqrt(gg) Y)
    f = sp.Function('f')(u, v, x)
    a_, c_, d_ = e4(f), e1(f), e3(f)
    sg = 2 * O ** 2 * sp.sqrt(gg) * Y
    coords = [u, v, x]
    vec = lambda V4, V3, V1: [V3 / O, V4 / O, V3 * b / O + V1 / sp.sqrt(gg)]   # (u, v, x) components
    Div = lambda Vc: sum(sp.diff(sg * Vc[i], coords[i]) for i in range(3)) / sg
    gi = g.inv()
    box = sum(sp.diff(sg * sum(gi[i, j] * sp.diff(f, coords[j]) for j in range(3)), coords[i]) for i in range(3)) / sg
    rcs = {'tr chi': trchi, 'chih': chih, 'tr chib': trchib, 'chibh': chibh, 'omega': om, 'omegab': omb, 'eta': eta,
           'etab': etab}
    mons = {'a^2': a_ ** 2, 'c^2': c_ ** 2, 'd^2': d_ ** 2, 'a c': a_ * c_, 'a d': a_ * d_, 'c d': c_ * d_}
    libS = [(rn + ' ' + mn, rv * mv) for rn, rv in rcs.items() for mn, mv in mons.items()]
    libS += [('k ' + mn, k * mv) for mn, mv in mons.items()]
    _, _, gs1 = run('S1 Div(a^2 e3 + c^2 e4 - 2 a c e1) + 2 a Box f =', Div(vec(c_ ** 2, a_ ** 2, -2 * a_ * c_))
                    + 2 * a_ * box, libS, 181)
    _, _, gs2 = run('S2 Div(c^2 e3 + d^2 e4 - 2 c d e1) + 2 d Box f =', Div(vec(d_ ** 2, c_ ** 2, -2 * c_ * d_))
                    + 2 * d_ * box, libS, 182)
    ks = [l_ for l_ in list(res['S1 Div(a^2 e3 + c^2 e4 - 2 a c e1) + 2 a Box f ='][0]) +
          list(res['S2 Div(c^2 e3 + d^2 e4 - 2 c d e1) + 2 d Box f ='][0]) if l_.startswith('k ')]
    print('S3 the pairs\' quadratic forms contain the axis connection k = e1 log Y: %s (none: the pairs carry no 1/s '
          'coefficient, and their flux through the axis is Y times a bounded density, zero)' % (ks or 'none'))
    ok &= gs1 and gs2 and not ks
    # controls
    _, rc1 = AB.fit(O * e4(trchi) + O * trchi ** 2 / 2 + O * om * trchi,
                       [O * chih ** 2, O * R44], ['Om chih^2', 'Om Ric_44'], seed=161)
    _, rc2 = AB.fit(O * e4(eta), [e for l_, e in lib3 if l_ not in ('Om beta^r', 'Om Ric_41')] + [O * beta],
                       [l_ for l_, _ in lib3 if l_ not in ('Om beta^r', 'Om Ric_41')] + ['Om beta'], seed=162)
    _, rc3 = AB.fit(e1(chih), [e for _, e in lib6], [l_ for l_, _ in lib6], seed=163)
    cts = [rc1 > 1e-10, rc2 > 1e-10, rc3 > 1e-10]
    print('controls: (c1) A1 with omega tr chi: residual %s; (c2) A3 with beta, Ric_41 withheld: residual %s; (c3) A6 '
          'without 2 k chih: residual %s -> %s' % (mp.nstr(rc1, 3), mp.nstr(rc2, 3), mp.nstr(rc3, 3),
                                                   'all fail (good)' if all(cts) else 'A CONTROL FITS (bad)'))
    ok &= all(cts)
    print('axhier5 (%.0f s): %s' % (time.time() - t0, 'all checks pass' if ok else 'FAILURES'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
