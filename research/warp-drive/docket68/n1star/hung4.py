"""hung4.py -- the four-dimensional control of W7: Hung's Proposition 4.2 recomputed.

Hung (arXiv:1909.06733, section 4.1 and Appendix C) writes the harmonic-gauge linearised Einstein equations about
Schwarzschild, for an even mode l, as box H = A H + B H + U H in seven components H1..H7: H1 = (h_tt + f^2 h_rr)/2
+ (M/r) trs h, H2 = trs h / 2, H3 = (h_tt/f - f h_rr)/2, H6 = f h_tr + (M/r) trs h, H4 = f h_rA, H7 = h_tA,
H5 = hhat_AB/sqrt2, with f = 1 - 2M/r, trs h = r^-2 gamma^AB h_AB, and A zeroth order, B first order angular (a number
at the mode) and U first order along L = d_t + f d_r in rows 6 and 7 only.  Appendix C derives each row as a
combination of the Lichnerowicz components LW = box h + 2 Riem h (ME1-ME7 at the mode) and of the harmonic gauge
condition (HG1-HG3): the gauge condition removes the first-order terms the Lichnerowicz operator alone carries.

This instrument recomputes the seven rows from the metric with the same instrument that wavegauge5.py W7 runs on
five-dimensional Tangherlini (C1), and holds them against the printed rows (C2).  What it finds, READ against
computed:
  rows 1-5 reproduce the printed A and B rows (B at the mode: D1 -> -k^2/r^2, D1* -> -1, D2 -> -(k^2 - 2)/(2 r^2),
  D2* -> -1 on the normalised bases), with no first-order term, and row 7 reproduces the printed row and the printed
  U row 7, (2M/r^2) f^-1 nabla_L (H7 - H4) ("nabla_L . r" read as r nabla_L), once the printed "(ME3)" of its
  combination is read as (HG3), the angular component of the gauge condition, which is what balances its first-order
  terms; row 6 reproduces the printed A, B and U rows (with "nabla_L . r" read as nabla_L(r .)) once its printed
  combination (1 - 2M/r)(ME2) + (M/r^2)(ME6) + (4M(r - 2M)/r^2)(HG2) is read as (1 - 2M/r)(ME3) + (M/r^3)(ME6) +
  (4M(r - 2M)/r^3)(HG2), the component with one t index and the powers of r the dimensions require; the printed
  combination leaves second-order terms.  The control (--mutants) uses the printed row-6 combination and a
  sign-flipped gauge admixture, both caught.  Nothing here is a finding about Hung's theorem: the rows are his, the
  combinations print with two misprints, and the instrument that reproduces them is the one W7 runs.

Conventions.  The mode ansatz at symbolic k^2 = l(l+1): h_tt = A S, h_tr = B S, h_rr = C S, h_tA = D S_A,
h_rA = E S_A, h_AB = r^2 (K S gamma_AB + G S_AB), S'' + cot th S' = -k^2 S, S_AB = D_A D_B S/k^2 + gamma_AB S/2
(so Hung's H0 = A/f, H1 = B, H2 = f C, K = K, h0 = D, h1 = E, G_Hung = G/(2 k^2)), the angle evaluated exactly at two
Pythagorean points (cos, sin) = (3/5, 4/5), (5/13, 12/13) after the harmonic's ODE is applied; the operators
box^0_l = -f^-1 d_t^2 + f d_r^2 + (2/r)(1 - M/r) d_r - l(l+1)/r^2, box^1_l = r box^0_l r^-1 + 1/r^2,
box^2_l = r^2 box^0_l r^-2 + 4/r^2 are (C.1)-(C.3).

python3 hung4.py [--selftest | --mutants]   (about two minutes; --verbose lists every row)
"""
import sys
import time

import sympy as sp

