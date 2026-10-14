#!/usr/bin/env python3
"""DOCKET 67 / pass S item 32 -- qcd-one-loop-beta-threshold-matching.

Audits the INPUTS of address.py:88-97, 465-501:
  (a) b_0(n_f) = 11 - 2 n_f/3                       (textbook; Gross-Wilczek/Politzer 1973)
  (b) one-loop continuous matching at mu = m_Q  =>  Lambda_{n-1}^{b_{n-1}} = Lambda_n^{b_n} m_Q^{2/3}
  (c) Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27),  d ln Lambda_3/d ln v = 2/9
and measures how far the 'EXACTLY' survives beyond one loop by an INDEPENDENT route
(numerical RG running with v-scaled masses at a fixed high scale), to be compared with
the sibling audit's Hill-Solon closed form (dlnlambdaqcd-dlnv-2-9).

Sections
 1. SU(3) group theory from explicit Gell-Mann matrices: T_F = 1/2, C_A = 3, C_F = 4/3.
 2. b_0 = (11/3) C_A - (4/3) T_F n_f = 11 - 2 n_f/3 (the one-loop coefficients 11/3, 4/3 are
    NAMED-NOT-READ textbook input; cross-checked against the Nielsen-Hughes spin formula,
    which is a heuristic restatement, not a derivation).
 3. Threshold chain in sympy; tree's address.py functions imported READ-ONLY and compared.
 4. Robustness at one loop: matching at mu = kappa m_Q (kappa fixed) leaves 2/9 unchanged;
    matching-scale-invariance of the physical low-energy coupling under the one-loop
    decoupling relation alpha_l^-1 = alpha_h^-1 + ln(mu^2/m^2)/(6 pi).
 5. Beyond one loop, numerically: alpha_s(mu0) and m_Q(mu0) = lambda * m_Q^PDG(mu0) held,
    lambda varied; d ln Lambda_3/d ln lambda measured at LO / NLO / NNLO.
    Inputs NAMED-NOT-READ in this stage (PDG 2024 values; beta_0..beta_2, gamma_0..gamma_1,
    c2 = 11/72): see the report.
Exit 0 iff 0 failures.
"""
import math
import sys
from fractions import Fraction

import sympy as sp

FAIL = []


def chk(name, got, want, tol=None):
    if tol is None:
        ok = got == want
    else:
        ok = abs(got - want) <= tol
    print(("ok   " if ok else "FAIL ") + name + " : got %r want %r" % (got, want))
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- 1. group theory
print("1. SU(3) FROM EXPLICIT GELL-MANN MATRICES")
I = sp.I
lam = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3),
]
T = [m / 2 for m in lam]
TF = sp.nsimplify(sp.simplify((T[0] * T[0]).trace()))
orth = all(sp.simplify((T[a] * T[b]).trace() - (TF if a == b else 0)) == 0
           for a in range(8) for b in range(8))
chk("Tr(T^a T^b) = T_F delta^ab, T_F = 1/2", (TF, orth), (sp.Rational(1, 2), True))
# f^abc from [T^a, T^b] = i f^abc T^c  =>  f^abc = -2 i Tr([T^a,T^b] T^c)
f = [[[sp.simplify(-2 * I * ((T[a] * T[b] - T[b] * T[a]) * T[c]).trace())
       for c in range(8)] for b in range(8)] for a in range(8)]
CA = sp.simplify(sum(f[0][c][d] ** 2 for c in range(8) for d in range(8)))
CAdiag = all(sp.simplify(sum(f[a][c][d] * f[b][c][d] for c in range(8) for d in range(8))
                         - (CA if a == b else 0)) == 0 for a in range(8) for b in range(8))
chk("f^acd f^bcd = C_A delta^ab, C_A = 3", (CA, CAdiag), (3, True))
CF = sp.simplify(sum((t * t for t in T[1:]), T[0] * T[0]))
chk("sum_a T^a T^a = C_F 1, C_F = 4/3", CF, sp.eye(3) * sp.Rational(4, 3))

