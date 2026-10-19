# N1*: the proof

Commissioned at item 522 (N1STAR-LOG.md D7). Labels: **computed** (an instrument here, with a selftest whose mutants
it catches), **deduced** (an argument written out here, or a standard theorem invoked **READ** with its hypotheses
checked), **READ** (verbatim at source), **OPEN**.

**Status (2026-10-19).** N1* reduces to three theorems. **Theorem E** (evolution: existence on the domain and
lam-uniform estimates for the remainder, given an approximant and data) is proved in sections 1-4 (deduced; its
exact inputs computed in `ks5.py`, `foliation5.py`, `ansatz5.py`). **Theorem A** (the approximant to any order in the
gauge used here) is proved in section 5 from given stage data (deduced; its leading order computed in `lead5.py`).
**The data** -- stage data whose approximant satisfies the constraints to order K, and an exact vacuum datum within
O(lam^K) of it (Theorem D) -- are **OPEN**; section 6 shows why Touati's construction does not transfer as it stands
and proposes the route. Independent verification of sections 1-5 is pending. N1* is therefore **not yet proved**.

The proof differs from Touati's [Tou23a] in one decision: the approximant is carried to high order K, so that the
remainder is O(lam^K) and every nonlinear term is beaten by a power of lam rather than by the size eps of the data.
What then has to be uniform in lam is a *linear* estimate on the large background, and it is: its only coefficient
of size 1/lam couples one scalar component of the remainder to the wave, that component's own equation has no such
coefficient, and the coupling is absorbed by a phase shift of the wave (Lemma 3.3), exactly as in [Tou23a] section
3.2.3, with a compactly supported mollifier in place of his Fourier cut-off.

## 0. The statement

### 0.1 Coordinates and background (computed, `ks5.py` K1-K5)

X = (tau, x) in R x R^4, r = |x|, xhat = x/r, v = tau + r. The T^2 action is the rotation of the planes (x1, x2)
and (x3, x4); its axes are regular points of R^4, and every tensor below is an array of Cartesian components.

    g0 = eta + (mu(v)/r^2) dv dv,   g0^-1 = eta^-1 - (mu/r^2) L0 L0,   L0 = d_tau - xhat.d_x,   det g0 = -1,

with mu smooth, nondecreasing, mu >= mu0 > 0, constant for v <= v_start and for v >= v_end. g0 is five-dimensional
Vaidya (K1), Ric(g0) = F0^2 dv dv with F0^2 = 3 mu'/(2 r^3) (`ansatz5.py` A2). The phase is v; ell := g0^-1 dv = -L0
is null and geodesic, L0(v) = 0, L0(tau) = 1, L0(r) = -1 (K2). box~ := g0^{ab} d_a d_b acting componentwise, and
(K3), for every function u,

    [L0, box~] u = (2/r) (box~ u + (d_tau + d_r) L0 u) - (3/r^2) d_r u,      d_r = xhat.d_x.            (0.1)

H0^rho := g0^{ab} Gamma[g0]^rho_ab = (-mu/r^3, mu x^i/r^4) (K5), smooth on r > 0.

### 0.2 The reduced equations

The gauge is the wave-map gauge relative to g0. For a Lorentzian metric g put

    D^rho(g) := g^{ab} (Gamma[g]^rho_ab - Gamma[g0]^rho_ab),    Ric^H(g)_mn := Ric(g)_mn
                - (1/2)(g_{m rho} Dh_n D^rho + g_{n rho} Dh_m D^rho)
              = -(1/2) g^{ab} d_a d_b g_mn + Q_mn(X; g)(dg, dg),                                              (0.2)

Dh the covariant derivative of g0. D is a vector field and Ric^H a tensor, built from g and g0 alone, so both are
invariant under the isometries of g0 (O(4), with T^2 and both reflections) and may be computed in any coordinates. In
the coordinates of 0.1, Q is a quadratic polynomial in dg (with a linear and a constant part) whose coefficients are
rational in g and smooth in X through Gamma[g0] and its first derivatives (smooth on r > 0; its trace is H0 of K5).
(Deduced: the standard decomposition Ric_mn = -(1/2) g^{ab} d_a d_b g_mn + (1/2)(g_{m rho} d_n G^rho + g_{n rho} d_m
G^rho) + (quadratic in dg), G^rho = g^{ab} Gamma[g]^rho_ab, standard, e.g. Ringstrom, *The Cauchy problem in general
relativity*, EMS 2009; D differs from G by g^{ab} Gamma[g0]_ab, which has no derivative of g, and Dh D from d
D by Gamma[g0] D.) Second derivatives of g enter (0.2) only through -(1/2) g^{ab} d_a d_b g. D(g0) = 0, so Ric^H(g0) =
Ric(g0). Ric^H(g) = 0 is a quasilinear wave system; a solution with D = 0 is vacuum.

### 0.3 Profiles and scaled norms

A *profile* is a smooth f(X, th) on Omega x S^1, S^1 = R/2piZ; [f](X) := f(X, v(X)/lam); <f> is its th-mean. For a
function or tensor f on Sigma_tau := Omega cap {tau} (Omega in section 1), with d^j all spacetime coordinate
derivatives of order j and ||.|| the flat L^2(Sigma_tau),

    |f|_j := sum_{i<=j} lam^i ||d^i f||.                                                                  (0.3)

Chain rule: d_a [f] = lam^-1 (d_a v)[d_th f] + [d_a f], so |[f]|_j <= C_j sup_{i<=j} |d^i_{(X,th)} f|_{L^inf}
(the oscillation costs nothing in scaled norms), and ||d^i [f]||_{L^inf} <= C lam^-i.

### 0.4 Theorem E (evolution) -- proved in sections 1-4 (deduced), verification pending

Fix k = 6 and K >= 6. Let

    g_app = g0 + lam [g1] + sum_{j=2}^{N} lam^j [g_j],      g_j profiles,                                  (0.4)

with every d^i_{(X,th)} g_j bounded on Omega x S^1 independently of lam, and

- (E1) *transversality of the wave*: (g1 - <g1>)(ell, .) = 0 for all (X, th) (the mean <g1> is unrestricted);
- (E2) *the leading equation*: the lam^0 coefficient R^(0)(X, th) of the two-scale expansion of Ric^H(g_app)
  (section 3.1) vanishes identically in (X, th);
- (E3) *the residual*: |Ric^H(g_app)|_k (tau) <= C_R lam^K on [tau0, tau_end];
- (E4) *the data*: g is a Cauchy datum on Sigma_tau0 for Ric^H(g) = 0 with w := g - g_app satisfying
  Data(w) := ||w|| + sum_{1<=j<=k+1} lam^(j-1) ||d_x^j w|| + sum_{j<=k} lam^j ||d_x^j d_tau w|| <= C_D lam^K on
  Sigma_tau0.

