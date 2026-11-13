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
l5², K ≥ 6, g_λ the metric of Theorem 2, and env satisfying Lemma L.16's hypotheses (b), (c) [round 6, V5-m3: and (H_D)
of Lemma L.18; A25] on (v_s, v_s + x0]. There
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

## Round 5 (2026-11-02)

Status: written (round 5); not yet read by an independent verifier. Round 4 was read by one (the verifier of round 4,
vE4; scripts kept outside the record); its findings are seated in R5.1, each re-derived before it was accepted. New
programs, each with a docstring stating its claims, controls and labels; all pass and every control fails (`.out` beside
each): `checks/edge1_5.py` X1-X11, `checks/degtwo5.py` T1-T6, `checks/constL5.py` K1-K3. Changed on the verifier's
findings and rerun: `checks/bandL4p5.py` (H2: level by level, over a grid of δ, with the amended m), `checks/lamL5b.py`
(M2's control a mutation of the computed path; M4 prints its B-based thresholds as lower bounds; M5 prints Λ_8c). Round
4's reruns of `layerlin5`, `layerpast5`, `layerdeg5`, `layerfix5`, `layerband5`, `veryedge5`, `lamL5` and `bandL4p5`
finished and replaced the old outputs: every check passes and every control fails; the differences are timings and the
two corrections R4.6 names (layerband5 B3 at M = 2N + 8, now x_deep = 5.31·10^(−15) at λ = 10^(−1000); veryedge5 V5 (d)
with U's bound summed to ε_(2N+3), now 8.05·10^105 per env where round 3 printed 7.33·10^98; both orderings stand).
`checks/stagen5.py` S1 and `checks/stagefree5.py` G4 were re-pinned to the amended supplement by the coordinator
(D615, D616; N1STAR-PROOF.md md5 709c63be…), not here. The text of rounds 1-4 is kept; this section amends it.

### R5.0 Findings

1. **Theorem 1's deep layer, very edge included, is decided (Theorem L_1E, R5.3).** [round 6, V5-M1, V5-M2: item 1 is
   restated as Theorem L_1E′ and item 3's L.25 (a) proved anew, R6.1, R6.2] With stage N's data fixed by
   Lemma 6.2's rule (free until D615, fixed by that rule since), the part of g_λ⁻¹(dΦ0, dΦ0) linear in the waves is,
   at the boundary, the first harmonic −Re[S e^(iv/λ)] of a sum of two amplitudes: Theorem L's stage term λ³ A ν d env
   and a term carried by the first-degree constraint correction U^(1),
   −λ^(N+1) A Γ_R i^N d Ξ env^(N−1), with Γ_R > 0 and Ξ explicit, |Ξ| ≥ min(c_N, |1 − c_N|), c_N := N μ0/(r0² + μ0).
   The second dominates once λ^(N−2) env^(N−1)/env ≫ 1, which happens before the very edge, and it decides the very
   edge. For a flat log-concave edge whose derivatives to order N are log-concave there (hypothesis (H_N), checked on
   the record's envelope) and every τ0 with (v_s − τ0)² ∉ {(N − 1)μ0, (2N − 1)μ0}, every interval of length 4πλ near
   the edge below a level λ^(P1) independent of λ, down to v_s, has timelike and spacelike points on every column.
   Lemma H_Σ is proved (R5.3 (b)); U^(1)'s leading part is computed (R5.3 (c)); the two readings of "the lapse and
   shift of g_app" in the supplement's section 6.4 give the same conclusion. [round 6, V5-m6: readings 1 and 2; reading 2
   is the supplement's; A30] O1a′ is closed.
2. **L.15_P (b), L.17_P and L.18_P are proved (R5.2)**, in one form (L.17, L.18) covering Theorem 2's solution and,
   with slice data, Theorem 1's. Theorem L_E is deduced on its stated hypotheses with no sketch under it (the verifier
   of round 4's MAJOR 1); the localisation holds at every depth, which repairs MINOR 3.
3. **(b) is settled (R5.4).** The transition |R − 1| < 2λ^γ: on every column the maxima of g_λ⁻¹(dΦ0, dΦ0) over
   consecutive carrier periods decrease strictly through it and change sign exactly once (Theorem L.24). Dips: the
   statement "every interval of length 4πλ below λ^(3+δ) has timelike points" is false for envelopes with flat
   interior zeros accumulating at the edge (Proposition L.25 (a), computed) and true for log-concave flat edges (L_E,
   L_1E); for every envelope the causal character at a point is decided by an explicit ratio of the exact first-degree
   term to the margin (L.25 (b)). Theorem 1's levels between λ^P and the very edge at fixed λ: covered, since L_1E's
   level λ^(P1) does not depend on λ (take P := P1 in L.12 (ii)).
4. **(d): C_L11 and C_L4 are explicit formulas (R5.5)** in λ0's leaves (the profile bounds of order ≤ 11, Lemma 6.4's
   and Proposition 6.5's constants, Theorem E's M, Lemma 2.3's constant, λ0), the certified numbers of CONSTANTS5 1.4
   and two constants of the seed alone; their values need what λ0's needs and nothing else (constL5).
5. **The verifier of round 4 (R5.1):** MAJOR 2 repaired (L.12 (iii) holds for every δ ∈ (0, 1/2] with γ = 1/10, each
   error compared with the margin at its own level); MAJOR 3 superseded by item 1; MINOR 1-7 and the nits repaired.
6. **Nothing is left open (R5.7).** The proposed paper text is R5.8.

### R5.1 The verifier of round 4, seated (each re-derived)

Verdicts (READ from the report, as relayed): Proposition L.19 (ii)-(iii), the pre-D615 free choice and the amendment's
mathematics, Lemma L.15_P, Lemma L.16 (b) (an independent quadrature gives |ρ_2|/R_2 ≤ 0.47), Theorem L_E's phase
argument and its 0.72, the envelope's log-concavity (κ ∼ 3/(4x²), α = 1/2, c_R → 2.309), Lemma L.4′ and λ_L's
arithmetic (the Duffin-Schaeffer constants, log10 M_1456 ≥ 8091.604 at x = 5.19·10^(−4), Λ_4 ≤ 10^(−11.568)) confirmed.

- **V4-M1 (major).** Confirmed: L_E rested on L.17_P, L.18_P, labelled sketches in R4.9. Repaired by proving them in
  full (R5.2); L_E is deduced, on the hypotheses it states.
- **V4-M2 (major).** Confirmed: round 4's H2 compared the errors at E = λ^(3−δ) with the margin at E = λ^(3+δ), and
  failed for δ ≥ 0.1994 at γ = 1/10. Repaired: bandL4p5 H2 compares every error with the margin at the same level
  (all exponents are linear in log E/log λ, so the ends of each range suffice), over δ ∈ {1/1000, 1/100, 1/20, 1/10,
  1/5, 1/4, 3/10, 2/5, 49/100}, m := max(56 M, 4 P M, ⌈4 M/δ⌉), P ∈ {50, 200}, K ∈ [6, 40]: (iii) holds with γ = 1/10 at
  every grid point; the slacks decrease in δ and the least of them is 0.4818 at δ = 1/2, K = 6, so (iii) holds for every
  δ ∈ (0, 1/2]. (i) is monotone in δ (its region {E ≥ λ^(3−δ)} shrinks as δ grows) and is checked at min(δ, 1/4); its
  ledger run at δ itself fails only at K = 6, δ ≥ 2/5, which is therefore harmless. Control: round 4's mixed
  comparison fails at δ = 1/4. A24 below records the consequence.
- **V4-M3 (major).** Confirmed: P2″'s "the sign there is set by the constraint correction U at first degree" stated a
  reduction that needed Lemma H_Σ and a slice-data degree-two bound, neither proved. Superseded: both are proved (R5.3
  (b), R5.2) and the very edge is decided (Theorem L_1E); P2″ is replaced by R5.8.
- **V4-m1.** Confirmed: Proposition L.19 (iv) applied L.4 or L.4′ to the ± constructions, which needs Lemma L.3 with
  the weight of ψ = env^(2/3) (L.3's flat-edge bounds hold for the rule, not for every stage-N choice), and asserted the
  ledger terms ψ_c ε_c and λ^(2N) ψ_c². L.19 concerns the supplement before D615; its (iv) is relabelled a sketch, and
  no statement proposed for the paper uses it (R5.8 speaks only of the amended construction). P2″'s "from a few
  wavelengths above v_s up to where env falls to about λ^(3N−9)" came from G3's unit-constant model and is dropped.
- **V4-m2.** N1STAR-PROOF.md is now 709c63be… (D616: Lemma 6.2's statement fixes the stage data its proof constructs).
  No program of this round prints its md5 or line numbers; stagen5 and stagefree5 were re-pinned by the coordinator.
- **V4-m3.** Confirmed: L_E's "at most C κ^(2c) env²" fails where c_*λ ≤ v − v_s and 4 C_P λ κ > 1 (up to x ∼ (C_P
  λ)^(1/2)), since η(v_1) carries env(v + 4 C_P λ) ≫ env(v). Repaired by Lemma L.18 at every depth: under (H_D) the
  degree-two terms are at most C κ(v)^(2c) env(v)² at every depth of the edge, with no condition on c_*.
- **V4-m4.** Confirmed and repaired: lamL5b M4, computed with B ≥ M_m, now prints lower bounds of the thresholds,
  min(Λ_8b, Λ_8d) ≥ 10^(−296.754) max(C_L11, C_L4)^(−4/3), Λ_8c ≥ 10^(−38.489) C_L11^(−1/11.5), log10 Λ_5′ ≥ −2.923,
  and log10 C_ε ≤ 220.06 as the upper bound it is; M5 now prints the upper bound Λ_8c ≤ 10^(−36.992) C_L11^(−1/11.5)
  (from C_ε's i = 26 term with the lower bound of M_m, log10 C_ε ≥ 211.45). R4.5's line "log10 C_ε ≤ 220.06 ... Λ_8b,
  Λ_8d ≤ 10^(−285.27)" reads: the upper bound 10^(−285.27) comes from C_ε ≥ 10^211.45; the lower one from C_ε ≤
  10^220.06.
- **V4-m5.** Confirmed: H2 used round 3's m = 56 M (at δ = 10^(−3) its (i) failed for K = 6-19). Repaired with V4-M2.
- **V4-m6.** Confirmed: P2″ omitted L_E's hypotheses (log-concavity alone does not make R_2 small). R5.8 states them:
  |κ′| ≤ c κ^(1+α) with α < 1 and L.16 (c)'s derivative bounds.
- **V4-m7.** R4.4 and R4.9 pin N1STAR-PROOF.md before the amendment (02e76176…, section 6.4 at 802-810). At 709c63be…:
  Lemma 6.2's statement at 631-634, its proof's range at 636, section 6.4 at 807-815. R4.4's "S1 and G4 must be
  re-pinned" is done (b865d40).
- **Nits.** R4.5's Taylor point is v_s + 5.2·10^(−4) (lamL5b prints 0.00052). L_E's proof: "λ^(−2c−5)" reads
  "λ^(−2c−3)" (on {λκ ≤ 1}, κ^(2c) env²/(λ env λ²) ≤ λ^(−2c−3) env). R4.5's "If C_L11, C_L4 ≥ 1": max(C_L11, C_L4) ≥ 1
  suffices. P2″'s "computed in closed form" reads "its leading term, with remainder O(min(λ, 1/κ))". lamL5b M2's
  control is now a mutation of the computed path (μ′ = (4/9) env² for (2/9) env², detected). L.4′'s proof: step 5 uses
  step 3's coefficients (the data's τ-derivatives on Σ_τ0 come from the equation solved for ∂_τ²); the triangular
  argument covers it, since the coefficients of the same level there are bounded and the large ones multiply lower
  levels. Λ_5′'s formula, until now only in lamL5b's docstring:
  Λ_5′ = min_(i≤4) [5 C_(i,m) (5/4)^(1−i/m) M_m^(i/m)]^(−1/(14(1−i/m) − 1)).

Amendments of this round:

- **A22** (the coordinator's request). Where rounds 3-4 describe stage N's data as free in the present tense (R3.0 item
  5, R3.4 "the supplement leaves stage N's data free", R3.5 O6, R4.0 item 2, R4.2 (a) "which the supplement leaves
  free" and "not determined by Theorem 1 as the supplement now states it", R4.7 O1a′), read "free until D615, fixed by
  Lemma 6.2's rule since". Proposition L.19 is a statement about the supplement before D615. [round 6, V5-n7: A27]
- **A23.** R4.0 item 1, A18 and R4.7 O1b: Theorem L_E's degree-two inputs are Lemmas L.17 and L.18 of R5.2, proved; in
  its proof the degree-two terms are bounded by L.18 at every depth (V4-m3), not by L.17_P with the tilt 4 C_P λ.
- **A24.** R4.3, amended Proposition L.12: (iii) holds for every δ ∈ (0, 1/2] with γ = 1/10 (V4-M2), and (i) for every
  such δ by monotonicity.
- **A25.** R4.7: O1a′, O1d, O1e and "the levels between λ^P and the very edge" are closed by R5.3 and R5.4.

### R5.2 Degree two and localisation, written in full (task (c))

Notation. g0° is the seed with μ ≡ μ0 and dRic^H the linearisation of the reduced operator at g0° (the gauge relative
to g0°); in case P (Theorem 2's solution) S(V) := (P ∪ Ω) ∩ {v ≤ V}, in case Ω (Theorem 1's) S(V) := Ω ∩ {v ≤ V};
N_V := S(V) ∩ {v = V}; ε_c(v) as in R2.1; "local" means evaluated at v(X), or at v(X) + δ with δ κ(v(X)) ≤ 1.

**Lemma L.15_P (b), written in full (deduced, with E1, E2, E5 of layernull5).** Its statement is R4.1's.

*Proof.* (1) *The operator.* In Cartesian components dRic^H(h) = −½ g0°^(ab) ∂_a ∂_b h + 𝔅(∂h) + ℭ h, with 𝔅, ℭ
smooth on P ∪ Ω and, on P, O(r⁻³), O(r⁻⁴) with their derivatives (Christoffel symbols and curvature of g0° = η +
(μ0/r²) L⊗L in Kerr-Schild form); dRic^H commutes with the Lie derivative along the rotations Ω_ab, which are Killing
for g0° (the operator is natural under the isometries of g0°, the gauge being relative to g0°). (2) *Energy on S(v)
with the null face kept.* For u := Ω^β e_M, |β| ≤ 2, run the supplement's Lemma 9.5 on P and Lemma 2.3 on Ω (READ),
with 𝔅∂u + ℭu moved to the right side, on S(v) ∩ {τ ≤ τ′}: the face N_v has the flux density T(L0, Y) = ½(1 +
μ0/r²)(ℓu)² + |∇̊u|²/(2r²) ≥ 0 (E1 at μ = μ0), kept on the left; {r = a} is spacelike with the region to its past (Lemma
1.1 (b)); nothing comes in, i.e. e_M is the limit of the solutions with zero data on Σ_(τ_n), τ_n → −∞ (Proposition
9.8's scheme), and the estimate is uniform in n. The right side's first-order terms are absorbed by Gronwall's lemma
with the kernel C t^(−3/2) on P, integrable (E5), and C on Ω. So sup_τ ‖∂u(τ)‖ + F_v(u)^(1/2) ≤ C ∫_(−∞)^(τ_end)
‖Ω^β dRic^H(e_M)(τ)‖_(L²(Σ_τ ∩ S(v))) dτ. (3) *The source* is −Re[λ e^(iv/λ) A I_M(v) Q b_M]: on Σ_τ ∩ S(v) its L²
norm is at most λ A sup_(v'≤v) |I_M(v')| ‖Ω^β Q b_M‖_(L²(Σ_τ)), and Q b_M ∈ E_3 (b_0 ∈ E_(3/2), b_n ∈ E_2 for n ≥ 1 by
L.3_P (a_P) at the seed; Q of second order with coefficients in E_0, E_1, E_2), whose L² norm on the slices of P is at
most C t^(−3/2) (E5); on Ω it is bounded and τ ∈ [τ0, τ_end]. (4) *Pointwise.* Along the generator of N_v from r = ∞,
where r^(3/2)|Ω^β e_M| → 0 (nothing comes in), to r(X), ‖Ω^β e_M(r, ·)‖_(L²(S³)) ≤ ∫_r^∞ ‖ℓΩ^β e_M‖ ≤ (2 F_v(Ω^β
e_M))^(1/2) (∫_r^∞ r'⁻³ dr')^(1/2) (E1, E5), and H²(S³) ⊂ L^∞ (the argument of Lemma 9.3 (a)) gives |e_M(X)| ≤ C
Σ_(|β|≤2) F_v(Ω^β e_M)^(1/2) ≤ C_M λ sup_(v'≤v(X)) |I_M(v')|. ∎

**Lemma L.17 (degree two; deduced, with degtwo5 T1, T2).** Let g_λ be Theorem 2's metric (case P) or Theorem 1's with
stage N's data by Lemma 6.2's rule (case Ω; N := N_P, resp. N = K + 3, M := M_P, resp. M*), h^(1) its A-linear part
(the linear solution of dRic^H(h) = 0 with nothing coming in but the wave, case P; with the A-linear Cauchy data of
R5.3 (a) on Σ_τ0, case Ω), and r2 := g_λ − g0° − h^(1). Let v_1 := v + ρ_v, ρ_v the reach of the remainder estimate
used at the point (4 C_P λ, resp. 2 C1 λ (τ_end − τ0), for L.4_P, resp. L.4; at most 1/κ(v) after Lemma L.18), and
assume ε_M(v_1) ≤ λ⁵. Then at every X = (v, r_q(v), ω), v_s < v ≤ v_♯,

    |r2(X)| ≤ C_2 [ε_c(v)² + ε_c(v) η(v_1) + η(v_1)²],     η(v_1) := λ^(N−6) ε_M(v_1),     |(g0 − g0°)(X)| ≤ C ε_0(v)²,

C_2 depending on the quantities of R2.1 (Theorem E's or Theorem P's bounds included) and c a fixed cost.

*Proof.* (1) *The equation.* g_λ solves the supplement's reduced equation Ric^H_(g0)(g_λ) = 0, the gauge relative to
g0. The gauge vectors relative to g0 and to g0° differ by g^(ab)(Γ[g0] − Γ[g0°])_ab, and every component of Γ[g0] −
Γ[g0°] is a polynomial of degree ≤ 2 in (μ − μ0, μ′) with no constant term and coefficients functions of (r, θ) (T2);
so Ric^H_(g0)(g) = Ric^H_(g0°)(g) + 𝒜(g) with |𝒜| ≤ C(|μ − μ0| + |μ′| + |μ″|) for (g, ∂g) bounded, and
|∂^k Ω^β 𝒜| ≤ C ε_(k+1)(v)² at points with that v
(μ − μ0 ≤ (2/9) A² (v − v_s) ε_0², μ′ = (2/9) A² env², μ″ = (4/9) A² env env′): local. With u := g_λ − g0°, g0° vacuum
and D_(g0°)(g0°) = 0, Ric^H_(g0°)(g0° + u) = dRic^H(u) + 𝒩(u), and by the quasilinear form of the reduced operator (the
supplement's (0.2): second derivatives only in −½ g^(ab) ∂_a ∂_b g; T1) |𝒩(u)| ≤ C (|u| |∂²u| + |∂u|² + |u|²) for |u| +
|∂u| ≤ c, with Ω^β-derivatives by Leibniz. As dRic^H(h^(1)) = 0: dRic^H(r2) = −𝒩(u) − 𝒜(g_λ) =: f_2.
(2) *Bounds on u* = (g_app − g0°) + w. By L.3_P (a_P)-(c_P) (case P), L.3 (a)-(c) (case Ω) and D5, |∂^k Ω^β (g_app −
g0°)| ≤ C λ^(1−k) ε_c(v′) at points with v = v′, k ≤ 2 (each derivative of [g_j] costs λ⁻¹ only through ∂_θ), with the
decay of the classes E_(3/2), E_2 on P. For w: Lemma L.4_P (case P), L.4 (case Ω) run with ∂^α, |α| ≤ 4 (their proofs
at four more derivatives: the coefficients ∂^j g_app, j ≤ 6, are bounded on the region since ε_M(v_1) ≤ λ⁵ gives
λ^(1−j) ε_j ≤ 1 there; ∂^j w, j ≤ 3, by Theorem E, resp. Theorem P (P-iii); the source and data cost λ⁻¹ per derivative,
L.3 (d), (e), L.3_P (d_P)) give E_4(τ) ≤ C λ^(N−7) ε_M(v_1), and Sobolev's inequality on the slices (L.4 step 7)
|∂^k Ω^β w| ≤ C λ^(N−5−k) ε_M(v_1) ≤ C λ^(1−k) η(v_1), k ≤ 2.
(3) *The source.* With (2): |u| ≤ C(λ ε_c + λ η), |∂u| ≤ C(ε_c + η), |∂²u| ≤ C λ⁻¹(ε_c + η), so |𝒩(u)| ≤ C(ε_c + η)²,
and |f_2| ≤ C(ε_c(v′)² + ε_c(v′) η(v_1) + η(v_1)²) at points with v = v′ ≤ v; on P each product carries the decay of
two factors (t^(−3) at least), so ‖Ω^β f_2(τ)‖_(L²(Σ_τ ∩ S(v))) ≤ C(...) t^(−3/2), integrable.
(4) *The linear estimate.* r2 = 0 on {v ≤ v_s} (g_λ = g0 = g0° and h^(1) = 0 there: E.2_P, E.2). Case P: nothing comes
in, and steps (2), (4) of L.15_P (b) give |r2(X)| ≤ C Σ_β ∫ ‖Ω^β f_2‖ dτ. Case Ω: r2's data on Σ_τ0 ∩ {v′ ≤ v} are the
degree-two part of g_λ's data: g_app's data minus their A-linear part, at most C ε_c(v)² with their derivatives (L.3
(c), (e)), and U − U^(1), which solves Lemma 6.4's system with source −(Φ − Φ^(1)) − Nl(U) − (L_app − L)U (L_app − L
the coefficients at the approximant's data minus g0's, of degree one; Nl(U) at most C λ⁻¹ |U|²_(C¹)), so that Lemma
6.4 on [a, r] (R2.3 (e)) and |U| ≤ C λ^(N−2) ε_c give |U − U^(1)| ≤ C ε_c(v)² with its derivatives; then L.8 on
Ω_v and L.10 (from the generator's point on Σ_τ0) give the same bound, plus C ε_c(v)² from the data. (g0 − g0°) =
(μ − μ0) r⁻² dv²: D3. ∎

**Lemma L.18 (localisation at every depth; deduced, with degtwo5 T3, T4).** Let env satisfy, on (v_s, v_s + x0],
log-concavity with κ := (log env)′ and

    (H_D)     κ(v_s + y/2) κ(v_s + 4y)^c env(v_s + 4y) → 0 as y ↓ 0, for every c > 0

(true for exp(−a/x^q) and for exp(−e^(1/x)); sampled for the record's envelope, T4). There are λ_D, x_D > 0 such that
for λ ≤ λ_D the bounds of L.17 hold at every boundary point X with x := v(X) − v_s ≤ x_D with ρ_v ≤ 1/κ(v(X)); under
L.16 (c)'s hypotheses then |r2(X)| ≤ C κ(v)^(2c′) env(v)² (env(v + 1/κ) ≤ e env(v), κ decreasing; c′ a fixed cost).

*Proof.* (1) *Any tilt serves.* In L.4_P (resp. L.4) the tilt 2 C_P λ (2 C1 λ) is used only to make the face {v + e
ψ(τ) = V} have a timelike conormal α = dv + e ψ′ dτ for g_λ, and to keep the region inside S(V). Let Δ(V) := sup_(S(V))
‖g_λ⁻¹ − g0⁻¹‖, the Euclidean operator norm on covectors weighted by t^(3/2) on P (ψ′ = t^(−3/2) there, 1 on Ω).
Then for every e with 2Δ(V) ≤ e ≤ 2 C_P λ (resp. 2 C1 λ), g_λ⁻¹(α, α) ≤ ψ′(−2e + (13/4)Δ(V)) < 0 (T3: g0⁻¹(α, α) =
−2eψ′ − e²ψ′²(1 + μ/r²), |α|_e² ≤ 13/4 for eψ′ ≤ 1/2), so the proof of L.4_P (L.4) runs on R(V, e) := S(V) ∩ {v + e
ψ(τ) ≤ V} with the same constants (the slices still shrink, ρ′ < 0), and so does its four-derivative form in L.17
(2). Every X with v(X) + e ψ_max ≤ V lies in R(V, e), ψ_max := 2 + τ_end − τ0. (2) *Stage 0* is L.4_P (L.4) itself, e_0
:= 2 C_P λ (2 C1 λ): |w| ≤ C λ^(N−3) ε_M(v(X) + e_0 ψ_max) at every depth. [round 6, V5-n3: λ^(N−5) ε_(M*) for L.4, and
so in δ_k; A26] (3) *Stage k ≥ 1.* Put y_0 := x_D and, given
stage k − 1 valid at every depth with reach e_(k−1) ψ_max ≤ y_(k−1), put δ_k := C(λ ε_c(v_s + 4y_(k−1)) + λ^(N−3)
ε_M(v_s + 4y_(k−1))), which bounds Δ(v_s + 3y_(k−1)) (|g_app⁻¹ − g0⁻¹| ≤ C λ ε_c with the weight, L.3_P (a_P), L.3 (a);
|w| by stage k − 1 at depths ≤ 3y_(k−1), whose reach is ≤ y_(k−1)), e_k := 2δ_k, and y_k := the least y with
1/κ(v_s + y) ≥ e_k ψ_max (κ decreases). Stage k holds at every X of depth ≤ 3y_(k−1) − e_k ψ_max, with reach e_k
ψ_max, which is ≤ 1/κ(v(X)) at depths ≥ y_k: local there. (H_D) gives y_k ≤ y_(k−1)/2 for x_D small (δ_k ≤ C' κ(v_s +
4y_(k−1))^c env(v_s + 4y_(k−1)), c the cost of ε_M against env under L.16 (c), and 1/κ(v_s + y_(k−1)/2) is larger
once y_(k−1) ≤ x_D), and e_k ψ_max ≤ 1/κ(v_s + y_k) ≤ y_k (κ(v_s + y) ≥ 1/y near a flat edge: log env − log env(v_s +
y/2) → ∞). So every depth in [y_k, y_(k−1)] is covered locally by stage k, y_k → 0, and the depths ≥ x_D by stage 0 for
λ ≤ λ_D (e_0 ψ_max ≤ 1/κ(v_s + x_D)). T4 runs the descent with unit constants (C = 10³, c = 30) from y_0 = 10^(−4):
log10 y_k = −4, −439, −5.96·10^437 for exp(−1/x) and −4, −325.3, −8.57·10^323 for the record's envelope, faster than
any geometric sequence; (H_D)'s quantity is below 1 and decreasing at 10^(−4), 3·10^(−5), 10^(−5); control: env = x^40
stalls at once. ∎

Consequences. Theorem L_E's proof (R4.1) reads, at its degree-two step, "at most C κ^(2c′) env² by L.17 and L.18"
(A23); the remainder of the proof is as written. For case Ω, L.17 and L.18 are the degree-two inputs of Theorem L_1E.

### R5.3 Theorem 1's g_λ in the deep layer (task (a))

**(a) The A-linear part, under D615.** H_j (j ≤ N + 1) are the first-degree profiles of (3.1) with Lemma 6.2's rule at
every stage, m = N included; h_app^(1) := Re Σ_(j≤N+1) λ^j H_j e^(iv/λ) on Ω; Φ^(1) is the first-degree part of the
constraint map of g_app's data on Σ_τ0; U^(1) = (a^(1), w^(1), q^(1)) solves Lemma 6.4's system with the coefficients
of Lemma 6.3 at g0's data, source −Φ^(1) and zero data at r = a; h^(1) solves dRic^H(h) = 0 on Ω with the Cauchy data
of h_app^(1) plus those U^(1) induces by section 6.4 (spatial part a dr dr, ∂_τ of it by K + wΠ + q dr + dr q, ∂_τ of
lapse and shift by the linearised D = 0). Then e := h^(1) − h_app^(1) solves dRic^H(e) = −λ^(N+1) Re[R_X(H_(N+1))
e^(iv/λ)] with U^(1)'s data (the λ-series telescopes by (3.1)), and g_λ − g0° = h^(1) + r2 with r2 bounded by L.17,
L.18 (case Ω).

**(b) Lemma H_Σ (the ingoing projection; deduced, with edge1_5 X1-X3).** Let Ψ solve dRic^H(Ψ) = f on Ω with data
(Ψ_Σ, ∂_τΨ_Σ) on Σ_τ0, all zero on {v ≤ v_s}, T² × Z2 × Z2-invariant and of the form e^(iv/λ) times amplitudes Â (as
functions of v = τ0 + r on Σ_τ0 and of (v, r, θ) for f). Let 𝒟(v) be the supremum over Σ_τ0 ∩ {v′ ≤ v}, over Ω ∩ {v′ ≤
v} for f, and over Ω^β, |β| ≤ 2, [round 6, V5-m8: |β| ≤ 6; A28] of |Â_Ψ| + |Â_∂Ψ|/|s̃| + |Â_f|/|s̃|, where s̃ := κ_𝒟 +
i/λ and κ_𝒟 := (log 𝒟)′,
and assume 𝒟 satisfies L.16 (b), (c)'s hypotheses and |∂_v Â| ≤ C κ_𝒟 𝒟 for every amplitude. Then at P = (v, √μ0,
ω), v_s < v ≤ v_s + x0,

    Ψ(P) = e^(iv/λ) [ G(√μ0 ← r0) X_in(v) + Z_f(v) ] (1 + O(ϵ(v))) + O(𝒟(v)/|s̃(v)|),   r0 := v − τ0,
    X_in := ½ (F Â_Ψ + (2 − F) Â_∂Ψ/s̃) at r0,   Z_f := s̃⁻¹ ∫_(√μ0)^(r0) G(√μ0 ← r′) Â_f(v, r′, ·) dr′,

G the propagator of the transport T = 0 (the scalar sector's closed form: H_vv(√μ0) = μ0^(−3/4) r0^(3/2) [X_vv + F(r0)
X_vr + F(r0)² X_rr/4], X3), and ϵ := λκ_𝒟 if λκ_𝒟 ≤ 1, C(κ_𝒟^(α−1) + 1/κ_𝒟) otherwise. [round 6, V5-M1, R6-f1: the factor
1 + O(ϵ) comes only from replacing s⁻¹ by 1/s̃; exact form R6.1 (a)]

*Proof.* (1) *Characteristic form (X1, exact in all fifteen components).* With L := ∂_v + (F/2)∂_r, the outgoing null
direction, and P := iT (T the transport of L.2 (b)), dRic^H(h) = −P(Lh) + Q̃h with Q̃ free of ∂_v and of ∂_r² (first
order in r, second order in the angles). So Y := LΨ obeys P Y = Q̃Ψ − f along each generator of ℓ, and at the horizon
F = 0, so Y = ∂_vΨ there. (2) Along ℓ from Σ_τ0 (r = r0) to √μ0: Y(v, √μ0) = G(√μ0 ← r0) Y(v, r0) − ∫ G(√μ0 ← r′)
(Q̃Ψ − f)(v, r′) dr′. (3) The horizon is a generator of L, and Ψ = 0 there for v ≤ v_s: Ψ(v, √μ0) = ∫_(v_s)^v Y(v′,
√μ0) dv′. (4) *A priori bound:* |Ω^β Ψ| ≤ C 𝒟(v′) and |Ω^β (∂_v − i/λ)Ψ| ≤ C κ_𝒟 𝒟(v′) on Ω ∩ {v ≤ v′}. For this take
the leading two-sided parametrix: h_in := e^(iv/λ) G(r ← r0(v)) X_in(v), and h_out := e^(iψ(u)/λ) H(r ← r_Σ(u))
X_out(r_Σ(u)), with u the outgoing Eddington-Finkelstein time, ψ(u(τ0, r)) = τ0 + r, H the outgoing transport (X2: in
(u, r) the operator is −P′∂_u + Q′ with P′ of first order in r and Q′ free of ∂_u, so h_out's residual is e^(iψ/λ)
Q′(·), free of 1/λ), r_Σ(u) where the outgoing ray meets Σ_τ0, and (X_in, X_out) the solution, from zero at r_b := v_s
− τ0, of the matching system on Σ_τ0 (equal values and τ-derivatives; on Σ_τ0 the null covectors with tangential part
s dr are s dτ and −F s/(2 − F) dτ, X3, so the system is s X_in + ((2 − F)/2)Ã X_in = ((2 − F)/2) Â_∂Ψ + (F/2)(s +
A_out) Â_Ψ with bounded Ã, A_out, and |X_in| + |X_out| ≤ C 𝒟 by L.16). The source is taken up by the ingoing
particular solution h_f := e^(iv/λ) Z_f with zero data: Y_f := −∫_(r0(v))^r G(r ← r′) Â_f(v, r′) dr′ along ℓ and Z_f(v,
r) := ∫_(τ0+r)^v e^(−i(v−v′)/λ) Y_f(v′, r) dv′, so that s Z_f = Y_f, P(s Z_f) = −Â_f, Z_f = s Z_f = 0 on Σ_τ0 and |Z_f|
≤ C 𝒟; its residual is e^(iv/λ) Q Z_f. The difference e := Ψ − h_in − h_out − h_f has zero data and the source −(the
three residuals), at most C 𝒟 in the strip of v-width x that carries the amplitudes, so L.8 and L.10 give |Ω^β e| ≤ C
x^(1/2) 𝒟; h_out vanishes for u > u(r_b), a neighbourhood of the horizon's part in the strip. The same for (∂_v −
i/λ)Ψ, the solution with data and source (∂_v − i/λ)(·) (∂_v is Killing for g0° and commutes with dRic^H), whose
amplitudes are ∂_v Â. (5) *The error terms of (2)-(3).* The ∂_r Ψ terms of Q̃Ψ are integrated by parts along the ray,
leaving boundary terms and integrals of Ψ, so |∫ G Q̃Ψ dr| ≤ C 𝒟(v′) by (4) (angular derivatives up to two). Their
v′-integral: if λκ_𝒟 ≤ 1, one integration by parts against e^(iv′/λ) with the bound on (∂_v − i/λ)Ψ gives at most C λ
𝒟(v); if λκ_𝒟 ≥ 1, ∫_(v_s)^v 𝒟 ≤ C 𝒟(v)/κ_𝒟 (log-concavity). Either way O(𝒟/|s̃|). (6) *The main term* ∫_(v_s)^v
G(√μ0 ← r0(v′)) Y(v′, r0(v′)) dv′, with Y on Σ_τ0 equal to e^(iv′/λ)(½(2 − F)Â_∂Ψ + ½F s̃ Â_Ψ)(1 + O(ϵ)) (on the data
∂_r|_v = ∂_r|_τ − ∂_τ, and ∂_r|_τ acts on the amplitude as s̃ up to O(ϵ), X3: X_in = (LΨ)/s̃), is e^(iv/λ) G X_in (1 +
O(ϵ)) by L.16 (b) (λκ ≥ 1) or two integrations by parts (λκ ≤ 1); likewise the source's term gives Z_f. ∎

**(c) Lemma L.21 (the first-degree constraint correction; deduced, with edge1_5 X4-X7).** (i) The first-degree part
of D(g_app) is exactly λ^(N+1) Re[D_X H_(N+1) e^(iv/λ)] on Ω, and that of Ric^H(g_app) is λ^(N+1) Re[R_X(H_(N+1))
e^(iv/λ)]. (ii) Write D_X H_(N+1) = Σ_k env^(k) D_k. On Σ_τ0, D_N = i^N A τ r^(−3/2) dθ (tangential) and the (v, r)
components of D_(N−1) are N i^N A d (−r^(−7/2)/2, r^(−7/2)). (iii) The ρ-component of Φ^(1) at r0 is

    F_ρ = λ^(N+1) Re{ e^(iv/λ) i^N A d(θ) r0^(−7/2) [ env^(N) − c_N s env^(N−1) ] } (1 + O(1/κ + λ)),
    c_N := N μ0/(r0² + μ0),   s := ∂_v + i/λ.

(iv) a^(1)(r0) = −λ^(N+1) Re{e^(iv/λ) i^N A d α(r0)⁻¹ r0^(−7/2) env^(N−1) Ξ} (1 + O(ϵ + 1/|s̃| + λ)), α(r) := 3r³/(r² +
μ0)², Ξ := [(1 − c_N) λκ_(N−1) − i c_N]/(λκ_(N−1) + i), κ_k := (log env^(k))′; and |Ξ|² = [(1 − c_N)² T² + c_N²]/(T² + 1)
≥ min(c_N², (1 − c_N)²), T := λκ_(N−1), Ξ = −c_N − iT + O(T²) (X8). [round 6: with ϵ replaced by ϵ′ := min{(λκ)² + λκ^α,
κ^(α−1)}, (iv′), R6.1 (b)] (v) The ingoing amplitude of the scalar data
a^(1) induces, transported to the horizon, is H_vv(√μ0) = K_R a^(1)(1 + O(1/|s̃|)) with K_R = μ0^(−3/4) r0^(−5/2) (r0²
− μ0)²/4 if section 6.4's "lapse and shift of g_app" means g_(τμ) (reading 1) and K_R = μ0^(−3/4) r0^(3/2)/4 if it means
the ADM lapse and shift vector (reading 2); K_R > 0 in both, [round 6, V5-m6: a third reading gives (r0² − 2μ0)/(4
μ0^(3/4) r0^(1/2)); A30] and it depends neither on the τ-derivative of the spatial
part nor on K's sign convention (X7: D = 0 fixes the combination X_vv + F X_vr that reaches the horizon). (w^(1),
q^(1)) and the stage profiles' data enter the scalar sector at relative order O(1/κ + 1/|s̃|).

*Proof.* (i) At first degree the λ^(m−1) part of the linearised contracted Bianchi identity B[D] = −div Gt(E) is a
transport along ℓ of δ_m := i Pol(H_(m+1)) + D_X H_m with a source from E's order-m profile, zero for m ≤ N (by (3.1));
δ_m = 0 on Σ_τ0 by the rule (D615 for m = N), so δ_m = 0 on Ω for m ≤ N (Lemma 6.1's induction at first degree), and
dD(h_app^(1)) = Σ_m λ^m δ_m e^(iθ) + λ^(N+1) D_X H_(N+1) e^(iθ); the Ric^H statement is (3.1) telescoped. (ii) D_X =
Pol∘∂_v + q (L.13 (a)); by L.13 (b) the top two families of H_(N+1) are i^(N−1) c_20 and (N − 1) i^(N−2) c_30, and on
Σ_τ0 the rule gives Pol(c_(j+1,k)) = i [D_X H_j]_k; the recursion for the scalar part of family j − 2 of D_X H_j is x_j
= i x_(j−1) + i^(j−2) q(c_20)_sc, x_2 = q(c_20)_sc, so x_(N+1) = N i^(N−1) q(c_20)_sc (X5, N ≤ 40), with q(c_20)_sc = i
A d (r^(−5/2) β, r^(−7/2)) and β(r0) = −1/(2r0) (layerlin5 N4); the top family is i^(N−1) Pol(c_20) = i^N A τ r^(−3/2)
dθ (N3). (iii) 2G(n, n) = 2 Gt(E + S(D))(n, n) at first degree; E's top family (−iT of the top family of H_(N+1), a
multiple of R_X(H_1)) has no (n, n) part and zero trace (N1 (a), N3), and S(D)'s is computed in X4: for D = e^(iv/λ) (X1
f τ dθ + X0 d (p dv + q dr)), 2Gt(S(D))(n, n) has no s X1 term, the X1 coefficient f d/r² and the s X0 coefficient d(2
(n·dv) D0(n) + g0⁻¹(dv, D0)); with (ii), the bracket. The lower families are smaller by O(1/κ) (one env-derivative
fewer) or O(λ) (no phase derivative). (iv) The ρ-equation of (6.4) at g0's data is α ∂_r a − Δ_α a + b·∂_S a + c a + e_w
w = −F_ρ (K at g0's data has no rθ part, so q does not enter it), α computed in X6 (Lemma 6.3's coefficient, no ∂_r² a).
Its solution from zero at r = a, with the oscillating source, is a = −(α s)⁻¹ F_ρ plus terms of relative order 1/|s̃|
(Δ_α a, b·∂_S a, c a, e_w w, the last from the J-equations, where w ∼ (F_J,r + 2r⁻² ∂_θ q)/(6 s̃)); the remainder after
two terms of this expansion has a source of relative order |s̃|⁻² and Lemma 6.4's bound on [a, r] makes it
O(x^(1/2)/|s̃|) relative. s⁻¹(env^(N) − c_N s env^(N−1)) = (1 − c_N) env^(N−1) − (i/λ) s⁻¹ env^(N−1) (since s⁻¹∂ = 1 −
(i/λ) s⁻¹) and s⁻¹ env^(N−1) = env^(N−1)/(κ_(N−1) + i/λ) (1 + O(ϵ)) by L.16 (b) for env^(N−1) ((H_N)) or by integration
by parts (λκ ≤ 1): the bracket is env^(N−1) Ξ. (v) X7: the data of a dr dr on Σ_τ0, the τ-derivative of the spatial rr
part (any value), and D = 0 at leading order (∂_v H_rr + (F/2)∂_r H_rr = 0, ∂_r H_vv + F ∂_r H_vr − (F/2) ∂_v H_rr = 0),
give the ingoing amplitudes printed by X7, which X3's transport takes to K_R a. (w, q) are a K- correction, whose
amplitudes after division by s̃ are of relative order 1/|s̃| and lie in the vector sector and the tangential trace,
which T = 0 does not take to vv; the stage profiles' scalar sector is a family lower (κ^(N−2) against κ^(N−1)). ∎

**(d) Proposition L.22 (the first-degree horizon value; deduced).** Assume (H_N): env and env^(k), k ≤ N, are positive
and log-concave on (v_s, v_s + x0] with κ_k/κ ∈ [1/2, 2], |κ_k′| ≤ c_R κ_k^(1+α) for an α < 1 − 1/(N − 2), [round 6,
V5-m4: α < 1 suffices, and E_S is L.22′'s; R6.1] and L.16
(c)'s bounds |env^(j)| ≤ c_j κ^j env (sampled for exp(−1/x) and the record's envelope on x ≤ 10^(−2), k ≤ 12: X10).
Then for v_s < v ≤ v_s + x0, h^(1)_vv(v, √μ0, θ) = Re[S(v, θ) e^(iv/λ)] with

    S = S_st + S_U + E_S,   S_st := λ³ A ν(r0) d env (1 + 2iλκ) 𝟙_(λκ≤1),
    S_U := −λ^(N+1) A Γ_R(r0) i^N d Ξ env^(N−1),   Γ_R := K_R r0^(−7/2)/α(r0) > 0,
    |E_S| ≤ C [λ³ env ((λκ)² + λ) 𝟙_(λκ≤1) + λ^(N+1) κ^(N−2) env 𝟙_(λκ>1) + (ϵ + 1/κ + λ) |S_U|],

and |∂_v^k E_S| ≤ C κ^k (the same), k ≤ 2. The last term of S_st is L.13 (c)'s top family at j = 4 (2iλ env′ = 2iλκ
env); for λκ > 1 the stage sum Σ_j λ^j H_j,vv is at most C λ^(N+1) κ^(N−2) env, a family below S_U.

*Proof.* h^(1) = h_app^(1) + e: h_app^(1)'s horizon value is Σ_(j≤N+1) λ^j H_j,vv(v, r_q) (L.13 (c), Corollary L.11's
proof with (H_N)'s derivative bounds in place of ε_M); e's is Lemma H_Σ with U^(1)'s data (Lemma L.21) and the source
−λ^(N+1) R_X(H_(N+1)) (whose scalar sector is a family below its top, which is S-class, so Z_f's vv part is at most
C λ^(N+1) κ^(N−1) env/|s̃|). The derivative bounds: ∂_v commutes with dRic^H, and every amplitude's derivative is κ
times it, by (H_N). ∎

**(e) Lemma W (two signs on a window; deduced, elementary; X9).** Let J := [v, v + 4πλ], S ∈ C²(J; ℂ), ε: J → R and
f := Re[S e^(i·/λ)] + ε. (A) If |S| ≥ m on J, arg S varies by at most π/6 on J and |ε| ≤ m/4, f takes both signs on
[round 7, V6-m2: stated pointwise as (A′), R7.1]
J. (B) If |S′| ≥ L0 and |S″| ≤ L0/(80πλ) on J and |ε| ≤ πλL0/5, f takes both signs on J. [round 6, V5-n6: (B) is used by
no proof]
*Proof.* (A) The phase t/λ + arg S(t) increases by at least 4π − π/6 on J, so it meets 0 and π modulo 2π, where f ≥
m − m/4 and f ≤ −m + m/4. (B) S(t) = S′(v)(t − t0) + R(t), |R| ≤ πλL0/10, t0 = α + iβ. At the points t_k where
e^(i(t/λ + arg S′(v))) = ±1 (spacing πλ, alternating), Re[S′(v)(t − t0) e^(it/λ)] = ±|S′(v)|(t_k − α) (the β part
vanishes there), so |f(t_k) ∓ |S′(v)|(t_k − α)| ≤ 3πλL0/10. If one side of α within J, beyond α ± πλ/2, has length ≥
2πλ, it holds two consecutive t_k of opposite type and |t_k − α| ≥ πλ/2: two signs. Otherwise both sides have lengths
in [πλ/2, 2πλ), each holds a t_k, and the gap of length πλ around α holds exactly one: the left side's last and the
right side's first are of the same type, on opposite sides of α: two signs. ∎

**(f) Theorem L_1E (Theorem 1's deep layer and very edge; deduced from L.17, L.18, H_Σ, L.21, L.22 and Lemma W, with
edge1_5 X1-X11 and degtwo5 T1-T4).** Let μ0 = √72 l5², K ≥ 6, N = K + 3, g_λ the metric of Theorem 1 built by the
supplement with stage N's data by Lemma 6.2's rule (D615, D616), env satisfying (H_N) and (H_D), and τ0 admissible with
ρ0² := (v_s − τ0)²/μ0 ∉ {N − 1, 2N − 1}. [round 6, V5-M1, V5-m4, V5-m6: restated as Theorem L_1E′, R6.1] [round 7:
Theorem L_1E″, R7.3, excludes neither value] [round 8, the reader of round 7's m1: 2N − 1 for N ≡ 0 mod 4 under (H_N+2)
and (H_t), R7.2; both proved for the record's envelope, Proposition L.27; Theorem L_1E‴, R8.4] There are λ_1E > 0, x0′ ∈
(0, x0] and P1 (depending on K, the record's costs, the envelope's constants and the distance of ρ0² from {N − 1, 2N −
1}) such that for λ ≤ λ_1E, every v ∈ (v_s, v_s + x0′] with env(v + 4πλ) ≤ λ^(P1) and every ω ∈ S³: on [v, v + 4πλ] the
boundary x_K = 1 has, at ω, points where it is timelike for g_λ and points where it is spacelike. In particular on the
whole very edge {λκ ≥ 1}, down to v_s. With Proposition L.12 (ii) at P := P1 (first-reach points; every point for an
envelope increasing at its edge) and λ ≤ min(λ_U(P1), λ_1E): every such interval below the level λ^(3+δ).

*Proof.* At X = (v′, r_q(v′), ω): g_λ⁻¹(dΦ0, dΦ0) = −m0 − h^(1)(Φ0♯, Φ0♯) − r2(Φ0♯, Φ0♯) + q (Lemma L.1), Φ0♯ =
∂_v + β0 ∂_r with β0 = O(ε²), and h^(1)(Φ0♯, Φ0♯) = Re[S e^(iv′/λ)](1 + O(ε²)) + O(r_q − √μ0)|∂_r h^(1)| (D3). The
non-harmonic part ε(v′) := −m0 − r2(Φ0♯, Φ0♯) + q + (the β0 and r_q shifts) is at most C κ^(2c′) env² by L.17, L.18 and
m0 ≤ C(env² + ∫ env²) ≤ C env² (log-concavity). Fix ω, put J := [v, v + 4πλ]. *Case 1 (S_U ≥ S_st up to a factor, or
λκ ≥ 1).* |Ξ| ≥ min(c_N, |1 − c_N|) ≥ c0 > 0 (x0′ small keeps c_N(r0) away from 1), so |S| ≥ (c0/2)|S_U| [round 6, R6-f1:
this needs (ϵ + 1/κ + λ) small, false at λκ ≈ 1 with ϵ = λκ; R6.1] and Lemma W
(A) applies: arg S_U moves per carrier radian by O(κ^(α−1) + λ^(1−α)) (d arg Ξ/dT = O(1/(1 + T²)) and |dT/dv| ≤ c_R λ
κ^(1+α)), env^(N−1) > 0, and ε ≤ C κ^(2c′) env² ≤ |S|/8 once env ≤ λ^(P1) (for λκ ≤ 1, κ ≤ 1/λ; for λκ > 1, env is
smaller than every power of 1/κ by L.16 (c)'s second hypothesis). *Case 2 (S_st dominant, Λ := λ^(N−2) env^(N−1)/env ≪
1)* is Theorem L's: |S| ≥ |S_st|/2 = λ³ A |ν| |d| env/2 (at the double root ρ* of ν, |ν| ≥ c x² as in round 1 section
7, and x² ≫ λ in this case) [round 6, V5-M1 (b): not for every edge (H_N) admits; (H_ρ*), R6.1], phase as in Case 1,
Lemma W (A). *Case 3 (the crossover, |S_st| ≈ |S_U|, λκ ≪ 1).* The
amplitudes are λ³ A d env [ν(1 + 2iT) + Γ_R i^N (c_N + iT) Λ] + E_S (Ξ = −c_N − iT + O(T²)). If i^N Γ_R c_N Λ/ν is not
a negative real number the two real parts do not cancel and |S| ≥ c λ³ |ν| env (Lemma W (A)); if it is (N ≡ 0 or 2
modulo 4, according to ν's sign), at the cancellation the quadrature part is T ν (2 − 1/c_N) ≠ 0 (X8; c_N ≠ 1/2), so
|S| ≥ c T λ³ |ν| env, which exceeds |E_S| ≤ C (T² + λ + κ^(α−1) + 1/κ) λ³ |ν| env since at the crossover κ ≈
λ^(−(N−2)/(N−1)) and (1 − α)(N − 2) > 1; [round 6, V5-M1 (a): this bound misquotes L.22 (it drops ϵ |S_U|, puts |ν| on
the λ-term, and writes T for λκ and λκ_(N−1)) and does not close at a real cancellation; Case 3 is redone in R6.1] Lemma
W (A) again. In every case ε is below m/4. ∎

X11 runs the two-term formula with unit constants [round 6, V5-m1: now with L.22's cutoff, and S_U removed as its
control] (exp(−1/x), λ = 10^(−6), r0 = 3, ν = −1/9) for N = 9 (the two
amplitudes in quadrature) and N = 12 (their real parts cancel at the crossover), over 1200 windows each from env = λ⁴
to x = 0.2 λ^(1/2): every window has both signs (control: a degree-two term inflated by λ^(−8) leaves windows with one
sign).

*Remarks.* (1) The constraint correction, not the approximant, carries the first-degree term once Λ ≫ 1: on the very
edge of Theorem 1's solution the boundary is decided by the solve of section 6.3 at first degree. (2) The excluded τ0
[round 7, V6-m1: ρ0² = N − 1 is not excluded, the errors being relative to the bracket (R7.1); ρ0² = 2N − 1 is admitted
by Case 3′ (R7.2)] [round 8, m1: for N ≡ 0 mod 4 under (H_N+2) and (H_t); proved for the record's envelope, L.27]
are two values: at ρ0² = N − 1 the coefficient (1 − c_N) of Ξ's limit vanishes and |S_U| falls to the size of E_S on
the deep very edge; at ρ0² = 2N − 1 the quadrature part at a real cancellation vanishes. (3) The hypotheses (H_N),
(H_D) are properties of the envelope near its edge, satisfied by exp(−a/x^q) edges [round 6, V5-m4: for q > 1/(N − 3)
under round 5's α; every q > 0 under R6.1's] and checked for the record's C_c^∞
envelope (X10, T4); the solver's sin⁴ envelope is not flat and is outside Theorem 1 (R3.3).

### R5.4 The transition, the dips, and the levels at fixed λ (task (b))

**Theorem L.24 (one switch per column; deduced, with degtwo5 T5).** Let K ≥ 6, env increasing at its edge with (H_N),
δ ∈ (0, 1/2], and let Proposition L.12 (iii) hold (λ ≤ λ_U). Fix ω and divide the band λ^(3+δ) ≤ E ≤ λ^(3−δ) into
consecutive carrier periods I_k of length 2πλ; put M_k := max_(I_k) g_λ⁻¹(dΦ0, dΦ0) at ω. Then M_(k+1) < M_k wherever
R ∈ [1 − 2λ^γ, 1 + 2λ^γ], M_k > 0 where R ≥ 1 + 2λ^γ and M_k < 0 where R ≤ 1 − 2λ^γ: the sequence (M_k) changes sign
exactly once. Before the switch every carrier period has timelike points at ω; after it the boundary is spacelike
throughout every period at ω.

*Proof.* In the band λκ ≤ λ^(δ′) and Λ ≤ λ, so g_λ⁻¹(dΦ0, dΦ0) = −m0 − Re[S e^(iv/λ)] + ρ with S = S_st + E_S (L.22) and
ρ the degree-two part. Write ρ = ρ_s + ρ_r: ρ_s the explicit degree-two profiles of g_app at the boundary (the means λ
m_j, the second harmonics λ χ and their higher-order companions, and q of Lemma L.1), whose amplitudes are of size C λ
ε² and vary at rate C κ times that; ρ_r := w − e, the degree-two part of the remainder, at most C λ^(N−6) ε_c(v_1)² by
L.4's energy argument applied to w − e, whose source and data are of degree two (Ric^H(g_app) minus its first-degree
part, at most C λ^(N−1) ε² by (F2); the coefficient differences acting on w and e, at most C λ^(N−6) ε²; U − U^(1), L.17
(4)) [round 6, V5-m7: L.17 (4) gives C ε_c²; the bound used, C λ^(N−2−j) ε_c², is proved in R6.3], with v_1 − v = O(λ)
and ε_c(v_1) ≤ 2 ε_c(v) at these levels (R2.6's window argument). For t ∈ I_k, g⁻¹(t + 2πλ) −
g⁻¹(t) = −[m0(t + 2πλ) − m0(t)] − Re[(S(t + 2πλ) − S(t)) e^(it/λ)] + [ρ(t + 2πλ) − ρ(t)] (e^(2πi) = 1). With m0′ ≥ 1.9 κ
m0 and |S′| ≤ (1 + O(λκ)) κ |S|, at R ≤ 1.1: m0′ − |S′| ≥ 0.93 κ m0 (T5: m0′/(κ m0) ≥ 2.001, resp. 2.003, and (m0′ −
|S′|)/(κ m0) ≥ 0.936, resp. 0.968, for exp(−1/x), resp. the record's envelope, at R ∈ [0.9, 1.1], m0's formula exact).
The ρ_s increment at a fixed phase is at most 2πλ C κ λ ε², the ρ_r one at most 2 C λ^(N−6) ε², both below πλκ m0/4 for
λ small (m0 ≥ c ε² at these levels, N ≥ 9). So every value on I_(k+1) is below the value a period earlier by at least
1.7πλκ m0 − πλκ m0/2 > 0: M_(k+1) < M_k. The signs where |R − 1| ≥ 2λ^γ are L.12 (iii). ∎

T5's model (exp(−1/x), λ = 10^(−6), a slowly varying degree-two term of size λ^(1/10) m0 and a structureless one of
size λ³ m0) finds the maxima over 80 consecutive periods around R = 1 strictly decreasing with one sign change (control:
a structureless term of size m0/3 gives more).

**Proposition L.25 (dips; deduced, with degtwo5 T6).** (a) *False in general.* Let env := Σ_(n≥n0) e^(−n²) β(2^(n+2)(v −
v_s − 2^(−n))) near v_s, β(t) := e^(−1/(1−t²)) on [−1, 1], continued to a C_c^∞ envelope: smooth and flat at v_s
(e^(−n²) 2^(kn) → 0 for every k), zero on the intervals J_n between consecutive bumps. For λ small take n with e^(−n²−1)
∈ [λ⁴, λ^3.1]; on J_n — inside the layer, below λ^(3+δ) for δ ≤ 1/10 — the boundary is spacelike throughout at every
angle, for Theorems 1 and 2: there g_λ⁻¹(dΦ0, dΦ0) ≤ −m0/2 < 0. Indeed m0 ≥ (2/27) ∫ env² ≥ (2/27) e^(−2n²) 2^(−n−2) ∫β²,
while the first-degree term is the oscillatory tail of bump n: for Theorem 2 λ|ν∞ d||I_2| ≤ λ⁹ ∫|∂_u⁸(u bump_n)| (eight
integrations by parts of I_2), for Theorem 1 the same for the stage and source terms (H_Σ's representation (3),
integrated by parts in v′; the stage profiles vanish on J_n) and the U^(1)-memory is at most λ^(N+9) sup|bump_n^(N+8)|
times the bump's width (Lemma 6.4's solution operator does not depend on λ); the ratio to m0 falls like (λ 2^(n+2))^9
e^(n²) → 0 as λ → 0. The degree-two terms are O(λ m0). [round 6, V5-M2: asserted, not derived; (a) is proved by another
route in R6.2] T6 prints the three quantities at λ = 10^(−8), 10^(−10), 10^(−12)
(n = 8, 9, 10: the first-degree bound 1.0·10^(−69), 2.8·10^(−93), 9.9·10^(−118) against m0 ≥ 2.5·10^(−61), 2.1·10^(−76),
3.3·10^(−93); at λ = 10^(−6) eight integrations by parts do not yet suffice); control: on a bump's top the first-degree
term exceeds the margin. So "every interval of length 4πλ in the layer below λ^(3+δ) has timelike points" is false for
such envelopes, for every small λ. (b) *True criterion for every envelope.* At every boundary point in the deep layer,
g_λ⁻¹(dΦ0, dΦ0) = −m0 − Re[S e^(iv/λ)] + O(degree two) with S the exact first-degree amplitude: for Theorem 2's solution
S = λ A ν∞ d I_2(v) + O(λ sup|I_3|) for every envelope (L.15_P (b) uses no property of env), for Theorem 1's S of L.22
wherever (H_N)'s bounds hold on [v − 1/κ, v] (locally). So every interval [v, v + 4πλ] has timelike points at ω if max_J
(|S| − m0) ≥ C(λ^γ m0 + degree two) and none if max_J (|S| + C degree two) < min_J m0: the causal character is decided
by the ratio |S|/m0 up to the factor 1 ± 2λ^γ, at every point, dips and zeros included; [round 6, V5-m10: withdrawn;
(b′), R6.2] at a transversal crossing of the
ratio through 1 the switch is single (the proof of L.24, which uses only m0′ − |S′| ≥ c κ m0 there). (c) *True for
log-concave edges:* Theorems L_E (Theorem 2) and L_1E (Theorem 1), down to v_s.

**The levels between λ^P and the very edge at fixed λ (Theorem 1).** L_1E's level λ^(P1) does not depend on λ. So
Proposition L.12 (ii) with P := P1 and L_1E together cover, for λ ≤ min(λ_U(P1), λ_1E), every level below λ^(3+δ) down
to v_s: nothing is left between them.

### R5.5 C_L11 and C_L4 as formulas (task (d); deduced, with constL5 K1-K3) [round 6, V5-m11: and K4]

Both constants are assembled from the steps of the proofs of Lemma L.3, Corollary L.11 and Lemma L.4, each step a
monotone expression in the constants of the supplement it invokes. With K := K_s + P_6 (P_i := sup_(Ω×S¹) Σ_j |∂^i g_j|,
K_s the bound of the seed's operator coefficients on Ω with two derivatives), C_tr := e^(2πK(b(τ0) − a)) (L.9 (b) with
‖∂_θ⁻¹‖ ≤ π, ‖Π_osc‖ ≤ 2), C_N := C_S3 (1 + √2 (b(τ0) − a)^(1/2) a^(−3/2)) (L.10, C_S3 the H²(S³) ⊂ L^∞ constant) and
C_E := C2 (L.8 is Lemma 2.3 on Ω_v), the recursion over the stages m = 1, ..., N reads

    Ce_m = C64 K (sa_m² + sb_m),                               sa_m := Σ_(l≤m) Ca_l,   sb_m := Σ_(l<m) Cb_l,
    Ca_(m+1) = C_tr (K_s (P_6 Ce_m + K sa_m) + (b − a) K sa_m (1 + sb_m)),          Ca_1 := A K_s,
    Cb_m = C_N C_E e^(C_E T) (Ce_m + T K (sa_m² + sb_m) + T K Ca_(m+1) (1 + sa_m)),   T := τ_end − τ0,
    Cc_(m+1) = C_tr (K (Cc_m + Cb_m + sa_m Ca_m) + K_s Ce_m),                       Cc_1 := C_tr K (A K_s)²,
    Cd = K^(N+1) (1 + sa + sb)^(N+1)/(N − 2)!,    CU = 2 C0 K (sa + sb),

(L.3 (e), (a), (b), (c), (d), U), and

    C_L11 = max{ Σ_(j=4)^(N+1) λ0^(j−4) Ca_j,  Σ_(j≤N+1) λ0^(j−1) Cc_j + λ0² Ca_3 C_D3 + 3 C_β Σ_j λ0^(j−1) Ca_j,
                 (1 + C_β)² },
    C_L4 = C_S e^(C2 (1 + M + K) T) (CU (1 + K_s) + T Cd),

with C_D3 = (2/9) A²/(4√μ0), C_β = (2/9) A² (3/(4μ0)) (D3). K1: the leaves of this DAG (83 named constants at N = 9)
are, of the profile bounds, P_6 (order 6 ≤ 11), and C64, C0, M, C2, λ0, the certified a, b(τ0), τ_end − τ0, C_S, A, μ0,
and the seed's K_s, C_S3: nothing outside λ0's leaves (CONSTANTS5 1.3, 1.5) but two constants of the seed alone
(control: a step needing P_12, beyond the order λ0 uses, is detected). K2: with the certified numbers inserted, both
increase in every remaining leaf (each node a positive expression; finite differences at 40 points; control: a node with
a difference is detected), so upper bounds of the leaves give upper bounds of C_L11 and C_L4. K3 prints them at P* in
the remaining leaves (as an illustration only, with each remaining leaf 1 and λ0 = 0.00244: log10 C_L11 ≈ 1.8·10^5,
log10 C_L4 ≈ 1.8·10^6). So λ_L's dependence on C_L11, C_L4 is a stated formula in the leaves of λ0: a number for λ_L
needs exactly the certified nine-stage solve that a number for λ0 needs (CONSTANTS5 1.5), and the seed's two constants,
and nothing else. Until then the certified statement stands: the threshold this proof delivers is below 2.71·10^(−12)
whatever those leaves are (R4.5), and below 10^(−285.27) max(C_L11, C_L4)^(−4/3) (Λ_8b, Λ_8d) and 10^(−36.99)
C_L11^(−1/11.5) (Λ_8c).

### R5.6 λ_L, updated

λ_L = min{λ0 (< 0.0024433), 1/(2 C1), Λ_4(C1) (≤ 2.71·10^(−12) (1 + 0.945 C1)^(−1.0097)), Λ_5′ (∈ [10^(−2.92),
10^(−2.82)]), Λ_6 (≤ (64.55 C1)^(1/27)), 0.611, Λ_8b,d (∈ [10^(−296.75), 10^(−285.27)] max(C_L11, C_L4)^(−4/3)), Λ_8c (∈
[10^(−38.49), 10^(−36.99)] C_L11^(−1/11.5))}, with C_L11, C_L4 of R5.5 and C1 from Theorem 1's C (CONSTANTS5). Theorem
L_1E and L.24 add thresholds λ_1E, λ_D of the same kind (finite expressions in the same leaves and the envelope's
constants); they are below Theorem L's threshold or do not bind Theorem L's statement, and they enter no number the
paper prints.

### R5.7 Open items

None is left. O1a′: closed (Theorem L_1E). [round 6: V5-M1 and V5-M2 reopened O1a′ and O1d; closed again in R6.1, R6.2]
O1b: closed (Theorem L_E with L.17, L.18 proved). O1c: closed (round 4).
O1d: settled (Proposition L.25: false in general, true for log-concave edges, a criterion at every point). O1e: settled
(Theorem L.24). The levels between λ^P and the very edge: covered (R5.4). O2: round 5 awaits an independent reader, as
every round has. O4: λ_L is an explicit formula in λ0's leaves (R5.5, R5.6), certified below 2.71·10^(−12). O5:
answered (A3). O6: closed (D615, D616).

### R5.8 Proposed paper text (replaces R4.8's P1″ and P2″; P3-P6 stand, P3's list extended) [round 6: superseded by R6.5]

(P1‴) Proposition 3.2: replace the sentence from "If μ0 = √72 l5² exactly, the" to "Propositions E.2-E.4)." by:

> If μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the shell
> starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
> `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that layer, for λ small, every column has points
> where it is timelike for g_λ, so the no-return property stated above for μ0 > √72 l5² fails at equality
> (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L, L_P, L_E and L_1E, Corollary L.7).

(P2‴) Section 9: replace the bullet "**The boundary at equality.**" by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced in `docket68/n1star/EQUALITY5.md` and `EQUALITY5-LAYER.md`
>   [†], computed by the programs of Appendix A), x_K = 1 is the seed's horizon on {v ≤ v_s}, v_s := inf supp env, and is
>   spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η. In the layer between, for λ small and 0 < δ ≤ 1/2, it is spacelike
>   where sup_(v'≤v) env ≥ λ^(3−δ), and where λ^(3+δ) ≤ sup env ≤ λ^(3−δ) its character is that of the ratio of λ³ A env
>   |ν| |d| to the margin, up to a factor 1 ± 2λ^(1/10) (d the double divergence of the waves' angular tensor, |d| ≥ 8/3;
>   ν a coefficient of the seed and τ0). If env is flat and log-concave at its edge, with κ := (log env)′ obeying |κ′| ≤
>   c κ^(1+α) (α < 1) and the derivative bounds of `EQUALITY5-LAYER.md` R5.2-R5.3 (checked by sampling for the C_c^∞
>   envelope used for the constants), and for Theorem 1's solution (v_s − τ0)²/μ0 ∉ {K + 2, 2K + 5}, then that ratio
>   crosses 1 once per column, and below λ^(3+δ), down to v_s, every interval of length 4πλ has timelike and spacelike
>   points on every column; the term linear in the waves is computed there to leading order, for Theorem 1 carried by the
>   constraint correction at first degree. With flat interior zeros near the edge some such intervals are spacelike
>   throughout. So timelike curves of g_λ cross x_K = 1 into D_T, and a domain O(λ)-close to D_T has an inner boundary no
>   causal curve enters (EQUALITY5.md, Proposition E.4). λ_L is an explicit formula in λ0's constants, and the threshold
>   this proof delivers is below 3·10^(−12).

[†] "(rounds 1-4 read by independent verifiers; round 5 not yet read)". (P3‴) Appendix A, C, D: add
`checks/edge1_5.py` X1-X11, `checks/degtwo5.py` T1-T6 and `checks/constL5.py` K1-K3 beside round 4's entries (about
five minutes, ten minutes and two minutes), each with its controls as in its docstring; P5's commands for bandL4p5 and
lamL5b stand, with their new md5s.

### R5.9 Labels and sources (round 5)

*Labels.* Computed: X1-X8, T1-T3 (exact, sympy); K1-K3 (exact rationals and sympy); X9, X10, T4, T6 (sampled or
bounds, mpmath); X11, T5 (mpmath, models with unit constants; T5's m0 formula exact). Deduced: Lemma L.15_P (b) in full,
Lemmas L.17, L.18, H_Σ, L.21, W, Proposition L.22, Theorems L_1E and L.24, Proposition L.25, the formulas of R5.5;
L_E deduced on its hypotheses (A23); relabelled: L.19 (iv) a sketch (V4-m1). READ: N1STAR-PROOF.md (md5 709c63be…) [round
6, V5-n8: commit 1b38ece]
sections 0.2 ((0.2): the quasilinear form), 1, 2, 5.1-5.4, 6.1-6.4 (Lemma 6.2 as amended at D615, D616; Lemmas 6.3,
6.4, Proposition 6.5; section 6.4's data assembly), 9.1-9.4 (Lemma 9.5, Proposition 9.8, Theorem P) as in R2.9;
CONSTANTS5.md sections 1.3-1.5 and Round 4 (λ0's leaves; λ0 < 0.0024433); layerlin5 N3-N4 (H_2, D_X H_2); the verifier
of round 4's report (verdicts, findings, as relayed); the coordinator's re-pinning of stagen5 and stagefree5.

Files (round 5): this section; `checks/edge1_5.py`, `checks/degtwo5.py`, `checks/constL5.py`, each with its `.out`;
changed and rerun: `checks/bandL4p5.py`, `checks/lamL5b.py`, each with its `.out`; round 4's reruns moved into place.

## Round 6 (2026-11-06)

This round seats the verifier of round 5, each finding re-derived before it is repaired (R6.0); repairs the two majors by
proof, not by relabelling (R6.1: Theorem L_1E′; R6.2: Proposition L.25′); proves the smaller repairs (R6.3); and revises
the paper texts (R6.5). Round 5's text stands; bracketed notes "[round 6, …]" at its sites point here.

### R6.0 The verifier of round 5, seated (each finding re-derived)

Verdicts READ from the report (as relayed) and confirmed here: L.22's two-term structure (c_N, α, X7's data, K_R in
readings 1 and 2); Λ ≫ 1 before the very edge; Lemma H_Σ up to a derivative count; L.15_P (b), L.17 and L.18 in full;
Theorem L.24; R5.5's formulas as transcribed; λ_L ≤ 2.7041·10^(−12) (lamL5b M5); R5.1's seating; the two old paper texts
each once in RESPONSE-HL-5D.md (md5 7193c56e…, unchanged at this round's reading); all twelve programs reproduce.

- **V5-M1 (a) (major).** Re-derived and confirmed. For N ≡ 0 mod 4 (K ≡ 1 mod 4) the real parts of S_st and S_U cancel
  inside the crossover (ν < 0 off ρ*, Γ_R > 0, i^N = 1). There round 5 set the quadrature part T0 |ν| |2 − 1/c_N| λ³ A
  |d| env, T0 := λκ, against a bound that misquotes L.22: L.22's E_S contains (ϵ + 1/κ + λ)|S_U| with ϵ = λκ (the factors
  1 + O(ϵ) of H_Σ and of L.21 (iv)), and |S_U| ≈ |S_st| at the cancellation, so E_S may be C T0 |ν| λ³ A |d| env, the
  quadrature part's own order with C unknown; the misquote drops that term, puts |ν| on the λ-term (the family below L.13
  (c)'s top does not carry ν) and writes T for both λκ and λκ_(N−1). X12 measures it with unit constants: over the whole
  crossover the least ratio of |σ_main| to round 5's bound stays at 1.04-1.17 from λ = 10^(−10) to 10^(−80). Repaired by
  proof, for every N (R6.1).
- **R6-f1 (found in this round; the same cause).** Round 5's Case 1 needs |E_S| ≤ (c0/4)|S_U|; at λκ ≈ 1 the term C ϵ
  |S_U| with ϵ = λκ ≈ 1 does not give it. Repaired by the same sharpening: ϵ′ ≤ C κ^(α−1) for every λ (R6.1 (b)).
- **V5-M1 (b) (major).** Re-derived and confirmed. At ρ0 = ρ*, ν(r0) = −c_ν x² (1 + o(1)), x := v − v_s, c_ν > 0 (round 1
  section 7). Case 2 needs λ ≪ |ν|. For exp(−1/x^q) the Case 2/3 boundary λ^(N−2) κ^(N−1) ≍ x² lies at x ≍
  λ^((N−2)/((q+1)(N−1)+2)), where x² ≫ λ iff q > (N − 5)/(N − 1); for 1/(N − 3) < q ≤ (N − 5)/(N − 1) it fails while
  (H_N) holds (α = 1/(q + 1)). Round 5's stage error λ³ env (λκ)² carried no ν and also exceeds |S_st| at ρ* (for
  exp(−1/x), N = 9, on x ∈ [λ^(5/12), λ^(1/3)]); by L.13 (c) it is λ³ env (|ν|(λκ)² + λ) (R6.1 (c)), so only the λ-term
  needs a hypothesis. Repaired: ρ0 = ρ* is admitted under (H_ρ*) [round 7: its second half is removed by Case 3′, R7.2]
  [round 8, m1: for N ≡ 0 mod 4 under (H_N+2), (H_t); and its first half too, under the same, Lemma L.28, R8.1] (κ x² ≥
  c_* near the edge, → ∞ if N ≡ 0 mod 4) and excluded otherwise (R6.1). The record's envelope (κ x² → 3/4) meets the
  first condition and not the second; P* (ρ0² = 6.25 against ρ*² = 3.2632…) is not affected.
- **V5-M2 (major).** Re-derived and confirmed. Round 5's "the degree-two terms are O(λ m0)" on J_n is asserted. L.17's
  C_2 ε_c(v)² is a past supremum, at least (h_n s_n^c B_c)² on J_n against m0 ≲ h_n²/s_n, a factor of about s_n^(2c+1)
  too large; L.17's hypothesis ε_M(v_1) ≤ λ⁵ fails there; with round 5's choice h_n ≥ λ⁴, L.15_P (b)'s λ sup_(v′≤v) |I_3|
  ≍ λ⁴ h_n can exceed m0 as well; T6 (round 5) bounded the first-degree tail only and did not see the zeros. Repaired by
  proof (R6.2) through another decomposition — at a zero of every env^(k) every term of g_λ⁻¹(dΦ0, dΦ0) other than −m0 is
  a mean of g_app or the remainder w — with h_n ∈ [λ^3.5, λ^3.1]; T6 rewritten.
- **V5-m1.** Confirmed. X11 now cuts the stage term off at λκ > 1 (L.22), and its control is the run with S_U removed,
  which leaves windows with one sign (the control fails, as it must).
- **V5-m2.** Confirmed (the sin¹⁶ mutant passed round 5's four points). X10 now samples 401 points of [10^(−3.5),
  10^(−2)] with exact derivatives (Bell polynomials in those of log env): (H_N) for k ≤ 13, L.16 (c)'s c_j for j ≤ 14
  (printed: 1.0), sup |κ_k′|/κ_k^(3/2) = 2.867 and 2.855 against the stated c_R = 3, and |κ_k − κ| ≤ 2.16 k κ^(1/2),
  resp. 2.30 k κ^(1/2), below the c_R 2^(1/2) k κ^(1/2) that (H_N) implies; the mutant is the control (detected). The
  docstring's unchecked sentence on x = 10^(−1.5) is removed.
- **V5-m3.** Confirmed: L.18, L_E's degree-two input since A23, needs (H_D), which L.16 (b), (c) do not give (they bound
  κ′ and the derivatives, not κ^c env along the descent). A25 adds (H_D) to L_E's statement.
- **V5-m4.** Confirmed for round 5 (its Case 3 needed κ^(α−1) ≪ T, i.e. (1 − α)(N − 2) > 1). Repaired by proof: R6.1's
  Case 3 compares T0 κ^(α−1) with T0, so α < 1 suffices; Theorem L_1E′ holds with α < 1, the paper's "(α < 1)" is then
  right, and Remark (3) holds for exp(−a/x^q) with every q > 0.
- **V5-m5.** Confirmed. P2⁗ (R6.5) restores the spheres'-horizon clause verbatim, "inside x_K ≤ 1" and "future".
- **V5-m6.** Confirmed: X7 computes reading 3 (ADM lapse and shift covector kept): K_R = (r0² − 2μ0)/(4 μ0^(3/4)
  r0^(1/2)), zero at ρ0² = 2. The supplement's convention is reading 2: its section 4, step (ii), "Z := d_tau - beta_ext
  (beta_ext the shift of g_ext)" makes the shift a vector field (N1STAR-PROOF.md line 461 at md5 fb2fbf06…; line 425 at
  709c63be…). Theorem L_1E′ is stated for reading 2, and reading 1 gives the same; its proof uses only Γ_R ≠ 0 and which
  N cancel, so under reading 3 it holds with ρ0² ≠ 2 excluded as well [round 7: irrelevant under the supplement's reading
  2, R7.3] (for ρ0² < 2, Γ_R < 0, the cancelling N are ≡ 2 mod
  4, and the quadrature part is the same). A30.
- **V5-m7.** Confirmed: L.17 (4) gives |U − U^(1)| ≤ C ε_c² only. R6.3 proves |∂_r^j (U − U^(1))| ≤ C λ^(N−2−j) ε_c², j ≤
  3, from the same three sources; A29.
- **V5-m8.** Confirmed. 𝒟 is taken over |β| ≤ 6 (R6.3, A28); for the amplitudes used only constants change.
- **V5-m9.** Confirmed (bandL4p5 H1's ledger stops at level 2). degtwo5 T7 runs the non-triangular ledger at levels 0-4
  with ε_6 ≤ λ⁵, L.17 (2)'s hypothesis: every coefficient bounded; control: at ε_6 ≤ λ⁴ one of level 4 is not.
- **V5-m10.** Confirmed. L.25 (b) is restated where it decides (L.25′ (b′), R6.2); "at every point, dips and zeros
  included" is withdrawn.
- **V5-m11.** Confirmed (K1, K2 pass Cd's power N + 5 and a dropped term of Ca). constL5 K4 holds the DAG against an
  independent step-by-step transcription of R5.5's display at 20 random points (largest relative difference
  8.5·10^(−35)); both mutations are its control and are detected. K1, K2 stand for what they state (the leaf set,
  monotonicity).
- **V5-n1.** X3's closed form is now checked against layerlin5's T_tab rows (vv, vr, rr); docstring corrected.
- **V5-n2.** δ = 1/2 is in H2's grid (least slack 0.4818 at K = 6, P = 50, so γ(1/2) = 1/10).
- **V5-n3.** A26: L.18's stage 0 reads |w| ≤ C λ^(N−5) ε_(M*) for L.4 (C λ^(N_P−3) ε_(M_P) for L.4_P), and δ_k's second
  term likewise; the descent is unchanged.
- **V5-n4.** m0 ≥ √(μ/μ0) − 1 ≥ (μ − μ0)/(3μ0) = (2A²/(27μ0)) ∫_(v_s)^v env² (μ′ = (2/9)A² env², μ − μ0 ≤ μ0 in the
  layer); "(2/27)" was the case μ0 = A = 1 (A34). T6 no longer uses d or ν; the bumps m > n enter ε_k as a factor 2; its
  unit constants are labelled.
- **V5-n5.** lamL5b rerun; M1 pins CONSTANTS5.md at its md5 at this run.
- **V5-n6.** Lemma W (B) is used by no proof, round 6's included (A35). It was tried for Case 3 and set aside: with
  L.22's derivative bound |∂_v E_S| ≤ C κ |E_S| the error's derivative is not below (B)'s L0 ≍ |ν| κ^α at the crossover
  (λ²κ^(3−α) and λκ^(2−α) both grow there for N = 12).
- **V5-n7.** A27: A22 also covers "Stage N's data are left free by the record (R3.4)" and "which the record leaves free
  (stage N)" (lines 1065, 1069 of the file as round 5 left it, md5 24e5c624…), and its quote "the supplement leaves stage
  N's data free" is at R3.0 item 5 (line 914), not R3.4.
- **V5-n8.** A33: R5.9's "md5 709c63be…" is N1STAR-PROOF.md at commit 1b38ece; the file is under live edits; at this
  round's reading its md5 is fb2fbf06….

### R6.1 Theorem L_1E repaired (V5-M1, R6-f1, V5-m4, V5-m6)

Write s := ∂_v + i/λ acting on amplitudes, (s⁻¹g)(v) := ∫_(v_s)^v e^(−i(v−v′)/λ) g(v′) dv′ (so that ∫_(v_s)^v e^(iv′/λ) g
dv′ = e^(iv/λ) s⁻¹g), T0 := λκ, T := λκ_(N−1), and ϵ′ := min{(λκ)² + λκ^α, κ^(α−1)}.

**(a) Lemma H_Σ, exact form (deduced, from its proof).** Under H_Σ's hypotheses, with 𝒟 over |β| ≤ 6, at P = (v, √μ0, ω):

    Ψ(P) = e^(iv/λ) s⁻¹[ G(√μ0 ← r0) y + ∫_(√μ0)^(r0) G(√μ0 ← r′) Â_f(·, r′) dr′ ](v) + O(𝒟(v)/|s̃(v)|),
    y := ½ (2 − F(r0)) Â_∂Ψ + ½ F(r0) s Â_Ψ,      r0 = v′ − τ0 inside s⁻¹.

*Proof.* Steps (1)-(5) stand. In step (6): on Σ_τ0, ∂_v|_r = ∂_τ and ∂_r|_v = ∂_r|_τ − ∂_τ, and Ψ_Σ = e^(i(τ0 + r)/λ)
Â_Ψ(τ0 + r), so LΨ = (1 − F/2) ∂_τΨ + (F/2) ∂_r|_τ Ψ = e^(iv/λ) y exactly; the main term ∫_(v_s)^v G(√μ0 ← r0(v′)) Y(v′,
r0(v′)) dv′ is e^(iv/λ) s⁻¹(G y) by definition, and the source's term is the second. ∎ Round 5's statement is this with
s⁻¹h replaced by h/s̃; that replacement, with s̃ built from 𝒟 rather than from h, is the only source of its factor 1 +
O(ϵ).

**(b) Lemma L.21 (iv′) (deduced; X13).** Let g > 0 on (v_s, v], flat at v_s, log-concave with κ_g := (log g)′ ∈ [κ/2,
2κ], |κ_g′| ≤ c_R κ_g^(1+α) (α < 1), and |g^(j)| ≤ c_j κ^j g (j ≤ 3). Then for every λ > 0

    s⁻¹g = g (κ_g + i/λ)⁻¹ (1 + ρ_g),      |ρ_g| ≤ C ϵ′   (C from c_R, α, c_j; flat-edge tails included).

For g = env^(N−1) these hypotheses are (H_N) of (d) below, and L.21 (iv) holds with 1 + O(ϵ + 1/|s̃| + λ) replaced by 1 +
O(ϵ′ + 1/κ + λ).

*Proof.* (i) λκ ≤ 1/4. Three integrations by parts (g and its derivatives vanish at v_s): s⁻¹g = −iλg + λ²g′ + iλ³g″ −
iλ³ s⁻¹g‴. As g″ = (κ_g² + κ_g′) g and g(κ_g + i/λ)⁻¹ = −iλg(1 − iλκ_g)⁻¹ = −iλg(1 + iλκ_g − λ²κ_g²) + O(λ⁴κ³g), the
difference is iλ³κ_g′ g − iλ³ s⁻¹g‴ + O(λ⁴κ³g). Near the edge (H_N) gives (κ(v′)/κ(v))^j g(v′)/g(v) = exp(−∫_(v′)^v (κ_g
− j|κ′|/κ)) ≤ e^(−κ(v)(v−v′)/4) once 2j c_R (2κ)^(α−1) ≤ 1 [round 7, V6-n1: with κ_g's own derivative, once 2^(2−α) j c_R
κ^(α−1) ≤ 1] (κ decreases, κ_g ≥ κ/2), so |s⁻¹g‴| ≤ c_3 ∫_(v_s)^v κ³ g ≤ 4
c_3 κ² g, and |ρ_g| ≤ C(λ²κ^(1+α) + (λκ)²) ≤ C((λκ)² + λκ^α). (ii) Every λ. Put e^(−ψ(u)) := g(v − u) e^(κ_g u)/g(v)
(zero for u ≥ x) and s̃_g := κ_g + i/λ; then g⁻¹ s⁻¹g − s̃_g⁻¹ = ∫_0^∞ e^(−s̃_g u)(e^(−ψ) − 1) du, and one integration by
parts (ψ(0) = 0) gives ρ_g = −∫_0^∞ e^(−s̃_g u) ψ′ e^(−ψ) du, so |ρ_g| ≤ ∫_0^x ψ′(u) g(v − u)/g(v) du ≤ ∫_0^∞ ψ′(u)
e^(−κ_g u) du; with ψ′(u) = κ_g(v − u) − κ_g(v) ≤ 2^(1+α) c_R κ_g^(1+α) u for u ≤ U_* (L.16 (b)'s U_*, for g), |ρ_g| ≤
2^(1+α) c_R κ_g^(α−1) plus the part beyond U_*, smaller than every power of 1/κ at a flat edge (as in L.16 (b)). For λκ ≤
1/4 take the smaller of (i) and (ii); for λκ > 1/4, (λκ)² > κ^(α−1) near the edge, and ϵ′ = κ^(α−1). For g = env^(N−1):
log-concavity, κ_(N−1)/κ ∈ [1/2, 2] and the c_R bound are (H_N); |g^(j)| = |env^(N−1+j)| ≤ c_(N−1+j) κ^(N−1+j) env ≤ c
2^(N−1) κ^j g, since env ≤ 2^(N−1) κ^(−(N−1)) env^(N−1) (env^(N−1)/env = Π_(k<N−1) κ_k, κ_k ≥ κ/2), so L.16 (c)'s first
bound to j = N + 2 is used. In (iv)'s proof the only ϵ is "s⁻¹ env^(N−1) = env^(N−1)/(κ_(N−1) + i/λ)(1 + O(ϵ))"; the
smooth coefficients α⁻¹ r^(−7/2) and c_N commute with s⁻¹ up to O(λ) relative (one integration by parts). ∎

**(c) Lemma L.21 (v′) and Proposition L.22′ (deduced; X7, L.13 (c)).** L.21 (v) holds as stated, with no ϵ: in (a)'s form
the data of a := a^(1) give y = s(Φa) + Φ_0 a, where Φ comes from X7's solve, in which s is a symbol and the coefficients
are free of it, and Φ_0 from D's terms without derivatives; then s⁻¹(Gy) = GΦa − s⁻¹((GΦ)′a − GΦ_0 a) [round 7, V6-n2:
GΦa − s⁻¹(G′Φa − GΦ_0 a)], the horizon
combination of GΦa is K_R a (X7: free of s and of the free datum ∂_τγ_rr), and the rest is O(λ|a|) (|s⁻¹h| ≤ λ|h| + λ ∫
|h′| ≤ Cλ|h| for h a smooth multiple of a, since ∫_(v_s)^v κ_(N−1) env^(N−1) = env^(N−1)(v)). With (b), L.22 holds with

    |E_S| ≤ C [λ³ env (|ν| (λκ)² + λ) 𝟙_(λκ≤1) + λ^(N+1) κ^(N−2) env 𝟙_(λκ>1) + (ϵ′ + 1/κ + λ) |S_U|],

and its derivative bounds as stated. The stage part: by L.13 (c), Σ_j λ^j H_j,vv = λ³ A d ν Σ_(k≤N−2) (k + 1)(iλ)^k
env^(k) + Σ_(j≥4) λ^j Σ_(k≤j−4) (…) env^(k); for λκ ≤ 1 the first is λ³ A d ν env (1 + 2iλκ) + O(|ν| λ³ (λκ)² env)
(|env^(k)| ≤ 2^k κ^k env, (H_N); the sum is finite) and the second O(λ⁴ env). ∎

**(d) Theorem L_1E′ (Theorem 1's deep layer and very edge; deduced from L.17, L.18, H_Σ (a), L.21 (iv′), (v′), L.22′ and
Lemma W (A), with edge1_5 X1-X13 and degtwo5 T1-T4).** Let μ0 = √72 l5², K ≥ 6, N = K + 3, g_λ Theorem 1's metric with
stage N's data by Lemma 6.2's rule (D615, D616) and section 6.4's "lapse and shift" read as the supplement reads the
shift (reading 2; reading 1 gives the same), and env satisfying on (v_s, v_s + x0]:

    (H_N)   env^(k), k ≤ N, positive and log-concave, κ_k/κ ∈ [1/2, 2], |κ_k′| ≤ c_R κ_k^(1+α) for an α < 1,
            and |env^(j)| ≤ c_j κ^j env for j ≤ N + 2;
    (H_D)   as in Lemma L.18.

Let τ0 be admissible, ρ0 := (v_s − τ0)/√μ0, with ρ0² ≠ N − 1, ρ0² ≠ 2N − 1 if N ≡ 0 mod 4 [round 7: superseded by Theorem
L_1E″, R7.3], and, if ρ0 = ρ*,

    (H_ρ*)  κ(v)(v − v_s)² ≥ c_* > 0 on (v_s, v_s + x0], and κ(v)(v − v_s)² → ∞ as v ↓ v_s if N ≡ 0 mod 4.

Then Theorem L_1E's conclusion holds, with λ_1E, x0′, P1 depending also on α, c_* and the distances of ρ0² from N − 1 and
(if N ≡ 0 mod 4) 2N − 1, and of ρ0 from ρ* if ρ0 ≠ ρ*.

*Proof.* As round 5's: Lemma L.1, the non-harmonic part ε ≤ C κ^(2c′) env² (L.17, L.18), J := [v, v + 4πλ], ω fixed. Put
σ := S/(λ³ A d env), Λ := λ^(N−2) env^(N−1)/env, X := Γ_R c_N Λ/|ν|, and ê := E_S/(λ³ A d env), so σ = ν(1 +
2iT0)𝟙_(T0≤1) − Γ_R i^N Ξ Λ + ê and, by L.22′, |ê| ≤ C[(|ν|T0² + λ)𝟙_(T0≤1) + Λ/κ 𝟙_(T0>1) + (ϵ′ + 1/κ + λ) Γ_R |Ξ| Λ].
Two facts: T = T0(1 + O(κ^(α−1))), since κ_(N−1) − κ = Σ_(k<N−1) κ_k′/κ_k and each term is at most c_R 2^α κ^α by (H_N);
and Λ = Π_(k<N−1) (λκ_k) /λ ≍ T0^(N−2) κ up to 2^(±(N−1)). Fix M ≥ 8, large against the constants. Case 1: Γ_R|Ξ|Λ ≥ M
|ν| |1 + 2iT0|, or T0 > 1. Case 2: Γ_R|Ξ|Λ ≤ |ν|/M. Case 3: otherwise.

*Case 1.* |σ| ≥ (1 − 1/M) Γ_R|Ξ|Λ − |ê| ≥ Γ_R|Ξ|Λ/2 for λ and x0′ small: ϵ′ + 1/κ + λ → 0 (ϵ′ ≤ κ^(α−1) for every λ:
R6-f1's repair), |ν|T0² ≤ |ν| ≤ Γ_R|Ξ|Λ/M, and λ ≪ Λ — off ρ*, Λ ≥ M ν_*/(Γ_R|Ξ|) with ν_* := inf |ν| > 0; at ρ*, if x² <
Mλ then κ ≥ c_*/(Mλ), T0 ≥ c_*/M and Λ ≍ T0^(N−2) κ ≫ λ, and if x² ≥ Mλ then Λ ≥ c M x² ≥ c M² λ (Λ ≥ M|ν|/(Γ_R|Ξ|), |ν|
≥ c_ν x²/2). The phase: arg(Γ_R i^N Ξ Λ) moves over J by O(κ^(α−1) + λ^(1−α)) (round 5), the rest by at most 2
arcsin(2/M) + o(1) ≤ π/6. Lemma W (A), with ε ≤ m/4 once env ≤ λ^(P1) (round
5). [round 7, V6-m2: pointwise, Lemma W (A′)]

*Case 2.* Λ ≍ T0^(N−2) κ ≲ |ν| ≤ C with κ → ∞, so T0 → 0. |σ| ≥ |ν|(1 − 1/M) − |ê| ≥ |ν|/2, since λ ≪ |ν|: off ρ*
trivially; at ρ*, x² ≥ Mλ (otherwise, as in Case 1, Λ ≫ λ ≳ x²/M ≳ |ν|/M, against Case 2). The phase: arg σ stays within
2 arcsin(2/M) + o(1) of arg(ν(1 + 2iT0)), which moves by O(λ²|κ′|) = O(λ^(1−α)) over J. Lemma W (A).

*Case 3.* Here κ ≍ (|ν| λ^(−(N−2)))^(1/(N−1)) and T0 → 0; λκ² → ∞ (off ρ*: λκ² ≍ λ^(−(N−3)/(N−1)); at ρ*: T0^(N−2) κ ≍
|ν| ≳ x² ≳ c_*/κ gives T0 κ ≳ κ^(1−2/(N−2)) → ∞). With −Ξ = c_N + iT + O(T²):

    σ_main := ν(1 + 2iT0) + Γ_R i^N (c_N + iT) Λ,      σ = σ_main + O(|ν| T0²) + ê.

(i) N ≢ 0 mod 4. N odd: Re σ_main = ν(1 + O(T0)); N ≡ 2 mod 4: Re σ_main = ν − Γ_R c_N Λ, of modulus ≥ |ν|. So |σ_main| ≥
|ν|/2, and |ê| ≤ C|ν|(T0² + λ/|ν| + M(ϵ′ + 1/κ + λ)) ≪ |ν| (at ρ*, λ ≪ |ν| as in Case 2). (ii) N ≡ 0 mod 4: Re σ_main =
|ν|(X − 1), Im σ_main = 2νT0 + Γ_R T Λ = |ν| T0 (X/c_N − 2) + O(|ν| T0 κ^(α−1)). Put η := |1 − 2c_N|/4 > 0 (ρ0² ≠ 2N −
1). If |X − 1| ≥ η, |σ_main| ≥ |ν|η/2; if |X − 1| < η, |X/c_N − 2| ≥ |1/c_N − 2| − η/c_N = (3/4)|1 − 2c_N|/c_N, so |Im
σ_main| ≥ |ν| T0 |1 − 2c_N|/(2c_N). Either way |σ_main| ≥ c₃ |ν| T0, c₃ := min(η/2, |1 − 2c_N|/(2c_N)). And |ê| +
O(|ν|T0²) ≤ C|ν|[T0² + λ/|ν| + M(T0² + T0 κ^(α−1) + 1/κ + λ)] ≤ c₃|ν|T0/2 for λ small: T0² ≪ T0; λκ^α = T0 κ^(α−1) ≪ T0
for every α < 1 (all that Case 3 uses: V5-m4); 1/κ ≪ T0 as λκ² → ∞; λ ≪ T0; and λ/|ν| ≪ T0, i.e. |ν|κ → ∞: off ρ* as |ν|
≥ ν_*, at ρ* by (H_ρ*) (|ν|κ ≥ (c_ν/2) x²κ → ∞). The phase: over J, Re σ_main moves by O(|ν| λ (κ^α + |ν′/ν|)) (Λ′/Λ =
κ_(N−1) − κ = O(κ^α); |ν′/ν| = O(1) off ρ*, O(1/x) at ρ*), Im σ_main by O(|ν| λ²κ^(1+α)), and ê by O(λκ)|ê| (|∂_v E_S| ≤
Cκ(…)); against |σ| ≥ c₃|ν|T0/2 = c₃|ν|λκ/2 these are O(κ^(α−1) + 1/(κx) + λκ^α) → 0 (κx ≥ c_*/x at ρ*). Lemma W (A) with
m := c₃|ν|T0 λ³ A |d| env/2: ε ≤ C κ^(2c′) env² ≤ m/4 once env ≤ λ^(P1) (κ ≤ 1/λ here, and |ν| ≥ c_ν c_*/(2κ) at ρ*). ∎

X12 measures Case 3's inequality at a real cancellation with unit constants (N = 12, c_N = 6/5, ν = −1/9, Γ_R = 1, exact
derivatives of exp(−1/x) and of the record's envelope): over the whole crossover |S_U|/|S_st| ∈ [1/4, 4] the least ratio
of |σ_main| to the bound above is 5.76, 47.6, 3.1·10^3, 1.36·10^7 [round 7, V6-n13: with the stage λ-term carrying no
|ν|, the numbers of R7.0] at λ = 10^(−10), 10^(−20), 10^(−40), 10^(−80) (both
envelopes), and arg σ_main moves by at most 0.009 over 4πλ; to round 5's bound the ratio stays at 1.04-1.17 (the
control). X13 checks (b) for g = env^(11) of exp(−1/x) by quadrature: |ρ_g|/(λκ)² ≤ 0.048 [round 7, V6-m4: an unconverged
quadrature; converged ≤ 0.012, R7.1] at λ = 10^(−6), 10^(−7), λκ =
1/5, …, 1/40 (control: dropping the first-order term breaks the bound).

*Remarks.* (1) The excluded or conditioned τ0 [round 7, V6-m1: ρ0² = N − 1 and 2N − 1 are admitted, and at ρ* only
(H_ρ*)'s first half is needed, R7.3] [round 8, m1: 2N − 1, and ρ* for N ≡ 0 mod 4, under (H_N+2) and (H_t); at ρ* not
even the first half, under the same, Lemma L.28]: ρ0² = N − 1 (|S_U| falls to E_S's size on the deep very edge), ρ0² = 2N
− 1 when N ≡ 0 mod 4 (no quadrature part at a real cancellation; for N ≢ 0 mod 4 nothing cancels and 2N − 1 is admitted),
ρ0 = ρ* without (H_ρ*); under reading 3 also ρ0² = 2 [round 7: irrelevant under reading 2]. (2) For exp(−a/x^q) edges
(H_N), (H_D) hold for every q > 0 (α = 1/(q + 1)) and (H_ρ*) for q ≥ 1, its second half for q > 1 [round 7: the second
half is no longer used]; for the record's envelope (H_N) and L.16 (c) are sampled (X10, k ≤ 13, j ≤ 14) and (H_D) in T4;
[round 8: (H_N), L.16 (c), (H_D), (H_N+2), (H_t) proved for it, every K, Proposition L.27, R8.2] it meets (H_ρ*)'s first
half (κx² → 3/4), not its second. (3) Lemma W (B) is not used. (4) The levels between λ^P and the very edge at fixed λ
(R5.4) are covered as there, with L_1E′.

### R6.2 Proposition L.25 repaired (V5-M2, V5-m10)

**Proposition L.25′ (dips; deduced, with degtwo5 T6).** (a) *False in general.* Let env := Σ_(n≥n0) h_n β(s_n(v − v_s −
2^(−n))) near v_s, h_n := e^(−n²), s_n := 2^(n+2), β(t) := e^(−1/(1−t²)) on (−1, 1), continued to a C_c^∞ envelope (flat
at v_s: h_n s_n^k → 0 for every k). Bump n lives on v − v_s ∈ [3/4, 5/4]·2^(−n), so env = 0 on J_n := v_s + (5/4,
3/2)·2^(−n). There is λ_25 > 0 such that for λ ≤ λ_25, with n the least index with h_n ≤ λ^3.1 (then h_n ≥ λ^3.5) [round
7, V6-n4: for λ ≤ 10^(−31.7) only; V6-m3: R7.4 takes 0 < δ ≤ 1/2], at
every ω and every v ∈ J_n′ := v_s + [(5/4)2^(−n), (3/2)2^(−n) − ρ_w], ρ_w = O(λ) the reach of L.4′ (resp. L.4_P),

    g_λ⁻¹(dΦ0, dΦ0)(v, r_q(v), ω) ≤ −m0(v)/2 < 0,

for Theorem 1's g_λ (K ≥ 6) and for Theorem 2's. J_n′ lies in the layer below λ^(3+δ) for δ ≤ 1/10 [round 7, V6-m3: every
δ ≤ 1/2 in R7.4] (sup_(v′≤v) env =
h_n/e ≤ λ^3.1) and is longer than 2^(−n−3) ≫ 4πλ: so "every interval of length 4πλ in the layer below λ^(3+δ) has
timelike points" is false for this envelope, for every λ ≤ λ_25.

*Proof.* Fix v ∈ J_n′, ω, and X := (v, r_q(v), ω). (1) *The oscillating profiles vanish at X.* W, χ, gh_m and the phase
terms solve, at fixed v, transports along ℓ whose sources and data at that v are polynomials in env^(k)(v) and in the
oscillating profiles at that v, every monomial with an oscillating factor (a monomial of means, phases and μ-terms alone
has no θ-dependence and enters only the mean equations; Lemma 6.2's data are proportional to env and its derivatives at
that v): the argument of the supplement's Proposition 8.2 (N1STAR-PROOF.md section 8) for v outside the shell, applied at
a v with env^(k)(v) = 0 for every k. By induction on the order they vanish at X. So on J_n′, g_λ − g0 = Σ_(j≥1) λ^j m_j +
w. (2) *Bounds.* ε_k(v_1) ≤ 2 h_n s_n^k B_k, B_k := max_(i≤k) sup |β^(i)|, v_1 := v + ρ_w (bump n − 1 starts at
(3/2)2^(−n), beyond v_1; the bumps m > n add at most h_n s_n^k, as h_(m+1) s_(m+1)^k ≤ h_m s_m^k/2 once e^(2m+1) ≥
2^(k+1)). L.3 (b) (L.3_P on Ω for Theorem 2): |m_j| ≤ C ε_(2j)(v)². L.4′ (Theorem 1): |w| ≤ C λ^(N−5) ε_(M*)(v_1) given
ε_4(v_1) ≤ λ; L.4_P (Theorem 2): |w| ≤ C λ^(N_P−3) ε_(M_P)(v_1) given ε_(M_P)(v_1) ≤ λ³. Both hypotheses hold for λ
small, since h_n ≤ λ^3.1 and s_n^k B_k = e^(O(√(log 1/λ))). (3) *The margin.* m0 ≥ (2A²/(27μ0)) ∫_(v_s)^v env² ≥
(2A²/(27μ0)) h_n² s_n⁻¹ ∫β² (A34). (4) Lemma L.1 with k := g_λ − g0 gives |g_λ⁻¹(dΦ0, dΦ0) + m0| ≤ C|k| ≤ C′(λ ε_(2N)(v)²
+ λ^(N−5) ε_(M*)(v_1)) (Theorem 1; N_P, M_P for Theorem 2), whose ratio to (3)'s bound is at most C″(λ s_n^(4N+1) B_(2N)²
[round 7, V6-n5: the means' term j-resolved, max_j λ^j s_n^(4j+1) B_(2j)², as T6 computes]
+ λ^(N−5) h_n⁻¹ s_n^(M*+1) B_(M*)) ≤ C″(λ s_n^(4N+1) B_(2N)² + λ^(N−8.5) s_n^(M*+1) B_(M*)) (h_n ≥ λ^3.5), which tends to
0 since N ≥ 9 and s_n = 2^(n+2), n ≤ (3.5 log(1/λ))^(1/2) + 1, grows slower than every power of 1/λ; for Theorem 2 the
same with λ^(N_P−6.5). So for λ ≤ λ_25 the ratio is at most 1/2. ∎

Round 5's proof of (a) is withdrawn: its first-degree estimates are not needed (the first-degree memory is part of w),
and its degree-two sentence was unproved. T6 computes (2)-(4) in log10 with unit constants (A = μ0 = 1, the record's
constants 1): Theorem 1's ratio is +221 at λ = 10^(−100) and −86 at 10^(−1000), Theorem 2's −621 and −1.05·10^4, the
means' −52 and −865; all fall strictly to below −8·10^5 at 10^(−10^6); L.4′'s hypothesis holds on the whole grid, L.4_P's
only at 10^(−10^6) (it needs λ^0.1 s_n^44 B_44 ≤ 1). λ_25 is far below the paper's thresholds; the statement is "for
every small λ" and no more. Control: the zero intervals removed (an extra bump [round 7, V6-m5: and round 5's bump choice
h_n ≈ λ⁴] on J_n) is detected.

(b′) *The criterion, where it decides.* At a boundary point in the deep layer, g_λ⁻¹(dΦ0, dΦ0) = −m0 − Re[S e^(iv/λ)] + ρ
with S the exact first-degree amplitude (Theorem 2: S = λ A ν∞ d I_2 + O(λ sup_(v′≤v) |I_3|), every envelope, L.15_P (b);
Theorem 1: L.22′'s S where (H_N) holds on [v − 1/κ,
v] [round 7, V6-m6: L.22′ needs (H_N) on all of (v_s, v_s + x0]; R7.4]) and |ρ| ≤ D(v), the degree-two bound available at
v: L.18's C
κ^(2c′) env² where L.18's hypotheses hold, (a)'s on a zero interval as in (a) [round 7, V6-m6: there S := 0 and D is
(a)'s bound; in the band S is L.12 (iii)'s; R7.4], L.17's otherwise. Every interval [v, v +
4πλ] with S slowly varying on it has timelike points at ω if max_J (|S| − m0) ≥ C(λ^γ m0 + D) and none if max_J (|S| + D)
< min_J m0. So the ratio |S|/m0 decides, up to the factor 1 ± 2λ^γ, where D ≤ λ^γ m0 — in the band λ^(3+δ) ≤ E ≤ λ^(3−δ)
(L.12 (iii)) and on zero intervals as in (a) — and the sign is timelike where |S| exceeds m0 + D by such a margin (the
very edge of L_E, L_1E′); at a dip where env > 0 and D exceeds m0 it decides nothing. A transversal crossing of the ratio
through 1 in the band is a single switch (L.24's proof). (c) stands, with L_1E′.

### R6.3 The smaller repairs proved, and the amendments

**(m7) U − U^(1) (deduced).** On Σ_τ0 ∩ {τ0 + r ≤ v}, |∂_r^j (U − U^(1))| ≤ C λ^(N−2−j) ε_c(v)², j ≤ 3. *Proof.* U −
U^(1) solves Lemma 6.4's system with source −(Φ − Φ^(1)) − Nl(U) − (L_app − L)U (L.17 (4)). (i) Φ(γ, K) vanishes below
order N − 2 in its profiles (Lemma 6.1, READ; L.3 (e)); its part of degree ≥ 2 has every monomial with two factors of
degree one or one of degree two (L.3 (b), (c)), each radial derivative costing λ⁻¹ (through the phase on Σ_τ0): ‖∂_r^j (Φ
− Φ^(1))‖ ≤ C λ^(N−2−j) ε_c². (ii) Nl(U) ≤ C λ⁻¹ |U|²_(C¹) with |∂_r^j U| ≤ C λ^(N−2−j) ε (L.3 (e)): at most C λ^(2N−7−j)
ε², below λ^(N−2−j) ε² for N ≥ 5. (iii) L_app − L, the coefficients at the approximant's data minus g0's, is of degree
one, with ∂_r^j at most C λ^(−j) ε; times U: C λ^(N−2−j) ε². Lemma 6.4 on [a, r] (R2.3 (e)), with a constant independent
of λ, and the derivative count of L.3 (e) give the bound. ∎ So L.24's ρ_r ≤ C λ^(N−6) ε_c(v_1)² stands with this input
(A29).

**(m8) H_Σ's angular count (deduced).** Step (4) bounds Ω^β e, |β| ≤ 2, pointwise through L.10 (H²(S³) ⊂ L^∞), which uses
the energies of Ω^β e for |β| ≤ 4; their sources are Ω^β of the parametrix residuals e^(iv/λ) Q̃(…), with Q̃ of second
order in the angles: |β| ≤ 6 on the amplitudes. The amplitudes of L.21-L.22 are smooth T² × Z2 × Z2-invariant multiples
of d(θ), τ(θ), so only constants change (A28).

*Amendments* (each re-derived above; the sites carry bracketed notes):

- **A25** (V5-m3). Theorem L_E: "env satisfying Lemma L.16's hypotheses (b), (c)" reads "… (b), (c) and (H_D) of Lemma
  L.18".
- **A26** (V5-n3). Lemma L.18 (2), (3): stage 0 is |w| ≤ C λ^(N_P−3) ε_(M_P)(·) for L.4_P and C λ^(N−5) ε_(M*)(·) for
  L.4, and δ_k's second term carries the same power.
- **A27** (V5-n7). A22 extends to the two sentences of R3 named in R6.0 (V5-n7), and its quote is at R3.0 item 5.
- **A28** (V5-m8). Lemma H_Σ: 𝒟 is the supremum over Ω^β, |β| ≤ 6.
- **A29** (V5-m7). L.24's proof: "U − U^(1), L.17 (4)" reads "U − U^(1), at most C λ^(N−2−j) ε_c² with j derivatives
  (R6.3)".
- **A30** (V5-m6). R5.0 item 1 and L.21 (v): "the two readings" reads "readings 1 and 2 (reading 2 the supplement's)";
  reading 3 is as in R6.0.
- **A31** (V5-M1, V5-m4, R6-f1). R5.3 (f) is superseded by Theorem L_1E′; L.22's α < 1 − 1/(N − 2) reads α < 1, its E_S
  bound is L.22′'s, and R5.3's citations of L_1E read L_1E′.
- **A32** (V5-M2, V5-m10). R5.4's Proposition L.25 is superseded by L.25′.
- **A33** (V5-n8). R5.9's md5 709c63be… is N1STAR-PROOF.md at commit 1b38ece.
- **A34** (V5-n4). m0 ≥ (2A²/(27μ0)) ∫ env²; "(2/27)" is the case μ0 = A = 1.
- **A35** (V5-n6). Lemma W (B) is used by no proof.

### R6.4 Programs (round 6)

- `checks/edge1_5.py`: X3 against T_tab (n1); X7 with reading 3 and s as a symbol (m6, R6.1 (c)); X10 dense (m2); X11
  with L.22's cutoff, control S_U removed (m1); X12 Case 3 at a real cancellation (M1 (a)); X13 L.21 (iv′) by quadrature.
  Full run with `.out`.
- `checks/degtwo5.py`: T6 rewritten (M2: L.25′ (a)); T7 the ledger at levels 0-4 (m9). Full run with `.out`.
- `checks/constL5.py`: K4, the formulas against an independent transcription, with two mutations as control (m11). Full
  run with `.out`.
- `checks/bandL4p5.py`: δ = 1/2 in H2's grid (n2); `checks/lamL5b.py` rerun (n5). Each with its `.out`.

*Labels.* Computed, exact (sympy or exact rationals): X1-X8, T1-T3, T7, K1, K2; computed, sampled or bounds (mpmath): X9,
X10, X13, T4, T6, K3, K4; models with unit constants: X11, X12, T5. [round 7, V6-n12: and T6] Deduced: Lemma H_Σ (a),
Lemma L.21 (iv′), (v′),
Proposition L.22′, Theorem L_1E′, Proposition L.25′, R6.3's two lemmas; READ: as in R6.6.

### R6.5 Proposed paper text (replaces R5.8's P1‴ and P2‴; P3-P6 stand, P3's list extended)

(P1⁗) Proposition 3.2: P1‴ with "L_1E" read "L_1E′" (the verifier of round 5 confirmed that it claims nothing beyond
Theorem L and Corollary L.7; the hypotheses of L_E and L_1E′ do not enter it). The old text, lines 302-305 of
RESPONSE-HL-5D.md at md5 7193c56e…, from "If μ0 = √72 l5² exactly, the" to "(supplement `docket68/n1star/EQUALITY5.md`,
Propositions E.2-E.4).", occurs once; it is replaced by:

> If μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the shell
> starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
> `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that layer, for λ small, every column has points
> where it is timelike for g_λ, so the no-return property stated above for μ0 > √72 l5² fails at equality
> (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L, L_P, L_E and L_1E′, Corollary L.7).

(P2⁗) Section 9: the bullet [round 7: P1⁗ and P2⁗ are superseded by R7.6] "**The boundary at equality.**", lines
1533-1541 at md5 7193c56e…, occurs once; it is
replaced by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced in `docket68/n1star/EQUALITY5.md` and `EQUALITY5-LAYER.md`
>   [†], computed by the programs of Appendix A), x_K = 1 is the seed's horizon on {v ≤ v_s}, v_s := inf supp env, and is
>   spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η. In the layer between, for λ small and 0 < δ ≤ 1/2, it is spacelike
>   where sup_(v'≤v) env ≥ λ^(3−δ), and where λ^(3+δ) ≤ sup env ≤ λ^(3−δ) its character is that of the ratio of λ³ A env
>   |ν| |d| to the margin, up to a factor 1 ± 2λ^(1/10) (d the double divergence of the waves' angular tensor, |d| ≥ 8/3;
>   ν ≤ 0 a coefficient of the seed and τ0, with a double root at (v_s − τ0)/√μ0 = ρ* = 1.806…). Suppose that near v_s
>   env and its first K + 3 derivatives are positive and log-concave, with logarithmic derivatives κ_k within a factor 2
>   of κ := (log env)′ and |κ_k′| ≤ c κ_k^(1+α) for an α < 1, and that env obeys the derivative and decay bounds of
>   `EQUALITY5-LAYER.md` R5.2 and R6.1 (checked by sampling for the C_c^∞ envelope used for the constants); for Theorem
>   1's solution suppose also (v_s − τ0)²/μ0 ∉ {K + 2, 2K + 5, ρ*²}. Then that ratio crosses 1 once per column, and below
>   λ^(3+δ), down to v_s, every interval of length 4πλ has timelike and spacelike points on every column; the term linear
>   in the waves is computed there to leading order, for Theorem 1 carried by the constraint correction at first degree.
>   With flat interior zeros accumulating at the edge, some such intervals are spacelike throughout, for every small λ.
>   So timelike curves of g_λ cross x_K = 1 into D_T. A domain O(λ)-close to D_T, inside x_K ≤ 1, has an inner boundary
>   that no future causal curve enters, and the spheres' horizon holds in the form: at most one zero per column, within C
>   λ of √μ(v); exactly one on the columns with v ≤ v_s and on those that reach across √μ(v) + C λ with √μ(v) − r_q(v) ≥
>   C' λ. λ_L is an explicit formula in the leaves of λ0, two constants of the seed and Theorem 1's C1, and the threshold
>   this proof delivers is below 3·10^(−12).

[†] "(rounds 1-5 read by independent verifiers; round 6 not yet read)". Each claim's source: the layer and band, L.12
(i), (iii) (A24); the single crossing, L.24; the intervals below λ^(3+δ), L.12 (ii) with L_E (Theorem 2; A25) and L_1E′
(Theorem 1; R6.1), every interval since env increases at its edge under these hypotheses; the linear term, L.15_P (b) and
L.22′; the zeros, L.25′ (a); the crossing curves, Corollary L.7; the inner boundary and the spheres' horizon,
EQUALITY5.md Propositions E.4, E.5; λ_L, R5.5, R5.6. ρ*² is excluded for Theorem 1 although L_1E′ admits it under (H_ρ*);
the paper states the simpler, weaker claim. (P3⁗) Appendix A, C, D: `checks/edge1_5.py` X1-X13, `checks/degtwo5.py` T1-T7
and `checks/constL5.py` K1-K4 beside round 4's entries, with the run times of their `.out` files and their controls as in
their docstrings; P5's commands for bandL4p5 and lamL5b stand, with their new md5s.

### R6.6 Open items, labels and sources

None in section 9's sense: [round 7: the exclusions listed here are removed or narrowed in R7.3] every claim of P1⁗ and
P2⁗ is proved in the record on hypotheses the text states. What those
hypotheses leave out is stated with them: Theorem 1's very edge at ρ0 = ρ* without (H_ρ*) (for N ≡ 0 mod 4 this includes
the record's envelope) and at ρ0² = N − 1, or 2N − 1 with N ≡ 0 mod 4; envelopes with dips, beyond (b′). O2: round 6
awaits an independent reader.

READ: the verifier of round 5's report (as relayed); N1STAR-PROOF.md at md5 fb2fbf06… (section 4 step (ii), line 461;
section 6.2's (F1), (F2) and Lemma 6.1; section 8, Proposition 8.2's proof); RESPONSE-HL-5D.md at md5 7193c56e… (lines
302-305 and 1533-1541). Files (round 6): this section and its bracketed notes; `checks/edge1_5.py`, `checks/degtwo5.py`,
`checks/constL5.py`, `checks/bandL4p5.py`, `checks/lamL5b.py`, each with its `.out`.

