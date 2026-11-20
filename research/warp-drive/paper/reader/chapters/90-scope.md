## Scope {#ch:scope}

This chapter collects what [[thm:main]], [[thm:past-construction]], [[thm:bondi-law]] and [[thm:settling]], and the
results of [[part:settling]], [[part:constants]] and [[part:further]], claim and what they do not claim; each statement
is followed by the place where it is stated or proved.

### The construction and its domain {#sec:scope-domain}

[[thm:main]] is made on the compact domain Ω ⊃ D_T ∩ {τ ≥ τ0}, [[thm:past-construction]] on Ω together with its past
domain, and [[thm:bondi-law]] near past null infinity for the solutions of [[thm:past-construction]]; the inner boundary
r = a of Ω and of the past domain lies a fixed distance inside the curvature boundary x_K = 1, and nothing in the three
theorems is claimed beyond Ω and the past domain ([[sec:domain]], [[sec:why-five]]). Below the inner boundary the
theorems are not silent: the boundary sits at the curvature scale l5, which is arbitrary, and since
r_q(v) = (√72 μ(v) l5²)^(1/4) tends to 0 with l5, a smaller l5 puts every point with r > 0 and v ≤ v_end + T inside
D_T, the constants of [[thm:main]] then depending on l5 ([[sec:domain]], [[thm:main]]). At r = 0 the limit itself is
singular, its Kretschmann scalar being 72 μ²/r⁸ ([[prop:vaidya]]). Nothing in the paper involves an inner or Cauchy
horizon ([[sec:why-five]]).

The envelope is taken in C_c^∞, and the hypothesis is used as it stands: for a fixed K the estimates use finitely many
derivatives of env, whose number is not determined, an envelope of finite smoothness is not covered, and the profile
sin⁴(π(v − 1/2)/3) on [1/2, 7/2], which is C³ and not C⁴, is covered for no K ≥ 6 ([[rem:envelope-regularity]]).

Item 6 of [[thm:main]] concerns the round family of spheres {v, r = const}: the zero set of their outgoing expansion on
the columns is not a marginally trapped surface ([[prop:one-zero]], [[rem:round-family]]). Item 7 concerns the Hawking
mass of the spheres of the domain, which is not the angular mean of the mass aspect at past null infinity; that mean is
governed by the mass law of [[thm:bondi-law]] ([[prop:mean-mass]], [[rem:mean-mass-aspect]]). The expansion of
[[prop:bondi-hierarchy]], on which [[thm:bondi-law]] rests, claims no uniformity in λ beyond its leading term, and
nothing is claimed about future null infinity or the Bondi mass there, which the domain does not reach
([[rem:bondi-scope]]).

If μ0 > √72 l5², the boundary x_K = 1 is spacelike for g_λ with a uniform margin once λ is small, and a future causal
curve that meets it leaves D_T there and does not return ([[prop:boundary-spacelike]]). At equality, μ0 = √72 l5²,
this fails in a layer at the start of the shell whose width tends to 0 with λ: on every column the boundary has points
where it is timelike for g_λ, and future timelike curves cross it into D_T ([[thm:layer]], [[cor:layer]]). That the domain of [[prop:eq-domain]],
whose inner boundary no future causal curve enters, is needed in place of D_T is not shown ([[cor:layer]]). Inside the
layer the character of the boundary is decided in the parts of the layer that [[prop:layer-regions]] describes, by one
switch per column on the band between the levels λ^(3+δ) and λ^(3−δ) for an envelope increasing at its edge with the
hypothesis (H_N) of [[def:edge-hypotheses]] ([[thm:l-24]]), and at the very edge for envelopes with the edge
hypotheses, which hold for env_C ([[thm:very-edge]], [[cor:edge-envelope]]). Some regularity of the edge is needed: for
an envelope whose intervals of zeros accumulate at the edge, the boundary is spacelike throughout intervals of length
4πλ below the level λ^(3+δ), for every small λ ([[prop:edge-dips]]), and at a dip of a general envelope the criterion
of [[rem:edge-criterion]] decides nothing.