Then there are lam0 > 0 and M, depending on Omega, k, K, C_R, C_D and the bounds on the profiles but not on lam, such
that for 0 < lam <= lam0 the solution g of Ric^H(g) = 0 with these data exists on Omega, is unique there (smooth if
the data are), and

    w = h + phi [d_th g1],   with   N(tau) <= M lam^K   on [tau0, tau_end],                               (0.5)

N the quantity (4.1) (energies of h, phi, box~ phi to order k, scaled). In particular ||w(tau)|| + ||d w(tau)||
<= M lam^(K-1), |w| <= M lam^(K-3) and |d w| <= M lam^(K-4) on Omega, and |g - g0| <= C lam, |d g| <= C.

### 0.5 Theorem A (the approximant) -- proved in section 5 from given stage data; the choice of data OPEN

For every N and every smooth choice of stage data there are profiles g1, ..., g_N with (E1)-(E3), K = N - 1, whose
oscillating part of g1 is the record's waves (F, G of the instructions, section 2) with a second harmonic chi dv dv
and a phase shift, on the background g0 with mu' = (2/9) A^2 env^2. For N1* the stage data must in addition make the
approximant's Cauchy data satisfy the constraints and D = 0 to order K (section 6, OPEN).

### 0.6 Theorem D (the data) -- OPEN

For lam small there is a vacuum Cauchy datum (gamma, kappa) on Sigma_tau0 (the constraints hold exactly), with the
gauge condition D = 0 imposed through d_tau g, whose w satisfies (E4).

### 0.7 How N1* follows

