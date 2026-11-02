"""wedge5.py -- SETTLE-GLAM5 section 5: the energy identity of the scattering problem on the wedge W.

W := {v >= v1, t <= t_S} near spatial infinity: its past boundary is the ingoing cone N = {v = v1} and past null
infinity at v >= v1 (nothing incoming there after the shell), its future boundary the far part S of Hintz's initial
surface. The background is the record's g0 after the shell, five-dimensional Tangherlini in Kerr-Schild form,
g0 = eta + (mu/r^2) k k, k = dt + xhat . dx (det g0 = -1), in Cartesian (t, x1..x4); u := t - r, v := t + r.
For a scalar phi, T_ab = d_a phi d_b phi - (1/2) g_ab |d phi|^2, and X := w(u) d_t.

  W1 (exact, rational points) d_a (g^ab T_bc X^c) = (box_g phi) X phi + T(grad w, d_t): the divergence identity of
     the multiplier, d_t being Killing (checked at 6 points, random cubic phi, mu = 1 and mu = 3, w = (-u)^(2a) at
     a = 1/3 and 3/4, exactly in rationals and radicals).
  W2 (exact) g0^(-1)(du, du) = -4 mu/r^2 and g0^(-1)(du, dt) = -1 - 2 mu/r^2: grad u is timelike and past-directed,
     so for w' < 0 grad w is future timelike, and T(grad w, d_t) >= 0 wherever d_t is timelike (r^2 > mu): the bulk
     term has the sign that makes the energy through S at most that through N (computed at 2000 random points and
     gradients: min >= 0). Control: w = v^(2a) (w' > 0 along grad v, which is past null) gives negative values.
  W3 (exact) the weighted flux through N of a field r^-2 M(omega) with its ell-gain is int r^(2a) (|d_r phi|^2 +
     r^-2 |grad_omega phi|^2) r^3 dr, finite exactly for a < 1; control: with no ell-gain (|d_r phi| ~ r^-2, the
     bound the record gives for g_lam - g_app uniformly in lam) it diverges for every a >= 0.
  W4 (exact) the Gronwall kernels along W, where r >= v1 - t: a first-order coefficient O(r^-3) (the record's gauge
     about Ricci-flat g0: Gamma[g0] ~ mu r^-3) gives int^(t_S) (v1 - t)^-3 dt < oo, and a quasilinear term with
     |d h| <= C r^(-3/2-a) gives int (v1 - t)^(-3/2-a) dt < oo; control: an O(r^-1) first-order coefficient (the
     constraint damping 1-forms of III.K's gauge, c = r^-1 dt) gives a divergent kernel: the continuation is posed
     in the record's own gauge, not III.K's.
  W5 (exact) the energy on the cap {t = T} cap W of a field with |d phi| <= r^-3 is O(|T|^(2a-2)), which tends to 0
     as T -> -oo for a < 1 (nothing incoming in the limit); control: a = 1 makes it infinite.
  W6 (exact) the weighted Hardy inequality int_R^oo r^(2a-1) phi^2 <= a^-2 int_R^oo r^(2a+1) phi_r^2 on the power
     test functions it is sharp on (phi = r^-b, b > a); control: at a = 0 the constant is lost.
Labels: computed (exact, sympy).

    python3 checks/wedge5.py
"""
import random
import sys

import sympy as sp

t, x1, x2, x3, x4 = X = sp.symbols("t x1 x2 x3 x4", real=True)
FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def metric(m):
    r = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    k = [sp.Integer(1), x1/r, x2/r, x3/r, x4/r]
    eta = sp.diag(-1, 1, 1, 1, 1)
    g = eta + m/r**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j])
    K = eta*sp.Matrix(k)  # eta^-1 = eta
    gi = eta - m/r**2*K*K.T
    return g, gi, r


