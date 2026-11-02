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
