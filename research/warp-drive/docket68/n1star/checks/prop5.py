#!/usr/bin/env python3
"""prop5.py -- CERTIFY-10L5-RESULT.md round 4 (the verifier of round 3, finding 2(b)): what the hierarchy of null3.py
imposes, and what must propagate for it to be an existence scheme.  Labels: deduced (exact, sympy) for Q1-Q3.

The hierarchy (null3.py N8) transports chi, eta, omegab along e4 and chib, etab, omega along e3 by N1-N3, recovers the
metric (k, w, b) by d_v, and the scalars by their pairs.  Where its unknowns agree with the metric it builds (the
compatibility relations), its rows are N1-N3 with Ric replaced by sum dPhi_i dPhi_i, so it imposes
    E_44 = E_33 = E_x4 = E_x3 = 0  and  E_34 + E_xx = 0      (E := Ric(ht) - sum dPhi_i dPhi_i),
five of the six components, and Box Phi_i = 0 (P1, P4).  Two things are then left.

  Q1 (exact) the sixth component propagates.  If E has only E_34 = -q, E_xx = q in the null frame (the five imposed
     components zero), then S := E - (1/2)(tr E) ht has the single component S_34 = q, and its divergence is
        (div S)(e4) = -(1/2) e4 q + (lower order),  (div S)(e3) = -(1/2) e3 q + (lower order),  (div S)(ex) = (Ricci
        coefficients) q,
     the lower-order coefficients printed.  The contracted Bianchi identity div(Ric - (1/2) R ht) = 0 and
     div T = sum (Box Phi_i) dPhi_i, T the scalars' stress tensor, give div S = -sum (Box Phi_i) dPhi_i = 0 once the
     wave equations hold: so q obeys a homogeneous linear transport along e4 (and e3), and q = 0 on one initial cone
     implies q = 0 everywhere (Sachs and Rendall's lemma in the reduced system).  Control: with E_xx = 2q (the imposed
     combination E_34 + E_xx = 0 violated) S is not of that single-component form.
  Q2 (exact) the identity used: on the general (2+1)-metric and two scalars, div(Ric - (1/2) R ht - T) =
     -sum (Box Phi_i) dPhi_i, every component.
  Q3 (deduced, stated) the compatibility relations do not propagate by one-directional transport: chib = e^-w (k_u +
     b k_x + b_x), omegab = -e^-w (w_u + b w_x)/2 and eta + etab = 2 e^-k w_x (chi, omega and eta - etab agree with
     the metric by construction, since k, w, b are recovered from them by d_v).  e3 of the first needs k_uu, e4 of the
     second needs d_x omega, e4 of the third needs e4 etab: each is an angular or cross derivative of an unknown
     transported in the other direction.  So their propagation is a genuinely two-dimensional statement (in [Wu26]'s
     dimension it is done through the Bianchi equations, Christodoulou's and Luk's route); it is not shown here, and it
     is the input the hierarchy needs to be an existence scheme rather than an a priori estimate.

  python3 checks/prop5.py
"""
import os, sys, time, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('null3', os.path.join(HERE, 'null3.py'))
N3 = importlib.util.module_from_spec(_s); _s.loader.exec_module(N3)
print = N3.print
u, v, x = N3.u, N3.v, N3.x
X3 = [u, v, x]