Given A and D, Theorem E gives g_lam on Omega. D(g_lam) solves a homogeneous linear wave system (contracted Bianchi
identity) with D = d_tau D = 0 on Sigma_tau0 (the gauge condition and the constraints), so D = 0 on Omega and g_lam is
vacuum (deduced; the standard argument, e.g. Ringstrom 2009, with Omega inside the domain of dependence of
Sigma_tau0 cap Omega, Lemma 1.1(e)). Its T^2 x Z2 x Z2 invariance follows from uniqueness, since Ric^H and D are built
from g and the O(4)-invariant g0 alone (0.2) and the data are invariant. D_T cap {tau >= tau0} lies in Omega (Lemma
1.1). Hence (i) on D_T cap {tau >= tau0} with the data on Sigma_tau0 (the instructions' route W item 4: "construct
Cauchy data on a slice before the shell reaches the hole ... restate (i) on it"); the remainder estimate is (0.5); no
derivative is lost (the bootstrap of section 4 closes at the fixed order k); the formulation is regular across the
axes (Cartesian arrays on R^4); the background is the large g0. (ii): |g_lam - g0| <= C lam; d g_lam bounded; d g_lam
- d g0 = dv [d_th g1] + O(lam) tends to zero weakly since <d_th g1> = 0. The rates of (ii)-(iii) beyond these rest on
Theorem A's profiles.

## 1. The domain

Fix T > 0, V := v_end + T, q0 := r_q(mu0) = (sqrt(72) mu0 l5^2)^(1/4), so q0 <= sqrt(mu0) (the seed condition
mu0 >= sqrt(72) l5^2). Fix 0 < delta0 < q0, a := q0 - delta0, tau0 with v_start - tau0 > sqrt(mu0) + 1 (on
Sigma_tau0 the shell lies outside the seed's horizon: the slice is before the shell reaches the hole), and
tau_end := max_{v <= V} (v - r_q(v)),

    Omega := { tau0 <= tau <= tau_end,  |x| >= a,  v + (tau - tau_end) <= V + 1 }.                         (1.1)

Sigma_tau = A(tau) := { a <= |x| <= b(tau) }, b(tau) = V + 1 - tau + (tau_end - tau).

**Lemma 1.1** (deduced from `foliation5.py` B1, B4 and `ks5.py` K2; the three contractions computed in K2's
g0^-1). (a) Each Sigma_tau is spacelike: g0^-1(dtau, dtau) = -1 - mu/r^2. (b) {r = a} is spacelike and r decreases
along future causal curves near it: g0^-1(dr, dr) = 1 - mu/r^2 <= 1 - mu0/a^2 < 0 and g0^-1(dr, dtau) = mu/r^2 > 0.
(c) {v + tau = const} is spacelike and v + tau increases along future causal curves: g0^-1 of d(v + tau) is
-2 - (1 + mu/r^2) < 0, g0^-1(dv, dtau) = -1. (d) L0 is future null with L0(tau) = 1, L0(v) = 0, L0(r) = -1; the
integral curve of L0 through any point of Omega, followed to the past, stays in Omega and meets Sigma_tau0. (e) There
is eps1 > 0 such that for every Lorentzian g with |g - g0| <= eps1 on Omega, J^-(p; g) cap {tau >= tau0} lies in
Omega for every p in Omega, Sigma_tau and the two lateral boundaries stay spacelike for g, and L0 stays transverse
to Sigma_tau. (f) b(tau) - a >= 1 + delta0, b <= b(tau0), and D_T cap {tau >= tau0} lies in Omega.

*Proof.* (a)-(c) are the contractions of g0^-1 = eta^-1 - (mu/r^2) L0 L0 with L0(tau) = 1, L0(r) = -1, L0(v) = 0:
g0^-1(dtau, dtau) = -1 - mu/r^2, g0^-1(dr, dr) = 1 - mu/r^2, g0^-1(dr, dtau) = 0 - (mu/r^2)(-1)(1),
g0^-1(dv, .) = ell = -L0. For (b): at r = a < q0 <= sqrt(mu0) <= sqrt(mu), dr and dtau are timelike with
g0^-1(dr, dtau) > 0, so grad r lies in the cone opposite to grad tau, which is past directed; hence grad r is future
directed and dr(Y) = g0(grad r, Y) < 0 for future causal Y. (c): dv(Y) = -g0(L0, Y) >= 0 and dtau(Y) > 0 for future
causal Y. (d): along -L0, tau decreases, r increases and v is fixed, so r >= a and v + (tau - tau_end) <= V + 1 are
kept. (e): the strict inequalities in (a)-(c) and L0(tau) = 1 are open conditions in g on the compact Omega; a past
causal curve from p cannot cross {r = a} or {v + tau = const} outward, by (b), (c), nor Sigma_tau_end. (f): b
decreases, b(tau_end) = V + 1 - tau_end = min_{v <= V} (V - v + r_q(v)) + 1 >= q0 + 1; a point of D_T has v <= V,
r >= r_q(v) >= q0 > a and tau = v - r <= v - r_q(v) <= tau_end. []

## 2. Inequalities on the slices

All constants below depend on Omega (through a, b(tau0), delta0) and not on lam; 0 < lam <= lam1 := min(1, delta0)/10.

**Lemma 2.1 (Sobolev, products; deduced).** On A(tau), ||f||_{L^inf} <= C sum_{i<=3} ||d_x^i f||, hence
||d^i f||_{L^inf} <= C lam^(-3-i) |f|_{i+3}. For k = 6, |f g|_k <= C lam^-3 |f|_k |g|_k, and if a is a profile,
|[a] f|_k <= C |f|_k. *Proof.* The annuli A(tau) are images of the fixed annulus {a <= |x| <= a + 1 + delta0} under
radial maps with uniformly bounded derivatives of all orders (b - a in [1 + delta0, b(tau0) - a]), so Sobolev's
embedding H^3 into L^inf in four dimensions (standard) holds with a uniform constant; scaling each derivative
by lam gives the second form. For products, distribute lam^k d^k and put the factor with at most three derivatives
in L^inf. The last claim is (0.3)'s chain-rule remark. []

**The mollifier.** Fix rho in C_c^inf(B_1), rho >= 0, int rho = 1, and sigma0 in C^inf([0, 1]) with sigma0 = 1 on
[0, 1/3], sigma0 = -1 on [2/3, 1]. For f on A(tau) put sigma(tau, x) := sigma0((|x| - a)/(b(tau) - a)),
Phi(x) := x + 2 lam sigma xhat and

    P f (x) := int rho(z) f(Phi(x) - lam z) dz        (spatial, at fixed tau).                              (2.1)

Near the inner sphere the ball is shifted outward by 2 lam, near the outer one inward, so Phi(x) - lam z lies in
A(tau): |x + 2 lam xhat - lam z| >= xhat.(x + 2 lam xhat - lam z) >= |x| + lam, and in the middle third the
distance to the boundary is at least (b - a)/3 >= 1/3 > 3 lam. DPhi = I + lam E with E bounded with all derivatives.

**Lemma 2.2 (the mollifier; deduced).** For f on A(tau) and a smooth bounded function or profile a:
(M1) ||P f|| <= C ||f||;  (M2) ||d_x P f|| <= C lam^-1 ||f||;  (M3) ||f - P f|| <= C lam ||d_x f||;
(M4) d_x P f = P(d_x f) + lam E1 P(d_x f), and lam ||P d_x f|| <= C ||f||;
(M5) ||[a, P] d_x f|| <= C ||d_x a||_inf ||f||  and  ||[a, P] f|| <= C lam ||d_x a||_inf ||f||;
(M6) d_tau P f = P(d_tau f) + lam E2 P(d_x f);
with E1, E2 bounded; iterating, lam^j ||d^j P f|| <= C sum_{i<=j} lam^i ||d^i f|| and the same with (1 - P).

*Proof.* For fixed z, x -> Phi(x) - lam z is a diffeomorphism of A(tau) into itself with Jacobian 1 + O(lam), which
gives (M1). P f(x) = lam^-4 int rho((Phi(x) - y)/lam) f(y) dy, and d_x falls on rho: (M2). For (M3), f(x) -
f(Phi(x) - lam z) is the integral of d_x f along the segment from x to Phi(x) - lam z, of length <= 3 lam; the
segment stays in A(tau) by the estimate above (its radial component is at least lam toward the interior near either
sphere), and the change of variables gives the bound. (M4): the chain rule, d_x[f(Phi - lam z)] = DPhi^T (d f)(Phi
- lam z); and (d_j f)(Phi(x) - lam z) = -lam^-1 d_{z_j}[f(Phi(x) - lam z)], integrated by parts onto rho. (M5) is
Friedrichs' lemma in this form: [a, P] d_j f (x) = int rho(z)(a(x) - a(Phi(x) - lam z))(d_j f)(Phi(x) - lam z) dz;
integrating by parts in z as in (M4), the factor lam^-1 meets either d_z of a(Phi(x) - lam z), which is O(lam), or
a(x) - a(Phi(x) - lam z), which is O(lam). (M6): sigma depends on tau through b(tau). Higher derivatives by
induction. []

**Lemma 2.3 (energy; deduced).** Let gt be a Lorentzian metric on Omega with |gt - g0| <= eps1 and
||d gt||_inf <= M1, and let u (a function or a Cartesian array) satisfy -(1/2) gt^{ab} d_a d_b u = f on Omega. Then
for tau in [tau0, tau_end],

    ||d u(tau)|| + ||u(tau)|| <= C(M1) ( ||d u(tau0)|| + ||u(tau0)|| + int_{tau0}^{tau} ||f(s)|| ds ).            (2.2)

*Proof.* With the multiplier Y := -gt^-1 dtau (future timelike, Lemma 1.1(e)) and the energy current
J^a = T^a_b Y^b, T_ab = d_a u d_b u - (1/2) gt_ab gt(du, du), the divergence theorem on Omega cap {tau0 <= s <= tau}
in the coordinate density gives the flux through Sigma_tau equal to the flux through Sigma_tau0 minus the fluxes
through the lateral boundaries plus the bulk. The lateral boundaries are spacelike with Omega to their past (Lemma
1.1(b), (c), (e)), so their fluxes are nonnegative and are dropped; the fluxes through Sigma_tau are comparable to
||d u||^2 (dominant energy, Y and the normal uniformly timelike); the bulk is bounded by C(M1)(||d u||^2 +
||f|| ||d u||) since d gt and d Y are bounded. ||u|| is added through d_tau ||u||^2 = 2 <u, d_tau u> plus a boundary
term b'(tau) int_{|x|=b} |u|^2 <= 0. Gronwall. []

**Lemma 2.4 (transport; deduced, `ks5.py` K4).** If L0 phi - c(X) phi = f on Omega with c bounded, then
||phi(tau)|| <= e^{C(tau - tau0)} (||phi(tau0)|| + int ||f||).

*Proof.* d_tau phi = L0 phi + xhat.d_x phi and int_{A(tau)} 2 phi xhat.d_x phi = int_{|x|=b} phi^2 - int_{|x|=a}
phi^2 - int (3/r) phi^2 (div xhat = 3/r), so d_tau ||phi||^2 = 2 <phi, f + c phi> - int (3/r) phi^2 +
(1 + b') int_{|x|=b} phi^2 - int_{|x|=a} phi^2, and 1 + b' = -1 < 0. Gronwall. []

## 3. The linear structure

### 3.1 Two-scale form

For profiles G(X, th) the operator R[G](X, th; lam) is Ric^H with every d_a replaced by d_a + lam^-1 (d_a v) d_th;
then Ric^H([G]) = [R[G]]. R[G] is polynomial in lam^-1 and contains no explicit th, so

    R[G(., . + c)](X, th) = R[G](X, th + c)   for every constant c.                                        (3.1)

For g_app (0.4), R[g_app-profile] = lam^-1 R^(-1) + R^(0) + lam R^(1) + ...; R^(-1) = -(1/2) g0^-1(dv, dv) d_th^2 g1
= 0, since every other term of (0.2) contains at most first derivatives and d[g_app] is bounded.

### 3.2 The linearisation

Let P(w) := (d/ds) Ric^H(g_app + s w) at s = 0. From (0.2), with g_app^{-1} expanded to second order,

    P(w) = -(1/2) g_app^{ab} d_a d_b w + (1/2) lam^-1 s(w) [d_th^2 g1] + B . d w + C . w,     s(w) := w(ell, ell),  (3.2)

B, C profiles (bounded with all X- and th-derivatives). *Deduced:* second derivatives of g_app enter P only through
(1/2) w^{ab} d_a d_b g_app; d_a d_b [lam g1] = lam^-1 d_a v d_b v [d_th^2 g1] + O(1); w^{ab} d_a v d_b v =
w(ell_app, ell_app) with ell_app := g_app^-1 dv = ell - lam <g1>(ell, .)^# + O(lam^2) by (E1) (the oscillating part
of g1 drops out of the O(lam) term); so w(ell_app, ell_app) = s(w) + O(lam)|w|, and that difference times lam^-1
goes into C. All other terms are linear in w or d w with coefficients built from g_app and d g_app, which are bounded.

For a profile Y, P([Y]) = [lam^-1 T Y + P_0 Y], with

    T Y = -(ell_app . d_X d_th Y) - (1/2)(g_app^{ab} d_a d_b v) d_th Y + B . (dv (x) d_th Y)
          + (1/2) Y(ell, ell) d_th^2 g1 - (1/2) n1 d_th^2 Y,

where lam n1 := g_app^-1(dv, dv) = -lam <g1>(ell, ell) + O(lam^2) by (E1): the principal term's lam^-2 part,
-(1/2) lam^-2 g_app^-1(dv, dv) d_th^2 Y, is of size lam^-1 and is kept in T.

**Lemma 3.1 (the phase-shift identity; deduced).** Under (E2), T(d_th g1) = lam T1 with T1 a profile.

*Proof.* Differentiate (3.1) for G = the profile of g_app at c = 0: the linearisation of R at G in the direction
d_th G equals d_th R[G]. d_th G = lam d_th g1 + lam^2 d_th g2 + ..., and P([Y]) = [D_G R[Y]], so the left side is
lam^-1 T(lam d_th g1 + lam^2 d_th g2 + ...) + P_0(lam d_th g1 + ...) = T(d_th g1) + O(lam). The right side is
d_th(lam^-1 R^(-1) + R^(0)) + O(lam) = O(lam) by section 3.1 and (E2). Both sides are expansions in powers of lam with
profile coefficients, the remainders lam times bounded profiles. []

This is the analytic content of Touati's transport and polarization at first order, in one line: a constant phase
shift of the wave is a symmetry of the leading equation, so its generator d_th g1 is annihilated by the 1/lam part of
the linearised operator.

### 3.3 The decomposition

Write G1 := [d_th g1], G2 := [d_th^2 g1]. By (E1), G1(ell, .) = G2(ell, .) = 0, and also
(d_X d_th g1)(ell, ell) = 0 and (d_X d_X d_th g1)(ell, ell) is bounded (differentiate g1(ell, .) = 0).

**Lemma 3.2 (deduced).** For phi(X) (no th) and the metric g = g_app + w,

    -(1/2) g^{ab} d_a d_b (phi G1) + B . d(phi G1) + C . (phi G1)
      = -lam^-1 (ell_app . d phi) G2 + lam^-1 phi [T(d_th g1)] - (1/2)(box~_app phi) G1
        + B1 . d phi + C1 phi + N_phi,                                                                          (3.3)

box~_app := g_app^{ab} d_a d_b, B1 . d phi and C1 phi with bounded profile coefficients, and N_phi collecting the
terms with a factor of w: |N_phi| <= C|w| (lam^-2 |phi| + lam^-1 |d phi| + |d^2 phi|) (and likewise for derivatives,
in scaled norms), with d^2 phi in N_phi multiplying G1 only. *Proof.* Expand d_a d_b(phi G1) by the chain rule (0.3):
the lam^-2 term carries g^-1(dv, dv) = g_app^-1(dv, dv) + O(|w|), whose first part is lam n1 and belongs to
phi T(d_th g1); the lam^-1 terms are the cross term -lam^-1 g^{ab} d_a phi d_b v G2, with g^{ab} d_b v = ell_app^a +
O(|w|), and phi times the lam^-1 part of P(G1), which is phi T(d_th g1) by the definition of T; the rest has bounded
coefficients. []

Let s := s(w) and define phi by the transport

    L0 phi = -(1/2) P s,     phi = 0 on Sigma_tau0,                                                         (3.4)

i.e. ell . d phi = (1/2) P s; it exists on Omega by Lemma 1.1(d). Put h := w - phi G1. Then s(h) = s(w) = s, and the
equation Ric^H(g_app + w) = 0, written as -(1/2) g^{ab} d_a d_b w + (1/2) lam^-1 s G2 + B.dw + C.w = F + N(w) with
F := -Ric^H(g_app) and N(w) the terms of second and higher order in (w, d w) other than the principal part, becomes,
by (3.3), (3.4) and Lemma 3.1,

    -(1/2) g^{ab} d_a d_b h + B.dh + C.h = F + N(w) - N_phi - (1/2) lam^-1 ((1 - P) s) G2
              + lam^-1 ((ell_app - ell) . d phi) G2 - phi [T1] + (1/2)(box~_app phi) G1 - B1.dphi - C1 phi.         (3.5)

Every coefficient on the right is a bounded profile; the one 1/lam coefficient left multiplies (1 - P)s, which is
O(lam d s) by (M3), and |ell_app - ell| <= C lam. Two things remain: box~_app phi has two derivatives of phi, and
phi is driven by s.

**Lemma 3.3 (the ell-ell component; deduced).** box~ s = c1 . d h + c0 . h + c2 . d phi + c3 phi - 2q F(ell, ell)
- 2q N(w)(ell, ell) + 2q N_phi(ell, ell) + sum_{a, i} c^{ai} d_a d_i h, where c0..c3 are bounded profiles, the sum runs
over pairs with i spatial, |c^{ai}| <= C(lam + |w|) and |d c^{ai}| <= C(1 + |d w|); N_phi(ell, ell) contains no
second derivative of phi. There is no 1/lam coefficient.

*Proof.* box~ s = (box~ h)(ell, ell) + 2 g0^{ab} d_a(ell ell) . d_b h + h . box~(ell ell). Write g0^{ab} d_a d_b =
q g^{ab} d_a d_b + sum c^{ai} d_a d_i with q := g0^{tautau}/g^{tautau} (g^{tautau} != 0 by Lemma 1.1(e)); then
c^{ai} = O(|g^-1 - g0^-1|) = O(lam + |w|). Contract (3.5) with ell ell: G2(ell, ell) = G1(ell, ell) = 0 removes the
1/lam terms and the box~_app phi term exactly; B1.dphi and C1 phi stay first order; the d^2 phi in N_phi multiplies
G1 and also drops. []

**Lemma 3.4 (the commutator transport; computed in `ks5.py` K3, deduced).** Psi := box~ phi satisfies

    L0 Psi - (2/r) Psi = -(1/2) box~ P s - (1/r)(d_tau + d_r) P s - (3/r^2) d_r phi,                             (3.6)

and box~_app phi = Psi + c^{ab} d_a d_b phi with |c| <= C lam. Every second derivative of phi is a combination,
with bounded coefficients, of L0 P s, d_x P s, d phi and the spatial Hessian d_x^2 phi, which satisfies the transport
L0(d_x^2 phi) = -(1/2) d_x^2 P s + (d_x xhat) * d_x^2 phi + (d_x^2 xhat) * d_x phi.

*Proof.* (0.1) applied to phi with L0 phi = -(1/2) P s. For the second claim, d_tau = L0 + xhat.d_x, L0 L0 phi =
-(1/2) L0 P s and L0 d_i phi = d_i L0 phi + (d_i xhat^m) d_m phi, and [L0, d_i] involves spatial derivatives only
since L0^tau = 1. []

## 4. Proof of Theorem E

Let k = 6. On [tau0, tau] (wherever the solution exists) put

    N(tau) := sum_{j<=k} lam^j ( ||d^j d h|| + ||d^j Psi|| + ||d^j d phi|| + lam ||d^j d_x^2 phi|| )
              + ||h|| + ||phi||.                                                                                (4.1)

**Step 1 (what N controls; deduced).** |w|_{k+1} <= C N: lam^j d^j(phi G1) is a sum of lam^i d^i phi times bounded
functions (0.3), and lam^i ||d^i phi|| <= lam N for 1 <= i <= k + 1. Hence, by Lemma 2.1, ||d^i w||_inf <=
C lam^(-3-i) N for i <= 4, and |d w|_k <= lam^-1 |w|_{k+1} <= C lam^-1 N.

**Step 2 (data; deduced).** phi = 0 on Sigma_tau0, so h = w there; the derivatives of h, phi, Psi on Sigma_tau0 of
order up to k + 1 in tau are fixed by (3.4), (3.5) and the equation for w, whose coefficients obey the scaled bounds
of (0.3); solving for d_tau^2 by induction gives N(tau0) <= C (Data(w) + lam^K) <= C (C_D + C_R) lam^K. (d_tau phi =
-(1/2) P s on Sigma_tau0, and d_x P s = P d_x s + O(lam) P d_x s by (M4): no 1/lam enters.)

**Step 3 (the bootstrap).** Suppose N <= 2 M lam^K on [tau0, tau*] with M to be fixed. Then (Step 1) |w| <=
C M lam^(K-3), |d w| <= C M lam^(K-4) <= C M lam^2, so for lam <= lam0(M) the metric g = g_app + w satisfies Lemma
1.1(e) and |d g| <= M1 with M1 independent of M.

**Step 4 (h; deduced).** Apply d^alpha, |alpha| = j <= k, to (3.5) and use Lemma 2.3 for each component, then multiply
by lam^j. The commutator [d^alpha, g^{ab}] d_a d_b h has terms d^i g . d^(j-i+1) d h, i >= 1; with
||d^i g_app||_inf <= C lam^(1-i), lam^j of each is at most C lam^(j-i+1) ||d^(j-i+1) d h|| <= C N; the w part is at
most C M lam^(K-4) N (i <= 4 in L^inf; for i >= 5, d^i w in L^2 and the other factor in L^inf by Lemma 2.1). The
right side of (3.5): lam^j ||d^alpha F|| <= C_R lam^K by (E3); B.dh and C.h give C N (profile coefficients cost lam^-1
per derivative, compensated by the weights); the term lam^-1 ((1 - P)s) G2 gives sum_i lam^(i-1) ||d^i (1 - P) s||
<= C sum_i lam^i ||d^i d s|| <= C N by (M3), (M4), (M6); lam^-1 (ell_app - ell).dphi G2 and phi[T1] give C N;
(1/2)(box~_app phi) G1 = (1/2) Psi G1 + (1/2)(c d^2 phi) G1 with |c| <= C lam, and by Lemma 3.4 lam d^2 phi is
controlled by lam L0 P s, lam d_x P s, lam d phi and lam d_x^2 phi, each at most C N at every level j <= k (no
Bernstein inequality is needed: lam^(j+1) ||d^j L0 P s|| <= C lam^(j+1) ||d^j d s|| by (M4), (M6)); B1.dphi, C1 phi
give C N. The nonlinear terms N(w) and N_phi are at most C lam^-5 N^2 + C lam^-3 N^2 by Lemmas 2.1 and Step 1 (worst:
quadratic in d w, |d w d w|_k <= C lam^-3 |d w|_k^2 <= C lam^-5 N^2), hence at most C M^2 lam^(2K-5) <= C M^2
lam^(K+1). So

    sum_{j<=k} lam^j ||d^j d h(tau)|| + ||h(tau)|| <= C ( N(tau0) + int_{tau0}^{tau} (N + C_R lam^K + C M^2 lam^(K+1)) ).

**Step 5 (phi; deduced).** Apply d^alpha to (3.4): L0 d^alpha phi = -(1/2) d^alpha P s + [L0, d^alpha] phi, where
[L0, d^alpha] has smooth lam-independent coefficients and involves d^(j) phi with lower or equal order; lam^j ||d^alpha
P s|| <= C sum_{i<=j} lam^i ||d^i s|| <= C N by (M1), (M4), (M6). The same for d phi (with d P s <= C P d s). For
lam d_x^2 phi use the transport of Lemma 3.4: lam^(j+1) ||d^alpha d_x^2 P s|| = lam^(j+1) ||d_x P(d^alpha d_x s)||
+ (commutators) <= C lam^j ||d^j d s|| by Bernstein (M2) in the one spatial derivative. Lemma 2.4 then gives the
phi-part of N(tau) at most C (N(tau0) + int_{tau0}^{tau} N) (d_tau phi does not vanish on Sigma_tau0).

**Step 6 (Psi; deduced).** Apply d^alpha to (3.6) and Lemma 2.4 (c = 2/r <= 2/a). The term box~ P s = P box~ s +
[box~, P] s. By Lemma 3.3, box~ s is first order in (h, phi) up to F, the nonlinear terms and sum c^{ai} d_a d_i h;
for the last, P(c d_a d_i h) = P d_i(c d_a h) - P((d_i c) d_a h) and ||P d_i f|| <= C lam^-1 ||f|| (M2, M4), with
|c| <= C(lam + |w|): at most C ||d h|| at level 0, and at level j, lam^j ||d^alpha P d_i (c d h)|| <= C lam^(j-1)
sum_i ||d^i c||_inf ||d^(j-i) d h|| <= C N since ||d^i c||_inf <= C lam^(1-i). For the commutator, [g0^{ab}, P]
d_a d_b s with at least one spatial index is bounded by C ||d s|| by (M5); the tau-tau term is rewritten with
d_tau^2 s = (box~ s - 2 g0^{tau i} d_tau d_i s - g0^{ij} d_i d_j s)/g0^{tautau} (g0^{tautau} = -1 - mu/r^2), after which
(M5) applies to the spatial terms; in box~ s (Lemma 3.3) the first-order terms gain the factor lam of (M5)'s
second form, and the terms c^{ai} d_a d_i h are written d_i(c d_a h) - (d_i c) d_a h, so that (M5)'s first form bounds
them by C ||c d h|| + C ||d c||_inf ||d h|| <= C N (at level j likewise; applying the second form to them would cost a
derivative at j = k). The terms of
g0^{ab}(d_a d_b P - P d_a d_b) s carry, by (M4) and (M6), a factor lam and a spatial derivative inside P, so they are
at most C ||d s|| by (M4); likewise at level j. The other terms of (3.6) are
first order in P s and phi. So the Psi-part of N(tau) is at most C (N(tau0) + int (N + C_R lam^K + C M^2 lam^(K+1))).

**Step 7 (closing).** Steps 4-6: N(tau) <= C2 (N(tau0) + int_{tau0}^{tau} N + (tau_end - tau0)(C_R lam^K + C M^2
lam^(K+1))), C2 independent of M and lam. Gronwall and Step 2: N(tau) <= C3 ((C_D + 1 + C_R) lam^K + C M^2
lam^(K+1)), C3 := C2 e^{C2 (tau_end - tau0)} (1 + tau_end - tau0) C. Take M := C3 (C_D + 1 + C_R) + 1 and lam0 so
small that C3 C M^2 lam0 <= 1 and Step 3 holds; then N <= M lam^K < 2 M lam^K on [tau0, tau*], improving the
bootstrap. N is continuous in tau for a smooth solution, so the bootstrap set is open and closed in the interval of
existence.

**Step 8 (existence and continuation; deduced from standard theorems not yet READ at source, section 7).** Local
existence, uniqueness and the continuation criterion for quasilinear wave systems -(1/2) g^{ab}(u) d_a d_b u = F(X, u,
du) with data in H^(k+1) x H^k, k + 1 > 4/2 + 1 (Ringstrom 2009; Sogge's version assumes coefficients near Minkowski's
and is not the one to use): the solution extends as long as its H^(k+1) x H^k norm and |du| stay bounded and the
metric stays uniformly Lorentzian with the slices spacelike. On Omega: extend the data from Sigma_tau0 to R^4 with a
bounded extension operator and Gamma[g0] smoothly, and re-extend at each restart time; by finite speed of propagation
and Lemma 1.1(e) the solution on Omega depends only on the data on Sigma_tau0 cap Omega. Step 7 bounds the criterion's
quantities (|w|_{k+1} <= C N, |d w| small) for each fixed lam, so the solution exists on all of Omega with (0.5). The
bounds after (0.5) are Step 1. []

## 5. Theorem A: the approximant

**Status.** The construction of the approximant from given stage data is proved here (deduced), with its stage 0
computed (`lead5.py`). Which stage data make the approximant's Cauchy data satisfy the constraints and the gauge
condition to order K belongs to the data problem, section 6, and is OPEN.

### 5.1 Stage 0 (computed: `lead5.py` L1-L5, `ansatz5.py` A2-A3)

Ric^H is a tensor (0.2), so the leading equation can be computed in the record's Eddington-Finkelstein coordinates,
where ell = d_r. Let W_TT be the record's first-order wave (ansatz5 A3: traceless, transverse, amplitude r^(-3/2)) and
W := W_TT + chi dv dv. Then (`lead5.py`): R^(-1) = 0 (L1); the th-mean of the lam^0 coefficient R^(0) of the two-scale
expansion of Ric^H(g0 + lam [W]) vanishes exactly when mu' = (2/9) A^2 env^2 H^2 (c^4 + s^4), which is mu' = (2/9)
A^2 env^2 for the record's H (L2, the energy condition of ansatz5 A4, now in this gauge); with chi = 0 the oscillating
part of R^(0) is a second harmonic in the vv component only (L3); chi enters R^(0) only as -(d_r + 3/(2r)) d_s chi in
vv (L4); W(ell, .) = 0 and tr W = 0 (L5). So with chi the solution, zero on Sigma_tau0, of the transport
(d_r + 3/(2r)) d_s chi = (the vv second harmonic of L3) along ell, the lam^0 equation holds identically in (X, th).
chi dv dv is the wave-map-gauge form of the record's second-order polarization term B (ansatz5 A4); the regularity of
chi at the axes is inherited from its source, a function of (v, r, x = cos 2th) (not yet checked by an instrument).

### 5.2 The ansatz

The unknowns are the means m_j (j >= 1), the phases phi_j (j >= 1) and the oscillating profiles gh_j (j >= 2, zero
th-mean). With the mean metric gbar := g0 + sum_{j=1}^{N} lam^j m_j, the phase u := v + sum_{j=1}^{N} lam^j phi_j, and

    G := gbar + lam W + sum_{j=2}^{N+1} lam^j gh_j(X, th),      g_app := G(X, u/lam),                          (5.1)

Ric^H(g_app) = [R_u[G]]_u, R_u the two-scale operator with d_a -> d_a + lam^-1 (d_a u) d_th, and
lam^-1 du = lam^-1 dv + sum_j lam^(j-1) dphi_j. Expand R_u[G] = sum_m lam^m Rm^(m). The phase is the eikonal of the
mean metric: in -(1/2) g^{ab} d_a d_b (lam W), the terms in which both derivatives fall on the phase sum to
-(1/2) lam^-1 gbar^-1(du, du) d_th^2 W plus terms with an oscillating factor of g^-1, and

    gbar^-1(du, du) = sum_{j>=1} lam^j e_j,    e_j = 2 ell.dphi_j - m_j(ell, ell) - q_j,                          (5.2)

q_j a polynomial in (m_i, dphi_i), i < j (q_1 = 0; q_2 = (m1 m1)(ell, ell) + |dphi1|^2 - 2 m1(ell, dphi1), with
indices moved by g0).

**Lemma 5.1 (where each unknown first enters; deduced).** Rm^(-1) = 0. Rm^(0) is the lam^0 coefficient of
R_v[g0 + lam W] at (X, th), minus (1/2) e_1 d_th^2 W. For m >= 1,

    Rm^(m) = Th gh_{m+1} - (1/2) e_{m+1} d_th^2 W + Wm(m_m, phi_m) + K_m,                                       (5.3)

where Th is the operator T of section 3.2 at lam = 0 built on (g0, W, m1, phi1); Wm is linear in m_m (to second order:
its th-mean part is -(1/2) box~ m_m + first order) and in phi_m (through dphi_m and box~ phi_m, the latter only as
-(1/2)(box~ phi_m) d_th W); and K_m depends only on m_i, phi_i (i < m) and gh_i (i <= m).

*Proof.* In (0.2) every monomial has at most two derivatives. A derivative is d_X (weight 0), lam^-1 dv d_th (weight
-1) or lam^(i-1) dphi_i d_th (weight i - 1), and d_th acts only on oscillating factors (W of weight 1, gh_i of weight
i); m_i has weight i. The order of a monomial is the sum of the weights. A factor of stage m + 1 can reach order m only
as gh_{m+1} hit by one lam^-1 dv d_th, or as m_{m+1} or dphi_{m+1} in the phase contraction (5.2): these are the
linearisation T (section 3.2) and e_{m+1}. Two factors of stage m (weights >= m - 1 each, and every d_th needing an
oscillating factor) reach order m only in the phase contraction (5.2) at m = 1 -- the q_2 terms -- which (5.2) places
in e_2. The second harmonic of W hit twice by lam^-1 dv d_th is contracted with gbar^-1(dv, dv), of weight >= 1, since
g0^-1(dv, dv) = 0. []

**Lemma 5.2 (Th; deduced).** With e_1 = 0, Th Y = -(ell . d_X) d_th Y + Mm Y on zero-mean profiles Y, Mm algebraic in
X (smooth bounded profile coefficients) and of first order in th. *Proof.* The lam^-1 part of the principal term on
lam Y(X, u/lam) is -(ell . d_X) d_th Y - (ell.dphi1) d_th^2 Y - (1/2) n1 d_th^2 Y with n1 = -m1(ell, ell) (section 3.2);
the d_th^2 Y terms are -(1/2) e_1 d_th^2 Y = 0. The rest of T is algebraic. []

**Lemma 5.3 (each stage is a linear hyperbolic system; deduced).** Let m >= 1 and let everything of earlier stages
be given and smooth. Impose e_m = 0, the th-mean of (5.3) and its oscillating part without the e_{m+1} term:

    (a) -(1/2) box~ m_m + Bbar . d m_m + Cbar m_m = Sm_m - <Wm_phi(dphi_m)> - <Th gh_{m+1}>,
    (b) L0 phi_m = -(1/2) m_m(ell, ell) - (1/2) q_m,
    (c) Pi_osc Th gh_{m+1} = -Pi_osc (Wm(m_m, phi_m) + K_m),

with data (m_m, d_tau m_m), phi_m and gh_{m+1} on Sigma_tau0. It has a unique smooth solution on Omega. *Proof.* <Th
gh> contains no X-derivative of gh (the d_X d_th term has mean zero), and Wm_phi's mean contains only dphi_m (box~ phi
multiplies d_th W, of mean zero). (c) is, for Z := d_th gh_{m+1}, the transport -(ell . d_X) Z + Mm' Z = F along ell
with Mm' a bounded operator on smooth zero-mean profiles (Lemma 5.2): an ODE along the integral curves of ell, which
reach Sigma_tau0 inside Omega (Lemma 1.1(d)). Its source contains box~ phi_m; put Psi_m := box~ phi_m, which by (0.1)
satisfies the transport L0 Psi_m - (2/r) Psi_m = -(1/2) box~(m_m(ell, ell) + q_m) - (1/r)(d_tau + d_r)(m_m(ell, ell) +
q_m) - (3/r^2) d_r phi_m, and box~(m_m(ell, ell)) = (box~ m_m)(ell, ell) + first order, with box~ m_m from (a): first
order in (m_m, phi_m) and algebraic in gh_{m+1}. The system for (m_m, phi_m, Psi_m, Z) is then linear with smooth
coefficients and closes without loss: m_m in H^(s+1), phi_m in H^(s+1), Psi_m and Z in H^s. Existence and uniqueness
on Omega follow from the energy and transport estimates of Lemmas 2.3 and 2.4 (lam plays no role) by Picard
iteration; Psi_m = box~ phi_m holds because their difference solves a homogeneous transport with zero data; smooth
data give smooth solutions. []

### 5.4 The approximant in Theorem E's form

Solve stage 0 (5.1) and the stages m = 1, ..., N (Lemma 5.3), with gh_{N+1} from stage N, and set e_{N+1} := 0 by
not including phi_{N+1}, m_{N+1}. Then Rm^(m) = 0 for m <= N - 1 by Lemma 5.1, and R_u[G] - sum_{m<N} lam^m Rm^(m) is
lam^N times a polynomial in lam with profile coefficients, so |Ric^H(g_app)|_k <= C lam^N. Rewrite with the fixed phase
v: G(X, v/lam + phi1 + lam Psi), Psi := sum_{j>=2} lam^(j-2) phi_j, expanded in lam Psi by Taylor's formula about
th + phi1 to order N, gives profiles g_j(X, th) independent of lam with g1 = m1 + W(X, th + phi1(X)) and a remainder
O(lam^(N+1)) in scaled norms. (E1) holds (W is transverse); (E2) holds, since the fixed-phase two-scale operator
satisfies R_v[G(., . + Phi)](X, th) = R_u[G](X, th + Phi), whose lam^0 coefficient is Rm^(0)(X, th + phi1) = 0
(Rm^(-1) = 0 and e_1 = 0); (E3) holds with K = N - 1. So **Theorem E applies to the approximant of any order, built
from any smooth stage data**; what remains for N1* is the choice of stage data and the data theorem.

## 6. The data: OPEN, and the route

**6.1 What is required.** Theorem E needs (E4): an exact vacuum datum on Sigma_tau0, with D = 0 imposed through
d_tau g, within O(lam^K) of the approximant's in scaled norms. Two steps: (D-a) choose the stage data so that the
approximant's Cauchy data satisfy the constraints and D = 0 to O(lam^K) (at each order a lam-independent problem:
for the means, the linearised constraints at the background's data on Sigma_tau0, elliptic; for the oscillating
profiles, algebraic conditions -- the polarization conditions and the symbols of the constraints at dr); (D-b)
correct the remaining O(lam^K) error exactly.

