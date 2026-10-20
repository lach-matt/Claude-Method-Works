# N1*: the proof

Commissioned at item 522 (N1STAR-LOG.md D7). Labels: **computed** (an instrument here, with a selftest whose mutants
it catches), **deduced** (an argument written out here, or a standard theorem invoked **READ** with its hypotheses
checked), **READ** (verbatim at source), **OPEN**.

**Status (2026-10-20). N1* is PROVED** (N1STAR-LOG.md D21). It reduces to three theorems, all written out. **Theorem E**
(evolution: existence on the domain and lam-uniform estimates for the remainder, given an approximant and data) is
proved in sections 1-4 (deduced; its exact inputs computed in `ks5.py`, `foliation5.py`, `ansatz5.py`). **Theorem A**
(the approximant to any order in the gauge used here) is proved in section 5 (deduced; its leading order computed in
`lead5.py`). **Theorem D** (the data: an exact vacuum datum on the slice before the shell reaches the hole, within
O(lam^K) of the approximant's) is proved in section 6 (deduced; the facts about the approximant's slice data computed in
`data5.py`), by solving the constraints outward in r as a parabolic-hyperbolic system [Rac16] from a sphere inside the
shell, where the approximant's data are the seed's exactly. Every standard theorem the proof invokes is READ at source
by the site's retrieval protocol, most on two independent routes, its hypotheses checked against the statement READ
(section 7, D17-D18); that check found one gap the verifiers had not (Step 8: the time lines of the coordinates of 0.1
are spacelike inside the horizon), repaired. Seven independent verifiers, one at a time, checked the proof and each
round of repairs: sections 0-4 (D12), sections 5-6 (D15), and the repairs (D16, D18, D19, D20, D21). None found a major
gap; every minor gap and note was repaired, most as the verifier proposed. The last round read Proposition 6.5 whole and
found it to hold, with one clause of Lemma 6.4 stated more weakly than its proof gives; that clause is restated (D21) in
the form the verifier specified, and it and the three notes applied with it are the only text no verifier has read after
the edit. The instruments' selftests and mutant runs pass (README.md).

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
(READ: [CBCM10] (2.7)-(2.9), in n + 1 dimensions, with H = D and D^ = Dh: Ric = Ric^H + (1/2)(g Dh D + g Dh D) and Ric^H
= -(1/2) g^{ab} Dh_a Dh_b g + f^[g, Dh g], f^ free of second derivatives of g; in the coordinates of 0.1, Dh_a Dh_b g -
d_a d_b g is Gamma[g0] and its first derivatives times (g, dg), which gives (0.2). Section 7.) Second derivatives of g
enter (0.2) only through -(1/2) g^{ab} d_a d_b g. D(g0) = 0, so Ric^H(g0) = Ric(g0). Ric^H(g) = 0 is a quasilinear wave
system; a solution with D = 0 is vacuum.

### 0.3 Profiles and scaled norms

A *profile* is a smooth f(X, th) on Omega x S^1, S^1 = R/2piZ; [f](X) := f(X, v(X)/lam); <f> is its th-mean. For a
function or tensor f on Sigma_tau := Omega cap {tau} (Omega in section 1), with d^j all spacetime coordinate
derivatives of order j and ||.|| the flat L^2(Sigma_tau),

    |f|_j := sum_{i<=j} lam^i ||d^i f||.                                                                  (0.3)

Chain rule: d_a [f] = lam^-1 (d_a v)[d_th f] + [d_a f], so |[f]|_j <= C_j sup_{i<=j} |d^i_{(X,th)} f|_{L^inf}
(the oscillation costs nothing in scaled norms), and ||d^i [f]||_{L^inf} <= C lam^-i.

### 0.4 Theorem E (evolution) -- proved in sections 1-4 (deduced), verified (D12; Step 8, D18-D20)

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

### 0.5 Theorem A (the approximant) -- proved in section 5 (deduced), verified (D15, D16)

For every N and every smooth choice of stage data there are profiles g1, ..., g_N with (E1)-(E3), K = N - 1, whose
oscillating part of g1 is the record's waves (F, G of the instructions, section 2) with a second harmonic chi dv dv
and a phase shift, on the background g0 with mu' = (2/9) A^2 env^2. Stage data making the approximant's Cauchy data
satisfy the constraints and D = 0 to order N - 2 exist (Lemma 6.2).

### 0.6 Theorem D (the data) -- proved in section 6 (deduced), verified (D15, D16, D18-D21)

For lam small there is a vacuum Cauchy datum (gamma, kappa) on Sigma_tau0 (the constraints hold exactly), with the
gauge condition D = 0 imposed through d_tau g, whose w satisfies (E4); it equals the seed's datum on Sigma_tau0 cap
{r < v_start - tau0}.

### 0.7 How N1* follows

Given A and D, Theorem E gives g_lam on Omega. D(g_lam) solves a homogeneous linear wave system (contracted Bianchi
identity) with D = d_tau D = 0 on Sigma_tau0 (the gauge condition and the constraints), so D = 0 on Omega and g_lam is
vacuum (deduced: by the contracted Bianchi identity D solves -(1/2) g^{ab} d_a d_b D = f with f linear in (D, d D) with
bounded coefficients, so Lemma 2.3 and Gronwall's lemma give D = 0 on Omega; the identity is READ in [LR05] and, in n +
1 dimensions, [CBCL06] section 3). Its T^2 x Z2 x Z2 invariance follows from uniqueness on Omega (Step 8), since Ric^H
and D are built from g and the O(4)-invariant g0 alone (0.2) and the data are invariant. D_T cap {tau >= tau0} lies in
Omega (Lemma 1.1). Hence (i) on D_T cap {tau >= tau0} with the data on Sigma_tau0 (the instructions' route W item 4:
"construct Cauchy data on a slice before the shell reaches the hole ... restate (i) on it"); the remainder estimate is
(0.5); no derivative is lost (the bootstrap of section 4 closes at the fixed order k); the formulation is regular across
the axes (Cartesian arrays on R^4); the background is the large g0. (ii): |g_lam - g0| <= C lam; d g_lam bounded; d
g_lam - d g0 = dv [d_th g1] + O(lam) tends to zero weakly since <d_th g1> = 0. The rates of (ii)-(iii) beyond these rest
on Theorem A's profiles.

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

**Lemma 2.1 (Sobolev, products; deduced).** On A(tau), ||f||_{L^inf} <= C sum_{i<=3} ||d_x^i f||, hence ||d^i
f||_{L^inf} <= C lam^(-3-i) |f|_{i+3}. For k = 6, |f g|_k <= C lam^-3 |f|_k |g|_k, and if a is a profile, |[a] f|_k <= C
|f|_k. *Proof.* The annuli A(tau) are images of the fixed annulus {a <= |x| <= a + 1 + delta0} under radial maps with
uniformly bounded derivatives of all orders (b - a in [1 + delta0, b(tau0) - a]), so Sobolev's embedding H^3 into L^inf
in four dimensions ([BH17] Theorem 7.26, READ) holds with a uniform constant; scaling each derivative by lam gives the
second form. For products, distribute lam^k d^k and put the factor with at most three derivatives in L^inf. The last
claim is (0.3)'s chain-rule remark. []

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

