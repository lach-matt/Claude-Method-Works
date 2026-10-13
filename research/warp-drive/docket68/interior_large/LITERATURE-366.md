# What the literature says about stage C (item 366)

M, item 366: "Before we do anymore, please search the web for models, equations, insights, anything regarding the
current topic of the workload that may change our approach". Searched 2026-10-13, no runs made. The topic is evolving
the large RSII hole's interior (FW's static hole continued to s = r^2 < 0) toward its singularity: the slicing, the
gauge source, the brane as a boundary of a hyperbolic evolution, and what is known of such interiors.

**Access.** Web search (eleven queries). Full text read through the alphaXiv connector for eight papers. Direct fetches
of arxiv.org failed (DNS), so every quote below comes from the connector's text of the arXiv PDF. READ marks a verbatim
quote from a paper's full text. "Search summary" marks something seen only in a search result and not opened.
"Deduced" marks the board's own inference.

## The findings

**L1. Wang and Choptuik met our brane failure and fixed it.** They ran the only full dynamical RSII evolution found:
generalized harmonic, finite differences, a brane-confined scalar collapsing to a hole, and excision inside the
apparent horizon. Sources: arXiv 1604.04832; Wang's thesis, arXiv 1505.00093.
READ, 1604.04832 sec. II: "while the damping term introduced in [16] suffices to damp the constraint-violating modes in
the bulk, it can not control the corresponding modes appearing at and near the brane. We solve this problem by
explicitly enforcing the constraints at the brane."
READ, thesis sec. 5.4.1 (p. 117): "for the braneworld, it turns out that these damping terms are not sufficient -- the
constraints do not converge to zero as the resolution increases. In fact, the residuals of the constraints almost stay
the same when the resolution increases." That is C2's step 3 at mu = 50 (Nx = 28 against 40).
READ, thesis sec. 5.4.2 (pp. 118-120): "should h^mu = h^mu can be equivalently expressed by setting the values of
eta_tz,z, eta_rz,z and eta_zz,z, which in principle can serve as the boundary conditions for eta_muz". It continues:
"In addition, we impose the perpendicular gauge at the brane (eta_tz|z=l = eta_rz|z=l = 0)". On how both are imposed:
"Imposing two boundary conditions on one function is achieved by the following trick ... eta_tz = (z - l) xi^t". And
the result: "It turns out that this method works well, and there is no need to use special damping."
READ, thesis eq. (3.51)-(3.52): their source is tensorial, h^b = -(Gamma^b - Gammabar^b) g, built on a background
metric gbar. That is our Einstein-DeTurck form with a reference metric, so their cure applies to our system as it stands.
READ, thesis eq. (5.25)-(5.26), a weaker fallback: multiply only the trace term of the damping by F = z^n/(z^n - c l^n),
with n = 4 and c = 0.99. They report "the constraints converged at the expected order".
*Bearing (deduced).* Our brane rows impose Israel (on T, S, A), xi^x = 0 and F = 0. The tangential component of the
constraint is left to Codazzi's Robin condition, which holds only in the continuum: the brane node is not evolved. Wang
and Choptuik impose every component. In our variables that means writing F = (1 - x) Fhat, so F = 0 holds identically,
and adding the row xi~^s = 0 at the brane, which fixes Fhat there. **This changes the approach**: it targets the
brane-localised, non-convergent violation that ended every driver run at mu = 50.

**L2. A time coordinate that runs to infinity at the singularity is the right kind, and harmonic time is one.**
Garfinkle, "Harmonic coordinate method for simulating generic singularities", gr-qc/0110013.
READ, p. 1: "The solution to this difficulty is to choose a time coordinate that tends to infinity as the singularity is
approached. In this way, the simulation is not forced to end at finite coordinate time, the whole spacetime up to the
singularity is covered". The Gowdy time "(minus the logarithm of the area of the symmetry T^2s) is also harmonic".
READ, p. 5: "While harmonic coordinates are singularity avoiding [3] they are just barely so and come arbitrarily close
to a singularity."
READ, p. 2, on gauge sources: "I know of no systematic way to find appropriate source terms and expect that in the cases
where they are needed, one will have to resort to a trial and error method".

