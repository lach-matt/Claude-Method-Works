# EQUALITY5-LAYER -- the layer at μ0 = √72 l5²: the boundary has timelike points

Status: written (this note); not yet read by an independent verifier. Check scripts: `checks/layerlin5.py` N0–N6 and
`checks/layerwin5.py` W1–W3 (computed), all pass, every control fails (`.out` files beside them). This note decides
EQ5 of `EQUALITY5.md` (Remark E.6) **negatively**: in the layer the boundary x_K = 1 is neither spacelike nor timelike
throughout; for λ small its causal character for g_λ alternates on the scale of the phase, at every angle (Theorem L).
The decision rests on computed algebra (Proposition L.2, section 4) and on three analytic lemmas (L.3, L.4 and the
identification in L.2 (a)) that are deduced here from the supplement's own construction and energy lemmas, written at
the level of a proof sketch; their independent check is open item O2. Nothing in `EQUALITY5.md`, the paper or the log
is changed.

## 0. The answer

**Theorem L (the layer at equality; deduced, with layerlin5 N0–N6 and layerwin5 W1–W3).** Let μ0 = √72 l5², A > 0,
env ∈ C_c^∞(R) not identically zero, v_s := inf supp env, τ0 with v_s − τ0 > √μ0 + 1, K ≥ 7, and let g_λ (0 < λ ≤
λ0) be the metric of Theorem 1 built as in the supplement (Theorem A with the stage data of its Lemma 6.2, N = K + 3,
the correction of its Proposition 6.5, Theorem E). There are λ_L ∈ (0, λ0] and, for every λ ≤ λ_L, an interval
W_λ = [v*_λ, v*_λ + 4πλ] with v_s < v*_λ, v*_λ → v_s as λ → 0, and W_λ inside the layer v_s < v < v_s + η_λ of
Proposition E.3 (c), such that for every λ ≤ λ_L and **every angle ω ∈ S³**:

    g_λ⁻¹(dΦ0, dΦ0)(v, r_q(v), ω) = −λ³ A env(v) K(v − τ0) Re[d(θ) e^(iv/λ)] + ρ_λ(v, ω)   on W_λ,          (0.1)

    sup_(W_λ × S³) |ρ_λ|  ≤  δ(λ) λ³ inf_(W_λ) (env |K(· − τ0)|) inf_θ |d(θ)|,      δ(λ) → 0,

with d(θ) := div_σ div_σ (T^G − i T^F) the double divergence on the round S³ of the wave's angular tensor (section
4), |d| > 0 at every angle, and

    K(r0) = −μ0^(−7/4) (2ρ³ − 3ρ² − 2)² / (36 ρ⁶),     ρ := r0/√μ0,                                          (0.2)

which vanishes only at ρ* = 1.80644… (a double root). Consequently, on every column ω the boundary {x_K = 1} has, in
every half of W_λ, points where it is **timelike** for g_λ (g_λ⁻¹(dΦ0, dΦ0) > 0) and points where it is spacelike.
The boundary is not spacelike throughout the layer, and not timelike throughout it either. No genericity is needed: the
statement holds for every C_c^∞ envelope (section 6) and every admissible τ0, including (v_s − τ0)/√μ0 = ρ*.

**Corollary L.7 (deduced).** At each timelike point some future timelike curves of g_λ cross {x_K = 1} from {x_K > 1}
into D_T: Proposition 3.2's statement (every future causal curve that meets the boundary leaves D_T and does not
return) fails at equality inside the layer. Proposition E.4's domain D_T^λ, whose inner boundary has the margin −C_Φ λ
there, is therefore not only a replacement but a necessary one. (A spacelike covector takes both signs on the future
timelike cone; take the g_λ-geodesic through the point with a velocity on which dΦ0 > 0.)

**The mechanism, and a correction to Remark E.6.** Expand around the exact seed in the amplitude, λ fixed. The margin
m0 is of second degree in the wave (it is the mass increase); the term of first degree is −[g_λ − g0](Φ0♯, Φ0♯) on
the boundary, Φ0♯ = ∂_v + O(A² env²) ∂_r. Its λ¹ part is zero (W_TT is tangent to the spheres, ansatz5 A3), and,
contrary to the heuristic recorded in Remark E.6, so is its λ² part: the supplement's λ² profile lies in the class S
of section 3 (its vv, vr, rr components and trace vanish), by polarization and by the isotropy of Pol^+ (N2–N3). The
first nonzero part is λ³, a first harmonic of the phase, proportional to the double divergence d of the angular tensor
(the scalar part of the wave on S³) and to the mass through the coupling 2μ0/r³ of the vv and vr transports (N1, N4,
N5). Near the edge, where A env is smaller than every power of λ, this first-degree term beats m0 and every error term
(section 6), and it changes sign with the phase.

## 1. Setting (READ: `EQUALITY5.md` sections 0–2, the paper sections 2–4, the supplement sections 2, 5, 6)

Coordinates (v, r, θ, φ1, φ2) as in `EQUALITY5.md` (0.1) and `ansatz5.py`: g0 = −F dv² + 2 dv dr + r² σ, F = 1 −
μ(v)/r², σ = dθ² + cos²θ dφ1² + sin²θ dφ2²; ∂_v here is the Kerr–Schild ∂_τ (v = τ + r); ℓ = g0⁻¹ dv = ∂_r. At
equality r_q = (μ0 μ)^(1/4), Φ0 = r − r_q(v), m0 = −g0⁻¹(dΦ0, dΦ0) (EQUALITY5 (0.2)). Φ0♯ := g0⁻¹ dΦ0 = ∂_v + β0 ∂_r,
β0 := F(r_q) − r_q' = 1 − √(μ/μ0) − r_q μ'/(4μ). The hypersurface {Φ0 = 0} is timelike at a point exactly when dΦ0 is
spacelike there, g_λ⁻¹(dΦ0, dΦ0) > 0.

g_λ = g_app + w, g_app = g0 + Σ_(j=1)^N λ^j [g_j] (fixed phase, supplement (0.4) and 5.4). Write k := g_λ − g0,

    E(v) := sup_(v' ≤ v) env(v'),     ε_M(v) := Σ_(i ≤ M) sup_(v' ≤ v) |env^(i)(v')|,

and say a quantity is *of degree ≥ 2* if, with μ − μ0 = (2/9) A² ∫ env² counted as degree 2, it is a sum of products of
at least two factors of the form (A env^(i)) times smooth coefficients. A profile H(v, r, θ) e^(iv/λ) is the complex
form of a first harmonic; the real part is meant.

**The class S.** S := {h : h_vv = h_vr = h_rr = 0, σ^AB h_AB = 0}: under T² × Z2 × Z2 the remaining components are vθ,
rθ and the traceless tangential ones.

## 2. The expansion on the boundary

**Lemma L.1 (deduced; the identity computed, N0).** On the boundary,

    g_λ⁻¹(dΦ0, dΦ0) = −m0 − k(Φ0♯, Φ0♯) + q,     |q| ≤ C |k(Φ0♯, ·)| (|k(Φ0♯, ·)| + |k|²),

C depending on the bounds of g0⁻¹ and g_λ⁻¹ on Ω. *Proof.* g_λ⁻¹ = g0⁻¹ − g0⁻¹ k g0⁻¹ + g0⁻¹ k g0⁻¹ k g_λ⁻¹ (N0,
exact; it fails without the last term); contract with dΦ0 twice; g_λ⁻¹ dΦ0 = Φ0♯ + O(|k|²) + O(|k(Φ0♯, ·)|). ∎

## 3. The part linear in the wave

**Proposition L.2 (computed: layerlin5 N1–N5; (a) deduced).** (a) *Identification.* The part of first degree of
Σ_j λ^j [g_j] is Re Σ_j λ^j H_j e^(iv/λ), where H_1 := A env(v) r^(1/2) T, T := diag(−(a + b), cos²θ a, sin²θ b) on
(θ, φ1, φ2) with a = 2p1, b = 2p2 per unit amplitude, the quadratures combined as T = T^G − i T^F (so that Re[A env
r^(1/2) T e^(iv/λ)] is W_TT of (2.5′)), and for j ≥ 1

    T(H_(j+1)) = −R_X(H_j)  along ℓ,      H_(j+1) = i Pol^+(D_X H_j)  on Σ_τ0  (at r = r0 := v − τ0),       (3.1)

T := −i(∇_ℓ + 3/(2r)) the λ⁻¹ part, and R_X, D_X the λ⁰ parts, of the linearizations of Ric^H and D at the seed on
H e^(iv/λ) (N1 (b): the λ⁻² parts vanish, g0⁻¹(dv, dv) = 0; the λ⁻¹ part of the linearized D is i Pol), and Pol^+ the
map of the supplement's Lemma 6.2 (i). *Proof.* At first degree the means m_m, the phases φ_m, χ and the slice data
(h_m, Q_m) of Lemma 6.2 (iii) vanish: their sources are θ-means (Lemma 5.3 (a), (b); Lemma 6.2 (ii), (iii)), and every
first-degree profile is a first harmonic (W is, and the transport and Pol^+ act pointwise in θ). So Lemma 5.3 (c) is,
at first degree, the transport by Th of the λ^(m+1) profile with source minus the X-part of the linearized Ric^H on the
λ^m profile, and Th at first degree is the λ⁻¹ part of the linearized Ric^H (supplement section 3.2, the terms of T
bilinear in W dropping); Lemma 6.2 (i) is ∂_θ ĝ_(m+1) = −Pol^+(D_X ĝ_m) on Σ_τ0, since Λ_m(h_m) has no first-degree
part; the fixed-phase rewriting (supplement 5.4) adds only terms with a factor φ_j. With ĝ = Re[H e^(iθ)], ∂_θ ĝ =
Re[i H e^(iθ)], which is (3.1). Coefficients at μ(v) instead of μ0 differ by terms of degree ≥ 3. ∎

(b) *Two identities (N1, exact for every T² × Z2 × Z2-invariant h, all components arbitrary functions of (v, r, θ)).*
For h ∈ S, (dRic^H h)_vv = 0 and tr_g0 dRic^H h = 0 (control: h_vr ≠ 0 gives a nonzero vv component). The transport
T is, componentwise, vv: −i(∂_r H_vv + 3H_vv/(2r) + 2μ0 H_vr/r³), vr: −i(∂_r H_vr + 3H_vr/(2r) + μ0 H_rr/r³), rr:
−i(∂_r + 3/(2r))H_rr, vθ: −i(∂_r H_vθ + H_vθ/(2r) + μ0 H_rθ/r³), rθ: −i(∂_r + 1/(2r))H_rθ, tangential: −i(∂_r −
1/(2r))H_AB; Pol_v = −(1/2)(F H_rr + r⁻² tr_σ H), Pol_r = H_rr, Pol_θ = H_rθ.

(c) *Pol^+ (N2).* At a point, in a Euclidean-orthonormal Cartesian frame (which carries the Euclidean structure of
the Cartesian (τ, x) that Lemma 6.2 (i) names), for V = (V_v, V_r, V_θ, 0, 0): Pol^+ V has vv = V_r/4, vr = −V_r/2,
rr = V_r, trace −V_r − 2V_v, vθ = −V_θ/2, rθ = V_θ. Pol Pol^+ = 1, and Pol^+ V is Frobenius-orthogonal to the kernel
directions dv dv and dv dr + dr dv. The tangential part V_θ reaches none of vv, vr, rr, trace: the isotropy group O(3)
of the point leaves no invariant pairing of a tangential covector with the (v, r) plane (Schur).

(d) *H_1 and H_2 (N3, for every angular pair a(θ), b(θ) and every envelope).* H_1 is polarized and transported; D_X
H_1 = A env r^(−3/2) τ dθ with τ := ((a − b) − 3(a + b) cos 2θ)/sin 2θ − (a + b)' = (div_σ T)_θ; R_X(H_1) has no vv,
vr, rr, vθ component. The solution of (3.1) at j = 1 is

    H_2: rθ = i A env τ r^(−3/2),  vθ = i A env τ r^(−1/2) β(r),  β := −1/(2r0) + (μ0/3)(r⁻³ − r0⁻³),
         AB = −i r^(1/2) ∫_(r0)^r s^(−1/2) R_X(H_1)_AB ds,  vv = vr = rr = 0,                                  (3.2)

checked in all fifteen components of T(H_2) + R_X(H_1) = 0, all five of i Pol(H_2) + D_X H_1 = 0, and against the
data i Pol^+(D_X H_1) at r0 (control: β without its mass term violates the vθ equation). **H_1 and H_2 lie in S.**

(e) *The scalar part of H_3 (N4).* D_X H_2 = i A env d (r^(−5/2) β(r), r^(−7/2), ·, 0, 0) with d := (cos θ sin θ)⁻¹ ∂_θ
(cos θ sin θ τ) = div_σ div_σ T, and R_X(H_2) has zero vv component and zero trace ((b), H_2 ∈ S). The gauge
(i Pol(H_3) = −D_X H_2: H_rr = i(D_X H_2)_r, H_vr = (1/2) tr H + i(D_X H_2)_v), the trace transport (r^(3/2) tr H
constant along ℓ) and the vv transport, with the data i Pol^+(D_X H_2) at r0, determine (vv, vr, rr, tr) of H_3; they
satisfy T(H_3) + R_X(H_2) = 0 in vv, vr, rr and trace (the vr and rr equations are consistency checks: they hold
because the gauge propagates), and i Pol(H_3) + D_X H_2 = 0 in v and r (control: H_3,vv transported without the
mass coupling 2μ0 H_vr/r³ violates the vv equation). In closed form, Q := r^(3/2) H(∂_v, g0⁻¹ dr) =
r^(3/2)(H_vv + F H_vr) obeys ∂_r Q = i F ∂_r(r^(3/2)(D_X H_2)_v), and at r_h = √μ0, where F = 0, Q = r_h^(3/2) H_vv.

(f) *The horizon value (N5).* H_3,vv(v, √μ0, θ) = A env(v) d(θ) K(r0) with K as in (0.2). Equivalently K =
−r_h^(−3/2) β(r_h)²: minus the square of the horizon value of H_2's vθ radial factor β. K < 0 except at
ρ* (the one real root of 2ρ³ − 3ρ² − 2, double in K, K'' ≠ 0 there), and K → −μ0^(−7/4)/9 as r0 → ∞, the value for
data at past null infinity (the clean incoming wave). Control: a transverse angular tensor, (a, b) = ((1 + 3 cos 2θ)/2,
(1 − 3 cos 2θ)/2), has τ = 0, so d = 0 and no signal.

**Consequence (deduced from L.1, L.2).** On the boundary, the first-degree part of k(Φ0♯, Φ0♯) is λ³ Re[H_3,vv
e^(iv/λ)] + O(λ⁴ ε_M) + O(ε_M² λ³ ε_M): the λ and λ² parts vanish because H_1, H_2 ∈ S, and the shifts r_q − √μ0 and β0
are of degree 2.

## 4. The angular factor (computed, N6)

For the record's wave (h(ζ) = √(2/(1 + ζ²)), ζ = cos 2θ; a = 2p1, b = 2p2 per quadrature), exactly,

    d^F = √2 P(ζ)/(1 + ζ²)^(5/2),   d^G = √2 P(−ζ)/(1 + ζ²)^(5/2),   P(ζ) := −2ζ⁵ − (20/3)ζ³ − (20/3)ζ² − (38/3)ζ + 4/3,

d = d^G − i d^F. P has one root in [−1, 1] (ζ ≈ 0.0995) and gcd(P(ζ), P(−ζ)) = 1, so |d|² = (d^F)² + (d^G)² > 0 at
every angle, the axes included (P(±1) ≠ 0). One quadrature alone vanishes at one angle (the control): the two
quadratures a quarter turn apart are what make the signal nonzero everywhere. (By hand: a common root of P(ζ) and
P(−ζ) is a common root of the even part 4/3 − (20/3)ζ² and the odd part −ζ(2ζ⁴ + (20/3)ζ² + 38/3), and there is none.)

## 5. Flat-edge bounds and the weighted remainder

**Lemma L.3 (flat-edge bounds of the construction; deduced, sketch).** For every i there are M, C (depending on N,
i, the construction, not on λ or v) such that at every X ∈ Ω with v(X) ≤ v_s + 1: (a) every profile of the approximant
and its (X, θ)-derivatives of order ≤ i are bounded by C ε_M(v(X)), and their parts of degree ≥ 2 by C ε_M(v(X))²;
(b) the profile ρ_N of the residual, Ric^H(g_app) = λ^N [ρ_N], obeys the same bound; (c) on Σ_τ0 the correction U of
Proposition 6.5 at radius r obeys |∂^i U| ≤ C λ^(N−2−i) ε_M(τ0 + r).

*Proof (sketch).* Induction over the stages of Lemma 5.3, every one of which vanishes for v < v_s (EQUALITY5 section 0).
Data on Σ_τ0 (Lemma 6.2): χ, φ_m, (m_m)_(τ·) are zero; ĝ_(m+1) and d_τ(m_m)_(τ·) are pointwise in known quantities;
(h_m, Q_m) and U solve Lemma 6.4's evolution in r from zero data at r = a, whose solution on [a, r] is the solution of
the problem posed on [a, r] (uniqueness), bounded by the sources on [a, r] alone (Lemma 6.4's bound with R := r; the
contraction of Proposition 6.5 run on [a, r] with the same constants); on Σ_τ0, r' ≤ r is v' ≤ v. Transports run along
ℓ, at fixed v. The wave equations for the means: on Ω_v := Ω ∩ {v' ≤ v} the face {v' = v} is null for g0 with Ω_v to its
past, so its flux is nonnegative and is dropped (the argument of Proposition E.2), and Lemmas 2.3–2.4 bound the solution
on Ω_v by its data and sources there; commuted derivatives and Sobolev's embedding on the Ω_v (uniformly Lipschitz for v
∈ [v_s, v_s + 1]) [round 2, R2.0 (C3): read slice by slice this fails near r = a; replaced in R2.3] give the pointwise
form, each derivative of a source costing derivatives of env (M grows with N and i). Products of first-degree factors
give the degree-2 bounds; μ(v) − μ0 ≤ C ε_0². ∎

**Lemma L.4 (the weighted remainder; deduced, sketch).** Put ε := 2C1 λ (C1 of EQUALITY5 section 0, |g_λ⁻¹ − g0⁻¹| ≤ C1
λ). For v1 ≤ v_s + 1 with ε_M(v1) ≤ λ^6 and every point X of Ω with v(X) + ε(τ(X) − τ0) ≤ v1 and r(X) ≥ r_q(v(X)),

    |w(X)| ≤ C λ^(N−6) ε_M(v1).

*Proof (sketch).* R := Ω ∩ {v + ε(τ − τ0) ≤ v1}. Its lateral face has conormal dv + ε dτ, timelike for g_λ: g_λ⁻¹(dv + ε
dτ, dv + ε dτ) ≤ −2ε − ε²(1 + μ/r²) + C1 λ (1 + ε)² [R2.0 (C2): C1 λ ((1 + ε)² + 1)] < 0; v + ετ increases along future
causal curves of g_λ, so R lies to the past of the face and its flux is dropped; R does not meet the outer face of Ω,
and its slices {a ≤ r ≤ v1 − ε(τ − τ0) − τ} have outer radii decreasing in τ. From the quasilinear form (supplement
(0.2)), −(1/2) g_λ^ab ∂_a ∂_b w = −Ric^H(g_app) + (1/2)(g_λ^ab − g_app^ab) ∂_a ∂_b g_app − [Q(g_λ)(∂g_λ, ∂g_λ) −
Q(g_app)(∂g_app, ∂g_app)], whose last two terms are bounded by C(|w| + |∂w|) on R because |∂² g_app| ≤ C(1 + λ⁻¹
ε_2(v1)) ≤ C there (Lemma L.3 (a); the one large coefficient of the supplement's section 5.1 is λ⁻¹ times the wave's
amplitude, which is small on R). The energy inequality of the supplement's Lemma 2.3 with gt := g_λ, run on R, Gronwall,
and the same for ∂^i w, i ≤ 3 (the commutators carry ∂^j g_λ, j ≤ 4, bounded on R: |∂^j g_app| ≤ C(1 + λ^(1−j) ε_j(v1))
≤ C, and |∂^j w| ≤ C λ^(K−2−j) [R2.0 (C1): λ^(K−3−j)] for j ≤ 4 by Theorem E and Lemma 2.1; the term w ∂^(i+2) g_app is
≤ C|w| on R because λ^(−i−1) ε_(i+2)(v1) ≤ 1), bound w in H^4 of the slices of R by the data of w on Σ_τ0 ∩ R (Lemma L.3
(c), four derivatives: C λ^(N−6) ε_M(v1)) and ∫ ‖∂^i Ric^H(g_app)‖ (L.3 (b): C λ^(N−3) ε_M(v1)). The slice through X has
width at least r_q − a ≥ δ0, so Sobolev's embedding (supplement Lemma 2.1) has a uniform constant. ∎

## 6. The window

**Lemma L.5 (interpolation on a half-line; deduced, standard; W1).** Let f be smooth on R, f = 0 on (−∞, v_s], m ≥ 2,
E(v) := sup_(v' ≤ v) |f|, M_m(v) := sup_(v' ≤ v) |f^(m)|. For 0 < i < m and v > v_s,

    sup_(v' ≤ v) |f^(i)(v')| ≤ C_(i,m) E(v)^(1 − i/m) M_m(v)^(i/m),      C_(i,m) := Λ_(i,m) + (m − 1)^(m − i),

Λ_(i,m) := Σ_k |l_k^(i)(0)| for the Lagrange basis on the nodes 0, −1, …, −(m − 1). *Proof.* For u ≤ v and h > 0 let
P interpolate f at u, u − h, …, u − (m − 1)h, all in (−∞, v]: |P^(i)(u)| ≤ Λ_(i,m) E h^(−i); f − P has m zeros in an
interval of length (m − 1)h and (f − P)^(m) = f^(m), so (Rolle, m − i integrations from zeros) |(f − P)^(i)(u)| ≤
M_m ((m − 1)h)^(m − i); take h = (E/M_m)^(1/m). ∎ W1 checks the inequality for exp(−1/x) at three (i, m) with these
constants, and that the bound by E alone (no interpolation) fails at the edge, f'/f = 1/x².

