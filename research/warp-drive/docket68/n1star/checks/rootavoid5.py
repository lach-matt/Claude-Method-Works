#!/usr/bin/env python3
"""rootavoid5: the two avoidances of finite sets of roots that CONSTANTS5.md R9.0 MAJOR 2 (c) left undecided, decided
at the weights of dweights5 W1 (INVERSE5-SCALAR.md part B). Labels: READ (cited lines, md5-pinned files), computed
(exact: rationals, integer congruences, sympy over Q), certified (interval enclosures, mpmath.iv at 200 bits, and
fixed-point integers with outward rounding), deduced (where said).

The conditions (read by content):
  (I)  I11:156-160 (III.I'''''''''' Definition 1.3) and I14:36-38 (Definition 1.1 (b)): a level beta in (3, 4 + eps_K]
       avoids the finite set of values for which beta - Re lambda_0, lambda_0 in Lambda, Re lambda_0 < 2, equals
       -Re mu for a root mu of L-hat_b0(0) or lies in Re pi_1 E_K (III.G' Lemma 1.3).
  (II) I9:290-291 (Step 3.4' at the levels below 3) and I14:124-126 (level 3 at the levels in (3, 4)), with I12:289-292
       for the two levels above 4: eps, eps' such that w and every 2 - alpha + j avoid the -mu (III.G'''' Proposition
       5.1's hypotheses: 2 - alpha + j != -mu for every j in N_0 and w != -mu, every root mu).
The parameters: eps = eps' = 10^-12, eps_ind = 1.9e-8, eps_K = 1.88e-8, eta_2 = eps_+ - 3 eps, the beta-chain beta_k =
alpha_1 + k s (s = 0.999 eps_K), k < K, and the top alpha = 4 + eps_K; the rounds tau_i = tau_0 + i (eps_ind - eps),
tau_0 = 2 + eps_ind - 2 eps (levels below 3), tau_i = tau_3 + i (eps_ind - eps), tau_3 = 1 + eta_2 - 2 eps (levels
above 3): all rational (dweights5.weights and counts, imported).

  R0 (READ) the cited lines, by content, in md5-pinned files; and the uses of Proposition 5.1's hypotheses in its
     proof (III.G'''' (5.3) for j = k_0, ..., floor(l_zf) only; (5.5) and Corollary 3.4 at the weight w).
  R1 (computed, exact) the weights and the chain: K, the levels below 3, in (3, 4), above 4.
  R2 (computed, exact) the rational indicial roots of L-hat_b0(0) (III.F' Proposition 2.3: -l, l + 2, the roots of
     box^Ups plus 1, of box^C minus 1). (a) box^Ups s0: lambda^2 - lambda - 2 - z has discriminant 9 + 4z, not a rational
     square. (b) box^Ups sl, l >= 1: Q_l(s) = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa has discriminant
     (z + 2)^2 + 4 kappa, a rational square iff m^2 - (2 q (l + 1))^2 = p^2 + 4 p q (z = p/q) has a solution: the
     divisor pairs of 1000001 = 101 x 9901 give l = 0 only, so no Q_l root (and no lambda with lambda (lambda - 1) a Q_l
     root) is rational for l >= 1. (c) box^C (damping5.polys, imported): the s0 quartic and the s1 sextic factor over Q
     with the one rational root 2 (Coulomb); the scalar sextic has no rational root for 2 <= l <= LC; the vector
     quadratic has a rational root exactly at the l with (l + 1)^2 + 250002000000 a square (divisor pairs of
     250002000000), all listed, every such root with |lambda| > 100. Physical and remaining box^Ups roots are integers.
  R3 (computed, certified) the finite root sets: every root with -mu in (-1, 4), by type, with enclosures: the
     integers 0, 1, 2, 3 and the class roots d0, d1, 1 + delta_2, 1 + delta'_1, 2 + delta_3, 2 + delta'_2, 3 + delta_4,
     3 + delta'_3 (irrational by R2 (a)-(b)); box^C contributes none (N1STAR-PROOF.md Proposition 10.44 (ii), READ: no
     box^C root has real part in [-100, 2] but the Coulomb root 2, which D removes at s0 and s1, lin5 E2).
  R4 (computed, exact; certified margins) (II) at the 53,244,734 levels below 3 and every tf round: w = beta - eps' -
     tau_i is never 0 (a linear congruence, no solution in range), never d0 or d1 (rational against irrational); its
     distance to the root set is at least the printed certified margin; 2 - alpha_i = 3 - tau_i lies in (0, 1), so 2 -
     alpha_i + j is never an integer, never a rational root of R2, never an irrational one.
  R5 (computed, exact; certified margins) (II) at the levels in (3, 4) and every level-3 round: w = beta - 2 - eps -
     tau_i in [-eps, 1), never 0, no root in [-eps, 0), never d0 or d1; 2 - tau_i in (0, 1). At the two levels above 4
     (I12 Step 4, alpha_tau = min(tau, 2 - delta), delta := (eps_ind - l_3 - 2 eps)/2 rational): w and 2 - alpha_tau in
     (0, 1), rational, so off every root; delta in (0, eps_ind), off {-mu - j}.
  R6 (computed, exact; certified margin) (I) at every level in (3, 4 + eps_K] and at alpha: on R9.1's reading of Lambda
     (Lambda below 2 = lambda_sharp + N_0 d1, lambdagen5 L1, md5-pinned), beta - lambda_0 = x with x in X := {-mu} u
     Re pi_1 E_K in (1, 2.4901 + eps_K] (eleven values) forces n d1 + theta in Q, theta the irrational part of x;
     d1 has degree 4 over Q, d0 and the delta's lie outside Q(d1) or meet no relation (sympy, exact), so only x = 2,
     n = 0 survives: beta = lambda_sharp + 2 = 3.5099, which is not a level (exact). The least distance of the levels
     from the set, certified: printed.
  R7 (computed, exact) Proposition 5.1's hypothesis as literally stated (every j, every root): the scalar box^C
     sextic, scaled to integer coefficients, is -64 lam^6 + c5 lam^5 + ..., c5 odd and free of kappa, so a rational
     root (any l) is an integer or = c5/64 = 49/64 mod 1 (rational root theorem, 2-adic valuations); the values
     2 - alpha in (1/64) Z are found by congruence and none has the fractional part 15/64 that -mu would need.
  R8 (computed, exact) the rest of I11:160's appended set (I12 section 1's exclusion set): l_zf not an integer; (4.2)
     at level 1; Lemma 4.2's interval. Not decided: (4.2) at level 2 (its tf-exponents are not listed).
  R9 (computed, exact) Definition 1.1 (a) at the levels (beta - 2 not the real part of a rate), not asked by R9 but
     decided by the same arithmetic: rational candidates not levels; irrational parts never rational (Q(d1) tests).
  R10 (computed, exact; certified margin) I9:55-58, the III.I'''''''' admissibility I11:157 assigns to the levels
     alpha < 3 (the round-10 verifier's gap): at every one of the 53,244,734 levels in (2, 3), alpha_1 = beta_0
     included, alpha - 2 != Re lambda - 1 and alpha - Re lambda not in {-Re mu} u Re pi_1 E_K for lambda in pi_1 M
     = lambda_sharp + N_0 d1 (R9.1's reading); the range alpha in (2, min(a_K, 3)) (a_K at the base from R10.1),
     Lemma 3.1's alpha_0 = alpha_1 < min(a_K, 2 + eps_ind, 5/2), and Lemma 3.2 Step 3's Proposition 5.1 at each level
     (I9:276-279: w = alpha - eps' - 2 + eps, 2 - alpha_P = eps).
  Negative controls (each mutates the computed path; each must fail): C1 a level planted at 3.5099 (R6 finds it);
  C2 eps' moved to make w = 0 at one (k, i) (R4's congruence finds it); C3 z = 7/2, where (z + 2)^2 + 12 = (13/2)^2
  (R2 (b) finds a rational class root at l = 1); C4 d1 replaced by a rational (R6's field argument fails: rational
  sums appear); C5 a root planted at a value w takes (R4's margin is 0); C6 the value 15/64 planted among the values
  2 - alpha (R7 finds the hit); C7 R9's field test on 2 d1 + 1/3 (it reports it); C8 a level below 3 planted at
  lambda_sharp + 1 (R10 finds it).

    python3 checks/rootavoid5.py [--selftest]      (some minutes; --selftest skips the R6 and R10 margin enumerations)
"""
import builtins
import contextlib
import hashlib
import io
import os
import sys
import textwrap
import time
from fractions import Fraction as Fr
from math import gcd, isqrt