t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]
Mm = sp.symbols("M", positive=True)
k = sp.symbols("k", positive=True)
f = 1 - 2*Mm/r
fp = sp.diff(f, r)
cs, sn = sp.cos(th), sp.sin(th)
g = sp.diag(-f, 1/f, r**2, r**2*sn**2)
gi = g.inv()
N = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                         for d in range(N))/2) for c in range(N)] for b in range(N)] for a in range(N)]
_R = {}
S = sp.Function("S")(th)
Sp = sp.diff(S, th)
RULE2 = -sp.cot(th)*Sp - k**2*S
PYTH = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13))]
s0, s1 = sp.symbols("s0 s1")
D = sp.diff


def riem(a, b, c, d):
    if (a, b, c, d) not in _R:
        _R[(a, b, c, d)] = sp.simplify(D(Gam[a][d][b], X[c]) - D(Gam[a][c][b], X[d])
                                       + sum(Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b] for e in range(N)))
    return _R[(a, b, c, d)]


def riem_low(a, e, b, ff):
    return sp.simplify(sum(g[a, gg]*riem(gg, e, b, ff) for gg in range(N) if g[a, gg] != 0))


def Dh(h, c, a, b):
    return D(h[a, b], X[c]) - sum(Gam[e][c][a]*h[e, b] + Gam[e][c][b]*h[a, e] for e in range(N))


def red(e):
    e = e.doit()
    for _ in range(8):
        ds = [d for d in e.atoms(sp.Derivative) if d.expr == S and d.derivative_count >= 2]
        if not ds:
            break
        e = e.xreplace({d: D(RULE2, th, d.derivative_count - 2) for d in ds}).doit()
    return e


def at_angle(e, cs0, sn0):
    for _ in range(3):
        rep = {}
        for atom in e.atoms(sp.cos, sp.sin, sp.tan, sp.cot):
            if atom.args[0] != th:
                rep[atom] = sp.expand_trig(atom)
        rep.update({sp.tan(th): sn/cs, sp.cot(th): cs/sn})
        e = e.xreplace(rep)
    e = e.xreplace({cs: cs0, sn: sn0})
    assert not e.has(th), e
    return e


def lin(e, V):
    """e linear in V and their derivatives: {(j, nt, nr): coefficient}, zero coefficients dropped"""
    e = sp.expand(e)
    rep, keys = {}, {}
    for dd in e.atoms(sp.Derivative):
        if dd.expr in V:
            nt = sum(c for v_, c in dd.variable_count if v_ == t)
            nr = sum(c for v_, c in dd.variable_count if v_ == r)
            s_ = sp.Symbol("D%d_%d%d" % (V.index(dd.expr), nt, nr))
            rep[dd] = s_
            keys[s_] = (V.index(dd.expr), nt, nr)
    for j, v_ in enumerate(V):
        s_ = sp.Symbol("D%d_00" % j)
        rep[v_] = s_
        keys[s_] = (j, 0, 0)
    ee = sp.expand(e.xreplace(rep))
    syms = [q for q in rep.values() if ee.has(q)]
    out = {}
    if syms:
        P = sp.Poly(ee, *syms)
        assert P.total_degree() <= 1
        for m, c in zip(P.monoms(), P.coeffs()):
            idx = [i for i, e_ in enumerate(m) if e_ == 1]
            c = sp.cancel(c)
            if idx and c != 0:
                out[keys[syms[idx[0]]]] = c
    return out


def ang(e, which, V):
    """the coefficient of S (which 0) or S' (which 1) in e; the other vanishes; the angle drops out"""
    out = []
    for cs0, sn0 in PYTH:
        ee = at_angle(red(e).xreplace({Sp: s1}).xreplace({S: s0}), cs0, sn0)
        rep = {}
        for dd in ee.atoms(sp.Derivative):
            if dd.expr in V:
                nt = sum(c for v_, c in dd.variable_count if v_ == t)
                nr = sum(c for v_, c in dd.variable_count if v_ == r)
                rep[dd] = sp.Symbol("D%d_%d%d" % (V.index(dd.expr), nt, nr))
        for j, v_ in enumerate(V):
            rep[v_] = sp.Symbol("D%d_00" % j)
        ee = sp.expand(ee.xreplace(rep))
        syms = [q for q in rep.values() if ee.has(q)]
        P = sp.Poly(ee, s0, s1, *syms)
        other, mine = 0, 0
        for m, c in zip(P.monoms(), P.coeffs()):
            mono = sp.Mul(*[q**e_ for q, e_ in zip(syms, m[2:])])
            if m[(which + 1) % 2] == 1:
                other += sp.cancel(c)*mono
            elif m[which] == 1:
                mine += sp.cancel(c)*mono
        assert sp.cancel(other) == 0, "the other angular factor survives"
        out.append(mine)
    assert sp.cancel(sp.expand(out[0] - out[1])) == 0, "angle dependence"
    back = {sp.Symbol("D%d_%d%d" % (j, nt, nr)): (D(V[j], *([t]*nt + [r]*nr)) if nt + nr else V[j])
            for j in range(len(V)) for nt in range(3) for nr in range(3)}
    return out[0].xreplace(back)