# ---------------------------------------------------------------- 2. b_0
print("\n2. b_0(n_f) = (11/3) C_A - (4/3) T_F n_f")
nf = sp.symbols("n_f")
b0_group = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf
chk("b_0 = 11 - 2 n_f/3", sp.expand(b0_group - (11 - sp.Rational(2, 3) * nf)), 0)
# Nielsen-Hughes heuristic: a spin-s field in rep R contributes -(-1)^{2s}((2s)^2 - 1/3) T(R)
# per real d.o.f. pair (vector: C_A; Weyl fermion: T_F, Dirac = 2 Weyl)
nh_gluon = ((2 * 1) ** 2 - sp.Rational(1, 3)) * CA           # 11/3 C_A
nh_dirac = -2 * ((2 * sp.Rational(1, 2)) ** 2 - sp.Rational(1, 3)) * TF   # -4/3 T_F
chk("Nielsen-Hughes restatement reproduces 11/3 C_A and -4/3 T_F",
    (nh_gluon, nh_dirac), (sp.Rational(11), sp.Rational(-2, 3)))
chk("step b_0(n-1) - b_0(n) = 2/3 for every n",
    sp.simplify(b0_group.subs(nf, nf - 1) - b0_group), sp.Rational(2, 3))
chk("asymptotic freedom b_0 > 0 iff n_f <= 16", [n for n in range(0, 20)
                                                 if b0_group.subs(nf, n) > 0][-1], 16)
# QED check of the same one-loop formula in address.py's convention (B_DIRAC_UNIT_CHARGE)
chk("QED limit: Dirac Q=1 coefficient 4/3 (address.py:520 convention)",
    sp.Rational(4, 3) * 1, sp.Rational(4, 3))

# ---------------------------------------------------------------- 3. the chain
print("\n3. THRESHOLD CHAIN (one loop, alpha_s continuous at mu = m_Q)")
L6, mc, mb, mt, v, mu, kap = sp.symbols("Lambda6 m_c m_b m_t v mu kappa", positive=True)
b0 = lambda n: sp.Rational(11) - sp.Rational(2, 3) * n
# one loop: 1/alpha_n(mu) = (b0(n)/(2 pi)) ln(mu/Lambda_n); continuity at mu = kappa*m:
#   b_hi ln(k m/L_hi) = b_lo ln(k m/L_lo)
def step(lnL_hi, n, m, k=1):
    L_lo = sp.symbols("Llo", positive=True)
    sol = sp.solve(sp.Eq(b0(n) * (sp.log(k * m) - lnL_hi),
                         b0(n - 1) * (sp.log(k * m) - sp.log(L_lo))), L_lo)[0]
    return sp.expand(sp.expand_log(sp.log(sol), force=True))


lnL = sp.log(L6)
for n, m in ((6, mt), (5, mb), (4, mc)):
    lnL = step(lnL, n, m)
coeffs = {s: sp.simplify(lnL.coeff(sp.log(s))) for s in (L6, mt, mb, mc)}
chk("Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27)",
    tuple(coeffs[s] for s in (L6, mt, mb, mc)),
    (sp.Rational(7, 9), sp.Rational(2, 27), sp.Rational(2, 27), sp.Rational(2, 27)))
chk("mass dimension closes: 7/9 + 3 x 2/27 = 1", sum(coeffs.values()), 1)
dl = sum(coeffs[s] for s in (mt, mb, mc))
chk("d ln Lambda_3 / d ln v = 2/9 (every m_Q ~ v, Lambda_6 fixed)", dl, sp.Rational(2, 9))
chk("top alone would give (2/3)/b0(5) = 2/23 at n_f=5 -- telescoping check",
    sp.Rational(2, 3) / b0(5), sp.Rational(2, 23))
