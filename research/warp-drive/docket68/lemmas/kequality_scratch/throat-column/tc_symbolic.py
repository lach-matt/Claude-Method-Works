#!/usr/bin/env python3
"""tc_symbolic.py -- model B (the corridor's own throat bulk): the two-plane balance, exact parts (sympy).

Scratch instrument for M-RULINGS items 179-181 (scratch, not a board instrument; read-only on the repository).
Owner imported by path, never copied: lemmas/sim2_facing.py (throat_rhs, lemma_t, t5c).

  X1  INDEPENDENT DERIVATION of the column equations (computed, exact).  ds^2 = dy^2 + alpha^2 g2 + beta^2 h2 with
      g2 = -F dt^2 + dx^2/F, F = 1 + cA x^2/4 (scalar curvature -cA/2: AdS2 of radius 2 at cA = 1) and
      h2 = dth^2/G + G dph^2, G = 1 - cS th^2/4 (Gaussian curvature cS/4: the S2 of radius 2 at cS = 1).  My own
      diagonal-metric Ricci, not the owner's _ricci_diag.  At cA = cS = 1 the alpha'' and beta'' equations and the
      constraint must equal sim2_facing.throat_rhs (called with sympy symbols) exactly.  cA = cS = 0 is flat slicing:
      pure AdS5 in Poincare form, the control.
  X2  THE UMBILIC DEFECT D = q - p obeys D' = -4 a D + S, S = cA/(4 alpha^2) + cS/(4 beta^2), a = (p + q)/2 (computed
      exactly from throat_rhs).  With D(0) = 0: D(y) = Int_0^y S(t) exp(-4 Int_t^y a) dt (variation of constants,
      verified symbolically).  So at cA = cS = 1, D > 0 on (0, y_s) for EVERY e: no umbilic depth (deduced, exact).
      At cA = cS = 0, D == 0: every depth umbilic (the control).
  X3  GAUSS AT A LEVEL SURFACE (computed, exact): the constraint is R4/2 = p^2 + q^2 + 4pq - 6e^2 with
      R4 = -cA/(2 alpha^2) + cS/(2 beta^2).  At an umbilic surface k^2 = e^2 + R4/12.  At our plane (alpha = beta = 1,
      cA = cS = 1) R4 = 0, so k = -e, s1 = +1 for EVERY e: our balance at the Randall-Sundrum tension is an identity in
      e = m/ell and pins nothing (deduced; R(eq. 17) = 0).
  X4  ISRAEL AT POSITION 2's PLANE, every framing (computed, exact).  Slab side K_s = -diag(p,p,q,q) (normal into the
      slab), far side K_f = diag(p',p',q',q') (outward), S = -(nu/2)[(K_s + K_f) - delta tr]; pure tension iff
      p' - p = q' - q.  (a) mirrored (p' = -p, q' = -q): pure tension iff p = q; s2 = ell p(y2) = ell a(y2) <= -1 (T5c).
      (b) pure-trace far side of curvature ell_f (p' = q'): pure tension iff p = q -- impossible by X2.  (c) free far
      side (traceless part cancelled): s2 = -kbar/e, kbar = (-a +- sqrt(a^2 + e_f^2 - e^2))/2, one equation in (y2, e).
  X5  POSITIVE CONTROL (computed, exact): with slices of unequal radii at the plane (R4 != 0) an umbilic plane's
      tension DOES fix e: alpha0 = 1, beta0 = 2, s1 = 1/2 gives e^2 = 1/24 exactly -- the machinery can return an
      equality when the geometry carries one.
  X6  T5c and Lemma T re-read from the owner (lemma_t, t5c): the fixed point -1 at s1 = 1.
python3 tc_symbolic.py
"""
import itertools
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _owner  # noqa: E402

S2M = _owner.sim2()

y, t, x, th, ph = sp.symbols("y t x theta phi", real=True)
e, ef = sp.symbols("e e_f", nonnegative=True)
cA, cS = sp.symbols("c_A c_S", real=True)


