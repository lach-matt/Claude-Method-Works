#!/usr/bin/env python3
r"""
fluctuation.py -- KUO & FORD, RE-DERIVED EXACTLY.  THE SEMICLASSICAL DEBT.

M: "the geometry is sourced by the expectation value of the stress-tensor
operator.  That's a good approximation -- this is a problem.  This is the
coefficient debt.  We need precision math.  And it is worth reading Kuo & Ford."

M is right about what the debt is.  Every DEMAND row in ledger.py is a demand on
<rho>, inside G = 8 pi G <T>, and the error term of that equation is stated
nowhere in this tree.  Kuo & Ford (gr-qc/9304008) are the paper that turns
"good approximation" into a computed quantity:

    Delta(x) = | <:T00^2:> - <:T00:>^2 | / <:T00^2:>          KF (3.2)

normal-ordered against the Minkowski vacuum, flat spacetime, coincidence limit,
massless minimally coupled scalar.  Delta << 1 is their criterion for the
semiclassical equation to hold.

    python3 fluctuation.py             the reading
    python3 fluctuation.py --selftest  every figure re-derived, and the proofs

===============================================================================
1. EVERY PRINTED EQUATION, TESTED TWO INDEPENDENT WAYS
===============================================================================

Single-mode states by (F) exact Fock-space matrices and (G) exact Gaussian
normal-ordered moments from the generating function
<exp(s a+) exp(t a)> = exp(s a* + t a + N s t + M* s^2/2 + M t^2/2).
(F) and (G) are each other's control, and a third, numeric Fock series at 60
digits, controls (G) on the infinite squeezed-vacuum state.

    KF (2.16) middle line   <:T00:> vacuum+2           EXACT
    KF (2.16) final line    ... = K eps(2eps - sqrt2 cos2th)/(1+eps^2)
                            IS HALF ITS OWN MIDDLE LINE.  A dropped 2.
    KF (3.7)                <:T00^2:> = 12 K^2 eps^2/(1+eps^2)^2
                            EXACT IS 12 K^2 eps^2/(1+eps^2).  One power too many.
    KF (3.8)                Delta = (10 eps + sqrt2 cos2th)/(12 eps)
                            NOT THE EXACT DELTA, which is
                            Delta = 1 - (2eps - sqrt2 cos2th)^2 / (3(1+eps^2)).
    KF (3.18), (3.22)       <:T00:> squeezed coherent / vacuum   EXACT
    KF (3.19), (3.23)       <:T00^2:> squeezed                   NOT EXACT.
                            For the squeezed vacuum the exact result is
                            <:T00^2:> = 3 <:T00:>^2, IDENTICALLY.
    KF (3.21)               coherent state, Delta = 0            EXACT
    KF (3.33)               Casimir rho = -pi^2/(90 L^4)          EXACT
    KF (3.41), (3.42)       print 1/2 where 1/4 holds; the 1/8 of (3.43)
                            is right, so this one is typographical.
    KF (3.45)               Delta' >= 1/2, Delta >= 1/3; 6 and 6/7   EXACT

===============================================================================
2. WHAT THAT DOES TO THEIR CONCLUSION -- IT SURVIVES, AND ITS INEQUALITY DOES NOT
===============================================================================

KF state after (3.8): "the condition for the expectation value of energy
density to be negative is cos(2 theta) > sqrt2 eps.  In this case we have
Delta(x) > 1."  With the exact Delta that is FALSE, and z3 finds the
counterexample.  What is true, and PROVED here (T2):

        rho < 0   ==>   1/3  <  Delta  <  1          (vacuum + two particle)

At eps = 1/10, theta = 0 the exact Delta is 0.5134; KF's (3.8) gives 2.0118.
Their qualitative conclusion -- fluctuations of order unity wherever rho < 0 --
SURVIVES in every case they study.  The inequality they printed does not.

===============================================================================
3. A THEOREM STRONGER THAN THEIRS, AND WHAT IT COSTS THEM
===============================================================================

For ANY zero-mean quasifree (Gaussian) state -- squeezed vacua, the Casimir
vacuum, thermal states -- Wick's theorem gives

        <:T00^2:> = rho^2 + (1/2) SUM_AB G_AB^2 ,   G_AB = <:d_A phi d_B phi:>

and since rho = (1/2) tr G, Cauchy-Schwarz gives SUM G_AB^2 >= (tr G)^2/4, so

        Delta' >= 1/2 ,  Delta >= 1/3        (T1, PROVED by z3)

with equality only at G = (rho/2) I.  KF reach 1/3 assuming G diagonal; the
proof here does not need it.

AND THE SAME THEOREM CUTS AGAINST THE READING THEIR PAPER INVITES.  The bound
does not care about the SIGN of rho.  The same image-sum machinery, run in
imaginary time, gives a thermal state -- and reproduces Stefan-Boltzmann,
rho = pi^2/(30 beta^4) with p = rho/3, as a positive control -- and then gives

        THERMAL RADIATION:  Delta' = 2/3,  Delta = 2/5.

So ordinary positive-energy blackbody radiation fails KF's pointwise criterion
by the same margin as negative energy.  And the single-mode squeezed vacuum has
Delta = 2/3 EXACTLY, at every point where rho != 0, on BOTH sides of zero.

    THE POINTWISE Delta DOES NOT DISCRIMINATE NEGATIVE ENERGY.  It
    discriminates the MEAN FIELD: coherent states give 0, every zero-mean
    Gaussian state gives at least 1/3.

===============================================================================
4. WHAT THIS MEANS FOR THE COEFFICIENT DEBT -- AND WHAT THIS FILE REFUSES
===============================================================================

The debt is real and is now stated exactly: semiclassical gravity's error term
is Delta, and at a point Delta >= 1/3 for every state that carries negative
energy by squeezing or by boundaries.

BUT THE POINTWISE Delta CANNOT BE THE DEMAND ROW, for three reasons, each read
at source or proved here:
  (a) it condemns thermal radiation equally (Delta = 2/5), whose gravity the
      semiclassical equation handles when the field is SMEARED over the scales
      gravity responds to -- so the physical quantity is smeared, not pointwise;
  (b) KF say so themselves: averaging "introduces an arbitrary length or time
      scale" -- AND FOR THE CORRIDOR THE SCALE IS NOT ARBITRARY.  It has its
      own: the width b, and Fewster's sampling time.  That is where a price
      must be computed;
  (c) KF: the curved-space version "will require a renormalization procedure
      for quartic operator products in such spacetimes, which has not yet been
      developed."  Their words, 1993.

So this file REFUSES to price the corridor's fluctuation demand.  It supplies
the exact flat-space measure, the theorem, and the scale question the price
must answer.  No ledger row moves on it.

STATUS OF THE SOURCE.  Checked against arXiv gr-qc/9304008 v1, its PDF TEXT
LAYER, fetched twice through the alphaXiv connector; the page image was not
viewed.  The published version, Phys. Rev. D 47, 4510 (1993), is
NAMED-NOT-READ -- the discrepancies above are against v1 and MUST NOT be quoted
as errors in the journal version until it is read.

NOTHING IS REPAIRED.  Kuo & Ford is not edited; the discrepancies are recorded.
"""

