#!/usr/bin/env python3
"""gdr9_5.py -- GAUGEDECAY5.md Rounds 9-10: computational support for the round-8 claims that no check exercised (the
round-8 verifier's list), each with a control that runs the computed path with a mutated input and must fail.

Background as in gdlge2_5.py: the ingoing chart, g = -f dv^2 + 2 dv dr + r^2 gamma, f = 1 - mu/r^2, mu = s^2 = r_h^2;
the scalar type a S dv + b S dr + c dS (Lap S = -kappa S, kappa = l(l + 2)) and the vector type psi Y (delta d Y =
lambda Y, lambda = (l + 1)^2) of the zero-energy operator P-hat(0) = Box on stationary 1-forms, (R8.1); I.A's frame
dt_*, dx^1, ..., dx^4, in which a scalar-type form has the Cartesian size max(|a|, |b|, |c|/r).

  N1 (exact) Lemma R8.2 on a finite-dimensional model.  (i) The rotation fields Omega_ij = x_i d_j - x_j d_i are
     Killing fields of III.B's g^KS = eta + mu |x|^-2 (dt + d|x|)^2 in Cartesian coordinates, the reflections are
     isometries, and both fix t and |x| (so t_*, r): T_g commutes with every operator built from g, t_* and r.  (ii)
     On V := C^5 (x) H_<=2 (1-forms on S^3 in I.A's frame whose components are harmonic polynomials of degree <= 2;
     dim 70) the six generators act by L_Omega (on the components and on the frame, A_g = diag(1, g)); they are
     antisymmetric for the L^2(S^3) Gram matrix (the T_g are isometries); they split as su(2) + su(2); the two
     Casimirs are diagonalisable with eigenvalues -j(j + 1), j in {0, 1/2, 1, 3/2}; the isotypic projections P_(j1,j2)
     have the ranks the Clebsch-Gordan rule predicts.  Pi := 1 - P_(0,0) - P_(1/2,1/2) - P_(1,0) - P_(0,1) is
     idempotent, self-adjoint for the Gram matrix, commutes with the six generators, with a reflection and with the
     componentwise Laplacian (so with I(lambda) = (-lambda^2 + 2 lambda + Lap) Id and N_tf); every component of
     ran Pi has spherical mean 0 (Lemma R8.2 (d)) and ell vanishes on it (R8.2 (c)).  (iii) Pi_G, the projection on the
     G-fixed vectors (G = O(2) x O(2): the torus and the reflections x2 -> -x2, x4 -> -x4), kills P_(1/2,1/2), P_(1,0)
     + P_(0,1), every P_(j1,j2) with j1 != j2 (no vector type in the class) and P_(3/2,3/2) (no odd l), and not
     P_(0,0) or P_(1,1); so Pi_G Pi = Pi_G (1 - P_(0,0)) (Pi_cl = Pi_G (1 - Pi_0)).  Control: Pi with P_(0,1) not
     removed does not commute with the reflection x1 -> -x1 (conjugation by it exchanges (1,0) and (0,1)).
  N2 (exact; one standard asymptotic formula, cross-checked numerically) Lemma R8.4 and L6's cross-check at every
     l >= 1, scalar type.  With psi solving (r^3 f psi')' = kappa r psi and A solving f (r^3 A')' = kappa r A, the
     three 1-forms u_1 = (0, psi', psi) (= d(psi S)), u_2 = (0, -(kappa/2) r^2 psi', (kappa/2) r^2 psi - r^3 f psi')
     and u_3 = (A, -A/f, 0) solve (R8.1) for kappa symbolic; in x = r^2/mu the two equations are the hypergeometric
     ones with (a, b; c) = (-nu, nu + 1; 1) for psi(x) = F(1 - x) and (1 - nu, nu + 2; 2) for A = (1 - x) F(1 - x),
     kappa = 4 nu (nu + 1), nu = l/2, so the solutions regular at the horizon are 2F1's; their jets (a'(r_h), b(r_h),
     c(r_h)) have determinant -kappa^2; at the horizon the order-k recursion matrix is -2 s^2 k diag(k - 1, s (k + 1),
     k) with k symbolic and order 0 forces a(r_h) = 0, so the smooth solutions form a 3-space and u_1, u_2, u_3 span
     it.  At infinity (DLMF section 15.8: the leading coefficient Gamma(c) Gamma(b - a)/(Gamma(b) Gamma(c - a)) of
     (-z)^-a; checked with mpmath at nu = 1/2, ..., 9/2) u_1, u_3, u_2 have Cartesian growth exactly r^(l - 1), r^l,
     r^(l + 1), with nonzero leading coefficients for every nu > 0: no nonzero combination grows more slowly than
     r^(l - 1), which is r^1 or faster for every l >= 2, odd l included.  Control: the same path at l = 1 (nu = 1/2)
     gives growth r^0: the four l = 1 forms d(psi S), S in S_1, of (A71).
  N3 (exact; the same asymptotic formula) The vector type at every l >= 1: r (r f psi')' = lambda psi is, in x, the
     hypergeometric equation with ((l + 1)/2, -(l + 1)/2; 1), the horizon-regular solution grows like r^(l + 1) with
     coefficient Gamma(l + 1)/(Gamma((l + 1)/2) Gamma((l + 3)/2)) != 0, Cartesian size r^l, excluded by o(r) for
     l >= 1 (L4's closed forms at l = 1, 3, 5, 7 extended to every l).  Control: the same path with lambda = l^2 in
     place of (l + 1)^2 fails the hypergeometric identification.
  N4 (exact) Lemma R8.4 (d), inside the horizon: the Frobenius exponents of the scalar system at r = r_h are
     {-1, 0, 0, 0, 0, 1} (the determinant of N2's recursion matrix, -8 k^4 s^7 (k - 1)(k + 1)), those of the vector
     equation {0, 0}, both asserted as values (round 10); integers, so a solution smooth across r_h that vanishes on
     r > r_h has zero Taylor series there, and a nonzero Frobenius combination of integer exponents is not flat, so it
     vanishes on (r_0, r_h) (the system is regular there).  Control: the same computation with the exponent k shifted
     by 1/3 gives non-integral roots.
  N5 (exact) The kernel at b-weights in (-1, 0) and (0, 2) on the full bundle, every input computed (round 10).
     l = 0 (c absent): the four solutions W*, (d_v)^flat, (0, (r^2 + mu)/r) and (0, 1/(r (r^2 - mu))) of the 2 x 2
     system are independent; the first three are smooth at r_h and the fourth is not; their growths r^-2, r^0, r^1,
     against the threshold r^1 read from L2's computed gap: the l = 0 kernel is span{W*, (d_v)^flat} at weights in
     (-1, 0) and span{W*} in (0, 2).  Scalar l = 1: one per harmonic, counted from N2's growth exponents at nu = 1/2
     (0, 2, 1); vector l = 1: none (N3's exponent at l = 1); l >= 2: none (N2, N3).  With the dimensions of the
     degree-0 and degree-1 harmonics and their G-fixed parts from N1's model, the kernel is 2-dimensional in the
     class and 6-dimensional on all 1-forms at weights in (-1, 0).  Control: at weights in (0, 2) the same count
     gives 1, not 2.
  N6 (exact inputs; the arithmetic deduced) The index counts of (A71).  Computed: the indicial root 0 is simple, with
     a one-dimensional null space, in the l = 0 block and in the scalar l = 1 block, and is not a root of the vector
     l = 1 block (its determinant from gdlge2_5.py's L2 code) nor of any block l >= 2 (L2); the representation
     dimensions 1 and 4 and the G-fixed dimensions 1 and 0 (N1's model); the kernels (N5).  READ: the cokernel at
     the weights (0, 2) is span{ell} (III.D' Lemma 2.1 (3)).  Deduced (standard: the relative index theorem): the
     index jumps by 1 in the class and by 5 on all 1-forms from (0, 2) to (-1, 0), so the cokernels are 2 - 1 = 1 and
     6 - 5 = 1, as (A71) deduces.  Control: the jump with the l = 1 root counted once (its representation dimension
     dropped) gives cokernel 4, contradicting the deduced 1.
  N7 (exact) Corollary R8.11's decomposition.  For class 1-forms Z = a S dv + b S dr + c dS (S = P_j(cos 2 th),
     l = 2j = 2, 4; a, b, c arbitrary functions of (v, r)), L_Z g has no l = 0 part (the means of its orbit components
     and of H = gamma^ij h_ij/(6 r^2) vanish), and for Z_0 = a_0 dv + b_0 dr, L_{Z_0} g is spherically symmetric: so
     (L_Z g)_>=2 = L_{Z_>=2} g.  Control: with S + 1/7 in place of S the l = 0 part is not 0.
  N8 (exact exponents; Hankel asymptotics standard, checked with mpmath) R8.6's sctf step and the sctf half of the
     full-bundle failure.  On degree l the solutions of N_tf(1) are e^(-i r) r^-1 H^(1,2)_(l+1)(r) = g_1,
     e^(-2 i r) g_2: |g_j| r^(3/2) -> (2/pi)^(1/2) and r d_r g_j = O(r^-3/2) (conormal), while r d_r of e^(-2 i r)
     g_2 is of size r^(-1/2); |f_j| r^(l+2) -> 2^(l+1) l!/pi at ztf.  int^oo |g|^2 r^(2 r') r^3 dr < oo iff r' < -1/2:
     at R_out (order > -1/2) g_1 is excluded (R8.6 (iii)), at R_in (order < -1/2 for an admissible choice)
     e^(-2 i r) g_2 is admitted (the full-bundle failure).  Control: at R_in's order replaced by R_out's the
     membership fails.

Labels: computed (exact, sympy, except N2, N3 and N8's numerical cross-checks of standard asymptotics, mpmath); N6's
index arithmetic deduced from computed inputs (the relative index theorem, standard).
Run: python3 checks/gdr9_5.py [N1 ... N8]   (a few minutes)      Self-test of the harness: python3 checks/gdr9_5.py
--selftest (each control mechanism fed a known-true and a known-false statement).
"""
import itertools
import sys