### The thresholds and the constants {#sec:scope-constants}

The threshold λ0 and the constant C of [[thm:main]] are produced by its proof and are not evaluated
([[sec:main-statement]]). At the numerical point of [[def:lambda0-point]] the threshold that the proof of [[thm:main]]
delivers is below 0.0024433 in the operator norm of the proof, and any λ0 and C with the properties that the proof
gives them satisfy λ0 < 0.0019079 when |·| is read as the Frobenius norm and λ0 < 0.0012228 when it is read as the
largest absolute entry ([[prop:lambda0]]). Of the conditions that the proofs place on λ0 the bound uses only C λ0 ≤ ε1,
and no lower bound for λ0 is given ([[sec:lambda0-bound]]). The first stage's mean correction M_22 at the point where
the wave is largest would sharpen the three bounds; its value is a numerical observation that no proof uses, no bound
on it is proved, and the bounds proved are those of [[prop:lambda0]] ([[rem:m22-value]]).

The thresholds λ1 and δ of [[thm:settling]] are positive by its proof, and their values are not determined
([[rem:ec-not-evaluated]]). The proof's formulas give λ1 < δ and bound the modulus of the initial family at 2δ by
2^(−(32d+8)), d the loss with which the Nash–Moser theorem is applied ([[prop:ec-delta-cap]]). A lower bound for δ or
λ1 would need upper bounds for every constant of the proof that enters them ([[sec:ec-delta]]).

The loss d is at least the loss d_acc that the proof assigns to the tame estimates, and the regularity of the
Nash–Moser step is N_NM = 21d + 6; d_acc is composed of elementary losses in closed form and of the numbers of steps of
the iterations of the construction, except the loss of the forward solution operators, which the proof fixes without
a value ([[thm:loss-d]] (i)). At the computational point of [[def:ec-point]], d > 7.959 × 10¹⁵ and
N_NM > 1.671 × 10¹⁷, so that log₁₀ of the modulus at 2δ is below −7.666 × 10¹⁶ ([[thm:loss-d]] (ii),
[[prop:ec-delta-cap]]). These are lower bounds for the loss that this proof's choices produce, not for the least loss
with which the tame estimates hold ([[thm:loss-d]]); the upper bound for d at that point is [[pending:scope-d-upper]].
The computational point is a point at which the formulas of the proof can be evaluated, and it lies outside the set on
which [[thm:settling]] is proved ([[rem:ec-point-outside]]). No result of [[ch:explicit-constants]] is used in the
proof of any theorem of this paper ([[ch:explicit-constants]]).

Explicit values stop upstream of every constant of [[thm:settling]]: the proof fixes the gauge and damping parameters
only below thresholds whose existence it proves, and the cut-offs and orders of its function spaces only up to
admissibility; arguments by contradiction, compactness and defect measures give constants without a value; and the
parametrix norms at ι⁺, the tame constants to the order N_NM, the Nash–Moser thresholds of the exterior and slab
problems and the constants of the gluing are not evaluated. This is a limit of the explicit evaluation, not of
[[thm:settling]] ([[rem:ec-not-evaluated]]).

Explicit resolvent bounds are proved for one operator, the scalar wave operator on five-dimensional Tangherlini of mass
1, cut off to {6/5 ≤ r ≤ 4}: for every harmonic and every real 0 < |σ| ≤ 3, and with the constant 11.477 for
3 ≤ |σ| ≤ 384 ([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]], [[thm:band]]). The smaller values
observed from |σ| = 12 on, and their decay in |σ|, are not proved ([[rem:band-observed]]). For the scalar-type blocks of
the linearised gauge-fixed operator at zero energy, an upper bound for the least singular value obstructs a good
constant at a weight next to an indicial root ([[lem:rb-quasimode]]).

