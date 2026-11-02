#!/usr/bin/env python3
"""reduce5.py -- CERTIFY-10L5-RESULT.md round 3, F5: the class is (2+1)-dimensional gravity coupled to two free waves.
Labels: deduced, every identity exact (sympy, rational functions of the jets after the exponentials are named).

The class (dnsolve5.py), with P, Q taken as free functions (the record's P, Q of m, n are a special case):
    g5 = -4 e^{2W} du dv + R^2 [ e^{-2(P+Q)} (dx - (1-x^2) s du)^2 / (4(1-x^2)) + (1+x)/2 e^{2P} dphi1^2
         + (1-x)/2 e^{2Q} dphi2^2 ] = h + e^{2A} dphi1^2 + e^{2B} dphi2^2,
A = log R + P + (1/2) log((1+x)/2), B = log R + Q + (1/2) log((1-x)/2), h the orbit metric in (u, v, x).
Write rho = e^{A+B} (the area of the T^2 orbit over (2 pi)^2), L = log rho, psi = (A - B)/2 and the Einstein-frame orbit
metric  ht = rho^2 h.  Then for EVERY metric of the class (no field equation used):

  R1 (exact) Ric5(d_phi1, d_phi1) = -e^{2A} rho^2 Box_ht A,   Ric5(d_phi2, d_phi2) = -e^{2B} rho^2 Box_ht B.
  R2 (exact) on the orbit directions a, b in {u, v, x}:
         Ric5_ab = Ric(ht)_ab - (3/2) L_a L_b - 2 psi_a psi_b + (Box_ht L) ht_ab.
     So the vacuum equations of the class are exactly  Ric(ht) = dPhi1 dPhi1 + dPhi2 dPhi2,  Box_ht Phi_i = 0,  with
     Phi1 = sqrt(3/2) L and Phi2 = sqrt(2) psi = (A - B)/sqrt(2): (2+1)-dimensional gravity coupled to a free wave map
     into the flat plane.  [Wu26]'s Einstein-scalar system (1.4) (READ, p. 2) is the model, not its vacuum one; the
     reduced problem has no Weyl curvature (dimension 3) and its sections are one-dimensional (no shear, no Gauss
     curvature).  Its curvature residues are Ric(ht) - sum dPhi_i dPhi_i and Box_ht Phi_i.
  R3 (exact; the residual map) E_ab := Ric(ht)_ab - (3/2) L_a L_b - 2 psi_a psi_b equals
         Ric5_ab + (e^{-2A} Ric5_11 + e^{-2B} Ric5_22) h_ab,
     and Box_ht A = -e^{-2A} rho^-2 Ric5_11, Box_ht B = -e^{-2B} rho^-2 Ric5_22: the reduced residues are fixed linear
     combinations of the five-dimensional Ricci tensor, off shell, so a certified bound on one is a certified bound on
     the other (in the orthonormal frames of h and of g5: |E| <= |Ric5| + 3 max |Ric5|, termwise).
  R4 (exact) the Einstein frame in the record's variables: ht = -4 Omt^2 du dv + gt (dx - (1-x^2) s du)^2 with
         gt = R^6/16  (P and Q drop out)  and  log Omt = W + 2 log R + P + Q + (1/2) log((1 - x^2)/4),
     sqrt|det ht| = R^7 (1 - x^2) e^{2(P+Q) + 2W}/8.  So round 2's Jordan variable zeta = W + 2 log R + P + Q
     (symbol5.py Y1: the left null vector d zeta of the free formulation's principal symbol) IS the Einstein-frame lapse
     log Omt, up to a fixed function of x.  The free scheme evolved it through Ric_xx; the frame hierarchy of
     null3.py transports it by its own null-structure equation (omega, omegab), where it has no second x-derivative.
     The Einstein frame degenerates at the axes: Omt^2 ~ (1 - x^2) and Phi1, Phi2 carry log(1 -+ x).

  Controls (each must fail): (c1) the conformal weight rho in place of rho^2 in R2; (c2) the coefficient 1 in place of
  3/2 on L_a L_b in R2; (c3) R1 with rho in place of rho^2.

  python3 checks/reduce5.py
"""
import os, sys, time, importlib.util
import sympy as sp


