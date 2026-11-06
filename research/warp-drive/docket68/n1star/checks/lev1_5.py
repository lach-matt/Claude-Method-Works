#!/usr/bin/env python3
"""lev1_5.py -- CERTIFY-10L5-RESULT.md round 4 (task 4, level 1): Theorem 7.L's system commuted once with the
background's e_x, its closure, and its constant on the record's solution.  Labels: deduced (exact, sympy) for L1-L3;
computed (floating point, on the record's run, as linest5.py E4) for L4.

Commute every row of linest5.py's linearised system (fifteen frame-difference unknowns Z) with e_x = e^{-k} d_x of the
background, and put Z' := e_x Z.  With null3.py N4's commutators,
    [e_x, e4] = chi e_x - (eta + etab)/2 e4,   [e_x, e3] = chib e_x - (eta + etab)/2 e3,   [e_x, d_v] = e^w chi e_x,
each row X(dY) = sum m_Z Z + S becomes
    X(dY') = sum (e_x m_Z) Z + sum m_Z Z' - c_X dY' + (eta + etab)/2 (X dY) + e_x S,
with X dY replaced by its own row (and, for the pairs, e3 a = e_x c + ..., e4 c = e_x a + ..., e3 c = e_x d + ...,
e4 d = e_x c + ...).  The pairs commute into pairs for (a', c') and (c', d') with the same principal parts.

  L1 (exact) the three commutators on the general (2+1)-metric of null3.py, applied to an arbitrary function; control:
     the e4 commutator without its (eta + etab)/2 e4 term must fail.
  L2 (exact) the thirty-unknown level-1 system: no x-derivative of a level-1 unknown (a level-2 term) on any right
     side; the background enters through its state, its first and second x-derivatives and those of w and k only.
     The table (which unknowns enter which level-1 row) is printed.
  L3 control: commuting linest5.py E3's control row (chib by null3.py N7's e4 equation, which carries e_x(d etab))
     puts a level-2 term on a right side, and the check must flag it.
  L4 (computed) the level-1 constant on rcert5's box, |x| <= 1/2: the unweighted coefficient profile and F^2 as in
     linest5.py E4b, and the weighted one of wgron5.py's Theorem 8.W (optimal weights), for the thirty unknowns.

  Theorem 8.L1 (deduced: Theorem 7.L's proof, unchanged, on the thirty-unknown system).  On the same truncated domains,
     f_1(u, v) <= (D_1 + S_1) exp(2 int a_o^(1) du + 2 int a_i^(1) dv), with f_1 the level-0 norm of (Z, Z') and the
     coefficient sums of L4.  Since H^1 of a one-dimensional section embeds in L^inf (||f||_inf <= ||f||/sqrt|I| +
     sqrt|I| ||f'||), it bounds Z in L^inf on the sections: the control the quadratic remainder needs away from the axes.

  python3 checks/lev1_5.py [RUN.npz]        (RUN: the record's l1_rc0.9_M32.npz; without it L4 is skipped)
"""
import os, sys, time, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('linest5', os.path.join(HERE, 'linest5.py'))
L5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(L5)
_s = importlib.util.spec_from_file_location('wgron5', os.path.join(HERE, 'wgron5.py'))
WG = importlib.util.module_from_spec(_s); _s.loader.exec_module(WG)
print = L5.print
N3 = L5.N3
UNK = L5.UNK
U = L5.U
U1 = {n: sp.Symbol('p' + n) for n in UNK}
UNK1 = UNK + ['p' + n for n in UNK]
DXX = {s_: sp.Symbol('XX_' + str(s_)) for s_ in L5.STATE}
WX, KX = sp.symbols('WX KX')
chi, chib, eta, etab = L5.chi, L5.chib, L5.eta, L5.etab
Ew, Ek = L5.Ew, L5.Ek


def ex_bg(m):
    """e_x of a background coefficient m(state, Ew, Ek, DX)"""
    d = sum(sp.diff(m, s_) * L5.DX[s_] for s_ in L5.STATE)
    d += sp.diff(m, Ew) * Ew * WX + sp.diff(m, Ek) * Ek * KX
    d += sum(sp.diff(m, L5.DX[s_]) * DXX[s_] for s_ in L5.STATE)
    return d / Ek


def ex_rhs(rhs):
    """e_x of a right side linear in the level-0 unknowns (and possibly carrying dx_<unknown> symbols)"""
    out = 0
    for n in UNK:
        co = rhs.coeff(U[n])
        if co != 0:
            out += ex_bg(co) * U[n] + co * U1[n]
    dxs = [q for q in rhs.free_symbols if str(q).startswith('dx_')]
    for q in dxs:                                   # a level-1 term in a level-0 row: its e_x is level 2
        co = rhs.coeff(q)
        out += co * sp.Symbol('dxx_' + str(q)[3:]) / Ek + ex_bg(co) * q
    return sp.expand(out)


