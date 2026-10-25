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

**Theorem P (2026-10-20, D32)** builds the same solution from the record's free data at past null infinity, so that the
datum on Sigma_tau0 is the trace of the solution coming in and Theorem D is not needed on that route (section 9,
computed inputs in `past5.py`). It is PROVED (D35): a verifier found one major gap in the near-region estimate (D34), it
was repaired, and a second verifier found that the repair closes it.

**Theorem M (2026-10-20, D37)** gives the solution's Bondi mass at past null infinity: g_lam has Bondi coordinates there
with an expansion in r^(-1/2), the five-dimensional Bondi mass law holds for it pointwise, and its mean mass is mu(v) +
O(lam) while the shell passes and mu + (2/9) lam^2 A^2 int env'^2 + O(lam^3) after it, the rate the numerics measure
(section 11, computed inputs in `bondi5.py`). It is deduced; a twelfth verifier found no major gap and five minor ones,
repaired (D40), and a thirteenth found one major gap in a repair, Lemma 11.0's energy region, repaired by running the
identity on the approximating solutions of Theorem P's construction (D44); the repairs are not yet read.

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
f||_{L^inf} <= C lam^(-3-i) |f|_{i+3}. For k = 6, |f g|_k <= C lam^-3 |f|_k |g|_k, and if a is a profile, |[a] f|_k <=
C |f|_k. *Proof.* The annuli A(tau) are images of the fixed annulus {a <= |x| <= a + 1 + delta0} under radial maps with
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
gives (M1). P f(x) = lam^-4 int rho((Phi(x) - y)/lam) f(y) dy, and d_x falls on rho: (M2). For (M3), f(x) - f(Phi(x) -
lam z) is the integral of d_x f along the segment from x to Phi(x) - lam z, of length <= 3 lam; the segment stays in
A(tau) by the estimate above (its radial component is at least lam toward the interior near either sphere), and the
change of variables gives the bound. (M4): the chain rule, d_x[f(Phi - lam z)] = DPhi^T (d f)(Phi - lam z); and (d_j
f)(Phi(x) - lam z) = -lam^-1 d_{z_j}[f(Phi(x) - lam z)], integrated by parts onto rho. (M5) is Friedrichs' lemma in this
form: [a, P] d_j f (x) = int rho(z)(a(x) - a(Phi(x) - lam z))(d_j f)(Phi(x) - lam z) dz; integrating by parts in z as in
(M4), the factor lam^-1 meets either d_z of a(Phi(x) - lam z), which is O(lam), or a(x) - a(Phi(x) - lam z), which is
O(lam). (M6): sigma depends on tau through b(tau). Higher derivatives by induction. []

**Lemma 2.3 (energy; deduced).** Let gt be a Lorentzian metric on Omega with |gt - g0| <= eps1 and ||d gt||_inf <= M1,
and let u (a function or a Cartesian array) satisfy -(1/2) gt^{ab} d_a d_b u = f on Omega. Then for tau in [tau0,
tau_end],

    ||d u(tau)|| + ||u(tau)|| <= C(M1) ( ||d u(tau0)|| + ||u(tau0)|| + int_{tau0}^{tau} ||f(s)|| ds ).            (2.2)

*Proof.* With the multiplier Y := -gt^-1 dtau (future timelike, Lemma 1.1(e)) and the energy current J^a = T^a_b Y^b,
T_ab = d_a u d_b u - (1/2) gt_ab gt(du, du), the divergence theorem on Omega cap {tau0 <= s <= tau} in the coordinate
density gives the flux through Sigma_tau equal to the flux through Sigma_tau0 minus the fluxes through the lateral
boundaries plus the bulk. The lateral boundaries are spacelike with Omega to their past (Lemma 1.1(b), (c), (e)), so
their fluxes are nonnegative and are dropped; the fluxes through Sigma_tau are comparable to ||d u||^2 (dominant energy,
Y and the normal uniformly timelike); the bulk is bounded by C(M1)(||d u||^2 + ||f|| ||d u||) since d gt and d Y are
bounded. ||u|| is added through d_tau ||u||^2 = 2 <u, d_tau u> plus a boundary term b'(tau) int_{|x|=b} |u|^2 <= 0.
Gronwall. []

**Lemma 2.4 (transport; deduced, `ks5.py` K4).** If L0 phi - c(X) phi = f on Omega with c bounded, then ||phi(tau)|| <=
e^{C(tau - tau0)} (||phi(tau0)|| + int ||f||).

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

**Lemma 3.3 (the ell-ell component; deduced).** box~ s = c1 . d h + c0 . h + c2 . d phi + c3 phi - 2q F(ell, ell) - 2q
N(w)(ell, ell) + 2q N_phi(ell, ell) + sum_{a, i} c^{ai} d_a d_i h, where c0..c3 are bounded profiles, the sum runs over
pairs with i spatial, |c^{ai}| <= C(lam + |w|) and |d c^{ai}| <= C(1 + |d w|); N_phi(ell, ell) contains no second
derivative of phi. There is no 1/lam coefficient.

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

**Step 4 (h; deduced).** Apply d^alpha, |alpha| = j <= k, to (3.5) and use Lemma 2.3 for each component, then
multiply by lam^j. The commutator [d^alpha, g^{ab}] d_a d_b h has terms d^i g . d^(j-i+1) d h, i >= 1; with ||d^i
g_app||_inf <= C lam^(1-i), lam^j of each is at most C lam^(j-i+1) ||d^(j-i+1) d h|| <= C N; the w part is at most C
M lam^(K-4) N (i <= 4 in L^inf; for i >= 5, d^i w in L^2 and the other factor in L^inf by Lemma 2.1). The right side
of (3.5): lam^j ||d^alpha F|| <= C_R lam^K by (E3); B.dh and C.h give C N (profile coefficients cost lam^-1 per
derivative, compensated by the weights); the term lam^-1 ((1 - P)s) G2 gives sum_i lam^(i-1) ||d^i (1 - P) s|| <= C
sum_i lam^i ||d^i d s|| <= C N by (M3), (M4), (M6); lam^-1 (ell_app - ell).dphi G2 and phi[T1] give C N;
(1/2)(box~_app phi) G1 = (1/2) Psi G1 + (1/2)(c d^2 phi) G1 with |c| <= C lam, and by Lemma 3.4 lam d^2 phi is
controlled by lam L0 P s, lam d_x P s, lam d phi and lam d_x^2 phi, each at most C N at every level j <= k (no
Bernstein inequality is needed: lam^(j+1) ||d^j L0 P s|| <= C lam^(j+1) ||d^j d s|| by (M4), (M6)); B1.dphi, C1 phi
give C N. The nonlinear terms N(w) and N_phi are at most C lam^-5 N^2 + C lam^-3 N^2 by Lemmas 2.1 and Step 1 (worst:
quadratic in d w, |d w d w|_k <= C lam^-3 |d w|_k^2 <= C lam^-5 N^2), hence at most C M^2 lam^(2K-5) <= C M^2
lam^(K+1). So

    sum_{j<=k} lam^j ||d^j d h(tau)|| + ||h(tau)|| <= C ( N(tau0) + int_{tau0}^{tau} (N + C_R lam^K + C M^2 lam^(K+1)) ).

**Step 5 (phi; deduced).** Apply d^alpha to (3.4): L0 d^alpha phi = -(1/2) d^alpha P s + [L0, d^alpha] phi, where [L0,
d^alpha] has smooth lam-independent coefficients and involves d^(j) phi with lower or equal order; lam^j ||d^alpha P s||
<= C sum_{i<=j} lam^i ||d^i s|| <= C N by (M1), (M4), (M6). The same for d phi (with d P s <= C P d s). For lam d_x^2
phi use the transport of Lemma 3.4: lam^(j+1) ||d^alpha d_x^2 P s|| = lam^(j+1) ||d_x P(d^alpha d_x s)|| + (commutators)
<= C lam^j ||d^j d s|| by Bernstein (M2) in the one spatial derivative. Lemma 2.4 then gives the phi-part of N(tau) at
most C (N(tau0) + int_{tau0}^{tau} N) (d_tau phi does not vanish on Sigma_tau0).

**Step 6 (Psi; deduced).** Apply d^alpha to (3.6) and Lemma 2.4 (c = 2/r <= 2/a). The term box~ P s = P
box~ s + [box~, P] s. By Lemma 3.3, box~ s is first order in (h, phi) up to F, the nonlinear terms and
sum c^{ai} d_a d_i h; for the last, P(c d_a d_i h) = P d_i(c d_a h) - P((d_i c) d_a h) and ||P d_i f||
<= C lam^-1 ||f|| (M2, M4), with |c| <= C(lam + |w|): at most C ||d h|| at level 0, and at level j,
lam^j ||d^alpha P d_i (c d h)|| <= C lam^(j-1) sum_i ||d^i c||_inf ||d^(j-i) d h|| <= C N since ||d^i
c||_inf <= C lam^(1-i). For the commutator, [g0^{ab}, P] d_a d_b s with at least one spatial index is
bounded by C ||d s|| by (M5); the tau-tau term is rewritten with d_tau^2 s = (box~ s - 2 g0^{tau i}
d_tau d_i s - g0^{ij} d_i d_j s)/g0^{tautau} (g0^{tautau} = -1 - mu/r^2), after which (M5) applies to
the spatial terms; in box~ s (Lemma 3.3) the first-order terms gain the factor lam of (M5)'s second
form, and the terms c^{ai} d_a d_i h are written d_i(c d_a h) - (d_i c) d_a h, so that (M5)'s first form
bounds them by C ||c d h|| + C ||d c||_inf ||d h|| <= C N (at level j likewise; applying the second form
to them would cost a derivative at j = k). The terms of g0^{ab}(d_a d_b P - P d_a d_b) s carry, by (M4)
and (M6), a factor lam and a spatial derivative inside P, so they are at most C ||d s|| by (M4);
likewise at level j. The other terms of (3.6) are first order in P s and phi. So the Psi-part of N(tau)
is at most C (N(tau0) + int (N + C_R lam^K + C M^2 lam^(K+1))).

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
gives D^(j) = 0 on Omega for j <= m - 2 and d_th D^(m-1) = 0; then the first derivatives of D^(m-1) on Sigma vanish too:
the tangential ones by (F1), the normal one of the mean by (F2) at order m - 1, and the oscillating part is zero. For m
= 1, 2 the same holds directly: D^(0) = 0, and for m = 2 the order-0 transport, with d_th D^(1) = 0 on Sigma by (F1),
gives d_th D^(1) = 0 on Omega, and the normal derivative of <D^(1)> vanishes on Sigma by (F2) at order 1. The tangential
derivatives of D^(m) vanish by (F1), and the phase part lam^-1 (d u) d_th D^(m+1) of the derivatives has mean zero. So
the order-m mean of 2 G(g_app)(n, .) on Sigma is d_n <D^(m)> (the order-m mean of (6.2)), the E-part having mean zero
(after stage m, R^(i) = 0 for i < m and R^(m) = -(1/2) e_(m+1) d_th^2 W, of mean zero): (F2) at order m is the order-m
mean of the constraint equations. That is P(h_m, Q_m) + B_m(h_m) = S_m, with P the linearisation of the constraint map
at the data of g0 on Sigma ([CD03] (2.2)), B_m algebraic in h_m (the means of the products of h_m and of gh_(m+1) of (i)
with the oscillating data), and S_m known. Solve it with h_m = a_m dr dr, Q_m = w_m Pi + q_m dr + dr q_m by Lemma 6.4
(B_m is a zeroth-order term of the kind allowed there), from zero data at r = a. Its sources vanish where the earlier
stages' data and the waves do, so (a_m, w_m, q_m) vanish on r < v_start - tau0, and are smooth. []

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

norms on the spheres S^3, for s > 3/2 + 2, with C depending only on s, R - a, alpha0, delta0, A00 and an upper
bound for M_s := sup_r ||(alpha, Delta_alpha, S, S A0, S A^B)||_{H^(s+1)(S^3)} + sup_r ||(b, c, e, c', f, f',
c'')||_{H^s(S^3)} + int_a^R ||d_r (S A0)||_{L^inf} dr, and increasing in M_s; no other r-derivative of a
coefficient enters. The bound is tame: at an index s'' > s, with ||U||_(s''; [a, r]) the left side at index s''
on [a, r] and m_(s'')(r) the norms at index s'' of the coefficients at r (those of M_(s''), without the
supremum), ||U||_(s''; [a, r]) <= C (||F||_{L^2((a, r); H^(s''))} + int_a^r m_(s'')(r') omega_s(r') dr'), with C
depending only on s'', M_s and the bounds above, and omega_s square-integrable on (a, R), its L^2 norm bounded by
the solution's X_s norm. The inequality the proof gives, for the squared energy Z at index s'' (Moser and
Kato-Ponce), is d_r Z + c0 ||a||^2_(H^(s''+2)) <= omega_0 Z + C ||F||^2_(H^(s'')) + C m_(s'') omega_s Z^(1/2);
integrating, taking the supremum over [a, r], and Young's and Gronwall's lemmas give the bound (D26, the eighth
verifier's m2).

*Proof.* Commute s angular derivatives (by the Killing fields of the round S^3) through (6.4); the
commutators are estimated in terms of M_s by the Moser and commutator (Kato-Ponce) inequalities on S^3
([GO13], [DS23] Remark 2.3, section 7). Parabolic energy: d_r (1/2) ||a||^2_{H^(s+1)} + c0 ||a||^2_{H^(s+2)}
<= C (||a||^2_{H^(s+1)} + ||(w, q)||^2_{H^s} + ||F_rho||^2_{H^s}) after dividing by alpha (its d_r is not
needed: the equation is solved for d_r a). Hyperbolic energy, after applying S to the second equation: d_r
<(w, q), S A0 (w, q)>_{H^s} <= C (1 + ||d_r (S A0)||_{L^inf}) ||(w, q)||^2_{H^s} + C ||(w, q)||_{H^s} (||d_r
a||_{H^s} + ||a||_{H^(s+1)} + ||F_J||_{H^s}), the S A^B terms integrating by parts on the closed spheres,
and ||d_r a||_{H^s} <= C (||a||_{H^(s+2)} + ||(w, q)||_{H^s} + ||F_rho||_{H^s}) from the first equation.
Young's inequality and Gronwall's lemma (which needs ||d_r (S A0)||_{L^inf} only integrable in r) give the
bound. Existence (Faedo-Galerkin; no citation). Let P_L be the L^2(S^3)-orthogonal projection onto the
eigenfunctions of the Laplacian with eigenvalue <= L(L + 2), for the covector q those of the Hodge Laplacian
on 1-forms. The eigenspaces are SO(4)-invariant, so P_L commutes with the Laplacian and with the Lie
derivative along every Killing field, which is what X^I means on q. Solve the first equation for d_r a
(dividing by alpha), and seek a_L and (w, q)_L in the range of P_L with d_r a_L = P_L[...] and P_L[S A0 d_r
(w, q)_L] = P_L[...] (the symmetrized second equation, d_r a_L in it), with the data of the lemma projected
by P_L: a linear system of ordinary differential equations in r for finitely many coefficients, whose matrix
P_L S A0 P_L is positive definite on the range (S A0 > 0) and continuous in r, the other coefficients and
the sources being integrable in r, so Picard iteration gives a unique absolutely continuous solution on [a,
R]. The test functions of the argument above, X^{I*} X^I applied to a_L or to (w, q)_L, lie in the range of
P_L, so the projection drops out of each tested equation (<P_L G, f> = <G, f> for f in the range) and the
energy identities are those above, with one addition: the commutator [X^I, S A0] d_r (w, q)_L needs ||d_r
(w, q)_L||_{H^(s-1)}, which testing the projected second equation with X^{J*} X^J d_r (w, q)_L, |J| = 0,
..., s - 1 in turn, bounds by C (||(w, q)_L||_{H^s} + ||d_r a_L||_{H^(s-1)} + ||F_J||_{H^(s-1)}) (S A0 > 0;
the commutators are of lower order in J). So the bound holds for (a_L, (w, q)_L) uniformly in L; a weak-*
limit L -> infinity solves (6.4) and obeys it, and uniqueness follows from the bound. (Earlier forms of this
step regularised by epsilon Delta_S and cited a linear parabolic theory, [Hua15] and [MM10]; neither is
needed, and [MM10] concerns a scalar equation, N1STAR-LOG.md D18.) []

**Proposition 6.5 (the exact correction; deduced).** Let the stage data be those of Lemma 6.2 with N >= K + 3 and
(gamma, K) the data of g_app on Sigma. For lam <= lam0 there is U on Sigma, U = 0 on r < v_start - tau0, with
Phi(Psi(U)) = 0 on Sigma (Phi the constraint map) and sup_r ||d_r^j U(r)||_{H^s(S^3)} <= C_(j,s) lam^(N-2-j).

*Proof.* Write Phi(Psi(U)) = Phi(gamma, K) + L U + Nl(U), L the linearisation (Lemma 6.3) and Nl the
remainder, quadratic in (U, dU, d d_S a) with coefficients involving at most two derivatives of gamma and
one of K, hence of size <= C lam^-1. Phi(gamma, K) = O(lam^(N-2)) with all its angular derivatives (its
profiles vanish below order N - 2 by Lemma 6.1, and angular derivatives of profiles cost nothing on
Sigma), and it vanishes on r < v_start - tau0. The rho-component is linear in d_r a and in the angular
second derivatives of a, with coefficients depending on a algebraically (the scalar curvature of gamma + a
dr dr contains no (d_r a)^2), and the J-component is linear in d(w, q) with coefficients depending on a
algebraically. Put ||U||_{X_s} := sup_r (||a||_{H^(s+1)} + ||(w, q)||_{H^s}) + ||a||_{L^2 H^(s+2)} + ||d_r
a||_{L^2 H^s}, the left side of Lemma 6.4 with the d_r a the first equation gives. Iterate: U_(i+1)
solves, with zero data at r = a, the linear system (6.4) whose principal coefficients are frozen at U_i,
as is the whole coefficient f of d_r a in the J-equation, f(gamma, K; a, w, q), evaluated at U_i and
multiplying d_r a_(i+1) (it depends on a and on (w, q), so the terms q_th d_r a and a d_r a of J's
remainder are not left in the source; in the contraction the extra source (f(U_i) - f(U_(i-1))) d_r a_i is
at most C lam^(N-2) ||U_i - U_(i-1)||_{X_(s0)} in L^2 H^(s0)), and whose sources are -Phi(gamma, K) and
the remaining terms, at least quadratic and evaluated at U_i. Fix s0 > 3/2 + 4 and s := s0 + 2. At U = 0
the coefficients are those of Lemma 6.3; frozen at U_i they change by at most C lam^-1 ||U_i||_X, d_r a_i
entering M only through int ||d_r (S A0)||_{L^inf} dr <= C (1 + ||U_i||_{X_(s0)}); so while ||U_i||_{X_s}
<= 2 C0 lam^(N-2), Lemma 6.4's hypotheses hold at indices s0 and s with constants independent of lam, for
lam small and N >= 4. Lemma 6.4 at index s keeps the iterates in the ball of radius 2 C0 lam^(N-2) of X_s,
and at index s0 gives ||U_(i+1) - U_i||_{X_(s0)} <= C lam^(N-3) ||U_i - U_(i-1)||_{X_(s0)} (the difference
of the frozen coefficients multiplies U_i, estimated in the higher norm), a contraction: bounded in X_s
and contracting in X_(s0), the iterates converge to a solution in X_s (the scheme of Kato and Majda for
quasilinear symmetric hyperbolic systems, READ in [DS23] section 4 and [AO14] section 4.1, section 7; the
parabolic component obeys the same estimates). Uniqueness holds in the ball of radius 2 C0 lam^(N-2) of
X_s, by the difference estimate. The r-derivatives follow from the equations, each d_r of a coefficient
costing at most lam^-1. Smoothness (persistence of regularity): the coefficients and sources of each step
are smooth in the angles when the previous iterate is, so by Lemma 6.4 at every index the iterates U_i are
smooth, by induction. At an index s'' > s the bound of Lemma 6.4 is linear in the top norms, those of the
coefficients (functions of a) entering linearly by the Moser and Kato-Ponce inequalities with factors
depending only on the X_s bound; with E_i(r) the X_(s'') norm of U_i on [a, r] it reads E_(i+1)(r) <= A +
W (int_a^r E_i^2)^(1/2), W uniform in i (by Lemma 6.4's tame form: the sources enter in L^2 H^(s''), and
the weight built from ||d_r a_(i+1)||_inf and ||d_r (w, q)_(i+1)||_inf, bounded in L^2(a, R), through
Cauchy-Schwarz, ||d_r (S A0)||_inf entering Gronwall's exponent; a source term carrying d_r a_i would put
E_i(r) itself on the right, which is why the coefficient of d_r a is frozen); by induction and Minkowski's
inequality E_i(r) <= A sum_k W^k ((r - a)^k / k!)^(1/2) for every i, with no smallness, and the limit U
lies in X_(s'') for every s''. A is proportional to lam^(N-2) (the source Phi(gamma, K) and the low norms
are) and W does not depend on lam, so ||U||_{X_(s'')} <= C_(s'') lam^(N-2) for every s'', which with the
equations gives the stated rate at every s and j. So U is smooth for lam <= lam0, lam0 independent of s''.
Theorem E needs only k + 1 = 7 derivatives of the data in any case. []

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

**Proposition 8.1 (one zero per column of the spheres' outgoing expansion; deduced, with `horizon5.py` H1-H3).** Assume
mu0 > sqrt(72) l5^2 and the hypotheses of section 0.7 with K >= 6. For a column, the set of points of D_T cap {tau >=
tau0} with v and the angles omega in S^3 fixed and r varying, let theta^+_lam(r) be the outgoing null expansion, for
g_lam, of the sphere S_(v,r) := {tau = v - r, |x| = r} at the point (v, r, omega). There are lam1 in (0, lam0] and C,
delta1 > 0 independent of lam such that for lam <= lam1: - (a) on every column theta^+_lam has at most one zero, and
theta^+_lam > 0 above it, < 0 below it; - (b) on every column with sqrt(mu(v)) <= v - tau0 - delta1 it has exactly one
zero R_lam(v, omega), and |R_lam(v, omega) - sqrt(mu(v))| <= C lam; - (c) the spheres S_(v,r) with r <= sqrt(mu(v)) - C
lam (within the domain) are trapped, both future null expansions being negative at every point, and those with r >=
sqrt(mu(v)) + C lam are untrapped. In particular there is no inner apparent horizon, and the apparent horizon converges
to sqrt(mu) at O(lam). If mu0 = sqrt(72) l5^2, (a) holds, and (b)-(c) hold on the columns with mu(v) >= mu0 + delta1.

*Proof.* (i) The expansion. The normal space of S_(v,r) is spanned by dtau and dr. For a metric g near g0 let k_g :=
c(g)(dr + alpha dtau) be the outgoing null covector of the sphere, with c(g) > 0 fixed by n(tau) = 1 for its normal n =
g^-1 k_g, which is future directed (for g0, alpha = (m - 1)/(m + 1), m = mu/r^2, and n0(tau) = 1: `horizon5.py` H1); it
depends smoothly on g. In the coordinates (tau, r, th, p1, p2) the expansion is theta^+ = -gamma^AB Gamma[g]^c_AB
(k_g)_c, A, B tangent to the sphere: a smooth function of g and linear in its first derivatives; being a scalar of the
sphere and of g, it is estimated in the Cartesian arrays of 0.1, where the axes are regular points, the polar chart
serving only for H1-H2. (ii) The background. For g0, theta^+ = c(r) 3 (1 - mu/r^2)/(2 r) with c = 2 r^2/ (r^2 + mu) > 0
(H1); mu = mu(v) enters only algebraically, since the sphere lies in {v = const} and no v-derivative of the metric
enters Gamma^c_AB contracted as above. Its one zero on (0, inf) is r = sqrt(mu), simple: d_r theta^+ = 3/mu there (c =
1 at r^2 = mu). The future ingoing normal is L0 = -g0^-1 dv, with expansion -3/r < 0 (H1). (iii) The approximant. Write
g_app = g0 + lam [g1] + sum_(j>=2) lam^j [g_j] with g1 = m1 + W(X, th + phi1) (section 5.4). The fast derivative lam^-1
(d_a v) d_th enters theta^+ only through d_c of the tangential components g_AB (d_A v = 0 on the sphere), and the term
of order lam^0 it produces from lam [W] is (1/2) k(g0^-1 dv) d_th (tr_S W) (H2's reason), which vanishes because tr_S W
= tr_g0 W - 2 W(ell, n0)/g0(ell, n0) = 0 by W(ell, .) = 0 and tr_g0 W = 0 (lead5.py L5); m1 has no th-dependence; the
terms lam^j [g_j], j >= 2, give at most lam^(j-1). H2 computes this for a sample profile tangent and traceless on the
spheres, and H2b for the record's wave itself at the shifted phase th + phi1, with chi dv^2 and a mean m1 of every
T^2-invariant component, symbolically in every function (k_g, gamma^-1 and g^-1 to first order in lam): no term of
order lam^-2, lam^-1 or lam^0 beyond g0's, and a trace on the spheres gives one. So theta^+(g_app) = theta^+(g0) + lam
[Th1] + lam^2 E with Th1 a profile and E bounded with its X-derivatives. Along a column v is constant (H3), so d_r
[Th1] = [d_r Th1] along it with no 1/lam: |theta^+(g_app) - theta^+(g0)| + |d_r (theta^+(g_app) - theta^+(g0))| <= C
lam along every column. (iv) The remainder. theta^+ is smooth in g and linear in dg, so |theta^+(g_lam) -
theta^+(g_app)| <= C (|w| + |dw|) and its r-derivative along a column is at most C (|w| + |dw| + |d^2 w|); by section
4, Step 1, ||d^i w||_inf <= C M lam^(K-3-i) for i <= 4, so both are at most C lam^(K-5) <= C lam (K >= 6). (v) The
zero. The columns lie in the compact Omega, r >= r_q(v) >= q0 > 0, and sqrt(mu(v)) - r_q(v) = mu^(1/4)(mu^(1/4) -
(sqrt(72) l5^2)^(1/4)) is increasing in mu, hence >= its value at mu0, which is positive when mu0 > sqrt(72) l5^2. Fix
delta in (0, that value) with d_r theta^+(g0) >= 3/(2 mu_max) on |r - sqrt(mu(v))| <= delta, and let m_delta > 0 be the
minimum of |theta^+(g0)| on the rest of the columns. For C lam < min(m_delta, 3/(4 mu_max)): theta^+_lam has no zero
where |r - sqrt(mu)| > delta, and on |r - sqrt(mu)| <= delta it is strictly increasing in r, so it has at most one
zero, with the stated signs: (a). If the column contains [sqrt(mu) - delta, sqrt(mu) + delta] (true when sqrt(mu(v)) <=
v - tau0 - delta1 with delta1 := delta), theta^+_lam changes sign there, so it has exactly one zero R_lam, and |R_lam -
sqrt(mu)| <= C lam / (3/(4 mu_max)): (b). (c): theta^+_lam < 0 at every point of a sphere below the band and > 0 above
it, and the ingoing expansion is -3/r + O(lam) < 0 everywhere. At mu0 = sqrt(72) l5^2 the same argument runs on the
columns where sqrt(mu) - r_q >= delta, which is mu(v) >= mu0 + delta1 for some delta1 > 0; (a) needs only the
monotonicity band and holds on every column. []

**The mass of a sphere.** For a spacelike 3-sphere S in a five-dimensional Lorentzian metric g let n+, n- be its future
null normals, theta+- their expansions, Theta := 2 theta+ theta- / (-g(n+, n-)) (independent of the normalisation of
n+-), R := (Area(S)/(2 pi^2))^(1/3), and M[S](g) := R^2 (1 + (R^2/9) <Theta>), <.> the mean over S: the five-dimensional
Hawking mass. For g0 and S_(v,r), M = mu(v) (`mass5.py` M1). M is natural in the sense of diffeomorphism covariance,
M[S](phi^* g) = M[phi(S)](g) for every diffeomorphism phi and every g near g0 (D30: the ninth verifier's N-4), and is a
smooth function of g and dg on S.

**Lemma 8.2 (the quarter-turn symmetry; deduced, with `mass5.py` M2-M4).** Let sigma be the isometry th -> pi/2 - th,
phi1 <-> phi2 of S^3, extended to R x R^4 fixing tau and r; it is an isometry of g0 fixing v and each S_(v,r) (M4). For
a family of profiles put (Sg)_j(X, th) := (-1)^j sigma^* g_j(X, 3 pi/2 - th). (a) If G = g0 + sum_j lam^j g_j then G~ :=
g0 + sum_j lam^j (Sg)_j = sigma^* G(., 3 pi/2 - .; -lam), and its two-scale residual is R[G~](X, th; lam) = sigma^*
R[G](X, 3 pi/2 - th; -lam) (M3, with sigma an isometry of g0 commuting with Ric^H, which is built from g and g0 alone):
its coefficient of lam^m is (-1)^m sigma^* R^(m)(., 3 pi/2 - .), so S preserves (E1)-(E3) at every order. (b) The
stage-0 wave is S-invariant: W_TT(sigma X, 3 pi/2 - s) = -W_TT(X, s) (M2, the record's two polarizations a quarter turn
apart; one quadrature alone, or two in phase, is not), and chi, the unique solution of its transport with zero data, is
S-invariant with it. Every later stage of section 5 and every choice of Lemma 6.2 (phi_m = 0 and (m_m)_(tau .) = 0 on
Sigma, d_th gh_(m+1) := -Pol^+(...) with Pol^+ O(4)-equivariant, the unique solutions of Lemmas 5.3 and 6.4) is the
unique solution of a problem that S maps to itself. On the unknowns of section 5 the induced action is m_j -> (-1)^j
sigma^* m_j, phi_j -> (-1)^j sigma^* phi_j and gh_j -> (-1)^j sigma^* gh_j(., 3 pi/2 - .), consistent with the Taylor
rewriting of 5.4 (it needs sigma^* phi1 = -phi1, which follows from L0 phi1 = -(1/2) m1(ell, ell)). Hence Sg = g:
sigma^* g_j(., 3 pi/2 - .) = (-1)^j g_j, and for the means m_j = <g_j>, sigma^* m_j = (-1)^j m_j; in particular sigma^*
m1 = -m1. []

**Proposition 8.2 (the mean mass; deduced, with `mass5.py`).** Under the hypotheses of section 0.7 with K >= 6, for
every sphere S_(v,r) in D_T cap {tau >= tau0} and lam <= lam0: |M[S_(v,r)](g_lam) - mu(v)| <= C lam^2 if v <= v_start
or v >= v_end, and <= C lam if v_start < v < v_end.

*Proof.* The oscillating profiles (W, chi, gh_m and the phase terms) vanish outside v_start < v < v_end: each is the
solution of a transport along ell, at fixed v, whose sources and data are supported there (Lemma 5.3, Lemma 6.2(i),
the wave being proportional to env). So for v outside that interval g_app = g0 + lam m1 + lam^2 E with E bounded with
its derivatives, and M[S](g_lam) = M[S](g0) + lam DM[m1] + O(lam^2) + O(|w| + |dw|), DM the derivative of M at g0 on
S. DM is linear, and naturality with sigma fixing g0 and S gives DM[sigma^* m] = DM[m] (M[S](g0 + eps sigma^* m) =
M[sigma(S)](sigma_* g0 + eps m) = M[S](g0 + eps m)); by Lemma 8.2, DM[m1] =
DM[sigma^* m1] = -DM[m1] = 0. The remainder is at most C lam^(K-4) <= C lam^2 (section 4, Step 1). (For v < v_start
the means vanish too: their sources and data on Sigma are supported in v >= v_start, and v does not decrease along
future causal curves of g0.) Inside the shell the fast derivative of lam [W] enters theta+- only through
tr_S d_th W = 0 (Proposition 8.1, (iii)), and the area through tr_S W = 0, so M[S](g_app) - mu(v) = O(lam). []

The record's "mean mass" is the angular mean of the mass aspect at past null infinity; the Hawking mass of the spheres
of the domain is its counterpart here, and the two are the same limit only through a construction from past null
infinity, which is not part of this proposition.


## 9. Theorem P: the construction from past null infinity (D32)

**Status. Theorem P is PROVED** (deduced, with its exact inputs computed in `past5.py`, P1-P8; D35). A tenth independent
verifier read it whole (D34): the far region, the decay counting, the gauge argument and the radiation field held; the
near region did not close as first written, because the commutator of the mollifier with box~ forces Psi's transport by
a term of size ||d s|| with no decay in t. That term is an exact L0-derivative (Lemma 9.4b, P8), and Proposition 9.9
transports Psi - (1/2) X_s, whose forcing decays. An eleventh verifier read the repair and the seated minor findings
(D35) and found that it closes the gap and that Theorem P holds as stated; its two minor findings and four notes are
seated (the coefficient class of the angular derivatives of phi, the full commutator with mu(v) and psi(tau, v) in Lemma
9.4b and P8, the data terms at tau_T, the constants, a rate in Theorem A_P), and these are the only text of section 9 no
verifier has read after the edit.

**Theorem P.** Let the seed, A, env and the record's angular profile be as in section 0 (mu' = (2/9) A^2 env^2), and
let W_TT be the record's first-order wave (section 5.1), whose r^(3/2)-normalised components at past null infinity
are the record's free data F, G. There is beta0 > 0, depending on the seed, A, env and the profile but not on K or
lam, such that for every K >= 6 there are lam_P > 0 and C with the following property. For 0 < lam <= lam_P there is
a smooth vacuum metric g_lam on P cup Omega (P in 9.1), in the wave-map gauge relative to g0, with

- (P-i) g_lam = g0 on P cap {v <= v_start}: the seed, exactly;
- (P-ii) the record's radiation field at past null infinity: for every v < V_P and xhat,
  r^(3/2) (g_lam - g0 - lam [W_TT]) (v - r, r xhat) -> 0 as r -> oo, [W_TT] taken at the phase v/lam;
- (P-iii) on P, |g_lam - g_app| <= C lam^(K-3) t^-2 and |d(g_lam - g_app)| <= C lam^(K-4) t^-2 (t in 9.1, g_app the
  approximant of Theorem A_P of order N = K + 4 + ceil(4 beta0));
- (P-iv) on Omega, the conclusions of Theorem E with this K, (0.5) included;
- (P-v) invariance under T^2 x Z2 x Z2; and uniqueness: g_lam is the only solution of Ric^H(g) = 0 on P with
  (P-i), with |g - g_app| + |d(g - g_app)| <= eps_P t^(-3/2), and with the energy of g - g_app on A_P(tau)
  tending to zero as tau -> -oo.

Hence N1* holds with the record's data at past null infinity: section 0.7's argument applies on Omega to g_lam, with
the datum on Sigma_tau0 now its trace, and Theorem D is not used. The proof is in sections 9.1-9.4; 9.5 reports what
the radiation field gives at past null infinity, and what it does not.

### 9.1 The past domain (deduced from `past5.py` P1 and Lemma 1.1)

Put t := 1 + tau0 - tau for tau <= tau0, fix kappa := 1/2, h(tau) := kappa t^(-1/4), and
V_P := V + 1 + (tau_end - tau0) + kappa, so that V_P - kappa is the largest v on Sigma_tau0 cap Omega (section 1).

    P := { tau <= tau0,  |x| >= a,  v + h(tau) <= V_P },     P+ := P cap {v >= v_start},
    A_P(tau) := Sigma_tau cap P+ = { r_in(tau) <= |x| <= r_out(tau) },                                      (9.1)
    r_in := v_start - tau,  r_out := V_P - h(tau) - tau.

**Lemma 9.1.** (a) Each Sigma_tau is spacelike (Lemma 1.1(a)). (b) The outer boundary B := {v + h(tau) = V_P} is
spacelike, g0^-1(dPhi, dPhi) = -2 h' - h'^2 (1 + mu/r^2) <= -(kappa/2) t^(-5/4) (P1), and v + h(tau) increases along
future causal curves, so P lies to the past of B. (c) Sigma_tau0 cap P = Sigma_tau0 cap Omega. (d) On P+,
t + a1 <= r <= t + a2 with a1 := v_start - tau0 - 1 > sqrt(mu0) and a2 := V_P - tau0 - 1, and the thickness
r_out - r_in = V_P - h - v_start lies in [d0, d1], d0 := V_P - kappa - v_start >= 1, d1 := V_P - v_start. (e) L0 is
tangent to the inner boundary {v = v_start} of P+; the past integral curve of L0 through any point of P stays in P and
runs to past null infinity (v and xhat fixed, r -> oo). (f) There is eps_P > 0 such that for every Lorentzian g on P
with |g^-1 - g0^-1| <= eps_P t^(-5/4), B and the Sigma_tau are spacelike for g with g^-1(dPhi, dPhi) <= -(kappa/4)
t^(-5/4), {r = a} is spacelike with r decreasing along future causal curves, L0 is transverse to Sigma_tau, and
J^-(p; g) cap {tau >= tau1} lies in P for every p in P and tau1 <= tau(p).

*Proof.* (a), (b): P1 computes g0^-1(dPhi, dPhi) for Phi = v + h(tau) exactly, with h' = (kappa/4) t^(-5/4) > 0;
for a future causal Y, dv(Y) = -g0(L0, Y) >= 0 and dtau(Y) > 0, so dPhi(Y) > 0. (c): at tau0, h = kappa and the
condition reads v <= V_P - kappa. (d): r = v - tau with v in [v_start, V_P]; d0 >= 1 because V_P - kappa = V + 1 +
tau_end - tau0 >= v_start + 1. (e): along -L0, v and xhat are fixed, tau decreases and h decreases, so v + h <= V_P
is kept, r = v - tau grows without bound, and v >= v_start is kept. (f): (a), (b) and Lemma 1.1(b) are strict, with
margins of at least (kappa/2) t^(-5/4) in (b) and fixed margins in (a) and in Lemma 1.1(b), which hold at r = a <
sqrt(mu0) whatever tau is; the causal claim follows as in Lemma 1.1(e). []

**Lemma 9.2 (the seed region).** Let g solve Ric^H(g) = 0 on P cap {tau1 <= tau <= tau2}, be C^2, satisfy the margin
of Lemma 9.1(f), and agree with g0 on Sigma_tau1 cap {v <= v_start} with its first tau-derivative. Then g = g0 on P cap
{tau1 <= tau <= tau2, v <= v_start}.

*Proof.* g0 is vacuum on {v <= v_start}, where mu is constant (section 0.1). For 0 < eps <= 1 let R_eps := P cap {tau
>= tau1, v + eps h(tau) <= v_start}, and tau* the supremum of the tau' <= tau2 with g = g0 on R_eps cap {tau <= tau'}.
R_eps cap Sigma_tau* is compact, g = g0 on it, and g is continuous, so on a neighbourhood U of it |g^-1 - g0^-1| <=
(eps kappa/8) t^(-5/4); there {v + eps h = v_start} is spacelike for g and g0 with R_eps to its past (P1 with eps
kappa for kappa), and {r = a} likewise (Lemma 9.1(f)). The difference u := g - g0 solves -(1/2) g^{ab} d_a d_b u = f
with |f| <= C (|u| + |d u|) (the principal part and Q of (0.2) are smooth in (g, dg), and d^2 g0 is bounded), u = d_tau
u = 0 on Sigma_tau*, and Lemma 2.3's proof on R_eps cap {tau* <= tau <= tau* + delta} (delta small, the region in U)
gives u = 0 there: so tau* = tau2. Letting eps -> 0 covers {v < v_start}, and continuity covers v = v_start. []

### 9.2 Inequalities on the past slices (deduced)

All constants depend on P (a, a1, a2, d0, d1, kappa) and not on tau or lam; 0 < lam <= lam1. With Omega_ab := x_a d_b
- x_b d_a the rotations of R^4, the scaled norms on A_P(tau) are

    |f|_(j,P) := sum_{i + |beta| <= j} lam^i ||d^i Omega^beta f||,      ||.|| the flat L^2(A_P(tau)),              (9.2)

d^i the spacetime coordinate derivatives of order i; the rotations carry no weight because Omega v = 0 (P6), so
Omega [f] = [Omega f] costs no power of lam.

**Lemma 9.3 (Sobolev with rotations; Poincare).** (a) ||f||_inf <= C t^(-3/2) sum_{i + |beta| <= 3} ||d_r^i Omega^beta
f|| on A_P(tau), d_r = xhat.d_x; hence ||d^i f||_inf <= C lam^(-3-i) t^(-3/2) |f|_(i+3,P). (b) If f = 0 on {r =
r_in(tau)}, ||f|| <= C ||d_r f||.

*Proof.* (a) In polar coordinates A_P(tau) = [r_in, r_out] x S^3 with r_out - r_in in [d0, d1]. On [0, d] x S^3 with
the product metric, H^3 embeds in L^inf with a constant uniform for d in [d0, d1] ([BH17] Theorem 7.26 in charts; a
compact family of compact manifolds with boundary); the covariant derivatives of S^3 are bounded by the rotations,
|nabla^k f| <= C sum_{|beta| <= k} |Omega^beta f| (the Omega_ab span every tangent space of S^3, their commutators
are rotations); and int |.|^2 dr domega <= r_in^-3 int |.|^2 r^3 dr domega <= t^-3 ||.||^2 since r_in >= t (Lemma
9.1(d)). For the scaled form apply this to d^i f and reorder: [Omega_ab, d_c] = -delta_ac d_b + delta_bc d_a. (b) On
each ray f(r) is the integral of d_r f from r_in, over a length at most d1, and r^3 varies over the ray by a factor
at most (1 + d1)^3 (r_in >= 1); Cauchy-Schwarz. []

**Lemma 9.4 (the mollifier on the past slices).** The mollifier (2.1), with sigma(tau, x) := sigma0((|x| -
r_in)/(r_out - r_in)) and rho radial, satisfies (M1)-(M6) on A_P(tau) with constants independent of tau, and commutes
with the rotations (hence with T^2 and both reflections).

*Proof.* The proof of Lemma 2.2 is local at the scale lam and uses only that the annulus has thickness at least d0 >=
1 and inner radius at least 1, that DPhi = I + lam E with E bounded with its derivatives (E involves d sigma, of size
1/d0, and d xhat, of size 1/r <= 1), and, for (M6), that d_tau r_in = -1 and d_tau r_out = -1 - h' are bounded.
Phi(x) = x + 2 lam sigma xhat and rho are invariant under O(4), so P (f o R) = (P f) o R for R in O(4). []

**Lemma 9.4b (the mollifier's commutator with box~; computed P8, deduced; D34).** Write P = C o M, with M f := rho_lam *
f the convolution (rho_lam(y) := lam^-4 rho(y/lam)) and C g := g o Phi the radial shift. In the coordinates (tau, v,
xhat), Delta(tau) := r_out - r_in, C is g(tau, v, xhat) -> g(tau, psi_tau(v), xhat) with psi_tau(v) = v + 2 lam
sigma0((v - v_start)/Delta(tau)), since |x| - r_in = v - v_start at fixed tau. Put

    X_f := 4 lam sigma_v C(d_r M f),     sigma_v := sigma0'((v - v_start)/Delta)/Delta.                         (9.4b)

Then [box~, P] f = -L0 X_f + R_f, and for j <= k, with Z ranging over {lam d_tau, lam d_r, Omega} (d_r = xhat.d_x),

    ||Z^j X_f|| <= C lam sum_{i <= j} ||Z^i d f||,
    ||Z^j R_f|| <= C (t^-1 + h') sum_{i <= j} ||Z^i d f|| + ||Z^j R'_f||,

where R'_f collects the terms with two time derivatives of f, each with a factor at most C lam (mu r^-3 + |mu'| r^-2),
which for f = s are rewritten through the equation of Lemma 3.3 as in Step 6. *Proof.* By (9.5), box~ = -(1 + mu/r^2)
L0^2 - 2 d_r L0 + (3/r) d_r + r^-2 Deltaring, with L0 = d_tau at fixed (v, xhat) and d_r = d_v at fixed tau (P8 checks
the radial part against (9.5)). For psi independent of tau, P8 gives exactly [box~_rad, C] g = -L0(2 (psi' - 1) C d_v
g) + (3 psi'/r - 3/(psi - tau)) C d_v g - mu (1/r^2 - 1/(psi - tau)^2) C L0^2 g, with 2 (psi' - 1) = 4 lam sigma_v; the
dependence of psi on tau, and of mu on v, add exactly the terms listed in P8, (mu(psi) - mu(v))/(psi - tau)^2 C L0^2 g
and three terms with a factor psi_t or psi_tt, where psi_t = 2 lam sigma0' (v - v_start) h'/Delta^2 and psi_tt are at
most C lam h' (Lemma 9.1: Delta' = -h') and |mu(psi) - mu(v)| <= 2 lam |mu'|; the angular part gives [r^-2 Deltaring,
C] = (r^-2 - (psi - tau)^-2) C Deltaring, of size C lam r^-3 times two rotations, that is C lam r^-1 times two
derivatives. M commutes with the constant-coefficient part eta^{ab} d_a d_b of box~; with the rest, -(mu/r^2) L0 L0 (L0
= d_tau - xhat.d_x), it commutes up to terms with the factor lam |d(mu xhat xhat/r^2)| <= C lam (mu r^-3 + |mu'| r^-2)
(M5). Apply this to g = M f: a lam-weighted second spatial derivative of M f costs no more than one derivative of f
(Bernstein, (M2)); 3 psi'/r - 3/(psi - tau) is at most C/r; and L0 commutes with lam sigma_v, C and M up to factors C
(h' + r^-1) (L0 sigma_v = O(h'), the psi_t terms above, [xhat.d_x, M] = O(lam r^-1) by (M5)), while the Z commute with
them up to bounded operators of the same order, which suffices: every term of R_f already carries a decaying factor,
and the bound on X_f needs none. Z commutes with L0 exactly (d_tau, d_r and Omega do, and L0 = d_tau - d_r), so the
same holds at every order. []

So the part of [box~, P] f with no decaying factor is an exact L0-derivative. Lemma 2.2's version on Omega has the same
form, harmlessly there; on P it would force Psi's transport (3.6) by a term of size ||d s|| with no decay, which
Proposition 9.9 removes by transporting Psi - (1/2) X_s in place of Psi.

**Lemma 9.5 (energy on P).** Let gt be a Lorentzian metric on P with the margin of Lemma 9.1(f) and ||d gt||_inf <=
k(tau) on Sigma_tau cap P+ (the support of u; near r = a, in the seed region, d g0 is only bounded), and let u vanish on
P cap {v <= v_start} and satisfy -(1/2) gt^{ab} d_a d_b u = f on P cap {tau1 <= tau <= tau2}. Then for tau in [tau1,
tau2]

    ||d u(tau)|| <= C exp(C int_{tau1}^{tau} k) ( ||d u(tau1)|| + int_{tau1}^{tau} ||f|| ),                   (9.3)
    ||u(tau)|| <= C ||d u(tau)||.

*Proof.* Lemma 2.3's proof on P cap {tau1 <= s <= tau}: B has P to its past with a spacelike normal for gt (Lemma
9.1(b), (f)), so its flux is nonnegative and is dropped; u vanishes near {r = a}; on P+ the slices are uniformly
spacelike and Y = -gt^-1 dtau uniformly timelike (g0^-1(dtau, dtau) = -1 - mu/r^2 with mu/r^2 bounded), so the
fluxes through Sigma_tau are comparable to ||d u||^2 with constants independent of tau; the bulk is at most C k ||d
u||^2 + ||f|| ||d u||. Gronwall; the second bound is Lemma 9.3(b). []

**Lemma 9.6 (transport on P).** Let L0 psi - (c0/r) psi = f on P+ cap {tau1 <= tau <= tau2}, c0 a constant, and gam
:= c0 - 3/2. With a_+ := a1 if gam > 0 and a_+ := a2 if gam <= 0,

    (t + a_+)^gam ||psi(tau)|| <= (t1 + a_+)^gam ||psi(tau1)||                                              (9.4)
                                  + int_{tau1}^{tau} (t' + a_+)^gam ||f(tau')|| dtau',

*Proof.* As in Lemma 2.4, d_tau ||psi||^2 = 2 <psi, L0 psi> - int (3/r) psi^2 + (boundary terms): L0 is tangent to
{v = v_start}, so that face contributes nothing, and the outer face contributes -h' int_{r = r_out} psi^2 r^3 domega
<= 0. Hence d_tau ||psi||^2 <= 2 gam int psi^2/r + 2 <psi, f>, and t + a1 <= r <= t + a2 (Lemma 9.1(d)) gives
d_tau ||psi|| <= gam (t + a_+)^-1 ||psi|| + ||f||. Since d_tau t = -1, d_tau ((t + a_+)^gam ||psi||) <= (t +
a_+)^gam ||f||. []

The transports used below have c0 = 0 (phi and its derivatives in the frame of section 9.3; gam = -3/2), c0 = 3/2
(the oscillating profiles; gam = 0) and c0 = 2 (Psi; gam = 1/2).

### 9.3 Decay classes and the approximant from past null infinity (Theorem A_P)

On P+ use (v, r, xhat): d_v := d_v at fixed (r, xhat), which is d_tau at fixed x, and ell f := ell . df, the
derivative along the ingoing generators (ell = -L0, ell v = 0, ell r = 1); d_r = d_v + ell. Profiles are smooth on P x
S^1 and vanish for v <= v_start (then to all orders at v = v_start, env being smooth).

- E_p: profiles f with |d_X^alpha Omega^beta d_th^j f| <= C r^-p on P+ x S^1 for all alpha, beta, j (Cartesian d_X).
- L_p ("a leading term"): f = r^-p F + f~ with F(v, xhat, th) smooth, bounded with all derivatives and vanishing
  for v <= v_start, and f~ in E_(p+1/2).
- O_p ("transported"): f in L_p whose remainder also has ell f~ in E_(p+3/2); then ell f in L_(p+1).

**Lemma 9.7 (the decay calculus; computed P2-P4, deduced).** (a) E_p E_q is in E_(p+q) and L_p L_q in L_(p+q); d_X,
Omega, d_th and d_v preserve E_p and L_p. (b) In (v, r, xhat), g0^-1(du, du') = d_v u ell u' + ell u d_v u' + (1 -
mu/r^2) ell u ell u' + r^-2 <dring u, dring u'> (dring on the unit S^3; g^vv = 0, g^vr = 1, g^rr = 1 - mu/r^2, P2), and
for every function

    box~ u = 2 d_v ell u + (3/r) d_v u + (1 - mu/r^2) ell ell u + (3/r) ell u + r^-2 Deltaring u.                 (9.5)

(c) box~ (r^-p F) = (3 - 2p) r^(-p-1) d_v F + E_(p+2); at p = 3/2 the first term vanishes (P2), so box~ W_TT is in
E_(7/2); and box~ maps O_p into L_(p+1). (d) If S = r^-q S_q + S~ is in L_q with q > 5/2 and c is in E_(3/2) (a
multiplication, or as in Lemma 5.2 a bounded operator on zero-mean functions of th with coefficients in E_(3/2)), the
transport (ell + 3/(2r) + c) Z = S has exactly one solution with r^(3/2) Z -> 0 along every generator, and Z = -r^(1-q)
S_q/(q - 5/2) + Z~ is in O_(q-1) (P4); at q = 5/2 a logarithm appears (P4).

*Proof.* (a) Leibniz, with d_X = xhat (d_v + ell) + r^-1 (angular), whose coefficients have bounded derivatives. (b)
(9.5) is the flat operator in polar coordinates written in (v, r) plus -(mu/r^2) L0 L0 = -(mu/r^2) ell ell; P2 checks it
on r^-p M(v) Y for symbolic p, every M and harmonics Y of degrees 0, 1, 2, and computes g0^-1 in (v, r). (c) From (9.5):
on r^-p F the terms 2 d_v ell and (3/r) d_v give (3 - 2p) r^(-p-1) d_v F and the others are E_(p+2); on f~ with ell f~
in E_(p+3/2) every term of (9.5) is in E_(p+3/2). The Cartesian components of W_TT are r^(-3/2) F (P3). (d) Along a
generator, with C(r) := -int_r^oo c, (r^(3/2) e^C Z)' = r^(3/2) e^C S, and |C| <= C' r^(-1/2) (for an operator c, e^C is
the propagator of the linear ordinary differential equation along the generator, bounded since the integral of the norm
of c converges); so Z = -r^(-3/2) e^(-C) int_r^oo r'^(3/2) e^(C(r')) S dr' is the solution, and every other differs by
r^(-3/2) e^(-C) times a function of (v, xhat, th). The leading term is P4's; the remainder has sources S~ and -c Z in
E_(q+1/2), so it is in E_(q-1/2), and ell Z~ = -(3/(2r)) Z~ - c Z + S~ is in E_(q+1/2). d_v, Omega and d_th commute with
ell and r. []

**Theorem A_P (deduced; P3, P5, Lemma 9.7 and Lemmas 5.1-5.3).** For every N the stages of section 5 have unique
solutions on P with nothing coming in from past null infinity: the energy of each m_m on A_P(tau) tends to zero as tau
-> -oo, and phi_m, chi and gh_(m+1) are the transport solutions of Lemma 9.7(d) that vanish there. They vanish for v
<= v_start, are T^2 x Z2 x Z2 invariant and obey Lemma 8.2's symmetry, and

    W_TT in O_(3/2) (a pure leading term),   chi in O_2,   m_m in L_2,   phi_m in L_1 with ell phi_m in L_2,
    gh_(m+1) in O_2.                                                                                        (9.6)

The approximant g_app of (0.4), built from them as in section 5.4, satisfies (E1) and (E2) on P, and Ric^H(g_app) =
lam^(N-1) [R_N] + lam^N [R'_N] with R_N, R'_N in E_3, uniformly for 0 < lam <= 1, so |Ric^H(g_app)|_(k,P) <= C_R
lam^(N-1) t^(-3/2) (K = N - 1, as in section 5.4). On Omega the profiles continue as the solutions of Lemma 5.3 with
their own data on Sigma_tau0, g_app is smooth on P cup Omega, and section 5's conclusions hold on Omega.

*Proof.* **The count.** Give the factors of (0.2) these classes: g0 - eta in L_2 (a coefficient, not a profile: it does
not vanish for v <= v_start, and the class is used for it only through its bounds); Gamma[g0] in E_2 (its mu' part is
(mu'/(2 r^2)) ell dv dv) and H0 in E_3; W_TT in O_(3/2); chi, gh_i in O_2; m_i in L_2; phi_i in L_1, with ell phi_i in
L_2. *Claim:* for m >= 1, every monomial of Rm^(m) (Lemma 5.1) that contains none of m_m, phi_m, gh_(m+1) lies in L_3.
A monomial of (0.2) has at most two derivatives; g^-1 is expanded about g0^-1, each term of the expansion adding
profile factors; the phase enters only through du = dv + sum lam^j dphi_j acting on an oscillating factor. (i) Two
profile factors from {W, chi, gh_i, m_i} give L_3 at least (Lemma 9.7(a)). (ii) A factor dphi_i (in E_1 only) occurs as
(d_a phi_i) d_th Y with Y oscillating; with a second profile factor besides Y the monomial is in E_4. Without one, both
derivatives sit on Y in the principal part, contracted by g0^-1, and the monomial is one of g0^-1(dphi_i, dv) d_th^2 Y
= (ell phi_i) d_th^2 Y, g0^-1(dphi_i, dphi_j) d_th^2 Y, g0^-1(dphi_i, d d_th Y) or (box~ phi_i) d_th Y. By (9.5) the
first is L_2 L_(3/2), the second L_3 L_(3/2) (g^vv = 0: no product d_v phi_i d_v phi_j occurs), the third d_v phi_i ell
d_th Y + ell phi_i d_v d_th Y + ... is in L_1 L_(5/2) + L_2 L_(3/2) (Y in O_p gives ell Y in L_(p+1)), and box~ phi_i =
2 d_v ell phi_i + (3/r) d_v phi_i + ... is in L_2: each in L_(7/2). (iii) A monomial with one profile factor and no
dphi: the factor is of weight j and carries derivatives of total weight m - j. If it is a mean m_j, the only such terms
are those of its own stage equation (j = m) and Gamma[g0] times m_j (E_2 L_2). If it is oscillating, two slow
derivatives give box~ Y (j = m; in L_3 by Lemma 9.7(c), E_(7/2) for W) and one fast derivative gives Th Y (j = m + 1:
the unknown gh_(m+1)); two fast derivatives carry g0^-1(dv, dv) = 0. This proves the claim; the same count shows that
the coefficients with which the unknowns enter (a)-(c) of Lemma 5.3 are in E_2 for m_m and E_3 for dphi_m in (a),
E_(3/2) for gh_(m+1) in (a) (the mean of a product with d_th W), and in (c) E_(3/2) for m_m, Psi_m := box~ phi_m and
ell phi_m, E_(5/2) for d_v phi_m and r^-1 Omega phi_m (it multiplies ell d_th W or r^-1 Omega d_th W).

**Stage 0.** lead5.py's L1-L5 hold pointwise wherever the profiles are defined. The vv second harmonic of R^(0) is
exactly r^-3 times a function of (v, th) (P5), so chi, the solution of (ell + 3/(2r)) d_s chi = (that harmonic)
vanishing at past null infinity, is r^-2 times a function of (v, th, s) (Lemma 9.7(d), q = 3): chi is in O_2, with no
remainder. It is smooth at the axes, as in section 5.1.

**Stage m >= 1.** Let the earlier stages be solved, in their classes. By the count, the source of (a) is S_m = r^-3
S_(m,3) + S~_m with S~_m in E_(7/2); the source of (c) without the unknowns is r^-3 K_(m,3) + E_(7/2); and q_m is in
L_3 (each of its terms pairs two of m_i, dphi_i as in (ii)). *Leading terms:* M_m := 2 int_{-oo}^{v} S_(m,3) dv',
which vanishes for v <= v_start; m^0 := r^-2 M_m; phi^0 := -(1/2) r^-1 M_m(ell, ell); gh^0 := the leading term of
Lemma 9.7(d) (q = 3) for the source r^-3 K_(m,3). Then -(1/2) box~ m^0 = r^-3 S_(m,3) + E_4 (Lemma 9.7(c), p = 2) and
ell phi^0 = (1/2) m^0(ell, ell), so the remainders (m~, phi~, gh~) := (m_m - m^0, phi_m - phi^0, gh_(m+1) - gh^0)
solve the system (a)-(c) with every source in E_(7/2) (the coefficients act on the leading terms through the classes
of the count, and ell phi~ = (1/2)(m~(ell, ell) + q_m) with q_m in E_3).

*Estimates.* For n large let P_n := P cap {tau >= tau_n}. Lemma 5.3, whose proof uses Lemmas 2.3 and 2.4 only, holds
on P_n with Lemmas 9.5 and 9.6 in their place, and gives the solution of the stage system on P_n whose data on
Sigma_tau_n are the leading terms; its remainders start at zero. Commute the system with d_X and Omega to an order J
(the classes are preserved), and let e(tau) be the energy of m~ to that order, f(tau) the norms of d_v phi~ and Omega
phi~, p(tau) that of Psi~ := box~ phi~, and z(tau) that of Z~ := d_th gh~ (zero mean, so ||gh~|| <= ||Z~||). The
L^2 norm of an E_q profile on A_P(tau) is at most C t^(3/2 - q), and Lemma 9.3(b) bounds m~ by e. Lemma 9.5 for (a),
Lemma 9.6 with c0 = 0 for d_v phi~ and Omega phi~ (L0 commutes with d_v and Omega), with c0 = 2 for Psi~ (the transport
of Lemma 3.4 with sigma~ := m~(ell, ell) + q_m in place of P s, box~ sigma~ taken from (a), so that no derivative is
lost), and with c0 = 3/2 for Z~ ((c), Lemma 5.2) give, with every integral over (tau_n, tau),

    e <= C int ( t^-2 e + t^(-3/2) z + t^-3 f + t^-2 ),         t^(-3/2) f <= C int t^(-3/2) ( e + t^(-3/2) ),
    t^(1/2) p <= C int t^(1/2) ( t^-1 e + t^-2 f + t^(-3/2) (z + p) + t^-2 ),
    z <= C int ( t^(-3/2) (z + e + p) + t^(-5/2) f + t^-2 ).                                                       (9.7)

The bad terms of the Psi~ forcing, r^-1 (d_tau + d_r) sigma~ and r^-2 d_r phi~, are the t^-1 e and t^-2 f. Every kernel
is integrable at -oo, and the sources give e, z <= A_e t^-1, f <= A_f and p <= A_p t^-1 uniformly in n, with the
constants taken in order: e and z are fed by f and p through kernels with an extra integrable power, so for t >= T0, T0
large, (9.7) returns their bounds with a factor 1/2; f and p are fed by e with kernels of size O(1) (f <= (2/3) C sup t
e, p <= 2 C (A_e + A_f + 1) t^-1), so A_f := C' A_e and A_p := C'' (A_e + A_f) close; and [1, T0] is a bounded interval
(Gronwall). As n -> oo the solutions converge: the difference of the n-th and the n'-th solves the homogeneous system on
P_n with data on Sigma_tau_n given by the n'-th remainders there, of sizes C t_n^-1 (e, z, p) and O(1) (f); (9.7)
without sources keeps e and z of size C t_n^-1, p of size C t^(-1/2) t_n^(-1/2), and f, transported with gam = -3/2, of
size C (t/t_n)^(3/2) <= C t^(3/2) t_n^(-3/2), so the difference tends to zero on every bounded part of P. The limit
solves the stage system on P with the same bounds, and a solution with nothing coming in is unique, since the difference
of two satisfies (9.7) without sources and tends to zero at -oo. *Classes:* Lemma 9.3(a) turns e <= C t^-1 into m~ in
E_(5/2); then sigma~ is in E_(5/2), phi~ = -(1/2) int_r^oo sigma~ dr' is in E_(3/2) with ell phi~ in E_(5/2), Psi~ is in
E_(5/2) by (9.5), the source of (c) is in E_(7/2), and gh~ is in O_(5/2) by Lemma 9.7(d). This is (9.6) at stage m.

**The residual, the phase, the continuation.** Section 5.4's argument gives Rm^(m) = 0 for m <= N - 1; the rest of
R_u[G] is lam^N times a sum of monomials of (0.2) with all factors known, each in E_3 by the count (the expansion of
g^-1 converges uniformly, |g_app - g0| <= C lam r^(-3/2)). Rewriting with the fixed phase v (Taylor's formula in lam
Psi about th + phi1, section 5.4) multiplies profiles by powers of phi_j, keeping every product in its class, and
costs lam^(N+1) in the metric and so lam^(N-1) in Ric^H: R_N in E_3, the scaled norm because d^i [f] costs lam^-i and
Omega costs nothing. (E1) holds (W_TT and chi dv dv are transverse to ell) and (E2) by stage 0. On Sigma_tau0
(Lemma 9.1(c)) the profiles' data determine, by Lemma 5.3 on Omega, solutions there; the two solve the same smooth
linear system and agree on Sigma_tau0 with all their tau-derivatives (each fixed by the system from the data), so
together they are smooth on P cup Omega. The stage system is equivariant under T^2 x Z2 x Z2 and under Lemma 8.2's S,
nothing coming in is invariant, and the solutions are unique: they are invariant. []

### 9.4 Theorem E_P, and the proof of Theorem P

Take the approximant of Theorem A_P of order N = K + 4 + ceil(4 beta0) (beta0 below) and put K' := N - 1, so that
F := -Ric^H(g_app) has |F|_(k,P) <= C_R lam^K' t^(-3/2). Put T := lam^-2 and let tau_T be the time with t = T; the
*far region* is P cap {tau <= tau_T} and the *near region* P cap {tau_T <= tau <= tau0}.

**The coefficients on P.** By Theorem A_P and section 3, on P+: B and C of (3.2) are in E_(3/2) (built from g_app and d
g_app, and d [lam g1] = dv [d_th g1] + lam [d g1]); G1 = [d_th g1] and G2 = [d_th^2 g1] are in E_(3/2), and the slow
derivative [ell d_th g1] is in E_(5/2) (g1's oscillating part W_TT(. + phi1) is in O_(3/2) up to L_(5/2)); g_app^-1 -
g0^-1 is in lam E_(3/2) and ell_app - ell in lam E_2; and T1 of Lemma 3.1 is in E_3: T1 collects the lam^1 terms of the
linearisation in the direction d_th G, namely d_th Rm^(1) = 0, -P_0(d_th g1) and -T(d_th g2), and the count of section
9.3 puts each in E_3 (for instance box~ (W_TT(. + phi1)) = box~ W_TT + 2 g0^-1(dphi1, d d_th W_TT) + (box~ phi1) d_th
W_TT + g0^-1(dphi1, dphi1) d_th^2 W_TT, each in E_(7/2), and (ell + 3/(2r)) annihilates W_TT and maps gh_2 into L_3). In
(3.5) and Lemma 3.2 the terms in phi therefore have these coefficients: E_(3/2) on ell phi = (1/2) P s and on Psi;
E_(5/2) on d_v phi (the slow coupling (d_v d_th g1)(d_r phi) of section 3.3 acts through ell phi, by (9.5)) and on the
angular derivatives r^-1 Omega phi (the angular block r^-2 <dring phi, dring d_th g1> of (9.5) is (r^-1 Omega phi) .
(r^-1 Omega d_th g1)); E_3 on phi and on lam d_x^2 phi. The same holds for the ell ell contraction of Lemma 3.3, in
which the d phi terms of B1 vanish since g1's oscillating part is transverse to ell and ell depends on xhat alone.

**Proposition 9.8 (the far region; deduced).** There are lam_F > 0 and M_F, independent of tau_n, such that for 0 <
lam <= lam_F and every tau_n < tau_T the solution g_n of Ric^H(g_n) = 0 on P cap {tau >= tau_n} with g_n = g_app and
d_tau g_n = d_tau g_app on Sigma_tau_n exists on P cap {tau_n <= tau <= tau_T}, equals g0 on {v <= v_start} there,
and w_n := g_n - g_app satisfies

    E(tau) := sum_{i + |beta| <= k} lam^i ||d^i Omega^beta d w_n|| <= M_F lam^K' t^(-1/2).                       (9.8)

*Proof.* Bootstrap E <= 2 M_F lam^K' t^(-1/2). Lemma 9.3 gives |w_n| <= C M_F lam^(K'-3) t^-2 and |d w_n| <= C M_F
lam^(K'-4) t^-2, so g_n has the margin of Lemma 9.1(f) (|g_app^-1 - g0^-1| <= C lam t^(-3/2)) and Lemma 9.2 gives
w_n = 0 on {v <= v_start}; |d g_n| <= C t^(-3/2). Apply lam^i d^i Omega^beta to P(w) = F + N(w) (section 3.2,
the equation for w without the decomposition) and Lemma 9.5 with k = C t^(-3/2): (i) the 1/lam term: lam^-1 |s G2|_k
<= C lam^-1 t^(-3/2) E, using Lemma 9.3(b) for the undifferentiated s and [lam d G2] in E_(3/2); (ii) B.dw and C.w
give C t^(-3/2) E; (iii) the commutators [lam^i d^i Omega^beta, g^{ab}] d_a d_b w are as in Step 4, with lam^i d^i
g_app in lam E_(3/2) for i >= 1; for the rotations, [Omega, box~] = 0 (P6), and Omega and [Omega, d_a d_b] (a
combination of second derivatives) act otherwise only through g^-1 - g0^-1, in lam E_(3/2) plus w; so they are at
most C t^(-3/2) E; (iv) the nonlinear terms are at most C lam^-5 t^(-3/2) E^2 (Step 4, with Lemma 9.3(a) in
place of Lemma 2.1); (v) |F|_k <= C_R lam^K' t^(-3/2). On the far region t >= T, so int lam^-1 t^(-3/2) <= 2 lam^-1
T^(-1/2) = 2: the 1/lam coupling is integrable to a constant. Gronwall: E(tau) <= C e^(6C) (2 C_R lam^K' + C M_F^2
lam^(2K'-5)) t^(-1/2), which is at most M_F lam^K' t^(-1/2) for M_F := 4 C e^(6C) C_R + 1 and lam small. Existence
and continuation are Step 8 on the bounded pieces P cap {tau_i <= tau <= tau_i + delta}, whose slices are compact
annuli of the kind used there. []

**Proposition 9.9 (the near region; deduced; repaired, D34).** There are beta0 >= 2 and lam_N > 0, M_N such that for 0
< lam <= lam_N the solutions of Proposition 9.8 continue to P cap {tau_T <= tau <= tau0} with w_n = h + phi [d_th g1]
(section 3.3, phi = 0 on Sigma_tau_T) and

    N_P(tau) <= M_N lam^K' t^(-1/2) (T/t)^beta0   on [tau_T, tau0].                                                (9.9a)

Here N_P is the quantity (4.1) with four changes: Omega^beta stands beside d^i in the h-part (i + |beta| <= k); the
parts in phi and Psi are commuted with Z in {lam d_tau, lam d_r, Omega}, which commute with L0 exactly, and the second
derivatives of phi are taken as lam (d_r^2 phi, r^-1 d_r Omega phi, r^-2 Omega^2 phi) (with d_tau = L0 + d_r and L0 phi
= -(1/2) P s these give every second derivative; at each order the norms are equivalent to the Cartesian ones, with
constants depending on k); the Psi-part is that of Psi' := Psi - (1/2) X_s (Lemma 9.4b); and the factor t^(-1/2) of
(9.9a) is t^(1/2) for the parts in phi. beta0 depends only on the constants C of (9.9) below at the orders j <= k,
which are built from the bounds of g0, g1, g2 (whose profiles do not depend on N: stage m of Theorem A_P is fixed by
the stages before it), from P and from Lemmas 9.3-9.6 and 9.4b; every term with a profile g_j, j >= 3, carries a factor
lam and is absorbed for lam <= lam_N. In particular N_P(tau0) <= M_N lam^(K' - 2 beta0).

*Proof.* Steps 1-7 of section 4 on [tau_T, tau], with these changes. Lemmas 9.3-9.6 replace Lemmas 2.1-2.4; the
mollifier is that of Lemma 9.4; the coefficients have the decay listed above; and the phi-quantities are transported
from Sigma_tau_T, where phi vanishes (h = w_n there); its Z-derivatives containing lam d_tau, and Psi', do not vanish
there, but with L0 phi = -(1/2) P s all are bounded by C' E(tau_T), so N_P(tau_T) <= C' E(tau_T) <= C' M_F lam^K'
T^(-1/2), and each line below carries this data term. Write H for the h-part of N_P, Q' for the Psi'-part, and D0, D1,
D2 for the parts ||phi||, the first derivatives (d_tau phi, d_r phi, r^-1 Omega phi) and the second derivatives of phi.
Since Psi = Psi' + (1/2) X_s and ||Z^j X_s|| <= C lam H (Lemma 9.4b), the Psi-part is at most Q' + C lam H. The
transport of Psi' follows from (3.6) and Lemma 9.4b:

    (L0 - 2/r) Psi' = -(1/2) P box~ s - (1/2) R_s + r^-1 X_s - r^-1 (d_tau + d_r) P s - 3 r^-2 d_r phi,       (9.9b)

in which the term (1/2) L0 X_s of -(1/2) [box~, P] s has been absorbed. With every integral over (tau_T, tau) (the
initial values at tau_T of Lemma 9.6 are those of N_P(tau_T) and are included in its first term):

- H <= C N_P(tau_T) + C int ( t^(-3/2) (H + Q') + t^(-5/2) D1 + t^-3 (D0 + D2) + lam^K' t^(-3/2) + R_nl ) (Step 4; the
  coefficients above; ell phi = (1/2) P s is bounded by H through Lemma 9.3(b));
- t^(-1/2) (D0 + D1) <= C T^(-1/2) N_P(tau_T) + C int t^(-1/2) H (Step 5: Lemma 9.6 with c0 = 0 for phi, d_tau phi and
  d_r phi and c0 = 1 for r^-1 Omega phi, with forcing -(1/2) Z^j of P s, d_tau P s, d_r P s and r^-1 Omega P s, the last
  bounded at top order by Bernstein in one r^-1 Omega; the c0 = 0 parts satisfy the stronger bound with t^(-3/2); ell
  phi is (1/2) P s itself);
- t^(1/2) D2 <= C T^(1/2) N_P(tau_T) + C int t^(1/2) H (the transports of lam d_r^2 phi, lam r^-1 d_r Omega phi and lam
  r^-2 Omega^2 phi have c0 = 0, 1, 2, so Lemma 9.6 applies with c0 <= 2; the forcing, lam times the same derivatives of
  P s, is bounded by Bernstein (M2) in one d_r or one r^-1 Omega);
- t^(1/2) Q' <= C T^(1/2) N_P(tau_T) + C int t^(1/2) ( t^-1 H + t^-2 D1 + t^(-3/2) (H + Q') + t^-3 (D0 + D2) + lam^K'
  t^(-3/2) + R_nl ) (Lemma 9.6 with c0 = 2 for (9.9b): Lemma 9.4b bounds R_s and r^-1 X_s by C (t^-1 + h') H <= C t^-1
  H, its R'_s terms rewritten through Lemma 3.3 as in Step 6; r^-1 (d_tau + d_r) P s and r^-2 d_r phi give t^-1 H and
  t^-2 D1; P box~ s is bounded through Lemma 3.3 with the coefficients above),                                   (9.9)

R_nl the nonlinear terms. Z commutes with L0, and [Z, r^-c] has the factor r^(-c-1), so every line holds at every order
j <= k with c0 unchanged. Bootstrap: H, Q' <= B t^(-1/2) (T/t)^beta and D0, D1, D2 <= B t^(1/2) (T/t)^beta, with B := 8
C C' (M_F + C_R + 1) lam^K' and C the sum of the constants of each line of (9.9). For beta > 1 and a > -beta, int_t^T
t'^(-1-a) (T/t')^beta dt' <= t^(-a) (T/t)^beta / (beta + a), and int_t^T t'^(-1) dt' = log(T/t) <= (T/t)^beta / beta.
Substituting the bootstrap bounds, each integral in (9.9) returns its bound times C/(beta - 1) at most: the t^-1 H and
t^-2 D1 terms of the Q'-line give C B (T/t)^beta / beta, which is the loss the split pays, and every other term carries
an extra integrable power. So for beta = beta0 := max(2, 4C + 1) the bounds are improved to B/2, provided the nonlinear
terms are small, which they are: every bootstrap quantity is at most B lam^(-2 beta0) t^(1/2) <= B lam^(-2 beta0 - 1),
so by Lemma 9.3(a) R_nl <= C lam^-5 t^(-3/2) (B lam^(-2 beta0 - 1))^2, and its contributions to (9.9) are at most C B^2
lam^(-8 - 4 beta0) (the log T of the Q'-line included), small against B because K' = K + 3 + ceil(4 beta0) > 8 + 4
beta0. The margin of Lemma 9.1(f) holds, by Lemma 9.3, as in Proposition 9.8. []

**Proof of Theorem P.** *The solution on P cup Omega.* At tau0, Data(w_n) <= C lam^-1 N_P(tau0) <= C M_N lam^(K' - 2
beta0 - 1) (the term ||d_x(phi G1)|| contains lam^-1 ||phi||), and K' - 2 beta0 - 1 >= K + 2. (E1)-(E3) hold on Omega
(Theorem A_P), so Theorem E with this K continues g_n to Omega with (0.5): (P-iv) for g_n. *The limit.* For n' > n,
delta := g_n - g_n' solves on P cap {tau >= tau_n} a linear system -(1/2) g_n^{ab} d_a d_b delta = f, |f| <= C(lam)
t^(-3/2) (|delta| + |d delta|), whose coefficient involves d^2 g_n' (at most C lam^-1 t^(-3/2)); Lemma 9.5 gives ||d
delta(tau)|| <= C(lam) ||d w_n'(tau_n)|| <= C(lam) M_F lam^K' t_n^(-1/2), and Lemma 2.3 continues the bound to Omega. So
g_n converges, with the bounds of Propositions 9.8 and 9.9 and (0.5), uniformly with k - 5 derivatives on compact sets.
The limit is smooth: for fixed lam the higher norms of g_n are bounded uniformly in n by the linear (tame) energy
estimates for the commuted equation, with constants depending on lam and the order, whose kernels are C(lam) t^(-3/2) on
the far region (integrable) and are taken over the bounded interval [tau_T, tau0] on the near region, with no
decomposition needed for fixed lam; the limit does not depend on the order used, by the uniqueness of (P-v). It solves
Ric^H(g_lam) = 0 on P cup Omega, equals g0 on {v <= v_start} (P-i), and by Lemma 9.3 and the bootstrap bounds satisfies
(P-iii), the factor (T/t)^beta0 <= lam^(-2 beta0) being absorbed by K' - 2 beta0 >= K. *The gauge.* D(g_lam) solves the
homogeneous linear system of section 0.7, whose coefficients are built from g_lam, d g_lam, d^2 g_lam and so are at most
C(lam) t^(-3/2) on P+. D(g_lam) = D(g_app) + O(|w| + |d w|), and D(g_app) = sum_{j >= 1} lam^j [D_j] with D_j in E_2:
its lam^0 part is (d_th g1)(ell, .) and the trace of d_th g1 against dv, which vanish by (E1) and tr W_TT = 0 (chi dv dv
is transverse and traceless too); the d_v-part of the slow divergence of W_TT is d_v (W_TT(ell, .)) = 0, the rest gains
a power; and every other term is a product, or a derivative of a stage-j profile of class E_2. So the energy of D(g_lam)
on A_P(tau) is at most C t^(-1/2) and tends to zero as tau -> -oo, and Lemma 9.5 (Gronwall with the integrable kernel
C(lam) t^(-3/2)) gives D(g_lam) = 0 on P; then D = d_tau D = 0 on Sigma_tau0, and section 0.7 gives D = 0 on Omega:
g_lam is vacuum. *The radiation field (P-ii).* g_lam - g0 - lam [W_TT] = w + lam [m1] + lam [chi dv dv] + lam ([W_TT(. +
phi1)] - [W_TT]) + sum_{j >= 2} lam^j [g_j]; |w| <= C lam^(K-3) t^-2, m1 and chi are in L_2, W_TT(. + phi1) - W_TT is in
L_1 L_(3/2), and every g_j (j >= 2) is in E_2 (means, oscillating profiles and the Taylor terms phi_i^p d_th^p W_TT of
section 5.4), so r^(3/2) times the sum tends to zero as r -> oo at fixed (v, xhat). *Uniqueness and symmetry (P-v).* For
a second solution g' with (P-i), |g' - g_app| + |d(g' - g_app)| <= eps_P t^(-3/2) and energy of g' - g_app tending to
zero, delta := g_lam - g' solves a linear system with coefficients at most C(lam) t^(-3/2) (they involve d^2 g_lam and d
g', both controlled), its energy tends to zero at -oo, and Lemma 9.5 gives delta = 0 on P; Step 8's uniqueness continues
this to Omega. The data at past null infinity, g_app and the equation are invariant under T^2 x Z2 x Z2, so g_lam is, by
this uniqueness. Finally, section 0.7's argument holds on Omega for g_lam, with Sigma_tau0's datum now the trace of
g_lam: N1* with the record's data at past null infinity. []

### 9.5 The flux at past null infinity, and what remains open

By (P-ii) the radiation field of g_lam at past null infinity is lam [W_TT] exactly, at every lam: its two polarizations
are the record's free data F, G, with no correction at any order. What that field carries is computed in P7. The flux
density (4/3)(P1_v^2 + P1_v P2_v + P2_v^2), the quadratic form whose phase mean is mu' (paper, Proposition 2.3), has
sphere mean exactly

    (2/9) A^2 [ env^2 + lam^2 env'^2 - (1/2)(env^2 - lam^2 env'^2) sin(2v/lam) + lam env env' cos(2v/lam) ],     (9.10)

and its integral in v from -oo is mu(v) - mu0 + (2/9) lam^2 A^2 int_{-oo}^{v} env'^2 + (2/9) A^2 ((lam/4) env^2
cos(2v/lam) + (lam^2/4) env env' sin(2v/lam)) + O(lam^3) (computed, P7; the last term is the integral of (2/9) A^2
(lam^2/4) (env'^2 - env env'') sin(2v/lam), O(lam^3) by one more integration by parts). So while the shell passes, the
integrated flux oscillates about mu(v) - mu0 with amplitude (lam/18) A^2 env^2, at twice the wave frequency; after it
(env = env' = 0) it exceeds mu(v_end) - mu0 by exactly (2/9) lam^2 A^2 int env'^2 + O(lam^3).

*What this does not prove.* The record's "mean mass" is the angular mean of the mass aspect at past null infinity. If
that mass changes at the rate of this flux, as a mass law at null infinity asserts, its angular mean is mu(v) + O(lam)
while the shell passes and mu + (2/9) lam^2 A^2 int env'^2 + O(lam^3) after it: the O(lam^2) rate, with its
coefficient. A mass law at past null infinity in five dimensions, and its application to g_lam, are not derived
here: Theorem P gives the radiation field exactly and the remainder pointwise as O(lam^(K-3) t^-2), which is of the
order of a mass term (r^-2) without an expansion of g_lam in powers of r^(-1/2) at past null infinity. That part
stays OPEN. Proposition 8.2 (the Hawking mass of the spheres S_(v,r)) holds on Omega and, by the same argument, on any
part of P with r bounded, with constants that grow with r; it is not a statement at past null infinity.

## 10. Late-time settling and the wavelength 10 l5: how far each goes (D33)

Neither item is proved here. This section records what was built for each on M's directions of 2026-10-20 (the copper
study for settling; the Navier-Stokes work for the wavelength) and exactly where each stops.

### 10.1 Settling, built on the copper study's barrier (`settle5.py` T1-T4; T5-T6 in 10.3)

After the shell, on Omega cap {v >= v_end}, g_lam is Tangherlini of the final mass plus lam m1 + O(lam^2) with its
first derivatives (Theorem E and section 5). Settling asks that the solution, continued outside D_T to late times,
converge to a member of the Tangherlini family.

*The class (computed, T1; deduced).* A co-closed T^2-invariant vector field on S^3 is b1(th) d_phi1 + b2(th) d_phi2
(its d_th coefficient would be C/(cos th sin th), not smooth at the axes), and it is odd under the reflections, as
are the linearised Myers-Perry rotations. So the class carries no vector-type perturbation and no linearised rotation:
only scalar-type and tensor-type perturbations, on the harmonics of even degree l = 2k that carry the record's waves
(seed_escape.py E3).

*Linear settling (READ, deduced).* [HKW18] (P.-K. Hung, J. Keller, M.-T. Wang, arXiv:1809.05144v1) prove, p. 4,
Theorem 2, for the gauge-invariant master quantities of every type on (2 + n)-dimensional Schwarzschild-Tangherlini,
"in spacetime dimension six and below, the uniform decay estimate E^N_Psi(Sigma_tau) <= C(n, M) I_Psi(Sigma_0)/tau^2",
and, p. 3, Theorem 1, that the l < 2 part is a pure gauge solution plus a linearised Myers-Perry solution. In the class
the latter is a linearised change of mass alone (T1). So, linearly, a perturbation of the final hole in the class
settles, in its gauge-invariant part, to a change of its mass, at the rate tau^-2 in energy. What [HKW18] leaves open
is stated there, p. 4: "the remaining linearized metric components can be controlled by the gauge-invariant master
quantities ... We do not treat this matter in the current paper". For the scalar wave on these backgrounds the same
rate is [Sch13] (V. Schlue, Anal. PDE 6 (2013), arXiv:1012.5963v1, p. 5, Theorem 1), "E[phi](Sigma_tau) <= C D /
tau^2", n >= 3.

*The ringdown, measured on the copper study's barrier (computed, T2-T4).* The tensor-type potential of [CLY03b] (V.
Cardoso, J. P. S. Lemos, S. Yoshida, arXiv:hep-th/0311260v2, (2.4) at n = 3) is exactly the barrier of
seed_escape.py E1 (T2). Evolving it in time from a pulse gives the fundamental l = 2 mode omega r_h = 1.513 - 0.353 i,
and the scalar-type l = 2 potential gives 0.948 - 0.257 i, both within 1% of [CLY03b]'s continued-fraction values
(Tables 3 and 1, pp. 8-9: 1.5106 + 0.3575 i and 0.9477 + 0.2561 i, time dependence e^(i omega t)) (T3). The least
damped mode of the class is the scalar-type l = 2 one, with e-folding time r_h/0.2561 = 3.905 r_h: 39.0, 54.5, 70.1
and 123.5 l5 at the copper study's seeds mu = 100, 195, 322 and 1000 l5^2 (T4).

*What stays open.* Nonlinear settling. The class depends on (t, r, th): its reduced problem is 2+1 dimensional, the
dimension of Klainerman and Szeftel's polarized axisymmetric stability of four-dimensional Schwarzschild ([HKW18],
p. 2: "Klainerman-Szeftel [20] for the Schwarzschild spacetime subject to polarized axisymmetric perturbations"); the
five-dimensional results READ ([Hol08], and Dafermos and Holzegel's triaxial Bianchi IX, cited in [Sch13], p. 2, as
"for work on the 5-dimensional case under symmetry see also [12, 23]") have the solution depend on (t, r) alone. A
five-dimensional counterpart in the T^2-mirror class would be needed, together with the decay of the metric components
in a gauge, and the solution would first have to be continued outside D_T. None of this is attempted.

### 10.2 The wavelength 10 l5, and the Navier-Stokes work (`paper/response5.py` R7; `growth5.py`, D38)

*What the recommended work does (READ).* The Navier-Stokes direction is read as Alpoge and Buckmaster's programme of
September 2026 (finite-time blowup with smooth forcing for incompressible porous media, Boussinesq and 3D Euler,
building on Cordoba and Martinez-Zoroa). In their Boussinesq paper the solution is built from "localized oscillatory
perturbations, which we call layers"; on fields of the local form "u (x,t) = D(t)x, theta (x,t) = G(t) . x" each
layer is an exact wave whose amplitudes solve ordinary differential equations ("no sinusoidal identity was used"), and
"Corrections outside the central region cancel oscillatory localization errors to successively higher orders". Their
frequencies are chosen, growing layer by layer. Chen and Hou's rigorous numerics is cited there ([4]) and is not part
of their proof. This corrects D31's reading, which took the recommended method to be computer-assisted.

*What it would change here (computed, R7; deduced).* Its building block is a wave that is exact on a background that
is linear over the wave's support, so its error is the background's departure from linearity, not its size. The
analogue here would replace the curvature length L = K^(-1/4) by the scale on which the curvature varies, r. At
lam = 10 l5 that ratio is lam/r = 1.00 and 0.32 at the horizon and 1.85 and 1.04 on x_K = 1 (mu = 100 and 1000
l5^2), against lam/L = 2.91, 0.92 and 10: smaller at the larger seed, small nowhere. And the method chooses its
wavelengths, while 10 l5 is prescribed.

*The go/no-go, measured (computed, `growth5.py` G0-G5; D38, D41, D43).* ROUTES-OPEN.md section 2 asks first for the
growth factor exp int K dv of the computed solution over D_T, non-rigorously, as what decides the a posteriori route.
growth5.py runs the record's own scheme (hf_mirror5.py's, on hf_core5's domain: seed 1, A = 1, the record's envelope
on [1/2, 7/2], the ingoing slices continued to the core boundary x_K = 1 on the seed, y = 1.361 at mu0 = 100 l5^2 and
1.815 at 1000 l5^2) at lam = 10 l5, that is lam/sqrt(mu0) = 1.000 and 0.3162, and records at every step K_v := max
|d_v P_i|, the radiation field's own rate, and K_all := the sup of the first derivatives (d_v, d_r, r^-1 d_th) of the
five dimensionless departures from Vaidya at the Isaacson mean mass (P1, P2, beta, r U, W - W_V) in the Bondi chart;
at every step the count of zeros of the round spheres' outgoing expansion per column (hf_mirror5.horizon) and W at the
core boundary, from which the breakdown is read off as the first v from which a second zero persists over 0.01 in v,
or W at the boundary is >= 0 (the scheme's premise, hf_core5 C3: one zero per column and the core boundary trapped,
so that the region outside it is fixed by the data outside it); and, from a second run with A -> A (1 + 10^-3) on the
same fixed step, the finite-difference amplification of the data's difference into the slices, a lower bound for the
linear propagator's norm.

At mu0 = 100 l5^2 (lam/r_h = 1.00; the wave's metric amplitude lam A r^-3/2 at the core boundary is 2.5, against the
regime boundary near 1.2 that hf_mirror5 X9 recorded) a second zero of the expansion first appears at v = 1.4516 (Ny =
20) and 1.4508 (Ny = 28) for a single step on either grid, returns on [1.4758, 1.4839] for 0.008 in v on both grids, and
holds over [1.500, 1.540] and [1.496, 1.545] -- the breakdown by the persistence criterion above, which gives 1.500 and
1.496 for a hold anywhere in (0.0082, 0.040] and 1.476 for a hold of 0.008 or less; the single step at 1.45 is the
figure an earlier text of this section and D38 quote, a transient the criterion excludes since a verifier read the data
(D44); after 1.54 the count returns to one on [1.548, 1.661] and [1.549, 1.717] and to two from 1.669 and 1.721, so the
second zero holds and lapses rather than stays (D45) -- and W at the core boundary turns positive (the boundary ceases
to be outflow, the causal premise) at v = 1.516 and 1.512, the mean mass aspect runs ahead of Vaidya's (1.136 against
1.011 at v = 1.5), and the slice solve fails at v = 1.69 and 1.75: before the shell's peak at v = 2. At mu0 = 1000 l5^2
(lam/r_h = 0.316; amplitude 1.9 at the boundary) the same sequence at Ny = 20, 24 and 28: the second zero from v =
1.5829, 1.5825 and 1.5825, W positive at the boundary at 1.680, the slice solve failing at 1.69-1.71. The breakdown time
agrees between the grids at both seeds, so it is the scheme's solution's and not the grid's. Up to it, int K_v dv = 0.65
and 0.75 (exp 1.9 and 2.1), int K_all dv = 2.8 and 12.3 (exp 17 and 2 x 10^5, the latter from d_r of W - W_V at the deep
core boundary), and the amplification is 1.28 and 1.00. The record's own regime, lam = 0.1 at mu0 = 100 l5^2, as
control: complete to v = 4.5 with one zero throughout, int K_v dv = 1.93 (exp 6.9), int K_all dv = 8.77 (exp 6 x 10^3,
from d_v of the oscillating part of W), amplification 1.71. A deeper excision does not help, and deeper is earlier: at
mu0 = 100 l5^2 and y = 1.6 (r = 0.39 r_h, inside x_K = 1 as the paper's own inner boundary r = a is) the second zero
stays from v = 1.410, W at that boundary turns positive at 1.455 and the slice solve fails at 1.556; at y = 2.0 (r =
0.25 r_h) the three come at 1.353, 1.362 and 1.370; at mu0 = 1000 l5^2 and y = 2.2 (r = 0.21 r_h, Ny = 16) at 1.524,
1.558 and 1.559, against 1.583, 1.680 and 1.69 at the standard excision (G5, single grids; int K_all to the break 5.4,
29 and 46, from d_r of W - W_V at the deep boundary). What the stored samples show at v = 1.5 at mu0 = 100 l5^2: in some
column the expansion has no zero at all, so by hf_core5's criterion no round sphere is trapped there; in the column
where the wave is strongest W > 0 for r >= 0.74 r_h and W < 0 on r = 0.54-0.66 r_h, and the zero of W in that column
moves inward with v (0.86-1.02 r_h at v = 1.0 and 1.25, 0.66-0.74 at 1.5, the boundary r = 0.54 at 1.516) while in other
columns W < 0 persists out to 1.26 r_h (Ny = 20; 1.22 at Ny = 28; the next grid point, 1.61, has W > 0 in every
stored sample); with the deeper excisions failing earlier, no excision depth keeps the premise.
Where the second zero sits and how it moves is not a measurement of these runs: `--run` stored q as its maximum and the
zeros only when every column had one (D45, OPEN; the run records every zero per column from D45 on). Two phrases carry
one meaning each here: a sphere *ceases to be trapped* when the expansion's second zero reaches it, and the boundary
*ceases to be outflow* when W there is >= 0 -- the second is the premise's causal clause, the first its one-zero clause.

*What it decides.* (i) No approximant on D_T at lam = 10 l5 comes from the record's own scheme, at either seed or any
excision: the scheme evolves ingoing null slices from a timelike excision that must stay trapped (outflow), and during
the passage the premise fails before the shell's peak: a column loses every zero of its expansion and the boundary
ceases to be outflow. Within the scheme's gauge and up to that time the computed solution stands, and what it shows is
that at 10 l5 round spheres inside the seed's horizon cease to be trapped, and the boundary to be outflow, in the
scheme's gauge while the shell passes -- a measurement on the scheme's solution, not a theorem, and a statement about
those spheres, not about the event horizon, which is teleological and beyond the run. An earlier text of this section
read the data as an inner marginally trapped surface moving outward and concluded that the exterior of the event horizon
is unaffected; the stored samples support neither (the zero of W moves inward, and the zeros of the expansion were not
stored per column), and both are withdrawn (D45). For the record's set-up, in which the core replaces vacuum inside x_K
= 1, what stands is that the region between x_K = 1 and the apparent horizon is then no longer fixed by the exterior
data alone. (ii) The question is re-posed, not closed: the natural formulation at 10 l5 is the characteristic initial
value problem in double-null gauge, with the incoming wave as data on an ingoing null hypersurface from past null
infinity and the seed's outgoing null cone from inside x_K = 1 as the other, whose domain of dependence needs no inner
boundary condition and no premise of trapping. There large data is no obstacle to local existence -- Luk's theorem, as
[Wu26] states it (Theorem 2.1): "there is a future open neighborhood of H_0 cup H_0-bar and metric (g, b, Omega) on it
solving the Einstein vacuum equations" with no smallness -- and [Wu26]'s Theorem 2.2 is the a posteriori structure the
route needs, "the difference of metrics is controlled by the difference of curvature residues" (p. 6), realised there as
a Picard iteration in double-null gauge with independent residual audits, in four dimensions; its five-dimensional
version in the class is a 2+1 problem, and is not built here. (iii) How small the residual must be: the sup-norm
Groenwall factor exp int K_all (17 and 2 x 10^5 at 10 l5, 6 x 10^3 in the control) is far above the amplification
measured along one direction of the data (1.28, 1.00 and 1.71), which is a lower bound for the propagator's norm and no
measure of it either; the radiation field's own exp int K_v is 2 to 7; and a certified argument would have to carry the
propagator's norm, as [MP11] do with their explicit constants, not a sup-norm bound. (iv) The control's figures are the
first measurement of these quantities in the record's own regime.

READ (alphaXiv, 2026-10-20). [Wu26] S. Wu, "Picard Iteration for the Characteristic Initial Value Problem in Einstein
Equations", arXiv:2609.08421v1: abstract ("an iteration algorithm for vacuum and Einstein scalar-field equations in
double-null gauge, which transform the non-linear PDE into systems of ODE"); p. 2, the metric (1.1) g = -2 Omega^2 (du
dv + dv du) + g_AB (dth^A - b^A du)(dth^B - b^B du); p. 6, Theorem 2.1 (Luk's local existence, quoted above) and
Theorem 2.2 with "the difference of metrics is controlled by the difference of curvature residues"; p. 26, a trapped
region and an apparent-horizon tube of eighteen MOTSs reconstructed on successive incoming null cones. [An12] X. An,
"Formation of Trapped Surfaces from Past Null Infinity", arXiv:1207.5271: the short-pulse existence result for
incoming radiation from past null infinity in four dimensions, the analytic counterpart of the large-data question
here; not used.

*What stays open.* Existence at 10 l5 on the domain of dependence of the record's data: a computed solution from the
characteristic formulation, with a certified residual and a certified linear estimate around it, closed by the
argument of Theorem E with the explicit constants in place of powers of lam (the method of Chen and Hou's "Rigorous
Numerics", arXiv:2305.05660, and [Wu26]'s Theorem 2.2); not attempted. What is computed at 10 l5 beyond the above is
the linear scattering of the shell off the seed (seed_escape.py E2-E4).

### 10.3 The linear milestone in the class: every metric component, in the Regge-Wheeler-type gauge (D39)

ROUTES-OPEN.md section 3 names the first milestone L1: linear stability of five-dimensional Tangherlini within the
class, with decay of every metric component in a gauge. [HKW18] prove the decay of the gauge-invariant master
quantities and leave the components to "a suitable choice of linearized gauge" (p. 4: "It is expected that, after
estimating the master quantities and making a suitable choice of linearized gauge, the remaining linearized metric
components can be controlled by the gauge-invariant master quantities ... We do not treat this matter in the current
paper"). In the class, the gauge and the control are already written down in [KI03] (H. Kodama and A. Ishibashi,
arXiv:hep-th/0305147v3, READ 2026-10-20), and the following is what they give. The computed companion is `settle5.py`
T5 and T6.

**Proposition 10.1 (deduced from READ).** Let h be a smooth solution of the linearised vacuum equations about
Tangherlini of mass mu_f on the domain of outer communication, T^2-invariant and even under both reflections, with
the data [HKW18] Theorem 2 requires on a slice Sigma_0 of their decay foliation. Then:

(i) *Decomposition.* h = h_0 + h_S + h_T: h_0 is the l = 0 scalar part, a change of mass plus a pure gauge solution; h_S
and h_T are the scalar- and tensor-type parts, h_S supported on the even harmonics l = 2, 4, ... (seed_escape.py E3) and
h_T on l >= 2 (whether only even l occur for the invariant tensor harmonics is not needed and not shown; (iv) and T5
cover every l >= 2); there is no vector-type part and no l = 1 part.

(ii) *The gauge.* For every scalar mode l >= 2 the gauge f_a = 0, H_T = 0 exists and is reached by the gauge vector
X_a = (r/k)(f_a + (r/k) D_a H_T), k^2 = l(l + 2), which is smooth wherever h is; in it the mode is
    h_S = F_ab S dy^a dy^b + 2 r^2 F gamma_ij S dz^i dz^j,
F and F_ab the gauge invariants of the mode. The tensor part needs no gauge: h_T = 2 r^2 H_T T_ij with H_T itself
gauge-invariant.

(iii) *Reconstruction.* With n = 3, m = l(l + 2) - 3 >= 5, x = mu_f/r^2, H = m + 6x, f = 1 - x and Phi~ := r^(3/2) H
Phi, Phi the master field of the mode,
    r F = (1/(12 r^2 H)) [ (2H - 3 r f') Phi~ + 6 r Dr . DPhi~ ],
    r F_ab + r F g_ab = (1/H) ( D_a D_b Phi~ - (1/2) (box Phi~) g_ab ),                                      (10.1)
D the covariant derivative of the orbit metric g_ab; and H_T = r^(-3/2) Phi for the tensor type. The coefficients 1/H <=
1/5, (2H - 3 r f')/(12 r^2 H) and 1/(2 r H) are bounded on r >= r_h uniformly in l, but Phi~ carries H = m + 6x, of
order l^2: in terms of Phi, (1/H) D_a D_b (r^(3/2) H Phi) = r^(3/2) D_a D_b Phi + lower-order terms with coefficients
bounded uniformly in l (H depends on r alone), so r F_ab costs two orbit-space derivatives of Phi and, through its trace
-2 r F (the bracket of (10.1) is traceless), the factor of r F, (2H - 3 r f') Phi~/(12 r^2 H) = (m + 3x) r^(-1/2) Phi/6,
which carries m = l(l + 2) - 3, two angular derivatives. (10.1) is covariant on the orbit space, so in any chart regular
at the horizon (ingoing Eddington-Finkelstein) every component of h_S and h_T is a combination of the master fields and
their derivatives to order two -- two orbit-space derivatives, and the factor m through F and the trace of F_ab -- with
coefficients bounded on r >= r_h uniformly in l (verifiers' findings, D44, D45).

(iv) *Decay.* [HKW18] Theorem 2 gives, in spacetime dimension five, E~^N_Psi(Sigma_tau) <= C(3, M) I_Psi(Sigma_0)/tau^2
for the master quantities of the scalar and tensor portions, the constant uniform in l (their (179)-(186): the estimates
"are uniform in the angular mode numbers" and are summed). With (10.1), the metric components of h_S + h_T in the gauge
of (ii), measured with two derivatives fewer -- two orbit-space derivatives for F_ab, two angular derivatives for F, the
factor m of (iii) -- decay at the same rate; and h_0 is delta mu_f K plus a pure-gauge part pi_X ((i), [HKW18] Theorem 1
in the class), which a separate l = 0 gauge condition removes (h_0 = c K). So in the Regge-Wheeler-type gauge of (ii)
for l >= 2, with h_0 = c K, every metric component of h settles to a change of the mass at the rate tau^-2 in energy,
with the loss of two derivatives counted as above.

*Proof.* (i) is `settle5.py` T1 for the absence of vector-type perturbations and of the linearised rotations (the
co-closed T^2-invariant vector fields on S^3 and the Myers-Perry rotations are odd under the reflections), together
with the parity of the invariant harmonics: a T^2-invariant scalar harmonic on S^3 is a function of theta alone,
hence a Gegenbauer polynomial in cos 2theta, of even degree (seed_escape.py E3); so l = 1 is absent, and [HKW18]
Theorem 1 ("delta g_(l<2) = pi_X + c K + sum d_m K_m", p. 3) reduces in the class to delta g_(l<2) = pi_X + c K, c the
mass shift, the d_m being the rotations. (ii) is [KI03] (2.7)-(2.8) and (2.4): with f_a = H_T = 0 the invariants are
F = H_L and F_ab = f_ab, and the gauge exists for k^2 (k^2 - 3) != 0, that is l >= 2 (p. 5); for l = 1 the authors
show there is no physical degree of freedom (p. 7), and l = 1 is absent here anyway. For the tensor type, [KI03] §5.1:
"H_T is gauge-invariant by itself". (iii) is [KI03] (3.13)-(3.14) at n = 3 with F~ = r F, F~_ab = r F_ab ((2.13)),
and (5.4), Phi = r^(3/2) H_T. The bounds: H = m + 6x with 0 < x <= 1 on r >= r_h, so 5 <= m <= H <= m + 6 and
1/H <= 1/5; 3 r f' = 6x <= 6; r^2 >= mu_f. (iv): [HKW18]'s scalar master quantity is Phi of (169), which is [KI03]'s
(3.1) with x = mu, carried on the tensor harmonic ((174), (179)); their energies E~^N_Psi are the N-th order red-shift
energies on the decay foliation, regular at the horizon ((115), (131)), and the T-derivatives in (10.1) are controlled
through the equation and the commutation with T that I_Psi already carries. []

*What this is.* The content of [HKW18]'s deferred sentence, in the class: a linear stability statement for every
metric component, in a named gauge, at their rate. It is the analogue of Hung-Keller-Wang's four-dimensional result
in the Regge-Wheeler gauge and of Johnson's in the generalized wave gauge, which [HKW18] cite on p. 4, and in the
class it costs nothing beyond (10.1), because the class has no vector part and no l = 1.

*What this is not.* It is not L1. The gauge of (ii) is defined mode by mode through the harmonic decomposition, not
by a hyperbolic condition, so it is not the wave-map gauge in which the nonlinear problem of section 2.5 is posed;
passing between the two is a pure-gauge solution whose decay is the zero-frequency analysis of the route ROUTES-OPEN.md
section 3 takes from [Hin26] (named there), and
[HKW18] record (p. 4) that in four dimensions Johnson needed "an intermediate passage through the wave-coordinate
gauge" for exactly this. It gives energy decay with a loss of two derivatives, pointwise decay only through Sobolev
embedding on the slices with more derivatives, and no sharp rate.

*The sharp rate, measured (computed, T6; READ).* The late-time tail of the l = 2 master fields of both types, measured
from the pulse's launch, is a power law with local exponent 7.05 (tensor; 7.03 at half the step) and 7.06 (scalar) on
tau in [550, 700] r_h, approaching 7 from above (7.41, 7.22, 7.12, 7.07 on the four earlier windows) with the origin at
the launch; shifting the origin by the launch radius, 15 r_h either way, moves the [550, 700] exponent to 6.89 and 7.23
and the earlier windows the other way, so the limit 7 is resolved and the direction of approach is not; the l = 4 tensor
field gives 11.5 on [150, 250]. This is the law of [CYDL03] (V. Cardoso, S. Yoshida, O. J. C. Dias and J. P. S. Lemos,
arXiv:hep-th/0307122v3, READ 2026-10-20) for odd dimension, Psi ~ t^-(2l+D-2) ((14), p. 4: 7 and 11 at D = 5; their own
D = 5 numerics 7.1 and 11.4, Fig. 2), and the tail is the flat five-dimensional Green's function's rather than the
hole's (p. 2, p. 4), so it is the rate a nonlinear iteration in the class would have to carry. No growing mode appears
for l = 2, ..., 10 in either type to tau = 275 r_h (T5: on the region r* in [-20, 50] r_h, which the computed slices
cover to that time, the field falls by at least five orders within 150 r_h of the launch and keeps falling to 275 -- a
finite-time observation, excluding growth rates above ln(10^5)/150 r_h = 0.08/r_h and not slower ones; the sign-reversed
potential, the control, grows).

*What stays open.* L1 in the wave-map gauge; the zero-energy structure of the gauge problem in spatial dimension four;
L2 and L3; and the nonlinear iteration. The solution would first have to be continued outside D_T.

### 10.4 The passage to the harmonic gauge in the class (`wavegauge5.py` W1-W7; D42, D46, D47)

L1 asks for linear stability in a generalised wave gauge, and Proposition 10.1 stopped at the Regge-Wheeler-type gauge.
In four dimensions the passage is Hung's even-part paper [Hun19] (P.-K. Hung, arXiv:1909.06733v1, READ 2026-10-20):
the harmonic gauge Gamma_b[h] := nabla^a (h_ab - (1/2) tr h g_ab) = 0, under which the linearised equation is the
Lichnerowicz wave equation (his (1.4)); a gauge vector W carrying h to the Regge-Wheeler gauge, determined
algebraically for l >= 2 ((4.11)-(4.13)) and solving the tensorial wave equation with the Zerilli quantity as source
((4.21)-(4.23)); and, at l = 0, two non-decaying solutions, the stationary one-form W* = dt/r + 2M dr/(r^2 f) ((8.1))
and the gauge-fixed mass change K* = K + pi_{W**} growing linearly in time ((8.38)-(8.39)), to which the spherically
symmetric part converges (Theorems 1.3-1.4), the rest decaying at tau^(-2+) (Theorems 1.1-1.2). Nothing of this exists
in five dimensions (the search of 2026-10-20 found [HKW18] alone, which stops at the master quantities). In the class
every explicit object of that structure is computed here; the decay estimates are not.

**Proposition 10.2 (computed, exact, `wavegauge5.py`; deduced).** On five-dimensional Tangherlini of mass mu, for
perturbations in the class:
(i) Under Gamma[h] = 0 the linearised vacuum equation is the Lichnerowicz equation box h_ab + 2 R_a^c_b^d h_cd = 0,
    and for a one-form X, Gamma[pi_X] = box X; so h_RW + pi_X is in harmonic gauge exactly when box X = -Gamma[h_RW]
    (W1).
(ii) The tensor type is in harmonic gauge as it stands: Gamma[h_T] = 0 for h_T = 2 r^2 H_T T_ij with T traceless and
    divergence-free (W5). For the tensor part, L1 is Proposition 10.1 itself.
(iii) For a scalar mode with harmonic S (k^2 = l(l + 2), l = 2, 4, ... even) the gauge vector is of scalar type,
    X = X_t S dt + X_r S dr + X_L r S_i dz^i, and box X = -Gamma[h_RW] is three 1+1 equations for (X_t, X_r, X_L) with
    coefficients in (r, mu, k) alone, principal part -f^-1 d_t^2 + f d_r^2, first-order couplings, and sources linear
    in F, F_ab and their first derivatives -- by (10.1), in the master field and its derivatives to order three (W4,
    checked at l = 2 and 4): the counterpart of [Hun19] (4.21)-(4.23).
(iv) The l = 0 sector. box W = 0 for W = W0(r) dt + W1(r) dr has W0 = a + b/r^2 and W1 = c/(r^3 f) + d r^3/(r^2 - mu),
    and the combination regular at the horizon with finite energy is
        W* = dt/r^2 + sqrt(mu) dr/(r^3 f) = dv/r^2 - dr/(r (r + sqrt mu))                                     (10.2)
    (W2). The mass change K := d g/d mu has Gamma[K] = dr/(r^3 f), and K* := K + pi_{W**} with W** = t W* + A dt +
    B dr, A = (log f + mu/r^2)/(2 sqrt mu), B = (3 mu^2 log(r^2 - mu) + 2 mu^2 + 3 mu r^2 - 2 r^4 log r + r^4
    log(r^2 - mu))/(8 mu r (r^2 - mu)), satisfies Gamma[K*] = 0 and K* = t pi_{W*} + (stationary) (W3): the
    counterparts of [Hun19] (8.1) and (8.39). These are the counterparts of Hung's two non-decaying solutions; if the
    five-dimensional analogue of his Theorems 1.3-1.4 holds -- the decay estimate this section leaves open -- a
    perturbation in the class settles in harmonic gauge to c1 K* + c2 pi_{W*}, the mass change growing linearly in t as
    in four dimensions (conditional, D45).

    (v) *The gauge-vector system is triangular (W6).* With S := div X, F := dX, P := F_tr/S_l, Q_t := -F_{t th}/S_l'
    and Q_r := -F_{r th}/S_l' (S_l the harmonic) and box_l := -f^-1 d_t^2 + f d_r^2 + ((3r^2 - mu)/r^3) d_r - k^2/r^2
    the scalar wave operator at mode l, seven identities hold in X, exactly (W6; at l = 2 in the selftest, at l = 4
    under --l4, where all seven pass and the control fails, in 72 minutes): div(box X) = box_l(div X);
    (box X)_t = box_l X_t + (2 mu/r^3) P; (box X)_r = d_r S - f^-1 d_t P - (k^2/r^2) Q_r; r (box X)_L = box_l(r X_L) -
    (2 k f/r) Q_r; (box X)_t = d_t S - (f/r^3) d_r(r^3 P) - (k^2/r^2) Q_t; d(box X)_tr = box_l P - ((3 r^2 - 9 mu)/r^4)
    P - (2 k^2/r^3) Q_t; and, the last two combined, box_l(r P) + (4 mu/r^4) r P = r d(box X)_tr + 2 (d_t S - (box
    X)_t). So for box X = J the system is triangular: S solves the free scalar wave equation with source div J; r P
    solves the scalar wave equation with the potential -4 mu/r^4 and a source in S and J (the Maxwell master equation of
    [KI03b] (5.20) at n = 3, A = -r^3 P/k^2, in another normalisation); X_t solves box_l X_t = J_t - (2 mu/r^3) P with
    no potential; r X_L solves the scalar wave equation with source (2 k f/r) Q_r + r J_L, Q_r = (r^2/k^2)(d_r S - f^-1
    d_t P - J_r) algebraic in the rungs below; and X_r = Q_r - d_r(r X_L)/k is algebraic. Hung's condition (A.3),
    k^2/r^2 + V >= 0, holds on every rung: V = 0 for S, X_t and r X_L, and V = -4 mu/r^4 for r P gives k^2/r^2 - 4
    mu/r^4 >= 0 for r^2 >= 4 mu/k^2, true on the exterior for k^2 >= 8 (equality would need r^2 = mu/2). The counterpart
    of [Hun19] (4.21) carries no potential where four dimensions has 2M/r^3.
(vi) *Hung's Proposition 4.2 in five dimensions (W7).* In Hung's components -- H1 = (h_tt + f^2 h_rr)/2 + ((1 - f)/2) trs
    h, H2 = trs h/sqrt3, H3 = (h_tt/f - f h_rr)/2, H6 = f h_tr + ((1 - f)/2) trs h, H4 = f k h_rth/(r S'), H7 = k
    h_tth/(r S'), hhat_ij = 2 r^2 H5 S_ij, with trs h = r^-2 gamma^ij h_ij and (1 - f)/2 = mu/(2 r^2), which in four
    dimensions is his M/r -- and under Gamma[h] = 0, admixed as 2 f f' Gamma_r in rows 1 and 6 and k f' Gamma_th/r in
    rows 4 and 7, the Lichnerowicz equation reads boxhat H = A H + U H, boxhat := -f^-1 d_t^2 + f d_r^2 + ((3 r^2 -
    mu)/r^3) d_r the wave operator of the quotient ((v)'s box_l without its -k^2/r^2, so that A carries the angular
    eigenvalues K/r^2 of (10.4) on its diagonal and is otherwise of degree at most one in k, W8f, g): A zeroth order and
    rational in r, mu, k, and U = (2f'/f) nabla_L (H6 - H1) in row 6, (f'/f) nabla_L (H7 - H4) in row 7, nothing else, L
    = d_t + f d_r (Hung's U, p. 19, with 2M/r^2 -> f' = 2 mu/r^3). The leading part A_main := lim r^2 A at k^2 = l(l + 2)
    has the eigenvalues (l + a)(l + a + 2), a = -2, -1, 0, 0, 0, 1, 2 -- Hung's Lemma 4.3 with (l + a)(l + a + 1)
    replaced -- so its quadratic form is semi-positive for every l >= 2, with one zero at l = 2 and comparable to the
    angular term for l >= 4, and A - A_main/r^2 = O(mu/r^4). In the horizon-regular variables H6' := (H6 - H1)/f^2 =
    -h(L', L')/2 and H7' := (H7 - H4)/f = k h(L', d_th)/(r S'), L' = f^-1 (d_t - f d_r) the future-directed transversal
    null direction, every coefficient is regular at r = sqrt mu, rows 1-5 carry no first-order term, and rows 6', 7'
    carry 2 f' nabla_L' H6' and f' nabla_L' H7' with no nabla_L: Hung's 4M/r^2 and 2M/r^2 (p. 23), positive, so the red-
    shift step of his Proposition 4.1 applies as written. The l = 0 sector (H1, H2, H3, H6) has the same form, r^2 A_main
    with eigenvalues 0, 0, 3, 8. Without the gauge admixture the Lichnerowicz operator alone carries, in the null frame,
    -f' times the boost weight as the nabla_L' coefficient of each component (-2f' on h(L, L), -f' on h(L, d_th), 0 on
    h(L, L') and the angular part, +f' and +2f' on h(L', d_th) and h(L', L')); the gauge condition removes the negative
    ones, which is what Hung's Appendix C does in four dimensions (`hung4.py`, the control, reproduces his printed rows
    from the Schwarzschild metric the same way).

*Proof.* Each item is a sympy identity on the metric -f dt^2 + dr^2/f + r^2 (dth^2 + cos^2 th dphi1^2 + sin^2 th
dphi2^2), f = 1 - mu/r^2, with the class's eight components as functions of (t, r, th): (i) is the linearised Ricci
tensor against the Lichnerowicz operator and the symmetrised gradient of Gamma, and Gamma[pi_X] against box X; (ii)
is Gamma of 2 r^2 H T_ij with T = diag(a, cos^2 th b, sin^2 th c), a + b + c = 0, reduced by the divergence condition
D^i T_ij = 0 solved for a'; (iii) divides box X + Gamma[h_RW] by S (t, r components) and by r S_i (angular) and checks
the quotients are th-free and have the stated second-order coefficients; (iv) solves the two decoupled radial ODEs,
tests regularity in the ingoing chart, and verifies Gamma[K*] = 0 by direct computation after B is found by variation
of parameters from the two homogeneous solutions 1/(r^3 f) and r^3/(r^2 - mu). The controls: the curvature term's sign
reversed, dt/r^2 alone (singular at the horizon), W** without its t W* term, a vector-type angular part, and T without
the divergence condition, each fail. (v) is W6, section 10.4's seven identities with every coefficient evaluated at the
three sample points to forty digits. (vi) is W7: the Lichnerowicz components and the gauge one-form on the ansatz in
Hung's components, the harmonic kept symbolic with its equation S'' = -2 cot 2th S' - k^2 S applied and the angle
evaluated exactly at two Pythagorean points, every coefficient a rational function cancelled exactly, the leading
matrix's characteristic polynomial factored over Q[l]; the control reverses the sign of the gauge admixture, and
first-order terms survive in rows 1-5. []

*What L1 still needs, and nothing else.* Decay for the system (iii) with (10.1)'s source and for its l = 0 part: the
five-dimensional version of [Hun19]'s sections 5-8 (the vector field method on the three coupled equations and the
red-shift argument for the coefficient of the singular stationary solution), which rests on the decay of the homogeneous
vector wave equation on Tangherlini -- not in the literature. ROUTES-OPEN.md section 4 proposes the route (D46): by (vi)
the system is triangular and every rung is a scalar wave equation on Tangherlini with a potential satisfying Hung's
condition (A.3), so the estimate is Schlue's scalar estimates and Hung's Appendix A in five dimensions, rung by rung,
with the l = 0 argument of [Hun19] section 8 on W2's ODE; and on (vi) Hung's Proposition 4.1 -- the red-shift and r^p
estimates for h itself, with the compact region as the error -- is deduced in five dimensions in 10.5 (Proposition
10.3, D48), so that what remains is the compact region, which the master quantities and the gauge vector govern. With
it, every metric component in the class would decay in a gauge in which the nonlinear problem can be posed, and the
final state would be read off (iv). The scalar tails of T6 (t^-7 at l = 2) bound the rate such an estimate could reach.

### 10.5 Hung's Proposition 4.1 in five dimensions (`wavegauge5.py` W8; D48)

The first estimate of this section. [Hun19]'s Proposition 4.1 (p. 18, (4.1)) is the energy inequality for h itself in
the harmonic gauge: the r^p and red-shift estimates of Dafermos and Rodnianski applied to the seven components of his
Proposition 4.2, with the compact region between the two as the only error term. Its five-dimensional form is deduced
here on the structure of Proposition 10.2(vi), from identities W8 computes; constants are not tracked, and every
inequality is Cauchy-Schwarz, a choice of a constant, or the divergence theorem. It is not a decay statement -- it is
consistent with the growing K* of (iv) -- and what it leaves to the compact region is said at the end.

*Setting.* Five-dimensional Tangherlini, f = 1 - mu/r^2, r_h = sqrt mu, s := r/sqrt mu (Hung's r/M), the tortoise
coordinate dr_*/dr = 1/f, the ingoing chart (v, R) := (t + r_*, r) in which g = -f dv^2 + 2 dv dR + r^2 gamma_{S^3} is
smooth across r = r_h ([Hun19] (2.1) with the five-dimensional f). T := d_t, L := d_t + f d_r, L-bar := d_t - f d_r,
L' := f^-1 L-bar = -d_R, the future-directed transversal null direction, regular at the horizon. The foliation is
[Hun19] section 2.2 with (2M, 9M/4, 5M/2, M) read as (r_h, 9 r_h/8, 5 r_h/4, r_h), and R_null >= 10 r_h (his 10M is 5
    r_h; the larger value only helps);
Sigma_tau := {t + r_* - g(r) = tau}, spacelike in [r_h, R_null] and null, with n = L, in r >= R_null, meeting H^+
transversally; Sigma''_tau := Sigma_tau cap {r <= R_null}, Sigma'_tau := Sigma_tau cap {r >= R_null}; D(tau_1, tau_2)
the region between two leaves, H^+(tau_1, tau_2) and I^+(tau_1, tau_2) its boundaries at the horizon and at null
infinity; dvol = r^3 dt dr domega and dvol_3 the induced form of the leaf (-n^flat wedge dvol_3 = dvol; on Sigma' it is
    r^3 dv domega / 2 in the ingoing chart's v, and dvol = f dtau wedge dvol_3). The cut-offs: eta_null(r) := phi((r -
        R_null)/r_h) with phi = 0 on
(-oo, 0] and 1 on [1, oo), so d eta_null is supported in [R_null, R_null + r_h], and Phi-tilde := eta_null Phi;
eta_rs := 1 on [r_h, 9 r_h/8] and 0 on [5 r_h/4, oo); and the red-shift vector field
    Y(sigma) := eta_rs ((sigma/2)(r - r_h) T + (2 + sigma (r - r_h)) L'),                                         (10.3)
causal on the exterior and equal to 2 L' at r = r_h ([Hun19] (2.6)-(2.7)). The divergence theorem on D(tau_1, tau_2)
for a one-form J is [Hun19] (2.14): int_{Sigma_tau_1} J.n = int_{Sigma_tau_2} J.n + int_{H^+} J.L + int_{I^+} J.L-bar +
int_D div J, the fluxes at H^+ and I^+ taken with the normals L and L-bar, the second as the limit of the flux through v
= v_0 -- so a current whose fluxes through H^+ and through every v = v_0 are non-negative gives int_{Sigma_tau_2} J.n +
int_D div J <= int_{Sigma_tau_1} J.n with no decay at I^+ assumed beyond the finiteness of the norms. Every current
below is of that kind.

*Components and norms.* H = (H1, ..., H7) are Hung's components (Proposition 10.2(vi)), H' := (H1, ..., H5, H6', H7')
the horizon-regular ones, Hhat := D_m H with D_m := diag(sqrt2, 1, sqrt2, sqrt2, 2 n_S, sqrt2, sqrt2), n_S :=
sqrt(2 (k^2 - 3)/(3 k^2)) in [sqrt(5/12), sqrt(2/3)] for l >= 2, the rescaling in which V_inf below is symmetric;
Hhat' := D_m H'. H and H' are related by H6 = H1 + f^2 H6', H7 = H4 + f H7', so on r >= 5 r_h/4, where f >= 9/25, every
norm below of H, H', Hhat and Hhat' is equivalent to every other with constants independent of l; at the horizon only
H' and Hhat' are the right variables. At a scalar mode (k^2 = l(l + 2), l even) a vector Phi of functions of (t, r) has
the angular energy
    |nabla-slash Phi|^2 := r^-2 Phi . K . Phi,   K := diag(k^2, k^2, k^2, k^2 - 2, k^2 - 6, k^2, k^2 - 2),       (10.4)
(W8f: the rough Laplacian of S^3 on S, on the one-form S_th dth and on the traceless tensor S_AB has the eigenvalues
-k^2, -(k^2 - 2), -(k^2 - 6)), so that (k^2/4)|Phi|^2 <= Phi . K . Phi for l >= 2; and its radiation field Phi^(0) :=
s^(3/2) Phi (Hung's s Phi; [Sch13] (5.11) at n = 4). With |d Phi|^2 := |nabla_T Phi|^2 + |nabla-slash Phi|^2 +
|nabla_L' Phi|^2 (Hung's set partial = {T, Omega/r, L'}, (2.8)) and |(sqrt mu d)^{<= 1} Phi|^2 := |Phi|^2 +
mu |d Phi|^2, the norms are [Hun19] (2.15), (2.18)-(2.21) with M^-2 read as mu^-1 and the radial weight lowered by one
for the measure r^3 dr:
    F[Phi](tau) := int_{Sigma''_tau} (|d Phi|^2 + mu^-1 s^-2 |Phi|^2) dvol_3
                   + int_{Sigma'_tau} (|nabla_L Phi|^2 + |nabla-slash Phi|^2 + mu^-1 s^-2 |Phi|^2) dvol_3,
    B-bar[Phi](tau) := int_{Sigma_tau} s^-2 (|d Phi|^2 + mu^-1 s^-2 |Phi|^2) dvol_3,
    E^{p,(0)}_L[Phi](tau) := int_{Sigma'_tau} s^(p-3) |nabla_L Phi^(0)|^2 dvol_3,
    E^{p,(0)}_ang[Phi](tau) := int_{Sigma'_tau} s^(p-3) |nabla-slash Phi^(0)|^2 dvol_3,
    E^{p,(0)}_{L,ang} := E^{p,(0)}_L + E^{p,(0)}_ang,
each summed over the modes. So int_{Sigma'} s^(p-3) |nabla_L Phi^(0)|^2 dvol_3 = mu^2 int s^p |nabla_L Phi^(0)|^2 ds
domega, the one-dimensional content of Hung's (2.19), and F and E^p have the dimension of mu, as his have that of M.

**Proposition 10.3 (deduced from W7, W8 and [Hun19] section 4.1; constants not tracked).** Let h be a scalar-type
solution in the class of the harmonic-gauge Lichnerowicz equation (Proposition 10.2(i)) on the exterior of
five-dimensional Tangherlini, smooth up to H^+, supported on the modes l >= 2. There are R_H >= 10 r_h, depending on
delta, and r_rs,H in (r_h, 5 r_h/4) such that for R_null >= R_H, every p in [delta, 2 - delta] and tau_2 >= tau_1,
    F[H'](tau_2) + E^{p,(0)}_L[H-tilde](tau_2)
      + mu^-1/2 int_{tau_1}^{tau_2} (B-bar[H'] + E^{p-1,(0)}_{L,ang}[H-tilde]) dtau
      <~ F[H'](tau_1) + E^{p,(0)}_L[H-tilde](tau_1)
         + mu^-3/2 int_{D(tau_1, tau_2) cap {r_rs,H <= r <= R_null + r_h}} |(sqrt mu d)^{<= 1} H'|^2 dvol,         (10.5)
the constant depending on R_null and delta, whenever the right side is finite: the energy of h in the harmonic gauge
is controlled, at every later time and in the spacetime bulk, by its initial value and by h on the compact region
[r_rs,H, R_null + r_h], where the master quantities and the gauge vector of Propositions 10.1 and 10.2 speak for it.
It is [Hun19] (4.1) with M^-1, M^-3 read as mu^-1/2, mu^-3/2.

*What is computed (W8, exact, sympy; the three divergence identities formally, on two components with the matrices
symbolic, the structure being the same at seven).* On the system boxhat H = A H + U H of Proposition 10.2(vi):
 (W8a) the radiation field Psi := s^(3/2) Hhat satisfies, with d_u d_v := d_t^2 - f d_r (f d_r), the mixed derivative in
     u, v := (t -+ r_*)/2 (not the ingoing chart's v),
          d_u d_v Psi = -f V Psi - f Uhat Psi,   V := Ahat + V0 I,   V0 := (3/4 + 9 mu/(4 r^2))/r^2,              (10.6)
       Ahat := D_m A D_m^-1 and Uhat the first-order term in these variables -- [Sch13] (5.11)-(5.12) at n = 4,
       component by component, the matrix in place of the angular eigenvalue;
 (W8b) V_inf := lim r^2 V is symmetric with the eigenvalues (l + a + 1/2)(l + a + 3/2), a = -2, -1, 0, 0, 0, 1, 2, at
       k^2 = l(l + 2): V_inf >= (3/4) I and V_inf >= (3/32) l(l + 2) I >= (3/32) K at every l >= 2 -- where Hung's
       A_main + B_main + O has the zero eigenvalue (l - 1)(l - 2) at l = 2 and he needs his Corollary 3.3 -- and
       V - V_inf/r^2 = O(mu/r^4);
 (W8c) Uhat Psi = (2f'/f) nabla_L (Psi_6 - Psi_1) - (3f'/r)(Psi_6 - Psi_1) in row 6, (f'/f) nabla_L (Psi_7 - Psi_4) -
       (3f'/(2r))(Psi_7 - Psi_4) in row 7, nothing else, f' = 2 mu/r^3: |Uhat Psi| <= 9 mu r^-3 f^-1 |nabla_L Psi| +
       13 mu r^-4 |Psi| (the two rows added, each by Cauchy-Schwarz);
 (W8d) for J^p_a := s^(p-3) f^-1 (T^o_ab[Psi] L^b - (1/(2 r^2)) Psi . V_inf . Psi L_a), T^o_ab[Psi] := nabla_a Psi .
       nabla_b Psi - (1/2) g_ab nabla^c Psi . nabla_c Psi on the quotient (a, b in {t, r}), the divergence taken with the
       measure r^3,
          div J^p = mu^-1/2 s^(p-4) f^-2 (p f/2 - s^-2) |nabla_L Psi|^2 + ((2 - p)/2) mu^-3/2 s^(p-6) Psi . V_inf . Psi
                    + s^(p-3) f^-1 nabla_L Psi . ((V - V_inf/r^2) Psi + Uhat Psi),                                (10.7)
       J^p . L-bar = mu^-1 s^(p-5) Psi . V_inf . Psi >= 0 (the flux at I^+) and J^p . L = s^(p-3) f^-1 |nabla_L Psi|^2
       (the flux through Sigma'): [Hun19] (4.5) and the two lines before it, the powers of s lowered by one (the check
       runs with r^(p-3) for s^(p-3), a constant factor);
 (W8e) for J_delta,a := s^-delta (T^o_ab[Q] - (1/(2 r^2)) Q . V_inf . Q g_ab) T^b and a solution of boxhat Q = V Q + U Q,
          div J_delta = (delta/4) mu^-1/2 s^(-1-delta) (|nabla_L-bar Q|^2 - |nabla_L Q|^2)
                        + s^-delta nabla_T Q . ((V - V_inf/r^2) Q + U Q),
                          (10.8)
       [Hun19] (4.6) and p. 23; the identity is polynomial in delta and holds for any constant symmetric matrix in the
       place of V_inf, so at delta = 0 with K it is the T-current's, div((T^o_ab[Q] - (1/(2 r^2)) Q . K . Q g_ab) T^b)
       = nabla_T Q . ((V - K/r^2) Q + U Q);
 (W8f) the angular eigenvalues (10.4);
 (W8g) A - K/r^2, its horizon-regular form A' - K/r^2 (the matrix of Proposition 10.2(vi)'s regular variables) and the
       sub-leading part A - A_main/r^2 have entries of degree at most one in k, and A' - K/r^2 is finite at r = r_h;
       so
       (the entries being rational, homogeneous of degree -2 in (r, sqrt mu) and without pole on the closed exterior,
       hence bounded by C r^-2 and C k r^-2, and k |Phi| <= 2 r |nabla-slash Phi| by (10.4)), at every mode l >= 2
          |(A' - K/r^2) Phi| <= C (r^-1 |nabla-slash Phi| + r^-2 |Phi|)        on [r_h, oo),
          |(A - A_main/r^2) Phi| <= C mu r^-4 (r |nabla-slash Phi| + |Phi|)    on [10 r_h, oo),                   (10.9)
       with C independent of l, and at l = 0 the same decay O(mu/r^4) of the sub-leading part;
 (W8h) at r = r_h, in the ingoing chart, for a vector Q of functions of (v, R) solving boxhat Q - (K/r^2) Q = Acal Q +
       beta L' Q with beta diagonal, for c > 0 and Y = Y(sigma) of (10.3), with T_ab[Q] := T^o_ab[Q] - (1/(2 r^2)) g_ab
       Q . K . Q the energy-momentum tensor of the components,
          div(T_ab[Q] Y^b - (c/r^2) |Q|^2 Y_a)|_{r = r_h} = (sigma/2)|Q_v|^2 + (2/r_h)|Q_R|^2 + (6/r_h) Q_R . Q_v
                + (sigma/2 + 1/r_h)|nabla-slash Q|^2 + c (sigma/mu + 2/mu^(3/2))|Q|^2 + (2c/mu) Q . Q_R
                + nabla_Y Q . (Acal Q - (c/r^2) Q) + 2 Q_R . beta Q_R,                                            (10.10)
       Q_v := d_v Q, Q_R := d_R Q = -nabla_L' Q: [Hun19] (2.13) with 2M -> r_h, his 1/(2M) and 2/M becoming 2/r_h and
           6/r_h. The same current in four dimensions (hung4.py C3) has c sigma/(4M^2)|Q|^2 and (c/(2M^2)) Q . Q_R
               beside nabla_Y Q . (-(c/r^2) Q) -- the c sigma/mu |Q|^2 and (2c/mu) Q . Q_R here, with r_h = 2M -- where
                   his print has c sigma/(8M^2) and no Q . Q_R term, a normalisation of c the argument does not depend
                       on, c being free; the terms new in five dimensions are (1/r_h)|nabla-slash Q|^2 and
                           (2c/mu^(3/2))|Q|^2; and the beta term, which in the system is 2 Q_R . diag(0, 0, 0, 0, 0,
                               2f', f') Q_R >= 0 (Proposition 10.2(vi)), has the sign Hung's argument needs.
The control reverses the sign of V0 and takes L-bar for L in J^p: (10.6), the spectrum and (10.7) fail.

*Proof.* Three estimates, as [Hun19] Lemma 4.4, (4.8) and (4.9), then their sum. Everything is at a fixed mode and summed
over the modes last; every constant is uniform in l by (W8b) and (W8g).

*Step 1 (the far region; [Hun19] Lemma 4.4).* Let Psi := s^(3/2) eta_null Hhat, the radiation field of H-tilde. By
(10.6), d_u d_v Psi = -f V Psi - f Uhat Psi - f G_eta, where G_eta collects Uhat's action on eta_null and the terms in
d eta_null, d^2 eta_null: supported in [R_null, R_null + r_h], with |G_eta|^2 <~_{R_null} mu^-2 |(sqrt mu d)^{<= 1} H|^2
    there. Apply the divergence theorem to J^p of (W8d) built on this Psi; its divergence is (10.7) with G_eta added to
Uhat Psi. The fluxes: through Sigma'_tau the current gives E^{p,(0)}_L[H-tilde](tau) up to the factor f in [99/100, 1];
on Sigma'' and H^+ it vanishes (Psi does); at every v = v_0 it is non-negative (W8d). The bulk, for p in [delta, 2 -
delta] and s >= s_H := max(10, (8/delta)^(1/2)): the first term of (10.7) is at least (p/4) mu^-1/2 s^(p-4) |nabla_L
Psi|^2 (there p f/2 - s^-2 >= p/4 and f^-2 >= 1); the second, by (W8b) with its two bounds averaged, is at least
    (2 - p) mu^-3/2 s^(p-6) ((3/16)|Psi|^2 + (3/128) Psi . K . Psi)
      >= (3 delta/16) mu^-3/2 s^(p-6) |Psi|^2 + (3 delta/128) mu^-1/2 s^(p-4) |nabla-slash Psi|^2,
the zeroth-order and angular bulk that Hung obtains at l = 2 only through his Corollary 3.3 (a Hardy inequality); in
five dimensions V_inf >= (3/4) I gives them outright, and no Hardy inequality enters the proof. The cross terms, by
Cauchy-Schwarz with epsilon and then R_H: by (10.9) and D_m bounded,
    s^(p-3) f^-1 |nabla_L Psi| |(V - V_inf/r^2) Psi|
      <= epsilon mu^-1/2 s^(p-4) |nabla_L Psi|^2 + C epsilon^-1 mu^-1/2 s^(p-8) (|nabla-slash Psi|^2 + mu^-1 s^-2
        |Psi|^2),
the second term absorbed by the bulk above once s^4 >= C' epsilon^-1 delta^-1; by (W8c),
    s^(p-3) f^-1 |nabla_L Psi| |Uhat Psi|
      <= 16 mu^-1/2 s^(p-6) f^-2 |nabla_L Psi|^2 + 7 mu^-3/2 s^(p-8) f^-1 |Psi|^2,
absorbed once s^2 >= C'' delta^-1; and the G_eta term is at most epsilon mu^-1/2 s^(p-4) |nabla_L Psi|^2 + C(R_null)
mu^-3/2 |(sqrt mu d)^{<= 1} H|^2 chi_{[R_null, R_null + r_h]}. With epsilon = p/16 and R_H the largest of the thresholds
(depending on delta alone), the divergence theorem gives
    E^{p,(0)}_L[H-tilde](tau_2) + mu^-1/2 int_{tau_1}^{tau_2} (E^{p-1,(0)}_{L,ang}[H-tilde]
      + mu^-1 int_{Sigma'_tau} s^(p-6) |H-tilde^(0)|^2 dvol_3) dtau
      <~ E^{p,(0)}_L[H-tilde](tau_1) + mu^-3/2 int_{D cap {R_null <= r <= R_null + r_h}} |(sqrt mu d)^{<= 1} H|^2 dvol,
                                                                                                                 (10.11)
dvol = f dtau dvol_3 on D' reading the bulk as an integral in tau. For the ingoing derivative add epsilon_1 J_delta of
(W8e) built on Q := eta_null Hhat, whose equation carries the same cut-off terms: its fluxes through Sigma_tau, H^+ and
every v = v_0 are non-negative, the one through Sigma_tau at most C F[H](tau) (V_inf >= 0, T causal), and by (10.8) its
divergence is (delta/4) mu^-1/2 s^(-1-delta) |nabla_L-bar Q|^2 minus (delta/4) mu^-1/2 s^(-1-delta) |nabla_L Q|^2 plus
a cross term, which by Cauchy-Schwarz, (10.9) and (W8c) is at most epsilon_2 mu^-1/2 s^(-1-delta) (|nabla_L Q|^2 +
|nabla_L-bar Q|^2) + C epsilon_2^-1 (mu^-1/2 s^(-8-delta) (|nabla_L Psi|^2 + |nabla-slash Psi|^2) + mu^-3/2
    s^(-10-delta) |Psi|^2) + C(R_null) mu^-3/2 |(sqrt mu d)^{<= 1} H|^2 chi_{[R_null, R_null + r_h]}. The negative term
        and the C epsilon_2^-1 terms are absorbed by the bulk of (10.11): the first since |nabla_L Q|^2 <= 2 s^-3
            |nabla_L Psi|^2 + (9/2) mu^-1 s^-5 |Psi|^2 with s^(-4-delta) <= s^(p-4) and s^(-6-delta) <= s^(p-6); the
                others, whose powers come from Q = s^-3/2 Psi and the bounds mu^-1 s^-4 and mu^-1/2 s^-3 of (10.9) and
                    (W8c) on the coefficients, since s^(-8-delta) <= s^(p-4) and s^(-10-delta) <= s^(p-6) -- for s >= 1
                        and every p >= delta, after enlarging R_H once more and for epsilon_1 small. So (10.11)
holds with mu^-1/2 int_D s^(-1-delta) |nabla_L-bar H-tilde|^2 dvol added on the left and F[H](tau_1) on the right: this
is [Hun19] (4.4).

*Step 2 (the horizon; [Hun19] (4.8)).* In the regular variables the system is boxhat Hhat' - (K/r^2) Hhat' = Acal
Hhat' + beta nabla_L' Hhat', Acal := D_m (A' - K/r^2) D_m^-1 regular at r_h and of degree at most one in k (W8g), beta =
diag(0, 0, 0, 0, 0, 2f', f') (Proposition 10.2(vi)). Consider, as [Hun19] (4.7), J_a := T_ab[Hhat'] (Y + eta_rs T)^b -
(c/r^2) |Hhat'|^2 (Y + eta_rs T)_a with c := 1/2 and Y = Y(sigma). It is supported in r <= 5 r_h/4. Its flux through
Sigma_tau is non-negative and, on [r_h, 9 r_h/8], where Y + T is timelike and equals 2 L' + T at the horizon, is
comparable (constants depending on sigma) to mu^-1 |(sqrt mu d)^{<= 1} Hhat'|^2 dvol_3; through H^+ it is
2 |nabla-slash Hhat'|^2 + T(T, L) + (4c/r_h^2)|Hhat'|^2 >= 0 ((Y + T) . L = -4 there, T(L', L) = |nabla-slash|^2). Its
divergence at r = r_h is (10.10) plus the T part, nabla_T Hhat' . (Acal Hhat' - (2c/r^2) Hhat' - beta Hhat'_R) (T is
    Killing and nabla_T r = 0). Collect: the form (sigma/2)|Q_v|^2 + (1/r_h)|Q_R|^2 + (6/r_h) Q_R . Q_v in (Q_v, Q_R) is
positive definite for sigma > 18/r_h; the other (1/r_h)|Q_R|^2 absorbs, by Cauchy-Schwarz with (10.9) at r_h, the terms
(2c/mu) Q . Q_R, nabla_Y Q . (Acal Q - (c/r^2) Q) + nabla_T Q . (Acal Q - (2c/r^2) Q) (nabla_Y Q = -2 Q_R and nabla_T Q
    = Q_v there) and -Q_v . beta Q_R up to
C (mu^-1/2 |Q_v|^2 + mu^-1/2 |nabla-slash Q|^2 + mu^-3/2 |Q|^2), C depending on the coefficients at r_h alone; 2 Q_R .
beta Q_R >= 0 is dropped; and (sigma/2 + 1/r_h)|nabla-slash Q|^2 + c (sigma/mu + 2/mu^(3/2))|Q|^2 with (sigma/2)|Q_v|^2
dominate the C terms for sigma >= sigma_0/r_h, sigma_0 depending on C. Hence div J|_{r_h} >= c_0 mu^-3/2 |(sqrt mu
d)^{<= 1} Hhat'|^2, and since every coefficient is continuous in the regular chart (Proposition 10.2(vi)) the same holds
on [r_h, r_rs,H] for some r_rs,H in (r_h, 9 r_h/8], while |div J| <= C mu^-3/2 |(sqrt mu d)^{<= 1} Hhat'|^2 on [r_rs,H,
5 r_h/4]. The divergence theorem gives
    mu^-1 int_{Sigma_tau_2} |(sqrt mu d)^{<= 1} Hhat'|^2 chi_{[r_h, r_rs,H]} dvol_3
      + mu^-3/2 int_D |(sqrt mu d)^{<= 1} Hhat'|^2 chi_{[r_h, r_rs,H]} dvol
      <~ mu^-1 int_{Sigma_tau_1} |(sqrt mu d)^{<= 1} Hhat'|^2 chi_{[r_h, 5 r_h/4]} dvol_3
         + mu^-3/2 int_D |(sqrt mu d)^{<= 1} Hhat'|^2 chi_{[r_rs,H, 5 r_h/4]} dvol,                               (10.12)
[Hun19] (4.8).

*Step 3 (the T-energy, and the sum; [Hun19] (4.9)).* (10.11) controls E^{p,(0)}_L[H-tilde](tau_2) and the bulk on r >=
R_null + r_h, whose integrand, s^(p-4) (|nabla_L Psi|^2 + |nabla-slash Psi|^2 + mu^-1 s^-2 |Psi|^2) + s^(-1-delta)
|nabla_L-bar H-tilde|^2 with p - 4 > -5 and 1 + delta < 2, bounds the integrand of B-bar[H] there; (10.12) controls
F[H'] at tau_2 and B-bar[H'] in the bulk on [r_h, r_rs,H]. What (10.5) still asks is F[H'](tau_2) on r >= r_rs,H and
B-bar[H'] on [r_rs,H, R_null + r_h], the latter already of the form of the error term. For the former consider J_T,a :=
(T_ab[Hhat'] - (1/(2 r^2))|Hhat'|^2 g_ab) T^b ([Hun19] (4.9), in the regular variables): its flux through Sigma_tau is
non-negative, controls F[H'](tau) on r >= r_rs,H (T timelike there, uniformly; on Sigma' the flux is (1/2)|nabla_L
Hhat'|^2 + (f/2)|nabla-slash Hhat'|^2 + (f/(2 r^2))|Hhat'|^2) and is at most C F[H'](tau); its fluxes through H^+ and
every v = v_0 are non-negative; and by (W8e) at delta = 0, div J_T = nabla_T Hhat' . (Acal Hhat' - beta Hhat'_R -
Hhat'/r^2), so by (10.9), Proposition 10.2(vi) and Cauchy-Schwarz with the weights s^(-1-delta), s^(1+delta),
    |div J_T| <~ mu^-3/2 |(sqrt mu d)^{<= 1} Hhat'|^2 chi_{[r_h, R_null + r_h]}
                 + (mu^-1/2 s^(-1-delta) (|nabla_T Hhat'|^2 + |nabla_L-bar Hhat'|^2)
                 + mu^-1/2 s^(-4+delta) (|nabla-slash Psi|^2 + mu^-1 s^-2 |Psi|^2)) chi_{[R_null + r_h, oo)},
Psi the radiation field of H-tilde: on s >= 10, |Acal Hhat'| + |Hhat'|/r^2 <~ s^(-3/2) (r^-1 |nabla-slash Psi| + r^-2
|Psi|) by the equivalence of the norms of H and H' there, and |beta Hhat'_R| <= 4 mu r^-3 f^-1 |nabla_L-bar Hhat'| =
4 mu^-1/2 s^-3 f^-1 |nabla_L-bar Hhat'| with s^-3 <= s^(-1-delta). The second line is bounded by the bulk of Step 1
(|nabla_T|^2 <= 2|nabla_L|^2 + 2|nabla_L-bar|^2, s^(-1-delta)|nabla_L Hhat'|^2 <~ s^(p-4)|nabla_L Psi|^2 + mu^-1
s^(p-6)|Psi|^2, and s^(-4+delta) <= s^(p-4) for p >= delta). Apply the divergence theorem to epsilon_3 J_T with epsilon_3
small enough for |div J_T| to be absorbed by the bulk of (10.12) on [r_h, r_rs,H] and by that of Step 1 on [R_null +
r_h, oo), and add the three estimates. The compact-region terms of each -- [R_null, R_null + r_h] in Step 1, [r_rs,H,
5 r_h/4] in Step 2, [r_rs,H, R_null + r_h] in Step 3 -- lie in [r_rs,H, R_null + r_h], the error term of (10.5); the
initial terms are F[H'](tau_1) and E^{p,(0)}_L[H-tilde](tau_1) by the equivalence of the norms on r >= 5 r_h/4. []

*Remark (the l = 0 sector).* At l = 0 the components are (H1, H2, H3, H6), with no angular term, U in row 6 alone and the
regular variable H6' with 2f' nabla_L' (Proposition 10.2(iv), (vi)); r^2 A0_main has the eigenvalues 0, 0, 3, 8,
diag(sqrt2, 1, sqrt2, sqrt2) A0_main diag(sqrt2, 1, sqrt2, sqrt2)^-1 is symmetric and A0 - A0_main/r^2 = O(mu/r^4) (W8g),
so V_inf := A0_main + (3/4) I in that rescaling is symmetric with the eigenvalues 3/4, 3/4, 15/4, 35/4 > 0, and the three
steps apply as written, without the angular terms: (10.5) holds for h_{l=0} with the norms read without |nabla-slash|.
This is [Hun19] Remark 4.5, whose l = 0 leading matrix has the eigenvalues 0, 0, 1, 6 and needs no Hardy inequality
either. Deduced; it does not bound h_{l=0}: (iv)'s K* grows linearly in t, and the right side of (10.5) grows with it.

*What L1 still needs, and nothing else.* (10.5) reduces the decay of h in the harmonic gauge to its decay on the compact
region [r_rs,H, R_null + r_h], and there h = h_RW + pi_X (Proposition 10.2(i), (iii)): the Regge-Wheeler-type part is
Proposition 10.1's, which decays, and pi_X is the gauge vector's, the triangular system (v) with (10.1)'s source. In four
dimensions this is how [Hun19] closes (sections 4.2-7, the compact region bounded by the Zerilli quantity and W). The
rungs are 10.6: each scalar wave equation of (v), with its potential, has the estimates of [Hun19] Appendix A in five
dimensions for a source in the norm (10.16) (Propositions 10.4-10.5, the Morawetz multiplier for the Maxwell potential
computed); the sources the rungs carry are not yet in that norm; 10.7 computes the substitutions that bring them into it
(the growing source, ROUTES-OPEN.md 4.3(3)) and names the two estimates still owed, and 10.8 does the same for l = 0
(4.3(4)). The scalar tails of T6 (t^-7 at l = 2) bound the rate any of this could reach.

### 10.6 The rungs: the scalar wave equation with the Maxwell potential and the free one (`rungs5.py` M1-M5; D49)

The gauge-vector system of Proposition 10.2(v) is triangular, and each rung is a scalar wave equation on the exterior of
five-dimensional Tangherlini at a scalar mode of the class,
    box u - V u = G,   k^2 = l(l + 2) >= 8,   V = 0 (S = div X, X_t, r X_L)  or  V = -4 mu/r^4 (r P),          (10.14)
with G the source the rungs below and J := -Gamma[h_RW] supply ((10.1); Proposition 10.2(iii), (v)). In four dimensions
the estimates for such an equation are [Hun19] Appendix A, resting on Dafermos and Rodnianski; in five, [HKW18] section 7
runs the same chain for a Regge-Wheeler-type equation on Tangherlini without a source -- the T-energy comparison (111),
the red-shift (Lemma 11, "for any bounded radial potential"), the Morawetz current (122)-(123) with Lemma 13 and Theorem
14, the r^p current (125) with Proposition 15 and Theorem 16, and the dyadic argument of Theorem 18 -- and the one input
that depends on the potential is the Morawetz multiplier, chosen there for their master potentials (9.3.2, 10.4.2). Here
the chain is run for the two rung potentials of (10.14) with the source carried, constants not tracked. The setting, the
foliation, the cut-offs and the norms F, B-bar, E^{p,(0)}_L, E^{p,(0)}_ang are those of 10.5; r_P := sqrt(2 mu) is the
photon sphere ([HKW18]'s (n + 1)M/r^(n-1) = 1 at n = 3, 2M = mu); and the degenerate bulk is
    B[u](tau) := int_{Sigma_tau} s^-2 ((1 - 2 mu/r^2)^2 |d u|^2 + f^2 |nabla_r u|^2 + mu^-1 s^-2 |u|^2) dvol_3,
      (10.15)
[Hun19] (2.16) with (1 - 3M/r)^2 read as (1 - 2 mu/r^2)^2 and (1 - 2M/r)^2 as f^2; the source norm, for p in [delta, 2 -
delta] and tau_2 >= tau_1, is
    E^p_source[G](tau_1, tau_2) := mu^1/2 int_{D(tau_1, tau_2)} s^(p+1) |G|^2 dvol
                                   + mu (int_{Sigma''_tau_1} + int_{Sigma''_tau_2}) |G|^2 dvol_3
                                   + mu^3/2 int_{D(tau_1, tau_2) cap {r <= 5 r_h/2}} |nabla_T G|^2 dvol,
                                     (10.16)
the five-dimensional weights this proof produces (the first three terms are [Hun19]'s E^p_source, the display before his
(2.23), with M -> mu^1/2; the fourth replaces his degenerate |d G|^2 and |d_r G|^2 on D'', whose mechanism is not
reproduced here, by |nabla_T G|^2 on a neighbourhood of the photon sphere).

**Proposition 10.4 (the rung estimates; deduced from M1-M5, W8 and [HKW18] section 7; constants not tracked).** Let u
solve (10.14) on the exterior, smooth up to H^+, with G smooth and the norms below finite. There are R_H >= 10 r_h,
depending on delta, and C, depending on delta and R_null, such that for R_null >= R_H, every p in [delta, 2 - delta]
and tau_2 >= tau_1,
    F[u](tau_2) + E^{p,(0)}_L[u-tilde](tau_2) + mu^-1/2 int_{tau_1}^{tau_2} (B[u] + E^{p-1,(0)}_{L,ang}[u-tilde]) dtau
<= C (F[u](tau_1) + E^{p,(0)}_L[u-tilde](tau_1) + E^p_source[G](tau_1, tau_2)).                               (10.17)
There is no compact-region term: where Proposition 10.3 leaves h on [r_rs,H, R_null + r_h] to the master quantities, the
rung's Morawetz current controls it.

*What is computed (M1-M5, exact, sympy; the identities formal in u(t, r)).*
 (M1) The Morawetz identity, [HKW18] (123) at n = 3 with a source: for a radial F, X := F d_r* (' := d_r* = f d_r), omega
      := F' + 3 f F/r, a radial beta, and
          J^M0_a := T_ab[u] X^b + (1/4) omega d_a(u^2) - (1/4) (d_a omega) u^2 + F' beta u^2 (dr*)_a,
with T_ab[u] := d_a u d_b u - (1/2) g_ab (du . du + (k^2/r^2 + V) u^2) on the quotient,
          div J^M0 = (F'/f) |d_r* u + beta u|^2 + (F/r^3)(1 - 2 mu/r^2) k^2 u^2 + W0 u^2 + G (F d_r* u + omega u/2),
          W0 := -(1/4) box omega - (1/2) V' F + (1/2) d_r(mu/r^2) V F + F'' beta/f + F' (beta'/f + 3 beta/r - beta^2/f),
                                                                                                                 (10.18)
box omega = r^-3 d_r (r^3 f d_r omega) and d_r(mu/r^2) = -2 mu/r^3 (d_r, not d_r*, in that one term); the k^2 term is
the angular energy's, |nabla-slash u|^2 = k^2 u^2/r^2, so the coefficient of |nabla-slash u|^2 is F (1 - 2 mu/r^2)/r.
 (M2) With [HKW18]'s n = 3 choice read in mu = 2M,
          F := (1 - 2 mu/r^2)(1 - mu/(2 r^2) + mu^2/(5 r^4)),   beta := 1/(2 sqrt mu)                           (10.19)
(their beta = 1/2 in units M = 1), F'/f = dF/dr = mu (25 r^4 - 24 mu r^2 + 12 mu^2)/(5 r^7) > 0 on the closed exterior
(13/(5 sqrt mu) at r_h, 5 mu/r^3 at infinity, and F'/f >= 13 mu/(5 r^3) throughout); F is bounded, from -7/10 at r_h to
1; the coefficient of k^2 u^2 is F (1 - 2 mu/r^2)/r^3 = (r^2 - 2 mu)^2 (10 r^4 - 5 mu r^2 + 2 mu^2)/(10 r^11) >= (r^2 - 2
mu)^2/(2 r^7) >= 0, a double zero at the photon sphere; and with half the angular term borrowed at the lowest mode,
(1/2) k^2 u^2 >= 4 u^2,
          W := W0 + 4 F (1 - 2 mu/r^2)/r^3 = -(y^3/40) Q(y) mu^-3/2,   y := sqrt(mu)/r in (0, 1],
with Q a polynomial of degree ten having no root in [0, 1] (Sturm) and Q(0) = -140, for V = -4 mu/r^4 and for V = 0
alike: W > 0 on the exterior, W >= c r^-3 with c = 1/5 (Maxwell; min r^3 W = 0.240478) and 1/7 (free; 0.166665), W(r_h)
= 29/(20 mu^3/2) and 17/(4 mu^3/2), and W(r_P) = (11/20 - 51 sqrt 2/160) mu^-3/2 for both, F vanishing there. The other
half of the angular term, (1/2) F (1 - 2 mu/r^2) |nabla-slash u|^2 / r, stays in the bulk with its coefficient
proportional to k^2, where (b) needs it. Some borrowing is necessary: W0 alone is negative at the horizon for the Maxwell
rung (r^3 W0 = -27/20 at r_h) and at infinity for both (r^3 W0 -> -1/2); the share theta of k^2 u^2 >= 8 u^2 borrowed
must exceed 27/112 for the Maxwell rung (r^3 W_theta(r_h) = -27/20 + 28 theta/5) and 1/16 for the free one (r^3 W_theta
-> -1/2 + 8 theta), theta = 1/4 already serves both (min r^3 W_theta = 0.050 and 0.111), and borrowing all of it, as the
first version of this section did, leaves nothing for (b) at l = 2. [HKW18] 9.3.2 made this choice of F and beta for
their potentials; for beta = 0 or beta >= 1/sqrt mu the bulk is negative on part of the exterior (the control uses
2/sqrt mu).
 (M3) [Hun19]'s (A.3) with room: k^2/r^2 - 4 mu/r^4 >= k^2/(2 r^2) on the exterior for every k^2 >= 8 (equality at r_h
      when k^2 = 8), so the T-energy density of the Maxwell rung is pointwise at least half of the one without the
      potential, and |V| <= 4/mu on the exterior.
 (M4) The radiation variable Psi := r^(3/2) u: d_u d_v Psi = -f Vcal Psi - f r^(3/2) G with Vcal := k^2/r^2 + V + V0, V0
      the weight's potential of (10.6), V_inf := lim r^2 Vcal = k^2 + 3/4 >= 35/4, and Vcal - V_inf/r^2 = -7 mu/(4 r^4)
      (Maxwell), 9 mu/(4 r^4) (free); the p-current identity (10.7) holds for one component with r^(3/2) G in the place
      of Uhat Psi.
 (M5) The g-current, [HKW18] p. 55: for a radial g,
          div((1/4)(d_a g) u^2 - (1/4) g d_a(u^2)) = (1/4)(box g) u^2 + (1/2) g f^-1 |d_t u|^2
                                                     - (1/2) g (f |d_r u|^2 + (k^2/r^2 + V) u^2) - (1/2) g u G.
                                                       (10.20)

*Proof.* Six currents, one divergence theorem, every bulk positive. Fix r_h < r_0 <= 9 r_h/8 and 5 r_h/4 <= r_1 < r_P --
so that eta_rs is constant off [r_0, r_1], and, the foliation being [Hun19]'s with his g = r_* on [5M/2, R_null] read as
[5 r_h/4, R_null], the leaves are t = const on [r_1, R_null] -- and R_1 := R_null + r_h (so that r >= R_1 lies where
eta_null = 1), and let chi_M be a cut-off equal to 1 on r <= R_1 and 0 on r >= R_1 + r_h.
Throughout, the sums over the modes are taken last; the constants are uniform in l by (M2), (M3), (M4) and the Poincare
inequality k^2 u^2 >= 8 u^2.

*(a) The T-energy and the red-shift.* By (M3) the T-energy density f |nabla_r u|^2 + (k^2/r^2 + V) u^2 + ... is at least
half the one with V = 0 pointwise, so [HKW18]'s comparison (111) holds without a Hardy inequality, with the other
direction trivial. The red-shift current T-hat_ab[u] Y^b of [HKW18] 7.8 (the Y of (10.3)) has, for sigma large, the
coercive divergence (113) in r <= r_0 -- their Lemma 11, which asks only that V be bounded, (M3); at one component the
identity is (10.10) with Acal = V, beta = 0. The N-current J^N := T_ab[u] T^b + T-hat_ab[u] Y^b then gives, as their
Theorem 12 with the source,
    F[u](tau_2) + int_{tau_1}^{tau_2} int_{Sigma_tau cap {r <= r_0}} (F's density) dtau
<~ F[u](tau_1) + int_{tau_1}^{tau_2} int_{Sigma_tau cap {r_0 <= r <= r_1}} (F's density) dtau + int_D |nabla_N u| |G|
dvol, the fluxes through H^+ and I^+ non-negative. The middle term and the source term are what the Morawetz current
pays.

*(b) The Morawetz current.* By (M1), (M2) and the Poincare inequality in the form k^2 u^2 >= (1/2) k^2 u^2 + 4 u^2,
    div J^M0 >= (F'/f) |d_r* u + beta u|^2 + (F/(2 r))(1 - 2 mu/r^2) |nabla-slash u|^2 + W u^2 + G (F d_r* u + omega u/2)
with every coefficient non-negative and W >= c r^-3 (the term dropped, (1/2)(F/r^3)(1 - 2 mu/r^2)(k^2 - 8) u^2, is
non-negative; half the angular term is in W and the other half is here, each used once). [HKW18] pp. 55-57 turn this into
the current J^M := J^M0 + (1/4)(d g) u^2 - (1/4) g d(u^2) + epsilon_3 T-hat_ab[u] Y^b of their Lemma 13 by three generic
steps, each a choice of a constant and valid for any F, beta, W with these signs: the epsilon_0 and epsilon_1 splits of
the square and of the angular term, which leave epsilon_0 (F'/f) |d_r* u|^2 + epsilon_1 (F/r)(1 - 2 mu/r^2) |nabla-slash
u|^2 + (1/4) W u^2 (their p. 55: |a + b|^2 >= epsilon_0 |a|^2 - (epsilon_0/(1 - epsilon_0)) |b|^2 with b = beta u costs
(epsilon_0/(1 - epsilon_0)) beta^2 (F'/f) u^2, and beta^2 F'/f <= 5/(4 r^3) on the exterior against W >= c r^-3, (M2), so
epsilon_0 <= 3c/(5 + 3c) serves; epsilon_1 <= 1/2); the g-current (10.20) with g := epsilon_2 mu chi (1 - 2 mu/r^2)^2 /
r^3, chi vanishing for r <= r_0 and equal to 1 for r >= (r_0 + r_1)/2, which adds (1/2) g f^-1 |d_t u|^2 and whose
negative terms -(1/2) g (f |d_r u|^2 + (k^2/r^2 + V) u^2) + (1/4)(box g) u^2 are absorbed by the three positive ones for
epsilon_2 small (F'/f >= 13 mu/(5 r^3), and the coefficient of k^2 u^2 left after the epsilon_1 split is at least (1/2 -
epsilon_1)(r^2 - 2 mu)^2/(2 r^7) against the epsilon_2 mu (r^2 - 2 mu)^2/(2 r^9) of g, (M2); (M3) for the sign of
k^2/r^2 + V); and the red-shift addition epsilon_3 T-hat_ab Y^b, which makes the bulk coercive in r <= r_0 by (a). The
result is their Lemma 13 for the rung:
    K^M := div J^M >~ r^-1 s^-2 ((1 - 2 mu/r^2)^2 (|nabla_T u|^2 + |nabla-slash u|^2) + f^2 |nabla_r u|^2 + mu^-1 |u|^2)
                       in r >= r_0,   K^M >~ (F's density) in r <= r_0,
                         (10.21)
up to the source term G (F d_r* u + omega u/2 - g u/2 + epsilon_3 Y(u)), and the boundary terms of J^M through Sigma_tau,
H^+ and v = v_0 are bounded by F's density, by T-hat_ab T^b n^a and by T-hat_ab T^b L^a (F bounded, omega - g = 0 at r_h
since F'(r_h) = 0 and g vanishes there). (10.21) is at least r^-1 times B's integrand (10.15) (its mu^-1 r^-3 |u|^2 is >=
mu^-1 r^-1 s^-4 |u|^2), so B's integrand <~ K^M on r <= R_1 + r_h with a constant depending on R_null -- which is the
point of the degenerate bulk: the Morawetz current pays the middle term of (a), r_1 < r_P, and the whole of B on r <=
R_1.

*(c) The far region.* (M4) puts the rung in the form of Proposition 10.3's Step 1 with one component, Uhat = 0 and the
source s^(3/2) G in the normalisation of Psi-tilde := s^(3/2) eta_null u (plus the commutator of box with eta_null,
supported in [R_null, R_null + r_h]): the p-current J^p of (W8d) on Psi-tilde and epsilon_1 J_delta of (W8e) on eta_null
u give (10.11) with its left side enlarged by mu^-1/2 int_D s^(-1-delta) |nabla_L-bar u-tilde|^2 dvol and its right side
by F[u](tau_1), the compact-region term supported in [R_null, R_null + r_h] (paid in (d) by epsilon_M K^M, which is
non-degenerate there) -- the only differences being that V_inf = k^2 + 3/4 is a number, that Vcal - V_inf/r^2 = O(mu/r^4)
is -7 mu/(4 r^4) or 9 mu/(4 r^4), and that the source enters the two cross terms: s^(p-3) f^-1 |nabla_L Psi-tilde|
s^(3/2) |G| <= epsilon mu^-1/2 s^(p-4) |nabla_L Psi-tilde|^2 + C epsilon^-1 mu^1/2 s^(p+1) |G|^2 and epsilon_1 s^-delta
|nabla_T u-tilde| |G| <= epsilon mu^-1/2 s^(-1-delta) |nabla_T u-tilde|^2 + C epsilon^-1 mu^1/2 s^(1-delta) |G|^2, with
s^(1-delta) <= s^(p+1) since s >= 1: the first term of
(10.16).

*(d) The sum.* Apply the divergence theorem to J := J^N + epsilon_M chi_M J^M + epsilon_p (J^p + epsilon_1 J_delta) on
D(tau_1, tau_2). Bulk: in r <= r_0 the N-bulk and epsilon_M K^M are coercive; in [r_0, R_1] epsilon_M K^M is (10.21),
which absorbs the N-bulk's negative part on [r_0, r_1] (non-degenerate there, r_1 < r_P) for epsilon_M fixed and
epsilon_p small; in r >= R_1 the far bulks of (c) are positive, K^M >= 0 up to its source term (F' > 0, the angular
coefficient >= 0, W > 0), and the cut-off term (d chi_M) . J^M, supported in [R_1, R_1 + r_h] and bounded by |d u|^2 +
mu^-1 s^-2 |u|^2 there, is absorbed by the far bulks for epsilon_M small (the J^p bulk for nabla_L, nabla-slash and u,
the J_delta bulk for nabla_L-bar, both present since R_1 >= R_null + r_h). Boundary: through Sigma_tau_2 the current
gives F[u] + epsilon_p E^{p,(0)}_L[u-tilde] up to constants (J^N by [HKW18] Lemma 11, J^M bounded by F's density, J^p as
in 10.5); through Sigma_tau_1 at most C of the same; through H^+ and every v = v_0 non-negative for J^N and J^p +
epsilon_1 J_delta and bounded by T-hat_ab T^b n^a, which J^N's own flux controls, for epsilon_M J^M. Sources: J^p's and
J_delta's by (c); J^M's -- G (F d_r* u + omega u/2 - g u/2 + epsilon_3 Y(u)) on r <= R_1 + r_h -- by Cauchy-Schwarz
against (10.21), whose |nabla_r u|^2, |u|^2 and near-horizon terms are non-degenerate, at the cost of C mu^1/2 int |G|^2
dvol there, below the first term of (10.16); and J^N's, int_D nabla_N u . G: in r <= r_0 against the N-bulk, on [r_0,
r_1] and on [2 r_h, R_1], where (1 - 2 mu/r^2)^2 >= 1/4, against (10.21), in r >= R_1 against the far bulks as in (c)
(|nabla_T u| <= |nabla_L u| + |nabla_L-bar u|), and on [r_1, 2 r_h], which contains the photon sphere, where (10.21)
degenerates in nabla_T u, by parts in T with a cut-off chi_T equal to 1 on [r_1, 2 r_h] and supported in [r_0, 5 r_h/2]:
int_D chi_T nabla_T u . G = -int_D chi_T u nabla_T G + int_{Sigma_tau_2} chi_T u G (T . n) - int_{Sigma_tau_1} chi_T u G
(T . n) (T is Killing, chi_T is radial, and the cut-off kills the null boundaries, r_0 > r_h and 5 r_h/2 < R_null), the
bulk bounded by epsilon mu^-3/2 int chi_T |u|^2 + C epsilon^-1 mu^3/2 int chi_T |nabla_T G|^2 and the two boundary terms
by epsilon F[u](tau_i) + C epsilon^-1 mu int_{Sigma''_tau_i} |G|^2 dvol_3 (supp chi_T lies in Sigma'') -- the last three
terms of (10.16), the epsilon F[u](tau_2) absorbed on the left. Collecting, with B's integrand bounded by (10.21) on r <=
R_1 and by the far bulks on r >= R_1 (as in Proposition 10.3's Step 3), (10.17) follows. []

**Proposition 10.5 (decay of the rungs; deduced from Proposition 10.4 by [HKW18] Theorem 18's argument with the source
carried; constants not tracked).** Let u solve (10.14) as in Proposition 10.4, fix delta-bar in [delta, 1/10], and let
    I^(0)[u] := (F[T^{<= 2} u] + k^2 F[T^{<= 1} u] + k^4 F[u] + E^{2-delta,(0)}_L[T^{<= 2} u-tilde]
                 + k^2 E^{2-delta,(0)}_L[T^{<= 1} u-tilde] + k^4 E^{2-delta,(0)}_L[u-tilde])(0),
    I_{source, delta-bar}[G] := sup_{p in [delta, 2 - delta-bar]} sup_{tau_2 >= tau_1 >= 0} (1 + tau_1/sqrt mu)^(2 - p -
      delta-bar)
                 E^p_source[T^{<= 2} G, k T^{<= 1} G, k^2 G](tau_1, tau_2)
([Hun19] (2.23)-(2.24) with K^{<= j} read at a mode of the class, where the rotations act as k -- except that his I^(0)
carries E^{2-delta}_L for K^{<= 1} only, and here it is carried at every order of T and k, because (iv) runs the argument
for T u and k u through (10.17), whose right side has E^p_L; a boundedness statement for F alone would spare them and is
not proved here). Then for every p in [delta, 2 - delta-bar] and tau >= 0,
    F[u](tau) + E^{p,(0)}_L[u-tilde](tau) + mu^-1/2 int_tau^oo (B[u] + E^{p-1,(0)}_{L,ang}[u-tilde]) dtau'
<~ (1 + tau/sqrt mu)^(-2 + p + delta + delta-bar) (I^(0)[u] + I_{source, delta-bar}[G]),                       (10.22)
[Hun19] (A.10) in five dimensions, with one more delta in the exponent: the cost of carrying the source through the times
between the dyadic samples with (10.17) itself rather than with a separate boundedness theorem, cosmetic for L1, which
any rate tau^(-2+) serves, and what is proved.

*Proof.* Write e_p(tau) := F[u](tau) + E^{p,(0)}_L[u-tilde](tau), I := I^(0)[u] + I_{source, delta-bar}[G], and tau_j :=
2^j sqrt mu. Four facts, each from (10.17):
 (i) *Boundedness.* (10.17) at p and on [0, tau] with E^p_source[G](0, tau) <= I gives e_p(tau) <~ e_p(0) + I <~ I for p
     <= 2 - delta-bar, and the same for T^{<= 2} u, k T^{<= 1} u and k^2 u, whose data are in I^(0) and whose sources
     are in I_source.
 (ii) *The first dyadic step, p = 2 - delta-bar.* (10.17) on [tau_{j-1}, tau_j]: mu^-1/2 int_{tau_{j-1}}^{tau_j}
     E^{1-delta-bar}_{L,ang} dtau <~ I by (i), so by the mean value theorem, applied to the sum of the integrals for u, T
     u, k u, T^2 u, k T u and k^2 u so that one sample time serves all six, there is tau-tilde_j in [tau_{j-1}, tau_j]
     with E^{1-delta-bar,(0)}_L[u-tilde](tau-tilde_j) <~ (tau_j/sqrt mu)^-1 I, and the same for the other five, and by
     interpolation of the weights, s^(1-3) = (s^(1-delta-bar-3))^(1-delta-bar) (s^(2-delta-bar-3))^(delta-bar),
     E^{1,(0)}_L[u-tilde](tau-tilde_j) <~ (tau_j/sqrt mu)^(-1+delta-bar) I.
 (iii) *The second dyadic step, p = 1.* (10.17) on [tau-tilde_{j-2}, tau-tilde_j], with E^1_source(tau-tilde_{j-2},
     tau-tilde_j) <= (1 + tau-tilde_{j-2}/sqrt mu)^(-1+delta-bar) I from the definition of I_source:
         mu^-1/2 int_{tau-tilde_{j-2}}^{tau-tilde_j} (B[u] + E^{0,(0)}_{L,ang}[u-tilde]) dtau
           <~ (tau_j/sqrt mu)^(-1+delta-bar) I + F[u](tau-tilde_{j-2}).
The integrand controls F's: on r >= R_1, E^{0,(0)}_{L,ang}'s, s^-3 (|nabla_L (s^(3/2) u)|^2 + |nabla-slash (s^(3/2)
u)|^2) >= (1/2)|nabla_L u|^2 + |nabla-slash u|^2 - (9/4) mu^-1 s^-2 |u|^2 >= (1/2)|nabla_L u|^2 + (1/2)|nabla-slash
u|^2 + (7/4) mu^-1 s^-2 |u|^2 by k^2 >= 8 (no Hardy inequality; [HKW18] Lemma 17 borrows the same way), and on r <= R_1
B's, non-degenerate except at the photon sphere, where (1 - 2 mu/r^2)^2 multiplies |nabla_T u|^2 and |nabla-slash u|^2.
There the one-dimensional Poincare inequality in r on [r_P - rho, r_P + rho], int |w|^2 dr <~ rho^2 int |d_r w|^2 dr +
int_{rho <= |r - r_P| <= 2 rho} |w|^2 dr, applied to w = nabla_T u along Sigma_tau, where d_r is nabla_r since the
leaves are t = const on [5 r_h/4, R_null], with B[T u]'s f^2 |nabla_r T u|^2 and B[u]'s |nabla_T u|^2 off the photon
sphere, while |nabla-slash u|^2 = k^2 u^2/r^2 is k^2 B[u]'s zeroth-order term, non-degenerate; this gives
int_{Sigma_tau} (F's density) <~ B[u] + B[T u] + k^2 B[u] + E^{0,(0)}_{L,ang}[u-tilde]. So, with (iii) for T u and k u
as well (their sources are T G and k G, their data in I),
         mu^-1/2 int_{tau-tilde_{j-2}}^{tau-tilde_j} F[u] dtau <~ (tau_j/sqrt mu)^(-1+delta-bar) I +
           F[u](tau-tilde_{j-2})
                                                           + F[T u](tau-tilde_{j-2}) + k^2 F[u](tau-tilde_{j-2}).
 (iv) *The rate.* Since tau-tilde_j - tau-tilde_{j-2} >= tau_{j-2}, the mean value theorem gives tau-hat_j in the
     interval with F[u](tau-hat_j) <~ (tau_j/sqrt mu)^(-2+delta-bar) I + (tau_j/sqrt mu)^-1 (F[u] + F[T u] + k^2 F[u])
     (tau-tilde_{j-2}), so F[u](tau-hat_j) <~ (tau_j/sqrt mu)^-1 I by (i). Between the samples, (10.17) at p = delta from
     the nearest tau-hat_j below gives F[u](tau) <~ F[u](tau-hat_j) + E^{delta,(0)}_L[u-tilde](tau-hat_j) + (tau_j/sqrt
     mu)^(-2+delta+delta-bar) I, and E^{delta,(0)}_L <= (E^{0,(0)}_L)^(1-theta) (E^{2-delta-bar,(0)}_L)^theta with theta
     := delta/(2 - delta-bar) and E^{0,(0)}_L <~ F: so F[u](tau) <~ (tau/sqrt mu)^(-1+theta) I for every tau >= sqrt mu,
     and the same for T u and k u by (ii)-(iii) run for them, with (10.17) for T^2 u, k T u and k^2 u, whose data are in
     I^(0) and whose sources are in I_source. Fed back into the first inequality, since theta < delta <=
     delta-bar, F[u](tau-hat_j) <~ (tau_j/sqrt mu)^(-2+delta-bar) I, and between the samples, by the same interpolation,
     F[u](tau) <~ (tau/sqrt mu)^(-2+delta+delta-bar) I. The p-weighted energy follows by interpolation between
     E^{0,(0)}_L <~ F and E^{2-delta-bar,(0)}_L <~ I: E^{p,(0)}_L[u-tilde](tau) <~ (tau/sqrt
     mu)^((-2+delta+delta-bar)(1-p/(2-delta-bar))) I <= (tau/sqrt mu)^(-2+p+delta+delta-bar) I; and the integrated terms
     from (10.17) on [tau, oo) with the decayed data at tau and E^p_source(tau, oo) <= (1 + tau/sqrt mu)^(-2+p+delta-bar)
     I. []

*What this gives, and what it does not.* Each rung of Proposition 10.2(v) -- S with source div J, r P with source r
dJ_tr + 2 (d_t S - J_t) in S and J, X_t with source J_t - (2 mu/r^3) P, r X_L with source (2 k f/r) Q_r + r J_L -- is an
equation (10.14), and Propositions 10.4-10.5 are the estimates for that equation with a source in the norm (10.16). They
do not by themselves give the decay of the gauge vector, because the sources the rungs carry are not in (10.16)'s
weights: the norm asks for mu^1/2 int s^(p+1) |G|^2 dvol, and what a rung below supplies, by (10.17), is mu^-1/2 int
E^{p'-1,(0)}_{L,ang} dtau, a bulk integral of s^(p'-4) |nabla_L Psi|^2 with p' <= 2 - delta, and s^(-1-delta)
|nabla_L-bar u|^2 from J_delta. For r P the source carries 2 d_t S, and s^(p+1) |nabla_T S|^2 = s^(p-2) |nabla_T
Psi_S|^2 up to lower order would need p' = p + 2 of S's rung, outside the hierarchy for every p >= delta; for r X_L the
source (2 k f/r) Q_r carries (2 f r/k) d_r S, which grows in r. This is [Hun19] section 4.3's problem in five
dimensions. There the first rung is tr h, which solves the homogeneous wave equation in the harmonic gauge and so decays
at the rate of his Proposition A.5 with k = 1 (his Proposition 5.2, (1 + tau/M)^(-4+p+3 delta)); P and W are replaced
through (4.27)-(4.30) by P-bar and W-bar, combinations of them with S and psi_Z carrying the factor u + r, interpolated
by eta_b into (4.35)-(4.38); and the sources G_P, G_0, G_1, G_2 of (4.39)-(4.42) are bounded in his Lemmas 4.8-4.10 with
factors (1 + tau/M)^2 that the faster decay of the first rung pays (his Lemma 5.5). That is ROUTES-OPEN.md 4.3(3), done
in 10.7, where the five-dimensional substitutions are computed and what 10.6 contributes is the estimate each barred
rung is fed to; l = 0 (4.3(4); his Theorem 8.1, the red-shift argument for the coefficient of the singular stationary
solution, with W2's ODE) is 10.8. Neither needs an estimate for a new equation; both are work on the sources and on the
first rung, and both leave the first rung's rapid decay to be proved.

### 10.7 The growing source: [Hun19] section 4.2 in five dimensions (`growing5.py` G1-G5; D50)

10.6 estimates a rung whose source lies in the norm (10.16); the sources the rungs of Proposition 10.2(v) carry do not
(10.6's closing paragraph). [Hun19] section 4.2 meets the same obstacle in four dimensions and resolves it in three
moves: the first rung is taken as tr h, which solves the homogeneous wave equation in the harmonic gauge; the gauge
vector's components are written with the master field as source ((4.21)-(4.26)); and the components are replaced by
combinations with the master field and tr h carrying the factor u + r ((4.27)-(4.30)), interpolated into the horizon
region by eta_b ((4.35)-(4.38)), so that every source has a good weight in r at the price of a weight in u, which the
rapid decay of the first rungs pays (his Lemmas 4.8-4.10, 5.5). This section computes the five-dimensional form of each
move; what the computation does not give is said at the end.

*Setting.* A scalar mode l >= 2 (even, k^2 = l(l + 2) >= 8) of a perturbation h in the class in harmonic gauge, h =
h_RW + pi_X (Proposition 10.2(iii)), X = X_t S dt + X_r S dr + X_L r S_i dz^i with box X = J := -Gamma[h_RW]. In
[KI03]'s variables at n = 3 (Proposition 10.1(iii)): x := mu/r^2, m := k^2 - 3, H := m + 6x, Phi the master field on the
orbit space with
    box_2 Phi = (V_S/f) Phi,   V_S = f Q/(16 r^2 H^2),
    Q = 1296 x^3 + (624 m - 144) x^2 + (36 m^2 - 432 m) x + 16 m^3 + 60 m^2                                   (10.27)
([KI03] (3.5)-(3.7) at n = 3, K = 1, lambda = 0; box_2 the d'Alembertian of g_2 = -f dt^2 + dr^2/f), Psi := r^(3/2) H
Phi, and h_RW's components F, F_ab reconstructed by (10.1). The scalar-wave normalisation of the master field is phi :=
r^(-3/2) Phi = Psi/(r^3 H): it is to Phi what [Hun19]'s r^-1 psi_Z is to psi_Z, since Phi, like psi_Z, solves the
radiation-field form of a wave equation on the orbit space, and the energies F, B, E^p of 10.5 are phi's. Sigma := tr h
is the first rung: box Sigma = 0 (the trace of Proposition 10.2(i)'s Lichnerowicz equation, R_ab = 0), and S = div X =
(Sigma - tr h_RW)/2 with tr h_RW = 4 F (the trace of (10.1) is -2F, G1) -- [Hun19]'s S = tr h = tr h_RW - S_W with his
S_W = 2 div W. u := t - r_* + const, u = tau for r >= R_null; eta_b as in 10.8.

*What is computed (G1-G5, exact, sympy; the harmonic kept symbolic with S'' = -2 cot 2th S' - k^2 S applied and the
angle evaluated at two exact points, as in W7).*
 (G1) The reconstruction read from [KI03] solves the Einstein equations: with F, F_ab from (10.1) and Phi solving
      (10.27), F^a_a = -2F ([KI03] (2.11)) and D^b(r F_ab) - 2 D_a(r F) = 0 ([KI03] (2.12), the equations E_a = 0) hold
      modulo (10.27), at three rational (mu, k) and three radii; and at n = 2 the same transcription of (3.7) is the
      Zerilli potential (Q = 128 lambda^2 (lambda + 1) + 192 lambda^2 x + 288 lambda x^2 + 144 x^3, m = 2 lambda). A READ
      check of (10.27) and (10.1).
 (G2) The source in h_RW's components, theta-free after division by S and r S_th:
          J_t = 3 d_t F + (f/2) d_t F_rr - f d_r F_tr + (1/(2f)) d_t F_tt - ((3 r^2 - mu)/r^3) F_tr,
          J_r = 3 d_r F - (f/2) d_r F_rr + f^-1 d_t F_tr - (1/(2f)) d_r F_tt - ((3 r^2 - mu)/r^3) F_rr + (6/r) F,
          J_L = (k/(2 r f)) F_tt - (k f/(2 r)) F_rr - (k/r) F,                                              (10.28)
      and tr h_RW = 4F.
 (G3) The direct system, [Hun19] (4.21)-(4.23) in five dimensions: with X_1 := f X_r and d_t X_t eliminated through
      S = div X = -f^-1 d_t X_t + r^-3 d_r(r^3 X_1) + (k/r) X_L,
          box_l X_t + (2 mu/r^3)(d_t X_r - d_r X_t) = J_t,
          box_l X_1 - (3/r^2)(1 - 3 mu/r^2) X_1 - (2k/r^2)(1 - 2 mu/r^2) X_L = (2 mu/r^3) S + f J_r,
          box_l X_L + (1/r^2)(1 + mu/r^2) X_L - (2k/r^2) X_1 = J_L                                            (10.29)
      (his (4.21): box W_0 + (2M/r^3) W_0 = -(2M/r^3) P_even + ...; (4.22): box W_1 - (2/r^2)(1 - 4M/r) W_1 - (2/r)(1
      - 3M/r) D-slash_1 W_2 = -(M/r^2) S + ...; (4.23): box_1 W_2 - (1/r^2)(1 - 2M/r) W_2 - (2/r) D-slash_1* W_1 = 0),
      the first line being W6's (box X)_t = box_l X_t + (2 mu/r^3) P. The (X_1, X_L) pair is coupled at zeroth order
      with the matrix his section 6 calls A_W, read in five dimensions.
 (G4) The sources in [Hun19]'s canonical form -- d_r^2 eliminated by the master equation, so that only d_t^a and
      d_t^a d_r remain -- and in the scalar-wave normalisation phi, with box_l phi = V_phi phi,
          V_phi = -12 mu (k^2 + 3) ((k^2 - 3) r^2 + 2 mu) / (r^6 H^2) = O(mu/r^4)                               (10.30)
      (the master potential read on phi: [HKW18]'s scalar master quantity, whose decay Proposition 10.1(iv) cites, is
      Phi = r^(3/2) phi), with H = k^2 - 3 + 6 mu/r^2 and f = 1 - mu/r^2, the trace and the four rung sources read
          tr h_RW = 4F = 2 r f d_r phi + c_F phi,            c_F = (12 mu + (2/3)(k^2 - 3)(k^2 + 6) r^2)/(r^2 H),
          G_P := r dJ_tr + d_t Sigma - d_t(4F) - 2 J_t = 4 r f d_t d_r phi + c_2 d_t phi + d_t Sigma,
                                                             c_2 = (24 mu + (4/3)(k^2 - 3)(k^2 + 6) r^2)/(r^2 H),
          G_t := J_t = -2 r f d_t d_r phi + c_t d_t phi,     c_t = -2 (3 m r^4 - (4 m - 6) mu r^2 - 12 mu^2)/(r^4 H),
          G_1 := f J_r = -2 r d_t^2 phi + 2 mu f ((m + 12) r^2 - 6 mu)/(r^4 H) d_r phi - r f V_phi phi,
          G_L := J_L = 0,                                                                      m := k^2 - 3     (10.31)
      every other term cancelling modulo the master equation (the coefficient functions read exactly at k^2 = 8, 24, 48
      and fitted in k, the fit checked at a fourth mode, k^2 = 80, outside the fitting set; G4 verifies (10.31) at four
      (k^2, mu) points) -- [Hun19] (4.25), (4.21), (4.22), (4.23): his -6 f nabla_t nabla_r psi_Z and 2 f nabla_t nabla_r
      psi_Z are O(r) d_t d_r on r^-1 psi_Z, his 2 nabla_t^2 psi_Z is O(r) d_t^2, and his W_2 equation has no source
      either. The bad terms are the O(r) d_t d_r phi of G_P and G_t, the O(1) d_t phi of both, the d_t Sigma of G_P and
      the O(r) d_t^2 phi of G_1; everything else is in the norm's weights.
 (G5) The substitutions, [Hun19] (4.27)-(4.30) in five dimensions. With u := t - r_* + const and the corrections taken
      where eta_b = 1,
          r P-bar   := r P - r^2 d_t phi + (u + r) ((2 k^2/3) phi + Sigma/2),
          X_t-bar   := X_t + (r^2/2) d_t phi - (u + r) phi,
          X_1-bar   := X_1 + (r^2 f/2) d_r phi + ((k^2 - 3) r^4 + 6 mu^2)/(r^3 H) phi,
          X_L-bar   := X_L + (k r/2) phi                                                                        (10.32)
      (his P-bar = P + (3/2) r nabla_t psi_Z - ((u + r)/(2r))(2 lambda + 3) psi_Z - ((u + r)/2) S, W-bar_0 = W_0 - (r/2)
      nabla_t psi_Z + ((u + r)/(2r)) psi_Z, W-bar_1 = W_1 - (r/2) f nabla_r psi_Z + (3M/(2r)) f (lambda + 3M/r)^-1 psi_Z,
      W-bar_2 = W_2 - (r/2) D-slash_1* psi_Z, with psi_Z = r (r^-1 psi_Z): the same shape term by term). Each coefficient
      was found, not fitted: the r^2 d_t phi terms are forced exactly by the d_t d_r phi coefficients of (10.31) through
      2 nabla(A) . nabla d_t phi = 2 f A' d_t d_r phi (A' = -2 r, r); (r^2 f/2) d_r phi is the solution of the
      first-order ODE that the d_t^2 phi coefficient of the X_1 equation imposes, its homogeneous solution f dropped; (k
      r/2) phi is forced exactly by the coupling -(2k/r^2) X_1-bar in the X_L equation; the zeroth-order coefficient of
      X_1-bar is the exact integral that removes the d_r phi term of the X_1 equation; and the (u + r) coefficients are
      the limits at infinity of the exact functions f c/2 that would remove the d_t phi, d_t Sigma coefficients outright
      (2 k^2/3, 1/2 and -1), through 2 nabla(u + r) . nabla = -2 f^-1 d_t - (2 mu/r^2) d_r. The barred rungs solve, where
      eta_b = 1 and modulo box_l phi = V_phi phi, box_l Sigma = 0,
          box_l(r P-bar) + (4 mu/r^4) r P-bar = -(mu/(r^2 f)) nabla_L Sigma - (mu/(2 r^3)) Sigma - (4 k^2 mu/(3 r^2))
              d_r phi + O(r^-2) d_t phi - (2 k^2 mu/(3 r^3)) phi + (u + r) ((2 mu/r^4) Sigma + O(r^-4) phi),
          box_l X_t-bar = (2 mu/r^2) d_r phi + O(r^-2) d_t phi + (mu/r^3) phi - (u + r) V_phi phi - (2 mu/r^3) P,
          box_l X_1-bar - (3/r^2)(1 - 3 mu/r^2) X_1-bar - (2k/r^2)(1 - 2 mu/r^2) X_L-bar = (2 mu/r^3) S + c_1(r) phi,
          box_l X_L-bar + (1/r^2)(1 + mu/r^2) X_L-bar - (2k/r^2) X_1-bar = c_L(r) phi,                        (10.33)
      every coefficient O(r^-2) or better and the (u + r)-weighted ones O(r^-4); in the first line the Sigma terms are
      exact and the phi coefficients are leading terms, in the second the d_r phi, phi and (u + r) phi terms are exact
      (the last is -V_phi, (10.30)), and in the third and fourth the source is a single phi term, c_1 and c_L of order
      r^-3 with leading terms 2 mu k^2 (k^2 + 1)/((k^2 - 3) r^3) and -6 k mu (k^2 + 1)/((k^2 - 3) r^3) -- all checked at
      the four (k^2, mu) of G4 by exact cancellation (G5): his (4.31)-(4.34), with s^-2 nabla_L Sigma where he has s^-1
      nabla_L S and no d_t^2 term left anywhere. The interpolation into the horizon region is his (4.35)-(4.38) verbatim,
      P-hat := P + eta_b (...) and so on, with G_P, G_0, G_1, G_2 the sources of the hatted rungs.

*What is deduced.* The three regions of his Lemmas 4.8-4.10. On [r_h, b r_h] the hatted rungs are the rungs and the
sources are (10.31): bounded by mu^-1/2 |(sqrt mu d)^{<= 1} Sigma| and mu^-1/2 |(sqrt mu d)^{<= 2} phi| (one derivative
more than the rung's own order, the price of the photon sphere he names), with constants depending on b. On [b r_h, 2 b
r_h] the cut-off's derivatives act on the corrections, whose (u + r) factor is (1 + tau/sqrt mu) there: the sources are
bounded by (1 + tau/sqrt mu) times the same quantities. On [2 b r_h, oo) they are (10.33): mu^-1/2 s^-2 |nabla_L Sigma| +
mu^-1/2 s^-3 |Sigma| + mu^-1/2 s^-2 |(sqrt mu d)^{<= 1} phi| + (1 + tau/sqrt mu) mu^-1/2 s^-4 (|Sigma| + |phi|) for r
P-bar, and better for the others. So I_source[G] of each hatted rung is bounded, as in his Lemmas 5.5 and 5.7, by the
initial norms of Sigma and phi with the derivatives counted, provided the first rungs decay fast enough to pay the (1 +
tau)^2 of the middle region: Sigma and phi at the rate (1 + tau/sqrt mu)^(-4+p+delta) of his Proposition A.5 with k = 1.
Then Propositions 10.4-10.5 apply to r P-hat and X_t-hat in turn (their potentials -4 mu/r^4 and 0, their sources in
(10.16)), and the pair (X_1-hat, X_L-hat) is a system with the zeroth-order matrix of (10.29) and a source in (10.16).

*What remains, and is not done here.* Two estimates, both of a known type and neither in this record. (a) The rapid decay
of the first rungs: for Sigma (box_l Sigma = 0) and for phi (box_l phi = V_phi phi, V_phi = O(mu/r^4), the master
potential), the extension of the r^p hierarchy of 10.6 past p = 2 by one commutation with f^-1 r^2 nabla_L
(Angelopoulos-Aretakis-Gajic; his Proposition A.5 with k = 1 and its conditions (A.7)-(A.9)), giving (1 + tau/sqrt
mu)^(-4+p+3 delta) in place of 10.6's (-2+p+...). 10.9 computes the five-dimensional conditions and deduces the rate for
l >= 2, and for Sigma at l >= 1 (Proposition 10.6); at l = 0 it finds the extension obstructed. (b) The coupled estimate
for (X_1-hat, X_L-hat): his section 6 for the system W = A_W W + G, the T-energy, red-shift, Morawetz and r^p currents
for a two-component system whose coupling matrix is (10.29)'s; 10.10 computes the five-dimensional currents and deduces
it (Proposition 10.7). With (a) and (b) the gauge vector decays and h = h_RW + pi_X with it -- his Theorems 2.5 and
2.4(1) in five dimensions, for the class at l >= 2 (10.10). Nothing of this section is proved: (10.27)-(10.33) are
computed, exactly, at the sample points stated; the three-region bounds are deduced from them by his argument; (a) is
deduced in 10.9 for l >= 2 and (b) in 10.10.

### 10.8 The l = 0 sector: [Hun19] Theorem 8.1 in five dimensions (`lzero5.py` Z1-Z5; D50)

The l = 0 part of a perturbation in the class is h_0 = c K + pi_W (Proposition 10.1(i): a change of mass and a pure
gauge part), and in harmonic gauge h_0 = c K* + pi_{W'} with box W' = 0, since Gamma[K*] = 0 and Gamma[pi_W'] = box W'
(Proposition 10.2(i), (iv)). What [Hun19] section 8 proves in four dimensions is that such a W' converges to c_1(oo) W*,
W* the stationary one-form regular at the horizon ((10.2) here), so that h_0 settles to c K* + c_1(oo) pi_{W*}, the mass
change growing linearly in t (his Theorems 8.1 and 8.7). The identities his argument rests on are computed here in five
dimensions; the argument itself is his, transcribed; and the two estimates it feeds on are named at the end.

*Setting.* W = W0 dt + f^-1 W1 dr spherically symmetric with box W = 0 on the exterior; S_W := tr pi_W = 2 div W, P :=
r (dW)_tr - 2 W0 (his P_even = r (dW)_tr - W0: the coefficient of W0 is the one value for which box_s P is a multiple of
d_t S_W, Z2), W3 := f^-1 (W1 - W0), the dr-component in the ingoing chart and regular at the horizon; box_s := -f^-1
d_t^2 + f d_r^2 + ((3 r^2 - mu)/r^3) d_r the wave operator at l = 0; L' = f^-1 (d_t - f d_r); u := t - r_* + const with
u = tau for r >= R_null; eta_b the cut-off of [Hun19] p. 29, 0 on [r_h, b r_h] and 1 on [2 b r_h, oo), b r_h >= 2 R_null.

*What is computed (Z1-Z5, exact, sympy; the one-form box from W1's machinery).*
 (Z1) His (8.2)-(8.3): (box W)_t = box_s W0 + (4 mu/r^4) W0 + (2 mu/r^4) P and f (box W)_r = box_s W1 - (3/r^2)(1 - 3
      mu/r^2) W1 - (mu/r^3) S_W; so box W = 0 reads
          box_s W0 + (4 mu/r^4) W0 = -(2 mu/r^4) P,   box_s W1 - (3/r^2)(1 - 3 mu/r^2) W1 = (mu/r^3) S_W      (10.23)
      (four dimensions: 2M/r^3 for 4 mu/r^4 and 2 mu/r^4, (2/r^2)(1 - 4M/r) and M/r^2).
 (Z2) His (8.4)-(8.5): modulo box W = 0, box_s P = d_t S_W and box_s S_W = 0.
 (Z3) His (8.9)-(8.12): P = r d_t W3 + r L' W0 - 2 W0; S_W = -2 L' W0 + 2 f d_r W3 + (6/r) W0 + (6/r)(1 - mu/(3 r^2)) W3;
      the W3 equation
          box_s W3 - f' L' W3 - (3 f/r^2) W3 - (3/r^2) W0 = 0,   f' = 2 mu/r^3,                                (10.24)
      his (8.11) with 2M/r^2 -> f' and 2 -> 3, the coefficient of nabla_L' W3 positive -- the red-shift sign his (8.34)
      needs; and d_t W0 = (r f/4) d_r S_W - (1/2) d_t P (his (8.12) with r f/2 and 1). On the horizon f d_r = d_t along
      the generator (W0, W3, P and S_W being the regular components in (v, r)), so W0 + P/2 - (sqrt mu/4) S_W is constant
      along H^+ -- deduced from (8.12), not a check of Z3 -- and his c_1(oo) is
          c_1(oo) := mu (W0 + P/2 - (sqrt mu/4) S_W)|_{H^+}                                                    (10.25)
      (his -2M (M S_W - P_even - W0)|_{H^+}).
 (Z4) The two radial ODEs. At fixed tau, (10.23)'s first line is f d_rho^2 W0 + ((3 r^2 - mu)/r^3) d_rho W0 + (4 mu/r^4)
      W0 = O_2 in the (tau, rho) coordinates of his (2.3), O_2 the terms in P and d_t W0 (his (8.14)-(8.15)); the
      homogeneous solutions are W_{0,1} = 1/r^2, regular, W*'s dt-component, and W_{0,2} = 1 + (mu/r^2) log(r^2/mu - 1),
      singular at the horizon (his 1/r and 1 + (2M/r) log(r/2M - 1)), with Wronskian a constant times 1/(r^3 f). And
      S_W = 0 with W0 = c_1/r^2 and a stationary W3 is 2 f W3' + (6/r)(1 - mu/(3 r^2)) W3 = -2 c_1/r^3 (his (8.24)), with
      the homogeneous solution 1/(r^3 f), singular (his 1/(r^2 f)), and the regular particular solution -c_1/(r (r +
      sqrt mu)), which at c_1 = 1 is W*'s own W3 = f^-1 (sqrt mu/r^3 - 1/r^2) (W2); his particular solution -c_1/r is
      replaced by this one, and the coefficient d(tau) of the singular solution is defined against it.
 (Z5) His substitution (8.6), P-hat := P + eta_b (u + r) S_W/2: where eta_b = 1, modulo box_s S_W = 0,
          box_s P-hat = -(mu/(r^2 f)) nabla_L S_W - (mu/(2 r^3)) S_W,                                         (10.26)
      the d_t S_W of (Z2) cancelled: the source has the weights s^-2 f^-1 nabla_L S_W and mu^-1/2 s^-3 S_W where his
      Lemma 8.3 has s^-1 nabla_L S_W and M^-1 s^-2 S_W -- the same coefficient 1/2, better weights.

*What is deduced: his argument on these identities.* With (10.23)-(10.26) in place of (8.2)-(8.12), (8.14), (8.16),
(8.24) and (8.6), [Hun19] section 8.2 goes through line by line: W0 = c_1(tau) W_{0,1} + c_2(tau) W_{0,2} + O_3 by
variation of parameters from the Wronskian, the coefficients read off at rho = 2 r_h (his 4M) and their tau-derivatives
expressed through O_1 := (r f/4) d_r S_W - (1/2) d_t P; d_tau W3 = c_2(tau)/(r^3 f) + O_4 from (Z3)'s P (his (8.23) with
1/(r f) replaced by 1/(r^3 f), the W3 ODE's singular solution); c_2(tau) = (r^3/2)·O_6-type from the tau-derivative of
(10.24), so c_2 -> 0 when the O_j do; W3 = -c_1(tau)/(r (r + sqrt mu)) + d(tau)/(r^3 f) + O_10 from (Z4)'s ODE; W-bar_0
:= W0 - c_1(tau)/r^2 and W-bar_3 := W3 + c_1(tau)/(r (r + sqrt mu)) solve (10.23)'s first line and (10.24) with sources
O_11, O_12 in P and the O_j; the red-shift current (8.34) on (W-bar_0, W-bar_3), whose horizon divergence is coercive
because the coefficient of nabla_L' in (10.24) is f' > 0 (his "the coefficient of nabla_L' W_{l=0} in box W_{l=0} is
non-negative"), gives the integrated decay of d(tau) and d'(tau) and of W_{l=0} near the horizon, the singular 1/(r^3 f)
being what the current sees; and c_1(tau) converges by (10.25). Every step is an identity of (Z1)-(Z5), the divergence
theorem on a current whose coercivity is the sign in (10.24), or an ODE in rho with the solutions of (Z4); the constants
are not tracked and the O_j are bounded, as in his Appendix B, by sup norms of (sqrt mu d)^{<= m} P and S_W on [r_h <
r_underline, R_null], which the spherical symmetry turns into energy norms. So: **if S_W and P-hat decay as in his
Propositions 8.2 and 8.4, W' converges to c_1(oo) W* at his rate (1 + tau/sqrt mu)^(-2+2 delta) in the energy of (sqrt mu
d)^{<= 1} W-hat on Sigma''_tau, W-hat := W' - c_1(oo) W*, and h_0 settles to c K* + c_1(oo) pi_{W*}** (his Theorem 8.7),
the five-dimensional analogue of his Theorems 1.3-1.4 that Proposition 10.2(iv) left conditional.

*What it feeds on, and is not proved here.* Two estimates for the free scalar wave equation at l = 0 on five-dimensional
Tangherlini, his Propositions 8.2 and 8.4: (a) for S_W, with box_s S_W = 0, the decay (1 + tau/sqrt mu)^(-4+p+delta) of
F + E^{p,(0)}_L for p up to 4 - delta -- his Proposition A.6(1), Angelopoulos-Aretakis-Gajic's extended hierarchy; (b)
for P-hat, with the source (10.26) and its cut-off terms on [b r_h, 2 b r_h], where (u + r) S_W carries a factor (1 +
tau/sqrt mu) that (a)'s rate pays, his Proposition A.6(2). Neither is in 10.6: Propositions 10.4-10.5 are stated at k^2
>= 8, where the Morawetz bulk borrows the angular term, and at l = 0 there is none to borrow -- the Morawetz multiplier
for the l = 0 free wave is a separate choice ([Sch13] makes it in every dimension), and the extension of the hierarchy
past p = 2 is the rapid-decay input the growing source of 10.7 needs as well. The radiation field at l = 0 has V_inf =
3/4 (W8(h)), not zero as in four dimensions, so the Newman-Penrose constant that his Proposition A.6 assumes to vanish
has no five-dimensional counterpart at this order. 10.9 computes what the extension past p = 2 meets in five dimensions:
at l >= 2, and for Sigma at l >= 1, it goes through (Proposition 10.6), at l = 0 it is obstructed (H4), so (a) here is
open in a stronger sense -- his route does not supply it. 10.11 supplies weaker forms of (a) and (b) -- the same
commutator with a Hardy absorption, S_W at (1 + tau/sqrt mu)^(-3+p+3 delta) for p <= 2 - delta where his rate is (1 +
tau/M)^(-4+p+delta) up to p = 4 - delta -- re-runs his Appendix B at the weaker rate, and with them discharges the
conditional at that rate, (1 + tau/sqrt mu)^(-1+4 delta) for h_0 in place of his (1 + tau/M)^(-2+2 delta).

### 10.9 The first rungs' rapid decay: [Hun19] Proposition A.5 in five dimensions, and l = 0 (`hierarchy5.py` H1-H4; D51)

10.7 charges the sources of the barred rungs with a factor (1 + tau/sqrt mu)^2 on [b r_h, 2 b r_h], which the rate of
Propositions 10.4-10.5, (1 + tau/sqrt mu)^(-2+p+delta), cannot pay. [Hun19] pays it with Proposition A.5 at k = 1 (his
Propositions 5.2 and 5.4: S = tr h and r^-1 psi_Z decay at (1 + tau/M)^(-4+p+3 delta)), the r^p hierarchy of
Angelopoulos-Aretakis-Gajic extended past p = 2 by one commutation with f^-1 r^2 nabla_L, under the conditions
(A.7)-(A.9) on the potential; and at l = 0 with Proposition A.6(1), the hierarchy to p < 4 when the Newman-Penrose
constant vanishes (his Proposition 8.2). This section computes the five-dimensional form of the commuted equation, of
the current it enters and of each condition, for the first rungs Sigma = tr h (box_l Sigma = 0) and phi (box_l phi =
V_phi phi, (10.30)), states what follows by his argument, and finds the l = 0 case obstructed.

*Setting.* u a scalar mode k^2 = l(l + 2) with box_l u = V u, V = 0 (Sigma) or V = V_phi (phi); Psi := r^(3/2) u its
radiation field, with L Lbar Psi = -f Vcal Psi, Vcal = k^2/r^2 + V + (3/4 + 9 mu/(4 r^2))/r^2 and V_inf = k^2 + 3/4 =
(l + 1/2)(l + 3/2) (M4; L = d_t + f d_r, Lbar = d_t - f d_r); F, B, E^{p,(0)}_L as in 10.5-10.6, whose radiation field
Phi^(0) := s^(3/2) u is mu^(-3/4) Psi, a constant the linear identities below do not see. The commuted field is
    Psi_1 := f^-1 r^2 nabla_L Psi
(his (2.4)'s Phi^(1) with M s^2 read as r^2), in 10.5's normalisation Psi_1 = mu^(5/4) Phi^(1) with Phi^(1) := sqrt(mu)
f^-1 s^2 nabla_L Phi^(0) (his M s^2 read as sqrt(mu) s^2), E^{p,(1)}_L[u] := mu^2 int s^p |nabla_L Phi^(1)|^2 ds (his
(2.19) at j = 1), and
    I^(1)[u] := I^(0)[T^{<= 2} u] + k^2 I^(0)[T^{<= 1} u] + k^4 I^(0)[u]
                + (E^{2-delta,(1)}_L[T^{<= 2} u-tilde] + k^2 E^{2-delta,(1)}_L[T^{<= 1} u-tilde]
                   + k^4 E^{2-delta,(1)}_L[u-tilde])(0),
his (2.23) at k = 1 read as Proposition 10.5 reads it at k = 0.

*What is computed (H1-H4, exact, sympy).*
 (H1) The commuted equation. For a symbolic radial potential V,
          L Lbar Psi_1 = -(2/r)(1 - 2 mu/r^2) nabla_L Psi_1 - f Vcal_1 Psi_1 + f (9 mu/(2 r^3) - r^2 V' - 2 r V) Psi,
          Vcal_1 = Vcal - 2/r^2 + 12 mu/r^4,   V^(1)_inf := lim r^2 Vcal_1 = k^2 - 5/4 = (l - 1/2)(l + 5/2),    (10.34)
      exactly: the angular coefficient shifts by -2, his j(j + 1) at j = 1; the Psi term, the "bad term" of his account
      of [2], is (9 mu f/(2 r^3)) Psi for V = 0, free of k; and a first-order term appears. In four dimensions the same
      computation on r psi gives Vcal_1 = l(l + 1)/r^2 + V^(1) exactly, his V^(1) of the definition before (A.7), whose
      -2/r^2 is the datum (A.8) reads and Lemma 5.3 verifies: his V^(j) is counted from V, the radiation field's own
      2M/r^3 being its j = 0 term, so his 14 M/r^3 is the 12 M/r^3 by which Vcal_1 exceeds Vcal - 2/r^2, with that
      2M/r^3. Beside it stand the first-order term -(2/r)(1 - 3M/r) nabla_L Phi^(1), which his sentence that r^-1 (r^2
      L)^k (r psi) "behaves like a solution of (A.2) with potential V^(k)" does not print and which enters the current
      with a good sign (H2), and the Psi term f (2M/r^2 - r^2 V' - 2 r V) Phi^(0) (READ, H1).
 (H2) The current. For J^p of (10.7) built on Psi_1 with V^(1)_inf, the divergence taken with the measure r^3,
          div J^p[Psi_1] = r^(p-4) f^-2 (p f/2 + 2 - 5 mu/r^2) |nabla_L Psi_1|^2 + ((2 - p)/2) r^(p-6) V^(1)_inf Psi_1^2
                           + r^(p-3) f^-1 nabla_L Psi_1 . ((Vcal_1 - V^(1)_inf/r^2) Psi_1 - f^-1 C Psi),      (10.35)
      C the coefficient of Psi in (10.34): the first-order term adds 2 (1 - 2 mu/r^2) to the |nabla_L Psi_1|^2
      coefficient, which is then positive for r^2 > (10 + p) mu/(4 + p), at most 5 mu/2, on every p in [0, 2] -- the
      commuted hierarchy does not need p > 0 for its first term, the gain [2] is known for; and the Psi_1 nabla_L Psi_1
      term is div((1/2) h Psi_1^2 L) - (1/2) Psi_1^2 r^-3 d_r(r^p (Vcal_1 - V^(1)_inf/r^2)), h := r^(p-3) f^-1 (Vcal_1 -
      V^(1)_inf/r^2), so that the Psi_1^2 bulk is r^(p-6) B_1 with
          B_1 := ((2 - p)/2) V^(1)_inf - (1/2) r^(6-p) r^-3 d_r(r^p (Vcal_1 - V^(1)_inf/r^2)).
 (H3) His conditions in five dimensions. For Sigma, B_1 = ((2 - p)/2)(k^2 - 5/4) + (57/8)(4 - p) mu/r^2 exactly, positive
      on the whole exterior for p in [0, 2] and l >= 1: (A.7) at j = 1 with no R_null needed. For phi, B_1 = ((2 -
      p)/2)(k^2 - 5/4) + (mu/r^2) Q_1(k^2, mu/r^2, p)/H^3 with Q_1 a polynomial (H = k^2 - 3 + 6 mu/r^2), and B_1 >=
      (1/4)(2 - p)(k^2 - 5/4) for r >= R_1: R_1 = 8.14 r_h at k^2 = 8 and R_1 = r_h at k^2 = 24, 48, 80, over p in [1/10,
      19/10] on a grid of 21 values, complete because B_1 - (1/4)(2 - p)(k^2 - 5/4) is affine in p -- the computation of
      his Lemma 5.3 for R_Z. The base bulk, (A.5), is B_0 = ((2 - p)/2)(k^2 + 3/4) + (9/8)(4 - p) mu/r^2 for Sigma
      (positive everywhere) and for phi holds with the same room for r >= R_0 = 10.56, 4.61, 3.04, 2.29 r_h at the four
      modes. (A.8): V^(1)_inf = k^2 - 5/4, 7/4 at l = 1 and 27/4 at l = 2, positive for l >= 1. (A.9): r^4 |V_phi|/mu <=
      12 (k^2 + 3)/(k^2 - 3) and r^3 |d_r(r^2 V_phi)|/mu <= 24 (k^2 + 3)/(k^2 - 3) on the exterior, exactly, the suprema
      attained at infinity -- 26.4 and 52.8 at k^2 = 8, 12.9 and 25.9 at k^2 = 80 -- and bounded uniformly in l as V_phi
      -> -12 mu/r^4 (k -> oo; his lim V_Z = -8 M/r^3). (A.3): r^2 (k^2/r^2 + V_phi) decreases in mu/r^2, so its minimum
      is the horizon's value, 4/11 at k^2 = 8 (124/9, 628/17, 5692/83 at the other modes), exactly: phi's T-energy
      density is non-negative, with 4.5 % of room at l = 2 where the Maxwell rung has half (M3), and the bound fails at
      k^2 = 3, the l = 1 mode the scalar sector does not contain. (A.4), the Morawetz multiplier for V_phi, is [HKW18]'s
      (their decay of the master quantity, which Proposition 10.1(iv) cites) and is not re-derived.
 (H4) l = 0. There V_inf = 3/4 and V^(1)_inf = -5/4: (A.8) fails for the commuted potential, and the base bulk B_0 =
      (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 is negative for every p > 2 once r^2 > 3 (4 - p) mu/(p - 2), so the hierarchy
      of S_W stops at p < 2. In four dimensions V_inf = 0 at l = 0 and the Psi^2 bulk is (3 - p) M r^(p-6), positive to
      p = 3: the room his Proposition A.6(1) uses, with the Newman-Penrose constant for p up to 4. The obstruction is the
      odd dimension: the radiation field r^(3/2) u carries (3/4)/r^2 at l = 0 where r psi carries nothing.

*What is deduced.*

**Proposition 10.6 (rapid decay of the first rungs; deduced from H1-H3, the currents of Propositions 10.3-10.5 and
[Hun19] Proposition A.5's argument; constants not tracked).** Let u solve box_l u = V u at a mode l >= 2 of the class,
with V = 0 or V = V_phi, and for V_phi let the Morawetz estimate of [HKW18] for the master equation be given as
Proposition 10.1(iv) reads it. Then for p in [delta, 2 - delta] and tau >= 0,
    (F[u] + E^{p,(0)}_L[u-tilde])(tau) + mu^-1/2 int_tau^oo (B[u] + E^{p-1,(0)}_L[u-tilde])(tau') dtau'
        <= C (1 + tau/sqrt mu)^(-4+p+3 delta) I^(1)[u].                                                        (10.36)

*Proof, his.* (i) The base hierarchy for Psi, Proposition 10.4 at G = 0 (for V_phi, [HKW18] Theorem 18), gives
E^{p,(0)}_L decaying as (1 + tau/sqrt mu)^(-2+p+delta). (ii) The commuted hierarchy: J^p[Psi_1] on D(tau_1, tau_2) cap {r
>= R_null} with (10.35), R_null >= R_1: the bulk is at least c (E^{p-1,(1)}_L + int s^(p-6) Psi_1^2) by H2-H3; the bad
term r^(p-3) f^-2 |C nabla_L Psi_1 Psi| with C = O(mu/r^3) is <= epsilon r^(p-4) |nabla_L Psi_1|^2 + C_epsilon mu^2
r^(p-8) Psi^2, and mu^2 r^(p-8) Psi^2 <= (mu/R_null^2) mu r^(p-6) Psi^2 is the base bulk at the same p -- the absorption
he credits to [2]'s Poincare inequality, which at a fixed mode is this weight count; the cut-off terms on [R_null,
R_null + r_h] are controlled by the Morawetz bulk as in Proposition 10.3's Step 1. So E^{p,(1)}_L[u-tilde](tau_2) + int
E^{p-1,(1)}_L <~ E^{p,(1)}_L[u-tilde](tau_1) + (base terms), and the dyadic argument of [HKW18] Theorem 18 gives
E^{p,(1)}_L decaying as (1 + tau/sqrt mu)^(-2+p+delta). (iii) The step between the levels: nabla_L Phi^(0) = mu^(-1/2) f
s^-2 Phi^(1), so E^{2,(0)}_L[u-tilde] = mu int f^2 s^-2 |Phi^(1)|^2 ds <= 4 mu int |d_s Phi^(1)|^2 ds = 4 mu^2 int f^-2
|nabla_L Phi^(1)|^2 ds <= 4 (100/99)^2 E^{0,(1)}_L[u-tilde], by the Hardy inequality on the null leaf (the cut-off field
vanishing at R_null; d_s = sqrt(mu) f^-1 nabla_L along the leaf, f >= 99/100 there) -- his Lemma 3.2 with the same
exponents, 2 at level 0 and 0 at level 1, because 10.5's Phi^(0) = s^(3/2) u is the radiation field of the
five-dimensional measure. (iv) With (ii)-(iii) the base hierarchy restarts from E^{2-delta,(0)}_L decaying as tau^(-2+2
delta), and its own dyadic argument gives (10.36): his (A.11) at k = 1, the three deltas being the two hierarchies' and
the interpolation's. For Sigma, l >= 1 suffices (V^(1)_inf = 7/4 > 0 at l = 1).

*What this gives 10.7.* With (10.36) for Sigma and phi, 10.7's three-region bound closes as his Lemma 5.5: the middle
region's (1 + tau/sqrt mu)^2 spends 2 of the 4, and I_source[G] of each hatted rung is bounded with (1 + tau/sqrt
mu)^(-2+p+3 delta), his accounting exactly, at every mode l >= 2 of the class. 10.7's item (a) is done for l >= 2, as
his Proposition A.5 does it, and with the same reservation: the argument is his, transcribed onto (10.34)-(10.35) and
H3's conditions, deduced and not proved here.

*What remains, and is not done here.* Two items. The l = 0 sector: his Proposition 8.2 (S_W at (1 + tau/M)^(-4+p+delta),
p < 4 - delta) rests on Proposition A.6(1), that is on V_inf = 0 at l = 0, which is false in five dimensions (H4). What
his route supplies for S_W here is Propositions 10.4-10.5's (1 + tau/sqrt mu)^(-2+p+delta) and nothing more: the
commutation that rescues l >= 1 has V^(1)_inf = -5/4, and the base hierarchy stops at p < 2. So the conditional of 10.8
("if S_W and P-hat decay as in his Propositions 8.2 and 8.4") is not discharged by his method, and the five-dimensional l
= 0 sector is open in a stronger sense than 10.7 said: either a different commutator at l = 0 in odd dimension (the
five-dimensional l = 0 wave has the tail t^-3 by [CYDL03], so the faster decay is expected and the obstruction is the
method's), or his Appendix B's O_j bounds re-run with the weaker rate, which is not examined here. 10.11 takes the
second, with the same commutator rather than a different one: V^(1)_inf = -5/4 is absorbed by a Hardy inequality on the
leaf for p < 1, and his Appendix B is re-run at the weaker rate. And (b) of 10.7, the coupled estimate for (X_1-hat,
X_L-hat), which 10.10 deduces. Nothing of this section
is proved: (10.34)-(10.35) and H3-H4 are computed, exactly and at the modes stated; Proposition 10.6 is deduced by his
argument; l = 0 is 10.11's, and (b) is 10.10's.


### 10.10 The coupled estimate: [Hun19] section 6 in five dimensions (`coupled5.py` K1-K6; D52)

10.7's item (b). The last two components of the gauge vector, X := (X_1-hat, X_L-hat) with X_1 := f X_r, solve a coupled
system with the zeroth-order matrix of (10.29) and the sources G of 10.7: with box_s := -f^-1 d_t^2 + r^-3 d_r(r^3 f d_r)
and x := mu/r^2,
    box_s X = V X + G,   V := (k^2/r^2) I + A,   A := (1/r^2) [[3 (1 - 3x), 2k (1 - 2x)], [2k, -(1 + x)]],     (10.37)
[Hun19]'s (6.1) W = A_W W + G. His section 6 estimates such a pair by four currents -- the T-energy, the red-shift, the
Morawetz and the r^p current -- with the non-self-adjoint part of A_W handled in the compact region by the identities
(6.8)-(6.10), which express derivatives of W through quantities sections 4-5 already control. This section computes the
five-dimensional form of the identities and of three of the currents, the T-energy, Morawetz and r^p ones -- the
red-shift current is deduced, not computed -- and finds the Morawetz bulk positive without his substitutions.

*What is computed (K1-K6, exact, sympy).*
 (K1) The identities. For the scalar-type one-form of Proposition 10.2(iii), with W6's S = div X, P = (dX)_tr/S, Q_t and
      Q_r,
          d_r X_1 + (3/r) X_1 + (k/r) X_L = S + f^-1 d_t X_t =: F_1,
          f d_r X_L + (f/r) X_L + (k/r) X_1 = (k f/r) Q_r =: F_2,
          d_t X_1 = f (P + d_r X_t) =: F_3,
          d_t X_L = (k/r)(Q_t - X_t) =: F_4,                                                                   (10.38)
      with Q_r = (r^2/k^2)(d_r S - f^-1 d_t P - J_r) and Q_t = (r^2/k^2)(d_t S - (f/r^3) d_r(r^3 P) - J_t) under box X =
      J (W6, re-run): his (6.8), (6.9), (6.10), and a fourth, d_t X_L, that his list does not have. Both time derivatives
      and both radial derivatives of the pair are zeroth order in it modulo S, P, X_t and J -- the rungs below it and the
      master field. They hold for the unhatted pair, which is the hatted one on [r_h, b r_h].
 (K2) The pair's matrix. r^2 V tends to [[k^2 + 3, 2k], [2k, k^2 - 1]], whose eigenvalues at k^2 = l(l + 2) are (l + 1)(l
      + 3) and (l - 1)(l + 1), the flat decomposition into the modes l +- 1: positive definite for every mode of the
      class, the least 3 at l = 2. Hung's leading matrix [[Lambda + 2, -2 sqrt Lambda], [-2 sqrt Lambda, Lambda]] has (l
      + 1)(l + 2) and l(l - 1), the eigenvalues {0, 6} at l = 1 that his p. 40 calls "only semi-positive definite"
      (READ). The antisymmetric part of A is (k mu/r^4)[[0, -2], [2, 0]]; A_12 = 2k(1 - 2x)/r^2 vanishes and changes sign
      at the photon sphere r^2 = 2 mu, as his 1 - 3M/r does at r = 3M, so no diagonal rescaling symmetrises A.
 (K3) The T-current. For C = diag(c_1, c_2) and N symmetric, J := sum_i c_i T[X_i](d_t, .) - (1/2)(X.N.X) g(d_t, .) has
      div J = d_t X.(C V - N) X + d_t X.C G. Take C = diag(10, 1) and N_in := [[10 V_11, V_21], [V_21, V_22]] on [r_h,
      R_T], where C V - N_in = [[0, 10 V_12 - V_21], [0, 0]] exactly and the error is d_t X_1 (10 V_12 - V_21) X_L -- the
      time derivative of X_1 only, which is F_3 -- and C = I, N_ex := [[V_11, V_12], [V_12, V_22]] beyond, where V - N_ex
      = [[0, 0], [V_21 - V_12, 0]] and the error is (4 k mu/r^4) d_t X_L X_1 (Hung's J_1,1 + J_1,2 weighs T[W_1] by 1 + 9
      and T[W_2] by 1 + 1, his (6.17)-(6.18), READ; here the weight 1 on X_L suffices); a radial weight c_1(r), the join
      on [R_T, 4 R_T], adds c_1' f d_r X_1 d_t X_1, again in d_t X_1 alone; N_in >= (k^2/4) r^-2 I on the whole exterior
      and N_ex >= (k^2/4) r^-2 I for r^2 >= 2 mu, for every real k^2 >= 8 (exact: each determinant a polynomial in (x,
      k^2) whose coefficients in powers of k^2 - 8 are positive on the interval, by Sturm sequences). With c_1 = 1, N_in
      is indefinite at the horizon at k^2 = 8 (the control): the weight is needed, as in four dimensions.
 (K4) The Morawetz current for a pair: for M symmetric and box_s X = V X + G with V arbitrary, J := T(F d_r*, .) + (1/4)
      omega d|X|^2 - (1/4)(d omega)|X|^2 + F' beta |X|^2 dr*, T built with X.M.X, has
          div J = (dF/dr) |f d_r X + beta X|^2 + X.W_M.X + (F f d_r X + (omega/2) X).((V - M) X + G),
      W_M := s_0 I - (1/2) F f M' - (mu/r^3) F M, s_0 the scalar part of rungs5's W0 -- M1 for a system; and the
      g-current of M5 likewise, with X.V.X = X.sym(V).X.
 (K5) The Morawetz bulk is positive outright. With M = sym(V) and rungs5's F and beta = 1/(2 sqrt mu), the cross term F f
      d_r X.(V - M) X is -(2 k mu F/r^4)(X_L Y_1 - X_1 Y_L), Y := f d_r X + beta X, exactly (the beta parts cancel by
      antisymmetry), and completes into the first term at the cost (k^2 mu^2 F^2/((dF/dr) r^8))|X|^2. Keeping a tenth of
      the angular term k^2 F (1 - 2 mu/r^2)/r^3 for the bulk's angular control,
          W_rest := W_M - (1/10)(k^2 F (1 - 2 mu/r^2)/r^3) I - (k^2 mu^2 F^2/((dF/dr) r^8)) I >= (1/40) r^-3 I
      on the whole exterior for every real k^2 >= 8, exactly: in y = sqrt(mu)/r, r^3 W_rest - I/40 = [[p_1 + e k^2, k q],
      [k q, p_2 + e k^2]] with e >= 0 (a double zero at the photon sphere), p_i + 8e > 0, and the determinant's
      coefficients in k^2 - 8 non-negative, the constant one positive and the linear one with a double zero at the photon
      sphere (Sturm on the numerators, the photon-sphere factor divided out). The completion cost is at most 35/13 of the
      kept tenth, uniformly in k: their ratio is 50 x (1 - x/2 + x^2/5)/(25 - 24 x + 12 x^2), increasing in x to its
      value at the horizon. At l = 2 the least eigenvalue of r^3 W_rest has its minimum 0.0352 at r = 1.261 r_h; keeping
      half of the angular term instead fails at l = 2 (the control). Hung needs (6.8)-(6.9) on [2M, bM] -- his matrices
      M_[2M,bM] and the polynomials p_1, p_2, p_3 -- because his pair is only semi-definite at l = 1; in five dimensions
      the class starts at l = 2, where the pair is definite, and the substitution is not needed for positivity.
 (K6) The r^p current. Psi := r^(3/2) X solves L Lbar Psi = -f Vcal Psi - f r^(3/2) G, Vcal = V + (3/4 + 9 mu/(4 r^2))
      r^-2 I, with V_inf := lim r^2 Vcal = [[k^2 + 15/4, 2k], [2k, k^2 - 1/4]], eigenvalues (l + 3/2)(l + 5/2) and (l -
      1/2)(l + 1/2), positive definite; sym(Vcal) - V_inf/r^2 = O(mu/r^4) and the antisymmetric part is (k mu/r^4) [[0,
      -2], [2, 0]]. So (10.7) holds for the pair with V_inf positive definite, as W8d has it for h's components.

*What is deduced.*

**Proposition 10.7 (the coupled estimate; deduced from K1-K6, Propositions 10.4-10.6, 10.7's sources and [Hun19] section
6's argument; constants not tracked).** Let X = (X_1-hat, X_L-hat) solve (10.37) at a mode l >= 2 of the class, with G
the sources of 10.7. For p in [delta, 2 - 3 delta] and tau >= 0,
    (F[X] + E^{p,(0)}_L[X-tilde])(tau) + mu^-1/2 int_tau^oo (B-bar[X] + E^{p-1,(0)}_{L,ang}[X-tilde])(tau') dtau'
      <= C (1 + tau/sqrt mu)^(-2+p+3 delta) Decay[X],   C independent of l,                                 (10.39)
Decay[X] := (F[X] + E^{2-delta,(0)}_L[X-tilde])(0) + I_{source,3 delta}[G] + I^(0)[k^{<= 1} T^{<= 1} (X_t-hat, r
P-hat)] + mu (I^(0)[(sqrt mu d)^{<= 1} k^{<= 1} S] + I^(1)[k^{<= 1} Sigma, k^{<= 3} phi]), his Decay[W] with Q_even's
place taken by K1's F_2, F_4.

*Proof, his.* (i) The T-current of K3, the two choices joined at R_T >= 2 R_null by Hung's cut-off eta_T on [R_T, 4 R_T]:
its flux is comparable to the T-energy, by K3's lower bounds; the inner error d_t X_1 (10 V_12 - V_21) X_L lives on [r_h,
4 R_T], inside [r_h, b r_h] where the pair is unhatted, and there d_t X_1 = F_3 by (10.38), so |error| <= epsilon r^-3
|X|^2 + C_epsilon k^2 r^-1 |F_3|^2: the first is K5's bulk, the second the rungs P and X_t with one angular derivative;
the outer error (4 k mu/r^4) d_t X_L X_1 decays like r^-4 and is absorbed by the r^p bulk for R_T large, as his 6.5
absorbs 6M/r^2 nabla_t W_2 D_1* W_1. The join's cut-off adds c_1' f d_r X_1 d_t X_1 on [R_T, 4 R_T] (K3), c_1 the first
weight, 10 inside and 1 outside -- again d_t X_1 = F_3 alone -- and there C V - N is the convex combination of the two
errors while N stays >= (k^2/4) r^-2 I; all of it lies in [r_h, b r_h], where the pair is unhatted, once b r_h >= 4 R_T,
b being fixed after R_T as in his 6.5, whose estimate uses [2M, 4 R_T] inside [2M, bM]. (ii) The red-shift current: the
pair is regular at the horizon (X_1 = X_t + f X_R in the ingoing chart, X_L an angular component) and (10.37) has bounded
zeroth-order coefficients and no first-order term, so [HKW18] Lemma 11's red-shift estimate "for any bounded radial
potential" applies componentwise, the coupling being lower order -- deduced, as in Proposition 10.4, not computed. The
coefficients are bounded at each mode, A_12 and A_21 being of order k/r^2; uniformity in l needs the k-linear coupling
absorbed by the red-shift current's angular term, as Proposition 10.3's Step 2 absorbs the terms of Acal of degree one in
k. (iii) The Morawetz current: K4-K5 give a bulk at least c ((dF/dr)|Y + c'(r) J X|^2 + (1/10) k^2 F (1 - 2 mu/r^2) r^-3
|X|^2 + r^-3 |X|^2/40), J X := (X_L, -X_1) and c'(r) := -k mu F/((dF/dr) r^4), the zeroth-order part non-degenerate
everywhere, and the g-current of K4 adds |d_t X|^2 away from the photon sphere as M5 does. The angular and time
derivatives degenerate at r^2 = 2 mu, as for the scalar rungs; Hung removes the degeneracy with (6.8)-(6.9), and here
(10.38) does the same, with one identity more and uniformly in l: the completed square bounds (dF/dr)|f d_r X|^2 by
itself, 3 (dF/dr) beta^2 |X|^2 and three times the completion cost, which is at most 35/13 of the kept tenth of the
angular term (K5); then (k/r) X_L = F_1 - d_r X_1 - (3/r) X_1 and (k/r) X_1 = F_2 - f d_r X_L - (f/r) X_L bound the
angular term k^2 r^-2 |X|^2 near r_P, and d_t X_1 = F_3, d_t X_L = F_4 the time derivatives, so B-bar, the non-degenerate
bulk, is bounded by K5's bulk plus the F's, at the price of the rungs' derivatives, with a constant independent of l.
(iv) The r^p current: K6 with (10.7), V_inf positive definite; the remainders O(mu/r^4) and the antisymmetric term
r^(p-3) nabla_L Psi . E Psi <= epsilon r^(p-4)|nabla_L Psi|^2 + C_epsilon k^2 mu^2 r^(p-10) |Psi|^2 are absorbed for r >=
R_W, as his A_W,sub is. (v) His 6.5: C_1 J_1 + epsilon_2 J_2 + J_3 + epsilon_4 J^p_4 with the constants chosen in his
order, the source term Err[W, G] bounded by I_source[G], which 10.7 bounds and 10.9's rates close, the F-terms on [r_h, b
r_h] by Propositions 10.5 and 10.6 for P-hat, X_t-hat, Sigma and phi, and the dyadic argument (6.35)-(6.37) to (10.39).

*What this gives.* With 10.6 (the rungs S, X_t-hat, r P-hat, by Propositions 10.4-10.5 fed with 10.7's sources), 10.9
(the first rungs Sigma and phi at the rapid rate) and (10.39), every component of the gauge vector at every mode l >= 2
of the class decays at (1 + tau/sqrt mu)^(-2+p+3 delta); on [r_h, b r_h] the hatted components are the unhatted ones.
Then h decays as [Hun19] section 7 has it: Proposition 10.3 (his Proposition 4.1) leaves only the compact region, and
there h = h_RW + pi_X is bounded, as his Proposition 7.1 bounds it, by the master field with three derivatives ((10.1)
and [HKW18]'s decay, Proposition 10.1(iv)) and by the gauge vector with two, the bulks of (10.39), of 10.6's rungs and of
their commuted versions -- so h decays in harmonic gauge at every mode l >= 2 of the class at (1 + tau/sqrt mu)^(-2+p+3
delta), with the loss of a fixed number of derivatives: [Hun19]'s Theorem 2.4(1), the l >= 2 part of his Theorem 1.2, in
five dimensions, for the class. Route A is thereby carried through for l >= 2, every step deduced on computed identities
and none proved here.

*What remains, and is not done here.* The l = 0 sector alone: 10.9 found that his Proposition A.6 does not transcribe
(V_inf = 3/4 at l = 0 in five dimensions), so 10.8's conditional stands, and with it the final-state statement of
Proposition 10.2(iv), c_1 K* + c_2 pi_{W*}; 10.11 takes it by another route. Nothing of this section is proved:
(10.37)-(10.38) and K2-K6 are computed, exactly, for every real k^2 >= 8 where so stated and at l = 2 for K1; Proposition
10.7 is deduced by his argument, the red-shift step without a computation; l = 0 is 10.11's.

### 10.11 The l = 0 sector by another route: the commuted hierarchy with a Hardy absorption (`lzerorate5.py` Y1-Y5; D53)

10.8 reduced the l = 0 sector to two estimates for the free wave at l = 0, his Propositions 8.2 and 8.4, and 10.9 found
his route to the first obstructed: at k = 0 the commuted potential has V^(1)_inf = -5/4 (H4), so his (A.8) fails, and his
Proposition A.6(1) rests on V_inf = 0, false at l = 0 in five dimensions. (A.8) asks for more than the commuted hierarchy
uses. For p < 2 the flux of V^(1)_inf r^(p-2) Psi_1^2 at null infinity vanishes, and V^(1)_inf enters only the Psi_1^2
bulk, -(5/8)(2 - p) r^(p-6) Psi_1^2 at leading order; the commuted current's own |nabla_L Psi_1|^2 bulk, (2 + p/2)
r^(p-4) at leading order -- the 2 being the first-order term's (H2) -- pays for it through the Hardy inequality on each
outgoing leaf when (4 + p)(2 - p) > 5, that is for p < 1. So the commuted hierarchy runs at l = 0 on [delta, 1 - delta],
one step past p = 2 where his runs two. This section computes what that needs (Y1-Y5), takes the base Morawetz estimate
at l = 0 from [Sch13], and deduces the decay of S_W at (1 + tau/sqrt mu)^(-3+p+3 delta), of P-hat at (1 + tau/sqrt
mu)^(-1+4 delta), and with them 10.8's conclusion at the second rate.

*Setting.* As 10.8: h_0 = c K* + pi_{W'} with box W' = 0, S_W := tr pi_{W'} with box_s S_W = 0, P, and P-hat := P + eta_b
(u + r) S_W/2 with G_P := box_s P-hat, b r_h >= 2 R_null. As 10.9: Psi := r^(3/2) S_W, Psi_1 := f^-1 r^2 nabla_L Psi,
Phi^(0), Phi^(1), E^{p,(0)}_L and E^{p,(1)}_L. R_null >= 10 r_h, so that f >= 99/100 beyond it as in 10.9 (iii), and
R_null >= 3 r_h/delta^(1/2) when delta < 1/10. F, the non-degenerate bulk B-bar (a fixed mode loses no derivative at the
photon sphere, his p. 73) and E^p_source as in 10.6; D^{<= m} the commutators T and the red-shift vector field, the
rotations acting trivially at l = 0.

*What is READ.* [Sch13] at its spatial dimension n = 4 (his 2m is mu): Proposition 4.1, (4.4), pp. 19-20, for every
solution of box phi = 0 on the exterior, "int_{R^oo_{r_0,r_1}(t_0)} {r^-n (d phi/d r*)^2 + r^-(n+1) (d phi/dt)^2 + r^-3
(1 - 2m/r^(n-2)) |nabla-slash phi|^2} dmu_g <= C(n, m) int_{Sigma_tau_0} (J^T(phi) + J^T(T phi), n)", with "no
restriction on the spherical harmonic number" (p. 44). It holds at l = 0, and his proof shows how: Step 2
((4.90)-(4.91), p. 47) treats pi_{<L} phi, which contains l = 0, by the current J^(alpha)(phi) = J^{X_a,0}(phi) + sum_i
J^{X_b,2}(Omega_i phi) ((4.67), p. 38), whose uncommuted part, f^a solving (4.64), gives the bulk C(n - 1)/(alpha^2
r^n)(d phi/d r*)^2 at every l ((4.71), p. 39) -- only the commuted part vanishes at l = 0 -- and Corollary 4.18 (p. 43)
supplies d phi/dt through K^aux. Corollary 4.3 gives its non-degenerate form with the red-shift, Proposition 4.22 the
zeroth-order term on a timelike boundary, and Theorem 1 (1.9), p. 5, E[phi](Sigma_tau) <= C D/tau^2 by the hierarchy
(5.17) at p = 1, 2. At l = 0 this is the Morawetz estimate 10.8 found missing; it costs one T-derivative, which D^{<= m}
absorbs. [Hun19] section 8, Proposition A.6 and Appendix B as quoted in 10.8 (READ 2026-10-21, pp. 58-75), with his
remark that "our assumption E^{4-delta,(0)}_L < oo implies the Newman-Penrose constant vanishes" (p. 73).

*What is computed (Y1-Y5, exact, sympy; on hierarchy5.py's equation and current at k = 0).*

 (Y1) The l = 0 currents. At k = 0, (10.34) has Vcal_1 = -5/(4 r^2) + 57 mu/(4 r^4) and C = 9 mu f/(2 r^3), and the base
      current, with no first-order term, is

          div J^p[Psi] = r^(p-4) f^-2 (p f/2 - mu/r^2) |nabla_L Psi|^2 + ((2 - p)/2) r^(p-6) V_inf Psi^2
                         + r^(p-3) f^-1 nabla_L Psi (Vcal - V_inf/r^2) Psi,                                       (10.40)

      which (10.35)'s first-order term raises by 2 (1 - 2 mu/r^2); on an outgoing leaf of r >= R_null, where the measure
      r^3 dt dr is r^3 du dr and nabla_L = f d_r, the bulk of (10.35) after H2's integration by parts is, with w := Psi_1
      on the leaf,

          r^(p-1) c w'^2 + r^(p-3) B_1 w^2 - (9 mu/2) r^(p-3) Psi w',
          c := p f/2 + 2 - 5 mu/r^2,   B_1 = -(5/8)(2 - p) + (57/8)(4 - p) mu/r^2,                                (10.41)

      the f's cancelling exactly.

 (Y2) The Hardy step. For w vanishing at R and p < 2, d_r(r^(p-2) w^2) = (p - 2) r^(p-3) w^2 + 2 r^(p-2) w w' gives with
      Cauchy-Schwarz A := int_R^oo r^(p-3) w^2 dr <= 4 B/(2 - p)^2, B := int_R^oo r^(p-1) w'^2 dr (the identity computed;
      the constant checked on w = 1 - R/r at p = 1/2, where A/B = 8/15 against 16/9, and 4/9, half the constant squared,
      is refuted). With c_R := 2 + p/2 - (5 + p/2) mu/R^2 and Q := c_R (2 - p) - 5/2, exactly,

          c_R B - (5/8)(2 - p) A = (Q/(2 (2 - p))) B + (Q (2 - p)/8) A + kappa (4 B/(2 - p)^2 - A),
          kappa := (2 - p)(5 + Q)/8,                                                                              (10.42)

      so that by the Hardy inequality the first two terms of (10.41), integrated along the leaf, are at least (Q/(2 (2 -
      p))) B + (Q (2 - p)/8) A when Q > 0 (c >= c_R and B_1 >= -(5/8)(2 - p) on the leaf); and the third is a perfect
      square away: eps a^2 - (9/2) a b + (81/(16 eps)) b^2 = (eps^(1/2) a - (9/4) eps^(-1/2) b)^2.

 (Y3) The window. Q(p, x) = (2 + p/2 - (5 + p/2) x)(2 - p) - 5/2 has Q(p, 0) = (1 - p)(3 + p)/2, decreases in x and is
      concave in p, so its minimum over [delta, 1 - delta] x [0, x_R] is at a corner: Q(1/10, 1/100) = 25981/20000 and
      Q(9/10, 1/100) = 2701/20000 at R_null = 10 r_h, and for delta in (0, 1/10], with x_R = delta/9 (R_null = 3
      r_h/delta^(1/2)), Q(delta, delta/9) > 0 and Q(1 - delta, delta/9) = delta (25 - 19 delta + delta^2)/18 > 0. The
      window closes at p = 0.9716 at x = 1/100 and at p = 1 at x = 0. At leading order the condition is (4 + p)(2 - p) >
      -4 V^(1)_inf, which needs V^(1)_inf > -2: it is open on p < 1 at the five-dimensional l = 0 value -5/4 and empty
      at the four-dimensional one, -2 (his V^(1) at l = 0, H1), where his Proposition A.6(1) rests instead on V_inf = 0
      and a vanishing Newman-Penrose constant. Controls: R_null = 5 r_h, where Q(9/10, 1/25) < 0; p = 1 at x = 0, where Q
      = 0.

 (Y4) The base hierarchy at l = 0 borrows no angular term. B_0 = (3/8)(2 - p) + (9/8)(4 - p) mu/r^2 >= (3/8)(2 - p) > 0
      for p < 2 (H3's bulk at k = 0); and on x <= 1/100 the T-energy density of S_W on the leaf, r^3 |nabla_L S_W|^2 =
      |nabla_L Psi - (3/2)(f/r) Psi|^2, is at most 12 times the p = 1 bulk density of (10.40), f^-2 ((1 - 3 mu/r^2)/2)
      |nabla_L Psi|^2 + r^-2 B_0 Psi^2 (the 2 x 2 form positive definite, exactly): the radiation field's own (3/4)/r^2
      does at l = 0 what k^2 >= 8 does in Proposition 10.5 (iii). Dropping it leaves the form indefinite at large r (the
      control).

 (Y5) The cut-off source. For box_s S_W = 0 at l = 0, eta = eta(r) and w := u + r,

          box_s (eta w S_W/2) = (w/2)(S_W box_s eta + 2 f eta' d_r S_W) + eta (S_W box_s w/2 + grad w . grad S_W)
                                + f eta' (d_r w) S_W,                                                             (10.43)

      with box_s w = -mu/r^3 and grad w . grad S_W = -f^-1 d_t S_W - (mu/r^2) d_r S_W: where eta_b = 1, G_P is    (10.26)
      (Z5 re-derived), and the terms carrying the growing u + r are S_W and d_r S_W only, on [b r_h, 2 b r_h] -- his
      Lemma 8.3's middle line, (1 + tau/M) |(M d)^{<= 1} D^{<= m} S_W|, in five dimensions. With w = u instead, the eta_b
      = 1 source carries d_r S_W at weight 1 (the control).

*What is deduced.*

**Proposition 10.8 (the l = 0 sector; deduced from Y1-Y5, H1-H2, [Sch13] Proposition 4.1 and Theorem 1, Proposition
10.5's argument and [Hun19] section 8 with his Appendix B; constants not tracked).** Let h_0 = c K* + pi_{W'} be the l =
0 part of a perturbation in the class in harmonic gauge (10.8), fix delta in (0, 1/10] and R_null as in the setting, and
let

    I_0[S_W] := (F + E^{2-delta,(0)}_L + E^{1-delta,(1)}_L)[D^{<= 10} S_W](0),
    Decay_0[W'] := F[D^{<= 2} W'](0) + (F + E^{2-delta,(0)}_L)[D^{<= 7} P-hat](0) + mu I_0[S_W]

be finite -- no Newman-Penrose condition: E^{1-delta,(1)}_L is finite when d_r Psi_1 = O(r^-2) along the leaf, so that
Psi_1 tends at null infinity to a limit, zero or not, at the rate 1/r, where his E^{4-delta,(0)}_L < oo forces the limit
to vanish. Then for tau >= 0:

 (i) for p in [delta, 2 - delta] and m <= 8,
    (F[D^{<= m} S_W] + E^{p,(0)}_L[D^{<= m} S_W-tilde])(tau) + mu^-1/2 int_tau^oo (B-bar[D^{<= m} S_W]
      + E^{p-1,(0)}_L[D^{<= m} S_W-tilde])(tau') dtau' <= C (1 + tau/sqrt mu)^(-3+p+3 delta) I_0[S_W];            (10.44)
 (ii) for m <= 7,
    (F[D^{<= m} P-hat] + E^{delta,(0)}_L[D^{<= m} P-hat-tilde])(tau) + mu^-1/2 int_tau^oo B-bar[D^{<= m} P-hat] dtau'
      <= C (1 + tau/sqrt mu)^(-1+4 delta) Decay_0[W'];                                                            (10.45)

 (iii) W' converges to c_1(oo) W*, c_1(oo) of (10.25): the energy of (sqrt mu d)^{<= 1} W-hat on Sigma''_tau, W-hat := W'
      - c_1(oo) W*, and its integral over D''(tau, oo), normalised as in his Theorem 8.1, are at most C (1 + tau/sqrt
      mu)^(-1+4 delta) Decay_0[W']; so h_0 settles to c K* + c_1(oo) pi_{W*}, the final state of Proposition 10.2(iv).

*Proof.* (a) The base hierarchy at l = 0. [Sch13] Proposition 4.1 gives the Morawetz bulk of S_W at l = 0 with one
T-derivative on the right, Corollary 4.3 its non-degenerate form and Proposition 4.22 the zeroth-order term on the
timelike boundary r = R_null. The red-shift commutator in D^{<= m} gives Y^j S_W an inhomogeneous equation,
so for those the Morawetz step is the one with a source of (d) -- deduced, not READ. With these in place of Proposition
10.4's Morawetz step, and the current (10.40) with B_0 >
0 (Y4) in place of its angular term -- its |nabla_L Psi|^2 coefficient positive for mu/r^2 < p f/2, which x_R <= delta/9
secures -- Proposition 10.5's argument runs at l = 0, its step (iii) with Y4's domination where it borrowed k^2 >= 8, and
gives (F + E^{p,(0)}_L)[D^{<= m} S_W](tau) <~ (1 + tau/sqrt mu)^(-2+p+2 delta) I_0 for p in [delta, 2 - delta], his
Theorem 1 (1.9) with the r^p weights -- (10.22)'s rate at delta-bar = delta; the boundedness of [Sch13] Theorem 1 would
save that delta, which (c) does not need.

(b) The commuted hierarchy at l = 0. Take J^p of (10.7) on chi Psi_1, chi the cut-off vanishing at R_null and equal to 1
beyond R_null + r_h as in 10.9 (iii), on D(tau_1, tau_2) cap {r >= R_null}, p in [delta, 1 - delta]. On each leaf,
(10.41) with (10.42), the Hardy inequality (no boundary term, chi Psi_1 vanishing at R_null) and Y3's Q >= Q_0 > 0 bound
the first two terms below by (Q_0/4) B + (Q_0/8) A; the third, by the perfect square with eps = Q_0/8, costs C mu^2
r^(p-5) Psi^2 <= C mu^((2+p-delta)/2) r^(delta-3) Psi^2 (r >= R_null >= sqrt mu), the base zeroth-order bulk at level
delta, which B_0 >= (3/8)(2 - delta) puts under (a). The flux of V^(1)_inf r^(p-2) Psi_1^2 at null infinity vanishes for
p < 2, |Psi_1| <~ r^((1-p)/2) (E^{p,(1)}_L)^(1/2) along the leaf, as does the boundary term of H2's integration by parts,
and the cut-off terms on [R_null, R_null + r_h] are bounded by the Morawetz bulk of D^{<= 2} S_W, by (a). The A-term is
the step between the levels: since Psi_1 = f^-1 r^2 nabla_L Psi, A = int r^(p+1) f^-2 |nabla_L Psi|^2 dr, the base energy
at level p + 1 up to f^2 >= (99/100)^2 -- what 10.9 (iii) took by a separate Hardy inequality is here the bulk itself. So
E^{p,(1)}_L[S_W](tau_2) + mu^-1/2 int_{tau_1}^{tau_2} (E^{p-1,(1)}_L + E^{p+1,(0)}_L)[S_W] dtau <~
E^{p,(1)}_L[S_W](tau_1) + (a)'s terms at tau_1, for p in [delta, 1 - delta].

(c) The rate for S_W. By (b) at p = 1 - delta, mu^-1/2 int E^{2-delta,(0)}_L[S_W] over each dyadic interval [tau_{j-1},
tau_j] is <~ I_0, so at a sample time there E^{2-delta,(0)}_L <~ (tau_j/sqrt mu)^-1 I_0, and by (a) at p = 2 - delta from
the sample, at every tau. Proposition 10.5's steps (ii)-(iv) then run with (1 + tau/sqrt mu)^-1 I_0 for I_0 at the top:
(ii) gives E^{1-delta,(0)}_L <~ tau^-2 at sample times and E^{1,(0)}_L <~ tau^(-2+delta) by interpolation; (iii) gives F
<~ tau^(-3+delta) at sample times; (iv) between them, through E^{delta,(0)}_L <= (E^{0,(0)}_L)^(1-theta)
(E^{2-delta,(0)}_L)^theta with theta = delta/(2 - delta), F <~ (1 + tau/sqrt mu)^(-3+2 delta) I_0. The p-weighted
energies follow by interpolation between E^{0,(0)}_L <~ F and E^{2-delta,(0)}_L <~ tau^-1, at (1 + tau/sqrt mu)^(-3+p+2
delta), and the integrated terms from (a) on [tau, oo): (10.44), with a delta to spare.

(d) P-hat. By Z2 and Y5, G_P = d_t S_W on [r_h, b r_h], where eta_b = 0, G_P is (10.26) on [2 b r_h, oo), and on [b r_h,
2 b r_h], which b r_h >= 2 R_null places in the far region where u = tau, |D^{<= m} G_P| <~ mu^-1/2 (1 + tau/sqrt mu)
|(sqrt mu d)^{<= 1} D^{<= m} S_W| -- his Lemma 8.3. So E^p_source[D^{<= m} G_P](tau, oo) is bounded through (10.44): the
middle region, compact, by mu^-1/2 int_tau^oo (1 + tau'/sqrt mu)^2 B-bar[D^{<= m+1} S_W] dtau' <~ (1 + tau/sqrt mu)^(-1+4
delta) I_0, summed over dyadic intervals (2 - 3 + 4 delta < 0); the inner region by the integrated bulk of (10.44), at
(1 + tau/sqrt mu)^(-3+4 delta); the outer by (10.26)'s weights, which put the source density r^-2 below the bulk of
(10.44) at the same p. So E^p_source(tau, oo) <~ (1 + tau/sqrt mu)^(-1+4 delta) I_0 for every p in [delta, 2 - delta],
uniformly -- less than his I_source,l=0,delta asks, (1 + tau/M)^(-2+p+delta), and enough. The Morawetz step for P-hat,
which carries a source, is [Sch13]'s with the source added: his Proposition 4.1 is stated for box phi = 0, and its
currents are multiplier identities, so with a source each divergence gains the source times the multiplier, which
Cauchy-Schwarz puts into E^p_source and the bulk -- deduced, as Proposition 10.4 carries its source, not READ.
Proposition 10.5's argument with it gives (i) boundedness at every p <= 2 - delta, the source integral being finite at
every p; (ii) the dyadic step at p = 2 - delta; (iii) at p = 1, with the source's (1 + tau_j/sqrt mu)^(-1+4 delta) for
its (1 + tau_j/sqrt mu)^(-1+delta-bar) -- 4 delta in delta-bar's place, past 10.5's range delta-bar <= 1/10 once delta >
1/40, but its steps (i)-(iv) use only 4 delta < 1 and, for the middle region's dyadic sum, -1 + 4 delta < 0, which delta
<= 1/10 secures -- F[P-hat] <~ (tau_j/sqrt mu)^-1 at sample times; and (iv) between them F(tau) <~ F + E^{delta,(0)}_L
at the sample plus the source from it, <~ tau^(-1+theta) + tau^(-1+4 delta), with theta < delta: (10.45), its integrated
term from (10.17) at p = delta on [tau, oo).

(e) W'. 10.8's argument, his section 8.2 on (10.23)-(10.26), with (10.44)-(10.45) for his Propositions 8.2 and 8.4: his
Appendix B bounds the O_j by sup norms on [r-underline, R_null] of (sqrt mu d)^{<= m+6} P and S_W, which spherical
symmetry turns into energies, and P = P-hat there since eta_b vanishes on [r_h, b r_h]; so his Lemmas 8.5-8.6 hold at the
rate of (10.45), Err_{l=0}(tau_1, tau_2) <~ (1 + tau_1/sqrt mu)^(-1+4 delta) Decay_0[W']. His (8.36), E(tau_2) + mu^-1/2
int_{tau_1}^{tau_2} E <~ E(tau_1) + Err_{l=0}(tau_1, tau_2), from the red-shift current on (W-bar_0, W-bar_3), coercive
by (10.24)'s sign, then gives E(tau) <~ (1 + tau/sqrt mu)^(-1+4 delta) Decay_0[W'] in one dyadic step, the rate being
below 1. Since mu (W0 + P/2 - (sqrt mu/4) S_W) is constant along H^+ (10.25) and W0 = c_1(tau)/r^2 + W-bar_0, c_1(tau) -
c_1(oo) = -mu (P/2 - (sqrt mu/4) S_W + W-bar_0)(tau, r_h), whose square the energy bounds, so it tends to zero at the
square root of that rate; W-hat - W-bar is (c_1(tau) - c_1(oo)) times W*'s components, its energy at the rate itself,
and (iii) follows as his Theorem 8.1's last step does. With c K* (Proposition
10.2(iv)), h_0 settles to c K* + c_1(oo) pi_{W*}. []

*What this gives.* Proposition 10.2(iv)'s conditional is discharged, and 10.8's at the weaker rate: at l = 0 the
perturbation settles to a change of mass and a stationary gauge mode, c K* + c_1(oo) pi_{W*}, at (1 + tau/sqrt mu)^(-1+4
delta). With 10.10, every mode of the class is carried: h decays in harmonic gauge at every mode l >= 2 at (1 + tau/sqrt
mu)^(-2+p+3 delta) and settles at l = 0 -- [Hun19]'s Theorems 1.2-1.4 (his Theorems 2.4(1) and 8.7) in five dimensions,
for the class. Route A is carried through, every step deduced on computed identities and READ inputs, none proved here.
The l = 0 rate is a power below his (1 + tau/M)^(-2+2 delta): the commuted hierarchy runs one step where his runs two.
The five-dimensional l = 0 wave has the tail t^-3 ([CYDL03]), so the loss is the method's; a second commutation, or an
absorption that keeps B_1's positive (57/8)(4 - p) mu/r^2, is not attempted.

*What remains, and is not done here.* Nothing of route A. Nothing of this section is proved: (10.40)-(10.43) and Y1-Y5
are computed, exactly; the base Morawetz estimate at l = 0 is READ ([Sch13]); Proposition 10.8 is deduced by Proposition
10.5's argument and his section 8, constants not tracked. Route B's item 2, the five-dimensional constraint damping
(ROUTES-OPEN.md 4.5), is 10.12's.

### 10.12 Route B's constraint damping in five dimensions: the indicial roots at zero energy (`damping5.py` U1-U6; D54)

*The setting.* Route B (ROUTES-OPEN.md 4.4) is [Hin26]'s nonlinear argument carried to five dimensions. Its gauge-fixed
Einstein operator Ric(g) - delta*_{g,C} Upsilon(g) has the constraint propagation operator box^C = 2 delta_g G_g
(delta*_g + C), and [Hin26] (1.43) asks that the zero energy operator of box^C have no indicial root with real part in
[-C_0, 1) -- "C_0 = 100 suffices by a large margin". In four dimensions that is [Hin26a] Theorem 4.9, for C omega = h^-1
(2 c (x)_s omega - (1 - e) g iota_{c#} omega), c = r^-1 (dt - v dr), v in (0, 1), e > 0 small and then h > 0 small -- e
below the bounds of his Theorem 4.9 and his Lemma 4.4, of which he writes "the maximal possible value of e_0 is very
small (namely, e_0 < c v^2 for c ~ 0.000152)" (p. 33). Indicial roots see only the model at infinity ([Hin26] Theorem
7.1's proof: "Parts (3) and (4) only see the Minkowskian model"), so in five dimensions the question is one on 4+1
Minkowski. ROUTES 4.4 item 2 named it the first genuinely new object of the route. Notation: delta* omega =
(1/2)(omega_{a;b} + omega_{b;a}), G = Id - (1/2) g tr_g, (delta k)_a = -g^{bc} k_{ab;c}, n the spatial dimension (4
here, 3 his), kappa := l (l + n - 2).

*What is computed* (`damping5.py`, exact unless said).

(U1) The indicial families, from the definitions: box^C on Minkowski^{n+1} in polar coordinates, applied to the
stationary 1-forms r^-lam (a S dx^0 + b S dx^1 + c r dS) (scalar type, S a spherical harmonic) and r^(1-lam) V (vector
type), returns the same type times r^(-lam-2) with a matrix N(lam) -- 3 x 3 for scalar l >= 1, 2 x 2 at l = 0, 1 x 1 for
the vector type -- free of the angles and affine in kappa. At n = 3 and weight 1, N is his (4.19) with Corollary 4.7's
q's entry by entry, and the vector polynomial p_v (the display of his section A.1), p_s0 and the sextic (A.13) follow.

(U2) The weight must be adapted to the dimension. Since G (g f) = (1 - D/2) g f in D = n + 1 dimensions, with C omega =
h^-1 (2 c (x)_s omega - m (1 - e) g iota_{c#} omega),

    h G_g C omega = 2 c (x)_s omega + (-1 + m (1 - e)(D/2 - 1)) g <c, omega>,                                  (10.46)

which is his h^-1 (2 c (x)_s omega - e g <c, omega>) -- the form whose symbol is his Lemma 3.2's l_{g,c,e} -- for every e
if and only if m = 2/(D - 2): 1 in four dimensions, his, and 2/3 in five. C_5 below is C with m = 2/3.

(U3) The polynomials at weight 2/3. The vector type: p_v = -h lam^2 + (2h - 2v) lam + h kappa + 6v (his: -h lam^2 + (h -
2v) lam + h kappa + 4v). lam = 2 is a root of the scalar type at l = 0 and l = 1 for every (v, e, h) -- the Coulomb rate
r^-(n-2), as lam = 1 is in his. At h = 0 the scalar sextic h^3 det N is

    8 v (lam - 2) Q_5,  Q_5 = e ((v^2 - 1) kappa + (1 + v^2)(lam - 3)(lam + 1)) - 2 v^2 (lam - 2)(lam - 3),   (10.47)

-16 v^3 (lam - 3)(lam - 2)^2 at e = 0 (his: 8 v (lam - 1) Q_4, and the roots 1, 1, 2 of his (P1)); and the very negative
roots lam = (h lt)^-1 have the same h = 0 limit in four and five dimensions; the top-weight parts (lam of weight 1,
kappa of weight 2) are h^3 (kappa - lam^2)^3 and h (kappa - lam^2), so the roots go as +-kappa^(1/2) and accumulate only
at +-infinity, his Theorem 4.9's last clause.

(U5) His weight transcribed literally fails: with m = 1 the scalar type at l = 0 has, at h = 0, the root (7 v^2 - 1 + 3e
(1 + v^2))/(5 v^2 + 1 - 3e (1 + v^2)), at e = 0 in (-1, 1) for every v in (0, 1); at the parameters below the quartic has
a real root in (0, 1), inside [-C_0, 1).

(U6, numerical, a measurement) At v = 1/2 over e, h in {10^-2, 10^-3, 10^-4} and l <= 10^6, 85 sampled values (mpmath,
50 digits): besides lam = 2 at l = 1, found at all nine, the roots of the upper family stay above 1.93; they are above 2
exactly where h <= e (six points) and between 1.939 and 1.967 where h > e (three); the lower family sits near -1/h, so
C_0 asks h small against 1/C_0 -- at h = 10^-2 its largest root is -96.3 (e = 10^-2), inside [-100, 1).

**Proposition 10.9 (computed; exact).** At (v, e, h) = (1/2, 1/102400, 10^-6) -- v = 1/2 as [Hin26a] p. 3 suggests, e
below the five-dimensional bound of his Lemma 4.4 (Proposition 10.10) and h < e, chosen here -- with C = C_5, the zero
energy operator of box^C on 4+1 Minkowski has, over every l and both types, no indicial root with real part in [-100,
19/10], and the only ones with real part in [-100, 2] are lam = 2 at l = 0 and l = 1, each simple; the roots accumulate
only at +-infinity. With m = 1 in place of 2/3 it fails.

*Deduced.* That these are the indicial roots of box^C on five-dimensional Tangherlini, so that [Hin26] (1.43) holds
there with C_0 = 100: indicial roots see only the leading-order part at infinity ([Hin26] p. 136, "Parts (3) and (4)
only see the Minkowskian model"; p. 29, "indicial roots are determined by the leading-order (in the sense of decay as
rho -> 0) part"), Tangherlini differs from Minkowski by O(mu r^-2), and c must equal r^-1 (dt - v dr) for large r -- a
five-dimensional c of [Hin26a] Proposition 5.1's kind, which 10.13 prepares and 10.14 constructs.

*Proof* (U4). The leading coefficient of the scalar sextic is -h^3 /= 0, so its roots move continuously in real kappa.
On a line Re lam = x a root appears only if the polynomial shifted to the line has a zero constant coefficient (a real
root at x) or a zero Hurwitz determinant Delta_{deg-1} (Orlando's formula: two roots summing to 2x, which a pair on the
line does). Both, as polynomials in kappa, have no root on kappa >= 3 at x = -100 and x = 19/10 (Sturm), and at l = 1
Routh arrays count 3 roots right of 19/10 and 3 left of -100; so the strip is empty for every l >= 1, and the same for
the vector quadratic (1 and 1) and, at l = 0, the quartic (2 and 2). At x = 2 the same holds for kappa >= 8 (l >= 2; 3 |
0 | 3 at l = 2), and at l = 1 and l = 0 the cofactors of lam - 2, a quintic and a cubic, have 2 | 0 | 3 and 1 | 0 | 2
(right | between | left) and do not vanish at 2; the vector type has 1 | 0 | 1 at l = 1 and does not cross. A Routh
array with no zero in its first column also excludes roots on its line, a zero constant term being refused.
Four-dimensional control: the same at his weight 1, at the lines 9/10 and 1 -- his Theorem 4.9 at this point. The roots'
growth is U3's top-weight computation. Controls: the line 21/10, right of lam = 2; U5's m = 1. The first version of this
section used (v, e, h) = (1/2, 1/100, 1/1000), which the certificate also clears but which lies above Lemma 4.4's bound
(W6 of 10.13): an indicial statement only (the twenty-second verifier, D54). []

*READ.* [Hin26a] (arXiv:2606.27658v2, alphaXiv, 2026-10-21): pp. 1-3 (Theorem 1.1, (1.1)-(1.2)), 5, 7, 25 (Definition
3.1, Lemma 3.2), 29, 33-37 (section 4.3, Lemma 4.6, Corollary 4.7, (4.19), Definition 4.8, Theorem 4.9, Remarks
4.10-4.12), 67 (Theorem 6.2), 69-74 (Appendix A, (A.1)-(A.2), A.2, (A.13)), 85. [Hin26] (arXiv:2606.28253v2): pp. 1, 4,
25-26, 17, 29 ((1.43) and the reason for its strip), 82 (Definition 4.2, (4.6)-(4.9)), 136 (Theorem 7.1).

*What this gives, and what it does not.* The indicial half of route B's strong damping condition, which ROUTES 4.4 named
as the first object with no five-dimensional construction, has one at the level of the Minkowski model: Hintz's
constraint damping with the trace weight 2/(D - 2) in place of 1, at a point below the five-dimensional bound of his
Lemma 4.4 (Proposition 10.10), h < e chosen here, computed exactly; its transfer to Tangherlini is deduced. The point is
not certified as one of his construction: that also asks e below the bounds of his Proposition 5.1 on the black hole
side, which 10.14 meets on Tangherlini at this e, and h below the h_0(e) of his Theorem 5.2, which his proof does not
make explicit (the twenty-third verifier, D56). Which strip the five-dimensional argument needs: [Hin26] p. 29 asks for
no root in [-C_0, 1) because a root lam of box^C gives the root lam - 1 of the linearized gauge-fixed operator (the
order of decay gained under delta*), and that operator's large roots are those below its indicial gap, which begins at
0. The shift does not depend on the dimension, so the strip needed in five dimensions is his literal [-C_0, 1), provided
the five-dimensional operator's gap also begins at 0 -- not computed here; 10.24 computes that it does, at this point.
Both strips are clear at the point: [-100, 19/10] with nine tenths to spare, and [-100, 2] but for the Coulomb root. Not
done, and OPEN (10.21 deduces (1)-(2) from [Hin26a] Theorem 5.2): [Hin26] Theorem 7.1's other parts on five-dimensional
Tangherlini -- (1) mode stability of box^C at nonzero energy, (2) invertibility of its zero energy operator on the
weighted spaces, and (4) the tf-admissibility, which sees only the Minkowski model but is not an indicial-root statement
-- on the five-dimensional c of 10.14; and item 2's other half, the modification E^Upsilon of [Hin26] Proposition 6.12
that removes W* from box^Upsilon. Nothing of this section is proved: Proposition 10.9 is computed, at one parameter
point, with U6 a numerical survey at larger e and h, whose grid does not contain the point; its transfer to Tangherlini
is deduced.


### 10.13 The semiclassical inputs of the constraint damping in five dimensions (`semiclass5.py` W1-W6; D55)

*The setting.* [Hin26a] proves its Theorem 6.2 -- [Hin26] Theorem 7.1 (1)-(2), mode stability of box^C at nonzero
energy and invertibility of its zero energy operator -- by semiclassical estimates in h on a compactified spacetime.
Their inputs are fibrewise linear algebra (his section 3, stated for "dim M = 4"); the symbols of the zero section
transport operator at the critical sets of -r^2 c# on Minkowski space (section 4.1-4.2): a saddle at the corner dK+ of
K+ and sf, a sink at R_v = {r/t = v}, and, where -c# turns from pointing into the black hole to pointing out of it, an
interior saddle at r = r_0 with c = r_0^-2 (r_0 dt - v (r - r_0) dr), his (4.8); and the indicial roots (section 4.3;
10.12). His Proposition 5.1 then glues a c on Kerr from these pieces for e below the bounds of his Lemma 4.4 and
Theorem 4.9, and his Theorem 5.2 solves the forward problem on weighted 3b-spaces whose weights the critical-set lemmas
fix. This section recomputes the inputs on 4+1 Minkowski. The semiclassical part has his form in any dimension once the
weight is 2/(D - 2) (10.12, U2): L = 4ih delta(c (x)_s .) + 2ihe d iota_{c#}, his (3.2).

**Proposition 10.10 (computed; exact unless said).** On 4+1 Minkowski, with the weight 2/3:
 (i) (his section 3) B = g^-1 - (1 + e) G(c)^-1 c# (x) c# makes l(zeta) self-adjoint and is positive definite for e >
     0, and the characteristic polynomial of l(zeta)/2 is (lam - G(c) zeta_0)^3 times his (3.8) quadratic; his Lemmas
     3.3-3.8, whose proofs use only this, hold verbatim. With the weight 1 the effective e is (3e - 1)/2 < 0 and B is
     indefinite (W1).
 (ii) (his Lemmas 4.1-4.2) At dK+ the eigenvalues of r^2 (-l(dw/w) + S)/2 at e = 0, w = rho_sf^b_sf rho_K^b_K, are
     v (1 + b_K - b_sf), 2v (1 + b_K - b_sf) and v (2 + b_K - b_sf) (3x); at R_v (b_K = 0) v (1 - b_sf), 2v (1 - b_sf)
     and v (2 - b_sf) (3x). They are positive iff b_K > b_sf - 1 and b_sf < 1, where his are b_K > b_sf - 1/2 and
     b_sf < 1/2: the thresholds are -(n - 2)/2 and (n - 2)/2 at n = 3 and 4 (W3). Deduced, his section 5 being open in
     five dimensions: with his b_K = a_K, b_sf = a_sf + 1 (p. 39) and spaces normalised by |dg| (footnote 15), his
     (5.14), a_sf < -1/2 and a_K > a_sf + 1/2, would become a_sf < 0 and a_K > a_sf.
 (iii) (his Lemma 4.4) At the interior saddle, at e = 0, S is his -- a_22 = v, trace 5v, determinant 2 v^2 (3 - 2x^2),
     positive on |x| <= 6/5 < (3/2)^(1/2) -- and at v = 1/2, e = 1/102400 it is positive definite on |x| <= 6/5 (Sturm).
     The largest admissible e is about 0.000069 v^2, against about 0.000154 v^2 in four dimensions (numerical, a grid
     of 1201 points in x and bisection; his "c ~ 0.000152") (W4).
 (iv) (his Lemma 4.3) l(+-dr) is negative definite for +-(r - r_0) >= r_0 e^(1/2)/v, r in [r_0/2, 2 r_0] (beyond
     r_0 (1 + 1/v) c is not timelike); its proof, Lemma 3.8's condition 2(1 - e) w/(e (1 - w)) >= 2 > 1 for
     e <= w < 1, w = v^2 (r - r_0)^2/r_0^2, involves no dimension (W5).
 (v) Proposition 10.9's point (1/2, 1/102400, 10^-6) is admissible for (iii); e = 1/100 is not (W6).

*Proof.* W1-W6 of semiclass5.py. S is computed from its definition, S = (L - L*)/(2ih), the adjoint taken with respect
to |dg| and B in Cartesian coordinates, and not from his Lemma 3.9's formula; the four-dimensional control reproduces
his (4.6) for every e, his (4.7) and Lemma 4.2, and Lemma 4.4's a_00, a_10, a_11 and a_22 with his e = 0 determinant.
His printed a_01 is the computed one times e; with it the e = 0 determinant would be 2 v^2 (1 - x^2)(3 + 2x^2), not his
2 v^2 (3 - 2x^2) -- a misprint, x e^(1/2) for x/e^(1/2) (W2). []

*READ.* [Hin26a] (alphaXiv, 2026-10-21) pp. 9-10, 25-33 (section 3: Definition 3.1, Lemmas 3.2-3.9, Remark 3.4,
Corollary 3.6; section 4.1-4.2: (4.1)-(4.9), Lemmas 4.1-4.4 and the sentence after Lemma 4.4), 38-41 (Proposition 5.1
and its proof), 43, 53, 66-68 (Definition 6.1, Theorem 6.2 and its proof); [Hin26] pp. 17, 29, 134-137.

*What this gives, and what it does not.* Every input of [Hin26a]'s semiclassical argument that is a computation on
Minkowski space carries to five dimensions, with three differences, each computed: the weight 2/(D - 2); the weight
thresholds at the two critical sets on sf, shifted by 1/2; and a smaller admissible e, about 0.000069 v^2 for 0.000154
v^2. The e = 0 limit at the interior saddle, on which his 6/5 > 1 rests, is unchanged. Not deduced here: his Theorems
5.2 and 6.2 in five dimensions. They need, besides these inputs, a five-dimensional c of his Proposition 5.1's kind on
Tangherlini -- past timelike, pointing into the black hole near the horizon, equal to r^-1 (dt - v dr) at large r, with
the interior saddle and the positivity (6) -- which 10.14 constructs; his 3b-analysis (sections 2 and 5); and section
6's own five-dimensional steps: the weight interval of (6.1) with its density r^2 |dr dg/| (r^3 in five dimensions), the
exponent of (6.4) and the data weights of (5.16). This record has read none of these in five dimensions (10.21 now
computes section 6's steps). The one Minkowski input of his section 6, S^C of his (4.17), carries over: in the null
splitting it is the same matrix with three angular copies (the twenty-third verifier, not an instrument here). Not done,
and OPEN: the 3b-estimates of his section 5 in five dimensions; section 6's five-dimensional steps; his Theorem B.1, the
tf-admissibility; and item 2's E^Upsilon. Nothing of this section is proved: Proposition 10.10 is computed, (iii)'s e_0
numerically.


### 10.14 A constraint damping 1-form on five-dimensional Tangherlini (`cform5.py` C1-C7; D56)

*The setting.* [Hin26a] Proposition 5.1 glues, for e small and r_0 large, a stationary c on Kerr from the Minkowski
pieces of his section 4: (1) r c past timelike; (2) c = (1/2) r_0^-2 (r_0 dt - v (r - r_0) dr) on [r_0/2, 2 r_0] and
r^-1 (dt - v dr) for r >= 3 r_0 (r >= 2 r_0 before smoothing, his (5.11)); (3) S positive definite on |r - r_0| <= (6/5)
r_0 e^(1/2)/v; (4)-(5) positivity at the corner dK+ and at the sink R_v of sf, for the weights w = rho_sf^(a_sf + 1)
rho_K^a_K and w' = rho_sf^(a_sf + 1); (6) -l(-dr) positive definite for m <= r <= r_0 - r_0 e^(1/2)/v and -l(dr) for
r >= r_0 + r_0 e^(1/2)/v, with two conditions on sf. Near the horizon he uses three pieces and a partition of unity,
Boyer-Lindquist t being singular there. His proof is perturbative: each of its bounds (e', e_partial, e_2, r_1, r_2,
delta_r) exists, and none is given but footnote 14's numerical "roughly r_2 >= 81m/e^(1/2)" on Schwarzschild. This
section writes one c on five-dimensional Tangherlini, explicitly, and checks its conditions at the point of Proposition
10.9 exactly. Tangherlini in Kerr-Schild time,

    g = -f dt^2 + 2 (1 - f) dt dr + (2 - f) dr^2 + r^2 dOmega_3^2,   f = 1 - mu/r^2,                         (10.48)

regular across the horizon, its t differing from the static time by int (f^-1 - 1) dr; mu = 1, so r_h = 1, and the
domain [r_h/2, oo) stands for his m <= r (m = r_+/2 at a = 0).

**Proposition 10.11 (computed; exact unless said).** At (v, e) = (1/2, 1/102400) and r_0 = 100 the 1-form

    c = (2 r_0)^-1 (dt + (v/2) dr)                for r <= r_0/2,
    c = (1/2) r_0^-2 (r_0 dt - v (r - r_0) dr)    for r_0/2 <= r <= 2 r_0,                                      (10.49)
    c = r^-1 (dt - v dr)                          for r >= 2 r_0

is continuous and has the following properties on (10.48).
 (i) (condition (1)) r c is past timelike on [r_h/2, oo). The inner piece is past timelike for every r > 0 and every v
     in (0, 1): G(dt + b dr) = (1 - b)(-2 + f (1 - b)) and <dt + b dr, dt> = -(2 - b) + f (1 - b), negative for
     f < 1 and 0 < b < 1 (C2).
 (ii) (condition (6) off sf) <c, dr> > 0 on [r_h/2, r_0 - r_0 e^(1/2)/v] -- -c# points into the black hole there -- and
     <c, dr> < 0 on [r_0 + r_0 e^(1/2)/v, oo), with Lemma 3.8's f e G(c) + 2 (1 - e) <c, dr>^2 > 0 (G(dr) = f): so
     -l(-dr), resp. -l(dr), is positive definite (C3; Lemma 3.8 holds in five dimensions, Proposition 10.10(i)).
 (iii) (condition (3)) S, computed on (10.48) from its definition, is of order zero, free of the angles and block
     diagonal, is the Minkowski S of 10.13 at mu = 0, and is positive definite on |r - r_0| <= (6/5) r_0 e^(1/2)/v
     (C1, C4).
 (iv) (conditions (4)-(6) on sf, where g and its Minkowski model agree as 3sc-metrics) The symbol T = r^2 (-l(dw/w) + S)
     of r^-1 (dt - v dr) depends on rho_K = r/t and the weights only, is B-self-adjoint, and its eigenvalues are
     positive at dK+ iff b_K > b_sf - b* and at R_v iff b_sf < b*, where b* = 0.99340731... is a root of 204795 d^2 -
     409605 d + 204801: Proposition 10.10(ii)'s thresholds at e = 0, moved by 0.0066. At (a_K, a_sf) = (1, -102), the
     weights of his Theorem 6.2's proof at C_0 = 100, T is positive definite on all of sf with rho_K <= 10, and at the
     sink's weight on all of sf (C7). His (5.8) holds on (0, 10] but on an interval about v of half-width under 0.00166,
     so the conditions (6) on sf hold with delta_sf = 1/100 and any delta_r (C5).
 (v) (a measurement) The smallest integer r_0 for which (i)-(iii) hold is 86: (1) holds at every integer r_0 in [2, 86],
     (6) from 33 on, (3) at 86 alone. At e/4 it is 137. By scaling (deduced: with mu = u r_0^2 every condition depends
     on u and r/r_0 alone) it is 86 mu^(1/2) = 86 r_h (C6).

*Proof.* C1-C7 of cform5.py. Each sign condition is checked by Sturm on the numerator and the denominator of a rational
function of r over its interval, unbounded intervals included. S is computed from S = (L - L*)/(2ih) with Christoffel
symbols in polar Kerr-Schild coordinates, the adjoint taken with |dg| = r^3 cos th sin th and B. Controls: the adjoint
with g^-1 (not of order zero); the inner piece dt + dr (null); r_0 = 30 ((6) fails just outside the saddle); the window
12/5; e = 1/2 in (5.8); the claim 87; and b_sf = 1 at this e ((5) fails). []

*Deduced.* (a) Conditions (4)-(5) off sf, for 0 < rho_sf <= 2 delta_r: Tangherlini differs from its Minkowski model by
rho_sf C^oo terms, so the positivity of (iv) persists for some delta_r > 0 (his argument, p. 39). delta_r is not made
explicit, here or in his proof. (b) The smoothing at r_0/2 and 2 r_0: there only (1) and (6) are asked, and l(dr)
depends on c at each point and not on its derivatives, so a small smoothing keeps them (his argument, p. 41). (c) The
outer piece is r^-1 (dt - v dr) in Kerr-Schild time; in the static time t_s it is r^-1 (dt_s - v dr) + O(mu r^-3) dr,
with the same leading part at infinity, which is all the indicial roots of 10.12 see.

*READ.* [Hin26a] (alphaXiv, 2026-10-21): pp. 3 (v = 1/2; the sign of the dr term), 93 (Theorem B.4; Theorem B.1, which
the text below names, is on p. 87, as the twenty-fifth verifier read at source), 38-41 (Proposition 5.1 and its proof,
(5.1)-(5.13), footnote 14), 41 (Theorem 5.2, (5.14)-(5.15)), 53 (Proposition 5.1 (4) and (6) in use), 67 (Theorem 6.2
and its proof: a_K = 1, a_sf = -C_0 - 2).

*What this gives, and what it does not.* The five-dimensional c that 10.12 and 10.13 named as missing exists on
Tangherlini, explicitly. At the point of Proposition 10.9 its conditions (1), (3) and (6) hold exactly on the
Tangherlini metric itself, and (4)-(6) on sf. Only (4)-(5) in a neighbourhood of sf, off it, and the smoothing are
deduced, by his arguments. So every bound his Proposition 5.1 places on e -- Lemma 4.4's, Theorem 4.9's at h = 10^-6
(Proposition 10.9; not for every h below an h_0(e)), e' near the horizon, e_partial at the critical sets, (5.9) and
(5.10) -- is met at e = 1/102400 on Tangherlini, by computation, for the weights (1, -102). The construction is simpler
than his because of the time it uses: Kerr-Schild time is regular across the horizon, and one piece, dt + (v/2) dr,
serves from inside the horizon to r_0/2, where his, in Boyer-Lindquist time, uses three and a partition of unity. The
saving is the time, not the dimension: on four-dimensional Schwarzschild in Kerr-Schild time dt + dr/4 serves as well
(the twenty-fourth verifier, exact; at a /= 0 not checked). The bound on r_0 is also far below his: 86 r_h at e =
1/102400 -- and every r_0 > 85.52 r_h, by the twenty-fourth verifier's threshold analysis ((3) holds iff r_0 > 85.521
r_h, (6) iff r_0 > 32.900 r_h; at e/4 (3) iff r_0 > 136.787 r_h; not an instrument here) -- against footnote 14's
roughly 81 m/e^(1/2) = 25920 m (12960 r_+) on Schwarzschild at that e. Tangherlini's correction falls like mu r^-2 where
Schwarzschild's falls like m r^-1. These are two numerical bounds, not a law: at e/4 the ratio 137/86 = 1.59 is neither
4^(1/4) nor 4^(1/2). What [Hin26a] still asks in five dimensions is his Theorem 5.2 -- the 3b-estimates of his section 5
on five-dimensional Tangherlini, with an h_0(e) that his proof does not make explicit, so that h = 10^-6 is not
certified below it -- and his section 6's five-dimensional steps and Theorem B.1. All of these are OPEN, as is item 2's
E^Upsilon, whose inputs 10.15 computes. Nothing of this section is proved: Proposition 10.11 is computed at one point,
and (v) is a measurement.


### 10.15 The gauge potential operator in five dimensions: inputs of [Hin26] Proposition 6.12 (`gaugepot5.py` G1-G7; D57)

*The setting.* Beside the constraint damping, [Hin26]'s route needs mode stability of the gauge potential wave operator
box^Ups = 2 delta_E G delta* at every frequency of the closed upper half plane, zero included: with that of box^C it
gives mode stability of the gauge-fixed linearized operator and a simple zero energy nullspace (his section 1.4.1). The
unmodified operator box = 2 delta G delta*, on a Ricci-flat metric the 1-form wave operator, has a zero energy state --
on Kerr his Lemma 6.10, from [AHW24]; on five-dimensional Tangherlini W* of 10.4, (10.2) -- and his Proposition 6.12
removes it by modifying the divergence: near the horizon by gamma_H E_{H+,1}, E_{H+,1} h = 2 iota_{c_H#} h - c_H tr h
with c_H compactly supported ((6.22)), near infinity by h -> -gam (2 iota_{c#} h - (1 - e) c tr h), c = r^-1 dt ((6.5)).
Step 1 of his proof is an augmented-operator argument at low energy whose inputs are the kernel omega_(0) and cokernel
omega* = delta(r - r_+) dr of box(0) and two pairings, (6.21) <[box, t_*] omega_(0), omega*> = 4 pi and (6.23) <2
E_{H+,1} G delta* omega_(0), omega*> in (3 pi, 5 pi), which make <f, omega*> = 4 pi (-i sigma^ + c_b gamma^) != 0
((6.26)); Step 2 adds the modification near infinity perturbatively. This section computes the five-dimensional inputs.
Near infinity the modification takes the trace weight 2/(D - 2) = 2/3, as C does (10.12, U2), so that E G h = -gam (2
iota_c h - e c tr h) in any dimension. At the horizon gaugepot5.py takes the same weight in E_{H+,1}; the pairing (6.23)
is the same at his weight 1, since tr delta* W* = 0.

**Proposition 10.12 (computed; exact).** On 4+1 Minkowski and on five-dimensional Tangherlini, f = 1 - mu/r^2, r_h =
mu^(1/2):
 (i) (his Lemma 6.6) The indicial roots of box^Ups solve, at s0, lam (lam - 3)(lam^2 - lam - 2 - z) = 0, z = 4 e gam^2
     (his z is e gam^2, p. 117); at vl, (lam + l)(l + 2 - lam) = 0; at sl, (l + 3 - lam)(l + lam - 1) Q = 0, Q = s^2 -
     (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa, s = lam (lam - 1), kappa = l (l + 2). At gam = 0 the indicial
     gap is (0, 2), his (0, 1); for z > 0, 2 < lam_s1,2 < lam_s0 and every other root is at least 3 or at most 0, so (0,
     lam_s1,2) is an indicial gap, his (6.17b). With the weight 1 the s0 root 2 moves to (1 + (9 - 8 gam^2 (1 -
     3e))^(1/2))/2, in (1, 2) when e < 1/3 and 0 < gam^2 (1 - 3e) < 1 (G1).
 (ii) (the zero energy equations) For stationary 1-forms on Tangherlini the dt part and the spatial part of box
     decouple, by the time reflection: A S dt solves (f/r)(r^3 A')' = kappa A; B S dr + C dS and the vector type V solve
     the systems of G2, each the Euler-Lagrange form of an energy, B (r^3 f^2 B')' + kappa C (r f C')' = (r^3 f^2 B B' +
     kappa r f C C')' - r^3 f^2 B'^2 - kappa r f C'^2 with a zeroth-order matrix of determinant kappa^2 f (kappa - 1 +
     mu/r^2) > 0 for r > r_h and l >= 1, and V (r f V')' = (r f V V')' - r f V'^2 (G2, G3).
 (iii) (his Lemma 6.10 at l = 0) At l = 0, A = a + b/r^2 and B = c/(r^3 f) + d r/f; smooth at the future horizon and
     decaying, the kernel is the span of W* = dt/r^2 + mu^(1/2) dr/(r^3 f) (G4).
 (iv) (the cokernel functional) For every stationary u, <box(0) u, delta(r - r_h) dr> = 0: g^-1(box u, dr) vanishes at
     r_h for u = a(r) dv + b(r) dr, is a multiple of S at every l >= 1, and vanishes for the vector type (G5).
 (v) (his Lemma 6.11 and (6.26)) With |dg_X| = r^3 cos th sin th |dr dth dp1 dp2| and t_* = v near the horizon, <[box,
     t_*] W*, delta(r - r_h) dr> = 4 pi^2, where his is 4 pi (the four-dimensional control reproduces it); W* is
     divergence-free; eta = iota_{grad r} delta* W* = -mu^(-3/2) (dv + (3/2) dr) at r_h; and <2 E_{H+,1} G delta* W*,
     delta(r - r_h) dr> = -12 pi^2 c_v - 8 pi^2 c_r for c_H = c_v dv + c_r dr at r_h. So c_H = -(1/2) chi(r) dr, chi = 1
     near r_h, gives 4 pi^2, and <f(0, sigma^, gamma^), omega*> = 4 pi^2 (-i sigma^ + gamma^) != 0 for Im sigma^ >= 0,
     gamma^ >= 0, not both zero (G6).
 (vi) d_sigma box(0) W* = -i [box, t_*] W* = i r^-3 dt + O(r^-4) for t_* = t - r*: of order rho^3, as his omega_(0)'s is
     in four dimensions, but by the dimension and not by his cancellation: (rho d_rho - 3/2) rho^2 = rho^2/2, where (rho
     d_rho - 1) rho = 0 (G7).

*Proof.* G1-G7 of gaugepot5.py. The operator is built from its definitions, with Christoffel symbols in polar
coordinates (static for the mode equations and at infinity, ingoing at the horizon) and harmonics of symbolic degree (S
= cos^l th cos l p1 and the record's vector harmonic); the pairings integrate over the horizon sphere, of area 2 pi^2
r_h^3. Four-dimensional controls: his Lemma 6.6's roots, his (6.21) = 4 pi, and his cancellation at infinity. Controls:
the weight 1; 2 delta delta* without G; f -> 1 in (ii)'s A equation; dt/r^2 alone; delta(r - 2 r_h) dr; c_H = +(1/2) dr,
for which (6.26) vanishes at (sigma^, gamma^) = (i, 1); and the four-dimensional cancellation claimed in five
dimensions. []

*Deduced.* (a) The kernel of box(0) on Tangherlini, on 1-forms smooth across the future horizon and decaying at infinity
(shifted weight alpha + 2 in (0, 2)), is the span of W*. At l = 0 this is (iii). At l >= 1 the dv component of a kernel
element is A S, so A is smooth, and at r_h the A equation f (r^3 A')' = kappa r A reads -kappa r_h A(r_h) = 0: A
vanishes there and A/f is smooth. Multiplying by A and integrating over [r_h, oo), where the boundary terms vanish
(A(r_h) = 0, and A ~ r^-(l+2) at infinity), gives -int r^3 A'^2 = kappa int r A^2/f, so A = 0. Then B, C and V are
smooth at r_h, and the identities of (ii), integrated over [r_h, oo) with the boundary terms vanishing at r_h (f = 0)
and at infinity (decaying exponents at least 2, by (i)), give B = C = V = 0. Inside the horizon a kernel element
vanishes to infinite order at r_h, a regular singular point of each mode's equations, and so vanishes (Lemma 10.56 (c);
D149). This is his Lemma 6.10's kernel in five dimensions, which [Hin26] takes from [AHW24] on Kerr; here Tangherlini is
static and the argument is an energy identity. The smoothness of kernel elements at the horizon, and their expansion at
infinity, are [Hin26c]'s radial-point and b-regularity, taken as in four dimensions and OPEN in five. (b) By (iv),
delta(r - r_h) dr annihilates the range of box(0); it spans the cokernel once the index is 0, which in four dimensions
is [Hin26c] Corollary 9.43 with his Lemma 6.8 (tf-admissibility). (c) With (a), (b) and (v), the augmented
zero-parameter operator of his Step 1 is injective: pairing box(0) u + c f(0, sigma^, gamma^) = 0 with omega* gives c =
0, then u is a multiple of W* and the augmentation row makes it 0. By (vi), the first summand of f lies in rho^3 C^oo,
inside the target space when alpha + 2 < 1; with (a), which needs alpha + 2 in (0, 2), the admissible range is alpha + 2
in (0, 1) (his condition is alpha + 2 + eta < 3/2, p. 124).

*READ.* [Hin26] (alphaXiv, 2026-10-21): pp. 25-26 (section 1.4.1), 82 ((4.6)), 113 (section 6, (6.1)-(6.6)), 117-118
(Lemma 6.6, (6.17a)-(6.17b), Remark 6.7, Lemma 6.8), 119-124 (section 6.4: Proposition 6.9, Lemmas 6.10-6.11,
Proposition 6.12 and its proof, (6.20)-(6.28), footnotes 65-69). E^Upsilon is his Definition 4.1, (4.1)-(4.2), p. 81, as
the twenty-fifth verifier read at source; Definition 4.2 on p. 82 is E^C.

*What this gives, and what it does not.* The zero energy structure of the unmodified gauge potential operator (E^Upsilon
= 0) in five dimensions is that of four: a one-dimensional kernel spanned by W*, decaying at the Coulomb rate r^-(n-2);
a cokernel functional supported at the horizon; and pairings that do not vanish -- 4 pi^2 where his is 4 pi, in both
cases (n - 2) times the area of the unit sphere -- so that a horizon modification of his form removes the kernel, at the
level of his Step 1's algebra. Two things differ: the kernel for l >= 1 is settled here by an energy identity,
Tangherlini being static, where [Hin26] needs [AHW24] for Kerr; and the first term of f decays at rho^3 by the
dimension, where his needs a cancellation. Not done, and OPEN: [Hin26c]'s low-energy theory in five dimensions -- the
index 0 of box(0) on the weighted spaces, and with it that delta(r - r_h) dr spans the cokernel; tf-admissibility (his
Lemma 6.8, from [Hin26c] Proposition 9.40); the estimates (6.27)-(6.28) -- and his Step 2, the perturbation near
infinity; mode stability of box at nonzero frequencies in five dimensions, which his Proposition 6.9 takes from [AHW24]
Theorem 5.1 on Kerr (deduced on Tangherlini, within a class, in 10.16); the high-energy side of his Proposition 6.9 in
five dimensions -- his Proposition 6.5, from section 6.1's strong trapping admissibility (Lemma 6.4; deduced in 10.17)
-- and Lemma 6.1's structure (deduced in 10.18 from its computed U1-U4); and the radial-point and b-regularity behind
(a) (its threshold, 3/2, deduced in 10.18, for this section's c_H). Nothing of this section is proved: Proposition 10.12
is computed, and (a)-(c) are deduced. 10.20 deduces the index 0, tf-admissibility and the estimates, and his Proposition
6.12, on the reading of [Hin26c] section 9 stated in 10.19 and widened in 10.20.

### 10.16 Mode stability of the 1-form wave operator at sigma != 0 in five dimensions (`modes5.py` M1-M5; D58)

*The setting.* [Hin26] Proposition 6.9 makes box^Upsilon = 2 (delta + E^Upsilon) G delta* mode stable at every sigma
with Im sigma >= 0 and |sigma| >= c_0, for E^Upsilon small: high energies by his Proposition 6.5, and bounded
frequencies by perturbation from the unmodified operator box = 2 delta G delta*, [Hin26c] Theorem 9.5's Fredholm
estimates holding uniformly. The input is the mode stability of box at sigma != 0, which on Kerr he takes from [AHW24]
Theorem 5.1. On a Ricci-flat metric box is the Hodge d'Alembertian d delta + delta d, which commutes with d and delta:
for a mode omega at sigma != 0, delta omega is a scalar wave mode, d omega a Maxwell field, and omega = (i/sigma) (d
iota_T omega + iota_T d omega), T = d_t. This section computes the five-dimensional reductions on Tangherlini and
deduces from them the mode stability of box there. The spectral family: every field is e^(-i sigma t) times a stationary
one, d_t -> -i sigma, in the static chart, f = 1 - mu/r^2, r_h = mu^(1/2); kappa = l (l + 2) is the eigenvalue of -Delta
on S^3, lam that of delta_S d_S on a co-closed 1-form of S^3, and r* the tortoise coordinate, Phi_* = f Phi'.

**Proposition 10.13 (computed; exact).** On five-dimensional Tangherlini, f = 1 - mu/r^2:
 (i) box = 2 delta G delta* equals d delta + delta d on every 1-form (M1).
 (ii) (scalar waves) For u = r^(-3/2) Phi(r) S, S any function on S^3 with Delta S = -kappa S, -f r^(3/2) (delta d u)/S
     = f (f Phi')' + sigma^2 Phi - V_0 Phi, V_0 = (f/r^2)(kappa + 3/4 + 9 mu/(4 r^2)) (M2).
 (iii) (Maxwell, vector type) For A = V Y, V = r^(-1/2) Phi(r), Y any 1-form on S^3: delta A = r^-2 V delta_S Y, (delta
     d A)_t = i sigma r^-2 V delta_S Y, (delta d A)_r = -r^-2 V' delta_S Y, and -f r^(1/2) ((delta d A)_i - r^-2 V
     (delta_S d_S Y)_i) = (f (f Phi')' + sigma^2 Phi - U_1 Phi) Y_i, U_1 = (f/r^2)(-1/4 + 5 mu/(4 r^2)); so for Y
     co-closed with delta_S d_S Y = lam Y the potential is V_1 = (f/r^2)(lam - 1/4 + 5 mu/(4 r^2)). The record's vector
     harmonic is co-closed with lam = (l + 1)^2, symbolic l (M3).
 (iv) (Maxwell, scalar type) For A = a(r) S dt + b(r) S dr -- every scalar-type A in the gauge c = 0, since A - d(c S
     e^(-i sigma t)) has the same dA -- and M = delta d A, with R[W] := (f W'/r)' - kappa W/r^3 + sigma^2 W/(r f): R[r^3
     F_tr] = (r^2 M_t)' + i sigma r^2 M_r; F_tr = -i sigma b - a', and where it vanishes, M_t = kappa a/r^2 and M_r =
     kappa b/r^2; f r^(1/2) R[r^(1/2) Phi] = f (f Phi')' + sigma^2 Phi - V_2 Phi, V_2 = (f/r^2)(kappa + 3/4 - 7 mu/(4
     r^2)); at l = 0, M_r = -i sigma F_tr/f and F = F_tr dt dr; and for every solution of R[W] = 0, A(W) = (-f W' S dt +
     i sigma W S dr/f)/(kappa r) is a Maxwell field with r^3 F_tr = W (M4).
 (v) For r > r_h: V_0 > 0 at every l, V_1 > 0 for lam >= 2, V_2 > 0 for kappa >= 3 (l >= 1), while at l = 0 V_2 is
     negative near the horizon; r* = r + (r_h/2) log((r - r_h)/(r + r_h)) has dr*/dr = 1/f and r* = r - mu/r - (mu^2/3)
     r^-3 + o(r^-3), and f'(r_h)/2 = 1/r_h; and d iota_T omega + iota_T d omega = -i sigma omega for every spectral
     1-form (M5).

*Proof.* M1-M5 of modes5.py. box is built with Christoffel symbols, d and delta from the volume form and the diagonal
metric; M1 on five arbitrary functions of all five coordinates, and the reductions on arbitrary functions of the angles
-- S with the rule d_th^2 S -> ... that imposes Delta S = -kappa S, Y with no condition -- so that (ii)-(iv) hold for
every harmonic and not for a representative only. Four-dimensional controls: Schwarzschild in M1-M4, where the
potentials are f (kappa/r^2 + mu/r^3), f lam/r^2 and f kappa/r^2. Controls: f = 1 - mu/r in five dimensions, not Ricci
flat, where box and d delta + delta d differ; the four-dimensional exponents r^-1 in (ii) and r^0 in (iii); the
four-dimensional weight r^2 F_tr in (iv); and V_2's positivity claimed at l = 0. []

*Deduced (mode stability of box at nonzero frequency).* Let sigma != 0, Im sigma >= 0, and let omega = e^(-i sigma t)
omega_0 solve box omega = 0 for r > r_h, smooth across the future event horizon (in v = t + r*, r and the angles) and
outgoing at infinity: omega_0 = e^(i sigma r) times a function conormal at infinity -- an expansion in powers of
r^(-1/2) suffices, the outgoing fields of five dimensions carrying r^(-3/2) -- the conditions holding uniformly on the
sphere, so that each spherical harmonic component inherits them. Then omega = 0. (a) The scalar step. delta omega solves
delta d (delta omega) = delta box omega = 0, by (i) and delta delta = 0. For each spherical harmonic component u = R(r)
S of it, Phi = r^(3/2) R solves -Phi_** + V_0 Phi = sigma^2 Phi by (ii). At the horizon Phi = e^(-i sigma r*) h(r) with
h smooth at r_h, u being smooth in v; at infinity, V_0 being O(r^-2), the solutions are e^(+-i sigma r*) (1 + O(1/r)),
and the class admits only the first, so Phi = c e^(i sigma r*) (1 + O(1/r)) by (v). If Im sigma > 0, Phi and Phi_* decay
exponentially at both ends, and int (|Phi_*|^2 + V_0 |Phi|^2) dr* = sigma^2 int |Phi|^2 dr* with V_0 > 0 forces Phi = 0:
otherwise sigma^2 would be positive and sigma real. If sigma is real, the Wronskian Im(conj(Phi) Phi_*) is constant,
-sigma |h(r_h)|^2 at the horizon and sigma |c|^2 at infinity, so c = 0 and Phi = 0. So delta omega = 0. (b) The Maxwell
step. Then delta d omega = box omega - d delta omega = 0: omega is a Maxwell potential. Its vector part, each co-closed
component r^(-1/2) Phi Y, has -Phi_** + V_1 Phi = sigma^2 Phi by (iii), with V_1 > 0 since lam >= 2 (on co-closed
1-forms of S^3, delta_S d_S = nabla* nabla + Ric with Ric = 2; Bochner), so Phi = 0 as in (a). Its scalar part at l >=
1: W = r^3 F_tr solves R[W] = 0 by (iv), so Phi = r^(-1/2) W solves -Phi_** + V_2 Phi = sigma^2 Phi with V_2 > 0 by (v);
F_tr = F_vr is smooth across the horizon, so Phi = 0 as in (a), and then F_tr = 0 and M = 0 give a = b = 0 in the gauge
c = 0 by (iv), kappa being nonzero: that part of omega is a gradient. At l = 0, M_r = -i sigma F_tr/f = 0 gives F_tr =
0, which is all of F there. So d omega = 0. (c) The gauge step. By (v) and d omega = 0, omega = (i/sigma) d phi with phi
= omega(T), smooth across the horizon (T = d_v there) and in the class at infinity; d phi = -i sigma omega gives delta d
phi = -i sigma delta omega = 0, so phi is a scalar mode, phi = 0 by (a), and omega = 0.

This is the five-dimensional counterpart, on Tangherlini, of what his Proposition 6.9 takes from [AHW24] Theorem 5.1 on
Kerr; Tangherlini being static, each step is an ODE with a positive potential, save the spherically symmetric Maxwell
sector, which its own equation settles.

*READ.* [Hin26] (alphaXiv, 2026-10-21): pp. 118-119 (Lemma 6.8, Proposition 6.9 and its proof). [KI03b]
(arXiv:hep-th/0308128v4; ROUTES-OPEN.md 4.1): (4.23), (5.17), (5.19) and (5.20), at Q = 0, n = 3, K = 1: (4.23)'s
(k_V^2 + (n - 1) K)/r^2 is lam/r^2, k_V^2 + 2 = (l + 1)^2; F_ab = epsilon_ab E S with r^n E = -k^2 A (5.19) makes their
A a multiple of W = r^3 F_tr, and (5.20) without source is r R[W] = 0 -- (iii)'s and (iv)'s master equations.

*What this gives, and what it does not.* The unmodified gauge potential operator has no mode at sigma != 0, Im sigma >=
0, on five-dimensional Tangherlini, in the class stated: the input his Proposition 6.9 takes from [AHW24] Theorem 5.1,
here by three ODE arguments, with potentials positive at l >= 1. The potentials differ from four dimensions by the terms
the sphere S^3 brings -- 3/4 in V_0 and V_2 and -1/4 in V_1, and 9/4, 5/4 and -7/4 times mu/r^2 -- and positivity
survives in each sector at l >= 1; at l = 0 the Maxwell scalar potential is negative near the horizon, and that sector
is settled by the equation, M_r = -i sigma F_tr/f, not by positivity. Not done, and OPEN: that the kernel elements of
his spectral family in five dimensions lie in the class -- [Hin26c] Theorem 9.5(5) in five dimensions, kernel elements
in A^(3/2 - eps) by 10.18(b) with S-bar = 0 -- and the index 0 that turns injectivity into invertibility (his p. 119),
with the vanishing carried from r > r_h to the region inside the horizon by the standard interior uniqueness (10.76 (b);
D149); his Proposition 6.5, from section 6.1's trapping (whose input, his Lemma 6.4, 10.17 deduces), and the uniform
estimates of [Hin26c] Theorem 9.5 in five dimensions, which with this give his Proposition 6.9 there for small
E^Upsilon; and the low-energy part (10.15). Nothing of this section is proved: Proposition 10.13 is computed, and the
mode stability is deduced. 10.19 deduces all of these but the low-energy part, on the reading of [Hin26c] section 9
stated there (10.20 widens it for the low-energy part).

### 10.17 Strong trapping admissibility of the gauge potential operator in five dimensions (`trap5.py` T0-T4; D59)

*The setting.* [Hin26] Proposition 6.5, the mode stability of box^Upsilon at high energies (|sigma| >= C, Im sigma >=
0), comes from [Hin26c] Theorem 9.16, whose input at the trapped set is his Lemma 6.4: box^Upsilon is strongly trapping
admissible ([Hin26c] Definition 5.8). That is, for every eps > 0 there is a stationary positive definite fiber inner
product on pi^*(T^*), homogeneous of degree 0, with sigma^-1 (1/2i) (S_sub - S_sub^*) < eps at the trapped set Gamma_0
((6.14)), Gamma_0 = {xi = H_G xi = 0} in the future characteristic set over r > r_+ ([Hin26c] Definition 4.13).
E^Upsilon vanishes near the trapped set by his requirement (6.1), so only box = 2 delta G delta* enters, with S_sub(box)
= -i nabla_{H_G} ((6.13), from [Hin17] Proposition 4.1). His proof uses a frame e_0 = zeta, e_1, e_2, e_3
((6.15)-(6.16b)) in which nabla_{H_G} = H_G + 2 sigma N with N nilpotent ((6.16c)). In five dimensions the angular
directions orthogonal to the motion form a plane, not a line; this section computes the frame's part and carries the
plane by metric compatibility. Notation: zeta = -sigma dt + xi dr + eta, G = g^-1(zeta, zeta), H_G = d_zeta G d_z - d_z
G d_zeta, C = r^2 |eta|^2_g, the Casimir of S^3 (his Carter constant at a = 0), and w^(0) = f^(1/2) dt, w^(1) = f^(-1/2)
dr with zeta_(0), zeta_(1) the components of zeta along them.

**Proposition 10.14 (computed; exact).** On five-dimensional Tangherlini, f = 1 - mu/r^2, r_h = mu^(1/2):
 (i) S_sub(box) = -i nabla^{pi^* T^*}_{H_G}: conjugated to half densities by |dg|, box = 2 delta G delta* has principal
     part G Id and subprincipal part i Gam^c_ab d_{zeta_b} G (T0).
 (ii) The trapped set is {r^2 = 2 mu, xi = 0} in the future characteristic set: on G = 0 at xi = 0, H_G xi = (2 C/(f
     r^5))(r^2 - 2 mu), whose only zero in r > r_h is r^2 = 2 mu; there C = 4 mu sigma^2 > 0, the differentials of xi,
     H_G xi and G are independent, and under H_G/(H_G t) the normal expansion rate is nu = (2 mu)^(-1/2), the inverse of
     the photon-sphere radius (T1).
 (iii) H_G C = 0, and on G = 0 the frame e_0 = zeta, e_1 = r (zeta_(1) w^(0) + zeta_(0) w^(1)), e_2 = (r^2/2) (zeta_(0)
     w^(0) + zeta_(1) w^(1) - eta) has the Gram matrix C J, J = [[0, 0, -1], [0, 1, 0], [-1, 0, 0]], of determinant
     -C^3; an angular covector is g-orthogonal to all three iff it is orthogonal to eta (T2).
 (iv) On G = 0: nabla_{H_G} e_0 = 0, nabla_{H_G} e_1 = -2 sigma e_0, nabla_{H_G} e_2 = -2 sigma e_1 (T3).
 (v) For N e_0 = 0, N e_1 = e_0, N e_2 = e_1, the operator N + N^* has norm 2^(1/2) eta^(1/2) for the inner product
     diag(1, eta^-1, eta^-2) in (e_0, e_1, e_2)/C^(1/2), and 2^(1/2) eta for diag(1, eta^-2, eta^-4) (T4).

*Proof.* T0-T4 of trap5.py, from the definitions in the static chart, the covector components symbolic and the
identities reduced modulo G in zeta_t. Four-dimensional controls, Schwarzschild in T0-T3: (i); the photon sphere r = 3
mu/2 with nu = 2/(3^(3/2) mu) = 1/(3^(3/2) M); the Gram matrix of (6.16a); and (6.16c) at a = 0, with e_3 = r (zeta_(3)
w^(2) - zeta_(2) w^(3)) parallel. Controls: the coordinate density dx in place of |dg| in (i); the four-dimensional
ratio r_ph = (3/2) r_h claimed in five dimensions; the Gram matrix off the characteristic set; e_1 without its weight r;
and a diagonal entry in N. []

*Remarks (computed).* (a) In these conventions nabla_{H_G} e_1 = -2 sigma e_0, in four dimensions as in five; (6.16c)
prints +2 sigma, which is the computed relation with e_1 replaced by -e_1. The twenty-seventh verifier traced his sign
(D63): with his sigma = -<., d_t> and the standard H_p the coefficient is -2 sigma; his source, [Hin24a]
(arXiv:2408.06712) Proposition 3.21 (p. 60), obtains +2 sigma from alpha_0 = -g^-1(D_b e_1, e_2) with Remark 3.22's e_2,
printed with the sign opposite to its (3.34b) -- the likeliest cause a sign slip in e_2 -- and +2 sigma holds for sigma
= +<zeta, d_t>, or with e_1 -> -e_1. The matrix is nilpotent either way, which is all the proof uses. (b) For the inner
product his proof names, diag(1, eta^-1, eta^-2, eta^-3), the norm is 2^(1/2) eta^(1/2) -- e_3 does not enter, N
vanishing on it -- where his text says O(eta); O(eta) holds for the squared weights. Either tends to 0, which is all the
proof uses. His Proposition 8.3 (p. 147) has the same wording (as the twenty-seventh verifier read).

*Deduced.*
 (a) (his Lemma 6.4 in five dimensions) Near Gamma_0, where C > 0 by (ii), pi^*(T^*) = P + V_perp, P = span{e_0, e_1,
     e_2} and V_perp its g-orthogonal complement, the angular covectors orthogonal to eta (iii), on which g is positive
     definite. P is nabla_{H_G}-invariant by (iv); nabla is metric, so V_perp is invariant too and nabla_{H_G} is g-skew
     there. Take B_eta = diag(1, eta^-1, eta^-2) on P in (e_0, e_1, e_2)/C^(1/2) -- stationary and homogeneous of degree
     0, since H_G C = 0 and C has degree 2 -- and g on V_perp. In these frames B_eta is constant, -i H_G is symmetric
     (H_G preserves the symplectic volume) and H_G sigma = 0, so by (i) sigma^-1 (1/2i) (S_sub - S_sub^*) is N + N^* on
     P and 0 on V_perp, of norm 2^(1/2) eta^(1/2) by (v): below any eps > 0 for small eta. So box is strongly trapping
     admissible on five-dimensional Tangherlini, and so is box^Upsilon when E^Upsilon vanishes near r^2 = 2 mu ((6.1))
     -- a choice of the supports of c_H and c^Upsilon, as in his Proposition 6.12.
 (b) ([Hin26c] Proposition 4.19 in five dimensions) On Gamma_0 the flow is the t-translation together with the geodesic
     flow of the round S^3, which is periodic, and it is normally hyperbolic at the uniform rate nu of (ii): the trapped
     set is r-normally hyperbolic for every r.

*READ.* [Hin26] (alphaXiv, 2026-10-22): pp. 113-116 (section 6: (6.1)-(6.3), Lemma 6.1, Remark 6.2; section 6.1:
(6.12)-(6.16c), Lemma 6.4 and its proof, Proposition 6.5). [Hin26c] (arXiv:2606.28008v1; alphaXiv, 2026-10-22): pp. 88
(Definition 4.13, Lemma 4.14), 90-91 (Proposition 4.19), 101-103 (Example 5.4, Remark 5.6, section 5.1.1, Definition
5.8, Remark 5.9), 265 (the high-frequency control, resting on strong trapping admissibility).

*What this gives, and what it does not.* The trapping input of his Proposition 6.5 holds on five-dimensional
Tangherlini: the 1-form wave operator, and with it box^Upsilon, is strongly trapping admissible, by his argument -- the
frame and its nilpotent connection matrix are the same -- with the second angular direction carried by metric
compatibility; the trapped set is the photon sphere r^2 = 2 mu, with expansion rate 1/r_ph per unit t. Not done, and
OPEN: [Hin26c] Theorem 9.16 in five dimensions -- the high-energy estimates themselves, with the radial point estimates
at the horizon and at infinity; [Hin26c] works "in 3 + 1 dimensions for concreteness" (Remark 5.6) -- and with it his
Proposition 6.5 there; the other OPEN items of 10.15-10.16 stand. Nothing of this section is proved: Proposition 10.14
is computed, and (a)-(b) are deduced. 10.19 computes the rest of Theorem 9.16's inputs and deduces it, with his
Proposition 6.5, on the reading stated there.

### 10.18 The structure and thresholds of the gauge potential operator in five dimensions (`thresh5.py` U1-U4; D60)

*The setting.* [Hin26c]'s estimates for a stationary wave-type operator P_0 = -2 d_t* rho (rho d_rho - (n - 1)/2 - S) +
P_0^(0) + Q d_t* - g00 d_t*^2 (its Definition 9.4, n the spatial dimension; (5.1a), with 1 at n = 3, Remark 5.6) need
threshold conditions on the orders: at the event horizon s > 1/2 + vartheta_H+, vartheta_H+ the supremum over N^*H+ of
the spectrum of (rho^2/(2 (r_+ - m))) xi^-1 sigma_1((P_0 - P_0^*)/2i) (Definition 5.11(4)); at infinity, through S-bar,
the bottom of the spectrum of S over the boundary ((5.2), (9.16c), (9.20), Lemma 5.12). S-bar names two things here, as
in the sources, whose difference [Hin26]'s footnote 60 points out: the endomorphism of Proposition 10.15 (i)-(ii), his
S-bar_{E-bar^Upsilon} of (6.6), and, in a threshold or a weight, the number min Re spec of it ([Hin26c] (5.2)). [Hin26]
Lemma 6.1 puts box^Upsilon in this class, his Lemma 6.3 computes S-bar for E^Upsilon on Minkowski ((6.11)), and his
footnote 71 gives the horizon threshold 3/2 for the unmodified 1-form operator. 10.15 named Lemma 6.1's structure and
this regularity as OPEN in five dimensions; this section computes them, with the trace weight 2/3 at infinity and at the
horizon, f = 1 - mu/r^2, r_h = mu^(1/2). At a = 0, rho^2/(2 (r_+ - m)) is 1/f'(r_+).

**Proposition 10.15 (computed; exact).**
 (i) On 4+1 Minkowski, in t* = t - r and the Cartesian frame (dt, dx^i), box^Upsilon = 2 (delta + E-bar) G delta*, with
     E-bar h = -gam (2 iota_c# h - (2/3)(1 - e) c tr h), c = r^-1 dt, is -2 d_t* rho (rho d_rho - 3/2 - S-bar) plus a
     stationary operator: no d_t*^2 term, and S-bar omega = gam (omega + omega_t dt* + e <dt*, omega> dt) (U1).
 (ii) The spectrum of S-bar is gam (1 - e), 2 gam, and gam on the three angular directions: his (6.11)'s, the weight
     2/(D - 2) making (2/(D - 2))(1 - D/2) = -1 in every dimension (U2).
 (iii) At N^*H+ in the ingoing chart (r = r_h, zeta = xi dr), the subprincipal symbol of box + 2 gam_H E_H G delta*, E_H
     h = 2 iota_c_H# h - (2/3) c_H tr h, c_H = c_v dv + c_r dr, on half densities by |dg|, is i xi f'(r_h) K with K
     lower triangular, its diagonal 1 + c_v gam_H r_h, -1 + 2 c_v gam_H r_h and c_v gam_H r_h (three times), and its
     angular block diagonal (U3).
 (iv) On Tangherlini, with t* = t - r, g^-1(dt*, dt*) = -(2 mu rho^2 - mu^2 rho^4)/(1 - mu rho^2), in rho^2 C^oo, and
     g - g-bar = O(rho^2) in the frame (dt, dr, r dw) (U4).

*Proof.* thresh5.py U1-U4: (i) from the definitions in Cartesian coordinates, d_t = d_t* and d_x^i = d_x^i - (x^i/r)
d_t*, exact on a stereographic chart of the sphere; (iii) from the full symbol on half densities, as 10.17's T0.
Four-dimensional controls: (i) with rho d_rho - 1 and the same S-bar at the weight 1; (ii) his (6.11)'s spectrum; (iii)
1 + 2 c_v gam mu, -1 + 4 c_v gam mu and 2 c_v gam mu (twice), the threshold 3/2 of his footnote 71 at gam_H = 0.
Controls: the weight 1 in five dimensions, where S-bar's e becomes (3e - 1)/2 and its spectrum (3/2)(1 - e) gam, 2 gam,
gam; the scalar wave operator, K = 0, threshold 1/2; and f = 1 - mu/r in five dimensions, O(rho). []

*Deduced.*
 (a) (the horizon threshold) For small |c_v gam_H| the diagonal entries 1 + c_v gam_H r_h and -1 + 2 c_v gam_H r_h are
     distinct from each other and from the angular ones, so K is diagonalizable and, for a suitable fiber inner product,
     vartheta_H+ is the largest of them: 1 + c_v gam_H r_h. It is 1 at gam_H = 0, as in four dimensions, and 1 at every
     gam_H for 10.15's c_H = -(1/2) chi dr (c_v = 0, chi = 1 at r_h). So the threshold behind 10.15's deduced (a) is s >
     3/2 in five dimensions; his footnote's "close to 3/2 for small gamma_H" is, for this c_H, equality.
 (b) (the structure at infinity) By (i)-(ii), [Hin26] Lemma 6.1(1) holds in five dimensions with rho d_rho - 3/2 for rho
     d_rho - 1 and S-bar's spectrum his; by (iv) the differences (6.7) gain a power, S_E - S-bar in rho^2 C^oo and the
     zero energy operators' difference in rho^4 Diff_b^2, Tangherlini's Christoffel symbols differing from Minkowski's
     by O(rho^3) where Kerr's differ by O(rho^2). The transport equation (rho d_rho - 3/2 - S-bar) u = 0 gives outgoing
     kernel elements of the spectral family the leading behaviour rho^(3/2 + S-bar) (his (9.21): rho^(1 + S), the
     endomorphism; (9.20) is the space A^(1 + S-bar - eps), the number), which lies in rho^r L^2(r^3 dr) iff r < -1/2 +
     S-bar: the threshold (9.16c) at R_out is unchanged on the Euclidean density, and Lemma 5.12's vartheta_out = 2
     S-bar (to within eps) carries over, -2 d_t* rho (rho d_rho - 3/2) being symmetric for the five-dimensional density.

*READ.* [Hin26] (alphaXiv, 2026-10-22): pp. 113-115 (Lemma 6.1, (6.4a)-(6.7), footnote 60, Lemma 6.3, (6.10)-(6.11)),
124 (footnote 71). [Hin26c] (alphaXiv, 2026-10-22): pp. 100 ((5.1a)-(5.2)), 101 (Example 5.4, Remark 5.6), 104-105
(Definitions 5.10-5.11, Lemma 5.12, Definition 5.13), 158 (Definition 9.4), 161-163 ((9.16a)-(9.16c), Theorem 9.5 with
(9.20)-(9.21)).

*What this gives, and what it does not.* The numbers [Hin26c]'s estimates need from the gauge potential operator in five
dimensions: the horizon threshold is 3/2, as in four, and stays 3/2 under 10.15's horizon modification; S-bar has his
spectrum; the structure is his with (n - 1)/2 = 3/2, Tangherlini's deviation from Minkowski one power better than
Kerr's. Not done, and OPEN: the radial point, propagation and trapping estimates themselves in five dimensions ([Hin26c]
sections 7 and 9, general in their arguments, written in 3 + 1); the threshold at R_in, vartheta_in of [Hin26c]
Definition 5.11(6) -- a property of the operator, which the order functions must clear; and the rest of item 2. Nothing
of this section is proved: Proposition 10.15 is computed, and (a)-(b) are deduced. 10.19 computes the similarity at R_in
from which the threshold there, -1/2 - S-bar, is deduced, and the trapping and dynamical inputs, and deduces his
Propositions 6.5 and 6.9 on the reading stated there.


### 10.19 The inputs of the high-energy and Fredholm estimates in five dimensions (`hienergy5.py` V1-V4; D62)

*The setting.* [Hin26] Proposition 6.5, the invertibility of the spectral family of box^Upsilon for |sigma| >= C, Im
sigma >= 0, is [Hin26c] Theorem 9.16 with his Lemma 6.4 as its input at the trapped set; his Proposition 6.9 adds
[Hin26c] Theorem 9.5's Fredholm estimates at bounded sigma != 0, uniform under small perturbations, and the mode
stability of the unmodified operator (10.16 in five dimensions). [Hin26c] section 9 sets up stationary asymptotically
Minkowski wave operators on R^n (his Definition 9.4: P_0 = -2 d_t* rho (rho d_rho - (n - 1)/2 - S) + ...), and the
symmetry its radial point estimates at infinity rest on is stated for the density r^(n-1) |dr dg| ((9.37), (9.41)); but
it treats scalar operators only -- "the purely notational modifications required to treat operators acting on vector
bundles are left to the reader" (p. 158) -- and states his Theorems 9.5 and 9.16 on the Kerr model with
three-dimensional numbers: (9.20)'s A^(1 + S-bar - eps) and (9.21)'s rho^(1 + S), (9.55) in Part (5) of the proof (p.
172), and his Proposition 4.24 in section 9.3.6 (p. 193). From the operator his estimates take: the horizon threshold
vartheta_H+ ((9.16a); 10.18: 1), with the radial point structure (9.24); the threshold at the incoming radial set R_in,
vartheta_in = sup over the boundary of sigma_1^b(Im P_0-hat(0))(-2 dr/r) - 2 Re S ((9.16b), (9.32)); the bottom S-bar of
the spectrum of S at R_out ((9.16c); 10.18); at high energy the trapped set's hypotheses (Gamma.1)-(Gamma.4) and the
loss function delta_Gamma ((9.79)-(9.81)); the global dynamics (his Proposition 4.24 on Kerr, and the paragraph after
(9.5)); and a timelike dr inside the horizon for his energy estimate there (Proposition 9.35). 10.18 left R_in and the
rest OPEN. As there, S-bar is the endomorphism in Proposition 10.16(i) and the number min Re spec S-bar ([Hin26c] (5.2))
in a threshold.

**Proposition 10.16 (computed; exact).** On 4+1 Minkowski and five-dimensional Tangherlini, f = 1 - mu/r^2:

 (i) (the incoming radial set) rho (rho d_rho - c) is skew for the density rho^(-5) d rho exactly when c = 3/2; and for
     box^Upsilon at the trace weight 2/3, the first-order part A_w of its zero energy operator at the incoming covector
     (the coefficients of the spatial derivatives contracted with the radial direction, times r) satisfies A_w + S-bar =
     D S-bar D, D the reflection of the radial direction, so spec (A_w + S-bar) = spec S-bar = gamma (1 - e), 2 gamma,
     gamma; at gamma = 0 both vanish (V1).
 (ii) (the trapped set) For the semiclassical family at z = 1, G_1 = -1/f + f xi^2 + C/r^2 (C the S^3 Casimir), the
     trapped set is r^2 = 2 mu, xi = 0, C = 4 mu, the only critical point with r > r_h; the linearised flow on Sigma_1
     has eigenvalues +-nu, nu = 4 (2 mu)^(-1/2), with phi_s/u = xi +- (nu/(2 f)) (r - r_ph) as left eigenvectors and
     {phi_u, phi_s} = nu/f > 0; d_C G_1 = 1/r^2 != 0; beta_0 = 1/f(r_ph) = 2, the same for t* = t - F(r); and nu/(4
     beta_0) = (8 mu)^(-1/2), half 10.17's expansion rate per unit t (V2).
 (iii) (the loss) At a point of the trapped set, nabla_{H_G} on 10.17's frame is e_0 -> 0, e_1 -> -2 e_0, e_2 -> -2 e_1,
     with no component in V_perp, which it preserves; with diag(1, eta^-1, eta^-2) on span{e_0, e_1, e_2}, p_1 = -(M +
     M^*)/2 there has spectrum 0, +-(2 eta)^(1/2), so that there sup p_1/(2 beta_0) = (2 eta)^(1/2)/4 and 2 sup p_1/nu =
     (mu eta)^(1/2) (V3).
 (iv) (the dynamics) On Sigma_1, f^2 xi^2 = 1 - C W with W = f/r^2, and W' = 2 (2 mu - r^2)/r^5 on r > r_h: one critical
     point, a maximum W = 1/(4 mu) at r^2 = 2 mu, with W(r_h) = 0 and W -> 0 at infinity; f is increasing and vanishes
     at r_h, so g_tt = -f < 0 for r > r_h and, in the ingoing chart, g^-1(dr, dr) = f < 0 on 0 < r < r_h; and g_vr = 1
     and g(g^-1 dr, -d_r) = -1, so g^-1(dr) is future directed there, -d_r lying in the future cone of d_v (V4).

*Proof.* V1-V4 of hienergy5.py. V1 builds box^Upsilon on 4+1 Minkowski with thresh5.py's minkowski, reads A_w off the
coefficients of the spatial first derivatives and S-bar off those of d_t*, and checks the conjugation exactly over the
sphere; V2 linearises H_{G_1} on Sigma_1, where C = r^2 (1/f - f xi^2) is conserved; V3 evaluates trap5.py's frame and
connection at theta = pi/4, sigma = 1, eta along d theta, and decomposes; V4 is algebra. Four-dimensional controls: (i)
at the weight 1, the same; (ii) r = 3 mu/2, beta_0 = 3, nu/(4 beta_0) = 1/(3^(3/2) mu), trap5.py T1's rate halved; (iii)
the same spectrum, 2 sup p_1/nu = (3 mu^2 eta/2)^(1/2); (iv) W' = (3 mu - 2 r)/r^4. Controls: the constant 1 for 3/2;
the weight 1 in five dimensions, where spec (A_w + S-bar) is not his (6.11)'s; A_w with its sign flipped -- at R_out A_w
does not enter (xi_sc = 0) -- where -A_w + S-bar is not similar to S-bar; the four-dimensional ratio r_ph = (3/2) r_h in
(ii) and (iv); and in (iii) a connection with a diagonal entry, where sup p_1 does not tend to 0. The identity of (i) is
structural, as the twenty-eighth verifier observed: S-bar = (1/2) M(dt - dr) and A_w + S-bar = (1/2) M(dt + dr), M the
first-order symbol of 2 E-bar G delta*, built from c, a multiple of dt, and g, so it holds by reflection covariance at
every weight and in every dimension; V1 checks it. []

*Deduced.*

 (a) (The incoming threshold.) By (9.38a)-(9.38b), p_1 - 2 Re S at R_1,in is -2 Re (A_w + S-bar) in any fiber inner
     product, and by (i) A_w + S-bar is similar to S-bar; so vartheta_in = -2 S-bar to within eps, exactly when S-bar is
     diagonalisable (as in his Lemma 5.12 and Remark 10.2), and (9.16b) reads r + alpha_+ > -1/2 - S-bar: the mirror of
     10.18's -1/2 + S-bar at R_out. At gamma = 0 it is his p. 122's r > -1/2. The operator being of his class with (n -
     1)/2 = 3/2 (i), his radial point estimates at infinity -- written for scalar operators, the bundle case left to the
     reader (p. 158) -- carry these thresholds for n = 4 on the reading of (d). Admissible order functions (his
     Definition 5.11) exist at all weights: s constant above 3/2 for r <= r_Gamma,+ (10.18), decreasing along the flow
     to R_out, and as large as needed at R_in.
 (b) (The trapped set.) By (ii), (Gamma.1)-(Gamma.3) hold: Gamma_u/s are the separatrices C = 4 mu of the hyperbolic
     point of the radial flow (stable manifold theorem) times the S^3 directions, of codimension 1 in Sigma_1^+ and
     transversal along Gamma; the sign of {phi_u, phi_s} is a normalisation (phi_u -> -phi_u preserves (Gamma.2)), its
     content that the bracket does not vanish. By (iii) and 10.17 -- p_1 = 0 on V_perp (deduced there), and the
     isometries, transitive on Gamma, carrying (iii)'s point to every point -- (Gamma.4) holds with gamma_+ = (2
     eta)^(1/2)/4 as small as wished, gamma_- < 0 and delta_Gamma(0) = (mu eta)^(1/2) -> 0 as eta -> 0 -- the
     "arbitrarily small h^(-eps)-loss" of his remark after (9.81). The gap nu_min/(4 beta_0) = (8 mu)^(-1/2) is, in
     units of Im sigma, half the expansion rate per unit t, as in four dimensions.
 (c) (The dynamics.) By (iv), on Sigma_1 a bicharacteristic with C < 4 mu passes between the horizon and infinity, one
     with C > 4 mu turns once and returns to the end it came from, and one with C = 4 mu lies on Gamma or tends to it:
     each tends to R_H+, Gamma, R_in or R_out, or crosses into the horizon -- the spectral-side counterpart of his
     Proposition 4.24, which his section 9.3.6 uses. There is no ergoregion, so at bounded sigma the characteristic set
     over the interior of X lies over r <= r_h (his p. 159); and dr is future timelike inside the horizon ((iv)), his
     Proposition 9.35's hypothesis.
 (d) With 10.18, the inputs of [Hin26c] Theorems 9.5 and 9.16 that the operator supplies are in hand in five
     dimensions: computed -- A_w + S-bar = D S-bar D, nu, beta_0, the spectrum of p_1 at a point, W, the time
     orientation inside -- or deduced -- vartheta_H+, vartheta_in and its threshold, (Gamma.1)-(Gamma.4); the horizon's
     radial point structure ((9.24): beta_0 > 0, beta > 0, a quadratic defining function; his p. 165, for a
     non-degenerate red-shift) and a global t* with dt* past timelike (his Definition 9.3) are those of a
     non-degenerate static horizon, f'(r_h) > 0 by (iv), stated and not computed here. The reading is (i) that his
     scalar estimates hold for operators on bundles with the notational modifications he leaves to the reader, and (ii)
     that his Theorems 9.5 and 9.16 hold restated for n = 4 -- (9.20) and (9.55) with 3/2 for 1 (10.18(b)), his
     Proposition 4.24 replaced by (c) -- neither verified here line by line (since written out, (ii) as 10.75
     (lviii)-(lix); D164). On it, Theorem 9.16 gives the spectral family of box^Upsilon invertible for Im sigma >= 0,
     |sigma| >= C_0, between the spaces (9.18), with the bound |sigma|^(-1 + delta_Gamma(Im sigma - eps)) on its
     inverse (p. 193): [Hin26] Proposition 6.5 in five dimensions, whose uniformity over a compact set of parameters is
     that of his estimates under small perturbations, part of the reading. Theorem 9.5 gives it Fredholm at bounded
     sigma != 0, of index 0 (constant in sigma, and 0 by the invertibility at large |sigma|), with kernel elements in
     A^(3/2 + S-bar - eps) (10.18(b)). For the unmodified box (S-bar = 0) a kernel element is A^(3/2 - eps) at infinity
     and smooth on X: in the t-family it is e^(i sigma r) times a conormal function, smooth across the horizon --
     10.16's class -- so it vanishes for r > r_h by 10.16, and inside, dr being timelike (c), by uniqueness for the
     Cauchy problem in r with vanishing data at r_h. Injective of index 0, the spectral family of box is invertible at
     every sigma != 0, Im sigma >= 0; the Fredholm estimates hold uniformly under small perturbations within the class,
     so that of box^Upsilon is invertible at Im sigma >= 0, |sigma| >= c_0, for small e, gamma and gamma_H (E^Upsilon
     vanishing near the trapped set, (6.1)): his Proposition 6.9 in five dimensions.

*READ.* [Hin26c] (alphaXiv, 2026-10-22): pp. 81 (Definition 4.5), 98 (Proposition 4.24), 100 ((5.2)), 104-105
(Definition 5.11, Lemma 5.12), 157-159 (Notation 9.2, Definitions 9.3-9.4 and the sentence after, (9.4)-(9.6)), 161, 163
((9.16a)-(9.16c), Theorem 9.5), 165 ((9.24)), 167-168 (Proposition 9.10, (9.32)-(9.42)), 172 (section 9.2.3, (9.55)),
174-175 (Theorem 9.16, Remarks 9.17-9.18), 178 (Proposition 9.25), 180 (Propositions 9.26-9.27), 182
((Gamma.1)-(Gamma.4), (9.79)-(9.81)), 191 (Proposition 9.35), 193 (section 9.3.6, the proof of Theorem 9.16). [Hin26]
(alphaXiv, 2026-10-22): pp. 113, 114 (footnote 60), 116 (Lemma 6.4's proof, Proposition 6.5), 118-119 (Lemma 6.8's
proof, Proposition 6.9 and its proof), 121-122 (Proposition 6.12, the orders in its proof), 200 (Remark 10.2).

*What this gives, and what it does not.* The inputs [Hin26c]'s spectral theory at nonzero frequency takes from the
operator are in hand for box^Upsilon on five-dimensional Tangherlini, computed or deduced: the threshold at R_in,
deduced from V1's similarity, is the mirror of R_out's, -1/2 - S-bar against -1/2 + S-bar; the trapped set is a single
photon sphere, its gap half the expansion rate per unit t and its loss as small as wished, as in four dimensions; and
the dynamics and the interior are his. The dimension enters his statements through (n - 1)/2 and, in his Theorems 9.5
and 9.16, through three-dimensional numbers to be restated, and his estimates are written for scalar operators. With
them his Propositions 6.5 and 6.9 are deduced in five dimensions on the reading of (d), and 10.16's OPEN items -- the
kernel's class, the index 0, the interior -- are settled at the level of deduction. Not done, and OPEN: the line-by-line
check that [Hin26c] section 9's proofs hold for n = 4 and on bundles (the scalar-to-bundle step; Propositions 9.9-9.11
and 9.22-9.27, Lemmas 9.20, 9.21 and 9.33, Theorem 9.28 on [Dya16], Proposition 9.35; Parts (3) and (5) of section 9.2.3
and section 9.3.6, with their three-dimensional numbers); the low-energy theory in five dimensions -- the zero energy
operator's Fredholm property (his Theorem 9.36, on the indicial gap of 10.12 and 10.15), tf-admissibility (his
Definition 5.10 and Lemma 6.8) and the uniform low-energy estimate (his Theorem 9.41) -- and with it his Proposition
6.12 (10.20 deduces them); and [Hin26a] Theorem 5.2, section 6 (10.21 deduces it from Theorem 5.2) and Theorem B.1
(10.22 and 10.23 deduce Theorems 5.2 and B.1 on readings). Nothing of this section is proved: Proposition 10.16 is
computed, and (a)-(d) are deduced.


### 10.20 The low-energy theory in five dimensions (`lowenergy5.py` L1-L3; D64)

*The setting.* [Hin26] Proposition 6.12 makes box^Upsilon mode stable on the whole closed upper half plane, sigma = 0
included, for E^Upsilon with a horizon modification gamma_H in (0, eps_0] and small e and gamma at infinity: by his
Proposition 6.9 away from sigma = 0 (10.19 in five dimensions), and near it by a perturbation in two steps -- Step 1,
the horizon modification alone, through a Grushin problem augmented by W* and a pairing <., f*> with f* compactly
supported in the interior and <W*, f*> = 1 (his (6.24)), the horizon functional entering through (6.26), whose estimate
(6.27) is [Hin26c] Theorem 9.41's for the augmented operator; Step 2, the modification at infinity, by the uniformity of
the zero energy and transition face estimates. These rest on [Hin26c] sections 9.4-9.6: Theorem 9.36 (the zero energy
operator is b-Fredholm when the weight, shifted by the density, lies in an indicial gap), tf-admissibility (Definition
5.10; Proposition 9.40 for the wave operator, his Lemma 6.8 for box^Upsilon), Corollary 9.43 (index 0) and Theorem 9.41
(uniform low-energy estimates). Section 9.5 is stated for R^n -- (9.110) with (n - 1)/2, Theorem 9.38 with n/2,
Corollary 9.39 with -n + 2 + beta, and Proposition 9.40 for every n >= 3 with the weights (0, n - 2) -- while Theorems
9.36 and 9.41 and Corollary 9.43 write the shift of his Lemma 3.11 at n = 3, alpha + 3/2. 10.15 computed the zero energy
indicial roots, kernel, cokernel functional and pairings in five dimensions, and left the index 0, tf-admissibility and
the estimates OPEN.

**Proposition 10.17 (computed; exact, and numerical where said).** On 4+1 Minkowski and five-dimensional Tangherlini:

 (i) (the transition face) The 1-form wave operator, box^Upsilon at gamma = 0, acts componentwise in the Cartesian frame
     on 4+1 Minkowski, and its spectral family conjugated by e^(i sigma r) is Delta_e - sigma^2 on each component (L1).
 (ii) (the Bessel reduction) At n = 4, u = r^-1 w turns -u'' - (3/r) u' + l (l + 2) u/r^2 - u = 0 into Bessel's equation
     of order l + 1; the exponents at r = 0 are l and -(l + 2), in rho^ = 1/r^ the zero energy roots -l and l + 2 of
     10.15's vl family, the gap (0, 2) at l = 0; and numerically (mpmath, 30 digits, l = 0, ..., 4) x^(l+1)
     H^(1)_(l+1)(x) -> -(i/pi) Gamma(l + 1) 2^(l+1) as x -> 0, e^(-ix) x^(1/2) H^(1)_(l+1)(x) -> (2/pi)^(1/2) e^(-i
     ((l + 1) pi/2 + pi/4)) as x -> oo, and on the imaginary ray H^(1) decays and H^(2) grows (L2).
 (iii) (the weights) rho^a lies in rho^alpha L^2(r^3 dr) near infinity iff a > alpha + 2, so his Lemma 3.11's shift is
     n/2 = 2; and on Tangherlini with t* = t - r, 2 g00 W* = -4 mu rho^4 dt + O(rho^5), from g00 of thresh5.py U4 and
     W*'s leading term rho^2 dt of 10.15 (L3) -- that d_sigma^2 of the spectral family is 2 g00 Id, so that this is
     d_sigma^2 box(0) W*, is deduced from his Definition 9.4, not computed by L3; 10.15(vi) uses t* = t - r_*, which
     differs from t - r by O(mu/r) and moves d_sigma box(0) W* only at rho^5.

*Proof.* L1-L3 of lowenergy5.py. L1 builds the operator with thresh5.py's minkowski, applies it to e^(-i sigma t*) e^(-i
sigma r) w(x) with w abstract, and checks every coefficient exactly over the sphere; L2 is exact for the reduction and
the exponents, and numerical (mpmath) for the Hankel asymptotics, which are standard ([Hin26c] cites [Olv97]); L3 is
exact. Four-dimensional controls: (i) at n = 3, the same; (ii) u = r^(-1/2) w, order l + 1/2, exponents l and -(l + 1),
the range (0, 1); (iii) the shift 3/2. Controls: gamma = 1 in (i), where the modification does not act componentwise;
the conjugation by e^(-i sigma r); the range (0, 3) claimed in (ii); and in (iii) the Coulomb fall-off rho of four
dimensions put on W*, where the term is rho^3. []

*Deduced.*

 (a) (Theorem 9.36 at n = 4) With s_0 > 3/2 at the horizon (10.18), no ergoregion and dr timelike inside the horizon
     (10.19(c)), the zero energy operator of box^Upsilon is Fredholm on the b-spaces of weight alpha with alpha + 2 in
     an indicial gap, his (3.47) holding with the shift of (iii); its kernel elements lie in A^beta for beta below the
     top of the gap.
 (b) (Proposition 9.40 at n = 4) By (i) the transition face operator of the unmodified box is, on each component, the
     conjugated Helmholtz operator. By (ii) and his argument -- outgoing, or for Im sigma^ > 0 decaying, forces H^(1),
     whose size r^^-(l+2) near r^ = 0 is not O(r^^-beta) for beta < 2, and the adjoint condition with -n + 2 + beta =
     -2 + beta in the same way -- box is tf-admissible with every weight in (0, 2), as his Proposition 9.40 states for
     n >= 3 (READ). The range is sharp: at l = 0 the outgoing solution is admitted for beta > 2.
 (c) (his Lemma 6.8 in five dimensions) The transition face operator depends only on the operator at infinity (his
     (6.18a), Lemma 6.1(2), 10.18(b)); for small gamma and e >= 0 the Fredholm estimates (9.111) hold uniformly, so
     box^Upsilon is tf-admissible with a weight in (0, 2), and by his Corollary 9.39 with every weight in the indicial
     gap (0, lam_s1,2) of 10.15(i). The horizon modification is compactly supported and does not enter.
 (d) (Corollary 9.43 at n = 4) The zero energy operators of box and box^Upsilon have index 0 on the spaces of (a), with
     alpha + 2 in the gap. For box, whose kernel is the span of W* (10.15(a)), the cokernel is one-dimensional, and
     10.15(iv)'s functional at the horizon, which annihilates the range and does not vanish (10.15(v)), spans it.
 (e) ([Hin26] Proposition 6.12 in five dimensions) Step 1: the augmented operator of his (6.24), with W* in place of
     omega_(0), has an injective zero-parameter operator (10.15(c)) of index 0 by (d), so it is invertible; the
     augmentation is consistent with the spaces when alpha + 2 + eta < 1, its terms being rho^3 (10.15(vi)), rho^4
     ((iii)) and compactly supported, and it vanishes faster than quadratically at the transition face, whose operator
     is box's, invertible by (b) and his Corollary 9.39; so (6.27) holds as in his Theorem 9.41's proof, and box with
     the horizon modification alone is mode stable for small |sigma| and gamma_H in (0, eps_0]. Step 2: the zero energy
     and transition face estimates hold uniformly under the small modification at infinity, so the low-energy estimate,
     and with it mode stability near sigma = 0, persists for small e and gamma. With 10.19's Propositions 6.5 and 6.9:
     box^Upsilon, with 10.15's horizon modification c_H = -(1/2) chi dr, gamma_H in (0, eps_0], and c^Upsilon = r^-1 dt
     near infinity with small e and gamma, is mode stable at every sigma with Im sigma >= 0 on five-dimensional
     Tangherlini -- his Proposition 6.12 -- on the reading of [Hin26c] section 9 stated in 10.19(d), widened, for (iii),
     to Lemma 3.11, Theorems 9.36-9.41 and Corollary 9.43 read at n = 4 with alpha + 2 for alpha + 3/2, section 9.5
     again stated for scalar operators.

*READ.* [Hin26c] (alphaXiv, 2026-10-22): pp. 61 (Lemma 3.11, Definition 3.12, (3.47)), 104 (Definition 5.10), 193-195
(Theorem 9.36 and its proof, (9.107)-(9.109); section 9.5: (9.110), Theorem 9.38, (9.111)-(9.115)), 197-198 (Corollary
9.39, Proposition 9.40 and its proof), 198-200 (Theorem 9.41 and its proof, (9.119)-(9.122), Remark 9.42, Corollary 9.43
and its proof). [Hin26] (alphaXiv, 2026-10-22): pp. 117-119 (Lemma 6.6, (6.17b), Lemma 6.8 and its proof), 121-124
(Proposition 6.12 and its proof, (6.24)-(6.28)).

*What this gives, and what it does not.* At the level of deduction [Hin26] section 6.4 holds in five dimensions: the
gauge potential operator with 10.15's modification is mode stable on the closed upper half plane. The dimension enters
through the shift n/2 = 2 in the weights, the gap (0, 2) of the unmodified operator where his is (0, 1), and the
augmentation's first term, which decays at rho^3 by the dimension where his needs a cancellation; the shifted weight
alpha + 2 is left in (0, 1), as his alpha + 3/2 is. Not done, and OPEN: the line-by-line reading of [Hin26c] section 9
at n = 4, now including sections 9.4-9.6 and Lemma 3.11; [Hin26] section 6.5 (the large zero energy states of
box^Upsilon; 10.28 deduces section 6.5.1 on Lemma 6.13, 10.29 Proposition 6.18 (1)-(3), 10.30 (4)-(7)) and Lemma 6.13 in
five dimensions (10.29 deduces it); the constraint propagation operator's counterpart, his section 7, which rests on
[Hin26a] (Theorem 5.2, section 6, Theorem B.1; 10.21 deduces section 6 from Theorem 5.2, and 10.22-10.23 Theorems 5.2
and B.1 on readings); and the linearized gauge-fixed Einstein operator, his section 8, in five dimensions. Nothing of
this section is proved: Proposition 10.17 is computed, and (a)-(e) are deduced.


### 10.21 [Hin26a] section 6 in five dimensions: the constraint propagation operator (`cpmodes5.py` K1-K3; D66)

*The setting.* [Hin26a] Theorem 6.2 -- [Hin26] Theorem 7.1 (1)-(2) -- states, for C_h omega = h^-1 (2 c (x)_s omega -
(1 - e) g iota_{c#} omega) with c of his Proposition 5.1 (r^-1 (dt - v dr) for large r), e small and h in (0, h_0): (1)
box^{C_h} has no nontrivial outgoing mode at sigma != 0, Im sigma >= 0, outgoing meaning (his Definition 6.1) omega =
e^(-i sigma t) e^(i sigma r_*) omega_1 for large r with omega_1 conormal of some weight; and (2) its zero energy
operator is invertible from H-bar_b^(s,l) to H-bar_b^(s-1,l+2) for l in [-C_0 - 3/2, -1/2) and s >= -C_0, with the
density r^2 |dr dg/|, its indicial roots having Re lam >= 1 or Re lam < -C_0, the only one with Re lam = 1 being lam =
1, simple of scalar type 0 and of scalar type 1. His proof (pp. 67-69) deduces it from his Theorem 5.2 (solvability on
weighted 3b-spaces under (5.14), alpha_sf < -1/2 and alpha_K > alpha_sf + 1/2) with alpha_K = 1 and alpha_sf = -C_0 - 2.
Part (1): by his (6.4), box^C = -2 d_t* rho (rho d_rho - 1 - S-bar^C - rho S~) + box^C(0)-hat + Q d_t* + R d_t*^2, the
outgoing part satisfies a regular-singular ODE that gains an order while below 1 + min spec S-bar^C, so omega_1 lies in
A^1, the spectrum being positive; the data then obey |omega^(0)| <= C r^-1 and |omega^(1)| <= C, so lie in
rho^(-3/2-eps) H-bar_b (r^2 |dr dg/|), and Theorem 5.2 puts omega in rho_sf^(-C_0-2) L^2, which a nonzero mode, |omega|
= e^((Im sigma) t) |omega_0|, is not over an annulus. Part (2): injectivity by the same with data (omega_0, 0), as l >=
alpha_sf + 1/2; index 0 from his Theorem B.1 and [Hin26c] Corollary 9.43, or directly from the radial ordinary
differential operators of a static metric and his Theorem 4.9(3). In five dimensions 10.12 computed the indicial roots
(the trace weight 2/(D - 2)), 10.13 the semiclassical inputs, deducing the five-dimensional (5.14), alpha_sf < 0 and
alpha_K > alpha_sf at e = 0, and 10.14 a c on Tangherlini; section 6's own steps were OPEN.

**Proposition 10.18 (computed; exact).** With C at the trace weight 2/3, on 4+1 Minkowski in t* = t - r, rho = 1/r and
the Cartesian frame:

 (i) (the structure at infinity) box^C = -2 d_t* rho (rho d_rho - 3/2 - S-bar^C) plus a stationary operator: the d_t*
     d_r coefficient is 2 Id, with no d_t* times a tangential derivative and no d_t*^2 term; and S-bar^C, read off the
     coefficients of d_t*, has spectrum h^-1 {2 (1 - v), (1 - e)(1 - v), 1 - v (three times)} -- his (4.17), [Hin26]
     (7.5), with three angular copies -- all positive for 0 < v < 1 and 0 <= e < 1 (K1).
 (ii) (the radial sets) At the incoming covector the first-order part A_w of the zero energy operator satisfies A_w +
     S-bar^C = D S-bar^C(-v) D, D the reflection of the radial direction, so spec (A_w + S-bar^C) = h^-1 {2 (1 + v),
     (1 - e)(1 + v), 1 + v (three times)} (K2).
 (iii) (the weights) Over a slab 0 <= t <= T r the weight rises by 1/2 in any dimension, the integral of rho^(-2a)
     r^(n-1) dt being T rho^(-2a-1) r^(n-1); rho^k lies in rho^a L^2(r^3 dr) near infinity iff a < k - 2, so pointwise
     bounds r^-1 and 1 put the data in rho^(-2-eps) H-bar_b (r^3 |dr dg/|); alpha_sf + 1/2 = -C_0 - 2 gives alpha_sf =
     -C_0 - 5/2; and Theorem 6.2(2)'s range, l + 2 in [-C_0, 2), is l in [-C_0 - 2, 0) for the density r^3 |dr dg/|
     (K3).

*Proof.* K1-K3 of cpmodes5.py. K1 builds box^C = 2 delta G (delta* + C) on the 1-forms of Minkowski^(n+1) in the
coordinates (t*, x) and the Cartesian frame, and reads the d_t*^2, d_t* d_x and d_t* coefficients at x = (1, 0, ..., 0);
S-bar^C is r/2 times the d_t* coefficient less (n - 1)/2 = 3/2, the shift the scalar wave operator carries. K2 reads A_w
off the coefficients of the spatial first derivatives contracted with the radial direction and checks the conjugation
exactly; the identity is structural, as 10.19's is, the reflection of dr carrying c = r^-1 (dt - v dr) to r^-1 (dt + v
dr) (deduced). K3 is exact arithmetic. Four-dimensional controls: (i) at the weight 1, his spectrum h^-1 {2 (1 - v),
(1 - e)(1 - v), 1 - v (twice)} with the shift 1 of his (6.4); (ii) the same; (iii) his rho^(-3/2-eps) (r^2), alpha_sf =
-C_0 - 2 and l in [-C_0 - 3/2, -1/2). Controls: the weight 1 in five dimensions, where the spectrum is not his; A_w with
its sign flipped (at R_out A_w does not enter); and the four-dimensional data weight -3/2 claimed in five dimensions. []

*Deduced.*

 (a) ((6.4) in five dimensions) On five-dimensional Tangherlini, with t* = t - r near infinity and c of 10.14 -- of the
     form a(r) dt + b(r) dr, equal to r^-1 (dt - v dr) for large r -- box^C = -2 d_t* rho (rho d_rho - 3/2 - S-bar^C -
     rho S~) + box^C(0)-hat + Q d_t* + R d_t*^2 with Q in rho^3 Diff_b^1, R in rho^2 C^oo and box^C(0)-hat in rho^2
     Diff_b^2: by (i), Tangherlini approaching Minkowski at O(rho^2) (10.18, U4), one power better than Kerr, and the
     errors absorbed as in his proof.
 (b) (Part (1)) Let omega = e^(-i sigma t) e^(i sigma r_*) omega_1, omega_1 in A^gamma, be an outgoing mode solution,
     r_* the five-dimensional tortoise coordinate, with r_* - r = O(r^-1), so that e^(-i sigma (t - r_* - t*)) and its
     inverse lie in A^0. By (a), 2 i sigma rho (rho d_rho - 3/2 - S-bar^C) omega_1 lies in A^(gamma+2), so omega_1 lies
     in A^(gamma+1) while gamma + 1 < 3/2 + min spec S-bar^C, and in A^1 by the positivity in (i), a fortiori. The data
     then obey |omega^(0)| <= C r^-1 and |omega^(1)| <= C and, by (iii), lie in rho^(-2-eps) H-bar_b (X, r^3 |dr dg/|),
     inside rho^(alpha_sf + 1/2) for alpha_sf = -C_0 - 5/2. Theorem 5.2 in five dimensions with alpha_sf = -C_0 - 5/2
     and alpha_K = 1, which satisfy the five-dimensional (5.14) at 10.14's e = 1/102400, alpha_sf < b* - 1 and alpha_K >
     alpha_sf + 1 - b* (10.22(c), solv5.py Q4; at e = 0 10.13's alpha_sf < 0 and alpha_K > alpha_sf), puts omega in
     rho_sf^(-C_0-5/2) L^2(Omega, |dg|); a nonzero omega_0 is not square integrable over [0, oo) times an annulus, where
     rho_sf is bounded below. So omega = 0.
 (c) (Part (2), injectivity) A kernel element omega_0 in H-bar_b^(s,l)(X, r^3 |dr dg/|) with l >= -C_0 - 2 = alpha_sf +
     1/2 gives a stationary solution with data (omega_0, 0), and Theorem 5.2 forces omega_0 = 0, as in his proof.
 (d) (Part (2), index 0 and the roots) By his direct route: Tangherlini is static and c is spherically symmetric, so the
     zero energy operator decomposes over the scalar- and vector-type harmonics of S^3 into radial ordinary differential
     operators whose indicial roots at infinity are 10.12's. By Proposition 10.9, at (v, e, h) = (1/2, 1/102400, 10^-6),
     none has real part in [-100, 2) and the only one with real part 2 is lam = 2, simple, at l = 0 and at l = 1; and
     each harmonic's roots split evenly across the strip, as his Theorem 4.9 gives in four dimensions (10.12's counts: 3
     and 3 for the scalar sextic at l >= 1, 2 and 2 for the quartic at l = 0, 1 and 1 for the vector type, lam = 2
     counted on the right). So for C_0 <= 100, on the weights of (iii), each radial operator has index 0 as in his
     proof, and the zero energy operator, Fredholm and injective by (c), is invertible. It is Fredholm by [Hin26c]
     Theorem 9.36 at n = 4, on the reading of 10.20, which stands here in place of his own citations for (6.1), [HHV21,
     Theorem 4.3], [Vas21b, section 6] and [Vas18, Theorem 6.9] (p. 68), given box^C's quantity at the conormal bundle
     of the horizon, vartheta_H+ < -C_0 - 1/2 ([Hin26c] p. 193 asks s_0 > 1/2 + vartheta_H+, and s >= -C_0), that is the
     threshold 1/2 + vartheta_H+ of 10.18's convention below -C_0, which is not computed here: by the mechanism of his
     Remark 5.7, stated there for the spacetime estimate (5.21), the damping h^-1 l, positive on future causal covectors
     (Lemma 3.5), pushes the threshold below any fixed number for small h, and in five dimensions it is OPEN. (He takes
     C_0 + 4 in Theorem 4.9 for his adjoint route, p. 69, which the direct route does not need.) Its indicial roots have
     Re lam >= 2 or Re lam < -C_0, the only one with Re lam = 2 being lam = 2, simple of scalar type 0 and of scalar
     type 1. His other route, through his Theorem B.1, has by (i)-(ii) the l-window of (B.13), -1/2 - h^-1 (1 - e)(1 +
     v) < l < -1/2 + h^-1 (1 - e)(1 - v), in five dimensions, on the reading of 10.19(d) ([Hin26c] (9.16b)-(9.16c),
     (9.32)); Theorem B.1 itself is not deduced here (10.23 deduces it on readings).
 (e) ([Hin26a] Theorem 6.2 in five dimensions, on his Theorem 5.2) So, with Theorem 5.2 applied for C_0 + 1 as in his
     proof (p. 67): for every h in (0, h_0), h_0 = h_0(e, C_0) that of Theorem 5.2 in five dimensions, depending also on
     the weights, box^C on five-dimensional Tangherlini has no outgoing mode at sigma != 0, Im sigma >= 0, and its zero
     energy operator is injective on the weights l >= -C_0 - 2; and at h = 10^-6, the one point at which the roots are
     known (Proposition 10.9), for C_0 <= 100 and given the horizon threshold of (d), it is invertible from
     H-bar_b^(s,l) to H-bar_b^(s-1,l+2) for l in [-C_0 - 2, 0) and s >= -C_0, with the density r^3 |dr dg/| -- provided
     10^-6 lies below the five-dimensional h_0(e, C_0), which is not certified (10.12, 10.14): [Hin26] Theorem 7.1
     (1)-(2) in five dimensions, conditional on [Hin26a] Theorem 5.2 there (10.22 deduces it on a reading). His Theorem
     1.1(2) follows as his does, with C_0 + 2 for C_0, so for C_0 <= 98 at that point: a stationary solution with
     |omega_mu| <= C r^(C_0) lies in r^(C_0 + 2 + eps) L^2(r^3 dr), the shift being n/2 = 2, so by the roots in r^eps
     L^2, and vanishes by the injectivity at l = -eps.

*READ.* [Hin26a] (arXiv:2606.27658v2, alphaXiv, 2026-10-22): pp. 1-3 (Theorem 1.1, (1.2)), 9-11 (section 1.2.2, Figure
1.1, Remark 1.4), 38-43 (Proposition 5.1, Theorem 5.2, (5.14)-(5.18), Lemma 5.3, footnote 15, section 5.2.1), 44 (Remark
5.7), 47 (Proposition 5.8), 51 (Proposition 5.9), 54 (Proposition 5.11), 64 (Proposition 5.17), 66-69 (the end of
section 5.2.7, Definition 6.1, Theorem 6.2 and its proof, (6.1)-(6.4), Remarks 6.3-6.4), 87 ((B.13)-(B.17), Theorem
B.1), 93 (Theorem B.4), 98 (section B.4). [Hin26] (arXiv:2606.28253v2, alphaXiv): p. 135 ((7.3)-(7.6)).

*What this gives, and what it does not.* At the level of deduction, and conditional on his Theorem 5.2, [Hin26a] section
6 holds in five dimensions: the constraint propagation operator has no outgoing mode in the punctured closed upper half
plane, and its zero energy operator is invertible on the weights l in [-C_0 - 2, 0). The dimension enters through the
volume r^3, which puts a mode's data in rho^(-2-eps), half an order below his, and so alpha_sf = -C_0 - 5/2; through the
shift (n - 1)/2 = 3/2 of (6.4), above which S-bar^C, his matrix with three angular copies, stays positive; and through
the indicial roots of 10.12, which put the top of the range at the Coulomb root 2 where his is at 1. His argument is
otherwise unchanged. Not done, and OPEN: his Theorem 5.2 in five dimensions -- the 3b-estimates of his section 5 and
their h_0 -- on which (b)-(e) rest (10.22 computes its remaining inputs and deduces it on a reading); his Theorem B.1 in
five dimensions and the tf-admissibility of box^C ([Hin26] Theorem 7.1(4)) (10.23 deduces both on the same reading);
[Hin26] section 6.5 and Lemma 6.13; and [Hin26] sections 7 and 8 in five dimensions. Nothing of this section is proved:
Proposition 10.18 is computed, and (a)-(e) are deduced, (b)-(e) on [Hin26a] Theorem 5.2, which 10.22 deduces on the
reading that his 3b-analysis holds in five dimensions.


### 10.22 [Hin26a] Theorem 5.2 in five dimensions: the inputs, and the reading (`solv5.py` Q1-Q4; D67)

*The setting.* 10.21 deduced [Hin26a] Theorem 6.2 on five-dimensional Tangherlini from his Theorem 5.2 there, which it
left OPEN. His proof of Theorem 5.2 (section 5.2, pp. 41-66) is a chain of semiclassical estimates on weighted
3b-spaces. Lemma 5.3 puts h^2 box_g in h^2 rho_sf^2 Diff_3b^2 and L in h rho_sf^2 Diff_3b^1, from (2.12)-(2.14) -- the
Christoffel symbols of a 3sc-metric lie in rho_sf C^oo -- and c in rho_sf C^oo. Propositions 5.5-5.6 give elliptic
estimates at finite nonzero frequency and damped estimates at fiber infinity from Lemmas 3.5 and 3.7; Proposition 5.6's
proof "does not rely on any fine properties of the null-geodesic flow" (p. 44) and uses "only simple causal information"
near tau = 0 and r = m (pp. 44-45). Propositions 5.8, 5.9, 5.11 and 5.12 propagate estimates along the zero section
through the three critical sets of -r c# and between them, by positive commutators whose signs are his Proposition 5.1
(3)-(6). Proposition 5.16 gives energy estimates near the initial surface X = {t = 0} and the final surface Sigma# = {r
= m} inside the black hole, from Lemma 5.14, stated for any time-oriented Lorentzian vector space, and Corollary 5.15,
stated on R^(1+n) and for n-dimensional manifolds of bounded geometry (pp. 58-60); it asks that d tau, tau = t/r, be
past timelike for g_3b = rho^2 g on tau^-1([0, T]) and that m - r be a time function near Sigma#. Section 5.2.7 combines
them, with a duality argument for existence. The weights enter only at the corner dK+ and the sink R_v of sf, through
Proposition 5.1 (4)-(5). In five dimensions 10.13 computed his section 3's quantities, deducing that Lemmas 3.3-3.8 hold
verbatim at the trace weight 2/(D - 2), and section 4's symbols, and 10.14 wrote a c on Tangherlini in Kerr-Schild time
((10.48)) with his Proposition 5.1 (1)-(6) at (v, e) = (1/2, 1/102400) and r_0 = 100, (4)-(5) at the four-dimensional
weights (1, -102) and with the thresholds b_sf < b* and b_K > b_sf - b* at that e, b* = 0.99340731.... Not computed: the
3sc structure of Tangherlini, the geometry of the energy estimates, and (4)-(5) at the weights 10.21 uses.

**Proposition 10.19 (computed; exact).** On five-dimensional Tangherlini in Kerr-Schild time, g = eta + mu r^-2 k (x) k
with k = dt + dr:

 (i) (the 3sc structure) In Cartesian coordinates g^-1 = eta^-1 - mu r^-2 k# (x) k# exactly; the Christoffel symbols are
     polynomials of degree at most 2 in mu with no constant term and satisfy Gamma(lam x; mu) = lam^-1 Gamma(x; mu
     lam^-2); and c = r^-1 (dt - v dr) has components homogeneous of degree -1 (Q1).
 (ii) (near X) r^2 g^-1(d tau, d tau) = -(1 - tau^2) - mu r^-2 (1 + tau)^2 and r g^-1(d tau, dt) = -1 - mu r^-2 (1 +
     tau) (Q2).
 (iii) (near Sigma#) g^-1(dr, dr) = f = 1 - mu r^-2, increasing with f(r_h) = 0; g^-1(dr, dt) = mu r^-2 > 0 and g^-1(dt,
     dt) = -1 - mu r^-2 < 0 for every r > 0 (Q3).
 (iv) (the weights) In cform5.py's symbol T = r^2 (-l(dw/w) + S) on sf at (v, e) = (1/2, 1/102400), at the weights of
     10.21, (alpha_K, alpha_sf) = (1, -C_0 - 5/2), that is b_K = 1 and b_sf = -C_0 - 3/2: the characteristic polynomials
     at dK+ and at R_v have positive roots for every C_0 >= 0, and at C_0 = 100, the largest C_0 10.21 uses, T is
     positive definite for every rho_K in [0, 10] (Q4).

*Proof.* Q1-Q4 of solv5.py. Q1 builds g in Cartesian coordinates with r an independent symbol and d_i = d/dx_i + (x_i/r)
d/dr, so that the scaling, a homogeneity in (x, r) jointly, is checked as an identity of rational functions over all 125
components; Q2-Q3 are exact algebra on the (t, r) block of g^-1; Q4 evaluates cform5.py C7's characteristic polynomials
(2 - d - lam)^3 q(d, lam) at d = -C_0 - 5/2 (dK+) and d = -C_0 - 3/2 (R_v), with C_0 symbolic, and runs C7's Sturm test
at C_0 = 100. Four-dimensional controls: Schwarzschild in Kerr-Schild time, 2m r^-1 for mu r^-2, with Gamma(lam x; m) =
lam^-1 Gamma(x; m/lam), in rho^2; and (ii)-(iii) the same with 2m/r. Controls: the four-dimensional profile with the
five-dimensional scaling; T = 1 in (ii), where the bound degenerates at infinity; the interval [2 r_h, 3 r_h) in (iii),
outside the horizon; and alpha_K = alpha_sf in (iv), below the threshold at dK+. []

*Deduced.*

 (a) (Lemma 5.3) By (i), Gamma lies in mu rho^3 C^oo(S^3 x [0, 4]_(mu rho^2)), mu rho^2 = 4 at r = m = r_h/2, in rho_sf
     C^oo with two powers to spare (Kerr's are in rho^2), so (2.12) holds and with it (2.14): h^2 box_g in h^2 rho_sf^2
     Diff_3b^2, and delta* and delta in rho_sf Diff_3b^1. 10.14's c, (10.49) smoothed near r_0/2 and 2 r_0 as in
     10.14(b) and his p. 41, is stationary and smooth, and r^-1 (dt - v dr) for r >= 3 r_0, so it lies in rho_sf C^oo,
     and L in h rho_sf^2 Diff_3b^1, with semiclassical principal symbol G - i l, as in his.
 (b) (Propositions 5.5-5.6) They use Lemmas 3.5 and 3.7, which hold in five dimensions (10.13(i)); Proposition 5.6's
 proof uses also "only simple causal information" near tau = 0 and r = m (pp. 44-45), which is (d).
 (c) (Propositions 5.8, 5.9, 5.11, 5.12) Their signs are his Proposition 5.1 (3)-(6): (3) and (6) by 10.14 at r_0 = 100;
     (4)-(5) at the weights of 10.21 by (iv) at the critical points; on a neighbourhood of size delta_r in r by
     continuity, as in his proof (p. 39; 10.14(a)); and (5) on |r/(t v) - 1| <= 2 delta_sf, delta_sf > 0.0034 being
     forced by cform5.py C5, not by continuity but because T' at the sink does not depend on rho_K (C7; 10.14(iv)) --
     and at C_0 = 100 on all of sf with rho_K <= 10. The five-dimensional (5.14) at this e is alpha_sf < b* - 1 and
     alpha_K > alpha_sf + 1 - b* (10.14(iv), with b_sf = alpha_sf + 1 and b_K = alpha_K), at e = 0 10.13(ii)'s alpha_sf
     < 0 and alpha_K > alpha_sf.
 (d) (Proposition 5.16) By (ii), d tau is past timelike for g_3b on tau^-1([0, T]) for every T < 1, with g_3b^-1(d tau,
     d tau) <= -(1 - T^2) uniformly up to sf -- his hypothesis for (1), where his T is sufficiently small. By (iii), on
     [r_h/2, r_h) dr is timelike and in the cone opposite to the past timelike dt, so future timelike: m - r, with m =
     r_h/2 (10.14), is a time function, Sigma# is spacelike, future timelike vectors leave Omega there, and (2) applies
     with r_3 < r_h. The hypothesis of Lemma 5.14 and Corollary 5.15 on l, positive definite on future causal covectors,
     is Lemma 3.5 (10.13(i)). The uniformity Corollary 5.15 asks -- the data g, (E, <., .>_E), nabla^E, l, phi and dt in
     a compact subset of C^oo(I x B_3) (p. 60) -- follows from (i) and c in rho_sf C^oo (deduced).
 (e) ([Hin26a] Theorem 5.2 in five dimensions) On the reading that his 3b-analysis -- the 3b-pseudodifferential calculus
     of his section 2.3 and the positive commutator and energy arguments of section 5.2 -- holds in five dimensions as
     its arguments do, not verified here line by line: at (v, e) = (1/2, 1/102400), with 10.14's c and any weights with
     alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*, there is h_0 = h_0(e, C_0) > 0, depending also on the weights
     and not made explicit, such that for h in (0, h_0) and s in [-C_0, C_0] the forward problem (5.15) and the initial
     value problem (5.16), with the density r^3 |dr dg/| for r^2 |dr dg/|, have solutions with the weights of his
     Theorem 5.2. With 10.21, [Hin26a] Theorem 6.2 holds on five-dimensional Tangherlini on the same reading: (1) and
     the injectivity of (2) for every h in (0, h_0); the invertibility of (2) at h = 10^-6, Proposition 10.9's point,
     for C_0 <= 100, provided 10^-6 < h_0 and given 10.21(d)'s horizon threshold. (Since written out as 10.75 (lxi), on
     no reading; D167.)

*READ.* [Hin26a] (arXiv:2606.27658v2, alphaXiv, 2026-10-22): pp. 9 (section 1.2.2), 12-16 (Definition 2.1, its charts,
(2.4), (2.7)-(2.10), Definitions 2.2 and 2.5, (2.11)-(2.14)), 25-27 (Lemmas 3.3, 3.5, 3.7 and 3.8, Remark 3.4, Corollary
3.6), 38 (Proposition 5.1), 19 (section 2.3.1), 41-45 (Theorem 5.2, footnote 15, Lemma 5.3, (5.18)-(5.20), Lemma 5.4,
Propositions 5.5-5.6), 47-48 and 51 (Proposition 5.8 and its proof), 51-52 and 54 (Proposition 5.9, (5.53)-(5.54), the
remark after its proof), 54 (Proposition 5.11), 56 (Proposition 5.12), 58-60 (Remark 5.13, Lemma 5.14, Corollary 5.15,
Proposition 5.16), 64 (Proposition 5.17 and its proof), 66 (the end of section 5.2.7).

*What this gives, and what it does not.* 10.21's condition is reduced from an OPEN theorem to a reading: every input
[Hin26a] section 5.2 takes from the metric and from c is computed in five dimensions, in 10.13, 10.14 and here, or
deduced from computed quantities -- (4)-(5) off the critical points and the smoothing of c (10.14(a)-(b), (c) above),
Lemmas 3.3-3.8 (10.13(i)), the uniformity of Corollary 5.15 ((d)). The estimates themselves are positive commutator and
energy arguments; of them, Lemma 5.14 and Corollary 5.15 are stated in any dimension (pp. 58-59), and the rest of
section 5.2 is written in 3+1 -- charts on S^2 (p. 60), alpha_sf < -1/2 in Proposition 5.11 (p. 54) -- and is to be read
at n = 4. The dimension enters through the trace weight 2/(D - 2) in C (10.12-10.13); through the thresholds of (5.14),
at e = 0 alpha_sf < 0 and alpha_K > alpha_sf where his are -1/2 and alpha_sf + 1/2 (10.13(ii)), at e = 1/102400 b* - 1
and alpha_sf + 1 - b*; and through Tangherlini's faster approach to Minkowski, which only helps. What remains is the
line-by-line reading of his sections 2.3 and 5.2 at n = 4, the 3b-calculus whose proofs he cites from his [Hin26d]
section 3 (p. 19) among it, and h_0, which neither his proof nor this record makes explicit. Not done, and OPEN: that
reading; 10.21(d)'s horizon threshold; his Theorem B.1 in five dimensions, and with it [Hin26] Theorem 7.1(4) (10.23
deduces both on the same reading); [Hin26] sections 6.5, 7.2 and 8 in five dimensions. Nothing of this section is
proved: Proposition 10.19 is computed, and (a)-(e) are deduced.

### 10.23 [Hin26a] Theorem B.1 in five dimensions, and [Hin26] Theorem 7.1(4) (`tface5.py` F1-F5; D69, D71, D72)

*The setting.* 10.21 left [Hin26a] Theorem B.1 OPEN in five dimensions, and with it [Hin26] Theorem 7.1(4), the
tf-admissibility of the constraint propagation operator for every weight beta in [-C_0, 1), which his proof takes from
Theorem B.1 with beta' := -beta + 3/2 - eps, "the shift by 3/2 in the weights being due to the weight rho^-3 of this
density" ([Hin26] p. 137). Theorem B.1 (pp. 85-88) concerns box^C = 2 delta G (delta* + C) on Minkowski space R_t x R^3
with c = r^-1 (dt - v dr): it is homogeneous of degree -2 under dilations ((B.10)); its spectral family at sigma in
e^(i[0, pi]) is a scattering operator near infinity and a weighted b-operator near the origin ((B.12)); and it is
invertible on H_sc,b^(s,(l, beta)) for l in (B.13)'s l-window and beta in (1/2, 3/2 + C_0], the density being r^2 |dr
dg/|. His proof has three parts. Proposition B.2 gives the Fredholm property, "also" from [Hin26b] Theorem 9.38
([Hin26c]'s here), and index 0 by a relative index argument (p. 91). Theorem B.4 (pp. 93-98) gives solvability and
uniqueness on edge-b spaces for alpha_sf < -1/2 and alpha_cf > 1/2 by the arguments of Theorem 5.2: positivity at the
cone face cf "from (4.5) (with beta_K - beta_sf replaced by alpha_cf - 1)"; -(1/2) r^2 l(dr/r), whose eigenvalues are
positive, "and is thus positive definite (with respect to the fiber inner product from Lemma 3.3)" (p. 96); energy
estimates near X, in tau = t/r with d tau past timelike for |tau| < 1, and near the final hypersurface r = 1 - t; and
his Proposition 5.11, quoted at the sink of sf, where the edge-b and 3b spaces agree. Section B.4 (p. 98) takes l =
-1/2, beta = 7/2, alpha_sf = -5/2, alpha_cf = 5/2 and, "without loss", C_0 >= 2: a kernel element omega_0 at Im sigma >=
0 gives omega = e^(-i sigma (t - r)) omega_0, whose data lie in Theorem B.4's (B.33), so that omega is Theorem B.4's
solution, in rho_sf^alpha_sf rho_cf^alpha_cf H-bar_eb^1, which the integral of t^(2 (alpha_sf + alpha_cf)) over t >= 1
forbids unless omega_0 = 0. 10.21 computed (B.13)'s l-window in five dimensions (K2) and noted that its beta-range
carries the density's shift; 10.22 computed the inputs of Theorem 5.2. Not computed before this section: the dilation
structure, the beta-range, the threshold at cf, section B.4's numbers and the index argument's in five dimensions.

**Proposition 10.20 (computed; exact).** On 4+1 Minkowski space with c = r^-1 (dt - v dr) and the trace weight 2/3:

 (i) (dilations) In t* = t - r, the coefficient of every k-th order derivative in box^C, d_t* counted, is homogeneous of
     degree k - 2 in x, on each of its 147 terms (F1).
 (ii) (the origin) r^mu lies in r^beta L^2(r^3 dr) near r = 0 iff mu > beta - 2; so if the indicial roots in rho = 1/r
     at infinity avoid [-C_0, 2), those in r at the origin, their negatives, avoid (-2, C_0], and the weights at the
     origin are beta in (0, 2 + C_0] (F2).
 (iii) (the thresholds) At (v, e) = (1/2, 1/102400): cform5.py's T = r^2 (-l(dw/w) + S) at rho_K = 0 with d = b_sf - b_K
     = 1 - alpha_cf is positive definite at alpha_cf = 5/2 and at d = 0.9934, and not at d = 0.9935, between which lies
     b*, the smaller root of q(d, 0) = 204795 d^2 - 409605 d + 204801, derived from det T (cform5.py C7's); as e -> 0,
     the limit a substitution, T's entries being polynomial in e (B is singular at e = 0), its eigenvalues are 2 - d
     (three times), 1 - d and 2 - 2 d, the threshold d < 1; and -(1/2) r^2 l(dr/r) has characteristic polynomial (lam -
     v)^3 (lam^2 - (3 - e) v lam + (2 - e) v^2 - e), with positive roots there and, at e = 0, for every v > 0 (F3).
 (iv) (section B.4) (alpha_sf, alpha_cf) = (-5/2, 5/2) satisfies alpha_sf < b* - 1 and alpha_cf > 1 - b*; the integral
     of t^(2 (alpha_sf + alpha_cf)) over [1, oo) diverges; l = -1/2 lies in the l-window for every h > 0 and 0 < v, e <
     1; beta = 7/2 lies in (ii)'s range iff C_0 >= 3/2; in (tau = t/r, r) the density |dg| = r^4 |dt (dr/r) dg/| is r
     times X's r^3 |dr dg/|, so (B.33)'s data weights are alpha_sf + 1/2 and alpha_cf - 1/2, and section B.4's data, in
     rho_sf^(l - 1) rho_cf^beta (the l - 1 of his inclusion H_sc,b^1 in rho_sc^-1 H_b^1, READ), lie in them; a kernel
     element of size rho^(3/2 + S-bar - eps) at infinity lies in rho^l L^2(r^3 dr) iff l < -1/2 + S-bar - eps; for the
     adjoint, box^C's formal adjoint in the incoming T = t + r has mixed coefficient -2 Id and no d_T^2 term, and
     S-tilde = -(r/2) (its d_T coefficient) - 3/2 has spectrum h^-1 {(1 - e)(1 + v), 2 (1 + v), 1 + v (three times)},
     whose bottom S_in = h^-1 (1 - e)(1 + v) is 10.21 K2's spec (A_w + S-bar^C); an element of size rho^(3/2 + S_in -
     eps) at R_in lies in rho^(-l-1) L^2(r^3 dr) (the dual weight -l - 1 READ, his p. 137) iff l > -1/2 - S_in + eps,
     the l-window's lower end; and beta' = -beta + 2 - eps lies in (ii)'s range for every sufficiently small eps > 0 iff
     beta in [-C_0, 2) (F4).
 (v) (Proposition B.2's index) The free 1-form wave operator 2 delta G delta* has at the origin the r-roots -3, -2 | 0,
     1 at l = 0, -l - 3, -l - 2, -l - 1 | l - 1, l, l + 1 for scalar type l >= 1, and -l - 2 | l for vector type; the
     window of beta - 2 between the two groups contains (-2, 0), and rising into it from below crosses 2, 3 and 1 roots
     (F5).

*Proof.* F1-F5 of tface5.py. F1 builds box^C in Cartesian coordinates (t*, x), with r an independent symbol and d_i =
d/dx_i + (x_i/r) d/dr - (x_i/r) d/dt*, expands it, and checks every coefficient under (x, r) -> (lam x, lam r) as an
identity of rational functions; F2 and F4 are exact algebra on the exponents, with F4's integral and the Jacobian of t =
tau r by sympy, and F4's S-tilde from box^C's formal adjoint (dt dx, the Euclidean fibre product in the Cartesian frame)
rewritten in T = t + r ([Hin26c] (9.117); the thirty-second verifier's construction); F3 builds T from semiclass5.py for
any n, equal at n = 4 to cform5.py's, derives q(d, 0) from det T, takes the limit e -> 0 by substitution (T's entries
are polynomial in e, B being singular at e = 0), counts real roots with multiplicity, and factors the characteristic
polynomial of semiclass5.py's l; F5 reads the free operator's roots off gaugepot5.py's indicial determinants at gamma =
0, each simple. Four-dimensional controls, at his trace weight 1: the program's 90 terms; his beta in (1/2, 3/2 + C_0],
the eigenvalues 1 - 2 d, 1/2 - d and 3/2 - d (twice) as e -> 0 and so his alpha_cf > 1/2 (and 0.4956 at e = 1/102400),
(lam - v)^2 for (lam - v)^3, C_0 >= 2, S-tilde's bottom h^-1 (1 - e)(1 + v) (his p. 137), beta in [-C_0, 1), and his
free roots -l - 2, -l - 1, -l | l - 1, l, l + 1 with the window (-l, l - 1) for beta - 3/2 (p. 91). Controls: c = r^-1
dt - v dr in (i), not homogeneous; his beta-range claimed in five dimensions in (ii); alpha_cf = 0 in (iii), where T is
not positive definite; the characteristic polynomial with n - 2 copies of v in (iii); alpha_cf = -alpha_sf - 1 in (iv),
where the closing integral converges, his top 1 claimed there, which the endpoints refuse, and the bottom h^-1 (1 -
e)(1 - v) claimed for S_in; and his window claimed in (v). []

*Deduced.*

 (a) ((B.10), (B.12)) By (i), box^C on 4+1 Minkowski is dilation invariant of degree -2, so every term of r^2
     box^C(sigma) that carries sigma carries a positive power of r, and at r = 0 it is r^2 box^C(0), a weighted
     b-operator; at infinity it is the scattering operator whose structure 10.21 computed (K1-K2: S-bar^C, the radial
     sets, the l-window). By dilation invariance the indicial roots of box^C(0) at the origin, in r, are the negatives
     of those at infinity, in rho = 1/r -- which are Proposition 10.9's, stated on 4+1 Minkowski: they avoid [-C_0, 2)
     at its point for C_0 <= 100.
 (b) (Proposition B.2) box^C(sigma) is Fredholm on (B.13)'s spaces with the l-window of 10.21 and, by (a) and (ii),
     beta in (0, 2 + C_0], C_0 <= 100, at that point -- by his microlocal argument, or by [Hin26c] Theorem 9.38 at n =
     4 on the reading of 10.19-10.20, whose part (3) gives that the index depends neither on theta in [0, pi] nor on the
     weight, so that with his Corollary 9.39 the index 0 would follow from tf-admissibility at theta = 0, which is what
     is being proved -- and of index 0 by his relative index argument (p. 91) with (v), l taken a variable order > -1/2
     at R_in and < -1/2 at R_out (p. 91; F4's dimension-free -1/2), which keeps the operator Fredholm as h^-1 -> 0,
     where (B.13)'s window empties: lowering beta below every root at the origin raises the index by the number of the
     damped operator's roots with real part >= 2 at that point, 2, 3 and 1 by 10.12; deforming h^-1 to 0 with beta held
     below the roots keeps it; and rising into the free operator's window, where it is invertible ([Hin26c] Proposition
     9.40 at n = 4, 10.20), lowers it by as many, (v).
 (c) (Theorem B.4) By (iii) and cform5.py C7 (positive definite iff d < b*), the positivity at cf holds for alpha_cf >
     1 - b*, and -(1/2) r^2 l(dr/r) has positive eigenvalues, so that it is positive definite with respect to the fiber
     inner product of his Lemma 3.3, which holds in five dimensions (10.13(i)), as he concludes. Near X, d tau is past
     timelike for |tau| < 1 by Proposition 10.19(ii) at mu = 0, and the energy estimates near X and near r = 1 - t are
     Minkowski geometry, for which his Lemma 5.14 and Corollary 5.15 are stated in any dimension (10.22(d)). At the sink
     his Proposition 5.11 is quoted, which 10.22(c) has with alpha_sf < b* - 1. So, on the reading of 10.22(e) in its
     edge-b version, Theorem B.4 holds on 4+1 Minkowski at (v, e) = (1/2, 1/102400) for alpha_sf < b* - 1 and alpha_cf >
     1 - b*, for h below an h_0 not made explicit, with (B.33)'s data weights by (iv).
 (d) (Theorem B.1) Section B.4 runs as his with (iv): for a kernel element omega_0 at Im sigma >= 0, omega = e^(-i sigma
     (t - r)) omega_0 has data in (B.33), so by the uniqueness of Theorem B.4(2) it lies in rho_sf^(-5/2) rho_cf^(5/2)
     H-bar_eb^1, and the divergent integral of (iv) gives omega_0 = 0; with (b), box^C(sigma) is invertible. So [Hin26a]
     Theorem B.1 holds on 4+1 Minkowski on the readings of (b)-(c): for l in the l-window and beta in (0, 2 + C_0], with
     the density r^3 |dr dg/|, at (v, e) = (1/2, 1/102400), for C_0 <= 100 (his "without loss" C_0 >= 2 becoming C_0 >=
     3/2), and at h = 10^-6 provided that lies below the h_0 of Theorems 5.2 and B.4 -- the one point at which (a)'s
     roots are known.
 (e) ([Hin26] Theorem 7.1(4)) His proof applies Theorem B.1 at beta' = -beta + 3/2 - eps, the 3/2 from the density's
     weight rho^-3; in five dimensions that weight is rho^-4 ([Hin26c] p. 196: mu_e = r^^(n-1) |dr^ dg/| = rho^^-n
     mu_b) and the shift n/2 = 2 of (ii), and by (iv) beta' lies in (0, 2 + C_0] for every sufficiently small eps > 0
     iff beta in [-C_0, 2): the kernel half of tf-admissibility. The adjoint half ([Hin26c] Definition 5.10, p. 104,
     stated for every n in his Corollary 9.39, p. 197, "with -1 + beta in (5.16) replaced by -n + 2 + beta"; his p.
     137): an element of the kernel of N_tf(box^C, 1)^* on e^(-2i/rho) A^(alpha, -2+beta) is improved first at ztf, by
     the normal-operator argument of the proof of [Hin26c] Theorem 9.38 (p. 196), then at R_in to the decay 3/2 + S_in -
     eps, S_in = h^-1 (1 - e)(1 + v) the bottom of S-tilde's spectrum ((iv); his p. 137), and so lies in the dual of
     Theorem B.1's spaces with -l - 1 < -1/2 + S_in, the l-window's lower end by (iv) -- the condition of [Hin26c]'s
     parenthetical to (9.115) (p. 195), "when r|R_in,1 + alpha_+ > (n - 2)/2 - alpha", at alpha = (n - 1)/2 + S_in -
     eps, for every n; Theorem B.1 makes it 0. At ztf, comparing the improved weight with the dual weight -beta' + 2 =
     beta + eps asks beta < 2 again (the thirty-second verifier; not computed here). So, on the same readings and at the
     same point, the constraint propagation operator on five-dimensional Tangherlini is tf-admissible for every weight
     beta in [-C_0, 2), his [-C_0, 1), for C_0 <= 100.

*READ.* [Hin26a] (arXiv:2606.27658v2, alphaXiv, 2026-10-22): pp. 85-91 (Appendix B: (B.1)-(B.17), Theorem B.1,
Proposition B.2 and its proof -- the beta-range from Theorem 4.9 on p. 89, the radial thresholds, the index 0 on p. 91),
93-94 (Theorem B.4 with (B.31)-(B.33), the energy estimate (B.34)-(B.37)), 96-98 (the positivity at cf, (B.38)-(B.41),
the eigenvalues of -(1/2) r^2 l(dr/r) and Lemma 3.3's inner product, the remark on Proposition 5.11, section B.4:
(B.42)-(B.45) and the closing integral). [Hin26] (arXiv:2606.28253v2): pp. 136-137 (Theorem 7.1 and the proof of its
part (4), both halves). [Hin26c] Definition 5.10 (p. 104), Theorem 9.38(3), (5) (p. 195) and its proof (p. 196),
Corollary 9.39 and Proposition 9.40 (p. 197), as the thirty-first and thirty-second verifiers read at source.

*What this gives, and what it does not.* The transition face problem reduces to the readings 10.19-10.22 already name:
every number Appendix B takes in four dimensions -- the degree of homogeneity, the beta-range at the origin, the
thresholds at cf and at the sink, the matrix -(1/2) r^2 l(dr/r), the data weights of (B.33), section B.4's weights and
closing integral, and Proposition B.2's free roots, windows and counts -- is computed in five dimensions, or typed from
10.12 and 10.21 where those compute it (the roots at Proposition 10.9's point and their counts, the spectrum at R_in).
The dimension moves the beta-range by 1/2 at both ends, (0, 2 + C_0] for his (1/2, 3/2 + C_0], the thresholds at e =
1/102400 to 1 - b* and b* - 1 for his 1/2 and -1/2 (to 0 and 0 as e -> 0, 10.13(ii)), and the top of the tf weights from
1 to 2, the Coulomb root n - 2; section B.4's choice works unchanged. Not done, and OPEN: the line-by-line readings
([Hin26a] sections 2.3 and 5.2 and Appendix B's edge-b version, [Hin26c] section 9, at n = 4); h_0; box^C's horizon
threshold (10.21(d)); [Hin26] sections 6.5, 7.2 and 8 in five dimensions (section 8's Lemmas 8.4-8.5 and Proposition
8.6 in 10.24). Nothing of this section is proved: Proposition 10.20 is computed, and (a)-(e) are deduced.

### 10.24 [Hin26] Lemma 8.4 in five dimensions: the gauge-fixed Einstein operator's indicial roots (`lin5.py` E1-E5; D72)

*The setting.* [Hin26] section 8 studies the linearized gauge-fixed Einstein operator L = D Ric + delta*_{E^C}
delta_{E^Ups} G ((8.1)), whose Minkowski model has 2 L = box + 2 E^C delta G + 2 delta*_{E^C} E^Ups G ((8.5), the
curvature term vanishing there). His Lemma 8.4 (p. 149) lists the indicial roots of its zero energy operator by harmonic
type, in terms of box^Ups's (his Lemma 6.6) and box^C's ((7.8)): "All indicial roots ... are simple"; "there is a
positive number eps_ind > 0 such that no indicial root has real part in the interval (0, eps_ind). Moreover, the number
of roots of a fixed type with real parts <= 0, resp. >= eps_ind are equal"; and those from box^C with real part <= 0 lie
below -100. His proof (pp. 149-151) explains the shifts -- a root lam of box^Ups gives lam + 1 through delta*, unless
the indicial solution is a Killing 1-form, "and thus only for lam = -1, 0", and a root lam of box^C gives lam - 1
through the adjoint -- and computes each type's determinant, as "- det N_vl(L(0), lam) = (lam + l)(lam - l - 1) x
N_vl(box^Ups(0), lam - 1) x N_vl(box^C(0), lam + 1)" at vl (p. 151). Lemma 8.5 puts the kernel of N(L(0), 0) inside that
of the gauge operator's; Proposition 8.6 (pp. 151-153) makes L tf-admissible with weight beta in (0, eps_ind) for small
gam_Ups, the kernel half by the linearized second Bianchi identity, Lemma 8.5, his Theorem 7.1(4) and [Hin26c]
Proposition 9.40 for box on symmetric 2-tensors, the cokernel half by an index argument that counts the roots crossed.
10.12 and 10.15 computed box^C's and box^Ups's roots in five dimensions, and 10.23 deduced Theorem 7.1(4); 10.12 left
whether the five-dimensional operator's gap also begins at 0 "not computed here". Not computed before this section: L's
own roots in five dimensions, and its tensor harmonic type, which four dimensions lacks.

**Proposition 10.21 (computed; exact, and numerical where said).** On 4+1 Minkowski, with E^Ups h = -gam_U (2
iota_{c_U#} h - (2/3)(1 - e_U) c_U tr h), c_U = r^-1 dt, and E^C w = gam_C (2 c (x)_s w - (2/3)(1 - e_C) g <c, w>), c =
r^-1 (dt - v dr), let N(lam) be the indicial family of r^2 L(0) on static tensors r^-lam u, u of degree 0 and of one
harmonic type of degree l on S^3 -- scalar (S = z^l), vector (z^(l-1) beta) or tensor (z^(l-2) beta (x) beta), beta = z
dw - w dz on C^2 = R^4 -- of size 4 at s0, 6 at s1, 7 at sl (l >= 2), 2 at v1, 3 at vl (l >= 2) and 1 at tl (l >= 2):

 (i) (the types; (8.5)) At two points of R^4, |x| = 5 and 3, the images under r^2 L of the basis tensors of types s0,
     s2, v1, v2 and t2 lie in their span, with the same N(lam) at both, and (8.5) holds at both on each (E1).
 (ii) (the factorization) Every parameter symbolic, det N_L(lam) = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det
     N_C(lam + 1) / D(lam), c a nonzero number, with D = (lam - 1)^2 at s0 and s1, lam (lam - 2) at v1 and 1 at sl and vl
     (l >= 2 symbolic); at tl, det N_L = c (lam + l)(lam - l - 2) (E2).
 (iii) (cross-checks; the free operator) det N_Ups and det N_C are gaugepot5.py G1's and damping5.py's, up to constants
     and, for det N_C, the power of h = 1/gam_C by which damping5.py normalizes; at gam_U = gam_C = 0, where 2 L = box,
     every type has integer roots, none in (0, 2), as many <= 0 as >= 2 (l = 0, 1 and l = 2, 3, 7) (E4).
 (iv) (the point) At (v, e_C, gam_C) = (1/2, 1/102400, 10^6) and (e_U, gam_U) = (1/100, 1/100), for every type and l <=
     12, the roots (those of the factors of (ii), by mpmath at 50 digits) are simple; none has real part in (0, 1]; s0
     has 4 | 4 with real part <= 0 | > 1, s1 6 | 6, sl 7 | 7, v1 2 | 2, vl 3 | 3 and tl 1 | 1; box^C's with real part <=
     0 lie below -101; the least positive real part is 1.000003 (box^C's root nearest 2, less 1, at l = 2), the greatest
     negative -3.3333 x 10^-7 (box^Ups's at s1, -z/12 to first order in z = 4 e_U gam_U^2 = 4 x 10^-6), and the least
     distance from Z of the real part of a non-integer root with |lam| <= 50 is 7.3846 x 10^-8; 0 is a root of s0 and s2
     only, where the kernel of N(L, 0) is one-dimensional and N(r delta_{E^Ups} G, 0) vanishes on it (exact; his
     N(rho^-1 delta_{E^Ups}(0) G, 0), rho = 1/r) (E5).

*Proof.* E1-E5 of lin5.py. The operators are built from their definitions in Cartesian coordinates, r an independent
symbol, on fields r^-(lam + deg) times expressions of degree deg, with z^p a symbol of derivative p z^p dz/z so that l
is symbolic; N(lam) is read off at a point by least squares, with the closure residual exactly 0, and the determinants
are taken over Q[lam, gam_U, e_U, gam_C, e_C, v]. Four-dimensional control (E3): at n = 3 and the trace weight 1 the
same computation gives his (1)-(5), s0 with no factor, s1 and v1 (lam + 1)(lam - 2)/(lam (lam - 1)), sl and vl (lam +
l)(lam - l - 1). Controls: in (i) a scalar basis with its Hessian tensor replaced by the tensor type's, which is not
closed; in (ii) the four-dimensional factor (lam + l)(lam - l - 1) claimed; in (iii) the gap (0, 3) claimed; in (iv) D
kept at s0, where the root 1 enters (0, 1]. []

*Deduced.*

 (a) (his Lemma 8.4 in five dimensions, every l) By (ii) the roots of each type are box^Ups's plus 1, box^C's minus 1,
     and -l and l + 2, less D's. By Proposition 10.12(i), for z = 4 e_U gam_U^2 > 0 every root of box^Ups is at most 0
     or above 2, and none lies in (-1, 0) -- at s0 (1 - (9 + 4z)^(1/2))/2 < -1, the negative roots of Q solve lam (lam -
     1) = s with s > l (l + 1) >= 2, so lam < -1, and the others are 1 - l and -l -- so plus 1 at most 1 or above 3; the
     only ones in (0, 1] are the 1 that its root 0 gives at s0 and at s1 (the Killing dt and dx; 1 - l at l = 1), and D
     removes them, as it removes the 0 that its root -1 gives at v1 (the rotations) -- his "only for lam = -1, 0". By
     Proposition 10.9, at the point and for every l, every root of box^C has real part below -100 or above 2, but the
     Coulomb root 2 at l = 0 and 1, which D removes; so minus 1 below -101 or above 1. And -l <= 0 < 2 <= l + 2. So for
     every l no root has real part in (0, 1], and since the roots accumulate only at infinity (Proposition 10.9's, and
     box^Ups's explicitly), the least positive real part is attained and exceeds 1 (1.000003 at l <= 12 at the point),
     and the gap is (0, eps_ind) for any eps_ind up to it. Counting each factor's roots on either side -- box^C 2 | 2 at
     l = 0, 3 | 3 scalar and 1 | 1 vector for l >= 1 (Proposition 10.9's certificates); box^Ups 2 | 2 at s0, 3 | 3 at sl
     and 1 | 1 at vl (10.12(i)); the physical 1 | 1 -- with D removing one root on each side (box^Ups's at 0 or -1 on
     the left, box^C's 2 or 3 on the right), every type splits evenly for every l: s0 4 | 4, s1 6 | 6, sl 7 | 7, v1 2 |
     2, vl 3 | 3, tl 1 | 1, as (iv) computes at l <= 12. And 0 is a root only of s0 (the physical -l) and s2 (box^Ups's
     1 - l), each simple. Simplicity in general is computed here only for l <= 12 (every l, and (8.13): 10.52), the
     closest pair at the point being at s1, the physical 3 and box^Ups's 3 + z/12 + O(z^2), 3.3 x 10^-7 apart; his
     (8.13), which asks d(Re lam, Z) >= eps_ind for the non-integer roots with |lam| <= 50, holds for l <= 12 by (iv)
     once eps_ind is at most 7.3846 x 10^-8 -- box^Ups's shifted roots lie within O(z/l) of integers, the nearest
     computed at l = 12, so that over |lam| <= 50, which reaches l near 50, the bound is smaller still and not computed
     -- and he uses it "only really ... for |lam| <= 4".
 (b) (Lemma 8.5) At the point, by (iv). For every z > 0 at Proposition 10.9's point -- 0 is a simple root at s0 only if
     box^C has no root at 1, which Proposition 10.9 gives there -- his proof carries over: by (a) the kernel at s0 is
     one-dimensional, spanned by delta* of t dt plus the correction -N(box^Ups(0), -1)^-1 [box^Ups, t] dt, which is well
     defined since -1 is not an s0 root of box^Ups for z > 0 (10.12(i): 0, 3 and (1 +- (9 + 4z)^(1/2))/2), and at s2 by
     delta* of the kernel of N_s2(box^Ups(0), -1), -1 = 1 - l being box^Ups's root there; both are annihilated by the
     gauge operator, since box^Ups annihilates the 1-forms.
 (c) (Proposition 8.6, the kernel half) For beta in (0, eps_ind) and N_tf(L, sigma^) u_0 = 0: the indicial roots at r^ =
     0 are the negatives of (a)'s, so the first above -beta is the s0 and s2 root 0, and u_0 is its indicial solutions
     plus an element of A^(alpha, delta) for delta in (0, 1) with every negative real part below -delta -- delta exists:
     by (a) and 10.12(i), for l >= 2 every negative real part is at most -1, so the greatest is at l <= 1, -3.3333 x
     10^-7 at the point (iv). The linearized second Bianchi identity holds in any dimension, so the gauge 1-form eta_0
     solves N_tf(box^C(0), sigma^) eta_0 = 0; its r^^-1 leading term vanishes by (b), so eta_0 lies in A^(alpha, delta -
     1), and since 1 - delta lies in [-C_0, 2), Theorem 7.1(4) in five dimensions (10.23(e)) gives eta_0 = 0. Then u_0
     solves the operator with the unmodified symmetric gradient; at gam_Ups = 0 that is box/2, which acts componentwise
     on symmetric 2-tensors in the Cartesian frame, so by 10.20(b) ([Hin26c] Proposition 9.40 at n = 4) it is
     tf-admissible with every weight in (0, 2), and by the uniformity of [Hin26c] (9.111) for small gam_Ups, u_0 = 0 --
     once u_0 lies in the domain of [Hin26c] (9.112), which his proof obtains by improving the decay at sctf with (8.7)
     and the threshold at the outgoing radial set ([Hin26c] Theorem 9.38(5)). In five dimensions that improvement needs
     the spectrum of S-bar_{E^Ups, E^C} of his Lemma 8.2 -- by [Hin26c] Theorem 9.38(5) it is to (n - 1)/2 + S-bar - eps
     = 3/2 + min spec S-bar - eps, his 1 - eps with (8.7) -- not computed here; 10.25 computes it: min spec S-bar = 0.
 (d) (Proposition 8.6, the cokernel half) His index argument (p. 153), with the density r^^3 |dr^ dg/| and -q + 2 in (0,
     eps_ind) for his -q + 3/2 (the shift n/2 = 2 of 10.23(ii)): on each type, raising q past every root crosses the
     roots with real part <= 0, 4, 6, 7, 2, 3 or 1 by (a), lowering the index by as many; deforming gam_Ups and gam_C to
     0 with q held above every root keeps it; at gam = 0, N_tf(L, 1) = N_tf(box/2, 1), and lowering q into -q + 2 in (0,
     2) crosses the free operator's roots with real part <= 0, as many by (iii) -- for every l, box acting componentwise
     with the roots -k and k + 2 on harmonics of degree k -- raising it by as many; there box/2 is invertible
     (10.20(b)). S-bar also enters the Fredholm setting of (8.17), [Hin26c] Theorem 9.38(2) asking r + alpha_+ < -1/2 +
     S-bar at R_out (p. 195), but only through the existence of admissible orders along the deformation, which any
     continuous S-bar allows (the thirty-third verifier), so (d) rests on the readings alone. So the index of (8.17) is
     0 and, with (c), its cokernel is trivial. He writes that 3 roots are crossed at scalar type l >= 2; his own list
     has 7 on each side there, 3 being the 1-form count of the example after his Definition 2.30 (p. 67: -l - 1, -l,
     -l + 1 | l, l + 1, l + 2); the argument uses only that the two counts agree. So, on the readings of 10.19-10.23 and
     with (c)'s threshold from 10.25, L is tf-admissible on 4+1 Minkowski with every weight beta in (0, eps_ind), for
     gam_Ups small, at the point.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23): pp. 28 (section 1.4.3's three kinds of indicial roots, "With
no modifications E^Ups and E^C, it would be (0, 1) just as for the scalar wave operator", footnote 28), 144-146 (section
8: (8.1)-(8.5), Lemma 8.2), 149-151 (Lemma 8.4, (8.13), its proof, Lemma 8.5 and its proof), 151-153 (section 8.3,
(8.15)-(8.17), Proposition 8.6 and its proof, both halves, Corollary 8.7), 117 (Lemma 6.6), 135-137 ((7.3)-(7.8),
Theorem 7.1).

*What this gives, and what it does not.* His Lemma 8.4 in five dimensions, for every l at Proposition 10.9's point, from
a computed factorization and the roots of 10.12 and 10.15: the physical roots are -l and l + 2, the Coulomb exponent n -
2 = 2 in place of his 1, and the mass the s0 root 2; the gap begins at 0, which 10.12 left open, and reaches past 1 --
in four dimensions 1 is an s0 root and his gap is (0, eps_ind) with eps_ind < 1; each type splits evenly, the tensor
type included; and box^C's nonpositive roots lie below -101. Lemma 8.5 is computed at the point and deduced for every
z > 0 there, and Proposition 8.6 is deduced on readings, at that point for small gam_Ups, but for one input, the
spectrum of S-bar_{E^Ups, E^C} (his Lemma 8.2 and (8.7)), which 10.25 computes. Not done, and OPEN: simplicity and
(8.13) beyond l <= 12; how small gam_Ups must be, and h_0; section 8.4 (mode stability, Proposition 8.8, which uses
[AHW24] on Kerr; 10.27 deduces it), section 8.5, and sections 9-10, in five dimensions (10.26 takes his Proposition 8.3,
strong trapping admissibility of L). Nothing of this section is proved: Proposition 10.21 is computed, and (a)-(d) are
deduced.

### 10.25 [Hin26] Lemma 8.2's S-bar and (8.7) in five dimensions (`sbar5.py` S1-S3; D74, D76)

*The setting.* 10.24(c) carried the kernel half of [Hin26] Proposition 8.6 to five dimensions but for one step: "One
first improves the sctf = scf cap tf-decay rate alpha to 1 - eps for every eps > 0 using (8.7), and then notes that
A^(1-eps,-beta)(tf) is contained in the domain of [Hin26c, (9.112)] in view of the threshold condition r + alpha_+ <
-1/2 at the outgoing radial set" (p. 152). (8.7) closes his Lemma 8.2 (p. 146): in 2 L-bar = -2 d_t* rho (rho d_rho -
1 - S-bar_{E^Ups, E^C}) + L-bar(0) ((8.3b)), S-bar "is equal to 1/2 rho^-1 times the sum of d_t*-coefficients of the
second and third terms" of 2 L-bar = box + 2 E^C delta G + 2 (delta* + E^C) E^Ups G; it is "lower triangular" in his
splitting (5.27), with diagonal 2 (1 - v) gam_C, (1 - v) gam_C, (1 - e_C)(1 - v) gam_C, (1 - e_Ups) gam_Ups, gam_Ups, 0,
2 gam_Ups ((8.8)), "and min spec S-bar = 0. (8.7)". Corollary 8.7 (p. 153) asks beta_sctf < 1 + min Re S-bar = 1
((8.18a)). 10.18 and 10.21 computed the S-bar of box^Ups and of box^C in five dimensions (thresh5.py U2, cpmodes5.py
K1); not computed before this section: L's.

**Proposition 10.22 (computed; exact).** On 4+1 Minkowski with t* = t - r, and E^Ups and E^C as in Proposition 10.21:

 (i) (the structure) The wave operator on symmetric 2-tensors, componentwise in the Cartesian frame, has no d_t*^2 term,
     the mixed term 2 d_t* d_r and the d_t* term 3/r: it is -2 d_t* rho (rho d_rho - 3/2) plus a stationary operator.
     And 2 L-bar - box is first order, with d_t* coefficient 2 rho S-bar, S-bar a constant 15 x 15 matrix: free of r at
     (r, 0, 0, 0), with the same characteristic polynomial at (1, 2, 2, 4) (S1).
 (ii) (the spectrum) spec S-bar = {0 (five times), gam_Ups (three times), 2 gam_Ups, (1 - e_Ups) gam_Ups, (1 - v) gam_C
     (three times), 2 (1 - v) gam_C, (1 - e_C)(1 - v) gam_C}: the union of the spectra of the S-bar of box^Ups and of
     box^C -- computed here by the same construction from 2 E^Ups G delta* and 2 delta G E^C, and equal to thresh5.py
     U2's and cpmodes5.py K1's -- with five zeros; every eigenvalue is >= 0 for 0 < v, e_Ups, e_C < 1 and gam_Ups,
     gam_C > 0. At the trace weight 1 the two eigenvalues (1 - e) gam become (3/2)(1 - e) gam and the rest stay; at
     gam_C = 0, the unmodified symmetric gradient, the spectrum is {0 (ten times), gam_Ups (three times), 2 gam_Ups,
     (1 - e_Ups) gam_Ups}, the minimum 0 again (S2).
 (iii) (the consequences) u = rho^(3/2 + s) solves (rho d_rho - 3/2 - s) u = 0; rho^(3/2 - eps) lies in rho^l L^2(r^3
     dr) near infinity iff l < -1/2 - eps; and rho^(3/2 + s) lies in rho^beta L^2(drho/rho) iff beta < 3/2 + s (S3).

*Proof.* S1-S3 of sbar5.py. Fields h(t*, x) on 4+1 Minkowski with r = |x|, d_t = d_t* and d_i = d/dx_i - (x_i/r) d_t*;
the operators are lin5.py's, with time dependence; the coefficients of d_t* h are read off at a point after expansion,
the spectra by sympy, and the signs by substituting v = 1/(1 + p), e = 1/(1 + q). Four-dimensional control: rho d_rho -
1, and his (8.8)'s seven values with multiplicities 1, 2, 1, 1, 2, 2, 1 in his order -- the ranks of the summands of his
splitting (5.27) -- summing to 10, min spec 0 -- his (8.7) -- and his 1 - eps and 1. Controls: c_Ups = dt in place of
r^-1 dt in (i), where S-bar carries r; the incoming t* = t + r in (ii), where the constraint part becomes gam_C {2 (1 +
v), (1 - e_C)(1 + v), 1 + v}, 10.21 K2's spectrum at R_in, and the union fails; and his 1 - eps claimed in (iii). []

*Deduced.*

 (a) ((8.7), (8.4), (8.18a) in five dimensions) min spec S-bar = 0, attained five times (twice in four dimensions), for
     every admissible parameter -- at the point of 10.24 in particular -- and at either trace weight. On
     five-dimensional Tangherlini S_{E^Ups, E^C} - S-bar lies in rho C^oo, his (8.4), as 10.18 deduces his (6.7) for
     box^Ups: the metric differs from Minkowski's by O(mu rho^2), and c and c_Ups equal Minkowski's for large r (10.14,
     10.15). So Corollary 8.7's condition reads beta_sctf < 3/2 + min Re S-bar = 3/2, his 1, by (iii).
 (b) (Proposition 8.6, the last step of the kernel half) In 10.24(c) the kernel element u_0 improves at sctf, by
     [Hin26c] Theorem 9.38(5) at n = 4 and (a), to 3/2 - eps for every eps > 0, his 1 - eps; that theorem's
     parenthetical (p. 195, as the thirty-fourth verifier read it) places the intersection over eps > 0 of A^((n -
     1)/2 + S-bar - eps, -beta_- - eps) in the domain of [Hin26c] (9.112) under its part (2)'s outgoing threshold r +
     alpha_+ < -1/2 + S-bar, here -1/2 since min spec S-bar = 0 -- dimension-free as in 10.23(iv) -- and that is what
     his proof cites; (iii) cross-checks it, rho^(3/2 - eps) lying in rho^l L^2(r^3 dr) iff l < -1/2 - eps. The operator
     of that step, with the unmodified symmetric gradient, is (ii)'s at gam_C = 0, whose minimum is 0 as well. So the
     step 10.24(c) left OPEN holds on the same reading, and with 10.24(d) his Proposition 8.6 holds on 4+1 Minkowski, at
     Proposition 10.9's point and for gam_Ups small, on the readings of 10.19-10.24: L is tf-admissible with every
     weight beta in (0, eps_ind).

*READ.* [Hin26] (arXiv:2606.28253v2): pp. 144-146 (section 8's opening on p. 144, which fixes c_Ups = r^-1 dt and
gam_Ups << 1, (8.1), Lemma 8.1 with (8.2)-(8.5), Lemma 8.2 with (8.6)-(8.8) and its proof), 152 (the parenthetical in
the proof of Proposition 8.6), 153 (Corollary 8.7, (8.18a)); alphaXiv, 2026-10-23. [Hin26c] Theorem 9.38(5) (p. 195), as
10.23 reads it.

*What this gives, and what it does not.* The one input 10.24 left OPEN for Proposition 8.6 is computed: the S-bar of the
linearized gauge-fixed Einstein operator in five dimensions carries the gauge potential operator's spectrum, the
constraint propagation operator's and five zeros, and min spec S-bar = 0, so the decay at sctf improves to 3/2 - eps,
(n - 1)/2 where his is 1, and the threshold keeps its dimension-free -1/2. Proposition 8.6 is now deduced on readings
alone, at Proposition 10.9's point for small gam_Ups. Not done, and OPEN: those readings ([Hin26c] section 9 at n = 4,
line by line); how small gam_Ups must be, and h_0; simplicity and (8.13) beyond l <= 12; section 8.4 (mode stability,
Proposition 8.8, which uses [AHW24] on Kerr; 10.27 deduces it), section 8.5, and sections 9-10, in five dimensions
(10.26 takes his Proposition 8.3, strong trapping admissibility of L). Nothing of this section is proved: Proposition
10.22 is computed, and (a)-(b) are deduced.

### 10.26 [Hin26] Proposition 8.3 in five dimensions: strong trapping admissibility of L (`strap5.py` P1-P3; D75, D77)

*The setting.* [Hin26] Proposition 8.3 (p. 147) makes 2 L_b strongly trapping admissible ([Hin26c] Definition 5.8): "for
all eps > 0 there exists a time-translation-invariant positive definite fiber inner product on pi^*(S^2 T^*),
homogeneous of degree 0 with respect to fiber-dilations ..., such that sigma^-1 (1/2i)(S_sub(2 L_b) - S_sub(2 L_b)^*) <
eps at Gamma_0" ((8.9)). His proof (pp. 147-149): E^Ups is supported away from the trapped set, so "only the constraint
damping modifications enter", i S_sub(2 L_b) = i S_sub(box) + 2 E^C sigma_1(i delta) G ((8.10)); in the frame of (6.16b)
and the splitting (8.11) this is H_G + sigma A with a printed 10 x 10 matrix A, gam = C^(1/2) gam_C/sigma; "A is upper
triangular in the basis" (8.12) with eigenvalues "0 (6x), -2 (1 - e_C) gam c_2 (1x), -2 gam c_2 (2x), -4 gam c_2 (1x)";
c_2 = -g^-1(c_C, e_0) < 0 since c_C is past timelike and e_0 future null; and the inner product diag(1, eta^-1, ...,
eta^-9) in (8.12) gives the bound. He needs it "for fixed modification parameters" (footnote 77: for the b-regularity of
solutions with a fixed loss). 10.17 computed the frame on five-dimensional Tangherlini and carried his Lemma 6.4; not
computed before this section: the symmetric 2-tensor operator, whose angular part in five dimensions is a plane V, on
which nabla_{H_G} rotates.

**Proposition 10.23 (computed; exact).** On an abstract covector frame e_0, ..., e_n with g^-1 Gram [[0, 0, -1], [0, 1,
0], [-1, 0, 0]] (+) Id_(n-2), the 1-form part of nabla_{H_G}/sigma s N (N e_1 = e_0, N e_2 = e_1), E^C with the trace
weight m, c = c_mu e_mu, and A defined by i S_sub(2 L) = H_G + sigma A through (8.10):

 (i) (the four-dimensional control) At n = 3, his sign s = +2 and m = 1, A in the splitting (8.11) equals his printed
     matrix in all 100 entries, and it is upper triangular in his basis (8.12) with his diagonal, in his order; and at
     10.17's sign s = -2, A equals his printed matrix after the change of frame e_1 -> -e_1, c_1 -> -c_1 (P1).
 (ii) (five dimensions, c general) At n = 4, s = -2 (10.17's) and m = 2/3, det(lam - A) = lam^10 (lam + 2 gam c_2)^3
     (lam + 4 gam c_2)(lam + 2 (1 - e_C) gam c_2) -- at m = 1 the last factor is lam + 3 (1 - e_C) gam c_2 -- and A is
     upper triangular, for every c, gam and e_C, in the constant basis e_0^2, e_0 e_1, e_0 e_2, e_0 e_3, e_0 e_4, e_1
     e_3, e_1 e_4, e_3 e_4, e_1^2 - e_3^2, e_1^2 - e_4^2, e_1^2, e_1 e_2, e_2 e_3, e_2 e_4, e_2^2 (P2).
 (iii) (five dimensions, c with no angular part) At c_3 = c_4 = 0, A commutes with the rotation R of the plane of e_3,
     e_4, extended to S^2; in the units e_0^2, e_0 e_1, e_0 e_2, e_1^2 - T/2, e_1^2, e_1 e_2, e_2^2, (e_0 e_3, e_0 e_4),
     (e_1 e_3, e_1 e_4), (e_2 e_3, e_2 e_4), (e_3 e_4, e_3^2 - e_4^2), T = e_3^2 + e_4^2, it is block upper triangular
     with scalar diagonal blocks 0, 0, 0, 0, -2 (1 - e_C) gam c_2, -2 gam c_2, -4 gam c_2, 0, 0, -2 gam c_2, 0; R acts
     within each unit and is skew there -- on (e_3 e_4, e_3^2 - e_4^2), in his normalization 2 e_3 (x)_s e_4, as [[0,
     2], [-2, 0]], both members of norm^2 2; and in the basis orthonormal for the inner product weighting unit k by
     eta^-k the matrix of A tends to that block diagonal as eta -> 0 (P3).

*Proof.* P1-P3 of strap5.py, exact over Q[gam, e_C, c_mu], with sympy: the Leibniz extension of s N to S^2, G = 1 -
(1/2) g tr, sigma_1(i delta) = -C^(1/2) iota_{e_2} (his notation: the contraction with the vector e^2 of the dual frame)
and E^C as in Proposition 10.21, his normalization 2 e_a (x)_s e_b of (8.11). Four-dimensional control: (i) itself, so
that 10.17's sign and his are one frame read two ways. Controls: the computed sign s = -2 against his printed matrix
with no change of frame in (i), where 8 entries differ, the nabla part; e_1^2 placed before e_1^2 - e_3^2 in (ii), where
A is not upper triangular; and c_4 = 1/3 in (iii), where A does not commute with R, nor is it block triangular in the
units (five entries below the unit blocks). []

*Deduced.*

 (a) (his Proposition 8.3 on five-dimensional Tangherlini) Near the trapped set Gamma_0 = {r^2 = 2 mu, xi = 0}
     (10.17(ii)) take 10.17's frame e_0 = zeta, e_1, e_2, normalized by C^(1/2), with nabla_{H_G} e_0 = 0, nabla_{H_G}
     e_1 = -2 sigma e_0, nabla_{H_G} e_2 = -2 sigma e_1 (trap5.py T3), and a local g-orthonormal frame e_3, e_4 of V, on
     which nabla_{H_G} is k R with k a function and R skew (10.17(a)). E^Ups vanishes near the photon sphere ((6.1)),
     S_sub(box) = -i nabla on symmetric 2-tensors ([Hin17] Proposition 4.1, his (6.13), in any dimension; 10.17 T0
     computes it on 1-forms), and (8.10) holds as he writes it, so i S_sub(2 L) = H_G + sigma A + k R in this frame, A
     that of (ii) with s = -2. 10.14's c = a(r) dt + b(r) dr has no angular part, so c_3 = c_4 = 0 and (iii) applies; it
     is past timelike at r^2 = 2 mu > r_h^2 (Proposition 10.11(i)), and e_0 is future null, so c_2 = -g^-1(c, e_0) < 0,
     and with gam = C^(1/2) gam_C/sigma > 0 -- sigma > 0 on the future characteristic set, d_t being timelike outside
     the horizon ([Hin26c] Lemma 4.14, (4.41), as he cites it) -- every diagonal block of (iii) is >= 0 (for 0 < e_C <
     1). The inner product of (iii) -- weights eta^-k on the units in the frames e_mu, the two members of each angular
     pair weighted alike -- is independent of the choice of e_3, e_4, so it is defined near Gamma_0, stationary and
     homogeneous of degree 0 -- the frame being normalized by C^(1/2) (10.17(a)), and H_G C = 0 keeping the connection
     matrix unchanged under that normalization; for it H_G is skew (it acts componentwise and preserves the symplectic
     volume), k R is skew by (iii), and the symmetric part of A is its block diagonal, >= 0, plus O(eta^(1/2)). So
     sigma^-1 (1/2)(i S_sub(2 L) + (i S_sub(2 L))^*) > -C eta^(1/2) at Gamma_0, below any eps for small eta, with the
     modification parameters fixed, as footnote 77 asks: 2 L is strongly trapping admissible on five-dimensional
     Tangherlini.
 (b) (general c) For a c with angular components, (ii)'s constant basis triangularizes A, but the rotation of V along
     the flow is skew only for weights constant on its orbits, which (ii)'s single-member units do not give; on
     Tangherlini the question does not arise, c being spherically symmetric.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23): pp. 34 (item (1)), 113-116 (section 6.1, (6.12)-(6.16c),
Lemma 6.4 and its proof), 147-149 (section 8.1: Proposition 8.3, (8.9)-(8.12), the printed A and its eigenvalues, the
proof's last paragraph, footnote 77). [Hin26c] Definition 5.8 (pp. 102-103), as 10.17 reads it, and Lemma 4.14 (p. 88),
as the thirty-fifth verifier read it.

*What this gives, and what it does not.* His Proposition 8.3 on five-dimensional Tangherlini, by his computation in five
dimensions: the 15 x 15 subprincipal matrix has the same structure as his 10 x 10 -- ten zeros and the eigenvalues -2
(1 - e_C) gam c_2, -2 gam c_2 (three times), -4 gam c_2, all >= 0 at the trapped set -- and a constant basis
triangularizes it; the one new point, the rotation of the angular plane along the flow, is absorbed by weighting the
angular pairs alike, which c's spherical symmetry permits. Not done, and OPEN: [Hin26c]'s use of it (the high-energy
estimates of Theorem 9.16 for symmetric 2-tensors in five dimensions, on the reading of 10.19); his section 8.4 (mode
stability, Proposition 8.8, which uses [AHW24] on Kerr; 10.27 deduces it), section 8.5 and sections 9-10, in five
dimensions; and the readings of 10.19-10.25. Nothing of this section is proved: Proposition 10.23 is computed, and
(a)-(b) are deduced.

### 10.27 [Hin26] Proposition 8.8 in five dimensions: the Einstein operator's mode stability (`gmodes5.py` G1-G5; D78)

*The setting.* [Hin26] Proposition 8.8 (p. 153): "Mode stability holds for L_b at all 0 != sigma in C with Im sigma >=
0: the kernel of L-hat_b(sigma) on A^alpha(X; S^2 T^*X) is trivial for all alpha in R, and L-hat_b(sigma) is invertible
as a map [Hin26c, (9.18)]." His proof (pp. 153-154): the index 0 of that map, "which follows from Proposition 8.3",
reduces invertibility to injectivity; for u in the kernel, eta := delta_{E^Ups}(sigma) G u solves box^C(sigma) eta = 0
by the second Bianchi identity, so eta = 0 by his Theorem 7.1(1); then D Ric(e^(-i sigma t*) u) = 0, and "By [AHW24,
Theorem 6.1(1)], we obtain u = delta*_{g_b}(sigma) omega where omega in A^alpha'(X; T^*X) for some alpha' in R"; then
box^Ups(sigma) omega = 0, and his Proposition 6.12 gives omega = 0. In five dimensions 10.21(e) deduces his Theorem
7.1(1), 10.20(e) his Proposition 6.12 and 10.26 his Proposition 8.3. Not computed before this section: the input from
[AHW24], mode stability of the linearized Einstein operator itself, which on Kerr goes through the Teukolsky equation.
On Tangherlini, static, the decomposition of [KI03] (H. Kodama and A. Ishibashi, arXiv:hep-th/0305147v3; n = 3, K = 1,
Lambda = 0, 2M = mu) reduces each harmonic type of S^3 to one master equation; this section computes that reduction in
five dimensions from D Ric itself.

**Proposition 10.24 (computed; exact).** On five-dimensional Tangherlini, f = 1 - mu/r^2, with h decomposed by the
harmonics of S^3 as in [KI03] (2.4), (5.1)-(5.9) -- h_ab = f_ab S, h_ai = r f_a S_i, h_ij = 2 r^2 (H_L gamma_ij S + H_T
S_ij) at the scalar type, the like at the others -- D Ric the linearized Ricci operator and delta* the symmetric
gradient:

 (i) (tensor type) For h_ij = 2 r^2 H T_ij, T trace-free and divergence-free with (Delta + k_T^2) T = 0, k_T^2 = l(l +
     2) - 2, l >= 2: D Ric(h)_ab = D Ric(h)_ai = 0 and D Ric(h)_ij = -r^2 (box H + (3/r) Dr.DH - (k_T^2 + 2) H/r^2)
     T_ij, [KI03] (5.3); and Phi = r^(3/2) H solves -Phi_tt + f (f Phi')' - V_T Phi = 0 with V_T = (f/r^2)(k_T^2 +
     11/4 + 9 mu/(4 r^2)), [KI03] (5.6) (G1).
 (ii) (vector type, l >= 2) For V co-closed with (Delta + k_V^2) V = 0, k_V^2 = l(l + 2) - 1, V_ij = -(D_i V_j + D_j
     V_i)/(2 k_V): delta*(r^2 B V_i dz^i) shifts f_a by (r/2) D_a B and H_T by -k_V B/2, so B = -2 H_T/k_V leaves H_T =
     0 and F_a = f_a + (r/k_V) D_a H_T, [KI03] (5.10); there D Ric(h)_ab = 0, D Ric(h)_ai = r E_a V_i and D Ric(h)_ij =
     2 r^2 E_T V_ij with E_T = -(k_V/(2 r^3)) D_a(r^2 F^a); and at sigma != 0, with Omega := r^2 F^r/(i sigma), E_T = 0
     is r^2 F^t = Omega', and then E_a = 0 iff Phi = r^(-3/2) Omega solves f (f Phi')' + (sigma^2 - V_V) Phi = 0, V_V =
     (f/r^2)(k_V^2 + 7/4 - 27 mu/(4 r^2)), [KI03] (5.15) (G2).
 (iii) (scalar type, l >= 2) delta* of A_a S dy^a + r^2 B S_i dz^i shifts f_ab by D_(a A_b), f_a by (r^2 D_a B - k
     A_a)/(2 r), H_L by k B/6 + f A_r/(2 r) and H_T by -k B/2, so the gauge 1-form -2 X_a S dy^a - (2 r^2/k) H_T S_i
     dz^i, X_a = (r/k)(f_a + (r/k) D_a H_T) of [KI03] (2.8), leaves f_a = H_T = 0 and their invariants F, F_ab of (2.7);
     there the reduced equations E_ab, E_a, E_L, E_T are computed, and at sigma != 0, in their X, Y, Z of (2.20)-(2.21)
     with Z = i sigma Z~: E_t, E_r and E_tr give exactly (2.24a-c); E_tt, E_rr and E_L then reduce to multiples of one
     linear form C in (X, Y, Z~), which the flow preserves, so the solutions form a two-dimensional space; Phi := (3 Z~
     - r (X + Y))/(r^(1/2) H), H = m + 6 mu/r^2, m = k^2 - 3, solves f (f Phi')' + (sigma^2 - V_S) Phi = 0 on C = 0, V_S
     = f Q/(16 r^2 H^2) with Q of (3.7) at n = 3, [KI03] (3.1)-(3.6); and det[r^(1/2) Phi; r^(1/2) Phi'; C] = -r^4 (r^2
     - mu)^5, C as G3 normalizes it: a multiple of C by a function of r rescales the determinant by that function (G3).
 (iv) (the exceptional sectors, sigma != 0) Scalar l = 0: f_tt = H_L = 0 is reached by a gauge 1-form A_t dt + A_r dr
     algebraic in the mode, and then the mode equations force f_tr = f_rr = 0. Vector l = 1 (V Killing): D Ric(h)_ab = 0
     and E_r = r^2 d_t F^(1)_tr/(2 (r^2 - mu)), F^(1)_tr = r d_t(f_r/r) - r d_r(f_t/r), [KI03] (5.16), so a mode has
     F^(1) = 0 and f_a = (r/2) D_a B with B = 2 i f_t/(sigma r). Scalar l = 1 (D_i D_j S = -gamma_ij S): the shifts of
     f_tt, f_t and H_L are free of derivatives, with determinant (r^2 - mu)(sigma^2 r^4 - mu)/(4 r^6), and then the mode
     equations force f_tr = f_rr = f_r = 0. Every pivot of these eliminations has its factors free of r among the powers
     of sigma (G4).
 (v) (the potentials, and the horizon) V_T > 0, V_V >= (f/r^2)(l (l + 2) - 6) > 0 and V_S > 0 for l >= 2 on r > r_h, Q
     >= 16 m (m - 3)(m + 9) for 3 < m <= 12 and Q >= 16 m^3 + 60 m^2 for m >= 12, so Q > 0 there (the first bound alone
     fails beyond m = 12; corrected, D79). In ingoing Eddington-Finkelstein coordinates (v = t + r*, r) Gamma^lam_rr =
     0; and the master fields, written in the ingoing components of the reduced field, are free of 1/f: 3 Z~ - r (X + Y)
     = (4 sigma r^3 F - sigma r^3 f F'_rr - 2 sigma r^3 F_vr - 3 i r^2 f F_vr - 3 i r^2 F_vv)/(r sigma) and Omega = r^2
     (f F'_r + F_v)/(i sigma) (G5).

*Proof.* G1-G5 of gmodes5.py, exact. A harmonic enters through its Taylor jets at a point of S^3 (sin chi = 3/5, sin
theta = 5/13), every jet free but for the harmonic's defining equations and their derivatives there, so that an identity
checked there holds for every harmonic of the type at that point, and so at every point, the isometries of S^3 acting
transitively and commuting with D Ric and delta*. D Ric is checked on delta* omega for an omega with arbitrary jets,
where it vanishes. At scalar l = 1 the jets stop at order 2, the constraints at order 0: S's third jet enters D Ric only
through nabla^j (nabla_j nabla_i - nabla_i nabla_j) S, which vanishes. (iv)'s eliminations -- the equations and their
r-derivatives, every derivative eliminated first -- run over Q(3^(1/2), i)(r, sigma) at mu = 1: the homothety t, r ->
lam t, lam r carries g_mu to lam^2 g_(mu/lam^2) and sigma to lam sigma, and D Ric of lam^2 g is that of g. Controls: in
(i) the divergence condition dropped, where D Ric(h)_ai is not zero; in (ii) +27 for -27; in (iii) Z = -i sigma Z~,
where (2.24a-c) fail; in (iv) f_t left free at l = 1, where the derivative-free rank is 2 of 4; in (v) V_V lowered by 6.
[]

*Deduced.*

 (a) ([AHW24] Theorem 6.1(1) on five-dimensional Tangherlini) Let 0 != sigma, Im sigma >= 0, and let h = e^(-i sigma t)
     u solve D Ric(h) = 0 on r > r_h in the class of 10.16: smooth across the future horizon and outgoing at infinity.
     Then h = delta*(e^(-i sigma t) omega) with omega in the same class. Each harmonic component of u is in the class, D
     Ric and delta* commuting with the decomposition. For l >= 2 the gauge 1-form of (ii) or (iii) is built from u's
     coefficients and their orbit-space derivatives, covariantly on the orbit space, so it is in the class, and the
     reduced field solves D Ric = 0; its master field -- r^(3/2) H, r^(-3/2) Omega, or (iii)'s Phi -- is by (v) e^(-i
     sigma r*) times a function smooth at r_h, and at infinity c e^(i sigma r*) (1 + O(1/r)), the potentials being
     O(r^-2) there. By (v) and 10.16(a) -- the energy identity int (|Phi_*|^2 + V |Phi|^2) dr* = sigma^2 int |Phi|^2 dr*
     if Im sigma > 0, the constant Wronskian Im(conj(Phi) Phi_*) if sigma is real -- Phi = 0, and then the reduced
     coefficients vanish: H by (i), F_a by (ii), X = Y = Z~ = 0 by (iii)'s determinant and so F, F_ab by (2.21). So u is
     delta* of the gauge 1-form. For l <= 1, (iv) gives u = delta* xi with xi algebraic in u's coefficients, at scalar l
     = 1 off the sphere sigma^2 r^4 = mu; across it xi is smooth, since xi = eta/(r - r_s) with eta smooth would leave
     (r - r_s)^2 delta* xi = (r - r_s) delta* eta - dr (x)_s eta smooth only with eta(r_s) = 0. In every sector xi is
     smooth across the future horizon: by (v), in ingoing coordinates (delta* xi)_rr = d_r xi_r, and the r-row of delta*
     xi = u is a linear ODE in r for xi whose coefficients and source are smooth across r = r_h, the exterior xi its
     solution. Summed over the harmonics, the gauge 1-forms' coefficients are bounded by polynomial multiples in l of
     u's and of their derivatives, so the sum converges with u's.
 (b) ([Hin26] Proposition 8.8 in five dimensions) His proof then runs as written: eta = 0 by his Theorem 7.1(1)
     (10.21(e), on [Hin26a] Theorem 5.2, which 10.22 deduces on a reading); u = delta*(sigma) omega by (a);
     box^Ups(sigma) omega = 0 on r >= r_h; continued into the part of X inside the horizon as a solution of
     box^Ups(sigma) omega = 0 -- harmonic by harmonic a linear ODE in r with coefficients smooth there -- it vanishes by
     his Proposition 6.12 (10.20(e)), a statement on all of X, and u = 0 on r >= r_h; the index 0 comes from his
     Proposition 8.3 (10.26) through [Hin26c] Theorem 9.5 on the reading of 10.19. So, on the readings of 10.19-10.26,
     at Proposition 10.9's point with gam_Ups small, L-hat(sigma) is injective, and so invertible, at 0 != sigma, Im
     sigma >= 0 -- with, as in 10.16, the kernel elements' class ([Hin26c] Theorem 9.5(5) in five dimensions), omega's
     continuation into the part of X inside the horizon as a solution there (the harmonics summed), and the vanishing of
     u carried from r >= r_h to that part by the standard interior uniqueness, all OPEN (D149: the continuation and the
     interior uniqueness deduced at proof level in 10.76 from Lemma 10.56; the class stays on 10.53 (c)'s reading, 10.55
     (b)).

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23): pp. 25 (section 1.4.1: "Mode stability for the ungauged
linearized Einstein equation D_{g_b} Ric(h) = 0 (see [AHW24, Theorem 6.1(1)]) implies that h is the sum of a linearized
Kerr metric g-dot_b(b-dot) and a pure gauge term delta*_{g_b} omega. In the absence of the former (which can only occur
at frequency sigma = 0) ..."), 153-154 (section 8.4: Proposition 8.8 and its proof). [KI03] (arXiv:hep-th/0305147v3,
alphaXiv, 2026-10-23): pp. 4-5 ((2.1)-(2.8)), 7-10 ((2.20)-(2.24), (3.1)-(3.14)), 13-15 (section 5, (5.1)-(5.17)), 18-20
(Appendices A and B). The extraction drops minus signs; (2.23)'s Z = i sigma Z~ is settled by (A.1b) through (2.22a),
(2.24c), (3.9c) and (3.12c), and by G3, where the other sign fails.

*What this gives, and what it does not.* The input his Proposition 8.8 takes from [AHW24] on Kerr, on five-dimensional
Tangherlini: every outgoing mode of the linearized Einstein operator at sigma != 0, Im sigma >= 0, is pure gauge, its
gauge 1-form in the same class. The computation is [KI03]'s, carried from their general formulas to D Ric at n = 3
directly: the tensor type, which four dimensions lacks, has the potential of 10.16's scalar wave (k_T^2 + 2 = l(l + 2));
the vector potential's -27 mu/(4 r^2) and the scalar potential's Q leave both positive at l >= 2; and l <= 1 is pure
gauge at nonzero frequency. Not done, and OPEN: the kernel elements' class, omega's continuation inside the horizon and
the interior uniqueness, as in 10.16 (the last two deduced at proof level in 10.76; D149); how small gam_Ups must be,
and h_0, below
which Proposition 10.9's h = 10^-6 must lie (10.21(e)); the zero-energy analysis of his section 8.4 (Proposition 8.9,
Remark 8.10 and Proposition 8.11, [AHW24] Theorem 6.1(2); 10.28 deduces Proposition 8.9, 10.32 Proposition 8.11 up to
[AHW24] Theorem 6.1(2), which 10.33 deduces at a = 0), section 8.5 and sections 9-10, in five dimensions; and the
readings of 10.19-10.26. Nothing of this section is proved: Proposition 10.24 is computed, and (a)-(b) are deduced.

### 10.28 [Hin26] section 6.5.1, Proposition 8.9 in five dimensions: zero energy states (`zstates5.py` Z1-Z6; D80, D82)

*The setting.* [Hin26] section 6.5.1 builds the zero energy states of box^Upsilon from the symmetries of Minkowski space
-- dt, the translations d(rS) (S in S_1, the span of the x^i/r), the boosts t* d(rS) + r d(rS) - rS dt and the rotations
V (V in V_1, dual to the rotation vector fields) ((6.29)) -- each corrected by solving box^Ups(0) omega' =
-box^Ups(0)(leading term) with his Lemma 6.13, the orders from his Lemma 6.14: delta*_g(0) - delta*_gbar(0) in rho^2
Diff^0_b and box^Ups(0) - box^Ups_gbar(0) in rho^3 Diff^2_b, Kerr meeting Minkowski at m/r. His Proposition 6.15 gives
h_b,s1(S) in A^((2,0) u (2 + E_ind)) ((6.32a)), the boost's correction with a logarithm, (log rho) c_b,s1
omega-bar_s1(S) ((6.31)), the s1 root 0 met, and h_b,v1 = 0 at a = 0 (Remark 6.17). His Proposition 8.9 brings the
linearized Kerr metrics into the gauge delta_(g,E) G h = 0, delta_(g,E) = delta_g + E^Ups, E^Ups h = -gam_Ups (2
iota_(g^-1 c) h - (1 - e_Ups) c tr h), c = r^-1 dt near infinity ((4.1)-(4.3)): g-dot(1, 0) in rho C^oo has its source
in rho^2 C^oo, so its gauge 1-form carries (log rho) c_b omega-bar_s0 ((8.19)), the s0 root 0 met; g-dot(0, a-dot) in
rho^2 C^oo has its source in rho^3 C^oo and its gauge 1-form at rho^1, 1 being no root ((8.20)). Both feed his
Proposition 8.11, the seven-dimensional kernel of L-hat(0), and Lemma 8.12's pairings. In five dimensions E^Ups takes
the trace weight 2/3 (10.15), and z = 4 e_Ups gam_Ups^2 enters the indicial roots of 10.15(i).

**Proposition 10.25 (computed; exact).** On five-dimensional Tangherlini, f = 1 - mu/r^2, against 4+1 Minkowski gbar,
with four-dimensional Schwarzschild as the control:

 (i) (the orders, his Lemma 6.14) In Cartesian coordinates g - gbar is in rho^2 C^oo and Gamma(g) of order rho^3 (four
     dimensions: rho, rho^2), the same along a second ray; whence -- deduced, as his Lemma 6.14 from his (3.21) --
     delta*_g(0) - delta*_gbar(0) is in rho^3 Diff^0_b and box^Ups(0) - box^Ups_gbar(0) in rho^4 Diff^2_b; and r* = r +
     (r_h/2) log((r - r_h)/(r + r_h)) has r* - r -> 0, with no logarithm (four dimensions: r* - r ~ 2M log r) (Z1).
 (ii) (the translations) delta*_g dx^1 is of order rho^3 and box dx^1 = 2 delta G delta* dx^1 of order rho^4 (four
     dimensions: rho^2, rho^3); 2 is an s1 root of box^Ups(0) at z = 0 (the root l + 1 at l = 1) and not for z > 0,
     where the root through 2 is (1 + (17 + 2z - 2 (z^2 + 4z + 16)^(1/2))^(1/2))/2 > 2 (Z2).
 (iii) (the boosts) delta*_g (t dx^1 - x^1 dt) = t delta*_g dx^1 + K with K stationary of order rho^2 (four dimensions:
     rho); with his t-bar = t* + r ((6.5)), in retarded coordinates u = t* = t - r*, g = -f du^2 - 2 du dr + r^2 (round
     S^3) and gbar = -du^2 - 2 du dr + r^2 (round S^3), the boost B-bar = t-bar dx^1 - x^1 dt-bar is Killing for gbar,
     K-bar = delta*_g B-bar - t* delta*_g dx^1 is of order rho^2 and the stationary residual box^Ups_g B-bar - t*
     box^Ups_g dx^1 of order rho^3 (four dimensions: rho, rho^2); 1 is no s1 root of box^Ups(0) for z >= 0, the s1
     polynomial at l = 1 being 3 (12 + 3z) at lam = 1 (Z3).
 (iv) (the rotations) each of the six x^i dx^j - x^j dx^i equals g gbar^-1 of itself and is Killing for g; as 1-forms
     they have rank 6 (V_1 = so(4)), and the x^i/r rank 4 (S_1) (Z4).
 (v) (the linearized rotating and mass-changing metrics) h_mu = d_mu g and h_A = (mu/r^4)(dt (x) w + w (x) dt), w = x^1
     dx^2 - x^2 dx^1, solve D Ric(h) = 0 and are of orders rho^2 and rho^3 (four dimensions: d_M g of order rho); eta_mu
     = delta_(g,E) G h_mu is of order rho^3 and spherically symmetric; delta G h_A = 0, so eta_A = E^Ups h_A = (2
     gam_Ups mu/(f r^5)) w, of order rho^4 and of vector type l = 1; and 1 is no s0 root and 2 no v1 root of box^Ups(0)
     (10.15(i): s0 0, 3, (1 +- (9 + 4z)^(1/2))/2; v1 -1, 3; the s0 polynomial at 1 is 2 (2 + z), the v1 polynomial at 2
     is 3), the orders the same at a second angle (Z5).
 (vi) (the Myers-Perry family) The one-spin metric of [ER08] (32)-(33) at d = 5, -dt^2 + (mu/Sigma)(dt - a sin^2 theta
     dphi)^2 + (Sigma/Delta) dr^2 + Sigma dtheta^2 + (r^2 + a^2) sin^2 theta dphi^2 + r^2 cos^2 theta dpsi^2, Sigma =
     r^2 + a^2 cos^2 theta, Delta = r^2 + a^2 - mu, has Ric = 0 at three exact points, is Tangherlini at a = 0 on the
     round S^3 (x^1 + i x^2 = r sin theta e^(i phi), x^3 + i x^4 = r cos theta e^(i psi)), and d_a g at a = 0 is -h_A,
     with w = r^2 sin^2 theta dphi = x^1 dx^2 - x^2 dx^1 (Z6).

*Proof.* Z1-Z6 of zstates5.py, exact. (i), (iii) and (iv) in Cartesian coordinates, g = -f dt^2 + dx^2 + (mu/(r^2 -
mu))(x.dx)^2/r^2, the orders read along the generic ray x = R u, u = (2, 4, 5, 6)/9, and again along (1, 2, 4, 10)/11,
where every component is rational in R; (ii), (iii)'s t-bar part and (v) in polar or retarded coordinates, the orders
read on gbar's orthonormal frame (dt, dr, r dchi, r sin chi dtheta, r sin chi sin theta dphi) at sin chi = 3/5, sin
theta = 5/13, sin phi = 8/17, and again at 5/13, 8/17, 3/5 -- the same orders, the two frames differing by a rotation
bounded with its inverse; a leading coefficient vanishing on the chosen ray or angle could only overstate an order, and
the orders agree at both. (vi) by the curvature at (r, a, mu, sin theta) = (2, 1/3, 1, 3/5), (3, 1/2, 2, 5/13) and (5/2,
2/7, 3/2, 8/17), exact. Controls: in (i) the four-dimensional orders claimed; in (ii) z = 0; in (iii) four-dimensional
Schwarzschild, where K is of order rho; in (iv) f R, which is not Killing; in (v) four-dimensional Schwarzschild's
d_M g, of order rho, its source at rho^2; in (vi) a^2 dropped from Delta, not Ricci-flat. []

*Deduced.*

 (a) ([Hin26] Proposition 6.15 in five dimensions) Take z > 0, and his Lemma 6.13 in five dimensions (deduced in 10.29
     on the readings of 10.20). His proof runs with every order raised by one. Translations: f_b = box^Ups
     omega-bar_s1(S) is in rho^4 C^oo by (ii), its E^Ups part too (c in rho C^oo against delta*_g dx^1 in rho^3), of
     type s1, so omega' = -box^Ups(0)^-1 f_b is in A^((2,0) u (2 + E_ind)), 2 being no s1 root at z > 0, and h_b,s1(S) =
     delta*_g omega_b,s1(S) in A^((3,0) u (3 + E_ind)). Boosts: of his four terms in f-breve_b the first vanishes, the
     boost being Killing for gbar, and the others gain one order: [box^Ups - box^Ups_gbar, t*] omega-bar_s1 +
     (box^Ups(0) - box^Ups_gbar(0)) omega-breve-bar^1 is (iii)'s stationary residual, of order rho^3 (computed; in four
     dimensions he cites his Lemma 6.1's structure), and [box^Ups, t*] omega' is in A^((3,0) u (3 + E_ind)) -- so
     f-breve_b is in A^((3,0) u (3 + E_ind)), of type s1, and the stationary correction lies at rho^1, 1 being no s1
     root by (iii): no logarithm in place of (6.31), and h-breve^1_b,s1(S) in A^((2,0) u (2 + E_ind)), K being of order
     rho^2. Rotations: by (iv) omega_b,v1(V) = V and h_b,v1(V) = 0 for all six V (his Remark 6.17 at a = 0); and
     omega_b,s0 = g(d_t, .) is Killing.
 (b) ([Hin26] Proposition 8.9 in five dimensions) Mass: g-dot(mu) = h_mu is in rho^2 C^oo and 2 eta_mu in rho^3 C^oo,
     spherically symmetric, so the gauge 1-form omega-dot(mu) = -box^Ups(0)^-1(2 eta_mu) is in A^((1,0) u (1 + E_ind)),
     1 being no s0 root -- no logarithm in place of (8.19) -- and g-dot^Ups(mu) = h_mu + delta*_g omega-dot(mu) in
     A^((2,0) u (2 + E_ind)). Angular momenta, one for each antisymmetric A, six in place of his three: g-dot(A) = h_A
     is in rho^3 C^oo and its source 2 eta_A = 2 E^Ups h_A in rho^4 C^oo, of vector type l = 1, so omega-dot(A) is in
     A^((2,0) u (2 + E_ind)), 2 being no v1 root, and g-dot^Ups(A) in A^((3,0) u (3 + E_ind)); at gam_Ups = 0 the source
     would vanish and h_A be in the gauge already. By (vi), h_mu and h_A are the derivatives of the five-dimensional
     Myers-Perry family ([ER08] (32)-(33)) at zero rotation, in the mass and in the rotation in A's plane (h_A with the
     rotation reversed: d_a g = -h_A).

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23; quotations transliterated to ASCII): pp. 25 (section 1.4.1:
"The zero energy nullspace of L_b is always nontrivial; it is 7-dimensional when the two 1-form wave operators have no
zero modes"), 81 (Definition 4.1, (4.1)-(4.3); footnote 49: "upon perturbing away the s1 indicial root 0--which is
absent indeed in Lemma 8.4--mildly simplifies the construction of improved zero energy states corresponding to
asymptotic boosts"), 113 (Lemma 6.1), 117 (Lemma 6.6), 124-128 (Lemma 6.13; section 6.5.1: Lemma 6.14, Proposition 6.15,
(6.29)-(6.35), Remarks 6.16-6.17, and the proof: "Since 1 is not an indicial root of box^Ups_{g_b,E^Ups}(0), we have
omega'_b in A^{(1,0) u (1+E_ind)}"), 154-155 (Proposition 8.9 and its proof, (8.19)-(8.20): "This is equal to
-box^Ups_{g_b,E^Ups}(0) omega-dot_b(0, a-dot) for some omega-dot_b(0, a-dot) in A^{(1,0) u (1+E_ind)} by Lemma 6.13 and
the fact that 1 is not an indicial root"; Remark 8.10; Proposition 8.11), 157 (Lemma 8.12, Corollary 8.13). [ER08] (R.
Emparan, H. S. Reall, Black holes in higher dimensions, arXiv:0801.3471v2, alphaXiv, 2026-10-23): p. 14 (section 4.1,
the single-spin metric (32)-(33)).

*What this gives, and what it does not.* The zero energy states his section 6.5.1 builds and the gauged linearized
metrics of his Proposition 8.9 have five-dimensional counterparts, at the level of deduction, one order faster in rho
and without his two logarithms: Tangherlini meets Minkowski at mu/r^2 where Kerr does at m/r; the exponents the
constructions need -- 1 for the boosts and the mass, 2 for the translations and the angular momenta -- miss the
five-dimensional indicial roots once z > 0, the translations' 2 meeting the s1 root at z = 0, which e_Ups, gam_Ups > 0
move; and the rotations' gauge source comes from E^Ups alone. Not done, and OPEN: his Lemma 6.13 in five dimensions
(10.20; 10.29 deduces it on 10.20's readings), and with it every inverse used here; the index sets E_ind; section 6.5.2
(Proposition 6.18, the generalized zero energy states; 10.29-10.30 deduce it), section 7.2's dual states (10.31 deduces
them, section 7.2.1 at first order in the rotation), his Proposition 8.11, Lemma 8.12's pairings and Corollary 8.13 in
five dimensions (10.32) -- the candidates for his Proposition 8.11's kernel number 1 + 6 + 4 = 11 against his 7, a count
not established; section 8.5 and sections 9-10; how small gam_Ups must be, and h_0. Nothing of this section is proved:
Proposition 10.25 is computed, and (a)-(b) are deduced.

### 10.29 [Hin26] Lemma 6.13 and Proposition 6.18 (1)-(3) in five dimensions (`genstates5.py` H1-H5; D81)

*The setting.* His Lemma 6.13 (pp. 124-125): for E^Ups of his Proposition 6.12, large s and alpha in (0, lam^Ups_s1,1),
the zero energy operator box^Ups(0) from {u in H-bar^(s,alpha)_b : box^Ups(0) u in H-bar^(s-1,alpha+2)_b} to
H-bar^(s-1,alpha+2)_b is invertible (an unweighted b-density), and box^Ups(0)^-1 maps A^(2+E), min Re E > 0, into some
A^(E'), min Re E' > 0, "a special case of Lemma 2.13" (pp. 51-52, polyhomogeneity by the Mellin transform on a compact
manifold with boundary). Its inputs are his (6.17b) -- "no indicial root lies in the interval (0,
lambda^Upsilon_{s1,1}), which is thus an indicial gap" (p. 117) -- the Fredholm property there ([Hin26c] Theorem 9.36),
index 0 ((6.20), [Hin26c] Corollary 9.43 with his Lemma 6.8) and his Proposition 6.12 at sigma = 0. His Proposition
6.18 (pp. 129-134) builds generalized zero energy states, polynomials in t*, for the roots of L-hat(0) with real part
in [-3, 0] that are not stationary pure gauge: (1) the s0 root 0, the correction omega-breve^(0),1_s0 in A^((-1,0) u
(0,1) u (1 + E_ind)), its source "with s0 leading- and sub-leading-order term" (p. 132); (2) the s1 root -1, the boost
carried to second order, its leading term h-bar^2_s1 stationary, "this stationarity is due to t* omega-bar_s1(S) +
omega-breve-bar^1_s1(S) being a Killing 1-form (namely, a Lorentz boost)" (p. 132); (3) the v1 root -1, with his
(6.40), h-bar^1_v1(V) = (1/4)(0, 0, (1 + gam_Ups/2) V, 0, (1 - gam_Ups/2) V, 0) in his splitting (2.37b), and his
Remark 6.19: at a = 0 the rotation is Killing and h^(<=1)_v1 a large zero energy state; and (4)-(7), the states from
box^Ups's roots below -1. 10.28 deduced section 6.5.1 and Proposition 8.9 in five dimensions on Lemma 6.13 there, OPEN.

**Proposition 10.26 (computed; exact).** On 4+1 Minkowski, with E^Ups at the trace weight 2/3 and c = r^-1 dt (10.15),
e_U = e_Ups, gam_U = gam_Ups and z = 4 e_U gam_U^2, in polar coordinates and in his splitting (2.37b) on d xbar^0, d
xbar^1 and r T*S^3 (xbar^0 = t + r, xbar^1 = t - r = t*), and on five-dimensional Tangherlini, f = 1 - mu/r^2:

 (i) (part (1)) t* omega-bar + W, omega-bar = -dt, W = r (-dt + b dr), b = (2 - e_U)/(4 e_U), solves box^Ups = 0;
     h-bar^(0)_s0 = delta*(t* omega-bar + W) is stationary, of degree 0, (a, b, e, p) = (2 - 5 e_U, -(2 + 3 e_U), 2 - 5
     e_U, 4 (2 - e_U))/(16 e_U), and lies in the kernels of D Ric and of delta_(g,E) G. On Tangherlini the source
     box^Ups(t* omega_s0) = 2 delta_(g,E) G (dt* (x)_s omega_s0), omega_s0 = -f dt, has on (dt, dr) the rho^1 term (2
     e_U gam_U - 4 gam_U - 3, 2 gam_U), no rho^2 term, and the rho^3 term (mu, 2 mu (gam_U + 1)); -1, -2, -3 and -4 are
     no s0 roots of box^Ups(0) for 0 < z < 4 (-1 for every z > 0; -2 is one at z = 4) (H1).
 (ii) (part (2)) t*^2 dx^1 + 2 t* B + 2 W, B = r d(rS) - rS dt, S = x^1/r, W = r^2 (alpha S d(t + r) + beta S d(t -
     r)) + kappa r^3 dS, (alpha, beta, kappa) = (4 - 7 e_U, -(4 + 17 e_U), (2/3)(25 e_U - 4))/(24 e_U), solves box^Ups
     = 0; h-bar^2_s1 = dt* (x)_s B + delta* W is stationary, nonzero, of degree -1, and in both kernels; -2, -3 and -4
     are no s1 roots for 0 < z < 20/3 (-2 for every z > 0 and one at z = 0; -3 one at z = 20/3) (H2).
 (iii) (part (3)) t* V + kappa r V, V = x^1 dx^2 - x^2 dx^1 = r^2 sin^2 chi sin^2 theta dphi, solves box^Ups = 0 exactly
     at kappa = 1 + 2 gam_U/5, and h-bar^1_v1 = (1/4)(0, 0, (1 + 2 gam_U/5) V, 0, (1 - 2 gam_U/5) V, 0), stationary and
     in both kernels: his (6.40) in five dimensions; -2, -3 and -4 are no v1 roots at any z (H3).
 (iv) (the four-dimensional control) His printed dt* (x)_s omega-bar = (0, -1/4, -1/2, 0) (p. 132), dt* (x)_s B = (0, 0,
     0, -1, 1/2, 0) rho^-1 S (p. 133), kappa = 1 + gam_U/2 and (6.40) (pp. 130, 134) come out exactly, b and (alpha,
     beta, kappa) there being (2 - e_U)/(3 e_U) and (2 - 3 e_U, -(2 + 7 e_U), 2 (4 e_U - 1))/(10 e_U); the Schwarzschild
     source has the rho^2 term (2M, 2M (2 gam_U + 1)) (H4, and H1's control); the two splittings are the same in five
     dimensions (H4).
 (v) (his Lemma 6.13's gap) The s1 and s0 roots of box^Ups(0) through 2 are lam_s1,2 = (1 + (17 + 2z - 2 (z^2 + 4z +
     16)^(1/2))^(1/2))/2 = 2 + z/12 + O(z^2) and lam_s0 = (1 + (9 + 4z)^(1/2))/2 = 2 + z/3 + O(z^2), and lam_s1,2 <
     lam_s0 for every z > 0, his (6.17b); 1 and 2 lie in (0, lam_s1,2) for z > 0, 2 at its edge at z = 0 (H5).

*Proof.* H1-H5 of genstates5.py, exact. Each 1-form is posed with unknown coefficients, box^Ups taken in polar
coordinates, the coefficients solved from the expansion in r and t at generic angles, and the vanishing then checked
identically; the values -k against the roots of box^Ups(0) by the least positive zero in z of 10.15(i)'s polynomial at
each; the splitting is read on d_0 = (d_t + d_r)/2 and d_1 = (d_t - d_r)/2. Controls: in (i) the five-dimensional claim,
no rho^2 term, on Schwarzschild, and -2 claimed no s0 root at z = 4; in (ii) the factor 2 on B dropped, where no W
exists, and -3 claimed no s1 root at z = 20/3; in (iii) his kappa = 1 + gam_U/2 in five dimensions; in (iv) the
five-dimensional kappa in four; in (v) z = 0, where 2 is the gap's edge, and lam_s1,2's first-order coefficient claimed
1/3. []

*Deduced.*

 (a) ([Hin26] Lemma 6.13 in five dimensions) For alpha in (0, lam_s1,2) -- an indicial gap by 10.15(i) and (v), every
     other root at least 3 or at most 0 -- the zero energy operator is Fredholm (10.20(a)) and of index 0 (10.20(d)),
     the index constant across the gap, and injective at the shifted weights in (0, 1) (his Proposition 6.12 at sigma =
     0, 10.20(e)); so injective at every alpha in the gap, past weight 1 by inclusion alone, rho^alpha H_b lying in
     rho^alpha' H_b for alpha > alpha' -- his "and thus has trivial nullspace on A^eps(X; T*X) for all eps > 0" (p.
     121), a kernel element being moreover polyhomogeneous by his Lemma 2.13, its exponents in the index set the
     indicial roots above the gap generate (shifted by integers, possibly with logarithms) -- and invertible, on the
     b-spaces of 10.20 with the shift alpha + 2 of Proposition 10.17(iii), which is alpha itself for an unweighted
     b-density; and its polyhomogeneity is his Lemma 2.13, a statement on any compact manifold with boundary, here [0,
     rho_0) x S^3. So, on the readings of 10.20, his Lemma 6.13 holds in five dimensions, and 10.28's deductions rest on
     it rather than on an OPEN input. Every correction 10.28 needs lies inside the gap -- at rho^1 for the boosts and
     the mass, at rho^2 for the translations and the rotating metrics, the rotations themselves needing none at a = 0 --
     so Lemma 6.13 applies to it directly; his boosts' and mass's corrections sit at rho^0, the gap's lower end, and
     need his Lemma 2.15 first.
 (b) ([Hin26] Proposition 6.18 (1)-(3) in five dimensions) Part (1): by (i) the source is rho times its leading term
     plus O(rho^3), and box^Ups(0) - box^Ups_gbar(0) is in rho^4 Diff^2_b (Proposition 10.25(i)), so
     omega-breve^(0),1_s0 = W + A^((1,0) u (1 + E_ind)), without his (0,1): no logarithm; the leading term h-bar^(0)_s0
     of h^(0)_s0 spans the one-dimensional kernel of N_s0(L-bar(0), 0) (10.24(a)-(b)); and omega-breve^(0),k_s0, k = 2,
     3, 4, exist, -k being no s0 root for 0 < z < 4 (his Lemmas 2.15 and 6.13). Part (2): by (ii) omega-breve^(0),k_s1,
     k = 2, 3, 4, exist with s1 leading terms, -k being no s1 root for 0 < z < 20/3, and h-bar^2_s1(S) spans ker
     N_s1(L-bar(0), -1), the root simple (10.24(iv)). Part (3): by (iii) with h-bar^1_v1 as computed; and since every
     rotation is Killing on Tangherlini (Proposition 10.25(iv)), h^(<=1)_v1(V) = h-breve^1_v1(V) is a stationary large
     zero energy state for each of the six V in V_1 = so(4) -- his Remark 6.19 at a = 0, six states where he has three.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23; quotations transliterated to ASCII): pp. 51-52 (Lemma 2.13
and its proof, Remark 2.14, Lemma 2.15 and its proof), 64-67 (Definition 2.28, (2.34)-(2.35), (2.37b), (2.38)-(2.40),
Lemma 2.29, (2.43)-(2.46c), Definition 2.30), 81 (Definition 4.1, and: "The flexibility afforded by allowing for nonzero
e^Upsilon simplifies some bookkeeping: it is used in the present paper to reduce the multiplicity of these indicial
roots as well as to remove integer coincidences in indicial roots of zero energy operators, which leads to fewer
logarithmic terms (at low exponents) in asymptotic expansions."), 113 (Lemma 6.1), 117-119 (Lemma 6.6, (6.17a)-(6.17b),
Lemma 6.8, (6.20)), 121 (Proposition 6.12, and: "and thus has trivial nullspace on A^eps(X; T*X) for all eps > 0"),
124-125 (Lemma 6.13 and its proof), 128-134 (section 6.5.2: Proposition 6.18, (6.40) on p. 130, (6.36)-(6.42), Remark
6.19, and the proof).

*What this gives, and what it does not.* His Lemma 6.13 stands in five dimensions on the readings of 10.20, and with it
10.28's constructions; and the first three classes of his generalized zero energy states -- on the time translation, on
the translations and boosts carried to second order, and on the rotations -- have five-dimensional counterparts, their
leading terms computed exactly on Minkowski, part (1) without his logarithm, his (6.40) becoming (1/4)(1 +- 2 gam_U/5),
six rotation states at a = 0. The coefficients of (i) and (ii) carry 1/e_U, in four dimensions as in five: at e_U = 0,
-1 at s0 and -2 at s1 are roots of box^Ups(0), the integer coincidences his e_Ups > 0 removes (p. 81). Not done, and
OPEN: the readings of 10.20 line by line; the index sets E_ind; his Proposition 6.18 (4)-(7) in five dimensions (10.30
computes their leading terms and deduces them); section 7.2's dual states (10.31); his Proposition 8.11, Lemma 8.12's
pairings and Corollary 8.13 in five dimensions (10.32); section 8.5 and sections 9-10; how small gam_Ups must be, and
h_0. Nothing of this section is proved: Proposition 10.26 is computed, and (a)-(b) are deduced.

### 10.30 [Hin26] Proposition 6.18 (4)-(7) in five dimensions: the states without symmetry (`puregauge5.py` J1-J6; D84)

*The setting.* [Hin26] section 6.5.2 lists the generalized zero energy states by the roots of L-hat(0) in [-3, 0] (p.
128); parts (1)-(3), on the time translation, the boosts and the rotations, are 10.29's. "The remaining four classes of
pure gauge solutions we record are not 'special' in that the corresponding gauge potentials do not involve
(approximate) symmetries" (p. 130): "For each indicial root lambda in Lemma 6.6 (all of which are real) with lambda <
-1, there exists an element in ker box^Ups(0) with rho^lambda-growth and leading-order term given by an indicial
solution corresponding to the indicial root lambda. The symmetric gradient thereof is a pure gauge state with
nontrivial rho^(lambda+1) leading-order term" (p. 131), the s2 root -1 included: (4) the s0 root -lam^Ups_s0,1, (5) the
sl roots -lam^Ups_sl,l+j, l = 1, 2, 3, j = 0, 1, (6) the sl roots -l + 1, 2 <= l <= 5, (7) the vl roots -l, l = 2, 3,
4, each with generalized states (6.36a) of degree k up to 2, 2, 5 - l and 4 - l. His proof (p. 134) solves box^Ups(0)
omega' = -(box^Ups(0) - box-bar^Ups(0)) omega-bar, notes that the symmetric gradient "has non-zero leading-order term
since N(delta*(0), lambda - 1) is injective (see the discussion following (2.46c))", and solves A0 omega-breve^k = -A1
omega-breve^(k-1) - A2 omega-breve^(k-2) "using Lemmas 2.15 and 6.13 as usual", box^Ups = A0 + A1 d_t* + A2 d_t*^2
((6.4a), (6.6)). In five dimensions the gauge potential operator's roots are 10.15(i)'s, its zero energy operator
differs from Minkowski's in rho^4 Diff^2_b (Proposition 10.25(i)), and his Lemma 6.13 is 10.29(a)'s.

**Proposition 10.27 (computed; exact).** On 4+1 Minkowski, with E^Ups at the trace weight 2/3, c = r^-1 dt and z = 4 e_U
gam_U^2, in his splitting (2.37b), (2.43) -- s0 and sl 1-forms (a S, b S, c dS) on d xbar^0, d xbar^1 and r T*S^3, vl
1-forms c r V -- with N0(lam) = rho^-2 A0 and N1(lam) = rho^-1 A1 on rho^lam:

 (i) (the indicial families) For s0, sl (l <= 5) and vl (l <= 4), A2 = 0, det N0 is 10.15(i)'s polynomial exactly, and
     N1 = -2 (lam - 3/2) + 2 S-bar with S-bar independent of lam; at vl N0 = -(lam + l)(lam - l - 2) and N1 = -2 (lam -
     3/2 - gam_U). In four dimensions N0 is his Lemma 6.6 matrix entry by entry (p. 117), N1 = -2 (lam - 1) + 2 S-bar,
     and N1_v1 = -2 (lam - 1 - gam_U) (p. 134) (J1).
 (ii) (the classes) For every l, Q(l(l + 1)) = l z and Q((l + 1)(l + 2)) = -(l + 2) z (Q of 10.15(i)), so for z > 0 Q's
     two negative roots satisfy -l - 1 < mu_l,0 < -l and mu_l,1 < -l - 1, with mu_l,0 = -l - l z/(2 (l + 1)(2l + 1)) +
     O(z^2) and mu_l,1 = -l - 1 - (l + 2) z/(2 (l + 1)(2l + 3)) + O(z^2) (l <= 6); mu_s0 = (1 - (9 + 4z)^(1/2))/2 = -1 -
     z/3 + O(z^2) lies in (-2, -1) for 0 < z < 4; sl's -l + 1 and vl's -l are roots at every z; and at z = 1/100 the
     roots <= 0 of each type are these and the Killing 0 (s0, s1) and -1 (v1). In four dimensions his -lam_s0,1 = -(1 +
     z)^(1/2), his lam_sl,l and lam_sl,l+1 and his first-order coefficient 2/(2l + 1) (in his z = z/4) come out of (i)'s
     matrices (J2).
 (iii) (the symmetric gradient) N(delta-bar*(0), lam) is injective except at 0 (s0, s1) and -1 (v1), in five dimensions
     as in four, and never fails at sl (2 <= l <= 5) or vl (2 <= l <= 4); in four dimensions his (2.46a)-(2.46c) come out
     entry by entry (J3).
 (iv) (no resonance) For each class root mu, none of mu - k (k up to his range), mu + 2 and mu itself, as a double root,
     meets a root of its type for 0 < z < 4, and 4 is sharp: there the s0 class root -2 meets 0 under mu + 2. In four
     dimensions, mu + 1 in place of mu + 2, the bound is 3 and not sharp: at z = 3 only the s0 partner root 2 meets (2 -
     2 = 0, and 2 is double), the class root -2 nothing. At z = 0 they meet exactly at sl: mu_l,0 - 1 = mu_l,1, mu_l,1 +
     2 = -l + 1, and -l + 1 - k = mu_l,k-1 for k <= min(2, 5 - l) (four dimensions: mu + 1 = 0 at s0, and at sl mu_l,0 -
     1 = mu_l,1, mu_l,1 + 1 = mu_l,0, mu_l,0 + 1 = -l + 1 and the same -l + 1 - k); never at vl (J4).
 (v) (the states) t*^k omega-bar + sum_i k!/(k - i)! t*^(k - i) omega-breve-bar^i, omega-breve-bar^i at rho^(mu - i) from
     N0(mu - i) omega-breve-bar^i = -N1(mu - i + 1) omega-breve-bar^(i - 1), lies in ker box^Ups at every class's largest
     k: exactly in e_U and gam_U at sl's -l + 1 and vl's -l, in both dimensions, and at s0's and Q's roots modulo their
     polynomial, irreducible over Q, at (e_U, gam_U) = (1/3, 1/2) and (1/7, 2/5). At vl, omega-breve-bar^i = kappa_i r^i
     omega-bar with kappa_i = prod_(j <= i) (2l + 2j + 1 + 2 gam_U)/(j (2l + j + 2)) (four dimensions 2 (l + j +
     gam_U)/(j (2l + j + 1))): 10.29's 1 + 2 gam_U/5 and his 1 + gam_U/2 at l = 1 (J5).
 (vi) (e_U = 0, on Minkowski) At e_U = 0, gam_U = 1/3 and 2/7, in both dimensions: mu_l,0 = -l's first recursion step,
     which meets mu_l,1 = -l - 1, is obstructed, rank N0(-l - 1) = 2 against 3 with its right side (l = 1, 2, 3); -l +
     1's first step, which meets -l, is solvable, rank 2 with its right side (l = 2, 3, 4); and its second, which meets
     -l - 1, has an obstruction of degree 1 in the first step's kernel coefficient alpha, so one alpha removes it (l = 2,
     3; five dimensions, l = 2, gam_U = 1/3: 2 (15 alpha - 17)/63) (J6).

*Proof.* J1-J6 of puregauge5.py, exact. N0 and N1 are read by applying box^Ups to rho^lam times each basis 1-form, lam a
symbol, and to t* times it, at r = 1 and two generic angles, with the zonal harmonic U_l(cos chi) at sl and P(x^3,
x^4)(x^1 dx^2 - x^2 dx^1)/r^(l + 1), P harmonic of degree l - 1, at vl; the classes by exact real roots; the injectivity
by the real roots of det(M^T M), M the symmetric gradient's matrix at two angles; the resonances by resultants in lam and
their least positive zeros in z, and the roots at the bound exactly; the states by applying box^Ups to the assembled
t*-polynomial in polar coordinates, every power of t checked, the irrational roots carried as a symbol modulo their
irreducible polynomial with each step's det N0(mu - i) checked nonzero modulo it; the e_U = 0 steps by ranks and the left
kernel. Controls: in (i) his four-dimensional matrices claimed in five dimensions; in (ii) z = -1/100, where the roots
move the other way; in (iii) v1 claimed injective at -1, the rotations; in (iv) z = 0, and the range claimed 0 < z < 5;
in (v) the factor k!/(k - i)! dropped; in (vi) -l + 1's first step claimed obstructed. []

*Deduced.*

 (a) ([Hin26] Proposition 6.18 (4)-(7) in five dimensions, on Tangherlini) Take 0 < z < 4 and his Lemma 6.13 in five
     dimensions (10.29(a), on the readings of 10.20). His proof runs with the classes of (ii) and his ranges. For a
     class root mu with indicial solution omega-bar, box^Ups(0) omega' = -(box^Ups(0) - box-bar^Ups(0)) omega-bar is in
     rho^(mu + 4) C^oo by Proposition 10.25(i), so omega' is in A^((mu + 2, 0) u (mu + 2 + E_ind)) by his Lemmas 2.15
     and 6.13, mu + 2 being no root of the type by (iv) -- one order faster than his A^((lam, 0) u (1 + E_ind)), lam =
     mu + 1. The symmetric gradient's leading term is delta-bar* omega-bar at rho^(mu + 1), nonzero by (iii), the rest
     at rho^(mu + 3) (delta*_g - delta*_gbar in rho^3 Diff^0_b, Proposition 10.25(i)); mu + 1 is a root of L-hat(0) by
     Proposition 10.21(ii)'s factor det N_Ups(lam - 1), and where it is simple (10.24(iv), at one parameter point, l <=
     12) that leading term spans ker N(L-bar(0), mu + 1). The generalized states: in A0 omega-breve^k = -A1
     omega-breve^(k-1) - A2 omega-breve^(k-2) the leading terms are (v)'s. His A0 = box-hat(0) in rho^2 Diff^2_b, A1 in
     rho Diff^1_b and A2 = -g^00 in rho^2 C^oo (p. 132, from (6.4a)) hold in five dimensions by 10.18(b), [Hin26] Lemma
     6.1(1) there; Tangherlini's A0 differs from Minkowski's in rho^4 Diff^2_b (Proposition 10.25(i)), its A1 in rho^3
     Diff^1_b (S_E - S-bar in rho^2 C^oo, 10.18(b), and Q in rho^3 Diff^1_b), and A2, zero on Minkowski, is in rho^2
     C^oo: each contributes two orders above the leading equation at rho^(mu - k + 2). So the leading terms are solvable
     without logarithm, mu - k being no root of the type by (iv). The corrections, two orders faster, can meet roots --
     omega-breve^2's at rho^mu, the class root itself (in four dimensions omega-breve^1's, one order faster), and at s0
     mu_s0 + 4 = 1 - mu_s0 at z = 7/4, above the gap -- and with the rest, by his Lemma 6.13, they lie in E_ind; so his
     index sets hold as stated, and the constant coefficients k! h-breve^k lie in A^((mu + 1 - k, 0) u (mu + 1 - k +
     E_ind)) by (6.44).
 (b) (what five dimensions changes) The four classes and their ranges are his. The tensor types of L-hat(0), which four
     dimensions lacks, carry no pure gauge state, 1-forms having no tensor type: their roots -l and l + 2 (10.24(ii))
     fall, at l = 2, 3, with his section 8.5's physical states. At e_U = 0 the coincidences of (iv) occur and logarithms
     can enter the sl states: on Minkowski (vi) forces one at mu_l,0's first recursion step and none at -l + 1's first
     two steps, the second's obstruction removed by the first's kernel freedom; whether mu_l,1's stationary correction
     forces one (in four dimensions also s0's and both sl corrections) needs Tangherlini's sources at e_U = 0 and is not
     computed. e_U > 0 removes them all, as his p. 81 says.
 (c) (every l) N(delta-bar*(0), lam) is injective at sl and vl for every l >= 2 and every lam: delta-bar*(0) being
     homogeneous, a kernel element gives a stationary Killing 1-form rho^lam omega-bar of Minkowski space, and those --
     dt, the translations and the rotations -- have l <= 1, in five dimensions as in four (his remark after (2.46c), p.
     67). (iii) computes l <= 5 and l <= 4, which every class needs.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23; quotations transliterated to ASCII): pp. 19 ((1.27)-(1.29)),
67 ((2.43)-(2.46c), and: "Note that for all other pure types . = sl, vl (l >= 2) and for all lambda in C, the operator
N.(delta*(0), lambda) is injective"), 113 (Lemma 6.1, (6.4a)-(6.6)), 117-118 (Lemma 6.6 and its proof, (6.17a)-(6.17b),
Remark 6.7), 121 (Proposition 6.12), 128-134 (section 6.5.2: Proposition 6.18 (4)-(7), footnotes 74-76, Remark 6.19, the
proof of parts (4)-(7)), 149-151 (Lemma 8.4 and its proof), 158 (section 8.5, Proposition 8.14).

*What this gives, and what it does not.* All seven parts of his Proposition 6.18 now have five-dimensional counterparts
with their leading terms computed exactly on Minkowski: the four classes without symmetry carry over with his ranges,
each stationary correction one order faster, no logarithm in the leading terms at e_U > 0, and the vector type's
coefficients in closed form. Not done, and OPEN: the readings of 10.20 line by line; the index sets E_ind; whether five
dimensions needs his window [-3, 0], which is his choice for the decay he proves; section 7.2's dual states (10.31); his
Proposition 8.11, Lemma 8.12's pairings and Corollary 8.13 in five dimensions (10.32); section 8.5 (the physical states,
s2, v2, s3 and v3, and in five dimensions t2 and t3) and sections 9-10; how small gam_Ups must be, and h_0. Nothing of
this section is proved: Proposition 10.27 is computed, and (a)-(c) are deduced.

### 10.31 [Hin26] section 7.2 in five dimensions: the constraint operator's dual states (`dual5.py` A1-A3; D86)

*The setting.* [Hin26] section 7.2 records the large zero energy states of the adjoint of the constraint propagation
operator box^C = 2 delta G delta*_(g, E^C), "whose trace-reversed symmetric gradients will be shown to span the cokernel
of the linearized gauge-fixed Einstein operator in §8.4" (p. 135). Lemma 7.2 is "a dual statement of (7.7)" (p. 137):
with an unweighted b-density and adjoints for the spatial volume density, "for all alpha in (0, C_0 + 1] and s <= C_0 +
1" the adjoint's zero energy operator is invertible, and "The indicial roots of box^C(0)* are equal to 1 - conj(lambda)
where lambda runs over the indicial roots of box^C(0)" ((7.10), pp. 137-138). Since (box^C)* = 2 (delta*_(g, E^C))* G
delta* ((7.11)), "Killing 1-forms on Minkowski space will give rise to large zero energy states of (box^C)*, and their
trace-reversed symmetric gradients decay as r -> infinity" (p. 138): Proposition 7.3 builds them from the time
translation, the translations and the rotations, h*_s0 in H-dot_b^(0, C_0 + 2) and h*_s1, h*_v1 with a rho^2 leading term
((7.15)), h*_v1 rapidly decaying when V is a multiple of V(a) ((7.14), (7.16)). Section 7.2.1 resolves the v1 states near
a = 0: by Lemma 7.5, delta*_(g_b) V_b = rho^2 (-2m (dt* + dr) (x)_s rho V(S')) + ... ((7.20), S' = S(a(b) x a(V))), the
correction omega_0 = -2 m gam^C/(1 + 2 v_C gam^C) rho V' ((7.31)) from N_v1(rho^-2 box*(0), 1) = 2 + 4 gam^C v_C (p.
143), and the rho^2 leading term (7.18) of h*-sharp depends on V only through a(b) x a(V). In five dimensions box^C's
indicial roots are Proposition 10.9's, the invertibility of its zero energy operator 10.21(e)'s, and all six rotations
are Killing on Tangherlini (10.28).

**Proposition 10.28 (computed; exact).** With box^C at the trace weight 2/3 (m = 2/(D - 2)), c = r^-1 (dt - v dr) and h =
1/gam_C (10.12), its formal adjoint 2 (delta + C*) G delta*, C* k = h^-1 (2 iota_(g^-1 c) k - m (1 - e) c tr k), on 4+1
Minkowski and Tangherlini, f = 1 - mu/r^2, and on the one-spin Myers-Perry metric at first order in its rotation, g_T - a
h_A (Proposition 10.25(vi)), in his splitting (2.37b), (2.43):

 (i) (the adjoint's indicial roots) For s0, sl (l <= 3) and vl (l <= 3), det N*(lam) = det N(2 - lam), N the indicial
     family of box^C, whose polynomials are 10.12's at kappa = l (l + 2) times h^-2 (s0), h^-3 (sl) and h^-1 (vl); in
     four dimensions det N(1 - lam), his (7.10). So for these types the adjoint's roots are 2 - conj(lam); at v1 box^C's
     are 3 and -1 - 2 v gam_C and the adjoint's -1 and 3 + 2 v gam_C (four dimensions 2 and -1 - 2 v gam_C, his (7.8)),
     and N*_v1(2) = 3 + 6 gam_C v_C (four dimensions N*_v1(1) = 2 + 4 gam_C v_C, his p. 143) (A1).
 (ii) (the translations) On Tangherlini, with dx = d(r S), S = cos chi, box^C*(dx) vanishes to order rho^3 with a nonzero
     rho^4 term (four dimensions rho^3, his p. 139); the correction rho^2 (a S d xbar^0 + b S d xbar^1 + c r dS)
     cancelling it is unique, 2 being no root of the adjoint's s1 polynomial (four dimensions rho^1); and h*_s1 = G
     delta*(dx + omega') vanishes to order rho^2 with a nonzero rho^3 term (four dimensions rho^2, his (7.15)) (A2).
 (iii) (the rotations near a = 0) At first order in a, with V a rotation 1-form and V_a = g_a gbar^-1 V, delta*_(g_a) V_a
     = (a/2) L_R k = -(mu/r^4) a dt (x)_s V' on Myers-Perry, k = -h_A, V' = L_R w the rotation 1-form of the bracket of
     V's plane with the spin plane 12 (four dimensions, Kerr: -(2M/r^3) a dt (x)_s V', his (7.20)'s -2 m rho^2 (dt* + dr)
     (x)_s rho V(S')). V' = 0 for the planes 12 and 34, so two of the six rotations stay Killing at this order (four
     dimensions one of three, the spin axis's). For the planes 13, 14, 23 and 24 the correction omega_0 = c_0 r^-3 V'
     (four dimensions r^-2 V') is unique, c_0 = -2 mu/(3 (h + 2v)) (four dimensions -2M/(h + 2v), his (7.31)), and the
     leading term of h-sharp, at rho^3 (four dimensions rho^2), is that of delta*_(g_a) V_a times (h + 2v - 2)/(h + 2v)
     on d xbar^0 and (h + 2v + 2)/(h + 2v) on d xbar^1, in five dimensions as in four -- his (7.18) (A3).

*Proof.* A1-A3 of dual5.py, exact. box^C and its adjoint are applied in polar coordinates to rho^lam times each basis
1-form of 10.30 (the zonal harmonic at sl, the vector harmonic at vl), read at r = 1 and two generic angles, which agree
(pure type), the angular components in the orthonormal frame; the sources and corrections by their series in rho, the
correction's coefficients solved at one generic angle and checked at a second; on Myers-Perry with d_a g = -h_A
(Proposition 10.25(vi)) and V' in Cartesian components. Controls: in (i) the shift 1 claimed in five dimensions; in (ii)
the four-dimensional order rho^2 claimed in five dimensions; in (iii) his c_0 = -2 mu/(h + 2v) claimed in five
dimensions. []

*Deduced.*

 (a) ([Hin26] Lemma 7.2 in five dimensions) Part (1): with an unweighted b-density and adjoints for the spatial volume
     density, the adjoint's zero energy operator is invertible from H-dot_b^(s, alpha) to H-dot_b^(s - 1, alpha + 2) for
     alpha in (0, C_0 + 2] and s <= C_0 + 1, by duality from 10.21(e): there the weights are l in [-C_0 - 2, 0) for the
     Euclidean density r^3 |dr dg/|, the dual weight is -l - 2, and the b-density shifts it by n/2 = 2 where his shifts
     by 3/2, his (0, C_0 + 1]. It rests on what 10.21(e) rests on: the one point h = 10^-6 of Proposition 10.9, C_0 <=
     100, and 10^-6 below the uncertified five-dimensional h_0 of [Hin26a] Theorem 5.2 (10.22, on a reading). Part (2):
     his (7.10) with the density rho^-4 in place of rho^-3 gives N(rho^-2 box, lam)* = N(rho^-2 box*, 2 - conj(lam)), as
     (i) computes; with Proposition 10.9's roots -- none with real part in [-100, 19/10], and in [-100, 2] only lam = 2
     at l = 0, 1 -- the adjoint's roots are 0 (s0 or s1), have negative real part, or have real part > C_0 + 2.
 (b) ([Hin26] Proposition 7.3 in five dimensions, on Tangherlini) His proof runs with (a). The time translation's state
     is his, h*_s0 in H-dot_b^(0, C_0 + 3). For the four translations f_b is in rho^4 C^oo by (ii), so the correction is
     in H-dot_b^(1, ((2,0), C_0 + 2)), 2 being no root of the adjoint by (a), and h*_s1 in H-dot_b^(0, ((3,0), C_0 + 3)),
     its rho^3 leading term nonzero by (ii): one order faster than his (7.15). The six rotations are Killing on
     Tangherlini (10.28, Z4), so his (7.14) holds for every V and h*_v1 is in H-dot_b^(0, C_0 + 3). At a = 0, then, the
     time translation's and the six rotations' h* decay rapidly and the four translations' begin at rho^3: 1 + 4 + 6 = 11
     dual states against his 1 + 3 + 3 = 7.
 (c) ([Hin26] section 7.2.1 at first order in the rotation) On one-spin Myers-Perry, at first order in a, his Proposition
     7.4's structure holds by (iii): the leading term of h*_v1(V), at rho^3, depends on V only through V', the bracket of
     V's plane with the spin plane, and is his (7.18) with m -> mu/2 and rho^2 -> rho^3, the leading term of delta*_(g_a)
     V_a being -mu rho^3 (dt* + dr) (x)_s rho (a V') where his is -2m rho^2 (dt* + dr) (x)_s rho V(S'). The rotations in
     the planes 12 and 34 stay Killing at this order, and on the full metric for every a, d_phi and d_psi being Killing
     there (Proposition 10.25(vi), Z6: its coefficients functions of r and theta); the other four are not Killing at
     first order. So the space of V for which (7.16) holds falls from six at a = 0 to two for small a != 0 (four
     dimensions three to one): his discontinuity at a = 0 (p. 140), of four dimensions in five where his is of two. The
     higher orders in a, Lemma 7.5 on the full metric, and his (7.19) are not computed.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-23; quotations transliterated to ASCII): pp. 126 ((6.30)-(6.32),
Remarks 6.16-6.17), 134-137 (section 7: (7.1)-(7.8), Theorem 7.1 and its proof), 137-139 (section 7.2: Lemma 7.2 and its
proof, (7.9)-(7.11), Proposition 7.3 and its proof, (7.12)-(7.15)), 140-144 (section 7.2.1: (7.16), Proposition 7.4,
(7.17)-(7.19), Lemma 7.5 and its proof, (7.20)-(7.28), the proof of Proposition 7.4, (7.29)-(7.35)).

*What this gives, and what it does not.* His section 7.2 has a five-dimensional counterpart: Lemma 7.2 on what 10.21(e)
rests on, Proposition 7.3 on Tangherlini with eleven dual states, the translations' one order faster, and section
7.2.1's structure at first order in the rotation, two of the six rotations Killing there. Not done, and OPEN: the higher
orders in a, Lemma 7.5 and (7.19) on the full Myers-Perry metric (10.36: Lemma 7.5 at every spin computed; Proposition
7.4 and (7.19) deduced on readings); his Proposition 8.11, Lemma 8.12's pairings and Corollary 8.13 in five dimensions,
where these dual states enter (10.32); section 8.5 and sections 9-10; the readings of 10.20-10.22 line by line; how
small gam_Ups must be, and h_0. Nothing of this section is proved: Proposition 10.28 is computed, and (a)-(c) are
deduced.

### 10.32 [Hin26] Lemma 8.12 and Proposition 8.11 in five dimensions: the zero energy pairings (`pairing5.py`; D88, D89)

*The setting.* [Hin26] Proposition 8.11 (pp. 155-156) gives L-hat_b(0) index 0 on the weights (0, eps_ind) and counts
both sides: "(1) (Kernel.) The nullspace of (8.22) is 7-dimensional", spanned by the gauged linearized Kerr metrics
g-dot^Ups_b(b-dot) and the translations' deformation tensors h_b,s1(S); "(2) (Cokernel.)" the kernel of the adjoint "is
the 7-dimensional space spanned by" the dual states h*_b,s0, h*_b,s1(S), h*_b,v1(V) of his section 7.2. The kernel bound
uses [AHW24] Theorem 6.1(2), and both counts use the pairings of his Lemma 8.12 (p. 157), whose proof is that "The proof
of [Hin24b, Lemma 3.17] applies verbatim." That proof removes the gauge terms by integration by parts -- "We may thus
replace L by 2D Ric" ([Hin24b] p. 52) -- and cites [Hin23b] Theorem 9.6, whose proof rewrites "all pairings ... as
boundary pairings (i.e. L2-inner products only involving the leading order terms of various tensors at" infinity
([Hin23b] p. 106), the limits (9.22) of < [D-hat Ric(0), chi_eps] g'_b(b-dot), G (dt* (x)_s omega*) >, with the table -8
pi m-dot, -8 pi m (q . a-dot), 4 pi m (q . c) (p. 105). In five dimensions the kernel's candidates are the mass, the six
angular momenta of so(4) and the four translations (10.28-10.29), and the dual states eleven (10.31).

**Proposition 10.29 (computed; exact).** On n + 1 Minkowski (n = 3, 4) in Cartesian coordinates, with D Ric, G and the
fiber inner product of eta, the boundary pairings of [Hin23b] (9.22), and of its proof of Theorem 9.6(4) for the centres
of mass, on the leading terms -- the mass perturbation mu-dot R^-(n-2) (dt^2 + dr^2), the rotation -(2 mu/R^n) dt (x)_s
w_A (w_A = x^i dx^j - x^j dx^i on the plane ij; d_a g = -h_A, Proposition 10.25(vi)), and h_b,c, h-breve_b,c at first
order in mu -- against G (dt (x)_s omega*), omega* = dt, the rotations w_B and the translations dx^j:

 (i) (four dimensions) His table, with mu = 2m: -4 pi mu-dot = -8 pi m-dot; -4 pi mu per plane = -8 pi m (q . a-dot); 2
     pi mu (q . c) = 4 pi m (q . c); every other entry 0, except the mass and the centres of mass against the rotations,
     which lie above the critical weight, where the leading terms do not determine them (his values there -8 pi (q . a)
     m-dot, from subleading terms, and 0; both 0 at a = 0) (P1).
 (ii) (five dimensions, the Kerr rows) Mass against dt -3 pi^2 mu-dot, against the translations 0, against the rotations
     undetermined, above the critical weight; a rotation -2 pi^2 mu against its own plane, 0 against the other planes,
     dt and the translations (P2).
 (iii) (five dimensions, the centres of mass) (3 pi^2/2) mu (q . c) against q . dx, 0 against dt, undetermined against
     the six rotations, above the critical weight; h-breve_b,c is O(mu), its Minkowski part zero, the boost being
     Killing (P3).
 (iv) (non-degeneracy) With the undetermined entries (the mass and the centres of mass against the rotations) as
     unknowns, the 11 x 11 matrix -- rows mass, rotations, centres of mass; columns dt, rotations, translations -- is
     block triangular with determinant (-3 pi^2) (-2 pi^2 mu)^6 (3 pi^2 mu/2)^4, nonzero for mu != 0 whatever the
     unknowns; four dimensions (-4 pi) (-4 pi mu)^3 (2 pi mu)^3 (P4).
 (v) (invariance) The Kerr-Schild mass perturbation mu-dot R^-(n-2) (dt + dr)^2, a pure gauge tensor delta*(dG), G = R
     (four dimensions) or log R (five), whose cut-off source is not zero and whose pairing with dt is -I_A + I_B with
     I_A = I_B = -4 pi or -3 pi^2, a cancellation, and t* = t - r in place of t leave the Kerr rows unchanged, his
     Theorem 9.6(1) and (7) (P5).

*Proof.* P1-P5 of pairing5.py, exact. Each pairing is < [P, chi] u, v > with chi a radial cutoff, 1 near 0 and 0 near
infinity: the integrand is chi'(R) A + chi''(R) B with A and B homogeneous, the sphere integrals are exact, and each
entry is classified by its weight, read from the homogeneity of its two tensors, before it is computed: -I_A + I_B at
the critical weight (int chi' = -1, int R chi'' = 1), 0 below it, undetermined above it whether or not the leading terms
vanish pointwise there -- D88 classified only the entries with a nonzero leading integrand and returned 0 for the mass's
six and each centre of mass's other three entries against the rotations (four dimensions three and one), corrected in
D89; a nonzero sphere integral above it would be a divergence, and none occurs. P5's pure gauge tensor has a nonzero
cut-off source: for delta*(f(R) alpha), alpha constant -- D88's delta*(log R dt) among them -- chi times it is pure
gauge again, the source 0 and the check empty (D89); and D89's delta*(x_2 R^-(n-2) dx_1) paired 0 by reflection parity
alone -- against dt both sphere integrals vanish, the tensor being odd under x_1 -> -x_1, and against the translations
the integrand is 0 -- as the non-gauge x_1 x_2 R^-n (dt^2 + dR^2) does, so that check could not fail either; delta*(dG)
replaces it (the forty-second verifier; D92). Controls: in (i) G dropped from the dual slot; in (ii) the mass
perturbation's dr^2 term dropped; in (iii) h-breve_b,c dropped; in (iv) the translations' first-order pairing < D Ric(t
h_b,c), h* >, which [Hin23b] Theorem 9.6(6) says vanishes, in place of the centre of mass; in (v) a non-gauge R^-(n-2)
dx_1^2 added to the mass, and the non-gauge R^-(n-2) |dx|^2 in place of delta*(dG), which pairs -4 pi and -6 pi^2 with
dt. []

*Deduced.*

 (a) (the values) In both dimensions the entries are -8 pi M-dot, -8 pi J-dot (the component on the rotation's plane) and
     4 pi M (q . c), M and J the ADM mass and angular momentum in the normalization g_tt = -1 + 16 pi M/((n - 1)
     Omega_(n-1) r^(n-2)), g_t phi = -8 pi J sin^2 theta/(Omega_(n-1) r^(n-2)): M = 3 pi mu/8 and J = pi mu a/4 in five
     dimensions, M = mu/2 and J = M a in four.
 (b) ([Hin26] Lemma 8.12 in five dimensions, at a = 0) His reduction -- the gauge terms and the gauge corrections removed
     by integration by parts, the dual states vanishing inside the horizon and decaying at infinity, faster in five
     dimensions (10.31(b)), and the pairings rewritten as [Hin23b]'s boundary pairings -- uses only integration by parts
     and decay, so his Lemma 8.12 for his L_b of (8.1) has (ii)-(iii)'s values in five dimensions at a = 0. The
     undetermined entries are 0 there: the mass's by SO(4) symmetry -- at a = 0 the pairing is SO(4)-equivariant, the
     mass state invariant, and the rotation duals span so(4), which has no invariant vector; the centres of mass's by
     his argument for Theorem 9.6(5): by its part (1) omega* may be the cut-off Killing form, the rotations being
     Killing on Tangherlini, so h* is compactly supported and the centre of mass's pairing < D-hat Ric(0) h-ring, h* >
     vanishes by integration by parts; (c) does not need them. His printed values, -16 pi m-dot and so on, are
     [Hin24b]'s, whose L ((3.1a), p. 33) is 2 (D Ric + delta* delta G), twice his L_b of (8.1) (p. 145); for L_b they
     halve. And the s0 entries change sign with the s0 dual state's normalization: [Hin23b]'s is dt (Definition 9.2),
     his omega-bar_s0 = g-bar(d_t*, .) = -dt ((6.29), p. 125; (7.12), p. 138; [Hin24b] Lemma 3.11(2), p. 44, omega*_s0 -
     chi d_t^flat), so with his dual state the mass entry is +8 pi m-dot for L_b, +3 pi^2 mu-dot in five dimensions,
     where he prints -16 pi m-dot with [Hin23b]'s sign (the forty-first verifier; D89). Neither the factor nor the sign
     changes any non-degeneracy. For b near Tangherlini's parameters the matrix stays non-degenerate by continuity.
 (c) ([Hin26] Proposition 8.11 in five dimensions) The eleven tensors g-dot^Ups(mu-dot), g-dot^Ups(0, A) (A in so(4)) and
     h_s1(S) (S in S_1) lie in ker L-hat(0) (10.28-10.29) and are independent: for u = g-dot^Ups(b-dot) + h_s1(S) = 0
     the pairings of [L, t*] u with the dual states see b-dot alone, h_s1(S) pairing to 0 with each ([Hin23b] Theorem
     9.6(6)), so b-dot = 0 by (b); and then S = 0, since h_s1(S) = 0 only if S = 0, d(rS) not being Killing for
     Tangherlini ([Hin26] p. 156); the eleven dual states lie in ker L-hat(0)* (10.31(b) and his (8.25)) and are
     independent by the same matrix. With his index 0 (his Propositions 8.3 and 8.6, deduced in 10.26 and 10.25, and
     [Hin26c] Corollary 9.43 at n = 4, 10.20(d)), dim ker = dim coker >= 11. Equality is his kernel argument, which runs
     as his with 10.21(e) for Theorem 7.1(2), 10.28 for Proposition 8.9, 10.15 for Lemma 6.6 and 10.20 for Proposition
     6.12, but needs [AHW24] Theorem 6.1(2) -- every decaying stationary solution of D Ric(h) = 0 a linearized Kerr
     metric plus a pure gauge term -- in five dimensions, for linearized Myers-Perry: 10.33 deduces it at a = 0, and
     with it this equality at Tangherlini, and near it on a reading (10.33(f)).
 (d) ([Hin26] Corollary 8.13 in five dimensions) With 11 for 7, on (c): his construction of the linear right inverse uses
     only the (co)kernel's dimension and the pairings.

*READ.* [Hin26] (alphaXiv, 2026-10-23; quotations transliterated to ASCII): pp. 125 ((6.29)), 138 ((7.12)), 145 ((8.1)),
154-158 (Proposition 8.9, Remark 8.10, Proposition 8.11 and its proof, (8.22)-(8.25), Lemma 8.12, (8.26), Corollary 8.13
and its proof); [Hin24b] (arXiv:2408.06715v1): pp. 13, 33 ((3.1a)), 38-39 (Lemma 3.8 and its proof), 44 (Lemma 3.11),
49-53 (Proposition 3.16 and its proof, Lemma 3.17 and its proof); [Hin23b] (arXiv:2306.07409v2): pp. 101-110 (Lemma 9.1,
Definition 9.2, Lemma 9.3, Theorem 9.6, Lemma 9.7, the proof of Theorem 9.6), 116-117.

*What this gives, and what it does not.* The non-degeneracy his zero energy analysis turns on holds in five dimensions:
the eleven kernel states and the eleven dual states pair through -8 pi times the ADM mass and angular momentum and 4 pi
M times the centre of mass, as in four, so his Lemma 8.12 carries over at and near Tangherlini, and his Proposition 8.11
and Corollary 8.13 up to the five-dimensional [AHW24] Theorem 6.1(2). Not done, and OPEN: that rigidity statement in
five dimensions beyond a = 0 (10.33 deduces it at a = 0); the a-dependent entries beyond continuity; his section 8.5
(Proposition 8.14, Lemma 8.15's pairings) and sections 9-10; section 7.2.1 beyond first order in the rotation (10.36:
Lemma 7.5 at every spin computed; Proposition 7.4 and (7.19) deduced on readings); the readings of 10.20-10.22 line by
line; how small gam_Ups must be, and h_0. Nothing of this section is proved: Proposition 10.29 is computed, and (a)-(d)
are deduced.

### 10.33 [AHW24] Theorem 6.1(2) in five dimensions: the stationary solutions on Tangherlini (`static5.py` S1-S6; D90)

*The setting.* [Hin26] Proposition 8.11's kernel bound (p. 156): "every element u of the nullspace of (8.22) lies in
A^(eps_ind - eps)(X; S^2 T*X) for all eps > 0"; then eta = 0 and D Ric(u) = 0, and "By [AHW24, Theorem 6.1(2)], with q =
eps_ind - 3/2 - eps for an arbitrarily small eps > 0 so that q in (-3/2, -1/2), there exist b-dot in R^4 and a
stationary 1-form omega in H-bar_b^(oo,q-1)(X; T*X) subset A^(-1+eps_ind-eps) such that u = g-dot_b(b-dot) +
delta*_(g_b) omega." [AHW24] (L. Andersson, D. Hafner, B. F. Whiting, arXiv:2207.12952v1) Theorem 6.1 (p. 35): "Let 0 <
a < m, sigma in C, Im sigma >= 0, and suppose g-dot = e^(-i sigma t*) h-tilde, h-tilde in H-bar_b^(oo,q)(X; S^2 ...), q
in (-3/2; -1/2) is an outgoing mode solution of the linearized Einstein equation D_(g_b) Ric(g-dot) = 0. Then there
exist parameters m-dot in R, a-dot in R^3, and an outgoing 1-form omega in H-bar_b^(oo,q-1)(X; ...), such that g-dot -
g-dot_(m,a)(m-dot, a-dot) = delta*_(g_b) omega." Their proof at sigma = 0 (section 6.4, p. 41) runs through the
Teukolsky scalars, which vanish (their Theorem 4.5), the gauge invariants of a type D perturbation and the completeness
of the invariants. 10.32(c) left the statement OPEN in five dimensions. On Tangherlini, static, [KI03]'s decomposition
reduces it harmonic by harmonic to ordinary differential equations in r -- their section 4 (p. 11) treats the static
scalar type itself, (4.1)-(4.3), and finds "the same master equation" -- and static5.py computes them at sigma = 0 from
D Ric itself, with gmodes5.py's reduced operators (Proposition 10.24) on coefficients independent of t.

**Proposition 10.30 (computed; exact).** On five-dimensional Tangherlini, f = 1 - mu/r^2, r_h = mu^(1/2), for h
stationary and decomposed by the harmonics of S^3 as in Proposition 10.24, F_t = r y at the vector type:

 (i) (tensor type, l >= 2) For h_ij = 2 r^2 H(r) T_ij: D Ric(h)_ab = D Ric(h)_ai = 0 and D Ric(h)_ij = -r^2 ((1/r^3)(r^3
     f H')' - l(l + 2) H/r^2) T_ij; Phi = r^(3/2) H solves f (f Phi')' = V_T Phi, V_T = (f/r^2)(l(l + 2) + 3/4 + 9 mu/(4
     r^2)), V_T/f positive and bounded on r >= r_h, the sign the identity (f Phi Phi')' = f Phi'^2 + V_T Phi^2/f on
     solutions, true for any f and V_T, needs; the exponents of H are l and -(l + 2) at infinity and 0, twice, at r_h
     (S1).
 (ii) (vector type, l >= 2) E_r = (k_V^2 - 2) F_r/(2 r^2), E_T = -k_V (r^2 f F_r)'/(2 r^3) and E_t = -(f (r^5 y')' -
     (k_V^2 - 2) r^3 y)/(2 r^4), k_V^2 - 2 = l(l + 2) - 3 >= 5, the sign the identity (r^5 y y')' = r^5 y'^2 + (k_V^2 -
     2) r^3 y^2/f on solutions needs; the exponents of f_t = r y are l and -(l + 2) at infinity; in ingoing coordinates
     (v, r, z), dt = dv - dr/f, h_vi = r f_t V_i and h_ri = r (f_r - f_t/f) V_i (S2).
 (iii) (scalar type, l >= 2) E_tr = k^2 F_tr/(2 r^2), F_tr entering no even equation, and E_T = -(k^2/(4 r^2))(f F_rr -
     F_tt/f + 2 F); in [KI03]'s X = r (-F_tt/f - 2 F), Y = r (f F_rr - 2 F), which solve E_T = 0, E_r and the
     combination of E_tt, E_rr and E_L free of second derivatives give the flow Y' = mu (X - Y)/(r (r^2 - mu)) ([KI03]
     (2.24b) at sigma = 0) and X' = (mu (mu - 2 r^2) X + (k^2 r^2 (r^2 - mu) + 4 mu r^2 - 3 r^4) Y)/(mu r (r^2 - mu)),
     on which E_tt, E_rr, E_L and E_r vanish: [KI03]'s static system (4.2) at n = 3, identically; Z~ := (f r^2/k^2)(X' -
     X/r - (f'/f - 2/r) Y), [KI03] (2.24a) at sigma = 0 read as its definition, has Z~' = X ((2.24c)); Phi := (3 Z~ - r
     (X + Y))/(r^(1/2) H), H = k^2 - 3 + 6 mu/r^2, solves f (f Phi')' = V_S Phi with Proposition 10.24(iii)'s V_S, is
     [KI03]'s static master variable (4.3), (Q_Y X - Q_X Y)/(2 k^2 r^(1/2) f' H), identically (the forty-second
     verifier; D92), and det[r^(1/2) Phi; r^(1/2) Phi'] = r^3/(k^2 mu); 3 Z~ - r (X + Y) = (-mu (k^2 r^2 + 9 r^2 - 6 mu)
     X + (3 (k^2 - 3) r^4 - 2 (2 k^2 - 9) mu r^2 - 12 mu^2) Y)/(k^2 mu r); r^2 V_S -> l(l + 2) + 3/4 at infinity,
     exponents l + 3/2 and -l - 1/2; and where F_tr = 0, in ingoing components, F_vv = -f F_vr, X = r (F_vr - 2 F) and Y
     = r (f F_rr + F_vr - 2 F), F_rr there the ingoing component (S3).
 (iv) (scalar l = 0) delta*(A_t dt + A_r dr) shifts H_L by f A_r/(2 r) and f_tr by (f/2)(A_t/f)'; f_tr enters no
     stationary equation; at H_L = 0 the equations give F_tt'' = -3 F_tt'/r and F_rr algebraic in F_tt and F_tt', so the
     stationary solutions are spanned by (F_tt, F_rr) = (f, 0), the time rescaling, and (r^-2, r^-2 f^-2), the mass;
     r^-2 (dt + dr/f)^2 solves, and is r^-2 dv^2 in ingoing coordinates (S4).
 (v) (vector l = 1, V Killing) D Ric(h)_ab = 0, E_r = 0, D Ric(h)_ij = 0 and E_t = -f (r^5 y')'/(2 r^4), so f_t = a r +
     b r^-3 with f_r free; delta*(r^2 B V_i dz^i) shifts f_t by (r/2) d_t B and f_r by (r/2) B', so f_t = a r is
     delta*(2 a t r^2 V_i dz^i); f_t = r^-3, f_r = r^-3/f is r^-2 V_i dz^i dv in ingoing coordinates (S5).
 (vi) (scalar l = 1, D_i D_j S = -gamma_ij S) The stationary shifts of f_tt, f_t and H_L by A_t S dt + A_r S dr + r^2 B
     S_i dz^i are free of derivatives, with determinant -mu (r^2 - mu)/(4 r^6), and those of f_rr and f_r are A_r' + mu
     A_r/(r (r^2 - mu)) and (r^2 B' - 3^(1/2) A_r)/(2 r); at f_tt = f_t = H_L = 0 the stationary equations force f_tr =
     f_rr = f_r = 0 (S6).

*Proof.* S1-S6 of static5.py, exact, the harmonics at the point of 10.27; the exponents at infinity from the limit of
r^2 op(r^s)/r^s, at r_h from the Frobenius indicial polynomial; (iii)'s flow solves E_r and the second-derivative-free
combination for (X', Y'), whose determinant 18 k mu r^2 (r^2 - mu)^6 is nonzero on r > r_h, and E_tt, E_rr, E_L and E_r
then vanish with the flow's second derivatives substituted. Controls: in (i) Phi = r^(1/2) H; in (ii) l = 1, where E_r
vanishes identically; in (iii) Phi without 1/H; in (iv) (r^-2, 0) in place of the mass; in (v) the rotation with f_r =
0, singular at r_h; in (vi) f_t left free, where the rank is short. []

*Deduced.*

 (a) ([AHW24] Theorem 6.1(2) on five-dimensional Tangherlini) Let h be stationary on r >= r_h, smooth there in ingoing
     coordinates, conormal at infinity with every component in the frame (dt, dr, r dz) O(r^-eps) for some 0 < eps < 1,
     and D Ric(h) = 0. Then h = g-dot(mu-dot, A) + delta* omega with mu-dot real, A in so(4), g-dot(mu-dot, A) = mu-dot
     r^-2 dv^2 + 2 r^-2 dv (x)_s V_A, V_A the Killing 1-form of A on the unit S^3 written V_i dz^i, and omega
     stationary, smooth across the horizon and O(r^(1 - eps)), [AHW24]'s q - 1. Harmonic by harmonic, each component in
     the class and D Ric and delta* commuting with the decomposition, (b)-(e).
 (b) (tensor and vector types, l >= 2) Tensor: H = O(r^-eps) is smooth at r_h, and at infinity the exponent l > 0 is
     excluded, so H = O(r^(-l-2)); by (i) the boundary terms f Phi Phi' vanish at r_h (f = 0, Phi smooth) and at
     infinity (O(r^(-2l-2))), so the integral of f Phi'^2 + V_T Phi^2/f over (r_h, oo) is 0 and Phi = 0. Vector: B = -2
     H_T/k_V removes H_T, the 1-form r^2 B V_i dz^i O(r^(1-eps)); E_r forces F_r = 0, so f_r = -(r/k_V) H_T' is smooth
     at r_h, and with h_ri smooth in ingoing form so is f_t/f: y = f_t/r vanishes at r_h; at infinity y = O(r^(-l-3));
     (ii)'s identity gives y = 0, and h = delta*(r^2 B V_i dz^i).
 (c) (scalar type, l >= 2) [KI03]'s gauge 1-form -2 X_a S dy^a - (2 r^2/k) H_T S_i dz^i, built covariantly on the orbit
     space from h's coefficients, is stationary, smooth across the horizon and O(r^(1-eps)); E_tr forces F_tr = 0, so by
     Proposition 10.30(iii) X and Y are smooth at r_h, and O(r^(1-eps)) at infinity; Phi is smooth at r_h, H being at
     least k^2 - 3, positive, and O(r^(7/2-eps)) by the degrees 2 and 4 of its coefficients, which excludes the exponent
     l + 3/2 >= 7/2, so Phi = O(r^(-l-1/2)); the identity (f Phi Phi')' = f Phi'^2 + V_S Phi^2/f with V_S > 0
     (Proposition 10.24(v)) gives Phi = 0 as in (b), and the determinant X = Y = 0, so F_ab = F = 0 by (2.21) and h is
     delta* of the gauge 1-form.
 (d) (l = 0 and vector l = 1) Scalar l = 0: A_r = 2 r H_L/f and A_t = f int 2 f_tr/f dr, fixed up to c f dt, which is
     Killing, are O(r^(1-eps)) and leave (F_tt, F_rr) = c (f, 0) + mu-dot (r^-2, r^-2 f^-2), which decays only if c = 0;
     the Schwarzschild-form mass differs from mu-dot r^-2 dv^2 by f_tr = mu-dot/(r^2 f), itself delta*(A_t dt) with
     (A_t/f)' = 2 mu-dot/(r^2 f^2), A_t = O(r^-1). Vector l = 1: f_t = a r + b r^-3 with a = 0 by the decay, a r being
     the rigid rotation; f_r = (r/2) B' with B = int 2 f_r/r dr, up to a constant (the Killing r^2 V), O(r^-eps); b r^-3
     with f_r = b r^-3/f is 2 b r^-2 dv (x)_s V, regular, and the six Killing V make A.
 (e) (scalar l = 1; the sum and the horizon) By (vi) h = delta* omega with omega = A_t S dt + A_r S dr + r^2 B S_i dz^i,
     unique in the sector, which holds no Killing 1-form; A_t = -2 r f_t/3^(1/2) is O(r^(1-eps)); the f_rr row, (f^(1/2)
     A_r)' = f^(1/2) f_rr, gives A_r = O(r^(1-eps)) (eps < 1); and H_L's, B = (6 r^3 H_L - 3 (r^2 - mu) A_r)/(3^(1/2)
     r^3) = O(r^-eps). The gauge 1-forms' coefficients are bounded by polynomial multiples in l of h's coefficients and
     their derivatives, so the sum over the harmonics converges with h's, as in 10.27(a); and omega is smooth across the
     future horizon, since delta* omega = h - g-dot(mu-dot, A) is, and the r-row of delta* omega in ingoing coordinates
     is a linear ordinary differential equation in r with coefficients smooth there (Proposition 10.24(v)).
 (f) ([Hin26] Proposition 8.11 and Corollary 8.13 in five dimensions) At Tangherlini his kernel argument (10.32(c)) runs
     with (a) for [AHW24] Theorem 6.1(2): an element u of the nullspace of (8.22) is in A^(eps_ind - eps) by his normal
     operator argument on section 10.24's roots, so O(r^-(eps_ind - eps)) with 0 < eps_ind - eps < 1, and smooth across
     the horizon; (a) gives u = g-dot(mu-dot, A) + delta* omega with omega O(r^(1 - eps_ind + eps)), his
     A^(-1+eps_ind-eps); the rest is his, with 10.28 for Proposition 8.9, 10.15 for Lemma 6.6 and 10.20 for Proposition
     6.12: dim ker = 11, with his index 0 dim coker = 11, and his augmented operator is invertible at b_0 with 11 for 7
     (10.32(d)). His Corollary 8.13 is a statement for b near b_0, its proof taking the (co)kernel there as Proposition
     8.11 gives it (p. 157), so at b_0 alone it gives that invertibility only (the forty-second verifier; D92). Near
     Tangherlini dim ker <= 11 needs the kernel's dimension upper semicontinuous in b along (8.22), a property of the
     uniform Fredholm estimates his Corollary 8.13's proof invokes ([Vas13] section 2.7, [Hin26c] section 9.2.3; p.
     157), not read line by line here: on that reading dim ker = 11 near Tangherlini with 10.32(c)'s lower bound, and
     his Corollary 8.13 holds with 11 for 7.
 (g) (what the decay excludes) Without it, (iv)-(v) add the time rescaling f dt^2 = delta*(t f dt) and the rigid
     rotations, f_t = a r, delta*(2 a t r^2 V_i dz^i): pure gauge, but with 1-forms linear in t, which [AHW24]'s
     stationary omega excludes; and for l >= 2 the solution smooth at r_h has a nonzero growing part, H, f_t and Phi of
     order r^l, r^l and r^(l + 3/2) -- the static tidal fields, which are not pure gauge -- since by (b)-(c) none is
     both smooth there and decaying.

*READ.* [AHW24] (arXiv:2207.12952v1, alphaXiv, 2026-10-23 and 2026-10-24; quotations transliterated to ASCII): pp. 1
(the title and abstract), 35 (Theorem 6.1), 41 (section 6.4, the proof of Theorem 6.1); [Hin26]: pp. 156-157 (the proof
of Proposition 8.11, its kernel part; Corollary 8.13's proof), 2026-10-24; [KI03] as in 10.27, and p. 11 (section 4,
(4.1)-(4.3), and "the same master equation holds for both non-static and static perturbations"), alphaXiv, 2026-10-24.

*What this gives, and what it does not.* The rigidity his zero energy count takes from [AHW24], at Tangherlini: every
decaying stationary solution of the linearized Einstein equation that is smooth across the horizon is a linearized
Myers-Perry metric at zero rotation -- a mass and one of so(4)'s six rotations -- plus a pure gauge term, the gauge
1-form one power of r larger. Each harmonic type reduces to an ordinary differential equation in r; for l >= 2 the
energy identities of the master equations at zero frequency, with Proposition 10.24's potentials, leave nothing smooth
at the horizon and decaying, and l = 0 and 1 give the mass, the rotations and pure gauge. With it his Proposition 8.11
holds at Tangherlini with eleven for seven, and his augmented operator is invertible there; near Tangherlini, on a
reading, Proposition 8.11 and his Corollary 8.13. Not done, and OPEN: [AHW24] Theorem 6.1(2) on Myers-Perry with a != 0
beyond that reading; the class of (8.22)'s kernel elements and their smoothness across the horizon in five dimensions
line by line; omega's continuation inside the horizon, as in 10.27(b) (deduced at proof level in 10.76; D149); his
section 8.5 beyond
10.34 (Proposition 8.14, Lemma 8.15) and sections 9-10; section 7.2.1 beyond first order in the rotation (10.36: Lemma
7.5 at every spin computed; Proposition 7.4 and (7.19) deduced on readings); the readings of 10.20-10.22 line by line;
how small gam_Ups must be, and h_0. Nothing of this section is proved: Proposition 10.30 is computed, and (a)-(g) are
deduced.

### 10.34 [Hin26] section 8.5 in five dimensions: the physical large zero energy states (`physical5.py` Y1-Y4; D91)

*The setting.* [Hin26] section 8.5 (p. 158): "Consider the indicial roots lambda of L-hat_b(0) in Lemma 8.4 with Re
lambda in [-3, 0] ... For most of them, Proposition 6.18 produces corresponding large zero energy states ... The only
exceptional indicial roots are the sl and vl roots -l for l >= 2. They are not related to pure gauge states; we shall
instead construct them using properties of L_b directly." His Proposition 8.14 (p. 158): for b near b_0, states
h^(-2)_b,s2(S), h^(-2)_b,v2(V) in A^((-2,0) u (-2+E_ind)) with generalized companions h-breve^(-2),1 in A^((-3,0) u
(-3+E_ind)), and h^(-3)_b,s3(S), h^(-3)_b,v3(V), all "in ker D_(g_b) Ric cap ker delta_(g_b,E^Ups) G_(g_b)", their
leading terms "comprising the spaces N_s2(L-bar(0), -2) and N_v2(L-bar(0), -2)", and the same at -3; his Lemma 8.15 (pp.
158-159): (1) <L-hat_b(0) h-breve^2_b,s1(S), h*> = 0 for h*_b,s0 and h*_b,v1, and S -> <L-hat_b(0) h-breve^2_b,s1(S),
h*_b,s1(.)> an isomorphism;
(2) <L-hat_b(0) h-breve^1_b,v1(V), h*> = 0 for h*_b,s0 and h*_b,s1, and "= -8 pi m <a(V), a(b) x a(V')>" ((8.29)),
proved from his Remark 8.10, "g-dot_(m,a)(0, v x a) = -L_R g_(m,a) = -2 delta* V_b(v)", with (8.21) and Lemma 8.12. His
proof of Proposition 8.14 (pp. 160-163): a formal solution (Step 1), the obstruction pairings with the dual states
removed by adding h-breve^2_b,s1(S_1) + h-breve^1_b,v1(V_1) through Lemma 8.15 -- smoothly in b although the cokernel's
relevant part jumps at a = 0, by his functional lambda-sharp on all of R^3 ((8.33)) (Step 2) -- Corollary 8.13(2) (Step
3), the generalized state through (8.37) and Lemma 8.12, using that "-3 is not an s2 root" (Step 4), and the gauge by
Theorem 7.1(2) (Step 5). In five dimensions section 10.24 found the physical roots -l and l + 2 at every type, the
tensor type included, which four dimensions lacks (10.30(b)), and 10.33 the stationary solutions on Tangherlini.

**Proposition 10.31 (computed; exact, and numerical where said).** On five-dimensional Tangherlini, z = r^2/mu, with
10.33's reduced fields -- H at the tensor type, y = F_t/r at the vector type, [KI03]'s Y at the scalar type -- and F the
Gauss function 2F1:

 (i) (the equations) 10.33's stationary equations are hypergeometric in z, z (1 - z) w'' + (c - (a + b + 1) z) w' - a b
     w = 0: for H with (a, b, c) = (-l/2, 1 + l/2, 1), for y with ((1 - l)/2, (l + 3)/2, 3), and for Y = z^(1/2) (z -
     1)^-1 w with (-l/2, 1 + l/2, 2), l symbolic (Y1).
 (ii) (the solutions smooth at the horizon) H_l = F(-l/2, 1 + l/2; 1; 1-z), y_l = (1-z) F((l + 5)/2, (3 - l)/2; 2; 1-z)
     and Y_l = z^(1/2) F(2 + l/2, 1 - l/2; 2; 1-z) solve them; for l = 2, ..., 8 the terminating ones (H at even l, y at
     odd l, Y at even l) do so exactly, their F factors polynomials of degrees l/2, (l - 3)/2 and l/2 - 1 in z, and
     every one at 40 digits at three radii; at infinity they grow as Gamma(l + 1)/Gamma(1 + l/2)^2 z^(l/2), -Gamma(l +
     1)/(Gamma((l + 5)/2) Gamma((l + 1)/2)) z^((l - 1)/2) and Gamma(l + 1)/(Gamma(2 + l/2) Gamma(1 + l/2)) z^((l -
     1)/2), coefficients that are never 0, matched at z = 10^12 (Y2).
 (iii) (the roots his Step 4 needs) At sl, vl and tl, l = 2, 3, at Proposition 10.9's point, -l is a simple root of det
     N_L and -l - 1 is none, its nearest root at distance 1 (at sl less the class root's distance below -l); the nearest
     other root to -l at sl is box^Ups's class root mu_l,1 + 1 = -l - (l + 2) z/(2 (l + 1)(2l + 3)) + O(z^2)
     (Proposition 10.27(ii)), z = 4 e_U gam_U^2 = 4 x 10^-6, real and below -l by 3.81 x 10^-7 (l = 2) and 2.78 x 10^-7
     (l = 3), its first-order term matched to 10^-3 (Y3; D91 printed 3.3 x 10^-7, section 10.24's s1 pair, D92); the two
     meet at z = 0 (Proposition 10.27(iv)).
 (iv) (the rotation equivariance) On 4+1 Minkowski, with h_A = (mu/R^4)(dt (x) w_A + w_A (x) dt), w_A = x . A dx
     (10.28), L_R h_A = h_[A,B] for R = B x and every pair of the six basis rotations; B(V, V') := <[A_V, A_b], A_V'> at
     A_b = e_12 is antisymmetric of rank 4 with kernel spanned by e_12 and e_34, the trace form is ad-invariant, and in
     three dimensions B is his triple product up to sign (Y4).

*Proof.* Y1-Y4 of physical5.py: (i) symbolic in l; (ii) exact by hyperexpand where the series terminates, and by mpmath
at 40 digits (the operators on the functions at r = 1.3, 2.1, 5.7, mu = 1, and the growth at z = 10^12 against the
coefficients of [DLMF] (15.8.2), which in the case b - a = m an integer, (15.8.8), for m >= 1 -- here m = l + 1 -- keeps
the dominant term's coefficient Gamma(c) Gamma(m)/(Gamma(b) Gamma(c - a))); (iii) lin5.py's factors of Proposition
10.21(ii) at 50 digits; (iv) exact. Controls: in (i) c = 2 at the tensor type; in (ii) the tensor solution with c = 2;
in (iii) -l in place of -l - 1; in (iv) h_[B,A] for h_[A,B]. []

*Deduced.*

 (a) (the states at Tangherlini, every l >= 2) At a = 0, for each l >= 2 and each of the three types, the stationary
     solution of D Ric = 0 smooth across the horizon is unique up to scale and pure gauge -- 10.33(b)-(c)'s reduction
     leaves H, y or Y, and of the two Frobenius solutions at z = 1 (exponents 0 twice for H, 0 and 1 for y with y(r_h) =
     0 forced, 0 and -1 for Y) one is smooth -- and by (ii) it grows like r^l in the frame (dt, dr, r dz), its
     coefficient never 0 (H, f_t = r y and F = -(X + Y)/(6 r), X = Y + r (r^2 - mu) Y'/mu, all of order r^l). Put into
     the gauge by a stationary 1-form, as his section 1.4.1 does ("upon adding to h a pure gauge term delta*_(g_b) omega
     ... we can arrange that also the linearized gauge condition ... holds"), it is the large zero energy state of his
     Proposition 8.14 at the root -l, its leading term spanning that type's part of ker N(L-bar(0), -l) where -l is
     simple -- computed for l <= 12 at the point (section 10.24) and l = 2, 3 in (iii): his s2, v2, s3, v3, and the
     tensor types t2, t3 that four dimensions lacks, and every higher l so far as -l is simple (the forty-third
     verifier; D94). At a = 0 no obstruction arises in his Step 2: L-hat(0) and the dual states are SO(4)-covariant, and
     a type-l tensor, l >= 2, pairs to 0 with the dual states of types s0, s1 and v1.
 (b) ([Hin26] Lemma 8.15 in five dimensions) (1) His proof -- L h^(<=2)_b,s1 = 0 gives L-hat(0) h-breve^2_b,s1 = -(1/2)
     [[L, t*], t*] h_b,s1 - [L, t*] h-breve^1_b,s1 -- makes the s1 pairings minus section 10.32's centre-of-mass row:
     against h*_s0 0, against h*_s1 the isomorphism S(c) -> -(3 pi^2/2) mu (q . c) at a = 0 (Proposition 10.29(iii)),
     and so near it; against h*_v1 0 at a = 0 (10.32(b)), and near it 0 on the rotations that stay Killing (12 and 34
     for one spin), his Theorem 9.6(5) argument applying to them, but not established on the others. His Step 2 uses the
     vanishing against every h*_v1 ("By Lemma 8.15, the left-hand side of (8.34) is independent of the choice of V_1 ...
     Similarly, the left-hand side of (8.35) is independent of S_1", p. 161); a modification of it serves instead: by
     the five-dimensional Proposition 7.4, as his (8.32c)-(8.33) give lambda_v1, the pairings P(S_1, V') := <L-hat(0)
     h-breve^2_s1(S_1), h*_v1(V')> depend on V' only through [A_b, A_V'], P = <p_b(S_1), [A_b, A_V']>, and are absorbed
     into V_1 in (2) (the forty-third verifier; D94). (2) His Remark 8.10 holds in five dimensions: rotating the
     parameter, g_(mu, A(s)) = (e^(-sR))* g_(mu,A) with A(s) = e^(s ad B) A, so g-dot(0, [B, A]) = -L_R g = -2 delta*
     V_b, as (iv) has it at first order in the rotation (L_R h_A = h_[A,B] and d_a g = -h_A, Proposition 10.25(vi));
     with Proposition 10.29(ii)'s rotation row, his computation gives <L-hat(0) h-breve^1_v1(V), h*_v1(V')> = (1/2)(-2
     pi^2 mu) <[A_V, A_b], A_V'> = -pi^2 mu <[A_V, A_b], A_V'>, L-hat(0) here the zero energy part of L_b, with [L_b,
     t*] h_b,v1 + L-hat(0) h-breve^1_v1 = 0 (his (8.2a) writes 2 L_b = ... + L-hat_b(0)). The same computation in four
     dimensions, with Proposition 10.29(i)'s rotation row -4 pi mu (mu = 2m), gives -4 pi m <a(V), a(b) x a(V')>, half
     his -8 pi m, which is (1/2) times Lemma 8.12's printed -16 pi m (p. 157), the normalization 10.32(b) halves; so the
     five-dimensional value is his with so(4)'s bracket for the cross product, in that normalization. It is 0 at a = 0
     (h_v1 = 0 there); against h*_s0 and h*_s1 it is 0 at a = 0 (Proposition 10.29(ii)), and near it these are the
     rotation row's a-dependent entries, not computed beyond continuity (10.32), so that his Step 2 solves (8.34)-(8.35)
     as a coupled system. Near a = 0 it is a perturbation of the decoupled one: with A_V1 below substituted, the s1
     equations are (1)'s isomorphism plus the a-dependent cross entries, which vanish at a = 0, so they remain uniquely
     solvable for small a, on the continuity of those entries (the forty-fourth verifier; D95). By (iv) the form has
     rank 4 at one spin, its kernel the Killing rotations, and ad-invariance, <[A_V1, A_b], A_V'> = <A_V1, [A_b, A_V']>,
     meets (8.35) with (1)'s P absorbed: A_V1 = (v_b + p_b(S_1))/(pi^2 mu), smooth in b, and v_b/(pi^2 mu) where P = 0
     -- his choice, whose printed "-8 pi m a(V_1) = v_b" has the sign reversed against (8.33) (his (8.35) prints
     lambda_b,s1 for lambda_b,v1).
 (c) ([Hin26] Proposition 8.14 near Tangherlini) For his l = 2, 3 and b near b_0 his Steps 0-5 run, Step 2 as modified
     in (b), with (b) for Lemma 8.15, 10.33(f) for Corollary 8.13, (iii) for Step 4's "-3 is not an s2 root" (and at the
     vector and tensor types), 10.32-10.33 for Lemma 8.12 in (8.37), and 10.21(e) for Theorem 7.1(2) in Step 5: the
     states exist in five dimensions with smooth dependence on b, the tensor types included, on the readings 10.33(f)
     rests on, on the weights shifted as in Proposition 10.20(ii), and on [Hin26] Proposition 7.4, Lemma 7.5 and (7.19)
     in five dimensions on the full, two-spin Myers-Perry metric, which his Steps 1-2 use ((8.32c)-(8.33)), 10.31(c) has
     at first order in one spin (the forty-third verifier; D94), and 10.36 at every spin, on its readings (D96).

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII): pp. 25 (section 1.4.1), 140-142 (section
7.2.1: (7.16)-(7.18), Proposition 7.4, Lemma 7.5), 154-163 (Proposition 8.9, Remark 8.10, (8.21), Proposition 8.11,
Lemma 8.12, Corollary 8.13, section 8.5: Proposition 8.14, Lemma 8.15 and their proofs, (8.27)-(8.37)); [DLMF]
(https://dlmf.nist.gov/, 2026-10-24) section 15.8 ((15.8.2), (15.8.8)) and section 15.10 ((15.10.1), the exponent pairs
{0, 1 - c}, {0, c - a - b}, {a, b} at 0, 1, infinity).

*What this gives, and what it does not.* The physical states his section 8.5 builds exist in five dimensions: at
Tangherlini explicitly, for every l >= 2 and the three types, the static tidal solutions in Gauss functions of r^2/mu,
growing like r^l with coefficients that never vanish; near it, for his l = 2, 3, by his construction with its Step 2
modified, whose smoothness in the rotation rests on his Lemma 8.15, which carries over with so(4)'s bracket in place of
the cross product, and on his Proposition 7.4 in five dimensions. Not done, and OPEN: which l five dimensions needs
(10.35: on readings l = 2, t2 included); Lemma 8.15(1)'s pairing against the non-Killing rotations at a != 0 (absorbed
by the modified Step 2 under Proposition 7.4); Proposition 7.4, Lemma 7.5 and (7.19) on the full two-spin metric and the
general Myers-Perry rotation beyond first order and two spins (10.36: Lemma 7.5 at every spin computed; Proposition 7.4
and (7.19) deduced on readings); the readings 10.33(f) rests on, and the weights; his sections 9-10 in five dimensions.
Nothing of this section is proved: Proposition 10.31 is computed, and (a)-(c) are deduced.

### 10.35 [Hin26]'s window in five dimensions: the large indicial roots the expansion needs (`window5.py`; D93, D95)

*The setting.* [Hin26] (p. 17, (1.23)): a term t*^-alpha at iota+ whose coefficient has the term R^-lam u_d(omega) at R
= 0, lam a large indicial root of L-hat(0), "contributes to u via t*^(-alpha+lam) u-bar^(lam)(r, omega)", and "very
large (i.e., very negative) indicial roots contribute to very strongly decaying terms in the K+-asymptotics of u (and
are thus ultimately uninteresting for the purpose of solving a nonlinear problem, for which some finite decay order
suffices)". The order needed: "in a nonlinear iteration scheme we need u to have O(t*^(-2-eps_K))-decay (due to the
2-admissibility of L_b, cf. Corollary 11.10) ... we need the forward map to map u into a tensor f with
O(t*^(-4-eps_K))-decay. This means that we must show that the contributions to u that are not of size O(t*^(-4-eps_K))
have spatial dependence given by large zero energy states" (p. 273); "The '2' in '2-admissibility' is the order of the
'pole' of L-hat_b(sigma)^-1 at sigma = 0" (p. 34); and the pure gauge contributions without t*^(-2-eps_K)-decay "must
moreover be eliminated using gauge modifications" (p. 218). The order alpha: "Sources f arising in the nonlinear
iteration furthermore turn out to also cause a t*^-1-term at iota+" (p. 28), footnote 27: "on a dynamical background,
there is a coupling of the trace-free spherical-spherical part of the metric perturbation, which decays at radiation
field order r^-1, into the (dt*)^2-component ... (cf. the (7, 6)-component of A_h in (5.28)); the resulting r^-1-term in
the (dt*)^2-component then does propagate from I+ to iota+ and gives the claimed t*^-1-term", which "On the nonlinear
level ... is anticipated to encode the Bondi mass" (p. 32); and "The smallest lam for which we will apply this result is
lam = 1, in which case the remainder in (9.41) has more than 4 orders of decay at K+" (p. 177). His index sets carry the
radiative order too: E+ "is the (extended) union of E_I and an index set determined by the pure resonances" ((1.19), p.
16), Proposition 11.16's E-sharp_+ has "smallest elements (1, 0) and (1 + (1 - e_Ups) gam_Ups, 0)" (p. 248), and "The
coupling of (A_h)_{7,4} with u_01 moreover contributes the index set (1 + (1 - e_Ups) gam_Ups, 0) at I+" (p. 228); in
four dimensions these exponents are the Coulombic 1. Hence his window [-3, 0] (p. 128) and Proposition 9.9's expansion
(9.32) (p. 174), each state with its generalized companions to a stated order: h^(<=4)_s1, h^(<=3)_v1, h^(0),(<=3)_s0,
the class roots -lam_sl,l+j + 1 (0 <= l <= 3, j = 0, 1, 1 <= l + j <= 3) to order 2, -l + 2 at sl to 5 - l (l = 2, ...,
5), -l + 1 at vl to 4 - l (l = 2, 3, 4), s2 and v2 at -2 to 1, s3 and v3 at -3 to 0. 10.34 left open which l five
dimensions needs.

**Proposition 10.32 (computed; exact, and numerical where said).** At lin5.py's point (Proposition 10.21(iv)):

 (i) (the roots in [-3, 0]) The roots of det N_L itself with real part in [-3, 0] are, in four dimensions (n = 3, trace
     weight 1): s0: 0 and a class root just below 0; s1: -1 and class roots just below 0 and -1; s2: 0, -2 and class
     roots just below -1 and -2; s3: -1, -3 and a class root just below -2; s4: -2; s5: -3; v1: -1; v2: -1, -2; v3: -2,
     -3; v4: -3; none at s6 and v5 -- his Lemma 8.4's roots in [-3, 0] (p. 149) and the terms of his (9.32). In five
     dimensions they are the same, and t2: -2, t3: -3, none at t4, t5. Every one is real, the integers exact (the
     physical -l, box^Ups's -l + 2 at sl and -l + 1 at vl, s0's 0), each class root a root of det N_Ups(lam - 1) and
     less than 1/4 below its integer. Of these only four-dimensional s0's 0 is a root of det N_C(lam + 1), box^C's root
     1 shifted by -1, which his Lemma 8.4 lists as 0, without the superscript C (p. 149) -- at four-dimensional s1 the
     same shifted root cancels against lin5.py's denominator -- and in five dimensions none is (W1).
 (ii) (the bookkeeping) Let a root mu, fed by t*^-alpha at iota+, give a(t*) = t*^(-alpha+mu) and companions a^(j)(t*)
     of K+ order alpha - mu + j (at s1's and v1's -1, his a_s1 and a_v1 of (9.39a), alpha - 1 + j and alpha + j), and
     keep a state while that order is at most 4, with k = floor(4 - order) companions. At alpha = 1 this gives (9.32)'s
     orders exactly -- s1 4, v1 3, s0 3, -l + 2 at sl 5 - l, -l + 1 at vl 4 - l, s2 and v2 1, s3 and v3 0 -- and at most
     his 2 at the class roots. For every alpha in (1, 2] the physical states kept are s2, v2 and t2 at -2, with k = 0,
     and none at l >= 3. At alpha = 2 the roots kept are those in [-2, 0]: s0's 0 (k = 2) and its class root (1), s1's
     -1 (3) and its class roots just below 0 (1) and -1 (0), s2's 0 (2), its class root just below -1 (0) and its -2
     (0), s3's -1 (1), s4's -2 (0), v1's -1 (2), v2's -1 (1) and -2 (0), v3's -2 (0), t2's -2 (0); of order at most 2:
     s0's 0, s1's -1 (order 1), s2's 0 and v1's -1, and the class roots just below 0 at s0 and s1 at order 2 + O(z). At
     alpha = 3/2, and at 3/2 + 1/100, the roots kept are those in [-5/2, 0]: the same physical states; beyond alpha =
     2's list s2's and s3's class roots just below -2 (k = 0); the class roots just below 0 at s0 and s1 with k = 2 and
     those just below -1 at s1 and s2 with k = 1; the list of order at most 2 the same (W2).
 (iii) (the orders at null infinity) In d + 1 dimensions, for S of degree l on S^(d-1), box(r^-p a(t - r) S) = (2p - d +
     1) a'(t - r) r^(-p-1) S + (l + p)(p - d - l + 2) a r^(-p-2) S exactly: the radiative order p = (d - 1)/2 kills the
     first term, the Coulombic order p = d - 2 at l = 0 the second, where the first is (d - 3) a' r^(-d+1); at d = 4 the
     two orders are 3/2 and 2 and the coefficient is 1, at d = 3 they coincide and it vanishes (W3).

*Proof.* W1-W3 of window5.py: (i) the roots of lin5.py's det N_L at 50 digits, with no cancellation rule, and those of
its factors det N_Ups(lam - 1) and det N_C(lam + 1) for the attribution, a root exact within 10^-30 of an integer; (ii)
exact rational arithmetic, alpha on the grid 1 + m/100 (m = 1, ..., 100), the orders linear in alpha and the class
roots' distance below their integer a positive symbol; (iii) sympy. Controls: in (i) the five-dimensional roots claimed
without the tensor types, and no root from box^C claimed in four dimensions (D93's claim); in (ii) s3 and v3 claimed not
needed at alpha = 1; in (iii) the radiative order claimed to leave the a' term. []

*Deduced.*

 (a) (the iota+ order in five dimensions, a reading) His t*^-1 term is the mass aspect's: the trace-free spherical
     part's radiation fields, quadratically, source the (dt*)^2 component, and in four dimensions the order they
     produce, the Coulombic, is the radiative order 1 ((iii) at d = 3), which his gauge shift 2 gam_Ups keeps from
     resonance (Definition 5.2, p. 85: pi_11 h "without this coupling would have r^(-1-2 gam_Ups)-decay"). In five
     dimensions Theorem M(c) has the mass aspect at s^4 = r^-2 with d_v M quadratic in the radiation fields, (11.2) --
     at past null infinity, and the same at future null infinity with u for v -- the Coulombic order of (iii) at d = 4,
     apart from the radiative 3/2; and a rho_I^z term at future null infinity makes the index (z, 0) at iota+ (p. 273,
     his (11.37)). So alpha_5 = 2 on the reading that no iota+ term of the five-dimensional iteration decays more
     slowly: data O(r^(-2-eps_0)), the analogue of his O(r^(-1-eps_0)), give terms t*^-z with z > 2. But his iota+ index
     sets carry the I+ (radiative-order) exponents: E-sharp_+'s smallest elements (1, 0) and (1 + (1 - e_Ups) gam_Ups,
     0), and the (7, 4) coupling's index set (the setting), are radiative-order exponents, which in four dimensions
     coincide with the Coulombic 1. The same bookkeeping in five dimensions gives alpha_5 = 3/2 + O(gam),
     conservatively, unless the iota+ coefficients at the radiative order vanish there, which is not examined here; no
     five-dimensional (5.28), and so no (7, 4)-type coupling, had been written (D95; 10.38 writes it at h = 0, D100).
 (b) (the pole order, a reading) In five dimensions the zero energy states of Proposition 8.11 (10.32-10.33) are the
     mass, the six rotations and the four centres of mass, these with the boosts h-breve^1_s1 (10.29) as companions and
     the chain ended by Proposition 10.29(iii)'s nonzero pairing (3 pi^2/2) mu (q . c); so L-hat_b(sigma)^-1 has a pole
     of order 2 at 0 as in four dimensions (p. 34, footnote 35), and on the reading that [Hin26c]'s admissibility in
     five dimensions asks the same l_K > 2, u needs t*^(-2-eps_K) and the sources t*^(-4-eps_K). A second reading is in
     this: in four spatial dimensions the mass state, decaying like r^-2, lies just outside L^2, the borderline case in
     which, for Schroedinger operators, logarithmic terms enter the low-energy resolvent; whether they enter here, and
     so whether the pole is exactly of order 2 with no logarithm, is not examined (ROUTES-OPEN.md 4.4, item 3, asks the
     same of the pole's order in the class).
 (c) (the window) Hence five dimensions needs [alpha_5 - 4, 0]: [-2, 0] at alpha_5 = 2, [-5/2, 0] at alpha_5 = 3/2 +
     O(gam). By (ii), for every alpha_5 in (1, 2], its physical states are s2, v2 and t2 at -2 without generalized
     companions: of 10.34's states those at l = 2 -- at a = 0 Y2's, near it by his Steps 0-3 and 5 on 10.34(c)'s
     conditions -- and not his Step 4, which builds the s2 and v2 companions, nor any state at l >= 3, the higher tensor
     types included. The pure gauge states kept and their companions are (ii)'s: s1's -1 enters at K+ order alpha_5 - 1,
     a centre-of-mass motion decaying like t*^(1 - alpha_5) (his (9.39a) at lam = alpha_5), and is eliminated as his
     are, with s0's and s2's 0 and v1's -1 at order at most 2, and the class roots just below 0 at order alpha_5 + O(z)
     (at alpha_5 = 2 unless eps_K lies below their distance); at alpha_5 = 3/2 + O(gam) the class roots just below -2 at
     s2 and s3 enter too, at K+ order 7/2 + O(gam, z), and the class roots carry more companions, all of them pure gauge
     states of the kind his (9.32) eliminates.
 (d) (four dimensions) At alpha = 1, (ii) returns his window [-3, 0], (9.32) and the need for s3 and v3.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII): pp. 16 ((1.19)), 17-18 ((1.23)-(1.25)),
27-30 (section 1.4.3, footnotes 27-28), 31 (Figure 1.7), 32 (section 1.4.4), 34 (footnote 35), 37, 85 (Definition 5.2),
92-93 (Proposition 5.11, (5.27)-(5.28)), 117 (Lemma 6.6), 128, 149 (Lemma 8.4), 169 (Proposition 9.4), 173-177
(Definition 9.8, Proposition 9.9, (9.32), Proposition 9.11, (9.39a)-(9.39b)), 199 (Theorem 10.1), 218, 225 (Corollary
11.10), 228 (the proof of Lemma 11.15), 248 (the proof of Proposition 11.32), 273, 279 (Remark 11.60), 324 (section
13.2).

*What this gives, and what it does not.* Which large indicial roots five dimensions needs: the physical states are s2,
v2 and t2 at -2 alone, and none of their companions, for any iota+ order in (1, 2]; so 10.34's l = 3 states and his Step
4 are spare in five dimensions, and the one tensor state needed is t2's, which 10.34 has at a = 0 and near it. The
window shrinks from [-3, 0] to [alpha_5 - 4, 0]: to [-2, 0] if the slowest iota+ term is the mass aspect's t*^-2, the
Coulombic order separating from the radiative one above four dimensions; to [-5/2, 0], with two more pure gauge
class-root states, if the radiative order 3/2 reaches iota+ as his index sets would carry it. Not done, and OPEN: which
alpha_5 -- his (5.28) and Proposition 11.16 in five dimensions line by line, and whether the radiative-order iota+
coefficients vanish there (10.38: (5.28) at h = 0 computed, the radiative coefficients vanishing at iota+ cap I+, and
alpha_5 = 2, on readings); [Hin26c]'s Theorem 11.1 in five dimensions; whether logarithms enter at the pole; whether a
five-dimensional radiation field can have a nonzero late limit (10.38(d): not, on readings); the data class; sections
9-10 (section 7.2.1 at every spin is 10.36's). Nothing of this section is proved: Proposition 10.32 is computed, and
(a)-(d) are deduced.

### 10.36 [Hin26] section 7.2.1 in five dimensions at every spin: Lemma 7.5 on the Myers-Perry family (`mp5.py`; D96)

*The setting.* [Hin26] Lemma 7.5: "Let V in V_1 and set V_b := g_b gbar^-1 V; set S' := S(a(b) x a(V)) in S_1. Then
delta*_(g_b) V_b = rho^2 (-2m (dt* + dr) (x)_s rho V(S')) - delta*_(g_b)(rho S(a) S' dr + (1/2) d/(S(a) S')) + h~_b(S')
(7.20) where h~_b : S_1 -> rho^3 C^oo(X; S^2 T*X) is linear and depends smoothly on b" (p. 140); its proof writes
delta*_(g_b) V_b = (1/2) L_R g_b = -(1/2) g_b (L_R g_b^-1) g_b and works through the coefficients of (3.17). His
Proposition 7.4 then gives h*_v1(V) = h-sharp_b,v1(a(b) x a(V)) + h*-flat_b,v1(V) with h-sharp_b,v1(w) in rho^2 C^oo
"depending smoothly on b and linearly on w in R^3" (p. 140), and footnote 82: "while lambda_b,v1 only induces a
functional on the subspace {a(b) x a(V'_1)} ... which depends in a discontinuous fashion on a ..., the functional
lambda-sharp_b,v1 is defined on all of R^3" (p. 161). 10.31(c) has this in five dimensions at first order in one spin,
and 10.34(c) and 10.35(c) make it on the full two-spin metric a condition. In five dimensions the spin is a matrix A in
so(4) and the Myers-Perry metric in Kerr-Schild form ([ER08] p. 14: "the solutions belong in the Kerr-Schild class",
their (31)) can be written for every A at once: with s = -tr(A^2)/2, p = Pf A, P = r^4 + s r^2 + p^2 and M = (r^2 + s)
I + A^2, so that M/P = (r^2 - A^2)^-1, let r > 0 be the root of Q = P - x^T M x, k = dt + (M (r I + A) x / P) . dx and
H = mu r^2/(P F), F = 1 + x^T A^2 M^2 x / P^2; g_A = eta + H k (x) k. The rotations are R = A_V x, V = (A_V x) . dx,
V_A = g_A gbar^-1 V = g_A(R, .); for W in so(4), V(W) = (W x) . dx.

**Proposition 10.33 (computed; exact).** With g_A as above, A in so(4), and four dimensions on Kerr over so(3):

 (i) (the family) A^4 + s A^2 + p^2 I = 0 and (r^2 I - A^2) M = P I identically, so k is null exactly where Q = 0. At A
     = a J_12 + b J_34, P is [ER08]'s Pi and F its F (44) with mu_i^2 = (x_(2i-1)^2 + x_(2i)^2)/(r^2 + a_i^2), g_tt =
     -1 + mu r^2/(Pi F) is its (42)'s, and Q = 0 is sum mu_i^2 = 1; at A = 0 g_A is Tangherlini in ks5.py's ingoing
     Kerr-Schild form. g_A is Ricci-flat exactly at rational points (r = 3/2, mu = 7/5, x rational on Q = 0, the
     metric's jet to second order solved for exactly): two spins (1/3, 1/5) with A rotated out of block form by a
     Cayley rotation, equal spins (2/7, 2/7), one spin (1/2, 0); Kerr likewise (M1).
 (ii) (Lemma 7.5 at every spin) Q, P and x^T A^2 M^2 x are invariant, and M (r I + A) x covariant, under so(4) acting on
     (x, A) at fixed r, symbolically in A, x and r for each basis rotation; hence, for W = [A, A_V], delta*_(g_A) V_A =
     (1/2) L_R g_A = (1/2) D_A g_A(W), the derivative of the family along W -- checked directly on the full metric, r
     implicit, at the points of (i) for all six basis rotations, none Killing there. In four dimensions the same with
     [A_a, A_v] = A_(a x v); there A x = a x x is the negative of the angular momentum (J = -m a), so W = [A_b, A_V] =
     -A_(S') for his S' = a(b) x a(V) (M2).
 (iii) (the expansion) Along x = X/eps, X = (1, 2, 2, 4): at A = 0, D_A g_A(W) = (2 mu/r^4)(dt + dr) (x)_s V(W) exactly,
     the eps^3 term alone; at A = a J_12 + b J_34 with (a, b) = (1/3, 1/5) its eps^3 term is the same and its eps^4,
     eps^5 and eps^6 terms are nonzero. In four dimensions (2 mu/r^3)(dt + dr) (x)_s V(W), mu = 2m, at eps^2, the rest
     from eps^3 (M3).
 (iv) (the Killing rotations) dim ker ad_A = 6 at A = 0, 4 at a = b != 0 and at a = -b != 0, 2 otherwise, one spin
     included, and L_R g_A = 0 exactly at the points of (i), unrotated, for a basis of the kernel; in four dimensions 3
     and 1 (M4).
 (v) (h-sharp's leading term) From the Kerr-Schild leading term (mu/r^4)(dt + dr) (x)_s V, the correction of 10.31(iii)
     is c_0 = mu (h + 2v + 2)/(3 (h + 2v)), against 2 mu/(3 (h + 2v)) from (mu/r^4) dt (x)_s V, the difference mu/3
     being the pure gauge (mu/r^4) dr (x)_s V = delta*(-mu r^-3 V/3); and the rho^3 leading terms of h-sharp agree. In
     four dimensions c_0 = M (h + 2v + 2)/(h + 2v) against 2M/(h + 2v), the difference M, the rho^2 leading terms
     agreeing (M5).

*Proof.* M1-M5 of mp5.py: (i) the identities symbolically, the Ricci tensor at each point from the jet of g to second
order in exact rational arithmetic, r's jet solved from Q by Newton steps; (ii) the invariances as polynomial identities
in sympy, the full identity at the points by the same jets with a displacement along W; (iii) sympy series in eps with
exact A, W, X; (iv) ranks of the 6 x 6 matrices of ad_A and the jets of (ii); (v) dual5.py's operators on Tangherlini,
the leading orders solved at one generic angle and checked at a second. Controls: in (i) H = mu r/(P F), the
even-dimensional exponent, claimed Ricci-flat; in (ii) the bracket reversed; in (iii) the remainder claimed at rho^5; in
(iv) equal spins claimed to leave 2; in (v) c_0 claimed unchanged. []

*Deduced.*

 (a) ([Hin26] Lemma 7.5 in five dimensions, at every spin) By (ii) the whole of delta*_(g_b) V_b is (1/2) D_A g_b(W)
     with W = [A_b, A_V] (g_A at A = a J_12 + b J_34 is [ER08] (42) with (a_1, a_2) = (-a, -b), [ER08]'s p. 10 (16) and
     p. 14's footnote 4 fixing the sense, so A is minus the spin, and in four dimensions W = -A_(S'), the leading term
     below his -2m rho^2 (dt* + dr) (x)_s rho V(S') with its sign; D98): it depends on V only through W, linearly, and
     is defined for every W in so(4), not only on the image of ad_(A_b) -- the structural reason being the equivariance
     g_(O A O^T)(O x) = O g_A(x) O^T, which 10.34(b)(2) already uses at first order as his Remark 8.10. By (iii),
     delta*_(g_b) V_b = mu rho^3 (dt + dr) (x)_s rho V(W) + h~_b(W) with h~_b : so(4) -> rho^4 C^oo linear and smooth in
     b (rational in x, r and the entries of A_b, r analytic in rho at fixed direction), the leading term independent of
     A_b. These coordinates need no spin-dependent pure gauge term at leading order -- their dt is the ingoing
     Kerr-Schild time, so dt + dr carries the spin-independent pure gauge mu rho^3 dr (x)_s rho V(W) against his static
     dt* + dr, as (v) shows: his -delta*(rho S(a) S' dr + (1/2) d/(S(a) S')) comes from x = r omega with r the
     Boyer-Lindquist radius, in which the flat part of the Kerr family is not Cartesian; Kerr in Kerr-Schild form has
     none, (iii). Any other SO(4)-equivariant family of coordinates gives the same structure, the leading term changing
     by a pure gauge term as (v) shows; that the five-dimensional g_b of route B is chosen equivariantly is a reading,
     as his is SO(3)-equivariant.
 (b) ([Hin26] Proposition 7.4 in five dimensions, at every spin) His proof runs with (a): the ansatz V_b plus rho S-type
     terms becomes V_b plus c_0 r^-3 V(W) with c_0 fixed by N*_v1(2) = 3 + 6 gam_C v_C (10.31(i)), and h-sharp_b,v1(W)
     is defined for every W in so(4), smooth in b, with leading term at rho^3 that of 10.31(iii) with a V' replaced by
     -V(W), the same at every spin by (iii) and in any equivariant coordinates by (v). The two sources of his (7.33) lie
     in rho^5 C^oo, one order beyond his, the shift of 10.31(b); no root of the adjoint has real part in [3, C_0 + 2]
     (10.31(a)), so their formal solution is in rho^3 C^oo to that order, and his (7.19) becomes (delta*_(g_b, E^C))*
     h-sharp_b,v1(W) and D Ric(0)* h-sharp_b,v1(W) in rho^(floor(C_0) + 3) C^oo -- on the readings 10.31(a) rests on.
 (c) (the discontinuity) The space of V for which (7.16) holds, ker ad_(A_b), is six-dimensional at a = 0,
     four-dimensional at a = +-b != 0, two-dimensional otherwise: his discontinuity at a = 0, of a richer kind; h-sharp
     being defined on all of so(4), his footnote 82 holds as stated with lambda-sharp_b,v1(W) = <v_b, W>, v_b in so(4)
     smooth in b, so that 10.34(b)'s modified Step 2, A_V1 = (v_b + p_b(S_1))/(pi^2 mu), stands at every small spin.
 (d) (what it settles) 10.34(c)'s and 10.35(c)'s condition -- his Proposition 7.4, Lemma 7.5 and (7.19) on the full
     two-spin metric -- holds, on the readings of (a) and (b); his Steps 1-3 near Tangherlini, Step 2 modified, use
     nothing more of section 7.2.1.
 (e) (four dimensions) On Kerr the same computation gives his Lemma 7.5's structure, with no pure gauge term at leading
     order in Kerr-Schild coordinates and the remainder at rho^3, the cross product as so(3)'s bracket.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII): pp. 65 (Definition 2.28), 126 (Remark 6.17),
140-144 (section 7.2.1: (7.16), Proposition 7.4, (7.17)-(7.19), Lemma 7.5 and its proof, (7.20)-(7.28), the proof of
Proposition 7.4, (7.29)-(7.35)), 161 ((8.32c)-(8.33), footnote 82). [ER08] (arXiv:0801.3471v2): pp. 10 ((14)-(16)), 14
((31)-(34)), 16 ((42)-(44)), 19 (section 4.3).

*What this gives, and what it does not.* His section 7.2.1 in five dimensions at every spin: Lemma 7.5 is an exact
identity of the Myers-Perry family -- the deformation tensor of a rotation is the family's derivative along the bracket
of the spin with the rotation -- so h-sharp is defined on all of so(4) and smooth in the spin across the jumps 6, 4, 2
of the Killing rotations, and the condition 10.34 and 10.35 placed on the full two-spin metric is met on readings. Not
done, and OPEN: the formal solution of (b) beyond its leading order and (7.19) itself, deduced and not computed;
Ricci-flatness of the family symbolically rather than at points; the five-dimensional g_b in coordinates outgoing at
infinity with his cut-offs; the readings 10.31(a) rests on; sections 9-10. Nothing of this section is proved:
Proposition 10.33 is computed, and (a)-(e) are deduced.

### 10.37 [Hin26] section 9.1 in five dimensions: the pure iota+ resonances (`iota5.py`; D97)

*The setting.* [Hin26]'s model at future timelike infinity is "N_iota+(L-bar, lam) = ... = -2 v (v d_v - lam)(v d_v -
1 - S-bar) + v^2 L~-bar(0)(omega, v d_v, d_omega)" (9.11), v = t*/r, where "At v = oo, the indicial roots of
L~-bar(0)(omega, -R d_R, d_omega), i.e., the negatives of the indicial roots recorded in Lemma 8.4, dictate the
asymptotic behavior ... At v = 0 on the other hand, the indicial roots of v d_v - 1 - S-bar take on this role" (p.
168). Definition 9.6: "We denote by spec_iota+(L-bar) in {z in C : Re z >= 1 + eps_ind} the set of poles of
N_iota+(L-bar, lam)^-1 acting on C-dot^oo(iota+; S^2 T*)", and "Elements of spec_iota+(L-bar) were called 'pure'
resonances" (p. 172); "u_3(v, omega) := (v/(v+2))^(3/2) in ker N_iota+(box-bar_4+1, 3) ... Since u_3 has vanishing
incoming data (no v^3-term), it is thus what we call a 'pure' resonant state" (p. 16), and E_+ "is the (extended)
union of E_I and an index set determined by the pure resonances of the iota+-model operator" ((1.19), p. 16).
Proposition 9.2(2): "For all lam in C with Re lam < 1 + eps_ind, the map (9.3) is invertible. Furthermore, for every
C, the map (9.3) is invertible for all but finitely many lam in C with Re lam <= C" (p. 165); its proof extends u by
zero across v = 0 ("Given the membership (9.6), the extension of u to {v < 0} by 0 lies in L^1_loc"), Fourier
transforms in v, and ends "But since Re(-lam + 1) > -eps_ind, Proposition 8.6 applies and shows that w-flat_+- = 0"
(p. 166). 10.35(a) reads alpha_5 = 2 "on the reading that no iota+ term of the five-dimensional iteration decays more
slowly"; a pure resonance with real part at most 2 would be such a term. Here the five-dimensional model by type, from
lin5.py's operators, and its pure resonances. A pure resonant state at lam is u = t*^-lam G(v), N_iota+ G = 0, with
L1(D) G = O(v^(min mu + 1)) at v = 0, mu over the outgoing exponents -- his (9.17), "(v d_v - 1 - S-bar) h in
A^(E^tot_(iota+,I) + 1)", which "reflects the fact that the asymptotics of h at I+, i.e., as v -> 0, are of radiation
field type (with characteristic exponents given by the spectrum of 1 + S-bar)" (p. 169): only outgoing exponents, so
no v^lam unless lam is one of them, its coefficient then in ker L1(lam) (D99) -- and only those of his E_K at v = oo,
"an upper bound for the resulting index set E_K can be determined from -1 times the indicial roots in Lemma 8.4 with
non-positive real parts" (p. 170).

**Proposition 10.34 (computed; exact, and numerical where said).** On 4+1 Minkowski, with lin5.py's bases, point and
parameters:

 (i) (the model) With t* = t - r and fields T^a r^-x u (T = t*, u of degree 0 and one harmonic type), L-bar, box^C and
     box^Ups return T^(a-1) r^(-x-1) [a L1(x) u] + T^a r^(-x-2) [N(x) u] and no T^(a-2) term (dt* is null), closed in
     the type; so with a = x - lam and G = sum s^x, s = v, the model is M0(D) G + s M1(D) G = 0, D = s d/ds, M0(x) =
     (x - lam) L1(x) with L1 affine, M1 = N -- his (9.11) at n = 4 -- and M1 is lin5.py's indicial matrix itself (s0,
     v1). At gam_Ups = gam_C = 0, L1(x) = (3 - 2x) Id for box^C and box^Ups (s0, s1, v1) and (3 - 2x)/2 Id for L-bar
     (s0, s1, v1, v2, t2), the transport of the free wave (I1).
 (ii) (the connection) z = s/(s + 2) sends the singular points s = 0, -2, oo to 0, oo, 1, so the Frobenius series at s =
     0 (the roots of det L1) and at s = oo (the K lowest roots of det N) both converge at s = 2; a pure resonance is a
     zero of the 2K x 2K determinant of the two families there. On the free 4+1 wave its zeros are lam = 3 + l + k (l, k
     = 0, 1, 2) to 10^-25 and at lam = 3, l = 0 the outgoing series is z^(3/2) = (v/(v + 2))^(3/2) exactly, his u_3; on
     box^C at s0, gam_C = 1, it vanishes at 1 + mu and 2 + mu for its upper root mu = 2.6457654215... (I2).
 (iii) (the descent at work) On box^C at s0, gam_C = 10: the argument principle counts 4 zeros in [6/5, 9/2] x [-3, 3],
     the points 1 + mu + k for the upper roots mu = 2, 2.1355877934... of det N (k = 0, 1), each located to 10^-22, so
     none complex; at 1 + mu the resonant state's moment m = int_0^oo s^-lam G ds is nonzero with N(lam - 1) m = 0 to
     10^-17 of its scale, and at 2 + mu it vanishes (I3).
 (iv) (the record's point: gam_C = 10^6, e_C = 1/102400, v = 1/2, gam_Ups = e_Ups = 1/100) The roots of det N_L with
     real part in (0, 3/2] are, at s0, 1.0000747438..., at s1 1.0001201950..., none at v1, each 1 less than a root of
     det N_C, none in (0, 1]. For every l <= 400 (damping5.py's polynomials) box^C's roots with real part in [-100, 5/2]
     are the Coulomb 2 at l = 0 and 1 and, at every scalar type, roots in (2, 5/2): 2 + 7.474 x 10^-5 at l = 0, 2 +
     1.202 x 10^-4 at l = 1, two for 2 <= l <= 135 and one for 136 <= l <= 400, the lowest of all 2 + 2.932 x 10^-6 at l
     = 2; at the vector types none (the lowest 3, at l = 1). Beyond, the scalar types have one root in (2, 5/2) for 401
     <= l <= 706 and none for 707 <= l <= 711 and at l = 10^3, 10^4, 10^5. The e_C-root is 2 + e_C ((1 - v^2) kappa + 3
     (1 + v^2))/(2 v^2) of damping5.py U3's Q_5 within 5 h, h = 1/gam_C; and box^C's s0 root above 2 decreases from
     2.0149221 to 2.0000747 as gam_C runs over 10^2, 10^2.5, ..., 10^6, inside (2, 5/2); over 201 points gam_C = 10^(2 +
     k/50) it is the only root of det N_C in (2, 5/2), decreasing, and det N_L has no root with real part in (0, 1] and
     exactly four with real part <= 0, I2's K lowest (I4).
 (v) (the s0 candidate at moderate gam_C, the record's other parameters) At gam_C = 10 and 100 the determinant of
     L-bar's s0 connection changes sign once on a grid of [1.2, 2.3] with the candidate +- 10^-3, 10^-5 added, at the
     candidate -- box^C's root 2.1355877934... and 2.0149221090... -- where it is below 10^-4 of its value at +- 10^-5:
     there L-bar has a pure resonant state at the candidate, a pole of the inverse on the reading of index 0 (10.37(c)).
     At gam_C = 10^6 the method fails: the outgoing exponents near 10^6 need millions of terms at s = 2, and digits to
     match (at gam_C = 100, 400 suffice and 200 do not; the forty-sixth verifier found of the order of 3 gam_C terms
     needed, 900 at gam_C = 300, where 200 digits left the candidate unresolved and 400 resolved it; 260 to 480 terms at
     40 to 140 digits gave a smooth determinant at the record's point that was a truncation artefact) (I5).

*Proof.* I1-I5 of iota5.py: (i) sympy, the powers of T split after the point is substituted; (ii)-(iii) mpmath at
30-40 digits, the connection asserting at every evaluation that the K lowest roots of det N are those with real part <=
0 (D99), the recursions in z four-term, the argument principle with every step's change of argument below pi/6, the
moment by quadrature in z on both halves; (iv) the roots at 50 digits, det N_L's from (i)'s M1 and box^C's from
damping5.py U3's sextic and quadratic; (v) 50 and 100 digits, 260 and 700 terms. Controls: in (i) the powers of T split
with z = x1 + i x2 symbolic, where sympy's expand moves T into denominators T x1 + I T x2 and the transport of the
degree-p harmonics is lost; in (ii) the outgoing exponent moved by 1/10; in (iii) a count of 3 claimed, and N(lam - 2) m
= 0; in (iv) L-bar's root 1 at s0, which lin5.py's denominator (lam - 1)^2 removes, counted; in (v) the zero claimed
10^-3 above the candidate. []

*Deduced.*

 (a) (towers) If u = t*^-lam G(v) is a pure resonant state, so is d_t* u = t*^(-lam-1) (D - lam) G at lam + 1: the
     model's coefficients do not depend on t*, the outgoing and the E_K exponents are kept, and (D - lam) G != 0, since
     c v^lam is not O(v^nu) at oo for Re lam > 0 >= Re nu. So spec_iota+ is closed under lam -> lam + 1, as (ii)-(iii)
     find.
 (b) (descent) Let mu_j be the outgoing exponents, nu_k those of E_K, and Re nu_k + 1 < Re lam < Re mu_j + 1 for all
     j, k. Then m := int_0^oo v^-lam G(v) dv converges and N(lam - 1) m = 0: pair the equation with v^-lam dv/v; (D -
     lam) L1(D) G integrates to [v^-lam L1(D) G], which vanishes at both ends since L1(mu_j) g_j = 0 makes L1(D) G =
     O(v^(mu + 1)) at 0, and s M1(D) G pairs to M1(lam - 1) m, the boundary terms vanishing by the same bounds. Either
     m != 0 and lam - 1 is a root of det N, or m = 0 and G~(v) := v^(lam - 1) int_0^v w^-lam G(w) dw -- in spacetime
     int_0^t* u dt* -- is a pure resonant state at lam - 1: (D - lam + 1) G~ = G, so H := L1(D) G + s N(D) G~ has (D -
     lam) H = 0, H = c v^lam, and H = O(v^(min mu + 1)) at 0 forces c = 0; G~ has the exponents mu_j + n at 0, and at
     oo, m being 0, G~ = -v^(lam - 1) int_v^oo w^-lam G dw = O(v^nu); and G~ != 0. In spacetime: the time integral of
     a pure resonant state is a static solution homogeneous of degree 1 - lam, r^-(lam - 1) m, or zero, and then the
     state is the time derivative of one at lam - 1.
 (c) (injectivity in five dimensions) The injectivity half of his proof of Proposition 9.2(2) (p. 166) carries over with
     v d_v - 3/2 - S-bar for v d_v - 1 - S-bar: the threshold becomes s < 2 + min spec S-bar - Re lam, the extension by
     zero is in L^1_loc for Re lam < 5/2 (min spec S-bar = 0, 10.25), the Fourier transform and the conjugation by
     r^(-lam + 1) are free of the dimension (the shift comes from L~(0)'s argument v d_v + lam), and Proposition 8.6 in
     five dimensions (10.24(c)-(d), 10.25(b)) takes the weights in (-eps_ind, 0). So there is no pure resonance with Re
     lam < 1 + eps_ind -- at the record's point, on 10.24-10.25's readings. The bound comes from the zero energy weight,
     which does not see the dimension: 1 + eps_ind in five dimensions as in four. The other half is not carried: the
     index 0 property of his Proposition 9.2(1), proved "in an indirect way" by the semiclassical estimate (9.9) on cone
     Sobolev spaces as Im lam -> +oo, with the inversion of N_tf(L-bar, 1) and, for the adjoint, his tf-admissibility
     (pp. 167-168); it turns injectivity into invertibility and makes the inverse exist and be meromorphic. In five
     dimensions it is a reading. (d) needs only the kernel half -- a resonant state is a kernel element, and a pole of
     the inverse, where there is one, gives one -- while the converse, a kernel element being a pole, which Proposition
     10.34(v) and (e) use, rests on that reading (the forty-sixth verifier, D99).
 (d) (below 5/2) For L-bar the outgoing exponents are 3/2 + spec S-bar >= 3/2 and E_K's are the roots with real part <=
     0, as many as K (10.24), so (b) applies whenever 1 < Re lam < 5/2. A pure resonance with real part in [1 + eps_ind,
     5/2) has lam - 1 a root of det N_L with real part in [eps_ind, 3/2), or is the time derivative of one at lam - 1;
     (c) excludes that one below 1 + eps_ind, and (b) sends it above to a root or a state with real part in [eps_ind,
     1/2), of which there are none ((c), and no root of det N_L in (0, 1]). By lin5.py E2 the roots of det N_L are the
     physical -l and l + 2, box^Ups's plus 1 and box^C's minus 1, D's cancelled; in (0, 3/2) neither the physical ones
     lie nor box^Ups's (gaugepot5.py G1: near -1 its roots lie below -1 for z > 0 -- at s0 (1 - (9 + 4z)^(1/2))/2 = -1 -
     z/3 + O(z^2), at s1 a root of lam (lam - 1) = (8 + z - (16 + 4z + z^2)^(1/2))/2 > 2 -- so their shifts are
     negative; near 0 only its exact Killing 0 at s0 and s1, which D removes), and box^C has no root in [-100, 2] but
     the Coulomb 2 (damping5.py U4, (iv)). Hence at the record's point, on the readings of (c), spec_iota+(L-bar) cap
     {Re lam < 5/2} lies in {lam^C : det N_C(lam^C) = 0, 2 < Re lam^C < 5/2, scalar types}, the lowest candidate over l
     <= 400 2 + 2.93 x 10^-6 (l = 2), and no pure resonance has real part at most 2.
 (e) (the candidates) A state at a candidate is of the constraint kind: its moment is nonzero ((d)) and an indicial
     solution of det N_L's box^C root, whose gauge 1-form is not zero (his Lemma 8.4's proof: with it zero the solution
     is pure gauge or physical, and the root would be one of theirs), so eta = delta_(E^Ups) G h != 0 and eta is a pure
     resonant state of box^C at lam^C + 1 = 1 + (box^C's upper root). By (v) L-bar has a pure resonant state at the s0
     candidate at gam_C = 10 and 100, a resonance on (c)'s index 0 reading. Along gam_C in [100, 10^6] it stays alone in
     (2, 5/2) ((iv), at 201 points of a logarithmic grid, with det N_L free of roots in (0, 1] and its K lowest roots
     those with real part <= 0), and by (b)-(d) the zeros in the strip lie at candidates; on the reading that (c) holds
     along that path (the record has it at 10^6 only), Hurwitz's theorem carries the zero along the candidate, and
     2.0000747438... is a pure resonance of L-bar at the record's point. Not computed there.
 (f) (for 10.35) The second channel of alpha_5 is closed on its alpha_5 = 2 reading: no pure resonance has real part at
     most 2, so the pure resonance part of E_+ lies above 2. A pure term reaches K+ at order lam^C - nu, nu <= 0 in E_K;
     at s0 and s2, whose E_K contains 0 (10.35(i)), that is 2 + 7.47 x 10^-5 and 2 + 2.93 x 10^-6 if those candidates
     are resonances -- terms of the kind 10.35(c)'s caution names, when eps_K exceeds their distance. Such terms are of
     the constraint kind ((e)): a solution whose gauge 1-form vanishes, the constraints propagated, does not excite
     them; whether the iteration's sources do is his section 12's question in five dimensions, not examined here.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII; printed page numbers): pp. 16-17 ((1.16),
(1.19), footnote 9, (1.20)-(1.22), Example 1.6), 164-166 ((9.2), Proposition 9.2 and its proof), 167 (the index 0 step;
D99), 168 ((9.9), D99; (9.10)-(9.11), Definition 9.3), 169 (Proposition 9.4, (9.17); D99), 170 (Remark 9.5, the proof of
Proposition 9.4), 172 (Definition 9.6, Remark 9.7), 180 (Lemma 9.13), 184-185 (Definition 9.19, Lemma 9.21, Proposition
9.22), 149 (Lemma 8.4 and its proof).

*What this gives, and what it does not.* The pure iota+ resonances of the five-dimensional model: on (b)'s descent and
(c)'s injectivity, every one with real part below 5/2 sits at a root of box^C's zero energy operator in (2, 5/2) -- one
at s0, one at s1, two at each scalar l from 2 to 135, one from 136 to 706 and none from 707 to 711 nor at l = 10^3,
10^4, 10^5 -- so none has real part at most 2, and the alpha_5 = 2 reading of 10.35 is not undercut by pure resonances.
L-bar has a pure resonant state at the s0 candidate at gam_C = 10 and 100, a resonance on the reading of index 0, and,
on a further reading, at the record's point. Not done, and OPEN: the candidates at the record's point by computation (a
method for exponents near 10^6: their WKB form, or the gam_C -> oo limit); the s1 and l >= 2 candidates (the s1
determinant at gam_C = 10 sits below 10^-110 at 100 digits, not resolved); (c)'s readings, the index 0 half of his
Proposition 9.2 in five dimensions among them, and the path of (e); whether his section 12 excites the constraint-kind
states; four dimensions, where the same argument would place the part of his spec_iota+ below 2 at box^C's roots in (1,
2). Nothing of this section is proved: Proposition 10.34 is computed, and (a)-(f) are deduced.

### 10.38 [Hin26] (5.27)-(5.28) and Proposition 5.14 in five dimensions; the radiative order at iota+ (`scri5.py`; D100)

*The setting.* [Hin26] Proposition 5.11: "L_(g,g0) == (2 r^-1 d_0 r + r^-1 A_h) d_1 + r^-1 B_h" (5.26a), "where, in the
bundle splitting S^2 T* = <(dx^0)^2> + (2 dx^0 (x)_s r T*S^2) + <r^2 g-slash> + <2 dx^0 dx^1> + (2 dx^1 (x)_s r T*S^2) +
r^2 ker tr-slash + <(dx^1)^2>, (5.27) the operator A_h is lower triangular and B_h is strictly lower triangular" (pp.
92-93), (5.28) printing A_h with a constant part and entries d_1(r h_01), d_1(r h_1a), d_1(r h_ab) of the perturbation
h, and B_h with entries d_1^2(r h); "one expects that if L_g g-dot = 0 ... then various components of g-dot decay like
O(rho_I^(1+z)) where z is an eigenvalue of A_h" (p. 97); "pi_01 h and pi_1/ h have r^(-1-(1 - e_Ups) gam_Ups)- and
r^(-1-gam_Ups)-decay, respectively; and pi-slash_0 h has a r^-1 radiation field, which couples into pi_11 h (which
without this coupling would have r^(-1-2 gam_Ups)-decay)" (p. 85, after Definition 5.2); Definition 5.13: "F_I,11 := 1 +
(E^C_I u (1, 0) u (1 + (1 - e_Ups) gam_Ups, 0))" (5.43), and Proposition 5.14's proof: "The (7, 4) and (7, 6) entries of
I + A_h couple pi_01 g-dot and pi-slash_0 g-dot into the 11-component of the output, while the (7, 7) entry of I + A_h
annihilates the rho_I^(1+2 gam_Ups)-term in the expansion of g-dot_11; hence the definition of F_I,11 in (5.43)" (p.
98); at timelike infinity, "we do not need to include the index set (1, 0) in E_iota+,I,11 ... (This arose from the
coupling of the r^2 ker tr-component with the (dx^1)^2-component via the (7, 6)-component of A_h in (5.28); but this
coupling is absent when h = 0.)" (p. 169). 10.35(a) left the iota+ order alpha_5 between two readings, 2 (the mass
aspect) and 3/2 + O(gam) (his index sets carrying the radiative order), with "no five-dimensional (5.28), and so no (7,
4)-type coupling" written; 10.37 closed the pure resonance channel. Here the five-dimensional (5.28) at the background,
the exponents it gives at null infinity, and the radiative order at timelike infinity. x^0 = t + r, x^1 = t - r
(damping5.py), d_0 = (d_t + d_r)/2, d_1 = (d_t - d_r)/2, d_1 = d_t* at null infinity, and A_0 := A_h at h = 0 is
sbar5.py's S-bar (10.25: 2 rho S-bar the d_t* coefficient of 2 L - box) -- his own "A_h = A_0 = S-bar_(E-bar^Ups,
E-bar^C) in the notation of Lemma 8.2" (p. 223; and (8.8), p. 146) -- v below being v_C.

**Proposition 10.35 (computed; exact, and numerical where said).** On 4+1 Minkowski, in the splitting (5.27) with S^3:

 (i) (the five-dimensional (5.28) at h = 0) A_0 is lower triangular, the same at (R, 0, 0, 0) and at (1, 2, 2, 4), and
     agrees with the constant part of his (5.28) in its diagonal 2 (1 - v) gam_C, (1 - v) gam_C, (1 - e_C)(1 - v) gam_C,
     (1 - e_Ups) gam_Ups, gam_Ups, 0, 2 gam_Ups, its (5, 2) entry (1 + v) gam_C + gam_Ups and its (7, 4) entry 2 (1 -
     e_Ups) gam_Ups; it differs in four trace couplings: (3, 1) = (4/3)(1 - e_C)(1 + v) gam_C (his 2 (1 - e_C)(1 + v)
     gam_C), (4, 1) = (1 + 2 e_C)(1 + v) gam_C/3 + gam_Ups (his e_C (1 + v) gam_C + gam_Ups), (4, 3) = ((1 + 2 e_C)(1 -
     v) gam_C + 3 e_Ups gam_Ups)/4 (his (e_C (1 - v) gam_C + e_Ups gam_Ups)/2) and (7, 3) = (3/2)((1 + v) gam_C + e_Ups
     gam_Ups) (his (1 + v) gam_C + e_Ups gam_Ups). In four dimensions, at the trace weight 1, the same computation is
     his (5.28) at h = 0, all 49 entries (C1). Which entries differ is a matter of slot 3's normalization: its
     coordinate here is the coefficient of r^2 g-slash, the trace over 3; with his pi_C's (1/2) tr-slash (Definition
     5.2, p. 85) in its place -- row 3 scaled by 3/2, column 3 by 2/3 -- (3, 1) and (7, 3) are his and only (4, 1) and
     (4, 3) differ, by (1 - e_C)(1 + v) gam_C/3 and (1 - e_C)(1 - v) gam_C/6 (deduced from the entries; the
     forty-seventh verifier).
 (ii) (the exponents at null infinity by type) iota5.py's L1(x) for L-bar (10.37) has det L1(x) = prod (3/2 + (A_0)_ii -
     x) over the slots its type occupies: s0 the scalar ones 1, 3, 4, 7; v1 the vector ones 2, 5; v2 those and the
     trace-free 6; t2 the 6 alone -- every parameter symbolic (C2).
 (iii) (no state at a radiative exponent) At s0, gam_C = 10 and 100 with the record's other parameters, at lam = 3/2 +
     (1 - e_Ups) gam_Ups and 3/2 + 2 gam_Ups, the exponents of pi_01 and pi_11 that the (7, 4) entry couples, the
     connection determinant of 10.37 with that exponent's own column, its leading coefficient in ker L1(lam), is above
     3/10 of its largest value on iota5.py I5's grid of [1.2, 2.3], and agrees with its values at lam +- 10^-15 to 10^-9
     of them -- the computation's noise, 10^-15 at gam_C = 10 and 10^-11 at 100; at t2, lam = 3/2, likewise (C3).

*Proof.* C1-C3 of scri5.py: (i) sympy, sbar5.py's S-bar at the point, applied to an element of each summand of (5.27) --
(dx^0)^2, 2 dx^0 (x)_s w, the tangential metric, 2 dx^0 dx^1, 2 dx^1 (x)_s w, a trace-free tangential tensor, (dx^1)^2,
w the tangential part of dx_3 -- and the result read in the frame (d_0, d_1, tangential), each summand landing in its
own type; (ii) sympy, L1 = M0/(x - lam) entrywise, free of lam, and its determinant against the product; (iii) mpmath at
50 and 100 digits, 260 and 700 terms, iota5.py's connection with the column at the exponent computed from a null vector
of L1(lam), the recursion's M0(lam + n) = n L1(lam + n) being invertible for n >= 1. At s0 the determinant is itself
small, about 7 x 10^-12 at gam_C = 10, two E_K exponents lying close together (0 and -1.33 x 10^-6, the smallest
singular value 1.2 x 10^-6: the forty-seventh verifier, who reproduced the values at gam_C = 10 to 15 digits by a
Frobenius expansion in s and Taylor stepping), so that (iii)'s test is relative to the grid. Controls: in (i) the
five-dimensional matrix claimed to be his; in (ii) s0 claimed to carry slot 5 for slot 4; in (iii) the zero claimed, and
the leading coefficient taken off ker L1(lam), where the value is not the limit. []

*Deduced.*

 (a) (the structure at null infinity) The five-dimensional (5.26a) reads L == (2 r^(-3/2) d_0 r^(3/2) + r^-1 A_h) d_1 +
     r^-1 B_h: the leading part is the wave operator's, -2 d_t* rho (rho d_rho - 3/2) (10.25(i)), and A_h = A_0 + the
     perturbation's entries. His -- 2 d_1(r h_01), 2 d_1(r h_1a), 2 d_1(r h_ab), -(1/2) d_1(r h_ab) and -2 d_1(r h_01)
     in A_h, 2 d_1^2(r h) in B_h -- come from the Christoffel symbols of g_b + h and from (delta*_(g0) - delta*_g)
     delta_g G_g ((5.36), p. 96), each linear in d_1 h and r^-1 h with the r-weights of a Christoffel symbol, which do
     not see the dimension; and the dual metric's h-terms multiply d_0 or angular derivatives ((5.11)). With h at the
     five-dimensional radiative order r^(-3/2), not r^-1, every such entry is O(r^(-1/2)) against A_0: a coupling
     through the perturbation moves an exponent at null infinity up by 1/2. A scaling argument, not computed.
 (b) (Definition 5.2 and (5.42) in five dimensions) By (i)-(ii) the components decay at null infinity like r^(-3/2-z), z
     an eigenvalue of A_0 on their slot: pi_C h strongly, z = O(gam_C); pi_01 h with z = (1 - e_Ups) gam_Ups; pi_1/ h
     with z = gam_Ups; pi-slash_0 h with a radiation field at r^(-3/2); pi_11 h with z = 2 gam_Ups -- his rates with 3/2
     for 1, the diagonal being his. His positivity conditions (5.42) are unchanged.
 (c) (Proposition 5.14 and footnote 27 in five dimensions) The (7, 4) entry is his, 2 (1 - e_Ups) gam_Ups: it couples
     pi_01's leading term into the 11-component at its exponent 3/2 + (1 - e_Ups) gam_Ups, as his Lemma 11.15's proof
     has it at 1 + (1 - e_Ups) gam_Ups (p. 228). The (7, 6) entry is the perturbation's alone and by (a) half an order
     lower: pi-slash_0's radiation field reaches the 11-component at 3/2 + 1/2 = 2, the Coulombic order. So, on (a)'s
     reading, F_I,11 becomes 1 + (E^C_I u (3/2 + (1 - e_Ups) gam_Ups, 0) u (2, 0)). The iteration's quadratic sources
     likewise: the slowest at null infinity is the 11-component's (d_1 h)^2, r^-3 in five dimensions where his
     Definition 5.13(3) has r^-2, and it enters at the exponent 2 -- the mass aspect, whose law Theorem M(c) computes at
     past null infinity ((11.2)) and time reflection carries to future null infinity. His footnote 27's t*^-1 is the
     radiative and the Coulombic order at once in four dimensions; in five it is the Coulombic 2 alone.
 (d) (the radiative order at timelike infinity) A term r^(-x0) a(u) at null infinity, x0 = 3/2 + z with z in {0, (1 -
     e_Ups) gam_Ups, gam_Ups, 2 gam_Ups}, reaches iota+ at its own order only if a has a nonzero limit at iota+ cap I+:
     t*^-lam v^x = r^-x t*^(x - lam), so that limit is the v^(x0) coefficient, in ker L1(x0) by his (9.17), of a term
     t*^(-x0) G of the iota+ expansion. Let lam_1 be the least real part in the solution's iota+ expansion and suppose 0
     < lam_1 < 2. Its term solves the homogeneous model: the sources are quadratic, of iota+ order at least 2 lam_1; the
     data, O(r^(-2-eps_0)) (10.35(a)), give no incoming term below 2; and (c)'s forced terms enter at 2; and nothing
     below order 2 is fed into iota+ from K+, so that at v = oo the term carries E_K's exponents alone -- a reading: the
     zero energy and pure gauge states of 10.35(c)'s window enter at K+ order alpha_5 or are eliminated as his are. So
     it is a resonant state in 10.37's sense (D99) -- outgoing at v = 0, its v^lam coefficient, if lam_1 is an outgoing
     exponent, in ker L1(lam_1), which is what makes 10.37(b)'s boundary term at 0 vanish, so that (b) holds at such lam
     verbatim. 10.37(c)-(d) leave none with real part below 2 (det N_L has no root in (0, 1]; at lam_1 = x0, x0 - 1 =
     1/2 + z). Hence lam_1 >= 2, and every radiative coefficient a(u) tends to 0 at iota+ cap I+, like t*^(x0 - 2) at
     least, up to logarithms. (iii) computes the absence of such a state at the two exponents the (7, 4) entry couples,
     at moderate gam_C.
 (e) (alpha_5) So, on the readings of 10.37(c) -- the injectivity half on 10.24-10.25's, the index 0 half -- of (a), of
     polyhomogeneity at iota+ cap I+ as in his Propositions 9.4 and 9.11, of the decay that makes lam_1 > 0, and of
     (d)'s K+ side, the slowest iota+ term of the five-dimensional iteration is the mass aspect's t*^-2, forced at null
     infinity by (c), with 10.37's constraint-kind candidates above it: alpha_5 = 2 by both channels, and 10.35(a)'s
     conservative 3/2 + O(gam) is not attained. 10.35(c)'s window is [-2, 0], with the physical states s2, v2 and t2 at
     -2 and no companions.
 (f) (four dimensions) There the radiative order is the Coulombic one and his (1, 0) the mass's. Whether his E-sharp_+'s
     element (1 + (1 - e_Ups) gam_Ups, 0) is attained, the same descent would decide on his Lemma 8.4's roots in (0,
     eps_ind); his index sets are upper bounds, and this is not examined here.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII; printed page numbers): pp. 85 (after
Definition 5.2), 87 (Definition 5.4, section 5.2's opening, Lemma 5.6, (5.11)), 92-93 (Proposition 5.11 with
(5.25)-(5.28)), 96 ((5.36)-(5.39)), 97 ((5.40)-(5.42)), 98 (Definition 5.13, (5.43), Proposition 5.14 and its proof),
146 ((8.8)), 168-169 ((9.11), Definition 9.3 with (9.12)-(9.13), the remark on (1, 0) and the (7, 6) entry, Proposition
9.4, (9.17)), 223 (Proposition 11.6(1)); and, as 10.35 reads them, 27-29 (footnote 27), 228 (Lemma 11.15's proof), 248,
273.

*What this gives, and what it does not.* The five-dimensional (5.28) at the background, entry by entry, its
four-dimensional form reproduced: the same diagonal and the same (7, 4) coupling, four trace couplings changed, and the
couplings through the perturbation half an order lower. So the iteration's sources reach null infinity at the Coulombic
order, the mass aspect's, and the radiative order reaches timelike infinity only through a resonant state at its own
exponent, which the descent and the injectivity exclude below 2: alpha_5 = 2 on readings, both of 10.35(a)'s channels
closed on them, and the window [-2, 0]. Not done, and OPEN: (a)'s entries by computation (the five-dimensional (5.28)
with h); his Proposition 11.16 in five dimensions line by line; (e)'s readings -- 10.37(c)'s index 0 half,
polyhomogeneity at iota+ cap I+ in five dimensions, the data class, the decay lam_1 > 0, nothing below 2 fed from K+;
states at the radiative exponents at the record's gam_C, which (iii) reaches only at 10 and 100; four dimensions ((f)).
Nothing of this section is proved: Proposition 10.35 is computed, and (a)-(f) are deduced.

### 10.39 [Hin26] section 10.1 in five dimensions: the augmented zero energy operator (`aug5.py`; D102)

*The setting.* [Hin26] Theorem 10.1: "Let alpha_sf in R be such that alpha_sf + 3/2 in (0, eps_ind), and let delta >
alpha_sf + 3/2. Then the operator L_b is 2-admissible with sf-weight alpha_sf, sf-loss delta, and margin 1" (p. 199).
Near zero energy the nullspace of L-hat_b(0) (Proposition 8.11) is met by a finite rank augmentation, and "a naive
attempt" (10.5) adds the columns L-hat_b(sigma)(i sigma^-1 g-dot^Ups_b) and L-hat_b(sigma)(-sigma^-2 h_b,s1 + i sigma^-1
h-breve^1_b,s1), regular at sigma = 0 with values [L_b, t*] g-dot^Ups_b - (i sigma/2)[[L_b, t*], t*] g-dot^Ups_b (10.7)
and [L_b, t*] h-breve^1_b,s1 + (1/2)[[L_b, t*], t*](h_b,s1 - i sigma h-breve^1_b,s1) (10.8) (p. 201). "The issue,
however, is that these entries only have r^-2 decay" ((10.9a)-(10.9b)); "(Only terms arising from angular momentum
changes, [L_b, t*] g-dot^Ups_b(0, a-dot) in A^((3,0) u (3+E_ind)), have acceptable o(r^-2)-decay.) Therefore, they do
not lie in the target space of L-hat_b(0) in (8.22)", and "the tf-decay order 2 ... corresponds to L_b g-dot^Ups_b(1, 0)
having iota+-decay order 3 (see (2.26a)), which we must thus consider to be (borderline) unacceptable" (p. 202);
footnote 97: "[[L_b, t*], t*] in rho^2 C^oo(X)". Hence Lemma 10.3's improved states, built by inverting the iota+-normal
operator (his Proposition 9.11) and carrying chi_K c_b t*^-1 h^(0)_b,s0 and chi_K c'_b h^(<=1)_b,s1(S-dot log t*)
((10.13), p. 203), and Remark 10.8's sigma (log |sigma|) terms (p. 212); while the angular momenta, of "stronger
(namely, O(r^-2)- instead of O(r^-1)-) decay", take "g-dot^Ups,aug_b(0, a-dot) := chi_K g-dot^Ups_b(0, a-dot)"
((10.24a)), with "the index sets at I+ and K+ ... empty, and the index set at iota+ ... (4, 0) u (4 + E_ind)", and
"Lemma 10.4 generalizes similarly (with the same proof)" ((10.24b)-(10.24c), p. 207). Lemma 10.4 asks of the Fourier
transform f-hat of L_b applied to the augmentation tensor: (1) f-hat(0) in A^(2+eps_ind-eps), "and thus f-hat(0) in
H_b^(oo,1/2+eps_ind-eps)" with the asymptotically Euclidean density, f-hat(0) == the entry modulo L-hat_b(0) of
A^(-eps); (2) uniform bounds in H^((m;k),(r+alpha_sf+1, alpha_sf+2, 0)); (3) f-hat(sigma) - chi_zf f-hat(0) at zf-order
eps_ind - eps; (4) holomorphy in Im sigma > 0 (p. 204). Proposition 10.6 inverts the augmented zero energy operator from
H-tilde_b^(s0,alpha_sf) to H-tilde_b^(s0-1,alpha_sf+2), alpha_sf in (-3/2, -3/2 + eps_ind), by Proposition 8.11's index
0 and pairing with the dual states through Lemma 8.12; Proposition 10.7 gives the uniform bounds, "The only novelty
compared to [Hin26c, Theorem 9.41] is our handling of the augmentation terms" (pp. 208-209). In five dimensions the
states are one order faster and carry no logarithm (section 10.28(a)-(b)): g-dot^Ups(mu) and h-breve^1_s1 in A^((2,0) u
(2+E_ind)), g-dot^Ups(A) and h_s1 in A^((3,0) u (3+E_ind)); the asymptotically Euclidean density is r^3 |dr dg/|, and
alpha_sf + 2 in (0, eps_ind) stands for his alpha_sf + 3/2 (the shift n/2 = 2, section 10.24(d)). Here a bare 10.n is a
section of this record and a parenthesized (10.n) one of his equations.

**Proposition 10.36 (computed; exact).** On 4+1 Minkowski in (T, x), T = t - r, r = |x|, with L-bar = D Ric + (delta* +
E^C)(delta + E^Ups) G -- sbar5.py's E^Ups (trace weight 2/3, c_Ups = r^-1 dt) and E^C -- and four-dimensional Minkowski
(trace weight 1) as the control:

 (i) (the gauged states, his Proposition 8.9 on the model) The mass state r^-2 (dt^2 + dr^2) + delta* omega, omega =
     r^-1 (a dt + b dr), a = -2 gam_Ups (e_Ups + 2)/(2 e_Ups gam_Ups^2 + 1), b = (1 - 4 gam_Ups^2)/(2 (2 e_Ups
     gam_Ups^2 + 1)), and the rotation state r^-4 (dt (x) w + w (x) dt) + delta*(p r^-3 w), w = x^1 dx^2 - x^2 dx^1, p
     = -4 gam_Ups/3, are in the gauge and solve L-bar g-dot = 0, every parameter symbolic; with r^-1 log r dt and r^-1
     log r dr admitted beside them, their coefficients are 0. In four dimensions the mass state r^-1 (dt^2 + dr^2)
     needs omega = c log r dt + b dr, c = 4 gam_Ups (1 + e_Ups)/(4 e_Ups gam_Ups^2 + 1), b = (1 - 4 gam_Ups^2)/(4 e_Ups
     gam_Ups^2 + 1) -- the logarithm of his (8.19) -- and the rotation state r^-3 (dt (x) w + w (x) dt) takes p = -2
     gam_Ups, with no logarithm, as in his (8.20) (A1).
 (ii) (the entries, his (10.9)) [L-bar, T] g-dot = L-bar(T g-dot) is stationary, nonzero, and homogeneous of degree -3
     for the mass state and -4 for the rotation state, and [[L-bar, T], T] g-dot = 0. In four dimensions -2 and -3: his
     (10.9a)'s r^-2 and his angular momenta's (3, 0) (A2).
 (iii) (the cut-off states, his (10.14) and (10.24b)) For chi = chi(r/T), chi unspecified, L-bar(chi g-dot) = [L-bar,
     chi] g-dot is nonzero and homogeneous of degree -4 for the mass state and -5 for the rotation state in (T, x), so
     of iota+ order 4 and 5. In four dimensions 3 -- his "iota+-decay order 3 ... (borderline) unacceptable" -- and 4,
     (10.24b)'s (4, 0) (A3).

*Proof.* A1-A3 of aug5.py, exact. The gauge 1-forms are solved on the ansatz at two points and checked, with L-bar
g-dot, at the symbolic point (X1, 0, X3, 0): L-bar commutes with the rotations of R^4 and the reflections, the mass
state is invariant under all of them and the rotation state under the rotations of the planes 12 and 34 and the
reflection x^3 -> -x^3, and every orbit of these meets that set (four dimensions (X1, 0, X3)). (ii) and (iii) at (v_C,
e_C, gam_C, e_Ups, gam_Ups) = (1/3, 1/5, 10, 1/7, 3/2), at a point and at twice it -- in (ii) at T = 0 and 3, in (iii)
at T = r -- the ratio exact; nonzero there, so not identically. Controls: in (i) omega dropped, h claimed in the gauge,
and the four-dimensional mass state without the logarithm, which has no solution; in (ii) the five-dimensional mass
entry claimed of degree -2; in (iii) the five-dimensional mass state claimed of iota+ order 3. []

*Deduced.*

 (a) (his (10.9) in five dimensions) His Lemma 8.1 writes 2 L_b = -2 d_t* rho(rho d_rho - 1 - S) + L-hat_b(0) + Q
     d_t* - g^00 d_t*^2 with g^00 = g_b^-1(dt*, dt*) in rho^2 C^oo and Q in rho^3 Diff^1_b ((8.2a)-(8.2b), p. 145),
     so that [L_b, t*] at zero frequency is -rho(rho d_rho - 1 - S) + Q/2, in rho Diff^1_b, and [[L_b, t*], t*] =
     -g^00. In five dimensions the first term reads -rho(rho d_rho - 3/2 - S) (sections 10.25(i), 10.38(a)), and g^00
     is in rho^2 C^oo: g_b - g-bar in rho^2 C^oo (section 10.25(i)), g-bar^-1(dT, dT) = 0, and t* = t - r* (section
     10.28(iii)) with d(r* - r) = (1/f - 1) dr in rho^2 C^oo dr (section 10.25(i)). With 10.28's orders, [L_b, t*]
     g-dot^Ups(mu) and [L_b, t*] h-breve^1_s1 lie in A^((3,0) u (3+E_ind)), [L_b, t*] g-dot^Ups(A) in A^((4,0) u
     (4+E_ind)), and the double commutator terms in A^4 and A^5: every entry of (10.5) is in A^3, one order better
     than his. (ii) computes the mass and rotation entries' leading terms on the model, nonzero at the orders 3 and
     4, his orders reproduced in four dimensions; the boost entry's order is 10.28(a)'s, its correction vanishing on
     the model, where the boosts are Killing.
 (b) (the target space) A stationary tensor in A^q lies in H_b^(oo,l)(X, r^3 |dr dg/|) for every l < q - 2, since
     r^(2(l - q)) r^3 is integrable at infinity exactly then. So each five-dimensional entry, in A^3, lies in
     H_b^(oo,1-eps) for every eps > 0: in the target weight alpha_sf + 2 whenever alpha_sf + 2 < 1, which covers (0,
     eps_ind) once eps_ind <= 1 -- as the bound 10.24(a) computes for his (8.13) at l <= 12, eps_ind at most 7.3846 x
     10^-8 (the record's number, not his), makes it. His four-dimensional r^-2, against r^2 |dr dg/|, lies in
     H_b^(oo,l) for l < 1/2 only, below his target weights (1/2, 1/2 + eps_ind). His criterion, o(r^-2) decay, is the
     same in both dimensions -- the density's shift and the weights' shift are both n/2 -- and in five every entry
     meets it, as only his angular momenta's do in four.
 (c) (his (10.24a) for every state) So take g-dot^Ups,aug(b-dot) := chi_K g-dot^Ups(b-dot) for all seven b-dot =
     (mu-dot, A) and h^(<=1),aug_s1(S) := chi_K h^(<=1)_s1(S), h^(<=1)_s1 = t* h_s1 + h-breve^1_s1, as he does for the
     angular momenta. By his (10.14) -- [L_b, chi_K] in rho_+^2 Diff^2_b, and rho = r^-1 a joint defining function of I+
     u iota+ -- with chi_K g-dot^Ups(mu-dot) in A^(oo,(2,0) u (2+E_ind),(0,0)) and chi_K h^(<=1)_s1 in A^(oo,(2,0) u
     (2+E_ind),(-1,0)) (t* h_s1 losing one order of 10.28's 3), L_b of either lies in A^(oo,(4,0) u (4+E_ind),oo): iota+
     order 4 >= 3 + eps_ind, empty index sets at I+ and K+, his (10.12) without his Proposition 9.11 ((10.15)-(10.16));
     (iii) computes the mass state's order 4 on the model, against his 3; the boosts' is deduced, their states vanishing
     on the model. His Lemma 10.3 also gives the augmentation the correct asymptotics at I+ (p. 202); chi_K g-dot
     vanishes near I+, as his (10.24a) has it for the angular momenta, and whether his section 11 needs more there is
     open. Lemma 10.4 then runs as for (10.24c), "with the same proof": (1) f-hat(0) == the entry of (10.7), resp.
     (10.8), modulo L-hat_b(0) of A^(-eps), the error coming from (chi_K - chi_+) g-dot alone, the t*^-1 and log t*
     terms of (10.13) being absent; (2)-(4) as his, (10.18) with the iota+ order 4 for his 3 + eps_ind, so the tf-order
     3 for his 2 + eps_ind, and by (b) the target weight met. The naive (10.5) meets (1)-(4) as well, its entries being
     polynomials in sigma with coefficients in A^3 and A^4 and the zf-order of sigma [[L_b, t*], t*] g-dot being 1 >=
     eps_ind; whether his section 10.2 could use it in place of (10.26), whose columns are Fourier transforms of tensors
     on spacetime for the Paley-Wiener step, is not examined -- (10.24a)'s route needs no such question.
 (d) (his Proposition 10.6 in five dimensions) His proof: a kernel element (u, (mu-dot, A), S-dot) has L-hat_b(0)u +
     [L_b, t*] g-dot^Ups(mu-dot, A) + (1/2)[[L_b, t*], t*] h_s1(S-dot) + [L_b, t*] h-breve^1_s1(S-dot) + L-hat_b(0) h' =
     0, h' in A^(-eps); the eleven dual states are O(r^-3) (section 10.31(b)), where his "only requires
     O(r^(-1-eta))-decay", so the integrations by parts hold, and 10.32's pairings -- block triangular, determinant (-3
     pi^2)(-2 pi^2 mu)^6 (3 pi^2 mu/2)^4 up to his factor and sign (section 10.32(b)) -- give mu-dot = 0, A = 0, S-dot =
     0; then u lies in ker L-hat_b(0), the eleven-dimensional span of 10.32(c), and f*_1 in C_c^oo tensor R^7, f*_2 in
     C_c^oo tensor S_1 (S_1 four-dimensional) remove it. With the index 0 of 10.32(c) (dim ker = dim coker = 11, on
     10.33's reading near a = 0), the augmented zero energy operator is invertible from H-tilde_b^(s0,alpha_sf) to
     H-tilde_b^(s0-1,alpha_sf+2) for alpha_sf + 2 in (0, eps_ind).
 (e) (his Proposition 10.7 and Theorem 10.1 in five dimensions) His Proposition 10.7 uses Proposition 10.6, Lemma
     10.4(2)-(3) for the augmentation's (1, 2) and (1, 3) entries, and the structure (10.32) of L-hat_b(sigma) from
     Lemma 8.1 -- in five dimensions 2 i sigma rho(rho d_rho - 3/2 - S) + L-hat_b(0) - i sigma Q + g^00 sigma^2, by (a)
     -- with [Hin26c] Theorem 9.41 at n = 4 (section 10.20's reading); his section 10.2 then gives (10.3) through the
     contour (10.4) -- the Paley-Wiener representation of the proof of [Hin26c] Theorem 12.2, and the argument of
     [Hin26c] section 14.1 adapted (pp. 200-201, 212), both at n = 4, readings here, taken as he cites them -- whose
     shift uses mode stability (section 10.27) and [Hin26c] Theorems 9.5 and 9.16 (section 10.19). So, on the readings
     of 10.19-10.20 ([Hin26c] at n = 4, with its Theorem 12.2's proof and section 14.1), 10.24-10.25 (tf-admissibility,
     with min spec S-bar = 0 for his Remark 10.2), 10.26 (strong trapping admissibility), 10.27 (mode stability) and
     10.32-10.33 (Proposition 8.11's equality), and of (c)-(d), L_b is 2-admissible in five dimensions with sf-weight
     alpha_sf, alpha_sf + 2 in (0, eps_ind), and sf-loss delta > alpha_sf + 2: his Theorem 10.1, with his proof's loss
     (section 10.40 finds none in five dimensions).
 (f) (no logarithm in the augmentation) In five dimensions the augmentation tensors are chi_K times the states: no t*^-1
     h^(0)_s0 and no t* log t* term ((10.13)), so no sigma (log |sigma|) in the augmentation's columns ((10.40), Remark
     10.8), and his section 10.1.3 is not needed. Whether L-tilde_b(sigma)^-1 itself has logarithmic terms at sigma = 0
     is his section 11's question, not examined here.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII; printed page numbers): pp. 145 (Lemma 8.1,
(8.2a)-(8.2b), (8.5)), 199-205 (Theorem 10.1, (10.1)-(10.4), Remark 10.2, (10.5)-(10.9b), footnotes 96-97, Lemma 10.3
with (10.10)-(10.16) and its proof, Lemma 10.4 and its proof to (10.18)), 207-209 (its proof's parts (3)-(4), (10.23),
(10.24a)-(10.24c), Lemma 10.5, (10.26), Proposition 10.6 and its proof, Proposition 10.7 with (10.28)-(10.32)), 211-212
((10.36)-(10.41), Remark 10.8, section 10.2's opening, Lemma 10.9), 214 ((10.46)-(10.48), Lemmas 10.10-10.11).

*What this gives, and what it does not.* In five dimensions his zero energy augmentation needs no improved states: the
entries of the naive (10.5) decay like r^-3, one order better than his r^-2 and inside the target space, and his own
device for the angular momenta, (10.24a), serves every state, mass and boosts included; Proposition 10.6 follows from
10.32's pairings as his, and Theorem 10.1 -- 2-admissibility with alpha_sf + 2 in (0, eps_ind) -- holds on the readings
named in (e). The model computes the mechanism: the gauged mass state needs no logarithm in five dimensions, its entry
is of degree -3 where his is -2, and its cut-off state is of iota+ order 4 where his is the borderline 3. Not done, and
OPEN: [Hin26c] Theorem 12.2's representation and section 14.1 at n = 4; his Proposition 10.7 and section 10.2 line by
line in five dimensions (Lemma 10.9 onward, (10.56)-(10.59)); the boost entry and g^00 on Tangherlini and Myers-Perry by
computation ((a) reads their orders); the readings of (e); his section 11, and the I+ asymptotics of his Lemma 10.3 if
it needs them. Nothing of this section is proved: Proposition 10.36 is computed, and (a)-(f) are deduced.

### 10.40 [Hin26] section 10.2 in five dimensions: the proof of 2-admissibility, with no sf-loss (`lowfreq5.py`; D104)

*The setting.* His Theorem 10.1 demands, for a stationary-L_b-admissible order function s "with weights alpha_sf, -2 and
margin 1", that for f in H^((s;k),(alpha_sf+2,0))_3b;b "the unique forward solution u of L_b u = f satisfies u in
H^((s-1;k),(alpha_sf-delta,-2))_3b;b" ((10.3), p. 200), and his Remark 10.2 reads the margin at the outgoing radial set:
"the requirement is that s + alpha_sf < -1/2 - 1 (1 being the margin) at the outgoing radial set". The proof writes u
through the contour (10.4) and splits it ((10.50)) as u = u_hi + u_reg + g-dot + h_s1. The high frequencies are lossless
(Lemma 10.9: "losses will only arise from the low-energy behavior ... the order 2 (or rather 2 + delta) difference of
the sf-decay orders in (10.3) only arises in the low-energy theory", pp. 212-213), and so is the regular part (Lemma
10.10, p. 214). For the singular part, "Differentiation in t* removes these poles": Lemma 10.12 has "d_t* g-dot in
H^((s;k),(-1/2-eps,0))_3b;b" (10.51) and "d_t*^2 h_s1 in H^((s;k),(1/2-eps,0))_3b;b" (10.52). Its proof takes d_t*
g-dot^Ups,aug in A^(1,2,2) ((10.54)) and his split (10.57) of d_t*^2 h^(<=1),aug_s1 through (2.25a), "(Fu)|_(sigma in
+-[0,1]) in H^(k, min(beta_I,beta_iota)-eps, beta_iota-1, ((0,0),beta_K-1))_b" for beta_I >= beta_iota - min(beta_K, 1 -
eps) (p. 60) -- the scf order the least of the I+ and iota+ orders, the tf order the iota+ order less 1, against an
unweighted b-density -- to (10.56) and (10.59), and then, by [Hin26c] (13.30a), to "uniform ... bounds in
H^((m;k),(r,-1/2-eps,0)) ... (now using |dg_b|_X|) ...; the requirement on r here is that r < -1/2 at the zero section
R_out" (p. 216): his I+ order 1 makes the scf weight -1/2 against |dx|. Lemma 2.20, Plancherel, with the 3b sf weight
alpha' the tf weight and s' + alpha' the scf order (p. 55), then gives the membership "provided alpha' < -1/2 and s' +
alpha' < -1/2 at R_out" (pp. 215-216). Two integrations by Lemma 10.13, which needs u on {t* <= 1} in
H^((s;k),(beta-1,-l)) and d_t* u in H^((s;k),(beta,-l+1)) with l > 1/2, from (10.61)-(10.62), then give "u in
H^((s-1;k),(-3/2-eps,-2))_3b;b ... This proves (10.3) (since alpha_sf - delta < -3/2)" (p. 217): his sf-loss delta >
alpha_sf + 3/2 comes from the singular part alone. In five dimensions 10.39 makes the augmentation chi_K times the
states, of orders rho^2 (mass, boosts' h-breve) and rho^3 (rotations, h_s1) (section 10.28), cut off to vanish near I+,
and alpha_sf + 2 in (0, eps_ind) stands for his alpha_sf + 3/2.

**Proposition 10.37 (computed; exact).** On 4+1 Minkowski, with aug5.py's gauged states, and with four-dimensional
Minkowski as the control:

 (i) (the columns at zero frequency) For chi a piecewise cubic step, 1 on [0, 1/4] and 0 from 1/2, C^1 at its joints:
     d_T(chi(r/T) g-dot) is homogeneous of degree -(k + 1) and vanishes where r/T is outside (1/4, 1/2); at r = 2 its
     integral over T >= 1 is g-dot, and that of d_T^2(chi(r/T)(T h + h')) is h, for h, h' constant in T (for a ramp chi,
     C^0 only, -3h'/8). The mass state is of degree -2 (four dimensions -1), measured from its components, and h_s1 one
     order faster (section 10.28), so the zero-frequency values of the two derivative columns, the states g-dot and
     h_s1, lie in rho^alpha L^2(r^(n-1) dr) = r^-alpha L^2(r^(n-1) dr) exactly for alpha below 0 and 1 in five
     dimensions -- in four below -1/2 and 1/2, his (10.51) and (10.52) (W1).
 (ii) (the weights) The arithmetic of section 10.2, with the requirements at R_out read from (2.25a): a column of iota+
     order q and I+ order beta_I has tf weight q - 1 - n/2 - eps and scf weight min(beta_I, q) - n/2 - eps against |dx|;
     d_t* g-dot's weight is the lesser of its tf weight and its scf weight less s at R_out (at s' = s, s being below
     -3/2 - alpha_sf there), d_t*^2 h_s1's likewise at s' = s - 1, d_t*^2 u_sing's the lesser of the second and the
     first plus 1; then Lemma 10.13 twice from the initial weights alpha_sf + 1 and alpha_sf of (10.61)-(10.62) -- at
     the 598 rational points of the region alpha_sf + n/2 in (0, eps_ind), eps_ind in (0, 1], eps below both margins
     that a grid of five eps_ind, ten alpha_sf and twelve eps gives: four dimensions, beta_I = 1, -1/2 - eps, 1/2 - eps,
     the final weight -3/2 - eps and the loss alpha_sf + 3/2 + eps, his; five dimensions, no I+ term, -eps, 1 - eps
     (also at s' = s), the final weight alpha_sf and the loss 0 at every point; five dimensions with I+ terms at the
     radiative order beta_I = 3/2, alpha_sf + 1 - eps, alpha_sf + 2 - eps, the final alpha_sf - eps and the loss eps
     (W2).

*Proof.* W1-W2 of lowfreq5.py: (i) sympy, the integrals over the transition T in [4, 8] at r = 2, chi being 0 before it
and 1 after it, the joints checked C^1 so that the second derivative carries no delta there; the degree from the
components of aug5.py's mass state along a ray, at the parameter point of aug5.py; the weights by the integrability of
r^(2 (alpha - k)) r^(n-1) at infinity. (ii) exact rational arithmetic. Controls: in (i) the five-dimensional weight
claimed to be -1/2, and a ramp chi; in (ii) five dimensions with four-dimensional state orders and I+ order 1 (a loss),
four dimensions claimed lossless, and five dimensions claimed at alpha_sf + 1 and alpha_sf + 2 (D104's reading). []

*Deduced.*

 (a) (Lemmas 10.9-10.11 in five dimensions) The high-frequency piece rests on [Hin26c] Theorem 9.16(5)'s high-energy
     estimates with strong trapping admissibility (section 10.26) and on the margin of Remark 10.2, whose threshold
     quantity is min spec S-bar = 0 in five dimensions too (section 10.25); the regular part and the coefficients
     b-hat_1, S-hat_1 rest on Proposition 10.7 (section 10.39(e)). They are lossless as his: u_hi and u_reg lie in
     H^((s;k),(alpha_sf,0))_3b;b -- on those readings.
 (b) (Lemma 10.12 in five dimensions) With 10.39(c)'s augmentation, d_t* g-dot^Ups,aug = (d_t* chi_K) g-dot is supported
     where chi_K varies, in A^(oo,3,oo) (iota+ order 2 + 1; nothing at I+ or K+), and d_t*^2 h^(<=1),aug_s1 = 2 (d_t*
     chi_K) h_s1 + (d_t*^2 chi_K) h^(<=1)_s1 is in A^(oo,4,oo) -- his (10.57)'s h_1 alone, with no h_2 and no t*^-1 or
     log t* term; both are integrable in t*. By (2.25a) their Fourier transforms have scf orders 3 - eps and 4 - eps and
     tf orders 2 - eps and 3 - eps (unweighted b-density), so against |dx| = r^3 dr dS^3 scf weights 1 - eps and 2 - eps
     and tf weights -eps and 1 - eps (Proposition 10.37(i): the zero-frequency values are the states themselves, at
     these weights). With [Hin26c] (13.30a) at n = 4 relating r to the scf weight as his p. 216 does at n = 3 (section
     10.41: READ at n = 3, its shift at n = 4 computed) -- and his p. 206, "r + alpha_sf + 1 < 3/2 - eps" for the scf
     order 3 - eps -- and Lemma 2.20, d_t* g-dot lies in H^((s';k),(alpha',0))_3b;b for alpha' < 0 with s' + alpha' < 1
     at R_out, and d_t*^2 h_s1 for alpha' < 1 with s' + alpha' < 2 there. By the margin, s < -3/2 - alpha_sf < 1/2 at
     R_out, so both requirements hold at s' = s with alpha' = -eps and 1 - eps: the derivative columns carry the states'
     own weights, and the requirement at R_out does not bind. In four dimensions his I+ order 1 makes both scf weights
     -1/2, his "r < -1/2 at R_out", which at s' = s binds d_t*^2 h_s1 ((d)); I+ terms at the five-dimensional radiative
     order 3/2 would make them -1/2 too, and bind both (Proposition 10.37(ii)). (D104 took the requirement at R_out as
     his -1/2 here, and had alpha_sf + 1 and alpha_sf + 2: true, but weaker; corrected in D105.)
 (c) (Lemma 10.13 and the conclusion in five dimensions) For s = 0 Lemma 10.13 does not see the dimension -- it takes
     "|dt*| with any smooth weighted b-density on X", and its proof drops the angular variables, removes powers of r,
     and estimates in L^2(|dt dr|); for variable orders, "The case of general t*-translation-invariant orders s is
     treated exactly as in the proof of [Hin26c, Lemma 14.6]" (p. 217), a reading at n = 4. So d_t*^2 u_sing in
     H^((s-1;k),(1-eps,0)), with (10.62)'s d_t* u_sing in H^((s-1;k),(alpha_sf+1,0)) on {t* <= 1}, gives d_t* u_sing in
     H^((s-1;k),(alpha_sf+1,-1)), since alpha_sf + 2 < 1 - eps; with (10.61)'s u_sing in H^((s;k),(alpha_sf,0)) there,
     u_sing in H^((s-1;k),(alpha_sf,-2)) (Proposition 10.37(ii)): the integrations keep the initial weights, which set
     the bound. With (a), u = u_hi + u_reg + u_sing is in H^((s-1;k),(alpha_sf,-2))_3b;b: (10.3) holds with alpha_sf in
     place of alpha_sf - delta. So, on the readings of (a)-(c) and of 10.39, L_b is 2-admissible in five dimensions with
     sf-weight alpha_sf, alpha_sf + 2 in (0, eps_ind), and no sf-loss -- every delta >= 0 in (10.3), which [Hin26c]
     Definition 5.13 admits (section 10.41(a)). His loss is set by his states' decay, r^-1 (mass) and r^-2 (h_s1),
     through the tf weights -1/2 and 1/2 and the scf weight -1/2 of their I+ order 1; in five dimensions the states
     decay like r^-2 and r^-3 and the columns have no I+ term. Were I+ terms of the radiative order 3/2 added -- whether
     his section 11 needs I+ asymptotics is 10.39's open question -- the loss would be eps: every delta > 0 (Proposition
     10.37(ii)).
 (d) (a note on (10.52)) He writes that its conditions "hold for alpha' = 1/2 - eps and s' = s (see again Remark
     10.2)" (p. 216). As we read Remark 10.2, the margin gives s < -3/2 - alpha_sf at R_out, which is below 0 but not
     below -1 + eps, while s' + alpha' < -1/2 at s' = s would ask the latter; at s' = s - 1 it asks s < eps, which
     holds. His proof uses (10.52) only through (10.63), at (s - 1;k), so his conclusion is unaffected; in five
     dimensions (b)'s requirement at R_out holds at s' = s. A reading of his text, recorded and not more.
 (e) (downstream) His Corollary 11.10 and Theorem 11.12 carry the loss as delta > alpha_sf + 3/2, resp. delta > beta_+ -
     1/2 (p. 225); in five dimensions, on the readings of (c), delta may be taken 0 there (section 10.41(a)) -- his
     section 11 is not examined here.

*READ.* [Hin26] (alphaXiv, 2026-10-24; quotations transliterated to ASCII; printed page numbers): pp. 21 (the Fourier
transform, Figure 1.5), 54-55 (the 3b spaces, Definition 2.19, Lemma 2.20), 60 ((2.25a)-(2.26b)), 199-201 (Theorem 10.1,
(10.1)-(10.4), Remark 10.2), 206 (the proof of Lemma 10.4(2): the scf order and r at R_out), 212-217 (section 10.2:
Lemma 10.9 and its proof, (10.45), Lemmas 10.10-10.13, (10.46)-(10.64), the end of the proof of Theorem 10.1), 225
(Corollary 11.10, Theorem 11.12's opening).

*What this gives, and what it does not.* In five dimensions the proof of his Theorem 10.1 closes with no loss of decay
at spatial infinity: the derivatives that remove the poles carry the states' own weights, one order better than his; the
augmentation, cut off to vanish near I+, leaves the requirement at R_out slack; and the two integrations in t* keep the
initial weights. In four dimensions the computation returns his -3/2 - eps and his loss. Not done, and OPEN: [Hin26c]
Lemma 3.9, the microlocal part of Lemma 13.13, the 3b-calculus behind Lemma 14.6, and Theorems 9.5, 9.16 and 9.41 at n =
4 (readings, with 10.19-10.20; section 10.41 reads the rest at source); Lemma 10.9 line by line in five dimensions;
whether the boosts' columns meet (b)'s orders on Tangherlini by computation (section 10.39's OPEN); his section 11.
Nothing of this section is proved: Proposition 10.37 is computed, and (a)-(e) are deduced.

### 10.41 [Hin26c]'s readings behind 10.40, at source (`lowfreq5.py` W3; D106)

*The setting.* Section 10.40 rested on [Hin26c] at n = 4 for: the delta of its Definition 5.13; (13.30a), which turns
the scf order of a Fourier transform into the requirement at R_out; Lemma 14.6, which [Hin26]'s Lemma 10.13 cites for
variable orders; Lemma 3.9; and the Paley-Wiener argument of Theorem 12.2's proof and section 14.1, which [Hin26]'s
proof of Theorem 10.1 follows ("Following essentially the same strategy as in [Hin26c, section 14.1]", his p. 200).
[Hin26c]'s subject is Kerr in 3 + 1 dimensions -- "a blow-up of (-1, 1)_sigma x R^3" (p. 21), "r^-(alpha_sf+2) L^2(R^3,
|dx|)" with "alpha_sf := beta_sf - 3/2" (p. 20) -- though parts are written in general n: the scaled bounded geometry of
his section 3.1 is set "on an n-dimensional manifold" (p. 46), and the b-spaces of section 13.1 use "|dsigma/|sigma|
dx/<x>^n|" and S^(n-1) (p. 247). So each item is READ here at n = 3, and what this section adds is where n enters each.
[Hin26c] cites our [Hin26] as [Hin26b].

**Proposition 10.38 (computed; exact).** On R^n, n = 3 and 4, near infinity (|x| >= 1), r^-a lies in L^2(|dx|) iff a >
n/2 and in L^2(mu_b), mu_b = |dx|/|x|^n, iff a > 0: L^2(|dx|) = rho^(n/2) L^2(mu_b), rho = |x|^-1, the shift 3/2 at n =
3 and 2 at n = 4. (13.30a)'s rule -- the target's scf order at R_out below the source's less the shift, its tf order the
source's less the shift -- reproduces his printed instances at n = 3: p. 206's "r + alpha_sf + 1 < 3/2 - eps" for the
scf order 3 - eps and "r + alpha_sf < -1/2" for 2 - eps; p. 216's "r < -1/2" for (10.56)'s orders (1 - eps, 1 - 2eps),
the tf weight -1/2 - 2eps (his -1/2 - eps, eps renamed); and (10.59)'s (1 - eps, 2 - eps), r < -1/2 and 1/2 - eps -- the
rule's r < -1/2 - eps for every eps > 0 being his r < -1/2, eps arbitrary (p. 206). At n = 4 it gives section 10.40(b)'s
requirements r < 1 - eps and r < 2 - eps and its tf weights -eps and 1 - eps (W3).

*Proof.* W3 of lowfreq5.py: sympy, the integrals of r^(-2a) r^(n-1) and r^(-2a) r^(-1) over r >= 1 at a and a + 1/10,
bracketing the two thresholds; exact arithmetic for the rule, eps symbolic. Controls: the shift taken as 3/2 at n = 4;
the rule without the shift. []

*READ.* [Hin26c] (arXiv:2606.28008v1; alphaXiv, 2026-10-24; quotations transliterated to ASCII; printed pages):

 (a) (Definition 5.13, p. 106) "Let aleph >= 0 and alpha_sf in R, delta >= 0. We then call a stationary wave-type
     operator P_0 (Definition 5.1) aleph-admissible with sf-weight alpha_sf and sf-loss delta such the following holds
     for all stationary-P_0-admissible orders s with weights alpha_sf, -aleph and margin 0", with (1) trapping
     admissibility, (2) tf-admissibility "with weight alpha_sf + 3/2" (footnote 46: "In particular, alpha_sf + 3/2 lies
     in the indicial gap (beta_-, beta_+)") and (3) the estimate (5.22); and Remark 5.14 (p. 106): "The following
     relaxed version of Definition 5.13 is easier to verify in some settings (such as [Hin26b, Theorem 10.1]) ... we say
     that P_0 is aleph-admissible with sf-weight alpha_sf, sf-loss delta, and margin d_aleph >= 0 if for all
     stationary-P_0-admissible orders s with weights alpha_sf, -aleph and margin d_aleph, conditions (1)-(2) hold as
     stated, while (5.22) is replaced by u in H^((s-d_aleph;k),(alpha_sf-delta,-aleph))_3b;b". His p. 8: "The general
     assumption is that P_0 be aleph-admissible with sf-loss delta (Definition 5.13)"; pp. 106-107: "a suitable version
     of the linearized gauge-fixed Einstein operator is 2-admissible with sf-weight alpha_sf in (-3/2, -1/2) and any
     sf-loss delta > alpha_sf + 3/2".
 (b) ((13.30a), pp. 252, 255) "L^2(X, mu) = rho^(3/2) L^2(X, mu_b), rho = |x|^-1" for mu = |dx| and "mu_b := |dx|/|x|^3"
     (p. 252), with Lemma 13.13's r-bar_o := sup_(R_out) r; (13.30a) bounds the H^((s-1;k),(r+alpha_++1,
     alpha_tf+2,0))_(sc-b,|sigma|);b(X, mu) norm by the H^(k+l,(r-bar_o+alpha_++5/2+eps, alpha_tf+7/2,
     0))_(b,|sigma|)(X, mu_b) norm, "(The shift of 3/2 in the decay orders at rho^-1(0) = scf cup tf is due to the
     passage from mu to mu_b.)" (p. 255).
 (c) (Lemma 14.6 and its proof, pp. 264-265) for a t*-translation-invariant order s, beta in R and l > 1/2, "d_t* u =: f
     in H^(s,(beta,-l+1))_3b(M_0), t* >= 1 on supp u ==> u in H^(s,(beta-1,-l))_3b(M_0)" with "the Minkowskian volume
     density |dt dx|"; the case s = 0 "drop[s] the angular variables" and estimates in t at each r, "For general s, let
     A in Psi-tilde^s_3b(M_0) (see (3.27)) be elliptic with parametrix B ... we may arrange for A, B (and thus R and B')
     to be t*-translation-invariant". Lemma 3.9 (p. 59) is on X-tilde = R^3 with |dx| (p. 56). The class Psi-tilde_3b of
     (3.27) (p. 55) is built on the scaled bounded geometry structures of his section 3.1, "the scaled bounded geometry
     perspective introduced by the author in [Hin26c]" (pp. 45-46) -- his key for P. Hintz, *Pseudodifferential
     operators on manifolds with scaled bounded geometry*, Commun. Am. Math. Soc. 6 (2026) 153-243 (p. 277), not this
     record's [Hin26c] -- as against "the proof of the boundedness of a 3b-ps.d.o. on 3b-Sobolev spaces as proved in
     [Hin23d]" (p. 46), arXiv:2302.13803 (p. 277).
 (d) (Theorems 12.2 and 14.2) "box_g is 0-admissible with any sf-weight alpha_sf in (-3/2, -1/2) and sf-loss 0" (p.
     233), its Paley-Wiener argument pairing u-hat(sigma) with phi in C_c^oo(X^o) and shifting the contour from gamma =
     0 to gamma > 0, "For t* <= 1 < t_+, this tends to 0 as gamma -> oo" (p. 235), from the bounds of Theorems 9.41 and
     9.16 and the continuity of Theorem 9.5(6); and "Let alpha_sf in (-3/2, -1/2) and delta > alpha_sf + 3/2. Then the
     Hodge d'Alembertian (or tensor wave operator) box_g on 1-forms is 1-admissible with sf-weight alpha_sf and sf-loss
     delta" (p. 262), whose proof (pp. 265-267) takes the contour (14.19), the augmentation (14.13) with its entry in
     rho^3 C^oo (Lemma 14.3), the singular part a(t*) u_0 with u_0 in rho C^oo, and Lemma 14.5 "(with alpha = 1, m = 1,
     and beta_sf = -3/2 - eps, eps > 0)", whose condition (14.16), "max(beta_sf, s|_(partial R_(partial K^+,out)) +
     beta_sf) < (-m) + (-3/2 + alpha)" (p. 263), s at the outgoing radial set, gives (14.29), "chi_T a u_0 in
     H^((s;k),(-3/2-eps,0))_3b;b", and the loss; his p. 8: "The delta-loss at iota+ is more subtle; it arises for the
     1-form wave operator P = P_0 = box_(g_m,a) from the lack of decay of a term a(t*)u_0".

*Deduced.*

 (a) (Definition 5.13's delta) delta = 0 is admitted, so section 10.40(c)'s hedge goes: on the readings of 10.40, L_b in
     five dimensions is 2-admissible with sf-weight alpha_sf, sf-loss 0 and margin 1 in Remark 5.14's sense -- the form
     of [Hin26]'s (10.3), margin 1 and s - 1 -- for alpha_sf + 2 in (0, eps_ind). Definition 5.13(2)'s weight alpha_sf +
     3/2 is alpha_sf + n/2 at n = 3; in five dimensions it is alpha_sf + 2, the shift n/2 = 2 of section 10.23(ii) as
     applied in 10.24(d).
 (b) ((13.30a) at n = 4) Its statement sees the dimension through the density, as he says: at n = 4 the shift is 2
     (Proposition 10.38), which is what section 10.40(b) used, and the rule reproduces his four printed instances, at
     three places, at n = 3. The rest of Lemma 13.13's proof -- b-regularity giving scattering decay away from R_out, an
     elliptic parametrix in the scattering calculus (p. 252) -- is, at n = 4, a reading.
 (c) (Lemmas 14.6 and 10.13 at n = 4) For s = 0 the estimate is in t at each fixed (r, omega), so the density on X --
     r^(n-1) dr dS^(n-1), or [Hin26]'s "any smooth weighted b-density on X" -- passes through, and the lemma holds at
     every n; for general s it rests on an elliptic t*-translation-invariant parametrix in the class Psi-tilde_3b of
     (3.27), built on the calculus of his *Pseudodifferential operators on manifolds with scaled bounded geometry* (READ
     (c)), which his section 3.1 recalls "on an n-dimensional manifold" (p. 46); at n = 4 its 3b instance is a reading
     of that paper (not read here).
 (d) (the Paley-Wiener argument and section 14.1 at n = 4) The Paley-Wiener argument is in t* alone; at n = 4 it rests
     on Theorems 9.41, 9.16 and 9.5(6) there, the readings of 10.19-10.20, and on the invertibility of the spectral
     family for Im sigma >= 0, mode stability (section 10.27). Section 14.1 is the template section 10.40 follows: in it
     the loss comes from the zero energy state's decay through (14.16) -- u_0 in rho^1 against -3/2 = -n/2 at n = 3,
     after one integration in t* (m = 1) -- as 10.40(c) found the loss of [Hin26] section 10.2 to come from his states'
     decay.
 (e) (what remains) Of 10.40's [Hin26c] readings, these stay readings at n = 4: Lemma 3.9, the microlocal part of Lemma
     13.13, the 3b-calculus behind Lemma 14.6, and Theorems 9.5, 9.16 and 9.41 (10.19-10.20).

*What this gives, and what it does not.* Every [Hin26c] item section 10.40 cites is now READ at source at n = 3,
with where n enters it: 10.40's hedge on delta is gone, delta = 0 being admitted, and the shift in (13.30a) at n = 4
is computed. Not done, and OPEN: the readings of (e) at n = 4; his scaled bounded geometry paper (READ (c)); his
section 11. Nothing of this section is proved: Proposition 10.38 is computed, and (a)-(e) are deduced.

### 10.42 [Hin26] section 11.1 in five dimensions: admissibility and forward solutions (`cone5.py`; D108)

*The setting.* His section 11 linearizes around g = g_(b0,b,-S) + h, "g_(b0,b,-S) := (1 - chi_K) phi*_(-S) g_b0 + chi_K
g_b" (11.1) (p. 218), with h in index sets E+ at iota+ subject to "(1, 0) in E+, min Re E+ >= 1, jE+ subset E+ for all j
in N" (11.6) and remainder weights "3 + eps_I, 3 + eps_+, 2 + eps_K" (11.10) (pp. 220-221): "The requirement (1, 0) in
E+ ensures that smooth decaying perturbations are allowed as far as their behavior at (iota+)^o is concerned" (p. 221),
for "the two metrics g_b0 + h and g_b0,b,0 = chi_K g_b + (1 - chi_K) g_b0 + h differ near (iota+)^o by chi_K (g_b -
g_b0) in rho_+ C^oo" (Remark 11.7, p. 224). Lemma 11.5 puts h in the e3b class "provided that l_I < min(2 gam_Ups, 1/2),
l_+ < 1, l_K <= 2 + eps_K" (11.14), Sobolev embedding giving "h in C^(k-3,(1,1-eps,2+eps_K))" (p. 222); Proposition 11.6
records the structure (11.17)-(11.18) of L_(g,g0), "the computations in section 5.2 ... carry over with only notational
changes from a neighborhood of I0 cup I+ to a neighborhood of I+ cup iota+" (p. 223); and Corollary 11.9's proof: "Since
g_(b0,b,-S) - g-bar is a smooth section of S^2 T* and of class rho_+ C^oo near (iota+)^o, we have P(g0, g0) in rho_+^3
C^oo there. Since (3, 0) subset E+ + 2 by (11.6), this term lies in the space in (11.20)" (p. 225). Corollary 11.10:
L_(g,g0) "is admissible (relative to L_b) of class ((0; k - 5), (2l_I, l_+, l_K)) in the sense of [Hin26c, Definition
5.18] for all l_I < min(2gam_Ups, 1/2), l_+ in (delta, 1), and l_K in (2, 2 + eps_K]", "The weights l_+ in (delta, 1)
and l_K > 2 satisfy the conditions in [Hin26c, (5.23)]" (p. 225), which read "l_I in (0, 1/2], l_+ > delta, l_K > aleph"
([Hin26c] p. 109), within [Hin26c] Definition 5.15's "l_I in [0, 1/2], l_+ in [0, 1], l_K >= 0", "The requirements 2l_I,
l_+ <= 1 are made for convenience" (p. 107). Theorem 11.12 states [Hin26c] Theorem 11.1 "in the form using unweighted
b-densities": "Let beta_+ in (1/2, 1/2 + eps_ind) and beta_I in (beta_+, 1); fix delta > beta_+ - 1/2", f in H^(k+d,
beta_I+1, beta_++2, 1/2)_b, "u in H^(k, beta_I, beta_+-delta, -3/2)_b" (11.22) (pp. 225-226); [Hin26c] p. 228: "mu_b :=
rho_I^3 rho_+^4 rho_K |dt dx| ... (in which case rho_I^3 rho_+^4 rho_K = 1/(t* r^3))" and (11.5) "beta_I = alpha_I +
3/2, beta_+ = alpha_+ + 2", from Theorem 11.1's "alpha_I < -1/2 + S-bar ... alpha_+ < alpha_I - 1/2" (pp. 228, 201).

**Proposition 10.39 (computed; exact).** On Minkowski space R^(1,n), n = 4, with n = 3 as the control:

 (i) (the densities and the weights) With [Hin26c]'s (11.4), rho_I = t*/(t* + r), rho_+ = (t* + r)/(t* r), rho_K =
     r/(t* + r): 1/(t* r^n) = rho_I^n rho_+^(n+1) rho_K, so the unweighted b-density shifts the weights at (I+, iota+,
     K+) by (n/2, (n + 1)/2, 1/2) -- (3/2, 2, 1/2) at n = 3, his (11.5), and (2, 5/2, 1/2) at n = 4. alpha_sf + n/2 in
     (0, eps_ind) is beta_+ in (1/2, 1/2 + eps_ind) in both dimensions, and his delta > beta_+ - 1/2 is Theorem 10.1's
     delta > alpha_sf + 3/2. A radiation field r^-((n-1)/2) is of I+ order (n - 1)/2 against mu_b and -1/2 against |dt
     dx| in both (rho_I rho_+ = 1/r) (C1); so [Hin26c]'s threshold alpha_I < -1/2 + S-bar ((10.2)), on the reading
     that it stands as printed at n = 4 -- a reading, not computed here -- is beta_I < (n - 1)/2 + S-bar: with min spec
     S-bar = 0, his 1 at n = 3 and 3/2 at n = 4.
 (ii) (the background differences at iota+) Homogeneity along rays in the cone, in Cartesian components: a change of
     mass, r^-(n-2) k (x) k (Kerr-Schild, k null), is of degree -(n - 2); of rotation, r^-n (dt (x)_s w), w = x^1 dx^2 -
     x^2 dx^1, of degree -(n - 1); a boost, L_X of the mass term, X = t d_x1 + x^1 d_t, of degree -(n - 2) -- each
     nonzero. So iota+ orders 2, 3 and 2; at n = 3, 1, 2 and 1, his rho_+ C^oo (C2).
 (iii) (the patched background's curvature) For g = eta + M(t, r) r^-(n-2) (dt + dr)^2, M = mu_0 + d F(r/t), F
     arbitrary: Ric = 0 for F constant; its part linear in the deviation, d F's, is homogeneous of degree -n, nonzero,
     and vanishes where F is constant; its quadratic part (mu_0 d, d^2) is homogeneous of degree -(2n - 2); there is no
     cubic part. So the curvature of a cut-off interpolation between two masses is of iota+ order 4, supported where the
     cut-off varies; at n = 3 order 3, his Corollary 11.9 (C3).

*Proof.* C1-C3 of cone5.py: sympy, exact. (i) the identity of densities simplified to 0, the weights in rational
arithmetic at 72 points of (0, eps_ind); (ii) each component's ratio along the ray lam p, p = (7, 1/2, 1, ...), equal
to lam^deg with one deg for all nonzero components; (iii) the Ricci tensor of the Kerr-Schild metric with M(t, r)
generic, by its Christoffel symbols with the exact inverse eta^-1 - H k# k#, in the frame (dt, dr, r dS^(n-1)), then M
= eps(mu_0 + d F(r/t)) and the eps^k pieces tested for homogeneity under (t, r) -> lam (t, r). Controls: the shifts
claimed dimension-free; the five-dimensional mass change claimed of order 1; its curvature claimed of order 3. []

*Deduced.*

 (a) (Definition 11.3 in five dimensions) The background differences his E+ admits for g_(b0,b,-S) and Remark 11.7 -- a
     change of mass or rotation, chi_K (g_b - g_b0), and the cut-off boost -- are of iota+ order 2, 3 and 2 (Proposition
     10.39(ii)), and the iteration's slowest iota+ term is the mass aspect's t*^-2 (alpha_5 = 2, section 10.38, on
     readings). So his (11.6) becomes (2, 0) in E+, min Re E+ >= 2, jE+ subset E+: every order there one above his, on
     10.38's readings, which are also what keeps the radiative 3/2 out of E+ (his Proposition 11.16 in five dimensions,
     10.38's OPEN; without them min Re E+ = 3/2 + (1 - e_Ups) gam_Ups, and (b)-(e) still hold: 10.44(e)).
 (b) (Lemma 11.5) With min Re E+ = 2, Sobolev embedding puts h at 2 - eps at iota+ where his is 1 - eps, so (11.14)'s
     l_+ < 1 relaxes to l_+ < 2 and [Hin26c] Definition 5.15's convenience bound l_+ <= 1 is the one that binds; l_K <=
     2 + eps_K is unchanged, and l_I rests on E^C_I and gam_Ups at I+, his section 5 at n = 4 (10.38's readings).
 (c) (Proposition 11.6, Proposition 11.8, Corollary 11.9) The structure (11.17)-(11.18) rests on his section 5.2's
     computation, which 10.38 carries to five dimensions at h = 0 (its h-terms OPEN there), with the error classes at
     iota+ shifted as E+ is. P(g0, g0) = Ric(g_(b0,b,-S)), supported on supp d chi_K, is of class rho_+^4 C^oo near
     (iota+)^o -- Proposition 10.39(iii) for a change of mass; for rotation and boost by his own count, not computed
     here: their differences are of orders 3 and 2 (Proposition 10.39(ii)), so g - g-bar in rho_+^2 C^oo and d in rho_+
     V_b give Ric in rho_+^4 C^oo -- and (4, 0) in E+ + 2: his conclusion, one order higher.
 (d) (Corollary 11.10) [Hin26c] (5.23) asks l_+ > delta and l_K > aleph; with sf-loss 0 (section 10.41(a)) and aleph = 2
     (the boosts' t* growth, sections 10.28-10.29; the 2-admissibility deduced on readings in sections 10.39-10.41(a)),
     L_(g,g0) is admissible relative to L_b of class ((0; k - 5), (2l_I, l_+, l_K)) for l_+ in (0, 1) and l_K in (2, 2 +
     eps_K] -- on the readings of [Hin26c] Definitions 5.15 and 5.18 at n = 4 and of (b)'s l_I.
 (e) (Theorem 11.12) [Hin26c] Theorem 11.1 at n = 4, a reading, in the unweighted b-density with the shifts (2, 5/2,
     1/2): for beta_+ in (1/2, 1/2 + eps_ind) -- his interval, alpha_sf + 2 in (0, eps_ind) -- beta_I in (beta_+, 3/2)
     (his alpha_+ < alpha_I - 1/2 is beta_+ < beta_I in both dimensions) and sf-loss 0, the forward solution of L_(g,g0)
     u = f, f in H^(k+d, beta_I+1, beta_++2, 1/2)_b, lies in H^(k, beta_I, beta_+, -3/2)_b: his (11.22) with delta = 0
     and the top of beta_I at 3/2, the radiation field's order. The tame estimate (11.23) is his, with delta = 0.

*READ.* [Hin26] (alphaXiv, 2026-10-24; printed pages): pp. 218-226 (section 11's opening, (11.1)-(11.11), Definition
11.3, Remark 11.4, Lemma 11.5, Proposition 11.6, Remark 11.7, Proposition 11.8, Corollaries 11.9-11.10, Remark 11.11,
Theorem 11.12, Remark 11.13), 231 (section 11.3's opening), 244 ((11.85)), 263 ((11.148)-(11.151)). [Hin26c] pp. 107,
109 (Definitions 5.15 and 5.18), 201 ((10.2)), 228 (Theorem 11.1, (11.4)-(11.6a)).

*What this gives, and what it does not.* His first step towards decay, in five dimensions: the index sets at iota+ one
order up, the patched background's curvature at rho_+^4, the dynamical operator admissible with l_+ in (0, 1), and
forward solutions that lose at timelike infinity only the two orders the operator takes -- his t*^(3/2) growth in
spatially compact sets is the K+ weight -3/2, unchanged, aleph = 2 being the boosts'. Not done, and OPEN: [Hin26c]
Theorem 11.1 and Definitions 5.15 and 5.18 at n = 4 (readings); the h-terms of (5.28) in five dimensions and his
Proposition 11.16 there (10.38's OPEN), and with them E^C_I, gam_Ups and l_I at I+; his sections 11.2-11.8. Nothing of
this section is proved: Proposition 10.39 is computed, and (a)-(e) are deduced.

### 10.43 The class in [Hin26]'s construction: his states, parameters and steps that survive (`class5.py`; D111)

The settling the paper needs is stability within the T^2-mirror class: G = O(2) x O(2) acting on R^4 = R^2 x R^2 -- the
rotations of the (x1, x2) and (x3, x4) planes and the reflections x2 -> -x2, x4 -> -x4 -- and trivially in t. [Hin26]'s
Steps 2, 4 and 5 remove a boost, the black hole's rotation and centre-of-mass motions, and his section 12 carries them
as parameters. This section computes which of his generators and harmonic types are G-invariant, and deduces that his
construction may be run on G-invariant objects alone.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; quotations transliterated to ASCII): pp. 63-64,
Definition 2.27, "S_l := ker(Delta - l(l + 1))", "V_l := {*dS : S in S_l}", 1-forms and 2-tensors "of scalar type l" and
"of vector type l"; p. 219, the steps of section 11 (Step 2: "we shall counteract this term by boosting the initial Kerr
black hole"; Step 4: "changes of the final black hole parameters as well as a logarithmic plus constant modulation of
its center-of-mass"; Step 5: "t*^(-alpha)-shifts in the center-of-mass"); p. 301: "The only remaining independent terms
are those that, in linearized theory, are related to the zero energy bound states of L_b ... These are the final black
hole parameters b, the boost parameter S, and the center-of-mass shift S^(0)_1", and Definition 12.1, (12.11)-(12.12c):
U = (b - b0, S, S^(0)_1, (u^0_lam, f_lam), S_rem, b_rem, V_1,rem, (S^(0)_l,rem)_(l=0,2),
(S^(-lam^Ups_sl,1+1)_l,rem)_(l=0,1), h-tilde), "S, S^(0)_1 in S_1"; p. 302, (12.14)-(12.16), the components of p-vec and
q-vec each in some S_l or V_l (l <= 5) or in R^4; p. 310, Theorem 12.3; p. 312, Theorem 12.8, "there exist U' in D^oo
such that D_Phi(U) P(D_U Phi(U')) = f" with tame estimates; pp. 321-322, the proof of Theorem 13.1: "We use the simple
Nash-Moser iteration scheme of Saint Raymond [SR89] for the map P o Psi", with its assumptions (1)-(4) checked there.

**Proposition 10.40 (computed; exact).** With G as above:

 (i) (the generators) Of the fifteen Killing fields of 4+1 Minkowski -- d_t, d_i, t d_i + x^i d_t, x^a d_b - x^b d_a --
     the G-invariant combinations are the multiples of d_t; under T^2 alone, without the reflections, d_t and the
     rotations of the two planes. Tangherlini's mass change mu' r^-2 (dt + dr)^2 is G-invariant (C1).
 (ii) (the harmonics of S^3) For l <= 8: one G-invariant scalar harmonic at each even l, none at odd l; no G-invariant
     smooth divergence-free 1-form at any l, the invariant 1-forms being a(theta) d theta, divergence-free only for a =
     C/sin 2 theta (under T^2 alone there are two at each odd l, cos^2 theta d phi1 and sin^2 theta d phi2 at l = 1);
     and one G-invariant transverse traceless tensor harmonic, (rough Laplacian + l(l + 2) - 2) T = 0, at each even l >=
     2, none at odd l (under T^2 alone two at each even l >= 2) (C2, with C3's upper bounds).

*Proof.* C1-C3 of class5.py: sympy, exact, and C3 exact modulo a prime. (i) invariance as vanishing brackets with the
two plane rotations and invariance under the two reflections, a linear system in the fifteen coefficients whose solution
space is computed; the mass change by its Lie derivatives and pullbacks. (ii) scalar: G-invariant polynomials of degree
l are polynomials in x1^2 + x2^2 and x3^2 + x4^2, their harmonic ones counted by rank; vector: on S^3 = {(cos theta e^(i
phi1), sin theta e^(i phi2))} the reflections reverse d phi1 and d phi2, so an invariant 1-form is a(theta) d theta, and
its divergence-free condition is solved exactly; tensor: the invariant ansatz T = A d theta^2 + B cos^2 theta d phi1^2 +
C sin^2 theta d phi2^2, C = -A - B (the cross terms are reflection-odd), A and B polynomials in cos^2 theta of degree
floor(l/2) + 1, smooth at the axes, the divergence and the rough Laplacian from the round metric's Christoffel symbols
(their off-diagonal parts vanish identically), each equation imposed exactly at 48 rational points of the circle -- more
than twice its degree as a trigonometric polynomial (the fifty-second verifier measured at most 14 at l = 8; the
instrument asserts the bound) -- and the solution space counted by rank. The ansatz exhibits its solutions, so C2's
counts are lower bounds. C3 counts the same harmonics a second way, as homogeneous degree-l polynomials on R^4
(harmonic; for 1-forms divergence-free with x.V = 0; for tensors divergence-free, traceless, with x.H = 0), invariance
as linear conditions, by rank modulo 2^31 - 1, which bounds each count from above (a TT eigentensor of level l extends
to R^4 as r^l T(x/r), harmonic by the eigenvalue equation and bounded at 0, so a homogeneous polynomial,
G-equivariantly; D121); the totals are SO(4)'s (l + 1)^2, 2 l (l + 2), 2 (l - 1)(l + 3), and the G-invariant counts meet
C2's, which are therefore exact. Controls: T^2 alone (three generators; two invariant divergence-free 1-forms at each
odd l and two TT tensors at each even l >= 2, C3); the eigenvalue moved by one (no tensor harmonic); x.H = 0 dropped
(C3's totals break). [] []

*Deduced.*

 (a) (equivariance) The gauge-fixed Einstein operator P(g, g0) = Ric(g) - delta*_(g0,E^C) Ups^(E^Ups)(g, g0) is natural
     under diffeomorphisms carrying its modifications along; its modifications here are built from dt and dr with radial
     coefficients (the damping 1-form of 10.14, the horizon modification c_H = -(1/2) chi(r) dr of 10.15, the trace
     weight 2/(D - 2)), so they are O(4)-invariant, and so are Tangherlini, the cut-off chi_K = chi_0(t*) chi_1(r/t*)
     (p. 318), the cut-offs chi_- and chi_+ of his sections 11.8 and 12 (functions of t*; pp. 277, 292) and his t*.
     Hence for G-invariant g0 and h, P and its linearizations commute with G; forward solutions with G-invariant sources
     are G-invariant, by uniqueness; and the Haar mean Pi over the compact G is a bounded projection (of norm 1 for
     G-invariant norms) on every weighted b-Sobolev space of [Hin26c]'s compactification, G acting by isometries that
     preserve t*, r and so every boundary defining function.
 (b) (the parameters) Every component of U, p-vec and q-vec lies in a representation of G: the final parameters b = (m,
     A), A in so(4) (10.36), with A -> R A R^-1; the boost S and the centre-of-mass shift in S_1; the remainders in S_l
     and V_l, harmonics of S^3 in five dimensions. An invariant A commutes with both plane rotations, so A = a J_12 + b
     J_34, and the reflections reverse J_12 and J_34: A = 0. By (ii) the G-fixed S_l vanish at odd l and are
     one-dimensional at even l, and the G-fixed V_l vanish. So in the class S = 0, S^(0)_1 = 0, b = (m, 0), S_rem = 0
     and V_1,rem = 0; of the S_l and V_l components of (12.11)-(12.15) only those in S_l with l even remain, with the
     tensor type's at even l >= 2 where the five-dimensional lists carry it; b - b0 and b_rem keep their mass component
     (in R^4 in his (12.12a) and (12.12c), R^7 in five dimensions); and (u^0_lam, f_lam) and h-tilde are restricted to
     their G-fixed parts.
 (c) (his steps) Step 2 (section 11.4) reduces to Proposition 11.20 with S-dot = 0: its t* h_(b,s1)(S-dot) term, the
     boost parameter and augmentation #1 (section 11.4.2, Definition 11.25) are G-invariant only when zero, while the
     improved remainder the proposition proves is still used (10.45(b)). Step 4 (section 11.6) reduces to the change of
     the mass, the centre-of-mass motion lying in S_1. Step 5 (section 11.7) reduces to Proposition 11.51 with no S_1
     shifts and no centre-of-mass modifications (10.46(a)). Step 6 (section 11.8) remains with its gauge modifications
     restricted to (b)'s components (10.46(b)), and Steps 1 and 3 as his.
 (d) (the zero energy states) Of the eleven kernel states (10.28) and the eleven dual states (10.31), each the image of
     a Killing field under a construction that commutes with O(4) (each step a unique solution, 10.29(a)), only the mass
     state and the time translation's dual state are G-invariant, by (i); of 10.29's generalized states, part (1)'s (s0)
     alone; of 10.30's classes, the scalar ones at even l; of the physical states (10.34) and the window (10.35), which
     needs l = 2, the scalar s2 and the tensor t2, one each, and no vector v2. The constructions on the rotations and
     boosts -- 10.29(2)-(3), 10.31's rotations at first order in the spin, 10.36's family at nonzero spin, 10.32's
     angular momentum and centre-of-mass pairings -- are not needed in the class.
 (e) (the iteration in the class) His construction of Phi (section 12.2) solves at each step a linear problem whose
     right side is G-invariant when its inputs are; replacing each solution by its G-average, again a solution, gives
     Phi on the G-fixed data D^oo_G with G-invariant output, satisfying (12.31) by his proof. For G-invariant U and f,
     Theorem 12.8's U' is read off from the forward solution of Corollary 11.66, G-invariant by (a), and lies in D^oo_G
     if the read-off commutes with G; and his smoothing operators S_theta may be replaced by Pi S_theta Pi, with the
     same estimates by (a). [SR89]'s scheme then runs on the closed subspaces D^oo_G -> B^oo_G. The scheme is run for P
     o Psi with Psi(U) = (chi_-(t*) h_(-S), 0, 0) + Phi(U) ((12.34), (13.6), as the fifty-second verifier read them; to
     be READ at A7), and its assumption (3) carries D_S(h_(-.))(S'): in the class S = S' = 0, so that term is absent,
     and h_0 is G-invariant when the data are and the solution of (13.5) is unique, which A8 checks. So [Hin26]'s
     argument in five dimensions needs only the G-fixed objects of (b)-(d) -- deduced, on the readings already named for
     each step and on the reading that his read-off in Theorem 12.8's proof commutes with G, which A7 checks (ROUTES
     4.44); deduced in 10.47(c)-(e).

OPEN: everything ROUTES 4.44 lists after A1; (e)'s reading of Theorem 12.8's proof (A7), for which a second route is
noted: if his Phi is G-equivariant on all of D^oo -- each of its steps unique -- the G-average of U' solves (12.35) with
the same estimates and the read-off needs no reading; (e)'s Psi and h_0 (A7, A8). Labels: computed (class5.py C1-C3;
exact, C3 modulo a prime); deduced ((a)-(e)); READ ([Hin26] pp. 63-64, 219, 277, 292, 301-302, 310, 312, 318, 321-322);
nothing proved.

### 10.44 [Hin26] section 11.2 in five dimensions: the structure at I+ and its formal solutions (`iplus5.py`; D112)

His Lemma 11.15 and Propositions 11.14 and 11.16 integrate the I+ normal operator component by component with b-ODE
lemmas. This section computes the five-dimensional normal operator's leading part, exponents and exceptional terms, and
deduces the three statements in five dimensions.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): p. 47, b-Sobolev spaces on [0, oo)^k
x R^(n-k) x S, "S is a closed (i.e., compact, no boundary) smooth manifold"; pp. 49-50, Lemma 2.12, "We work on [0,
1)_x x H where H is a compact manifold with corners"; pp. 57-58, Lemmas 2.22 and 2.23 on "[0, 2) x [0, 2) x (-2, 2)^d";
p. 86, Definition 5.3(3) and (5.5)-(5.8); p. 181, Lemma 9.14 and (9.47); p. 220, Definition 11.3; pp. 224-226,
Proposition 11.8, Theorem 11.12; pp. 226-230, Proposition 11.14, (11.26) "rho_I^-1 rho_+^-2 L = L_0 + L~, L_0 = -(rho_I
d_rho_I - (I + A_h))(rho_I d_rho_I - rho_+ d_rho_+) + rho_+^-1 B_h", Lemma 11.15 and its proof (the (7, 6) term
"(A_h)_7,6 = -1/2 d_1(r h_ab)" producing (1, 0), the (7, 4) term (1 + (1 - e_Ups) gam_Ups, 0), "using l_I <= 3 + eps_I
< 1 + (1 - e_C)(1 - v_C) gam_C"), Proposition 11.16 with (11.33a)-(11.33b) and Steps 1-3 of its proof, (11.34) "L~ in
rho_I Diff^2_b"; p. 235, the coordinates "rho_I = t*/r ... rho_+ = 1/t* (cf. (3.4e))".

**Proposition 10.41 (computed; exact, but for (ii)'s 2 I0 - 1, which rests on 10.38(a)).**

 (i) (the leading part) For the wave operator of R^(1,n) on u(t*, r) Y, Y a harmonic of S^(n-1) with eigenvalue -kappa,
     in rho_I = t*/r, rho_+ = 1/t*: rho_I^-1 rho_+^-2 (-box/2) = -(rho_I d_rho_I - (n - 1)/2)(rho_I d_rho_I - rho_+
     d_rho_+) + rho_I R, R = -(a^2 - (n - 2) a - kappa)/2 on rho_I^a rho_+^b, angular term and potential in R: his I = 1
     at n = 3, and 3/2 at n = 4 (P1).
 (ii) (the bookkeeping) The five-dimensional A_0 of 10.38(i) is lower triangular with his diagonal; the 11-component's
     exceptional I+ exponents are 2 I0 - 1, from the (7, 6) coupling's I+ order I0 - 1 by 10.38(a)'s scaling argument (a
     reading), and I0 + (1 - e_Ups) gam_Ups, from A_0's (7, 4) entry (computed): 2 and 3/2 + (1 - e_Ups) gam_Ups at I0 =
     3/2, his 1 and 1 + (1 - e_Ups) gam_Ups at I0 = 1 from his (5.28); his Steps' coefficients are (2 - (3/2 + 2
     gam_Ups)) = (1 - 4 gam_Ups)/2, zero only at gam_Ups = 1/4, and -(1 + e_Ups) gam_Ups; and z - 3/2 - A_0 is
     invertible for 3/2 + 2 gam_Ups < Re z < 3/2 + (1 - e_C)(1 - v) gam_C, at the record's point (v, e_C, gam_C, e_Ups,
     gam_Ups) = (1/2, 1/102400, 10^6, 1/100, 1/100) for 38/25 < Re z < 63999567/128 = 499996.6171875 (P2).
 (iii) (Proposition 11.16's Steps 1-2) L_0 with the full A_0, on rho_I^z U(rho_+) e_11, z = 2 and 3/2 + (1 - e_Ups)
     gam_Ups, is (4 gam_Ups - 1)/2 (z - rho_+ d_rho_+) U e_11 and (1 + e_Ups) gam_Ups (z - rho_+ d_rho_+) U e_11, no
     other component appearing, nonzero at the point (P3).

*Proof.* P1-P3 of iplus5.py: sympy, exact. (i) the operator applied to rho_I^a rho_+^b Y with a, b, kappa symbolic,
t* = t - r, and the difference from the claimed leading part shown to carry a factor rho_I with polynomial
coefficients; (ii) scri5.py's five528() and his528() (10.38), the exponents and coefficients read from their entries,
the gap at lin5.py's point; (iii) L_0 with scri5.py's full A_0 applied to the seven-component ansatz. Controls: the
exponent claimed n/2; I0 = 1 with the five-dimensional matrix (the exponents then his, not ours); A_0's (7, 7) entry
moved to 1/2, which makes the z = 2 coefficient vanish (P3; D121). []

*Deduced.*

 (a) ((11.26) and (11.34) in five dimensions) rho_I^-1 rho_+^-2 L_b = L_0 + L~ with L_0 = -(rho_I d_rho_I - (3/2 +
     A_0))(rho_I d_rho_I - rho_+ d_rho_+) and L~ in rho_I Diff^2_b: the scalar part is (i), the bundle part 10.38(i)
     with its leading 2 r^(-3/2) d_0 r^(3/2) (10.38(a)). For L_(g,g0) the coefficients carrying h enter as his A_h - A_0
     and B_h, each linear in d_1 h and r^-1 h with a Christoffel symbol's weights (10.38(a), a scaling argument), so of
     I+ order one below h's.
 (b) (Definition 5.3 and (5.5)-(5.8) in five dimensions) min Re E^C_I > 3/2 + 2 gam_Ups; E^tot_I := E^C_I u (3/2, 0) u
     (3/2 + (1 - e_Ups) gam_Ups, 0) u (3/2 + gam_Ups, 0) u (3/2 + 2 gam_Ups, 0) with his two closure conditions, j
     E^tot_I in E^C_I (j >= 2) and E^C_I + (E^tot_I - 1) in E^C_I, met by his smallest-index-set argument (p. 86, (ii));
     E_I,01 := E^C_I u (3/2 + (1 - e_Ups) gam_Ups, 0), E_I,1/ := E^C_I u (3/2 + gam_Ups, 0), E-slash_I,0 := E^C_I u
     (3/2, 0), E_I,11 := E^C_I u (2, 0) u (3/2 + (1 - e_Ups) gam_Ups, 0) u (3/2 + 2 gam_Ups, 0): his with 3/2 for 1,
     except that the (7, 6) term gives (2, 0) for his (1, 0) (ii).
 (c) (Lemma 11.15 and Proposition 11.14 in five dimensions) His proofs run with (a)-(b), his Lemmas 2.12 and 2.23
     holding on [0, 1) x [0, 1) x S^3 as stated: Step 1 reaches alpha_I < 3/2, every exponent of 3/2 + A_h being at
     least 3/2; Step 2 passes 3/2 + (1 - e_Ups) gam_Ups with E-slash_I,0's (3/2, 0) and E_I,11's exceptional terms; Step
     3 gains eta < min Re(E^C_I - 1) per pass up to l_I, which needs l_I < 3/2 + (1 - e_C)(1 - v_C) gam_C (ii). So Lemma
     11.15 holds with min(alpha_I, 3/2, l_+) for his min(alpha_I, 1, l_+), and Proposition 11.14 as stated with (b)'s
     index sets.
 (d) (Proposition 11.16 in five dimensions) For l-breve_+, l_I not in Re pi_1 E^C_I u {2, 3/2 + (1 - e_Ups) gam_Ups} and
     l_I < 3/2 + (1 - e_C)(1 - v_C) gam_C: Steps 1-2 solve away the exceptional terms at z = 2 and 3/2 + (1 - e_Ups)
     gam_Ups by (iii) (gam_Ups != 1/4), Step 3 the rest, Lemma 2.12 adding (z, 0) at iota+; so E^#(1)_+ = E-breve_+ u
     {(2, 0)} u {(3/2 + (1 - e_Ups) gam_Ups, 0)}, and E^#(j+1)_+ adds the z of pi_1 E^C_I with j < Re z <= j + 1 as his
     (11.33b). The formal solutions' iota+ index set then has least real part 3/2 + (1 - e_Ups) gam_Ups, unless
     E-breve_+ goes lower -- on (a)'s scaling argument for the (7, 6) term.
 (e) (E_+ in five dimensions, and 10.42 without 10.38's readings) The iteration's iota+ index set E_+ must contain
     E^#_+, so without 10.38(d)-(e)'s readings min Re E_+ = 3/2 + (1 - e_Ups) gam_Ups, with (2, 0) in E_+ for the mass
     (Remark 11.7). 10.42's conclusions hold with it: Lemma 11.5's l_+ < min Re E_+ stays above Definition 5.15's
     binding l_+ <= 1; Corollary 11.9's (4, 0) in E_+ + 2 needs (2, 0) in E_+ alone; Corollary 11.10 and Theorem 11.12
     use min Re E_+ > 1 only. So 10.42 no longer rests on 10.38's readings for E_+, and alpha_5 = 2 (10.38(e)) is what
     those readings add.

OPEN: the five-dimensional weights l_I at I+ for the iteration (fixed with A3, by the Fourier transform's conditions
(2.27)); 10.38(a)'s scaling argument; Definition 5.3's closure written out with section 5 (A8). Labels: computed
(iplus5.py P1-P3; exact); deduced ((a)-(e)); READ ([Hin26] pp. 47, 49-50, 57-58, 86, 181, 224-230, 235); nothing proved.

### 10.45 [Hin26] sections 11.3-11.6 in the class: Steps 1-4 as one, with the mass alone (deduced; D113)

In his Steps 1-4 the forward solution's low-energy part is u_reg + g-dot + h_s1: g-dot from the augmentation by the Kerr
parameter changes b-hat_1, h_s1 from the boosts and translations S-hat_1, the boost being the second order "pole" of the
resolvent at zero energy. In the class S-hat_1 vanishes at every frequency, so his four steps reduce to one, with one
order of decay lost at K+ where his lose two.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): p. 23, "u-hat loses one order at zf
relative to f-hat", "When L-hat(sigma)^-1 has a second order 'pole' ... there is also a linear (in t*) contribution to
u"; pp. 218-219, the six steps; p. 221, Remark 11.4, "we will require rho_K^(4+eps_K)-decay of f at K+ due to the second
order pole of the resolvent ... which (in a rough accounting) causes forward solutions to lose 2 powers of t*-decay";
pp. 231-238, Proposition 11.17 and its proof, (11.41)-(11.52), u_lo := u_reg + g-dot + h_s1 (11.43b), (11.47)-(11.51);
pp. 238-247, Propositions 11.20 and 11.30, Definition 11.25; pp. 247-252, Proposition 11.32 and its proof,
(11.112)-(11.115) with footnote 116, "we only need to integrate once to control u_sing globally; the reason is that the
most singular term F(h^(<=1),aug_b,s1)(S-hat(0)) ~ |sigma|^-2 ... is absent"; pp. 252-256, Proposition 11.34,
(11.116)-(11.117), and its proof; p. 238, "limited by 1 due to transport from I+"; p. 262, Lemma 11.45 and Corollary
11.46, "(This thus decays at K+.)".

*Deduced.*

 (a) (the low-energy structure in the class) Restricted to G-invariant elements (10.43(a)), the augmented zero energy
     operator of 10.39 is invertible with the mass state as its only augmentation (10.43(d)) -- his Proposition 10.6 in
     five dimensions on 10.39's readings, restricted by equivariance. For G-invariant f the coefficient b-hat_1(sigma)
     is the mass alone (A = 0) and S-hat_1(sigma) = 0 at every sigma (S_1 has no G-fixed element, Proposition
     10.40(ii)): in his (11.43b) u_lo = u_reg + g-dot, h_s1 = 0.
 (b) (Propositions 11.17 and 11.32 in the class) His proofs run with h_s1 = 0. In (11.48)-(11.49) and (11.114) only
     F(d_t* g-dot) remains, regular at zf (his (11.47), first line; its five-dimensional weights 10.40(b), the states'
     own), so one integration of d_t* suffices throughout -- footnote 116's case from the start -- and u_sing = g-dot
     has K+ order alpha~_K - 1 where his (11.51) and (11.115) have alpha~_K - 2. His Step 2 reduces to Proposition 11.20
     with S-dot = 0 (its leading term t* h_b,s1(S-dot) has S-dot in S_1), the improvement it proves being the one above;
     Proposition 11.30 and augmentation #1 are not needed (S = 0).
 (c) (Proposition 11.34 and Corollary 11.46 in the class) For G-invariant f of K+ order alpha_K in (1, 1 + eps_K): u =
     chi_K g-dot^Ups_b(m-dot) + u~ with m-dot real and continuous in f, and u~ of K+ order alpha_K - 1 in (0, eps_K) --
     his (11.117) with b-dot = (m-dot, 0) and no S_1 term (the log t* h_b,s1 of his (9.39b) has its coefficient in S_1),
     on one order less decay of f at K+ than his alpha_K in (2, 2 + eps_K). The mass parameter m' of his Definition
     11.40 (with S = S^(0)_1 = S^(0,1)_1 = 0) eliminates m-dot: the map m' -> m-dot is the identity at (h, m) = (0, m_0)
     (his Lemma 11.45), so close to it for small (h, m - m_0). Corollary 11.46 in the class: u~ decays at K+.
 (d) (the requirements on h) The coefficients of L - L_b carry h; for f of K+ order alpha_K the iteration needs (L -
     L_b) u of that order with u bounded at K+, so h of K+ order alpha_K + eps suffices -- 1 + eps_K + eps in the class
     against his 2 + eps_K, the price of the second order pole being absent. At iota+ the cap is 10.44's: u~ has iota+
     order 3/2 + (1 - e_Ups) gam_Ups - eps where his has 1 - eps ("limited by 1 due to transport from I+"), the mass
     state having iota+ order 2 (10.39(c)). f's iota+ requirement, his (11.116)'s 4 - eps, is 3 + min Re E_+ - eps, the
     order f_1 carries in (11.155) and (11.195); in five dimensions 9/2 + (1 - e_Ups) gam_Ups - eps. (L - L_b) u, at 2 +
     2 min Re E_+ = 5 + 2 (1 - e_Ups) gam_Ups by his (11.19), lies above it (D121; D113 had taken that order as the
     requirement).
 (e) (what this gives) In the class, his Steps 1-4 hold in five dimensions as one statement: for G-invariant f with the
     orders of (c)-(d), the forward solution is a mass change plus a remainder decaying at K+, and the mass change is
     removed by the final mass -- on the readings of 10.39-10.44 and of [Hin26c] Proposition 13.18 and Corollary 13.17
     at n = 4 (the low- and high-energy resolvent bounds his proofs invoke).

OPEN: the weight l_I at I+ for the iteration (his 3 + eps_I; 7/2 + eps_I, two orders past the radiation field, is the
five-dimensional candidate, to be fixed with his (2.27) at A6; settled in 10.46(e)); [Hin26c] Proposition 13.18 and
Corollary 13.17 at n = 4 (Phase B). Labels: deduced ((a)-(e)); READ ([Hin26] pp. 23, 218-219, 221, 231-262); nothing
computed here, nothing proved.

### 10.46 [Hin26] sections 11.7-11.8 in the class: Proposition 11.51, Theorem 11.59, Corollary 11.66 (`sharp5.py`; D114)

His section 11.7 (Step 5) pushes forward solutions to almost t*^-1 decay while undoing polynomially decaying
centre-of-mass motions; his section 11.8 (Step 6) eliminates every pure gauge term of K+ order at most 2, records every
term below 4 + eps_K as a parameter, and absorbs those parameters into the operator (augmentation #5). In the class the
centre-of-mass and boost terms vanish (10.43) and the pole at zero energy is first order (10.45), so sources need K+
order 3 + eps_K and the recorded terms are those below it. This section computes which terms those are in five
dimensions and deduces his three results in the class.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): p. 218, "The pure gauge contributions
that do not have t*^(-2-eps_K)-decay must moreover be eliminated using gauge modifications"; p. 221, (11.9)-(11.11) and
Remark 11.4; pp. 263-264, (11.148)-(11.151); pp. 265-266, Proposition 11.51 and its proof; p. 274, "we really need
beta_+ = 3 + eps_+"; pp. 275-277, Definition 11.55, Definition 11.56 with footnote 124 ("the sum lam + mu is the
t*^-1-power at which the corresponding pure gauge term arises in the K+-expansion, while lam is the iota+-decay rate"),
Lemma 11.57 with footnote 125, Definition 11.58; pp. 278-279, Theorem 11.59, (11.195)-(11.196d), Remarks 11.60-11.62
(11.61: the strong decay of h "solely to ensure that the linearization of P in the black hole parameters b has 4 + eps_K
orders of K+-decay"); pp. 280-292, its proof, with p. 289, (3), "all terms in (9.39b), with lam = 1, that have t*-order
<= 2 + eps_K (so <= 2) ... are pure gauge and can be eliminated using the modification parameters", and (5), the
logarithmic term at zf, "a multiple of t*^-2 h^(0)_b,s0 and thus can be eliminated using the parameter S^(0),(2,0)_0";
pp. 292-294, Definition 11.63, the proof of the lemma before Corollary 11.66 with (11.232), Corollary 11.66 with
(11.233)-(11.234); p. 302, (12.14), "we only include terms with exponents ... lam-tilde + mu <= 2".

**Proposition 10.42 (computed; `sharp5.py` K1-K4, `class5.py` C2-C3).**

 (i) (the types and roots) The G-fixed types among window5.py's five-dimensional lists are the scalar ones at l = 0, 2,
     4, 6 and the tensor ones at l = 2, 4. Their roots of det N_L in [-3, 0] at lin5.py's point are s0: c0, e0; s2: c-1,
     c-2, e-2, e0; s4: e-2; t2: e-2; none at s6 and t4 -- the class roots between 2.6 x 10^-7 and 1.4 x 10^-6 below the
     integer. alpha_min = 3/2 + (1 - e_Ups) gam_Ups = 1.5099 there.

 (ii) (the bookkeeping) Let alpha be an iota+ exponent the class's sources carry -- every one at least alpha_min, by the
     class's index sets below; the check covers [alpha_min, 3], above which nothing is recorded. A root mu gives K+
     order alpha - mu, plus the class roots' distance. A term is recorded, with floor(3 - order) companions, while its
     order is at most 3; it is eliminated if pure gauge with order at most 2 (the class roots: below 2). The eliminated
     terms lie in {s0 e0, s0 c0, s2 e0}, all three at alpha_min, and the recorded ones in these and s2 c-1, with at most
     one companion. No physical state is recorded at any alpha >= alpha_min, and every recorded term's L_b-image has K+
     order above 3. In four dimensions at alpha = 1 with threshold 4, the same rule gives his eight eliminated
     parameters ((11.197); p. 289, (3)) and his physical s2, v2, s3, v3 with 1, 1, 0, 0 companions ((11.196b)).
 (iii) (the weights) His I+ remainder weight 3 + eps_I lies in the five-dimensional non-resonant gap 3/2 + 2 gam_Ups < z
     < 3/2 + (1 - e_C)(1 - v) gam_C (38/25 to 63999567/128 = 499996.6171875 at the point; iplus5.py P2), as in his own
     (51/50 to 499996.1171875); his iota+ remainder 3 + eps_+ feeds K+ orders above 3 only.

*Proof.* sharp5.py. K1 takes class5.py's counts (C2, made exact by C3's upper bounds); K2 finds the roots with
window5.py's routine (mpmath, 50 digits); K3 is exact on 151 points of [alpha_min, 3], the orders being linear in alpha;
K4 is exact at the point. Controls: without the reflections the vector type enters (K1); s4 claimed rootless (K2); at
alpha = 1, four dimensions' order, the class records the physical s2 and t2 at -2 (K3); the radiative order 3/2 +
gam_Ups taken as I+ weight falls below the gap (K4). []

*The class's iota+ index sets (deduced; D121).* His E_+ contains (1, 0): "The requirement (1, 0) in E+ ensures that
smooth decaying perturbations are allowed as far as their behavior at (iota+)^o is concerned" (p. 221) -- the Kerr
parameter change chi_K (g_b - g_b0) in rho_+ C^oo (Remark 11.7, p. 224) -- and his E-tilde_+ of (11.87) adds (1, 0) u
(1 + E_ind) from the boost (Lemma 11.28, (11.88): the linearization in S is rho_+ C^oo from g_0 and A^((1,1) u (1 +
E_ind)) from h^(-1)); (11.151) adds E^#_+; Lemma 11.41's linearization in b starts from chi_K g-dot_b(b-dot) in rho_+
C^oo (p. 260). In the class the boost terms are absent (10.43) and the mass change is r^-2 in five dimensions, in rho_+^2
C^oo at iota+ (10.39(c)). So the class takes E_+^G with (2, 0) in place of his (1, 0), and E-tilde_+^G := (2, 0) u (2 +
E_ind) u (E_+^G + ((2, 0) u (2 + E_ind))) u E^#_+ -- his (11.151) with the boost's exponents removed and the mass's at
its five-dimensional order, on the reading that the mass patch h^(0)(m-dot) has iota+ index set (2, 0) u (2 + E_ind) in
five dimensions (its logarithm, if any, not computed). Every element has real part at least alpha_min = min Re E^#_+
(10.44(e)); so the sources of (11.155) and (11.195), with iota+ index sets E_+^G + 3 and E-tilde_+^G + 2, feed K+ only
from exponents alpha >= alpha_min, which is (ii)'s hypothesis (the fifty-third verifier's major finding: at his alpha = 1
the rule would record the physical s2, t2 and s4 e-2).

*Deduced.*

 (a) (Proposition 11.51 in the class) His proof inducts in eps_K-steps on the K+ order of f, solving at I+ (Proposition
     11.16; 10.44) and at iota+, and fixes at each step the parameters whose terms it uncovers: the S_1 shifts
     S^(lam-1,k)_1 and the final parameters. In the class the shifts vanish and the final parameters are the mass
     (10.43(b)). With 10.45's single order of loss: for G-invariant f with the iota+ structure of (11.155) in the
     class's index sets and K+ order alpha_K in (1, 1 + alpha_min), there is a unique mass parameter m' for which the
     forward solution has K+ order alpha_K - 1. No gauge parameter is needed below the K+ order alpha_min, where (ii)'s
     first terms appear.

 (b) (Theorem 11.59 in the class) Let h be G-invariant and small in H^(oo, (<E^C_I>, 3+eps_I), (E_+, 3+eps_+), 3+eps_K),
     with 10.44's five-dimensional index sets. Let p-vec be small and G-fixed: the mass m - m_0, and the parameters
     S^(0),(lam,k)_0, S^(-lam^Ups_s0,1+1),(lam,k)_0 and S^(0),(lam,k)_2 (on the G-fixed line of S_2) at the exponents of
     K+ order at most 2 -- (ii)'s eliminated set, by (12.14)'s rule. Let f = f_1 + f_2 be G-invariant, as in (11.195)
     but with K+ order 3 + eps_K for 4 + eps_K. Then there is a unique G-fixed p-vec' such that the forward solution is
     u = chi_K u_exp + u~, where

       u_exp = g-dot^Ups_b(m-dot_rem(t*)) + h^(0),<=1_b,s0(S-dot^(0)_0) + h^(-lam^Ups_s0,1+1),<=1_b,s0(S-dot^(c0)_0)
               + h^(0),<=1_b,s2(S-dot^(0)_2) + h^(-lam^Ups_s2,2+1)_b,s2(S-dot^(c-1)_2),

     m-dot_rem has t*-order 2 + eps_K, each S-dot lies in Definition 11.58's space with 3 + eps_K for 4 + eps_K (every
     term of order at least 2 + eps_K), and u~ has K+ order 3 + eps_K. His proof runs with (ii)'s list in place of
     (9.39b)'s, one order of loss in place of two, and 3 in place of 4. Parts 1-3 eliminate (ii)'s three types at every
     exponent of order at most 2. The logarithmic zf term of his Part 3, (5), if five dimensions carry it, is a multiple
     of t*^-a h^(0)_b,s0 and so one of them; (2, 0) lies in E^#_+ (10.44). Part 4 records the rest. Only the mass term
     is not pure gauge: no physical state enters below K+ order 3 + eps_K, where his (11.196b) carries s2, v2, s3 and v3
     (Remark 11.60(4)).

 (c) (the requirement on h) By his Remark 11.61, h needs K+ order 4 + eps_K only for the linearization of P in b. In the
     class that linearization is a source of h's K+ order, and sources need 3 + eps_K, so h of K+ order 3 + eps_K
     suffices. L - L_b needs 2 + eps_K, as in his.

 (d) (Corollary 11.66 in the class) Take augmentation #5 (Definition 11.63) with q-vec = (m_rem, S^(0)_0, S^(c0)_0,
     S^(0)_2, S^(c-1)_2), and h, p-vec, q-vec G-invariant. For G-invariant f in H^(oo, (<E^C_I + 1>', 4+eps_I), 5+eps_+,
     3+eps_K) there are unique p-vec' and q-vec' such that the forward solution h' lies in H^(oo, (<E^C_I>, 3+eps_I),
     (E-tilde^#, 3+eps_+), 3+eps_K). The lemma before it (p. 294) needs L_b h_b,rem(q-vec) of K+ order 3 + eps_K. For
     the gauge terms this is (ii)'s last clause, through his (9.37). For the mass, L_b g-dot^Ups_b(m-dot_rem) = [L_b,
     t*] g-dot^Ups_b(m-dot_rem') + (1/2) [[L_b, t*], t*] g-dot^Ups_b(m-dot_rem''), with m-dot_rem' of order 3 + eps_K.
     (L - L_b) h_b,rem has K+ order 2(2 + eps_K).

 (e) (the weights) By (iii) his weights lie in the five-dimensional gaps: 3 + eps_I at I+, and at iota+ 3 + eps_+ for h
     and 5 + eps_+ for f. His (2.27) (p. 61), beta_I >= beta_iota - beta_K and beta_I > beta_iota - min(1, min Re E_K),
     which the iteration's spaces also need, holds with his weights in four dimensions; at n = 4 it rests on Proposition
     2.25's density shifts (10.42(e)), a reading -- so 10.45's OPEN item on l_I is settled on that reading (D121).

OPEN: the readings of 10.39-10.45 on which (a)-(d) rest; Lemma 11.57's linearizations in five dimensions, on 10.30's
gauge potentials (Phase B); whether the five-dimensional zf expansion of the mass's singular part carries his Part 3,
(5) term (covered either way). Labels: computed (Proposition 10.42); deduced ((a)-(e)); READ ([Hin26] pp. 218, 221,
263-266, 274-294, 302); nothing proved.

### 10.47 [Hin26] section 12 in the class: Theorems 12.3 and 12.8 (deduced; D116)

His section 12 replaces the arguments (h, p-vec, q-vec) of the augmented operator by data U: a map Phi with P(Phi(U)) in
the source class of Corollary 11.66 (Theorem 12.3), and every forward solution of the linearized problem written as D_U
Phi(U') (Theorem 12.8). In the class the data shrink to the mass, the iota+ data and the tail, and the read-off that
10.43(e) took as a reading follows from the construction itself.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): pp. 182-186, Definition 9.16 and
(9.49) ("(1, 0) in Spec ... 1 != lam in spec ... => Re lam > 1"), Corollary 9.18 (the solution "depending linearly on
f", given by a contour integral of N_iota+(L-bar, lam)^-1), Definition 9.19 ("the solution u in (9.51) is unique modulo
Res"), Lemma 9.21, (9.54)-(9.56), Proposition 9.22 and its proof (an explicit right inverse: "We can furthermore
uniquely write f = f_1 + f_2"); p. 295, the proof of Corollary 11.66; pp. 296-297, section 12's two requirements; pp.
301-302, Definition 12.1, (12.11)-(12.16), "the parameters b - b0, S, S^(0)_1 and S_rem, b_rem will be taken over
directly"; p. 304, h^[0], p-vec^[0], q-vec^[0] and (12.18); p. 310, the summary ("I := ceil(3 eps_ind^-1) + 1 steps
suffice") and Theorem 12.3 with properties (1)-(3); p. 312, (12.34), "Psi(U) := (chi_-(t*) h_(-S), 0, 0) + Phi(U)",
Lemma 12.7, Theorem 12.8 and Remark 12.9 ("the particular solution (h', p-vec', q-vec') constructed by Corollary 11.66
... is of the form D_U Phi(U'), with a constructive procedure for the determination of U'"); pp. 315-317, the proof of
Theorem 12.8 ("uniquely determined, given u_1 and b'"; Cases A and B; Step 3); p. 321, (13.5) and (13.6).

*Deduced.*

 (a) (the data in the class) Definition 12.1 in the class: U = (m - m_0, (u^0_lam, f_lam)_lam, m_rem, h-tilde), with
     (u^0_lam, f_lam) G-fixed for lam in the five-dimensional spec^(<3+eps_+)_iota+(L-bar, E^C_I), m_rem in H-dot^(k,
     2+eps_K) -- one order below his b_rem's 3 + eps_K (10.46(b)) -- and h-tilde G-invariant in H^(k, (<E^C_I>,
     3+eps_I), 3+eps_+, 3+eps_K). His S, S^(0)_1, S_rem and V_1,rem vanish (10.43(b)). His S^(0)_(l,rem) (l = 0, 2) and
     S^(-lam^Ups_s0,1+1)_(0,rem), conormal at 3 + eps_+, give terms of K+ order above 3 + eps_K (Proposition 10.42(iii))
     and so belong to h-tilde; the q-vec components they would complete are finite polyhomogeneous sums (Definition
     11.58 with 3 + eps_K for 4 + eps_K, since 3 + eps_+ >= 3 + eps_K).

 (b) (the iota+ spectrum) The five-dimensional (9.49): the poles of (9.48) below 3 + eps_+ are the pure resonances --
     none with real part at most 2, candidates at box^C's roots in (2, 5/2) of scalar type, above 5/2 not computed
     (10.37(d)-(e), on its readings) -- and the incoming exponents of E^C_I (his Remark 9.17), in five dimensions those
     of 10.44, the least 3/2 + (1 - e_Ups) gam_Ups, where Res(L-bar, lam) = {0} (Re lam <= 2). The G-fixed resonant
     states are of scalar type at even l and of tensor type at even l >= 2 (Proposition 10.40). That finitely many lie
     below 3 + eps_+ is his Proposition 9.2(2) in five dimensions, on 10.37(c)'s reading of its index 0 half.

 (c) (equivariance of Phi) Every operation in Phi's construction is canonical and built from O(4)-invariant objects on
     Tangherlini: N_iota+(L-bar, lam)^-1 through Lemma 9.14 and Proposition 9.4(2) with the radial cut-off chi_I(v);
     Res_iota+(L-bar, E^C_I, lam) of (9.56); Corollary 9.18's contour integral; the expansions at R = 0 (Proposition
     9.9), unique; the modification parameters, unique solutions of linear equations; the cut-offs chi_iota, chi_K and
     chi_-, functions of t* and r. With O(4) acting on every component of U and of (h, p-vec, q-vec), the parameters
     included (R^* g_(b0,b,-S) = g_(b0,R.b,-R.S), b0 Tangherlini's), Phi commutes with O(4) on all of D^oo, and so with
     G.

 (d) (Theorem 12.3 in the class) For G-invariant U small in D^d, Phi(U) = (h, p-vec, q-vec) is G-invariant, p-vec and
     q-vec in 10.46(b)'s G-fixed lists, and P(Phi(U)) lies in F^oo_G := H^(k-2, (<E^C_I + 1>', 4+eps_I), 5+eps_+,
     3+eps_K): his (12.31) with 3 + eps_K for 4 + eps_K -- the K+ order of P(Phi(U)) is that of h and of L_b
     h_b,rem(q-vec), 3 + eps_K by 10.46(d) -- and his steps run until the iota+ order 5 + eps_+, each eliminating
     sharp5.py's terms (Proposition 10.42(ii)) and recording its recorded ones. His properties (1)-(3) hold with the
     mass for (S, b - b0, S^(0)_1) and m_rem for (S_rem, b_rem).

 (e) (Theorem 12.8 in the class) For U in D_G small and G-invariant f in F^oo_G there is U' in D_G with D_Phi(U) P(D_U
     Phi(U')) = f and his tame estimates. His proof reads U' off the forward solution of Corollary 11.66 -- G-invariant,
     being unique (10.46(d)) -- step by step, subtracting D_U Phi of inputs it determines uniquely, and in his Case B
     through Proposition 9.22's explicit right inverse; every step is canonical, so U' is G-invariant, which is
     10.43(e)'s reading, now deduced from (c) and his construction as his text gives it. (D_U Phi is not injective
     (Remark 12.9), but no choice enters: the read-off starts from Corollary 11.66's particular solution.) Psi(U) =
     (chi_-(t*) h_0, 0, 0) + Phi(U) in the class, S = 0, with h_0 G-invariant when the data are and (13.5)'s solution is
     unique (A8); Lemma 12.7 as his.

OPEN: the five-dimensional iota+ spectrum between 5/2 and 3 + eps_+ (not computed; finitely many on 10.37(c)'s reading);
Proposition 9.4(2), Corollary 9.18 and Propositions 9.9, 9.15 and 9.22 in five dimensions (READ at n = 3; their
five-dimensional inputs 10.37's and 10.44's; Phase B); h_0 and (13.5) (A8). Labels: deduced ((a)-(e)); READ ([Hin26] pp.
182-186, 295-297, 301-302, 304, 310, 312, 315-317, 321); nothing computed here, nothing proved.

### 10.48 [Hin26] section 5 in five dimensions, in the class: Theorems 5.17, 5.21 and 5.23 (deduced; D117)

His section 5 solves the gauge-fixed equation in the exterior region t* <= 1, near spatial and null infinity, from small
data (Theorem 5.17, by [Hin23a]'s estimates and [SR89]), proves the solution partially polyhomogeneous (Theorem 5.21),
and pulls it back along boosts (Theorem 5.23); his section 13 starts from its family h_S. The five-dimensional structure
at I+ is 10.38's and 10.44's; here the theorems themselves.

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): p. 84 ("The setup, estimates, and
arguments are very similar to those in [Hin23a]"); pp. 85-87, Definitions 5.2-5.4, (5.5)-(5.9); pp. 92-97, Proposition
5.11 with (5.25), "2 l-flat_I <= 3", and (5.40)-(5.42); pp. 97-99, Definition 5.13, Proposition 5.14, Corollary 5.15;
pp. 99-102, (5.49), "l-flat_0 > 1, 1 < l-flat_I < min(l-flat_0, 1 + (1 - e_Ups) gam_Ups, 3/2)", Lemma 5.16, Theorem 5.17
and its proof ("the same (with minor, only notational, modifications) as that of [Hin23a, Corollary 3.36]"; the tame
estimate (5.52) "proved (for d = 11) in [Hin23a, Theorem 3.35]"), Remarks 5.18-5.20 (5.19: decay r^-1 or weaker at I0
"would need to revisit the exterior stability argument"), (5.53); pp. 102-108, Theorem 5.21 ("min Re E_0 > 1 + 2
gam_Ups"; "E^C,#_I := E^C_I u (E_0 n {Re z >= alpha_I})") and its proof, Steps 1-2; pp. 108-109, (5.75)-(5.77b), Theorem
5.23 ("h_0 = h on all of Omega_ext,r1") and Remark 5.24 (trivial data: "h_S = 0 ... by finite speed of propagation").

*Deduced.*

 (a) (the class of perturbations) Definition 5.3 in five dimensions is 10.44(a)'s: 3/2 for 1 in (5.5)-(5.8), E_I,11 with
     the exceptional (2, 0), and min Re E^C_I > 3/2 + 2 gam_Ups. Every exponent of E^tot_I is then at least 3/2 -- the
     diagonal of 3/2 + A_0 (10.44(ii), iplus5.py P2) and (2, 0) -- where in four dimensions pi-slash_0 h and pi_11 h
     start at 1. So in five dimensions his simplest space, for 1 < l-flat_I < 3/2, is H^(k, l-flat_0, l-flat_I) for
     every component: no radiation-field term is carried in Theorem 5.17's iteration, and (5.25)'s 2 l-flat_I <= 3
     holds.

 (b) (the operator) Proposition 5.11's (5.26a) and (5.27)-(5.28), Proposition 5.14 and Corollary 5.15 in five dimensions
     are 10.38's (scri5.py; the leading part with 3/2 for 1, A_0 lower triangular), with (5.46)'s orders unchanged: L in
     rho_0^2 rho_I Diff_b in both dimensions.

 (c) (Theorem 5.17) His proof is [Hin23a]'s: a first-order energy estimate with weight l-flat_0 at I0 and a weight below
     the radiative order at I+, commuted with rho_0 d_rho_0, rho_I d_rho_I and the rotations into the tame (5.52), then
     [SR89]. In five dimensions, on the reading that [Hin23a]'s estimates hold at n = 4 with the radiative order 3/2 for
     1 (as 10.42 reads [Hin26c]'s), the weights l-flat_0 > l-flat_I and 1 < l-flat_I < 3/2 serve (Lemma 5.16 needs
     rho_0^(l-flat_0)/rho_0^(l-flat_I) -> 0, as his), and Theorem 5.17 holds: a unique small h in H^(oo, l-flat_0,
     l-flat_I). The radiation fields are at r^(-3/2), so quadratic terms are half an order smaller at I+ than in four
     dimensions; nothing here uses that.
 (d) (Theorem 5.21) Step 1, at I0, commutes rho_0 d_rho_0 - z through (5.58)-(5.60) and does not see the dimension once
     (5.59) holds, which is (b). Step 2, at I+, integrates the I+ normal operator with the error on the right, as
     10.44's Propositions 11.14-11.16 do for the linear problem. With E^C_I's lower bound 3/2 + 2 gam_Ups, his
     hypothesis min Re E_0 > 1 + 2 gam_Ups becomes min Re E_0 > 3/2 + 2 gam_Ups; a mass change, r^-2 in five dimensions
     ((2, 0) in E_0), meets it exactly when gam_Ups < 1/4, the non-resonance 10.44 already needs, and does at the
     record's point (gam_Ups = 1/100). With l_I < 3/2 + (1 - e_C)(1 - v) gam_C (the gap of 10.46(iii)), Theorem 5.21
     holds in five dimensions on (c)'s reading.

 (e) (Theorem 5.23 in the class) S = 0 throughout the class (10.43(b)), so only h_0 = h is used ("h_0 = h on all of
     Omega_ext,r1"), the solution of (13.5) at S = 0, which is Theorem 5.17's problem with the cut-off gauge
     Upsilon^(chi_0 E^Ups), chi_0 a function of t_IVP/r. Its data G-invariant, h_0 is G-invariant by uniqueness and the
     equivariance of 10.43(a) -- 10.47(e)'s open item. The smooth dependence on S (Theorem 5.23(2)) is not needed. If
     the data equal Tangherlini's outside a compact set, h_0 vanishes near I0 by finite speed of propagation (Remark
     5.24), and Step 1 of (d) is empty; whether the record's data do is Phase C's (C2).

OPEN: [Hin23a]'s energy estimates (its Proposition 3.32, Theorem 3.35, Corollary 3.36) at n = 4 -- a reading not in
ROUTES 4.44's Phase B list, added as B10; section 5.7's construction of gauged Cauchy data from geometric data in five
dimensions (A9 meets it); the record's data near I0 (C2). Labels: deduced ((a)-(e)); READ ([Hin26] pp. 84-109); nothing
computed here, nothing proved.

### 10.49 [Hin26] section 13 in five dimensions, in the class: Theorem 13.1 (deduced; D117)

His Theorem 13.1 concatenates the exterior solution (Theorem 5.23) with [SR89]'s Nash-Moser iteration for P o Psi, whose
linearized solvability is Theorem 12.8. This section carries it into the class in five dimensions, on the readings of
10.13-10.48, and so completes Phase A of ROUTES 4.44 on those readings, which Phase B discharges (B1-B4, B10 and
10.45(e)'s [Hin26c] Proposition 13.18 and Corollary 13.17 at n = 4; D126).

*READ.* [Hin26] (arXiv:2606.28253v2, alphaXiv, 2026-10-24; printed pages; ASCII): pp. 2-3, Theorem 1.1 and Remark 1.3
("initial data (gamma, k) that are exactly Kerrian outside of a compact set", [CD03]); p. 110, Proposition 5.25 and its
proof ("very similar to [HV18b, Proposition 3.10] and [HV24, Theorem 4.2]"); pp. 318-319, Theorem 13.1, (13.1a)-(13.3),
"(1) O(t*^(-2-eps_K)) in spatially compact subsets"; pp. 319-320, Remarks 13.2-13.4; pp. 320-323, its proof: Step 1 ("we
moreover require gam_Ups to be so small that 1 + 2 gam_Ups < min Re E_0"), Step 2 ((13.5)), Step 3 ((13.6), [SR89]'s
assumptions (1)-(4): "the construction of Phi ... only involves the inversion of model operators ... with smooth
coefficients"; "D_U Psi(U') = D_S(h_-.)(S') + D_U Phi(U')"; smoothing operators from [Hin24a]), Step 4 (the metric g,
the gauge 1-form eta, "Applying the second Bianchi identity to (13.7) gives the homogeneous wave equation ... and thus
eta = 0 and therefore also Ric(g) = 0"; "the weakest decay at K+ arises from the term chi_K h^(<=1)_b,s1(S_rem)").

**Statement (deduced; Theorem 13.1 in the class).**

Let m_0 > 0 and Sigma_IVP be his Cauchy surface of {t_IVP >= 0, r >= r_0} in five-dimensional Tangherlini of mass m_0
(r_0 inside the horizon), eps_0 > 0, and E_0 an index set with jE_0 in E_0 and min Re E_0 > 3/2 + 2 gam_Ups. There are
eps, d, 0 < eps_K < eps_+ < eps_I < eps_0 and index sets E^C_I (Definition 5.3 in five dimensions, 10.44) and E_+
(10.44(e), 10.47(b)) such that: for G-invariant data (gamma, k) on Sigma_IVP satisfying the constraint equations, with
gamma - gamma_(m_0) in H^(oo, (E_0, 3+eps_0)), k - k_(m_0) in H^(oo, (E_0 + 1, 4+eps_0)) and both smaller than eps in
H^d, there are a mass m near m_0 and a G-invariant h in H^(oo, (E_0, 3+eps_0), (<E^C_I>, 3+eps_I), (E_+, 3+eps_+),
2+eps_K)(Omega) such that g = (1 - chi_K) g_(m_0) + chi_K g_m + h attains (gamma, k) and Ric(g) = 0. In particular g -
g_m = O(t*^(-2-eps_K)) in spatially compact subsets of {r >= r_0}.

*Deduced.*

 (a) (Step 1) The constraint damping is [Hin26] Theorem 7.1 (his summary of [Hin26a]) in five dimensions (10.21-10.23,
     Phase B's B4), E^Ups with c_Ups and c_H from 10.14-10.15, gam_Ups small with the conclusions of Proposition 6.12
     (10.15-10.18) and Proposition 8.6 (10.24-10.25) and with 3/2 + 2 gam_Ups < min Re E_0 (10.48(d)); the record's
     point has gam_Ups = 1/100.
 (b) (Step 2) Proposition 5.25's gauged Cauchy data: frame linear algebra on Sigma_IVP (5.80)-(5.81), with three spatial
     frame vectors replaced by four -- dimension-free on its face, a reading; the data G-invariant, so are h_0 and h_1,
     the construction being natural. Theorem 5.21 in five dimensions (10.48(d)) gives the exterior solution, local
     well-posedness the interior one, and (13.5) is needed at S = 0 only (10.48(e)): h_0 = h, G-invariant.

 (c) (Step 3) [SR89]'s assumptions for P o Psi from D_G to B^oo_G := H^(oo, (<E^C_I + 1>', 4+eps_I), 5+eps_+, 3+eps_K):
     (1) by Theorem 12.3 in the class (10.47(d)), C^2; (2) tame estimates of Phi as his, its construction inverting only
     model operators with smooth coefficients; (3) by Theorem 12.8 in the class (10.47(e)), with D_U Psi(U') = D_U
     Phi(U') since S' = 0, and his finite speed of propagation for supports; (4) smoothing operators on the G-fixed
     spaces, Pi S_theta Pi (10.43(e)): m - m_0 and u^0_lam finite-dimensional, f_lam and h-tilde term by term and on the
     remainder, m_rem on a weighted b-Sobolev space. [SR89]'s theorem, abstract, gives a small U in D_G with P(Psi(U)) =
     0 when P(Psi(0)), supported in t*^-1([7/4, 2]), is small in B^oo_G, which (13.1b)'s smallness gives.

 (d) (Step 4) The metric g, the gauge 1-form eta and the conclusion eta = 0, Ric(g) = 0 by the second Bianchi identity
     and the constraints are dimension-free. The weakest K+ decay in the class is chi_K g-dot^Ups_m(m-dot_rem), m_rem in
     H-dot^(oo, 2+eps_K) (10.46(b)), where his is chi_K h^(<=1)_b,s1(S_rem): the same order 2 + eps_K, so the same rate
     in spatially compact sets. The other rates of his Theorem 13.1, (2)-(4), are not carried: their five- dimensional
     exponents (the mass patch's at iota+, among them) are not computed.

*What this gives.* Phase A of ROUTES 4.44 is complete conditional on its readings (B1-B4, B10, 10.45(e); D126): Hintz's
argument has been carried, step by step, into five dimensions in the T^2-mirror class, with the class's simplifications
computed (10.43, 10.46) and every five-dimensional input either computed (10.13-10.46's propositions) or named as a
reading. The statement above is deduced, not proved: it rests on the readings of [Hin26] at n = 4 recorded in
10.13-10.48, of [Hin26a] (B4), of [Hin26c] (B1-B3) and of [Hin23a] (B10), and on the open computations those sections
list. Phase B discharges the readings; Phase C applies the statement to the record's solution, whose data must be shown
to lie in its hypotheses (C2).

OPEN: Phase B (B1-B10); Phase C; the rates (2)-(4) in five dimensions. Labels: deduced (the statement, (a)-(d)); READ
([Hin26] pp. 2-3, 110, 318-323); nothing computed here, nothing proved.

### 10.50 Phase C: the record's solution after the shell in 10.49's hypotheses (deduced; D118)

ROUTES 4.44's Phase C asks whether g_lam itself settles: C1 a solution on a region containing a Cauchy surface of the
exterior after the shell, C2 its data there in 10.49's spaces and small with lam, C3 the conclusion. The record's domain
Omega (1.1) is bounded, so C1 needs the solution beyond it; this section deduces C1-C3 from the record's own sections 1,
5 and 6 and three readings, named in (f).

*Deduced.*

 (a) (no oscillation after the shell) mu is constant for v >= v_end and mu' = (2/9) A^2 env^2 (0.5), so env = 0 there
     and the leading wave W, proportional to env, vanishes on {v > v_end}. That set is a union of generators of ell
     (L0(v) = 0, 0.1). By Lemma 6.2 the oscillating stage data gh_(m+1) on Sigma are -Pol^+ of terms bilinear with d_th
     W or built from earlier oscillating quantities, and by Lemma 5.3(c) gh_(m+1) solves a transport along ell whose
     source has an oscillating factor in every term (the oscillating part of a product of means is zero). By induction
     on m every oscillating profile vanishes on {v > v_end}, so there g_app = g0 + sum_j lam^j m_j, with g0 Tangherlini
     of mass mu_end (0.1) and the m_j smooth and independent of lam.

 (b) (the slice) Take tau1 with v_end - a < tau1 <= tau_end; such tau1 exist once T > r_q(mu_end) - a, since tau_end >=
     V - r_q(V) (1.1). Then Sigma' := {tau = tau1} meets Omega in {a <= r <= b(tau1)}, where v = tau1 + r > v_end, and a
     < q0 <= sqrt(mu0) < sqrt(mu_end), inside every horizon in play.

 (c) (beyond Omega; C1) Extend the construction to a larger domain Omega' of the form (1.1) (Theorems A, D and E do not
     depend on the size of Omega); on Sigma cap Omega' minus Omega's base, v > v_end and the data are those of
     Tangherlini(mu_end) plus smooth O(lam) terms, by (a) and Theorem D. Glue them, on an annulus outside b(tau0), to
     exact Tangherlini data of a mass m with |m - mu_end| = O(lam), G-equivariantly: the obstruction space of the gluing
     is the G-invariant part of the Killing initial data, which by Proposition 10.40(i) is spanned by d_t, matched by
     the mass parameter. The glued data agree with the record's on Omega's base, so their development contains g_lam on
     Omega (Lemma 1.1(e)); it is exactly Tangherlini(m) in the domain of dependence of the outer region; and between the
     two it is a smooth O(lam) perturbation of Tangherlini over the finite interval [tau0, tau1], with no oscillation
     there by (a), so it exists there by Cauchy stability. This gives the solution on Sigma'.

 (d) (the data; C2) On Sigma', g - g_(Tangherlini(m)) is supported in a compact set and is O(lam) in H^d: inside Omega
     it is (mu_end - m) terms, lam m_1 + lam^2 m_2 + ..., and w, whose unscaled H^j norms are at most M lam^(K - j) by
     (0.5) once Theorem E holds at order k >= d with K >= d + 1; outside, the Cauchy stability bound and the glued
     annulus. It is G-invariant (Theorem E's Step 8 and the equivariant gluing) and solves the constraints. So E_0 =
     empty -- compactly supported data, his Theorem 1.1's case -- and 10.49's hypotheses hold for lam small, with m_0 :=
     m; his Remark 13.3 lets the initial surface be a tau-level set near the hole and near infinity.

 (e) (the conclusion; C3) For lam <= lam_1 the maximal development of the glued data, which contains g_lam on Omega,
     settles in the class to Tangherlini of a mass m' with |m' - m| small, at the rate t*^(-2-eps_K) in spatially
     compact sets of the exterior -- on 10.49's readings and those of (f).

(f) The readings Phase C adds: (C-i) Theorem E at every order k >= d with K >= d + 1 -- discharged in 10.51 from the
record's own sections 4-6; (C-ii) G-equivariant gluing of vacuum data to Tangherlini in five dimensions ([CD03]-type,
its obstructions the Killing initial data); (C-iii) Cauchy stability over a finite time for smooth data, standard.
Labels: deduced ((a)-(e)), from the record's Lemmas 1.1, 5.3 and 6.2 and Theorems A, D, E; nothing computed here,
nothing proved.

### 10.51 Theorem E at every order (Phase C's C-i; deduced; D119)

10.50(d) needs Theorem E's remainder small in H^d for Hintz's large d, while section 4 fixes k = 6. Here the proof of
section 4 is read for its dependence on k.

*Deduced.*

 (a) (where k = 6 enters) Step 1: Lemma 2.1's scaled Sobolev bound ||d^i w||_inf <= C lam^(-3-i) N needs i + 3 <= k + 1,
     so i <= 4 at k = 6 and i <= k - 2 in general. Step 4: the commutator terms d^i g . d^(j-i+1) d h are split with d^i
     w in L^inf for i <= 4 and in L^2 for i >= 5, the other factor then of order j - i + 1 <= 2 in L^inf; at order k the
     split is at k - 2, the L^inf factor needing at most 2 + 1 + 3 <= k + 1 derivatives of N's quantities. The nonlinear
     terms use |d w d w|_k <= C lam^-3 |d w|_k^2, the scaled product bound in four space dimensions, valid at every k >=
     3 with C = C_k. Step 8: [DS23] Theorem 2.4 with r = k > 4/2 + 1. Steps 2, 5, 6 and 7 do not use k = 6.

 (b) (the closing) The bootstrap closes when 2K - 5 >= K + 1 (Step 4's C M^2 lam^(2K-5) <= C M^2 lam^(K+1)), that is
     when K is at least 6, whatever k is; the constants C, C2, M and lam0 then depend on k. So Theorem E holds at every
     k >= 6 with K >= 6: N_k(tau) <= M_k lam^K on [tau0, tau_end], given (E3) and (E4) at order k.
 (c) (the inputs at order k) (E3) at order k: Theorem A's residual is lam^N times a profile bounded with all its
     derivatives (5.4), so |Ric^H(g_app)|_k <= C_k lam^N for every k. (E4) at order k: Proposition 6.5 bounds the
     correction at every order, sup_r ||d_r^j U(r)||_{H^s(S^3)} <= C_(j,s) lam^(N-2-j), with lam0 independent of the
     order ("||U||_(X_(s'')) <= C_(s'') lam^(N-2) for every s''"), so Data(w) at order k is O(lam^(N-3)) = O(lam^K) with
     section 6.4's N = K + 3.
 (d) (unscaled norms) N_k <= M_k lam^K gives ||d^j d h|| <= M_k lam^(K - j) for j <= k, so the remainder is O(lam) in
     H^d once k >= d and K >= d + 1, as 10.50(d) uses.

C-i is discharged: Theorem E holds at every order k >= 6 with K >= 6, its inputs at every order by Theorem A and
Proposition 6.5. Labels: deduced ((a)-(d)), from the record's sections 4-6; nothing computed here, nothing proved.

### 10.52 [Hin26] Lemma 8.4's simplicity and (8.13) for every l (`eind5.py` E1-E2; D120)

*The setting.* 10.24 computed the indicial roots of L at the record's point for l <= 12 and located them for every l;
simplicity, and his (8.13) -- d(Re lam, Z) >= eps_ind for the non-integer roots with |lam| <= 50 -- were left at l <= 12
(Phase B's B8). By 10.24(ii) and gaugepot5.py G1, for l >= 2 the scalar type's roots are -l and l + 2, box^Ups's 2 - l
and l + 4 and the four roots of Q(lam - 1), Q(lam') = s^2 - (2 + 2 kappa + z) s + kappa (kappa + 1) + z kappa, s =
lam'(lam' - 1), kappa = l (l + 2), z = 4 e_Ups gam_Ups^2 = 4 x 10^-6, and box^C's six scalar roots less 1; the vector
type's are -l and l + 2, box^Ups's 1 - l and l + 3, and box^C's two vector roots less 1; the tensor type's are -l and
l + 2.

**Proposition 10.43 (computed).** At the record's point, (v, e_C, gam_C) = (1/2, 1/102400, 10^6), (e_Ups, gam_Ups) =
(1/100, 1/100):

 (i) (simplicity, exact) for every l >= 2 every scalar, vector and tensor root of L is simple. Q(lam - 1) at lam = -l,
     l + 2, l + 4, 2 - l is a nonzero polynomial in l with no root l >= 1; Q's discriminant in s, (z + 2)^2 + 4 kappa, is
     positive and its roots in s positive, so its four roots in lam are distinct; box^C's scalar discriminant in lam, of
     degree 9 in kappa, has its positive real roots near l = 135.59, 14640.49, 1534412.09 and 4959861.06, each isolated
     strictly between consecutive integers, so it vanishes at no integer l; box^C at lam + 1 = 1 - l, l + 3, l + 5, 3 - l
     has no root l >= 2, and its resultant with Q(lam - 1) has no root kappa > 0 (Sturm); box^C's vector quadratic,
     kappa/10^6 + 3 - lam^2/10^6 - (499999/500000) lam, has a positive discriminant and at lam + 1 = 1 - l, l + 3, 2 - l,
     l + 4 no root l >= 2.
 (ii) ((8.13), exact certificate and numerical scan) box^C's lower roots lie below -100 at every l (Proposition 10.9);
     at l* = 10^4 its three upper scalar roots and its upper vector root lie right of Re lam = 51 and none crosses that
     line for kappa >= l*(l* + 2) (the constant coefficient and the Hurwitz determinant shifted to the line have no root
     there, Sturm); box^Ups's roots are 2 - l, l + 4 (scalar), 1 - l, l + 3 (vector) and within O(z) of -l, 1 - l, l +
     2, l + 3 (Q), so only l <= 52 reach |lam| <= 50. Over l = 0, 2, 3, ..., l* - 1 (mpmath, 30 digits), the least
     distance from Z of the real part of a non-integer root with |lam| <= 50 is 1.94137 x 10^-8, at l = 50, lam =
     -49.0000000194 (box^Ups's root near 1 - l). Over l <= 12 the scan gives 10.24(iv)'s 7.3846 x 10^-8.

*Proof.* E1-E2 of eind5.py. Controls: at z = 0, Q(lam - 1) vanishes at the physical roots lam = -l and l + 2, which are
then double (E1); the certificate placed at l* = 12, where box^C's upper roots have not yet passed the line (E2). []

*Deduced.* [Hin26] Lemma 8.4 holds in five dimensions at the point for every l, as stated: 10.24(a) gave the gap and the
counts for every l, (i) gives "All indicial roots ... are simple" for l >= 2 and 10.24(iv) for l = 0, 1, and (ii) gives
his (8.13) with eps_ind at most 1.94137 x 10^-8, the scan covering l = 0 and l >= 2 and 10.24(iv) l = 1 (D126). The
bound comes from box^Ups's roots near 1 - l, which approach the integers as l grows (O(z/l)); it is attained at the
largest l whose root still has |lam| <= 50, so it depends on (8.13)'s cutoff 50, which he uses "only really ... for
|lam| <= 4" (10.24(a)). B8 is discharged. Labels: computed ((i) exact, (ii)'s certificate exact and its scan numerical),
deduced (Lemma 8.4); nothing proved beyond Lemma 8.4 at the point.

### 10.53 [Hin26c] section 9 at n = 4, at source (B1-B2; D123)

*The setting.* Sections 10.19-10.20, 10.23-10.25, 10.29, 10.32 and 10.39-10.42 use [Hin26c] section 9's spectral theory
-- Theorems 9.5, 9.16, 9.36, 9.38 and 9.41, Corollaries 9.39 and 9.43, Proposition 9.40 -- and its Definitions 5.10,
5.13 and 5.18 and Theorems 10.1 and 11.1 "at n = 4", a reading (Phase B's B1-B3). Here is what the paper says about its
dimension, READ at source, and what follows from it.

*READ.* [Hin26c] (arXiv:2606.28008v1; alphaXiv, 2026-10-24; printed page = PDF page - 4; quotations transliterated to
ASCII):

 (1) p. 101, Remark 5.6: "In the present paper, we work in 3 + 1 dimensions for concreteness. The constant 1 in (5.1a)
     arises naturally when P_0 = box_g ... See [Hin23c, section 3.1.2] for matching conventions in general dimension."
     (5.10) and (5.13) (p. 103) carry rho d_rho - 1 - S (retrieved again at source with Definition 5.13(2) and
     Corollary 9.43, D129).
 (2) pp. 157-158, section 9's opening: "we present the arguments in some detail (and generality) here" (Remark 9.1);
     Definition 9.3, "Let X be an open n-dimensional manifold (n >= 1)"; Definition 9.4, "Let X be an open neighborhood
     of the boundary dR^n of the radial compactification of R^n ... P_0 = -2 d_t* rho (rho d_rho - (n - 1)/2 - S) +
     P^_0(0) + Q d_t* - g_00 d_t*^2"; "We will only consider scalar wave operators; the purely notational modifications
     required to treat operators acting on vector bundles are left to the reader." Notation 9.2 names the algebras "on
     R^3-bar".
 (3) pp. 163, 168: Theorem 9.5 uses "the Euclidean volume density on X for the underlying L^2-spaces", with the
     thresholds (9.16a)-(9.16c), r + alpha_+ < -1/2 + S-bar at R_out, and kernel elements in A^(1 + S-bar - eps)
     ((9.20)); section 9.2.2: d_sigma P^_0(0) = 2 i rho (rho d_rho - (n - 1)/2 - S) - i Q "is symmetric with respect to
     the Euclidean volume density r^(n-1) |dr dg/| ... when S = 0 and Q = 0" (the record takes from it the density
     only).
 (4) pp. 194-198, section 9.5, "with X in R^n a neighborhood of dR^n-bar": (9.110) with (n - 1)/2; Theorem 9.38 for
     "-q + n/2" in an indicial gap, (9.114) A^((n-1)/2 + S-bar - eps, -beta), (9.115) A^(alpha, -n + 2 + beta), its
     proof with "H^(oo,q)_b([0, 1); r^^(n-1) |dr^|) in A^(q - n/2)" and the Euclidean density r^^(n-1) |dr^ dg/|;
     Corollary 9.39, tf-admissibility "except with -1 + beta in (5.16) replaced by -n + 2 + beta"; Proposition 9.40:
     "Suppose the spatial dimension satisfies n >= 3. Then scalar wave operator box_g, or indeed the tensor wave
     operator acting on sections of any tensor bundle, on an asymptotically Minkowski spacetime is tf-admissible with
     all weights beta in (0, n - 2)."
 (5) Written at n = 3: p. 61, Lemma 3.11's proof, "if we pass from |dx| to a b-density such as |dx|/<x>^3, the weight
     alpha is replaced by alpha + 3/2", and (3.47) "If alpha + 3/2 lies in an indicial gap"; pp. 193-194, Theorem 9.36,
     "alpha + 3/2 lies in an indicial gap", and its proof through Proposition 9.9 and (3.47); p. 198, Theorem 9.41,
     "tf-admissible with weight alpha + 3/2", "alpha lying in the interval (-3/2 + beta_-, -3/2 + beta_+)", and
     "|sigma|^(3/2 - alpha)" in its proof; p. 200, Corollary 9.43, "tf-admissible with weight alpha + 3/2", proved from
     Theorem 9.41 and the index 0 of (9.18); p. 106, Definition 5.13(2), "tf-admissible with weight alpha_sf + 3/2"; p.
     201, Theorem 10.1, "alpha_I < -1/2 + S-bar, alpha_+ < alpha_I - 1/2"; p. 228, Theorem 11.1 and (11.5), mu_b =
     rho_I^3 rho_+^4 rho_K |dt dx|, beta_I = alpha_I + 3/2, beta_+ = alpha_+ + 2; p. 211, Corollary 9.39 applied "with
     n = 3".

*Deduced.*

 (a) (the general statements) Definition 9.4, the computations of sections 9.2.2 and 9.5, Theorem 9.38, Corollary 9.39
     and Proposition 9.40 carry n, so at n = 4 they hold as printed: -q + 2 in an indicial gap, (n - 1)/2 = 3/2, the
     adjoint weight -2 + beta, and the tensor wave operator tf-admissible for every beta in (0, 2). These are the
     readings of 10.20(b), 10.23(e) and 10.24(c), now at source.
 (b) (the n = 3 numerals) Each comes from the b-density. On R^n-bar, |dx| = <x>^n |dx|/<x>^n, so H^(s,alpha)_b(|dx|) =
     H^(s, alpha + n/2)_b(b-density), Lemma 3.11's proof with <x>^n for <x>^3, and (3.47) holds once alpha + n/2 lies in
     an indicial gap. At n = 4: Theorem 9.36 holds with alpha + 2 for alpha + 3/2 (its other input, Proposition 9.9, is
     dimension-free); Theorem 9.41 with weight alpha + 2, the interval (-2 + beta_-, -2 + beta_+) and |sigma|^(2 -
     alpha), its proof applying Corollary 9.39 with -q + n/2 = alpha + 2; Corollary 9.43 with weight alpha + 2, by the
     same proof; Definition 5.13(2) with alpha_sf + 2. These are the substitutions 10.20 and 10.40-10.42 made.
 (c) (kernel elements) Theorem 9.5(5)'s exponent 1 + S-bar is (n - 1)/2 + S-bar: the threshold -1/2 + S-bar at R_out is
     in Euclidean L^2 (Theorem 9.5(1)), and a conormal function in rho^r L^2(r^(n-1) dr) lies in A^(r + n/2 - 0), as in
     (9.114)'s proof. At n = 4 kernel elements at nonzero frequency lie in A^(3/2 + S-bar - eps), which is the class
     10.16 and 10.27 left OPEN as "Theorem 9.5(5) in five dimensions".
 (d) (bundles) Section 9 is written for scalar operators and leaves bundles to the reader as "purely notational", while
     Proposition 9.40 states the tensor case; so B1's scalar-to-bundle step is, at source, the author's remark, the same
     at n = 3 as at n = 4, and the record's operators (box^Ups on 1-forms, box^C, L on symmetric 2-tensors) are the kind
     he applies it to.
 (e) (what remains) Theorem 9.16 at n = 4: its statement carries no n, but its proof (pp. 174-193: Propositions
     9.25-9.28 and 9.35, Theorem 9.28 at the trapped set) rests on Proposition 4.24's dynamics at the Kerr face, which
     10.17-10.18 supply in five dimensions; sections 9.3.1-9.3.5 were not checked line by line at n = 4. Definition 5.18
     and Theorems 10.1 and 11.1 at n = 4 are 10.42's reading, unchanged here.

B1 and B2 are discharged at source but for Theorem 9.16's proof at n = 4, which (e) leaves as a reading (written out as
10.75 (lix); D164). Labels: READ
(1)-(5); deduced (a)-(e); nothing computed or proved here.

### 10.54 Every small h, not one point: B5 and B6 (`uniform5.py` H1-H2; D124)

*The setting.* The record computed box^C's indicial roots at one point, (v, e, h) = (1/2, 1/102400, 10^-6) (Proposition
10.9, damping5.py U4), and so carried the condition that 10^-6 lie below the h_0 of [Hin26a] Theorems 5.2 and 6.2
(10.21(e), 10.22, 10.23; B5), and left box^C's horizon threshold OPEN (10.21(d); B6). His own h_0 is not explicit:
"there exists e_0 = e_0(v) in (0, 1) such that for all e in (0, e_0), there exists h_0 > 0 such that for all h in (0,
h_0)" (Theorem 4.9, p. 37; Theorem 6.2, p. 67 likewise), and "Only a calculation of the indicial roots, as performed in
Theorem 4.9, allows one to get invertibility ... for some fixed positive h in the full stated range of weights" (Remark
6.3, p. 69; READ, alphaXiv, 2026-10-24). So the five-dimensional statement wanted is his: at the record's e, every
sufficiently small h.

**Proposition 10.44 (computed; exact).** At (v, e) = (1/2, 1/102400) and for every h in (0, 10^-6]:

 (i) no indicial root of box^C (10.12's operator) at any harmonic type and degree has real part in [-100, 19/10]; the
     counts (right | between | left) are 3 | 0 | 3 for the scalar sextic at every l >= 1, 1 | 0 | 1 for the vector
     quadratic, 2 | 0 | 2 for the quartic at l = 0;
 (ii) the only roots with real part in [-100, 2] are lam = 2 at l = 0 and at l = 1, each simple.

*Proof.* H1-H2 of uniform5.py, damping5.py U4's certificate with h a second parameter: for h > 0 the leading coefficient
in lam (-h^3 for the scalar types l >= 1, h^2 for scalar type 0, -h for the vector type) does not vanish, so the roots
move continuously over the connected region {kappa >= kappa_0, 0 < h <= 10^-6},
and reach a line Re lam = x only where the shifted constant coefficient or the Hurwitz determinant vanishes; these are
polynomials in (kappa, h) whose number of roots kappa >= kappa_0 can change only at an h where their leading coefficient
in kappa, their value at kappa_0 or their discriminant in kappa vanishes, and none of those has a root in (0, 10^-6]
while at 10^-6 neither has a root kappa >= kappa_0 (Sturm throughout). At l = 0 and 1, lam - 2 divides for every h and
the cofactors are treated the same way. Mutant: 10^-3 in place of 10^-6, above e, where the critical values appear
(damping5.py U6: the upper roots stay above 2 exactly where h <= e). []

*Deduced.*

 (a) ([Hin26a] Theorem 4.9 in five dimensions, at the record's e) For every h in (0, 10^-6], with C_0 = 100: Re lam >= 2
     or Re lam < -C_0; the only root with Re lam = 2 is lam = 2, simple, of scalar types 0 and 1; the counts of (i); and
     the roots accumulate only at +-infinity (damping5.py U3's top-weight parts h^3 (kappa - lam^2)^3 and h (kappa -
     lam^2), whose roots +-kappa^(1/2) are free of h). This is his Theorem 4.9
     with 2 for his 1, for every h below an explicit bound rather than below an h_0.
 (b) (what inherits) Every conclusion the record drew from Proposition 10.9 at the point holds for every h in (0,
     10^-6]: 10.21(d)'s index 0 and roots; 10.24(a)'s gap (0, 1] and even split of L's roots (box^C's minus 1, box^Ups's
     plus 1 and the physical, the last two free of h); 10.35's window5.py roots in [-3, 0], which box^C does not reach;
     10.37's "none has real part at most 2" for the pure iota+ resonances; the class's iota+ index sets above alpha_min
     (10.46). The point's numbers themselves -- 1.000003, the roots in (2, 5/2) of iota5.py I4 -- move with h and are
     not used beyond these bounds.
 (c) (what does not depend on h, or improves as h falls) The symbols of the semiclassical argument -- 10.13's Lemmas
     3.3-3.8, the e-bound of his Lemma 4.4 (semiclass5.py W4), cform5.py's and solv5.py's T at (v, e), tface5.py F3 --
     are free of h. The quantities proportional to gam_C = 1/h grow as h falls, and the record uses lower bounds of them
     only: A_0's diagonal and the I+ gap's upper end 3/2 + (1 - e_C)(1 - v) gam_C (10.44), dual5.py's 3 + 2 v gam_C
     (10.31), tface5.py's S_in = h^-1 (1 - e)(1 + v) (10.23), and strap5.py's diagonal -2 (1 - e_C) gam c_2, -2 gam
     c_2, -4 gam c_2, whose signs alone are used (10.26). 10.38(iii) is not of this kind: its non-resonance at the
     radiative exponents is computed at gam_C = 10 and 100 only and is OPEN at the record's gam_C (10.38); nothing in
     this section rests on it (D129).
 (d) (what holds off a countable set) Simplicity (10.52(i)) is, for each l, the nonvanishing of a polynomial in h that
     is nonzero at 10^-6, so it fails for at most finitely many h at each l, and for at most countably many in all;
     (8.13) holds at every h with its own eps_ind(h) > 0, finitely many roots having |lam| <= 50 (the top-weight parts)
     and each non-integer one lying off Z; the record uses eps_ind only through eps_ind > 0, its value 1.94137 x 10^-8
     being the point's (10.52; D129). So the h that the record's theorems take may be any h in (0, 10^-6] outside a
     countable set, below the h_0 of his Theorems 5.2 and 6.2 and of [Hin26] Theorem 7.1 ("for all sufficiently large
     gam_C").
 (e) (B6, the horizon threshold) 10.21(d) needs vartheta_H+ < -C_0 - 1/2 for box^C at the conormal bundle of the
     horizon. The part of that quantity of order h^-1 is h^-1 rho_oo times the damping symbol l_{g,c,e} of C (his Lemma
     3.2), even in the covector, which his Lemma 3.5 -- computed in five dimensions in 10.13 -- makes definite on future
     causal covectors with respect to Lemma 3.3's fiber inner product, with the sign that damps (his Remark 5.7's
     mechanism, as 10.21(d) reads it); the horizon's conormal covectors are null and its cosphere bundle is compact, so
     vartheta_H+ <= vartheta_0 - c h^-1 with c > 0 and vartheta_0 free of h, neither computed, and the threshold holds
     for every h below some h_2 > 0. With (d), any h in (0, min(10^-6, h_0, h_2)) off a countable set serves.

B5 is discharged: the record's point was a sample, and its conclusions hold for every h in (0, 10^-6] or off a countable
set there. B6 is deduced, the threshold holding for every small h with its bound h_2 not computed, which his own
statement does not need. Labels: computed (Proposition 10.44), deduced ((a)-(e)), READ (the quotations); nothing proved
beyond that.

### 10.55 The Minkowski model and the interior: B9 and B7 (`transfer5.py` T1-T2; D125)

*The setting.* The record computed every indicial family, tf-normal operator and I+ structure on 4+1 Minkowski and
carried them to Tangherlini on [Hin26]'s word that these "only see the Minkowskian model" (10.12) and on [Hin26c]
Example 5.4's order, box_(g_m,a) - box_(g-bar) in rho^3 Diff^2_3b (B9). And 10.16 and 10.27 left OPEN the kernel class,
the index 0 and the "standard interior uniqueness" that carries a mode's vanishing inside the horizon (B7).

**Proposition 10.45 (computed; exact).** Five-dimensional Tangherlini is, in Kerr-Schild coordinates (t, x), x in R^4,
r = |x|, g = eta + (mu/r^2) k (x) k with k = dt + dr null for eta and for g, g^-1 = eta^-1 - (mu/r^2) k# (x) k#
exactly, and Ric(g) = 0 (T1, at three points). Every Christoffel symbol is mu G_3 + mu^2 G_5 with G_j homogeneous of
degree -j; with t* = t - r, g^-1(dt*, dt*) = -4 mu/r^2, g^-1(dt*, dr) = -1 + 2 mu/r^2, g^-1(dr, dr) = 1 - mu/r^2; and
the damping 1-form with the static time differs from Minkowski's r^-1 (dt - v dr) by -mu dr/(r (r^2 - mu)), of order
r^-3 (T2).

*Proof.* T1-T2 of transfer5.py, the homogeneity exactly, as G_j(s x) = s^-j G_j(x) for rational functions of x, r and a
scale s (D129; at one point before). Controls: the four-dimensional profile mu/r in five dimensions, which is not Ricci
flat (T1) and whose connection is one order below Minkowski's, not two (T2). []

*Deduced.*

 (a) (B9, the transfer) Every operator of the record -- box^Ups, box^C, L and their spectral families -- is built from
     g, its connection and curvature (of order mu r^-4) and the 1-forms c, c_Ups; on Tangherlini each differs from its
     Minkowski model by terms two orders below the model's own: in rho^4 Diff^2_b against the model's rho^2 Diff^2_b,
     where [Hin26c] Example 5.4 has rho^3 in four dimensions. So the indicial families at infinity, the tf-normal
     operators (only Minkowskian terms survive, [Hin26] p. 118) and S-bar are the Minkowski model's, as 10.12, 10.15,
     10.24 and 10.38 used; g^00 = -4 mu rho^2 is in rho^2 C^oo, [Hin26c] Definition 9.4's class; and the mass enters at
     rho^2, rho_+^2 at iota+ (10.46). 10.39's OPEN "the boost entry and g^00 on Tangherlini" is answered for g^00 here
     and is removed for the boost by the class (10.43); Myers-Perry is outside the class.
 (b) (B7, the kernel class and the index) Kernel elements at nonzero frequency lie in A^(3/2 + S-bar - eps) (10.53(c)),
     the class 10.16 and 10.27 named. The index 0 at nonzero frequency is [Hin26c] Theorem 9.5(3), proved in his section
     9.3 from Theorem 9.16(3)'s invertibility at large frequency, so at n = 4 on 10.53(e)'s reading of Theorem 9.16.
 (c) (B7, the interior) Every operator of the record on Tangherlini is stationary and SO(4)-invariant (c, c_Ups and the
     modifications near the horizon are spherically symmetric, 10.14-10.15), so its spectral family splits over the
     harmonic types and degrees into systems of ordinary differential operators in r, regular on (r_int, r_h) (f = 1 -
     mu/r^2 does not vanish there) and with a regular singular point at r_h, where f vanishes simply. A kernel element
     on X, smooth across the horizon by the radial point estimate there, that vanishes for r > r_h vanishes to infinite
     order at r_h; a solution of a regular singular system with that property is zero near r_h (its Frobenius exponents
     are finitely many), and then on (r_int, r_h) by uniqueness for the regular system. This is the "standard interior
     uniqueness" of 10.16. (D149: that a solution vanishing to infinite order at a regular singular point vanishes near
     it is Lemma 10.56 (c), proved in 10.76; the finiteness of the exponents alone does not give it for coefficients
     that are only smooth.)

B9 is discharged (computed and deduced); B7 is deduced, the index 0 at nonzero frequency on 10.53(e)'s reading. Labels:
computed (Proposition 10.45), deduced ((a)-(c)); nothing proved beyond that.

### 10.56 [Hin26a] at n = 4, at source (B4; D125)

*The setting.* 10.21-10.23 deduced [Hin26a] Theorems 5.2, 6.2 and B.1 in five dimensions from computed inputs, on the
reading that his arguments hold at n = 4 (Phase B's B4). Here his section 5.2, read at source, against that reading.

*READ.* [Hin26a] (arXiv:2606.27658v2; alphaXiv, 2026-10-24; printed page = PDF page; ASCII):

 (1) pp. 41-42, Theorem 5.2: "Fix v in (0, 1), C_0 > 0, and alpha_sf, alpha_K such that alpha_sf < -1/2, alpha_K >
     alpha_sf + 1/2 (5.14) ... Then there exists h_0 > 0 such that for all h in (0, h_0)", with the initial data in
     "rho_sf^(alpha_sf + 1/2) H-bar^1_b(X, r^2 |dr dg/|)" (5.16); Lemma 5.3, "h^2 box_g in h^2 rho_sf^2 Diff^2_3b,
     L_(g,c,e,h) in h rho_sf^2 Diff^1_3b" (5.17).
 (2) p. 42, the proof's plan: elliptic estimates and complex absorption at nonzero and infinite semiclassical
     frequencies (section 5.2.1); "propagation estimates near the three critical sets of the vector field -r c#"
     (sections 5.2.2-5.2.4); real principal type propagation along the zero section (5.2.5); energy estimates near X and
     Sigma# (5.2.6); their combination (5.2.7, pp. 64-65, Propositions 5.5, 5.6, 5.8, 5.9, 5.11, 5.12, 5.16, 5.17), with
     "h_0 > 0 sufficiently small" at each absorption.
 (3) p. 60: the energy estimate is stated on "I_t x M where ... M is an n-dimensional manifold of bounded geometry"; p.
     65: "|dg| is a smooth positive multiple of dtau . r^3 dr |dg/|, and rho_sf^(alpha_sf + 1/2) H-bar^s_b(X, r^2 |dr
     dg/|) = rho_sf^(alpha_sf) H-bar^s_b(X, r^3 dr |dg/|)".
 (4) pp. 67-69, Theorem 6.2's proof: Theorem 5.2 "with C_0 increased by 1", Theorem 4.9, and index 0 because "Theorem
     4.9(3) implies that, acting on suitable weighted spaces ... they are of index 0", with "the shift in the weight at
     dX by -3/2 when passing from L^inf-based spaces to L^2-based spaces"; p. 91, Theorem B.1's index argument, through
     "Theorem 4.9(3)" and the flat roots "-l - 2, -l - 1, -l and l - 1, l, l + 1".

*Deduced.*

 (a) (Theorem 5.2 at n = 4) Every estimate of the proof is microlocal or an energy estimate, and each takes from the
     metric and from c only symbol data: the critical sets of -r c# and the subprincipal symbols there, the positivity
     of the damping symbol (his Lemmas 3.5 and 3.8), the thresholds (5.14) and c itself. In five dimensions these are
     computed: 10.13 (Lemmas 3.3-3.8 and the symbols at the critical sets, semiclass5.py W1-W6), 10.14 (c, cform5.py),
     10.22 (solv5.py Q1-Q4: (5.14) as alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*, b* = 0.99340731...). The
     calculus is stated for general dimension ((3); [Hin23d]), and the densities move as (3) shows: r^3 |dr dg/| in
     place of r^2 |dr dg/|, the data weight shifting by 1/2 more, as 10.21(c) takes it. So Theorem 5.2 holds at n = 4
     for every h below its h_0 -- on the reading, now narrowed to it, that each commutator's sign in sections
     5.2.1-5.2.6 is the sign of the five-dimensional symbol the record computed; the commutator computations were not
     redone at n = 4.
 (b) (Theorem 6.2 at n = 4) His proof needs Theorem 5.2, Theorem 4.9 and index 0 from Theorem 4.9(3); in five dimensions
     (a), 10.54(a) for every h in (0, 10^-6], and 10.21(d)'s radial operators, the L^inf to L^2 shift being n/2 = 2
     (10.21(e)).
 (c) (Theorem B.1 at n = 4) His index argument needs Theorem 4.9(3) and the flat operator's roots; in five dimensions
     10.54(a) and tface5.py F5's computed roots, -3, -2 | 0, 1 at l = 0, -l - 3, -l - 2, -l - 1 | l - 1, l, l + 1 and
     -l - 2 | l (10.23).

B4 is deduced at source with one reading left, (a)'s: the sign of each commutator in his section 5.2 as computed in five
dimensions. (Since discharged at source in 10.65 and written out as 10.75 (lxi); D167.) Labels: READ (1)-(4); deduced
(a)-(c); nothing computed or proved here.

### 10.57 [Hin23a] in five dimensions, at source (B10; D125)

*The setting.* [Hin26] Theorem 5.17 solves the gauge-fixed equation near spatial and null infinity by [Hin23a]'s
estimates and [SR89]; 10.48 carried it to five dimensions on the reading that [Hin23a]'s Proposition 3.32, Theorem 3.35
and Corollary 3.36 hold at n = 4 (B10). With the record's data a compactly supported perturbation of Tangherlini
(10.50), the solution is Tangherlini near I0 by finite speed of propagation ([Hin26] Remark 5.24, 10.48), so [Hin23a] is
needed only for a piece of null infinity.

*READ.* [Hin23a] (arXiv:2302.13804v1; alphaXiv, 2026-10-24; printed page = PDF page; ASCII):

 (1) p. 1: "(3 + 1)-dimensional spacetimes"; p. 9, section 3.1: "Consider an n-dimensional manifold M with corners".
 (2) pp. 21-22, Proposition 3.29: L_g = -2 (rho_I d_rho_I - A_g)(rho_0 d_rho_0 - rho_I d_rho_I) + x_I^2 Laplacian + 2
     B_g + L~_g, L~_g in (x_I C^oo + H^(k-2,(l_0, 2 l_I))_b) Diff^2_(e,b), the 7 x 7 matrix A_g carrying the entries
     -(1/2) d_1 h_(ab) and 2 d_1 h_(ab), for g = g_m + r^-1 h.
 (3) pp. 27-30, Proposition 3.32 and its proof: the multiplier W, Lemma 3.33 ("Write points x in R^n ...", d_p the
     smallest integer > p/2, Sobolev embedding H^(d_(n-1))(R^(n-1)) in L^inf) applied "with n = 4", and the sharp
     weights from "A_g is lower triangular ... with scalar diagonal entries that are independent of h".
 (4) pp. 30-32, Theorem 3.35: k >= m + 11, its improvements giving pi-slash_0 u's and pi_11 u's leading terms at I+
     ((3.63)-(3.64)) -- p. 9: "pi-slash_0 u has a radiation field, i.e. a leading order term of size O(rho_I) = O(r^-1)";
     Corollary 3.36: [SR89] "with loss of derivatives parameter d = 11 ... 2433 = 16 d^2 + 43 d + 24"; the gauge by the
     second Bianchi identity.

*Deduced.*

 (a) (where the dimension enters) The calculus is general (1). The dimension enters through the radiative order -- r^-1
     h in (2), r^-(3/2) h in five dimensions (10.38) -- through the densities (rho_0^4 rho_I^3 for rho_0^5 rho_I^4), and
     through Lemma 3.33's Sobolev index, applied on the four-dimensional boundary I+ (u, S^3) in five dimensions: d_4 =
     3 in place of d_3 = 2, one more derivative in each tame bound of Proposition 3.32.
 (b) (Proposition 3.29 at n = 4) The h-dependent entries of A_g and B_g are the couplings of the radiation field r^-1 h
     at the borderline order. With g - g_m = r^-(3/2) h they carry one more factor x_I = r^-(1/2) and join L~_g, so A_g
     is 10.38's A_0, lower triangular with h-free diagonal (10.44(ii)): the hypothesis of (3)'s sharp-weight step holds
     outright, not only to leading order. (The order count is deduced, not computed: 10.38's OPEN "h-terms of (5.28)".)
 (c) (Theorem 3.35 not needed) Its improvements recover the r^-1 radiation field and h_11's limit at I+ (4). The
     record's five-dimensional spaces carry no radiation field at the iteration's weight: [Hin26] p. 102's first step,
     the tame energy estimate with any I+ weight below the radiative order (10.48(a)), gives the space Theorem 5.17
     needs, the quadratic terms gaining x_I^(1/2) there.
 (d) (Corollary 3.36 at n = 4) [SR89] applies with the loss of (a)-(c), finite whatever its value, given data with
     enough derivatives; the record's glued data are smooth (10.50). The gauge and Ricci flatness follow by the second
     Bianchi identity in any dimension.

B10 is deduced at source, with (b)'s order count and (c)'s gain read, not computed. Labels: READ (1)-(4); deduced
(a)-(d); nothing computed or proved here.

### 10.58 [Hin26c] sections 5-8, 10, 11 and 13 at n = 4, at source (B3; D127; `iplusnorm5.py`, D166)

*The setting.* 10.40-10.42 and 10.45(e) took [Hin26c]'s Definitions 5.13, 5.15 and 5.18, Theorems 8.14, 10.1 and 11.1,
and Proposition 13.18 and Corollary 13.17 "at n = 4" (B3). 10.53 read section 9 at source. Here the rest.

*READ.* [Hin26c] (arXiv:2606.28008v1; alphaXiv, 2026-10-24; printed page = PDF page - 4; ASCII):

 (1) pp. 39 and 102: (2.25)-(2.27), "g-bar = -dt*^2 - 2 dt* dr + r^2 g/, g-bar^-1 = -2 d_t* (x)_s d_r + d_r^2 + r^-2
     g/^-1", rewritten in rho_+ = 1/t*, x_I = (t*/r)^(1/2) as (1/2) x_I^2 rho_+^2 (x_I d_x_I (x)_s (-2 rho_+ d_rho_+ +
     (1 + x_I^2/2) x_I d_x_I) + x_I^2 g/^-1); and (5.7), 2 x_I^-2 rho_+^-2 P_0 == -(x_I d_x_I - 2 (1 + S))(x_I d_x_I - 2
     rho_+ d_rho_+) + 2 x_I^2 Laplacian-slash mod x_I Diff^2_eb, its "1" that of (5.1a)'s rho d_rho - 1 - S.
 (2) pp. 107-109: Definition 5.15, h in x_I^-2 rho_+^-2 C^((d_0;k),(2 l_I, l_+, l_K))_(e3b;b); Definition 5.18, (5.25)
     and (5.27), "-(x_I d_x_I - 2 (1 + p_1))(x_I d_x_I - 2 rho_+ d_rho_+)", p_1 = S|_(dX) + p~_1.
 (3) p. 114: section 7's estimates "rely only on the principal symbol of P and thus on the dynamical properties of
     asymptotically Kerr metrics (except for the precise values of certain threshold conditions on weights and
     regularity orders which are determined by subprincipal terms of P)", and "can almost be quoted from the literature:
     [HV26, section 4] ... [Hin23c, section 5.1] ... [Hin24a, section 4.3] ... and [Hin21, section 3B2]"; p. 115,
     Proposition 7.1 with the weights (7.3), "alpha_I < -1/2 + p-bar_1, alpha_+ < alpha_I - 1/2", footnote 51 naming the
     radial point estimates they come from; p. 19, footnote 13: "we work with L^2 relative to the metric density rather
     than mu_b, which leads to constant shifts in the orders".
 (4) p. 156: Theorem 8.14, the combination of Propositions 8.6 and 8.9 (energy estimates near t* = 1), 7.11 (the
     microlocal estimate) and 8.12-8.13 (near r = m), under "alpha_I < -1/2 + p-bar_1"; p. 201, Theorem 10.1 under
     (10.2), "alpha_I < -1/2 + S-bar, alpha_+ < alpha_I - 1/2"; p. 228, Theorem 11.1 and (11.5), mu_b = rho_I^3 rho_+^4
     rho_K |dt dx|, "beta_I = alpha_I + 3/2, beta_+ = alpha_+ + 2".
 (5) p. 255: (13.30a), "The shift of 3/2 in the decay orders at rho^-1(0) = scf u tf is due to the passage from mu to
     mu_b"; Proposition 13.18, "with P_0 being tf-admissible with weight alpha + 3/2 ... Let beta_scf < 1 + S-bar ...
     beta_tf - beta_zf in (beta_-, beta_+)", proved "identical to that of Corollary 13.14, mutatis mutandis".

*Deduced.*

 (a) (where n enters) (2.25)-(2.27) are Minkowski algebra in (t*, r) and do not see n beyond the round sphere's g/; at
     n = 4 they hold with S^3's. The "1" of (5.1a) and (5.7) is (n - 1)/2 ([Hin26c] Definition 9.4, 10.53), so at n = 4
     Definition 5.18's (5.27) reads -(x_I d_x_I - 2 (3/2 + p_1))(...), the record's iplus5.py P1 leading part. The
     densities give every other numeral: 3/2 = n/2 in (11.5), (13.30a), Proposition 13.18 and Definition 5.13(2), and
     mu_b = rho_I^4 rho_+^5 rho_K |dt dx| at n = 4 (rho_I^n rho_+^(n+1) rho_K, the b-density being |dt dx|/(t* r^n)),
     so beta_I = alpha_I + 2, beta_+ = alpha_+ + 5/2 and beta_scf < 3/2 + S-bar, as 10.41-10.42 took them. The
     thresholds (7.3) and (10.2) are stated in p-bar_1 and S-bar, measured in the metric density, the -1/2
     dimension-free as at (9.16c) (10.53(c)).
 (b) (the dynamics) Section 7 uses the principal symbol only, apart from those thresholds (3). Near I+ and iota+ the
     dynamics are (2.27)'s and (4.67)'s, free of n; near the horizon and the trapped set they are five-dimensional
     Tangherlini's, computed in 10.17-10.18 (hienergy5.py, the horizon's radial set and normally hyperbolic trapping).
 (c) (what is left) Definitions 5.13, 5.15, 5.18, Theorems 10.1 and 11.1, Proposition 13.18 and Corollary 13.17 hold at
     n = 4 with (a)'s numerals, on one reading: that the propagation, radial point and energy estimates of sections 7-8,
     quoted in part from [HV26], [Hin23c], [Hin24a] and [Hin21], hold at n = 4 once their symbols are five-dimensional
     -- the same reading as 10.53(e)'s for Theorem 9.16 and 10.56(a)'s for [Hin26a] section 5.2. (Since written out as
     10.75 (lx), with Proposition 10.57 below; D166.)

**Proposition 10.57 (computed; `iplusnorm5.py` N1-N9; exact).** For n = 3 and n = 4, with c = (n - 1)/2 and S a
complex constant:

 (N1) t*^2 times -box on R^(1+n), on r^b t*^(-a-b) = tau^a R^b (tau = 1/t*, R = r/t*), is -2 R^-1 (tau d_tau + R
      d_R)(R d_R + c) + R^-2 P^(0)(0, omega, -R d_R) with P^(0)(rho d_rho) = -(rho d_rho)^2 + (n - 2) rho d_rho, and
      [Hin26c] (10.7)'s second line in x_I = R^-(1/2) is the same operator: c = 1 (his) and 3/2.
 (N2) Im d_sigma N^0(P_0, 0) for |dx_I/x_I| is -x_I^2 (n + 2 Re S) (his (10.25) at n = 3).
 (N3) The symbol of h Im(-(1/2) x_I^2 X (X - 2(c + S))), X = x_I d_x_I, is x_I^2 (c + 1 + Re S) xi; with (N2) it is
      x_I^2 ((c + 1) xi - (2c + 1) + Re S (xi - 2)), his 2 xi - 3 + Re S (xi - 2) at n = 3, and x_I^2 at xi = 2 for both
      n; Q_1's symbol is x_I^2 xi; the total of (10.27) at R_I+,+1,in is -4(gam_I + h^-1 Im z) for both n.
 (N4) At R_I+,out, (4 gam_I + 2) - 4(c + Re S) - 2 < 0 iff gam_I < c + Re S.
 (N5) |dt dx| = R^n tau^-(n+1) |dtau/tau dR/R domega| = 2 x_I^-2n tau^-(n+1) |dtau/tau dx_I/x_I domega|, whence -Im sigma
      = alpha~_+ + (n + 1)/2, gam_cf = alpha~_K - alpha~_+ - n/2, gam_I = alpha_I + n/2, gam_+ = alpha_+ + (n + 1)/2;
      with [Hin26c] (11.4)'s functions rho_I^n rho_+^(n+1) rho_K = 1/(t* r^n), and |dt dx|/(t* r^n) is |dt*/t* dr/r
      domega|; L^2(|dx|) = rho^(n/2) L^2(|dx|/|x|^n); -1/2 + n/2 = c.
 (N6) At R_cf,+1,in, Im(R^-2 P^(0)) vanishes for R^n |dR/R| and gives -n hhat xi for |dR/R|; sigma(Q_0,h) = -hhat (n + 2
      Re S); with gam_cf = -(alpha_+ + n/2) the total at xi = -2 is -4b - 4 alpha_+ - 2 + 2 vartheta - 4 Re S for both n,
      and the n = 3 sum as printed, without Re S, gives (10.28).
 (N7) At R_cf,out, twice Im(2h D_R) is -2 hhat and twice Im(-2(c + S) i R^-1 h) is -4 hhat (c + Re S); with gam_cf =
      -(alpha_+ + n/2) the total is 4b + 4 alpha_+ + 2 - 4 Re S for both n, negative iff b + alpha_+ < -1/2 + Re S.
 (N8) R^(i sigma) R^2 N^0(P_0, sigma) R^(-i sigma) = -2 d_v (v d_v + i sigma - c - S) + P^(0)(v d_v + i sigma), v =
      1/R; on F(v_+^lam) = Gamma(lam + 1)(-i rhat)^(-lam-1) its Fourier transform is 2i rhat(-rhat d_rhat + i sigma -
      (c + 1) - S) + P^(0)(-rhat d_rhat - 1 + i sigma); and conjugation by rhat^(1 - i sigma) with rho-hat = 1/rhat gives
      N_tf(P_0, 1) = 2i rho-hat(rho-hat d_rho-hat - c - S) + rho-hat^2 P^(0)(rho-hat d_rho-hat).
 (N9) The C(n, 2) rotation fields span T S^(n-1) at a point; (gam_cf + n/2, b - gam_cf - n/2) for Rhat^n |dRhat/Rhat| is
      (gam_cf, b - gam_cf) for |dRhat/Rhat|, and (q - 2, r + 1) from there is (gam_cf - 2, b - gam_cf + 1).

*Proof.* N1-N9 of `iplusnorm5.py`, sympy, exact. Operators sum_a x^a p_a(X) are composed and adjoined exactly, the
adjoint for x^m |dx/x| being x^a p-bar(-X - a - m), Im A = (A - A*)/(2i), and principal symbols are read by h X -> i
xi; N1 acts on tau^a R^b, N8 on v^lam, F(v_+^lam) and rhat^mu, N5 computes the Jacobians. 9/9; each check's mutant (c
= 1 at n = 4, the density x_I |dx_I/x_I|, Q_0 at n = 3 beside the n = 4 symbol, r^(n-2), gam_cf = -(alpha_+ + 3/2) at n
= 4, his numeral 2 at n = 4, n - 1 rotation fields) is caught, 9/9.

B3 is deduced at source, its numerals all accounted for and computed in Proposition 10.57 (D166); the one reading left
is (c)'s, now (lvi)-(lix)'s and 10.20's. Labels: READ (1)-(5); deduced (a)-(c); computed (Proposition 10.57); nothing
proved here.

### 10.59 The remaining items: (2.27), the iota+ spectrum, 10.38(a), and the gluing (D127)

*READ.* [Hin26] (arXiv:2606.28253v2; printed page = PDF page - 4): p. 59, section 2.3 works on "M := [R_t* x X; {-oo,
+oo} x dX], X := R^n_x" with the b-density |dx/<x>^n|; p. 61, Proposition 2.25, its condition (2.27) "beta_I >=
beta_iota - beta_K, beta_I > beta_iota - min(1, min Re E_K)". [CD03] (Chrusciel-Delay, gr-qc/0301073v2): p. 4, "These
are the general relativistic constraint equations whatever the space-dimension n"; Theorem 7.7 (p. 34), the constraint
map onto its range orthogonal to the KIDs, in weighted spaces on R^n, "k > n/2"; Remark 8.2 (p. 36), on the gluing to
Kerr at infinity: "The argument below carries over to any dimension, the only element missing is an equivalent of
Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry metrics"; p. 55, symmetric gluings by
uniqueness: "Uniqueness implies that the solution will be even".

*Deduced.*

 (a) ([Hin26] (2.27) at n = 4; 10.46(e)) Proposition 2.25 is stated on X = R^n with the b-density |dx|/<x>^n, so (2.27)
     holds at n = 4 as printed; the density shifts between it and the iteration's spaces are n/2 (10.42(e), 10.58(a)).
     10.46(e)'s reading is discharged.
 (b) (the iota+ spectrum between 5/2 and 3 + eps_+; 10.47(b)) Where those resonances lie is not needed. Theorem 12.3's
     forward map carries whatever finitely many there are (his Proposition 9.2(2), on 10.37(c)'s reading), and their
     exponents feed K+ through 10.46(ii)'s bookkeeping, which sharp5.py K3 checks for every iota+ exponent in
     [alpha_min, 3] -- a whole interval, not a list -- with no physical state recorded. So 10.47(b)'s "above 5/2 not
     computed" leaves nothing open beyond Proposition 9.2(2)'s finiteness.
 (c) (10.38(a)'s scaling; the h-terms of (5.28)) The exceptional exponent that 10.38(a) puts at 2 I0 - 1 = 2 enters only
     through min Re of the class's iota+ index sets (10.46), alpha_min = 3/2 + (1 - e_Ups) gam_Ups = 1.5099... If the
     h-couplings carry the further factor x_I that 10.38(a) and 10.57(b) count, the exponent rises by 1/2 or more;
     either way it is at least 2 > alpha_min, so the conclusions do not depend on the reading. The exponent itself stays
     a reading.
 (d) (C-ii, the gluing) The record's data after the shell are, on an annulus far out, an O(lam) perturbation of
     Tangherlini of mass mu_end (10.50). [CD03]'s method is dimension-free (its p. 4 and Remark 8.2), its obstruction
     the KIDs; on Tangherlini the G-invariant KIDs are d_t's alone (Proposition 10.40(i): among the fifteen Killing
     fields of 4 + 1 Minkowski only d_t is G-invariant, and Tangherlini's are d_t and so(4)'s rotations, none of those
     G-invariant), whose charge is the mass. So the gluing needs only the mass family of Tangherlini as its reference
     family -- [CD03]'s missing Proposition F.1 being, for that one-parameter family, the mass charge's monotone
     dependence on the parameter -- and it can be done G-equivariantly: the constraint map commutes with G, the solution
     is unique in the complement of the KIDs, and so it is G-invariant, as [CD03] obtains parity by uniqueness. C-ii is
     deduced on [CD03] at source; the n = 4 weighted estimates behind its Theorem 7.7 are as printed (k > n/2).

Labels: READ (the quotations); deduced (a)-(d); nothing computed or proved here.


### 10.60 The general class: the inputs at every b near b0 (E1-E2; deduced; D130)

*The setting.* Without the T^2-mirror class (ROUTES 4.60) [Hin26]'s argument runs at every b = (mu, A) near b0 =
(mu_0, 0) in the Myers-Perry family g_A of 10.36, where his statements take their spectral inputs at each b: mode
stability of the gauge potential operator, of the constraint propagation operator and of L_b at sigma != 0, Im sigma >= 0
(his Proposition 6.12, Theorem 7.1(1)-(2), Proposition 8.8, the last two from [AHW24] Theorem 6.1(1) and [Hin26a]), and
the zero energy count (his Proposition 8.11, from [AHW24] Theorem 6.1(2)). The record computed and deduced them at b0
(10.12-10.27, 10.33, 10.52-10.54). This section deduces them near b0 by perturbation, the route [HHV21] takes from
Schwarzschild to slowly rotating Kerr.

*READ.* [HHV21] (arXiv:1906.00860v2; alphaXiv, 2026-10-24; printed pages; ASCII): p. 6, "allowing us to deduce Theorem
1.1 perturbatively from the statement for Schwarzschild parameters b = b0"; p. 14, "we expect the linear stability of
higher-dimensional Schwarzschild black holes ... and their perturbations, slowly rotating Myers-Perry black holes
[MP86], to follow by similar arguments, the main task again being computational, namely the detailed mode analysis; the
general microlocal tools apply to such spacetimes as well"; p. 90, Proposition 10.11's proof, "Perturbation arguments
... imply ... the invertibility of P^_(b,gamma)(sigma) in Im sigma >= 0 for b sufficiently close to b0"; pp. 92-98,
Lemma 11.1 ("invertible for sigma in C, Im sigma >= 0, |sigma| < C_1, and |b - b0| <= C_1"), Proposition 11.3 and its
proof: "The key facts we will use ... (1) the zero energy nullspace K_b is 7-dimensional, and the generalized zero
energy nullspace K^_b is 11-dimensional, with both depending continuously on b ...; (2) suitable pairings ... are
non-degenerate for b = b0, which persists for b near b0", and "using high energy estimates as well as perturbative
arguments (starting with the mode stability of L_b0) in compact subsets of {Im sigma >= 0, sigma != 0}". [Hin26]
(printed pages): p. 5, Remark 1.4 ((a) "an r-normally hyperbolic trapped set [HPS77]", (b) "a non-degenerate source at
the conormal bundle of the event horizon"); pp. 122-124, Proposition 6.12's proof, Step 2: "the Fredholm estimates
[Hin26c, (9.107)] hold uniformly also for small perturbations of box^gamma within the class of stationary wave-type
operators ... Therefore, the low-energy estimate in [Hin26c, Theorem 9.41] holds uniformly as well ... for a fixed
neighborhood {|sigma| <= c_0, Im sigma >= 0}", and p. 122, "by inspection of the first row of box~(lambda, sigma^,
gamma^) for lambda != 0 the surjectivity (and thus invertibility)"; p. 136, Theorem 7.1, "provided b = (m, a)
sufficiently close to b0"; p. 144, section 8's "Kerr parameters b = (m, a) that are close to subextremal parameters b0";
p. 154, Proposition 8.9, "depending smoothly on b near b0", and Proposition 8.8's proof, "By [AHW24, Theorem 6.1(1)]";
pp. 200-201, Theorem 10.1's proof, "the absence of poles of L^_b(sigma)^-1 (to handle regions of bounded |Re
sigma|)--which is a consequence of mode stability (Proposition 8.8)"; pp. 208-209, Proposition 10.6, "By Proposition
8.11, the map (10.27) is Fredholm of index 0. Therefore, we only need to prove its injectivity", by Lemma 8.12's
pairings, and Proposition 10.7, "for all 0 != sigma in C with Im sigma >= 0 and |sigma| <= c, the operator L~_b(sigma)
is invertible". [Hin26c] p. 157, Theorem 8.14 (the spacetime estimate): "This holds also when P_0 is replaced by
sufficiently small perturbation within the class of stationary wave-type operators (including for different but nearby
Kerr parameters)"; p. 116, Remark 7.2: "The estimate (7.5) holds also when the underlying stationary operator P_0 is
perturbed within the class of stationary wave-type operators (Definition 5.1), which in particular allows for
perturbations of the Kerr parameters m and a". Again (D133): [Hin26] p. 119, Proposition 6.9's proof, "Since the
Fredholm estimates in [Hin26c, Theorem 9.5] hold uniformly for small perturbations of box_(g_b) (within the class of
stationary wave-type operators, to which box^Ups_(g_b,E^Ups) belongs by Lemma 6.1), it is again the same standard
functional analytic argument"; p. 204, Lemma 10.4(2), "f^(|sigma| sigma^, .) is uniformly bounded in the norm of
H^((m;k),(r+alpha_sf+1, alpha_sf+2, 0))", and (4), "f^(sigma, .) is holomorphic in Im sigma > 0 with values in
H^(m,r+alpha_sf+1)_sc"; p. 208, Proposition 10.6's proof, "By Lemma 10.4, we then have ...", "Recall moreover that
h*_(b,s0) has O(r^-2) decay (as do all other dual states in (7.15)), so integration by parts is justified ... (Given the
almost boundedness of h', this in fact only requires O(r^(-1-eta))-decay of h*_(b,s0) for any eta > 0.)"; p. 214,
(10.48), "u^_lo(sigma) = chi(|sigma|)(u^_reg,1(sigma) + F(g-dot^(Ups,aug)_b)(sigma)(b^_1(sigma)) +
F(h^(<=1,aug)_(b,s1))(sigma)(S^_1(sigma)))"; pp. 215-216, after (10.56) and (10.59), uniform bounds for F(d_t*
g-dot^(Ups,aug)_b)(sigma) and F(d_t*^2 h^(<=1,aug)_(b,s1))(sigma) "provided r < -1/2 at R_out".

*Deduced.*

 (a) (the operators near b0) g_A is a smooth family of stationary metrics, Tangherlini at A = 0 (Proposition 10.33(i)),
     differing from it at order 3 at iota+ (Proposition 10.39(ii)); so L_b, box^Ups_b and box^C_b at b near b0 are small
     perturbations of those at b0 within [Hin26c]'s stationary wave-type operators, with the same Minkowski model at
     infinity, the same indicial roots (10.12, 10.24, 10.52, 10.54: the roots see only the model, [Hin26] p. 136) and the
     same tf-normal operators (10.23, 10.25).
 (b) (high energy) The conditions [Hin26c] takes from the flow and the subprincipal symbols are strict at b0: the
     trapped set's r-normal hyperbolicity (10.17), the strong trapping admissibility of the three operators (10.17,
     10.19, 10.26), the threshold at the horizon (10.18, 10.54(e)). Normal hyperbolicity persists under small
     perturbations of the flow ([HPS77], as [Hin26] Remark 1.4 cites it) and the inequalities are open, so all hold at b
     near b0. The spectral Fredholm estimates of [Hin26c] Theorem 9.5 hold uniformly under such perturbations ([Hin26]
     p. 119, Proposition 6.9's proof), as does the spacetime estimate (7.5) ([Hin26c] Remark 7.2, p. 116; Theorem 8.14,
     p. 157), and the semiclassical estimates of [Hin26c] section 9.3 rest on the strict conditions just listed:
     invertibility at |sigma| >= C, Im sigma >= 0, uniformly in b near b0 (D133).
 (c) (intermediate frequencies) At b0 the three spectral families are invertible at sigma != 0, Im sigma >= 0 (10.16,
     10.21, 10.27); invertibility is open in (b, sigma), so it holds for b near b0 on each compact subset of {Im sigma >=
     0, sigma != 0} ([HHV21] p. 90's argument).
 (d) (low energy) box^C_b0(0) is invertible on the weighted spaces (10.21(e), for every h, 10.54) and tf-admissible by
     its model (10.23); so by [Hin26c] Theorem 9.41, uniformly for small perturbations ([Hin26] p. 124), box^C_b(sigma)
     is invertible for 0 < |sigma| <= c_0 at b near b0; box^Ups_b likewise, his Proposition 6.12's own proof. For L_b:
     the eleven states -- g-dot^Ups_b(mu-dot, A-dot), (mu-dot, A-dot) in R + so(4), and h_b,s1(S), S in S_1 -- exist at
     every b near b0, continuous in b (his Propositions 6.15 and 8.9, stated for b near b0; in five dimensions
     10.28-10.29), and are independent at b0 (10.32(c)), hence near it. The dimension of ker L^_b(0) on the weighted
     space is upper semicontinuous in b, the family being Fredholm of index 0 and continuous in b ([HHV21] Lemma 11.1's
     setting), and is 11 at b0 (10.32-10.33); so it is 11 near b0 and the eleven states span it: his Proposition 8.11 at
     b near b0, with [AHW24] Theorem 6.1(2) replaced by continuity. Lemma 8.12's pairings are continuous in b and
     non-degenerate at b0 (10.32), so near it. His Proposition 10.6, whose proof uses Proposition 8.11, Lemma 8.12,
     Lemma 10.4 and the decay of the dual states (p. 208: it needs only O(r^(-1-eta)); in five dimensions they decay
     rapidly or from rho^3, 10.31-10.32), then holds at b near b0, Lemmas 10.3-10.4 being stated for b near b0; and his
     Proposition 10.7 gives L~_b(sigma) invertible for 0 < |sigma| <= c, Im sigma >= 0. Its first row makes L^_b(sigma)
     onto: at sigma != 0, F(g-dot^aug)(sigma) = i sigma^-1 F(d_t* g-dot^aug)(sigma) and F(h^aug)(sigma) = -sigma^-2
     F(d_t*^2 h^aug)(sigma) lie in the domain of L^_b(sigma), their bounds after (10.56) and (10.59) holding with r <
     -1/2 at the outgoing radial set (pp. 215-216), and L^_b(sigma) maps them into the target by Lemma 10.4(2), (4)
     (p. 204) -- his own (10.48), u^_lo = u^_reg,1 + F(g-dot^aug)(sigma)(b^_1) + F(h^aug)(sigma)(S^_1) (p. 214). So
     L^_b(sigma), of index 0, is invertible: mode stability at low energy, [HHV21] Proposition 11.3's mechanism in
     [Hin26]'s form (D133).
 (e) (what this gives) By (b)-(d), at every b near b0 the inputs [Hin26] takes from [AHW24] and [Hin26a] hold in five
     dimensions -- mode stability of box^Ups_b, box^C_b and L_b at sigma != 0, Im sigma >= 0, and the zero energy count
     -- with constants uniform in b near b0, on the readings of 10.53-10.58 and those of [HHV21]'s perturbation arguments
     at n = 4.
 (f) (E2) His Lemma 8.15 against the rotations that do not stay Killing at a != 0: 10.34(b) modified his Step 2 so that
     those pairings are absorbed into V_1, solvable for small a by continuity; his Proposition 7.4 and (7.19) on the full
     metric: Lemma 7.5 at every spin is computed (10.36), and his proof of Proposition 7.4 uses it with his Lemmas 2.15
     and 7.2 (p. 144), which carry over as 10.29 and 10.31 carry them (deduced).

Nothing here is computed; the inputs at b0 are 10.12-10.54's. Labels: deduced ((a)-(f)); READ (the quotations); nothing
proved.

### 10.61 [Hin26] section 11 without the class (E3-E4; `general5.py` G1; D131)

In the class his Steps 1-4 reduced to one, the pole at zero energy was first order and forward solutions lost one order
at K+ (10.45); the recorded terms were those below K+ order 3 (10.46). Without the class his six steps run in full: the
boosts' second order pole costs two orders, as in four dimensions ([Hin26] p. 25: "a second order pole at sigma = 0, and
thus forward solutions of L_b lose two powers of t*-decay (at K+)"), and Theorem 11.59 records every term below K+ order
4 + eps_K.

*READ.* [Hin26] (printed pages): p. 25 (section 1.4.1's zero energy nullspace and the boosts' generalized states); p. 40
(the boost: "we produce a family of solutions g_ext,-S indexed by a (small) boost parameter S ... We then regard S in S_1
as an unknown"); pp. 218-221, 231-294 as read for 10.45-10.46 (Propositions 11.17, 11.20, 11.30, 11.32, 11.34, 11.51,
Definition 11.25, Lemma 11.28 with (11.87)-(11.88), Lemmas 11.41 and 11.45, Corollary 11.46, Theorem 11.59, Corollary
11.66); pp. 318-319, Theorem 13.1's "(1, 0), (1, 1) in E_+", the logarithmic term at iota+ "supported only on supp d
chi_K"; p. 323, its weakest terms: at iota+ "h^(-1)(S) ..., h^(0)(b - b0), h^(0,1)_s1(S^(0,1)_1) ..., and
h^(0),(1,0)_s0(S^(0),(1,0)_0) ... have a t*^-1 log t* leading-order term", at K+ "chi_K h^(<=1)_b,s1(S_rem), S_rem in
H^(oo, 2+eps_K)_b".

**Proposition 10.46 (computed; exact; `general5.py` G1).** Over every type of window5.py's five-dimensional lists and
every iota+ exponent alpha in [alpha_min, 4] (251 points, the orders linear in alpha), with sharp5.py's rule and K+
threshold 4: the eliminated terms are the six pure gauge classes s0 c0, s0 e0, s1 c0, s1 e-1, s2 e0, v1 e-1; the recorded
ones fourteen classes, those six and s1 c-1, s2 c-1, s2 c-2, s3 c-2, s3 e-1, s4 e-2, v2 e-1, v3 e-2; the recorded
physical states are s2, v2 and t2 at -2, each with no companion, exactly while alpha <= 2; and every recorded term's
L_b-image has K+ order above 4. In four dimensions at alpha = 1 the same rule gives his eight eliminated parameters and
his physical s2, v2, s3, v3 with 1, 1, 0, 0 companions.

*Proof.* G1 of general5.py, sharp5.py's routine on window5.py's lists (window5.py W1 computes their roots). Control: four
dimensions as stated. Mutant: the class's threshold 3, where no physical state is recorded. []

*Deduced.*

 (a) (the index sets at iota+) Without the class his E_+ and E-tilde_+ take their five-dimensional orders: the Kerr
     parameter changes enter at (2, 0) (the mass) and (3, 0) (the rotation), and the boost's linearization at order 2,
     g_0's part (Proposition 10.39(ii)) and h^(-1)'s, the boost's generalized state, whose four-dimensional logarithms
     ((6.31), (8.19)) five dimensions do not carry (10.28: "without his two logarithms"); his (1, 0) and (1, 1) become
     (2, 0) for these, with a logarithm at (2, 1) only if the mass patch or the s0 and s1 parameters carry one, which is
     not computed (10.46). The centre-of-mass patch h^(0)_s1(S^(0)_1) stays at (1, 0) in every dimension, but its
     leading part is pure gauge for g-bar, and what it feeds the equation -- [L_b, chi_K] h_b,s1 linearly and the
     quadratic terms along it -- has iota+ order 5 and 4 at n = 4 (10.75 (xxxvii); the sixty-fourth verifier). The patch
     aside, min Re is 2 either way, above alpha_min = min Re E^#_+ (10.44(e)), so the least iota+ exponent the sources
     carry is alpha_min, as in the class: Proposition 10.46's hypothesis. A logarithm changes only the log power of the
     K+ terms it feeds, which his parameters S^(lam,k) index.
 (b) (Steps 1-4 with the boosts) His Propositions 11.17, 11.20, 11.30, 11.32 and 11.34, Lemma 11.45 and Corollary 11.46
     run with the five-dimensional states -- h_s1 for the four translations and h^(<=1)_s1 for the four boosts
     (10.28-10.29), the second order pole that the chain to Proposition 10.29(iii)'s pairing (3 pi^2/2) mu ends
     (10.35(b)), augmentation #1 with S in S_1, the parameters b-dot = (mu-dot, A-dot) in R + so(4) and the S_1
     modulations -- and with the inputs at b near b0 of 10.60: f of K+ order in (2, 2 + eps_K) at Step 4, u~ two orders
     lower; the Kerr parameter change removed by his Lemma 11.45 at b near b0, the boost by S, the constant and
     logarithmic centre-of-mass motions by S^(0)_1 and S^(0,1)_1. Whether five dimensions carry his log t* h_b,s1 of
     (9.39b) is not computed (10.35(b)'s question); its parameter is zero if not.
 (c) (Steps 5-6) His Proposition 11.51, Theorem 11.59 and Corollary 11.66 run with Proposition 10.46's lists in place of
     (9.39b)'s at alpha = 1 and his threshold 4 + eps_K: the six classes eliminated at every exponent of K+ order at most
     2, the fourteen recorded with their companions, and the physical s2, v2 and t2 recorded as his s2 and v2 are
     ((11.196b)). The tensor type t2 is the one kind his lists lack: a physical state that exists in five dimensions
     (10.34(a), the static tidal solutions, with his Proposition 8.14's construction near b0 in 10.34(c), the tensor
     types included), recorded by a parameter T_2 beside his S_2 and V_2.
 (d) (the requirements on h and the weights) As his: h of K+ order 4 + eps_K for the linearization of P in b (Remark
     11.61), L - L_b of 2 + eps_K; the weights 3 + eps_I at I+ and 3 + eps_+ at iota+ in the five-dimensional gaps
     (10.46(e), iplus5.py P2).
 (e) (what this gives) His section 11 in five dimensions without the class: forward solutions with the class's orders at
     I+ and iota+, two orders of loss at K+, the Kerr parameter, boost, centre-of-mass, pure gauge and physical terms
     recorded as his parameters -- on the readings of 10.39-10.45, 10.53-10.58 and 10.60.

10.39's OPEN "the boost entry ... by computation" is answered by 10.28(iii)'s computed stationary residual of order
rho^3, and 10.40's on the boosts' columns follows from those orders with the transfer of 10.55. OPEN: the logarithms of
(a) and (b), covered either way. Labels: computed (Proposition 10.46); deduced ((a)-(e)); READ; nothing proved.

### 10.62 [Hin26] sections 12, 5 and 13 without the class (E5-E6; deduced; D131)

*READ.* [Hin26] (printed pages): pp. 296-318 as for 10.47 (Definition 12.1, (12.11)-(12.16), Theorems 12.3 and 12.8); pp.
76-81 (section 3.4, the asymptotic boost diffeomorphism phi_S, the identity in r <= 5 m_0) and pp. 108-110 (section 5.6,
Theorem 5.23); pp. 318-323, Theorem 13.1 and its proof, "there exist b = (m, a) and S in S_1, with |b - b0| and |S|
small", "g = g_(b0,b,-S) + h ... attains the initial data (phi_S)_*(gamma, k) at phi_S(Sigma_IVP)", "O(t*^(-2-eps_K)) in
spatially compact subsets", and Remark 13.2, "Theorem 13.1 remains valid if ... we replace b0 with parameters b1
satisfying |b1 - b0| < eps".

*Deduced.*

 (a) (Definition 12.1 in five dimensions) U = (b - b0, S, S^(0)_1, (u^0_lam, f_lam), S_rem, b_rem, V_1,rem,
     (S^(0)_l,rem)_(l=0,2), (S^(-lam^Ups_sl,1+1)_l,rem)_(l=0,1), h~) with b in R + so(4) (seven), S, S^(0)_1, S_rem in
     S_1 (four each) and V_1,rem in so(4) (six); p-vec and q-vec his (12.14)-(12.15) with Proposition 10.46's lists, the
     physical T_2 added, and the orders of 10.61.
 (b) (Theorems 12.3 and 12.8) His proofs with 10.61 in place of his section 11: P(Phi(U)) in his (12.31)'s space with the
     five-dimensional orders, and right inverses with tame estimates.
 (c) (section 5 with the boost) His section 3.4's phi_S is a Lorentz boost of R^(4,1) near infinity; the boosted
     Tangherlini metric differs from Tangherlini at order 2 at iota+ (Proposition 10.39(ii)), inside E_+ (10.61(a));
     Theorem 5.23 pulls back 10.48's exterior solutions of Theorem 5.17 by phi_S, its proof the boost theorem for the
     exterior problem, at n = 4 on 10.48's readings.
 (d) (Theorem 13.1 in five dimensions, without the class) Let mu_0 > 0, Sigma_IVP and E_0 be as in 10.49, and let (gamma,
     k) satisfy the constraints, its decay (13.1a) with 10.49's orders and its smallness (13.1b), with no symmetry. Then
     there are b = (mu, A) near (mu_0, 0) and S in S_1 small, and h as in (13.2) with 10.61's index sets, such that g =
     g_(b0,b,-S) + h attains (phi_S)_*(gamma, k) at phi_S(Sigma_IVP), Ric(g) = 0, and g settles to the Myers-Perry metric
     g_b at the rate O(t*^(-2-eps_K)) in spatially compact subsets of {r >= r_0}, the weakest K+ term chi_K
     h^(<=1)_b,s1(S_rem) as his. The proof is his Steps 1-4 with (a)-(c), 10.60-10.61 and [SR89] as in 10.49(c); by his
     Remark 13.2 b0 may be replaced by any b1 near it.

Labels: deduced ((a)-(d)), on the readings of 10.39-10.48, 10.53-10.58 and 10.60-10.61; READ; nothing computed here,
nothing proved.

### 10.63 Phase C without the class: gluing to the Myers-Perry family (E7; `general5.py` G2; D132)

In the class (10.50) the data of g_lam after the shell were glued at large radius to exact Tangherlini, the obstruction
being the G-invariant Killing initial data, d_t's alone, matched by the mass. A perturbation without symmetry meets the
whole obstruction space -- the fifteen Killing initial data of 4 + 1 Minkowski space -- and is matched by a member of the
translated, rotated and boosted Myers-Perry family, by its Poincare charges: [CD03]'s gluing, whose Remark 8.2 names the
one element missing in higher dimensions.

*READ.* [CD03] (arXiv:gr-qc/0301073v2; alphaXiv, 2026-10-24; printed page = PDF page): p. 34, Theorem 7.7 ("for all
sigma >= 2 - n"); pp. 35-37, Theorem 8.1 and its proof ("Let, as in Appendix F, K_i0 denote the set of initial data for
boosted, rotated, and translated Kerr metrics", (8.7): "the maps lam F_lam converge ... to the map Q of Proposition F.1;
that last map is a homeomorphism", "taking V in R^10 to be a ball around (Q^0_(i)) of a radius small enough so that V is
included in the image of the map Q"); p. 36, Remark 8.2, "The argument below carries over to any dimension, the only
element missing is an equivalent of Proposition F.1 for the family of translated, rotated, and boosted Myers-Perry
metrics"; p. 38, a reference family's condition 4, "The map which to (K_omega, g_omega) assigns its Poincare charges
(p_mu(omega), J_munu(omega)) is a diffeomorphism between Omega and an open subset of R^10"; p. 72, (E.5b) "n/2 - 1 <
alpha <= n - 2" and the parity condition (E.9) "alpha_- > alpha, alpha + alpha_- > n - 1"; pp. 75-77, (E.26)-(E.27),
Appendix F and Proposition F.1 with (F.4)-(F.6) ("p_mu = (m, 0, 0, 0), J_munu = 2 m a delta^1_[mu delta^2_nu]", "J_0i =
-m a_i"), and its parity argument for Kerr in Boyer-Lindquist coordinates ("the coordinate components of the shift
vector are odd").

**Proposition 10.47 (computed; exact; `general5.py` G2).** On the linearizations at five-dimensional Tangherlini (the
static spatial metric of mass mu) in the mass, in the four boosts, in the six rotations W in so(4) (the shift mu (W x)_i
/ r^4, Proposition 10.33(iii)'s leading term) and in the four translations, the ADM energy, momentum, angular momentum
and centre-of-mass fluxes at infinity (G = 1) are E = 3 pi mu/8 at Tangherlini, dE/dmu = 3 pi/8, P = -E v (v the
velocity of the coordinate boost, the black hole moving with -v in the new coordinates, the sign of [CD03]'s
transformation law (E.14)), J(W) = (pi mu/4) W -- two thirds of E per unit spin -- and E C = E c, every other entry 0:
the 15 x 15 Jacobian of the charges in the parameters is diagonal with determinant (3 pi/8)(pi mu/4)^6 (3 pi mu/8)^8,
nonzero for mu > 0. In four dimensions the same fluxes give E = m, P = -m v, J = m a, E C = m c, [CD03]'s (F.4)-(F.6).


*Proof.* G2 of general5.py: each flux of the linearized data split into its parts homogeneous in (x, r), the part of
degree -(n - 1) integrated exactly over the unit sphere, higher parts checked to integrate to zero, lower ones vanishing
in the limit. Control: four dimensions as stated. Mutant: mu = 0. []

*READ again (D133).* [CD03] p. 35, (8.1) as printed: "|g^-_ij| + r|d_k(g^-_ij)| + r|K^-_ij| <= C(1 + r)^-alpha_-,
alpha_- > alpha, alpha + alpha_- > 2", "the 3 + 1 equivalent of the parity conditions (E.9)"; p. 36, Remark 8.4: "The
ADM momentum and angular momentum of (K^_R, g^_R) converges to that of (K, g) as R tends to infinity"; p. 38, "the
collection of initial data obtained from boosted and space-translated Kerr space-times provides an example of a
reference family"; p. 72, (E.8), "x^mu -> -x^mu", (E.9), and "(E.5), (E.8) hold for the Kerr metric in the
Boyer-Lindquist coordinates ... with alpha = 1 and alpha_- = 2"; p. 77, "the coordinate components of the shift vector
are odd ... the Christoffel symbols are odd while the partial derivatives of the coordinate components of the shift
vector are even". [ER08] p. 14, (34): "M = (d - 2) Omega_(d-2) mu/(16 pi G), J = 2 M a/(d - 2)"; p. 16: "The relation
between mu and a_i and the mass and angular momenta is the same as (34)". [Hin26] p. 3: section 5.7.1, "Initial data at
Boyer-Lindquist time 0"; p. 319, Remark 13.2 (the verifier's reading: b0 replaced by Kerr parameters b1 = (m1, a1)).

*Deduced.*

 (a) ([CD03] Proposition F.1's equivalent near Tangherlini) The family -- g_A (10.36) for A in so(4), translated and
     boosted by Poincare transformations of R^(4,1) near the identity -- has 1 + 6 + 4 + 4 = 15 parameters for the
     fifteen Poincare charges (p_mu, J_munu) of 4 + 1 dimensions. Its charge map is smooth: g_A's charges are the exact
     Myers-Perry ones, E = 3 pi mu/8 and J = (pi mu/4) A up to orientation ([ER08] (34), pp. 14 and 16, at d = 5 with
     Omega_3 = 2 pi^2), polynomial in (mu, A), and the Poincare transformation carries them polynomially in its
     parameters ([CD03]'s transformation law (E.14), p. 73, which its Appendix F uses) (D133); and by Proposition 10.47
     its derivative at Tangherlini is invertible; by the inverse function theorem it is a diffeomorphism from a
     neighbourhood of (mu_0, 0, 0, 0) onto a neighbourhood of Tangherlini's charges (3 pi mu_0/8, 0, 0, 0): [CD03]'s
     reference family condition 4 near Tangherlini, and the homeomorphism onto a set containing a ball that its proof of
     Theorem 8.1 uses.
 (b) (decay and parity) [CD03]'s parity condition (E.9) bounds the part of the spacetime metric odd under x^mu -> -x^mu,
     time included ((E.8), p. 72). A metric even under (E.8) has on x^0 = 0 an even spatial metric and an odd second
     fundamental form, k being built from d_t gamma_ij and D_(i Y_j), both odd; so the 3 + 1 form of (E.9) bounds
     gamma^- and k^+: |gamma^-| + r |d gamma^-| + r |k^+| <= C r^(-alpha_-). As printed, (8.1) (p. 35) bounds r |K^-|,
     and boosted Kerr would fail it: on the slice t = v x of a static metric -N^2 dt^2 + h, the boosted slice to first
     order in v, K = v N Hess_h(x) + O(v^2) up to sign, Hess_h(x)_ij = -Gamma(h)^x_ij, which for Schwarzschild in
     isotropic coordinates is odd and of order m r^-2, so r |K^-| is of order r^-1 and (8.1) would force alpha_- <= 1 <
     alpha -- though p. 38 makes boosted Kerr a reference family; and the Kerr value alpha_- = 2 of p. 72 is that of
     Kerr's even K, of order r^-3 (its evenness on p. 77, the order from the shift's r^-2). We read (8.1) with k^+
     (deduced; D133). (The fifty-ninth verifier read boosted Kerr as meeting (8.1) with alpha_- = 2; that drops (8.1)'s
     factor r, and the reading stands, D143.) At n = 4, with alpha = 2 (inside (E.5b)'s (1, 2]), (E.9) asks alpha_- > 2.
     The members: in static coordinates their spatial metrics differ from the Euclidean one at order r^-2 and are even,
     their shifts odd and of order r^-3, so k = k^+ is O(r^-4) and alpha_- = 3; a boost maps even and odd parts to
     themselves and a translation adds a derivative of the even part, of order r^-3 (alpha_- = 3 > alpha, alpha +
     alpha_- = 5 > n - 1 = 3), as [CD03] p. 77 argues for Kerr in Boyer-Lindquist coordinates (deduced for Myers-Perry
     the same way). The data: on 10.50's tau-slice they are exact Tangherlini outside a compact set, but tau = v - r = t
     + (r* - r) = t - mu/r + O(r^-3) (exterior5.py X1), so there their k is even and of order mu r^-3: alpha_- = 2, the
     borderline (E.9) excludes. So the gluing is done on a Cauchy surface Sigma'' of their development that is the
     tau1-slice on a large ball and a static slice {t = t1} of the exterior Tangherlini metric beyond a larger one: the
     development is that metric there (10.50(c)), and t - t1 interpolated by a cut-off between 0 and -mu/r + O(r^-3) has
     a gradient of size mu r^-2, so Sigma'' is spacelike. It is [Hin26]'s own initial surface near infinity (his section
     5.7.1, "Initial data at Boyer-Lindquist time 0"), his Remark 13.3 returning to a tau-level set. On Sigma'' the data
     have gamma^- = 0 and k = 0 outside a compact set, and a perturbation (gamma~, k~) with |gamma~^-| + r |d gamma~^-|
     + r |k~^+| <= C r^(-alpha_-), alpha_- > 2, keeps (E.9). G-invariance, which makes gamma and k even, does not give
     this: it removes gamma^-, not k^+. (The class's gluing, 10.50(c) and 10.59(d), needs no parity condition. On the
     data, [CD03] uses (E.9) only for the convergence of the charges J^munu, angular momentum and centre of mass
     ((E.19), (E.20b), O(R_0^(n - 1 - alpha - alpha_-)); Proposition E.1, pp. 73-74); the energy-momentum p^mu converges
     without it ((E.17), (E.20a); D138). Its two other uses fall on the reference family, not the data: that Lorentz
     transformations preserve (E.5) and (E.9), and that the integral over T_R in (E.22) vanishes for J^munu "again by
     parity considerations" (p. 74) -- the steps to (E.23) and so to the transformation law (E.14) that (a) uses -- and
     the Myers-Perry members meet (E.9) with alpha_- = 3, as above. And (E.20b)'s bulk term (1/(16 pi)) int_(r >= R_0) T
     X, which for a linear KID (E.12)'s bound alone would not make finite, vanishes: the data are vacuum, as Theorem 8.1
     assumes ("suppose that (K, g) satisfies the vacuum constraint equations", p. 35) and as g_lam's development is
     (D143). The charge of a KID Y on a sphere about the origin is linear in Y and equivariant, so on G-invariant data
     it is the charge of Y's average over the compact G, a multiple of d_t (10.50): the pairings with the other KIDs
     vanish at every radius, and the mass converges for alpha > n/2 - 1 = 1, (E.17)'s O(R_0^(n - 2 - 2 alpha)) (deduced;
     D136).)
 (c) (C1-C2 without the class) Let (gamma', k') be the data on (b)'s Sigma'' of the glued development of 10.50(c)-(d) --
     which contains g_lam on Omega and is exact Tangherlini outside a compact set of Sigma'' (D136) -- plus any
     perturbation that satisfies the constraints, is small in the norms of 10.62(d) and has (b)'s parity or decays
     faster than r^(-3/2) (10.66(d); D143). 10.50's construction runs with [CD03] Theorem 8.1's proof in five dimensions
     (Theorem 7.7 is stated in general n): glued on an annulus to a member of the family whose charges lie in a small
     ball about those of (gamma', k') -- they converge to them as R -> infinity ([CD03] Remark 8.4), not equal them
     (D133) -- inside (a)'s neighbourhood since those are near Tangherlini's, the obstruction the full
     fifteen-dimensional space of Killing initial data, matched by (a). The glued data equal a translated, rotated and
     boosted Myers-Perry metric outside a compact set, and near spatial infinity their development is that metric by
     finite speed of propagation.
 (d) (C3 without the class) 10.62(d) with the glued member as the reference near infinity: his Remark 13.2 (p. 319)
     replaces b0 by Kerr parameters b1 = (m1, a1), which covers the member's mass and spin; its boost and translation
     add to gamma terms of orders r^-2 and r^-3 and to k terms of order r^-3, polyhomogeneous and small, which lie in
     10.49's class -- there min Re E_0 > 3/2 + 2 gam_Ups, so E_0 may contain 2 + N, while in four dimensions a boost
     changes the data at r^-1, outside his class (D133): the maximal vacuum development settles to a Myers-Perry metric
     g_b, b = (mu, A) near (mu_end, 0), at the rate O(t*^(-2-eps_K)) in spatially compact subsets of the exterior, the
     initial slice boosted by phi_S -- on the readings of 10.49-10.50, 10.53-10.59 and 10.60-10.62.

Labels: computed (Proposition 10.47); deduced ((a)-(d)); READ; nothing proved. The equivalent of [CD03]'s Proposition F.1
is computed and deduced here near Tangherlini only, which is the case the gluing needs; its global form for the
Myers-Perry family is not attempted.

### 10.64 [Hin23a] section 3 at n = 4 by modification: every place the dimension enters (`exterior5.py`; D134, D136)

*The setting.* [Hin23a]'s section 3 is the one reading behind Theorem 4 that is a whole proof in another dimension
rather than estimates on symbols: [Hin26] Theorem 5.17 is solved by its energy estimates and [SR89] (10.48(c), 10.57).
Its calculus is dimension-free (10.57 (1)); the dimension n of space enters its section 3 at eight places. Each is
computed here at n = 3, against his printed values, and at n = 4, and his proof is then run at n = 4 with the computed
quantity in place at each.


*READ.* [Hin23a] (arXiv:2302.13804v1; alphaXiv, 2026-10-24; printed page = PDF page; ASCII): pp. 3-4, (1.3)-(1.6); p. 7,
(2.1)-(2.6) and Definition 2.2, "delta*_(g,E_C) := delta*_g + gamma_C (2 c_C (x)_s (-) - g iota_(g^-1)(c_C))",
"delta_(g,E_Ups) = (delta*_(g,E_Ups))^* = delta_g + gamma_Ups (2 iota_(g^-1)(c_Ups) - c_Ups tr_g)", (2.7), x^0 = t + r,
x^1 = t - r, and (2.9)'s splitting; p. 8, (2.10)-(2.11) and Remark 2.3, "G_gbar A*_(E_C,E_Ups) G_gbar = -A_(E_Ups,E_C)";
pp. 8-9, (2.14)-(2.15b); p. 12, Lemma 3.6, "Put xbar_I := min(sqrt3/2, 1/sqrt(8m)) when m > 0", its proof, "r = rho_0^-1
x_I^-2 > (1/2) x_I^-2 > 4m", and (3.8), "g_m^-1(r d rho_I, r d rho_I) = (2 x^1/r)(1 + (x^1/2r)(1 - 2m/r)) < 0" (D136);
p. 16, Proposition 3.17's proof, "mu_b = rho_0^4 rho_I^3 |dg_m| is a smooth positive b-density", (3.22)-(3.25); p. 17,
Definitions 3.19-3.20 ("l_I < min(-gamma_Ups, l_0, 1/2)", "k >= 3"); p. 18, Notation 3.22 ("O^(alpha,beta)_3 into
rho_0^alpha x_I^(2 beta) L^inf"), Lemma 3.23; p. 20, Lemma 3.25; pp. 21-25, Definition 3.27, Lemma 3.28, Proposition
3.29 and its proof, (3.30)-(3.46), with (3.34), (3.36), (3.39), (3.40), (3.42) and (3.43); p. 26, Corollary 3.31,
(3.47)-(3.49); pp. 27-30, Proposition 3.32, Lemma 3.33 ("with n = 4"), Lemma 3.34; pp. 30-32, (3.59a)-(3.59b), Theorem
3.35, Corollary 3.36; p. 33, Remark 3.38. With 10.57's READ (1)-(4).


**Proposition 10.48 (computed; `exterior5.py` X1-X8).** For n = 3 and n = 4, with k = (n - 1)/2:

 (X1) r^k box r^-k = 4 d_0 d_1 + ((n - 1)(n - 3)/4) r^-2 on functions of (x^0, x^1), with no first-order term: the added
     term 0 at n = 3 (his (3.34)) and 3/4 at n = 4. Tangherlini's r* - r = -mu/r - mu^2/(3 r^3) - mu^3/(5 r^5) - ..., a
     series in 1/r without the logarithm of his r* = r + 2m log(r - 2m).
 (X2) rho_0^(n+1) rho_I^n |dg| = |d rho_0/rho_0 d rho_I/rho_I dg-slash| exactly on Minkowski, rho_0 = 1/(r - t), rho_I =
     (r - t)/r: his mu_b at n = 3, rho_0^5 rho_I^4 |dg| at n = 4 -- the density for which L = 2 rho_I rho^-(2+k) P'
     rho^k is symmetric (rho_I^-1 rho^(2+2k) = rho_I^-1 rho^(n+1)).
 (X3) For the model L0 = -2 rho_I d_rho_I (rho_0 d_rho_0 - rho_I d_rho_I) + x_I^2 (Lap + q_n), q_n = (n - 1)(n - 3)/4,
     and his W = w^2 V of (3.22), the principal symbol of [L0, W] - (div W) L0 is w^2 (-4 alpha_I (xi_0 - xi_I)^2 + 4 c
     (alpha_0 - alpha_I) xi_I^2 + (1 + 2 (alpha_0 - alpha_I) + c (1 - 2 alpha_I)) x_I^2 (lambda + q_n)), lambda the
     angular operator's value: his (3.25) with Lap + q_n for Lap, q_n entering only with the angular operator (exactly,
     at xi = 0).
 (X4) A_(E_C,E_Ups) of (2.10), built from Definition 2.2's operators on S^2 T* R^(1+n) in the frame (dx^0, dx^1, r e^a),
     c = r^-1 dt, and reduced to (2.9)'s splitting (00, 01, 0a, 11, 1a, tr, tf), tr the coefficient of r^2 g-slash: at n
     = 3 his (2.11), with his (3.36), (3.39), (3.40), (3.42) and (3.43) as intermediates; at n = 4 (gC = gamma_C, gU =
     gamma_Ups)

          2gC      0        0       0       0       0                0
          -gU      -3gU/2   0       0       0       3gU/8            0
          0        0        gC      0       0       0                0
          0        -3gU     0       -2gU    0       3gC/2 + 3gU/4    0
          0        0        gC-gU   0       -gU     0                0
          2gC      0        0       0       0       3gC/2            0
          0        0        0       0       0       0                0

     The dimension enters through the trace: G's (n - 1)/4 and (3 - n)/2 and (2.5)'s (n - 1)/2 c tr. At both n: pi_C's
     block closed; A lower triangular in ran pi_CUps + ran pi-slash_0 + ran pi_11; the duality G^-1 A*_(E_C,E_Ups) G =
     -A_(E_Ups,E_C) on all of S^2 T*, Remark 2.3's with G^-1 = G only at n = 3. Diagonal: pi_CUps's 2gC, gC, gC, -gU,
     -gU at n = 3 (his (2.15a)-(2.15b)) and 2gC, gC, 3gC/2, -3gU/2, -gU at n = 4; pi-slash_0's 0; pi_11's -2gU.
 (X5) For g = -dx^0 dx^1 + r^2 (g-slash + r^-k chi(x^1) T), T = d theta_1^2 - sin^2 theta_1 d theta_2^2 trace-free, the
     chi'^2 term of R_11 is r^-2k/2 exactly: r^-2 at n = 3, r^-3 at n = 4. Against the terms of L = 2 rho_I rho^-(2+k)
     P' rho^k, of size r^-(1+k), the ratio is r^(1-k): 1 at n = 3 -- his (3.47), where -(1/2) |d_1 pi-slash_0 h|^2
     sources h_11's leading term (Remark 3.38's mass loss) -- and r^-(1/2) at n = 4.
 (X6) The least integer above dim M/2 is 3 at n = 3 and at n = 4 (Notation 3.22's k >= 3, O_3 in L^inf); Lemma 3.33's
     d_(dim M - 1) is 2 at n = 3 and 3 at n = 4.
 (X7) For g = g-bar + r^-k h, h a frame component of size 1 -- h_ab = chi(x^1) T_ab or h_11 = eta(x^1) -- and u = r^-k
     f(x^1) U, the principal h u part of L_2 = 2 r^(k+1) P r^-k -- the four derivative-squared monomials -- for P(g) =
     Ric(g) - delta*_(g-bar,E_C) Upsilon(g; g-bar), which is his (3.30)'s operator 2P'_g but for the gamma_Ups term,
     which carries G_(g_m) and does not enter the h u part, in the frame: in (7,1) (U = (dx^0)^2, angular output) chi'
     f' and chi'' f with coefficient 4 T-hat each; in (4,7) (U = T, output (dx^1)^2) chi' f' with -2 and no chi'' f; in
     (4,1) (h_11, U = (dx^0)^2) eta'' f with 4. At n = 3 these are r-independent and are his printed entries in L_2's
     normalization: twice A(7,1) = 2 d_1 h_ab on d_1 u and twice B(7,1) = 2 rho_0^-1 d_1^2 h_ab on u, 4 and 4; twice
     A(4,7) = -(1/2) d_1 h_ab, -2, B having no (4,7) entry, when the entry -- which maps the tf block to the scalar
     (dx^1)^2 block -- acts by contraction, -(1/2) d_1 h_ab u^ab with |T|^2 = 2. Read instead as a coordinate on a unit
     tf basis, the printed entry would give -1: the identification of this one entry rests on the reading (D138), the
     computed -2 does not; twice B(4,1) = 2 rho_0^-1 d_1^2 h_11, 4. At n = 4 they are the same numbers times r^-(1/2) =
     r^(1-k), exactly. Each entry is linear in h.
 (X8) Lemma 3.6 at n = 4: with f = 1 - mu/r^2, r* = r + (sqrt(mu)/2) log((r - sqrt(mu))/(r + sqrt(mu))) (dr*/dr = 1/f),
     x^0 = t + r*, x^1 = t - r*, rho_0 = 1/(r* - t) and rho_I = (r* - t)/r, d rho_0 = rho_0^2 dx^1 is null and g^-1(r d
     rho_I, r d rho_I) = (2 x^1/r)(1 + x^1 f/(2r)), his (3.8) with f for 1 - 2m/r. With xbar_I = min(sqrt3/2, 1/(2
     mu^(1/4))) for his min(sqrt3/2, 1/sqrt(8m)), r = rho_0^-1 x_I^-2 > (1/2) xbar_I^-2 >= 2 sqrt(mu), twice the horizon
     radius as his 4m is: r* is defined, f > 3/4 (his 1/2), x^1/r = -x_I^2 < 0 and |x^1 f/(2r)| < 3/8, so (3.8) is
     negative.

*Proof.* X1-X8 of `exterior5.py`, sympy, exact: X1 from the wave operator of g = -dx^0 dx^1 + r^2 g-slash and the series
of r*; X2 from the Jacobian of (t, r) in (rho_0, rho_I); X3 by applying [L0, W] - (div W) L0 to e^(i (xi_0 log rho_0 +
xi_I log rho_I)); X4 on every symmetric 2-tensor, the reduction checked against the image of each representative; X5
from the Christoffel symbols of the stated metric on S^2 and S^3; X7 likewise, P's h u part as the mixed derivative in
two parameters; X8 from the null form of g_m and the bound at r = 2 r_h. Controls: n = 3 gives his (2.11), (3.25),
(3.34), mu_b, the five intermediates, Proposition 3.29's h-dependent entries -- three as printed, the fourth under the
contraction reading of X7 -- and Lemma 3.6's 4m. Mutants: conjugation by r^-((n-2)/2) (X1), div W dropped (X3), G with
1/4 for 1/2, and the sign of (2.4)'s g-term (X4), h scaled by r^-((n-2)/2) (X7), and his 1/sqrt(8m) at n = 4 (X8) --
each caught. []


*Deduced: [Hin23a] section 3 at n = 4, by modification.* With g_m Tangherlini of mass mu, r* as in X1, rho_0 = 1/(r* -
t), rho_I = (r* - t)/r, x_I = rho_I^(1/2), g = g_m + r^-(3/2) h and L_g := 2 rho_I rho^(-7/2) P'_g rho^(3/2), his
section 3 runs as follows.

 (a) (Sections 3.1-3.2, Lemmas 3.6-3.16.) The calculus is dimension-free (10.57 (1)), M now with S^3 fibres; Lemma 3.6
     holds with xbar_I = min(sqrt3/2, 1/(2 mu^(1/4))) (X8). r* - r is smooth in 1/r (X1), so the coordinates are
     Minkowski's up to smooth corrections, the logarithms of his (1.1) absent.
 (b) (Proposition 3.17.) L = -2 rho_I d_rho_I (rho_0 d_rho_0 - rho_I d_rho_I) + x_I^2 (Lap + 3/4) mod x_I Diff^2_(e,b)
     (X1; the mass enters at r^-2 = rho_0^2 rho_I^2), symmetric on L^2(M, mu_b) with mu_b = rho_0^5 rho_I^4 |dg_m| (X2).
     His multiplier (3.22) gives Q-bar of (3.25) with Lap + 3/4 in place of Lap, positive elliptic under his conditions,
     the added term only increasing it (X3). His estimate (3.21) and its proof by commuting b-vector fields follow
     unchanged: [x_I^2 3/4, X_j] lies in x_I^2 C^oo, of Lemma 3.16's form.
 (c) (Definitions 3.19-3.20, Notation 3.22.) The projections carry (1/3) g-slash^(ab) h_(ab), the trace over S^3, for
     his (1/2) g-slash^(ab) h_(ab); the spaces are his, k >= 3 (X6).
 (d) (Lemmas 3.23-3.28, Corollary 3.26.) Each h-dependent order gains rho^(1/2) = (rho_0 rho_I)^(1/2), one factor
     r^-(3/2) for r^-1, and the mass terms rho_0 rho_I (mu r^-2 for 2m r^-1); the leading Minkowski coefficients are
     those of X4's frame. His memberships hold a fortiori.
 (e) (Proposition 3.29.) L_g = -2 (rho_I d_rho_I - A)(rho_0 d_rho_0 - rho_I d_rho_I) + x_I^2 (Lap + 3/4) + L~_g with A
     X4's matrix at n = 4. The h-dependent entries of his A_g and B_g, each linear in h, are at n = 4 his n = 3 values
     times r^-(1/2) (X7), so they join L~_g, which stays in (x_I C^oo + H^(k-2,(l_0, 2 l_I))_b) Diff^2_(e,b) since l_I <
     1/2. So at n = 4 A_g = A, h-free and lower triangular with scalar diagonal (X4): the hypothesis of his sharp-weight
     step holds outright, as 10.57(b) found, with the orders computed for R_11's quadratic term (X5) and for the
     h-dependent entries (X7) (D136).
 (f) (Corollary 3.31.) (3.49) holds with A; the (dx^1)^2 component's quadratic term lies r^-(1/2) below the linear one
     (X5), in O^(l_0,l_I)_(k-2), so (3.47) at n = 4 reads 2 rho_I rho^(-7/2) P(g) (his printed 2 rho_I^-1 rho^3 a
     misprint for 2 rho_I rho^-3, by Definition 3.27; D157) in rho_0^-1 (-4 gamma_Ups d_1
     h_11)(dx^1)^2 + O^(l_0,l_I)_(k-2): no radiation term at leading order. (The five-dimensional mass aspect, at r^-2 =
     r^-(3/2) r^-(1/2), lies below the radiation field: X5's ratio.)
 (g) (Proposition 3.32.) The basic estimate (3.53) is (b)'s, Q-bar dominating the skew-adjoint part (L_g^* - L_g) W for
     alpha_I large and negative, as his. The tame estimate (3.51) commutes the same b-vector fields, the Sobolev counts
     unchanged (X6). His A^0_h term, the one use of Lemma 3.33 (with d_(dim M - 1) = 3 at n = 4), is absent: A_h = A_g -
     A_(g_m) has no leading term at I+ (e), so all of A_h is treated as his A~_h, "like the contribution from L~_g". The
     sharp-weight step uses (e) and alpha_I < min(alpha_0, 0), as his.
 (h) (Theorem 3.35.) The decay recovery integrates the I+ normal operator rho_I d_rho_I - A block by block: pi_CUps by
     its eigenvalues, whose least positive entry is -gamma_Ups in both dimensions when -gamma_Ups < gamma_C (X4), so l_I
     < min(-gamma_Ups, l_0, 1/2) serves as his; pi-slash_0 by 0, the radiation field; pi_11 by -2 gamma_Ups, with no
     source at leading order by (f), so at n = 4 h_11 has no leading term at I+. (For [Hin26]'s use this theorem is not
     needed, 10.57(c).)
 (i) (Corollary 3.36.) [SR89] with the loss of derivatives of (g)-(h), finite, which is all it needs, for data small in
     H^(16 d^2 + 43 d + 24) (2433 at his d = 11); the gauge and Ricci flatness by the second Bianchi identity in any
     dimension (10.57(d)).

This replaces B10's reading by a proof by modification: every place n enters [Hin23a]'s section 3 is computed, and each
step above is his with the computed quantity in place. For [Hin26] Theorem 5.17's use (10.48(c)), his later gauge's A_0
at n = 4 is 10.38's, lower triangular with h-free diagonal; X1-X3, X5 and X6 are the same there.

Labels: computed (Proposition 10.48, X1-X8; X7's identification with his (3.29) READ, one entry under a stated reading);
deduced ((a)-(i)); READ; nothing proved. What remains of B10 is that his proofs, read step by step, use n only where
(a)-(i) name it: the census read at source, each replacement computed.


### 10.65 [Hin26a] section 5.2 at n = 4: the calculus and the commutators (B4; D135)

*The setting.* 10.22 computed in five dimensions every input [Hin26a] section 5.2 takes from the metric and from c, and
10.56 narrowed B4 to one reading: that the commutator computations of his sections 5.2.1-5.2.6, not redone at n = 4,
give the signs of the computed five-dimensional symbols. Here they are redone at source. Each is an identity of
semiclassical symbols in which the dimension does not appear, on a calculus constructed in every dimension.

*READ.* [Hin23d] (arXiv:2302.13803v1; alphaXiv, 2026-10-24; printed page = PDF page): p. 3, "(t, x) in R x R^(n-1) =
R^n"; p. 7, "polar coordinates r = |x|, omega = x/|x| in S^(n-2)", the 3b-vector fields "r d_t, r d_r, d_omega" (1.7)
and Diff^m_3b(M) (1.9); pp. 10-11, section 1.1.1, "3b-analysis on R^n takes on a particularly clean form on an
appropriate compactification of R^n = R_t x R^(n-1)_x"; p. 12, "One can also define 3b-ps.d.o.s (modulo the space
Psi^-oo_3b(M) of residual operators) as bounded geometry pseudodifferential operators [Shu92] on M^o ... this
perspective immediately gives a composition law and suffices for the purposes of symbolic analysis"; p. 109, Proposition
5.10, the composition law, stated for every n. [Hin26a] (arXiv:2606.27658v2; alphaXiv, 2026-10-24): p. 10, the sink's
weight from "(the eigenvalues of) the subprincipal term E", "cf. Lemma 4.2 and Proposition 5.11"; p. 38, Proposition 5.1
(3)-(6); p. 47, (5.31)-(5.32), J = h^2 J_0 + h^3 J_1; pp. 51 and 53, the commutants of Propositions 5.8(2) and 5.9 and
their principal symbol identity "a H_(-l+j) a + S a^2 = c_0 a^2 + b_0^2 + b_K^2 - e^2 + f", b_0 at the corner
"(rho_sf^-2 [-l(dw/w)] + S + w^-1 H_j w - c_0)^(1/2)", "By Proposition 5.1(4) and the observation that rho_sf^-2 j
vanishes cubically at o ..., the square root in the definition of b_0 is indeed well-defined", and b_sf's and e's square
roots from "Proposition 5.1(6)"; p. 54, Proposition 5.11 and its commutant "a = (w')^-1 chi_sf chi_R chi_0, w' =
rho_sf^(alpha_sf + 1)"; p. 58, Lemma 5.14, "Let (T*, <., .>_G) be a time-oriented Lorentzian vector space". [Hin26d]
(arXiv:2408.06651; alphaXiv, 2026-10-24), the general construction [Hin26a]'s section 2.3.1 cites (his p. 19), which
10.56 left OPEN: p. 5, Definition 1.3, "Let M be a smooth n-dimensional manifold. Then a scaled bounded geometry
structure ... on M is"; p. 9, Definition 1.9, the parameterized version, "Let M be a smooth n-dimensional manifold, and
let P be a set"; p. 14, example (10), "3b-algebra, defined in [Hin23c] ... the vector fields are r d_t, r d_r, d_omega_m
(vector fields on S^(n-2))", with unit cells (2^(j-2), 2^(j+2))_t x (2^(k-2), 2^(k+2))_r x (l + (-4, 4)^(n-2))_omega
(1.15); p. 27, section 3, "We now develop the theory of (parameterized) scaled b.g. structures (Definitions 1.3 and
1.9)" (D138). With 10.22's READ (pp. 19, 38, 41-60, 64-66) and 10.56's.

*Deduced.*

 (a) (The calculus) [Hin26a]'s semiclassical 3b-calculus, his section 2.3 from [Hin23d] and the bounded-geometry
     calculus (his section 2.3.1, 10.22's READ p. 19), is constructed on R_t x R^(n-1)_x for every n, [Hin23d]'s n the
     spacetime dimension (pp. 3, 7, 10-12, 109), and its bounded-geometry construction is [Hin26d]'s, for a smooth
     manifold of any dimension n, with the 3b-algebra among its examples in every dimension ([Hin26d] pp. 4, 8, 14, 26;
     10.56's OPEN item, read here): at n = 5 it is the calculus of five-dimensional Tangherlini's compactification, with
     fibres S^3.
 (b) (The commutators: Propositions 5.8, 5.9, 5.11, 5.12) Each proof takes the semiclassical principal symbol of
     (i/2h)[-L_h + J, A^2] + h^-1 (Im L_h) A^2, or its adjoint form, as a H_(-l+j) a + S a^2 (pp. 51, 53-54) and splits
     it, a being a power of the weight w times cut-offs, into c_0 a^2 + b_0^2 + b^2 - e^2 + f. These are identities of
     symbols: the commutator's principal symbol is the Hamilton derivative, and on a = w^(-1) chi it is w^(-2) chi^2
     (-H_(-l+j) log w) + w^(-2) chi H_(-l+j) chi, with -H_(-l) log w = -l(dw/w). The dimension enters only through l, j,
     S and w, and through the density |dg| in the adjoint that defines S = h^-1 Im L_h. At n = 4 these are 10.13's, with
     the density r^3 |dr dg-slash| (10.56 READ (3)), and the quantity under each square root is one of his Proposition
     5.1 (3)-(6), computed in five dimensions (10.14, 10.22(c), (iv)): (3) for b_0 near r = r_0 (Proposition 5.8), (4)
     for b_0 at dK+ (Proposition 5.9), (5) for b_0 at the sink (Proposition 5.11), (6) for b_K, b_sf and e and for the
     real principal type propagation between the critical sets (Propositions 5.8, 5.9, 5.12). The cubic vanishing of
     rho_sf^-2 j at the zero section, which lets b_0's square root exist, comes from J's form (5.32), J = h^2 J_0 + h^3
     J_1 with h^-2 Im box_h and L_h* rho_sf^-2 box_h, and does not see the dimension.
 (c) (Propositions 5.5-5.6, 5.16, 5.17) The elliptic and fibre-infinity estimates use Lemmas 3.5 and 3.7, which hold at
     n = 4 (10.13(i)); the energy estimates use Lemma 5.14, stated for a Lorentzian vector space, and Corollary 5.15,
     stated for n-dimensional manifolds of bounded geometry (p. 60; there n is spatial, R^(1+n) the spacetime, where
     [Hin23d]'s n is the spacetime dimension), with 10.22(d)'s hypotheses computed; Proposition 5.17's combination and
     the duality argument for existence (pp. 64-66) do not see the dimension.


So B4's reading is discharged at source: [Hin26a] Theorem 5.2 holds in five dimensions, for h below its h_0, with every
sign its proof uses computed there, on a calculus constructed in every dimension; 10.21's Theorem 6.2 and 10.23's
Theorem B.1 follow with it (10.56(b)-(c)). What remains is the census's own claim, that his section 5.2 uses the
dimension only where (a)-(c) name it, read at source (10.56 READ (1)-(4)) -- as for [Hin23a]'s section 3 in 10.64.

Labels: READ; deduced ((a)-(c)); nothing computed here (the inputs are 10.13, 10.14 and 10.22's); nothing proved.

### 10.66 [CD03]'s gluing and [Hin26]'s boost at n = 4 by modification (`gluing5.py`; D137)

*The setting.* For part (ii) of Theorem 4, 10.63 left two readings besides the estimates: [CD03]'s proof of its Theorem
8.1 at n = 4, and Hintz's handling of the boost (his sections 3.4, 5.6 and 11-13). Their censuses in full text
(alphaXiv, 2026-10-24; [CD03] 126 rows, [Hin26]'s boost sections 123) find where the dimension enters. Each place is
computed here at n = 3 against the printed value and at n = 4, and the proofs are run with the computed quantity in
place.

*READ.* [CD03] (arXiv:gr-qc/0301073v2; alphaXiv, 2026-10-24; printed page = PDF page): p. 4, "whatever the
space-dimension n", "we shall assume that n >= 2"; p. 19, Lemma 3.18 and Theorem 3.19 ("open sets in R^n"); p. 22, (5.2)
"rH^s_k(g) := rH^k_(x, x^(-s-n/2))(g)"; p. 24, Theorem 5.6, "with s >= n - 2, s > 1 if n = 3, k > n/2", the map (5.7) on
rH^-s and (5.8) with "(delta J, delta rho) in rH^(s-n)_(k+1)(g) x rH^(s-n)_k(g)" and "(delta K, delta g) ... in
rH^(s-n+1)_(k+2)(g) x rH^(s-n+2)_(k+2)(g)", its proof, "The conditions s >= n - 1 and k > n/2 ensure"; p. 35, "we assume
that the initial data manifold is three-dimensional", Theorem 8.1, "for some alpha > 1/2 and 2 <= k in N", (8.1), "so
that all Poincare charges of (K, g) are finite and well defined"; p. 36, Remark 8.2, "The argument below carries over to
any dimension, the only element missing is an equivalent of Proposition F.1", and the proof: "e^(i), i = 1, ..., 10", "Q
in R^10", (8.2)-(8.3), "chi in C^oo(R^3)", "We choose the index t to be larger than or equal to k + 5 -- say t = k + 6
... this ensures the continuous embedding rH^(t-1)_(k+2) subset H^(k+2)", (8.4) with rH^(t-2); p. 37, "Theorem 5.6 with
s = t - 1 provides a solution delta x_(Q,R) in rH^(t-1)_(k+2) x rH^t_(k+2)" (8.5), (8.6) with "O(R^-2 beta)", "on
S(0, 1)
all the initial data considered coincide -- up to a rescaling -- with (g, K) ... by (E.20) ... = R^-1 {Q^0_(i) +
O(R^-delta)}", (8.7), "up to an additive constant, the maps lambda F_lambda converge ... to the map Q of Proposition
F.1", "V in R^10"; p. 58, (A.1); pp. 71-75, Appendix E for "n >= 2": (E.5b) "n/2 - 1 < alpha <= n - 2", (E.9),
Proposition E.1 and its proof, (E.16) ("Q^alpha_beta is a quadratic form in nabla g"), (E.17) "O(R_0^(n-2-2 alpha))",
(E.19) "For J^munu simple parity considerations lead instead to ... O(R_0^(n-1-alpha-alpha_-))", (E.20a)-(E.20b),
(E.26)-(E.27). [Hin26] (arXiv:2606.28253v2; alphaXiv, 2026-10-24): p. 63, Definition 2.27, "We denote the (2l +
1)-dimensional space of spherical harmonics of degree l by S_l := ker(Lap-slash - l(l + 1)) subset C^oo(S^2)"; p. 74,
(3.21), "g_m - gbar = (2m/r) dt*^2"; p. 77, section 3.4, "A Lorentz boost on Minkowski space in the direction v in R^3
is given by the time 1 flow of the vector field t v . d_x + (x . v) d_t. Since x . v = rS where S = (x/|x|) . v in S_1,
the 1-form dual to this vector field is given by omegabar(S) := t d(rS) - rS dt" (3.38), and (3.39); p. 78,
(3.40)-(3.41) and Lemma 3.18; p. 79, Lemma 3.19, "h_(S,11) := 2m [(cosh(c/2) + (S/c) sinh(c/2))^-3 - 1]" (3.43), "c^2 =
(3/(4 pi)) ||S||^2_(L^2(S^2))", and (3.44); p. 80, "phi_S^* g_m - g_m = ... = 2m rho [a(theta)^3 - 1] (dt*)^2"; pp.
108-109, Theorem 5.23, "For all S in S_1 with sufficiently small norm"; p. 246, Proposition 11.30(2), "S^(-1)_(h,b,S) is
invertible provided h, b, and S are sufficiently small in X^d ..., R^4, and S_1 ~= R^3"; p. 318, Theorem 13.1,
(13.2)-(13.3).

**Proposition 10.49 (computed; `gluing5.py` D1-D4).** For n = 3 and n = 4:

 (D1) The Killing fields of Minkowski R^(1,n) number (n + 1)(n + 2)/2: [CD03]'s ten at n = 3, fifteen at n = 4.
 (D2) Carried to Gamma(1, 4) by Phi_R -- g_R(y) = g(Ry), K_R(y) = R K(Ry) -- the linearized charges of the family at
     Schwarzschild and at Tangherlini scale by R^-(n - 2) for energy and momentum and by R^-(n - 1) for angular momentum
     and centre of mass.
 (D3) The embedding of the proof's rH^(t-1)_(k+2) in H^(k+2) needs t >= k + 3 - n/2, met by t = k + 6 at both n. (8.4)'s
     source rH^(t-2) and (8.5)'s solution rH^(t-1) x rH^t are Theorem 5.6's (5.8) exactly at s = t + n - 2: t + 1 at n =
     3, t + 2 at n = 4. Theorem 5.6's s >= n - 1 and k > n/2, and Theorem 5.4's exclusions s not in {(n - 1)/2, (n -
     3)/2}, hold for every k >= floor(n/2) + 1: 2 at n = 3 (the printed "2 <= k") and 3 at n = 4.
 (D4) With S = c x_n/r in S_1, the 1-form omega(S) = t d(rS) - rS dt raised by Minkowski's metric is c (x_n d_t + t
     d_(x_n)), so phi_S = exp(V(S)), with V = (1/2) gbar^-1(omega, .) where his cut-offs are 1, is the Lorentz boost of
     rapidity c/2. The Kerr-Schild metric gbar + mu r^(2-n) (dt*)^2, t* = t - r, is Ricci flat at n = 3 (his (3.21), mu
     = 2m) and at n = 4. Its mass term pulls back on t = r to mu r^(2-n) a^n (dt*)^2, exactly, with a = (cosh(c/2) + cos
     theta sinh(c/2))^-1: his h_(S,11) = 2m (a^3 - 1) at n = 3, and mu (a^4 - 1) at r^-2 at n = 4. His c^2 = (3/(4
     pi)) ||S||^2_(L^2(S^2)) is (n/|S^(n-1)|) ||S||^2_(L^2), 2/pi^2 at n = 4. S_1 has dimension n: four boosts at n = 4.

*Proof.* D1-D4 of `gluing5.py`, sympy, exact. D1 is the rank of the Killing operator on polynomial vector fields of
degree at most 2. D2 is general5.py's charge integrals of each linearized direction of 10.63's family, before and after
Phi_R. D3 is the arithmetic of (5.2)'s weights, x^(2i - 2s - n) bounded on the annulus. D4 is the boost on the cone t =
r, r'^2 = (r D)^2 with D = cosh(c/2) + cos theta sinh(c/2) checked first, plus the Ricci tensor of the Kerr-Schild
metric and general5.py's sphere integrals. The controls are the n = 3 values above, each [CD03]'s or Hintz's printed
one. The mutants -- the Killing operator unsymmetrized (D1), K_R without its factor R (D2), the printed s = t - 1 (D3)
and r for r' in the pull-back (D4) -- are each caught. []

*Deduced: [CD03] Theorem 8.1's proof at n = 4.* By the census, the dimension enters the proof at five steps written for
n = 3 only (the ten KIDs, the Kerr family, the cut-off on R^3, the homeomorphism, the ball in R^10), through (5.2)'s
weights, and through Appendix E's exponents. Every result the proof cites is stated for general n (sections 2-4,
5.1-5.10 and 7, Appendices A-E and G). The census also records that Theorem 5.6's statement asks s >= n - 2 where its
proof uses s >= n - 1. Step by step:

 (a) (Theorem 3.19, Lemma 3.18, (8.2), the constraint map, Proposition 5.10 and Corollary 5.11.) All are stated for
     every n. Proposition 5.10's k >= floor(n/2) + 1 is 3 at n = 4.
 (b) (KIDs, family, cut-off.) e^(i), i = 1, ..., 15 (D1); Q in R^15; 10.63(a)'s translated, rotated and boosted
     Myers-Perry metrics for the Kerr family; chi in C^oo(R^4).
 (c) ((8.3)-(8.5).) beta := min(alpha, n - 2), which is 2 for the glued data's alpha = 2: after the scale-down, (g -
     delta)(R x) and R K(R x) are O(R^-alpha) for the data, and the family's g_Q - delta, of order r^-(n-2) (the mass
     term mu r^(2-n)), and K_Q, of order r^-(n-1), give O(R^-(n-2)) (deduced; [CD03]'s printed min(alpha, 1) is this at
     n = 3; D147). t = k + 6 embeds (D3). Theorem 5.6 with s = t + 2 gives (8.5) as printed, for k >= 3 (D3), which
     smooth data meet. The printed s = t - 1 gives (8.4)'s source a fortiori, but a solution only in rH^(t-3) x rH^(t-2)
     at n = 3; s = t + n - 2 is the index (8.5) states. This is a reading of [CD03]'s index, recorded.
 (d) ((8.6)-(8.7).) Each pairing's main term is its charge difference times that charge's own power under Phi_R (D2):
     R^-2 for E and P at n = 4, R^-3 for J and E C. (8.7) prints R^-1 for every i at n = 3, where D2 gives R^-1 and
     R^-2; we read it as a misprint for J and E C. With R^-2 for them at n = 3 the printed (8.6) error O(R^-2 beta) =
     O(R^-2) is not below their main terms, so the three-dimensional proof needs for them the parity-improved error of
     (E.19), which (8.6) does not state; at n = 4 the printed error O(R^-4) lies below their R^-3 without it (gluing5.py
     D2; D143). Theorem 3.19 applies to F_R rescaled componentwise by these powers, an invertible diagonal map that does
     not move the zeros. The errors, in the units of the rescaled data on Gamma(1, 4), are O(R^-2 beta) = O(R^-4) for
     the KIDs constant at infinity. For the linear ones they are O(R^-(alpha + alpha_-)) under parity and O(R^-2 alpha)
     without it, the bound of (E.17) times the extra power of r that a linear KID carries. Both lie below the main terms
     when 2 alpha > n - 2 and either alpha + alpha_- > n - 1 or 2 alpha > n - 1. (E.5b) and (E.9) are printed for every
     n, and the glued data meet them with alpha = 2, alpha_- = 3 (10.63(b)). The convergence of the charges in (E.20),
     which the proof uses on S(0, 1) and S(0, 4), has the same exponents.
 (e) (The homeomorphism and the ball.) 10.63(a): the family's charge map is a local diffeomorphism near Tangherlini,
     hence a homeomorphism from a neighbourhood onto a set containing a ball V in R^15 about Q^0, and Theorem 3.19 gives
     the parameter in U = Q^-1(V).

So [CD03] Theorem 8.1 holds at n = 4 for smooth data near Tangherlini's with 1 < alpha <= 2: under (E.9), or without it
when alpha > 3/2 (D2). The second has no four-dimensional counterpart, because there (E.5b) caps alpha at 1 = (n - 1)/2.
This is 10.63(c)'s gluing. Since the static slice's data are exact Tangherlini far out, 10.63(b)'s parity condition on a
perturbation can therefore be replaced by its decay: |gamma~| + r |d gamma~| + r |k~| <= C r^-alpha for some alpha >
3/2, of either parity.

*Deduced: [Hin26]'s boost at n = 4.*

 (f) (Sections 3.4 and 5.6.) S_1 is the space of degree-1 harmonics on S^3, of dimension 4, matching the four boosts
     (D1, D4). phi_S is the Lorentz boost of rapidity c/2 cut off as in his (3.39), and Lemma 3.18's support properties
     are those of the cut-offs. Lemma 3.19 at n = 4 reads phi_S^* g_mu - g_mu = mu r^-2 (a^4 - 1)(dt*)^2 modulo faster
     terms (D4), at the order r^-2 = r^-(3/2) r^-(1/2). So the boost changes the data inside 10.49's class, where E_0
     may contain 2 + N (10.63(d)). In four dimensions it changes them at the radiation order r^-1, which needs his
     separate treatment of the (1,1)-component ([Hin23a] Definition 3.20, cited by him at p. 79). Theorem 5.23's "S in
     S_1 with sufficiently small norm" carries over with S_1 ~= R^4.
 (g) (Sections 11.4-13.) The boost enters as the finite-dimensional parameter space S_1 ~= R^4. Proposition 11.30(2)'s
     S^(-1)_(h,b,S) in L(S_1) is the identity plus o(1) on a four-dimensional space, invertible for small (h, b, S).
     Definitions 11.25, 11.37, 11.40 and 12.1 and Theorem 12.3 carry S_1, the centre-of-mass shifts S^(0)_1 and b = (mu,
     A) in the Myers-Perry parameters (10.36) as parameters. The linear growth t* h_(b,s1)(S-dot) at zero energy and the
     index sets at iota+ that the boost's terms carry are 10.43-10.46's and 10.61-10.62's five-dimensional ones. These
     are the places the census finds the dimension entering his boost bookkeeping. It read his sections 3.4, 5.6, 11.4,
     12.2-12.3 and 13.1-13.3 in full and the other boost passages in windows around each occurrence.

This replaces two of Theorem 4 (ii)'s readings by deductions by modification: every place the census finds the dimension
entering [CD03]'s Theorem 8.1 or [Hin26]'s boost is computed (Proposition 10.49), and each step above is theirs with the
computed quantity in place. What remains is the censuses' own claim, read at source, that their proofs use n only where
(a)-(g) name it -- as for [Hin23a]'s section 3 in 10.64 and [Hin26a]'s section 5.2 in 10.65.

Labels: computed (Proposition 10.49, D1-D4); deduced ((a)-(g)); READ; nothing proved.

### 10.67 [Hin26c] sections 7-8 and 9.3 at n = 4 by modification (`edge5.py`; D137)

*The setting.* 10.58(c) and 10.53(e) left one reading of [Hin26c]: that the propagation, radial point, trapping and
energy estimates of its sections 7-8 and the semiclassical estimates of section 9.3 (Theorem 9.16's proof) hold at n = 4
once their symbols are five-dimensional. The full-text censuses of sections 7-8 (122 rows) and 9 (119 rows; alphaXiv,
2026-10-24) find where the dimension enters. Each place is computed here at n = 3 against the printed value and at n
= 4.

*READ.* [Hin26c] (arXiv:2606.28008v1; alphaXiv, 2026-10-24; printed page = PDF page - 4): p. 101, Remark 5.6, "In the
present paper, we work in 3 + 1 dimensions for concreteness. The constant 1 in (5.1a) arises naturally when P_0 =
box_(g_m,a) ... See [Hin23c, section 3.1.2] for matching conventions in general dimension"; p. 142, (8.2), the edge
coordinates "t*, x_I = r^-(1/2), omega in S^2", (8.3), "P == (1/2) x_I^2 [-2 (x_I d_x_I - 2(1 + p_1)) d_t* + 2 x_I^2
Lap-slash + p_0]", Lemma 8.1 ("let alpha_I < -1/2 + p-bar_1", (8.5)) and footnotes 58-59 (the metric density, x_I^-6);
p. 143, (8.9), "X_0 := x_I^(-4 alpha_I - 2)(-x_I d_x_I + d_t*) = r^(2 alpha_I + 1)(2 r d_r + d_t*)", the K-current "(X)K
:= (X)pi . T = -(1/2)(L_X g^-1)_munu T(d_mu, d_nu), T(X, Y) := X (x)_s Y - (1/2) g(X, Y) g^-1", "the condition alpha_I <
-1/2 provides positivity on dt* (x) dt* by direct computation", the factor e^(-2 w t*) and "2 w T(X_0, -grad t*) gives
arbitrary amounts of positive definiteness also on the second symmetric tensor power of the span of dx_I/x_I, x_I^-1
T*S^2", and (8.10), "(X_0)K == x_I^(-4 alpha_I) [-(2 alpha_I + 1) d_t*^2 - 2 d_t* (x)_s x_I d_x_I - 2(alpha_I + 1) x_I^2
gslash^-1], T(X_0, -grad t*) == (1/2) x_I^(-4 alpha_I)((x_I d_x_I)^2 + x_I^2 gslash^-1)"; p. 144, (8.11)-(8.14); p. 175,
"We work with a general stationary wave operator P_0 on M = R_t x X as in Definition 9.3"; p. 179, (9.73), "P_(h,z) = 2i
z rho h (rho d_rho - (n - 1)/2 - S) + ..."; p. 182, section 9.3.4, "Let P_0 be a general stationary wave operator on M =
R_t x X (Definition 9.3)"; p. 191, section 9.3.5, "We prove a general result here for a general stationary wave operator
P_0". The census rows: section 7's radial-set symbols (7.13)-(7.23) and the fields (7.29a)-(7.30), "V_3, V_4, V_5 in
V(S^2) spanning V(S^2) over C^oo(S^2)", Lemma 7.12's alpha in N_0^6 and the angular Laplacian "as a sum of terms X_a X_b
... a, b in {3, 4, 5}" (pp. 127-129); section 8.2's "0 <= mu <= nu <= 3", R^3 and X_1, ..., X_4 (pp. 148, 155); Lemma
8.8's H^3_b (pp. 151-152); section 9.3.3's T*S^2 (p. 179); Theorem 9.28's (2 pi)^(-n-1) (p. 188).

**Proposition 10.50 (computed; `edge5.py` E1-E4).** For n = 3 and n = 4:

 (E1) Minkowski's wave operator in the edge coordinates (t*, x_I = r^-(1/2), omega) is box = x_I^2 (x_I d_x_I - (n - 1))
     d_t* + x_I^4 ((1/4)(x_I d_x_I)^2 - ((n - 2)/2) x_I d_x_I + Lap_S). Its second-order part does not depend on n
     except through the sphere's metric. Its first-order term x_I d_x_I - (n - 1) is his x_I d_x_I - 2(1 + p_1), with
     p_1 = 0, at n = 3, and x_I d_x_I - 2(3/2) at n = 4: Remark 5.6's constant 1 is (n - 1)/2.
 (E2) The K-current of X_0 on Minkowski, in his frame, is r^(2 alpha_I)[-(2 alpha_I + 1) d_t*^2 - (n - 1) d_t* (x)_s x_I
     d_x_I - (2 alpha_I + n - 1) x_I^2 gslash^-1] modulo lower order: his (8.10) at n = 3; at n = 4 the d_t*^2
     coefficient is unchanged, the cross term is -3 and the angular coefficient is -(2 alpha_I + 3). T(X_0, -grad t*) is
     his (1/2) r^(2 alpha_I)((x_I d_x_I)^2 + x_I^2 gslash^-1) at both n. K + 2 w T is positive definite for alpha_I <
     -1/2 and w large, and the d_t*^2 entry is positive exactly when alpha_I < -1/2.
 (E3) The C(n, 2) rotation fields x_a d_b - x_b d_a span T S^(n-1) at every point (3 on S^2, his V_3, V_4, V_5; 6 on
     S^3), and the sum of their squares is the Laplacian of S^(n-1).
 (E4) r^(n-1) |dr| = 2 x_I^(-2n) |dx_I/x_I|: his x_I^-6, and x_I^-8 at n = 4. The least integer above (n + 1)/2 is 3 at
     both n (Lemma 8.8's H^3_b). Lemma 7.12's commuting operators number 2 + C(n, 2) + 1 (his 6; 9 at n = 4). Section
     8.2's second-order monomials in (t*, x) number (n + 1)(n + 2)/2 (10; 15), and its fields X_1, ..., X_(n+1) number 4
     and 5.

*Proof.* E1-E4 of `edge5.py`, sympy, exact. E1 applies both sides to e^(c t*) x_I^p Y_lambda. E2 is -(1/2)(L_X0 g^-1)
contracted with T on the Minkowski metric -dt*^2 - 2 dt* dr + r^2 g-hat, with the leading coefficients taken in the
frame d_t*, x_I d_x_I = -2 r d_r and x_I d_omega. E3 is the rank at a point of the sphere plus the identity sum
Omega_ab^2 f = r^2 Lap f on degree-0 functions. E4 is arithmetic. The controls are his (8.3), (8.10), V_3-V_5 and x_I^-6
at n = 3. The mutants -- 2 for n - 1 (E1), the trace term dropped (E2), n - 1 rotation fields (E3) and r^(n-2) (E4) --
are each caught. []

*Deduced: [Hin26c] sections 7-8 and 9.3 at n = 4.*

 (a) (Section 7.) Propositions 7.4-7.9 and 7.11 are positive commutator estimates: each takes the principal symbol of a
     commutator with a weighted commutant and splits it into squares, as 10.65(b) found for [Hin26a] section 5.2. The
     dimension enters through the characteristic set and radial sets at I+, functions of the principal symbol (E1:
     n-free but for the sphere). It enters through the dynamics at the horizon and the trapped set, which are
     five-dimensional Tangherlini's (10.17-10.18), and through the thresholds. Those are stated in p-bar_1 and S-bar,
     the imaginary part of the subprincipal symbol relative to the metric density, so they are dimension-free once p_1
     is measured from the symmetric Minkowski part x_I d_x_I - (n - 1) (E1; 10.58(a)). Lemma 7.12 commutes the fields
     V_1, V_2 and the rotation fields, 6 of them at n = 4 (E3), and Lemmas 7.15-7.21 commute d_r, t* d_t* and t d_t,
     free of n; every commutator identity they use ([V_1, V_2] = [V_i, V_a] = 0, Lap-slash as a sum of X_a X_b) holds on
     S^3 (E3); and the counts change as E4 states.
 (b) (Section 8.) Lemma 8.1's proof is the energy identity with X = e^(-2 w t*) X_0. Its one computation, (8.10), is E2:
     at n = 4 the d_t*^2 coefficient, which gives the threshold alpha_I < -1/2 + p-bar_1, is his. The cross and angular
     coefficients change, but his proof bounds them by the 2 w T(X_0, -grad t*) term, which is his at both n and gives
     arbitrary positivity on dx_I/x_I and x_I^-1 T*S^3. Propositions 8.6 and 8.9 commute the same fields (a), Lemma 8.7
     extends in omega in S^3, and Proposition 8.3 extends P across the inner sphere in fifteen second-order monomials
     (E4). Section 8.2, near that sphere, commutes X_1, ..., X_5 on R^4 (E4). Lemma 8.8's Sobolev index 3 is unchanged
     (E4). Theorem 8.14 follows at n = 4.
 (c) (Section 9.3, Theorem 9.16's proof.) Sections 9.3.1, 9.3.4 and 9.3.5 are stated for a general stationary wave
     operator on R_t x X. The one numeral is (9.73)'s (n - 1)/2, which is 3/2 at n = 4 (E1, as in 10.53(a)). The
     cotangent sphere of section 9.3.3 is X's, T*S^3. Theorem 9.28's normalization is (2 pi)^(-n-1). The dynamics are
     10.17-10.18's.

So [Hin26c]'s sections 7-8 and Theorem 9.16 hold at n = 4 by modification. Every place the censuses find the dimension
is computed (Proposition 10.50) or is a general-n statement read at source (10.53, (c)), and each step above is his with
the computed quantity in place. 10.58(c)'s and 10.53(e)'s readings are discharged. As in 10.64-10.66, what remains is
the censuses' own claim, read at source, that his proofs use n only where (a)-(c) and 10.53 name it. Estimates he quotes
from [HV26], [Hin23c], [Hin24a] and [Hin21] enter through their statements, which are applied at n = 4 with these
inputs. ([Hin23c] section 3.1.2 sets its conventions in general dimension, by his Remark 5.6.)

Labels: computed (Proposition 10.50, E1-E4); deduced ((a)-(c)); READ; nothing proved.

### 10.68 [HHV21]'s perturbation arguments at n = 4 (D137)

*The setting.* The record uses two of [HHV21]'s arguments, both in 10.60: the openness in (b, sigma) of invertibility
(10.60(c), "[HHV21] p. 90's argument"), and Lemma 11.1's setting for the upper semicontinuity of dim ker L^_b(0)
(10.60(d)). The full-text census of [HHV21] (205 rows; alphaXiv, 2026-10-24) finds the dimension in its counts, its
weights and its 3 + 1 formulas.

*READ.* [HHV21] (arXiv:1906.00860v2; alphaXiv, 2026-10-24): p. 92, Lemma 11.1, "There exist V in Psi^-oo ... with
compactly supported Schwartz kernel, and a constant C_1 > 0 such that L-check_b(sigma) := L^_b(sigma) + V ... is
invertible for sigma in C, Im sigma >= 0, |sigma| < C_1, and |b - b_0| <= C_1", and its proof, "It suffices to prove the
invertibility for b = b_0, sigma = 0, since arguments as in the proof of Lemma 10.9 then imply the invertibility and
continuous dependence for (b, sigma) close to (b_0, 0) ... The main input for the perturbation theory is the fact that K
and R-perp have the same (finite) dimension, namely 7 ... select h#_1, ..., h#_7 ... such that (<h#_i, h*_j>) = delta_ij
... We then set V = sum_k h#_k <-, h-flat_k>"; the census rows: Lemma 3.4's ranks 1, 4, 10 (p. 28), Proposition 9.1(2)'s
"7-dimensional kernel and cokernel" (p. 70), "a in R^3", "dim K_(b0,s) = 4, dim K_(b0,v) = 3" (p. 93), the weights s >
5/2, l in (-3/2, -1/2) (pp. 89-91).

*Deduced.*

 (a) (Lemma 11.1 at n = 4.) Its proof uses of the dimension only N = dim K = dim R-perp, finite: V is built from N pairs
     with <h#_i, h*_j> = delta_ij and <h_i, h-flat_j> = delta_ij, and (11.2) is the N x N identity. At n = 4, N = 11,
     the eleven states of 10.60(d) and their duals (10.32-10.33). So L^_b(0) + V is invertible near b_0. Since ker
     L^_b(0) = {u : (L^_b(0) + V) u = V u} has dimension at most rank V = 11, and the eleven states exist at every b
     near b_0, the dimension is 11 there: 10.60(d)'s semicontinuity.
 (b) (The openness, p. 90 and Lemma 10.9.) Invertibility of a family of bounded operators continuous in (b, sigma),
     between the fixed spaces of [Hin26]'s five-dimensional weights (10.24, 10.52), is open. This does not see the
     dimension.
 (c) (The census.) The counts (ranks 1, 4, 10 of the scalar, 1-form and symmetric 2-tensor bundles, which are 1, 5, 15
     at n = 4; the 7 = 1 + 3 + 3 of Proposition 9.1(2) and Lemma 11.1, which is 11 = 1 + 6 + 4 at n = 4; a in R^3; dim
     S_1 = 3) and the weights (s > 5/2, l in (-3/2, -1/2)) are [HHV21]'s four-dimensional instances. The record does not
     use them: its counts and weights are the five-dimensional ones computed in 10.24 and 10.28-10.33.

So the two [HHV21] arguments the record uses hold at n = 4, with N = 11. Labels: deduced ((a)-(c)); READ; nothing
computed or proved here (N is 10.32-10.33's).

### 10.69 A second census, by token sweep (`censusweep.py`; D139)

*The setting.* 10.64-10.68 rest on censuses taken by reading the full texts, and on the claim that they found every
place the dimension enters. This sweep tests that claim by another route. It lists every marker of the dimension on
every page of each carried passage, and each hit is read against the sections.

**Proposition 10.51 (computed; `censusweep.py`).** On the alphaXiv full texts (fetched 2026-10-24) the patterns S^2,
S^3, R^3, R^4, R^10, 3 + 1, "dimension", "k-dimensional", n - 1, n - 2, n/2, n + 1, a 7 x 7 count and the densities
|x|^3, r^2 |d..|, x^-6 give 278 hits on the 205 pages swept, 81 of them with a hit. By paper: [Hin23a] section 3 (pp.
9-33), 104 hits; [Hin26a] section 5.2 (pp. 38-66), 25; [Hin26c] sections 7-8 and 9.3 (pp. 114-157, 174-193), 26;
[Hin26]'s boost sections (pp. 77-81, 108-110, 238-262, 267-278, 301-326), 65; [HHV21] pp. 89-93, 10; [CD03] Theorem 8.1,
section 8.2 and Appendices E-F (pp. 35-38, 71-77), 48. (D143: the page-marked copy's markers close their pages; D139
read them as opening them, which put its CD03 window, then pp. 35-37 and 71-77, one page late and gave 40, and 270 in
all. The window now also takes in p. 38, section 8.2's reference family, which 10.63(a) uses.)

*Read against the sections.*

 (a) [Hin23a]: section 3.1's manifold "n-dimensional" with fibres R^(n-2), Lemma 3.33's d_(n-1) (X6), R^4 as Minkowski's
     compactification, and 73 sphere hits on the round S^2 (X1-X5): 10.64.
 (b) [Hin26c]: the rotation fields (E3), the densities r^2, x_I^-6 (E2, E4), section 8.2's R^3 (E4), (9.73)'s (n - 1)/2
     and Theorem 9.28's (2 pi)^(-n-1) (10.67(c)), Notation 9.2's R^3 (10.53), one codimension and one symbol class
     S^2_cl: 10.67 and 10.53.
 (c) [Hin26]: the boost direction in R^3 (D4), c^2 = (3/(4 pi)) ||S||^2 (D4), the final parameters b = (m, a) in R^4 at
     n = 3 and (mu, A) in R^7 at n = 4, with S_1 ~= R^3 at n = 3 and R^4 at n = 4, in sections 11.4-12 (10.66(g)), the
     harmonic parameter spaces S_2, S_3, V_2, V_3 (10.61-10.62), iota+'s S^2, the splitting (3.37) (exterior5.py X4),
     and "finite-dimensional" parameters: 10.66, 10.61-10.62.
 (d) [HHV21]: Lemma 11.1's 7 (10.68(a)), Proposition 11.3's 4 and 3 and b in R^4, which the record does not use
     (10.68(c)), and the bundle S^2 T*X: 10.68.
 (e) [CD03]: Theorem 8.1's three-dimensional data manifold and (8.1), the "3 + 1 equivalent" of (E.9), on p. 35 (10.66's
     setting; 10.63(b)); Remark 8.2's "(n + 1) dimensions" (10.66); the proof's R^3, R^10 and ball (10.66(b), (e));
     section 8.2's reference family on R^3 with charges in R^4 x R^6, or R^4 when time-symmetric (10.63(a)); Appendix
     E's setting in n + 1 dimensions and its n-expressions (D2), its "n + 1 = 3 + 1" Schwarzschild and Kerr examples and
     (E.26)'s vacuum development in n + 1 form (10.63(b)); and Appendix F's R^3, R^(1,3) and R^4 x R^6 (10.63(a)): 10.63
     and 10.66 (D143).
 (f) [Hin26a]: Lemma 5.14 on R^(n+1) and Corollary 5.15 on an n-dimensional manifold (10.65(c)), the S^2 charts,
     (5.16)'s r^2 |dr dgslash| (the metric density, 10.56 READ (3)), Proposition 5.17's R^3 and T*R^4. One hit is in no
     section. p. 62, after (5.74): "we use the volume density r^3 |dr dgslash| on level sets of tau, which upon
     tensoring with |d tau| is a smooth positive multiple of the metric density |dg|". p. 65: "rho_sf^(alpha_sf + 1/2)
     H-bar^s_b(X, r^2 |dr dgslash|) = rho_sf^(alpha_sf) H-bar^s_b(X, r^3 dr |dgslash|)". At n = 4 the metric density is
     r^3 |dt dr dgslash_(S^3)|, so the density with that property is r^4 |dr dgslash_(S^3)|, and p. 65's identity reads
     with r^3 and r^4. This is a choice of norm fixed by the metric density, so (5.74)'s estimate is unchanged. Named
     here; it adds no input.

So the token sweep finds no place the dimension enters that 10.53-10.58 and 10.63-10.68 do not name, but one norm
convention, now named. Two censuses by different methods agree. That is evidence for completeness, not a proof of it: a
dimension can enter without any of these markers, through a numeral read in 3 + 1, which only reading finds. The
censuses that did that reading are 10.53-10.58's and those behind 10.64-10.68.

Labels: computed (Proposition 10.51, the sweep); READ ((f)'s quotes); deduced (the accounting (a)-(f)); nothing proved.

### 10.70 The deductions inventoried (`DEDUCTIONS.tsv`; D140)

*The setting.* What separates Theorem 4 from proved is, besides the censuses (10.69), that the deductions of 10.12-10.69
are not written at proof level. This section measures that gap. Every deduced item -- each lettered item under
a *Deduced* heading, and each sentence labelled deduced -- was extracted with its sources and sorted by one fixed rule
on its own words.

 (A) It applies a result printed for general n, or dimension-free, to computed inputs.
 (B) It carries a proof written in 3 + 1 dimensions to n = 4 by modification.
 (C) It is a perturbation, continuity, openness or semicontinuity argument.
 (D) It is arithmetic or bookkeeping on computed values.
 (?) The rule's words do not decide.

**Count (measured; `DEDUCTIONS.tsv`, 248 rows).** D 90, B 60, C 31, A 29, ? 38. By range: 10.12-10.29, 57 items (A 4, B
16, C 11, D 14, ? 12); 10.30-10.45, 77 (A 5, B 17, C 3, D 40, ? 12); 10.46-10.58, 60 (A 10, B 13, C 7, D 17, ? 13);
10.59-10.69, 54 (A 10, B 14, C 10, D 19, ? 1).

The B items, where a 3 + 1 proof is carried by modification, are: 10.15 (a), (b); 10.18 (b); 10.19 (a), (d); 10.20 (a);
10.21 (a), (c); 10.22 (e); 10.23 (b)-(d); 10.24 (b); 10.27 (b); 10.28 (a); 10.29 (a); 10.30 (a), (c); 10.31 (a), (b);
10.32 (b), (c); 10.34 (c); 10.36 (b); 10.37 (c); 10.39 (d), (e); 10.41 (b); 10.42 (e); 10.43 (c); 10.44 (c); 10.45 (b),
(e); 10.46 (a), (b), (e); 10.47 (d), (e); 10.48 (b), (c); 10.49 (a); 10.53 (e); 10.54 (a); 10.55 (b); 10.56 (b); 10.58
(c); 10.60 (f); 10.61 (b), (c); 10.62 (b)-(d); 10.63 (c); 10.64 (b), (e)-(g); 10.66 (f); 10.67 (a), (b).

*Read.* The 90 D items are proof-level once their computations are, since they are arithmetic on exact computed values.
The 29 A items are proof-level once each hypothesis of the cited general-n result is checked. Each names its hypotheses
and where they are computed. The 31 C items are standard functional-analytic or ODE arguments, about a page each written
out. The 60 B items are the core of what is not done: each says that a proof of Hintz's, or of a companion paper, runs
with the computed five-dimensional quantities in place. Writing each out line by line is the check 8.8 names. Some B
items written before 10.64-10.68 are since carried by modification at source and stay listed as written: 10.22 (e) by
10.65; 10.48 (c) by 10.64; 10.53 (e), 10.55 (b) and 10.58 (c) by 10.67. The 38 ? items are read one by one in 10.73: ten
summaries, two four-dimensional remarks, and the rest bookkeeping, applications, elementary, symmetry and harmonic
steps, and one modification step.

The sort is a first pass by a fixed rule, by extraction, not adjudicated item by item. The extractors flagged their
judgement calls: 10.56 (a), 10.59 (a), 10.61 (e), 10.65 (b), 10.67 (a) and the ? rows.

Labels: measured (the count); nothing computed, deduced or proved here.

### 10.71 The perturbation steps at proof level: five lemmas and the map (D141)

*The setting.* 10.70 counts 31 deduced steps of kind C: perturbation, continuity, openness or semicontinuity. Each has
the same shape. A property holds at one point -- Tangherlini, h at the record's point, sigma != 0 on a compact set --
and an abstract lemma carries it to a neighbourhood, given that the objects depend continuously on the parameter in a
stated topology. The lemmas are written out here with proofs. Each C item is then mapped to its lemma and its continuity
input, the input READ from the source that states it.

**Lemma 10.52 (proved).** Let X, Y be Banach spaces and p -> T_p a map from a topological space into the bounded
operators L(X, Y), continuous in operator norm.

 (P1) (Openness.) If T_p0 is invertible, T_p is invertible for p near p0 and p -> T_p^-1 is continuous in operator norm.
     *Proof.* T_p = T_p0 (I + T_p0^-1 (T_p - T_p0)), and ||T_p0^-1 (T_p - T_p0)|| < 1 near p0, so the Neumann series
     inverts the second factor; with ||T_p^-1|| <= ||T_p0^-1|| / (1 - ||T_p0^-1|| ||T_p - T_p0||), a bound uniform near
     p0; and A^-1 - B^-1 = A^-1 (B - A) B^-1 gives ||T_p^-1 - T_q^-1|| <= ||T_p^-1|| ||T_p - T_q|| ||T_q^-1||, so p ->
     T_p^-1 is continuous. []
 (P2) (Semicontinuity of the kernel.) If T_p0 is Fredholm of index 0 with dim ker T_p0 = N, there is V in L(X, Y) of
     rank N with T_p0 + V invertible. Then dim ker T_p <= N for p near p0, and if N independent elements of ker T_p are
     given at each such p, they span it. *Proof.* Let h_1, ..., h_N span ker T_p0 and f_1, ..., f_N span a complement of
     ran T_p0, of dimension N by index 0. Take l_j in X* with l_j(h_i) = delta_ij (Hahn-Banach), and V = sum f_j l_j.
     Then T_p0 + V is injective: (T_p0 + V)u = 0 forces T_p0 u = -sum l_j(u) f_j in ran T_p0 meet the complement, so
     l_j(u) = 0 and T_p0 u = 0; then u = sum c_i h_i with c_i = l_i(u) = 0. It is onto: for y = T_p0 x, u = x - sum_i
     l_i(x) h_i gives (T_p0 + V) u = T_p0 x + sum_j f_j (l_j(x) - l_j(x)) = y, as T_p0 h_i = 0 and l_j(h_i) = delta_ij;
     and f_j = (T_p0 + V) h_j; these span Y. By (P1), T_p + V is invertible near p0. On ker T_p, (T_p + V)u = Vu, so u =
     (T_p + V)^-1 V u and ker T_p embeds into ran V, of dimension N. []
 (P3) (Strict inequalities.) If F_p is a family of continuous real functions on a compact set K, with p -> F_p
     continuous into C^0(K), and F_p0 > 0 on K, then F_p > 0 on K for p near p0. *Proof.* min_K F_p0 = c > 0, and
     ||F_p - F_p0||_C0 < c near p0. []
 (P4) (Zeros of analytic families; Hurwitz.) If z -> f_p(z) is holomorphic on a disc D with p -> f_p continuous in the
     sup norm on D, and f_p0 has no zero on the boundary circle, then f_p and f_p0 have the same number of zeros in D,
     counted with multiplicity, for p near p0 (Rouche). A real-analytic function of one variable that is not identically
     zero vanishes at most on a discrete set.
 (P5) (Inverse function theorem.) A C^1 map from an open set of R^N to R^N with invertible derivative at x0 is a C^1
     diffeomorphism from a neighbourhood of x0 onto a neighbourhood of its value, which contains a closed ball about
     that value.

(P1)-(P3) are proved above. (P4) and (P5) are textbook theorems, cited.

*The map (deduced).* By DEDUCTIONS.tsv's rows:

 (i) (P1, openness of invertibility.) 10.20 (e), 10.34 (b) (a finite matrix), 10.60 (c), 10.60 (d) (with P2), 10.66 (g)
     (I + o(1) on R^4), 10.68 (b). The continuity input in each is the operator family's continuity in its parameter
     between fixed weighted spaces: [HHV21] Lemma 10.9 and p. 90 for (b, sigma), and [Hin26] p. 119 (Proposition 6.9's
     proof) and p. 124 for the families of [Hin26]. Both are READ (10.60).
 (ii) (P2, the kernel.) 10.33 (f) and 10.60 (d). N = 11 and the eleven independent states at every b near b0 are
     computed and deduced in 10.28-10.33 (10.68 (a)).
 (iii) (P3, strict inequalities.) 10.14 (a)-(b), 10.17 (a), 10.18 (a), 10.19 (b), 10.22 (c), 10.26 (a), 10.54 (e), 10.60
     (b). In each, the function is an explicit symbol, threshold or quantity computed in closed form, continuous in its
     parameter (eta, h, gamma, r, b). Compactness is of the set named: the critical set, the trapped set, the horizon's
     radial set. For the trapped set's normal hyperbolicity at b near b0 the input is [HPS77] persistence, cited by
     [Hin26] Remark 1.4.
 (iv) (P4.) 10.37 (e) (Hurwitz, along the candidate zero) and 10.54 (d) (a discrete exceptional set in h).
 (v) (P5.) 10.63 (a) and 10.66 (e): the charge map, polynomial in its parameters, with its Jacobian computed invertible
     (Proposition 10.47).
 (vi) (Not perturbative; the rule's word misled it.) 10.12 is exact: an indicial family depends only on the leading part
     at infinity. 10.20 (c) and 10.60 (a), (e) are uniformity statements read with (i)'s inputs. 10.21 (e) rests on
     [Hin26a] Theorem 5.2, a B step (10.65). 10.50 (c)-(e) are estimates from Theorems D and E and Hintz's
     final-parameter continuity. 10.54 (b)-(c) are computed (uniform5.py) and monotone. 10.63 (d) is now computed
     (gluing5.py D4).

So the twenty C steps of (i)-(v) are at proof level given their continuity inputs: (P1)-(P3) are proved here, (P4)-(P5)
are textbook theorems, and each input is a statement READ from the source that makes it; the eleven of (vi) are placed
as (vi) says, 10.21 (e) resting on a modification step and so on the censuses (D147). What (ii) of 8.8 leaves is the 60
B steps, the A steps' hypothesis checks and the 38 undecided rows.

Labels: proved (Lemma 10.52 (P1)-(P3)); cited ((P4), (P5), [HPS77]); deduced (the map); READ (the continuity inputs).

### 10.72 The general-n steps: every hypothesis placed (D142)

*The setting.* 10.70 counts 29 deduced steps of kind A. Each applies a result printed for general n, or dimension-free,
to computed inputs, so each is at proof level once every hypothesis of the cited result is placed. An extraction pass
listed each A step's hypotheses and where the record establishes each. Three hypotheses rested on readings, and those
are now READ at source here.

*READ.* [Hin26] (arXiv:2606.28253v2; alphaXiv, 2026-10-24): p. 110, Proposition 5.25 (gauged Cauchy data) and its proof,
p. 111: in a frame e_0 = nu, e_i tangent to Sigma_IVP, "The left-hand side of (5.80) for (X, Y) = (e_i, e_j) thus equals
-(1/2)(e_0 t_IVP)(h~_1)_ij, which thus uniquely determines (h~_1)_ij"; then (5.81)'s e^lambda component "For lambda = j
... uniquely determines (h~_1)_0j ... and for lambda = 0 one obtains -(1/2)(e_0 t_IVP)(h~_1)_00 = f_0 + (1/2)(e_0
t_IVP)(g_0)^ij (h~_1)_ij". p. 217, Lemma 10.13: "We use the product of |dt*| with any smooth weighted b-density on X to
define L^2(M_0)", and its proof for s = 0 "Dropping angular variables from the notation", a Hardy inequality in t at
fixed r. [Hin26c] (arXiv:2606.28008v1): pp. 264-265, Lemma 14.6 and its proof, the same Hardy inequality in t at fixed r
"We drop the angular variables from the notation", and general s by an elliptic A in Psi^s_3b with parametrix, the
calculus being [Hin23d]'s in every dimension (10.65).

*Placed (deduced).* Of the 29:

 (i) 23 have every hypothesis placed at a computed check, a READ statement printed for general n, or an earlier section:
     10.20 (b), 10.23 (e), 10.24 (c), 10.25 (b), 10.32 (d), 10.48 (d), 10.49 (d), 10.53 (a), (d), 10.56 (a), 10.57 (d),
     10.58 (a), (b), 10.59 (a), (d), 10.64 (a), (i), 10.65 (a)-(c), 10.66 (a), 10.67 (c), 10.68 (a).
 (ii) Four were partial and are placed now. 10.49 (b): Proposition 5.25's proof is a triangular linear system in a
     frame, (h~_1)_ij from (5.80), then (h~_1)_0j and (h~_1)_00 from (5.81), with coefficient -e_0 t_IVP for (h~_1)_0j
     (g_0^00 = -1 in the frame) and -(1/2) e_0 t_IVP for (h~_1)_ij and (h~_1)_00, none zero (D147). The same equations
     hold for i, j = 1, ..., n, so it holds at n = 4. 10.40 (c) and 10.41 (c): Lemmas 10.13 and 14.6 are Hardy
     inequalities in t at fixed (r, omega) -- Lemma 14.6 for the density |dt* dx|, Lemma 10.13 for any weighted
     b-density, the weight being arbitrary -- with general s through the 3b calculus, so they hold in any dimension.
     10.41 (d): its inputs, [Hin26c] Theorems 9.41, 9.16 and 9.5 (6) at n = 4, are 10.53's and 10.67's.
 (iii) 10.38 (a), that the h-dependent couplings at I+ fall by r^-(1/2) in five dimensions, is computed for [Hin23a]'s
     operator (exterior5.py X5, X7). For [Hin26]'s gauge it is now READ at source (D148): his E^Ups_g0 and E^C_g0
     ((4.1)-(4.2), (4.7), pp. 81-82) are built from the background g_0 and the fixed 1-forms c^Ups, c^C alone, and enter
     P(g, g_0) ((4.3), (4.8)) and its linearization (4.13) with g_0's coefficients, so the h-dependent terms of 2
     L_(g,g_0) -- box_g, 2 E^C_g0 delta_g G_g + 2 (delta*_g0 - delta*_g) delta_g G_g = 2 (delta*_(g_0,E^C) - delta*_g)
     delta_g G_g, 2 R_g and 2 delta*_(g_0,E^C)(C_(g,g_0) - Y_(g,g_0)) -- are [Hin23a]'s (3.30) term by term, E^C of the
     same order r^-1 (c^C = r^-1 (dt - v_C dr)); the orders X5 and X7 compute carry, and 10.38 (a) is placed.
 (iv) 10.51 (c) cites the record's own Theorem A and Proposition 6.5, not an outside general-n result. The rule misfiled
     it; it holds as stated there.

So every A step has its hypotheses placed, 10.38 (a)'s link READ at source (D148). With 10.71, the A and C steps
of (ii) are at proof level given their READ inputs. What (ii) leaves is the 60 B steps and the 38 undecided rows.

Labels: READ (the three proofs above); deduced (the placing); nothing computed or proved here.

### 10.73 The undecided rows: each read, and two lemmas (`synth5.py` S1-S3; D144)

*The setting.* 10.70's first pass left 38 of the 248 deduced rows undecided. Each is read here in full and placed. Two
kinds recur that 10.71-10.72 do not cover, steps by symmetry and sums over harmonics, and each is put at proof level by
a lemma proved here.

**Proposition 10.53 (computed; `synth5.py` S1-S3; exact).** On five-dimensional Tangherlini, with gmodes5.py's harmonics
([KI03], n = 3, K = 1): (i) (scalar type, (Delta + k^2) S = 0) the 1-form omega = A_t S dt + A_r S dr + r^2 B (-D_i S/k)
dz^i that removes f_a and H_T from h has B = -2 H_T/k and A_a = -(2 r/k)(f_a + (r/k) d_a H_T), every coefficient c(r)
k^-p with p >= 1, and h - delta* omega then has [KI03] (2.7)'s gauge-invariant F and F_ab; (ii) (vector type, D^i V_i =
0, (Delta + k_V^2) V = 0) delta*(r^2 B V_i dz^i) shifts f_a by (r/2) d_a B and H_T by -k_V B/2, so the gauge 1-form is B
= -2 H_T/k_V; (iii) on S^3, Re (x_1 + i x_2)^l restricted has Delta = -l(l + 2) for l = 1, ..., 6, and l(l - 1) + 3 l =
l(l + 2) for every l, so k^2 = l(l + 2) >= 8 for l >= 2. Controls: S^2, where -l(l + 1). Mutants: H_T's harmonic without
its 1/k^2, where B carries k; the S^2 count claimed for S^3.

**Lemma 10.54 (harmonic synthesis; proved).** Let E be the bundle of functions, 1-forms or symmetric 2-tensors over S^3,
Lambda a nonnegative self-adjoint elliptic second-order operator on its sections commuting with the rotations (the type
Laplacians whose eigenspaces the scalar, vector and tensor harmonics of each degree span), and P_j the orthogonal
projections onto its eigenspaces, eigenvalues kappa_j^2 -> oo. Let u(r), r in an interval J, be sections with ||d_r^i
u(r)||_(C^m(S^3)) <= C_m w_i(r) for i = 0, 1 and every m.

 (i) ||d_r^i P_j u(r)||_(C^m) <= C_(m,N) (1 + kappa_j^2)^-N w_i(r) for every m and N, uniformly in r in J.

 (ii) Let xi_j(r) = A_j(r)(P_j u(r), d_r P_j u(r)), A_j(r) linear into an eigenspace of a type Laplacian Lambda'
     (possibly of another bundle) with eigenvalue kappa'_j^2 <= C (1 + kappa_j^2), and ||A_j(r)(v_0, v_1)||_(L^2) <= C
     (1 + kappa_j^2)^M w(r) sum_i ||v_i||_(L^2)/w_i(r). Then sum_j xi_j(r) converges in every C^m(S^3), uniformly in r
     in J, to xi(r) with ||xi(r)||_(C^m) <= C_m w(r). If moreover the hypothesis on u holds for i = 2 with a weight w_2,
     and the A_j are C^1 in r with ||(d_r A_j(r))(v_0, v_1)|| <= C (1 + kappa_j^2)^M w'(r) sum_(i<=1) ||v_i||/w_i(r) and
     ||A_j(r)(v_1, v_2)|| <= C (1 + kappa_j^2)^M w'(r) (||v_1||/w_1(r) + ||v_2||/w_2(r)), then sum_j d_r xi_j converges
     likewise to d_r xi with ||d_r xi(r)||_(C^m) <= C_m w'(r), and a differential operator in (r, omega) of order one
     passes to the sum (D147).
*Proof.* (i) P_j commutes with d_r and with Lambda, so P_j v = (1 + kappa_j^2)^-N P_j (1 + Lambda)^N v and ||P_j
v||_(L^2) <= (1 + kappa_j^2)^-N ||(1 + Lambda)^N v||_(L^2) <= C_N (1 + kappa_j^2)^-N ||v||_(C^(2N)). On the eigenspace
the elliptic estimate gives ||P_j v||_(H^(2q)) <= C_q (1 + kappa_j^2)^q ||P_j v||_(L^2), and H^(2q)(S^3) is in C^m for
2q > m + 3/2 (Sobolev). Take v = d_r^i u(r). (ii) The same two steps for Lambda' give ||xi_j(r)||_(C^m) <= C (1 +
kappa_j^2)^(q + M - N) w(r) by (i) in L^2. The number of eigenvalues of Lambda below K, counted with multiplicity, is
O(K^(3/2)) (Weyl's law on S^3), so sum_j (1 + kappa_j^2)^-s converges for s > 3/2, and N > q + M + 3/2 gives the sum.
For the last sentence, d_r xi_j = (d_r A_j)(P_j u, d_r P_j u) + A_j(d_r P_j u, d_r^2 P_j u), each term bounded as before
by (i) with i <= 2 and the two bounds on A_j, and uniform convergence of the sum of derivatives gives the derivative of
the sum. []

**Lemma 10.55 (equivariance; proved).** Let G be a compact group acting on Banach spaces X and Y by linear isometries,
strongly continuously (g -> g x continuous for each x).

 (E1) If F: U -> Y, U in X a G-invariant set, is equivariant (F(g x) = g F(x)) and F(x) = y has at most one solution in
     U, then for G-invariant y that solution is G-invariant. *Proof.* F(g x) = g y = y and g x is in U, so g x = x. []

 (E2) Pi x = int_G g x dg (Haar probability measure, Bochner integral) is a projection of X onto the fixed space X^G
     with ||Pi|| <= 1, and Pi T = T Pi for every bounded equivariant linear T: X -> Y. So T x = y with y in Y^G gives
     T(Pi x) = y; and an invertible equivariant T has an equivariant inverse, and restricts to an isomorphism X^G ->
     Y^G. *Proof.* h Pi x = int h g x dg = Pi x by invariance of Haar measure; Pi x = x on X^G; ||Pi x|| <= int ||g x||
     dg = ||x||; T passes through the Bochner integral and T g = g T. T^-1(g y) = T^-1 g T T^-1 y = T^-1 T g T^-1 y = g
     T^-1 y. []

 (E3) A composite of equivariant maps is equivariant; so is a map built by solving, step by step, equations that are
     uniquely solvable and equivariant in their data (E1). []

 (E4) If S_theta are smoothing operators on a scale X_s on each of which G acts isometrically, Pi S_theta Pi maps
     X^G_s into X^G_t and satisfies their estimates with the same constants. *Proof.* ||Pi S_theta Pi x||_t <=
     ||S_theta Pi x||_t <= C theta^(t - s) ||x||_s, and for x in X^G, ||(I - Pi S_theta Pi) x||_s = ||Pi (I - S_theta)
     x||_s <= ||(I - S_theta) x||_s. []

The rotations act isometrically and strongly continuously on the record's weighted b-Sobolev spaces, normed by
rotation-invariant data (rho d_rho and the round Laplacian of S^3 near infinity, the static frame elsewhere), equivalent
to any other choice. *Proof.* The rotations commute with these data, so act isometrically. For u smooth and compactly
supported, g -> g u is continuous into every such space, its derivatives being uniformly continuous; such u are dense,
and ||g u - h u|| <= 2 ||u - u_k|| + ||g u_k - h u_k|| for isometries, so continuity extends. [] So the lemma applies
with G the record's symmetry group (D147).

*Placed (deduced).* By DEDUCTIONS.tsv's rows, now with a column `final`:

 (i) No step of their own (12). Summaries or assemblies of other rows (10): 10.36 (d), 10.41 (e), 10.49 (the statement
     and the Phase A paragraph), the closing paragraphs of 10.54-10.58, 10.61 (e). Four-dimensional controls or remarks,
     outside the five-dimensional chain (2): 10.36 (e), 10.38 (f).

 (ii) Bookkeeping on computed values (10). 10.14 (c): t = t_s + int (mu r^-2/f) dr, so dt = dt_s + mu r^-2 f^-1 dr.
     10.17 (b): on Gamma_0 the flow is the t-translation with the geodesic flow of the round S^3, isometric, so its
     tangential expansion rate is 0, below the computed normal rate nu, which is r-normal hyperbolicity for every r by
     its definition. 10.19 (c): the bicharacteristics' fates by C against 4 mu are the computed (iv). 10.21: the
     reflection identity is K2's exact check. 10.26 (b): c is spherically symmetric, so the case is void. 10.28 (i):
     coefficients in rho^2 C^oo and Christoffel symbols of order rho^3 give the stated orders by counting. 10.36 (a):
     computed in mp5.py, whose M2 computes, symbolically in A, the invariance and covariance under so(4) of the blocks
     the Kerr-Schild Myers-Perry metric is built from, and the full metric's identity at three spins; the family's
     equivariance g_(O A O^T)(O x) = O g_A(x) O^T at every spin follows from the blocks' (deduced), and the reading
     there is discharged (D147). 10.39 (f): the augmentation tensors are chi_K times the states, with no t*^-1 or log t*
     term. 10.41 (a): Definition 5.13 admits delta = 0 (READ), and alpha_sf + n/2 = alpha_sf + 2. 10.57 (c): Theorem
     3.35 is not invoked, the iteration's weight lying below the radiative order (10.48 (a), READ).
 (iii) Applications of dimension-free results (3), now with their hypotheses placed. 10.22 (b), (d): Lemmas 3.5 and 3.7,
     READ dimension-free at source (10.65 (c)), and Proposition 5.16's data in a compact set of C^oo by (i) there and c
     in rho_sf C^oo. 10.49 (c): [SR89]'s abstract theorem, its assumptions (1)-(4) placed at 10.47 (d), the construction
     of Phi (inverting model operators only), 10.47 (e) and 10.43 (e).

 (iv) Elementary steps written out where they stand (5). 10.15 (c): the pairing with omega* and (a), (b), (v). 10.16
     (c): with d omega = 0, Cartan's formula L_T omega = d(i_T omega) + i_T d omega gives d phi = -i sigma omega. 10.20
     (iii): the sigma^2 coefficient of e^(i sigma t*) P e^(-i sigma t*) is -G(dt*, dt*) for any second-order P with
     scalar principal symbol G (his Definition 9.4). 10.50 (a): induction on m from the record's Lemmas 5.3 (c) and 6.2.
     10.55 (c): a solution of a system with analytic coefficients and a regular singular point at r_h that vanishes to
     infinite order there is zero (Frobenius; Coddington and Levinson, chapter 4), then zero on (r_int, r_h) by
     uniqueness for the regular system.

 (v) Symmetry (5): 10.43 (a), (e), 10.45 (a), 10.47 (c), 10.48 (e), by Lemma 10.55. The inputs: every ingredient of P is
     O(4)-invariant (listed in 10.43 (a)); forward solutions are unique (his, and [Hin26c]'s); S_1 has no G-fixed
     element (Proposition 10.40 (ii), computed); Phi is built from unique solutions and invariant cut-offs (10.47 (c),
     so E3); the smoothing operators are averaged (E4); 10.45 (a) restricts the invertible augmented operator (E2);
     10.48 (e) is E1 with Theorem 5.17's uniqueness.

 (vi) Sums over harmonics (2): 10.27 (a), 10.33 (a), by Lemma 10.54 with Proposition 10.53. For l >= 2 the gauge 1-forms
     are (i)-(ii)'s, with coefficients r/k, r^2/k^2, 1/k and 1/k_V, bounded uniformly in l since k^2 >= 8 and k_V^2 is
     bounded below over l >= 2 (the eigenvalues are discrete and none is 0, a divergence-free 1-form with nabla V = 0
     being parallel, and S^3 having none); so M = 0. The finitely many l <= 1 terms need no bound. u (and h) are smooth
     across the horizon and conormal at infinity, where the rotations are b-vector fields, which gives the hypothesis
     with the weights of 10.27 and 10.33. The formula for A_a is covariant on the orbit space, so in ingoing coordinates
     it holds with f_a and H_T smooth across r = r_h, and each term, so the sum, is smooth there. delta* passes to the
     sums by Lemma 10.54 (ii)'s second part (D147): in 10.33 (a), h conormal with frame components O(r^-eps) has (r
     d_r)^i of its coefficients O(r^-eps), so w_i = r^(-eps-i) for i <= 2; A_r's coefficients 2r/k and 2r^2/k^2 multiply
     f_r and d_r H_T, so w = r^(1-eps) and, for the derivative, w' = r^(-eps), uniformly in l since k^2 >= 8; in 10.27
     (a) u is smooth and the r-interval compact.
 (vii) A modification step (1): 10.40 (a), his Lemmas 10.9-10.11 carried with the readings; it joins the B rows of
     10.74.

So of the 38, twelve have no step of their own, 25 are at proof level given their inputs (bookkeeping 10, applications
3, elementary 5, symmetry 5, harmonics 2), and one is a modification step. With 10.71-10.72, every deduced row of
10.12-10.69 that is not a modification step is at proof level given its computed and READ inputs, with one exception:
10.21 (e) rests on a modification step (10.71 (vi)) (D147); 10.38 (a)'s deduced link is READ at source (10.72 (iii);
D148).

Labels: computed (Proposition 10.53); proved (Lemmas 10.54 and 10.55); cited (Weyl's law, the elliptic estimate, Sobolev
embedding, Frobenius); deduced (the placing).

### 10.74 The modification steps: what each changes, and where it is computed (`B-MAP.tsv`; D145)

*The setting.* 10.70's 60 rows of kind B, with 10.73's 10.40 (a), each carry a proof written in 3 + 1 dimensions to n =
4 'with the five-dimensional quantities in place'. An extraction pass listed, for each, the quantities it says change
between n = 3 and n = 4, where it says each five-dimensional value comes from, its inputs, its residual wording
('carries over', 'as in his proof') and whether it rests on a reading; the values the rows only state were then placed
by hand. `B-MAP.tsv` holds the table, a column `placed` giving the result.

*Measured.* Of the 61 rows, 57 name the places where the dimension changes the proof, 215 places in all, and 4 name
none: the step is the source proof as it stands. The 222 placements of the five-dimensional values are: 93 at a computed
check, 95 at an earlier section where they are computed or deduced, 33 arithmetic in n (an entry naming an instrument or
a check counts as computed; B-MAP.tsv's column `kind`, D147) (n/2 = 2, (n - 1)/2 = 3/2, r^(n-1) dr = r^3 dr, rho^-n,
R^n, R^(n,1), S^(n-1)) and 1 the record's choice (gamma_Ups = 1/100). 39 rows say they rest on a reading -- of a source
theorem at n = 4, or of an earlier section that does -- and 10.64-10.68 have since carried the source papers'
dimension-dependent places by census and modification (D147). Before D149, 10.15 (a), whose source proof is a citation
replaced at n = 4, and 10.63 (c), whose seven places 10.66 places (four computed in gluing5.py), named none, 10.15 (a)'s
reading was unmarked, and 10.31 (b)'s placement naming zstates5.py Z4 was counted arithmetic (the sixty-first verifier).
D150-D151's write-outs (10.75 (xvii)-(xxx)) named eleven more places their rows lacked -- 10.60 (f) had none -- and one
more reading (10.20 (a)); n/2 = 2 is now an arithmetic placement at 10.20 (a) and 10.39 (e) (the sixty-second verifier);
the same shift, the b-density's, is placed at a section at 10.29 (a), 10.31 (a), 10.41 (b) and 10.56 (b), where an
earlier section computes it (the sixty-third verifier, which found the earlier wording's 'one occurrence' wrong). D154
cleared 10.48 (c)'s reading, [Hin23a]'s estimates at n = 4, which 10.75 (xxxi)-(xxxiv) now write out. D155's write-outs
(10.75 (xxxvii)-(xxxix)) named seventeen more places for 10.47 (d), 10.47 (e) and 10.62 (b) -- 10.47 (e) had none -- and
found [Hin26] section 9's iota+ solution theory, a reading at n = 4 (10.47's OPEN), among 10.47 (d)'s and 10.62 (b)'s
inputs. D156's (10.75 (xl)-(xliii)) named eight more places, for 10.21 (a) and 10.56 (b), and marked the readings 10.21
(c) and 10.56 (b) rest on, [Hin26a] Theorem 5.2 at n = 4 (10.56 (a)). D157 added three places the write-outs (xxiii) and
(xxv) named and their rows lacked (the sixty-third verifier), so D150's nine was a floor. D158's (10.75 (xliv)-(xlvi))
named six more places, for 10.23 (b)-(d), from tface5.py and cpmodes5.py. D159's (10.75 (xlvii)-(xlviii)) named three
more places, for 10.19 (a) and 10.55 (b). D160's (10.75 (xlix)-(lii)) named fourteen more places, for 10.43 (c), 10.45
(b), 10.45 (e) and 10.61 (b), 10.43 (c) having had none, and marked 10.45 (b) and 10.61 (b) as resting on readings:
[Hin26c] Proposition 13.18 and Corollary 13.17 and [Hin26] section 9's solution theory at n = 4. D161's (10.75
(liii)-(lv)) named twelve more places, for 10.46 (a), 10.46 (b) and 10.61 (c), and marked 10.46 (b) and 10.61 (c) as
resting on readings, as (xlix)-(l) found. D162 (the sixty-fourth verifier) narrowed 10.62 (b)'s order place to the mass
and the boost and named S^(0)_1's source order beside it, marked 10.15 (b) and 10.49 (a) as resting on readings, as
their items (iv) and (xxv) say, and counts a whole section's citation as citing its census rows. D163's (10.75
(lvi)-(lvii)) named eleven more places, for 10.67 (a)-(b), and corrected their two census-era places: his values for
'?', Lemma 7.12 for 'Lemmas 7.12-7.21', and the extension across r = m (p. 148) for 'near K+'. D164's (10.75
(lviii)-(lix)) named eight more places, for 10.19 (d) and 10.53 (e), the latter's first, and gave 10.19 (d)'s '?' his
A^(1 - eps); both keep a reading, the scalar-to-bundle step. D165 (the sixty-fifth verifier) marked 10.43 (c) as resting
on readings, as its item (li) now says, labelled three placements at an instrument computed, joined 10.32 (b)'s two
placements of one place, recorded 10.45 (e)'s weight as settled and gave 10.62 (b) its section 9 inputs. D166's (10.75
(lx)) named nineteen places for 10.58 (c), its first, seventeen at a computed check (iplusnorm5.py N1-N9, Proposition
10.57, and iplus5.py P1) and two arithmetic in n; the row keeps a reading, now (lvi)-(lix)'s and 10.20's. D167's (10.75
(lxi)) named nine more places for 10.22 (e), the last census row, and marked 10.22 (e), 10.21 (c) and 10.23 (c) as
resting on no reading: the one reading of each was [Hin26a] Theorem 5.2 at n = 4, now written out.

*The rule (deduced, not proved).* A row's proof is the source's with its listed places changed. It holds at n = 4 if (a)
the source proof uses n only at the listed places, and (b) each changed value meets every inequality or identity the
proof asks of it there. (b) is the table: every listed place has its five-dimensional value placed, and the inequalities
it must meet are the ones the row's section checks. (a) is the census question of 8.8 (i). For the rows that name no
place, (a) says the proof does not see n at all. So the B rows reduce to (i): to the censuses of the source proofs,
which two methods agree on (10.64-10.69) and which are read at source, not proved complete.

What 8.8 (ii) leaves is therefore not a separate kind of gap. Each deduced step of 10.12-10.69 is bookkeeping on
computed values, an application of a general-n result with its hypotheses placed, a perturbation step under Lemma 10.52,
an elementary step written out, a symmetry or harmonic step under Lemmas 10.54-10.55, or a modification step whose
changes are placed; and the last kind rests on the censuses. Writing the source proofs out line by line at n = 4 is what
would replace the censuses' evidence by proof.

Labels: measured (the table's counts); deduced (the placing, the rule); nothing proved here.

### 10.75 Sixty-one modification steps written out at n = 4 (D146-D167)

*The setting.* 10.74 reduces each modification step to the census of its source proof. Where that proof is short and
held in full text here, the census can be replaced by the proof itself: each of its steps, read at source, is matched to
its five-dimensional justification -- an identity true in every dimension, a computed check, or an earlier section. A
step so written out rests on its inputs, not on a census of its source. All but sixteen below are those whose source
proofs are at most about seven pages and are already matched step by step in the sections named, or short enough to
match here; each is READ at source (alphaXiv full texts, 2026-10-24; [CD03] the arXiv v2 text of 10.69; [Hin24b]
arXiv:2408.06715v1 for (xxvii)). The sixteen carry longer runs of proof, matched step by step the same way:
(xxxvii)-(xxxix) [Hin26] Theorems 12.3 and 12.8 (fifteen pages), (xlix)-(lv) his section 11 (pp. 231-295), (lvi)-(lvii)
[Hin26c] sections 7-8 (pp. 114-157), (lviii)-(lix) its sections 9.2-9.3 (pp. 161-193), (lx) its Definitions 5.13-5.18
with sections 10, 11 and 13.2 (pp. 106-109, 201-233, 247-255), and (lxi) [Hin26a] section 5.2 (pp. 41-66).

 (i) 10.27 (b), [Hin26] Proposition 8.8 (pp. 153-154). His proof, step by step at n = 4: (1) the spectral family is
     Fredholm of index 0 on [Hin26c] (9.18)'s spaces, by Proposition 8.3 (10.26) and [Hin26c] Theorem 9.5 (10.19, 10.53,
     10.67), so injectivity gives invertibility; (2) L-hat_b(sigma) u = 0 is L_b(e^(-i sigma t*) u) = 0, the definition
     of the spectral family; (3) with L_b = D Ric + delta*_(E^C) delta_(E^Ups) G ((8.1)), the contracted second Bianchi
     identity delta_g G_g Ric(g) = 0, true for every metric in every dimension, linearized at the Ricci-flat g_b gives
     delta G D Ric = 0, so delta G applied to L_b h = 0 gives (1/2) box^C eta = delta G delta*_(E^C) eta = 0 with eta :=
     delta_(E^Ups) G h, box^C := 2 delta G delta*_(E^C) (his p. 145), eta one order more decaying since delta in rho
     Diff^1_b; (4) eta = 0 by Theorem 7.1 (1) (10.21 (e)-10.23); (5) so D Ric(h) = 0, and [AHW24] Theorem 6.1 (1) on
     Tangherlini (10.27 (a), gmodes5.py, the sum over harmonics by Lemma 10.54) gives u = delta-hat*(sigma) omega on r >
     r_h; (6) eta = delta_(E^Ups) G delta* omega = (1/2) box^Ups omega, box^Ups := 2 delta_(E^Ups) G delta* (his p.
     144), so box^Ups(sigma) omega = 0 there; (7) harmonic by harmonic, omega is smooth up to r_h and continues inside
     the horizon as a solution by Lemma 10.56, so it is 0 by Proposition 6.12 (10.20 (e)) on all of X, and u = 0 on r >
     r_h and then on X (10.76 (b)-(c); D149). [AHW24] gives omega on X for Kerr, 10.27 (a) on r > r_h; the first writing
     of (7) took the continuation from 10.55 (c), which has only the interior uniqueness (the sixty-first verifier).
     Steps (2), (3) and (6) are identities in every dimension; the rest are earlier sections, (1), (4) and Proposition
     6.12 on the readings of 10.19-10.22.

 (ii) 10.24 (b), [Hin26] Lemma 8.5 (p. 151). His proof: 0 is an indicial root of the types s0 and s2 only; there the
     kernel is one-dimensional and spanned by the leading term of a gauged state, which satisfies the gauge condition,
     so its leading term satisfies (8.14). At n = 4, lin5.py E5 computes the first two facts exactly for l <= 12, 10.24
     (a) gives them for every l, and E5 computes the conclusion itself, N(r delta_(E^Ups) G, 0) vanishing on the kernel
     (10.24 (iv)), at the record's point; his argument through the gauged states h^(0)_(b,s0) (10.28-10.30) gives it for
     every z > 0.

 (iii) 10.15 (a), [Hin26] Lemma 6.10 (p. 120). His proof is a citation of [AHW24] Theorem 5.1 (2) on Kerr. At n = 4 it
     is replaced, not carried: on static Tangherlini each mode's equations are ODEs in r, and the kernel is found by an
     energy identity integrated over [r_h, oo) with the boundary terms computed (10.15 (i)-(ii), gaugepot5.py), the
     interior by 10.76 (b). It rests on a reading: the kernel elements' smoothness at the horizon and their expansion at
     infinity are [Hin26c]'s radial-point and b-regularity at n = 4, 10.19 (d)'s reading, which 10.15 (a) names (the
     sixty-first verifier; B-MAP.tsv's row now says so).

 (iv) 10.15 (b), [Hin26c] Corollary 9.43 (p. 200). His proof: augment the zero energy operator by maps E_01, E_10 onto a
     complement of its range and from its kernel; Theorem 9.41 gives the augmented operator invertible at sigma = i eps
     for small eps > 0; the index of (9.18) is 0; so the kernel and cokernel have equal dimension. At n = 4 the two
     inputs are Theorem 9.41 (10.39 (e), 10.53) and the index of (9.18) (10.19, 10.53), and the corollary's hypothesis,
     tf-admissibility (his Lemma 6.8 in four dimensions), is 10.15 (b)'s, on 10.20's reading; the rest is linear algebra
     in any dimension.

 (v) 10.29 (a), [Hin26] Lemma 6.13 (pp. 124-125). Its invertibility is Proposition 6.12's at zero energy (10.20 (e)),
     and his proof of its final part is Lemma 2.13, a statement on b-manifolds, here [0, rho_0) x S^3.

 (vi) 10.30 (c), the injectivity of N(delta-bar*(0), lam) at sl and vl for l >= 2 ([Hin26]'s remark after (2.46c), p.
     67, which justifies it in one line). The record's argument: delta-bar*(0) is homogeneous, so a kernel element gives
     a stationary Killing 1-form rho^lam omega of Minkowski space on R x (R^n \ 0); on that connected open set a Killing
     field is the restriction of one of R^(1,n)'s, a Killing field being fixed by its value and first derivative at a
     point and flat space realizing every such pair; and the Killing fields of R^(1,n) -- 15 at n = 4 (gluing5.py D1),
     the translations, rotations and boosts, a superset of the stationary ones -- have harmonic degree l <= 1 in every
     dimension.

 (vii) 10.39 (d), [Hin26] Proposition 10.6 (p. 208). His proof: index 0 (Proposition 8.11) reduces invertibility to
     injectivity; a kernel element (u, b-dot, S-dot) satisfies Lemma 10.4's identity; pairing with the dual states,
     integration by parts justified by their decay, Lemma 8.12's pairings give b-dot = 0 and S-dot = 0; then u lies in
     the kernel of L-hat_b(0), spanned by the gauged Kerr and s1 states, and the augmentation functionals f*_1, f*_2
     remove it. 10.39 (d) lists each step at n = 4: the index 0 of 10.32 (c), the eleven dual states of order r^-3
     (10.31 (b)) where his proof asks O(r^(-1-eta)), the pairings and their determinant (10.32, pairing5.py), the
     eleven-dimensional kernel (10.32 (c)), and f*_1 in C_c^oo x R^7, f*_2 in C_c^oo x S_1 with S_1 four-dimensional.

 (viii) 10.63 (c), [CD03] Theorem 8.1 (pp. 35-37). Its proof has twelve steps, each placed at n = 4 in 10.66: the KIDs
     e^(i), 15 (D1), and the charges Q^(i) of (E.26); the family of translated, rotated and boosted Myers-Perry metrics
     (10.63 (a)); the scale-down (8.2) and the cut-off on R^4; (8.3) with beta = min(alpha, n - 2) = 2; t = k + 6 (D3);
     (8.4) from (8.3), the constraint maps being smooth in the data and vanishing at flat data; Theorem 5.6 with s = t +
     n - 2, giving (8.5) (D3), where [CD03] prints s = t - 1 (p. 37; its index taken as s = t + n - 2, 10.66 (c)); the
     pairing with the KIDs and (E.27)'s boundary form, (8.6); the charges on S(0, 1) and S(0, 4) at D2's powers with
     (E.20)'s errors, (8.7) componentwise rescaled, where [CD03] prints R^-1 for every charge (read as a misprint, 10.66
     (d)); the charge map's local diffeomorphism (10.63 (a), Proposition 10.47); Theorem 3.19's conclusion with V a ball
     about the data's charges (10.66 (e)); and the smooth case by Proposition 5.10 and Corollary 5.11 (10.66 (a)).

 (ix) 10.31 (a), [Hin26] Lemma 7.2 (pp. 137-138). His proof has two parts: (1) duality with the target space of (7.7),
     the unweighted b-density shifting the weight by n/2; (2) (7.10), the adjoint's indicial family through the density
     rho^-3. 10.31 (a) writes both at n = 4: (1) by duality from 10.21 (e) with the shift n/2 = 2, so alpha in (0, C_0 +
     2]; (2) (7.10) with rho^-4, N(rho^-2 box, lam)* = N(rho^-2 box*, 2 - conj(lam)), computed (dual5.py), the roots
     placed by Proposition 10.9.

 (x) 10.31 (b), [Hin26] Proposition 7.3 (pp. 138-139). His proof has three parts -- the time translation, the
     translations, the rotations -- each a cut-off Killing 1-form corrected by Lemma 7.2, with the regularity in b by
     iterating Lemma 7.2 against a source in rho^3 Diff^2_b. 10.31 (b) writes each at n = 4: the time translation's
     state his; the four translations' sources in rho^4 C^oo (computed, (ii)), the correction one order faster, 2 being
     no root of the adjoint by (ix); the six rotations Killing on Tangherlini (zstates5.py Z4), so his (7.14) holds; and
     the iteration with Lemma 7.2 at n = 4 and the sources of order rho^4 (10.28 (i)).

 (xi) 10.18 (b), [Hin26] Lemma 6.1 (1) (pp. 113-114). Its statement -- the operator's structure at infinity -- is not
     carried from his proof but computed at n = 4: rho d_rho - 3/2 in place of rho d_rho - 1, S-bar's spectrum, and the
     differences (6.7) gaining a power (Proposition 10.15 (i), (ii), (iv), in section 10.18; thresh5.py). Q in rho^3
     Diff^1_b ((6.4b)) is deduced from Proposition 10.45 (D149): the model's sigma-linear part is the leading term, and
     the rest comes from g^-1(dt*, dr) + 1 = 2 mu/r^2 against d_r = -rho^2 d_rho and from the connection's and the
     damping 1-forms' differences from the model, of order r^-3, against d_t*.

 (xii) 10.28 (a), [Hin26] Proposition 6.15 (pp. 125-128; D148). His proof has four parts and a regularity paragraph: the
     time translation (Killing); the translations (f_b's order by Lemma 6.14, the correction by Lemma 6.13, 1 no s1
     root, the symmetric gradient's order); the boosts (four terms in f-breve_b, the first zero, Lemma 2.15 for the
     logarithm); the rotations; and the regularity in b by differentiating box^Ups(0) omega' = -f_b and inverting with
     Lemma 6.13 against an operator difference in rho^3 Diff^2_b. 10.28 (a) places each at n = 4 (the orders raised by
     one, 2 no s1 root at z > 0, Proposition 10.25 (iii)'s stationary residual of order rho^3 computed, no logarithm
     since 1 is no s1 root, Proposition 10.25 (iv)'s rotations); the regularity paragraph is the same iteration with
     Lemma 6.13 at n = 4 ((v)) and the difference in rho^4 Diff^2_b (10.28 (i)).

 (xiii) 10.30 (a), [Hin26] Proposition 6.18 (4)-(7) (pp. 132-134; D148). His proof of each part: an indicial solution of
     the class root, the correction against the operator difference in rho^3 Diff^2_b by Lemmas 2.15 and 6.13, the
     symmetric gradient's nonzero leading term (N(delta-bar*(0), lam - 1) injective), then the generalized states from
     A_0, A_1, A_2 of (6.44), and the smoothness in b as in Proposition 6.15. 10.30 (a) places each at n = 4: the
     difference in rho^4 Diff^2_b (Proposition 10.25 (i)), the correction one order faster, mu + 2 no root by
     Proposition 10.27 (iv), the leading term nonzero by Proposition 10.27 (iii) and (vi) above, A_0, A_1, A_2 with
     their five-dimensional orders (10.18 (b)) and the leading equations solvable without logarithm, mu - k no root by
     Proposition 10.27 (iv); the smoothness in b as in (xii).

 (xiv) 10.37 (c), the injectivity half of [Hin26] Proposition 9.2 (2) (pp. 165-167; D148). His steps: part (3)'s
     regularity (a general radial-set result of Haber-Vasy); the identification (9.5) in v; (9.6), the exponent 1 + min
     spec S-bar - Re lam; the extension by zero in L^1_loc; the Fourier transform ([Hin23d] Lemma 2.25) and the
     polynomial argument; the conjugation by r-hat^(-lam+1) to N_tf; and Proposition 8.6. 10.37 (c) places each at n =
     4: the threshold s < 2 + min spec S-bar - Re lam and the exponent shifted by 1/2 with v d_v - 3/2 - S-bar, the
     extension in L^1_loc for Re lam < 5/2 (min spec S-bar = 0, 10.25), the Fourier transform, the polynomial argument
     and the conjugation free of the dimension, and Proposition 8.6 at n = 4 (10.24 (c)-(d), 10.25 (b)). Its other half,
     the index 0 property, is not carried, as 10.37 (c) says.


 (xv) 10.32 (c), [Hin26] Proposition 8.11 (pp. 155-156; D148). His kernel argument: a normal operator argument puts u in
     A^(eps_ind - eps); the Bianchi step of (i) gives box^C eta = 0, so eta = 0 by Theorem 7.1 (2); [AHW24] Theorem 6.1
     (2) writes u = g-dot(b-dot) + delta* omega; Proposition 8.9 gauges g-dot; omega in ker box^Ups(0) with leading term
     a combination of dt and d(rS), the least root above -1 being 0 at s0 and s1 (Lemma 6.6); subtracting the Killing
     and s1 states leaves omega in A^eps, zero by Proposition 6.12; the pairings of Lemma 8.12 and d(rS) not Killing
     give the dimension. His cokernel argument: index 0 (Propositions 8.3, 8.6, [Hin26c] Corollary 9.43), the dual
     states of (7.13) and (7.15), and (8.25), whose pairings give the dimension, seven in four dimensions. 10.32 (c)
     places each at n = 4: [Hin26c] Theorem 9.5 (5) (10.53), Theorem 7.1 (2) (10.21 (e)), [AHW24] Theorem 6.1 (2) on
     Tangherlini (10.33, whose hypothesis A^(eps_ind - eps) meets), Proposition 8.9 (10.28 (b)), Lemma 6.6's roots
     (10.15, 10.24: none in (-1, 0), 0 at s0 and s1), Proposition 6.12 (10.20), the pairings (10.32 (b), pairing5.py),
     the eleven states and duals, and the index 0 ((iv) above).

 (xvi) 10.36 (b), [Hin26] Proposition 7.4 (pp. 140-144; D148). His proof: the ansatz V_b plus rho S-type terms plus chi
     rho omega_0; omega_0 from the v1 normal operator of the adjoint at 1, 2 + 4 gam_C v_C; the leading term
     h-bar-sharp; Lemma 7.5; the sources of (7.33) in rho^4 C^oo; a formal solution by Lemma 2.15 and the remainder by
     Lemma 7.2; the splitting (7.17) and the formal-solution property (7.19). 10.36 (b) places each at n = 4: the
     ansatz with c_0 r^-3 V(W), c_0 fixed by 3 + 6 gam_C v_C (dual5.py, 10.31 (i)); the leading term at rho^3 (10.31
     (iii)); Lemma 7.5 at every spin (10.36 (a)); the sources in rho^5 C^oo; no root of the adjoint with real part in
     [3, C_0 + 2] (10.31 (a)), so the formal solution is in rho^3 C^oo, Lemma 7.2 at n = 4 ((ix)); and (7.19) to order
     floor(C_0) + 3.

 (xvii) 10.39 (e), [Hin26] Proposition 10.7 (pp. 209-211) and Theorem 10.1, whose proof is his section 10.2 (pp.
     212-218; D150). Proposition 10.7's proof, step by step at n = 4: near zf, [Hin26c] (3.46)'s first equivalence --
     |sigma|^-q against the b-norm, a relation of defining functions with no density factor -- and Proposition 10.6
     ((vii)); the difference L~(sigma) - L~(0) of class (10.31), from (10.32) at n = 4, 2 i sigma rho(rho d_rho - 3/2 -
     S) + L-hat(0) - i sigma Q + g^00 sigma^2 (10.39 (a); Q in rho^3 Diff^1_b by (xi)), and Lemma 10.4 (3) for the
     augmentation columns (10.39 (c)); the conditions -N <= r_0 + alpha_0 + 1 and alpha_0 + 2 >= alpha_sf + 2 + eps_0
     with alpha_0 near -2 + eps_ind, his -3/2 replaced by -n/2, arithmetic on the record's alpha_sf + 2 in (0, eps_ind);
     the commutator with chi_zf in rho^oo_scf rho^2_tf rho^oo_zf Diff^1, from (10.32), and the augmentation rows removed
     by the compact support of f*_1, f*_2 (10.39 (d)); near tf, (3.46)'s second equivalence, whose |sigma|^(3/2) comes
     from the density relation, printed r^2 |dr dg/| = (|sigma|^(3/2))^2 r-hat^2 |dr-hat dg/| (p. 60), which with r-hat
     = r |sigma| is r^2 |dr dg/| = (|sigma|^(-3/2))^2 r-hat^2 |dr-hat dg/| (the sixty-third verifier), at n = 4 r^3 |dr
     dg/| = (|sigma|^-2)^2 r-hat^3 |dr-hat dg/|: the exponent's size n/2 moves from 3/2 to 2, so the norm factor,
     printed |sigma|^(3/2 - alpha_sf) and by the corrected relation |sigma|^(-3/2 - alpha_sf), is |sigma|^(2 -
     alpha_sf), or |sigma|^(-2 - alpha_sf), at n = 4, arithmetic; it stands on both sides of Proposition 10.7's chain
     and cancels, so its sign does not matter (the sixty-fourth verifier); tf-admissibility (Proposition 8.6; 10.24
     (c)-(d), 10.25) through [Hin26c] Corollary 9.39 (10.20's reading); |sigma|^2 N_tf against L-hat(sigma) with an
     error one order better at tf (10.55 (a)); the absorptions with |sigma|^delta, delta < -2 + eps_ind - alpha_sf;
     higher b-regularity by [Hin26c] Theorem 9.5 (4) (10.19's reading); and (10.29) by the resolvent identity, an
     identity, with sigma d_sigma L-hat(sigma) in sigma rho Diff^1_b + sigma rho^3 Diff^1_b + sigma^2 rho^2 C^oo by
     (10.32) and Lemma 10.4 (2). The threshold at the outgoing radial set in its statement is [Hin26c]'s at n = 4
     (10.41, a reading). Theorem 10.1's proof is 10.40 (a)-(c): Lemmas 10.9-10.11 ((xviii)), Lemma 10.12 with the
     five-dimensional orders (10.40 (b)), and Lemma 10.13 and the integration in t* (10.40 (c), Lemma 14.6's variable
     orders a reading).

 (xviii) 10.40 (a), [Hin26] Lemmas 10.9-10.11 (pp. 212-214; D150). Lemma 10.9's proof: the high-energy estimates of
     [Hin26c] Theorem 9.16 (5) (10.19, 10.53 (e); a reading), with the semiclassical loss function below any positive
     constant by strong trapping admissibility (Proposition 8.3; 10.26), give (10.45); [Hin26c] Lemma 3.9 passes between
     the 3b-norm and the Fourier side (a reading at n = 4, 10.41); and the count of powers of |sigma| with eps = 1/(k +
     1) is arithmetic free of n. Lemma 10.10's: the contour shifted to [-c, c] by the holomorphy of u-hat_reg,1 recorded
     after (10.47), from Proposition 10.7 ((xvii)); Lemma 2.20, Plancherel in t* with the sf-weight setting the tf and
     scf weights (no numeral), with [Hin26c] Lemma 3.9 for b-derivatives; and (10.29) ((xvii)). Lemma 10.11's:
     Proposition 10.7's bounds for b-hat_1 and S-hat_1, the same way. The Fourier representation the lemmas use is the
     Paley-Wiener argument of [Hin26c] Theorem 12.2's proof, with his Theorem 14.2, as his section 10.2 cites them:
     contour arguments free of n given Theorem 9.16's bounds (10.19, a reading). The threshold enters only through
     Remark 10.2's margin, min spec S-bar = 0 at n = 4 (10.25).

 (xix) 10.60 (f), [Hin26] Lemma 8.15 (pp. 158-160) at b near b_0, with Proposition 7.4 and Lemmas 2.15 and 7.2 (D150).
     His proof of (1): the expansion of 0 = L_b h^(<=2)_b,s1 in powers of t*, an identity in every dimension, gives
     L-hat_b(0) h-breve^2_b,s1 = -(1/2) [[L_b, t*], t*] h_b,s1 - [L_b, t*] h-breve^1_b,s1, and (8.26) (Lemma 8.12) the
     pairings. Of (2): (8.21) with a-dot = v x a (his Remark 8.10) and Lemma 8.12, the cyclicity of the triple product
     finishing; his direct computation is a second argument, not needed. 10.34 (b) writes both at n = 4: (1) as his, the
     centre-of-mass row 10.32's, the pairing against the rotations that stay Killing 0 and against the others not
     established, which 10.34 (b)'s modification of his Step 2 absorbs into V_1, solvable for small a by continuity
     (Lemma 10.52); (2) by Remark 8.10 at n = 4, g_(mu, A(s)) = (e^(-sR))* g_(mu, A) with A(s) = e^(s ad B) A, and 10.29
     (ii)'s rotation row, so(4)'s bracket in place of the cross product and the ad-invariance of the trace form in place
     of the triple product's cyclicity. His Proposition 7.4 and (7.19) on the full metric are (xvi), Lemma 7.2 is (ix),
     and Lemma 2.15 is a statement for an elliptic b-operator on any manifold with boundary (p. 52), free of n.

 (xx) 10.20 (a), [Hin26c] Theorem 9.36 (pp. 193-194; D150). His proof of (1): the radial point estimate at the event
     horizon (Proposition 9.9 at sigma = 0), real principal type propagation, an energy estimate near the inner boundary
     and elliptic regularity give the estimate with an error in H^(-N, alpha)_b; (3.47), which needs alpha + 3/2 in an
     indicial gap, bounds that error, and an interpolation inequality finishes. Of (2): the estimates in their strong
     form put kernel elements in H^(oo, alpha)_b, and a Mellin contour shift through the absence of indicial roots with
     real part in [alpha + 3/2, min(alpha + 5/2, beta)], one order per step, with the Sobolev embedding (3.72), H^(oo,
     beta - 3/2)_b in A^beta, gives A^beta. At n = 4 (10.20 (a)): the radial estimate with s_0 > 3/2 at the horizon
     (10.18), on 10.19's reading of Proposition 9.9; no ergoregion, and dr timelike inside the horizon for the energy
     estimate (10.19 (c)); (3.47) and the gap with alpha + 2 for alpha + 3/2 (10.20 (iii)); the contour shift over
     [alpha + 2, min(alpha + 3, beta)]; the embedding H^(oo, beta - 2)_b in A^beta, the density's n/2 = 2, arithmetic;
     propagation and interpolation free of n.

 (xxi) 10.41 (b), [Hin26c] Lemma 13.13 (pp. 252-253; D150). His proof: (13.24)-(13.26), a microlocal elliptic parametrix
     in the scattering calculus and the persistence of b-regularity, statements of the sc- and b-calculi on X with no
     numeral; then H^(k', beta)_b(X, mu_b) = H^(k', beta - 3/2)_b(X, mu), the passage from mu = |dx| to mu_b =
     |dx|/|x|^3 (p. 252), which gives (13.23a)'s 5/2 + eps (beta > r'_o + 3/2 with r' = r + alpha + 1) and (13.23b)'s
     3/2 - eps. At n = 4, mu_b = |dx|/|x|^4 and the shift is n/2 = 2 (Proposition 10.38, as 10.41 (b) places it for
     (13.30a)): 3 + eps and 2 - eps in place of 5/2 + eps and 3/2 - eps, the rest unchanged.

 (xxii) 10.44 (c), [Hin26] Lemma 11.15 and Proposition 11.14 (pp. 226-229; D150). Lemma 11.15's proof: reduce
     alpha_I below 1; Step 1, L~u gains eta in (0, 2 gam_Ups], eta < min Re E^C_I - 1, and integrating L_0's
     components one at a time -- rho_I d_rho_I minus a constant by his Lemma 2.12, then rho_I d_rho_I - rho_+
     d_rho_+ by Lemma 2.23 and u's vanishing for rho_+ >= 1, every eigenvalue of A_h at least 1 -- improves alpha_I
     by eta up to 1; Step 2 passes 1 by (1 - e_Ups) gam_Ups, the least nonzero eigenvalue, with pi-slash_0 u taking
     (1, 0) and u_11 taking (A_h)_(7,6)'s (1, 0); Step 3 completes the expansion, eta < min Re(E^C_I - 1) per pass
     by the closure (E^C_I - 1) + E^tot_I in E^C_I, up to l_I. Proposition 11.14's: integrate backwards from rho_I =
     c_I for the iota+ behaviour (Lemma 2.23, the case alpha_I > 1 or < 1), then forwards again, the a priori E_+ at
     iota+ excluding new exponents. At n = 4 (10.44 (a)-(c)): L_0 has 3/2 + A_0 for 1 + A_0 (10.44 (a), iplus5.py),
     so each threshold 1 becomes 3/2 -- alpha_I below 3/2, the eigenvalues of 3/2 + A_h at least 3/2, the case split
     at 3/2, and rho_I^-1 rho_+^-2 f in H^(oo, 3/2 - eps) at I+; eta <= 2 gam_Ups still meets eta < min Re E^C_I -
     1, as min Re E^C_I > 3/2 + 2 gam_Ups (10.44 (b)); Step 2's term is (3/2, 0) for pi-slash_0 u, while (A_h)_(7,6)'s
     product 2 E-slash_I,0 - 1 is (2, 0), above Step 2's reach 3/2 + eta, eta < (1 - e_Ups) gam_Ups, and so enters at
     Step 3 (10.44 (b); the sixty-third verifier); Step 3's min Re E^C_I > 1, which gives (2 + eps_I) + min Re E^C_I >
     l_I, holds as min Re E^C_I > 3/2 + 2 gam_Ups, and (11.26)'s remainder class takes 10.44 (a)-(b)'s index sets; Step
     3 needs l_I < 3/2 + (1 - e_C)(1 - v_C) gam_C; and Lemmas 2.12 and 2.23 hold on
     [0, 1) x [0, 1) x S^3, stated for a closed manifold S (p. 47). So Lemma 11.15 holds with min(alpha_I, 3/2,
     l_+), and Proposition 11.14 as stated with 10.44 (b)'s index sets.

 (xxiii) 10.66 (f), [Hin26] Theorem 5.23 (p. 109) with Lemma 3.19 (pp. 78-80; D150). Lemma 3.19's proof: g_(m,a) - g_m
     in r^-2 C^oo and the boosts' being isometries of g-bar reduce (3.44) to phi_S^*(g_m - g-bar) - (g_m - g-bar) near
     Y+; the flow of the boost field V(S) on (rho, v, theta), S = c cos theta, (3.45)-(3.49), gives d_rho f_rho =
     (cosh(cs) + cos theta sinh(cs))^-1 and d_v f_v its square, so with a(theta) := (cosh(c/2) + (S/c) sinh(c/2))^-1,
     phi_S^* (rho (dt*)^2) = rho a^3 (dt*)^2 modulo faster terms, and phi_S^* g_m - g_m = 2 m rho (a^3 - 1)(dt*)^2. At n
     = 4: the spin enters the Myers-Perry family one order below the mass (its Kerr-Schild form, 10.36), so g_(mu,A) -
     g_mu is in r^-3 C^oo; Lorentz boosts are isometries of 4+1 Minkowski; the flow equations see only the polar angle
     from the boost axis on S^3, the same ODEs; and g_mu - g-bar = mu rho^2 (dt*)^2 pulls back to mu rho^2 a^4 (dt*)^2
     (gluing5.py D4), of order r^-2, inside the class (10.66 (f)); and (3.43)'s normalization c^2 = (3/(4 pi))
     ||S||^2_(L^2(S^2)), S = c cos theta, is c^2 = (2/pi^2) ||S||^2_(L^2(S^3)), the mean of cos^2 over S^(n-1) being
     1/n, arithmetic. Theorem 5.23's proof: the data smooth in S by differentiating (5.77b), the linearized equation,
     its right side in (5.46)'s space (10.48 (b)'s error classes), solved by (5.52) and Theorem 5.21's proof (10.48
     (c)-(d)), finite difference quotients for the derivative; free of n given those inputs.

 (xxiv) 10.62 (d), [Hin26] Theorem 13.1 (pp. 318-323; D150). His proof: Step 1 fixes E^C from Theorem 7.1 with v_C =
     1/2, C_0 = 100 and (1 - e_C)(1 - v_C) gam_C > 100, and E^Ups with c_Ups, c_H and gam_Ups small for Propositions
     6.12 and 8.6, with 1 + 2 gam_Ups < min Re E_0; Step 2 makes Cauchy data by Proposition 5.25, the exterior solution
     by Theorem 5.21, the interior one by local well-posedness, and the boosted family h_S by Theorem 5.23; Step 3
     solves P(Psi(U)) = 0 by [SR89]'s Nash-Moser theorem, its four assumptions from Theorems 12.3 and 12.8, Moser-type
     product estimates, finite speed of propagation (Corollary 11.66) and smoothing operators on b-Sobolev and
     polyhomogeneous spaces ([Hin24a] Lemma 6.12 and Corollary 6.14); Step 4 defines g and the gauge 1-form eta, gets
     d_nu eta = 0 at the boosted surface from the constraints, eta = 0 and Ric(g) = 0 from the second Bianchi identity's
     homogeneous wave equation, and reads the rates from the terms of g. At n = 4, without the class: Step 1 is (xxv);
     Step 2 is 10.49 (b), with Theorem 5.23 at n = 4 ((xxiii)) for S != 0; Step 3 is 10.49 (c) with Theorems 12.3 and
     12.8 without the class (10.62 (b), on 10.61), finite speed of propagation for a wave-type operator, and the
     smoothing operators as 10.49 (c) takes them; Step 4 is 10.49 (d): with eta = 0 on the surface, the constraints give
     (G delta*_(E^C) eta)(nu, .) = 0, whose components are (1/2) d_nu eta_nu and (1/2) d_nu eta_i -- G is trace reversal
     by 1/2 in every dimension and E^C's terms are of order zero in eta -- so d_nu eta = 0, and the Bianchi step is
     dimension-free; the weakest K+ term chi_K h^(<=1)_b,s1(S_rem) has order 2 + eps_K as his. His rates (2)-(4) are not
     carried. It rests on the readings 10.62 names.

 (xxv) 10.49 (a), Step 1 of [Hin26]'s proof of Theorem 13.1 (p. 320; D150), at n = 4: E^C from Theorem 7.1 at n = 4
     (10.21-10.23, B4) with his v_C, C_0 and (1 - e_C)(1 - v_C) gam_C > 100; E^Ups with c_Ups and c_H from 10.14-10.15;
     gam_Ups small for Proposition 6.12 (10.15-10.18, 10.20 (e)) and Proposition 8.6 (10.24-10.25), the record's point
     taking 1/100; and 3/2 + 2 gam_Ups < min Re E_0 for his 1 + 2 gam_Ups, the I+ threshold being 3/2 (10.48 (d)). Each
     is a choice of parameters; no argument of his is carried beyond the inputs named.

 (xxvi) 10.54 (a), [Hin26a] Theorem 4.9 (p. 37; its proof in his Appendix A; D150). His proof analyses the
     characteristic polynomials' roots type by type, asymptotically in e and h for the scalar sextic. At n = 4 it is
     replaced, not carried: Proposition 10.44 (uniform5.py H1-H2, on damping5.py U4's certificate with h a second
     parameter) computes the five-dimensional polynomials and gives (1)-(3) with 2 for his 1 -- no root with real part
     in [-100, 19/10], the only roots in [-100, 2] lam = 2 at l = 0 and 1, simple, and the counts 3 | 0 | 3, 1 | 0 | 1,
     2 | 0 | 2 -- for every h in (0, 10^-6] at the record's (v, e) = (1/2, 1/102400), and (4) by the top-weight parts'
     roots, free of h (damping5.py U3).

 (xxvii) 10.32 (b), [Hin26] Lemma 8.12 at a = 0, whose proof is [Hin24b] Lemma 3.17's, "verbatim" (pp. 51-53; D150).
     That proof: (1)-(2) the gauge term's contribution is <delta*_(E^C)(0) eta, h*> with eta := [delta_(E^Ups) G, t]
     g-dot^Ups in A^1, since delta_(E^Ups) G g-dot^Ups = 0; h* vanishes inside the horizon and is O(r^-2) at infinity,
     so integration by parts moves delta*_(E^C)(0) onto h*, which annihilates it, h* being G delta* omega* with omega* a
     dual state; then g-dot^Ups is replaced by g-dot: by his Lemma 3.14 the difference is delta* omega, omega in A^(0-),
     and <[D Ric, t] delta* omega, h*> = -<D Ric(0)(dt (x)_s omega), h*> vanishes by integration by parts, h* lying in
     the kernel of D Ric(0)* = G D Ric(0) G (the sixty-third verifier); the rest is twice the pairings of D Ric,
     [Hin23b] Theorem 9.6's boundary pairings. (3): the gauge term vanishes again, by commutator identities
     ([delta_(E^Ups) G, t] is of order zero) and the same integration by parts; h_s1 and h-breve_s1 are replaced by
     h_(b,c) and h-breve_(b,c), the differences in A^(1-) and A^(0-) contributing 0 by identities and integration by
     parts; and [Hin23b] Theorem 9.6 finishes. At n = 4: g-dot^Ups in A^2 and the dual states O(r^-3) (10.28, 10.31
     (b)), so the boundary terms at infinity, eta h* times the area, are O(r^-2 r^-3 r^3) = O(r^-2) where his are O(r^-1
     r^-2 r^2) = O(r^-1) -- both vanish -- and h* still vanishes inside the horizon; the replacement of g-dot^Ups by
     g-dot holds the same way, the difference being pure gauge by the gauge-fixed derivative's construction (10.28) and
     its boundary terms against h* = O(r^-3) vanishing as above; the commutator identities hold in every dimension; and
     Theorem 9.6's pairings are computed at n = 4 as boundary pairings (pairing5.py), with the normalization and the s0
     dual state's sign 10.32 (b) records, his L being half of [Hin24b]'s.

 (xxviii) 10.34 (c), [Hin26] Proposition 8.14 (pp. 158-163; D151). His proof, for the scalar type (the vector type the
     same): Step 0, a first solution of L-hat_b(0) h' = -f_b by Fredholm theory ([Hin26c] Theorem 9.36) against the
     cokernel, not smooth in b near a = 0, which Steps 1-3 replace; Step 1, a formal solution by Lemma 2.15 and the
     obstructions lambda_b,s1, lambda_b,v1, the latter through Proposition 7.4's h-sharp_b,v1, (8.33) giving a vector
     v_b in R^3; Step 2, S_1 and V_1 solving (8.34)-(8.35) by Lemma 8.15; Step 3, L-hat_b(0) mapping h-breve^2_s1 and
     h-breve^1_v1 into rho^2 C^oo, Lemma 2.15, the integration by parts against the dual states' decay, and Corollary
     8.13 (2); Step 4, -3 no s2 root (Lemma 8.4), Lemma 2.15, and m-dot, S_1, a-dot from (8.37) by Lemmas 8.12 and 8.15;
     Step 5, the second Bianchi identity and Theorem 7.1 (2) for the gauge condition and the linearized Einstein
     equation. At n = 4 (10.34 (c)): Step 0 is not used for the conclusion; Step 1 by Lemma 2.15, free of n, and
     Proposition 7.4 at n = 4 ((xvi)), (8.33)'s v_b in so(4) for R^3 (10.34 (b)); Step 2 as 10.34 (b) modifies it, with
     Lemma 8.15 ((xix)), the modification the record's own and solvable by continuity; Step 3 with the generalized
     states one order faster (10.29), the dual states O(r^-3) (10.31 (b)) and Corollary 8.13 (10.33 (f), a reading);
     Step 4 with -3 no root at s2 and v2 (10.34 (iii)) and Lemma 8.12's pairings at n = 4 ((xxvii), 10.32), whose
     determinant does not vanish; Step 5 with Theorem 7.1 (2) (10.21 (e)) and the Bianchi identity, an identity: h in
     A^mu, mu >= -C_0 - 1, gives eta in A^(mu+1), mu + 1 >= -C_0, a stationary solution of box^C, and his Step 5
     concludes eta = 0 from 'the enhanced mode stability recorded in Theorem 7.1(2)' since mu + 1 >= -C_0 (p. 163). That
     theorem's range, alpha in [-C_0 - 3/2, -1/2) with the Euclidean density r^2 dr, meets A^(-C_0) only below its left
     end, A^(-C_0) lying in H-bar_b^alpha for alpha < -C_0 - 3/2 alone, and the source passes over the endpoint; at n =
     4 10.21 (e)'s range l in [-C_0 - 2, 0) with r^3 dr has the same endpoint. The record closes it by its own route,
     not the source's (the sixty-fourth and sixty-fifth verifiers): no indicial root of box^C has real part in [-100, 2)
     (Proposition 10.9), so for C_0 <= 100 the normal operator argument puts eta in A^(2-), which lies in H-bar_b^(s,l)
     with r^3 dr for every l < 0, inside [-C_0 - 2, 0), and 10.21 (e)'s injectivity at l = -eps gives eta = 0. His Part
     (2), the s3 and v3 states at the root -3, has at n = 4 the root -3 simple at s3, v3 and t3 (10.34 (iii)) and the
     states of 10.34 (a). The tensor types, which four dimensions lacks, have their states at Tangherlini from 10.34's
     Gauss functions and near it by the same steps.

 (xxix) 10.46 (e), [Hin26] (2.27) and Proposition 2.25 (pp. 61-63; D151). (2.27) is the hypothesis of Proposition 2.25
     (1), the Fourier transform of a partially polyhomogeneous tensor on M. Its proof -- (2.25a), and Lemmas 2.11, 2.12,
     2.23 and 2.24, b-analysis on M with b-weights -- carries no numeral of the dimension, and the proposition is stated
     on X = R^n (10.59 (a)); so at n = 4 (2.27) is the same inequality of b-weights, beta_I >= beta_iota - beta_K and
     beta_I > beta_iota - min(1, min Re E_K), and 10.46 (iii)'s five-dimensional weights -- 3 + eps_I at I+, 3 + eps_+
     for h and 5 + eps_+ for f at iota+ -- meet it as his do.

 (xxx) 10.62 (c), [Hin26] section 5.6's boost pullback (pp. 108-109) with Theorem 5.23 (D151). His argument: Theorems
     5.17 and 5.21 hold for any Ricci-flat background g_0 with g_0 - g_(m_0) in his class, which by Lemma 3.19 includes
     phi_S^* g_(b_0); Ric commutes with pullback; Upsilon_0 is natural under pullback (5.75), and the cut-off gauge
     (5.76) passes from Upsilon_0 near Sigma_IVP to Upsilon_(E^Ups) near I+; so phi_S^* h solves the initial value
     problem (5.77a) with the pulled-back data (5.77b), whose weights the pullback by the time-1 flow of a b-vector
     field preserves. At n = 4: phi_S is a boost of R^(4,1) (gluing5.py D1, D4); phi_S^* g_(b_0) - g_(b_0) is of order
     r^-2 at infinity ((xxiii)) and of order 2 at iota+ (Proposition 10.39 (ii)), inside 10.48's class and E_+ (10.61
     (a)); Theorems 5.17 and 5.21 are 10.48 (c)-(d), on 10.48's readings; and the invariance of Ric, (5.75), the cut-off
     and the flow hold in every dimension.

 (xxxi) 10.64 (b), [Hin23a] Proposition 3.17 (pp. 15-17; D152). His proof: away from I+, L is a b-operator with x_I a
     time function, and the energy estimate is the vector field argument of [HV20] Proposition 4.3; near I+, the
     multiplier W = w^2 V of (3.22), the pairing (3.23) in L^2(mu_b), mu_b the b-density making L symmetric, Q-bar of
     (3.25) positive elliptic when alpha_I < min(alpha_0, 0), a Poincare inequality in rho_I, the boundary terms dropped
     by their causal signs, and higher b-regularity by commuting Lemma 3.16's fields (rho_0 d_rho_0, rho_I d_rho_I,
     rotations, 1), [L, X_j] = x_I Y_jk X_k. At n = 4 (10.64 (b)): L's leading part is -2 rho_I d_rho_I (rho_0 d_rho_0 -
     rho_I d_rho_I) + x_I^2 (Lap + 3/4) modulo x_I Diff^2_(e,b) (exterior5.py X1); it is symmetric for mu_b = rho_0^5
     rho_I^4 |dg_m| (X2); Q-bar is (3.25) with Lap + 3/4, the added term entering with a positive coefficient (X3); div
     W against the b-density, the Poincare inequality, the boundary terms and the vector field argument away from I+ are
     free of n; and the rotations of S^3 span T S^3, with [x_I^2 3/4, X_j] in x_I^2 C^oo, of Lemma 3.16's form.

 (xxxii) 10.64 (e), [Hin23a] Proposition 3.29 (pp. 21-25; D152). His proof computes 2 P' of (3.30) term by term in the
     splitting (3.12): the conjugated tensor wave operator ((3.31)-(3.34), by Lemmas 3.23 and 3.25), the modified
     symmetric gradient ((3.35)-(3.41)), the modified divergence ((3.42)-(3.44)), the C_g term ((3.45)), the Y_g term
     ((3.46), Lemma 3.28) and the curvature term (Corollary 3.26), collecting A_g, B_g and the remainder L~_g in (x_I
     C^oo + H^(k-2,(l_0, 2 l_I))_b) Diff^2_(e,b), 2 l_I < 1 absorbing the borderline terms. At n = 4 (10.64 (d)-(e)):
     exterior5.py computes each term's leading part -- X1 the conjugated wave operator, with x_I^2 (Lap + 3/4); X4 the
     gauge terms' matrix A, h-free and lower triangular with scalar diagonal; X7 the h-dependent entries, his n = 3
     values times r^(-1/2), so that they join L~_g since l_I < 1/2; X5 R_11's quadratic term -- and Lemmas 3.23-3.28's
     orders each gain rho^(1/2) (10.64 (d)); the remainder's class is his.

 (xxxiii) 10.64 (f), [Hin23a] Corollary 3.31 (pp. 26-27; D152). His proof: the fundamental theorem of calculus with
     P(g_m) = 0 and Proposition 3.29 along g_m + s r^-1 h; the error terms in O^(l_0, l_I)_(k-2) (x_I^2 Lap h, B h, and
     rho_I d_rho_I annihilating h's leading terms at I+), leaving 2 int_0^1 A(rho_0^-1 d_1 h) ds, whose only non-error
     component is the (dx^1)^2 one, through A's (4, 4) and (4, 7) entries: (3.47). At n = 4 (10.64 (f)): the same steps
     with (xxxii)'s A, h-free (X4), so no h enters A's (4, 7) entry at leading order; the quadratic term enters through
     R_11 at r^(-1/2) below the linear one (X5), in O^(l_0, l_I)_(k-2); so 2 rho_I rho^(-7/2) P(g) -- his printed 2
     rho_I^-1 rho^3 being, by Definition 3.27 and the proof's integral of L, 2 rho_I rho^-3 (the sixty-third verifier)
     -- is rho_0^-1 (-4 gam_Ups d_1 h_11)(dx^1)^2 + O^(l_0, l_I)_(k-2). The integration and the error classes are free
     of n.

 (xxxiv) 10.64 (g), [Hin23a] Proposition 3.32 with Lemma 3.33 (pp. 27-30; D152). His proof: the basic estimate (3.53) by
     Proposition 3.17's multiplier, Q-bar dominating the skew-adjoint part (L_g^* - L_g) W for alpha_I large and
     negative (Proposition 3.29 and Sobolev embedding); three b-derivatives commuted, (3.54); the tame estimate (3.55)
     by Lemma 3.34's commutator identity (in any algebra), L~_g's coefficients by Moser estimates in H^(k-2)_b ([Tay11],
     on R^n in logarithmic coordinates), the localization near I+ absorbing, L^0_(g_m)'s commutators by Lemma 3.16,
     A^0_h by Lemma 3.33 on R^4 (d_3 = 2) and B_g similarly; and the sharp weights by A_g's lower triangular form with
     h-free scalar diagonal (3.59a), with a fiber inner product making its skew part small. At n = 4 (10.64 (g)): the
     basic estimate is (xxxi)'s; the algebra property and the embeddings into L^oo hold at the regularities he uses on
     the five-dimensional b-manifold (exterior5.py X6); A_h has no leading term at I+ ((xxxii), X7), so A^0_h = 0 and
     Lemma 3.33 is not used (it would be, on R^5, with d_4 = 3); B_g's h-dependent entries, which he estimates through
     Lemma 3.33, lie in L~_g at n = 4 (10.64 (e)) and are Moser-estimated with its coefficients; the commutator set over
     S^3 is (xxxi)'s; and the sharp-weight step holds with A h-free, lower triangular with scalar diagonal (X4), and
     alpha_I < min(alpha_0, 0) as his.

 (xxxv) 10.48 (b), [Hin26] Proposition 5.11 (pp. 92-97), Proposition 5.14 and Corollary 5.15 (pp. 98-99; D154).
     Proposition 5.11's proof computes (4.13) term by term in the splittings (3.34) and (3.37): Corollary 5.10 for the
     first term; E^C_(g_0) (5.29) from c_C, g_0 and g_0^-1 at infinity; delta_g by Corollary 5.9 and G_g by Lemma 5.6
     with tr g (5.30); the curvature term R_g (5.32) by Lemmas 5.6 and 5.8; delta*_(g_0,E^C) (5.33) by Corollary 5.9
     with g = g_0, C(g, g_0) (5.34) and (delta*_(g_0) - delta*_g) delta_g G_g (5.36) by Lemma 5.7; Upsilon_0 an error
     term; E^Ups (5.37)-(5.38); and the change to the splitting (5.27). Proposition 5.14's: the error term mapped by min
     Re(E^tot_I \ {(1, 0)}) > 1 and Definition 5.3 (3), B_h acting through its first column, and the diagonal entries of
     I + A_h annihilating the leading terms -- (4, 4) 1 + (1 - e_Ups) gam_Ups, (5, 5) 1 + gam_Ups, (6, 6) 1, (7, 7) 1 +
     2 gam_Ups -- with integer powers for its second claim. Corollary 5.15's: P(g_0, g_0) = 0 and the fundamental
     theorem of calculus with Proposition 5.14. At n = 4: the h-free part of every term, and so A_0 -- the leading part
     with 3/2 for 1, the trace entries of G_g and E^Ups taken over S^3 -- is computed (scri5.py, 10.38 (i)); the
     h-dependent terms are [Hin23a]'s (3.30) term by term (10.72 (iii), READ), of orders r^(-1/2) below his
     (exterior5.py X7, (xxxii)); the error classes keep (5.46)'s orders (10.48 (b)); the diagonal entries of 3/2 + A_h
     annihilate the leading terms of 10.44 (b)'s index sets, at 3/2, 3/2 + (1 - e_Ups) gam_Ups, 3/2 + gam_Ups and 3/2 +
     2 gam_Ups, with min Re(E^tot_I \ {(3/2, 0)}) > 3/2 (10.44 (b)); the second claim's integer powers hold as
     Tangherlini's coefficients and c, c_Ups expand in integer powers of r^-1 (10.55 (a)), on his one-line argument; and
     Corollary 5.15 is free of n.

 (xxxvi) 10.48 (c), [Hin26] Theorem 5.17 (pp. 101-102; D154). His proof is [Hin23a] Corollary 3.36's with notational
     changes: the tame estimates (5.52) for the linearized problem -- a first-order energy estimate from the structure
     (5.41b), which is [Hin23a] Proposition 3.29's, commuted with rho_0 d_rho_0, rho_I d_rho_I and the spherical fields
     as in [Hin23a] Proposition 3.32, then the partial expansion at I+ by integrating the leading term ([Hin23a] Theorem
     3.35, and in detail his Theorem 5.21's proof) -- and [SR89]'s Nash-Moser theorem; the region -r/4 <= t_IVP <= 0 is
     treated as the one away from I+. At n = 4: [Hin23a] Propositions 3.17, 3.29 and 3.32 are (xxxi), (xxxii) and
     (xxxiv), (5.41b) is (xxxv)'s; Theorem 3.35's decay recovery has its least positive entry -gam_Ups in both
     dimensions (10.64 (h)); the partial expansion is 10.48 (d)'s, with min Re E_0 > 3/2 + 2 gam_Ups; Corollary 3.36's
     finite loss and [SR89] are free of n (10.64 (i)); and the weights l-flat_0 > l-flat_I, 1 < l-flat_I < 3/2, the
     radiative order 3/2 for his 1 (10.48 (c)).


 (xxxvii) 10.62 (b), [Hin26] Theorem 12.3 (pp. 304-311) and Theorem 12.8 (pp. 312-318; D155). Theorem 12.3's proof is
     the construction of Phi in his section 12.2.1. It sets h^[0], p-vec^[0] and q-vec^[0] from the data, P of them
     having the orders (12.18) by a variant of Corollary 11.9. Step 1 takes P's t*^-3 coefficient f^(3,0) at iota+,
     compactly supported in the interior of iota+ since Ric(g_0) vanishes off supp d chi_K and u_1 lies in ker L-bar
     ((12.19)-(12.20)), sets h^(1,0) := -N_iota+(L-bar, 1)^-1 f^(3,0) (Proposition 9.4), and clears the R -> 0
     expansion (9.32) of t*(u_1 + t*^-1 h^(1,0)) (Proposition 9.9): its s1 logarithm by S^(0,1)_1 through (12.22), its
     other terms of K+ order at most 2, all pure gauge, by p-vec's parameters, and the rest, of K+ order in [2 +
     eps_K, 4 + eps_K], absorbed into q-vec. Step 2 does the same at each iota+ order lam_0 in turn, in steps of
     eps_ind up to 3 + eps_+: the source's orders are Lemma 12.2's (Remark 11.39, Lemma 11.65), L-bar h^(lam_0) =
     -f^(lam_0 + 2) is solved by Corollary 9.18, and (12.29)'s expansion is cleared the same three ways, the threshold
     Re(lam_0 + mu) <= 2. After ceil(3/eps_ind) + 1 steps P(Phi(U)) has (12.31)'s orders; (1)-(3) are read off the
     construction, and Lemma 12.7 adds Corollary 5.15 (1). Theorem 12.8's proof peels Corollary 11.66's solution at
     iota+ in increasing order. P's leading term vanishing reads L-bar(h^(lam_0) + h^(lam_0)') = 0, so the sum lies in
     Res^oo(L-bar, E^C_I, lam_0). Off the spectrum that space is zero, and since h^(lam_0) vanishes at R = 0 to the
     order its K+ order 4 + eps_K gives while every parameter's term in h^(lam_0)' decays more slowly, the parameters
     vanish (Case A); on the spectrum the sum is Res(L-bar, E^C_I, lam_0)(u^0, f) of (9.56), and D_U Phi of those data
     is subtracted (Case B, by Theorem 12.3 (3) and Remark 12.4). At the leading order b', S', S^(0)'_1 and the
     incoming data f'_1 are subtracted together -- his Step 1.3 without the restriction (12.40): 'one needs to replace
     (h', p', q') by (h', p', q') - D_U Phi(b', S', S^(0)'_1, (0, f'_1), 0, ..., 0)' (p. 315), its display, under
     (12.40), having S' = S^(0)'_1 = 0 -- Res_iota+(L-bar, 1) being {0} (the end of his Step 1.2, p. 315) and Phi
     taking S and S^(0)_1 over from U directly (p. 302); what remains is conormal and is D_U Phi of the remainders of
     (12.11) (Step 3). At n = 4: iota+ is [0, oo]_R x S^3. The mass and the boost enter at (2, 0) for his (1, 0)
     (10.61 (a); Proposition 10.39 (ii)), so Step 1 is the step at lam_0 = 2, with t*^-4 for t*^-3: f^(4,0) is
     compactly supported for the same reason, the patched curvature being of order 4 where the cut-off varies
     (Proposition 10.39 (iii)), and Res(L-bar, 2) = {0} (10.47 (b)) stands for his Res(L-bar, 1) = {0}. The induction
     starts below it, at alpha_min = 3/2 + (1 - e_Ups) gam_Ups, the least incoming exponent (10.44 (e)); the terms
     below 2 are Step 2's, the parameters of order 2 entering P only at order 4, and his count of steps suffices since
     alpha_min > 1. The centre-of-mass shift S^(0)_1 is the exception (the sixty-fourth verifier). Its patch h^(0)_s1
     = -[delta*_g_b, chi_K] omega^(0)_b,s1 = -d chi_K (x)_s omega^(0)_b,s1 ((1.39b), p. 26) has iota+ order 1 at every
     n, chi_K varying where r ~ t*; but its leading part -delta-bar*(chi_K omega-bar^(0)_s1) is pure gauge for g-bar,
     omega-bar^(0)_s1 = dx^i being Killing (his footnote 143, p. 314), and in (11.135a) the patch enters Ric's
     argument while the gauge 1-form Upsilon_E_Ups(g_b0 + h, g_b0) is evaluated without it. So S^(0)_1 enters P
     linearly only through D Ric(h^(0)_s1) + delta* theta^(0)_s1 = L_b(chi_K h_b,s1) = [L_b, chi_K] h_b,s1 ((1.39a)),
     of iota+ order 5 at n = 4: h_b,s1 lies in A^((3,0) u (3 + E_ind)) (10.28), where his (6.32a) has (2, 0), and the
     commutator, first order with coefficients d chi_K and box chi_K supported where r ~ t*, adds 2, each derivative
     there gaining t*^-1 (so 4 at n = 3; this record's count, not printed in the source); and quadratically, along the
     pure gauge patch, at order 4 in every dimension; both are compactly supported in (iota+)^o, the second in f^(4,0)
     beside the mass's and the boost's, the first cleared by Step 2 at lam_0 = 3. In Theorem 12.8 S^(0)'_1 is the
     parameter Corollary 11.66 gives, and D_U Phi(b', S', S^(0)'_1, (0, f'), 0, ...) is subtracted at lam_0 = 2 as his
     Step 1.3's general case subtracts it at his leading order; placing it at lam_0 = 2 is this record's step, not the
     source's: the patch is h_tot's one term of order 1, and its linearized output has order at least 4, so no step
     below lam_0 = 2 reads it. (9.32)'s lists are Proposition 10.46's: six pure gauge classes eliminated at K+ order
     at most 2 and fourteen recorded, and the physical s2, v2 and t2 recorded beside them, with T_2 added (10.61 (c));
     every recorded term's L_b-image has K+ order above 4, which is Lemma 12.2's input, and every recorded term's own
     K+ order is below 4 + eps_K, which is Case A's. Whether five dimensions carry the s1 logarithm, and so S^(0,1)_1,
     is 10.61 (b)'s question, the parameter zero if not; the metric terms of size t*^-1 log t* (his Lemmas 11.24 and
     11.38 and (11.191)) are annihilated to leading order by D_g-bar Ric, his remark after (12.18) (p. 304), because
     the iota+ model is Minkowski's, which holds at every n; so whichever are present at n = 4 are annihilated, the
     boost's being absent and the mass patch's and s0's not computed (10.61 (a)). The orders 3 + eps_+, 5 + eps_+, 4 +
     eps_I and 4 + eps_K stand (10.61 (d)); Corollary 11.66 is 10.61 (c)'s; and Corollary 5.15 is free of n ((xxxv)).
     The iota+ solution theory -- Proposition 9.4 (2), Corollary 9.18 with its expansion, Proposition 9.9, and
     (9.54)-(9.56) with Proposition 9.22's right inverse -- enters at n = 4 as 10.47's OPEN has it, READ at n = 3 with
     its five-dimensional inputs 10.37's and 10.44's: a reading; and Res(L-bar, 2) = {0} is 10.47 (b)'s, which rests
     on 10.37 (c)-(e)'s readings.

 (xxxviii) 10.47 (d), [Hin26] Theorem 12.3 in the class (D155). (xxxvii)'s construction with the class's data and lists:
     p-vec^[0] carries the mass alone, S, S^(0)_1, S_rem and V_1,rem vanishing (10.43 (b)), so Step 1 is the step at
     lam_0 = 2 where m - m_0 enters (Proposition 10.39 (ii)); each step eliminates the G-fixed pure gauge types S^(0)_0,
     S^(c0)_0 and S^(0)_2 at K+ order at most 2 (Proposition 10.42 (ii); 10.46 (b)) and records the rest below K+ order
     3 + eps_K in q-vec's G-fixed list (10.46 (d)), whose L_b-images have that order (10.46 (d), through his (9.37));
     the target's K+ order is 3 + eps_K for his 4 + eps_K, that of h and of L_b h_b,rem(q-vec); there is no s1 term to
     clear, the G-fixed S_l vanishing at odd l (10.43 (b)); and each step's solution is G-invariant when its inputs are,
     every operation commuting with O(4) (10.47 (c)). It rests on (xxxvii)'s reading of the iota+ solution theory.

 (xxxix) 10.47 (e), [Hin26] Theorem 12.8 in the class (D155). (xxxvii)'s peeling of the forward solution of Corollary
     11.66 in the class (10.46 (d)), G-invariant being unique. At lam_0 = 2 the mass m' (b' = (m', 0)) and the incoming
     data f'_2 are subtracted together, Res(L-bar, 2) being {0} (10.47 (b)). In Case A every G-fixed parameter at lam_0
     vanishes, its term having K+ order below 3 + eps_K, which is h^(lam_0)'s in the class (10.46 (b), (d)); in Case B
     D_U Phi of G-fixed data (u^0, f) is subtracted, (9.56) through Proposition 9.22's right inverse; Step 3's
     remainders are m'_rem and h-tilde'. Each subtraction is D_U Phi at data the step determines uniquely from
     G-invariant objects, so U' lies in D^oo_G -- 10.43 (e)'s reading, as 10.47 (e) has it; Psi for Phi is Lemma 12.7's,
     with S = 0. It rests on (xxxvii)'s reading.

 (xl) 10.42 (e), [Hin26] Theorem 11.12 (pp. 225-226; D156). It has no proof of its own: it states [Hin26c] Theorem 11.1
     for L_(g,g0), which Corollary 11.10 makes admissible relative to L_b in [Hin26c] Definition 5.18's sense, in the
     unweighted b-densities of [Hin26c] (11.4)-(11.6a); Remark 11.13's tameness is that theorem's. At n = 4: Corollary
     11.10 is 10.42 (d); the densities shift the weights at (I+, iota+, K+) by (n/2, (n + 1)/2, 1/2) = (2, 5/2, 1/2) for
     his (3/2, 2, 1/2) (Proposition 10.39 (i), cone5.py C1), so (11.21)-(11.23) read as 10.42 (e) states them, beta_+ in
     (1/2, 1/2 + eps_ind) in both dimensions; the top of beta_I is the radiation order (n - 1)/2 = 3/2 for his 1 (C1,
     [Hin26c] (10.2)'s threshold at n = 4 being a reading); and the sf-loss is 10.41 (a)'s. It rests on the reading of
     [Hin26c] Theorem 11.1 and Definitions 5.15 and 5.18 at n = 4 (10.42's OPEN; 10.58 (c)).

 (xli) 10.21 (a), [Hin26a] (6.4) (p. 68; D156). His derivation replaces g_(m,a) by the Minkowski metric g-bar, with
     g-bar^-1 = -2 d_t* (x)_s d_r + d_r^2 + r^-2 g-slash^-1, recalls (4.16), and estimates the errors by (2.9) and by
     comparison with (2.8), which gives the order of Q's principal part, its subprincipal rho^2 Diff^0_b part absorbed
     into S~; the zero energy operator is rho^2 times (4.18) plus rho^3 Diff^2_b. At n = 4: on 4+1 Minkowski with c =
     r^-1 (dt - v dr) the leading term is -2 d_t* rho (rho d_rho - 3/2 - S-bar^C), with no d_t* times a tangential
     derivative and no d_t*^2 term, and S-bar^C is his matrix with three angular copies, its spectrum positive
     (Proposition 10.18 (i), cpmodes5.py K1) -- the shift (n - 1)/2 for his 1, g-slash that of S^3; c is 10.14's, equal
     to r^-1 (dt - v dr) for large r; and Tangherlini differs from Minkowski at O(rho^2) (thresh5.py U4), one power
     below Kerr, so the errors are at most his orders: Q in rho^3 Diff^1_b, R in rho^2 C^oo, the zero energy operator in
     rho^2 Diff^2_b.

 (xlii) 10.21 (c), [Hin26a] Theorem 6.2 (2), injectivity (p. 68; D156). His proof: for s >= 1 a kernel element omega_0
     of (6.1) is a stationary solution with data (omega_0, 0), in H-bar_b^(s,l) with l >= alpha_sf + 1/2, so Theorem
     5.2 gives (6.3), omega in rho_sf^(alpha_sf) L^2, which a nonzero stationary omega is not over [0, oo) times an
     annulus; for general s, chi(tau) omega_0 solves the forward problem with source [box^C, chi] omega_0 in
     rho_sf^(alpha_sf + 2) rho_K^(alpha_K) H^(s-1)_3b, and Theorem 5.2 again applies. At n = 4: the density r^3 |dr
     dg/|, so alpha_sf = -C_0 - 5/2 and l >= -C_0 - 2 = alpha_sf + 1/2 (Proposition 10.18 (iii), cpmodes5.py K3); the
     annulus and the cut-off are free of n; and Theorem 5.2 at n = 4 is (lxi)'s, written out on no reading (D167), so
     this item rests on none.

 (xliii) 10.56 (b), [Hin26a] Theorem 6.2 (pp. 67-69; D156). His proof fixes alpha_K = 1 and alpha_sf = -C_0 - 2, which
     satisfy (5.14), and applies Theorem 5.2 with C_0 + 1, the indicial roots being Theorem 4.9's with C_0 + 4. Part
     (1): by (6.4) an outgoing mode's omega_1 satisfies a regular-singular ODE gaining an order while gamma + 1 < 1 +
     min spec S-bar^C, so lies in A^1, every eigenvalue being positive; its data are then O(r^-1) and O(1), in
     rho^(-3/2-eps) H-bar_b, inside rho^(alpha_sf + 1/2); Theorem 5.2 puts omega in rho_sf^(alpha_sf) L^2, which a
     nonzero mode, e^((Im sigma) t) |omega_0|, is not over an annulus. Part (2): injectivity as (xlii); Fredholm by the
     citations of p. 68; index 0 by Theorem B.1 with [Hin26b] Corollary 9.43, or by deforming to Schwarzschild, where
     the radial operators over the spherical harmonics have index 0 by Theorem 4.9 (3), or through the adjoint,
     injective on H-dot^(s',l')_b with l' = -l - 2 > -3/2 since its indicial roots 1 - lam-bar have real part <= 0 or >
     C_0 + 3 and the L^oo to L^2 shift is -3/2. At n = 4: (5.14) is alpha_sf < b* - 1, alpha_K > alpha_sf + 1 - b*
     (10.22 (c), solv5.py Q4), met by alpha_K = 1 and alpha_sf = -C_0 - 5/2 (10.21 (b)); Theorem 5.2 is (lxi)'s, written
     out (D167); the roots are Proposition 10.9's, Theorem 4.9 at n = 4 for h in (0, 10^-6] (10.54 (a)), the top of
     (6.1)'s range 2 for his 1; (6.4) is (xli), the ODE gaining while gamma + 1 < 3/2 + min spec S-bar^C, positive
     (Proposition 10.18 (i)); r_* - r = O(r^-1) (10.21 (b)); the data lie in rho^(-2-eps) H-bar_b (r^3 |dr dg/|)
     (Proposition 10.18 (iii)); the direct route's radial operators are over the scalar and vector harmonics of S^3,
     each of index 0 by 10.12's even split of the roots (10.21 (d)), Fredholm by [Hin26c] Theorem 9.36 at n = 4 (10.20,
     a reading) given 10.21 (d)'s horizon threshold, OPEN there; and the shift is n/2 = 2 (10.21 (e)). It rests on the
     readings 10.21 names, Theorem 5.2 no longer adding one (D167).

 (xliv) 10.23 (b), [Hin26a] Proposition B.2 (pp. 87-91; D158). His proof: r^2 box^C(sigma) is b-elliptic in r < 2,
     symbol xi_b^2 + |eta_b|^2; its scattering symbol G_sigma = -2 sigma xi + xi^2 + |eta|^2 is characteristic over rho
     = 0 at R_out, with the rescaled Hamiltonian flow (B.16) from the source R_in (xi = 2 sigma) to R_out for sigma =
     +-1, and Char_sigma = R_out for Im sigma > 0. Real sigma: (B.20) by elliptic estimates, a radial sink estimate at
     R_out with the commutant (B.21), whose main term (2 l + 1)(sigma - xi) is shifted by (B.24) = -2 h^-1 S-bar -- the
     scalar part 2 i sigma (rho^2 d_rho - rho) being symmetric for rho^-3 d rho/rho and box^C(0) - box^C(0)* in rho^2
     Diff^1_b -- so l < -1/2 + h^-1 min spec S-bar (B.26); a radial source estimate at R_in, its shift found through the
     involution t -> -t, c_v -> -c_(-v), so l > -1/2 - h^-1 (1 - e)(1 + v); real principal type propagation between;
     then (B.19) by the Mellin transform at r = 0, H^(s,beta)_b(r^2 |dr|) = H^(s,-3/2+beta)_b(dr/r), the indicial roots
     there the negatives of Theorem 4.9's, so beta in (1/2, 3/2 + C_0]; and the dual estimate (B.28) alike. Complex
     sigma: sigma^-1 box^C(sigma) = P - i Q with Q_0 = 2 rho h^-1 S-bar, Q_3 a complex absorption, box^C(0) = sum T_j*
     T_j + R from its b-symbol, and the same threshold. Uniformity in sigma by limiting absorption. Index 0: for scalar
     type l >= 1, lowering beta below the roots raises the index by 3 (Theorem 4.9 (3), Melrose's relative index
     theorem), deforming h^-1 to 0 keeps it, and raising beta into the free operator's window, where it is invertible
     ([Hin26b] Proposition 9.40, [Hin26a] Lemma 4.1), lowers it by 3; so I = 0. At n = 4: the symbols are free of n, eta
     in T*S^3; the scalar part is 2 i sigma (rho^2 d_rho - 3/2 rho), symmetric for rho^-4 d rho/rho, which is r^3 dr,
     the shift (n - 1)/2 (Proposition 10.18 (i), cpmodes5.py K1), so (B.24) is again -2 h^-1 S-bar with S-bar K1's
     matrix, positive; the thresholds are l < -1/2 + h^-1 (1 - e)(1 - v) and l > -1/2 - h^-1 (1 - e)(1 + v), the
     scattering weight -1/2 free of n and the bottoms K1's and K2's (Proposition 10.18 (i)-(ii); for R_in through the
     adjoint, Proposition 10.20 (iv), tface5.py F4); the involution holds in every dimension; at r = 0 H^(s, beta)_b(r^3
     |dr|) = H^(s,-2+beta)_b(dr/r) and the roots are Proposition 10.9's negatives, so beta in (0, 2 + C_0] for C_0 <=
     100 (Proposition 10.20 (ii), F2; 10.23 (a)); the decomposition into T_j* T_j and the absorption are free of n; and
     the index count is 3 at scalar type l >= 1, 2 at l = 0 and 1 at vector type, by 10.12's roots (Theorem 4.9 (3) at n
     = 4, 10.54 (a)), and the free operator's roots are -3, -2 | 0, 1 at l = 0, -l - 3, -l - 2, -l - 1 | l - 1, l, l + 1
     and -l - 2 | l, with the window (-2, 0) for beta - 2 (Proposition 10.20 (v), F5), its invertibility there [Hin26c]
     Proposition 9.40 at n = 4 (10.20, a reading).

 (xlv) 10.23 (c), [Hin26a] Theorem B.4 (pp. 93-98; D158). His proof, by Theorem 5.2's: energy estimates near X in tau
     = t/r, d tau past timelike for |tau| < 1, the metric a weighted b-metric, (B.34)-(B.35) by Proposition 5.16's
     proof; at nonzero and infinite semiclassical frequencies (B.37) by Proposition 5.6's, with the commutant at fiber
     infinity; the radial source estimate at cf, (B.39)-(B.40), from the symbol identity (B.38), where r^2 (-l(dw/w) +
     S) is positive definite at rho_cf = 0 for alpha_cf > 1/2 by (4.5)-(4.7) with beta_K - beta_sf replaced by
     alpha_cf - 1, -(1/2) r^2 l(dr/r) has positive eigenvalues, and r^2 l(d t/r) is negative definite on supp chi_1'
     by Lemma 3.5; propagation in sf by Proposition 5.11 into the sink for alpha_sf < -1/2 and section 5.2.5's real
     principal type propagation; their combination (B.41), duality for solvability, the initial value problem as at
     the end of section 5.2.7; and strong uniqueness by finite speed of propagation and a semiclassical estimate on {r
     <= 1 - t} with an energy estimate near r = 1 - t. At n = 4: the spacetime density is r^4 |dt (dr/r) dg/|
     (Proposition 10.20 (iv), tface5.py F4); d tau is past timelike for |tau| < 1 (Proposition 10.19 (ii) at mu = 0);
     the cf positivity holds for alpha_cf > 1 - b* at (v, e) = (1/2, 1/102400) and, as e -> 0, for alpha_cf > 0
     (cform5.py C7; Proposition 10.20 (iii), F3), his alpha_cf > 1/2; -(1/2) r^2 l(dr/r) has characteristic polynomial
     (lam - v)^3 (lam^2 - (3 - e) v lam + (2 - e) v^2 - e), roots positive (F3), and Lemmas 3.3 and 3.5 hold at n = 4
     (10.13 (i)); Proposition 5.11 at the sink holds for alpha_sf < b* - 1 (10.22 (c)); the energy estimates are
     Minkowski geometry, Lemma 5.14 and Corollary 5.15 stated in any dimension (10.22 (d)); finite speed of
     propagation is free of n; and the semiclassical edge-b calculus is stated for every dimension ([Hin23d]; 10.65
     (a)). It rested on 10.22 (e)'s reading in its edge-b version, that each commutator's sign is the computed
     five-dimensional symbol's; the section 5.2 proofs it borrows are written out at n = 4 in (lxi) with those signs
     computed, and its own cf estimate's are F3's, so it rests on no reading (D167).

 (xlvi) 10.23 (d), [Hin26a] section B.4 (p. 98; D158). His proof: without loss C_0 >= 2; l = -1/2 and beta = 7/2 (B.42);
     by Proposition B.2 it suffices that a kernel element omega_0 vanishes (B.43); Theorem B.4 with (alpha_sf, alpha_cf)
     = (-5/2, 5/2), e_0 the smaller of Theorems B.4's and 4.9's; omega = e^(-i sigma (t - r)) omega_0 solves the
     equation with data (B.44), which, Im sigma >= 0, lie in rho_sf^(l-1) rho_cf^beta H^(1-j)_b(X, r^2 |dr d omega|),
     inside (B.33)'s rho_sf^(alpha_sf + 1/2) rho_cf^(alpha_cf - 1/2) L^2; so Theorem B.4 gives a solution omega' in
     rho_sf^alpha_sf rho_cf^alpha_cf H-bar^1_eb, equal to omega by its uniqueness (2); and if omega_0 != 0, |omega_0| >=
     c on an open U, so the integral of rho_sf^(-2 alpha_sf) rho_cf^(-2 alpha_cf) |omega|^2 over U x [T, oo) is at least
     c^2 times the integral of t^(2 (alpha_sf + alpha_cf)) dt, infinite since 2 (alpha_sf + alpha_cf) = 0 >= -1. At n =
     4 (Proposition 10.20 (iv), tface5.py F4): (-5/2, 5/2) meets the five-dimensional thresholds alpha_sf < b* - 1 and
     alpha_cf > 1 - b*; l = -1/2 lies in the l-window for every h > 0; beta = 7/2 lies in (0, 2 + C_0] iff C_0 >= 3/2,
     his "without loss" C_0 >= 2 sufficing; with r^3 |dr dg/| the data weights are alpha_sf + 1/2 and alpha_cf - 1/2 and
     (B.44)'s data lie in them; U is open in R^4 \ {0}; and the closing integral diverges, its t-power free of n.
     Proposition B.2 is (xliv) and Theorem B.4 (xlv); it rests on their readings.

 (xlvii) 10.19 (a), [Hin26c] Proposition 9.10 (pp. 167-168; D159). His proof of the direct estimate at R_in: for Im
     sigma > 0 an elliptic estimate; for sigma near real, the commutant of symbol rho^(-r-1/2) psi_d psi_R, q =
     (xi_sc + 2 Re sigma)^2 + |eta_sc|^2 (9.35), and (9.34)'s three terms -- H_(Re G) q >= (Re sigma) q near R_in,
     the double commutator subprincipal, and Im P-hat_0(sigma) expanded by (9.36), its sigma^2 term subprincipal,
     d_sigma P-hat_0(0) = 2 i rho(rho d_rho - (n - 1)/2 - S) - i Q symmetric for r^(n-1) |dr dg/| when S = Q = 0, so
     that only S enters, (9.38a), and Im P-hat_0(0) in rho^2 Diff^1_b fibre-linear, (9.38b) -- give the threshold 4
     r + 2 + 4 Re S - 2 p_1 > 0, r > (1/2)(-1 + vartheta_in) (9.32); the Im sigma term has a sign, sigma^1(-Re
     d_sigma P-hat_0(0)) = 4 Re sigma > 0 at R_in. At n = 4: his proof is written with (n - 1)/2 and the density
     r^(n-1) (p. 168), and rho(rho d_rho - 3/2) is skew for rho^-5 d rho exactly (Proposition 10.16 (i),
     hienergy5.py V1); so (9.38a)-(9.38b) give p_1 - 2 Re S = -2 Re(A_w + S-bar) in any fibre inner product, A_w +
     S-bar = D S-bar D similar to S-bar (V1), vartheta_in = -2 S-bar to within eps, exactly when S-bar is
     diagonalisable (Lemma 5.12, Remark 10.2), and (9.16b) reads r + alpha_+ > -1/2 - S-bar, the mirror of 10.18's
     -1/2 + S-bar at R_out; H_(Re G) q and the Im sigma term's sign are free of n; and admissible order functions
     exist at every weight (Definition 5.11; 10.18). The operators are on bundles, the scalar-to-bundle step being
     the author's notational remark (10.53 (d)), part of 10.19 (d)'s reading.

 (xlviii) 10.55 (b), [Hin26c] Theorem 9.5 (3) and (5) (pp. 163, 172-173; D159). His proof of (3): Fredholm by the
     compact inclusions in (9.17); at sigma_0 in {sigma != 0, Im sigma >= 0} the augmented operator (9.54) -- E_01 onto
     a complement of the range, E_10 an isomorphism on the kernel -- is invertible, and by the uniform estimates (9.17)
     and a weak-limit argument ([Vas13] section 2.7) invertible nearby, so the index is locally, hence globally,
     constant on that connected set; it is 0 by Theorem 9.16 (3)'s invertibility at large |sigma| (his footnote 72,
     section 9.3). His proof of (5): a kernel element lies in H-bar^(oo,r)_b for r < -1/2 + S-bar, by Sobolev embedding
     (3.72) in C^(oo,1+S-bar-eps)_b, and integrating (9.55), (rho d_rho - 1 - S) u = -(2 i sigma rho)^-1 (P-hat_0(0) - i
     sigma Q + g^00 sigma^2) u, from rho = delta to 0 gives A^(1 + S-bar - eps). At n = 4: (9.17) is Theorem 9.5 (1)-(2)
     at n = 4, 10.19 (d)'s reading; the compactness and the augmentation are free of n; Theorem 9.16 (3) at n = 4 is
     10.53 (e)'s reading; the embedding shifts by n/2 = 2 for his 3/2, and (9.55) carries (n - 1)/2 = 3/2 for his 1
     (10.53 (c)), so kernel elements lie in A^(3/2 + S-bar - eps). It rests on the readings of 10.19 (d) and 10.53 (e).

 (xlix) 10.45 (b), [Hin26] Propositions 11.17 and 11.32 with Lemmas 11.18-11.19 (pp. 232-237, 247-252; D160), in the
     class. Proposition 11.17's proof: Theorem 11.12 and Proposition 11.14 give (11.40); iterating, (11.19) puts (L -
     L_b) u one step better, so L_b u = f' (11.41) with iota+ weight alpha~_+ below the cap that transport from I+ sets
     and K+ weight alpha~_K; Step 1 solves at I+ by Proposition 11.16; Step 2 splits by the Fourier transform in t*,
     u_hi decaying arbitrarily ([Hin26c] Corollary 13.17), f-hat's orders by (2.25a), the low-energy part by [Hin26c]
     Proposition 13.18 in the indicial gap of L-hat_b(0) (11.45), u_reg by a contour shift and (2.26a), and u_sing =
     g-dot + h_s1 through (10.56), (10.59) and (11.47)-(11.49), Lemma 11.19's moment condition and Lemma 11.18 (1): two
     integrations of d_t*; Step 3 Proposition 11.14 again. Lemma 11.18's proof integrates the hyperbolic field t* d_t*
     by Lemma 2.23 and the b-normal field at K+ by Lemma 2.12; Lemma 11.19's splits d_t* u near scf and zf, the scf
     part's total t*-integral vanishing (11.62) by its continuity across sigma = 0 in rho^beta_I |sigma|^(beta_iota -
     beta_I) H^k_b(|d sigma/sigma| d mu_b). Proposition 11.32's proof is the same scheme from (11.98): Step 1
     Proposition 11.16, with E-sharp_+; Step 2 removes the iota+ expansion by Corollary 9.12 (Proposition 9.11 at lam =
     1); Step 3.1 inverts the augmented zero energy operator (Proposition 10.6), S-hat_1(0) vanishing with (11.93)'s
     leading term, u-hat_reg,1(0) in H^(oo,(E_ind,+, alpha_+ - 1))_b by a normal operator argument (11.107b), and Lemma
     11.33 bounds the augmentation's terms; Step 3.2 removes the tf error by Proposition 9.30; Step 3.3 applies [Hin26c]
     Proposition 13.18, and one integration of d_t* bounds u_sing ((11.114)- (11.115), footnote 116); Step 4 Proposition
     11.14. In the class, at n = 4: h_s1 = 0 and S-hat_1 = 0 at every sigma (10.45 (a); S_1 has no G-fixed element,
     Proposition 10.40 (ii)), so (11.47)-(11.49) and (11.114) keep only F(d_t* g-dot), regular at zf with 10.40 (b)'s
     weights, and one integration of d_t* suffices in both propositions, u_sing = g-dot of K+ order alpha~_K - 1 for his
     alpha~_K - 2; Proposition 11.20 reduces to S-dot = 0 and Proposition 11.30 is not needed ((li)). The inputs:
     Theorem 11.12 is (xl), Proposition 11.14 (xxii) and Proposition 11.16 10.44 (d), whose E-sharp_+ has least elements
     3/2 + (1 - e_Ups) gam_Ups and 2 for his 1 and 1 + (1 - e_Ups) gam_Ups; (11.19) gains 2 + min Re E_+ at iota+ (10.42
     (c), 10.44 (e)), at least his; the cap, his 1, is 3/2 + (1 - e_Ups) gam_Ups, and h's K+ order is the class's (10.45
     (d)); (2.25a) and (2.26a) are Proposition 2.25's, stated on R^n ((xxix)); the indicial gap is 10.24's; the
     augmented zero energy operator is invertible with the mass state alone (10.43 (d), 10.45 (a)); Lemma 11.33's
     entries, from Lemma 10.5, are one order better at iota+ (10.39 (a), Proposition 10.36 (iii)); E_ind,+ is drawn from
     10.24's roots on G-invariant tensors; and Lemmas 11.18 and 11.19 hold as stated, their proofs using Lemmas 2.12 and
     2.23 on [0, 1) x [0, 1) x S^3, stated for a closed manifold ((xxii)), the Fourier transform in t* and d mu_b =
     |dx|/|x|^4 for his |dx|/|x|^3, the moment argument free of n. It rests on [Hin26c] Proposition 13.18 and Corollary
     13.17 at n = 4 (10.58 (c), a reading) and on Corollary 9.12 and Propositions 9.11 and 9.30 at n = 4, section 9's
     iota+ and tf solution theory, READ at n = 3: the reading (xxxvii) names, extended to these.

 (l) 10.61 (b), [Hin26] Propositions 11.17, 11.20, 11.30, 11.32 and 11.34, Lemma 11.45 and Corollary 11.46 (pp. 232-262;
     D160), without the class. Propositions 11.17 and 11.32 are (xlix)'s schemes with h_s1 and S-hat_1 present: two
     integrations of d_t* in 11.17 ((11.48)-(11.51), footnote 106), one in 11.32 (footnote 116). Proposition 11.20's
     proof: Proposition 11.17 and (11.19) give (11.65); Step 1 Proposition 11.16, leaving an iota+ term off K+
     (11.66a)-(11.66b); Step 2 removes it by Proposition 9.11; Step 3 inverts the augmented operator at sigma = 0
     (Proposition 10.6), compares near zero energy by Lemma 11.21 ((10.31), Lemma 10.5), applies [Hin26c] Proposition
     13.18 (11.71), integrates d_t* twice by Lemmas 11.19 and 11.18 ((11.73)-(11.74)), and identifies the t* term as
     h_b,s1(S-hat_1(0)) through (10.13) (11.75); Step 4 Proposition 11.14. Proposition 11.30's: Definition 11.25's P,
     whose linearization has Proposition 11.6's structure, so 11.17 and 11.20 hold for it; (1) on Lemma 11.28's source
     classes; (2) S^(-1) is the identity at (0, b0, 0) by (11.76)-(11.78b) and continuous in (h, b, S). Proposition
     11.34's: Proposition 11.32 and (11.19); Step 1 Proposition 11.16; Step 2 Proposition 9.11 for the leading iota+
     term, giving S-dot^(0,1)_1, and Corollary 9.12 with Proposition 11.16 for the rest; Step 3 the high-energy part,
     (2.25a), Proposition 10.6 at zero energy, Propositions 9.30 and 9.35 at tf; Step 4 the sub-leading zero energy
     piece (11.127); Step 5 [Hin26c] Proposition 13.18; Step 6 the constant term through (10.13), (11.133). Lemma 11.45:
     by (11.134b), (11.135b) and the argument after (11.137) the map is the identity at (h, p) = 0, and continuous;
     Corollary 11.46 solves the resulting linear equation. At n = 4 (10.61 (a)-(b)): (xlix)'s inputs without the class's
     restrictions; the states and their transforms are 10.28-10.29's and 10.40 (b)'s, one order faster than his and with
     no logarithm (10.39); S_1 is R^4 and b = (mu, A) lies in R + so(4) (10.36, 10.66 (g)); the second order pole is
     10.35 (b)'s, a reading, ended by Proposition 10.29 (iii)'s pairing (3 pi^2/2) mu; (10.13)'s total integrals and the
     identities (11.76)-(11.78b), (11.134b) and (11.135b) are free of n; Definition 11.25's h^(-1) and theta^(-1) and
     Lemma 11.24's classes take the boost's iota+ order 2 for his (1, 1), with no logarithm (10.61 (a)), so (11.80)'s
     (3, 1) question does not arise; Lemmas 11.28 and 11.41's classes shift as E_+ does (10.42 (c)); S^(-1)_(h,b,S) is
     the identity plus o(1) on R^4 (10.66 (g)); the K+ orders and the two orders of loss are his (10.61); and the iota+
     terms of Step 2 are taken in increasing order, the radiative ones from 3/2 + (1 - e_Ups) gam_Ups (10.44 (d)) before
     the parameters' at 2 + 2 = 4, whose Proposition 9.11 at lam = 2 carries S-dot^(0,1)_1 only if five dimensions carry
     his log t* h_b,s1 of (9.39b) -- 10.61 (b)'s question, the parameter zero if not. It rests on (xlix)'s readings,
     with Proposition 9.35 added to section 9's, and on 10.35 (b)'s.

 (li) 10.43 (c), [Hin26] section 11's steps in the class (pp. 231-295; D160). His sections 11.3-11.8 extract, in turn,
     the boost S-dot (11.4), the Kerr parameters and centre-of-mass shifts (11.6), the S_1 shifts and final parameters
     (11.7) and the pure gauge and physical terms (11.8), each as the unique solution of a linear problem built from G-
     equivariant objects (10.47 (c)). At n = 4 in the class: S_1 has no G-fixed element (Proposition 10.40 (ii)), so
     every S_1-valued parameter of a G-invariant solution vanishes -- S-dot = S-hat_1(0) of (11.75), S^(0)_1 and
     S^(0,1)_1 of (11.133) and Step 2.1, and the S^(lam-1,k)_1 shifts of Proposition 11.51 -- by uniqueness, each being
     G-equivariant in f; the rotation A in so(4) has no G-fixed element (10.43 (b)), so b = (m, 0); and Definition
     11.25's augmentation #1 enters with S = 0. So Step 2 reduces to Proposition 11.20 with S-dot = 0, whose improved
     remainder is still used ((xlix)); Step 4 to the mass change; Step 5 to Proposition 11.51 with no S_1 shifts (10.46
     (a)); Step 6 to the gauge modifications of (b)'s G-fixed components (10.46 (b)); Steps 1 and 3 are his, (xlix)'s at
     n = 4. It rests on (xlix)'s readings and on 10.46 (a)-(b)'s (the sixty-fifth verifier).

 (lii) 10.45 (e), [Hin26] Steps 1-4 in the class (pp. 231-262; D160). (xlix) and 10.45 (c) -- Proposition 11.34 and
     Corollary 11.46 in the class, the mass the only parameter and m' -> m-dot the identity at (h, m) = (0, m_0) by
     Lemma 11.45's identity (11.134b), continuous -- give for G-invariant f with 10.45 (c)-(d)'s orders a forward
     solution chi_K g-dot^Ups_b(m-dot) + u~, u~ decaying at K+, the mass change removed by the final mass. At n = 4 the
     iota+ cap is 3/2 + (1 - e_Ups) gam_Ups (10.45 (d)), the weight at I+ 10.46 (e)'s, and the readings (xlix)'s.

 (liii) 10.46 (a), [Hin26] Proposition 11.51 in the class (pp. 262-272; D161). His proof inducts on the K+ order alpha_K
     in eps_K steps from Corollary 11.46. Part 1 takes u at K+ order alpha'_K - 2 from the hypothesis, (11.19) for L -
     L_b, Proposition 11.16 at I+ (11.159), and the leading iota+ term by (11.119a)-(11.119b), its logarithmically
     divergent part absent since u decays; the zero energy piece by Proposition 2.25 (1) and Proposition 10.6 (11.162),
     the parameter components vanishing; the tf expansion of sigma^-1 f-hat_2 removed term by term by Proposition 9.30,
     whose most singular output (11.165a) transforms to t*^(-lam+1)(log t*)^k h_b,s1(S-dot^(lam-1,k)_1) (11.167) -- zero
     below the hypothesis's order, new in the next eps_K window, a remainder above it -- and the conormal tf error by
     Proposition 9.35; the sub-leading zero energy piece (11.172); Proposition 9.35 again, [Hin26c] Proposition 13.18,
     (2.26a) and Proposition 2.25 (2) for (11.178). Part 2 removes each new term by S^(lam-1,k)_1 through the corrected
     equation (11.182), the map from the parameter to the total coefficient being the identity plus o(1); E~'_++ is
     built by (11.186). In the class, at n = 4: every term Part 1 uncovers below K+ order 1 + alpha_min is a
     centre-of-mass motion t*^(-lam+1)(log t*)^k h_b,s1(S-dot), S-dot in S_1, which has no G-fixed element (Proposition
     10.40 (ii)), so S-dot = 0 for G-invariant f, each coefficient being unique and so G-equivariant in f; the G-fixed
     pure gauge types of Proposition 10.42 (ii) first enter at K+ order alpha_min, so no gauge parameter is needed below
     it; the final parameters are the mass (10.43 (b)); the induction runs from 10.45 (c)'s base, K+ order in (1, 1 +
     eps_K), with one order of loss (10.45); and the inputs are (xlix)'s -- Propositions 11.14 and 11.16 at n = 4, the
     iota+ cap and E-sharp_+'s least elements (10.44 (d), 10.45 (d)), Proposition 2.25 on R^n, Proposition 10.6 with the
     mass alone, 10.24's roots, d mu_b = |dx|/|x|^4 -- the leading iota+ terms taken in increasing order, the radiative
     ones from 3/2 + (1 - e_Ups) gam_Ups before the mass's at 4. It rests on (xlix)'s readings, with Proposition 9.35 as
     in (l).

 (liv) 10.46 (b), [Hin26] Theorem 11.59 in the class (pp. 273-292; D161). His proof: Part 1 sharpens Proposition 11.51,
     allowing the later modification terms and recording the iota+ expansion (11.204) through Proposition 9.30 (2) and
     Proposition 2.25 (2); Part 2 extracts the t*^-1 (log t*)^k terms -- Proposition 11.16 at I+ (11.207), Proposition
     9.11 at lam = 1 for the leading iota+ term, whose pure gauge outputs (11.208) are kept, the zero energy pieces
     through the augmentation L~'_b of (10.41), Propositions 9.30 and 9.35 at tf, [Hin26c] Proposition 13.18 and the
     singular parts (10.38)-(10.39), giving (11.219) -- and removes them by the parameters (11.205) through (11.220),
     the map the identity plus o(1); Part 3 repeats this to K+ order 2 + eps_K, the terms of (9.39b) of order at most 2
     being pure gauge, and the logarithmic zf term of Remark 10.8 removed by S^(0),(2,0)_0; Part 4 records every term
     below K+ order 4 + eps_K -- (11.223) from Proposition 9.11, the polyhomogeneous terms of the tf inversions, the
     conormal ones of Proposition 9.35 and of L~'_b(sigma)^-1 -- which make u_exp (11.196b). In the class, at n = 4
     (10.46 (b)): the lists are the G-fixed ones of Proposition 10.42 (ii) -- S^(0)_0, S^(c0)_0 and S^(0)_2 eliminated
     at K+ order at most 2, the rest recorded below 3 + eps_K -- with one order of loss and the target 3 + eps_K for his
     4 + eps_K, so Parts 3-4 stop one order earlier; the v1, s1 and boost terms are absent, S_1, V_1 and so(4) having no
     G-fixed element (10.43 (b), Proposition 10.40 (ii)); no physical state enters below 3 + eps_K (10.46 (b)); and the
     inputs are (liii)'s. Whether the mass state's borderline decay, r^-2 in four space dimensions, brings Remark 10.8's
     sigma log |sigma| term at n = 4 is 10.35 (b)'s reading; if it does, S^(0),(2,0)_0, G-fixed, removes its t*^-2
     h^(0)_b,s0 as his. It rests on (liii)'s readings and 10.35 (b)'s.

 (lv) 10.61 (c), [Hin26] Proposition 11.51, Theorem 11.59 and Corollary 11.66 without the class (pp. 262-295; D161).
     (liii)'s and (liv)'s proofs without the class's restrictions, and Corollary 11.66's: Definition 11.63's
     augmentation #5 with q-vec (11.227a), Lemma 11.65 -- L_b h_b,rem(q-vec) of K+ order 4 + eps_K by (9.37), each t*
     derivative gaining an order -- and Theorem 11.59 rephrased through (11.231), with tame estimates. At n = 4 (10.61
     (c)): the centre-of-mass motions of Proposition 11.51 have S-dot^(lam-1,k)_1 in S_1 = R^4 (10.66 (g)); the lists of
     Theorem 11.59 are Proposition 10.46's -- six pure gauge classes eliminated at K+ order at most 2, fourteen
     recorded, the physical s2, v2 and t2 at -2 with T_2 added (10.34 (a), (c)) -- in place of (9.39b)'s at lam = 1 and
     his (11.196b), at the threshold 4 + eps_K, every recorded term's L_b-image of K+ order above 4 (Proposition 10.46),
     which is Lemma 11.65's (11.232); his rotations of the axis, V_1, are so(4)'s (10.36); the logarithmic time
     reparameterization (11.188) and the identities (11.187) and (11.189) are pure gauge identities free of n; Remark
     10.8's logarithm is 10.35 (b)'s question; and the inputs are (l)'s. It rests on (l)'s readings.

 (lvi) 10.67 (a), [Hin26c] section 7 (pp. 114-141; D163). His Proposition 7.1, under (7.3) -- alpha_I < -1/2 + p-bar_1,
     alpha_+ < alpha_I - 1/2 -- concatenates elliptic regularity and real principal type propagation (Propositions
     3.23-3.24) with five radial point estimates and one trapping estimate in the order of Proposition 4.24 (Figure 4.3;
     pp. 125-127): Step 1 reaches every finite t* through Proposition 7.9 with t*,+ = t*#; Step 2 the radial sets dR+H+
     and dR+I+,in,+, whose a priori terms are supported at finite t*; Step 3 dR+dK+,in, every backward bicharacteristic
     from its a priori region tending to dR+I+,in,+ or crossing t* = 1 (Lemma 4.6 (3)); Step 4 the trapped set, every
     backward bicharacteristic off Gamma-bar^u entering what Steps 1-3 control; Steps 5-6 dR+dK+,out and dR+I+,out; then
     into r > m. Each radial estimate is a positive commutator: a = a-check^2, a-check = rho_inf^(-s+1/2) times weights
     and the cutoffs (7.8), regularized as in Proposition 7.4, and H_G a + 2 p_sub a split as -delta rho_inf^-1
     a-check^2 - b^2 - ... + e^2 + j G, b real once its bracket is positive. At dR+H+ ((7.11)) rho_inf^-1 H_G rho_inf =
     rho^-2 mu'(r+), rho_K^-2 H_G rho_K < 0 and H_G q >= 2c (Lemma 4.9), the bracket positive for s_0 > 1/2 +
     vartheta_H+ ((7.10)). At dR+dK+,in and dR+dK+,out ((7.15)-(7.18), (4.15)) rho_K^-1 H_G rho_K = -/+2, rho_+^-1 H_G
     rho_+ = +/-2, H_G q >= 2q or <= -2q, and the bracket +/-(2(2s - 1) + 2(2 alpha_+ + 2) - 4 alpha_K) - delta - 2
     p_sub gives (7.13) and (7.17). At dR+I+,in,+ ((7.21), (4.67)) x_I^-1 H_G x_I = 1, rho_+^-1 H_G rho_+ = -2,
     rho_inf^-1 H_G rho_inf = 0 and H_G q >= q; the bracket is 4 alpha_I - 4 alpha_+ - 2 - delta, positive under (7.19),
     and p_sub = (Re p_1)(xi-hat - 2) (7.22), zero there, because (1/2) x_I^2 rho_+^2 (x_I d_x_I - 2)(x_I d_x_I - 2
     rho_+ d_rho_+) is symmetric for r^2 |dt* dr dg/| = 2 rho_+^-4 x_I^-6 |...| and Lap-slash's imaginary part lies in
     x_I^4 Diff^1(S^2). At dR+I+,out, with Lemma 5.16's t* and H_G t* >= 0, x_I^-1 H_G x_I = -1, H_G q <= -q and p_sub =
     -2 Re p_1; a fibre inner product with Re p_1 > p-bar_1 - delta' (Definition 5.18 (3)) makes the bracket at least -4
     alpha_I - 2 - delta + 4(p-bar_1 - delta'), positive under (7.23). Proposition 7.10 is [Hin21] Theorem 3.9, with
     (P.1)-(P.5) from section 4.2.3 and H_G sigma = 0, (P.6') from Proposition 6.3, and (7.25) from Definition 5.8.
     Proposition 7.11 repeats Proposition 7.1 with b-regularity. Lemma 7.12 commutes X_1 = nabla 2t* d_t*, X_2 =
     nabla(-2 r d_r), X_3-X_5 spanning V(S^2) and X_6 = I through P near I+; every commutator ((7.31), (7.37)-(7.39),
     Lap-slash a sum of X_a X_b) is sum_j Q_j X_j with Q_j in x_I Diff^1_eb, so P^(k) is P plus terms lower in order and
     in decay (7.33), and p-bar_1 is unchanged. Lemmas 7.15-7.16 and Proposition 7.17 commute d_r, elliptic at dR+H+,
     and t* d_t*, the commutator's symbol -i j rho^-2 mu'(r+) xi_0 ((7.48)) having the sign that leaves vartheta_H+
     unchanged. Lemmas 7.19-7.20 commute t* d_t*, rho_K X_1 being elliptic at dR+dK+,in/out ((7.59)). Lemma 7.21 and
     Proposition 7.22 commute t d_t at the trapped set to second order, against the trapping estimate's lost derivative.
     The tame bounds are Proposition 3.28's. At n = 4 (10.67 (a)): Proposition 4.24's order stands, the dynamics over K+
     being 10.19 (c)'s on five-dimensional Tangherlini, and over I+ and iota+ (2.27)'s and (4.67)'s, free of n (10.58
     (a)-(b)). At dR+H+ rho^-2 mu'(r+) is f'(r_h) = 2/r_h > 0 (10.18: rho^2/(2 (r+ - m)) is 1/f'(r+)), so Lemma 4.9
     holds with T*S^3, the threshold is s_0 > 1/2 + vartheta_H+ with 10.18's vartheta_H+, and (7.48)'s p#_alpha = j
     f'(r_h) >= 0. At dK+ and I+, (4.15), (4.67), (7.18) and (7.21) are functions of the Minkowski principal symbol in
     which S^3's |eta|^2 replaces S^2's (E1), so every value and bracket is his. In (7.22) the symmetric operator is
     (1/2) x_I^2 rho_+^2 (x_I d_x_I - 3)(x_I d_x_I - 2 rho_+ d_rho_+) (E1; 10.58 (a)'s (5.27) with 3/2 for 1) and the
     density r^3 |dt* dr dg/| = 2 rho_+^-5 x_I^-8 |d rho_+/rho_+ dx_I/x_I dg/|, for which that operator is symmetric as
     his is for 2 rho_+^-4 x_I^-6 (checked exactly here, the constant n - 2 failing); so p_sub = (Re p_1)(xi-hat - 2)
     with p_1 measured from 3/2 (10.58 (a)), and (7.19) and (7.23) are his. (7.13) and (7.17) are Definition 5.11
     (5)-(6)'s, stated in p_sub for the metric density and so free of n (10.58 (a)), and admissible order functions
     exist at every weight (10.18). Proposition 7.10's trapped set is 10.17 (ii)'s: {r^2 = 2 mu, xi = 0}, of codimension
     2 in the characteristic set, with xi, H_G xi and G independent and normal rate (2 mu)^(-1/2), the flow along it
     S^3's geodesic flow and so r-normally hyperbolic for every r. [Hin21] Theorem 3.9 (p. 36) is stated on the partial
     compactification (3.10) of R_t x X (p. 31), X a manifold of any dimension, its dynamical input, Theorem 2.6 (p.
     25), for R_t x X with X closed (p. 7); so (P.1)-(P.5) hold by 10.17 (ii) and H_G sigma = 0, (P.6') by Proposition
     6.3, which is that theorem after [Hin21] section 4's reduction (the proof of Theorem 4.3, p. 47), and (7.25) is
     Definition 5.8's hypothesis, which 10.17's deduced (a) meets at n = 4. Lemma 7.12 commutes the six rotation fields
     of S^3 (E3): X_3, ..., X_8, with X_9 = I and alpha in N_0^9 (E4). They commute with r d_r and t* d_t* as his do
     ((7.31)) and close under brackets (so(4)), and Lap-slash on S^3 is the sum of their squares (E3), so (7.38)-(7.39)
     hold with a, b, c in {3, ..., 8}; P' = -(X_2 - 2(3/2 + p_1)) X_1 + 2 x_I^2 Lap-slash + p_0 + P~' (E1), the constant
     3 commuting with every X_i, and X-vec_shift = (X_1 + 2, X_2 - 2, X_3, ..., X_9), the weight x_I^2 rho_+^2 being
     free of n (E1). Lemmas 7.15-7.21 use no angular field: d_r is elliptic at dR+H+, and t d_t at the trapped set,
     where 10.17 (ii)'s C = 4 mu sigma^2 > 0 makes sigma nonzero. Section 3's calculus is set on an n-dimensional
     manifold (p. 46), Lemma 3.27's H^3_b index being 3 at both n (E4). It rests on no reading: its inputs are E1-E4,
     10.17-10.18, 10.19 (c), 10.58 (a)-(b) and [Hin21]'s statements, read at source.

 (lvii) 10.67 (b), [Hin26c] section 8 (pp. 141-157; D163). His Lemma 8.1 (pp. 142-146): localize near I+ by the level
     sets of t*~ = t* + r^alpha, spacelike for alpha in (0, ell_I) by Lemma 5.16's computation ((8.6)-(8.8)); for P =
     box_g, the multiplier X = e^(-2 w t*) X_0, X_0 = x_I^(-4 alpha_I - 2)(-x_I d_x_I + d_t*) (8.9), future timelike,
     whose K-current (X)K = e^(-2 w t*)((X_0)K + 2 w T(X_0, -grad t*)) has (8.10); for general P, X = nabla^E X_0
     (8.20), the identity (8.13), the symbol H_G(X^mu zeta_mu) - (div X) G = 2 (X)K(zeta, zeta) ([Hin25a]
     (9.60)-(9.63)), P - P^* from (8.3) and the density 2 x_I^-6 |dt* dx_I/x_I dg/| ((8.14)), and (8.15)-(8.18); the
     d_t*^2 entry x_I^(-4 alpha_I)(-2 alpha_I - 1 + p_1 + p_1^*), positive for alpha_I < -1/2 + p-bar_1 - eps, and w
     large for the rest, give (8.19) with c_0 = (1/4)(-2 alpha_I - 1 + 2 p-bar_1); then (8.21) with its first- and
     zeroth-order corrections, Case II's boundary term T(X, -grad t*) of the good sign, and the zeroth order term by
     integrating in t*. Corollary 8.2 follows by smoothing and a weak limit. Proposition 8.3 extends P across r = m
     (Lemma 8.5: Seeley's extension in z = |x| - m, and P written in the monomials I, d_z^mu, d_z^mu d_z^nu, 0 <= mu <=
     nu <= 3, p. 148), then uses propagation of edge regularity, Proposition 7.9, duality, and for P^* the radial source
     estimate at dR+I+,out that he leaves to the reader, Proposition 7.9's computation with the signs reversed.
     Propositions 8.6 and 8.9 induct on k with Lemma 7.12's commuted equation, whose p-bar_1 is P's, Lemma 8.7's
     extension in (t*, x_I, omega in S^2), and Lemma 8.8, whose part (3) rests on Lemma 3.27's H^(0;3)_b. Section 8.2:
     Lemma 8.10 with X = e^(2 w r) rho_K^(-2 alpha_K) grad r, dr timelike for r <= r-natural (Lemma 5.16 (1)), positive
     through the 2 w T(grad r, grad r) term at every alpha_K, the zeroth order term by a divergence identity;
     Propositions 8.11-8.13 by elliptic and real principal type estimates, commuting X_1, ..., X_4 (V_1 = t* d_t*,
     V_(1+j) = d_x^j) and X_5 = I ((8.41)-(8.42)), with (8.44). Theorem 8.14 combines Propositions 8.6 and 8.9 on t* in
     [1, 4], Proposition 7.11 on {t* >= 3, r >= r_1^+} and Propositions 8.12-8.13 down to r = m. At n = 4 (10.67 (b)):
     (8.10) is E2's, its d_t*^2 coefficient -(2 alpha_I + 1) his, so the threshold alpha_I < -1/2 + p-bar_1 and c_0 are
     his; the cross term -3 d_t* (x)_s x_I d_x_I, his -2, and the angular term -(2 alpha_I + 3) x_I^2 gslash^-1, his
     -2(alpha_I + 1), are dominated, as his are, by 2 w T(X_0, -grad t*) = w x_I^(-4 alpha_I)((x_I d_x_I)^2 + x_I^2
     gslash^-1), his at both n, for w large (E2), so (8.19) holds. The density is 2 x_I^-8 |dt* dx_I/x_I dg/| (E4), for
     which x_I^2 (x_I d_x_I - 3) is skew as x_I^2 (x_I d_x_I - 2) is for x_I^-6, the adjoint of x_I d_x_I for x_I^(-2n)
     |dx_I/x_I| being -x_I d_x_I + 2n (checked exactly here, the constant n - 2 failing); so (8.14) reads as his with
     p_1 measured from 3/2 (E1; 10.58 (a)). (8.13), (8.15)-(8.18), (8.21), [Hin25a]'s symbol identity and the boundary
     terms hold in every dimension, and the localization (8.6) is the Minkowski algebra of (2.25)-(2.27) with the
     class's weights (10.58 (a)). The extension across the inner sphere, his r = m, runs on R^4 with I, five first-order
     and fifteen second-order monomials (0 <= mu <= nu <= 4; E4), Seeley's construction acting in the one variable z; dr
     is timelike inside r_h on five-dimensional Tangherlini, g^-1(dr, dr) = f < 0 (10.19 (c)), so Lemma 5.16 (1)'s
     r-natural lies between that sphere and r_h. Propositions 8.6 and 8.9 commute (lvi)'s nine operators (E4), p-bar_1
     unchanged; Lemma 8.7's extension is in omega in S^3; Lemma 8.8's index 3 is Lemma 3.27's, the least integer above
     (n + 1)/2 at both n (E4); section 8.2 commutes X_1, ..., X_5 (V_(1+j) = d_x^j, j = 1, ..., 4) and X_6 = I, alpha in
     N_0^6 (E4), Lemma 2.11's commutator identities being free of n; and Theorem 8.14 combines these with (lvi)'s
     Proposition 7.11. It rests on no reading: its inputs are (lvi)'s, E1-E4, 10.19 (c) and 10.58 (a).

 (lviii) 10.19 (d), [Hin26c] Theorem 9.5 (pp. 161-174) and Theorem 9.16 (pp. 174-175) at n = 4 (D164). Theorem 9.5's
     proof (section 9.2.3): parts (1)-(2) concatenate Propositions 9.9 (the horizon), 9.10 (R_sigma,in) and 9.11 (R_out)
     with real principal type propagation, then a standard energy estimate ([Hin25a] Corollary 9.38) down to r = m.
     Proposition 9.9's positive commutator ((9.26)-(9.29)) uses (9.24)'s structure -- beta_0 = rho_inf^-1 (rho_inf H_G)
     rho_inf > 0, beta > 0, and q with rho_inf H_G q >= c q -- the bracket being 2 beta_0 times s - 1/2 - beta_0^-1
     p_1(0) - beta_0^-1 (p_1(sigma) - p_1(0)), with p_1(sigma) - p_1(0) = -(Im sigma)(rho_inf H_G0 t) from (9.30).
     Proposition 9.11's ((9.46)-(9.52)): q = xi_sc^2 + |eta_sc|^2 with H q <= -2q (9.48), Re P-hat_0(0) a sum of squares
     to leading order (9.49), rho^-1 H rho = -2 at R_out and the bracket -4r - 2 + 4 Re S > 0, that is r < -1/2 + S-bar,
     the Im sigma term (9.52) of the main term's sign, and (9.44) by induction on k with Lemma 9.13's commuted equation,
     whose extra term -2 k i sigma rho has that sign too. Part (4) is (9.53) away from R_out and (9.44) at it. Part (6)
     is (9.56)-(9.57) with the weak-limit continuity argument ([Vas13] section 2.7). Parts (3) and (5) are (xlviii)'s,
     Proposition 9.10 is (xlvii)'s, and Theorem 9.16 is (lix)'s. At n = 4 (10.19 (d)): (9.24) is the five-dimensional
     horizon's -- beta_0 = f'(r_h) = 2/r_h in (7.11)'s normalization and q Lemma 4.9's with T*S^3 (10.18; (lvi)), beta_1
     = vartheta_H+ (10.18 (a)) -- so Proposition 9.9's threshold s_0 > 1/2 - beta Im sigma + beta_1 is (9.16a).
     Proposition 9.11 is written for Definition 9.4's operator, with eta_sc in T*S^3 and S^3's Laplacian in (9.49), and
     its threshold -1/2 + S-bar, on the Euclidean density, is 10.18 (b)'s. Lemma 9.13 is printed for fields spanning
     V(S^(n-1)). (9.56) reads 2 i sigma rho(rho d_rho - 3/2 - S) - i sigma Q + 2 sigma^2 g_00, still in rho Diff^1_b
     (10.18 (b)), so (9.57) stands. The energy estimate needs dr timelike inside r_h (10.19 (c)), and the dynamics
     ordering the concatenation are 10.19 (c)'s. The kernel class at S-bar = 0 is A^(3/2 - eps) for his A^(1 - eps)
     ((xlviii)). It rests on the reading that his scalar estimates hold for operators on bundles (his p. 158; 10.53
     (d)), and on the uniformity of these estimates under small perturbations of the operator, which 10.19 (d) uses for
     [Hin26] Propositions 6.5 and 6.9: his Remark 7.2 states it for section 7, by the openness of each symbolic
     positivity, and it is taken here for section 9.

 (lix) 10.53 (e), [Hin26c] section 9.3, Theorem 9.16's proof (pp. 174-193; D164). His proof (section 9.3.6) concatenates
     real principal type propagation in three regimes of z -- Propositions 9.19 (|Im z| = O(h), standard), 9.22 (h << Im
     z << 1) and 9.23 (Im z >~ 1), positive commutators in which h^-1 Im P_h,z = -h^-1 Im(z) Q~_1,z,h (Lemma 9.21,
     (9.68)) has the main term's sign, Q_1,h's symbol 2 g^-1(-(Re z) dt + xi, dt) being positive on the future
     characteristic set (Lemma 9.20) -- with Proposition 9.25 at the horizon, Proposition 9.9's computation localized
     also at fiber infinity, (9.72) borrowing positivity from Q~_1,z,h when Im z/h is large; Propositions 9.26 and 9.27
     at R_(+-1,in) and R_out, Propositions 9.10's and 9.11's computations with the cutoff psi_d's terms -b_d^2 and e_d^2
     (rho^-1 H rho = 2 at R_in, -2 at R_out), Q_1,h's symbol 4 > 0 at R_in, g^00 <= 0, and (9.77) from Lemma 9.13's
     commuted equation; Theorem 9.28 at the trapped set under (Gamma.1)-(Gamma.4) -- the lossless estimate for Im(h^-1
     z) > gamma_+ by a commutator in phi_u, phi_s with Q_1,h's lower bound 2 beta_0 ((9.84b)), the estimate with loss 1
     by semiclassical defect measures (Lemmas 9.30-9.32 and Steps 1-4, after [Dya16]), and the loss delta_Gamma by
     complex absorption Q_3, Lemma 9.33's three-line interpolation and [HV16] Theorem 4.7's conversion ((9.99)-(9.101));
     and Proposition 9.35's energy estimate near r = m, X = grad r with dr future timelike on [r_-, r_+] and the
     K-current bound (9.106) for large Im z/h. Proposition 4.24's dynamics, through section 9.1.2, order the
     concatenation. Part (3) follows from (9.59)'s injectivity, part (4) from Remark 9.14 away from R_out and (9.77) at
     it, and part (5) from (9.60) through (9.56)-(9.57). At n = 4 (10.53 (e)): sections 9.3.1, 9.3.4 and 9.3.5 are
     written for a general stationary wave operator on R_t x X (Definition 9.3, X n-dimensional), and Lemmas 9.20-9.21
     and 9.30-9.33 and Propositions 9.19, 9.22, 9.23 and 9.35 are dimension-free as printed, Q_3's kernel normalization
     (2 pi)^(-n-1) included. Section 9.3.3 is written for Definition 9.4's operator, with (9.73)'s (n - 1)/2; its
     covectors eta_sc,h in T*S^2 are in T*S^3, and its radial sets, rho^-1 H rho = +-2 and Q_1,h's 4 are Minkowski's in
     (t, r) (10.58 (a)). Proposition 9.25's beta, beta_1 and q are the five-dimensional horizon's (10.18: f'(r_h) =
     2/r_h, vartheta_H+); Propositions 9.26 and 9.27 carry (xlvii)'s vartheta_in = -2 S-bar and 10.18 (b)'s -1/2 +
     S-bar; Theorem 9.28's hypotheses (Gamma.1)-(Gamma.4) and its loss are 10.19 (b)'s, gamma_+ = (2 eta)^(1/2)/4 and
     delta_Gamma(0) = (mu eta)^(1/2); Proposition 9.35's hypothesis is dr future timelike inside r_h on Tangherlini
     (10.19 (c)); and Proposition 4.24's role is taken by 10.19 (c)'s classification. 10.53 (e)'s second sentence,
     Definition 5.18 and Theorems 10.1 and 11.1 at n = 4, is 10.58 (c)'s, still on the census. It rests on the reading
     that his scalar estimates hold for operators on bundles (10.53 (d)), his section 9 leaving that step to the reader.

 (lx) 10.58 (c), [Hin26c] Definitions 5.13, 5.15 and 5.18 (pp. 106-109), Theorem 10.1 (pp. 201-227), Theorem 11.1
     (pp. 228-233), Corollary 13.17 and Proposition 13.18 (pp. 247-255) at n = 4 (D166). The definitions: Definition
     5.13 asks trapping admissibility (Definition 5.8), tf-admissibility with weight alpha_sf + 3/2, n/2 = 2 at n =
     4 (Proposition 10.57 (N5)), and (5.22)'s bound, whose weights alpha_sf + 2 and alpha_sf - delta are the
     operator's order and the loss, free of n; Definition 5.15's class x_I^-2 rho_+^-2 C^((d_0;k),(2 l_I, l_+, l_K))
     weighs the metric's coefficients, free of n, and Tangherlini's mass term m/r^2 is x_I^2 rho_+ times Kerr's m/r,
     so Remark 5.17's membership holds a fortiori; Definition 5.18's (5.23)-(5.26) are free of n, and its (5.27)
     reads -(x_I d_x_I - 2(3/2 + p_1))(x_I d_x_I - 2 rho_+ d_rho_+) (10.58 (a)), with characteristic exponents 3 + 2
     mu. Theorem 10.1's hypotheses (10.2)-(10.3), alpha_I < -1/2 + S-bar and alpha_+ < alpha_I - 1/2, are in the
     metric density and free of n; in section 10.1's b-densities they are gam_I < c + S-bar and gam_+ < gam_I, gam_I
     = alpha_I + n/2 and gam_+ = alpha_+ + (n + 1)/2, c = (n - 1)/2 (N5). His proof, section by section.
     10.1.1-10.1.2 (Proposition 10.6 (2)): N^0 of (10.6)-(10.7) with c = 3/2 (N1), elliptic, its principal symbol
     (10.21) free of n but for |eta|^2 on T*S^3, so the radial sets (10.18) and the flow are his. Step 1's radial
     point estimates: at R_I+,+1,in Q_0 = -x_I^2 (4 + 2 Re S) and the symbol of h Im's first-order term x_I^2 (5/2 +
     Re S) xi, summing to x_I^2 at xi = 2 as his do, so the total -4(gam_I + h^-1 Im z) and Im sigma > -gam_I are
     his (N2-N3); at R_I+,out gam_I < 3/2 + Re S (N4); at R_cf,+1,in the density R^4 |dR/R| gives the correction -4
     hhat xi and sigma(Q_0,h) = -hhat (4 + 2 Re S), and with gam_cf = -(alpha_+ + 2) the threshold is (10.28)
     unchanged (N5-N6) -- his sum omits the Re S that sigma(Q_0,h) carries, which enters alike at n = 3 and n = 4;
     at R_cf,out the total is 4b + 4 alpha_+ + 2 - 4 Re S, negative iff b + alpha_+ < -1/2 + Re S, his threshold,
     his printed '+ 4 Re S' a misprint by that threshold (N7); the real principal type estimates and the large Im z
     arguments are free of n. Step 2 passes to the Euclidean density Rhat^4 |dRhat/Rhat dgslash| and applies
     Corollary 9.39 with n = 4 and q = gam_cf + 2 = -alpha_+, the weights returning to (gam_cf - 2, b - gam_cf + 1)
     as his (N9), the tf-normal operator being N_tf(P_0, z) at n = 4. Step 3 commutes Lemma 10.7's V = (R d_R, the
     six rotation fields of S^3, I) for his five entries (N9), V_shift = (V_1 + 2, ...) free of n, with Lemma 7.12's
     commuted structure ((lvi)). 10.1.3 (Proposition 10.6 (1)): Lemma 10.9's 0-normal operator has indicial roots 2i
     sigma and 2(3/2 + S), the invertibility of N-hat' is a positivity argument free of n, and the left parametrix
     is Hintz's in the 0-calculus ([Hin26c]'s [Hin23a], arXiv:2112.08130, Theorem 1.5, stated for an n-dimensional
     manifold with boundary, p. 1: READ), its right b-density shift dim(iota+) - 1 = 3 for his 2 and alpha_lb =
     2(3/2 + S-bar) - eps (N9). Lemma 10.10 forms N^1 and its Fourier transform (10.40) with i sigma - 5/2 - S for
     his i sigma - 2 - S, the shifts by 1 being the one-dimensional transform's in v, and w-flat = rhat^(1 - i
     sigma) w solves N_tf(P_0, +-1) (N8); w-flat lies in A^(alpha, -beta) with beta in (beta_-, beta_+), since
     -gam_cf = alpha_+ + 2 is in that gap and Im sigma > -1 - beta_+ (his '1 + Im sigma < beta_+' is -1 - Im sigma <
     beta_+), so tf-admissibility at n = 4 gives w-flat = 0. 10.1.4 (Proposition 10.12): the Mellin transform in
     tau, the contour Im sigma = -gam_+, a Paley-Wiener argument in one variable and finite speed of propagation for
     uniqueness, free of n, with gam_I = alpha_I + 2 for his alpha_I + 3/2 (p. 219). Section 10.2 (Proposition
     10.14): P_+ = chi N_iota+(P_0) + (1 - chi) P_0, its metric g_chi with dt* past causal, Tangherlini's g - g-bar
     = O(m r^-2) one order better at iota+ than Kerr's, the estimates section 7's ((lvi)) and the normal operator's
     inversion Proposition 10.12's. Section 10.3 combines them with the shifts n/2 = 2 and (n + 1)/2 = 5/2 for his
     3/2 and 2 (N5), gam_+ - 1/2 = alpha_+ + 2 in (beta_-, beta_+) (Definition 5.13 (2) at n = 4), footnote 100's
     buffer 1/2 free of n -- Sobolev embedding in n spatial variables gives n/2 = 2 orders, alpha_+ + 2 pointwise
     and alpha_+ + 5/2 with t* regularity -- and (5.22) near K+. Theorem 11.1's proof (pp. 229-232): P_eps = chi_eps
     P_0 + (1 - chi_eps) P, Theorem 8.14's estimates (8.45)-(8.46) ((lvii)), Theorem 10.1 for P_0, the absorption
     with delta' = min(l_+ - delta, l_K - aleph), Propositions 8.6 and 8.9 at finite times, weak compactness, the
     passage from (e3b; b)- to b-spaces and continuous dependence: free of n. Its b-density form (11.4)-(11.6a) has
     mu_b = rho_I^4 rho_+^5 rho_K |dt dx| = |dt dx|/(t* r^4), beta_I = alpha_I + 2, beta_+ = alpha_+ + 5/2, beta_I <
     3/2 + S-bar and P_1 of sf-weight beta_+ - 5/2 (N5); Remark 11.4's condition is beta_- < 1 + S-bar for his 1/2 +
     S-bar (N9). Section 13.2: mu_b = |dx|/|x|^4 and L^2(mu) = rho^2 L^2(mu_b) (N5), so Lemma 13.13's
     (13.23a)-(13.23b) carry 3 and 2 for his 5/2 and 3/2, (13.26) beta - 2, and Corollary 13.14, through Theorem 9.5
     ((lviii)), beta_scf < 3/2 + S-bar; Corollary 13.17 joins Propositions 13.9 (2) and 13.11 (2), the Fourier
     transform in t* and free of n, with Proposition 13.16, through Theorem 9.16 ((lix)), so gam = min(beta_I, 3/2 +
     S-bar) for his 1 + S-bar; Proposition 13.18 is Corollary 13.14's proof with sigma d_sigma, on Theorem 9.41,
     tf-admissibility with weight alpha + 2, beta_scf < 3/2 + S-bar, (13.30a)'s alpha_+ + 3 and alpha_tf + 4 for his
     5/2 and 7/2 and (13.30b)'s 2 for his 3/2, beta_tf - beta_zf in (beta_-, beta_+) free of n. It rests on
     (lvi)-(lix)'s readings, Theorems 8.14, 9.5 and 9.16 at n = 4, and on Corollary 9.39 and Theorem 9.41 at n = 4
     (10.20's reading); its own places are computed (Proposition 10.57).

 (lxi) 10.22 (e), [Hin26a] Theorem 5.2 (pp. 41-66; D167). His proof, section 5.2. Lemma 5.3 puts h^2 box_g in h^2
     rho_sf^2 Diff^2_3b and L in h rho_sf^2 Diff^1_3b ((5.17)), from (2.14) and c in rho_sf C^oo, and Lemma 5.4 makes
     the characteristic set of rho_sf^-2 P_h dSigma u o by Lemma 3.7. Section 5.2.1: Proposition 5.5, elliptic estimates
     off o u dSigma; Proposition 5.6 at fibre infinity, a pairing argument ((5.24)-(5.30)) in which Re L_h is positive
     by Lemma 3.5 and the commutator (5.29) is symbolic, using only that d tau and dr are timelike where the cut-offs
     (5.20) vary. Near o, the elliptic multiple (5.31)-(5.32), C from Corollary 3.6, and positive commutators at the
     three critical sets of -r c#: Proposition 5.8 at r = r_0 in (K+)^o (section 5.2.2), whose symbol identity
     (5.39)-(5.43) needs S positive definite (Proposition 5.1 (3)) and -l(+-dr) positive on supp psi' (Proposition 5.1
     (6)), j = sigma(J) vanishing cubically at o, then the absorptions (5.44)-(5.47) and an iteration in h^(1/2);
     Proposition 5.9 at dK+ (section 5.2.3), with w = rho_sf^(alpha_sf + 1) rho_K^(alpha_K) in (5.53)-(5.54), b_0's
     square root from Proposition 5.1 (4) and b_sf's and e's from (6); Proposition 5.11 at the sink (section 5.2.4),
     with w' = rho_sf^(alpha_sf + 1) in (5.57), b_0's from Proposition 5.1 (5), e_1's from (6) and e_2's from the sign
     of -r^2 l(d(r/t)); and Proposition 5.12 with the propagations after it (section 5.2.5), the escape functions r and
     r/t and Proposition 5.1 (6). Section 5.2.6: Proposition 5.16's energy estimates near X and Sigma#, from Lemma 5.14
     and Corollary 5.15 with the multiplier a^2 L_h ((5.70)-(5.71)), the weights of (5.72)-(5.73), and the fundamental
     theorem of calculus for L_h ((5.77)-(5.78)). Section 5.2.7: Proposition 5.17's a priori estimate along the flow of
     -r c#, the adjoint estimate (5.81) the other way, duality for solvability, extension and restriction for
     regularity, and the initial value problem by short-time theory or by cutting off at tau = 0, the source then in
     H^(s'-1) for s' - 1 < -3/2, a differentiated delta in one variable. At n = 4: Lemma 5.3 is 10.22 (a) (Proposition
     10.19 (i)); Lemmas 3.5 and 3.7 and Corollary 3.6 hold (10.13 (i)); Proposition 5.1 (1)-(6) are 10.14's c at (v, e)
     = (1/2, 1/102400) and r_0 = 100, (3) and (6) computed there, (4)-(5) positive at dK+ and at the sink exactly when
     b_K > b_sf - b* and b_sf < b* (10.14 (iv)), near those sets by continuity as in his proof (p. 39), and (5) on |r/(t
     v) - 1| <= 2 delta_sf (10.22 (c)), so his (5.14) reads alpha_sf < b* - 1 and alpha_K > alpha_sf + 1 - b*; each
     commutator above is an identity of symbols free of n whose signs are these (10.65 (b)); the pairings are in L^2(M,
     |dg|), with |dg| = r^3 |dt dr dgslash| on five-dimensional Tangherlini, Kerr-Schild metrics having eta's
     determinant, and S = h^-1 Im L_h is formed with it (10.13); the causal facts Propositions 5.6 and 5.16 use -- d tau
     past timelike on tau^-1([0, T]) for every T < 1, dr future timelike inside r_h, m = r_h/2 -- are Proposition 10.19
     (ii)-(iii) (10.22 (d)); Lemma 5.14 is stated for a Lorentzian vector space and Corollary 5.15 on R^(1+n) and on
     n-dimensional manifolds of bounded geometry, here n = 4 with charts on S^3 times dyadic intervals, its uniformity
     10.22 (d)'s; the level-set density in (5.74) is r^4 |dr dgslash| for his r^3, |dt dr| being r |d tau dr|, and the
     data space of (5.16) is rho_sf^(alpha_sf + 1/2) H-bar_b(X, r^3 |dr dgslash|) = rho_sf^(alpha_sf) H-bar_b(X, r^4 dr
     |dgslash|), the shift 1/2 free of n; and the semiclassical 3b-calculus is constructed in every dimension (10.65
     (a), READ). So every place where five dimensions enter is computed or READ, and his h_0 exists at n = 4 as at n =
     3, not made explicit; it rests on no reading, and 10.56 (a)'s, already discharged at source in 10.65, is here
     written out.

So all of 10.74's 61 rows are written out at n = 4 and rest on their inputs, not on a census of their sources;
B-MAP.tsv's column `written` marks them. Thirty-nine of the sixty-one take a reading among their inputs (B-MAP.tsv's
column `reading`: 10.15 (a), 10.15 (b), 10.19 (a), 10.19 (d), 10.20 (a), 10.23 (b), 10.23 (d), 10.27 (b), 10.28 (a),
10.29 (a), 10.30 (a), 10.31 (a), 10.32 (c), 10.34 (c), 10.36 (b), 10.37 (c), 10.39 (d), 10.39 (e), 10.41 (b), 10.42 (e),
10.43 (c), 10.45 (b), 10.45 (e), 10.46 (a), 10.46 (b), 10.46 (e), 10.47 (d), 10.47 (e), 10.49 (a), 10.53 (e), 10.55 (b),
10.56 (b), 10.58 (c), 10.61 (b), 10.61 (c), 10.62 (b), 10.62 (c), 10.62 (d), 10.40 (a)), and rest on that reading
through that input, not through their own steps (the sixty-first verifier; D149). Two, (iii) and (xxvi), replace the
source proof by a computation rather than carry it. No row is left on the census; what remains of 8.8 is the readings
those thirty-nine take.

Labels: READ (the sixty-one source proofs); deduced (the matching); nothing computed or proved here, Lemma 10.56,
which (i) uses, being proved in 10.76.

### 10.76 Across the horizon: the continuation and the interior uniqueness (D149)

*The setting.* [Hin26]'s kernel arguments at nonzero frequency end with a mode stability statement on all of X, which
reaches inside the horizon to r_in < r_h. At n = 4 their inputs are computed on r > r_h: 10.27 (a), in place of [AHW24]
Theorem 6.1 (1), writes a mode as u = delta-hat*(sigma) omega there, and Proposition 6.12 (10.20 (e)) then needs omega
on X. 10.27 (b) left omega's continuation inside the horizon OPEN, 10.55 (c) deduced the interior uniqueness from the
regular singular point at r_h without a bound, and 10.75 (i) used both (the sixty-first verifier). Both follow from one
lemma on linear ordinary differential equations whose leading coefficient has a simple zero.

**Lemma 10.56 (proved).** Let delta > 0, I = (-delta, delta) and A in C^oo(I; C^(N x N)), and consider z X'(z) = A(z)
X(z).
 (a) A solution on (0, delta) with |X(z)| <= C_K z^K for every K vanishes there; likewise on (-delta, 0).
 (b) A solution on (0, delta) that extends smoothly to [0, delta) is the restriction of a smooth solution on I.
 (c) Let f, Q, R be smooth on I, f scalar with f(0) = 0 != f'(0) and f != 0 on I \ {0}, and Q, R N x N. For f phi'' + Q
     phi' + R phi = 0, a solution on one side of 0 that is flat at 0 -- it and its derivative O(|z|^K) for every K --
     vanishes there, and one that is smooth up to 0 from one side is the restriction of a smooth solution on I.

*Proof.* (a) Let M := max ||A|| on [-delta/2, delta/2]. If X(z_1) != 0 for some z_1 in (0, delta/2], X has no zero on
(0, z_1] (uniqueness for the equation, regular away from 0), and there d/dz log |X|^2 = 2 Re <X, A X>/(z |X|^2) <= 2
M/z, so |X(z)|^2 >= |X(z_1)|^2 (z/z_1)^(2M) for 0 < z <= z_1; with K > M this contradicts |X(z)| <= C_K z^K as z -> 0.
So X = 0 on (0, delta/2], and then on (0, delta). On (-delta, 0), Y(s) := X(-s) solves s Y'(s) = A(-s) Y(s), of the same
form. (b) By Borel's lemma there is B in C^oo(I) with the Taylor series of X at 0; Y := X on [0, delta) and B on
(-delta, 0) is smooth on I, all one-sided derivatives agreeing at 0. E := z Y' - A Y is smooth and vanishes on [0,
delta), so it is flat at 0. On (-delta/2, 0) let Phi solve z Phi' = A Phi with Phi(-delta/2) = 1; Phi^-1 solves z
(Phi^-1)' = -Phi^-1 A, and the estimate of (a), now |d/ds log |Y|^2| <= 2 M/s for s = -z, gives ||Phi(z)||,
||Phi(z)^-1|| <= C |z|^-M. Set W(z) := -Phi(z) int_0^z Phi(s)^-1 E(s) ds/s: the integral converges, E/s being flat, W =
O(|z|^K) for every K, and z W' = A W - E on (-delta/2, 0). Continue W to (-delta, 0) by the regular equation and by 0 to
[0, delta). Differentiating, z W^(j+1) = (A W - E)^(j) - j W^(j), so by induction on j every derivative is O(|z|^K) for
every K as z -> 0-, and W is smooth on I. Then Y + W is smooth, solves z (Y + W)' = A Y + E + A W - E = A (Y + W) on I \
{0} and so on I, and equals X on [0, delta). (c) h := f/z is smooth and nonzero on I. With X := (phi, z phi') the
equation is z X' = A X with A = [[0, 1], [-z R/h, 1 - Q/h]], smooth; phi flat, or smooth up to 0, makes X so; and the
first component phi of a solution X, which has X_2 = z phi' by the first row, solves f phi'' + Q phi' + R phi = 0 on I \
{0} by the second, and so on I. []

*Deduced (at proof level, given the inputs named).*

 (a) (the radial systems) Every operator of the record on Tangherlini -- box^Ups, box^C, L and their spectral families
     -- is stationary, SO(4)-invariant and of wave type, its principal part g^-1(xi, xi) times the identity (10.55 (c)).
     In the coordinates (t*, r, y) of X, regular across the horizon, its spectral family at sigma maps the span of each
     harmonic (of a type and a degree) to itself, and on the vector phi(r) of a field's coefficients in a basis of that
     span smooth in r > 0 it is f phi'' + Q phi' + R phi: the coefficient of phi'' is a nonzero constant times g^-1(dr,
     dr) = f = 1 - mu/r^2 (-f for box^Ups and box^C, -f/2 for L in [Hin26]'s sign convention, (4.12)-(4.13); the
     sixty-second verifier), the cross term and the angular derivatives entering Q and R, both smooth on [r_in, oo). f
     vanishes at r_h, simply (f'(r_h) = 2 mu/r_h^3), and nowhere else on [r_in, oo), 0 < r_in < r_h. So Lemma 10.56 (c)
     applies at r_h, and on [r_in, r_h) and (r_h, oo) the systems are regular.
 (b) (the interior uniqueness) A kernel element on X that vanishes for r > r_h vanishes on X: its coefficients in each
     harmonic are smooth on X (it lies in A^alpha(X)) and so vanish to infinite order at r_h from inside; by (a) and
     Lemma 10.56 (c) they vanish near r_h, and on [r_in, r_h) by uniqueness for the regular system; so every harmonic
     component vanishes, and the element is 0. This is 10.55 (c) with its last step proved, and the interior of 10.15
     (a).
 (c) (the continuation; [Hin26] Proposition 8.8 at n = 4) Let u be in the kernel of L-hat(sigma), sigma != 0, Im sigma
     >= 0, and fix a harmonic. On r > r_h, u = delta-hat*(sigma) omega (10.27 (a)), and box^Ups(sigma) omega = 2 eta = 0
     (10.75 (i) (6)). omega is smooth up to r_h: the components (delta* omega)_(r nu) = (1/2)(d_r omega_nu + d_nu
     omega_r) - Gamma^lam_(r nu) omega_lam, nu = t*, r and the angular ones, with d_t* = -i sigma and the angular
     derivatives acting on the harmonic, give d_r omega = M(r) omega + N(r) (u_(r nu))_nu with M, N smooth on [r_in, oo)
     in the regular chart, a regular linear system of which omega is the solution on (r_h, oo); so omega extends
     smoothly across r_h. By (a) and Lemma 10.56 (c), omega on r >= r_h is the restriction of a smooth solution of
     box^Ups(sigma) omega~ = 0 near r_h, continued to [r_in, r_h) by the regular system. omega~ lies in A^alpha'(X;
     T*X), being omega near infinity, so Proposition 6.12 (10.20 (e)) gives omega~ = 0; then u = delta* omega = 0 on r >
     r_h, and u = 0 on X by (b). Each harmonic is treated alone, and u, all of whose harmonic components vanish, is 0.
     At sigma = 0 the same argument serves his Proposition 8.11's omega in ker box^Ups(0) (10.32 (c), 10.33): there the
     first-order system's source is (u - g-dot^Ups(b-dot))_(r nu), and the Killing and s1 states are subtracted before
     Proposition 6.12 applies, as his proof does; Lemma 10.56 asks nothing of sigma.

What this closes: omega's continuation inside the horizon (10.27 (b), 10.33) and the interior uniqueness (10.15 (a),
10.16, 10.55 (c)), OPEN or deduced without a bound before. What it does not: the kernel elements' class (10.55 (b), on
10.53 (c)'s reading) and Proposition 6.12 at n = 4 (10.20 (e), on the readings of 10.19-10.20) stay as they were.

Labels: proved (Lemma 10.56); deduced at proof level ((a)-(c)), given the inputs named; nothing computed here.

## 11. Theorem M: the Bondi mass at past null infinity (D37)

**Status. Theorem M is deduced here, with its exact inputs computed in `bondi5.py` B1-B4, and was read by a twelfth
verifier (D40): no major finding; its five minor findings are repaired in place (Lemma 11.0; Lemma 11.2's hypothesis
(H_m) and the induction in m at J = 3; Proposition 11.2(i) rebuilt by characteristics; B1's orders below s^3,
Proposition 11.3(0); the coefficient of G_k) and its four notes seated (the J = 3 source, the areal coefficient 6 rho_k,
the orders of R_rr, the wording on derivatives). Proved means proved: the deduction rests on Theorem P and the computed
B1-B3, and a thirteenth read the repairs (D44): Lemma 11.0's identity had been run on a region unbounded toward past
null infinity, where the flux at the orders above Theorem P's is not known to vanish -- a major gap, repaired by running
it on the approximating solutions g_n of Proposition 9.8 and passing to the limit -- with three minor findings in
Proposition 11.2 and Theorem M(a), repaired; the repairs of D44 have not themselves been read.** It closes the first of
the three items section 10 and the paper's section 8 left open: a mass law at past null infinity in five dimensions, and
its application to g_lam. The law itself is published (Tanabe, Tanahashi and Shiromizu, READ in 11.3) and is recomputed
here in the class with every coefficient from s^1 general (B1); what is new is that g_lam has the asymptotic expansion
at past null infinity the law needs, in Bondi coordinates built on g_lam, and what the law then gives.

**Theorem M.** Let g_lam be Theorem P's solution, 0 < lam <= lam_P, on P. (a) On a far region P cap {t >= T_M},
T_M = T_M(lam), there are Bondi coordinates (v_B, r_B, th_B, phi1, phi2): v_B is null for g_lam with v_B - v -> 0 at
past null infinity along every generator of g0, th_B is constant along the generators of {v_B = const}, r_B is the
areal radius of the spheres {v_B, r_B = const}, and

    g_lam = -e^{2 b} W dv_B^2 + 2 e^{2 b} dv_B dr_B
            + r_B^2 [ e^{-2 (P1 + P2)} (dth_B - U dv_B)^2 + cos^2 th_B e^{2 P1} dphi1^2 + sin^2 th_B e^{2 P2} dphi2^2 ]
                                                                                                              (11.1)

(hf_mirror5's form, the numerical solver's own), with P1, P2, b, U and W - 1 admitting expansions in s := r_B^(-1/2),

    f = sum_{k=1}^{6} s^k f_k(v_B, th_B) + o(s^6),

whose coefficients are smooth, bounded with all derivatives, T^2 x Z2 x Z2 invariant and zero for v_B <= v_start, and
whose remainders have every (v_B, th_B)-derivative o(s^6) and gain an order -- one power of r_B, two of s -- under each
r_B-derivative.
(b) P_i = s^3 p_i + s^5 (...) + ...: the s^3 coefficients are the record's free data at phase v_B/lam,
p_1 = (2 c^2 G - s^2 F)/3, p_2 = (2 s^2 F - c^2 G)/3, F = lam A env(v_B) h sin(v_B/lam), G = lam A env(v_B) h
cos(v_B/lam) (c = cos th_B, s = sin th_B; the radiation field of (P-ii)), and the s^4 coefficients vanish.
(c) W = 1 + s^3 V1 - s^4 M + ..., V1 a divergence on S^3, and the mass aspect M(v_B, th_B) satisfies, pointwise,

    d_v M = (4/3) (p1_v^2 + p1_v p2_v + p2_v^2),                                                             (11.2)

with M = mu0 for v_B <= v_start; so the Bondi mass mu_B(v) := <M(v, .)> (the mean over S^3) obeys mu_B' = (9.10)
exactly:

    mu_B(v) = mu(v) + (2/9) lam^2 A^2 int_{-oo}^{v} env'^2 + (2/9) A^2 ((lam/4) env^2 cos(2v/lam)
              + (lam^2/4) env env' sin(2v/lam)) + O(lam^3),                                                  (11.3)

and after the shell mu_B = mu(v_end) + (2/9) lam^2 A^2 int env'^2 + O(lam^3) (P7).
(d) The Hawking mass M[S] of section 8 of the Bondi spheres S = {v_B, r_B = const} tends to mu_B(v_B) as r_B -> oo
(B3).

So the record's mean mass at past null infinity -- the sphere mean of the Bondi mass aspect, the quantity the
numerical solver integrates -- is, for g_lam, mu(v) + O(lam) while the shell passes and mu + (2/9) lam^2 A^2 int
env'^2 + O(lam^3) after it, with this coefficient: the O(lam^2) rate of the paper's section 6, now proved for g_lam. The
proof is in 11.1-11.3; 11.4 compares with the numerics.

### 11.1 The expansion of g_lam at past null infinity

Throughout, lam is fixed, and every constant may depend on it. On the far region P cap {t >= T}, T = lam^-2 (section
9.4), Theorem P gives u := g_lam - g0 = lam [W_TT] + u_1 with, by (P-ii)'s proof, u_1 in E_2 pointwise with all its
Cartesian derivatives (m1, chi, gh_j, the Taylor terms and w; d^i [f] costs lam^-i, a constant now), and lam [W_TT] =
r^(-3/2) G_3 with G_3(v, xhat) := the r^(3/2)-normalised Cartesian components of lam W_TT at phase v/lam, smooth and
bounded with all derivatives, vanishing for v <= v_start (P3). Theorem P controls finitely many derivatives (k = 6:
Proposition 9.8 with Lemma 9.3 gives d^i w in E_2 for i <= 4, the higher norms bounded); the approximating solutions of
its construction give every order at fixed lam, uniformly, Lemma 11.0, which is what the induction below consumes.

**Lemma 11.0 (every order at fixed lam).** Every Cartesian derivative d_X^alpha Omega^beta u_1 is in E_2 on the far
region, with constants depending on lam and the order.

*Proof.* By Lemma 11.1 below, u_1 = u - r^(-3/2) G_3 solves -(1/2) g_lam^{ab} d_a d_b u_1 = F_1 := S(u) - (1/2)
(g_lam^{ab} - g0^{ab}) d_a d_b u_1 + (1/2) box~ (r^(-3/2) G_3), and F_1 is in E_3 with all derivatives (S(u) by Lemma
11.1; the second term is E_(3/2) E_2; the third is in E_(7/2) by Lemma 9.7(c) and P2), where "all derivatives" of a term
containing u_1 means the orders already controlled. Induction on the order: for |gamma| = j + 1, U := d^gamma u_1 solves
-(1/2) g_lam^{ab} d_a d_b U = d^gamma F_1 + sum_{0 < gamma' <= gamma} (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b
u_1. The terms with |gamma'| = 1 are (d g_lam) d U with d g_lam in E_(3/2), of the kind Lemma 9.5's kernel k absorbs; a
term with |gamma'| >= 2 is a product of a derivative of g_lam of order <= j + 1 with one of u_1 of order <= j + 1, and is
estimated in L^2(Sigma_tau) with the factor of higher order in L^2 (the energies of the lower steps, at most C t^(-1/2))
and the other in sup norm (E_2 by the induction hypothesis, through Lemma 9.3 for the orders it costs, and by Theorem P
for the lowest), so the source is at most C(lam, j) t^(-3/2) in L^2. The identity is not run on the region between {v =
v_start} and Sigma_tau: that region is unbounded toward past null infinity (Lemma 9.1(e)), and the flux of d^gamma u_1
through infinity there is known to vanish only at the orders Theorem P controls (a thirteenth verifier's finding, D44).
It is run for each approximating solution g_n of Proposition 9.8 -- which equals g0 on {v <= v_start} and solves the same
equations, so that u_1^n := g_n - g0 - r^(-3/2) G_3 has the structure above, Lemma 11.1 applying to it verbatim with
(9.8) through Lemma 9.3 in place of Theorem P at the lowest orders, uniformly in n -- on P cap {tau_n <= tau' <= tau},
the region of (9.8)'s own identity. On Sigma_tau_n the data of U_n := d^gamma u_1^n are explicit: w_n = g_n - g_app
vanishes there with its first derivatives and its higher derivatives are those of the approximant's residual Ric^H(g_app)
through the equation, and g_app - g0 - r^(-3/2) G_3 is explicit with all derivatives (Lemma 9.7(c), P2), so ||d
U_n(tau_n)|| <= C(lam, j) t_n^(-1/2) with t_n >= t. Lemma 9.5's identity then gives ||d U_n(tau)|| <= ||d U_n(tau_n)|| +
C int_{tau_n}^tau t'^(-3/2) dtau' <= C(lam, j) t^(-1/2) at every order, uniformly in n. The bookkeeping of sup against
L^2 closes at every order N := |gamma|: the factor taken in sup norm has order at most floor((N + 2)/2), E_2 is in hand
pointwise to order max(4, N - 3) (Theorem P for the lowest orders, Lemma 9.3 on the energies of the lower steps for the
rest, at the cost of three), and floor((N + 2)/2) <= max(4, N - 3) for every N >= 1. Lemma 9.3 turns the energies of the
next three orders into |d^gamma u_1^n| <= C(lam, j) t^(-3/2) t^(-1/2) = C(lam, j) t^-2, uniformly in n (with Omega^beta
among the derivatives the same way: Lemma 9.3(a) with the rotation energies, the commutator [Omega, g_n^{ab} d_a d_b]
absorbed as in 9.8(iii)), and the bounds pass to the limit: g_n -> g_lam with k - 5 derivatives on compact sets (section
9.4, the proof of Theorem P), the higher derivatives of u_1^n are bounded uniformly in n on each compact set, so by
Arzela-Ascoli a subsequence converges in every C^j, its limit is d^gamma u_1, and the bound is inherited: d^gamma u_1 is
in E_2. []

**Lemma 11.1 (the equation for u).** On P, -(1/2) box~ u = S(u) with

    S(u) := -Ric(g0) + (1/2) (g_lam^{ab} - g0^{ab}) d_a d_b (g0 + u) - [ Q(g0 + u)(d g0 + d u, d g0 + d u)
            - Q(g0)(d g0, d g0) ],                                                                            (11.4)

and S(u) is in E_3: Ric(g0) = (3 mu'/(2 r^3)) dv dv exactly (ansatz5.py A2), g_lam^-1 - g0^-1 is in E_(3/2), d^2 g0 in
E_2 and d^2 u in E_(3/2), and the Q-difference is quadratic in d u (E_3) plus Gamma[g0] times d u (E_2 E_(3/2)).

*Proof.* Ric^H(g_lam) = 0 and Ric^H(g0) = Ric(g0) (section 0.2); subtract, using (0.2) for both. The classes are those
of section 9.3's count, with d^i u in E_(3/2) at fixed lam for the orders Lemma 11.0 controls, which that lemma supplies
in turn, order by order. []

**Lemma 11.2 (one half-order).** Let q be in {3, 7/2, 4, ...}, and let u~ be a symmetric tensor on the far region,
vanishing for v <= v_start, with every Cartesian derivative d_X^alpha Omega^beta u~ in E_(q-1), solving

    -(1/2) g_lam^{ab} d_a d_b u~ = r^-q S_q + S~,       S~ in E_(q+1/2) with all derivatives,                  (11.5)

S_q(v, xhat) smooth, bounded with all derivatives, vanishing for v <= v_start. Put F(v, xhat) := (2/(2q - 5))
int_{v_start}^{v} S_q dv'. Then u~ = r^(1-q) F + u~~ with every Cartesian derivative of u~~ in E_(q-1/2). If moreover,
for some m >= 1 and every j < m,

    (H_m)   ell^j S~ is in E_(q+1/2+j) and ell^j (g_lam - g0) in E_(3/2+j), each with all derivatives,

then ell^m u~~ is in E_(q-1/2+m) with all derivatives.

*Proof.* By Lemma 9.7(c), -(1/2) box~ (r^(1-q) F) = -(1/2)(3 - 2(q-1)) r^-q d_v F + E_(q+1) = r^-q S_q + E_(q+1), and
(g_lam^-1 - g0^-1) d^2 (r^(1-q) F) is in E_(3/2) E_(q-1) = E_(q+1/2). So u~~ := u~ - r^(1-q) F solves -(1/2) g_lam^{ab}
d_a d_b u~~ = S' with S' in E_(q+1/2) with all derivatives, vanishes for v <= v_start, and has every derivative in
E_(q-1). *Energy.* Lemma 9.5 with gt = g_lam (the margin of Lemma 9.1(f) holds on P by Theorem P; ||d g_lam||_inf <= C
t^(-3/2) on P+, integrable) and f = S', from tau1 -> -oo: ||d u~~(tau1)|| <= C t1^(3/2 - (q-1)) -> 0 since q > 5/2,
and ||S'(tau')|| <= C t'^(3/2 - q - 1/2) = C t'^(1-q), so ||d u~~(tau)|| <= C int_{-oo}^{tau} t'^(1-q) dtau' = C
t^(2-q)/(q-2). Commuting with d_X and Omega preserves the form: [d_X, g_lam^{ab} d_a d_b] = (d_X g_lam^{ab}) d_a d_b
with d_X g_lam^{ab} in E_(3/2), a term of the kind Lemma 9.5's k absorbs (k = C t^(-3/2), integrable), and [Omega,
box~] = 0 (P6); so every commuted energy is at most C t^(2-q). *Pointwise.* Lemma 9.3(b) (u~~ = 0 on {v = v_start})
and 9.3(a): |d_X^alpha Omega^beta u~~|_inf <= C t^(-3/2) t^(2-q) = C t^(1/2 - q): that is E_(q-1/2), since t and r are
comparable on P+ (Lemma 9.1(d)). *The ell-gain.* Write the equation of u~~ through (9.5): with psi := ell u~~ (ell
acting on Cartesian components),

    2 d_v psi + (1 - mu/r^2) ell psi + (3/r) psi = -2 S' - (3/r) d_v u~~ - r^-2 Deltaring u~~
                                                  - (g_lam^{ab} - g0^{ab}) d_a d_b u~~ =: f,                   (11.6)

f in E_(q+1/2) (its terms: E_(q+1/2), E_(q+1/2), E_(q+3/2), E_(3/2) E_(q-1/2)). The operator n := 2 d_v + (1 - mu/r^2)
ell is the outgoing null direction of g0 (in (v, r), n = 2 d_v + (1 - mu/r^2) d_r, and g0^-1(dv, dv) = 0, g0^-1(dv,
dr) = 1, g0^-1(dr, dr) = 1 - mu/r^2 by Lemma 9.7(b)), so (11.6) is a transport along the outgoing generators: along
one, dv/dsigma = 2 and dr/dsigma = 1 - mu/r^2 in (0, 1], so from a point (v, r) the generator reaches {v = v_start},
where psi = 0, after a parameter length (v - v_start)/2 <= d1/2 (Lemma 9.1(d)), at a radius r' in [r - d1/2, r];
integrating (n + 3/r) psi = f along it, |psi(v, r)| <= e^(3 d1/(2 r')) (d1/2) sup |f| <= C r^(-q-1/2), the supremum
over the segment, which lies in the far region once r is large. Derivatives commute through (11.6) up to terms of the
same kind, so ell u~~ is in E_(q+1/2) with all derivatives: the case m = 1, which needs nothing of (H_m) since f
contains no ell-derivative of S' or of g_lam. For m >= 2, under (H_m), the equation of ell^m u~~ is (11.6) commuted
m - 1 times with ell; its forcing is ell^(m-1) f plus the commutators [ell, n] = (2 mu/r^3) ell, [ell, 3/r] = 3/r^2 and
[ell, (g_lam^{ab} - g0^{ab}) d_a d_b] = (ell (g_lam - g0)^{ab}) d_a d_b applied to the lower ell^j u~~. Each term of
ell^(m-1) f is in E_(q+1/2+m-1): ell^j S' by (H_m) (S' is S~ plus (g_lam^-1 - g0^-1) d^2 (r^(1-q) F) and box~ (r^(1-q)
F) - r^-q S_q, whose ell-derivatives gain by (H_m) and explicitly), ell^j of (3/r) d_v u~~ and r^-2 Deltaring u~~ by
the gains already established for j < m, and (ell^j (g_lam - g0)^{ab}) d^2 ell^(m-1-j) u~~ by (H_m) with those gains:
E_(3/2+j) E_(q-1/2+m-1-j) = E_(q+m). The commutator terms are of the same kind. So the transport gives ell^m u~~ in
E_(q-1/2+m), and derivatives commute as before. []

**Proposition 11.1 (the expansion).** For every J >= 3 there are smooth tensors G_k(v, xhat), k = 3, ..., J, bounded with
all derivatives, vanishing for v <= v_start, T^2 x Z2 x Z2 invariant, with G_3 as above, and

    u = sum_{k=3}^{J} r^(-k/2) G_k + u_J,     d_X^alpha Omega^beta ell^m u_J in E_((J+1)/2 + m)                 (11.7)

on the far region. The G_k are determined inductively: G_k = (2/(k - 3)) int_{v_start}^{v} S_(k/2 + 1) dv' for k >= 4
(G_4 = 2 int S_3), where r^-q S_q is the leading term of the source once the terms below it are known.

*Proof.* Induction on J with Lemma 11.2. J = 3: u_3 := u_1 is in E_2 with all derivatives (Lemma 11.0), and by Lemma
11.1 it solves -(1/2) g_lam^{ab} d_a d_b u_3 = S(u) - (1/2)(g_lam^{ab} - g0^{ab}) d_a d_b u_3 + (1/2) box~ (r^(-3/2)
G_3) =: F_1: the second term is in E_(7/2) (E_(3/2) E_2), the third in E_(7/2) (Lemma 9.7(c), P2), and S(u) in E_3 with
an r^-3 leading term determined by G_3 alone: -(3 mu'/2) dv dv (Ric(g0)) plus the terms of (11.4) quadratic in
d(r^(-3/2) G_3) or of the form (r^(-3/2) G_3) d^2 (g0 + r^(-3/2) G_3), since every term containing u_3 is in E_(7/2)
(E_(3/2) E_2 or Gamma[g0] E_2). So (11.5) holds at q = 3 and Lemma 11.2 gives u = r^(-3/2) G_3 + r^-2 G_4 + u_4 with
every derivative of u_4 in E_(5/2). *The ell-gains at J = 3, by induction on m.* The case m = 1 needs no hypothesis:
ell u_4 is in E_3, hence ell u_1 = ell (r^-2 G_4) + ell u_4 is in E_3 and ell (g_lam - g0) = ell (r^(-3/2) G_3) + ell
u_1 in E_(5/2), with all derivatives. Suppose ell^j u_4 is in E_(5/2+j) for j < m. Then ell^j (g_lam - g0) is in
E_(3/2+j) for j < m, and so is ell^j S~ in E_(7/2+j): S~ = F_1 - r^-3 S_3 is a polynomial in g0, g_lam^-1, u, d u, d^2
u whose every term either is explicit (the terms in G_3 and g0, whose ell-derivatives gain an order each because r^-k
and the profiles do) or contains u_1 or a derivative of it, on which ell^j gains j orders by the hypothesis, the other
factors keeping their classes. So (H_m) holds and Lemma 11.2 gives ell^m u_4 in E_(5/2+m): (11.7) at J = 4. Stage J >=
4: the remainder u_J has every ell-gain, so the source of u_J, a polynomial in (u, d u, d^2 u) with coefficients smooth
in (X, g) whose arguments are expanded to the previous order with remainders in E_((J+1)/2), has the expansion r^-q
S_q + S~ with q = (J+3)/2 and S~ satisfying (H_m) for every m: every product with a remainder factor is in E_(3/2 +
(J+1)/2) = E_(q+1/2) or better and gains under ell, so the r^-q coefficient is a polynomial in the G_k, k <= J, and
their derivatives, and Lemma 11.2 applies at every m. Invariance and the vanishing for v <= v_start are inherited by the
integrals from v_start. []

The coefficients from G_4 on depend on lam (through the phase v/lam and the powers of lam of the profiles), and the
proposition claims nothing uniform in lam: it is an asymptotic statement at past null infinity at each fixed lam, which
is all the mass law needs.

### 11.2 Bondi coordinates at past null infinity

**Lemma 11.3 (the ell-components).** G_3(ell, .) = 0 and tr G_3 = 0 (W_TT is transverse and traceless: (E1), A3);
so u(ell, .) is in E_2 and tr_S u (the trace on the spheres S_(v,r)) in E_2, and g_lam^{vv} = -u(ell, ell) + E_3 is in
E_2, (g_lam^-1 - g0^-1)(dv, .) = -g0^-1 u(ell, .) + E_3 in E_2.

*Proof.* g^-1 = g0^-1 - g0^-1 u g0^-1 + O(u^2) and g0^-1 dv = ell. []

Write the coordinate components of the G_k in the (v, r, th) basis: u_rr = sum_k s^k C_k, u_vr = sum s^k B_k, u_vv =
sum s^k A_k, u_(r th) = r sum s^k E_k, u_(v th) = r sum s^k D_k, u_(th th) = r^2 sum s^k F_k, u_11 = r^2 cos^2 th sum
s^k G_k, u_22 = r^2 sin^2 th sum s^k H_k (one power of r per angular index, the classes being of orthonormal
components), with s = r^(-1/2); by Lemma 11.3, A_3 = B_3 = C_3 = D_3 = E_3 = 0 and F_3 + G_3 + H_3 = 0, with F_3 = -2
(p1 + p2), G_3 = 2 p1, H_3 = 2 p2 (A3).

**Proposition 11.2 (the Bondi chart; computed B2 to the orders stated, deduced).** There is T_M(lam) such that on the
far region P cap {t >= T_M} the functions

    v_B := v + ů,   th_B := th + ϑ,   r_B := r (1 + rho)

exist with: (i) g_lam^-1(dv_B, dv_B) = 0, ů -> 0 along every generator of g0 as r -> oo; (ii) g_lam^-1(dv_B, dth_B) = 0,
ϑ -> 0 likewise; (iii) r_B is the areal radius: r_B^6 cos^2 th_B sin^2 th_B is the determinant of the metric induced
on {v_B, r_B = const} in the coordinates (th_B, phi1, phi2); (iv) they are T^2 x Z2 x Z2 invariant and equal (v, th,
r) for v <= v_start. With u expanded to order J by (11.7), they have expansions in s with coefficients smooth in (v,
th), vanishing for v <= v_start,

    ů = sum_{k=2}^{J-2} s^k ů_k + E_((J-1)/2),   ϑ = sum_{k=4}^{J-2} s^k ϑ_k + E_((J-1)/2),
    rho = sum_{k=4}^{J-2} s^k rho_k + E_((J-1)/2),                                                            (11.8)

whose first coefficients are ů_2 = -C_4/2, ů_3 = -C_5/3, ů_4 = -C_6/4 + C_4 d_v C_4/8, ϑ_4 = -E_4/2 - d_th C_4/4 and
rho_4 = (F_4 + G_4 + H_4)/6 - (1/3) div(ϑ_4) (div f := (sin th cos th)^-1 d_th (f sin th cos th)) (B2), and whose
remainders gain an order under ell. In the chart (v_B, r_B, th_B, phi1, phi2) the metric has the form (11.1), its
functions given by the inverse components g^{v_B r_B} = e^{-2 b}, g^{r_B r_B} = e^{-2 b} W, g^{r_B th_B} = e^{-2 b} U,
g^{th_B th_B} = 1/(r_B^2 S), S := e^{-2(P1 + P2)}, g^{phi_i phi_i} = 1/(r_B^2 cos^2 th_B e^{2 P1}), 1/(r_B^2 sin^2 th_B
e^{2 P2}) (B1 checks these against (11.1)), and they have expansions in s_B := r_B^(-1/2) with coefficients smooth in
(v_B, th_B), vanishing for v_B <= v_start, to order s_B^(J-2) with remainders o(s_B^(J-2)) whose r_B-derivatives gain
an order each. Their first coefficients are e^{2 P1} = 1 + 2 p1 s_B^3 + O(s_B^4), likewise P2, and e^{-2 b} = 1 -
(d_v C_4/2) s_B^2 - (d_v C_5/3) s_B^3 + O(s_B^4) (B2).

*Proof.* (i) Write the eikonal equation for ů with L := g_lam^-1 dv = ell + eps, eps := (g_lam^-1 - g0^-1)(dv, .) in
E_2 (Lemma 11.3):

    2 ell ů = -g_lam^{vv} - 2 eps(dů) - g_lam^-1(dů, dů) =: N[ů].                                            (11.9)

v_B is built by characteristics, not by iterating (11.9) (an iteration in a norm of ů and ell ů loses a derivative at
each step through the term eps(dů), as a verifier observed). In g0 the generators of {v = v0} are the affinely
parametrised null geodesics gamma0(r) = (v0, r, xhat0), with ell = d_r their tangent and Gamma[g0]^a_{rr} = 0. For each
(v0, xhat0) let gamma be the null geodesic of g_lam asymptotic to gamma0: gamma(r) = (v0 + zeta(r), r, xhat0 + xi(r)),
parametrised by r, solving d^2 gamma^a/dr^2 + Gamma[g_lam]^a_{bc} gamma'^b gamma'^c = kappa gamma'^a with kappa fixed by
the r-component (gamma^r = r), and zeta, zeta', xi, xi' -> 0 as r -> oo. Writing gamma' = d_r + eta, the system is eta'
= -(Gamma[g_lam] - Gamma[g0])^a_{rr} - 2 Gamma[g_lam]^a_{rb} eta^b - Gamma^a_{bc} eta^b eta^c + kappa gamma'^a, a
Volterra system from r = oo whose forcing (Gamma[g_lam] - Gamma[g0])^v_{rr} = (1/2) g^{vd}(2 d_r u_{dr} - d_d u_{rr}) is
in E_3 by Lemma 11.3 and the ell-gain of u (g^{vr} = 1 + E_(3/2) multiplies d_r u_{rr} in E_3; g^{vv} in E_2 multiplies
E_2; g^{v th} r^-1 is in E_3), whose angular forcing is in E_4 (g^{th th} = r^-2 (1 + E_(3/2)) times d_r u_{th r} = r
d_r u(e_th, ell) + u(e_th, ell) in E_2), whose linear part -2 Gamma[g0]^a_{rb} eta^b vanishes for a = v
(Gamma[g0]^v_{rb} = 0 in the ingoing chart) and is -(2/r) xi' for a = theta (Gamma[g0]^th_{r th} = 1/r) -- not an
integrable perturbation but the unperturbed operator of the angular equation, xi'' + (2/r) xi' = E_4, which the
integrating factor r^2 solves with xi' in E_3 and xi in E_2 -- and whose remaining coefficients are Lipschitz in (zeta,
xi, zeta', xi') in the weighted norms below with constants integrable in r (d(Gamma[g_lam] - Gamma[g0]) in E_(3/2); the
terms quadratic in eta, Gamma[g0]^v_{th th} = -r the largest coefficient, are O(r^-2) times the norm); kappa =
Gamma^r_{bc} gamma'^b gamma'^c is in E_2 and multiplies eta. So for r >= T_M the Picard iteration converges in the
weighted sup norms r^2 |zeta'| + r |zeta| + r^3 |xi'| + r^2 |xi| (ODE contraction: no derivative is lost), the solution
depends smoothly on (v0, xhat0) with derivatives of the same decay (variational equations with the same structure), is
invariant, and is gamma0 for v0 <= v_start (there g_lam = g0 along the whole generator). The map Phi: (v0, r, xhat0) ->
gamma(r) is then a C^1-small perturbation of the identity for r >= T_M, a diffeomorphism onto a neighbourhood of past
null infinity, and N_{v0} := Phi({v0} x [T_M, oo) x S^3) is a null hypersurface: along each gamma, d/dr g_lam(gamma',
gamma') = 2 kappa g_lam(gamma', gamma'), so g_lam(gamma', gamma') e^{-2 int kappa} is constant and equal to its limit
g0(ell, ell) = 0 at infinity (gamma is null); and for each Jacobi field X = d_{xhat0} gamma of the congruence, tangent
to N_{v0} as gamma' is, d/dr g_lam(gamma', X) = kappa g_lam(gamma', X) + g_lam(gamma', nabla_X gamma') = kappa
g_lam(gamma', X) + (1/2) X g_lam(gamma', gamma') = kappa g_lam(gamma', X), so g_lam(gamma', X) e^{-int kappa} is
constant along gamma and equal to its limit at infinity, which is 0: g_lam(gamma', X) = d_{xhat0} zeta + r^2 xi' (1 +
d_{xhat0} xi) + r u(ell, e_th) + smaller, with d_{xhat0} zeta, r^2 xi' and r u(ell, e_th) in E_1. (The transverse field
d_{v0} gamma is not needed, and is not orthogonal to gamma': g0(ell, d_v) = 1.) Hence gamma' is normal to N_{v0}, which
is null. Put v_B := v0 o Phi^-1, so that g_lam^-1(dv_B, dv_B) = 0, and ů := v_B - v = -zeta o Phi^-1: ů is in E_1 with
ell ů in E_2 (ell ů = -zeta' up to the E_2 Jacobian corrections) and all derivatives, vanishes for v <= v_start, and is
invariant. *Expansion.* v_B satisfies (11.9) exactly, so ů = -(1/2) int_r^oo N[ů] dr' along the generators of g0. Insert
(11.7): -g_lam^{vv} = u(ell, ell) + u(ell, .)^2-terms = r^-2 C_4 + r^(-5/2) C_5 + r^-3 C_6 + ... + E_((J+1)/2), the
integrals of the powers are the powers below, the nonlinear terms at order s^(k+2) involve only ů_j with j < k, and the
remainder of ů is the integral along the generator of a remainder, with ell of it the integrand: (11.8), whose first
coefficients B2 computes by solving (11.9) order by order (the s^(k+2) coefficient of the equation is -k ů_k plus known
terms, k >= 1). (ii) th_B := xhat0 o Phi^-1 (the angle of the generator of g0 that gamma is asymptotic to) is constant
along the generators of N_{v0}, whose tangent is L = g_lam^-1 dv_B up to a factor (gamma' is the null normal of N_{v0}):
L th_B = 0, and ϑ = th_B - th = -xi o Phi^-1 is in E_2 with ell ϑ in E_3. The transport L th_B = 0 reads 2 ell ϑ = -2
eps(dth) - 2 g_lam^-1(dů, dth) - 2 (eps + g_lam^-1 dů)(dϑ), with eps(dth) = -r^-2 u(d_th, ell) + E_4 = -r^-1 u(e_th,
ell) + E_4 in E_3 (e_th := r^-1 d_th) and g_lam^-1(dů, dth) = r^-2 d_th ů + E_4 in E_3, and ϑ expands as in (11.8), the
s^(k+2) coefficient of the equation being -k ϑ_k plus known terms (B2). (iii) Let J0 be the Jacobian of (v, s, th) ->
(v_B, r_B, th_B). In a chart with g^{v_B v_B} = g^{v_B th_B} = 0 the covariant metric has g_{r_B r_B} = g_{r_B th_B} =
0, so it has the form (11.1) once r_B is areal, and its inverse determinant is -e^{-4 b}/(r_B^6 cos^2 th_B sin^2 th_B)
with e^{-2 b} = g^{v_B r_B}; the inverse determinant transforms with (det J0)^2. So the areal condition is the equation

    r_B^6 cos^2 th_B sin^2 th_B det(g_lam^-1) (det J0)^2 + (g^{v_B r_B})^2 = 0,                             (11.10)

whose s^k coefficient is 6 rho_k plus known terms: the factor d_r r_B = 1 + rho + r d_r rho of (det J0)^2 cancels
against the same factor of (g^{v_B r_B})^2 = (g_lam^-1(dv_B, dr_B))^2 at this order, and r_B^6 contributes 6 rho_k (the
leading determinant is 1), so the condition is algebraic in rho and solvable for every k >= 1; the coefficients with k
<= 3 vanish identically (B2: tr_S u is in E_2, and the shifts enter at s^4), so rho starts at s^4 with rho_4 as stated,
the trace of G_4 on the sphere plus the Jacobian of the angular shift. The remainder is algebraic in those of (i)-(ii)
and of u. (iv) and the Bondi functions: the formulae are the inverse of (11.1)'s (v, r, th) block. Re-expression in
(v_B, th_B, s_B): a coefficient f(v, th) = f(v_B - ů, th_B - ϑ) is expanded by Taylor's formula, ů = O(s^2) and ϑ =
O(s^4) shifting coefficients by two and four half-orders, and s = s_B (1 + rho)^(1/2) by four; the expansion to order
s_B^(J-2) with remainders o(s_B^(J-2)) follows, and the remainders' r_B-gains from the ell-gains of the ingredients
(d_{r_B} is a combination of ell and E_2 multiples of d_v, d_th). The first coefficients: e^{2 P1} = 1/(r_B^2 cos^2 th_B
g^{11}) with g^{11} = g_lam^{11} unchanged (phi1 is), r_B/r = 1 + O(s^4), th_B - th = O(s^4), and g_lam^{11} = r^-2
cos^-2 th (1 - 2 p1 s^3 + O(s^4)): so e^{2 P1} = 1 + 2 p1 s_B^3 + O(s_B^4) (B2); e^{-2 b} = g^{v_B r_B} = g_lam^-1(dv +
dů, dr_B) = 1 + d_v ů + O(s^4) at the orders shown, since g_lam^{vr} = 1 + E_2, g_lam^-1(dů, dr) = d_v ů + ell ů with
ell ů = O(s^4), and dr_B = dr + O(s^2)... (B2 computes it: -(d_v C_4/2) s^2 - (d_v C_5/3) s^3 + O(s^4)). []

Taking J = 8 in Proposition 11.1 gives the Bondi functions to order s_B^6 with o(s_B^6) remainders: this is what 11.3
uses. (The hierarchy below, run from s^1 (B1's first step), gives b_1 = b_2 = b_3 = 0 for a vacuum metric, so d_v C_4
= d_v C_5 = 0 and, by (iv), C_4 = C_5 = 0: the (ell, ell) component of g_lam - g0 is O(r^-3). This is a consequence,
not an input: Proposition 11.3's hypothesis lets b start at s^1.)

### 11.3 The hierarchy in the class, and the proof of Theorem M

**READ (alphaXiv, 2026-10-20).** [TTS09] K. Tanabe, N. Tanahashi and T. Shiromizu, "On asymptotic structure at null
infinity in five dimensions", arXiv:0909.0426v2, pp. 2-5. Bondi coordinates in five dimensions: "ds^2 = -(V e^B/r^2)
du^2 - 2 e^B du dr + r^2 h_AB (dx^A + U^A du)(dx^B + U^B du)" (4), h_AB built from C1, C2, C3, D1, D2, D3 (5), with
"the function r by the equation r^6 sin^2 theta cos^2 theta = det(g_AB)" (2). "When functions C corresponds to
gravitational waves, C behaves as ~ 1/r^{3/2} near null infinity" (p. 3); from the equations "B = B1/r^3 + O(r^{-7/2})"
(20) with "B1 = -(C11^2 + C11 C21 + C21^2 + D11^2 + D21^2 + D31^2)/8" (21), "U^A = U_{A1}/r^{5/2} + O(1/r^3)" (25), "V =
r^2 + V1(u, x^A) r^{1/2} - M(u, x^A) + O(r^{-1/2})" (26) with V1 = -(2/3)((sin th cos th)^-1 (U_th1 sin th cos th)_,th +
U_phi1,phi + U_psi1,psi) (27) "and M(u, x^A) is an integration constant" (p. 4), and

    "dM(u, x^A)/du = -(1/3)((C11,u)^2 + C11,u C21,u + (C21,u)^2 + (D11,u)^2 + (D21,u)^2 + (D31,u)^2)"     ((28), p. 4),

"Eq. (28) represents mass loss rate by gravitational waves"; the r^-2 term A of C satisfies "dA/du = 0" (35) and
vanishes for asymptotic flatness, their (36), by its value at spatial infinity; and "there is no supertranslation
freedom unlike in four dimensions" (p. 7).

In the class, with D1 = D2 = D3 = 0 (both reflections) and th_T = pi/2 - th, their form is (11.1) with C1 = -2(P1 +
P2), C2 = 2 P1, C3 = 2 P2, B = 2 b, V/r^2 = W (routes5.py Q2; the time reversal u -> -v leaves the squares of (28)
unchanged and the sign of M's rate reversed: an incoming flux raises the mass). B1 recomputes the hierarchy in (11.1)
itself, as series in s = r^(-1/2) with general coefficient functions of (v, th), each quantity a truncated Laurent
series handled termwise (an r-derivative raises the s-order by two and v-, th-derivatives preserve it; which
coefficients the s^6 equation contains is read off, not assumed), so that nothing below is taken from [TTS09] but the
comparison.

**Proposition 11.3 (the hierarchy at past null infinity; computed, `bondi5.py` B1).** Let a metric of the form (11.1) be
vacuum near past null infinity, with P1, P2, b, U, W - 1 having expansions in s to order s^6 with o(s^6) remainders
gaining two s-orders (one power of r) under each r-derivative as in Theorem M(a), P_i = O(s^3), and b, U, W - 1 = O(s).
Write p := P1's s^3 coefficient, q := P2's, a1, a2 the s^4 coefficients, b_k, u_k, w_k the coefficients of b, U, W.
Then, in order: (0) from R_rr at s^5, s^6 (R_ss = 4 s^-6 R_rr at s^-1, s^0: -12 b_1, -24 b_2) and R_(r th) at s^1, s^2
(R_(s th) = -2 s^-3 R_(r th) at s^-2, s^-1: -(7/4) u_1, 3 b_1 u_1 - 3 u_2): b_1 = b_2 = 0 and u_1 = u_2 = 0; (i) from
R_rr at s^7, ..., s^10 (R_ss at s^1, ..., s^4): b_3 = b_4 = b_5 = 0 and b_6 = -(1/4)(p^2 + p q + q^2) ([TTS09] (21) with
C = 2P, B = 2b); (ii) from R_(r th) at s^3, ..., s^6: u_3 = u_4 = 0, u_5 = (12/5)(p + q) tan th - (8 p + 16 q)/(5 sin
2th) - (4/5) d_th (p + q), and u_6 the same expression in (a1, a2) with 4/3 for 4/5 and 8/3, 16/3 for 8/5, 16/5; (iii)
from R_vr at s^5, ..., s^7: w_1 = w_2 = 0 and w_3 = -(2/3) div(u_5) ([TTS09] (27)): <w_3> = 0; (iv) from the traceless
part of R_AB at s^2: d_v a1 = d_v a2 = 0 (the three angular components give -(d_v a1 + d_v a2), cos^2 th d_v a1, sin^2
th d_v a2; [TTS09] (35)); (v) R_vv at s^5 is then an identity (the rate of (iii)), and at s^6 it is linear in d_v w_4
and reads

    d_v M = (4/3)(p_v^2 + p_v q_v + q_v^2) + (2/3) div(d_v u_6),      M := -w_4;                            (11.2')

the coefficient at s^6 involves only p, q, a1, a2 and w_4, so remainders o(s^6) do not disturb it; with (iv), d_v u_6 =
0 and (11.2') is (11.2) pointwise. B1 runs (0) with b, U, W - 1 from s^1 and P from s^3 to s^4, and (i)-(v) with the
ansatz carried to s^7 (so that the absence of the s^7 coefficients from the s^6 equation is seen, not assumed), in about
three minutes; its controls, the law with coefficient 1 for 4/3 and the law without its divergence while a1, a2 are
free, fail.

**Proof of Theorem M.** (a) is Proposition 11.2 with J = 8. (b): the s^3 coefficient of P_i is p_i by Proposition
11.2's last sentence, the record's free data at phase v_B/lam (A3; (P-ii) is this statement in the wave gauge, and the
chart change preserves it). a_i: by Proposition 11.3(iv) d_v a_i = 0, and a_i = 0 for v_B <= v_start where the metric
is g0 (Proposition 11.2(iv)); so a_i = 0 -- [TTS09]'s argument from spatial infinity, with the seed in its place. (c):
Proposition 11.3(v) with a_i = 0 is (11.2); M = mu0 for v_B <= v_start since g_lam = g0 there, Vaidya with mu = mu0,
whose W = 1 - mu0 s^4; the sphere mean of (11.2) is the mean of (4/3)(p1_v^2 + p1_v p2_v + p2_v^2), which P7 computes
as (9.10); integrating from v_start gives (11.3) and the statement after the shell. (d) is B3: in (11.1), with n- =
-d_r (theta- = -3/r exactly, the area form being r^3 cos th sin th) and n+ = d_v + (W/2) d_r + U d_th (null; theta+ = 3
W/(2 r) + div U), g(n+, n-) = -e^{2b}, so M[S] = r^2 (1 - <e^{-2b} (W + (2r/3) div U)>) = -s^-1 <w_3 + (2/3) div u_5> -
<w_4 + (2/3) div u_6> + O(s), and the divergences have zero mean: M[S] -> <-w_4> = mu_B. []

### 11.4 The numerics, and what this closes

The numerical solver (hf_mirror5.py, hf_core5.py) evolves the metric in the form (11.1) from the record's free data at
y = 0 (past null infinity), and the rate of its mass aspect M = -w_y|_{y=0} is fixed by E_vv = 0, the s^6 equation
above (aspect_rates: "By Bondi's lemma these are the conservation laws at past null infinity"). So its mean mass M_mean
is mu_B as integrated by the solver, and its offset from mu(v) after the shell should be (2/9) lam^2 A^2 int env'^2 +
O(lam^3) = (5 pi^2/108) lam^2 for the solver's envelope sin^4(pi (v - 1/2)/3) on [1/2, 7/2] (int env'^2 = 5 pi^2/24, A =
1; response5.py R8): 0.45693 lam^2. The runs give offset/lam^2 = 0.4589, 0.4577, 0.4568 at lam = 0.05, 0.025, 0.0125
(mu0 = 100 l5^2) and 0.4578, 0.4569 at lam = 0.025, 0.0125 (1000 l5^2), converging to 0.4569 as O(lam) (B4; the run at
lam = 0.00625 on the 32 x 16 grid gives 0.4535, 0.7 % low, the grid being coarse for that wavelength; the quartering
hf_theorem5.py F4 recorded was this rate). This compares the law's integral with the solver's own integration of the
same law; it does not test g_lam, which Theorem M does.

Closed: the item "the mean mass at past null infinity" of the paper's section 8. Not claimed: uniformity in lam of the
expansion (11.7) beyond the leading term, which the mass law does not need; and nothing about future null infinity or
the Bondi mass there, which the domain does not reach.