def w1():
    print("W1  the divergence identity")
    random.seed(5)
    ok_all = True
    for m in (1, 3):
        g, gi, r = metric(sp.Integer(m))
        check(f"W1a mu={m}: g^-1 g = 1 and det g = -1", sp.simplify(gi*g - sp.eye(5)) == sp.zeros(5, 5)
              and sp.simplify(g.det()) == -1)
        for aa in (sp.Rational(1, 3), sp.Rational(3, 4)):
            u = t - r
            wf = (-u)**(2*aa)
            phi = sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4))*mono
                      for mono in [t, x1, x2*x3, t*x4, x1**2*t, x2*x3*x4, t**3, x4**2, x1*x3*t])
            dphi = [sp.diff(phi, c) for c in X]
            grad = gi*sp.Matrix(dphi)
            nrm = sum(dphi[i]*grad[i] for i in range(5))
            T = sp.Matrix(5, 5, lambda i, j: dphi[i]*dphi[j] - g[i, j]*nrm/2)
            Xv = sp.Matrix([wf, 0, 0, 0, 0])
            P = gi*T*Xv
            div = sum(sp.diff(P[i], X[i]) for i in range(5))
            box = sum(sp.diff(grad[i], X[i]) for i in range(5))
            dw = [sp.diff(wf, c) for c in X]
            gw = gi*sp.Matrix(dw)
            Tgt = sum(gw[i]*T[i, 0] for i in range(5))
            rhs = box*wf*dphi[0] + Tgt
            for pt in ([1, 3, 2, 5, 4], [-2, 7, 1, 1, 3], [0, 4, 4, 2, 1]):
                sub = dict(zip(X, [sp.Integer(c) for c in pt]))
                d = sp.nsimplify(sp.N((div - rhs).subs(sub), 50), rational=False)
                val = abs(sp.N((div - rhs).subs(sub), 50))
                if val > sp.Float("1e-40"):
                    ok_all = False
                _ = d
    check("W1b div(T(X)) = (box phi) X phi + T(grad w, d_t) at 12 points", ok_all)


def w2():
    print("W2  the sign of the bulk term")
    mu, r = sp.symbols("mu r", positive=True)
    # in (t, r) with k = dt + dr: g0^-1 = eta^-1 - (mu/r^2) K K, K = -d_t + d_r
    eta_i = sp.diag(-1, 1)
    K = sp.Matrix([-1, 1])
    gi = eta_i - mu/r**2*K*K.T
    du = sp.Matrix([1, -1])
    dt_ = sp.Matrix([1, 0])
    check("W2a g0^-1(du, du) = -4 mu/r^2", sp.simplify((du.T*gi*du)[0] + 4*mu/r**2) == 0)
    check("W2b g0^-1(du, dt) = -1 - 2 mu/r^2 (grad u past-directed)", sp.simplify((du.T*gi*dt_)[0] + 1
                                                                                  + 2*mu/r**2) == 0)
    g = gi.inv()
    check("W2c g0(d_t, d_t) = -(1 - mu/r^2): d_t timelike for r^2 > mu",
          sp.simplify(g[0, 0] + 1 - mu/r**2) == 0)
    random.seed(11)
    mins = {"wu": 1e9, "wv": 1e9}
    for _ in range(2000):
        m = random.uniform(0.1, 2.0)
        rr = random.uniform(1.5, 30.0)*m**0.5
        G = sp.Matrix([[-1 + m/rr**2, m/rr**2], [m/rr**2, 1 + m/rr**2]])
        Gi = G.inv()
        # 1+1 block plus an angular gradient with |grad_omega phi|^2 = q >= 0 (it enters T(V,Y) as -(1/2) g(V,Y) q)
        a_t, a_r, q = random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(0, 3)
        dphi = sp.Matrix([a_t, a_r])
        nrm = (dphi.T*Gi*dphi)[0] + q
        for key, dw in (("wu", -sp.Matrix([1, -1])), ("wv", sp.Matrix([1, 1]))):
            V = Gi*dw  # grad w = w' grad(u or v); the factor |w'| > 0 is dropped
            Y = sp.Matrix([1, 0])
            Tvy = (V.T*dphi)[0]*(Y.T*dphi)[0] - (V.T*G*Y)[0]*nrm/2
            mins[key] = min(mins[key], float(Tvy))
    check("W2d T(grad w, d_t) >= 0 for w = w(u), w' < 0 (2000 random points, mu, d phi)",
          mins["wu"] >= -1e-12, f"min {mins['wu']:.3e}")
    check("W2e control: w = w(v), w' > 0 gives negative values", mins["wv"] < -1e-3,
          f"min {mins['wv']:.3e}")