def ricci_diag(g, X):
    """Mixed Ricci R^a_a of a diagonal metric g (list) in coordinates X: textbook Christoffels, no owner code."""
    n = len(X)
    gi = [1 / gg for gg in g]

    def Gam(a, b, c):  # Gamma^a_{bc}
        val = 0
        if b == c:
            val += -sp.diff(g[b], X[a]) / 2 if a != b else 0
        if a == b:
            val += sp.diff(g[a], X[c]) / 2
        if a == c:
            val += sp.diff(g[a], X[b]) / 2
        if a == b == c:
            val = sp.diff(g[a], X[a]) / 2
        return gi[a] * val

    G = [[[sp.simplify(Gam(a, b, c)) for c in range(n)] for b in range(n)] for a in range(n)]
    R = []
    for b in range(n):
        Rbb = 0
        for a in range(n):
            Rbb += sp.diff(G[a][b][b], X[a]) - sp.diff(G[a][b][a], X[b])
            for d in range(n):
                Rbb += G[a][a][d] * G[d][b][b] - G[a][b][d] * G[d][a][b]
        R.append(sp.simplify(gi[b] * Rbb))
    return R


def x1_equations():
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    F = 1 + cA * x**2 / 4
    G = 1 - cS * th**2 / 4
    g = [sp.Integer(1), -al**2 * F, al**2 / F, be**2 / G, be**2 * G]
    X = [y, t, x, th, ph]
    R = ricci_diag(g, X)
    E = [sp.simplify(R[i] + 4 * e**2) for i in range(5)]       # vacuum: R^a_b = -4 e^2 delta (Lambda5 = -6/ell^2)
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    sub = {sp.Derivative(al, (y, 2)): (P + p**2) * a, sp.Derivative(be, (y, 2)): (Q + q**2) * b,
           sp.Derivative(al, y): p * a, sp.Derivative(be, y): q * b}
    Es = [sp.simplify(v.subs(sub).subs({al: a, be: b})) for v in E]
    sol = sp.solve([Es[1], Es[3]], [P, Q], dict=True)[0]
    cons = sp.simplify(Es[0].subs(sol))
    # the owner's coded system, called with sympy symbols (its body is plain arithmetic)
    al_s, be_s = sp.symbols("a b", positive=True)
    rhs = S2M.throat_rhs(0, [al_s, be_s, p, q, 0, 0, 0, 0, 0, 0], e, 1)
    own_P, own_Q = rhs[2], rhs[3]
    own_c = p**2 + q**2 + 4 * p * q - 6 * e**2 - 1 / (4 * b**2) + 1 / (4 * a**2)   # SIM2's coded constraint (C7)
    at1 = {cA: 1, cS: 1}
    chk_P = sp.simplify(sol[P].subs(at1) - own_P.subs({al_s: a, be_s: b}))
    chk_Q = sp.simplify(sol[Q].subs(at1) - own_Q.subs({al_s: a, be_s: b}))
    ratio = sp.simplify(cons.subs(at1) / own_c)
    # x and phi equations must repeat t and theta (AdS2 boost, SO(3))
    rep = (sp.simplify(Es[2] - Es[1]), sp.simplify(Es[4] - Es[3]))
    return {"P": sp.simplify(sol[P]), "Q": sp.simplify(sol[Q]), "cons": cons, "chk_P": chk_P, "chk_Q": chk_Q,
            "cons_ratio": ratio, "repeat": rep, "syms": (p, q, a, b)}