def rows1(R):
    R1 = {}
    hx = (eta + etab) / 2
    for name, (op, bnd, rhs, fac) in R.items():
        r1 = ex_rhs(rhs)
        if op == 'e4':
            r1 += -chi * U1[bnd] + hx * rhs
        elif op == 'e3':
            r1 += -chib * U1[bnd] + hx * rhs
        elif op == 'dv':
            r1 += -Ew * chi * U1[bnd]
        else:
            i = name[-1]
            a, c, d = 'da' + i, 'dc' + i, 'dd' + i
            if name.startswith('P1'):
                r1 += -chib * U1[a] + hx * (U1[c] + rhs)
            elif name.startswith('P2'):
                r1 += -chi * U1[c] + hx * (U1[a] + rhs)
            elif name.startswith('P3'):
                r1 += -chib * U1[c] + hx * (U1[d] + rhs)
            else:
                r1 += -chi * U1[d] + hx * (U1[c] + rhs)
        R1['p' + name] = (op, 'p' + bnd, sp.expand(r1), fac)
    return R1


def l1():
    w, c, b, f = N3.w, N3.c, N3.b, N3.f
    u, v, x = N3.u, N3.v, N3.x
    e4 = lambda F_: sp.exp(-w) * sp.diff(F_, v)
    e3 = lambda F_: sp.exp(-w) * (sp.diff(F_, u) + b * sp.diff(F_, x))
    ex = lambda F_: sp.exp(-c) * sp.diff(F_, x)
    k4 = sp.exp(-w) * sp.diff(c, v)
    k3 = sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x) + sp.diff(b, x))
    z = -sp.exp(c - 2 * w) * sp.diff(b, v) / 4
    et, etb = z + sp.exp(-c) * sp.diff(w, x), -z + sp.exp(-c) * sp.diff(w, x)
    hx = (et + etb) / 2
    r4 = N3.zero(ex(e4(f)) - e4(ex(f)) - (k4 * ex(f) - hx * e4(f)))
    r3 = N3.zero(ex(e3(f)) - e3(ex(f)) - (k3 * ex(f) - hx * e3(f)))
    rv = N3.zero(ex(sp.diff(f, v)) - sp.diff(ex(f), v) - sp.exp(w) * k4 * ex(f))
    ctl = N3.zero(ex(e4(f)) - e4(ex(f)) - k4 * ex(f))
    return r4, r3, rv, ctl


def level2(rhs):
    return sorted(str(q) for q in rhs.free_symbols if str(q).startswith('dx_p') or str(q).startswith('dxx_'))


