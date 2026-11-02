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
ℓ, at fixed v. The wave equations for the means: on Ω_v := Ω ∩ {v' ≤ v} the face {v' = v} is null for g0 with Ω_v to
its past, so its flux is nonnegative and is dropped (the argument of Proposition E.2), and Lemmas 2.3–2.4 bound the
solution on Ω_v by its data and sources there; commuted derivatives and Sobolev's embedding on the Ω_v (uniformly
Lipschitz for v ∈ [v_s, v_s + 1]) give the pointwise form, each derivative of a source costing derivatives of env (M
grows with N and i). Products of first-degree factors give the degree-2 bounds; μ(v) − μ0 ≤ C ε_0². ∎

**Lemma L.4 (the weighted remainder; deduced, sketch).** Put ε := 2C1 λ (C1 of EQUALITY5 section 0, |g_λ⁻¹ − g0⁻¹| ≤ C1
λ). For v1 ≤ v_s + 1 with ε_M(v1) ≤ λ^6 and every point X of Ω with v(X) + ε(τ(X) − τ0) ≤ v1 and r(X) ≥ r_q(v(X)),

    |w(X)| ≤ C λ^(N−6) ε_M(v1).

*Proof (sketch).* R := Ω ∩ {v + ε(τ − τ0) ≤ v1}. Its lateral face has conormal dv + ε dτ, timelike for g_λ:
g_λ⁻¹(dv + ε dτ, dv + ε dτ) ≤ −2ε − ε²(1 + μ/r²) + C1 λ (1 + ε)² < 0; v + ετ increases along future causal curves of
g_λ, so R lies to the past of the face and its flux is dropped; R does not meet the outer face of Ω, and its slices
{a ≤ r ≤ v1 − ε(τ − τ0) − τ} have outer radii decreasing in τ. From the quasilinear form (supplement (0.2)),
−(1/2) g_λ^ab ∂_a ∂_b w = −Ric^H(g_app) + (1/2)(g_λ^ab − g_app^ab) ∂_a ∂_b g_app − [Q(g_λ)(∂g_λ, ∂g_λ) − Q(g_app)(∂g_app,
∂g_app)], whose last two terms are bounded by C(|w| + |∂w|) on R because |∂² g_app| ≤ C(1 + λ⁻¹ ε_2(v1)) ≤ C there
(Lemma L.3 (a); the one large coefficient of the supplement's section 5.1 is λ⁻¹ times the wave's amplitude, which is
small on R). The energy inequality of the supplement's Lemma 2.3 with gt := g_λ, run on R, Gronwall, and the same for
∂^i w, i ≤ 3 (the commutators carry ∂^j g_λ, j ≤ 4, bounded on R: |∂^j g_app| ≤ C(1 + λ^(1−j) ε_j(v1)) ≤ C, and
|∂^j w| ≤ C λ^(K−2−j) for j ≤ 4 by Theorem E and Lemma 2.1; the term w ∂^(i+2) g_app is ≤ C|w| on R because
λ^(−i−1) ε_(i+2)(v1) ≤ 1), bound w in H^4 of the slices of R by the data of w on Σ_τ0 ∩ R (Lemma L.3 (c), four
derivatives: C λ^(N−6) ε_M(v1)) and ∫ ‖∂^i Ric^H(g_app)‖ (L.3 (b): C λ^(N−3) ε_M(v1)). The slice through X has width
at least r_q − a ≥ δ0, so Sobolev's embedding (supplement Lemma 2.1) has a uniform constant. ∎

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

Fix p := 14, M from Lemmas L.3–L.4 (with i ≤ 4), m := 56 M, κ := 64, y := λ^p, v* := v*(y), W_λ := [v*, v* + 4πλ], v1
:= v* + 4πλ + ε(τ_end − τ0) = v* + O(λ), L := v1 − v*. For λ small the hypothesis of Lemma L.6 holds (λ ≪ y^(1/m)),
so on [v*, v1] env ∈ [3y/4, 5y/4] and ε_M(v1) ≤ C y^(1 − M/m) ≤ λ^6 (Lemma L.4's hypothesis).

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