def mode_system():
    """the Lichnerowicz components ME1-ME7 and gauge components HG1-HG3 at the mode, in the coordinate functions"""
    A_, B_, C_, D_, E_, K_, G_ = V = [sp.Function(nm)(t, r) for nm in ("A", "B", "C", "D", "E", "K", "G")]
    gam = sp.diag(1, sn**2)
    DDS = sp.diag(D(S, th, 2), sn*cs*Sp)
    SAB = DDS/k**2 + gam*S/2
    h = sp.zeros(N)
    h[0, 0] = A_*S; h[0, 1] = h[1, 0] = B_*S; h[1, 1] = C_*S
    h[0, 2] = h[2, 0] = D_*Sp; h[1, 2] = h[2, 1] = E_*Sp
    for i in range(2):
        h[2 + i, 2 + i] = r**2*(K_*S*gam[i, i] + G_*SAB[i, i])
    DhT = [[[Dh(h, c, a, b) for b in range(N)] for a in range(N)] for c in range(N)]

    def DDh(d, c, a, b):
        return (D(DhT[c][a][b], X[d]) - sum(Gam[e][d][c]*DhT[e][a][b] + Gam[e][d][a]*DhT[c][e][b]
                                            + Gam[e][d][b]*DhT[c][a][e] for e in range(N)))
    E = {}
    for (a, b) in [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (3, 3)]:
        box = sum(gi[c, d]*DDh(d, c, a, b) for c in range(N) for d in range(N) if gi[c, d] != 0)
        rh = sum(gi[c, e]*gi[d, ff]*riem_low(a, e, b, ff)*h[c, d] for c in range(N) for d in range(N)
                 for e in range(N) for ff in range(N) if gi[c, e] != 0 and gi[d, ff] != 0 and h[c, d] != 0)
        E[(a, b)] = box + 2*rh
    trh = sum(gi[a, b]*h[a, b] for a in range(N) for b in range(N))
    G = [sum(gi[a, c]*Dh(h, c, a, b) for a in range(N) for c in range(N) if gi[a, c] != 0) - D(trh, X[b])/2
         for b in range(N)]
    trE = (E[(2, 2)] + E[(3, 3)]/sn**2)/r**2                      # trs LW
    TF = E[(2, 2)] - r**2*trE/2                                   # hat LW_thth = r^2 eG S_thth
    outs = []
    for cs0, sn0 in PYTH:
        ee = at_angle(red(TF).xreplace({Sp: s1}).xreplace({S: s0}), cs0, sn0)
        a0 = sp.expand(ee.xreplace({s1: 0}).xreplace({s0: 1}))/(r**2*sp.Rational(-1, 2))
        a1 = sp.expand(ee.xreplace({s0: 0}).xreplace({s1: 1}))/(r**2*(-(cs0/sn0)/k**2))
        assert all(c == 0 for c in lin(sp.expand(a0 - a1), V).values()), "traceless part not proportional to S_AB"
        outs.append(a0)
    assert all(c == 0 for c in lin(sp.expand(outs[0] - outs[1]), V).values())
    eG = outs[0]
    ME = {1: ang(E[(0, 0)], 0, V), 2: ang(E[(1, 1)], 0, V), 3: ang(E[(0, 1)], 0, V), 4: ang(E[(0, 2)], 1, V),
          5: ang(E[(1, 2)], 1, V), 6: r**2*ang(trE, 0, V), 7: r**2*eG/k**2}
    HG = {1: ang(G[0], 0, V), 2: ang(G[1], 0, V), 3: ang(G[2], 1, V)}
    return V, ME, HG