import sys

SOURCE = "Kuo & Ford, 'Semiclassical gravity theory and quantum fluctuations', gr-qc/9304008 v1"
SOURCE_READ = "arXiv v1 PDF text layer, via alphaXiv, twice"
JOURNAL_VERSION_READ = False                # PRD 47, 4510 -- NAMED-NOT-READ
PAGE_IMAGE_VIEWED = False

# ------------------------------------------------ KF's printed equations, as READ
KF_216_FINAL_IS_EXACT = False               # half its own middle line
KF_216_MIDDLE_IS_EXACT = True
KF_37_IS_EXACT = False                      # (1+eps^2)^2 for (1+eps^2)
KF_38_IS_EXACT = False
KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 = False  # refuted
KF_318_IS_EXACT = True
KF_319_IS_EXACT = False
KF_322_IS_EXACT = True
KF_323_IS_EXACT = False
KF_321_IS_EXACT = True
KF_333_IS_EXACT = True
KF_341_HALF_IS_TYPOGRAPHICAL = True
KF_345_IS_EXACT = True
KF_QUALITATIVE_CONCLUSION_SURVIVES = True

# ------------------------------------------------------------- what is new here
POINTWISE_DELTA_DISCRIMINATES_SIGN = False  # thermal radiation gives 2/5
BOUND_NEEDS_DIAGONAL_G = False              # KF assumed it; T1 does not
PRICES_THE_CORRIDOR = False
LEDGER_ROW_MOVES = False
NOTHING_IS_REPAIRED = True