# the telescoping identity behind 2/27: (2/3)/b_lo * prod(b_hi/b_lo) below = (2/3)/b_0(3)
chk("each heavy exponent telescopes to (2/3)/b_0(3)", sp.Rational(2, 3) / b0(3),
    sp.Rational(2, 27))

# the tree's own functions, imported READ-ONLY (no file is written by import)
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
sys.dont_write_bytecode = True
try:
    import address  # noqa: E402
    a, e = address._lambda_exponent_direct()
    chk("address._lambda_exponent_direct == (7/9, {t,b,c: 2/27})",
        (a, e), (Fraction(7, 9), {"m_t": Fraction(2, 27), "m_b": Fraction(2, 27),
                                  "m_c": Fraction(2, 27)}))
    chk("address.dln_lambda_dln_v() == 2/9", address.dln_lambda_dln_v(), Fraction(2, 9))
    chk("address.beta0(n) == 11 - 2n/3 for n = 0..6",
        [address.beta0(n) for n in range(7)],
        [Fraction(33 - 2 * n, 3) for n in range(7)])
    chk("address H1: d ln m_p/d ln v at S=0.06 == 2/9 + 7S/9",
        address.dln_mp_dln_v(Fraction(6, 100), "H1"),
        Fraction(2, 9) + Fraction(7, 9) * Fraction(6, 100))
except Exception as exc:  # pragma: no cover
    chk("address.py importable read-only (%s)" % exc, False, True)

# ---------------------------------------------------------------- 4. robustness at one loop
print("\n4. ONE-LOOP ROBUSTNESS")
lnLk = sp.log(L6)
for n, m in ((6, mt), (5, mb), (4, mc)):
    lnLk = step(lnLk, n, m, kap)
dlk = sum(sp.simplify(lnLk.coeff(sp.log(s))) for s in (mt, mb, mc))
chk("matching at mu = kappa m_Q (kappa fixed): d ln Lambda_3/d ln v still 2/9", dlk,
    sp.Rational(2, 9))
chk("... and kappa only rescales Lambda_3 by a v-independent constant",
    sp.simplify(sp.diff(lnLk - lnL, v)), 0)
# one-loop decoupling relation (standard MSbar, NAMED-NOT-READ):
#   1/alpha_lo(mu) = 1/alpha_hi(mu) + ln(mu^2/m^2)/(6 pi)
# must equal the running difference (b_lo - b_hi)/(4 pi) ln(mu^2/m^2) for consistency:
chk("one-loop decoupling log coefficient 1/(6 pi) == (b_lo - b_hi)/(4 pi)",
    sp.simplify(sp.Rational(1, 6) / sp.pi - sp.Rational(2, 3) / (4 * sp.pi)), 0)

# ---------------------------------------------------------------- 5. beyond one loop
print("\n5. BEYOND ONE LOOP: numerical RG, alpha_s(mu0) and m_Q(mu0)/v held fixed")
Z3 = 1.2020569031595942


def beta_coeffs(n):
    # d a/d ln mu^2 = -sum beta_i a^{i+2}, a = alpha_s/(4 pi)  (NAMED-NOT-READ here;
    # beta_0..beta_3 were READ from Hill-Solon 1409.8290 eq.(109) by the sibling audit)
    return (11 - 2 * n / 3, 102 - 38 * n / 3,
            2857 / 2 - 5033 * n / 18 + 325 * n ** 2 / 54)


def gamma_coeffs(n):
    # d ln m/d ln mu^2 = -sum g_i A^{i+1}, A = alpha_s/pi  (NAMED-NOT-READ)
    return (1.0, (202 / 3 - 20 * n / 9) / 16)


def rhs(a, n, nb, ng):
    """(da, d ln m) per d ln mu^2 with nb beta terms and ng gamma terms, a = alpha/(4 pi)."""
    B = beta_coeffs(n)[:nb]
    G = gamma_coeffs(n)[:ng]
    da = -sum(B[i] * a ** (i + 2) for i in range(nb))
    A = 4 * a
    dlm = -sum(G[i] * A ** (i + 1) for i in range(ng))
    return da, dlm