import mpmath
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

from gdlge2_5 import gap_from_l2, indicial_scalar, indicial_vector
from gdrad5 import positive_sum
from hgauge5 import GEO, WSTAR
from rwgauge5 import p1, p2, r, s, th, v

HALF = sp.Rational(1, 2)
mu = s**2
f_ = 1 - mu/r**2
_print = print


def print(*args, **kw):                                         # report lines wrapped at 121 characters
    import textwrap
    text = ' '.join(str(a_) for a_ in args)
    _print('\n'.join(textwrap.fill(ln, 121, subsequent_indent='      ', break_on_hyphens=False) if ln else ln
                     for ln in text.split('\n')), **kw)


kap, nu, x, z = sp.symbols('kappa nu x z', positive=True)


def sys_scalar(a, b, c, k, m=mu):
    """(E_v, E_r, E_th) of (R8.1), as gdlge2_5.py"""
    d = sp.diff
    Ev = -(r*(r**2 - m)*d(a, r, 2) + 3*(r**2 - m)*d(a, r) - k*r*a)/r**3
    Er = -(r**2*(r**2 - m)*d(b, r, 2) + (3*r**3 + m*r)*d(b, r) - (k*r**2 + 3*r**2 - 3*m)*b + 2*k*r*c - 3*r**2*a)/r**4
    Eth = -(r*(r**2 - m)*d(c, r, 2) + (r**2 + m)*d(c, r) - k*r*c + 2*r**2*a + 2*(r**2 - m)*b)/r**3
    return [Ev, Er, Eth]


def sys_vector(ps, lm, m=mu):
    return -(r*sp.diff(r*(1 - m/r**2)*sp.diff(ps, r), r) - lm*ps)/r**2


# ----------------------------------------------------------------------------------------------------------------- N1
X4 = sp.symbols('x1:5', real=True)


def _monos(m):
    return [e for e in itertools.product(range(m + 1), repeat=4) if sum(e) == m]


def _moment(e):
    """(1/|S^3|) int_{S^3} x^e d omega = Gamma(2) prod Gamma((e_i + 1)/2) / (pi^2 Gamma((|e| + 4)/2))"""
    if any(ei % 2 for ei in e):
        return sp.Integer(0)
    val = sp.prod([sp.gamma(sp.Rational(ei + 1, 2)) for ei in e])/sp.gamma(sp.Rational(sum(e) + 4, 2))/sp.pi**2
    return sp.nsimplify(sp.simplify(val))


_MODEL = {}


def model(L=2):
    """the model V = C^5 (x) H_<=L with the O(4) action, the Gram matrix and the componentwise Laplacian"""
    if L in _MODEL:
        return _MODEL[L]
    H = []
    for m in range(L + 1):
        ms = _monos(m)
        cs = sp.symbols('c0:%d' % len(ms))
        P = sum(cs[i]*sp.prod([X4[j]**e[j] for j in range(4)]) for i, e in enumerate(ms))
        lap = sp.expand(sum(sp.diff(P, xj, 2) for xj in X4))
        if lap == 0:
            ns = [sp.eye(len(ms))[:, i] for i in range(len(ms))]
        else:
            eqs = sp.Poly(lap, *X4).coeffs()
            ns = sp.Matrix([[sp.expand(e).coeff(c) for c in cs] for e in eqs]).nullspace()
        for vv in ns:
            H.append((m, sp.expand(sum(vv[i]*sp.prod([X4[j]**ms[i][j] for j in range(4)]) for i in range(len(ms))))))
    nH = len(H)
    allmon = sorted(set(itertools.chain(*[_monos(m) for m in range(L + 1)])))
    idx = {e: i for i, e in enumerate(allmon)}

    def vec(p):
        out = [0]*len(allmon)
        if p != 0:
            for term, co in sp.Poly(p, *X4).terms():
                out[idx[term]] = co
        return out
    B = sp.Matrix([vec(p) for _, p in H]).T
    left = (B.T*B).inv()*B.T

    def op(fn):
        return sp.Matrix.hstack(*[left*sp.Matrix(vec(sp.expand(fn(p)))) for _, p in H])
    Om = {}
    for i in range(4):
        for j in range(i + 1, 4):
            Om[(i, j)] = op(lambda p, i=i, j=j: X4[i]*sp.diff(p, X4[j]) - X4[j]*sp.diff(p, X4[i]))
    Gm = sp.Matrix(nH, nH, lambda a, b: sum(co*_moment(t_) for t_, co in
                                             sp.Poly(sp.expand(H[a][1]*H[b][1]), *X4).terms()))
    I5, IH = sp.eye(5), sp.eye(nH)
    toD = lambda M: DomainMatrix.from_Matrix(M).convert_to(QQ)
    Xg = {}
    for (i, j), O in Om.items():
        F = sp.zeros(5)
        F[1 + i, 1 + j] = 1                                   # L_Omega dx^k = delta_jk dx^i - delta_ik dx^j
        F[1 + j, 1 + i] = -1
        Xg[(i, j)] = toD(sp.kronecker_product(I5, O) + sp.kronecker_product(F, IH))

    def refl(k):
        F = sp.eye(5)
        F[1 + k, 1 + k] = -1
        return toD(sp.kronecker_product(F, op(lambda p: p.subs(X4[k], -X4[k], simultaneous=True))))
    out = dict(H=H, nH=nH, X=Xg, R={k: refl(k) for k in range(4)}, G=toD(sp.kronecker_product(I5, Gm)),
               D=toD(sp.kronecker_product(I5, sp.diag(*[-m*(m + 2) for m, _ in H]))), n=5*nH, L=L)
    _MODEL[L] = out
    return out