VACPLUS2_EPS_WITNESS = (1, 10)              # eps = 1/10, theta = 0


def _need():
    try:
        import sympy as sp
        import z3
    except ImportError as exc:              # pragma: no cover
        raise SystemExit("fluctuation.py needs sympy and z3 (pip install sympy z3-solver): %s" % exc)
    return sp, z3


# =========================================================== single-mode algebra
def single_mode(sp):
    K, eps, s, c = sp.symbols('K epsilon s c', positive=True)
    z = sp.symbols('z')                     # z = exp(2 i theta)
    cos2 = (z + 1 / z) / 2
    cos4 = (z**2 + z**-2) / 2
    # :T00: = K (2 a+a - z a^2 - zbar a+^2), from KF (2.10)-(2.14)
    T1 = {(1, 1): 2 * K, (0, 2): -z * K, (2, 0): -K / z}

    def nprod(A, B):
        out = {}
        for (m1, n1), a in A.items():
            for (m2, n2), b in B.items():
                out[(m1 + m2, n1 + n2)] = out.get((m1 + m2, n1 + n2), 0) + a * b
        return out

    T2 = nprod(T1, T1)

    def lower(v):
        return [sp.sqrt(j + 1) * v[j + 1] for j in range(len(v) - 1)] + [0]

    def fock(vec, P):
        tot = 0
        for (m, n), coef in P.items():
            am, an = list(vec), list(vec)
            for _ in range(m):
                am = lower(am)
            for _ in range(n):
                an = lower(an)
            tot += coef * sum(sp.conjugate(x) * y for x, y in zip(am, an))
        return sp.simplify(sp.expand(tot))

    Sg, Tg = sp.symbols('S T')

    def gauss(P, al, alc, N, M, Mc):
        G = sp.exp(Sg * alc + Tg * al + N * Sg * Tg + Mc * Sg**2 / 2 + M * Tg**2 / 2)
        tot = 0
        for (m, n), coef in P.items():
            d = sp.diff(G, Sg, m, Tg, n) if (m or n) else G
            tot += coef * d.subs({Sg: 0, Tg: 0})
        return sp.expand(tot)

    return dict(K=K, eps=eps, s=s, c=c, z=z, cos2=cos2, cos4=cos4,
                T1=T1, T2=T2, fock=fock, gauss=gauss)


def is_zero(sp, e, s, c):
    e = sp.expand(sp.simplify(e))
    return sp.simplify(sp.expand(e.subs(c, sp.sqrt(1 + s**2)))) == 0


def vacuum_plus_two(sp, m):
    K, eps, z, cos2 = m['K'], m['eps'], m['z'], m['cos2']
    N = 1 + eps**2
    vec = [1 / sp.sqrt(N), 0, eps / sp.sqrt(N)] + [0] * 6
    rho = m['fock'](vec, m['T1'])
    T2 = m['fock'](vec, m['T2'])
    delta_exact = 1 - (2 * eps - sp.sqrt(2) * cos2)**2 / (3 * N)
    return dict(
        rho=rho, T2=T2,
        mid=eps / N * (sp.sqrt(2) * (-K * z - K / z) + 2 * eps * (2 * K)),
        final=K * eps / N * (2 * eps - sp.sqrt(2) * cos2),
        kf37=K**2 * 12 * eps**2 / N**2,
        kf38=(10 * eps + sp.sqrt(2) * cos2) / (12 * eps),
        delta=sp.simplify(1 - rho**2 / T2),
        delta_closed=delta_exact)