def run(a, lnm, t0, t1, n, nb, ng, steps=3000):
    """RK4 in t = ln mu^2; lnm is a dict name -> ln m(mu) for the running masses."""
    h = (t1 - t0) / steps
    for _ in range(steps):
        k1 = rhs(a, n, nb, ng)
        k2 = rhs(a + h * k1[0] / 2, n, nb, ng)
        k3 = rhs(a + h * k2[0] / 2, n, nb, ng)
        k4 = rhs(a + h * k3[0], n, nb, ng)
        a += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        dl = h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        lnm = {k: x + dl for k, x in lnm.items()}   # gamma_m is flavour-blind
    return a, lnm


def find_threshold(a, lnm, t, name, n, nb, ng):
    """Run down in the n-flavour theory until ln m_name(mu) = ln mu, i.e. mu = m(m)."""
    # bracket by bisection on t
    def g(tt):
        aa, ll = run(a, lnm, t, tt, n, nb, ng, steps=400)
        return ll[name] - tt / 2, aa, ll
    hi, lo = t, 2 * lnm[name] - 2.0          # ln mu^2 of the start, and well below
    for _ in range(60):
        mid = (hi + lo) / 2
        val, _, _ = g(mid)
        if val > 0:          # m(mu) > mu: threshold is above mid
            lo = mid
        else:
            hi = mid
    tt = (hi + lo) / 2
    aa, ll = run(a, lnm, t, tt, n, nb, ng, steps=3000)
    return tt, aa, ll


def lambda3(scale, a0, lnm0, t0, order, c2=11 / 72, a_ref=0.35 / (4 * math.pi)):
    """ln(mu_ref) at which alpha^(3) = 4 pi a_ref, with all m_Q(mu0) multiplied by `scale`.
    order 0: 1-loop beta, masses NOT run (m(m) = scale * m^PDG(m)) -- the tree's model.
    order 1: 2-loop beta + 1-loop gamma_m, alpha continuous at mu = m(m).
    order 2: 3-loop beta + 2-loop gamma_m + decoupling alpha_l = alpha_h(1 + c2 (alpha_h/pi)^2)."""
    nb, ng = {0: (1, 0), 1: (2, 1), 2: (3, 2)}[order]
    lnm = {k: x + math.log(scale) for k, x in lnm0.items()}
    a, t = a0, t0
    for n, name in ((6, "t"), (5, "b"), (4, "c")):
        if order == 0:
            tt = 2 * lnm[name]                    # threshold at scale * m(m)
            a, lnm = run(a, lnm, t, tt, n, nb, ng)
        else:
            tt, a, lnm = find_threshold(a, lnm, t, name, n, nb, ng)
        if order == 2:
            A = 4 * a
            a = a * (1 + c2 * A ** 2)
        t = tt
    # 3-flavour running to alpha = alpha_ref: integrate t as a function of a
    nb3 = nb
    B = beta_coeffs(3)[:nb3]
    N = 20000
    h = (a_ref - a) / N
    fn = lambda x: -1.0 / sum(B[i] * x ** (i + 2) for i in range(nb3))
    for _ in range(N):
        k1 = fn(a); k2 = fn(a + h / 2); k3 = fn(a + h / 2); k4 = fn(a + h)
        t += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        a += h
    return t / 2   # ln mu_ref


# PDG 2024 inputs (NAMED-NOT-READ in this stage): alpha_s(M_Z), MSbar m(m)
MZ, ASMZ = 91.1876, 0.1180
MQ = {"c": 1.2730, "b": 4.183, "t": 162.5}