def iso_projections(M):
    """the su(2) + su(2) split, the Casimirs and the isotypic projections P_(j1,j2) of the model"""
    Xg, n, L = M['X'], M['n'], M['L']
    Id = DomainMatrix.eye(n, QQ)
    L_ = [Xg[(1, 2)], -Xg[(0, 2)], Xg[(0, 1)]]
    K_ = [Xg[(0, 3)], Xg[(1, 3)], Xg[(2, 3)]]
    h = QQ(1, 2)
    Jp = [(a + b)*h for a, b in zip(L_, K_)]
    Jm = [(a - b)*h for a, b in zip(L_, K_)]
    split = all((a*b - b*a).is_zero_matrix for a in Jp for b in Jm)
    split &= all((Jp[i]*Jp[(i + 1) % 3] - Jp[(i + 1) % 3]*Jp[i] - Jp[(i + 2) % 3]).is_zero_matrix or
                 (Jp[i]*Jp[(i + 1) % 3] - Jp[(i + 1) % 3]*Jp[i] + Jp[(i + 2) % 3]).is_zero_matrix for i in range(3))
    Cp = Jp[0]*Jp[0] + Jp[1]*Jp[1] + Jp[2]*Jp[2]
    Cm = Jm[0]*Jm[0] + Jm[1]*Jm[1] + Jm[2]*Jm[2]
    js = [sp.Rational(k, 2) for k in range(L + 2)]
    ev = {j: QQ(-int(2*j)*(int(2*j) + 2), 4) for j in js}

    def minpoly_zero(C):
        P = Id
        for j in js:
            P = P*(C - Id*ev[j])
        return P.is_zero_matrix

    def proj(C, j):
        P = Id
        for jj in js:
            if jj != j:
                P = P*(C - Id*ev[jj])*(QQ(1)/(ev[j] - ev[jj]))
        return P
    diag = minpoly_zero(Cp) and minpoly_zero(Cm)
    Pp, Pm = {j: proj(Cp, j) for j in js}, {j: proj(Cm, j) for j in js}
    P = {(a, b): Pp[a]*Pm[b] for a in js for b in js}
    return P, split, diag, js


def cg_prediction(L):
    """the Clebsch-Gordan multiplicities of V: dt (x) H_m = (m/2, m/2); C^4 (x) H_m = (1/2, 1/2) (x) (m/2, m/2)"""
    dims = {}
    for m in range(L + 1):
        key = (sp.Rational(m, 2), sp.Rational(m, 2))
        dims[key] = dims.get(key, 0) + (m + 1)**2
        for da in (HALF, -HALF):
            for db in (HALF, -HALF):
                a, b = sp.Rational(m, 2) + da, sp.Rational(m, 2) + db
                if a >= 0 and b >= 0:
                    dims[(a, b)] = dims.get((a, b), 0) + int((2*a + 1)*(2*b + 1))
    return dims


def killing():
    """Omega_ij Killing for g^KS = eta + mu |x|^-2 (dt + d|x|)^2, reflections isometries, t and |x| fixed"""
    t = sp.Symbol('t', real=True)
    xs = list(X4)
    co = [t] + xs
    R = sp.sqrt(sum(q**2 for q in xs))
    kk = [sp.Integer(1)] + [q/R for q in xs]
    eta = sp.diag(-1, 1, 1, 1, 1)
    g = sp.Matrix(5, 5, lambda a, b: eta[a, b] + mu/R**2*kk[a]*kk[b])
    ok = True
    for i in range(4):
        for j in range(i + 1, 4):
            V = [sp.Integer(0)]*5
            V[1 + i], V[1 + j] = xs[j], -xs[i]                # Omega = x_j d_i - x_i d_j (either sign)
            Lg = sp.Matrix(5, 5, lambda a, b: sum(V[c]*sp.diff(g[a, b], co[c]) + g[c, b]*sp.diff(V[c], co[a])
                                                  + g[a, c]*sp.diff(V[c], co[b]) for c in range(5)))
            ok &= Lg.applyfunc(sp.simplify) == sp.zeros(5)
            ok &= sp.simplify(sum(V[c]*sp.diff(R, co[c]) for c in range(5))) == 0
    for k in range(4):
        A = sp.eye(5)
        A[1 + k, 1 + k] = -1
        sub = {xs[k]: -xs[k]}
        gr = (A.T*g.subs(sub, simultaneous=True)*A).applyfunc(sp.simplify)
        ok &= gr == g.applyfunc(sp.simplify)
    return ok