def print(*a, **k):
    """print, every line wrapped at 121 characters (the record's line limit)"""
    import builtins, textwrap
    s = (k.pop('sep', ' ')).join(str(q) for q in a)
    lines = []
    for ln in s.split('\n'):
        if len(ln) <= 121:
            lines.append(ln)
        else:
            ind = len(ln) - len(ln.lstrip()) + 4
            lines.extend(textwrap.wrap(ln, 121, subsequent_indent=' ' * ind, break_on_hyphens=False))
    builtins.print('\n'.join(lines), **k)

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('dnull5', os.path.join(os.path.dirname(HERE), 'dnull5.py'))
dn = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(dn)

u, v, x, p1, p2 = sp.symbols('u v x phi1 phi2', real=True)
C5, C3 = [u, v, x, p1, p2], [u, v, x]
names = ('R', 'P', 'Q', 'W', 's')
F = {k: sp.Function(k)(u, v, x) for k in names}
R, P, Q, W, s = [F[k] for k in names]
EP, EQ, EW = sp.symbols('EP EQ EW', positive=True)


def jets(e):
    """derivatives of the fields -> symbols R_uv etc.; fields -> symbols; exp(aP + bQ + cW + d) -> EP^a EQ^b EW^c e^d"""
    e = e.doit()
    sub = {}
    for d in e.atoms(sp.Derivative):
        k = str(d.expr.func)
        combo = ''.join(sorted([str(vv) for vv, c in d.variable_count for _ in range(c)], key='uvx'.index))
        sub[d] = sp.Symbol(k + '_' + combo)
    e = e.xreplace(sub).xreplace({f: sp.Symbol(k) for k, f in F.items()})
    Ps, Qs, Ws = sp.symbols('P Q W')

    def ex(arg):
        arg = sp.expand(arg)
        a, b, c = arg.coeff(Ps), arg.coeff(Qs), arg.coeff(Ws)
        rest = sp.expand(arg - a * Ps - b * Qs - c * Ws)
        assert not (rest.free_symbols & {Ps, Qs, Ws}), arg
        return EP ** a * EQ ** b * EW ** c * sp.exp(rest)
    return e.replace(sp.exp, ex)


def zero(e):
    """exact: the rational function (after naming the exponentials) vanishes identically"""
    e = sp.together(sp.expand(jets(e)))
    return sp.expand(sp.numer(e)) == 0


def build():
    A = sp.log(R) + P + sp.log((1 + x) / 2) / 2
    B = sp.log(R) + Q + sp.log((1 - x) / 2) / 2
    Gx = R ** 2 * sp.exp(-2 * (P + Q)) / (4 * (1 - x ** 2)); beta = (1 - x ** 2) * s
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -2 * sp.exp(2 * W); g[2, 2] = Gx; g[0, 2] = g[2, 0] = -Gx * beta; g[0, 0] = Gx * beta ** 2
    g[3, 3] = R ** 2 * (1 + x) / 2 * sp.exp(2 * P); g[4, 4] = R ** 2 * (1 - x) / 2 * sp.exp(2 * Q)
    return A, B, g


def box(hm, sq, f):
    hi = hm.inv()
    return sum(sp.diff(sq * hi[a, b] * sp.diff(f, C3[b]), C3[a]) for a in range(3) for b in range(3)) / sq


