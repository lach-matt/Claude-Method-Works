#!/usr/bin/env python3
"""DOCKET 67, key gr-qc/9304008-quartic-renormalisation.

Kuo & Ford (gr-qc/9304008 v1, Sec. V): in flat space the quartic expectation
values in Delta 'may be defined in terms of normal ordered products'; the
curved-space generalisation 'will require a renormalization procedure for
quartic operator products in such spacetimes, which has not yet been
developed'; averaging would define 'a quantity similar to Delta without
invoking normal ordering' but 'introduces an arbitrary length or time scale'.

What is finite and checkable here is the ALGEBRA that makes the remark
substantive (or not), plus the fidelity of the tree's quotation.  Nothing
here decides the literature-status question (whether a procedure was later
developed) -- that is READ, not computed.

  Q0  fidelity: fluctuation.py:114-116's quotation equals the source text
      saved by this docket's kuo-ford-1993-measure stage (d67/src note).
  Q1  a c-number counterterm cancels in the variance in ANY state
      (generic 3x3 density matrix, generic Hermitian A) -- the Hu-Verdaguer
      mechanism the tree's DOCKET 64 correction cites.
  Q2  exact single-mode Weyl algebra: for a QUADRATIC operator, changing the
      normal-ordering reference quasifree state shifts it by a c-number only;
      for a QUARTIC product (the square KF need) the shift carries an
      OPERATOR-valued quadratic term.  So <:T^2:> -- and KF's Delta -- is not
      fixed up to a constant by fixing <T>: the quartic needs its own
      prescription.  This is the content of KF's remark, and it is real.
  Q3  the variance Var_psi(:A:_ref) is reference-independent (exact).
  Q4  numeric witness: KF's Delta for one squeezed state, normal-ordered
      w.r.t. two references, differs; Var does not.
  Q5  the ambiguity structure: :x^4:_s - :x^4:_t = -6(s-t) :x^2:_t + 3(s-t)^2
      (lower Wick powers with c-number coefficients -- the shape of the
      Hollands-Wald finite-renormalisation freedom, here in its simplest
      commutative instance; NOT a proof of their theorem).
Exit 0 iff every check passes.
"""
import re
import sys
from math import comb

import sympy as sp

RES = []


def chk(name, got, want):
    ok = (got == want)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "   got %r want %r" % (got, want)))


# ---------------------------------------------------------------- Q0 fidelity
ROOT = "/home/user/Claude-Method-Works/research/warp-drive/"
NOTE = ("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-"
        "527dc14c2847/scratchpad/d67/src/gr-qc_9304008.note")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


flu = open(ROOT + "fluctuation.py").read().splitlines()
tree_quote = norm(" ".join(l.strip() for l in flu[113:116]))   # lines 114-116
m = re.search(r'"(will require.*?developed\.)"', tree_quote)
note = norm(open(NOTE).read())
chk("Q0a fluctuation.py:114-116 carries a quotation", m is not None, True)
chk("Q0b the quotation occurs verbatim in the source text (saved note)",
    m is not None and m.group(1) in note, True)
chk("Q0c the source sentence is time-indexed ('has not yet been developed')",
    "which has not yet been developed" in note, True)
chk("Q0d the source restricts the remark to normal-ordered quartic products "
    "and names averaging as the route 'without invoking normal ordering'",
    ("may be defined in terms of normal ordered products" in note
     and "without invoking normal ordering" in note), True)
led = open(ROOT + "ledger.py").read().splitlines()
d22 = norm(" ".join("".join(re.findall(r'"((?:[^"\\\\]|\\\\.)*)"', l)) for l in led[749:763]))  # 750-763, literals joined
chk("Q0e ledger.py D22_DOCKET62 applies the remark to the SMEARED price",
    "the SMEARED fluctuation priced" in d22 and "quartic operator products" in d22, True)
chk("Q0f ledger.py D22_DOCKET62 drops the time index ('said did not exist')",
    "said did not exist" in d22 and "not yet" not in d22, True)