def hung_rows(V, ME, HG, row6="corrected", gauge_sign=1):
    """Hung's seven combinations; returns {row: (second-order, first-order, zeroth-order)} in his H's"""
    A_, B_, C_, D_, E_, K_, G_ = V
    H0, H1c, H2c, Kc, h0, h1, GH = A_/f, B_, f*C_, K_, D_, E_, G_/(2*k**2)
    Hs = {1: f*(H0 + H2c)/2 + 2*Mm/r*Kc, 2: Kc, 3: (H0 - H2c)/2, 4: f*h1, 5: sp.sqrt(2)*r**2*GH,
          6: f*H1c + 2*Mm/r*Kc, 7: h0}
    box0 = lambda u: -D(u, t, 2)/f + f*D(u, r, 2) + 2/r*(1 - Mm/r)*D(u, r) - k**2/r**2*u     # noqa: E731
    box1 = lambda u: r*box0(u/r) + u/r**2                                                      # noqa: E731
    box2 = lambda u: r**2*box0(u/r**2) + 4*u/r**2                                              # noqa: E731
    gs = gauge_sign
    six = (f*ME[2] + Mm/r**2*ME[6] + gs*4*Mm*(r - 2*Mm)/r**2*HG[2] if row6 == "printed"
           else f*ME[3] + Mm/r**3*ME[6] + gs*4*Mm*(r - 2*Mm)/r**3*HG[2])
    combos = {1: (box0, ME[1]/2 + Mm/r**3*ME[6] + f**2*ME[2]/2 + gs*4*Mm*(r - 2*Mm)/r**3*HG[2]),
              2: (box0, ME[6]/(2*r**2)),
              3: (box0, ME[1]/(2*f) - f*ME[2]/2),
              4: (box1, f*ME[5] + gs*2*Mm/r**2*HG[3]),
              5: (box2, ME[7]/sp.sqrt(2)),
              6: (box0, six),
              7: (box1, ME[4] + gs*2*Mm/r**2*HG[3])}
    hsym = [sp.Function("H%d" % i)(t, r) for i in range(1, 8)]
    sol = sp.solve([sp.Eq(expr, hsym[i - 1]) for i, expr in Hs.items()], list(V), dict=True)[0]
    out = {}
    for i, (bx, cmb) in combos.items():
        res = (bx(Hs[i]) - cmb).subs(sol).doit()
        parts = lin(res, hsym)
        out[i] = ({kk: v for kk, v in parts.items() if kk[1] + kk[2] == 2},
                  {kk: v for kk, v in parts.items() if kk[1] + kk[2] == 1},
                  {kk[0]: v for kk, v in parts.items() if kk[1] + kk[2] == 0})
    return out


