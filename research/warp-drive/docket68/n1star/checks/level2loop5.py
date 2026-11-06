"""level2loop5.py -- the level-2 rounds of III.I(11) Step 3 against E_ind's least element (LOSS-D LD13, D529).

III.I(11) Step 3 (PART-III-I12-SPECTRAL.md:278-281) treats each tf-exponent (alpha_0, k) of g_2 with
1 + eta_1 <= Re alpha_0 < 2 + eta_2, and "its remainder exponents alpha_0 + E_ind may again lie below 2 + eta_2, and
are treated in turn (finitely many rounds, the real parts rising by >= eps_ind)". LOSS-D LD12 (v) counted that loop
as about (1 + eta_2 - eta_1)/eps_ind rounds per chain, of order 1/(eps_K eps_ind) over the beta-chain "if the smallest
element of E_ind is about eps_ind". This script computes, exactly at the record's point z = 4e-6, what E_ind's least
elements are on LD9's reading of its classes, and what that does to the count.

The roots are III.D Lemma 4.1's list (PART-III-D-GAUGEPOT.md:186-206): the non-integer roots of Box^Upsilon(0) above
1/2 are lambda_s0,2 = (1 + (9 + 4z)^(1/2))/2 and, for l >= 1, lambda = 1/2 + (1/4 + s)^(1/2) with s a root of
Q_l(s) = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa, kappa = l (l + 2); the other factors have integer
roots. Exponents are roots plus non-negative integers (D4:52-60), and the record's classes
(PART-III-D3-SYMSTATES.md:143-148) are A^((2,0) u (2 + E_ind)) and A^((1,0) u (1 + E_ind)): a root lambda enters
E_ind as lambda - b + j, b in {1, 2}, j >= 0, when that is positive (LD9).

  L1  the roots at z = 4e-6, exact to 40 digits: d1 = lambda_s1,2 - 2, d0 = lambda_s0,2 - 2, delta_2, delta'_1, and
      delta_50 (LD10's bound on eps_ind, which LD10 E3 puts at 1.94137e-8);
  L2  E_ind's elements below 2 over l <= 50, on two readings. LD9's, per state: the s0 state is rho^2 C^infty
      (D3:143), so lambda_s0,2 enters only through a class 1 + E_ind (the mass state's gauge part), as 1 + d0, and
      the sl roots through either class; then the only element below 1 is d1, the next 1 + delta_2. The broad
      reading, every root through either class (a rho^(2+d0) term in some 2 + E_ind class, which no cited state
      carries): then d0 is below 1 too. Controls: a class base b = 3 makes the least element delta_2 < d1, and
      b = l + 1 in harmonic l makes it delta_50 (the record's base-3 classes, F4:97, 299-300 and I12:96-98, are
      derivative images of base-2 terms with the same offsets, so they add nothing below 1, and b = l + 1 does not occur
      at b_0; D531); the integer roots add the element 1 itself, one more point per chain (D531);
  L3  the window: eta_2 - eta_1 < eps_+ < eps_ind <= delta_50 (I12:58-59, LD7, LD10), and every element of E_ind in
      [1, 2) exceeds 1 + delta_50, so in [1 + eta_1, 2 + eta_2) a chain adds only elements below 1: on LD9's reading
      alpha_0 + n d1, at most floor((1 + delta_50)/d1) + 1 rounds; on the broad one alpha_0 + n d1 + m d0, the
      lattice points below 1 + delta_50, counted exactly (d0 - 4 d1 = 5.6e-13 is not 0, so they are distinct);
  L4  per beta-level, the level-3 rounds of LD11 average about (1/2)/eps_ind >= (1/2)/delta_50; the ratio of L3's
      count per chain to that, on each reading.

Run: python3 checks/level2loop5.py   (stdlib only, about two seconds)
"""
from decimal import Decimal, getcontext
import sys

getcontext().prec = 60
Z = Decimal('4e-6')
LMAX = 50


def sqrt(x):
    return x.sqrt()


def s0_root():
    return (1 + sqrt(9 + 4 * Z)) / 2


def sl_roots(l):
    """the two Q_l roots, as lambda = 1/2 + (1/4 + s)^(1/2), ordered: lambda_sl,l+1 < lambda_sl,l+2"""
    k = Decimal(l * (l + 2))
    b = 2 + 2 * k + Z
    c = k * (k + 1) + Z * k
    disc = sqrt(b * b - 4 * c)
    s1, s2 = (b - disc) / 2, (b + disc) / 2
    half = Decimal('0.5')
    return half + sqrt(Decimal('0.25') + s1), half + sqrt(Decimal('0.25') + s2)