**6.2 Why Touati's data construction does not transfer as it stands (READ, arXiv:2206.13062v2, 2026-10-19).** His
Theorem 2.1 solves the constraints by the conformal method (conformal factor phi and vector field W, with the mean
curvature tau and a TT-tensor sigma as oscillating parameters), inverting the flat operators Delta_e and div_e L_e
and closing each fixed point by the smallness of the background: "taking eps small enough ensures that Psi is a
contraction" (section 5.4.2, p. 29), with the background eps-close to Euclidean, (2.1): "‖g0 - e‖_{H^{N+1}_delta} +
‖K0‖_{H^N_{delta+1}} <= eps". On Sigma_tau0 the background is the slice of five-dimensional Vaidya through the
hole: the trace-free part of K0 and d tau0 are of order one near r = a, so the coupling terms of the linearised
conformal system are not small there, and whether that system is invertible on the slice is not known. (The second
harmonic chi dv dv does not add to this: chi = 0 on Sigma_tau0 is a free choice (5.1), and then chi and d_th chi
vanish on the slice, tr K oscillates there only at O(lam), and d tau = d tau0 + O(1).)

**6.3 The route: the far slice (proposed; D1 is written below, D2-D5 are not yet done).** Take tau0 so negative
that on Sigma_tau0 the shell lies at r >= R0 with R0 large, and take Omega's outer boundary v + delta1 (tau - tau_end)
= V + 1 with delta1 := 1/|tau0| (any delta1 > 0 serves Lemma 1.1), so that the slice beyond R0 has width
W_f = O(1) independent of tau0. For r < R0 the approximant's data are exactly the seed's (no waves: v < v_start; chi
and the means vanish there by the choice of their data). In the far annulus A_f = {R_in <= r <= R_out}, R_in = R0 - 2,
the background is eps-close to flat, eps <= C(mu1/R0^2 + A/R0^(3/2)) -> 0 as tau0 -> -infinity, *with no smallness
of the data*.