## Round 7 (2026-11-06)

This round seats the verifier of round 6 (no major finding), each finding re-derived first (R7.0), and removes the
exclusions of Theorem 1's very edge that were limits of the method: ρ0² = N − 1 (R7.1 (c)), ρ0² = 2N − 1 with N ≡ 0 mod 4
and the second half of (H_ρ*) (R7.2, a new argument that decides every crossover window by Lemma W (A′) or (B)), [round
8, m1: for N ≡ 0 mod 4 under (H_N+2) and (H_t), proved for the record's envelope in R8.2] and reading 3's ρ0² = 2 (R7.3).
One case is not removed: ρ0 = ρ* on an edge with liminf κ(v − v_s)² = 0, where the method provably fails without the
coefficients of the stage family below the top, which are not computed; [round 8, nit 11: "cannot decide for some
admissible b̂4, b̂5"; the coefficients are computed and the case removed, R8.1] R7.3 proves the failure and names the
coefficients. Proposition L.25′ is extended to every δ ≤ 1/2 (R7.4). Earlier text stands, with bracketed notes "[round 7,
…]" at every amended site.

### R7.0 The verifier of round 6, seated (each finding re-derived)

Verdicts READ from the report (as relayed) and confirmed here: H_Σ's exact form, L.21 (iv′) in both regimes (|ρ_g| ≤
2.006 ϵ′ by an independent quadrature; this round's X13: 2.001), (v′), L.22′, Theorem L_1E′ with α < 1, Proposition L.25′
for λ ≤ λ_25, the seating of round 5, and the two old paper texts each once in RESPONSE-HL-5D.md (md5 7193c56e…;
at this round's last reading 5930486d…, the two texts unchanged and at the same lines); [round 8, M1: false for P2: at
5930486d… its bullet is at lines 1547-1555 (moved at commit 8a1f050), and lines 1533-1541 are the middle of the two-dust
bullet; R8.0, R8.5] 33 of 33 checks pass and 33 controls fail.

- **V6-m1.** Re-derived and confirmed: L_1E′ never uses ρ0² ≠ N − 1. At c_N = 1, Ξ = −i/(T + i) and |Ξ| = (1 + T²)^(−1/2)
  → 0 on the deep very edge, but every error of L.21 (iii)-(iv) is relative to the bracket, not to env^(N−1): the top
  family's two terms cancel exactly to −(i/λ) s⁻¹ env^(N−1) (X4, X5, exact), the next family is s⁻¹(O(env^(N−1)) + O(s
  env^(N−2))), which is O(λ + 1/κ) times the bracket at every T (X16: at most 2.0·(λ + 1/κ) for λκ ∈ [10^(−2), 10^4];
  control: a lower term with one s too many is not), the c_N′ commutator is O(λ²) relative, [round 8, nit 4: O(λ), inside
  O(λ + 1/κ)] and the solve's corrections are relative. On the deep very edge the only non-relative term is the stage's
  Λ/κ, and Γ_R|Ξ|Λ/(Λ/κ) ≥ Γ_R κ (1 + T²)^(−1/2) ≥ Γ_R/(2√2 λ) for T ≥ 1. Case 1 uses Γ_R|Ξ|Λ, not c0, and in Case 3 |Ξ|
  = 1 + O(T). Repaired: ρ0² = N − 1 is admitted (R7.1 (c), Theorem L_1E″); round 5's and round 6's reason ("|S_U| falls
  to E_S's size") is withdrawn (A36); K + 2 leaves the paper's set.
- **V6-m2.** Confirmed (on the deep very edge env varies across J by up to e^(4πλκ)). Lemma W (A) is restated pointwise,
  (A′) in R7.1 (a); its proof was already pointwise; X9 adds 1000 amplitudes growing by up to e^50 across the window
  (control: |ε| = |S| leaves one sign). A37.
- **V6-m3.** Confirmed: L.25′ (a) was proved for δ ≤ 1/10 only, and P2⁗'s sentence claimed more. Repaired by proof for
  every 0 < δ ≤ 1/2 by the verifier's route (R7.4: n least with h_n ≤ λ^(3+δ), then h_n ≥ λ^(3.4+δ) for λ ≤ λ_h(δ), ratio
  λ^(N−8.4−δ) e^(O(√log(1/λ))), N ≥ 9), T6 at δ = 1/10 and 1/2; P2⁗′'s sentence states the family and nothing more
  (R7.6).