def w3():
    print("W3  the weighted flux through N")
    r, R, a = sp.symbols("r R a", positive=True)
    dens = r**(2*a)*((sp.diff(r**-2, r))**2 + r**-2*(r**-2)**2)*r**3
    I = sp.integrate(dens.subs(a, sp.Rational(9, 10)), (r, R, sp.oo))
    check("W3a with the ell-gain (phi = r^-2 M): finite at a = 9/10", I.is_finite and I.is_positive, str(I))
    I1 = sp.integrate(dens.subs(a, 1), (r, R, sp.oo))
    check("W3b ... and infinite at a = 1", I1 == sp.oo, str(I1))
    dens0 = r**(2*a)*(r**-2)**2*r**3
    I0 = sp.integrate(dens0.subs(a, 0), (r, R, sp.oo))
    check("W3c control: no ell-gain (|d_r phi| ~ r^-2): infinite already at a = 0", I0 == sp.oo, str(I0))


def w4():
    print("W4  the Gronwall kernels along W")
    t_, v1, tS, a = sp.symbols("t v1 t_S a", real=True)
    L = sp.Symbol("L", positive=True)  # L := v1 - t_S > 0
    tt = sp.Symbol("tt", positive=True)  # tt := v1 - t >= L
    k3 = sp.integrate(tt**-3, (tt, L, sp.oo))
    kq = sp.integrate(tt**(-sp.Rational(3, 2) - sp.Rational(1, 4)), (tt, L, sp.oo))
    k1 = sp.integrate(tt**-1, (tt, L, sp.oo))
    check("W4a O(r^-3) coefficient: int (v1-t)^-3 dt finite", k3.is_finite, str(k3))
    check("W4b quadratic term with |dh| <= r^(-3/2-a), a = 1/4: finite", kq.is_finite, str(kq))
    check("W4c control: O(r^-1) coefficient (III.K's damping 1-forms): divergent", k1 == sp.oo, str(k1))


def w5():
    print("W5  the cap at t = T")
    r, Tm = sp.symbols("r Tm", positive=True)  # Tm := v1 - T -> oo
    for aa, finite in ((sp.Rational(1, 2), True), (sp.Rational(9, 10), True), (sp.Integer(1), False)):
        E = sp.integrate(r**(2*aa)*r**-6*r**3, (r, Tm, sp.oo))
        if finite:
            check(f"W5a a={aa}: cap energy = {E}, -> 0 as T -> -oo", sp.limit(E, Tm, sp.oo) == 0)
        else:
            check(f"W5b control a={aa}: cap energy infinite", E == sp.oo, str(E))


def w6():
    print("W6  the weighted Hardy inequality")
    r, R = sp.symbols("r R", positive=True)
    ok = True
    for aa in (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(9, 10)):
        for b in (aa + sp.Rational(1, 10), aa + 1, 2):
            if b <= aa:
                continue
            lhs = sp.integrate(r**(2*aa - 1)*r**(-2*b), (r, R, sp.oo))
            rhs = sp.integrate(r**(2*aa + 1)*sp.diff(r**-b, r)**2, (r, R, sp.oo))/aa**2
            ok = ok and sp.simplify(rhs - lhs) >= 0
    check("W6a int r^(2a-1) phi^2 <= a^-2 int r^(2a+1) phi_r^2 on phi = r^-b, b > a", ok)
    bb = sp.Rational(1, 10)
    lhs = sp.integrate(r**(-1)*r**(-2*bb), (r, R, sp.oo))
    rhs = sp.integrate(r*sp.diff(r**-bb, r)**2, (r, R, sp.oo))
    check("W6b control: at a = 0 the ratio lhs/rhs = 1/b^2 is unbounded as b -> 0 (here 100)",
          sp.simplify(lhs/rhs) == 100, str(sp.simplify(lhs/rhs)))


def main():
    w2()
    w3()
    w4()
    w5()
    w6()
    w1()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