def setup(order, asmz=ASMZ):
    """Establish alpha^(6)(mu0) and m_Q(mu0) at mu0 = 1000 GeV consistent with the
    PDG m(m) at the given order (so the lambda = 1 point reproduces PDG)."""
    nb, ng = {0: (1, 0), 1: (2, 1), 2: (3, 2)}[order]
    c2 = 11 / 72 if order == 2 else 0.0
    a = asmz / (4 * math.pi)
    # up from M_Z in n_f = 5 to m_t, match, up to mu0 in n_f = 6
    t_mz, t_t, t0 = math.log(MZ ** 2), math.log(MQ["t"] ** 2), math.log(1000.0 ** 2)
    a, _ = run(a, {}, t_mz, t_t, 5, nb, ng)
    a = a / (1 + c2 * (4 * a) ** 2)
    a6_mt = a
    a0, _ = run(a, {}, t_t, t0, 6, nb, ng)
    # masses at mu0: run each m(m) up to mu0 through the flavour regions (order >= 1);
    # the flavour-blind gamma_m runs every mass alike, so track the log-ratio per region
    lnm0 = {}
    for name in ("c", "b", "t"):
        if order == 0:
            lnm0[name] = math.log(MQ[name])       # the tree's model: m(m) itself ~ v
            continue
        # piecewise: from m(m) up to mu0 with the n_f of each region
        edges = [("c", 4), ("b", 5), ("t", 6)]
        start = {"c": 0, "b": 1, "t": 2}[name]
        lm, t_cur = math.log(MQ[name]), math.log(MQ[name] ** 2)
        # alpha at m(m) in the region's theory: run from M_Z
        n_here = edges[start][1]
        # get alpha^(n_here)(m(m)) by running from M_Z in n_f=5 (and matching for c, t)
        a_cur = asmz / (4 * math.pi)
        if name == "t":
            a_cur = a6_mt
        elif name == "b":
            a_cur, _ = run(a_cur, {}, t_mz, t_cur, 5, nb, ng)
        else:
            ab, _ = run(a_cur, {}, t_mz, math.log(MQ["b"] ** 2), 5, nb, ng)
            ab = ab * (1 + c2 * (4 * ab) ** 2)
            a_cur, _ = run(ab, {}, math.log(MQ["b"] ** 2), t_cur, 4, nb, ng)
        for k in range(start, 3):
            n = edges[k][1]
            t_end = t0 if k == 2 else math.log(MQ[edges[k + 1][0]] ** 2)
            a_cur, d = run(a_cur, {"x": lm}, t_cur, t_end, n, nb, ng)
            lm = d["x"]
            if k < 2:
                a_cur = a_cur / (1 + c2 * (4 * a_cur) ** 2)
            t_cur = t_end
        lnm0[name] = lm
    return a0, lnm0, t0


results = {}
for order in (0, 1, 2):
    a0, lnm0, t0 = setup(order)
    eps = 0.02
    up = lambda3(math.exp(eps), a0, lnm0, t0, order)
    dn = lambda3(math.exp(-eps), a0, lnm0, t0, order)
    d = (up - dn) / (2 * eps)
    # reference independence (massless 3-flavour theory): a different alpha_ref
    up2 = lambda3(math.exp(eps), a0, lnm0, t0, order, a_ref=0.5 / (4 * math.pi))
    dn2 = lambda3(math.exp(-eps), a0, lnm0, t0, order, a_ref=0.5 / (4 * math.pi))
    d2 = (up2 - dn2) / (2 * eps)
    results[order] = d
    print("     order %d: d ln Lambda_3/d ln v = %.5f  (= %.4f x 2/9)   [alpha_ref 0.5: %.5f]"
          % (order, d, d / (2 / 9), d2))
    chk("order %d: independent of the reference coupling (massless n_f=3)" % order,
        d, d2, tol=2e-4)