- **V6-m4.** Confirmed: X13's one panel per period was not converged (0.04126 against 0.003909 at λ = 10^(−7), λκ =
  1/40), and regime (ii) was untested. X13 now uses four Gauss-Legendre panels per carrier period (eight agree to
  4.7·10^(−14)), covers λκ ∈ [1/50, 10^4] at λ = 10^(−6), 10^(−9), and also checks the sharp form (iv″) of R7.1 (b).
  R6.1's "≤ 0.048" reads "≤ 0.012" (A38).
- **V6-m5.** Confirmed. T6's control now also mutates the bump choice to round 5's h_n ≈ λ⁴ (Theorem 1's ratio then
  grows: +355 to +25138 in log10, the verifier's figures), beside removing the zero intervals; both are detected.
- **V6-m6.** Confirmed. (b′) is restated as (b″) in R7.4: on a zero interval as in (a) the first-degree term is inside w,
  so S := 0 and D is (a)'s bound; L.22′ is used under (H_N) on (v_s, v_s + x0] as proved; in the band the deciding S is
  L.12 (iii)'s.
- **V6-n1.** Re-derived: with κ_g ≥ κ/2 the condition is 2^(2−α) j c_R κ^(α−1) ≤ 1 with κ_g's own derivative (so ∫ κ_g³ g
  ≤ 2 κ_g² g, and κ³ ≤ 8κ_g³). A39.