# ---------------------------------------------------------- Q1 c-number cancels
n = 3
rs = sp.symbols('r0:9')
A = sp.Matrix(n, n, lambda i, j: sp.Symbol('a%d%d' % (min(i, j), max(i, j))))
rho = sp.Matrix(n, n, lambda i, j: sp.Symbol('p%d%d' % (min(i, j), max(i, j))))
c = sp.Symbol('c')
tr = lambda M: sp.expand(M.trace())
constraint = {rho[2, 2]: 1 - rho[0, 0] - rho[1, 1]}


def var(Aop):
    return sp.expand((tr(rho * Aop * Aop) - tr(rho * Aop) ** 2).subs(constraint))


chk("Q1 Var(A + c 1) == Var(A) for generic A, generic unit-trace rho",
    sp.simplify(var(A + c * sp.eye(n)) - var(A)), 0)
chk("Q1' but <(A + c1)^2> != <A^2> (the shift is NOT invisible in a 2nd moment)",
    sp.simplify((tr(rho * (A + c * sp.eye(n)) ** 2) - tr(rho * A * A)).subs(constraint)) != 0, True)

# ------------------------------------------ exact single-mode Weyl algebra
# element = dict {(m, n): coef} meaning  a+^m a^n  (normal-ordered basis)


def mul(X, Y):
    out = {}
    for (m1, n1), x in X.items():
        for (m2, n2), y in Y.items():
            # a^n1 a+^m2 = sum_k C(n1,k) C(m2,k) k! a+^(m2-k) a^(n1-k)
            for k in range(min(n1, m2) + 1):
                key = (m1 + m2 - k, n1 + n2 - k)
                out[key] = out.get(key, 0) + x * y * comb(n1, k) * comb(m2, k) * sp.factorial(k)
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def add(*Xs):
    out = {}
    for X in Xs:
        for k, v in X.items():
            out[k] = out.get(k, 0) + v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def scal(s, X):
    return {k: sp.expand(s * v) for k, v in X.items()}


ONE = {(0, 0): sp.Integer(1)}


def lin(al, be):
    """X = al a + be a+"""
    return add({(0, 1): al}, {(1, 0): be})


def dfact(k):
    return sp.Integer(1) if k <= 0 else sp.factorial2(k)