import sympy as sp
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import dweights5 as DW           # noqa: E402  (weights, chain, d1 enclosure)
    import lambdagen5 as LG          # noqa: E402  (sl offsets, d0 enclosure)
    import damping5 as DP            # noqa: E402  (box^C indicial polynomials)

iv.prec = 200
OK = {}
P5 = os.path.join(ROOT, 'proof5')
PINS = {'PART-III-I9-COMMOTION.md': 'ac9ba304de45a96da478856a208681fb',
        'PART-III-I11-SPACETIME.md': '6e227bf7766fbe6b32949939b9235ed7',
        'PART-III-I14-LEVELS.md': 'd9a6893d2e57709d38ceae41b2b441ea',
        'PART-III-I12-SPECTRAL.md': '625e9374d22531b41c8e545dbac3427b',
        'PART-III-G5-TF.md': '52d411a185132b641f4097747aad1e41',
        'PART-III-F2-INDICIAL.md': 'db226a7608978c859d6c2003d3a35761',
        'PART-III-G2-IOTA.md': 'c5180a130c0c0ac4aa166d1fde8c405c',
        'PART-III-I10-CORR4.md': '491774f9b522ad1d1f188819b09b2a40'}
LG_OUT_MD5 = '03645ae643b694197578381ea7614063'
ANCHORS = [('PART-III-I11-SPACETIME.md', 156, 160, ['avoids the finite set of values for which',
                                                    r'\mathrm{Re}\,\pi_1\mathcal E_K']),
           ('PART-III-I14-LEVELS.md', 36, 38, ['avoids the finite set of III.I', r'\mathrm{Re}\,\pi_1\mathcal E_K']),
           ('PART-III-I9-COMMOTION.md', 290, 291, ['avoid the discrete set of the $-\\mu$']),
           ('PART-III-I9-COMMOTION.md', 55, 58, [r'*Admissible levels.* $\alpha\in(2,\min(a_K,3))$ is admissible if',
                                                r'$\lambda\in\pi_1\mathcal M$ and every root $\mu$ of III.G']),
           ('PART-III-I11-SPACETIME.md', 156, 157, [r'for $\alpha<3$, it is admissible in the sense of III.I']),
           ('PART-III-I14-LEVELS.md', 124, 126, [r'its conditions $w\ne-\mu$, $2-\tau+j\ne-\mu$ hold for $\epsilon$']),
           ('PART-III-I12-SPECTRAL.md', 289, 292, [r'$\alpha_\tau := \min(\tau,2-\delta)', r'$\{-\mu-j\}$']),
           ('PART-III-G5-TF.md', 624, 627, [r'with $2-\alpha+j\ne-\mu$ and $w\ne-\mu$ for']),
           ('PART-III-G5-TF.md', 655, 659, [r'For $j = k_0,k_0+1,\ldots,\lfloor\ell_{\mathrm{zf}}\rfloor$ in turn',
                                            r'$2-\alpha+j\ne-\mu$, the roots being real']),
           ('PART-III-F2-INDICIAL.md', 104, 122, [r'$\lambda^C_{\mathrm sl,\ll,j}-1$', r'tl, $l\ge2$: $-l$; $l+2$']),
           ('PART-III-G2-IOTA.md', 104, 108, [r'$\lambda^\Upsilon_{\mathrm s0,2}-2\in(0,\frac{z_\Upsilon}3]$']),
           ('PART-III-I10-CORR4.md', 74, 75, [r'$d_{\mathrm c0} := -\mu_{\mathrm c0}$'])]
LC = 120                       # the scalar box^C sextic is factored over Q for 2 <= l <= LC
FIX = 2 ** 160                 # fixed-point scale for the certified margins


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def r0():
    ok = True
    for f, pin in PINS.items():
        m = hashlib.md5(open(os.path.join(P5, f), 'rb').read()).hexdigest()
        ok = ok and m == pin
    for f, a, b, keys in ANCHORS:
        txt = ' '.join(open(os.path.join(P5, f), encoding='utf-8').read().split('\n')[a - 1:b])
        txt = ' '.join(txt.split())
        for kk in keys:
            ok = ok and (' '.join(kk.split()) in txt)
    lg = open(os.path.join(HERE, 'lambdagen5.out'), encoding='utf-8').read()
    ok = ok and hashlib.md5(lg.encode('utf-8')).hexdigest() == LG_OUT_MD5
    ok = ok and 'lambda_sharp + N_0 Inc' in ' '.join(lg.split())
    return ok