- **V6-n2.** Re-derived: s⁻¹(G s(Φa)) = GΦa − s⁻¹(G′Φa), so s⁻¹(Gy) = GΦa − s⁻¹(G′Φa − GΦ_0 a); both O(λ|a|). A39.
- **V6-n3.** Superseded: L_1E″ uses only (H_ρ*)'s first half, so λ_1E depends on c_* and c_t, not on a rate.
- **V6-n4.** Re-derived: "then h_n ≥ λ^3.5" needs 2√(3.1L) + 1 ≤ 0.4L, L := log(1/λ), i.e. λ ≤ 10^(−31.7) (the verifier's
  scan agrees). [round 8, nit 3: the inequality holds from λ_h(1/10) = 10^(−35.80); 10^(−31.77) is where h_n ≥ λ^3.5 last
  fails in a scan] In R7.4 the window is [λ^(3.4+δ), λ^(3+δ)], valid for λ ≤ λ_h(δ) := exp(−y_h²), y_h := (2√(3+δ) +
  √(4(3+δ) + 1.6))/0.8: 10^(−35.8) at δ = 1/10, 10^(−40.14) at δ = 1/2. And φ_m, sourced by the means, enters g_app only
  through the oscillating profiles' phase, so step (1) stands.
- **V6-n5.** Confirmed (λ ε_(2N)²/m0 is +306.8 at λ = 10^(−100)). R6.2 (4)'s means term reads max_j λ^j s_n^(4j+1)
  B_(2j)², the form T6 computes (A40).
