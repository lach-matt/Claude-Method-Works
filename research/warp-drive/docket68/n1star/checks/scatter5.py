"""scatter5.py -- SETTLE-GLAM5 round 2, R2: the nonlinear scattering problem on the wedge W, on top of Lemma 5.1,
and what the weight a < 1/2 of (N2) does and does not give.

Setting of round 1 section 5: W = D^-(S), N = {v = v1}, Tangherlini g_(b_0) in the record's gauge, weight
w = (-u)^(2a), u = t - r, so w ~ r^(2a) on W near spatial infinity; E_w the weighted energy, density
r^(2a) |d phi|^2 r^3 dr domega on the slices.

  S1 (exact and computed) the weighted radial Sobolev inequality behind the bootstrap: for f decaying on [R, oo),
     R^(2a+3) f(R)^2 <= 2 ||r^(a+3/2) f|| ||r^(a+3/2) f_r|| (L^2(dr)), so with H^2(S^3) in L^oo and the commuted
     energies (d_t, the rotations; d_r from the equation), |d h| <= C r^(-3/2-a) E^(1/2). Exact on f = r^-b, b > a + 2,
     and at 200 random f = r^-b (1 + c sin(k r)) by quadrature. Control: without the f_r factor the inequality fails
     (bumps of width eps: the ratio grows like 1/eps).
  S2 (exact) the bootstrap closes for every a > -1/2: the error kernel int_(-oo)^(t_S) (v1 - t)^(-3/2-a) dt =
     (v1 - t_S)^(-1/2-a)/(1/2 + a), and E <= E_0 exp(C eps K_a) <= 2 E_0 once C eps K_a <= log 2. Control: in 3 + 1
     dimensions (radiation fields at r^-1, |d h| <= r^(-1-a)) the kernel at a = 0 diverges.
  S3 (exact) the data on N: the record's energy bound lam^K' t^(-1/2) per annulus gives a dyadic flux sum
     sum_k 2^(k(2a - 1)), finite exactly for a < 1/2. Control: a = 1/2 diverges.
  S4 (exact) the obstruction: a field with a radiation field at past null infinity, phi = r^(-3/2) F(s) Y_l,
     s = (v - v1)/r, F = 2F1(3/2 + l, -1/2 - l; 1; s/2): (a) it solves box phi = 0; (b) r^(3/2) phi -> F(0) = 1 at
     past null infinity, at every v >= v1 (a radiation field, constant in v: incoming); (c) its flux through N with
     weight a is finite exactly for a < 1/2 and (d) its cap energy on {t = T} cap W tends to 0 as T -> -oo exactly
     for a < 1/2: so the energy class of weight a < 1/2 does not exclude incoming radiation; (e) on a slice t = c it
     reaches spatial infinity as rho^(3/2) T_(3/2)(l), T_(3/2)(l) != 0, with d_t^2 phi = rho^(7/2) F''(1) Y_l + ...,
     F''(1) != 0 (l <= 20; Gauss's second theorem and no pole, deduced for every l): a curvature term rho^(7/2),
     which III.K's class (either data class) excludes. Control: at a = 1/2 the flux and the cap energy diverge.
  S5 (exact) gauge cannot remove it: the linearized Riemann tensor of a pure-gauge perturbation d_a xi_b + d_b xi_a
     of 4 + 1 Minkowski space vanishes identically (generic xi, all 50 independent components checked at a point
     with random polynomial xi). Control: h = f(t, x1) dx2^2 (not pure gauge) has nonzero linearized Riemann tensor.
Labels: computed (exact, sympy; mpmath at 30 digits).

    python3 checks/scatter5.py
"""
import itertools
import random
import sys

import mpmath as mp
import sympy as sp

FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def s1():
    print("S1  the weighted radial Sobolev inequality")
    r, R = sp.symbols("r R", positive=True)
    ok = True
    for a in (sp.Rational(1, 4), sp.Rational(9, 20), sp.Rational(11, 4)):
        for b in (a + sp.Rational(21, 10), a + 3, a + 5):
            f = r**(-b)
            lhs = R**(2*a + 3)*f.subs(r, R)**2
            n1 = sp.integrate(r**(2*a + 3)*f**2, (r, R, sp.oo))
            n2 = sp.integrate(r**(2*a + 3)*sp.diff(f, r)**2, (r, R, sp.oo))
            ratio = sp.simplify(lhs**2/(4*n1*n2))
            ok = ok and ratio.is_number and ratio <= 1
    check("S1a R^(2a+3) f(R)^2 <= 2 ||r^(a+3/2) f|| ||r^(a+3/2) f_r|| on f = r^-b, exact", ok)
    mp.mp.dps = 30
    random.seed(7)
    worst = mp.mpf(0)
    for _ in range(200):
        a = mp.mpf(random.choice([0.1, 0.3, 0.45, 2.6, 2.9]))
        b = a + 2 + mp.mpf(random.uniform(0.2, 2.0))
        c, k = mp.mpf(random.uniform(-0.9, 0.9)), mp.mpf(random.uniform(0.5, 4))
        R0 = mp.mpf(random.uniform(1, 5))
        f = lambda x: x**(-b)*(1 + c*mp.sin(k*x))
        fr = lambda x: mp.diff(f, x)
        n1 = mp.quad(lambda x: x**(2*a + 3)*f(x)**2, [R0, R0 + 10, R0 + 100, mp.inf])
        n2 = mp.quad(lambda x: x**(2*a + 3)*fr(x)**2, [R0, R0 + 10, R0 + 100, mp.inf])
        worst = max(worst, R0**(2*a + 3)*f(R0)**2/(2*mp.sqrt(n1*n2)))
    check("S1b 200 random f = r^-b (1 + c sin kr): ratio <= 1", worst <= 1, "max ratio " + mp.nstr(worst, 6))
    ratios = []
    for eps in (mp.mpf("0.1"), mp.mpf("0.01"), mp.mpf("0.001")):
        bump = lambda x: mp.exp(-((x - 2)/eps)**2)
        n1 = mp.quad(lambda x: x**3*bump(x)**2, [2 - 10*eps, 2, 2 + 10*eps])
        ratios.append(2**3*bump(2)**2/n1)
    check("S1c control: without the f_r factor (sup by ||r^(3/2) f|| alone) the ratio is unbounded",
          ratios[2] > 50*ratios[0], str([mp.nstr(x, 4) for x in ratios]))


def s2():
    print("S2  the bootstrap kernel")
    a = sp.Symbol("a", positive=True)
    L, tt, C, eps, E0 = sp.symbols("L tt C epsilon E_0", positive=True)
    K = sp.integrate(tt**(-sp.Rational(3, 2) - a), (tt, L, sp.oo), conds="none")
    Kn = sp.gammasimp(sp.powsimp(K, force=True))
    check("S2a int_L^oo (v1 - t)^(-3/2-a) = L^(-1/2-a)/(1/2+a), finite for every a > 0 (and a > -1/2)",
          sp.simplify(sp.powsimp(Kn - L**(-sp.Rational(1, 2) - a)/(sp.Rational(1, 2) + a), force=True)) == 0,
          str(Kn))
    closes = sp.simplify(sp.exp(C*eps*K).subs(eps, sp.log(2)/(C*K)) - 2) == 0
    check("S2b E <= E_0 exp(C eps K_a) = 2 E_0 at eps = log 2/(C K_a): the bootstrap improves for smaller eps", closes)
    K3 = sp.integrate(tt**(-1), (tt, L, sp.oo))
    check("S2c control: n = 3 (|d h| ~ r^(-1-a)) at a = 0: the kernel diverges", K3 == sp.oo, str(K3))