The threshold λ_2 of [[thm:own-data]], the threshold λ_L of [[thm:layer]] and the thresholds of [[thm:very-edge]] and
[[thm:l-24]] are not evaluated ([[thm:own-data]], [[rem:layer-threshold-size]], [[rem:edge-thresholds]]). λ_L is the
threshold that the proof delivers, not the largest λ for which [[thm:layer]] holds, and for the envelope env_C it is at
most 10^(−430) ([[rem:layer-threshold-size]]).

### After the shell {#sec:scope-after}

[[thm:settling]] concerns the exterior of the black hole after the shell, and its rate holds in spatially compact
subsets of the exterior ([[thm:settling]]). Its item (i) concerns the development of glued data, which agree with the
data of g_λ on a ball and are continued equivariantly to exact Tangherlini data beyond it; they are not the data of a
continuation of g_λ beyond the ball, and their development is not one ([[sec:after-shell-gluing]]). Its item (ii) is
stated for perturbations in Hintz's own data class, and not for a class of decaying data reached by gluing, since gluing
replaces the data near infinity on which the solution near the hole at late times depends ([[rem:settling-class]]). The
perturbations that (ii) reaches, directly or through gluing uniformly in the gluing radius, are exactly those small in
Hintz's class: a perturbation of order of decay a > 3 and small enough size is reached directly, for 3/2 < a ≤ ℓ0 the
rate does not decide, and the statement that (ii) applies up to the gluing is false for fixed size and large radius at
every such a ([[thm:after-shell-reach]]).

With its inner radius taken as half the radius q_end of the curvature boundary after the shell, the development of
[[thm:settling]] (i) is defined on all of {r ≥ q_end} to the future of its initial surface and settles there at the
rate of [[thm:settling]], for every final mass, with λ1, δ and the constants depending on μ_end; the part of its domain
below q_end lies beyond the curvature boundary ([[prop:interior]]). For λ small, glued to g_λ along the part of the
initial surface where the two induce the same data, it forms one vacuum spacetime; how far their identification reaches
into the future is not decided, nor whether that part of the initial surface is acausal in all of the domain of g_λ
([[lem:interior-one-spacetime]], [[rem:interior-one-spacetime]]), and nothing in the proof of [[thm:settling]] uses the
identification ([[rem:vii-4-1]]). The interior covered by [[prop:interior]] belongs to a vacuum continuation of g_λ fixed
by the gluing, not to the continuation of g_λ's own data ([[rem:interior-one-spacetime]]). At a fixed λ the data of
either construction of g_λ are available only on a bounded part of Hintz's initial surface, since the proofs give no
threshold uniform in the size of the domain ([[rem:interior-reach]]).

The development of g_λ's own data on Hintz's initial surface settles, with no gluing and with no exceptional set in λ, in
a data class wider than that of [[thm:settling]] (ii) by half-integer orders ([[thm:own-data]]). The class of (ii) does
not contain these data: for every amplitude but at most one, the coefficient of r^(−5/2) that g_λ − g0 carries at past
null infinity after the shell is nonzero for every λ ∈ (0, λ_P] off a set with no accumulation point in (0, λ_P], and it
reaches the data at spatial infinity ([[ch:own-data]], [[prop:own-tail]]). The constants ε, d_1 and λ_2 depend on the
class ([[thm:own-data]]). The continuation of g_λ to the past domain of dependence of the far
part of the initial surface is unique in the wave-map gauge among the continuations within 1/50 of Tangherlini whose
commuted energies of some weight a_0 ∈ (0, 1/2) stay bounded and whose energy tends to 0 toward past null infinity
([[prop:own-uniqueness]]); existence is not attempted at a weight a_0 ≤ 1/2 ([[rem:own-low-weight]]).

### The linear solution in other gauges {#sec:scope-gauges}

The linear statement of [[thm:settling]] is made in the gauge of the stability theory. A linear solution in another
gauge with the same data, given on the whole future of the initial surface outside r = r_♭, differs from it by a
linearised diffeomorphism ℒ_X g, and nothing is asserted there about the size or the decay of X ([[cor:ix-2-3]],
[[rem:ix-2-4]]). Two gauges are treated.