def n1(control=False):
    M = model(2)
    n = M['n']
    Id = DomainMatrix.eye(n, QQ)
    Gd, Dd, Xg, R = M['G'], M['D'], M['X'], M['R']
    P, split, diag, js = iso_projections(M)
    remove = [(0, 0), (HALF, HALF), (1, 0)] + ([] if control else [(0, 1)])
    Pi = Id
    for key in remove:
        Pi = Pi - P[(sp.Rational(key[0]), sp.Rational(key[1]))]
    kill = True if control else killing()
    iso = all((Xg[k_].transpose()*Gd + Gd*Xg[k_]).is_zero_matrix for k_ in Xg)
    iso &= all((R[k_].transpose()*Gd*R[k_] - Gd).is_zero_matrix for k_ in R)
    pred = cg_prediction(M['L'])
    ranks = {k_: P[k_].rank() for k_ in P if not P[k_].is_zero_matrix}
    cg = ranks == {k_: v_ for k_, v_ in pred.items() if v_}
    idem = (Pi*Pi - Pi).is_zero_matrix
    selfadj = (Pi.transpose()*Gd - Gd*Pi).is_zero_matrix
    comm = all((Pi*Xg[k_] - Xg[k_]*Pi).is_zero_matrix for k_ in Xg)
    comm_R = all((Pi*R[k_] - R[k_]*Pi).is_zero_matrix for k_ in R)
    comm_D = (Pi*Dd - Dd*Pi).is_zero_matrix
    nH = M['nH']
    i0 = [k_ for k_, (m_, _) in enumerate(M['H']) if m_ == 0][0]
    Mean = DomainMatrix.from_Matrix(sp.Matrix(5, n, lambda a, b: 1 if b == a*nH + i0 else 0)).convert_to(QQ)
    means0 = (Mean*Pi).is_zero_matrix                         # Lemma R8.2 (d); its first row is ell (c)
    if control:
        print("  N1 control (Pi with P_(0,1) not removed): idempotent %s, self-adjoint %s, commutes with the "
              "rotations %s, with the reflections %s" % (idem, selfadj, comm, comm_R), flush=True)
        return idem and selfadj and comm and comm_R
    # the class: Pi_G, the Gram-orthogonal projection on the G-fixed vectors
    St = DomainMatrix.from_Matrix(sp.Matrix.vstack(Xg[(0, 1)].to_Matrix(), Xg[(2, 3)].to_Matrix(),
                                                   (R[1] - Id).to_Matrix(), (R[3] - Id).to_Matrix())).convert_to(QQ)
    Bf = sp.Matrix.hstack(*St.to_Matrix().nullspace())
    Bd = DomainMatrix.from_Matrix(Bf).convert_to(QQ)
    PiG = Bd*(Bd.transpose()*Gd*Bd).inv()*Bd.transpose()*Gd
    g_ok = (PiG*PiG - PiG).is_zero_matrix and all((PiG*Xg[k_] - Xg[k_]*PiG).is_zero_matrix for k_ in ((0, 1), (2, 3)))
    z = lambda key: (PiG*P[key]).is_zero_matrix
    hb = HALF
    cls = {"(1/2,1/2)": z((hb, hb)), "(1,0)+(0,1)": (PiG*(P[(1, 0)] + P[(0, 1)])).is_zero_matrix,
           "every j1 != j2": all(z(k_) for k_ in P if k_[0] != k_[1]), "(3/2,3/2) (odd l)": z((3*hb, 3*hb)),
           "not (0,0)": not z((0, 0)), "not (1,1)": not z((1, 1))}
    pcl = (PiG*Pi - PiG*(Id - P[(0, 0)])).is_zero_matrix and (PiG*Pi - Pi*PiG).is_zero_matrix
    dimG = Bf.shape[1]
    ok = (kill and iso and split and diag and cg and idem and selfadj and comm and comm_R and comm_D and means0 and
          g_ok and all(cls.values()) and pcl)
    print("  N1: Omega_ij Killing for g^KS, reflections isometries, t and |x| fixed: %s; model V = C^5 (x) H_<=2, dim "
          "%d: the T_g isometries of the Gram matrix: %s; su(2) + su(2): %s; Casimirs diagonalisable: %s; isotypic "
          "ranks %s = Clebsch-Gordan: %s; Pi idempotent %s, self-adjoint %s, commutes with the rotations %s, the "
          "reflections %s, the componentwise Laplacian %s; spherical means (and ell) vanish on ran Pi: %s; G-fixed "
          "space dim %d, Pi_G a projection commuting with the torus: %s; Pi_G kills %s; Pi_G Pi = Pi_G (1 - P_(0,0)) "
          "= Pi Pi_G: %s" % (kill, n, iso, split, diag, sorted(ranks.items(), key=str), cg, idem, selfadj, comm,
                             comm_R, comm_D, means0, dimG, g_ok, cls, pcl), flush=True)
    return ok


# ----------------------------------------------------------------------------------------------------------------- N2
_psi = sp.Function('psi')(r)
_A = sp.Function('A')(r)


def _reducer(F, ode):
    F2 = sp.solve(ode, sp.diff(F, r, 2))[0]

    def red(e):
        for _ in range(3):
            e = e.subs(sp.Derivative(F, (r, 4)), sp.diff(F2, r, 2)).subs(sp.Derivative(F, (r, 3)), sp.diff(F2, r))
            e = e.subs(sp.Derivative(F, (r, 2)), F2)
        return sp.simplify(e)
    return red


def three_solutions():
    odeP = sp.diff(r**3*f_*sp.diff(_psi, r), r) - kap*r*_psi
    odeA = f_*sp.diff(r**3*sp.diff(_A, r), r) - kap*r*_A
    u1 = (sp.Integer(0), sp.diff(_psi, r), _psi)
    u2 = (sp.Integer(0), -kap*r**2*sp.diff(_psi, r)/2, kap*r**2*_psi/2 - r**3*f_*sp.diff(_psi, r))
    u3 = (_A, -_A/f_, sp.Integer(0))
    return odeP, odeA, u1, u2, u3


def hyp_op(a, b, c, G):
    return z*(1 - z)*sp.diff(G, z, 2) + (c - (a + b + 1)*z)*sp.diff(G, z) - a*b*G


def hyp_identify(ode_r, F, a, b, c, pref, lam_sub):
    """the radial equation ode_r for F(r), in x = r^2/mu with F = pref(x) Y(1 - x), is a nonzero multiple of the
    hypergeometric operator with (a, b; c) acting on Y(z), z = 1 - x"""
    Y = sp.Function('Y')
    e = ode_r.subs(lam_sub).subs(F, (pref*Y(1 - x)).subs(x, r**2/mu)).doit()
    e = sp.simplify(e.subs(r, sp.sqrt(mu*x)))
    e = sp.simplify(e.subs(x, 1 - z).doit())
    ratio = sp.simplify(e/hyp_op(a, b, c, Y(z)))
    return (not ratio.has(Y)) and ratio != 0, ratio


def lead_coeff(a, b, c):
    """DLMF section 15.8 (b - a a positive integer included): 2F1(a, b; c; z) ~ Gamma(c) Gamma(b - a)/(Gamma(b)
    Gamma(c - a)) (-z)^-a as z -> -oo, for b - a > 0"""
    return sp.gamma(c)*sp.gamma(b - a)/(sp.gamma(b)*sp.gamma(c - a))


def lead_numeric(a, b, c, nus, pred=None):
    """mpmath check of lead_coeff (or of pred) at the given nu: 2F1(a, b; c; 1 - X) (X - 1)^a at X = 10^12"""
    mpmath.mp.dps = 30
    worst = 0
    for nv in nus:
        sub = {nu: nv}
        aa, bb, cc = [complex(sp.N(q.subs(sub), 30)).real for q in (a, b, c)]
        Xv = mpmath.mpf(10)**12
        val = mpmath.hyp2f1(aa, bb, cc, 1 - Xv)*(Xv - 1)**aa
        pred_v = sp.N((lead_coeff(a, b, c) if pred is None else pred).subs(sub), 30)
        worst = max(worst, abs(float(val/mpmath.mpf(str(pred_v))) - 1))
    return worst


NUS = [sp.Rational(k, 2) for k in range(1, 10)]