def squeezed(sp, m):
    s, c, z, K = m['s'], m['c'], m['z'], m['K']
    al, alc, w = sp.symbols('alpha alphabar w')
    rho = m['gauss'](m['T1'], al, alc, s**2, -w * s * c, -s * c / w)
    T2 = m['gauss'](m['T2'], al, alc, s**2, -w * s * c, -s * c / w)
    Sm, g = sp.symbols('S_mod g')
    sub = {al: Sm * sp.sqrt(g), alc: Sm / sp.sqrt(g)}
    C = lambda u: (u + 1 / u) / 2
    kf318 = 2 * K * (s * c * C(z * w) + s**2 + Sm**2 * (1 - C(z * g)))
    kf319 = 2 * K**2 * (Sm**4 * (C(z**2 * g**2) - 4 * C(z * g) + 3)
                        + 3 * Sm**2 * (2 * s * c * (2 * C(z * w * g) - C(z**2 * w * g))
                                       + 4 * s**2 * (C(g) - C(z)) - C(w * g))
                        + 3 * s**2 * (c**2 * C(z**2 * w**2) + 3 - 4 * C(z)))
    sv = {al: 0, alc: 0, w: 1}
    return dict(
        rho=sp.expand(rho.subs(sub)), T2=sp.expand(T2.subs(sub)),
        kf318=kf318, kf319=kf319,
        rho_sv=sp.expand(rho.subs(sv)), T2_sv=sp.expand(T2.subs(sv)),
        kf322=2 * K * s * (c * m['cos2'] + s),
        kf323=2 * K**2 * s**2 * (2 * c**2 * m['cos4'] - 8 * s * c * m['cos2'] + 3 * (s**2 + c**2)),
        rho_cs=sp.expand(rho.subs({s: 0, c: 1})), T2_cs=sp.expand(T2.subs({s: 0, c: 1})))


# ============================================================ image sums (KF III.C)
def image_stress(sp, shift):
    dt, dx, dy, dz = sp.symbols('dt dx dy dz', real=True)
    n = sp.symbols('n', integer=True, positive=True)
    D = (dt, dx, dy, dz)
    st, sz = shift(n)
    sig = -(dt + st)**2 + dx**2 + dy**2 + (dz + sz)**2
    G = sp.zeros(4, 4)
    for A in range(4):
        for B in range(A, 4):
            t = -sp.diff(1 / (4 * sp.pi**2 * sig), D[A], D[B])
            t = sp.simplify(t.subs({dt: 0, dx: 0, dy: 0, dz: 0}))
            G[A, B] = G[B, A] = sp.simplify(2 * sp.summation(t, (n, 1, sp.oo)))
    rho = sp.simplify((G[0, 0] + G[1, 1] + G[2, 2] + G[3, 3]) / 2)
    p = [sp.simplify(G[i, i] + (G[0, 0] - G[1, 1] - G[2, 2] - G[3, 3]) / 2) for i in (1, 2, 3)]
    T2 = rho**2 + sum(G[A, B]**2 for A in range(4) for B in range(4)) / 2
    Dp = sp.simplify((T2 - rho**2) / rho**2)
    return dict(G=G, rho=rho, p=p, Dprime=Dp, Delta=sp.simplify(Dp / (1 + Dp)))


# ======================================================================== proofs
def prove(z3, hyps, goal):
    s = z3.Solver()
    s.add(*hyps)
    s.add(z3.Not(goal))
    return s.check() == z3.unsat


def theorems(z3):
    g = {(A, B): z3.Real('g%d%d' % (min(A, B), max(A, B))) for A in range(4) for B in range(4)}
    tr = g[0, 0] + g[1, 1] + g[2, 2] + g[3, 3]
    sq = z3.Sum([g[A, B] * g[A, B] for A in range(4) for B in range(4)])
    out = {}
    out['T1'] = prove(z3, [], sq * 4 >= tr * tr)
    out['T1_equality'] = prove(z3, [sq * 4 == tr * tr],
                               z3.And([g[A, B] == (tr / 4 if A == B else 0)
                                       for A in range(4) for B in range(A, 4)]))
    guard = z3.Solver()
    guard.add(z3.Not(sq * 3 >= tr * tr))
    out['T1_guard_fails'] = guard.check() == z3.sat
    e, cc, q = z3.Reals('e c q')
    H = [q > 0, q * q == 2, cc >= -1, cc <= 1, e * (2 * e - q * cc) < 0]
    X = 2 * e - q * cc
    out['T2_gt_third'] = prove(z3, H, X * X < 2 * (1 + e * e))
    out['T2_lt_one'] = prove(z3, H, X * X > 0)
    kf = z3.Solver()
    kf.add(*H)
    kf.add(z3.Not(X * X > 6 * (1 + e * e)))
    out['KF_gt_one_refuted'] = kf.check() == z3.sat
    return out