In the Regge–Wheeler-type gauge the gauge vector is explicit, and the perturbation settles to the change of mass on each
region r_♭ < r ≤ R′, the horizon included, at the rate of the stability theory with two derivatives lost; the constant
depends on R′, and nothing is claimed uniformly in r ([[thm:rw-settling]]). The gauge vector itself decays one power
more slowly, its spherically symmetric part being a time integral, and whether that part decays faster for the solution
of the stability theory is not determined ([[thm:rw-settling]] (c), [[rem:rw-zeta]]). Uniformly in r the statement
fails: the orbit-space components can grow like r^(1/2) on the outgoing part of the leaves of [HKW18]
([[thm:rwg-1]]); with the weight r^(−1/2) on the orbit-space components and r^(1/2) on the angular block they settle
pointwise and uniformly in r, the weights are sharp, and the rates are not claimed sharp ([[thm:rwg-2]],
[[thm:rwg-2-prime]]). Compared with the decay of the master quantities proved in [HKW18], the components settle on each
region r ≤ R at the rate τ⁻² in energy once one datum more than [HKW18]'s energies is finite, the second derivative of
the master fields transversal to the horizon, and for the scalar type that datum cannot be dropped ([[prop:np-10-1]],
[[lem:np-10-1b]]).

In the harmonic gauge every perturbation of the class has a representative on the whole future of the initial surface
outside r = r_♭ that induces the given data and settles on each region r_♭ < r ≤ R′, the horizon included, to
ṁK* + cℒ_(W*)g at the rate t*^(−min(p_0,3/2)+ε), at t*^(−1+ε) when the data differ from a change of mass only on a
ball, and at t*^(−3/2−κ), κ < δ_♯, for data of compact support ([[thm:harmonic-rate]]). The gauge-fixed change of mass
ṁK* grows linearly in v, and the growth cannot be avoided: when the mass changes, no harmonic-gauge solution settles to
a change of mass near the horizon at an integrable rate ([[thm:gd-2-3]]). Without decay of the data of the spherically
symmetric gauge vector Z′_0, the growth can be traded for a stationary term that does not decay at infinity
([[prop:gd-r2-13]] (c)).

### Further families {#sec:scope-families}

[[thm:two-dusts]] places the outgoing packet on Σ_τ0 between the seed's horizon and the shell. It does not treat a
packet outside the shell, for which the two families do not cross in the future of Σ_τ0, nor one inside the seed's
horizon, a case not examined ([[rem:two-dust-scope]]).

The Cauchy stability of the class Einstein–null-dust system, without smallness, constructs the background; the
high-frequency construction over a non-round background needs more: beyond one ingoing and one outgoing family the
further families must have densities vanishing near the axes, and pairwise separation does not suffice when three or
more families are present at a point ([[thm:class-stability]], [[rem:class-scope]]). Its application to the two-dust
background assumes that the outgoing packet does not reach the inner sphere, which the construction of that background
does not decide ([[cor:class-two-dust]]).

[[thm:vlasov]] realises as weak limits of class vacuum metrics, along odd numbers of dusts, the class
Einstein–restricted massless Vlasov solutions whose field is a caustic-free family of dusts labelled by initial
direction and kept off the axes, on domains of the type of Ω whose initial spheres have positive mean curvature; no
smallness is assumed, and the hypotheses hold on a nonempty open set of solutions ([[thm:vlasov]], [[lem:vlasov-open]],
[[prop:vlasov-nonempty]]). The hypotheses avoid four obstructions proved in [[ch:vlasov]], among them that two dusts of
one orientation are not separated at an axis and that a continuous density carried to an axis transversally would
focus there ([[rem:vlasov-obstructions]]). The two radial dusts of [[thm:two-dusts]], which reach the axes, can be added
to a small restricted field when the outgoing packet does not reach the inner sphere; the solution then exists on its
adapted domain and is a weak limit of class vacuum metrics only on narrower domains of the type of Ω inside it, the
high-frequency step not being carried out on the adapted domain itself, and no uniqueness of that solution is stated
[[pending:scope-two-dust-radial]].