def scalar_growth(nu_val=None):
    """round 10: the leading Cartesian coefficients (a, b, c/r) of u_1, u_2, u_3 at r^(l - 1), r^(l + 1), r^l (the
    limits as r -> oo of the components of their leading terms divided by those powers), nu symbolic or at nu_val;
    all finite and not all 0 means Cartesian growth exactly that power"""
    _, _, u1, u2, u3 = three_solutions()
    sub = {} if nu_val is None else {nu: nu_val}
    CP, CA = lead_coeff(-nu, nu + 1, 1), lead_coeff(1 - nu, nu + 2, 2)
    kk = (4*nu*(nu + 1)).subs(sub)
    lp, la = (CP*(r**2/mu)**nu).subs(sub), (-CA*(r**2/mu)**nu).subs(sub)
    want = [w_.subs(sub) for w_ in (2*nu - 1, 2*nu + 1, 2*nu)]
    lims = []
    for u_, lead_sub, w_ in ((u1, {_psi: lp}, want[0]), (u2, {_psi: lp}, want[1]), (u3, {_A: la}, want[2])):
        out = []
        for c_ in (u_[0], u_[1], u_[2]/r):
            c_ = sp.sympify(c_).subs(lead_sub).doit().subs(kap, kk)
            e_ = sp.simplify(sp.powsimp(sp.expand_power_base(sp.expand(c_/r**w_), force=True), force=True))
            out.append(sp.simplify(sp.limit(e_, r, sp.oo).subs(sub)))
        lims.append(out)
    exact = [all(q_.is_finite is not False and q_ not in (sp.oo, -sp.oo, sp.zoo, sp.nan) for q_ in L_) and
             any(q_ != 0 for q_ in L_) for L_ in lims]
    return want, lims, exact


def vector_growth(l_val):
    """round 10: the leading coefficient of psi/r at r^l for the horizon-regular vector solution of degree l_val"""
    l = sp.Symbol('l', positive=True)
    C = lead_coeff(-(l + 1)/2, (l + 1)/2, sp.Integer(1)).subs(l, l_val)
    e_ = sp.simplify(sp.powsimp(sp.expand_power_base(C*(r**2/mu)**sp.Rational(l_val + 1, 2)/r/r**l_val, force=True),
                                force=True))
    lim = sp.simplify(sp.limit(e_, r, sp.oo))
    return sp.Integer(l_val), lim, (lim.is_finite is not False and lim != 0 and lim not in (sp.oo, sp.zoo, sp.nan))


def n2(control=False):
    odeP, odeA, u1, u2, u3 = three_solutions()
    redP, redA = _reducer(_psi, odeP), _reducer(_A, odeA)
    solves = [all(redP(e) == 0 for e in sys_scalar(*u1, kap)), all(redP(e) == 0 for e in sys_scalar(*u2, kap)),
              all(redA(e) == 0 for e in sys_scalar(*u3, kap))]
    sub = {kap: 4*nu*(nu + 1)}
    hP, ratP = hyp_identify(odeP, _psi, -nu, nu + 1, 1, sp.Integer(1), sub)
    hA, ratA = hyp_identify(odeA, _A, 1 - nu, nu + 2, 2, 1 - x, sub)
    # jets at r_h from F(0) = 1, F'(0) = a b/c (sympy's 2F1), x = r^2/mu, psi = F_P(1 - x), A = (1 - x) F_A(1 - x)
    FP, FA = sp.hyper([-nu, nu + 1], [1], z), sp.hyper([1 - nu, nu + 2], [2], z)
    FP0, FP1 = sp.simplify(FP.subs(z, 0)), sp.simplify(sp.diff(FP, z).subs(z, 0))
    FA0 = sp.simplify(FA.subs(z, 0))
    xr = (2*r/mu).subs(r, s)                                   # dx/dr at r_h
    psi_h, dpsi_h = FP0, -FP1*xr
    kk = 4*nu*(nu + 1)
    J = sp.Matrix([[0, dpsi_h, psi_h],
                   [0, -kk*s**2/2*dpsi_h, kk*s**2/2*psi_h],
                   [-xr*FA0, FA0*s**2/mu, 0]])                # u3: A'(r_h) = -x' F_A(0), -A/f = F_A r^2/mu
    detJ = sp.factor(J.det())
    jets_ok = sp.simplify(detJ + kk**2) == 0
    # the horizon recursion with the order k symbolic: the coefficient of (r - s)^(k - 1) of r^p E[U (r - s)^k]
    k, y = sp.Symbol('k'), sp.Symbol('y', positive=True)
    Us = sp.symbols('U_a U_b U_c')
    mon = (r - s)**k
    rows = []
    for e, pw in zip(sys_scalar(Us[0]*mon, Us[1]*mon, Us[2]*mon, kap), (3, 4, 3)):
        ee = sp.powsimp(sp.expand(e*r**pw/(r - s)**(k - 1)), force=True)
        ee = sp.expand(sp.powsimp(sp.expand(sp.simplify(ee.subs(r, s + y))), force=True))
        rows.append([sp.factor(ee.subs(y, 0).coeff(u_)) for u_ in Us])
    Mk = sp.Matrix(rows)
    rec_ok = sp.simplify(Mk - (-2*s**2*k)*sp.diag(k - 1, s*(k + 1), k)) == sp.zeros(3)
    a0 = sp.factor(sp.expand(sp.simplify((sys_scalar(Us[0], Us[1], Us[2], kap)[0]*r**3).subs(r, s + y))).subs(y, 0))
    a0_ok = sp.simplify(a0 - kap*s*Us[0]) == 0
    # growth at infinity: psi ~ C_P (r^2/mu)^nu, A ~ -C_A (r^2/mu)^nu (C_A that of F_A, times (1 - x))
    CP, CA = lead_coeff(-nu, nu + 1, 1), lead_coeff(1 - nu, nu + 2, 2)
    numP, numA = lead_numeric(-nu, nu + 1, sp.Integer(1), NUS), lead_numeric(1 - nu, nu + 2, sp.Integer(2), NUS)
    def nonzero(co):
        """a product of signs, powers of nu, nu + 1, mu and Gamma functions of positive arguments: nonzero for nu > 0"""
        for fa in sp.Mul.make_args(sp.factor(co)):
            base = fa.base if fa.is_Pow else fa
            if base.is_number:
                if base == 0:
                    return False
                continue
            if isinstance(base, sp.gamma):
                if not positive_sum(base.args[0], [nu]):
                    return False
                continue
            if not (positive_sum(base, [nu, s]) or positive_sum(-base, [nu, s])):
                return False
        return True
    want, lims, exact = scalar_growth()                      # u_1, u_2, u_3: l - 1, l + 1, l
    p_claim = -gap_from_l2()['gap'][0]                         # round 10: the threshold r^1 is the claim's (L2's gap)
    exp_ok = all(exact)
    coefs = [q_ for L_ in lims for q_ in L_ if q_ != 0]
    nz_ok = len(coefs) == 6 and all(nonzero(co) for co in coefs)
    exps = want
    distinct = len(set(want)) == 3
    if control:
        # the same growth reading at l = 1 (nu = 1/2): u_1 = d(psi S) has Cartesian growth exactly r^0, so the least
        # exponent is below 1 and the conclusion fails: the four l = 1 kernel forms of (A71), at every weight in (-1, 0)
        sub_h = {nu: HALF}
        want_h, lims_h, exact_h = scalar_growth(HALF)
        exact = all(exact_h)
        least = min(want_h)
        print("  N2 control (the same path at l = 1, nu = 1/2): leading Cartesian coefficients %s (exact growths "
              "%s: %s); the least exponent %s >= %s (the claim's threshold): %s"
              % (lims_h, want_h, exact, least, p_claim, least >= p_claim), flush=True)
        return exact and least >= p_claim
    n_ = sp.Symbol('n', nonnegative=True)                    # l = 2 + n, nu = 1 + n/2: l - 1 - p_claim = n >= 0
    least_ok = all(c_ >= 0 for c_ in sp.Poly(sp.expand((2*nu - 1 - p_claim).subs(nu, 1 + n_/2)), n_).coeffs())
    ok = (all(solves) and hP and hA and jets_ok and rec_ok and a0_ok and exp_ok and nz_ok and distinct and least_ok
          and numP < 1e-9 and numA < 1e-9)
    print("  N2: u_1, u_2, u_3 solve (R8.1), kappa symbolic: %s; in x = r^2/mu the psi- and A-equations are multiples "
          "%s, %s of the hypergeometric operators (-nu, nu + 1; 1), (1 - nu, nu + 2; 2): %s, %s; jet determinant %s "
          "(= -kappa^2: %s); horizon recursion matrix %s (= -2 s^2 k diag(k - 1, s (k + 1), k): %s), order 0 a-row "
          "%s (forces a(r_h) = 0: %s); leading coefficients %s, %s (mpmath at nu = 1/2..9/2, worst relative "
          "error %.1e, %.1e); leading Cartesian coefficients (a, b, c/r) of u_1, u_2, u_3 at r^(l - 1), r^(l + 1), r^l: "
          "%s (finite, not all 0: %s), nonzero "
          "coefficients for nu > 0: %s; distinct: %s; least exponent l - 1 >= 1 for every l >= 2: %s"
          % (solves, ratP, ratA, hP, hA, detJ, jets_ok, Mk, rec_ok, a0, a0_ok, CP, CA, numP, numA, lims, exp_ok,
             nz_ok, distinct, least_ok), flush=True)
    return ok