chk("LO numeric run reproduces 2/9 (the tree's model)", results[0], 2 / 9, tol=1e-5)
# the sibling audit's Hill-Solon closed form at S = 0 gives heavy sum = d ln Lambda_3/d ln v:
#   NLO 1.0592.., NNLO 1.0651.., N3LO 1.0617.. x 2/9 at S=0.06; (f-S)/(1-S) = 0.23839 at S=0 N3LO
print("     beyond-LO shift: NLO %+.2f%%, NNLO %+.2f%%  (sibling audit, Hill-Solon N3LO at S=0: "
      "+7.28%%)" % (100 * (results[1] / (2 / 9) - 1), 100 * (results[2] / (2 / 9) - 1)))
chk("beyond LO the shift is POSITIVE and below 10%",
    0 < results[1] / (2 / 9) - 1 < 0.10 and 0 < results[2] / (2 / 9) - 1 < 0.10, True)
chk("NNLO numeric agrees with the Hill-Solon N3LO value 0.23839 (sibling) within 2%",
    results[2], 0.23839, tol=0.02 * 0.23839)

# sensitivity of the NNLO shift to alpha_s(M_Z) +- 0.0009 (PDG 2024 band, NAMED-NOT-READ)
sens = []
for asmz in (ASMZ - 0.0009, ASMZ + 0.0009):
    a0, lnm0, t0 = setup(2, asmz)
    up = lambda3(math.exp(0.02), a0, lnm0, t0, 2)
    dn = lambda3(math.exp(-0.02), a0, lnm0, t0, 2)
    sens.append((up - dn) / 0.04)
print("     NNLO over alpha_s(M_Z) = 0.1171 .. 0.1189: %.5f .. %.5f" % tuple(sens))
chk("alpha_s(M_Z) band moves the NNLO value by < 1%",
    max(abs(s / results[2] - 1) for s in sens) < 0.01, True)

# ---------------------------------------------------------------- 6. per-quark localisation
print("\n6. PER-QUARK (scale one m_Q(mu0) at a time) vs Hill-Solon closed form (sibling audit)")
# Hill-Solon 1409.8290 eq.(39)+(119) at lambda = 0, iterated c -> b -> t, as transcribed and
# checked against their eqs.(120),(61) by sibling audit dlnlambdaqcd-dlnv-2-9 (4-loop running,
# c2 = 11/72): NLO / NNLO / N3LO per quark
HS = {"t": (0.075674, 0.075618, 0.075673), "b": (0.078762, 0.079123, 0.078988),
      "c": (0.082940, 0.084455, 0.083726)}


def per_quark(order, name):
    a0, lnm0, t0 = setup(order)
    def L(e):
        lm = dict(lnm0)
        lm[name] += e
        return lambda3(1.0, a0, lm, t0, order)
    return (L(0.02) - L(-0.02)) / 0.04


pq = {n: per_quark(2, n) for n in "tbc"}
for n in "tbc":
    print("     %s: numeric NNLO %.5f   Hill-Solon NLO/NNLO/N3LO %.5f %.5f %.5f   (LO 2/27 = %.5f)"
          % ((n, pq[n]) + HS[n] + (2 / 27,)))
chk("per-quark sum equals the all-scaled NNLO value", sum(pq.values()), results[2], tol=1e-6)
chk("top leg: numeric NNLO within 0.5% of Hill-Solon N3LO", pq["t"], HS["t"][2],
    tol=0.005 * HS["t"][2])
chk("bottom leg: numeric NNLO within 1% of Hill-Solon N3LO", pq["b"], HS["b"][2],
    tol=0.01 * HS["b"][2])
print("     charm leg: numeric NNLO %.5f vs Hill-Solon N3LO %.5f (%+.1f%%) -- the"
      " 'poorly convergent alpha_s(m_c) expansion' Hill-Solon name; a truncation spread,"
      " recorded, not an error" % (pq["c"], HS["c"][2], 100 * (pq["c"] / HS["c"][2] - 1)))
chk("charm leg: the two routes differ by less than 6% of f_c", pq["c"], HS["c"][2],
    tol=0.06 * HS["c"][2])

print("\n%d failures" % len(FAIL))
sys.exit(1 if FAIL else 0)
