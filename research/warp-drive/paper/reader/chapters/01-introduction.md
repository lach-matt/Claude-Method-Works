# Part. Introduction and statements {#part:statements}

## Introduction {#ch:introduction}

### Burnett's problem {#sec:burnett}

Burnett's problem [Bur89] concerns families of vacuum metrics whose derivatives converge only weakly. Huneau and
Luk state it as follows ([HL18], p. 1; their footnote omitted): "On a fixed manifold, consider a one-parameter family of
Lorentzian metrics g_λ for λ ∈ (0, λ_0], λ_0 ∈ R which satisfies the Einstein vacuum equations
R_μν(g_λ) = 0. (1.1) Assume moreover that there exists a metric g_0 such that as λ → 0, • g_λ converges to g_0
uniformly on compact sets; and • the derivatives of g_λ converges weakly in L² to the derivatives of g_0. Due to the
nonlinearity of the equations, it can happen that the limiting metric g_0 is a solution to the Einstein equations which
is not vacuum". Burnett's own assumptions, as Luk and Rodnianski print them ([LR20], p. 3, their (1.3)), are
"|g_n − g_∞| ≤ λ_n, |∂g_n| ≤ C, |∂²g_n| ≤ Cλ_n^(−1)". The direct question asks which limits occur; the reverse asks
whether a given Einstein–matter solution is such a limit.

### The theorem of Huneau and Luk {#sec:huneau-luk}

Huneau and Luk work with metrics ([HL18], pp. 2–3) "⁽⁴⁾g = e^(−2φ) g + e^(2φ) (dx³)²", for which "Einstein vacuum
equations R(⁽⁴⁾g)_μν = 0 are equivalent to the following system for (g, φ): □_g φ = 0, R_μν(g) = 2∂_μφ ∂_νφ. (1.3)"
Their main theorem reads ([HL18], p. 10; their footnotes 11 and 12 omitted, and the two column vectors of (4.1)
printed in a row with ";"):

> **Theorem 4.2 (Main theorem).** Let k ≥ 10, −1/2 < δ < 0, R > 0 and A be a finite set. Given an admissible free
> initial data set (φ̇, ∇φ, F̆_A, u_A)↾Σ_0 such that
> • |∇u_A↾Σ_0| > 1/2;
> • u_A↾Σ_0 is angularly separated;
> • (Smallness condition) ‖∇u_A − c⃗_A‖_(H^11_δ) + ‖φ̇‖_(H^10) + ‖∇φ‖_(H^10) + ‖F̆_A‖_(H^10) ≤ ε;
> • (Genericity condition on initial data) there exists a point p ∈ R² such that ((∂_1φ_0)↾Σ_0; (∂_1φ̇_0)↾Σ_0)(p)
> and ((∂_2φ_0)↾Σ_0; (∂_2φ̇_0)↾Σ_0)(p) are linearly independent. (4.1)
>
> Then, there exists ε_0 > 0 such that if ε < ε_0, a unique solution (g_0, φ_0, (F_0)_A, (u_0)_A) to (1.4) arising
> from the given admissible free initial data set exists on a time interval [0, 1], and there exists a one-parameter
> family of solutions (g_λ, φ_λ) to (1.3) for λ ∈ (0, λ_0) (for some λ_0 ∈ R sufficiently small), which are all
> defined on the time interval [0, 1], such that (g_λ, φ_λ) → (g_0, φ_0) uniformly on compact sets and
> (∂g_λ, ∂φ_λ) ⇀ (∂g_0, ∂φ_0) weakly in L² with ∂g_λ, ∂φ_λ ∈ L^∞_loc uniformly.

Here (1.4) is the Einstein–null dust system with |A| families ([HL18], p. 3), the admissible free data are posed on a
maximal slice of R² and solved for in an elliptic gauge ([HL18], pp. 8–9, Definition 3.2 and Theorem 3.3), and angular
separation is [HL18] Definition 4.1, p. 10. Their review states where the smallness comes from and names the
large-data problem ([HL24], p. 28): "Notice that in the U(1) setting, because of our use of an elliptic gauge,
smallness is required even for local existence of smooth solution. It would be interesting to carry out these
constructions without smallness assumptions: Problem 8.6. Construct local high-frequency solutions as in Sections 5, 6
and 7.2 but such that the limiting solution is far away from Minkowski spacetime."