- **V6-n6.** Confirmed. constL5 K4 draws its random leaves in sorted order; its output under PYTHONHASHSEED = 0 and 1 is
  identical (largest relative difference 8.49·10^(−35) under both).
- **V6-n7.** lamL5b M1 now pins both live files by content at the run: CONSTANTS5.md md5 0320dd90…, N1STAR-PROOF.md md5
  223e1749…, "Z := d_tau - beta_ext" from line 493. [round 8, nit 12: the live files have moved since: CONSTANTS5.md
  b9617854…, N1STAR-PROOF.md 88179da4…, the phrase now from line 497; lamL5b's `.out` keeps the run's pins]
- **V6-n8.** The P1 splice is reflowed: the old text is taken from "R13). If μ0 = …", so the new text begins with "R13).
  " and every line is ≤ 120 characters (R7.6).
- **V6-n9.** P2⁗′ defines λ_L as Theorem L's threshold (R5.6) and says that the finer thresholds (λ_η, and λ_U, λ_E,
  λ_1E, λ_26, λ_25 of this note) are not evaluated.
- **V6-n10.** P2⁗′ reads "on the very edge, for Theorem 1, carried by the constraint correction".
- **V6-n11.** P2⁗′ states the sampled range: v − v_s ∈ [10^(−3.5), 10^(−2)], (H_N) to k ≤ 14 and L.16 (c) to j ≤ 15
  (X10), so K ≤ 9 with the two extra derivatives of R7.2; (H_D) at three points (T4). [round 8, m3: P2⁗′'s text omitted
  "(H_D) at three points"; superseded, R8.5 states the proof, L.27]
- **V6-n12.** R6.4's labels: T6 is a computation with unit constants too (A41).
- **V6-n13.** Confirmed. X12's majorant is now L.22′'s, |ν| T0² + λ + (ϵ′ + 1/κ + λ)|S_U|, and the least ratios are 11.7,
  95.3, 6.27·10^3, 2.71·10^7 at λ = 10^(−10), …, 10^(−80) (the verifier's figures); (H_ρ*) is exercised by X15 (R7.2).
- **Item 7 (the exclusions), re-derived.** ρ0² = N − 1: V6-m1. ρ0² = 2N − 1 with N ≡ 0 mod 4: the verifier's control B
  (leading order fails) is confirmed, but its proposed repair is not: carrying σ to order T0² cannot work, because at c_N
  = 1/2 the leading amplitude vanishes to every order in T0 (R7.2 (a)); the verifier's "min|σ| ≈ |ν|T0²" is the value at
  X = 1 on its grid, while the zero is at X = 1/(1 + T0²) (re-derived: a golden-section minimisation gives min|σ| =
  2T0|Q̃| |ν|, Q̃ of first order in x and κ^(α−1); X14 prints min|σ|/(|ν|T0²) ≤ 1.8·10^(−13)). The exclusion is removed
  instead by R7.2's argument, which does not need a lower bound for |σ|. ρ0 = ρ* without (H_ρ*)'s second half: removed by
  R7.2 too; without its first half the verifier's diagnosis (the stage family below the top, of unknown phase, competes
  with ν) is confirmed and made exact in R7.3. Reading 3's ρ0² = 2: irrelevant (R7.3). L.25′ (a)'s λ_25: not evaluated,
  said so (R7.4).

### R7.1 Three lemmas

**(a) Lemma W (A′) (pointwise; deduced, X9).** Let J := [v, v + 4πλ] and f := Re[S e^(i·/λ)] + ε on J. If S ≠ 0 on J, arg
S varies by at most π/6 on J and |ε(t)| ≤ |S(t)|/4 for every t ∈ J, then f takes both signs on J. *Proof.* t/λ + arg S(t)
increases by at least 4π − π/6 > 2π on J, so it meets 0 and π modulo 2π at t₁, t₂ ∈ J; f(t₁) ≥ |S(t₁)| − |S(t₁)|/4 > 0
and f(t₂) ≤ −|S(t₂)| + |S(t₂)|/4 < 0. ∎ In Case 1 of L_1E′ the pointwise ratio |ε|/|S| ≤ C κ^(2c′) env/(λ³ Γ_R |Ξ| Λ)
tends to 0 once env ≤ λ^(P1), which is all (A′) needs.

**(b) Lemma L.21 (iv″) (the sharp form; deduced, X13).** Let g satisfy (iv′)'s hypotheses, and let g′, g″, g‴ be positive
and log-concave with log-derivatives κ_1, κ_2, κ_3 in [κ/2, 2κ] and the c_R bound (for g = env^(N−1): (H_N) to k ≤ N +
2). Then for λκ ≤ 1/4

    ρ_g = −λ² κ_g′ + O((λκ)³ κ^(α−1) + (λκ)² κ^(2α−2)),   so   |ρ_g| ≤ C (λκ)² κ^(α−1),   |ρ_g|/λ ≤ C λ κ^(1+α).

*Proof.* From (iv′)'s three integrations by parts, with s̃_g = (i/λ)(1 − iT_g), T_g := λκ_g: 1 + ρ_g = s̃_g s⁻¹g/g = (1 −
iT_g)[1 + iT_g − λ² g″/g + λ² s⁻¹g‴/g]. Write g″/g = κ_g κ_1 and g‴/g = κ_g κ_1 κ_2, and apply (iv′)'s part (ii) (every
λ) to g‴: s⁻¹g‴ = −iλ g‴ (1 − iT_3)⁻¹ (1 + ρ_3), T_3 := λκ_3, |ρ_3| ≤ C κ^(α−1). So

    1 + ρ_g = 1 + T_g² − (1 − iT_g) λ² κ_g κ_1 [1 + iλκ_2 (1 + ρ_3)/(1 − iT_3)].

If κ_1 = κ_2 = κ_3 = κ_g and ρ_3 = 0 the bracket is 1/(1 − iT_g) and ρ_g = 0 exactly. Each κ_i − κ_(i−1) =
κ_(i−1)′/κ_(i−1) is O(κ^α) and ρ_3 = O(κ^(α−1)); to first order in these deviations ρ_g = −T_g² (κ_1 − κ_g)/κ_g + O(T_g³
κ^(α−1)), and T_g² (κ_1 − κ_g)/κ_g = λ² κ_g′; the second-order terms are O(T_g² κ^(2α−2)). ∎ X13 checks |ρ_g + λ² κ_g′| ≤
5 (λκ)³ κ^(−1/2) for env^(11) of exp(−1/x) (α = 1/2): largest ratio 3.972 (control: without the correction the ratio
grows like 2/(λκ)). X13 also checks (iv′) itself over λκ ∈ [1/50, 10^4], both regimes: |ρ_g| ≤ 2.001 ϵ′, with converged
quadrature; R6.1's 0.048 was the unconverged value of a ratio whose converged maximum is 0.0118 (A38).

**(c) L.21 at c_N = 1 (deduced, X16).** At c_N = 1 the errors of L.21 (iii)-(iv) are relative to the bracket s⁻¹[env^(N)
− s env^(N−1)] = −(i/λ) s⁻¹ env^(N−1), of size env^(N−1)/|T + i| (1 + O(ϵ′)): the top family's two terms cancel exactly
(X4, X5: the coefficients 1 and c_N are exact), the next family contributes s⁻¹(φ_1 env^(N−1) + φ_2 s env^(N−2)) with
smooth φ_i, of size env^(N−1)(λ + 1/κ_(N−2))(1 + O(ϵ′)) against |T + i|⁻¹ env^(N−1), i.e. O(λ + 1/κ) relative for every T
(|T + i| = λ|κ_(N−1) + i/λ| and |T + i|/κ_(N−2) ≤ 2/κ + 4λ); the c_N′ commutator s⁻¹(c_N′ env^(N−1)) is O(λ²) relative to
the bracket's (i/λ) part; the solve's terms are relative by construction. [round 8, nit 4: the commutator is O(λ)
relative, not O(λ²); inside O(λ + 1/κ)] So L.22′ holds at c_N = 1 with its errors relative to S_U, and, with
Γ_R|Ξ|Λ/(Λ/κ) ≥ Γ_R/(2√2 λ) on T ≥ 1, Case 1 closes on the deep very edge at ρ0² = N − 1. X16 measures the ratio of the
lower families to the bracket over (λ + 1/κ): at most 2.0 for λκ ∈ [10^(−2), 10^4] (control: a term λ⁻¹ s⁻¹ env^(N−1),
one s too many, is of the bracket's own size and is detected). [round 8, nit 5: X16 is computed, sampled, with unit
coefficients and s⁻¹ → 1/(κ_(N−1) + i/λ): it checks λ + |T + i|/κ_(N−2) ≤ 5λ + 2/κ]

### R7.2 Case 3′: every crossover window by Lemma W (A′) or (B) (removes ρ0² = 2N − 1 and (H_ρ*)'s second half)

**(a) Why order T0² cannot decide c_N = 1/2 (deduced; X14).** With i^N = 1 the top stage family is λ(i/s)²[A d ν env] =
−λ A d ν s⁻² env (L.13 (c)), and U^(1)'s bracket is s⁻¹[∂^N − c_N s ∂^(N−1)] env. At c_N = 1/2, s⁻¹(∂ − s/2)∂^(N−1) = ½
s⁻¹(∂ − i/λ)∂^(N−1) = ½ s⁻²(∂² + λ⁻²)∂^(N−1), so the top first-degree horizon amplitude is s⁻² F with F real: F = −λ A d
[ν env + ½ Γ_R λ^N (env^(N+1) + λ⁻² env^(N−1))]. In the symbol model (env^(k) = κ^k env, T = T0) σ = −ν/(1 − iT0)² + X(1
+ iT0)/(1 − iT0) vanishes exactly at X = 1/(1 + T0²): [round 8, nit 1: as printed it vanishes at X = ν/(1 + T0²); the
model is σ = ν/(1 − iT0)² + |ν|X(1 + iT0)/(1 − iT0) = |ν|(1 − iT0)^(−2)[X(1 + T0²) − 1]] the T0² coefficient of |σ|'s
lower bound is zero, and so is every higher one. In the exact model the minimum is 2T0|Q̃| |ν|(1 + o(1)), [round 8, nit
2: 2T0|ν|(|Q̃| + higher order)] Q̃ := (1 − 2c_N(r0)) − (κ − κ_(N−1))/κ, of first order in x and κ^(α−1), and Q̃ vanishes
identically to first order for exp(−a/x) with a = 2N(N − 1)√μ0/ρ0. So no lower bound for |σ| at the cancellation decides
these envelopes; a window where S is small is decided instead by S′ (Lemma W (B)).

**(b) Two hypotheses.**

    (H_N+2)  (H_N) for env^(k), k ≤ N + 2, with the same α;
    (H_t)    κ − κ_(N−1) ≥ c_t κ^α on (v_s, v_s + x0]  (implied by |κ′| ≥ c_t κ^(1+α), since κ − κ_(N−1) =
             Σ_(k<N−1) |κ_k′|/κ_k ≥ |κ′|/κ).

Both hold for exp(−a/x^q) edges (α = 1/(q + 1)); X10 samples them for exp(−1/x) and the record's envelope: [round 8, m1,
nit 7: X10 measures c_t and does not test (H_t); both hypotheses are proved for both envelopes, with controls, hyp5,
Proposition L.27] κ − κ_k ≥ 2.0 k κ^(1/2), resp. 1.996 k κ^(1/2), k ≤ 14, and |κ′| ≥ 2.0 κ^(3/2), resp. 1.996 κ^(3/2).

**(c) Proposition L.26 (Case 3′; deduced, with edge1_5 X14, X15).** In Theorem L_1E′'s setting [round 8, nit 9: without
its conditions on τ0] assume (H_N+2), (H_D), (H_t), and, if ρ0 = ρ*, (H_ρ*)'s first half κ(v)(v − v_s)² ≥ c_*. There are
λ_26, M such that for λ ≤ λ_26 every window J in the crossover |ν|/M ≤ Γ_R|Ξ|Λ ≤ M|ν||1 + 2iT0| has, at ω, points where
g_λ⁻¹(dΦ0, dΦ0) is positive and points where it is negative — for every N and every c_N(ρ0), c_N = 1/2 included.