**L3. Harmonic slicing is the marginal case. Our chart behaves as a strongly avoiding one.** Alcubierre, "Hyperbolic
slicings of spacetime: singularity avoidance and gauge shocks", gr-qc/0210050.
READ, sec. II A, eq. (11): with f = 1 and zero shift, alpha = h(x^i) gamma^(1/2) along the normals.
READ, sec. III: the summary for f = A alpha^n and a singularity of order m runs as follows. "For n < 0 we have strong
singularity avoidance. For n = 0 and mA >= 1 we have marginal singularity avoidance. For both n > 0, and n = 0 with mA <
1, we do not have singularity avoidance". And: "In the particular case when we have a singularity of order m = 1, then
harmonic slicing (n = 0, A = 1) marks the boundary between avoiding and reaching the singularity."
*Bearing (deduced).* Vacuum Kasner in any dimension has gamma^(1/2) proportional to tau, since the exponents sum to 1.
So m = 1, and pure harmonic time approaches the five-dimensional singularity as its time goes to infinity. B6 found the
DeTurck lapse falling as |s|^-2.1 while the spatial metric stays finite: g_tautau, g_thetatheta and g_xx all tend to
finite limits under B6's power laws in u. The lapse therefore collapses while the volume element does not, which is
Alcubierre's strong avoidance. The slices freeze at a limit surface, as maximal slicing freezes at r = 3M/2 in
Schwarzschild (search summary, gr-qc/9706046). Pure harmonic time cannot do this: alpha proportional to
gamma^(1/2) can vanish only where the volume does, at the singularity. What separates the DeTurck time from harmonic
time is the reference metric's pull Fbar^s. **This changes the approach**: the slicing to try is pure harmonic time,
h^s = -Fbar^s (C1's wF = 1 with mu = 0), switched on smoothly. The only earlier wF = 1 runs (`gauge_16`, `gauge_16c`)
carried the damping-on-xi fault and the old brane rows, so harmonic time has not yet had a valid test.

**L4. Our lapse driver is Pretorius's kind.** Pretorius, "Evolution of binary black hole spacetimes", gr-qc/0507014.
READ, p. 1: the code has "a time slicing that slows down the 'collapse' of the lapse that would otherwise occur in pure
harmonic time slicing".
READ, eq. (3): "H_t = -xi_1 (alpha - 1)/alpha^eta + xi_2 H_t,nu n^nu, H_i = 0".
READ, p. 2: "kappa ~ 1.25/M_0, xi_1 ~ 19/M_0, xi_2 ~ 2.5/M_0, eta = 5 (these parameters did not need to be fine tuned)".
*Bearing (deduced).* Our h^s = mu (Nst c - N)/N^3 is the same restoring force, with N^-3 in place of alpha^-5. Pretorius
also gives H_t a response time through xi_2 instead of setting it algebraically. He used the driver with excision, not
to approach a singularity, and his aim (stop the lapse collapsing) is the one L3 says should not be ours. Keep the
driver only as a fallback to L3, with the xi_2 lag as its gentler form.

**L5. Damping cannot stop violations entering through a boundary; the boundary must be constraint-preserving.**
Lindblom, Scheel, Kidder, Owen, Rinne, "A new generalized harmonic evolution system", gr-qc/0512093.
READ, sec. 4: "These modifications will do nothing, however, to prevent the influx of constraint violations through the
boundaries of the computational domain. Constraint-preserving boundary conditions are needed to prevent this".
READ, eq. (62): boundary data are imposed on the incoming characteristic fields by
d_t u = D_t u + v (d_perp u - d_perp u|_BC). This is how a pseudospectral code avoids imposing values strongly.
Search summary (Gottlieb and Hesthaven's review; Funaro and Gottlieb): penalty boundary terms and spectral filtering
are the standard stabilisers for Chebyshev collocation of hyperbolic problems.
*Bearing.* This is the principle behind L1. If L1's rows still leave a boundary instability, imposing the brane rows by
penalty, or filtering the top Chebyshev modes, is the next thing to try.

**L6. Gauge conditions built from derivatives need gauge drivers.** Lindblom, Matthews, Rinne, Scheel, arXiv 0711.2084
(search summary): sources depending on first derivatives (Bona-Masso slicing, K-freezing) are promoted to evolved
fields, keeping the system hyperbolic. *Bearing:* needed only if a Bona-Masso f < 1 slicing is wanted, to reach the
singularity at finite time (L3). Pure harmonic time (L3) and our algebraic h need none.

**L7. Interiors have been evolved to r = 0 with the areal radius as the coordinate.** Chesler, "Numerical evolution of
the interior geometry of charged black holes", arXiv 2001.02788.
READ, sec. II: "We employ infalling Bondi-Sachs coordinates". READ, sec. IV A: "we employ z = log r as a radial
coordinate"; "We employ pseudospectral methods with domain decomposition with 20 equally spaced domains in z"; "when
integrating very close to r = 0, the equations of motion become very stiff ... we evolve forward in v using Matlab's
stiff ODE solver, ode15s"; "r_min = 10^-8". READ, sec. V: the Kasner exponents are read off invariant ratios P_1 and
P_2 of curvature components, which are "invariant under coordinate transformations that only mix time and radius".
*Bearing.* (a) The invariant Kasner diagnostic can be adopted now. (b) A characteristic code with an areal coordinate
puts the singularity at a known coordinate place. It would be a new code, with a brane as a timelike boundary of a null
evolution, so it is the route if L1 to L3 fail.

**L8. Near a singularity, spikes demand resolution; our symmetry may forbid them.** Garfinkle and Pretorius, "Spike
behavior in the approach to spacetime singularities", arXiv 2010.01399.
READ, sec. II: they use "the scale invariant tetrad method of Uggla et al [9] ... with constant mean curvature slicing";
"the singularity is approached as t -> -infinity". READ, sec. VI: "Spikes are a significant challenge for numerics, due
to the need to resolve small scale features at so many points as to make adaptive mesh refinement impractical". Their
1D runs use dx = 2 pi/2500.
Search summary (Isenberg and Moncrief; Berger and Moncrief): the polarised Gowdy approach is velocity dominated, and
spikes appear in the unpolarised case.
*Bearing (deduced; not proven for five dimensions with S^2 orbits).* Our metric on the symmetry orbits (tau, theta,
phi) is diagonal; F lives in the (s, x) orbit space. That is the analogue of polarised Gowdy, so a monotonic local
Kasner approach without spikes is the expectation. Any spike would sit at an isolated x, in one spatial dimension, where
resolution can reach it.

**L9. An exact brane-localised black hole interior exists to test against.** Emparan, Horowitz and Myers' AdS4
C-metric (hep-th/9911043, hep-th/9912135), as presented in Emparan, Frassino and Way, "Quantum BTZ black hole",
arXiv 2007.15999.
READ, eq. (2.1)-(2.3): ds^2 = l^2/(l + x r)^2 (-H dt^2 + dr^2/H + r^2 (dx^2/G + G dphi^2)), with H(r) = r^2/l_3^2 +
kappa - mu l/r and G(x) = 1 - kappa x^2 - mu x^3.
READ, eq. (2.10): "the surface x = 0 is always totally umbilic. That is, that the extrinsic curvature K_ab and induced
metric h_ab satisfy K_ab = -(1/l) h_ab".
*Bearing (deduced).* This is our Israel condition, one dimension down: a vacuum brane in an AdS bulk with a localised
hole. The bulk metric is closed form inside the horizon too, down to r = 0, where it is singular for mu not 0. The flat
brane is l_3 -> infinity. **This changes the approach**: porting the interior pipeline (static ansatz continued inside,
brane rows, gauge, damping) to this four-dimensional problem gives a test whose answer is known. That test covers the
interior, the brane treatment and the approach to the singularity, and it can be run before any RSII interior is trusted.

## Not found

No paper evolving a braneworld black hole's interior toward its singularity. Wang and Choptuik, the only dynamical RSII
evolution found, excise inside the apparent horizon. No paper on a DeTurck reference metric degenerating in a
Lorentzian evolution. One result was seen only as a search summary: harmonic slices of Schwarzschild covering the whole
spacetime (doi 10.1103/PhysRevD.52.6182). An absence in these searches is not a finding of novelty.

## What would change, in order (the board's proposal; nothing run)

1. **Brane rows (L1, L5).** Add xi~^s = 0 at the brane, with F = (1 - x) Fhat replacing the bare F = 0 row. The test is
   the mu = 50 pair at Nx = 28 and 40 that failed to converge in C2: it should converge.
2. **Slicing (L2, L3).** Pure harmonic time, h^s = -Fbar^s, ramped in from the old chart, with the new brane rows. One
   cheap check first, on runs already made: whether N/gamma^(1/2) stays constant along the normals in the old chart.
   That measures how far the DeTurck slicing departs from harmonic (L3).
3. **Validation (L9).** The AdS4 C-metric brane hole, with the same pipeline, against the exact interior.
4. **Diagnostics (L7, L8).** Invariant Kasner exponents; resolution checks for spikes near the singularity.
5. **Fallbacks.** Pretorius's lagged driver (L4); penalty boundaries and filtering (L5); a characteristic code with an
   areal coordinate (L7).

What stays: the formulation, Einstein-DeTurck with a reference metric, which L1 shows to be the family that worked for
the dynamical RSII problem. Also the bulk damping kap [n_(a xi_b) - (1/3) g n.xi].

## Sources

Wang and Choptuik, arXiv 1604.04832. Wang, thesis, arXiv 1505.00093. Garfinkle, gr-qc/0110013. Alcubierre,
gr-qc/0210050. Pretorius, gr-qc/0507014. Lindblom et al., gr-qc/0512093. Lindblom, Matthews, Rinne, Scheel, arXiv
0711.2084 (search summary). Chesler, arXiv 2001.02788. Garfinkle and Pretorius, arXiv 2010.01399. Emparan, Frassino and
Way, arXiv 2007.15999; Emparan, Horowitz, Myers, hep-th/9911043 and hep-th/9912135. Beig and O Murchadha,
gr-qc/9706046 (search summary). Funaro and Gottlieb; Gottlieb and Hesthaven (search summaries).