# ------------------------------------------------------------------------------------------------ R1 the chain
def chain(w=None):
    if w is None:
        w = DW.weights(Fr(19, 10 ** 9), Fr(189, 10 ** 10), Fr(188, 10 ** 10), Fr(1, 10 ** 12))
    keys = ('alpha', 'alpha1', 's', 'tau0', 'tau3', 'step', 'epsp', 'eps', 'eps_ind')
    D = 1
    for kk in keys:
        D = D * w[kk].denominator // gcd(D, w[kk].denominator)
    I = {kk: int(w[kk] * D) for kk in keys}
    assert all(Fr(I[kk], D) == w[kk] for kk in keys)
    K = -(-(I['alpha'] - I['alpha1']) // I['s'])
    k3 = (3 * D - I['alpha1']) // I['s'] + 1
    k4 = (4 * D - I['alpha1']) // I['s'] + 1
    return dict(w=w, D=D, I=I, K=K, k3=k3, k4=k4)


def beta(C, k):
    return C['I']['alpha1'] + k * C['I']['s'] if k < C['K'] else C['I']['alpha']


# ------------------------------------------------------------------------------------------------ R2 rational roots
def is_rat_square(q):
    q = Fr(q)
    if q < 0:
        return False
    a, b = q.numerator, q.denominator
    return isqrt(a) ** 2 == a and isqrt(b) ** 2 == b


def divisor_pairs(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append((d, n // d))
        d += 1
    return out


def ups_rational_l(z):
    """the l >= 0 at which (z + 2)^2 + 4 l (l + 2) is a rational square: m^2 - (2 q (l + 1))^2 = p^2 + 4 p q"""
    p, q = z.numerator, z.denominator
    N = p * p + 4 * p * q
    ls = []
    for d, e in divisor_pairs(N):
        if (e - d) % 2 == 0:
            A = (e - d) // 2
            if A % (2 * q) == 0 and A // (2 * q) >= 1:
                ls.append(A // (2 * q) - 1)
    return sorted(set(ls))


def factor_divisor_pairs(n):
    """divisor pairs of n through its factorisation (n up to ~1e12)"""
    f = sp.factorint(n)
    divs = [1]
    for pr, e in f.items():
        divs = [d * pr ** k for d in divs for k in range(e + 1)]
    return sorted((d, n // d) for d in divs if d * d <= n)


def boxC_point():
    return {DP.h: sp.Rational(1, 10 ** 6), DP.e: sp.Rational(1, 102400), DP.v: sp.Rational(1, 2)}


def rational_roots(P, x):
    out = []
    for fac, _m in sp.factor_list(sp.Poly(P, x, domain='QQ'))[1]:
        if fac.degree() == 1:
            cf = fac.all_coeffs()
            out.append(sp.Rational(-cf[1], cf[0]))
    return out


def r2(z=Fr(4, 10 ** 6), polys=None):
    res = {}
    res['s0_disc_square'] = is_rat_square(9 + 4 * z)
    res['Q_rational_l'] = ups_rational_l(z)
    pk, p0, pv = polys
    pt = boxC_point()
    lam = DP.lam
    res['C_s0'] = rational_roots(sp.expand(p0.subs(pt)), lam)
    res['C_s1'] = rational_roots(sp.expand(pk.subs(pt).subs(DP.K, 3)), lam)
    sl = {}
    for lv in range(2, LC + 1):
        rr = rational_roots(sp.expand(pk.subs(pt).subs(DP.K, lv * (lv + 2))), lam)
        if rr:
            sl[lv] = rr
    res['C_sl'] = sl
    # vector quadratic: -h lam^2 + (2h - 2v) lam + h kappa + 6v; disc/(4 h^2) = (l + 1)^2 + 250002000000
    h, v = Fr(1, 10 ** 6), Fr(1, 2)
    c0 = (h - v) ** 2 / h ** 2 + 6 * v / h - 1
    assert c0.denominator == 1
    c0 = int(c0)
    vec = []
    for d, e in factor_divisor_pairs(c0):
        if (e - d) % 2 == 0 and (e - d) // 2 >= 2:
            lv = (e - d) // 2 - 1
            m = (e + d) // 2
            kap = lv * (lv + 2)
            for sg in (1, -1):
                root = ((2 * h - 2 * v) + sg * 2 * h * m) / (2 * h)
                assert -h * root ** 2 + (2 * h - 2 * v) * root + h * kap + 6 * v == 0
                vec.append((lv, root))
    res['C_vec'] = vec
    res['c0'] = c0
    return res


# ------------------------------------------------------------------------------------------------ R3 window roots
def window_roots():
    """every root mu with -mu in (-1, 4): (name, types, lo, hi) as Fractions; integers exact"""
    d1lo, d1hi = DW.d1_interval()
    d0lo, d0hi = LG.frpair(LG.d0_iv())
    out = [('0', 's0 (time translation), s2 (2 - l)', Fr(0), Fr(0)),
           ('1', 's1, v1 (-1); s3 (2 - l); v2 (1 - l)', Fr(1), Fr(1)),
           ('2', 's2, v2, t2 (-l); s4 (2 - l); v3 (1 - l)', Fr(2), Fr(2)),
           ('3', 's3, v3, t3 (-l); s5; v4', Fr(3), Fr(3)),
           ('d1', 's1 (2 - lambda_s1,2)', d1lo, d1hi), ('d0', 's0 (2 - lambda_s0,2)', d0lo, d0hi)]
    for lv, (nm, j) in ((1, ("1 + delta'_1", 1)), (2, ('1 + delta_2', 0)), (2, ("2 + delta'_2", 1)),
                        (3, ('2 + delta_3', 0)), (3, ("3 + delta'_3", 1)), (4, ('3 + delta_4', 0))):
        lo, hi = LG.frpair(LG.sl_offsets_iv(lv)[j])
        base = (lv - 1) if j == 0 else lv
        out.append((nm, 's%d (2 - lambda_s%d,%d)' % (lv, lv, lv + 1 + j), base + lo, base + hi))
    return out


# ------------------------------------------------------------------------------------------------ R4, R5 congruences
def congruence_hits(A, s, st, klo, khi):
    """the k in [klo, khi] with A + k s = 0 mod st (A + k s >= 0 there)"""
    g = gcd(s, st)
    if A % g:
        return []
    m = st // g
    k0 = (-(A // g) * pow(s // g, -1, m)) % m
    first = klo + ((k0 - klo) % m)
    return list(range(first, khi + 1, m))[:5]


def residue_min(A, s, st, klo, khi):
    """min over k in [klo, khi] of (A + k s) mod st, and whether the range covers a full cycle"""
    g = gcd(s, st)
    m = st // g
    full = khi - klo + 1 >= m
    if full:
        return A % g, True, g
    return min((A + k * s) % st for k in range(klo, khi + 1)), False, g


def lattice_dist(x_lo, x_hi, a, g):
    """certified lower bound for the distance from [x_lo, x_hi] (Fractions) to a + g Z"""
    n = (x_lo - a) // g
    cands = [a + (n + t) * g for t in (-1, 0, 1, 2)]
    best = None
    for c_ in cands:
        if x_lo <= c_ <= x_hi:
            return Fr(0)
        dd = min(abs(c_ - x_lo), abs(c_ - x_hi))
        best = dd if best is None else min(best, dd)
    return best


def r4(C, roots, plant=None):
    D, I = C['D'], C['I']
    s, st = I['s'], I['step']
    A2 = I['alpha1'] - I['epsp'] - I['tau0']
    kB = max(0, -(A2 // s))
    klo, khi = kB, C['k3'] - 1
    hits = congruence_hits(A2, s, st, klo, khi)
    rmin, full, g = residue_min(A2, s, st, klo, khi)
    margins = {}
    for nm, _t, lo, hi in roots:
        if plant is not None and nm == 'd0':
            lo = hi = plant
        flo, fhi = Fr(lo) * D, Fr(hi) * D
        if not (0 <= fhi and flo < D):
            continue
        if lo == hi and Fr(lo).denominator == 1:
            margins[nm] = Fr(rmin, D) if int(lo) == 0 else None
            continue
        margins[nm] = lattice_dist(flo, fhi, A2 % g, g) / D
    tau_in = Fr(I['tau0'], D) > 2 and Fr(beta(C, khi) - I['epsp'], D) < 3
    return dict(hits=hits, rmin=Fr(rmin, D), full=full, g=g, margins=margins, A=A2, klo=klo, khi=khi,
                tau_in=tau_in)


def r5(C, roots):
    D, I = C['D'], C['I']
    s, st = I['s'], I['step']
    A3 = I['alpha1'] - 2 * D - I['eps'] - I['tau3']
    A3c = I['alpha1'] - 2 * D - I['tau3']                 # the round condition tau_i <= beta - 2
    klo = max(C['k3'], -(A3c // s))
    khi = C['k4'] - 1                                      # beta < 4
    hits = congruence_hits(A3, s, st, klo, khi)
    _r, full, g = residue_min(A3 % st, s, st, klo, khi)
    rmin = lattice_dist(Fr(0), Fr(0), A3 % g, g)            # w may be negative (down to -eps): both sides
    margins = {}
    for nm, _t, lo, hi in roots:
        flo, fhi = Fr(lo) * D, Fr(hi) * D
        if not (-I['eps'] <= fhi and flo < D):
            continue
        if lo == hi and Fr(lo).denominator == 1:
            margins[nm] = None if int(lo) != 0 else 'exact'
            continue
        margins[nm] = lattice_dist(flo, fhi, A3 % g, g) / D
    top = []
    for k in range(C['k4'], C['K'] + 1):
        b = Fr(beta(C, k), D)
        l3 = b - 4 - Fr(I['eps'], D)
        dl = (Fr(I['eps_ind'], D) - l3 - 2 * Fr(I['eps'], D)) / 2
        top.append((k, b, l3, dl, dl > 0 and dl < Fr(I['eps_ind'], D)))
    return dict(hits=hits, rmin=rmin / D, full=full, g=g, margins=margins, klo=klo, khi=khi, top=top)


# ------------------------------------------------------------------------------------------------ R6 Lambda
def algebraic_numbers():
    z = sp.Rational(4, 10 ** 6)
    D1 = z ** 2 + 4 * z + 16
    lam12 = (1 + sp.sqrt(17 + 2 * z - 2 * sp.sqrt(D1))) / 2               # lambda^Ups_s1,2
    d0 = (1 + sp.sqrt(9 + 4 * z)) / 2 - 2

    def sl(lv, j):
        k = lv * (lv + 2)
        b, c_ = 2 + 2 * k + z, k * (k + 1) + z * k
        disc = sp.sqrt(b * b - 4 * c_)
        s_ = (b - disc) / 2 if j == 0 else (b + disc) / 2
        return sp.Rational(1, 2) + sp.sqrt(sp.Rational(1, 4) + s_) - (lv + 1 + j)
    return lam12, d0, sl


def field_tests(fake_d1=None):
    """for each irrational offset theta of X: whether n d1 + theta is rational for some n >= 0 (exact, over Q(d1))"""
    lam12, d0, sl = algebraic_numbers()
    x = sp.Symbol('x')
    mp = sp.minimal_polynomial(lam12, x)
    deg = sp.degree(mp, x)
    thetas = [('d0', d0), ('d1', lam12 - 2), ("delta'_1", sl(1, 1)), ('delta_2', sl(2, 0)), ("delta'_2", sl(2, 1)),
              ('delta_3', sl(3, 0))]
    try:
        pos = sp.polys.numberfields.subfield.to_number_field(3 * (lam12 - 2) + sp.Rational(1, 7), lam12).coeffs()
        pos = [sp.Rational(q) for q in pos][::-1][:2] == [sp.Rational(1, 7) - 6, 3]
    except sp.polys.polyerrors.IsomorphismFailed:
        pos = False
    out = []
    for nm, th in thetas:
        if fake_d1 is not None:
            out.append((nm, 'd1 rational: n d1 + theta rational for theta = d1 at every n', True))
            continue
        if nm == 'd1':
            out.append((nm, '(n + 1) d1 irrational (deg %d)' % deg, False))
            continue
        try:
            coords = sp.polys.numberfields.subfield.to_number_field(th, lam12).coeffs()
        except sp.polys.polyerrors.IsomorphismFailed:
            out.append((nm, 'not in Q(d1)', False))
            continue
        # theta = sum_i c_i lam12^i (highest first); n d1 + theta rational iff its non-constant part vanishes
        cs = [sp.Rational(q) for q in coords][::-1] + [0] * 4
        bad = (cs[2] == 0 and cs[3] == 0 and cs[1] <= 0 and cs[1].q == 1)
        out.append((nm, 'in Q(d1), coordinates %s' % [str(q) for q in cs[:4]], bad))
    return deg, mp, out, pos


def X_set():
    """the values x = -mu or x in Re pi_1 E_K with x in (1, 2.4901 + eps_K]: (name, integer part, offset name)"""
    return [('2', 2, None), ('1 + d0', 1, 'd0'), ('2 + d0', 2, 'd0'), ('1 + d1', 1, 'd1'), ('2 + d1', 2, 'd1'),
            ("1 + delta'_1", 1, "delta'_1"), ("2 + delta'_1", 2, "delta'_1"), ('1 + delta_2', 1, 'delta_2'),
            ('2 + delta_2', 2, 'delta_2'), ("2 + delta'_2", 2, "delta'_2"), ('2 + delta_3', 2, 'delta_3')]


def offset_iv(nm):
    if nm is None:
        return Fr(0), Fr(0)
    if nm == 'd1':
        return DW.d1_interval()
    if nm == 'd0':
        return LG.frpair(LG.d0_iv())
    lv = int(nm[-1])
    j = 1 if "'" in nm else 0
    return LG.frpair(LG.sl_offsets_iv(lv)[j])


def r6_exact(C, plant_level=None):
    """the only rational candidate is beta = lambda_sharp + 2; is it a level?"""
    D, I = C['D'], C['I']
    cand = DW.LSHARP + 2
    v = cand * D
    hit = False
    if v.denominator == 1:
        v = int(v)
        a1 = I['alpha1'] if plant_level is None else int(plant_level * D) - (C['k3'] + 7) * I['s']
        hit = (v - a1) % I['s'] == 0 and C['k3'] <= (v - a1) // I['s'] < C['K']
        hit = hit or v == I['alpha']
    return cand, hit


def r6_margin(C):
    """certified least distance from the levels in (3, 4 + eps_K] (and alpha) to lambda_sharp + n d1 + x"""
    D, I = C['D'], C['I']
    s = I['s'] * FIX
    a1 = I['alpha1'] * FIX
    lo_lev, hi_lev = beta(C, C['k3']) * FIX, I['alpha'] * FIX
    top = I['alpha'] * FIX
    d1lo, d1hi = DW.d1_interval()
    dlo = (d1lo * D * FIX).__floor__()
    dhi = -((-d1hi * D * FIX).__floor__())
    N = int((2 - DW.LSHARP) / d1lo) + 1
    best = None
    where = None
    for xn, ip, off in X_set():
        olo, ohi = offset_iv(off)
        clo = ((DW.LSHARP + ip + olo) * D * FIX).__floor__()
        chi = -((-(DW.LSHARP + ip + ohi) * D * FIX).__floor__())
        plo, phi = clo, chi
        for n in range(N + 1):
            if n:
                plo += dlo
                phi += dhi
            if Fr(plo, D * FIX) - DW.LSHARP - ip - olo >= 2 - DW.LSHARP:
                break
            if phi < lo_lev - s or plo > hi_lev + s:
                continue
            kk = (plo - a1) // s
            dist = None
            for k in (kk - 1, kk, kk + 1, kk + 2):
                if C['k3'] <= k < C['K']:
                    b = a1 + k * s
                    d_ = 0 if plo <= b <= phi else min(abs(b - plo), abs(b - phi))
                    dist = d_ if dist is None else min(dist, d_)
            d_ = 0 if plo <= top <= phi else min(abs(top - plo), abs(top - phi))
            dist = d_ if dist is None else min(dist, d_)
            if best is None or dist < best:
                best, where = dist, (xn, n)
    return Fr(best, D * FIX), where, N


def r7(C, polys):
    """the literal reading. The scalar box^C sextic at the point, scaled to integer coefficients, is
    -64 lam^6 + c5 lam^5 + c4(kappa) lam^4 + ... with c5 an odd constant: by the rational root theorem a rational root
    has denominator 2^a, a <= 6; for 1 <= a <= 5 the term lam^5 alone has the least 2-adic valuation (so no root), and
    for a = 6 the numerator is = c5 mod 64. So every rational root is an integer or = c5/64 mod 1, at every l. The
    values 2 - alpha of I9, I14 and I12 in (1/64) Z are listed exactly; a hit needs 1 - (2 - alpha) = c5/64 mod 1."""
    D, I = C['D'], C['I']
    pk = polys[0]
    lam, K = DP.lam, DP.K
    Q = sp.Poly(sp.expand(pk.subs(boxC_point())), lam)
    cs = Q.all_coeffs()
    den = sp.ilcm(*[sp.Rational(c_).q for cc in cs for c_ in sp.Poly(cc, K).all_coeffs()])
    csi = [sp.Poly(sp.expand(cc * den), K) for cc in cs]
    lead = csi[0].all_coeffs()
    c5 = csi[1].all_coeffs()
    struct = len(lead) == 1 and int(lead[0]) == -64 and len(c5) == 1 and int(c5[0]) % 2 == 1
    c5 = int(c5[0])
    frac_only = Fr(c5 % 64, 64)                       # the one non-integer fractional part a rational root can have
    q = 64
    assert D % q == 0
    M = D // q
    st = I['step']
    imax2 = (beta(C, C['k3'] - 1) - I['epsp'] - I['tau0']) // st
    imax3 = (I['alpha'] - 2 * D - I['tau3']) // st
    vals = []
    for nm, A, imax in (('3 - tau_i', 3 * D - I['tau0'], imax2), ('2 - tau_i', 2 * D - I['tau3'], imax3)):
        g = gcd(st, M)
        if A % g == 0:
            m = M // g
            i = ((A // g) * pow(st // g, -1, m)) % m
            while i <= imax:
                vals.append((nm, i, Fr(A - i * st, D)))
                i += m
    deltas = []
    for k in range(C['k4'], C['K'] + 1):
        l3 = Fr(beta(C, k), D) - 4 - Fr(I['eps'], D)
        deltas.append((Fr(I['eps_ind'], D) - l3 - 2 * Fr(I['eps'], D)) / 2)
    okd = all(0 < q * d < 1 for d in deltas)
    hits = [(nm, i, v) for nm, i, v in vals if (1 - v) % 1 == frac_only]
    return dict(ok=struct and not hits and okd, den=sp.factorint(den), lead=-64, c5=c5, frac=frac_only, q=q,
                imax2=imax2, imax3=imax3, vals=vals, hits=hits, deltas=deltas)


def r8(C):
    """l_zf not an integer at levels 1-3; (4.2) at level 1 with alpha_0 = 2; Lemma 4.2's interval at level 3"""
    D, I = C['D'], C['I']
    s = I['s']
    A = I['alpha1'] - I['eps']                     # beta_k - eps = (A + k s)/D
    hits = congruence_hits(A, s, D, 0, C['K'] - 1)
    top_int = (I['alpha'] - I['eps']) % D == 0
    ok = not hits and not top_int
    return dict(ok=ok, hits=hits + (['alpha'] if top_int else []))


def r9(C):
    """Definition 1.1 (a) at every level in (3, 4 + eps_K]: beta - 2 is not the real part of a rate (lambda - 1 at s1,
    lambda at s0, s2, v1, lambda + d0 and lambda + d1 at c0, c1; lambda in Lambda; I10 section 1). On R9.1's reading
    Lambda in (1, 3 + eps_K] is: the rational points R (lambda_sharp, 2, 3 and the least E^C_I's points, closed under
    + 1), each plus n d1, plus at most one offset theta1 in {d0} u {delta_l, delta'_l} (the E_col bases and the
    once-usable increments 1 + d0, 1 + delta_2, 1 + delta'_1); a c-rate adds d0 or d1. A rate is rational only if
    n d1 + theta1 + theta2 is, theta2 in {0, d0, d1}: the field tests exclude it unless theta1 = theta2 = 0 and n = 0
    (exact); the rational candidates for beta are then lambda + 2 and lambda + 1 (s1) for lambda in R."""
    D, I = C['D'], C['I']
    eK = C['w']['eps_K']
    with contextlib.redirect_stdout(io.StringIO()):
        import prop31loss5 as P31
    eci = sorted(z for z in P31.least_ECI() if z <= 4)
    R = set([DW.LSHARP, Fr(2), Fr(3)] + eci)
    for _ in range(3):
        R |= {x + 1 for x in R if x + 1 <= 4}
    cands = sorted({x + 2 for x in R if 1 < x <= 2 + eK} | {x + 1 for x in R if 2 < x <= 3 + eK})
    hits = []
    for b in cands:
        v = b * D
        if v.denominator != 1:
            continue
        v = int(v)
        k = (v - I['alpha1']) // I['s']
        if ((v - I['alpha1']) % I['s'] == 0 and C['k3'] <= k < C['K']) or v == I['alpha']:
            hits.append(b)
    lam12, d0, sl = algebraic_numbers()
    offs = [('d0', d0)] + [('delta_%d' % lv, sl(lv, 0)) for lv in range(2, 7)] + \
           [("delta'_%d" % lv, sl(lv, 1)) for lv in range(1, 6)]
    bad = []
    for nm1, t1 in offs:
        for nm2, t2 in (('0', 0), ('d0', d0)):
            try:
                sp.polys.numberfields.subfield.to_number_field(t1 + t2, lam12)
                bad.append((nm1, nm2))
            except sp.polys.polyerrors.IsomorphismFailed:
                pass
    return dict(ok=not hits and not bad, cands=cands, hits=hits, bad=bad, ntests=2 * len(offs), eci=len(eci))


def X9_set():
    """I9:55-58 at a level alpha in (2, 3): x = alpha - lambda, lambda in pi_1 M = lambda_sharp + N_0 d1 (Re < 2), lies
    in (0, 3 - lambda_sharp) = (0, 1.4901); there the roots -mu (R3) and Re pi_1 E_K give seven values; the first
    clause, alpha - 2 != lambda - 1, is x = 1"""
    return [('1', 1, None), ('d0', 0, 'd0'), ('d1', 0, 'd1'), ('1 + d0', 1, 'd0'), ('1 + d1', 1, 'd1'),
            ("1 + delta'_1", 1, "delta'_1"), ('1 + delta_2', 1, 'delta_2')]


def levels_margin(C, X, klo, khi, top=True):
    """certified least distance from the levels beta_k, klo <= k <= khi (and alpha if top), to lambda_sharp + n d1 + x,
    x in X, lambda_sharp + n d1 < 2 (fixed-point integers at 1/(D FIX), d1's enclosure rounded outward)"""
    D, I = C['D'], C['I']
    s = I['s'] * FIX
    a1 = I['alpha1'] * FIX
    lo_lev, hi_lev = beta(C, klo) * FIX, (I['alpha'] if top else beta(C, khi)) * FIX
    tp = I['alpha'] * FIX
    d1lo, d1hi = DW.d1_interval()
    dlo = (d1lo * D * FIX).__floor__()
    dhi = -((-d1hi * D * FIX).__floor__())
    N = int((2 - DW.LSHARP) / d1lo) + 1
    best, where = None, None
    for xn, ip, off in X:
        olo, ohi = offset_iv(off)
        plo = ((DW.LSHARP + ip + olo) * D * FIX).__floor__()
        phi = -((-(DW.LSHARP + ip + ohi) * D * FIX).__floor__())
        for n in range(N + 1):
            if n:
                plo += dlo
                phi += dhi
            if Fr(plo, D * FIX) - DW.LSHARP - ip - olo >= 2 - DW.LSHARP:
                break
            if phi < lo_lev - s or plo > hi_lev + s:
                continue
            kk = (plo - a1) // s
            dist = None
            for k in (kk - 1, kk, kk + 1, kk + 2):
                if klo <= k <= khi:
                    b = a1 + k * s
                    d_ = 0 if plo <= b <= phi else min(abs(b - plo), abs(b - phi))
                    dist = d_ if dist is None else min(dist, d_)
            if top:
                d_ = 0 if plo <= tp <= phi else min(abs(tp - plo), abs(tp - phi))
                dist = d_ if dist is None else min(dist, d_)
            if dist is not None and (best is None or dist < best):
                best, where = dist, (xn, n)
    return Fr(best, D * FIX), where, N


def r10(C, plant=None):
    """I9:55-58 (III.I'''''''' admissibility) at every level below 3, alpha_1 = beta_0 included: alpha in (2, min(a_K,
    3)); alpha - 2 != Re lambda - 1 and alpha - Re lambda not in {-Re mu} u Re pi_1 E_K, lambda in pi_1 M. Exact: the
    only rational candidate is lambda_sharp + 1 (x = 1, n = 0); the irrational offsets d0, d1, delta'_1, delta_2 are
    R6's field tests. Also the range: alpha_1 < a_K at the base (R10.1's a_K - 2 = (1 - 10^-9) eps_K)."""
    D, I = C['D'], C['I']
    cand = DW.LSHARP + 1
    v = cand * D
    a1 = I['alpha1'] if plant is None else int(plant * D) - 1234 * I['s']
    hit = v.denominator == 1 and (int(v) - a1) % I['s'] == 0 and 0 <= (int(v) - a1) // I['s'] < C['k3']
    eK = C['w']['eps_K']
    aK_base = 2 + (1 - Fr(1, 10 ** 9)) * eK
    a1f = Fr(I['alpha1'], D)
    # Lemma 3.1 (I9:201): alpha_0 = alpha_1 in (2, min(a_K, 2 + eps_ind, 5/2))
    rng = (2 < a1f < min(aK_base, 2 + Fr(I['eps_ind'], D), Fr(5, 2)) and Fr(beta(C, C['k3'] - 1), D) < 3)
    # Lemma 3.2 Step 3 (I9:276-279): Proposition 5.1 with alpha_K = alpha - eps', l_zf = alpha_K - 2, w = alpha_K - 2
    # + eps, its alpha 2 - eps: w and l_zf in (0, 1) and rational, 2 - alpha_P = eps in (0, d1), d1 the least positive
    # root: off every root (Lemma B.1), l_zf not in N_0
    eps, epsp = Fr(I['eps'], D), Fr(I['epsp'], D)
    d1lo = DW.d1_interval()[0]
    lo_w = Fr(beta(C, 0), D) - epsp - 2 + eps
    hi_w = Fr(beta(C, C['k3'] - 1), D) - epsp - 2 + eps
    step3 = 0 < lo_w and hi_w < 1 and 0 < eps < d1lo and 0 < Fr(beta(C, 0), D) - epsp - 2
    return dict(cand=cand, hit=hit, rng=rng, aK=aK_base, step3=step3, w=(lo_w, hi_w))


# ------------------------------------------------------------------------------------------------ main
def main(selftest=False):
    t0 = time.time()
    print('rootavoid5: the avoidances of I11:156-160 and of I9:290-291 / I14:124-126, at dweights5 W1\'s weights')
    OK['R0'] = r0()
    print('  R0 (READ): the cited lines carry the conditions (by content), the files are md5-pinned, Proposition 5.1\'s '
          'proof uses 2 - alpha + j != -mu only for j = k_0, ..., floor(l_zf) ((5.3)) and w != -mu ((5.5)); '
          'lambdagen5.out L1 (pinned): Lambda below 3.0198 is lambda_sharp + N_0 Inc: %s' % OK['R0'])
    C = chain()
    D, I = C['D'], C['I']
    OK['R1'] = (C['K'] == 106489469 and C['k3'] == 53244734 and Fr(beta(C, C['k4'] - 1), D) < 4 < Fr(beta(C, C['k4']), D)
                and C['K'] - C['k4'] + 1 == 2)
    print('  R1 (exact): D = %d; K = %d steps, %d levels below 3, %d in (3, 4), %d above 4 (beta_%d and alpha); '
          's = %s, tau step = %s: %s' % (D, C['K'], C['k3'], C['k4'] - C['k3'], C['K'] - C['k4'] + 1, C['K'] - 1,
                                         C['w']['s'], C['w']['step'], OK['R1']))
    print('      (computing the box^C indicial polynomials, damping5.polys, about half a minute)')
    polys = DP.polys(4, sp.Rational(2, 3))
    R2 = r2(polys=polys)
    vec_ni = [(lv, rt) for lv, rt in R2['C_vec'] if rt.denominator != 1]
    vec_ok = all(abs(rt) > 100 for _l, rt in vec_ni)
    OK['R2'] = (not R2['s0_disc_square'] and R2['Q_rational_l'] == [0] and R2['C_s0'] == [2] and R2['C_s1'] == [2]
                and R2['C_sl'] == {} and vec_ok)
    vl = sorted(set(lv for lv, _ in R2['C_vec']))
    print('  R2 (exact): 9 + 4z = %s not a rational square: %s; (z + 2)^2 + 4 l (l + 2) a rational square only at l in '
          '%s (divisor pairs of p^2 + 4pq = %d = %s); box^C rational roots: s0 quartic %s, s1 sextic %s, scalar sextic '
          'at 2 <= l <= %d: %s; vector quadratic ((l + 1)^2 + %d a square): %d values of l, %d rational roots, %d not '
          'integers (the least |lambda| of those: %s; every one above 100: %s); all other roots of III.F\' '
          'Proposition 2.3 are integers: %s' % (
              9 + 4 * DW.Z, not R2['s0_disc_square'], R2['Q_rational_l'], DW.Z.numerator ** 2 + 4 * DW.Z.numerator
              * DW.Z.denominator, sp.factorint(DW.Z.numerator ** 2 + 4 * DW.Z.numerator * DW.Z.denominator),
              R2['C_s0'], R2['C_s1'], LC, R2['C_sl'] or 'none', R2['c0'], len(vl), len(R2['C_vec']), len(vec_ni),
              min((abs(rt) for _l, rt in vec_ni), default='none'), vec_ok, OK['R2']))
    print('      the vector-type l with rational box^C roots (first ten): %s' % vl[:10])
    roots = window_roots()
    OK['R3'] = len(roots) == 12 and all(0 < (hi - lo) < Fr(1, 10 ** 40) or lo == hi for _n, _t, lo, hi in roots)
    print('  R3 (certified): the roots with -mu in (-1, 4) (box^C none: Proposition 10.44 (ii), READ): %s: %s' % (
        '; '.join('%s = %s [%s]' % (nm, ('%.12g' % float(lo)) if lo != hi else lo, ty) for nm, ty, lo, hi in roots),
        OK['R3']))
    R4 = r4(C, roots)
    m4 = {k: v for k, v in R4['margins'].items() if v is not None}
    OK['R4'] = not R4['hits'] and R4['full'] and R4['rmin'] > 0 and all(
        v > 0 for v in m4.values()) and R4['tau_in']
    print('  R4 (exact): levels below 3 with rounds: k in [%d, %d]; w = beta_k - eps\' - tau_i = 0 has no solution '
          '(the congruence A + k s = 0 mod step: gcd(s, step) = %d does not divide A: hits %s); w >= %s = %.4e on every '
          '(k, i) (the residues cover a full cycle: %s); certified distance of w to d0: %.4e, to d1: %.4e; tau_i in '
          '(2, 3), so 2 - alpha_i = 3 - tau_i in (0, 1) is no integer and, rational, no irrational root: %s' % (
              R4['klo'], R4['khi'], R4['g'], R4['hits'], R4['rmin'], float(R4['rmin']), R4['full'],
              float(m4.get('d0', -1)), float(m4.get('d1', -1)), OK['R4']))
    R5 = r5(C, roots)
    m5 = {k: v for k, v in R5['margins'].items() if v not in (None, 'exact')}
    OK['R5'] = (not R5['hits'] and R5['full'] and R5['rmin'] > 0 and all(v > 0 for v in m5.values())
                and all(t[-1] for t in R5['top']))
    print('  R5 (exact): levels in (3, 4) with rounds: k in [%d, %d]; w = beta - 2 - eps - tau_i in [-eps, 1): w = 0 '
          'has no solution (hits %s); |w| >= %.4e (no root in [-eps, 0), R3); distance to d0 %.4e, to d1 %.4e; '
          '2 - tau_i in (0, 1); the two levels above 4: %s, each with delta = (eps_ind - l_3 - 2 eps)/2 in (0, '
          'eps_ind) rational, w and 2 - alpha_tau rational in (0, 1): off every root: %s' % (
              R5['klo'], R5['khi'], R5['hits'], float(R5['rmin']), float(m5.get('d0', -1)), float(m5.get('d1', -1)),
              ['beta_%d: l_3 = %.4e, delta = %.4e' % (k, float(l3), float(dl)) for k, _b, l3, dl, _o in R5['top']],
              OK['R5']))
    deg, mp, ft, pos = field_tests()
    cand, hit = r6_exact(C)
    OK['R6'] = deg == 4 and not any(b for _n, _s, b in ft) and not hit and pos
    print('  R6 (exact): d1 = lambda_s1,2 - 2, lambda_s1,2 of degree %d over Q (minimal polynomial %s); for each '
          'irrational offset theta of X, n d1 + theta in Q for some n >= 0: %s; so the only rational candidate is '
          'beta = lambda_sharp + 2 = %s (x = 2, n = 0), a level: %s; the test recognises 3 d1 + 1/7 in Q(d1) with its '
          'coordinates: %s: %s' % (deg, mp, '; '.join('%s: %s -> %s' % (n, s_, b) for n, s_, b in ft), cand, hit,
                                   pos, OK['R6']))
    if not selftest:
        mg, where, N = r6_margin(C)
        OK['R6m'] = mg > 0
        print('  R6 (certified margin): over the %d values x and n <= %d, the least distance of a level in (3, 4 + '
              'eps_K] or of alpha from lambda_sharp + n d1 + x is %.6e (at x = %s, n = %d), > 0: %s' % (
                  len(X_set()), N, float(mg), where[0], where[1], OK['R6m']))
    R7 = r7(C, polys)
    OK['R7'] = R7['ok']
    print('  R7 (exact): Proposition 5.1\'s hypothesis read for every j and every root: 2 - alpha + j is rational and '
          'never an integer, so it can meet only a non-integer rational root. R2 found none for box^Ups (every l), the '
          'physical factors, box^C at s0, s1 and the vector type (every l). The scalar sextic, scaled to integer '
          'coefficients (lcm %s), is -64 lam^6 %+d lam^5 + ... with that coefficient odd and free of kappa: a rational '
          'root, at any l, is an integer or has fractional part %s exactly (rational root theorem and 2-adic '
          'valuations), so -mu = 1 - lam_C has fractional part 0 or %s. The values 2 - alpha in (1/64) Z that occur: %s '
          '(3 - tau_i at I9, i <= %d; 2 - tau_i at I14 and the top levels, i <= %d: none); delta = %s, '
          'below 1/64. None equals %s: %s' % (
              R7['den'], R7['c5'], R7['frac'], 1 - R7['frac'],
              ['%s = %s at i = %d' % (nm, v, i) for nm, i, v in R7['vals']], R7['imax2'], R7['imax3'],
              ', '.join('%.4e' % float(d) for d in R7['deltas']), 1 - R7['frac'], OK['R7']))
    R8 = r8(C)
    OK['R8'] = R8['ok']
    print('  R8 (exact): the rest of I11:156-160\'s appended set (the exclusion set of III.I\'\'\'\'\'\'\'\'\'\'\' '
          'section 1, read at every level as I14 Definition 1.1 (c) does): l_zf = beta - 1 - j - eps is never an '
          'integer (j = 1, 2, 3; beta - eps in Z has no solution: %s); at level 1 the only tf-exponent in [2, 2 + '
          'eta_1) on R9.1\'s reading is 2 (modcount5 M5: no point of Lambda in (2, 2 + m) or (3, 3 + m), m > eta_1, '
          'whichever of I12 section 1\'s dictionaries is read), so (4.2)\'s last condition asks beta - 2 - eps != '
          '-mu, rational against the roots: an integer '
          'never (beta - eps not in Z); III.I\'\' Lemma 4.2 and III.H (1.1) ask beta_tf - beta_zf = tau - beta + 2 + '
          'eps in (0, 1) at level 3, which holds for the final tau in (beta - 2, beta - 1 - eps) (deduced): %s. Not '
          'decided here: (4.2) at level 2, whose tf-exponents in [1 + eta_1, 2 + eta_2) the record does not list' % (
              R8['hits'] or 'none', OK['R8']))
    R9 = r9(C)
    OK['R9'] = R9['ok']
    print('  R9 (exact): Definition 1.1 (a) at every level in (3, 4 + eps_K] (not asked by R9, decided by the same '
          'arithmetic): beta - 2 is never the real part of a rate. The rational candidates (lambda + 2 and lambda + 1 '
          'for the rational points of Lambda, from lambda_sharp, 2, 3 and the least E^C_I\'s %d points): %s; levels '
          'among them: %s; the irrational parts n d1 + theta1 + theta2 (theta1 in d0 and the E_col offsets delta_2..6, '
          'delta\'_1..5; theta2 in {0, d0}; theta2 = d1 is n + 1): none in Q(d1) (%d exact tests, failures %s): %s' % (
              R9['eci'], [str(x) for x in R9['cands']], R9['hits'] or 'none', R9['ntests'], R9['bad'] or 'none',
              OK['R9']))
    R10 = r10(C)
    OK['R10'] = not R10['hit'] and R10['rng'] and R10['step3'] and OK['R6']
    print('  R10 (exact): I9:55-58 (III.I\'\'\'\'\'\'\'\' admissibility), which I11:157 assigns to the levels '
          'alpha < 3, '
          'at every level in (2, 3), alpha_1 = beta_0 = %s included: the range alpha in (2, min(a_K, 3)) holds (at the '
          'base a_K = 2 + (1 - 10^-9) eps_K = %s > alpha_1, R10.1; at the levels a_K >= 4 + eps_K): %s; x = alpha - '
          'lambda, lambda in lambda_sharp + N_0 d1, lies in (0, 1.4901), where {-mu} u Re pi_1 E_K is {1, d0, d1, 1 + '
          'd0, 1 + d1, 1 + delta\'_1, 1 + delta_2} (the first clause, alpha - 2 != lambda - 1, is x = 1); the offsets '
          'are R6\'s, outside Q(d1), so the only rational candidate is alpha = lambda_sharp + 1 = %s, a level: '
          '%s; Lemma 3.1\'s alpha_0 = alpha_1 < min(a_K, 2 + eps_ind, 5/2) (in the range check above); Lemma 3.2 Step '
          '3\'s Proposition 5.1 (I9:276-279) at every level below 3: w = alpha - eps\' - 2 + eps in [%.4e, %.4e] '
          'and l_zf in (0, 1), rational, and 2 - alpha_P = eps below d1, the least positive root: off every root: '
          '%s: %s' % (Fr(I['alpha1'], D), R10['aK'], R10['rng'], R10['cand'], R10['hit'], float(R10['w'][0]),
                      float(R10['w'][1]), R10['step3'], OK['R10']))
    if not selftest:
        mg9, where9, N9 = levels_margin(C, X9_set(), 0, C['k3'] - 1, top=False)
        OK['R10m'] = mg9 > 0
        print('  R10 (certified margin): over the seven values x and n <= %d, the least distance of a level in (2, 3) '
              '(alpha_1 included) from lambda_sharp + n d1 + x is %.6e (at x = %s, n = %d), > 0: %s' % (
                  N9, float(mg9), where9[0], where9[1], OK['R10m']))
    # controls
    OK['C1'] = r6_exact(C, plant_level=DW.LSHARP + 2)[1]
    print('  C1 (control): a level planted at lambda_sharp + 2 = 3.5099: R6 finds it: %s' % OK['C1'])
    k0, i0 = R4['klo'] + 1000, 3
    epsp = Fr(beta(C, k0) - I['tau0'] - i0 * I['step'], D)
    w2 = dict(C['w'])
    w2['epsp'] = epsp
    C2 = chain(w2)
    R4b = r4(C2, roots)
    OK['C2'] = bool(R4b['hits'])
    print('  C2 (control): eps\' = %s, chosen so that w = 0 at (k, i) = (%d, %d): R4 finds hits %s: %s' % (
        epsp, k0, i0, R4b['hits'][:3], OK['C2']))
    OK['C3'] = ups_rational_l(Fr(7, 2)) != [0]
    print('  C3 (control): z = 7/2 ((z + 2)^2 + 12 = (13/2)^2): rational class-root degrees %s, not [0]: %s' % (
        ups_rational_l(Fr(7, 2))[:5], OK['C3']))
    ftc = field_tests(fake_d1=True)[2]
    OK['C4'] = any(b for _n, _s, b in ftc)
    print('  C4 (control): d1 replaced by a rational: the field argument reports rational sums: %s' % OK['C4'])
    wval = Fr(R4['A'] + (R4['klo'] + 5) * I['s'] - 2 * I['step'], D)
    R4c = r4(C, roots, plant=wval)
    OK['C5'] = R4c['margins'].get('d0') == 0
    print('  C5 (control): a root planted at w = %s (a value w takes): R4\'s margin %s: %s' % (
        wval, R4c['margins'].get('d0'), OK['C5']))
    R7['vals'].append(('planted', 0, 1 - R7['frac']))
    OK['C6'] = any((1 - v) % 1 == R7['frac'] for _n, _i, v in R7['vals'])
    print('  C6 (control): the value 2 - alpha = %s planted among R7\'s values: R7\'s test finds the hit: %s' % (
        1 - R7['frac'], OK['C6']))
    OK['C8'] = r10(C, plant=DW.LSHARP + 1)['hit']
    print('  C8 (control): a level below 3 planted at lambda_sharp + 1 = 2.5099: R10 finds it: %s' % OK['C8'])
    lam12 = algebraic_numbers()[0]
    try:
        sp.polys.numberfields.subfield.to_number_field(2 * (lam12 - 2) + sp.Rational(1, 3), lam12)
        OK['C7'] = True
    except sp.polys.polyerrors.IsomorphismFailed:
        OK['C7'] = False
    print('  C7 (control): R9\'s test on the offset 2 d1 + 1/3 (in Q(d1)): reported as a possible rational sum: %s' %
          OK['C7'])
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    builtins.print('%d/%d (%.0f s)' % (sum(OK.values()), len(OK), time.time() - t0))
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main(selftest='--selftest' in sys.argv))