*Proof.* (1) *Splitting.* σ := S/(λ³ A d env) = A_s + B_s + ê, where A_s := the whole stage sum Σ_(j≤N+1) λ^j H_j,vv(v,
√μ0) over λ³ A d env (L.13 (c): ν(r0) st(v) + λ a₁(r0, v), st := Σ_(k≤N−2)(k + 1)(iλ)^k env^(k)/env, a₁ a finite sum of
smooth coefficients times (λ^k env^(k)/env), so |a₁| ≤ C and |a₁′| ≤ C(1 + T0 κ^α)); B_s := −Γ_R i^N Ξ_ex Λ with the
exact Ξ_ex := (1 − c_N) − (i/λ) s⁻¹env^(N−1)/env^(N−1) (no replacement of s⁻¹); and ê the rest, every term of which is
O((1/κ + λ)|B_s|) with |∂_v^k ê| ≤ C κ^k (1/κ + λ)|B_s| (L.22's derivative bounds: the lower families of F_ρ, the solve's
corrections, the c_N, α, r^(−7/2) commutators, H_Σ's O(𝒟/|s̃|) and Z_f). The term (ϵ′)|S_U| of L.22′, whose crude
derivative bound κϵ′|S_U| is too large (V5-n6), does not occur: s⁻¹ is kept. (2) *Derivatives.* (s⁻¹g/g)′ = −ρ_g, so
Ξ_ex′ = −c_N′ + (i/λ)ρ_g and, by (iv″), |Ξ_ex′| ≤ C(1 + λκ^(1+α)); with Λ′/Λ = κ_(N−1) − κ and |Ξ_ex| ≥ c_N/2 (T0 ≤ 1):
B_s′ = −B_s(κ − κ_(N−1))(1 + O(T0 + κ^(−α))). And A_s′ = ν′ st + ν st′ + λa₁′ with |st′| ≤ C T0 κ^α. Second derivatives:
|B_s″| ≤ C|B_s| κ^(1+α) (by (H_N) and ρ_g′ = κ_g′(1 + ρ_g)/s̃_g − s̃_g ρ_g, |ρ_g′|/λ ≤ C κ^(1+α)), |A_s″| ≤ C(|ν| +
λ)κ^(1+α) (at ρ*, |ν″| ≤ C ≤ C′|ν|κ as κx² ≥ c_*, and |ν′| ≤ C|ν|κ^α, see (4)), |ê″| ≤ C(κ + λκ²)|B_s|. (3) *|A_s| at a
near-cancellation.* Off ρ*, |ν| ≥ ν_*; at ρ*, x² ≥ Mλ throughout Case 3 (if x² < Mλ, κ ≥ c_*/(Mλ), T0 ≥ c_*/M and Λ ≍
T0^(N−2) κ ≫ M|ν|, against Case 3); so |A_s − ν| ≤ C(|ν|T0 + λ) ≤ |ν|/8 for λ small. (4) *The dichotomy.* Put τ := c_t
κ^(α−1) |ν|/16 (κ at v). If |A_s + B_s| ≥ τ on J: then |σ| ≥ τ/2 (|ê| ≤ C(1/κ + λ)M|ν| ≪ τ, as κ^(α−1) ≫ 1/κ, λ), arg σ
moves over J by at most 4πλ C|ν|κ^α/(τ/2) = 128πC T0/c_t ≤ π/6 (at ρ*, |ν′| ≤ 2c_ν x ≤ C|ν|κ^α, as κ^(−α) ≤ αc_R(v − v_s)
by the c_R bound), and |ε| ≤ C κ^(2c′) env² ≤ |S|/4 pointwise once env ≤ λ^(P1): Lemma W (A′). Otherwise |A_s + B_s| < τ
at some t₀ ∈ J, hence ≤ τ + 4πλ C|ν|κ^α ≤ 2τ on J, so B_s = −A_s + O(τ) = |ν|(1 + O(1/8 + τ/|ν|)) lies near the positive
real axis (ν < 0). Then Re B_s′ ≤ −|ν| c_t κ^α/2, and Re A_s′ ≤ C(|ν| T0 κ^α + λ(1 + T0κ^α)) because Re(ν′ st) ≤ 0 at ρ*
(ν′ = −2c_ν x(1 + o(1)) < 0) and |ν′| ≤ C ≪ |ν|κ^α off ρ*; so Re σ′ ≤ −|ν| c_t κ^α/3. With S = λ³ A d env σ, S′ = λ³ A d
env (κσ + σ′) and |κσ| ≤ 2κτ = c_t|ν|κ^α/8, so |S′| ≥ λ³ A |d| env |ν| c_t κ^α/5 =: L0 on J (env changes by at most
e^(8πT0) ≤ 2 across J), while |S″| = λ³ A|d| env |κ²σ + κ′σ + 2κσ′ + σ″| ≤ C λ³ A|d| env |ν| κ^(1+α) ≤ L0/(80πλ) once λκ
≤ c_t/(800πC) (T0 → 0 in Case 3), and |ε| ≤ πλL0/5 once env ≤ λ^(P1). Lemma W (B). ∎

*What is used, and what is not.* Nothing in (4) depends on c_N(ρ0) or on N mod 4: the transversality is Λ′/Λ = κ_(N−1) −
κ (H_t), and the sign of B_s′ against A_s′ is fixed by ν ≤ 0, ν′ ≤ 0 at ρ* and Λ decreasing. The lower bound for |σ| is
never used where |σ| is small. At ρ* the stage family below the top, λa₁, is kept in A_s exactly (its phase is unknown)
and only its smallness against ν, step (3), is used: that is (H_ρ*)'s first half.

**(d) Computation (X14, X15; unit constants, exact derivatives).** X14, at ρ0² = 23 = 2N − 1, N = 12 (c_N(ρ0) = 1/2), ν =
−1/9, with ρ_g of (iv″) in Ξ_ex: for exp(−1/x) and the record's envelope at λ = 10^(−40) and 10^(−80) (λκ = 2.0·10^(−4),
4.7·10^(−8)) every window is decided, by (A′) on the 201-point log grid of the crossover and by (B) on all 121 windows
around min|σ|; at λ = 10^(−160) [round 8, m2: vacuous rows (x + 4πλ == x at 60 digits), dropped from X14; nit 8: X14 does
not exercise L.26's mechanism — with Λ frozen its windows are still decided, the model's σ′ carrying |ν|T0κ^α from the
stage series and Ξ′; L.26 needs (H_t) because those terms have no known sign] the minimum lies below the 60-digit
resolution of the search and the sampled windows are all decided by (A′); and min|σ| ≤ 1.8·10^(−13) |ν|T0² (the T0² route
fails). Control: round 5's error class (ϵ = λκ, crude derivative bound) in place of ê: the windows around min|σ| are not
decided. X15, at ρ0 = ρ*, N = 12, ν = K(r0), with an unknown structured term λ b4, |b4| = 1, b4 ∈ {1, i, −1, −i}:
exp(−1/x) (κx² = 1) with N = 12 at λ = 10^(−40), 10^(−80) and N = 10 at λ = 10^(−40), and the record's envelope (κx² =
0.75) with N = 12 at λ = 10^(−40): λ/|ν| ≤ 3.4·10^(−6) at the crossover, and every window decided for each b4. Control:
exp(−1/x^(1/2)) (κx² → 0, (H_ρ*)'s first half fails), N = 10, with the family's two leading coefficients λ(b4 + iT0 b5)
chosen (both of modulus < 1) so that σ and σ′ vanish together: with |b4| = 0.0033 and |b5| = 1.0·10^(−4) (λ/|ν| ≈ 349 at
the crossover) [round 8, nit 6: X15 now prints these figures] a window is undecided: the control fails, as it must.

### R7.3 Theorem L_1E″, and what each exclusion became

**Theorem L_1E″ (Theorem 1's deep layer and very edge; deduced from L_1E′'s proof, R7.1 and Proposition L.26).** Let μ0 =
√72 l5², K ≥ 6, N = K + 3, g_λ Theorem 1's metric with stage N's data by Lemma 6.2's rule (D615, D616), section 6.4's
"lapse and shift of g_app" read as the supplement reads the shift (reading 2: N1STAR-PROOF.md section 4, step (ii), "Z :=
d_tau - beta_ext (beta_ext the shift of g_ext)", from line 493 at md5 223e1749…, a live file (lines 483-484 at 7400212b…,
the verifier's reading); reading 1 gives the same), env satisfying (H_N) (α < 1, L.16 (c)'s first bound to j ≤ N + 2) and
(H_D) on (v_s, v_s + x0], and τ0 admissible, ρ0 := (v_s − τ0)/√μ0, with [round 8: superseded by Theorem L_1E‴, R8.4: at
ρ* the first condition may be replaced by (H_N+2) and (H_t)]

    if ρ0 = ρ*:                                       κ(v)(v − v_s)² ≥ c_* > 0 on (v_s, v_s + x0];
    if N ≡ 0 mod 4 and (ρ0² = 2N − 1 or ρ0 = ρ*):    (H_N+2) and (H_t).

Then L_1E's conclusion holds: there are λ_1E > 0, x0′ ∈ (0, x0] and P1 such that for λ ≤ λ_1E, every v ∈ (v_s, v_s + x0′]
with env(v + 4πλ) ≤ λ^(P1) and every ω ∈ S³, on [v, v + 4πλ] the boundary x_K = 1 has, at ω, points where it is timelike
for g_λ and points where it is spacelike; with L.12 (ii), every such interval below λ^(3+δ). *Proof.* R6.1's Cases 1-3
with: Lemma W (A′) in Case 1 (R7.1 (a)); R7.1 (c) at c_N = 1; in Case 3 the non-cancelling branches as in R6.1 (they use
(H_ρ*)'s first half only), the cancelling branch (N ≡ 0 mod 4) by R6.1's quadrature argument when c_N(ρ0) ≠ 1/2 and ρ0 ≠
ρ*, and by Proposition L.26 otherwise; Case 2 as in R6.1. ∎

*The exclusions.*

- **ρ0² = N − 1 (paper's K + 2): removed** (R7.1 (c); V6-m1).
- **ρ0² = 2N − 1 with N ≡ 0 mod 4 (paper's 2K + 5): removed**, under (H_N+2) and (H_t), which hold for the edges named
  and are sampled for the record's envelope (R7.2). [round 8, m1: proved for it, every K, Proposition L.27]
- **ρ0 = ρ*: narrowed** from (H_ρ*) (both halves) to its first half, κ(v − v_s)² bounded below, for every N (R7.2); it
  holds whenever (H_N)'s α ≤ 1/2. The record's envelope (κx² → 3/4) is now covered for every K. [round 8, m1: an
  overclaim in round 7 — at ρ* with K ≡ 1 mod 4 it needs (H_N+2), (H_t), then sampled for K ≤ 9; true now, L.27 proving
  both for every K]
- **ρ0 = ρ* with liminf κ(v − v_s)² = 0: the method provably fails, [round 8, nit 11: cannot decide for some admissible
  b̂4, b̂5; removed: b̂4 = −0.0382 i and b̂5 = 3b̂4 are computed, Lemma L.28, R8.1] and the coefficients that would
  decide it are named.** The case needs (H_N)'s α > 1/2 (since κ^(−α) ≤ αc_R(v − v_s), α ≤ 1/2 gives κ(v − v_s)² bounded
  below). There the crossover can lie at x² ≪ λ (for exp(−1/x^(1/2)), N = 10, λ = 10^(−40): λ/|ν| ≈ 349 there), where the
  stage family below the top dominates ν: λa₁ = λ(b̂4 + iT0 b̂5 + …), b̂4(θ) := c_(4,0),vv(√μ0; ρ*√μ0, θ)/(A d(θ)) and
  b̂5 the coefficient of λ env′ from c_(5,1),vv (L.13 (c)'s family j − 4 at j = 4, 5). Step (3) then fails — at a
  near-cancellation A_s ≈ −B_s ≈ ν + λb̂4, whose phase is b̂4's — and with it the sign argument of step (4): for N ≡ 2
  mod 4 (B_s ≈ −c_N Λ) and Re b̂4 > 0 the real parts of σ′ ≈ ν′ + A_s(κ − κ_(N−1)) cancel, and λ T0′ b̂5 can cancel the
  rest. The record bounds b̂4, b̂5 by C and nothing more, and X15's control exhibits admissible values (|b̂4| = 0.0033,
  |b̂5| = 1.0·10^(−4)) for which σ and σ′ vanish together and a window is undecided: the method cannot decide these
  windows. What would decide them is b̂4(ρ*√μ0, θ) and b̂5(ρ*√μ0, θ): H_4's and H_5's family-(j − 4) coefficients at the
  horizon, a computation like layerlin5 N4-N5 one and two orders higher, with the r0-dependence of the lower profiles
  kept (∂_v acts on r0 = v − τ0). That computation is not done in this round; [round 8: done, bfam5, R8.1] L_1E″ and the
  paper state the case as excluded (R7.6).
- **ρ0² = 2 under reading 3: irrelevant.** The supplement's convention is reading 2 ("Z := d_tau - beta_ext", from line
  493 at md5 223e1749…; lamL5b M1 locates it at each run), under which Γ_R = K_R r0^(−7/2)/α > 0 for every ρ0; L_1E″ is
  stated for readings 1 and 2 only, and no statement of this note or of the paper carries ρ0² ≠ 2.

### R7.4 Proposition L.25″ (dips, every δ ≤ 1/2) and the criterion (b″)

**Proposition L.25″ (a) (deduced, with degtwo5 T6).** L.25′ (a) holds for every 0 < δ ≤ 1/2 with n the least index with
h_n ≤ λ^(3+δ): for λ ≤ min(λ_25(δ), λ_h(δ)) and every ω, g_λ⁻¹(dΦ0, dΦ0) ≤ −m0/2 on J_n′, which lies below λ^(3+δ) (sup
env = h_n/e) and is longer than 4πλ. *Proof.* As L.25′ (a)'s, with these changes. Since h_(n−1) > λ^(3+δ), h_n = h_(n−1)
e^(−(2n−1)) > λ^(3+δ) e^(−(2n−1)), and n ≤ √((3 + δ)L) + 1 with L := log(1/λ); so h_n ≥ λ^(3.4+δ) once 2√((3 + δ)L) + 1 ≤
0.4L, i.e. λ ≤ λ_h(δ) (R7.0, V6-n4). Step (4)'s ratio is at most C″(max_j λ^j s_n^(4j+1) B_(2j)² + λ^(N−5) h_n⁻¹
s_n^(M*+1) B_(M*)) ≤ C″(max_j λ^j s_n^(4j+1) B_(2j)² + λ^(N−8.4−δ) s_n^(M*+1) B_(M*)) → 0, since N − 8.4 − δ ≥ 0.1 for N
≥ 9; for Theorem 2 λ^(N_P−6.4−δ). L.4′'s hypothesis ε_4(v_1) ≤ λ and L.4_P's ε_(M_P)(v_1) ≤ λ³ hold for λ small as before
(h_n ≤ λ^(3+δ)). ∎ T6, at δ = 1/10 and 1/2 on λ = 10^(−10^2), …, 10^(−10^6): Theorem 1's ratio, in log10, is +221, −86,
−6544, −82950, −877515 at δ = 1/10 and +286, +335, −2578, −42399, −476461 at δ = 1/2 (the decay λ^(0.1) wins only from λ
≈ 10^(−10^4) on), Theorem 2's and the means' are negative throughout; from λ = 10^(−10^6) (δ = 1/10, where L.4_P's
hypothesis first holds on the grid) and λ = 10^(−10^4) (δ = 1/2) on, every ratio is below 0 with both hypotheses and
decreasing; λ_h = 10^(−35.8) and 10^(−40.14); both controls detected. λ_25(δ) is not evaluated: an effective threshold
[round 8: withdrawn; λ_25(δ) is a certified formula in the record's constants, R8.3] would need a bound for w on a zero
interval without the derivative loss of L.4′ (s_n^(M*+1)), i.e. the first-degree memory computed and a localised
degree-two bound where L.17's hypothesis fails.

**(b″) The criterion, where it decides** (replaces (b′); V6-m6). At a boundary point in the deep layer, g_λ⁻¹(dΦ0, dΦ0) =
−m0 − Re[S e^(iv/λ)] + ρ with |ρ| ≤ D(v), where (S, D) is: on a zero interval as in (a), S := 0 and D the bound of (a)'s
step (4) (the first-degree memory is inside w there); in the band λ^(3+δ) ≤ E ≤ λ^(3−δ), S the first-degree amplitude of
L.12 (iii) and D its degree-two bound, D ≤ λ^γ m0; on a stretch where (H_N) and (H_D) hold on all of (v_s, v_s + x0] —
the setting of L.22′ and L.18 — S of L.22′ (Theorem 1) or of L.15_P (b) (Theorem 2) and D = C κ^(2c′) env². Every
interval [v, v + 4πλ] on which S varies slowly has timelike points at ω if max_J (|S| − m0) ≥ C(λ^γ m0 + D), and none if
max_J (|S| + D) < min_J m0. So the ratio |S|/m0 decides up to 1 ± 2λ^γ in the band, a zero interval as in (a) is
spacelike, the very edge of L_E, L_1E″ has timelike points, and elsewhere (a dip where env > 0 and no listed D is below
m0) the criterion decides nothing.

### R7.5 Amendments, programs, labels

- **A36** (V6-m1). R5.3 Remark (2) and R6.1 Remark (1): ρ0² = N − 1 is not excluded; the reason given there is withdrawn
  (R7.1 (c)).
- **A37** (V6-m2). Lemma W (A) reads as (A′) of R7.1 (a); L_1E′'s Case 1 cites (A′).
- **A38** (V6-m4). R6.1: "|ρ_g|/(λκ)² ≤ 0.048" reads "≤ 0.012" (converged).
- **A39** (V6-n1, n2). R6.1 (b)(i): "once 2^(2−α) j c_R κ^(α−1) ≤ 1, with κ_g's own derivative"; R6.1 (c): "s⁻¹(Gy) = GΦa
  − s⁻¹(G′Φa − GΦ_0 a)".
- **A40** (V6-n5). R6.2 (4): the means' term is max_j λ^j s_n^(4j+1) B_(2j)².
- **A41** (V6-n12). R6.4: "models with unit constants: X11, X12, T5, and T6 (a computation with unit constants)".
- **A42.** R6.1 (d)'s Theorem L_1E′ is superseded by L_1E″ (R7.3); R6.2's L.25′ (a) by L.25″ (a) and (b′) by (b″) (R7.4);
  R6.6's list of exclusions by R7.3.
- **Programs.** `checks/edge1_5.py`: X9 (A′), X10 (H_N to k ≤ 14 and (H_t)), X12 (L.22′'s majorant), X13 (converged, both
  regimes, (iv″)), and new X14 (Case 3′ at c_N = 1/2), X15 (Case 3′ at ρ*), X16 (c_N = 1). `checks/degtwo5.py`: T6 (δ ≤
  1/2, j-resolved means, the two controls). `checks/constL5.py`: K4's sorted leaves, run under two hash seeds.
  `checks/lamL5b.py`: M1 pins both live files. Each with its `.out` from a full run (R7.7).
- **Labels.** Computed, exact: X1-X8, X16 (symbolic families; X16 sampled), [round 8, nit 5: X16 is computed, sampled]
  T1-T3, T7, K1, K2; computed, sampled or bounds (mpmath): X9, X10, X13, T4, K3, K4; computations with unit constants:
  X11, X12, X14, X15, T5, T6. Deduced: Lemma W (A′), L.21 (iv″), R7.1 (c), Proposition L.26, Theorem L_1E″, Proposition
  L.25″, (b″).

### R7.6 Proposed paper text (replaces R6.5's P1⁗ and P2⁗; P3-P6 stand, P3's list extended)

(P1⁗′) Proposition 3.2: the old text, from "R13). If μ0 = √72 l5² exactly, the" (line 302 of RESPONSE-HL-5D.md at md5
5930486d…, the file as it now stands) to "Propositions E.2-E.4)." (line 305), occurs once; it is replaced by:

> R13). If μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the
> shell starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
> `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that layer, for λ small, every column has points
> where it is timelike for g_λ, so the no-return property stated above for μ0 > √72 l5² fails at equality
> (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L, L_P, L_E and L_1E″, Corollary L.7).

(P2⁗′) Section 9: the bullet from "- **The boundary at equality.** If μ0 = √72 l5² exactly (computed," (line 1533) to
[round 8, M1: line 1547] "with √μ(v) − r_q(v) ≥ C' λ." (line 1541) [round 8, M1: 1555, at 5930486d…; superseded by R8.5's
final text, generated from these bounds], which occurs once, is replaced by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced in `docket68/n1star/EQUALITY5.md` and `EQUALITY5-LAYER.md`
>   [†], computed by the programs of Appendix A), x_K = 1 is the seed's horizon on {v ≤ v_s}, v_s := inf supp env, and is
>   spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η. In the layer between, for λ small and 0 < δ ≤ 1/2, it is spacelike
>   where sup_(v'≤v) env ≥ λ^(3−δ), and where λ^(3+δ) ≤ sup env ≤ λ^(3−δ) its character is that of the ratio of λ³ A env
>   |ν| |d| to the margin, up to a factor 1 ± 2λ^(1/10) (d the double divergence of the waves' angular tensor, |d| ≥ 8/3;
>   ν ≤ 0 a coefficient of the seed and τ0, with a double root at (v_s − τ0)/√μ0 = ρ* = 1.806…). Suppose that near v_s
>   env and its first K + 3 derivatives are positive and log-concave, with logarithmic derivatives κ_k within a factor 2
>   of κ := (log env)′ and |κ_k′| ≤ c κ_k^(1+α) for an α < 1, and that env obeys the derivative and decay bounds of
>   `EQUALITY5-LAYER.md` R5.2 and R6.1 (sampled for the C_c^∞ envelope used for the constants, on 10^(−3.5) ≤ v − v_s ≤
>   10^(−2) and for K ≤ 9). For Theorem 1's solution suppose also that (v_s − τ0)/√μ0 ≠ ρ* unless κ (v − v_s)² is bounded
>   below near v_s (as it is when α ≤ 1/2), and, when K ≡ 1 mod 4 and (v_s − τ0)²/μ0 = 2K + 5 or (v_s − τ0)/√μ0 = ρ*,
>   that the first K + 5 derivatives obey the same and |κ′| ≥ c′ κ^(1+α). Then that ratio crosses 1 once per column, and
>   below λ^(3+δ), down to v_s, every interval of length 4πλ has timelike and spacelike points on every column; the term
>   linear in the waves is computed there to leading order, on the very edge, for Theorem 1, carried by the constraint
>   correction at first degree. For some envelopes whose intervals of zeros accumulate at the edge (`EQUALITY5-LAYER.md`,
>   Proposition L.25″ (a)), intervals of length 4πλ below λ^(3+δ) on which x_K = 1 is spacelike throughout occur for
>   every small λ. So timelike curves of g_λ cross x_K = 1 into D_T. A domain O(λ)-close to D_T, inside x_K ≤ 1, has an
>   inner boundary that no future causal curve enters, and the spheres' horizon holds in the form: at most one zero per
>   column, within C λ of √μ(v); exactly one on the columns with v ≤ v_s and on those that reach across √μ(v) + C λ with
>   √μ(v) − r_q(v) ≥ C' λ. The threshold λ_L of Theorem L's proof is an explicit formula in the leaves of λ0, two
>   constants of the seed and Theorem 1's C1, and is below 3·10^(−12); the thresholds of the finer statements (λ_η above
>   and those named in `EQUALITY5-LAYER.md`) are not evaluated.

[†] "(rounds 1-6 read by independent verifiers; round 7 not yet read)". Sources: the layer and band, L.12 (i), (iii)
(A24); the single crossing, L.24; the intervals below λ^(3+δ), L.12 (ii) with L_E (Theorem 2; A25) and L_1E″ (Theorem 1;
R7.3); the linear term, L.15_P (b) and L.22′; the dips, L.25″ (a); the crossing curves, Corollary L.7; the inner boundary
and the spheres' horizon, EQUALITY5.md Propositions E.4, E.5; λ_L, R5.5, R5.6. (P3⁗′) Appendix A, C, D:
`checks/edge1_5.py` X1-X16, `checks/degtwo5.py` T1-T7, `checks/constL5.py` K1-K4, with the run times of their `.out`
files and their controls as in their docstrings; P5's commands for bandL4p5 and lamL5b stand, with their new md5s.

### R7.7 Open items, runs, sources

Open items: none in section 9's sense. Every claim of P1⁗′ and P2⁗′ is proved on the hypotheses the text states; the one
case the hypotheses leave out (ρ0 = ρ* with liminf κ(v − v_s)² = 0) is stated as excluded, the method's failure there is
shown (X15's control exhibits admissible coefficients for which it cannot decide), and the coefficients that would decide
it are named (R7.3). The thresholds λ_η, λ_U, λ_E, λ_1E, λ_26 and λ_25 are not evaluated, and the paper says so. [round
8: λ_25 is a certified formula in the record's constants, R8.3; the others depend on λ0's leaves] [R9, m1: "depend on
λ0's leaves" reads "depend on constants the record does not certify: λ0's leaves for Theorem 1, Theorem P's for Theorem
2"; λ_25's inputs are written out in R9.1, C_L1 certified, and λ_25 is certified below 10^(−6613.6), R9.2] O2: round 7
awaits an independent reader.

Runs (full, each `.out` beside its program): edge1_5 X1-X16, 2548 s (`.out` md5 37f1af44…, program 66b0ba5e…); degtwo5
T1-T7, 388 s (44b85247…, 2340d7a0…); constL5 K1-K4 under PYTHONHASHSEED = 0 and 1, the outputs identical (775ff458…,
fb8f0f6b…); lamL5b M1-M5, 141 s (535c8b1e…, 8633d245…); bandL4p5 unchanged (its `.out` stands). Every check passes and
every control fails; the times are under a load average near 25 on four cores.

READ: the verifier of round 6's report (as relayed) and its scripts (case3.py's model B, re-run here: min|σ_main|/(|ν|T0)
at X = 1 as it reports, and a golden-section minimisation for the true minimum); N1STAR-PROOF.md at md5 223e1749…
(section 4 step (ii), from line 493); CONSTANTS5.md at md5 0320dd90… (M1); RESPONSE-HL-5D.md at md5 5930486d… (lines
302-305, 1533-1541; the same texts and lines as at 7193c56e…). [round 8, M1: P2's lines are 1547-1555 at 5930486d… (moved
at 8a1f050); P1's are 302-305] File md5 before this round: acaf8822….

## Round 8 (2026-11-06)

This round removes the one exclusion round 7 left (ρ0 = ρ* on an edge with liminf κ(v − v_s)² = 0): the coefficients
b̂4, b̂5 of the stage family below the top are computed exactly (R8.1), b̂4 is a nonzero imaginary number at ρ* for every
wave, and Lemma L.28 decides every crossover window there. It proves (H_N+2), (H_t), (H_D), L.16 (c) and (H_ρ*)'s first
half for the record's envelope, for every K, where round 7 sampled them (R8.2); writes λ_25 as a certified formula in
the record's constants and names what it waits for (R8.3); states Theorem L_1E‴, which has no exclusion left (R8.4);
and gives the final paper texts, each old text generated from its quoted bounds (R8.5). It also seats the independent
reader of round 7, who confirmed its mathematics and found the P2 splice at the wrong lines (R8.0). Earlier text stands,
with bracketed notes "[round 8, …]" at every amended site.

### R8.0 The reader of round 7, seated (each finding re-derived)

READ (as relayed, and its report `scratchpad/report-vE7.md`): the mathematics of round 7 confirmed — R7.0's
re-derivations, Lemma W (A′), L.21 (iv″), R7.1 (c), the rejection of the T0² route (re-derived independently),
Proposition L.26 line by line, Theorem L_1E″, L.25″, (b″) — and all four programs reproduced; not confirmed as it stood
because of M1.

- **M1 (the P2 splice).** Re-derived and confirmed. In RESPONSE-HL-5D.md at md5 5930486d… and at 4c121081… (the file as
  it now stands) the bullet "- **The boundary at equality.** If μ0 = √72 l5² exactly (computed," … "with √μ(v) − r_q(v)
  ≥ C' λ." is at lines 1547-1555 (it moved 14 lines at commit 8a1f050), and lines 1533-1541 are the middle of the
  two-dust bullet before it; `wsE5/r7/old2.txt` was those nine lines, which occur once, so the "occurs once" check
  passed and the splice would have overwritten the two-dust bullet. R7.0's "the two texts unchanged and at the same
  lines" and R7.7's "1533-1541; the same texts and lines as at 7193c56e" were false for P2 (true for P1, lines
  302-305). Repaired: notes at R7.0, R7.6, R7.7; R8.5 generates every old text from its quoted start and end strings
  (content, never line numbers: `wsE5/r8/paper/gen_old.py`), checks that each occurs once in the file at its current
  md5, and simulates the splice (the two-dust bullet intact, every line ≤ 121).
- **m1 (overclaims).** Confirmed: "the record's envelope … is now covered for every K" (R7.3) needed, for K ≡ 1 mod 4
  at ρ*, (H_N+2) and (H_t), which round 7 only sampled (X10: k ≤ 14, K ≤ 9); and the round's opening, R7.3's ρ*
  bullet and five round-7 notes read as unconditional where L_1E″ conditions on (H_N+2) and (H_t) for N ≡ 0 mod 4.
  Repaired both ways: the conditions are added at each site ("[round 8, m1: …]"), and R8.2 proves both hypotheses for
  the record's envelope for every K (Proposition L.27), so that the sentence of R7.3 is now true.
- **m2.** Confirmed: at mp.dps = 60 and λ = 10^(−160), x ≈ 2·10^(−73) and x + 4πλ == x, so X14's rows there decided
  zero-width windows. They are dropped (X14 at 10^(−40) and 10^(−80), both resolved); edge1_5 rerun.
- **m3.** Confirmed: P2⁗′ did not say "(H_D) at three points". Superseded: R8.5's text states the proof (L.27).
- **Nits.** (1) R7.2 (a)'s symbol-model formula reads σ = ν/(1 − iT0)² + |ν|X(1 + iT0)/(1 − iT0) = |ν|(1 −
  iT0)^(−2)[X(1 + T0²) − 1] (re-derived; the zero at X = 1/(1 + T0²) stands). (2) "min|σ| = 2T0|Q̃||ν|(1 + o(1))" reads
  2T0|ν|(|Q̃| + higher order): for the envelope with a = 2N(N − 1)√μ0/ρ0, Q̃'s first-order part vanishes and other
  second-order terms set the minimum (the conclusion is strengthened). (3) V6-n4: 2√(3.1L) + 1 ≤ 0.4L holds from
  λ_h(1/10) = 10^(−35.80); 10^(−31.77) is where h_n ≥ λ^3.5 last fails in a scan. (4) The c_N′ commutator is O(λ)
  relative to the bracket's (i/λ) part, not O(λ²) (inside O(λ + 1/κ); R7.0 V6-m1 and R7.1 (c)). (5) X16 is "computed,
  sampled" (R7.5's labels), with unit coefficients and the symbol s⁻¹ → 1/(κ_(N−1) + i/λ): it checks λ + |T + i|/κ_(N−2)
  ≤ 5λ + 2/κ. (6) X15's control figures are now printed (edge1_5's `.out`). (7) X10 measures c_t and cannot fail on (H_t)
  alone; (H_t) is now proved — a certified lower bound for c_t, not a sample (hyp5 H1-H3) — and hyp5's controls exercise
  the certifier (the range [0, 1/40], the sin⁴ edge); an envelope failing (H_t) alone is not constructed. (8) X14 does
  not exercise L.26's mechanism: with Λ frozen its windows are still decided, the model's σ′ carrying |ν|T0κ^α from the
  stage series and Ξ′; L.26 needs (H_t) because those terms have no known sign — said in R7.2 (d)'s note; X17 (R8.1) does
  not exercise Lemma W (B) either (all its windows go by (A′), the phase of b̂4 keeping σ from zero [R9, nit 3: |λb̂4|
  against |ν| keeps it there, not the phase: a positive real b̂4 of the same modulus is decided too, R9.3]). (9) L.26
  reads "in
  Theorem L_1E′'s setting without its conditions on τ0". (10) R8.5's text writes the [†] parenthesis out and is reflowed
  (every line ≤ 119). (11) "provably fails" reads "cannot decide for some admissible b̂4, b̂5" (R7.3 said so); superseded
  by R8.1. (12) Pin drift, re-measured: CONSTANTS5.md is now b9617854…, N1STAR-PROOF.md 88179da4…, and "Z := d_tau -
  beta_ext" is now from line 497 of it; lamL5b's `.out` records the run's pins (0320dd90…, 223e1749…, line 493),
  unchanged and not rerun.

### R8.1 The family below the top, computed; the last exclusion removed (task 1)

*The computation (bfam5 B1-B5; exact).* The profiles of R7.3: H_j = Σ_k env^(k)(v) c_(j,k)(r, r0, θ), r0 = v − τ0,
H_(j+1) solving T(H_(j+1)) + R_X(H_j) = 0 along ℓ with the data i Pol^+(D_X H_j) at r = r0, and ∂_v acting on r0:
∂_v(c E^(k)) = (∂_(r0) c) E^(k) + c E^(k+1). The operators are taken once from layerlin5's `ops` on the general profile
(eight free functions; the λ^(−1) and λ^0 parts of dRic^H and dD as lists of coefficient, component and derivative) and
applied to family vectors, for every angular profile a(θ), b(θ) of the wave H1 = A E r^(1/2) diag(−(a + b), cos²θ a,
sin²θ b). In the angle t = tan(θ/2) every coefficient is rational, and each profile is kept in a canonical form (a sum
over the wave factor a^(k), b^(k) and the powers of r, log r, r0, log r0 of reduced rational functions of t), so that a
zero test is an exact cancellation. At μ0 = 1, every T² × Z2 × Z2-invariant component:

- B1: H2 = c_(2,0) E (family 1 of R_X(H1), D_X(H1) vanishes), T(H2) + R_X(H1) = 0 (8 components) and i Pol(H2) +
  D_X(H1) = 0 (3) everywhere, H2 ∈ S (layerlin5 N3).
- B2: H3 = c_(3,1) E′ + c_(3,0) E with the r0-motion: c_(3,1) = i c_(2,0), both equations in both families, and c_(3,0)'s
  vv component at the horizon is A d K(r0), K = −(2r0³ − 3r0² − 2)²/(36r0⁶): L.13 (b), (c) hold with ∂_v acting on r0
  (the motion enters c_(3,0)'s vector sector, not its scalar one).
- B3: H4: c_(4,2) = −c_(2,0) and c_(4,1) = 2i c_(3,0) (L.13 (b)'s top two families at j = 4, with the r0-motion), both
  equations in families 0 and 1, and, exactly, for every angular profile (Δ the Laplacian of S³, Δf = (cos θ sin
  θ)⁻¹∂_θ(cos θ sin θ ∂_θ f)):

      c_(4,0),vv(1; r0, θ) = A [α4(r0) d + β4(r0) Δd],
      α4 = −i (6376r0⁹ − 26460r0⁸ + 58590r0⁷ − 74865r0⁶ + 132300r0⁵ − 122661r0⁴ + 8400r0³ + 4320r0² + 25340)/(90720r0⁹),
      β4 = i (r0 − 1)(2r0³ − 3r0² − 2)²/(72r0⁷) = −i (r0 − 1) K(r0)/(2r0).

- B4: H5's family 1 in its vv, vr, rr components (all that c_(5,1),vv needs), both equations there, and c_(5,1),vv(1;
  r0, θ) = 3i c_(4,0),vv(1; r0, θ) exactly (at the horizon; the analogue, one family lower, of L.13 (b)'s c_(4,1) = 2i
  c_(3,0)).

**So b̂4 and b̂5 are numbers.** b̂4(r0, θ) := c_(4,0),vv(1; r0, θ)/(A d(θ)) = α4 + β4 Δd/d and b̂5 :=
c_(5,1),vv/(i A d) = 3 b̂4 (so that the family contributes λ(b̂4 + iT0 b̂5 + …) to σ, as R7.3 normalised it). β4 carries
K's double root, so at ρ*

    b̂4(ρ*, θ) = α4(ρ*) = i (366ρ*² − 153ρ* − 934)/420 = −0.03819094879585768 i,
    b̂5(ρ*, θ) = 3 b̂4(ρ*, θ) = −0.11457284638757305 i      (μ0 = 1),

for every θ and every wave with d ≠ 0: constant, purely imaginary, nonzero (−i b̂4 is the real root of 9261000y³ +
48686400y² + 66864105y + 2483108; enclosed by interval arithmetic in B5). For μ0 ≠ 1 the seed's scaling multiplies both
by a positive power of μ0, which changes no phase. [R9, nit 5: argued by scaling; now computed at μ0 = 16 (bfam5 B6):
c_(3,0),vv = 2^(−7) A d K(r0/4), c_(4,0),vv = 2^(−9) A(α4(r0/4) d + β4(r0/4) Δd) and c_(5,1),vv = 3i c_(4,0),vv at r = 4,
exactly, so b̂4(4ρ*, θ) = 16^(−9/4) b̂4(ρ*, θ)|_(μ0=1); at other μ0 the factor μ0^(−9/4) is deduced by the same
scaling] b̂4 never lies in [0, ∞): its distance from [0, ∞) is δ_* = 0.0381909… at every angle. For the paper's wave
(T = T^G − iT^F, N6) B5 also certifies it on all of θ ∈ [0, π/2] from the general form b̂4 = α4 + β4 Δd/d, as N(ζ)/((1 +
ζ²)²|P|²) with N polynomial in ζ = cos 2θ. Control (ii) of bfam5:
with r0 frozen (∂_v not acting on r0) the family changes, c_(4,0),vv/A = α4′ d + β4′ Δd with the same β4′ = β4 and
α4′(ρ*) = +0.0037320 i in place of −0.0381909 i — R7.3's insistence on the r0-motion was needed.

**Lemma L.28 (ρ* without (H_ρ*); deduced, with edge1_5 X17).** In Proposition L.26's setting (without Theorem L_1E′'s
conditions on τ0) at ρ0 = ρ*, assume (H_N+2), (H_D) and (H_t) but not (H_ρ*)'s first half (so α > 1/2, R7.3), and δ_*
:= inf_θ dist(b̂4(ρ*√μ0, θ), [0, ∞)) > 0 (true, by the above). There are λ_28, M such that for λ ≤ λ_28 every window J
of length 4πλ in the deep layer (env ≤ λ^(P1)) has, at ω, points where g_λ⁻¹(dΦ0, dΦ0) is positive and points where it
is negative — for every N.

*Proof.* Split by the size of ν at J's left end t₀ (ν moves over J by at most 8πc_ν xλ ≪ λ). (1) *|ν(t₀)| ≥ 2M′λ*
(M′ := 16C, C the bound of |a₁|). Then |λa₁| ≤ |ν|/8 on J, which is all that L.26's step (3) and R6.1's Cases 1-3 at ρ*
take from (H_ρ*): Case 1's λ ≪ Λ (Λ ≥ M|ν|/(Γ_R|Ξ|) ≥ cMM′λ), Case 2's and Case 3 (i)'s λ ≪ |ν|, and, for N ≡ 0 mod 4,
L.26 itself. L.26's other use, |ν″| ≤ C′|ν|κ, is replaced by |ν″| ≤ 2c_ν ≤ |ν|κ^(1+α), true near v_s since x²κ^(1+α) ≥
κx/(αc_R) → ∞ (the c_R bound gives κ^α ≥ 1/(αc_R x), and κx → ∞ for α < 1); the phase bounds use |ν′| ≤ 2c_ν x ≤
C|ν|κ^α and λ/x ≤ (λc_ν/M′)^(1/2). (2) *|ν(t₀)| < 2M′λ*: |ν| ≤ 3M′λ on J, and, with a₁ = b̂4(r0, θ) + iT0 b̂5 + O(T0² +
λ) and b̂4(r0) − b̂4(ρ*) = O(x),

    A_s = ν(1 + 2iT0) + λ b̂4(ρ*) + O(λ(T0 + x + λ)),      dist(A_s, [0, ∞)) ≥ λδ_*/2   (T0, x, λ small),

because dist(z + ν, [0, ∞)) ≥ dist(z, [0, ∞)) for ν ≤ 0. Three cases, R6.1's with |ν| replaced by λ. *R1*: Γ_R|Ξ|Λ ≥
Mλ or T0 > 1: |σ| ≥ Γ_R|Ξ|Λ/2, the phase as in Case 1: Lemma W (A′). *R2*: Γ_R|Ξ|Λ ≤ λδ_*/M: T0 → 0 (Λ ≍ T0^(N−2)κ ≲
λ), |σ| ≥ λδ_*/4, and arg σ moves over J by at most 4πλ(|ν′| + C|ν|T0κ^α + Cλ(1 + T0κ^α))/(λδ_*/4) ≤ C(λ^(1/2) +
λ^(1−α)T0^(1+α))/δ_* → 0: (A′). [R9, nit 4: the
bound omits B_s's motion: |B_s′| ≤ Cλδ_*κ^α/M (L.26 (2); Γ_RΛ ≤ 2λδ_*/(c_N M) here), whose part 4πλ|B_s′|/(λδ_*/4) ≤
16πC T0κ^(α−1)/M tends to 0 too] *R3*: otherwise; T0 ≍ λ^(2/(N−1)) → 0 and λκ^(1+α) ≍ λ^(2(1+α)/(N−1)−α) → ∞ (α >
1/2 > 2/(N − 3) for N ≥ 9). Put τ := c_t δ_* λκ^(α−1)/16; |ê| ≤ C(1/κ + λ)Mλ ≪ τ. If |A_s + B_s| ≥ τ on J: |σ| ≥ τ/2
and arg σ moves by at most 8πλ·C(λ^(1/2) + λκ^α)/τ ≤ C′(λ^(1/2)κ^(1−α) + T0)/δ_* ≤ C′(λ^(α−1/2) + T0)/δ_* → 0 (κ ≤ 1/λ,
α > 1/2): (A′). Otherwise |A_s + B_s| ≤ 2τ on J, and with B_s′ = −B_s(κ − κ_(N−1))(1 + O(T0 + κ^(−α))) (L.26 (2)),

    σ′ = [ν′ + A_s(κ − κ_(N−1))] − (A_s + B_s)(κ − κ_(N−1)) + O(λκ^α(T0 + κ^(−α))) + ν st′ + λa₁′ + ê′.

Since ν′ ≤ 0 and κ − κ_(N−1) ≥ c_tκ^α > 0 (H_t), |ν′ + A_s(κ − κ_(N−1))| ≥ (κ − κ_(N−1)) dist(A_s, [0, ∞)) ≥
c_tδ_*λκ^α/2 (for real s ≤ 0 and c > 0, |s + cz| ≥ c dist(z, [0, ∞))); the rest is at most C(τκ^α + λκ^α(T0 +
κ^(−α)) + M′λT0κ^α + λ(1 + T0κ^α)) ≪ λκ^α. So |σ′| ≥ c_tδ_*λκ^α/3, while |σ″| ≤ C(1 + λκ^(1+α)) ≤ 2Cλκ^(1+α) (L.26 (2),
with |ν″| ≤ 2c_ν); Lemma W (B) as in L.26 (4) with L0 := λ³A|d| env c_tδ_*λκ^α/5: |κσ| ≤ 2κτ = c_tδ_*λκ^α/8, and |S″| ≤
L0/(80πλ) once T0 ≤ c(δ_*, c_t), the other terms of S″ (2κ|σ′| ≤ Cκ(λ^(1/2) + λκ^α), κ²|σ| ≤ 2κ²τ) being o(κ^α). ∎

*What decided it.* Nothing in (2) uses N mod 4 or c_N: the transversality is (H_t), and the direction of A_s, which b̂4
holds away from [0, ∞). b̂5 is not used. R7.3 located the obstruction at a positive real b̂4 (with N ≡ 2 mod 4), and
X15's control exhibited admissible values (|b̂4| = 0.0033, |b̂5| = 1.0·10^(−4)) for which σ and σ′ vanish together; the
computed b̂4 is −0.0382 i, of fixed phase, and is not of that kind. X17 runs X15's model (unit constants, Γ_R = 1) with
it on exp(−1/x^(1/2)) (κx² → 0) at λ = 10^(−40): every window decided at N = 9, 10, 11, 12, 13 with b̂5 = 3b̂4 (κx² from
4.7·10^(−11) to 3.5·10^(−12) and λ/|ν| from 21.8 to 7.1·10^5 at the crossover; all 122 windows of each by (A′)), and at N
= 10 also for b5 ∈ {0, ±1, ±i}. Control: X15's adversarial (b̂4, b̂5) in place of the computed ones leaves a window
undecided. [R9, nit 3: these rows do not test δ_* > 0: b̂4 rotated onto the positive real axis with |b̂4| kept and b̂5 =
3b̂4 is decided too (re-derived; X17's printed row). L.28's deduction, not these rows, carries the phase; X17's phase
rows (R9.3) show it in X15's adversarial configuration, where only the positive real phase leaves a window undecided]
*So the exclusion ρ0 = ρ* with liminf κ(v − v_s)² = 0 is removed*, under (H_N+2) and (H_t), which the record's
envelope satisfies (R8.2).

### R8.2 The hypotheses, proved for the record's envelope (task 2)

*Which envelopes.* The paper uses two. The envelope of the constants, CONSTANTS5.md R2.2 (i) (a) (`envelope5.py`): env =
c cos¹²(πy/2) exp(−y²/(1 − y²)), y = (2v − 4)/3, on [1/2, 7/2], c ≤ 1.3241035; at its left edge, x := v − 1/2 and t :=
2x/3, log env = log c + 12 log sin(πx/3) + 1 − 1/(t(2 − t)), an exp(−3/(4x)) edge. And the solver's sin⁴(π(v − ½)/3) of
section 6's numerics, which is C³ and not C⁴ at v_s (CONSTANTS5.md 1.1) and so outside Theorem 1's class env ∈ C_c^∞:
no statement of this note is made for it. X9-X16's model edge exp(−1/x) is treated beside the first.

*The reduction.* With A_j(x) := x^(j+1) ℓ^(j)(x), ℓ := log env, the complete Bell polynomial gives env^(k)/env = x^(−2k)
Q_k, Q_0 = 1, Q_(k+1) = Σ_(i≤k) C(k, i) x^i A_(i+1) Q_(k−i) (checked against the Bell polynomials, hyp5 H0), so κ =
A_1/x², κ_k = R_k/x², R_k := Q_(k+1)/Q_k, κ_k′ = −(2R_k − xR_k′)/x³, and every hypothesis is a statement about
functions of x that are analytic on [0, x0] *including x = 0*: env^(k) > 0 ⇔ Q_k > 0; κ_k/κ ∈ [1/2, 2] ⇔ R_k/A_1 ∈ [1/2,
2]; log-concavity ⇔ P_k := 2R_k − xR_k′ > 0; the c_R bound at α = 1/2 ⇔ P_k/R_k^(3/2) ≤ c_R; |κ′| ≥ c_t κ^(3/2) ⇔ (2A_1 −
xA_1′)/A_1^(3/2) ≥ c_t; L.16 (c) ⇔ |Q_j|/A_1^j ≤ c_j; (H_ρ*)'s first half ⇔ A_1 ≥ c_*. For the record's envelope A_j =
(3/4)(−1)^(j+1) j! − (3/4) j! (x/(3 − x))^(j+1) + 12(−1)^(j−1)(j − 1)! x + 12(π/3)^j x^(j+1) g^(j)(πx/3), g(z) := log(sin
z/z), analytic on |x| < 3; for exp(−1/x), A_j = (−1)^(j+1) j!.

**Proposition L.27 (the hypotheses for the record's envelope; computed, certified and exact, hyp5 H0-H5).** Let env be
the record's C_c^∞ envelope (v_s = 1/2) or exp(−1/(v − v_s)). (a) On (v_s, v_s + 1/200]: (H_N) for every N ≤ 16
[R9, nit 1: for every N ≤ 14; (H_N) includes L.16 (c) to j ≤ N + 2, certified to j ≤ 16 below; its parts for
env^(k), k ≤ 16, hold to 16] with α = 1/2 and c_R = 3.35875 (resp. 2.58122), κ_k/κ ∈ [0.74998, 1.00745] (resp.
[0.81866, 1.00301]); |κ′| ≥ c_t κ^(3/2) with c_t = 2.13951 (resp. 2.0), hence (H_t) with that c_t for N ≤ 18; L.16 (c)'s
first bound for j ≤ 16 with c_j ≤ 1.00321
(resp. 1.00001); κ(v − v_s)² ∈ [0.7499, 0.81] (resp. = 1), so (H_ρ*)'s first half with c_* = 0.7499 (resp. 1). In
particular (H_N+2) holds for N ≤ 14, i.e. K ≤ 11. (b) For every N there is x0(N) > 0 such that (H_N+2), (H_t), L.16 (c)
to j ≤ N + 2 and (H_ρ*)'s first half hold on (v_s, v_s + x0(N)]. (c) (H_D) holds for every c > 0. So every hypothesis of
Theorem L_1E‴ (R8.4) and of Proposition L.26 holds for the record's envelope, for every K ≥ 6.

*Proof.* (a) Interval arithmetic (mpmath.iv, 40 digits, outward rounding) on 400 closed intervals covering [0, 1/200], x
= 0 included; g's series exact to n = 30 with its tail enclosed by |g_n| = ζ(2n)/(nπ^(2n)) ≤ 2/(nπ^(2n)) (hyp5 H1, H2).
(b) At x = 0 every quantity takes a value strictly inside its range: Q_k(0) = A_1(0)^k > 0, R_k(0) = A_1(0), R_k′(0)
finite, so P_k(0) = 2A_1(0) > 0, P_k/R_k^(3/2) and the c_t ratio tend to 2A_1(0)^(−1/2) (2 and 4/√3 = 2.309, the value
R5.3 sampled for c_R [R9, nit 2: R4.1 sampled it, Q2 at line 1340]), Q_j/A_1^j → 1, A_1(0) = 1, resp. 3/4; computed
exactly from the recursion for k ≤ 40 (H3). The quantities being analytic at 0, each inequality holds strictly on a
neighbourhood. (c) κ(y/2) κ(4y)^c env(4y) ≤ 1.33 M(4/y²)(M/(16 y²))^c e^(1 − 3/(16y)) → 0, M := max A_1 = 0.81 on [0,
1/200] (env ≤ c e^(1 − 3/(4x))); exactly
(4/y²)(16y²)^(−c) e^(−1/(4y)) for exp(−1/x) (H4, sympy's limit with c a positive symbol). ∎

The X10 samples of round 7 (κ − κ_k ≥ 2.0 k κ^(1/2), |κ′| ≥ 1.996 κ^(3/2) on [10^(−3.5), 10^(−2)]) are superseded by (a)
and (b), which are proofs. Controls: on [0, 1/40] exp(−1/x)'s certification fails (first at env^(16)'s log-concavity near
x = 0.0081; Q_17 has its first zero at 0.01868), and the solver's sin⁴ edge fails at once (A_1(0) = 0); the recursion
without its binomials disagrees with the Bell polynomials; at x = 0 the sin⁴ edge makes nothing strict; (H_D)'s limit is
∞ for the sin⁴ edge (H0-H4's controls, all detected). H5 records exactly why the sin⁴ envelope is outside: env^(4)(v_s+)
= 8π⁴/27 ≠ 0, κ_3/κ → 1/4 < 1/2, env^(5) < 0 just above v_s.

*Consequence for L_1E‴.* Its hypotheses (H_N), (H_D), (H_N+2), (H_t) and (H_ρ*)'s first half stay hypotheses of the
theorem (a general envelope need not satisfy them), and Proposition L.27 proves them for the record's envelope and for
exp(−a/x) edges (the same argument with A_j constant); round 6's statement for exp(−a/x^q) (q > 0, α = 1/(q + 1)) stands
by the same reduction with Q_k a polynomial in x^q. The sentence of P2⁗′ "sampled for the C_c^∞ envelope ..." is replaced
in R8.5 by the proved statement.

### R8.3 λ_25 (task 3)

λ_25(δ) is computable *as a formula*, not as a number: L.25′ (a)'s proof (R6.2, R7.4) bounds every term against m0's
lower bound with the record's constants as factors, and nothing else is unknown. With λ = 10^(−E), s := ((3 +
δ) ln 10)^(1/2), n + 2 ≤ s E^(1/2) + 3 and (below λ_h) h_n ≥ λ^(3.4+δ), each condition of the proof reads −aE + b
E^(1/2) + c + γ ≤ log10 τ and holds for every E ≥ E_i := y₊², y₊ := (b + (b² + 4a(c + γ − log10 τ))^(1/2))/(2a): (W1)
Theorem 1's remainder, a = N − 8.4 − δ, b = (M* + 1) s log10 2, c = log10(27/I_β) + log10 B⁺_(M*) + 3(M* + 1) log10 2, τ
= 1/4; (M1) its means, each j ≤ N with a = j, τ = 1/(4N); (W2), (M2) Theorem 2's with N_P, M_P [R9: evaluated at β0
= 2, N_P = K + 12, as T6; in general N_P = K + 4 + ⌈4β0⌉, β0 = max(2, 4C_9 + 1) unevaluated; and (M2)'s constant is
Theorem 2's, γ_mP := log10(C_L1 C_L3P μ0/A²), which the list below omits (R9.2)]; the hypotheses ε_4(v_1) ≤
λ (L.4′) and ε_(M_P)(v_1) ≤ λ³ (L.4_P), a = 2 + δ and δ; λ ≤ λ_h(δ); the tail condition e^(2n+1) ≥ 2^(M_P+1); and J_n′
longer than 4πλ, with γ = log10(4π + C_ρ). So

    λ_25(δ) = min(λ_rec, 10^(−E_25)),   E_25 := max_i E_i(δ, γ_i),

with B_k ≤ B⁺_k := max_(i≤k) (2i/e)^(2i) ‖p_i‖₁ (certified: β^(i) = e^(−1/u) p_i(t)/u^(2i), u = 1 − t², e^(−1/u) u^(−2i)
≤ (2i/e)^(2i)) and I_β ≥ 0.133018 (a right-endpoint sum, β² decreasing on [0, 1)). **Computed (certified coefficients,
lam25_5 L1, L2):** with unit constants (every γ = 0), K = 6: E_25 = 130159.1 at δ = 1/10 (binding: L.4_P's hypothesis,
a = δ) and 55868.9 at δ = 1/2 (binding: W1, a = N − 8.4 − δ = 0.1); with R5.5's illustration log10 C_L4 ≈ 1.8·10^6 (every
leaf 1, every other constant 1): E_25 = 3683621 at δ = 1/10 and 19007279 at δ = 1/2, binding W1. L3 evaluates every
condition directly (actual n, h_n) at 200 points beyond E_25: all hold; control: a lost factor ½ in the s_n bound gives a
threshold at which a condition fails (detected).

*What a number needs* (precisely): γ_w = log10(C_L1 C_L4 μ0/A²), γ_m = log10(C_L1 C_L3 μ0/A²), γ_wP = log10(C_L1 C_L4P
μ0/A²), C_ρ, and λ_rec — Lemma L.1's constant C_L1 (the expansion of g⁻¹ at the boundary), L.3 (b)'s C_L3 (the means),
L.4′'s C_L4 (R5.5's formula in λ0's leaves), L.4_P's C_L4P, L.4′'s reach ρ_w ≤ C_ρ λ, and the threshold λ_rec below
which g_λ exists and L.3 (b), L.4′, L.4_P hold (λ0's, for Theorem 1). These are the leaves λ_L also waits for (R5.5,
R5.6): with them λ_25 is a number. [R9, m1: not shown here. Only C_L4 is R5.5's formula in λ0's leaves (and C_L3 is
R5.5's unnamed node Cb_m); C_L1, C_L4P, C_ρ and λ_rec were not written out, and C_L4P, C_ρ's Theorem-2 half and λ_rec
(through
λ_P, C_P) are Theorem 2's constants, which are not λ0's leaves. All are written out in R9.1, with C_L1 certified; with
them λ_25 is a formula with every coefficient certified, and λ_25 itself is certified below 10^(−6613.6) (R9.2)] R7.4's
sentence ("an effective threshold would need a bound for w on a zero interval without the derivative loss") is
withdrawn: the derivative loss enters E_25 only through b√E and c, and is computed.

### R8.4 Theorem L_1E‴: no exclusion left

**Theorem L_1E‴ (Theorem 1's deep layer and very edge; deduced from L_1E″'s proof, Proposition L.26 and Lemma L.28).**
As Theorem L_1E″ (R7.3) — reading 2 cited now as N1STAR-PROOF.md section 4, step (ii), "Z := d_tau - beta_ext", from
line 497 at md5 88179da4…, a live file — with its two conditions on τ0 replaced by

    if N ≡ 0 mod 4 and ρ0² = 2N − 1:   (H_N+2) and (H_t);
    if ρ0 = ρ*:                         (H_N+2) and (H_t), except when N ≢ 0 mod 4 and κ(v)(v − v_s)² ≥ c_* > 0.

Then L_1E's conclusion holds for every admissible τ0: there are λ_1E > 0, x0′ ∈ (0, x0] and P1 such that for λ ≤ λ_1E,
every v ∈ (v_s, v_s + x0′] with env(v + 4πλ) ≤ λ^(P1) and every ω ∈ S³, on [v, v + 4πλ] the boundary x_K = 1 has, at
ω, points where it is timelike for g_λ and points where it is spacelike; with L.12 (ii), every such interval below
λ^(3+δ). *Proof.* L_1E″'s, and at ρ* without (H_ρ*)'s first half Lemma L.28 ((1) for the windows with |ν| ≥ 2M′λ, (2)
for the rest). ∎

*The exclusions, all gone.* ρ0² = N − 1: removed (R7.1 (c)). ρ0² = 2N − 1 with N ≡ 0 mod 4: removed under (H_N+2), (H_t)
(R7.2). ρ0 = ρ*: with κx² bounded below as R7.2-R7.3; without it, under (H_N+2), (H_t), by Lemma L.28, b̂4 being
computed (R8.1). Reading 3's ρ0² = 2: irrelevant (R7.3). For the record's envelope every hypothesis of L_1E‴ is proved
(Proposition L.27), so for the paper's data the theorem holds for every K ≥ 6 and every admissible τ0. What a general
envelope must satisfy is stated with the theorem ((H_N), (H_D), and (H_N+2), (H_t) at the two τ0 above); the sin⁴
envelope of the solver is outside Theorem 1's class altogether (C³, R8.2).

### R8.5 Final paper text (replaces R7.6's P1⁗′ and P2⁗′; P3-P6 stand, P3's list extended)

Each old text is generated from its quoted start and end strings in RESPONSE-HL-5D.md at md5 4c121081… (the file as it
now stands; the same texts as at 5930486d…), never from line numbers, by `wsE5/r8/paper/gen_old.py`, which checks that
each occurs exactly once; the splice is simulated (the two-dust bullet before P2 intact, every line ≤ 121; the spliced
file would have md5 25a5f219…). Copies: `wsE5/r8/paper/old1.txt`, `new1.txt`, `old2.txt`, `new2.txt`. Re-checked at
the end of the round, the paper having moved again to md5 b21cd7ca…: both old texts occur once, at the same lines and
with the same content md5s, and the simulated splice gives fb8308f7…, the two-dust bullet intact. [R9, nit 6:
fb8308f7… is the splice at b21cd7ca…; at 805be200… (the paper as it now stands, the old texts unchanged, lines 302-305
and 1547-1555) these texts give 46f943fb…; R9.4's texts replace them]

(P1, final) Proposition 3.2: the old text from "R13). If μ0 = √72 l5² exactly, the" to "Propositions E.2-E.4)."
(lines 302-305 at 4c121081…; md5 397a2813…) occurs once and is replaced by:

> R13). If μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the
> shell starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
> `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that layer, for λ small, every column has points
> where it is timelike for g_λ, so the no-return property stated above for μ0 > √72 l5² fails at equality
> (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L, L_P, L_E and L_1E‴, Corollary L.7).

(P2, final) Section 9: the old text from "- **The boundary at equality.** If μ0 = √72 l5² exactly (computed," to "with
√μ(v) − r_q(v) ≥ C' λ." (lines 1547-1555 at 4c121081… and at 5930486d…; md5 ca1f042d…) occurs once and is replaced by:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced in `docket68/n1star/EQUALITY5.md` and `EQUALITY5-LAYER.md`,
>   whose rounds 1-7 independent verifiers have read and whose round 8 awaits a reader; computed by the programs of
>   Appendix A), x_K = 1 is the seed's horizon on {v ≤ v_s}, v_s := inf supp env, and is spacelike for g_λ on {v ≥ v_s +
>   η} once λ ≤ λ_η. In the layer between, for λ small and 0 < δ ≤ 1/2, it is spacelike where sup_(v'≤v) env ≥ λ^(3−δ),
>   and where λ^(3+δ) ≤ sup env ≤ λ^(3−δ) its character is that of the ratio of λ³ A env |ν| |d| to the margin, up to a
>   factor 1 ± 2λ^(1/10) (d the double divergence of the waves' angular tensor, |d| ≥ 8/3; ν ≤ 0 a coefficient of the
>   seed and τ0, with a double root at (v_s − τ0)/√μ0 = ρ* = 1.806…). Suppose that near v_s env and its first K + 5
>   derivatives are positive and log-concave, with logarithmic derivatives κ_k within a factor 2 of κ := (log env)′,
>   |κ_k′| ≤ c κ_k^(1+α) for an α < 1 and |κ′| ≥ c′ κ^(1+α), and that env obeys the derivative and decay bounds of
>   `EQUALITY5-LAYER.md` R5.2 and R6.1; the C_c^∞ envelope used for the constants satisfies all of these, with α = 1/2,
>   for every K (proved, `EQUALITY5-LAYER.md` Proposition L.27). Then that ratio crosses 1 once per column, and below
>   λ^(3+δ), down to v_s, every interval of length 4πλ has timelike and spacelike points on every column, for every
>   admissible τ0 (at ρ* this uses the next family of the term linear in the waves, computed: `EQUALITY5-LAYER.md` R8.1);
>   the term linear in the waves is computed there to leading order, on the very edge, for Theorem 1, carried by the
>   constraint correction at first degree. For some envelopes whose intervals of zeros accumulate at the edge
>   (`EQUALITY5-LAYER.md`, Proposition L.25″ (a)), intervals of length 4πλ below λ^(3+δ) on which x_K = 1 is spacelike
>   throughout occur for every small λ. So timelike curves of g_λ cross x_K = 1 into D_T. A domain O(λ)-close to D_T,
>   inside x_K ≤ 1, has an inner boundary that no future causal curve enters, and the spheres' horizon holds in the form:
>   at most one zero per column, within C λ of √μ(v); exactly one on the columns with v ≤ v_s and on those that reach
>   across √μ(v) + C λ with √μ(v) − r_q(v) ≥ C' λ. The threshold λ_L of Theorem L's proof is an explicit formula in the
>   leaves of λ0, two constants of the seed and Theorem 1's C1, and is below 3·10^(−12); the thresholds of the finer
>   statements (λ_η above and those named in `EQUALITY5-LAYER.md`) depend on constants of the approximant that the record
>   does not certify, λ0's leaves among them, and are not evaluated (for the dips, λ_25 is written as a certified formula
>   in those constants, `EQUALITY5-LAYER.md` R8.3).