def main():
    t0 = time.time(); ok = True
    A, B, g = build()
    good = zero(g[3, 3] - sp.exp(2 * A)) and zero(g[4, 4] - sp.exp(2 * B))
    print('R0 g_11 = e^{2A}, g_22 = e^{2B} with A, B as stated:', 'PASS' if good else 'FAIL'); ok &= good
    rho2 = R ** 4 * (1 - x ** 2) * sp.exp(2 * (P + Q)) / 4
    good = zero(rho2 - sp.exp(2 * (A + B)))
    print('   rho^2 = R^4 (1 - x^2) e^{2(P+Q)}/4 = e^{2(A+B)}:', 'PASS' if good else 'FAIL'); ok &= good
    h = g[:3, :3]
    ht = rho2 * h
    sq = R ** 7 * (1 - x ** 2) * sp.exp(2 * (P + Q) + 2 * W) / 8
    good = zero(sq ** 2 + ht.det())
    print('R4 sqrt|det ht| = R^7 (1 - x^2) e^{2(P+Q)+2W}/8:', 'PASS' if good else 'FAIL'); ok &= good
    gt = ht[2, 2]; Om2 = -ht[0, 1] / 2
    good = zero(gt - R ** 6 / 16) and zero(ht[0, 2] + gt * (1 - x ** 2) * s)
    good &= zero(ht[0, 0] - gt * ((1 - x ** 2) * s) ** 2)
    zeta = W + 2 * sp.log(R) + P + Q
    good &= zero(Om2 - sp.exp(2 * zeta) * (1 - x ** 2) / 4)
    print('R4 gt = R^6/16, the shift unchanged, Omt^2 = e^{2 zeta} (1 - x^2)/4 with zeta = W + 2 log R + P + Q:',
          'PASS' if good else 'FAIL'); ok &= good
    print('   (%.0f s) computing Ric(g5) ...' % (time.time() - t0), flush=True)
    Ric5 = dn.ricci(g, C5)
    print('   (%.0f s) computing Ric(ht) ...' % (time.time() - t0), flush=True)
    Rict = dn.ricci(ht, C3)
    print('   (%.0f s) checks ...' % (time.time() - t0), flush=True)
    bA, bB = box(ht, sq, A), box(ht, sq, B)
    good = zero(Ric5[3, 3] + sp.exp(2 * A) * rho2 * bA) and zero(Ric5[4, 4] + sp.exp(2 * B) * rho2 * bB)
    print('R1 Ric5_11 = -e^{2A} rho^2 Box_ht A, Ric5_22 = -e^{2B} rho^2 Box_ht B:', 'PASS' if good else 'FAIL')
    ok &= good
    c3 = zero(Ric5[3, 3] + sp.exp(2 * A) * sp.sqrt(rho2) * bA)
    print('   control (c3) rho in place of rho^2:', 'identity (bad)' if c3 else 'fails (good)'); ok &= not c3
    L, psi = A + B, (A - B) / 2
    bL = bA + bB
    d = lambda f, i: sp.diff(f, C3[i])

    def r2(i, j, coefL=sp.Rational(3, 2), hconf=ht):
        return Ric5[i, j] - (Rict[i, j] - coefL * d(L, i) * d(L, j) - 2 * d(psi, i) * d(psi, j) + bL * hconf[i, j])
    pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    res = {pq: zero(r2(*pq)) for pq in pairs}
    good = all(res.values())
    print('R2 Ric5_ab = Ric(ht)_ab - (3/2) L_a L_b - 2 psi_a psi_b + (Box_ht L) ht_ab, ab in uu uv ux vv vx xx:',
          ' '.join('%s%s' % ('uvx'[i], 'uvx'[j]) + ('+' if res[(i, j)] else '-') for i, j in pairs),
          'PASS' if good else 'FAIL'); ok &= good
    # the residual map R3: E_ab = Ric5_ab + (e^{-2A} Ric5_11 + e^{-2B} Ric5_22) h_ab
    tr = sp.exp(-2 * A) * Ric5[3, 3] + sp.exp(-2 * B) * Ric5[4, 4]
    good = all(zero(Rict[i, j] - sp.Rational(3, 2) * d(L, i) * d(L, j) - 2 * d(psi, i) * d(psi, j)
                    - Ric5[i, j] - tr * h[i, j]) for i, j in pairs)
    print('R3 E_ab = Ric5_ab + (e^{-2A} Ric5_11 + e^{-2B} Ric5_22) h_ab (all six):', 'PASS' if good else 'FAIL')
    ok &= good
    # c1: R2 with the Einstein frame built from rho instead of rho^2
    hc = sp.sqrt(rho2) * h
    Rc = dn.ricci(hc, C3)
    c1 = zero(Ric5[0, 1] - (Rc[0, 1] - sp.Rational(3, 2) * d(L, 0) * d(L, 1) - 2 * d(psi, 0) * d(psi, 1)
                           + bL * hc[0, 1])) and zero(Ric5[1, 1] - (Rc[1, 1] - sp.Rational(3, 2) * d(L, 1) ** 2
                                                                    - 2 * d(psi, 1) ** 2))
    print('   control (c1) the conformal weight rho in place of rho^2 (uv, vv):',
          'identity (bad)' if c1 else 'fails (good)')
    ok &= not c1
    c2 = zero(r2(1, 1, coefL=1)) and zero(r2(0, 1, coefL=1))
    print('   control (c2) coefficient 1 in place of 3/2 (vv, uv):', 'identity (bad)' if c2 else 'fails (good)')
    ok &= not c2
    print('reduce5 (%.0f s):' % (time.time() - t0), 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