def report():
    sp, z3 = _need()
    m = single_mode(sp)
    v = vacuum_plus_two(sp, m)
    q = squeezed(sp, m)
    L, beta = sp.symbols('L beta', positive=True)
    cas = image_stress(sp, lambda n: (0, n * L))
    thm = image_stress(sp, lambda n: (sp.I * n * beta, 0))
    th = theorems(z3)
    e0 = sp.Rational(*VACPLUS2_EPS_WITNESS)
    at = {m['eps']: e0, m['z']: 1}

    print("=" * 79)
    print("fluctuation.py -- Kuo & Ford re-derived exactly")
    print("=" * 79)
    print("\n  source:  %s\n           %s" % (SOURCE, SOURCE_READ))
    print("           journal version PRD 47 4510 read: %s\n" % JOURNAL_VERSION_READ)
    print("  1. THE PRINTED EQUATIONS")
    rows = [
        ("(2.16) middle line", is_zero(sp, v['mid'] - v['rho'], m['s'], m['c'])),
        ("(2.16) final line", is_zero(sp, v['final'] - v['rho'], m['s'], m['c'])),
        ("(3.7)  <:T^2:> vac+2", is_zero(sp, v['kf37'] - v['T2'], m['s'], m['c'])),
        ("(3.8)  Delta vac+2", is_zero(sp, v['kf38'] - v['delta'], m['s'], m['c'])),
        ("(3.18) <:T:> squeezed coherent", is_zero(sp, q['kf318'] - q['rho'], m['s'], m['c'])),
        ("(3.19) <:T^2:> squeezed coherent", is_zero(sp, q['kf319'] - q['T2'], m['s'], m['c'])),
        ("(3.22) <:T:> squeezed vacuum", is_zero(sp, q['kf322'] - q['rho_sv'], m['s'], m['c'])),
        ("(3.23) <:T^2:> squeezed vacuum", is_zero(sp, q['kf323'] - q['T2_sv'], m['s'], m['c'])),
        ("(3.21) coherent Delta = 0", is_zero(sp, q['T2_cs'] - q['rho_cs']**2, m['s'], m['c'])),
    ]
    for name, ok in rows:
        print("      %-36s %s" % (name, "EXACT" if ok else "NOT EXACT"))
    print("      (2.16) final / exact = %s" % sp.simplify(v['final'] / v['rho']))
    print("      (3.7)  printed / exact = %s" % sp.simplify(v['kf37'] / v['T2']))
    print("      squeezed vacuum: <:T^2:> = 3 rho^2 identically: %s"
          % is_zero(sp, q['T2_sv'] - 3 * q['rho_sv']**2, m['s'], m['c']))
    print()
    print("  2. THE INEQUALITY")
    print("      at eps = 1/10, theta = 0:  exact Delta = %.4f   KF (3.8) = %.4f"
          % (float(v['delta'].subs(at)), float(v['kf38'].subs(at))))
    print("      KF 'rho<0 => Delta>1' refuted: %s" % th['KF_gt_one_refuted'])
    print("      T2  rho<0 => 1/3 < Delta < 1:  %s" % (th['T2_gt_third'] and th['T2_lt_one']))
    print()
    print("  3. THE GENERAL BOUND, AND THE THERMAL CONTROL")
    print("      T1  Delta' >= 1/2 for every zero-mean Gaussian state: %s  (guard fires: %s)"
          % (th['T1'], th['T1_guard_fails']))
    print("      Casimir   rho = %s   xi = %s   Delta' = %s   Delta = %s"
          % (cas['rho'], [sp.simplify(p / cas['rho']) for p in cas['p']], cas['Dprime'], cas['Delta']))
    print("      thermal   rho = %s   p/rho = %s   Delta' = %s   Delta = %s"
          % (thm['rho'], [sp.simplify(p / thm['rho']) for p in thm['p']], thm['Dprime'], thm['Delta']))
    print()
    print("  THE POINTWISE Delta DOES NOT DISCRIMINATE NEGATIVE ENERGY.")
    print("  This file does not price the corridor's fluctuation demand.  No ledger row moves.\n")