*(D1) Uniform inversion in the far annulus (deduced).* For (gamma, K) the approximant's data restricted to A_f, with
|gamma - e| + |d gamma| + |K| + |d tau| <= C eps (d tau has no 1/lam part on Sigma_tau0, by 6.2) and the Hamiltonian
constraint holding to O(lam^K), the linearised conformal operator (four space dimensions: gamma' = psi^2 gamma,
K' = psi^-2 (sigma + L W) + (1/4) psi^2 tau gamma; Lichnerowicz -6 Delta psi + R psi - |sigma + L W|^2 psi^-5
+ (3/4) tau^2 psi^3 = 0, momentum div(sigma + L W) = (3/4) psi^4 d tau)

    (dpsi, dW) -> ( -6 Delta_gamma dpsi + V dpsi - 2 sigma . L dW ,  div_gamma L dW - 3 d tau dpsi ),
    V = R + 5 |sigma|^2 + (9/4) tau^2 = 6 |sigma|^2 + (3/2) tau^2 + O(lam^K),

is invertible H^1_0(A_f)^2 -> H^-1 with a bound independent of lam and tau0, for eps small. Its bilinear form B
satisfies B(u, u) >= 6 (1 - C eps) ||grad dpsi||^2 - C eps ||dpsi||^2 + (1/2)(1 - C eps)||L_e dW||^2 - C eps
(||dpsi||_{H^1}^2 + ||dW||_{H^1}^2), and int |L_e dW|^2 = 2 int |grad dW|^2 + int (div dW)^2 >= 2 ||grad dW||^2 for
dW in H^1_0 (integration by parts, n = 4), while Poincare's inequality on A_f has a constant C(W_f); so B is coercive
once eps is small, and Lax-Milgram applies. No compactness argument and no smallness of the waves is used, only that
the far region is weakly curved.