# ----------------------------------------------------------------------------------------------------------------- N3
def n3(control=False):
    l = sp.Symbol('l', positive=True)
    ps = sp.Function('psi')(r)
    lam = l**2 if control else (l + 1)**2
    ode = r*sp.diff(r*f_*sp.diff(ps, r), r) - lam*ps
    a, b = -(l + 1)/2, (l + 1)/2
    hv, rat = hyp_identify(ode, ps, a, b, 1, sp.Integer(1), {})
    C = lead_coeff(a, b, sp.Integer(1))
    num = lead_numeric(a.subs(l, 2*nu - 1), b.subs(l, 2*nu - 1), sp.Integer(1), NUS)
    pos = all(sp.gamma(q).subs(l, sp.Symbol('m_', positive=True)).is_positive for q in (l + 1, (l + 1)/2, (l + 3)/2))
    # psi ~ C (r^2/mu)^((l + 1)/2): Cartesian size psi/r ~ r^l (the limit of psi/r^(l + 1) finite and nonzero),
    # excluded by o(r) for l >= 1
    e_ = sp.simplify(sp.powsimp(sp.expand_power_base(C*(r**2/mu)**((l + 1)/2)/r/r**l, force=True), force=True))
    lim = sp.simplify(sp.limit(e_, r, sp.oo))
    expo = l
    excl = lim.is_finite is not False and lim != 0 and lim not in (sp.oo, sp.zoo, sp.nan)
    tag = "  N3 control (lambda = l^2 in place of (l + 1)^2)" if control else "  N3"
    print("%s: the vector equation in x is %s times the hypergeometric operator ((l + 1)/2, -(l + 1)/2; 1): %s; the "
          "horizon-regular solution grows like r^(l + 1) with coefficient %s (positive: %s; mpmath worst relative "
          "error %.1e); psi/r ~ %s r^%s, excluded at every weight beta > -1 for l >= 1: %s"
          % (tag, rat if hv else "not a multiple", hv, C, pos, num, lim, expo, excl), flush=True)
    return hv and pos and excl and num < 1e-9


# ----------------------------------------------------------------------------------------------------------------- N4
def n4(control=False):
    k, y = sp.Symbol('k'), sp.Symbol('y', positive=True)
    Us = sp.symbols('U_a U_b U_c')
    shift = sp.Rational(1, 3) if control else 0              # control: a non-integral exponent pattern
    mon = (r - s)**k
    rows = []
    for e, pw in zip(sys_scalar(Us[0]*mon, Us[1]*mon, Us[2]*mon, kap), (3, 4, 3)):
        ee = sp.powsimp(sp.expand(e*r**pw/(r - s)**(k - 1)), force=True)
        ee = sp.expand(sp.powsimp(sp.expand(sp.simplify(ee.subs(r, s + y))), force=True))
        rows.append([sp.factor(ee.subs(y, 0).coeff(u_)) for u_ in Us])
    det = sp.factor(sp.Matrix(rows).det().subs(k, k + shift))
    ex_s = sp.roots(sp.Poly(det, k))
    # vector: r (r f psi')' = lambda psi with psi = (r - s)^k: the coefficient of (r - s)^(k - 1)
    ps = (r - s)**k
    ev = sp.powsimp(sp.expand((r*sp.diff(r*f_*sp.diff(ps, r), r) - kap*ps)/(r - s)**(k - 1)), force=True)
    ev = sp.expand(sp.powsimp(sp.expand(sp.simplify(ev.subs(r, s + y))), force=True)).subs(y, 0)
    ex_v = sp.roots(sp.Poly(sp.factor(ev.subs(k, k + shift)), k))
    integral = all(q.is_integer for q in ex_s) and all(q.is_integer for q in ex_v)
    count = sum(ex_s.values()) == 6 and sum(ex_v.values()) == 2
    # round 10 (the round-9 verifier's Minor 3): the values, as R9.c states them, not only their integrality
    values = ex_s == {-1: 1, 0: 4, 1: 1} and ex_v == {0: 2}
    tag = "  N4 control (exponents shifted by 1/3)" if control else "  N4"
    print("%s: horizon exponents of the scalar system %s (det %s), of the vector equation %s; = {-1: 1, 0: 4, 1: 1} "
          "and {0: 2}: %s; all integers, 6 and 2 with multiplicity: %s: a solution smooth across r_h vanishing on "
          "r > r_h vanishes on (r_0, r_h)" % (tag, ex_s, det, ex_v, values, integral and count), flush=True)
    return integral and count and values


# ----------------------------------------------------------------------------------------------------------------- N5
def l0_solutions():
    Ws = (WSTAR[0], WSTAR[1])
    dv = (-f_, sp.Integer(1))
    uc = (sp.Integer(0), (r**2 + mu)/r)
    us = (sp.Integer(0), 1/(r*(r**2 - mu)))
    return {"W*": Ws, "(d_v)^flat": dv, "(0, (r^2 + mu)/r)": uc, "(0, 1/(r (r^2 - mu)))": us}


_KC = {}