def x2_defect(eqs):
    p, q, a, b = eqs["syms"]
    D = sp.expand(eqs["Q"] - eqs["P"])
    abar = (p + q) / 2
    S = cA / (4 * a**2) + cS / (4 * b**2)
    form = sp.simplify(D - (-4 * abar * (q - p) + S))
    # variation of constants, verified with generic functions
    A_, S_ = sp.Function("A"), sp.Function("Sfun")
    tt, ss = sp.symbols("t s", real=True)
    Dsol = sp.Integral(S_(tt) * sp.exp(-4 * sp.Integral(A_(ss), (ss, tt, y))), (tt, 0, y))
    ode_res = sp.simplify(sp.diff(Dsol, y).doit() - (-4 * A_(y) * Dsol + S_(y)))
    D0 = Dsol.subs(y, 0).doit()
    # also the owner's own throat_rhs: Q - P at cS = 1 (sign of the S2 term) and at its s2 = -1 mutation
    al_s, be_s = sp.symbols("a b", positive=True)
    r1 = S2M.throat_rhs(0, [al_s, be_s, p, q, 0, 0, 0, 0, 0, 0], e, 1)
    rm = S2M.throat_rhs(0, [al_s, be_s, p, q, 0, 0, 0, 0, 0, 0], e, -1)
    own = sp.simplify(r1[3] - r1[2] - (-2 * (q - p) * (q + p) + 1 / (4 * al_s**2) + 1 / (4 * be_s**2)))
    own_mut = sp.simplify(rm[3] - rm[2] - (-2 * (q - p) * (q + p) + 1 / (4 * al_s**2) - 1 / (4 * be_s**2)))
    # Lemma T on the column: a' = (P + Q)/2 = e^2 - a^2 - D^2/4 once the constraint (cons = 0) is used
    cons_sol = sp.solve(sp.Eq(eqs["cons"], 0), cS)[0]
    lt_res = sp.simplify(((eqs["P"] + eqs["Q"]) / 2).subs(cS, cons_sol) - (e**2 - abar**2 - (q - p)**2 / 4))
    # and the stable variables at = a + e, D: at' = -at^2 + 2 e at - D^2/4 (used by tc_numeric's stable integration)
    at_ = sp.Symbol("at", real=True)
    st_res = sp.simplify((e**2 - (at_ - e)**2 - sp.Symbol("D")**2 / 4) - (-at_**2 + 2 * e * at_ - sp.Symbol("D")**2 / 4))
    return {"form_residual": form, "ode_residual": ode_res, "D0": D0, "own_residual": own,
            "own_mut_residual": own_mut, "S_at_throat": S.subs({cA: 1, cS: 1}), "S_flat": S.subs({cA: 0, cS: 0}),
            "lemmaT_residual": lt_res, "stable_residual": st_res}


def x3_gauss(eqs):
    p, q, a, b = eqs["syms"]
    R4 = -cA / (2 * a**2) + cS / (2 * b**2)
    gauss = sp.simplify(eqs["cons"] - 2 * (p**2 + q**2 + 4 * p * q - 6 * e**2 - R4 / 2))   # my yy eq is 2x SIM2's
    # direct check of R4 from the slice metric with my own Ricci
    al0, be0 = sp.symbols("alpha0 beta0", positive=True)
    F = 1 + cA * x**2 / 4
    G = 1 - cS * th**2 / 4
    R4d = sum(ricci_diag([-al0**2 * F, al0**2 / F, be0**2 / G, be0**2 * G], [t, x, th, ph]))
    R4_ok = sp.simplify(R4d - R4.subs({a: al0, b: be0}))
    k = sp.Symbol("k", real=True)
    umb = sp.solve(sp.Eq(eqs["cons"].subs({p: k, q: k}), 0), k)
    at_plane = [sp.simplify(u.subs({a: 1, b: 1, cA: 1, cS: 1})) for u in umb]
    # our plane: mirrored, normal into the slab +d_y: K = diag(p,p,q,q) = -e delta; rho = -S^t_t, S = -nu(K - delta K)
    nu = sp.Symbol("nu", positive=True)
    Kd = [-e] * 4
    rho1 = -(-nu * (Kd[0] - sum(Kd)))
    s1 = sp.simplify(rho1 / (3 * nu * e))
    cons_at_plane = sp.simplify(eqs["cons"].subs({p: -e, q: -e, a: 1, b: 1, cA: 1, cS: 1}))
    return {"gauss_residual": gauss, "R4_residual": R4_ok, "umbilic_k": umb, "k_at_plane": at_plane, "s1": s1,
            "constraint_at_plane_all_e": cons_at_plane}