Sources: the layer and band, L.12 (i), (iii) (A24); the single crossing, L.24; the intervals below λ^(3+δ), L.12 (ii)
with L_E (Theorem 2; A25) and L_1E‴ (Theorem 1; R8.4); the hypotheses for the C_c^∞ envelope, Proposition L.27 (R8.2);
ρ*, Lemma L.28 and R8.1; the linear term, L.15_P (b) and L.22′; the dips, L.25″ (a); λ_25, R8.3; the crossing curves,
Corollary L.7; the inner boundary and the spheres' horizon, EQUALITY5.md Propositions E.4, E.5; λ_L, R5.5, R5.6. (P3,
final) Appendix A, C, D: `checks/edge1_5.py` X1-X17, `checks/degtwo5.py` T1-T7, `checks/constL5.py` K1-K4,
`checks/bfam5.py` B1-B5, `checks/hyp5.py` H0-H5, `checks/lam25_5.py` L1-L3, with the run times of their `.out` files and
their controls as in their docstrings; P5's commands for bandL4p5 and lamL5b stand.

### R8.6 Amendments, programs, labels, runs, sources

- **A43** (task 1). R7.3's Theorem L_1E″ is superseded by L_1E‴ (R8.4); R7.3's bullet "ρ0 = ρ* with liminf κ(v −
  v_s)² = 0" by R8.1 (b̂4, b̂5 computed; Lemma L.28).
- **A44** (task 2, m1). R7.2 (b)'s "X10 samples them" and R6.1 Remark (2)'s "sampled" are superseded by Proposition
  L.27; the round-7 sites that read as unconditional carry the conditions (notes "[round 8, m1: …]").
- **A45** (task 3). R7.4's "λ_25(δ) is not evaluated: an effective threshold would need …" is withdrawn (R8.3).
- **A46** (M1). R7.0, R7.6 and R7.7: P2's old text is at lines 1547-1555, not 1533-1541; every old text is generated
  from its bounds (R8.5).
- **A47** (m2, m3, nits 1-12). X14 at λ = 10^(−40), 10^(−80) only; the readings of R8.0, each by a note "[round 8, …]"
  at its site in R7.0 (V6-m1, V6-n4, V6-n7, V6-n11), R7.1 (c), R7.2 (a)-(d), R7.3, R7.5, R7.6, R7.7.
- **Programs.** New: `checks/bfam5.py` (B1-B5, two controls), `checks/hyp5.py` (H0-H5, a control each),
  `checks/lam25_5.py` (L1-L3, a control). Changed: `checks/edge1_5.py` (X14 without its 10^(−160) rows, X15's control
  printed, X17 new). Unchanged: degtwo5, constL5, lamL5b, bandL4p5, layerlin5 (their `.out` stand).
- **Labels.** Computed, exact: bfam5 B1-B4 and B5's forms, hyp5 H0, H3-H5; certified (interval arithmetic): bfam5 B5's
  values and the paper's-wave decision, hyp5 H1, H2, lam25_5 L1, L2 (a formula with certified coefficients, evaluated
  with unit constants and with R5.5's illustration); computed, sampled: lam25_5 L3; computations with unit constants:
  X14, X15, X17. Deduced: Proposition L.27 (b), Lemma L.28, Theorem L_1E‴, R8.3's formula.

*Open items.* None in section 9's sense: Theorem L_1E‴ has no exclusion, every hypothesis it states is proved for the
envelope the paper uses, and the thresholds λ_η, λ_U, λ_E, λ_1E, λ_26, λ_28 are not evaluated for the reason the paper
gives (they depend on λ0's leaves, which the record does not certify), λ_25 being written as a formula in them. [R9,
m1: they depend on constants the record does not certify, λ0's leaves for Theorem 1 and Theorem P's for Theorem 2;
λ_25's inputs are written out in them in R9.1, and λ_25 is certified below 10^(−6613.6), R9.2] O2:
round 8 awaits an independent reader.

Runs (full, each `.out` beside its program, under a load average between 11 and 28 on four cores): bfam5 B1-B5 under
PYTHONHASHSEED = 0, two runs byte-identical, about 2870 s each (`.out` md5 d9e0d744…, program dcce2a37…); hyp5 H0-H5, two
runs byte-identical, 804 s and 801 s (67e5484b…, 0ec4da5a…); lam25_5 L1-L3, two runs byte-identical (4bab471a…,
cfd69ab4…); edge1_5 X1-X17, one run, 2187 s (6fec900e…, 1683ee60…; it prints its times, so two runs differ there; its
X1-X16 rows repeat round 7's apart from X14's dropped rows and X15's printed control). Every check passes and every
control fails.

READ: the reader of round 7's report (`scratchpad/report-vE7.md`); RESPONSE-HL-5D.md at md5 4c121081… (P1 lines 302-305,
P2 lines 1547-1555, located by content); N1STAR-PROOF.md at 88179da4… (the phrase from line 497); CONSTANTS5.md at
b9617854… (R2.2 (i) (a)'s envelope and its peak c ≤ 1.3241035; 1.1's sin⁴ remark); layerlin5.py (its `ops`, `polplus`,
`DIV2`, N5's K, N6's closed forms), edge1_5.py's X15 model. The live files at the end of the round: RESPONSE-HL-5D.md
b21cd7ca…, N1STAR-PROOF.md 5043cedf… (the phrase still from line 497), CONSTANTS5.md 1d92d5f7…. [R9, nit 7: re-measured
at round 9: RESPONSE-HL-5D.md 805be200…, N1STAR-PROOF.md 5c1a186a… ("Z := d_tau - beta_ext" still from line 497),
CONSTANTS5.md unchanged] File md5 before this round: 5f1739c3….

## Round 9 (2026-11-13)

This round seats the reader of round 8, who confirmed it (no major finding; one minor, seven nits), each finding
re-derived (R9.0). It writes out every input of λ_25 that round 8 named and left unwritten — C_L1, C_L3, C_L4P, C_ρ and
λ_rec, with C1, C_P and λ_P beneath them — each traced through its lemma's proof, C_L1 certified (R9.1); settles what
λ_25 is: an explicit formula whose remaining inputs are λ0's leaves and Theorem 2's constants, which the record does not
certify, and which is certified below 10^(−6613.6) whatever they are (R9.2); computes what the nits asked for (R9.3:
X17's phase rows, bfam5 at μ0 = 16); and gives the paper texts in final form (R9.4). Earlier text stands, with bracketed
notes "[R9, …]" at every amended site.

### R9.0 The reader of round 8, seated (each finding re-derived)

READ (as relayed, and its report `scratchpad/report-vE7r8.md`): round 8 confirmed — b̂4, b̂5 and β4(ρ*) = 0 (b̂4
re-derived by an independent program from layerlin5's covariant operators), Lemma L.28 line by line (the (B) branch
reachable in a model), hyp5's certification and its analytic-at-0 reduction, lam25_5's formula, X17 and both splices;
bfam5 and hyp5 reproduced byte-identically, edge1_5 and lam25_5 apart from their times.

- **m1 (λ_25's constants).** Confirmed by reading R5.5: its display writes C_L11 and C_L4 in λ0's leaves, and L.3 (b)'s
  constant only as the node Cb_m of its recursion, unnamed; Lemma L.1's C_L1, L.4_P's C_L4P, the reach C_ρ and λ_rec are
  written nowhere, and C_L4P, the Theorem-2 half of C_ρ and λ_rec (through λ_P and C_P) are constants of Theorem 2's
  construction, which are not λ0's leaves at all. So "these are the leaves λ_L also waits for" (R8.3) and "they depend
  on λ0's leaves" (R7.7's note, R8.6) were not shown. Repaired at the three sites ("[R9, m1: …]") and by doing the work:
  R9.1 writes all five out, R9.2 states what λ_25 is. Reading R8.3 again for this, two more gaps (R9.2): (M2)'s constant
  is Theorem 2's (γ_mP), which its list omits, and its Theorem-2 rows take β0 = 2.
- **Nit 1.** Confirmed: (H_N) of R6.1 (d) includes |env^(j)| ≤ c_j κ^j env for j ≤ N + 2, which hyp5 certifies to j ≤
  16; so L.27 (a) gives (H_N) for N ≤ 14 (note at L.27 (a)); its sentence on (H_N+2), K ≤ 11, stands.
- **Nit 2.** Confirmed: the sample c_R = 2.309 is R4.1's (L.16's Q2, line 1340); note at L.27's proof.
- **Nit 3.** Re-derived: X17's rows with b̂4 replaced by +|b̂4| and b̂5 = 3|b̂4| are decided (N = 9 and 10; N = 10 is
  now printed by X17). So those rows do not test δ_* > 0, and R8.0's "the phase of b̂4 keeping σ from zero" was wrong:
  |λb̂4| against |ν| at the crossover keeps σ there, whatever the phase. Repaired both ways the reader allows: the text
  says that L.28's deduction carries the phase (notes at R8.0 (8) and R8.1), and X17 gains rows in which the phase alone
  decides (R9.3 (a)).
- **Nit 4.** Re-derived: in L.28 (2) R2, |B_s′| ≤ Γ_R Λ(|Ξ_ex′| + |Ξ_ex||κ − κ_(N−1)|) ≤ Cλδ_*κ^α/M (L.26 (2), |Ξ_ex| ≥
  c_N/2, Γ_R|Ξ_ex|Λ ≤ λδ_*/M, κ ≥ 1), which adds 4πλ|B_s′|/(λδ_*/4) ≤ 16πC T0κ^(α−1)/M → 0 to arg σ's motion over J;
  added at its site. The conclusion stands.
- **Nit 5.** Done by computation: bfam5 B6 runs the chain at μ0 = 16 (R9.3 (b)); the general μ0 stays deduced.
- **Nit 6.** Re-measured: at 805be200… (the paper as it now stands) both old texts occur once, at lines 302-305 and
  1547-1555, content md5s 397a2813… and ca1f042d…, and R8.5's texts would give 46f943fb… (fb8308f7… was at b21cd7ca…);
  note at R8.5. R9.4's texts supersede them.
- **Nit 7.** Re-measured: N1STAR-PROOF.md 5c1a186a… ("Z := d_tau - beta_ext" still from line 497), CONSTANTS5.md
  1d92d5f7…; note at R8.6.

### R9.1 The inputs of λ_25, written out (m1)