The results on localised data concern the explicit two-dust background of [[sec:bg-data]], on its slice Σ_τ0 or on a
slice bent from it, and invariant data near the background's data ([[ch:localised-data]]). Data localised in angle away
from the axes exist on the whole of a slice bent from Σ_τ0 by at most 0.0012, on which Rácz's split is hyperbolic
everywhere; on Σ_τ0 itself the split is hyperbolic except in one band inside the shell, where it is hyperbolic for no
foliation ([[thm:loc-bent-slice]], [[prop:loc-band]]). Localisation in angle and radius at once is decided at second
order in the amplitude by the sign of the charge, and it is stated in terms of the sign of f, nothing using the event
horizon: on a vacuum band that meets {f < 0} such vacuum data whose first-order part is not a gauge perturbation exist
for every small amplitude, on a vacuum band where f > 0 they are excluded for small amplitude when the first-order part
is not a gauge perturbation, and on every vacuum band they are excluded for small amplitude when the first-order part
perturbs the extrinsic curvature alone ([[thm:charge-sign]]).

### At the prescribed wavelength 10 l5 {#sec:scope-ten-l5}

[[thm:main]] is a statement for small λ; for the smooth envelope of [[def:lambda0-point]], whose parameters are those
of the first seed at 10 l5, the threshold that its proof delivers lies below 10 l5 by a factor above 409
([[sec:lambda0-bound]]). At λ = 10 l5 there is no separation of scales: the wavelength is 10 times the curvature
length on x_K = 1, and at the horizon more than 2.91 times it at the first seed and more than 0.92 times it at the
second ([[prop:tl5-scales]], [[thm:ten-l5]]); the statement that the waves are high-frequency on D_T once
λ < l5/10 concerns the approximant, not the threshold λ0 ([[sec:tl5-scales]]). The envelope taken there,
sin⁴(π(v − 1/2)/3), is C³ and not C⁴, so [[thm:main]] does not apply to it at any λ ([[rem:envelope-regularity]]).

Posed as a characteristic initial value problem in double-null gauge, the problem at 10 l5 has a solution where the
solution is the seed, v ≤ 1/2 in units of the horizon radius; and wherever a vacuum solution exists in the gauge with the
seed's transverse derivative of R on the seed's cone, its leaves inside the seed's horizon generator are outer trapped,
and its T²-invariant marginally outer trapped sections lie at or outside that generator ([[thm:ten-l5]]). No existence is
claimed for v > 1/2: the continuation lemma assumes smooth data and the local existence, uniqueness and continuation of
the characteristic problem in the gauge, which this paper does not establish, the data are not smooth, its a priori
estimate is one on a whole region, the axes included, and the residual bounds proved hold at points and on boxes of a
region not of that form ([[thm:ten-l5]], [[lem:tl5-continuation]], [[rem:tl5-beyond]]). Beyond v = 1/2 the shift on
the outgoing data cone is subject to a constraint that this paper does not treat ([[def:tl5-problem]]). The size of
the constant of a linear estimate on a solution found at the first seed, and with it how far the closing condition of
the continuation lemma lies from the residual bounds proved, is a numerical observation that no proof uses
([[rem:tl5-constants]]).

### Numerical observations {#sec:scope-observations}

The remarks headed as numerical observations state what was observed, no proof in this paper uses them, and nothing in
them is claimed: among them the value of M_22 ([[rem:m22-value]]), the absence of growing modes of the master equations
up to a finite time ([[rem:rw-numerics]]), the solutions at 10 l5 ([[rem:tl5-bondi-scheme]], [[rem:tl5-runs]]) and three
further constants of the linear theory at the final black hole ([[rem:ec-linear-observed]]).