def x4_israel():
    p, q, pf, qf, a_, D_, nu = sp.symbols("p q p_f q_f a D nu", real=True)
    Ks = [-p, -p, -q, -q]
    S_of = lambda Kf: [-(nu / 2) * ((Ks[i] + Kf[i]) - sum(Ks[j] + Kf[j] for j in range(4))) for i in range(4)]
    # (a) mirror
    Sm = S_of([-p, -p, -q, -q])
    mirror_pure = sp.solve(sp.Eq(Sm[0], Sm[2]), q)
    rho_m = sp.simplify(-Sm[0].subs(q, p))
    s2_mirror = sp.simplify(rho_m / (3 * nu * e))
    # general far side, pure tension: p_f - p = q_f - q = 2 kbar
    kb = sp.Symbol("kbar", real=True)
    Sg = S_of([p + 2 * kb, p + 2 * kb, q + 2 * kb, q + 2 * kb])
    pure = sp.simplify(Sg[0] - Sg[2])
    rho_g = sp.simplify(-Sg[0])
    # far constraint with the same induced R4: p_f^2 + q_f^2 + 4 p_f q_f - 6 e_f^2 = p^2 + q^2 + 4 p q - 6 e^2
    farc = sp.expand((p + 2 * kb)**2 + (q + 2 * kb)**2 + 4 * (p + 2 * kb) * (q + 2 * kb) - 6 * ef**2
                     - (p**2 + q**2 + 4 * p * q - 6 * e**2))
    roots = sp.solve(sp.Eq(farc, 0), kb)
    roots_a = [sp.simplify(r.subs(q, 2 * a_ - p)) for r in roots]
    s2_roots = [sp.simplify(-r / e) for r in roots_a]
    # (b) pure-trace far side needs p_f = q_f, i.e. p + 2kb = q + 2kb -> p = q
    return {"mirror_pure_iff": mirror_pure, "s2_mirror": s2_mirror, "pure_residual_general": pure,
            "rho_general": rho_g, "kbar_roots": roots_a, "s2_roots": s2_roots}


def x5_positive_control(eqs):
    p, q, a, b = eqs["syms"]
    k, s1 = sp.symbols("k s_1", real=True)
    cons = eqs["cons"].subs({cA: 1, cS: 1, a: 1, b: 2})
    sol = sp.solve(sp.Eq(cons.subs({p: s1 * (-e), q: s1 * (-e)}), 0), e**2)
    e2 = sp.solve(sp.Eq(cons.subs({p: -s1 * e, q: -s1 * e}), 0), e)
    val = [sp.nsimplify(sp.simplify(v.subs(s1, sp.Rational(1, 2)))) for v in e2]
    # at alpha = beta (eq. (17)'s throat) the same equation is an identity in e for s1 = 1, and has no root for s1 != 1
    cons_eq = sp.simplify(eqs["cons"].subs({cA: 1, cS: 1, a: 1, b: 1}).subs({p: -s1 * e, q: -s1 * e}))
    return {"e_for_s1_half": val, "equal_radii_constraint": sp.factor(cons_eq)}


def x6_owner():
    lt = S2M.lemma_t()
    t5 = S2M.t5c(sp.Rational(1, 32))
    return {"lemma_t": lt, "t5c": t5}