On J_n′ the oscillating profiles vanish (L.25″ (a)'s step (1)), so k := g_λ − g0 = Σ_(j≥1) λ^j m_j + w there, and step
(4) bounds |g_λ⁻¹(dΦ0, dΦ0) + m0| ≤ C_L1|k| ≤ C_L1(Σ_j λ^j C_L3 ε_(2j)(v)² + C_L4 λ^(N−5) ε_(M*)(v_1)) for Theorem 1
(C_L3P, C_L4P, N_P, M_P for Theorem 2). |·| of an array is the Frobenius norm of its Cartesian components (the norm of
L.4's energies and of Lemma 2.1's C_S), which bounds the operator norm used below. Each input is a formula traced
through its lemma's proof; `checks/lamconst5.py` C1-C5 computes or certifies it (R9.5).

(a) **C_L1 (Lemma L.1; certified).** N0's identity g_λ⁻¹ = g0⁻¹ − g0⁻¹ k g0⁻¹ + g0⁻¹ k g0⁻¹ k g_λ⁻¹, contracted with dΦ0
twice, gives g_λ⁻¹(dΦ0, dΦ0) + m0 = −k(Φ0♯, Φ0♯) + Φ0♯·k g0⁻¹ k g_λ⁻¹ dΦ0; with |g_λ⁻¹| ≤ n_b/(1 − n_b|k|),

    |g_λ⁻¹(dΦ0, dΦ0) + m0| ≤ C_L1 |k|,       C_L1 := |Φ0♯|² + |Φ0♯| |dΦ0| n_b² ε1/(1 − n_b ε1),

where |k| ≤ ε1 (on Ω for λ ≤ λ0, Step 3 of λ0's proof; for λ ≤ λ_P, λ_EP below), ε1 the construction's fixed number, 0 <
ε1 < s0, s0 ∈ [0.030768559, 0.030768560] g0's least absolute eigenvalue on Ω (CONSTANTS5 Round 4; N1STAR-PROOF.md 0.3),
and n_b := 1 + 2μ_end/μ0 ≥ |g0⁻¹| at the boundary (g0⁻¹ = η⁻¹ − (μ/r²) L ⊗ L, |L|² = 2, r = r_q ≥ √μ0); C_L1 increases
with ε1, so its value at ε1 = s0 bounds it for every admissible ε1. In Cartesian components Φ0♯ = ∂_v + β0 ∂_r = (1 −
β0)∂_τ + β0 x̂·∂_x and dΦ0 = −r_q′ dτ + (1 − r_q′) x̂·dx, so |Φ0♯|² = (1 − β0)² + β0², 0 ≤ −β0 ≤ (√(μ_end/μ0) − 1) +
A²c²/(18√μ0), and |dΦ0|² = r_q′² + (1 − r_q′)² ≤ 1 (0 ≤ r_q′ = r_q μ′/(4μ) ≤ A²c²/(18√μ0) ≤ 1, μ′ = (2/9)A² env², env ≤
c). At P* (μ0 = A = 1, μ_end = 227/192, c ≤ 1.3241035): sup r_q′ ≤ 0.0974028, |β0| ≤ 0.1847352, |Φ0♯|² ≤ 1.437725, n_b ≤
3.364584, n_b²s0/(1 − n_b s0) ≤ 0.388536, and

    C_L1 ≤ 1.9036       (certified, lamconst5 C1, every admissible ε1; log10 C_L1 ≤ 0.27958),

1.44488 at CONSTANTS5 1.4's ε1 = 5.2617·10^(−4). C1 also takes the exact ratio at 400 boundary points (μ ∈ [μ0, μ_end],
μ′ ∈ [0, (2/9)A²c²], the Kerr–Schild g0 in Cartesian components) for four k each, two adversarial (∓s0 uu^T, u along
Φ0♯) and two random, |k| = s0: at most 0.924 of the pointwise constant and 0.791 of C_L1. Control: without its quadratic
term (pointwise |Φ0♯|²) the bound is exceeded at an adversarial k.

(b) **C_L3 (L.3 (b); Theorem 1).** C_L3 := max_(m≤N) Cb_m, Cb_m = C_N C_E e^(C_E T)(Ce_m + T K (sa_m² + sb_m) + T K
Ca_(m+1)(1 + sa_m)) the (b) line of R5.5's recursion: a formula in λ0's leaves (lamconst5 C2, on constL5's DAG: its
leaves are λ0's P6, C64, C0, M, C2, λ0 and the seed's K_s, C_S3).

(c) **C1 and C_ρ (EQUALITY5 section 0; L.4′ and L.4_P, step 1).** C1 is "from C and the bound of g0⁻¹" (EQUALITY5
section 0): |g_app − g0| ≤ C_app λ and |w| ≤ 2 C_inf M λ^(K−3) (Step 3 of λ0's proof, CONSTANTS5 1.3), |g_λ⁻¹ − g0⁻¹| ≤
|g0⁻¹ k g_λ⁻¹| ≤ |k|/(s0(s0 − |k|)) (|g0⁻¹| ≤ 1/s0, and |g_λ⁻¹| ≤ (s0 − ε1)⁻¹ as Lemma 2.3 carries it), so

    C1 := ι (C_app + 2 C_inf M λ0^(K−4)),     ι := 1/(s0(s0 − ε1)),

a formula in λ0's leaves (C2; ε1 is one, s0 certified). L.4's region {v + 2C1λ(τ − τ0) ≤ v1} contains the boundary point
(v, r_q(v), ω) once v1 ≥ v + 2C1λ(v − r_q(v) − τ0), and v − r_q(v) ≤ τ_end on Ω; L.4_P's region {v + 2C_Pλψ(τ) ≤ v1}, ψ
= 2 + τ − τ0 on Ω, likewise. So

    C_ρ := max(2 C1 (τ_end − τ0), 2 C_P (2 + τ_end − τ0)).

(d) **λ_rec.** λ_rec := min(λ0, 1/(2C1), λ_P, 1/(2C_P), λ_kP), λ_kP := ε1/(C_kP + C_Piii) (R9.1 (e)): g_λ exists for λ ≤
λ0 (Theorem 1), λ ≤ λ_P (Theorem 2); L.4′ and L.4_P need s = C1λ, C_Pλ ≤ 1/2 (step 1); |k| ≤ ε1, which Lemma L.1's C_L1
and the derivations of C1 and C_P use, holds on Ω below λ0 (Step 3) and λ_P (λ_EP) and on P below λ_kP. Nothing else in
L.25″ (a)'s proof asks for λ small beyond R8.3's conditions: L.3 (b)'s ball condition for U (R2.3 (e)), 4 C_b C0 λ^(N−3)
ε_(2N+2) ≤ 1, is λ0's ninth term once ε_(2N+2)(v_1) ≤ 1, which (H2) gives (ε_(2N+2) ≤ ε_(M_P) ≤ λ³); v_1 ≤ v_♯ follows
from (J) (C_ρλ ≤ 2^(−n−2)); L.3_P holds for every λ ≤ 1 (Theorem A_P).

(e) **Theorem 2's: C_P, C_L3P, C_L4P and λ_P (transcribed from L.3_P, L.4_P and N1STAR-PROOF.md sections 9.1-9.4).** The
supplement states λ_P only as existing ("there are lam_P > 0 and C"); its proof fixes every step, and with the constants
each step names:

    β0 := max(2, 4C_9 + 1),   N_P := K + 4 + ⌈4β0⌉,   K′ := N_P − 1,
    M_F := 4 C_F e^(6C_F) C_R + 1   (9.8),        M_N := 8 C_9 C′ (M_F + C_R + 1)   (9.9: B = M_N λ^K′),
    C_Piii := C_93 max(2M_F, M_N (1 + C_kP))   ((P-iii) by Lemma 9.3 (a); the φ-part through ∂_θ g1 ∈ E_(3/2)),
    M_EP := C3 (M_N + 1 + C_RO) + 1   (Theorem E's M at the trace data N_P(τ0) ≤ M_N λ^(K′−2β0): λ0's M, C_D := M_N),
    C_P := ι (C_kP + max(C_Piii, 2 C_inf M_EP)),
    C_dP := C_E5 K_P^(N_P+1) (1 + S_aP + S_bP)^(N_P+1)/(N_P − 2)!,     C_E5 := π (2 d1)^(1/2) ≤ 15.0254,
    C_L4P := C_S e^(C2 (1 + M_EP + K_ΩP) T) (2 C_95 e^(2 C_95 C_k4) C_dP + T C_dΩP),

with C_L3P := max_m Cb_m^P and C_dΩP := Cd^P from L.3's recursion on Ω (R5.5) with each stage's slice data replaced by
L.3_P's trace constant Tr_m on Σ_τ0, and P6 by P6P (L.3_P's last item: on Ω, (a)-(d) of L.3 with (e) replaced by the
traces). C_P: on P, |k| ≤ (C_kP + C_Piii) λ t^(−3/2), on Ω, |k| ≤ (C_kP + 2 C_inf M_EP) λ (λ ≤ 1). C_dP: L.3_P (d_P) is
L.3 (d) with E5's L² norm of an E_3 profile on A_P(τ) (r ≥ t + a1, thickness ≤ d1 := V_P − v_s, so the norm is at most
π(2d1)^(1/2) t^(−3/2) times the class constant). C_L4P: L.4_P's (2) no data; (3) the kernel C_k4 t^(−3/2) on P, which
Lemma 9.5 turns into e^(2C_95 C_k4); (4) the source C_dP λ^(N_P−3) ε t^(−3/2), integrated to 2C_dP; then Lemma 2.3 on Ω
as L.4's step 6 (R5.5's e^(C2(1+M+K)T) with M_EP) and step 7's C_S. And

    λ_P := min{λ1, d0/20, 1, λ_F, λ_mF, λ_N, λ_abs, λ_mN, λ_EP},
    λ_F := (8 C_F² e^(6C_F) M_F)^(−1/(K′−5))     (9.8's bootstrap closes: C_F e^(6C_F) C_F (2M_F)² λ^(K′−5) ≤ M_F/2),
    λ_mF := min(ε_P/(2ι C_kP), (ε_P/(4ι C_93 M_F))^(1/(K′−3)))     (Lemma 9.1 (f)'s margin on the far region),
    λ_N := (4 C_9 M_N)^(−1/(K′−8−4β0))     (9.9's nonlinear terms: C_9 B² λ^(−8−4β0) ≤ B/4),
    λ_abs := 1/(8 C_abs)     (9.9: the terms with a profile g_j, j ≥ 3, absorbed),
    λ_mN := (ε_P/(2ι C_93 M_N (1 + C_kP)))^(1/(K′−3−2β0))     (the margin on the near region),
    λ_EP := min(ε1/(2C_kP), (min(ε1, ε2)/(4 C_inf M_EP))^(1/(K−3)), (2 C_dw M_EP)^(−1/(K−4)), 1/(C3 C_nl M_EP²))
                                             (Theorem E on Ω, (P-iv): λ0's Steps 3 and 7 with M_EP),

λ1 = min(1, δ0)/10 ≥ 0.026985 and d0 ≥ 10.9372 certified (section 9.2). lamconst5 C3: every leaf is Theorem P's (below),
λ0's (C2, C3, C_dw, C_inf, C_nl, ε2, ε1 and ι), the seed's (K_s, C_S3) or certified; C_P, C_ρ, C_L3P, C_L4P increase,
and every term of λ_P decreases (ε_P: increases), in every leaf at fixed β0; an independent transcription agrees to
10^(−30) at 20 points (controls: L.4_P's factor 2 dropped, λ_N's exponent with 2β0 for 4β0, and a planted leaf, each
detected). C4, the census of N1STAR-PROOF.md sections 9.1-9.4 at 5c1a186a…: 31 lines carry a threshold phrase (lam_X,
"small", "absorb", eps_P, eps_U, lam1, d0/20, "lam <= 1", "there is/are", "margin of Lemma 9.1", "Theorem E with this
K"), 23 of them a term of λ_P and 8 setting none (β0's existence, ε_U's class, a local step in τ, an exponent count, an
identity of (9.9b), Lemma 9.5's hypothesis, an amendment note); every term of λ_P has its line (control: a planted "for
lam small enough by compactness" stays unclassified). Theorem P's leaves: C_kP, C_R, C_RO, K_P, S_aP, S_bP, P6P and
Tr_1, …, Tr_(N_P) (Theorem A_P's profile classes on P and their continuation on Ω), C_F, C_9, C′, C_abs (the bootstrap
constants of 9.8, 9.9), C_93, C_95, ε_P (Lemmas 9.3 (a), 9.5, 9.1 (f) on P) and C_k4 (L.4_P's kernel). The seed's C_S3
(L.10, H²(S³) ⊂ L^∞) is certified here: by harmonics, (Σ_(|β|≤2) ‖Ω^β u‖)² ≥ ‖u‖² + ⟨−Δu, u⟩ + ‖Δu‖²/6 (the six squares
Ω_ab², Cauchy–Schwarz) and sup|u_k| ≤ (k + 1)|S³|^(−1/2)‖u_k‖, so C_S3² ≤ Σ_k (k + 1)²/(2π²(1 + k(k + 2) + k²(k +
2)²/6)), and C_S3 ≤ 0.434955 (C2, the tail bounded; control: without the ‖Δu‖² term the sum grows linearly).

(f) **Where a number is blocked, exactly.** Every input of λ_25 is now a written formula. Three sets of leaves are not
numbers, and each is blocked at a named step:
- *λ0's leaves* (the profile bounds P6, C64, C0, C2, C_app, C_inf, C_dw, C_nl, ε2, the choice ε1 < s0; the nodes M, C3,
  ι and λ0 itself): at the step CONSTANTS5 1.5 names — a certified solve of the nine stages of Lemma 5.3 on Ω (a wave
  equation for each mean, transports for the phases and the oscillating profiles, Lemma 6.2's data through Lemma 6.4's
  solve on Σ) with derivative bounds to order about 11, and for ε2 a concrete extension g_ext. No program of the record
  solves the stages (CONSTANTS5 R8.2's enclosure of stage 1 was attempted and not obtained); λ0 has certified upper
  bounds (0.0024433 operator norm, 0.0019079 Frobenius, 0.0012228 largest entry; LAMBDA0-DATA5.md), not a value.
- *Theorem P's leaves*: at the same kind of step on the past domain — Theorem A_P's stages solved from past null
  infinity (transports from infinity, the means' energies on P) with their class constants; 9.8's C, 9.9's C, C′ and
  absorption constant are "built from the bounds of g0, g1, g2 ..., from P and from Lemmas 9.3-9.6 and 9.4b"
  (N1STAR-PROOF.md 9.9), and β0 = max(2, 4C_9 + 1) with them, so even N_P is not known. The geometric three (C_93, C_95,
  ε_P) are computable as CONSTANTS5 computed C_S and ε1 for Ω; they are not computed here, since with the profile
  classes open they would not make λ_25 a number.
- *The seed's K_s* ("the bound of the seed's operator coefficients on Ω with two derivatives", R5.5): a property of the
  explicit seed, but the record does not fix the operator and norm it bounds; computable once they are fixed, not
  computed.

### R9.2 λ_25: what it is

λ_25(δ) = min(λ_rec, 10^(−E_25(δ))), E_25 := max_i E_i(δ, γ_i) (R8.3), with γ_w = log10(C_L1 C_L4 μ0/A²), γ_m =
log10(C_L1 C_L3 μ0/A²), γ_wP = log10(C_L1 C_L4P μ0/A²), γ_mP = log10(C_L1 C_L3P μ0/A²), γ_J = log10(4π + C_ρ), and
λ_rec, C_ρ, C_L3P, C_L4P of R9.1. *Two corrections to R8.3* (notes there): (M2)'s constant is Theorem 2's means on Ω
(γ_mP; its list named only γ_m), and its (W2), (M2), (H2), (Tl) are written at N_P = K + 12, i.e. β0 = 2, as T6 took it,
while the supplement's N_P is K + 4 + ⌈4β0⌉ with β0 = max(2, 4C_9 + 1) unevaluated.

**Status: λ_25 is not a certified number.** Its formula is explicit with every coefficient certified (lam25_5 L1,
lamconst5 C1, C5); its value needs λ0's leaves, Theorem P's leaves and K_s (R9.1 (f)), which the record does not
certify. **Certified, whatever those leaves are** (lamconst5 C5): the conditions whose γ involves no uncertified leaf —
(H1), (H2), (Lh), (Tl), and (J) with γ_J ≥ log10(4π) — give E_cf(δ) ≤ E_25(δ), so

    λ_25(1/10) ≤ 10^(−130159.0),     λ_25(1/2) ≤ 10^(−6613.6),     λ_25(δ) ≤ 10^(−6613.6) for every δ ∈ (0, 1/2],

binding (H2), L.4_P's hypothesis ε_(M_P)(v_1) ≤ λ³, at β0 = 2. They hold for every β0: E_H2 increases with β0 (130159.0,
142080.1, 180961.0, 307495.9 at β0 = 2, 9/4, 3, 5 for δ = 1/10; 6613.6, 7194.3, 9079.3, 15151.5 for δ = 1/2). And E_H2
decreases in δ: at E = E_H2(δ) and δ′ < δ, f_δ′(E) − f_δ(E) = (δ − δ′)E − (b(δ) − b(δ′))√E ≥ (δ − δ′)√E(√E − c_b) > 0
(√(3 + δ) − √(3 + δ′) ≤ (δ − δ′)/(2√3), c_b := M_P log10 2 (ln 10)^(1/2)/(2√3) ≤ 5.803), since √E ≥ b(0)/δ ≥ 69.62; so
(H2) fails at δ′ for that E (checked as well at eight δ from 1/2 to 1/100). Direct evaluation at 200 points beyond each
E_cf, with the actual n and h_n: those conditions hold. Control: (W1) admitted to the constant-free set is rejected (its
γ involves C_L4). For Theorem 1's dips alone (L.4_P not used), the constant-free conditions give only λ_h's 10^(−35.80)
and 10^(−40.14). *Illustration* (every uncertified leaf 1, λ0 = 0.00244, ε1 = 5.2617·10^(−4) so ι = 1074.6, β0 = 5 and
N_P = 30; a value of the formula, not a bound): log10 C_L3 ≈ 1.80·10^5, log10 C_L4 ≈ 1.80·10^6, log10 C_L3P ≈
1.96·10^13, log10 C_L4P ≈ 6.08·10^14, λ_rec ≈ 6.0·10^(−9) (λ_P, by λ_EP), E_25 ≈ 2.6·10^13, binding (W2).

So the paper says: λ_25 is written out as an explicit formula in constants the record does not certify, its other inputs
certified, and is below 10^(−6613) whatever they are (R9.4).

### R9.3 The computations the nits asked for

(a) **X17's phase rows (nit 3; edge1_5, computed, unit constants).** X15's adversarial configuration (exp(−1/x^(1/2)), N
= 10, λ = 10^(−40)), whose b̂4 = 0.00329147 (arg b̂4 = 2.9·10^(−10) π), with b̂5 = −1.006·10^(−4), is on the positive
real axis (δ_* = 0) and leaves a window undecided (X17's control): with |b̂4| and b̂5 kept and b̂4 rotated to −i|b̂4|
(the computed phase), to i|b̂4| and to −|b̂4|, every window is decided, all 122 by (A′), while unrotated a window is
undecided. Only the phase changes the decision, as L.28 says it must; the computed b̂4 lies on the negative imaginary
axis. Printed beside them (not a check): b̂4 rotated onto the positive real axis with |b̂4| = 0.0382 and b̂5 = 3b̂4 is
decided (N = 10, all 122 windows by (A′); N = 9 likewise, re-derived), which is why X17's first rows do not test δ_* >
0.

(b) **bfam5 B6 (nit 5; exact).** The chain B1-B4 at μ0 = 16 (the horizon r = 4, μ0^(1/4) = 2, every coefficient
rational; the transports' mass couplings μ0 H/r³ and the operators specialised at μ0 = 16, H4's families 0 and 1): H2,
H3, H4 (families 0, 1) and H5's family 1 satisfy both equations in every component computed, and at the horizon, exactly
and for every angular profile, c_(3,0),vv/A = 2^(−7) K(r0/4) d, c_(4,0),vv/A = 2^(−9)(α4(r0/4) d + β4(r0/4) Δd) with
B5's α4, β4 (the ratio of the α-coefficients is 1/512), and c_(5,1),vv/(iA) = 3 c_(4,0),vv/A. So b̂4(4ρ*, θ) = 16^(−9/4)
b̂4(ρ*, θ)|_(μ0=1) = −2^(−9)·0.0381909… i and b̂5 = 3b̂4 at μ0 = 16, the factor the scaling c_(j,k),vv ∝ μ0^(−1/4 − j/2
+ k/2) at fixed ρ predicts; at other μ0 the factor μ0^(−9/4) is deduced, not computed. Control (iii): with the operators
at μ0 = 16 and the transports' couplings left at μ0 = 1, B2's vv equation fails.

### R9.4 Paper texts (final; supersede R8.5's)

Generated by `wsE5/r9/paper/gen_old.py` from the quoted bounds (content, never line numbers) in RESPONSE-HL-5D.md at md5
805be200… (the file as it now stands): (P1) the old text from "R13). If μ0 = √72 l5² exactly, the" to "Propositions
E.2-E.4)." occurs once (lines 302-305, content md5 397a2813…); (P2) the old text from "- **The boundary at equality.**
If μ0 = √72 l5² exactly (computed," to "with √μ(v) − r_q(v) ≥ C' λ." occurs once (lines 1547-1555, ca1f042d…). Copies:
`wsE5/r9/paper/old1.txt`, `new1.txt`, `old2.txt`, `new2.txt` (final form) and `new2_unread.txt` (its variant while round
9 is unread). Both splices are simulated: each reverts exactly, the two-dust bullet before P2 is intact, every new line
is at most 119 characters; the spliced file would have md5 d65a39cc… (final) or 8d54a957… (variant).

(P1, final) R8.5's text, unchanged:

> R13). If μ0 = √72 l5² exactly, the boundary is the seed's horizon, and null for g_λ, on {v ≤ inf supp env}; after the
> shell starts it is spacelike for g_λ outside a layer whose width tends to 0 with λ (supplement
> `docket68/n1star/EQUALITY5.md`, Propositions E.2-E.4), and inside that layer, for λ small, every column has points
> where it is timelike for g_λ, so the no-return property stated above for μ0 > √72 l5² fails at equality
> (`docket68/n1star/EQUALITY5-LAYER.md`, Theorems L, L_P, L_E and L_1E‴, Corollary L.7).

(P2, final) The bullet, with the status of the record's rounds in its final form and λ_25's sentence as R9.2 states it:

> - **The boundary at equality.** If μ0 = √72 l5² (deduced in `docket68/n1star/EQUALITY5.md` and `EQUALITY5-LAYER.md`,
>   whose rounds 1-9 independent verifiers have read; computed by the programs of Appendix A), x_K = 1 is the seed's
>   horizon on {v ≤ v_s}, v_s := inf supp env, and is spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η. In the layer
>   between, for λ small and 0 < δ ≤ 1/2, it is spacelike where sup_(v'≤v) env ≥ λ^(3−δ), and where λ^(3+δ) ≤ sup env ≤
>   λ^(3−δ) its character is that of the ratio of λ³ A env |ν| |d| to the margin, up to a factor 1 ± 2λ^(1/10) (d the
>   double divergence of the waves' angular tensor, |d| ≥ 8/3; ν ≤ 0 a coefficient of the seed and τ0, with a double root
>   at (v_s − τ0)/√μ0 = ρ* = 1.806…). Suppose that near v_s env and its first K + 5 derivatives are positive and
>   log-concave, with logarithmic derivatives κ_k within a factor 2 of κ := (log env)′, |κ_k′| ≤ c κ_k^(1+α) for an α < 1
>   and |κ′| ≥ c′ κ^(1+α), and that env obeys the derivative and decay bounds of `EQUALITY5-LAYER.md` R5.2 and R6.1; the
>   C_c^∞ envelope used for the constants satisfies all of these, with α = 1/2, for every K (proved, `EQUALITY5-LAYER.md`
>   Proposition L.27). Then that ratio crosses 1 once per column, and below λ^(3+δ), down to v_s, every interval of
>   length 4πλ has timelike and spacelike points on every column, for every admissible τ0 (at ρ* this uses the next
>   family of the term linear in the waves, computed: `EQUALITY5-LAYER.md` R8.1); the term linear in the waves is
>   computed there to leading order, on the very edge, for Theorem 1, carried by the constraint correction at first
>   degree. For some envelopes whose intervals of zeros accumulate at the edge (`EQUALITY5-LAYER.md`, Proposition L.25″
>   (a)), intervals of length 4πλ below λ^(3+δ) on which x_K = 1 is spacelike throughout occur for every small λ. So
>   timelike curves of g_λ cross x_K = 1 into D_T. A domain O(λ)-close to D_T, inside x_K ≤ 1, has an inner boundary that
>   no future causal curve enters, and the spheres' horizon holds in the form: at most one zero per column, within C λ of
>   √μ(v); exactly one on the columns with v ≤ v_s and on those that reach across √μ(v) + C λ with √μ(v) − r_q(v) ≥ C' λ.
>   The threshold λ_L of Theorem L's proof is an explicit formula in the leaves of λ0 and one constant of the seed, and
>   is below 3·10^(−12); the thresholds of the finer statements (λ_η above and those named in `EQUALITY5-LAYER.md`)
>   depend on constants of the approximants that the record does not certify (λ0's leaves for Theorem 1, those of the
>   construction from past null infinity for Theorem 2) and are not evaluated; for the dips, λ_25 is written out as an
>   explicit formula in those constants, its other inputs certified, and is below 10^(−6613) whatever they are
>   (`EQUALITY5-LAYER.md` R8.3, R9.1, R9.2).

(P2, variant while round 9 is unread) The same with its second line "whose rounds 1-8 independent verifiers have read
and whose round 9 awaits a reader; computed by the programs of" in place of "whose rounds 1-9 independent verifiers have
read; computed by the programs of Appendix A)" (reflowed; `new2_unread.txt`).

Sources (R8.5's, extended): λ_25, R8.3, R9.1, R9.2. (P3, final) Appendix A, C, D: R8.5's list, with
`checks/lamconst5.py` C1-C5 added beside `checks/lam25_5.py` L1-L3, and bfam5's B1-B6, with the run times of their
`.out` files and their controls as in their docstrings; P5's commands for bandL4p5 and lamL5b stand.

### R9.5 Amendments, programs, labels

- **A48** (m1). R7.7's note, R8.3 and R8.6: λ_25's inputs are not all λ0's leaves; written out in R9.1 (notes "[R9, m1:
  …]").
- **A49** (R9.2). R8.3: (M2)'s constant is γ_mP, and its Theorem-2 rows are at β0 = 2 (note at R8.3).
- **A50** (nits 1-7). L.27 (a): (H_N) for N ≤ 14; L.27's proof: R4.1's sample; R8.0 (8) and R8.1: X17's rows do not
  carry the phase; L.28 (2) R2: the |B_s′| term; R8.1: μ0 = 16 computed; R8.5: the splice md5 at 805be200…; R8.6: the
  pins re-measured. Each by a note "[R9, …]" at its site.
- **Programs.** New: `checks/lamconst5.py` (C1-C5, a control each). Changed: `checks/edge1_5.py` (X17's phase rows and
  its printed row; X1-X16 unchanged), `checks/bfam5.py` (B6 and control (iii); μ0 a parameter of the transports, the
  operator table and Pol^+'s data, B1-B5 unchanged). Unchanged: hyp5, lam25_5, constL5, degtwo5, lamL5b, bandL4p5,
  layerlin5 (their `.out` stand).
- **Labels.** Certified (interval arithmetic): lamconst5 C1 (C_L1), C2's C_S3, C5 (E_cf). Computed, exact: bfam5 B6;
  lamconst5 C2-C4 (the DAGs, the transcription, the census). Computed with unit constants: X17's phase rows. Deduced:
  the formulas of R9.1 (each from the proof step named beside it), E_H2's monotonicity in δ. Not evaluated, with the
  blocking step named: λ_25's value, λ_rec, C_L3, C_L4, C_L3P, C_L4P, C1, C_P, C_ρ, λ_P (R9.1 (f)).

### R9.6 Open items, runs, sources

*Open items.* None in section 9's sense: Theorem L_1E‴ has no exclusion, every hypothesis it states is proved for the
envelope the paper uses, every input of λ_25 is written out, and the paper states the thresholds' status as R9.2 does.
λ0's, Theorem P's and the seed's uncertified leaves are not open items of this note: they are the constants of Theorems
1 and 2, whose certification is the nine-stage solve CONSTANTS5 1.5 describes and its analogue on P; R9.1 (f) names the
step. O2: round 9 awaits an independent reader.

Runs (full, each `.out` beside its program, under a load average near 8 on four cores, with other jobs running): bfam5
B1-B6 under PYTHONHASHSEED = 0, 1612 s (`.out` md5 dfb2115e…, program 9e16e91b…; its B1-B5 lines and controls (i), (ii)
byte-identical to round 8's `.out` d9e0d744…, B6 and control (iii) new); edge1_5 X1-X17, 1496 s (49000672…, b46b5e0f…;
X1-X16 as round 8's apart from the printed times, X17's rows as round 8's with the phase rows added); lamconst5 C1-C5,
two runs byte-identical, 550 s and 419 s (aee57835…, 7c35b511…); a scratch run of X17's model at N = 9 with b̂4 → +|b̂4|
(nit 3's re-derivation), decided. Every check passes and every control fails.

READ: the reader of round 8's report (`scratchpad/report-vE7r8.md`, and its scripts `mut/m17.py`); RESPONSE-HL-5D.md at
md5 805be200… (P1 lines 302-305, P2 lines 1547-1555, located by content); N1STAR-PROOF.md at 5c1a186a… (sections
9.1-9.4: Theorem P, Lemmas 9.1-9.5, Theorem A_P, Propositions 9.8, 9.9, the proof of Theorem P; "Z := d_tau - beta_ext"
from line 497); CONSTANTS5.md at 1d92d5f7… (1.3's formula for λ0 and its ninth term, 1.4's C_S and ε1, Round 4's s0 and
ε1 < s0, 1.5); LAMBDA0-DATA5.md at 09c806ae… (λ0's certified bounds); EQUALITY5.md section 0 (C1); constL5.py (R5.5's
DAG). File md5 before this round: dd1853e4….