def s3():
    print("S3  the weighted flux of e on N from the record's energy decay")
    k = sp.Symbol("k", integer=True, nonnegative=True)
    res = {}
    for a in (sp.Rational(1, 4), sp.Rational(49, 100), sp.Rational(1, 2), sp.Rational(3, 4)):
        res[a] = sp.summation(sp.Integer(2)**(k*(2*a - 1)), (k, 0, sp.oo))
    check("S3a sum_k 2^(k(2a-1)) finite at a = 1/4, 49/100", res[sp.Rational(1, 4)].is_finite and
          res[sp.Rational(49, 100)].is_finite, str(res[sp.Rational(1, 4)]))
    check("S3b control: diverges at a = 1/2 and a = 3/4", res[sp.Rational(1, 2)] == sp.oo and
          res[sp.Rational(3, 4)] == sp.oo)


def box(F, r, v, kappa):
    return 2*sp.diff(F, v, r) + 3*sp.diff(F, v)/r + sp.diff(F, r, 2) + 3*sp.diff(F, r)/r - kappa*F/r**2


def s4():
    print("S4  a radiation field is invisible to the weight a < 1/2")
    v, r, v1, s = sp.symbols("v r v1 s", real=True)
    rp = sp.Symbol("rp", positive=True)
    p = sp.Rational(3, 2)
    ok_eq = True
    for l in range(0, 4):
        F = sp.hyper([p + l, p - l - 2], [p - sp.Rational(1, 2)], s/2)
        Fp = sp.simplify(sp.hyperexpand(F))
        phi = r**(-p)*Fp.subs(s, (v - v1)/r)
        res = sp.simplify(box(phi, r, v, l*(l + 2)).subs(r, rp))
        ok_eq = ok_eq and res == 0
    check("S4a r^(-3/2) 2F1(3/2+l, -1/2-l; 1; s/2) Y_l solves box = 0 (l = 0..3, exact)", ok_eq)
    lim = [sp.limit(sp.hyperexpand(sp.hyper([p + l, p - l - 2], [1], s/2)), s, 0) for l in range(4)]
    check("S4b r^(3/2) phi -> F(0) = 1 at past null infinity (s -> 0 at fixed v), every v: incoming radiation",
          lim == [1, 1, 1, 1], str(lim))
    a = sp.Symbol("a", positive=True)
    R, Tm = sp.symbols("R Tm", positive=True)
    flux = {}
    cap = {}
    for aa in (sp.Rational(1, 4), sp.Rational(9, 20), sp.Rational(1, 2)):
        # on N: |d_r phi|^2 + r^-2 |grad phi|^2 ~ r^-5; on the cap t = T: |d phi|^2 ~ r^-5 (s bounded there)
        flux[aa] = sp.integrate(rp**(2*aa)*rp**-5*rp**3, (rp, R, sp.oo))
        cap[aa] = sp.integrate(rp**(2*aa)*rp**-5*rp**3, (rp, Tm, sp.oo))
    fin = all(flux[x].is_finite for x in (sp.Rational(1, 4), sp.Rational(9, 20)))
    to0 = all(sp.limit(cap[x], Tm, sp.oo) == 0 for x in (sp.Rational(1, 4), sp.Rational(9, 20)))
    check("S4c-d flux through N finite and cap energy -> 0 as T -> -oo, at a = 1/4, 9/20", fin and to0,
          f"{flux[sp.Rational(1, 4)]}, {cap[sp.Rational(1, 4)]}")
    check("S4e control: at a = 1/2 both diverge (the weight sees the radiation field)",
          flux[sp.Rational(1, 2)] == sp.oo and cap[sp.Rational(1, 2)] == sp.oo)
    mp.mp.dps = 30
    vals = []
    for l in range(0, 21):
        A, B, Cc = mp.mpf(3)/2 + l, -mp.mpf(1)/2 - l, mp.mpf(1)
        T32 = mp.sqrt(mp.pi)*mp.gamma(mp.mpf(1))*mp.rgamma((mp.mpf(3)/2 + l + 1)/2)*mp.rgamma((mp.mpf(3)/2 - l - 1)/2)
        F2 = (A*B*(A + 1)*(B + 1)/(Cc*(Cc + 1)))/4*mp.hyp2f1(A + 2, B + 2, Cc + 2, mp.mpf(1)/2)
        F2d = mp.diff(lambda x: mp.hyp2f1(A, B, Cc, x/2), mp.mpf(1), 2)
        vals.append((abs(T32), abs(F2), abs(F2 - F2d)))
    check("S4f T_(3/2)(l) != 0 and F''(1) != 0 for l <= 20 (F'' by Gauss's second theorem, checked by differentiation)",
          min(x[0] for x in vals) > 1e-20 and min(x[1] for x in vals) > 1e-20 and max(x[2] for x in vals) < 1e-15,
          "min |T|, |F''|: " + mp.nstr(min(x[0] for x in vals), 4) + ", " + mp.nstr(min(x[1] for x in vals), 4))
    c = sp.Symbol("c", real=True)
    phi0 = r**(-p)*sp.Function("F")((v - v1)/r)
    tvar = sp.Symbol("t", real=True)
    d2 = sp.diff(phi0.subs(v, tvar + r), tvar, 2)
    lead = sp.simplify(d2*r**sp.Rational(7, 2))
    check("S4g on a slice t = c, d_t^2 phi = r^(-7/2) F''(s): a curvature term rho^(7/2) at spatial infinity",
          sp.simplify(lead - sp.Subs(sp.Derivative(sp.Function("F")(sp.Symbol("x")), sp.Symbol("x"), 2),
                                     sp.Symbol("x"), (tvar + r - v1)/r).doit()) == 0, str(lead)[:60])
    _ = c


