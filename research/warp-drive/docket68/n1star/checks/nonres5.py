#!/usr/bin/env python3
"""nonres5: non-resonance of the two crossing phases at every order (FAMILIES5-FULL.md section 4).

On a round double-null background g0 = -2 e^(2 sig) du dv + R^2 dOmega_3^2 (sig, R arbitrary), with the ingoing phase
f(v) and the outgoing phase h(u) (any lam-independent normalisations, f', h' != 0), a term lam^j q(X) e^(i(n1 s1 + n2
s2)) E of the approximant, s1 = f/lam, s2 = h/lam, meets the reduced operator first at order lam^(j-2), through the
principal part -(1/2) g^ab d_a d_b alone (every other term of Ric^H has at most one derivative: N1STAR-PROOF.md (0.2)),
with the symbol sym(n1, n2) := (1/2) g0^-1(k, k), k := n1 f' dv + n2 h' du.

  N1 (exact) sym(n1, n2) = n1 n2 g0^uv f' h' = -e^(-2 sig) f' h' n1 n2: zero exactly on the pure harmonics (n1 n2 = 0),
     which are therefore solved by transport along their own generator, and on every mixed harmonic |sym| >= e^(-2 sig)
     |f' h'| > 0, uniformly in (n1, n2): there are no small divisors, and dividing loses no derivative. This is the
     whole of [Tou24]'s strong coherence (1.18) in this setting, for all mixed phases at once: in the (u, v) plane the
     null cone is two lines, and n1 f' dv + n2 h' du lies on neither unless n1 n2 = 0. Checked symbolically, and over
     every (n1, n2) with |n1|, |n2| <= 12.
  N2 (exact) the corrected phases u_in = f + lam phi_in, u_out = h + lam phi_out and the mean metric gbar = g0 + lam m
     change sym by lam (n1^2 a + n1 n2 b + n2^2 c), a, b, c bounded: at stage m only harmonics with |n1| + |n2| <= m +
     2 occur (each oscillating factor of weight w carries harmonics of total size <= w, and a monomial reaching order m
     has total weight <= m + 2: Lemma 5.1's weight count), so the correction is O(lam (m + 2)^2) and is moved to the
     next order, as the record does with its e_j; checked: the lam-coefficient of the corrected symbol is the stated
     quadratic form in (n1, n2).
  Control (exact): two ingoing radial phases f1(v), f2(v) (two families of the same orientation): sym = 0 on every
     harmonic (resonant: the mixed harmonics are not solved by division), and for f2 = 2 f1 the harmonic (2, -1) has
     d(2 f1 - f2) = 0: a zero-frequency combination, which feeds the mean.

Labels: computed (exact, sympy). Run: python3 checks/nonres5.py   (seconds)
"""
import sys

import sympy as sp


def main():
    u, v, lam = sp.symbols('u v lam')
    sig = sp.Function('sigma')(u, v)
    f, h = sp.Function('f')(v), sp.Function('h')(u)
    n1, n2 = sp.symbols('n1 n2', integer=True)
    ginv = sp.Matrix([[0, -sp.exp(-2 * sig)], [-sp.exp(-2 * sig), 0]])      # g0^-1 in (u, v), g0 = -2 e^(2 sig) du dv
    k = sp.Matrix([n2 * sp.diff(h, u), n1 * sp.diff(f, v)])                   # components (k_u, k_v)
    sym = sp.simplify((k.T * ginv * k)[0] / 2)
    n1ok = sp.simplify(sym + sp.exp(-2 * sig) * sp.diff(f, v) * sp.diff(h, u) * n1 * n2) == 0
    sg, fp, hp = sp.symbols('sg fp hp', positive=True)
    num = sym.subs({sp.Derivative(f, v): fp, sp.Derivative(h, u): hp}).subs(sig, sg)
    grid = all((abs(num.subs({n1: a, n2: b})) >= sp.exp(-2 * sg) * fp * hp) if a * b else num.subs({n1: a, n2: b}) == 0
               for a in range(-12, 13) for b in range(-12, 13))
    grid = bool(grid)
    print('  N1: sym(n1, n2) = %s: the stated form %s; zero on pure harmonics and |sym| >= e^(-2 sig) |f\' h\'| on every'
          ' mixed one with |n1|, |n2| <= 12: %s' % (sym, n1ok, grid), flush=True)
    # N2: corrections
    pin, pout = sp.Function('phi_in')(u, v), sp.Function('phi_out')(u, v)
    m = sp.Matrix(2, 2, lambda i, j: sp.Function('m%d%d' % (min(i, j), max(i, j)))(u, v))
    gbar_inv = ginv - lam * ginv * m * ginv                                     # (g0 + lam m)^-1 to first order
    kin = sp.Matrix([sp.diff(f + lam * pin, u), sp.diff(f + lam * pin, v)])
    kout = sp.Matrix([sp.diff(h + lam * pout, u), sp.diff(h + lam * pout, v)])
    kk = n1 * kin + n2 * kout
    full = sp.expand((kk.T * gbar_inv * kk)[0] / 2)
    c1 = sp.expand(full.coeff(lam, 1))
    quad = sp.Poly(c1, n1, n2)
    degs = {mono for mono in quad.monoms()}
    n2ok = all(sum(d) == 2 for d in degs) and sp.simplify(full.coeff(lam, 0) - sym) == 0
    print('  N2: the lam-coefficient of the corrected symbol is a quadratic form in (n1, n2) (monomials %s), its lam^0 '
          'part the symbol of N1: %s' % (sorted(degs), n2ok), flush=True)
    # control: two ingoing phases
    f1, f2 = sp.Function('f1')(v), sp.Function('f2')(v)
    kc = sp.Matrix([0, n1 * sp.diff(f1, v) + n2 * sp.diff(f2, v)])
    symc = sp.simplify((kc.T * ginv * kc)[0] / 2)
    zero_freq = sp.simplify(sp.diff(2 * f1 - (2 * f1), v)) == 0
    kc2 = (2 * sp.diff(f1, v) - 1 * sp.diff(2 * f1, v))
    ctl = symc == 0 and sp.simplify(kc2) == 0 and zero_freq
    print('  control (two ingoing phases): sym = %s on every harmonic (resonant); f2 = 2 f1: d(2 f1 - f2) = %s: %s'
          % (symc, sp.simplify(kc2), ctl), flush=True)
    ok = {'N1': n1ok and grid, 'N2': n2ok, 'control': ctl}
    for kname, val in ok.items():
        print(kname, 'PASS' if val else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