### What is proved {#sec:what-is-proved}

We prove the counterpart of Theorem 4.2 of [HL18] in five dimensions, for one family of null dust, on a background
that is far from Minkowski: a black hole growing by an ingoing shell, on a fixed domain that reaches inside the horizon
to the surface where the limit's curvature reaches a fixed scale ([[thm:main]]). It is an instance of Problem 8.6 in a
five-dimensional symmetry class, not an answer to Problem 8.6 as posed, which concerns four dimensions. Solutions with
the same properties are also constructed from the waves' free data at past null infinity ([[thm:past-construction]]),
and at past null infinity they obey the five-dimensional Bondi mass law with the prescribed radiation field
([[thm:bondi-law]]).

Beyond that domain, and outside the black hole, we prove that in the class the development of a continuation of their
data beyond a ball about the hole settles at late times to five-dimensional Tangherlini of a nearby mass, and that the
developments of their perturbations without symmetry that are small in Hintz's data class settle to slowly rotating
Myers–Perry black holes ([[thm:settling]]). The route is Hintz's proof of the nonlinear stability of Kerr [Hin26],
carried into five dimensions: every input that depends on the dimension is established at Tangherlini, the class removes
his boosts, rotations and their gauge modifications, and without it they are restored, with the inputs at every nearby
Myers–Perry parameter proved by perturbation from Tangherlini, in the manner of [HHV21], and the charges by which the
gluing at large radius matches the Myers–Perry family determined. The proof is written out in full in spacetime
dimension n + 1 = 5: his stability paper, the parts of his companion papers [Hin26a, Hin26c, Hin23a] that the route
uses, and the gluing of [CD03], part by part, from statements of those papers that hold in every dimension. We also
prove that the development of g_λ's own data settles, with no gluing, in a class wider by half-integer orders, and the
linear solution's settling in a Regge–Wheeler-type gauge and in harmonic gauge; and we prove the two-dust and
restricted-Vlasov counterparts, state the constants, and state the scope.