*(D2)-(D5), not yet done:* (D2) the formal constraint hierarchy (D-a) with the means' data supported in r >= R_in
(at each order the lam-independent version of the D1 problem with Dirichlet conditions, then the collar step below);
(D3) the exact correction: the D1 problem with the O(lam^K) error and quadratic terms, by contraction in scaled norms
(scaled elliptic regularity on balls of radius lam, polynomial losses absorbed by lam^K); (D4) the collar: the
corrected data meet the seed's at r = R_in only continuously; interpolate with a cut-off in the wave-free collar
R_in < r < R_in + 1 (where every correction is smooth with lam-independent bounds, the coefficients there being the
seed's) and remove the O(lam^K') constraint error there by a localized deformation of Tangherlini data
(Corvino-Schoen; in four space dimensions, Chrusciel-Delay), whose obstruction in the T^2 x Z2 x Z2-invariant class
is the static KID alone, absorbed by taking the interior Tangherlini mass mu0 + O(lam^K'): READ with hypotheses
checked, not yet done; (D5) the restatement of (i) on D_T cap {tau >= tau0} for each tau0 below a threshold, with
the seed mass mu0 + O(lam^K') (equivalent to the record's data to that order).

## 7. What is left

- **The data (section 6): OPEN.** The one remaining part of N1*: D2-D5 of section 6.3.
- **Verification.** Sections 0-4 were checked by one independent verifier (N1STAR-LOG.md D12): no major gap, one
  minor gap (Step 6 at the top level, repaired) and seven notes (repaired). Sections 5-6 are not yet verified.
- **READ at source** of the standard theorems the proof invokes: the decomposition of Ricci in wave coordinates
  (0.2); local existence, uniqueness, continuation and finite speed of propagation for quasilinear wave systems
  (Step 8); the propagation of the gauge (0.7); Sobolev embedding and extension on the annuli (Lemma 2.1).
- Regularity of chi at the axes (section 5.1), by an instrument.