def frac(x):
    return x - int(x)


def e_ind(s0_bases, sl_bases, lmax=LMAX, top=Decimal(2)):
    """E_ind's elements below `top`: lambda - b + j > 0 for each non-integer root lambda and each class base b"""
    roots = [(s0_root(), s0_bases)]
    for l in range(1, lmax + 1):
        for lam in sl_roots(l):
            roots.append((lam, sl_bases(l)))
    out = set()
    for lam, bases in roots:
        for base in bases:
            x = lam - base
            while x <= 0:
                x += 1
            while x < top:
                out.add(x)
                x += 1
    return sorted(out)


def lattice_count(g1, g2, top):
    """#{(n, m) >= 0 : n g1 + m g2 < top}, exactly"""
    tot, m = 0, 0
    while m * g2 < top:
        r = top - m * g2
        q = int(r / g1)
        tot += q + (0 if q * g1 >= r else 1)
        m += 1
    return tot


def main():
    ok = True

    def check(name, cond, msg):
        nonlocal ok
        print(f'  {name} {"PASS" if cond else "FAIL"}: {msg}')
        ok = ok and cond

    # L1
    d0 = s0_root() - 2
    l1a, l1b = sl_roots(1)
    l2a, _ = sl_roots(2)
    d1, dp1, de2 = l1a - 2, l1b - 3, l2a - 3
    de50 = sl_roots(50)[0] - 51
    print(f'  z = 4e-6: d1 = {d1:.8e}, d0 = {d0:.8e}, delta_2 = {de2:.8e}, delta\'_1 = {dp1:.8e}, '
          f'delta_50 = {de50:.8e}')
    check('L1', abs(d1 - Decimal('3.3333305e-7')) < Decimal('1e-14') and abs(d0 - Decimal('1.3333327e-6')) < Decimal(
        '1e-13') and abs(de50 - Decimal('1.94137e-8')) < Decimal('1e-13') and de2 < d1 < dp1 < d0,
          'LD9\'s d1 and d0 and LD10\'s delta_50 reproduced; delta_2 < d1 < delta\'_1 < d0')

    # L2
    rec = e_ind((1,), lambda l: (1, 2))
    broad = e_ind((1, 2), lambda l: (1, 2))

    def show(xs):
        return ', '.join(f'{x:.6e}' if x < 1 else f'1 + {x - 1:.6e}' for x in xs)

    print("    E_ind below 2 (l <= 50), first five, LD9's reading: " + show(rec[:5]))
    print('    the broad reading: ' + show(broad[:5]))
    check('L2', [x for x in rec if x < 1] == [d1] and rec[1] == 1 + de2 and [x for x in broad if x < 1] == [d1, d0],
          f"below 1: d1 alone on LD9's reading (next 1 + delta_2), d1 and d0 on the broad one")
    ctl3 = e_ind((1, 2, 3), lambda l: (1, 2, 3))
    ctl = e_ind((1, 2), lambda l: (1, 2, l + 1))
    check('L2c', ctl3[0] == de2 and ctl[0] == de50,
          f'control: a class base 3 makes the least element delta_2 = {ctl3[0]:.6e}; b = l + 1 in harmonic l makes it '
          f'delta_50 = {ctl[0]:.6e}')

    # L3
    top = 1 + de50
    nxt = min(x for x in broad if x >= 1) - 1
    n1 = int(top / d1) + 1
    n2 = lattice_count(d1, d0, top)
    approx = top * top / (2 * d1 * d0)
    check('L3', nxt > de50 and n1 == lattice_count(d1, Decimal(10), top) and abs(n2 / approx - 1) < Decimal('1e-4'),
          f"every element in [1, 2) exceeds 1 + {nxt:.4e} > 1 + delta_50; per chain at most {n1} rounds on LD9's "
          f"reading, {n2} = {Decimal(n2):.5e} on the broad one (about 1/(2 d1 d0) = {approx:.5e})")

    # L4
    lvl3 = Decimal('0.5') / de50
    r1, r2 = n1 / lvl3, n2 / lvl3
    print(f'    per beta-level: level-3 rounds about (1/2)/eps_ind >= {lvl3:.5e}')
    check('L4', abs(r1 - 2 * de50 / d1) < Decimal('1e-6') and r1 < Decimal('0.117') and r2 > 40000,
          f'level-2 rounds per chain / level-3 rounds per level <= {r1:.5f} = 2 delta_50/d1 on LD9\'s reading '
          f'(smaller for smaller eps_ind), {r2:.5e} on the broad one; 1/(eps_K d1) > {1 / (de50 * d1):.5e}')

    print('  ALL PASS' if ok else '  FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