def selftest():
    sp, z3 = _need()
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-62s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("fluctuation.py --selftest\n")
    m = single_mode(sp)
    s, c = m['s'], m['c']
    v = vacuum_plus_two(sp, m)
    chk("(2.16) middle line is exact", is_zero(sp, v['mid'] - v['rho'], s, c), KF_216_MIDDLE_IS_EXACT)
    chk("(2.16) final line is exact", is_zero(sp, v['final'] - v['rho'], s, c), KF_216_FINAL_IS_EXACT)
    chk("  and is exactly half of it", sp.simplify(v['final'] / v['rho']), sp.Rational(1, 2))
    chk("exact <:T^2:> vac+2 is 12 K^2 eps^2/(1+eps^2)",
        sp.simplify(v['T2'] - 12 * m['K']**2 * m['eps']**2 / (1 + m['eps']**2)), 0)
    chk("(3.7) is exact", is_zero(sp, v['kf37'] - v['T2'], s, c), KF_37_IS_EXACT)
    chk("exact Delta = 1 - (2eps - sqrt2 cos2th)^2/(3(1+eps^2))",
        sp.simplify(v['delta'] - v['delta_closed']), 0)
    chk("(3.8) is exact", is_zero(sp, v['kf38'] - v['delta'], s, c), KF_38_IS_EXACT)
    at = {m['eps']: sp.Rational(*VACPLUS2_EPS_WITNESS), m['z']: 1}
    chk("witness: exact Delta at eps=1/10, theta=0 is 0.5134",
        round(float(v['delta'].subs(at)), 4), 0.5134)
    chk("witness: KF (3.8) there gives 2.0118", round(float(v['kf38'].subs(at)), 4), 2.0118)
    chk("witness point has rho < 0", float(v['rho'].subs(at).subs(m['K'], 1)) < 0, True)

    q = squeezed(sp, m)
    chk("(3.18) is exact", is_zero(sp, q['kf318'] - q['rho'], s, c), KF_318_IS_EXACT)
    chk("(3.19) is exact", is_zero(sp, q['kf319'] - q['T2'], s, c), KF_319_IS_EXACT)
    chk("(3.22) is exact", is_zero(sp, q['kf322'] - q['rho_sv'], s, c), KF_322_IS_EXACT)
    chk("(3.23) is exact", is_zero(sp, q['kf323'] - q['T2_sv'], s, c), KF_323_IS_EXACT)
    chk("squeezed vacuum: <:T^2:> = 3 rho^2 identically",
        is_zero(sp, q['T2_sv'] - 3 * q['rho_sv']**2, s, c), True)
    # Evaluated on the state, at one point of each sign -- not the constant 1 - 1/3.
    sv_pts = []
    for rr, zz in ((sp.Rational(3, 10), sp.exp(sp.I * sp.Rational(2, 5))),       # theta = 0.2
                   (sp.Rational(3, 10), sp.exp(sp.I * sp.pi * sp.Rational(19, 20)))):
        at_sv = {m['K']: 1, s: sp.sinh(rr), c: sp.cosh(rr), m['z']: zz}
        rv = complex(sp.N(q['rho_sv'].subs(at_sv), 40))
        dv = 1 - rv**2 / complex(sp.N(q['T2_sv'].subs(at_sv), 40))
        sv_pts.append((rv.real > 0, round(dv.real, 12)))
    chk("  so Delta = 2/3 at a rho>0 point AND a rho<0 point",
        sorted(sv_pts), [(False, round(2 / 3, 12)), (True, round(2 / 3, 12))])
    chk("(3.21) coherent state: <:T^2:> = rho^2, Delta = 0",
        is_zero(sp, q['T2_cs'] - q['rho_cs']**2, s, c), KF_321_IS_EXACT)

    # ---- the independent control on method (G): squeezed vacuum as a Fock series
    import mpmath as mpm
    mpm.mp.dps = 50
    r, theta = mpm.mpf('0.7'), mpm.mpf('1.1')
    t = mpm.tanh(r)
    nmax = 160
    cs = [mpm.mpf(0)] * (nmax + 1)
    for k in range(nmax // 2 + 1):
        cs[2 * k] = (-t)**k * mpm.sqrt(mpm.factorial(2 * k)) / (2**k * mpm.factorial(k)) / mpm.sqrt(mpm.cosh(r))

    def low(vv):
        return [mpm.sqrt(j + 1) * vv[j + 1] for j in range(len(vv) - 1)] + [0]

    def mom(mm, nn):
        am, an = cs[:], cs[:]
        for _ in range(mm):
            am = low(am)
        for _ in range(nn):
            an = low(an)
        return mpm.fsum(x * y for x, y in zip(am, an))
    zz = mpm.e**(2j * theta)
    T2f = (6 * mom(2, 2) - 4 * zz * mom(1, 3) - 4 / zz * mom(3, 1) + zz**2 * mom(0, 4) + zz**-2 * mom(4, 0))
    subs = {m['K']: 1, s: float(mpm.sinh(r)), c: float(mpm.cosh(r)), m['z']: complex(zz)}
    T2g = complex(sp.N(q['T2_sv'].subs(subs), 30))
    chk("CONTROL: Fock series agrees with Gaussian moments to 1e-12",
        abs(complex(T2f) - T2g) < 1e-12 * abs(T2g), True)
    T2kf = complex(sp.N(q['kf323'].subs(subs), 30))
    chk("  and the printed (3.23) does not", abs(complex(T2f) - T2kf) > 1e-3 * abs(T2g), True)

    # ---- Casimir, and the thermal positive control
    L, beta = sp.symbols('L beta', positive=True)
    cas = image_stress(sp, lambda n: (0, n * L))
    chk("Casimir rho = -pi^2/(90 L^4)  [KF (3.33)]", sp.simplify(cas['rho'] + sp.pi**2 / (90 * L**4)), 0)
    chk("Casimir xi = (-1, -1, 3)", [sp.simplify(p / cas['rho']) for p in cas['p']], [-1, -1, 3])
    chk("Casimir G is diagonal", all(cas['G'][A, B] == 0 for A in range(4) for B in range(4) if A != B), True)
    chk("Casimir Delta' = 6", cas['Dprime'], 6)
    chk("Casimir Delta = 6/7", cas['Delta'], sp.Rational(6, 7))
    chk("(3.41) printed 1/2 holds",
        sp.simplify(cas['G'][0, 0]**2 - (cas['rho'] + sum(cas['p']))**2 / 2) == 0, False)
    chk("  and 1/4 holds, so it is typographical",
        sp.simplify(cas['G'][0, 0]**2 - (cas['rho'] + sum(cas['p']))**2 / 4) == 0, KF_341_HALF_IS_TYPOGRAPHICAL)
    thm = image_stress(sp, lambda n: (sp.I * n * beta, 0))
    chk("CONTROL: thermal rho = pi^2/(30 beta^4), Stefan-Boltzmann",
        sp.simplify(thm['rho'] - sp.pi**2 / (30 * beta**4)), 0)
    chk("CONTROL: thermal p = rho/3", [sp.simplify(p / thm['rho']) for p in thm['p']],
        [sp.Rational(1, 3)] * 3)
    chk("thermal radiation Delta' = 2/3", thm['Dprime'], sp.Rational(2, 3))
    chk("thermal radiation Delta = 2/5 -- fails KF's criterion too", thm['Delta'], sp.Rational(2, 5))
    chk("so the pointwise Delta does not discriminate the sign",
        POINTWISE_DELTA_DISCRIMINATES_SIGN, thm['Delta'] < sp.Rational(1, 3))

    # ---- the proofs
    th = theorems(z3)
    chk("T1 PROVED: Delta' >= 1/2 for every zero-mean Gaussian state", th['T1'], True)
    chk("T1 equality only at G = (rho/2) I", th['T1_equality'], True)
    chk("T1 does not need G diagonal", BOUND_NEEDS_DIAGONAL_G, False)
    chk("VACUITY GUARD: the stronger false bound is refuted", th['T1_guard_fails'], True)
    chk("T2 PROVED: vac+2, rho<0 => Delta > 1/3", th['T2_gt_third'], True)
    chk("T2 PROVED: vac+2, rho<0 => Delta < 1", th['T2_lt_one'], True)
    chk("KF's 'rho<0 => Delta>1' REFUTED", th['KF_gt_one_refuted'], True)
    chk("  recorded", KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1, False)
    chk("their qualitative conclusion survives", KF_QUALITATIVE_CONCLUSION_SURVIVES, True)

    # ---- refusals
    chk("the journal version is NOT claimed read", JOURNAL_VERSION_READ, False)
    chk("the corridor is NOT priced", PRICES_THE_CORRIDOR, False)
    chk("no ledger row moves", LEDGER_ROW_MOVES, False)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        print("  SELFTEST FAILED: %d" % len(fails))
        for f in fails:
            print("    %s: got %r want %r" % f)
        return 1
    print("  SELFTEST OK")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