def kernel_counts():
    """round 10 (the round-9 verifier's Minor 2): every input of N5's and N6's counts computed.  The l = 0 kernel from
    the four l = 0 solutions; the threshold from L2's computed gap; the scalar l = 1 count from N2's growth reading at
    nu = 1/2 (the solutions' exponents are distinct, so the count is the number of exponents below the threshold);
    the vector l = 1 count from N3's at l = 1; the representation dimensions and the class's G-fixed dimensions from
    N1's model"""
    if _KC:
        return _KC
    sols = l0_solutions()
    solve = {k_: all(sp.simplify(e_) == 0 for e_ in sys_scalar(a_, b_, sp.Integer(0), 0)[:2])
             for k_, (a_, b_) in sols.items()}
    rr = 2*s
    W = sp.Matrix([[a_.subs(r, rr), sp.diff(a_, r).subs(r, rr), b_.subs(r, rr), sp.diff(b_, r).subs(r, rr)]
                   for a_, b_ in sols.values()])
    indep = sp.simplify(W.det()) != 0
    smooth, grow = {}, {}
    for k_, (a_, b_) in sols.items():
        smooth[k_] = all(sp.limit(c_, r, s).is_finite for c_ in (a_, b_)) and \
            all(sp.limit(sp.diff(c_, r), r, s).is_finite for c_ in (a_, b_))
        ex = None
        for p_ in (-2, -1, 0, 1):
            if all(sp.limit(c_*r**(-p_), r, sp.oo).is_finite for c_ in (a_, b_)) and \
                    any(sp.limit(c_*r**(-p_), r, sp.oo) != 0 for c_ in (a_, b_)):
                ex = p_
                break
        grow[k_] = ex
    p_claim = -gap_from_l2()['gap'][0]                         # growth below r^p_claim at the weights of (-1, 0)
    ker = [k_ for k_ in sols if smooth[k_] and grow[k_] is not None and grow[k_] < p_claim]
    ker02 = [k_ for k_ in sols if smooth[k_] and grow[k_] is not None and grow[k_] < 0]
    want_h, lims_h, exact_h = scalar_growth(HALF)
    distinct = len(set(want_h)) == 3
    l1_scalar = sum(1 for w_ in want_h if w_ < p_claim) if all(exact_h) and distinct else None
    ev1, limv, exv = vector_growth(1)
    l1_vector = (1 if ev1 < p_claim else 0) if exv else None
    M = model(2)
    dimH = {m_: sum(1 for mm, _ in M['H'] if mm == m_) for m_ in (0, 1)}
    # the class: the G-fixed vectors of dt (x) H_m (the torus and the reflections x2 -> -x2, x4 -> -x4)
    nH = M['nH']
    fixG = {}
    for m_ in (0, 1):
        idx = [i_ for i_, (mm, _) in enumerate(M['H']) if mm == m_]          # the dt block, fibre index 0
        blk = lambda D: D.to_Matrix().extract(idx, idx)
        St = sp.Matrix.vstack(blk(M['X'][(0, 1)]), blk(M['X'][(2, 3)]), blk(M['R'][1]) - sp.eye(len(idx)),
                              blk(M['R'][3]) - sp.eye(len(idx)))
        fixG[m_] = len(St.nullspace())
    P, _, _, _ = iso_projections(M)
    dim_vec1 = P[(1, 0)].rank() + P[(0, 1)].rank()
    full = len(ker)*dimH[0] + (l1_scalar or 0)*dimH[1] + (l1_vector or 0)*dim_vec1
    cls = len(ker)*fixG[0] + (l1_scalar or 0)*fixG[1]                      # no vector type in the class (N1)
    _KC.update(solve=solve, indep=indep, smooth=smooth, grow=grow, ker=ker, ker02=ker02, p_claim=p_claim,
               l1_scalar=l1_scalar, l1_vector=l1_vector, want_h=want_h, dimH=dimH, fixG=fixG, dim_vec1=dim_vec1,
               full=full, cls=cls, nH=nH)
    return _KC


def n5(control=False):
    K = kernel_counts()
    if control:
        # the same count at the weights of (0, 2) (decay required): 1, not 2
        print("  N5 control (the same count at weights in (0, 2)): kernel %s, dimension %d (2 asked)"
              % (K['ker02'], len(K['ker02'])), flush=True)
        return len(K['ker02']) == 2
    ok = (all(K['solve'].values()) and K['indep'] and K['ker'] == ["W*", "(d_v)^flat"] and K['ker02'] == ["W*"]
          and not K['smooth']["(0, 1/(r (r^2 - mu)))"] and K['l1_scalar'] == 1 and K['l1_vector'] == 0
          and K['cls'] == 2 and K['full'] == 6)
    print("  N5: l = 0 solutions %s; independent: %s; smooth at r_h %s; growth exponents %s; kernel at weights in "
          "(-1, 0) (growth below r^%s, from L2's gap): %s, in (0, 2): %s; scalar l = 1: %s per harmonic (N2's "
          "exponents at nu = 1/2: %s), vector l = 1: %s (N3 at l = 1), l >= 2: none (N2, N3); harmonics of degree "
          "0, 1: %s, G-fixed among them %s (N1's model), vector l = 1 dimension %d: the kernel is %d-dimensional in "
          "the class and %d-dimensional on all 1-forms: %s"
          % (K['solve'], K['indep'], K['smooth'], K['grow'], K['p_claim'], K['ker'], K['ker02'], K['l1_scalar'],
             K['want_h'], K['l1_vector'], K['dimH'], K['fixG'], K['dim_vec1'], K['cls'], K['full'], ok), flush=True)
    return ok


# ----------------------------------------------------------------------------------------------------------------- N6
def n6(control=False):
    K = kernel_counts()
    rep = {}
    mult = {}
    for name, (kk, with_c) in {"l = 0": (0, False), "scalar l = 1": (3, True)}.items():
        M, lam = indicial_scalar(kk, with_c=with_c)
        dt = sp.factor(M.det())
        simple = dt.subs(lam, 0) == 0 and sp.diff(dt, lam).subs(lam, 0) != 0
        nullity = M.shape[0] - M.subs(lam, 0).rank()
        mult[name] = nullity if simple else None
        rep[name] = (dt, simple, nullity)
    dv1, lamv = indicial_vector(4)                              # vector l = 1, from L2's computation
    vec1 = sp.expand(dv1).subs(lamv, 0) != 0
    dims = {"l = 0": K['dimH'][0], "scalar l = 1": K['dimH'][1]}            # N1's model
    fix = {"l = 0": K['fixG'][0], "scalar l = 1": K['fixG'][1]}
    if control:
        dims["scalar l = 1"] = 1                               # the representation dimension dropped
    jump_cl = sum(mult[k_]*fix[k_] for k_ in mult)
    jump_full = sum(mult[k_]*dims[k_] for k_ in mult)
    cok02 = 1                                                  # READ: III.D' Lemma 2.1 (3), cokernel span{ell}
    ind02 = len(K['ker02']) - cok02                            # kernel span{W*} at (0, 2): N5 (III.D' Lemma 2.1 (2))
    ker_cl, ker_full = K['cls'], K['full']                     # N5
    # deduced (standard: the relative index theorem): ind(-1, 0) = ind(0, 2) + the jump; cokernel = kernel - index
    cok_cl, cok_full = ker_cl - (ind02 + jump_cl), ker_full - (ind02 + jump_full)
    ok = vec1 and None not in mult.values() and cok_cl == 1 and cok_full == 1 and jump_cl == 1 and jump_full == 5
    tag = "  N6 control (the l = 1 root counted once)" if control else "  N6"
    print("%s: (indicial det, root 0 simple, null space dimension) %s; 0 not a root of vector l = 1 (det %s): %s; "
          "computed inputs: dimensions %s, G-fixed %s, kernels %d and %d at (-1, 0), %d at (0, 2) (N5); the index "
          "arithmetic, deduced (the relative index theorem): jumps %d in the class and %d on all 1-forms, cokernels "
          "%d and %d (the deduced span{ell}: 1 and 1): %s" % (tag, rep, dv1, vec1, dims, fix, ker_cl, ker_full,
                                                             len(K['ker02']), jump_cl, jump_full, cok_cl, cok_full,
                                                             ok), flush=True)
    return ok