def main():
    t0 = time.time(); ok = True
    r4, r3, rv, ctl = l1()
    good = r4 and r3 and rv and not ctl
    print('L1 (exact) [e_x, e4] = chi e_x - (eta + etab)/2 e4: %s; [e_x, e3] = chib e_x - (eta + etab)/2 e3: %s; '
          '[e_x, d_v] = e^w chi e_x: %s; control (e4 without the (eta + etab)/2 term): %s ->' % (
              r4, r3, rv, 'fails (good)' if not ctl else 'holds (bad)'), 'PASS' if good else 'FAIL')
    ok &= good
    R = L5.rows()
    R1 = rows1(R)
    bad = {nm: level2(r[2]) for nm, r in R1.items() if level2(r[2])}
    print('L2 the level-1 rows (%d), the unknowns on each right side:' % len(R1))
    for nm, (op, bnd, rhs, fac) in R1.items():
        lst = sorted({str(q) for q in rhs.free_symbols if str(q) in set(UNK1)}, key=UNK1.index)
        print('   %-8s (%s, bounds %s): %s' % (nm, op, bnd, ' '.join(lst)))
    allsyms = set().union(*[r[2].free_symbols for r in R1.values()])
    bgok = all(str(q) in set(UNK1) | {str(s_) for s_ in L5.STATE} | {'Ew', 'Ek', 'WX', 'KX'} or
               str(q).startswith('X_') or str(q).startswith('XX_') for q in allsyms)
    good = not bad and bgok
    print('   no level-2 term on any right side: %s; the background through state, DX, DXX, w_x, k_x only: %s ->' % (
        not bad, bgok), 'PASS' if good else 'FAIL')
    ok &= good
    ctl_rhs = sp.expand(L5.lin(-chi * chib) + 2 * sp.Symbol('dx_detab') / Ek)
    hit = level2(ex_rhs(ctl_rhs))
    print('L3 control: chib by null3.py N7\'s e4 equation, commuted: level-2 terms %s ->' % hit,
          'fails (good)' if hit else 'passes (bad)')
    ok &= bool(hit)
    if len(sys.argv) > 1:
        bg, inbox, uu, vv, x = L5.background(sys.argv[1])
        M = len(x)
        _, D1, _ = L5.D5.cheb_gauss(M)
        dxa = lambda A_: np.einsum('ij,abj->abi', D1, A_)
        for s_ in L5.STATE:
            bg[DXX[s_]] = dxa(bg[L5.DX[s_]])
        bg[WX] = dxa(np.log(bg[Ew])); bg[KX] = dxa(np.log(bg[Ek]))
        # the level-1 rows' terms, with linest5's bookkeeping; the measure terms as at level 0
        syms = L5.STATE + [Ew, Ek] + list(L5.DX.values()) + list(DXX.values()) + [WX, KX]
        args = [bg[s_] for s_ in syms]
        one = np.ones_like(bg[Ew])
        T, D = [], {n: 0.0 * one for n in UNK1}
        Rall = dict(R); Rall.update(R1)
        Uall = dict(U); Uall.update({'p' + n: U1[n] for n in UNK})
        for name, (op, bnd, rhs, fac) in Rall.items():
            fac_v = bg[Ew] if fac == Ew else 1.0
            for n in UNK1:
                co = rhs.coeff(Uall[n])
                if co == 0:
                    continue
                cv = np.abs(sp.lambdify(syms, co, 'numpy')(*args) * fac_v) * one
                if n == bnd:
                    D[bnd] = D[bnd] + 2 * cv
                else:
                    T.append((bnd, n, cv))
            if op in ('e4', 'dv'):
                D[bnd] = D[bnd] + np.abs(bg['dv_lw']) + 1.0
            elif op == 'e3':
                D[bnd] = D[bnd] + np.abs(bg['du_lw'] + bg['dx_bw']) + 1.0
            else:
                D[bnd] = D[bnd] + 1.0
        E = bg[Ew]
        q3 = np.abs(E * (bg[chib] - 2 * bg[L5.omb])); q4 = np.abs(E * (bg[chi] - 2 * bg[L5.om]))
        qx = np.abs(E * (bg[eta] + bg[etab]))
        for pre in ('', 'p'):
            for i in (1, 2):
                D[pre + 'da%d' % i] = D[pre + 'da%d' % i] + q3 + qx
                D[pre + 'dc%d' % i] = D[pre + 'dc%d' % i] + q4 + qx + q3 + qx
                D[pre + 'dd%d' % i] = D[pre + 'dd%d' % i] + q4 + qx
        typ = dict(L5.TYPE); typ.update({'p' + n: L5.TYPE[n] for n in UNK})
        grp = {n: WG.GROUP[n] for n in UNK}; grp.update({'p' + n: 'p' + WG.GROUP[n] for n in UNK})
        groups = list(dict.fromkeys(grp[n] for n in UNK1))
        sel = inbox[:, :, None] & (np.abs(x)[None, None, :] <= 0.5)
        B = WG.Bound(T, D, sel, uu, vv, unk=UNK1, typ=typ, group=grp, groups=groups)
        J1, Io, Ii = B.J_exact(np.zeros(len(groups)), np.zeros(len(T)))
        print('L4 (computed) level 1 on |x| <= 1/2, unweighted: int a_o du = %.1f, int a_i dv = %.1f, F_1^2 = 10^%.1f '
              '(level 0: 10^138.0)' % (Io, Ii, J1 / np.log(10)))
        from scipy.optimize import minimize
        p0 = np.zeros(len(groups) + len(T)); best = None
        for it in range(3):
            r_ = minimize(B.J_relaxed, p0, method='L-BFGS-B', options=dict(maxiter=3000))
            p0 = r_.x
            Jx = B.J_exact(r_.x[:len(groups)], r_.x[len(groups):])
            if best is None or Jx[0] < best[0][0]:
                best = (Jx, r_.x.copy())
        (Jx, Io, Ii), p = best
        tw = p[:len(groups)]
        print('   weighted (Theorem 8.W\'s optimum): log(max/min lam) = %.2f, int a_o du = %.1f, int a_i dv = %.1f, '
              'F_1^2 = 10^%.1f (level 0 weighted: 10^66.9)' % (tw.max() - tw.min(), Io, Ii, Jx / np.log(10)))
    print('lev1_5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