**Lemma L.6 (levels; deduced; W2).** For 0 < y < E(v_s + 1) put v*(y) := min{v : E(v) = y}; then env(v*) = y and E <
y before v*. If L C_(1,m) (2y)^(1 − 1/m) M_m^(1/m) ≤ y/4 (M_m := sup |env^(m)|), then on [v*, v* + L] env lies in [3y/4,
5y/4], E ≤ 5y/4, and ε_M(v* + L) ≤ C y^(1 − M/m) (Lemma L.5). Moreover v* − v_s ≥ (y/C_κ)^(1/κ) for every κ, C_κ :=
sup |env^(κ)|/κ! (Taylor's formula at v_s, where env is flat). *Proof.* E is continuous and nondecreasing with E(v_s) =
0; by Lemma L.5, |env'| ≤ C_(1,m)(2y)^(1−1/m) M_m^(1/m) as long as E ≤ 2y, so env moves by at most y/4 on [v*, v* + L],
which keeps E ≤ 5y/4 (continuity). ∎ No regularity of the edge is used: W2 runs it for exp(−1/x), exp(−1/x²) and
exp(−1/x) sin²(π/x), whose zeros accumulate at the edge.

## 7. Proof of Theorem L

Fix p := 14, M from Lemmas L.3–L.4 (with i ≤ 4) [R2.0 (C4): M = M* := 2N + 8], m := 56 M, κ := 64, y := λ^p, v* :=
v*(y), W_λ := [v*, v* + 4πλ], v1 := v* + 4πλ + ε(τ_end − τ0) = v* + O(λ), L := v1 − v*. For λ small the hypothesis of
Lemma L.6 holds (λ ≪ y^(1/m)), so on [v*, v1] env ∈ [3y/4, 5y/4] and ε_M(v1) ≤ C y^(1 − M/m) ≤ λ^6 (Lemma L.4's
hypothesis).

*Every point of W_λ is in the layer:* μ(v1) − μ0 ≤ (2/9) A² (v1 − v_s)(5y/4)² ≪ λ, while μ(v_s + η_λ) − μ0 = μ0((1 + 2C_Φ
λ)² − 1) ≥ 4 μ0 C_Φ λ; μ is nondecreasing, so v1 < v_s + η_λ.

*The expansion.* At X = (v, r_q(v), ω), v ∈ W_λ, Lemma L.1 with k = Σ λ^j [g_j] + w, Proposition L.2 and Lemmas L.3–L.4
give k(Φ0♯, ·) = O(λ² ε_M + ε_M² + |w|) (the first-degree λ¹ part W(∂_v, ·) is zero; λ² H_2(∂_v, ·) is not), so q =
O(λ⁴ ε_M² + ε_M⁴ + |w|²), and

    −k(Φ0♯, Φ0♯) = −λ³ A env K Re[d e^(iv/λ)] + O(λ⁴ ε_M) + O(λ ε_M²) + O(λ^(N−6) ε_M(v1)),
    0 ≤ m0 ≤ C (E(v)² + ∫_(v_s)^v env²) ≤ C y²,

the O(λ ε_M²) collecting the degree ≥ 2 parts of λ[g1] = λ(m1 + χ dv² + W(θ + φ1)) and of the higher profiles, and
the shifts r_q − √μ0, β0 = O(ε_M²). With ε_M ≤ C y^(1 − M/m) this is (0.1) with

    |ρ_λ| ≤ C (y² + λ⁴ y^(1 − M/m) + λ y^(2(1 − M/m)) + λ^(N−6) y^(1 − M/m)).

*Domination.* Case (v_s − τ0)/√μ0 ≠ ρ*: K(v − τ0) is continuous and K(v_s − τ0) ≠ 0, so |K| ≥ K_* > 0 on W_λ for λ
small, and the signal's amplitude is at least λ³ (3y/4) K_* d_*, d_* := min |d| > 0 (section 4). The exponent
conditions (e1) 2p > 3 + p, (e2) pM/m < 1, (e3) p(1 − 2M/m) > 2, (e4) N − 6 − 3 > pM/m, (e5) p/m < 1, (e6) p(1 − M/m)
> 6 hold for p = 14, m = 56 M once N ≥ 10, i.e. K ≥ 7 (W3, exact; control: N = 9 violates (e4)), so δ(λ) → 0. Case
(v_s − τ0)/√μ0 = ρ*: K(v − τ0) = (K_ρρ(ρ*)/(2μ0))(v − v_s)²(1 + o(1)) with K_ρρ(ρ*) ≠ 0 (N5; K as a function of
ρ) and v − v_s ≥ v* − v_s ≥ (y/C_κ)^(1/κ) (Lemma L.6), so the amplitude is at least c λ³ y^(1 + 2/κ); the conditions
with 3 + p replaced by 3 + p(1 + 2/κ) hold as well (W3).

*Sign change.* e^(iv/λ) turns twice on W_λ. At every ω, at the points of each half of W_λ where Re[d e^(iv/λ)] sgn(−K)
= |d|, (0.1) gives g_λ⁻¹(dΦ0, dΦ0) ≥ λ³ (3y/4)|K||d|(1 − δ(λ)) > 0: timelike; where it is −|d|, the value is < 0:
spacelike. ∎

## 8. Labels, sources and what is open

- L1 (computed, N0): the inverse identity. L2 (computed, N1–N5, exact for every angular profile and envelope; (a)
  deduced): the first-degree profiles, H_1, H_2 ∈ S, the horizon value A env d K. L3 (computed, N6): d for the record's
  wave, nonzero at every angle. L4 (computed, W1; deduced, standard): Lemma L.5. L5 (computed as a model with unit
  constants, W2; exact ledger, W3): the window's arithmetic. L6 (deduced, sketch): Lemmas L.3, L.4. L7 (deduced):
  Theorem L, Corollary L.7.
- READ: `EQUALITY5.md` (0.1)–(0.2), Lemma E.1, Propositions E.2–E.4, Remark E.6; the paper sections 2.4–2.5, 3, 4,
  Theorem 1, Proposition 3.2; the supplement `N1STAR-PROOF.md` sections 0.2–0.4, 2 (Lemmas 2.1, 2.3, 2.4), 3.1–3.2, 5
  (Lemmas 5.1–5.3, 5.4), 6 (Lemma 6.2, Lemma 6.4, Proposition 6.5).

Open items.

- O1 *The very edge.* For fixed λ and v − v_s ≲ λ^(1/2), the λ-expansion of the first-degree term breaks down (the
  envelope varies faster than the phase) and the highest stages and the correction U dominate it; the sign there is
  not computed. Theorem L does not need it: its window lies at v* − v_s ≥ (λ^p/C_κ)^(1/κ) ≫ λ^(1/2).
- O2 *Lemmas L.3, L.4 and L.2 (a)* are written as sketches over the supplement's lemmas (Sobolev on the Ω_v; the
  restriction of Lemma 6.4 and Proposition 6.5 to [a, r]; the degree bookkeeping of Lemma 5.3). An independent reading
  is the next step.
- O3 *Theorem 2's solution* (data from past null infinity): its first-degree profiles are the clean ones, for which
  N5 gives K = −μ0^(−7/4)/9 ≠ 0 at every r0, so the same conclusion would follow from the analogues of L.3–L.4 on the
  past domain P; these are not written.
- O4 *Constants.* λ_L is not evaluated; K ≥ 7 is what the ledger uses (N − 6 ≥ 4), not a sharp threshold. The size
  of the timelike margin is λ³ A env ≤ λ^17 on W_λ.
- O5 *The convention of Pol^+.* Lemma 6.2 (i) states that its Euclidean structure is O(4)-invariant; among the
  natural products on symmetric arrays only the Frobenius Σ_ab Y_ab Z_ab is, and N2 uses it. A different choice of
  the oscillating stage data changes K (not the vanishing of the λ, λ² parts, which (c) of Proposition L.2 makes
  independent of any isotropic choice); it was not pursued.

Files: this note; `checks/layerlin5.py` (+ `.out`, about five minutes); `checks/layerwin5.py` (+ `.out`, about a minute).

## Round 2

Status: written (round 2); not yet read by an independent verifier. New check scripts, all pass, every control fails
(`.out` files beside them): `checks/layerdeg5.py` D1–D5, `checks/layernull5.py` E1–E6, `checks/layerpast5.py` P1–P3,
`checks/layerledger5.py` L1–L4 (computed). Round 1's `layerlin5` N0–N6 and `layerwin5` W1–W2 are used as they stand;
W3 is superseded by L1. Round 2 writes Proposition L.2 (a) and Lemmas L.3, L.4 at proof level (R2.2–R2.5), carries
Theorem L to Theorem 2's solution (O3, R2.7), and checks the paper at equality (R2.8). Round 1's text is kept; the
three places where it is wrong or has a gap carry a bracketed pointer to R2.0.

### R2.0 Results, and corrections to round 1

1. **Proved (deduced):** Proposition L.2 (a), Lemma L.3 and Lemma L.4 (R2.3–R2.5), on three tools, Lemmas L.8–L.10
   (R2.2), which run the supplement's energy and transport lemmas on the past sets Ω_v := Ω ∩ {v' ≤ v} and keep the
   flux through their null face {v' = v} instead of dropping it. Every identity and inequality they use is computed
   (the table in R2.9).
2. **Improved:** L.4 now gives |w| ≤ C λ^(N−5) ε_(M*)(v1) under ε_(M*)(v1) ≤ λ³, M* := 2N + 8, so Theorem L holds for
   **K ≥ 6**, that is for every metric of Theorem 1 (round 1: K ≥ 7; layerledger5 L1, L4).
3. **O3 closed (deduced, R2.7):** Theorem L holds for Theorem 2's solution with K(v − τ0) replaced by the constant
   K∞ = −μ0^(−7/4)/9, computed here directly from the transports with nothing coming in (layerpast5 P1–P3), not as a
   limit r0 → ∞; there is no exceptional case.
4. **The paper (R2.8):** Corollary L.7 contradicts no statement of the paper; the paper's section 9 sentence that in the
   layer the causal character "is not decided ... which is why the expansion cannot decide the layer" is superseded.
   The replacement wording is the block "Proposed paper text".

Corrections to round 1 (each marked at its site):

- (C1) Section 5, proof of L.4: "|∂^j w| ≤ C λ^(K−2−j) for j ≤ 4 by Theorem E" is wrong by one power. Theorem E
  (supplement section 4, Step 1) gives C M λ^(K−3−j). Round 2's proof needs j ≤ 3 only, bounded once K ≥ 6.
- (C2) Section 5, proof of L.4: the perturbation term in g_λ⁻¹(dv + ε dτ, dv + ε dτ) is C1 λ ((1 + ε)² + 1), the
  Euclidean norm of α = (1 + ε) dτ + x̂·dx in Cartesian components, not C1 λ (1 + ε)². The conclusion stands (E3).
- (C3) Section 5, proof of L.3: "Sobolev's embedding on the Ω_v", read slice by slice as the supplement's Lemma 2.1
  is, fails: Ω_v ∩ Σ_τ = {a ≤ r ≤ v − τ} is arbitrarily thin as v − τ ↓ a, and L.4 needs pointwise bounds there.
  Round 2 needs no Sobolev inequality on those slices: the oscillating profiles are bounded by transport along ℓ, the
  means by the flux through the null face (Lemma L.10).
- (C4) Section 7 used a derivative count M from L.3–L.4 without a value. Round 2's counts are explicit: M* = 2N + 8.

### R2.1 Conventions, and two structural facts

*Notation.* Ω, Σ_τ, a, δ0 = q0 − a, b(τ), τ_end and V are those of the supplement's section 1; v_s := inf supp env with
v_s − τ0 > √μ0 + 1; v_♯ := v_s + min(1, T) ≤ V. On Ω ∩ {v ≤ v_♯} Ω's outer face is not met (there v = V + 1 + τ_end
− τ ≥ V + 1). As in round 1, ε_c(v) := Σ_(i≤c) sup_(v'≤v) |env^(i)(v')|, nondecreasing and zero on v ≤ v_s. A
profile has **cost c at order i** when |∂^α_(X,θ) f(X, θ)| ≤ C ε_c(v(X)) for |α| ≤ i (Cartesian ∂_X). Only ∂_v reaches
env: ℓ = ∂_r at fixed v, the rotations Ω_ab := x_a ∂_b − x_b ∂_a and ∂_θ cost nothing.

For v ≤ v_♯: Ω_v := Ω ∩ {v' ≤ v} and N_v := Ω ∩ {v' = v}. N_v is null for g0 (dv is null, Prop. 2.2 (c), READ) and
Ω_v lies to its past (v increases along future causal curves of g0, EQUALITY5 Lemma E.1 (d)). For X ∈ Ω, γ_X is the
integral curve of ℓ from X: in (v, r, ω) it is r ↦ (v(X), r, ω(X)), r ≥ r(X), and it meets Σ_τ0 at X_Σ := (v(X),
v(X) − τ0, ω(X)) inside Ω (supplement Lemma 1.1 (d), READ). v is constant along γ_X, so every bound weighted by
ε_c(v) holds with the same weight along the whole curve.

*Constants.* C depends on N, the order i, Ω (a, δ0, b(τ0), τ_end − τ0), μ0, A, finitely many global C^k norms of env,
the λ-independent bounds of Theorem A's profiles and of Lemma 6.2's stage data on Ω × S¹ (supplement 0.5, 5.4, 6.2,
READ: every profile is smooth on Ω × S¹ with all derivatives bounded independently of λ), and Theorem E's M and C1;
never on λ, v, v1 or the point.

*The construction (READ: supplement 5.1–5.4, 6.2–6.4).* Stage 0: W = W_TT + χ dv², gh_1 := W. Stage m = 1, ..., N:
the mean m_m, the phase φ_m, Ψ_m := □̃φ_m and Z_(m+1) := ∂_θ gh_(m+1) solve Lemma 5.3 (a)–(c) with Lemma 6.2's data:
φ_m = 0, (m_m)_(τ·) = 0, (h_m, Q_m) by Lemma 6.4 from zero data at r = a, d_τ(m_m)_(τ·) by (ii), and Z_(m+1) =
−Pol^+(Λ_m(h_m) + known) on Σ_τ0. Lemma 6.2's proof fixes the data of stages 1, ..., N − 1; stage N's are taken by the
same rule (any rule pointwise or radial in the earlier stages and vanishing where they do serves below; EQUALITY5
section 0 already assumes that every stage vanishes for v < v_s).

*Two structural facts (deduced; READ Lemmas 5.1–5.3, 6.1–6.2; computed D1, D2).*

(F1) Every monomial of the source −Π_osc(Wm(m_m, φ_m) + K_m) of Lemma 5.3 (c), and of "known" in Lemma 6.2 (i),
contains an oscillating factor among W, χ, gh_l (l ≤ m), carrying at most two derivatives in (c) and one in "known";
its other factors are profiles of Theorem A, bounded globally, or coefficients built from g0. (A monomial with no
oscillating factor does not depend on θ, and Π_osc removes it.)

(F2) Every monomial of the mean sources (S̄m_m, q_m, ⟨Th gh_(m+1)⟩ and the coefficient of dφ_m in ⟨Wm_φ⟩), of the
slice sources (S_m and the coefficient of B_m), of the residual Ric^H(g_app) − Ric(g0) and of the constraint map
Φ(γ, K) − Φ(g0's data) contains two oscillating factors, or a factor among the means and phases of the earlier stages,
μ − μ0 and μ^(k), k ≥ 1. For: every oscillating factor has θ-mean zero, so the θ-mean of a monomial with exactly one
oscillating factor vanishes (D2); and each source is a polynomial in the profiles and in μ − μ0, μ^(k), with
coefficients built from the seed, whose constant term is the seed's own value of that source, zero (at A = 0 the
construction returns the seed). For ⟨Th gh_(m+1)⟩ more is true: by D1 the seed's fast operator on the k-th harmonic is
k T, so Th_0 (the seed part of Th) is an operator in X composed with ∂_θ, of θ-mean zero on every profile, and
⟨Th gh_(m+1)⟩ = ⟨(Th − Th_0) gh_(m+1)⟩, whose coefficients are built from W, χ, m_1, φ_1 and μ − μ0.

The μ-factors are weighted at every point: 0 ≤ μ − μ0 ≤ (2/9) A² (v − v_s) ε_0(v)², |μ^(k)| ≤ C ε_(k−1)(v)².

### R2.2 Three tools

**Lemma L.8 (energy on Ω_v, the null face kept; deduced: supplement Lemma 2.3, READ; E1, E2).** Let v ≤ v_♯ and let
u, a function or a Cartesian array, satisfy −½ g0^(ab) ∂_a ∂_b u = f on Ω_v. Put e(τ) := ‖∂u(τ)‖ + ‖u(τ)‖, flat L²
norms on Σ_τ ∩ Ω_v, and F_v(u) := ∫_(N_v) T(L0, Y) r³ dr dω, with T the energy tensor of u for g0, Y := −g0⁻¹ dτ and
L0 = −ℓ. Then

    sup_(τ0≤τ≤τ_end) e(τ) + F_v(u)^(1/2) ≤ C_E ( e(τ0) + ∫_(τ0)^(τ_end) ‖f‖ ),                                (R2.1)

C_E depending on Ω and μ(v_end) only, not on v; and T(L0, Y) = ½ (1 + μ/r²)(ℓu)² + |∇̊u|²/(2r²) (E1).