def riem_lin(h, X):
    """linearized Riemann tensor of eta + h, eta = diag(-1, 1, 1, 1, 1): R_abcd = (1/2)(h_ad,bc + h_bc,ad - h_ac,bd
    - h_bd,ac)"""
    n = len(X)
    out = {}
    for a, b, c, d in itertools.product(range(n), repeat=4):
        if a < b and c < d and (a, b) <= (c, d):
            out[(a, b, c, d)] = sp.Rational(1, 2)*(sp.diff(h[a][d], X[b], X[c]) + sp.diff(h[b][c], X[a], X[d])
                                                    - sp.diff(h[a][c], X[b], X[d]) - sp.diff(h[b][d], X[a], X[c]))
    return out


def s5():
    print("S5  the linearized curvature is gauge invariant")
    X = sp.symbols("t x1 x2 x3 x4", real=True)
    random.seed(3)
    mons = [m for m in itertools.product(range(3), repeat=5) if sum(m) <= 3]
    xi = []
    for _ in range(5):
        xi.append(sum(sp.Rational(random.randint(-4, 4), random.randint(1, 3))*sp.Mul(*[X[i]**m[i] for i in range(5)])
                      for m in random.sample(mons, 12)))
    eta = [-1, 1, 1, 1, 1]
    xil = [eta[i]*xi[i] for i in range(5)]
    h = [[sp.diff(xil[b], X[a]) + sp.diff(xil[a], X[b]) for b in range(5)] for a in range(5)]
    R = riem_lin(h, X)
    check(f"S5a pure gauge h = d xi + d xi: all {len(R)} components of the linearized Riemann tensor vanish",
          all(sp.expand(x) == 0 for x in R.values()))
    f = sp.Function("f")(X[0], X[1])
    h2 = [[0]*5 for _ in range(5)]
    h2[2][2] = f
    R2 = riem_lin(h2, X)
    check("S5b control: h = f(t, x1) dx2^2 is not pure gauge: some component is nonzero",
          any(sp.simplify(x) != 0 for x in R2.values()))


def main():
    for f in (s1, s2, s3, s4, s5):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