The two theorems share their architecture. Both reduce the vacuum equations in the symmetry class to 2+1 gravity
coupled to free waves with a flat, positive-definite target ([[prop:reduction]]; [HL18] (1.3)); both build an
approximate solution by geometric optics and correct it on a fixed interval; both conclude with uniform convergence of
the metric and weak, not strong, convergence of its derivatives (in Huneau and Luk, of the 3+1 metric; their reduced
metric's derivatives converge uniformly, [HL18] Remark 4.3, p. 10), the defect being null dust. They differ in what is
large: Huneau and Luk allow any finite number of angularly separated dusts on a small background; we allow one dust on
a large one, and the amplitude of the waves is not small either.

### Why five dimensions and a black hole {#sec:why-five}

In five dimensions the T² class is the natural analogue of polarized U(1): the two rotations of R⁴ = R² × R² commute,
the two reflections make the Killing fields hypersurface orthogonal and mutually orthogonal, and the reduction is
exact ([[prop:reduction]]). Unlike Huneau and Luk's translation, each rotation has an axis, where the reduced system
degenerates; the proof therefore never uses the reduced system and works in five-dimensional Cartesian coordinates, in
which the axes are regular points. Five-dimensional Vaidya is the simplest large solution of the limiting system: its
mass grows by exactly the averaged energy of the waves, and it carries a horizon. The domain ends where the curvature
reaches a fixed scale l5, x_K := l5² √𝒦 = 1 with 𝒦 the Kretschmann scalar; that surface lies inside the horizon, or on
it at equality, and is spacelike when μ0 > √72 l5² ([[prop:boundary-spacelike]]), so the domain is the domain of
dependence of its data and nothing inside it is excised. The solution is constructed on a compact set Ω reaching a
fixed distance inside that surface, and nothing in [[thm:main]], [[thm:past-construction]] and [[thm:bondi-law]] is
claimed beyond Ω and the past domain; [[thm:settling]] concerns the exterior of the black hole after the shell. Nothing
in the paper involves an inner or Cauchy horizon.

### Relation to Huneau and Luk, Touati, and Luk and Rodnianski {#sec:relation}

Point by point; HL is [HL18], T is [Tou23a], LR is [LR20], and "here" is this paper.

- *Dimension and symmetry.* HL: 3+1, polarized U(1), a translation with no axis. T: 3+1, none. LR: 3+1, none. Here:
  4+1, T² with both reflections, rotations with two axes.
- *Reduced system.* HL: 2+1 gravity with one free wave φ, their (1.3). T, LR: none. Here: 2+1 gravity with two free
  waves on the target (3/2) dψ² + 2 dω² ([[prop:reduction]]), identified, and not used in the proof.
- *Gauge.* HL: elliptic (maximal slices, conformally flat). T: generalised wave. LR: double null. Here: the wave-map
  gauge relative to the limit g0.
- *Background.* HL: small, near Minkowski (the smallness condition of Theorem 4.2). T: small, his (2.9), with an
  asymptotically planar phase, his (2.10). LR: large and angularly regular, on a double null domain short in one null
  direction (u̲* ≤ ε, ε depending on the bound C of the data, their Theorem 1.9). Here: five-dimensional Vaidya with
  a black hole; no smallness of μ0, A or env.
- *Dusts.* HL: any finite number, angularly separated, with generic data. T: one. LR: two, measure-valued; their
  reverse statement, the counterpart of Huneau and Luk's theorem, is their Corollary 1.14, local. Here: one.
- *Data.* HL: admissible free data on a maximal slice. T: the conformal method of [Tou23b]. LR: characteristic.
  Here: Cauchy data on Σ_τ0, the constraints solved outward in r.
- *Domain.* HL: [0, 1] × R². T: [0, 1] × R³. LR: [0, u*] × [0, u̲*] × S². Here: Ω ⊃ D_T ∩ {τ ≥ τ0}, through the
  horizon to a spacelike boundary.
- *What closes the estimates.* HL: the smallness ε. T: the smallness ε, with λ ≤ λ0 as well ([Tou23a] Proposition
  7.1, p. 13). LR: angular regularity on a domain short in one null direction. Here: powers of λ, with the
  approximant carried to any order.
- *The derivative loss.* HL: elliptic estimates for the metric. T: a null foliation and a Fourier cut-off. LR:
  angular regularity. Here: the phase-shift identity, the exact commutator [[eq:commutator]] and a compact mollifier.
- *Conclusion.* HL: uniform convergence, weak L² convergence of derivatives, ∂ in L^∞ uniformly. T: g_λ = g0 +
  λ g(1) + … in generalised wave gauge. LR: C⁰ and weak W^(1,2). Here: uniform at O(λ), ∂g bounded, weak L².

*What carries over.* The reduction to a 2+1 system with free waves on a flat, positive-definite target, which here is
two copies of Huneau and Luk's scalar ([[prop:reduction]]); the geometric-optics construction around an eikonal phase
of the limit; the weak limit as null dust with Isaacson's flux [Isa68b]; the time interval fixed in advance.

*What changes.* One more dimension; a T²-mirror class whose orbits degenerate on two axes, so that the reduced system
cannot be used there; a large black-hole background in place of small data, so that the trapped region and a spacelike
inner boundary are inside the domain; Cauchy data before the shell reaches the hole, and by [[thm:past-construction]]
data at past null infinity, which none of the three poses, rather than on a maximal slice or characteristic
hypersurfaces; one family of dust, not many.

*What the proof needs beyond theirs.* (1) An approximant of every order ([[thm:approximant]]), so that the nonlinear
terms are beaten by λ and only a linear estimate on the large background must be uniform; (2) the phase-shift identity
of [[ch:uniform-existence]], which removes the one large coefficient of that linear problem; (3) the exact commutator
[[eq:commutator]] on five-dimensional Vaidya, in which the mass drops out; (4) a compactly supported mollifier adapted
to a domain with boundary, in place of a Fourier projector ([[ch:inequalities]]); (5) a domain inside the horizon whose
time lines are spacelike, handled by changing only the independent variables to lines along a timelike vector field
([[ch:uniform-existence]]); (6) the constraints solved as a parabolic–hyperbolic evolution in r with no smallness and
no data imposed far out ([[ch:data]]); (7) a gauge hierarchy making D vanish to every order ([[ch:data]]).

### Scope {#sec:introduction-scope}

[[thm:main]], [[thm:past-construction]] and [[thm:bondi-law]] are made on D_T, on Ω and on the past domain of
[[thm:past-construction]], the last two bounded inside by r = a, a fixed distance inside x_K = 1; beyond them
[[thm:settling]] is stated outside the black hole, and its development also reaches inside the black hole after the
shell, up to the curvature boundary ([[prop:interior]]). Below the inner boundary the theorems are not silent: the
boundary sits at the curvature scale l5, which is arbitrary, and a smaller l5 puts every point with r > 0 and v ≤
v_end + T inside D_T, since r_q(v) = (√72 μ(v) l5²)^(1/4) tends to 0 with l5, the constants then depending on l5; at r = 0 the
limit itself is singular, its Kretschmann scalar being 72 μ²/r⁸ ([[prop:vaidya]]). The thresholds λ0, λ1 and δ exist by
the proofs and are not evaluated; [[prop:lambda0]] bounds λ0 above at a numerical point, and [[ch:explicit-constants]]
states where the explicit evaluation of λ1 and δ stops. A high-frequency theorem, whose expansion parameter is the
wavelength over the curvature length, does not apply at a prescribed wavelength of 10 l5; there existence holds where
the solution is the seed ([[thm:ten-l5]]). [[ch:scope]] collects these statements.

### Organisation of the paper {#sec:organisation}

[[part:statements]] sets up the class, the background, the domain, the gauge and the waves ([[ch:setting]]) and states
the theorems ([[ch:theorems]]).

[[part:approximant]] builds the approximate solution to every order by a two-scale expansion around the phase v
([[ch:approximant]]).

[[part:existence]] proves existence on Ω with remainder estimates uniform in λ: the inequalities on the slices
([[ch:inequalities]]), the linear structure, the phase-shift identity and the bootstrap ([[ch:uniform-existence]]), and
the exact data, the constraints being solved outward in r ([[ch:data]]).

[[part:remaining]] proves the statements on the boundary, the spheres' horizon and the mean mass
([[ch:horizon-mass]]), the construction from past null infinity ([[ch:past-construction]]) and the Bondi mass law
([[ch:bondi]]).

The stability theory of five-dimensional Schwarzschild–Tangherlini occupies five parts: the spectral family on bundles
([[part:stability]]), analysis on the compactified spacetime ([[part:stability-analysis]]), the Myers–Perry family and
the linear theory at low energy ([[part:stability-linear]]), forward solutions and their asymptotics
([[part:stability-forward]]), and the exterior, the nonlinear theorem, gluing and linear stability
([[part:stability-nonlinear]]).

[[part:settling]] proves [[thm:settling]] ([[ch:settling-proof]]) and then treats the solutions after the shell and
the reach of the theorem ([[ch:after-shell]]), the interior after the shell ([[ch:interior]]), the settling of g_λ's
own data ([[ch:own-data]]), and the linear solution in a Regge–Wheeler-type gauge ([[ch:rw-gauge]]) and in harmonic
gauge ([[ch:harmonic-structure]], [[ch:harmonic-rate]]).

[[part:constants]] gives explicit resolvent bounds on five-dimensional Tangherlini ([[ch:resolvent-bounds]]) and what
the proof of [[thm:settling]] makes explicit ([[ch:explicit-constants]]).

[[part:further]] treats two crossing dusts ([[ch:two-dusts]]), the class Einstein–null-dust system
([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data and the sign of the charge
([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]], [[ch:equality-edge]]), the threshold λ0 at a
numerical point ([[ch:lambda0]]), the prescribed wavelength 10 l5 ([[ch:ten-l5]]) and the scope ([[ch:scope]]).

[[app:standard-results]] states the results of the literature that the proofs use, each with its source, number and
page.