*Proof.* Run the proof of Lemma 2.3 on Ω_v ∩ {τ0 ≤ τ' ≤ τ} with g̃ := g0 and J := T(Y, ·). Its boundary is Σ_τ0 ∩
Ω_v, Σ_τ ∩ Ω_v, part of {r = a} (spacelike with Ω_v to its past, Lemma 1.1 (b): flux ≥ 0, dropped) and part of N_v.
In (v, r, ω) the volume form is r³ dv dr dω (E1) and N_v's outward conormal is dv, so its outward flux is ∫ J(dv) r³
dr dω = ∫ T(ℓ, Y) r³ dr dω = −∫ T(L0, Y) r³ dr dω. Moved to the left it is the part of F_v(u) with τ' ≤ τ, and E1
computes its density: no transverse derivative ∂_v u enters, and it is nonnegative. The bulk is at most C (e² + ‖f‖ e)
as in Lemma 2.3, and d_τ ‖u‖² = 2⟨u, ∂_τ u⟩ − ∫_(r=v−τ) |u|² r³ dω, the outer radius v − τ decreasing at rate one
(E2). Gronwall's lemma, then τ = τ_end for the flux. The constant is Lemma 2.3's, which depends on the bounds of g0
and Y on Ω only. ∎

**Lemma L.9 (transport; deduced: supplement Lemma 2.4, READ; E2, D4).** (a) If L0 φ − c φ = f on Ω_v with c bounded,
then ‖φ(τ)‖ ≤ e^(C(τ−τ0)) (‖φ(τ0)‖ + ∫_(τ0)^τ ‖f‖), norms on Σ_τ ∩ Ω_v. (b) Let Z(X, θ) ∈ R^d solve −(ℓ·∂_X) Z +
𝓜 Z = F on Ω × S¹, with 𝓜(X) a linear operator on C(S¹; R^d) of norm at most M1. Then for X ∈ Ω

    sup_θ |Z(X, ·)| ≤ e^(M1 L) ( sup_θ |Z(X_Σ, ·)| + L sup_(γ_X × S¹) |F| ),      L := r(X_Σ) − r(X) ≤ b(τ0) − a.

The derivatives (∂^α_X ∂_θ^p Z)_(|α|+p≤i) solve a system of the same kind (the commutator of ∂_X with ℓ·∂_X is
(∂ℓ)·∂_X, of the same order), with data on Σ_τ0 the tangential derivatives of Z|_(Σ_τ0) and the transverse ones from
the equation (dτ(ℓ) = −1).

*Proof.* (a) is Lemma 2.4's proof with outer radius b(τ) := v − τ: its outer boundary term carries the factor 1 + b' =
0 (E2), since L0 is tangent to N_v. (b) In (v, r, ω), ℓ = ∂_r and γ_X is r ↦ (v(X), r, ω(X)), so the equation is a
linear ordinary differential equation in r on the Banach space C(S¹; R^d): Gronwall's lemma. ∎

For the stage transports, 𝓜 := (Mm − ⟨Mm ·⟩) ∂_θ⁻¹ on zero-mean profiles (Lemma 5.2, READ: Mm algebraic in X and of
first order in θ). ‖∂_θ⁻¹‖ ≤ π on zero-mean C(S¹) (D4) and ‖Π_osc‖ ≤ 2, so ‖𝓜‖ ≤ C by Theorem A's global bounds.

**Lemma L.10 (pointwise bounds from the null face; deduced: E1, E5; Sobolev on S³ as in the supplement's Lemma 9.3
(a), READ).** For u smooth on Ω_v and Y ∈ N_v,

    |u(Y)| ≤ C_N Σ_(|β|≤2) ( sup_(N_v ∩ Σ_τ0) |Ω^β u| + F_v(Ω^β u)^(1/2) ),                                     (R2.2)

Ω^β products of the rotations, C_N depending on a and b(τ0) only.

*Proof.* In (v, r, ω), γ_Y runs in N_v from r(Y) ≥ a to r_Σ := v − τ0, and the rotations commute with ℓ = ∂_r. On S³,
|u(r, ·)|_∞ ≤ C Σ_(|β|≤2) ‖Ω^β u(r, ·)‖_(L²(S³)) (H² ⊂ L^∞ in dimension three, the rotations spanning every tangent
space; the argument of Lemma 9.3 (a)), and ‖Ω^β u(r, ·)‖ ≤ ‖Ω^β u(r_Σ, ·)‖ + ∫_r^(r_Σ) ‖ℓ Ω^β u(r', ·)‖ dr' ≤ C sup
|Ω^β u|_(r_Σ) + (r_Σ − a)^(1/2) a^(−3/2) (∫∫ (ℓ Ω^β u)² r'³ dr' dω)^(1/2), the last double integral at most 2 F_v(Ω^β u)
by E1. ∎

Why the null face and not the slices: Ω_v's slices are thin near r = a (C3), and N_v ∩ Ω is not: its r-extent is v −
τ0 − max(a, v − τ_end) ≥ 1. The flux through N_v controls exactly the derivatives tangent to it (E1), which is what an
integration along γ_Y and a Sobolev inequality on the spheres need.

### R2.3 Lemma L.3, written in full

**Lemma L.3 (flat-edge bounds of the construction; deduced, with D1–D5, E1, E2, L3; this replaces round 1's sketch).**
Let N ≥ 3 (N = K + 3 for Theorem 1) and let H_j (1 ≤ j ≤ N + 1) be the first-degree profiles of (3.1): H_1 := A env
r^(1/2) T and, at the seed, T(H_(j+1)) = −R_X(H_j) along ℓ with H_(j+1) = i Pol^+(D_X H_j) at r0 = v − τ0 on Σ_τ0.
For every X ∈ Ω with v := v(X) ≤ v_♯ and every order i:

- (a) **oscillating, degree one:** |∂^i_(X,θ) gh_j(X)| ≤ C ε_(i+2j−2)(v), 1 ≤ j ≤ N + 1;
- (b) **means and phases, degree two:** |∂^i m_j(X)| + |∂^i φ_j(X)| ≤ C ε_(i+2j)(v)² and |∂^i Ψ_j(X)| ≤ C
  ε_(i+2j+2)(v)², 1 ≤ j ≤ N;
- (c) **oscillating, the remainder of degree two:** |∂^i_(X,θ)(gh_j − Re[H_j e^(iθ)])(X)| ≤ C ε_(i+2j)(v)², and |∂^i
  H_j(X)| ≤ C ε_(i+2j−2)(v), 1 ≤ j ≤ N + 1;
- (d) **residual:** |∂^i Ric^H(g_app)(X)| ≤ C λ^(N−1−i) ε_(i+2N+2)(v);
- (e) **slice data:** on Σ_τ0 at radius r with τ0 + r ≤ v_♯, the stage-m data (h_m, Q_m, d_τ(m_m)_(τ·)), with their
  angular and i radial derivatives, are at most C ε_(i+2m)(τ0 + r)², and the correction U of Proposition 6.5 obeys
  sup_(r'≤r) ‖∂_r^j U(r')‖_(H^s(S³)) ≤ C λ^(N−2−j) ε_(j+2N+2)(τ0 + r) for j ≤ 3 and Proposition 6.5's s.

Every cost that L.2 (a) and L.4 use, at orders i ≤ 4, is at most M* := 2N + 8 (computed: L3, which also checks the
closed forms of the costs from the recursion the proof below follows).

*Proof.* Induction on the stage m = 0, 1, ..., N. At stage m the steps run in the order (e) for the stage-m slice data,
(a) for gh_(m+1), (b) for (m_m, φ_m, Ψ_m), (c) for gh_(m+1); each uses only the global bounds of Theorem A and what the
earlier steps proved.

*Stage 0.* The Cartesian components of W_TT are A env(v) times smooth functions of (r, x̂, θ) (`ansatz5.py` A3,
`past5.py` P3, READ): cost i at order i. χ solves (∂_r + 3/(2r)) ∂_s χ = (the vv second harmonic of R^(0)[g0 + λW_TT])
along ℓ, zero on Σ_τ0 (supplement 5.1, READ). That source is quadratic in ∂_θ W_TT and W_TT, with no slow derivative:
the λ⁰ coefficient's quadratic terms come from Q(∂g, ∂g) with both derivatives fast, and the term (λ W)(λ⁻²∂_θ² W) of
the principal part is contracted with W(ℓ, ·) = 0. So L.9 (b) gives |∂^i χ| ≤ C ε_i(v)²: (a) and (c) at j = 1, since
gh_1 − Re[H_1 e^(iθ)] = χ dv².

*Stage m ≥ 1, (e).* (h_m, Q_m) solve Lemma 6.4's system on [a, R] (coefficients those of Lemma 6.3 at the approximant's
data, B_m a zeroth-order term) from zero data at r = a, with source S_m. Its restriction to [a, r] solves the same
problem on [a, r], whose solution is unique (Lemma 6.4 on [a, r]), and Lemma 6.4's bound holds on [a, r] with its
constant for [a, R]: the proof integrates an energy inequality in r from a, and Gronwall's lemma over a shorter
interval gives a smaller constant. By (F2) and the induction hypothesis, |∇̊^β S_m| ≤ C ε_(2m)(τ0 + r')² on the sphere
of radius r' (on Σ_τ0, v = τ0 + r' on that sphere, so angular derivatives cost nothing). Hence sup_(r'≤r)
(‖h_m‖_(H^(s+1)) + ‖Q_m‖_(H^s)) ≤ C ε_(2m)(τ0 + r)², pointwise by Sobolev on S³ (s > 7/2). Radial derivatives follow from
the equations, each costing one radial derivative of the sources, one env-derivative. d_τ(m_m)_(τ·) is algebraic in
these and in known quantities (Lemma 6.2 (ii)).

*(a).* Z_(m+1) solves L.9 (b)'s equation with the 𝓜 above and F := −Π_osc(Wm(m_m, φ_m) + K_m). By (F1) each monomial
of F has an oscillating factor among W, χ, gh_l (l ≤ m), with at most two derivatives, the other factors bounded
globally (m_m, φ_m, Ψ_m included): F has cost i + 2m at order i. Its data, −Pol^+(Λ_m(h_m) + known): Λ_m(h_m) is
bilinear in h_m (bounded globally) and ∂_θ W; "known" has an oscillating factor with at most one derivative (F1); Pol^+
is smooth and pointwise: cost i + 2m − 1. L.9 (b), commuted to order i, gives cost i + 2m = i + 2(m + 1) − 2.

*(b).* m_m solves −½ □̃ m_m + B̄·∂m_m + C̄ m_m = S̄m_m − ⟨Wm_φ(dφ_m)⟩ − ⟨Th gh_(m+1)⟩ (Lemma 5.3 (a), READ), a wave
equation with g0's principal part. Commute with ∂^α (|α| ≤ i) and Ω^β (|β| ≤ 2; the rotations are Killing for g0,
[Ω_ab, □̃] = 0, `past5.py` P6, READ). The sources: S̄m_m and q_m are at most C ε_(i+2m)(v)² by (F2) and the induction
hypothesis (two oscillating factors with at most two derivatives, cost i + 2m; earlier means with two derivatives,
cost i + 2m); ⟨Th gh_(m+1)⟩ = ⟨(Th − Th_0) gh_(m+1)⟩ is at most C ε_(i+2m)(v)² through its coefficients W, χ, μ − μ0
and (a), while its coefficients m_1, φ_1 give, at m = 1, terms linear in the stage's own unknowns and, at m ≥ 2, terms
of size ε²·ε; ⟨Wm_φ(dφ_m)⟩ is linear in dφ_m. The data on Σ_τ0 ∩ Ω_v are those of (e) and (m_m)_(τ·) = 0. Apply L.8 to
∂^α Ω^β m_m on Ω_(v') for each v' ≤ v, together with L.9 (a) for ∂^α Ω^β ∂φ_m (L0 ∂φ_m = −½ ∂(m_m(ℓ, ℓ) + q_m) +
[L0, ∂] φ_m, φ_m = 0 on Σ_τ0), and Gronwall's lemma: the energies and the fluxes F_(v')(∂^α Ω^β m_m)^(1/2) are at most
C ε_(i+2m)(v')². L.10 at every point of N_(v') then gives |∂^α m_m| ≤ C ε_(i+2m)(v')² there; every Y ∈ Ω with v(Y) ≤
v_♯ lies on N_(v(Y)). φ_m: L0 φ_m = −½ (m_m(ℓ, ℓ) + q_m) with φ_m = 0 on Σ_τ0, integrated along γ_Y, gives the same
bound. Ψ_m: its transport (Lemma 5.3's proof, READ: L0 Ψ_m − (2/r) Ψ_m = −½ □̃ σ_m − (1/r)(∂_τ + ∂_r) σ_m − (3/r²) ∂_r
φ_m, σ_m := m_m(ℓ, ℓ) + q_m), with data from φ_m's on Σ_τ0, uses two more derivatives of m_m: cost i + 2m + 2.

*(c).* Put δ_(m+1) := gh_(m+1) − Re[H_(m+1) e^(iθ)]. By D1 the seed's operators on one harmonic are exactly λ⁻¹ k T +
R_X and λ⁻¹ i k Pol + D_X (no λ⁻² part), so (3.1) is Lemma 5.3 (c) and Lemma 6.2 (i) with every coefficient at the seed
and every source cut to its part linear in the oscillating profiles; Pol Pol^+ = 1 (N2). Hence ∂_θ δ_(m+1) solves L.9
(b)'s equation with the seed's 𝓜_0 and the source

    −[Π_osc(Wm + K_m) − R_X^seed(Re[H_m e^(iθ)])] − (𝓜 − 𝓜_0) Z_(m+1),

whose bracket is R_X^seed(δ_m) + (R_X^(g0) − R_X^seed)(gh_m) + (the monomials of Π_osc K_m with two or more oscillating
factors) + Π_osc Wm(m_m, φ_m). By the induction hypothesis (c), (a), by (b) at stage m and |μ − μ0| ≤ C ε², each part is
at most C ε_(i+2m+2)(v)²; 𝓜 − 𝓜_0 has coefficients W, χ, m_1, φ_1, μ − μ0, so (𝓜 − 𝓜_0) Z_(m+1) is at most C ε². The
data differ by (Pol^+_(g0) − Pol^+_seed)(·) + Pol^+(Λ_m(h_m)) + Pol^+(D_X^seed δ_m + (D_X^(g0) − D_X^seed) gh_m +
monomials with two oscillating factors), at most C ε² by (e). L.9 (b): cost i + 2m + 2 = i + 2(m + 1). The bound on
H_(m+1) itself is the proof of (a) with the seed's coefficients.

*(d).* Ric^H(g_app) is F(X, λ, θ) at θ = v/λ, F := λ⁻² A_2 + λ⁻¹ A_1 + A_0 the two-scale operator on the profile of
g_app. F − Ric(g0) =: F_p is a smooth function of λ ∈ [0, λ0] and of finitely many jets of the profiles, vanishing when
they vanish: A_2 carries g_app⁻¹(dv, dv) ∂_θ² (·), A_1 carries ∂_θ, both only on profiles (g0⁻¹(dv, dv) = 0), and
Ric(g0) = (3μ'/(2r³)) dv² is the only monomial free of profiles. Section 5.4 (READ) gives ∂_λ^n F = 0 at λ = 0 for n ≤
N − 2 ((E3) with K = N − 1). So F = λ^(N−1) ((N − 2)!)⁻¹ ∫_0^1 (1 − s)^(N−2) ∂_λ^(N−1) F_p(X, sλ, θ) ds, and by the
mean value theorem in the jets, with (a), (b) for profiles up to gh_(N+1), m_N, φ_N and two derivatives, the integrand
is at most C ε_(2N+2)(v). Each derivative of [·] costs λ⁻¹ through ∂_θ and one more env-derivative (D5).

*(e) for U.* On [a, r] with τ0 + r ≤ v_♯: the source −Φ(γ, K) of Proposition 6.5's problem has profiles that vanish
below order N − 2 (Lemma 6.1, READ), so, by Taylor's formula in λ as in (d) (Φ(γ, K) − Φ(g0's data) vanishes with the
profiles) and by (F2), (a), (b), sup_(r'≤r) ‖Φ(γ, K)(r')‖_(H^s) ≤ C λ^(N−2) ε_(2N+2)(τ0 + r) (angular derivatives
free on Σ_τ0). Run Proposition 6.5's iteration on [a, r]: its inputs are Lemma 6.4 on [a, r]
(constant at most that of [a, R]) and the coefficient bounds, restrictions of those on [a, R]. The iterates stay in the
ball of radius 2C0 λ^(N−2) ε_(2N+2)(τ0 + r) of X_s([a, r]) (the quadratic remainder is at most C λ⁻¹ (2C0 λ^(N−2) ε)² ≤
C0 λ^(N−2) ε for λ small, N ≥ 4) and contract in X_(s0)([a, r]). The limit and the restriction of Proposition 6.5's U
both solve the problem on [a, r] and lie in the ball of radius 2C0 λ^(N−2), where Proposition 6.5's difference
estimate gives uniqueness: they coincide. The r-derivatives come from the equations, each costing at most λ⁻¹
(Proposition 6.5, READ) and one env-derivative. ∎

### R2.4 Proposition L.2 (a), written in full, and the expansion on the boundary

**Proposition L.2 (a) (identification; deduced, with D1, D2, D5, layerlin5 N1–N2, Lemma L.3).** For X ∈ Ω with v :=
v(X) ≤ v_♯ and 1 ≤ j ≤ N, the fixed-phase profiles g_j of (0.4) satisfy

    |∂^i_(X,θ) (g_j − Re[H_j e^(iθ)])(X)| ≤ C ε_(i+2j)(v)²,                                                      (R2.3)

H_j of (3.1). That is: the part of first degree of Σ_j λ^j [g_j] is Re Σ_j λ^j H_j e^(iv/λ), and the rest is of degree
two in the quantitative sense (R2.3).

*Proof.* (i) *(3.1) is the first-degree system.* D1 computes, for every component and every harmonic k, that the seed's
linearized Ric^H on H e^(ikv/λ) is exactly λ⁻¹ k T(H) + R_X(H), with no λ⁻² part and R_X independent of k, and its
linearized D is λ⁻¹ i k Pol(H) + D_X(H). So the order-m coefficient of the two-scale expansion, restricted to the terms
linear in the oscillating profiles and with the seed's coefficients, is Re[(T(H_(m+1)) + R_X(H_m)) e^(iθ)] (Lemma 5.1's
Th gh_(m+1) and the part of K_m linear in gh_m), and the order-m oscillating part of D is Re[(i Pol(H_(m+1)) + D_X
H_m) e^(iθ)]; Lemma 6.2 (i) solves the latter on Σ_τ0 by H_(m+1) := i Pol^+(D_X H_m), Pol Pol^+ = 1 (N2). This is
round 1's argument, now with D1 behind it. (ii) *The means and phases have no part of first degree*: Lemma L.3 (b),
which rests on (F2), that is on D2 (a θ-mean of a monomial with one oscillating factor vanishes) and on D1 (⟨Th_0 ·⟩ =
0). (iii) *The fixed-phase rewriting* (supplement 5.4, READ): g_j is the λ^j coefficient of the means and of Σ_l λ^l
gh_l(X, θ + φ_1 + λΨ), Ψ := Σ_(i≥2) λ^(i−2) φ_i, so g_j = m_j + gh_j(X, θ + φ_1) + T_j, T_j a sum of products of
∂_θ^p gh_l (p ≥ 1, l < j) with monomials of positive degree in φ_2, ..., φ_(j−1). By L.3 (b), |m_j|, |φ_i| ≤ C ε²;
by L.3 (a), |∂_θ^p gh_l| ≤ C ε; so |T_j| ≤ C ε³ and |gh_j(θ + φ_1) − gh_j(θ)| ≤ |φ_1| sup |∂_θ gh_j| ≤ C ε³; and
|gh_j − Re[H_j e^(iθ)]| ≤ C ε² by L.3 (c). The derivatives follow by Leibniz and D5, with costs at most i + 2j. ∎

**Corollary L.11 (the expansion on the boundary; deduced, with D3, layerlin5 N3, N5, Lemma L.1).** At X = (v, r_q(v),
ω), v_s < v ≤ v_♯, with ε := ε_(M*)(v) and θ := v/λ,

    −k(Φ0♯, Φ0♯) = −λ³ A env(v) K(v − τ0) Re[d(θ) e^(iθ)] + O(λ⁴ ε + λ ε² + |w(X)|),
    |k(Φ0♯, ·)| ≤ C (λ² ε + λ ε² + |w(X)|),     |k| ≤ C (λ ε + |w(X)|),     0 ≤ m0(v) ≤ C (ε_0(v)² + ∫_(v_s)^v env²),

the O(·) with constants as in R2.1.

*Proof.* Φ0♯ = ∂_v + β0 ∂_r with |β0| ≤ (μ − μ0)/(2μ0) + r_q μ'/(4μ0) ≤ C ε² (D3). k = Σ_j λ^j [g_j] + w, and by
(R2.3) Σ_j λ^j g_j = Σ_j λ^j Re[H_j e^(iθ)] + O(λ ε²). H_1, H_2 ∈ S (N3): H_1(∂_v, ·) = 0, H_2(∂_v, ∂_v) = 0 and
|H_2(∂_v, ·)| ≤ C ε. H_3,vv(v, √μ0, θ) = A env(v) d(θ) K(v − τ0) (N5), and |H_3,vv(v, r_q) − H_3,vv(v, √μ0)| ≤ sup
|∂_r H_3| (r_q − √μ0) ≤ C ε·ε² (L.3 (c); D3: 0 ≤ r_q − √μ0 ≤ (μ − μ0)/(4√μ0)). The orders λ^j, j ≥ 4, give C λ⁴ ε;
the β0-terms |β0|·|k| ≤ C ε² (λ ε + |w|). m0 is bounded by D3. ∎

### R2.5 Lemma L.4, written in full

**Lemma L.4 (the weighted remainder; deduced, with E3, E6, D5, L.3; this replaces round 1's sketch).** Let K ≥ 6 and
N = K + 3 (Theorem 1). Let C1 be such that |(g_λ⁻¹ − g0⁻¹)(α, α)| ≤ C1 λ |α|_e² on Ω for every covector α, |·|_e the
Euclidean norm of Cartesian components (EQUALITY5 section 0's C1, taken in this norm), and let λ be so small that s :=
C1 λ ≤ 1/2. Put ε := 2 C1 λ. Let v1 ≤ v_♯ with ε_(M*)(v1) ≤ λ³, and R := Ω ∩ {v + ε (τ − τ0) ≤ v1}. Then for every X ∈ R
with r(X) ≥ q0,

    |w(X)| ≤ C λ^(N−5) ε_(M*)(v1),                                                                              (R2.4)

C depending on the quantities of R2.1, Theorem E's M included, and not on λ, v1 or X.

*Proof.* **1. The region (E3).** R ⊂ Ω ∩ {v ≤ v1}, since τ ≥ τ0. Its face {v + ε(τ − τ0) = v1} has conormal α = dv + ε
dτ, with g0⁻¹(α, α) = −2ε − ε²(1 + μ/r²) and |α|_e² = (1 + ε)² + 1, so g_λ⁻¹(α, α) ≤ −2s + 4s³ − 4s²μ/r² < 0: α is
timelike for g_λ. α(Y) = 1 + ε(1 + μ/r²) > 0 with Y = −g0⁻¹ dτ, future timelike for g_λ (EQUALITY5 section 0, NIT-7),
so v + ε(τ − τ0) increases along future causal curves of g_λ and R lies to the past of its face. R does not meet Ω's
outer face (there v ≥ V + 1 > v1). Its slices are {a ≤ r ≤ ρ(τ)}, ρ(τ) := v1 − ε(τ − τ0) − τ (which is below b(τ)),
with ρ' = −1 − ε < 0.

**2. The equation (E6).** From (0.2) of the supplement, Ric^H(g_λ) = 0 and g_λ = g_app + w,

    −½ g_λ^(ab) ∂_a ∂_b w = f := −Ric^H(g_app) + ½ (g_λ^(ab) − g_app^(ab)) ∂_a ∂_b g_app − [Q(g_λ)(∂g_λ, ∂g_λ) −
                              Q(g_app)(∂g_app, ∂g_app)].

**3. Coefficients on R.** For X ∈ R and j ≤ 4, by D5 |∂^j (g_app − g0)(X)| ≤ C Σ_(l≤N) Σ_(p≤j) λ^(l−p) |∂_θ^p
∂_X^(j−p) g_l|. A θ-derivative removes the means, so for p ≥ 1 the factor is at most C ε_(M*)(v1) by L.3 (a) and L.2
(a); for p = 0 it is bounded globally. Hence |∂^j (g_app − g0)| ≤ C (λ + λ^(1−j) ε_(M*)(v1)) ≤ C for j ≤ 4, by the
hypothesis ε_(M*)(v1) ≤ λ³. Theorem E (Step 1, READ) gives |∂^j w| ≤ C M λ^(K−3−j) ≤ C on Ω for j ≤ 3 (K ≥ 6). So |∂^j
g_λ| ≤ C on R for j ≤ 3, and |g_λ − g0| ≤ C λ.

**4. The source.** On R, |(g_λ⁻¹ − g_app⁻¹) ∂²g_app| ≤ C |w| (step 3), and the Q-difference is at most C (|w| + |∂w|)
by the mean value theorem in (g, ∂g), as in the proof of EQUALITY5 Proposition E.2. Differentiating, for i ≤ 2: |∂^i f|
≤ |∂^i Ric^H(g_app)| + C Σ_(p≤i+1) |∂^p w|, using ∂^q g_app for q ≤ 4 and ∂^q w for q ≤ 3, bounded by step 3. And
|∂^i Ric^H(g_app)| ≤ C λ^(N−1−i) ε_(M*)(v1) on R (L.3 (d)).

**5. The data (Theorem D's construction, supplement 6.4, READ; L.3 (e)).** On Σ_τ0 ∩ R = {a ≤ r ≤ v1 − τ0}: the spatial
part of w is a dr dr; the τ-derivative of its spatial part is fixed by w Π + q dr + dr q and the shift acting on a dr
dr; its lapse and shift parts vanish, and their τ-derivatives solve D(g) − D(g_app) = −D(g_app) with invertible
coefficient, where D(g_app) = λ^(N−1) [D^(N−1)] + O(λ^N) with profiles weighted by (F2) (Lemma 6.1, READ); the higher
τ-derivatives on Σ_τ0 follow from step 2's equation solved for ∂_τ² (g_λ^(ττ) ≠ 0), whose coefficients are bounded by
step 3. With L.3 (e), |∂^p w| ≤ C λ^(N−2−p) ε_(M*)(v1) on Σ_τ0 ∩ R for p ≤ 3, so that

    E_2(τ0) := Σ_(i≤2) (‖∂ ∂^i w(τ0)‖ + ‖∂^i w(τ0)‖) ≤ C λ^(N−5) ε_(M*)(v1),          norms on R ∩ Σ_τ.

**6. Energy on R.** Apply ∂^α, |α| ≤ 2, to step 2's equation. The commutator ½ [∂^α, g_λ^(ab)] ∂_a ∂_b w has terms
∂^p g_λ⁻¹ · ∂^(|α|−p+2) w, 1 ≤ p ≤ 2, at most C Σ_(q≤3) |∂^q w| (step 3). Run Lemma 2.3 (READ) with g̃ := g_λ on R in
place of Ω: the tilted face is spacelike for g_λ with R to its past (step 1), so its flux is nonnegative and dropped;
{r = a} likewise (Lemma 1.1 (b), (e)); the L² boundary term carries ρ' < 0. So E_2(τ) ≤ C (E_2(τ0) + ∫_(τ0)^τ (E_2 +
Σ_(i≤2) ‖∂^i Ric^H(g_app)‖)), and Gronwall's lemma gives E_2(τ) ≤ C (λ^(N−5) + λ^(N−3)) ε_(M*)(v1) on [τ0, τ_end].

**7. Pointwise.** For X ∈ R with r(X) ≥ q0, the slice R ∩ Σ_(τ(X)) = {a ≤ r ≤ ρ(τ(X))} contains X, so ρ(τ(X)) ≥ r(X) ≥
q0 = a + δ0, and ρ(τ(X)) ≤ b(τ0): its width lies in [δ0, b(τ0) − a]. Sobolev's inequality with a uniform constant on
such annuli (the proof of the supplement's Lemma 2.1, READ: images of a fixed annulus under radial maps with bounded
derivatives) gives |w(X)| ≤ C Σ_(p≤3) ‖∂_x^p w(τ(X))‖ ≤ C E_2(τ(X)). ∎

Round 1's L.4 used four derivatives and lost one more power of λ; three suffice for |w| (H³ ⊂ L^∞ in four dimensions),
and the data's third derivatives are C λ^(N−5), which is what sets the exponent.

### R2.6 Theorem L with round 2's lemmas

Round 1's section 7 runs as written with Proposition L.2 (a), Corollary L.11 and Lemmas L.3, L.4 in place of the
sketches, with three changes: M := M* = 2N + 8 and m := 56 M; L.4's hypothesis is ε_(M*)(v1) ≤ λ³; and its w-term is
O(λ^(N−5) ε_(M*)(v1)). So, with y := λ^p, p = 14, and the window and v1 of round 1,

    |ρ_λ| ≤ C ( y² + λ⁴ y^(1−M/m) + λ y^(2(1−M/m)) + λ^(N−5) y^(1−M/m) ),

and the term q of Lemma L.1 is at most C (λ² ε + λ ε² + |w|)(λ² ε + λ ε² + |w| + λ² ε²), within the same bound. The
conditions (e1)–(e8) of layerledger5 L1 (the dominance of the signal λ³ y, or λ³ y^(1+2/κ) at the double root ρ*,
over each term; Landau's window; L.4's hypothesis; the window inside the layer) hold for every N ≥ 9 and both cases.
**So Theorem L holds for every K ≥ 6, every metric of Theorem 1, and Corollary L.7 with it** (deduced; computed L1, L4:
round 1's exponent N − 6 needed N ≥ 10, round 2's N − 5 needs N ≥ 9).

### R2.7 Theorem 2's solution (O3)

**Theorem L_P (deduced; computed layerpast5 P1–P3, layernull5 E4–E5, layerledger5 L2).** Let μ0 = √72 l5², K ≥ 6, and
let g_λ, 0 < λ ≤ λ_P, be the metric of Theorem 2 (the supplement's Theorem P, READ), built from Theorem A_P's
approximant of order N_P := K + 4 + ⌈4β0⌉ with nothing coming in from past null infinity; A, env, v_s and τ0 as in
Theorem L. Then Theorem L's conclusions hold for g_λ with K(v − τ0) replaced by the constant

    K∞ := −μ0^(−7/4)/9 ≠ 0,

so with no exceptional case, and Corollary L.7 holds for g_λ.

The proof follows R2.3–R2.6, with four changes: the seed region (E.2_P), the first-degree profiles (computed), the
flat-edge bounds on the past domain (L.3_P) and the remainder (L.4_P), which is simpler here than for Theorem 1.

**Proposition E.2_P.** g_λ = g0 on (P ∪ Ω) ∩ {v ≤ v_s}. Hence EQUALITY5's Propositions E.3 and E.4 hold for this g_λ.

*Proof.* Theorem A_P's stages vanish for v ≤ v_s: on P they are transport solutions along ℓ at fixed v, and means
whose energy on P ∩ {v' ≤ v} is fixed by sources there (Theorem A_P, READ; the null face {v' = v} has its flux of one
sign, as in L.8), and all sources vanish where env does; on Ω they continue by Lemma 5.3 with these traces. So g_app =
g0 on (P ∪ Ω) ∩ {v ≤ v_s}. The approximating solutions g_n of Proposition 9.8 equal g_app, with their τ-derivative, on
Σ_(τ_n); Lemma 9.2 (READ) with v_start replaced by v_s (its proof uses only that g0 is vacuum on that region, where μ =
μ0) gives g_n = g0 on P ∩ {τ ≥ τ_n, v ≤ v_s}, and so g_λ, their limit. On Ω ∩ {v ≤ v_s}, g_λ's data on Σ_τ0 are g0's
with their τ-derivative (g_λ is smooth on P ∪ Ω), and the proof of EQUALITY5 Proposition E.2 runs as written. E.3 and
E.4 use only E.1, E.2 and |g_λ⁻¹ − g0⁻¹| ≤ C1 λ on Ω, which Theorem P (P-iv) gives. ∎

**The first-degree profiles with nothing coming in (computed: layerpast5).** Theorem A_P solves every transport with
r^(3/2) Z → 0 along the generators (Lemma 9.7 (d), READ), not with Lemma 6.2's data, so its first-degree profiles H_j^∞
solve T(H_(j+1)^∞) = −R_X(H_j^∞) with that condition (H_1^∞ = H_1). P1: H_2^∞, the r0 → ∞ form of round 1's (3.2) (vθ
radial factor β∞ = (μ0/3) r⁻³), solves the transport in all fifteen components, lies in S, satisfies i Pol(H_2^∞) + D_X
H_1 = 0 in all five, and decays (r^(3/2) |H_2^∞|_cart → 0). P2: in every sector the homogeneous solutions have
r^(3/2)|h|_cart → their free constant, so the decay condition fixes the solution (control: round 1's H_2 at r0 = 3√μ0
does not decay). P3: R_X(H_2^∞) has vv = 0 and trace 0; the scalar sector of H_3^∞ is tr = 0, rr = −A env d r^(−7/2), vr
= −(μ0/3) A env d r^(−11/2), vv = −(μ0²/9) A env d r^(−15/2), which solves the transports in vv, vr, rr and trace,
decays, and satisfies i Pol(H_3^∞) + D_X H_2^∞ = 0 in v and r; at the horizon H_3,vv^∞ = A env d K∞. On Ω the profiles
continue by the same seed transports with their traces as data (Theorem A_P's continuation, READ), so the formulas hold
there. The H_j^∞ do not depend on τ0, and K∞ is the r0 → ∞ limit of round 1's K(r0), now obtained without the limit.

**Lemma L.3_P (flat-edge bounds from past null infinity; deduced, with E1, E5).** Write E_p(ε^d) for the profiles f on
P_v := P ∩ {v' ≤ v} (v ≤ v_♯) with |∂_X^α Ω^β ∂_θ^n f| ≤ C ε_c(v)^d r^(−p), c the cost (here as in L.3); Theorem A_P's
classes E_p, L_p, O_p (READ) are the case d = 0. Then:

- (a_P) W_TT ∈ E_(3/2)(ε), χ ∈ E_2(ε²), gh_j ∈ E_2(ε) for j ≥ 2;
- (b_P) m_j = r⁻² M_j + m̃_j with |M_j| ≤ C ε²; |m̃_j| ≤ C ε² r⁻¹ and |m̃_j| ≤ C ε r^(−7/4), with their derivatives; the
  phases and Ψ_j satisfy |∂φ_j| ≤ C ε r^(−3/4) and |Ψ_j| ≤ C ε r^(−7/4) beyond their leading terms (built from M_j,
  O(ε²)); and on P_v ∩ Σ_τ the L² norms of the remainders carry the weight ε² with the t-rates of Theorem A_P's (9.7);
- (c_P) gh_j − Re[H_j^∞ e^(iθ)] ∈ E_2(ε²);
- (d_P) ‖∂^i Ric^H(g_app)‖_(L²(P_v ∩ Σ_τ)) ≤ C λ^(N_P−1−i) ε_c(v) t^(−3/2);
- and on Ω ∩ {v ≤ v_♯} the bounds (a)–(d) of Lemma L.3 hold, with (e) replaced by the traces on Σ_τ0 of (a_P)–(c_P),
  except that φ_j and Ψ_j are bounded by C ε (not ε²), which is all that L.2 (a) and L.3 (c) use of them (every use
  multiplies them by an oscillating factor, or squares them in q_m).

*Proof.* (a_P): induction over the stages as in L.3 (a). W_TT = r^(−3/2) F with F linear in env (`past5.py` P3, READ); χ
is r⁻² times a function of (v, θ, s), quadratic in env (P5, READ). At stage m the source of (c) is in L_3 without the
unknowns, and with them through coefficients in E_(3/2) and E_(5/2) (Theorem A_P's count, READ); by (F1) each monomial
has an oscillating factor, so the source is in E_3(ε), and the transport from infinity, Z = −r^(−3/2) e^(−C) ∫_r^∞
r'^(3/2) e^(C) S dr' along the generator at fixed v (Lemma 9.7 (d), READ), maps E_3(ε) into E_2(ε) (E5: the weight is
that of the generator's v). (b_P): M_j := 2 ∫_(−∞)^v S_(j,3) with S_(j,3) of degree two by (F2), so |M_j| ≤ C (v − v_s)
ε². The remainders (m̃, φ̃, Ψ̃) solve Theorem A_P's remainder system, whose estimates (9.7) are linear in the sources
and run on P_v (Lemmas 9.5, 9.6 on P_v: the null face {v' = v} has P_v to its past and its flux is kept, as in L.8; L0
is tangent to it, so the transport's boundary term vanishes, E2; Lemma 9.3 (b)'s Poincaré inequality holds on the
thinner slices with the same constant); with the oscillating remainder taken as a known source by (a_P), all sources lie
in E_(7/2)(ε²), so the energies and the flux through {v' = v} carry ε² with (9.7)'s t-rates. The flux gives, as in L.10
but integrating from infinity along γ_Y (E5: ∫_r^∞ r'^(−3) dr' = 1/(2r²)), |∂^α Ω^β m̃_j| ≤ C ε² r⁻¹; Theorem A_P (READ)
gives |m̃_j| ≤ C r^(−5/2); min ≤ geometric mean (E5) gives C ε r^(−7/4). Then σ̃_j := m̃_j(ℓ, ℓ) + q_j is at most C ε
r^(−7/4) (q_j is quadratic in (m_i, dφ_i), i < j, with no product ∂_vφ_i ∂_vφ_k since g0^vv = 0, READ), φ̃_j = −½ ∫_r^∞
σ̃_j (READ) gives |φ̃_j|, |∂_v φ̃_j| ≤ C ε r^(−3/4), and Ψ̃_j by (9.5) (READ) is at most C ε r^(−7/4). (c_P): as in L.3
(c), the source of the δ-transport is a sum of products of two oscillating factors (E_3(ε²)), of mean-type factors with
coefficients carrying an oscillating factor (by (b_P) and the coefficient classes E_(3/2), E_(5/2): at most C ε²
r^(−13/4)), of R_X^seed(δ_m) (E_3(ε²) by the induction and Lemma 9.7 (c), READ), and of (μ − μ0) times oscillating
factors; so it lies in E_3(ε²), and the transport from infinity with q = 3 > 5/2 gives E_2(ε²) (Lemma 9.7 (d), READ; at
q = 13/4, E5). (d_P): as L.3 (d), estimating each monomial in L² on the slices by one weighted factor in L² (its
weighted (9.7) norm, which has the t-rate of its class) or in L^∞ (oscillating factors), and the others in L^∞ by their
classes; the classes of each monomial add to at least 3 (R_N, R'_N ∈ E_3, READ), and an E_3 profile has L² norm at most
C t^(−3/2) on a slice of P_v (E5). On Ω: L.3's proof with Σ_τ0's data replaced by these traces, which are of the stated
sizes at the bounded radii of Σ_τ0 ∩ Ω. ∎

**Lemma L.4_P (the weighted remainder for Theorem 2's solution; deduced, with E4, E5, E6).** Let C_P be such that
|(g_λ⁻¹ − g0⁻¹)(α, α)| ≤ C_P λ t^(−3/2) |α|_e² on P and ≤ C_P λ |α|_e² on Ω (Theorem A_P: g_app⁻¹ − g0⁻¹ ∈ λ E_(3/2);
Theorem P (P-iii), (P-iv), READ), s := C_P λ ≤ 1/2, ε := 2 C_P λ, and ψ(τ) := 2 t^(−1/2) for τ ≤ τ0, ψ(τ) := 2 + τ −
τ0 for τ ≥ τ0 (C¹, increasing, E4). For v1 ≤ v_♯ with ε_(M_P)(v1) ≤ λ³, M_P := 2 N_P + 8, and R_P := (P ∪ Ω) ∩ {v + ε
ψ(τ) ≤ v1}: for every X ∈ R_P ∩ Ω with r(X) ≥ q0,

    |w(X)| ≤ C λ^(N_P−3) ε_(M_P)(v1).                                                                           (R2.5)

*Proof.* As L.4, with four differences. (1) The face {v + εψ(τ) = v1} has conormal dv + ε ψ' dτ, and E4 gives g_λ⁻¹
of it at most −2sψ' + 4s³ψ'³ − 4s²ψ'²μ/r² < 0 with ψ' = t^(−3/2) on P: the tilt decays exactly as the perturbation
does, and ψ stays bounded (ψ ≤ 2 on P), so R_P ⊂ {v ≤ v1} and R_P does not reach the outer boundary B of P (on R_P, v
+ h ≤ v1 + κ < V_P). (2) There are no data: by E.2_P, w = 0 on {v ≤ v_s}, and the energy of w on A_P(τ1) tends to zero as
τ1 → −∞ (Proposition 9.8's (9.8), passed to the limit, READ), so the energy inequality on R_P ∩ {τ ≤ τ'} (Lemma 9.5 on
P, Lemma 2.3 on Ω, READ; the tilted face's flux dropped) starts from zero at −∞. (3) On P the coefficients decay: ∂g_λ
and the factor ∂²g_app of (g_λ⁻¹ − g_app⁻¹) ∂²g_app are at most C t^(−3/2), the latter because its one large part,
λ⁻¹ dv dv [∂_θ² g1], is weighted by the wave's amplitude, at most λ⁻¹ ε_(M_P)(v1) t^(−3/2) ≤ C t^(−3/2) on R_P (L.3_P
(a_P)); so the Gronwall kernel is C t^(−3/2) on P, integrable (E5: ∫ t^(−3/2) dτ = 2), and C on Ω. No decomposition
w = h + φ [∂_θ g1] is needed on R_P: the 1/λ coefficient that forced it on P's near region is small there. Theorem P's
bounds on ∂^j w, j ≤ 3 (P-iii and (9.8)–(9.9) with Lemma 9.3 (a), READ) bound the nonlinear terms. (4) The source:
‖∂^i Ric^H(g_app)‖_(L²) ≤ C λ^(N_P−1−i) ε t^(−3/2) on R_P ∩ Σ_τ (L.3_P (d_P)), integrable in τ. Gronwall's lemma gives
E_2(τ) ≤ C λ^(N_P−3) ε_(M_P)(v1), and step 7 of L.4 gives (R2.5). ∎

*Proof of Theorem L_P.* With E.2_P, the layer of E.3 (c) is defined for this g_λ. Corollary L.11 holds at the boundary
points with H_j^∞ in place of H_j (L.3_P (c_P) and the continuation on Ω) and with K∞ in place of K(v − τ0) (P3). The
window, the domination and the sign change are round 1's section 7 with |K| ≥ |K∞| on W_λ, so only the first case
occurs, and with the w-term O(λ^(N_P−3) ε_(M_P)(v1)) from L.4_P, where v1 := v* + 4πλ + ε(2 + τ_end − τ0) puts every
boundary point of W_λ in R_P. The conditions (e1)–(e8) hold for every K ≥ 6 and β0 ≥ 2 (L2). ∎

### R2.8 The paper at equality: what Corollary L.7 meets, and the proposed text

READ (`../../paper/RESPONSE-HL-5D.md`, 2026-11-02; the file was being edited by another job while this was written, so
the passages are quoted, not cited by line):

- Proposition 3.2, first sentence: the boundary is spacelike **for g0** wherever μ > √72 l5² or μ' > 0, "and every
  future causal curve that meets it leaves D_T there and does not return". At equality this concerns g0, for which it
  holds (on v > v_s, m0 > 0). Not contradicted.
- Proposition 3.2, the equality sentence: "If μ0 = √72 l5² exactly, the boundary coincides with the seed's horizon for
  v ≤ v_start and is null there; g_λ equals the seed on {v ≤ inf supp env}, so it is null for g_λ too, and after the
  shell starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
  `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4)." Theorem L's timelike points lie inside that layer
  (W_λ ⊂ {v_s < v < v_s + η_λ}, round 1 section 7), so the sentence is true; it is silent about the layer, and the
  no-return property it states for μ0 > √72 l5² is not claimed at equality. Not contradicted.
- Section 9, "The boundary at equality": "in the layer between, whose width tends to 0 with λ, its causal character is
  not decided, because there the margin and the perturbation both vanish to every order (computed: ... eqlayer5.py —
  ... while env' and env'' are not bounded by the margin's order, which is why the expansion cannot decide the layer)."
  Theorem L decides the layer, negatively, and by the expansion: near the edge the term of first degree, λ³ A env K
  Re[d e^(iv/λ)], exceeds the margin, which is of order env² + ∫ env². The computed fact cited (eqlayer5) stands; the
  status "not decided" and the inference "the expansion cannot decide the layer" are superseded. This is the one
  sentence of the paper that Theorem L overturns; it states a status, not a theorem.
- Section 1.4 and the abstract say x_K = 1 is spacelike, and D_T the domain of dependence of its data, "when μ0 >
  √72 l5²": not claimed at equality. Corollary L.7 shows the restriction is needed: at equality D_T is not the domain of
  dependence of its data for g_λ. Section 2.3's statement that Ω is a domain of dependence, and Theorems 1–3 (built on
  Ω ⊃ D_T ∩ {τ ≥ τ0}), are unaffected.
- Section 6's "The boundary" paragraph concerns μ0 > √72 l5² only. Not contradicted.

So Corollary L.7 contradicts nothing the paper proves; one status sentence and its stated reason are superseded, and
Proposition 3.2's equality sentence is incomplete. Theorem L and its lemmas are deduced here and **not yet read by an
independent verifier**, while the paper's section 9 ("Review") says every part of the supplement was so read: the text
below should be seated after that reading (O2), or with each mark [†] written out as "(not yet read by an independent
verifier)".

#### Proposed paper text

(P1) Proposition 3.2: replace the sentence from "If μ0 = √72 l5² exactly, the" to "(supplement
`docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4)." by:

> If μ0 = √72 l5² exactly, the boundary coincides with the seed's horizon for v ≤ v_start and is null there; g_λ equals
> the seed on {v ≤ inf supp env}, so it is null for g_λ too; after the shell starts it is spacelike for g_λ outside a
> layer whose width tends to 0 with λ (supplement `docket68/n1star/EQUALITY5.md`, Propositions E.2–E.4); and inside
> that layer it is not spacelike: for λ small it has, on every column, points where it is timelike for g_λ, alternating
> with points where it is spacelike on the scale of the wavelength, so that some future timelike curves of g_λ cross it
> into D_T there, and the no-return property of the first sentence fails for g_λ at equality (deduced [†], supplement
> `docket68/n1star/EQUALITY5-LAYER.md`, Theorems L and L_P and Corollary L.7, for the solutions of Theorems 1 and 2).
> What holds at equality in its place is a domain O(λ)-close to D_T, inside x_K ≤ 1, whose inner boundary no future
> causal curve of g_λ enters (EQUALITY5.md, Proposition E.4).

(P2) Section 9: replace the bullet "**The boundary at equality.**" by:

> - **The boundary at equality.** If μ0 = √72 l5² exactly (computed, `docket68/n1star/checks/eq5.py` E1–E6,
>   `checks/eqlayer5.py` L1–L2, `checks/layerlin5.py` N0–N6, `checks/layerwin5.py` W1–W2, `checks/layerdeg5.py` D1–D5,
>   `checks/layernull5.py` E1–E6, `checks/layerpast5.py` P1–P3, `checks/layerledger5.py` L1–L4; deduced, supplement
>   `docket68/n1star/EQUALITY5.md` and `docket68/n1star/EQUALITY5-LAYER.md` [†]): g_λ equals the seed on {v ≤ v_s},
>   v_s := inf supp env, so x_K = 1 is the seed's horizon there; it is spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η;
>   and in the layer between, whose width tends to 0 with λ, it is not spacelike. There the margin is of the order of
>   env² + ∫ env² (`checks/eqlayer5.py`), while the part of g_λ⁻¹(dΦ0, dΦ0) linear in the waves has no term of order λ
>   or λ² (the first two profiles have no vv, vr or rr component, by the gauge's polarization) and at order λ³ is −λ³ A
>   env(v) K Re[d(θ) e^(iv/λ)]: d is the double divergence on S³ of the waves' angular tensor, nonzero at every angle
>   for the waves of section 2.4, and K is a constant of the seed, K = −μ0^(−7/4)/9 for the solution of Theorem 2 and,
>   for that of Theorem 1, a function of the radius at which the data slice meets the incoming ray that vanishes at one
>   value only. Near the edge of the envelope, where env is smaller than every power of λ, this term exceeds the margin
>   and every error term, so for every K ≥ 6 and λ ≤ λ_L, on every column, a window of width 4πλ inside the layer has
>   points where x_K = 1 is timelike and points where it is spacelike: some future timelike curves of g_λ cross it into
>   D_T, and Proposition 3.2's no-return property fails there. What holds in its place is a domain O(λ)-close to D_T,
>   inside x_K ≤ 1, whose inner boundary no future causal curve enters; and the spheres' horizon holds in the form: at
>   most one zero per column, within C λ of √μ(v); exactly one on the columns with v ≤ v_s and on those that reach
>   across √μ(v) + C λ with √μ(v) − r_q(v) ≥ C' λ. Not settled: the causal character at the very edge, v − v_s of order
>   λ^(1/2) or less, where the expansion in λ breaks down, and the value of λ_L.

(P3) Appendix A, after the entry for `checks/eqlayer5.py`, add:

> - `checks/layerlin5.py` N0–N6: the term linear in the waves at x_K = 1 at equality: the inverse-metric identity (N0);
>   the two-scale linearized operators at the seed and their class S, closed under them (N1); the gauge's Pol^+ (N2);
>   the first three profiles of the record's construction, H_1 and H_2 in S, H_3's scalar sector and its horizon value
>   A env d K (N3–N5); d for the record's waves, nonzero at every angle (N6). Controls: the identity truncated; a profile
>   with a vr component; Pol^+ without its trace term; a transport without its mass coupling; a transverse angular
>   tensor; one quadrature alone. Exact; about five minutes.
> - `checks/layerwin5.py` W1–W2: the interpolation inequality on a half-line with its constants, and the window near a
>   flat edge for three envelopes. Controls: the bound without interpolation; the level λ²; K = 0. About a minute.
> - `checks/layerdeg5.py` D1–D5, `checks/layernull5.py` E1–E6, `checks/layerpast5.py` P1–P3,
>   `checks/layerledger5.py` L1–L4: the bookkeeping of degree (the seed's operators on every harmonic, products of
>   harmonics, the shifts of degree two), the energy and transport identities on the past sets with the null face kept,
>   the tilted faces of the remainder estimates, the first-degree profiles with nothing coming in and K = −μ0^(−7/4)/9
>   for Theorem 2's solution, and the exponent and derivative ledgers (K ≥ 6). Each with a control that must fail.
>   Exact; under three minutes in all.

(P4) Appendix C, after the row "the boundary at equality: the layer", add the row:

> | the boundary at equality: timelike points in the layer | `docket68/n1star/EQUALITY5-LAYER.md`;
> `checks/layerlin5.py`, `checks/layerwin5.py`, `checks/layerdeg5.py`, `checks/layernull5.py`, `checks/layerpast5.py`,
> `checks/layerledger5.py` |

(written as one table row in the paper; it is broken here only for the line length)

(P5) Appendix D, after `python3 checks/eqlayer5.py`, add the six commands (layerlin5 about five minutes, layerwin5 about
a minute, layerdeg5 about a minute and a half, layernull5 about ten seconds, layerpast5 about a minute and a half,
layerledger5 under a second), and the md5 rows of the new files and outputs.

(P6) Optional, section 1.4: after "and is spacelike when μ0 > √72 l5² (section 6)" add "; at equality it is not, in a
layer of width tending to zero with λ (section 9)".

### R2.9 Labels, computational support, and what is open

*Labels.* Deduced: Lemmas L.8–L.10, L.3, L.4, Proposition L.2 (a), Corollary L.11, Theorem L for K ≥ 6, Proposition
E.2_P, Lemmas L.3_P, L.4_P, Theorem L_P, and the reading of the paper in R2.8. Computed: D1–D5, E1–E6, P1–P3, L1–L4
(exact; D4 on samples). READ: the supplement `N1STAR-PROOF.md` sections 0.2–0.5, 1 (Lemma 1.1), 2 (Lemmas 2.1, 2.3,
2.4), 3.1–3.2, 4 (Step 1), 5.1–5.4 (Lemmas 5.1–5.3), 6.1–6.4 (Lemmas 6.1–6.4, Proposition 6.5), 9.1–9.4 (Lemmas 9.1–
9.7, Theorem A_P, Propositions 9.8–9.9, Theorem P); `EQUALITY5.md` sections 0–2; the paper's Proposition 3.2, sections
1.4, 2.3, 6 and 9; round 1's N0–N6, W1–W2.

*Computational support, step by step.*

| step | used for | check |
|---|---|---|
| seed operators on the k-th harmonic: λ⁻¹ k T + R_X, λ⁻¹ i k Pol + D_X, no λ⁻² part | (F2), L.3 (c), L.2 (a) (i) | D1 |
| θ-means of products; one oscillating factor gives mean zero | (F2), L.3 (b), (e) | D2 |
| β0, r_q − √μ0, m0 of degree two, with constants | L.11 | D3 |
| ∂_θ⁻¹ bounded by π on zero-mean C(S¹) | L.9 (b), L.3 (a), (c) | D4 |
| the chain rule: a derivative of [f] costs λ⁻¹ only through ∂_θ | L.3 (d), L.4 step 3 | D5 |
| null-face flux density T(L0, Y), volume form, causal character of Y, L0 | L.8, L.10 | E1 |
| L² transport and energy boundary terms on Ω_v's slices | L.8, L.9 (a), L.3_P | E2 |
| the tilted face of L.4: timelike conormal, future side, slices shrinking | L.4 step 1 | E3 |
| the past tilted face ψ: C¹, bounded, tilt decaying as the perturbation | L.4_P | E4 |
| ∫_r^∞ r'⁻³, ∫ t^(−3/2), L² of r⁻³ on a slab, transport from infinity, min ≤ mean | L.10, L.3_P, L.4_P | E5 |
| the equation for the remainder w | L.4 step 2, L.4_P | E6 |
| H_2^∞, uniqueness of "nothing coming in", H_3^∞'s scalar sector, K∞ | R2.7 | P1–P3 |
| exponent conditions, K ≥ 6; Theorem 2; derivative costs ≤ 2N + 8 | R2.6, R2.7, L.3 | L1–L4 |
| H_1, H_2 ∈ S, H_3,vv at the horizon, K(r0), Pol^+, d ≠ 0 | L.11, L.2 (a) | N1–N6 (round 1) |
| interpolation on a half-line; the window | R2.6 | W1–W2 (round 1) |

Standard theorems used as READ in the supplement and not re-derived: Sobolev's embedding on annuli and on S³ (Lemma 2.1,
Lemma 9.3 (a)), the divergence theorem and Gronwall's lemma, the dominant energy property (made explicit by E1 for the
one null face used).

*Open.*

- O1 (the very edge, v − v_s ≲ λ^(1/2)): unchanged; Theorem L does not need it.
- O2: round 2 writes L.2 (a), L.3, L.4 and the analogues for Theorem 2 at proof level. An independent reading of rounds
  1 and 2 is the remaining step; until it is done, Theorem L is deduced, not verified.
- O3: closed by Theorem L_P (deduced), subject to O2.
- O4 (λ_L): not evaluated, and not computable in practice from this proof. The exact obstruction: λ_L must make (i)
  Theorem 1's constants (C1, M, Theorem A's profile bounds, the C of L.3–L.4, none evaluated) beaten by the λ-powers of
  (e1)–(e8); (ii) Lemma L.6's hypothesis, L C_(1,m) (2y)^(1−1/m) M_m^(1/m) ≤ y/4 with L = O(λ), y = λ^14 and m =
  56 (2N + 8), that is λ^(1−1/(4M*)) below a multiple of 1/(C_(1,m) M_m^(1/m)), with M_m = sup |env^(m)| at m ≥ 1456
  (N = 9); and (iii) v*(λ^14) − v_s below the scale on which K(v − τ0) stays near K(v_s − τ0), a modulus of the
  flatness of env at its edge, which no finite set of env's norms fixes. For Theorem 2's solution (iii) is void (K∞ is
  constant).
- O5 (the convention of Pol^+): unchanged for Theorem 1. Theorem 2's solution does not use Pol^+ for its profiles, so
  Theorem L_P and K∞ are independent of that convention.
- O6 (new, minor): Lemma 6.2's proof fixes the stage data of stages 1, ..., N − 1 only; round 2 takes stage N's by the
  same rule (R2.1). Any rule local in the earlier stages and vanishing where they do gives the same lemmas.

Files (round 2): this section; `checks/layerdeg5.py`, `checks/layernull5.py`, `checks/layerpast5.py`,
`checks/layerledger5.py`, each with its `.out` (about a minute and a half, ten seconds, a minute and a half, under a
second).

## Round 3

Status: written (round 3, 2026-11-02); not yet read by an independent verifier. Rounds 1-2 were read by one (vE2,
2026-11-02, scripts kept outside the record); its verdicts and findings are seated in R3.1. New programs, each with a
docstring stating its claims, controls and labels, all pass and every control fails (`.out` beside each):
`checks/veryedge5.py` V1-V5, `checks/layerband5.py` B1-B3, `checks/lamL5.py` L1-L4, `checks/stagen5.py` S1-S4,
`checks/layerfix5.py` F1-F4. Changed: `checks/layerwin5.py` (docstring lemma numbers, W2's label, the printed name of
(e6), its output wrapped at 121 columns) and `checks/layerlin5.py` (its output wrapped; no check changed); both outputs
regenerated, and `layerlin5.out` no longer ends in a line `exit 0` that the program does not print. The text of rounds 1
and 2 is kept; this section amends it, item by item.

### R3.0 Findings

1. **The verifier's report (R3.1).** Theorem L, Corollary L.7, Theorem L_P, Proposition E.2_P, Lemmas L.4, L.8, L.10,
   Proposition L.2 (a) and Corollary L.11 read as sound; K∞ re-derived independently; all six programs reproduce. Its
   one major finding (M1: round 2 understated what Theorem L leaves open in the layer) and its minor findings and nits
   are seated as amendments A1-A17, each with a check. Two corrections of substance: the costs of Lemma L.3 (b), (c),
   (d), (e) are one higher than printed (i + 2j + 1, i + 2N + 3, j + 2N + 3), still within M* = 2N + 8 (F1); and the
   horizon coefficient (round 1's K, renamed **ν**) depends on τ0 and on the convention of Pol^+ (F2).
2. **The layer outside the window is decided, up to stated bands (Proposition L.12, R3.2 (b)-(d)).** For every K ≥ 6:
   spacelike wherever sup_(v'≤v) env ≥ λ^(σ_K − δ), σ_K := min(3, (K − 3)/2), zeros of env included; timelike points
   within 4πλ of every first-reach point at the levels λ^p, 3 + δ ≤ p ≤ P (every point of that range for an envelope
   increasing at its edge, as the record's is); and for K ≥ 10 the band between is decided by the explicit ratio R =
   λ³ A env |ν| |d| / m0 (computed ledger B2; deduced).
3. **The very edge (O1; R3.2 (e)).** The expansion in λ of the first-degree term is the binomial expansion of λ (i/s)²
   [A d ν env], s := ∂_v + i/λ (computed structure V1, V2; deduced), and stops being asymptotic where λ|env'/env| ≥ 1:
   v − v_s ≲ (cλ)^(1/2) for an exp(−c/x) edge (the record's, c = 3/4), (kλ)^(1/(k+1)) for exp(−1/x^k), about 1/ln(1/λ)
   for exp(−e^(1/x)) (V4). Re-summed, it alternates on every carrier period there too (V5). For Theorem 1's solution
   this cannot be read off the approximant: on the very edge its first-degree term is fixed by data the construction
   sets at orders invisible to Theorem 1 (stage N's data and the correction U), which change it at leading order
   (V3, V5 (d), S4). **Decided: no expansion of the approximant decides the very edge for Theorem 1's g_λ; the
   deciding quantity is named.** For Theorem 2's solution the first-degree term is intrinsic, and the alternation
   follows from two named lemmas that the record does not contain.
4. **λ_L (O4; R3.3)** is explicit in Theorem 1's constants and the envelope's (lamL5): λ_L is the minimum of nine
   terms, of which two are numbers at P*, one a number times a known function of C1, and the rest known functions of
   λ0, C1, C_Φ, C_L11, C_L4. Certified: the threshold rounds 1-2 deliver is below 2.5·10^(−4655); with an amended Lemma
   L.5 (A15) below 6.7·10^(−58). Unevaluated: λ0 and C1 of Theorem 1 and the constants C_L11, C_L4 built from the same
   leaves (CONSTANTS5.md 1.5). The paper's sin⁴ envelope is not flat at its edge and Theorem L does not apply to it (L1).
5. **Stage N (O6; R3.4)** is settled: the supplement leaves stage N's data free; Theorems A, D, E hold for any smooth
   choice (S2); Lemma 6.2's step runs at m = N inside Theorem A of order N (S3) and is the rule that makes section 6.4's
   seed-data claim true. The choice is invisible in the layer and decisive on the very edge (S4).
6. **What stays open** is listed exactly in R3.5; **proposed paper text** in R3.6, replacing R2.8's P1-P2.

### R3.1 The verifier's report (vE2), seated

Verdicts (READ from the report): Theorem L, Corollary L.7, Theorem L_P and E.2_P sound as deductions, with no
contradiction with the paper; L.8, L.10 (the repair of C3), L.4, L.2 (a) and L.11 sound; K∞ = −μ0^(−7/4)/9 confirmed by
an independent re-derivation (δΓ in coordinates, its own Pol^+, the T table, H1, H2, R_X(H2)_vv = 0, D_X H2, the root
ρ* = 1.80644); all six programs reproduce.

- **A1 (M1, major).** Round 1 lines 5-6, 48, 258-260, round 2 line 856 and P2's "Not settled" sentence understate what
  is open. Theorem L answers EQ5's yes/no question (the boundary is not spacelike throughout the layer) and decides the
  pointwise causal character on W_λ only. What protects W_λ is the derivative control at a first-reach point (Lemmas
  L.5-L.6), not its distance from the edge; and the scale λ^(1/2) is that of an exp(−1/x) edge only. Repaired: R3.2
  decides the rest of the layer as far as the lemmas reach and states the remainder exactly (R3.5); the breakdown scales
  are computed for five edge classes with a control (V4); R3.6 rewrites the paper's sentence.
- **A2.** "where A env is smaller than every power of λ" (round 1 line 48) and "where env is smaller than every power of
  λ" (P2) are false at the window: env first reaches λ^14 there. Read "near the point where env first reaches λ^14".
- **A3.** Round 1's K (0.2) is renamed **ν(r0)** (it clashed with the Kretschmann scalar and with the regularity index K
  of Theorem 1), and K∞ is ν∞; every later "K(v − τ0)" of rounds 1-2 reads ν(v − τ0). ν is not "a constant of the seed"
  (P2): it depends on τ0, through r0 = v − τ0, and on the convention of Pol^+. With the Frobenius product in a Euclidean
  frame of (τ, x), the supplement's (Lemma 6.2 (i), READ), it is (0.2); with that of (v, x) it is −μ0^(−7/4)(ρ³ −
  1)²/(9ρ⁶), whose only zero, ρ = 1, lies outside the admissible ρ > 1 + μ0^(−1/2); both tend to ν∞ (computed F2, which
  reproduces the verifier's formula independently; control: the claim that the two agree fails). ν∞ does not depend on
  the convention (Theorem 2's solution uses no Pol^+, R2.9 O5).
- **A4.** Lemma L.3 (b), (c) (round 2 lines 420-422): the energy of ∂^i m_m on Ω_v needs the stage-m slice data at
  order i + 1, so the costs are i + 2j + 1 for m_j, φ_j and gh_j − Re[H_j e^(iθ)], i + 2j + 3 for Ψ_j, i + 2N + 3 in (d)
  and j + 2N + 3 for U in (e); (R2.3) reads ε_(i+2j+1). The largest cost used is 2N + 6 ≤ M* = 2N + 8, so no later
  statement changes (computed F1, the recursion with the data/energy step, N = 3..40; controls: without the step the
  closed form fails; a source with three derivatives exceeds 2N + 8). F1 supersedes layerledger5 L3.
- **A5.** Four controls were tautological: N5's (τ = 0 for a transverse tensor, never touching K), N6's (the same root
  recounted), P3's (the integral of 0 against K∞) and D4's square-wave clause (π/2 ≤ π). Replaced by mutations of the
  computed paths (F3): ν with β's mass term dropped is not (0.2); d^F's closed form with P's coefficient 38/3 mutated to
  37/3 fails at 7 angles against div div T; ν∞ with the vv coupling halved is not −μ0^(−7/4)/9; the square wave's
  antiderivative has amplitude π/2 exactly and refutes sup|Y| ≤ sup|Z|/2. Each passes unmutated and fails mutated.
- **A6.** Corollary L.7's "not only a replacement but a necessary one" (round 1 line 38) overstates. Read: "Corollary
  L.7 shows that D_T lacks, at equality, the inner-boundary property it has for μ0 > √72 l5²; it does not show that
  Proposition E.4's particular domain is needed."
- **A7.** layerwin5 W2 models three derivatives (e3), not M* = 26; relabelled a three-derivative qualitative model (its
  docstring). With 26 derivatives and unit constants the exp(−1/x) model needs λ of order 10^(−1000) (layerband5 B3).
- **A8.** "Exact" for D3, E3, E5: their monotonicity (D3, 60 sample points), negativity on (0, 1/2] (E3, 10 points) and
  min ≤ geometric mean (E5, 6 pairs) were sampled. Done exactly in F4 (solved inequalities; controls: (x − 1)/3 and
  s ≤ 1 fail). layerledger5 L3's "computed" certifies the recursion it transcribes, not the proof's counts, which are
  deduced (R2.3); the same holds for F1.
- **A9 (nit).** Round 1 line 242: the lower bound of the signal is λ³ A (3y/4)|ν||d|; the factor A was omitted.
- **A10 (nit).** Corollary L.11 (round 2 line 530): θ := v/λ collides with the angle θ; read ϑ := v/λ there.
- **A11 (nit).** β0 has two meanings: the coefficient in Φ0♯ = ∂_v + β0 ∂_r (lines 56, 537) and the decay exponent in
  N_P = K + 4 + ⌈4β0⌉ (lines 619, 717); read the latter as β_P.
- **A12 (nit).** Round 2 line 283: "three places" should be four (markers C1-C4).
- **A13 (nit).** Round 1 lines 14, 15, 236, 267 (K ≥ 7, W3) are superseded by R2.0 item 2 and layerledger5 L1, L4
  (K ≥ 6).
- **A14 (nit).** Round 1 line 156: the residual is Ric^H(g_app) = λ^(N−1)[ρ_N] (the supplement's (E3) with K = N − 1,
  READ 5.4), as round 2's L.3 (d) uses (λ^(N−1−i)); λ^N there was wrong.
- **A15.** Lemma L.5's constant (round 1) is valid but needlessly large: the remainder f − P has its i-th derivative
  vanishing at m − i points of an interval of length (m − 1)h, so |(f − P)^(i)(u)| ≤ M_m ((m − 1)h)^(m−i)/(m − i)!
  (divided differences), and C*_(i,m) := min_κ [Λ_(i,m) κ^(−i) + ((m − 1)κ)^(m−i)/(m − i)!] serves; with the
  Chebyshev-Lobatto nodes on [u − H, u] at i = 1, whose differentiation row sums to n² (Markov's bound, certified at n =
  1455), C^Ch_(1,m) := min_κ [2(m − 1)² κ^(−1) + κ^(m−1)/(m − 1)!] serves (deduced; lamL5 L3 checks both on exp(−1/x)
  as W1 did; control: the bound without interpolation fails). At m = 1456: log10 C_(1,m) = 4601.97 (round 1), 435.27
  (C*), 3.90 (C^Ch).
- **A16 (nits, programs).** layerwin5's docstring lemma numbers (L.6 → L.5, L.7 → L.6) and the printed name of (e6)
  (L.4's hypothesis) corrected; layerlin5.out regenerated without the `exit 0` line.
- **A17 (nit).** P1 (R2.8): "the no-return property of the first sentence" — that sentence concerns g0. Read "the
  no-return property that Proposition 3.2 states for μ0 > √72 l5²" (R3.6).

### R3.2 The layer, region by region

**(a) Notation.** x := v − v_s; E(v) := sup_(v'≤v) env; v is a *first-reach point* if env(v) = E(v) > E(v') for v' <
v; ε_c(v) as in R2.1; R(v, ω) := λ³ A env(v) |ν(v − τ0)| |d(θ)| / m0(v); ϑ := v/λ. The layer is v_s < v < v_s + η_λ
(E.3 (c)); m0 < 2 C_Φ λ there.

**Proposition L.12 (the layer outside the window; deduced, with layerband5 B1-B2).** Let K ≥ 6, N = K + 3, M := M*,
δ ∈ (0, 1/2), P > 4 and m ≥ max(56 M, (P + 1) M). There is λ_U > 0 such that for λ ≤ λ_U, every v in the layer
v_s < v < v_s + η_λ and every ω ∈ S³:

- (i) *(upper layer)* if E(v) ≥ λ^(σ_K − δ), σ_K := min(3, (K − 3)/2), the boundary is spacelike for g_λ at (v, ω),
  whether or not env vanishes at v;
- (ii) *(every level)* if v is a first-reach point with λ^P ≤ env(v) ≤ λ^(3+δ), then on [v, v + 4πλ] the boundary has,
  at ω, points where it is timelike and points where it is spacelike (generic case ρ(v_s) ≠ ρ*; at ρ*, with the
  exponent 1 + 2/κ of round 1);
- (iii) *(the band, K ≥ 10)* if λ^(3+δ) ≤ E(v) ≤ λ^(3−δ), then g_λ⁻¹(dΦ0, dΦ0) = −m0 − λ³ A env ν Re[d e^(iϑ)] + ρ
  with |ρ| ≤ λ^γ m0, γ := 1/10 at δ = 1/10 (B2): where R ≥ 1 + 2λ^γ the boundary has timelike points at ω within the
  carrier period about v; where R ≤ 1 − 2λ^γ it is spacelike at (v, ω).

*Proof.* (i) Lemma L.1 and Corollary L.11 hold on v_s < v ≤ v_♯ with w a free remainder, which Theorem E (Step 1, READ)
bounds by C M λ^(K−3) on Ω. Lemma L.5 at the point v gives ε_M(v) ≤ C_ε E(v)^(1−M/m) and ε_1(v) ≤ C_(1,m) E^(1−1/m)
M_m^(1/m). The margin is controlled by E, not by env(v): let v_m ≤ v with env(v_m) = E(v); env ≥ E/2 on [v_m −
E/(2ε_1), v_m], an interval inside [v_s, v] since env(v_s) = 0; so ∫_(v_s)^v env² ≥ E³/(8 ε_1) (B1, sampled on three
envelopes, two with zeros; control: 1/8 in place of 8 fails), and, μ − μ0 ≤ μ0 in the layer for λ small, m0 ≥ √(μ/μ0)
− 1 ≥ (μ − μ0)/(3μ0) ≥ c E^(2+1/m), c :=
A²/(108 μ0 C_(1,m) M_m^(1/m)). Every other term of −k(Φ0♯, Φ0♯) + q is at most C(λ³E + λ⁴C_ε E^(1−M/m) + λ C_ε²
E^(2−2M/m) + M λ^(K−3)), and B2 (i) checks each exponent against c E^(2+1/m) for E ≥ λ^(σ_K − δ), every K in [6, 40]
(control: σ = 3 at K = 6 fails the w-condition). (ii) Round 1's section 7 at the level y := env(v) = λ^p in place of
λ^14, with round 2's lemmas: its conditions (e1)-(e8) are linear in p, B2 (ii) checks them at p = 3 + δ and p = 50 (m =
56 M, K = 6), so they hold on the whole range with constants uniform in p (control: p = 3 fails (e6), L.4's
hypothesis). (iii) As (i), keeping both m0 and the λ³ term; B2 (iii) checks every error exponent above (3 + δ)(2 + 1/m)
+ γ for K ≥ 10 (control: K = 9 fails through Theorem E's w). ∎

**(b) The record's envelope.** CONSTANTS5's C_c^∞ envelope is increasing on [1/2, 2] (both factors of β increase on
y ∈ (−1, 0)), so every v there is a first-reach point and (ii) covers {λ^P ≤ env ≤ λ^(3+δ)} entirely; with K ≥ 10 the
layer is then decided except the very edge (below the level λ^P) and the transition |R − 1| < 2λ^γ. B3 draws the map for
an exp(−1/x) edge with unit constants and M* = 26: covered for K = 10 at λ = 10^(−1000) and 10^(−3000), a gap for K = 6;
at λ = 10^(−300) not covered even for K = 10, the degree-two error λ ε_26² of Corollary L.11 exceeding the margin
(computed, a model). The reach of (ii) is set by the record's derivative bookkeeping (M* derivatives at each order),
not by the expansion, which loses one derivative per order: B3's deepest window point lies far above x_b below.

**(c) The structure of the expansion (computed V1, V2; deduced).**

**Proposition L.13.** (a) At the seed, dRic^H and dD are of first order in ∂_v: R_X = −i T ∘ ∂_v + Q and D_X = Pol ∘
∂_v + q, with Q, q free of v-derivatives (V1, every T² × Z2 × Z2-invariant H; it rests on g0⁻¹(dv, dv) = 0; control:
T with its vv mass coupling halved leaves a v-derivative). (b) Write H_j = Σ_k env^(k)(v) c_(j,k)(r, r0, θ). Then
c_(j,j−2) = i^(j−2) c_(2,0) for j ≥ 2 and c_(j,j−3) = (j − 2) i^(j−3) c_(3,0) for j ≥ 3. (c) On the boundary, for j ≥ 3,

    H_j,vv(v, √μ0, θ) = (j − 2) i^(j−3) A d(θ) ν(v − τ0) env^(j−3)(v) + Σ_(k<j−3) (...) env^(k)(v),

so the top terms of the first-degree series Σ_j λ^j H_j,vv are λ³ A d ν Σ_k (k + 1)(iλ)^k env^(k): the expansion in
λ of λ (i/s)² [A d ν env], s := ∂_v + i/λ, (i/s) f (v) := i ∫_(−∞)^v e^(−i(v−v')/λ) f(v') dv'.

*Proof.* (a) is V1. (b) By (a), T(H_(j+1) − i ∂_v H_j) = −Q(H_j); and by the data rule H_(j+1) − i ∂_v H_j = −i (1 −
Π) ∂_v H_j + i Pol^+ q H_j on Σ_τ0, Π := Pol^+ Pol, a projector (Pol Pol^+ = 1, N2). Since H_j(r0) lies in the range of
Π for j ≥ 2, coefficient by coefficient, the top coefficient obeys c_(j+1,top+1) = i c_(j,top), and the next one e_(j+1)
= i e_j + i^(j−2) c_(3,0), the terms from the r0-dependence cancelling; induction. V2 runs the record's recursion on a
three-component system with this structure (a mass coupling, a gauge sector, a transported wave), with slice data and
with data from infinity, and finds both identities in every component to j = 9 (controls: R_X without its ∂_v part,
and slice data carrying i∂_v of the wave, fail). (c) H_2 ∈ S has no scalar part, nor has ∂_(r0) H_2; the scalar sector
of c_(3,0) at the horizon is A d ν (N5). ∎

**(d) What the expansion says at the very edge (computed V4, V5; a model with unit constants).** Let x_b(λ) be where λ
|env'/env| = 1. V4: x_b = (kλ)^(1/(k+1)) exactly for exp(−1/x^k), x_b ln(1/λ) decreasing towards 1 for exp(−e^(1/x)),
exponent 1/2 for the record's envelope (an exp(−3/(4x)) edge: x_b ≈ (3λ/4)^(1/2)), and x_b = 4λ(1 + o(1)) for sin⁴;
below x_b/2 the top terms of (c) increase with the order, above 3 x_b they decrease (control: "x_b ∼ λ^(1/2) for every
flat edge" fails for three classes). V5 (env = exp(−1/x), λ = 10^(−6)): in the window the truncated series agrees with
the re-summed F := λ (i/s)² env to 1.6·10^(−8); at x = 0.3 λ^(1/2) it is off by a factor 1.3·10^8 and two consecutive
truncations differ by 13 times the first, so **no truncation of the expansion is asymptotic on the very edge**, while
the local form λ (i/s̃)² env, s̃ := env'/env + i/λ, agrees with F to 1.8·10^(−3) = O(x). The phase of (i/s̃)² varies by
at most 4x per carrier radian (d/dv arctan(x²/λ) ≤ 2x/λ), so Re[c F e^(iϑ)] changes sign twice on every carrier period
at the very edge (three phases c), and |F| exceeds the margin's bound (E² + ∫E²)/9 by a factor above 10^1398 (control: c
= 0 leaves −m0 < 0). So the expansion, re-summed, predicts at the very edge what Theorem L proves on W_λ: alternation on
every column.

**(e) Theorem 1's solution: why no expansion decides the very edge (deduced, with V3, V5 (d), S4).**

**Proposition L.14.** On v − v_s < x_b the A-linear part of g_λ's data on Σ_τ0 at r0 = v − τ0 is Σ_(j≤N+1) λ^j H_j(r0)
plus U^(1), the A-linear part of Proposition 6.5's correction. (a) By L.13 its scalar sector's top term is λ^(N+1) (N −
1) i^(N−2) env^(N−2) c_(3,0)(r0), stage N's data. (b) Transported along ℓ to the horizon with T = 0 it gives the
factor ν_hom A d in place of c_(3,0), ν_hom = −μ0^(−7/4)/(4ρ⁶), never zero and not ν (V3); at x = 0.3 λ^(1/2), λ =
10^(−6), N = 9 the transported top term exceeds the re-summed first-degree value by a factor 2·10^7 (V5 (d): 1.7·10^(−13)
with ν_hom at P*, against 8.0·10^(−21) for the re-summed term with unit coefficient, per env). (c) The record bounds
U^(1) there only by C λ^(N−2) ε_(2N+3) (L.3 (e) with A4), larger again (7.3·10^98 per env, V5 (d); control: in the
window the ordering fails). (d) Stage N's data are left free by the record (R3.4); the two natural choices, Lemma 6.2's
rule at m = N or zero, change the top data term by a factor 12.7 at the very edge and by 0.04 in the window (S4).

So on the very edge the first-degree term of Theorem 1's g_λ is fixed by data set at orders invisible to Theorem 1,
which the record leaves free (stage N) or does not compute (U), and which change it at leading order. Since the margin
and every term of degree two are of order env², below any nonzero first-degree term polynomial in env and its
derivatives there, the sign is that of the first-degree term. **No expansion of the approximant decides the very edge
for Theorem 1's g_λ.** The quantity that decides it is a(v, ω) := the A-linear part of g_λ(∂_v, ∂_v) at (v, √μ0, ω):
where a ≠ 0, g_λ⁻¹(dΦ0, dΦ0) has the sign of −a. To leading order (Lemma H below), a is the T = 0 transport to r = √μ0
of the A-linear scalar data of g_λ on Σ_τ0 at r0 = v − τ0; with Lemma 6.2's rule at m = N and U^(1) left out it is
Re[λ^(N+1) (N − 1) i^(N−2) ν_hom A d env^(N−2) e^(iϑ)] (1 + o(1)), which alternates on every carrier period; U^(1)'s
part is the one uncomputed term (Lemma 6.4's radial system at first degree).

*Lemma H (stated, not proved).* On v_s < v < v_s + x_b, the A-linear solution whose data on Σ_τ0 are e^(iϑ) D(v), D
growing at the rate |D'/D| ≥ 1/λ with slowly varying log-derivative, equals at r = √μ0 the T = 0 transport of its data
times (1 + O(|s̃|^(−1)) + O(x)). It is the complex-frequency form of round 1's transport (the ∂_v-free operators of L.13
(a) being O(|s̃|^(−1)) against T), and it is not in the record.

**(f) Theorem 2's solution (deduced; conditional).** Its A-linear part (the derivative in A at A = 0, where it exists)
is the linear solution with nothing coming in but the wave: two such solutions differ by one whose energy tends to zero
in the past, hence vanish (the argument of L.4_P (2)); so it does not depend on N_P and carries no truncated data. Its
λ-series has L.13's structure with the transports from infinity (V2's second run), so its re-summed horizon value is λ
(i/s̃)² ν∞ A d env (1 + O(x)). *If* the seed's linear response at the horizon to an incoming e^(sv) wave has its
expansion in powers of 1/s uniformly for s in the closed first quadrant (Lemma H_P) and a degree-two form of L.4_P
holds (|w − w^(1)| ≤ C λ^(−q) ε_M(v1)², by the same energy argument with sources quadratic in the profiles), then on
every column the boundary has timelike and spacelike points in every carrier period of the very edge, down to v_s:
Theorem L_P's conclusion holds on the whole very edge. Neither lemma is proved here.

### R3.3 λ_L made explicit (O4)

**The formula (deduced from round 1's section 7 with round 2's lemmas; computed lamL5 L4).** In the generic case, with
p = 14, m = 56 M, Δτ := τ_end − τ0, G := 3 A ν_* d_*/32, ν_* := min |ν| on W_λ, d_* := min |d|:

    λ_L = min{ λ0, 1/(2 C1), Λ_4, Λ_5, Λ_6, Λ_8a, Λ_8b, Λ_8c, Λ_8d },
    Λ_4 = [ 8 · 2^(−1/m) C_(1,m) M_m^(1/m) (4π + 2 C1 Δτ) ]^(−m/(m−p))                     (Lemma L.6's hypothesis)
    Λ_5 = min_(i≤M) [ (M + 1) C_(i,m) (5/4)^(1−i/m) M_m^(i/m) ]^(−1/(p(1−i/m) − 3))           (L.4's hypothesis)
    Λ_6 = (288 μ0 C_Φ / (25 A²))^(1/(2p−1))                                                 (the window in the layer)
    Λ_8a = (3 A ν_* d_* / (100 C_m0))^(1/(p−3)),  C_m0 := (A²/(9μ0))(1 + (μ0 μ_end)^(1/4))   (the margin, D3)
    Λ_8b = (G/(C_L11 C_ε))^(4/3),  Λ_8c = (G/(C_L11 C_ε²))^(1/11.5),  Λ_8d = (G/(C_L4 C_ε))^(4/3)   (errors, N = 9)
    C_ε := Σ_(i≤M) C_(i,m) (5/4)^(1−i/m) M_m^(i/m)   (ε_M(v1) ≤ C_ε y^(1−M/m), Lemma L.5)

(each of Λ_8a-d makes its error at most an eighth of the signal's lower bound λ³ A (3y/4) ν_* d_*; the exponents 4/3,
1/11.5 are 1/(1 − pM/m), 1/(p − 2 − 2pM/m) at N = 9; at the double root ρ*, y is replaced by y^(1+2/κ) in the signal).

**Its factors at P* (computed, exact or certified).** The paper's envelope sin⁴(π(v − 1/2)/3) is not flat at its edge:
its one-sided derivatives at v_s are 0, 0, 0, 0, 24(π/3)⁴, 0, −480(π/3)⁶ and vanish to the left, so env^(4) jumps by
28.86, env is C³ and not C⁴, M_m = ∞ for m ≥ 5, and Theorems 1 and L do not apply (L1; control: the C_c^∞ envelope has
|env^(4)| < 10^(−100) at v_s + 10^(−3)). With CONSTANTS5's C_c^∞ envelope (the same ∫ env², R2.2 (a) there): M_1456 ≤
B(1456), log10 B(1456) = 8573.894, by Cauchy's estimate on discs of radius θ(1 − |y0|), θ = 1 − 2^(−39) (certified,
interval arithmetic; B(k) ≥ e_k/2 for k ≤ 14, consistent with CONSTANTS5's sampled values; at m = 400 a power-series
value of |env^(400)| at one point, stable between 200 and 280 digits, lies 10^41 below B; control: B without m! lies
below it). ν_* = |ν(5/2)| = 196/15625, because dν/dρ = −(ρ² + 2)(2ρ³ − 3ρ² − 2)/(6ρ⁷) makes |ν| increase on ρ > ρ*
and W_λ lies in ρ ≥ 5/2 (so round 2's condition (iii) of O4, the modulus of ν near the edge, is void at P*); d_* = 8/3
at ζ = 0 (exact, from the real critical points); C_m0 = 0.226972. Then:

| term | round 1's L.5 | amended L.5 (A15) |
|---|---|---|
| log10 C_(1,m); log10 C_(26,m) | 4601.97; 4522.89 | 3.90 (Chebyshev); 460.02 (C*) |
| Λ_4 at C1 = 0 (an upper bound of Λ_4) | 2.44·10^(−4655) | 1.25·10^(−12) |
| Λ_5 | 7.61·10^(−436) | 6.66·10^(−58) |
| log10 C_ε | 4676.10 | 613.22 |
| Λ_8a | 0.611 | 0.611 |

**What λ_L is.** At P*, with the amended Lemma L.5,

    λ_L = min{ λ0, 1/(2 C1), 1.25·10^(−12) (1 + 0.945 C1)^(−1.0097), 6.66·10^(−58), (11.52 C_Φ)^(1/27), 0.611,
               10^(−820.96) min(C_L11, C_L4)^(−4/3), 10^(−106.86) C_L11^(−1/11.5) }.

Certified: the λ_L that rounds 1-2's proof delivers is below 2.5·10^(−4655), and with A15 below 6.7·10^(−58), whatever
Theorem 1's constants are (each a bound on the threshold this proof delivers, CONSTANTS5 V-M2, not on the largest λ for
which Theorem L holds). Unevaluated: λ0 and C1 of Theorem 1 (CONSTANTS5.md, read at its current state: λ0 is
constructive and has no number; at P* the λ0 of its proof is below 0.0239; C1 comes from Theorem 1's C, not evaluated),
C_Φ (from C1) and C_L11, C_L4, the constants of Corollary L.11 and Lemma L.4, built from Theorem A's profile bounds,
Theorem E's M and Lemmas 2.3, 2.4, 6.4 and Proposition 6.5's C0, the leaves CONSTANTS5 1.5 lists as uncomputed. If those
are at least 1 (not shown), λ_L ≤ 10^(−820) at P*. The binding envelope cost is C_ε, from M_m^(M/m) = 10^153 and the
equally spaced C*_(26,m); the 26 derivatives the record's bookkeeping carries at the window are what make λ_L so small
(R3.2 (b)), not the flat edge as such.

### R3.4 Stage N's data (O6)

READ (`N1STAR-PROOF.md`, located by content; stagen5 S1 prints the md5 and lines at each run, at this writing
02e76176…: lines 543, 610-611, 631, 634, 756, 802, 809; the file is being edited by another job and its lines move,
fc53b76a… an hour earlier had 540, 607-608, 628, 631, 753, 799, 806): section 5.4
solves "the stages m = 1, ..., N (Lemma 5.3), with gh_{N+1} from stage N"; Lemma 6.2 states stage data "for every N",
but its proof begins "Stage m = 1, ..., N - 1"; Lemma 6.1 needs (F1) at orders 1, ..., N − 1 and (F2) at 1, ..., N − 2;
Proposition 6.5 and section 6.4 take "the stage data of Lemma 6.2 with N := K + 3"; section 6.4 states that the data
equal the seed's on Σ ∩ {r < v_start − τ0}.

*Settled (deduced; computed S2-S3).* By the weights of Lemma 5.1, stage N's unknowns enter D at order ≥ N and the
constraint map at order ≥ N − 1 (gh_(N+1) through the λ⁻² Pol-combination; m_N, φ_N through e_N, which stage N's own
transport makes zero): past (F1) and (F2) and inside Lemma 6.1's O(λ^(N−2)) (S2; control: stage N − 1's gh_N enters D at
order N − 1, which (F1) constrains). So Theorems A, D, E, and Theorem 1, hold for every smooth choice of stage N's data.
Lemma 6.2's step at m = N runs inside Theorem A of order N: after stage N, Rm^(N) = −(1/2) e_(N+1) ∂_θ² W with e_(N+1)
= −q_(N+1) independent of θ, of θ-mean zero, which is all step (iii) uses (S3; control: a θ-dependent coefficient). The
rule is therefore: **stage N's data by Lemma 6.2's step at m = N** (equivalently, Lemma 6.2 read with N + 1, whose
stage-N data do not depend on later stages). *The precise gap in the supplement:* it leaves stage N unspecified, and
section 6.4's seed-data claim needs stage N's data to vanish on Σ ∩ {r < v_start − τ0}, which this rule (or zero
data) gives and an arbitrary choice does not. Round 2's R2.1 used this rule; its L.3 (e) bounds hold for it at m = N by
the proof at m < N. *Consequence:* the choice (the rule, or zero data) is invisible in the layer, entering at relative
order λ/x² (0.04 at the window, S4), and decisive on the very edge (12.7 at x = 0.3 λ^(1/2), S4; R3.2 (e)).

### R3.5 Open items, exactly

- **O1** (rewritten). *Decided:* the very edge for Theorem 1's g_λ is not decidable by any expansion of the approximant
  (L.14); the deciding quantity is a(v, ω) of R3.2 (e), which depends there on stage N's data and on U^(1). *Still
  open, with the obstruction:* (O1a) the sign of a on v − v_s ≲ x_b for Theorem 1's g_λ (needs U^(1), the A-linear
  part of Proposition 6.5's correction near r0 = v_s − τ0, and Lemma H); (O1b) the very edge for Theorem 2's solution
  (needs Lemma H_P and a degree-two L.4_P; then decided, alternating); (O1c) for 6 ≤ K ≤ 9, the band λ^(3+δ) < E <
  λ^(σ_K − δ), where Theorem E's |w| ≤ C M λ^(K−3) competes with the margin and L.4 does not apply (ε_M > λ³); (O1d) for
  envelopes not increasing at the edge, the points with E ≤ λ^(3+δ) that are not first-reach points (dips, interior
  zeros; at a simple zero the leading first-degree term is λ⁴ · 2i A d ν env', L.13, not analysed); (O1e) the
  transition |R − 1| < 2λ^γ of the band; and, for a fixed λ, the levels below λ^P (L.12 (ii) reaches them as λ_U(P)
  decreases; only below x_b is the obstruction intrinsic).
- **O2.** Rounds 1-2 read by vE2 (R3.1); round 3 awaits a reader.
- **O3.** Closed (R2.7), K∞ confirmed independently (vE2).
- **O4.** Closed as far as the record allows (R3.3): λ_L explicit; unevaluated λ0, C1, C_Φ, C_L11, C_L4.
- **O5.** Answered for the (v, x) convention (A3, F2): ν changes, its admissible range has no root; the supplement fixes
  (τ, x) (READ, Lemma 6.2 (i)), and ν∞ does not depend on the convention.
- **O6.** Settled (R3.4).

### R3.6 Proposed paper text (replaces R2.8's P1 and P2; P3-P6 stand, with P3's list extended)

(P1′) Proposition 3.2: replace the sentence from "If μ0 = √72 l5² exactly, the" to "Propositions E.2-E.4)." by:

> If μ0 = √72 l5² exactly, the boundary coincides with the seed's horizon for v ≤ v_start and is null there; g_λ equals
> the seed on {v ≤ inf supp env}, so it is null for g_λ too; after the shell starts it is spacelike for g_λ outside a
> layer whose width tends to 0 with λ (supplement `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that
> layer it is not spacelike throughout: for λ small every column has points where it is timelike for g_λ, so the
> no-return property stated above for μ0 > √72 l5² fails at equality (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L
> and L_P, Corollary L.7).

(P2′) Section 9: replace the bullet "**The boundary at equality.**" by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced, supplement `docket68/n1star/EQUALITY5.md` and
>   `EQUALITY5-LAYER.md` [†]; computed, `checks/eq5.py`, `eqlayer5.py`, `layerlin5.py`, `layerwin5.py`, `layerdeg5.py`,
>   `layernull5.py`, `layerpast5.py`, `layerledger5.py`, `layerfix5.py`, `layerband5.py`, `veryedge5.py`, `lamL5.py`,
>   `stagen5.py`): g_λ is the seed on {v ≤ v_s}, v_s := inf supp env, and x_K = 1 is spacelike for g_λ on {v ≥ v_s + η}
>   once λ ≤ λ_η. In the layer between, x_K = 1 is spacelike wherever sup_(v'≤v) env ≥ λ^(min(3, (K−3)/2) − δ); on
>   every column it has timelike points within 4πλ of each point where env first reaches a level λ^p, 3 + δ ≤ p ≤ P
>   (every point of that range when env increases at its edge); and for K ≥ 10 the band between is decided by the ratio
>   of λ³ A env |ν| |d| to the margin, d the double divergence of the waves' angular tensor (|d| ≥ 8/3) and ν a
>   coefficient depending on τ0 and on the gauge data's convention (ν∞ = −μ0^(−7/4)/9 for Theorem 2's solution). So
>   some future timelike curves of g_λ cross x_K = 1 into D_T, and Proposition 3.2's no-return property fails at
>   equality; a domain O(λ)-close to D_T, inside x_K ≤ 1, has an inner boundary that no future causal curve enters
>   (EQUALITY5.md, Proposition E.4), and the spheres' horizon holds as there stated. Not settled, with the obstruction
>   identified: the very edge, where λ|env'/env| ≳ 1 (v − v_s ≲ λ^(1/2) for the record's envelope), on which no
>   expansion in λ is asymptotic and the first-degree term of Theorem 1's solution is fixed by data the construction
>   sets at its top order (stage N's data and the correction U); for 6 ≤ K ≤ 9 a band where Theorem 1's remainder bound
>   competes with the margin; and the value of λ_L, explicit in Theorem 1's constants, which are not evaluated (the
>   envelope's own terms put it below 10^(−57)).

[†] as in R2.8: "(rounds 1-2 read by an independent verifier; round 3 not yet read)". (P3′) Appendix A, C, D: add
`checks/layerfix5.py` F1-F4, `checks/layerband5.py` B1-B3, `checks/veryedge5.py` V1-V5, `checks/lamL5.py` L1-L4 and
`checks/stagen5.py` S1-S4 beside round 2's entries (about half a minute, a minute, two minutes, four minutes and a few
seconds), each with its controls as in its docstring.

### R3.7 Labels and sources (round 3)

*Labels.* Computed: V1-V3, F1-F4, B2, S2-S3, L1, L3 (exact); L2, L4 (certified, interval arithmetic; L2's m = 400
value in floating point at 200 and 280 digits); V4, V5, B3, S4 (mpmath; V2, V5, B3, S4 are models, V2 of the algebra
with the record's structure, V5, B3, S4 with unit constants); B1 sampled. Deduced: Propositions L.12-L.14, the
re-summation of R3.2 (d), R3.2 (f) (conditional on Lemmas H_P and a degree-two L.4_P, stated, not proved), the formula
of R3.3, the settlement of R3.4, amendments A1-A17. READ: the verifier's report (verdicts, as relayed); `N1STAR-PROOF.md`
sections 5.4, 6.1-6.4 (Lemmas 6.1, 6.2, Proposition 6.5); CONSTANTS5.md sections 0, 1.3-1.5 and Round 2 R2.2 (λ0's
status, the C_c^∞ envelope and its constants, P*); the paper's Proposition 3.2 and section 9 (RESPONSE-HL-5D.md lines
296-305 and 1532-1542 at this reading).

Files (round 3): this section; `checks/veryedge5.py`, `checks/layerband5.py`, `checks/lamL5.py`, `checks/stagen5.py`,
`checks/layerfix5.py`, each with its `.out`; `checks/layerwin5.py` and `checks/layerlin5.py` changed as stated above.

## Round 4

Status: written (round 4, 2026-11-02); not yet read by an independent verifier. Round 3 was read by one (the verifier
of round 3, vE3; scripts kept outside the record); its findings are seated in R4.6, each re-derived before it was
accepted. New programs, each with a docstring stating its claims, controls and labels; all pass and every control fails
(`.out` beside each): `checks/edgeP5.py` Q1-Q4, `checks/stagefree5.py` G1-G4, `checks/bandL4p5.py` H1-H4,
`checks/lamL5b.py` M1-M5. Changed on the verifier's findings and rerun: `checks/layerlin5.py` (N5, N6 controls),
`checks/layerpast5.py` (P3 control), `checks/layerdeg5.py` (D4 control), `checks/layerfix5.py` (F1 print, F3 control,
F4), `checks/layerband5.py` (B3 with M = 2N + 8), `checks/veryedge5.py` (V5 (d) sums to 2N + 3), `checks/lamL5.py`
(docstring and labels: its thresholds are lower bounds). The text of rounds 1-3 is kept; this section amends it.

### R4.0 Findings

1. **Theorem 2's very edge is decided (Theorem L_E, R4.1).** For an envelope whose logarithm is concave near v_s and
   whose log-derivative κ obeys |κ'| ≤ c κ^(1+α), α < 1 (the record's C_c^∞ envelope: α = 1/2), the boundary has, on
   every column, timelike and spacelike points in every interval of length 4πλ whose envelope stays below λ^(P0), down
   to v_s; with Proposition L.12 (ii) run for Theorem 2, in every such interval below the level λ^(3+δ). The
   first-degree term is not expanded but computed: it is λ A ν∞ Re[d e^(iv/λ) s^(−2) env] plus terms that an energy
   estimate bounds (Lemma L.15_P), and the one-dimensional integral s^(−2) env equals env/s̃² up to a relative error at
   most c' κ^(α−1), for every λ (Lemma L.16). Round 3's Lemma H_P is not needed and is not proved as stated; its
   degree-two lemma is written at the level of the record's sketches (Lemmas L.17_P, L.18_P).
2. **Theorem 1's very edge is not determined by the supplement as written (Proposition L.19, R4.2).** Stage N's data are
   free there. Adding to stage N's mean the Cauchy data of ±2A ∇∇f, f a solution of the seed's scalar wave equation
   with profile ψ = env^(2/3) (smooth, symmetric, zero where the waves are), changes g_λ's A-linear part by exactly
   ±2λ^N A ∇∇f (a pure-gauge solution in the harmonic gauge; U unchanged at first degree), whose horizon value is
   ±2λ^N A μ0^(−3/4) ψ'' (1 + o(1)), sign-definite. It dominates the layer's deep part, so the two choices make the
   boundary spacelike, respectively timelike, there on every column (computed model: from 3λ above v_s up to the level
   λ^18.7 at λ = 10^(−1000), K = 6). No Lemma H is used. Under the O6 amendment, which fixes stage N's data, this
   freedom is gone and the sign of a(v, ω) is open: it needs U at first degree and a slice-data form of Lemma H, neither
   of which is obtained here (R4.2 (b)).
3. **The band 6 ≤ K ≤ 9 is an artefact (Lemma L.4', R4.3).** Lemma L.4's hypothesis ε_(M*)(v1) ≤ λ³ serves only to bound
   ∂³g_app and ∂⁴g_app; they multiply lower derivatives of w, and a triangular Gronwall needs only ε_4(v1) ≤ λ, with the
   same conclusion |w| ≤ C λ^(N−5) ε_(M*)(v1). Proposition L.12 then holds with σ_K = 3 and with (iii) for every K ≥ 6,
   once its parameters are taken as the verifier of round 3 requires (m and κ growing with P and 1/δ; H4).
4. **O6 (R4.4):** the amendment is the verifier's text at N1STAR-PROOF.md line 634 (Lemma 6.2's proof), which section
   6.4 cites; section 6.4 itself then needs no change. Nothing in Theorem 1 or the paper changes; the metric that
   Theorem 1's construction names becomes unique, and Theorem L, Proposition L.12 and Theorem L_E concern that metric.
5. **λ_L (R4.5).** The direction of round 3's certification was wrong (verifier, M2): computed with an upper bound of
   M_m, those thresholds are lower bounds. With a lower bound of M_m (Taylor at the flat edge, log10 M_1456 ≥ 8091.60),
   CONSTANTS5's λ0 < 0.0024433 and Lemma L.4', the threshold this proof delivers is certified below 2.71·10^(−12), and
   below 10^(−285.27) max(C_L11, C_L4)^(−4/3) with Chebyshev-Lobatto interpolation (Duffin-Schaeffer). C_Φ ≤ 5.6034 C1
   at P*; C_L11, C_L4 cannot be evaluated (the obstruction is λ0's).
6. **Open items** are stated exactly in R4.7; proposed paper text in R4.8.

### R4.1 Theorem 2's solution at the very edge (task 1)

*Setting.* g0° is the seed with μ ≡ μ0 (static). Its linearised operator satisfies dRic^H(h) = −P ∂_v h + Q h for every
T² × Z2 × Z2-invariant h(v, r, θ), with P := i T (T the transport of L.2 (b); P = ∇_ℓ + 3/(2r) plus the mass
couplings) and Q free of ∂_v (computed, V1). P_∞⁻¹ S is the solution Z of P Z = S with r^(3/2) |Z|_cart → 0 along the
generators (the supplement's Lemma 9.7 (d), READ); B := P_∞⁻¹ Q. Both act in (r, θ) at fixed v, so B commutes with
∂_v. Put H_1 := A env r^(1/2) T, b_n := B^n (r^(1/2) T), s := ∂_v + i/λ acting on functions of v, and

    I_n(v) := (s^(−n) env)(v) = ∫_0^∞ u^(n−1)/(n−1)! e^(−iu/λ) env(v − u) du,     I_0 := env,     s I_n = I_(n−1).

h^(1) is the solution of dRic^H(h) = 0 on P ∪ Ω whose incoming radiation is that of the wave Re[λ H_1 e^(iv/λ)] and
nothing else (zero on v ≤ v_s, E.2_P); it is what R3.2 (f) calls the A-linear part of Theorem 2's g_λ, and below it is
used only through Lemma L.17_P, so no differentiability in A is needed.

**Lemma L.15_P (exact re-summation; deduced, with edgeP5 Q1 and layerpast5 P1-P3).** (a) The profiles H_j^∞ of R2.7 are
H_2^∞ = −i B H_1 and H_(j+1)^∞ = i (∂_v − B) H_j^∞ (j ≥ 2): Σ_j λ^j H_j^∞ is the expansion in λ of λ (s − B)⁻¹ s H_1.
(b) For M ≥ 1 put h_M := Re[λ e^(iv/λ) A Σ_(n≤M) I_n(v) b_n(r, θ)] and e_M := h^(1) − h_M. Then

    dRic^H(e_M) = −Re[λ e^(iv/λ) A I_M(v) (Q b_M)(r, θ)],     e_M = 0 on {v ≤ v_s},     nothing coming in,

and at every X ∈ Ω with v(X) ≤ v_♯: |e_M(X)| ≤ C_M λ sup_(v'≤v(X)) |I_M(v')|. (c) b_0 and b_1 have no vv, vr, rr
component, and b_2,vv(√μ0, θ) = −ν∞ d(θ), ν∞ = −μ0^(−7/4)/9.

*Proof.* (a) From T(H_(j+1)) = −R_X(H_j), R_X = −i T ∂_v + Q (V1) and T = −i P: P H_(j+1) = i P ∂_v H_j − i Q H_j; and
P_∞⁻¹ P ∂_v H_j is ∂_v H_j for j ≥ 2 and 0 for j = 1 (H_1 is the homogeneous transport, the one profile that does not
decay). Q1 checks the closed form against the record's recursion to j = 10 in V2's model, every component; λ (s − B)⁻¹ s
H_1 = λ Σ_n s^(−n) B^n H_1 with s^(−n) = (λ/i)^n (1 − iλ∂_v)^(−n) has exactly these coefficients. (b) d/dv (e^(iv/λ) X)
= e^(iv/λ) s X and P, Q are free of ∂_v, so dRic^H(e^(iv/λ) X) = e^(iv/λ)(−P(s X) + Q X); with X = λ A Σ_(n≤M) I_n b_n,
s I_n = I_(n−1), P b_0 = 0 (T(H_1) = 0) and P b_n = Q b_(n−1) (the definition of B), −P(s X) + Q X telescopes to λ A I_M
Q b_M (Q1: P B^n H_1 = Q B^(n−1) H_1 for n ≤ 6). h_M carries the wave as its term n = 0 and b_n (n ≥ 1) decay (Q1; L.3_P
(a_P)), so e_M has nothing coming in; I_n and h^(1) vanish on v ≤ v_s. For the bound: the energy estimate of the static
seed's linear operator on P_v ∪ Ω_v with the null face {v' = v} kept (L.8 on Ω_v, the supplement's Lemma 9.5 on P_v as in
L.3_P (b_P), READ), then L.10 along the generator: |e_M(X)| ≤ C Σ_(|β|≤2) ∫ ‖Ω^β(source)(τ)‖ dτ; the source is λ A
I_M(v') Ω^β Q b_M with Q b_M ∈ E_3, whose L² norms on the slices of P_v are integrable in τ (E5). No tilt is needed: the
operator is g0°'s. (c) N3, P1 (H_1, H_2^∞ ∈ S) and P3 (H_3,vv^∞ = A env d ν∞ at the horizon; H_3^∞ = A env' b_1 − A env
b_2, and b_1 has no vv component). ∎

**Lemma L.16 (the kernel lemma; deduced, elementary; edgeP5 Q2).** Let env > 0 and log-concave on (v_s, v_s + x0], κ :=
(log env)' > 0; for v there put x := v − v_s and s̃ := κ(v) + i/λ. For every λ > 0:

- (a) |I_n(v)| ≤ env(v)/κ(v)^n for n ≥ 1;
- (b) I_2(v) = env(v) s̃^(−2) (1 + ρ_2), |ρ_2| ≤ R_2(v) := ∫_0^x [κ⁻¹(ψ'' + ψ'²) + ψ' + u(ψ'' + ψ'²)] env(v − u)/env(v)
  du, where ψ'(u) := κ(v − u) − κ(v) ≥ 0 and ψ''(u) := −κ'(v − u) ≥ 0; R_2 does not depend on λ. If |κ'| ≤ c_R κ^(1+α) on
  (v_s, v], α ∈ (0, 1), then R_2 ≤ 3·2^(1+α) c_R κ^(α−1) + 2^(5+2α) c_R² κ^(2α−2) + T(v), T the integral beyond U_* :=
  (1 − 2^(−α)) κ^(−α)/(α c_R), at most a multiple of x (1 + x) sup_(v'≤v−U_*) (κ² + |κ'| + κ)(v') env(v')/env(v), which
  for a flat edge is smaller than every power of 1/κ (env(v − U_*) ≤ env(v) e^(−κ U_*));
- (c) if moreover |env^(j)| ≤ c_j κ^j env and κ(v')^j env(v') ≤ c_j κ(v)^j env(v) e^(−κ(v)(v − v')/2) for v_s < v' ≤ v
  and j ≤ n + 1, then |I_n(v)| ≤ C_n env(v) λ^n (1 + λκ); with (a), |I_n| ≤ C'_n env min(λ, 1/κ)^n.

*Proof.* (a) env(v − u) ≤ env(v) e^(−κu) (the tangent line of a concave logarithm), and ∫_0^∞ u^(n−1) e^(−κu)/(n−1)! =
κ^(−n). (b) Put e^(−ψ(u)) := env(v − u) e^(κu)/env(v) (zero for u ≥ x): ψ(0) = ψ'(0) = 0, ψ ≥ 0, and I_2/env − s̃^(−2) =
∫_0^∞ u e^(−s̃u)(e^(−ψ) − 1) du. Two integrations by parts against e^(−s̃u) — the boundary terms vanish, at u = 0 by
ψ(0) = ψ'(0) = 0 and at u = x because env and env' vanish at the flat edge — give ρ_2 = −J_1 − s̃ J_2, J_m := s̃⁻¹
∫_0^x G_m' e^(−s̃u) du, G_1 := ψ' e^(−ψ), G_2 := u ψ' e^(−ψ). With |e^(−s̃u)| = e^(−κu), |s̃| ≥ κ and |G_m'| ≤ (R_2's
bracket) e^(−ψ), |ρ_2| ≤ R_2. On [0, U_*], κ(v − u) ≤ 2κ (comparison for dK/du ≤ c_R K^(1+α)), so ψ' ≤ c_R (2κ)^(1+α) u
and ψ'' ≤ c_R (2κ)^(1+α), and with e^(−ψ−κu) ≤ e^(−κu) the integral over [0, U_*] is at most the two displayed terms.
(c) Integrate I_n by parts n + 1 times against e^(−iu/λ): the boundary terms at u = 0 are (iλ)^n env(v) and λ^(n+1)
times env'(v); the remainder is λ^(n+1) ∫ |∂_u^(n+1)(u^(n−1) env(v − u))|/(n−1)!, a sum of ∫ u^(j−2) |env^(j)(v − u)|, j
= 2, ..., n + 1, each at most c'_j κ env(v) by the two hypotheses. ∎

Q2 samples (a)-(c) on exp(−1/x) (α = 1/2, c_R = 2), exp(−1/x²) (α = 1/3) and the record's C_c^∞ envelope (an exp(−3/(4x))
edge, log-concave on its whole support: both factors of log env are concave in t; α = 1/2, c_R = 2.309 sampled on x ≤
0.3), at λ = 10^(−3) and 10^(−6) and λκ = 10^(−2), ..., 10^4: |I_n| κ^n/env ≤ 1.0000, |I_n|/(env min(λ, 1/κ)^n) ≤ 1.0002,
|ρ_2|/R_2 ≤ 0.9999 (R_2 is attained as λκ → ∞, where nothing oscillates), R_2 κ^(1−α) ≤ 9.33. Controls: the frozen local
form s̃ := i/λ (the λ-expansion's leading term) is off by more than 1 at the very edge; s̃ built with 2κ violates (b).

**Lemma L.17_P (degree two; deduced, at the level of the record's sketches).** For Theorem 2's g_λ let r2 := g_λ − g0° −
h^(1) and v_1 := v + 4 C_P λ. At X = (v, r_q(v), ω), v_s < v ≤ v_♯,

    |r2(X)| + |(g0 − g0°)(X)| ≤ C_2 [ε_c(v)² + ε_c(v) η(v_1) + η(v_1)²],     η(v_1) := λ^(N_P−5) ε_(M_P)(v_1),

c a fixed cost; and m0 ≤ C(E(v)² + ∫ env²) (D3).

*Proof (sketch).* Ric^H relative to g0 = g0° + (μ − μ0) r⁻² dv² differs from Ric^H relative to g0° by terms linear in μ −
μ0 and μ' (local, at most C ε_0²). With Ric^H(g0° + u) = dRic^H(u) + 𝒩(u), |𝒩(u)| ≤ C(|u||∂²u| + |∂u|²) (indices and
angular derivatives included, |u|_(C¹) small): dRic^H(r2) = −𝒩(u) − (the μ-terms), u := g_λ − g0°, nothing coming in,
r2 = 0 on v ≤ v_s. The linear estimate of L.15_P (b), at g0° and so with no tilt, gives |r2(X)| ≤ C Σ_(|β|≤2) ∫ ‖Ω^β(𝒩(u)
+ μ-terms)‖. Split u = (g_app − g0°) + w: L.3_P (a_P)-(c_P) give |∂^k Ω^β(g_app − g0°)| ≤ C λ^(1−k) ε_c(v) on the past
set (local); L.4_P run with ∂^α, |α| ≤ 4 (its proof; the coefficients bounded on R_P by L.3_P and Theorem P's bounds on
∂^(≤3) w, the top derivatives of g_app by the triangular rule of L.4' below) gives |∂^k Ω^β w| ≤ C λ^(N_P−3−k)
ε_(M_P)(v_1), k ≤ 2. The products give the three terms (the approximant's part: |u||∂²u| ≤ (λε)(λ⁻¹ε) = ε²). ∎

**Lemma L.18_P (localisation; deduced, sketch).** Under Lemma L.16 (c)'s hypotheses, at every boundary point X with v −
v_s ≤ c_* λ the bounds of L.4_P used in L.17_P hold with v_1 replaced by v + δ, δ κ(v) ≤ 1, and so with ε_(M_P)(v_1) ≤ C
κ(v)^(M_P) env(v).

*Proof (sketch).* L.4_P's tilt 2 C_P λ serves only to give the face {v + εψ(τ) = v_1} a timelike conormal for g_λ; any
tilt above 2 sup |g_λ⁻¹ − g0⁻¹| over the region serves, with the same constants. On S(V) := (P ∪ Ω) ∩ {v ≤ V} that sup is
Δ(V) ≤ C(ε_c(V) + λ^(N_P−3) ε_(M_P)(V + 4 C_P λ)), smaller than every power of λ near v_s. Descend: with x_0 := c_* λ and
tilt Δ(v_s + 2x_0) the bound at depth x uses v + C Δ, which is local once x ≥ x_1 := C' Δ(v_s + 2x_0)^(1/2); repeat with
x_(k+1) := C' Δ(v_s + 2x_k)^(1/2), which tends to 0 faster than any geometric sequence. (Q4: at x = λ/10, λ = 10^(−6),
the unlocalised bound, squared, exceeds the first-degree term by 10^3553353; the localised one is below it by
10^(−4342893).) ∎

**Theorem L_E (the very edge for Theorem 2's solution; deduced from L.15_P-L.18_P, with edgeP5 Q1-Q4).** Let μ0 = √72
l5², K ≥ 6, g_λ the metric of Theorem 2, and env satisfying Lemma L.16's hypotheses (b), (c) on (v_s, v_s + x0]. There
are λ_E > 0, x0' ∈ (0, x0] and P0 (depending on K and the record's derivative costs) such that for λ ≤ λ_E, every v ∈
(v_s, v_s + x0'] with env(v + 4πλ) ≤ λ^(P0) and every ω ∈ S³: on [v, v + 4πλ] the boundary has, at ω, points where it
is timelike for g_λ and points where it is spacelike. In particular on the whole very edge {λκ ≥ 1}, down to v_s.
With Proposition L.12 (ii) for Theorem 2 (levels λ^p, 3 + δ ≤ p ≤ P0, at first-reach points; its proof is R2.7's with
the window ledger, which is monotone in N, at the parameters of H4): for an envelope increasing at its edge, as the
record's is, every interval [v, v + 4πλ] near the edge with env(v + 4πλ) ≤ λ^(3+δ).

*Proof.* At X = (v', r_q(v'), ω): Lemma L.1, k = h^(1) + r2 − (g0 − g0°), Φ0♯ = ∂_v + β0 ∂_r with β0 = O(ε²). By L.15_P
with M = 3,

    −k^(1)(Φ0♯, Φ0♯) = λ A ν∞ Re[d(θ) e^(iv'/λ) I_2(v')] + ρ',
    |ρ'| ≤ C λ (|I_3(v')| + sup_(v''≤v') |I_3(v'')| + ε² |I_2(v')|),

the terms n = 0, 1 having no vv, vr, rr component and b_2,vv(r_q) = −ν∞ d + O(r_q − √μ0). By L.16 (a), (c) (κ decreasing,
env increasing) |ρ'| ≤ C λ env(v') min(λ, 1/κ(v'))³; by L.16 (b) the main term is λ A |ν∞| |d| env |s̃|^(−2) Re[e^(iΘ)(1
+ ρ'')], Θ := v'/λ + arg(ν∞ d) − 2 arg s̃, |ρ''| ≤ R_2 + C min(λ, 1/κ) ≤ 1/4 for x0' small and λ ≤ λ_E (|s̃|^(−2) ≥
min(λ, 1/κ)²/2). Θ increases, dΘ/dv' ≥ λ⁻¹(1 − 2|κ'|/κ²) ≥ 1/(2λ), so on [v, v + 4πλ] it passes 0 and π modulo 2π; there
cos(Θ + arg(1 + ρ'')) ≥ cos 0.253, resp. ≤ −cos 0.253, and the main term is ±(at least 0.72) λ A |ν∞| d_* env |s̃|^(−2).
The terms of degree two (L.17_P, localised by L.18_P where v' − v_s < c_* λ; m0; q of L.1) are at most C κ^(2c) env² by
L.16 (c)'s derivative hypothesis, and C κ^(2c) env²/(λ env min(λ, 1/κ)²) is at most C λ^(−2c−5) env on {λκ ≤ 1} and
tends to 0 faster than every power of 1/κ on {λκ ≥ 1} for a flat edge: below a tenth of the main term once env ≤
λ^(P0), P0 := 2c + 6, λ small. Both signs of g_λ⁻¹(dΦ0, dΦ0) occur. ∎

Q3 runs this with unit constants (|ν∞ d| = 1/9, μ0 = A = 1, a degree-two term 10 (1 + λκ)² env² of either sign, J_2 =
e^(iv/λ) I_2 by exact Taylor steps) over three carrier periods at five depths, from the ordered regime (env = λ⁴) to λκ
= 1000, λ = 10^(−6), three phases of d: every period has timelike and spacelike points (30 cases). Controls: no
first-degree term, or a degree-two term 10^6 λ^(−3) times larger, leaves none.

*What became of R3.2 (f)'s two lemmas.* Lemma H_P (an expansion of the horizon response in powers of 1/s, uniform on the
closed first quadrant) is not proved: near Re s = 0 it is a high-frequency resolvent bound for the seed. It is not
needed: L.15_P puts the whole response in time-domain form and L.16 evaluates it for every λ. The degree-two form of
L.4_P is L.17_P; below c_* λ it needs L.18_P, because L.4_P's tilt reaches v + 4 C_P λ, where env can exceed env(v) by
more than every power of λ (Q4).

### R4.2 Theorem 1's g_λ at the very edge (task 2)

**(a) Proposition L.19 (stage N's free data decide the deep layer; deduced, with stagefree5 G1-G4; no Lemma H used).**
Let μ0 = √72 l5², K ≥ 6, N = K + 3, env with a flat log-concave edge as in Lemma L.16 (c), g_λ^rule Theorem 1's metric
with stage N's data by Lemma 6.2's rule (R2.1), and ψ ∈ C_c^∞, supported in [v_s, ∞), log-concave near v_s and less flat
than env (for the record's envelope ψ := env^(2/3), which is C_c^∞). Let f solve the seed's scalar wave equation □f = 0
on Ω with the Cauchy data on Σ_τ0 of f_3 := Σ_(n≤3) (∂_v^(−n) ψ) b_n^sc, b_0^sc = r^(−3/2), b_(n+1)^sc := P_sc,∞⁻¹ Q_sc
b_n^sc (G2), and let g_λ^± be built as g_λ^rule except that stage N's mean m_N takes the data of m_N^rule ± 2A ∇∇f on
Σ_τ0. Then:

- (i) g_λ^± are metrics of Theorem 1 as the supplement states it. Lemma 6.2's statement holds for them (its proof fixes
  stages 1, ..., N − 1 only; G4); Theorems A, D, E hold for every stage-N choice that is smooth, T² × Z2 × Z2-invariant
  and vanishes on Σ_τ0 ∩ {r < v_start − τ0} (R3.4, with the verifier's qualification, R4.6 V-m1); f depends on (v, r)
  only and vanishes on {v ≤ v_s}, so ±2A ∇∇f is such a choice, g_λ^± = g0 there, and every stage vanishes where the waves
  do.
- (ii) Their A-linear parts are h^(1)_± = h^(1)_rule ± 2 λ^N A ∇∇f exactly (h^(1) the linear solution with the A-linear
  data; no differentiability in A is used). For h := 2∇∇f: dD(h) = d(□f), dRic^H(h) = −∇∇(□f), and dRic(h) = 0 for every
  f (G1, all fifteen components), so h's induced data satisfy the linearised constraints, the A-linear part of the
  constraint map, and with it U^(1) = −L⁻¹ Φ^(1), do not change, the A-linear data of g_λ change by exactly the Cauchy
  data of 2λ^N A ∇∇f (the ∂_τ of lapse and shift being fixed by dD = 0, which h satisfies), and the harmonic-gauge
  Cauchy problem has one solution. The means' first-degree sources are θ-means of one oscillating factor (zero), so m_N's
  A-linear part solves the seed's linearised equation, as ±2A ∇∇f does.
- (iii) (∇∇f)_vv = ∂_v²f − (F'/2) ∂_v f − (F F'/2) ∂_r f, at r = √μ0 equal to ∂_v²f − μ0^(−1/2) ∂_v f; with □f_3 =
  −2 (∂_v^(−3) ψ) Q_sc b_3^sc (G2) and the energy bound for f − f_3 (zero data on Σ_τ0, ∂_v commuted), (∇∇f)_vv(v, √μ0)
  = μ0^(−3/4) ψ'' − (7/4) μ0^(−5/4) ψ' + ... = μ0^(−3/4) ψ''(v)(1 + O(1/κ_ψ)) > 0 near v_s: sign-definite, not
  oscillating.
- (iv) There are c_* and λ_F such that for λ ≤ λ_F, wherever 3 c_* λ ≤ v − v_s and 2λ^N ψ''(v) ≥ 10 B(v), B(v) the sum
  of every other term the record bounds at the boundary point — the rule's first-degree part, O(λ³ ε_(M*)(v)) (L.11);
  its degree-two parts O(ε²) and their change O(λ^(N−1) ψ_c ε_c); the remainder, by L.4 or L.4' applied to the new
  construction, O(λ^(N−5)(ε_(M*) + ψ_c ε_c)(v + c_* λ)); m0 — g_λ^+ makes the boundary spacelike on every column and
  g_λ^− timelike. For env = exp(−1/x), ψ = env^(2/3), N = 9, M* = 26 and unit constants (G3) that set is the whole range
  from 3λ to x_1, with env(x_1) = λ^23.4 at λ = 10^(−100) and λ^18.7 at λ = 10^(−1000) (the exponent tends to 3N − 9 =
  18 as λ → 0): it contains the very edge above 3λ and the levels below about λ^(3N−9). At Theorem L's window (env =
  λ^14) the new term is below a tenth of the signal λ³ env: Theorem L and L.12 (ii) at levels above about λ^(3N−9) hold
  for g_λ^± as for g_λ^rule. Control: ψ := env, as flat as env, dominates nowhere on the very edge.

So **the causal character of x_K = 1 on the very edge, and at every level below about λ^(3N−9), is not determined by
Theorem 1 as the supplement now states it**: the choice is stage N's data (here its mean), which the supplement leaves
free. The two choices are smooth, symmetric, vanish where the waves do, and change g_λ by a gauge term of size λ^N.

**(b) Under the O6 amendment.** With stage N's data fixed by the rule (R4.4) no free choice is left in the construction
(N := K + 3 in 6.4, Pol^+ fixed by Lemma 6.2 (i), U unique in its ball, Theorem E's solution unique), and a(v, ω) is
determined, with a(v, ω) defined through h^(1)_rule (the linear solution with g_λ's A-linear data on Σ_τ0). It is not
computed, and Lemma H is not proved. The obstruction, exactly: (1) U^(1), the solution of Lemma 6.4's system at first
degree whose source is the A-linear constraint residual of the truncated approximant, λ^N sym(dv ⊗ i D_X H_(N+1)) +
O(λ^(N+1)) (with the rule at stage N, D's first-degree part on Σ_τ0 is λ^(N+1) D_X H_(N+1), and (6.2)); (2) Lemma H_Σ:
for data e^(i(τ0+r)/λ) D(r) on Σ_τ0 with D log-concave and κ_D := D'/D ≥ 1/λ, the value at (v, √μ0) of the linear
solution equals the T = 0 transport of the ingoing part of the data at r0 = v − τ0, times (1 + O(κ_D^(α−1) + λ));
(3) the degree-two bound of L.17_P on Ω with slice data (U's quadratic part and g_app's degree-two profiles as data, L.3
(e)), which is L.17_P's argument and is not written. Lemma L.15_P does not extend to (2): the transport from Σ_τ0 at r0
= v − τ0 does not commute with ∂_v, and U^(1)'s data are not transport-consistent (their ∂_τ part is set by the
constraints), so the solution they generate has an outgoing part as large as its ingoing one, and an energy estimate
does not see that the outgoing part misses the horizon; separating the two needs an estimate the record does not have.

**(c) Remark L.20 (deduced, conditional on Lemma H_Σ).** Under the amendment every A-linear datum of g_λ on Σ_τ0 is a
first harmonic e^(i(τ0+r)/λ) times a function built from env and its derivatives at r (the stage profiles) or, for U^(1),
a radial solve of such a source, which Lemma L.16 localises on the very edge. With Lemma H_Σ, a(v, ω) = Re[e^(iv/λ)
env(v) Φ(v, ω)] with Φ a finite sum of c_t(ω) λ^(a_t) κ^(b_t) s̃^(−c_t)(1 + o(1)), whose phase moves by o(1) per carrier
period (Theorem L_E's argument for Θ). So wherever Φ's leading coefficient is not zero, the boundary alternates on
every carrier period of the very edge; its sign at a point, and whether that coefficient vanishes, need U^(1). The free
mean of (a) breaks exactly this structure: it is a θ-mean, not a first harmonic.

### R4.3 The band 6 ≤ K ≤ 9 (task 3)

**Lemma L.4' (the weighted remainder under a weaker hypothesis; deduced, with bandL4p5 H1).** Lemma L.4 holds with its
hypothesis ε_(M*)(v1) ≤ λ³ replaced by ε_4(v1) ≤ λ: for X ∈ R with r(X) ≥ q0, |w(X)| ≤ C λ^(N−5) ε_(M*)(v1).

*Proof.* Steps 1, 2, 5 and 7 of R2.5 do not use the hypothesis. Step 3 gives |∂^j(g_app − g0)| ≤ C(λ + λ^(1−j)
ε_j(v1)): bounded for j ≤ 2 (ε_2 ≤ λ), of size λ^(1−j) ε_j for j = 3, 4. Order the energies E_0, E_1, E_2 (E_i controls
∂^(i+1) w and ∂^i w). In ∂^i of step 2's equation, every coefficient of a w-factor of the same level is a derivative of
order ≤ 2 of g_λ or of order ≤ 1 of g_app, bounded; ∂³g_app and ∂⁴g_app occur only in ∂^(i−p) w ∂^(p+2) g_app (p ≥ 1),
∂^(1+a) g_app ∂^(1+b) w and the cubic Q-terms, each multiplying a w-factor of a strictly lower level. So E_0 obeys Lemma
2.3 with bounded coefficients, E_0 ≤ C λ^(N−3) ε_(M*)(v1), and E_i ≤ C(E_i(τ0) + ∫(‖∂^i Ric^H(g_app)‖ + Σ_(j<i) L_ij
E_j)) with L_ij ≤ C λ^(j−i)(ε_4/λ); inductively E_i ≤ C λ^(N−3−i) ε_(M*)(v1). Step 7 as written. ∎

H1 checks the bookkeeping exactly: 25 terms over the three levels, each a coefficient λ^e times ∂^k w with e ≥ max(k, 1)
− i − 1 at h = 1 (ε_4 ≤ λ^h); at h = 1/2 the term w ∂²g_app of level 0 fails (λ⁻¹ ε_2 a large Gronwall coefficient), and
the non-triangular rule (every coefficient into Gronwall) first holds at h = 3, Lemma L.4's own hypothesis.

**Proposition L.12, amended (deduced, with bandL4p5 H2-H4).** Take m := max(56 M, 4 P M, 4 M/δ) and κ := max(64, 8 P,
8/δ) in its proof (the verifier of round 3's M1; with round 3's m = 56 M and κ = 64, (e6) fails at p = 3 + δ for δ <
3/55, and at ρ* (e2), (e4) fail for p ≥ 21 and (e1) for δ ≤ 3/31; H4's control). With L.4', parts (i)-(iii) hold for
every K ≥ 6 with σ_K := 3, δ ∈ (0, 1/2):

- (i) where ε_4 ≤ λ, that is E ≤ λ^(s_A), s_A = (1 + δ)/(1 − 4/m), the margin c E^(2+1/m) beats the signal, λ⁴ε, λε²
  and w = λ^(N−5) ε up to E = λ^(3−δ); above λ^(s_A), Theorem E's |w| ≤ C M λ^(K−3) does, as in layerband5 B2 (i), for E
  ≥ λ^((K−3)/2 − δ); s_A ≤ (K − 3)/2 − δ for K ≥ 6, so the ranges overlap (H2, K in [6, 40]);
- (ii) the window conditions (e1)-(e8), with (e6) read as L.4''s p (1 − 4/m) > 1 (or L.4's p (1 − M/m) > 3), hold at
  p = 3 + δ and p = P, generic and at ρ*, for every K in [6, 40], δ in {1/100, 1/20, 1/10, 1/4, 1/2}, P in {50, 200}
  (H4; they are linear in p);
- (iii) in the band every error exponent, w's now N − 5 + (3 − δ)(1 − M/m), exceeds (3 + δ)(2 + 1/m) + γ for every K in
  [6, 40] (H2; control: K = 5 fails, and Theorem E's w fails at K = 9 as in B2).

H3 reruns B3's model map with L.4' (windows where ε_4 ≤ λ): K = 6 now covers [x_deep, x_top] at λ = 10^(−1000) and
10^(−3000) (control: L.4's rule leaves the gap B3 found). **So O1c's band is an artefact of Lemma L.4's hypothesis,
not a property of g_λ**; what stays undecided there is the transition |R − 1| < 2λ^γ (O1e).

### R4.4 O6: the amendment to N1STAR-PROOF.md (task 4)

READ (stagefree5 G4; N1STAR-PROOF.md md5 02e76176…, 10852 lines at this writing; the lines are +7 from D612/D614's):
Lemma 6.2's statement at line 631 ("For every N there are stage data for Theorem A satisfying (F1) and (F2), all
vanishing on Sigma cap {r < v_start - tau0}."), its proof's range at line 634, section 6.4 at lines 802-810 ("Take the
stage data of Lemma 6.2 with N := K + 3 and U of Proposition 6.5." ... "T^2 x Z2 x Z2-invariant (...), and equal to the
seed's data on Sigma cap {r < v_start - tau0}.").

*The amendment (the verifier of round 3's text, checked against the file: the old string occurs once, at line 634).*
In N1STAR-PROOF.md, Lemma 6.2's proof, replace

> Stage m = 1, ..., N - 1, everything of the earlier stages given:

by

> Stage m = 1, ..., N, everything of the earlier stages given (stage N's data are not needed for (F1), (F2) but are
> fixed here, so every stage's data are smooth, T^2 x Z2 x Z2-invariant and vanish on Sigma cap {r < v_start - tau0}; at
> m = N step (iii) runs inside Theorem A of order N, since after stage N Rm^(N) = -(1/2) e_{N+1} d_th^2 W with e_{N+1}
> = -q_{N+1} independent of th):

Section 6.4 then needs no change: its "stage data of Lemma 6.2 with N := K + 3" include stage N's, and its last
sentence (symmetry, seed data on Σ ∩ {r < v_start − τ0}) holds as written. (If Lemma 6.2's proof is to stay as it is, the
same content can be put in 6.4 instead, at line 802: "Take the stage data of Lemma 6.2 with N := K + 3, those of stage N
by the step of its proof at m = N (which runs as written there: ...), and U of Proposition 6.5.") Checked: step (iii) at
m = N applies Lemma 6.1 with N := m, whose hypotheses ((F1) at orders 1, ..., N − 1, (F2) at 1, ..., N − 2) the earlier
stages arrange (stagen5 S2); after stage N, Rm^(N) = −(1/2) e_(N+1) d_th² W with e_(N+1) = −q_(N+1) independent of θ
(5.4, READ), of θ-mean zero, which is all the step uses. After seating, `checks/stagen5.py` S1 and `checks/stagefree5.py`
G4 must be re-pinned: the pinned line 634 changes, and S1's control (which looks for "Stage m = 1, ..., N,") then
holds.

*Effects (deduced).* Theorem 1: none; its conclusions hold for every admissible stage-N choice (R3.4 with V-m1's
qualification), and the amendment picks one. The sites the verifier lists (Theorem D, N1STAR-PROOF.md 131-133; the
paper's Theorem 1 items 1-2; Proposition 6.5's U = 0; 6.4's invariance; sections 8.1, 8.2, 10.50 (a), (d)) need stage
N's data symmetric and zero on Σ ∩ {r < v_start − τ0}, which the amendment gives. The metric that Theorem 1's
construction names becomes unique: Proposition L.19 shows that without the amendment the layer below about λ^(3N−9) is
not determined, and Theorem L, Proposition L.12 and the window bounds (which use L.3's flat-edge bounds, true for the
rule and not for every choice) concern the amended construction. Theorem 2 does not use Lemma 6.2's slice data. The
paper: its Theorem A sentence ("for every N and every smooth choice of stage data", RESPONSE-HL-5D.md line 492) and its
sentence on how the stage data are chosen (line 635) stand; its equality text should name the amended construction
(R4.8).

### R4.5 λ_L (task 5)

Computed (lamL5b M1-M5) at P*:

- λ0 < 0.0024433 (READ, CONSTANTS5 Round 4, certified there: Lemma 2.3's ε1 must lie below g0's least absolute
  eigenvalue on Ω, 0.0307686). So the first term of λ_L's minimum is below 0.0024433, and Λ_8a = 0.611 cannot bind.
- C_Φ = C1 max_(|β|≤B) ((1 − β)² + β²) = C1 ((1 + B)² + B²): |dr − β dv|_e² = (1 − β)² + β² in Cartesian components
  (dv = dτ + dr, dr = x̂·dx). B = 1 + sup |r_q'| ≤ 1 + c²/18 ≤ 1.0974028 (r_q' = μ0^(1/4) μ^(−3/4) μ'/4, μ' = (2/9) env²,
  env ≤ c ≤ 1.3241035), so C_Φ ≤ 5.6033913 C1 (certified), and Λ_6 = (288 C_Φ/25)^(1/27) ≤ (64.5511 C1)^(1/27), which is
  below λ0's bound only if C1 < 4.63·10^(−73).
- C_L11, C_L4: not computable here. Each is built from the sup norms of the profiles of stages 1-9 and their derivatives,
  Theorem E's M and Proposition 6.5's C0, the leaves CONSTANTS5 1.5 and R4.2 list; the obstruction is λ0's (stage 1's
  lower-order coefficients, its data, and Lemma 2.3's C(M1) at g̃ within 0.0307686 of g0 are not extracted).
- *Direction* (the verifier's M2, re-derived). Λ_4, Λ_5, Λ_5' and Λ_8b-d decrease in M_m. lamL5's B(1456) is an upper
  bound of M_1456, so its thresholds are lower bounds of the proof's (values of λ below which each condition certainly
  holds). Every derivative of env vanishes at v_s, so env(v) = env^(m)(ξ)(v − v_s)^m/m! and M_m ≥ m! env(v)/(v − v_s)^m:
  log10 M_1456 ≥ 8091.60 (M5, certified at v_s + 5.1·10^(−4); control: the bound with k! mutated to (k + 2)! exceeds
  CONSTANTS5's certified e_14). With it, upper bounds: Λ_4(0) ≤ 10^(−4654.28) = 5.3·10^(−4655) (round 1's L.5),
  2.71·10^(−12) (Chebyshev at i = 1); Λ_5 ≤ 10^(−434.32) (round 1), 10^(−56.38) = 4.2·10^(−57) (A15), each by its i = 26
  term; Λ_8b ≤ 10^(−809.48) C_L11^(−4/3) (A15) by C_ε ≥ its i = 26 term.
- Lemma L.4' replaces Λ_5 by Λ_5' (ε_4(v1) ≤ λ at y = λ^14): with C^DS_(i,m) := min_κ [T_(m−1)^(i)(1)(2/κ)^i +
  κ^(m−i)/(m−i)!], the constants of Lemma L.5 on Chebyshev-Lobatto nodes by the Duffin-Schaeffer inequality (the
  endpoint row sum of the i-th differentiation matrix is T_n^(i)(1): M3, to 50 digits at n ≤ 24 and in floating point at
  n = 1455; log10 C^DS_(i,1456) = 3.897, 7.312, 10.501, 13.541 for i = 1, ..., 4), Λ_5' lies in [10^(−2.93), 10^(−2.82)]
  and does not bind. With C^DS at every i ≤ 26, log10 C_ε ≤ 220.06 (round 3: 613.22), and Λ_8b, Λ_8d ≤ 10^(−285.27)
  max(C_L11, C_L4)^(−4/3), Λ_8c ≤ 10^(−36.99) C_L11^(−1/11.5).

**λ_L at P*, updated (with Lemma L.4' and the Duffin-Schaeffer constants).**

    λ_L = min{ λ0 (< 0.0024433), 1/(2 C1), Λ_4(C1) (≤ 2.71·10^(−12) (1 + 0.945 C1)^(−1.0097)), Λ_5' (≤ 10^(−2.82)),
               Λ_6 (≤ (64.55 C1)^(1/27)), 0.611, Λ_8b,d (≤ 10^(−285.27) max(C_L11, C_L4)^(−4/3)),
               Λ_8c (≤ 10^(−36.99) C_L11^(−1/11.5)) }.

Certified: the threshold this proof delivers with Lemma L.4' is below 2.71·10^(−12), whatever Theorem 1's constants are;
for rounds 1-3's proof (L.4 and round 1's or A15's constants) the corrected figures are 5.3·10^(−4655) and 4.2·10^(−57).
If C_L11, C_L4 ≥ 1 (not shown), λ_L ≤ 10^(−285.27). As before these bound the proof's threshold, not the largest λ for
which Theorem L holds.

### R4.6 The verifier of round 3, seated (each re-derived), and amendments to rounds 1-3

Verdicts (READ from the report): L.12 (i), including at the zeros of env; the four breakdown scales; L.3's costs i + 2j +
1 ≤ 2N + 8; ν in the (v, x) frame, −μ0^(−7/4)(ρ³ − 1)²/(9ρ⁶) with its one root ρ = 1 inadmissible; B(1456) = 10^8573.89
a valid upper bound; the amended L.5 (A15); O6 (stage N enters D at order ≥ N and the constraint map at ≥ N − 1; the step
at m = N valid); all seven programs reproduce.

- **V-M1 (major; L.12's hypotheses).** Confirmed (H4's control reproduces each failure). Repaired in R4.3: m :=
  max(56 M, 4 P M, 4 M/δ), κ := max(64, 8 P, 8/δ), H4 checking a range of δ and P, generic and at ρ*. With L.4', (e6)
  is p (1 − 4/m) > 1 and no longer binds.
- **V-M2 (major; the direction of certification).** Confirmed (re-derived in lamL5b M5, numbers as the verifier's to
  the second figure). R3.3 and R3.0 item 4 read: round 1's threshold is below 5.3·10^(−4655), A15's below 4.2·10^(−57),
  and "λ_L ≤ 10^(−820) if C_L11, C_L4 ≥ 1" reads 10^(−809.5) (A15) or, with L.4' and the Duffin-Schaeffer constants,
  10^(−285.27) (R4.5); P2′'s "below 10^(−57)" is superseded by R4.8. lamL5's docstring and printed labels now say that
  its thresholds are lower bounds; lamL5b M5 certifies the upper ones, with a control.
- **V-M3 (major; "decided" on the very edge).** Confirmed. R3.0 item 3, R3.2 (e) (L.14 and the sentences after it) and
  R3.5 O1 showed what the record's bounds and the unit-constant models allow, not the sign for g_λ; "which change it at
  leading order" (U) is withdrawn, since only U's bound allows it; "where a ≠ 0 the sign is that of −a" needs a degree-
  two bound for Theorem 1, not stated in round 3. Replaced by Proposition L.19 (as the supplement stands: not determined,
  unconditionally, with no Lemma H and no differentiability in A) and R4.2 (b) (under the amendment: open, the exact
  obstruction stated). The verifier asks that Lemma H be proved; it is not, and R4.2 (b) says why.
- **V-m1.** Confirmed: R3.4's "Theorems A, D, E, and Theorem 1, hold for every smooth choice of stage N's data" reads
  "for every choice that is smooth, T² × Z2 × Z2-invariant and vanishes on Σ_τ0 ∩ {r < v_start − τ0}". The verifier's
  amendment text is R4.4's.
- **V-m2.** P2′'s "Not settled" list omits O1d, O1e and, at fixed λ, the levels below λ^P; δ's range is not stated; "the
  envelope's own terms" (P*) is undefined in the paper. All three repaired in R4.8.
- **V-m3.** R3.3 (lines 1136 and 1228): "at P* the λ0 of its proof is below 0.0239" reads "below 0.0024433" (CONSTANTS5
  Round 4).
- **V-m4.** R3.0 item 3 (line 900): "is the binomial expansion of" reads "has as its top two derivative families those
  of" (as L.13 (c) states).
- **V-m5.** Lemma H (R3.2 (e)) gave no quantity for "slowly varying", Lemma H_P no order or remainder, the degree-two
  L.4_P no q, M. Lemma H_P is replaced by L.15_P and L.16 (quantified); the degree-two lemma is L.17_P (no λ^(−q) loss;
  costs c, M_P); Lemma H_Σ is stated with its quantity in R4.2 (b).
- **V-m6 (controls).** Repaired, each now mutating the computed path: layerlin5 N5 (K from N4's construction with the vv
  mass coupling halved), N6 (one quadrature scaled by 11/10); layerpast5 P3 (the vv transport with the coupling halved,
  not an integral of 0); layerdeg5 D4 (d_θ⁻¹ mutated to d_θ, on cos 4t); layerfix5 F3's top-level control returns the
  four mutated claims instead of negating the check. Kept, and so labelled: F3 (b) mutates the claimed closed form and
  (d) refutes a sharper constant.
- **Nits.** R3.3 line 1131: "min(C_L11, C_L4)^(−4/3)" reads "max(C_L11, C_L4)^(−4/3)". lamL5's docstring route for B(m)
  is the partial-fraction split 1/(1 − z²) = (1/u + 1/(2 − u))/2, u = 1 − z, which gives e^(3/4) (Re 1/w ≥ 1/(w0 + ρ)
  alone gives e^1); corrected. R3.3 line 1109: sin⁴ is the solver's envelope (the paper's line 678), while Theorem 1
  takes C_c^∞ envelopes. veryedge5 V5 (d) summed U's bound to ε_(2N+2) where A4 has ε_(2N+3); corrected and rerun (the
  ordering stands). layerband5 B3 used M = 26 at K = 10, where M* = 34; corrected and rerun (still covered, as the
  verifier found). stagen5 S3 is an elementary identity (the θ-mean of a θ-independent coefficient times ∂_θ² of a
  periodic W); its label reads "READ (5.4: e_(N+1) = −q_(N+1), a polynomial in the means and phases) with an elementary
  identity", not "computed". V2's identities concern the top two derivative families, which the slice motion cannot
  reach (∂_(r0) does not raise the order of env's derivative), so V2 does not test that motion; L.13's proof reads "the
  r0-dependence does not enter the top two families" for "the terms from the r0-dependence cancelling". layerfix5 F4's
  vacuous clause is dropped and F1's hard-coded 24 computed. layerwin5 W3 labels (e6) "L.4's hypothesis" with round 1's
  exponent 6; W3 is superseded by layerledger5 L1 (R2.0). R3.2 (b) line 1019 calls the levels below λ^P "the very edge";
  read "the levels below λ^P (the very edge lies below them)". lamL5 L2's control detects only factors above 10^41; B's
  validity rests on the Cauchy-disc bound (the verifier's sampling confirms it), and the direction is fixed by M5.
- **Mutation tallies** (READ from the report): veryedge5 8/10 (V2's slice motion, above), lamL5 7/9 (L2, above), stagen5
  4/5 (S3, above), layerfix5 6/8, layerband5 7/7, layerwin5 2/2.

Further amendments of this round:

- **A18.** R3.2 (f) and R3.5 O1b: Theorem 2's very edge is decided (Theorem L_E); Lemma H_P is replaced by L.15_P and
  L.16 and is not proved as stated; the degree-two L.4_P is L.17_P with L.18_P.
- **A19.** Theorem L (round 1 line 16, "Theorem A with the stage data of its Lemma 6.2") and every later use of L.3 read
  "with stage N's data by Lemma 6.2's rule" (R2.1 took it; Proposition L.19 shows it is needed).
- **A20.** R3.2, Proposition L.12 and R3.5 O1c: σ_K = min(3, (K − 3)/2) becomes 3, (iii) holds for every K ≥ 6, with
  the parameters of V-M1 (R4.3); O1c is closed.
- **A21.** R3.2 (d)'s "a factor above 10^1398" is V5's model figure at one depth; Theorem L_E's domination is at every
  depth of the very edge.

### R4.7 Open items, exactly

- **O1a′** Theorem 1's very edge under the O6 amendment: the sign of a(v, ω) needs U^(1), Lemma H_Σ and the slice-data
  degree-two bound (R4.2 (b)); with Lemma H_Σ the very edge alternates wherever Φ's leading coefficient is not zero
  (Remark L.20). Without the amendment it is not determined (Proposition L.19).
- **O1b** closed (Theorem L_E), subject to L.15_P (b)'s energy estimate on P_v ∪ Ω_v, L.17_P and L.18_P being read.
- **O1c** closed (L.4', with V-M1's parameters).
- **O1d** (dips and interior zeros below λ^(3+δ); envelopes not log-concave at the edge): unchanged; Lemma L.16 needs
  log-concavity near the edge.
- **O1e** the transition |R − 1| < 2λ^γ: unchanged. And, for Theorem 1 at fixed λ, the levels between λ^P and the very
  edge (L.12 (ii) reaches them as λ_U(P) decreases): unchanged; for Theorem 2 they are covered by Theorem L_E.
- **O2** Rounds 3-4: round 3 read (vE3, R4.6); round 4 awaits a reader.
- **O4** λ_L: R4.5; C1, C_L11, C_L4 and λ0's value unevaluated.
- **O5** unchanged. **O6** closed by R4.4's amendment once it is seated.

### R4.8 Proposed paper text (replaces R3.6's P1′ and P2′; P3-P6 stand, P3's list extended)

(P1″) Proposition 3.2: replace the sentence from "If μ0 = √72 l5² exactly, the" to "Propositions E.2-E.4)." by:

> If μ0 = √72 l5² exactly, the boundary coincides with the seed's horizon for v ≤ v_start and is null there; g_λ equals
> the seed on {v ≤ inf supp env}, so it is null for g_λ too; after the shell starts it is spacelike for g_λ outside a
> layer whose width tends to 0 with λ (supplement `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that
> layer it is not spacelike throughout: for λ small every column has points where it is timelike for g_λ, so the
> no-return property stated above for μ0 > √72 l5² fails at equality (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L,
> L_P and L_E and Corollary L.7, for the solutions of Theorems 1 and 2 as the supplement builds them).

(P2″) Section 9: replace the bullet "**The boundary at equality.**" by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced, supplement `docket68/n1star/EQUALITY5.md` and
>   `EQUALITY5-LAYER.md` [†]; computed, `checks/eq5.py`, `eqlayer5.py`, `layerlin5.py`, `layerwin5.py`, `layerdeg5.py`,
>   `layernull5.py`, `layerpast5.py`, `layerledger5.py`, `layerfix5.py`, `layerband5.py`, `veryedge5.py`, `lamL5.py`,
>   `stagen5.py`, `edgeP5.py`, `stagefree5.py`, `bandL4p5.py`, `lamL5b.py`): g_λ is the seed on {v ≤ v_s}, v_s := inf
>   supp env, and x_K = 1 is spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η. In the layer between, for every K ≥ 6 and
>   every δ ∈ (0, 1/2), x_K = 1 is spacelike wherever sup_(v'≤v) env ≥ λ^(3−δ); on every column it has timelike points
>   within 4πλ of each point where env first reaches a level λ^p, 3 + δ ≤ p ≤ P (every point of that range when env
>   increases at its edge), for λ below a threshold depending on P; and between the levels λ^(3+δ) and λ^(3−δ) it is
>   decided by the ratio of λ³ A env |ν| |d| to the margin, d the double divergence of the waves' angular tensor (|d| ≥
>   8/3) and ν a coefficient depending on τ0 (ν∞ = −μ0^(−7/4)/9 for Theorem 2's solution). For Theorem 2's solution the
>   very edge, where λ |env'/env| ≳ 1 and no expansion in λ is asymptotic, is decided as well: there the part of
>   g_λ⁻¹(dΦ0, dΦ0) linear in the waves is computed in closed form, λ A ν∞ Re[d e^(iv/λ) s⁻² env] with s = ∂_v + i/λ, and
>   for an envelope whose logarithm is concave at its edge (the C_c^∞ envelope used for the constants is) every interval
>   of length 4πλ below the level λ^(3+δ), down to v_s, has timelike and spacelike points on every column. For Theorem
>   1's solution the very edge depends on the construction's top stage: with stage N's data left free, two admissible
>   choices, differing by a gauge term of size λ^N, make x_K = 1 spacelike, respectively timelike, from a few wavelengths
>   above v_s up to where env falls to about λ^(3N−9); with stage N's data fixed by the rule of the supplement's Lemma
>   6.2 (its proof as amended, `docket68/n1star/EQUALITY5-LAYER.md` R4.4), no choice is left and the sign there is set
>   by the constraint correction U at first degree, which is not computed. So some future timelike curves of g_λ cross
>   x_K = 1 into D_T, and Proposition 3.2's no-return property fails at equality; a domain O(λ)-close to D_T, inside
>   x_K ≤ 1, has an inner boundary that no future causal curve enters (EQUALITY5.md, Proposition E.4), and the spheres'
>   horizon holds as there stated. Not settled: for Theorem 1's solution, the very edge (U at first degree) and, at fixed
>   λ, the levels between λ^P and the very edge; the transition where that ratio is within λ^γ of 1; envelopes that dip
>   or vanish inside the layer, or whose logarithm is not concave at the edge; and the value of λ_L, explicit in Theorem
>   1's constants, which are not evaluated (at the parameter point of the constants' supplement,
>   `docket68/n1star/CONSTANTS5.md`, the threshold this proof delivers is below 3·10^(−12) whatever those constants are).

[†] "(rounds 1-3 read by independent verifiers; round 4 not yet read)". (P3″) Appendix A, C, D: add `checks/edgeP5.py`
Q1-Q4, `checks/stagefree5.py` G1-G4, `checks/bandL4p5.py` H1-H4 and `checks/lamL5b.py` M1-M5 beside round 3's entries
(about half an hour, four minutes, three minutes and two minutes), each with its controls as in its docstring; P5's
commands for layerlin5, layerpast5, layerdeg5, layerfix5, layerband5, veryedge5 and lamL5 stand, with their new md5s.

### R4.9 Labels and sources (round 4)

*Labels.* Computed: Q1, G1, G2, H1, H2, H4 (exact); M2, M4, M5 (certified, interval arithmetic); M3 (to 50 digits at n
≤ 24, floating point at n = 1455); Q2 (mpmath, sampled); Q3, Q4, G3, H3 (mpmath, models with unit constants). Deduced:
Lemmas L.15_P, L.16, L.4', Theorem L_E, Proposition L.19, the amended Proposition L.12, the formula of R4.5; sketches:
Lemmas L.17_P, L.18_P; conditional: Remark L.20 (on Lemma H_Σ, stated, not proved); not re-derived: the Duffin-Schaeffer
inequality (standard; its row sums computed at the stated n). READ: N1STAR-PROOF.md sections 5.4, 6.1-6.4 (lines 541-552,
600-669, 756-810 at md5 02e76176…) and 9.1-9.4 as in R2.9; CONSTANTS5.md Round 4 (R4.0, R4.2: λ0 < 0.0024433; md5 printed
by lamL5b M1, the file being written in parallel); the verifier of round 3's report (verdicts, findings, tallies, as
relayed); the paper's Proposition 3.2, Theorem A and section 9 (RESPONSE-HL-5D.md lines 296-305, 492, 635 and 1532-1543,
md5 a69a9453…).

Files (round 4): this section; `checks/edgeP5.py`, `checks/stagefree5.py`, `checks/bandL4p5.py`, `checks/lamL5b.py`, each
with its `.out`; changed and rerun: `checks/layerlin5.py`, `checks/layerpast5.py`, `checks/layerdeg5.py`,
`checks/layerfix5.py`, `checks/layerband5.py`, `checks/veryedge5.py`, `checks/lamL5.py`, each with its `.out`.