def expect(X, N, M, Mb):
    """<a+^m a^n> in a zero-mean quasifree state with <a+a>=N, <aa>=M, <a+a+>=Mb
    (exact: sum over pairings of the ordered word a+..a+ a..a)."""
    tot = 0
    for (m, n_), coef in X.items():
        s = 0
        for k in range(min(m, n_) + 1):
            if (m - k) % 2 or (n_ - k) % 2:
                continue
            s += (comb(m, k) * comb(n_, k) * sp.factorial(k) * dfact(m - k - 1)
                  * dfact(n_ - k - 1) * N ** k * Mb ** ((m - k) // 2) * M ** ((n_ - k) // 2))
        tot += coef * s
    return sp.expand(tot)


def two_pt(X, Y, N, M, Mb):
    return expect(mul(X, Y), N, M, Mb)


def normal_order(Xs, st):
    """:X1...Xk:_st by the inverse Wick formula: sum over partial pairings
    (-1)^p prod st(Xi Xj) (i<j) times the ordered product of the unpaired."""
    k = len(Xs)

    def rec(idx):
        if not idx:
            return [(sp.Integer(1), [])]
        i, rest = idx[0], idx[1:]
        out = [(w, [i] + u) for w, u in rec(rest)]          # i unpaired
        for jpos, j in enumerate(rest):
            rem = rest[:jpos] + rest[jpos + 1:]
            wij = -two_pt(Xs[i], Xs[j], *st)
            out += [(wij * w, u) for w, u in rec(rem)]
        return out

    tot = {}
    for w, u in rec(list(range(k))):
        prod = ONE
        for i in sorted(u):
            prod = mul(prod, Xs[i])
        tot = add(tot, scal(w, prod))
    return tot


# references: vacuum (0,0,0) and a generic quasifree (N1, M1, M1b); state psi (N,M,Mb)
N, M, Mb, N1, M1, M1b = sp.symbols('N M Mb N1 M1 M1b')
vac = (0, 0, 0)
ref1 = (N1, M1, M1b)
al1, be1, al2, be2 = sp.symbols('al1 be1 al2 be2')
X1, X2 = lin(al1, be1), lin(al2, be2)

# sanity: vacuum normal ordering of a+ a is itself, of a a+ is a+ a
chk("sanity :a a+:_vac == a+ a", normal_order([lin(1, 0), lin(0, 1)], vac), {(1, 1): 1})
# sanity: <:X1 X2:_ref1>_ref1 == 0 and <:X1X2X1X2:_ref1>_ref1 == 0
chk("sanity <:X1X2:_ref>_ref == 0", expect(normal_order([X1, X2], ref1), *ref1), 0)
chk("sanity <:X1X2X1X2:_ref>_ref == 0", expect(normal_order([X1, X2, X1, X2], ref1), *ref1), 0)

# Q2: quadratic shift is c-number; quartic shift has an operator part
d2 = add(normal_order([X1, X2], vac), scal(-1, normal_order([X1, X2], ref1)))
chk("Q2a quadratic: :X1X2:_vac - :X1X2:_ref is a pure c-number",
    set(d2.keys()) <= {(0, 0)}, True)
d4 = add(normal_order([X1, X2, X1, X2], vac), scal(-1, normal_order([X1, X2, X1, X2], ref1)))
opdeg = {k for k in d4 if k != (0, 0)}
chk("Q2b quartic: :X1X2X1X2:_vac - :...:_ref has operator-valued part",
    len(opdeg) > 0, True)
chk("Q2c ...and that part is QUADRATIC only (lower Wick power, c-number coeffs)",
    all(m_ + n_ == 2 for (m_, n_) in opdeg), True)

# Q3: variance of a quadratic A is reference-independent
A_vac = normal_order([X1, X2], vac)
A_ref = normal_order([X1, X2], ref1)


def variance(Aop, st):
    return sp.expand(expect(mul(Aop, Aop), *st) - expect(Aop, *st) ** 2)


psi = (N, M, Mb)
chk("Q3 Var_psi(:X1X2:_vac) == Var_psi(:X1X2:_ref) identically",
    sp.simplify(variance(A_vac, psi) - variance(A_ref, psi)), 0)

# KF's quartic <:A^2:>: A^2 built as :X1X2X1X2: (4 linear factors).  Its
# reference dependence at fixed psi is NOT the square of the quadratic shift:
kf_vac = expect(normal_order([X1, X2, X1, X2], vac), *psi)
kf_ref = expect(normal_order([X1, X2, X1, X2], ref1), *psi)
shift = sp.expand(kf_vac - kf_ref)
chk("Q2d <:A^2:>_psi shift depends on the STATE psi (not a constant)",
    any(sp.diff(shift, s_) != 0 for s_ in (N, M, Mb)), True)

# ------------------------------------------------------------ Q4 numeric witness
# KF's single mode: :T00: = K(2 a+a - z a^2 - zbar a+^2).  Take K=1, z=1:
# 2a+a - a^2 - a+^2 = -(a - a+)^2 + 1  -> with X = (a - a+) (anti-Hermitian;
# use Y = i(a - a+)/sqrt2, Hermitian quadrature p): -(a-a+)^2 = 2 p^2.
# So :T00: = 2 :p^2: w.r.t. vacuum, KF normalisation irrelevant for ratios.
p = lin(sp.I / sp.sqrt(2), -sp.I / sp.sqrt(2))


def sq_state(r):          # squeezed vacuum S(r): N = sinh^2 r, M = -sinh r cosh r (phase 0)
    return (sp.sinh(r) ** 2, -sp.sinh(r) * sp.cosh(r), -sp.sinh(r) * sp.cosh(r))


st_psi = sq_state(sp.Rational(1, 2))
st_ref = sq_state(sp.Rational(-1, 5))


def kf_delta(Tfac, T2fac, ref, st):
    """Tfac: list of (coef, [X,X]) quadratic pieces; T2 = T*T as normal-ordered quartics."""
    T = add(*[scal(cf, normal_order(XX, ref)) for cf, XX in Tfac])
    T2 = add(*[scal(c1 * c2, normal_order(XX1 + XX2, ref)) for c1, XX1 in Tfac for c2, XX2 in Tfac])
    t = expect(T, *st)
    t2 = expect(T2, *st)
    return sp.N(t), sp.N(t2), sp.N(sp.Abs((t2 - t ** 2) / t2)), T


# (i) KF's single mode at theta = 0: :T00: = 2 :p^2: -- ONE quadrature
one_q = [(2, [p, p])]
tv, t2v, Dv, Tv = kf_delta(one_q, None, vac, st_psi)
tr_, t2r, Dr, Tr = kf_delta(one_q, None, st_ref, st_psi)
print("   Q4 one quadrature, psi=S(1/2): vac ref Delta=%.6f ; S(-1/5) ref Delta=%.6f" % (Dv, Dr))
chk("Q4a vacuum-ordered Delta, zero-mean Gaussian single mode == 2/3 (KF/tree value)",
    abs(Dv - sp.Rational(2, 3)) < 1e-12, True)
chk("Q4b RECORD (against over-reading): with ONE quadrature the reference change is "
    "INVISIBLE in Delta (<:X^4:> = 3<:X^2:>^2 for any Gaussian pair)",
    abs(Dv - Dr) < 1e-12, True)
# (ii) two quadratures, T = :x^2: + :p^2: (the shape of phi_t^2 + phi_x^2)
xq = lin(1 / sp.sqrt(2), 1 / sp.sqrt(2))
two_q = [(1, [xq, xq]), (1, [p, p])]
tv2, t2v2, Dv2, Tv2 = kf_delta(two_q, None, vac, st_psi)
tr2, t2r2, Dr2, Tr2 = kf_delta(two_q, None, st_ref, st_psi)
print("   Q4 two quadratures, psi=S(1/2): vac ref <T>=%.6f Delta=%.6f ; S(-1/5) ref <T>=%.6f Delta=%.6f"
      % (tv2, Dv2, tr2, Dr2))
chk("Q4c with TWO quadratures KF's Delta CHANGES with the reference state",
    abs(Dv2 - Dr2) > 1e-3, True)
Vv = sp.N(variance(Tv2, st_psi))
Vr = sp.N(variance(Tr2, st_psi))
print("   Q4 Var(T): vac ref %.9f ; S(-1/5) ref %.9f" % (Vv, Vr))
chk("Q4d ...while the variance does NOT", abs(Vv - Vr) < 1e-9, True)

# ------------------------------------------------------------- Q5 ambiguity shape
x, s, t = sp.symbols('x s t')


def wick_pow(k, g):      # :x^k:_g = g^(k/2) He_k(x/sqrt g)  (probabilists' Hermite)
    return sp.expand(sp.simplify(g ** sp.Rational(k, 2) * sp.hermite_prob(k, x / sp.sqrt(g))))


w4s, w4t, w2t = wick_pow(4, s), wick_pow(4, t), wick_pow(2, t)
chk("Q5a :x^4:_g == x^4 - 6 g x^2 + 3 g^2", sp.expand(w4s - (x**4 - 6*s*x**2 + 3*s**2)), 0)
chk("Q5b :x^4:_s - :x^4:_t == -6(s-t) :x^2:_t + 3(s-t)^2",
    sp.expand(w4s - w4t - (-6*(s - t)*w2t + 3*(s - t)**2)), 0)

print("%d/%d PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
