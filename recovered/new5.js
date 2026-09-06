h2('5.  Excited Neighbourhoods and the Displacement Vector'));
B.push(p([t('Two quantities derived from the coordinates are used repeatedly in what follows, and one further expression is recorded for provenance. This section defines all three and states plainly which is which.')]));

B.push(h3('5.1  Neighbours and displacement'));
B.push(p([t('Each cell has two nearest neighbours reachable by a single excitation: one along the shell axis and one along the subshell axis,')]));
B.push(eq('Q₁ = (n+1, ℓ, k)          [shell excitation]','2'));
B.push(eq('Q₂ = (n, ℓ±1, k)          [subshell excitation]','3'));
B.push(p([t('with Q₂ taking ℓ+1 where the angular-momentum condition permits and ℓ−1 otherwise. The displacement from the midpoint of the excited pair back to the ground cell,')]));
B.push(eq('ΔQ  =  Q₀ − ½(Q₁ + Q₂)','4'));
B.push(p([t('is a static vector characterising the geometry of each cell\\'s immediate neighbourhood. It is the workhorse of Part I: Section 6 shows that its direction sorts the elements into three classes, Section 17 uses those classes in stating the adjacency result, and Section 23.1 reports that they separate hydride formation enthalpies at p = 0.010 — the only case in this paper of a purely geometric construction tracking a measured quantity unaided. ΔQ is a difference of coordinates and is therefore invariant under any translation of the origin, a point Section 8 returns to.')]));

B.push(h3('5.2  Configuration-space spread'));
B.push(p([t('Writing an element\\'s state as a superposition over its ground cell and the two neighbours, with weights c₀, c₁, c₂ summing in square to unity, the expectation position and variance in configuration space are')]));
B.push(eq('⟨Q⟩ = Σ |c|² · (n, ℓ, k)     and     σ² = ⟨Q²⟩ − ⟨Q⟩²','5'));
B.push(p([t('The variance measures how far an element\\'s weight is distributed across its accessible cells. At maximum excitation it takes the value ½ for every element except hydrogen and helium, for which the two neighbours coincide and σ² vanishes; that degeneracy is the content of Class A in Section 6. Like ΔQ, σ² is built from coordinate differences and is origin-independent.')]));

B.push(h3('5.3  A time-dependent expression, recorded for provenance'));
B.push(p([t('The framework from which this paper developed was originally organised around a time-dependent form of Equation (5). Requiring normalisation at all t, ground-state occupancy at t = 0, and sinusoidal evolution at a base frequency Ω gives c₀ = cos(Ωt) and c₁ = c₂ = sin(Ωt)/√2; phase-shifting by π/2 gives the emission mirror, and combining the two yields')]));
B.push(eq('Ψ±(t)  =  √2 · sin(Ωt + π/4) · Σ(n,ℓ,k)∈Λ  |n, ℓ, k⟩','6'));
B.push(p([t('designated the Lach elemental field equation. Its internal consistency was checked symbolically and holds exactly: the normalisation cos²(Ωt) + 2·[sin(Ωt)/√2]² = 1 is identically satisfied, as is the identity cos(Ωt) + sin(Ωt) = √2 sin(Ωt + π/4) that produces the combined form.')]));
B.push(p([t('Its status in this paper is limited, and the limits should be stated at the outset rather than discovered later. Equation (6) is a construction on the lattice, not a solution of a Hamiltonian derived from physical potentials. The parameter Ω is formal; nothing here establishes a correspondence between Ω and a measurable frequency in any material. And the expression is element-independent — the summation carries no element label and the prefactor is common to all, so every element shares a single envelope and the equation distinguishes none of them. Nothing in Parts II through V depends on it. It is retained because it is part of the provenance of the construction and because a time-dependent formulation is the natural place from which a predictive extension of the lattice would have to begin; whether such an extension is possible is not addressed here, and Part V gives reasons for caution. Readers interested only in the results may treat Sections 5.1 and 5.2 as the operative content of this section.')]));

B.push(