# ----------------------------------------------------------------------------------------------------------------- N7
def mean_s3(u):
    return sp.simplify(2*sp.integrate(sp.expand(sp.expand_trig(u*sp.sin(th)*sp.cos(th))), (th, 0, sp.pi/2)))


def n7(control=False):
    a, b, c = [sp.Function(n_)(v, r) for n_ in ("a", "b", "c")]
    gam = sp.diag(1, sp.cos(th)**2, sp.sin(th)**2)
    out = []
    ok = True
    for j in (1, 2):
        S = sp.legendre(j, sp.cos(2*th)) + (sp.Rational(1, 7) if control else 0)
        Z = [a*S, b*S, c*sp.diff(S, th), 0, 0]
        h = GEO.lie(Z)
        Hh = sum(h[2 + i][2 + i]/gam[i, i] for i in range(3))/(6*r**2)
        ms = [mean_s3(h[0][0]), mean_s3(h[0][1]), mean_s3(h[1][1]), mean_s3(Hh)]
        out.append((2*j, ms))
        ok &= all(m_ == 0 for m_ in ms)
    if control:
        print("  N7 control (S + 1/7): l = 0 parts of L_Z g %s" % out, flush=True)
        return ok
    a0, b0 = sp.Function('a0')(v, r), sp.Function('b0')(v, r)
    h0 = GEO.lie([a0, b0, 0, 0, 0])
    sym = all(sp.simplify(h0[i][j_]) == 0 for i in range(2) for j_ in range(2, 5))
    sym &= all(sp.simplify(sp.diff(h0[i][j_], th)) == 0 for i in range(2) for j_ in range(2))
    ang = sp.Matrix(3, 3, lambda i, j_: h0[2 + i][2 + j_])
    sym &= sp.simplify(ang - ang[0, 0]*gam) == sp.zeros(3)
    print("  N7: l = 0 parts (means of h_vv, h_vr, h_rr, H) of L_Z g for class Z of degree l: %s; L_{Z_0} g "
          "spherically symmetric for Z_0 = a_0 dv + b_0 dr: %s; so (L_Z g)_>=2 = L_{Z_>=2} g" % (out, sym), flush=True)
    return ok and sym


# ----------------------------------------------------------------------------------------------------------------- N8
def n8(control=False):
    mpmath.mp.dps = 30
    rows = []
    ok = True
    for l in range(4):
        n_ = l + 1
        big, small = mpmath.mpf(10)**6, mpmath.mpf(10)**-6
        H1 = lambda q: mpmath.hankel1(n_, q)/q
        H2 = lambda q: mpmath.hankel2(n_, q)/q
        g1 = lambda q: mpmath.exp(-1j*q)*H1(q)
        g2 = lambda q: mpmath.exp(1j*q)*H2(q)
        amp = [abs(g1(big))*big**1.5, abs(g2(big))*big**1.5]
        cl = abs(amp[0] - mpmath.sqrt(2/mpmath.pi)) < 1e-5 and abs(amp[1] - mpmath.sqrt(2/mpmath.pi)) < 1e-5
        dg = [abs(big*mpmath.diff(g1, big))*big**1.5, abs(big*mpmath.diff(g2, big))*big**1.5]
        osc = abs(big*mpmath.diff(lambda q: mpmath.exp(-2j*q)*g2(q), big))*big**0.5
        conormal = all(d_ < 10 for d_ in dg) and abs(osc - 2*mpmath.sqrt(2/mpmath.pi)) < 1e-4
        ztf = abs(H2(small))*small**(l + 2)
        ztf_ok = abs(ztf - 2**(l + 1)*mpmath.factorial(l)/mpmath.pi) < 1e-6
        # the Bessel equation (L8): -u'' - 3u'/r + l(l+2)u/r^2 - u = 0 for u = H(r)/r, numerically at r = 3
        q0 = mpmath.mpf(3)
        res = -mpmath.diff(H2, q0, 2) - 3/q0*mpmath.diff(H2, q0) + l*(l + 2)/q0**2*H2(q0) - H2(q0)
        ode_ok = abs(res) < 1e-15
        rows.append((l, cl, conormal, ztf_ok, ode_ok))
        ok &= cl and conormal and ztf_ok and ode_ok
    # exact exponent arithmetic: |g|^2 r^(2 r') r^3 with |g| ~ c r^-3/2: integrable at oo iff 2 r' < -1
    rp, B = sp.Symbol('rp', real=True), sp.Symbol('B', positive=True)
    integrand_exp = 2*rp - 3 + 3
    r_out = -HALF + B                                           # R_out: the X* order exceeds -1/2
    r_in = -HALF - B                                            # R_in: below -1/2 for an admissible choice
    test_in = r_out if control else r_in
    excl_out = positive_sum(sp.simplify(integrand_exp.subs(rp, r_out) + 1), [B])      # >= -1: divergent
    admit_in = positive_sum(sp.simplify(-1 - integrand_exp.subs(rp, test_in)), [B])  # < -1: convergent
    tag = "  N8 control (R_in's order replaced by R_out's)" if control else "  N8"
    print("%s: (l, |g_j| r^(3/2) -> (2/pi)^(1/2), g_j conormal and e^(-2ir) g_2 not, |f_2| r^(l+2) -> 2^(l+1) l!/pi, "
          "Bessel equation): %s; at R_out g_1 excluded: %s; at R_in e^(-2ir) g_2 admitted: %s"
          % (tag, rows, excl_out, admit_in), flush=True)
    return ok and excl_out and admit_in


CHECKS = [("N1", n1), ("N2", n2), ("N3", n3), ("N4", n4), ("N5", n5), ("N6", n6), ("N7", n7), ("N8", n8)]


def selftest():
    """the harness: positive_sum, the growth exponent reader and the DomainMatrix projections each told a true and a
    false statement"""
    B = sp.Symbol('B', positive=True)
    t1 = positive_sum(B + 1, [B]) and not positive_sum(B - 1, [B])
    Id = DomainMatrix.eye(2, QQ)
    Pm = DomainMatrix.from_Matrix(sp.Matrix([[1, 0], [0, 0]])).convert_to(QQ)
    t2 = (Pm*Pm - Pm).is_zero_matrix and not ((Id + Pm)*(Id + Pm) - (Id + Pm)).is_zero_matrix
    t3 = abs(float(lead_coeff(sp.Integer(-1), sp.Integer(2), sp.Integer(1))) - 2.0) < 1e-12   # 2F1(-1,2;1;z) = 1-2z
    t4 = lead_numeric(-nu, nu + 1, sp.Integer(1), [sp.Integer(1)]) < 1e-9 and \
        lead_numeric(-nu, nu + 1, sp.Integer(1), [sp.Integer(1)], pred=lead_coeff(-nu, nu + 2, sp.Integer(1))) > 1e-3
    ok = t1 and t2 and t3 and t4
    print("selftest: positive_sum %s, projections %s, DLMF leading coefficient %s, mpmath check %s: %s"
          % (t1, t2, t3, t4, "PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    if "--selftest" in sys.argv[1:]:
        return selftest()
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