def main():
    t0 = time.time(); ok = True
    w, c, b = N3.w, N3.c, N3.b
    g = N3.metric(); G = N3.christoffel(g); gi = g.inv()
    E4 = sp.Matrix([0, sp.exp(-w), 0]); E3 = sp.Matrix([sp.exp(-w), 0, sp.exp(-w) * b])
    EX = sp.Matrix([0, 0, sp.exp(-c)])
    # coframe: theta^4, theta^3, theta^x with theta^a(e_b) = delta
    Fm = sp.Matrix.hstack(E3, E4, EX)                       # columns: e3, e4, ex
    Cof = Fm.inv()                                          # rows: theta^3, theta^4, theta^x
    q = sp.Function('q')(u, v, x)

    def tensor_from_frame(comp, qq):
        """covariant 2-tensor with frame components comp[(i, j)] (i, j in '34x'), symmetric"""
        idx = {'3': 0, '4': 1, 'x': 2}
        T = sp.zeros(3)
        for (i, j), val in comp.items():
            th_i, th_j = Cof[idx[i], :], Cof[idx[j], :]
            T += val * (th_i.T * th_j + (th_j.T * th_i if i != j else 0 * th_i.T * th_j))
        return T

    def div(T):
        """(div T)_b = g^{ac} (d_c T_ab - G^d_{ca} T_db - G^d_{cb} T_ad)"""
        out = []
        for bb in range(3):
            s_ = 0
            for a in range(3):
                for cc in range(3):
                    if gi[a, cc] == 0:
                        continue
                    term = sp.diff(T[a, bb], X3[cc]) - sum(G[d][cc][a] * T[d, bb] for d in range(3)) \
                        - sum(G[d][cc][bb] * T[a, d] for d in range(3))
                    s_ += gi[a, cc] * term
            out.append(s_)
        return sp.Matrix(out)
    E = tensor_from_frame({('3', '4'): -q, ('x', 'x'): q}, q)
    trE = sum(gi[a, cc] * E[a, cc] for a in range(3) for cc in range(3))
    S = E - trE / 2 * g
    fr = lambda T, X, Y: (X.T * T * Y)[0]
    comps = {'S_33': fr(S, E3, E3), 'S_44': fr(S, E4, E4), 'S_34': fr(S, E3, E4), 'S_xx': fr(S, EX, EX),
             'S_x3': fr(S, EX, E3), 'S_x4': fr(S, EX, E4)}
    single = N3.zero(comps['S_34'] - q) and all(N3.zero(comps[k_]) for k_ in comps if k_ != 'S_34') and \
        N3.zero(trE - 2 * q)
    print('Q1 E_34 = -q, E_xx = q (the five imposed components zero): tr E = 2q and S = E - (tr E/2) ht has S_34 = q '
          'only: %s' % single)
    ok &= single
    Em = tensor_from_frame({('3', '4'): -q, ('x', 'x'): 2 * q}, q)
    trm = sum(gi[a, cc] * Em[a, cc] for a in range(3) for cc in range(3))
    Sm = Em - trm / 2 * g
    single_m = N3.zero(fr(Sm, E3, E4) - q) and N3.zero(fr(Sm, EX, EX))
    print('   control (E_xx = 2q): single-component form %s' % ('holds (bad)' if single_m else 'fails (good)'))
    ok &= not single_m
    dS = div(S)
    vec = lambda X, F_: sum(X[n] * sp.diff(F_, X3[n]) for n in range(3))
    form = {'chi': sp.exp(-w) * sp.diff(c, v), 'chib': sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x) + sp.diff(b, x)),
            'omega': -sp.exp(-w) * sp.diff(w, v) / 2, 'omegab': -sp.exp(-w) * (sp.diff(w, u) + b * sp.diff(w, x)) / 2,
            'eta': -sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x),
            'etab': sp.exp(c - 2 * w) * sp.diff(b, v) / 4 + sp.exp(-c) * sp.diff(w, x)}
    names = list(form)
    terms_q = [form[n_] * q for n_ in names] + [vec(E4, q), vec(E3, q), vec(EX, q)]
    labels = ['%s q' % n_ for n_ in names] + ['e4 q', 'e3 q', 'ex q']
    cs = sp.symbols('k0:20')
    res = {}
    for tag, X in (('e4', E4), ('e3', E3), ('ex', EX)):
        lhs = (X.T * dS)[0]
        expr = lhs - sum(k * t for k, t in zip(cs, terms_q))
        e = N3.num(N3.jets(expr))
        jsyms = sorted(e.free_symbols - set(cs), key=str)
        eqs = sp.Poly(e, *jsyms).coeffs()
        sol = sp.solve(eqs, cs[:len(terms_q)], dict=True)
        if not sol:
            res[tag] = None; continue
        sol = sol[0]
        free = [cs[i] for i in range(len(terms_q)) if cs[i] not in sol]
        coef = [sp.sympify(sol.get(cs[i], 0)).subs({f_: 0 for f_ in free}) for i in range(len(terms_q))]
        chk = N3.zero(lhs - sum(k * t for k, t in zip(coef, terms_q)))
        res[tag] = (chk, {l_: k for l_, k in zip(labels, coef) if k != 0})
    good = all(r_ is not None and r_[0] for r_ in res.values())
    for tag, r_ in res.items():
        print('   (div S)(%s) = %s' % (tag, ' + '.join('(%s) %s' % (k, l_) for l_, k in r_[1].items()) if r_ else 'no fit'))
    tr4 = res['e4'] and res['e4'][1].get('e4 q', 0) != 0 and 'e3 q' not in res['e4'][1] and 'ex q' not in res['e4'][1]
    tr3 = res['e3'] and res['e3'][1].get('e3 q', 0) != 0 and 'e4 q' not in res['e3'][1] and 'ex q' not in res['e3'][1]
    print('Q1 (div S)(e4) is a transport of q along e4 alone: %s; (div S)(e3) along e3 alone: %s ->' % (tr4, tr3),
          'PASS' if good and tr4 and tr3 else 'FAIL')
    ok &= good and bool(tr4) and bool(tr3)
    # Q2: the contracted Bianchi identity with the scalars, on the general metric
    P1, P2 = sp.Function('P1')(u, v, x), sp.Function('P2')(u, v, x)
    Ric = N3.ricci(g, G)
    Rs = sum(gi[a, cc] * Ric[a, cc] for a in range(3) for cc in range(3))
    dP = lambda P: sp.Matrix([sp.diff(P, X3[i]) for i in range(3)])
    sq = 2 * sp.exp(2 * w + c)
    box = lambda P: sum(sp.diff(sq * gi[i, j] * sp.diff(P, X3[j]), X3[i]) for i in range(3) for j in range(3)) / sq
    T = sp.zeros(3)
    for P in (P1, P2):
        dp = dP(P)
        T += dp * dp.T - (dp.T * gi * dp)[0] / 2 * g
    Ein = Ric - Rs / 2 * g - T
    dE = div(Ein)
    rhs = -(box(P1) * dP(P1) + box(P2) * dP(P2))
    q2 = all(N3.zero(dE[i] - rhs[i]) for i in range(3))
    print('Q2 div(Ric - R ht/2 - T) = -sum (Box Phi_i) dPhi_i on the general (2+1)-metric, all three components: %s ->' %
          q2, 'PASS' if q2 else 'FAIL')
    ok &= q2
    # control: a wrong normalisation of T (the 1/2 dropped) breaks Q2
    Tw = sp.zeros(3)
    for P in (P1, P2):
        dp = dP(P)
        Tw += dp * dp.T - (dp.T * gi * dp)[0] * g
    ctl = all(N3.zero(div(Ric - Rs / 2 * g - Tw)[i] - rhs[i]) for i in range(3))
    print('   control (T with |dPhi|^2 g in place of |dPhi|^2 g/2): %s' % ('holds (bad)' if ctl else 'fails (good)'))
    ok &= not ctl
    print('Q3 (deduced, stated) the compatibility relations of chib, omegab, eta + etab with the metric are not '
          'propagated by any one-directional row: not shown (see the docstring).')
    print('prop5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