**Step 8 (existence and continuation; deduced, the local theory READ, section 7).** The local theory READ, [DS23]
Theorems 2.4 and 2.6 and [AO14] Theorem 1.1 with its Remark 1.2, needs the time lines timelike as well as the slices
spacelike: [AO14] (1.3) asks A^{ij} xi_i xi_j >= |xi|^2 / gamma and A^{00} <= -kappa, and in the first-order form the
eigenvalue 0 meets a characteristic speed wherever g^{ij} xi_i xi_j = 0, against [DS23] (A4) ("the lambda_i's do not
meet each other"). In the coordinates of 0.1 this fails on part of Omega: g0^{ij} xi_i xi_j = |xi|^2 - (mu/r^2)
(xhat.xi)^2 < 0 for radial xi where r^2 < mu, and Omega reaches r = a < sqrt(mu0). So the theorems are applied in other
coordinates, in four steps. (i) The coefficients. On Omega the system for w is Ric^H(g_app + w) = 0 relative to g0, and
the profiles of g_app are defined on Omega x S^1 (Lemma 5.3). Extend them to R^5 x S^1 by one universal extension
operator acting in X, the same for every order (Stein's or Rychkov's, for the bounded Lipschitz domain Omega, a convex
polygon in (tau, r) times S^3; [SY21], section 7): g_app extends smoothly with bounded derivatives of every order, for
all tau, and is unchanged on Omega. Outside a neighbourhood U of Omega, replace g_app and g0 by g_ext and g0_ext,
obtained by interpolating lapse, shift and spatial metric (relative to tau) convexly to (1, 0, delta) on {r <= a/4} and
on {r >= R2 + 1}, R2 := b(tau0) + 1. Every such combination is a Lorentzian metric with each Sigma_tau spacelike, so the
system keeps its form, with coefficients smooth in X and equal to Minkowski's outside a compact set in x; on U nothing
changes. (ii) The coordinates. Z := d_tau - beta_ext (beta_ext the shift of g_ext) has Z(tau) = 1, g_ext(Z, Z) =
-N_ext^2 <= -N_min^2 < 0, and Z = d_tau outside a compact set. Put X = (tau, Phi(tau, y)), Phi the flow of Z from tau0:
the slices are unchanged and d_tau at fixed y is Z, so in (tau, y) the matrix g_ext^{ij} is the inverse spatial metric,
uniformly positive definite, and g_ext^{00} = -N_ext^-2. Only the independent variables change: the unknowns stay the
Cartesian arrays of 0.1, the principal part stays -(1/2) g^{ab} d_a d_b with g^{ab} transformed as a tensor, and the
system stays quasilinear with coefficients smooth in (tau, y). (iii) The cut-off. Let chi be a smooth map of the
components, the identity on |w| <= eps2/2 and into |w| <= eps2, with eps2 so small that every metric within eps2 of
g_ext keeps (1.3) with fixed constants in (tau, y); put chi(w) for w in the coefficients and lower-order terms. The
modified system agrees with the original where |w| <= eps2/2, which holds on Omega (|w| <= C M lam^(K-3), Step 3). The
coefficients and the source are taken at time theta(tau), theta smooth, equal to tau on [tau0 - 1, tau_end + 1] and
constant outside [tau0 - 2, tau_end + 2]: the coordinates of (ii) degenerate as |tau| grows (the flow lines of Z pile up
where beta_ext vanishes), and [DS23] (A1) asks for bounds uniform in t; on [tau0, tau_end] nothing changes. Its
coefficients and source equal Minkowski's outside a compact set in y, so it is posed on a torus T^4_L of large period.
In V := (w, d_tau w, d_y w) it is symmetric hyperbolic, A^0 = diag(1, -g^{00}, g^{ij}) > 0, and satisfies (A1)-(A4) of
[DS23] on all of R^m: the distinct eigenvalues are lambda_- < 0 < lambda_+, the characteristic roots having product
g^{ij} xi_i xi_j / g^{00} < 0, so they never meet; u_i = d_i w propagates, since d_tau (u_i - d_i w) = d_i (u_0 - d_tau
w) = 0. (iv) The restarts. At tau_i extend the data from Sigma_tau_i cap Omega = A(tau_i), in x, by the universal
Seeley-type operator of [LY22] Theorem 26 for the smooth annulus (one operator bounded on every H^m, so smooth data
extend to smooth data), cut off, and compose with Phi(tau_i, .) to pass to y. The constants are uniform in tau, the
annuli being images of a fixed one under radial diffeomorphisms with bounded derivatives (deduced: [LY22] Lemma 27
states the composition bounded, and its proof, by chain and product rules and a change of variables, gives a bound
through finitely many derivatives of the diffeomorphism and its inverse). [DS23] Theorem 2.4 with r = k > 4/2 + 1 (k =
6) gives a solution on [tau_i, tau_i + delta], delta depending only on the norm of the data, which Steps 1 and 7 bound
for each fixed lam (|w|_{k+1} <= C N <= C M lam^K); the data are smooth, and by [DS23] Theorem 2.6 the solution lies in
every H^r on the same interval, so it is smooth. On Omega cap {tau_i <= tau <= tau_i + delta} it solves the original
system while |w| <= eps2/2, and it is the only solution there with the data on Sigma_tau_i cap Omega: for two such,
-(1/2) g1^{ab} d_a d_b (w1 - w2) = (1/2) (g1^{ab} - g2^{ab}) d_a d_b w2 + F(X, w1, d w1) - F(X, w2, d w2) =: f, ||f|| <=
C (||w1 - w2|| + ||d (w1 - w2)||) since d^2 w2 is bounded, and Lemma 2.3 from tau_i with Gronwall's lemma gives w1 = w2.
This is the finite speed of propagation the proof uses, deduced from Lemma 2.3 with no citation, and the uniqueness 0.7
uses for the symmetry. With Step 7 the bootstrap continues, so the solution exists on all of Omega with (0.5). The
bounds after (0.5) are Step 1. []

## 5. Theorem A: the approximant

**Status.** The construction of the approximant from given stage data is proved here (deduced), with its stage 0
computed (`lead5.py`). The stage data that make the approximant's Cauchy data satisfy the constraints and the gauge
condition to high order are chosen in section 6 (Lemma 6.2). Verified by two independent verifiers (N1STAR-LOG.md D15,
D16).

### 5.1 Stage 0 (computed: `lead5.py` L1-L5, `ansatz5.py` A2-A3)

Ric^H is a tensor (0.2), so the leading equation can be computed in the record's Eddington-Finkelstein coordinates,
where ell = d_r. Let W_TT be the record's first-order wave (ansatz5 A3: traceless, transverse, amplitude r^(-3/2)) and
W := W_TT + chi dv dv. Then (`lead5.py`): R^(-1) = 0 (L1); the th-mean of the lam^0 coefficient R^(0) of the two-scale
expansion of Ric^H(g0 + lam [W]) vanishes exactly when mu' = (2/9) A^2 env^2 H^2 (c^4 + s^4), which is mu' = (2/9) A^2
env^2 for the record's H (L2, the energy condition of ansatz5 A4, now in this gauge); with chi = 0 the oscillating part
of R^(0) is a second harmonic in the vv component only (L3); chi enters R^(0) only as -(d_r + 3/(2r)) d_s chi in vv
(L4); W(ell, .) = 0 and tr W = 0 (L5). So with chi the solution, zero on Sigma_tau0, of the transport (d_r + 3/(2r))
d_s chi = (the vv second harmonic of L3) along ell, the lam^0 equation holds identically in (X, th). chi dv dv is the
wave-map-gauge form of the record's second-order polarization term B (ansatz5 A4). chi is smooth at the axes (deduced):
ell has no angular component, so the transport preserves smoothness on S^3, and its source, the second harmonic of
R^(0)(d_tau, d_tau) (the Eddington-Finkelstein d_v is the Kerr-Schild d_tau), is built from g0 and W_TT, which is
smooth at both axes (`ansatz5.py` A3).

### 5.2 The ansatz

The unknowns are the means m_j (j >= 1), the phases phi_j (j >= 1) and the oscillating profiles gh_j (j >= 2, zero
th-mean). With the mean metric gbar := g0 + sum_{j=1}^{N} lam^j m_j, the phase u := v + sum_{j=1}^{N} lam^j phi_j, and

    G := gbar + lam W + sum_{j=2}^{N+1} lam^j gh_j(X, th),      g_app := G(X, u/lam),                          (5.1)

Ric^H(g_app) = [R_u[G]]_u, R_u the two-scale operator with d_a -> d_a + lam^-1 (d_a u) d_th, and
lam^-1 du = lam^-1 dv + sum_j lam^(j-1) dphi_j. Expand R_u[G] = sum_m lam^m Rm^(m). The phase is the eikonal of the
mean metric: in -(1/2) g^{ab} d_a d_b (lam W), the terms in which both derivatives fall on the phase sum to
-(1/2) lam^-1 gbar^-1(du, du) d_th^2 W plus terms with an oscillating factor of g^-1, and

    gbar^-1(du, du) = sum_{j>=1} lam^j e_j,    e_j = 2 ell.dphi_j - m_j(ell, ell) - q_j,                          (5.2)

q_j a polynomial in (m_i, dphi_i), i < j (q_1 = 0; q_2 = -(m1 m1)(ell, ell) - |dphi1|^2 + 2 m1(ell, dphi1), with
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
linearisation T (section 3.2; it contains the term (1/2) gh_{m+1}(ell, ell) d_th^2 W, gh_{m+1} undifferentiated in g^-1
against W hit twice by the phase) and e_{m+1}. Two factors of stage m (weights >= m - 1 each, and every d_th needing an
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

Solve stage 0 (5.1) and the stages m = 1, ..., N (Lemma 5.3), with gh_{N+1} from stage N; phi_{N+1} and m_{N+1} are not
included, so e_{N+1} = -q_{N+1} need not vanish, which is harmless since only Rm^(m), m <= N - 1, is used. Then Rm^(m)
= 0 for m <= N - 1 by Lemma 5.1, and R_u[G] - sum_{m<N} lam^m Rm^(m) is lam^N times a profile bounded uniformly in lam
(rational in lam through g^-1), so |Ric^H(g_app)|_k <= C lam^N. Rewrite with the fixed phase v: G(X, v/lam + phi1 + lam
Psi), Psi := sum_{j>=2} lam^(j-2) phi_j, expanded in lam Psi by Taylor's formula about th + phi1 to order N, gives
profiles g_j(X, th) independent of lam with g1 = m1 + W(X, th + phi1(X)) and a remainder O(lam^(N+1)) in scaled norms.
(E1) holds (W is transverse); (E2) holds, since the fixed-phase two-scale operator satisfies R_v[G(., . + Phi)](X, th)
= R_u[G](X, th + Phi), whose lam^0 coefficient is Rm^(0)(X, th + phi1) = 0 (Rm^(-1) = 0 and e_1 = 0); (E3) holds with K
= N - 1. So **Theorem E applies to the approximant of any order, built from any smooth stage data**; the stage data for
N1* are chosen in Lemma 6.2.

## 6. Theorem D: the data

**Status.** Proved here (deduced), with the facts it uses about the approximant's slice data computed in `data5.py`
(S0-S6) and the form of the constraints READ in [Rac16] (I. Racz, *Constraints as evolutionary systems*, Class. Quantum
Grav. 33 (2016) 015014, arXiv:1508.01810v3, READ 2026-10-19); verified by two independent verifiers (D15, D16). No
smallness of the background is used, so the data are posed on the slice Sigma := Sigma_tau0 of section 1, before the
shell reaches the hole (route W item 4), and they coincide with the seed's data on Sigma cap {r < v_start - tau0}.

### 6.1 Two identities (deduced; standard)

For a Lorentzian g put E := Ric^H(g) and S(D)_mn := (1/2)(g_{m rho} Dh_n D^rho + g_{n rho} Dh_m D^rho), so that Ric(g)
= E + S(D) by (0.2), and Gt(T) := T - (1/2)(tr_g T) g.

(I1) The contracted Bianchi identity div_g Gt(Ric) = 0 reads

    B_g[D] := div_g Gt(S(D)) = -div_g Gt(E),                                                             (6.1)

B_g linear in D, of second order with principal part (1/2) g^{ab} d_a d_b; its other coefficients involve g, dg, g0 and
the derivatives of g0, and no second derivative of g (div_g S(D) = g grad (Dh D) and grad = d + Gamma[g]).

(I2) On a slice {tau = const} with future unit normal n, the induced data (gamma, K) have constraint map (J, rho) =
(2(-div K + d tr K), R - |K|^2 + (tr K)^2) [CD03] (2.1) equal to 2 G(n, .) (rho the n-component, J the tangential
components, up to the sign convention of K), G = Gt(Ric), by the Gauss and Codazzi equations. If D = 0 on the slice
then dD = -n (x) Z there with Z := d_n D, so S(D) = -(1/2)(n (x) Z + Z (x) n), tr S = -n.Z and Gt(S(D))(n, .) = (1/2)
Z. Hence on a slice where D = 0,

    2 G(n, .) = 2 Gt(E)(n, .) + Z,                                                                        (6.2)

and for a solution of Ric^H(g) = 0 with D = 0 on the slice the constraints hold there exactly when d_n D = 0 there.

**What Theorem D asks.** Let (gamma, K) on Sigma satisfy the constraints, and give g on Sigma the lapse and shift of
g_app, the spatial part gamma, d_tau of the spatial part fixed by K, and d_tau of the lapse and shift fixed by D(g) = 0
on Sigma (D is linear in d_tau g_{tau .} with invertible coefficient on a spacelike slice: the standard choice of the
gauge's data). Then (g, d_tau g) is a Cauchy datum for Ric^H = 0 with D = 0 and, by (6.2), d_tau D = 0 on Sigma, which
is what 0.7 uses. (E4) asks that w := g - g_app be O(lam^K) in the scaled norm Data. So two steps: the approximant's
data must satisfy the constraints and D = 0 to high order (section 6.2), and the error must be removed exactly with
lam-uniform bounds (section 6.3).

**Why Touati's construction does not transfer as it stands (READ, arXiv:2206.13062v2, 2026-10-19).** His Theorem 2.1
solves the constraints by the conformal method, inverting the flat operators Delta_e and div_e L_e and closing each
fixed point by the smallness of the background: "taking eps small enough ensures that Psi is a contraction" (section
5.4.2, p. 29), with (2.1): "‖g0 - e‖_{H^{N+1}_delta} + ‖K0‖_{H^N_{delta+1}} <= eps". Here the slice passes through the
hole, the background data are not close to Euclidean, and an elliptic method needs boundary data at r = a as well as
far out. The evolution in r below needs neither: it is solved outward from a sphere inside the shell, where the
approximant's data are the seed's exactly, and nothing is imposed further out.

### 6.2 The approximant's data (Lemmas 6.1, 6.2)

D(g_app) has the two-scale form [D_u[G]]_u, D_u[G] = sum_{m>=0} lam^m D^(m)(X, th), as Ric^H in 5.2. (6.1) is an
identity of differential polynomials in g, and d_a -> d_a + lam^-1 (d_a u) d_th are commuting derivations, so (6.1)
holds order by order for the profiles, its right side at order j involving R^(i), i <= j + 1, only (the profiles of
Ric^H(g_app), which vanish for i <= N - 1, 5.4). D^(0) = g0^-1 (d_th W(ell, .) - (1/2) dv tr d_th W) = 0 by (E1) and tr
W = 0 (`lead5.py` L5).

**Lemma 6.1 (the gauge hierarchy; deduced).** Let N >= 3 and suppose that on Sigma

- (F1) D^(m)(X, th) = 0 for all th, m = 1, ..., N - 1;
- (F2) d_tau <D^(m)> = 0, m = 1, ..., N - 2.

Then D^(m) = 0 on Omega x S^1 for m <= N - 2, and d_th D^(N-1) = 0. Hence |D(g_app)|_k <= C lam^(N-1) on every
Sigma_tau, and the constraint map of g_app's data on Sigma has scaled norm |.|_(k-1) <= C lam^(N-2).

*Proof.* In two-scale form the principal part of B_g on lam^m [Y]_u is lam^(m-2) (1/2) g^-1(du, du) d_th^2 Y +
lam^(m-1) (g^-1(du, d_X) + (1/2) box_g u + M) d_th Y + lam^m (1/2) g^{ab} d_a d_b Y, where g^-1(du, du) = O(lam^2)
(gbar^-1(du, du) = O(lam^(N+1)) by (5.2) and W(ell, .) = 0; the leading part, -lam^2 gh_2(ell, ell), multiplies d_th^2
Y, which vanishes for the Y = D^(m) of the induction), g^-1(du, d_X) = ell . d_X + O(lam), box_g u = box_g0 v + O(lam),
and M(X, th), from the coefficient Gamma[g] of dD (of size dg = O(1)), is a bounded multiplication operator on
profiles. Induction on m = 0, ..., N - 2 with the hypothesis: D^(j) = 0 for j < m and d_th D^(m) = 0 (true at m = 0).
At order m the oscillating part of (6.1) is the transport (ell . d_X + (1/2) box_g0 v + M) Z = (first order in <D^(m)>)
for Z := d_th D^(m+1), and its mean is the linear wave equation (1/2) box_gbar <D^(m)> + (first order) <D^(m)> + <M Z>
= 0; every other term vanishes by the hypothesis or because it contains R^(i), i <= m + 1 <= N - 1. The data are zero:
<D^(m)> by (F1), d_tau <D^(m)> by (F2), Z by (F1) at order m + 1. This linear system for (<D^(m)>, Z) closes without
loss exactly as in Lemma 5.3 (the mean in H^(s+1), Z in H^s; Lemmas 2.3, 2.4; the transport curves reach Sigma inside
Omega by Lemma 1.1(d)), so <D^(m)> = 0 and Z = 0: the hypothesis at m + 1. Then D(g_app) = lam^(N-1) [D^(N-1)] +
O(lam^N) with bounded profiles, and 2 G(g_app)(n, .) = 2 Gt(E)(n, .) + 2 Gt(S(D))(n, .) with S(D) first order in D: the
scaled norm of the second term is <= C lam^-1 lam^(N-1), of the first <= C lam^(N-1) (E3). []

**Lemma 6.2 (the stage data; deduced, with Lemma 6.4).** For every N there are stage data for Theorem A satisfying (F1)
and (F2), all vanishing on Sigma cap {r < v_start - tau0}.

*Proof.* Stage 0: chi = 0 on Sigma, as chosen in 5.1. Stage m = 1, ..., N - 1, everything of the earlier stages given:
put phi_m = 0 and (m_m)_{tau .} = 0 on Sigma. The unknowns left on Sigma are h_m and Q_m, the order-m means of the
induced metric and second fundamental form (h_m is the spatial part of m_m, and given h_m, Q_m fixes d_tau of that
spatial part), d_tau (m_m)_{tau .}, and gh_(m+1).

(i) On Sigma the oscillating part of D^(m) is Pol(d_th gh_(m+1)) + Lambda_m(h_m) + (known), Pol(Y) := Y(ell, .) - (1/2)
dv tr_g0 Y, and Lambda_m algebraic: the terms of the order-m oscillating part of D linear in m_m or in d phi_m
(bilinear with d_th W, such as m_m(ell, .) contracted with d_th W, <m_m, d_th W> ell and d_th W(grad phi_m, .)), in
which d_tau phi_m = -(1/2)(m_m(ell, ell) + q_m) by Lemma 5.3(b) and the tangential derivatives of phi_m vanish. Pol is
onto at every point: `data5.py` S1 finds rank 5 at one point, and Pol depends only on (g0, dv) at the point, every pair
of a Lorentzian metric and a nonzero null covector being equivalent under GL(5) to every other. So d_th gh_(m+1) :=
-Pol^+(Lambda_m(h_m) + known) on Sigma (the right side has zero th-mean, and gh_(m+1) is its zero-mean antiderivative
in th), with Pol^+ := Pol^T (Pol Pol^T)^-1 and the transposes taken in the Euclidean structure of the Cartesian
coordinates (tau, x), which is O(4)-invariant (so Pol^+ commutes with the symmetries), solves it, smoothly, pointwise
and linearly in h_m.

(ii) The mean of D^(m) on Sigma is linear in d_tau (m_m)_{tau .} with the invertible coefficient of the gauge's data
(above), plus terms in h_m, Q_m and known quantities: it fixes d_tau (m_m)_{tau .}.

(iii) First, every first derivative of D^(j), j < m, vanishes on Sigma. Solve stage m with any data: D^(j), j <= m - 1,
does not depend on the data of stage m, and R^(i) = 0 for i <= m - 1 once stage m is solved (Lemmas 5.1 and 5.3: before
it, R^(m-1) = -(1/2) e_m d_th^2 W, and stage m imposes e_m = 0). For m >= 3, Lemma 6.1 with N := m applies (its
hypotheses, (F1) at orders 1, ..., m - 1 and (F2) at orders 1, ..., m - 2, were arranged at the earlier stages) and
gives D^(j) = 0 on Omega for j <= m - 2 and d_th D^(m-1) = 0; then the first derivatives of D^(m-1) on Sigma vanish
too: the tangential ones by (F1), the normal one of the mean by (F2) at order m - 1, and the oscillating part is zero.
For m = 1, 2 the same holds directly: D^(0) = 0, and for m = 2 the order-0 transport, with d_th D^(1) = 0 on Sigma by
(F1), gives d_th D^(1) = 0 on Omega, and the normal derivative of <D^(1)> vanishes on Sigma by (F2) at order 1. The
tangential derivatives of D^(m) vanish by (F1), and the phase part lam^-1 (d u) d_th D^(m+1) of the derivatives has
mean zero. So the order-m mean of 2 G(g_app)(n, .) on Sigma is d_n <D^(m)> (the order-m mean of (6.2)), the E-part
having mean zero (after stage m, R^(i) = 0 for i < m and R^(m) = -(1/2) e_(m+1) d_th^2 W, of mean zero): (F2) at order
m is the order-m mean of the constraint equations. That is P(h_m, Q_m) + B_m(h_m) = S_m, with P the linearisation of
the constraint map at the data of g0 on Sigma ([CD03] (2.2)), B_m algebraic in h_m (the means of the products of h_m
and of gh_(m+1) of (i) with the oscillating data), and S_m known. Solve it with h_m = a_m dr dr, Q_m = w_m Pi + q_m dr
+ dr q_m by Lemma 6.4 (B_m is a zeroth-order term of the kind allowed there), from zero data at r = a. Its sources
vanish where the earlier stages' data and the waves do, so (a_m, w_m, q_m) vanish on r < v_start - tau0, and are
smooth. []

### 6.3 The exact correction (Lemmas 6.3, 6.4, Proposition 6.5)

On Sigma use (r, omega), omega in S^3, a <= r <= b(tau0). For data (gamma, K) on Sigma and U := (a, w, q) (a and w
functions, q a covector tangent to the spheres) put, as in [Rac16] (the lapse of the foliation by the spheres, and the
mixed and trace parts of K),

    Psi(U) := (gamma + a dr dr,  K + w Pi + q dr + dr q),     Pi the metric induced on the spheres.          (6.3)

**Lemma 6.3 (the constraints as an evolution in r; computed `data5.py` S2-S4, S6; READ [Rac16]).** (a) The constraint
map of Psi(U) is quasilinear in U: second order in a with no d_r^2 a and no d_r of a tangential derivative, first order
in (w, q), and a enters J to first order only. Its rho-component is parabolic in r where the spheres have positive mean
curvature H: at the data of g0 on Sigma (computed, S3, in the symmetric class), (3 r^3/(r^2 + mu)^2) d_r a - (r^2 +
mu)^-1 d_th^2 a + (lower order) = theta^3 H d_r a - theta^2 Delta_S a + ..., theta^2 = gamma^{rr} = r^2/(r^2 + mu), H =
3/(r^2 + mu)^(1/2) > 0 for all r. Its J-component is symmetric hyperbolic in (w, q) with r as time: [Rac16] (3.3),
READ: "the coefficients of d_rho and d_K are symmetric, and that the coefficient of d_rho is also positive definite";
at g0's data (S3, `--show`): J_r = 6 d_r w - (2/r^2) d_th q + ..., J_th = -(2 r^2/(r^2 + mu)) d_r q + 4 d_th w + ...,
real speeds c^2 = 2 (r^2 + mu)/(3 r^4) > 0. The raw coefficient of d_r (w, q), diag(6, -2 r^2/(r^2 + mu)), is
indefinite; the symmetrizer S = diag(1, -1/(2 r^2)) gives S A0 = diag(6, 1/(r^2 + mu)) > 0 and S A^th = [[0, -2/r^2],
[-2/r^2, 0]], symmetric, and S depends on gamma alone. In the symmetric class (fields of (r, th), q = q_th dth; q_phi1,
q_phi2 and J_phi vanish by the reflections) these equations are the whole system, and the construction stays in that
class; the closed forms printed by `--show` hold for every r > 0 (S3 checks the signs at one point). (b) At the
approximant's data (the data of g0 + lam [W] on Sigma) the linearisation of the constraint map in U has no coefficient
of order 1/lam (computed, S2; and S4, with the second harmonic chi dv dv nonzero on Sigma): the O(1/lam) second
derivatives of gamma enter the coefficients of U only through traces of W on the spheres, which vanish, and the d_r
K_rr terms of div K and d tr K cancel, so oscillations of the radial components are harmless (an oscillating trace does
produce such a coefficient: the mutants trace_W, trace_slip). The profiles g_j, j >= 2, the means and the phase
corrections contribute O(1) to the second derivatives of gamma and to dK. (c) The phase on Sigma is (tau0 + r)/lam, so
angular derivatives (along the spheres) of every coefficient are bounded uniformly in lam; at the approximant's data
the order-0 parts of all principal coefficients equal the background's (computed, S6; alpha = theta^3 H involves d_r
gamma, but W has zero trace on the spheres), so alpha and S A0 keep their signs for lam small; S depends on gamma
alone, whose first derivatives are bounded uniformly in lam, and Lemma 6.4 needs no d_r alpha. Lower-order coefficients
may oscillate at O(1) (those of d_th a in J_th and of a in rho do, the latter with nonzero mean, which is part of B_m
in Lemma 6.2(iii)); Lemma 6.4 needs only their angular regularity.

**Lemma 6.4 (the linear evolution; deduced).** Consider on [a, R] x S^3 the linear system, with coefficients measurable
in r for which M_s below is finite

    alpha d_r a - (Delta_alpha) a + b . d_S a + c a + e . (w, q) = F_rho,
    A0 d_r (w, q) + A^B d_B (w, q) + c' (w, q) + f d_r a + f' . d_S a + c'' a = F_J,                         (6.4)

Delta_alpha a second-order angular operator elliptic on each sphere with ellipticity constant >= delta0 > 0, alpha >=
alpha0 > 0, and an invertible symmetrizer S with S A0 >= A00 > 0 and S A^B symmetric, with zero data at r = a. For s >=
0 there is a unique solution, and

    sup_r (||a||_{H^(s+1)} + ||(w, q)||_{H^s}) + ||a||_{L^2 H^(s+2)} <= C (||F_rho||_{L^2 H^s} + ||F_J||_{L^2 H^s}),

norms on the spheres S^3, for s > 3/2 + 2, with C depending only on s, R - a, alpha0, delta0, A00 and an upper bound for
M_s := sup_r ||(alpha, Delta_alpha, S, S A0, S A^B)||_{H^(s+1)(S^3)} + sup_r ||(b, c, e, c', f, f', c'')||_{H^s(S^3)} +
int_a^R ||d_r (S A0)||_{L^inf} dr, and increasing in M_s; no other r-derivative of a coefficient enters. The bound is
tame: at an index s'' > s, with ||U||_(s''; [a, r]) the left side at index s'' on [a, r] and m_(s'')(r) the norms at
index s'' of the coefficients at r (those of M_(s''), without the supremum), ||U||_(s''; [a, r]) <= C (||F||_{L^2((a,
r); H^(s''))} + int_a^r m_(s'')(r') omega_s(r') dr'), with C depending only on s'', M_s and the bounds above, and
omega_s square-integrable on (a, R), its L^2 norm bounded by the solution's X_s norm. The inequality the proof gives,
for the squared energy Z at index s'' (Moser and Kato-Ponce), is d_r Z + c0 ||a||^2_(H^(s''+2)) <= omega_0 Z + C
||F||^2_(H^(s'')) + C m_(s'') omega_s Z^(1/2); integrating, taking the supremum over [a, r], and Young's and Gronwall's
lemmas give the bound (D26, the eighth verifier's m2).

*Proof.* Commute s angular derivatives (by the Killing fields of the round S^3) through (6.4); the commutators are
estimated in terms of M_s by the Moser and commutator (Kato-Ponce) inequalities on S^3 ([GO13], [DS23] Remark 2.3,
section 7). Parabolic energy: d_r (1/2) ||a||^2_{H^(s+1)} + c0 ||a||^2_{H^(s+2)} <= C (||a||^2_{H^(s+1)} + ||(w,
q)||^2_{H^s} + ||F_rho||^2_{H^s}) after dividing by alpha (its d_r is not needed: the equation is solved for d_r a).
Hyperbolic energy, after applying S to the second equation: d_r <(w, q), S A0 (w, q)>_{H^s} <= C (1 + ||d_r (S
A0)||_{L^inf}) ||(w, q)||^2_{H^s} + C ||(w, q)||_{H^s} (||d_r a||_{H^s} + ||a||_{H^(s+1)} + ||F_J||_{H^s}), the S A^B
terms integrating by parts on the closed spheres, and ||d_r a||_{H^s} <= C (||a||_{H^(s+2)} + ||(w, q)||_{H^s} +
||F_rho||_{H^s}) from the first equation. Young's inequality and Gronwall's lemma (which needs ||d_r (S A0)||_{L^inf}
only integrable in r) give the bound. Existence (Faedo-Galerkin; no citation). Let P_L be the L^2(S^3)-orthogonal
projection onto the eigenfunctions of the Laplacian with eigenvalue <= L(L + 2), for the covector q those of the Hodge
Laplacian on 1-forms. The eigenspaces are SO(4)-invariant, so P_L commutes with the Laplacian and with the Lie
derivative along every Killing field, which is what X^I means on q. Solve the first equation for d_r a (dividing by
alpha), and seek a_L and (w, q)_L in the range of P_L with d_r a_L = P_L[...] and P_L[S A0 d_r (w, q)_L] = P_L[...] (the
symmetrized second equation, d_r a_L in it), with the data of the lemma projected by P_L: a linear system of ordinary
differential equations in r for finitely many coefficients, whose matrix P_L S A0 P_L is positive definite on the range
(S A0 > 0) and continuous in r, the other coefficients and the sources being integrable in r, so Picard iteration gives
a unique absolutely continuous solution on [a, R]. The test functions of the argument above, X^{I*} X^I applied to a_L
or to (w, q)_L, lie in the range of P_L, so the projection drops out of each tested equation (<P_L G, f> = <G, f> for f
in the range) and the energy identities are those above, with one addition: the commutator [X^I, S A0] d_r (w, q)_L
needs ||d_r (w, q)_L||_{H^(s-1)}, which testing the projected second equation with X^{J*} X^J d_r (w, q)_L, |J| = 0,
..., s - 1 in turn, bounds by C (||(w, q)_L||_{H^s} + ||d_r a_L||_{H^(s-1)} + ||F_J||_{H^(s-1)}) (S A0 > 0; the
commutators are of lower order in J). So the bound holds for (a_L, (w, q)_L) uniformly in L; a weak-* limit L ->
infinity solves (6.4) and obeys it, and uniqueness follows from the bound. (Earlier forms of this step regularised by
epsilon Delta_S and cited a linear parabolic theory, [Hua15] and [MM10]; neither is needed, and [MM10] concerns a scalar
equation, N1STAR-LOG.md D18.) []

**Proposition 6.5 (the exact correction; deduced).** Let the stage data be those of Lemma 6.2 with N >= K + 3 and
(gamma, K) the data of g_app on Sigma. For lam <= lam0 there is U on Sigma, U = 0 on r < v_start - tau0, with
Phi(Psi(U)) = 0 on Sigma (Phi the constraint map) and sup_r ||d_r^j U(r)||_{H^s(S^3)} <= C_(j,s) lam^(N-2-j).

*Proof.* Write Phi(Psi(U)) = Phi(gamma, K) + L U + Nl(U), L the linearisation (Lemma 6.3) and Nl the remainder,
quadratic in (U, dU, d d_S a) with coefficients involving at most two derivatives of gamma and one of K, hence of size
<= C lam^-1. Phi(gamma, K) = O(lam^(N-2)) with all its angular derivatives (its profiles vanish below order N - 2 by
Lemma 6.1, and angular derivatives of profiles cost nothing on Sigma), and it vanishes on r < v_start - tau0. The
rho-component is linear in d_r a and in the angular second derivatives of a, with coefficients depending on a
algebraically (the scalar curvature of gamma + a dr dr contains no (d_r a)^2), and the J-component is linear in d(w, q)
with coefficients depending on a algebraically. Put ||U||_{X_s} := sup_r (||a||_{H^(s+1)} + ||(w, q)||_{H^s}) +
||a||_{L^2 H^(s+2)} + ||d_r a||_{L^2 H^s}, the left side of Lemma 6.4 with the d_r a the first equation gives. Iterate:
U_(i+1) solves, with zero data at r = a, the linear system (6.4) whose principal coefficients are frozen at U_i, as is
the whole coefficient f of d_r a in the J-equation, f(gamma, K; a, w, q), evaluated at U_i and multiplying d_r a_(i+1)
(it depends on a and on (w, q), so the terms q_th d_r a and a d_r a of J's remainder are not left in the source; in the
contraction the extra source (f(U_i) - f(U_(i-1))) d_r a_i is at most C lam^(N-2) ||U_i - U_(i-1)||_{X_(s0)} in L^2
H^(s0)), and whose sources are -Phi(gamma, K) and the remaining terms, at least quadratic and evaluated at U_i. Fix s0 >
3/2 + 4 and s := s0 + 2. At U = 0 the coefficients are those of Lemma 6.3; frozen at U_i they change by at most C lam^-1
||U_i||_X, d_r a_i entering M only through int ||d_r (S A0)||_{L^inf} dr <= C (1 + ||U_i||_{X_(s0)}); so while
||U_i||_{X_s} <= 2 C0 lam^(N-2), Lemma 6.4's hypotheses hold at indices s0 and s with constants independent of lam, for
lam small and N >= 4. Lemma 6.4 at index s keeps the iterates in the ball of radius 2 C0 lam^(N-2) of X_s, and at index
s0 gives ||U_(i+1) - U_i||_{X_(s0)} <= C lam^(N-3) ||U_i - U_(i-1)||_{X_(s0)} (the difference of the frozen coefficients
multiplies U_i, estimated in the higher norm), a contraction: bounded in X_s and contracting in X_(s0), the iterates
converge to a solution in X_s (the scheme of Kato and Majda for quasilinear symmetric hyperbolic systems, READ in [DS23]
section 4 and [AO14] section 4.1, section 7; the parabolic component obeys the same estimates). Uniqueness holds in the
ball of radius 2 C0 lam^(N-2) of X_s, by the difference estimate. The r-derivatives follow from the equations, each d_r
of a coefficient costing at most lam^-1. Smoothness (persistence of regularity): the coefficients and sources of each
step are smooth in the angles when the previous iterate is, so by Lemma 6.4 at every index the iterates U_i are smooth,
by induction. At an index s'' > s the bound of Lemma 6.4 is linear in the top norms, those of the coefficients
(functions of a) entering linearly by the Moser and Kato-Ponce inequalities with factors depending only on the X_s
bound; with E_i(r) the X_(s'') norm of U_i on [a, r] it reads E_(i+1)(r) <= A + W (int_a^r E_i^2)^(1/2), W uniform in i
(by Lemma 6.4's tame form: the sources enter in L^2 H^(s''), and the weight built from ||d_r a_(i+1)||_inf and ||d_r (w,
q)_(i+1)||_inf, bounded in L^2(a, R), through Cauchy-Schwarz, ||d_r (S A0)||_inf entering Gronwall's exponent; a source
term carrying d_r a_i would put E_i(r) itself on the right, which is why the coefficient of d_r a is frozen); by
induction and Minkowski's inequality E_i(r) <= A sum_k W^k ((r - a)^k / k!)^(1/2) for every i, with no smallness, and
the limit U lies in X_(s'') for every s''. A is proportional to lam^(N-2) (the source Phi(gamma, K) and the low norms
are) and W does not depend on lam, so ||U||_{X_(s'')} <= C_(s'') lam^(N-2) for every s'', which with the equations gives
the stated rate at every s and j. So U is smooth for lam <= lam0, lam0 independent of s''. Theorem E needs only k + 1 =
7 derivatives of the data in any case. []

### 6.4 Proof of Theorem D

Take the stage data of Lemma 6.2 with N := K + 3 and U of Proposition 6.5. Put g on Sigma: the spatial part gamma + a
dr dr, the lapse and shift of g_app, d_tau of the spatial part fixed by K + w Pi + q dr + dr q, and d_tau of the lapse
and shift fixed by D(g) = 0 (6.2). Then the constraints hold exactly (Proposition 6.5), D = 0 and, by (6.2), d_tau D =
0 on Sigma. For w := g - g_app on Sigma: the spatial part and d_tau of it are U and its tangential derivative
combinations, and d_tau w_{tau .} solves the linear relation D(g) - D(g_app) = -D(g_app) = O(lam^(N-1)) with invertible
coefficient. So, each derivative costing at most lam^-1, Data(w) <= C lam^-1 lam^(N-2) = C lam^K: (E4). The data are
smooth (Proposition 6.5), T^2 x Z2 x Z2-invariant (the construction commutes with the symmetries, by uniqueness in
Lemma 6.4, Proposition 6.5 and Lemma 5.3, Pol^+ being equivariant), and equal to the seed's data on Sigma cap {r <
v_start - tau0}. []

## 7. What is left

- **Verification.** Sections 0-4 were checked by one independent verifier (N1STAR-LOG.md D12): no major gap, one minor
  gap (Step 6 at the top level, repaired) and seven notes (repaired). Sections 5-6 were checked by a second (D15): no
  major gap, two minor gaps (Lemma 6.2(iii), Proposition 6.5, repaired) and ten notes (repaired, among them an error at
  O(lam) in `data5.py`'s inverse metric that touched no check, now caught by S5). The repairs were checked by a third
  (D16): the two repairs hold; it found two further minor gaps, both in the rewritten Lemma 6.4 and Proposition 6.5 (the
  regularisation must act on the symmetrized equation; the persistence of regularity must be stated as a tame
  inequality), and nine notes, all repaired as it proposed. A fourth (D18) checked those repairs and the two made at D17
  (Step 8, the time lines; Lemma 6.4): no major gap; one minor gap, the linear parabolic theory cited for Lemma 6.4
  ([MM10] is about a scalar equation, and [Hua15] was READ only in its introduction), repaired by a Faedo-Galerkin
  existence proof with no citation; five notes, repaired (the extensions in Step 8 by one operator for every order;
  g_app extended beyond Omega; Proposition 6.5's smoothness by induction; the (2.7) paraphrase marked). A fifth (D19)
  checked those: no major gap; two minor gaps (Proposition 6.5's smoothness bound, a term to freeze as a coefficient;
  Step 8, time clamped in the coefficients for [DS23] (A1)) and four notes (the projection on the covector q; Lemma
  6.4's coefficients need only M_s finite; the data extended in x before the change to y; the uniformity in tau of the
  extension constants deduced, not READ), all repaired. A sixth (D20) checked those: no major gap; one minor gap (f, the
  coefficient of d_r a in the J-equation, depends on a too, so the whole of it is frozen; it checked the repair) and two
  notes (the bound's form, A + W (int E_i^2)^(1/2); the tame form stated in Lemma 6.4), applied. A seventh (D21) read
  Proposition 6.5 whole with that repair: it holds; one minor gap (Lemma 6.4's tame clause, as stated, too weak for its
  use; restated in the integral form the proof gives, as it specified) and three notes (the weight list; the rate
  lam^(N-2) at every index; the status lines), applied. **Not read by a verifier after the edit:** the D21 restatement
  and notes.
- **READ at source (D17).** By the retrieval protocol of the site's Ask prompt: targets enumerated, routes by type with
  the open ones first, the sources a source names followed back and the papers citing a target followed forward, a
  blocked route left for the next and not retried, two independent routes closing a fact and one route fragile. rho
  counts the open routes whose statement covers the use here. Every standard theorem the proof invokes is now READ.

| target (used in) | route type | source | result | value found | rho |
| --- | --- | --- | --- | --- | --- |
| T1 local theory (St. 8) | preprint | [DS23] arXiv:2308.09851v1 Thm 2.4, 2.6 | open | exists, T(norm), continues | 2 |
| | preprint | [AO14] arXiv:1401.0277v1 Thm 1.1, Rem 1.2 | open | n >= 3, x-dependent, s > n/2 + 1 | |
| | citing paper | [CBCL06] arXiv:gr-qc/0608108v2 sec. 5.1 | open | Einstein, R^(n+1), s > n/2 (prose) | |
| | preprint | [Sbi13] arXiv:1309.7591 (1.2) | open | n = 3, smooth only | |
| | review | Bahouri-Chemin arXiv:math/0304390 sec. 1 | open | s > d/2 + 1 by energy, any d | |
| | lecture notes | Holzegel, Muenster SS 2021 (PDF); Luk, Stanford | blocked | proxy 403, scrape timeout | |
| | book | Ringstrom 2009; Choquet-Bruhat 2009 | untried | not reachable here | |
| T2 Ricci in the gauge (0.2) | primary | [CBCM10] arXiv:1006.4467 (2.7)-(2.9) | open | wave-map gauge, n + 1 | 2 |
| | citing paper | [CBCL06] (3.1) | open | wave coordinates, R^(n+1) | |
| | primary | [LR05] arXiv:math/0411109v2 (1.3) | open | harmonic gauge, 3 + 1 | |
| T2b gauge propagates (0.7) | primary | [LR05] p. 1, (2.1)-(2.5) | open | Bianchi; wave coordinate condition | 3 |
| | citing paper | [CBCL06] sec. 3 | open | n + 1 dimensions | |
| | review | Rendall arXiv:gr-qc/0505133v1 | open | constraints and gauge propagate | |
| T3 Sobolev (2.1, St. 8) | review | [BH17] arXiv:1704.07930 Thm 7.21, 7.26, 9.14 | open | sp > n; extension | 2 |
| | preprint | [DS23] sec. 4.1; [AO14] sec. 4.1.3 | open | the embedding, as used | |
| T3b one extension, all orders | primary | [LY22] arXiv:2211.15567v2 Thms 1, 26 | open | Seeley-type, smooth | 2 |
| | citing paper | [SY21] arXiv:2110.14477v4 secs. 1, 2.1 | open | Rychkov, Stein: Lipschitz | |
| | primary | Seeley 1964 (ams.org PDF) | blocked | fetch failed | |
| T4 linear parabolic (6.4) | preprint | [MM10] arXiv:1010.0733 Thm 1.1 | open | scalar only; not used | 0 |
| | preprint | [Hua15] arXiv:1506.05030 sec. 1 | open | introduction only; not used | |
| T5 Moser, Kato-Ponce (6.4, 6.5) | primary | [GO13] arXiv:1303.5144 sec. 1 | open | commutator on R^n, 1 < p < inf | 2 |
| | preprint | [DS23] Rem. 2.3(i), proof of Prop. 3.1 | open | composition, commutator on T^N | |
| T6 Kato-Majda scheme (6.5) | preprint | [AG22] arXiv:2204.01179v3 sec. 9 | open | bounded high, weak limit | 3 |
| | preprint | [DS23] secs. 4.1-4.2; [AO14] sec. 4.1 | open | bounded high, contracting low | |
| constraints | primary | [CD03] arXiv:gr-qc/0301073v2 (2.1); [Rac16] | open | as cited in section 6 | |
| (catalogue) | database | OpenAlex | blocked | proxy 403 | |

  The statements, verbatim where they carry the use:
  - [DS23] (M. M. Disconzi and Y. Shao, *Strongly hyperbolic quasilinear systems revisited*), for d_t u + A^i(u) d_i u
    = R(u) on T^N with A^i, R smooth in (t, x, zeta) (A1)-(A2), A^i xi_i diagonalizable with real eigenvalues (A3) that
    "do not meet each other" (A4): Theorem 2.4, "Let r > N/2 + 1 ... for any u0 in H^r with M~ = dist(U^c, Im(u0)) > 0,
    there exists some T > 0 depending on ||u0||_r and M~ such that (1.1) has a unique solution u in B(I) on I = [-T,
    T]"; Theorem 2.6, "one and only one of the following statements holds. T* = infinity; inf dist(U^c, Im u(t)) = 0;
    lim ||u||_B([0,T]) = +infinity", B(I) = C(I; C^1) cap C^1(I; C).
  - [AO14] (L. Andersson and T. A. Oliynyk, *A transmission problem for quasi-linear wave equations*): Theorem 1.1,
    "Suppose n >= 3, s in Z_(> n/2) ... Then there exist a T > 0 and a map U ... the unique solution ... Moreover, if
    ||u||_W^(1,infinity)((0,T) x T^n) < infinity, then ... u can be continued uniquely", under (1.3), "1/gamma |xi|^2
    <= A^ij(U) xi_i xi_j <= gamma |xi|^2 and A^00(U) <= -kappa"; Remark 1.2: (i)(a) A, F "depend explicitly on x",
    (ii)(b) the theorem holds for "A^mu nu(U, dU) d_mu d_nu U = F(U, dU) ... provided that we take s > n/2 + 1 and
    change the continuation principle to that of bounding ||U||_W^(2,infinity)". The case used is H = 0. Their
    statement assumes F(0, 0) = 0; a source F(x, 0, 0) in H^s, which the system here has, is carried by their proof
    ((4.2)) and by [DS23]'s statement, which allows R(t, x, 0) != 0.
  - [CBCL06] (Y. Choquet-Bruhat, P. T. Chrusciel, J. Loizelet): "The vacuum Einstein equations in wave coordinates on
    R^(n+1) constitute a set of quasi-diagonal quasi-linear wave equations" (3.1); "the harmonicity functions F^mu :=
    box_g x^mu satisfy an homogeneous linear system of wave equations on (V, g), with also d_t F^mu = 0, hence F^mu =
    0 if (V, g) is globally hyperbolic" (sec. 3); "Such a solution exists if the initial data belong to H^loc_(s+1) x
    H^loc_s, s > n/2" (sec. 5.1).
  - [CBCM10] (Y. Choquet-Bruhat, P. T. Chrusciel, J. M. Martin-Garcia), paraphrasing (2.7), which writes H^lambda :=
    g^(alpha beta) Gamma^lambda_(alpha beta) - W^lambda, W^lambda := g^(alpha beta) Gamma^^lambda_(alpha beta): H^lambda
    = g^(alpha beta)(Gamma^lambda_(alpha beta) - Gamma^^lambda_(alpha beta)) (2.7); "R_(alpha beta) = R^(H)_(alpha beta)
    + 1/2 (g_(alpha lambda) D^_beta H^lambda + g_(beta lambda) D^_alpha H^lambda)" (2.8), "R^(H)_(alpha beta) = -1/2
    g^(lambda mu) D^_lambda D^_mu g_(alpha beta) + f^[g, D^ g]_(alpha beta)", f^ "independent of the second derivatives
    of g" (2.9): this is (0.2), D = H, Dh = D^, in any dimension.
  - [BH17] (A. Behzadan and M. Holst, *Multiplication in Sobolev spaces, revisited*): Theorem 7.21, "Let Omega in R^n
    be a bounded open set with Lipschitz continuous boundary. Then for all s > 0 and for 1 <= p < infinity, there
    exists a continuous linear extension operator"; Theorem 7.26, "If sp > n, then W^(s,p)(Omega) -> L^infinity(Omega)
    cap C^0(Omega) and W^(s,p)(Omega) is a Banach algebra"; Theorem 9.14, the same embedding on compact manifolds.
  - [GO13] (L. Grafakos and S. Oh, *The Kato-Ponce inequality*): "||J^s(fg) - f (J^s g)||_(L^p) <= C [||grad
    f||_(L^infinity) ||J^(s-1) g||_(L^p) + ||J^s f||_(L^p) ||g||_(L^infinity)] for 1 < p < infinity and s > 0".
    [DS23] Remark 2.3(i): "for any u in H^s ... ||N(u)||_s <= C_I + F_I(||u||_infinity) ||u||_s". On S^3 both follow
    from R^3 through a finite atlas and a partition of unity, the spaces of [BH17] section 9 being defined so (deduced).
  - [MM10] (C. Mantegazza and L. Martinazzi), Theorem 1.1 concerns a scalar equation ("smooth initial datum u0 : M ->
    R"; systems only in a remark), and the [Hua15] sentence quoted at D17 is from its introduction, not the statement of
    its Theorem 2.4. Neither is used since D18: Lemma 6.4's existence is by Faedo-Galerkin, deduced.
  - [LY22] (H. Lu and L. Yao, *On Seeley-type universal extension operators for the upper half space*): Theorem 1, an
    extension operator E with "(ii) ... E : W^(k,p)(R^n_+) -> W^(k,p)(R^n) and E : C^(k,s)(R^n_+) -> C^(k,s)(R^n) are
    defined and bounded for all k in Z, 0 < p <= infinity and 0 < s < 1. E : C^k(R^n_+) -> C^k(R^n) is bounded for all k
    = 0, 1, 2, ..." (simultaneously); Theorem 26, "Universal Seeley's extension on smooth domains": for a bounded smooth
    domain, "E : W^(k,p)(Omega) -> W^(k,p)_c(U) ... bounded for all k in Z, 0 < p <= infinity"; Lemma 27, composition
    with bounded diffeomorphisms; and of Seeley's operator, "E : C^k(R^n_+) -> C^k(R^n) for all k = 0, 1, 2, ... In
    particular Seeley's extension [preserves] C^infinity-smoothness". [SY21] (Z. Shi and L. Yao), restating Rychkov:
    "for a Lipschitz domain Omega there exists an operator E = E_Omega that is bounded on Besov spaces E : B^s_pq(Omega)
    -> B^s_pq(R^n) for all 0 < p, q <= infinity, s in R ... Since E is one single operator which works for all such
    spaces, we call it an universal extension operator", and Stein: "an extension operator E_S which is independent of
    k, such that E_S : W^(k,p)(Omega) -> W^(k,p)(R^n) is bounded for all k in N and 1 <= p <= infinity". The two papers
    share an author; Seeley's and Stein's originals were not reachable.
  - [AG22] (F. Angeles, arXiv:2204.01179v3, *The Cauchy problem for a quasilinear system of equations with coupling in
    the linearization*): the iterates bounded in H^s, a weakly convergent subsequence (9.6); [AO14] sec. 4.1: "the
    well-known strategy ... of setting up an appropriate iterative approximation scheme and showing convergence by
    establishing boundedness in a high norm followed by contraction in a low norm".
  - [LR05] (H. Lindblad and I. Rodnianski), arXiv:math/0411109v2, READ 2026-10-19: the reduced equations in wave
    coordinates, their (1.3), "g^{alpha beta} d_alpha d_beta g_mu nu = F_mu nu(g)(dg, dg)"; the gauge's data, their
    (2.3)-(2.5); and "any solution of the system (2.1) with initial data ... compatible with (2.2) and constraint
    equations, gives rise to a solution of the full Einstein system. In addition, thus constructed tensor g_mu nu will
    satisfy the wave coordinate condition (2.2) for all times" (3 + 1, harmonic gauge; the argument is the contracted
    Bianchi identity, p. 1: "The Bianchi identities D_mu G^{mu nu} = 0", which holds in any dimension and for the gauge
    relative to g0). Rendall, arXiv:gr-qc/0505133v1: local existence and uniqueness of the reduced equations, Cauchy
    stability, and "it must be checked that it is a solution of the original equations. This means checking that the
    constraints and gauge conditions propagate." [CD03] (2.1), the constraint map, which "are the general relativistic
    constraint equations whatever the space-dimension n", and [Rac16], as cited in section 6. The identities (6.1) and
    (6.2) are deduced from the Bianchi identity and the constraint map by the algebra written in 6.1.
- **Fragile.** The universal extension rests on two papers that share an author ([LY22], [SY21]); the per-order
  extension and the embedding have two routes each. The continuation statements READ are for n >= 3 ([AO14]) and any N
  ([DS23]); none is for a domain with boundary, which Step 8 avoids by the torus and the uniqueness from Lemma 2.3.

## 8. Part (iii) for lam > 0 (D25)

**Proposition 8.1 (one apparent horizon per column; deduced, with `horizon5.py` H1-H3).** Assume mu0 > sqrt(72) l5^2
and the hypotheses of section 0.7 with K >= 6. For a column, the set of points of D_T cap {tau >= tau0} with v and the
angles omega in S^3 fixed and r varying, let theta^+_lam(r) be the outgoing null expansion, for g_lam, of the sphere
S_(v,r) := {tau = v - r, |x| = r} at the point (v, r, omega). There are lam1 in (0, lam0] and C, delta1 > 0
independent of lam such that for lam <= lam1:
- (a) on every column theta^+_lam has at most one zero, and theta^+_lam > 0 above it, < 0 below it;
- (b) on every column with sqrt(mu(v)) <= v - tau0 - delta1 it has exactly one zero R_lam(v, omega), and
  |R_lam(v, omega) - sqrt(mu(v))| <= C lam;
- (c) the spheres S_(v,r) with r <= sqrt(mu(v)) - C lam (within the domain) are trapped, both future null expansions
  being negative at every point, and those with r >= sqrt(mu(v)) + C lam are untrapped.
In particular there is no inner apparent horizon, and the apparent horizon converges to sqrt(mu) at O(lam). If mu0 =
sqrt(72) l5^2, (a) holds, and (b)-(c) hold on the columns with mu(v) >= mu0 + delta1.

*Proof.* (i) The expansion. The normal space of S_(v,r) is spanned by dtau and dr. For a metric g near g0 let k_g be the
null covector dr + alpha dtau whose normal n = g^-1 k_g is future directed with n(tau) = 1 (for g0, alpha = (m - 1)/(m +
1), m = mu/r^2, and n0(tau) = 1: `horizon5.py` H1); it depends smoothly on g. In the coordinates (tau, r, th, p1, p2)
the expansion is theta^+ = -gamma^AB Gamma[g]^c_AB (k_g)_c, A, B tangent to the sphere: a smooth function of g and
linear in its first derivatives; being a scalar of the sphere and of g, it is estimated in the Cartesian arrays of 0.1,
where the axes are regular points, the polar chart serving only for H1-H2. (ii) The background. For g0, theta^+ = c(r) 3
(1 - mu/r^2)/(2 r) with c = 2 r^2/ (r^2 + mu) > 0 (H1); mu = mu(v) enters only algebraically, since the sphere lies in
{v = const} and no v-derivative of the metric enters Gamma^c_AB contracted as above. Its one zero on (0, inf) is r =
sqrt(mu), simple: d_r theta^+ = 3/mu there (c = 1 at r^2 = mu). The future ingoing normal is L0 = -g0^-1 dv, with
expansion -3/r < 0 (H1). (iii) The approximant. Write g_app = g0 + lam [g1] + sum_(j>=2) lam^j [g_j] with g1 = m1 + W(X,
th + phi1) (section 5.4). The fast derivative lam^-1 (d_a v) d_th enters theta^+ only through d_c of the tangential
components g_AB (d_A v = 0 on the sphere), and the term of order lam^0 it produces from lam [W] is (1/2) k(g0^-1 dv)
d_th (tr_S W) (H2's reason), which vanishes because tr_S W = tr_g0 W - 2 W(ell, n0)/g0(ell, n0) = 0 by W(ell, .) = 0 and
tr_g0 W = 0 (lead5.py L5); m1 has no th-dependence; the terms lam^j [g_j], j >= 2, give at most lam^(j-1). H2 computes
this for a profile W tangent and traceless on the spheres, with chi dv^2 added and k_g, gamma^-1 and g^-1 to first order
in lam: no term of order lam^-1 or lam^0 beyond g0's, and a trace on the spheres gives one. So theta^+(g_app) =
theta^+(g0) + lam [Th1] + lam^2 E with Th1 a profile and E bounded with its X-derivatives. Along a column v is constant
(H3), so d_r [Th1] = [d_r Th1] along it with no 1/lam: |theta^+(g_app) - theta^+(g0)| + |d_r (theta^+(g_app) -
theta^+(g0))| <= C lam along every column. (iv) The remainder. theta^+ is smooth in g and linear in dg, so
|theta^+(g_lam) - theta^+(g_app)| <= C (|w| + |dw|) and its r-derivative along a column is at most C (|w| + |dw| + |d^2
w|); by section 4, Step 1, ||d^i w||_inf <= C M lam^(K-3-i) for i <= 4, so both are at most C lam^(K-5) <= C lam (K >=
6). (v) The zero. The columns lie in the compact Omega, r >= r_q(v) >= q0 > 0, and sqrt(mu(v)) - r_q(v) =
mu^(1/4)(mu^(1/4) - (sqrt(72) l5^2)^(1/4)) is increasing in mu, hence >= its value at mu0, which is positive when mu0 >
sqrt(72) l5^2. Fix delta in (0, that value) with d_r theta^+(g0) >= 3/(2 mu_max) on |r - sqrt(mu(v))| <= delta, and let
m_delta > 0 be the minimum of |theta^+(g0)| on the rest of the columns. For C lam < min(m_delta, 3/(4 mu_max)):
theta^+_lam has no zero where |r - sqrt(mu)| > delta, and on |r - sqrt(mu)| <= delta it is strictly increasing in r, so
it has at most one zero, with the stated signs: (a). If the column contains [sqrt(mu) - delta, sqrt(mu) + delta] (true
when sqrt(mu(v)) <= v - tau0 - delta1 with delta1 := delta), theta^+_lam changes sign there, so it has exactly one zero
R_lam, and |R_lam - sqrt(mu)| <= C lam / (3/(4 mu_max)): (b). (c): theta^+_lam < 0 at every point of a sphere below the
band and > 0 above it, and the ingoing expansion is -3/r + O(lam) < 0 everywhere. At mu0 = sqrt(72) l5^2 the same
argument runs on the columns where sqrt(mu) - r_q >= delta, which is mu(v) >= mu0 + delta1 for some delta1 > 0; (a)
needs only the monotonicity band and holds on every column. []