def main():
    eqs = x1_equations()
    print("X1 column equations, my own Ricci, with slice curvatures (cA, cS):")
    print("   alpha''/alpha - p^2 = P =", eqs["P"])
    print("   beta''/beta  - q^2 = Q =", eqs["Q"])
    print("   constraint (yy)       =", eqs["cons"])
    print("   against sim2_facing.throat_rhs at cA = cS = 1: P - P_owner =", eqs["chk_P"], "; Q - Q_owner =", eqs["chk_Q"],
          "; constraint / SIM2's coded constraint =", eqs["cons_ratio"])
    print("   x-eq minus t-eq, phi-eq minus theta-eq:", eqs["repeat"])
    d2 = x2_defect(eqs)
    print("\nX2 the umbilic defect D = q - p:")
    print("   D' - (-4 a D + S) =", d2["form_residual"], " with S = cA/(4 alpha^2) + cS/(4 beta^2)")
    print("   owner's throat_rhs: Q - P - (-2D(p+q) + 1/(4a^2) + 1/(4b^2)) =", d2["own_residual"],
          "; at its s2 = -1 mutation the S2 term flips sign:", d2["own_mut_residual"])
    print("   variation of constants D = Int_0^y S exp(-4 Int a): ODE residual =", d2["ode_residual"], "; D(0) =", d2["D0"])
    print("   S at the throat (cA = cS = 1):", d2["S_at_throat"], "(> 0 wherever alpha, beta are finite and nonzero)")
    print("   S with flat slices (cA = cS = 0):", d2["S_flat"], "-> D == 0 from D(0) = 0: every depth umbilic")
    print("   Lemma T on the column, a' - (e^2 - a^2 - D^2/4) on the constraint surface:", d2["lemmaT_residual"],
          "; stable form at' = -at^2 + 2e at - D^2/4:", d2["stable_residual"])
    print("   so for y > 0 (D > 0): a' < e^2 - a^2 <= 0 wherever a <= -e, hence |a| strictly increasing from e")
    g3 = x3_gauss(eqs)
    print("\nX3 Gauss at a level surface:")
    print("   constraint - 2 (p^2 + q^2 + 4pq - 6e^2 - R4/2) =", g3["gauss_residual"], "; R4 from the slice metric:",
          g3["R4_residual"])
    print("   umbilic level surface: k =", g3["umbilic_k"])
    print("   at our plane (alpha = beta = 1, the throat of eq. (17)): k =", g3["k_at_plane"], "; mirrored s1 =", g3["s1"])
    print("   the constraint at our plane's data p = q = -e, alpha = beta = 1:", g3["constraint_at_plane_all_e"],
          "for every e (an identity: ours pins nothing)")
    i4 = x4_israel()
    print("\nX4 Israel at position 2's plane (slab side y < y2):")
    print("   (a) mirrored: pure tension iff q =", i4["mirror_pure_iff"], "; then s2 = rho/sigma_RS(ell) =", i4["s2_mirror"])
    print("   general far side with p_f - p = q_f - q = 2 kbar: S^t_t - S^th_th =", i4["pure_residual_general"],
          "; rho =", i4["rho_general"])
    print("   far constraint fixes kbar =", i4["kbar_roots"])
    print("   so s2 = -kbar/e =", i4["s2_roots"])
    print("   (first root: far trace a_f = a + 2 kbar = -sqrt(...) < 0, a DECAYING far side; second: a_f = +sqrt(...), GROWING)")
    pc = x5_positive_control(eqs)
    print("\nX5 positive control: slices of unequal radii (alpha0 = 1, beta0 = 2), umbilic plane at s1 = 1/2: e =",
          pc["e_for_s1_half"])
    print("   with equal radii (eq. (17)'s throat) the same condition reads", pc["equal_radii_constraint"],
          "= 0: s1^2 = 1 at every e, no e for s1^2 != 1")
    o6 = x6_owner()
    print("\nX6 owner: lemma_t", o6["lemma_t"], "; t5c(1/32)", o6["t5c"])
    ok = all([eqs["chk_P"] == 0, eqs["chk_Q"] == 0, eqs["cons_ratio"] == 2, eqs["repeat"] == (0, 0),
              d2["form_residual"] == 0, d2["own_residual"] == 0, d2["own_mut_residual"] == 0,
              d2["ode_residual"] == 0, d2["D0"] == 0,
              d2["lemmaT_residual"] == 0, d2["stable_residual"] == 0, g3["gauss_residual"] == 0, g3["R4_residual"] == 0,
              g3["constraint_at_plane_all_e"] == 0, g3["s1"] == 1,
              sp.simplify(i4["s2_mirror"] - p_over_e()) == 0, i4["pure_residual_general"] == 0,
              any(sp.simplify(v**2 - sp.Rational(1, 24)) == 0 for v in pc["e_for_s1_half"])])
    print("\nall exact checks:", "PASS" if ok else "FAIL")
    return ok


def p_over_e():
    p = sp.Symbol("p", real=True)
    return p / e


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