def printed():
    """Hung's A and B rows at the mode (p. 19), as box H_i = sum_j coeff_ij H_j; s = r/M; B at the mode with
    D1 -> -k^2/r^2, D1* -> -1, D2 -> -(k^2 - 2)/(2 r^2), D2* -> -1"""
    s = r/Mm
    lam2 = (k**2 - 2)/2                                           # Hung's lambda: l(l+1) = 2 lambda + 2
    P = {1: {0: 2/r**2*(1 - 6/s), 1: -2/r**2*(1 - 8/s + 10/s**2), 2: -2/r**2*(1 - 10/s + 20/s**2),
             3: 2/r*(1 - 6/s)*(-k**2/r**2)},
         2: {0: -2/r**2, 1: 2/r**2*(1 - 2/s), 2: 2/r**2*(1 - 4/s), 3: -2/r*(-k**2/r**2)},
         3: {0: -2/r**2, 1: 2/r**2*(1 - 2/s), 2: 2/r**2*(1 - 4/s), 3: -2/r*(-k**2/r**2)},
         4: {3: 2/r**2*(sp.Rational(5, 2) - 9/s), 0: 2/r*(-1), 1: -2/r*(-1), 2: 2/r*(-1 + 3/s)*(-1),
             4: 2/r*sp.sqrt(2)*(1 - 3/s)*(-lam2/r**2)},
         5: {4: 2/r**2, 3: 2/r*sp.sqrt(2)*(-1)},
         6: {0: 2/r**2*(-4/s), 1: 2/r**2*(4/s - 6/s**2), 2: 2/r**2*(6/s - 16/s**2), 5: 2/r**2*(1 - 2/s),
             3: 2/r*(-4/s)*(-k**2/r**2), 6: 2/r*(1 - 2/s)*(-k**2/r**2)},
         7: {3: 2/r**2*(-2/s), 6: 2/r**2*(sp.Rational(1, 2) - 3/s), 1: 2/r*(-2/s)*(-1), 2: 2/r*(1/s)*(-1),
             4: 2/r*(-sp.sqrt(2)/s)*(-lam2/r**2), 5: 2/r*(-1)}}
    return P


def c1(control=0, verbose=False):
    """C1: the seven rows, as Appendix C combines them, have the scalar principal part and no first-order term but
    the U rows 6 and 7"""
    chk = Checklist(verbose, quiet=control != 0)
    V, ME, HG = mode_system()
    rows = hung_rows(V, ME, HG, row6="printed" if control == 1 else "corrected", gauge_sign=-1 if control == 2 else 1)
    for i in range(1, 8):
        sec, first, zero = rows[i]
        chk("row %d: the principal part is box^j_l H%d (no second-order remainder)" % (i, i), not sec)
        if i in (6, 7):
            c = 4*Mm/(r**2*f) if i == 6 else 2*Mm/(r**2*f)
            jj = (0, 5) if i == 6 else (3, 6)
            want = {(jj[0], 1, 0): -c, (jj[1], 1, 0): c, (jj[0], 0, 1): -c*f, (jj[1], 0, 1): c*f}
            good = set(first) == set(want) and all(sp.cancel(first[q] - want[q]) == 0 for q in want)
            chk("row %d: the first-order terms are (%dM/r^2) f^-1 nabla_L (H%d - H%d), the printed U"
                % (i, 4 if i == 6 else 2, 7 if i == 7 else 6, 4 if i == 7 else 1), good)
        else:
            chk("row %d: no first-order term" % i, not first)
    return chk.ok, rows


def c2(control=0, verbose=False):
    """C2: the zeroth-order rows against the printed A and B rows at the mode"""
    chk = Checklist(verbose, quiet=control != 0)
    ok, rows = c1(control=0, verbose=False)
    P = printed()
    for i in range(1, 8):
        zero = rows[i][2]
        want = dict(P[i])
        if i == 6:                                   # "nabla_L . r" read as nabla_L (r .): adds (4M/r^3)(H6 - H1)
            want[0] = want[0] - 4*Mm/r**3
            want[5] = want[5] + 4*Mm/r**3
        if control == 1:
            want[i - 1] = want[i - 1] + 1/r**2
        good = set(zero) == set(want) and all(sp.cancel(zero[j] - want[j]) == 0 for j in want)
        chk("row %d: the zeroth-order terms are the printed A and B row at the mode%s"
            % (i, " (with nabla_L (r .) in U)" if i == 6 else ""), good)
    return chk.ok


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


def c1ok(control=0, verbose=False):
    return c1(control, verbose)[0]


CHECKS = [("C1 Hung's seven rows: scalar principal parts, first-order terms only the two U rows", c1ok, 2),
          ("C2 the zeroth-order rows are the printed A and B at the mode", c2, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=kk) for kk in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"hung4.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for kk in range(1, nc + 1):
            total += 1
            m = fn(control=kk)
            caught += (not m)
            print(f"mutant {kk} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"hung4.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
